(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- 세부영역 반영 제안: 6건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- next_ref_id: ref-629
- 새 출처 id 구간: ref-629 ~ ref-658 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-629 부터 순서대로 쓰고 ref-658 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

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

### data/area_reflection_proposals.json (대상 영역 21. 온보딩·설정·현장 시운전 에 대한 트랙 반영 제안 6건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-11",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "6. 대표 접근법과 기술",
      "summary": "현장 시운전에서 평면도를 배경으로 벽·문·승강기·차선·충전 정점을 사람이 주석하고 측정으로 축척을 맞추는 방식(Open-RMF traffic-editor, f1·f2). 제품 쪽 평면도 PNG 업로드·축척 요건은 [추정] 벤더 주장(MiR Fleet, 유통사 게재본, f4). 운영 요소가 사람 주석으로 남는 점(f20, [추정]).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-11",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "8. 대표 연구와 자료",
      "summary": "전문가의 지도 작성 노동을 줄이려는 평면도 기반 위치추정 동기(Boniardi 외 2019, f6)와 국내 문헌고찰의 현장 검증·지표 보고 부족(f18, 건설로봇 대상).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-19",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "6. 대표 접근법과 기술",
      "summary": "다중 AGV 도입 병목(정밀 지도, 픽업·하역 위치 좌표, 경로망 설계)을 3D 스캔 의미 지도로 줄이는 반자동 방법(Beinschob 외 2017, ref-217)과 충전기 앞으로 로봇을 몰고 가 마커로 위치를 등록하는 절차(벤더 주장, ref-219).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-22",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "3. 왜 중요한가",
      "summary": "새 현장 AGV·이동로봇 도입의 긴 설치 시간 원인으로 정밀 2D 지도 작성, 픽업·하역 위치 지정, 전문가 수작업 경로망 설계가 꼽힌다(Beinschob 외 2017 [사실], ref-217). 지도 작성은 새 환경 배치의 시간이 많이 드는 과정이다(Heselden·Das 2024 [사실], ref-269). PAN-Robots 설치 기간 6개월→2개월은 과제 측 보고값(비교 조건 미확인, [추정], ref-265).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-22",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "6. 대표 접근법과 기술",
      "summary": "새 현장·새 제조사마다 반복되는 작업(지도 작성 주행, 위치 지정, 경로망 설계, 좌표 대응, 형식별 레이아웃 재입력)의 정리: [추정], ref-217·ref-079·ref-105·ref-046. Open-RMF 플릿 어댑터 설정의 층별 좌표 대응점·사양·작업 능력 항목: [사실], ref-105. OTTO 설정 복제·부분 재지도화: [추정] 벤더 주장, ref-271.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-22",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 21,
      "section": "8. 대표 연구와 자료",
      "summary": "Beinschob 외(2017, ref-217), Beinschob·Reinke(2015, ref-266), 다중 AGV 경로망 자동 설계 연구(IEEE T-ASE 2024, ref-267, 비교 절 제외), Rüdt 외(2025, ref-268), Heselden·Das(2024, ref-269), PAN-Robots CORDIS 기사(ref-265, [추정]).",
      "status": "제안"
    }
  ]
}
```

### docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md (요약)

```markdown
# 22. 시뮬레이션·예측용 디지털 트윈

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 23. 시험·형식 검증·벤치마크

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [분류원문]

## 2. SCM 관점의 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md (요약)

```markdown
# 24. 자산·소프트웨어 수명주기 관리

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [분류원문]

## 2. SCM 관점의 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 465건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 117개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
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
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
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
```

### docs/open-questions.md (요약: 대상 영역 [21] 에 걸린 1건 / 전체 72건)

```markdown
- oq-022 [열림] 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? (영역 6, 21)
```

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
# area_no 는 1~28 의 세부영역 번호다. 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 7. 화물·재고·자산 식별과 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 7            # 7. 화물·재고·자산 식별과 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "팔레트 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 7            # 주 연구영역: 7. 화물·재고·자산 식별과 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 팔레트 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 7            # 7. 화물·재고·자산 식별과 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1~7). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
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

### runs/2026-09-25-51/research.md

