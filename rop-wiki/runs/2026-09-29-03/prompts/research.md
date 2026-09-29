(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-03
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 11. 채팅으로 실제 상황 시뮬레이션 재현 (C. 채팅 기반 구성·운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-824
- 새 출처 id 구간: ref-824 ~ ref-853 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-824 부터 순서대로 쓰고 ref-853 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-03/target.json

```json
{
  "run_id": "2026-09-29-03",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 95,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 11,
    "area_name": "11. 채팅으로 실제 상황 시뮬레이션 재현",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=11"
}
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 11
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현

# 11. 채팅으로 실제 상황 시뮬레이션 재현

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

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]

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

### docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md (요약)

```markdown
# 10. 채팅으로 로봇 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 823건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 211개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
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

### docs/open-questions.md (요약: 대상 영역 [11] 에 걸린 0건 / 전체 130건)

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

### runs/2026-09-29-02/research.md

```markdown
# 리서치 브리프 2026-09-29-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-02 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 10. 채팅으로 로봇 구성 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 연합 형성·어포던스·능력 매칭·팩트시트·플릿 설정·구성 코파일럿 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 팩트시트, IDTA 02020 능력 기술, Open-RMF 플릿 설정 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 5. 로봇 능력·작업 표현과 짝 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]
2. 자연어 지시에서 이기종 로봇 팀을 구성(연합 형성)하고 능력에 따라 역할을 배정하는 언어 모델 연구는 무엇이 있고, 로봇 능력을 어떤 형태로 모델에 주는가? (섹션 6·8 겨냥)
3. 대화로 정한 로봇 구성이 시나리오의 작업을 수행할 수 있는지를 온톨로지·능력 모델로 실행 전에 확인하는 방법(능력 매칭, 계획 생성, 어포던스)은 무엇인가? (섹션 4·6·7 겨냥)
4. 로봇 종류·장비·적재·초기 위치·역할을 담는 구조화 데이터 형식(VDA 5050 팩트시트, AAS 능력 기술 서브모델, Open-RMF 플릿 설정)은 어떤 필드를 두는가? (섹션 4·7 겨냥)
5. 언어 모델이 낸 구성·조정안을 제약 해결기·시뮬레이션·사람 검토로 검증한 사례는 어느 현장 유형에서 보고되었는가? (섹션 3·5·11 겨냥, 13. 대화형 기능의 신뢰·기반 연결)
6. 로봇 대수를 정하는 근거(대수 산정 시뮬레이션·로봇 대 작업자 비율)는 무엇이며 국내 자료가 있는가? (섹션 5·8 겨냥)
7. 채팅 로봇 구성에서 ROP가 직접 맡을 것과 로봇 자체 스킬 실행·제조사 관제에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | SMART-LLM(Kannan·Venkatesh·Min, 2023)은 고수준 자연어 지시를 작업 분해 → 연합 형성(로봇 팀 구성) → 작업 배정의 세 단계로 나눠 프로그램형 few-shot 프롬프트로 다중 로봇 작업 계획을 만들며, 네 가지 복잡도의 벤치마크와 시뮬레이션·실제 로봇 실험으로 평가했다. | ref-090 | 아니오 | medium | 2024-03-23 | 수행 자원 | — |
| f2 | [사실] | CoMuRoS(Borate 외, 2025)는 중앙의 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 동적 문맥(작업 이력, 로봇·작업 상태, 이벤트)으로 이기종 로봇에 하위 작업을 배정하고, 로봇마다 자체 언어 모델이 ROS 2 기본 스킬로 실행 코드를 만드는 구조로, 하드웨어 실험에서 협동 회수 9/10, 협동 운반 8/8, 사람 보조 회수 5/5 성공을 보고했다. | ref-677 | 아니오 | medium | 2026-06-18 | 수행 자원 | — |
| f3 | [추정] | 언어 모델 기반 다중 로봇 계획 연구(SMART-LLM, CoMuRoS)가 로봇 유형별 스킬 집합을 텍스트로 모델에 주고 그 위에서 팀 구성과 역할 배정을 하는 점을 보면, 채팅으로 로봇 구성은 로봇 종류·역할을 자유 서술이 아니라 기계가 읽을 수 있는 능력 목록으로 만들어 두어야 이후 배정·계획 단계가 그것을 쓸 수 있을 것으로 보인다. | ref-090, ref-677 | 아니오 | low | 2026-09-29 | — | — |
| f4 | [사실] | SayCan(Ahn 외, 2022)은 언어 모델이 제안한 고수준 행동 후보를 스킬별 가치 함수(어포던스)가 현재 환경에서 실행 가능한지로 점수화해 결합함으로써, 언어로 표현된 지시를 물리적으로 실행 가능한 로봇 행동에 접지(grounding)한다. | ref-088 | 아니오 | medium | 2022-08-16 | 제약 | — |
| f5 | [사실] | Nakajima·Miura(IROS 2024)는 서비스 로봇의 '가져다 줘' 작업에서 환경 정보를 담은 온톨로지와 언어 모델을 결합해, 온톨로지의 확정 지식으로 언어 모델의 환각을 줄이고 사용자에게 되묻는 명확화 질문의 필요를 줄이는 방식을 제안했다. | ref-820 | 아니오 | medium | 2024-10-22 | — | — |
| f6 | [사실] | Vieira da Silva 외(2024)는 자연어 능력 설명을 few-shot 프롬프트로 기계 해석 가능한 능력 온톨로지로 바꾸고, 생성 결과를 구문 검사·모순 검사·환각 및 누락 요소 검사의 자동 루프로 검증해 사람은 처음 설명과 마지막 검토만 맡게 하는 방법을 제안했다. | ref-465 | 아니오 | medium | 2024-10-18 | — | — |
| f7 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 은 자산관리셸 안에서 공정·제품이 요구하는 능력(required)과 자원이 제공하는 능력(provided)을 속성(최대 속도·공차 등), 속성 제약(전제·불변·사후 조건)과 전이 제약(순서·병렬), 그리고 능력을 구현하는 스킬과 함께 모델링해 요구 능력과 자원 능력을 비교·매칭할 수 있게 한다. | ref-229 | 아니오 | medium | 2026-09-29 | 제약 | 원문 미열람 |
| f8 | [사실] | Nabizada 외(IEEE CASE 2026)는 VDI 3682·IEC 61360-1·IDTA 02011·IDTA 02016 으로 구조화한 자산관리셸 능력 모델에서 PDDL 계획 문제를 자동 생성해, PDDL 전문 지식 없이도 주어진 설비 배치가 요구 공정 순서를 지원하는지 자동 계획으로 확인하고 배치 대안 4종을 비교하는 방법을 실험실 생산 시스템으로 검증했다. | ref-201 | 아니오 | medium | 2026-06-01 | 완료·인계 | — |
| f9 | [추정] | 요구 능력과 제공 능력을 같은 모델로 적는 능력 기술 서브모델과 그 모델에서 계획 문제를 자동 생성해 배치의 실행 가능성을 확인하는 연구를 함께 보면, 이 영역의 '로봇 구성 적합성 사전 확인'은 시나리오에서 요구 능력을, 대화로 정한 로봇 집합에서 제공 능력을 뽑아 매칭하거나 계획을 시도해 보고 부족한 능력·대수를 되돌려 주는 방식으로 구현할 수 있을 것으로 보인다. | ref-229, ref-201 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f10 | [사실] | VDA 5050 3.0.0 의 팩트시트(factsheet) 토픽은 관제가 이동 로봇을 설정하는 데 쓰는 매개변수·제조사 정보로, typeSpecification(seriesName, agvKinematic, agvClass, maxLoadMass, localizationTypes, navigationTypes), physicalParameters, protocolLimits, protocolFeatures, agvGeometry, loadSpecification(loadPositions, loadSets), vehicleConfig 로 구성된다. | ref-031 | 아니오 | medium | 2026-09-29 | 작업 대상 | — |
| f11 | [사실] | Open-RMF 플릿 어댑터 템플릿의 설정 파일(config.yaml)은 rmf_fleet 절에 플릿 이름, 선속도·각속도·가속도 한계, 발자국·근접 반경(profile), 후진 가능 여부, 배터리·기계·주변·도구 시스템 값, 재충전 임계값, 플릿이 수행할 수 있는 RMF 작업 유형(task_capabilities), 사용자 정의 동작(actions), 작업 종료 후 행동(finishing_request), 로봇별 충전기 배정과 개별 재정의를 두는 robots 목록을 적는다. | ref-105 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f12 | [추정] | 이 영역이 대화로 정하려는 값(로봇 종류·대수·장착 장비·초기 위치·역할)은 VDA 5050 팩트시트의 종류·적재 사양과 Open-RMF 플릿 설정의 작업 유형·로봇 목록·충전기 배정처럼 관제가 실제로 읽는 구조에 이미 자리가 있으므로, 채팅 로봇 구성의 결과물은 이런 구조를 채우는 구조화 값이어야 하고 팩트시트 같은 등록 데이터는 대화가 물어볼 필요 없이 읽어 오는 입력이 될 것으로 보인다. | ref-031, ref-105 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f13 | [사실] | Valerio 외(2026)는 산업 제품 구성 문제에서 언어 모델과 기호적 제약 해결을 결합하는 신경-기호 방식을 하이브리드 추론·미세조정·훈련의 세 통합 전략으로 정리하고, 대화형 '구성 코파일럿'의 출력이 구문상 유효하고 수백 개 기능·규칙의 지식 베이스와 의미적으로 일치하며 실제 제조 가능해야 한다는 조건을 제시했다. | ref-824 | 아니오 | medium | 2026-09-24 | 제약 | — |
| f14 | [사실] | Ko·Lin(2026)은 병원 멸균공급실을 본뜬 가상의 수술기구 분류 라인 4개를 대상으로 운영자가 자연어로 라인·작업 조정을 요청하면 로컬 언어 모델이 구조화 요구사항과 후보 전략을 만들고 디지털 트윈 시뮬레이션이 실행 가능성을 검증하는 '제안–검증–결정' 흐름을 평가해, 시험 사례 18건 중 자율 전략 성공 3/10, 잘못된 입력 거부 7/8, 최종 검토 도달 4건 모두 통과, 시뮬레이션 검증 평균 164.39초를 보고했다. | ref-759 | 아니오 | medium | 2026-09-24 | 병원 / 예외·성과 | — |
| f15 | [사실] | Liu 외(2026)는 사람 참여 산업 로봇을 위한 에이전트형 신경-기호 계획·시운전 프레임워크에서 언어 모델은 의도 해석과 문맥 추론에만 쓰고 검증·순서 결정·실행은 모두 결정론적으로 두며, 언어 모델이 낸 계획을 기호적으로 검증한 뒤 Unity3D 디지털 트윈에서 사람이 검토·수정·재검증하고 나서야 실제 로봇에 배포하는 방식으로 기준선 10종보다 높은 작업 성공률을 보고했다. | ref-674 | 아니오 | medium | 2026-06-06 | 완료·인계 | — |
| f16 | [사실] | 산업 제품 구성(Valerio 외), 병원 라인 작업 조정(Ko·Lin), 산업 로봇 시운전(Liu 외)의 서로 다른 세 연구가 모두 언어 모델을 해석 단계에 한정하고 제약 해결기·기호 검증·시뮬레이션 검증과 사람의 최종 검토를 거친 뒤에만 구성·계획을 채택하는 구조를 택했다. | ref-824, ref-759, ref-674 | 예 | medium | 2026-09-24 | 제약 | — |
| f17 | [사실] | Figat·Mackey·Ingham(2026)은 임무 수준 목표를 온톨로지 개념, 확률 시간 페트리 넷, 자원 모델링, 몬테카를로 시뮬레이션으로 하드웨어·소프트웨어 사양으로 바꾸는 RSTM2 방법론을 제안해 임무·시스템·하위 시스템 수준의 구조 대안 비교와 자원 배분을 다루며, 가상 사례 연구로만 검증하고 다중 로봇(NASA CADRE) 적용 가능성을 언급한다. | ref-828 | 아니오 | medium | 2026-02-05 | — | — |
| f18 | [사실] | Howard(Cal Poly 석사논문, 2026)는 작업자 피킹(picker-to-parts) 창고에서 협동 자율이동로봇 대수 산정을 처리량 최대화가 아닌 라인당 비용 최소화로 다시 정의하고 FlexSim 이산 사건 시뮬레이션 27,000회·반개방형 대기행렬·XGBoost 대리모델로 분석해, 최적 로봇 대 작업자 비율이 수요에 따라 1:1 에서 2.5:1 로 옮겨 가고 작업자 유휴 비용이 로봇 유휴 비용의 약 2.5배이며 처리량 기준 산정은 구독형 과금에서 대수를 과대 산정한다고 보고했다. | ref-829 | 아니오 | medium | 2026-06 | 물류창고 / 수행 자원 | — |
| f19 | [추정] | 국내 자율이동로봇 업체 폴라리스3D 는 공장에 맞는 로봇 대수를 정하려면 일일 목표 이송 횟수와 시간당 적재량, 출발지–목적지 평균 이동 거리·속도, 공정 수, MES·엘리베이터 등 기존 설비 연동 여부가 직접 영향을 주므로 도입 전 전문가 인터뷰나 시뮬레이션 사전 분석이 필수라고 밝힌다. | ref-830 | 아니오 | low | 2026-06-12 | 제조 공장 / 제약 | 벤더 주장 |
| f20 | [추정] | 대수 산정이 처리량·수요 밀도·이동 거리·작업자 비율 같은 현장 수치와 시뮬레이션에 달려 있다는 연구와 업체 설명을 보면, 채팅으로 로봇 구성에서 '몇 대'라는 값은 언어 모델이 대화만으로 정할 수 없고 35. 처리능력·규모·배치 설계와 34. 시뮬레이션·예측용 디지털 트윈의 산정 엔진을 불러 그 결과와 비용 목적(처리량 대 비용)을 사용자에게 되묻는 방식이어야 할 것으로 보인다. | ref-829, ref-830 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f21 | [사실] | 심현재 외(제어로봇시스템학회 국내학술대회, 2023)는 이기종 다중 로봇을 클라우드에서 운용하는 AGM(Adaptive Goal Management) 소프트웨어 플랫폼을 제시해 적응형 목표 실행 방식과 REST API 로 서로 다른 로봇을 등록·통신하고 작업을 배정하는 구조를 보고했다. | ref-825 | 아니오 | medium | 2023-06 | 수행 자원 | — |
| f22 | [추정] | 연계 대상: 로봇별 언어 모델이 ROS 2 기본 스킬에서 실행 코드를 만드는 일(CoMuRoS)과 스킬의 가치 함수로 현재 장면의 실행 가능성을 점수화하는 일(SayCan)은 분류 원문 19장의 로봇 자체 지능·제어 쪽이며, 10. 채팅으로 로봇 구성에서 ROP가 직접 맡을 것은 대화를 구조화 구성(종류·대수·장비·위치·역할)으로 바꾸고 온톨로지의 요구·제공 능력으로 적합성을 확인해 부족을 알린 뒤 사람이 승인한 구성만 확정하는 일로 보인다. | ref-677, ref-088, ref-229 | 아니오 | low | 2026-09-29 | — | — |
| f23 | [추정] | 자연어 설명에서 능력 온톨로지를 생성하는 방법(Vieira da Silva 외)과 언어 모델·제약 해결 결합 구성(Valerio 외)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 매뉴얼·설명서 해석의 적용 대상인 4. 이기종 로봇 등록과 5. 로봇 능력·작업 표현 페이지에도 함께 연결해야 한다. | ref-465, ref-824 | 아니오 | low | 2026-09-29 | — | — |
| f24 | [추정] | 온톨로지의 확정 지식으로 명확화 질문의 필요를 줄이는 연구와 잘못된 조정 요청 8건 중 7건을 검증 단계에서 거부한 연구를 함께 보면, 채팅 로봇 구성의 되묻기는 온톨로지·팩트시트로 알 수 없는 값(대수, 초기 위치, 역할 우선순위)에 한정하고 알 수 있는 값은 읽어 온 근거를 보여 주며, 수행 불가 판정은 어떤 요구 능력이 어느 로봇에도 없는지로 설명하는 것이 맞을 것으로 보인다. | ref-820, ref-759 | 아니오 | low | 2026-09-29 | 제약 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-677 | Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2511.22354 | 아니오 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.07962 | 아니오 |
| ref-820 | Nakajima, H., & Miura, J. (IROS 2024) | Combining Ontological Knowledge and Large Language Model for User-Friendly Service Robots | 2024-10-22 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.16804 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-229 | IDTA (Industrial Digital Twin Association, admin-shell-io GitHub) | IDTA 02020 Submodel Template Capability Description — README (published/Capability Description/1/0) | 미확인 | 표준 | medium | 2026-09-29 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-824 | Valerio, D., Kogler, P., Bischof, S., Hubauer, T., & Rangwala, H. | Neuro-symbolic AI for Industrial Configuration | 2026-09-24 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2609.29947 | 아니오 |
| ref-825 | 심현재, 무함마드 카짐, Michael Muldoon, 김광기 (제어로봇시스템학회 국내학술대회) | 클라우드 기반 이기종 다중로봇 운용 소프트웨어 플랫폼 연구 | 2023-06 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11480590 | 아니오 |
| ref-088 | Ahn, M., Brohan, A., Brown, N., Chebotar, Y. 외 (Google/Everyday Robots) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2204.01691 | 아니오 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026) | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 2026-06-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.02167 | 아니오 |
| ref-828 | Figat, M., Mackey, R. M., & Ingham, M. D. | Ontology-Driven Robotic Specification Synthesis | 2026-02-05 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2602.05456 | 아니오 |
| ref-829 | Howard, T. L. (California Polytechnic State University, 석사논문) | A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities | 2026-06 | 논문 | medium | 2026-09-29 | https://digitalcommons.calpoly.edu/theses/3387/ | 아니오 |
| ref-830 | 폴라리스3D(Polaris3D) | AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기 | 2026-06-12 | 벤더 문서 | low | 2026-09-29 | https://polaris3d.com/blog/trends/amr-roi-calculator/ | 아니오 |
| ref-759 | Ko, T.-H., & Lin, C.-T. | Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin | 2026-09-24 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2609.29061 | 아니오 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L. | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 2026-06-06 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.08214 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-29 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f16(언어 모델 출력은 검증·사람 검토 뒤에만 채택), f18·f20(대수는 현장 수치·시뮬레이션에 달림), f3(역할·능력은 기계가 읽는 목록이어야 함) / 섹션 4: f1(연합 형성), f4(어포던스), f7(요구·제공 능력과 제약), f10(팩트시트), f11(플릿 설정·task_capabilities), f13(구성 코파일럿) / 섹션 5: 병원 — f14(가상 멸균공급실 라인의 자연어 작업 조정, 시뮬레이션임을 명시), 물류창고 — f18(피킹 창고 대수 산정 비율), 제조 공장 — f19(벤더 주장 병기, 대수 산정 입력) / 섹션 6: f1·f2(언어 모델 팀 구성·역할 배정), f4·f5(어포던스·온톨로지로 실행 가능성 접지), f6(자연어→능력 온톨로지), f8·f9(능력 모델→계획으로 적합성 확인), f13·f15·f16(제약 해결·기호 검증·디지털 트윈 검토), f17(요구→사양 합성), f24(되묻기 범위) / 섹션 7: f10(VDA 5050 팩트시트), f7(IDTA 02020), f11(Open-RMF 플릿 설정), f12(구조화 결과물) / 섹션 8: f1, f2, f4, f5, f6, f8, f13, f14, f15, f17, f18, 국내 f21 / 섹션 9: f22(연계 대상: 로봇별 코드 생성·어포던스 점수화는 로봇 자체 지능·제어; 직접 범위: 대화→구조화 구성·적합성 확인·승인) / 섹션 10: 5. 로봇 능력·작업 표현(f7·f9, 원문 주석의 짝), 4. 이기종 로봇 등록(f10·f12·f21), 25. 작업 배정 — MRTA(f1·f2), 35. 처리능력·규모·배치 설계와 34. 시뮬레이션·예측용 디지털 트윈(f18·f20), 9. 채팅으로 시나리오 구성(f9 요구 능력의 출처), 13. 대화형 기능의 신뢰·기반(f16·f24), 20. 로봇·제조사 관제 연동(f11), 21. 상호운용 표준·적합성(f10), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f23, 교차 규칙) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 5. 로봇 능력·작업 표현 페이지에 f7·f8 반영, 4. 이기종 로봇 등록 페이지에 f6·f10 반영, 35. 처리능력·규모·배치 설계 페이지에 f18 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 연합 형성 | Coalition Formation | 하나의 하위 작업을 맡을 로봇 팀을 각 로봇의 능력과 제약에 맞춰 고르는 다중 로봇 계획 단계이다. |
| 어포던스 | Affordance | 현재 환경과 로봇 상태에서 어떤 스킬을 실제로 실행할 수 있는지를 나타내는 값으로, 언어 모델의 제안을 실행 가능한 행동에 접지하는 데 쓴다. |
| 능력 기술 서브모델 | Capability Description Submodel (IDTA 02020) | 자산관리셸에서 요구 능력과 제공 능력을 속성·제약·스킬과 함께 적어 자원 능력 매칭에 쓰는 IDTA 서브모델 템플릿이다. |
| 구성 코파일럿 | Configuration Copilot | 자연어 요구를 제약으로 형식화하고 제약 해결기로 유효한 구성을 찾아 자연어로 돌려주는 대화형 구성 보조 도구이다. |

## 열린 질문

새로 생긴 질문:

- 대화로 로봇 종류·대수·장비·역할을 정하고 수행 가능 여부를 판정하는 기능을 평가할 공개 벤치마크나 지표(적합성 판정 정확도, 질문 횟수, 구성 완료 시간)가 있는가? | 관련 영역: 10. 채팅으로 로봇 구성, 13. 대화형 기능의 신뢰·기반 | 근거: f14 | 종류: 일반
- 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? | 관련 영역: 10. 채팅으로 로봇 구성, 4. 이기종 로봇 등록, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반
- 채팅으로 정한 로봇 대수를 시뮬레이션 기반 대수 산정과 어떻게 연결하고, 처리량 최대화와 비용 최소화 가운데 어느 목적을 누가 정하는가? | 관련 영역: 10. 채팅으로 로봇 구성, 35. 처리능력·규모·배치 설계, 3. 경제성·조달·사업 모델 | 근거: f20 | 종류: 일반
- 로봇 구성이 시나리오 요구를 채우지 못할 때 부족한 능력·대수를 사용자에게 어떤 형식(요구 능력별 매칭 결과, 불능 제약 집합 등)으로 설명해야 이해와 수정이 쉬운가? | 관련 영역: 10. 채팅으로 로봇 구성, 5. 로봇 능력·작업 표현 | 근거: f9 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f1 SMART-LLM 이 로봇 스킬 집합을 프롬프트에 주는 구체 형식은 초록에서 확인하지 못함(본문 미열람)
    - f5 Nakajima·Miura 의 정량 결과는 초록에 없어 미확인
    - f10 VDA 5050 팩트시트가 '계획·규모 산정·시뮬레이션'에 쓰인다는 문구는 검색 요약에만 있어 finding 에 넣지 않음
    - f19 폴라리스3D 대수 산정 입력은 벤더 주장이며 독립 출처 교차 확인 없음
    - f16 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f7·f10·f11 발행일 미확인(공식 저장소 문서)
    - ACMG(MDPI Applied Sciences, 자연어→CSP 모델 생성)와 Järvenpää 외 능력 매칭 의미 규칙 논문(Taylor & Francis)은 403 으로 열지 못해 넣지 않음
    - Springer '유통센터 AMR 플릿 규모 산정 시뮬레이션' 장은 인증 리다이렉트로 열지 못해 넣지 않음
    - 국내 언어 모델 기반 로봇 구성 대화 연구는 검색에서 확인되지 않음(국내 자료는 이기종 플랫폼 논문과 벤더 대수 산정 설명뿐)
    - 대화만으로 로봇 구성을 정한 실제 현장 배치 사례는 찾지 못함(가상 라인·실험실·시뮬레이션 사례뿐)
- 범위 경계 위반 의심:
    - f22: 로봇별 코드 생성·어포던스 점수화는 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f8·f9: 제조 설비 배치의 계획 가능성 확인 연구는 설비 제어가 아니라 능력 모델 활용 방법으로만 제안함
    - f13: 산업 제품 구성(비로봇) 연구는 방법 참고로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-677~ref-674, 예약 구간 안) 상한 도달로 REBEL(다중 사람–로봇 초기 작업 배정), IDTA 02047 AGV 기술 데이터 서브모델, LLM 다중 로봇 서베이(arXiv 2502.03814)는 원문을 열었으나 넣지 못했다. 원문 열람 16건(webfetch 12, github_raw 4: fleet_adapter_template config, IDTA 02020 README, VDA5050_EN.md 재사용 ref-031). 교차 확인 1건(f16: 서로 다른 세 연구 그룹). 논문은 모두 arXiv·DBpia·학위논문 초록 페이지 확인이라 신뢰도 medium 이하. 분류 원문 핵심 질문(어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가)에는 f1·f2(언어 모델로 팀 구성·역할 배정 가능), f7·f8·f9(요구·제공 능력 매칭과 계획 생성으로 적합성 확인 가능), f18·f20(대수는 시뮬레이션 산정 필요), f16(검증·승인 뒤에만 확정)으로 답했으며 결론은 '종류·역할·적합성은 온톨로지·능력 모델로 대화 안에서 확인 가능하나 대수와 초기 위치는 별도 산정·사람 확인이 필요'라는 추정(f12·f20·f22·f24)이다. 현장 유형: 병원(f14, 가상 라인임을 명시), 물류창고(f18), 제조 공장(f19, 벤더 주장)으로 실외·상업 시설·가정 사례는 없다. L. AI·학습 기술 관련 finding(f6·f13·f23)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 4. 이기종 로봇 등록·5. 로봇 능력·작업 표현 양쪽에 연결하도록 제안했다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 817건과의 URL 중복을 대조하지 못했으므로 SayCan·IDTA 02020·fleet_adapter_template 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 능력 매칭·요구 능력·제공 능력·팩트시트·플릿 어댑터는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

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

### runs/2026-09-25-27/research.md

```markdown
# 리서치 브리프 2026-09-25-27

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-27 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 클라우드·포그·엣지, 가용성·분할 내성(CAP), 서비스 품질(QoS), 베이스·호라이즌 용어 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 열린 질문 중 이 영역에 직접 걸린 것 없음(2026-09-25-24 브리프가 제안한 시각 동기화 질문은 게시 전)
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
2. 로봇 관제 표준·미들웨어(VDA 5050, ROS 2의 DDS·Zenoh, Open-RMF)는 연결 끊김, 손실이 있는 무선망, 여러 기계·네트워크에 걸친 분산 배치를 어떻게 다루는가? (섹션 6·7 겨냥)
3. 클라우드·포그(fog)·엣지·로봇 사이에서 계산을 나누는 기준은 무엇이고, 로봇 작업을 클라우드로 넘긴 연구는 지연·성능에 대해 무엇을 보고하는가? (섹션 4·6·8 겨냥)
4. 엣지 플랫폼은 클라우드와 끊긴 동안 무엇을 유지하고 재연결 뒤 어떻게 맞추며, 분산 시스템 이론(CAP)은 이 선택에 어떤 제약을 주는가? (섹션 4·6 겨냥)
5. 물류센터 무선망(와이파이·5G 특화망 이음5G)의 지연·가용성 요구와 국내 적용 사례는 무엇인가? (섹션 3·5·8 겨냥, 국내 자료 우선)
6. 관제 서버의 가용성(이중화)과 여러 거점을 함께 운영하는 구성은 어떤 방식이 공개되어 있는가? (섹션 6·9 겨냥)
7. 통신·컴퓨팅 구조에서 ROP가 직접 맡을 부분과 무선망 구축·로봇 로컬 주행처럼 외부에 맡길 부분의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 명세는 이동로봇이 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된(released) 노드까지 주문을 수행하며, 해제되지 않은 호라이즌(horizon) 구간은 주행하지 않도록 정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 명세는 통신이 연결 실패와 메시지 손실을 고려한 무선망에서 이루어진다고 전제하고, order·instantActions·state 등 대부분 토픽에 MQTT QoS 0(최선 노력), connection 토픽에만 QoS 1을 쓰며, 연결 시 브로커가 단절을 대신 알리는 last will 메시지를 등록하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f3 | [추정] | 이번에 연 VDA 5050 명세에서는 브로커 위치, 허용 지연, 대역폭, 무선랜 요건, 메시지 크기 상한에 대한 규정을 찾지 못했다. | ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |
| f4 | [사실] | ROS 2 설계 문서는 ROS 2가 DDS를 채택해 ROS 1의 중앙 마스터 없이 완전 분산 방식으로 참여자를 발견하게 했고, 이로써 마스터라는 단일 장애점을 없앴다고 설명한다. | ref-468 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | ROS 2 QoS 설계 문서는 저가 로봇의 불안정한 무선망을 배경으로 이력(history)·깊이(depth)·신뢰성(최선 노력/신뢰)·지속성(transient local/volatile) 정책을 두고, 센서 데이터에는 완전성보다 적시성을 우선해 최선 노력과 작은 큐를, 서비스·파라미터에는 신뢰 전송을 쓰는 프로파일을 제시한다. | ref-469 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f6 | [사실] | ROS 2 미들웨어 구현 rmw_zenoh는 기본적으로 Zenoh 라우터를 거쳐 가십(gossip)으로 발견 정보를 주고받고 멀티캐스트 발견은 꺼 두며, 서로 다른 호스트를 잇려면 한쪽 라우터가 다른 라우터의 엔드포인트에 연결하도록 설정한다. | ref-470 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | Open-RMF free_fleet는 플릿 어댑터와 로봇 사이를 Zenoh로 잇고, 로봇마다 로봇 이름을 네임스페이스로 한 zenoh-bridge-ros2dds를 두며, Zenoh 라우터는 어댑터와 같은 네트워크에서 실행해 로봇 쪽과 관제 쪽 ROS 2 도메인을 분리한다. | ref-256 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF rmf-web의 API 서버는 ROS 2 기반 RMF와 웹 클라이언트 사이를 잇는 별도 서비스로, 플릿 어댑터가 API 서버 엔드포인트로 작업·로봇 상태를 보내며, 기본 설정에서는 비영속 내부 데이터베이스를 쓰고 설정 파일로 영속 저장소를 지정할 수 있다. | ref-473 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f9 | [사실] | KubeEdge는 클라우드 부분(CloudHub·EdgeController·DeviceController)과 엣지 부분(EdgeHub·Edged·MetaManager 등)으로 나뉘며, 클라우드–엣지 네트워크가 불안정하거나 엣지가 오프라인 상태에서 재시작되어도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하도록 설계되었다고 밝힌다. | ref-471 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f10 | [추정] | Azure IoT Edge 문서는 오프라인 동안 엣지 허브가 상위로 보낼 메시지를 재연결까지 저장하고 로컬 모듈·하위 장치를 인증해 현장 안 통신을 이어 가며, 메시지 보관 기본 수명은 7,200초이고 재연결 즉시 저장된 메시지를 보낸다고 설명한다. | ref-472 | 아니오 | low | 2026-03-02 | 예외·성과 | 벤더 주장 |
| f11 | [사실] | NIST SP 500-325는 포그 컴퓨팅을 클라우드와 말단 장치 사이에서 지연을 고려한 분산 애플리케이션을 지원하는 계층형 모델로 제시하고, 포그 노드가 논리적 위치와 통신 지연 비용을 알아 요청–응답 시간을 줄인다고 설명한다. | ref-474 | 아니오 | medium | 2018-03 | — | 원문 미열람 |
| f12 | [사실] | Kehoe 외(2015)는 클라우드가 로봇·자동화에 주는 이점을 빅데이터 접근, 온디맨드 병렬 계산, 로봇 간 집단 학습, 사람 계산(크라우드소싱) 네 가지로 정리했다. | ref-476 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f13 | [사실] | FogROS2 저자들은 ROS 2 노드를 클라우드·포그로 넘기는 이 플랫폼이 실험에서 SLAM 지연을 50% 줄이고 파지 계획 시간을 14초에서 1.2초로, 동작 계획을 45배 빠르게 했다고 보고했으며, 이를 위해 쿠버네티스 백엔드, UDP 기반 보안 통신, 영상 H.264 압축을 썼다. | ref-475 | 아니오 | medium | 2022-05 | 수행 자원 | 원문 미열람 |
| f14 | [사실] | 공장 내 물류용 인프라 기반 자율이동로봇 연구(arXiv 2512.15215)는 인프라 센싱·현장 내(on-premise) 클라우드 계산·로봇 탑재 자율성을 결합한 참조 구조를 제시하고, 계산 부하를 엣지로 넘기기 위해 무선 시간 민감 네트워크(wireless TSN)를 쓰는 방향을 전망했다. | ref-479 | 아니오 | medium | 2025-12 | 수행 자원 | 원문 미열람 |
| f15 | [사실] | Gilbert·Lynch(2002)는 비동기 네트워크 모델에서 분산 서비스가 일관성·가용성·분할 내성을 동시에 모두 만족할 수 없음을 증명해 Brewer의 추측(CAP)을 정리로 만들었다. | ref-481 | 아니오 | medium | 2002-06 | — | 원문 미열람 |
| f16 | [사실] | MQTT 5.0 표준은 연결 종료 뒤 세션 상태(미확인 QoS 1 메시지·구독)를 보존하는 세션 만료 간격, 발행 메시지의 수명인 메시지 만료 간격, 연결이 끊긴 뒤 유언 메시지 발행을 늦추는 유언 지연 간격, 여러 구독자에 메시지를 나누는 공유 구독을 둔다. | ref-477 | 아니오 | medium | 2019-03 | 예외·성과 | 원문 미열람 |
| f17 | [추정] | VDA 5050이 주문·상태에 재전송 없는 QoS 0을 쓰고 상태를 사건 발생 시와 최소 30초마다 다시 보내게 하므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 전달되리라 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신하는 구조가 필요할 것으로 보인다. | ref-031, ref-477 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f18 | [사실] | ETRI Journal 논문(2020)은 공장 자동화 같은 초저지연 서비스가 종단 간 10ms 미만 지연을 요구하며, 3GPP가 Release 15/16에서 모바일 엣지 컴퓨팅(MEC)을, Release 16/17에서 IEEE 802.1 시간 민감 네트워킹(TSN)과 연동하는 시간 민감 통신을 표준화하고 있다고 정리했다. | ref-482 | 아니오 | medium | 2020 | 제약 | 원문 미열람 |
| f19 | [추정] | CJ대한통운은 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G를 구축했다고 발표하면서 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들고, 무선 단말 시범 적용 뒤 로봇·설비·CCTV로 확대하겠다고 밝혔으며 와이파이 대비 약 1,000배 빠른 속도를 주장했다. | ref-478 | 아니오 | low | 2023-04 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | FreightWaves 기사가 전한 하이브리드 WMS 공급사(Synergy Logistics)의 조사 보고서는 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고, 절반 가까이가 소프트웨어·연결 중단으로 자동화 자산이 멈췄으며, 중단 비용이 시간당 5천~10만 달러라고 주장한다. | ref-480 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f21 | [추정] | MiR Fleet Enterprise 문서는 이 플릿 관리 소프트웨어가 선택적 이중화(redundancy)와 클라우드·가상 환경 배치를 지원한다고 소개한다. | ref-227 | 아니오 | low | 2025-01 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f22 | [추정] | 분류 원문의 질문(인터넷이 끊겨도 현장에서 어디까지 운영할 수 있는가)에 대해, 로봇은 이미 해제된 구간까지는 관제 없이도 수행하고(f1) 엣지 플랫폼은 오프라인 동안 현장 안 통신과 상위 전송 메시지 보관을 이어 가므로(f9·f10), 관제·브로커를 현장 서버에 두면 외부망 단절 중에도 이미 받은 주문과 현장 내 배정은 계속할 수 있으나, 클라우드 WMS의 새 주문 수신과 재고 확정은 멈추고 CAP 제약(f15)에 따라 단절 중 현장 기록과 WMS 기록을 재연결 후 맞추는 절차가 필요할 것으로 보인다. | ref-031, ref-471, ref-472, ref-481 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f23 | [추정] | 확인한 자료를 종합하면 역할 분담은 로봇 탑재부가 실시간 주행·회피를, 현장 서버(엣지·포그)가 지연에 민감한 배정·교통·설비 연동과 단절 중 운영 지속을, 클라우드가 대규모 계산·학습·분석·여러 거점 가시성을 맡는 층 구조로 정리될 것으로 보인다. | ref-474, ref-476, ref-475, ref-479, ref-480 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f24 | [추정] | 연계 대상: 무선망(와이파이·5G 특화망) 구축·운영과 로봇 로컬 주행·회피는 분류 원문 9장의 외부 연계 영역에 가깝고, ROP는 명령·상태 메시지의 통신 품질 요구, 연결 상태 감시(last will 등), 재연결 뒤 상태 재구성 절차를 맡는 것으로 보인다. | ref-031, ref-478 | 아니오 | low | 2026-09-25 | — | — |
| f25 | [추정] | rmw_zenoh의 라우터 간 연결(f6), free_fleet의 로봇별 Zenoh 브리지(f7), 별도 기계에 둘 수 있는 rmf-web API 서버(f8)를 보면 오픈소스 스택만으로도 거점마다 현장 코어를 두고 라우터·API로 중앙에 모으는 다거점 구성이 가능해 보이나, 이번 조사에서 Open-RMF 다거점 운영의 공개 사례는 찾지 못했다. | ref-470, ref-256, ref-473 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/free_fleet | 아니오 |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 2025-01 | 벤더 문서 | low | 2026-09-25 | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 | 예 |
| ref-468 | ROS 2 Design | ROS on DDS | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/ros_on_dds.html | 아니오 |
| ref-469 | ROS 2 Design | ROS 2 Quality of Service policies | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/qos.html | 아니오 |
| ref-470 | ROS 2 (ros2/rmw_zenoh GitHub) | rmw_zenoh — README (A ROS 2 RMW implementation based on Zenoh) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/ros2/rmw_zenoh | 아니오 |
| ref-471 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/kubeedge/kubeedge | 아니오 |
| ref-472 | Microsoft | Operate Azure IoT Edge devices offline | 2026-03-02 | 벤더 문서 | medium | 2026-09-25 | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities | 아니오 |
| ref-473 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-474 | NIST | NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model | 2018-03 | 정부·연구기관 | medium | 2026-09-25 | https://csrc.nist.gov/pubs/sp/500/325/final | 예 |
| ref-475 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2205.09778 | 예 |
| ref-476 | Kehoe, B., Patil, S., Abbeel, P., & Goldberg, K. | A Survey of Research on Cloud Robotics and Automation | 2015 | 논문 | medium | 2026-09-25 | https://escholarship.org/uc/item/3t04p9m1 | 예 |
| ref-477 | OASIS | MQTT Version 5.0 | 2019-03 | 표준 | medium | 2026-09-25 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 예 |
| ref-478 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 2023-04 | 벤더 문서 | low | 2026-09-25 | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 | 예 |
| ref-479 | arXiv 2512.15215 저자(미확인) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.15215 | 예 |
| ref-480 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 미확인 | 기사 | low | 2026-09-25 | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms | 예 |
| ref-481 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 2002-06 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/564585.564601 | 예 |
| ref-482 | ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행) | Ultra-low-latency services in 5G systems: A perspective from 3GPP standards | 2020 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f20(연결 중단으로 자동화 자산 정지, 조사 주장), f19(국내 와이파이 간섭 문제), f22(SCM 질문) / 섹션 4: f11(포그 컴퓨팅), f15(CAP), f5(QoS), f1(베이스·호라이즌), f16(MQTT 세션·메시지 만료·유언) / 섹션 5: 피킹 중 외부망 단절 시 운영 범위 f22(예외·성과), 적치 이동 중 브로커 단절 f1·f17(예외·성과), 무선망 품질 제약 f2·f18(제약) / 섹션 6: f4·f6·f7(분산 발견·라우터·브리지), f9·f10(엣지 오프라인 운영), f13(클라우드 오프로딩), f14(현장 내 클라우드 참조 구조), f21(관제 서버 이중화, 벤더 주장), f23(층별 역할 분담), f25(다거점 구성) / 섹션 7: VDA 5050(f1·f2·f3), ROS 2 DDS·QoS(f4·f5), rmw_zenoh(f6), Open-RMF free_fleet·rmf-web(f7·f8), KubeEdge(f9), MQTT 5.0(f16), NIST SP 500-325(f11), 3GPP MEC·TSC(f18) / 섹션 8: f12, f13, f14, f15, 국내 f18·f19 / 섹션 9: f24(연계 대상: 무선망·로컬 주행), f22·f23(직접 범위) / 섹션 10: 9. 로봇·제조사 관제 연동(f1·f2·f7), 12. 명령·작업 실행의 신뢰성(f1·f17 재연결·재전송), 8. 실시간 세계 상태·데이터 일관성(f17 상태 재구성, 2026-09-25-24 f9·f10), 1. 주문·업무 시스템 연계(f20·f22 WMS 단절), 20. 예외 복구·재계획·업무 연속성(f22), 26. 사이버보안·접근권한·개인정보(ref-009 DDS-Security, f13 보안 통신), 3. 처리능력·거점·설비 계획(f25 다거점), 27. AI·학습·적응과 모델 운영(f12 집단 학습, f13 계산 오프로딩) / 섹션 11: open_questions_new 3건. 다음 실행 후보: 12. 명령·작업 실행의 신뢰성 페이지에 f1·f17 반영 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 포그 컴퓨팅 | Fog Computing | 클라우드와 말단 장치 사이에 계산·저장·네트워크 자원을 계층으로 두어 지연에 민감한 분산 애플리케이션을 현장 가까이에서 처리하게 하는 컴퓨팅 모델이다. |
| CAP 정리 | CAP Theorem | 네트워크 분할이 일어날 수 있는 분산 서비스는 일관성과 가용성을 동시에 완전히 보장할 수 없다는 정리이다. |
| 5G 특화망(이음5G) | Private 5G Network (e-Um 5G) | 이동통신사가 아닌 기업·기관이 건물·공장 같은 특정 구역 단위로 5G 주파수를 할당받아 직접 구축해 쓰는 국내 5G 통신망이다. |
| 베이스·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 관제가 이미 해제해 로봇이 주행해도 되는 경로(베이스)와 계획만 되어 있고 아직 해제되지 않은 경로(호라이즌)를 구분하는 개념이다. |

## 열린 질문

새로 생긴 질문:

- 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? | 관련 영역: 11. 분산 시스템·통신·컴퓨팅 구조, 1. 주문·업무 시스템 연계, 20. 예외 복구·재계획·업무 연속성 | 근거: f22 | 종류: 일반
- 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? | 관련 영역: 11. 분산 시스템·통신·컴퓨팅 구조, 9. 로봇·제조사 관제 연동 | 근거: f3 | 종류: 일반
- 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? | 관련 영역: 11. 분산 시스템·통신·컴퓨팅 구조, 3. 처리능력·거점·설비 계획 | 근거: f25 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 21회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·프로젝트마다 발행 주체 한 곳의 자료
    - f3 은 열람 도구 응답 기준의 부재 관찰이며 VDA 5050 명세 전문 대조 아님
    - f11·f12·f13·f14·f15·f16·f18·f19·f20·f21 원문 미열람(검색 요약 범위)
    - f13 수치(SLAM 지연 50%, 14초→1.2초, 45배)는 저자 보고값이며 실험 조건 미확인
    - f19 '1,000배' 속도는 벤더 주장이며 독립 측정 없음, 로봇 적용 결과 미확인
    - f20 조사 수치는 하이브리드 WMS 판매사 보고서로 표본·방법 미확인, 기사 발행일 미확인
    - f21 이중화 방식(능동·대기 등) 미확인
    - ref-479 저자·ref-482 전체 저자 목록 미확인
    - Tanwani 외 포그 로보틱스 논문, 3GPP TS 22.104 AGV 요구값, MiR HoST 무정지 서버는 확인했으나 신규 출처 상한으로 넣지 않음
- 범위 경계 위반 의심:
    - f24: 무선망 구축·로컬 주행은 분류 원문 9장 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f13·f14: 로봇 인식·계획 계산을 클라우드로 넘기는 연구는 로봇 자체 지능 영역을 포함하므로 계산 배치 선례로만 제안함
    - f19: 무선망 인프라 사례이며 ROP 직접 범위로 서술하지 않도록 수행 자원(통신 기반) 사례로만 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문 8건을 열었다: 재사용 ref-031(VDA 5050 명세)·ref-256(free_fleet README), 신규 ref-468(ROS on DDS)·ref-469(ROS 2 QoS 설계)·ref-470(rmw_zenoh)·ref-471(KubeEdge)·ref-472(Azure IoT Edge 오프라인 문서, MicrosoftDocs 저장소)·ref-473(rmf-web). FogROS2 README 경로는 404 라 논문 검색 요약만 썼다. 나머지 신규 8건과 재사용 ref-227 은 원문 미열람이며 신뢰도 상한 medium. finding 신뢰도는 모두 medium 이하, 교차 확인 0건. 검색 21회/30, 신규 출처 15건/15(ref-468~ref-482, 예약 구간 안)로 신규 출처 상한에 도달했다. 이전 실행 2026-09-25-24 의 ref-378~ref-392(ROS 2 QoS 문서·Sparkplug 등)는 참고문헌 목록에 없어 id 충돌을 피하려고 재사용하지 않았다. 분류 원문 SCM 질문은 f22 로 답했으나 물류센터의 공개 운영 기준이 없어 추정이다. 한국 자료: CJ대한통운 이음5G 보도자료(벤더 주장)와 ETRI Journal 논문을 넣었고, 국내 학술 자료 가운데 물류 로봇 관제의 네트워크 단절 운영을 다룬 연구는 찾지 못했다. KubeEdge 의 DeviceTwin 명칭은 22. 시뮬레이션·예측용 디지털 트윈과 무관한 장치 상태 동기화 모듈이라 섞지 않았다. 27. AI·학습·적응과 모델 운영 관련은 f12(집단 학습)·f13(계산 오프로딩) 연결만 섹션 10 제안에 두었다. 정정 요청 없음, 입력 누락 없음.
```
