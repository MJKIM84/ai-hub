(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-02
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 10. 채팅으로 로봇 구성 (C. 채팅 기반 구성·운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-818
- 새 출처 id 구간: ref-818 ~ ref-847 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-818 부터 순서대로 쓰고 ref-847 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-02/target.json

```json
{
  "run_id": "2026-09-29-02",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 94,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 10,
    "area_name": "10. 채팅으로 로봇 구성",
    "category": "C. 채팅 기반 구성·운영",
    "category_letter": "C"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=10"
}
```

### docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md

```markdown
---
title: "10. 채팅으로 로봇 구성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 10
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 10. 채팅으로 로봇 구성

# 10. 채팅으로 로봇 구성

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]

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

### docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md (요약)

```markdown
# 8. 채팅으로 맵 작성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md (요약)

```markdown
# 12. 채팅으로 업무 지시·오케스트레이션

소속 대분류: C. 채팅 기반 구성·운영 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 817건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 207개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automation-bias: 자동화 편향 (Automation Bias)
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
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
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
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
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
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
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
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
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
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [10] 에 걸린 0건 / 전체 126건)

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

### runs/2026-09-29-01/research.md

```markdown
# 리서치 브리프 2026-09-29-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-01 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 8. 채팅으로 맵 작성 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 위상 지도·의미 지도·빌딩 맵·레이아웃 교환 형식·축척 보정·명확화 질문 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델과 짝 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]
2. 자연어 설명이나 경로 지시만으로 로봇용 위상·의미 지도를 만들거나 편집하는 연구는 무엇이 있고 어느 정도 정확한가? (섹션 6·8 겨냥)
3. 언어 모델로 평면도를 생성·편집·이해하는 연구는 기하·위상 제약을 얼마나 지키며 어떤 한계가 보고되는가? (섹션 3·6·8·11 겨냥)
4. 대화 결과를 담을 지도 형식(Open-RMF 빌딩 맵, VDMA LIF·VDA 5050 노드·에지, 도면 변환 결과)은 층·구역·통로·문·승강기·충전 위치를 어떤 요소로 표현하고 축척은 어떻게 정하는가? (섹션 4·7 겨냥)
5. 병원·제조 공장·실외 같은 현장 유형에서 층·승강기·문을 포함한 지도 작성·정합 사례는 무엇인가? (섹션 5 겨냥, 국내 자료 포함)
6. 말로 확정할 수 없는 값(축척·치수·통과 조건)을 확인 질문으로 받아 확정하는 방식의 근거가 되는 대화 연구는 무엇인가? (섹션 4·6 겨냥, 13. 대화형 기능의 신뢰·기반 연결)
7. 지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 SLAM·도면 해석 등 외부에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Deguchi 외(ICRA 2024)는 대규모 언어 모델로 자연어 경로 지시문을 노드·에지·행동으로 된 위상 지도로 바꾸는 방법을 제안했고, 기하 지도나 카메라 없이 언어만으로 지도를 만들며, 지도를 언어 모델 기억에 암묵적으로 두는 것보다 명시적 위상 지도를 만드는 쪽이 정확도가 뚜렷이 높았다고 보고했다. | ref-815 | 아니오 | medium | 2024-03-15 | — | — |
| f2 | [사실] | SENT-Map(2025)은 실내 환경을 의미 정보가 붙은 JSON 형식 위상 지도로 표현해 사람과 기반 모델이 같은 형식을 읽고 고칠 수 있게 하며, 시각 기반 모델과 운영자가 짝을 이뤄 지도를 만든 뒤 자연어 질의로 계획하는 2단계 방식으로 소형 로컬 모델도 실내 계획을 할 수 있음을 보였다. | ref-816 | 아니오 | medium | 2025-11-05 | — | — |
| f3 | [사실] | Walter 외(RSS 2013)는 사람이 말로 설명한 장소 이름과 공간 관계를 센서 관측과 함께 계량·위상·의미가 결합된 의미 그래프로 공동 추정하는 알고리즘을 제시했고, 자연어를 넣으면 센서만 쓸 때보다 지도 정확도가 올라간다고 보고했다. | ref-819 | 아니오 | medium | 2013-06 | — | — |
| f4 | [추정] | 위 세 연구를 보면 대화로 만드는 지도는 장소·연결·이름 같은 위상·의미 층을 담는 데 강점이 있고 정확한 기하(치수·좌표)는 센서·도면·사람 확인에서 와야 하므로, ROP의 채팅 맵 작성은 위상·의미 요소를 대화로 만들고 기하 정합은 별도 입력으로 받는 구조가 맞을 것으로 보인다. | ref-815, ref-816, ref-819 | 아니오 | low | 2026-09-29 | — | — |
| f5 | [사실] | Tell2Design(ACL 2023)은 자연어 지시와 짝지은 8만 건 이상의 평면도 설계 데이터셋으로 언어 유도 평면도 생성 과제를 제시했고, 예술적 이미지 생성과 달리 공간·관계 제약을 만족해야 하는 점을 핵심 난점으로 꼽았다. | ref-817 | 아니오 | medium | 2023 | — | — |
| f6 | [사실] | HouseMind(CVPR 2026)는 방 단위 이산 토큰으로 어휘를 만들어 멀티모달 언어 모델 하나가 평면도를 이해·생성하고 텍스트 지시로 편집하게 했으며, 기하 타당성과 제어 가능성이 기존 확산·언어 모델 방식보다 낫고 로컬 배포가 가능하다고 보고했다. | ref-823 | 아니오 | medium | 2026-03-12 | — | — |
| f7 | [사실] | Holodeck(CVPR 2024)은 한 문장 설명에서 GPT-4가 평면도·출입구·창·재질을 설계하고 객체 사이 공간 관계 제약을 생성해 최적화로 배치하는 방식으로 3D 실내 환경을 만들며, 사람 평가에서 주거 장면에 대해 절차적 생성 기준선보다 선호되었다. | ref-825 | 아니오 | medium | 2023-12-14 | — | — |
| f8 | [사실] | FloorplanQA(2025)는 JSON·XML 로 기술한 실내 평면도에 대해 거리 측정·가시성·경로 찾기·객체 배치 질문으로 최신 공개·상용 언어 모델을 평가했고, 모델들이 단순 질문은 처리하지만 물리 제약을 지키지 못하고 공간 일관성을 잃는 약점이 있다고 보고했다. | ref-822 | 아니오 | medium | 2025-07-10 | — | — |
| f9 | [추정] | 평면도 생성 데이터셋 연구와 평면도 공간 추론 벤치마크가 서로 독립적으로 언어 모델의 공간·물리 제약 준수를 핵심 난점으로 지목하므로, 채팅으로 만든 층·구역·통로·문 배치는 언어 모델 출력 그대로 쓰지 말고 기하 검증기나 사람 확인을 거쳐야 할 것으로 보인다. | ref-817, ref-822 | 예 | medium | 2026-09-29 | 제약 | — |
| f10 | [사실] | Open-RMF 의 Traffic Editor 는 2D 평면도 이미지 위에 층(레벨)·벽·꼭짓점(충전소·주차·도킹 속성 부여 가능)·플릿별 교통 차선·문 4종(여닫이·양여닫이·미닫이·양미닫이)·여러 층을 잇는 승강기·바닥 다각형을 그려 제조사 중립 빌딩 맵을 만들고 결과를 .building.yaml 로 저장한다. | ref-079 | 아니오 | medium | 2026-09-29 | 작업 대상 | — |
| f11 | [사실] | Traffic Editor 에서 층의 축척은 사용자가 실제 거리를 아는 두 점 사이에 측정선을 긋고 그 물리 거리를 미터로 입력해야 정해지므로, 평면도 이미지만으로는 축척이 확정되지 않고 사람이 값을 넣어야 한다. | ref-079 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f12 | [추정] | Traffic Editor 의 빌딩 맵이 층·차선·문·승강기·충전 위치를 담는 텍스트(YAML) 구조이고 축척은 사람이 준 거리로 정해지는 점을 보면, 채팅 맵 작성은 이런 텍스트 지도 구조를 대화로 채우되 축척·치수처럼 말로 확정할 수 없는 값은 확인 질문으로 받는 흐름이 자연스러울 것으로 보인다. | ref-079, ref-816 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f13 | [사실] | Open-RMF 공식 데모 저장소의 Clinic 월드는 두 층과 승강기 2대, 역할이 다른 로봇 플릿 2개를 두고 로봇이 승강기로 층을 오가는 시뮬레이션 빌딩 맵이며, Hotel 월드는 객실 층 2개·로비·승강기 2대·여러 문·플릿 3개를 둔다(실제 현장 배치가 아닌 시뮬레이션 데모). | ref-104 | 아니오 | medium | 2026-09-29 | 병원 / 제약 | — |
| f14 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합자가 노드·에지·스테이션으로 된 주행 레이아웃을 제3자 관제 시스템에 처음 넘겨 주기 위한 형식이며 VDA 5050 의 영향을 받아 정의되었다. | ref-046 | 아니오 | medium | 2023-09 | 완료·인계 | — |
| f15 | [추정] | LIF 의 노드·에지·스테이션과 Open-RMF 빌딩 맵의 꼭짓점·차선·문·승강기처럼 플릿 관제가 실제로 읽는 지도 형식이 이미 여럿이므로, 채팅 맵 작성의 결과물은 자유 서술이 아니라 이런 형식에 맞는 구조화 지도 요소여야 하고 형식마다 요소 대응(예: 충전 위치를 스테이션·꼭짓점 속성 어디에 둘지)이 필요할 것으로 보인다. | ref-046, ref-079 | 아니오 | low | 2026-09-29 | — | — |
| f16 | [사실] | Zhang 외(2025)는 건축 CAD 파일에서 구조 레이어 분리, AreaGraph 기반 위상 분할, 도면 글자와 방의 자동 연결, 다층 융합을 거쳐 로봇 내비게이션용 계층 위상·계량 OSM 지도를 자동 생성하는 GUI 포함 파이프라인을 제시하며, SLAM 기반 지도 작성은 시간·노동·강건성에서 한계가 있다고 주장했다. | ref-083 | 아니오 | medium | 2025-07-01 | — | — |
| f17 | [사실] | 김영재·김세윤·김홍준(2022)은 공공 지도 서비스 데이터로 자율주행 이동 로봇의 분기점 단위 전역 경로 계획용 위상 지도를 구축하는 방법을 제안하고 A* 모의실험으로 유효성을 검증해, 실외 로봇 서비스의 지도 구축 비용을 줄일 수 있다고 보고했다. | ref-820 | 아니오 | medium | 2022-06 | 실외 / 수행 자원 | — |
| f18 | [사실] | 연계 대상: 노주형 외(2026, 로봇학회 논문지)는 3D 라이다·IMU SLAM 과 프런티어 탐사, 매니퓰레이터로 승강기 버튼을 누르는 승강기 연동으로 로봇이 다층 실내 지도를 스스로 만드는 시스템을 제시해 KAIST N1 건물 5개 층을 27분에 지도화하고 승강기 상호작용 성공률 95%를 보고했으며, 이는 로봇 자체 지능·제어 쪽 지도 작성이다. | ref-163 | 아니오 | medium | 2026 | 기타 / 수행 자원 | — |
| f19 | [추정] | 국내 업체 모빌리오는 공장 순찰 로봇 관제 화면에서 2D 라이다 지도(PGM)와 CAD·BIM 도면을 기둥·모서리 같은 기준점 3개 이상으로 맞춰 좌표계를 일치시킨 뒤 회전각·크기를 미세 조정해 정합하는 '맵 정합' 기능을 제공한다고 밝히며, 도면 자체나 구역을 편집하는 기능은 설명하지 않는다. | ref-827 | 아니오 | low | 2026-08-24 | 제조 공장 / 완료·인계 | 벤더 주장 |
| f20 | [사실] | Doğan·Torre·Leite(HRI 2022)는 요청에서 가리킨 물체가 모호할 때 로봇이 아는 환경 정보로 후속 명확화 질문을 하는 시스템을 63명 사용자 연구로 평가해, 명확화 질문을 받은 사람들이 과제를 더 쉽게 느끼고 로봇의 과제 이해·역량을 더 높게 평가했다고 보고했다. | ref-826 | 아니오 | medium | 2022-03 | — | 원문 미열람 |
| f21 | [추정] | 명확화 질문이 사용자 인식을 개선한다는 연구와 축척이 사람의 거리 입력으로만 정해지는 편집기 관행을 함께 보면, 채팅 맵 작성은 축척·치수·통과 조건처럼 말로 확정할 수 없는 값을 모델이 추정해 채우지 않고 선택지가 붙은 확인 질문으로 받는 쪽이 맞을 것으로 보인다. | ref-826, ref-079 | 아니오 | low | 2026-09-29 | 제약 | — |
| f22 | [추정] | 연계 대상: 라이다 SLAM 으로 점유 격자를 만들고 위치를 추정하는 일(노주형 외, 모빌리오의 PGM 지도)과 도면을 벡터·위상 구조로 해석하는 일(Zhang 외)은 각각 분류 원문 19장의 로봇 자체 지능·제어와 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해의 몫이며, 8. 채팅으로 맵 작성은 그 결과를 입력으로 받는 쪽이다. | ref-163, ref-827, ref-083 | 아니오 | low | 2026-09-29 | — | — |
| f23 | [추정] | 8. 채팅으로 맵 작성에서 ROP가 직접 맡을 범위는 대화에서 층·구역·통로·문·승강기·충전 위치 같은 구조화 지도 요소를 만들어 플릿 중립 형식(빌딩 맵·LIF 류)에 담고, 확정할 수 없는 값을 확인 질문으로 받아 사람이 화면에서 확인·승인한 지도만 확정하는 일이며, 기하 지도 생성과 도면 해석 엔진은 연계 대상으로 두는 것이 맞을 것으로 보인다. | ref-079, ref-046, ref-816, ref-822 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f24 | [추정] | 언어·멀티모달 모델로 평면도를 이해·생성·편집하거나(HouseMind, FloorplanQA) CAD 에서 지도를 뽑는(Zhang 외) 연구는 L. AI·학습 기술의 45. 문서·도면·장면 이해에 속하는 방법이며, 원문 교차 규칙대로 적용 대상인 14. 도면·BIM에서 지도 만들기와 이 영역 양쪽에서 연결해야 한다. | ref-823, ref-822, ref-083 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-815 | Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs) | Language to Map: Topological map generation from natural language path instructions | 2024-03-15 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.10008 | 아니오 |
| ref-816 | Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K. | SENT Map -- Semantically Enhanced Topological Maps with Foundation Models | 2025-11-05 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2511.03165 | 아니오 |
| ref-817 | Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W. | Tell2Design: A Dataset for Language-Guided Floor Plan Generation | 2023 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2311.15941 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-819 | Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX) | Learning Semantic Maps from Natural Language Descriptions | 2013-06 | 논문 | medium | 2026-09-29 | https://www.roboticsproceedings.org/rss09/p04.html | 아니오 |
| ref-820 | 김영재, 김세윤, 김홍준 (대한공간정보학회지) | 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구 | 2022-06 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654 | 아니오 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | 표준 | high | 2026-09-29 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-822 | Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P. | FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations | 2025-07-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.07644 | 아니오 |
| ref-823 | Qin, S., Weber, R. E., & Lu, X. | Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans | 2026-03-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2603.11640 | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — README (Demonstrations of Open-RMF) | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-825 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12-14 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-826 | Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022) | Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation | 2022-03 | 논문 | medium | 2026-09-29 | https://dl.acm.org/doi/10.5555/3523760.3523822 | 예 |
| ref-827 | 모빌리오(Mobilio) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 | 2026-08-24 | 벤더 문서 | low | 2026-09-29 | https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/ | 아니오 |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.00552 | 아니오 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f9(언어 모델의 공간 제약 미준수 → 확인·검증 필요), f16(SLAM 지도 작성의 시간·노동 한계와 도면 활용), f11(축척은 사람이 줘야 확정) / 섹션 4: f1(위상 지도), f2(사람·모델이 함께 고치는 JSON 지도), f10(빌딩 맵 요소), f11(축척 보정), f14(레이아웃 교환 형식), f20(명확화 질문) / 섹션 5: 병원 — f13(Clinic 데모 월드의 2층·승강기 2대, 시뮬레이션임을 명시), 제조 공장 — f19(벤더 주장 병기, 라이다 지도–도면 정합), 실외 — f17(공공 지도 기반 위상 지도), 기타 — f18(연계 대상: 대학 건물 다층 자율 지도화) / 섹션 6: f1·f3(언어→위상·의미 지도), f2(공동 편집 텍스트 지도), f5·f6·f7(언어→평면도 생성·편집), f8·f9(공간 추론 한계와 검증), f12·f21(텍스트 지도 구조를 대화로 채우고 확정 불가 값은 확인 질문) / 섹션 7: f10·f11(Open-RMF Traffic Editor·building.yaml), f14·f15(VDMA LIF·VDA 5050 노드·에지·스테이션), f13(rmf_demos) / 섹션 8: f1, f2, f3, f5, f6, f7, f8, f16, 국내 f17·f18 / 섹션 9: f22(연계 대상: SLAM·도면 해석), f23(직접 범위: 구조화 지도 요소 생성·확인 질문·사람 승인) / 섹션 10: 14. 도면·BIM에서 지도 만들기(f16·f24), 15. 지도·공간·위치 모델(f10·f14·f15), 16. 장소 의미·지도 관리(f2·f3), 45. 문서·도면·장면 이해(f24, 교차 규칙), 13. 대화형 기능의 신뢰·기반(f9·f20·f21), 22. 설비·건물 시스템 연동(f13 승강기·문), 20. 로봇·제조사 관제 연동(f14), 21. 상호운용 표준·적합성(f15) / 섹션 11: open_questions_new 3건. 다음 실행 후보: 14. 도면·BIM에서 지도 만들기 페이지에 f16·f24 반영, 15. 지도·공간·위치 모델 페이지에 f14·f15 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 트래픽 에디터 | Traffic Editor (Open-RMF) | 2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다. |
| 언어 유도 평면도 생성 | Language-guided Floor Plan Generation | 방 종류·위치·크기·관계를 적은 자연어 설명에서 공간·관계 제약을 만족하는 평면도를 생성하는 과제이다. |
| 명확화 질문 | Clarification Question (Follow-up Clarification) | 요청이 모호할 때 시스템이 아는 정보를 바탕으로 사용자에게 되묻는 질문으로, 확정할 수 없는 값을 추정으로 채우지 않고 사람에게 확인받는 대화 장치이다. |

