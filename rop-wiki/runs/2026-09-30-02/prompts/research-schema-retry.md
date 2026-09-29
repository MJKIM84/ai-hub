(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-02
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 67. 기타 현장 (Q. 현장 유형별 적용)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-995
- 새 출처 id 구간: ref-995 ~ ref-1024 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-995 부터 순서대로 쓰고 ref-1024 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-02/target.json

```json
{
  "run_id": "2026-09-30-02",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 111,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 67,
    "area_name": "67. 기타 현장",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=67"
}
```

### docs/categories/site-type-applications/other-sites.md

```markdown
---
title: "67. 기타 현장"
type: area
category: "Q. 현장 유형별 적용"
area_no: 67
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 67. 기타 현장

# 67. 기타 현장

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]

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

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 994건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 264개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
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

### docs/open-questions.md (요약: 대상 영역 [67] 에 걸린 0건 / 전체 190건)

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

### runs/2026-09-30-01/research.md

```markdown
# 리서치 브리프 2026-09-30-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-01 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 66. 실외 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 공공 영역 이동로봇(PMR)·개인 배송 장치(PDD)·원격 조작형 소형차·실시간 이동 측위(RTK)·침범 후 시간(PET) 용어 없음(실외이동로봇 운행안전인증·원격 조작은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 보도 배송(배민 딜리), 순찰(뉴빌리티 뉴비), 캠퍼스 배송(Starship·NAU), 접근성 사고(피츠버그), 눈 속 고립(탈린)과 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 위성 위치·센서 융합, 불확실성을 고려한 경로 계획, 날씨·사람 도움에 기대는 예외 처리 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법 운행안전인증, 도로교통법 보행자 지위, 일본 원격 조작형 소형차, 미국 주 PDD 법, ISO 4448 시리즈, Nav2 GPS 항법 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 보도 로봇–보행자 상충 관측 연구, 눈 속 로봇 연구, 강건 경로 계획 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
2. 국내에서 실외 로봇이 보도를 다니려면 어떤 법적 요건(지능형로봇법 운행안전인증, 도로교통법상 보행자 지위, 보험)을 갖춰야 하며 그 기준은 어떻게 바뀌어 왔는가? (섹션 3·7 겨냥, 한국 자료 우선)
3. 일본·미국 등 다른 나라는 보도 주행 로봇의 크기·속도·신고를 어떻게 규정하고, 관할마다 다른 규정은 운영에 어떤 제약을 주는가? (섹션 7·9 겨냥)
4. 실외 배송·순찰·캠퍼스 운영의 실제 사례(국내외)는 어떤 작업을 어디서 어떻게 하고 있으며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥, 현장 유형 실외 명시)
5. 눈·비 같은 날씨와 보행자·장애물은 실외 로봇의 운행·경로·예외 처리에 어떤 영향을 주며 이를 다루는 방법은 무엇인가? (섹션 6·8 겨냥)
6. 실외 로봇의 위치 추정(위성 위치·RTK·센서 융합)은 어떤 한계가 있고, 공공 영역 이동로봇 표준(ISO 4448 등)은 무엇을 다루는가? (섹션 6·7 겨냥)
7. 실외에서 ROP 가 직접 맡을 것(요청 수신·배정·관할별 규정과 날씨를 경로·속도 제약으로 반영·예외 인계)과 로봇 자체 주행·위치 추정·배달 앱·법적 인증에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 따른 의무인증으로, 최대 속도 15km/h·최대 질량 500kg 이하의 배송 등 자율주행(원격제어 포함) 로봇과 관제장치의 조합을 대상으로 하며, 현재 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개 항목을 심사하고 신청일로부터 30일 이내에 처리한다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f2 | [사실] | 개정 지능형로봇법과 도로교통법은 2023-11-17 시행됐으며, 질량 500kg·시속 15km 이하 실외이동로봇은 16가지 시험항목의 운행안전인증을 받아야 보도를 다닐 수 있게 됐다. | ref-991, ref-992 | 예 | high | 2023-11-16 | 실외 / 제약 | — |
| f3 | [사실] | 정책브리핑에 따르면 개정 도로교통법은 운행안전인증을 받은 실외이동로봇에 보행자 지위를 주어 보도 통행을 허용하되 신호위반·무단횡단 금지 등 보행자 의무를 지키게 하고 위반 시 운용자에게 범칙금 3만 원을 부과하며, 보도에서 운영하려는 자에게 보험 또는 공제 가입 의무를 지우고 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다. | ref-991 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f4 | [사실] | 지디넷코리아(2023-07-28)가 전한 운행안전 기준안은 질량에 따라 최고 속도를 230kg 초과 5km/h, 100kg 초과~230kg 10km/h, 100kg 이하 15km/h로 나누고, 로봇 폭은 기본 80cm·보도 폭 250cm 이상이면 최대 120cm로 하며, 보험 보장액을 사망·후유장애 1억 5천만 원, 부상 3천만 원, 재물 피해 사고당 10억 원으로 정했다. | ref-992 | 아니오 | medium | 2023-07-28 | 실외 / 제약 | — |
| f5 | [추정] | 2023년 시행 당시 16개였던 운행안전인증 시험항목이 현재 한국로봇산업진흥원 안내에는 8개 심사항목으로 적혀 있어 심사항목이 통폐합된 것으로 보이나, 개정 시점·근거 고시와 세부 기준이 완화됐는지는 이번 조사에서 원문으로 확인하지 못했다. | ref-991, ref-980 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f6 | [사실] | 일본은 2023-04-01 시행한 개정 도로교통법에서 최고 속도 6km/h 이하, 길이 120cm·폭 70cm·높이 120cm 이하의 자동배송 로봇 등을 원격 조작형 소형차(遠隔操作型小型車)로 정의해 보도·노측대를 보행자에 준하는 규칙으로 다니게 하고, 차체 표지 부착과 통행 장소를 관할하는 도도부현 공안위원회에 대한 사전 신고를 요구한다. | ref-985 | 아니오 | medium | 2023 | 실외 / 제약 | — |
| f7 | [사실] | Supply Chain Dive(2023-04-26)에 따르면 2022년 말까지 미국 최소 23개 주가 배송 로봇(개인 배송 장치, PDD) 법을 제정했으나 주마다 기준이 달라 조지아는 최대 500파운드·보도 4mph, 뉴햄프셔는 최대 80파운드·10mph를 허용하며, 이 차이는 가벼운 로봇을 쓰는 Starship 과 무거운 장치를 원한 Amazon·FedEx 가 각 주 입법에 준 영향에서 비롯됐다고 분석했다. | ref-986 | 아니오 | medium | 2023-04-26 | 실외 / 제약 | — |
| f8 | [의견] | Ottonomy CEO 는 미국 주별 배송 로봇 규정의 차이가 커서 모든 주를 같은 기준으로 맞추는 일이 악몽이 될 것이라고 평가했다. | ref-986 | 아니오 | low | 2023-04-26 | 실외 / 제약 | — |
| f9 | [사실] | DC Velocity 에 따르면 Starship Technologies 는 2026-06-08 미국 대학 캠퍼스 운영을 종료하고 캠퍼스 로봇 1,200대 이상을 유럽·미국의 식료품 배송으로 옮긴다고 발표했으며, 식료품 시장이 더 크고 로봇이 개방된 도심 환경에서 안정적으로 운행한다는 점과 2018년부터의 캠퍼스 운영 경험을 이유로 들었다. | ref-981 | 아니오 | medium | 2026-06 | 실외 / 수행 자원 | — |
| f10 | [추정] | Starship 은 핀란드에서 자사 로봇이 식료품 배송의 약 20%를 처리하고 일반 배달원보다 건당 3~4달러 싸게 배송하며 식료품 사업이 2년간 10배 성장 궤도에 있다고 주장한다. | ref-981 | 아니오 | low | 2026-06 | 실외 / 예외·성과 | 벤더 주장 |
| f11 | [추정] | 우아한형제들은 배달로봇 딜리 신규 모델이 바퀴를 키워 낮은 연석을 넘고 경사로 주행이 나아졌으며 적재량이 2L 생수 6병에서 18병으로, 배터리 용량이 약 30% 늘었고 LED 깃대로 이면도로 시인성을 높였으며, 시범 운영에서 평균 배달 시간 약 30분과 응답자 90%의 재이용 의사를 얻었다고 밝혔다. | ref-983 | 아니오 | low | 2025-06-23 | 실외 / 예외·성과 | 벤더 주장 |
| f12 | [사실] | 지디넷코리아(2025-06-23)에 따르면 배민 배달로봇 딜리 신규 모델은 2025-06-17 한국로봇산업진흥원의 실외이동로봇 운행안전인증을 받았고, 딜리는 2025년 2월부터 서울 강남구 논현동·역삼동에서 배민B마트 배달을 시범 운영했으며 신규 모델은 2025년 8월부터 현장에 투입될 예정이었다. | ref-983 | 아니오 | medium | 2025-06-23 | 실외 / 시작 조건 | — |
| f13 | [사실] | 스포츠경향(2026-09-02)에 따르면 뉴빌리티의 자율주행 로봇 뉴비는 덕수궁에서 주·야간 순찰과 화재·쓰러짐 같은 이상 상황 감지를 지원하고 서울숲·충남대학교병원·도쿄 시부야 등에서 운영되며, 5방향 카메라 영상으로 지도를 만들고 위치를 파악하는 V-SLAM 방식을 쓴다. | ref-984 | 아니오 | medium | 2026-09-02 | 실외 / 작업 대상 | — |
| f14 | [추정] | 뉴빌리티는 2026년 상반기까지 국내외 150여 개 현장에서 로봇을 운영해 누적 14만 6,721km 이상을 주행했고 2025년 한 해 4만 4,638회 서비스를 수행했으며 연간 약 1억 4,500만 건의 데이터를 만든다고 밝혔다. | ref-984 | 아니오 | low | 2026-09-02 | 실외 / 예외·성과 | 벤더 주장 |
| f15 | [사실] | Pitt News(2019-10-21)에 따르면 피츠버그 포브스 애비뉴에서 길을 건너려 대기하던 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇히는 일이 생기자 피츠버그 대학이 몇 시간 만에 시험 운행을 멈췄고, Starship 은 로봇이 원래 경사로 뒤에서 기다리도록 설계됐으며 해당 교차로의 지도 오류 때문이라며 소프트웨어를 고치고 다른 교차로를 점검했다고 밝혔다. | ref-987 | 아니오 | medium | 2019-10-21 | 실외 / 예외·성과 | — |
| f16 | [사실] | Gehrke·Phair·Russo·Smaglik(Transportation Research Interdisciplinary Perspectives 18, 2023-03)은 노던애리조나대학 캠퍼스 10개 지점의 1주일 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용을 침범 후 시간(PET) 대리 안전 지표로 분석하고, 상충 수준·지점 특성을 예측 요인으로 모형화해 공유 통로의 시설 관리 전략을 제시하려 했다. | ref-990 | 아니오 | medium | 2023-03 | 실외 / 제약 | — |
| f17 | [사실] | Dobrosovestnova·Schwaninger·Weiss(RO-MAN 2022)는 에스토니아 탈린에서 상업 운영 중인 배송로봇이 겨울에 눈에 갇혔을 때 지나가던 사람들이 자발적으로 도와 운행을 이어 가게 한 사례를 관찰·자기민속지·온라인 콘텐츠 분석으로 연구하고, 사람의 도움이 현실적 완화책이 될 수 있지만 회사가 무급 행인의 도움에 운영을 기대서는 안 된다고 지적했다. | ref-993 | 아니오 | medium | 2022 | 실외 / 예외·성과 | — |
| f18 | [사실] | Tong·Simoni(arXiv 2507.12067, 2025-07; 2026-03 개정)는 보행자·장애물·날씨·혼잡 때문에 보도 배송로봇의 이동 시간이 크게 불확실하다고 보고 강건 최적화와 시뮬레이션을 결합한 경로 계획을 스톡홀름 도심 자료로 시험해, 타원 불확실성 집합과 분포 강건 최단경로(DRSP) 방법이 평균·최악 지연에서 가장 나았고 그 이점은 폭이 넓고 느린 로봇, 궂은 날씨·혼잡 조건에서 가장 컸다고 보고했다. | ref-982 | 아니오 | medium | 2025-07-16 | 실외 / 제약 | — |
| f19 | [사실] | 연계 대상: Nav2 공식 튜토리얼은 실외 항법에 GPS 를 쓰되 일반 GPS 정확도가 좋은 조건에서 1~2m, 최대 10m이고 위치가 자주 튀며, RTK 는 약 1cm까지 줄이지만 기준국이 필요하고 도심·숲에서는 정확도가 더 떨어진다고 적으며, 바퀴 주행거리계·IMU·GPS 를 두 개의 확장 칼만 필터로 융합하고 위경도 목표점을 UTM 좌표로 바꾸며 사전 지도 없이 로봇을 따라 움직이는 전역 비용 지도(rolling costmap)를 쓰는 구성을 안내한다. | ref-988 | 아니오 | medium | 2026-09-30 | 실외 / 수행 자원 | — |
| f20 | [사실] | ISO/TC 204(지능형 교통 시스템)가 개발하는 ISO 4448 시리즈는 보도 등 공공 영역에서 보행자 곁을 다니는 공공 영역 이동로봇(PMR)을 다루며, 개요(Part 1) 외에 경로 계획 충분성(Part 6), 운행 데이터 기록기(Part 9), 안전·신뢰성(Part 16) 부분이 위원회 초안 단계로 준비되고 있다고 표준 책임자가 밝혔다. | ref-989 | 아니오 | medium | 2025-04-20 | 실외 / 제약 | — |
| f21 | [사실] | ISO/TR 4448-1:2024 는 2024-08 발행된 기술 보고서로, 연석에서 사람·화물을 싣고 내리는 로봇 도로 차량과 보호받지 않는 보행자 사이에서 배송·점검·유지보수·감시 같은 일을 하는 로봇 장치의 배치 체계를 개관한다. | ref-994 | 아니오 | medium | 2024-08 | 실외 / 제약 | 원문 미열람 |
| f22 | [추정] | 확인한 자료를 종합하면 66. 실외의 로봇 작업은 (1) 보도 배송 — 음식·장보기 물품을 매장에서 주문자 문 앞까지(f9·f12), (2) 순찰 — 궁궐·공원·역 주변·병원 부지의 주·야간 이상 감지(f13), (3) 캠퍼스 배송 — 대학 캠퍼스 음식 배달(f9·f15·f16)의 세 형태로 나타나며, 대표 업체가 2026년 캠퍼스에서 식료품·도심 배송으로 방향을 바꾼 점(f9)은 캠퍼스 모델이 실외 운영의 시험장 역할을 했음을 시사한다. | ref-981, ref-983, ref-984, ref-987, ref-990 | 아니오 | low | 2026-09-30 | 실외 / 작업 대상 | — |
| f23 | [추정] | 확인한 자료를 종합하면 실외 로봇 작업의 여섯 항목은 시작 조건이 배달 앱·장보기 주문과 순찰 일정(f12·f13), 작업 대상이 음식·식료품과 순찰 구역·이상 상황·보행자(f9·f13), 수행 자원이 배송·순찰 로봇과 관제장치·원격 제어자, 때로 도움을 주는 행인(f1·f17), 제약이 인증·보행자 의무·속도·폭·보험과 관할별 크기·속도·신고 기준, 연석 경사로·좁은 보도·눈·위치 오차(f1~f7·f15·f18·f19), 완료·인계가 주문자 문 앞 전달(f12), 예외·성과가 눈 속 고립·접근성 사고와 운행 중단·배달 시간·비용(f10·f11·f15·f17)으로 채워질 수 있으나, 완료·인계의 확인 방식은 이번 자료에서 명시적으로 확인되지 않았다. | ref-983, ref-984, ref-981, ref-980, ref-993, ref-991, ref-992, ref-985, ref-986, ref-987, ref-982, ref-988 | 아니오 | low | 2026-09-30 | 실외 | — |
| f24 | [추정] | 확인한 자료를 종합하면 날씨는 실외 로봇 운영에서 인증 요건(방수 성능, f1), 이동 시간 불확실성과 경로 선택(f18), 눈 속 고립과 사람 개입(f17)의 세 층위로 나타나므로, 운영 계층은 날씨·혼잡을 배정·경로의 제약과 예외 복구 조건으로 다뤄야 할 것으로 보인다. | ref-980, ref-982, ref-993 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f25 | [추정] | 확인한 자료를 종합하면 66. 실외에서 ROP 가 직접 맡을 범위는 배달·장보기 주문과 순찰 일정을 받아 인증받은 로봇에 배정하고(f1·f12·f13), 관할마다 다른 속도·크기·보행자 의무·신고 조건과 날씨·혼잡을 경로·속도·운행 가능 구역 제약으로 반영하며(f2·f6·f7·f18·f24), 연석 경사로 같은 접근성 민감 지점의 대기 규칙을 지도 제약으로 관리하고(f15), 눈 속 고립·위치 오차 같은 예외를 원격 제어자·현장 인력에게 넘기는 일(f17·f19)이며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. | ref-980, ref-983, ref-984, ref-991, ref-985, ref-986, ref-982, ref-987, ref-993, ref-988 | 아니오 | low | 2026-09-30 | 실외 | — |
| f26 | [추정] | 연계 대상: 분류 원문 19장 기준으로 배달 앱·식료품 주문 시스템은 상위 업무 시스템, 로봇의 위치 추정(GPS·RTK·V-SLAM)·장애물 회피·연석 주행은 로봇 자체 지능·제어, 운행안전인증·도로교통법·일본 신고제·미국 주 PDD 법·보험은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·상태 확인·제약 반영만 걸고 주행 안전 성능과 법적 인증 취득은 로봇 제조사·운영사에 맡겨야 할 것으로 보인다. | ref-983, ref-988, ref-984, ref-980, ref-991, ref-985, ref-986 | 아니오 | low | 2026-09-30 | 실외 | — |
| f27 | [추정] | 이 영역은 보도 통행 규정·인증을 다루는 59. 법·규제·보험·라이선스와 50. 안전 표준·인증·사고 조사(f1~f7·f20·f21), 보행자·자전거와의 상충을 다루는 19. 사람·보행자 모델과 49. 사람 근접 안전(f15·f16), 위경도 좌표와 운행 구역을 다루는 15. 지도·공간·위치 모델과 16. 장소 의미·지도 관리(f15·f19), 날씨·혼잡 아래 경로를 다루는 27. 다중 로봇 경로·교통 관리 — MAPF 와 26. 작업 순서·스케줄링(f18), 눈 속 고립·원격 개입을 다루는 32. 예외 복구·재계획·업무 연속성과 31. 사람–로봇 협업(f17), 순찰 이상 감지를 다루는 38. 모니터링·이상 탐지·원인 분석(f13), 접근성을 다루는 60. 노동·수용성·접근성(f15), 배달 앱 연동을 다루는 23. 업무 시스템 연동(f12), 이기종 관제를 다루는 20. 로봇·제조사 관제 연동(f1·f25), 사업 전환을 다루는 1. 기술·시장·업체 동향과 3. 경제성·조달·사업 모델(f9·f10)과 이어진다. | ref-980, ref-991, ref-985, ref-986, ref-989, ref-994, ref-987, ref-990, ref-988, ref-982, ref-993, ref-984, ref-983, ref-981 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-981 | DC Velocity | Starship steers its delivery robots off college campuses and toward grocery sector | 2026-06 | 기사 | medium | 2026-09-30 | https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector | 아니오 |
| ref-982 | Tong, X., & Simoni, M. D. (arXiv) | Robust Route Planning for Sidewalk Delivery Robots | 2025-07-16 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.12067 | 아니오 |
| ref-983 | 지디넷코리아 | 배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득 | 2025-06-23 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20250623095742 | 아니오 |
| ref-984 | 스포츠경향 | 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 | 2026-09-02 | 기사 | medium | 2026-09-30 | https://sports.khan.co.kr/article/202609020605003/ | 아니오 |
| ref-985 | 内閣府 (일본 내각부) | 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について | 2023 | 정부·연구기관 | high | 2026-09-30 | https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html | 아니오 |
| ref-986 | Supply Chain Dive | Why delivery robots face a regulatory ‘nightmare’ | 2023-04-26 | 기사 | medium | 2026-09-30 | https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/ | 아니오 |
| ref-987 | The Pitt News | Pitt pauses testing of Starship robots due to safety concerns | 2019-10-21 | 기사 | medium | 2026-09-30 | https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/ | 아니오 |
| ref-988 | Open Navigation (Nav2) | Navigating Using GPS Localization — Nav2 documentation | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html | 아니오 |
| ref-989 | Urban Robotics Foundation (Bern Grush) | ISO-4448 Update Winter 2024 | 2024-02-04 | 업계 보고서 | medium | 2026-09-30 | https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024 | 아니오 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03 | 논문 | medium | 2026-09-30 | https://doi.org/10.1016/j.trip.2023.100789 | 아니오 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | 정부·연구기관 | high | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-993 | Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022) | With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow | 2022 | 논문 | medium | 2026-09-30 | https://ieeexplore.ieee.org/abstract/document/9900588/ | 아니오 |
| ref-994 | ISO | ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm | 2024-08 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/81068.html | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/outdoor.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f2·f3(2023-11 보도 통행 허용), f9(대표 업체의 캠퍼스 철수와 도심 전환), f15(접근성 사고) / 섹션 4: f3(보행자 지위), f6(원격 조작형 소형차), f7(PDD), f16(침범 후 시간), f19(RTK), f20·f21(PMR) / 섹션 5(현장 유형 모두 실외): 보도 배송 — f12(딜리), f11(벤더 주장); 순찰 — f13, f14(벤더 주장); 캠퍼스 — f9, f10(벤더 주장), f15, f16; 날씨 — f17; 작업 형태 f22, 여섯 항목 f23(완료·인계 근거 부족 명시) / 섹션 6: 위치 추정·센서 융합 f19(연계 대상 표시), 강건 경로 계획 f18, 날씨 대응 f24, 사람 도움·원격 개입 f17 / 섹션 7: 운행안전인증 f1·f2·f4·f5, 도로교통법 f3, 일본 f6, 미국 f7·f8, ISO 4448 f20·f21(원문 미열람), Nav2 f19 / 섹션 8: f16, f17, f18 / 섹션 9: f25(직접 범위), f26(연계 대상) / 섹션 10: f27 — 1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60 / 섹션 11: open_questions_new 5건. f10·f11·f14 는 벤더 주장 병기 필수. 다음 실행 후보: 59. 법·규제·보험·라이선스 페이지에 f2~f7 반영, 19. 사람·보행자 모델 페이지에 f15·f16 반영, 50. 안전 표준·인증·사고 조사 페이지에 f20·f21 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 공공 영역 이동로봇 | Public-area Mobile Robot (PMR) | 보도·연석 같은 공공 공간에서 보호받지 않는 보행자 곁을 다니며 배송·점검·감시 등을 하는 로봇으로, ISO/TC 204 의 ISO 4448 시리즈가 쓰는 용어다. |
| 개인 배송 장치 | Personal Delivery Device (PDD) | 미국 여러 주 법에서 보도·횡단보도를 다니며 물건을 나르는 배송 로봇을 가리키는 법적 범주로, 무게·속도 상한이 주마다 다르다. |
| 원격 조작형 소형차 | Remote-controlled Small Vehicle (遠隔操作型小型車) | 일본 개정 도로교통법(2023-04 시행)이 정한 최고 6km/h·120×70×120cm 이하의 자동배송 로봇 등의 범주로, 보도를 보행자에 준하는 규칙으로 다니며 공안위원회에 사전 신고해야 한다. |
| 침범 후 시간 | Post-Encroachment Time (PET) | 한 이동체가 충돌 가능 지점을 떠난 뒤 다른 이동체가 그 지점에 도착하기까지의 시간 차로, 실제 충돌 없이 상충의 심각도를 재는 대리 안전 지표다. |

