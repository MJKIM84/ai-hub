(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-52
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 21. 온보딩·설정·현장 시운전 (F. 도입·검증·유지관리)
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

### runs/2026-09-25-52/target.json

```json
{
  "run_id": "2026-09-25-52",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 52,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 21,
    "area_name": "21. 온보딩·설정·현장 시운전",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=21"
}
```

### runs/2026-09-25-52/research.json

```json
{
  "run_id": "2026-09-25-52",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 21,
    "area_name": "21. 온보딩·설정·현장 시운전",
    "category": "F. 도입·검증·유지관리"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음 (트랙 반영 제안: 도입 설치 시간의 원인)",
    "섹션 4. 핵심 개념과 용어 비어 있음",
    "섹션 5. 현장 시나리오 비어 있음 — 새 제조사 로봇을 적치 운반에 추가하는 시나리오 필요",
    "섹션 6. 대표 접근법과 기술 비어 있음 (트랙 반영 제안 3건 대상)",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음 (트랙 반영 제안 2건 대상)",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 기존 oq-022 관련"
  ],
  "research_questions": [
    "새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]",
    "새 로봇을 관제에 등록할 때 로봇 신원·기능·제약을 어떤 표준 메시지나 설정으로 받는가(VDA 5050 팩트시트, MassRobotics 신원 보고, Open-RMF 플릿 어댑터 설정)? (섹션 4·6·7 겨냥)",
    "지도·레이아웃·경로망은 새 현장에서 어떻게 만들고 관제에 넘기며, 이를 자동화·반자동화하는 연구는 무엇인가? (섹션 3·6·8 겨냥, 트랙 반영 제안 검토)",
    "제조사별 로봇 지도와 공통 지도 사이의 좌표 대응과 다층 정렬은 어떻게 설정하는가? (섹션 6 겨냥, 6. 지도·공간·위치 모델 연결)",
    "능력 기술 표준과 문서(매뉴얼) 해석 AI 는 로봇 등록·능력 매칭 작업을 어떻게 줄이려 하는가? (섹션 6·8 겨냥, 교차 규칙: 27. AI·학습·적응과 모델 운영 → 5·21)",
    "현장 시운전 전 안전 준비·가상 시운전·국내 시험·실증 체계는 무엇이 있는가? (섹션 7·9·10 겨냥, 한국 자료 우선)",
    "oq-022 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 활용한 사례가 있는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 명세는 팩트시트(factsheet) 토픽을 관제(fleet control)에서 이동로봇 설정을 돕는 파라미터·제조사 정보 전달 수단으로 두고, 관제가 즉시 동작 factsheetRequest 로 로봇에 팩트시트 전송을 요청할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.10절: 팩트시트는 \"Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control\"를 전달한다. 표 4에 factsheetRequest 즉시 동작. (두 출처는 같은 저장소라 독립 아님)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "VDA 5050 팩트시트 스키마는 유형 사양(typeSpecification), 물리 파라미터, 프로토콜 한계, 지원 프로토콜 기능·동작(protocolFeatures), 로봇 기하, 적재 사양(loadSpecification), 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)의 일곱 절을 필수로 두며, 스키마 설명은 이 정보가 관제 통합에 필요하고 시스템 계획·규모 산정·시뮬레이션에도 쓸 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "factsheet.schema 최상위 필수 절 7개. 설명문: 로봇 유형 계열을 VDA 5050 준수 관제에 통합하는 데 필요하며 계획·규모 산정·시뮬레이션에 적용 가능. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 은 지도 배포를 위해 즉시 동작 downloadMap(지도 id·버전·내려받기 링크)·enableMap·deleteMap 을 두고, 관제가 내려받기를 지시하면 로봇이 지도 서버에서 지도를 받아 특정 버전을 활성화하는 흐름을 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표 4: downloadMap 은 새 지도 내려받기를 트리거(mapId, version, 링크), enableMap·deleteMap. 그림 13: 관제 트리거 → 로봇이 지도 서버에서 받음 → 버전 활성화.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 은 도입(implementation) 단계에서 경로 정의·스테이션 설정·로봇 속성 저장이 이루어진다고 설명하되 경로 설정 자체는 명세 범위 밖으로 두며, 경로망은 레이아웃 교환 형식(LIF)으로 관제에 가져올 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.2절: 경로 수동 정의, 스테이션 설정, 로봇 속성 저장을 도입 단계 활동으로 서술하고 경로 설정은 이 문서의 대상이 아니라고 적음. LIF(VDMA 2024-03)로 경로를 관제에 가져올 수 있다고 언급.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합사업자가 간선·노드·스테이션으로 이루어진 주행 레이아웃을 제3자 중앙 관제 시스템에 처음 넘겨주기 위한 비구속적 교환 형식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 통합사업자가 \"initially transfer a track layout to a central (third-party) master control system\" 할 수 있게 함. 레이아웃은 edges·nodes·stations 모음. 1.0.0, 2023-09, 비구속적 접근.",
      "as_of": "2023-09",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "MassRobotics AMR 상호운용 표준의 신원 보고(identityReport)는 uuid·시각·제조사명·모델·일련번호·기본 외곽 치수를 필수로, 최고 속도·예상 가동 시간·충전기 형식·지원 업체·제품 문서 URI·화물 종류·최대 화물 부피·최대 화물 무게를 선택으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AMR_Interop_Standard.json identityReport required: uuid, timestamp, manufacturerName, robotModel, robotSerialNumber, baseRobotEnvelope. optional: maxSpeed, maxRunTime, chargerType, productDocumentation, cargoType, cargoMaxVolume, cargoMaxWeight 등.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 플릿 어댑터 설정 파일은 새 플릿마다 속도·가속 한계, 외곽 반경, 배터리·기계 파라미터, 후진 가능 여부, 수행 가능한 작업 유형(순회·배송·청소), 작업 종료 후 동작, 로봇 좌표계와 RMF 좌표계를 대응점 쌍으로 변환하는 reference_coordinates, 제조사 관제 API 연결 정보를 채우게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 의 rmf_fleet(limits, profile, battery_system, mechanical_system, reversible, task_capabilities, finishing_request), 선택 reference_coordinates, fleet_manager(prefix, 인증). 필드와 어댑터 코드가 맞지 않으면 가져오기 오류.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "Open-RMF traffic-editor 는 기존 건축 도면·평면도를 배경 이미지로 불러오고, 알려진 두 점 사이 거리 측정으로 축척을 맞춘 뒤 정점·벽·문·승강기·주행 차선·충전기를 사람이 주석하게 하며, 층 사이 정렬은 수직으로 맞춘 기준점(fiducial) 쌍으로 변환을 계산한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목적: 여러 플릿의 의도를 \"standardized, vendor neutral manner through a graphical interface\"로 표현. 측정선으로 축척(기본 1픽셀=5cm), 충전기는 정점 속성, 기준점 쌍으로 층간 이동·회전·축척 계산.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF 는 대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor(rmf_site)를 공개하며, 이 도구의 프로젝트에서 시뮬레이션과 주행 그래프를 생성할 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-643"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"an experimental approach to visualizing and editing large RMF deployment sites\". Rust·Bevy 기반, 데스크톱·웹, 프로젝트에서 시뮬레이션·주행 그래프 생성, 웹판은 JSON 내보내기. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 제어권 없이 상태만 보고하므로, 새 플릿 온보딩 때 어느 수준으로 연동할지가 선택 사항이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-251"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "integration_fleets: Full Control·Traffic Light·Read Only 세 연동 수준과 각 수준의 제어 범위. (재인용: 2026-09-25-50)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Beinschob 외(Robotics and Autonomous Systems 87권, 2017)는 다중 AGV 도입의 긴 설치 시간 원인으로 공장의 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문가의 수작업 경로망 설계를 들고, 레이저 스캐너 시스템으로 3D 의미 지도를 얻어 이를 반자동화하는 통합 시스템을 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-217"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 요약: 긴 도입 시간은 정밀 2D 지도, 픽업·하역 위치의 3D 지리 참조, 경로망 수작업 설계에서 비롯. 혁신적 레이저 스캐너로 3D 의미 지도 획득. (PAN-Robots 과제)",
      "as_of": "2017",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "EU CORDIS 의 PAN-Robots 과제 소개는 기존 표지를 활용한 위치 추정과 반자동 공장 탐사로 시스템 설치 기간을 6개월에서 2개월로 줄일 수 있다고 적지만, 이는 과제 측 보고값이며 비교 조건은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-265"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 요약: 설치를 6개월 대신 2개월에 할 수 있어 공장 중단 시간을 줄인다; 반자동 공장 탐사와 기존 랜드마크 활용 위치 추정 덕분. 비교 기준·현장 수 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "Heselden·Das(arXiv 2404.13499, 2024)는 지도 작성이 새 환경에 로봇을 배치할 때 시간이 많이 드는 과정이라고 보고, 전역 위치·물체 위치·위상·점유 정보 중심의 표준화된 지도 처리 방식과 빠진 데이터를 틀·절차적으로 생성하는 관리 스크립트를 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-269"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 요약: 지도 작성은 새 환경 배치의 시간 소모 과정. 전역 위치·물체 위치·위상·점유 중심 표준 처리, 빠진 데이터의 템플릿·절차적 생성으로 효율적 배치와 플랫폼 간 상호운용 향상. ICRA 2024 워크숍.",
      "as_of": "2024-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "노주형 외(한국로봇학회 논문지 21권 1호, 2026)는 3D 라이다–관성 센서 기반 SLAM 탐사와 로봇팔로 승강기 버튼을 누르는 기능을 결합해 사물인터넷 장치 개조나 외부 시스템 연동 없이 다층 실내 지도를 처음부터 끝까지 자율로 구축하는 시스템을 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-163"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 3D LiDAR–IMU SLAM 기반 프런티어 생성, 다중 센서 융합 비용 지도, RGB-D 카메라와 4자유도 매니퓰레이터로 승강기 버튼 조작, 완전 자율 다층 지도 구축. 48–57쪽.",
      "as_of": "2026",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 은 공정·제품 요구와 자원 능력을 함께 모델링해 요구 능력과 제공 능력을 비교하고 생산 공정의 계획·오케스트레이션을 지원하도록 만든 자산관리셸 서브모델 명세다.",
      "tag": "사실",
      "source_ids": [
        "ref-229"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes.\" 버전 1.0(IDTA 첫 공식 발행). 시운전 공수는 언급 없음.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "Vieira da Silva 외(arXiv 2307.00827, ETFA 2023)는 새 자원과 기능의 통합 공수를 줄이려는 플러그 앤 프로듀스(Plug and Produce)를 위해 능력·스킬을 기술하는 두 접근(온톨로지 기반 형식 기술, 자산관리셸 서브모델 표준화)이 서로 호환되지 않는다고 보고 둘 사이의 대응을 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 플러그 앤 프로듀스의 핵심은 새 자원과 기능 통합 공수 감소; 능력·스킬 모델링에 온톨로지와 AAS 서브모델이라는 호환되지 않는 두 접근이 있음.",
      "as_of": "2023-07",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "Vieira da Silva 외(arXiv 2406.07962, 2024)는 능력의 자연어 설명을 소수 예시 프롬프트에 넣어 LLM(Large Language Model, 대규모 언어 모델)으로 능력 온톨로지를 생성하고, 구문 검사·모순 검사·환각과 누락 요소 검사를 LLM 과 반복하는 방식으로 결과를 자동 검증하는 방법을 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 자연어 능력 설명 → few-shot 프롬프트 → 능력 온톨로지 생성 → 구문 검사, 모순 검사, 환각·누락 요소 검사의 검증 루프. 2024-10 개정.",
      "as_of": "2024-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "연계 대상: ISO 3691-4:2023 은 무인 산업용 트럭과 그 시스템의 안전 요구사항과 검증 수단을 정하고, 트럭이 안전하게 운행하도록 운행 구역을 준비하는 요구를 부속서 A 에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약(ISO 소개): 무인 산업용 트럭과 시스템의 안전 요구와 검증; 운행 구역 상태가 안전 운행에 큰 영향을 주며 구역 준비는 부속서 A 에 규정.",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "한국산업기술시험원(KTL)과 한국통합물류협회(KILA)는 2026-07-23 물류로봇·자동화 설비의 시험·인증과 표준화 협력 업무협약을 맺고, AMR·AGV·팔레타이징 로봇·모바일 매니퓰레이터·자율주행 지게차의 성능·안전성 검증을 KTL 테스트베드와 회원사 물류센터를 잇는 연구개발–시험평가–현장 실증 체계로 지원하겠다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-639"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사 요약: 2026-07-23 MOU, KILA 168개 회원사, 대상 로봇 5종, KTL 테스트베드와 실제 물류창고 연계. 협약 단계이며 실적은 미확인.",
      "as_of": "2026-07-24",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "Siemens 는 고객사례에서 IDC 가 가상 시운전(virtual commissioning)으로 코드를 시스템 설계와 대조 검증해 현장에서 큰 변경이 필요 없었고 가동 개시를 3주 앞당겼다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-640"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 가상 시운전으로 launch time 3주 단축, 현장에서 큰 변경 불필요. 비교 기준·현장 조건 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "vendor_claim": true,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "f1~f8·f11·f13 을 종합하면 새 제조사 로봇이나 새 현장을 추가할 때 반복되는 작업은 로봇 신원·기능·제약 등록(팩트시트·신원 보고·어댑터 설정), 지도·레이아웃·경로망 작성과 가져오기, 제조사 지도와 공통 지도의 좌표 대응, 연동 수준 선택으로 나눌 수 있고, 앞의 등록 항목은 표준 메시지로 받을 수 있으나 경로망 설계와 좌표 대응은 여전히 사람의 설정 작업으로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-228",
        "ref-230",
        "ref-153",
        "ref-079",
        "ref-217",
        "ref-269"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "팩트시트·identityReport 는 등록 정보를 표준화(f1·f2·f6), 경로 설정은 VDA 5050 범위 밖(f4), traffic-editor 는 사람 주석(f8), 경로망 수작업은 도입 병목(f11·f13). 이 위키의 종합 추론.",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "이번에 확인한 범위의 팩트시트 스키마 최상위 절과 신원 보고 필드에는 제조사 지도와 공통(관제) 지도 사이의 좌표 대응을 담는 항목이 보이지 않고, Open-RMF 는 이를 현장별 어댑터 설정(reference_coordinates)으로 두므로, 좌표 정합은 현장 시운전의 설정·검증 항목으로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-230",
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "factsheet.schema 7개 절, identityReport 필드 목록에 좌표 대응 항목 없음(부재 확인 아닌 관찰), Open-RMF 는 대응점 쌍 설정으로 변환.",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "제약"
    },
    {
      "id": "f23",
      "claim": "연계 대상: 로봇 자체의 SLAM 지도 작성·위치 추정·센서 교정은 제조사 몫이고, 관제 인터페이스가 제공하는 것(팩트시트 요청, 지도 배포 지시, 레이아웃 가져오기, 어댑터 설정)을 보면 이종 로봇을 연결하는 ROP 는 로봇 등록 정보의 수집·검증, 레이아웃·좌표 대응 설정, 연동 수준 결정과 그 설정의 버전 관리를 맡는 경계가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-153",
        "ref-251"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 은 지도 배포 동작과 팩트시트만 정하고 경로 설정은 범위 밖(f3·f4), Open-RMF 는 어댑터 설정·연동 수준을 통합 측에 둠(f7·f10). 분류 원문 9장 '로봇 자체 지능·제어' 경계 적용.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
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
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. 팩트시트, 지도 배포 동작, 도입 단계, LIF 언급을 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "MassRobotics AMR 상호운용 표준의 JSON 스키마. 신원 보고(identityReport)와 상태 보고 필드 정의.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration)",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 플릿 어댑터 연동 수준(Full Control·Traffic Light·Read Only) 설명. 이번 실행에서는 다시 열지 않고 이전 실행(2026-09-25-50) 확인 내용을 재인용.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
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
      "summary": "VDA 5050 팩트시트 JSON 스키마. 로봇 유형 사양·물리 파라미터·프로토콜 한계·기능·기하·적재·구성 절을 정의하고 관제 통합 용도를 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — traffic-editor",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF traffic-editor 사용법. 평면도 배경, 측정으로 축척 설정, 벽·문·승강기·차선·충전기 주석, 기준점으로 층 정렬.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 튜토리얼. 설정 파일의 로봇 사양·작업 능력·좌표 변환 대응점·제조사 관제 연결 항목 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets_adapter_tutorial.md",
      "source_unopened": false
    },
    {
      "id": "ref-229",
      "org": "IDTA (admin-shell-io/submodel-templates)",
      "title": "IDTA 02020 Submodel Capability Description 1.0 — README",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "자산관리셸 능력 기술 서브모델 1.0 소개. 요구 능력과 제공 능력의 비교, 생산 계획·오케스트레이션 지원.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Capability%20Description/1/0/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDMA LIF 1.0.0 공식 저장소 README. 통합사업자가 간선·노드·스테이션 레이아웃을 제3자 관제에 넘기는 교환 형식.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Intralogistics-2X-LIF/Layout-Interchange-Format/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-217",
      "org": "Beinschob, P. 외",
      "title": "Semi-automated map creation for fast deployment of AGV fleets in modern logistics",
      "published": "2017",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Robotics and Autonomous Systems 87권. 다중 AGV 도입 병목(정밀 지도, 픽업·하역 위치, 경로망 설계)을 3D 의미 지도로 반자동화.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-269",
      "org": "Heselden, J. R., & Das, G. P.",
      "title": "Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.13499",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 새 환경 배치의 지도 작성 부담을 줄이는 표준화된 지도 처리 방식과 관리 스크립트 제안(ICRA 2024 워크숍).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-037",
      "org": "Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A.",
      "title": "Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.00827",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플러그 앤 프로듀스를 위한 능력·스킬 모델의 온톨로지 방식과 자산관리셸 방식 사이 대응 제안.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-637",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 자연어 능력 설명에서 능력 온톨로지를 생성하고 구문·모순·환각 검사로 검증하는 방법.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업용 트럭과 시스템의 안전 요구·검증, 운행 구역 준비(부속서 A).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-639",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KTL 과 한국통합물류협회의 물류로봇 시험·인증·표준화 업무협약(2026-07-23) 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-640",
      "org": "Siemens Digital Industries Software",
      "title": "Virtual commissioning with Siemens solutions reduces launch time by three weeks",
      "published": null,
      "url": "https://resources.sw.siemens.com/en-US/case-study-idc/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IDC 고객사례: 가상 시운전으로 가동 개시 3주 단축(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-265",
      "org": "European Commission CORDIS",
      "title": "PAN-ROBOTS: Automating logistics for the factory of the future",
      "published": null,
      "url": "https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU FP7 PAN-Robots 과제 결과 소개. 반자동 공장 탐사로 설치 기간 6개월→2개월(과제 측 보고).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철 (한국로봇학회)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇학회 논문지 21권 1호. 자율 탐사와 로봇팔 승강기 조작으로 다층 실내 지도를 자율 구축.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-643",
      "org": "Open Robotics (open-rmf/rmf_site)",
      "title": "rmf_site — README (RMF Site Editor)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_site",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor 소개.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_site/main/README.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
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
      "rationale": "3절 왜 중요한가: f11·f13(설치 시간 원인, 트랙 반영 제안 2026-09-25-22 재확인), f12(PAN-Robots 6→2개월, 추정), f21(SCM 질문 연결) / 4절 용어: 팩트시트(f1·f2, 기존 용어), 신원 보고(f6), LIF(f5, 기존 용어), 기준점(f8), 가상 시운전(f20), 플러그 앤 프로듀스(f16) / 5절 시나리오: 적치 단계에 새 제조사 AMR 추가 — 수행 자원 f6·f7·f21, 제약 f22·f18, 예외·성과 f12·f20 / 6절 접근법: 표준 등록 메시지 f1·f2·f6, 어댑터 설정 f7, 평면도 주석·측정 축척 f8·f9(트랙 반영 제안 2026-09-25-11 재확인), 연동 수준 선택 f10, 반자동·자율 지도 작성 f11·f13·f14(트랙 반영 제안 2026-09-25-19 재확인), 능력 기술·매칭 f15·f16, 문서 해석 AI f17 / 7절 표준·오픈소스: VDA 5050(f1~f4), LIF(f5), MassRobotics(f6), Open-RMF(f7~f10), IDTA 02020(f15), ISO 3691-4(f18, 연계 대상), 국내 KTL–KILA 체계(f19) / 8절 연구: f11·f13·f14·f16·f17 / 9절 범위: f23(로봇 자체 SLAM·교정은 연계 대상), f18 / 10절 연결: 5. 로봇 능력·작업 온톨로지(f15~f17), 6. 지도·공간·위치 모델(f8·f13·f22), 9. 로봇·제조사 관제 연동(f1·f6·f7·f10), 10. 설비·건물 시스템 연동(f14 승강기), 22. 시뮬레이션·예측용 디지털 트윈(f2·f20), 23. 시험·형식 검증·벤치마크(f19), 24. 자산·소프트웨어 수명주기 관리(f3 지도 버전), 25. 안전·위험 관리(f18), 27. AI·학습·적응과 모델 운영(f17, 교차 규칙) / 11절 열린 질문: oq-022(미해결)와 새 질문 2건. 트랙 반영 제안 가운데 MiR·OTTO 벤더 주장(ref-271 등), Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 이번에 다시 확인하지 않아 다음 실행 후보로 남긴다"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "가상 시운전",
      "term_en": "Virtual Commissioning",
      "definition": "제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다."
    },
    {
      "term_ko": "플러그 앤 프로듀스",
      "term_en": "Plug and Produce",
      "definition": "새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다."
    },
    {
      "term_ko": "신원 보고",
      "term_en": "Identity Report (MassRobotics identityReport)",
      "definition": "MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다."
    }
  ],
  "open_questions_new": [
    "국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동 | 근거: f21 | 종류: 일반",
    "제조사 로봇 지도와 공통 관제 지도 사이 좌표 대응(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음: 항목마다 단일 출처(f1 의 두 출처는 같은 저장소라 독립 아님)",
      "f11·f13·f14·f16·f17·f18: 원문 미열람, 검색 요약 범위",
      "f12 PAN-Robots 6→2개월: 과제 측 보고값, 비교 조건 미확인",
      "f19 KTL–KILA 협약: 기사만 확인, 기관 보도자료 원문 미확인",
      "f20 Siemens 가상 시운전 3주 단축: 벤더 주장, 독립 확인 없음",
      "f22: 팩트시트 최상위 절과 신원 보고 필드 범위의 부재 관찰이며 하위 필드 전체 확인 아님",
      "ISO 3691-4 의 시운전 절차·통합사업자 책임 구분은 제3자 해설에서만 보여 finding 으로 내지 않음",
      "oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 한국어 검색 2회에서 찾지 못함"
    ],
    "scope_violations": [
      "f18: ISO 3691-4 는 설비·차량 안전 영역(25. 안전·위험 관리, 분류 원문 9장 연계)이라 '연계 대상: '으로 표시하고 운행 구역 준비 요구만 시운전 제약으로 연결",
      "f23: 로봇 자체 SLAM·위치 추정·센서 교정은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역으로 구분",
      "f14: 로봇팔 승강기 조작 자율 지도 작성은 로봇 자체 기능 연구이므로 8절 연구 사례로만 두고 ROP 직접 범위로 서술하지 않도록 제안"
    ],
    "budget_used": {
      "queries": 18,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-230(재사용), ref-228·ref-079·ref-153·ref-229·ref-046·ref-643(신규). 그 밖의 신규 출처(ref-217~ref-163)와 재사용 ref-251 는 원문 미열람(신뢰도 상한 medium, 모든 finding medium 이하). 검색 18회/30, 신규 출처 15건/15(ref-228~ref-643, 예약 구간 안) — 신규 출처 상한 도달로 MiR·OTTO 벤더 문서, Boniardi 외 2019, 다중 AGV 경로망 자동 설계(IEEE T-ASE 2024), Rüdt 외 2025, 문서 해석 LLM(기술 매뉴얼 지식 추출) 논문은 추가하지 않았다. 입력의 참고문헌 목록이 요약본(0건 표시)이라 트랙 반영 제안이 인용한 ref-217·ref-265·ref-269 등의 서지 정보를 몰라 재사용하지 못하고, 같은 문헌(Beinschob 외 2017, PAN-Robots CORDIS, Heselden·Das 2024)을 새 id(ref-217·ref-265·ref-269)로 다시 적었다 — 같은 URL 이면 퍼블리셔가 기존 id 로 합쳐야 한다. ref-251 는 이전 브리프(2026-09-25-50) 값을 재인용. 트랙 반영 제안 6건 가운데 traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)는 이번 finding 으로 재확인했고, 나머지는 페이지 제안 rationale 에 다음 실행 후보로 적었다. 한국 자료: KTL–KILA 협약(f19, 기사), 한국로봇학회 논문(f14). 한국어 검색에서 나온 블로그·업체 홍보 글은 쓰지 않았다. 교차 규칙: 문서 해석 AI(f17)는 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 연구 방법으로 27. AI·학습·적응과 모델 운영 연결을 제안. 8. 실시간 세계 상태·데이터 일관성 관련 주장 없음, 22. 시뮬레이션·예측용 디지털 트윈은 가상 시운전(f20)·팩트시트의 시뮬레이션 용도(f2) 연결로만 제안. 정정 요청 없음. oq-022 는 해결하지 못함."
  }
}
```

### runs/2026-09-25-52/verification.json

```json
{
  "run_id": "2026-09-25-52",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 표 2(4.3절 토픽 표)에 factsheet 토픽 설명 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control', 표 4에 factsheetRequest 즉시 동작이 있다. evidence_excerpt 가 인용 위치를 '6.10절'로 적었지만 입력 원문에서 확인한 위치는 표 2다(6.10절 본문은 발췌 범위 밖). ref-228 는 같은 저장소라 독립 출처가 아니다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 검증자가 raw factsheet.schema 를 직접 열어 확인했다. 최상위 required 배열은 headerId·timestamp·version·manufacturer·serialNumber 와 내용 절 여섯 개(typeSpecification, physicalParameters, protocolLimits, protocolFeatures, mobileRobotGeometry, loadSpecification)다. mobileRobotConfiguration 은 필수가 아니다(선택 절이며 버전과 충전 파라미터를 담는다). 그래서 '일곱 절 필수'는 원문과 다르다. 스키마 설명문(로봇 유형 비교, 계획·규모 산정·시뮬레이션, VDA 5050 준수 관제로의 통합에 필요한 통신 인터페이스 정보)은 원문과 맞는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 표 4(downloadMap: mapId·mapVersion·mapDownloadLink·선택 mapHash, enableMap, deleteMap)와 6.3.1절(관제가 즉시 동작으로 지도 서버에서 끌어오는 pull 방식 다운로드를 지시, 내려받기와 활성화는 별도 과정)에 있다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 5.2절(경로 정의·경로망 구성·로봇 구성, 'not part of this document', LIF – VDMA 2024-03). 2절 범위 제외 항목에도 commissioning workflows 가 있다. LIF 기준일이 ref-046(1.0.0, 2023-09)과 다르다(f5 비고)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw README 를 열었다. 1.0.0(2023-09), 통합사업자가 제3자 중앙 관제에 주행 레이아웃을 처음 넘기는 형식, edges·nodes·stations, 'non-binding approach'. VDA 5050 3.0.0 명세(ref-031)는 LIF 를 'VDMA 2024-03'으로 인용하므로 기준일 표기가 두 출처에서 다르다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw AMR_Interop_Standard.json 을 열었다. identityReport 필수 6개가 일치한다. 선택 필드는 브리프 목록 외에 emergencyContactInformation·supportVendorContactInformation·thumbnailImage 도 있다(브리프 목록은 일부 나열이다)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw integration_fleets_adapter_tutorial.md 를 열었다. limits·profile·battery_system·mechanical_system·reversible·task_capabilities(loop·delivery·clean)·finishing_request·reference_coordinates(대응 웨이포인트 최소 4개 권장)·fleet_manager(prefix·인증), 제공 필드 밖을 쓰면 가져오기 오류라는 경고가 있다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw traffic-editor.md 를 열었다. 평면도 배경, 두 점 측정선으로 축척, 정점(충전기 등 속성)·벽·문·승강기·차선 주석, 수직 정렬 기준점(fiducial)으로 층간 변환, 'standardized, vendor neutral manner through a graphical interface'. 기본 축척 1픽셀=5cm 는 검증자 열람 응답에서 확인하지 못했다(주장 본문에는 없다)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw rmf_site README 를 열었다. 'experimental approach to visualizing and editing large RMF deployment sites', rmf_site_cmake 로 시뮬레이션·주행 그래프 생성, Rust·Bevy 기반 웹·데스크톱."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "조건부 유지: 검증자가 raw integration_fleets.md(ref-251)를 열었다. 여기에는 Full Control(경로 지정·언제든 교체)과 Traffic Light(일시정지·재개만)만 있고 'Read Only' 문구는 없다. Read Only(제어권 없이 상태만 보고)는 raw rmf-core.md(ref-004)에서 확인했다. 두 문서는 같은 책이라 독립 출처가 아니다. 마지막 절 '온보딩 때 연동 수준이 선택 사항'은 출처 문장이 아니라 추론이다. 브리프 표시는 ref-251 fetched false 그대로이며 원문 미열람이다(검증자 열람으로 실재 확인)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): ScienceDirect·ResearchGate·Scilit 검색 결과에서 Beinschob·Meyer·Reinke·Digani·Secchi·Sabattini, RAS 87권 281–295쪽(2017), 정밀 2D 지도·픽업·하역 3D 지리 참조·수작업 경로망 병목, 레이저 스캐너 3D 의미 지도, 경로망 자동 설계, PAN-Robots(FP7)가 일치한다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): CORDIS 기사 제목·URL 이 일치하고, '6개월 대신 2개월' 설치는 검색 요약에 나온다. '기존 표지 활용 위치추정·반자동 공장 탐사 덕분'이라는 원인 서술은 검증자 검색 요약에서 확인하지 못했다. 과제 측 보고값이므로 [추정] 유지가 맞다. 발행일 미확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): arXiv 2404.13499, Heselden·Das, 지도 작성은 새 환경 배치의 시간 소모 과정, 전역 위치·물체 위치·위상·점유 중심 표준 처리, 템플릿·절차적 생성, ICRA 2024 Field Robotics 워크숍."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "조건부 유지(원문 미열람, 검색 결과 일치): KCI 서지(노주형·강규리·김연찬·심현철, 한국로봇학회 논문지 21권 1호 48–57쪽, 2026)가 일치한다. 검색 요약에서 3D LiDAR–IMU SLAM, 다중 센서 융합 비용 지도, RGB-D·4자유도 매니퓰레이터 버튼 조작, 처음부터 끝까지 완전 자율 다층 지도 구축을 확인했다. '사물인터넷 장치 개조나 외부 시스템 연동 없이'는 검증자 검색 요약에 나타나지 않았다. 로봇 자체 기능 연구이므로 범위상 8절 사례로만 둔다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw Capability Description 1/0 README 를 열었다. 'enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes', 버전 1.0 은 IDTA 첫 공식 발행판이다. 브리프는 fetch_url 을 적었지만 fetched false·source_unopened true 로 표시했다(과소 표시라 수정 지시 대상 아님)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): arXiv 2307.00827, Vieira da Silva·Köcher·Gill·Weiss·Fay(HSU), ETFA 2023(IEEE Xplore 10275459). plug and produce 원칙, 온톨로지 방식과 AAS 서브모델 방식이 서로 호환되지 않음, 양방향 대응 개념."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): arXiv 2406.07962, Vieira da Silva·Köcher·Gehlhoff·Fay. 자연어 설명 → few-shot 프롬프트 → LLM 이 능력 온톨로지 생성 → 구문·모순·환각·누락 검사 루프. 2024-10-18 개정. 교차 규칙상 27. AI·학습·적응과 모델 운영 연결이 필요하다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): ISO 3691-4:2023 소개 페이지(iso.org/standard/83545). 무인 산업용 트럭과 시스템의 안전 요구·검증 수단, 운행 구역 상태가 안전 운행에 큰 영향을 주고 구역 준비는 부속서 A 에 규정. 연계 대상 표시가 적절하다(25. 안전·위험 관리)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): 부산일보 기사와 URL 이 일치하고 헬로티·데일리안·경남일보·네이트 뉴스도 같은 내용(2026-07-23 MOU, KILA 168개 회원사, AMR·AGV·팔레타이징 로봇·모바일 매니퓰레이터·자율주행 지게차, KTL 테스트베드–회원사 물류센터 연계, 단체표준 개발)을 보도한다. 다만 모두 같은 기관 발표에서 나온 보도라 독립 교차 확인으로 보지 않는다. 협약 단계이며 실적은 미확인이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치), 벤더 주장 [추정] 유지. 제목 'reduces launch time by three weeks'가 일치한다. 검색 요약상 내용은 IDC 가 Tecnomatix Plant Simulation 으로 고속 분류기(sortation)를 가상 시운전해, 현장 시운전만 한 유사 업그레이드 프로젝트(8주)보다 시운전 기간을 3주 줄였다는 것이다(파트너 Simsol). 브리프의 '비교 기준 미확인'은 검색 요약과 다르고, '코드를 설계와 대조 검증해 현장에서 큰 변경 불필요'는 검증자 검색 요약에서 확인하지 못했다. 발행일 미확인."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 이 위키의 종합 추론이다. 근거 finding(f1·f4·f6·f7·f8·f11·f13)은 살아남았다. f2 가 강등됐으므로 f2 를 인용하는 부분은 정정된 f2 기준으로 쓴다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 검증자 열람에서도 factsheet.schema 에 좌표 변환·지도 정합 전용 필드가 없었고 identityReport 에도 없었다. MassRobotics statusReport 의 location 에는 사용 좌표계를 가리키는 planarDatum 참조가 있지만 좌표 대응 자체는 아니다. 브리프의 '팩트시트 최상위 절(7개)' 표현은 f2 정정(필수 6절 + 선택 mobileRobotConfiguration)에 맞춰야 한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 분류 원문 9장 '로봇 자체 지능·제어' 경계를 적용한 추론이며 연계 대상 표시가 있다. 근거 f3·f4·f7·f10 이 살아남았다(f10 의 Read Only 근거는 ref-004)."
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
      "f11·f12·f13 과 트랙 반영 제안(2026-09-25-19·22)이 같은 문헌이다: Beinschob 외 2017(제안 ref-217 ↔ 이번 ref-217), PAN-Robots CORDIS(ref-265 ↔ ref-265), Heselden·Das 2024(ref-269 ↔ ref-269). 같은 URL 이면 퍼블리셔가 기존 id 로 합쳐야 한다.",
      "f7(ref-153 플릿 어댑터 튜토리얼)이 트랙 반영 제안의 ref-105(플릿 어댑터 설정)와 같은 문서일 수 있다(퍼블리셔 URL 병합 확인 필요).",
      "f10 은 실행 2026-09-25-50 브리프 f9(ref-251·ref-004)와 같은 주장이다. 같은 각주를 재사용한다.",
      "f4(ref-031 이 인용한 LIF 'VDMA 2024-03')와 f5(ref-046 LIF 1.0.0, 2023-09)의 기준일 표기가 다르다(출처 충돌 — 둘 다 제시)."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "브리프의 '좌표 대응·좌표 정합'(f7·f22·새 열린 질문)은 용어집 map-alignment '지도 정합 (Map Alignment)'과 같은 개념으로 보인다. 페이지 4절 용어 설명에서는 용어집 표기 '지도 정합'을 쓰고 대응점 설정을 그 방법으로 설명해야 한다.",
      "팩트시트는 용어집 vda-5050-factsheet 'VDA 5050 팩트시트', LIF 는 layout-interchange-format '레이아웃 교환 형식', 경로망은 roadmap, 플릿 어댑터는 fleet-adapter 로 이미 있다. 새로 등록하지 말고 연결만 한다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f2: 본문에서 '일곱 절을 필수로 둔다'를 '유형 사양·물리 파라미터·프로토콜 한계·프로토콜 기능·로봇 기하·적재 사양의 여섯 절(과 헤더 필드)을 필수로 두고, 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)은 선택 절로 둔다'로 고치고 태그를 [추정]으로 강등한다. 이유: 검증자가 연 factsheet.schema 의 required 배열에 mobileRobotConfiguration 이 없다.",
    "f22: '팩트시트 스키마 최상위 절' 서술이 f2 의 '일곱 절'을 전제하지 않게 '필수·선택 최상위 절'로 고친다. 태그는 [추정]을 유지한다.",
    "f10: Full Control·Traffic Light 문장에는 [^ref-251], Read Only 문장에는 공통 참고문헌 [^ref-004](RMF Core Overview)를 붙이고, '새 플릿 온보딩 때 어느 수준으로 연동할지가 선택 사항이 된다'는 부분은 별도 문장의 [추정]으로 분리한다. 이유: ref-251 원문에는 Read Only 문구가 없고 ref-004(rmf-core)에 있다.",
    "f14: '사물인터넷 장치 개조나 외부 시스템 연동 없이' 구절을 뺀다. 검색 요약에서 확인되지 않았다. 이 연구는 8절(대표 연구와 자료)의 사례로만 두고 ROP 직접 범위로 서술하지 않는다(로봇 자체 지능·제어 연계 영역).",
    "f20: [추정]·'벤더 주장' 병기를 유지한다. 비교 기준은 '현장 시운전만 한 유사 업그레이드 프로젝트(8주) 대비 시운전 기간 3주 단축(고속 분류기, Tecnomatix Plant Simulation)'으로 적는다. '코드를 시스템 설계와 대조 검증해 현장에서 큰 변경이 필요 없었다'는 빼거나 벤더 서술임을 명시한다. 이유: 검색 요약에 비교 기준이 있고 앞 구절은 확인되지 않았다.",
    "f4·f5: 7절에서 LIF 를 소개할 때 기준일을 둘 다 제시한다('VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용 [^ref-031]', 'LIF 공식 저장소는 1.0.0 을 2023-09 로 표기 [^ref-046]'). 11절에 '레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델 | 근거: f4, f5 | 종류: 출처 충돌' 열린 질문을 올린다. 이유: 두 출처가 다르면 한쪽을 고르지 않는다.",
    "f12: PAN-Robots '6개월 → 2개월'은 [추정]과 '과제 측 보고값, 비교 조건 미확인'을 유지하고, 원인 설명(기존 표지 활용 위치추정·반자동 공장 탐사)은 과제 측 서술로만 적는다.",
    "4절 용어: '좌표 대응·좌표 정합'은 용어집 '지도 정합 (Map Alignment)' 표기로 통일한다. 팩트시트·LIF·경로망·플릿 어댑터는 기존 용어집 항목에 연결하고 신규 등록하지 않는다. glossary_updates 신규 후보는 가상 시운전·플러그 앤 프로듀스·신원 보고 3건만 둔다.",
    "각주: 모든 각주 정의가 이번 실행의 원문 열람 여부를 따르게 한다. ref-251·ref-229·ref-217~ref-163 는 접근일 뒤 ' (원문 미열람)'을 붙이고 reference_updates[].source_unopened: true 로 둔다. ref-004 는 공통 참고문헌 페이지의 각주 형식 줄을 그대로 복사한다.",
    "10절 연결: f17(문서 해석 LLM)은 교차 규칙대로 5. 로봇 능력·작업 온톨로지와 27. AI·학습·적응과 모델 운영 양쪽에 연결한다. 22. 시뮬레이션·예측용 디지털 트윈 연결은 가상 시운전(f20)·팩트시트의 시뮬레이션 용도(f2)로 한정하고, 8. 실시간 세계 상태·데이터 일관성과 섞지 않는다.",
    "트랙 반영 제안: 이번 브리프 finding 이 다시 확인한 내용(traffic-editor f8, 플릿 어댑터 설정 f7, Beinschob 외 f11, Heselden·Das f13, PAN-Robots f12)만 반영한다. MiR·OTTO 벤더 주장(ref-271·ref-219), Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 본문에 넣지 않고 다음 실행 후보로 둔다. 이유: 이번 실행에서 검증하지 않았다.",
    "f1: 팩트시트 토픽 설명의 인용 위치는 'VDA 5050 3.0.0 표 2(4.3절)'로 적는다. 직접 인용은 이 출처당 1회만 한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. GitHub 원문(ref-031 입력 원문, ref-228·ref-230·ref-153·ref-079·ref-643·ref-046·ref-229, ref-251·ref-004 는 검증자 열람)은 직접 대조했고, 나머지는 검색 결과 일치로 확인했다. 확인 22건, 미확인 1건, 교차 확인 0건. 강등: f2 사실 → 추정(팩트시트 필수 절은 6개이고 mobileRobotConfiguration 은 선택). 원문 미열람 출처: ref-217, ref-269, ref-037, ref-637, ref-470, ref-639, ref-640, ref-265, ref-163(ref-251·ref-229 는 브리프에 미열람으로 표시됐으나 검증자가 GitHub 원문으로 실재를 확인). 주의: 모든 주장이 단일 출처이다. 설치 기간 단축 수치(PAN-Robots 6→2개월, Siemens 3주)는 과제·벤더 측 보고값이다. f21~f23 은 이 위키의 종합 추론이다. f10 의 Read Only 근거는 ref-004 다. LIF 기준일은 두 출처가 다르다(2023-09 대 VDMA 2024-03). oq-022 는 해결되지 않았다. 정정 요청 없음. 검색은 리서치 18회와 검증 11회로 합계 29회/30이다.",
  "retry_reason": null
}
```

### runs/2026-09-25-52/pages.json

```json
{
  "run_id": "2026-09-25-52",
  "outline": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 550,
      "summary": "새 로봇·새 현장 도입이 오래 걸리는 원인으로 정밀 지도 작성, 픽업·하역 위치 지정, 수작업 경로망 설계가 꼽힌다. [사실][^ref-217]",
      "planned_findings": [
        "f11",
        "f13",
        "f12",
        "f21"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 650,
      "summary": "온보딩의 핵심 용어는 VDA 5050 팩트시트, 신원 보고, 레이아웃 교환 형식, 경로망, 플릿 어댑터, 지도 정합, 가상 시운전, 플러그 앤 프로듀스다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f16",
        "f20"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 800,
      "summary": "적치 단계에 새 제조사 AMR 을 추가하는 가상 시나리오로, 등록 정보는 표준 메시지로 받지만 경로망·지도 정합은 사람의 설정으로 남는다. [추정][^ref-217]",
      "planned_findings": [
        "f6",
        "f7",
        "f21",
        "f22",
        "f18",
        "f3",
        "f12",
        "f20"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1100,
      "summary": "표준 등록 메시지, 어댑터 설정과 연동 수준 선택, 평면도 주석·레이아웃 가져오기, 반자동 지도 작성, 능력 기술·문서 해석 AI, 가상 시운전의 여섯 접근이 있다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f13",
        "f15",
        "f16",
        "f17",
        "f20"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 500,
      "summary": "VDA 5050 3.0.0·팩트시트 스키마, LIF, MassRobotics, Open-RMF 도구, IDTA 02020 이 온보딩 정보를 다루고 ISO 3691-4:2023 은 연계 대상이다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f15",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 550,
      "summary": "지도 작성 반자동화(Beinschob 외 2017, Heselden·Das 2024)와 능력 모델 대응·LLM 온톨로지 생성(Vieira da Silva 외) 연구가 대표적이다. [사실][^ref-217]",
      "planned_findings": [
        "f11",
        "f13",
        "f14",
        "f16",
        "f17",
        "f12",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 450,
      "summary": "로봇 자체 SLAM·위치 추정·교정은 제조사 몫이고, 이종 로봇을 잇는 ROP 는 등록 정보 검증·레이아웃과 지도 정합 설정·연동 수준 결정과 그 버전 관리를 맡는 것으로 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f23",
        "f18",
        "f8"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 550,
      "summary": "능력 기술은 5. 로봇 능력·작업 온톨로지, 지도 정합은 6. 지도·공간·위치 모델, 등록 메시지는 9. 로봇·제조사 관제 연동과 이어진다. [사실][^ref-228]",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f8",
        "f22",
        "f1",
        "f6",
        "f7",
        "f10",
        "f14",
        "f2",
        "f20",
        "f19",
        "f3",
        "f18"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "section": "11. 열린 질문",
      "budget_chars": 400,
      "summary": "국내 표준 등록 정보 적용 사례, 지도 정합 합격 기준, LIF 기준일 충돌, oq-022 도면 활용 사례가 열려 있다.",
      "planned_findings": [
        "f4",
        "f5",
        "f21",
        "f22"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성, 13절 각주 19건, page-status 마커 추가, 트랙 반영 제안 중 재확인된 5건 반영"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area21-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 온보딩·설정·현장 시운전 의 \"6. 대표 접근법과 기술\" 절(1,742자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area21-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 온보딩·설정·현장 시운전 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(936자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area21-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 온보딩·설정·현장 시운전 의 \"4. 핵심 개념과 용어\" 절(914자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area21-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 온보딩·설정·현장 시운전 의 \"8. 대표 연구와 자료\" 절(871자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 21. 온보딩·설정·현장 시운전 | 영역 심화: 3~11절 신규 작성(표준 등록 메시지·어댑터 설정·평면도 주석·반자동 지도 작성·가상 시운전, 적치 시나리오) | run 2026-09-25-52",
  "index_updates": {
    "home_recent": "2026-09-25 — 21. 온보딩·설정·현장 시운전: 영역 심화 초안 작성(등록 표준 메시지, 지도 정합, 반자동 지도 작성, 가상 시운전)",
    "category_recent": "2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 초안 작성, 적치 단계 새 제조사 AMR 시운전 시나리오",
    "area_recent": "2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 신규 작성, 트랙 반영 제안 가운데 재확인된 5건 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "virtual-commissioning",
      "term_ko": "가상 시운전",
      "term_en": "Virtual Commissioning",
      "definition": "제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다.",
      "description": "효과 수치는 현재 벤더 사례(시운전 기간 3주 단축, 벤더 주장)로만 확인됐다.",
      "related_areas": [
        21,
        22
      ],
      "sources": [
        "ref-640"
      ]
    },
    {
      "action": "new",
      "slug": "plug-and-produce",
      "term_ko": "플러그 앤 프로듀스",
      "term_en": "Plug and Produce",
      "definition": "새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다.",
      "description": "능력·스킬 기술에는 온톨로지 방식과 자산관리셸 서브모델 방식이 있으며 서로 호환되지 않아 대응이 연구되고 있다.",
      "related_areas": [
        21,
        5
      ],
      "sources": [
        "ref-037"
      ]
    },
    {
      "action": "new",
      "slug": "identity-report",
      "term_ko": "신원 보고",
      "term_en": "Identity Report (MassRobotics identityReport)",
      "definition": "MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다.",
      "related_areas": [
        21,
        9
      ],
      "sources": [
        "ref-230"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-24",
      "summary": "원문 미열람. Open-RMF 핵심 구성 개요. 이번 페이지에서는 읽기 전용(Read Only) 플릿 연동 수준의 근거로 인용.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. 팩트시트, 지도 배포 동작, 도입 단계, LIF 언급을 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration)",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 플릿 어댑터 연동 수준(Full Control·Traffic Light) 설명.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "MassRobotics AMR 상호운용 표준의 JSON 스키마. 신원 보고(identityReport)와 상태 보고 필드 정의.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
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
      "summary": "VDA 5050 팩트시트 JSON 스키마. 필수 여섯 절(유형 사양·물리 파라미터·프로토콜 한계·프로토콜 기능·로봇 기하·적재 사양)과 선택 로봇 구성 절, 관제 통합 용도 설명.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — traffic-editor",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF traffic-editor 사용법. 평면도 배경, 측정으로 축척 설정, 벽·문·승강기·차선·충전기 주석, 기준점으로 층 정렬.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 튜토리얼. 설정 파일의 로봇 사양·작업 능력·좌표 변환 대응점·제조사 관제 연결 항목 설명.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-229",
      "org": "IDTA (admin-shell-io/submodel-templates)",
      "title": "IDTA 02020 Submodel Capability Description 1.0 — README",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자산관리셸 능력 기술 서브모델 1.0 소개. 요구 능력과 제공 능력의 비교, 생산 계획·오케스트레이션 지원.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDMA LIF 1.0.0 공식 저장소 README. 통합사업자가 간선·노드·스테이션 레이아웃을 제3자 관제에 넘기는 교환 형식.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-217",
      "org": "Beinschob, P. 외",
      "title": "Semi-automated map creation for fast deployment of AGV fleets in modern logistics",
      "published": "2017",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Robotics and Autonomous Systems 87권. 다중 AGV 도입 병목(정밀 지도, 픽업·하역 위치, 경로망 설계)을 3D 의미 지도로 반자동화.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-269",
      "org": "Heselden, J. R., & Das, G. P.",
      "title": "Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.13499",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 새 환경 배치의 지도 작성 부담을 줄이는 표준화된 지도 처리 방식과 관리 스크립트 제안(ICRA 2024 워크숍).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-037",
      "org": "Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A.",
      "title": "Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.00827",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플러그 앤 프로듀스를 위한 능력·스킬 모델의 온톨로지 방식과 자산관리셸 방식 사이 대응 제안.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-637",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 자연어 능력 설명에서 능력 온톨로지를 생성하고 구문·모순·환각 검사로 검증하는 방법.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업용 트럭과 시스템의 안전 요구·검증, 운행 구역 준비(부속서 A).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-639",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KTL 과 한국통합물류협회의 물류로봇 시험·인증·표준화 업무협약(2026-07-23) 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-640",
      "org": "Siemens Digital Industries Software",
      "title": "Virtual commissioning with Siemens solutions reduces launch time by three weeks",
      "published": null,
      "url": "https://resources.sw.siemens.com/en-US/case-study-idc/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IDC 고객사례: 고속 분류기 가상 시운전으로 현장 시운전만 한 유사 프로젝트(8주) 대비 시운전 기간 3주 단축(벤더 주장).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-265",
      "org": "European Commission CORDIS",
      "title": "PAN-ROBOTS: Automating logistics for the factory of the future",
      "published": null,
      "url": "https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU FP7 PAN-Robots 과제 결과 소개. 설치 기간 6개월→2개월(과제 측 보고, 비교 조건 미확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철 (한국로봇학회)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇학회 논문지 21권 1호. 자율 탐사와 로봇팔 승강기 조작으로 다층 실내 지도를 자율 구축.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    },
    {
      "id": "ref-643",
      "org": "Open Robotics (open-rmf/rmf_site)",
      "title": "rmf_site — README (RMF Site Editor)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_site",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor 소개.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가?",
      "areas": [
        21,
        9
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사 로봇 지도와 공통 관제 지도 사이 좌표 대응(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가?",
      "areas": [
        21,
        6,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가?",
      "areas": [
        21,
        6
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "적치",
      "item": "시작 조건",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    },
    {
      "step": "적치",
      "item": "작업 대상",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    },
    {
      "step": "적치",
      "item": "수행 자원",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    },
    {
      "step": "적치",
      "item": "제약",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    },
    {
      "step": "적치",
      "item": "완료·인계",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    },
    {
      "step": "적치",
      "item": "예외·성과",
      "link": "docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "21. 온보딩·설정·현장 시운전"
    }
  ],
  "standards_updates": [
    {
      "name": "RMF Site Editor (rmf_site)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_site",
      "related_areas": [
        21,
        6
      ],
      "summary": "대규모 Open-RMF 배치 현장을 시각화·편집하는 실험적 도구로, 프로젝트에서 시뮬레이션과 주행 그래프를 생성할 수 있다고 설명한다.",
      "ref_id": "ref-643"
    }
  ],
  "additional_research_requests": [
    "트랙 반영 제안 가운데 이번 실행에서 다시 확인하지 않은 항목(MiR 평면도 업로드·축척 요건 벤더 주장 ref-271 등, 충전기 마커 등록 절차 ref-219, OTTO 설정 복제·부분 재지도화, Boniardi 외 2019, Beinschob·Reinke 2015 ref-266, 다중 AGV 경로망 자동 설계 IEEE T-ASE 2024 ref-267, Rüdt 외 2025 ref-268, 국내 건설로봇 문헌고찰)을 다음 21. 온보딩·설정·현장 시운전 실행에서 검증해 6·8절에 반영할지 판단해야 한다.",
    "중복 id 병합 확인: ref-217↔ref-217(Beinschob 외 2017), ref-265↔ref-265(PAN-Robots CORDIS), ref-269↔ref-269(Heselden·Das 2024), ref-079↔ref-079(traffic-editor, 같은 URL), ref-046↔ref-046(LIF, 같은 URL), ref-470↔ref-470(ISO 3691-4, 같은 URL), ref-229↔ref-229(IDTA 02020, 같은 URL), ref-153↔ref-105 여부 — 퍼블리셔가 같은 URL 이면 기존 id 로 합쳐야 한다.",
    "3절·5절의 설치 기간 단축 수치(PAN-Robots 6→2개월, Siemens 3주)를 독립 출처로 교차 확인할 자료가 필요하다(현재 과제·벤더 측 보고값뿐).",
    "5절 완료·인계 칸: 현장 시운전의 합격 기준(지도 정합 오차, 위치 정확도 시험 방법)에 관한 표준·지침 근거가 필요하다(ISO 3691-4 시운전 절차 원문 또는 공인 해설).",
    "7절: KTL–KILA 협약(2026-07-23)의 기관 보도자료 원문과 이후 실증 실적 확인이 필요하다.",
    "11절 oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 추가 한국어 검색으로 찾아야 한다."
  ],
  "fixes_applied": [
    "f2 필수 절 정정 — 6절 '표준 메시지로 로봇 등록 정보 받기'에서 필수 여섯 절(과 헤더 필드)·선택 mobileRobotConfiguration 으로 고쳐 쓰고 [추정][^ref-228]로 강등했으며 7절 표 행도 [추정]으로 표기했다.",
    "f22 표현 정정 — 5절 제약 칸을 '팩트시트의 필수·선택 최상위 절과 신원 보고 필드'로 고쳐 쓰고 [추정]을 유지했다.",
    "f10 분리 — 6절에서 Full Control·Traffic Light 문장에 [사실][^ref-251], Read Only 문장에 [사실][^ref-004]를 붙이고 '온보딩 때 연동 수준이 선택 사항'은 별도 [추정] 문장으로 분리했으며 ref-004 각주는 공통 참고문헌 형식 줄을 그대로 옮겼다.",
    "f14 구절 삭제 — '사물인터넷 장치 개조나 외부 시스템 연동 없이'를 빼고 8절 연구 사례로만 두었으며 로봇 자체 기능 연구(연계 대상)임을 밝혔다.",
    "f20 비교 기준 — 4·5·6절에서 [추정] 벤더 주장을 유지하고 6절에 '현장 시운전만 한 유사 업그레이드 프로젝트(8주) 대비 3주 단축, 고속 분류기, Tecnomatix Plant Simulation'으로 적었으며 '코드를 설계와 대조 검증해 큰 변경 불필요' 구절은 뺐다.",
    "f4·f5 LIF 기준일 — 7절 표 아래에 'VDMA 2024-03 인용[^ref-031]'과 '1.0.0, 2023-09[^ref-046]'을 둘 다 제시하고, 11절과 open_question_updates 에 출처 충돌 질문을 올렸다.",
    "f12 — 3·5절에서 [추정]과 '과제 측 보고값, 비교 조건 미확인'을 유지하고, 6절에서 원인 설명은 'PAN-Robots 과제 측은 … 서술한다'로 과제 측 서술로만 적었다.",
    "4절 용어 — '좌표 대응·좌표 정합'을 용어집 '지도 정합 (Map Alignment)'으로 통일하고 대응점 설정을 그 방법으로 설명했으며, 팩트시트·LIF·경로망·플릿 어댑터는 기존 용어집 링크만 걸고 glossary_updates 는 가상 시운전·플러그 앤 프로듀스·신원 보고 3건만 냈다.",
    "각주 — ref-251·ref-229·ref-217~ref-163 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true 로 두었으며, ref-004 는 공통 참고문헌 각주 형식 줄을 그대로 복사했다.",
    "10절 연결 — f17 을 5. 로봇 능력·작업 온톨로지와 27. AI·학습·적응과 모델 운영 양쪽에 연결했고, 22. 시뮬레이션·예측용 디지털 트윈 연결은 가상 시운전·팩트시트의 시뮬레이션 용도로 한정했으며 8. 실시간 세계 상태·데이터 일관성은 연결하지 않았다.",
    "트랙 반영 제안 — traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)만 반영하고 MiR·OTTO 벤더 주장, Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 본문에서 빼고 additional_research_requests 에 다음 실행 후보로 적었다.",
    "f1 인용 위치 — 6절에서 'VDA 5050 3.0.0 표 2(4.3절)'로 적고 ref-031 직접 인용은 그 한 곳에서만 했다.",
    "분량 초과 자동 분리: 21. 온보딩·설정·현장 시운전 본문 7,666자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,676자"
  ]
}
```

### runs/2026-09-25-52/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-25-area21-s6.md (1,742자)
    - docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-25-area21-s7.md (936자)
    - docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-25-area21-s4.md (914자)
    - docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-25-area21-s8.md (871자)
```

### runs/2026-09-25-52/pages/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전"
type: area
category: "F. 도입·검증·유지관리"
area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [VDA 5050 팩트시트, 레이아웃 교환 형식, 플릿 어댑터, 지도 정합, 가상 시운전]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-251, ref-230, ref-228, ref-079, ref-153, ref-229, ref-046, ref-217, ref-269, ref-037, ref-637, ref-470, ref-639, ref-640, ref-265, ref-163, ref-643]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 21. 온보딩·설정·현장 시운전

# 21. 온보딩·설정·현장 시운전

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [분류원문]

## 2. SCM 관점의 질문

새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

다중 무인운반차(Automated Guided Vehicle, AGV) 도입이 오래 걸리는 원인으로 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문가의 수작업 경로망 설계가 꼽힌다(Beinschob 외, 2017). [사실][^ref-217] 지도 작성은 새 환경에 로봇을 배치할 때 시간이 많이 드는 과정으로 지목된다(Heselden·Das, 2024). [사실][^ref-269]

이 작업이 새 제조사·새 물류센터마다 반복되면, 늘린 로봇 대수가 실제 처리능력으로 바뀌는 시점이 늦어진다. [의견] 유럽연합 PAN-Robots 과제는 설치 기간을 6개월에서 2개월로 줄일 수 있다고 소개했으나, 이는 과제 측 보고값이며 비교 조건은 확인되지 않았다. [추정][^ref-265]

반복 작업은 로봇 신원·기능·제약 등록, 지도·레이아웃·경로망 작성과 가져오기, 제조사 지도와 공통 지도의 정합, 연동 수준 선택으로 나눌 수 있다. 등록 정보는 표준 메시지로 받을 수 있지만 경로망 설계와 지도 정합은 여전히 사람의 설정 작업으로 남는 것으로 보인다. [추정][^ref-031][^ref-230][^ref-153][^ref-079][^ref-217]

## 4. 핵심 개념과 용어

온보딩(onboarding)은 새 로봇·새 현장을 관제에 등록하고 설정해 운용에 넣는 과정이며, 아래 용어가 그 단계를 이룬다.

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area21-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 적치

**시나리오:** 새 제조사 AMR 을 적치 운반에 추가하고 현장 시운전하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 물동량이 늘어 적치 운반 능력을 키우기로 하고, 기존 관제에 다른 제조사의 자율이동로봇(Autonomous Mobile Robot, AMR)을 더하기로 결정한다. [의견] |
| 작업 대상 | 입고 검수를 마친 팔레트·토트를 보관 위치까지 옮기는 적치 운반. [의견] |
| 수행 자원 | 새 AMR 은 신원 보고로 제조사·모델·일련번호·외곽 치수를 알린다. [사실][^ref-230] 통합 담당자는 플릿 어댑터 설정에 속도 한계·작업 유형·좌표 대응점·제조사 관제 연결 정보를 채운다. [사실][^ref-153] 경로망 설계와 지도 정합은 사람의 설정 작업으로 남는 것으로 보인다. [추정][^ref-217] |
| 제약 | 이번에 확인한 팩트시트의 필수·선택 최상위 절과 신원 보고 필드에는 지도 정합을 담는 항목이 보이지 않아, 정합은 현장별 설정·검증 항목으로 남는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-153] 연계 대상: 운행 구역 준비는 ISO 3691-4:2023 부속서 A 가 요구한다. [사실][^ref-470] |
| 완료·인계 | 관제가 지도 내려받기를 지시하고 로봇이 특정 지도 버전을 활성화한다. [사실][^ref-031] 이어 시운전 적치에서 도착 위치와 재고 위치 변경이 일치해야 운용 투입을 인정한다. [의견] 합격 기준은 미확인이다(11절). |
| 예외·성과 | 설치 기간 6개월→2개월(PAN-Robots)은 과제 측 보고값이며 비교 조건 미확인이다. [추정][^ref-265] 가상 시운전으로 시운전 기간을 3주 줄였다는 사례도 벤더 주장이다. [추정] 벤더 주장[^ref-640] |

다음은 설명을 위한 가상의 시나리오이다. 이 영역이 관여하는 칸은 주로 수행 자원·제약·완료·인계다. 로봇이 스스로 알리는 등록 정보와, 현장마다 사람이 정해야 하는 경로망·지도 정합이 갈리는 지점이 시운전 기간을 좌우한다. [의견]

시운전 중 정합 오차로 로봇이 엉뚱한 보관 위치에 도착하면 적치 완료와 재고 위치가 어긋난다. 그래서 어떤 시험으로 정합을 합격 판정할지가 열린 질문으로 남는다. [의견] 흐름 전체는 [흐름 매트릭스](../../flow-matrix.md)에서 본다.

## 6. 대표 접근법과 기술

반복 작업을 줄이는 접근은 등록 정보의 표준화, 설정의 구조화, 지도 작성의 반자동화, 능력 기술의 기계 판독화로 나뉜다. [추정][^ref-031][^ref-153][^ref-217][^ref-229]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area21-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

온보딩에 쓰이는 정보는 관제 인터페이스 표준, 레이아웃 교환 형식, 오픈소스 설정 도구, 능력 기술 서브모델로 흩어져 있다. [사실][^ref-031][^ref-046][^ref-153][^ref-229]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area21-s7.md)에 있다.

## 8. 대표 연구와 자료

연구는 지도 작성 부담을 줄이는 쪽과 능력 정보를 기계가 읽게 하는 쪽으로 나뉜다. [추정][^ref-217][^ref-037]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 대표 연구와 자료](../../topics/2026/2026-09-25-area21-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

로봇 자체의 SLAM 지도 작성·위치 추정·센서 교정은 제조사 몫이고, 이종 로봇을 잇는 ROP 는 등록 정보의 수집·검증, 레이아웃·지도 정합 설정, 연동 수준 결정과 그 설정의 버전 관리를 맡는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-153][^ref-251]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트·신원 보고 수집과 검증, 어댑터 설정, 지도 배포 지시와 버전 관리, 연동 수준 결정 | SLAM 지도 작성, 위치 추정, 센서 교정, 로컬 주행 |
| 시설·설비 제어 | 평면도 위 문·승강기·충전기 위치 주석과 운행 구역 설정 | 승강기 제어, 운행 구역 안전 준비(ISO 3691-4:2023 부속서 A) |

VDA 5050 은 지도 배포 동작과 팩트시트를 정하지만 경로 설정은 범위 밖으로 둔다. [사실][^ref-031] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

온보딩은 등록할 정보(능력·지도)를 정의하는 영역과, 그 정보를 쓰고 검증하는 영역 사이에 놓인다.

- [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 요구·제공 능력 비교와 매뉴얼 기반 능력 온톨로지 생성이 로봇 등록을 줄이려 한다. [사실][^ref-229][^ref-637]
- [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md) — 평면도 주석, 층 정렬, 지도 정합이 공통 공간 모델을 만든다. [사실][^ref-079]
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 팩트시트·신원 보고·어댑터 설정·연동 수준이 연동의 첫 단계다. [사실][^ref-031][^ref-153]
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 다층 지도 작성과 평면도 위 승강기·문 주석이 설비 연동과 맞물린다. [사실][^ref-079]
- [22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) — 가상 시운전과 팩트시트의 시뮬레이션 용도로만 이어진다. [추정][^ref-640][^ref-228]
- [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) — 시운전 합격 판정과 국내 시험·실증 체계가 이어진다. [사실][^ref-639]
- [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 지도 id·버전 배포와 활성화가 버전 관리 대상이다. [사실][^ref-031]
- [25. 안전·위험 관리](../g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — 운행 구역 준비 요구가 시운전 제약이 된다. [사실][^ref-470]
- [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — LLM 능력 온톨로지 생성은 매뉴얼 해석을 이 영역과 5. 로봇 능력·작업 온톨로지에 적용하는 연구 방법이다. [사실][^ref-637]

관련 트랙: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md).

## 11. 열린 질문

국내 적용 사례와 시운전 합격 기준이 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-022** (열림) 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? 이번 실행의 한국어 검색에서는 사례를 찾지 못했다.
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가?
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가?
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? [^ref-031][^ref-046]

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-251]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration), 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Programming Multiple Robots with ROS 2 — traffic-editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: IDTA (admin-shell-io/submodel-templates), IDTA 02020 Submodel Capability Description 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-25
[^ref-217]: Beinschob, P. 외, Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-269]: Heselden, J. R., & Das, G. P., Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments, 2024-04, https://arxiv.org/abs/2404.13499, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-640]: Siemens Digital Industries Software, Virtual commissioning with Siemens solutions reduces launch time by three weeks, 미확인, https://resources.sw.siemens.com/en-US/case-study-idc/, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission CORDIS, PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전"
type: area
category: "F. 도입·검증·유지관리"
area_no: 21
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 21. 온보딩·설정·현장 시운전

# 21. 온보딩·설정·현장 시운전

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [분류원문]

## 2. SCM 관점의 질문

새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

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

### runs/2026-09-25-52/pages/topics/2026/2026-09-25-area21-s6.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전 — 대표 접근법과 기술"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-251, ref-230, ref-228, ref-079, ref-153, ref-229, ref-217, ref-269, ref-037, ref-637, ref-640, ref-265, ref-643]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#6
---

[홈](../../index.md) › [주제](../index.md) › 21. 온보딩·설정·현장 시운전 — 대표 접근법과 기술

# 21. 온보딩·설정·현장 시운전 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 반복 작업을 줄이는 접근은 등록 정보의 표준화, 설정의 구조화, 지도 작성의 반자동화, 능력 기술의 기계 판독화로 나뉜다. [추정][^ref-031][^ref-153][^ref-217][^ref-229]
- 이 페이지는 [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

반복 작업을 줄이는 접근은 등록 정보의 표준화, 설정의 구조화, 지도 작성의 반자동화, 능력 기술의 기계 판독화로 나뉜다. [추정][^ref-031][^ref-153][^ref-217][^ref-229]

### 표준 메시지로 로봇 등록 정보 받기

VDA 5050 3.0.0 표 2(4.3절)는 팩트시트 토픽을 "assist set-up of the mobile robot in fleet control" 하는 정보 전달 수단으로 둔다. [사실][^ref-031] 팩트시트 스키마는 유형 사양·물리 파라미터·프로토콜 한계·프로토콜 기능·로봇 기하·적재 사양의 여섯 절(과 헤더 필드)을 필수로 두고, 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)은 선택 절로 둔다. [추정][^ref-228] 스키마 설명은 이 정보가 관제 통합에 필요하고 계획·규모 산정·시뮬레이션에도 쓸 수 있다고 적는다. [추정][^ref-228] MassRobotics 신원 보고는 필수 6개 외에 최고 속도·충전기 형식·제품 문서 URI·화물 한계 등을 선택 필드로 둔다. [사실][^ref-230]

### 어댑터 설정과 연동 수준 선택

Open-RMF 플릿 어댑터 설정 파일은 속도·가속 한계, 외곽 반경, 배터리·기계 파라미터, 후진 가능 여부, 수행 가능한 작업 유형(순회·배송·청소), 좌표 대응점, 제조사 관제 API 연결 정보를 채우게 하며, 정해진 필드 밖을 쓰면 가져오기 오류가 난다. [사실][^ref-153] 전체 제어(Full Control) 연동은 경로를 지정하고 언제든 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light) 연동은 일시정지·재개만 허용한다. [사실][^ref-251] 읽기 전용(Read Only) 플릿은 제어권 없이 상태만 보고한다. [사실][^ref-004] 따라서 새 플릿을 온보딩할 때 어느 수준으로 연동할지가 선택 사항이 된다. [추정][^ref-251][^ref-004]

### 평면도 주석과 레이아웃 가져오기

Open-RMF traffic-editor 는 건축 도면·평면도를 배경으로 불러와 두 점 사이 측정으로 축척을 맞추고, 정점·벽·문·승강기·주행 차선·충전기를 사람이 주석하게 한다. [사실][^ref-079] 실험적 도구 RMF Site Editor 는 대규모 배치 현장을 편집하고 프로젝트에서 시뮬레이션과 주행 그래프를 생성할 수 있다고 설명한다. [사실][^ref-643] 경로망은 LIF 로 관제에 가져올 수 있고 [사실][^ref-031], 지도는 VDA 5050 즉시 동작 downloadMap·enableMap·deleteMap 으로 배포·활성화한다. [사실][^ref-031] 한계는 운영 요소 주석이 여전히 사람 몫이라는 점이다. [추정][^ref-079]

### 반자동 지도 작성

Beinschob 외(2017)는 레이저 스캐너 시스템으로 3D 의미 지도를 얻어 지도 작성·위치 지정·경로망 설계를 반자동화하는 통합 시스템을 제안한다. [사실][^ref-217] Heselden·Das(2024)는 전역 위치·물체 위치·위상·점유 정보 중심의 표준화된 지도 처리와, 빠진 데이터를 틀·절차적으로 생성하는 관리 스크립트를 제안한다. [사실][^ref-269] PAN-Robots 과제 측은 기존 표지를 활용한 위치 추정과 반자동 공장 탐사를 설치 기간 단축의 이유로 서술한다. [추정][^ref-265]

### 능력 기술과 문서 해석 AI

IDTA 02020 능력 기술 서브모델 1.0 은 요구 능력과 제공 능력을 비교해 공정 계획·오케스트레이션을 지원하도록 만든 자산관리셸 서브모델이다. [사실][^ref-229] 능력·스킬 기술에는 온톨로지 방식과 자산관리셸 서브모델 방식이 있는데 서로 호환되지 않아 둘 사이 대응이 제안됐다. [사실][^ref-037] 대규모 언어 모델(Large Language Model, LLM)로 자연어 능력 설명에서 능력 온톨로지를 생성하고 구문·모순·환각·누락 검사로 검증하는 방법도 있다. [사실][^ref-637] 이는 27. AI·학습·적응과 모델 운영의 매뉴얼 해석을 이 영역에 적용하는 연구 방법이다.

### 가상 시운전

Siemens 고객사례는 IDC 가 Tecnomatix Plant Simulation 으로 고속 분류기를 가상 시운전해, 현장 시운전만 한 유사 업그레이드 프로젝트(8주)보다 시운전 기간을 3주 줄였다고 설명한다. [추정] 벤더 주장[^ref-640]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-251]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration), 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Programming Multiple Robots with ROS 2 — traffic-editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: IDTA (admin-shell-io/submodel-templates), IDTA 02020 Submodel Capability Description 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-217]: Beinschob, P. 외, Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-269]: Heselden, J. R., & Das, G. P., Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments, 2024-04, https://arxiv.org/abs/2404.13499, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-640]: Siemens Digital Industries Software, Virtual commissioning with Siemens solutions reduces launch time by three weeks, 미확인, https://resources.sw.siemens.com/en-US/case-study-idc/, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission CORDIS, PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: Open Robotics (open-rmf/rmf_site), rmf_site — README (RMF Site Editor), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-52 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-52 | 21. 온보딩·설정·현장 시운전 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-52/pages/topics/2026/2026-09-25-area21-s7.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-230, ref-228, ref-079, ref-153, ref-229, ref-046, ref-470, ref-639, ref-643]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#7
---

[홈](../../index.md) › [주제](../index.md) › 21. 온보딩·설정·현장 시운전 — 관련 표준·프레임워크·오픈소스

# 21. 온보딩·설정·현장 시운전 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 온보딩에 쓰이는 정보는 관제 인터페이스 표준, 레이아웃 교환 형식, 오픈소스 설정 도구, 능력 기술 서브모델로 흩어져 있다. [사실][^ref-031][^ref-046][^ref-153][^ref-229]
- 이 페이지는 [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

온보딩에 쓰이는 정보는 관제 인터페이스 표준, 레이아웃 교환 형식, 오픈소스 설정 도구, 능력 기술 서브모델로 흩어져 있다. [사실][^ref-031][^ref-046][^ref-153][^ref-229]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 3.0.0 | 표준 | 팩트시트·factsheetRequest, 지도 배포 동작, 도입 단계 서술 [사실] | [^ref-031] |
| VDA 5050 팩트시트 스키마 | 표준 | 필수 여섯 절과 선택 로봇 구성 절 [추정] | [^ref-228] |
| LIF 1.0.0 | 표준 | 주행 레이아웃을 제3자 관제에 넘기는 형식 [사실] | [^ref-046] |
| MassRobotics AMR 상호운용 표준 | 표준 | 신원 보고 필드 [사실] | [^ref-230] |
| Open-RMF 플릿 어댑터 | 오픈소스 | 새 플릿 사양·작업 능력·좌표 대응점 설정 [사실] | [^ref-153] |
| Open-RMF traffic-editor | 오픈소스 | 평면도 주석, 축척, 층 정렬 [사실] | [^ref-079] |
| RMF Site Editor(rmf_site) | 오픈소스 | 배치 현장 편집, 주행 그래프·시뮬레이션 생성(실험적) [사실] | [^ref-643] |
| IDTA 02020 Capability Description 1.0 | 표준 | 요구·제공 능력 비교 [사실] | [^ref-229] |
| ISO 3691-4:2023 | 표준(연계 대상) | 무인 산업용 트럭의 안전 요구·검증, 운행 구역 준비(부속서 A) [사실] | [^ref-470] |

LIF 의 기준일은 두 출처가 다르다. VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용한다. [사실][^ref-031] LIF 공식 저장소는 1.0.0 을 2023-09 로 표기한다. [사실][^ref-046] 어느 쪽이 현행인지는 11절 열린 질문으로 남긴다.

국내에서는 한국산업기술시험원(KTL)과 한국통합물류협회(KILA)가 2026-07-23 물류로봇 시험·인증·표준화 협약을 맺고, KTL 테스트베드와 회원사 물류센터를 잇는 실증 체계를 밝혔다. 협약 단계이며 실적은 미확인이다. [사실][^ref-639] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Programming Multiple Robots with ROS 2 — traffic-editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: IDTA (admin-shell-io/submodel-templates), IDTA 02020 Submodel Capability Description 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-25
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: Open Robotics (open-rmf/rmf_site), rmf_site — README (RMF Site Editor), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-52 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-52 | 21. 온보딩·설정·현장 시운전 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-52/pages/topics/2026/2026-09-25-area21-s4.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전 — 핵심 개념과 용어"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-230, ref-228, ref-079, ref-153, ref-046, ref-037, ref-640]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#4
---

[홈](../../index.md) › [주제](../index.md) › 21. 온보딩·설정·현장 시운전 — 핵심 개념과 용어

# 21. 온보딩·설정·현장 시운전 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 온보딩(onboarding)은 새 로봇·새 현장을 관제에 등록하고 설정해 운용에 넣는 과정이며, 아래 용어가 그 단계를 이룬다.
- 이 페이지는 [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

온보딩(onboarding)은 새 로봇·새 현장을 관제에 등록하고 설정해 운용에 넣는 과정이며, 아래 용어가 그 단계를 이룬다.

- **[VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)(factsheet)** — 관제가 이동로봇을 설정하는 데 필요한 파라미터·제조사 정보를 로봇이 보내는 토픽이다. 관제는 즉시 동작 factsheetRequest 로 전송을 요청할 수 있다. [사실][^ref-031][^ref-228]
- **신원 보고(Identity Report)** — MassRobotics 상호운용 표준에서 제조사·모델·일련번호·외곽 치수를 필수로 알리는 메시지다. [사실][^ref-230]
- **[레이아웃 교환 형식](../../glossary/layout-interchange-format.md)(Layout Interchange Format, LIF)** — 통합사업자가 간선·노드·스테이션으로 된 주행 레이아웃을 제3자 관제에 처음 넘기는 비구속적 교환 형식이다. [사실][^ref-046]
- **[경로망](../../glossary/roadmap.md)(Roadmap)** — VDA 5050 3.0.0 은 경로 정의를 도입 단계 활동으로 설명하되 경로 설정 자체는 명세 범위 밖으로 둔다. [사실][^ref-031]
- **[플릿 어댑터](../../glossary/fleet-adapter.md)(Fleet Adapter)** — Open-RMF 에서 새 플릿의 사양·작업 능력·제조사 관제 연결을 설정 파일로 받는 연동 계층이다. [사실][^ref-153]
- **[지도 정합](../../glossary/map-alignment.md)(Map Alignment)** — 로봇 좌표계와 공통 좌표계를 맞추는 일로, Open-RMF 는 대응점 쌍(reference_coordinates)으로 변환을 구한다. [사실][^ref-153] 층 사이 정렬은 수직으로 맞춘 기준점(fiducial) 쌍으로 계산한다. [사실][^ref-079]
- **가상 시운전(Virtual Commissioning)** — 현장 설치 전에 제어 로직·관제 설정을 가상 모델에 연결해 시험하는 방법이며, 효과 수치는 벤더 사례뿐이다. [추정] 벤더 주장[^ref-640]
- **플러그 앤 프로듀스(Plug and Produce)** — 새 자원과 기능의 통합 공수를 줄이려는 원칙으로, 능력·스킬 기술이 그 바탕이다. [사실][^ref-037]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Programming Multiple Robots with ROS 2 — traffic-editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-25
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-640]: Siemens Digital Industries Software, Virtual commissioning with Siemens solutions reduces launch time by three weeks, 미확인, https://resources.sw.siemens.com/en-US/case-study-idc/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-52 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-52 | 21. 온보딩·설정·현장 시운전 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-52/pages/topics/2026/2026-09-25-area21-s8.md

```markdown
---
title: "21. 온보딩·설정·현장 시운전 — 대표 연구와 자료"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-217, ref-269, ref-037, ref-637, ref-265, ref-163]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#8
---