## 열린 질문

새로 생긴 질문:

- 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? | 관련 영역: 8. 채팅으로 맵 작성, 15. 지도·공간·위치 모델, 21. 상호운용 표준·적합성 | 근거: f15 | 종류: 일반
- 언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? | 관련 영역: 8. 채팅으로 맵 작성, 13. 대화형 기능의 신뢰·기반 | 근거: f9 | 종류: 일반
- 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? | 관련 영역: 8. 채팅으로 맵 작성, 14. 도면·BIM에서 지도 만들기, 55. 현장 조사·설치·시운전 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 19회 · 신규 출처 15건
- 미확인 항목:
    - f20 ACM 원문 403 으로 미열람, 검색 결과 요약(63명 사용자 연구, 효과)만 사용
    - f19 모빌리오 맵 정합 기능은 벤더 주장이며 독립 출처 교차 확인 없음
    - f9 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f10·f11·f13 발행일 미확인(오픈소스 문서)
    - VDMA LIF 공식 가이드라인 PDF 는 텍스트 추출 실패로 공식 저장소 README 만 확인, JSON 구조 세부(층·지도 id 필드)는 미확인
    - ArchPlanVQA(ASCE, 도면 CAD 이해 벤치마크)는 403 으로 열지 못해 넣지 않음
    - Nav2 keepout 필터 문서는 docs.nav2.org·raw 경로 모두 404 로 열지 못해 넣지 않음
    - 대화만으로 로봇 지도를 만든 실제 현장 배치 사례(연구 프로토타입·시뮬레이션 데모 외)는 찾지 못함
    - 국내 언어 모델 기반 지도 작성 연구는 검색에서 확인되지 않음(국내 자료는 위상 지도 구축·다층 SLAM·벤더 정합 기능뿐)
