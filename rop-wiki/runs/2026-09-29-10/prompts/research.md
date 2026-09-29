(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-10
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 1. 기술·시장·업체 동향 (A. 기획·사업)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-899
- 새 출처 id 구간: ref-899 ~ ref-928 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-899 부터 순서대로 쓰고 ref-928 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-10/target.json

```json
{
  "run_id": "2026-09-29-10",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 102,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 1,
    "area_name": "1. 기술·시장·업체 동향",
    "category": "A. 기획·사업",
    "category_letter": "A"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=1"
}
```

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md

```markdown
---
title: "1. 기술·시장·업체 동향"
type: area
category: "A. 기획·사업"
area_no: 1
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [A. 기획·사업](index.md) › 1. 기술·시장·업체 동향

# 1. 기술·시장·업체 동향

!!! info "소속 대분류"
    [A. 기획·사업](index.md) — 핵심 질문:
    어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]

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

### docs/categories/planning-and-business/use-cases-requirements-and-scope.md (요약)

```markdown
# 2. 사용 사례·요구·책임 범위

소속 대분류: A. 기획·사업 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **책임 범위 정의**: 플랫폼이 직접 맡을 범위와 외부(업무 시스템·로봇 자체 지능·설비 제어·현장 간 운송·업종별 조건)에 맡길 범위를 정한다
- **사용 사례 발굴·요구 정의**: 로봇에게 맡길 일과 성공 기준·수용 기준을 정한다
- **현장 유형별 요구 정리**: 물류창고·제조 공장·병원·상업 시설·가정·실외 같은 현장 유형마다 공통 요구와 고유 요구를 정리한다

## 2. 핵심 질문

로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 898건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 239개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [1] 에 걸린 0건 / 전체 158건)

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

### runs/2026-09-29-08/research.md