```markdown
# 리서치 브리프 2026-09-25-51

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-51 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 2 · 답한 질문 q2-02

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-02 열림(target.json 지정, CLI 지정 질문 id). 같은 질문을 다룬 실행 2026-09-25-43 은 트랙 최근 실행 표에서 생성·갱신 0/0 으로 끝나 단계 2 페이지 3절에 q2-02 소제목이 없고 백로그 상태도 '열림'이다
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 페이지 4절에 표준·형식 목록 비교 없음(q2-01 데이터 항목만 실림)
- 완료 조건: 업무 분해·배정 설계 초안의 진행 상태·배정 개념 속성이 외부 표현 형식과 대조되지 않음(두 개념 모두 상태 '초안'·일부 확정)
- 13. 작업 배정 — MRTA 페이지 섹션 7. 관련 표준·프레임워크·오픈소스에 배정 결과(누구에게 배정했는가)와 배정 과정 상태를 기록하는 형식 근거 없음
- 로봇 작업 표현을 다루는 IEEE 표준(IEEE 1872.1-2024)이 트랙 페이지에 아직 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q2-02 분해한 작업과 배정 결과를 표현하는 기존 표준·형식(작업·미션 기술, 워크플로 기술)은 무엇이 있고, ROP의 작업 모델에 비해 무엇이 빠지는가?
3. 로봇 관제 쪽 형식(Open-RMF 복합 작업 기술·작업 상태, VDA 5050 주문·동작, MassRobotics 상태 보고)은 작업의 단계 구조·배정 결과·진행 상태를 어떤 필드로 표현하는가? (단계 2 페이지 3절, 13. 작업 배정 — MRTA 섹션 7 겨냥)
4. 업무·워크플로 쪽 형식(OPC UA for ISA-95 작업 지시·작업 응답, BPMN 2.0.2 수행자, Serverless Workflow DSL)은 작업 구조·수행 자원·기한·우선순위를 어떻게 표현하는가? (1. 주문·업무 시스템 연계, 2. 공정·워크플로 모델링 연결)
5. 로봇 계획·실행 표현(HDDL 계층적 작업 네트워크, 행동 트리 XML)과 로봇 작업 표현 표준(IEEE 1872.1-2024)은 분해 구조와 작업 지식을 어떻게 기술하며, 로봇 임무 기술 형식을 비교한 연구는 무엇을 보는가? (14. 작업 순서·스케줄링 연결)
6. 서로 다른 로봇·플릿의 작업 선후를 표준 형식 안에서 표현·집행할 수단이 있는가? (oq-049 관련)
7. 국내에 로봇 작업·임무 기술 형식을 정한 KS 표준이나 연구가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 복합(compose) 작업 기술 스키마는 수행 순서대로 나열한 단계(phases) 배열만 필수로 두고, 각 단계는 플릿이 지원하는 활동 기술과 맞아야 하는 활동(activity: 범주와 기술)을 필수로, 작업 취소 시 수행할 활동 목록(on_cancel)을 선택으로 두며, 운영자에게 보일 범주·상세는 선택 필드다. | ref-600 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | Open-RMF 작업 상태 스키마는 예약 정보(booking)만 필수로 두고, 배정 결과를 그룹(group)과 이름(name)으로 된 assigned_to 로, 배정 과정을 queued·selected·dispatched·failed_to_assign·canceled_in_flight 값의 dispatch 상태로, 진행을 queued·underway·delayed·completed·canceled·failed 등의 status 값과 단계별 상태·예상 소요 시간(estimate_millis)·시작·종료 시각으로 표현한다. | ref-599 | 아니오 | medium | 2026-09-25 | 피킹 / 수행 자원 | — |
| f3 | [추정] | 이번에 연 Open-RMF 복합 작업·작업 상태 스키마에서 의존 관계는 한 단계 안의 사건(event) 사이 deps 로만 나타나고, 작업과 작업 사이의 선행 의존, 배정 근거(선택 이유·산출 방식), 사용자 확인 여부를 담는 필드는 확인되지 않아, 이 항목은 ROP 의 작업 모델이 따로 보유해야 할 것으로 보인다. | ref-599, ref-600 | 아니오 | low | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 은 관제의 최소 기능으로 주문의 이동로봇 배정을 두지만, 주문은 로봇 한 대가 지나갈 노드–간선 그래프 구간이고 전체 운반 주문은 orderId·orderUpdateId 로 이어진 여러 하위 주문으로 나뉠 수 있으며, 외부 IT 시스템과의 인터페이스는 범위에서 제외하므로 업무·작업 수준의 구조나 배정 근거를 담는 메시지는 두지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f5 | [사실] | VDA 5050 3.0.0 의 사전 정의 동작 waitForTrigger 는 이동로봇이 관제(FLEET_CONTROL)나 로봇 자체 입력(LOCAL)의 트리거를 기다리게 하고, 관제는 제3 시스템에서 기다리던 과정이 끝났다는 정보를 받으면 순간 동작 trigger 로 이를 풀며, 시간 초과 처리와 필요 시 주문 취소는 관제가 맡는다. | ref-031 | 아니오 | medium | 2026-09-25 | 피킹 / 완료·인계 | — |
| f6 | [사실] | MassRobotics AMR 상호운용 표준의 JSON 스키마는 로봇이 내보내는 식별 보고(identityReport)와 상태 보고(statusReport)만 정의하고 로봇에 작업을 보내는 메시지는 두지 않으며, 상태 보고에 운용 상태(navigating, idle, charging, waitingHumanEvent 등)와 예측 시각이 붙은 목적지(destinations)·약 10초의 단기 경로(path)를 담는다. | ref-601 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | OPC UA for ISA-95 작업 제어 노드셋에서 작업 지시 데이터형은 시작·종료 시각, 우선순위(숫자가 클수록 높음), 인원·설비·물리 자산·자재 요구를 선택 필드로 두고, 작업 응답 데이터형은 연결된 작업 지시 id·실제 시작·종료 시각·작업 상태(JobState)와 인원·설비·물리 자산·자재 실적(Actuals)을 두며, 설비 데이터형의 ID 는 설비 클래스 또는 개별 설비를 가리킬 수 있다. | ref-130 | 아니오 | medium | 2024-01-31 | 완료·인계 | — |
| f8 | [추정] | 이번에 연 ISA-95 작업 제어 노드셋의 작업 지시·작업 응답 데이터형에서는 작업 지시 사이의 선행·의존 관계를 담는 필드가 확인되지 않았고, 작업 상태 기계의 상태 이름도 열람 응답에서 확인되지 않았다. | ref-130 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | OMG BPMN 2.0 명세는 활동을 맡을 사람 역할을 수행자의 특수화인 사람 수행자(HumanPerformer)와 그 하위 역할인 잠재 담당자(PotentialOwner)로 지정하고, 자원 배정 식(ResourceAssignmentExpression)으로 실행 시 사용자·그룹 같은 자원을 역할에 배정하게 한다. | ref-605 | 아니오 | medium | 2014-01 | 수행 자원 | 원문 미열람 |
| f10 | [사실] | Corradini 외는 BPMN 기반 다중 로봇 시스템 개발 틀 FaMe 를 제안했으며(Robotics and Autonomous Systems 160권), 공개 저장소는 다중 로봇의 협력을 BPMN 모델로 조직하는 틀로 소개한다. | ref-606 | 아니오 | medium | 2023 | — | — |
| f11 | [사실] | Open Workflow Specification(Serverless Workflow) DSL 문서는 워크플로 작업 유형으로 call·do(순차)·emit·for·fork(병렬)·listen·raise·run·set·switch·try·wait 를 두고, 시간 초과 시 실행을 중단하고 timeout 오류를 내게 하며, every·cron·after·on 으로 일정을 표현한다. | ref-602 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [추정] | 이번에 연 Serverless Workflow DSL 문서에서는 작업을 특정 수행자·자원에 배정하거나 우선순위·기한을 표현하는 개념이 확인되지 않았다. | ref-602 | 아니오 | low | 2026-09-25 | — | — |
| f13 | [사실] | BehaviorTree.CPP 는 행동 트리를 실행 시 불러오는 XML 기반 도메인 특화 언어로 정의하고, 사용자 정의 노드를 정적으로 링크하거나 플러그인으로 불러오며, 비동기 동작을 기본으로 지원하고 상태 전이를 기록·재생하는 로깅 기반을 둔다. | ref-603 | 아니오 | medium | 2026-09-25 | — | — |
| f14 | [사실] | HDDL(Höller 외, AAAI 2020)은 PDDL 을 확장해 상위 작업(task)과 그 작업을 하위 작업·동작의 부분 또는 전체 순서 네트워크로 분해하는 방법(method)을 기술하는 계층적 작업 네트워크(HTN) 계획 언어로, 2020년 국제 계획 경진대회 첫 계층 계획 부문의 공통 언어로 만들어졌다. | ref-604 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f15 | [사실] | IEEE 1872.1-2024(로봇 작업 표현 표준)는 학습·로봇·자동화 분야의 작업 지식을 표현·추론·교환하기 위한 온톨로지를 정의하며, 계층적 계획기와 설계자가 작업 지식을 표현하는 방식을 다루고, 실무 구현 지침 P1872.1.1 이 따로 개발되고 있다. | ref-608 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f16 | [사실] | Filippone·Pettinari·Pelliccione(GSSI, arXiv 2603.15427)는 로봇·다중 로봇 임무 기술 형식으로 행동 트리, 상태 기계, 계층적 작업 네트워크, BPMN 네 가지를 제어 구조·임무 개념·표현력·도구 지원 측면에서 비교 분석했다. | ref-607 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f17 | [추정] | q2-02 에 대해 이번에 확인한 형식을 업무 분해·배정 설계 초안과 대조하면, 로봇 관제 형식(Open-RMF, VDA 5050)은 작업 단계·배정 결과·진행 상태를, 업무 형식(ISA-95 작업 지시·응답)은 기한 후보·우선순위·자원 요구·실적을, 워크플로 형식(BPMN, Serverless Workflow)과 계획·실행 표현(HDDL, 행동 트리)은 분해·순서 구조나 수행자 지정을 담지만, 지시 원문과 상황 값의 출처, 배정 근거·산출 방식, 사용자 확인 여부를 함께 담는 형식은 찾지 못해 ROP 는 이 항목을 자체 작업 모델에 두고 외부 형식으로 옮겨야 할 것으로 보인다(IEEE 1872.1 본문은 미열람이라 대조하지 못함). | ref-599, ref-600, ref-031, ref-130, ref-605, ref-602, ref-604, ref-603, ref-608 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | 확인한 형식 가운데 서로 다른 로봇·플릿 작업 사이의 선행 의존을 필드로 표현하는 것은 없었고(Open-RMF 의 deps 는 한 단계 안 사건 사이에 한정), VDA 5050 의 waitForTrigger–trigger 처럼 관제가 다른 과정의 완료 정보를 받아 로봇을 풀어 주는 동작이 플릿 사이 동기화 수단이 될 수 있어 보이나, 그 판단·시간 초과 처리는 관제(ROP) 몫으로 남는다. | ref-031, ref-599, ref-130 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f19 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 표준 형식의 배정 결과(Open-RMF assigned_to·dispatch 상태, ISA-95 설비 실적)는 누가 맡았는지만 남기므로, 최근접 배정과 다른 배정 기준의 전체 효과를 사후에 비교하려면 ROP 가 배정 근거·목적함수 값을 별도로 기록해야 할 것으로 보인다. | ref-599, ref-130 | 아니오 | low | 2026-09-25 | 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-599 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-600 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json | 아니오 |
| ref-601 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-602 | CNCF Serverless Workflow (serverlessworkflow/specification GitHub) | Serverless Workflow Specification — dsl.md | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/serverlessworkflow/specification/blob/main/dsl.md | 아니오 |
| ref-603 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP | 아니오 |
| ref-604 | Höller, D., Behnke, G., Bercher, P., Biundo, S., Fiorino, H., Pellier, D., & Alford, R. | HDDL – A Language to Describe Hierarchical Planning Problems | 2019-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1911.05499 | 예 |
| ref-605 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | medium | 2026-09-25 | https://www.omg.org/spec/BPMN/2.0.2/ | 예 |
| ref-606 | Pettinari, S. (FaMe 공식 저장소, UNICAM PROS) | FaMe — a BPMN-driven framework for Multi-Robot System development (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/SaraPettinari/fame | 아니오 |
| ref-607 | Filippone, G., Pettinari, S., & Pelliccione, P.(GSSI) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-608 | IEEE Standards Association | IEEE 1872.1-2024 — IEEE Standard for Robot Task Representation | 2024 | 표준 | medium | 2026-09-25 | https://standards.ieee.org/ieee/1872.1/6993/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-02 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19 (신뢰도 low) — 2절 q2-02 상태 답함, 3절 q2-02 소제목 신설({#q2-02}): 로봇 관제 형식(Open-RMF 복합 작업·작업 상태 f1·f2, VDA 5050 주문 단위·배정 기능 f4, waitForTrigger f5, MassRobotics 보고 전용 f6), 업무 형식(ISA-95 작업 지시·응답 f7·f8), 워크플로 형식(BPMN 수행자 f9, BPMN 다중 로봇 틀 f10, Serverless Workflow f11·f12), 계획·실행 표현(HDDL f14, 행동 트리 XML f13), 로봇 작업 표현 표준 IEEE 1872.1(f15, 본문 미열람), 임무 기술 형식 비교 연구(f16), 초안 대비 빠진 항목(f3·f17), 플릿 사이 선후(f18), SCM 질문 연결(f19) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 4 | 아이디어 페이지 4절: '작업·배정 결과를 표현하는 표준·형식' 소절 신설 — 형식 비교표(f1·f2·f4·f6·f7·f9·f11·f13·f14·f15), 초안 대비 빠진 항목(f3·f17, 추정), 임무 기술 형식 비교 연구(f16). 평가 데이터(q2-03)는 미조사임을 명시 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(진행 상태 값의 외부 표현 원천, 배정 결과의 외부 표현 대응 메모)가 승인되면 2절 반영과 초안 버전 인상(f2·f4·f7·f3·f19). 미승인 부분과 플릿 사이 선행 의존(f18), IEEE 1872.1 과의 대응(f15)은 6절 질문으로 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f2, f4, f19): Open-RMF 작업 상태의 배정 결과(assigned_to)·배정 과정(dispatch) 상태, VDA 5050 의 배정 기능과 주문 단위, 배정 근거 기록 필요와 분류 원문 질문 연결 |
| update | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f7, f9, f10, f11, f16): ISA-95 작업 응답의 실적 필드, BPMN 수행자와 다중 로봇 BPMN 틀 FaMe, Serverless Workflow, 임무 기술 형식 비교 연구 |
| update | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f1, f5, f14, f18): Open-RMF 복합 작업의 단계 순서, HDDL 의 하위 작업 부분·전체 순서 표현, VDA 5050 waitForTrigger 를 통한 플릿 사이 동기화 가능성(oq-049 관련) |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 7 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f15): 로봇 작업 지식 표현 온톨로지 표준 IEEE 1872.1-2024(본문 미열람)와 구현 지침 P1872.1.1 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 계층적 작업 네트워크 | Hierarchical Task Network (HTN) | 복합 작업을 미리 정한 분해 방법으로 하위 작업 네트워크로 나누어 결국 실행 가능한 기본 동작의 순서에 이르게 하는 자동 계획 방식이다. |
| 계층 도메인 정의 언어 | Hierarchical Domain Definition Language (HDDL) | PDDL 을 확장해 작업·분해 방법과 하위 작업의 부분 또는 전체 순서를 기술하는 계층적 작업 네트워크 계획 문제의 공통 기술 언어이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 12 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 10건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 형식마다 단일 공식 파일·단일 논문
    - f9 BPMN 2.0.2 명세 원문 미열람(검색 요약 범위), 절 번호 미확인
    - f14 HDDL·f16 Filippone 외 원문 미열람(검색 요약 범위)
    - f15 IEEE 1872.1-2024 본문 유료로 미열람: 작업 분해·배정·의존을 어떤 개념으로 표현하는지 미확인
    - f3·f8·f12 는 연 문서 범위의 부재 관찰이며 부재 확인 아님
    - f18 waitForTrigger 를 플릿 사이 선후 집행에 쓴 사례 미확인
    - ISA-95 작업 상태 기계의 상태 이름 미확인
    - f10 FaMe 의 BPMN 협업 다이어그램·실행 환경 세부는 README 에 없어 미확인
- 범위 경계 위반 의심:
    - 없음
- 한계: web_fetch_available: false · fetch_mode mirror_only. 원문을 연 출처: ref-031(입력 원문 텍스트, inbox), ref-130·ref-599·ref-600·ref-601·ref-602·ref-603·ref-606(github_raw). 원문 미열람: ref-604(HDDL), ref-605(BPMN 2.0.2), ref-607(Filippone 외), ref-608(IEEE 1872.1-2024) — 신뢰도 상한 medium. 검색 7회/40, 신규 출처 10건/20(ref-599~ref-608, 예약 구간 안), 재사용 2건(ref-031, ref-130). 질문 선택: target.json 지정 q2-02 1건. 같은 질문을 다룬 실행 2026-09-25-43 은 트랙 최근 실행 표에서 생성·갱신 0/0 이고 백로그·단계 페이지에 q2-02 가 여전히 '열림'이라 반영되지 않은 것으로 보고 다시 조사했다. 그 브리프가 쓴 ref-569~ref-573 은 실행 2026-09-25-30 이 쓴 같은 번호와 겹치고, ref-111·ref-114·ref-116·ref-230 은 입력 참고문헌 목록(요약)에 없어 이번에는 같은 문서를 원문으로 다시 열고 예약 구간의 새 id 를 부여했다(같은 URL 이 기존에 있으면 퍼블리셔가 합친다 — 퍼블리셔 확인 필요). 새로 더한 것: IEEE 1872.1-2024(로봇 작업 표현 표준), FaMe README. q2-02 는 형식별 필드 관찰로 답했으나 초안 대비 빠진 항목(f17)은 이 위키의 대응 추론이라 질문 종합 신뢰도를 low 로 두었다. 한국 자료: 한국어 검색 1회에서 로봇 작업·임무 기술 형식을 정한 KS 표준이나 국내 연구를 찾지 못함(KS B ISO 8373·10218, KS B 7321-2, KS B 7323 같은 용어·안전·모듈 정보 모델 표준만 확인되어 finding 으로 넣지 않음). 교차 규칙: 이번 finding 은 LLM 방법이 아니라 표현 형식이라 27. AI·학습·적응과 모델 운영 반영은 제안하지 않았다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 새 일반 열린 질문 없음: 플릿 사이 선후는 기존 oq-049, 배정 비교 실측은 oq-052 와 겹친다. 용어 후보 2건(f14 근거). 트랙 glossary_targets 가운데 용어집에 없는 '사람 확인 루프'는 이번 finding 근거가 없어 내지 않았다. 후속 질문 3건. 온톨로지 변경 제안 2건. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 4건(갱신 상한과 별도).

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 2
- 답한 질문 id: q2-02

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | ROP 가 업무→작업 분해 구조를 내부에 둘 때 BPMN·Serverless Workflow·HDDL 같은 기존 형식을 표준 표현으로 채택할지, 자체 작업 모델 스키마를 두고 Open-RMF 복합 작업·VDA 5050 주문으로 변환할지, 변환 때 배정 근거·확인 여부는 어디에 남기는가? (q2-02 에서 파생) | 3 | f17 |
| — | Open-RMF 복합 작업의 단계와 VDA 5050 waitForTrigger–trigger 를 조합해 제조사가 다른 플릿 사이 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 집행할 수 있는가, 트리거 누락·시간 초과 때 누가 복구하는가? (q2-02 에서 파생) | 3 | f18 |
| — | IEEE 1872.1-2024 로봇 작업 표현 온톨로지는 작업 분해·선후 의존·배정 대상을 어떤 개념으로 표현하며, 업무 분해·배정 설계 초안의 업무·작업·배정 개념과 어떻게 대응하는가? (q2-02 에서 파생) | 2 | f15 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 진행 상태 (Progress) | f2, f7 | 속성 '상태 값'에 외부 표현 원천 후보를 메모로 단다: Open-RMF 작업 상태 status 값(queued·underway·delayed·completed·canceled·failed 등)과 배정 과정 dispatch 값(queued·selected·dispatched·failed_to_assign·canceled_in_flight), ISA-95 작업 응답의 JobState·실제 시작·종료 시각. 초안의 '접수·실행·완료·취소' 네 값과의 대응 규칙은 6절 질문으로 둔다. |
| modify | concept | 배정 (Assignment) | f2, f4, f3, f19 | 배정 결과의 외부 표현 대응을 메모로 단다: Open-RMF 는 assigned_to(그룹·이름)와 dispatch 상태로, VDA 5050 은 주문을 받는 로봇으로 배정 대상만 표현하고 선택 근거·배정 산출 방식·확인 여부 필드는 없어 작업 모델이 보유한다. 기존 속성과 충돌하지 않는 메모 수준 제안이다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 필요한 데이터 항목과 표준·형식 목록이 아이디어 2. 자연어 업무 지시 챗봇 4절에 아직 실리지 않음(이번 제안 반영 전), 평가 데이터(q2-03) 미조사
    - 작업 모델의 정보 항목이 업무 분해·배정 설계 초안 개념 목록 표에 일부만 반영됨(작업 요구의 적재물 속성·완료 조건 미확정)
    - 열린 질문 q2-03, q2-04, q2-05, q2-06
```

