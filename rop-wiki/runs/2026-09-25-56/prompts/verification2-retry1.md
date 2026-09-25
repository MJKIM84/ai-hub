(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-56
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 22. 시뮬레이션·예측용 디지털 트윈 (F. 도입·검증·유지관리)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-25-56/target.json

```json
{
  "run_id": "2026-09-25-56",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 56,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 22,
    "area_name": "22. 시뮬레이션·예측용 디지털 트윈",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=22"
}
```

### runs/2026-09-25-56/research.json

```json
{
  "run_id": "2026-09-25-56",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 22,
    "area_name": "22. 시뮬레이션·예측용 디지털 트윈",
    "category": "F. 도입·검증·유지관리"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(디지털 모델·섀도·트윈 구분, 8. 실시간 세계 상태·데이터 일관성과의 경계)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음(트랙 floorplan-recognition 반영 제안 1건: Sommer 외 2023, ref-241)",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건)"
  ],
  "research_questions": [
    "성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]",
    "디지털 트윈·시뮬레이션의 정의와 표준(ISO 23247, KS X ISO 23247)은 무엇이며, 디지털 모델·디지털 섀도·디지털 트윈 구분으로 8. 실시간 세계 상태·데이터 일관성과 어떻게 경계를 긋는가? (섹션 3·4·7 겨냥)",
    "물류센터 로봇 운영 정책·배치·수요 변화의 효과를 예측하는 대표 접근법(이산 사건 시뮬레이션, 물리 기반 로봇 시뮬레이터, 데이터 기반 모델 생성)은 무엇인가? (섹션 6 겨냥)",
    "오픈소스 도구(Open-RMF 시뮬레이션, RAWSim-O, OFacT)는 무엇을 재현하고 어떤 결정을 실험하게 하는가? (섹션 7 겨냥)",
    "시뮬레이션 모델의 검증·타당성 확인 방법과 실데이터 검증 부족 문제는 연구에서 어떻게 다뤄지는가? (섹션 8·11 겨냥)",
    "ROP 가 직접 맡을 시뮬레이션 범위와 외부에 맡길 범위(센서·물리 시뮬레이션, 로봇 로컬 주행, 수요예측)는 어떻게 나뉘는가? (섹션 9·10 겨냥)",
    "국내 물류센터 디지털 트윈 사례와 트랙 floorplan-recognition 반영 제안(스캔·객체 인식 기반 계획용 트윈, Sommer 외 2023)은 무엇을 보여 주는가? (섹션 5·8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ISO 23247(제조를 위한 디지털 트윈 프레임워크)은 국내에 KS X ISO 23247 로 부합화되어 있으며 제1부 개요 및 일반 원리, 제2부 참조 구조, 제4부 정보 교환 등 부로 나뉜다.",
      "tag": "사실",
      "source_ids": [
        "ref-659"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 표준 상세 목록: KS X ISO 23247-1 '개요 및 일반 원리', -2 '참조 구조', -4 '정보 교환' (제3부 목록은 이번 검색에서 확인하지 못함) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "ISO 는 2026년에 ISO 23247-5(디지털 트윈을 위한 디지털 스레드)와 ISO 23247-6(디지털 트윈 결합)을 발간했고, 국가기술표준원은 2026-07-28 이 두 표준이 한국(ETRI) 제안으로 발간되었다고 알렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-661",
        "ref-662"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "ISO 카탈로그에 ISO 23247-6:2026 'Digital twin composition' 등재. 기사: 국표원이 디지털 쓰레드(23247-5)·디지털 트윈 결합(23247-6) 국제표준 2건 발간을 밝힘(2026-07-28)",
      "as_of": "2026-07-28",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "ISO 23247-6 은 목적에 따라 여러 디지털 트윈을 골라 결합하는 방법을 정해, 제품·설비·공정의 개별 트윈을 묶어 생산 라인·공장 전체의 복합 트윈을 구성하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-661",
        "ref-662"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "개별 트윈을 블록처럼 결합해 라인·공장 전체를 덮는 복합 디지털 트윈을 구현한다는 설명(기사 요약 중심, ISO 본문 미열람)",
      "as_of": "2026-07-28",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "NIST 의 제조용 디지털 트윈 과제는 디지털 트윈을 신뢰할 수 있고 상호운용 가능하게 만드는 측정 과학과 표준 개발을 목표로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-660"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "과제 목표: 디지털 트윈을 reliable, interoperable, trustworthy 하게 만드는 측정 과학·표준 개발 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "Kritzinger 외(2018)는 제조 분야 문헌을 디지털 모델·디지털 섀도·디지털 트윈으로 구분해 분류했고, 가장 높은 단계인 디지털 트윈을 다룬 문헌은 드물고 모델·섀도 문헌이 더 많다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-291"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Digital Model(DM), Digital Shadow(DS), Digital Twin 구분; DT 문헌은 scarce, DM·DS 문헌이 더 많음. 향후 과제로 충실도 수준·데이터 소유권 등 7개 제시",
      "as_of": "2018",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "분류 원문의 구분(8. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 22. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험)에 문헌의 모델·섀도·트윈 구분을 맞추면, '디지털 트윈'이라는 이름이 실시간 동기화 수준을 가리키는 경우와 시나리오 실험 기능을 가리키는 경우가 섞여 쓰이므로 이 위키는 용도(현재 표현/미래 실험)로 나눠 적는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-291",
        "ref-664"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Kritzinger 외는 데이터 연결 수준으로 DM·DS·DT 를 구분하고, Agalianos 외는 DES 가 실시간 데이터를 질의하며 DT 의 일부로 진화한다고 서술 — 두 축(동기화 수준, 실험 용도)이 다름",
      "as_of": "2020",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "Agalianos 외(2020)는 물류 4.0 에서 이산 사건 시뮬레이션(DES)이 사물인터넷 장치의 실시간 데이터를 질의하며 디지털 트윈의 한 부분으로 진화하고, 이를 통해 창고 계획·관리·의사결정을 지원한다고 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-664"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Procedia Manufacturing 51, 1636–1641. DES 와 DT 통합 문헌을 검토하고 물류의 추세·과제를 식별",
      "as_of": "2020",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "Le·Fan(2024)의 물류·공급망 디지털 트윈 문헌 검토는 실제 데이터로 검증한 논문은 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 실무 적용의 부족을 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-665"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "only a few papers employ actual data sets for validation whereas the majority utilize generative data sets (Computers & Industrial Engineering 187)",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Le·Fan(2024)은 COVID-19 이후 공급망 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고, 물류·공급망 디지털 트윈 개념 틀을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-665"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "팬데믹 이후 risk and disruption management 에서 DT 의 이점이 부각; LSCS 용 개념 프레임워크 제안",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "Coelho 외(2021)는 Simio 로 만든 사내 물류 시뮬레이션 의사결정 지원 도구를 제안하고, 이 모델이 현실을 대표하여 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-666"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "유통 시설과 생산 시설의 사내 물류 활동 분석; 지능형 객체 기반 Simio 모델이 operations improvement without disrupting real sets 에 쓰일 수 있음",
      "as_of": "2021",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Open-RMF 문서는 Gazebo·Ignition 물리 시뮬레이터를 ROS 2 와 연결해 시뮬레이션에 쓴 코드를 수정 없이 실제 시스템에서도 실행하고, 시나리오 반복·예외 상황 탐색·장시간 검증을 현장 배치 전에 할 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"the exact same code used to run the simulations will also be run on the physical system as well without any changes\" — 배터리 소모·충돌 비용 없이 반복 시험",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Open-RMF 의 building_map_generator 는 traffic_editor 로 주석한 .building.yaml 에서 Gazebo·Ignition 월드(바닥·벽 메시)와 플릿 어댑터용 주행 그래프를 함께 생성하므로, 레이아웃이 바뀌면 주석을 고쳐 시뮬레이션 월드를 다시 만들 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 모드: .world·model.sdf 생성, 경로 계획용 YAML 주행 그래프 내보내기; 설비 레이아웃 변경 시 주석 수정 후 재생성",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Open-RMF 시뮬레이션은 로봇용 slotcar 플러그인(레일식 주행과 가감속), 문·승강기 플러그인, 작업셀 적재·하역을 흉내 내는 TeleportDispenser·TeleportIngestor, Menge 기반 보행자 군중 시뮬레이션(CrowdSim), 배터리·충전기 동작 전환 도구를 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406",
        "ref-668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "slotcar 는 /robot_path_requests 를 구독해 rail-like navigation 구현; rmf_simulation README 에 Toggle charging(배터리·충전기), Crowd simulation(Menge) 항목 (두 출처 모두 Open Robotics 계열)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "연계 대상: Open-RMF 시뮬레이션의 로봇 모델은 레일식 주행을 흉내 내는 단순화 모델이므로, 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도는 제조사·물리 시뮬레이터 쪽에 맡기고 ROP 시뮬레이션은 플릿 조율·설비 상호작용을 실험하는 데 초점이 맞는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-406",
        "ref-668"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "slotcar 는 'simple robot navigation stack'으로 경로 요청을 받아 레일식으로 이동하고 업데이트를 보냄 — 로컬 주행 알고리즘을 재현하지 않음",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "rmf_simulation 저장소는 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 지원 대상으로 적어, 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리가 필요하다.",
      "tag": "사실",
      "source_ids": [
        "ref-668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: Gazebo Classic 11 (support ending January 2025), Gazebo Fortress; ros_gz 지원 판에 맞춤(예: ROS Humble–Fortress)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS)의 이산 사건 시뮬레이션 프레임워크로, 운영 중 생기는 여러 결정 문제의 효과를 연구하고 새 결정 방법을 끼워 넣을 수 있게 하며 2D·3D 화면과 로봇 위치 히트맵을 제공한다(C#, GPL v3).",
      "tag": "사실",
      "source_ids": [
        "ref-101"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"a discrete event-based simulation for Robotic Mobile Fulfillment Systems\"; 결정 문제별 새 방법 구현 확장성, 히트맵·경로 계획 시각화, GNU GPL v3",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "Merschformann 외(2019)의 RMFS 결정 규칙 연구는 이산 사건 시뮬레이션으로 배정 규칙을 가정한 미래에서 실험했고, 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다.",
      "tag": "사실",
      "source_ids": [
        "ref-398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RMFS 결정 규칙 조합을 시뮬레이션으로 비교, 피킹 주문 배정 규칙의 처리량 영향이 큼 (재인용: 2026-09-25-55)",
      "as_of": "2019",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "국내 연구로 시뮬레이션과 메타모델을 결합해 자동물류센터 설계를 최적화한 연구가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-402"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KISTI ScienceON 수록 '시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화' (재인용: 2026-09-25-55)",
      "as_of": "2006",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "다중 AGV 시스템의 경로망을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있어, 경로망 배치안 평가가 시뮬레이션으로 이루어진다.",
      "tag": "사실",
      "source_ids": [
        "ref-267"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (재인용: 2026-09-25-55)",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "OFacT(Open Factory Twin)는 Fraunhofer ISST 등이 개발한 생산·물류용 오픈소스 디지털 트윈 프레임워크로, 주문·자원·부품·공정으로 공장 상태를 기술하는 상태 모델, 주문·자원 에이전트 제어, 일관성 검사를 포함한 데이터 통합, 시나리오 평가·예측용 시뮬레이션, KPI 비교 계획 서비스를 갖춘다(Apache 2.0).",
      "tag": "사실",
      "source_ids": [
        "ref-670"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Open source Digital Twin Framework for Production and Logistics\"; Simulation 은 evaluate different scenarios or produce forecasts; 창고·공급망도 대상",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "OFacT 가 현재 상태를 담는 상태 모델·데이터 통합과 시나리오를 돌리는 시뮬레이션·계획 서비스를 별도 구성요소로 두는 것은, 8. 실시간 세계 상태·데이터 일관성(현재 표현)과 22. 시뮬레이션·예측용 디지털 트윈(미래 실험)을 나누는 분류 원문의 구분과 같은 방향의 설계로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-670"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "README 구성요소: State Model / Data Integration(실데이터·일관성 검사) 와 Simulation / Planning Services(시나리오·KPI) 분리",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "Sargent 의 시뮬레이션 모델 검증·타당성 확인(V&V) 틀은 개념 모델 타당성, 모델 검증, 운영 타당성, 데이터 타당성을 나누어 확인하고 결과 문서화와 모델 인가(accreditation)를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-671"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "conceptual model validity, model verification, operational validity, data validity 및 권장 검증 절차·인가 논의(WSC 논문, 검색 요약 기준)",
      "as_of": "2008",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "CJ대한통운은 2021년 11월 현실 물류센터와 같은 가상 물류센터를 구축해 작업 동선·재고 배치·설비 효율을 최적화하고 장비 고장·피킹 오류·상품 파손 원인을 사전에 파악하며, AI 가 시나리오를 학습해 몇 시간 걸릴 일을 수초~수분에 해결한다고 발표했다.",
      "tag": "추정",
      "source_ids": [
        "ref-672"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 보도자료 — 운영 현황 모니터링·재현, 작업동선·재고배치·설비효율 최적화, 이듬해 택배 네트워크(허브·서브터미널)로 확대 계획",
      "as_of": "2021-11",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f24",
      "claim": "NVIDIA 는 'Mega' Omniverse 블루프린트를 공장·창고 디지털 트윈에서 로봇 플릿과 물리 AI 를 배치 전에 개발·시험·최적화하는 참조 작업 흐름(센서 시뮬레이션·합성 데이터 생성 결합)으로 소개하고, KION·Accenture 가 창고·유통 공정 최적화에 쓴다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-673"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: reference workflow for combining sensor simulation and synthetic data generation ... verify performance of autonomous systems in industrial digital twins (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f25",
      "claim": "분류 원문 질문 '성수기 주문량이 늘면 어디가 먼저 막힐까?'에 대해, 확인한 DES 연구·도구는 주문 도착량과 배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 답하며, ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-398",
        "ref-101",
        "ref-666",
        "ref-664"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "RAWSim-O·RMFS 결정 규칙 연구는 결정 규칙별 처리량 비교, Coelho 외는 개선안 시험, Agalianos 외는 창고 계획 지원 — 성수기 병목 위치를 직접 보고한 ROP 사례 없음",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "Sommer 외(2023)는 레이저 스캔과 객체 인식으로 공장의 건조 환경(built environment) 디지털 트윈을 자동 생성해 생산 계획의 입력으로 쓰는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-241"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Journal of Industrial Information Integration 33, 100462 (2023). 스캔·객체 검출로 공장 레이아웃 모델링과 객체 인식을 자동화해 계획 입력으로 제공",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "Sommer 외(2023)의 트윈은 생산 계획을 위한 배치·공간 모델이므로 22. 시뮬레이션·예측용 디지털 트윈의 초기 모델 생성(계획용)에 해당하고, 운영 중 현재 상태를 동기화하는 8. 실시간 세계 상태·데이터 일관성과는 구분되는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-241",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "계획 입력용 자동 생성(ref-241)과, 주석한 평면도에서 시뮬레이션 월드를 만드는 Open-RMF 흐름(ref-406)이 모두 실험용 모델의 초기값 생성 단계",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f28",
      "claim": "ROP 가 직접 맡을 시뮬레이션 몫은 자신의 작업 배정·교통·충전 정책과 설비 요청(문·승강기)을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보이며, Open-RMF 처럼 같은 코드를 시뮬레이션과 실제에 쓰는 구조가 그 근거가 된다.",
      "tag": "추정",
      "source_ids": [
        "ref-406",
        "ref-668"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "문·승강기 플러그인이 /door_requests·/lift_requests 에 응답하고 slotcar 가 경로 요청을 받음 — 오케스트레이션 계층의 요청이 시뮬레이션 대상",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f29",
      "claim": "연계 대상: 센서 시뮬레이션·합성 데이터 생성·물리 기반 로봇 거동 재현은 시뮬레이터 제공자와 로봇 제조사 영역이고, 시나리오의 주문·물동량 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-673",
        "ref-665"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Mega 블루프린트는 센서 시뮬레이션·합성 데이터를 제공 기능으로 둠; 물류·공급망 DT 틀은 수요·교란 시나리오를 상위 계획 입력으로 다룸(분류 원문 9장 경계 적용)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색은 23. 시험·형식 검증·벤치마크의 회귀·장애 시험과 환경을 공유하므로, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인이라는 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "RMF 문서: scenario repeatability, edge case exploration, long-running validation before facility deployment",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-659",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 23247 을 부합화한 KS X ISO 23247 시리즈의 제1부 표준 상세 페이지. 검색 결과에서 제2부(참조 구조)·제4부(정보 교환) 항목도 확인.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-660",
      "org": "NIST",
      "title": "Digital Twins for Advanced Manufacturing",
      "published": null,
      "url": "https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조 디지털 트윈을 신뢰·상호운용 가능하게 하는 측정 과학과 표준 개발을 목표로 하는 NIST 과제 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-661",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 여러 디지털 트윈을 목적에 따라 결합하는 방법을 다루는 ISO 23247 제6부 카탈로그 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-662",
      "org": "머니투데이",
      "title": "설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간",
      "published": "2026-07-28",
      "url": "https://www.mt.co.kr/economy/2026/07/28/2026072809211448284",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국가기술표준원이 한국 제안 ISO 23247-5(디지털 쓰레드)·23247-6(디지털 트윈 결합) 발간을 알린 내용을 보도.",
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
      "summary": "원문 미열람. IFAC-PapersOnLine 게재. 디지털 모델·디지털 섀도·디지털 트윈을 구분해 제조 분야 문헌을 분류하고 연구 공백 7가지를 제시.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-664",
      "org": "Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G.",
      "title": "Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/pii/S2351978920320990",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Procedia Manufacturing 51. 물류에서 DES 와 디지털 트윈 통합 문헌을 검토하고 추세·과제를 정리.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-665",
      "org": "Le, T. V., & Fan, R.",
      "title": "Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Computers & Industrial Engineering 187. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀 제안, 실데이터 검증 논문이 소수라고 보고.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-666",
      "org": "Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P.",
      "title": "Simulation-based decision support tool for in-house logistics: the basis for a digital twin",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Computers & Industrial Engineering 153. Simio 기반 사내 물류 시뮬레이션 의사결정 지원 도구를 디지털 트윈의 기초로 제안.",
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
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 장: Gazebo·Ignition 연동, building_map_generator 의 월드·주행 그래프 생성, slotcar·문·승강기·작업셀·군중 플러그인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
      "source_unopened": false
    },
    {
      "id": "ref-668",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_simulation — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_simulation",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 플러그인 저장소: 문·승강기·군중·충전 전환·slotcar·읽기 전용·텔레포트 디스펜서/인제스터, 지원 Gazebo 판.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_simulation/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (merschformann GitHub)",
      "title": "RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "RMFS 이산 사건 시뮬레이션 프레임워크 README: 결정 문제별 방법 확장, 2D·3D 화면·히트맵, C#, GPL v3.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/merschformann/RAWSim-O/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-670",
      "org": "OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund)",
      "title": "ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README)",
      "published": null,
      "url": "https://github.com/OpenFactoryTwin/ofact",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "생산·물류용 오픈소스 디지털 트윈 프레임워크 README: 상태 모델, 에이전트 제어, 데이터 통합, 시뮬레이션, 계획 서비스, 환경 인터페이스. Apache 2.0.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/OpenFactoryTwin/ofact/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-671",
      "org": "Sargent, R. G.",
      "title": "Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation)",
      "published": "2008",
      "url": "https://dl.acm.org/doi/abs/10.5555/1516744.1516780",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션 모델의 개념 모델 타당성·모델 검증·운영 타당성·데이터 타당성과 검증 절차·인가를 다룬 WSC 튜토리얼 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-672",
      "org": "CJ대한통운",
      "title": "가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료)",
      "published": "2021-11",
      "url": "https://www.cjlogistics.com/ko/newsroom/news/NR_00000905",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 디지털 트윈 구축 계획과 기대 효과를 알린 기업 보도자료(국내 사례).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-673",
      "org": "NVIDIA",
      "title": "NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins",
      "published": null,
      "url": "https://blogs.nvidia.com/blog/mega-omniverse-blueprint",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 시설 디지털 트윈에서 로봇 플릿을 배치 전에 시험하는 참조 작업 흐름을 소개한 벤더 블로그.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. Journal of Industrial Information Integration 33. 스캔과 객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성해 생산 계획 입력으로 쓰는 방법.",
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
      "summary": "원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-402",
      "org": "KISTI ScienceON 수록 논문(저자 미확인)",
      "title": "시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화",
      "published": null,
      "url": "https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션과 메타모델로 자동물류센터 설계를 최적화한 국내 연구.",
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
      "summary": "원문 미열람. 다중 AGV 경로망을 시뮬레이션 기반으로 자동 설계하는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f7·f9·f10·f11(배치 전 반복 시험·운영 방해 없는 개선안 시험), f8(실데이터 검증 부족) / 4절 핵심 개념: f5(디지털 모델·섀도·트윈), f6 의견·f21 추정(8. 실시간 세계 상태·데이터 일관성과의 구분: 현재 표현 vs 가정한 미래 실험), f3(디지털 트윈 결합) / 5절 현장 시나리오: f25(피킹·제약, 분류 원문 질문 — 추정), f17(피킹·예외·성과), f23(국내 사례, 벤더 주장 병기) / 6절 대표 접근법: f7(DES 와 실시간 데이터), f10(DES 의사결정 지원), f11·f13(물리 시뮬레이터·플러그인), f12·f26·f27(평면도·스캔에서 초기 모델 생성), f24(벤더 주장) / 7절 표준·오픈소스: f1·f2·f3·f4(ISO 23247·KS X ISO 23247·NIST), f11~f13·f15(Open-RMF 시뮬레이션), f16(RAWSim-O), f20(OFacT) / 8절 대표 연구: f5·f7·f8·f9·f10·f17·f18·f19·f22, 트랙 floorplan-recognition 단계 1 반영 제안(2026-09-25-19) 검토 결과 f26(사실)·f27(추정, 계획용 트윈이므로 8. 실시간 세계 상태·데이터 일관성과 구분) / 9절 경계: f28(ROP 직접: 자기 정책을 시뮬레이션된 플릿·설비에 실행), f14·f29('연계 대상': 로봇 자체 거동·센서 시뮬레이션·수요예측) / 10절 연결: 8. 실시간 세계 상태·데이터 일관성(f6·f21), 23. 시험·형식 검증·벤치마크(f30), 24. 자산·소프트웨어 수명주기 관리(f15), 21. 온보딩·설정·현장 시운전과 6. 지도·공간·위치 모델(f12·f26), 13. 작업 배정 — MRTA·15. 다중 로봇 경로·교통 관리 — MAPF(f17·f19), 27. AI·학습·적응과 모델 운영(f23·f24 벤더 주장, 학습 환경으로서 트윈), 28. 표준·상호운용성·다사업자 거버넌스(f1~f3), 20. 예외 복구·재계획·업무 연속성(f9) / 11절 열린 질문: open_questions_new 3건과 f25 의 미확인 사항. 벤더 주장 f23·f24 는 [추정]+'벤더 주장' 병기."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "디지털 스레드",
      "term_en": "Digital Thread",
      "definition": "제품 수명주기 전반의 설계·생산·운영 데이터를 연결해 디지털 트윈을 만들고 유지하게 하는 데이터 연결 체계로, ISO 23247-5 가 제조 디지털 트윈용 틀을 정한다."
    },
    {
      "term_ko": "디지털 트윈 결합",
      "term_en": "Digital Twin Composition",
      "definition": "제품·설비·공정의 개별 디지털 트윈을 목적에 맞게 골라 묶어 라인·공장 단위의 복합 트윈을 만드는 방법으로, ISO 23247-6 이 다룬다."
    },
    {
      "term_ko": "시뮬레이션 모델 검증·타당성 확인",
      "term_en": "Verification and Validation (V&V) of Simulation Models",
      "definition": "시뮬레이션 모델이 설계대로 구현되었는지(검증)와 목적에 비추어 현실을 충분히 대표하는지(타당성 확인)를 개념 모델·운영·데이터 측면에서 확인하는 절차다."
    }
  ],
  "open_questions_new": [
    "물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 4. 성과·경제성·프로세스 개선 | 근거: f8 | 종류: 일반",
    "제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f3 | 종류: 일반",
    "제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 9. 로봇·제조사 관제 연동 | 근거: f14 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 1,
    "unverified": [
      "f1: KS X ISO 23247 제3부 목록과 각 부의 KS 제정일 미확인",
      "f2·f3: ISO 23247-6 본문 미열람, 결합 방법 설명은 기사 요약 중심",
      "f4: NIST 과제 페이지 원문 미열람, 발행일 미확인",
      "f22: Sargent 논문의 정확한 판(2008 WSC 외 여러 판 존재) 원문 미확인",
      "f23·f24: 벤더 주장, 독립 출처로 효과 수치 확인 못 함",
      "f25: ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례 찾지 못함",
      "ref-241: 참고문헌 목록의 기존 값을 입력으로 받지 못해 검색 결과로 기관·제목·URL 을 채움(퍼블리셔 대조 필요)",
      "ref-673 발행일 미확인"
    ],
    "scope_violations": [
      "f14·f29: 센서 인식·로컬 주행·센서 시뮬레이션과 수요예측은 분류 원문 9장 외부 연계 영역이므로 '연계 대상:'으로 표시",
      "f24: 물리 AI 학습·센서 시뮬레이션은 ROP 직접 범위가 아님(벤더 주장으로만 서술)"
    ],
    "budget_used": {
      "queries": 23,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처는 ref-406(Open-RMF 시뮬레이션 장, 미러 목록 경로), ref-668(rmf_simulation), ref-101(RAWSim-O), ref-670(OFacT) 4건이며 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 23회/30, 신규 출처 15건/15(ref-659~ref-673, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 23247-1 정의 원문, 물류 디지털 트윈 대규모 사례(Ashrafian·Pedersen 2023), 데이터 기반 시뮬레이션 모델 자동 생성 검토 논문은 출처로 넣지 않음. 재사용 4건: ref-398·ref-402·ref-267(2026-09-25-55 브리프 값 사용), ref-241(입력에 참고문헌 목록 값이 없어 검색으로 확인한 값으로 기재). 트랙 반영 제안 1건(2026-09-25-19, floorplan-recognition 단계 1, 8절)은 f26(사실)·f27(추정)으로 조사해 반영을 제안. 교차 확인은 f2 1건뿐. 한국 자료: KS X ISO 23247(ref-659), 국표원 발표 기사(ref-662), 국내 연구(ref-402), CJ대한통운 보도자료(ref-672, 벤더 주장). 한국어 검색에서 나온 업체 블로그는 출처로 쓰지 않음. 27. AI·학습·적응과 모델 운영 연결은 f23·f24 벤더 주장뿐이라 교차 규칙 대상(5·21·6·13·19)에 직접 해당하는 근거는 없음. 정정 요청 없음, 대상 영역 열린 질문 0건, 해결 제안 없음."
  }
}
```

### runs/2026-09-25-56/verification.json

```json
{
  "run_id": "2026-09-25-56",
  "stage": "first",
  "verdict": "조건부 승인",
  "retry_reason": null,
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 KSSN 상세 페이지 KS X ISO 23247-1(K001010140724)·-2(참조 구조)·-4(정보 교환)가 브리프 기록과 같은 기관·제목·URL로 나타남. 단일 발행 주체(KSSN). 발행일 미확인이므로 기준일은 확인일 2026-09-25."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "원문 미열람. ISO 카탈로그 검색 결과에 ISO 23247-5:2026·23247-6:2026 등재(7월 발간), 국표원 발표는 머니투데이(ref-662) 외에 산업부 영문 보도자료·에너지데일리·아주경제 등 검색 결과로 2026-07-28 확인. ISO 와 한국 정부 발표로 교차 확인."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "원문 미열람. ISO 카탈로그 요약(스니펫)이 여러 디지털 트윈의 결합 원리·방법론을 정하고 통합·단일화·연합의 세 결합 유형을 다룬다고 적어 '여러 트윈을 골라 결합'의 핵심은 ISO·기사 두 출처로 확인. '제품·설비·공정 트윈을 블록처럼 묶어 라인·공장 전체' 예시는 기사 쪽 설명이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. NIST 과제 페이지가 검색 결과에서 기관·제목·URL 일치. 스니펫은 '신뢰할 수 있는(trustworthy) 디지털 트윈을 위한 측정 과학과 개방형 표준'을 목표로 적고 ISO 23247 과의 연계를 언급하지만 'interoperable' 문구는 스니펫에 없어 문구 조정 지시."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 예산 소진으로 이번 검증에서 재검색하지 않음. IFAC-PapersOnLine 2018 논문으로 서지(저자·제목·URL)가 알려진 문헌과 일치하고 모델·섀도·트윈 구분과 트윈 문헌이 드물다는 결론은 널리 인용되는 초록 내용이다. 단일 출처."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 두 문헌의 구분 축을 이 위키가 종합한 판단이므로 '구축자 의견'임을 밝혀야 한다. 원문 미열람."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 예산 소진으로 재검색하지 않음. Procedia Manufacturing 51(2020) 검토 논문으로 서지가 브리프 기록과 일치. 단일 출처."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과로 Le·Fan(2024) Computers & Industrial Engineering 게재 확인. '실데이터 검증 논문 소수' 문구는 브리프 발췌(초록) 기준이며 이번 스니펫에서 문구 자체는 재확인하지 못함. 단일 출처. 이 출처의 직접 인용은 이 1회뿐이어야 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 서지는 f8 과 같이 확인. 팬데믹 이후 위험·교란 관리 이점과 개념 틀 제안은 브리프 발췌(초록) 기준. 단일 출처."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 예산 소진으로 재검색하지 않음. Computers & Industrial Engineering 153(2021) 논문으로 서지가 브리프 기록과 일치. 단일 출처."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증자가 미러 raw(osrf/ros2multirobotbook src/simulation.md)를 직접 열어 확인: 같은 코드를 수정 없이 실제 시스템에서 실행, 시나리오 반복성·드문 예외 상황 연구·배치 전 장시간 시뮬레이션 문구가 있음. 발행일 미확인, 기준일 확인일."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "미러 원문에서 확인: building_map_generator 두 모드(.world 생성, 주행 그래프 내보내기)와 2D 도면 주석 수정 후 재실행으로 시뮬레이션 환경을 재구성한다는 문구. 2026-09-25-54 f8(ref-441·ref-079)과 같은 내용이다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문에서 slotcar 의 /robot_path_requests 구독, 문·승강기 요청 토픽, TeleportDispenser·TeleportIngestor, Menge 기반 crowdsim 확인. 배터리·충전기 전환(Toggle Charging)은 ref-668 README 에만 있음. 두 출처 모두 Open Robotics 계열이라 독립 교차 확인 아님."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·'연계 대상' 표시 적절. ref-668 README 는 slotcar 를 로봇 주행 스택 역할의 모델 플러그인으로 설명. 발췌의 영문 인용구는 ref-406 두 번째 직접 인용이 되므로 페이지에서는 재서술한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-668 원문 확인: gz_classic 플러그인을 통한 Gazebo Classic 지원은 Gazebo 11 EOL(2025년 1월 예정)까지만 보장, Fortress 지원. 'EOL 예정일까지만 보장'이 원문 표현이다. 뒤 절 '수명주기 관리가 필요하다'는 출처 진술이 아니라 추론이다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "미러 원문(RAWSim-O README) 확인: RMFS 이산 사건 시뮬레이션, 결정 방법 확장, 2D·3D 시각화·히트맵, C#, GPL v3 이상."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 2026-09-25-55 f32 재인용(같은 ref-398). 검증 예산 소진으로 재검색하지 않음. '크게 바꾸었다'는 저자의 시뮬레이션 조건 결과임을 밝힌다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 2026-09-25-55 재인용. 출처 published 는 null 인데 as_of 가 2006 으로 적혀 서로 맞지 않는다(식별번호 JAKO2006… 에서 추정한 값으로 보임)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 제목으로 연구의 존재만 확인. '경로망 배치안 평가가 시뮬레이션으로 이루어진다'는 일반화이며, 2026-09-25-55 f33 은 같은 출처의 해석을 [추정]으로 두었다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "미러 원문(OFacT README) 확인: Fraunhofer ISST·HSBI·FH Dortmund, 상태 모델·에이전트 제어, 일관성 검사를 포함한 데이터 통합, 시뮬레이션, 시나리오·KPI 계획 서비스, 창고·공급망 대상, Apache 2.0(문서는 CC-BY-4.0)."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "추정 → 의견. README 는 세 계층으로 나눈다: 디지털 트윈(상태 모델·에이전트 제어), 환경(데이터 통합·작업 지시·시뮬레이션·데이터 스페이스), 계획 서비스(시나리오·KPI). 데이터 통합과 시뮬레이션이 같은 환경 계층이므로 발췌의 '상태 모델·데이터 통합 대 시뮬레이션·계획' 분리 서술은 원문 구조와 다르다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 예산 소진으로 재검색하지 않음. Sargent 의 WSC V&V 튜토리얼은 해마다 여러 판이 있으므로 2008 판(40th WSC)이라는 기준을 명시한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에서 CJ대한통운 보도자료(2021-11-22, NR_00000905)와 이투데이 보도 확인. 기사는 보도자료를 전한 것이라 독립 확인이 아니다. 스니펫상 내용은 '구축했다'가 아니라 '12월부터 단계적 구축, 2023년 AI·알고리즘 적용 완성 목표'인 계획 발표이며, '몇 시간 → 수초~수분' 수치는 이번 스니펫에서 확인되지 않았다. [추정]+벤더 주장 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 예산 소진으로 재검색하지 않음. NVIDIA 블로그의 Mega 블루프린트 발표로 서지가 브리프 기록과 맞음. [추정]+벤더 주장 표시 적절. 발행일 미확인."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 분류 원문 SCM 질문을 다룬 종합 판단이다. 근거 출처 가운데 ref-398·ref-666·ref-664 가 원문 미열람인데 finding 의 source_unopened 가 false 로 적혀 있다(브리프 표시 누락). '공개 사례를 찾지 못했다'는 이번 조사 범위의 한계로 서술한다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과로 Sommer·Stjepandić·Stobrawa·von Soden(2023) JIII 33 확인. 스니펫은 '스캐너 또는 3D 카메라'와 딥러닝(CNN) 객체 인식을 말하며 '레이저 스캔'으로 한정하지 않는다. 트랙 floorplan-recognition 반영 제안(2026-09-25-19)의 내용과 맞다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 검색 스니펫상 이 논문은 디지털 트윈 시뮬레이션을 계획(prospective planning)뿐 아니라 기존 시스템 분석과 공정 병행 모니터링에도 쓸 수 있다고 적으므로, '계획용'은 논문이 생성한 모델을 계획 입력으로 쓴 용도에 한정해 서술한다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-406 원문의 문·승강기 요청 토픽, slotcar 경로 요청으로 근거가 확인된다. ROP 직접 범위 판단은 이 위키의 해석이다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·'연계 대상' 표시 적절. 원문 미열람 출처(ref-673, ref-665)에 기대며 수요예측 입력 부분은 ref-665 보다 분류 원문 9장 경계를 적용한 판단에 가깝다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. ref-406 원문이 시나리오 반복·예외 탐색·장시간 검증을 말하는 것은 확인. 22·23 목적 구분은 구축자 의견임을 밝힌다."
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
      "f17·f18·f19 는 2026-09-25-55 f32·f33(D. 계획·최적화 대분류 연결)과 같은 주장·출처(ref-398·ref-402·ref-267)이다. 같은 각주 id 를 재사용하고 f19 의 해석 부분은 그쪽처럼 [추정]으로 맞춘다",
      "f12 는 2026-09-25-54 f8(ref-441·ref-079, building_map_generator 의 주행 그래프·시뮬레이터 월드 생성)과 같은 내용이다. 충돌은 없다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f2·ref-662 는 '디지털 쓰레드', 용어 후보는 '디지털 스레드'로 적었다. 페이지와 용어집에서 '디지털 스레드(Digital Thread)' 하나로 통일한다",
      "f13 의 TeleportDispenser·TeleportIngestor 는 용어집의 '디스펜서·인제스터(dispenser-ingestor)'를 쓰고 링크한다. 디지털 섀도·디지털 트윈·이산 사건 시뮬레이션·로봇 이동형 풀필먼트 시스템은 기존 용어집 항목이 있으므로 새로 정의하지 않고 연결한다"
    ]
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "ref-406 의 직접 인용이 f11 발췌(\"the exact same code …\")와 f14 발췌('simple robot navigation stack') 두 곳에 있다. 페이지에서는 출처당 1회 원칙에 따라 f11 의 인용만 쓰거나 둘 다 재서술한다"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "모든 각주: 원문을 열지 않은 출처 ref-659·ref-660·ref-661·ref-662·ref-291·ref-664·ref-665·ref-666·ref-671·ref-672·ref-673·ref-241·ref-398·ref-402·ref-267 의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 에서 이 출처들에 source_unopened: true 를 넣는다. 이유: web_fetch_available: false 이고 raw 미러로 연 출처는 ref-406~ref-670 뿐이다.",
    "f2·f3: 검증에서 ISO 카탈로그와 국표원 발표로 교차 확인했으므로 [사실]을 유지한다. f3 의 '제품·설비·공정 트윈을 블록처럼 묶어 라인·공장 전체' 예시는 국표원 발표(ref-662) 쪽 설명이라고 밝히고 각주 ref-662 를 붙인다.",
    "f4: '신뢰할 수 있고 상호운용 가능하게'를 '신뢰할 수 있는(trustworthy) 디지털 트윈을 위한 측정 과학과 개방형 표준 개발'로 고친다. 이유: 원문 미열람 상태에서 스니펫에 'interoperable'이 없다.",
    "f6·f30: [의견]마다 '구축자 의견'임을 문장에 밝힌다. 이유: 문헌의 진술이 아니라 이 위키의 종합 판단이다.",
    "f15: 사실 부분은 'Gazebo Classic 지원은 Gazebo 11 지원 종료(2025년 1월 예정)까지만 보장한다고 README 가 적는다 [사실]'로 쓰고, '시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리가 필요하다'는 별도 문장 [추정]으로 나눈다. 이유: 뒤 절은 출처 진술이 아니라 추론이다.",
    "f18: 본문 기준일을 2006 이 아니라 확인일 2026-09-25 로 적고 각주 발행일은 '미확인'을 유지한다. 이유: 출처 published 가 null 이고 2006 은 확인되지 않았다.",
    "f19: [사실]은 '다중 AGV 경로망을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE, 2024)가 있다'까지만 쓰고, '경로망 배치안 평가가 시뮬레이션으로 이루어진다'는 [추정]으로 나누거나 뺀다. 이유: 제목만 확인했고 2026-09-25-55 f33 도 이 해석을 [추정]으로 두었다.",
    "f21: [추정] → [의견](구축자 의견)으로 강등하고, OFacT 구조를 README 대로 적는다: 상태 모델·에이전트 제어(디지털 트윈 계층), 데이터 통합·시뮬레이션(환경 계층), 시나리오·KPI(계획 서비스). 이유: 데이터 통합과 시뮬레이션이 같은 계층이라 브리프의 분리 서술이 원문과 다르다.",
    "f23: '가상 물류센터를 구축해'를 '12월부터 단계적으로 구축해 2023년 AI·알고리즘 적용 디지털 트윈을 완성하겠다는 계획을 발표했다(2021-11-22)'로 고치고, '몇 시간 걸릴 일을 수초~수분에' 수치는 뺀다. [추정]과 '벤더 주장' 병기는 유지한다. 이유: 보도자료는 계획 발표이고 해당 수치는 검증에서 확인되지 않았다.",
    "f24: [추정]과 '벤더 주장' 병기를 유지하고 9절에서 센서 시뮬레이션·합성 데이터·물리 AI 는 연계 대상으로만 쓴다. 이유: 제조사 블로그이며 독립 확인이 없다.",
    "f26: '레이저 스캔'을 '스캐너·3D 카메라 스캔'으로 고친다. 이유: 검색 요약은 레이저로 한정하지 않는다.",
    "f27: 8절·10절에서 '계획용 트윈'은 이 논문이 생성한 모델을 생산 계획 입력으로 쓴 용도에 한정한다고 적고, 논문이 공정 병행 모니터링 용도도 언급한다는 점을 함께 적는다. [추정]을 유지한다. 이유: 이 트윈 전체를 8. 실시간 세계 상태·데이터 일관성과 분리된 것으로 단정할 근거가 없다.",
    "f14 인용: ref-406 직접 인용은 f11 의 한 구절만 쓰고 f14 의 'simple robot navigation stack'은 재서술한다. 이유: 출처당 직접 인용 1회 원칙.",
    "용어: '디지털 쓰레드'를 '디지털 스레드(Digital Thread)'로 통일하고, TeleportDispenser·TeleportIngestor 는 기존 용어 '디스펜서·인제스터'에, 디지털 섀도·디지털 트윈·이산 사건 시뮬레이션·로봇 이동형 풀필먼트 시스템은 기존 용어집 항목에 링크한다. glossary_updates 에는 디지털 스레드·디지털 트윈 결합·시뮬레이션 모델 검증·타당성 확인 세 후보만 새로 등록한다.",
    "4절·10절: 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 분류 원문 문장으로 두고, f5(모델·섀도·트윈 = 데이터 연결 수준)는 이와 다른 축이라고 밝혀 섞지 않는다.",
    "10절: 27. AI·학습·적응과 모델 운영 연결은 f23·f24 벤더 주장에만 기대므로 [추정]과 '벤더 주장'을 병기하고, 교차 규칙 적용 대상(5·6·13·19·21)에 대한 근거는 이번 브리프에 없다고 적는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 1건(f21), 교차 확인 2건(f2·f3: ISO 카탈로그와 국가기술표준원 발표). 강등: f21 추정 → 의견(OFacT 계층 구조를 원문과 다르게 서술). 원문 미열람 출처: ref-659, ref-660, ref-661, ref-662, ref-291, ref-664, ref-665, ref-666, ref-671, ref-672, ref-673, ref-241, ref-398, ref-402, ref-267(raw 미러로 연 출처는 ref-406·ref-668·ref-101·ref-670이며 검증자가 다시 열어 확인함). 주의: 3·6절의 사실 주장 대부분이 단일 출처이고, 9절(ROP 직접/연계 경계)과 5절 성수기 병목 질문의 답은 이 위키의 [추정]이다. ROP 오케스트레이션 정책을 성수기 시나리오로 시험한 공개 물류센터 사례는 찾지 못했다. CJ대한통운(f23)과 NVIDIA(f24)는 벤더 주장이며, CJ대한통운 건은 구축 완료가 아니라 계획 발표다. 검증 검색 7회를 써 리서치 사용량과 합쳐 회당 상한 30회에 도달했다. 그래서 f5·f7·f9·f10·f17·f18·f19·f22·f24는 재검색하지 않고 서지 일치로만 확인했다. 브리프 표시 누락: f25는 원문 미열람 출처(ref-398·ref-666·ref-664)에 기대는데도 source_unopened가 false로 적혀 있다. 트랙 floorplan-recognition 반영 제안(2026-09-25-19, 8. 대표 연구와 자료)은 f26(사실)·f27(추정)으로 반영을 승인한다. 정정 요청 없음, 해결 인정한 열린 질문 없음."
}
```

### runs/2026-09-25-56/pages.json

```json
{
  "run_id": "2026-09-25-56",
  "outline": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "시뮬레이션·예측용 디지털 트윈은 실제 운영을 방해하지 않고 개선안을 먼저 시험하는 도구로 쓰일 수 있다. [추정][^ref-666] 다만 물류·공급망 디지털 트윈 연구 가운데 실제 데이터로 검증한 논문은 소수다. [사실][^ref-665]",
      "planned_findings": [
        "f10",
        "f11",
        "f9",
        "f8"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 750,
      "summary": "분류 원문은 8. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 나눈다. 문헌의 디지털 모델·섀도·트윈 구분은 데이터 연결 수준이라는 다른 축이다. [사실][^ref-291]",
      "planned_findings": [
        "f5",
        "f6",
        "f3",
        "f2",
        "f22"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 1000,
      "summary": "피킹 단계의 성수기 가정 시나리오. 주문 도착량·배정 규칙·자원 수를 바꿔 처리량과 대기를 비교하는 방식으로 병목을 찾는다. [추정][^ref-398][^ref-101]",
      "planned_findings": [
        "f25",
        "f17",
        "f13",
        "f28",
        "f29",
        "f19",
        "f30",
        "f8",
        "f23"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 900,
      "summary": "이 위키는 대표 접근을 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법으로 정리한다(구축자 의견). [의견][^ref-664][^ref-406][^ref-241]",
      "planned_findings": [
        "f7",
        "f10",
        "f11",
        "f13",
        "f14",
        "f12",
        "f26",
        "f24"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 850,
      "summary": "제조용 디지털 트윈 표준 ISO 23247(국내 KS X ISO 23247)과 Open-RMF 시뮬레이션, RAWSim-O, OFacT 같은 오픈소스가 있다. [사실][^ref-659][^ref-406][^ref-101][^ref-670]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f11",
        "f13",
        "f15",
        "f16",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1000,
      "summary": "이 위키는 대표 자료를 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구로 정리한다(구축자 의견). [의견][^ref-291][^ref-664][^ref-665][^ref-671][^ref-241]",
      "planned_findings": [
        "f5",
        "f7",
        "f8",
        "f9",
        "f10",
        "f17",
        "f18",
        "f19",
        "f22",
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 750,
      "summary": "ROP는 자기 배정·교통·충전 정책과 설비 요청을 시뮬레이션된 플릿·설비에 그대로 실행해 보는 몫을 맡는 것으로 보인다. [추정][^ref-406] 로봇 거동 충실도·센서 시뮬레이션·수요예측은 연계 대상이다.",
      "planned_findings": [
        "f28",
        "f14",
        "f29",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1050,
      "summary": "8. 실시간 세계 상태·데이터 일관성, 23. 시험·형식 검증·벤치마크, 21. 온보딩·설정·현장 시운전, 13. 작업 배정 — MRTA 등 12개 영역과 연결된다.",
      "planned_findings": [
        "f6",
        "f26",
        "f27",
        "f30",
        "f15",
        "f12",
        "f17",
        "f19",
        "f23",
        "f24",
        "f1",
        "f3",
        "f9",
        "f8",
        "f14"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "section": "11. 열린 질문",
      "budget_chars": 450,
      "summary": "예측 오차를 공개한 물류센터 사례, ISO 23247의 물류 적용성, 단순화 로봇 모델의 오차 보정이 열린 질문이다.",
      "planned_findings": [
        "f8",
        "f3",
        "f14",
        "f25"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(4·6·7·8·10절은 주제 페이지로 분리), 2차 수정: 4절 끊긴 문장 정정, 5절 수행 자원·완료·인계 칸 태그 정정, 6·8절 요약 [의견]화, 7절 요약 각주 보강, 9절 벤더 주장 병기, sources 정리"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area22-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 \"7. 관련 표준·프레임워크·오픈소스\" 절을 옮겼다. 2차 수정: 요약·첫 문장에 RAWSim-O·OFacT 근거 각주(ref-101·ref-670) 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area22-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 \"8. 대표 연구와 자료\" 절을 옮겼다. 2차 수정: 요약·첫 문장의 대표 자료 선정을 [의견](구축자 의견)으로 바꾸고 근거 각주 보강"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area22-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 \"10. 다른 연구영역과의 연결\" 절을 옮겼다. 2차 수정: 번호만 쓴 호칭 2곳 정정, 6. 지도·공간·위치 모델 연결을 [사실]/[추정]으로 분리, 28 연결의 '표준 기반' 단정 정정"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area22-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 \"4. 핵심 개념과 용어\" 절을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area22-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 \"6. 대표 접근법과 기술\" 절을 옮겼다. 2차 수정: 요약·첫 문장을 [의견](구축자 의견)으로 바꾸고 ref-241 각주 추가, '3절' 지칭을 원 페이지 3. 왜 중요한가 링크로 정정"
    }
  ],
  "changelog_entry": "2026-09-25 | 22. 시뮬레이션·예측용 디지털 트윈 | 영역 심화: 3~11절 신규 작성(1차 조건부 승인 수정 16건·2차 수정 11건 반영, 트랙 floorplan-recognition 반영 제안 8절 반영) | run 2026-09-25-56",
  "index_updates": {
    "home_recent": "2026-09-25 — 22. 시뮬레이션·예측용 디지털 트윈: 영역 심화로 3~11절 신규 작성(ISO 23247, Open-RMF 시뮬레이션·RAWSim-O·OFacT, 성수기 피킹 시나리오)",
    "category_recent": "2026-09-25 — 22. 시뮬레이션·예측용 디지털 트윈: 영역 심화로 3~11절 신규 작성, 8. 실시간 세계 상태·데이터 일관성과의 구분 명시",
    "area_recent": "2026-09-25 — 22. 시뮬레이션·예측용 디지털 트윈: 3~11절 신규 작성, 열린 질문 3건 등록, 8절에 트랙 건축 도면 자동 인식 반영 제안(Sommer 외 2023) 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "digital-thread",
      "term_ko": "디지털 스레드",
      "term_en": "Digital Thread",
      "definition": "제품 수명주기 전반의 설계·생산·운영 데이터를 연결해 디지털 트윈을 만들고 유지하게 하는 데이터 연결 체계로, ISO 23247-5 가 제조 디지털 트윈용 틀을 정한다.",
      "description": "ISO 23247-5:2026 은 한국(ETRI) 제안으로 2026년 발간되었다고 국가기술표준원이 2026-07-28 알렸다.",
      "related_areas": [
        22,
        28
      ],
      "sources": [
        "ref-661",
        "ref-662"
      ]
    },
    {
      "action": "new",
      "slug": "digital-twin-composition",
      "term_ko": "디지털 트윈 결합",
      "term_en": "Digital Twin Composition",
      "definition": "제품·설비·공정의 개별 디지털 트윈을 목적에 맞게 골라 묶어 라인·공장 단위의 복합 트윈을 만드는 방법으로, ISO 23247-6 이 다룬다.",
      "description": "라인·공장 단위 예시는 국가기술표준원 발표 쪽 설명이다.",
      "related_areas": [
        22,
        28
      ],
      "sources": [
        "ref-661",
        "ref-662"
      ]
    },
    {
      "action": "new",
      "slug": "verification-and-validation-of-simulation-models",
      "term_ko": "시뮬레이션 모델 검증·타당성 확인",
      "term_en": "Verification and Validation (V&V) of Simulation Models",
      "definition": "시뮬레이션 모델이 설계대로 구현되었는지(검증)와 목적에 비추어 현실을 충분히 대표하는지(타당성 확인)를 개념 모델·운영·데이터 측면에서 확인하는 절차다.",
      "description": "Sargent(2008, 40th WSC 판)는 개념 모델 타당성·모델 검증·운영 타당성·데이터 타당성과 결과 문서화·모델 인가를 다룬다.",
      "related_areas": [
        22,
        23
      ],
      "sources": [
        "ref-671"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-659",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 23247 을 부합화한 KS X ISO 23247 시리즈의 제1부 표준 상세 페이지. 검색 결과에서 제2부(참조 구조)·제4부(정보 교환) 항목도 확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s7.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-660",
      "org": "NIST",
      "title": "Digital Twins for Advanced Manufacturing",
      "published": null,
      "url": "https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 신뢰할 수 있는(trustworthy) 제조 디지털 트윈을 위한 측정 과학과 개방형 표준 개발을 목표로 하는 NIST 과제 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area22-s7.md"
      ]
    },
    {
      "id": "ref-661",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 여러 디지털 트윈을 목적에 따라 결합하는 방법을 다루는 ISO 23247 제6부 카탈로그 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s4.md",
        "docs/topics/2026/2026-09-25-area22-s7.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-662",
      "org": "머니투데이",
      "title": "설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간",
      "published": "2026-07-28",
      "url": "https://www.mt.co.kr/economy/2026/07/28/2026072809211448284",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국가기술표준원이 한국 제안 ISO 23247-5(디지털 스레드)·23247-6(디지털 트윈 결합) 발간을 알린 내용을 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area22-s4.md",
        "docs/topics/2026/2026-09-25-area22-s7.md"
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
      "summary": "원문 미열람. IFAC-PapersOnLine 게재. 디지털 모델·디지털 섀도·디지털 트윈을 구분해 제조 분야 문헌을 분류하고 연구 공백 7가지를 제시.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s4.md",
        "docs/topics/2026/2026-09-25-area22-s8.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-664",
      "org": "Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G.",
      "title": "Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics",
      "published": "2020",
      "url": "https://www.sciencedirect.com/science/article/pii/S2351978920320990",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Procedia Manufacturing 51. 물류에서 DES 와 디지털 트윈 통합 문헌을 검토하고 추세·과제를 정리.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s4.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s8.md"
      ]
    },
    {
      "id": "ref-665",
      "org": "Le, T. V., & Fan, R.",
      "title": "Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Computers & Industrial Engineering 187. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀 제안, 실데이터 검증 논문이 소수라고 보고.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s8.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-666",
      "org": "Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P.",
      "title": "Simulation-based decision support tool for in-house logistics: the basis for a digital twin",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Computers & Industrial Engineering 153. Simio 기반 사내 물류 시뮬레이션 의사결정 지원 도구를 디지털 트윈의 기초로 제안.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s8.md"
      ]
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 장: Gazebo·Ignition 연동, building_map_generator 의 월드·주행 그래프 생성, slotcar·문·승강기·작업셀·군중 플러그인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s7.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-668",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_simulation — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_simulation",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 플러그인 저장소: 문·승강기·군중·충전 전환·slotcar·읽기 전용·텔레포트 디스펜서/인제스터, 지원 Gazebo 판.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s7.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (merschformann GitHub)",
      "title": "RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "RMFS 이산 사건 시뮬레이션 프레임워크 README: 결정 문제별 방법 확장, 2D·3D 화면·히트맵, C#, GPL v3.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s7.md"
      ]
    },
    {
      "id": "ref-670",
      "org": "OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund)",
      "title": "ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README)",
      "published": null,
      "url": "https://github.com/OpenFactoryTwin/ofact",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "생산·물류용 오픈소스 디지털 트윈 프레임워크 README: 상태 모델·에이전트 제어(디지털 트윈 계층), 데이터 통합·시뮬레이션(환경 계층), 계획 서비스. Apache 2.0.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s7.md"
      ]
    },
    {
      "id": "ref-671",
      "org": "Sargent, R. G.",
      "title": "Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation)",
      "published": "2008",
      "url": "https://dl.acm.org/doi/abs/10.5555/1516744.1516780",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션 모델의 개념 모델 타당성·모델 검증·운영 타당성·데이터 타당성과 검증 절차·인가를 다룬 WSC 튜토리얼 논문(2008 판).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s4.md",
        "docs/topics/2026/2026-09-25-area22-s8.md"
      ]
    },
    {
      "id": "ref-672",
      "org": "CJ대한통운",
      "title": "가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료)",
      "published": "2021-11",
      "url": "https://www.cjlogistics.com/ko/newsroom/news/NR_00000905",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 물류센터 디지털 트윈 단계적 구축 계획(2023년 완성 목표)과 기대 효과를 알린 기업 보도자료(국내 사례, 벤더 주장).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-673",
      "org": "NVIDIA",
      "title": "NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins",
      "published": null,
      "url": "https://blogs.nvidia.com/blog/mega-omniverse-blueprint",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 시설 디지털 트윈에서 로봇 플릿을 배치 전에 시험하는 참조 작업 흐름을 소개한 벤더 블로그.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
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
      "summary": "원문 미열람. Journal of Industrial Information Integration 33. 스캐너·3D 카메라 스캔과 객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성해 생산 계획 입력으로 쓰는 방법.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s6.md",
        "docs/topics/2026/2026-09-25-area22-s8.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
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
      "summary": "원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s8.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    },
    {
      "id": "ref-402",
      "org": "KISTI ScienceON 수록 논문(저자 미확인)",
      "title": "시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화",
      "published": null,
      "url": "https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 시뮬레이션과 메타모델로 자동물류센터 설계를 최적화한 국내 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area22-s8.md"
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
      "summary": "원문 미열람. 다중 AGV 경로망을 시뮬레이션 기반으로 자동 설계하는 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md",
        "docs/topics/2026/2026-09-25-area22-s8.md",
        "docs/topics/2026/2026-09-25-area22-s10.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가?",
      "areas": [
        22,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가?",
      "areas": [
        22,
        28
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가?",
      "areas": [
        22,
        9
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    },
    {
      "step": "피킹",
      "item": "완료·인계",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "22. 시뮬레이션·예측용 디지털 트윈"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/87426.html",
      "related_areas": [
        22,
        28
      ],
      "summary": "여러 디지털 트윈을 목적에 따라 골라 결합하는 방법을 정한 ISO 23247 제6부. 국가기술표준원은 2026-07-28 한국(ETRI) 제안으로 발간됐다고 알렸다(원문 미열람).",
      "ref_id": "ref-661"
    },
    {
      "name": "KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등)",
      "kind": "표준",
      "org": "국가표준인증종합정보센터(KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "related_areas": [
        22,
        28
      ],
      "summary": "ISO 23247 을 국내에 부합화한 KS 시리즈. 제1부 개요 및 일반 원리, 제2부 참조 구조, 제4부 정보 교환 등으로 나뉜다(제3부·제정일 미확인, 원문 미열람).",
      "ref_id": "ref-659"
    },
    {
      "name": "Open-RMF rmf_simulation (시뮬레이션 플러그인)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_simulation",
      "related_areas": [
        22,
        23,
        24
      ],
      "summary": "Gazebo 에서 slotcar 로봇, 문·승강기, 디스펜서·인제스터, 군중, 충전 전환을 재현하는 플러그인 저장소. Gazebo Classic 지원은 Gazebo 11 지원 종료까지만 보장하고 Fortress 를 지원한다.",
      "ref_id": "ref-668"
    },
    {
      "name": "OFacT (Open Factory Twin)",
      "kind": "오픈소스",
      "org": "OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund)",
      "url": "https://github.com/OpenFactoryTwin/ofact",
      "related_areas": [
        22,
        8
      ],
      "summary": "생산·물류용 오픈소스 디지털 트윈 프레임워크. 상태 모델·에이전트 제어, 데이터 통합·시뮬레이션, 시나리오·KPI 계획 서비스로 구성(Apache 2.0).",
      "ref_id": "ref-670"
    }
  ],
  "additional_research_requests": [
    "4절: ISO 23247-1 의 디지털 트윈 정의 원문(신규 출처 예산으로 이번 브리프에 없음) — 용어 정의를 표준 문구로 확인하기 위해",
    "7절: KS X ISO 23247 제3부 목록과 각 부의 KS 제정일 — 표 행의 '미확인'을 채우기 위해",
    "5·11절: ROP(또는 다중 플릿 오케스트레이션) 정책을 성수기 시나리오로 시험하고 실제 처리량과 비교한 공개 물류센터 사례, 특히 국내 사례 — 2절 질문에 사례로 답하기 위해",
    "5절: CJ대한통운 물류센터 디지털 트윈의 실제 구축 여부와 효과 수치의 독립 출처 확인 — 벤더 주장 표시를 해제할 수 있는지 판단하기 위해",
    "6절: 데이터 기반 시뮬레이션 모델 자동 생성 검토 논문과 물류 디지털 트윈 대규모 사례(Ashrafian·Pedersen 2023) — 대표 접근법 절의 데이터 기반 모델 생성 항목을 채우기 위해",
    "7절: ISO 23247-6 본문의 결합 유형(통합·단일화·연합) 원문 확인 — 디지털 트윈 결합 설명을 기사 요약이 아닌 표준 문구로 보강하기 위해"
  ],
  "fixes_applied": [
    "모든 각주 원문 미열람 표시 — 원문을 열지 않은 출처 ref-659·660·661·662·291·664·665·666·671·672·673·241·398·402·267 의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙였고, reference_updates 의 이 15건에 source_unopened: true 를 넣었다(ref-406·668·101·670 은 표시하지 않음).",
    "f2·f3 — 4·7절에서 [사실]을 유지했고, 7절 표 아래에 '제품·설비·공정 트윈을 블록처럼 묶어 라인·공장 전체' 예시는 국가기술표준원 발표 쪽 설명이라고 밝히고 각주 ref-662 만 붙였다.",
    "f4 — 7절 NIST 문장을 '신뢰할 수 있는(trustworthy) 디지털 트윈을 위한 측정 과학과 개방형 표준 개발'로 고쳤고 '상호운용' 문구를 뺐다.",
    "f6·f30 — 4절(모델·섀도·트윈 축 구분), 5절 완료·인계 칸, 10절 8·23 연결 문장의 [의견]마다 '구축자 의견'임을 문장에 밝혔다.",
    "f15 — 7절에서 'Gazebo Classic 지원은 Gazebo 11 지원 종료(2025년 1월 예정)까지만 보장한다고 README 가 적는다' [사실] 문장과 '수명주기 관리가 필요해 보인다' [추정] 문장을 나눴다(10절 24 연결도 [추정]).",
    "f18 — 8절 국내 연구 항목에 '발행일 미확인, 확인일 2026-09-25'로 기준일을 적고 각주 발행일은 '미확인'을 유지했다.",
    "f19 — 8절에서 '연구가 있다' [사실]과 '경로망 배치안 평가에 시뮬레이션이 쓰인다는 해석' [추정]을 나눴고, 5절 제약 칸·10절 15 연결에는 [사실] 부분만 썼다.",
    "f21 — 7절에서 OFacT 구조를 README 대로 상태 모델·에이전트 제어(디지털 트윈 계층), 데이터 통합·시뮬레이션(환경 계층), 시나리오·KPI(계획 서비스)로 [사실] 서술하고, 분류 원문 구분과의 대응은 '구축자 의견' [의견]으로 강등했으며 데이터 통합과 시뮬레이션이 같은 계층임을 밝혔다.",
    "f23 — 5절에서 '2021-11-22 ... 12월부터 단계적으로 구축해 2023년 AI·알고리즘을 적용한 디지털 트윈을 완성하겠다는 계획을 발표했다'로 고치고 '몇 시간 → 수초~수분' 수치를 뺐으며 [추정] 벤더 주장 병기를 유지했다.",
    "f24 — 6절 NVIDIA 문장에 [추정] 벤더 주장을 유지했고, 9절 표·본문에서 센서 시뮬레이션·합성 데이터·물리 AI 는 '연계 대상'으로만 썼다.",
    "f26 — 6·8절에서 '레이저 스캔'을 '스캐너·3D 카메라 스캔'으로 고쳤다.",
    "f27 — 8절과 10절 8 연결에서 이 논문이 생성한 모델을 생산 계획 입력으로 쓴 용도에 한정한다고 적고 공정 병행 모니터링 용도도 언급함을 함께 적었으며 [추정]을 유지했다.",
    "f14 인용 — 'simple robot navigation stack' 을 '경로 요청을 받아 레일처럼 움직이는 단순한 주행 역할'로 재서술했고(6·9절), ref-406 의 f11 구절도 재서술해 ref-406 직접 인용은 페이지에 한 번도 쓰지 않았다.",
    "용어 — '디지털 쓰레드'를 쓰지 않고 '디지털 스레드(Digital Thread)'로 통일했고, TeleportDispenser·TeleportIngestor 는 용어집 '디스펜서·인제스터'에, 디지털 섀도·디지털 트윈·이산 사건 시뮬레이션·로봇 이동형 풀필먼트 시스템은 기존 용어집 항목에 링크했으며, glossary_updates 에는 디지털 스레드·디지털 트윈 결합·시뮬레이션 모델 검증·타당성 확인 세 항목만 넣었다.",
    "4절·10절 구분 — 4절에 분류 원문 문장(현재 상태를 표현 / 가정한 미래를 실험)을 [분류원문]으로 두고, f5 의 모델·섀도·트윈 구분은 데이터 연결 수준이라는 다른 축이라고 4절과 10절 8 연결에 밝혀 섞지 않았다.",
    "10절 27 연결 — 27. AI·학습·적응과 모델 운영 연결 문장에 [추정] 벤더 주장(ref-672·ref-673)을 병기하고, 교차 규칙 적용 대상(5·6·13·19·21 영역, 번호와 이름 병기)에 대한 AI 연결 근거는 이번 브리프에 없다고 적었다.",
    "분량 초과 자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 본문 9,142자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,514자",
    "형식 재작성: docs/topics/2026/2026-09-25-area22-s10.md 본문의 세부영역 링크 12건이 원 세부영역 페이지 위치 기준 경로로 남아 깨졌으므로 주제 페이지 위치 기준 '../../categories/<대분류 slug>/<파일>.md' 로 고쳤다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: 번호만 쓴 호칭 — 2026-09-25-area22-s10.md 3절의 '8번 영역'을 '8. 실시간 세계 상태·데이터 일관성'으로, '23번 영역'을 '23. 시험·형식 검증·벤치마크'로 고쳤다.",
    "2차: 6. 지도·공간·위치 모델 연결 — 2026-09-25-area22-s10.md 에서 '스캔·객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성하는 방법이 있다. [사실][^ref-241]'과 '이렇게 만든 공간 모델은 이 영역의 초기 공간 모델 생성에 해당하는 것으로 보인다. [추정][^ref-241]' 두 문장으로 나눴다.",
    "2차: 28. 표준·상호운용성·다사업자 거버넌스 연결 — '제조용 디지털 트윈 표준 ISO 23247 시리즈(디지털 트윈 결합 포함)가 관련 표준이다. [사실][^ref-659][^ref-661]'로 고치고, 물류센터 적용 여부는 원 페이지 11. 열린 질문의 둘째 질문으로 남아 있다고 링크와 함께 적었다.",
    "2차: 7절 요약 각주 — 세부영역 페이지 7절 요약 문장과 2026-09-25-area22-s7.md 세 줄 요약·3절 첫 문장에 [^ref-101][^ref-670]을 더했고, 세부영역 페이지 13절에 ref-670 각주 정의를 더했다.",
    "2차: 6·8절 요약 [의견]화 — 세부영역 페이지 6·8절 요약 문장과 2026-09-25-area22-s6.md·s8.md 의 세 줄 요약·3절 첫 문장을 '이 위키는 …로 정리한다(구축자 의견). [의견]'으로 바꾸고, 6절은 ref-664·ref-406·ref-241, 8절은 ref-291·ref-664·ref-665·ref-671·ref-241 각주를 붙였으며, 세부영역 페이지 13절에 ref-241·ref-671 정의를 더했다.",
    "2차: 5절 수행 자원 칸 — '시뮬레이션된 로봇(slotcar 모델)과 문·승강기 설비 플러그인이 Open-RMF 의 경로·문·승강기 요청에 응답한다. [사실][^ref-406][^ref-668]'로 고치고 ROP 연결은 바로 뒤 [추정] 문장에만 두었다.",
    "2차: 5절 완료·인계 칸 — 태그 없던 첫 문장을 뒤 문장과 합쳐 '시뮬레이션 결과를 업무 완료나 재고 변경으로 인정하지 않고, 채택안의 변경 후 동작 확인은 23. 시험·형식 검증·벤치마크로 넘긴다는 구분은 구축자 의견이다. [의견][^ref-406]'으로 고쳤다.",
    "2차: 9절 벤더 주장 병기 — '로봇 자체 지능·제어' 행 외부 연계 칸을 로봇 거동 충실도 [추정][^ref-406][^ref-668] 문장과 센서 시뮬레이션·합성 데이터·물리 AI '[추정] 벤더 주장[^ref-673]' 문장으로 나눴다.",
    "2차: 4절 끊긴 문장 — 세부영역 페이지 4절의 '분류 원문은 이렇게 적는다.'를 '분류 원문의 해당 문장은 2절 원문 주석에 있다.'로 고쳤다.",
    "2차: s6 '3절' 지칭 — 2026-09-25-area22-s6.md 의 '한계는 3절에서 본 실데이터 검증 부족이다.'를 원 세부영역 페이지의 '3. 왜 중요한가' 절 링크(#3-왜-중요한가)를 가리키는 문장으로 고쳤다.",
    "2차: 프런트매터 sources — 세부영역 페이지 sources 를 13절 각주 정의(ref-101·241·267·291·398·406·659·661·664·665·666·668·670·671·672·673)와 같게 맞췄고, 본문에서 인용하지 않는 ref-402·ref-660·ref-662 는 빼서 분리 주제 페이지(s8·s7·s4) 프런트매터에만 두었다."
  ]
}
```

### runs/2026-09-25-56/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-56/pages/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈"
type: area
category: "F. 도입·검증·유지관리"
area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [디지털 트윈, 이산 사건 시뮬레이션, ISO 23247, Open-RMF 시뮬레이션, 시나리오 실험]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-101, ref-241, ref-267, ref-291, ref-398, ref-406, ref-659, ref-661, ref-664, ref-665, ref-666, ref-668, ref-670, ref-671, ref-672, ref-673]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 22. 시뮬레이션·예측용 디지털 트윈