```markdown
# 리서치 브리프 2026-09-29-08

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-08 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 대분류 | B. 로봇 온톨로지 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 스킬 인터페이스·전제·유지·사후 조건·수행 가능 동작 용어 없음(스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·자산관리셸은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 능력 기반 로봇 후보 질의, 능력–실행 연결(능력→스킬→인터페이스), 온톨로지 기반 연동 자동화(모델 매핑·설정 초안 생성), 실행 시점 조건 판단(전제조건·상태 검사) 네 갈래 모두 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 능력·스킬·서비스 모델 온톨로지, IDTA 02020 능력 기술 서브모델, Open-RMF 사용자 정의 작업, VDA 5050 커넥터, OPC UA 스킬 실행 프로토콜, SkiROS2 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-150 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]
2. 작업 요구에 맞는 로봇·자원 후보를 온톨로지 질의로 찾고 근거와 함께 돌려주는 능력 매칭 접근에는 무엇이 있는가? (섹션 4·6·8 겨냥)
3. 온톨로지의 능력을 실제 로봇 명령·어댑터·스킬 인터페이스에 묶는 모델(능력·스킬·서비스 모델, 자산관리셸 능력 기술, OPC UA 스킬, Open-RMF 사용자 정의 작업)은 무엇을 정하며, 검토되지 않은 연결의 실행을 어떻게 막는가? (섹션 6·7 겨냥)
4. 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만드는 방법(모델 간 매핑, 계획 도메인 자동 생성, 모델 기반 생성)은 무엇이 보고되었는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)
5. 배터리·적재·문·승강기 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단하는 전제조건·정책 검사(SPARQL·SHACL, 전제·유지·사후 조건)는 어떻게 구현되는가? (섹션 4·6 겨냥)
6. oq-150 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (섹션 5·11 겨냥, 현장 유형 명시·한국 자료 우선)
7. 온톨로지 기반 연동에서 ROP가 직접 맡을 것(후보 질의·매핑·설정 초안·조건 검사)과 스킬 내부 구현·설비 API 에 맡길 것의 경계는 어디이며, 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Plattform Industrie 4.0 의 능력·스킬·서비스(CSS) 참조 모델을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, 스킬을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의하고, 모든 스킬이 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다. | ref-882 | 아니오 | medium | 2026-09-29 | — | — |
| f2 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 판은 생산 공정의 요구 능력과 가용 자원의 제공 능력을 비교하는 기반을 목적으로 하며, 능력을 속성(최대 속도·허용 공차 등), 제약(전제조건·불변·사후조건의 속성 제약과 순서·병렬의 전이 제약), 능력을 구현하는 스킬(기술·소프트웨어 모듈)의 세 관계로 모델링한다. | ref-229 | 아니오 | medium | 2026-09-29 | 제약 | 원문 미열람 |
| f3 | [사실] | 서로 다른 두 발행 주체(헬무트 슈미트 대학 계열 CaSkade 의 CSS 온톨로지, IDTA 의 능력 기술 서브모델)가 구현 독립적 능력과 실행 구현인 스킬을 분리하고 요구 능력–제공 능력 매칭을 모델의 목적으로 각각 정의해, 이 영역의 능력–실행 분리 구조가 한 곳 이상에서 확인된다. | ref-882, ref-229 | 예 | medium | 2026-09-29 | — | — |
| f4 | [사실] | Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. | ref-038 | 아니오 | medium | 2023-02-09 | — | — |
| f5 | [사실] | Dussard·Sarthou·Clodic(2023, 2025 개정)은 로봇이 보유한 물리 구성요소와 하위 능력으로부터 상위 능력을 온톨로지 추론으로 도출해 로봇이 어떤 작업에 배정될 수 있고 없는지를 스스로 판단하게 하고, 능력과 외부 객체 속성 사이의 어포던스 관계까지 추론하는 방법을 제안했다. | ref-249 | 아니오 | medium | 2025-09-10 | 수행 자원 | — |
| f6 | [사실] | Järvenpää·Siltala·Hylli·Lanz(Procedia CIRP 97, 2021)의 능력 매치메이킹 소프트웨어는 제품 요구와 자원 능력의 매칭을 자동화해 기존 생산 시스템이 새 제품 요구를 충족하는지 확인하고 대형 카탈로그에서 후보 자원을 찾으며, 외부 설계 도구와의 연동을 사례로 설명했다. | ref-890 | 아니오 | medium | 2021 | 수행 자원 | — |
| f7 | [사실] | 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)이 온톨로지 기반 능력 기술로 작업·요구에 맞는 로봇·자원 후보를 찾는 접근을 각각 보고해, 능력 기반 로봇 후보 질의가 한 곳 이상에서 확인된다. | ref-249, ref-890, ref-038 | 예 | medium | 2025-09-10 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 의 사용자 정의 작업 문서는 플릿 설정의 action_categories 로 지원 동작을 선언하고, add_performable_action 의 consider 콜백이 동작 설명을 보고 수락 여부를 정하며 set_action_executor 가 실행을 맡는 두 부분 API 를 정하고, 사용자 정의 동작 중 로봇은 읽기 전용 교통 참여자가 되어 교통 협상에 참여하지 않으며 문·승강기 사용은 사용자 정의 로직에서 바꿀 수 없다고 적는다. | ref-880 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f9 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 새 플릿 설정에 작업 능력(loop·delivery·clean)과 재충전 임계값, 배터리·기계 시스템 매개변수를 적게 하고 로봇 측 API 가 battery_soc 를 보고하게 하여, 능력 선언과 실행 시점 배터리 상태가 같은 설정·API 에 담긴다. | ref-153 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f10 | [사실] | Mayr·Rovida·Krueger 의 SkiROS2(IROS 2023)는 스킬을 전제·유지·사후 조건으로 정의하고 OWL 세계 모델(지식 베이스)로 세계 상태와 개체를 추론하며 확장 행동 트리로 작업 계획과 반응적 실행을 합쳐, 서로 다른 작업과 로봇 시스템 사이에서 스킬을 교체해 쓰는 사례(작업 계획·추론·다중 센서 통합·제조 실행 시스템 연결 등)를 보였다. | ref-881 | 아니오 | medium | 2023-06-29 | 제약 | — |
| f11 | [사실] | Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 특정 작업에 대한 에이전트 자격과 전제조건을 검사하고 SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 Fundació Ave Maria 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다. | ref-885 | 아니오 | medium | 2025-04-30 | 병원 / 제약 | — |
| f12 | [사실] | 서로 다른 세 발행 주체(룬드대학교의 SkiROS2, 그리스 연구진의 HERON, IDTA 의 능력 기술 서브모델)가 능력·스킬에 전제조건과 사후조건 같은 실행 조건을 붙이고 실행 전에 이를 검사하는 구조를 각각 두어, 이 영역의 실행 시점 조건 판단이 한 곳 이상에서 확인된다. | ref-881, ref-885, ref-229 | 예 | high | 2025-04-30 | 제약 | — |
| f13 | [사실] | Vieira da Silva 외(2023, 2024 개정)는 자산관리셸 서브모델과 능력·스킬 온톨로지가 서로 호환되지 않는 두 모델링 틀임을 분석하고, 비교 가능한 요소와 다른 요소를 가려낸 뒤 두 개의 단방향 선언적 매핑으로 이루어진 양방향 매핑 개념을 제시했다. | ref-037 | 아니오 | medium | 2024-04-28 | — | — |
| f14 | [사실] | Nabizada 외(IEEE CASE 2026 채택)는 네 가지 Industrie 4.0 표준으로 구조화한 자산관리셸 능력 모델에 완전한 PDDL 계획 문제를 자동 생성할 정보가 충분함을 보이고, PDDL 전용 서브모델 없이 분산 다중 자산관리셸 구조를 계획 문제로 변환하는 추출 알고리즘을 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증했다. | ref-201 | 아니오 | medium | 2026-06-01 | — | — |
| f15 | [사실] | Nagrath·Blender·Shaik·Schlegel(2022)은 서비스 로봇에서 소프트웨어 컴포넌트의 자산관리셸을 표준화된 디지털 데이터 시트로, 시스템 수준 자산관리셸을 런타임 운영 데이터 수집과 스킬 수준 명령의 창구로 쓰며, 자산관리셸을 손으로 만들지 않고 모델 기반 개발·조합 워크플로에서 생성·채운다고 보고했다. | ref-883 | 아니오 | medium | 2022-08-02 | — | — |
| f16 | [사실] | Sidorenko 외(FAIM 2021)는 스킬을 유한 상태 기계로 OPC UA 에 노출하고 Industrie 4.0 언어 메시지와 상호작용 상태 기계를 능동 자산관리셸 안에 모델링한 스킬 실행 상호작용 프로토콜을 제시해, 두 Industrie 4.0 컴포넌트가 계층적 제어 대신 동등 협력 방식으로 스킬을 함께 실행하는 예시를 시연했다. | ref-887 | 아니오 | medium | 2021-11-03 | 완료·인계 | — |
| f17 | [사실] | 서로 다른 세 발행 주체(Schlegel 연구진, SmartFactory-KL 계열 Sidorenko 연구진, CaSkade 의 CSS 온톨로지)가 능력 모델과 별도로 스킬 실행 인터페이스(OPC UA 서버·상태 기계·자산관리셸 스킬 명령)를 두고 능력→스킬→인터페이스 순으로 실제 명령에 묶는 구조를 각각 보고해, 이 영역의 능력–실행 연결 방식이 한 곳 이상에서 확인된다. | ref-883, ref-887, ref-882 | 예 | medium | 2022-08-02 | — | — |
| f18 | [사실] | ROS 2 패키지 vda5050_connector(1.1.1, BSD-3, VDA 5050 2.0 지원)는 MQTT 브리지·컨트롤러(주문 검증·실행·피드백)·어댑터의 세 부분으로 로봇을 VDA 5050 관제에 연결하며, 어댑터는 상태·노드 주행·VDA 동작의 세 핸들러를 플러그인으로 두어 로봇 플랫폼마다 사용자가 핸들러 패키지를 직접 만들어야 한다. | ref-886 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f19 | [추정] | 등록된 능력 모델에서 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만들었다고 직접 보고한 자료는 이번 조사에서 확인되지 않았으며, 확인된 것은 모델 간 선언적 매핑(f13), 자산관리셸에서 계획 도메인 자동 생성(f14), 모델 기반 자산관리셸 생성(f15), 어댑터의 고정된 핸들러 구조(f18·f9)이므로 이를 결합하면 능력 모델에서 핸들러·설정 초안을 만드는 경로가 가능해 보이나 사례는 미확인이다. | ref-037, ref-201, ref-886, ref-153 | 아니오 | low | 2026-09-29 | — | — |
| f20 | [사실] | 서로 다른 두 발행 주체(Open Robotics 의 플릿 어댑터·사용자 정의 작업 문서, ROS 패키지 색인의 vda5050_connector)가 로봇 연동 어댑터를 '플릿·능력 설정'과 '로봇별 핸들러·API 구현'의 두 부분으로 각각 구성해, 온톨로지로 자동화할 수 있는 부분(설정·매핑)과 손작업이 남는 부분(로봇별 구현)의 경계가 한 곳 이상에서 확인된다. | ref-880, ref-153, ref-886 | 예 | high | 2026-09-29 | 수행 자원 | — |
| f21 | [사실] | 창이종합병원 CHART 는 KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 와 함께 캐피털랜드 Galen 오피스 빌딩에서 개방 API 를 가진 KONE DX 급 승강기와 RMF 로 자율이동로봇이 여러 층을 오가는 시험 환경을 만들고, 청소·보안·배송·컨시어지 등 여러 업체 로봇으로 시험을 확대할 계획을 밝혔으나 업체 수와 정량 결과는 공개 페이지에 없다. | ref-889 | 아니오 | medium | 2026-09-29 | 기타 / 수행 자원 | — |
| f22 | [사실] | Valner 외(2022)의 타르투대학교병원 현장 시험에서는 프로그램 제어가 없는 병원 문을 카드 인식·근접 센서를 대신 작동시키는 서보 장치로 보완해야 했으므로, 온톨로지·설정만으로 연동되지 않는 설비가 남아 손작업 없는 연동의 한계를 보여준다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 제약 | 원문 미열람 |
| f23 | [사실] | 황선명(보안공학연구논문지 8권 1호, 2011)은 컴포넌트 온톨로지와 환경 온톨로지를 구축해 사람의 명령을 사전 정의된 작업에 연결하고 환경 온톨로지에서 매개변수를 얻어 필요한 컴포넌트 목록을 구성·실행하는 로봇 컴포넌트 동적 재구성 방법을 제안했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 기반 로봇 연동 연구다. | ref-888 | 아니오 | medium | 2011 | — | — |
| f24 | [사실] | Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하게 하여, 온톨로지 기반 연동의 앞 단계인 능력 모델 작성 부담을 줄이는 방법을 제안했다. | ref-465 | 아니오 | medium | 2024-10-18 | 완료·인계 | 원문 미열람 |
| f25 | [추정] | 확인한 자료를 종합하면 6. 온톨로지 기반 시스템·로봇 연동에서 ROP가 직접 맡을 범위는 능력 온톨로지 질의로 후보 로봇을 찾아 근거와 함께 돌려주는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안 생성, 실행 전 전제조건·정책 검사(배터리·문·승강기 상태)이며, 근거를 함께 돌려주는 설명 기능과 검토되지 않은 연결의 실행 차단은 확인한 출처 어디에도 명시되지 않아 ROP 가 따로 설계해야 할 요구로 보인다. | ref-882, ref-880, ref-886, ref-885 | 아니오 | low | 2026-09-29 | — | — |
| f26 | [추정] | 연계 대상: 스킬의 내부 구현과 상태 기계 실행(OPC UA 서버·로봇 SDK 쪽)과 승강기 제조사의 개방 API 자체는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 쪽이므로, 이종 제조사를 잇는 ROP 는 스킬 인터페이스 호출·상태 확인·완료 판정과 승강기 사용 요청·인계만 맡고 구현 성능은 제조사·설비 측에 맡겨야 할 것으로 보인다. | ref-887, ref-889, ref-882 | 아니오 | low | 2026-09-29 | 제약 | — |
| f27 | [추정] | 이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 어댑터·규격은 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성, 문·승강기 상태는 22. 설비·건물 시스템 연동, 후보 질의 결과는 25. 작업 배정 — MRTA, 실행 조건과 완료 판정은 29. 명령·작업 실행의 신뢰성과 18. 실시간 세계 상태·데이터 일관성에 이어지며, 언어 모델로 능력 온톨로지를 만드는 방법(f24)은 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에도 연결된다. | ref-880, ref-229, ref-885, ref-465 | 아니오 | low | 2026-09-29 | — | — |
| f28 | [추정] | oq-150 관련: Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서(f8·f9)로 확인되지만 문·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 oq-150 은 미해결로 남는다. | ref-880, ref-229, ref-153 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University) | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2023-02-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2209.10900 | 아니오 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택) | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 2026-06-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.02167 | 아니오 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2024-04-28 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2307.00827 | 아니오 |
| ref-249 | Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS) | Ontological Component-based Description of Robot Capabilities | 2025-09-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.07569 | 아니오 |
| ref-880 | Open Robotics (Programming Multiple Robots with ROS 2) | User-defined Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_userdefined.html | 아니오 |
| ref-881 | Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023) | SkiROS2: A skill-based Robot Control Platform for ROS | 2023-06-29 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.17030 | 아니오 |
| ref-882 | CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소 | CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README) | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/CaSkade-Automation/CSS | 아니오 |
| ref-883 | Nagrath, V., Blender, T., Shaik, N., & Schlegel, C. (Technische Hochschule Ulm) | Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots | 2022-08-02 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2208.01273 | 아니오 |
| ref-229 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0) | 미확인 | 표준 | medium | 2026-09-29 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-885 | Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel) | HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics | 2025-04-30 | 논문 | high | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/ | 아니오 |
| ref-886 | ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda) | vda5050_connector - ROS Package Overview | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://index.ros.org/p/vda5050_connector/ | 아니오 |
| ref-887 | Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo) | An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell | 2021-11-03 | 논문 | medium | 2026-09-29 | https://zenodo.org/records/5648095 | 아니오 |
| ref-888 | 황선명 (대전대학교, 보안공학연구논문지 8(1)) | 온톨로지 기반의 로봇 동적재구성에 관한 연구 | 2011 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001533055 | 아니오 |
| ref-889 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART) | Robot-Lift Integration Challenge \| Changi General Hospital | 미확인 | 정부·연구기관 | medium | 2026-09-29 | https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge | 아니오 |
| ref-890 | Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97) | Capability matchmaking software for rapid production system design and reconfiguration planning | 2021 | 논문 | medium | 2026-09-29 | https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/ | 아니오 |
| ref-153 | Open Robotics (Programming Multiple Robots with ROS 2) | Fleet Adapter Tutorial (integration_fleets_action_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-09-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-10-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.07962 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4(이기종 로봇 기능을 일관되게 기술할 방법 부재), f20(어댑터가 설정과 로봇별 구현으로 나뉘어 손작업이 남음), f22(설비가 프로그램 제어를 못 하면 온톨로지·설정만으로 연동되지 않음) / 섹션 4: f1(능력·스킬·서비스·스킬 인터페이스), f2(속성·제약·스킬, 전제조건·불변·사후조건), f10(전제·유지·사후 조건), f8(수행 가능 동작·action_categories), f5(구성요소 기반 능력 추론·어포던스) / 섹션 5: 병원 — f11(HERON 의료센터 시뮬레이션: 물류 운반·다중 로봇 조정, 임상 배치 아님을 명시), f22(타르투대학교병원 문 보완 장치), 기타 — f21(싱가포르 Galen 오피스 빌딩 승강기 연동 시험 환경), 제조 공장·물류창고 현장 사례는 확인되지 않음을 서술(f6·f14 는 생산 시스템 설계·실험실 수준) / 섹션 6: 능력 기반 후보 질의 f5·f6·f7, 능력–실행 연결 f1·f15·f16·f17·f8, 연동 자동화 f13·f14·f15·f19(자동 생성 사례 미확인은 추정), 실행 시점 조건 판단 f9·f10·f11·f12, 앞 단계 능력 모델 생성 f24(교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 함께 연결) / 섹션 7: f1(CSS 온톨로지), f2(IDTA 02020), f8·f9(Open-RMF 사용자 정의 작업·플릿 어댑터), f18(vda5050_connector), f16(OPC UA 스킬 실행 프로토콜), f10(SkiROS2) / 섹션 8: f4, f5, f6, f13, f14, f15, f16, f11, 국내 f23 / 섹션 9: f25(직접 범위: 후보 질의·매핑표·검토 승인 기록·설정 초안·전제조건 검사), f26(연계 대상: 스킬 내부 구현·승강기 API) / 섹션 10: f27 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 18. 실시간 세계 상태·데이터 일관성, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 63. 병원·의료(f11·f22) / 섹션 11: 기존 oq-150(f28 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f8·f21 반영, 21. 상호운용 표준·적합성 페이지에 f2·f13·f18 반영, 25. 작업 배정 — MRTA 페이지에 f5·f7 반영, 트랙 manual-capability-ontology 단계 4(실행 연결)에 f1·f16·f17 참고. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 스킬 인터페이스 | Skill Interface | 능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다. |
| 전제·유지·사후 조건 | Pre-, Hold-, Post-condition | 스킬이 시작될 때 참이어야 하는 조건(전제), 실행 중 계속 유지되어야 하는 조건(유지), 끝난 뒤 성립해야 하는 조건(사후)으로 스킬을 정의해 실행 가능 여부 판단과 완료 확인에 쓰는 방식이다. |
| 수행 가능 동작 | Performable Action (Open-RMF perform_action) | Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다. |

## 열린 질문

새로 생긴 질문:

- 등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 20. 로봇·제조사 관제 연동, 4. 이기종 로봇 등록 | 근거: f19 | 종류: 일반
- Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 바꿀 수 없을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 28. 공용 자원·충전·에너지 최적화, 29. 명령·작업 실행의 신뢰성 | 근거: f8 | 종류: 일반
- 국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 25. 작업 배정 — MRTA | 근거: f23 | 종류: 일반
- 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f13 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 5
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f6 탐페레 매치메이킹의 OWL 온톨로지·SPIN 규칙 구현 세부는 검색 결과 요약에서만 보였고 연 초록 페이지에 없어 claim 에 넣지 않음(Procedia CIRP ScienceDirect 원문 403)
    - f3 CSS 온톨로지와 IDTA 02020 은 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립성이 제한적임(신뢰도 medium 으로 둠)
    - f2 IDTA 02020 1.0 판 발행일 미확인(README 에 날짜 없음), f1·f8·f18·f21 출처 발행일 미확인
    - f11 HERON 은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 같은 구체 상태 조건은 전문에서 확인하지 못함
    - f14 AAS→PDDL 생성의 정량 결과와 f10 SkiROS2 의 실기 배치 결과는 초록에 없어 미확인
    - f16 Sidorenko 외 논문은 Zenodo 초록만 확인(상태 기계 세부 미확인)
    - MDPI Electronics 15(16):3562 'Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation'(배터리·층 접근 조건의 의미 기반 실행 가능성 추론)은 두 경로 모두 403 으로 열지 못해 넣지 않음 — 실행 시점 조건 판단의 핵심 후보 출처
    - Järvenpää 외 'Semantic rules for capability matchmaking'(IJCIM 2022, tandfonline)과 'development of an ontology for describing the capabilities of manufacturing resources'(Springer JIM 2018)는 403·인증 리다이렉트로 열지 못함
    - Plattform Industrie 4.0 CSS 토론 문서는 웹 페이지가 보안 검증으로 막히고 PDF 는 텍스트 추출이 되지 않아 CSS 온톨로지 README(ref-882)로 대신함 — 참조 모델 원문 미열람
    - RoboCaSk 온톨로지 저장소 raw README 는 404 로 확인하지 못해 f1 에 이름만 적음
    - f7·f17 외 능력 기반 후보 질의가 '근거와 함께' 후보를 돌려주는 설명 기능은 어느 출처에서도 확인하지 못함
    - oq-150 미해결(f28)
    - f3·f7·f12·f17·f20 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
- 범위 경계 위반 의심:
    - f26: 스킬 내부 구현·OPC UA 상태 기계 실행과 승강기 제조사 API 는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 연계 영역이므로 '연계 대상: '으로 표시함
    - f21: 승강기 개방 API 연동은 22. 설비·건물 시스템 연동의 범위와 겹치므로 이 영역에서는 온톨로지·플랫폼 기반 이기종 로봇의 층간 이동 시험 환경 사례로만 제안함
    - f11: HERON 의 역할 기반 권한·오버라이드 정책 검사는 48. 안전·위험 관리·51. 인증·권한·격리와 겹치므로 실행 시점 조건 판단 사례로만 제안함
    - f14·f6: 제조 생산 시스템 설계·계획 도메인 생성 연구는 이동로봇 플랫폼이 아니므로 능력 모델에서 실행 산출물을 자동 생성하는 방법의 선례로만 제안함
    - f24: 언어 모델 능력 온톨로지 생성은 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f27)
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-038~ref-890, 예약 구간 안) 상한 도달로 CSS 참조 모델 논문(arXiv 2209.09632), ETFA 능력·스킬 서베이(arXiv 2204.12908), MiR VDA 5050 어댑터 벤더 블로그, RoSO/SMGI(arXiv 2605.08185), 온톨로지 기반 로봇 사양 합성(arXiv 2602.05456), 국내 클라우드 기반 이기종 다중로봇 플랫폼(제어로봇시스템학회 2023, 온톨로지 언급 없음)은 열었으나 넣지 않았다. 원문 열람 15건(github_raw 2: CSS 온톨로지 README·IDTA 02020 README, webfetch 13: arXiv 초록 7건, PMC 전문 1건, Open-RMF 문서, ROS Index, Zenodo, KCI 초록, CGH 페이지, 탐페레 연구 포털), 재사용 3건(ref-153·ref-869·ref-465, 이전 브리프 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않음). 주의: 실행 컨텍스트가 예약한 ref-038~ref-905 구간은 같은 날 이전 실행 2026-09-29-07 이 ref-038·ref-037·ref-880·ref-881·ref-883 으로 낸 다른 URL 과 번호가 겹치므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 5건(f3: CaSkade·IDTA — 공통 참조 모델 파생이라 medium, f7: LAAS·탐페레·HSU, f12: 룬드·그리스 연구진·IDTA, f17: Schlegel 연구진·Sidorenko 연구진·CaSkade, f20: Open Robotics·ROS Index/InOrbit). 신뢰도 high 는 f12·f20 두 건(각각 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지로 새 로봇·새 시스템을 손작업 없이 연동)에는 f1·f2·f3(능력–스킬–인터페이스 분리와 요구/제공 매칭 모델), f5·f6·f7(능력 기반 후보 질의), f13·f14·f15(모델 매핑·계획 도메인·자산관리셸 자동 생성), f8·f18·f20(어댑터의 설정 부분과 로봇별 구현 부분), f9~f12(실행 조건 검사)로 답했으며 결론은 '능력 모델과 실행 인터페이스를 잇는 구조와 조건 검사는 여러 곳에서 확인되지만, 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성해 손작업을 없앤 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다'는 추정(f19·f25)이다. 현장 유형: 병원(f11 시뮬레이션, f22 타르투대학교병원 재인용), 기타(f21 싱가포르 오피스 빌딩)만 확인했고 제조 공장·물류창고·상업 시설·가정·실외 현장 사례는 없다(제조 관련 출처는 생산 시스템 설계·실험실 수준). 국내 자료는 KCI 논문(f23, 2011) 한 건이며 국내 운영 사례는 찾지 못했다. 벤더 문서 출처 없음(MiR 블로그는 출처 상한으로 제외). L. AI·학습 기술 관련 finding(f24)은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성은 실행 조건의 현재 상태 연결로만 제안했고 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 없다. 용어집에 이미 있는 스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·어포던스·자산관리셸·계획 도메인 정의 언어·행동 트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-150 은 f28 로 부분 진전만).
```

