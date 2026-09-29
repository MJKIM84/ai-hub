(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-04
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 9. 채팅으로 시나리오 구성 (C. 채팅 기반 구성·운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-839
- 새 출처 id 구간: ref-839 ~ ref-868 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-839 부터 순서대로 쓰고 ref-868 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-04/target.json

```json
{
  "run_id": "2026-09-29-04",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 96,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 9,
    "area_name": "9. 채팅으로 시나리오 구성",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=9"
}
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md

```markdown
---
title: "9. 채팅으로 시나리오 구성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 9
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 9. 채팅으로 시나리오 구성

# 9. 채팅으로 시나리오 구성

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

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]

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

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 838건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 215개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- event-trace: 사건 트레이스 (Event Trace)
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

### docs/open-questions.md (요약: 대상 영역 [9] 에 걸린 0건 / 전체 134건)

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

### runs/2026-09-29-03/research.md

```markdown
# 리서치 브리프 2026-09-29-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-03 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 11. 채팅으로 실제 상황 시뮬레이션 재현 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 자동 시뮬레이션 모델 생성·사건 트레이스·시나리오 재구성·로그 재생(rosbag)·조건부 검증 용어 없음(디지털 트윈·이산 사건 시뮬레이션·현실 격차·시뮬레이션 V&V 는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 짝 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
2. 자연어 대화나 텍스트 설명에서 실행 가능한 시뮬레이션 모델·시나리오를 만드는 연구는 무엇이 있고, 정확도와 한계는 어떻게 보고되는가? (섹션 3·6·8 겨냥)
3. 운영 기록(이벤트 로그·로봇 통신 기록)을 지정해 시뮬레이션을 자동으로 만들거나 재생하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)
4. 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 어떤 방법으로 비교하고, 맞지 않는 부분을 어떻게 찾아내는가? (섹션 4·6 겨냥)
5. 대화로 로봇 수·경로·정책 같은 조건을 바꿔 다시 돌리고 결과 차이를 설명하는 언어 모델 에이전트 방식은 무엇이며 무엇을 검증해야 하는가? (섹션 6·8·11 겨냥, 13. 대화형 기능의 신뢰·기반 연결)
6. 병원·제조 공장·물류창고·실외 등 현장 유형별로 실제 상황을 시뮬레이션에 재현하거나 조건을 바꿔 비교한 사례(국내 자료 포함)는 무엇인가? (섹션 5 겨냥)
7. 실제 상황 재현에서 ROP가 직접 맡을 것(기록→시나리오 변환, 대화, 비교·설명)과 시뮬레이션 엔진·로봇 자체 기록 재생처럼 외부에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Elbasheer 외(2025, Journal of Intelligent Manufacturing)는 대규모 언어 모델과 자동 시뮬레이션 모델 생성(ASMG)을 결합해 자연어 대화에서 실행 가능한 제조 시스템 시뮬레이션 모델을 직접 만드는 방법을 제안했고, 의도 표현→템플릿 기반 지식 추출→객체지향 데이터 기반 구성요소로 모델 구성→실행·결과 분석의 4단계로 18개 동작 유형을 지원하며 응답 시간이 단순 동작 8초에서 전체 시스템 생성 5분까지라고 보고했다. | ref-836 | 아니오 | medium | 2025-11-14 | — | 원문 미열람 |
| f2 | [사실] | Kleiman 외(2025)의 Simulation Agent 프레임워크는 시뮬레이션이 언어 모델의 답을 실제 시스템의 구조적 표현에 접지시키고, 언어 모델은 비전문가가 복잡한 시뮬레이터를 대화로 다루게 하는 인터페이스가 되는 결합 구조를 제안하며 초록에는 정량 평가가 없다. | ref-824 | 아니오 | medium | 2025-05-19 | — | — |
| f3 | [사실] | Xia 외(2026)는 언어 모델 에이전트들이 사용자 질의와 기준 구성에서 구조화 과제 표현을 만들고 실험을 설계해 매개변수 구성을 나란히 시뮬레이션한 뒤 결과를 해석해 권고를 내는 다중 에이전트 프레임워크를 제약 공정 설계에 적용했고, 언어만 쓰는 방식보다 출력 구체성과 사용자 평가 정확도·유용성이 높았다고 절제 실험과 사례로 보고했다. | ref-832 | 아니오 | medium | 2026-08-22 | — | — |
| f4 | [추정] | 대화로 모델을 만드는 연구(f1), 시뮬레이션으로 언어 모델을 접지하는 구조(f2), 에이전트가 구성을 바꿔 비교 실험을 돌리는 연구(f3)를 함께 보면, 이 영역의 '대화로 조건 바꿔 비교'는 언어 모델이 시뮬레이터의 매개변수(로봇 수·경로·정책)를 바꿔 실행하고 결과 차이를 설명하는 에이전트 구조로 구현되며 결론은 언어 모델의 추론이 아니라 시뮬레이션 출력에 근거해야 할 것으로 보인다. | ref-836, ref-824, ref-832 | 아니오 | low | 2026-09-29 | 예외·성과 | — |
| f5 | [사실] | Chen 외(2026)는 자연어 환경 사양에서 DEVS 형식의 이산 사건 시뮬레이터를 생성하되 구성요소 상호작용의 구조 추론과 구성요소별 사건·타이밍 논리 생성을 단계로 나누고, 생성된 시뮬레이터가 내는 구조화 사건 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 벤치마크를 제안했다. | ref-825 | 아니오 | medium | 2026-03-04 | — | — |
| f6 | [사실] | Camargo·Dumas·González-Rojas(Simod, 2020)는 정보시스템 이벤트 로그에서 프로세스 모델을 자동 발견하고 시뮬레이션 매개변수를 추출해 업무 프로세스 시뮬레이션 모델을 만들되, 하이퍼파라미터 최적화로 시뮬레이션 행동과 로그에서 관측된 행동의 유사도를 최대화하는 방법을 도구로 구현하고 여러 도메인 로그로 평가했다. | ref-828 | 아니오 | medium | 2020 | — | — |
| f7 | [추정] | 로그에서 시뮬레이션 모델을 발견하고 로그와의 유사도로 조정하는 방법(f6)과 생성된 시뮬레이터의 사건 트레이스를 제약과 대조하는 방법(f5)을 보면, 이 영역의 '운영 기록을 지정하면 재현'과 '재현 충실도 확인'은 기록에서 모델·매개변수를 뽑아 돌린 뒤 재현 트레이스와 실제 기록의 사건 순서·시각 유사도를 재는 흐름으로 구현할 수 있을 것으로 보인다. | ref-828, ref-825 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f8 | [사실] | Ghasemloo·Eckman·Li(2026)는 시뮬레이션 모델·디지털 트윈을 관측된 시스템 상태에서 반복 초기화하고 일부 확률 입력을 실제 관측값으로 고정한 채 나머지를 시뮬레이션해 조건부 출력 분포에 적합도 검정을 하는 '서브트레이스 조건부 검증'을 제안했고, 어느 입력 모델이 실제와의 불일치를 만드는지 진단하는 도구를 M/M/1 과 직렬 대기행렬 디지털 트윈 사례로 보였다. | ref-826 | 아니오 | medium | 2026-07-19 | — | — |
| f9 | [추정] | 서브트레이스 조건부 검증(f8)이 불일치의 원인이 되는 입력 모델을 진단하는 점을 보면, 이 영역의 '맞지 않는 부분을 알려 준다'는 기능은 도착·처리 시간·고장 같은 입력 모델 가운데 어느 것이 실제 기록과 어긋나는지를 통계 절차로 짚어 대화로 설명하는 방식으로 뒷받침될 수 있을 것으로 보인다. | ref-826 | 아니오 | low | 2026-09-29 | 예외·성과 | — |
| f10 | [사실] | rosbag2 는 ROS 2 시스템의 통신을 기록·재생하는 공식 도구로, ros2 bag record 로 토픽 메시지를 시각과 함께 저장하고 ros2 bag play 로 재생하며 재생 속도·시작 시점(seek)·토픽 선택·반복·/clock 토픽으로 시뮬레이션 시각 발행 같은 옵션을 두고 MCAP·SQLite3 저장 형식을 지원한다. | ref-831 | 아니오 | medium | 2026-09-29 | 작업 대상 | — |
| f11 | [추정] | 연계 대상: rosbag2 로 로봇 통신 기록을 재생하는 일은 로봇 한 대의 센서·제어 메시지를 되살려 로봇 자체 소프트웨어를 디버깅하는 로봇 자체 지능·제어 쪽 도구이며, 11. 채팅으로 실제 상황 시뮬레이션 재현이 다루는 재현은 플릿 수준 실행 기록(작업·배정·위치·사건 시각)을 시나리오로 바꿔 여러 로봇과 설비의 상황을 다시 돌리는 일이므로 두 층을 구분해야 할 것으로 보인다. | ref-831 | 아니오 | low | 2026-09-29 | — | — |
| f12 | [사실] | SoVAR(Guo 외, ASE 2024)는 대규모 언어 모델 프롬프트로 사고 보고서 텍스트에서 사고 정보를 추출하고 제약을 풀어 차량 궤적을 생성해 여러 지도 구조에 사고 시나리오를 재구성하는 도구로, NHTSA 사고 보고서로 Baidu Apollo 를 시험해 5종의 안전 위반을 찾았으며, 보고서 정보와 시뮬레이션 지도의 대응이 어렵고 기존 재구성 방법의 정보 추출 정확도가 제한적이라는 한계를 밝혔다. | ref-834 | 아니오 | medium | 2024-09-12 | 실외 / 시작 조건 | — |
| f13 | [사실] | OmniTester(Lu 외, 2024)는 멀티모달 언어 모델에 프롬프트 설계, SUMO 교통 시뮬레이터 연동, 검색 증강 생성과 자기 개선을 결합해 자율주행 시험 시나리오를 만들며, 실제 사고 보고서에서 추출한 새 시나리오를 재구성하고 생성 시나리오의 현실성·제어 가능성을 검증했다고 보고했다. | ref-835 | 아니오 | medium | 2024-09-10 | 실외 / 시작 조건 | — |
| f14 | [사실] | 서로 다른 두 연구 그룹(SoVAR, OmniTester)이 각각 언어 모델로 사고 보고서 텍스트에서 시나리오를 재구성해 시뮬레이터에서 재현하는 방법을 자율주행 시험에 적용했다고 보고해, 텍스트 기록에서 실제 상황을 시뮬레이션으로 재현하는 접근이 한 곳 이상에서 확인된다. | ref-834, ref-835 | 예 | medium | 2024-09 | 실외 | — |
| f15 | [사실] | Chat2Scenic(Gao 외, 2026)은 규정 문서를 대화형 인터페이스와 도메인 특화 언어 지식의 검색 증강 생성으로 반복 정제해 Scenic 시나리오로 바꾸며, 규정에서 뽑은 123개 시나리오에서 컴파일 성공 76.42%, 프레임워크 정확도 58.17%를 보고했다. | ref-833 | 아니오 | medium | 2026-07-15 | — | — |
| f16 | [추정] | 텍스트에서 시나리오를 재구성하는 세 연구(f12·f13·f15)가 정보 추출 정확도 제한, 지도 대응의 어려움, 58% 수준의 프레임워크 정확도를 보고하므로, 채팅으로 설명한 상황을 시뮬레이션에 재현한 결과는 언어 모델 출력 그대로 쓰지 말고 사람이 확인해야 하며, 실제 기록(위치·시각·사건)이 있으면 말로 한 설명보다 기록을 우선 입력으로 삼는 것이 맞을 것으로 보인다. | ref-834, ref-835, ref-833 | 아니오 | low | 2026-09-29 | 제약 | — |
| f17 | [사실] | BedreFlyt(Sieve 외, 오슬로대, 2025)는 병원 입원 병동의 환자 입원 흐름을 최적화 문제로 바꾸는 디지털 트윈으로, 실행 가능한 형식 모델·온톨로지·SMT 해결기를 결합하고 오케스트레이터 설정으로 평균·최악 자원 수요와 가용 자원 변동을 아우르는 what-if 시나리오를 만들어 병상 배정 문제에 적용했다. | ref-829 | 아니오 | medium | 2025-05-07 | 병원 / 수행 자원 | — |
| f18 | [사실] | 우지영·신효진·전창훈·박상찬(Electronics, 2025)은 감염병 환자가 도착했을 때 병원에서 일어나는 전 과정을 시뮬레이션하는 연합(federated) 디지털 트윈으로 간호사 추종 음압 이송 침대 로봇 여러 대를 동시에 운용하는 한국 병원 사례를 제시하고 시나리오 기반 시뮬레이션으로 시스템 성능을 검증했다. | ref-837 | 아니오 | medium | 2025-12-17 | 병원 / 시작 조건 | 원문 미열람 |
| f19 | [사실] | 이동건 외(성균관대·LG전자, 한국CDE학회 논문집 2021)는 자동물류시스템을 설계 단계에서 가상으로 검증하고 운영 단계에서 실시간 모니터링·분석하는 디지털트윈을 개발해 국내 제조업체의 AGV 자동물류시스템에 적용하고 진단·분석·예측·최적화의 실효성을 검증했다. | ref-830 | 아니오 | medium | 2021-12 | 제조 공장 / 예외·성과 | — |
| f20 | [사실] | Valiollahi 외(Scientific Reports, 2026)는 운송·조립 역할이 다른 이기종 로봇 플릿과 공정·공장 배치를 함께 모델링한 디지털 트윈 시뮬레이션으로 기존 공장(브라운필드)에서는 혼잡 때문에 플릿 확장 효과가 체감하고, 신규 공장(그린필드)에서는 배치·플릿 규모·역할 비율을 비교해 로봇당 생산성을 줄이지 않고 처리량을 최대 3.5배 높이는 구성을 찾았다고 보고했다. | ref-838 | 아니오 | medium | 2026-07-18 | 제조 공장 / 예외·성과 | 원문 미열람 |
| f21 | [사실] | Yang 외(2025)는 언어 모델을 디지털 트윈에 쓰는 연구를 기술(description)–예측(prediction)–처방(prescription) 프레임워크와 적용 단계별 분류로 정리하고, 정확한 모델링을 위한 데이터 부족·분석 비효율·물리–디지털 상호작용의 설명 부족을 과제로 꼽으며 자동 모델링·최적화를 보이는 기업 디지털 트윈 시스템을 제시했다. | ref-827 | 아니오 | medium | 2025-03-04 | — | — |
| f22 | [추정] | 자연어에서 시뮬레이션 모델을 만들거나(Elbasheer 외, Chen 외) 언어 모델 에이전트가 시뮬레이션 실험을 설계·해석하는(Xia 외) 연구는 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 이 영역 양쪽에 연결해야 한다. | ref-836, ref-825, ref-832 | 아니오 | low | 2026-09-29 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 11. 채팅으로 실제 상황 시뮬레이션 재현에서 ROP가 직접 맡을 범위는 플릿 실행 기록을 시나리오 사양으로 바꾸고, 대화로 조건 변경을 받아 시뮬레이션 실행을 요청하며, 재현 트레이스를 실제 기록과 대조해 차이를 설명하고 사람이 확인하게 하는 일이고, 이산 사건·물리 시뮬레이션 엔진과 로봇 자체 통신 기록 재생은 연계 대상으로 두는 것이 맞을 것으로 보인다. | ref-825, ref-826, ref-831, ref-832 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f24 | [추정] | 국내 자동물류 디지털트윈 연구가 설계 단계의 가상 검증과 운영 단계의 실시간 모니터링을 구분하는 점(f19)을 보면, 실제 상황 재현은 과거 기록을 가정한 조건으로 다시 실행하는 일이므로 34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현 쪽에 두고, 18. 실시간 세계 상태·데이터 일관성은 재현에 쓰는 기록의 원천으로만 연결해야 원문의 '현재 상태 표현' 대 '가정한 미래 실험' 구분을 지킬 수 있을 것으로 보인다. | ref-830 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-824 | Kleiman, J., Frank, K., Voyles, J., & Campagna, S. | Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making | 2025-05-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.13761 | 아니오 |
| ref-825 | Chen, Z., Zhuang, H., Li, Z., & Li, C. | Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism | 2026-03-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2603.03784 | 아니오 |
| ref-826 | Ghasemloo, M., Eckman, D. J., & Li, Y. | Subtrace-Conditional Validation of Simulation Models and Digital Twins | 2026-07-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.17088 | 아니오 |
| ref-827 | Yang, L., Luo, S., Cheng, X., & Yu, L. | Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges | 2025-03-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2503.02167 | 아니오 |
| ref-828 | Camargo, M., Dumas, M., & González-Rojas, O. | Automated Discovery of Business Process Simulation Models from Event Logs | 2020 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1910.05404 | 아니오 |
| ref-829 | Sieve, R., Kobialka, P., Slaughter, L., Schlatte, R., Johnsen, E. B., & Tapia Tarifa, S. L. (University of Oslo) | BedreFlyt: Improving Patient Flows through Hospital Wards with Digital Twins | 2025-05-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.06287 | 아니오 |
| ref-830 | 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)) | 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 | 2021-12 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861 | 아니오 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/ros2/rosbag2 | 아니오 |
| ref-832 | Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P. | LLM Agents Perform Controlled Experiments Using Simulation Models | 2026-08-22 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2608.23622 | 아니오 |
| ref-833 | Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. | Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving | 2026-07-15 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.14387 | 아니오 |
| ref-834 | Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024) | SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing | 2024-09-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2409.08081 | 아니오 |
| ref-835 | Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S. | Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles | 2024-09-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2409.06450 | 아니오 |
| ref-836 | Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing) | Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems | 2025-11-14 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10845-025-02732-z | 예 |
| ref-837 | Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)) | Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins | 2025-12-17 | 논문 | medium | 2026-09-29 | https://www.mdpi.com/2079-9292/14/24/4954 | 예 |
| ref-838 | Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports) | Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts | 2026-07-18 | 논문 | medium | 2026-09-29 | https://www.nature.com/articles/s41598-026-57316-5 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f16(텍스트→시나리오 재현의 정확도 한계와 사람 확인 필요), f4(비교 결론은 시뮬레이션 출력에 근거), f21(데이터 부족·설명 부족 과제) / 섹션 4: f1(자동 시뮬레이션 모델 생성), f5(사건 트레이스), f12(시나리오 재구성), f10(bag 기록·재생), f8(서브트레이스 조건부 검증), f6(로그 기반 모델 발견) / 섹션 5: 병원 — f17(입원 흐름 what-if, 병상 배정), f18(국내 감염병 이송 로봇 연합 디지털 트윈, 시뮬레이션 검증임을 명시), 제조 공장 — f19(국내 AGV 자동물류 디지털트윈), f20(플릿·배치 시나리오 비교), 실외 — f12·f13(사고 보고서 재구성, 자율주행 시험 도구임을 명시) / 섹션 6: f1·f2·f3·f4(대화→모델 생성·에이전트 비교 실험), f5·f6·f7(사양·로그→시뮬레이터, 트레이스 대조), f8·f9(조건부 검증·불일치 진단), f12·f13·f14·f15·f16(텍스트→시나리오 재구성과 한계) / 섹션 7: f10·f11(rosbag2), f5(DEVS), f6(Simod), f13(SUMO), f15(Scenic) / 섹션 8: f1, f3, f5, f6, f8, f12, f13, f14, f17, f20, f21, 국내 f18·f19 / 섹션 9: f23(직접 범위: 기록→시나리오, 대화 조건 변경, 트레이스 대조·설명, 사람 확인; 연계: 시뮬레이션 엔진·로봇 통신 기록 재생), f11(연계 대상) / 섹션 10: 36. 가상 시운전·실제 상황 재현과 33. 시나리오 모델·편집(f22, 원문 주석의 짝), 34. 시뮬레이션·예측용 디지털 트윈과 18. 실시간 세계 상태·데이터 일관성(f24, 구분), 37. 관제 화면·실행 기록(f7 기록 원천), 38. 모니터링·이상 탐지·원인 분석(f9), 9. 채팅으로 시나리오 구성(f1·f5), 13. 대화형 기능의 신뢰·기반(f4·f16), 54. 시험·형식 검증·벤치마크(f8·f15), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f22, 교차 규칙), 63. 병원·의료·62. 제조 공장(f17~f20) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 36. 가상 시운전·실제 상황 재현 페이지에 f5·f8·f14 반영, 34. 시뮬레이션·예측용 디지털 트윈 페이지에 f20·f21 반영, 63. 병원·의료 페이지에 f18 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 자동 시뮬레이션 모델 생성 | Automatic Simulation Model Generation (ASMG) | 사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다. |
| 사건 트레이스 | Event Trace | 시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록으로, 재현 결과를 실제 기록이나 제약과 대조하는 데 쓴다. |
| 시나리오 재구성 | Scenario Reconstruction | 사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다. |
| 백 파일 | Bag File (rosbag2) | ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 나중에 재생해 로봇 소프트웨어를 실제 하드웨어 없이 시험·디버깅하는 데 쓴다. |

## 열린 질문

새로 생긴 질문:

- 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 37. 관제 화면·실행 기록, 33. 시나리오 모델·편집 | 근거: f7 | 종류: 일반
- 재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 36. 가상 시운전·실제 상황 재현, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반
- 대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 13. 대화형 기능의 신뢰·기반 | 근거: f4 | 종류: 일반
- 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 61. 물류창고, 63. 병원·의료 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 19회 · 신규 출처 15건
- 미확인 항목:
    - f1 Elbasheer 외 원문 미열람(Springer 인증 리다이렉트, d-nb.info PDF 는 텍스트 추출 실패) — Semantic Scholar API 초록만 사용, 시뮬레이션 도구·정확도 검증 방식 미확인
    - f18 우지영 외 원문 미열람(MDPI 403) — 초록만 사용, 시뮬레이션 도구·정량 결과·승강기 연동 여부 미확인, 저자 한글 표기 미확인
    - f20 Valiollahi 외 원문 미열람(Nature 인증 리다이렉트) — 초록만 사용, 실제 공장 데이터 대조 여부 미확인
    - f6 Simod 의 정량 결과(유사도 수치)는 초록에 없어 미확인
    - f12 SoVAR 의 재현 성공률 수치는 초록에 없어 미확인
    - f14 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f10 rosbag2 README 발행일 미확인
    - Frydenlund 외 'Modeler in a box'(Sage), MDPI 'Conversational Digital Twins' 프레임워크, ScienceDirect 'LLM-driven discrete-event simulation'(JMS), Webb·Tokhi·Alkan AMR 플릿 디지털 트윈(SSRN), Springer AS/RS 디지털 트윈 검증 논문, WSC 2022 창고 디지털 트윈 논문(PDF 텍스트 추출 실패)은 열지 못해 넣지 않음
    - 국내 언어 모델 기반 시뮬레이션 재현 연구는 검색에서 확인되지 않음(국내 자료는 AGV 자동물류 디지털트윈과 병원 이송 로봇 연합 디지털 트윈뿐)
    - 대화만으로 실제 상황을 시뮬레이션에 재현한 실제 현장 운영 사례는 찾지 못함(연구 프로토타입·자율주행 시험 도구·시나리오 검증 사례뿐)
- 범위 경계 위반 의심:
    - f11: rosbag2 로봇 통신 기록 재생은 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f12·f13·f14: 자율주행 시험용 사고 시나리오 재구성은 로봇 자체 지능 시험 도구이며 업종별 조건(실외 차량)에 걸치므로 텍스트→시나리오 재현 방법의 선례로만 제안함
    - f3: 제약 공정 설계(비로봇) 연구는 에이전트 비교 실험 방법 참고로만 제안함
    - f17: 병원 병상 배정 최적화는 ROP 직접 범위 밖의 업무 계획이므로 what-if 시나리오 구성 방식의 사례로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-824~ref-838, 예약 구간 안) 상한 도달로 Webb·Tokhi·Alkan 의 AMR 플릿 디지털 트윈 사고 대응 논문(검색 요약: 대리모델로 makespan 2~10% 단축), CALM-DT(언어 모델 자체를 디지털 트윈 시뮬레이터로 쓰는 연구), 병원 디지털 트윈 ML 검증 논문(arXiv 2303.04117)은 열었거나 확인했으나 넣지 못했다. 원문 열람 12건(webfetch 11, github_raw 1: rosbag2 README), 미열람 3건(ref-836·ref-837·ref-838, Semantic Scholar API 초록으로 기관·제목·발행일 확인). 교차 확인 1건(f14: SoVAR·OmniTester 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv·DBpia 초록 확인). 분류 원문 핵심 질문(대화만으로 실제 상황 재현·조건 비교)에는 f1·f2·f3(대화→모델 생성·에이전트 비교 실험 가능), f5·f6·f8(사양·로그→시뮬레이터, 트레이스 대조 검증), f12·f13·f14·f15(텍스트 기록→시나리오 재구성 가능하나 정확도 한계)로 답했으며 결론은 '대화·텍스트로 시나리오를 만들고 조건을 바꿔 비교하는 것은 가능하나 재현 정확도는 실제 기록 대조와 사람 확인이 필요하고 물류·병원 로봇 플릿에 적용한 사례는 없다'는 추정(f4·f7·f9·f16·f23)이다. 현장 유형: 병원(f17·f18, 시뮬레이션 검증임을 명시), 제조 공장(f19·f20), 실외(f12·f13·f14, 자율주행 시험 도구임을 명시)로 물류창고·상업 시설·가정 사례는 없다. L. AI·학습 기술 관련 finding(f1·f3·f5·f22)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 양쪽에 연결하도록 제안했고, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분은 f24 로 지켰다. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 823건과의 URL 중복을 대조하지 못했으므로 rosbag2·Simod 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 디지털 트윈·디지털 섀도·이산 사건 시뮬레이션·현실 격차·시뮬레이션 V&V·가상 시운전·프로세스 마이닝은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

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

### runs/2026-09-25-20/research.md

```markdown
# 리서치 브리프 2026-09-25-20

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-20 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 9. 로봇·제조사 관제 연동 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 플릿 어댑터 제어 수준, 관제(fleet control)·제조사 관제, 저수준·고수준 연동 구분 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안(2026-09-25-02: VDA 5050 팩트시트·상태 오류 보고, 3.0.0 발행, MassRobotics 메시지, Open-RMF 작업 능력·사용자 정의 동작) 미반영
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-001, oq-005, oq-007, oq-014, oq-020 연결 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [분류원문]
2. 제조사 관제와 연동하는 방식(로봇 직접 제어, 제조사 관제에 작업 위임, 상태만 수신)은 어떻게 구분되며 각 방식은 제조사 쪽에 어떤 API·기능을 요구하는가? (섹션 3·4·6 겨냥)
3. VDA 5050·MassRobotics·Open-RMF 는 명령·상태·오류·연결 단절을 어떤 메시지로 다루며, 어댑터가 변환해야 할 것은 무엇인가? (섹션 6·7, 트랙 반영 제안 겨냥)
4. 제조사 API·표준 프로토콜을 연결하는 공개 어댑터 구현(Open-RMF 어댑터, VDA 5050 커넥터)과 이종 플릿 통합 연구·사례에는 무엇이 있는가? (섹션 7·8 겨냥)
5. 국내 물류·서비스 현장에서 이기종 로봇 통합 관제는 어떤 방식으로 구현되고 있는가? (섹션 5·8, 한국 자료 우선)
6. 어댑터 계층에서 ROP가 직접 맡을 것과 로봇 자체 주행·제조사 관제에 맡길 것의 경계는 어디인가? (섹션 9 겨냥)
7. oq-005·oq-014·oq-020 과 관련해 VDA 5050 판 정보와 상태 매핑에 새 근거가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 문서는 플릿 어댑터를 RMF가 받는 제어 수준에 따라 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only)·인터페이스 없음(No Interface) 네 범주로 나누며, 전체 제어는 실시간 상태와 개별 로봇 경로의 전체 제어를, 신호등은 상태와 로봇별 일시정지·재개 제어를, 읽기 전용은 정기 상태 보고만을 RMF에 준다. | ref-004, ref-258 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | Open-RMF 의 전체 제어 어댑터는 제조사 관제(또는 로봇 API)가 로봇이 따를 명시적 경로를 지정할 수 있고 그 경로를 언제든 중단해 새 경로로 바꿀 수 있으며 이동 중 위치를 실시간으로 갱신해 주기를 요구한다. | ref-258 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f3 | [사실] | Open-RMF 플릿 어댑터는 제조사별 API를 RMF 교통 스케줄·협상 시스템의 인터페이스에 잇고, 로봇의 예상 이동 경로(itinerary)를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 한다. | ref-004 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | Open-RMF 통합 개요는 ROS 1·ROS 2 를 직접 쓰는 로봇, REST·XMLRPC 같은 공식 API를 제공하는 제조사 관제, SQL 데이터베이스 같은 다른 통신 수단을 모두 연동 경로로 들고, 어댑터를 하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리로 설명한다. | ref-259 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇·제조사 관제 API에 이동 명령(navigate: 목적지 좌표·지도 이름·선택 속도 제한), 정지(stop), 사용자 정의 동작 시작(start_activity), 위치([x, y, theta])·현재 지도 이름·배터리 충전 상태 조회, 명령 완료 확인(is_command_completed)을 요구하고, navigate·stop·execute_action 세 콜백을 RMF 명령 실행의 기본으로 둔다. | ref-153 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇별 상태 조회를 비동기 갱신 루프로 처리해 한 로봇의 상태 조회 오류가 다른 로봇의 상태 갱신을 막지 않게 한다. | ref-153 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 플릿 어댑터 템플릿 설정은 제조사 관제 접속 정보(주소·사용자·암호), RMF 지도 좌표와 로봇 지도 좌표의 대응점 목록(reference_coordinates), 속도·가속 한계와 차체 반경, 배터리 사양, 플릿이 수행할 수 있는 작업 유형(task_capabilities)을 플릿 단위로 적게 한다. | ref-105 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 로봇 상태 스키마는 로봇 상태 값을 uninitialized·offline·shutdown·idle·charging·working·error 일곱 가지로 두고, 운영자가 알아야 할 문제를 범주(category)와 자유 형식 상세(detail)로 된 issues 배열로 보고한다. | ref-148 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF 의 free_fleet 은 fleet_adapter_template 기반 Python 플릿 어댑터로, 제조사 관제를 거치지 않고 각 로봇의 Nav2(ROS 2 Jazzy)·Nav1(ROS 1 Noetic) 내비게이션 스택에 zenoh 통신 계층으로 직접 접속한다. | ref-264 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 커뮤니티 어댑터 목록은 MiR(MiR Fleet)·OTTO Motors·Clearpath·InOrbit 등 제조사·플랫폼별 플릿 어댑터와 KONE 등 승강기 어댑터, 문·기기 어댑터를 함께 모아 둔다. | ref-262 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | VDA 5050 은 서로 다른 제조사의 AGV·AMR 을 하나의 관제(fleet control, master control)로 운용하기 위한 제조사 중립 통신 인터페이스이다. | ref-031, ref-267 | 예 | medium | 2026-09-25 | — | — |
| f12 | [사실] | VDA 5050 3.0.0 은 MQTT(최소 3.1.1)와 JSON 을 쓰며, 관제→로봇 방향의 order·instantActions·zoneSet·responses 토픽과 로봇→관제 방향의 state·visualization·connection·factsheet 토픽을 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | VDA 5050 3.0.0 주문은 노드·엣지 그래프를 sequenceId 순서로 보내며 실행이 허용된 base 구간과 계획만 된 horizon 구간으로 나누고, orderId·orderUpdateId 로 주문 갱신을 추적한다. | ref-031 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f14 | [사실] | VDA 5050 3.0.0 에서 로봇은 받을 수 없는 주문을 상태 메시지의 오류로 거절하며, 거절 오류 유형에 VALIDATION_FAILURE·UNSUPPORTED_PARAMETER·INVALID_ORDER_ACTION·OUTDATED_ORDER_UPDATE·SAME_ORDER_UPDATE_ID·START_NODE_OUT_OF_RANGE·NO_ROUTE_TO_TARGET 등이 있다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f15 | [사실] | VDA 5050 3.0.0 의 connection 토픽은 ONLINE·CONNECTION_BROKEN·HIBERNATING 상태를 두고, 로봇이 연결할 때 CONNECTION_BROKEN 을 담은 MQTT 유언 메시지(last will)를 설정해 비정상 단절 시 브로커가 관제에 대신 알리게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f16 | [사실] | VDA 5050 3.0.0 상태 메시지는 현재 orderId·orderUpdateId, 마지막으로 지난 노드(lastNodeId·lastNodeSequenceId), action 진행 상태(actionStates: INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 등)를 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f17 | [사실] | VDA 5050 3.0.0 은 교통 관리 로직과 교통 조정 알고리즘·의사결정을 문서 범위에서 제외해, 교통 조정 방식은 관제 구현에 맡긴다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f18 | [사실] | VDA 5050 3.0.0 은 로봇이 적재 명세·지원 action 을 담은 팩트시트를 factsheet 토픽으로 관제에 알리게 하고, 사전 정의 action 으로 옮길 수 없는 동작은 제조사가 추가 action 을 정의해 관제가 쓰게 한다. | ref-031, ref-228 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f19 | [사실] | VDA 5050 공식 저장소 main 명세의 판 표기는 3.0.0 이며, VDA 는 3.0 판 발행을 보도자료로 알렸다(정확한 발행일은 기존 열린 질문 oq-005 의 출처 충돌로 남음). | ref-031, ref-032 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | MassRobotics AMR 상호운용 표준은 여러 제조사 AMR 이 같은 공간에서 위치·속도·방향·상태·작업 가용성 정보를 공유하게 하는 것을 목적으로 하며, 공식 JSON 스키마는 식별 보고(identityReport)와 상태 보고(statusReport) 두 메시지만 정의해 로봇에 명령을 보내는 메시지를 두지 않는다. | ref-261, ref-230 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f21 | [사실] | InOrbit 이 공개한 ros_amr_interop 저장소는 ROS 2 로봇을 MQTT 기반 VDA 5050 관제에 연결하는 VDA5050 커넥터와, ROS 2 데이터를 YAML 매핑으로 MassRobotics 상호운용 수신기에 보내는 송신 노드를 제공한다. | ref-263 | 아니오 | medium | 2026-09-25 | — | — |
| f22 | [의견] | Interact Analysis 는 다중 플릿 오케스트레이션을 제3자 관제가 로봇에 직접 접속해 제어하는 저수준 제어(Low-Level Control, 현재 가장 흔함)와 제3자 관제가 각 제조사 관제에 작업을 넘기는 고수준 제어(High Level Control, 늘어나는 중)로 나누고, 장기적으로 어느 쪽이 쓰일지는 아직 정해지지 않았다고 본다. | ref-265 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f23 | [사실] | ARM Institute 의 IO-AMRs 과제는 AMR 제조사마다 자체 플릿 관리 소프트웨어를 써서 여러 브랜드를 섞은 플릿 운영이 어렵다는 문제를 다루며, 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. | ref-266 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f24 | [사실] | Franke 외(2023)는 VDA 5050 이 AGV·관제 사이 인터페이스만 다루고 AGV·관제와 주변 설비(periphery) 사이 인터페이스는 다루지 않는다고 지적하고, 소프트웨어 공급사·하드웨어 제조사·사용자 워크숍으로 새 표준 인터페이스 요구를 정리했다. | ref-267 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f25 | [사실] | 2026년 ScienceDirect 게재 연구는 상용 다중 제조사 AMR 플릿과 천장 반송 차량(OHT)·바닥 AGV 사이의 작업 조정을 하나의 소프트웨어 정의 공장(Software-Defined Factory) 틀에 넣고 통신·위치추정·경로계획·작업 배정을 중앙 시스템이 다루는 이종 플릿 제어 시스템을 제안했다. | ref-268 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f26 | [사실] | Applied Sciences(2025) 사례 연구는 자동차 공장에서 여러 제조사 AGV·AMR 의 위치·상태 데이터를 하나의 지도와 웹 플랫폼으로 통합해 감시하는 플릿 관리 소프트웨어를 개발하고 작업 상태 갱신 평균 지연 120 ms 를 보고했으며, 향후 VDA 5050 통합을 고려한 구조를 두었다. | ref-136 | 아니오 | medium | 2025 | 예외·성과 | 원문 미열람 |
| f27 | [추정] | MiR 이 기존 RESTful 로봇 인터페이스를 MQTT 와 연결해 자사 AMR 과 타사 관제 사이에 VDA 5050 메시지를 주고받게 하는 어댑터 'MiR VDA 5050' 을 출시했다고 국내 전문지가 보도했다. | ref-269 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f28 | [추정] | 클로봇은 브랜드·이동 방식과 무관하게 이기종 로봇을 하나의 시스템처럼 관제한다는 클라우드 기반 플릿 관리 시스템(CROMS)을 제공한다고 밝힌다. | ref-270 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f29 | [추정] | 카카오모빌리티는 서비스 요청을 로봇 실행 단위로 추상화하는 Task, 이기종 로봇을 통합 표준 API 로 잇는 Command Interface, 장애 시 작업을 다른 로봇에 재배정하는 Reallocation, 건물 인프라·기존 시스템을 잇는 Integration Backbone 을 로봇 플랫폼 구성으로 발표했다. | ref-271 | 아니오 | low | 2026-05 | — | 원문 미열람, 벤더 주장 |
| f30 | [추정] | 노바테크가 현대자동차그룹 메타플랜트 아메리카에서 12종 약 300대의 이기종 물류 로봇을 자사 오케스트레이션 플랫폼 하나로 통합 운영한다고 보도됐다. | ref-272 | 아니오 | low | 2026-07-14 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f31 | [사실] | VDA 5050 3.0.0 의 사전 정의 action pick·drop 은 적재물이 로봇에 들어왔거나(pick) 떠났고(drop) 로봇이 새 적재 상태를 보고했을 때를 완료(FINISHED)로 정의해, 관제는 action 상태와 적재 상태로 운반 작업의 적재·하역 완료를 확인할 수 있다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f32 | [추정] | 출하 운반에서 상위 시스템의 운반 요청은 ROP 가 연동 방식에 따라 VDA 5050 주문(노드·엣지와 pick·drop action)이나 제조사 관제·Open-RMF 어댑터의 이동·동작 명령으로 바꿔 전달해야 할 것으로 보인다. | ref-031, ref-153 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f33 | [추정] | 출하 운반 중 주문 거절 오류(NO_ROUTE_TO_TARGET 등)나 연결 단절(CONNECTION_BROKEN), 상태 error 가 보고되면 ROP 는 이를 공통 예외로 옮겨 다른 로봇·플릿 재배정이나 사람 확인으로 넘겨야 할 것으로 보인다. | ref-031, ref-148 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f34 | [추정] | 분류 원문의 질문(개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까)에 대해, 개별 로봇 제어(저수준 제어·전체 제어·VDA 5050 직접 연결)는 ROP 가 경로·교통을 통합 조정할 수 있는 대신 제조사가 경로 지정·중단·교체 API 나 VDA 5050 지원을 제공해야 하고, 제조사 관제 위임(고수준 제어)이나 신호등·읽기 전용 수준 연동은 연동 부담이 작은 대신 공용 통로·승강기·문에서의 조정이 일시정지·재개나 상태 관측에 그칠 것으로 보인다. | ref-004, ref-258, ref-265, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f35 | [추정] | 연계 대상: 로컬 경로 계획·장애물 회피·위치추정 같은 로봇 자체 주행 기능은 로봇·제조사 쪽에 남고, 이종 제조사를 잇는 ROP 의 어댑터는 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스를 맡는 것으로 보인다. | ref-031, ref-258, ref-105, ref-153 | 아니오 | low | 2026-09-25 | — | — |
| f36 | [추정] | 로봇·관제 인터페이스마다 상태 어휘가 달라(Open-RMF 로봇 상태 7종, VDA 5050 action 상태·주문 거절 오류 유형, MassRobotics 운용 상태 9종) 어댑터는 이를 ROP 공통 상태·오류로 옮기는 변환표를 가져야 할 것으로 보이며, 이들 사이의 공개 표준 매핑은 이번 검색에서 확인하지 못했다. | ref-148, ref-031, ref-230 | 아니오 | low | 2026-09-25 | 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-25 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-136 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2076-3417/15/13/7235 | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |
| ref-258 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-259 | Open Robotics | Integration (integration) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration.html | 아니오 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-261 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-262 | Open Robotics (open-rmf) | awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/awesome_adapters | 아니오 |
| ref-263 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/inorbit-ai/ros_amr_interop | 아니오 |
| ref-264 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/free_fleet | 아니오 |
| ref-265 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 예 |
| ref-266 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 예 |
| ref-267 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023 | 논문 | medium | 2026-09-25 | https://www.researchgate.net/publication/374741902_Identification_of_requirements_and_opportunities_for_new_types_of_standardized_interfaces_for_AGV_systems_based_on_the_VDA_5050_concept | 예 |
| ref-268 | ScienceDirect 게재 논문(저자 미확인) | Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory | 2026 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0278612526000166 | 예 |
| ref-269 | 헬로티(HelloT) | 미르, 다기종 모바일 로봇 연동 SW 어댑터 ‘MiR VDA 5050’ 론칭 | 미확인 | 기사 | low | 2026-09-25 | https://www.hellot.net/news/article.html?no=99467 | 예 |
| ref-270 | 클로봇(Clobot) | 통합 로봇 관제 플랫폼 크롬스[CROMS] | 미확인 | 벤더 문서 | low | 2026-09-25 | https://clobot.co.kr/croms | 예 |
| ref-271 | 디지털투데이 | 카카오모빌리티, 로봇 플랫폼 사업 본격화..."이기종 로봇 통합 운영" | 2026-05 | 기사 | low | 2026-09-25 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=665333 | 예 |
| ref-272 | 머니투데이 | "로봇 통합 관제 기술, 인정받았다"..노바테크, 70억원 투자 유치 | 2026-07-14 | 기사 | low | 2026-09-25 | https://www.mt.co.kr/industry/2026/07/14/2026071409414468672 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f23·f22·f34(제조사별 관제 소프트웨어로 혼합 플릿 운영이 어렵고, 직접 제어와 관제 위임 사이 선택이 필요함) / 섹션 4: f1(제어 수준 4범주), f11·f12(관제·VDA 5050 토픽), f22(저수준·고수준 제어), f13(base·horizon) / 섹션 5: 출하 흐름 — 시작 조건 f32, 수행 자원 f34, 완료·인계 f31·f16, 예외·성과 f33·f14·f15 / 섹션 6: f2·f5·f6·f7(어댑터 API 요구·비동기 갱신·좌표 대응), f9(로봇 직접 접속), f36(상태 변환표), f34(방식 비교) / 섹션 7: f11~f19(VDA 5050 3.0.0: 트랙 반영 제안의 팩트시트 [추정]·오류 보고·action 완료 보고·3.0.0 발행을 3.0.0 명세 원본 근거 f18·f14·f16·f19 로 대체), f20(MassRobotics 식별·상태 보고, 트랙 제안의 'setup·status' 명칭을 스키마 명칭으로 정정), f7·f5(Open-RMF 작업 능력 선언·사용자 정의 동작, 트랙 제안 f19·f20 반영), f3·f10·f21 / 섹션 8: f24·f25·f26 연구, f27~f30 국내 사례(모두 벤더 주장·기사) / 섹션 9: f35(연계 대상: 로컬 주행은 제조사), f17 / 섹션 10: 10. 설비·건물 시스템 연동(f24, f10 승강기·문 어댑터), 12. 명령·작업 실행의 신뢰성(f13·f14·f15·f16), 15. 다중 로봇 경로·교통 관리 — MAPF(f1·f3·f17), 5. 로봇 능력·작업 온톨로지(f18·f7), 11. 분산 시스템·통신·컴퓨팅 구조(f12·f15), 13. 작업 배정 — MRTA(f29 재배정), 20. 예외 복구·재계획·업무 연속성(f33), 6. 지도·공간·위치 모델(f7 좌표 대응) / 섹션 11: 기존 oq-001·oq-005·oq-007·oq-014·oq-020 연결, open_questions_new 3건. 트랙 반영 제안 1건(2026-09-25-02, 7절)을 이번 조사로 재확인해 반영 대상에 넣음. 다음 실행 후보: 10. 설비·건물 시스템 연동 페이지 7절에 f10·f24 반영 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 플릿 관리 시스템 | Fleet Management System (FMS) | 여러 이동로봇에 작업을 배정하고 경로·상태를 관리하는 관제 소프트웨어로, 로봇 제조사가 자사 로봇용으로 제공하는 경우가 많다. |
| 다중 플릿 오케스트레이션 | Multi-Fleet Orchestration | 제조사가 다른 여러 로봇 플릿을 제3자 관제가 한곳에서 조율하는 것으로, 로봇을 직접 제어하는 저수준 방식과 제조사 관제에 작업을 넘기는 고수준 방식이 있다. |
| 엠큐티티 | Message Queuing Telemetry Transport (MQTT) | 브로커를 거쳐 토픽 단위로 메시지를 발행·구독하는 경량 메시징 프로토콜로, VDA 5050 이 관제와 이동로봇 사이 통신에 쓴다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가? | 관련 영역: 9. 로봇·제조사 관제 연동, 3. 처리능력·거점·설비 계획 | 근거: f22 | 종류: 일반
- 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? | 관련 영역: 9. 로봇·제조사 관제 연동, 15. 다중 로봇 경로·교통 관리 — MAPF | 근거: f1 | 종류: 일반
- Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성, 19. 모니터링·이상 탐지·원인 분석 | 근거: f36 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 1
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f1 은 Open Robotics 문서 두 개라 독립 교차 아님
    - f18·f19·f20 은 같은 발행 주체(VDA, MassRobotics) 자료 두 개라 독립 교차 아님
    - f14 주문 거절 오류 유형별 오류 등급은 열람 도구 응답만으로 확정하지 않아 넣지 않음
    - f10 어댑터 목록 각 항목의 제어 수준 미확인
    - f22·f23·f24·f25·f26 원문 미열람(검색 요약 범위), ref-265·ref-266 발행일 미확인, ref-268 저자·권호 미확인
    - f26 의 120 ms 수치 측정 조건 미확인
    - f27~f30 벤더 주장·기사이며 독립 확인 없음. 클로봇 자체 명령 규격(CRCS)은 출처 URL 을 특정하지 못해 넣지 않음
    - oq-005(VDA 5050 3.0.0 정확한 발행일) 미해결
    - oq-014·oq-020 관련 표준 매핑은 이번에도 찾지 못함
