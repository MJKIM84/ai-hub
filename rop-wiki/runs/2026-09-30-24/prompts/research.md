(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-24
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 60. 노동·수용성·접근성 (P. 거버넌스·법규·사회)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1264
- 새 출처 id 구간: ref-1264 ~ ref-1293 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1264 부터 순서대로 쓰고 ref-1293 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-24/target.json

```json
{
  "run_id": "2026-09-30-24",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 133,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 60,
    "area_name": "60. 노동·수용성·접근성",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=60"
}
```

### docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md

```markdown
---
title: "60. 노동·수용성·접근성"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 60
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 60. 노동·수용성·접근성

# 60. 노동·수용성·접근성

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]

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

### docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md (요약)

```markdown
# 58. 다사업자 책임·계약·데이터

소속 대분류: P. 거버넌스·법규·사회 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

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
```

### docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md (요약)

```markdown
# 59. 법·규제·보험·라이선스

소속 대분류: P. 거버넌스·법규·사회 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1179건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 330개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [60] 에 걸린 3건 / 전체 271건)

```markdown
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
- oq-188 [열림] 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (영역 66, 60, 16)
- oq-266 [열림] 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? (영역 40, 56, 60)
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

### runs/2026-09-30-23/research.md

```markdown
# 리서치 브리프 2026-09-30-23

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-23 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 59. 법·규제·보험·라이선스 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 운행안전인증, 운용자, 책임보험·공제, 제조물(소프트웨어 포함 여부), 사이버복원력법 보고 의무, SBOM·SPDX, 패키지 라이선스 선언 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 실외(한국 보도 통행 로봇, 미국 주법 개인 배송 장치)·산업 사업장(산업용 로봇 안전검사) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 인증·보험 조건의 운영 제약 반영, 사고·취약점 보고 체계, 라이선스 선언·SBOM 관리 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법·도로교통법, 산업안전보건법 안전검사, EU 기계류 규정, EU 제조물책임지침, 한국 제조물책임법, 인공지능 기본법, EU 사이버복원력법, 개인정보보호법 제25조의2, ROS 2 REP 2004, SPDX(ISO/IEC 5962) 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-143, oq-173, oq-186, oq-187, oq-231, oq-239, oq-249, oq-250, oq-262 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]
2. 실외에서 로봇을 운행할 때 한국(지능형로봇법·도로교통법의 운행안전인증·운용자 의무·보험)과 해외(미국 주법의 개인 배송 장치)는 무엇을 요구하며, 운행안전인증의 심사항목과 인증 대상은 어떻게 정해져 있는가? (섹션 5·7 겨냥, oq-186·oq-187 관련, 한국 자료 우선)
3. 로봇 사고의 책임을 정하는 제조물 책임 법제는 소프트웨어·AI를 어떻게 다루는가(EU 개정 제조물책임지침, 한국 제조물책임법)? (섹션 4·6·7 겨냥)
4. AI 규제와 사이버보안 규제(한국 인공지능 기본법, EU 사이버복원력법)는 로봇 운영 사업자에게 어떤 의무와 시행 일정을 두는가? (섹션 7 겨냥, oq-143 관련)
5. 산업 사업장에서 로봇을 쓸 때 적용되는 기계·안전 규제(산업안전보건법 안전검사, EU 기계류 규정)는 무엇인가? (섹션 5·7 겨냥)
6. 오픈소스·SDK·3D 자산의 라이선스를 지키기 위한 선언·목록화 수단(ROS 2 패키지 라이선스 규칙, SPDX·SBOM, 시뮬레이션 모델 데이터베이스의 라이선스 표기)은 무엇인가? (섹션 6·7 겨냥)
7. 법·규제·보험·라이선스에서 ROP가 직접 맡을 것과 제조사·운영자·보험사·법무에 맡길 것의 경계는 어디이며 어느 영역(개인정보 법 포함, oq-262 관련)과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 한국에서는 개정 지능형로봇법과 도로교통법이 2023-11-17부터 시행되어, 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하의 실외이동로봇이 보행자 지위로 보도를 통행할 수 있게 되었다. | ref-1234, ref-1241 | 예 | high | 2023-11-16 | 실외 / 제약 | — |
| f2 | [사실] | 개정 도로교통법은 실외이동로봇을 조작·관리하는 운용자에게 정확한 조작과 안전한 운용 의무를 두고, 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지키게 하며, 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있게 했다. | ref-1234 | 아니오 | medium | 2023-11-16 | 실외 / 수행 자원 | — |
| f3 | [사실] | 한국에서 운행안전인증을 받은 실외이동로봇을 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 하며, 정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다. | ref-1234, ref-1240 | 예 | medium | 2023-11-16 | 실외 / 제약 | — |
| f4 | [사실] | 실외 사례(한국): 한국로봇산업협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고, 첫 가입 기업은 뉴빌리티·로보티즈였다. | ref-1240 | 아니오 | low | 2024-02-08 | 실외 / 예외·성과 | — |
| f5 | [사실] | 한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 근거하며, 인증 대상은 실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체이고, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다. | ref-1241 | 아니오 | medium | 2026-09-30 | 실외 / 수행 자원 | — |
| f6 | [사실] | 2023-07 한국로봇산업진흥원이 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다. | ref-1242 | 아니오 | low | 2023-07-28 | 실외 / 제약 | — |
| f7 | [추정] | f5와 f6을 비교하면 실외이동로봇 운행안전인증의 심사 체계가 제정 당시 16가지 안전기준에서 현재 8개 심사항목으로 재편된 것으로 보이나, 개정 시점·근거 고시와 알림음·등화장치·경사로 같은 기존 기준이 어느 항목에 흡수됐는지는 확인하지 못했다. | ref-1241, ref-1242 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f8 | [사실] | 실외 사례(미국): 버지니아주법 §46.2-908.1:1은 개인 배송 장치(PDD)가 보도·횡단보도에서 시속 10마일 이하로 운행하고 운영자를 식별하는 표시를 달게 하며, 운영자에게 장치 운행으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지하게 한다. | ref-1248 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f9 | [사실] | EU 개정 제조물책임지침(Directive (EU) 2024/2853)은 2026-12-09 이후 시장에 출시되거나 사용이 개시된 제품에 적용되며, 독립형 소프트웨어·디지털 제조 파일·통합 디지털 요소를 제품에 포함하고, 출시 뒤 제품을 실질적으로 변경한 자를 제조자로 볼 수 있게 한다. | ref-1235 | 아니오 | medium | 2026-03-23 | 예외·성과 | — |
| f10 | [사실] | 같은 지침에서는 결함 있는 소프트웨어나 필요한 보안 업데이트 미제공도 책임 원인이 될 수 있고, 청구인이 그럴듯한 청구를 하면 피고에게 증거 공개를 명할 수 있으며, 공개 의무 불이행 등의 경우 결함이 추정된다. | ref-1235 | 아니오 | medium | 2026-03-23 | 예외·성과 | — |
| f11 | [사실] | 한국 제조물책임법은 제조물을 제조되거나 가공된 동산으로 정의해 소프트웨어를 명시적으로 포함하지 않으므로, 사람의 개입 없이 동작한 자율 시스템 사고에서 소프트웨어 개발자가 제조물 책임을 지는지가 쟁점으로 남아 있다. | ref-1243 | 아니오 | medium | 2024-07 | 예외·성과 | — |
| f12 | [사실] | EU 기계류 규정(Regulation (EU) 2023/1230)은 2027-01-20부터 적용되며, 출시된 기계에 실질적 변경을 한 자를 제조자로 보아 제조자 의무를 지게 한다. | ref-1359, ref-1350 | 아니오 | medium | 2023-06-14 | 제약 | 원문 미열람 |
| f13 | [사실] | 한국 인공지능 기본법은 2026-01-22 시행되었고, 정부는 최종 의사결정 권한을 사람이 가지는 경우 고영향 인공지능 분류에서 제외된다고 설명하며, 과태료 등 규제를 최소 1년 이상 유예하고 지원데스크를 운영한다고 밝혔다. | ref-1245 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f14 | [사실] | EU 사이버복원력법(CRA)에 따라 2026-09-11부터 디지털 요소 제품의 제조자는 실제 악용되는 취약점과 중대한 보안 사고를 ENISA 단일 보고 플랫폼을 통해 24시간 안에 조기 경보, 72시간 안에 통지, 이후 최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 1개월)해야 한다. | ref-1236 | 아니오 | medium | 2026-09-11 | 예외·성과 | — |
| f15 | [사실] | 한국 개인정보보호법 제25조의2는 착용형·휴대형·부착·거치형 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영할 때 불빛·소리·안내판·안내방송 등으로 촬영 사실을 표시하게 하고, 표시했는데 거부 의사가 없는 경우 등에 한해 촬영을 허용한다. | ref-1244 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f16 | [사실] | 고용노동부는 2017-10-29부터 산업용 로봇과 컨베이어를 산업안전보건법상 안전검사 대상에 추가해, 이미 쓰던 설비는 2018-12-31까지 최초 안전검사를 받게 했고, 그 근거로 최근 5년간 산업용 로봇 재해자 221명을 들었다. | ref-1247 | 아니오 | medium | 2017-10-26 | 제약 | — |
| f17 | [사실] | ROS 2 개발자 가이드는 각 패키지에 LICENSE 파일(대개 Apache 2.0, 기존 허용형 라이선스가 있으면 예외)을 두고 모든 소스 파일에 라이선스·저작권 문구를 넣어 자동 린터(ament_copyright)로 검사하게 한다. | ref-1246 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f18 | [사실] | ROS 2 패키지 품질 등급을 정한 REP 2004(2019-12-17 작성, Active)는 품질 수준 1~4 패키지에 선언된 라이선스와 프로젝트 안의 저작권 명시·모든 저자 표기를 요구하고, 수준 5에는 권장만 한다. | ref-1237 | 아니오 | medium | 2019-12-17 | 작업 대상 | — |
| f19 | [사실] | SPDX는 소프트웨어 자재명세서(SBOM)의 출처·라이선스·보안 정보를 교환하는 개방 표준으로 ISO/IEC 5962:2021로 인정되었고, SPDX 라이선스 목록은 라이선스 식별자·예외·라이선스 표현식 문법을 제공한다. | ref-1238 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f20 | [사실] | Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 데이터베이스 안 모델의 라이선스를 지정하고 CC BY 3.0 Unported를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다. | ref-1239 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가)의 답은 현장마다 다르며, 실외는 운행 규정·운행안전인증·운용자 의무·의무 보험(한국 f1~f5, 미국 버지니아 f8), 산업 사업장은 기계 안전 규제(한국 안전검사 f16, EU 기계류 규정 f12), 공통으로 AI·사이버보안·개인정보 규제(f13·f14·f15), 사고 책임 법제(f9~f11), 오픈소스·3D 자산 라이선스(f17~f20)가 겹치는 구조로 보이고, 병원·상업 시설·가정 실내 로봇에 특화된 운행 규정은 이번 조사에서 확인하지 못했다. | ref-1234, ref-1241, ref-1248, ref-1247, ref-1359, ref-1245, ref-1236, ref-1244, ref-1235, ref-1243, ref-1246, ref-1238, ref-1239 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 59. 법·규제·보험·라이선스에서 ROP가 직접 맡을 범위는 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기며, 촬영 표시 같은 규제 상태를 운영 조건으로 확인하고, 플랫폼 배포물의 라이선스·SBOM 목록을 관리하는 일로 보인다. | ref-1241, ref-1234, ref-1236, ref-1244, ref-1238, ref-1246 | 아니오 | low | 2026-09-30 | 제약 | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장의 업종별 조건 경계에 따라 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자), 사업장 안전검사(사업주)는 외부가 맡고, ROP는 그 결과를 작업·경로·권한 제약으로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다. | ref-1241, ref-1240, ref-1243, ref-1235, ref-1244, ref-1247 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f24 | [추정] | 이 영역은 인증·안전검사의 50. 안전 표준·인증·사고 조사(f5·f16), 실외 운행 규정의 66. 실외(f1~f8), 촬영 표시의 53. 개인정보·영상 데이터(f15), 실질적 변경·책임 배분의 58. 다사업자 책임·계약·데이터(f9·f12), AI 규제의 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영(f13), 취약점 보고의 52. 통신 보호·위협 관리·감사(f14), 라이선스·SBOM·보안 업데이트의 57. 자산·소프트웨어 수명주기 관리(f10·f17~f19), 인증 정보 등록의 4. 이기종 로봇 등록(f5), 운행 구역 규정의 16. 장소 의미·지도 관리(f6), 3D 자산 라이선스의 36. 가상 시운전·실제 상황 재현(f20), 보험료 부담의 3. 경제성·조달·사업 모델(f4)과 이어진다. | ref-1241, ref-1247, ref-1234, ref-1244, ref-1235, ref-1359, ref-1245, ref-1236, ref-1246, ref-1237, ref-1238, ref-1242, ref-1239, ref-1240 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1234 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 (제목 일부만 확인) | 2023-11-16 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 아니오 |
| ref-1235 | Gibson Dunn | EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains | 2026-03-23 | 업계 보고서 | medium | 2026-09-30 | https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/ | 아니오 |
| ref-1236 | European Commission (Shaping Europe's digital future) | Cyber Resilience Act - Reporting obligations | 2026-09-11 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 아니오 |
| ref-1237 | ROS (ros-infrastructure/rep) | REP 2004 -- Package Quality Categories | 2019-12-17 | 오픈소스 문서 | high | 2026-09-30 | https://ros.org/reps/rep-2004.html | 아니오 |
| ref-1238 | SPDX Project (Linux Foundation) | SPDX Overview | 미확인 | 표준 | high | 2026-09-30 | https://spdx.dev/about/overview/ | 아니오 |
| ref-1239 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://classic.gazebosim.org/tutorials?tut=model_structure | 아니오 |
| ref-1240 | 지디넷코리아 | "실외 이동로봇 필수보험 94% 저렴하게" | 2024-02-08 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240208201432 | 아니오 |
| ref-1241 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-1242 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부만 확인) | 2023-07-28 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1243 | 김·장 법률사무소 | 인공지능, 소프트웨어 결함으로 인한 제조물책임의 … (제목 일부만 확인) | 2024-07 | 업계 보고서 | medium | 2026-09-30 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930 | 아니오 |
| ref-1244 | 법제처 찾기쉬운 생활법령정보 | 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인) | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3 | 아니오 |
| ref-1245 | 대한민국 정책브리핑 (과학기술정보통신부) | '인공지능기본법' 22일 시행…생성형 AI 결과물 … (제목 일부만 확인) | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148958380 | 아니오 |
| ref-1246 | Open Robotics (ROS 2 Documentation) | ROS 2 developer guide | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html | 아니오 |
| ref-1247 | 고용노동부 | 산업용 로봇과 컨베이어도 안전검사 필수 | 2017-10-26 | 정부·연구기관 | medium | 2026-09-30 | https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135 | 아니오 |
| ref-1248 | Commonwealth of Virginia (Code of Virginia) | § 46.2-908.1:1. Personal delivery devices | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/ | 아니오 |
| ref-1350 | European Parliament and Council of the European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery | 2023-06-14 | 정부·연구기관 | medium | 2026-09-30 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-1359 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(핵심 질문 답, 추정), f9·f11(소프트웨어 사고 책임의 법적 공백·변화), f14(보고 기한) / 섹션 4: 운행안전인증·관제장치 조합 f1·f5, 운용자 f2, 책임보험·공제 f3, 제조물(소프트웨어 포함 여부) f9·f11, 실질적 변경 f9·f12, 사이버복원력법 보고 f14, 이동형 영상정보처리기기 f15, 라이선스 선언·SBOM f17~f19 / 섹션 5: 실외 — f1·f5(제약·수행 자원, 한국)·f2(수행 자원)·f3(제약)·f4(예외·성과)·f6·f7(제약), f8(제약, 미국 버지니아). 산업 사업장 안전검사 f16 은 출처가 현장 유형을 밝히지 않아 현장 유형 미명시로 서술. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했음을 명시 / 섹션 6: 인증·보험 조건의 운영 제약 반영 f5·f3·f8, 사고·취약점 보고 체계 f14·f10, 라이선스 선언·자동 검사·SBOM f17~f20 / 섹션 7: 지능형로봇법·도로교통법 f1~f7, 버지니아 PDD 주법 f8, EU 제조물책임지침 f9·f10, 한국 제조물책임법 f11, EU 기계류 규정 f12, 인공지능 기본법 f13, EU 사이버복원력법 f14, 개인정보보호법 제25조의2 f15, 산업안전보건법 안전검사 f16, ROS 2 개발자 가이드·REP 2004 f17·f18, SPDX(ISO/IEC 5962) f19, Gazebo 모델 라이선스 f20 / 섹션 8: f9·f11·f14 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66 / 섹션 11: 기존 oq-143·oq-173·oq-186·oq-187·oq-231·oq-239·oq-249·oq-250·oq-262(모두 미해결 유지; oq-186 은 f5·f6·f7 로 현재 8개 항목만 확인, oq-143 은 f13 으로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 66. 실외 페이지에 f1~f8, 57. 자산·소프트웨어 수명주기 관리 페이지에 f17~f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 제조물책임 | Product Liability | 제조물의 결함으로 생명·신체·재산에 손해가 생겼을 때 제조업자 등이 과실과 관계없이 배상 책임을 지는 제도로, 한국은 제조물책임법, EU는 개정 제조물책임지침(2024/2853)이 정하며 EU 지침은 소프트웨어를 제품에 포함한다. |
| 사이버복원력법 | Cyber Resilience Act (CRA) | 디지털 요소를 가진 제품의 사이버보안 요구사항과 제조자의 취약점·중대 사고 보고 의무(2026-09-11부터)를 정한 EU 규정이다. |
| 소프트웨어 자재명세서 | Software Bill of Materials (SBOM) | 소프트웨어를 이루는 구성 요소와 그 출처·버전·라이선스·보안 정보를 기계가 읽을 수 있게 나열한 목록으로, SPDX(ISO/IEC 5962:2021) 같은 형식으로 교환한다. |
| 오픈소스 소프트웨어 스튜어드 | Open-source Software Steward | EU 사이버복원력법에서 상업 활동에 쓰이는 자유·오픈소스 소프트웨어의 개발을 체계적·지속적으로 지원하는 법인으로, 제조자보다 가벼운 사이버보안·보고 의무를 진다. |

## 열린 질문

새로 생긴 질문:

- 한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가? | 관련 영역: 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f3 | 종류: 일반
- EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f9 | 종류: 일반
- 국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f11 | 종류: 일반
- 로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가? | 관련 영역: 59. 법·규제·보험·라이선스, 52. 통신 보호·위협 관리·감사, 57. 자산·소프트웨어 수명주기 관리 | 근거: f14 | 종류: 일반
- 시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 36. 가상 시운전·실제 상황 재현, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 2
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f3 실외이동로봇 책임보험 가입금액(사망 1억5천만원·부상 3천만원·재물 10억원)은 검색 요약에만 있고 시행규칙 원문을 열지 못해 finding 에서 뺌
    - f4 단체보험 보장 한도 미확인
    - f7 운행안전인증 심사항목이 16가지에서 8개로 바뀐 개정 시점·근거 고시 미확인(oq-186). 검색 요약에 '다시 16개로 재정의'라는 서술이 있었으나 인증기관 페이지(2026-09-30 확인)는 8개를 나열해 확인되지 않은 요약은 쓰지 않음
    - f9·f10 EU 제조물책임지침은 EUR-Lex 원문·PDF 본문이 비어 열지 못해 법률사무소 해설 기준. 오픈소스 예외 조항 미확인
    - f11 김·장 뉴스레터 PDF 본문 미열람, 웹 요약 기준
    - f13 고영향 인공지능의 법정 영역 목록과 사업자 책무 조문은 시행령·가이드라인 원문을 열지 못해 미확인(신·김 뉴스레터 403)
    - f14 오픈소스 스튜어드 보고 의무 시점(2027-12-11)은 집행위원회 페이지 한 곳 기준이며, 제조자 보고 의무 시점과 같다고 적은 다른 요약과 교차 확인하지 못함
    - f15 개인정보보호법 제25조의2 시행일은 출처 요약이 2023-09-15(검색 요약)와 2024-12-03(생활법령 페이지 요약)으로 달라 finding 에 넣지 않음
    - f16 산업용 로봇 정기 안전검사 주기(최초 3년 이내, 이후 2년)는 검색 요약에만 있고 안전보건공단 페이지가 비어 확인하지 못함
    - Open-RMF 저장소 라이선스는 GitHub 페이지 403·raw 경로 404 로 확인하지 못해 넣지 않음
    - 일본 원격조작형 소형차 신고제(2023-04 시행)는 1차 출처를 열지 않아 넣지 않음
    - 병원·상업 시설·가정 실내 로봇의 운행 규정, 승강기 탑승 KS(oq-173), 실내 사람 근접 기준(oq-231)은 이번에 조사하지 못함
- 범위 경계 위반 의심:
    - f16: 산업용 로봇 안전검사는 사업주의 설비 안전 의무이고 원문 19장 '시설·설비 제어'·'업종별 조건' 쪽이므로 규제 사례로만 쓰고 ROP 직접 범위로 서술하지 않음(f23 연계 대상)
    - f9·f10·f11: 제조물 책임의 법적 판정은 당사자·법원 몫이므로 ROP 가 제공할 기록의 근거로만 쓰고 f23 에서 연계 대상으로 둠
    - f15: 영상 촬영 적법성 판단은 53. 개인정보·영상 데이터와 겹치므로 이 영역에서는 규제 목록으로만 다룸
    - f8: 미국 주법은 한국 현장에 바로 적용되지 않으므로 해외 비교 사례로만 제안
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1234~ref-1248, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-1350·ref-1359(EU 기계류 규정, 이전 브리프 2026-09-30-22 출처 표 값 사용, 이번에 다시 열지 않아 fetched false). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 신규 15건 모두 열었다(webfetch 13, github_raw 2). ros.org(봇 차단)는 ros-infrastructure/rep, docs.ros.org 는 ros2/ros2_documentation 공식 저장소 원본을 열었다. EUR-Lex(본문 비어 있음)·신·김 뉴스레터(403)·안전보건공단 포털(본문 비어 있음)·Open-RMF GitHub(403)는 열지 못해 출처로 쓰지 않았다. 교차 확인 2건(f1: 정책브리핑·한국로봇산업진흥원, f3: 정책브리핑·지디넷코리아). 벤더 주장 없음. 분류 원문 핵심 질문에는 f21 로 답했고 결론은 '현장마다 다르며 실외는 운행 규정·인증·운용자 의무·의무 보험, 산업 사업장은 기계 안전 규제, 공통으로 AI·사이버보안·개인정보 규제, 제조물 책임, 오픈소스·3D 자산 라이선스가 겹친다'는 추정이다. 현장 유형 사례는 실외(f1~f7 한국, f8 미국)뿐이고 f16(산업용 로봇 안전검사)은 출처가 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 정책브리핑(ref-1234·ref-1245)·한국로봇산업진흥원(ref-1241)·고용노동부(ref-1247)·법제처 생활법령(ref-1244)·김·장(ref-1243)·지디넷코리아(ref-1240·ref-1242)다. 기존 열린 질문 9건은 해결하지 못했다(oq-186 은 현재 8개 심사항목만 확인, 개정 시점·흡수 관계 미확인; oq-187 은 인증 대상이 로봇과 관제장치 조합이라는 전제만 재확인; oq-143 은 f13 이 사람의 최종 결정 권한 시 고영향 제외라는 정부 설명만 제공해 부분 근거). L. AI·학습 기술 관련은 f13(인공지능 기본법)을 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영에 연결 제안했다(f24). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 고영향 인공지능·실외이동로봇 운행안전인증·개인 배송 장치·이동형 영상정보처리기기·원격 조작형 소형차·위험성평가는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-22/research.md

```markdown
# 리서치 브리프 2026-09-30-22

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-22 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 58. 다사업자 책임·계약·데이터 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 데이터 보유자, 실질적 변경, 모델 계약 조항, API 폐기 정책, 서비스 수준 협약 구성 요소 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·가정(공동주택)·건물 승강기 연동의 다사업자 책임 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 변경 승인·책임 분담, 데이터 접근·공유 계약, API 버전·폐기 정책, 서비스 수준·감사 이력 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — EU 데이터법·모델 계약 조항, 산업디지털전환법·산업데이터 계약 가이드라인, VDA 5050 버전 규칙, ISO/IEC 19086-1, IEC 62443-2-4, 21 CFR Part 11 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-145, oq-149, oq-185, oq-241, oq-249, oq-259 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
2. 법·표준은 로봇·AI 시스템을 바꾼 주체의 책임을 어떻게 정하는가(기계류의 실질적 변경, AI 가치사슬 책임, 산업제어 서비스 제공자의 보안 요구)? (섹션 4·6·7 겨냥, oq-249 관련)
3. 여러 사업자가 함께 만드는 운영 데이터의 소유·접근·공유 권리를 정하는 법과 계약 도구(EU 데이터법과 모델 계약 조항, 국내 산업디지털전환법과 산업데이터 계약 가이드라인)는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
4. 제조사·플랫폼 API 가 바뀔 때 호환성과 공지를 정하는 규칙(VDA 5050 버전 규칙, 오픈소스의 API 폐기 정책)은 어떻게 되어 있는가? (섹션 6·7 겨냥)
5. 서비스 수준 약속과 감사 이력은 어떤 표준·규정이 요구하고 무엇을 기록해야 하는가(ISO/IEC 19086-1, 21 CFR Part 11, EU AI법 로그 보관)? (섹션 6·7 겨냥)
6. 병원·공동주택·건물 설비 연동 등 현장 유형별로 다사업자 책임·계약을 다룬 사례와 책임 분담표 공개 사례가 있는가? (섹션 5·11 겨냥, oq-241·oq-149·oq-185 관련)
7. 다사업자 책임·계약·데이터에서 ROP가 직접 맡을 것과 계약 당사자·법무·제조사·설비업체에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥, oq-145·oq-259 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU 데이터법(Regulation (EU) 2023/2854)은 2025-09-12부터 일반 적용되며, 연결 제품(IoT 기기) 사용자가 제품 사용으로 함께 만든 데이터에 접근·이용·이전할 수 있게 하고, 제조사·서비스 제공자 같은 데이터 보유자는 사용자와 계약을 맺어야 하며 사용자 동의 없이 비개인 데이터를 활용할 수 없다. | ref-1345 | 아니오 | medium | 2025-12-15 | 작업 대상 | — |
| f2 | [사실] | EU 데이터법은 사용자가 데이터를 직접 또는 데이터 보유자를 통해 자신이 고른 제3자에게 공유하게 하고, 기업 간 계약에서 일방적으로 부과된 조항 가운데 '항상 불공정'과 '불공정으로 추정'되는 조항을 정해 구속력을 없애며, 데이터 처리 서비스 간 전환 요금은 2027-01-12부터 완전히 없앤다. | ref-1345 | 아니오 | medium | 2025-12-15 | 제약 | — |
| f3 | [사실] | 유럽연합 집행위원회가 2025-11-19에 낸 권고 초안은 EU 데이터법 이행을 돕는 구속력 없는 모델 계약 조항(MCT) 네 벌(데이터 보유자–사용자, 사용자–데이터 수령자, 데이터 보유자–데이터 수령자(보상 포함), 자발적 공유자–수령자)과 클라우드 표준 계약 조항 여섯 개(전환·이탈, 해지, 보안·업무 연속성, 비분산, 일방 변경 금지, 책임)를 제시한다. | ref-1346 | 아니오 | medium | 2025-11-19 | — | — |
| f4 | [사실] | 한국의 산업 디지털 전환 촉진법(2022-07 시행)은 산업데이터 생성에 투자한 자에게 그 데이터의 사용·수익권을 인정하고 관계자 간 계약 체결을 권고하며, 정부가 산업데이터 계약 지침을 마련하도록 했다. | ref-1347 | 아니오 | low | 2022-03-15 | 작업 대상 | — |
| f5 | [사실] | 산업통상부의 산업데이터 계약 가이드라인(공공데이터포털 등록 2023-04-05, PDF 432쪽)은 총론·법적기초·산업데이터 가치 산정·계약의 유형·개인보상·국외이전으로 구성되며, 산업데이터 거래 당사자를 위해 유의사항·표준계약서·업종별 사례를 안내한다. | ref-1348, ref-1347 | 아니오 | medium | 2023-04-05 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 명세는 [주].[부].[수정] 의미적 버전을 써서 주 버전은 필수 필드 추가 같은 호환을 깨는 변경, 부 버전은 선택 매개변수 추가 같은 새 기능, 수정 버전은 문서 오탈자 같은 작은 정정에 쓰고, MQTT 토픽 경로에 주 버전을 넣으며(interfaceName/majorVersion/manufacturer/serialNumber/topic), 변경 제안은 공식 GitHub 저장소로 받는다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f7 | [사실] | Kubernetes 의 API 폐기 정책은 API 요소를 API 그룹 버전을 올려야만 제거할 수 있게 하고, 버전 간 왕복 변환에서 정보가 보존되어야 하며, 정식(GA) API 는 주 버전 안에서 제거하지 않고 베타는 폐기 공지 뒤 9개월 또는 3개 부 릴리스 동안 유지하며, 폐기된 API 호출에는 경고 헤더·감사 주석·지표를 남긴다. | ref-1349 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | ISO/IEC 19086-1:2016(2016-09-21, 1판)은 클라우드 서비스 수준 협약(SLA)의 공통 구성 요소(개요, 클라우드 서비스 계약과 SLA 의 관계, 개념, 용어)를 정하지만 모든 서비스에 쓰는 표준 SLA 구조나 서비스 수준 목표 세트는 정하지 않는다. | ref-1351 | 아니오 | medium | 2016-09-21 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | IEC 62443-2-4:2023(2023-12-15)은 산업 자동화·제어 시스템(IACS) 서비스 제공자가 자동화 솔루션의 통합·유지보수 중에 자산 소유자에게 제공할 보안 관련 프로세스 요구사항을 정하며, 자산 소유자·서비스 제공자·제품 공급자를 구분하고 업종별로 요구를 골라 쓰는 프로파일을 둔다. | ref-1352 | 아니오 | medium | 2023-12-15 | 수행 자원 | 원문 미열람 |
| f10 | [사실] | EU 기계류 규정(Regulation (EU) 2023/1230, 2023-06-14 채택, 2027-01-20 적용)은 기계에 실질적 변경을 한 자연인·법인을 제조자로 보아 제조자 의무를 지게 하며, 실질적 변경은 새로운 위험을 만들거나 기존 위험을 키워 새로운 중요한 보호 조치가 필요한 변경이고 적합성에 영향을 주지 않는 수리·정비는 이에 해당하지 않는다. | ref-1350, ref-1359 | 아니오 | medium | 2023-06-14 | 제약 | — |
| f11 | [사실] | EU AI법 제25조는 유통자·수입자·배포자(deployer)·제3자가 고위험 AI 시스템에 자기 이름을 붙이거나 실질적 변경을 하거나 용도를 바꾸면 제공자로 보고, 최초 제공자에게 기술 문서·정보·기술적 접근을 주는 협력 의무를 지우며, 제공자와 부품·도구·서비스 공급자는 필요한 정보·기능·기술적 접근·지원을 서면 계약으로 정하게 한다(오픈소스 제외). | ref-1356 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f12 | [사실] | EU AI법 제26조는 고위험 AI 시스템 배포자가 자기 통제 아래 있는 자동 생성 로그를 최소 6개월 보관하고, 제공자 지침에 따라 운영을 감시하다가 위험이 의심되면 제공자 등에 알리고 사용을 멈추며 중대한 사고는 즉시 제공자에게 먼저 알리게 한다. | ref-1357 | 아니오 | medium | 2026-09-30 | 예외·성과 | — |
| f13 | [사실] | 미국 21 CFR 11.10(e)는 폐쇄형 전자기록 시스템에 전자기록을 만들거나 고치거나 지우는 운영자 입력과 행위의 날짜·시각을 독립적으로 기록하는 보안이 적용된 컴퓨터 생성 타임스탬프 감사 추적을 쓰도록 요구한다. | ref-1353 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f14 | [의견] | Shaik(SSRN, 2026-05)은 자율 산업 시스템의 책임을 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이에 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)를 제안하고, 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. | ref-1355 | 아니오 | low | 2026-05-01 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | 병원 사례(싱가포르): 창이종합병원 CHART 는 의료 로봇 미들웨어 RoMi-H 통합을 맡을 시스템 통합자를 연 2회 등재 프로그램으로 평가·인증하고, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있어 다사업자 연동의 책임 주체를 사전 자격으로 정한다. | ref-1289 | 아니오 | medium | 2025-05 | 병원 / 수행 자원 | 원문 미열람 |
| f16 | [사실] | 한국승강기협회는 현대엘리베이터·오티스·TK엘리베이터·미쓰비시엘리베이터 등 승강기 제조사가 참여한 과학기술정보통신부 과제 '실내외 자율주행 로봇 상호연동 표준개발'로 배달 로봇과 승강기가 API 로 실시간 정보를 주고받는 연동 표준을 만들고 있으며, 2024-12-31까지 국내·국제 표준 개발, 전문가 협의체 구성, 테스트베드·개념증명을 목표로 했다. | ref-1354 | 아니오 | low | 2023-05-17 | 수행 자원 | — |
| f17 | [사실] | 가정 사례(한국 공동주택): 한국아파트신문 사설(2026-09-14)은 시흥 힐스테이트더웨이브시티의 주차로봇 2세트 실증, 서울 송파구 아파트의 자율주행 순찰로봇 2대, 강남 타워팰리스의 사족보행로봇 기술검증, 부산 강서구 아파트의 운반로봇 서비스를 들고, 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전했다. | ref-1358 | 아니오 | low | 2026-09-14 | 가정 / 수행 자원 | — |
| f18 | [의견] | 같은 사설은 공동주택에 로봇·AI·통신망·관제시스템이 더해지면 관리사무소장 등 관리주체의 관리 영역과 책임이 오히려 넓어질 수 있으므로 도입 전에 책임 범위를 명확히 하고 법제도를 정비해야 한다고 본다. | ref-1358 | 아니오 | low | 2026-09-14 | 가정 / 제약 | — |
| f19 | [추정] | 확인한 자료를 종합하면 핵심 질문(제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까)에 대해 이를 한 번에 정한 공개 표준이나 책임 분담표는 찾지 못했고, 실제 규칙은 (a) 변경을 한 주체가 제조자·제공자 의무를 지는 법 규정(기계류 규정의 실질적 변경, AI법 가치사슬 책임), (b) 인터페이스 표준의 버전·폐기 규칙, (c) 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치의 조합으로 정해지는 것으로 보인다. | ref-1350, ref-1356, ref-031, ref-1349, ref-1351, ref-1346, ref-1352, ref-1289 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 58. 다사업자 책임·계약·데이터에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. | ref-031, ref-1349, ref-1353, ref-1357, ref-1345, ref-1346, ref-1351 | 아니오 | low | 2026-09-30 | 완료·인계 | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무(59. 법·규제·보험·라이선스)에, 로봇 펌웨어와 제조사 API 의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. | ref-1350, ref-1356, ref-1354, ref-1358, ref-1355 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f22 | [추정] | 이 영역은 인터페이스 버전 규칙의 21. 상호운용 표준·적합성과 20. 로봇·제조사 관제 연동(f6·f7), 승강기 연동 책임의 22. 설비·건물 시스템 연동(f16), 감사 이력·로그의 37. 관제 화면·실행 기록과 52. 통신 보호·위협 관리·감사(f12·f13·f9), 데이터 권리와 개인정보의 53. 개인정보·영상 데이터(f1·f17, oq-259), API 폐기와 변경 관리의 57. 자산·소프트웨어 수명주기 관리(f7), 규제 책임의 59. 법·규제·보험·라이선스(f10·f11·f14), 통합자 자격·계약의 3. 경제성·조달·사업 모델(f15), 책임 범위 합의의 2. 사용 사례·요구·책임 범위(oq-241), AI 가치사슬 책임의 47. AI·학습·적응과 모델 운영과 13. 대화형 기능의 신뢰·기반(f11, oq-145), 적용 현장인 63. 병원·의료(f15)·65. 가정·공동주택(f17·f18)과 이어진다. | ref-031, ref-1349, ref-1354, ref-1357, ref-1353, ref-1352, ref-1345, ref-1358, ref-1350, ref-1356, ref-1355, ref-1289 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1289 | Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05 | 정부·연구기관 | medium | 2026-09-30 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 예 |
| ref-1345 | European Commission (Shaping Europe's digital future) | Data Act explained | 2025-12-15 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | 아니오 |
| ref-1346 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 아니오 |
| ref-1347 | 지디넷코리아 | 산업데이터 만든 자에게 사용·수익권 부여 | 2022-03-15 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20220315103750 | 아니오 |
| ref-1348 | 산업통상부 (공공데이터포털) | 산업통상부_산업데이터 계약 가이드라인_20230109 | 2023-04-05 | 정부·연구기관 | high | 2026-09-30 | https://www.data.go.kr/data/15113186/fileData.do | 아니오 |
| ref-1349 | The Kubernetes Authors | Kubernetes Deprecation Policy | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | 아니오 |
| ref-1350 | European Parliament and Council of the European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery | 2023-06-14 | 정부·연구기관 | medium | 2026-09-30 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-1351 | IEC / ISO (ISO/IEC JTC 1) | ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts | 2016-09-21 | 표준 | medium | 2026-09-30 | https://webstore.iec.ch/en/publication/25920 | 예 |
| ref-1352 | IEC (BSI Knowledge 게재) | IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers | 2023-12-15 | 표준 | medium | 2026-09-30 | https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1 | 예 |
| ref-1353 | U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재) | 21 CFR § 11.10 - Controls for closed systems | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.law.cornell.edu/cfr/text/21/11.10 | 아니오 |
| ref-1354 | 전기신문 (안상민) | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 2023-05-17 | 기사 | low | 2026-09-30 | https://www.electimes.com/news/articleView.html?idxno=320147 | 아니오 |
| ref-1355 | Shaik, A. S. (SSRN) | Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong? | 2026-05-01 | 논문 | medium | 2026-09-30 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139 | 예 |
| ref-1356 | Future of Life Institute (artificialintelligenceact.eu) | Article 25: Responsibilities Along the AI Value Chain \| EU Artificial Intelligence Act | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://artificialintelligenceact.eu/article/25/ | 아니오 |
| ref-1357 | Future of Life Institute (artificialintelligenceact.eu) | Article 26: Obligations of Deployers of High-Risk AI Systems \| EU Artificial Intelligence Act | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://artificialintelligenceact.eu/article/26/ | 아니오 |
| ref-1358 | 한국아파트신문 (사설) | 공동주택에 밀려오는 로봇, 또 다른 관리책임은 (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-09-30 | https://www.hapt.co.kr/news/articleView.html?idxno=169488 | 아니오 |
| ref-1359 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(핵심 질문 답, 추정), f18(공동주택 책임 확대 우려, 의견), f14(책임 공백 논의, 의견) / 섹션 4: 데이터 보유자·연결 제품 데이터 f1, 모델 계약 조항 f3, 산업데이터 사용·수익권 f4, 실질적 변경 f10·f11, 의미적 버전·API 폐기 정책 f6·f7, SLA 구성 요소 f8, 감사 추적 f13 / 섹션 5: 병원 — f15(수행 자원, 싱가포르), 가정 — f17(수행 자원, 한국 공동주택)·f18(제약), 현장 유형 미명시 건물 승강기 연동 — f16(22. 설비·건물 시스템 연동 연계로 서술). 물류창고·제조 공장·상업 시설·실외 사례는 찾지 못했음을 명시 / 섹션 6: 변경 승인·책임 분담 f10·f11·f9·f15, 데이터 접근·공유 계약 f1·f2·f3·f4·f5, API 버전·폐기 정책 f6·f7, 서비스 수준·감사 이력 f8·f12·f13 / 섹션 7: EU 데이터법·모델 계약 조항 f1~f3, 산업디지털전환법·산업데이터 계약 가이드라인 f4·f5, VDA 5050 버전 규칙 f6, Kubernetes 폐기 정책 f7, ISO/IEC 19086-1 f8(원문 미열람), IEC 62443-2-4 f9(원문 미열람), EU 기계류 규정 f10, EU AI법 제25·26조 f11·f12, 21 CFR Part 11 f13 / 섹션 8: f3·f5·f14 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65 / 섹션 11: 기존 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259(모두 미해결 유지; oq-241·oq-249 는 f10·f11·f12·f19 로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f16, 65. 가정·공동주택 페이지에 f17·f18, 57. 자산·소프트웨어 수명주기 관리 페이지에 f7 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 데이터 보유자 | Data Holder (EU Data Act) | EU 데이터법에서 연결 제품이나 관련 서비스가 만든 데이터를 이용·제공할 권리나 의무를 가진 자로, 사용자 요청 시 데이터를 사용자나 제3자에게 제공해야 하고 사용자와의 계약 없이 비개인 데이터를 활용할 수 없다. |
| 실질적 변경 | Substantial Modification | 출시된 기계나 AI 시스템을 바꿔 새로운 위험을 만들거나 위험을 키우거나 적합성·용도에 영향을 주는 변경으로, 이를 한 자가 제조자·제공자의 의무를 지게 되는 기준이다. |
| 모델 계약 조항 | Model Contractual Terms (MCTs) | EU 집행위원회가 데이터법 이행을 위해 데이터 보유자·사용자·데이터 수령자 사이의 데이터 접근·이용 계약에 쓰도록 권고하는 구속력 없는 표준 계약 문안이다. |
| API 폐기 정책 | API Deprecation Policy | API 요소를 언제 어떤 공지와 유예 기간을 거쳐 폐기·제거할지, 버전을 어떻게 올릴지를 미리 정해 이용자가 호환성을 예측하게 하는 규칙이다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반
- 로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동, 57. 자산·소프트웨어 수명주기 관리 | 근거: f7 | 종류: 일반
- 국내 산업데이터 계약 가이드라인의 표준계약서와 업종별 사례가 로봇 운영 데이터(지도·작업 이력·센서 로그)처럼 여러 사업자가 함께 만드는 데이터를 어떻게 다루는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 15. 지도·공간·위치 모델 | 근거: f5 | 종류: 일반
- 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스, 48. 안전·위험 관리 | 근거: f10 | 종류: 일반
- 로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 22. 설비·건물 시스템 연동 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f4 산업디지털전환법 제9조의 공동 생성 데이터·제3자 제공 시 권리(당사자 약정 우선) 조문은 검색 요약에만 있어 finding 으로 내지 않음 — 국가법령정보센터 조문 열람 실패
    - f5 산업데이터 계약 가이드라인 PDF(432쪽) 본문 미열람 — 계약 유형 구분과 표준계약서 조항 미확인
    - f8 ISO/IEC 19086-1 본문 미열람(유료), 표준 SLA 구조를 정하지 않는다는 부분은 검색 요약
    - f9 IEC 62443-2-4 범위·역할 구분은 검색 요약 기준, 본문 미열람
    - f10 EU 기계류 규정 실질적 변경 정의·제18조는 EUR-Lex 본문을 열지 못해 검색 요약 기준
    - f14 Shaik 원고가 든 2024년 독일 자동차 공장 사고(6개 당사자 책임 부인) 사례는 저자 주장으로 독립 확인 실패 — finding 에서 제외
    - f16 로봇-승강기 연동 표준 과제의 결과물(표준 번호·책임 분담) 미확인
    - f17 이동로봇 특별법안 원문·발의일 미확인
    - oq-241 로봇 오케스트레이션 도입 계약의 책임 분담표·표준 계약 조항 공개 사례를 이번에도 찾지 못함
    - ISO/IEC 20000-1:2018 변경 관리 조항은 공개 원문을 읽지 못해 넣지 않음
    - 국내 공공 정보시스템 SLA 가이드는 공식 출처를 찾지 못해 넣지 않음
    - 물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례를 찾지 못함
- 범위 경계 위반 의심:
    - f10·f11·f12·f14: 규제상 책임·로그 의무와 책임 배분 이론은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 변경 승인·책임 분담 근거로만 쓰고 법적 판정은 f21 에서 연계 대상으로 둠
    - f16: 승강기 쪽 연동 인터페이스와 설비 안전 제어는 원문 19장 '시설·설비 제어' 연계 영역이므로 ROP 직접 범위로 서술하지 않음(f21 연계 대상)
    - f13: 21 CFR Part 11 은 FDA 규제 대상 전자기록에 적용되는 규정이라 감사 추적 요구의 참고 사례로만 쓰고 병원 현장 의무로 단정하지 않음(site_type null)
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1345~ref-1359, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-031(이전 브리프 2026-09-30-19 출처 표 값 사용, 이번에 GitHub 공식 저장소 원문을 다시 열어 버전 규칙 확인), ref-1289(다시 열지 않고 재인용). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 17건 중 12건(webfetch 11, github_raw 1)을 열었고 ref-1289·ref-1350(EUR-Lex 본문 비어 있음)·ref-1351·ref-1352(유료 표준, 소개 페이지만)·ref-1355(SSRN 403)는 fetched false 다. 교차 확인 0건. 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '연동 오류 수정·변경 승인 주체를 한 번에 정한 공개 표준·책임 분담표는 찾지 못했고, 변경 주체 책임 법규·인터페이스 버전 규칙·SLA와 표준 계약 조항·통합자 자격의 조합으로 정해지는 것으로 보인다'는 추정이다. 현장 유형 사례는 병원(f15 싱가포르, 재인용)·가정(f17·f18 한국 공동주택)이고 승강기 연동(f16)은 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·상업 시설·실외는 찾지 못했다. 국내 자료는 지디넷코리아(ref-1347)·공공데이터포털(ref-1348)·전기신문(ref-1354)·한국아파트신문(ref-1358)이다. 기존 열린 질문 oq-145·oq-149·oq-185·oq-241·oq-249·oq-259 는 해결하지 못했다(oq-249 는 f10·f12 가 개별 기계·AI 시스템 쪽 의무만 보여 플랫폼 적용 여부는 미해결, oq-241 은 f19 로 부분 근거). L. AI·학습 기술 관련은 f11(AI 가치사슬 책임)을 47. AI·학습·적응과 모델 운영과 연결 제안했다(f22). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 감사 추적·서비스 수준 협약·의미적 버전 관리·산업데이터·서비스형 로봇·등재 프로그램·보안 수준(IEC 62443)은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