# 22. 시뮬레이션·예측용 디지털 트윈

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 3. 왜 중요한가

시뮬레이션·예측용 디지털 트윈은 실제 운영을 방해하지 않고 개선안을 먼저 시험하는 도구로 쓰일 수 있어, 2절의 성수기 병목 질문에 실제 성수기가 오기 전에 답하는 수단이 된다. [추정][^ref-666]

Coelho 외(2021)는 사내 물류 시뮬레이션 모델이 현실을 대표하면 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다. [사실][^ref-666] 로봇 플릿 쪽에서는 Open-RMF 문서가 물리 시뮬레이터를 쓰면 배터리 소모나 충돌 비용 없이 시나리오를 반복하고, 드문 예외 상황을 탐색하고, 현장 배치 전에 장시간 검증을 할 수 있다고 설명한다(확인일 2026-09-25). [사실][^ref-406]

공급망 수준에서도 Le·Fan(2024)은 COVID-19 이후 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고 물류·공급망 디지털 트윈 개념 틀을 제안했다. [사실][^ref-665] 다만 같은 검토는 실제 데이터로 검증한 논문이 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 예측이 현장에서 얼마나 맞는지는 아직 확인할 과제로 남는다. [사실][^ref-665]

## 4. 핵심 개념과 용어

이 위키는 디지털 트윈을 용도로 나눈다: 현재 상태를 표현하는 것은 8. 실시간 세계 상태·데이터 일관성, 그 모델을 이용해 가정한 미래를 실험하는 것은 이 영역이다. 분류 원문의 해당 문장은 2절 원문 주석에 있다.

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area22-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹

