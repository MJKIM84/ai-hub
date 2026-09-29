(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-07
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 4. 이기종 로봇 등록 (B. 로봇 온톨로지)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-869
- 새 출처 id 구간: ref-869 ~ ref-898 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-869 부터 순서대로 쓰고 ref-898 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-07/target.json

```json
{
  "run_id": "2026-09-29-07",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 99,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 4,
    "area_name": "4. 이기종 로봇 등록",
    "category": "B. 로봇 온톨로지",
    "category_letter": "B"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=4"
}
```

### docs/categories/robot-ontology/heterogeneous-robot-registration.md

```markdown
---
title: "4. 이기종 로봇 등록"
type: area
category: "B. 로봇 온톨로지"
area_no: 4
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 4. 이기종 로봇 등록

# 4. 이기종 로봇 등록

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

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

### docs/categories/robot-ontology/robot-capability-and-task-representation.md (요약)

```markdown
# 5. 로봇 능력·작업 표현

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 능력 표현**: 이동·계단·적재·도어 조작·충전·파지·점검 같은 능력을 매개변수·입출력·전제조건·제약·실패 모드와 함께 공통 모델로 표현한다
- **작업 유형·작업 요구 표현**: 배송·운반·인계·순찰·점검·조작 같은 작업 유형과 각 작업이 요구하는 능력·조건을 능력 모델과 같은 어휘로 표현한다
- **환경 조건과 능력 대조**: 층·문·승강기·계단·충전기 같은 공간 조건을 온톨로지에 함께 담아 로봇별로 지나갈 수 있는 곳과 쓸 수 있는 시설을 판단한다
- **표현 표준 정렬**: 능력·작업 표현을 로봇 온톨로지 표준(IEEE 1872 계열), VDA 5050 팩트시트, 자산 관리 셸 같은 기존 규격과 대응시킨다
- **온톨로지 저장·질의 기반**: 온톨로지를 저장하고 질의하는 기술(그래프 데이터베이스, RDF·OWL, SPARQL, JSON 스키마)을 고르고 성능을 확인한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md), [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 5번 영역 ‘로봇 능력·작업 온톨로지’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [옛 분류원문]

> 옛 질문: 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md (요약)

```markdown
# 6. 온톨로지 기반 시스템·로봇 연동

소속 대분류: B. 로봇 온톨로지 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]
```

### docs/categories/robot-ontology/ontology-verification-and-change-management.md (요약)

```markdown
# 7. 온톨로지 검증·변경 관리

소속 대분류: B. 로봇 온톨로지 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **온톨로지 검증**: 역량 질문, 원문 대조, 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)로 완전성과 정확성을 확인한다
- **온톨로지 버전·변경 관리**: 문서·펌웨어 개정에 따라 능력 정의의 버전을 관리하고, 영향받는 작업·현장을 찾아 다시 검증한다

## 2. 핵심 질문

온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 868건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 227개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
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
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
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

### docs/open-questions.md (요약: 대상 영역 [4] 에 걸린 1건 / 전체 146건)

```markdown
- oq-128 [열림] 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? (영역 10, 4, 21)
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

### runs/2026-09-29-06/research.md

```markdown
# 리서치 브리프 2026-09-29-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-06 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 13. 대화형 기능의 신뢰·기반 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 프롬프트 주입·탈옥·승인 피로·모델 대체 용어 없음(환각·과도한 에이전시·사람 참여 루프·모델 컨텍스트 프로토콜·구조화 출력·제약 디코딩·등각 예측·불확실도 정렬·자동화 편향·역할 기반 접근 통제·감사 추적·pass^k·사용자 시뮬레이터는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 오해석 방지·권한·모델 연결·평가·화면 연동·음성 여섯 갈래 모두 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — OWASP LLM Top 10, MCP 보안 원칙, EU AI Act 기록 조항, 국내 안내서(TTA·개인정보위) 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 8~12번 채팅 영역, 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 6건(oq-125, oq-127, oq-133, oq-136, oq-139, oq-141) 미반영
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
2. 언어 모델이 없는 물품·장소를 지어내거나 외부 입력(프롬프트 주입·탈옥)에 조종당해 로봇 동작으로 이어지는 위협은 무엇이 보고되었고, 근거 표시·불확실도 보정·사전 검증 같은 방어는 어떤 것이 있는가? (섹션 3·4·6 겨냥)
3. 사용자별로 대화로 지시할 수 있는 로봇·구역·작업 범위를 제한하고 승인 관문을 두는 권한 설계와 승인 부담(승인 피로)은 어떻게 다뤄지는가? (섹션 6·11 겨냥, oq-139·oq-141 관련)
4. 대화 기록의 보존·보호와 자동 로그에 관한 규제·안내서(EU AI Act, 국내 개인정보위·TTA 안내서)는 무엇을 요구하는가? (섹션 7·9 겨냥)
5. 언어 모델 공급자를 고르고 바꾸며 장애 때 임의 대체를 막으려면 무엇을 알아야 하는가(게이트웨이의 모델 대체·희석)? (섹션 6·11 겨냥)
6. 대화형 기능의 해석·분해 정확도, 질문 횟수, 신뢰성(반복 시행)을 재는 공개 벤치마크·지표는 무엇인가? (섹션 6·8 겨냥, oq-125·oq-127 관련)
7. 음성·다국어·현장 단말 대화와 화면 선택–대화 연동을 다룬 연구·현장 사례(현장 유형 명시)와 국내 자료는 무엇이며, ROP가 직접 맡을 것과 음성 인식·모델 공급자에 맡길 것의 경계는 어디인가? (섹션 5·9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리하고, 과도한 에이전시를 언어 모델 기반 시스템에 필요 이상의 기능·권한·자율이 주어진 상태로 설명한다. | ref-855 | 아니오 | medium | 2025 | — | — |
| f2 | [사실] | 모델 컨텍스트 프로토콜(MCP) 명세 2025-06-18 판의 '보안과 신뢰·안전' 절은 호스트가 어떤 도구든 호출하기 전에 사용자의 명시적 동의를 얻어야 하고, 도구 설명·주석은 신뢰할 수 있는 서버에서 온 것이 아니면 신뢰하지 말아야 하며, 프로토콜 자체는 이 원칙을 강제할 수 없으므로 구현자가 동의·인가 흐름을 응용 프로그램에 만들어야 한다고 적는다. | ref-856 | 아니오 | medium | 2025-06-18 | 시작 조건 | — |
| f3 | [사실] | Robey 외(2024)의 RoboPAIR 는 언어 모델로 제어되는 로봇을 탈옥시키는 알고리즘으로, 자율주행 언어 모델(화이트박스)·GPT-4o 계획기를 단 Clearpath Jackal(그레이박스)·Unitree Go2 로봇 개(블랙박스)의 세 설정에서 100% 공격 성공률을 보고했고, 배치된 상용 로봇 시스템에 대한 첫 탈옥 성공이라고 밝혔다. | ref-857 | 아니오 | medium | 2024-11-09 | 예외·성과 | — |
| f4 | [사실] | Huang 외(2025)의 서베이 '언어 모델 제어 로봇의 신뢰'는 추상 추론과 물리 동작 사이의 체화 격차(embodiment gap)를 중심으로 탈옥·백도어·다중 모달 프롬프트 주입을 포함한 공격 벡터 분류와, 형식 안전 명세·런타임 강제·다중 언어 모델 감독·프롬프트 강화를 포함한 방어 분류, 그리고 강건성 평가용 데이터셋·벤치마크를 정리했다. | ref-859 | 아니오 | medium | 2025-12-17 | — | — |
| f5 | [사실] | 서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 언어 모델에 대한 프롬프트 주입·탈옥이 도구 호출이나 로봇의 물리 동작으로 이어지는 위협을 각각 보고해, 언어 모델의 오해석뿐 아니라 외부 조작이 잘못된 실행의 원인이 된다는 점이 한 곳 이상에서 확인된다. | ref-855, ref-857, ref-859 | 예 | medium | 2025-12-17 | — | — |
| f6 | [추정] | MCP 가 도구 호출 전 사용자 동의를 호스트의 책임으로 두고 프로토콜이 강제하지 못한다는 점(f2)과 탈옥이 배치된 로봇에서도 성공한다는 점(f3·f5)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이나 도구 서버 안이 아니라 ROP 쪽 호스트에 승인 관문을 두고, 도구 설명·검색 문서·현장 입력을 신뢰하지 않는 입력으로 다루어야 지켜질 것으로 보인다. | ref-856, ref-857, ref-855 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f7 | [사실] | VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리로 옮긴 뒤 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 검증 모듈로, 승인 전에 계획을 자동으로 거르는 층의 사례다. | ref-753 | 아니오 | medium | 2025-07-07 | 제약 | 원문 미열람 |
| f8 | [사실] | Li 외(NeurIPS 2024 데이터셋·벤치마크 트랙, 구두 발표)의 Embodied Agent Interface 는 체화 의사결정 과제를 목표 해석·하위 목표 분해·행동 순서화·전이 모델링의 네 모듈로 나누고, 최종 성공률 대신 환각 오류·어포던스 오류·여러 계획 오류를 구분하는 세분화 지표로 언어 모델을 평가한다. | ref-858 | 아니오 | medium | 2025-01-19 | — | — |
| f9 | [사실] | Yao 외(2024)의 τ-bench 는 언어 모델이 흉내 내는 사용자와 도구·정책 지침을 가진 에이전트의 대화를 시뮬레이션해 대화 종료 시 데이터베이스 상태를 목표 상태와 비교하고, 같은 과제를 여러 번 시행해 모두 성공할 확률 pass^k 로 신뢰성을 재며, GPT-4o 같은 최신 함수 호출 에이전트도 과제 성공률 50% 미만·소매 도메인 pass^8 25% 미만이라고 보고했다. | ref-738 | 아니오 | medium | 2024-06-17 | 예외·성과 | — |
| f10 | [사실] | KnowNo(Ren 외, CoRL 2023)는 등각 예측으로 언어 모델 계획기의 불확실도를 보정해 후보 행동 집합이 하나로 좁혀지면 실행하고 여러 개가 남으면 사람에게 되묻는 틀로, 목표 성공률을 보장하면서 도움 요청을 줄였다고 보고했다. | ref-351 | 아니오 | medium | 2023-09-04 | 시작 조건 | 원문 미열람 |
| f11 | [사실] | Mullen·Manocha(2024, 2025 개정)의 LBAP 는 베이즈 추론으로 장면 근거(scene grounding)와 세계 지식을 함께 반영해 로봇의 확신도를 보정함으로써 언어 모델 환각에 대응하며, 실제 환경 시험에서 성공률 70% 조건에서 이전 방법보다 사람 도움 요청률을 33% 넘게 줄였다고 보고했다. | ref-864 | 아니오 | medium | 2025-06-17 | 예외·성과 | — |
| f12 | [사실] | 서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, '불확실도 보정 기반 되묻기'로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다. | ref-351, ref-864 | 예 | medium | 2025-06-17 | 시작 조건 | — |
| f13 | [추정] | 세분화 오류 지표(f8), 반복 시행 신뢰성 pass^k(f9), 성공률 대비 도움 요청률(f10·f11)을 함께 보면, 이 영역의 '대화형 기능 평가'는 해석·분해 정확도를 오류 유형별로 나누고 같은 과제를 여러 번 시행한 신뢰성과 질문 횟수를 성공률과 짝지어 재는 방식으로 구성할 수 있으나, 로봇 지도 작성·로봇 구성 대화에 특화된 벤치마크는 이번 조사에서 확인되지 않았다. | ref-858, ref-738, ref-864 | 아니오 | low | 2026-09-29 | — | — |
| f14 | [사실] | Laban 외(2025)는 20만 건 이상의 시뮬레이션 대화에서 언어 모델의 다중 턴 성능이 단일 턴보다 평균 39% 낮았고 원인이 초기 가정에 대한 과도한 의존 같은 신뢰성 저하라고 보고해, 대화가 길어질수록 오해석 위험이 커진다는 근거가 된다. | ref-840 | 아니오 | medium | 2025-05-09 | — | 원문 미열람 |
| f15 | [사실] | Michael·Roesner(2026)는 AI 에이전트의 사용자 수준 권한 제안 21건과 상용 에이전트 5종을 조사해 권한 정책 명세(자연어·권한 라벨·고정 선택지·구조화 제약·임의 규칙)와 강제 방식(에이전트 자율 준수·언어 모델 가드레일·결정적 위반 탐지·실시간 사용자 승인·형식 검증 강제)의 분류를 만들고, 상용 에이전트가 부담이 큰 실시간 승인과 투명성 없는 언어 모델 자동 검토 사이의 선택을 강요하며 낮은 사용자 부담·형식 근거·결정적 강제를 함께 갖춘 학술 시스템은 21건 중 하나도 없다고 보고했다. | ref-868 | 아니오 | medium | 2026-07-20 | 제약 | — |
| f16 | [사실] | Li 외(2025)의 다중 로봇 언어 모델 서베이는 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머물고 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다고 지적해, 승인 관문의 검토 부담이 열린 문제임을 뒷받침한다. | ref-165 | 아니오 | medium | 2025-02-06 | 제약 | 원문 미열람 |
| f17 | [추정] | 권한 강제 방식의 분류(f15)와 승인 부담 미정량화(f16), 호스트 책임의 동의 원칙(f2)을 함께 보면, 이 영역의 '대화 권한'은 프롬프트 안내가 아니라 도구 호출 수준에서 사용자·로봇·구역·작업 범위를 결정적으로 검사하는 정책으로 두고, 실행 전 승인은 위험도가 낮은 조회는 자동 허용하고 로봇을 움직이는 요청만 사람이 승인하는 식으로 단위를 나누어야 승인 피로를 줄일 수 있을 것으로 보이나, 로봇 대수·계획 크기에 따른 승인 단위를 정한 연구는 확인되지 않았다. | ref-868, ref-165, ref-856 | 아니오 | low | 2026-09-29 | 제약 | — |
| f18 | [사실] | EU AI Act 제12조(기록 보관)는 고위험 AI 시스템이 수명 기간 내내 사건을 자동으로 기록(로그)할 수 있어야 하고, 로그가 위험 상황 식별·시장 출시 후 모니터링·운영 모니터링에 필요한 사건을 담아 의도된 목적에 맞는 추적 가능성을 보장해야 한다고 규정한다. | ref-863 | 아니오 | medium | 2026-09-29 | 완료·인계 | — |
| f19 | [사실] | 개인정보보호위원회는 2025년 8월 '생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서'를 내어(공식 사이트 게시 2025-08-22) 생성형 AI 수명주기 각 단계에서 고려할 개인정보 처리·보호 이슈를 체계화하고 법적 기준과 안전조치를 제시했다. | ref-862 | 아니오 | medium | 2025-08 | — | — |
| f20 | [사실] | 과학기술정보통신부와 한국정보통신기술협회(TTA)의 '2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야'는 2024년 2월 발간되어 웹 문서로 2025-08-14까지 갱신되었고, 인공지능 서비스·제품 개발 과정의 기술적 신뢰성 확보 방안을 다루며 2024년에는 생성 AI 기반 서비스 분야 안내서가 함께 나왔다. | ref-860 | 아니오 | medium | 2025-08-14 | — | — |
| f21 | [추정] | 대화 기록의 보존·보호 요구는 EU AI Act 의 자동 로그 조항(f18), 국내 개인정보위 안내서(f19), TTA 신뢰성 안내서(f20)에 근거를 둘 수 있으나, ROP 의 로봇 대화 기능이 고위험·고영향 AI 에 해당하는지와 로그 항목·보존 기간을 어떻게 정할지는 확인되지 않았다. | ref-863, ref-862, ref-860 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f22 | [사실] | Zhang·Zhang·Qin(2026)의 IRIS 는 언어 모델 게이트웨이가 광고한 모델 대신 더 싼 모델을 내보내는 모델 대체(substitution)와 일부 요청만 약속한 백엔드로 보내는 라우팅 희석(dilution)을 응답 텍스트만으로 감사하는 방법으로, 상용 라이브러리에서 희석을 평균 탐지력 0.85·오탐률 0.017 로 잡고 교차 제공자 감사에서 문제 모델 쌍 15개 중 14개를 표시했다고 보고했다. | ref-865 | 아니오 | medium | 2026-07-23 | 예외·성과 | — |
| f23 | [추정] | 게이트웨이의 무단 모델 대체·희석이 실제로 관측된다는 점(f22)과 OWASP 가 공급망을 위험 항목으로 둔 점(f1)을 함께 보면, 이 영역의 '모델 장애 때 임의로 다른 모델로 넘기지 않는다'는 요구는 ROP 가 요청·응답마다 실제 제공 모델 식별자를 기록하고 대체를 사전에 정한 정책으로만 허용하며 게이트웨이 계층의 대체를 감사하는 절차로 구현해야 할 것으로 보인다. | ref-865, ref-855 | 아니오 | low | 2026-09-29 | 제약 | — |
| f24 | [사실] | Li 외(2026)의 서베이는 로봇 시스템의 음성 인식이 온라인 API 서비스에만 의존해야 하는지를 물으며 Whisper 같은 심층 학습 모델까지의 발전과 ROS 기반·클라우드 기반·혼합 배치 전략, 다양하고 동적인 환경에서 강건한 음성 인식을 배치하는 과제를 정리했다. | ref-866 | 아니오 | medium | 2026-07-13 | 수행 자원 | — |
| f25 | [사실] | Nandkumar·Peternel(Frontiers in Robotics and AI, 2025-04-29)은 네덜란드 슈퍼마켓의 상품 안내·회수 로봇을 위한 음성 대화 인터페이스에서 네 가지 음성 인식 기술을 영어·네덜란드어와 성별 집단(참가자 40명)으로 비교해 Whisper 가 가장 낮은 단어 오류율을 보였고, 질의 분류기와 상·중·하 세 층의 언어 모델이 1,612개 상품 데이터베이스에 근거해 답하게 한 다층 구조가 참가자 16명 평가에서 GPT-4 Turbo 보다 13개 항목 중 4개에서 유의하게 높았다고 보고했다. | ref-869 | 아니오 | medium | 2025-04-29 | 상업 시설 / 작업 대상 | — |
| f26 | [사실] | van Dam(2025)의 다중 모달 GUI 아키텍처는 응용 프로그램의 화면 이동 그래프와 의미를 모델 컨텍스트 프로토콜로 노출하고 뷰모델이 현재 보이는 화면에 적용되는 도구와 전역 도구를 언어 모델에 제공해 음성 입력과 시각 인터페이스의 정렬과 양쪽 모달리티의 일관된 피드백을 목표로 하며, 참조 구현(langbar)을 공개하고 로컬 배치 가능한 개방 가중치 모델이 전체 정확도에서 선도 상용 모델에 근접한다고 보고했다. | ref-861 | 아니오 | medium | 2025-10-09 | — | — |
| f27 | [추정] | 화면 상태와 가능한 동작을 도구로 노출해 음성·대화와 화면을 맞추는 구조(f26)와 화면 선택을 대화에 반영하는 이 영역의 요구를 함께 보면, 지도에서 고른 장소·로봇을 대화가 참조하고 대화로 바꾼 값이 편집 화면에 바로 보이게 하려면 편집기의 현재 선택·화면 상태를 언어 모델에 자원으로 주고 변경은 같은 상태 저장소를 거치게 하는 구조가 필요할 것으로 보이나, 로봇 지도·시나리오 편집기에 특화된 공개 구현은 확인되지 않았다. | ref-861, ref-856 | 아니오 | low | 2026-09-29 | — | — |
| f28 | [추정] | 확인한 자료를 종합하면 13. 대화형 기능의 신뢰·기반에서 ROP가 직접 맡을 범위는 해석 결과에 근거(장소·물품·문서 식별자)를 붙이고 불확실한 항목만 되묻는 흐름, 도구 호출 수준의 권한 검사와 실행 전 승인 관문, 대화·도구 호출·실제 제공 모델의 기록, 모델 공급자 연결·교체 정책, 오류 유형별 평가 시나리오이며, 음성 인식 엔진의 정확도와 언어 모델 자체의 안전 정렬은 연계 대상으로 두는 것이 분류 원문 19장의 경계에 맞을 것으로 보인다. | ref-856, ref-868, ref-865, ref-866, ref-858 | 아니오 | low | 2026-09-29 | — | — |
| f29 | [추정] | 연계 대상: 음성 인식 모델의 소음·다국어 강건성(Whisper 등)과 언어 모델 공급자의 탈옥 방어·안전 학습은 분류 원문 19장의 로봇 자체 지능 및 외부 도구 쪽이며, 이종 제조사를 잇는 ROP 는 인식 결과의 확인 절차와 모델 출력의 검증·승인·기록을 맡고 인식·모델 내부 성능은 공급자에게 맡겨야 할 것으로 보인다. | ref-866, ref-869, ref-857 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f30 | [추정] | 불확실도 보정·되묻기(KnowNo, LBAP), 세분화 벤치마크(Embodied Agent Interface), 탈옥 공격·방어(RoboPAIR, Huang 외)는 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 이 영역과 함께 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 영역, 권한·기록은 51. 인증·권한·격리와 52. 통신 보호·위협 관리·감사, 대화 기록의 개인정보는 53. 개인정보·영상 데이터, 평가는 54. 시험·형식 검증·벤치마크에 연결해야 한다. | ref-858, ref-857, ref-863 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-855 | OWASP GenAI Security Project | OWASP Top 10 for LLM Applications 2025 | 2025 | 업계 보고서 | medium | 2026-09-29 | https://genai.owasp.org/llm-top-10/ | 아니오 |
| ref-856 | Model Context Protocol (Anthropic 주도 오픈소스 프로젝트) | Specification — Model Context Protocol (2025-06-18) | 2025-06-18 | 오픈소스 문서 | high | 2026-09-29 | https://modelcontextprotocol.io/specification/2025-06-18 | 아니오 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 2024-11-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.13691 | 아니오 |
| ref-858 | Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks) | Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making | 2025-01-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.07166 | 아니오 |
| ref-859 | Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R. | Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges | 2025-12-17 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2601.02377 | 아니오 |
| ref-860 | 과학기술정보통신부·한국정보통신기술협회(TTA) | 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기) | 2024-02 | 정부·연구기관 | high | 2026-09-29 | https://tta-trustworthy-ai.gitbook.io/general | 아니오 |
| ref-861 | van Dam, H. G. W. | A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants | 2025-10-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.06223 | 아니오 |
| ref-862 | 개인정보보호위원회 | 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) | 2025-08 | 정부·연구기관 | medium | 2026-09-29 | https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836 | 아니오 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 미확인 | 정부·연구기관 | high | 2026-09-29 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 아니오 |
| ref-864 | Mullen, J. F., Jr., & Manocha, D. | Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners | 2025-06-17 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.13198 | 아니오 |
| ref-865 | Zhang, Y., Zhang, Z.-H., & Qin, H. | Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways | 2026-07-23 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.20860 | 아니오 |
| ref-866 | Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E. | Is That All We Can Do? Relying on Online API Services: A Survey of Localized Speech Recognition Model Integration in Robotic Systems | 2026-07-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.11792 | 아니오 |
| ref-738 | Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra) | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 2024-06-17 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.12045 | 아니오 |
| ref-868 | Michael, A. E., & Roesner, F. | How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement | 2026-07-20 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.13718 | 아니오 |
| ref-869 | Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI | Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents | 2025-04-29 | 논문 | high | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/ | 아니오 |
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-09-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-840 | Laban, P., Hayashi, H., Zhou, Y., & Neville, J. | LLMs Get Lost In Multi-Turn Conversation | 2025-05-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.06120 | 예 |
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 2025-02-06 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2502.03814 | 예 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.05118 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f3·f5(탈옥이 배치된 로봇의 물리 동작으로 이어짐), f14(다중 턴에서 신뢰성 저하), f9(도구 에이전트의 낮은 반복 신뢰성), f15·f16(승인 부담과 자동 검토의 불투명성) / 섹션 4: f1(프롬프트 주입·과도한 에이전시), f3(탈옥), f10·f11(불확실도 보정·되묻기), f8(환각·어포던스·계획 오류), f9(pass^k), f15(권한 명세·강제 방식, 승인 피로), f22(모델 대체·라우팅 희석) / 섹션 5: 상업 시설 — f25(슈퍼마켓 로봇의 음성 대화, 다국어 음성 인식 비교, 상품 DB 근거 응답; 네덜란드 사례임을 명시), 그 밖의 현장 유형 사례는 이번 조사에서 확인되지 않음을 서술 / 섹션 6: 오해석 방지·근거 표시 f10·f11·f12·f7·f25(불확실한 항목만 되묻기, 실행 전 자동 검증, DB 근거 응답), 권한·승인 f2·f6·f15·f17, 모델 연결·교체 f22·f23, 평가 f8·f9·f13, 화면 연동 f26·f27, 음성·다국어 f24·f25 / 섹션 7: f1(OWASP LLM Top 10 2025), f2(MCP 명세 보안 원칙), f18(EU AI Act 제12조), f19(개인정보위 생성형 AI 안내서), f20(TTA 신뢰할 수 있는 AI 개발 안내서), f26(langbar 참조 구현), f8·f9(공개 벤치마크) / 섹션 8: f3, f4, f8, f9, f10, f11, f14, f15, f16, f22, f24, f25, f26, 국내 f19·f20 / 섹션 9: f28(직접 범위: 근거 표시·되묻기, 권한 검사·승인 관문, 기록, 모델 정책, 평가), f29(연계 대상: 음성 인식 엔진 성능, 언어 모델 공급자의 안전 정렬) / 섹션 10: 8. 채팅으로 맵 작성·9. 채팅으로 시나리오 구성·10. 채팅으로 로봇 구성·11. 채팅으로 실제 상황 시뮬레이션 재현·12. 채팅으로 업무 지시·오케스트레이션(f6·f13·f27, 이 영역이 다섯 대화 영역의 공통 기반), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f30, 교차 규칙), 51. 인증·권한·격리(f15·f17), 52. 통신 보호·위협 관리·감사(f1·f3·f4·f18), 53. 개인정보·영상 데이터(f19·f21), 54. 시험·형식 검증·벤치마크(f8·f9), 20. 로봇·제조사 관제 연동(f2·f6 승인 관문 위치), 48. 안전·위험 관리(f3), 57. 자산·소프트웨어 수명주기 관리(f23 모델 교체), 64. 상업 시설(f25) / 섹션 11: 기존 oq-125·oq-127(f13 으로 부분 진전, 미해결), oq-133·oq-136(미조사), oq-139(f15·f16·f17 로 부분 진전, 미해결), oq-141(f2·f6 으로 부분 진전, 공개 구현 미확인)과 open_questions_new 4건. 다음 실행 후보: 52. 통신 보호·위협 관리·감사 페이지에 f1·f3·f4 반영, 51. 인증·권한·격리 페이지에 f15 반영, 54. 시험·형식 검증·벤치마크 페이지에 f8·f9 반영, 12. 채팅으로 업무 지시·오케스트레이션 페이지에 f2·f6 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 프롬프트 주입 | Prompt Injection | 사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다. |
| 탈옥 | Jailbreak | 언어 모델의 안전 제한을 우회하도록 유도하는 입력 기법으로, 로봇을 제어하는 언어 모델에서는 유해한 물리 동작을 끌어내는 데 쓰일 수 있다. |
| 승인 피로 | Approval Fatigue (Consent Fatigue) | 에이전트의 동작마다 사람에게 승인을 묻는 방식이 반복되어 사용자가 검토 없이 허용하거나 자동 승인으로 바꾸게 되는 현상으로, 실시간 승인 관문의 실효성을 떨어뜨린다. |
| 모델 대체·라우팅 희석 | Model Substitution / Routing Dilution | 언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다. |

## 열린 질문

새로 생긴 질문:

- ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 59. 법·규제·보험·라이선스, 53. 개인정보·영상 데이터 | 근거: f21 | 종류: 일반
- 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 52. 통신 보호·위협 관리·감사, 48. 안전·위험 관리 | 근거: f4 | 종류: 일반
- 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터 | 근거: f22 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 60. 노동·수용성·접근성, 61. 물류창고 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 2
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f19 개인정보위 안내서 PDF 원문 미열람(smartcity.go.kr 사본 ECONNRESET 뒤 404, pipc.go.kr ECONNRESET, kisa.or.kr 인증서 오류) — 4단계 구성·AI 에이전트 관련 내용은 검색 결과 요약에서만 보여 claim 에 넣지 않음
    - f20 TTA 안내서의 개발 요구사항 15개·검증항목 67개 수치는 검색 결과 요약에만 있고 연 페이지에 없어 claim 에 넣지 않음; 생성 AI 기반 서비스 분야 페이지의 세부 검증항목도 요약 도구 응답이 불명확해 인용하지 않음
    - f18 EU AI Act 조문 게재 페이지에 발행일·적용일 표시 없음(published null)
    - f8 Embodied Agent Interface 의 시뮬레이터·모델별 결과 수치는 초록에 없어 미확인
    - f24 음성 인식 서베이의 소음·다국어 수치는 초록에 없어 미확인
    - f3 RoboPAIR 의 방어 제안은 초록에 없어 미확인
    - f12·f5 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - 산업 현장 음성 제어 사례(ScienceDirect·SSRN 게재 'LLM-driven agent for speech-enabled control of industrial robots', 눈게 검사)는 403 으로 열지 못해 넣지 않음
    - SMaRTAban(영어·슬로바키아어 음성 제어 사족 로봇, Springer)은 인증 리다이렉트로 열지 못해 넣지 않음
    - CURE(arXiv 2510.08044, 결합 불확실도 추정)는 열었으나 되묻기·실행 결정을 초록이 밝히지 않아 출처 상한 때문에 제외
    - OpenTelemetry GenAI 시맨틱 규약(도구 호출·에이전트 스팬 기록)은 검색 결과에서만 확인했고 출처 상한으로 넣지 못함 — 대화·도구 호출 기록 형식의 후보
    - MiniScope(arXiv 2512.11147, 도구 호출 최소 권한)는 열었으나 출처 상한으로 제외(f17 의 결정적 권한 강제 근거로는 ref-868 만 씀)
    - oq-139·oq-141 은 f15·f16·f17·f2·f6 으로 부분 진전만 있고 승인 단위를 정한 연구나 공개 구현은 확인하지 못해 해결 제안하지 않음
    - oq-133·oq-136 은 이번 실행에서 조사하지 않음
- 범위 경계 위반 의심:
    - f29: 음성 인식 엔진의 소음·다국어 성능과 언어 모델 공급자의 안전 학습은 분류 원문 19장의 로봇 자체 지능·외부 도구 쪽이므로 '연계 대상: '으로 표시함
    - f3: RoboPAIR 의 자율주행 언어 모델 사례는 로봇 자체 지능 수준의 공격이므로 위협 근거로만 제안하고 ROP 직접 범위로 서술하지 않음
    - f18·f19·f20: 법·규제·안내서 내용은 59. 법·규제·보험·라이선스와 53. 개인정보·영상 데이터의 범위와 겹치므로 이 영역에서는 대화 기록 보존·보호 요구의 근거로만 제안함
    - f9·f15: 로봇이 아닌 일반 도구 에이전트 연구는 평가 지표·권한 설계의 선례로만 제안함
    - f25: 슈퍼마켓 안내·회수 로봇 사례는 다중 로봇 오케스트레이션이 아니므로 음성·다국어·근거 응답 사례로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-855~ref-869, 예약 구간 안) 상한 도달로 위 미확인 항목의 후보 출처(OpenTelemetry GenAI 규약, MiniScope, CURE, 산업 음성 제어 사례)를 넣지 못했다. 원문 열람 15건(webfetch 15; ref-868 은 arXiv HTML 전문, ref-869 는 PMC 전문, 나머지 논문은 arXiv 초록 페이지), 재사용 4건(ref-351·ref-840·ref-165·ref-753, 이전 브리프 2026-09-29-04·05 의 값 그대로, 이번에 다시 열지 않음). 이전 실행 2026-09-29-05 가 ref-855~ref-862 로 낸 출처(HMCF, ETRI 동향, ROSA, OSRA MCP 세션 등)는 이번 실행의 예약 구간과 번호가 겹치고 참고문헌 목록 입력(0건 요약)에 없어 재사용하지 않았으며, 그 가운데 OSRA Interop SIG MCP 세션(oq-141 근거)은 이번 finding 에 넣지 않았다 — 퍼블리셔가 URL 로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 2건(f5: OWASP·Robey 외·Huang 외, f12: KnowNo·LBAP — 모두 발행 주체가 다름). 모든 finding 신뢰도 medium 이하(high 신뢰도 출처 ref-856·ref-860·ref-863·ref-869 는 각각 단일 출처 finding 에만 쓰임). 분류 원문 핵심 질문(해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면)에는 f2·f6(호스트 쪽 승인 관문과 신뢰하지 않는 입력 처리), f7·f10·f11·f12(실행 전 자동 검증과 불확실도 보정 되묻기), f15·f17(도구 호출 수준의 결정적 권한 강제), f18·f21(자동 기록), f22·f23(모델 대체 감사)로 답했으며 결론은 '모델 밖의 검증·승인·권한·기록 층이 필요하고 승인 단위와 부담은 아직 정량화되지 않았다'는 추정(f6·f13·f17·f23·f28)이다. 현장 유형: 상업 시설(f25, 네덜란드 슈퍼마켓 연구)만 확인했고 물류창고·제조 공장·병원·가정·실외 사례는 없다. 국내 자료는 TTA 안내서(f20)와 개인정보위 안내서(f19) 두 건이며 국내 로봇 대화 기능 사례는 찾지 못했다. L. AI·학습 기술 관련 finding(f3·f4·f8·f10·f11·f30)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처 없음(OWASP 는 업계 보고서, MCP 명세는 오픈소스 문서로 분류). 용어집에 이미 있는 환각·과도한 에이전시·사람 참여 루프·모델 컨텍스트 프로토콜·구조화 출력·제약 디코딩·등각 예측·불확실도 정렬·자동화 편향·역할 기반 접근 통제·감사 추적·pass^k·사용자 시뮬레이터·명확화 질문은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음.
```

### runs/2026-09-29-05/research.md

```markdown
# 리서치 브리프 2026-09-29-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-05 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 사전 실행 계획 검증·감독 제어·실패 설명·로봇–작업 적합도 행렬 용어 없음(작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청·작업 상태 스키마, MCP 기반 관제 연결, ROSA·RobotFleet 같은 오픈소스 에이전트 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 짝 연결 필요, 13. 대화형 기능의 신뢰·기반·32. 예외 복구·재계획·업무 연속성·37. 관제 화면·실행 기록 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. 언어 모델이 자연어 업무 지시를 여러 이기종 로봇의 하위 작업으로 분해하고 의존 관계·능력에 맞춰 배정·일정을 제안하는 연구는 무엇이 있고 결과는 어떻게 보고되는가? (섹션 4·6·8 겨냥)
3. 언어 모델이 만든 계획을 실행 전에 자동 검증하고 사람이 승인하게 하는 설계(사전 실행 검증, 감독 제어)는 어떤 것이 있으며 승인 부담은 어떻게 다뤄지는가? (섹션 3·6·11 겨냥)
4. 어디까지 했는지·왜 멈췄는지를 대화로 묻고 실행 기록을 근거로 답하는 연구와, 관제가 제공하는 작업 상태·단계·사건 기록은 무엇인가? (섹션 4·6·7 겨냥)
5. 관제·플랫폼의 작업 요청 API 와 언어 모델 도구 호출(MCP)을 잇는 오픈소스·프레임워크는 무엇이고 승인 단계를 두는가? (섹션 7 겨냥)
6. 병원·제조 공장·물류창고·실외 등 현장 유형별로 대화로 로봇 업무를 지시한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
7. 채팅 업무 지시에서 ROP가 직접 맡을 것(대화→계획, 검증, 승인, 관제 작업 요청, 진행 설명)과 로봇 수준 코드 생성·스킬 실행·형식 최적화기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Li 외(2025)의 서베이는 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정, 중간 수준 동작 계획, 하위 수준 행동 생성, 사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. | ref-165 | 아니오 | medium | 2025-02-06 | — | — |
| f2 | [사실] | Li 외(2025) 서베이의 사람 개입 절은 실행 전에 사람이 계획을 승인하는 방식(Hunt 외), 로봇이 막히면 도움을 요청하는 방식(VADER), 환각을 줄이는 사람 검증 방식(Li 외)을 예로 들고, 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머문다는 점과 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다는 점을 빈틈으로 지적했다. | ref-165 | 아니오 | medium | 2026-05-03 | 제약 | — |
| f3 | [사실] | SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. | ref-090 | 아니오 | medium | 2023-09-18 | — | — |
| f4 | [사실] | DART-LLM(Wang 외, 2024)은 자연어 지시를 방향 비순환 그래프(DAG)로 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀로, 질의응답형 분해 모듈·로봇 배정 함수·구동 모듈·시각-언어 물체 탐지 모듈로 구성되며 세 복잡도 수준에서 DeepSeek-r1-671B 가 최고 성공률을, Llama-3.1-8B 가 응답 시간 안정성을 보였고 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다고 보고했다. | ref-059 | 아니오 | medium | 2024-11-13 | — | — |
| f5 | [사실] | FLEET(Rivera 외, 2025)은 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 능력을 반영한 로봇–작업 적합도 행렬을 만들고, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀어 배정하는 2단계 혼합 방식으로, 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했으며 능력이 다른 사족 로봇 실기로 검증했다. | ref-242 | 아니오 | medium | 2025-10-08 | 수행 자원 | — |
| f6 | [사실] | 서로 다른 세 연구 그룹(SMART-LLM, DART-LLM, FLEET)이 자연어 업무 지시를 언어 모델로 하위 작업으로 분해하고 이기종 로봇에 배정하는 방법을 각각 보고해, '대화 지시→분해→배정' 접근이 한 곳 이상에서 확인된다. | ref-090, ref-059, ref-242 | 예 | medium | 2025-10-08 | — | — |
| f7 | [추정] | FLEET 가 배정·일정은 형식 최적화기에 맡기고 언어 모델은 작업 그래프·능력 매칭에만 쓴 점(f5)과 DART-LLM 이 의존 관계를 DAG 로 명시한 점(f4)을 함께 보면, 이 영역의 '업무 파악·분해·배정·일정 제안'은 언어 모델이 대화를 의존 관계 있는 작업 그래프와 능력 요구로 바꾸고, 실제 배정·일정은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 엔진에 넘겨 계산한 결과를 계획으로 제안하는 혼합 구조가 원문 주석의 짝 연결과 맞을 것으로 보인다. | ref-242, ref-059 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f8 | [사실] | VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈로, 복잡도가 다른 가정 작업 데이터셋에서 시험했으며 코드를 공개했다. | ref-753 | 아니오 | medium | 2025-07-07 | 가정 / 제약 | — |
| f9 | [사실] | HMCF(Li 외, 2025)는 로봇마다 자기 능력을 이해하고 작업을 실행 가능한 지시로 바꾸는 언어 모델 에이전트를 두고, 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀로, 시뮬레이션에서 기존 계획 방법보다 작업 성공률을 4.76% 높이고 실제 환경에서 최소한의 사람 개입으로 제로샷 일반화를 보였다고 보고했다. | ref-855 | 아니오 | medium | 2025-05-01 | 예외·성과 | — |
| f10 | [사실] | 서로 다른 세 연구 그룹(Li 외 서베이가 정리한 Hunt 외의 실행 전 승인, HMCF 의 작업 검증·사람 감독, VerifyLLM 의 자동 사전 검증)이 언어 모델이 만든 로봇 계획을 실행 전에 검증하거나 사람이 승인하게 하는 설계를 각각 보고해, '실행 전 검증·승인' 접근이 한 곳 이상에서 확인된다. | ref-165, ref-855, ref-753 | 예 | medium | 2026-05-03 | 시작 조건 | — |
| f11 | [추정] | 자동 사전 검증(f8)과 사람 승인(f2·f9·f10)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이 낸 계획을 먼저 자동 검증(의존 관계·능력·논리 일관성)으로 걸러 승인자에게는 검토 가능한 구조(작업 그래프·배정·일정)로 보여 주는 방식으로 구현해야 서베이가 지적한 운영자 인지 부담을 줄일 수 있을 것으로 보인다. | ref-165, ref-753, ref-855 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f12 | [사실] | CoMuRoS(Borate 외, 2025)는 중앙 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 작업 이력·로봇 상태 같은 동적 정보로 일을 배정하고, 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 만들며, 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획해 로봇이 동료를 돕거나 중단된 작업을 재개하거나 사람 도움을 요청하게 하는 중앙 숙고·분산 실행 구조로, 실기에서 협업 복구 9/10·협동 운반 8/8·사람 보조 복구 5/5, 22개 시나리오 벤치마크에서 정확도 최대 0.91 을 보고했다. | ref-677 | 아니오 | medium | 2025-11-27 | 예외·성과 | — |
| f13 | [사실] | Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다. | ref-857 | 아니오 | medium | 2025-09-19 | 실외 / 완료·인계 | — |
| f14 | [사실] | REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하는 틀로, 다양한 작업·실패 시나리오를 담은 RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다. | ref-453 | 아니오 | medium | 2023-06-27 | 예외·성과 | — |
| f15 | [사실] | 서로 다른 두 연구 그룹(REFLECT, Argenziano 외)이 로봇의 실행 기록·경험 요약을 근거로 언어 모델이 무엇을 했고 왜 실패했는지를 자연어로 설명하거나 질의에 답하게 하는 방법을 각각 보고해, '실행 기록 근거의 진행·실패 설명' 접근이 한 곳 이상에서 확인된다. | ref-453, ref-857 | 예 | medium | 2025-09-19 | 완료·인계 | — |
| f16 | [추정] | 실행 기록 근거의 설명 연구(f14·f15)와 Open-RMF 작업 상태 스키마가 단계·사건·추정 시간·배정 로봇을 담는 점(f17)을 함께 보면, 이 영역의 '채팅으로 진행 상황 질의·결과 설명'은 언어 모델의 대화 기억이 아니라 관제의 작업 상태·단계 사건 기록(37. 관제 화면·실행 기록)을 조회해 시각과 함께 답하는 방식으로 구현해야 하며, 답에 근거 기록의 식별자·시각을 붙이는 것이 13. 대화형 기능의 신뢰·기반의 근거 표시 요구와 맞을 것으로 보인다. | ref-453, ref-857, ref-111 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f17 | [사실] | Open-RMF 작업 상태 스키마(rmf_api_msgs task_state.json)는 작업 상태 값으로 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 를 두고, 활성 단계 id(active), 완료까지 남은 추정 시간(estimate_millis), 배정 로봇(assigned_to 의 group·name), 단계마다 시작·종료 시각·추정·사건(events)·건너뛰기 요청, 그리고 중단(interruptions)·취소(cancellation) 요청 기록을 담는다. | ref-111 | 아니오 | medium | 2026-09-29 | 완료·인계 | — |
| f18 | [사실] | Open-RMF 는 작업을 단계(phase)로 구성하고 Clean·Delivery·Patrol·Compose 범주의 작업 요청을 특정 로봇 지정(robot_task_request) 또는 최적 플릿 위임(dispatch_task_request)으로 보내며, 요청은 범주(category)와 플릿 지원 스키마를 따르는 설명(description)을 필수로, 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·수행 플릿 이름을 선택으로 두고, 이후 작업 취소나 단계 건너뛰기 요청으로 추가 제어를 할 수 있다. | ref-110, ref-125 | 아니오 | medium | 2026-09-29 | 시작 조건 | — |
| f19 | [사실] | Open Source Robotics Alliance(OSRA) 상호운용 SIG 는 2026-07-02 세션에서 Open-RMF REST API 를 언어 모델이 부를 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(MCP) 서버와 평이한 영어 명령을 여러 단계의 RMF 임무로 바꾸는 에이전트(Nayantra)를 다뤘으며, 공지 본문에는 실행 전 사람 확인·승인이나 작업 상태 질의에 관한 언급이 없다. | ref-862 | 아니오 | medium | 2026-07-02 | 시작 조건 | — |
| f20 | [추정] | MCP 도구 호출로 언어 모델이 관제 API 를 직접 부르는 구현(f19)에는 승인 단계가 드러나지 않으므로, 분류 원문의 '대화 결과는 실행 명령이 아니라 계획'이라는 요구를 지키려면 ROP 는 언어 모델의 도구 호출 제안(작업 요청 초안)과 실제 dispatch_task_request 발행 사이에 계획 미리보기·승인 관문을 두고, 승인된 계획만 한 번 관제 작업 요청으로 변환해야 할 것으로 보인다. | ref-862, ref-110, ref-125 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f21 | [사실] | ROSA(Royce 외, NASA JPL, IEEE Aerospace 2025)는 ROS 1·ROS 2 로봇 시스템을 자연어로 점검·진단·조작하게 하는 오픈소스 언어 모델 에이전트로, 명령을 잘 정의된 도구로 ROS 에 연결하고 매개변수 검증과 제약 강제 같은 안전 장치를 두며 JPL 화성 실험장·실험실·시뮬레이션의 세 로봇으로 모의 운용을 시연했다. | ref-859 | 아니오 | medium | 2024-10-09 | — | — |
| f22 | [사실] | RobotFleet(Gupta 외, 2025)은 이기종 로봇 플릿을 컨테이너 서비스로 배치하고 언어 모델로 중앙 집중식 다중 로봇 작업 계획·스케줄링을 하며, 공유 선언형 세계 상태와 실행·재계획을 위한 양방향 통신, 모듈형 자율 스택 층을 갖춘 오픈소스 프레임워크다. | ref-777 | 아니오 | medium | 2025-10-12 | — | — |
| f23 | [사실] | Henkel 외(2026)의 체계적 문헌 고찰(88편)은 산업 자동화의 기반 모델 에이전트가 사용자 지원·모니터링 용도에 강하고 사람 상호작용(+37%)·불확실성 처리(+35%)에서 기존 산업 에이전트보다 나으나, 보고된 시스템의 75.0% 가 기술 성숙도 4~6 의 프로토타입·초기 검증 단계이고 배포 지향 근거는 9.1% 에 그치며, 일반화 부족·환각과 출력 불안정·데이터 부족·추론 지연이 지속적 장애물이라고 보고했다. | ref-861 | 아니오 | medium | 2026-05-04 | 예외·성과 | — |
| f24 | [사실] | ETRI 전자통신동향분석 39권 1호(2024-02)의 '거대언어모델 기반 로봇 인공지능 기술 동향'(이준기 외)은 언어 모델의 상식·추론 능력으로 명령을 이해하고 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획과 요소 기술을 수행하는 제어 코드 생성을 자동화하는 흐름을 정리했으며, 다중 로봇 조율이나 사람 승인 절차는 다루지 않고 대규모 계산 자원·데이터·시뮬레이션·물리 테스트베드가 소수 기업에 집중된 점을 한계로 적었다. | ref-858 | 아니오 | medium | 2024-02 | — | — |
| f25 | [사실] | Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. | ref-847 | 아니오 | medium | 2026 | 병원 / 시작 조건 | 원문 미열람 |
| f26 | [추정] | 확인한 자료를 종합하면 12. 채팅으로 업무 지시·오케스트레이션에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것으로 보인다. | ref-242, ref-753, ref-677, ref-111, ref-110 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f27 | [추정] | 연계 대상: 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 생성하는 일(CoMuRoS)과 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 로봇 자체 지능·제어 쪽이며, 이종 제조사를 연결하는 ROP 는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 할 것으로 보인다. | ref-677, ref-859, ref-110 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f28 | [추정] | 언어 모델 기반 다중 로봇 작업 분해·배정(SMART-LLM, DART-LLM, FLEET), 사전 계획 검증(VerifyLLM), 실패 설명(REFLECT)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 이 영역 양쪽에 연결하고, 승인·근거 표시·환각 관련 내용은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다. | ref-165, ref-861, ref-753 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 2025-02-06 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2502.03814 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-059 | Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H. | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D. | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10-08 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.07417 | 아니오 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.05118 | 아니오 |
| ref-777 | Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J. | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.10379 | 아니오 |
| ref-855 | Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S. | HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models | 2025-05-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.00820 | 아니오 |
| ref-677 | Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2511.22354 | 아니오 |
| ref-857 | Argenziano, F., Umili, E., Leotta, F., & Nardi, D. | Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning | 2025-09-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2509.16006 | 아니오 |
| ref-858 | 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)) | 거대언어모델 기반 로봇 인공지능 기술 동향 | 2024-02 | 정부·연구기관 | high | 2026-09-29 | https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html | 아니오 |
| ref-859 | Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025) | Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent | 2024-10-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.06472 | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. (CoRL 2023) | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023-06-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.15724 | 아니오 |
| ref-861 | Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y. | Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges | 2026-05-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2605.02592 | 아니오 |
| ref-862 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-07-02 | 오픈소스 문서 | medium | 2026-09-29 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |
| ref-847 | Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력 | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 2026 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10514-026-10255-6 | 예 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f2(사람 개입이 반응적이고 승인 부담 미정량화), f23(산업 배포 근거 9.1%, 환각·출력 불안정), f19·f20(도구 호출 직결 구현에 승인 단계 부재) / 섹션 4: f3(작업 분해·연합 형성·배정), f4(의존 관계 DAG), f5(작업 그래프·로봇–작업 적합도 행렬), f8(사전 실행 계획 검증), f2(감독 제어·실행 전 승인), f14(실패 설명), f17(작업 상태·단계·사건) / 섹션 5: 병원 — f25(간호 인력 자연어 지시→작업 순서열·실행 중 재스케줄링, 원문 미열람 명시), 실외 — f13(정밀 농업에서 질의로 진행 확인), 가정 — f8(가정 작업 데이터셋 검증, 실제 현장이 아닌 데이터셋임을 명시) / 섹션 6: f3·f4·f5·f6·f7(대화 지시→분해·의존·능력 매칭→형식 배정), f8·f9·f10·f11(자동 검증 후 사람 승인), f12(사건 기반 재계획·사람 도움 요청), f13·f14·f15·f16(기록 근거의 진행·실패 설명), f20(승인 관문 위치) / 섹션 7: f17·f18(Open-RMF 작업 요청·상태 스키마), f19(OSRA Interop SIG, MCP 서버), f21(ROSA), f22(RobotFleet), f8(VerifyLLM 코드 공개) / 섹션 8: f1, f2, f3, f4, f5, f8, f9, f12, f13, f14, f23, 국내 f24 / 섹션 9: f26(직접 범위: 대화→작업 그래프, 엔진 결과의 계획 제안, 검증·승인, 관제 작업 요청 변환, 기록 근거 설명), f27(연계 대상: 로봇 내부 코드 생성·스킬 실행·ROS 직접 제어) / 섹션 10: 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링(f7·f28, 원문 주석의 짝), 13. 대화형 기능의 신뢰·기반(f11·f16·f28), 32. 예외 복구·재계획·업무 연속성(f12·f26), 37. 관제 화면·실행 기록(f16·f17), 20. 로봇·제조사 관제 연동(f18·f19·f20), 9. 채팅으로 시나리오 구성(f18 작업 요청에 없는 기한·반복은 시나리오 모델에), 10. 채팅으로 로봇 구성(f5 능력 매칭), 5. 로봇 능력·작업 표현(f5·f9 능력 이해), 24. 작업·워크플로 모델링(f4 DAG), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f28, 교차 규칙), 63. 병원·의료(f25) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 f5·f6·f7 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f2·f10·f11·f23 반영, 37. 관제 화면·실행 기록 페이지에 f17 반영, 32. 예외 복구·재계획·업무 연속성 페이지에 f12 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사전 실행 계획 검증 | Pre-execution Plan Verification | 언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다. |
| 감독 제어 | Supervisory Control | 사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다. |
| 실패 설명 | Failure Explanation | 로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다. |
| 로봇–작업 적합도 행렬 | Robot–Task Fitness Matrix | 로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다. |

## 열린 질문

새로 생긴 질문:

- 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 13. 대화형 기능의 신뢰·기반 | 근거: f2 | 종류: 일반
- 사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 20. 로봇·제조사 관제 연동, 13. 대화형 기능의 신뢰·기반 | 근거: f19 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 61. 물류창고, 63. 병원·의료, 62. 제조 공장 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 3
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f25 병원 논문 원문 미열람(이전 실행에서 Springer 인증 리다이렉트) — 저자·정량 결과·승인 절차 미확인, 검색 결과 초록 범위만 재인용
    - f12 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)은 검색 결과 요약에서만 보여 claim 에 넣지 않음
    - f2 서베이가 인용한 Hunt 외·VADER·Li 외 원 논문은 직접 열지 않아 서베이 본문 요약에만 기댐
    - f4 DART-LLM 의 로봇 종류·성공률 수치는 초록에 없어 미확인
    - f9 HMCF 의 사람 개입 횟수 등 정량값은 초록에 없어 미확인
    - f6·f10·f15 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f17·f18 Open-RMF 문서·스키마 발행일 미확인
    - MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(제조 공장 사례 후보)는 403 으로 열지 못해 넣지 않음
    - Eluna(arXiv 2607.08960, 창고 SOP 에이전트)는 로봇 지시가 아닌 업무 시스템 자동화라 적용 사례로 넣지 않음
    - 국내 산업 사례: 한국어 검색 3회에서 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 찾았으나 대화형 업무 지시가 아니어서 출처로 넣지 않음
    - hellot SCM FAIR 2026 기사의 자연어 프롬프트는 영상 분석 조건 설정이라 이 영역과 무관해 제외
- 범위 경계 위반 의심:
    - f27: 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS 직접 제어 에이전트(ROSA)는 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f7·f26: 배정·일정 계산 자체는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 범위이므로 이 영역에서는 대화→작업 그래프 변환과 계획 제안·승인의 근거로만 제안함
    - f12·f26: 실행 중 재계획·복구는 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 승인된 계획과의 차이 표시·재승인 근거로만 제안함
    - f8: VerifyLLM 의 가정 작업 데이터셋은 실제 가정 현장이 아니므로 site_type 가정 은 데이터셋 기준임을 서술에 밝혀야 함
    - f23: 산업 자동화 일반(비로봇 포함) 문헌 고찰은 성숙도·과제 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-165~ref-847, 예약 구간 안) 상한 도달로 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, Hierarchical LLM multi-agent prompt optimization(arXiv 2602.21670), 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)는 확인했으나 넣지 못했다. 원문 열람 17건(webfetch 14, github_raw 3: task_new.md·task_request.json·task_state.json), 미열람 1건(ref-847, 이전 실행의 검색 결과 초록 재인용). ref-847 은 이전 실행 2026-09-29-04 가 ref-242 로 낸 병원 논문과 같은 URL 이나 참고문헌 목록 입력에 없어 새 id 로 냈으며 퍼블리셔가 기존 id 로 합칠 수 있다(이번 실행의 ref-242 는 FLEET 논문이다). 교차 확인 3건(f6: SMART-LLM·DART-LLM·FLEET, f10: Li 외 서베이·HMCF·VerifyLLM, f15: REFLECT·Argenziano 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록·HTML 본문 확인, high 신뢰도 출처는 ETRI 동향 1건이며 단일 출처). 분류 원문 핵심 질문(대화 지시→확인 가능한 계획→승인→실행·진행 설명)에는 f3·f4·f5·f6(분해·배정 가능), f8·f9·f10(실행 전 검증·승인 설계 존재), f13·f14·f15·f17(기록 근거 진행·실패 설명과 관제 상태 기록), f19·f20(도구 호출 직결 구현의 승인 부재)로 답했으며 결론은 '세 단계 각각의 연구·오픈소스는 있으나 셋을 하나의 승인 관문이 있는 흐름으로 이은 운영 사례는 확인되지 않았고 산업 배포 근거는 드물다'는 추정(f7·f11·f16·f20·f26)이다. 현장 유형: 병원(f25, 원문 미열람 명시), 실외(f13, 정밀 농업), 가정(f8, 데이터셋 기준)만 확인했고 물류창고·제조 공장·상업 시설 사례는 없다. L. AI·학습 기술 관련 finding(f1~f6·f8·f9·f12·f14·f28)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·13. 대화형 기능의 신뢰·기반 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 848건과의 URL 중복을 대조하지 못했으므로 서베이·SMART-LLM·ROSA 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시·구조화 출력·팬아웃·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-14/research.md

```markdown
# 리서치 브리프 2026-09-25-14

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-14 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 4. 성과·경제성·프로세스 개선 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 용어집 SCOR 항목만 이 영역에 연결됨
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-008, oq-011 있음, 정정 요청 없음

## 조사 질문

1. 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [분류원문]
2. 납기 준수율·처리량·리드타임·가동률 같은 성과 지표를 정의하는 표준·벤치마크(ISO 22400, SCOR, WERC DC Measures)는 무엇이며 각각 어떤 지표를 어떻게 정의하는가? (섹션 4·7 겨냥)
3. 처리량·재공품·리드타임의 관계와 병목을 찾는 방법(리틀의 법칙, 활성 구간 기반 병목 탐지, 프로세스 마이닝)은 무엇인가? (섹션 4·6 겨냥)
4. 로봇 창고 연구는 로봇 수·작업대·충전·에너지·운영 규칙이 처리량과 비용에 주는 영향을 어떻게 평가했는가? (섹션 5·6·8 겨냥)
5. ROP가 쌓는 실행 기록(로봇 상태, 작업 상태)으로 어떤 성과 지표를 계산할 수 있고, 무엇은 상위 업무 시스템 데이터가 있어야 하는가? (섹션 9·10 겨냥)
6. oq-011 스마트물류센터 인증의 세부 평가 기준에 성과관리·설비 지표가 어떻게 들어가는가, 국내 물류 로봇 도입의 투자 효과 자료는 무엇이 있는가? (한국 자료 우선, 섹션 3·8·11 겨냥)
7. oq-008 여러 거점 간 로봇 재배치·성수기 임대 보충의 경제성을 다룬 학술·공공 자료가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 22400-2:2014는 제조 운영 관리용 핵심성과지표(KPI)를 공식·구성 요소·시간 특성·단위와 함께 정의하며, 처리율(throughput rate), 가동 효율, 종합설비효율(OEE), 가용성, 품질률, 재고 회전율, 평균 고장 간격·수리 시간 등 30여 개 지표를 담는다. | ref-139 | 아니오 | medium | 2014 | 예외·성과 | 원문 미열람 |
| f2 | [사실] | ISO 22400-2에서 종합설비효율(OEE)은 가용성·효과성(성능)·품질률의 곱으로 정의되고 계획 가동 시간(PBT) 같은 시간 상태 모델을 기준으로 계산되며, 2부의 개정안(ISO/DIS 22400-2)이 진행 중이다. | ref-139 | 아니오 | medium | 2014 | 예외·성과 | 원문 미열람 |
| f3 | [의견] | Computers & Industrial Engineering(2020) 게재 논문은 ISO 22400의 OEE 정의가 판마다 서로 어긋나고 나카지마의 TPM 원래 정식화와도 달라 불완전하다고 평가하고, 둘을 맞추는 암묵적 가정을 제시했다. | ref-142 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f4 | [사실] | ASCM SCOR의 완전 고객 주문 이행률(RL.1.1 Perfect Customer Order Fulfillment)은 완전 주문 수를 전체 주문 수로 나눈 비율이며, 주문의 모든 품목 줄이 완전해야 완전 주문으로 보고, 하위 지표로 완납 주문 비율(RL.2.1), 최초 약속일 대비 납기 성과(RL.2.2), 주문 문서 정확도(RL.2.3), 무손상 상태(RL.2.4)를 둔다. | ref-140 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f5 | [사실] | SCOR의 대표 성과 지표는 신뢰성(완전 주문 이행), 대응성(주문 이행 사이클 타임), 비용(공급망 관리 총비용) 같은 성과 속성별로 나뉘어, 로봇 운영 지표보다 상위의 주문·공급망 단위 성과를 잰다. | ref-001, ref-140 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f6 | [사실] | WERC DC Measures 연례 조사는 물류센터 운영자가 꼽는 주요 지표로 정시 출하율, 평균 창고 용량 사용률, 주문 피킹 정확도, 입고–적치 소요 시간(dock-to-stock cycle time)을 다루며, 2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시했다. | ref-141 | 아니오 | medium | 2025 | 입고 / 완료·인계 | 원문 미열람 |
| f7 | [사실] | 리틀의 법칙(Little's Law)은 재공품(WIP) = 처리량(TH) × 사이클 타임(CT)의 관계이며, Hopp·Spearman의 팩토리 피직스는 병목 속도에서 최대 처리량을 내는 임계 재공품(critical WIP)을 넘으면 처리량은 늘지 않고 대기 때문에 사이클 타임만 길어진다고 본다. | ref-143 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f8 | [추정] | 리틀의 법칙과 RMFS 대기행렬 연구를 함께 보면, 작업대·포장대 같은 병목의 처리 속도를 넘어 로봇 작업을 더 투입하면 로봇 가동률은 올라가도 출하 처리량은 늘지 않고 주문 사이클 타임만 길어질 수 있어, 로봇 가동률 상승이 곧 출하량 증가를 뜻하지 않을 것으로 보인다. | ref-143, ref-096, ref-097 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |
| f9 | [사실] | Lamballais·Roy·de Koster(2017)의 RMFS 대기행렬 모델은 최대 주문 처리량·평균 주문 사이클 타임·로봇 가동률을 함께 추정하며, 처리량은 보관 구역 둘레의 작업대 위치에 영향을 받았다. | ref-096 | 아니오 | medium | 2017 | 피킹 / 수행 자원 | 원문 미열람 |
| f10 | [사실] | Ghelichi·Kilaru(2021)는 협업형 AMR 피킹 방식 두 가지(라스트 마일 배송형 LMD, 통로 만남형 MIA)의 해석적 모델을 세워, 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우하고, 피킹 주기가 높을 때 LMD가 필요한 로봇 수를 줄이며 MIA는 로봇이 더 필요하지만 작업자 참여를 높인다고 보고했다. | ref-145 | 아니오 | medium | 2021 | 피킹 / 수행 자원 | 원문 미열람 |
| f11 | [사실] | Azadeh·de Koster·Roy(2019)의 리뷰는 로봇형 처리 시스템(셔틀 기반 저장·반출, 컴팩트 저장, RMFS 등)이 공간을 적게 쓰고 수요 변동에 유연하며 24시간 운영할 수 있다고 정리하고, 연구를 시스템 분석·설계 최적화·운영 계획·통제로 나누면서 많은 신규 시스템이 학술적으로 거의 연구되지 않았다고 지적했다. | ref-144 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f12 | [사실] | Omega(2024) 게재 RMFS 에너지 연구는 일반·긴급 주문의 동적 우선순위 정책을 평가해 처리량과 에너지 소비 사이에 절충이 있음을 보이고, 제안한 우선순위 규칙이 선착순(FCFS) 대비 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. | ref-146 | 아니오 | medium | 2024 | 피킹 / 예외·성과 | 원문 미열람 |
| f13 | [사실] | 충전 설비 결정은 비용과 처리 시간의 절충으로 연구되어, RMFS에서는 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 저렴했고, AMR 물류센터 시뮬레이션에서는 충전기가 부족하면 큰 지연이, 과잉이면 불필요한 비용이 생겼다. | ref-098, ref-102 | 아니오 | medium | 2025 | 적치 / 제약 | 원문 미열람 |
| f14 | [사실] | 처리량 병목 탐지 문헌에서 활성 구간 방법(Roser 외 2001)은 중단 없이 가장 오래 가동 중인 자원을 순간 병목으로 보고, 병목을 순간·평균·이동(shifting) 병목으로 구분하며, 버퍼 재고와 결합해 병목 이동을 예측하는 데까지 확장되었다. | ref-115 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [추정] | 활성 구간 방법은 자원별 가동·유휴 시각 기록만으로 계산되므로, ROP가 수집하는 로봇 상태(작업 중·유휴·충전·오류) 기록과 작업대·승강기 이벤트를 쓰면 로봇·작업대·설비 가운데 이동하는 병목을 찾는 데 적용할 수 있을 것으로 보인다. | ref-115, ref-148 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f16 | [사실] | Open-RMF API의 로봇 상태 스키마(robot_state)는 로봇 상태를 uninitialized, offline, shutdown, idle, charging, working, error 일곱 값으로 두고, 배터리 충전 상태(0.0~1.0), 현재 작업 id, 운영자가 조치할 문제(issues), 위치, 시각(unix_millis_time)을 함께 보고한다. | ref-148 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f17 | [사실] | Open-RMF API의 작업 상태 스키마(task_state)는 작업 시작·종료 시각(unix_millis_start_time, unix_millis_finish_time), 최초 예상 소요 시간과 현재 예상 소요 시간(original_estimate_millis, estimate_millis), 12개 상태 값, 배정 로봇, 단계, 중단·취소·강제 종료 정보를 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f18 | [추정] | 로봇·작업 상태 기록으로 로봇 가동률(작업 중 시간 비율), 충전·오류 시간 비율, 작업 사이클 타임과 예상 대비 편차, 취소·실패 비율 같은 운영 지표는 ROP 안에서 계산할 수 있으나, 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표는 WMS·ERP의 주문 데이터와 연결해야 계산될 것으로 보인다. | ref-111, ref-148, ref-140 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f19 | [사실] | PM4Py는 Fraunhofer FIT에서 분사한 Process Intelligence Solutions가 관리하는 오픈소스 파이썬 프로세스 마이닝 라이브러리로, 프로세스 발견 등 알고리즘을 제공하고 객체 중심 이벤트 로그(OCEL)를 선택 기능으로 두며, 공개판은 AGPL-3.0이고 상용 라이선스를 별도로 둔다. | ref-147 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | 창고 업무 개선을 위한 프로세스 마이닝 사례 연구는 SAP 창고 관리 모듈 테이블에서 이벤트 로그를 뽑아 ProM의 Heuristic Miner로 분석했고, 병목 분석에서 자재가 고층 랙에 오래 머물고 고층 랙 사이를 옮겨 다니는 흐름을 찾았다. | ref-149 | 아니오 | medium | 2015 | 적치 / 예외·성과 | 원문 미열람 |
| f21 | [추정] | 오토스토어가 발표한 경제성 연구는 국내 도입 기업 5곳이 3년간 시스템 도입 비용 87.4억 원 대비 약 156.7억 원의 경제적 효과, 순현재가치 약 69.2억 원, 투자 회수 18개월, ROI 79%를 거뒀다고 밝혔다. | ref-150 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f22 | [사실] | oq-011 관련: 스마트물류센터 인증은 기반영역에서 성과관리 체계를 평가하며, 세부 항목 판단 기준을 데이터 관리 기반 구축(5등급), 실시간 모니터링(4등급), 관리와 통제(3등급), 최적화(2등급), 자율운영(1등급)의 단계로 둔다. | ref-106 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f23 | [의견] | 박정수·안영효(2010)는 화주기업과 물류기업이 공동으로 핵심성과지표(KPI)를 관리하는 방법을 다루며, 경영환경 변화에 대응하려면 KPI를 분석해 빠르게 피드백하는 체계가 필요하다고 보았다. | ref-151 | 아니오 | medium | 2010 | — | 원문 미열람 |
| f24 | [추정] | 연계 대상: 투자 수익률·순현재가치·회수 기간 같은 재무적 투자 평가와 원가 배분은 재무 등 상위 업무 영역의 몫이고, ROP는 그 입력이 되는 처리량·가동률·충전·예외 같은 실행 데이터를 제공하고 운영 규칙 변경의 효과를 측정하는 쪽을 맡는 것으로 보인다. | ref-150, ref-139, ref-148 | 아니오 | low | 2026-09-25 | — | — |
| f25 | [추정] | 분류 원문의 질문(로봇 가동률 상승이 출하량·비용 개선으로 이어졌는가)에 답하려면 같은 기간의 로봇 운영 지표(가동률·충전·오류 시간)와 주문 단위 지표(완전 주문 이행률, 주문 이행 사이클 타임)와 비용을 함께 비교해야 하며, 처리량이 작업대 같은 공유 자원에 묶이는 연구 결과로 볼 때 가동률만으로는 판단할 수 없을 것으로 보인다. | ref-096, ref-140, ref-148, ref-143 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-001 | ASCM | SCOR Digital Standard | 미확인 | 표준 | medium | 2026-09-25 | https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/ | 예 |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | 논문 | medium | 2026-09-25 | https://repub.eur.nl/pub/107376/ | 예 |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 예 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cslc.koti.re.kr/ | 예 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/54497.html | 예 |
| ref-140 | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 미확인 | 표준 | medium | 2026-09-25 | https://scor.ascm.org/performance/reliability/RL.1.1 | 예 |
| ref-141 | WERC(Warehousing Education and Research Council) | WERC DC Measures Survey - 2025 | 2025 | 업계 보고서 | medium | 2026-09-25 | https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf | 예 |
| ref-142 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Overall Equipment Effectiveness: consistency of ISO standard with literature | 2020 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527 | 예 |
| ref-143 | Project Production Institute | Little’s Law – A Practical Approach to Understanding Production System Performance | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/ | 예 |
| ref-115 | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 2023 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031 | 예 |
| ref-144 | Azadeh, K., de Koster, R., & Roy, D. | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873 | 예 |
| ref-145 | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 2021 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0307904X20305801 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-147 | Process Intelligence Solutions (PM4Py GitHub) | pm4py — Official public repository for PM4Py (Process Mining for Python) (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/process-intelligence-solutions/pm4py | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-149 | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 2015 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9 | 예 |
| ref-150 | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 미확인 | 기사 | low | 2026-09-25 | https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html | 예 |
| ref-151 | 박정수, 안영효(유통경영학회지) | 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구 | 2010 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f8·f25(로봇 가동률이 출하량을 보장하지 않음, 운영·주문·비용 지표를 함께 봐야 함), f22(국내 인증이 성과관리 체계를 평가) / 섹션 4: f1·f2(ISO 22400 KPI·OEE), f4·f5(SCOR 완전 주문 이행·사이클 타임·비용), f6(입고–적치 소요 시간·피킹 정확도), f7(리틀의 법칙·임계 재공품), f14(순간·이동 병목) / 섹션 5: 입고 완료·인계 f6, 적치 예외·성과 f20, 적치 제약 f13, 피킹 수행 자원 f9·f10, 피킹 예외·성과 f8·f12, 출하 완료·인계 f4, 출하 예외·성과 f18·f25 / 섹션 6: f7·f8(흐름 법칙), f9·f10(해석적 모델), f12·f13(에너지·충전 비용 절충), f14·f15(병목 탐지), f19·f20(프로세스 마이닝) / 섹션 7: f1·f2·f3(ISO 22400과 OEE 정합성 비판 병기), f4·f5(SCOR), f6(WERC DC Measures), f16·f17(Open-RMF 로봇·작업 상태 스키마), f19(PM4Py), f22(스마트물류센터 인증) / 섹션 8: f3, f9~f14, f20, f23(국내 KPI 연구), f21(벤더 주장 병기 필수) / 섹션 9: f18(ROP 안에서 계산 가능한 운영 지표 대 주문 데이터가 필요한 지표), f24(연계 대상: 재무 투자 평가) / 섹션 10: 1. 주문·업무 시스템 연계(f18 주문 단위 지표), 2. 공정·워크플로 모델링(f19·f20 프로세스 마이닝), 3. 처리능력·거점·설비 계획(f9·f10), 16. 공용 자원·충전·에너지 최적화(f12·f13), 19. 모니터링·이상 탐지·원인 분석(f14·f15), 8. 실시간 세계 상태·데이터 일관성(f16 현재 상태 기록), 22. 시뮬레이션·예측용 디지털 트윈(f12·f13 가정한 정책 실험) / 섹션 11: open_questions_new 4건, 기존 oq-008(미해결)·oq-011(f22로 부분 보강, 개별 지표 미확인). 다음 실행 후보: ASTM F45 이동로봇 성능 시험 방법(23. 시험·형식 검증·벤치마크)과 인간–로봇 협업 피킹 현장 실험(18. 사람–로봇 협업·운영 인터페이스)은 출처 예산으로 넣지 못함 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 종합설비효율 | Overall Equipment Effectiveness (OEE) | 설비의 가용성·성능(효과성)·품질률을 곱해 계획된 시간 대비 실제로 좋은 산출을 낸 비율을 나타내는 지표로, ISO 22400-2가 제조 운영 관리 KPI의 하나로 정의한다. |
| 완전 주문 이행률 | Perfect Order Fulfillment | 납기·수량·문서·상태가 모두 요구대로 충족된 주문의 비율로, SCOR의 신뢰성 대표 지표(RL.1.1)이다. |
| 리틀의 법칙 | Little's Law | 안정된 흐름에서 재공품(WIP)이 처리량과 사이클 타임의 곱과 같다는 관계로, 처리량·재고·리드타임을 함께 해석하는 기준이 된다. |
| 프로세스 마이닝 | Process Mining | 시스템에 남은 이벤트 로그로 실제 업무 흐름을 발견하고 설계와 비교하며 대기·병목을 분석하는 기법이다. |

## 열린 질문

새로 생긴 질문:

- 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 1. 주문·업무 시스템 연계 | 근거: f25 | 종류: 일반
- 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 16. 공용 자원·충전·에너지 최적화 | 근거: f2 | 종류: 일반
- 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 3. 처리능력·거점·설비 계획 | 근거: f21 | 종류: 일반
- 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? | 관련 영역: 4. 성과·경제성·프로세스 개선, 19. 모니터링·이상 탐지·원인 분석 | 근거: f15 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 28회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·연구마다 발행 주체 한 곳의 자료만 확인(f5 의 ref-001·ref-140 은 모두 ASCM)
    - f1 ISO 22400-2 KPI 개수(34개)는 제3자 요약 기준
    - f6 WERC 벤치마크 수치(최우수 피킹 정확도·입고–적치 시간 등)는 2차 요약 경유라 finding 으로 내지 않음
    - f7 ref-143 발행일 미확인
    - f12 Omega 논문 저자·실험 조건 미확인
    - f21 오토스토어 연구의 수행 주체·방법론 미확인(벤더 주장)
    - f22 스마트물류센터 인증 세부 항목에 로봇 대수·가동률 지표가 있는지 여전히 미확인 — oq-011 미해결
    - oq-008 로봇 재배치·성수기 임대(RaaS)는 벤더·블로그 자료만 나와 finding 으로 내지 않음 — 미해결
    - ref-142·ref-115·ref-146·ref-149 저자 미확인, ref-150 발행일 미확인
    - 인간–로봇 협업 피킹 현장 실험(Pasparakis·de Vries·de Koster, Logistics Research)과 ASTM F45 이동로봇 성능 시험 방법은 출처 상한으로 넣지 못함
- 범위 경계 위반 의심:
    - f24: 재무적 투자 평가(ROI·NPV·원가)는 분류 원문 9장 '상위 업무 시스템'의 재무 연계 영역이므로 '연계 대상: '으로 표시함
    - f21: 벤더의 경제 효과 주장은 vendor_claim 으로 표시하고 ROP 직접 범위로 서술하지 않음
- 한계: web_fetch_available: false · fetch_mode mirror_only. GitHub 공식 저장소 원문 3건(ref-147 PM4Py README, ref-111 task_state.json, ref-148 robot_state.json)만 raw.githubusercontent.com 으로 열었고, ISO·ASCM·WERC·논문·기사 12건은 검색 요약만 봐서 원문 미열람(신뢰도 상한 medium). 교차 확인 0건. 검색 28회/30, 신규 출처 15건/15(ref-139~ref-151, next_ref_id 기준)로 출처 상한에 도달했다. 재사용 6건(ref-001, ref-096, ref-097, ref-098, ref-102, ref-106). 이전 브리프에서 Open-RMF task_state.json 에 ref-054·ref-098 을 붙인 이력이 있으나 참고문헌 목록의 해당 id 는 다른 출처라 새 id(ref-111)를 붙였다 — 퍼블리셔가 중복을 확인해야 한다. 한국 자료: 스마트물류센터 인증 심사 기준(ref-106), 국내 KPI 논문(ref-151), 벤더 경제성 발표 기사(ref-150). 국내 공공 기관의 물류 로봇 투자 효과 실측 자료는 찾지 못했다. oq-011 은 f22 로 부분 보강했으나 해결 아님, oq-008 은 학술·공공 자료를 찾지 못했다. 에너지 지표는 RMFS 모델 연구(f12)와 충전 비용 절충(f13)뿐이고 현장 실측 자료는 없다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성(현재 로봇 상태 기록, f16)과 22. 시뮬레이션·예측용 디지털 트윈(정책·투자 대안의 가정 실험, f12·f13)은 구분해 연결을 제안했다.
```
