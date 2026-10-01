(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-16
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 53. 개인정보·영상 데이터 (N. 보안·개인정보)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1135
- 새 출처 id 구간: ref-1135 ~ ref-1164 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1135 부터 순서대로 쓰고 ref-1164 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-16/target.json

```json
{
  "run_id": "2026-09-30-16",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 125,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 53,
    "area_name": "53. 개인정보·영상 데이터",
    "category": "N. 보안·개인정보",
    "category_letter": "N"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=53"
}
```

### docs/categories/security-and-privacy/privacy-and-video-data.md

```markdown
---
title: "53. 개인정보·영상 데이터"
type: area
category: "N. 보안·개인정보"
area_no: 53
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [N. 보안·개인정보](index.md) › 53. 개인정보·영상 데이터

# 53. 개인정보·영상 데이터

!!! info "소속 대분류"
    [N. 보안·개인정보](index.md) — 핵심 질문:
    누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]

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

### docs/categories/security-and-privacy/authentication-authorization-and-isolation.md (요약)

```markdown
# 51. 인증·권한·격리

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장비·사용자 인증**: 로봇·설비·사용자를 인증한다
- **명령 권한 관리**: 누가 어느 로봇에 어떤 명령까지 내릴 수 있는지 정하고 강제한다
- **원격 접속·유지보수 계정**: 외부 유지보수 계정이 접속할 수 있는 범위와 기록을 관리한다
- **고객·현장 격리**: 고객·현장·방문자별로 데이터와 제어를 분리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 26번 영역 ‘사이버보안·접근권한·개인정보’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [옛 분류원문]

> 옛 질문: 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [옛 분류원문]

## 2. 핵심 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
```

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md (요약)

```markdown
# 52. 통신 보호·위협 관리·감사

소속 대분류: N. 보안·개인정보 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **통신 보호**: 로봇·플랫폼·설비 사이 통신을 암호화하고 무결성을 지킨다(ROS 2 보안 등)
- **보안 위협 모델·취약점 관리**: 위협 모델을 세우고 취약점을 찾아 고친다(ROS 2 위협 모델, IEC 62443 등)
- **문서·대화 입력 보안**: 문서나 대화에 숨은 지시를 명령으로 실행하지 않게 막는다(프롬프트 주입 방지)
- **명령·승인 감사 기록**: 누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1103건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 306개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
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
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
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
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
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
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
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
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
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
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [53] 에 걸린 7건 / 전체 240건)

