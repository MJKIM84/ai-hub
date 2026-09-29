(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-05
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 12. 채팅으로 업무 지시·오케스트레이션 (C. 채팅 기반 구성·운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-849
- 새 출처 id 구간: ref-849 ~ ref-878 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-849 부터 순서대로 쓰고 ref-878 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-05/target.json

```json
{
  "run_id": "2026-09-29-05",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 97,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 12,
    "area_name": "12. 채팅으로 업무 지시·오케스트레이션",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=12"
}
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 12
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 12. 채팅으로 업무 지시·오케스트레이션

# 12. 채팅으로 업무 지시·오케스트레이션

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

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]

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

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 848건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 219개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
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
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
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
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
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

### docs/open-questions.md (요약: 대상 영역 [12] 에 걸린 0건 / 전체 138건)

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

### runs/2026-09-29-04/research.md

```markdown
# 리서치 브리프 2026-09-29-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-04 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 9. 채팅으로 시나리오 구성 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 불확실도 정렬·과소명세·미션 명세 패턴·상황 상태 추적 용어 없음(명확화 질문·슬롯 채우기·명시적 확인·행동 트리·BPMN·LTL 은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 구성(compose)·작업 요청 스키마, BPMN, 미션 명세 패턴 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 짝 연결 필요, 24. 작업·워크플로 모델링·13. 대화형 기능의 신뢰·기반 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
2. 언어 모델이 과소명세된 지시에서 빠진 조건을 알아채고 되묻는 시점과 질문 내용을 어떻게 정하며, 되묻기의 효과는 어떻게 측정되는가? (섹션 3·4·6 겨냥)
3. 여러 턴에 걸친 대화에서 이미 합의한 단계·값을 보존하고 바뀐 부분만 반영하며 사용자가 정한 값을 모델 추정보다 우선하려면 무엇이 필요한가? (섹션 3·6·11 겨냥)
4. 자연어 설명에서 순서·분기·반복을 가진 워크플로(BPMN·행동 트리·시간 논리)를 만들고 실행 가능성을 검증하는 연구는 무엇이 있고 정확도는 어떻게 보고되는가? (섹션 4·6·8 겨냥)
5. 시나리오가 담아야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)을 관제·플랫폼의 작업 요청·작업 구성 형식은 어떤 필드로 받는가? (섹션 4·7 겨냥)
6. 병원·물류창고·제조 공장 등 현장 유형별로 대화로 작업 시나리오를 정한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
7. 채팅 시나리오 구성에서 ROP가 직접 맡을 것(대화→구조화 시나리오·되묻기·검증·승인)과 로봇 수준 실행·형식 계획기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | KnowNo(Ren 외, CoRL 2023)는 언어 모델 계획기의 불확실도를 등각 예측(conformal prediction)으로 측정해 후보 행동의 예측 집합이 하나로 좁혀지면 자율 실행하고 여러 개가 남으면 사람에게 되묻는 틀로, 공간·수량·속성·대명사 지시·선호·안전의 여러 모호성 유형에서 목표 성공률을 보장하면서 사람의 도움 요청을 줄였다고 보고했다. | ref-351 | 아니오 | medium | 2023-09-04 | — | — |
| f2 | [사실] | Deng 외(2026)는 되묻기 질문의 가치를 정답 목표에 대한 베이즈 믿음 갱신량으로 재는 정보 이득 보상(Information Gain Reward)으로 명확화 모델을 학습해, 명확화를 더한 τ-Bench 환경에서 다섯 종의 에이전트 모델 모두에서 되묻기 없는 기준선보다 성공률을 평균 3.7% 높이면서 상호작용 단계는 평균 0.3회만 늘렸다고 보고했다. | ref-840 | 아니오 | medium | 2026-06-02 | — | — |
| f3 | [추정] | 불확실도로 되묻기 시점을 정하는 연구(f1)와 질문의 정보 이득으로 질문 내용을 고르는 연구(f2)를 함께 보면, 이 영역의 '모자란 조건은 선택지와 이유를 붙인 질문으로 채운다'는 기능은 모든 항목을 순서대로 묻는 서식이 아니라 시나리오 항목마다 불확실도를 재어 실행 결과가 갈리는 항목만 후보 선택지와 함께 되묻는 방식으로 구현해야 질문 횟수를 줄일 수 있을 것으로 보인다. | ref-351, ref-840 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f4 | [사실] | Laban 외(2025)는 20만 건 이상의 시뮬레이션 대화로 상위 공개·비공개 언어 모델을 비교해 여섯 가지 생성 과제에서 다중 턴 성능이 단일 턴보다 평균 39% 낮았고, 그 원인이 능력 저하보다 신뢰성 저하이며 모델이 초기 턴에서 가정을 세우고 성급히 최종 답을 낸 뒤 그것에 과도하게 의존하기 때문이라고 보고했다. | ref-841 | 아니오 | medium | 2025-05-09 | — | — |
| f5 | [사실] | Tack·Laban·Neville(2026)은 사용자가 의도를 처음에 다 밝히지 않고 점진적으로 드러내고 수정하며 중간에 방향을 바꾸는 다중 턴 대화로 기존 단일 턴 벤치마크를 변환하는 틀을 제안했고, 정적 설정의 높은 성능이 의도가 바뀌는 설정으로 옮겨지지 않아 여러 모델 계열에서 큰 폭의 성능 하락이 나타난다고 보고했다. | ref-842 | 아니오 | medium | 2026-07-22 | — | — |
| f6 | [사실] | Tao·Tao·Wang(2026)의 IDSS(Intent-Driven Situation States)는 대화 이력과 별도로 도구가 확인한 사실과 작업 상태 판단을 분리한 명시적 상황 상태(사용자 의도·필요 변수·제약·실행 상태)를 학습 없이 유지하는 틀로, 세 개의 상호작용 벤치마크와 여덟 개 언어 모델에서 작업 완료·선호 도출·상호작용 효율이 개선됐고 특히 다중 개체 조정·바뀌는 제약·제약 인식 재계획 과제에서 이득이 컸다고 보고했다. | ref-843 | 아니오 | medium | 2026-08-16 | — | — |
| f7 | [추정] | 다중 턴에서 모델이 초기 가정에 묶이고(f4) 바뀌는 의도를 따라가지 못하며(f5) 명시적 상황 상태가 이를 완화한다는 연구(f6)를 함께 보면, 이 영역의 '합의 내용 보존·변경 표시·사용자 값 우선'은 언어 모델의 대화 문맥에 맡길 것이 아니라 시나리오를 대화 밖의 구조화 상태로 두고 값마다 출처(사용자 확정·모델 추정·미정)를 기록해 턴마다 바뀐 부분만 갱신·표시하는 방식으로 구현해야 할 것으로 보인다. | ref-841, ref-842, ref-843 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f8 | [사실] | Kourani·Berti·Schuster·van der Aalst(2024)는 텍스트 설명에서 프로세스 모델을 자동 생성하고 반복 정제하는 언어 모델 기반 틀을 제안해 프롬프트 전략, 안전한 모델 생성 규약, 오류 처리 기제를 두고, 생성 모델의 품질 보장과 BPMN·페트리 넷 표준 표기 내보내기를 지원하는 시스템으로 구현했으며 예비 결과만 보고했다. | ref-844 | 아니오 | medium | 2024-03-12 | — | — |
| f9 | [사실] | Matei 외(2026)는 다국어 BPMN 파일을 번역·SpiffWorkflow 실행 지향 적합성 검사·언어 모델 반복 수정으로 정답 말뭉치를 만들고 그 설명문에서 실행 가능한 BPMN 2.0 XML 을 재구성하는 다단계 파이프라인으로, 공개 BPMN 750개 중 검증된 정답 387개를 얻고 평균 재구성 유사도 0.75 이상과 이름만 다른 거의 완전한 재구성 약 50건을 보고했다. | ref-845 | 아니오 | medium | 2026-04-13 | — | — |
| f10 | [사실] | 서로 다른 두 연구 그룹(Kourani 외, Matei 외)이 자연어 텍스트에서 BPMN 프로세스 모델을 언어 모델로 생성하되 실행 지향 검사나 오류 처리로 생성 결과의 유효성을 확보하는 방법을 각각 보고해, 텍스트에서 실행 가능한 워크플로 모델을 만드는 접근이 한 곳 이상에서 확인된다. | ref-844, ref-845 | 예 | medium | 2026-04-13 | — | — |
| f11 | [추정] | 할 일·순서·반복·실패 처리 조건을 가진 시나리오는 프로세스 모델과 같은 구조이므로, 텍스트→BPMN 생성 연구(f8·f9·f10)가 쓰는 '생성 후 실행 지향 검사로 유효성 확보' 흐름은 9. 채팅으로 시나리오 구성이 대화 결과를 24. 작업·워크플로 모델링의 워크플로 모델로 내고 검증하는 방식의 선례가 될 것으로 보인다. | ref-844, ref-845 | 아니오 | low | 2026-09-29 | — | — |
| f12 | [사실] | BTGenBot(Izzo·Bardaro·Matteucci, 2024)은 최대 70억 매개변수의 경량 언어 모델을 기존 행동 트리에서 GPT-3.5 로 만든 데이터셋으로 미세조정해 자연어 작업 설명에서 로봇 행동 트리를 생성하며, llama2·llama-chat·code-llama 변형을 아홉 과제에서 구문 분석·검증 시스템·시뮬레이션·실제 로봇으로 평가했다. | ref-061 | 아니오 | medium | 2024-03-19 | — | — |
| f13 | [사실] | ConformalNL2LTL(Sundarsingh 외, 2025)은 자연어 지시를 선형 시간 논리 공식으로 옮길 때 번역을 질의응답 단계로 나누고 각 단계의 불확실도를 등각 예측으로 재어, 사용자가 정한 신뢰 문턱에 못 미치면 보조 모델에, 그래도 부족하면 사용자에게 되물어 사용자 지정 번역 성공률을 보장하는 방법이다. | ref-847 | 아니오 | medium | 2026-02-20 | — | — |
| f14 | [사실] | 서로 다른 세 연구 그룹(KnowNo, ConformalNL2LTL, Deng 외)이 언어 모델이 해석에 확신이 없을 때만 사람에게 되묻도록 불확실도나 정보 이득을 기준으로 되묻기를 제한하는 설계를 각각 보고해, '확신 없는 항목만 되묻기' 접근이 한 곳 이상에서 확인된다. | ref-351, ref-847, ref-840 | 예 | medium | 2026-06-02 | 시작 조건 | — |
| f15 | [사실] | Menghi 외(2019)는 로봇 문헌의 현실적 임무 요구 245건에서 이동 로봇 미션 명세 패턴 22개를 뽑아 사용 의도·알려진 용례·패턴 간 관계·시간 논리 템플릿과 함께 목록으로 정리하고, 패턴을 인스턴스화·조합·LTL/CTL 로 컴파일하는 도구를 만들어 실제 임무 요구 441건과 명세 1,251건, 산업 파트너 시나리오 5건, 시뮬레이터와 실제 로봇 2대로 검증했다. | ref-848 | 아니오 | medium | 2019-01-07 | — | — |
| f16 | [추정] | 반복되는 임무 요구를 패턴 목록으로 정리한 연구(f15)와 자연어를 시간 논리로 옮길 때 불확실한 단계만 되묻는 연구(f13)를 함께 보면, 이 영역의 핵심 질문인 '무엇을 되물어야 하는가'는 시나리오 항목(순서·반복·기한·회피·실패 처리)마다 대응하는 명세 패턴의 빈 자리를 채우는 질문 목록으로 구성하고 그중 해석이 불확실한 자리만 실제로 묻는 방식으로 답할 수 있을 것으로 보인다. | ref-848, ref-847 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f17 | [사실] | Open-RMF 문서는 작업(task)을 단계(phase)를 만들어 내는 객체로 정의하고 공개 API 단계로 GoToPlace·PickUp·DropOff·PerformAction 을, 내부 자동 추가 단계로 RequestLift 를 두며, 'compose' 범주의 작업은 활동(activity)의 순서열로 단계를 엮고, 작업 요청은 특정 로봇에 직접 배정하는 robot_task_request 와 최적 플릿에 맡기는 dispatch_task_request 로 보내며 Clean·Delivery·Patrol·Compose 범주의 JSON 스키마를 따른다. | ref-110 | 아니오 | medium | 2026-09-29 | 작업 대상 | — |
| f18 | [사실] | Open-RMF 작업 요청 스키마(rmf_api_msgs task_request.json)는 필수 필드로 범주(category)와 플릿이 지원하는 스키마를 따르는 설명(description)을, 선택 필드로 가장 이른 시작 가능 시각(unix_millis_earliest_start_time)·요청 시각·플릿 우선순위 스키마를 따르는 priority·용도 라벨(labels)·요청자(requester)·수행 허용 플릿 이름(fleet_name)을 두며, 완료 기한이나 반복 주기 필드는 두지 않는다. | ref-125 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f19 | [추정] | 이 영역이 대화로 정하려는 값 가운데 할 일·순서(compose 활동 순서열)·물품 인계(PickUp·DropOff)·시작 조건(가장 이른 시작 시각)·우선순위·요청자·수행 플릿은 Open-RMF 작업 구성과 작업 요청에 이미 자리가 있으나, 완료 기한·반복·실패 처리 조건은 작업 요청 스키마에 자리가 없으므로 채팅 시나리오 구성의 결과물은 관제 작업 요청보다 넓은 시나리오 모델(33. 시나리오 모델·편집, 24. 작업·워크플로 모델링)에 담고 실행 시점에 작업 요청으로 변환해야 할 것으로 보인다. | ref-110, ref-125 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f20 | [사실] | University West(스웨덴) 학위논문 'An LLM-Interface for Robot Mission Specification in Logistics'는 물류 현장의 자율이동로봇 임무 계획에서 사람의 자연어와 계획기가 요구하는 신호 시간 논리(STL) 사이의 번역 인터페이스로 언어 모델을 쓰는 신뢰성을 조사해, 현재 언어 모델이 공식의 구문과 논리는 만들지만 구문상 유효한 STL 공식을 일관되게 내지 못하는 것이 핵심 병목이라고 밝혔다. | ref-548 | 아니오 | medium | 2026-09-29 | 제약 | 원문 미열람 |
| f21 | [사실] | Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. | ref-852 | 아니오 | medium | 2026 | 병원 / 예외·성과 | 원문 미열람 |
| f22 | [사실] | 손승아·강태민·하동수(한국과학기술원)는 정보과학회지 2024년 10월호에 '자연어 로봇 제어 기술 동향: 분류, 기술, 응용'을 실어 인지 수준에 따른 시스템 분류, 사용 기술, 자연어 로봇 작업의 범위를 정리했다. | ref-853 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f23 | [추정] | 병원 사례(f21)에서 실행 중 들어온 추가 요청이 재스케줄링으로 이어진 점과 다중 턴에서 합의가 흔들리는 문제(f4·f5)를 함께 보면, 채팅 시나리오 구성은 실행 전 합의된 시나리오를 확정본으로 잠그고 실행 중 대화로 들어온 변경은 확정본에 대한 차이로 표시해 다시 승인받는 절차를 두어야 하며, 그 실행·재계획 자체는 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성이 맡는 것이 원문 구분에 맞을 것으로 보인다. | ref-852, ref-841, ref-842 | 아니오 | low | 2026-09-29 | 병원 / 완료·인계 | — |
| f24 | [추정] | 확인한 자료를 종합하면 9. 채팅으로 시나리오 구성에서 ROP가 직접 맡을 범위는 대화를 값마다 출처가 붙은 구조화 시나리오(할 일·물품·사람·순서·반복·기한·실패 처리 조건)로 바꾸고, 불확실한 항목만 선택지와 이유를 붙여 되묻고, 워크플로 모델과 실행 지향 검사로 시나리오의 유효성을 확인하며, 합의본을 보존·차이 표시하고 사람이 승인한 시나리오만 실행 단계로 넘기는 일로 보인다. | ref-351, ref-843, ref-845, ref-110 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f25 | [추정] | 연계 대상: 자연어에서 로봇 수준 행동 트리를 생성해 로봇에서 실행하는 일(BTGenBot)과 자연어를 LTL·STL 공식으로 옮겨 형식 계획기·모델 검사기로 계획을 만드는 일(ConformalNL2LTL, University West 학위논문)은 분류 원문 19장의 로봇 자체 지능·제어와 외부 계획 도구 쪽이며, ROP는 시나리오의 순서·기한·실패 처리 조건을 이들 도구가 읽을 수 있는 인터페이스로 넘기고 그 결과(실행 가능 여부·검증 결과)를 받아 대화로 설명하는 데 그쳐야 할 것으로 보인다. | ref-061, ref-847, ref-548 | 아니오 | low | 2026-09-29 | — | — |
| f26 | [추정] | 불확실도 정렬과 명확화 학습(KnowNo, Deng 외), 텍스트→프로세스 모델 생성(Kourani 외, Matei 외), 자연어→시간 논리 번역(ConformalNL2LTL)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 이 영역 양쪽에 연결하고, 오해석 방지·평가 부분은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다. | ref-351, ref-844, ref-847 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-09-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-840 | Deng, M., Li, Z., Li, X., Zhu, T., Zhao, Y., Guo, Z., & Wang, W. | Uncertainty-Aware Clarification in LLM Agents with Information Gain | 2026-06-02 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.03135 | 아니오 |
| ref-841 | Laban, P., Hayashi, H., Zhou, Y., & Neville, J. | LLMs Get Lost In Multi-Turn Conversation | 2025-05-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.06120 | 아니오 |
| ref-842 | Tack, J., Laban, P., & Neville, J. | LLMs Get Lost in Evolving User Intent | 2026-07-22 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.20734 | 아니오 |
| ref-843 | Tao, M., Tao, Y., & Wang, P. | Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents | 2026-08-16 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2608.15755 | 아니오 |
| ref-844 | Kourani, H., Berti, A., Schuster, D., & van der Aalst, W. M. P. | Process Modeling With Large Language Models | 2024-03-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.07541 | 아니오 |
| ref-845 | Matei, I., Zhenirovskyy, M., Menaka Sekar, P. K., & Wong, H. Y. | Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach | 2026-04-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2604.12105 | 아니오 |
| ref-061 | Izzo, R. A., Bardaro, G., & Matteucci, M. | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 2024-03-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.12761 | 아니오 |
| ref-847 | Sundarsingh, D. S., Wang, J., Deshmukh, J. V., & Kantaros, Y. | ConformalNL2LTL: Translating Natural Language Instructions into Temporal Logic Formulas with Conformal Correctness Guarantees | 2026-02-20 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2504.21022 | 아니오 |
| ref-848 | Menghi, C., Tsigkanos, C., Pelliccione, P., Ghezzi, C., & Berger, T. | Specification Patterns for Robotic Missions | 2019-01-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1901.02077 | 아니오 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-548 | University West (Högskolan Väst, DiVA) 학위논문 저자(미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 미확인 | 논문 | medium | 2026-09-29 | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf | 예 |
| ref-852 | Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력 | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 2026 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10514-026-10255-6 | 예 |
| ref-853 | 손승아, 강태민, 하동수 (한국과학기술원), 정보과학회지 42(10) | 자연어 로봇 제어 기술 동향: 분류, 기술, 응용 | 2024-10 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11940459 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4·f5(다중 턴에서 합의가 흔들림), f14(확신 없는 항목만 되묻기), f20(자연어→형식 명세의 병목) / 섹션 4: f1(불확실도 정렬·예측 집합), f2(정보 이득), f6(상황 상태), f15(미션 명세 패턴), f17(작업·단계·활동), f4(과소명세) / 섹션 5: 병원 — f21·f23(자연어 지시→작업 순서열, 실행 중 추가 요청, 원문 미열람 명시), 물류 — f20(물류 AMR 임무 명세 학위논문, 현장 유형은 '물류'로만 서술) / 섹션 6: f1·f2·f3·f13·f14(되묻기 시점·내용), f6·f7(합의 보존·값 출처), f8·f9·f10·f11(텍스트→워크플로 생성과 실행 지향 검사), f12(행동 트리 생성), f15·f16(패턴 기반 질문 목록) / 섹션 7: f17·f18·f19(Open-RMF compose·task_request), f8(BPMN·페트리 넷), f15(패턴 도구·LTL/CTL), f12(행동 트리) / 섹션 8: f1, f2, f4, f5, f6, f8, f9, f13, f15, f21, 국내 f22 / 섹션 9: f24(직접 범위), f25(연계 대상: 로봇 수준 행동 트리 실행·형식 계획기) / 섹션 10: 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현(f19·f26, 원문 주석의 짝), 24. 작업·워크플로 모델링(f11·f19), 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성(f23), 13. 대화형 기능의 신뢰·기반(f14·f26), 10. 채팅으로 로봇 구성(f17 수행 플릿), 26. 작업 순서·스케줄링(f18 시작 시각·우선순위), 20. 로봇·제조사 관제 연동(f17·f18), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f26, 교차 규칙), 63. 병원·의료(f21) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 24. 작업·워크플로 모델링 페이지에 f8·f9·f10 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f1·f4·f14 반영, 33. 시나리오 모델·편집 페이지에 f15·f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 불확실도 정렬 | Uncertainty Alignment | 언어 모델 계획기가 자신의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻도록 맞추는 것으로, 등각 예측으로 후보 집합을 만들어 집합 크기로 되묻기를 정한다. |
| 과소명세 | Underspecification | 사용자 지시에 실행에 필요한 조건(대상·장소·수량·기한 등)이 빠져 여러 해석이 가능한 상태로, 명확화 질문이나 기본값 규칙으로 채워야 한다. |
| 미션 명세 패턴 | Mission Specification Pattern | 이동 로봇 임무 요구에서 반복되는 명세 문제와 그 시간 논리 템플릿을 목록으로 정리한 것으로, 패턴을 채우고 조합해 형식 명세를 만든다. |
| 상황 상태 추적 | Situation State Tracking | 다중 턴 대화에서 대화 이력과 별도로 사용자 의도·필요 변수·제약·실행 상태를 명시적 상태로 유지해 확인된 사실과 판단을 구분하는 기법이다. |

## 열린 질문

새로 생긴 질문:

- 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 33. 시나리오 모델·편집 | 근거: f16 | 종류: 일반
- 대화로 정한 시나리오에서 사용자가 확정한 값과 모델이 추정한 값을 구분해 저장·표시하고 턴마다 바뀐 부분만 보여 주는 공개 데이터 형식이나 편집기 구현이 있는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 20. 로봇·제조사 관제 연동 | 근거: f19 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? | 관련 영역: 9. 채팅으로 시나리오 구성, 61. 물류창고, 63. 병원·의료 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 2
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f1 KnowNo 의 '10~24% 도움 감소' 범위는 HTML 본문 요약에서 봤으나 실험별 조건을 확인하지 못해 claim 에는 넣지 않고 발췌의 단계별 14%·시행별 8% 인용만 씀
    - f12 BTGenBot 의 실패 처리(fallback) 노드 생성 방식은 초록에 없어 미확인
    - f15 미션 명세 패턴 22개의 개별 이름·분류(이동·트리거·회피 등)는 초록에서 확인하지 못함
    - f20 University West 학위논문 원문 미열람(DiVA PDF·기록 페이지 5회 연결 재설정) — 저자·연도·실험 결과 미확인, 검색 결과 초록 범위만 사용
    - f21 Autonomous Robots 병원 논문 원문 미열람(Springer 인증 리다이렉트, MDPI 대안 403) — 저자·정량 결과·확인 절차 미확인
    - f22 정보과학회지 동향 논문 본문 미열람(DBpia 서지만 확인) — 초록·분류 내용 미확인
    - f8 Kourani 외의 정량 결과는 초록에 없어 미확인
    - f10·f14 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f17·f18 Open-RMF 문서·스키마 발행일 미확인
    - BPMNGen(Springer BISE 2025, 대화형 BPMN 생성)과 MDPI Applied Sciences 로봇 건강 보조원 프레임워크는 인증·403 으로 열지 못해 넣지 않음
    - OATH(arXiv 2510.14063)는 검색 요약과 달리 초록에 되묻기 대화 내용이 없어 제외
    - 대화만으로 로봇 작업 시나리오를 구성한 실제 현장 운영 사례는 찾지 못함(연구 프로토타입·병원 시범 배치·학위논문뿐)
- 범위 경계 위반 의심:
    - f25: 로봇 수준 행동 트리 실행과 LTL·STL 형식 계획기는 분류 원문 19장 '로봇 자체 지능·제어'·외부 도구 쪽이므로 '연계 대상: '으로 표시함
    - f21·f23: 병원 로봇의 실행 중 재스케줄링·실패 복구는 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 시나리오 변경·재승인 절차의 근거로만 제안함
    - f8·f9·f10·f11: 업무 프로세스(비로봇) 대상 연구는 워크플로 생성·검증 방법의 선례로만 제안함
    - f2·f4·f5·f6: 일반 언어 모델 에이전트 연구(로봇 아님)는 대화 설계 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-351~ref-853, 예약 구간 안) 상한 도달로 Cao·Lee 행동 트리 생성(arXiv 2302.12927), Choe 외 창고 협동 로봇 LLM-to-TL(arXiv 2505.13376), SEQUOR 다중 턴 제약 준수 벤치마크(arXiv 2605.06353), Bettencourt·Guerreiro BPMN 문헌 리뷰(arXiv 2604.14034), Purdue 'Human in the loop' 학위논문은 열었거나 확인했으나 넣지 못했다. 원문 열람 12건(webfetch 10, github_raw 2: task_new.md·task_request.json), 미열람 3건(ref-548·ref-852·ref-853, 검색 결과·서지 페이지로 기관·제목 확인). 교차 확인 2건(f10: Kourani 외·Matei 외, f14: KnowNo·ConformalNL2LTL·Deng 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록 페이지 확인, 오픈소스 문서는 단일 출처). 분류 원문 핵심 질문(무엇을 되물어야 하는가)에는 f1·f2·f13·f14(불확실한 항목만 되묻기), f15·f16(명세 패턴의 빈 자리를 질문 목록으로), f17·f18·f19(관제 작업 형식에 있는 항목과 없는 항목)로 답했으며 결론은 '되묻기 대상은 시나리오 항목의 빈 자리 가운데 해석이 불확실하고 실행 결과가 갈리는 것으로 제한하고, 기한·반복·실패 처리처럼 관제 요청에 자리가 없는 항목은 시나리오 모델에서 보관해야 한다'는 추정(f3·f16·f19·f24)이다. 현장 유형: 병원(f21·f23, 원문 미열람 명시)만 확인했고 물류는 학위논문(f20)이 '물류' 일반을 말해 site_type 을 채우지 않았으며 제조 공장·상업 시설·가정·실외 사례는 없다. 합의 내용 보존·변경 표시(f7)는 로봇 시나리오가 아닌 일반 언어 모델 대화 연구(f4·f5·f6)에서 도출한 추정이다. L. AI·학습 기술 관련 finding(f1·f2·f8·f9·f13·f26)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현·24. 작업·워크플로 모델링 양쪽에 연결하도록 제안했다. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 838건과의 URL 중복을 대조하지 못했으므로 KnowNo·Open-RMF task_new·rmf_api_msgs 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 명확화 질문·슬롯 채우기·명시적 확인·행동 트리·BPMN·LTL·구조화 출력·작업 분해·사람 참여 루프·등각 예측은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

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

