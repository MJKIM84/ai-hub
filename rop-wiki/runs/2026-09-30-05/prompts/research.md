(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-05
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 41. 플랫폼 아키텍처·외부 API (K. 플랫폼 아키텍처·인프라)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1023
- 새 출처 id 구간: ref-1023 ~ ref-1052 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1023 부터 순서대로 쓰고 ref-1052 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-05/target.json

```json
{
  "run_id": "2026-09-30-05",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 114,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 41,
    "area_name": "41. 플랫폼 아키텍처·외부 API",
    "category": "K. 플랫폼 아키텍처·인프라",
    "category_letter": "K"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=41"
}
```

### docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 41
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 41. 플랫폼 아키텍처·외부 API

# 41. 플랫폼 아키텍처·외부 API

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **클라우드·현장 서버·로봇 역할 분담**: 어떤 판단과 데이터를 클라우드·현장 서버·로봇 가운데 어디에 둘지 정한다
- **플랫폼 기준 아키텍처**: 서비스 분리, 이벤트 구조, 제조사 중립성을 갖춘 플랫폼 구조를 정한다
- **외부 API·SDK 제공**: 다른 시스템과 개발자가 플랫폼을 부를 수 있는 API·웹훅·SDK·문서를 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’에서 왔다. 그 본문은 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]

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

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md (요약)

```markdown
# 42. 분산 시스템·통신·컴퓨팅 구조

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 네트워크**: 와이파이 로밍·5G·사설망, 지연·대역폭·음영 구역을 설계하고 점검한다
- **연결이 끊겨도 계속 운영**: 인터넷이나 서버가 끊겨도 현장에서 어디까지 계속 운영할지 정하고 구현한다
- **다현장 운영 구조**: 여러 현장을 한 플랫폼에서 나누어 운영하는 구조를 만든다
- **확장성·성능**: 로봇과 작업 수가 늘어도 처리 성능을 유지한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 [옛 분류원문]

> 옛 질문: 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [옛 분류원문]

## 2. 핵심 질문

인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md (요약)

```markdown
# 43. 데이터·관측성·배포

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1022건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 274개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
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
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
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

### docs/open-questions.md (요약: 대상 영역 [41] 에 걸린 0건 / 전체 205건)

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

### runs/2026-09-30-04/research.md