## 열린 질문

새로 생긴 질문:

- 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? | 관련 영역: 66. 실외, 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f5 | 종류: 일반
- 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? | 관련 영역: 66. 실외, 20. 로봇·제조사 관제 연동, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반
- 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? | 관련 영역: 66. 실외, 60. 노동·수용성·접근성, 16. 장소 의미·지도 관리 | 근거: f15 | 종류: 일반
- 국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가? | 관련 영역: 66. 실외, 32. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반
- 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? | 관련 영역: 66. 실외, 21. 상호운용 표준·적합성, 16. 장소 의미·지도 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f5 운행안전인증 심사항목 16→8 개정 시점·근거 고시 원문 미확인(검색 요약에만 2025-11 개정 언급)
    - f6 일본 규정은 내각부 백서 단독, 경찰청 원문 PDF 는 본문 추출 실패
    - f7 미국 주 PDD 법 개수(23개 이상)는 2023-04 기사 기준이며 이후 변화 미확인
    - f10·f11·f14 는 회사 발표 수치(벤더 주장)이며 독립 확인 없음
    - f16 NAU 연구의 상충 비율 수치는 초록에 없어 넣지 않음(ScienceDirect 403)
    - f17 탈린 연구는 초록 기준, 운영 업체명 미확인
    - f18 은 동료심사 전 프리프린트
    - f21 ISO/TR 4448-1 은 원문 미열람(ISO 페이지 403), 검색 요약 범위만 사용
    - 뉴빌리티·딜리의 관제·원격 제어 방식과 수령 확인(완료·인계) 방식 미확인
    - 국내 실외 로봇의 강설·폭우 운영 기준 자료 미확인