**시나리오:** 성수기 주문 증가를 앞두고 피킹 배정 규칙과 로봇 대수를 가상 환경에서 비교

| 항목 | 내용 |
|---|---|
| 시작 조건 | 성수기 주문·물동량 전망이 시나리오 입력으로 들어온다. 이 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다(연계 대상). [추정][^ref-665][^ref-673] |
| 작업 대상 | 가정한 성수기 주문의 피킹 작업(가상 환경 안의 주문·운반 흐름) |
| 수행 자원 | 시뮬레이션된 로봇(slotcar 모델)과 문·승강기 설비 플러그인이 Open-RMF 의 경로·문·승강기 요청에 응답한다. [사실][^ref-406][^ref-668] ROP는 자기 배정·교통·충전 정책을 이 가상 플릿·설비에 그대로 실행해 보는 것으로 보인다. [추정][^ref-406][^ref-668] |
| 제약 | 주문 도착량·배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 어디가 먼저 막히는지 본다. [추정][^ref-398][^ref-101] 경로망 배치도 시뮬레이션으로 설계하는 연구가 있다. [사실][^ref-267] |
| 완료·인계 | 시뮬레이션 결과를 업무 완료나 재고 변경으로 인정하지 않고, 채택안의 변경 후 동작 확인은 23. 시험·형식 검증·벤치마크로 넘긴다는 구분은 구축자 의견이다. [의견][^ref-406] |
| 예외·성과 | Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398] 예측이 실제와 맞는지는 실데이터 검증이 부족해 미확인이다. [사실][^ref-665] |