### runs/2026-09-25-13/research.md

```markdown
# 리서치 브리프 2026-09-25-13

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-13 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 1. 주문·업무 시스템 연계 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문은 oq-002 1건, 정정 요청 없음
- 이전 실행 2026-09-25-08 이 같은 영역을 조사했으나 그 출처(ref-138~ref-187 제안분)가 참고문헌 목록에 없어 게시되지 않은 것으로 보여, 원문을 다시 열어 새 id 로 재조사함

## 조사 질문

1. 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [분류원문]
2. 로봇 관제 인터페이스(VDA 5050, Open-RMF)는 진행 중인 작업의 갱신·일시정지·취소·되감기를 어떤 메시지와 상태로 처리하며, 무엇이 바뀌지 않는가? (섹션 5·6·7 겨냥)
3. 상위 업무·실행 시스템과 하위 실행 계층 사이의 작업 요청·변경·취소는 ISA-95 계열 표준(B2MML 거래 동사, OPC UA for ISA-95 Job Control 메서드)에서 어떻게 표현되는가? (섹션 4·7 겨냥)
4. SCOR 같은 공급망 참조 모델은 주문(Order)과 이행(Fulfill)을 어떻게 나누며, 이는 ERP·WMS·TMS 와 ROP 사이 경계에 어떤 기준을 주는가? (섹션 3·9 겨냥)
5. 동적으로 도착하는 주문·긴급 주문을 진행 중인 피킹 사이클에 끼워 넣는 개입형(interventionist) 전략과 웨이브·웨이브리스 출고 지시 연구는 무엇을 보여 주는가? (섹션 6·8 겨냥)
6. 상위 시스템(WMS·MES·ERP)과 다제조사 로봇 관제를 연동한 연구·국내 실증 사례가 있는가? (섹션 5·8, 한국 자료 우선, oq-002 관련)
7. 주문·업무 시스템 연계에서 ROP가 직접 맡을 부분과 상위 업무 시스템·로봇 제조사에 맡길 부분의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 관제(fleet control)와 이동로봇 사이의 통신만 다루며, 주변 설비·외부 IT 시스템 같은 다른 통신 인터페이스와 교통 관리 로직은 범위 밖으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 에서 관제는 진행 중인 주문을 같은 orderId 에 orderUpdateId 를 올린 주문 갱신으로 바꿀 수 있지만, 이미 공개된 base 는 바꿀 수 없고(로봇이 이미 실행했다고 가정) 공개되지 않은 horizon 만 수정·삭제하거나 base 를 다르게 연장할 수 있다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 제약 | — |
| f3 | [추정] | 이번에 연 VDA 5050 3.0.0 명세에서는 주문(order) 메시지의 우선순위 필드를 찾지 못해, 로봇 인터페이스 수준에서 주문 간 우선순위를 표현하는 수단은 확인되지 않았다. | ref-031 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f4 | [사실] | VDA 5050 3.0.0 에서 이동로봇은 이전 주문의 마지막 노드와 모든 동작을 마쳤거나 cancelOrder 를 끝내 유휴 상태일 때만 다른 orderId 의 새 주문을 받으며, 진행 중에 다른 orderId 가 오면 OTHER_ORDER_ACTIVE 로 거부한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f5 | [사실] | VDA 5050 3.0.0 의 즉시 동작 cancelOrder 를 받으면 이동로봇은 가능한 한 빨리 멈추고 예정·실행 중 동작을 FAILED 로 보고하되, 취소할 수 없는 동작(cancelAllowed=false)은 끝날 때까지 RUNNING 으로 계속하며 그 뒤에 cancelOrder 가 FINISHED 가 된다. | ref-031 | 아니오 | medium | 2026-09-25 | 피킹 / 예외·성과 | — |
| f6 | [사실] | VDA 5050 3.0.0 의 즉시 동작 startPause 는 다음 노드 도달을 기다리지 않고 자동 주행을 멈추고 일시정지 가능한 동작만 멈추며, stopPause 는 주행과 동작을 재개한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 작업 요청 스키마(task_request)는 category·description 을 필수로 두고, 플릿이 지원하는 우선순위 스키마에 맞춰야 하는 priority, 최早 시작 시각, 요청 시각, 요청자, 라벨, 입찰할 수 있는 플릿 이름을 선택 필드로 둔다. | ref-138 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [사실] | Open-RMF API 는 이미 요청한 작업에 대해 task_id 로 지정하는 취소 요청(cancel_task_request), 중단 요청(interrupt_task_request), 지정한 단계의 처음부터 다시 시작시키는 되감기 요청(rewind_task_request, phase_id 필수)을 별도 스키마로 둔다. | ref-182, ref-183, ref-184 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF 작업 상태 스키마(task_state)는 상태 값 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 와 함께 배정 로봇, 최초·현재 예상 소요 시간, 완료·진행·대기 단계, 중단(interruptions)·취소(cancellation)·강제 종료(killed) 요청 정보를 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f10 | [사실] | Open-RMF 공식 문서는 작업을 /task_api_requests 토픽의 ApiRequest 로 보내며, dispatch_task_request 는 가장 적합한 플릿에, robot_task_request 는 특정 로봇에 작업을 맡기고, 별도 요청으로 작업 취소나 단계 건너뛰기를 할 수 있다고 안내한다. | ref-110 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f11 | [사실] | MESA International 의 B2MML 거래 프로파일 스키마(판 0701, 2023, ANSI/ISA-95.00.02-2018·95.00.05-2018 기반)는 거래 동사로 NOTIFY, GET, PROCESS, CHANGE, CANCEL, CONFIRM, SYNC ADD, SYNC CHANGE, SYNC DELETE 와 확장용 Other 를 정의한다. | ref-185 | 아니오 | medium | 2023 | 시작 조건 | — |
| f12 | [사실] | OPC Foundation 공식 노드셋의 OPC UA for ISA-95 Job Control(판 2.0.0, 2024-01-31)은 작업 지시 처리에 Store, StoreAndStart, Start, RevokeStart, Pause, Resume, Stop, Update, Abort, Cancel, Clear 메서드와 작업 응답 조회 메서드를 두고, 작업 지시 데이터형과 작업 응답 데이터형을 함께 정의한다. | ref-186 | 아니오 | medium | 2024-01-31 | 시작 조건 | — |
| f13 | [사실] | OPC UA for ISA-95 Job Control 명세는 Pause 로 시작된 작업 지시를 Interrupted 로, Resume 으로 다시 Running 으로 바꾸고, Abort 는 실행 중·중단·시작 전(AllowedToStart, NotAllowedToStart) 작업 지시 모두에 쓸 수 있어 Aborted 로 바꾸며, Aborted·Ended 가 된 작업 지시는 Clear 로 지운다. | ref-187 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | ISA 는 2025년 ISA-95 Part 1(ANSI/ISA-95.00.01-2025, IEC 62264-1 Mod)을 개정 발행하며, 이 표준 계열이 물류 시스템과 제조 제어 시스템의 통합을 기술하고 개정판이 기업 영역과 제조·제어 영역의 경계를 더 분명히 한다고 밝혔다. | ref-002 | 아니오 | medium | 2025-04 | — | 원문 미열람 |
| f15 | [사실] | ASCM 의 SCOR Digital Standard 는 공급망을 Orchestrate, Plan, Order, Source, Transform, Fulfill, Return 프로세스로 나누고, Order 를 위치·결제·가격·이행 상태 등 주문 데이터를 포함한 고객 구매 활동으로, Fulfill 을 배송 일정·피킹·포장·출하 등 주문 이행 활동으로 정의한다. | ref-190 | 아니오 | medium | 2025 | 출하 / 시작 조건 | 원문 미열람 |
| f16 | [사실] | Yu·Srinivas(2025)는 작업자가 피킹하고 AMR 이 운반하는 협업 동적 주문 피킹 문제(CHR-DOPP)에서 새 주문을 진행 중인 AMR·작업자 피킹 사이클에 반영하는 개입형 전략 두 가지(AMR 가용성·근접도 기반 반응형, 진행 중 사이클 교란을 줄이는 조건부형)를 제안하고, 개입 없는 협업 시스템보다 평균 주문 완료 시간과 평균 총 지연이 크게 좋았다고 보고했다. | ref-188 | 아니오 | medium | 2025 | 피킹 / 예외·성과 | 원문 미열람 |
| f17 | [사실] | Lorenz 외(2025)는 주문이 동적으로 도착하는 온라인 주문 묶음·순서·경로 문제에서 새 주문이 올 때마다 현재 해를 다시 최적화하는 재최적화(Reopt)를 수동 카트와 로봇 카트 조건에서 분석하고, 확률적 가정 아래 거의 확실하게 점근적 최적임을 보였으며 개입형·비개입형 재최적화를 구분했다. | ref-120 | 아니오 | medium | 2025 | 피킹 / 시작 조건 | 원문 미열람 |
| f18 | [사실] | Gallien·Weber(2010)는 미국 온라인 소매업체 자료로 자동 분류기가 있는 창고의 웨이브리스(연속) 출고 지시 모델을 검증하고, 제안한 웨이브리스 정책이 모든 시나리오에서 가장 좋은 웨이브 정책 이상의 처리량을 더 낮은 교착(gridlock) 확률로 냈다고 보고했다. | ref-189 | 아니오 | medium | 2010 | 포장 / 시작 조건 | 원문 미열람 |
| f19 | [사실] | Applied Sciences(2025) 게재 사례 연구는 자동차 부문 GreenAuto 프로젝트에서 여러 제조사의 AGV·AMR 을 한 지도에서 감시·관리하는 플릿 관리 소프트웨어를 만들고, MES·ERP 에는 REST API 로 정형 데이터를, 로봇 이벤트는 MQTT 로 발행하는 구조를 두며 VDA 5050 연동은 향후 과제로 설계했다. | ref-191 | 아니오 | medium | 2025 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 2025년 1월 기사에 따르면 통합 물류 플랫폼 운영사 테크타카는 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다. | ref-192 | 아니오 | low | 2025-01 | 피킹 / 수행 자원 | 원문 미열람 |
| f21 | [추정] | 확인한 로봇 인터페이스에서 진행 중 작업의 우선순위를 바꾸는 수단은 요청 시점 우선순위 지정(Open-RMF), 공개되지 않은 경로의 주문 갱신(VDA 5050), 일시정지·중단, 취소 후 재지시, 단계 되감기 정도로 보여, 출고 우선순위가 바뀔 때 어떤 작업을 끊고 무엇을 먼저 할지 정하는 규칙은 ROP 쪽 작업 대기열·재계획 로직이 맡아야 할 것으로 보인다. | ref-031, ref-138, ref-182, ref-183, ref-184 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f22 | [추정] | 상위 시스템의 변경·취소 지시(B2MML CHANGE·CANCEL, OPC UA Job Control Update·Pause·Abort)는 로봇 쪽 주문 갱신·일시정지·취소·재지시로 옮겨야 하지만, 취소할 수 없는 동작은 끝까지 수행되고 base 는 바뀌지 않으므로 번역이 일대일이 아니며, 이미 화물을 실은 뒤라면 되돌림 작업이 추가로 필요할 것으로 보인다. | ref-185, ref-186, ref-187, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f23 | [추정] | ISA-95 계열의 작업 지시–작업 응답(B2MML, OPC UA Job Control)과 VDA 5050 주문–상태, Open-RMF 작업 요청–작업 상태는 모두 요청–응답 구조이지만 이번 검색 범위에서 이들을 서로 옮기는 표준 매핑은 확인되지 않았고, 확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다. | ref-031, ref-186, ref-138, ref-111, ref-191 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f24 | [추정] | 연계 대상: 주문 접수·출고 지시 방식(웨이브·웨이브리스)과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP 는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 진행·완료·취소 결과를 되돌리는 경계에 서는 것으로 보인다. | ref-190, ref-189, ref-002, ref-138 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f25 | [추정] | 동적 피킹 연구(개입형 전략, 재최적화)가 진행 중 사이클에 새 주문을 반영할 때 완료 시간·지연이 개선됨을 보이므로, ROP 는 대기열 수준 재정렬만이 아니라 실행 중 작업의 수정도 지원하되 교란 비용을 조건으로 판단하는 구조가 필요할 것으로 보인다. | ref-188, ref-120 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-002 | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | 기사 | medium | 2026-09-25 | https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of | 예 |
| ref-138 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-182 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-183 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 아니오 |
| ref-184 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-185 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 아니오 |
| ref-186 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | high | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-187 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 | 예 |
| ref-188 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-120 | Lorenz 외 (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-189 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-190 | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 2025 | 표준 | medium | 2026-09-25 | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf | 예 |
| ref-191 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2076-3417/15/13/7235 | 예 |
| ref-192 | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 2025-01 | 기사 | low | 2026-09-25 | https://news.mt.co.kr/mtview.php?no=2025012116183583251 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1·f23(로봇 인터페이스는 상위 연계를 규정하지 않아 번역 계층 필요), f15(SCOR 의 Order·Fulfill 구분) / 섹션 4: f2(주문 갱신·base·horizon), f11(B2MML 거래 동사), f12·f13(작업 지시·작업 응답과 상태), f9(작업 상태), f18(웨이브·웨이브리스 출고 지시) / 섹션 5: 출하 우선순위 변경 f21(시작 조건·예외·성과)·f2·f3, 피킹 중 취소 f5·f22(예외·성과), 피킹 수행 자원 f16·f20, 포장·출고 지시 f18 — 흐름 단계와 여섯 항목 명시 / 섹션 6: f2·f4·f5·f6·f7·f8·f10·f21·f22·f25 / 섹션 7: f1~f6(VDA 5050 3.0.0), f7~f10(Open-RMF 작업 API), f11(B2MML), f12·f13(OPC UA for ISA-95 Job Control), f14(ISA-95 Part 1 2025), f15(SCOR DS) / 섹션 8: f16·f17·f18·f19, 국내 사례 f20(기사, 발표 단계임을 명시) / 섹션 9: f24(연계 대상: 출고 지시·우선순위 결정), f1, f23 / 섹션 10: 2. 공정·워크플로 모델링(f12), 9. 로봇·제조사 관제 연동(f1·f2·f10), 12. 명령·작업 실행의 신뢰성(f4·f8), 13. 작업 배정 — MRTA(f10·f16), 14. 작업 순서·스케줄링(f17·f21), 20. 예외 복구·재계획·업무 연속성(f5·f22), 28. 표준·상호운용성·다사업자 거버넌스(f23) / 섹션 11: open_questions_new 3건과 기존 oq-002 연결(f20) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 작업 지시 | Job Order (ISA-95) | ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다. |
| B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International 이 ISA-95(IEC 62264)의 데이터 모델과 거래를 XML 스키마로 구현한 교환 형식이다. |
| 웨이브리스 출고 지시 | Waveless Order Release | 주문을 큰 묶음(웨이브)으로 모아 내리지 않고 도착·여유 용량에 따라 연속으로 현장에 내려보내는 출고 지시 방식이다. |

## 열린 질문

새로 생긴 질문:

- 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | 관련 영역: 1. 주문·업무 시스템 연계, 14. 작업 순서·스케줄링 | 근거: f21 | 종류: 일반
- ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 1. 주문·업무 시스템 연계, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f23 | 종류: 일반
- 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | 관련 영역: 1. 주문·업무 시스템 연계, 20. 예외 복구·재계획·업무 연속성 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 규격마다 발행 기관 한 곳의 원문만 있고(Open-RMF 스키마 4건은 같은 저장소), 논문은 단일 출처
    - f3 VDA 5050 order 메시지 우선순위 필드 부재는 열람 도구 응답 기준이며 order.schema 직접 대조 안 함
    - f13 OPC 10031-4 상태 전이는 검색 요약만 확인(ref-187 원문 미열람), 노드셋 CSV 로는 메서드 이름만 확인
    - f14·f15·f16·f17·f18·f19 원문 미열람(검색 요약 범위만 사용)
    - f20 국내 실증은 발표 기사뿐이며 결과 미확인
    - ref-120 제1저자 이름 전체와 ref-191 저자 미확인
    - ref-031·ref-138~ref-110 발행일 미확인
    - TMS 연계(운송 마감·도크 배정)와 MES 생산 지시 연계는 1차 자료를 충분히 찾지 못함
- 범위 경계 위반 의심:
    - f24: 출고 지시 정책·우선순위 결정은 분류 원문 9장 '상위 업무 시스템' 쪽이므로 '연계 대상: '으로 표시함
    - f18: 웨이브·웨이브리스 출고 지시는 WMS·WES 정책이므로 ROP 직접 범위가 아니라 입력 조건으로만 쓰도록 제안
- 한계: fetch_mode mirror_only(web_fetch_available: false): raw.githubusercontent.com 공식 저장소 원문(VDA 5050 main 명세, Open-RMF rmf_api_msgs 스키마 5건과 task_new 원본, B2MML 거래 프로파일 스키마, OPC UA ISA-95 Job Control 노드셋)은 열어 fetched=true 로 표시했다. ISA 보도자료·OPC 온라인 참조·ASCM 문서·논문 4건·기사는 원문 미열람(신뢰도 상한 medium, 기사 low). 교차 확인 0건. 검색 20회/30, 신규 출처 15건/15(ref-138~ref-192, next_ref_id 기준)로 출처 상한에 도달해 Ceven·Gue(2017) 웨이브 출고 시각 연구, Open-RMF 입찰(task.md) 문서, SYNAOS 벤더 글(WMS/ERP–VDA 5050 번역 주장), 씨메스 벤더 블로그(WES 우선순위 재정렬 주장)는 넣지 못했다. 재사용 출처 2건(ref-031, ref-002). 이전 실행 2026-09-25-08 이 같은 영역을 조사했으나 그 출처 id 가 참고문헌 목록에 없어 게시되지 않은 것으로 보고 원문을 다시 열어 새 id 로 기록했다(같은 URL 이 이전 브리프의 ref-138~ref-187 제안과 겹치므로 퍼블리셔 확인 필요). 한국 자료는 기사 1건(발표 단계)뿐이며 학술·공공 자료는 한국어 검색 4회에서 찾지 못했다. oq-002 는 해결하지 못했다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다.
```