- 범위 경계 위반 의심:
    - f19: GPS·RTK·센서 융합은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·위치 추정)이므로 '연계 대상: '으로 표시하고 위치 오차가 운영 제약이 되는 근거로만 제안함
    - f13: V-SLAM 위치 추정 언급은 로봇 자체 지능·제어이며 순찰 사례의 설명으로만 씀
    - f26: 배달 앱, 로봇 주행·위치 추정, 인증·법령·보험은 상위 업무 시스템·로봇 자체 지능·제어·업종별 조건이므로 '연계 대상: '으로 표시함
    - f2~f7: 법령·인증 내용은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 실외 운영의 제약 근거로만 제안함
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f11 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 이전 반환값(runs/2026-09-30-01/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. 이번 브리프의 회사 성능·실적 주장(f10 Starship, f11 배민 딜리, f14 뉴빌리티)은 모두 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈고, 벤더 문서 유형 출처만 근거로 한 [사실] finding 은 없다(관련 finding: f10, f11, f14). 이전 실행과 finding·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-980~ref-994, 예약 구간 안)로 출처 상한에 도달해 Knightscope 등 해외 순찰 사례, 공원·골프장 등 다른 실외 작업, 한국 강설 운영 기준은 조사하지 못했다. 원문 열람: 14건 webfetch(논문 2건은 초록 페이지), 1건 미열람(ref-994 ISO 403). 열지 못해 쓰지 않은 것: 경찰청 PDF(본문 추출 실패), MDPI 피츠버그 파일럿 논문·ACM 논문·ScienceDirect(403), 한국로봇학회지 RTK 논문(PDF 손상). 교차 확인 1건(f2: 정책브리핑·지디넷코리아). 신뢰도 high finding 1건(f2). 분류 원문 핵심 질문(보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가)에는 작업 형태 f22, 여섯 항목 f23, 날씨 f24, 직접 범위 f25, 연계 대상 f26 으로 답했으며, 결론은 '보도 운영은 관할마다 다른 인증·보행자 의무·속도·크기 조건 위에서 이루어지고, 날씨·보행자·접근성 민감 지점이 경로·대기·예외 처리의 제약이 되며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 확인되지 않았다'는 추정이다. 현장 유형은 f27(연결)을 빼고 모두 실외이며 캠퍼스·궁궐·공원·도심 보도 사례다. 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 한국로봇산업진흥원·정책브리핑·지디넷코리아 2건·스포츠경향 다섯 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(f18 의 시뮬레이션은 경로 계획 평가용으로 26·27 쪽에만 연결). 용어집에 이미 있는 실외이동로봇 운행안전인증·원격 조작·비용 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음.
```

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


## 스키마 불일치 (재실행)

직전 반환값이 JSON 스키마(schemas/research.schema.json)와 맞지 않아 퍼블리셔가 반려했다. 아래 오류를 모두 고친, 스키마에 맞는 JSON 객체 하나만 다시 반환한다. 내용을 새로 조사하지 말고 형식만 고친다.

- finding f1: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
- finding f6: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
- finding f8: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
- finding f15: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
- finding f18: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