```markdown
# 리서치 브리프 2026-09-30-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-04 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 16. 장소 의미·지도 관리 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 지도 버전(mapId·mapVersion), 구역 집합(zoneSet), 대체 이름(alt_name), 의미 지도, 3차원 장면 그래프 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(청소 로봇 의미 지도 갱신), 병원(평면도 주요 위치 주석), 기타(로봇 친화형 건축물 정밀지도) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 장소 이름 레지스트리, 지도·구역 집합 버전 배포·활성화, 차선 폐쇄, 지도 변경 감지·갱신, 계층형 의미 지도 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 지도·구역, LIF, IMDF, IEEE 1873, Open-RMF 교통 편집기·LaneRequest, osmAG 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]
2. 장소의 이름·별칭·용도·접근 제한을 표현하는 표준·오픈소스 모델(IMDF, Open-RMF 교통 편집기, LIF, IEEE 1873, 계층형 의미 지도)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)
3. 지도 버전과 임시 통제 구역은 로봇–관제 인터페이스(VDA 5050, Open-RMF)에서 어떻게 배포·활성화·폐기되며 누가 책임지는가? (섹션 6·7·9 겨냥)
4. 공간이 바뀔 때 지도와 장소 의미를 갱신하는 연구와 운영 사례(가정·물류창고·병원 등)는 무엇이며 어떤 결과를 보고하는가? (섹션 5·8 겨냥)
5. 국내 공간정보·건축물 인증 체계는 로봇용 지도·장소 정보를 어떻게 다루는가? (섹션 3·5 겨냥, 한국 자료 우선)
6. 장소 의미·지도 관리에서 ROP가 직접 맡을 것과 로봇 자체 지도 작성·갱신, 건물 데이터 소유자, 설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)
7. oq-193 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추는가? (섹션 5·11 겨냥; oq-188·oq-190 은 11절 반영 대상으로만 확인)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세에서 지도는 작업 공간 구역을 가리키는 mapId 와 갱신을 나타내는 mapVersion 의 조합으로 식별되고 상태는 ENABLED·DISABLED 이며, 관제(fleet control)가 downloadMap·enableMap·deleteMap 즉시 동작으로 지도 서버의 지도를 로봇에 내려받게 하고 활성화하되 같은 mapId 에서는 한 버전만 활성화된다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f2 | [사실] | VDA 5050 3.0.0 명세는 올바른 지도가 활성화되도록 보장하는 책임을 관제에 두고, 로봇이 스스로 지도를 지우지 못하게 하며 사용 중인 지도의 삭제 요청은 로봇이 거부하게 한다. | ref-031 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f3 | [사실] | VDA 5050 3.0.0 명세는 진입 금지(BLOCKED)·유도선 주행(LINE_GUIDED)·해제(RELEASE)·재계획 조율·속도 제한·동작 구역과 우선·벌점·방향 구역을 구역 유형으로 두고, 구역 묶음(zoneSet)은 전역 고유 zoneSetId 를 가지며 mapVersion 이 아니라 mapId 에 묶이고 mapId 당 하나만 활성화되며 내용이 바뀌면 새 zoneSetId 가 필요하다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f4 | [사실] | VDA 5050 3.0.0 명세는 경로·경로망·스테이션 정의 같은 설정을 구현 단계의 일로 보고 명세 범위 밖에 두며, 구현 단계에서 LIF(Layout Interchange Format)로 경로를 관제에 가져올 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDMA 의 LIF 는 무인운반차 통합사업자가 궤도 레이아웃(에지·노드·스테이션의 모음)을 제3자 상위 관제 시스템으로 넘기기 위한 교환 형식이며, 공식 저장소 README 기준 1.0.0 판은 2023-09 에 나왔다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f6 | [사실] | IMDF 의 Unit(실내의 구별되는 공간)은 기능 분류(category)·접근 제한(restriction)·접근성(accessibility)·이름(name)·대체 이름(alt_name)·표시 지점(display_point)·소속 층(level_id)을 속성으로 가지며, 분류에는 승강기·에스컬레이터·계단·경사로·방·화장실·비공개 구역 등이 있다. | ref-1026 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f7 | [사실] | IMDF 용어집에서 이름(name)은 현실에 물리적으로 있고 보행자에게 표시되어야 할 기준 레이블이고, 대체 이름(alt_name)은 공간·물체·서비스를 가리키는 동의어로 색인·질의·검색에 쓰이며, 접근 제한(restriction)은 직원 전용처럼 일반 대중의 일부에게만 허용된 공간을 나타낸다. | ref-1027 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f8 | [사실] | OGC 는 IMDF 1.0.0 을 커뮤니티 표준 20-094 로 2021-02-02 승인하고 2021-02-18 게시했으며, 이 표준은 venue·building·level·unit·opening·fixture·anchor·occupant·geofence 등 16개 지형지물 유형을 정의한다. | ref-1028 | 아니오 | medium | 2021-02-18 | — | — |
| f9 | [사실] | Open-RMF 교통 편집기에서 로봇이 어떤 경유점에서 끝나는 작업을 주려면 그 경유점에 이름을 붙여야 하며, 경유점에는 주차(is_parking_spot)·대기(is_holding_point)·충전(is_charger)·디스펜서·인제스터 같은 속성을 달고, 층별 경유점(좌표·높이·이름)·벽·문·차선을 담은 .building.yaml 을 building_map_generator 로 항법 그래프로 내보내 플릿 어댑터가 쓴다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | Open-RMF 의 차선 요청 메시지(LaneRequest)는 플릿 이름과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어져, 지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 열게 한다. | ref-569 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f11 | [사실] | 에스토니아 타르투 대학병원 현장 시험에서는 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소와 함께 주요 위치를 주석해 로봇 운반 작업의 목적지를 정했고, 이 지도로 중환자실에서 검사실까지 혈액 검체를 운반했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 작업 대상 | 원문 미열람 |
| f12 | [사실] | Narayana 외(IROS 2020)는 실제 가정의 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도(lifelong semantic map)에서, 로봇 원시 지도가 주행마다 달라져도 사용자와 공유하는 의미 정보를 새 지도로 옮기고(공간 의미 전이), 메타 의미 계층으로 동적 물체 때문에 생긴 의미 충돌을 찾아 해소하며, 새로 탐색한 공간의 의미를 찾아 더하는 방법을 제시했다. | ref-1036 | 아니오 | medium | 2020-10 | 가정 / 작업 대상 | — |
| f13 | [사실] | 연계 대상: Stefanini 외(Sensors, 2023)의 LiDAR 점유 격자 지도 갱신 알고리즘은 격자 변화가 여러 스캔에서 반복될 때만(버퍼 10회 중 7회 이상) 지도에 반영하고, 감지된 변화량이 위치 추정 오류가 의심되는 범위이면 갱신을 멈춰 지도 오염을 막으며, 모의 창고 100개 시나리오와 80 m² 실험실에서 갱신 지도로 평균 위치 오차를 10 cm 아래(정적 지도는 50 cm 초과)로 유지했다고 보고했다. | ref-1037 | 아니오 | medium | 2023-07 | 예외·성과 | — |
| f14 | [사실] | Hughes 외(IJRR)는 3차원 장면 그래프를 물체·장소·방·건물 같은 추상화 층으로 환경을 묶는 계층형 공간 표현으로 제시하고, 시각·관성 데이터로 이를 실시간 구축하는 공개 소스 시스템 Hydra 를 Clearpath Jackal·Unitree A1 로봇으로 시험했다. | ref-347 | 아니오 | medium | 2023-05 | — | — |
| f15 | [사실] | Feng 외의 osmAG 는 OpenStreetMap XML 형식 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담는 파일 형식으로, 기존 OSM 도구로 사람이 읽고 고칠 수 있으며 로봇의 이동 방식과 속성을 고려한 전역 경로 계획을 지원하는 ROS 연동 C++ 라이브러리를 함께 제공한다. | ref-1031 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Xie·Schwertfeger·Blum 의 osmAG-LLM(RA-L 2026 채택)은 금방 낡는 고정밀 물체 지도 대신 osmAG 의미 지도를 환경 맥락으로 쓰고 대규모 언어 모델(LLM)이 방 속성 같은 지도 단서로 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 해, 동적·미기록 대상에서 기존 방법보다 나은 탐색 성공을 보고했다. | ref-1032 | 아니오 | medium | 2025-07 | — | — |
| f17 | [사실] | IEEE 1873-2015(Robot Map Data Representation for Navigation)는 항법하는 이동 로봇의 2차원 메트릭·위상 지도에 대한 데이터 모델과 데이터 형식을 정한 IEEE 로봇자동화학회(RAS) 표준으로 2015-09-03 승인·2015-10-26 발행됐으며, 10년 안에 개정되지 않아 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다. | ref-1033 | 아니오 | medium | 2026-03-26 | — | — |
| f18 | [사실] | 지디넷코리아(2022-04-11)에 따르면 네이버 제2사옥 1784 는 스마트도시협회가 처음 실시한 로봇 친화형 건축물 인증(4개 부문·25개 평가 범주)을 받았고, 평가위원은 이 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공하며 이동형 서비스 로봇의 승강기 이동을 지원한다고 평가했다. | ref-956 | 아니오 | low | 2022-04-11 | 기타 / 수행 자원 | — |
| f19 | [사실] | 국토지리정보원은 지하철·철도역사와 평창동계올림픽 관련 시설 등을 대상으로 LoD2 수준의 실내공간정보(2차원 도면·3차원 성과, shp·3ds·max 형식)를 구축해 공간정보 오픈 플랫폼(브이월드)으로 제공하며, 활용처로 길안내·시설물관리·안전·소방을 들고 로봇 활용은 언급하지 않는다. | ref-1035 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에 대해, 같은 이름은 장소마다 고유 식별자·기준 이름·별칭·용도 분류·접근 제한을 둔 장소 목록을 지도 요소(경유점·공간·스테이션)에 묶는 방식으로 표현되고(f6·f7·f9), 공간 변경은 지도 자체의 버전 교체(mapId·mapVersion)와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 나뉘어 관리되는 것으로 보인다(f1·f3·f10). | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇이 만든 원시 지도는 주행과 환경 변화에 따라 계속 달라지는데(f12·f13) 작업 목적지와 사용자 대화는 장소 이름으로 이루어지므로 이름과 지도 요소의 연결을 버전이 바뀌어도 유지해야 하고, VDA 5050 이 올바른 지도 활성화 책임을 관제에 두므로(f2) 여러 제조사 로봇을 묶는 ROP 가 그 책임을 이어받게 되기 때문이다. | ref-1036, ref-1037, ref-031, ref-079 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 16. 장소 의미·지도 관리에서 ROP 가 직접 맡을 범위는 장소 목록(식별자·이름·별칭·용도·접근 제한)의 관리와 제조사별 지도 요소와의 연결(f6·f7·f9), 제조사별 지도·구역 집합의 버전 기록과 배포·활성화 지시(f1·f2·f3), 공사·청소 같은 임시 통제 구역과 차선 폐쇄의 선언·해제(f3·f10), 사람이 층·공간·장소를 고치는 편집 화면과 변경 이력이다. | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM 지도 작성·점유 격자 갱신·장면 그래프 구축 같은 센서 기반 지도 생성(f13·f14)은 로봇 자체 지능·제어에, 공공 실내공간정보·BIM 같은 건물 공간 데이터의 구축·갱신(f19)은 건물·공공 데이터 소유자에, 승강기 운행은 시설·설비 제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 만든 지도·데이터를 받아 장소 의미를 붙이고 버전을 관리하는 인터페이스를 맡을 것으로 보인다. | ref-1037, ref-347, ref-1035, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 기준 평면도를 주는 14. 도면·BIM에서 지도 만들기(f11), 좌표 정렬·공간 그래프를 다루는 15. 지도·공간·위치 모델(f9·f15), 대화로 지도를 고치고 장소 이름을 찾는 8. 채팅으로 맵 작성과 12. 채팅으로 업무 지시·오케스트레이션(f7·f16), 현재 활성 지도 버전·폐쇄 구역을 알아야 하는 18. 실시간 세계 상태·데이터 일관성(f1·f10), 차선 폐쇄를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f10), 지도 교환 표준을 다루는 21. 상호운용 표준·적합성(f5·f8·f17), 버전 이력을 다루는 57. 자산·소프트웨어 수명주기 관리(f1), 접근 제한 공간을 다루는 51. 인증·권한·격리(f7), 장면 이해를 다루는 45. 문서·도면·장면 이해(f14·f16), 적용 현장인 63. 병원·의료(f11)·65. 가정·공동주택(f12)·67. 기타 현장(f18)과 이어진다. | ref-869, ref-079, ref-1031, ref-1027, ref-1032, ref-031, ref-569, ref-046, ref-1028, ref-1033, ref-347, ref-1036, ref-956 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-1026 | Apple (Apple Business Register) | Unit - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/types/unit | 아니오 |
| ref-1027 | Apple (Apple Business Register) | Glossary - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/glossary | 아니오 |
| ref-1028 | Open Geospatial Consortium (OGC) | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 2021-02-18 | 표준 | high | 2026-09-30 | https://docs.ogc.org/cs/20-094/index.html | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (IJRR) | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 2023-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2305.07154 | 아니오 |
| ref-1031 | Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv) | osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics | 2023-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2309.04791 | 아니오 |
| ref-1032 | Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv) | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.12753 | 아니오 |
| ref-1033 | IEEE Standards Association (IEEE RAS) | IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation | 2015-10-26 | 표준 | medium | 2026-09-30 | https://standards.ieee.org/standard/1873-2015.html | 아니오 |
| ref-956 | 지디넷코리아 | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 2022-04-11 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20220411142336 | 아니오 |
| ref-1035 | 국토지리정보원 | 실내공간정보 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.ngii.go.kr/kor/content.do?sq=324 | 아니오 |
| ref-1036 | Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020) | Lifelong update of semantic maps in dynamic environments | 2020-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2010.08846 | 아니오 |
| ref-1037 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066) | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 2023-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/ | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(원시 지도 변화와 이름 기반 작업·관제 책임), f20(핵심 질문 답, 추정) / 섹션 4: 지도 버전 f1, 구역 집합 f3, 이름·대체 이름·접근 제한 f6·f7, 의미 지도 f12, 3차원 장면 그래프 f14 / 섹션 5: 병원 — f11(타르투 대학병원 평면도 주요 위치 주석, 재인용), 가정 — f12(청소 로봇 의미 지도 갱신), 기타 — f18(네이버 1784 정밀지도·측위 인프라, 기사 기준 신뢰도 low). 여섯 항목 중 시작 조건·완료·인계 근거는 부족함을 명시. 물류창고 사례는 모의 실험(f13)뿐이라 현장 사례로 쓰지 않음 / 섹션 6: 장소 목록과 지도 요소 연결 f6·f7·f9, 지도 버전 배포·활성화 f1·f2, 임시 통제 구역 f3·차선 폐쇄 f10, 지도 변경 감지·갱신 f13(연계 대상), 평생 의미 지도 f12, 계층형 의미 지도 f14·f15, LLM 과 의미 지도 f16 / 섹션 7: VDA 5050 f1~f4, LIF f5, IMDF f6~f8, Open-RMF f9·f10, IEEE 1873 f17(비활성 보류 명시), osmAG f15 / 섹션 8: f12~f16, f19(국내 공공 실내공간정보) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 8, 12, 14, 15, 18, 21, 27, 45, 51, 57, 63, 65, 67 / 섹션 11: 기존 oq-188·oq-190·oq-193 과 open_questions_new 5건. 다음 실행 후보: 21. 상호운용 표준·적합성 페이지에 f5·f8·f17 반영, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 지도 버전 | Map Version (VDA 5050 mapId / mapVersion) | 같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 에서는 관제가 내려받게 한 여러 버전 가운데 한 버전만 활성화해 로봇이 쓰게 한다. |
| 대체 이름 | Alternative Name (IMDF alt_name) | IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다. |
| 의미 지도 | Semantic Map | 기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다. |
| 3차원 장면 그래프 | 3D Scene Graph | 물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다. |

## 열린 질문

새로 생긴 질문:

- 제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 15. 지도·공간·위치 모델 | 근거: f1 | 종류: 일반
- IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성 | 근거: f17 | 종류: 일반
- 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 40. 운영 절차·요청 창구, 63. 병원·의료 | 근거: f3 | 종류: 일반
- IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 12. 채팅으로 업무 지시·오케스트레이션 | 근거: f7 | 종류: 일반
- 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 67. 기타 현장 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 13건
- 미확인 항목:
    - f5 LIF 스키마의 layoutVersion·stationName 등 필드는 검색 요약에만 나와 README·스키마 원문으로 확인하지 못함(GitHub 저장소 페이지 403, VDMA 가이드라인 PDF 본문 추출 실패)
    - f13 수치는 저자 보고이며 교차 확인 실패
    - f14·f15·f16·f12 는 초록 기준이며 본문 실험 조건 미확인
    - f17 IEEE 1873 표준 본문(유료) 미열람, Amigoni 외 해설 논문(oru.diva-portal.org)은 ECONNRESET 으로 열지 못함
    - f18 기사 기준이며 스마트도시협회 인증 원자료 미확인
    - Nav2 금지 구역·속도 필터(costmap filter) 문서는 docs.nav2.org·raw 경로 404, navigation.ros.org 연결 거부로 열지 못해 넣지 않음
    - MiR 지도 편집기(바닥 계층과 구역·위치 구성 요소, 로봇 수 제한 구역)는 PDF 본문 추출 실패로 넣지 않음
    - oq-193 건설 현장 지도–BIM 동기화 주기는 이번 조사에서도 확인되지 않음
    - oq-188·oq-190 은 조사하지 않음(11절 반영 대상으로만 둠)
    - 물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례는 확인하지 못함
- 범위 경계 위반 의심:
    - f13: 로봇 점유 격자 지도 갱신은 분류 원문 19장의 로봇 자체 지능·제어(SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 장면 그래프를 센서로 구축하는 부분은 로봇 인식(연계 대상)이며 계층형 표현 구조만 이 영역 근거로 쓰도록 제안함(f23 에서 구분)
    - f19: 공공 실내공간정보 구축은 공공 데이터 소유자의 일이므로 입력 데이터 가용성 근거로만 제안함
    - f23: SLAM·건물 데이터 구축·승강기 운행을 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 18회/30, 신규 출처 13건/15, 재사용 3건(ref-031·ref-079 는 github_raw 로 다시 열었고 ref-869 는 2026-09-30-03 브리프 재인용으로 이번에 열지 않음). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1014 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-03)가 ref-1015·ref-1017·ref-1019·ref-1024 를 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-046~ref-1037 을 순서대로 썼다. 원문 열람: 신규 13건 모두 열었다(webfetch 11건, github_raw 2건). 논문은 대부분 초록 페이지이고 Stefanini 외(ref-1037)만 PMC 본문을 열었다. 열지 못해 쓰지 않은 것: Nav2 문서(404·연결 거부), MiR Fleet 참조 안내서 PDF(본문 추출 실패), VDMA LIF 가이드라인 PDF(본문 추출 실패), LIF GitHub 저장소 페이지(403), MDPI·preprints.org(403), IEEE 1873 해설 논문(ECONNRESET). 교차 확인 0건, 신뢰도 high finding 없음(사실 finding 은 모두 단일 출처; IMDF 는 Apple 문서와 OGC 게시본이 같은 원천이라 독립 출처로 보지 않음). 분류 원문 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에는 f20 으로 답했고, 결론은 '장소 목록을 지도 요소에 묶고, 지도 버전 교체와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 변경을 나눠 관리한다'는 추정이다. 현장 유형 사례는 병원(f11, 재인용)·가정(f12)·기타(f18)이며, 물류창고 근거는 모의 실험(f13)뿐이라 site_type 을 null 로 두었다. 국내 자료는 국토지리정보원(ref-1035)·지디넷코리아(ref-956) 두 건이며 국내 로봇 지도 표준(KS)은 검색 2회에서 찾지 못했다. L. AI·학습 기술 관련(f14 장면 그래프, f16 LLM 추론)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 활성 지도 버전·폐쇄 구역으로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 IMDF·IndoorGML·LIF·구역 집합·차선 폐쇄·필터 마스크·위상 지도·반정적 객체·공간 그래프는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다.
```

