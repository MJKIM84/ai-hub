(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-08
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 6. 온톨로지 기반 시스템·로봇 연동 (B. 로봇 온톨로지)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-876
- 새 출처 id 구간: ref-876 ~ ref-905 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-876 부터 순서대로 쓰고 ref-905 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-29-08/target.json

```json
{
  "run_id": "2026-09-29-08",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 100,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 6,
    "area_name": "6. 온톨로지 기반 시스템·로봇 연동",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=6"
}
```

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md

```markdown
---
title: "6. 온톨로지 기반 시스템·로봇 연동"
type: area
category: "B. 로봇 온톨로지"
area_no: 6
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 6. 온톨로지 기반 시스템·로봇 연동

# 6. 온톨로지 기반 시스템·로봇 연동

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

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]

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

### docs/categories/robot-ontology/heterogeneous-robot-registration.md (요약)

```markdown
# 4. 이기종 로봇 등록

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 875건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 232개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
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

### docs/open-questions.md (요약: 대상 영역 [6] 에 걸린 1건 / 전체 150건)

```markdown
- oq-150 [열림] 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (영역 4, 5, 6)
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

### runs/2026-09-29-07/research.md

```markdown
# 리서치 브리프 2026-09-29-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-07 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 4. 이기종 로봇 등록 |
| 대분류 | B. 로봇 온톨로지 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 디지털 명판·URDF·AGV 기술 데이터 서브모델·자산관리셸 레지스트리·온톨로지 채우기 용어 없음(VDA 5050 팩트시트·신원 보고·자산관리셸·소프트웨어 명판·능력 기술 서브모델·의미 식별자는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 등록 데이터 수집(팩트시트 요청·자산관리셸), 문서·URDF에서 능력 추출, 검토·승인 흐름, 어댑터 설정 생성 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 팩트시트, IDTA 02047·02006, MassRobotics 신원 보고, OPC UA Robotics, 자산관리셸 API, Open-RMF 플릿 어댑터 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-128 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]
2. 등록 시 받아야 할 식별·제원 데이터를 정한 기계가독 형식(VDA 5050 팩트시트, 자산관리셸 서브모델·디지털 명판, MassRobotics 신원 보고, OPC UA Robotics)은 각각 무엇을 필수로 요구하는가? (섹션 4·7 겨냥)
3. 플릿 관리 프레임워크(Open-RMF)는 새 로봇을 등록·연동할 때 어떤 설정과 구현을 요구하며, 병원 현장에서 실제로 어떻게 등록했는가? (섹션 5·6 겨냥)
4. 매뉴얼·URDF·자연어 설명에서 능력·제약을 자동으로 추출하고 검증과 사람 검토를 두는 방법은 무엇이 보고되었는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)
5. 제조사가 능력·제원 정보를 제공·갱신하는 경로(자산관리셸 레지스트리·디스커버리, 팩트시트 요청)와 벤더·통합사를 사전 평가하는 등록 승인 관문의 사례는 무엇인가? (섹션 6·9 겨냥)
6. oq-128 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있는가? (섹션 5·11 겨냥, 한국 자료 우선)
7. 이기종 로봇 등록에서 ROP가 직접 맡을 것(등록부·데이터 수집·추출 초안·검토 승인)과 로봇 내부 주행 기술·제조사 책임에 맡길 것의 경계는 어디이며, 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소(main, 3.0.0 판)의 팩트시트 JSON 스키마는 headerId·timestamp·version·manufacturer·serialNumber·typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 을 필수 속성으로, 하드웨어·소프트웨어 버전과 네트워크·배터리 매개변수를 담는 mobileRobotConfiguration 을 선택 속성으로 둔다. | ref-228 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f2 | [사실] | 같은 팩트시트 스키마에서 typeSpecification 은 시리즈 이름, 구동 방식(DIFFERENTIAL·OMNIDIRECTIONAL·THREE_WHEEL), 로봇 종류(FORKLIFT·CONVEYOR·TUGGER·CARRIER), 최대 적재 질량, 위치추정 방식, 주행 방식(물리 라인·가상 라인·자유 주행), 지원 구역 유형을, physicalParameters 는 최소·최대 속도, 각속도, 최대 가감속, 높이·폭·길이를 기종 단위로 기술한다. | ref-228 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다고 적어 등록 데이터를 로봇에서 직접 받는 경로를 둔다. | ref-031 | 아니오 | medium | 2026-09-29 | 시작 조건 | — |
| f4 | [사실] | IDTA 02047-1-0(2025-03) '실내 물류용 AGV 기술 데이터' 자산관리셸 서브모델은 TypeAndApplicationInformation·TechnicalParameters·VDA5050Factsheet·EnergyAndCommunication·Battery·Safety·TemporaryTechnicalData 컬렉션으로 구성되며, 혼합 플릿을 중앙 관제에 통합하고 시운전·운영·유지보수에 걸쳐 쓰는 것을 목표로 디지털 명판·기술 데이터 서브모델과 연계된다. | ref-198 | 아니오 | medium | 2025-03 | 수행 자원 | — |
| f5 | [사실] | IDTA 02006 디지털 명판 서브모델 3.0 판은 URIOfTheProduct·ManufacturerName·ManufacturerProductDesignation·SerialNumber·YearOfConstruction·DateOfManufacture 를 필수로, HardwareVersion·FirmwareVersion·SoftwareVersion·ContactInformation·Markings 를 선택으로 두어 로봇을 포함한 산업 장비의 식별자와 버전을 기계가독 명판으로 담는다. | ref-876 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f6 | [사실] | MassRobotics AMR 상호운용 표준의 JSON 스키마는 로봇이 접속 시 보내는 identityReport 에 uuid(RFC 4122)·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope 를 필수로, maxSpeed·maxRunTime·chargerType·supportVendorName·productDocumentation·cargoType·cargoMaxVolume·cargoMaxWeight 등을 선택으로 둔다. | ref-230 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f7 | [사실] | 서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하고, 셋 모두 제조사명·기종(시리즈)·일련번호·치수(외곽)·최대 적재·최대 속도 항목을 공통으로 담아 '제조사 제공 식별·제원 기록'이 이기종 로봇 등록의 표준 관행으로 한 곳 이상에서 확인된다. | ref-228, ref-230, ref-876 | 예 | high | 2026-09-29 | 수행 자원 | — |
| f8 | [사실] | OPC UA for Robotics 1부(OPC 40010-1) 1.02 판(2025-09-08)은 수직 통합·자산 관리·상태 감시를 범위로 MotionDeviceSystem 정보 모델을 정의하고, MotionDevice 와 Controller 에 Manufacturer·Model·SerialNumber·ProductCode·SoftwareRevision 식별 속성을 두어 산업용 로봇(매니퓰레이터) 등록에 쓸 식별 정보를 표준화한다. | ref-881 | 아니오 | medium | 2025-09-08 | 수행 자원 | — |
| f9 | [사실] | OPC Foundation 은 OPC UA for Robotics 명세를 STS XML 외에 'AI 응용용 마크다운'과 'RAG 청크' 형식으로도 제공해, 표준 문서 자체를 언어 모델이 읽어 처리하기 쉬운 형식으로 배포하기 시작했다. | ref-881 | 아니오 | medium | 2025-09-08 | — | — |
| f10 | [사실] | 자산관리셸 API 명세(IDTA-01002) 공식 저장소는 최신 3.2.0 판에서 AAS 저장소·서브모델 저장소·AAS 레지스트리·서브모델 레지스트리·디스커버리·개념 설명 저장소·AASX 파일 서버 등 아홉 가지 서비스 명세를 두어, 제조사가 낸 자산관리셸을 등록하고 찾는 인터페이스를 표준으로 정한다. | ref-880 | 아니오 | medium | 2026-09-29 | — | — |
| f11 | [추정] | 디지털 명판(f5)·AGV 기술 데이터 서브모델(f4)·레지스트리·디스커버리 API(f10)를 함께 보면, 이 영역의 '제조사 능력 정보 제공 경로'는 제조사가 명판과 기술 데이터 서브모델을 자산관리셸로 내고 레지스트리에 등록해 ROP 가 자산 식별자로 찾아 읽는 방식으로 구성할 수 있을 것으로 보이나, 로봇 관제가 이 경로로 실제 등록한 운영 사례는 확인되지 않았다. | ref-876, ref-198, ref-880 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f12 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 새 플릿을 등록하는 config.yaml 에 플릿 이름, 선속도·각속도 한계, 발자국·근접 반경(profile), 후진 가능 여부, 배터리·기계·주변·도구 시스템 매개변수, 재충전 임계값, 작업 능력(loop·delivery·clean), 로봇별 충전기를 적고, 로봇 측 RobotAPI 가 navigate·position·battery_soc·stop·start_activity·is_command_completed 를 구현해야 한다고 정한다. | ref-153 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f13 | [사실] | Valner 외(2022)의 타르투대학교병원 현장 시험은 자체 관제가 없는 PAL Robotics TIAGo 를 로봇 탑재 컴퓨터의 FreeFleet 클라이언트, 플릿 이름·DDS 설정의 FreeFleet 서버, 배터리·속도·발자국을 적은 RMF 어댑터 파일로 Open-RMF 에 등록했고, 프로그램 제어가 없는 병원 문은 카드 인식·근접 센서를 대신 작동시키는 서보 장치를 만들어 지나며 중환자실에서 검사실로 혈액 검체를 운반했다. | ref-874 | 아니오 | medium | 2022-08-23 | 병원 / 수행 자원 | — |
| f14 | [사실] | 서로 다른 두 발행 주체(Open Robotics 튜토리얼, 타르투대학교 연구진의 병원 현장 시험)가 플릿 관리 프레임워크에 로봇을 등록하는 일이 '기종 제원·배터리 매개변수를 적은 어댑터 설정 파일'과 '로봇별 API 구현'의 두 부분으로 이루어진다고 각각 보고해, 등록 작업의 구성이 한 곳 이상에서 확인된다. | ref-153, ref-874 | 예 | high | 2022-08-23 | 병원 / 수행 자원 | — |
| f15 | [사실] | 싱가포르 창이종합병원 CHART 의 RoMi-H 등재 프로그램(2025-05-01 시행)은 보건부가 Open-RMF 기반 RoMi-H 를 공공 의료기관의 자동화 통합 플랫폼으로 지정한 뒤 시스템 통합사가 기술·배치 역량 평가를 거쳐 2년 유효 등재를 받아야 병원 제안 요청에 참여하게 하며, 2026-08-24 기준 등재 업체는 5곳이다. | ref-878 | 아니오 | medium | 2026-08-24 | 병원 / 제약 | — |
| f16 | [추정] | 벤더 주장(기사 경유): 클로봇의 크롬스는 '국내 첫 이기종 로봇 통합관제 솔루션'으로 50대 이상 로봇 동시 제어와 엘리베이터 탑승을 지원한다고 소개되며, 기사는 LG CNS 와 함께 인천공항 다기종 로봇 제작·5G 디지털 트윈 관제 구축 사업을 계약했다고 전하나 VDA 5050 지원 여부·연동 제조사 수·등록 방식은 기사에 없다. | ref-875 | 아니오 | low | 2025-11-09 | 기타 / 수행 자원 | 벤더 주장 |
| f17 | [사실] | 신민종·한영석·정재윤(한국디지털산업학회지 29권 4호, 2024)은 자율이동로봇(AMR)의 하드웨어·소프트웨어 정보를 자산관리셸(AAS)로 기록해 JSON 으로 저장·송수신하고 OPC UA 로 실시간 감시하는 모니터링 시스템 설계를 제안했으나, 초록은 실제 현장 적용 결과를 적지 않는다. | ref-043 | 아니오 | medium | 2024 | — | — |
| f18 | [추정] | oq-128 관련: 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구(f17)와 벤더의 이기종 관제 소개(f16)뿐이며, VDA 5050 팩트시트나 자산관리셸 능력 기술을 실제 로봇 등록 데이터로 운영에 쓴 국내 사례는 이번 조사에서 확인되지 않아 oq-128 은 미해결로 남는다. | ref-043, ref-875 | 아니오 | low | 2026-09-29 | — | — |
| f19 | [사실] | Dussard·Sarthou(2026)는 URDF 가 로봇의 구조·운동학은 기술하지만 식별자에 의미가 없다는 점을 들어, 기존 온톨로지의 개념을 프롬프트에 넣어 언어 모델이 URDF 요소의 의미 관계를 추론하게 하고 여러 번 질의한 다수결과 구문·스키마 검증으로 출력을 제약해 로봇 온톨로지를 자동으로 채우는 방법을 여러 로봇 기술로 평가했다. | ref-239 | 아니오 | medium | 2026-06-10 | — | — |
| f20 | [사실] | Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 능력의 자연어 설명을 정해진 프롬프트에 넣어 언어 모델이 능력 온톨로지를 생성하고, 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행한 뒤 사람이 최종 검토·수정만 하게 하는 방법을 제안해 수작업 모델링 부담을 줄였다고 보고했다. | ref-465 | 아니오 | medium | 2024-10-18 | 완료·인계 | — |
| f21 | [사실] | Abolhasani·Pan(2024)의 OntoKGen 은 신뢰성·유지보수성 분야 기술 문서에서 언어 모델로 온톨로지와 지식 그래프를 뽑되, 대화형 인터페이스에서 시스템이 모범 사례 기반 온톨로지를 추천하고 사용자가 최종 결정을 갖게 하는 방식으로 '보편적으로 옳은 온톨로지는 없다'는 전제를 두고 사용자 검토를 설계의 중심에 두었다. | ref-883 | 아니오 | medium | 2024-12-10 | 완료·인계 | — |
| f22 | [사실] | 서로 다른 세 연구 그룹(LAAS 의 URDF 온톨로지 채우기, 헬무트 슈미트 대학 계열의 자연어 능력 온톨로지 생성, Abolhasani·Pan 의 기술 문서 온톨로지 추출)이 언어 모델 추출에 자동 검증이나 사용자 최종 검토를 결합한 방법을 각각 보고해, '자동 추출 + 자동 검증 + 사람 최종 검토' 구성이 한 곳 이상에서 확인된다. | ref-239, ref-465, ref-883 | 예 | medium | 2026-06-10 | 완료·인계 | — |
| f23 | [추정] | 이 영역이 요구하는 '원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만들고 사람이 대조해 확정·반려'하는 흐름은 f20·f21 의 사람 최종 검토와 방향이 같지만, 확인한 세 연구 어느 것도 추출 항목마다 매뉴얼의 절·줄 위치를 붙여 검토자가 대조하게 하는 근거 연결을 초록에서 밝히지 않아 근거 연결형 검토·승인은 아직 확인되지 않은 요구로 보인다. | ref-465, ref-883, ref-239 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f24 | [추정] | 확인한 자료를 종합하면 4. 이기종 로봇 등록에서 ROP가 직접 맡을 범위는 제조사·기종·일련번호·펌웨어·SDK 버전·장착 장비를 담는 등록부, 팩트시트·자산관리셸·신원 보고를 받아 저장·대조하는 수집 경로, 문서·URDF에서 뽑은 능력 초안의 검토·승인 기록, 어댑터 설정 초안 생성이며, 등록 승인 관문에 벤더·통합사 사전 평가(f15)를 둘 수 있을 것으로 보인다. | ref-031, ref-198, ref-153, ref-878 | 아니오 | low | 2026-09-29 | — | — |
| f25 | [추정] | 연계 대상: 팩트시트의 위치추정 방식·주행 방식(localizationTypes·navigationTypes)과 mobileRobotConfiguration 의 펌웨어·소프트웨어 버전은 제조사가 소유·갱신하는 로봇 자체 지능·제어 정보이므로, 이종 제조사를 잇는 ROP 는 등록 시 이를 받아 저장·대조하고 버전 변경을 추적하는 데 그치고 위치추정·회피 성능 자체는 제조사에 맡겨야 할 것으로 보인다. | ref-228, ref-031 | 아니오 | low | 2026-09-29 | 제약 | — |
| f26 | [추정] | 언어 모델로 URDF·자연어·기술 문서에서 온톨로지를 추출하는 연구(f19~f22)는 L. AI·학습 기술의 45. 문서·도면·장면 이해와 47. AI·학습·적응과 모델 운영에 속하는 방법이며 원문 교차 규칙(매뉴얼 해석은 4·55번)에 따라 이 영역과 55. 현장 조사·설치·시운전에 연결해야 하고, 등록 데이터는 5. 로봇 능력·작업 표현(능력 표현), 6. 온톨로지 기반 시스템·로봇 연동(어댑터 설정), 7. 온톨로지 검증·변경 관리와 57. 자산·소프트웨어 수명주기 관리(펌웨어·문서 개정), 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성(팩트시트·자산관리셸 규격)에 연결된다. | ref-239, ref-198, ref-153 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-228 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050/json_schemas/factsheet.schema (main) | 미확인 | 표준 | high | 2026-09-29 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-198 | Industrial Digital Twin Association (IDTA) | IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics | 2025-03 | 표준 | high | 2026-09-29 | https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf | 아니오 |
| ref-230 | MassRobotics (AMR Interoperability Working Group) | AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema | 미확인 | 표준 | high | 2026-09-29 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.17073 | 아니오 |
| ref-153 | Open Robotics (Programming Multiple Robots with ROS 2) | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-874 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-09-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-875 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 | 2025-11-09 | 기사 | low | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 아니오 |
| ref-876 | Industrial Digital Twin Association (IDTA) | IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment | 미확인 | 표준 | high | 2026-09-29 | https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf | 아니오 |
| ref-043 | 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)) | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 2024 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560 | 아니오 |
| ref-878 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | 정부·연구기관 | medium | 2026-09-29 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 아니오 |
| ref-031 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main) | 미확인 | 표준 | high | 2026-09-29 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-880 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README) | 미확인 | 표준 | high | 2026-09-29 | https://github.com/admin-shell-io/aas-specs-api | 아니오 |
| ref-881 | OPC Foundation | OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02) | 2025-09-08 | 표준 | high | 2026-09-29 | https://reference.opcfoundation.org/Robotics/v100/docs/ | 아니오 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-10-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.07962 | 아니오 |
| ref-883 | Abolhasani, M. S., & Pan, R. | Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation | 2024-12-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2412.00608 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/robot-ontology/heterogeneous-robot-registration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f7(세 표준 기관이 제조사 제공 등록 기록을 공통으로 요구), f14(등록 작업이 설정 파일+API 구현으로 이루어짐), f15(공공 의료의 벤더 사전 평가 관문) / 섹션 4: f1·f2(팩트시트 필수 속성·기종 제원 항목), f5(디지털 명판 필수 식별자·버전), f6(신원 보고), f19(URDF 는 구조·운동학 기술, 온톨로지 채우기), f10(자산관리셸 레지스트리·디스커버리) / 섹션 5: 병원 — f13(타르투대학교병원, FreeFleet·어댑터 파일 등록, 문 통과 보조 장치, 검체 운반), f15(싱가포르 공공 의료기관의 RoMi-H 등재 프로그램), 기타 — f16(인천공항 다기종 로봇 사업, 벤더 주장 병기), 제조 공장·물류창고 사례는 이번 조사에서 확인되지 않음을 서술 / 섹션 6: 등록 데이터 수집 f3(팩트시트 요청·게시)·f11(자산관리셸 경로, 추정), 어댑터 설정 등록 f12·f14, 문서·URDF·자연어에서 능력 추출 f19·f20·f21·f22, 검토·승인 f20·f21·f23(근거 연결형 검토는 미확인), 표준 문서의 AI 가독 형식 f9 / 섹션 7: f1·f2·f3(VDA 5050 팩트시트 스키마·명세), f4(IDTA 02047), f5(IDTA 02006), f6(MassRobotics), f8·f9(OPC UA Robotics), f10(자산관리셸 API), f12(Open-RMF 플릿 어댑터) / 섹션 8: f13, f19, f20, f21, 국내 f17 / 섹션 9: f24(직접 범위: 등록부, 수집 경로, 검토·승인 기록, 어댑터 설정 초안, 승인 관문), f25(연계 대상: 위치추정·주행 방식·펌웨어는 제조사 소유) / 섹션 10: f26 — 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 63. 병원·의료(f13·f15) / 섹션 11: 기존 oq-128(f17·f18 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지에 f13·f15 반영, 21. 상호운용 표준·적합성 페이지에 f7·f8 반영, 45. 문서·도면·장면 이해 페이지에 f19·f22 반영, 트랙 manual-capability-ontology 단계 2(문서 유형)에 f9·f19·f20 참고. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 디지털 명판 | Digital Nameplate (IDTA 02006) | 제품 URI·제조사·제품명·일련번호·제조 연도·제조일을 필수로 담고 하드웨어·펌웨어·소프트웨어 버전을 선택으로 두는 자산관리셸 서브모델로, 산업 장비의 명판 정보를 기계가독 형식으로 교환하게 한다. |
| AGV 기술 데이터 서브모델 | Technical Data for AGV in Intralogistics (IDTA 02047) | 실내 물류용 AGV·AMR 의 유형·기술 매개변수·VDA 5050 팩트시트·에너지·통신·배터리·안전·임시 기술 데이터를 컬렉션으로 나눠 담는 자산관리셸 서브모델 템플릿이다. |
| 통합 로봇 기술 형식 | Unified Robot Description Format (URDF) | 로봇의 링크와 관절로 구조·운동학·물리 속성을 기술하는 ROS 계열의 XML 형식으로, 식별자 자체에는 의미가 없어 온톨로지로 옮기려면 해석이 필요하다. |
| 자산관리셸 레지스트리·디스커버리 | AAS Registry / Discovery | 자산관리셸 API 명세(IDTA-01002)가 정한 서비스로, 등록된 자산관리셸과 서브모델의 서술자를 관리하고 자산 식별자로 해당 자산관리셸을 찾게 한다. |
| 온톨로지 채우기 | Ontology Population | 이미 정해진 온톨로지의 개념·관계에 맞춰 문서·모델 파일 같은 원천에서 개체와 관계 인스턴스를 뽑아 채우는 작업으로, 언어 모델을 쓸 때는 검증과 사람 검토를 함께 둔다. |

## 열린 질문

새로 생긴 질문:

- 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 45. 문서·도면·장면 이해, 7. 온톨로지 검증·변경 관리 | 근거: f23 | 종류: 일반
- VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? | 관련 영역: 4. 이기종 로봇 등록, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f7 | 종류: 일반
- 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 63. 병원·의료, 58. 다사업자 책임·계약·데이터 | 근거: f15 | 종류: 일반
- 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 3
- 예산 사용량: 검색 14회 · 신규 출처 15건
- 미확인 항목:
    - MDPI Applied Sciences 자동차 공장 다중 브랜드 플릿 통합 사례(제조 공장 사례 후보)는 두 경로 모두 403 으로 열지 못해 넣지 않음 — 제조 공장 현장 유형 사례 미확보
    - f16 클로봇 크롬스 공식 페이지(clobot.co.kr/croms) 403 — 'VDA 5050 기반 FMS' 문구는 검색 결과 요약에서만 보여 claim 에 넣지 않음, 벤더 주장 미교차
    - URDF 공식 문서(wiki.ros.org 는 Anubis 차단, docs.ros.org 차단, ros2_documentation raw 경로 404) 미열람 — URDF 서술은 ref-239 초록의 '구조·운동학 기술' 문구에만 기댐
    - Springer 'Conversational Knowledge Extraction from Technical Manuals'(ECML PKDD 2025)는 인증 리다이렉트로 열지 못해 넣지 않음
    - f4 IDTA 02047 PDF 는 컬렉션 이름과 관련 서브모델까지만 확인했고 개별 속성명·VDA 5050 팩트시트 대응 세부는 추출 응답이 얇아 미확인
    - f5 IDTA 02006 3.0 발행일 불확실(도구 응답 2024-11, 파일명 3-0-1 판 2025-10 게시) — published null
    - f11 자산 ID→AAS ID→엔드포인트 흐름은 IDTA Part 2 PDF 검색 결과 요약에서만 확인, 원문 미열람
    - f15 RoMi-H 등재 평가의 기술 항목(어댑터 시험·적합성 검사 등)은 공지에 없어 미확인
    - f17 KCI 논문 초록만 확인 — 서브모델 구성(명판·기술 데이터 등)과 현장 적용 결과 미확인
    - f19·f20·f21 정량 결과는 초록에 없어 미확인
    - f1·f2·f3·f6·f10·f12 출처 발행일 미확인(저장소 원문)
    - oq-128 미해결(f18)
    - f7·f14·f22 외 모든 finding 교차 확인 실패(표준·연구마다 발행 주체 한 곳)
- 범위 경계 위반 의심:
    - f25: 팩트시트의 위치추정·주행 방식과 펌웨어 버전은 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f15: 벤더 등재 제도는 58. 다사업자 책임·계약·데이터와 겹치므로 이 영역에서는 등록 승인 관문 사례로만 제안함
    - f8·f9: OPC UA Robotics 는 산업용 매니퓰레이터의 수직 통합 규격이므로 등록 식별 속성과 문서 형식 근거로만 제안하고 제어 연동은 다루지 않음
    - f19~f22: 언어 모델 추출 연구는 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f26)