```markdown
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-171 [열림] 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? (영역 63, 53)
- oq-181 [열림] 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? (영역 65, 53)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-228 [열림] 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? (영역 45, 53)
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

### runs/2026-09-30-15/research.md

```markdown
# 리서치 브리프 2026-09-30-15

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-15 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 50. 안전 표준·인증·사고 조사 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 조화 표준·적합성 추정, 협동 적용, 로봇 분류(ISO 10218:2025), 윤리적 블랙박스, 잠금·표지(LOTO), 중상 보고(SIR) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 제조 공장·물류창고 사고 사례, 실외 법정 인증, 가정 모의 사고 조사 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 표준 적합성 경로(제조사·통합자·사용자), 사고 기록 장치, 증언·기록 결합 조사 절차 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218-1/-2:2025, ISO/FDIS 13482, ANSI/A3 R15.08, 실외이동로봇 운행안전인증 고시, KS B 7317 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-170, oq-186, oq-230 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
2. 산업용·이동·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482, ANSI/A3 R15.08)은 최근 어떻게 개정되었고 제조사·통합자·사용자에게 무엇을 요구하는가? (섹션 4·7 겨냥, oq-170)
3. 한국에서 로봇에 적용되는 법정 인증·KS 표준(실외이동로봇 운행안전인증, 협동로봇 관련 기준, 이동로봇 승강기 탑승 KS)은 무엇이며 심사 항목은 무엇인가? (섹션 5·7 겨냥, oq-186, oq-230, 한국 자료 우선)
4. 로봇 사고·아차 사고를 기록하고 원인을 조사하는 방법(사고 기록 장치, 조사 절차)에 관한 연구는 무엇을 제안하는가? (섹션 6·8 겨냥)
5. 실제 로봇 사고 통계와 사례는 어떤 작업·상황에서 사고가 나는지, 조사 자료에 어떤 한계가 있는지 보여 주는가? (섹션 3·5 겨냥, 제조 공장·물류창고·가정·실외·기타)
6. 안전 표준·인증·사고 조사에서 ROP가 직접 맡을 것과 제조사·통합자·인증기관·조사 기관에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 10218-1:2025(산업용 로봇 설계·제조, 제조사 대상)와 ISO 10218-2:2025(로봇 적용·로봇 셀 설계·통합, 통합자 대상)는 2025년 2월 발행된 2011년판 이후 첫 개정으로, 별도 기술 사양이던 ISO/TS 15066 의 협동 적용 요구와 수동 적재·하역 및 말단 장치 관련 기술 보고서 내용을 본문에 합치고, 기능 안전 요구를 명시화하며, 새 로봇 분류와 사이버보안 요구를 더했다. | ref-1225, ref-1226 | 예 | medium | 2025-02 | — | — |
| f2 | [사실] | EN ISO 10218-1/-2:2025 의 참조가 2026-09-07 EU 관보에 (EU) 2026/2015 시행 결정으로 게재되어 기계류 지침 2006/42/EC 의 필수 안전보건 요구에 대한 적합성 추정을 주게 되었고, 개정판은 안전 관련 제어 기능에 일률적으로 요구하던 PL d·범주 3 대신 표의 기본 성능 수준 적용 또는 위험성평가 근거 선택을 허용하며, 교대 종료 같은 운전 정지용 정상 정지 기능을 새로 요구한다. | ref-1226 | 아니오 | medium | 2026-09-18 | — | — |
| f3 | [사실] | 서비스 로봇 안전 표준 ISO 13482 는 개정판 ISO/FDIS 13482 가 2026-09-15 기준 단계 50.20(FDIS 투표 개시)에 있어 ISO 13482:2014 를 대체할 예정이며, 개인·전문(상업) 용도 서비스 로봇의 물리적 접촉 위험과 기능 안전을 다루고 산업용·의료용 로봇은 적용 범위에서 제외한다. | ref-1227 | 아니오 | medium | 2026-09-15 | — | — |
| f4 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동로봇 시스템을 특정 적용·현장에 배치할 때 위험성평가는 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 주며, 교육과 안전 작업 절차는 사용자 책임이고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다. | ref-1199 | 아니오 | medium | 2023-10-26 | 수행 자원 | 원문 미열람 |
| f5 | [사실] | 연계 대상: 한국로봇산업진흥원이 맡는 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2 에 근거한 인증으로, 최대 질량 500kg·최고 속도 15km/h 이하 로봇을 대상으로 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 심사항목을 두고 인증 처리기간을 신청일로부터 30일 이내로 안내한다. | ref-1228 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f6 | [사실] | 연계 대상: 실외이동로봇 운행안전인증의 절차와 기준은 산업통상자원부 고시 제2023-211호 '실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시'(2023-11-17)로 정해졌고, 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 제정되었으며 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다룬다. | ref-1230 | 아니오 | medium | 2023-11-17 | 실외 / 제약 | — |
| f7 | [사실] | 연계 대상: 고시 행정예고 단계의 보도(ZDNet Korea 2023-07-28)는 운행안전 기준을 16가지로 전하며, 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm 이하(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정 주행, 비상정지, 장애물 회피, 알림음 55~73dB, 등화장치 표면 온도 60도 이하, 방수 IPX4 이상을 예로 들어, 진흥원 페이지의 8개 심사항목(f5)과 항목 수가 다르다. | ref-1229, ref-1208 | 아니오 | low | 2023-07-28 | 실외 / 제약 | — |
| f8 | [사실] | 국가기술표준원은 2021-11-11 행정안전부와 협력해 실내 배송 로봇처럼 층간 이동에 승강기를 타는 로봇을 위한 KS B 7317 '이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'을 제정했고, 이 표준은 속도 제어, 위험 상황의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지를 다룬다. | ref-1231 | 아니오 | medium | 2021-11-11 | 제약 | — |
| f9 | [의견] | Winfield 외(2020)는 산업용 로봇과 달리 사람 사이에서 움직이는 사회적 로봇의 사고는 항공·철도 사고 조사와 같은 엄격함으로 조사되어야 하며, 사고 조사 없는 사회적 로봇 개발은 항공 사고 조사 없는 항공만큼 무책임하다고 주장했다. | ref-1232 | 아니오 | medium | 2020-05 | — | — |
| f10 | [사실] | Winfield·van Maris·Salvini·Jirotka(2022)는 사회적 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고·아차 사고 조사를 돕는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스(EBB)의 공개 표준 초안을 항공기 비행기록장치를 본떠 제안했고, 이를 논의용 첫 초안으로 내놓았다. | ref-1233 | 아니오 | medium | 2022-05-13 | 예외·성과 | — |
| f11 | [사실] | 가정 사례(모의): Webb 외(2021)는 사고 조사를 목격자 증언, 윤리적 블랙박스 기록, 해당 환경·로봇 전문가 분석, 기술·조직 권고로 구성하고, 지원 주거 아파트에서 넘어진 거주자 곁의 보조 로봇이 오작동해 직원에게 알리지 못하고 인터넷에도 연결되지 않은 모의 사고를 역할극 증언 면담으로 조사해 방법을 시험했다. | ref-1234 | 아니오 | medium | 2021-06-29 | 가정 / 예외·성과 | — |
| f12 | [사실] | Sanders·Sener·Chen(Applied Ergonomics 121, 2024)은 미국 OSHA 중상 보고(SIR)에서 2015~2022년 로봇 관련 사고 77건을 찾아, 고정형 로봇 54건(부상 66건, 주로 손가락 절단과 머리·몸통 골절)과 이동로봇 23건(부상 27건, 주로 다리·발 골절)으로 나누었고, 보고서 서술이 더 구조화되고 상세해야 한다고 결론지었다. | ref-1235 | 아니오 | medium | 2024 | 예외·성과 | — |
| f13 | [사실] | 제조 공장 사례: 서울신문(2017-04-07)이 보도한 안전보건공단 산업안전보건연구원 조사에 따르면 2011~2015년 국내 산업용 로봇 재해자는 207명(사망 15명)이고, 그중 134명(64.7%)이 수리·점검·준비·설치 작업 중에, 90.7%가 방책 안에서 다쳤으며, 평균 근로손실일수는 707.5일로 제조업 평균 351.7일의 약 두 배였다. | ref-1236 | 아니오 | low | 2017-04-07 | 제조 공장 / 예외·성과 | — |
| f14 | [사실] | 물류창고 사례: 2023-11-07 경남 고성의 농산물유통센터에서 파프리카 상자를 선별해 팔레트로 옮기는(출하 단계) 산업용 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌고, 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다. | ref-1237 | 아니오 | low | 2023-11-08 | 물류창고 / 예외·성과 | — |
| f15 | [사실] | 제조 공장 사례: 2026-09-21 경남 고성의 식품 제조 공장에서 멈춘 제품 적재용 로봇을 점검하던 노동자가 끼여 2026-09-25 숨졌으며, 보도에 따르면 전원 차단·기동스위치 잠금·표지(LOTO)와 재가동 전 안전 확인 절차가 없었고, 고용노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을, 경찰은 임의 재가동·기계 오작동 여부를 조사 중이다. | ref-1238 | 아니오 | low | 2026-09-29 | 제조 공장 / 예외·성과 | — |
| f16 | [사실] | 기타(건설 현장) 사례: Belzile 외(2025)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토하고 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준은 없으며 이동 플랫폼의 위험성평가 문헌도 제한적이라고 보고, 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다. | ref-1239 | 아니오 | medium | 2025-02-28 | 기타 / 제약 | — |
| f17 | [추정] | 확인한 자료를 종합하면 핵심 질문(어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가)에 대해, 따를 표준·인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년 개정 중이며, 사고 원인 규명은 비행기록장치식 기록과 증언을 결합하는 방법이 연구 단계로 제안되었지만 현행 보고 자료는 서술이 구조화되지 않아 원인 분석에 한계가 있는 것으로 보인다. | ref-1225, ref-1226, ref-1227, ref-1199, ref-1228, ref-1231, ref-1233, ref-1234, ref-1235 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 확인한 사고 자료(f12~f15)는 로봇 관련 중대 사고가 정상 운전보다 점검·수리·프로그램 수정·재가동 같은 비정상 작업 중에, 방책 안에서, 재가동 확인 절차가 없을 때 주로 일어났음을 보여 주므로, 여러 로봇을 지휘하는 플랫폼에서는 정비·점검 상태와 재가동 명령의 권한·확인 이력을 남기는 것이 예방과 사후 조사 모두에 필요할 것으로 보인다. | ref-1236, ref-1237, ref-1238, ref-1235 | 아니오 | low | 2026-09-30 | 예외·성과 | — |
| f19 | [추정] | 확인한 자료를 종합하면 50. 안전 표준·인증·사고 조사에서 ROP가 직접 맡을 범위는 로봇·적용마다 인증 상태, 적용 표준과 판, 인증이 허용한 운행 조건(질량·속도·구역)을 등록 정보로 관리해 배정·경로 제약에 반영하는 일, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존하는 플릿 수준 실행 기록, 표준 판 개정을 추적하는 일로 보인다. | ref-1228, ref-1226, ref-1233, ref-1235 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가, 교육·작업 절차·잠금·표지는 사용자 사업장이, 실외 운행 인증과 보험은 운영자와 진흥원이, 법정 사고 조사는 고용노동부·경찰이 맡으므로, ROP는 그 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다. | ref-1225, ref-1199, ref-1228, ref-1208, ref-1238 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f21 | [추정] | 이 영역은 위험성평가·정지 절차의 48. 안전·위험 관리(f4·f15), 협동 적용·분리 거리의 49. 사람 근접 안전(f1), 인증 속성을 등록하는 4. 이기종 로봇 등록(f5), 승강기 탑승 기준의 22. 설비·건물 시스템 연동(f8), 사고 조사용 기록의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석(f10~f12), 재가동 권한의 51. 인증·권한·격리(f15), 사이버보안 요구의 52. 통신 보호·위협 관리·감사(f1), 시험·인증 절차의 54. 시험·형식 검증·벤치마크, 현장 위험성평가의 55. 현장 조사·설치·시운전(f16), 표준 판 추적의 57. 자산·소프트웨어 수명주기 관리(f2·f3), 책임 분담의 58. 다사업자 책임·계약·데이터(f4), 법정 인증·보험·조사의 59. 법·규제·보험·라이선스(f5~f7·f15), 적용 현장인 61. 물류창고(f14)·62. 제조 공장(f13·f15)·65. 가정·공동주택(f11)·66. 실외(f5~f7)·67. 기타 현장(f16)과 이어진다. | ref-1199, ref-1238, ref-1225, ref-1228, ref-1231, ref-1233, ref-1234, ref-1235, ref-1239, ref-1226, ref-1227, ref-1230, ref-1229, ref-1237, ref-1236 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1225 | The Robot Report | ISO 10218 industrial robot safety standard receives major overhaul | 2025-02 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ | 아니오 |
| ref-1226 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-09-30 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 아니오 |
| ref-1227 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | 표준 | medium | 2026-09-30 | https://iss.rs/en/project/show/iso:proj:83498 | 아니오 |
| ref-1228 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-1229 | ZDNet Korea | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사 | 2023-07-28 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1230 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | high | 2026-09-30 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 아니오 |
| ref-1231 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-30 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 아니오 |
| ref-1232 | Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv) | Robot Accident Investigation: a case study in Responsible Robotics | 2020-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2005.07474 | 아니오 |
| ref-1233 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2205.06564 | 아니오 |
| ref-1234 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 아니오 |
| ref-1235 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-09-30 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 아니오 |
| ref-1236 | 서울신문 | [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인) | 2017-04-07 | 기사 | low | 2026-09-30 | https://www.seoul.co.kr/news/society/2017/04/07/20170407011011 | 아니오 |
| ref-1237 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | 기사 | low | 2026-09-30 | https://www.khan.co.kr/article/202311081103001 | 아니오 |
| ref-1238 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | 기사 | low | 2026-09-30 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 아니오 |
| ref-1239 | Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv) | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02-28 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2502.20693 | 아니오 |
| ref-1199 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 예 |
| ref-1208 | 산업통상자원부·경찰청 (대한민국 정책브리핑) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인) | 2023-11-16 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/safety-standards-certification-and-incident-investigation.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f13·f12(사고가 점검·재가동 중, 방책 안에서 나고 손실이 큼), f17(핵심 질문 답, 추정) / 섹션 4: ISO 10218:2025 제조사·통합자 구분과 로봇 분류 f1, 조화 표준·적합성 추정 f2, 윤리적 블랙박스 f10, 잠금·표지(LOTO) f15, 중상 보고 f12 / 섹션 5: 제조 공장 — f13(예외·성과: 재해 통계)·f15(예외·성과: 적재 로봇 점검 중 사고, 조사 중임 명시), 물류창고 — f14(출하 단계 선별·팔레트 적재 로봇 사고), 실외 — f5·f6·f7(제약: 운행안전인증, 항목 수 출처 충돌 병기), 가정 — f11(모의 사고 조사임 명시), 기타 — f16(건설 현장). 병원·상업 시설 사례는 찾지 못함을 명시 / 섹션 6: 역할별 적합성 경로 f1·f4, 기록 장치와 증언 결합 조사 f10·f11, 비정상 작업 관리 f18(추정) / 섹션 7: ISO 10218-1/-2:2025 f1·f2, ISO/FDIS 13482 f3, ANSI/A3 R15.08-2 f4, 실외이동로봇 운행안전인증·고시 제2023-211호 f5~f7, KS B 7317 f8, EBB 초안 f10 / 섹션 8: f9~f12·f16 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 4, 22, 37, 38, 48, 49, 51, 52, 54, 55, 57, 58, 59, 61, 62, 65, 66, 67 / 섹션 11: 기존 oq-170·oq-186·oq-230(미해결 유지, f5~f7 로 부분 근거)과 open_questions_new 4건. 다음 실행 후보: 66. 실외 페이지에 f5~f7, 22. 설비·건물 시스템 연동 페이지에 f8 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 윤리적 블랙박스 | Ethical Black Box (EBB) | 로봇의 센서·구동기·제어 결정 데이터를 안전하게 계속 기록해 사고나 아차 사고 뒤 원인 조사에 쓰도록 항공기 비행기록장치를 본떠 제안된 장치 또는 소프트웨어 모듈이다. |
| 잠금·표지 | Lockout/Tagout (LOTO) | 점검·수리 전에 설비의 동력을 차단하고 기동 장치를 잠근 뒤 다른 사람이 가동하지 못하도록 표지를 다는 작업 안전 절차다. |
| 적합성 추정 | Presumption of Conformity | EU 관보에 참조가 게재된 조화 표준을 적용한 제품은 해당 법령(예: 기계류 지침)의 필수 안전보건 요구를 충족한 것으로 추정되는 효력이다. |

