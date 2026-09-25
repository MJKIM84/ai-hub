(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-67
- date: 2026-09-25
- run_type: category_link (대분류 연결)
- 대상: 대분류 F. 도입·검증·유지관리 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-25-67/target.json

```json
{
  "run_id": "2026-09-25-67",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 67,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "F. 도입·검증·유지관리",
    "category_letter": "F"
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

### runs/2026-09-25-67/research.json

```json
{
  "run_id": "2026-09-25-67",
  "date": "2026-09-25",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "F. 도입·검증·유지관리"
  },
  "gaps": [
    "F. 도입·검증·유지관리 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태",
    "E. 협업·현장 운영 페이지가 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈, E ↔ 21. 온보딩·설정·현장 시운전, E ↔ 24. 자산·소프트웨어 수명주기 관리를 '근거 없음'으로 남김(이번 실행에서도 근거 미확보)",
    "B. 공통 정보·환경 모델 페이지가 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리와의 연결을 '아직 다루지 않은 연결'로 둠 — 이번 실행 f11·f15 가 근거가 될 수 있음",
    "G. 안전·보안·지능·거버넌스 쪽 세부영역 페이지(25~28)가 seed 이거나 심화 전이라 G 연결은 F 쪽 근거에 기댐"
  ],
  "research_questions": [
    "새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]",
    "제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]",
    "21. 온보딩·설정·현장 시운전이 등록·설정하는 정보(팩트시트, 어댑터 설정, 경로망·지도 정합)는 B. 공통 정보·환경 모델과 C. 연결·실행 기반, D. 계획·최적화의 어느 세부영역으로 넘어가는가?",
    "22. 시뮬레이션·예측용 디지털 트윈은 A. 업무·공급망 설계(처리능력·성과)와 D. 계획·최적화(배정·경로망)의 어떤 결정을 가정한 미래로 실험하며, 8. 실시간 세계 상태·데이터 일관성과 어떻게 구분되는가?",
    "23. 시험·형식 검증·벤치마크는 C. 연결·실행 기반의 인터페이스·설비 연동, D. 계획·최적화의 교착·경로 알고리즘, E. 협업·현장 운영의 장애 대응을 어떤 시험·검증으로 잇는가? (oq-055, oq-058, oq-087 관련)",
    "24. 자산·소프트웨어 수명주기 관리의 지도·펌웨어 버전과 배터리 열화 정보는 B. 공통 정보·환경 모델, C. 연결·실행 기반, D. 계획·최적화, G. 안전·보안·지능·거버넌스의 어느 규칙·제약과 맞물리는가? (oq-090, oq-091 관련)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS) 운영의 여러 결정 문제가 미치는 효과를 연구하기 위한 이산 사건 시뮬레이션 프레임워크다.",
      "tag": "사실",
      "source_ids": [
        "ref-101"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RAWSim-O README: RMFS 의 결정 문제 효과를 연구하는 이산 사건 시뮬레이션 프레임워크 (재인용: 22. 시뮬레이션·예측용 디지털 트윈 페이지 7절·A 대분류 페이지) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 및 D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 22. 시뮬레이션·예측용 디지털 트윈: Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다.",
      "tag": "사실",
      "source_ids": [
        "ref-398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RMFS 결정 규칙 시뮬레이션 연구에서 피킹 주문 배정 규칙이 단위 처리량에 큰 영향(모델·시뮬레이션 조건의 저자 보고) (재인용: 2026-09-25-56)",
      "as_of": "2019",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "연계 대상: 22. 시뮬레이션·예측용 디지털 트윈의 성수기 시나리오 입력(주문·물동량 전망)은 A. 업무·공급망 설계의 1. 주문·업무 시스템 연계를 거쳐 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 수요예측 자체는 분류 원문 9장의 상위 업무 시스템 경계에 속한다.",
      "tag": "추정",
      "source_ids": [
        "ref-521"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Le·Fan(2024)은 물류·공급망 디지털 트윈 개념 틀을 제안하고 실데이터 검증 논문이 소수라고 보고 (재인용: 2026-09-25-56)",
      "as_of": "2024",
      "flow_step": "피킹",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ 21. 온보딩·설정·현장 시운전: 다중 AGV 도입이 정밀 지도 작성·좌표 지정·수작업 경로망 설계로 오래 걸린다는 연구와 설치 기간을 6개월에서 2개월로 줄일 수 있다는 과제 측 보고가 있어, 온보딩 기간이 증차한 로봇이 처리능력으로 바뀌는 시점을 좌우하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-217",
        "ref-265"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Beinschob 외(2017) 도입 지연 원인 / PAN-Robots 설치 기간 6→2개월은 과제 측 보고값, 비교 조건 미확인 (재인용: 2026-09-25-52)",
      "as_of": "2017",
      "flow_step": "적치",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ 23. 시험·형식 검증·벤치마크: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있어 공정 모델의 형식적 점검이 형식 검증과 이어질 것으로 보이나, 물류 로봇 공정 적용 사례는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-121"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Blondin 외, The complexity of soundness in workflow nets (LICS 2022) (재인용: 2026-09-25-29, A 대분류 페이지)",
      "as_of": "2022",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지 ↔ 21. 온보딩·설정·현장 시운전: IDTA 02020 능력 기술(Capability Description) 서브모델은 공정이 요구하는 능력과 자원이 제공하는 능력을 비교하게 하고, 능력을 속성·제약(전제조건·순서)·스킬로 구조화해 자원의 매칭과 시운전을 돕는다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-229"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: capability 는 'implementation-independent specification of a function in industrial production'; 요구·제공 능력 비교, properties·constraints·skills 구조",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "Vieira da Silva 외(2024-06)는 자연어 능력 설명에서 대규모 언어 모델(LLM)을 이용해 능력 온톨로지를 생성하는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions (arXiv 2406.07962) (재인용: 2026-09-25-52)",
      "as_of": "2024-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 21. 온보딩·설정·현장 시운전: 분류 원문 8장 교차 규칙이 매뉴얼 해석을 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 AI 연구 방법으로 두므로, LLM 기반 능력 온톨로지 생성은 새 로봇 등록 작업을 줄이는 방법으로 두 대분류를 잇는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-465",
        "ref-229"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "교차 규칙(분류 원문 8장)과 f6·f7 의 결합에 따른 이 위키의 추론. 온보딩 현장 적용 사례는 미확인",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 RMF 좌표계 사이 변환을 위한 기준 좌표(대응 경유점)를 설정에 두고, 대응 경유점을 최소 4개 둘 것을 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A minimum of 4 matching waypoints is recommended.\"",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "21. 온보딩·설정·현장 시운전 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델, C. 연결·실행 기반의 10. 설비·건물 시스템 연동, D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF traffic-editor 는 차선·경유점·충전소·주차 지점·문·승강기·층과 기준점(fiducial)을 이용한 층간 정렬을 주석하게 하고, 주석한 그래프는 building_map_generator 로 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문: annotated Graphs are exported as navigation graphs using the building_map_generator, used by rmf_fleet_adapters for path planning",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 지도 내려받기·활성화·삭제 즉시 동작(downloadMap·enableMap·deleteMap)을 두고 같은 mapId 에서는 한 번에 한 버전만 활성화하게 하며, 상태 스키마는 로봇이 mapId·mapVersion·mapStatus(ENABLED·DISABLED)를 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"There shall only be one version of maps with the same mapId enabled at a time\" / state.schema maps: mapId, mapVersion, mapStatus(ENABLED, DISABLED)",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "시작 조건"
    },
    {
      "id": "f12",
      "claim": "분류 원문이 6. 지도·공간·위치 모델에 '지도 버전 관리'를, 24. 자산·소프트웨어 수명주기 관리의 정의에 '지도 버전'을 함께 넣고 VDA 5050 이 지도 배포·활성화를 관제의 지시로 두므로, 지도 버전의 내용 정의는 B. 공통 정보·환경 모델 쪽, 배포·활성화 시점 조율과 이력 관리는 F. 도입·검증·유지관리 쪽이 맡는 분담이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 6번 주석·24번 한 줄 정의와 VDA 5050 지도 배포 즉시 동작에서 끌어낸 이 위키의 추론",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Kritzinger 외(2018)는 제조 분야 문헌을 검토해 물리 객체와 디지털 객체 사이 데이터 흐름의 자동화 정도에 따라 디지털 모델·디지털 섀도·디지털 트윈을 구분했다.",
      "tag": "사실",
      "source_ids": [
        "ref-291"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Digital Twin in manufacturing: A categorical literature review and classification (IFAC 2018) — 제조 대상 분류 (재인용: 2026-09-25-32)",
      "as_of": "2018",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 8번은 현재 상태를 표현하고 22번은 그 모델을 이용해 가정한 미래를 실험한다는 분류 원문 구분에 따라, 22번은 8번의 현재 상태(로봇·설비·배터리 상태)를 시나리오 초기값으로 받는 쪽이 될 것으로 보이며, 근거 분류 자료가 물류가 아닌 제조 대상이라는 한계가 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-291",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 7장 구분 + 제조 대상 디지털 섀도·트윈 구분 + Open-RMF 시뮬레이션 문서에서 끌어낸 추론",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 상태 스키마는 충전 상태(stateOfCharge), 배터리 건강 상태(batteryHealth, 0~100%), 현재 충전량으로 추정한 도달 거리(range), 충전 여부(charging)를 로봇이 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema batteryState: stateOfCharge, batteryHealth, range('Estimated reach with current State of Charge in meter'), charging",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 및 C. 연결·실행 기반의 10. 설비·건물 시스템 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션 문서에 따르면 building_map_generator 는 traffic-editor 로 주석한 건물 지도에서 Gazebo 시뮬레이션 세계와 주행 그래프를 만들고, 문·승강기 플러그인, 워크셀을 흉내 내는 TeleportDispenser·TeleportIngestor, 여러 플릿 어댑터의 승강기 요청을 조율하는 lift_supervisor 를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md: building_map_generator 가 .building.yaml 에서 월드·주행 그래프 생성; door·lift 플러그인, TeleportDispenser/TeleportIngestor, lift supervisor",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Sommer 외(2023)는 건물 환경 스캔과 객체 검출을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-241"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Automated generation of digital twin for a built environment using scan and object detection as input for production planning (2023) — 생산 계획 대상 (재인용: 2026-09-25-56)",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: VDA 5050 3.0.0 은 팩트시트를 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보로 두고, 초기 설정과 관제–이동로봇 능력 사이의 지속적인 호환성 평가에 쓰도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Factsheet shall be used to support initial configuration and ongoing compatibility assessment between fleet control and mobile robot capabilities.\"",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "VDA 5050 팩트시트 스키마는 적재 명세(loadSpecification.loadSets), 로봇 구성의 버전 목록(mobileRobotConfiguration.versions, 예: softwareVersion), 충전 설정(batteryCharging: criticalLowChargingLevel·minimumDesiredChargingLevel·maximumDesiredChargingLevel·minimumChargingTime)을 담아, 한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화에 함께 쓰인다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "factsheet.schema: loadSpecification.loadSets, mobileRobotConfiguration.versions(softwareVersion 등), mobileRobotConfiguration.batteryCharging.criticalLowChargingLevel 외",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 설정은 최대 선·각속도와 가속도, 수행 가능한 작업 유형(loop·delivery·clean), 로봇 외곽 반경, 배터리·재충전 임계값, 제조사 관제 API 연결 정보(주소·계정)를 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "integration_fleets_adapter_tutorial.md: speed limits, task capabilities, robot profiles, battery params, recharge thresholds, fleet manager prefix/username/password",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "수행 자원"
    },
    {
      "id": "f21",
      "claim": "22. 시뮬레이션·예측용 디지털 트윈·23. 시험·형식 검증·벤치마크 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 시뮬레이션 문서는 시뮬레이션 속 로봇이 배터리 소모나 충돌 비용 없이 장시간·가속 조건으로 드문 예외 상황을 시험할 수 있고, 장시간 시뮬레이션이 배치 전 시설 소유자의 확신을 높인다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Long running simulations can instill confidence in facility owners prior to deployment.\"",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션의 slotcar 플러그인은 경로·모드 요청을 받아 레일식으로 움직이고 센서 기반 주행 스택 없이 로봇 상태를 발행하는 전체 제어(full control) 로봇 모델이다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md: slotcar 는 rail-like navigation 으로 full control 로봇을 모사, 센서 기반 주행 스택 불필요",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "slotcar 같은 단순화 모델은 제조사 관제·로봇 고유 거동을 재현하지 않으므로, 9. 로봇·제조사 관제 연동 방식(전체 제어·신호등·읽기 전용)과 제조사별 거동 차이가 22. 시뮬레이션·예측용 디지털 트윈의 처리량 예측 오차 원인이 될 것으로 보인다(oq-086).",
      "tag": "추정",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f22 의 단순화 모델 설명에서 끌어낸 추론. 오차 크기 자료 미확인",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 오류를 CRITICAL 수준과 오류 필드 참조로 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL'\"",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "예외·성과"
    },
    {
      "id": "f25",
      "claim": "C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성 ↔ 24. 자산·소프트웨어 수명주기 관리: ROS 2 관리형 노드는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate 같은 전이를 두어, 감독 도구가 구성요소 준비를 확인한 뒤 실행을 허용하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-364"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ROS 2 Design node_lifecycle: managed node 상태 기계 (재인용: 2026-09-25-38, C 대분류 페이지)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "C. 연결·실행 기반의 9. 로봇·제조사 관제 연동·12. 명령·작업 실행의 신뢰성 ↔ 23. 시험·형식 검증·벤치마크: 공개 개인 프로젝트 vda5050-sim 은 VDA 5050 3.0.0 주문 수명주기·동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을, vda5050-lab 은 MQTT 기록에서 반복 주문 id·재연결·취소 불일치를 진단한다고 README 에 적으며, 둘 다 VDA·VDMA 공식 적합성 시험이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-407",
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 README 의 자기 기술 (재인용: 2026-09-25-38, C 대분류 페이지)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "OTTO by Rockwell Automation 은 자사 AMR 이 여러 관제 업체와 VDA 5050 인증을 마쳤다고 2026-04 발표했으나, 인증의 시험 항목은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-608"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Idealworks·NAiSE·SYNAOS 와 VDA 5050 인증 완료 발표 (재인용: 2026-09-25-59)",
      "as_of": "2026-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f28",
      "claim": "연계 대상: ros2_fault_injection 은 오도메트리·레이저 스캔·IMU·점군 같은 센서 신호와 속도 명령을 조작하는 로봇 수준 장애 주입 도구이며, 23. 시험·형식 검증·벤치마크에서 ROP 쪽 장애 주입은 같은 프록시 방식을 C. 연결·실행 기반의 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-601"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "README 기준 센서 신호 장애 주입과 Twist 명령 조작 (재인용: 2026-09-25-59). ROP 적용은 추론",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 22. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망(roadmap)을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-267"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (재인용: 2026-09-25-56)",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 23. 시험·형식 검증·벤치마크: Stern 외(2019)는 MAPF 의 가정·목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했으나, 그 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058).",
      "tag": "사실",
      "source_ids": [
        "ref-186"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks (2019) (재인용: 2026-09-25-59)",
      "as_of": "2019-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "Yan 외(2026-02)는 기존 MAPF 연구가 단순한 운동 모델과 완전한 실행·통신을 가정한다고 지적하고, 플릿 관리 시스템 안에서 계획 시점·방법·복구 설계 선택을 비교하는 시험대(LSMART)를 제안해 D. 계획·최적화의 경로 알고리즘과 23. 시험·형식 검증·벤치마크를 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LSMART 와 지속형 AGV 플릿 관리 설계 선택 연구(arXiv 2602.15721, 프리프린트) (재인용: 2026-09-25-59)",
      "as_of": "2026-02-17",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "von Berg 외(2026-05)는 창고 물류 AGV 의 교착 회피를 전이 시스템 인코딩과 BDD 로 분석한 사례 연구를 발표해, 15. 다중 로봇 경로·교통 관리 — MAPF 의 교착 문제가 23. 시험·형식 검증·벤치마크의 형식 검증 대상이 됨을 보인다(계산 규모 한계는 oq-088).",
      "tag": "사실",
      "source_ids": [
        "ref-609"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "BDD-Based Deadlock Avoidance for AGVs in Warehouse Logistics (FM 2026 사례 연구) (재인용: 2026-09-25-59)",
      "as_of": "2026-05",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 23. 시험·형식 검증·벤치마크: Lott·Honary(2026-09 프리프린트)는 분산 작업 배정기 6종을 패킷 손실·페이딩 같은 통신 저하 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-493"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark (재인용: 2026-09-25-55, D 대분류 페이지)",
      "as_of": "2026-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ 24. 자산·소프트웨어 수명주기 관리: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 작업 배정·충전 일정을 정하는 연구(2026-03, 프리프린트)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots (arXiv 2603.22731) (재인용: 2026-09-25-61)",
      "as_of": "2026-03",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f35",
      "claim": "로봇이 보고하는 batteryHealth 가 낮아지면 같은 충전 상태에서도 도달 거리(range)가 짧아질 수 있어, 24. 자산·소프트웨어 수명주기 관리의 배터리 열화 정보가 D. 계획·최적화의 13. 작업 배정 — MRTA·16. 공용 자원·충전·에너지 최적화의 제약 입력이 되는 것으로 보인다(물류센터 실측 자료 미확인).",
      "tag": "추정",
      "source_ids": [
        "ref-051",
        "ref-403"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15 의 상태 필드와 f34 의 연구에서 끌어낸 추론 (재인용: 2026-09-25-61 출하 시나리오)",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f36",
      "claim": "E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ 23. 시험·형식 검증·벤치마크: NIST ARIAC 2025 문서는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급(고우선) 주문을 과제로 두어 설비·로봇 장애와 긴급 주문 대응을 평가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A specified vacuum gripper will fail during grasp attempts.\" (challenges.rst, ARIAC 2025 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f37",
      "claim": "ARIAC 같은 장애 과제 정의와 장애 주입 도구를 결합하면, 20. 예외 복구·재계획·업무 연속성의 재배정·수동 전환·제한 운영 동작을 업데이트마다 다시 돌리는 회귀 시험 시나리오로 만들 수 있을 것으로 보이나, 물류 오케스트레이션에 적용해 공개한 사례는 확인되지 않았다(oq-087).",
      "tag": "추정",
      "source_ids": [
        "ref-528",
        "ref-601"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36·f28 에서 끌어낸 추론 (재인용: 2026-09-25-59 피킹 회귀 시험 시나리오)",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f38",
      "claim": "E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ 23. 시험·형식 검증·벤치마크: ASTM F3499-21 은 자율 무인 지상 차량(A-UGV)의 도킹 성능을 확인하는 시험 방법이며, 그 결과를 로봇팔 파지 허용 오차와 잇는 기준은 확인되지 않았다(oq-063).",
      "tag": "사실",
      "source_ids": [
        "ref-204"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Standard Test Method for Confirming the Docking Performance of A-UGVs (2021) (재인용: 2026-09-25-60, E 대분류 페이지)",
      "as_of": "2021",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 24. 자산·소프트웨어 수명주기 관리: Lei 외(2025)는 산업용 로봇의 고장 모드·데이터 수집·모델 기반과 데이터 기반 진단을 상태 기반 정비 관점에서 정리한 검토를 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-553"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Condition monitoring and fault diagnosis of industrial robots: A review (Sci China Tech Sci 68, 2025) (재인용: 2026-09-25-61)",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 23. 시험·형식 검증·벤치마크: ROSMonitoring 은 ROS 시스템의 런타임 검증 프레임워크로, 운영 중 감시가 사전 시험을 보완하는 연결 지점이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-602"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ROSMonitoring: a Runtime Verification Framework for ROS — README (재인용: 2026-09-25-59)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하며, 운용 구역 준비를 부속서 A 에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 3691-4:2023 소개 (재인용: 2026-09-25-52·59·63). 세부 시험 항목 미확인",
      "as_of": "2023-06",
      "flow_step": "적치",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "연계 대상: 국내에는 바퀴형 서비스 로봇의 이동 성능 시험방법 KS B ISO 18646-1 과 한국로봇산업진흥원의 시험평가 서비스가 있어, 로봇 자체 성능 시험은 시험기관 쪽이고 23. 시험·형식 검증·벤치마크의 ROP 몫은 그 결과를 등록·배정 조건으로 받는 쪽으로 보인다(oq-089).",
      "tag": "추정",
      "source_ids": [
        "ref-606",
        "ref-607"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "KSSN 표준 정보와 KIRIA 시험평가 페이지 (재인용: 2026-09-25-59). 오케스트레이션 수준 시험 포함 여부 미확인",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "한국산업기술시험원(KTL)과 통합물류협회가 물류로봇 시험인증 협력을 강화하기로 했다고 2026-07 보도되어, 국내 물류로봇 시험·인증 체계가 23. 시험·형식 검증·벤치마크와 28. 표준·상호운용성·다사업자 거버넌스를 잇는 후보가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-466"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "부산일보 2026-07-24 기사(1차 출처 미확인) (재인용: 2026-09-25-52)",
      "as_of": "2026-07-24",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ 24. 자산·소프트웨어 수명주기 관리: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템(IACS) 환경의 패치 관리를 다루는 기술 보고서다.",
      "tag": "사실",
      "source_ids": [
        "ref-554"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEC TR 62443-2-3:2015 Patch management in the IACS environment (재인용: 2026-09-25-61)",
      "as_of": "2015-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f45",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 24. 자산·소프트웨어 수명주기 관리: 로봇 시스템 위험성평가 가이드는 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로, 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 미확인이다(oq-092, oq-093).",
      "tag": "추정",
      "source_ids": [
        "ref-559"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세이프틱스 위험성평가 가이드(업체 자료, 발행일 미확인) (재인용: 2026-09-25-61) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f46",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 23. 시험·형식 검증·벤치마크: ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과(목표 조건·성공률)로 자동 평가하는 공개 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-539",
        "ref-541"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ALFRED(AI2-THOR 가정 작업), LoTa-Bench(ICLR 2024, 성공률 비교) (재인용: 2026-09-25-62). 물류 지시 데이터셋은 아님",
      "as_of": "2024-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f47",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고, 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나 물류센터 적용 여부는 미확인이다(oq-085).",
      "tag": "사실",
      "source_ids": [
        "ref-516",
        "ref-518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN KS X ISO 23247-1, ISO 23247-6:2026 Digital twin composition (재인용: 2026-09-25-56)",
      "as_of": "2026",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f48",
      "claim": "이번에 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 새 로봇 연동 승인 기준으로 쓰고 판 차이(2.x·3.0.0)로 생기는 UNSUPPORTED_PARAMETER 같은 미지원 오류를 누가 판정·수정할지가 23. 시험·형식 검증·벤치마크·24. 자산·소프트웨어 수명주기 관리에서 28. 표준·상호운용성·다사업자 거버넌스로 넘어가는 과제가 될 것으로 보인다(oq-055, oq-091).",
      "tag": "추정",
      "source_ids": [
        "ref-407",
        "ref-408",
        "ref-608",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f24·f26·f27 에서 끌어낸 추론. VDA 공식 인증 절차 부재는 확정 사실 아님",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
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
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 팩트시트 용도, 지도 배포 즉시 동작, UNSUPPORTED_PARAMETER, 범위 제외(안전·교통 전략·외부 IT 인터페이스)를 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "상태 메시지 JSON 스키마. maps(mapId·mapVersion·mapStatus), batteryState(stateOfCharge·batteryHealth·range·charging), 오류 수준, 운용 모드 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "traffic-editor 로 차선·경유점·충전소·주차·문·승강기·층 정렬을 주석하고 주행 그래프로 내보내는 흐름.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (RAWSim-O GitHub)",
      "title": "RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 결정 문제 효과를 연구하는 이산 사건 시뮬레이션 프레임워크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-121",
      "org": "Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022)",
      "title": "The complexity of soundness in workflow nets",
      "published": "2022",
      "url": "https://arxiv.org/abs/2201.05588",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 워크플로 넷 건전성 판정의 계산 복잡도 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정 항목(속도 한계·작업 유형·기준 좌표·관제 연결·배터리)과 대응 경유점 4개 이상 권장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets_adapter_tutorial.md",
      "source_unopened": false
    },
    {
      "id": "ref-186",
      "org": "Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외",
      "title": "Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks",
      "published": "2019-06",
      "url": "https://arxiv.org/abs/1906.08291",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MAPF 정의·변형·격자 벤치마크 정리.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-204",
      "org": "ASTM International",
      "title": "Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21)",
      "published": "2021",
      "url": "https://www.astm.org/f3499-21.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. A-UGV 도킹 성능 확인 시험 방법.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-217",
      "org": "Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L.",
      "title": "Semi-automated map creation for fast deployment of AGV fleets in modern logistics",
      "published": "2017",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV 플릿 신속 배치를 위한 반자동 지도 작성과 도입 지연 원인.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "팩트시트 JSON 스키마. loadSets, mobileRobotConfiguration.versions, batteryCharging 필드 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-229",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "능력 기술 서브모델 README. 요구·제공 능력 비교와 속성·제약·스킬 구조.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Capability%20Description/1/0/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-241",
      "org": "Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M.",
      "title": "Automated generation of digital twin for a built environment using scan and object detection as input for production planning",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 스캔·객체 검출로 건물 환경 디지털 트윈 자동 생성.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-265",
      "org": "European Commission (CORDIS)",
      "title": "PAN-ROBOTS: Automating logistics for the factory of the future",
      "published": null,
      "url": "https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 과제 소개, 설치 기간 단축 보고(과제 측).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-267",
      "org": "IEEE 게재 논문 저자(미확인)",
      "title": "Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개))",
      "published": "2024",
      "url": "https://ieeexplore.ieee.org/document/10287275/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션 기반 다중 AGV 경로망 자동 설계.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-291",
      "org": "Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W.",
      "title": "Digital Twin in manufacturing: A categorical literature review and classification",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/pii/S2405896318316021",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 분야 디지털 모델·섀도·트윈 구분.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-364",
      "org": "ROS 2 Design",
      "title": "Managed nodes (ROS 2 Design: node_lifecycle)",
      "published": null,
      "url": "https://design.ros2.org/articles/node_lifecycle.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 2 관리형 노드 상태 기계.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-398",
      "org": "Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L.",
      "title": "Decision rules for robotic mobile fulfillment systems",
      "published": "2019",
      "url": "https://www.sciencedirect.com/science/article/pii/S2214716019300946",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 결정 규칙의 시뮬레이션 비교.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-403",
      "org": "Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플릿 배터리 열화를 고려한 AMR 스케줄링(프리프린트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션: 배치 전 시험 이점, 월드 생성, 문·승강기·워크셀 플러그인, lift_supervisor, slotcar 모델.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
      "source_unopened": false
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 3.0.0 플릿 시뮬레이터, 적합성 시험 묶음·고장 주입(개인 프로젝트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록 기반 VDA 5050 주문·재연결·취소 진단 도구(개인 프로젝트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 설명에서 LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-466",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국내 물류로봇 시험인증 협력 보도.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-493",
      "org": "Lott, J., & Honary, V.(University of San Diego)",
      "title": "Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.13711",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 통신 저하 조건의 분산 배정기 벤치마크(프리프린트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-516",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 디지털 트윈 프레임워크 국내 부합 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-518",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 디지털 트윈 결합을 다루는 ISO 23247 Part 6.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-521",
      "org": "Le, T. V., & Fan, R.",
      "title": "Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류·공급망 디지털 트윈 검토와 개념 틀.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 과제: 컨베이어·전압 시험기·진공 그리퍼 고장, 긴급 주문.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/challenges.rst",
      "source_unopened": false
    },
    {
      "id": "ref-539",
      "org": "askforalfred (ALFRED 공식 저장소)",
      "title": "ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README)",
      "published": null,
      "url": "https://github.com/askforalfred/alfred",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 지시를 가정 작업 행동 순서로 대응시키는 벤치마크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기의 자동 정량 평가 벤치마크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-553",
      "org": "Lei, Y., Liu, H., Li, N. 외",
      "title": "Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301)",
      "published": "2025",
      "url": "https://link.springer.com/article/10.1007/s11431-024-2810-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 상태 감시·고장 진단 검토.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-554",
      "org": "IEC",
      "title": "IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment",
      "published": "2015-06",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IACS 환경 패치 관리 기술 보고서.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-559",
      "org": "세이프틱스(Safetics)",
      "title": "로봇 시스템 위험성평가 가이드",
      "published": null,
      "url": "https://doc.safetics.io/insight-risk-assessment/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 시스템 위험성평가 절차 안내(업체 자료).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-601",
      "org": "reeceholland (ros2_fault_injection GitHub)",
      "title": "ros2_fault_injection — README",
      "published": null,
      "url": "https://github.com/reeceholland/ros2_fault_injection",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 2 센서 신호·속도 명령 장애 주입 도구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-602",
      "org": "University of Liverpool Autonomy and Verification (ROSMonitoring GitHub)",
      "title": "ROSMonitoring: a Runtime Verification Framework for ROS — README",
      "published": null,
      "url": "https://github.com/autonomy-and-verification-uol/ROSMonitoring",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 런타임 검증 프레임워크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-604",
      "org": "Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02-17",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. FMS 안의 지속형 MAPF 시험대와 설계 선택 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-606",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-607",
      "org": "한국로봇산업진흥원(KIRIA)",
      "title": "시험평가 | KIRIA 첨단로봇 실증지원 디지털 플랫폼",
      "published": null,
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇산업진흥원 로봇 시험평가 안내.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR 의 VDA 5050 인증 발표(벤더 보도자료).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-609",
      "org": "von Berg, B., Aichernig, B. K., & Wedenik, F.",
      "title": "BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper)",
      "published": "2026-05",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 AGV 교착 회피의 BDD 기반 사례 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/f-deployment-verification-and-maintenance/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "'다른 대분류와의 연결' 절만 patches 로 채운다. A. 업무·공급망 설계: f1·f2(22↔3·4), f3(22↔1, 연계 대상), f4(21↔3), f5(23↔2) / B. 공통 정보·환경 모델: f6·f7(21↔5), f9·f10(21↔6), f11·f12(24↔6 지도 버전), f13·f14(22↔8, 8·22 구분 유지), f15(24↔8), f16·f17(22↔6) / C. 연결·실행 기반: f18·f19·f20(21↔9), f10(21↔10), f16·f21(22·23↔10), f22·f23(22↔9, oq-086), f24(24↔9), f25(24↔12), f26·f27(23↔9·12, f27 벤더 주장 병기), f28(23↔12, 연계 대상) / D. 계획·최적화: f2(22↔13), f29(22↔15), f10(21↔15), f30·f31·f32(23↔15), f33(23↔13), f19·f34·f35(24↔13·16) / E. 협업·현장 운영: f36·f37(23↔20), f38(23↔17), f39(24↔19), f40(23↔19) / G. 안전·보안·지능·거버넌스: f41(21·23↔25), f42·f43(23↔28, 연계 대상), f44(24↔26), f45(24↔25), f8·f46(21·23↔27, 교차 규칙), f47(22↔28), f48(23·24↔28) / '아직 다루지 않은 연결': 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(oq-081), 21. 온보딩·설정·현장 시운전 ↔ E. 협업·현장 운영, 22 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적과의 연결은 근거 미확보. 다음 실행 후보: B. 공통 정보·환경 모델 페이지의 '아직 다루지 않은 연결'(23·24)을 f11·f15 로 보강."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 23. 시험·형식 검증·벤치마크, 10. 설비·건물 시스템 연동, 21. 온보딩·설정·현장 시운전 | 근거: f16 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 38,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f11 은 VDA 명세와 VDA 스키마로 독립 출처 아님)",
      "f27 OTTO VDA 5050 인증의 시험 항목 미확인(벤더 주장)",
      "f43 KTL·통합물류협회 협력 내용은 기사 기준, 1차 출처 미확인",
      "f45 국내 변경 후 재평가 공식 규정 미확인(oq-092)",
      "20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거 미확보(oq-081)",
      "ref-407·ref-408·ref-121·ref-204·ref-539·ref-541 은 이번 입력의 참고문헌 요약 목록에 없어 게시 페이지 각주·이전 브리프 값을 옮겼고, 유형·신뢰도는 이번 실행의 판단"
    ],
    "scope_violations": [
      "f3: 수요예측은 분류 원문 9장 상위 업무 시스템 경계라 '연계 대상:' 표시",
      "f28: 센서 신호 장애 주입은 로봇 자체 인식·주행 견고성 시험이라 '연계 대상:' 표시",
      "f42: 로봇 자체 성능 시험은 시험기관·제조사 쪽이라 '연계 대상:' 표시",
      "f13·f17·f47: 제조 대상 자료라 물류 적용은 미확인으로 명시"
    ],
    "budget_used": {
      "queries": 1,
      "sources": 0
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-228(factsheet.schema), ref-079(traffic-editor.md), ref-153(fleet adapter tutorial), ref-406(simulation.md), ref-229(IDTA 02020 README), ref-528(ARIAC challenges.rst). 나머지 30건은 게시 페이지 각주·이전 브리프 재사용이며 원문 미열람(신뢰도 상한 medium). 대분류 연결 실행 규칙(R-3)에 따라 근거를 게시된 21~24 세부영역 페이지와 A·B·C·D·E 대분류 페이지 각주에서 먼저 찾았고 신규 출처는 0건이다. 한국어 검색 1회(물류센터 AMR 가상 시운전 디지털 트윈)는 기사·업체 블로그뿐이라 쓰지 않았다. 한국 자료: KS B ISO 18646-1(ref-606), KIRIA 시험평가(ref-607), KTL 협력 보도(ref-466), KS X ISO 23247-1(ref-516). 교차 규칙: 매뉴얼 해석 AI 는 f8 로 21. 온보딩·설정·현장 시운전·5. 로봇 능력·작업 온톨로지·27. AI·학습·적응과 모델 운영에 함께 연결했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f14 에서 원문 구분대로 나눴다. 페이지 절 번호는 대분류 페이지 절 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)로 5를 붙였다 [가정]. 정정 요청 없음. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-25-67/verification.json

```json
{
  "run_id": "2026-09-25-67",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: A. 업무·공급망 설계 페이지에 같은 주장이 같은 각주 ref-101 로 게시돼 있다. 이번 검증에서 원문 미열람(참고문헌 목록 일치). 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 22. 시뮬레이션·예측용 디지털 트윈 5절·D. 계획·최적화 페이지에 같은 주장(ref-398) 게시. 시뮬레이션 조건의 저자 보고임을 본문에 유지. 원문 미열람."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정]·'연계 대상:' 표시 적정(수요예측은 분류 원문 9장 상위 업무 시스템 경계). ref-521 원문 미열람."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 21. 온보딩·설정·현장 시운전 3절의 게시 주장과 같다. PAN-Robots 6→2개월은 과제 측 보고값·비교 조건 미확인임을 유지. ref-217·ref-265 원문 미열람."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: A 페이지 게시 주장과 같다. 적용 사례 미확인 표현 유지. ref-121 원문 미열람."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 검증 에이전트가 raw README 를 열어 '구현 독립적 기능 명세', 요구·제공 능력 비교, 속성·제약(전제조건·순서)·스킬 구조, 자원 매칭·계획·오케스트레이션 지원은 확인했으나 README 에 시운전(commissioning)·온보딩 언급은 없다. '시운전을 돕는다'는 출처에 없는 확장이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 21 페이지 10절 각주와 같은 논문(arXiv 2406.07962, 2024-06). 원문 미열람."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 분류 원문 8장 교차 규칙 적용 추론으로 [추정] 적정. 27. AI·학습·적응과 모델 운영과 21. 온보딩·설정·현장 시운전·5. 로봇 능력·작업 온톨로지 양쪽 연결 요건 충족."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw(integration_fleets_adapter_tutorial.md)에서 'A minimum of 4 matching waypoints is recommended.' 와 기준 좌표 설정 확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw(traffic-editor.md)에서 차선·경유점·충전기·주차·문·승강기·층, 기준점 층간 정렬, building_map_generator 로 주행 그래프 내보내기 문장 확인."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(ref-031 6.3절)과 raw state.schema 에서 downloadMap·enableMap·deleteMap, 같은 mapId 한 버전만 활성, mapId·mapVersion·mapStatus(ENABLED·DISABLED) 확인. ref-031·ref-051 은 같은 발행 주체라 교차 확인 아님."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 분류 원문 6번 주석('지도 버전 관리')·24번 정의('지도 버전')와 VDA 5050 지도 배포 즉시 동작에서 끈 추론으로 [추정] 적정."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: B 페이지·22 페이지 각주와 같다. 제조 대상 자료임을 본문에 명시해야 한다. 원문 미열람."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 8. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험) 구분을 지킨 [추정]. ref-291 원문 미열람."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(필드명 정정 필요): raw state.schema 에 batteryState 는 없고 최상위 powerSupply 아래 stateOfCharge·batteryHealth(0~100)·range('Estimated reach with current State of Charge in meter')·charging 이 있다. 주장 내용은 맞으나 근거 발췌의 묶음 이름이 틀렸다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw simulation.md 에서 building_map_generator 두 모드(world·navigation graph), 문·승강기 플러그인, TeleportDispenser·TeleportIngestor, lift_supervisor 확인. C 페이지 게시 주장과 같다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 22 페이지 6·8절 각주와 같다. 생산 계획 대상임을 명시. 원문 미열람."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(범위 축소): 입력 원문 Table 2 는 factsheet 를 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control'로 두어 설정 지원은 확인된다. 그러나 '초기 설정과 지속적 호환성 평가' 문장은 입력 원문 발췌(119,109자까지)와 raw 열람 결과·검색 결과 어디서도 확인하지 못했다(6.10절 미포함)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw factsheet.schema 에서 loadSpecification.loadSets, mobileRobotConfiguration.versions(key 예시 softwareVersion), mobileRobotConfiguration.batteryCharging 네 필드 확인. 다만 '한 등록 정보가 21·24·16 에 함께 쓰인다'는 해석이므로 [추정]으로 분리해야 한다(수정 지시)."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw 튜토리얼에서 선·각속도·가속도 한계, 작업 유형(loop·delivery·clean), 외곽 반경, 배터리·재충전 임계값, 관제 API 주소·계정 확인."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw simulation.md 에서 배터리 소모·충돌 비용 없음, 드문 예외 상황 시험, 'long running simulations can instill confidence in facility owners prior to deployment' 확인."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw simulation.md 에서 slotcar 의 레일식(rail-like) 주행과 로봇마다 주행 스택을 돌리지 않는다는 설명 확인."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f22 에서 끈 [추정], 오차 크기 미확인·oq-086 연결 적정."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 6.1.4.2 와 6.6.5.4 표에서 UNSUPPORTED_PARAMETER·CRITICAL·errorReferences 확인."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C 페이지 게시 주장과 같은 각주(ref-364). 이번 검증에서 원문 미열람."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C 페이지 게시 주장과 같다. README 자기 기술이며 공식 적합성 시험이 아님을 유지. ref-407·ref-408 원문 미열람."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: vendor_claim true, [추정] 적정. 23 페이지 9절과 같다. 본문에 '벤더 주장' 병기 필요. 원문 미열람."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 23 페이지 9절과 같다. '연계 대상:' 표시 적정. ref-601 원문 미열람."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 22·D 페이지와 같은 각주. 원문 미열람."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 23·D 페이지 게시 주장과 같다. 원문 미열람."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 23 페이지 3·8절과 같다(프리프린트). 끝의 '두 영역을 잇는다'는 해석이므로 분리 서술 지시. 원문 미열람."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 23 페이지 8절과 같다. 원문 미열람."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D 페이지 게시 주장과 같다(2026-09 프리프린트). 원문 미열람."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D 페이지 게시 주장과 같다. 24 페이지 각주는 '저자 미확인'이나 참고문헌 목록은 저자를 적으므로 목록 표기를 따른다. 원문 미열람."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 24 페이지 5절 출하 시나리오와 같은 [추정], 실측 미확인 명시."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw challenges.rst 에서 컨베이어·전압 시험기·진공 도구 고장, 고우선 주문 네 과제와 인용 문장 확인. 파일 자체에는 연도 표기가 없으나 문서 사이트 기준 ARIAC 2025."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f36·f28 에서 끈 [추정], 공개 사례 미확인·oq-087 연결 적정."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E 페이지 게시 주장과 같은 각주. 원문 미열람."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 24 페이지 8절과 같다. 원문 미열람."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ROSMonitoring 이 ROS 런타임 검증 프레임워크라는 부분만 [사실]. '운영 중 감시가 사전 시험을 보완하는 연결 지점'은 해석이므로 분리 지시. 원문 미열람."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 21·23 페이지 게시 주장과 같다. 세부 시험 항목 미확인. 안전 요구 자체는 연계 대상으로 적어야 한다. 원문 미열람."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 23 페이지 7·9절과 같은 [추정]·'연계 대상:'. 원문 미열람."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 기사 기준 [추정], 1차 출처 미확인. ref-466 원문 미열람."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 24 페이지 각주와 같다(2015-06, 발행 2년 경과 — 월간 재검증 대상). 원문 미열람."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 업체 자료(ref-559, 발행일 미확인) 기반 [추정], 국내 공식 규정 미확인 명시. 원문 미열람."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 벤치마크 각각 단일 출처(교차 확인 아님). 물류 지시 데이터셋이 아님을 본문에 남긴다. 원문 미열람."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 22 페이지 각주와 같다. 물류 적용 미확인·oq-085. 원문 미열람."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C 페이지 G 연결과 같은 방향의 [추정]. VDA 공식 인증 절차 부재가 확정 사실이 아님을 유지."
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
      "f1·f5 는 A. 업무·공급망 설계 페이지 '다른 대분류와의 연결' F 항목과 같은 주장 — 같은 각주(ref-101·ref-121) 재사용",
      "f16·f21·f25·f26·f48 은 C. 연결·실행 기반 페이지 F·G 항목과 같은 주장 — ref-406·ref-364·ref-407·ref-408 재사용",
      "f2·f29·f30·f33·f34 는 D. 계획·최적화 페이지 F 항목과 같은 주장 — ref-398·ref-267·ref-186·ref-493·ref-403 재사용",
      "f38 은 E. 협업·현장 운영 페이지 F 항목과 같은 주장 — ref-204 재사용",
      "f11·f15 는 B. 공통 정보·환경 모델 페이지 '아직 다루지 않은 연결'(23·24)을 채울 새 근거이며 기존 주장과 충돌하지 않는다",
      "ref-403 저자 표기가 24 페이지 각주('저자 미확인')와 참고문헌 목록(Li, J. 외)이 다르다 — 목록 표기를 따른다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "ref-031 에서 직접 인용이 f11·f18·f24 세 곳에 계획돼 있다 — 출처당 1회 규칙 위반"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "page_proposals 의 갱신 절: '5. 다른 대분류와의 연결'이 아니라 대분류 정본 제목 '다른 대분류와의 연결'(번호 없음) 절만 patches 로 교체한다 — 대분류 페이지 H2 는 번호가 없다(부록 C).",
    "f6: [사실] → [추정]으로 강등하고 '시운전을 돕는다' 표현을 빼고 '요구·제공 능력 비교와 자원 매칭·계획·오케스트레이션을 지원한다'로 고쳐 쓴다 — ref-229 README 에 시운전·온보딩 언급이 없다.",
    "f18: 팩트시트가 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보라는 부분만 ref-031 로 서술하고, '지속적인 호환성 평가' 부분과 그 영문 직접 인용은 싣지 않거나 '미확인'으로 표시해 전체를 [추정]으로 둔다 — 해당 문장을 원문 발췌에서 확인하지 못했다.",
    "f15: 필드 묶음을 언급할 때 batteryState 가 아니라 powerSupply(stateOfCharge·batteryHealth·range·charging)로 적는다 — ref-051 state.schema 3.0.0 판 기준.",
    "f19: 팩트시트 필드(loadSpecification.loadSets, mobileRobotConfiguration.versions, batteryCharging 네 필드)는 [사실][^ref-228]로, '한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, 16. 공용 자원·충전·에너지 최적화에 함께 쓰인다'는 해석은 별도 문장 [추정][^ref-228]으로 나눈다.",
    "f31·f40: 연구·도구의 내용은 [사실]로 두고, '두 영역을 잇는다'·'사전 시험을 보완하는 연결 지점이 된다'는 해석 부분은 별도 문장 [추정]으로 나눈다.",
    "ref-031 직접 인용은 절 전체에서 1회만 쓴다(f11 의 'one version of maps' 구절 권장), f24 의 UNSUPPORTED_PARAMETER 규정은 재서술한다.",
    "f27: 본문에 [추정] 과 함께 '벤더 주장'을 병기한다. f45: 근거가 업체 자료(세이프틱스, 발행일 미확인)임을 문장 안에 밝힌다. f43: 기사 기준이며 1차 출처 미확인임을 밝힌다.",
    "f3·f28·f42·f41: 수요예측, 로봇 센서 신호 장애 주입, 로봇 자체 성능 시험, 무인 산업 차량 안전 요구는 '연계 대상'으로 짧게 적고 ROP 직접 범위처럼 쓰지 않는다(분류 원문 9장).",
    "f14: 8. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 22. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험이라는 구분을 문장에 그대로 두고, 근거가 제조 대상 자료라는 한계를 적는다. f13·f17·f47 도 제조·생산 대상임을 밝힌다.",
    "f8·f46: 27. AI·학습·적응과 모델 운영 연결은 분류 원문 8장 교차 규칙에 따른 것임을 밝히고, 27. AI·학습·적응과 모델 운영 페이지와 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 페이지를 함께 링크한다.",
    "각주 정의: 원문을 열지 못한 출처(ref-101, ref-121, ref-186, ref-204, ref-217, ref-229, ref-241, ref-265, ref-267, ref-291, ref-364, ref-398, ref-403, ref-407, ref-408, ref-465, ref-466, ref-470, ref-493, ref-516, ref-518, ref-521, ref-539, ref-541, ref-553, ref-554, ref-559, ref-601, ref-602, ref-604, ref-606, ref-607, ref-608, ref-609)는 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다. ref-403 은 참고문헌 목록의 저자 표기(Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin))를 쓴다.",
    "기존 게시 페이지와 같은 주장(f1·f2·f5·f16·f21·f25·f26·f29·f30·f33·f34·f38)은 새 id 를 만들지 않고 해당 페이지와 같은 ref id 각주를 재사용하며, 다른 대분류 페이지의 같은 연결 절로 상호 참조 링크를 둔다.",
    "'아직 다루지 않은 연결'에는 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(oq-081), E. 협업·현장 운영 ↔ 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적을 근거 미확보로 적고, 다른 대분류·세부영역은 번호(문자)와 이름을 함께 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 46건, 미확인 2건, 교차 확인 0건. 강등: f6 사실 → 추정(IDTA 02020 README 에 시운전 언급 없음), f18 사실 → 추정(팩트시트의 '지속적 호환성 평가' 문장 미확인, 설정 지원만 확인). 원문 미열람 출처: ref-101, ref-121, ref-186, ref-204, ref-217, ref-241, ref-265, ref-267, ref-291, ref-364, ref-398, ref-403, ref-407, ref-408, ref-465, ref-466, ref-470, ref-493, ref-516, ref-518, ref-521, ref-539, ref-541, ref-553, ref-554, ref-559, ref-601, ref-602, ref-604, ref-606, ref-607, ref-608, ref-609(이상 게시 페이지 각주·참고문헌 목록과 일치로 실재 확인). 검증 에이전트가 raw 로 다시 연 출처: ref-051, ref-228, ref-079, ref-153, ref-406, ref-528, ref-229, ref-031(입력 원문 발췌 포함). 주의: 모든 연결이 단일 출처이거나 같은 발행 주체(VDA 명세·스키마) 근거이며, G. 안전·보안·지능·거버넌스 세부영역 페이지가 seed 라 G 쪽 연결은 F 쪽 근거에 기댄다. 브리프 기록 불일치: ref-229 는 sources 에 fetched: false 이나 self_check.limits 는 raw 로 열었다고 적는다(검증 에이전트가 열어 내용 확인). f15 근거 발췌의 batteryState 는 3.0.0 state.schema 에서 powerSupply 다. ref-031 직접 인용 3회 계획을 1회로 줄이도록 지시했다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-25-67/pages.json

```json
{
  "run_id": "2026-09-25-67",
  "outline": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 7000,
      "summary": "F. 도입·검증·유지관리의 네 세부영역은 A~E·G 대분류의 정보·인터페이스·알고리즘·운영 절차를 설치(21)·가정한 미래 실험(22)·시험(23)·버전과 열화 관리(24)로 잇는다. 예: VDA 5050 은 지도 배포·활성화를 관제 지시로 두고 로봇이 mapId·mapVersion 을 보고하게 한다. [사실][^ref-031][^ref-051]",
      "planned_findings": [
        "A: f1 f2 f3 f4 f5",
        "B: f6 f7 f9 f10 f11 f12 f13 f14 f15 f17",
        "C: f16 f18 f19 f20 f21 f22 f23 f24 f25 f26 f27 f28",
        "D: f2 f10 f29 f30 f31 f32 f33 f34 f35",
        "E: f36 f37 f38 f39 f40",
        "G: f8 f41 f42 f43 f44 f45 f46 f47 f48",
        "아직 다루지 않은 연결 5건"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 신규 작성(A·B·C·D·E·G 연결, 근거 미확보 연결 5건, 각주 41건)",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-09-25-67/pages/categories/f-deployment-verification-and-maintenance/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-09-25 | F. 도입·검증·유지관리 | 다른 대분류와의 연결 절 신규 작성(A·B·C·D·E·G 연결, f6·f18 강등 반영, 근거 미확보 연결 5건 명시) | run 2026-09-25-67",
  "index_updates": {
    "home_recent": "2026-09-25 — F. 도입·검증·유지관리: 다른 대분류와의 연결 절 신규 작성(여섯 대분류와의 연결, 근거 미확보 연결 5건 명시)",
    "category_recent": "2026-09-25 — F. 도입·검증·유지관리: 다른 대분류와의 연결 절 신규 작성(설치·시뮬레이션·시험·수명주기 관점에서 A·B·C·D·E·G 연결)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 팩트시트 용도, 지도 배포 즉시 동작, UNSUPPORTED_PARAMETER 를 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "상태 메시지 JSON 스키마. maps(mapId·mapVersion·mapStatus), powerSupply(stateOfCharge·batteryHealth·range·charging) 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "traffic-editor 로 차선·경유점·충전소·주차·문·승강기·층 정렬을 주석하고 주행 그래프로 내보내는 흐름.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (RAWSim-O GitHub)",
      "title": "RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 결정 문제 효과를 연구하는 이산 사건 시뮬레이션 프레임워크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-121",
      "org": "Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022)",
      "title": "The complexity of soundness in workflow nets",
      "published": "2022",
      "url": "https://arxiv.org/abs/2201.05588",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 워크플로 넷 건전성 판정의 계산 복잡도 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정 항목(속도 한계·작업 유형·기준 좌표·관제 연결·배터리)과 대응 경유점 4개 이상 권장.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-186",
      "org": "Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외",
      "title": "Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks",
      "published": "2019-06",
      "url": "https://arxiv.org/abs/1906.08291",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MAPF 정의·변형·격자 벤치마크 정리.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-204",
      "org": "ASTM International",
      "title": "Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21)",
      "published": "2021",
      "url": "https://www.astm.org/f3499-21.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. A-UGV 도킹 성능 확인 시험 방법.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-217",
      "org": "Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L.",
      "title": "Semi-automated map creation for fast deployment of AGV fleets in modern logistics",
      "published": "2017",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV 플릿 신속 배치를 위한 반자동 지도 작성과 도입 지연 원인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "팩트시트 JSON 스키마. loadSets, mobileRobotConfiguration.versions, batteryCharging 필드 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-229",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 능력 기술 서브모델 README. 요구·제공 능력 비교와 속성·제약·스킬 구조, 자원 매칭·계획·오케스트레이션 지원.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-241",
      "org": "Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M.",
      "title": "Automated generation of digital twin for a built environment using scan and object detection as input for production planning",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 스캔·객체 검출로 건물 환경 디지털 트윈 자동 생성.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-265",
      "org": "European Commission (CORDIS)",
      "title": "PAN-ROBOTS: Automating logistics for the factory of the future",
      "published": null,
      "url": "https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 과제 소개, 설치 기간 단축 보고(과제 측).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-267",
      "org": "IEEE 게재 논문 저자(미확인)",
      "title": "Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개))",
      "published": "2024",
      "url": "https://ieeexplore.ieee.org/document/10287275/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션 기반 다중 AGV 경로망 자동 설계.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-291",
      "org": "Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W.",
      "title": "Digital Twin in manufacturing: A categorical literature review and classification",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/pii/S2405896318316021",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 분야 디지털 모델·섀도·트윈 구분.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-364",
      "org": "ROS 2 Design",
      "title": "Managed nodes (ROS 2 Design: node_lifecycle)",
      "published": null,
      "url": "https://design.ros2.org/articles/node_lifecycle.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 2 관리형 노드 상태 기계.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-398",
      "org": "Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L.",
      "title": "Decision rules for robotic mobile fulfillment systems",
      "published": "2019",
      "url": "https://www.sciencedirect.com/science/article/pii/S2214716019300946",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RMFS 결정 규칙의 시뮬레이션 비교.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-403",
      "org": "Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플릿 배터리 열화를 고려한 AMR 스케줄링(프리프린트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션: 배치 전 시험 이점, 월드 생성, 문·승강기·워크셀 플러그인, lift_supervisor, slotcar 모델.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 3.0.0 플릿 시뮬레이터, 적합성 시험 묶음·고장 주입(개인 프로젝트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록 기반 VDA 5050 주문·재연결·취소 진단 도구(개인 프로젝트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 설명에서 LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-466",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국내 물류로봇 시험인증 협력 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-493",
      "org": "Lott, J., & Honary, V.(University of San Diego)",
      "title": "Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.13711",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 통신 저하 조건의 분산 배정기 벤치마크(프리프린트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-516",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 디지털 트윈 프레임워크 국내 부합 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-518",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 디지털 트윈 결합을 다루는 ISO 23247 Part 6.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-521",
      "org": "Le, T. V., & Fan, R.",
      "title": "Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류·공급망 디지털 트윈 검토와 개념 틀.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 과제: 컨베이어·전압 시험기·진공 그리퍼 고장, 긴급 주문.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-539",
      "org": "askforalfred (ALFRED 공식 저장소)",
      "title": "ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README)",
      "published": null,
      "url": "https://github.com/askforalfred/alfred",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 지시를 가정 작업 행동 순서로 대응시키는 벤치마크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기의 자동 정량 평가 벤치마크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-553",
      "org": "Lei, Y., Liu, H., Li, N. 외",
      "title": "Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301)",
      "published": "2025",
      "url": "https://link.springer.com/article/10.1007/s11431-024-2810-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 상태 감시·고장 진단 검토.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-554",
      "org": "IEC",
      "title": "IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment",
      "published": "2015-06",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IACS 환경 패치 관리 기술 보고서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-559",
      "org": "세이프틱스(Safetics)",
      "title": "로봇 시스템 위험성평가 가이드",
      "published": null,
      "url": "https://doc.safetics.io/insight-risk-assessment/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 시스템 위험성평가 절차 안내(업체 자료).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-601",
      "org": "reeceholland (ros2_fault_injection GitHub)",
      "title": "ros2_fault_injection — README",
      "published": null,
      "url": "https://github.com/reeceholland/ros2_fault_injection",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 2 센서 신호·속도 명령 장애 주입 도구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-602",
      "org": "University of Liverpool Autonomy and Verification (ROSMonitoring GitHub)",
      "title": "ROSMonitoring: a Runtime Verification Framework for ROS — README",
      "published": null,
      "url": "https://github.com/autonomy-and-verification-uol/ROSMonitoring",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 런타임 검증 프레임워크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-604",
      "org": "Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02-17",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. FMS 안의 지속형 MAPF 시험대와 설계 선택 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-606",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-607",
      "org": "한국로봇산업진흥원(KIRIA)",
      "title": "시험평가 | KIRIA 첨단로봇 실증지원 디지털 플랫폼",
      "published": null,
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇산업진흥원 로봇 시험평가 안내.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR 의 VDA 5050 인증 발표(벤더 보도자료).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    },
    {
      "id": "ref-609",
      "org": "von Berg, B., Aichernig, B. K., & Wedenik, F.",
      "title": "BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper)",
      "published": "2026-05",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 AGV 교착 회피의 BDD 기반 사례 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가?",
      "areas": [
        22,
        23,
        10,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [],
  "additional_research_requests": [
    "다른 대분류와의 연결 절: 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거(제한 운영 처리량 저하 사전 추정 방법·사례, oq-081)가 필요하다 — 이번 브리프에 없어 '아직 다루지 않은 연결'로 둠.",
    "다른 대분류와의 연결 절: E. 협업·현장 운영 ↔ 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조 및 7. 화물·재고·자산 식별과 추적과 이 대분류의 연결 근거가 필요하다.",
    "VDA 5050 3.0.0 명세에서 팩트시트를 '초기 설정과 지속적 호환성 평가'에 쓰도록 하는 문장이 실제로 있는지(6.10절 포함) 원문 확인이 필요하다 — 확인되면 21. 온보딩·설정·현장 시운전 ↔ 9. 로봇·제조사 관제 연동 항목을 [사실]로 올릴 수 있다.",
    "IDTA 02020 능력 기술 서브모델을 시운전·온보딩에 쓴 사례나 공식 문서 근거가 필요하다(현재 README 에는 시운전 언급 없음).",
    "G. 안전·보안·지능·거버넌스의 25~28 세부영역 페이지 심화 뒤, G 쪽 근거로 F. 도입·검증·유지관리와의 연결을 재확인할 필요가 있다.",
    "B. 공통 정보·환경 모델 페이지의 '아직 다루지 않은 연결'(23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리)을 ref-031·ref-051 근거로 보강하는 대분류 연결 실행을 제안한다."
  ],
  "fixes_applied": [
    "갱신 절 제목 — page_proposals 의 '5. 다른 대분류와의 연결' 대신 번호 없는 정본 제목 '다른 대분류와의 연결' 절 하나만 patches(replace)로 교체했다.",
    "f6 강등 — B. 공통 정보·환경 모델 항목에서 [추정]으로 쓰고 '시운전을 돕는다'를 빼고 '요구·제공 능력 비교와 자원 매칭·계획·오케스트레이션을 지원한다'로 고쳤다.",
    "f18 — C. 연결·실행 기반 항목에서 팩트시트가 설정을 돕는 매개변수·제조사 정보라는 부분만 ref-031 로 쓰고, 지속적 호환성 평가 용도는 '미확인'으로 표시해 전체를 [추정]으로 두었으며 영문 직접 인용은 싣지 않았다.",
    "f15 — 필드 묶음을 batteryState 가 아니라 powerSupply(stateOfCharge·batteryHealth·range·charging)로 적었다.",
    "f19 — 팩트시트 필드 서술은 [사실][^ref-228], '한 등록 정보가 21·24·16 세부영역에 함께 쓰인다'는 해석은 별도 문장 [추정][^ref-228]으로 나눴다.",
    "f31·f40 — LSMART 제안과 ROSMonitoring 정체는 [사실]로, '두 영역을 잇는다'·'배치 전 시험을 보완하는 연결 지점'은 별도 문장 [추정]으로 나눴다.",
    "ref-031 직접 인용 — f11 의 'only be one version of maps …' 구절 1회만 인용하고, f24 의 UNSUPPORTED_PARAMETER 규정과 f18 은 재서술했다.",
    "f27 은 '[추정] 벤더 주장' 병기, f45 는 문장 안에 업체(세이프틱스) 자료·발행일 미확인을 밝혔고, f43 은 기사 기준·1차 출처 미확인을 밝혔다.",
    "f3·f28·f42·f41 — 수요예측, 로봇 센서 신호 장애 주입, 로봇 자체 성능 시험, 무인 산업 차량 안전 요구를 각각 '연계 대상:'으로 시작하는 짧은 문장으로 쓰고 ROP 직접 범위처럼 쓰지 않았다.",
    "f14 — 현재 상태 표현(8. 실시간 세계 상태·데이터 일관성)과 가정한 미래 실험(22. 시뮬레이션·예측용 디지털 트윈)의 구분을 문장에 두고 제조 대상 자료 한계를 적었으며, f13·f17·f47 에도 제조·생산 계획 대상임을 밝혔다.",
    "f8·f46 — G 항목에서 27. AI·학습·적응과 모델 운영 연결이 분류 원문 8장 교차 규칙에 따른 것임을 밝히고 27·21·23 세 페이지를 함께 링크했다.",
    "각주 정의 — 지시된 미열람 출처 34건(ref-229 포함) 각주에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-403 은 참고문헌 목록 저자 표기(Li, J. 외, UT Austin)를 썼다.",
    "기존 주장 재사용 — f1·f2·f5·f16·f21·f25·f26·f29·f30·f33·f34·f38 은 기존 ref id 각주를 그대로 쓰고, A·B·C·D·E 대분류 페이지의 '다른 대분류와의 연결' 절로 상호 참조 링크를 두었다.",
    "'아직 다루지 않은 연결' 소절에 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(oq-081), E. 협업·현장 운영 ↔ 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적을 근거 미확보로 번호(문자)와 이름을 함께 적었다."
  ]
}
```

### runs/2026-09-25-67/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/f-deployment-verification-and-maintenance/index.md (1개 절)
```

### runs/2026-09-25-67/pages/categories/f-deployment-verification-and-maintenance/index.md

```markdown
---
title: "F. 도입·검증·유지관리"
type: category
status: draft
created: 2026-09-24
updated: 2026-09-25
version: 2
---

[홈](../../index.md) › F. 도입·검증·유지관리

# F. 도입·검증·유지관리

## 핵심 질문

새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

## 개요

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? | [21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md) | published |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? | [22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) | published |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? | [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) | published |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? | [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8] [분류원문]

## 다른 대분류와의 연결

이 절은 게시된 세부영역 페이지와 다른 대분류 페이지의 검증된 근거로, 이 대분류의 네 세부영역이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지를 정리한다. 이번 정리의 연결 근거는 모두 단일 출처이거나 같은 발행 주체(VDA 명세와 스키마)의 출처이며, 교차 확인된 것은 없다.

### A. 업무·공급망 설계

[A. 업무·공급망 설계](../a-business-supply-chain-design/index.md)와는 처리능력·성과 결정을 시뮬레이션으로 실험하고, 도입 기간과 공정 모델 점검으로 이어진다.

- **[22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) ↔ [3. 처리능력·거점·설비 계획](../a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)·[4. 성과·경제성·프로세스 개선](../a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)**: RAWSim-O 는 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS) 운영의 여러 결정 문제가 미치는 효과를 연구하는 이산 사건 시뮬레이션 프레임워크다(확인일 2026-09-25). [사실][^ref-101] Merschformann 외(2019)가 보고한 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다(모델·시뮬레이션 조건에서의 저자 보고). [사실][^ref-398]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md)**: 연계 대상: 성수기 시나리오 입력(주문·물동량 전망)은 1. 주문·업무 시스템 연계를 거쳐 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 수요예측 자체는 분류 원문 9장의 상위 업무 시스템 경계에 속한다. [추정][^ref-521]
- **[21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md) ↔ 3. 처리능력·거점·설비 계획**: 다중 AGV 도입이 정밀 지도 작성·좌표 지정·수작업 경로망 설계로 오래 걸린다는 연구(2017)와, 설치 기간을 6개월에서 2개월로 줄일 수 있다는 과제 측 보고(비교 조건 미확인)가 있어, 온보딩 기간이 증차한 로봇이 처리능력으로 바뀌는 시점을 좌우하는 것으로 보인다. [추정][^ref-217][^ref-265]
- **[23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) ↔ [2. 공정·워크플로 모델링](../a-business-supply-chain-design/02-process-and-workflow-modeling.md)**: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있어 공정 모델의 형식적 점검이 형식 검증과 이어질 것으로 보이나, 물류 로봇 공정 적용 사례는 확인되지 않았다. [추정][^ref-121]

같은 연결의 반대편은 [A. 업무·공급망 설계 페이지의 다른 대분류와의 연결](../a-business-supply-chain-design/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### B. 공통 정보·환경 모델

[B. 공통 정보·환경 모델](../b-common-information-and-environment-model/index.md)과는 등록·설정 때 넘어가는 능력·지도 정보, 버전 관리, 현재 상태와 가정한 미래의 구분으로 이어진다.

- **21. 온보딩·설정·현장 시운전 ↔ [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)**: IDTA 02020 능력 기술(Capability Description) 서브모델 README 는 능력을 속성·제약(전제조건·순서)·스킬로 구조화해 공정이 요구하는 능력과 자원이 제공하는 능력을 비교하고, 자원 매칭·계획·오케스트레이션을 지원한다고 설명한다(확인일 2026-09-25). [추정][^ref-229] Vieira da Silva 외(2024-06)는 자연어 능력 설명에서 대규모 언어 모델(Large Language Model, LLM)을 이용해 능력 온톨로지를 생성하는 방법을 제안했다. [사실][^ref-465]
- **21. 온보딩·설정·현장 시운전 ↔ [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md)**: Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 RMF 좌표계 사이 변환을 위한 기준 좌표(대응 경유점)를 설정에 두고, 대응 경유점을 최소 4개 둘 것을 권한다(확인일 2026-09-25). [사실][^ref-153] Open-RMF traffic-editor 는 차선·경유점·충전소·주차 지점·문·승강기·층과 기준점(fiducial)을 이용한 층간 정렬을 주석하게 하고, 주석한 그래프는 building_map_generator 로 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- **[24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) ↔ 6. 지도·공간·위치 모델**: VDA 5050 3.0.0 은 지도 내려받기·활성화·삭제 즉시 동작(downloadMap·enableMap·deleteMap)을 두고, 같은 mapId 에 대해 "only be one version of maps with the same mapId enabled at a time" 라고 정한다. [사실][^ref-031] 상태 스키마는 로봇이 mapId·mapVersion·mapStatus(ENABLED·DISABLED)를 보고하게 한다(확인일 2026-09-25). [사실][^ref-051] 분류 원문이 6. 지도·공간·위치 모델에 '지도 버전 관리'를, 24. 자산·소프트웨어 수명주기 관리의 정의에 '지도 버전'을 함께 넣고 VDA 5050 이 지도 배포·활성화를 관제의 지시로 두므로, 지도 버전의 내용 정의는 B. 공통 정보·환경 모델 쪽, 배포·활성화 시점 조율과 이력 관리는 F. 도입·검증·유지관리 쪽이 맡는 분담이 될 것으로 보인다. [추정][^ref-031]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [8. 실시간 세계 상태·데이터 일관성](../b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)**: Kritzinger 외(2018)는 제조 분야 문헌을 검토해 물리 객체와 디지털 객체 사이 데이터 흐름의 자동화 정도에 따라 디지털 모델·디지털 섀도·디지털 트윈을 구분했다(제조 대상 분류). [사실][^ref-291] 8. 실시간 세계 상태·데이터 일관성은 현재 상태를 표현하고 22. 시뮬레이션·예측용 디지털 트윈은 그 모델을 이용해 가정한 미래를 실험한다는 분류 원문의 구분에 따라, 22. 시뮬레이션·예측용 디지털 트윈은 8. 실시간 세계 상태·데이터 일관성의 현재 상태(로봇·설비·배터리 상태)를 시나리오 초기값으로 받는 쪽이 될 것으로 보이며, 근거 분류 자료가 물류가 아닌 제조 대상이라는 한계가 있다. [추정][^ref-291][^ref-406]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 8. 실시간 세계 상태·데이터 일관성**: VDA 5050 상태 스키마(3.0.0 판)는 powerSupply 아래 충전 상태(stateOfCharge), 배터리 건강 상태(batteryHealth, 0~100%), 현재 충전량으로 추정한 도달 거리(range), 충전 여부(charging)를 로봇이 보고하게 한다(확인일 2026-09-25). [사실][^ref-051]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ 6. 지도·공간·위치 모델**: Sommer 외(2023)는 건물 환경 스캔과 객체 검출을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 제시했다(생산 계획 대상 연구). [사실][^ref-241]

[B. 공통 정보·환경 모델 페이지의 다른 대분류와의 연결](../b-common-information-and-environment-model/index.md#다른-대분류와의-연결)은 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리와의 연결을 아직 다루지 않은 연결로 두고 있으며, 위 24. 자산·소프트웨어 수명주기 관리 두 항목이 그 절을 보강할 근거 후보다.

### C. 연결·실행 기반

[C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md)과는 등록 정보·어댑터 설정, 설비 연동의 시뮬레이션, 판 차이 오류와 적합성 시험으로 이어진다.

- **21. 온보딩·설정·현장 시운전 ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)**: VDA 5050 은 팩트시트를 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보로 두며, 초기 설정 뒤 관제–로봇 능력의 지속적인 호환성 평가에도 쓰도록 하는지는 미확인이다. [추정][^ref-031] 팩트시트 스키마는 적재 명세(loadSpecification.loadSets), 로봇 구성의 버전 목록(mobileRobotConfiguration.versions, 예: softwareVersion), 충전 설정(batteryCharging 의 criticalLowChargingLevel·minimumDesiredChargingLevel·maximumDesiredChargingLevel·minimumChargingTime)을 담는다(확인일 2026-09-25). [사실][^ref-228] 그래서 한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화에 함께 쓰이는 것으로 보인다. [추정][^ref-228] Open-RMF 플릿 어댑터 설정은 최대 선·각속도와 가속도, 수행 가능한 작업 유형(loop·delivery·clean), 로봇 외곽 반경, 배터리·재충전 임계값, 제조사 관제 API 연결 정보(주소·계정)를 요구한다. [사실][^ref-153]
- **21. 온보딩·설정·현장 시운전·22. 시뮬레이션·예측용 디지털 트윈·23. 시험·형식 검증·벤치마크 ↔ [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)**: 앞의 traffic-editor 주석 대상에는 문·승강기가 들어간다. [사실][^ref-079] Open-RMF 시뮬레이션 문서에 따르면 building_map_generator 는 traffic-editor 로 주석한 건물 지도에서 Gazebo 시뮬레이션 세계와 주행 그래프를 만들고, 문·승강기 플러그인, 워크셀을 흉내 내는 TeleportDispenser·TeleportIngestor, 여러 플릿 어댑터의 승강기 요청을 조율하는 lift_supervisor 를 둔다. [사실][^ref-406] 같은 문서는 시뮬레이션 속 로봇이 배터리 소모나 충돌 비용 없이 장시간·가속 조건으로 드문 예외 상황을 시험할 수 있고, 장시간 시뮬레이션이 배치 전 시설 소유자의 확신을 높인다고 설명한다. [사실][^ref-406]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ 9. 로봇·제조사 관제 연동**: Open-RMF 시뮬레이션의 slotcar 플러그인은 경로·모드 요청을 받아 레일식으로 움직이고 센서 기반 주행 스택 없이 로봇 상태를 발행하는 전체 제어(full control) 로봇 모델이다. [사실][^ref-406] 이런 단순화 모델은 제조사 관제·로봇 고유 거동을 재현하지 않으므로, 관제 연동 방식(전체 제어·신호등·읽기 전용)과 제조사별 거동 차이가 처리량 예측 오차의 원인이 될 것으로 보인다(오차 크기 미확인, [열린 질문](../../open-questions.md) oq-086). [추정][^ref-406]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 9. 로봇·제조사 관제 연동**: VDA 5050 3.0.0 에서는 로봇이 자신이 쓸 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 유형의 오류를 CRITICAL 수준으로, 문제가 된 필드의 참조와 함께 보고해야 한다. [사실][^ref-031]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)**: ROS 2 관리형 노드는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate 같은 전이를 두어, 감독 도구가 구성요소 준비를 확인한 뒤 실행을 허용하게 한다. [사실][^ref-364]
- **23. 시험·형식 검증·벤치마크 ↔ 9. 로봇·제조사 관제 연동·12. 명령·작업 실행의 신뢰성**: 공개 개인 프로젝트 vda5050-sim 은 VDA 5050 3.0.0 주문 수명주기·동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을, vda5050-lab 은 메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT) 기록에서 반복 주문 id·재연결·취소 불일치를 진단한다고 README 에 적으며, 둘 다 VDA·VDMA 공식 적합성 시험이 아니다. [사실][^ref-407][^ref-408] OTTO by Rockwell Automation 은 자사 AMR 이 여러 관제 업체와 VDA 5050 인증을 마쳤다고 2026-04 발표했으나, 인증의 시험 항목은 확인되지 않았다. [추정] 벤더 주장[^ref-608] 연계 대상: ros2_fault_injection 은 오도메트리·레이저 스캔·관성 측정 장치(Inertial Measurement Unit, IMU)·점군 같은 센서 신호와 속도 명령을 조작하는 로봇 수준 장애 주입 도구이며, 23. 시험·형식 검증·벤치마크에서 ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. [추정][^ref-601]

같은 연결의 반대편은 [C. 연결·실행 기반 페이지의 다른 대분류와의 연결](../c-connectivity-and-execution-foundation/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### D. 계획·최적화

[D. 계획·최적화](../d-planning-and-optimization/index.md)와는 배정·경로 알고리즘을 시뮬레이션·벤치마크·형식 검증으로 시험하고, 배터리 열화 정보를 제약으로 넘기는 데서 이어진다.

- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md)·[15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)**: 앞의 A. 업무·공급망 설계 항목에서 본 피킹 주문 배정 규칙 비교는 시뮬레이션 조건에서 나온 결과다. [사실][^ref-398] 다중 AGV 시스템의 경로망(roadmap)을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있다. [사실][^ref-267]
- **21. 온보딩·설정·현장 시운전 ↔ 15. 다중 로봇 경로·교통 관리 — MAPF**: 시운전 때 traffic-editor 로 주석한 그래프가 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- **23. 시험·형식 검증·벤치마크 ↔ 15. 다중 로봇 경로·교통 관리 — MAPF**: Stern 외(2019)는 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)의 가정·목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했으나, 그 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). [사실][^ref-186] Yan 외(2026-02, 프리프린트)는 기존 MAPF 연구가 단순한 운동 모델과 완전한 실행·통신을 가정한다고 지적하고, 플릿 관리 시스템 안에서 계획 시점·방법·복구 설계 선택을 비교하는 시험대(LSMART)를 제안했다. [사실][^ref-604] 이 시험대는 D. 계획·최적화의 경로 알고리즘을 23. 시험·형식 검증·벤치마크의 시험 환경으로 잇는 사례로 보인다. [추정][^ref-604] von Berg 외(2026-05)는 창고 물류 AGV 의 교착 회피를 전이 시스템 인코딩과 BDD 로 분석한 사례 연구를 발표했다(계산 규모 한계는 oq-088). [사실][^ref-609]
- **23. 시험·형식 검증·벤치마크 ↔ 13. 작업 배정 — MRTA**: Lott·Honary(2026-09, 프리프린트)는 분산 작업 배정기 6종을 패킷 손실·페이딩 같은 통신 저하 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크를 제시했다. [사실][^ref-493]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 13. 작업 배정 — MRTA·[16. 공용 자원·충전·에너지 최적화](../d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)**: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 작업 배정·충전 일정을 정하는 연구(2026-03, 프리프린트)가 있다. [사실][^ref-403] 로봇이 보고하는 batteryHealth 가 낮아지면 같은 충전 상태에서도 도달 거리(range)가 짧아질 수 있어, 배터리 열화 정보가 13. 작업 배정 — MRTA·16. 공용 자원·충전·에너지 최적화의 제약 입력이 되는 것으로 보인다(물류센터 실측 자료 미확인). [추정][^ref-051][^ref-403]

같은 연결의 반대편은 [D. 계획·최적화 페이지의 다른 대분류와의 연결](../d-planning-and-optimization/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### E. 협업·현장 운영

[E. 협업·현장 운영](../e-collaboration-and-field-operations/index.md)과는 장애 대응·인계·감시를 시험하고, 고장 진단을 정비로 넘기는 데서 이어진다.

- **23. 시험·형식 검증·벤치마크 ↔ [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)**: NIST ARIAC 2025 문서는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급(고우선) 주문을 과제로 두어 설비·로봇 장애와 긴급 주문 대응을 평가한다(확인일 2026-09-25). [사실][^ref-528] 이런 장애 과제 정의와 장애 주입 도구를 결합하면 20. 예외 복구·재계획·업무 연속성의 재배정·수동 전환·제한 운영 동작을 업데이트마다 다시 돌리는 회귀 시험 시나리오로 만들 수 있을 것으로 보이나, 물류 오케스트레이션에 적용해 공개한 사례는 확인되지 않았다(oq-087). [추정][^ref-528][^ref-601]
- **23. 시험·형식 검증·벤치마크 ↔ [17. 로봇 간 협업·물리적 인계](../e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)**: ASTM F3499-21 은 자율 무인 지상 차량(A-UGV)의 도킹 성능을 확인하는 시험 방법이며, 그 결과를 로봇팔 파지 허용 오차와 잇는 기준은 확인되지 않았다(oq-063). [사실][^ref-204]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)**: Lei 외(2025)는 산업용 로봇의 고장 모드·데이터 수집·모델 기반과 데이터 기반 진단을 상태 기반 정비 관점에서 정리한 검토를 발표했다. [사실][^ref-553]
- **23. 시험·형식 검증·벤치마크 ↔ 19. 모니터링·이상 탐지·원인 분석**: ROSMonitoring 은 ROS 시스템의 런타임 검증 프레임워크다. [사실][^ref-602] 이런 운영 중 감시는 배치 전 시험을 보완하는 연결 지점이 될 것으로 보인다. [추정][^ref-602]

같은 연결의 반대편은 [E. 협업·현장 운영 페이지의 다른 대분류와의 연결](../e-collaboration-and-field-operations/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### G. 안전·보안·지능·거버넌스

[G. 안전·보안·지능·거버넌스](../g-safety-security-intelligence-and-governance/index.md)의 세부영역 페이지는 아직 심화 전이라, 아래 연결은 이 대분류 쪽 근거에 기댄다.

- **21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 ↔ [25. 안전·위험 관리](../g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)**: 연계 대상: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하며, 운용 구역 준비를 부속서 A 에 둔다(세부 시험 항목 미확인). [사실][^ref-470]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 25. 안전·위험 관리**: 업체(세이프틱스) 자료인 로봇 시스템 위험성평가 가이드(발행일 미확인)는 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로, 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 미확인이다(oq-092, oq-093). [추정][^ref-559]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [26. 사이버보안·접근권한·개인정보](../g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)**: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템(Industrial Automation and Control Systems, IACS) 환경의 패치 관리를 다루는 기술 보고서다. [사실][^ref-554]
- **21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 ↔ [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)**: 분류 원문 8장 교차 규칙은 매뉴얼 해석을 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 AI 연구 방법으로 둔다. 이 규칙에 따르면 LLM 기반 능력 온톨로지 생성은 새 로봇 등록 작업을 줄이는 방법으로 두 대분류를 잇는 것으로 보이며, 온보딩 현장 적용 사례는 미확인이다. [추정][^ref-465][^ref-229] 같은 규칙대로 AI 내용을 적용 대상 영역과 양쪽으로 잇는다면, 23. 시험·형식 검증·벤치마크 쪽에는 AI 계획기의 평가 방법이 이어진다: ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과(목표 조건·성공률)로 자동 평가하는 공개 벤치마크이며, 물류 지시 데이터셋은 아니다. [사실][^ref-539][^ref-541] 관련 페이지는 [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md)다.
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [28. 표준·상호운용성·다사업자 거버넌스](../g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)**: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고, 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나, 제조 대상 표준이라 물류센터 적용 여부는 미확인이다(oq-085). [사실][^ref-516][^ref-518]
- **23. 시험·형식 검증·벤치마크·24. 자산·소프트웨어 수명주기 관리 ↔ 28. 표준·상호운용성·다사업자 거버넌스**: 연계 대상: 국내에는 바퀴형 서비스 로봇의 이동 성능 시험방법 KS B ISO 18646-1 과 한국로봇산업진흥원의 시험평가 서비스가 있어, 로봇 자체 성능 시험은 시험기관 쪽이고 23. 시험·형식 검증·벤치마크의 ROP 몫은 그 결과를 등록·배정 조건으로 받는 쪽으로 보인다(oq-089). [추정][^ref-606][^ref-607] 한국산업기술시험원(KTL)과 통합물류협회가 물류로봇 시험인증 협력을 강화하기로 했다는 2026-07-24 기사가 있어(기사 기준, 1차 출처 미확인), 국내 물류로봇 시험·인증 체계가 두 세부영역을 잇는 후보가 될 것으로 보인다. [추정][^ref-466] 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 새 로봇 연동 승인 기준으로 쓰고 판 차이(2.x·3.0.0)로 생기는 UNSUPPORTED_PARAMETER 같은 미지원 오류를 누가 판정·수정할지가 28. 표준·상호운용성·다사업자 거버넌스로 넘어가는 과제가 될 것으로 보인다(공식 인증 절차 부재는 확정 사실 아님, oq-055·oq-091). [추정][^ref-407][^ref-408][^ref-608][^ref-031]

### 아직 다루지 않은 연결

다음 연결은 이번 실행에서 근거를 확보하지 못해 비워 둔다.

- [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) ↔ 22. 시뮬레이션·예측용 디지털 트윈: 제한 운영 상태의 처리량 저하를 미리 추정하는 근거 미확보(oq-081).
- [E. 협업·현장 운영](../e-collaboration-and-field-operations/index.md) ↔ 21. 온보딩·설정·현장 시운전: 근거 미확보.
- 22. 시뮬레이션·예측용 디지털 트윈 ↔ [26. 사이버보안·접근권한·개인정보](../g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md): 근거 미확보.
- [C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md)의 [11. 분산 시스템·통신·컴퓨팅 구조](../c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)와 이 대분류의 연결: 근거 미확보.
- [B. 공통 정보·환경 모델](../b-common-information-and-environment-model/index.md)의 [7. 화물·재고·자산 식별과 추적](../b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)과 이 대분류의 연결: 근거 미확보.

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-204]: ASTM International, Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21), 2021, https://www.astm.org/f3499-21.html, 접근일 2026-09-25 (원문 미열람)
[^ref-217]: Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L., Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission (CORDIS), PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: ROS 2 Design, Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-466]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-09-25 (원문 미열람)
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-539]: askforalfred (ALFRED 공식 저장소), ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README), 미확인, https://github.com/askforalfred/alfred, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-553]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-554]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-559]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)
[^ref-601]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25 (원문 미열람)
[^ref-602]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25 (원문 미열람)
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-606]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-607]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-609]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가. 2차 수정: 7절 첫 문장 [추정]·각주 보강, 8절 대표 연구 분류·평가 [의견]화, 8절 ref-556 항목 롤백 문구 정정 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "4. 핵심 개념과 용어" 절(1,365자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "6. 대표 접근법과 기술" 절(1,327자)을 옮겼다. 2차 수정: 부품 진단 연계 대상 문장을 [추정]과 각주로 고치고, 5·9절 참조를 원 세부영역 페이지 절 링크로 바꿈 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area24-s3.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "3. 왜 중요한가" 절(1,019자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area24-s7.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(982자)을 옮겼다. 2차 수정: 1절 요약과 3절 첫 문장의 태그를 [추정]으로 낮추고 각주를 ref-031·ref-550·ref-554 로 바꿈 (실행 2026-09-25-61)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [8]은 참고문헌 [ref-008](../../references/ref-008.md)에 해당한다.[^ref-008]

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24
```

### docs/categories/f-deployment-verification-and-maintenance/index.md

```markdown
---
title: "F. 도입·검증·유지관리"
type: category
status: seed
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../../index.md) › F. 도입·검증·유지관리

# F. 도입·검증·유지관리

## 핵심 질문

새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

## 개요

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? | [21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md) | published |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? | [22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) | published |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? | [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) | published |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? | [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가. 2차 수정: 7절 첫 문장 [추정]·각주 보강, 8절 대표 연구 분류·평가 [의견]화, 8절 ref-556 항목 롤백 문구 정정 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "4. 핵심 개념과 용어" 절(1,365자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "6. 대표 접근법과 기술" 절(1,327자)을 옮겼다. 2차 수정: 부품 진단 연계 대상 문장을 [추정]과 각주로 고치고, 5·9절 참조를 원 세부영역 페이지 절 링크로 바꿈 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area24-s3.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "3. 왜 중요한가" 절(1,019자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area24-s7.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(982자)을 옮겼다. 2차 수정: 1절 요약과 3절 첫 문장의 태그를 [추정]으로 낮추고 각주를 ref-031·ref-550·ref-554 로 바꿈 (실행 2026-09-25-61)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [8]은 참고문헌 [ref-008](../../references/ref-008.md)에 해당한다.[^ref-008]

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24
```

### runs/2026-09-25-67/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/action-dependency-graph.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/b2mml.md
glossary/battery-swapping.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/compensating-transaction.md
glossary/condition-based-maintenance.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/goal-condition.md
glossary/grai.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/isa-95.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mobile-manipulator.md
glossary/model-checking.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/order-batching.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/plug-and-produce.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/signal-temporal-logic.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/software-nameplate.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/virtual-commissioning.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
glossary/zone-set.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-493.md
references/ref-494.md
references/ref-495.md
references/ref-496.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-500.md
references/ref-501.md
references/ref-502.md
references/ref-503.md
references/ref-504.md
references/ref-505.md
references/ref-506.md
references/ref-507.md
references/ref-508.md
references/ref-509.md
references/ref-510.md
references/ref-511.md
references/ref-512.md
references/ref-513.md
references/ref-514.md
references/ref-515.md
references/ref-516.md
references/ref-517.md
references/ref-518.md
references/ref-519.md
references/ref-520.md
references/ref-521.md
references/ref-522.md
references/ref-523.md
references/ref-524.md
references/ref-525.md
references/ref-526.md
references/ref-527.md
references/ref-528.md
references/ref-529.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
references/ref-539.md
references/ref-540.md
references/ref-541.md
references/ref-542.md
references/ref-543.md
references/ref-544.md
references/ref-545.md
references/ref-546.md
references/ref-547.md
references/ref-548.md
references/ref-549.md
references/ref-550.md
references/ref-551.md
references/ref-552.md
references/ref-553.md
references/ref-554.md
references/ref-555.md
references/ref-556.md
references/ref-557.md
references/ref-558.md
references/ref-559.md
references/ref-599.md
references/ref-600.md
references/ref-601.md
references/ref-602.md
references/ref-603.md
references/ref-604.md
references/ref-605.md
references/ref-606.md
references/ref-607.md
references/ref-608.md
references/ref-609.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-area22-s10.md
topics/2026/2026-09-25-area22-s4.md
topics/2026/2026-09-25-area22-s6.md
topics/2026/2026-09-25-area22-s7.md
topics/2026/2026-09-25-area22-s8.md
topics/2026/2026-09-25-area23-s10.md
topics/2026/2026-09-25-area23-s11.md
topics/2026/2026-09-25-area23-s4.md
topics/2026/2026-09-25-area23-s6.md
topics/2026/2026-09-25-area23-s7.md
topics/2026/2026-09-25-area24-s10.md
topics/2026/2026-09-25-area24-s3.md
topics/2026/2026-09-25-area24-s4.md
topics/2026/2026-09-25-area24-s6.md
topics/2026/2026-09-25-area24-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/index.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 56건 / 전체 574건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-008 | NIST | ARIAC Documentation | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/ | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | https://arxiv.org/abs/2307.00827 | 2026-09-25 | 아니오 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 2026-09-25 | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | https://github.com/merschformann/RAWSim-O | 2026-09-25 | 예 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 2026-09-25 | 예 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | https://arxiv.org/abs/1906.08291 | 2026-09-25 | 아니오 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 2026-09-25 | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 2026-09-25 | 예 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 2026-09-25 | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 2026-09-25 | 예 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 2026-09-25 | 아니오 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 2026-09-25 | 예 |
| ref-265 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 2026-09-25 | 아니오 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | https://ieeexplore.ieee.org/document/10287275/ | 2026-09-25 | 아니오 |
| ref-269 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 2024-04 | https://arxiv.org/abs/2404.13499 | 2026-09-25 | 아니오 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 2026-09-25 | 아니오 |
| ref-364 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | https://design.ros2.org/articles/node_lifecycle.html | 2026-09-25 | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 2026-09-25 | 아니오 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | https://arxiv.org/abs/2603.22731 | 2026-09-25 | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/simulation.html | 2026-09-25 | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | https://arxiv.org/abs/2406.07962 | 2026-09-25 | 아니오 |
| ref-466 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 2026-09-25 | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 2026-09-25 | 아니오 |
| ref-481 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 미확인 | https://resources.sw.siemens.com/en-US/case-study-idc/ | 2026-09-25 | 아니오 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 2026-09-25 | 아니오 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | https://www.iso.org/standard/87426.html | 2026-09-25 | 아니오 |
| ref-520 | Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G. | Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics | 2020 | https://www.sciencedirect.com/science/article/pii/S2351978920320990 | 2026-09-25 | 아니오 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 2026-09-25 | 아니오 |
| ref-522 | Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P. | Simulation-based decision support tool for in-house logistics: the basis for a digital twin | 2021 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646 | 2026-09-25 | 아니오 |
| ref-523 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | https://github.com/open-rmf/rmf_simulation | 2026-09-25 | 예 |
| ref-524 | OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) | ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) | 미확인 | https://github.com/OpenFactoryTwin/ofact | 2026-09-25 | 예 |
| ref-525 | Sargent, R. G. | Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation) | 2008 | https://dl.acm.org/doi/abs/10.5555/1516744.1516780 | 2026-09-25 | 아니오 |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 2026-09-25 | 아니오 |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 2026-09-25 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 2026-09-25 | 예 |
| ref-529 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Scoring | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html | 2026-09-25 | 예 |
| ref-550 | IDTA (admin-shell-io/id GitHub) | IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing) | 미확인 | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md | 2026-09-25 | 예 |
| ref-553 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 2026-09-25 | 아니오 |
| ref-554 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | https://webstore.iec.ch/en/publication/22811 | 2026-09-25 | 아니오 |
| ref-556 | Amazon Web Services (aws-samples GitHub) | ros2-ota-firmware-updates — README | 미확인 | https://github.com/aws-samples/ros2-ota-firmware-updates | 2026-09-25 | 예 |
| ref-557 | 네이트 뉴스(원 매체 미확인) | 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장 | 2026-07-23 | https://m.news.nate.com/view/20260723n24828 | 2026-09-25 | 아니오 |
| ref-559 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | https://doc.safetics.io/insight-risk-assessment/ | 2026-09-25 | 아니오 |
| ref-599 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019-09 | https://arxiv.org/abs/1807.00048 | 2026-09-25 | 아니오 |
| ref-600 | Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S. | A Study on Challenges of Testing Robotic Systems | 2020 | https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc | 2026-09-25 | 아니오 |
| ref-601 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | https://github.com/reeceholland/ros2_fault_injection | 2026-09-25 | 예 |
| ref-602 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 2026-09-25 | 예 |
| ref-603 | IDM Lab (USC) 게재 초록, 저자 미확인 | The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration] | 2024 | https://idm-lab.org/bib/abstracts/Koen24p.html | 2026-09-25 | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | https://arxiv.org/abs/2602.15721 | 2026-09-25 | 아니오 |
| ref-605 | NIST | ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles | 미확인 | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles | 2026-09-25 | 아니오 |
| ref-606 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 2026-09-25 | 아니오 |
| ref-607 | 한국로봇산업진흥원(KIRIA) | 시험평가 | KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | https://kiria.org/rp/kiria/tva/inr/page.dn | 2026-09-25 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 2026-09-25 | 아니오 |
| ref-609 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 148개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
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
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- model-checking: 모델 검사 (Model Checking)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
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
```

### docs/open-questions.md (요약: 대상 영역 [21, 22, 23, 24] 에 걸린 18건 / 전체 93건)

```markdown
- oq-022 [열림] 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? (영역 6, 21)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-058 [열림] 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (영역 15, 23)
- oq-063 [열림] ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? (영역 17, 23)
- oq-076 [열림] 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? (영역 21, 9)
- oq-077 [열림] 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? (영역 21, 6, 23)
- oq-078 [열림] 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? (영역 21, 6)
- oq-081 [열림] 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? (영역 20, 22)
- oq-084 [열림] 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? (영역 22, 4)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 22, 28)
- oq-086 [열림] 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? (영역 22, 9)
- oq-087 [열림] 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? (영역 23, 24)
- oq-088 [열림] BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? (영역 23, 15)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 23, 28)
- oq-090 [열림] 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? (영역 24, 23)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 24, 9, 28)
- oq-092 [열림] 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? (영역 24, 25)
- oq-093 [열림] EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (영역 24, 25)
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```