- 범위 경계 위반 의심:
    - f35: 로컬 경로 계획·장애물 회피·위치추정은 분류 원문 9장 '로봇 자체 지능·제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f9: free_fleet 은 로봇 내비게이션 스택에 직접 접속하는 구현이므로 로봇 주행 기능 자체를 ROP 직접 범위로 서술하지 않도록 연동 방식 사례로만 제안
    - f25: 제조 공장(OHT·AGV) 대상 연구이므로 물류센터 적용 사례처럼 서술하지 않도록 방법 참고로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 공식 원문을 열었다: 재사용 ref-004(rmf-core)·ref-031(VDA 5050 3.0.0 명세)·ref-105(어댑터 템플릿 설정)·ref-148(robot_state 스키마), 신규 ref-258·ref-259·ref-153(Open-RMF 통합 문서 원본)·ref-261(MassRobotics README)·ref-262(awesome_adapters)·ref-263(InOrbit ros_amr_interop)·ref-264(free_fleet). openTCS VDA 5050 어댑터와 InOrbit 저장소의 한 브랜치는 404 로 열지 못해 opentcs 는 출처에서 뺐다. 업계 보고서·연구기관·논문·기사·벤더 페이지 8건과 재사용 4건(ref-032·ref-136·ref-228·ref-230)은 원문 미열람이라 신뢰도 상한 medium(벤더·기사는 low). 검색 17회/30, 신규 출처 15건/15(ref-258~ref-272)로 신규 출처 상한에 도달해 SYNAOS 비교 글·DiVA 학위논문·MiR 공식 VDA 5050 페이지는 넣지 않았다. 교차 확인 1건(f11: VDA 5050 목적, 명세 원본과 Franke 외). 트랙 반영 제안 1건(2026-09-25-02)은 모두 다루었다: 팩트시트 기능 알림은 2.0.0 기준 [추정]에서 3.0.0 명세 원본 근거(f18)로, 상태 오류·action 완료 보고는 f14·f16·f31 로, 3.0.0 발행은 f19(발행일은 oq-005 로 남김)로, MassRobotics 는 f20(메시지 명칭은 스키마 기준 identityReport·statusReport)으로, Open-RMF 작업 능력·사용자 정의 동작은 f5·f7 로 재확인했다. 한국 자료: 국내 표준(TTA·KS)에서 이기종 로봇 관제 인터페이스 표준은 찾지 못했고, 국내 사례는 기사·벤더 자료(f27~f30)뿐이라 벤더 주장으로 표시했다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 분류원문 질문(개별 로봇 제어 대 제조사 관제 위임)은 f34 로 추정 수준 답만 냈고 정량 비교 자료는 찾지 못했다.
```
