(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-11
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 61. 물류창고 (Q. 현장 유형별 적용)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-910
- 새 출처 id 구간: ref-910 ~ ref-939 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-910 부터 순서대로 쓰고 ref-939 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-11/target.json

```json
{
  "run_id": "2026-09-29-11",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 103,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 61,
    "area_name": "61. 물류창고",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=61"
}
```

### docs/categories/site-type-applications/warehouse.md

```markdown
---
title: "61. 물류창고"
type: area
category: "Q. 현장 유형별 적용"
area_no: 61
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 61. 물류창고

# 61. 물류창고

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]

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

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

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

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

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

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

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

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

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

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 909건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 243개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
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
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
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
- skill-interface: 스킬 인터페이스 (Skill Interface)
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
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [61] 에 걸린 4건 / 전체 162건)

```markdown
- oq-134 [열림] 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? (영역 11, 61, 63)
- oq-138 [열림] 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? (영역 9, 61, 63)
- oq-142 [열림] 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? (영역 12, 61, 63, 62)
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
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

### runs/2026-09-29-10/research.md

```markdown
# 리서치 브리프 2026-09-29-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-10 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 1. 기술·시장·업체 동향 |
| 대분류 | A. 기획·사업 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 서비스형 로봇·로봇 밀도·에이전틱 AI·IT/OT 융합 용어 없음(다중 플릿 오케스트레이션·플릿 관리 시스템·모바일 매니퓰레이터는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 시장 통계 추적, 제품·업체 지형 분류(제조사 플릿 매니저 / 제3자 오케스트레이션 / 표준·오픈소스), 로봇 종류 변화 추적, AI 연구 동향 네 갈래 모두 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050, MassRobotics AMR 상호운용 표준, Open-RMF 의 지형상 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — IFR World Robotics, 국내 로봇산업 실태조사, 시장조사 업체 자료, 다중 로봇 서베이 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 2. 사용 사례·요구·책임 범위, 3. 경제성·조달·사업 모델, 4. 이기종 로봇 등록, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 44. 로봇 기반 모델·언어 모델 계획, 61. 물류창고, 62. 제조 공장 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 없음, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
2. 세계·국내 로봇 시장의 규모와 종류별 흐름(산업용·전문 서비스용·운송·물류)은 공식 통계에서 어떻게 나타나는가? (섹션 3·4·8 겨냥)
3. 오케스트레이션·관제·상호운용 제품과 업체(제3자 다중 플릿 오케스트레이션 소프트웨어, 상호운용 표준, 오픈소스, 국내 업체)의 지형은 어떻게 나뉘는가? (섹션 4·6·7 겨냥)
4. 오케스트레이션 대상 로봇의 종류·형태(AMR·휴머노이드·모바일 매니퓰레이터)는 어떻게 바뀌고 있으며 현장 도입 사례는 무엇인가? (섹션 5·6 겨냥, 현장 유형 명시)
5. 언어 모델·기반 모델 같은 AI 기술이 다중 로봇 오케스트레이션 연구에 어떻게 들어오고 있는가? (섹션 6·8 겨냥, 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 연결)
6. 국내 정책·통계·업체 동향(지능형 로봇 기본계획, 로봇산업 실태조사, 국내 이기종 로봇 관제 업체)은 무엇인가? (섹션 5·8 겨냥, 한국 자료 우선)
7. 동향 조사에서 ROP가 직접 맡을 것과 시장조사 기관·로봇 제조사에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 국제로봇연맹(IFR)의 World Robotics 2025 서비스 로봇 보고서(2025-10-07 발표)는 2024년 전문 서비스 로봇 판매가 약 20만 대(전년 대비 9% 증가)이며, 그중 운송·물류 응용이 102,900대(14% 증가)로 가장 많고 접객 로봇은 4만2천 대 이상(11% 감소), 의료 로봇은 16,700대(91% 증가)라고 집계했다. | ref-899 | 아니오 | medium | 2025-10-07 | — | — |
| f2 | [사실] | IFR 은 2024년 서비스형 로봇(Robot-as-a-Service, RaaS) 플릿이 31% 성장했고 운송·물류 부문에서는 42% 성장했다고 보고하며, 인력 부족과 고령화를 수요 동인으로 들고 기업이 구매 대신 구독·임대 계약을 택하는 흐름을 지적했다. | ref-899 | 아니오 | medium | 2025-10-07 | — | — |
| f3 | [사실] | IFR 의 World Robotics 2025 산업용 로봇 보고서는 2024년 세계 산업용 로봇 설치가 542,000대(4년 연속 50만 대 초과)이고 아시아가 74%, 중국이 295,000대(54%)를 차지하며, 한국은 30,600대(3% 감소)로 중국·일본·미국에 이은 4위, 세계 가동 대수는 4,664,000대(9% 증가), 2025년 575,000대·2028년 70만 대 초과를 전망한다고 밝혔다. | ref-900 | 아니오 | medium | 2025 | — | — |
| f4 | [사실] | IFR 의 2026-04-08 로봇 밀도 보도자료에 따르면 한국은 제조업 종사자 1만 명당 로봇 1,220대로 세계 1위이며 싱가포르 818대, 독일 449대, 일본 446대, 중국 166대, 세계 평균 132대다. | ref-901 | 아니오 | medium | 2026-04-08 | — | — |
| f5 | [사실] | IFR 이 2026-01-08 발표한 2026년 세계 로봇 5대 동향은 에이전틱 AI 와 자율성, IT·OT 융합에 따른 범용성, 휴머노이드의 신뢰성·효율 입증(사이클 타임·에너지·유지보수 비용 기준 충족 필요), 안전·사이버보안 거버넌스, 노동력 부족 대응이며, 오케스트레이션 대상 로봇의 종류가 휴머노이드로 넓어지는 흐름과 AI 결합을 동향으로 꼽는다. | ref-902 | 아니오 | medium | 2026-01-08 | — | — |
| f6 | [사실] | 한국로봇산업진흥원의 2024년 국내 로봇산업 실태조사(2025-07-04~09-12 조사, 2024년 12월 말 기준)를 전한 로봇신문 요약에 따르면 국내 로봇 사업체는 2,509개(0.6% 감소), 매출 6조1,695억 원(3.2% 증가), 생산 5조9,447억 원(4.5% 증가), 수출 1조2,578억 원, 수입 6,895억 원, 인력 34,649명이며, 매출 구성은 제조업용 로봇 3조1,075억 원(50.4%), 부품·소프트웨어 1조9,810억 원(32.1%), 전문서비스용 6,423억 원, 개인서비스용 4,386억 원이다. | ref-903 | 아니오 | medium | 2026-01-25 | — | — |
| f7 | [사실] | 산업통상자원부는 2024-01-16 로봇산업정책심의회에서 제4차 지능형 로봇 기본계획(2024~2028)을 확정하고 2030년까지 첨단로봇 100만 대 보급, 로봇 핵심부품 국산화율 80%, 규제 51개 개선, 로봇 핵심 인력 1만5천 명 이상 확보, 민관 합동 3조 원 이상 투자를 목표로 제시했다. | ref-904 | 아니오 | medium | 2024-01-16 | — | — |
| f8 | [사실] | 시장조사 업체 Interact Analysis(2023-01)는 다중 플릿 오케스트레이션 소프트웨어를 서로 다른 제조사의 AMR 플릿 여럿을 하나의 창고 시스템 안에서 관리하는 소프트웨어(고정 자동화의 창고 제어 시스템에 비견)로 정의하고, 접근을 로봇을 직접 통합하는 저수준 제어와 제조사 플릿 매니저를 관리하는 고수준 제어로 나누며 상호운용은 표준 또는 미들웨어로 푼다고 정리하면서 GreyOrange·Synaos·Waku Robotics·CoEvolution·InOrbit 등을 업체로 들었다. | ref-257 | 아니오 | medium | 2023-01 | 물류창고 / 수행 자원 | — |
| f9 | [의견] | Interact Analysis 는 2021~2027년 다중 플릿 오케스트레이션 소프트웨어 시장이 연평균 138% 성장할 것으로 전망했으나, 이 수치는 방법론이 공개되지 않은 시장조사 전망이다. | ref-257 | 아니오 | low | 2023-01 | — | — |
| f10 | [사실] | Interact Analysis(2025-07)는 이동로봇 시장의 2025년 전망을 8억 달러 낮추고 2030년 매출 전망 156억 달러, 2025~2030년 연평균 성장률을 26%에서 21%로 조정했으며, 원인으로 미국의 관세, 투자 관망, 창고 신축 감소(2030년까지 연 -2.0%)를 들고 AGV 운반 로봇 출하 성장률을 6%에서 4%로 낮춘 반면 사람 대상 운반(P2G) 로봇은 연 30% 성장을 유지했다. | ref-906 | 아니오 | medium | 2025-07 | — | — |
| f11 | [사실] | MassRobotics 의 AMR 상호운용 표준 설명 페이지(2023-06-19)에 따르면 1.0 판(2021-05 GitHub 공개)은 서로 다른 제조사 AMR 이 위치·목적지·식별자·제조사·모델·치수·운용 상태·속도·방향 같은 관측 정보를 공유하게 하되 플릿 관리·항법·안전 시스템·하드웨어는 다루지 않으며, 미션 통신 API 를 더한 2.0 판이 개발 중이고 InOrbit·Vecna Robotics·Locus Robotics 등이 작업반에 참여한다. | ref-391 | 아니오 | medium | 2023-06-19 | — | — |
| f12 | [사실] | Interact Analysis(2023-01)는 독일 자동차 산업이 상호운용의 중요성을 먼저 인식해 VDA 5050 을 개발했고 Audi·VW·BMW 같은 완성차 업체가 이 표준을 따르는 마스터 컨트롤 업체를 지원하거나 분사시켜 공급사 전반의 채택을 이끌었다고 서술한다. | ref-257 | 아니오 | medium | 2023-01 | 제조 공장 | — |
| f13 | [사실] | Li·An·Abrar·Zhou(드렉셀 대학교, 2025-02 v1, 2026-05 v5)의 서베이는 언어 모델(LLM)의 다중 로봇 시스템 적용을 고수준 작업 배정, 중수준 동작 계획, 저수준 행동 생성, 사람 개입의 네 층으로 분류하고, 수학적 추론 한계·환각·지연·벤치마크 부재를 적용의 과제로 꼽아 AI 가 오케스트레이션 연구에 들어오는 지점을 정리했다. | ref-165 | 아니오 | medium | 2026-05-03 | — | — |
| f14 | [추정] | Agility Robotics 는 2025-11-20 자사 휴머노이드 Digit 이 GXO 의 Flowery Branch 시설에서 10만 개 이상의 토트를 옮겼고 AMR 과 컨베이어 사이의 토트 이송과 다른 바닥 위치로의 토트 적재 작업을 하며 가변 하중 균형 유지와 조명 변화 속 물체 인식이 검증됐다고 발표했다. | ref-909 | 아니오 | low | 2025-11-20 | 물류창고 / 수행 자원 | 벤더 주장 |
| f15 | [사실] | The Robot Report(2024-06-27)는 GXO 가 Agility Robotics 와 다년 서비스형 로봇(RaaS) 계약을 맺어 조지아주 Spanx 물류 시설에서 Digit 이 6 River Systems 의 Chuck AMR 에서 컨베이어로 빈 토트와 상품 토트를 옮기게 했고, 이것이 매출이 발생하는 첫 상업 휴머노이드 배치라는 Agility 의 주장과 함께 GXO 가 Apptronik 의 Apollo 도 병행 시험한다고 보도했다. | ref-910 | 아니오 | medium | 2024-06-27 | 물류창고 / 수행 자원 | — |
| f16 | [사실] | 서로 다른 두 발행 주체(Agility Robotics 의 발표, 전문지 The Robot Report 의 보도)가 GXO 물류 시설에서 휴머노이드 Digit 이 AMR 과 컨베이어 사이의 토트 이송 작업에 서비스형 로봇 계약으로 투입됐다고 각각 전해, 휴머노이드가 AMR 과 함께 물류창고 실운영 흐름에 들어간 사례가 한 곳 이상에서 확인된다. | ref-909, ref-910 | 예 | medium | 2025-11-20 | 물류창고 / 수행 자원 | — |
| f17 | [사실] | 아시아경제(2026-09-03)에 따르면 CJ대한통운은 경기 용인 양지 올리브영 물류센터의 상품 포장 공정에 양팔 휴머노이드 로봇 2대를 투입해 박스 안에 완충재를 넣는 작업부터 시작했고, 2025년 군포 풀필먼트센터 현장 실증에서 한 단계 나아간 것이며 로보티즈(하드웨어)·에이딘로보틱스(로봇핸드)·리얼월드AI(로봇 기반 모델)와 협력하고 피킹·분류·검수·포장으로 범위를 넓힐 계획이라고 밝혔다. | ref-912 | 아니오 | low | 2026-09-03 | 물류창고 / 수행 자원 | — |
| f18 | [사실] | 서울신문(2026-09-23)에 따르면 현대차그룹은 미국 조지아 메타플랜트(HMGMA) 안에 휴머노이드 아틀라스가 실제 공장과 같은 환경에서 부품을 조립 순서대로 놓는 서열 작업과 물류 작업을 익히는 로봇 훈련 시설 RMAC 을 2026년 6월 시범 가동해 9월 21일 본격 가동했고, 2028년 서열 작업, 2030년 조립·물류 작업 투입과 그룹 공장에 아틀라스 2만5천 대 배치를 계획한다. | ref-913 | 아니오 | low | 2026-09-23 | 제조 공장 / 수행 자원 | — |
| f19 | [추정] | 로봇신문(2025-11-09)이 전한 클로봇의 설명에 따르면 이기종 로봇 통합 관제 플랫폼 크롬스(CROMS)는 여러 제조사의 로봇 50대 이상을 동시에 관제하고 실내 자율주행 소프트웨어 카멜레온은 정지 정밀도 ±1cm·주행 정밀도 ±2cm 를 낸다. | ref-870 | 아니오 | low | 2025-11-09 | — | 벤더 주장 |
| f20 | [사실] | 로봇신문(2025-11-09)에 따르면 2017년 설립된 클로봇은 이기종 로봇 통합 관제 플랫폼 크롬스와 범용 실내 자율주행 소프트웨어 카멜레온을 핵심 제품으로 두고 2024년 말 코스닥에 상장했으며, 인천국제공항에 청소 로봇과 다중 로봇 5G 디지털 트윈 관제 시스템을 적용하고 구독형 로봇 서비스 확대를 전략으로 밝혔다. | ref-870 | 아니오 | low | 2025-11-09 | 기타 / 수행 자원 | — |
| f21 | [추정] | 확인한 자료를 종합하면 로봇 오케스트레이션 제품 지형은 제조사별 플릿 매니저, 그 위에서 여러 제조사 플릿을 묶는 제3자 다중 플릿 오케스트레이션 소프트웨어(해외 GreyOrange·Synaos·InOrbit 등, 국내 클로봇 등), 그리고 이들을 잇는 상호운용 표준(VDA 5050, MassRobotics)과 오픈소스 미들웨어(Open-RMF)의 세 층으로 나뉘는 것으로 보인다. | ref-257, ref-391, ref-870, ref-004 | 아니오 | low | 2026-09-29 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 오케스트레이션 대상 로봇은 물량 면에서 운송·물류용 AMR 이 주도하는 가운데(f1) 휴머노이드가 물류창고(GXO, CJ대한통운)와 제조 공장(현대차그룹)에서 시범을 지나 운영 초기 단계에 들어섰고 IFR 이 이를 2026년 동향으로 꼽아(f5·f16·f17·f18), 이기종 로봇 등록과 관제가 AMR 중심에서 휴머노이드·양팔 로봇으로 넓어질 것으로 보이나 그 규모와 시점은 회사 발표 계획 수준이다. | ref-899, ref-902, ref-910, ref-912, ref-913 | 아니오 | low | 2026-09-29 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 1. 기술·시장·업체 동향에서 ROP가 직접 맡을 범위는 공식 통계(IFR, 한국로봇산업진흥원)와 시장조사·연구 서베이를 주기적으로 모아 오케스트레이션·관제·상호운용 제품 지형과 연결 대상 로봇 종류의 변화를 정리하고 그 결과를 2. 사용 사례·요구·책임 범위, 3. 경제성·조달·사업 모델, 4. 이기종 로봇 등록, 20. 로봇·제조사 관제 연동의 입력으로 넘기는 일이며, 통계 산출과 시장 전망 자체는 발행 기관의 몫으로 인용만 하는 것이 맞아 보인다. | ref-899, ref-903, ref-257, ref-165 | 아니오 | low | 2026-09-29 | — | — |
| f24 | [추정] | 연계 대상: 휴머노이드의 하중 균형·물체 인식이나 자율주행 소프트웨어의 정지·주행 정밀도 같은 로봇 자체 성능은 분류 원문 19장의 로봇 자체 지능·제어 쪽이므로, 이종 제조사를 잇는 ROP 는 이런 벤더 성능 주장을 동향 지형에 기록하되 검증은 제조사·인증 기관에 맡기고 지원 기능과 실행 조건의 확인만 맡아야 할 것으로 보인다. | ref-909, ref-870 | 아니오 | low | 2026-09-29 | — | — |
| f25 | [추정] | 이 영역은 같은 대분류의 2. 사용 사례·요구·책임 범위와 3. 경제성·조달·사업 모델(서비스형 로봇 확산 f2)에 입력을 주고, 로봇 종류 변화는 4. 이기종 로봇 등록에, 제품·표준 지형은 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성에, 언어 모델 기반 오케스트레이션 연구(f13)는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 25. 작업 배정 — MRTA 에, 현장 사례는 61. 물류창고(f16·f17)와 62. 제조 공장(f12·f18)에 이어진다. | ref-899, ref-902, ref-257, ref-165 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-899 | International Federation of Robotics (IFR) | World Robotics 2025 report – SERVICE ROBOTS – released by IFR | 2025-10-07 | 업계 보고서 | medium | 2026-09-29 | https://ifr.org/ifr-press-releases/news/service-robots-see-global-growth-boom | 아니오 |
| ref-900 | International Federation of Robotics (IFR) | World Robotics 2025 report – INDUSTRIAL ROBOTS – released by IFR | 2025 | 업계 보고서 | medium | 2026-09-29 | https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years | 아니오 |
| ref-901 | International Federation of Robotics (IFR) | Robot Density Surges in Europe, Asia, and Americas | 2026-04-08 | 업계 보고서 | medium | 2026-09-29 | https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas | 아니오 |
| ref-902 | International Federation of Robotics (IFR) | Top 5 Global Robotics Trends 2026 | 2026-01-08 | 업계 보고서 | medium | 2026-09-29 | https://ifr.org/ifr-press-releases/news/top-5-global-robotics-trends-2026 | 아니오 |
| ref-903 | 로봇신문 (한국로봇산업진흥원 '2024년 국내 로봇산업 실태조사 결과 보고서' 요약) | [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약 | 2026-01-25 | 기사 | medium | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=44544 | 아니오 |
| ref-904 | 로봇신문 (산업통상자원부 발표 보도) | 산업부, '제4차 지능형 로봇 기본계획' 발표 | 2024-01-16 | 기사 | medium | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=33788 | 아니오 |
| ref-257 | Interact Analysis (Rueben Scriven) | AMR Multi-Fleet Orchestration Software Explained | 2023-01 | 업계 보고서 | medium | 2026-09-29 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 아니오 |
| ref-906 | Interact Analysis (Ash Sharma) | Mobile Robot Market Forecast Revised Downward | 2025-07 | 업계 보고서 | medium | 2026-09-29 | https://interactanalysis.com/insight/mobile-robot-market-forecast-slashed/ | 아니오 |
| ref-391 | MassRobotics | What Is the MassRobotics AMR Interoperability Standard? | 2023-06-19 | 표준 | medium | 2026-09-29 | https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/ | 아니오 |
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. (Drexel University) | Large Language Models for Multi-Robot Systems: A Survey | 2026-05-03 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2502.03814 | 아니오 |
| ref-909 | Agility Robotics | Digit Moves Over 100,000 Totes in Commercial Deployment | 2025-11-20 | 벤더 문서 | low | 2026-09-29 | https://www.agilityrobotics.com/content/digit-moves-over-100k-totes | 아니오 |
| ref-910 | The Robot Report (Steve Crowe) | Agility Robotics' Digit humanoids land first official job | 2024-06-27 | 기사 | medium | 2026-09-29 | https://www.therobotreport.com/agility-robotics-digit-humanoid-lands-first-official-job/ | 아니오 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막 | 2025-11-09 | 기사 | low | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 아니오 |
| ref-912 | 아시아경제 | CJ대한통운, 물류업계 최초 AI 휴머노이드 상용화 '첫발' | 2026-09-03 | 기사 | low | 2026-09-29 | https://view.asiae.co.kr/article/2026090308385213768 | 아니오 |
| ref-913 | 서울신문 | 부품 배치 '척척' 무거운 짐도 '사뿐'… 아틀라스 2.5만대 로봇 학교 간다 | 2026-09-23 | 기사 | low | 2026-09-29 | https://www.seoul.co.kr/news/economy/industry/2026/09/23/20260923031003 | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-business/technology-market-and-vendor-trends.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1·f3(운송·물류 로봇과 산업용 로봇 설치가 계속 늘어 오케스트레이션 대상이 커짐), f5(IFR 2026 동향의 에이전틱 AI·휴머노이드), f10(시장 전망이 관세·경기로 흔들려 주기적 재확인 필요) / 섹션 4: f2(서비스형 로봇 RaaS), f4(로봇 밀도), f8(다중 플릿 오케스트레이션 소프트웨어의 두 접근), f5(에이전틱 AI·IT/OT 융합) / 섹션 5: 물류창고 — f16(GXO 의 휴머노이드–AMR 토트 이송, 교차 확인), f17(CJ대한통운 올리브영 물류센터 포장 공정, 회사 발표 기반임을 명시), 제조 공장 — f12(독일 자동차 산업의 VDA 5050 채택 견인), f18(현대차그룹 RMAC, 계획 단계임을 명시), 기타 — f20(인천공항 클로봇 관제), 병원·상업 시설·가정·실외 사례는 확인되지 않음을 서술 / 섹션 6: 시장 통계 추적 f1·f3·f4·f6, 제품 지형 세 층 f8·f11·f12·f21, 로봇 종류 변화 f5·f16·f22, AI 연구 동향 f13(교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 함께 연결) / 섹션 7: f12(VDA 5050), f11(MassRobotics AMR 상호운용 표준 1.0·2.0), f21(Open-RMF, ref-004 재사용) / 섹션 8: f1·f3·f4·f5(IFR), f8·f9·f10(Interact Analysis, 전망은 방법론 미공개임을 명시), f13(LLM 다중 로봇 서베이), 국내 f6(실태조사)·f7(기본계획)·f20(클로봇) / 섹션 9: f23(직접 범위: 통계·서베이 수집과 지형 정리, 다른 영역으로의 입력), f24(연계 대상: 로봇 자체 성능 검증은 제조사·인증 기관) / 섹션 10: f25 — 2. 사용 사례·요구·책임 범위, 3. 경제성·조달·사업 모델, 4. 이기종 로봇 등록, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 25. 작업 배정 — MRTA, 44. 로봇 기반 모델·언어 모델 계획, 61. 물류창고, 62. 제조 공장 / 섹션 11: open_questions_new 4건. f14·f19 는 벤더 주장 병기 필수. 다음 실행 후보: 3. 경제성·조달·사업 모델 페이지에 f2·f10 반영, 21. 상호운용 표준·적합성 페이지에 f11·f12 반영, 61. 물류창고 페이지에 f16·f17 반영, 62. 제조 공장 페이지에 f18 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 서비스형 로봇 | Robot-as-a-Service (RaaS) | 로봇을 구매하지 않고 구독·임대·사용량 계약으로 쓰는 사업 모델로, IFR 은 2024년 전문 서비스 로봇에서 이 방식의 플릿이 31% 성장했다고 집계한다. |
| 로봇 밀도 | Robot Density | 제조업 종사자 1만 명당 가동 중인 산업용 로봇 대수로, 국가 경제 규모에 대한 자동화 수준을 비교하는 IFR 지표이며 2024년 한국이 1,220대로 1위다. |
| 에이전틱 AI | Agentic AI | 구조화된 의사결정을 위한 분석형 AI 와 적응을 위한 생성형 AI 를 결합해 로봇이 스스로 판단·행동하게 하는 접근으로, IFR 이 2026년 로봇 동향의 첫째로 꼽았다. |
| IT/OT 융합 | IT/OT Convergence | 정보기술의 데이터 처리와 운영기술의 물리 제어를 실시간 데이터 교환으로 잇는 흐름으로, 로봇 관제·오케스트레이션이 업무 시스템과 설비 사이에 놓이는 배경이 된다. |

## 열린 질문

새로 생긴 질문:

- 국내 이기종 로봇 통합 관제 제품(크롬스 등)이 VDA 5050 이나 MassRobotics AMR 상호운용 표준을 지원하는지 공개 자료로 확인되는가? | 관련 영역: 1. 기술·시장·업체 동향, 21. 상호운용 표준·적합성 | 근거: f19 | 종류: 일반
- 다중 플릿 오케스트레이션 소프트웨어 시장의 규모·성장률에 대해 산정 방법론이 공개된 독립 출처가 있는가(확인한 시장조사 전망은 방법론이 공개되지 않았다)? | 관련 영역: 1. 기술·시장·업체 동향, 3. 경제성·조달·사업 모델 | 근거: f9 | 종류: 일반
- 휴머노이드가 AMR 과 함께 물류·제조 현장에 들어올 때 기존 플릿 관제·오케스트레이션 플랫폼은 휴머노이드를 어떤 인터페이스로 등록·관제하며 AMR–휴머노이드 인계는 누가 조율하는가? | 관련 영역: 1. 기술·시장·업체 동향, 4. 이기종 로봇 등록, 30. 로봇 간 협업·물리적 인계 | 근거: f16 | 종류: 일반
- 한국로봇산업진흥원 로봇산업 실태조사에 오케스트레이션·관제 소프트웨어 매출을 따로 집계하는 항목이 있는가, 없다면 국내 관제 소프트웨어 시장 규모를 어떤 자료로 추적할 것인가? | 관련 영역: 1. 기술·시장·업체 동향, 3. 경제성·조달·사업 모델 | 근거: f6 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f16 외 모든 finding 교차 확인 실패(통계·시장조사·기사마다 발행 주체 한 곳)
    - f6 한국로봇산업진흥원 실태조사 원문 보고서(진흥원 포털·공공데이터포털·한국로봇산업협회 페이지)는 연결 끊김·빈 응답으로 열지 못해 로봇신문 요약으로 대신함
    - f7 산업통상자원부 보도자료(korea.kr)는 열었으나 목표 수치가 첨부 PDF 에만 있어 로봇신문 기사로 대신함
    - ref-900 IFR 산업용 로봇 보도자료의 정확한 발행일: 열람 도구가 2024-09-25 로 읽었으나 World Robotics 2025 판 발표는 2025년이어서 published 를 연도(2025)로만 적음
    - f9·f10 Interact Analysis 전망의 산정 방법론 미확인
    - f14 Agility 의 토트 10만 개·검증 주장은 벤더 주장이며 독립 출처 없음
    - f19 클로봇 50대 이상 관제·±1cm 정밀도는 기사에 실린 회사 설명이며 제품 페이지(clobot.co.kr/croms)는 403 으로 열지 못함
    - f17·f18 CJ대한통운·현대차그룹 사례는 회사 발표 기반 기사 한 건씩이며 정량 성과·확정 일정 미확인
    - TechRxiv 'A Survey on Multi-Robot Collaboration Systems'(2025-10-31)는 두 경로 모두 403 으로 열지 못해 출처에서 제외 — 오케스트레이션 아키텍처 분류의 핵심 후보 출처
    - f21 의 Open-RMF 층은 이번 실행에서 다시 열지 않은 재사용 출처 ref-004 에 기댐
    - 국내 관제 업체 가운데 클로봇 외(스페이스뱅크 로보뷰엑스, 엠투엠글로벌)는 출처 상한으로 넣지 못함
- 범위 경계 위반 의심:
    - f24: 휴머노이드 균형·인식과 자율주행 정밀도는 분류 원문 19장의 로봇 자체 지능·제어 쪽이므로 '연계 대상: '으로 표시함
    - f2: 서비스형 로봇 확산은 3. 경제성·조달·사업 모델의 범위와 겹치므로 이 영역에서는 시장 동향으로만 제안하고 3번 페이지 반영을 다음 실행 후보로 남김
    - f9·f10: 시장 규모 전망은 발행 기관의 산출물이므로 ROP 직접 범위가 아니라 인용 대상으로만 제안함(f23)
    - f13: 언어 모델 다중 로봇 연구는 L. AI·학습 기술의 방법이므로 44. 로봇 기반 모델·언어 모델 계획과 25. 작업 배정 — MRTA 에 함께 연결하도록 제안함(f25)
    - f12: VDA 5050 채택 경위는 21. 상호운용 표준·적합성과 겹치므로 이 영역에서는 표준이 시장 지형을 바꾼 사례로만 제안함
- 한계: 재실행 1회차. 반려 사유 1(f14: 벤더 문서만 근거로 한 사실 태그에 vendor_claim 없음): 직전 반환값(runs/2026-09-29-10/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로 예산 안에서 브리프를 다시 작성했고, 벤더 기능·성능 주장은 f14(Agility Digit)·f19(클로봇 크롬스·카멜레온) 두 건으로 두어 vendor_claim true·태그 추정·신뢰도 low·evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다(관련 finding: f14, f19). 이번 브리프의 finding 번호는 직전 반환값과 대응하지 않는다. web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-899~ref-913, 예약 구간 ref-899~ref-928 안) 상한 도달로 SYNAOS 의 VDA 5050·MassRobotics·Open-RMF 비교 글(벤더 문서), Foundation Models in Robotics 리뷰(arXiv 2604.15395), 인더스트리뉴스 클로봇·이노빌 협약 기사(2024-09-30, 제조 공장), 디지털데일리 스페이스뱅크 로보뷰엑스 기사(2025-09-19), IFR 'VDA 5050 explained'(2021), 시장조사 업체(nextmsc·Research and Markets)의 오케스트레이션 소프트웨어 시장 규모 페이지는 열었거나 검색 결과로 봤으나 넣지 못했다. 원문 열람 15건(모두 webfetch: IFR 보도자료 4건, Interact Analysis 2건, MassRobotics 페이지, arXiv 초록, Agility 발표, The Robot Report·로봇신문 3건·아시아경제·서울신문 기사), 재사용 1건(ref-004 Open-RMF, 공통 규칙의 참고 자료 번호 그대로이며 이번에 다시 열지 않아 fetched false). 주의: 같은 날 이전 실행 2026-09-29-09 가 ref-899·ref-900 을 다른 URL(KCI STNet 논문, RoSO/SMGI 논문)에 부여했으므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 하고, 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 IFR·Interact Analysis·MassRobotics 페이지가 전체 898건과 URL 이 겹칠 수 있다. 교차 확인 1건(f16: Agility 발표 / The Robot Report 보도). 신뢰도 high 없음(교차 확인된 f16 도 벤더 문서·기사 조합이라 medium). 분류 원문 핵심 질문(어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가)에는 시장 흐름 f1~f4·f6·f10, 동향 f5, 제품·업체 지형 f8·f11·f12·f20·f21, 로봇 종류 변화 f14~f18·f22, 연구 f13 으로 답했으며 결론은 '운송·물류 AMR 이 물량을 주도하는 가운데 제3자 다중 플릿 오케스트레이션 소프트웨어와 상호운용 표준이 제품 지형을 층으로 나누고, 휴머노이드와 언어 모델이 새 대상·새 방법으로 들어오고 있으나 그 규모는 회사 발표와 시장 전망 수준'이라는 추정(f21·f22)이다. 현장 유형: 물류창고(f8 정의, f16 GXO 교차 확인, f17 CJ대한통운), 제조 공장(f12 독일 자동차 산업, f18 현대차그룹 계획), 기타(f20 인천공항)를 확인했고 병원·상업 시설·가정·실외 사례는 없다. 국내 자료는 실태조사 요약(f6)·기본계획(f7)·클로봇(f19·f20)·CJ대한통운(f17)·현대차그룹(f18) 다섯 건이며 국내 학술 서베이는 찾지 못했다(고려대 관제 플랫폼 설계 논문 2022 는 검색 결과로만 보고 넣지 않음). 벤더 문서 1건(ref-909)과 기사에 실린 벤더 주장 1건(ref-870)은 모두 vendor_claim 으로 표시했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 용어집에 이미 있는 다중 플릿 오케스트레이션·플릿 관리 시스템·모바일 매니퓰레이터·기술 성숙도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음. 해결된 열린 질문 없음.
```

### runs/2026-09-29-09/research.md

```markdown
# 리서치 브리프 2026-09-29-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-09 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 7. 온톨로지 검증·변경 관리 |
| 대분류 | B. 로봇 온톨로지 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 역량 질문·온톨로지 피트폴·버전 IRI·온톨로지 진화 용어 없음(형상 제약 언어·의미적 버전 관리·회귀 시험·모델 검사·온톨로지 채우기는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 역량 질문 기반 완전성 확인, 추론기·피트폴 스캐너·형상 검증 같은 자동 평가, 버전 식별·호환성 표기, 변경 표현·탐지·영향 분석 네 갈래 모두 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — OWL 2 버전 IRI, W3C SHACL, OOPS!, IDTA 서브모델 템플릿 버전·폐기 규칙, 지식 그래프 변경 언어 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-147 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]
2. 역량 질문(competency question)을 SPARQL 질의·테스트로 형식화해 온톨로지의 완전성과 정확성을 확인하는 방법과 데이터셋·로봇 적용 사례는 무엇인가? (섹션 4·6·8 겨냥)
3. 추론기 일관성 검사, 피트폴 스캐너(OOPS!), 형상 검증(SHACL) 같은 자동 평가 도구는 각각 무엇을 잡아내고 검증 보고서를 어떤 구조로 내는가? (섹션 6·7 겨냥)
4. 온톨로지와 서브모델 템플릿의 버전은 어떻게 식별하고 이전 판과의 호환·비호환·폐기를 어떻게 표기하는가(OWL 2 버전 IRI, IDTA 서브모델 템플릿 규칙)? (섹션 4·7 겨냥)
5. 온톨로지 변경을 표현·탐지하고 의존 자원에 미치는 영향을 분석하는 연구(온톨로지 진화, 변경 언어, 버전 비교, 재구성 허용성)는 무엇이 보고되었으며, 언어 모델을 검증에 쓰는 방법은 어디에 연결되는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)
6. oq-147 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (섹션 6·11 겨냥)
7. 온톨로지 검증·변경 관리에서 ROP가 직접 맡을 것(역량 질문 목록·테스트 실행·검증 보고서·버전 식별·재검증 목록)과 제조사·표준 발행 기관에 맡길 것의 경계는 어디이며, 현장 유형별 사례와 국내 자료는 무엇인가? (섹션 5·9·10 겨냥, 한국 자료 우선)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Wiśniewski·Potoniec·Ławrynowicz·Keet(2018)는 온톨로지 개발에서 역량 질문(competency question) 사용을 촉진하기 위해 여러 도메인 온톨로지에 대한 역량 질문 234개와 그 SPARQL-OWL 번역을 공개하고, 언어·의미 분석으로 106개의 역량 질문 패턴을 46개의 SPARQL-OWL 질의 서명과 대응시켜 역량 질문의 형식화·실행·관리를 지원하는 벤치마크로 제시했다. | ref-890 | 아니오 | medium | 2018-11-23 | — | — |
| f2 | [사실] | Martorana·Urgese·Tiddi·Schlobach(2025)의 OntoBOT 은 SOMA·DOLCE 를 확장해 가정용 개인 서비스 로봇의 작업·행동·환경·능력을 통합 표현하는 온톨로지이며, 역량 질문으로 평가하고 TIAGo·HSR·UR3·Stretch 네 로봇에 대해 검증했다. | ref-891 | 아니오 | medium | 2025-09-26 | 가정 / 수행 자원 | — |
| f3 | [사실] | 고영만 외(한국문헌정보학회지 49권 3호, 2015)는 학술용어사전 STNet 에 온톨로지 구조를 도입하면서 Pellet 추론기로 TBox 를 검증해 생성한 추론규칙이 모두 참임을 확인하고 SPARQL 검색 시나리오로 의미 검색 성능을 평가했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 검증 연구다. | ref-899 | 아니오 | medium | 2015 | — | — |
| f4 | [사실] | 서로 다른 세 발행 주체(포즈난 공과대학교·케이프타운 대학교 연구진의 역량 질문 데이터셋, 암스테르담 자유대학교 연구진의 OntoBOT, 국내 문헌정보학 연구진의 STNet)가 역량 질문 또는 SPARQL 질의 실행과 추론기 검증으로 온톨로지의 완전성·정확성을 확인하는 방식을 각각 보고해, 이 영역의 역량 질문·질의 기반 검증이 한 곳 이상에서 확인된다. | ref-890, ref-891, ref-899 | 예 | medium | 2025-09-26 | — | — |
| f5 | [사실] | Poveda-Villalón·Gómez-Pérez·Suárez-Figueroa(IJSWIS, 2014)의 OOPS!(OntOlogy Pitfall Scanner!)는 기술 논리에 익숙하지 않은 도메인 전문가를 위해 온톨로지의 모델링 결함(피트폴)을 온라인에서 탐지하는 도구로, 693개 이상의 온톨로지를 경험적으로 분석해 만든 카탈로그를 구조·기능·사용성 프로파일링 차원으로 분류하고 피트폴마다 심각·중요·경미의 중요도를 둔다. | ref-889 | 아니오 | medium | 2014-04 | — | — |
| f6 | [사실] | W3C 형상 제약 언어(SHACL) 권고안(2017-07-20)은 데이터 그래프를 형상 그래프의 조건 집합으로 검증하는 언어이며, 검증 보고서는 적합 여부(sh:conforms), 개별 결과(sh:result), 심각도(sh:resultSeverity: Violation·Warning·Info)와 초점 노드·경로·값·원인 형상을 담는다. | ref-459 | 아니오 | medium | 2017-07-20 | — | — |
| f7 | [사실] | Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 작업에 대한 에이전트 자격·전제조건을 검사하고 SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다. | ref-880 | 아니오 | medium | 2025-04-30 | 병원 / 제약 | 원문 미열람 |
| f8 | [사실] | 서로 다른 두 발행 주체(W3C 의 SHACL 권고안, 그리스 연구진의 HERON)가 형상 제약 검증을 각각 정의하고 로봇 온톨로지 정책 검증에 적용해, 온톨로지 인스턴스 데이터의 제약 검증 수단으로서 SHACL 이 한 곳 이상에서 확인된다. | ref-459, ref-880 | 예 | high | 2025-04-30 | 병원 / 제약 | — |
| f9 | [사실] | Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성한 뒤 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행하고 사람이 최종 검토·수정만 하게 하여, 온톨로지 검증 단계에 자동 검사와 사람 검토를 결합했다. | ref-465 | 아니오 | medium | 2024-10-18 | 완료·인계 | 원문 미열람 |
| f10 | [사실] | Alharbi·Tamma·Payne·de Berardinis(2026)는 개방형(KimiK2·Llama 3.1·3.2)과 폐쇄형(Gemini 2.5 Pro·GPT 4.1) 언어 모델이 생성한 역량 질문을 가독성·입력 텍스트 관련성·구조적 복잡성 지표로 여러 도메인에서 평가해, 모델의 생성 프로필이 사용 사례에 따라 뚜렷이 달라진다고 보고했다. | ref-898 | 아니오 | medium | 2026-04-17 | — | — |
| f11 | [사실] | W3C OWL 2 구조 명세 2판(2012-12-11)은 온톨로지를 온톨로지 IRI 로 식별하고 특정 판을 버전 IRI 로 구분하며 같은 온톨로지 시리즈에서 정확히 하나의 버전만 현재 버전으로 보고, 온톨로지 주석 owl:priorVersion(이전 판 IRI)·owl:backwardCompatibleWith(호환되는 이전 판)·owl:incompatibleWith(양립 불가능한 이전 판)로 판 사이 관계를 표기한다. | ref-886 | 아니오 | medium | 2012-12-11 | — | — |
| f12 | [사실] | IDTA 서브모델 템플릿 공식 저장소 README 는 템플릿을 published·deprecated 폴더로 관리하고 판을 주버전·리비전·버그 수정으로 표기하며, 새 판 발행 6개월 뒤 이전 판을 deprecated 로 옮기되 그 템플릿은 계속 유효하나 버그 수정·개선·갱신을 더 제공하지 않는다고 정한다. | ref-439 | 아니오 | medium | 2026-09-29 | — | 원문 미열람 |
| f13 | [사실] | 서로 다른 두 발행 주체(W3C, IDTA)가 온톨로지와 서브모델 템플릿의 판 식별자와 이전 판과의 호환·폐기 관계 표기를 각각 정의해, '판 식별자 + 이전 판 관계 명시'가 온톨로지·모델 버전 관리의 관행으로 한 곳 이상에서 확인된다. | ref-886, ref-439 | 예 | high | 2026-09-29 | — | — |
| f14 | [사실] | Zablith 외(The Knowledge Engineering Review, 2013)의 프로세스 중심 서베이는 온톨로지 진화(ontology evolution)를 도메인 변화나 정보 시스템 요구에 대응해 온톨로지를 최신으로 유지하는 일로 정의하고, 전형적 접근이 자연어 처리·추론 등 여러 분야 기법을 결합한 다단계 과정으로 설계된다고 정리했다. | ref-888 | 아니오 | medium | 2013-08-28 | — | — |
| f15 | [사실] | Hegde 외(Database, 2025)의 지식 그래프 변경 언어 KGCL 은 온톨로지·지식 그래프의 변경을 '동의어 추가'·'계층 재배치' 같은 통제 자연어 명령으로 요청하거나 기술하는 표준 데이터 모델로, 패치·diff 개념을 빌려 미래 변경 요청과 기존 변경 기술에 모두 쓰이며 GitHub 온톨로지 저장소 자동화 에이전트와 BioPortal 변경 요청 인터페이스로 구현되었다. | ref-892 | 아니오 | medium | 2024-09-20 | — | — |
| f16 | [사실] | Qiang·Taylor·Wang(2024, 2026 개정)의 OM4OV 는 온톨로지 매칭 시스템을 온톨로지 버전 간 변경 비교에 재사용할 수 있지만 확장 없이는 왜곡된 측정을 낸다고 분석하고, 기존 정렬을 활용해 후보를 줄이는 교차 참조 메커니즘을 더한 버전 비교 프레임워크를 제안했다. | ref-893 | 아니오 | medium | 2026-08-31 | — | — |
| f17 | [사실] | 서로 다른 세 발행 주체(Zablith 외의 유럽 연구진 서베이, Hegde 외의 생물의학 온톨로지 연구진, 호주 국립대학교 계열 Qiang 외)가 온톨로지 변경의 정의·표현·탐지를 각각 다루어, 온톨로지 변경 관리가 별도 연구 분야로 존재함이 한 곳 이상에서 확인된다. | ref-888, ref-892, ref-893 | 예 | medium | 2026-08-31 | — | — |
| f18 | [사실] | Eichelberger·Weber(2024)는 2024년 2월 기준 IDTA 가 발표한 84개 명세 가운데 18개를 중간 메타모델로 변환해 5만 줄 이상의 API 코드·테스트를 자동 생성했으나 명세의 문법적 변동과 문제 때문에 수동 개입이 필요했다고 보고해, 표준 명세 자체의 변동성이 이를 소비하는 시스템의 재검증 부담이 됨을 보였다. | ref-895 | 아니오 | medium | 2024-06-20 | — | — |
| f19 | [사실] | Osmani(2026)는 로봇 서비스 온톨로지(RoSO)를 구조적 일반지능 모델(SMGI)의 의미 계층으로 두고, 서비스 재구성 뒤에도 서비스 기술이 유효하게 남기 위한 정체성 보존 재구성 기준과 지역적으로 허용되는 갱신이 전역적으로도 허용되는 조합 조건을 제시해 런타임 변경의 허용 여부를 판단하는 거버넌스를 제안했다. | ref-900 | 아니오 | low | 2026-05-05 | — | — |
| f20 | [사실] | Nasir 외(2026)의 OntoKG-EQ 는 다섯 개의 고정된 역량 질문으로 정당화된 핵심 온톨로지가 모든 클래스·속성·형상 제약·지표를 통제하고, 각 답에 관찰·증거·출처까지 추적하는 설명을 붙여 검증된 그래프에서 결정론적으로 만들며, 17명 패널 연구에서 증거 묶음이 인지된 신뢰도와 완전성을 크게 높였다고 보고했다. | ref-896 | 아니오 | medium | 2026-09-08 | 완료·인계 | — |
| f21 | [사실] | Abolhasani·Ba·He·Pan(2026)의 TRACE-KG 는 미리 정의한 온톨로지 없이 문맥이 풍부한 지식 그래프와 유도 스키마를 함께 만들면서 원문 근거에 대한 완전한 추적 가능성을 유지해, 사람 검토자가 자동 추출 결과를 원문과 대조해 검증할 수 있게 한다. | ref-897 | 아니오 | medium | 2026-06-15 | 완료·인계 | — |
| f22 | [추정] | oq-147 관련: 추출한 지식 항목마다 원문 근거를 붙여 검토자가 대조하게 하는 구성은 일반 문서 지식 그래프 추출(f20·f21)과 능력 온톨로지 생성의 사람 최종 검토(f9)에서 확인되지만, 로봇 매뉴얼·URDF 에서 뽑은 능력 항목에 매뉴얼의 절·줄 위치를 붙여 확정·반려하는 공개 구현은 이번 조사에서도 확인되지 않아 oq-147 은 부분 진전에 그친다. | ref-896, ref-897, ref-465 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f23 | [사실] | VDA 5050 공식 저장소(main, 3.0.0 판)의 팩트시트 JSON 스키마는 팩트시트 자체의 version 을 필수 속성으로 두고 선택 속성 mobileRobotConfiguration 에 하드웨어·소프트웨어 버전을 담아, 로봇 펌웨어·소프트웨어 판이 바뀐 사실을 등록 데이터에서 읽을 수 있는 자리를 제공한다. | ref-228 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f24 | [추정] | 확인한 출처 어디에도 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없으며, 판 식별·호환 표기(f11·f12), 변경의 표현·탐지(f15·f16), 재구성 허용 판단(f19), 펌웨어 판 보고 자리(f23)가 흩어져 있어 ROP 는 이들을 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다. | ref-886, ref-439, ref-892, ref-893, ref-228 | 아니오 | low | 2026-09-29 | 예외·성과 | — |
| f25 | [추정] | 확인한 자료를 종합하면 7. 온톨로지 검증·변경 관리에서 ROP가 직접 맡을 범위는 능력 온톨로지의 역량 질문 목록과 그 SPARQL 테스트 실행 기록, SHACL 형상과 검증 보고서, 추론기 일관성 검사, 온톨로지 판 식별자와 이전 판 관계 표기, 변경 기술(변경 언어)과 영향받는 작업·현장의 재검증 목록이며, 원문 근거를 붙인 검토·확정 기록은 4. 이기종 로봇 등록의 검토·승인과 같은 기록을 공유해야 할 것으로 보인다. | ref-890, ref-459, ref-886, ref-892 | 아니오 | low | 2026-09-29 | — | — |
| f26 | [추정] | 연계 대상: 로봇 펌웨어·소프트웨어의 릴리스 관리 자체와 표준 발행 기관의 템플릿 개정·폐기 일정은 분류 원문 19장의 로봇 자체 지능·제어와 업종·규격 측 소유 사항이므로, 이종 제조사를 잇는 ROP 는 팩트시트의 판 정보와 템플릿 폐기 통보를 받아 온톨로지 재검증을 촉발하는 데 그치고 펌웨어 검증과 템플릿 유지보수는 제조사·IDTA 에 맡겨야 할 것으로 보인다. | ref-228, ref-439 | 아니오 | low | 2026-09-29 | 제약 | — |
| f27 | [추정] | 이 영역은 등록 검토·승인 기록을 주는 4. 이기종 로봇 등록, 검증 대상 어휘를 주는 5. 로봇 능력·작업 표현, 검증된 연결만 실행하는 6. 온톨로지 기반 시스템·로봇 연동을 앞뒤로 두고, 판 규칙은 21. 상호운용 표준·적합성과 57. 자산·소프트웨어 수명주기 관리, 테스트·형식 검증 방법은 54. 시험·형식 검증·벤치마크에 이어지며, 언어 모델로 역량 질문·온톨로지를 생성·검증하는 방법(f9·f10)은 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에도 연결된다. | ref-439, ref-459, ref-465, ref-898 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-886 | W3C (OWL Working Group) | OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition) | 2012-12-11 | 표준 | high | 2026-09-29 | https://www.w3.org/TR/owl2-syntax/ | 아니오 |
| ref-459 | W3C (RDF Data Shapes Working Group) | Shapes Constraint Language (SHACL) | 2017-07-20 | 표준 | high | 2026-09-29 | https://www.w3.org/TR/shacl/ | 아니오 |
| ref-888 | Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review) | Ontology evolution: a process-centric survey | 2013-08-28 | 논문 | medium | 2026-09-29 | https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article | 아니오 |
| ref-889 | Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)) | OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation | 2014-04 | 논문 | medium | 2026-09-29 | https://oa.upm.es/35873/ | 아니오 |
| ref-890 | Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M. | Competency Questions and SPARQL-OWL Queries Dataset and Analysis | 2018-11-23 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1811.09529 | 아니오 |
| ref-891 | Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam) | An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics | 2025-09-26 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2509.22434 | 아니오 |
| ref-892 | Hegde, H. 외 (Database, Oxford) | A Change Language for Ontologies and Knowledge Graphs | 2024-09-20 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2409.13906 | 아니오 |
| ref-893 | Qiang, Z., Taylor, K., & Wang, W. | OM4OV: Leveraging Ontology Matching for Ontology Versioning | 2024-09-30 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2409.20302 | 아니오 |
| ref-439 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | submodel-templates — IDTA Submodel Templates for AAS (README) | 미확인 | 표준 | medium | 2026-09-29 | https://github.com/admin-shell-io/submodel-templates | 예 |
| ref-895 | Eichelberger, H., & Weber, A. | Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible? | 2024-06-20 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.14470 | 아니오 |
| ref-896 | Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M. | OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying | 2026-09-08 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2609.08869 | 아니오 |
| ref-897 | Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026) | Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation | 2026-04-03 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2604.03496 | 아니오 |
| ref-898 | Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J. | Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models | 2026-04-17 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2604.16258 | 아니오 |
| ref-899 | 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)) | 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구 | 2015 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617 | 아니오 |
| ref-900 | Osmani, A. | From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance | 2026-05-05 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2605.08185 | 아니오 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-10-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-880 | Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel) | HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics | 2025-04-30 | 논문 | medium | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/ | 예 |
| ref-228 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050/json_schemas/factsheet.schema (main) | 미확인 | 표준 | high | 2026-09-29 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/robot-ontology/ontology-verification-and-change-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4(역량 질문·질의 기반 검증이 여러 곳에서 확인), f18(표준 명세 변동이 재검증 부담), f24(개정 시 영향·재검증 절차는 흩어져 있어 ROP 가 설계해야 함) / 섹션 4: f1(역량 질문·SPARQL-OWL), f5(피트폴·중요도), f6(형상 검증 보고서), f11(온톨로지 IRI·버전 IRI·이전 판 주석), f14(온톨로지 진화) / 섹션 5: 가정 — f2(OntoBOT, 네 로봇 역량 질문 평가, 현장 배치 아님을 명시), 병원 — f7(HERON 의료센터 시뮬레이션 정책 검증, 임상 배치 아님), 제조 공장·물류창고·상업 시설·실외 사례는 확인되지 않음을 서술 / 섹션 6: 역량 질문 검증 f1·f2·f3·f4, 자동 평가 f5·f6·f8, 언어 모델 결합 검증 f9·f10(교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 함께 연결), 버전·호환 표기 f11·f12·f13, 변경 표현·탐지·허용성 f15·f16·f17·f19, 원문 근거 검토 f20·f21·f22 / 섹션 7: f11(OWL 2), f6(SHACL), f5(OOPS!), f12(IDTA 서브모델 템플릿 규칙), f15(KGCL), f23(VDA 5050 팩트시트 판 정보) / 섹션 8: f1, f2, f5, f14, f15, f16, f18, f19, f20, f21, 국내 f3 / 섹션 9: f25(직접 범위: 역량 질문 목록·테스트 기록·형상·검증 보고서·판 식별·재검증 목록), f26(연계 대상: 펌웨어 릴리스·템플릿 폐기 일정) / 섹션 10: f27 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리, 63. 병원·의료(f7), 65. 가정·공동주택(f2) / 섹션 11: 기존 oq-147(f22 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 57. 자산·소프트웨어 수명주기 관리 페이지에 f12·f23 반영, 54. 시험·형식 검증·벤치마크 페이지에 f1·f6 반영, 트랙 manual-capability-ontology 단계 5(완전성·정확성 검증)에 f1·f4·f5·f6 참고, 단계 6(변경 관리)에 f11·f12·f15 참고. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 역량 질문 | Competency Question (CQ) | 온톨로지가 답할 수 있어야 하는 질문으로 요구사항을 적은 것으로, SPARQL 같은 질의로 형식화해 온톨로지가 요구를 충족하는지 검증하는 데 쓴다. |
| 온톨로지 피트폴 | Ontology Pitfall | 온톨로지 모델링에서 흔히 생기는 결함 유형으로, 피트폴 스캐너(OOPS!)가 구조·기능·사용성 차원의 카탈로그와 심각·중요·경미 중요도로 자동 탐지한다. |
| 버전 IRI | Version IRI (owl:versionIRI) | OWL 2 에서 같은 온톨로지 IRI 를 공유하는 온톨로지 시리즈 가운데 특정 판을 식별하는 IRI 로, 이전 판·호환·비호환 주석과 함께 온톨로지 버전 관리에 쓴다. |
| 온톨로지 진화 | Ontology Evolution | 도메인 변화나 정보 시스템 요구 변화에 대응해 온톨로지를 최신 상태로 유지하는 활동으로, 변경 감지·표현·적용·영향 관리를 포함하는 다단계 과정으로 다뤄진다. |

## 열린 질문

새로 생긴 질문:

- 로봇 능력 온톨로지에 대해 펌웨어·매뉴얼 개정을 감지해 영향받는 작업·현장을 찾고 재검증 대기열에 넣는 절차를 구현한 공개 구현이나 현장 사례가 있는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 57. 자산·소프트웨어 수명주기 관리, 4. 이기종 로봇 등록 | 근거: f24 | 종류: 일반
- 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 54. 시험·형식 검증·벤치마크, 36. 가상 시운전·실제 상황 재현 | 근거: f25 | 종류: 일반
- 국내에서 역량 질문·추론기·SHACL 로 로봇 온톨로지를 검증하거나 버전을 관리한 연구·현장 사례가 있는가(이번 조사에서 확인된 국내 자료는 학술용어사전 온톨로지 검증 연구 1건이다)? | 관련 영역: 7. 온톨로지 검증·변경 관리, 5. 로봇 능력·작업 표현 | 근거: f3 | 종류: 일반
- IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 21. 상호운용 표준·적합성, 4. 이기종 로봇 등록 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 4
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - Grüninger·Fox(1995) 'Methodology for the Design and Evaluation of Ontologies' 원문 PDF(토론토대학교 EIL)는 텍스트 추출이 되지 않고 Semantic Scholar API 는 429 로 서지를 확인하지 못해 출처에 넣지 않음 — 역량 질문의 원 제안자 인용은 스토리텔러가 쓰지 말 것
    - Themis(UPM 온톨로지 공학 그룹의 요구사항 기반 온톨로지 검증 도구)는 도구 페이지를 열었으나 개발 기관·논문을 페이지에서 확인하지 못했고 논문 PDF·Semantic Scholar 페이지는 연결 끊김·빈 응답으로 미확인 — 출처 제외
    - Köcher·Vieira da Silva·Fay 'Constraint Checking of Skills using SHACL'(INDIN 2021, 제조 스킬 검증)은 검색 결과 요약에서만 확인되고 HSU 페이지 404·Semantic Scholar 429 로 서지 미확인 — 제조 공장 현장 유형 사례 미확보
    - IDTA 'How to write a SMT v1.1' 지침 PDF 와 Dibowski 'Full Traceability and Provenance for Knowledge Graphs'(FOIS 2024) PDF 는 텍스트 추출 실패, MDPI 'Grounded Knowledge Graph Extraction via LLMs'(Computers 15(3):178)는 403 — oq-147 의 로봇 문서 적용 사례 후보 미열람
    - f14 Zablith 서베이의 진화 단계 이름은 초록 페이지에 없어 미확인(전문 PDF 403)
    - f16 OM4OV·f18 Eichelberger 의 정량 결과(검색 요약의 'AASX 파일 44%만 대상 명세 판 표시')는 초록에 없어 claim 에 넣지 않음
    - f2 OntoBOT 은 네 로봇에 대한 평가이며 가정 현장 배치 여부는 초록에서 확인하지 못함(site_type 은 출처가 밝힌 적용 대상 기준)
    - f7 HERON·f9 Vieira da Silva·f23 팩트시트는 재사용 출처로 이번에 다시 열지 않음
    - oq-147 미해결(f22 부분 진전)
    - f4·f8·f13·f17 외 모든 finding 교차 확인 실패(표준·연구마다 발행 주체 한 곳)
- 범위 경계 위반 의심:
    - f26: 펌웨어 릴리스 관리와 표준 템플릿 유지보수는 분류 원문 19장의 로봇 자체 지능·제어와 규격 발행 기관 소유이므로 '연계 대상: '으로 표시함
    - f7: HERON 의 역할 기반 권한 정책 검증은 51. 인증·권한·격리·48. 안전·위험 관리와 겹치므로 이 영역에서는 SHACL 검증 적용 사례로만 제안함
    - f9·f10·f20·f21: 언어 모델 기반 온톨로지 생성·역량 질문 생성·지식 그래프 추출은 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f27)
    - f18: IDTA 명세의 코드 생성은 21. 상호운용 표준·적합성의 범위와 겹치므로 표준 명세 변동이 재검증 부담이 된다는 근거로만 제안함
    - f20: 금융 분석 도메인의 지식 그래프이므로 역량 질문 통제·증거 추적 구성의 선례로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-886~ref-900, 예약 구간 안) 상한 도달로 Frontiers 'A survey of ontology-enabled processes for dependable robot autonomy'(2024, 32편 검토 — 연 원문에 검증·변경 관리 서술이 없어 finding 으로 쓰지 않음), Themis, Köcher 외 SHACL 스킬 검증, IDTA SMT 작성 지침, Dibowski 추적성 논문, MDPI 근거 기반 추출 논문은 넣지 못했다. 원문 열람 15건(github_raw 1: IDTA 서브모델 템플릿 README, webfetch 14: W3C 권고안 2건, arXiv 초록 9건, Cambridge 초록, UPM 기관 저장소 초록, KCI 초록), 재사용 3건(ref-465·ref-880 는 2026-09-29-08, ref-228 은 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않아 fetched false). 교차 확인 4건(f4: 포즈난·케이프타운/암스테르담/국내, f8: W3C/그리스 연구진, f13: W3C/IDTA, f17: Zablith 외/Hegde 외/Qiang 외). 신뢰도 high 는 f8·f13 두 건(각각 이번 실행에서 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지)에는 완전성·정확성 쪽은 f1~f8(역량 질문·질의 실행, 추론기, 피트폴 스캐너, SHACL)과 f9·f10(언어 모델 결합 검증)으로, 변경 쪽은 f11~f19·f23(판 식별·호환 표기, 변경 표현·탐지, 재구성 허용성, 팩트시트 판 정보)으로 답했으며 결론은 '검증 수단과 판 표기 규칙은 여러 곳에서 확인되지만 로봇 능력 온톨로지에 대해 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차와 원문 절·줄 근거를 붙인 검토 구현은 확인되지 않았다'는 추정(f22·f24)이다. 분류 원문 1절의 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)를 정의한 출처는 찾지 못해 열린 질문으로 올렸다. 현장 유형: 가정(f2 OntoBOT 평가), 병원(f7 HERON 시뮬레이션 재인용)만 확인했고 제조 공장·물류창고·상업 시설·실외·기타 사례는 없다(제조 사례 후보 Köcher 외는 서지 미확인). 국내 자료는 KCI 논문(f3, 2015, 문헌정보학 온톨로지) 한 건이며 로봇 온톨로지 검증의 국내 사례는 찾지 못했다. 벤더 문서·벤더 주장 없음. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 용어집에 이미 있는 형상 제약 언어·의미적 버전 관리·회귀 시험·모델 검사·온톨로지 채우기·런타임 검증은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-147 은 f22 로 부분 진전만). 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 전체 885건과의 URL 중복을 대조하지 못했으므로 W3C OWL 2·SHACL·IDTA 저장소·arXiv 2406.07962 등은 퍼블리셔가 기존 id 로 합칠 수 있다.
```