### runs/2026-09-25-31/research.md

```markdown
# 리서치 브리프 2026-09-25-31

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-31 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 12. 명령·작업 실행의 신뢰성 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(멱등성, 주문 갱신 id, 목표 id, 상태 기계, 마지막 유언 메시지 등)
- 섹션 5. 현장 시나리오 비어 있음(운반 요청 재전송·취소·재시작 시나리오)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(관련 기존 열린 질문 oq-014·oq-021·oq-033 이 이 영역을 관련 영역으로 둠)

## 조사 질문

1. 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [분류원문]
2. 로봇 인터페이스 표준(VDA 5050, ROS 2 액션, Open-RMF 작업 API)은 명령의 접수·실행·완료·취소 상태와 명령 식별자를 어떻게 정의하는가? (섹션 4·6·7 겨냥)
3. 중복 요청 방지(멱등성)를 위한 일반 표준·관행(IETF Idempotency-Key 초안, MQTT QoS)은 무엇이고, 로봇 명령 계층에 어떤 한계와 함께 적용되는가? (섹션 6·7 겨냥)
4. 시간 초과·연결 끊김을 감지하는 기법(마지막 유언 메시지, 상태 보고 주기, ROS 2 QoS deadline·liveliness)과 그 뒤의 처리 규칙은 어디까지 표준이 정하는가? (섹션 3·6 겨냥)
5. 관제 소프트웨어나 로봇이 재시작된 뒤 진행 중 작업 상태를 복원하는 방법(작업 백업, 관리형 노드 수명주기)은 어떤 것이 있고 공개 구현의 한계는 무엇인가? (섹션 6·8·11 겨냥)
6. 산업 자동화의 상태 기계 표준(OPC UA Programs, PackML, ISA-95 Job Control)과 행동 트리·사가(보상 트랜잭션) 같은 실행 구조 기법은 명령 실행 신뢰성에 어떻게 쓰이는가? (섹션 6·8·10 겨냥)
7. ROP가 직접 맡을 신뢰성 기능과 로봇 제조사·통신 계층에 맡길 기능의 경계는 무엇인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 이동로봇이 같은 orderUpdateId 의 주문을 다시 받았을 때 내용이 같으면 무시하고, 내용이 다르면 SAME_ORDER_UPDATE_ID 오류(WARNING)를 보고하도록 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 에서 이동로봇은 이전보다 낮은 orderUpdateId 의 주문을 받으면 새 주문을 버퍼에 받지 않고 이전 주문을 유지하며 OUTDATED_ORDER_UPDATE 오류(WARNING)를 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 관제는 로봇이 상태 메시지에 싣는 주문 id·주문 갱신 id 로 주문 수용 여부를 알 수 있으며, 로봇은 상태 메시지를 관련 사건이 생길 때 또는 적어도 30초마다 발행해야 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f4 | [사실] | VDA 5050 3.0.0 은 무선 전송이 신뢰할 수 없으므로 이미 전달한 기반(base) 경로는 바꿀 수 없고 관제는 기반이 이미 실행되었다고 가정해야 하며, 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다고 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | VDA 5050 3.0.0 은 order·instantActions·state 등 대부분의 토픽에 MQTT QoS 0(최선 노력)을, connection 토픽에 QoS 1(최소 한 번)을 쓰게 하고, 로봇이 예기치 않게 끊기면 브로커가 마지막 유언(last will) 메시지로 connectionState 를 CONNECTION_BROKEN 으로 알리게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 에서 cancelOrder 즉시 동작을 받은 로봇은 가능한 한 빨리 멈추고, 실행 중인 동작이 모두 취소·종료될 때까지 cancelOrder 를 RUNNING 으로, 이동과 모든 동작이 멈춘 뒤 FINISHED 로 보고하며, 이후 관제는 취소된 주문에 갱신을 보내지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | VDA 5050 3.0.0 은 동작 상태에 실패했지만 다시 시도할 수 있음을 뜻하는 RETRIABLE 을 두고, 관제가 즉시 동작 retry 로 재시도하거나 skipRetry 로 그 동작을 FAILED 로 넘기게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [사실] | ROS 2 액션 설계는 목표(goal) id 를 액션 클라이언트만 생성하되 UUID 로 만들어 여러 클라이언트 사이 충돌을 줄이고, 목표 상태를 ACCEPTED·EXECUTING·CANCELING(진행)과 SUCCEEDED·ABORTED·CANCELED(종료)로 나누며, 서버는 결과를 설정한 시간 동안 캐시해 여러 클라이언트가 받을 수 있게 한다. | ref-588 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 의 작업 파견 요청(dispatch_task_request)과 작업 요청(task_request) 스키마에는 요청자가 정하는 요청 식별자나 멱등성 키 필드가 없고, 요청 시각·우선순위·범주·설명·라벨·요청자·플릿 이름만 둔다. | ref-590, ref-125 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f10 | [추정] | Open-RMF 작업 요청 스키마에 요청자 측 식별자가 없으므로, 응답을 받지 못한 파견 요청을 그대로 다시 보내면 별개 작업이 하나 더 생길 수 있어 ROP 쪽에서 상위 요청 id 와 작업 id 의 대응을 저장해 중복을 걸러야 할 것으로 보인다. | ref-590, ref-125, ref-111 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f11 | [사실] | Open-RMF 의 작업 취소 요청과 작업 중단(interrupt) 요청은 작업 id(task_id)와 선택 라벨만으로 대상을 지정하며, 중단된 작업은 이후 재개 요청을 보내야 다시 진행된다. | ref-126, ref-127 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f12 | [사실] | Open-RMF 작업 상태 스키마는 queued·underway·completed·canceled·killed·failed 등 상태 값과 시작·종료 시각, 취소·강제 종료·중단 요청 기록을 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f13 | [사실] | Open-RMF rmf_task 라이브러리의 실행 중 작업(Task::Active)은 순서 번호가 붙은 문자열 형태의 백업을 만들 수 있고, 취소(cancel)는 로봇을 짐 없는 상태로 되돌리게 하며, 강제 종료(kill)는 취소보다 우선해 로봇을 안전한 유휴 상태로 되돌리게 하고, 단계 건너뛰기(skip)·되감기(rewind)를 제공한다. | ref-591 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f14 | [사실] | Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하고, 작업 로그와 백업을 SQLite 데이터베이스에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다. | ref-600 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | IETF HTTPAPI 작업반의 Idempotency-Key 헤더 초안(RFC 가 아닌 인터넷 초안)은 클라이언트가 만든 고유 키로 서버가 같은 요청의 재시도를 알아보게 하며, 키를 다른 내용의 요청에 재사용하면 안 되고, 서버는 키 만료 정책을 공개해야 하며, 원 요청이 처리 중일 때의 재요청에는 409, 다른 내용으로 재사용한 요청에는 422 를 돌려주도록 제안한다. | ref-592 | 아니오 | medium | 2025-10-15 | — | — |
| f16 | [사실] | MQTT 5.0 의 QoS 2(정확히 한 번)는 네 단계 확인 교환으로 프로토콜 상대 사이의 정확히 한 번 전달을 보장하며, 수신 측은 PUBCOMP 를 보낼 때까지 원 PUBLISH 의 패킷 식별자를 기억해 확인 응답 손실로 다시 온 중복 PUBLISH 를 버린다. | ref-306 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [추정] | MQTT QoS 보장은 클라이언트–브로커 같은 프로토콜 상대 사이에만 적용되므로, 관제가 응답 시간 초과 뒤 새 메시지로 주문을 다시 보내는 경우의 중복은 QoS 가 아니라 VDA 5050 의 주문 id·주문 갱신 id 같은 응용 계층 식별자로 걸러야 할 것으로 보인다. | ref-306, ref-031 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f18 | [사실] | ROS 2 의 서비스 품질(QoS) 정책은 신뢰(reliable)·최선 노력(best effort) 전달, 늦게 참여한 구독자를 위해 발행자가 샘플을 보존하는 transient local 지속성, 메시지 사이 최대 간격을 정하는 deadline, 임대 기간(lease duration) 안에 살아 있음을 알리지 않으면 활성 상실로 보는 liveliness 와, 그 위반을 알리는 QoS 이벤트를 둔다. | ref-282 | 아니오 | medium | 2026-09-25 | — | — |
| f19 | [사실] | ROS 2 관리형 노드(managed node) 설계는 Unconfigured·Inactive·Active·Finalized 네 주 상태와 전이 상태를 두어, 감독 도구가 모든 구성요소가 올바르게 준비되었는지 확인한 뒤 실행을 허용하고 노드를 운영 중에 재시작·교체할 수 있게 한다. | ref-589 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | OPC UA Part 10(Programs)의 프로그램 상태 기계는 Halted·Ready·Running·Suspended 상태를 두며, Suspended 는 멈춘 지점에서 기능을 재개할 수 있는 상태이고, Halted 는 초기 상태이자 실패 또는 완료를 나타내는 종료 상태가 될 수 있다. | ref-594 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f21 | [사실] | ISA-TR88.00.02(PackML)는 기계·유닛 상태 모델로 Idle·Starting·Execute·Completing·Complete·Resetting·Holding·Held·Unholding·Suspending·Suspended·Unsuspending·Stopping·Stopped·Aborting·Aborted·Clearing 17개 상태를 정의한다. | ref-595 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f22 | [사실] | 상위 작업 지시 쪽에서 OPC UA for ISA-95 Job Control 은 Store·StoreAndStart·Start·RevokeStart·Pause·Resume·Update·Abort·Stop·Cancel·Clear 메서드를, B2MML 거래 프로파일은 CHANGE·CANCEL 등 거래 동사를 정의한다. | ref-130, ref-129 | 아니오 | medium | 2024-01-31 | 시작 조건 | — |
| f23 | [사실] | 행동 트리 라이브러리 BehaviorTree.CPP 는 자식이 실패하면 지정한 횟수까지 다시 실행하는 RetryNode 와, 자식이 정해진 시간보다 오래 RUNNING 이면 중단(halt)하고 FAILURE 를 돌려주는 TimeoutNode 를 제공한다. | ref-597, ref-598 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f24 | [사실] | Colledanchise·Ögren 의 행동 트리 입문서는 행동 트리를 자율 에이전트의 작업 전환을 구조화하는 방법으로 소개하며, 모듈성과 반응성을 함께 갖춘 시스템을 만드는 효율적 방법이라고 설명한다. | ref-596 | 아니오 | medium | 2017-09 | — | 원문 미열람 |
| f25 | [사실] | Garcia-Molina·Salem(1987)의 사가(Saga)는 오래 걸리는 트랜잭션을 다른 트랜잭션과 섞여 실행될 수 있는 작은 트랜잭션의 순서로 나누고, 각 단계에 보상 트랜잭션을 두어 전부 완료되거나 부분 실행을 보상하게 하며, 보상은 의미상 되돌림이지 처음 상태 복원을 보장하지 않는다. | ref-599 | 아니오 | medium | 1987 | — | 원문 미열람 |
| f26 | [추정] | 로봇이 이미 화물을 싣거나 옮긴 물리 동작은 되돌릴 수 없으므로, 취소된 운반 작업의 복구는 사가의 보상 단계처럼 원위치 반송 같은 별도 작업을 새로 만들어 처리하는 형태가 될 것으로 보인다. | ref-599, ref-031, ref-591 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f27 | [사실] | IoT 엣지용 메시지 브로커 성능 비교 연구(arXiv 2603.21600)는 네트워크 장애 조건에서 QoS 0 의 메시지 손실이 약 6.3~6.6% 였고 QoS 1·2 는 손실이 없었다고 보고했다(저자 실험 조건). | ref-601 | 아니오 | medium | 2026-03 | 예외·성과 | 원문 미열람 |
| f28 | [추정] | VDA 5050 이 기반 경로 실행과 동작 상태 보고를 로봇에 맡기고 관제에는 식별자 규칙과 상태 해석을 맡기므로, ROP 가 직접 맡을 신뢰성 기능은 상위 요청의 중복 판별, 명령 식별자 발급·보존, 작업 상태 기계 유지, 시간 초과 판정, 재시작 뒤 상태 복원이 될 것으로 보인다. | ref-031, ref-591, ref-590 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [추정] | 연계 대상: 로봇 내부의 동작 재시도, 로컬 회피, 정지 방식(선 유도 로봇의 다음 노드 정지 등)은 로봇 제조사 영역이며, ROP 는 VDA 5050 의 RETRIABLE·cancelOrder 상태처럼 그 결과를 보고받아 판단하는 쪽에 가깝다. | ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f30 | [추정] | VDA 5050 3.0.0 은 상태 메시지가 오지 않을 때 관제가 할 일을 규정하지 않으므로, 시간 초과 기준과 그 뒤 처리(재질의·일시정지·사람 호출)는 30초 상태 주기와 CONNECTION_BROKEN 알림을 입력으로 ROP 가 따로 정해야 할 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |
| f31 | [추정] | VDA 5050 동작 상태, ROS 2 액션 목표 상태, Open-RMF 작업 상태, OPC UA 프로그램 상태, PackML 상태는 일시정지·중단·취소·실패의 구분이 서로 달라, ROP 가 상위 시스템에 되돌릴 공통 작업 상태로 옮기려면 대응 규칙이 필요할 것으로 보인다. | ref-031, ref-588, ref-111, ref-594, ref-595 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f32 | [추정] | 분류 원문 질문의 상황에서 관제가 응답이 끊긴 적치 운반 주문을 같은 주문 id·같은 주문 갱신 id·같은 내용으로 다시 보내면 VDA 5050 로봇은 이를 무시하므로 로봇 단계의 이중 실행은 막을 수 있으나, 상위 시스템이 새 요청으로 다시 보내 ROP 가 새 주문 id 를 발급하면 이 보호가 작동하지 않을 것으로 보인다. | ref-031, ref-592 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 아니오 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 예 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 아니오 |
| ref-588 | ROS 2 Design | Actions (ROS 2 Design) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/actions.html | 아니오 |
| ref-589 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 아니오 |
| ref-590 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json | 아니오 |
| ref-591 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp | 아니오 |
| ref-592 | IETF HTTPAPI Working Group (Jena, J., & Dalal, S.) | The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md | 아니오 |
| ref-306 | OASIS | MQTT Version 5.0 (OASIS Standard) | 미확인 | 표준 | medium | 2026-09-25 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 예 |
| ref-594 | OPC Foundation | OPC 10000-10 UA Part 10: Programs - 4.2.4 Program states | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4 | 예 |
| ref-595 | ISA | ISA-TR88.00.02-2022, Machine and Unit States: An implementation example of ISA-88.00.01 | 2022 | 표준 | medium | 2026-09-25 | https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp | 예 |
| ref-596 | Colledanchise, M., & Ögren, P. | Behavior Trees in Robotics and AI: An Introduction | 2017-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1709.00084 | 예 |
| ref-597 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/retry_node.h | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h | 아니오 |
| ref-598 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/timeout_node.h | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/timeout_node.h | 아니오 |
| ref-599 | Garcia-Molina, H., & Salem, K. | Sagas | 1987 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/38713.38742 | 예 |
| ref-600 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/issues/224 | 예 |
| ref-601 | arXiv 2603.21600 저자(미확인) | Benchmarking Message Brokers for IoT Edge Computing: A Comprehensive Performance Study | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.21600 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3(왜 중요한가): f4·f5·f14·f27·f32 — 무선 전송 불확실성, 재시작 시 작업 유실, 중복 처리 위험. 섹션 4(핵심 개념과 용어): f1·f2(주문 갱신 id), f8(목표 id·목표 상태), f15(멱등성 키), f5(마지막 유언), f18(deadline·liveliness), f25(사가·보상). 섹션 5(현장 시나리오): f32·f10(적치 운반 재전송, 예외·성과), f26(출하 취소 후 되돌림), f3·f12(완료·인계). 섹션 6(대표 접근법과 기술): 식별자 기반 중복 무시(f1·f2·f17), 멱등성 키(f15), 상태 기계(f8·f20·f21·f31), 시간 초과·활성 감지(f5·f18·f23·f30), 재시도(f7·f23), 상태 백업·복원(f13·f14·f19), 보상(f25·f26). 섹션 7(관련 표준·프레임워크·오픈소스): VDA 5050(f1~f7), ROS 2 액션·QoS·관리형 노드(f8·f18·f19), Open-RMF(f9·f11·f12·f13), MQTT 5.0(f16), IETF 초안(f15), OPC UA Programs·PackML·ISA-95 Job Control(f20·f21·f22), BehaviorTree.CPP(f23). 섹션 8(대표 연구와 자료): f24·f25·f27. 섹션 9(ROP가 직접 맡는 것과 외부와 연계하는 것): f28(직접 범위), f29(연계 대상), f17(통신 계층 보장과 응용 계층 구분). 섹션 10(다른 연구영역과의 연결): 1. 주문·업무 시스템 연계(f22), 2. 공정·워크플로 모델링(f31, oq-014), 9. 로봇·제조사 관제 연동(f1~f7, f31, oq-033), 11. 분산 시스템·통신·컴퓨팅 구조(f5·f16·f18·f27), 19. 모니터링·이상 탐지·원인 분석(f12·f31), 20. 예외 복구·재계획·업무 연속성(f7·f13·f26, oq-021). 섹션 11(열린 질문): 기존 oq-014·oq-021·oq-033 과 이번 새 질문. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 멱등성 키 | Idempotency Key | 클라이언트가 요청마다 만든 고유 값으로, 서버가 같은 요청의 재시도를 알아보고 한 번만 처리하게 하는 데 쓰인다. |
| 사가 | Saga | 오래 걸리는 작업을 작은 단계의 순서로 나누고 단계마다 보상 동작을 두어, 전부 완료되거나 부분 실행을 보상하게 하는 트랜잭션 구성 방식이다. |
| 마지막 유언 메시지 | Last Will (MQTT) | MQTT 클라이언트가 예기치 않게 끊기면 브로커가 대신 발행하도록 미리 등록해 둔 메시지로, VDA 5050 은 이를 로봇 연결 끊김(CONNECTION_BROKEN) 알림에 쓴다. |
| 관리형 노드 | Managed Node (ROS 2 Lifecycle Node) | Unconfigured·Inactive·Active·Finalized 상태와 전이를 가져 감독 도구가 준비 확인·재시작·교체를 제어할 수 있는 ROS 2 노드이다. |

## 열린 질문

새로 생긴 질문:

- 상위 시스템 요청의 중복을 판별하는 키(멱등성 키나 상위 요청 id)를 ROP 가 얼마 동안 보존해야 하는가, 운반 작업의 재전송 가능 기간에 맞춘 만료 기준을 정한 표준이나 사례가 있는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 1. 주문·업무 시스템 연계 | 근거: f15 | 종류: 일반
- VDA 5050 로봇이 재부팅되면 받아 둔 주문을 유지하는지에 대한 규정이 명세에서 확인되지 않는데, 제조사 구현이나 공개 사례는 재부팅 뒤 주문·동작 상태를 어떻게 복원하거나 폐기하는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 9. 로봇·제조사 관제 연동 | 근거: f4 | 종류: 일반
- Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? | 관련 영역: 12. 명령·작업 실행의 신뢰성, 20. 예외 복구·재계획·업무 연속성 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 표준·오픈소스마다 발행 주체 한 곳의 자료이거나 같은 저장소 안의 파일
    - f14 Open-RMF 이슈 #224 원문 미열람, 작업 백업 기능의 배포판 반영 여부 미확인
    - f16 MQTT 5.0 명세 원문 미열람(검색 요약 기준)
    - f20·f21 OPC UA Part 10, ISA-TR88.00.02 원문 미열람
    - f22 ISA-95 Job Control 상태 기계 상태 이름과 Store 메서드의 중복 id 반환 코드(부속서 B.2) 미확인
    - f27 브로커 비교 연구의 실험 조건·저자 미확인
    - f30 VDA 5050 의 상태 미수신 시 관제 대응 규정 부재는 열람 도구 응답 기준이며 부재 확정 아님
    - 국내 학술·현장 자료: 명령 중복·재시작 복원을 다룬 한국 자료를 검색 2회로 찾지 못함
- 범위 경계 위반 의심:
    - f29: 로봇 내부 재시도·정지 방식은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이라 '연계 대상: '으로 표시함
    - f16·f27: MQTT 전달 보장·브로커 성능은 11. 분산 시스템·통신·컴퓨팅 구조와 겹치므로 12번 페이지에는 명령 중복 판단의 입력으로만 쓰도록 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-031·ref-125·ref-126·ref-127·ref-130(documentation.csv)·ref-282(ros2_documentation jazzy 원본), 신규 ref-588·ref-589·ref-590·ref-591·ref-592·ref-597·ref-598. ref-130 NodeSet2.xml 은 응답이 잘려 상태 이름·반환 코드를 확인하지 못했다. task_dispatch_response.json 은 404 로 열지 못해 서버의 작업 id 부여 방식은 finding 으로 내지 않았다. 나머지 신규 7건과 재사용 ref-111·ref-129 는 원문 미열람이라 신뢰도 상한 medium. 모든 finding 신뢰도 medium 이하, 교차 확인 0건. 검색 12회/30, 신규 출처 14건/15(ref-588~ref-601, 예약 구간 안), 재사용 8건. 한국어 검색 2회에서 쓸 만한 한국 자료를 찾지 못했다(벤더 블로그·AI 요약뿐이라 출처로 넣지 않음). 행동 트리 용어는 용어집에 이미 있어 후보로 내지 않았다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 기존 열린 질문 oq-014·oq-021·oq-033 은 이번 조사로 해결되지 않았다(공통 상태 매핑·되돌림 규칙 표준을 찾지 못함).
```