- 범위 경계 위반 의심:
    - f18: 로봇 자체 SLAM·승강기 조작은 분류 원문 19장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f22: 라이다 지도 생성·도면 해석은 연계 영역(로봇 자체 지능·제어, 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해)이므로 '연계 대상: '으로 표시함
    - f5·f6·f7: 건축 설계용 평면도 생성 연구는 로봇 지도 작성이 아니므로 방법 참고로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 신규 출처 15건(ref-815~ref-163) 상한 도달로 rmf_traffic_editor 저장소 README(같은 Open Robotics 계열), LLM-Geo 류 GIS 에이전트 연구, HouseLLM·HypergraphFormer 등 추가 평면도 생성 연구는 넣지 못했다. 검색 19회/30. 원문 열람 14건(webfetch 11, github_raw 3), 미열람 1건(ref-826). 교차 확인 1건(f9: Tell2Design·FloorplanQA 독립 출처). 모든 finding 신뢰도 medium 이하(대부분 단일 출처, 논문은 초록 확인). 분류 원문 핵심 질문(말·도면만으로 쓸 수 있는 지도)에는 f1·f3(언어→위상·의미 지도 가능), f16(CAD→로봇 지도 자동 생성), f8·f9(언어 모델의 기하 제약 미준수)로 답했으며 결론은 '위상·의미 요소는 가능하나 기하·축척은 사람 확인이나 별도 입력이 필요'라는 추정(f4·f21·f23)이다. 현장 유형: 병원(f13, 시뮬레이션 데모임을 명시), 제조 공장(f19, 벤더 주장), 실외(f17), 기타(f18)로 물류창고 사례는 없다. L. AI·학습 기술 관련 finding(f6·f8·f16·f24)은 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기 양쪽에 연결하도록 제안했다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 807건과의 URL 중복을 대조하지 못했으므로 Traffic Editor·rmf_demos 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-26-02/research.md