## 열린 질문

새로 생긴 질문:

- 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 62. 제조 공장 | 근거: f1 | 종류: 일반
- 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 근거: f10 | 종류: 일반
- 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 48. 안전·위험 관리 | 근거: f13 | 종류: 일반
- ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 64. 상업 시설, 63. 병원·의료 | 근거: f3 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - oq-170 미해결: ISO 3691-4:2023 원문·ISO 페이지·iTeh 카탈로그가 열리지 않거나 본문이 없어 운용 구역 요구를 표준 원문으로 확인하지 못함(검색 요약의 제3자 블로그 설명은 넣지 않음)
    - oq-186·oq-230 미해결: 진흥원 페이지는 8개 심사항목, 행정예고 보도와 정책브리핑은 16가지 항목으로 전하며, 8개가 16개를 묶은 상위 항목인지 개정인지 고시 별표 원문으로 확인하지 못함. 근거 고시는 제2023-211호로 확인(f6)
    - f5 인증 처리기간: 진흥원 페이지는 30일 이내, 검색 요약 한 곳은 60일로 달라 페이지 값만 기재
    - f10 EBB 초안의 데이터 항목·형식·보존 기간: arXiv PDF 본문 추출 실패로 초록 범위만 기재
    - f12 OSHA SIR 분석: 출판사 페이지 403, 기관 저장소의 초록만 확인
    - f13 산업안전보건연구원 보고서 원문 미확인(기사 재인용), 끼임·부딪힘 비율은 기사에 없어 넣지 않음
    - f15 2026-09 고성 사고는 조사 진행 중이며 원인 확정 아님
    - ISO 10218:2025 의 '협동 적용' 용어 전환과 ANSI/A3 R15.06-2025·R15.08-3-2026 발간은 검색 요약에만 있어 넣지 않음(A3·ANSI 블로그 403)
    - 산업안전보건기준에 관한 규칙 제223조 단서와 협동로봇 설치 작업장 안전인증 기관: 법제처 원문이 열리지 않았고 인증기관을 한국로봇사용자협회로 적은 자료와 한국로봇산업진흥원으로 적은 기사가 달라 넣지 않음
    - KS B 7317 2025-05-09 개정 여부는 검색 요약에만 있어 넣지 않음
    - EU 기계류 규정 2023/1230 전환과 ISO 10218:2025 의 관계는 조사하지 못함
    - 병원·상업 시설의 안전 인증·사고 조사 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f5·f6·f7: 실외 보도 운행 법정 인증은 원문 19장 '업종별 조건'(실외 차량 등)의 연계 대상이므로 claim 을 '연계 대상: '으로 시작함
    - f20: 로봇 본체 인증(제조사·인증기관), 적용 위험성평가(통합자), 법정 사고 조사(노동부·경찰)는 ROP 밖 주체의 일로 '연계 대상: '으로 구분함
    - f13~f15: 산업용 로봇 셀의 방호장치·LOTO 는 원문 19장 '시설·설비 제어'·설비 안전 제어에 가까우므로 사고 조사 근거로만 쓰고 ROP 직접 범위(f19)는 기록·권한 쪽으로 한정함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1225~ref-1239, 예약 구간 안)로 신규 출처 상한에 도달해 ZDNet 2023-11-30(운행안전인증 심사 시작), ZDNet 2025-05-14(KS B 7317 평가 통과 사례), 한국로봇사용자협회·기사(협동로봇 설치 작업장 안전인증), CAST 핸드북(연결 끊김)을 출처로 넣지 못했다. 재사용 2건(ref-1199, ref-1208): 참고문헌 전체 목록이 입력에 없어 값은 이전 브리프 2026-09-30-14 출처 표를 따랐고 이번에 다시 열지 않아 fetched: false 로 적었다. 원문 열람: 신규 15건 모두 WebFetch 로 열었으나 ref-1232·ref-1233·ref-1235 는 초록만 읽었다. ISO(10218·13482·3691-4), A3, ANSI 블로그, ScienceDirect 는 403 이었다. 교차 확인 1건(f1: The Robot Report·IBF 두 곳). 기사 근거 finding(f7·f13·f14·f15)은 low. 벤더 기능 주장 없음. 분류 원문 핵심 질문에는 f17 로 답했고 결론은 '따를 표준은 로봇 유형·현장·국가 조건에 따라 갈리고 주요 표준이 개정 중이며, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계이고 현행 보고 자료는 구조화가 부족하다'는 추정이다. 현장 유형 사례는 제조 공장(f13·f15)·물류창고(f14)·실외(f5~f7)·가정(f11, 모의)·기타(f16, 건설 현장)이며 병원·상업 시설은 찾지 못했다. 국내 자료는 진흥원·산업통상자원부 고시·국가기술표준원·정책브리핑(재사용)과 기사 4건이다. 기존 열린 질문 oq-170·oq-186·oq-230 은 원문 확인 실패로 해결 제안하지 않았다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음(f14 의 인식 오류는 사고 사례로만 다룸). 용어집에 이미 있는 위험성평가·STPA·근본 원인 분석·운용 구역·실외이동로봇 운행안전인증·협동 적용·동력·힘 제한·속도·분리 감시는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-14/research.md

