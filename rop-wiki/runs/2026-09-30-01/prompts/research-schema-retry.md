(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-01
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 66. 실외 (Q. 현장 유형별 적용)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-980
- 새 출처 id 구간: ref-980 ~ ref-1009 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-980 부터 순서대로 쓰고 ref-1009 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-01/target.json

```json
{
  "run_id": "2026-09-30-01",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 110,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 66,
    "area_name": "66. 실외",
    "category": "Q. 현장 유형별 적용",
    "category_letter": "Q"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=66"
}
```

### docs/categories/site-type-applications/outdoor.md

```markdown
---
title: "66. 실외"
type: area
category: "Q. 현장 유형별 적용"
area_no: 66
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 66. 실외

# 66. 실외

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]

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

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
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

### docs/categories/site-type-applications/commercial-facilities.md (요약)

```markdown
# 64. 상업 시설

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
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

### docs/categories/site-type-applications/other-sites.md (요약)

```markdown
# 67. 기타 현장

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 979건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 260개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
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
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
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
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
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
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
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
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
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
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
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
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
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
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
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
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- teleoperation: 원격 조작 (Teleoperation)
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
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [66] 에 걸린 0건 / 전체 185건)

```markdown
없음
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

### runs/2026-09-29-17/research.md

```markdown
# 리서치 브리프 2026-09-29-17

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-17 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 65. 가정·공동주택 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 매터(Matter)·실외이동로봇 운행안전인증·비전 언어 행동 모델·원격 조작 용어 없음(이동형 영상정보처리기기·로봇 친화형 건축물 인증은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 공동주택 배송(삼성물산 래미안 리더스원·현대건설·롯데글로벌로지스), 세대 내 가사 로봇(로봇청소기·LG 클로이드·1X NEO), 사생활 사고(iRobot 이미지 유출)와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 공동현관·승강기 연동 방식, 단지 집하 방식, 수령 인증, 원격 조작 보조, 가정 기기 연동 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Matter 로봇청소기 장치 유형, 개인정보 보호법 제25조의2, 개정 지능형로봇법, 이동로봇 특별법안 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — BEHAVIOR-1K, 공동주택 서비스 로봇 인식 연구, 가정 로봇 데이터 유출 탐사 보도 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
2. 국내 공동주택에서 배송로봇은 단지 입구·지하주차장·공동현관·승강기를 거쳐 세대 현관까지 어떻게 이동하며, 공동현관·승강기 연동과 수령 확인은 어떤 방식으로 구현되는가? (섹션 5·6 겨냥, 현장 유형 가정 명시, 한국 자료 우선)
3. 세대 안의 집안일(정리·청소·세탁·주방) 로봇은 제품과 연구에서 어디까지 와 있으며 무엇이 아직 어려운가? (섹션 3·5·8 겨냥)
4. 가정 로봇의 카메라·지도·원격 조작은 어떤 사생활 위험을 만들었고(유출 사고·보안 조사), 이를 막는 법·설계 수단은 무엇인가? (섹션 3·6·7 겨냥)
5. 공동주택·단지 도로를 다니는 로봇에 적용되는 국내 제도(개정 지능형로봇법 실외이동로봇 운행안전인증, 이동로봇 특별법안, 개인정보 보호법 제25조의2)는 무엇을 규정하는가? (섹션 7 겨냥)
6. 가정 기기와 로봇을 제조사와 무관하게 연결하는 스마트홈 표준(Matter)은 로봇에 대해 무엇을 정의하는가? (섹션 7 겨냥)
7. 가정·공동주택에서 ROP 가 직접 맡을 것(배송 요청 수신·이기종 배정·공동현관·승강기 예약·수령 확인·사생활 제약 반영)과 배달 앱·택배사·승강기·월패드·로봇 자체 기능·법령에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 삼성물산은 2026-01 서울 서초구 래미안 리더스원에서 뉴빌리티·요기요와 함께 단지 인근까지 운영하던 음식배달로봇 서비스를 세대 현관까지 확장했으며, 공동현관 자동문 개폐와 엘리베이터 호출 연동을 해결해 도어 투 도어로 배달하고 주문자만 음식을 꺼낼 수 있게 했다. | ref-965, ref-966, ref-979 | 예 | medium | 2026-01-15 | 가정 / 완료·인계 | — |
| f2 | [추정] | 삼성물산은 래미안 리더스원 실증 기간에 서비스를 이용한 입주민 113명의 만족도가 95%이고 서비스 필요성 공감 99%, 유료 이용 의사 74%였다고 밝혔다. | ref-965 | 아니오 | low | 2026-01-15 | 가정 / 예외·성과 | 벤더 주장 |
| f3 | [사실] | 현대건설은 모빈과 함께 공동주택 배송로봇 서비스를 추진해, 로봇이 단지 입구에서 지하주차장과 공동출입문을 지나 승강기를 타고 세대 현관까지 식음료 등을 나르게 했다(적용 예정 단지로 DH 대치 에델루이가 보도됐다). | ref-966, ref-979 | 예 | medium | 2026-09-20 | 가정 / 수행 자원 | — |
| f4 | [사실] | 미디어펜(2026-09-20)에 따르면 현대건설 배송로봇은 승강기 시스템과 연동해 자동 호출·목적층 재호출·정원 초과 여부 판단을 구현했고, 업계는 공동출입문이 열리지 않거나 승강기를 호출할 수 없으면 단지 안 운행이 끊기며 관제시스템과 충전시설도 갖춰야 한다고 본다. | ref-979 | 아니오 | medium | 2026-09-20 | 가정 / 제약 | — |
| f5 | [사실] | 롯데글로벌로지스는 로보티즈와 함께 고양·파주 아파트 단지에서 택배 배송로봇을 실증했으며(한국로봇산업진흥원 규제혁신 로봇 실증사업), 로보티즈의 자율주행로봇 '개미'는 로봇팔로 승강기 버튼을 직접 눌러 타고 내리는 시험을 마쳤다. | ref-966, ref-976 | 아니오 | medium | 2025-01-19 | 가정 / 수행 자원 | — |
| f6 | [사실] | 정보통신신문(2024-07-18)은 공동주택 로봇 택배 운영 방식을 단지 단위 중앙집하(집하장 1개소), 동 단위 분산집하(동마다 물품보관함), 구역 단위 분산집하(N개 동마다 보관함 1개소)의 세 가지로 나누고, 택배 차량이 집하처에서 송장번호를 인식시키면 관제실이 거주자와 통신하며 로봇을 통제해 배송하는 흐름을 설명한다. | ref-976 | 아니오 | medium | 2024-07-18 | 가정 / 시작 조건 | — |
| f7 | [사실] | 같은 기사는 배송로봇이 좁은 보도에서 행인과 충돌하거나 통신 장애로 급정지할 위험을 지적하고, 개인영상정보 촬영은 불특정 다수의 동의 대신 불빛·소리·안내판으로 촬영 사실을 알리고 업무 목적에 불필요한 영상은 즉시 삭제해야 한다고 적는다. | ref-976 | 아니오 | medium | 2024-07-18 | 가정 / 제약 | — |
| f8 | [사실] | 2023-09-15 시행된 개인정보 보호법 제25조의2는 업무 목적의 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영하는 것을 원칙적으로 막고, 촬영 사실을 명확히 표시했는데도 거부 의사가 없는 경우 등만 예외로 두며, 목욕실·화장실·탈의실처럼 사생활 침해 우려가 큰 장소 내부를 볼 수 있는 곳의 촬영을 금지하고, 촬영 시 불빛·소리·안내판 등으로 표시하도록 한다. | ref-978 | 아니오 | medium | 2023-09-15 | 제약 | — |
| f9 | [추정] | 제25조의2가 '업무 목적'과 '공개된 장소'를 요건으로 두므로, 단지 도로·공동현관·승강기를 다니는 공동주택 배송로봇의 촬영은 이 조항의 관리 대상이 될 가능성이 크지만, 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 촬영은 이 조항의 직접 대상이 아닐 수 있어 제조사의 영상 수집·처리는 다른 규율(동의 기반 처리 등)에 기대야 할 것으로 보인다. | ref-978, ref-976 | 아니오 | low | 2026-09-29 | 가정 / 제약 | — |
| f10 | [사실] | 2023-11-17 시행된 개정 지능형로봇법은 질량 500kg·시속 15km 이하의 배송·순찰 로봇을 실외이동로봇으로 정의하고, 운행구역 준수·횡단보도 통행 등 16개 시험항목의 운행안전인증과 보험(공제) 가입을 요구하며, 인증받은 로봇은 개정 도로교통법에 따라 보행자와 같은 지위로 보도를 다닐 수 있다. | ref-967 | 아니오 | medium | 2023-11-16 | 제약 | — |
| f11 | [사실] | 한병도 의원이 2026-09 초 대표 발의한 국토교통부 마련 '이동로봇의 안전한 이용 및 상용화 촉진을 위한 특별법안'은 건축법·국토계획법·공동주택관리법·주차장법에 흩어진 이동로봇 규제를 손질해, 시행되면 아파트가 입주자대표회의 의결로 배송·보안·순찰·청소·충전·주차로봇을 도입할 수 있게 하고 배송로봇의 공동현관 통과·엘리베이터 이용을 위한 통신 시스템 연동 절차를 간소화·표준화한다. | ref-975 | 아니오 | medium | 2026-09-27 | 가정 / 시작 조건 | — |
| f12 | [사실] | Hwang·Kim·Kwag(한국생활환경학회지 30, 2026-06)은 공동주택 거주자 63명과 업계 종사자 65명(23개 기관)을 조사해 거주자의 95.2%가 서비스 로봇 도입에 긍정적이나 실제 체험 의향은 88.9%로 차이가 있고, 자녀가 있는 가구가 단지 내 배송을 유의하게 우선시하며, 거주자는 충돌 방지·개인정보 보호·사용자 인터페이스를, 업계는 시스템 통합·운영 안정성을 더 중시한다고 보고했다. | ref-972 | 아니오 | medium | 2026-06 | 가정 / 제약 | — |
| f13 | [사실] | MIT Technology Review(2022-12-19)는 iRobot 이 개발용 Roomba J7 로 가정 내부에서 수집한 이미지가 AI 학습용 라벨링을 위해 Scale AI 를 거쳐 베네수엘라 등의 외주 작업자에게 넘어갔고, 화장실의 여성과 복도의 아이가 찍힌 사진을 포함한 스크린숏 15장이 Facebook·Discord 등에 게시됐다고 보도했다. | ref-968 | 아니오 | medium | 2022-12-19 | 가정 / 예외·성과 | — |
| f14 | [사실] | 한국소비자원과 한국인터넷진흥원(KISA)이 국내 판매 로봇청소기 6개 모델(삼성전자·LG전자 2종, 드리미·로보락·에코백스·나르왈 4종)을 40개 보안 항목으로 조사한 결과, 일부 중국 브랜드 제품에서 사용자 인증 미흡으로 외부에서 촬영 사진을 열람하거나 카메라를 강제로 켤 수 있는 취약점이 발견됐고 국산 2종은 상대적으로 양호했다. | ref-969, ref-970 | 예 | medium | 2025-10 | 가정 / 예외·성과 | — |
| f15 | [사실] | Connectivity Standards Alliance(CSA)가 2023-10-23 공개한 Matter 1.2 는 새 장치 유형 9종 가운데 하나로 로봇청소기를 넣어 원격 시작·진행 알림, 건식·습식 청소 모드, 브러시·오류·충전 상태 같은 정보를 제조사와 무관하게 다루게 했으며, 이 발표에는 지도나 구역 청소가 언급되지 않는다. | ref-977 | 아니오 | medium | 2023-10-23 | 가정 / 수행 자원 | — |
| f16 | [추정] | Matter 가 로봇청소기의 시작·상태·모드를 제조사 공통 모델로 정의하므로, 세대 안의 제조사가 다른 청소 로봇을 하나의 제어 계층에서 일정·상태 수준으로 다루는 연동 경로가 될 수 있지만, 발표 범위에는 물건 운반·조작 같은 다른 가사 로봇 능력이 없어 가사 로봇 전반의 능력 표현으로는 부족할 것으로 보인다. | ref-977 | 아니오 | low | 2026-09-29 | 가정 / 수행 자원 | — |
| f17 | [사실] | Li 외(arXiv 2403.09227, CoRL 2022 예비판)의 BEHAVIOR-1K 는 '로봇이 무엇을 해 주길 원하는가'를 묻는 설문에서 고른 일상 활동 1,000개를 집·정원·식당·사무실 50개 장면과 주석 달린 물체 9,000여 개로 OmniGibson 시뮬레이터에 구현한 벤치마크이며, 이 활동들은 길고 복잡한 조작이 필요해 최신 로봇 학습 방법에도 어렵다고 보고한다. | ref-971 | 아니오 | medium | 2024-03-14 | 가정 / 작업 대상 | — |
| f18 | [추정] | LG전자는 CES 2026 에서 7자유도 팔 두 개·다섯 손가락 손·바퀴 기반 자율주행을 갖춘 가정용 로봇 LG 클로이드(CLOiD)가 냉장고에서 우유 꺼내기, 오븐에 크루아상 넣기, 세탁 시작, 건조된 옷 개기를 시연하며, 비전 언어 모델(VLM)과 비전 언어 행동 모델(VLA)을 쓰고 ThinQ·ThinQ ON 허브로 가전 서비스를 조율한다고 발표했다. | ref-974 | 아니오 | low | 2026-01-06 | 가정 / 수행 자원 | 벤더 주장 |
| f19 | [추정] | 1X 는 2025-10-28 가정용 휴머노이드 NEO 의 사전 주문(2만 달러 또는 월 499달러, 2026년 미국 가정 배송)을 받으며, 모르는 작업은 소유자가 1X 원격 조작자를 예약해 로봇을 안내하게 하는 '전문가 모드'와 로봇이 들어가지 않는 금지 구역·얼굴 흐림 같은 사생활 기능을 내세웠다. | ref-973 | 아니오 | low | 2025-10-30 | 가정 / 수행 자원 | 벤더 주장 |
| f20 | [추정] | 확인한 자료를 종합하면 65. 가정·공동주택의 로봇 작업은 (1) 공동주택 단지 배송 — 음식·택배를 공동현관·승강기를 거쳐 세대 현관까지(f1·f3·f5·f6), (2) 세대 안 청소 — 로봇청소기(f14·f15), (3) 정리·세탁·주방 같은 조작 가사 — 연구·시연 단계(f17·f18·f19), (4) 단지 공용 서비스 — 보안·순찰·청소·충전·주차(f11)의 네 형태로 나타난다. | ref-965, ref-966, ref-979, ref-976, ref-969, ref-977, ref-971, ref-974, ref-973, ref-975 | 아니오 | low | 2026-09-29 | 가정 / 작업 대상 | — |
| f21 | [추정] | 확인한 자료를 종합하면 가정·공동주택 로봇 작업의 여섯 항목은 다음처럼 채울 수 있다. 시작 조건은 배달 앱 주문·택배 송장 인식·입주자대표회의 의결·거주자 앱 일정(f1·f6·f11·f19), 작업 대상은 음식·택배·세탁물·바닥 같은 물건·공간과 거주자 영상·개인정보(f1·f13·f17·f18), 수행 자원은 배송로봇·관제실·공동현관·승강기와 가사 로봇·원격 조작자(f4·f6·f19)다. 제약은 공동현관·승강기 연동, 보도 통행 인증, 촬영 표시·금지 구역·민감 장소 촬영 금지(f4·f8·f10·f19), 완료·인계는 주문자만 꺼낼 수 있는 수령 방식과 세대 현관 하차(f1·f5), 예외·성과는 공동출입문·승강기 실패 시 운행 중단과 영상 유출·보안 취약점(f4·f13·f14)이다. | ref-965, ref-976, ref-975, ref-973, ref-968, ref-971, ref-974, ref-979, ref-978, ref-967, ref-966, ref-969 | 아니오 | low | 2026-09-29 | 가정 | — |
| f22 | [추정] | 확인한 자료를 종합하면 65. 가정·공동주택에서 ROP 가 직접 맡을 범위는 다음과 같다. 배달 앱·택배 관제의 요청을 받아 배송·청소·순찰 로봇에 배정하고(f1·f6·f11), 공동현관·승강기를 예약·호출·재호출하며(f4), 수령 확인 결과를 돌려주고(f1), 촬영 표시·금지 구역·원격 조작 승인 같은 사생활 조건을 경로·권한 제약으로 반영한다(f8·f19). 확인한 국내 사례는 모두 건설사 한 곳과 로봇 업체 한 곳의 짝이며, 여러 제조사 로봇을 한 단지에서 묶은 공개 사례는 확인되지 않았다. | ref-965, ref-976, ref-975, ref-979, ref-978, ref-973, ref-966 | 아니오 | low | 2026-09-29 | 가정 | — |
| f23 | [추정] | 연계 대상: 이종 제조사를 잇는 ROP 는 아래 외부 영역에 작업 요청·예약·인계·상태 확인만 걸고, 메뉴·결제·택배 배차, 승강기·자동문 제어, 주행·조작 안전 성능, 법적 판단은 해당 시스템·설비 업체·로봇 제조사·관리 주체에 맡겨야 할 것으로 보인다. 분류 원문 19장 기준으로 배달 앱·택배사 시스템은 상위 업무 시스템, 공동현관 자동문·승강기 제어반·월패드는 시설·설비 제어, 로봇의 자율주행·파지·VLA 모델은 로봇 자체 지능·제어, 개인정보 보호법·지능형로봇법·공동주택관리법상 절차는 업종별 조건에 속한다. | ref-965, ref-979, ref-974, ref-978, ref-967, ref-975 | 아니오 | low | 2026-09-29 | 가정 | — |
| f24 | [추정] | 이 영역은 여러 세부영역과 이어진다. 공동현관·승강기 연동은 22. 설비·건물 시스템 연동(f1·f4·f11), 배달 앱·택배 관제는 23. 업무 시스템 연동(f1·f6), 이기종 로봇 관제는 20. 로봇·제조사 관제 연동(f22), 수령 확인은 17. 작업 대상·자산 식별과 인계 추적(f1)과 연결된다. 영상 촬영·유출은 53. 개인정보·영상 데이터(f8·f9·f13), 보안 취약점은 52. 통신 보호·위협 관리·감사(f14), 원격 조작 승인은 51. 인증·권한·격리·31. 사람–로봇 협업(f19), 금지 구역은 16. 장소 의미·지도 관리(f19), Matter 는 21. 상호운용 표준·적합성(f15·f16)과 이어진다. VLA 는 44. 로봇 기반 모델·언어 모델 계획(f18), 학습 데이터 라벨링은 47. AI·학습·적응과 모델 운영(f13), BEHAVIOR-1K 는 54. 시험·형식 검증·벤치마크(f17), 법령·특별법안은 59. 법·규제·보험·라이선스(f8·f10·f11), 거주자 수용성은 60. 노동·수용성·접근성(f12), 보도 통행은 66. 실외(f10)와 이어진다. | ref-965, ref-979, ref-975, ref-976, ref-978, ref-968, ref-969, ref-973, ref-977, ref-974, ref-971, ref-967, ref-972 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-965 | 삼성물산 뉴스룸 | 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 | 2026-01-15 | 벤더 문서 | medium | 2026-09-29 | https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/ | 아니오 |
| ref-966 | 지디넷코리아 (신영빈) | 로봇이 문앞까지 택배 가져다 주는 미래 곧 온다 | 2025-01-19 | 기사 | medium | 2026-09-29 | https://zdnet.co.kr/view/?no=20250119062609 | 아니오 |
| ref-967 | AI타임스 | 실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행 | 2023-11-16 | 기사 | medium | 2026-09-29 | https://www.aitimes.com/news/articleView.html?idxno=155217 | 아니오 |
| ref-968 | MIT Technology Review (Eileen Guo) | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 2022-12-19 | 기사 | medium | 2026-09-29 | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ | 아니오 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | 기사 | medium | 2026-09-29 | https://byline.network/2025/10/31-283/ | 아니오 |
| ref-970 | 매일신문 | 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인 | 2025-10-06 | 기사 | medium | 2026-09-29 | https://www.imaeil.com/page/view/2025100618362463025 | 아니오 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.09227 | 아니오 |
| ref-972 | Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30) | Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs | 2026-06 | 논문 | high | 2026-09-29 | https://journal.ksles.org/articles/xml/g9G5/ | 아니오 |
| ref-973 | The Robot Report (Mike Oitzman) | NEO humanoid designed for household use, available for preorder | 2025-10-30 | 기사 | medium | 2026-09-29 | https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ | 아니오 |
| ref-974 | LG Electronics USA | LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026 | 2026-01-06 | 벤더 문서 | medium | 2026-09-29 | https://www.lg.com/us/press-release/lg-cloid-home-robot | 아니오 |
| ref-975 | 한국경제 (김익환) | 배송·주차·청소까지…로봇 아파트 뜬다 | 2026-09-27 | 기사 | medium | 2026-09-29 | https://www.hankyung.com/article/2026092776141 | 아니오 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 2024-07-18 | 기사 | medium | 2026-09-29 | https://www.koit.co.kr/news/articleView.html?idxno=123976 | 아니오 |
| ref-977 | Connectivity Standards Alliance (CSA) | Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board | 2023-10-23 | 표준 | high | 2026-09-29 | https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/ | 아니오 |
| ref-978 | CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관) | 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) | 2023-03-14 | 정부·연구기관 | medium | 2026-09-29 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982 | 아니오 |
| ref-979 | 미디어펜 (조태민) | 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 | 2026-09-20 | 기사 | medium | 2026-09-29 | https://www.mediapen.com/news/view/1124680 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/home-and-apartment.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f12(거주자 95.2% 긍정·자녀 가구 단지 내 배송 선호), f13·f14(가정 로봇 영상 유출·보안 취약점이 보여 주는 사생활 위험), f11(국회 발의된 이동로봇 특별법안) / 섹션 4: f8(이동형 영상정보처리기기 — 용어집 기존), f10(실외이동로봇 운행안전인증), f15(Matter), f18(VLA), f19(원격 조작·금지 구역) / 섹션 5(현장 유형 모두 가정): 공동주택 배송 — f1(래미안 리더스원), f2(만족도, 벤더 주장), f3·f4(현대건설), f5(롯데글로벌로지스·로보티즈), f6(집하 방식); 세대 안 가사 — f14·f15(로봇청소기), f18(LG 클로이드, 벤더 주장), f19(1X NEO, 벤더 주장); 사생활 사고 — f13(iRobot); 작업 형태 지도 f20, 여섯 항목 정리 f21 / 섹션 6: 공동현관·승강기 연동 f1·f4·f5(버튼 조작 팔 대 시스템 연동), 집하 방식과 관제 흐름 f6, 수령 인증 f1, 원격 조작 보조와 사생활 기능 f19, 가전 연동 f15·f16·f18 / 섹션 7: f15·f16(Matter 1.2), f8·f9(개인정보 보호법 제25조의2), f10(개정 지능형로봇법), f11(이동로봇 특별법안, 발의 단계임을 명시) / 섹션 8: f17(BEHAVIOR-1K), f12(공동주택 서비스 로봇 인식 연구), f13(MIT Technology Review 탐사 보도) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66 / 섹션 11: open_questions_new 5건(기존 열린 질문 없음). f2·f18·f19 는 벤더 주장 병기 필수. 다음 실행 후보: 53. 개인정보·영상 데이터 페이지에 f8·f9·f13·f14 반영, 22. 설비·건물 시스템 연동 페이지에 f4·f11 반영, 59. 법·규제·보험·라이선스 페이지에 f10·f11 반영, 21. 상호운용 표준·적합성 페이지에 f15 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 매터 | Matter (Connectivity Standards Alliance smart home standard) | Connectivity Standards Alliance 가 관리하는 스마트홈 기기 상호운용 표준으로, 1.2 판(2023-10)부터 로봇청소기를 장치 유형으로 정의해 제조사가 달라도 시작·청소 모드·상태 정보를 같은 방식으로 다루게 한다. |
| 실외이동로봇 운행안전인증 | Outdoor Mobile Robot Operational Safety Certification | 2023-11-17 시행된 개정 지능형로봇법에 따라 질량 500kg·시속 15km 이하의 배송·순찰 로봇이 운행구역 준수·횡단보도 통행 등 16개 시험항목을 통과해야 받는 인증으로, 인증받은 로봇은 보도를 보행자 지위로 다닐 수 있다. |
| 비전 언어 행동 모델 | Vision-Language-Action Model (VLA) | 카메라 영상과 언어 지시를 입력으로 받아 로봇의 물리 동작을 직접 출력하도록 학습한 모델로, 가정용 로봇이 우유 꺼내기·빨래 개기 같은 조작 가사를 수행하는 데 쓰인다고 발표되고 있다. |
| 원격 조작 | Teleoperation | 사람이 떨어진 곳에서 로봇의 센서 영상을 보며 로봇을 직접 조종하는 방식으로, 가정용 로봇에서는 로봇이 스스로 못 하는 작업을 원격 조작자가 대신 수행하며 학습 데이터를 모으는 데 쓰여 사생활 통제(승인·금지 구역·얼굴 흐림)가 함께 논의된다. |

## 열린 질문

새로 생긴 질문:

- 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? | 관련 영역: 65. 가정·공동주택, 53. 개인정보·영상 데이터 | 근거: f9 | 종류: 일반
- 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? | 관련 영역: 65. 가정·공동주택, 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성 | 근거: f11 | 종류: 일반
- 한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? | 관련 영역: 65. 가정·공동주택, 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반
- 공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가? | 관련 영역: 65. 가정·공동주택, 17. 작업 대상·자산 식별과 인계 추적, 23. 업무 시스템 연동 | 근거: f1 | 종류: 일반
- 원격 조작자가 가정 로봇을 대신 조종하는 방식(1X NEO 전문가 모드 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? | 관련 영역: 65. 가정·공동주택, 53. 개인정보·영상 데이터, 58. 다사업자 책임·계약·데이터 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 3
- 예산 사용량: 검색 14회 · 신규 출처 15건
- 미확인 항목:
    - f2 삼성물산 만족도 95%(113명)·필요성 99%·유료 이용 74%는 회사 발표(벤더 주장)이며 독립 확인 없음
    - f4 현대건설 승강기 연동 기능(자동 호출·재호출·정원 초과 판단)은 미디어펜 단독
    - f5 롯데글로벌로지스 실증의 기간·규모와 개미의 실제 단지 내 버튼 조작 운영 여부 미확인
    - f6·f7 집하 방식과 영상 고지 제언은 정보통신신문 단독
    - f8 개인정보 보호법 조문은 CaseNote 게재본으로 확인했고 국가법령정보센터 원문은 열지 않음
    - f9 가정 내부 로봇 촬영에 대한 제25조의2 적용 여부는 조문 요건에서 도출한 해석이며 개인정보보호위원회 해석 미확인
    - f10 지능형로봇법 내용은 AI타임스(보도자료 기사) 단독, 법령 원문 미열람
    - f11 이동로봇 특별법안은 발의 단계이며 법안 원문·국회 의안 정보 미열람, 통과 여부 미확인
    - f14 한국소비자원·KISA 보도자료 원문(kca.go.kr·kisa.or.kr)은 인증서 오류로 열지 못함. 발표일은 매일신문 2025-10-06 보도, 바이라인은 조사기간 2025-03~07 로 적어 보도 시점과 조사 시점이 다름
    - f15 Matter 1.3 이후 판의 로봇 관련 변경(구역 청소 등) 미확인
    - f18·f19 LG 클로이드·1X NEO 기능은 회사 발표(벤더 주장)이며 출시·실사용 성능 미확인
    - 홈네트워크(월패드) 연동 사례, 가정 돌봄 로봇, 세대 내 로봇청소기 보급률 수치는 이번에 조사하지 못함
- 범위 경계 위반 의심:
    - f23: 배달 앱·택배사 시스템, 공동현관 자동문·승강기 제어반·월패드, 로봇 자율주행·파지·VLA, 개인정보 보호법·지능형로봇법·공동주택관리법 절차는 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어·업종별 조건이므로 '연계 대상: '으로 표시함
    - f18·f19: VLA·원격 조작·빨래 개기 같은 조작 능력은 로봇 자체 지능·제어이므로 이 영역에서는 가사 로봇 현황과 사생활 제약의 근거로만 제안함
    - f15·f16: Matter 는 가전 제어 표준이며 ROP 는 연동 대상으로만 다룬다. 21. 상호운용 표준·적합성과 짝으로 제안함
    - f4·f11: 공동현관·승강기 통신 연동은 22. 설비·건물 시스템 연동의 핵심이므로 이 영역에서는 공동주택 배송의 제약·사례 근거로만 제안함
    - f10: 보도 통행 규정은 66. 실외 영역과 겹치므로 단지 도로를 지나는 배송의 제약 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 14회/30, 신규 출처 15건/15(ref-965~ref-979, 예약 구간 ref-965~ref-994 안)로 출처 상한에 도달했다. 그래서 Lutz·Schöttler·Hoffmann(2019) 소셜 로봇 사생활 검토(원문 PDF 프록시 거부), 이투데이(2026-08-12) 이동로봇 특별법 설명회 기사(43개 기업 참석), 파이낸셜뉴스(2026-09-08) 현대건설–한국교통안전공단 공동주택 모빌리티 안전기준 MOU 기사, 개인정보보호위원회 로봇청소기 점검 기사는 열었거나 찾았으나 넣지 않았다. 번호 충돌 주의: 같은 날 이전 실행 2026-09-29-16 브리프가 ref-965 를 Karlsen 외 Frontiers 논문(식당 서비스 로봇)에 이미 부여했다고 적혀 있다. 이번 실행 컨텍스트가 ref-965~ref-994 를 이 실행 전용으로 예약했으므로 지시대로 ref-965 부터 썼다. 퍼블리셔가 병합할 때 ref-965 충돌을 확인해야 한다. 또 이전 브리프들은 국가기술표준원 KS 로봇 승강기 탑승 보도자료(KDI 게재)를 ref-945(2026-09-29-16)와 ref-948(2026-09-29-13)로 서로 다르게 적어, 이번에는 그 출처를 재사용하지 않았다. 원문 열람: 15건 모두 webfetch 로 본문을 열었다. 한국소비자원·KISA 보도자료는 인증서 오류로 열지 못해 기사 두 건(바이라인·매일신문)으로 교차 확인했다. 한 기사(이투데이)는 요약 모델이 없는 공동주택 조항을 만들어 내어, 원문 문장을 다시 추출해 확인한 뒤 finding 에서 뺐다. 교차 확인 3건: f1 삼성물산 세대 현관 배송 사실(뉴스룸·지디넷코리아·미디어펜), f3 현대건설 이동 경로(지디넷코리아·미디어펜), f14 로봇청소기 보안 조사(바이라인·매일신문). 신뢰도 high finding 은 없다. 벤더 주장 finding 3건(f2 삼성물산 만족도, f18 LG 클로이드, f19 1X NEO). 분류 원문 핵심 질문(가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가)에는 작업 형태 f20, 여섯 항목 f21, 직접 범위 f22, 연계 대상 f23 으로 답했다. 결론은 다음과 같은 추정이다. 공동주택 배송은 공동현관·승강기 연동과 수령 인증이 운영 성패를 가르고 제도(특별법안의 입주자대표회의 의결·연동 표준화)가 막 정비되는 중이다. 세대 안 조작 가사는 시연·사전 주문·벤치마크 단계이며, 사생활은 촬영 표시·금지 구역·원격 조작 승인·학습 데이터 처리와 기기 보안 문제로 나타난다. 현장 유형은 f8·f10·f24(일반 법령·연결)를 빼고 모두 가정이다. 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 삼성물산·지디넷코리아·AI타임스·바이라인·매일신문·한국생활환경학회지·한국경제·정보통신신문·CaseNote(개인정보 보호법)·미디어펜 열 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(BEHAVIOR-1K 는 54. 시험·형식 검증·벤치마크로만 연결). L. AI·학습 기술 관련(f13 학습 데이터 라벨링, f18 VLA)은 47·44 와 적용 대상인 이 영역 양쪽에 연결했다. 용어집에 이미 있는 이동형 영상정보처리기기·로봇 친화형 건축물 인증·승강기 어댑터는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음.
```

### runs/2026-09-29-16/research.md

```markdown
# 리서치 브리프 2026-09-29-16

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-16 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 64. 상업 시설 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 다중 운행 차량 경로 문제·로봇친화형 건축물 인증·서비스 삼자 관계 용어 없음(승강기 어댑터·플릿 어댑터·오픈 RMF·서비스형 로봇은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 호텔 객실 배송(국내 호텔·일본 호텔), 식당 서빙(국내 서빙로봇 보급·노르웨이·유럽 식당), 매장·쇼핑몰 안내·청소(쇼핑몰 안내 로봇·Sam's Club·국내 상업시설 청소로봇), 실패 사례(헨나 호텔)와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 승강기 연동 방식(버튼 조작 팔·객실 전화 연동·클라우드 API), 다층 배송 경로 계획, 테이블오더·POS 연동, 식당 도입 5단계, 반자율 원격 운영 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — KS 로봇 엘리베이터 탑승 안전 요구사항, 로봇친화형 건축물 인증, Open-RMF 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 호텔 경로 계획 논문, 호텔 관리자 인식 연구, 식당 서비스 삼자 연구, 식당 도입 사례 연구, 쇼핑몰 커뮤니케이션 로봇 현장 시험, 한국노동연구원 음식업 로봇 보고서 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
2. 호텔 객실 배송에서 로봇은 승강기를 어떻게 타고(버튼 조작·객실 전화 연동·승강기 API), 손님과 승강기를 함께 쓰는 혼잡 시간은 배송 계획에 어떤 제약을 주는가? (섹션 5·6 겨냥, 현장 유형 상업 시설 명시, 한국 자료 우선)
3. 식당 서빙로봇은 국내에 얼마나 보급됐으며, 주문 시스템(테이블오더·POS)과의 연동, 매장 구조 요건, 직원과의 역할 분담, 작업장 안전은 어떻게 나타나는가? (섹션 3·5·6 겨냥)
4. 매장·쇼핑몰의 안내·청소·재고 스캔 로봇은 어떤 방식으로 운영되며 고객이 있는 공간에서 어떤 제약과 사람 개입이 필요한가? (섹션 5·6·8 겨냥)
5. 상업 시설 로봇 도입의 실패·예외 사례와 운영자(호텔 관리자·식당 직원)의 인식은 무엇을 보여 주는가? (섹션 3·8 겨냥)
6. 상업 시설 로봇이 건물을 이동하는 데 관련된 표준·인증(KS 로봇 엘리베이터 탑승, 로봇친화형 건축물 인증)과 이기종 로봇 미들웨어(Open-RMF)는 무엇을 규정·제공하는가? (섹션 7 겨냥)
7. 상업 시설에서 ROP 가 직접 맡을 것(요청 수신·이기종 배정·승강기 예약·혼잡 시간 회피·완료 반환)과 객실 관리 시스템·POS·승강기 제어·로봇 자체 기능에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Han·Ding·Liu·Meng(Sensors, 2025-03-13)은 다층 호텔의 로봇 객실 배송을 승강기를 암묵적 경유지로 두는 다중 운행 차량 경로 문제(MTVRP)로 모델링하고 적응형 대규모 이웃 탐색(ALNS)으로 풀어, 중국 호텔(3개 층 67실) 배치 자료 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 배송 시간이 거의 두 배가 되고 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄어든다고 보고했다. | ref-103 | 아니오 | medium | 2025-03-13 | 상업 시설 / 제약 | — |
| f2 | [사실] | 같은 논문은 호텔 승강기 운행 시간이 이용 패턴에 따라 달라지므로 아침 식사·체크아웃처럼 승강기 이용이 크게 늘어나는 시간대를 배송 계획에 고려하고, 혼잡 시간에는 단방향 승강기 운행 같은 전략으로 병목을 줄일 것을 제안한다. | ref-103 | 아니오 | medium | 2025-03-13 | 상업 시설 / 제약 | — |
| f3 | [사실] | 지디넷코리아(2022-05-03)에 따르면 국내 호텔에는 로봇팔로 승강기 버튼을 직접 눌러 층간 이동하는 로보티즈 ‘집개미’(명동 헨나호텔·코트야드 메리어트 타임스퀘어), 객실 호출에 따라 순차 방문하는 LG전자 ‘클로이 서브봇’(광명 테이크호텔, 최대 15kg; 수원 바이 메리어트), 객실 전화 시스템과 연동해 호출하는 현대로보틱스·KT ‘N봇’(노보텔 앰배서더 동대문), 안내·도슨트·보안 순찰을 하는 LG전자 ‘클로이 가이드봇’(롯데월드호텔), 222nm 자외선 방역로봇(KT, 강남 안다즈호텔)이 도입됐다. | ref-952 | 아니오 | medium | 2022-05-03 | 상업 시설 / 수행 자원 | — |
| f4 | [추정] | 오티스는 자사 클라우드 기반 API 인 Otis Integrated Dispatch(OID)가 API 를 쓸 수 있는 어느 브랜드의 로봇과도 승강기 군(그룹) 단위로 연동되며, 오사카 호텔 케이한 유니버설 타워에서 2022-12 부터 AIM Technologies 의 배송 로봇이 승강기를 스스로 호출·탑승·층 선택해 24시간 객실 배송을 하고 야간에 최대 60건의 배송 요청을 처리한다고 주장한다. | ref-958 | 아니오 | low | 2026-09-29 | 상업 시설 / 수행 자원 | 벤더 주장 |
| f5 | [사실] | 서울경제(2025-04-02)에 따르면 경기 화성 동탄의 상업시설 ‘레이크 꼬모’는 라이노스의 AI 청소로봇 ‘휠리 J40’을 도입해 클라우드 기반 승강기 관리 솔루션 rEMS 로 로봇이 전 층을 스스로 오가게 했으며, 운영사 우미에스테이트(우미건설 자산관리회사)는 이를 상업 공간 운영 모델로 확대하겠다고 밝혔다. | ref-964 | 아니오 | medium | 2025-04-02 | 상업 시설 / 수행 자원 | — |
| f6 | [추정] | 확인한 자료를 종합하면 상업 시설 로봇의 승강기 이용 방식은 (1) 로봇팔로 승강기 버튼을 직접 누르는 방식(f3), (2) 제조사 클라우드 API 로 승강기를 호출하는 방식(f4, 벤더 주장), (3) 별도 승강기 관리 솔루션을 거치는 방식(f5)으로 나뉘며, 방식마다 승강기 호출 권한·손님과의 공유 규칙을 누가 정하는지가 달라진다. | ref-952, ref-958, ref-964 | 아니오 | low | 2026-09-29 | 상업 시설 / 제약 | — |
| f7 | [사실] | Retail Dive(2022-02-01)에 따르면 Sam's Club 은 미국 약 600개 매장에서 이미 운영하던 자율 바닥 청소기(Tennant 제조, Brain Corp BrainOS 기반)에 재고 스캔 타워를 달아 바닥 청소와 재고 스캔을 한 로봇으로 수행하게 했고, 로봇이 모은 가격 정확도·재고 수준·상품 진열 위치 정보를 매장 관리자에게 전달한다. | ref-953 | 아니오 | medium | 2022-02-01 | 상업 시설 / 작업 대상 | — |
| f8 | [사실] | Kanda·Shiomi·Miyashita·Ishiguro·Hagita(IEEE Transactions on Robotics 26(5), 2010)는 쇼핑몰에서 쇼핑 정보 제공·길 안내·친밀감 형성을 하는 커뮤니케이션 로봇을 개발해 25일간 현장 시험으로 2,642회의 상호작용을 모았으며, 소음 속 음성 인식과 예상치 못한 지식 요구를 풀기 위해 바닥 센서·RFID 로 사람을 감지·식별하고 일부를 원격 조작자가 맡는 네트워크 로봇 시스템(반자율) 방식을 택했다. | ref-954 | 아니오 | medium | 2010-10 | 상업 시설 / 수행 자원 | 원문 미열람 |
| f9 | [사실] | Ivanov·Seyitoğlu·Markova(Information Technology & Tourism, 2020)는 불가리아 호텔 관리자(설문 79명, 면접 20명)를 조사해 관리자들이 공용 공간 청소·세탁물 배송·결제 처리 같은 반복적이고 지저분한 업무를 로봇에 맞는 일로 보는 반면 손님 감정 이해·프로그램 밖 특별 요청 처리 능력은 낮게 평가하며, 응답자 약 63%가 로봇 도입 의향이 없고 1년 안 도입 계획은 3.8%이며 비용·시설 개조·유지보수·서비스 품질 저하를 장벽으로 든다고 보고했다. | ref-955 | 아니오 | medium | 2020-09 | 상업 시설 / 예외·성과 | — |
| f10 | [사실] | 지디넷코리아(2024-07-30)에 따르면 국내 서빙로봇 업체 브이디컴퍼니는 2023년 말까지 약 3,000개 업장에 5,000대, 우아한형제들 자회사 비로보틱스는 2024년 3월 말 기준 약 2,000개 업장에 3,100대를 공급했으며, 서빙로봇은 식당을 넘어 스크린골프장·야구장·당구장·인쇄소·문화공간과 물류센터·중소형 공장으로 쓰임이 넓어지고 있다. | ref-956 | 아니오 | medium | 2024-07-30 | 상업 시설 / 수행 자원 | — |
| f11 | [추정] | 브이디컴퍼니는 2023-03-30 신제품 발표에서 손님이 테이블의 태블릿으로 주류·음료를 주문하면 주문 정보가 음료냉장고로 전달되고 서빙로봇이 자동으로 받아 테이블로 나르는 ‘브이디셜틀’과 레이저로 이동 경로를 바닥에 표시하는 ‘스위프트봇’을 내놓으며 2019~2022년 누적 3,000대를 공급했다고 밝혔다. | ref-959 | 아니오 | low | 2023-03-30 | 상업 시설 / 시작 조건 | 벤더 주장 |
| f12 | [사실] | Karlsen 외(NTNU·Nord University, Frontiers in Robotics and AI, 2026-04-22)는 노르웨이 식당 서비스 로봇 도입 사례(면접 22회·참여자 34명·관찰)를 분석해, 도입 동기가 인력 부족·직원 건강·안전·비용이고, 계단·문턱 같은 건축 장애물이 없는 넓은 배치가 필요해 신축 단계 반영이 개조 비용을 줄이며, 통합 과정은 시설 평가 → 수동 주행으로 공간 지도 작성 → 디지털 지도에 정차점·경로 지정 → 직원 관찰을 받는 며칠간의 시험 → 맞춤 설정의 5단계로 진행됐다고 보고했다. | ref-965 | 아니오 | medium | 2026-04-22 | 상업 시설 / 제약 | — |
| f13 | [사실] | 같은 연구는 서빙로봇이 피크 시간과 예약 없는 대규모 테이블에서 가장 쓸모 있고 주방 가까운 구역에서는 직원이 직접 나르는 편이 빨랐으며, 20인 테이블 기준 직원 왕복을 10회에서 2회로 줄여 약 320m 보행과 35.2kg 운반을 덜었다고 평가하고, 로봇의 이동·배치 결정에는 홀 직원이 참여해야 한다고 결론지었다. | ref-965 | 아니오 | medium | 2026-04-22 | 상업 시설 / 예외·성과 | — |
| f14 | [사실] | Odekerken-Schröder·Mennens·Steins·Mahr(Journal of Service Management 33(2), 2022)는 코로나19 시기 유럽의 패스트 캐주얼 아시아 음식점에서 음료·요리를 나르는 휴머노이드 서비스 로봇 2대를 대상으로 현장 고객 108명과 실험 참가자 361명을 조사해, 로봇의 낮은 기능적 가치를 일선 직원의 높은 응대 품질이 보완할 수 있고(보완) 기능이 뛰어난 로봇은 직원 지원 의존을 줄인다(대체)는 서비스 삼자 관계 결과를 보고했다. | ref-961 | 아니오 | medium | 2022 | 상업 시설 / 수행 자원 | — |
| f15 | [사실] | 한국노동연구원 박수민 외(2024)의 음식업 서비스 로봇 연구는 키오스크·태블릿 주문과 서빙로봇 전달로 운영되는 음식점에서 로봇 도입에 따른 작업 동선 변화가 사람과 사물의 충돌 위험을 만들고 로봇 설치·운행에 알맞은 물리적 공간이 필요하며, 조사 사업장에서 비상정지 버튼 활용 교육과 로봇 청소 시 안전이 미흡해 정기 교육이 병행돼야 한다고 보고한다. | ref-960 | 아니오 | medium | 2024 | 상업 시설 / 제약 | 원문 미열람 |
| f16 | [사실] | 2015년 나가사키 하우스텐보스에 문을 연 일본 헨나 호텔은 2019년 1월 로봇 243대 가운데 절반 이상을 줄였는데, 객실 음성 비서 로봇이 기본 질문에 답하지 못하거나 코 고는 소리를 명령으로 오인해 손님을 깨웠고, 짐 운반 로봇과 프런트 로봇이 여권 복사 같은 업무를 해내지 못해 사람 직원이 계속 개입해야 했다. | ref-962, ref-963 | 예 | medium | 2019-01 | 상업 시설 / 예외·성과 | — |
| f17 | [사실] | 지디넷코리아(2022-04-11)에 따르면 스마트도시협회는 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스의 4개 부문 25개 지표로 최우수·우수·일반 등급을 매기는 민간 ‘로봇 친화형 건축물 인증’을 시행해 첫 대상인 네이버 제2사옥(1784)에 2022-04-06 현장 실사를 거쳐 최우수 등급을 주었고, 평가위원은 이동형 서비스 로봇의 승강기 이동 지원과 로봇용 정밀지도·측위 인프라를 평가했다. | ref-957 | 아니오 | medium | 2022-04-11 | 기타 / 제약 | — |
| f18 | [사실] | 산업통상자원부 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항과 실내 배송 로봇에 관한 국가표준(KS) 제정을 발표했으며, 건물 안을 이동하는 로봇이 사람과 안전하게 접촉하도록 속도 제어·위험 상황의 보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지를 다룬다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | — |
| f19 | [추정] | Open-RMF 코어는 서로 다른 제조사 플릿을 제어 수준별로 붙이는 플릿 어댑터, 교통 일정 데이터베이스와 충돌 협상, 작업 배정, 문·승강기·디스펜서 같은 건물 설비의 표준 인터페이스를 제공하므로 제조사가 다른 배송·청소·안내 로봇이 승강기를 함께 쓰는 호텔·쇼핑몰의 참고 구조가 될 수 있으나, 이번 조사에서 호텔·식당·쇼핑몰의 Open-RMF 적용 사례는 확인하지 못했다. | ref-004 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 상업 시설의 로봇 작업은 (1) 호텔 객실 배송 — 비품·음식을 층간 이동해 객실로(f1·f3·f4), (2) 식당 서빙·음료 전달 — 주방·음료냉장고에서 테이블로(f10·f11·f12·f13·f14), (3) 매장·쇼핑몰·호텔 안내 — 쇼핑 정보·길 안내·도슨트(f3·f8), (4) 청소·방역과 재고 스캔 — 바닥·공용 공간과 선반 정보(f3·f5·f7), (5) 프런트·객실 응대 — 체크인·객실 음성 비서(f16, 실패 사례)의 다섯 형태로 나타난다. | ref-103, ref-952, ref-958, ref-956, ref-959, ref-965, ref-961, ref-954, ref-964, ref-953, ref-962 | 아니오 | low | 2026-09-29 | 상업 시설 / 작업 대상 | — |
| f21 | [추정] | 확인한 자료를 종합하면 상업 시설 로봇 작업의 여섯 항목은 시작 조건이 객실 호출·객실 전화·테이블 태블릿 주문(f3·f11), 작업 대상이 비품·음식·음료·바닥·선반 정보·안내받는 손님(f20), 수행 자원이 배송·서빙·청소·안내 로봇과 음식을 싣고 예외를 처리하는 직원·원격 조작자(f8·f13·f14), 제약이 손님과 함께 쓰는 승강기와 아침 식사·체크아웃 같은 혼잡 시간(f1·f2), 계단·문턱 없는 넓은 동선과 사람과의 충돌 위험(f12·f15), 승강기 탑승 안전 요구(f18), 예외·성과가 로봇 실패 시 직원 개입 부담과 보행·운반 감소 같은 지표(f13·f16)로 채워질 수 있으나, 완료·인계(손님 수령·테이블 전달 확인) 방식은 이번 자료에서 명시적으로 확인되지 않았다. | ref-952, ref-959, ref-954, ref-965, ref-961, ref-103, ref-960, ref-945, ref-962 | 아니오 | low | 2026-09-29 | 상업 시설 | — |
| f22 | [추정] | 확인한 자료를 종합하면 64. 상업 시설에서 ROP 가 직접 맡을 범위는 객실 호출·테이블 주문·청소 일정 같은 요청을 받아 제조사가 다른 배송·서빙·청소·안내 로봇에 배정하고(f3·f10·f11), 손님과 함께 쓰는 승강기를 예약하며 아침 식사·체크아웃 같은 혼잡 시간을 배송·청소 일정의 제약으로 반영하고(f1·f2·f6), 로봇이 처리하지 못하는 요청을 직원·원격 조작자에게 넘기며(f8·f14·f16), 완료와 재고 스캔 같은 수집 정보를 업무 시스템에 돌려주는 일(f7)이고, 이를 이기종 로봇에 걸쳐 하나의 계층으로 묶은 상업 시설 공개 사례는 확인되지 않았다. | ref-952, ref-956, ref-959, ref-103, ref-958, ref-964, ref-954, ref-961, ref-962, ref-953 | 아니오 | low | 2026-09-29 | 상업 시설 | — |
| f23 | [추정] | 연계 대상: 호텔 객실 관리 시스템·식당 POS·테이블오더·소매 재고 시스템은 분류 원문 19장의 상위 업무 시스템, 승강기 제어반과 제조사 승강기 API·승강기 관리 솔루션은 시설·설비 제어, 로봇의 자율 주행·장애물 회피·음성 인식은 로봇 자체 지능·제어, 식품 위생·숙박 손님 개인정보 같은 업종 규정은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 메뉴·결제·재고 판단, 승강기 제어, 주행 안전 성능은 해당 시스템·승강기 업체·로봇 제조사에 맡겨야 할 것으로 보인다. | ref-959, ref-953, ref-958, ref-964, ref-952, ref-954 | 아니오 | low | 2026-09-29 | 상업 시설 | — |
| f24 | [추정] | 이 영역은 승강기 연동을 다루는 22. 설비·건물 시스템 연동(f4·f5·f6·f17·f18), 객실 관리 시스템·POS·테이블오더·재고 시스템을 다루는 23. 업무 시스템 연동(f7·f11), 이기종 로봇과 Open-RMF 를 다루는 20. 로봇·제조사 관제 연동(f19), 승강기를 공용 자원으로 다루는 28. 공용 자원·충전·에너지 최적화와 혼잡 시간 일정을 다루는 26. 작업 순서·스케줄링(f1·f2), 로봇 대수 한계 이익을 다루는 35. 처리능력·규모·배치 설계(f1), 쇼핑몰 보행자와 충돌을 다루는 19. 사람·보행자 모델·49. 사람 근접 안전(f8·f15), 직원과 로봇의 분담을 다루는 31. 사람–로봇 협업(f13·f14), 직원 인식·일자리 우려를 다루는 60. 노동·수용성·접근성(f9·f12·f15), 매장 지도 작성·시험 운행을 다루는 55. 현장 조사·설치·시운전(f12), 실패 사례와 직원 개입을 다루는 32. 예외 복구·재계획·업무 연속성(f16), 음성 비서 실패를 다루는 13. 대화형 기능의 신뢰·기반(f16), 보급 현황을 다루는 1. 기술·시장·업체 동향(f10), 도입 비용을 다루는 3. 경제성·조달·사업 모델(f9·f12)에 이어진다. | ref-958, ref-964, ref-957, ref-945, ref-953, ref-959, ref-004, ref-103, ref-954, ref-960, ref-965, ref-961, ref-955, ref-962, ref-956 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-103 | Han, L., Ding, J., Liu, S., & Meng, M. (Sensors) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 2025-03-13 | 논문 | high | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-952 | 지디넷코리아 (윤상은) | 엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇 | 2022-05-03 | 기사 | medium | 2026-09-29 | https://zdnet.co.kr/view/?no=20220503124850 | 아니오 |
| ref-953 | Retail Dive (Sam Silverstein) | Sam's Club rolls out inventory-checking robots chainwide | 2022-02-01 | 기사 | medium | 2026-09-29 | https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/ | 아니오 |
| ref-954 | Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)) | A Communication Robot in a Shopping Mall | 2010-10 | 논문 | medium | 2026-09-29 | https://ieeexplore.ieee.org/abstract/document/5557825 | 예 |
| ref-955 | Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism) | Hotel managers' perceptions towards the use of robots: a mixed-methods approach | 2020-09 | 논문 | high | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/ | 아니오 |
| ref-956 | 지디넷코리아 (신영빈) | 식당 음식 나르던 서빙로봇, 공장·창고로 진격 | 2024-07-30 | 기사 | medium | 2026-09-29 | https://zdnet.co.kr/view/?no=20240730115912 | 아니오 |
| ref-957 | 지디넷코리아 (김성현) | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 2022-04-11 | 기사 | medium | 2026-09-29 | https://zdnet.co.kr/view/?no=20220411142336 | 아니오 |
| ref-958 | Otis Elevator Company | Elevators and service robots | 미확인 | 벤더 문서 | low | 2026-09-29 | https://www.otis.com/en/us/innovation/elevators-and-service-robots | 아니오 |
| ref-959 | 이투데이 (구예지) | 브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것” | 2023-03-30 | 기사 | medium | 2026-09-29 | https://www.etoday.co.kr/news/view/2235962 | 아니오 |
| ref-960 | 한국노동연구원 (박수민 외) | 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 | 2024 | 정부·연구기관 | medium | 2026-09-29 | https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf | 예 |
| ref-961 | Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)) | The service triad: an empirical study of service robots, customers and frontline employees | 2022 | 논문 | medium | 2026-09-29 | https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service | 아니오 |
| ref-962 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 미확인 | 기사 | medium | 2026-09-29 | https://incidentdatabase.ai/cite/346/ | 아니오 |
| ref-963 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 2019-01 | 기사 | low | 2026-09-29 | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ | 아니오 |
| ref-964 | 서울경제 (백주연) | 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장 | 2025-04-02 | 기사 | medium | 2026-09-29 | https://www.sedaily.com/article/14048085 | 아니오 |
| ref-965 | Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI) | Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation | 2026-04-22 | 논문 | high | 2026-09-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full | 아니오 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | high | 2026-09-29 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/commercial-facilities.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f10(국내 서빙로봇 보급 약 8,000대 규모와 다른 업종 확장), f12(인력 부족·직원 건강이 도입 동기), f9·f16(관리자 인식과 대규모 실패 사례가 보여 주는 운영 난도) / 섹션 4: f1(다중 운행 차량 경로 문제), f17(로봇친화형 건축물 인증), f14(서비스 삼자 관계), f8(반자율 네트워크 로봇 시스템) / 섹션 5(현장 유형은 f17 을 빼고 모두 상업 시설): 호텔 객실 배송 — f3(국내 호텔 5곳 이상), f4(오사카 호텔, 벤더 주장), f1·f2(중국 호텔 자료 경로 계획); 식당 서빙 — f10·f11(국내 보급·테이블오더 연동, f11 은 벤더 주장), f12·f13(노르웨이 식당), f14(유럽 식당), f15(국내 음식업 안전); 매장·쇼핑몰 안내·청소 — f8(쇼핑몰 안내 로봇), f7(Sam's Club 청소·재고 스캔), f5(레이크 꼬모 청소로봇); 실패 사례 — f16(헨나 호텔); 작업 형태 지도 f20, 여섯 항목 정리 f21(완료·인계 칸은 근거 부족) / 섹션 6: 승강기 이용 방식 f6(f3·f4·f5), 혼잡 시간 반영 경로 계획 f1·f2, 주문 시스템 연동 f11, 식당 도입 5단계 f12, 직원 역할 분담 f13·f14, 반자율 원격 운영 f8 / 섹션 7: f18(KS 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇, ref-945 재사용), f17(로봇친화형 건축물 인증, 오피스 사례임을 명시), f19(Open-RMF, ref-004 재사용, 상업 시설 적용 사례 미확인) / 섹션 8: f1(호텔 경로 계획), f9(호텔 관리자 인식), f14(식당 서비스 삼자), f12·f13(식당 도입 사례 연구), f8(쇼핑몰 현장 시험), f15(한국노동연구원 보고서, 원문 미열람) / 섹션 9: f22(직접 범위: 요청 수신·이기종 배정·승강기 예약·혼잡 시간 반영·직원 인계·결과 반환), f23(연계 대상: 객실 관리 시스템·POS·테이블오더·재고 시스템, 승강기 제어, 로봇 자체 주행·음성 인식, 업종 규정) / 섹션 10: f24 — 1. 기술·시장·업체 동향, 3. 경제성·조달·사업 모델, 13. 대화형 기능의 신뢰·기반, 19. 사람·보행자 모델, 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전, 55. 현장 조사·설치·시운전, 60. 노동·수용성·접근성 / 섹션 11: open_questions_new 5건(기존 열린 질문 없음). f4·f11 은 벤더 주장 병기 필수. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f6·f17 반영, 23. 업무 시스템 연동 페이지에 f7·f11 반영, 60. 노동·수용성·접근성 페이지에 f9·f15·f16 반영, 31. 사람–로봇 협업 페이지에 f13·f14 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 다중 운행 차량 경로 문제 | Multi-Trip Vehicle Routing Problem (MTVRP) | 적재 용량이 정해진 차량(로봇)이 한 거점에서 여러 번 출발·복귀하며 여러 목적지를 도는 경로를 정하는 차량 경로 문제의 변형으로, 다층 호텔의 로봇 객실 배송 계획에 승강기를 경유지로 넣어 쓰였다. |
| 로봇친화형 건축물 인증 | Robot-Friendly Building Certification | 스마트도시협회가 2022년 시작한 민간 인증으로, 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스 4개 부문 25개 지표로 건물이 로봇의 승강기 이동과 측위 등을 얼마나 지원하는지를 최우수·우수·일반 등급으로 평가한다. |
| 서비스 삼자 관계 | Service Triad (service robot, customer, frontline employee) | 서비스 로봇·고객·일선 직원 세 주체의 상호작용으로 서비스 가치를 설명하는 틀로, 로봇이 직원을 보완하는지 대체하는지와 직원 응대가 로봇의 기능 부족을 메우는지를 분석한다. |

## 열린 질문

새로 생긴 질문:

- 호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? | 관련 영역: 64. 상업 시설, 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동 | 근거: f19 | 종류: 일반
- 호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가? | 관련 영역: 64. 상업 시설, 23. 업무 시스템 연동 | 근거: f3 | 종류: 일반
- 영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가? | 관련 영역: 64. 상업 시설, 26. 작업 순서·스케줄링 | 근거: f7 | 종류: 일반
- 로봇친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가, 그리고 2025년 도입이 예고된 스마트+빌딩 인증과 어떤 관계인가? | 관련 영역: 64. 상업 시설, 22. 설비·건물 시스템 연동 | 근거: f17 | 종류: 일반
- 식당 서빙로봇과 호텔 배송 로봇은 손님이 음식·물품을 받았는지(완료·인계)를 어떤 방식(무게 감지·버튼·직원 확인·객실 문 앞 알림)으로 확인하며 그 결과가 주문 시스템에 기록되는가? | 관련 영역: 64. 상업 시설, 17. 작업 대상·자산 식별과 인계 추적 | 근거: f21 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 23회 · 신규 출처 15건
- 미확인 항목:
    - f1·f2 호텔 경로 계획 수치(승강기 시간 40→100초에서 배송 시간 약 2배, 로봇 5대 이상 한계 이익 감소)는 단일 논문·단일 호텔 자료이며 교차 확인 실패
    - f3 국내 호텔 로봇 도입 목록은 지디넷코리아 한 건이며 현재 운영 여부 미확인
    - f4 오티스 OID 호환 범위와 오사카 호텔 야간 60건 처리는 벤더 문서 단독(벤더 주장)
    - f5 레이크 꼬모 청소로봇의 운영 시간대와 rEMS 연동 성능은 기사에 없음
    - f7 Sam's Club 로봇의 운영 시간대(영업 중·후)와 생산성 수치 미확인
    - f8 Kanda 외 2010 논문은 출판사(ACM·IEEE·ResearchGate 403, ADS 405)와 Semantic Scholar 초록 비공개로 초록 원문을 열지 못해 검색 결과 요약만 확인
    - f10 서빙로봇 보급 대수는 업체가 밝힌 값을 기사가 옮긴 것이며 독립 집계 없음
    - f11 브이디컴퍼니 연동 방식·시장 규모는 회사 발표(벤더 주장)
    - f12·f13 노르웨이 식당 수치(320m·35.2kg)는 단일 사례 연구의 계산값
    - f15 한국노동연구원 보고서 원문·노동리뷰 원고(repository.kli.re.kr 403)를 열지 못해 검색 결과 요약 범위만 사용, 서빙로봇 단독 수치 미확인
    - f16 헨나 호텔 두 출처는 모두 2019년 언론 보도를 바탕으로 한 2차 자료이며 1차 보도(월스트리트저널 등)는 열지 않음
    - f17 로봇친화형 건축물 인증의 상업 시설 적용 사례와 이후 제도 변화 미확인
    - f18 KS 표준 번호·정식 명칭 미확인
    - f19 호텔·식당·쇼핑몰의 Open-RMF 적용 사례 미확인(싱가포르 Mapletree Business City 사례는 오피스·비즈니스 파크이고 IMDA 보도자료 본문이 로드되지 않아 제외)
    - f21 완료·인계 항목(손님 수령 확인 방식)은 근거 자료를 찾지 못함
- 범위 경계 위반 의심:
    - f23: 객실 관리 시스템·POS·테이블오더·재고 시스템의 메뉴·결제·재고 판단, 승강기 제어반·제조사 승강기 API·승강기 관리 솔루션의 제어, 로봇의 자율 주행·장애물 회피·음성 인식, 식품 위생·숙박 개인정보 규정은 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어·업종별 조건 쪽이므로 '연계 대상: '으로 표시함
    - f4·f5·f6: 승강기 연동 방식은 22. 설비·건물 시스템 연동 의 핵심이므로 이 영역에서는 상업 시설 로봇 운영의 제약·사례 근거로만 제안함
    - f7·f11: 재고 스캔 정보 전달과 테이블오더 연동은 23. 업무 시스템 연동 의 방법이므로 이 영역에서는 시작 조건·작업 대상의 근거로만 제안함
    - f8·f16: 음성 인식·객실 음성 비서 실패는 로봇 자체 기능과 13. 대화형 기능의 신뢰·기반 쪽이므로 이 영역에서는 사람 개입이 필요한 예외 사례로만 제안함
    - f17: 로봇친화형 건축물 인증의 첫 사례는 오피스(현장 유형 기타)이므로 site_type 을 기타로 두고 상업 시설 사례로 쓰지 않도록 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 23회/30, 신규 출처 15건/15(ref-103~ref-965, 이 실행 전용 예약 구간 ref-103~ref-980 안) 상한 도달로 arXiv 2412.10699(상업용 실내 배송 로봇 40종 사이버·물리 보안 분석, 초록만 확인), Shiomi 외 쇼핑몰 보행자 회피 연구(Semantic Scholar 429·ResearchGate 403), Retail/상업 시설 청소로봇 벤더 블로그, 싱가포르 IMDA Mapletree Business City RMF 보도자료(본문 로드 실패, 오피스)는 넣지 않았다. 주의: 같은 날 이전 실행 2026-09-29-13 브리프가 ref-103(비즈한국)·ref-952(품질경영학회지 논문)·ref-953(한국보건산업진흥원)을 다른 URL 에 부여했다고 적혀 있으나, 이번 실행 컨텍스트가 ref-103~ref-980 을 이 실행 전용으로 예약했으므로 그 지시를 따랐다 — 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 한다. 원문 열람: 신규 13건 webfetch(PMC 원문 2, Frontiers 원문 1, Emerald 초록 1, 기사 7, 오티스 페이지 1, AI Incident Database 1), 미열람 2건(ref-954 Kanda 외 초록 비공개, ref-960 한국노동연구원 403). ref-956 은 원 URL 이 연결 재설정으로 끊겨 다음 뉴스 게재본으로 열었다. 재사용 2건(ref-945 은 KDI 게재 원문을, ref-004 는 공식 저장소 raw 원문을 이번에 다시 열었다; 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 두 항목의 기관·제목은 직전 브리프 2026-09-29-13·12 의 표를 따랐다). 교차 확인 1건(f16 헨나 호텔 — AI Incident Database 와 Hotel Technology News, 둘 다 언론 보도 기반 2차 자료라 신뢰도 medium). 신뢰도 high finding 없음. 벤더 주장 finding 2건(f4 오티스, f11 브이디컴퍼니). 분류 원문 핵심 질문(손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가)에는 작업 형태 지도 f20, 여섯 항목 정리 f21, 직접 범위 f22, 연계 대상 f23 으로 답했으며 결론은 '영업 시간 운영의 핵심 제약은 손님과 함께 쓰는 승강기·동선의 혼잡 시간과 사람과의 충돌이고(f1·f2·f12·f15), 로봇은 피크 시간 운반 보조로 가치가 크되 로봇이 못 하는 요청은 직원·원격 조작자가 넘겨받는 혼합 운영이 전제이며(f8·f13·f14·f16), 이기종 로봇을 한 계층으로 묶은 상업 시설 공개 사례는 확인되지 않았다'는 추정이다. 현장 유형: f17(오피스, 기타)을 빼고 모두 상업 시설(호텔: 국내 여러 호텔·오사카·중국·불가리아·일본 헨나 / 식당: 국내 서빙로봇·노르웨이·유럽 / 매장·쇼핑몰: 미국 Sam's Club·일본 쇼핑몰·화성 레이크 꼬모)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 지디넷코리아 3건(f3·f10·f17)·이투데이(f11)·서울경제(f5)·한국노동연구원(f15)·국가기술표준원(f18, 재사용) 일곱 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다(f1 의 경로 계획은 26·35 쪽으로만 연결). 용어집에 이미 있는 승강기 어댑터·플릿 어댑터·오픈 RMF·서비스형 로봇·다중 플릿 오케스트레이션은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음.
```


## 스키마 불일치 (재실행)

직전 반환값이 JSON 스키마(schemas/research.schema.json)와 맞지 않아 퍼블리셔가 반려했다. 아래 오류를 모두 고친, 스키마에 맞는 JSON 객체 하나만 다시 반환한다. 내용을 새로 조사하지 말고 형식만 고친다.

- finding f11: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