### runs/2026-09-25-50/research.md

```markdown
# 리서치 브리프 2026-09-25-50

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-50 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 20. 예외 복구·재계획·업무 연속성 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 운반 중 고장 난 로봇의 화물·남은 주문 처리 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-003, oq-021, oq-038, oq-048 이 이 영역과 관련

## 조사 질문

1. 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]
2. 로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 고장·통신 단절·작업 취소·일시정지·재계획을 어떤 메시지·기능으로 다루는가? (섹션 6·7 겨냥)
3. 지연·고장이 생겼을 때 다중 로봇 경로와 작업 배정을 실시간으로 재계획하는 연구는 무엇이 있는가? (섹션 6·8 겨냥)
4. 업무 연속성 관리 표준과 국내 제도는 무엇이며 로봇 현장의 제한 운영·수동 전환 계획과 어떻게 연결되는가? (섹션 3·7 겨냥, 한국 자료 우선)
5. 이미 수행한 물리 작업을 취소·되돌릴 때 이벤트 기록과 재고를 어떻게 바로잡는가? (oq-021, oq-003 관련, 섹션 4·6 겨냥)
6. 통신 단절이나 관제 어댑터 재시작 동안 작업을 어디까지 계속하고 재연결 뒤 어떻게 맞추는가? (oq-038, oq-048 관련, 섹션 6·11 겨냥)
7. 예외 복구에서 ROP 직접 범위와 연계 대상(로봇 자체 복구·안전 제어, 상위 WMS)의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세에서 이동로봇은 즉시 동작 cancelOrder 를 받으면 가능한 한 빨리 정지하고, 예정된 동작은 FAILED 로 보고하며, 정지 뒤 cancelOrder 상태를 FINISHED 로 보고하고 유휴 상태가 된다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 MQTT 라스트 윌 메시지로 관제가 로봇의 연결 끊김을 감지하게 하고(connectionState ONLINE·OFFLINE·CONNECTION_BROKEN), 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 최신판 state 스키마는 오류 수준(errorLevel)을 WARNING·URGENT·CRITICAL·FATAL 로, 동작 상태(actionStatus)에 RETRIABLE 을 두며, 명세는 RETRIABLE 상태의 로봇이 관제나 운영자의 개입을 기다린다고 설명한다. | ref-051, ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 state 스키마의 loads 배열은 로봇에 실린 적재물의 식별번호(loadId), 종류, 적재 위치(loadPosition), 치수, 무게를 보고하게 하므로 고장 로봇에 어떤 화물이 실려 있는지 관제가 알 수 있는 근거가 된다. | ref-051 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f5 | [사실] | VDA 5050 의 startPause 즉시 동작은 자동 주행을 멈추고 일시정지 가능한 동작(pauseAllowed=true)만 멈추며, stopPause 로 주문 실행을 재개한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | VDA 5050 은 교착(deadlock) 탐지·해소와 통신 오류 탐지·해소를 관제(fleet control)의 역할로 두고, 구역 충돌 같은 상황에서 사용자 개입이 필요한지, 현재 주문을 취소하고 새 주문을 보낼지를 관제가 결정한다고 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 플릿 어댑터의 RobotUpdateHandle 은 작업 중단(interrupt)과 재개(resume), 작업 취소(cancel_task)·강제 종료(kill_task), 마지막 보고 위치에서의 재계획 요청(replan), 작업 수락 중지(set_commission), 이슈 생성(create_issue) 기능을 제공한다. | ref-570 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [사실] | Open-RMF 의 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자 사이의 협상이 시작되며, 긴급 참여자는 의도적으로 충돌을 게시해 협상을 강제할 수 있다. | ref-004 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 중단하고 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 RMF 에 제어권 없이 상태만 보고한다. | ref-569, ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f10 | [사실] | Open-RMF rmf_ros2 이슈 224 는 플릿 어댑터가 재시작되면 배정된 작업이 유실되는 문제를 제기하고, 작업 로그·백업을 SQLite 로 저장하는 PR 161 과 rmf-web 영속 데이터베이스를 조회하는 대안을 제안하지만, 배포판 반영 여부는 이번에 확인되지 않았다. | ref-582 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f11 | [사실] | Hönig 외(IEEE RA-L, 2019)는 MAPF 계획을 후처리해 로봇 간 순서와 운동 제약을 행동 의존 그래프(ADG)로 인코딩함으로써 예기치 않은 감속·장애물·지연에도 계획을 충돌 없이 실행하고 재계획과 실행을 겹치게 하는 창고용 실행 틀을 제시한다. | ref-571 | 아니오 | medium | 2019-04 | 예외·성과 | 원문 미열람 |
| f12 | [사실] | Feng 외(ICAPS 2024)는 실행 중 로봇이 지연될 때 경로는 유지하고 통과 순서만 다시 정하는 전환 가능 간선 탐색(Switchable-Edge Search, SES)을 제안하며, 최선 변형이 중소 규모 문제에서 1초 미만, 대규모 문제에서 기준선보다 최대 4배 빠르다고 보고한다. | ref-572 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Kalempa 외(Sensors, 2021)의 MRPF 는 작업 간 의존성, 우선순위 기반 선점(preemption) 스케줄링, 고장 복구를 함께 다루는 다중 로봇 작업 배정 방법이며, 소규모 창고 물류 실험 환경(ARENA)에서 평가되었다. | ref-573 | 아니오 | medium | 2021-09-30 | 수행 자원 | 원문 미열람 |
| f14 | [사실] | 창고 로봇 경로 계획용 다중 에이전트 롤아웃·재배열(multiagent rollout with reshuffling) 방법은 온라인 재계획으로 환경 변화에 적응하며, 일부 로봇이 고장 나는 예제로 이를 보여 준다. | ref-574 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | ISO 22301:2019(Security and resilience — Business continuity management systems — Requirements)는 교란 사건으로부터 보호하고 발생 가능성을 줄이며 복구를 보장하기 위한 업무연속성 관리 시스템(BCMS)의 수립·운영·점검·개선 요구사항을 정한다. | ref-575 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f16 | [사실] | 국내에서는 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」에 따라 행정안전부가 기업재난관리표준을 고시하고, 재해경감활동관리체계를 갖춘 기업을 문서평가·현장평가를 거쳐 재해경감 우수기업으로 인증한다. | ref-576 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [사실] | 고용노동부는 2022년 오미크론 확산기에 '중소규모 사업장 기능연속성계획(BCP) 수립 가이드'를 안내했으며, 가이드는 사업 우선순위 파악부터 위험성 분석, 피해 최소화 조치, 분야별 대응, 계획 수립·시행, 공유, 점검까지 7단계로 구성된다. | ref-577 | 아니오 | medium | 2022-03 | — | 원문 미열람 |
| f18 | [사실] | Microsoft 아키텍처 센터의 보상 트랜잭션 패턴은 실패한 여러 단계 작업에서 완료된 단계의 효과를 되돌리되 원래 상태를 그대로 복원하는 것이 아니라 업무 규칙에 맞춰 보정하며, 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하고, 영향이 큰 결정에는 사람을 참여시키라고 권한다. | ref-578 | 아니오 | medium | 2026-04-16 | 예외·성과 | — |
| f19 | [추정] | Element Logic 은 AutoStore 의 XHandler 소프트웨어 모듈이 고장 난 로봇을 넘겨받아 시스템을 멈추지 않고 오류를 처리하며, 자동 처리가 불가능하거나 로봇 충돌 위험이 있을 때만 시스템이 정지한다고 설명한다. | ref-579 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | Swisslog 은 AutoStore 그리드에서 로봇이 멈추면 자사 SynQ 소프트웨어가 멈춘 로봇 아래 보관함의 재고를 다른 보관함으로 재할당해, 멈춘 로봇을 정기 휴식이나 저수요 시간에 꺼낼 때까지 주문 처리를 계속한다고 설명한다. | ref-580 | 아니오 | low | 2025-07 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f21 | [사실] | GS1 EPCIS 저장소는 기존 이벤트를 수정·삭제하지 않는 일지(journal) 방식이며, 잘못 기록된 이벤트는 같은 eventID 에 오류 선언(errorDeclaration: 선언 시각, 사유, 정정 이벤트 id 목록)을 붙인 이벤트로 정정한다. | ref-581 | 아니오 | medium | 2016-09-29 | 완료·인계 | 원문 미열람 |
| f22 | [추정] | f1~f4·f13·f18·f21 을 종합하면 운반 중 고장 로봇의 화물과 남은 주문 처리는 고장·연결 끊김 감지(오류·연결 상태), 주문 일시정지·취소, 실린 화물 식별(loads), 남은 작업의 재배정, 화물의 물리적 회수, 재고·이벤트 기록의 보상·정정으로 이어지는 결정 흐름으로 볼 수 있을 것으로 보인다. | ref-031, ref-051, ref-573, ref-578, ref-581 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f23 | [추정] | 연계 대상: 장애물 회피·재위치 추정·비상정지 회로 같은 로봇 자체 복구·안전 제어는 제조사 몫이고, VDA 5050·Open-RMF 가 관제에 주는 기능(주문 취소·일시정지·재계획 요청·작업 수락 중지·이슈 보고)을 보면 이종 로봇을 연결하는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다. | ref-031, ref-570 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | VDA 5050 에서 연결이 끊긴 로봇이 마지막 해제 노드까지만 주행한다는 규칙(f2)을 보면, 관제가 한 번에 해제하는 주문 범위(base)의 길이가 통신 단절 동안 현장 작업이 얼마나 계속되는지를 정하는 설계 변수가 될 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-569 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-570 | Open Robotics (open-rmf/rmf_ros2) | rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 아니오 |
| ref-571 | Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N. | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019-04 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-572 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.18145 | 예 |
| ref-573 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 2021-09-30 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/1424-8220/21/19/6536 | 예 |
| ref-574 | KTH 연구진 (arXiv:2211.08201) | Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning | 2023 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2211.08201 | 예 |
| ref-575 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/75106.html | 예 |
| ref-576 | 행정안전부 | 재해경감 우수기업 인증제도 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do | 예 |
| ref-577 | 고용노동부 | 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내 | 2022-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591 | 예 |
| ref-578 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 2026-04-16 | 오픈소스 문서 | medium | 2026-09-25 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction | 아니오 |
| ref-579 | Element Logic | FAQ - Element Logic (AutoStore) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.elementlogic.net/solutions-and-services/autostore/faq/ | 예 |
| ref-580 | Swisslog | The benefits of using AutoStore for high-throughput retail fulfillment | 2025-07 | 벤더 문서 | low | 2026-09-25 | https://www.swisslog.com/en-us/case-studies-and-resources/blog/2025/07/benefits-of-autostore-htp | 예 |
| ref-581 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 예 |
| ref-582 | Open Robotics (open-rmf/rmf_ros2) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/issues/224 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f19·f20(벤더 주장 병기, 고장 로봇 하나가 전체를 멈추지 않게 하는 설계), f15·f17(업무 연속성) / 4절 용어: f1(cancelOrder), f2(연결 상태), f3(오류 수준·RETRIABLE), f18(보상 트랜잭션), f21(오류 선언), f11(ADG, 기존 용어 재사용) / 5절 시나리오: 피킹 단계 운반 중 고장 f22(시작 조건·작업 대상 f4·수행 자원 f13·완료·인계 f21·예외·성과 f1·f19·f20), 통신 단절 f2·f24 / 6절 접근법: 관제 인터페이스의 중단·취소·재계획 f1~f10, 실행 중 재계획 f11·f12·f14, 고장 허용 재배정 f13, 보상·정정 f18·f21 / 7절 표준·오픈소스: VDA 5050(f1~f6), Open-RMF(f7~f10), ISO 22301(f15), 국내 제도(f16·f17), EPCIS(f21) / 8절 연구: f11~f14 / 9절 범위: f23(로봇 자체 복구·안전 제어는 연계 대상) / 10절 연결: 12. 명령·작업 실행의 신뢰성(f1·f2·f10), 13. 작업 배정 — MRTA(f13), 15. 다중 로봇 경로·교통 관리 — MAPF(f8·f11·f12·f14), 19. 모니터링·이상 탐지·원인 분석(f3·f7 이슈 보고), 18. 사람–로봇 협업·운영 인터페이스(f5·f18 사람 개입), 7. 화물·재고·자산 식별과 추적(f4·f21, oq-003), 1. 주문·업무 시스템 연계(f18, oq-021), 11. 분산 시스템·통신·컴퓨팅 구조(f2·f24, oq-038), 22. 시뮬레이션·예측용 디지털 트윈(제한 운영 처리량 추정 질문) / 11절 열린 질문: oq-003·oq-021·oq-038·oq-048(f10 은 부분 근거일 뿐 해결 아님)과 새 질문 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 보상 트랜잭션 | Compensating Transaction | 여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다. |
| 업무연속성 관리 시스템 | Business Continuity Management System (BCMS) | 교란 사건에 대비하고 핵심 업무를 지속·복구하기 위한 조직의 관리 체계로, ISO 22301 이 요구사항을 정한다. |
| 주문 취소 즉시 동작 | cancelOrder (VDA 5050 instant action) | VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다. |

## 열린 질문

새로 생긴 질문:

- 운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 7. 화물·재고·자산 식별과 추적 | 근거: f22 | 종류: 일반
- 국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f16 | 종류: 일반
- 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 22. 시뮬레이션·예측용 디지털 트윈 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 14건
- 미확인 항목:
    - f3: 명세 본문 요약은 오류 수준을 WARNING·CRITICAL 위주로 설명하고 state 스키마는 네 값을 두어, 본문 문구와 스키마를 글자 단위로 대조하지 못함
    - f10: PR 161(SQLite 작업 백업)이 현재 배포판에 반영됐는지 미확인 — oq-048 해결 제안하지 않음
    - f11~f17·f21: 원문 미열람, 검색 요약 기준
    - ISO 22301 의 업무 영향 분석·목표 복구 시간(RTO) 요구는 제3자 해설에서만 확인되어 finding 으로 내지 않음
    - KS A ISO 22301 부합화 연도는 출처를 특정하지 못해 finding 으로 내지 않음
    - ref-574 저자 이름 미확인(KTH 연구진으로 표기)
    - f19·f20 벤더 주장, 독립 확인 없음
    - 모든 finding 교차 확인 없음
- 범위 경계 위반 의심:
    - f23: 장애물 회피·재위치 추정·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 취소·재배정·기록 정정만 맡는다고 구분
    - f16·f17: 기업 BCP 체계 전반은 전사 관리 영역이라 ROP 직접 범위가 아니며 현장 로봇 운영 계획의 참조 틀로만 제안
- 한계: 재실행(스키마 불일치) 1회차. 반려 사유 1·2(f19·f20 이 벤더 문서만 근거로 한 [사실]이고 vendor_claim 표시 없음): 직전 research.json 이 이번 입력에 포함되지 않아 형식만 고칠 원본이 없었으므로, 같은 대상에 대해 예산 안에서 브리프 전체를 다시 작성했다. 벤더 문서만 근거로 한 f19(Element Logic·AutoStore XHandler)·f20(Swisslog SynQ 재고 재할당)은 vendor_claim: true, 태그 추정, 신뢰도 low, evidence_excerpt 첫머리 '벤더 주장: '으로 냈다(관련 finding: f19, f20). 직전 브리프와 finding 번호·내용이 다를 수 있다. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031·ref-051(VDA 5050)·ref-004(rmf-core), 신규 ref-569(integration_fleets)·ref-570(RobotUpdateHandle.hpp)·ref-578(보상 트랜잭션 패턴). 그 밖의 신규 출처는 원문 미열람(신뢰도 상한 medium). web_fetch_available: false 에 따라 재사용 출처의 신뢰도도 medium 으로 적었다. 검색 20회/30, 신규 출처 14건/15(ref-569~ref-582, 예약 구간 안). 한국 자료: 행정안전부 재해경감 인증(f16), 고용노동부 BCP 가이드(f17). 국내 물류센터의 로봇 장애 수동 전환 사례는 한국어 검색 3회에서 찾지 못함(열린 질문으로 올림). 입력의 참고문헌 목록은 요약본(0건 표시)이라 기존 id 는 이전 브리프에 나온 ref-031·ref-051 과 공통 규칙의 ref-004 만 재사용했다 — 같은 URL 이 이미 있으면 퍼블리셔가 합쳐야 한다. 기존 열린 질문 oq-003·oq-021·oq-038·oq-048 은 관련 근거(f21·f18·f2·f24·f10)만 내고 해결 제안하지 않음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 열린 질문 1건으로만 연결했고 섞지 않았다. 정정 요청 없음.
```