- 한계: web_fetch_available: true · fetch_mode full. 검색 14회/30, 신규 출처 15건/15(ref-228~ref-883, 예약 구간 안) 상한 도달로 URDF 공식 문서, IDTA Part 2 API PDF, HERMES 검토 작업대, OntoKGen 외 매뉴얼 추출 논문, IFR 의 VDA 5050 해설을 넣지 못했다. 원문 열람 15건(github_raw 5: 팩트시트 스키마·VDA5050_EN.md·MassRobotics JSON·Open-RMF 튜토리얼·aas-specs-api README, webfetch 10: IDTA 02047·02006 PDF, arXiv 초록 3건, Frontiers 전문, KCI 초록, CGH 공지, OPC Foundation 참조 페이지, 로봇신문 기사). 재사용 출처 없음(참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 전체 868건과의 URL 중복을 대조하지 못했으므로 Open-RMF 튜토리얼·VDA 5050 저장소·MassRobotics 저장소는 퍼블리셔가 기존 id 로 합칠 수 있다). 교차 확인 3건(f7: VDA·MassRobotics·IDTA, f14: Open Robotics·타르투대학교, f22: LAAS·헬무트 슈미트 대학 계열·Abolhasani·Pan — 모두 발행 주체가 다름). 신뢰도 high 는 f7·f14 두 건(각각 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(제조사도 형식도 다른 로봇을 빠르고 믿을 수 있게 등록)에는 f3·f7(제조사가 기계가독 기록을 제공하고 로봇이 요청에 게시), f12·f14(등록은 설정 파일+API 구현), f19·f20·f21·f22(문서·URDF 에서 자동 추출 후 검증·사람 검토), f15(벤더 사전 평가 관문)로 답했으며 결론은 '식별·제원은 세 표준이 겹치게 정해 두었지만 능력 추출의 근거 연결형 검토와 형식 간 대응은 확인되지 않았다'는 추정(f11·f23·f24)이다. 현장 유형: 병원(f13 타르투대학교병원, f15 싱가포르 공공 의료기관), 기타(f16 인천공항, 벤더 주장)만 확인했고 제조 공장·물류창고·상업 시설·가정·실외 사례는 없다(제조 공장 후보 MDPI 논문은 403). 국내 자료는 KCI 논문(f17)과 로봇신문 기사(f16) 두 건이며 국내 운영 사례는 찾지 못해 oq-128 은 미해결이다. L. AI·학습 기술 관련 finding(f19~f23)은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 이 영역·55. 현장 조사·설치·시운전 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(IDTA 02047 의 TemporaryTechnicalData 는 f4 에 이름만 적음). 벤더 문서 출처는 없고 벤더 주장은 기사 경유 f16 한 건(vendor_claim). 용어집에 이미 있는 VDA 5050 팩트시트·신원 보고·자산관리셸·소프트웨어 명판·능력 기술 서브모델·의미 식별자·플릿 어댑터·플러그 앤 프로듀스는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음.
```

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

### runs/2026-09-25-17/research.md

```markdown
# 리서치 브리프 2026-09-25-17

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-17 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 좌표계·층·지도 정합·지도 버전·위치추정 신뢰도 용어 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 반영 제안(평면도 인식 세 갈래) 미반영
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안(공개 데이터셋·오픈소스) 미반영
- 섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안(DeepFloorplan, Raster-to-Graph, VLM 지도 파싱) 미반영
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 트랙 반영 제안(창고 평면도·충전 위치 라벨 데이터셋 부재) 미반영, 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 원문 주석이 요구하는 '현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도' 근거 없음
- 이전 트랙 실행 2026-09-25-11 이 traffic-editor·osmAG·BIM 지도 생성 출처를 ref-079~ref-095 로 제안했으나 참고문헌 목록의 해당 id 는 다른 출처라 게시되지 않은 것으로 보여 필요한 것은 새 id 로 다시 열었음

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. 이동로봇 인터페이스 규격(VDA 5050, MassRobotics, Open-RMF, ISO 21423)은 위치·지도·좌표계·층을 어떤 필드로 표현하며, 제조사 사이 좌표 변환은 어떻게 하는가? (섹션 4·6·7 겨냥)
3. 지도 버전 관리와 배포(지도 활성화·교체, 변경 탐지)는 규격과 연구에서 어떻게 다루는가? (원문 주석, 섹션 6·7 겨냥)
4. 위치추정 결과의 신뢰도는 규격에서 어떻게 보고되고, 연구는 위치추정 안전성·무결성을 어떻게 정량화하는가? (원문 주석, 섹션 4·6·8 겨냥)
5. 건축 도면(래스터·벡터 CAD·BIM/IFC)과 실내 공간 표준(IFC, IndoorGML, ISO 19164, LIF)은 이동 공간·경로·장소를 어떻게 기술하며, 도면과 현장의 차이는 어떻게 확인하는가? (섹션 6·7·8, 트랙 반영 제안 겨냥)
6. 업무상 장소(출하 대기장·도크)를 식별하는 업무 식별자(GS1 GLN)와 로봇 지도 위 장소를 잇는 방법이 있는가, 국내 연구·표준은 무엇이 있는가? (섹션 5·10, 한국 자료 우선)
7. 지도·공간·위치 모델에서 ROP가 직접 맡을 부분과 로봇 자체 위치추정·SLAM에 맡길 부분의 경계는 어디인가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 이동로봇 위치를 프로젝트별 좌표계(오른손 좌표계, 미터·라디안) 안의 x·y·theta 와 함께 위치추정 초기화 여부(positionInitialized), 자세 신뢰도 0~1 값(localizationScore), 노드에서의 위치 정확도 범위(deviationRange), 사용 중인 좌표계를 가리키는 지도 식별자(mapId)로 보고하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 로봇 상태의 지도 목록에 mapId·mapVersion·mapStatus(ENABLED/DISABLED)를 필수로 두고, 즉시 동작 downloadMap(지도 내려받기)·enableMap(내려받은 지도 활성화, 같은 지도의 다른 판은 비활성화)·deleteMap(지도 삭제)으로 관제가 지도 판을 배포·교체하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 은 지도마다 구역 집합(zoneSetId, 하나의 mapId 에 연결)을 두고 mapId 당 하나만 활성화하게 하며, 구역 유형으로 통행 금지(BLOCKED)·속도 제한(SPEED_LIMIT)·우선(PRIORITY)·방향 지정(DIRECTED) 등을 정의한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | MassRobotics AMR 상호운용 표준의 공식 JSON 스키마는 상태 보고의 위치를 x·y·z·각도(쿼터니언)와 참조하는 평면 기준(planarDatum, UUID)으로 두지만, 평면 기준의 원점·좌표계를 정의하는 메시지와 위치추정 신뢰도 필드는 스키마에 두지 않는다. | ref-033 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f5 | [사실] | Open-RMF API 의 로봇 상태 스키마는 위치를 지도 이름(map)·x·y·yaw 네 필수 필드의 2차원 위치(location_2D)로 보고하며, 위치추정 불확실성을 담는 필드는 두지 않는다. | ref-148, ref-155 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | Open-RMF traffic-editor 는 평면도 이미지를 로봇 교통 지도를 그리는 배경으로 들여와 기본 축척(1픽셀=5cm)을 두 점 사이 실측 거리 입력으로 보정하고, 층마다 대응하는 기준점(fiducial) 2쌍 이상으로 층 사이 이동·회전·축척 변환을 구하며, 로봇이 만든 지도를 레이어로 올려 축척·이동·회전으로 평면도에 맞추게 한다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | traffic-editor 는 경로 정점에 충전 위치(is_charger)·주차 위치(is_parking_spot)·대기 지점(is_holding_point)·이름 붙은 장소 속성을 사람이 주석하게 하고, 문(여닫이·미닫이 등 유형)·승강기·벽을 함께 기술한 결과를 .building.yaml 로 저장하며 building_map_generator 가 이를 시뮬레이션 월드로 만든다. | ref-079 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 통합 문서는 로봇 경로 지도로 경유점마다 층 이름(B1·L1 등)과 층 안 미터 단위 (x, y) 좌표, 충전·주차·비상 대피 지점 같은 기능 속성을, 간선마다 일방·양방향과 속도 제한을 요구하고, 받을 수 있는 형식으로 YAML·XML·텍스트·DXF·DWG·SVG 를 들며 텍스트 자료는 화면 캡처로 좌표계·건물 정렬을 점검하라고 권한다. | ref-080 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 플릿 어댑터는 로봇 좌표계가 RMF 와 다를 때 층별로 같은 위치를 가리키는 RMF 좌표와 로봇 좌표 쌍(reference_coordinates)을 설정에 적고, nudged 라이브러리로 두 좌표계 사이 회전·축척·이동 변환과 변환 오차를 추정하며, 대응 경유점을 4개 이상 두도록 권한다. | ref-154, ref-105 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | ROS 의 REP 105 는 이동로봇 좌표계를 연속적이지만 한없이 드리프트할 수 있는 odom 과, 드리프트가 크지 않은 대신 위치 보정 때문에 불연속 점프가 생기는 장기 전역 기준 map 으로 나누고, 여러 지도를 오가는 경우 공통 기준으로 earth 좌표계를 두게 한다. | ref-156 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | VDMA 의 LIF(Layout Interchange Format) 1.0.0(2023-09)은 무인운반차 통합사가 간선·노드·스테이션으로 이루어진 주행 레이아웃을 제3자 중앙 관제 시스템에 처음 넘기기 위한 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받았다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f12 | [사실] | ISO 21423 은 서로 다른 공급사의 산업용 자율이동로봇(AMR) 시스템과 플릿 관리자 사이의 상호운용을 위한 통신을 다루는 ISO 로봇 분야 규격이며, 발행 여부는 이번 확인 범위에서 미확인이다. | ref-161 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [추정] | ISO 21423 초안은 같은 환경의 모든 이동로봇과 플릿 관리자가 기준점 3개 이상으로 정의한 공유 공통 좌표계(CCS)로 위치를 주고받고 지도 변환을 하게 하는 것으로 요약된다. | ref-161 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | IFC 4.3 문서는 IfcSpace 를 건물 안에서 특정 기능을 제공하는 실제·이론상 경계 지어진 면적·체적으로 정의하고, 공간을 건물 층(IfcBuildingStorey)에 집합 관계(IfcRelAggregates)로 연결하며, 공간 바닥 높이(ElevationWithFlooring)를 속성으로 둔다. | ref-157 | 아니오 | medium | 2026-09-25 | — | — |
| f15 | [사실] | OGC IndoorGML 2.0 은 Part 1 개념 모델이 공개되었고 Part 2 인코딩은 작업 중이며, Part 2a XML 인코딩 초안은 실내 공간 분할(CellSpace·경계), 공간 연결을 나타내는 노드·엣지의 쌍대 그래프, 의미별 주제 레이어(ThematicLayer), 레이어 간 연결(InterLayerConnection)을 GML 3.2.1 로 인코딩한다. | ref-158 | 아니오 | medium | 2026-09-25 | — | — |
| f16 | [사실] | ISO 19164:2024 는 건물 실내 위치 기반 응용에 공통으로 필요한 실내 지물의 의미 분류 체계와 속성·지물 간 연관을 정하며 기하·위상 기술은 다루지 않고, OGC IndoorGML 이 이를 구현하는 표준으로 소개된다. | ref-159 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f17 | [사실] | GS1 글로벌 로케이션 번호(GLN)는 물리적 위치와 그 안의 하위 위치(도크 문·보관 위치 등)를 식별할 수 있고, 하위 위치는 GLN 확장 요소로도 식별하되 이 확장 요소는 조직 내부나 거래 당사자 간 합의로만 쓴다. | ref-164 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f18 | [추정] | 분류 원문 질문(제조사마다 다른 지도에서 ‘3층 출하 대기장’을 같은 장소로 인식)에 답하려면 (1) 층별 좌표 변환(Open-RMF 기준 좌표 쌍, ISO 21423 공통 좌표계 초안), (2) 지도·층 식별자 대응(VDA 5050 mapId, Open-RMF 지도·층 이름, MassRobotics planarDatum), (3) 업무 장소 식별자(GLN 하위 위치)와 지도 위 이름 붙은 경유점·스테이션의 대응 표가 함께 필요할 것으로 보이며, 이 대응을 한 규격이 정하는 것은 확인되지 않았다. | ref-154, ref-161, ref-031, ref-080, ref-033, ref-164, ref-079 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f19 | [사실] | Prakhya 외의 평생 3D 지도 작성 틀은 동적 점 제거, 여러 세션 지도의 자동 정합, 두 지도 사이 추가·제거 변화 탐지, 현재 상태의 기준 지도 하나와 변화분만 저장해 이전 세션 지도를 복원하고 두 세션 간 변화를 조회하는 지도 버전 관리로 구성된다. | ref-162 | 아니오 | medium | 2025-01 | — | 원문 미열람 |
| f20 | [추정] | 랙·팔레트 배치 변경으로 지도가 바뀌는 창고에서는 변화 탐지로 만든 새 지도 판을 제조사마다 배포·활성화(VDA 5050 mapVersion·enableMap)해야 하므로, 여러 제조사 지도의 판 번호와 활성 시점을 함께 기록하지 않으면 같은 장소의 좌표 대응이 판마다 어긋날 수 있을 것으로 보인다. | ref-031, ref-162, ref-154 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f21 | [사실] | Abdul Hafez·Joerger·Spenko(IJRR 2025)는 항공 분야의 무결성 위험(integrity risk) 지표를 EKF 기반 SLAM 위치추정에 적용해 센서 측정 결함을 고려한 위치추정 안전성을 정량화했고, 데이터 연관 오류가 이 지표로만 예측되는 큰 위치 성능 저하를 낼 수 있다고 보고했다. | ref-163 | 아니오 | medium | 2025-05 | 예외·성과 | 원문 미열람 |
| f22 | [추정] | 확인한 규격에서 위치추정 신뢰도는 VDA 5050 만 0~1 점수와 정확도 범위로 보고하고 MassRobotics 스키마와 Open-RMF 로봇 상태에는 해당 필드가 없어, 이종 제조사 로봇의 위치 신뢰도를 같은 기준으로 비교·수용하는 규칙은 ROP 쪽에서 따로 정해야 할 것으로 보인다. | ref-031, ref-033, ref-155 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f23 | [사실] | arXiv 2408.01737 연구는 건축 도면에서 만든 계층 그래프(A-Graph)와 3D 라이다로 추정한 상황 그래프(S-Graph)를 결합해 로봇 위치와 함께 도면(as-planned)과 현장(as-built)의 정렬·구조 편차를 실시간 추정하고, 최대 35cm·15도 편차까지 견고했다고 보고했다. | ref-224 | 아니오 | medium | 2024-08 | — | 원문 미열람 |
| f24 | [사실] | 노주형 외(로봇학회 논문지, 2026)는 3D 라이다–IMU SLAM 과 다중 센서 비용 지도로 탐사 경계를 만들고 RGB-D 카메라와 4자유도 팔로 승강기 버튼을 눌러 층을 옮겨 가며 사람 개입 없이 다층 실내 지도를 구축하는 시스템을 제시했다. | ref-165 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f25 | [사실] | 래스터 평면도 인식 연구에는 방 경계 유도 주의를 쓰는 다중 작업 신경망으로 벽·문·방 유형을 분할하는 DeepFloorplan 과, 래스터 평면도의 의미 분할을 개선해 다세대 평면도를 인식·재구성하는 Kratochvila 외(2024)가 있다. | ref-064, ref-078 | 아니오 | medium | 2024-08 | — | 원문 미열람 |
| f26 | [사실] | 평면도를 기하 구조로 바꾸는 접근에는 래스터 평면도를 벽 선분·방 다각형 같은 벡터 표현으로 바꾸는 Raster-to-Vector(2017)와, 주의 트랜스포머로 평면도의 구조 그래프를 자기회귀 방식으로 예측하는 Raster-to-Graph(2024)가 있다. | ref-065, ref-070 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f27 | [사실] | 벡터 CAD 도면 인식은 선 요소마다 문·창문 같은 기호 인스턴스와 벽 같은 영역 의미를 함께 판별하는 파놉틱 심볼 스포팅 과제로 다뤄지며, FloorPlanCAD(2021)와 ArchCAD-400K(2025)가 이 과제용 대규모 데이터셋을 공개했다. | ref-067, ref-073 | 예 | medium | 2025-03 | — | 원문 미열람 |
| f28 | [사실] | 공개 평면도 데이터셋으로 CubiCasa5K(평면도 이미지 분석), MLStructFP(다세대 평면도), ResPlan(주거 평면도 1만 7천 건의 벡터·그래프), 국내 AI Hub 건축 도면 데이터가 있다. | ref-063, ref-069, ref-071, ref-074 | 아니오 | medium | 2025-08 | — | 원문 미열람 |
| f29 | [추정] | 이전 트랙 실행은 FloorPlanCAD 주석이 비상업(CC BY-NC 4.0) 조건이고 ResPlan 이 CC BY 4.0 이라고 보고해, 공개 평면도 데이터셋을 상용 도면 인식에 쓰려면 데이터셋별 라이선스 검토가 필요할 것으로 보인다. | ref-066, ref-071 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f30 | [사실] | DeFazio 외(2024)는 시각–언어 모델(VLM)이 평면도 지도를 해석해 로봇 이동 과업 계획에 쓸 수 있는지 평가했고, 조밀하게 라벨이 붙은 평면도와 최대 아홉 단계 과업 조건에서 GPT-4o 의 성공률 0.96 을 보고했다. | ref-076 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f31 | [추정] | 도면에서 만든 지도·공간 모델에는 충전·대기 위치 같은 로봇 운영 요소와 도면–현장 편차가 자동으로 담기지 않아, traffic-editor 처럼 사람이 주석하고 축척·정렬을 맞추거나 위치추정 쪽에서 편차를 추정하는 단계가 남는 것으로 보인다. | ref-079, ref-224, ref-080 | 아니오 | low | 2026-09-25 | 제약 | — |
| f32 | [추정] | 연계 대상: 로컬 지도 작성·SLAM·위치추정 계산은 분류 원문 9장의 로봇 자체 지능·제어 쪽이고, 이종 제조사를 연결하는 ROP는 제조사 지도와 공통 좌표계 사이 변환, 층·지도 식별자와 업무 장소 대응, 지도 판 관리, 보고된 위치 신뢰도의 수용 기준을 맡는 경계가 될 것으로 보인다. | ref-156, ref-031, ref-154, ref-163 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-033 | MassRobotics | Autonomous Mobile Robot Standards Published by MassRobotics | 2021-05 | 표준 | medium | 2026-09-25 | https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/ | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1904.01920 | 예 |
| ref-064 | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 2019 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/zlzeng/DeepFloorplan | 예 |
| ref-065 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 2017 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/art-programmer/FloorplanTransformation | 예 |
| ref-066 | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 2021 | 오픈소스 문서 | medium | 2026-09-25 | https://floorplancad.github.io/ | 예 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2105.07147 | 예 |
| ref-069 | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 2023 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/MLSTRUCT/MLStructFP | 예 |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 2024 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/SizheHu/Raster-to-Graph | 예 |
| ref-071 | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 2025-08 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/m-agour/ResPlan | 예 |
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.22346 | 예 |
| ref-074 | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465 | 예 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.12842 | 예 |
| ref-078 | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 2024-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2408.01526 | 예 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html | 아니오 |
| ref-154 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-155 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/location_2D.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/location_2D.json | 아니오 |
| ref-156 | ROS (ros-infrastructure/rep) | REP 105 -- Coordinate Frames for Mobile Platforms | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://www.ros.org/reps/rep-0105.html | 아니오 |
| ref-157 | buildingSMART International | IFC 4.3 documentation — IfcSpace (IFC4.3.x-development) | 미확인 | 표준 | high | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md | 아니오 |
| ref-158 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | IndoorGML-SWG — README and OGC IndoorGML 2.0 Part 2a – XML Encoding (26-042, Candidate SWG Draft) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/opengeospatial/IndoorGML-SWG | 아니오 |
| ref-159 | ISO | ISO 19164:2024 - Geographic information — Indoor feature model | 2024 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83153.html | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (LIF – Layout Interchange Format, Version 1.0.0) | 2023-09 | 표준 | medium | 2026-09-25 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-161 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/86749.html | 예 |
| ref-162 | Prakhya, S. M., Yang, L., & Liu, Z. | Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems | 2025-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2501.18110 | 예 |
| ref-163 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 2025-05 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/02783649241287797 | 예 |
| ref-164 | GS1 | Identifying a physical location - GLN | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/standards/id-keys/gln/physical-location | 예 |
| ref-165 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |
| ref-224 | arXiv:2408.01737 저자(미확인) | Tightly Coupled SLAM with Imprecise Architectural Plans | 2024-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2408.01737 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f18(제조사별 좌표계·지도 식별자·업무 장소가 따로 놀아 같은 장소 인식에 대응 계층 필요), f20·f22(지도 판·위치 신뢰도가 제조사마다 다름) / 섹션 4: f1(mapId·localizationScore·deviationRange), f2(지도 판·활성화), f3(구역 집합), f10(map·odom·earth 좌표계), f6(기준점·축척), f14(IfcSpace), f15(IndoorGML 셀 공간·쌍대 그래프), f17(GLN 하위 위치), f21(무결성 위험) / 섹션 5: 출하 단계 — 완료·인계 f17·f18(3층 출하 대기장 도착 확인을 업무 장소 식별자와 지도 장소 대응으로), 적치 단계 예외·성과 f20(레이아웃 변경 뒤 지도 판 불일치), 예외·성과 f22 — 흐름 단계와 여섯 항목 명시 / 섹션 6: f9·f6(기준점 기반 좌표 변환), f2·f19·f20(지도 버전 관리), f21·f22(위치추정 신뢰도), f23·f31(도면–현장 편차), 트랙 반영 제안 6절(평면도 인식 세 갈래) f25·f26·f27 — 교차 규칙에 따라 도면 해석 AI 는 27. AI·학습·적응과 모델 운영과 양쪽 연결, 축척 복원이 별도 과제라는 이전 제안은 이번에 재확인 못 해 넣지 않음 / 섹션 7: f1~f3(VDA 5050 3.0.0), f4(MassRobotics), f5·f6~f9(Open-RMF traffic-editor·경로 지도·어댑터 변환·API 위치), f10(REP 105), f11(LIF), f12·f13(ISO 21423, 추정 병기), f14(IFC), f15·f16(IndoorGML·ISO 19164), f17(GS1 GLN), 트랙 반영 제안 7절 f28·f29(공개 데이터셋, 라이선스는 추정) / 섹션 8: f19·f21·f23·f24(국내 다층 지도 구축), 트랙 반영 제안 8절 f25·f26·f30(VLM 은 도면 해석 방법으로만) / 섹션 9: f32(연계 대상: SLAM·위치추정은 로봇 쪽, ROP 는 좌표 변환·식별자 대응·지도 판·신뢰도 수용 기준) / 섹션 10: 7. 화물·재고·자산 식별과 추적(f17 업무 위치·GLN), 8. 실시간 세계 상태·데이터 일관성(f1·f5 현재 위치 보고, f22), 9. 로봇·제조사 관제 연동(f1~f5·f9), 10. 설비·건물 시스템 연동(f7·f24 승강기·문), 15. 다중 로봇 경로·교통 관리 — MAPF(f3·f8 간선·구역), 21. 온보딩·설정·현장 시운전(f6·f9·f31 시운전 정렬), 22. 시뮬레이션·예측용 디지털 트윈(f7 시뮬레이션 월드 생성만), 24. 자산·소프트웨어 수명주기 관리(f2·f19 지도 판), 25. 안전·위험 관리(f21), 27. AI·학습·적응과 모델 운영(f25~f30), 28. 표준·상호운용성·다사업자 거버넌스(f11~f13·f15·f16) / 섹션 11: open_questions_new 3건과 트랙 반영 제안 11절(창고 평면도·충전 위치 라벨 데이터셋 부재, 트랙 백로그 q1-05·q2-04 연결 — 이번 실행은 재조사하지 않았으므로 트랙 근거 그대로 연결). 트랙 반영 제안 4건(2026-09-25-05) 모두 다룸 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| IndoorGML | IndoorGML | 실내 공간을 셀 공간과 그 경계, 공간 연결을 나타내는 노드·엣지의 쌍대 그래프, 주제 레이어로 표현하는 OGC 실내 공간 정보 표준이다. |
| 산업 기초 클래스 | Industry Foundation Classes (IFC) | BIM 소프트웨어 사이에서 공간(IfcSpace)·층·문 같은 건물 요소와 속성을 교환하기 위한 buildingSMART 의 개방형 데이터 스키마이다. |
| 레이아웃 교환 형식 | Layout Interchange Format (LIF) | 무인운반차 통합사가 노드·간선·스테이션으로 이루어진 주행 레이아웃을 제3자 관제 시스템에 넘기기 위해 VDMA 가 정한 교환 형식이다. |
| 지도 정합 | Map Alignment | 서로 다른 로봇·도면의 지도 좌표계를 대응점으로 구한 회전·축척·이동 변환으로 공통 좌표계에 맞추는 일이다. |

## 열린 질문

새로 생긴 질문:

- ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? | 관련 영역: 6. 지도·공간·위치 모델, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f13 | 종류: 일반
- 제조사마다 계산 방식이 다른 위치추정 신뢰도(VDA 5050 localizationScore 등)나 신뢰도 필드가 없는 로봇의 위치 보고를 ROP 가 같은 기준으로 수용·거부하는 방법이 있는가? | 관련 영역: 6. 지도·공간·위치 모델, 8. 실시간 세계 상태·데이터 일관성 | 근거: f22 | 종류: 일반
- 국내 물류센터에서 GLN 하위 위치나 WMS 로케이션 코드를 로봇 지도 위 경유점·스테이션과 대응시켜 목적지로 쓰는 사례가 있는가? | 관련 영역: 6. 지도·공간·위치 모델, 7. 화물·재고·자산 식별과 추적 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 31 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f13 ISO 21423 공통 좌표계 '기준점 3개 이상' 서술의 1차 출처(ISO 원문 여부) 미확인, 발행 여부 미확인
    - f11 LIF 의 레벨·좌표·차량 유형별 속성 필드는 README 범위에서 미확인, 저장소가 VDMA 공식 계정인지 미확인
    - f12·f16·f17·f19·f21·f23·f24 원문 미열람(검색 요약 범위)
    - f23 편차 35cm·15도 수치 단일 출처
    - f25~f30 은 이전 트랙 실행 2026-09-25-05 근거의 재인용이며 이번 실행에서 원문을 다시 열지 않음
    - 트랙 반영 제안의 '축척 복원은 별도 과제'([추정] f21, 2026-09-25-05)와 엘리베이터 라벨 관련 근거는 이번에 확인하지 못해 finding 으로 내지 않음
    - IndoorGML 2.0 Part 1(22-045r5) 본문은 파일 크기 한도로 열지 못해 Part 2a 초안과 README 로만 확인
    - GitHub 원문 출처 대부분 발행일 미확인, ref-224 저자 미확인
    - 모든 finding 교차 확인 실패(f27 제외): 규격·연구마다 발행 주체 한 곳 자료만 확인, f9 두 출처는 같은 기관
- 범위 경계 위반 의심:
    - f10·f19·f21·f23·f24: SLAM·위치추정·지도 작성은 분류 원문 9장 '로봇 자체 지능·제어'의 연계 영역이므로 좌표계 규약·지도 판·신뢰도 수용 관점으로만 쓰고 f32 에 '연계 대상: '으로 경계를 표시함
    - f24: 승강기 버튼을 누르는 팔 조작은 로봇 자체 제어이므로 다층 지도 구축 사례로만 인용
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 공식 저장소 원문 11건을 열었다(재사용 ref-031 VDA 5050 명세, ref-033 MassRobotics JSON 스키마, ref-105 어댑터 config.yaml, ref-148 robot_state.json / 신규 ref-079 traffic-editor, ref-080 integration_nav-maps, ref-154 어댑터 튜토리얼, ref-155 location_2D.json, ref-156 REP 105, ref-157 IfcSpace, ref-158 IndoorGML SWG README·26-042, ref-046 LIF README). ISO·GS1·논문 7건과 재사용 평면도 출처 12건은 원문 미열람(신뢰도 상한 medium). 검색 16회/30, 신규 출처 15건/15(ref-079~ref-224, next_ref_id 기준)로 출처 상한에 도달해 국가기술표준원 로봇 승강기 탑승 KS 보도자료(10. 설비·건물 시스템 연동 쪽), Automate ISO 21423 해설, 국내 IndoorGML 개념 논문(KCI), LT-mapper 는 넣지 못했다. 재사용 16건. 교차 확인은 f27 1건뿐. 주의: 이전 트랙 실행 2026-09-25-11 이 traffic-editor 등을 ref-079~ref-095 로 제안했으나 참고문헌 목록의 해당 id 는 다른 출처(ref-087 SayCan 등)라 이번에 새 id 로 부여했다 — 퍼블리셔가 URL 중복을 확인해야 한다. 트랙 반영 제안 4건(2026-09-25-05, 6·7·8·11절)은 재인용 finding(f25~f30)과 페이지 제안으로 다루었다. 한국 자료: KCI 다층 지도 구축 논문(ref-165), AI Hub 건축 도면 데이터(ref-074 재사용). 교차 규칙: 도면 해석 AI finding(f25~f30)은 27. AI·학습·적응과 모델 운영과 6. 지도·공간·위치 모델 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성은 현재 위치 보고 연결로만, 22. 시뮬레이션·예측용 디지털 트윈은 시뮬레이션 월드 생성 연결로만 제안해 섞지 않았다.
```