다음은 설명을 위한 가상의 시나리오이다. 물류센터 운영자가 성수기 전에 피킹 구역에서 어느 자원이 먼저 포화되는지 알고 싶어 한다. 이미 공개된 이산 사건 시뮬레이션 연구·도구는 이런 질문에 도착량·규칙·자원 수를 바꿔 결과를 비교하는 방식으로 답한다. 다만 ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사 범위에서 찾지 못했다. [추정][^ref-398][^ref-101][^ref-666][^ref-664]

국내에서는 CJ대한통운이 2021-11-22 현실 물류센터와 같은 가상 물류센터를 12월부터 단계적으로 구축해 2023년 AI·알고리즘을 적용한 디지털 트윈을 완성하겠다는 계획을 발표했고, 작업 동선·재고 배치·설비 효율 최적화와 장비 고장·피킹 오류·상품 파손 원인의 사전 파악을 목표로 들었다. [추정] 벤더 주장[^ref-672]

## 6. 대표 접근법과 기술

이 위키는 대표 접근을 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법으로 정리한다(구축자 의견). [의견][^ref-664][^ref-406][^ref-241]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area22-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준으로는 제조용 디지털 트윈 프레임워크 ISO 23247(국내 KS X ISO 23247)이 있고, 오픈소스로는 Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-659][^ref-406][^ref-101][^ref-670]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area22-s7.md)에 있다.