```markdown
# 리서치 브리프 2026-09-30-14

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-14 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 2. 사용 사례·요구·책임 범위 |
| 대분류 | A. 기획·사업 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 사용 사례 템플릿, 이해관계자 요구사항 명세, 제조사·통합자·사용자 역할, 플릿 제어 수준, 로봇활용 표준공정모델 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설·제조 공장·물류창고·실외 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 사용자 공동 설계, 현장 직원 면담, 업종별 표준공정 목록, 수요처 주관 실증 구조 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IEC 62559, ISO/IEC/IEEE 29148, ANSI/A3 R15.08-2, VDA 5050 범위, Open-RMF 플릿 제어 수준, RoMi-H 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]
2. 로봇에게 맡길 일을 고르고 요구·수용 기준을 정의할 때 쓰는 방법과 표준(사용 사례 템플릿, 요구공학 표준, 사용자 공동 설계)은 무엇인가? (섹션 4·6·7 겨냥)
3. 현장 유형별로 실제 어떤 일이 로봇에게 맡겨지고 있으며, 어떤 요구·제약·완료 확인 방식이 드러났는가? (섹션 5 겨냥, 병원·상업 시설·제조 공장·물류창고·실외, 한국 사례 우선)
4. 로봇 관제 규격과 오케스트레이션 도구는 플랫폼·제조사 관제·로봇 사이의 책임을 어떻게 나누고, 무엇을 규격 범위 밖에 두는가? (섹션 7·9 겨냥)
5. 안전 표준과 법규는 제조사·통합자·사용자·운영자의 책임을 어떻게 정하는가? (섹션 9·10 겨냥)
6. 한국 정부 사업은 수요처의 사용 사례 발굴과 요구 정의를 어떤 구조로 지원하는가? (섹션 5·6 겨냥, 한국 자료 우선)
7. 어떤 종류의 전문 서비스 로봇 적용이 많이 도입되고 있으며, 도입 동기는 무엇인가? (섹션 3 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 국제로봇연맹(IFR)의 World Robotics 2025 서비스 로봇 발표에 따르면 2024년 전문 서비스 로봇 판매는 약 20만 대(전년 대비 9% 증가)이며, 적용 분류별로 운송·물류 102,900대(+14%)가 가장 많고 접객 4만2천여 대(-11%), 전문 청소 2만5천여 대(+34%), 농업 약 19,500대(-6%) 순이다. | ref-1198 | 아니오 | medium | 2025-10 | — | — |
| f2 | [사실] | 같은 IFR 발표는 인력 부족을 기업이 전문 서비스 로봇을 쓰는 주요 동기로 들고, 운송·물류 분류에서 서비스형 로봇(RaaS) 방식이 2024년 42% 늘었다고 밝혔다. | ref-1198 | 아니오 | medium | 2025-10 | — | — |
| f3 | [사실] | ISO/IEC/IEEE 29148:2018 은 시스템·소프트웨어의 수명주기 전체에 걸쳐 요구사항을 도출·분석·문서화·검증·관리하는 공정과 그 산출 정보 항목(이해관계자 요구사항 명세(StRS) 등)의 내용과 형식을 규정하는 요구공학 표준이다. | ref-1207 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f4 | [사실] | IEC 62559 사용 사례 방법론은 에너지 시스템 요구 도출용 IntelliGrid 방법론에 기반한 IEC PAS 62559:2008 에서 나왔으며, 2부(IEC 62559-2:2015)는 사용 사례·행위자 목록·요구사항 목록의 템플릿을, 3부(IEC 62559-3:2017)는 템플릿 내용을 다른 엔지니어링 시스템으로 옮기는 XML 직렬화 형식을 정의하고, 4부는 표준화와 기업 프로젝트용 모범 사례를 다룬다. | ref-1206 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [추정] | IEC 62559-2 의 사용 사례·행위자 목록·요구사항 목록 템플릿 구조는 분류 원문 21장의 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과)으로 ROP 사용 사례를 기술할 때 행위자(로봇·사람·설비)와 요구 목록을 분리해 관리하는 틀로 쓸 수 있을 것으로 보이나, 로봇 오케스트레이션에 적용한 사례는 확인하지 못했다. | ref-1206 | 아니오 | low | 2026-09-30 | — | — |
| f6 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동로봇(IMR) 시스템을 특정 적용에 맞게 바꾸고 특정 현장에 배치할 때의 안전 요구를 다루며, 위험성평가는 IMR 시스템 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 제공하며, 교육과 안전 작업 절차는 사용자 책임이고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다. | ref-1199 | 아니오 | medium | 2023-10-26 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 명세는 관제(fleet control)가 이동로봇에 대한 주문 배정, 경로 계산, 막힘 감지·해소, 교통 제어를 맡고 이동로봇은 경로·동작을 실행하며 상태를 계속 보고한다고 나누되, 교통 조율 전략·알고리즘, 안전 요구, 보안 대책, 시운전 같은 프로젝트 수행 절차, 운영자·통합자·제조사 사이의 운영 책임 배분은 명세 범위 밖에 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 는 제조사 플릿을 연동 수준에 따라 완전 제어(경로를 RMF 가 지정), 신호등(상태와 일시정지·재개만), 읽기 전용(상태 보고만, 공유 공간당 최대 1개 플릿), 인터페이스 없음(공유 공간·자원에서 교착 가능성)으로 나누어 플랫폼이 맡을 수 있는 조율 범위가 연동 수준에 따라 달라진다고 설명한다. | ref-004 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f9 | [추정] | 로봇 관제 규격이 운영 책임 배분을 범위 밖에 두고(f7) 오케스트레이션 도구의 조율 범위가 제조사 플릿의 연동 수준에 따라 달라지므로(f8), 플랫폼이 직접 책임질 범위는 규격이 정해 주지 않고 사용 사례·현장·제조사 연동 수준마다 도입 단계에서 정해야 하는 것으로 보인다. | ref-031, ref-004 | 아니오 | low | 2026-09-30 | — | — |
| f10 | [사실] | 병원 사례로, 독일 샤리테 베를린 의대병원의 RoMi 연구(Friese 외, JMIR Nursing 2026-04)는 간호 인력과 함께 적용 시나리오·능력 요구·평가 기준을 공동으로 정하고, 반휴머노이드 서비스 로봇에 병실 메시지 전달, 소형 물품 배달, 음료 배급의 비임상 업무를 맡겼다. | ref-1195 | 아니오 | medium | 2026-04-14 | 병원 / 작업 대상 | — |
| f11 | [사실] | 같은 연구는 간호사 30명의 기술 사용 목록(TUI) 응답에서 사용 의도가 지각된 유용성(rs=0.74), 접근성(rs=0.628), 사용성(rs=0.505)과 양의 상관을, 회의감(rs=-0.516)과 음의 상관을 보였고, 시스템 능력과 한계의 투명한 전달과 직접 체험 기회가 도입에 필요하다고 결론지었다. | ref-1195 | 아니오 | medium | 2026-04-14 | 병원 / 예외·성과 | — |
| f12 | [사실] | 병원 사례로, 에스토니아 타르투 대학병원 현장 시험(Valner 외, Frontiers in Robotics and AI 2022-08)은 병원 직원과의 협업으로 검체·장비 운반을 자동화 대상으로 정하고, 중환자실 직원이 로봇 터치스크린으로 시작한 혈액 검체 운반을 검사실 직원이 꺼내 터치스크린으로 확인하는 방식으로 완료를 확인했으며, 이기종 로봇 플릿은 RMF 로 조율했다. | ref-1200 | 아니오 | medium | 2022-08-23 | 병원 / 완료·인계 | — |
| f13 | [사실] | 같은 현장 시험에서는 RFID 카드나 근접 센서로 여는 반자동문, 좁은 복도와 많은 사람이 제약이었고, 직접 만든 문 열기 장치가 전원이 떨어져 사람이 개입했으며, 저자들은 혼잡 대기와 기존 설비의 안전한 연동을 미해결 과제로 남겼다. | ref-1200 | 아니오 | medium | 2022-08-23 | 병원 / 제약 | — |
| f14 | [사실] | 병원 사례로, 한림대성심병원의 서비스로봇 실증은 약제 배송, 검체 이송, 부서 간 물품 배송, 환자 안내 등을 로봇에게 맡기고 있다. | ref-1201, ref-1209 | 예 | medium | 2025-04-10 | 병원 / 작업 대상 | — |
| f15 | [사실] | 한림대성심병원의 로봇 운용 규모는 ZDNet 기사(2024-09-19)가 7종 73대·누적 35,492건(2022-08~2024-05)과 서비스로봇 전용 승강기 구축을, 비즈한국 기사(2025-04-10)가 11종 77대를 전해 기준 시점마다 다르게 보도되었다. | ref-1201, ref-1209 | 아니오 | low | 2025-04-10 | 병원 / 수행 자원 | — |
| f16 | [의견] | 비즈한국 기사에 인용된 한 의대 교수는 검체 이송처럼 시간에 민감한 업무에서는 기존 컨베이어와 사람 운반이 속도와 안전 면에서 로봇보다 낫다는 의견을 냈다. | ref-1209 | 아니오 | low | 2025-04-10 | 병원 / 예외·성과 | — |
| f17 | [사실] | 같은 기사는 한국보건산업진흥원 보고서를 인용해 병원의 로봇 도입 장애로 수동 출입문, 건물 구역마다 다른 승강기 시스템, 통로 경사를 들었다. | ref-1209 | 아니오 | low | 2025-04-10 | 병원 / 제약 | — |
| f18 | [사실] | 싱가포르는 공공 의료기관에서 시험·배치하는 모든 로봇 시스템이 표준화되고 인정된 플랫폼으로 상호운용되도록 요구하며, 창이종합병원 CHART 가 개발한 RoMi-H 는 기계·제어·중앙(플릿 관리·로봇 간·설비 연동)·통합(API) 네 도메인으로 구성되고 2019-10-31 ROSCon 에서 공개되었다. | ref-1205 | 아니오 | medium | 2026-09-30 | 병원 / 제약 | — |
| f19 | [사실] | 상업 시설 사례로, 신라스테이 서초·반얀트리 클럽 앤 스파 서울의 호텔 룸서비스 로봇 배송에서 로보티즈는 배송 로봇을 만들고, 카카오모빌리티는 QR 주문과 수요–공급 매칭, 이기종 로봇 통합 관제, 인프라·보안, 운영 컨설팅을 맡는 플랫폼을 제공하며, 호텔은 서비스를 운영한다고 보도되었다. | ref-1203 | 아니오 | low | 2026-03-16 | 상업 시설 / 수행 자원 | — |
| f20 | [추정] | 같은 기사에 따르면 카카오모빌리티는 플랫폼 도입 뒤 일평균 로봇 가동률이 도입 초기 대비 약 8배 오르고 배송 성공률 100%, 룸서비스 매출 약 3배 증가를 이뤘다고 주장한다. | ref-1203 | 아니오 | low | 2026-03-16 | 상업 시설 / 예외·성과 | 벤더 주장 |
| f21 | [사실] | 제조 공장 사례로, 산업통상자원부는 2020년 뿌리·섬유·식음료·자동차 업종의 60개 기업을 대상으로 로봇활용 표준공정모델 14종을 개발하고, 표준공정모델 개발·공정개선 컨설팅·실증 보급·재직자 교육·협동로봇 안전인증을 묶은 패키지로 지원한다고 발표했으며, 6개 연구기관이 지원단을 구성했다. | ref-1196 | 아니오 | medium | 2020-06-25 | 제조 공장 / 시작 조건 | — |
| f22 | [사실] | 로봇신문 기사(2025-09-15)에 따르면 한국생산기술연구원은 2019년부터 뿌리산업·바이오화학 등 업종의 제조로봇 표준공정모델 64종을 개발해 실증사업에 148건을 공급했고, 2025년 베트남으로 첫 해외 적용을 넓혔다. | ref-1197 | 아니오 | low | 2025-09-15 | 제조 공장 | — |
| f23 | [사실] | 한국로봇산업진흥원의 서비스로봇 실증사업은 로봇 도입이 필요한 수요처(민간·공공)가 주관기관, 로봇기업이 참여기관이 되는 컨소시엄으로 운영되고, 국비는 로봇 도입 비용의 50% 이내이며 민간 부담 50% 이상 중 수요기관이 25% 이상을 부담하고, 분야는 물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료·기타다. | ref-1202 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f24 | [사실] | 물류창고 사례로, 곽경민 외(로봇학회논문지 17(4), 2022-11)는 물류 서비스를 계약물류·택배·풀필먼트로 나누고 로봇 적용을 이송 자동화(AGV·AMR·ASRS), 핸들링(박스 디팔레타이징·팔레타이징, 낱개 피킹), 지원(트럭 하역, 착용형 기기)으로 분류하며, 물류 특성에 맞는 기술과 운영 방식을 골라야 한다고 보았다. | ref-1204 | 아니오 | medium | 2022-11 | 물류창고 / 작업 대상 | — |
| f25 | [사실] | 연계 대상: 실외 사례로, 2023-11-17 시행된 개정 지능형로봇법은 운행안전인증(질량 500kg 이하·속도 15km/h 이하 대상, 운행구역 준수·횡단보도 통행 등 16개 시험항목)을 받은 실외이동로봇의 배달·순찰을 허용하고, 보도에서 로봇을 운영하려는 자에게 보험 또는 공제 가입 의무를 부과한다. | ref-1208 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f26 | [추정] | 확인한 자료를 종합하면 핵심 질문(로봇에게 어떤 일을 맡기고 플랫폼은 어디까지 책임질 것인가)에 대해, 실제 로봇에 맡겨지는 일은 반복적인 비임상·실내 운반과 정보 전달이 중심이며(f1·f10·f12·f14), 시간 민감 업무는 기존 수단이 낫다는 의견도 있어(f16) 일 선정은 현장 사용자와 함께 기준을 정하는 방식이 쓰이고(f10·f12), 플랫폼의 책임 범위는 규격이 정해 주지 않고 제조사 연동 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해지는 것으로 보인다(f6~f9·f25). | ref-1198, ref-1195, ref-1200, ref-1201, ref-1209, ref-031, ref-004, ref-1199, ref-1208 | 아니오 | low | 2026-09-30 | — | — |
| f27 | [추정] | 확인한 자료를 종합하면 2. 사용 사례·요구·책임 범위에서 ROP가 직접 맡을 것은 오케스트레이션 대상 사용 사례의 목록과 요구 명세(행위자·시작 조건·완료 확인·수용 기준)의 틀(f3·f4·f10), 제조사 플릿마다 연동 수준과 플랫폼이 맡는 조율 범위의 명시(f7·f8), 조달 조건으로서 상호운용 요구의 제시(f18), 현장 사용자와 함께 정한 평가 기준의 관리(f10·f11)로 보인다. | ref-1207, ref-1206, ref-1195, ref-031, ref-004, ref-1205 | 아니오 | low | 2026-09-30 | — | — |
| f28 | [추정] | 연계 대상: 분류 원문 19장 기준으로 이동로봇 적용의 위험성평가와 사용 정보 제공(통합자·제조사, f6), 보도 운행 로봇의 보험 가입과 인증(운영자·로봇 제조사, f25), 제조 공정 자체의 개선 컨설팅(f21), 전용 승강기·출입문 같은 건물 설비 개조(f13·f14·f17)는 ROP 밖의 주체가 맡고, ROP는 그 결과를 작업·경로·권한 제약과 책임 분담표로 받아 반영하는 것으로 보인다. | ref-1199, ref-1208, ref-1196, ref-1200, ref-1201, ref-1209 | 아니오 | low | 2026-09-30 | — | — |
| f29 | [추정] | 이 영역은 시장 규모의 1. 기술·시장·업체 동향(f1), 도입 비용 분담과 과금의 3. 경제성·조달·사업 모델(f2·f20·f23), 완료·인계 단계를 표현하는 24. 작업·워크플로 모델링(f12), 제조사 관제 연동 수준의 20. 로봇·제조사 관제 연동(f7·f8), 조달 요구로서의 21. 상호운용 표준·적합성(f18), 문·승강기의 22. 설비·건물 시스템 연동(f13·f14·f17), 통합자 위험성평가의 48. 안전·위험 관리·50. 안전 표준·인증·사고 조사(f6), 운영자 보험·인증의 59. 법·규제·보험·라이선스(f25), 운영 책임 배분의 58. 다사업자 책임·계약·데이터(f7·f19), 사용자 수용성의 60. 노동·수용성·접근성(f11·f16), 현장 조사의 55. 현장 조사·설치·시운전(f13), 적용 현장인 61. 물류창고(f24)·62. 제조 공장(f21·f22)·63. 병원·의료(f10~f18)·64. 상업 시설(f19·f20)·66. 실외(f25)와 이어진다. | ref-1198, ref-1202, ref-1200, ref-031, ref-004, ref-1205, ref-1199, ref-1208, ref-1203, ref-1195, ref-1209, ref-1204, ref-1196, ref-1197, ref-1201 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1195 | Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing) | Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study | 2026-04-14 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/ | 아니오 |
| ref-1196 | 산업통상자원부 (KDI 경제정보센터 게재) | 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수 | 2020-06-25 | 정부·연구기관 | medium | 2026-09-30 | https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C | 아니오 |
| ref-1197 | 로봇신문 | “제조 로봇 표준공정 모델 적용 사업 국내를 넘어 ... (제목 일부만 확인) | 2025-09-15 | 기사 | low | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=42376 | 아니오 |
| ref-1198 | International Federation of Robotics (IFR) | Service Robots See Global Growth Boom | 2025-10 | 업계 보고서 | medium | 2026-09-30 | https://ifr.org/news/service-robots-see-global-growth-boom/ | 아니오 |
| ref-1199 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 아니오 |
| ref-1200 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/ | 아니오 |
| ref-1201 | ZDNet Korea | 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인) | 2024-09-19 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240919162124 | 아니오 |
| ref-1202 | 한국로봇산업진흥원 | 서비스로봇 실증사업 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do | 아니오 |
| ref-1203 | 아시아경제 | 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) | 2026-03-16 | 기사 | low | 2026-09-30 | https://view.asiae.co.kr/article/2026031610244491183 | 아니오 |
| ref-1204 | 곽경민, 박범, 고은지, 윤철주, 김경훈 (로봇학회논문지 17(4)) | 급속 확산되는 물류현장의 로봇적용 사례 | 2022-11 | 논문 | medium | 2026-09-30 | https://jkros.org/_PR/view/?aidx=34724&bidx=3204 | 아니오 |
| ref-1205 | Changi General Hospital, CHART | ROMI-H | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.cgh.com.sg/chart/projects/romi-h | 아니오 |
| ref-1206 | IEC SyC Smart Energy | IEC 62559 - use case methodology | 미확인 | 표준 | high | 2026-09-30 | https://syc-se.iec.ch/deliveries/iec-62559-use-cases/ | 아니오 |
| ref-1207 | ISO / IEC / IEEE | ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering | 2018 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/72089.html | 예 |
| ref-1208 | 산업통상자원부·경찰청 (대한민국 정책브리핑) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인) | 2023-11-16 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 아니오 |
| ref-1209 | 비즈한국 | 병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인) | 2025-04-10 | 기사 | low | 2026-09-30 | https://bizhankook.com/articles/29394.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-business/use-cases-requirements-and-scope.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1·f2(적용 분류별 도입 규모와 인력 부족 동기), f9(책임 범위를 규격이 정해 주지 않음), f26(핵심 질문 답, 추정) / 섹션 4: 사용 사례 템플릿 f4, 이해관계자 요구사항 명세 f3, 제조사·통합자·사용자 역할 f6, 플릿 연동 수준 f8, 로봇활용 표준공정모델 f21 / 섹션 5: 병원 — f10(작업 대상: 메시지·물품·음료)·f11(예외·성과: 수용성)·f12(완료·인계: 터치스크린 확인)·f13(제약: 반자동문·인파)·f14·f15(작업 대상·수행 자원)·f16(의견)·f17(제약)·f18(제약: 상호운용 조달 요구), 상업 시설 — f19(수행 자원: 역할 분담)·f20(벤더 주장 병기), 제조 공장 — f21·f22(표준공정모델), 물류창고 — f24(물류 유형·로봇 분류), 실외 — f25(연계 대상: 운행안전인증·운영자 보험). 가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 사용자 공동 설계 f10·f11, 현장 직원 협업 f12, 업종별 표준공정 목록 f21·f22, 수요처 주관 실증 f23, 사용 사례 템플릿 적용 f5(추정) / 섹션 7: IEC 62559 f4, ISO/IEC/IEEE 29148 f3(원문 미열람), ANSI/A3 R15.08-2 f6, VDA 5050 범위 f7, Open-RMF 연동 수준 f8, RoMi-H f18 / 섹션 8: f10~f13·f24 / 섹션 9: f27(직접 범위), f28(연계 대상), f7·f8 / 섹션 10: f29 — 1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66 / 섹션 11: open_questions_new 5건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10~f18, 58. 다사업자 책임·계약·데이터 페이지에 f6·f7·f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사용 사례 템플릿 | Use Case Template (IEC 62559-2) | IEC 62559-2 가 정한 사용 사례 기술 양식으로, 사용 사례의 목표·시나리오와 함께 행위자 목록과 요구사항 목록을 구조화해 기록하게 한다. |
| 이해관계자 요구사항 명세 | Stakeholder Requirements Specification (StRS) | ISO/IEC/IEEE 29148 이 정한 요구공학 산출물의 하나로, 사용자와 이해관계자가 시스템에 기대하는 것을 구현 방법 없이 수용 기준과 함께 적은 문서다. |
| 로봇활용 표준공정모델 | Robot Standard Process Model (Korea) | 업종별 제조 공정에 로봇을 적용하는 방법을 표준화한 국내 참조 모델로, 수요기업이 공정을 골라 로봇 도입·실증에 쓰도록 정부 지원 사업과 연계해 개발·보급된다. |

## 열린 질문

새로 생긴 질문:

- 로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 58. 다사업자 책임·계약·데이터 | 근거: f7 | 종류: 일반
- 병원 검체 이송처럼 시간에 민감한 업무에서 로봇·컨베이어·사람 운반을 같은 조건으로 비교해 로봇에게 맡길 업무를 정한 정량 연구가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 63. 병원·의료 | 근거: f16 | 종류: 일반
- IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 24. 작업·워크플로 모델링 | 근거: f5 | 종류: 일반
- 싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 21. 상호운용 표준·적합성 | 근거: f18 | 종류: 일반
- 가정·공동주택과 기타 현장(공공시설·연구실 등)에서 여러 로봇에게 맡길 일과 요구를 사용자와 함께 도출한 연구나 실증 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 65. 가정·공동주택, 67. 기타 현장 | 근거: f26 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f3 ISO/IEC/IEEE 29148:2018: ISO 페이지·OBP 403 으로 원문 미열람, 범위와 정보 항목은 검색 결과 요약 기준
    - f6 ANSI/A3 R15.08-2: 표준 원문과 ANSI 블로그 403, 전문지 기사 기준(ANSI 블로그 검색 요약과 내용 일치하나 출처 상한으로 넣지 않음)
    - f1·f2 IFR 수치: 공식 요약 PDF 는 추출 실패, IFR 뉴스 페이지 기준. 운송·물류 안에서 공공 교통 없는 실내 운송이 가장 중요한 분류라는 서술은 검색 요약에만 있어 넣지 않음
    - f15 한림대성심병원 규모는 보도 시점마다 달라(7종 73대 대 11종 77대) 최신값 미확인
    - f17 한국보건산업진흥원 보고서 원문 미확인(기사 재인용)
    - f20 카카오모빌리티 가동률·성공률·매출 수치는 회사 주장이며 측정 기간·방법 미확인
    - f22 제조로봇 표준공정모델 전체 누계: 다른 기사 검색 요약의 '2020년부터 109개 공정 + 34개' 수치는 열지 않아 넣지 않았고 한국생산기술연구원 기관 수치(64종)만 기재
    - IEC 62559-2 템플릿의 세부 필드 목록은 원문 미열람으로 미확인
    - García 외 서비스 로보틱스 소프트웨어 공학 연구(ESEC/FSE 2020)는 초록에 요구·임무 명세 관련 결과가 없어 넣지 않음
    - WER 2017 로봇 시스템 요구공학 체계적 매핑 연구와 DTU 병원 운반 업무 사례 연구는 PDF 추출 실패로 넣지 않음
    - 가정·기타 현장의 사용 사례·요구 도출 자료는 찾지 못함
- 범위 경계 위반 의심:
    - f6: 이동로봇 위험성평가·안전 절차 책임은 M. 안전 대분류(48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사)의 내용이므로 이 영역에서는 책임 배분 근거로만 쓰고 f28 에서 '연계 대상: '으로 구분함
    - f25: 실외 로봇 인증·보험은 원문 19장 '업종별 조건'(실외 차량 등) 연계 대상이므로 claim 을 '연계 대상: '으로 시작함
    - f13·f14·f17: 전용 승강기·출입문 개조는 원문 19장 '시설·설비 제어' 연계 대상이며 ROP 는 요청·상태 확인 인터페이스만 맡는 것으로 f28 에서 구분함
    - f21·f22: 제조 공정 자체의 개선 컨설팅은 ROP 범위 밖이며 사용 사례 발굴 방법의 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1195~ref-1209, 예약 구간 안)로 신규 출처 상한에 도달해 ANSI 블로그(R15.08-3-2026)·IFR 서비스 로봇 정의 문서·RoMi-H 등재 프로그램 페이지를 출처로 더하지 못했다. 재사용 2건(ref-004, ref-031): 참고문헌 목록 전체가 입력에 없어 ref-004 값은 researcher.md 예시, ref-031 값은 이전 브리프 2026-09-25-09 출처 표를 따랐고 이번에 GitHub 공식 저장소 원본을 다시 열었다. 원문 열람: 16건 열었고(webfetch 14, github_raw 2) ISO/IEC/IEEE 29148(ref-1207)만 403 으로 못 열어 source_unopened 로 표시했다. PDF 출처(IFR 요약, DTU, WER 2017, ARIA 보고서)는 본문 추출에 실패해 쓰지 않았다. 교차 확인 1건(f14, 한림대성심병원 업무 종류: ZDNet·비즈한국 두 기사). 기사 근거 finding(f15·f16·f17·f19·f20·f22)은 low 로 두었고, 카카오모빌리티 성과 수치(f20)는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가)에는 f26 으로 답했고 결론은 '맡기는 일은 반복적 비임상·실내 운반과 정보 전달이 중심이고 사용자와 함께 선정하며, 플랫폼 책임 범위는 규격이 정하지 않아 제조사 연동 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해진다'는 추정이다. 현장 유형 사례는 병원(f10~f18)·상업 시설(f19·f20)·제조 공장(f21·f22)·물류창고(f24)·실외(f25)이며 가정·기타는 찾지 못했다. 국내 자료는 산업통상자원부 2건(ref-1196, ref-1208)·한국로봇산업진흥원(ref-1202)·로봇학회논문지(ref-1204)·기사 4건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음. 용어집에 이미 있는 플릿 제어 수준·서비스형 로봇·공공 영역 이동로봇·등재 프로그램·실외이동로봇 운행안전인증·의료 로봇 미들웨어 RoMi-H·로봇 친화형 건축물 인증·로봇–작업 적합도 행렬은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```