### runs/2026-09-30-03/research.md

```markdown
# 리서치 브리프 2026-09-30-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-03 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 14. 도면·BIM에서 지도 만들기 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 기준점(fiducial), 공간 경계, 설계–준공 편차, 포즈 그래프 지도 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(도면 주석·로봇 지도 정합), 기타(대학 건물 BIM 기반 위치 추정) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 래스터 평면도 벡터화, CAD 기호 인식, BIM→점유 격자·위상 지도 변환, 축척 보정·좌표 변환 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IFC 4.3(IfcSpace·IfcTransportElement), Open-RMF 교통 편집기·플릿 어댑터 좌표 변환 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — CubiCasa5K, Raster-to-Vector, FloorPlanCAD, AI Hub 건축 도면 데이터, BIM 기반 위치 추정 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]
2. 평면도(이미지·CAD)에서 벽·문·공간·기호를 인식하는 대표 방법과 공개 데이터셋(국내 데이터 포함)은 무엇이며 보고된 성능은 어느 수준인가? (섹션 4·6·8 겨냥)
3. IFC 같은 BIM(Building Information Modeling)에서 공간·문·승강기를 가져와 로봇 지도(점유 격자·위상 지도)를 만드는 표준 요소·연구·도구는 무엇인가? (섹션 6·7·8 겨냥)
4. 도면 픽셀을 미터로 보정하고 제조사별 로봇 지도를 도면 좌표에 맞추는 절차는 오픈소스 관제(Open-RMF)와 제품에서 어떻게 이루어지며, 누가 확인하는가? (섹션 5·6·7 겨냥, oq-126 관련)
5. 도면·BIM 과 실제 현장이 다를 때(설계–준공 편차, 가구·배치 변경) 어떻게 확인하고 반영하는가? (섹션 3·6·11 겨냥, oq-193 관련)
6. 병원·건설 현장 등 실제 현장에서 도면 기반 지도를 쓴 사례는 무엇이며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥)
7. 도면·BIM 지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 위치 추정·BIM 저작·설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 교통 편집기(traffic-editor)는 건축 도면 같은 기존 평면도 이미지를 배경으로 불러와 그 위에 교통 기반 시설을 그리게 하며, 주석은 기준 평면도 이미지의 왼쪽 위를 원점으로 하는 픽셀 좌표로 만들어지고 평면도가 제조사별 로봇 지도의 기준 좌표계 역할을 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | Open-RMF 교통 편집기에서 도면 축척은 도면의 축척 막대처럼 실제 거리를 아는 두 점 사이에 측정선을 긋고 실제 길이를 미터로 입력해 층별 픽셀–미터 비율을 정하는 방식으로 설정한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f3 | [사실] | Open-RMF 교통 편집기는 여러 층을 맞출 때 기둥처럼 층 사이에 수직으로 같은 위치에 있을 것으로 기대되는 기준점(fiducial)을 층마다 찍고, 이를 대응시켜 층 사이의 이동·회전·축척 변환을 자동으로 계산한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f4 | [사실] | Open-RMF 교통 편집기에서 도면 위에 주석으로 표현하는 요소는 벽, 문(여닫이·미닫이 등 유형 지정), 여러 층에 걸친 승강기(층별 카 문 위치 포함), 이동 그래프를 이루는 차선(lane), 충전 위치(is_charger 속성의 지점)다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f5 | [사실] | Open-RMF 교통 편집기는 로봇이 만든 지도를 레이어로 불러와 축척·이동·회전 변환을 주어 기준 평면도와 겹치도록 맞추게 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 교통 편집기 좌표계가 다르면 두 좌표계에서 서로 대응하는 지점 쌍(reference_coordinates)을 설정 파일에 적게 하고 최소 4개 대응 지점을 권장하며, nudged 라이브러리로 회전·축척·이동 변환을 추정해 명령 좌표를 자동으로 바꾼다. | ref-153 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | Valner 외(Frontiers in Robotics and AI, 2022-08)에 따르면 에스토니아 타르투 대학병원 현장 시험에서는 PAL Robotics TIAGo 를 원격 조작해 SLAM 으로 격자 지도를 만들고, 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합해 두 좌표 표현 사이 변환을 정했으며, 이 지도로 중환자실에서 검사실까지 시간이 중요한 혈액 검체를 운반하고 RFID·근접 센서로 여는 반자동 문 두 곳을 통과했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 수행 자원 | — |
| f8 | [사실] | 같은 타르투 대학병원 시험의 저자들은 넓은 구역을 한 번에 매핑하면 누적 불확실성 때문에 지도가 비틀리기 쉬우므로 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확하다고 보고했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 예외·성과 | — |
| f9 | [사실] | IFC 4.3 문서에서 IfcSpace 는 건물 안에서 특정 기능을 제공하는 실제 또는 이론상 경계로 둘러싸인 면적·부피이며, IfcRelAggregates 로 층(building storey, 외부 공간은 site)에 속해 공간 계층을 이루고 IfcRelSpaceBoundary 로 물리적·가상 경계가 정의된다. | ref-156 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | IFC 4.3 문서에서 IfcTransportElement 는 시설 안에서 사람·동물·물품을 옮기는 운송 요소 전체를 일반화한 요소로, 승강기(lift)·에스컬레이터·무빙워크를 포함하며 PredefinedType 이나 IfcTransportElementType 으로 구분한다. | ref-213 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f11 | [사실] | Kalervo 외(2019)의 CubiCasa5K 는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 주석한 데이터셋이며, 저자들은 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 합성곱 신경망으로 평면도를 자동 해석하는 방법을 함께 제시했다. | ref-063 | 아니오 | medium | 2019-04 | — | — |
| f12 | [사실] | Liu·Wu·Kohli·Furukawa(ICCV 2017)의 Raster-to-Vector 는 신경망으로 벽 모서리·문 끝점 같은 접합점을 찾고 정수 계획법으로 이를 벽선·문선·아이콘 상자로 묶어 위상·기하가 일관된 벡터 평면도를 만들며, 저자 평가에서 정밀도·재현율 약 90%를 얻고 실제 서비스용 평면도 이미지 수십만 장을 벡터로 변환했다고 보고했다. | ref-1015 | 아니오 | medium | 2017 | — | — |
| f13 | [사실] | Fan 외(ICCV 2021)의 FloorPlanCAD 는 주거·상업 건물의 벡터 CAD 평면도 1만 장 이상을 30개 객체 범주로 선 단위 주석한 데이터셋으로, 셀 수 있는 사물 인스턴스와 셀 수 없는 영역의 의미를 함께 찾는 파놉틱 심볼 스포팅 과제와 CNN–GCN 결합 방법을 제시했다. | ref-067 | 아니오 | medium | 2021-05 | — | — |
| f14 | [사실] | AI Hub 의 '건축 도면 데이터'(2022년 구축, 주관기관 에이치씨아이플러스)는 평면도 41,556장을 포함한 건축 도면 48,033장으로 이루어지며, 출입문·창호·벽체 등 구조 8종, 거실·침실·주방·현관·화장실 등 공간 12종, 객체 5종 라벨과 문자 인식(OCR) 304,462건을 담은 인공지능 학습용 데이터다. | ref-1019 | 아니오 | medium | 2026-09-30 | — | — |
| f15 | [사실] | 연계 대상: Hendrikx 외(ICRA 2021)는 IFC 형식 BIM 의 의미 요소를 로봇용 세계 모델 표현으로 바꿔 공간 데이터베이스에 저장하고, 로봇 주변의 구조 요소를 질의해 특징 검출기를 설정한 뒤 그래프 기반 방법으로 위치를 추정해, 2D LiDAR 와 주행거리계만 가진 로봇이 BIM 이 있는 대형 대학 건물에서 자세를 추적할 수 있음을 보였다. | ref-1017 | 아니오 | medium | 2021 | 기타 | — |
| f16 | [사실] | Vega Torres·Braun·Borrmann(ECPPM 2022)은 복잡한 BIM 에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 방법을 제안했으며, BIM 과 현실의 차이(Scan-BIM 편차)가 가구·잡동사니뿐 아니라 설계 모델과 준공 상태의 차이에서도 생긴다고 지적하고, 제안 방법이 변화·동적 환경에서 일반 AMCL 보다 강건하게 위치를 추정했다고 보고했다. | ref-081 | 아니오 | medium | 2022-09 | 제약 | — |
| f17 | [사실] | 연계 대상: 같은 연구진의 BIM-SLAM(ISARC 2023, arXiv 2024-08)은 BIM 에서 포즈 그래프 지도·기술자 같은 세션 데이터를 먼저 만들고 다중 세션 앵커링으로 실제 LiDAR 측정과 맞추며, BIM 에 없는 요소를 찾아 묶고 표면으로 재구성해 설계 모델과 실제 실내 상태의 차이를 드러내고, 로봇의 초기 자세를 몰라도 BIM 에 정렬된 지도를 만든다. | ref-221 | 아니오 | medium | 2024-08 | 제약 | — |
| f18 | [사실] | Zhang·Wu·Ma·Schwertfeger(arXiv 2507.00552, 2025-07; 2026-03 개정)는 SLAM 매핑의 시간·노력·강건성 한계를 피하려고 건축 CAD 파일에서 구조 요소를 추출하고 AreaGraph 기반 위상 분할로 이동 가능한 공간을 나누며 CAD 의 문자 라벨을 넣고 여러 층을 합쳐 로봇 항법용 계층형 위상·거리 OpenStreetMap 실내 지도를 자동 생성하는 파이프라인과 GUI 를 공개했다. | ref-083 | 아니오 | medium | 2025-07 | — | — |
| f19 | [추정] | 모빌리오(Mobilio Robotics)는 자사 산업용 순찰 로봇 관제 솔루션이 사용자가 기둥·모서리 같은 기준점 3개 이상을 지정하면 2D LiDAR 지도를 CAD·BIM 도면에 정합하고 회전각·크기를 미세 조정해 로봇 위치를 실제 도면 위에 보여 주며, 공장·플랜트를 대상으로 한다고 주장한다. | ref-817 | 아니오 | low | 2026-08-24 | — | 벤더 주장 |
| f20 | [사실] | 엔지니어링데일리 보도에 따르면 국토교통부의 건설산업 BIM 활성화 로드맵은 설계 단계부터 BIM 100% 도입을 핵심 목표로 삼고 측량·설계·시공·감리·유지관리까지 전 단계에 BIM 을 쓰게 하며, LH 공공주택부터 BIM 적용을 의무화해 단계적으로 넓히는 계획을 담았다. | ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에 대해, 평면도의 벽·문·공간·기호 인식과 BIM·CAD 에서 점유 격자·위상 지도를 만드는 일은 연구 수준에서 자동화가 진행됐지만(f12·f13·f16·f18), 축척 설정·로봇 지도와의 좌표 정합·설계–준공 편차 확인은 측정선·기준점 입력과 사람의 확인에 기대고 있어(f2·f3·f6·f7·f16), 현재 형태는 '자동 초안 + 사람 확인·보정'에 가깝다. | ref-1015, ref-067, ref-081, ref-083, ref-079, ref-153, ref-869 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 도면·BIM 지도가 중요한 까닭은, 넓은 공간을 로봇으로 매핑하면 지도가 비틀리기 쉽고 제조사마다 지도 좌표가 다른 반면 평면도는 여러 제조사 로봇 지도를 묶는 공통 기준 좌표와 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점을 주기 때문이다(f1·f4·f8·f10). | ref-079, ref-869, ref-213 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 14. 도면·BIM에서 지도 만들기에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고(f4·f9·f10), 층별 축척과 층 간 기준점을 설정하며(f2·f3), 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고(f5·f6), 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일이다(f16, oq-126 과 연결). | ref-079, ref-153, ref-156, ref-213, ref-081 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정 포함)은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속하므로, 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다. | ref-1017, ref-081, ref-221, ref-213, ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 좌표 정렬·다층 모델을 다루는 15. 지도·공간·위치 모델(f3·f5·f6), 지도 편집·버전을 다루는 16. 장소 의미·지도 관리(f1·f16), 대화로 맵을 만드는 8. 채팅으로 맵 작성(f2·f6), 도면 해석 AI 를 다루는 45. 문서·도면·장면 이해(f11~f14), 승강기·문 연동을 다루는 22. 설비·건물 시스템 연동(f4·f10), 충전 위치를 다루는 28. 공용 자원·충전·에너지 최적화(f4), 차선 그래프를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f4), 설치 때 매핑·정합을 하는 55. 현장 조사·설치·시운전(f7·f8), 현재 상태의 차이를 다루는 18. 실시간 세계 상태·데이터 일관성(f17), 병원 적용을 다루는 63. 병원·의료(f7)와 이어진다. | ref-079, ref-153, ref-081, ref-063, ref-1015, ref-067, ref-1019, ref-213, ref-869, ref-221 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-156 | buildingSMART International | IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md | 아니오 |
| ref-213 | buildingSMART International | IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-1015 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017) | Raster-to-Vector: Revisiting Floorplan Transformation | 2017 | 논문 | medium | 2026-09-30 | https://art-programmer.github.io/floorplan-transformation.html | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-1017 | Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021) | Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization | 2021 | 논문 | medium | 2026-09-30 | https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/ | 아니오 |
| ref-081 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022) | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2022-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2308.05443 | 아니오 |
| ref-1019 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-817 | 모빌리오(Mobilio Robotics) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션) | 2026-08-24 | 벤더 문서 | low | 2026-09-30 | https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98 | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv) | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.00552 | 아니오 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023) | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 2024-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2408.15870 | 아니오 |
| ref-1024 | 엔지니어링데일리 | "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 … (제목 일부만 확인) | 미확인 | 기사 | low | 2026-09-30 | https://www.engdaily.com/news/articleView.html?idxno=12613 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(공통 기준 좌표·공용 자원 목록의 출발점), f8(넓은 구역 매핑의 누적 오차), f20(국내 BIM 전 단계 적용 정책, 기사 기준 신뢰도 low) / 섹션 4: 기준점(fiducial) f3, 공간·공간 경계 f9, 운송 요소 f10, 설계–준공 편차 f16, 포즈 그래프 지도 f16 / 섹션 5: 병원 — f7(타르투 대학병원 평면도 주석·격자 지도 정합·검체 운반), f8(예외·성과); 기타 — f15(대학 건물 BIM 기반 위치 추정, 연계 대상 표시). 여섯 항목 가운데 시작 조건·완료·인계 근거는 부족함을 명시 / 섹션 6: 래스터 평면도 벡터화 f12, CAD 기호 인식 f13, 평면도 해석 데이터셋 f11·f14, BIM→점유 격자·포즈 그래프 f16, CAD→위상 OSM f18, 축척 보정 f2, 층 정렬 f3, 로봇 지도 정합 f5·f6, 편차 검출 f17, 제품 사례 f19(벤더 주장 병기 필수), 자동화 수준 종합 f21 / 섹션 7: IFC 4.3 f9·f10, Open-RMF 교통 편집기 f1~f5, 플릿 어댑터 좌표 변환 f6 / 섹션 8: f11~f18, f7 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 8, 15, 16, 18, 22, 27, 28, 45, 55, 63 / 섹션 11: 기존 oq-126·oq-193 과 open_questions_new 4건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 f6(대응점 기반 좌표 변환) 반영, 45. 문서·도면·장면 이해 페이지에 f11~f14 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 층 정렬 기준점 | Fiducial (Level Alignment Fiducial) | 기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다. |
| 공간 경계 | Space Boundary (IfcRelSpaceBoundary) | IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다. |
| 설계–준공 편차 | As-planned vs As-built Deviation | 설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다. |

## 열린 질문

새로 생긴 질문:

- Raster-to-Vector 의 약 90% 정밀도·재현율처럼 보고된 평면도 인식 성능은 주로 주거용 도면 기준인데, 병원·공장·물류창고 같은 비주거 시설 도면에서 벽·문·승강기·충전 위치 인식 정확도를 보고한 자료가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f12 | 종류: 일반
- AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 승강기·계단·충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f14 | 종류: 일반
- 도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 제품 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 55. 현장 조사·설치·시운전 | 근거: f6 | 종류: 일반
- 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 22. 설비·건물 시스템 연동 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f20 국토교통부 원문 보도자료(molit.go.kr)는 ECONNRESET 으로 열지 못해 기사 기준이며, 공공공사 금액별 BIM 의무화 연도(검색 요약에만 나옴)는 넣지 않음
    - ref-1024 기사 발행일과 제목 전체 미확인
    - ref-817 모빌리오 글의 제목 전체 미확인, 정합 기능·성능은 벤더 주장이며 독립 확인 없음
    - ref-1019 AI Hub 데이터 공개일 미확인(구축 연도 2022 만 확인)
    - f11~f13·f15~f18 은 논문 초록·프로젝트 페이지 기준이며 본문의 실험 조건 미확인(Raster-to-Vector CVF 본문 403)
    - f12 의 약 90% 수치는 저자 평가이며 교차 확인 실패
    - f9·f10 은 IFC 4.3 개발 브랜치 문서 기준으로 게시판(ADD2)과의 문구 일치 미확인
    - 도면 인식 결과를 로봇 지도로 확정하는 승인 주체·시점(oq-126)은 어느 자료에서도 확인되지 않음
    - 건설 현장 지도–BIM 동기화 주기와 국내 사례(oq-193)는 이번 조사에서 확인되지 않음
    - 병원 외 현장 유형(물류창고·제조 공장·상업 시설)의 도면 기반 지도 사례는 벤더 주장(f19) 외에 확인되지 않음
- 범위 경계 위반 의심:
    - f15·f17: BIM 을 사전 지도로 쓰는 로봇 위치 추정·SLAM 은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f16: BIM→점유 격자 지도 생성은 직접 범위 후보이나 AMCL 비교 등 위치 추정 성능 부분은 로봇 자체 지능·제어 쪽 근거로만 쓰도록 제안함
    - f24: 승강기 제어(시설·설비 제어), BIM 저작·갱신(건물 측 체계)을 '연계 대상: '으로 표시함
    - f20: BIM 정책은 이 영역의 입력 데이터 가용성 근거로만 쓰고 ROP 직접 범위로 서술하지 않음
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: finding f7 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음): 직전 반환값(runs/2026-09-30-03/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. finding·출처 번호는 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-817)만 근거로 한 finding 은 f19 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 이번 f7 은 동료심사 논문(ref-869, Frontiers)에 근거한 병원 사례이며 벤더 문서를 근거로 하지 않는다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f7, f19). web_fetch_available: true · fetch_mode full. 사용량은 검색 13회/30, 신규 출처 15건/15(ref-079~ref-1024, 예약 구간 안)로 출처 상한에 도달했다. 그래서 BIM2RDT(건설 현장 BIM–로봇 디지털 트윈, arXiv 2509.20705, 열었음), 평면도 사전지식 기반 장기 위치 추정(arXiv 2303.10959), IFC→ROS 지도 도구 BIRS, Nav2 지도 YAML 형식(해상도·원점; 문서 URL 404)은 넣지 못했다. 원문 열람: 15건 모두 열었다(github_raw 4건, webfetch 11건). 논문은 대부분 초록 페이지다. 열지 못해 쓰지 않은 것: 국토교통부 보도자료·ancnews(ECONNRESET), 한국경제(403), Springer 'Improving autonomous robotic navigation using IFC files'(인증 리디렉션), CVF 논문 페이지(403). 교차 확인 0건, 신뢰도 high finding 없음(모든 사실 finding 이 단일 출처). 분류 원문 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에는 f21 로 답했고 결론은 '인식·변환은 연구 수준에서 자동화됐으나 축척·정합·편차 확인은 사람 입력·확인에 기대는 자동 초안 + 사람 확인 형태'라는 추정이다. 현장 유형 사례는 병원(f7·f8)과 기타(f15, 대학 건물)이며, 물류창고·제조 공장·상업 시설 사례는 벤더 주장(f19, 현장 유형 미특정) 외에 찾지 못했다. 국내 자료는 AI Hub(ref-1019)·엔지니어링데일리(ref-1024)·모빌리오(ref-817) 세 건이다. L. AI·학습 기술 관련(평면도 인식 f11~f14)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 상태와 BIM 차이(f17)로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 평면도 인식·래스터–벡터 변환·파놉틱 심볼 스포팅·스캔 대 BIM 비교·지도 정합·유사 변환·IFC·점유 격자 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 은 관련 근거(f6·f7, f16·f17)가 늘었으나 해결되지 않았다.
```