## 8. 대표 연구와 자료

이 위키는 대표 자료를 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구로 정리한다(구축자 의견). [의견][^ref-291][^ref-664][^ref-665][^ref-671][^ref-241]

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료](../../topics/2026/2026-09-25-area22-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP가 직접 맡는 몫은 자기 작업 배정·교통·충전 정책과 설비 요청을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보인다. [추정][^ref-406][^ref-668]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 경로 요청을 받는 단순화 로봇 모델에 자기 배정·교통·충전 정책을 실행해 보는 것 [추정][^ref-406][^ref-668] | 연계 대상: 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도는 제조사·물리 시뮬레이터 영역으로 보인다. [추정][^ref-406][^ref-668] 센서 시뮬레이션·합성 데이터·물리 AI는 시뮬레이터 제공자 영역이다. [추정] 벤더 주장[^ref-673] |
| 시설·설비 제어 | 문·승강기 요청을 시뮬레이션 설비 플러그인에 보내고 응답을 받는 흐름의 시험 [추정][^ref-406] | 연계 대상: 실제 승강기·컨베이어·PLC·설비 안전 제어([범위 경계](../../about/scope-boundary.md)) |
| 상위 업무 시스템 | 주문 도착량·배정 규칙·자원 수를 바꿔 처리량·대기를 비교하는 시나리오 실험 [추정][^ref-398][^ref-101] | 연계 대상: 시나리오의 주문·물동량 전망은 수요예측에서 받는 입력 [추정][^ref-665] |

Open-RMF 시뮬레이션의 로봇 모델은 경로 요청을 받아 레일식으로 움직이는 단순화 모델이어서, ROP 시뮬레이션은 로봇 거동보다 플릿 조율·설비 상호작용 실험에 초점이 맞는 것으로 보인다. [추정][^ref-406][^ref-668] 센서 시뮬레이션·합성 데이터를 앞세운 제품 소개는 벤더 주장이며 ROP 직접 범위가 아니다. [추정] 벤더 주장[^ref-673] 경계는 제품 전략에 따라 움직일 수 있으므로 [범위 경계](../../about/scope-boundary.md) 페이지를 함께 본다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 상태 모델(8. 실시간 세계 상태·데이터 일관성)을 받아 미래를 실험하고, 그 결과를 시험·배정·교통·수명주기 영역으로 넘긴다. 아래 연결은 이 절의 각 문장 태그대로 읽는다.

자세한 내용은 주제 페이지 [22. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area22-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? 실데이터 검증 논문이 소수라는 검토가 배경이다.[^ref-665]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가?[^ref-661]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가?[^ref-668]

2절의 질문 가운데 ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못해 미확인으로 남긴다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-101]: Merschformann, M. (merschformann GitHub), RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-659]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-661]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-664]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-665]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-666]: Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P., Simulation-based decision support tool for in-house logistics: the basis for a digital twin, 2021, https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646, 접근일 2026-09-25 (원문 미열람)
[^ref-668]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-670]: OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund), ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README), 미확인, https://github.com/OpenFactoryTwin/ofact, 접근일 2026-09-25
[^ref-671]: Sargent, R. G., Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation), 2008, https://dl.acm.org/doi/abs/10.5555/1516744.1516780, 접근일 2026-09-25 (원문 미열람)
[^ref-672]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-09-25 (원문 미열람)
[^ref-673]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 미확인, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈"
type: area
category: "F. 도입·검증·유지관리"
area_no: 22
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 22. 시뮬레이션·예측용 디지털 트윈