### runs/2026-09-25-08/research.md

```markdown
# 리서치 브리프 2026-09-25-08

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-08 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 1. 주문·업무 시스템 연계 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음

## 조사 질문

1. 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [분류원문]
2. 상위 업무·실행 시스템(ERP·MES·WMS)과 하위 실행 계층 사이의 작업 요청·응답은 표준(ISA-95, B2MML, OPC UA for ISA-95)에서 어떤 단위와 동사로 표현되는가? (섹션 4·7 겨냥)
3. 로봇 관제 인터페이스(VDA 5050, Open-RMF)는 작업의 변경·취소·거부를 어떤 메시지와 상태로 처리하는가? (섹션 5·6 겨냥)
4. 상위 시스템의 변경·취소 지시를 진행 중인 로봇 작업으로 옮길 때 어떤 변환 규칙과 한계가 있는가? (섹션 6·9 겨냥)
5. 로봇 기반 풀필먼트의 운영 의사결정(주문 배정–작업 생성–작업 배정–경로)은 연구에서 어떻게 나뉘는가? (섹션 8·10 겨냥)
6. 국내 물류센터에서 WMS·WES·WCS 와 로봇 연동 역할 분담을 설명하는 자료가 있는가? (한국 자료 우선, 섹션 3·9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 에서 관제는 진행 중인 주문을 같은 orderId 를 유지하고 orderUpdateId 를 올린 주문 갱신으로 확장하며, 이미 공개(base)된 노드의 sequenceId 와 결정 지점의 내용은 바꾸지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f2 | [사실] | VDA 5050 3.0.0 의 즉시 동작 cancelOrder 를 받으면 이동로봇은 가능한 한 빨리 멈추고, 예정 동작은 FAILED 로 보고하며, 모든 이동과 동작이 멈춘 뒤 cancelOrder 가 FINISHED 가 되고 로봇은 새 주문을 받을 수 있는 유휴 상태가 된다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 3.0.0 은 주문 거부 사유로 OUTDATED_ORDER_UPDATE(더 낮은 orderUpdateId), OTHER_ORDER_ACTIVE(진행 중 주문과 다른 orderId), ORDER_UPDATE_FOLLOWING_CANCEL(취소 뒤 갱신), INVALID_ORDER_ACTION 등의 오류 유형을 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 명세의 범위는 관제(fleet control)와 이동로봇 사이 통신이며, 관제가 WMS·ERP 같은 상위 시스템에서 주문을 받는 인터페이스는 규정하지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | Open-RMF 작업 요청 스키마(task_request)는 category 와 description 을 필수로, 우선순위(priority), 최早 시작 시각(unix_millis_earliest_start_time), 요청자(requester), 라벨(labels), 허용 플릿(fleet_name)을 선택 필드로 둔다. | ref-110 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f6 | [사실] | Open-RMF 작업 취소 요청(cancel_task_request)은 type 과 취소할 task_id 를 필수로, 취소 목적을 적는 labels 를 선택으로 둔다. | ref-111 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 작업 상태 스키마(task_state)는 상태 값으로 uninitialized, blocked, error, failed, queued, standby, underway, delayed, skipped, canceled, killed, completed 를 두고, 배정 로봇(assigned_to)·예상 소요 시간·중단(interruptions)·취소(cancellation)·강제 종료(killed) 정보를 함께 담는다. | ref-112 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f8 | [사실] | Open-RMF 에서 작업은 /task_api_requests 토픽의 ApiRequest 로 보내며, dispatch_task_request 는 가장 적합한 플릿에, robot_task_request 는 특정 로봇에 작업을 맡긴다. | ref-113 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f9 | [사실] | B2MML 은 MESA International 이 공개한 ISA-95(IEC/ISO 62264) 데이터 모델의 XML 스키마(XSD) 구현으로, ERP·공급망 시스템과 제조 실행·제어 시스템의 통합에 쓰인다. | ref-114 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | B2MML 거래 프로파일 스키마는 거래 동사로 NOTIFY, GET, PROCESS, CHANGE, CANCEL, CONFIRM, SYNC ADD, SYNC CHANGE, SYNC DELETE 와 확장용 Other 를 정의한다. | ref-115 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f11 | [사실] | ISA-95 의 운영 관리 활동 모델에서 작업 일정(work schedule)은 하나 이상의 작업 요청(work request)으로, 작업 요청은 하나 이상의 작업 지시(job order)로 이루어지고, 실행된 작업은 작업 응답(job response)으로 보고되는 요청–응답 순환을 이룬다. | ref-116 | 아니오 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f12 | [사실] | OPC UA for ISA-95 Part 4: Job Control 은 작업 지시 수신 객체에 Store·StoreAndStart·Update·Abort·RevokeStart·Pause·Resume 메서드를 두며, Abort 는 실행 중·중단·시작 전 작업 지시 모두에 쓸 수 있고 상태를 Aborted 로 바꾼다. | ref-116 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Merschformann 외는 로봇 이동식 풀필먼트 시스템(RMFS)의 운영 의사결정을 주문 배정(주문을 작업대에), 작업 생성, 로봇에 대한 작업 배정, 경로 계획의 네 단계로 나눈다. | ref-117 | 아니오 | medium | 2018-01 | 피킹 / 수행 자원 | 원문 미열람 |
| f14 | [추정] | 국내 로봇 기업 블로그는 WMS 가 창고 업무 관리를, WES·WCS 가 실행을 맡으며 WES 가 WMS 주문 정보를 바탕으로 출고 시간·SKU 수·주문 난이도에 따라 작업 우선순위를 자동 재정렬한다고 설명한다. | ref-118 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | 원문 미열람, 벤더 주장 |
| f15 | [추정] | ISA-95 의 작업 지시–작업 응답 순환과 VDA 5050 주문–상태, Open-RMF 작업 요청–작업 상태는 모두 요청–응답 구조이지만, 이번 검색 범위에서 이들을 서로 옮기는 표준 매핑은 확인되지 않았다. | ref-116, ref-031, ref-110, ref-112 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f16 | [추정] | 진행 중인 로봇 작업의 우선순위를 바꾸려 할 때 로봇 인터페이스 수준에서 쓸 수 있는 수단은 주문 갱신(공개되지 않은 경로의 연장), 취소 후 재지시(VDA 5050 cancelOrder, Open-RMF cancel_task_request), 요청 시점의 우선순위 지정 정도로 보여, 우선순위 변경 규칙 자체는 ROP 쪽 작업 대기열에서 정해야 할 것으로 보인다. | ref-031, ref-110, ref-111 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f17 | [추정] | 상위 시스템의 변경·취소 지시(B2MML CHANGE·CANCEL, OPC UA Job Control Update·Abort)는 로봇 쪽의 주문 갱신·취소·재지시로 번역해야 하며, 로봇이 이미 싣거나 옮긴 뒤라면 되돌림 작업이 추가로 생길 수 있어 번역이 일대일이 아닐 것으로 보인다. | ref-115, ref-116, ref-031, ref-111 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f18 | [추정] | 연계 대상: 주문을 작업대·웨이브에 배정하고 재고를 할당하는 결정은 WMS·WES 등 상위 시스템의 몫이고, ROP는 작업 지시를 받아 로봇 작업으로 바꾸고 작업 응답(진행·완료·취소 결과)을 되돌리는 경계에 서는 것으로 보인다. | ref-116, ref-117, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-110 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-112 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-113 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-114 | MESA International | MESAInternational/B2MML-BatchML — README | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML | 아니오 |
| ref-115 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 아니오 |
| ref-116 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control (OPC 10031-4) | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/ | 예 |
| ref-117 | Merschformann, M. 외 | Decision Rules for Robotic Mobile Fulfillment Systems | 2018-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1801.06703 | 예 |
| ref-118 | 씨메스(CMES Robotics) | 물류 자동화 시스템을 이해하는 첫 걸음 : WES · WCS · WMS, 무엇이 다를까요? | 미확인 | 벤더 문서 | low | 2026-09-25 | https://blog.cmesrobotics.ai/wes-wcs-wms | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4·f15(로봇 인터페이스는 상위 연계를 규정하지 않아 번역 계층이 필요) / 섹션 4: f11·f12(작업 지시·작업 응답), f10(B2MML 거래 동사), f7(작업 상태) / 섹션 5: f14·f16(출하 우선순위 변경 — 시작 조건·예외·성과), f17(피킹 중 취소 — 예외·성과), f13(피킹 수행 자원) / 섹션 6: f1·f2·f3·f5·f6·f16·f17 / 섹션 7: f9·f10(B2MML), f11·f12(OPC UA for ISA-95 Job Control), f1~f4(VDA 5050), f5~f8(Open-RMF 작업 API) / 섹션 8: f13 / 섹션 9: f18(연계 대상: 주문 배정·재고 할당), f4 / 섹션 10: 2. 공정·워크플로 모델링(f11), 12. 명령·작업 실행의 신뢰성(f3·f6), 13. 작업 배정 — MRTA(f13), 14. 작업 순서·스케줄링(f16), 20. 예외 복구·재계획·업무 연속성(f2·f17), 9. 로봇·제조사 관제 연동(f1·f8) / 섹션 11: open_questions_new 2건. f14 는 벤더 주장 병기 필수 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 작업 지시 | Job Order (ISA-95) | ISA-95 에서 작업 센터가 실행할 작업 단위의 요청으로, 작업 요청(work request)을 이루는 구성 요소이다. |
| 작업 응답 | Job Response (ISA-95) | ISA-95 에서 작업 지시에 대해 수행된 작업을 보고하는 정보이다. |
| B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International 이 공개한 ISA-95 데이터 모델의 XML 스키마 구현이다. |

## 열린 질문

새로 생긴 질문:

- ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 1. 주문·업무 시스템 연계, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f15 | 종류: 일반
- 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | 관련 영역: 1. 주문·업무 시스템 연계, 20. 예외 복구·재계획·업무 연속성 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 10 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 9건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 규격별로 발행 기관 한 곳의 원문만 있음
    - f2·f3 는 VDA 5050 명세를 요약 도구 경유로 읽어 오류 유형 문자열의 글자 단위 일치 미확인
    - f11·f12 OPC UA for ISA-95 Job Control 원문 미열람(검색 요약), 판별 차이 미확인
    - f13 ref-117 원문 미열람
    - f14 벤더 주장이며 독립 출처 없음
    - VDA 5050 주문 메시지의 우선순위 필드 유무 미확인(f16)
    - ref-031·ref-110~ref-116·ref-118 발행일 미확인
- 범위 경계 위반 의심:
    - f18: 주문 배정·재고 할당은 분류 원문 9장 '상위 업무 시스템' 쪽이므로 '연계 대상: '으로 표시함
- 한계: 재실행 1회차(스키마 불일치 반려). 반려 사유 1(f20: 벤더 문서만 근거로 한 사실 태그에 vendor_claim 없음): 직전 반환값이 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 다시 작성했고, 벤더 문서(ref-118)만 근거로 한 주장은 f14 하나로 두어 vendor_claim true·태그 추정·신뢰도 low·evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 이번 브리프의 finding 번호는 직전 반환값과 대응하지 않는다. fetch_mode mirror_only: VDA 5050 명세, Open-RMF rmf_api_msgs 스키마 3건과 task_new 원본, B2MML README·거래 프로파일 스키마는 raw.githubusercontent.com 으로 열었다(fetched true). OPC 10031-4, arXiv 논문, 벤더 블로그는 원문 미열람(신뢰도 상한 medium). 검색 7회/30, 신규 출처 9건/15(ref-110~ref-118), 재사용 1건(ref-031). ref-001 SCOR·ref-002 ISA-95 는 이번 주장의 근거로 쓰지 않아 넣지 않았다. 한국 자료는 벤더 블로그 1건뿐이며 공공기관·학술 자료는 찾지 못했다. ERP·TMS·MES 연계 사례와 SCOR 관점 서술은 조사하지 못해 섹션 3·8 근거가 얇다. 27. AI·학습·적응과 모델 운영 관련 finding 없음.
```