```markdown
# 리서치 브리프 2026-09-26-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-26-02 |
| 날짜 | 2026-09-26 |
| 실행 유형 | monthly_recheck (월간 재검증) |
| 대상 영역 | 해당 없음 |
| 대분류 | 해당 없음 |

## 갭(비어 있거나 약한 섹션)

- target.json 이 재검증 대상 목록을 주지 않아(CLI 지정 monthly_recheck) 참고문헌 목록에서 발행 2년이 지난 표준·규정을 골라 재검증 대상으로 삼음
- ref-022 VDA 5050 2.0.0(2022-01): 3.0.0 판과의 관계 재확인 필요
- ref-139 ISO 22400-2:2014: 개정(Amd)·후속판 여부 미기록(4. 성과·경제성·프로세스 개선 7절 인용)
- ref-568 KS B ISO/TS 15066·ref-211 KS B ISO 10218-2: ISO 10218-2:2025 통합 이후 상태 미기록
- ref-470 ISO 3691-4:2023, ref-566 ISO 12100:2010: 개정 진행 여부 미기록
- ref-486 ISO 22301:2019: 개정 1:2024 내용 미기록
- ref-030 W3C SSN(2017): 2023 Edition 초안 존재 여부 미기록
- ref-345 실내공간정보 구축 작업규정(2018)과 ref-679(2021 고시)의 판 관계 미정리
- ref-637 산업 디지털 전환 촉진법 제명 변경(oq-122) 미확인
- ref-509 ISO 20607:2019·ref-510 IEC/IEEE 82079-1:2019 개정 진행 여부 미기록

## 조사 질문

1. 재검증 대상 ref-022 VDA 5050 2.0.0(2022-01): 현행판 여부
2. 재검증 대상 ref-139 ISO 22400-2:2014: 개정·후속판 여부(4. 성과·경제성·프로세스 개선 인용)
3. 재검증 대상 ref-568 KS B ISO/TS 15066(ISO/TS 15066:2016 부합)·ref-211 KS B ISO 10218-2: ISO 10218-2:2025 발행 뒤 상태
4. 재검증 대상 ref-470 ISO 3691-4:2023: 개정 진행 여부
5. 재검증 대상 ref-566 ISO 12100:2010: 개정 진행 여부
6. 재검증 대상 ref-486 ISO 22301:2019: 개정 1:2024 반영
7. 재검증 대상 ref-502 BPMN 2.0.2(2014-01)·ref-119 IEC 62264-3:2016: 현행판 여부(2. 공정·워크플로 모델링 인용)
8. 재검증 대상 ref-767 IEC 62443-3-3:2013: 현행판 여부
9. 재검증 대상 ref-030 W3C SSN(2017-10-19): 후속판 여부
10. 재검증 대상 ref-345 실내공간정보 구축 작업규정(2018-03-05): 현행 고시 여부
11. 재검증 대상 ref-314 KS B 7317(2021-11): 개정 여부
12. 재검증 대상 ref-637 산업 디지털 전환 촉진법(2022-01-04): 제명 변경·시행 여부(oq-122)
13. 재검증 대상 ref-509 ISO 20607:2019·ref-510 IEC/IEEE 82079-1:2019: 개정 진행 여부

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소 main 브랜치의 최신 게시판은 3.0.0 이므로, ref-022 가 가리키는 VDA 5050 2.0.0(2022-01)은 현행판이 아니라 이전 판으로 대체됨 상태다. | ref-052, ref-032, ref-022 | 아니오 | medium | 2026-09-26 | — | — |
| f2 | [사실] | ISO 22400-2:2014 에는 에너지 관리용 KPI 를 더한 개정 1(ISO 22400-2:2014/Amd 1:2017)이 2017-04 에 발행돼 있어, 4. 성과·경제성·프로세스 개선이 인용하는 ISO 22400-2:2014 는 개정 1과 함께 읽어야 한다. | ref-812, ref-139 | 아니오 | medium | 2017-04 | — | 원문 미열람 |
| f3 | [사실] | ISO 22400-2 는 개정판 ISO/DIS 22400-2 가 진행 중이며 2024-09-17 FDIS 등록이 승인돼 ISO 22400-2:2014 를 대체할 예정으로 표시돼 있으나, 새 판의 발행은 이번 실행에서 확인하지 못했다. | ref-811, ref-139 | 아니오 | medium | 2024-09-17 | — | 원문 미열람 |
| f4 | [사실] | ISO/TS 15066:2016 의 협동 적용 요구사항 대부분은 협동이 로봇 단독이 아닌 적용의 문제라는 이유로 ISO 10218-2:2025 에 통합되었다. | ref-471, ref-560 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f5 | [사실] | ISO 목록에서 ISO/TS 15066:2016 은 폐지되지 않고 2022 년 확인된 판으로 남아 있으며, 이를 대체할 ISO/AWI 15066-1(Collaborative Safety)이 개발 초기 단계에 있다. | ref-814, ref-813 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f6 | [추정] | 국가표준 목록에서 KS B ISO 10218-2 는 '2017 확인', KS B ISO/TS 15066 은 '2022 확인' 판으로 검색되고 ISO 10218-2:2025 를 부합화한 KS 는 이번 검색에서 확인되지 않아, 국내 KS 는 아직 구판(ISO 10218-2:2011·ISO/TS 15066:2016) 기준일 가능성이 있다. | ref-825, ref-568, ref-211 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f7 | [사실] | ISO 3691-4 는 2023 판이 현행이지만 차기판(ISO/CD 3691-4, 제2판 초안)이 위원회 검토 단계에 있다. | ref-819, ref-470 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f8 | [사실] | ISO 12100:2010 은 개정이 진행 중이며, 독일 DIN 이 개정 초안(DIN EN ISO 12100, 2025-01, ISO/DIS 12100:2024 기반)을 게시했다. | ref-820, ref-566 | 아니오 | medium | 2025-01 | — | 원문 미열람 |
| f9 | [추정] | ISO 12100 개정판은 2026 년 FDIS 단계 도달이 예상되며 2027-01-20 부터 적용되는 EU 기계 규정 2023/1230 에 맞춰 EN ISO 문안을 정렬하는 것으로 보인다. | ref-821, ref-555 | 아니오 | low | 2025-12-11 | — | 원문 미열람 |
| f10 | [사실] | ISO 22301:2019 에는 2024-02 발행된 개정 1(기후 행동 변경)이 있어, 조직 상황(4.1)과 이해관계자(4.2) 조항에서 기후 변화의 관련성 검토를 요구한다. | ref-822, ref-486 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f11 | [추정] | OMG BPMN 은 2014-01 발행된 2.0.2 판이 여전히 최신판으로 보이며, 이번 검색에서 그 뒤의 새 판은 확인되지 않았다. | ref-502 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f12 | [추정] | IEC 62264-3 은 2016 발행 제2판이 최신으로 검색되며, 이번 실행에서 그 뒤의 새 판은 확인되지 않아 2. 공정·워크플로 모델링의 인용은 유효한 것으로 보인다. | ref-119 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f13 | [추정] | IEC 62443-3-3 은 2013-08 발행 제1판이 현행으로 검색되며, 개정판 진행 상태는 이번 실행에서 확인하지 못했다. | ref-767 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f14 | [사실] | W3C 는 SSN 온톨로지의 후속판 'Semantic Sensor Network Ontology - 2023 Edition' 을 공개 작업 초안(Working Draft)으로 냈고 아직 권고안이 아니므로, 현행 권고안은 ref-030 의 2017 판이다. | ref-817, ref-818, ref-030 | 아니오 | medium | 2025 | — | — |
| f15 | [사실] | IEC/IEEE 82079-1 은 2019 판(제2판)이 현행이며 차기판이 위원회 초안(IEC/IEEE CD 82079-1) 단계에 있다. | ref-823, ref-510 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f16 | [추정] | ISO 20607:2019 는 디지털 사용 설명서를 반영하는 개정(ISO/DIS 20607)이 진행돼 2025-05-03 국제 투표가 끝났고 EN 채택 기한이 2026-01-20 으로 알려졌으나, 새 판 발행은 이번 실행에서 확인하지 못했다. | ref-824, ref-509 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f17 | [사실] | ref-345 는 실내공간정보 구축 작업규정의 2018-03-05 판을 가리키고, 같은 규정의 고시 제2021-1445호(2021-12-24) 판이 ref-679 로 따로 등록돼 있어 ref-345 는 구판이며, 2021 판 이후 개정 고시는 이번 검색에서 확인되지 않았다. | ref-345, ref-679 | 아니오 | medium | 2021-12-24 | — | 원문 미열람 |
| f18 | [추정] | KS B 7317(2021-11 제정)은 이번 검색에서 개정 기록이 확인되지 않았고 현행 표준으로 검색된다. | ref-314 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f19 | [사실] | 국가법령정보센터에 '산업 디지털 전환 및 인공지능 활용 촉진법' 제명의 법령 제정·개정문 페이지가 존재해, ref-637 이 가리키는 산업 디지털 전환 촉진법의 제명이 바뀐 것으로 확인된다. | ref-815, ref-637 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f20 | [추정] | 제명이 바뀐 '산업 디지털 전환 및 인공지능 활용 촉진법' 은 2026-07-01 부터 시행된 것으로 보도됐으나, 데이터 공동 생성 규정의 조문 번호·내용 변화는 확인하지 못했다. | ref-816 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-26 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-26 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 예 |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-26 | https://github.com/VDA5050/VDA5050/blob/main/README.md | 아니오 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/54497.html | 예 |
| ref-811 | ISO | ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/87563.html | 예 |
| ref-812 | ISO | ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management | 2017-04 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/68295.html | 예 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 미확인 | 업계 보고서 | medium | 2026-09-26 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/73934.html | 예 |
| ref-813 | ISO | ISO/AWI 15066-1 - Collaborative Safety | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/91522.html | 예 |
| ref-814 | ISO | ISO/TS 15066:2016 - Robots and robotic devices — Collaborative robots | 2016 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/62996.html | 예 |
| ref-825 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2(2017 확인) 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010116494 | 예 |
| ref-568 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 (2022-10-12 확인판 있음) | 2017-02-28 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 | 예 |
| ref-211 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/83545.html | 예 |
| ref-819 | ISO | ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/88615.html | 예 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | 표준 | medium | 2026-09-26 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 예 |
| ref-820 | DIN Media | DIN EN ISO 12100 - 2025-01 (Draft standard) | 2025-01 | 표준 | medium | 2026-09-26 | https://www.dinmedia.de/en/draft-standard/din-en-iso-12100/386233502 | 예 |
| ref-821 | Intertek | Machines Got Smarter, Now ISO 12100 has to Catch Up | 2025-12-11 | 업계 보고서 | low | 2026-09-26 | https://www.intertek.com/blog/2025/12-11-machines-and-iso-12100/ | 예 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | medium | 2026-09-26 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-486 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/75106.html | 예 |
| ref-822 | ISO | ISO 22301:2019/Amd 1:2024 - Security and resilience — Business continuity management systems — Requirements — Amendment 1: Climate action changes | 2024-02 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/88412.html | 예 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | medium | 2026-09-26 | https://www.omg.org/spec/BPMN/2.0.2/ | 예 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/67480.html | 예 |
| ref-767 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 2013-08 | 표준 | medium | 2026-09-26 | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 | 예 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-09-26 | https://www.w3.org/TR/vocab-ssn/ | 예 |
| ref-817 | W3C | First Public Working Draft: Semantic Sensor Network Ontology - 2023 Edition | 2025 | 표준 | medium | 2026-09-26 | https://www.w3.org/news/2025/first-public-working-draft-semantic-sensor-network-ontology-2023-edition/ | 예 |
| ref-818 | W3C Spatial Data on the Web WG (w3c/sdw-sosa-ssn GitHub) | sdw-sosa-ssn — README (Repository of the Spatial Data on the Web Working Group for the SOSA/SSN vocabulary) | 미확인 | 표준 | high | 2026-09-26 | https://github.com/w3c/sdw-sosa-ssn | 아니오 |
| ref-510 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/71620.html | 예 |
| ref-823 | IEC / IEEE / ISO | IEC/IEEE CD 82079-1 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/87206.html | 예 |
| ref-509 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/68519.html | 예 |
| ref-824 | IBF Solutions | New EN ISO 20607 – Instruction handbook for machinery | 미확인 | 업계 보고서 | low | 2026-09-26 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-en-iso-20607-instruction-handbook-for-machinery | 예 |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 2018-03-05 | 정부·연구기관 | medium | 2026-09-26 | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 | 예 |
| ref-679 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 2021-12-24 | 정부·연구기관 | medium | 2026-09-26 | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | 정부·연구기관 | medium | 2026-09-26 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 예 |
| ref-815 | 국가법령정보센터 | 법령 > 제정·개정문 > 산업 디지털 전환 및 인공지능 활용 촉진법 | 미확인 | 정부·연구기관 | medium | 2026-09-26 | https://law.go.kr/lsInfoP.do?lsiSeq=281883&viewCls=lsRvsDocInfoR | 예 |
| ref-816 | 폴리뉴스 | [입법이 산업을 바꾼다] 공장이 AI를 쓰기 시작했다…'산업 AI법' 시행이 제조업을 바꾼다 | 미확인 | 기사 | low | 2026-09-26 | https://www.polinews.co.kr/news/articleView.html?idxno=743929 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md | 4, 7 | needs_update 제안 (f2·f3): ISO 22400-2:2014 인용에 개정 1:2017(에너지 관리 KPI, ref-812)과 진행 중인 개정판 ISO/DIS 22400-2(2024-09-17 FDIS 등록 승인, ref-811)를 병기하고 기준일을 갱신한다. 4·7절은 주제 페이지로 분리돼 있으므로 해당 주제 페이지(2026-09-25-area04-s4, 2026-09-25-area04-s7)와 표준 목록의 ISO 22400-2 항목도 함께 고친다. 다음 실행 후보: 2. 공정·워크플로 모델링의 BPMN 2.0.2(f11)·IEC 62264-3:2016(f12)은 유효로 판정해 수정 불필요. |
| update | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md | 7 | needs_update 제안 (f4·f5·f6·f7·f8·f9): ISO/TS 15066 요구사항의 ISO 10218-2:2025 통합과 ISO/AWI 15066-1 개발, KS B ISO/TS 15066·KS B ISO 10218-2 의 구판 기준 가능성, ISO 3691-4 차기판(CD)·ISO 12100 개정 초안 진행을 반영. 다음 실행 후보: ref-022 needs_update(3.0.0 으로 대체됨, f1), ref-345 deprecated 제안(대체 출처: ref-679, f17), ref-637 needs_update(제명 변경 f19·f20, 28. 표준·상호운용성·다사업자 거버넌스 표기 재확인), ref-030 SSN 에 2023 Edition 초안 병기(f14, 5. 로봇 능력·작업 온톨로지와 트랙 manual-capability-ontology 비교표), ref-486 에 개정 1:2024 병기(f10, 20. 예외 복구·재계획·업무 연속성), ref-509·ref-510 개정 진행 병기(f15·f16, 트랙 매뉴얼 문서 유형), ref-767 IEC 62443-3-3·ref-314 KS B 7317 유효(f13·f18). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- ISO 10218-2:2025 발행 뒤 국내 KS B ISO 10218-2 와 KS B ISO/TS 15066 은 새 판으로 부합 개정되었거나 개정 예고되었는가, 국내 협동로봇 설치 작업장 안전인증은 어느 판을 기준으로 하는가? | 관련 영역: 25. 안전·위험 관리, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f6 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 38 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - f3 ISO 22400-2 개정판의 발행 여부 미확인(FDIS 등록 승인까지만)
    - f6 KS B ISO 10218-2·KS B ISO/TS 15066 의 2025 판 부합 여부 미확인(검색 범위 내 미발견)
    - f9 ISO 12100 FDIS 시점은 업계 블로그 요약뿐
    - f13 IEC 62443-3-3 개정판 진행 상태 미확인
    - f16 ISO 20607 새 판 발행 여부 미확인
    - f18 KS B 7317 개정 여부 미확인
    - f20 산업 디지털 전환 및 인공지능 활용 촉진법 시행일은 기사 1건뿐, 데이터 공동 생성 조문 번호·내용 미확인(oq-122 부분 답)
    - MassRobotics AMR 상호운용 표준(ref-033) 판 정보는 공식 저장소 README 에 없어 재검증하지 못함
- 범위 경계 위반 의심:
    - 없음
- 한계: 월간 재검증: target.json 이 재검증 대상을 지정하지 않아 참고문헌 목록에서 발행 2년이 지난 표준·규정 중 세부영역 페이지 인용과 연관된 것을 골랐다(전수 재검증 아님). web_fetch_available: false · fetch_mode mirror_only 로 github_raw 원문은 2건(ref-052 VDA 5050 README, ref-818 SOSA/SSN 작업반 README)만 열었고 나머지는 검색 결과 요약 범위만 사용해 신뢰도 상한 medium. 교차 확인 0건(같은 발행 기관 계열 출처뿐이거나 단일 출처). 판정 요약: 대체됨 — ref-022(3.0.0), ref-345(2021 고시 ref-679); 개정·후속 진행 — ref-139(Amd1·DIS), ref-568(10218-2:2025 통합·AWI 15066-1), ref-470(CD), ref-566(DIS), ref-486(Amd1:2024), ref-030(2023 Edition WD), ref-509·ref-510(DIS·CD), ref-637(제명 변경); 유효 — ref-502, ref-119, ref-767, ref-314(모두 추정 수준). oq-122 는 제명 변경·시행은 확인했으나 조문 변화가 미확인이라 해결로 올리지 않았다. 페이지 제안은 갱신 상한 2건에 맞추고 나머지는 rationale 에 다음 실행 후보로 남겼다. 입력의 대상 세부영역 페이지는 1~4번만 주어져 25. 안전·위험 관리 등 나머지 페이지의 인용 문장은 직접 대조하지 못했다. 신규 출처 15건(ref-811~ref-825) 상한 도달.
```