# 22. 시뮬레이션·예측용 디지털 트윈

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

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

### runs/2026-09-25-56/pages/topics/2026/2026-09-25-area22-s7.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-659, ref-660, ref-661, ref-662, ref-406, ref-668, ref-101, ref-670]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#7
---

[홈](../../index.md) › [주제](../index.md) › 22. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스

# 22. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준으로는 제조용 디지털 트윈 프레임워크 ISO 23247(국내 KS X ISO 23247)이 있고, 오픈소스로는 Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-659][^ref-406][^ref-101][^ref-670]
- 이 페이지는 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준으로는 제조용 디지털 트윈 프레임워크 ISO 23247(국내 KS X ISO 23247)이 있고, 오픈소스로는 Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-659][^ref-406][^ref-101][^ref-670]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 23247 / KS X ISO 23247 | 표준 | 제조를 위한 디지털 트윈 프레임워크. 국내 부합화판은 제1부 개요 및 일반 원리, 제2부 참조 구조, 제4부 정보 교환 등으로 나뉜다(제3부 목록과 각 부 제정일은 미확인, 확인일 2026-09-25). [사실][^ref-659] | KSSN(원문 미열람) |
| ISO 23247-5:2026·ISO 23247-6:2026 | 표준 | 디지털 트윈을 위한 디지털 스레드(제5부)와 디지털 트윈 결합(제6부). 국가기술표준원은 2026-07-28 두 표준이 한국(ETRI) 제안으로 발간됐다고 알렸다. [사실][^ref-661][^ref-662] | ISO 카탈로그·기사(원문 미열람) |
| Open-RMF 시뮬레이션(rmf_simulation) | 오픈소스 | 물리 시뮬레이터에서 플릿·문·승강기·작업셀·군중을 재현하고 같은 코드를 실제 시스템에 쓴다. [사실][^ref-406][^ref-668] | 공식 문서·저장소 |
| RAWSim-O | 오픈소스 | [로봇 이동형 풀필먼트 시스템](../../glossary/robotic-mobile-fulfillment-system.md)(RMFS)의 이산 사건 시뮬레이션 프레임워크. 운영 결정 문제에 새 결정 방법을 끼워 넣어 효과를 연구하고 2D·3D 화면과 로봇 위치 히트맵을 제공한다(C#, GPL v3). [사실][^ref-101] | 저장소 README |
| OFacT(Open Factory Twin) | 오픈소스 | Fraunhofer ISST 등이 개발한 생산·물류용 디지털 트윈 프레임워크. 상태 모델, 주문·자원 에이전트 제어, 일관성 검사를 포함한 데이터 통합, 시나리오 평가·예측용 시뮬레이션, KPI 비교 계획 서비스를 갖춘다(Apache 2.0). [사실][^ref-670] | 저장소 README |

ISO 23247-6은 여러 디지털 트윈을 목적에 따라 골라 결합하는 방법을 정한다. [사실][^ref-661][^ref-662] 제품·설비·공정의 개별 트윈을 블록처럼 묶어 라인·공장 전체의 복합 트윈을 만든다는 예시는 국가기술표준원 발표 쪽의 설명이다. [사실][^ref-662] NIST의 제조용 디지털 트윈 과제는 신뢰할 수 있는(trustworthy) 디지털 트윈을 위한 측정 과학과 개방형 표준 개발을 목표로 둔다(확인일 2026-09-25). [사실][^ref-660]

rmf_simulation README는 Gazebo Classic 지원을 Gazebo 11 지원 종료(2025년 1월 예정)까지만 보장한다고 적고 Gazebo Fortress를 지원 대상으로 둔다(확인일 2026-09-25). [사실][^ref-668] 따라서 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리가 필요해 보인다. [추정][^ref-668]

OFacT README는 상태 모델·에이전트 제어(디지털 트윈 계층), 데이터 통합·시뮬레이션(환경 계층), 시나리오·KPI(계획 서비스)로 구성요소를 나눈다. [사실][^ref-670] 현재 상태를 담는 상태 모델과 시나리오를 돌리는 계획 서비스가 따로 있는 점은 분류 원문의 현재 표현/미래 실험 구분과 같은 방향으로 읽을 수 있다는 것이 구축자 의견이다. 다만 데이터 통합과 시뮬레이션은 같은 환경 계층에 있다. [의견][^ref-670]

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)
- 관련 영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-659]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-660]: NIST, Digital Twins for Advanced Manufacturing, 미확인, https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing, 접근일 2026-09-25 (원문 미열람)
[^ref-661]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-662]: 머니투데이, 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간, 2026-07-28, https://www.mt.co.kr/economy/2026/07/28/2026072809211448284, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-668]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-101]: Merschformann, M. (merschformann GitHub), RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-670]: OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund), ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README), 미확인, https://github.com/OpenFactoryTwin/ofact, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-56 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-56 | 22. 시뮬레이션·예측용 디지털 트윈 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-56/pages/topics/2026/2026-09-25-area22-s8.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-241, ref-267, ref-398, ref-402, ref-291, ref-664, ref-665, ref-666, ref-671]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#8
---