[홈](../../index.md) › [주제](../index.md) › 21. 온보딩·설정·현장 시운전 — 대표 연구와 자료

# 21. 온보딩·설정·현장 시운전 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 연구는 지도 작성 부담을 줄이는 쪽과 능력 정보를 기계가 읽게 하는 쪽으로 나뉜다. [추정][^ref-217][^ref-037]
- 이 페이지는 [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

연구는 지도 작성 부담을 줄이는 쪽과 능력 정보를 기계가 읽게 하는 쪽으로 나뉜다. [추정][^ref-217][^ref-037]

- Beinschob 외, Semi-automated map creation for fast deployment of AGV fleets in modern logistics(2017, Robotics and Autonomous Systems 87권) — 다중 AGV 도입 병목을 3D 의미 지도로 반자동화한다. 이 영역의 설치 공수 문제를 정리한 대표 문헌이다. [사실][^ref-217]
- Heselden·Das, Unified Map Handling for Robotic Systems(2024, arXiv) — 표준화된 지도 처리와 빠진 데이터 생성으로 새 환경 배치를 돕는다. [사실][^ref-269]
- 노주형 외, 한국로봇학회 논문지 21권 1호(2026) — 3D 라이다–관성 센서 SLAM 탐사와 로봇팔 승강기 버튼 조작을 결합해 다층 실내 지도를 자율로 구축한다. 로봇 자체 기능 연구이므로 연계 대상 사례로 둔다. [사실][^ref-163]
- Vieira da Silva 외, Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies(2023, ETFA) — 플러그 앤 프로듀스를 위한 두 능력 모델 방식의 대응을 제안한다. [사실][^ref-037]
- Vieira da Silva 외, Toward a Method to Generate Capability Ontologies from Natural Language Descriptions(2024, arXiv) — LLM 기반 능력 온톨로지 생성과 자동 검증 루프를 제안한다. [사실][^ref-637]
- 보조 자료: EU CORDIS 의 PAN-Robots 소개(설치 기간 단축은 과제 측 보고값). [추정][^ref-265]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-217]: Beinschob, P. 외, Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-269]: Heselden, J. R., & Das, G. P., Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments, 2024-04, https://arxiv.org/abs/2404.13499, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission CORDIS, PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
[^ref-163]: 노주형, 강규리, 김연찬, 심현철 (한국로봇학회), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-52 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-52 | 21. 온보딩·설정·현장 시운전 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-52/docs_tree.txt

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
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
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
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fleet-adapter.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/grai.md
glossary/hallucination.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoorgml.md
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
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
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
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 481건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 122개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
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
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoorgml: IndoorGML (IndoorGML)
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
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [21] 에 걸린 1건 / 전체 75건)

```markdown
- oq-022 [열림] 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? (영역 6, 21)
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