### runs/2026-09-25-25/research.md

```markdown
# 리서치 브리프 2026-09-25-25

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-25 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 10. 설비·건물 시스템 연동 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 문·승강기·작업대(워크셀) 어댑터, 승강기 모드·세션, 해제 구역 개념 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 설비 인터페이스, VDA 5050 의 주변 설비 범위, 국내 KS·단체표준 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-010 연결 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [분류원문]
2. 로봇 관제가 문·승강기·작업대(컨베이어 등)와 요청·상태·완료를 주고받는 공개 인터페이스(Open-RMF 설비 메시지 등)는 어떤 구조인가? (섹션 4·6·7 겨냥)
3. VDA 5050 같은 로봇–관제 표준은 주변 설비 연동을 어디까지 다루며, 설비 연동 책임은 누구에게 두는가? (섹션 7·9 겨냥)
4. 국내에서 로봇의 승강기 탑승·연동을 다루는 국가표준·단체표준·제조사 API 는 무엇이 있는가? (섹션 7·8, 한국 자료 우선)
5. 승강기 같은 공용 설비가 다층 운반의 대기 시간·처리량에 주는 영향을 다룬 연구는 무엇인가? (섹션 3·8, oq-010 관련)
6. 설비 연동에서 ROP 가 맡는 요청·예약·상태 확인과 외부 설비 제어·안전 제어의 경계는 어디인가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 는 문 제어기와 통신하는 문 노드(door node) 앞에 문 어댑터를 두어, 플릿 어댑터·RMF 핵심 시스템의 문 요청을 받아 로봇 운영을 방해하지 않는다고 판단될 때만 문 노드에 전달하는 상태 감독자 역할을 맡긴다. | ref-283 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | Open-RMF 의 문 상태 메시지(DoorMode)는 자동문 제어기의 상태를 닫힘·움직이는 중·열림·오프라인·알 수 없음의 다섯 값으로 보고한다. | ref-412 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f3 | [사실] | Open-RMF 의 승강기 어댑터는 플릿 어댑터·RMF 핵심 시스템의 승강기 요청을 받아 적절하다고 판단될 때만 승강기 노드에 전달하고, 어댑터를 거치지 않고 승강기 노드에 직접 보낸 요청은 무효로 만든다. | ref-284 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f4 | [사실] | Open-RMF 승강기 요청 메시지(LiftRequest)는 승강기 이름, 요청자별 세션 id, 요청 유형(세션 종료·AGV 모드·사람 모드), 목적 층, 문 상태(닫힘·열림)를 담으며, AGV 모드에서는 정지 시 문이 항상 열려 있고 사람 모드에서는 문이 시간 초과로 자동으로 닫힐 수 있다. | ref-411 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | Open-RMF 승강기 상태 메시지(LiftState)는 이용 가능한 층·현재 층·목적 층, 문 상태(닫힘·움직임·열림), 운행 상태(정지·상승·하강·알 수 없음), 모드(설정 가능한 사람·AGV, 읽기만 가능한 화재·오프라인·비상)와 승강기를 점유한 세션 id 를 보고한다. | ref-286 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | Open-RMF 는 작업대(workcell)를 물건을 내주는 디스펜서와 받아들이는 인제스터 두 유형으로 두고 각각 요청·결과·상태 메시지를 쓰며, 배송 작업에서 로봇은 픽업 위치에서 디스펜서 서비스를 요청해 확인을 기다린 뒤 하역 위치에서 인제스터 서비스를 요청해 확인을 기다린다. | ref-023, ref-047, ref-049 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f7 | [사실] | VDA 5050 3.0.0 은 관제와 이동로봇 사이 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f8 | [사실] | VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 가운데 하나로 들어, 설비 연동 책임을 로봇이 아니라 관제 쪽에 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f9 | [사실] | VDA 5050 3.0.0 의 해제 구역(RELEASE zone)은 관제의 진입 허가를 받아야 들어갈 수 있는 구역으로, 로봇이 상태 메시지의 zoneRequests 로 진입을 요청하면 관제가 responses 토픽으로 허가·대기·철회·거절을 답하고, 허가가 철회·만료될 때의 행동은 releaseLossBehavior(정지·계속·대피)로 정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f10 | [사실] | VDA 5050 3.0.0 의 동작 구역(ACTION zone)은 로봇이 구역에 들어갈 때·지나는 동안·나올 때 미리 정한 action(entryActions·duringActions·exitActions)을 수행하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f11 | [사실] | 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했으며, 행정안전부(승강기 안전기준 소관)와 협력해 추진했다. | ref-413, ref-414 | 아니오 | medium | 2021-11 | 제약 | 원문 미열람 |
| f12 | [사실] | 국가기술표준원 보도자료는 로봇이 건물 안을 이동하고 엘리베이터에 타려면 속도 제어, 위험 상황에서의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지 기준이 필요하다고 설명한다. | ref-414 | 아니오 | medium | 2021-11 | 제약 | 원문 미열람 |
| f13 | [사실] | 대한승강기협회는 엘리베이터에 로봇이 탑승할 수 있도록 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준을 제정했다고 보도됐다. | ref-415 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | 대한승강기협회는 산업통상자원부 과제 '디지털 기반 차세대 개방형 승강기 운영시스템 개발'을 수행하며 승강기·로봇 분야 23개 단체 24명의 협의체를 꾸려 API 로 실시간 정보를 주고받는 승강기–로봇 연동 프로토콜(안)과 시나리오(안)를 협의했다고 보도됐다. | ref-416 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | KONE 은 청소·배송·보안용 자율 로봇을 자사 승강기와 연동하는 Service Robot API 를 엘리베이터 호출 API·설비 상태 API 와 함께 제공한다고 밝힌다. | ref-417 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f16 | [추정] | 현대엘리베이터는 2022년 3월 로봇이 엘리베이터를 호출해 탑승하는 '로봇 연동' 등을 제공하는 클라우드 기반 오픈 API 를 공개하고 추가 장비 없이 연동할 수 있다고 밝혔다. | ref-418 | 아니오 | low | 2022-03 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f17 | [추정] | 현대엘리베이터는 오픈 API 참여 주체가 1년여 만에 60여 곳으로 늘었고 병원·호텔·은행 등에서 배송로봇 40여 대가 자사 엘리베이터를 이용해 운행 중이라고 밝혔다. | ref-419 | 아니오 | low | 2023-02 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f18 | [사실] | Electronics(2025) 게재 연구는 실내 배송 로봇의 다층 경로계획에서 승강기 선택을 최적화하는 그래프 기반 방법을 제안해 층간 이동과 승강기 대기 시간을 경로계획에 함께 넣었다. | ref-420 | 아니오 | medium | 2025 | 예외·성과 | 원문 미열람 |
| f19 | [사실] | Digital Health(2026) 게재 연구는 이용이 많은 병원 환경에서 승강기 이용을 고려해 자율 약품 배송 로봇의 실현 가능성을 평가했다. | ref-060 | 아니오 | medium | 2026 | 예외·성과 | 원문 미열람 |
| f20 | [사실] | 다층 호텔 환경의 로봇 배송 경로계획 연구는 승강기를 포함한 층간 이동을 다중 로봇 경로계획 문제에 넣어 다룬다. | ref-103 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f21 | [사실] | 국내 연구(로봇학회 논문지 2026)는 탐사와 엘리베이터 연계를 이용해 다층 실내 지도를 자율로 구축하는 시스템을 보고했다. | ref-163 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f22 | [사실] | 국토교통부는 로봇이 승강기 등을 이용해 건물 안을 이동할 수 있게 하는 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'에 착수한다고 발표했다. | ref-421 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f23 | [추정] | 분류 원문의 질문(컨베이어 준비와 로봇 도착을 어떻게 맞출까)에 대해, Open-RMF 의 디스펜서·인제스터처럼 로봇 도착 후 설비에 요청을 보내고 결과를 받아야 다음 단계로 넘어가는 요청–결과 방식과, VDA 5050 해제 구역처럼 설비 앞 구역 진입을 관제가 허가하는 방식을 조합하면 ROP 가 설비 준비 신호와 로봇 도착을 한 작업 흐름 안에서 맞출 수 있을 것으로 보인다. | ref-023, ref-031 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f24 | [추정] | 입고·적치에서 로봇이 층간 운반에 승강기를 쓰면 한 세션이 승강기를 점유하는 동안 다른 로봇이 기다려야 하므로(Open-RMF 세션 방식), 승강기 대기가 처리량과 운반 시간에 영향을 줄 것으로 보인다. | ref-411, ref-286, ref-060, ref-103 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f25 | [추정] | 승강기가 화재·비상·오프라인 모드로 바뀌거나 문 상태가 오프라인·알 수 없음으로 보고되면 ROP 는 해당 설비를 쓰는 작업을 멈추거나 다른 경로·사람 확인으로 넘기는 예외로 다뤄야 할 것으로 보인다. | ref-286, ref-412 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f26 | [추정] | 연계 대상: 승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어는 설비 제조사·설비 제어기 쪽에 남고, ROP 는 어댑터를 통해 작업 요청·점유 예약·상태 확인·완료 확인을 맡는 것으로 보인다. | ref-283, ref-284, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 예 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.1177/20552076261437181 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-411 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-412 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-413 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-414 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 예 |
| ref-415 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 미확인 | 기사 | low | 2026-09-25 | https://www.ctman.kr/35296 | 예 |
| ref-416 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | 기사 | low | 2026-09-25 | https://www.electimes.com/news/articleView.html?idxno=320147 | 예 |
| ref-417 | KONE | KONE Service Robot API | 미확인 | 벤더 문서 | low | 2026-09-25 | https://dev.kone.com/api-portal/service-robot-api/ | 예 |
| ref-418 | 한국경제 | 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 | 2022-03 | 기사 | low | 2026-09-25 | https://www.hankyung.com/economy/article/202203314153Y | 예 |
| ref-419 | 파이낸셜뉴스 | 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" | 2023-02 | 기사 | low | 2026-09-25 | https://www.fnnews.com/news/202302140913318867 | 예 |
| ref-420 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics14050982 | 예 |
| ref-421 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f7·f8(로봇–관제 표준이 설비 연동을 관제에 맡김), f24(승강기 대기가 처리량에 영향), f22 / 섹션 4: f1·f3(문·승강기 어댑터), f4·f5(승강기 모드·세션), f6(디스펜서·인제스터), f9·f10(해제·동작 구역) / 섹션 5: 출하 완료·인계 f6·f23, 적치 예외·성과 f24·f25 / 섹션 6: f1~f6(어댑터 경유 요청·상태 감독), f9·f10(구역 기반 진입 허가), f23 / 섹션 7: Open-RMF 설비 메시지 f1~f6, VDA 5050 범위 f7~f10, 국내 KS B 7317 f11·f12, 대한승강기협회 단체표준·프로토콜 f13·f14, 제조사 API f15~f17(모두 [추정] 벤더 주장) / 섹션 8: f18~f22 / 섹션 9: f26(연계 대상: 설비 제어·안전은 외부), f7·f8 / 섹션 10: 9. 로봇·제조사 관제 연동(f8), 15. 다중 로봇 경로·교통 관리 — MAPF(f18·f20), 16. 공용 자원·충전·에너지 최적화(f24 승강기 점유), 3. 처리능력·거점·설비 계획(f24, oq-010), 6. 지도·공간·위치 모델(f21), 17. 로봇 간 협업·물리적 인계(f6), 20. 예외 복구·재계획·업무 연속성(f25), 25. 안전·위험 관리(f11·f12), 12. 명령·작업 실행의 신뢰성(f4 세션) / 섹션 11: 기존 oq-010 연결, open_questions_new 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 승강기 어댑터 | Lift Adapter | Open-RMF 에서 플릿 어댑터·핵심 시스템의 승강기 요청을 받아 적절할 때만 승강기 노드에 전달하는 감독 구성요소이다. |
| 디스펜서·인제스터 | Dispenser / Ingestor | Open-RMF 에서 로봇에 물건을 내주는 작업대(디스펜서)와 로봇에서 물건을 받아들이는 작업대(인제스터)로, 각각 요청·결과·상태 메시지로 배송 작업과 연동된다. |
| 해제 구역 | Release Zone | VDA 5050 3.0.0 에서 관제의 진입 허가를 받아야 이동로봇이 들어갈 수 있는 구역이다. |

## 열린 질문

새로 생긴 질문:

- 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? | 관련 영역: 10. 설비·건물 시스템 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f13 | 종류: 일반
- 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? | 관련 영역: 10. 설비·건물 시스템 연동, 17. 로봇 간 협업·물리적 인계 | 근거: f7 | 종류: 일반
- 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? | 관련 영역: 10. 설비·건물 시스템 연동, 26. 사이버보안·접근권한·개인정보 | 근거: f1 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 11회 · 신규 출처 14건
- 미확인 항목:
    - f11 KS B 7317 두 출처가 국가기술표준원 계열이라 독립 교차 아님, 표준 본문 조항 미확인
    - f13 단체표준 번호·제정일·내용 미확인
    - f15~f17 제조사 API·운행 대수는 벤더 주장이며 독립 확인 없음
    - f18·f19·f20 결과 수치·실험 조건 미확인
    - f22 국토교통부 보도자료 발행일 미확인
    - 컨베이어–로봇 인계 핸드셰이크의 공식 표준 출처를 찾지 못함(블로그·제품 페이지만 확인되어 넣지 않음)
    - VDMA 40001(OPC UA for Machinery)의 물류 설비 적용 범위는 검색 요약만으로 확정하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f26: 승강기·자동문·컨베이어·PLC 제어와 설비 안전 제어는 분류 원문 9장 '시설·설비 제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f11·f12: KS B 7317 은 로봇 자체의 탑승 안전 요구사항이므로 ROP 직접 범위가 아니라 25. 안전·위험 관리 연결과 제약 조건으로만 제안
- 한계: 재실행 1회차. 반려 사유 1(f17 벤더 문서 근거 [사실]에 vendor_claim 누락): 직전 반환값이 이 프롬프트에 포함되지 않아 같은 범위로 브리프를 다시 구성했고, 벤더·제조사 발표에 기댄 기능·실적 주장 f15·f16·f17 을 모두 vendor_claim: true, 태그 [추정], evidence_excerpt 첫머리 '벤더 주장: '으로 냈다 (관련 finding: f15, f16, f17). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처는 ref-023·ref-031(재사용)과 ref-283~ref-412(신규) 7건이고, 나머지 14건(신규 9, 재사용 5)은 원문 미열람이라 신뢰도 상한 medium(기사·벤더는 low). 검색 11회/30, 신규 출처 14건/15(ref-283~ref-421, 예약 구간 안). 교차 확인 0건: 대부분 단일 출처이거나 같은 발행 주체의 문서다. 한국 자료: KS B 7317, 국가기술표준원·국토교통부 보도자료, 대한승강기협회 단체표준·협의체 기사, 현대엘리베이터 오픈 API 기사, 국내 논문(ref-163). 분류원문 질문(컨베이어 준비와 로봇 도착 맞추기)은 f23 으로 추정 수준 답만 냈고 정량 연구는 찾지 못했다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 이전 실행 2026-09-25-20 의 신규 출처(ref-258~ref-272, 예: Franke 외 VDA 5050 주변 설비 논문)는 참고문헌 목록에 없어 재사용하지 않았다.
```