[홈](../../index.md) › [주제](../index.md) › 22. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료

# 22. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 위키는 대표 자료를 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구로 정리한다(구축자 의견). [의견][^ref-291][^ref-664][^ref-665][^ref-671][^ref-241]
- 이 페이지는 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 위키는 대표 자료를 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구로 정리한다(구축자 의견). [의견][^ref-291][^ref-664][^ref-665][^ref-671][^ref-241]

- Kritzinger 외, Digital Twin in manufacturing: A categorical literature review and classification(2018) — 디지털 모델·섀도·트윈으로 제조 문헌을 분류했다. 용어를 쓸 때의 기준점이다. [사실][^ref-291]
- Agalianos 외, Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics(2020) — 물류에서 DES가 실시간 데이터를 받아 디지털 트윈의 일부로 진화한다고 정리했다. [사실][^ref-664]
- Le·Fan, Digital twins for logistics and supply chain systems(2024) — 물류·공급망 디지털 트윈 개념 틀을 제안하고, 실데이터 검증 논문이 소수라고 보고했다. [사실][^ref-665]
- Coelho 외, Simulation-based decision support tool for in-house logistics(2021) — 사내 물류 시뮬레이션을 디지털 트윈의 기초로 제안했다. [사실][^ref-666]
- Merschformann 외, Decision rules for robotic mobile fulfillment systems(2019) — RMFS 결정 규칙을 시뮬레이션으로 비교했고, 저자의 시뮬레이션 조건에서 피킹 주문 배정 규칙이 처리량을 크게 바꾸었다. [사실][^ref-398]
- 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화(국내 연구, 발행일 미확인, 확인일 2026-09-25) — 시뮬레이션과 메타모델을 결합해 자동물류센터 설계를 최적화했다. [사실][^ref-402]
- Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems(IEEE T-ASE, 2024) — 다중 AGV 경로망을 시뮬레이션 기반으로 자동 설계하는 연구가 있다. [사실][^ref-267] 경로망 배치안 평가에 시뮬레이션이 쓰인다는 해석은 제목 수준의 추정이다. [추정][^ref-267]
- Sargent, Verification and validation of simulation models(2008, 40th WSC 판) — 개념 모델 타당성·모델 검증·운영 타당성·데이터 타당성과 결과 문서화·모델 인가를 다룬다. [사실][^ref-671]
- Sommer 외, Automated generation of digital twin for a built environment using scan and object detection as input for production planning(2023) — 스캐너·3D 카메라 스캔과 객체 인식으로 건조 환경 트윈을 자동 생성해 생산 계획 입력으로 썼다. [사실][^ref-241] 이 논문이 생성한 모델을 생산 계획 입력으로 쓴 용도는 이 영역의 초기 모델 생성에 해당하는 것으로 보이며, 논문이 공정 병행 모니터링 용도도 언급하므로 트윈 전체를 8. 실시간 세계 상태·데이터 일관성과 분리된 것으로 단정하지는 않는다. [추정][^ref-241] 이 항목은 [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) 트랙의 반영 제안에서 왔다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)
- 관련 영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-664]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-665]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-666]: Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P., Simulation-based decision support tool for in-house logistics: the basis for a digital twin, 2021, https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646, 접근일 2026-09-25 (원문 미열람)
[^ref-671]: Sargent, R. G., Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation), 2008, https://dl.acm.org/doi/abs/10.5555/1516744.1516780, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-56 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-56 | 22. 시뮬레이션·예측용 디지털 트윈 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-56/pages/topics/2026/2026-09-25-area22-s10.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-241, ref-267, ref-398, ref-659, ref-661, ref-291, ref-665, ref-406, ref-668, ref-672, ref-673]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#10
---

[홈](../../index.md) › [주제](../index.md) › 22. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결

# 22. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 현재 상태 모델(8. 실시간 세계 상태·데이터 일관성)을 받아 미래를 실험하고, 그 결과를 시험·배정·교통·수명주기 영역으로 넘긴다. 아래 연결은 이 절의 각 문장 태그대로 읽는다.
- 이 페이지는 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 현재 상태 모델(8. 실시간 세계 상태·데이터 일관성)을 받아 미래를 실험하고, 그 결과를 시험·배정·교통·수명주기 영역으로 넘긴다. 아래 연결은 이 절의 각 문장 태그대로 읽는다.

- [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) — 분류 원문의 구분(현재 상태를 표현 / 가정한 미래를 실험)을 따른다. 문헌의 모델·섀도·트윈 구분은 데이터 연결 수준이라는 다른 축이므로 섞지 않는다는 것이 구축자 의견이다. [의견][^ref-291] Sommer 외(2023)의 트윈은 계획 입력 용도에 한정해 이 영역에 연결하며, 모니터링 용도는 8. 실시간 세계 상태·데이터 일관성과 겹칠 수 있다. [추정][^ref-241]
- [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 시나리오 반복·예외 탐색 환경을 공유하지만, 이 영역은 운영 정책·수요 변화의 효과 예측, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인으로 목적을 나누는 것이 분류 원문 정의에 맞다는 것이 구축자 의견이다. [의견][^ref-406]
- [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) — 시뮬레이터 판 교체(Gazebo Classic 지원 종료)가 시뮬레이션 환경의 수명주기 관리를 요구하는 것으로 보인다. [추정][^ref-668]
- [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 주석한 도면에서 시뮬레이터 월드와 주행 그래프를 함께 만드는 흐름이 새 현장 설정과 이어진다. [사실][^ref-406]
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 스캔·객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성하는 방법이 있다. [사실][^ref-241] 이렇게 만든 공간 모델은 이 영역의 초기 공간 모델 생성에 해당하는 것으로 보인다. [추정][^ref-241]
- [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 배정 규칙의 처리량 효과를 시뮬레이션으로 비교한 연구가 있다. [사실][^ref-398]
- [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — 다중 AGV 경로망을 시뮬레이션 기반으로 설계하는 연구가 있다. [사실][^ref-267]
- [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) — 공급망 위험·교란 관리에서 디지털 트윈의 이점이 부각됐다는 검토가 있다. [사실][^ref-665]
- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 디지털 트윈을 AI 적용·물리 AI 시험 환경으로 쓴다는 연결은 CJ대한통운 계획 발표와 NVIDIA 소개에만 기댄다. [추정] 벤더 주장[^ref-672][^ref-673] 교차 규칙 적용 대상(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전)과의 AI 연결 근거는 이번 브리프에 없다.
- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 제조용 디지털 트윈 표준 ISO 23247 시리즈(디지털 트윈 결합 포함)가 관련 표준이다. [사실][^ref-659][^ref-661] 이 표준을 물류센터에 적용할 수 있는지는 원 페이지 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#11-열린-질문)의 둘째 질문으로 남아 있다.
- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 제조사 로봇을 단순화 모델로 시뮬레이션할 때 실제 거동과의 차이를 보정할 데이터가 필요해 보인다. [추정][^ref-668]
- [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) — 시뮬레이션 예측을 실제 성과와 비교한 실데이터 검증이 부족하다. [사실][^ref-665]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)
- 관련 영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-659]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-661]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-665]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-668]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-672]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-09-25 (원문 미열람)
[^ref-673]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 미확인, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-56 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-56 | 22. 시뮬레이션·예측용 디지털 트윈 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-25-56/pages/topics/2026/2026-09-25-area22-s4.md

````markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-661, ref-662, ref-291, ref-664, ref-671]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#4
---

[홈](../../index.md) › [주제](../index.md) › 22. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어

# 22. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 위키는 디지털 트윈을 용도로 나눈다: 현재 상태를 표현하는 것은 8. 실시간 세계 상태·데이터 일관성, 그 모델을 이용해 가정한 미래를 실험하는 것은 이 영역이다. 분류 원문은 이렇게 적는다.
- 이 페이지는 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 위키는 디지털 트윈을 용도로 나눈다: 현재 상태를 표현하는 것은 8. 실시간 세계 상태·데이터 일관성, 그 모델을 이용해 가정한 미래를 실험하는 것은 이 영역이다. 분류 원문은 이렇게 적는다.

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

- **디지털 모델·디지털 섀도·디지털 트윈(Digital Model / [Digital Shadow](../../glossary/digital-shadow.md) / [Digital Twin](../../glossary/digital-twin.md))** — Kritzinger 외(2018)가 제조 문헌을 분류한 세 단계로, 가장 높은 단계인 디지털 트윈을 다룬 문헌은 드물고 모델·섀도 문헌이 더 많았다. [사실][^ref-291] 이 구분은 실물과 데이터가 얼마나 자동으로 연결되는가라는 축이며, 분류 원문의 현재 표현/미래 실험 구분과는 다른 축이다. 그래서 이 위키는 두 축을 섞지 않고 용도(현재 표현/미래 실험)로 나눠 적는다는 것이 구축자 의견이다. [의견][^ref-291][^ref-664]
- **[이산 사건 시뮬레이션](../../glossary/discrete-event-simulation.md)(Discrete Event Simulation, DES)** — 물류에서 DES는 사물인터넷 장치의 실시간 데이터를 질의하며 디지털 트윈의 한 부분으로 진화하고 있다는 정리가 있다. [사실][^ref-664]
- **디지털 트윈 결합(Digital Twin Composition)** — 여러 디지털 트윈을 목적에 따라 골라 결합하는 방법으로, ISO 23247-6(2026)이 다룬다. [사실][^ref-661][^ref-662]
- **디지털 스레드(Digital Thread)** — ISO 23247-5(2026)가 다루는 디지털 트윈을 위한 데이터 연결 체계다. [사실][^ref-661][^ref-662]
- **시뮬레이션 모델 검증·타당성 확인(Verification and Validation, V&V)** — 개념 모델 타당성, 모델 검증, 운영 타당성, 데이터 타당성을 나누어 확인하는 틀이다(Sargent, 2008년 판 기준). [사실][^ref-671]

```mermaid
flowchart LR
  WS["8. 실시간 세계 상태·데이터 일관성: 현재 상태 표현"] -->|그 모델을 이용| SIM["22. 시뮬레이션·예측용 디지털 트윈: 가정한 미래 실험"]
  DEM["상위 업무 시스템 수요 전망: 연계 대상"] --> SIM
  SIM -->|채택안| TEST["23. 시험·형식 검증·벤치마크: 변경 후 동작 확인"]
```

도식의 앞 화살표는 분류 원문의 구분을, 뒤 두 화살표는 9·10절의 구축자 추정·의견을 그린 것이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)
- 관련 영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-661]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-662]: 머니투데이, 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간, 2026-07-28, https://www.mt.co.kr/economy/2026/07/28/2026072809211448284, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-664]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-671]: Sargent, R. G., Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation), 2008, https://dl.acm.org/doi/abs/10.5555/1516744.1516780, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-56 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-56 | 22. 시뮬레이션·예측용 디지털 트윈 의 "핵심 개념과 용어" 절에서 분리 |
````

### runs/2026-09-25-56/pages/topics/2026/2026-09-25-area22-s6.md

```markdown
---
title: "22. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 22
related_areas: [4, 6, 8, 9, 13, 15, 20, 21, 23, 24, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-241, ref-664, ref-666, ref-406, ref-668, ref-673]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#6
---

[홈](../../index.md) › [주제](../index.md) › 22. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술

# 22. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 위키는 대표 접근을 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법으로 정리한다(구축자 의견). [의견][^ref-664][^ref-406][^ref-241]
- 이 페이지는 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 위키는 대표 접근을 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법으로 정리한다(구축자 의견). [의견][^ref-664][^ref-406][^ref-241]

### 이산 사건 시뮬레이션

Agalianos 외(2020)는 물류 4.0에서 DES가 실시간 데이터를 받아 디지털 트윈의 일부가 되고, 이를 통해 창고 계획·관리·의사결정을 지원한다고 정리했다. [사실][^ref-664] Coelho 외(2021)는 Simio로 만든 사내 물류 의사결정 지원 도구를 디지털 트윈의 기초로 제안했다. [사실][^ref-666] 한계는 원 세부영역 페이지의 [3. 왜 중요한가](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md#3-왜-중요한가) 절에서 본 실데이터 검증 부족이다.

### 물리 시뮬레이터와 같은 코드 실행

Open-RMF는 Gazebo·Ignition 물리 시뮬레이터를 ROS 2와 연결해, 시뮬레이션에 쓴 코드를 수정 없이 실제 시스템에서도 실행한다고 설명한다. [사실][^ref-406] 로봇용 slotcar 플러그인(레일식 주행과 가감속), 문·승강기 플러그인, 작업셀 적재·하역을 흉내 내는 [디스펜서·인제스터](../../glossary/dispenser-ingestor.md) 플러그인(TeleportDispenser·TeleportIngestor), Menge 기반 보행자 군중 시뮬레이션, 배터리·충전기 동작 전환 도구를 제공한다. [사실][^ref-406][^ref-668] slotcar는 경로 요청을 받아 레일처럼 움직이는 단순한 주행 역할만 하므로 로봇의 로컬 주행 알고리즘은 재현하지 않는 것으로 보인다. [추정][^ref-406][^ref-668]

### 도면·스캔에서 초기 모델 생성

Open-RMF의 building_map_generator는 traffic_editor로 주석한 도면 파일에서 시뮬레이터 월드와 플릿 어댑터용 주행 그래프를 함께 만들어, 레이아웃이 바뀌면 주석을 고쳐 다시 생성할 수 있다. [사실][^ref-406] Sommer 외(2023)는 스캐너·3D 카메라 스캔과 객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성해 생산 계획 입력으로 쓰는 방법을 제안했다. [사실][^ref-241]

### 벤더 참조 작업 흐름

NVIDIA는 Mega Omniverse 블루프린트를 공장·창고 디지털 트윈에서 로봇 플릿과 물리 AI를 배치 전에 시험하는 참조 작업 흐름(센서 시뮬레이션·합성 데이터 생성 결합)으로 소개하고, KION·Accenture가 창고·유통 공정 최적화에 쓴다고 밝혔다. [추정] 벤더 주장[^ref-673]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)
- 관련 영역: [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-664]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-666]: Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P., Simulation-based decision support tool for in-house logistics: the basis for a digital twin, 2021, https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-668]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-673]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 미확인, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-56 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-56 | 22. 시뮬레이션·예측용 디지털 트윈 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-56/docs_tree.txt

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
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
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
glossary/root-cause-analysis-rca.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
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
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 524건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 134개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
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
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
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
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [22] 에 걸린 1건 / 전체 83건)

```markdown
- oq-081 [열림] 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? (영역 20, 22)
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

### runs/2026-09-25-56/verification2.json

```json
{
  "run_id": "2026-09-25-56",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "2차: 분리 주제 페이지 2026-09-25-area22-s10.md 의 6. 지도·공간·위치 모델 연결 문장이 '스캔·객체 인식으로 만든 공간 모델이 시뮬레이션의 초기 공간 모델이 된다'를 [사실][^ref-241]로 적었다. '초기 모델 생성에 해당한다'는 1차에서 [추정]으로 유지한 f27 의 해석이므로 태그를 올린 것이다. 사실 부분(f26: 자동 생성 방법이 있다)과 해석 부분([추정])으로 나눠야 한다. 원문 미열람."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "2차: 세부영역 페이지 5절 표 '수행 자원' 칸의 '시뮬레이션된 로봇과 문·승강기 설비 플러그인이 ROP의 요청에 응답한다 [사실]'. ref-406·ref-668 원문(1차에서 raw 미러로 확인)은 Open-RMF 의 /door_requests·/lift_requests·경로 요청에 응답한다고만 적는다. 그 요청을 'ROP의 요청'으로 부르는 것은 f28 의 [추정] 해석이다. 사실 문장은 Open-RMF 요청으로 한정하고, ROP 와의 연결은 바로 뒤 [추정] 문장에만 둔다."
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
      "f17·f18·f19 는 2026-09-25-55 와 같은 각주 id(ref-398·ref-402·ref-267)를 재사용했고, f19 의 해석은 그쪽처럼 [추정]으로 나눴다. 충돌 없음",
      "f12 는 2026-09-25-54 f8 과 같은 내용이며 충돌 없음"
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
    "2026-09-25-area22-s10.md 3절 8. 실시간 세계 상태·데이터 일관성 항목의 '모니터링 용도는 8번 영역과 겹칠 수 있다'와 23. 시험·형식 검증·벤치마크 항목의 '23번 영역은 변경 후 동작 확인'을 번호와 이름을 함께 쓴 호칭('8. 실시간 세계 상태·데이터 일관성', '23. 시험·형식 검증·벤치마크')으로 고친다 — 이유: 번호만 쓴 호칭은 공통 표기 규약 위반이다(원문 인용이 아니다).",
    "2026-09-25-area22-s10.md 3절 6. 지도·공간·위치 모델 항목: '스캔·객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성하는 방법이 있다. [사실][^ref-241]'과 '이렇게 만든 공간 모델은 이 영역의 초기 공간 모델 생성에 해당하는 것으로 보인다. [추정][^ref-241]' 두 문장으로 나눈다 — 이유: 해석 부분은 1차에서 [추정]으로 유지한 f27 인데 [사실]로 올렸다.",
    "2026-09-25-area22-s10.md 3절 28. 표준·상호운용성·다사업자 거버넌스 항목의 'ISO 23247 시리즈와 디지털 트윈 결합 표준이 이 영역의 표준 기반이다. [사실]'을 '제조용 디지털 트윈 표준 ISO 23247 시리즈(디지털 트윈 결합 포함)가 관련 표준이다. [사실][^ref-659][^ref-661]'로 고치고, 물류센터에 적용할 수 있는지는 11. 열린 질문의 둘째 질문으로 남아 있다고 적는다 — 이유: '이 영역의 표준 기반'은 브리프에 없는 판단이고, 같은 페이지가 올린 열린 질문과도 모순된다.",
    "세부영역 페이지 7절 요약 문장과 2026-09-25-area22-s7.md 세 줄 요약·3절 첫 문장('…Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-659][^ref-406]')에 RAWSim-O 와 OFacT 의 근거 각주 [^ref-101][^ref-670]을 더한다. 세부영역 페이지 13절에는 ref-670 각주 정의를 references 형식 그대로 더한다 — 이유: 인용한 두 각주가 RAWSim-O·OFacT 를 뒷받침하지 않는다.",
    "세부영역 페이지 6절·8절 요약 문장과 2026-09-25-area22-s6.md·2026-09-25-area22-s8.md 의 세 줄 요약·3절 첫 문장('대표 접근은 …이다 [사실]', '대표 자료는 …이다 [사실]'): 대표 항목을 고른 것은 이 위키의 정리이므로 '이 위키는 …로 정리한다'는 형태의 [의견](구축자 의견)으로 바꾼다. 각주는 6절에 ref-664·ref-406·ref-241, 8절에 ref-291·ref-664·ref-665·ref-671·ref-241 를 붙이고, 세부영역 페이지 13절에 없는 정의(ref-241·ref-671)를 더한다 — 이유: 선정 판단을 [사실]로 표기했고, 스캔·검증 틀 항목은 각주 근거가 빠졌다.",
    "세부영역 페이지 5절 표 '수행 자원' 칸: '시뮬레이션된 로봇(slotcar 모델)과 문·승강기 설비 플러그인이 Open-RMF 의 경로·문·승강기 요청에 응답한다. [사실][^ref-406][^ref-668]'로 고친다. ROP 와의 연결은 바로 뒤 [추정] 문장에만 둔다 — 이유: 출처는 'ROP의 요청'을 말하지 않는다(f28 은 [추정]).",
    "세부영역 페이지 5절 표 '완료·인계' 칸 첫 문장 '시뮬레이션 결과는 업무 완료나 재고 변경으로 인정되지 않는다.'는 태그가 없는 단정이다. 뒤 문장과 합쳐 구축자 의견([의견])에 포함하거나 삭제한다 — 이유: 브리프 finding 에 대응하지 않는 주장이다.",
    "세부영역 페이지 9절 표 '로봇 자체 지능·제어' 행의 외부 연계 칸에서 센서 시뮬레이션·합성 데이터·물리 AI 부분을 ref-673 에 기댈 때는 '벤더 주장'을 병기한다(예: '… [추정] 벤더 주장[^ref-673]'). ref-406 근거인 로봇 거동 충실도 부분은 별도 [추정][^ref-406][^ref-668] 로 둔다 — 이유: 1차 수정 지시 f24(벤더 주장 병기 유지).",
    "세부영역 페이지 4절 첫 단락이 '분류 원문은 이렇게 적는다.'로 끝나는데, 인용 문장이 주제 페이지로 옮겨져 뒤에 아무것도 없다. 이 문장을 '분류 원문의 해당 문장은 2절 원문 주석에 있다.'처럼 고치거나 삭제한다 — 이유: 게시 페이지에서 문장이 이어지지 않는다.",
    "2026-09-25-area22-s6.md 3절 '이산 사건 시뮬레이션' 소절의 '한계는 3절에서 본 실데이터 검증 부족이다.'를 원 세부영역 페이지의 '3. 왜 중요한가' 절을 가리키는 표현(링크 포함)으로 고친다 — 이유: 주제 페이지 안의 3절은 본문이므로 가리키는 대상이 모호하다.",
    "세부영역 페이지 프런트매터 sources 를 13절에 정의된 각주 id 와 같게 맞춘다(위 수정 뒤 본문에서 인용하지 않는 ref-402·ref-660·ref-662 는 빼고, 분리 주제 페이지 프런트매터에 둔다) — 이유: 태그·각주 유지 항목의 프런트매터–각주 일치 조건."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 1건(f21), 교차 확인 2건(f2·f3: ISO 카탈로그와 국가기술표준원 발표). 강등: f21 추정 → 의견(OFacT 계층 구조를 원문과 다르게 서술). 원문 미열람 출처: ref-659, ref-660, ref-661, ref-662, ref-291, ref-664, ref-665, ref-666, ref-671, ref-672, ref-673, ref-241, ref-398, ref-402, ref-267. raw 미러로 연 출처는 ref-406·ref-668·ref-101·ref-670이다. 주의: 3·6절의 사실 주장 대부분이 단일 출처이고, 9절(ROP 직접/연계 경계)과 5절 성수기 병목 질문의 답은 이 위키의 [추정]이다. ROP 오케스트레이션 정책을 성수기 시나리오로 시험한 공개 물류센터 사례는 찾지 못했다. CJ대한통운(f23)과 NVIDIA(f24)는 벤더 주장이며, CJ대한통운 건은 구축 완료가 아니라 계획 발표다. 트랙 floorplan-recognition 반영 제안(2026-09-25-19)은 f26·f27로 8절에 반영됐다. 정정 요청 없음, 해결 인정한 열린 질문 없음. / 2차 수정 후 재검증. 1차 수정 지시 16건의 이행을 확인했다. 원문 미열람 표시, f4·f15·f18·f19·f21·f23·f26·f27 문구, 인용 재서술, 디지털 스레드 용어 통일, 구축자 의견 명시가 모두 반영됐다. 드리프트·태그 문제 11건을 수정 지시로 넘긴다. 주요 항목: 분리 주제 페이지의 번호만 쓴 호칭 2곳, 6. 지도·공간·위치 모델 연결에서 f27 해석을 [사실]로 올림, 28. 표준·상호운용성·다사업자 거버넌스 연결의 '표준 기반' 단정, 6·7·8절 요약 문장의 선정 판단 [사실] 표기와 근거 각주 누락, 5절 수행 자원 칸의 'ROP의 요청' [사실], 9절 표의 벤더 주장 병기 누락. [분류원문] 보존, 섹션 순서 준수(형식 검증 통과), 링크 유효. 참고: 9절 표 '상위 업무 시스템' 행은 ROP 직접 몫에 f25(DES 연구 방식)를 옮겨 썼다. [추정]이라 이번에는 지적하지 않았지만, f28의 범위(자기 정책을 시뮬레이션에 실행)로 읽어야 한다.",
  "retry_reason": null
}
```
