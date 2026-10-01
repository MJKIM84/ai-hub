(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-21
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 56. 운영 이관·확대·교육 (O. 검증·도입·수명주기)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1315
- 새 출처 id 구간: ref-1315 ~ ref-1344 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1315 부터 순서대로 쓰고 ref-1344 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-21/target.json

```json
{
  "run_id": "2026-09-30-21",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 130,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 56,
    "area_name": "56. 운영 이관·확대·교육",
    "category": "O. 검증·도입·수명주기",
    "category_letter": "O"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=56"
}
```

### docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md

```markdown
---
title: "56. 운영 이관·확대·교육"
type: area
category: "O. 검증·도입·수명주기"
area_no: 56
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [O. 검증·도입·수명주기](index.md) › 56. 운영 이관·확대·교육

# 56. 운영 이관·확대·교육

!!! info "소속 대분류"
    [O. 검증·도입·수명주기](index.md) — 핵심 질문:
    만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

운영 이관·지원, 단계적 확대, 교육·변화 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 이관·지원 체계**: 구축 팀에서 운영 팀으로 넘기고 지원·장애 대응 체계를 정한다
- **단계적 확대**: 시범 운영에서 넓혀 가며 새 현장과 새 로봇을 추가한다
- **사용자 교육·변화 관리**: 운영자·작업자를 교육하고 일하는 방식의 변화를 관리한다

## 2. 핵심 질문

시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가? [분류원문]

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

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md (요약)

```markdown
# 55. 현장 조사·설치·시운전

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 조사, 설치·설정, 교정, 시운전, 인수 시험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 설치·설정**: 로봇·충전기·네트워크·설비를 설치하고 설정하며, 반복되는 설치 절차를 자동화한다
- **교정**: 센서·좌표·지도를 현장에 맞게 교정한다
- **현장 시운전**: 연동과 작업을 현장에서 시험 운전하며 문제를 잡는다
- **현장 조사**: 설치 전에 현장 치수·네트워크·설비·동선을 조사한다
- **인수 시험**: 합의한 수용 기준으로 인수 여부를 판정한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 21번 영역 ‘온보딩·설정·현장 시운전’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [옛 분류원문]

> 옛 질문: 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

새 현장에 설치하고 시운전할 때 반복 작업을 얼마나 줄일 수 있는가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1144건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 320개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
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

### docs/open-questions.md (요약: 대상 영역 [56] 에 걸린 0건 / 전체 258건)

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

### runs/2026-09-30-19/research.md

```markdown
# 리서치 브리프 2026-09-30-19

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-19 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 3. 경제성·조달·사업 모델 |
| 대분류 | A. 기획·사업 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 총소유비용(TCO)·수명주기 비용·투자 회수 기간·사용량 기반 과금·서비스형 로봇 계약 구조 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·제조 공장·병원·상업 시설의 도입 효과·과금·조달 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 투자 판단 기준, 수명주기 비용 분석, 다기준 선정, 과금 모델, 공공 실증·조달 방식 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IEC 60300-3-3, VDA 5050 목적, Open-RMF 라이선스, 국내 지원·조달 제도 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-129, oq-160, oq-162 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
2. 로봇 도입의 투자 판단에 쓰는 기준(투자수익률·회수 기간·총소유비용)과 비용 항목·분석 방법(수명주기 비용 표준 등)은 무엇인가? (섹션 4·6·7 겨냥)
3. 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델은 어떻게 구성되고, 과금 근거가 되는 사용량은 무엇으로 재는가? (섹션 4·6·9 겨냥)
4. 로봇·플랫폼 선정과 조달은 어떤 방법(다기준 의사결정, 시범 실증, 공공 조달)과 조건(개방 인터페이스, 인증 통합자)으로 이루어지는가? (섹션 5·6·7 겨냥, 한국 제도 우선)
5. 물류창고·제조 공장·병원·상업 시설 등 현장 유형별로 도입 효과와 비용을 정량 보고한 사례는 무엇이며 근거 수준은 어떤가? (섹션 3·5·8 겨냥)
6. 국내 로봇산업 통계는 관제·오케스트레이션 소프트웨어와 서비스형 로봇 매출을 따로 집계하는가, 시장 규모 자료의 산정 방법은 공개되어 있는가? (oq-162, oq-160, 섹션 8·11 겨냥)
7. 경제성·조달·사업 모델에서 ROP가 직접 맡을 것과 재무·구매·업무 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (oq-129 포함, 섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Modern Materials Handling 의 2026 사내 물류 로봇 설문(응답 166명, 2026-03~04)에서 로봇 투자 결정 요인은 투자수익률(ROI) 63%, 회수 기간 52%, 총소유비용(TCO) 47%, 공정 성과 41% 순이었다. | ref-1299 | 아니오 | medium | 2026-06-01 | 예외·성과 | — |
| f2 | [사실] | 같은 설문에서 로봇 도입 방식은 하드웨어 구매와 소프트웨어 구독을 섞은 하이브리드 53%, 전액 자본 지출 구매 37%, 서비스형 로봇(RaaS) 11%였다. | ref-1299 | 아니오 | medium | 2026-06-01 | 수행 자원 | — |
| f3 | [사실] | 같은 설문에서 로봇 투자가 사업 목표를 달성했다는 응답은 74%였고, 11%는 투자수익률·신뢰성·통합 비용 관련 목표에 못 미쳤다고 답했다. | ref-1299 | 아니오 | medium | 2026-06-01 | 예외·성과 | — |
| f4 | [사실] | NIST GCR 24-054 보고서는 로봇 도입의 가장 큰 과제로 투자수익률을 찾고 달성하는 일을 들고, 서비스형 로봇으로 초기 투자와 위험을 줄이는 방식이 매력적이라고 서술한다. | ref-1285 | 아니오 | low | 2024 | 예외·성과 | 원문 미열람 |
| f5 | [사실] | IEC 60300-3-3:2017(신뢰성 관리 — 적용 지침 — 수명주기 비용, 3판)은 수명주기 비용(LCC) 개념과 적용을 안내하며 특히 품목의 신뢰성(dependability)과 관련된 비용을 강조하는 국제 표준이다. | ref-1296 | 아니오 | medium | 2017-01-27 | — | 원문 미열람 |
| f6 | [사실] | Buerkle 외(Robotics and Computer-Integrated Manufacturing 81, 2023)는 산업용 로봇 서비스(IRaaS)를 유연성·사용성·안전·사업 모델(시간 기반·사용량 기반) 네 요소로 제안하고, 중소기업의 로봇 도입 장벽으로 큰 초기 투자, 총소유비용의 불확실성, 전문성 부족을 든다. | ref-1286 | 아니오 | medium | 2023-06 | 제조 공장 / 제약 | 원문 미열람 |
| f7 | [사실] | Lee·Aswani(2025, arXiv)는 서비스형 로봇 제공자가 작업마다 가격을 제시하고 고객이 수락·거절하며 로봇이 작업 후 확률적으로 열화하는 상황에서, 가격 결정과 로봇 교체 결정을 함께 최적화하는 마르코프 결정 과정 모델을 제시했다. | ref-1287 | 아니오 | medium | 2025-09-30 | 예외·성과 | — |
| f8 | [추정] | 물류창고 사례(벤더 주장): AutoStore 의 피킹량 기반 서비스형 로봇 모델은 알루미늄 저장 그리드를 고객이 먼저 사고, 로봇·포트(작업대)·소프트웨어는 피킹량에 따라 월 요금을 내는 구독으로 쓰게 하며, 보통 3~5년 최소 계약과 가동 로봇·포트 수에 따른 월 최소 요금을 둔다. | ref-1292 | 아니오 | low | 2026-09-30 | 물류창고 / 수행 자원 | 벤더 주장 |
| f9 | [사실] | 상업 시설 사례(한국): 지디넷코리아(2023-03)는 식당 서빙로봇 렌털 요금이 월 30만원대로 월 최저임금 수준 인건비 200만원대와 비교되며, 브이디컴퍼니(월 29만9천원 상품)·비로보틱스(3년 사용 후 소유권 결정하는 유예형)·알지티 등이 렌털 상품을 내놓았다고 보도했다. | ref-1293 | 아니오 | low | 2023-03 | 상업 시설 / 수행 자원 | — |
| f10 | [사실] | 병원 사례: Li 외(Scientific Reports 16, 2026-04)는 중국 3차 병원의 약품·검체 배송에 자율이동로봇 10대를 6개월 병행 대조로 평가해, 배송 시간이 수작업 대비 32~36% 줄고 인력 19명보다 7.3배 많은 배송을 했으며 10년 수명주기 동안 692.8만 위안 절감을 추정했다고 보고했다. | ref-1290 | 아니오 | medium | 2026-04 | 병원 / 예외·성과 | — |
| f11 | [사실] | 병원 사례(싱가포르): 창이종합병원의 CHART 는 RoMi-H(의료 로봇 미들웨어) 통합을 맡을 시스템 통합자를 연 2회 등재 프로그램으로 평가·인증하며, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있다. | ref-1289 | 아니오 | medium | 2025-05 | 병원 / 수행 자원 | — |
| f12 | [사실] | 한국로봇산업진흥원의 서비스로봇 실증사업(2020년부터)은 물류·웨어러블·의료·협동로봇·언택트 서비스 분야에 로봇 도입 비용의 50% 이내를 국비로 지원하고 민간 부담 50% 이상(수요기관 25% 이상)을 요구하며, 서류·발표·현장 평가로 과제를 뽑고 중간 점검과 최종 평가를 거친다. | ref-1288 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f13 | [사실] | 연계 대상: 조달청의 2026년 혁신제품 시범구매 기본계획은 예산을 전년 529억원에서 839억원으로 늘리고 로봇·드론·스마트팩토리 같은 AI 융복합 제품을 중점으로 하며, 조달청이 혁신제품을 사서 공공기관에 제공한 뒤 시범 사용 후 관리·활용 여부를 점검하는 방식이다. | ref-1295 | 아니오 | low | 2025-12-18 | 시작 조건 | — |
| f14 | [사실] | 로봇신문이 요약한 2024년 국내 로봇산업 실태조사(2024년 말 기준)에서 로봇산업 매출은 6조1695억원이며 제조업용 로봇 3조1075억원, 로봇부품 및 소프트웨어 1조9810억원, 전문서비스용 로봇 6423억원, 개인서비스용 로봇 4386억원으로 나뉜다. | ref-1294 | 아니오 | low | 2026-01 | — | — |
| f15 | [추정] | 같은 실태조사 요약에는 관제·오케스트레이션 소프트웨어나 서비스형 로봇(임대·구독) 매출을 따로 집계한 항목이 나타나지 않아, 국내 공식 통계만으로 관제 소프트웨어 시장 규모를 추적하기는 어려울 것으로 보인다. | ref-1294 | 아니오 | low | 2026-01 | — | — |
| f16 | [사실] | VDA 5050 3.0.0 명세는 이동로봇을 플릿 관제에 연결하는 복잡도를 줄이고 여러 제조사의 이기종 이동로봇 플릿이 같은 공간에서 조율되어 운영되게 하는 것을 목표로 든다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f17 | [사실] | Open-RMF 의 플릿 어댑터 패키지(rmf_fleet_adapter 2.14.0)는 Apache License 2.0 으로 배포된다. | ref-1297 | 아니오 | medium | 2026-09-30 | — | — |
| f18 | [추정] | 제조 공장 사례(한국, 벤더 주장 인용): 한국무역협회 보고서(2021-11)는 협동로봇 가격이 전통 산업용 로봇의 25~30% 수준이고 투자 회수 기간이 약 195일이라고 제시하나, 회수 기간 수치는 장비 제조사 자료에 기댄 것이다. | ref-1298 | 아니오 | low | 2021-11-22 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f19 | [사실] | 제조 공장 사례: Sivalingam·Subramaniam(Heliyon, 2024-02)은 디젤 연료 필터 조립 공정에 쓸 협동로봇 12종을 비용을 포함한 가중 기준으로 비교해 고르는 AHP–TOPSIS 혼합 다기준 의사결정 방법을 적용했다. | ref-1291 | 아니오 | medium | 2024-02 | 제조 공장 / 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(도입 비용을 넘는 효과가 나오며 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가)에 대해, 현장은 투자수익률·회수 기간·총소유비용을 주 판단 기준으로 쓰고 구매·하이브리드·서비스형 로봇으로 조달 방식이 나뉘며 병원·식당·창고의 효과 수치가 보고되지만 대부분 단일 사례·벤더 수치여서 같은 기준선의 독립 비교는 부족하고, 이기종 통합 비용과 잠금을 줄이려 개방 인터페이스·인증 통합자를 조달 조건으로 두는 사례가 있는 것으로 보인다. | ref-1299, ref-1285, ref-1296, ref-1292, ref-1290, ref-1293, ref-1298, ref-1289, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 3. 경제성·조달·사업 모델에서 ROP가 직접 맡을 범위는 사용량 기반 과금과 투자 효과 판단의 근거가 되는 계량 데이터(작업 완료 수·피킹 수·가동 시간 등)와 도입 전후 성과 기준선의 기록·제공, 로봇 선정 때 필요한 능력·인터페이스 적합성 정보 제공, 개방 인터페이스 준수로 로봇 교체·추가 비용을 낮추는 구조로 보인다. | ref-1292, ref-1299, ref-1286, ref-031, ref-1291 | 아니오 | low | 2026-09-30 | 완료·인계 | — |
| f22 | [추정] | 연계 대상: 분류 원문 19장 기준으로 자본 예산·회계 처리·구매 계약·요금 청구·정부 지원 신청은 재무·구매·전사 자원 계획 쪽이, 로봇 하드웨어 가격과 정비는 제조사·통합자가 맡으므로, ROP는 그들에게 사용량·성과 데이터를 넘기고 계약 조건(최소 요금·계약 기간)을 운영 제약으로 받는 쪽을 맡는 것으로 보인다. | ref-1292, ref-1288, ref-1295, ref-1296 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f23 | [추정] | 이 영역은 시장 통계의 1. 기술·시장·업체 동향(f14·f15), 수용 기준의 2. 사용 사례·요구·책임 범위(f20), 대수 산정 비용의 35. 처리능력·규모·배치 설계(oq-129), 성과 기준선의 39. 운영 성과 측정·개선(f3·f21), 개방 인터페이스의 21. 상호운용 표준·적합성과 20. 로봇·제조사 관제 연동(f16·f11·f3), 선정 기준의 5. 로봇 능력·작업 표현(f19), 계약 조건의 58. 다사업자 책임·계약·데이터(f8), 라이선스의 59. 법·규제·보험·라이선스(f17), 교체·수명주기 비용의 57. 자산·소프트웨어 수명주기 관리(f5·f7), 과금 데이터 전달의 23. 업무 시스템 연동(f22), 인력 대체 논의의 60. 노동·수용성·접근성(f9), 적용 현장인 61. 물류창고(f8)·62. 제조 공장(f6·f18·f19)·63. 병원·의료(f10·f11)·64. 상업 시설(f9)과 이어진다. | ref-1294, ref-1299, ref-031, ref-1289, ref-1291, ref-1292, ref-1297, ref-1296, ref-1287, ref-1293, ref-1290, ref-1298, ref-1286 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1285 | NIST (National Institute of Standards and Technology) | NIST Grant/Contractor Report NIST GCR 24-054 | 2024 | 정부·연구기관 | medium | 2026-09-30 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=958147 | 예 |
| ref-1286 | Buerkle, A., Eaton, W., Al-Yacoub, A., Zimmer, M., Kinnell, P., Henshaw, M., Coombes, M., Chen, W.-H., & Lohse, N. (Robotics and Computer-Integrated Manufacturing 81) | Towards industrial robots as a service (IRaaS): Flexibility, usability, safety and business models | 2023-06 | 논문 | medium | 2026-09-30 | https://www.sciencedirect.com/science/article/pii/S0736584522001661 | 예 |
| ref-1287 | Lee, J. S., & Aswani, A. (arXiv) | Profit Maximization for a Robotics-as-a-Service Model | 2025-09-30 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2509.26595 | 아니오 |
| ref-1288 | 한국로봇산업진흥원 | 서비스로봇 실증사업 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do | 아니오 |
| ref-1289 | Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05 | 정부·연구기관 | high | 2026-09-30 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 아니오 |
| ref-1290 | Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16) | Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios | 2026-04 | 논문 | medium | 2026-09-30 | https://www.nature.com/articles/s41598-026-49800-9 | 아니오 |
| ref-1291 | Sivalingam, C. S., & Subramaniam, S. K. (Heliyon) | Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process | 2024-02 | 논문 | medium | 2026-09-30 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10882119/ | 아니오 |
| ref-1292 | AutoStore | Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics? | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.autostoresystem.com/insights/buying-vs-raas-whats-the-best-strategy-for-investing-in-warehouse-robotics | 아니오 |
| ref-1293 | 지디넷코리아 (신영빈) | '30만원 vs 200만원' 인건비 부담…서빙로봇 판 커진다 | 2023-03 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20230307165036 | 아니오 |
| ref-1294 | 로봇신문 | [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약 | 2026-01 | 기사 | low | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=44544 | 아니오 |
| ref-1295 | 전자신문 | 조달청, 2026년 혁신제품 시범구매 기본계획 발표 | 2025-12-18 | 기사 | low | 2026-09-30 | https://www.etnews.com/20251218000194 | 아니오 |
| ref-1296 | IEC (International Electrotechnical Commission) | IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing | 2017-01-27 | 표준 | medium | 2026-09-30 | https://webstore.iec.ch/en/publication/31206 | 예 |
| ref-1297 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_ros2/rmf_fleet_adapter/package.xml | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/package.xml | 아니오 |
| ref-1298 | 한국무역협회 (KDI 경제정보센터 게재) | 협동로봇: 중소기업 스마트 제조의 시작점 | 2021-11-22 | 업계 보고서 | medium | 2026-09-30 | https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000159915&datecount=&issus=S&pg=&pp=20 | 아니오 |
| ref-1299 | Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사) | 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream | 2026-06-01 | 업계 보고서 | medium | 2026-09-30 | https://www.mmh.com/article/2026_intralogistics_robotics_survey_robotics_moves_into_the_mainstream | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-business/economics-procurement-and-business-models.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f20(핵심 질문 답, 추정), f1·f3(ROI·회수 기간·TCO 가 판단 기준이고 11% 는 통합 비용 등 목표 미달), f4(ROI 가 최대 과제) / 섹션 4: TCO·ROI·회수 기간 f1, 수명주기 비용 f5, 서비스형 로봇·사용량 기반 과금 f6·f8(벤더 주장 병기), 동적 가격·교체 f7 / 섹션 5: 물류창고 — f8(수행 자원, 벤더 주장), 제조 공장 — f6(제약)·f18(예외·성과, 벤더 주장)·f19(수행 자원), 병원 — f10(예외·성과)·f11(수행 자원, 싱가포르), 상업 시설 — f9(수행 자원, 한국 식당). 가정·실외·기타 사례는 찾지 못했음을 명시 / 섹션 6: 투자 판단 기준 f1·f2, 수명주기 비용 분석 f5, 다기준 선정 f19, 과금 모델 f2·f6·f7·f8·f9, 공공 실증·조달 f12·f13, 개방 인터페이스·인증 통합자 조건 f11·f16 / 섹션 7: IEC 60300-3-3 f5(원문 미열람), VDA 5050 목적 f16, Open-RMF 라이선스 f17, 서비스로봇 실증사업 f12, 조달청 혁신제품 시범구매 f13(연계 대상) / 섹션 8: f1~f3·f6·f7·f10·f19 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 1, 2, 5, 20, 21, 23, 35, 39, 57, 58, 59, 60, 61, 62, 63, 64 / 섹션 11: 기존 oq-129(미해결), oq-160(미해결), oq-162(f14·f15 로 부분 근거, 미해결 유지)와 open_questions_new 5건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10·f11, 64. 상업 시설 페이지에 f9, 62. 제조 공장 페이지에 f18·f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 총소유비용 | Total Cost of Ownership (TCO) | 장비를 사는 비용뿐 아니라 설치·통합·교육·운영·정비·폐기까지 보유 기간 전체에 드는 비용을 합한 투자 판단 지표이다. |
| 수명주기 비용 분석 | Life Cycle Costing (LCC, IEC 60300-3-3) | 품목의 획득부터 운영·정비·개선·폐기까지 수명주기 전체 비용을 산정해 대안을 비교하는 방법으로, IEC 60300-3-3 이 신뢰성 관련 비용을 중심으로 적용 지침을 준다. |
| 투자 회수 기간 | Payback Period | 도입으로 얻는 순절감·순수익의 누적액이 초기 투자액과 같아지기까지 걸리는 기간이다. |
| 피킹량 기반 과금 | Pay-per-pick | 자동화 창고 설비나 로봇의 사용료를 실제 처리한 피킹 수(물동량)에 따라 매기는 사용량 기반 과금 방식이다. |

## 열린 질문

새로 생긴 질문:

- ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 41. 플랫폼 아키텍처·외부 API | 근거: f2 | 종류: 일반
- 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가? | 관련 영역: 3. 경제성·조달·사업 모델, 58. 다사업자 책임·계약·데이터, 39. 운영 성과 측정·개선 | 근거: f8 | 종류: 일반
- 병원 배송 로봇 경제성 평가의 비용 항목·할인율·인건비 산정 방식을 비교 가능한 기준으로 정리한 연구가 있으며, 국내 병원 인건비 조건에서도 같은 결론이 나오는가? | 관련 영역: 3. 경제성·조달·사업 모델, 63. 병원·의료 | 근거: f10 | 종류: 일반
- 국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 21. 상호운용 표준·적합성 | 근거: f16 | 종류: 일반
- 이기종 로봇 통합 비용이 로봇 도입 총소유비용에서 차지하는 비중과, 공통 인터페이스·오케스트레이션 플랫폼이 그 비용을 얼마나 줄이는지 측정한 독립 연구가 있는가? | 관련 영역: 3. 경제성·조달·사업 모델, 20. 로봇·제조사 관제 연동 | 근거: f3 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 15건
- 미확인 항목:
    - f4 NIST GCR 24-054 는 PDF 본문 추출 실패로 검색 요약 범위만 사용, 제목·저자 세부 미확인
    - f6 Buerkle 외 2023 원문·초록 모두 열지 못함(403, API 초록 없음), 검색 요약 범위만 사용
    - f10 Li 외 2026 은 초록만 확인해 비용 항목·할인율·회수 기간 미확인
    - f14·f15 실태조사 보고서 원문 품목 분류표 미확인(기사 요약 기준)
    - f1~f3 설문 방법론(표본 추출·가중) 미공개
    - f8 AutoStore 그리드 비용 비중 20~40% 는 벤더 주장이며 독립 확인 실패
    - f18 협동로봇 회수 기간 195일은 제조사 자료 인용, 측정 기준 미확인
    - IRaaS 기술·시스템 요구(Mabkhot 외, Procedia CIRP 130, 2024)는 서지만 확인하고 초록을 얻지 못해 넣지 않음
    - Forrester TEI(Locus Robotics 위탁) PDF 추출 실패로 넣지 않음
    - 플릿 관리 소프트웨어 로봇당 월 요금(검색 요약의 $50~500)은 제3자 블로그뿐이고 InOrbit 공식 페이지에 가격이 없어 넣지 않음
    - 하나금융경영연구소 RaaS 보고서(국회도서관 국가전략정보포털)는 요약 내용의 사례 신뢰성이 낮아 넣지 않음
    - 싱가포르 보건부가 RoMi-H 를 공공 의료기관 통합 플랫폼으로 인정했다는 내용은 검색 요약과 CGH 소개 페이지 표현이 달라 finding 으로 내지 않음
    - 가정·실외·기타 현장의 경제성·과금 사례를 찾지 못함
    - oq-160 시장 규모 산정 방법론 공개 독립 출처를 찾지 못함
    - oq-129 채팅 기반 대수 결정과 비용 목적 설정 주체에 관한 자료를 찾지 못함
- 범위 경계 위반 의심:
    - f12·f13: 정부 지원 신청·공공 조달은 원문 19장 '상위 업무 시스템'의 재무·구매 쪽 연계 대상에 가까워 f13 은 '연계 대상: '으로 표시하고 f22 에서 ROP 직접 범위와 구분함
    - f8·f9: 로봇 하드웨어 가격·렌털 조건은 제조사·서비스 사업자의 사업 조건으로 참고 사례로만 쓰고, ROP 직접 범위는 f21 에서 계량 데이터 제공으로 한정함
    - f10: 병원 AMR 의 경로 계획 알고리즘(Dijkstra·A*·DWA)은 원문 19장 '로봇 자체 지능·제어' 쪽이라 claim 에서 빼고 경제성 결과만 씀
- 한계: web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-1285~ref-1299, 예약 구간 안)로 신규 출처 상한에 도달해 CGH RoMi-H 소개 페이지, Mabkhot 외(2024), 하나금융경영연구소 보고서를 출처로 넣지 않았다. 재사용 1건(ref-031): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-18 출처 표를 따랐고, 이번에 GitHub 공식 저장소 원문을 다시 열어 명세 목표 문장을 확인했다. 원문 열람: 16건 중 14건을 열었다(webfetch 12, github_raw 2). ref-1285(PDF 추출 실패)·ref-1286(403)은 fetched false·원문 미열람이며, ref-1296 은 유료 표준이라 공식 개요 페이지만 열어 원문 미열람으로 표시했다. ref-1290·ref-1291 은 PMC 가 캡차로 막혀 Europe PMC API 로 초록만 읽었다. 교차 확인 0건(주요 수치마다 독립 출처 2곳을 찾지 못함; NIST 보고서가 인용한 이전 MMH 설문 수치는 2026 설문과 연도가 달라 교차 확인으로 보지 않음). 벤더 주장 2건(f8·f18)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '판단 기준(ROI·회수 기간·TCO)과 조달 방식(구매·하이브리드·RaaS)은 확인되나 현장 효과 수치는 단일 사례·벤더 중심이어서 같은 기준선의 독립 비교가 부족하다'는 추정이다. 현장 유형 사례는 물류창고(f8, 벤더)·제조 공장(f6·f18·f19)·병원(f10 중국, f11 싱가포르)·상업 시설(f9, 한국 식당)이며 가정·실외·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-1288)·로봇신문(ref-1294)·전자신문(ref-1295)·지디넷코리아(ref-1293)·한국무역협회(ref-1298)다. 기존 열린 질문 oq-162 는 f14·f15 로 부분 근거(요약 기사상 관제 소프트웨어 별도 집계 항목 없음)만 있어 해결 제안하지 않았고, oq-129·oq-160 은 새 근거가 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다(f7 의 데이터 기반 가격 결정은 운영 연구 모델로 보고 L 영역 연결을 제안하지 않음). 용어집에 이미 있는 서비스형 로봇·서비스 수준 협약·핀옵스·기술 성숙도·차량 소요대수 산정·등재 프로그램·의료 로봇 미들웨어 RoMi-H 는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-18/research.md

```markdown
# 리서치 브리프 2026-09-30-18

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-18 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 40. 운영 절차·요청 창구 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 요청 창구(호출 버튼·단말·앱·API), 요청자 식별, 교대 인수인계, 역할 정의 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설·제조 공장·가정의 요청 창구와 운영 조직 사례, 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 요청 접수 스키마, 권한 모델, 구조화된 교대 인수인계, 전담 운영 조직의 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청 API, VDA 5050 범위, ANSI/A3 R15.08-3, 산업안전보건기준에 관한 규칙 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-203 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? [분류원문]
2. 현장 사용자가 로봇에게 일을 요청하는 창구(호출 버튼·터치스크린·앱·전화 경유·API)는 어떤 형태이며, 요청에 요청자·시각·우선순위 같은 무엇이 담기는가? (섹션 4·6·7 겨냥)
3. 운영자 교대 인수인계에 대해 연속 운영·고위험 분야(공정 산업·의료)의 지침과 근거는 무엇이며, 로봇 관제의 교대에 옮길 수 있는가? (섹션 4·6·8 겨냥)
4. 로봇 운영 절차·역할·교육을 요구하는 표준·법령(ANSI/A3 R15.08 시리즈, 산업안전보건기준에 관한 규칙 등)은 무엇을 요구하는가? (섹션 7 겨냥, 한국 법령 우선)
5. 병원·상업 시설·제조 공장·가정 현장에서 로봇 요청 창구와 운영 조직을 어떻게 두었고, 절차·역할이 불분명할 때 어떤 문제가 보고되었는가? (섹션 3·5 겨냥, 한국 사례 우선)
6. 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (oq-203, 섹션 6·11 겨냥)
7. 운영 절차·요청 창구에서 ROP가 직접 맡을 것과 업무 시스템·현장 조직·로봇 제조사에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 작업 요청(task_request) JSON 스키마는 작업 범주(category)와 그 범주에 맞는 설명(description)만 필수로 두고, 요청자 식별자(requester), 요청 목적 레이블(labels, 예: dashboard), 요청 시각, 가장 이른 시작 시각, 우선순위, 수행을 허용할 플릿 이름을 선택 항목으로 둔다. | ref-1255 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f2 | [사실] | Open-RMF 웹 API 서버(rmf-web api-server)는 OpenID Connect 액세스 토큰(JWT)으로 사용자를 확인하고, 역할·동작·자원의 권한 그룹 세 요소로 권한을 판정하며(관리자는 모든 그룹에 모든 동작 가능), 기록을 관계형 데이터베이스에 저장한다. | ref-1256 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 명세는 플릿 관제(마스터 컨트롤)와 로봇 사이 통신을 다루며, 현장 사용자·업무 담당자가 운반 요청을 관제에 올리는 방법은 정하지 않고 프로젝트 조정·수행 절차도 범위 밖에 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f4 | [사실] | Open-RMF 의 차선 폐쇄 요청 메시지(rmf_fleet_msgs/LaneRequest)는 플릿 이름, 열 차선 id 목록, 닫을 차선 id 목록 세 필드만 가지며 요청자·사유·유효 기간·승인 정보를 담는 필드는 없다. | ref-1257 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f5 | [추정] | 차선 폐쇄 메시지에 요청자·사유·해제 시점이 없으므로, 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지는 메시지 규격이 아니라 운영 절차와 그 위의 요청·권한 계층(예: 역할 기반 API 서버)에서 정하고 기록해야 할 것으로 보인다. | ref-1257, ref-1256 | 아니오 | low | 2026-09-30 | 제약 | — |
| f6 | [사실] | 영국 보건안전청(HSE)의 인적 요인 지침(Briefing Note No. 8, 2005)과 Brazier·Pacitti(2008)는 교대 인수인계를 대면으로, 양방향 확인 대화로, 문서화된 교대 일지로 뒷받침하고 충분한 시간을 두어 하도록 권고한다. | ref-1258, ref-1259 | 예 | medium | 2008 | 완료·인계 | — |
| f7 | [사실] | Brazier·Pacitti(2008)는 교대 인수인계가 실패하는 원인으로 핵심 운전 정보의 누락, 표준화되지 않은 비공식적 방식, 대면·양방향 대화의 부재, 불완전하거나 찾기 어려운 교대 일지를 든다. | ref-1259 | 아니오 | medium | 2008 | 예외·성과 | — |
| f8 | [사실] | 병원 인수인계 사례: Blazin 외(2020)에 따르면 구조화된 인계 프로그램 I-PASS(질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인)는 Starmer 외 연구에서 소아 병원 9곳 전공의의 의료 오류를 23%, 예방 가능한 유해 사건을 30% 줄였다. | ref-1267 | 아니오 | medium | 2020-07 | 병원 / 완료·인계 | — |
| f9 | [추정] | 공정 산업·의료의 교대 인수인계 근거(구조화된 항목, 대면·양방향 확인, 기록)는 로봇 관제 교대에도 옮길 수 있을 것으로 보이나, 여러 로봇을 운영하는 관제의 교대 인수인계 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외 등)을 정한 공개 절차나 표준은 이번 조사에서 찾지 못했다. | ref-1258, ref-1259, ref-1267 | 아니오 | low | 2026-09-30 | 완료·인계 | — |
| f10 | [사실] | 한국 산업안전보건기준에 관한 규칙 제222조는 산업용 로봇의 작동범위에서 교시 등 작업을 할 때 사업주가 로봇의 조작방법·순서, 매니퓰레이터 속도, 2명 이상 작업 시 신호방법, 이상 발견 시 조치, 이상으로 정지한 뒤 재가동할 때의 조치에 관한 지침을 정해 그에 따라 작업하게 하고, 기동스위치 등에 작업 중 표시를 하도록 요구한다. | ref-1269 | 아니오 | medium | 2025-09-01 | 제약 | — |
| f11 | [사실] | ANSI/A3 R15.08-3-2026(산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용, 2026-04-23 발행)은 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구사항을 정하며, 위험성평가와 응용·현재 운영 환경의 변경 관리, 수명주기 전반의 인원 안전을 강조한다. | ref-1265 | 아니오 | medium | 2026-04-23 | 제약 | 원문 미열람 |
| f12 | [사실] | 병원 사례: Mutlu·Forlizzi(HRI 2008)의 15개월 민족지 연구에서 자율 배송 로봇(TUG)은 내과 병동에서는 업무 중단에 대한 낮은 허용도, 인지된 비용과 이익의 불일치, 복잡한 통로에서의 주행 중단 때문에 업무 흐름에 부정적 영향을 주고 직원 저항을 낳았지만, 산후 병동에서는 업무 흐름과 사회적 맥락에 통합되었다. | ref-1263 | 아니오 | medium | 2008-03 | 병원 / 예외·성과 | — |
| f13 | [사실] | 병원 사례: 같은 연구의 TUG 운용에서는 직원이 터치스크린 단말에서 배송을 시작하고, 지정된 직원이 물품을 싣고 내리며, 로봇이 도움을 요청하면 직원이 알림에 응답하는 방식이었다. | ref-1263 | 아니오 | low | 2008-03 | 병원 / 시작 조건 | — |
| f14 | [사실] | 병원 사례(한국): 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했으며, 커맨드센터는 사용 시나리오 개발, 업무 프로세스 조율, 실시간 모니터링과 문제 대응을 맡는다. | ref-1261, ref-1262 | 예 | low | 2024-09-19 | 병원 / 수행 자원 | — |
| f15 | [사실] | 병원 사례(한국): 로봇신문 보도에 따르면 한림대학교성심병원에서는 의료진·환자가 안내 데스크나 각 부서에 요청하면 담당자가 로봇으로 서비스를 제공하며, 지디넷코리아 보도에 따르면 2022-08~2024-05 누적 사용은 35,492건이다. | ref-1262, ref-1261 | 아니오 | low | 2024-09-19 | 병원 / 시작 조건 | — |
| f16 | [사실] | 상업 시설 사례: 2017년 뉴욕 알로프트 호텔의 배송 로봇(Savioke Relay) 운용에서는 투숙객이 프런트에 전화로 요청하면 직원이 주문 내용과 객실 번호를 시스템에 입력했고(주문 접수는 자동화되지 않음), 로봇이 승강기와 연동해 이동한 뒤 객실 앞 도착 시 객실 전화로 자동 알림을 보냈다. | ref-1264 | 아니오 | low | 2017-04-18 | 상업 시설 / 시작 조건 | — |
| f17 | [사실] | 상업 시설 사례: Fu·Zheng·Wong(International Journal of Hospitality Management 2022)이 중국 고급 호텔 직원 19명을 면담한 결과, 로봇이 기술·시설·서비스 부서 가운데 어디에 속하는지가 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육, 동료 교육, 고장 처리·고객 안내 같은 추가 업무가 직원의 로봇 사용 저항으로 이어졌다. | ref-1260 | 아니오 | medium | 2022 | 상업 시설 / 수행 자원 | — |
| f18 | [사실] | 병원 사례: Proof News(2026-06) 보도에 따르면 미국 MultiCare 계열 두 병원(Good Samaritan, Tacoma General)의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기에서 막혀 사람이 계속 따라다녀야 했고, 기존 기송관 설비가 있어 간호사들이 로봇의 쓸모에 의문을 제기했다. | ref-1266 | 아니오 | low | 2026-06-09 | 병원 / 예외·성과 | — |
| f19 | [추정] | OMRON 은 버튼 하나를 눌러 지정 위치로 자율이동로봇(AMR)을 부르는 입출력 장치(Mobile I/O Box)를 제품으로 제시한다. | ref-1268 | 아니오 | medium | 2026-09-30 | 시작 조건 | 벤더 주장 |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가)에 대해, 요청 창구 기술(작업 요청 API 스키마, 역할 기반 권한, 호출 버튼, 터치스크린, 프런트 경유 입력)과 사용자 측 운영 요구 표준(ANSI/A3 R15.08-3)·교시 작업 지침 법령은 있으나, 여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인하지 못했고, 사례에서는 전담 운영 조직을 두거나(한림대학교성심병원) 역할이 불분명해 저항이 생기는(호텔) 형태로 현장마다 따로 정해지는 것으로 보인다. | ref-1255, ref-1256, ref-1268, ref-1265, ref-1269, ref-1261, ref-1262, ref-1260, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 40. 운영 절차·요청 창구에서 ROP가 직접 맡을 범위는 호출 버튼·단말·앱·업무 시스템 API 등 여러 요청 창구를 하나의 요청 형식(요청자·목적·시각·우선순위)으로 받는 접수 기능, 요청자·운영자·관리자 역할과 권한 정의, 요청 상태 알림, 임시 통제 구역 선언·해제의 요청자·승인·기한 기록, 교대 인수인계용 운영 상태 요약(열린 작업·폐쇄 구역·예외)의 제공과 기록으로 보인다. | ref-1255, ref-1256, ref-1257, ref-1258, ref-1267, ref-1264 | 아니오 | low | 2026-09-30 | 시작 조건 | — |
| f22 | [추정] | 연계 대상: 분류 원문 19장 기준으로 전자의무기록·호텔 객실 관리·제조 실행 시스템 같은 업무 시스템의 요청 발생, 병원·호텔의 인력 편성과 교대 근무 제도, 로봇 교시·정비 작업 지침(사업주·제조사 책임), 승강기·공동현관 제어는 각 업무 시스템·현장 조직·제조사·설비 업체가 맡으므로, ROP는 그 요청과 상태를 받아 작업·권한·경로 제약으로 연결하는 쪽을 맡는 것으로 보인다. | ref-1269, ref-1265, ref-1264, ref-1260, ref-031 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f23 | [추정] | 이 영역은 대화로 업무를 요청하는 12. 채팅으로 업무 지시·오케스트레이션(f1), 업무 시스템 요청을 받는 23. 업무 시스템 연동(f16·f22), 요청을 작업으로 바꾸는 24. 작업·워크플로 모델링과 25. 작업 배정 — MRTA(f1), 승강기·문 연동의 22. 설비·건물 시스템 연동(f16·f18), 임시 통제 구역의 16. 장소 의미·지도 관리(f4·f5), 인수인계 상태 표시의 37. 관제 화면·실행 기록(f9), 알림·에스컬레이션의 38. 모니터링·이상 탐지·원인 분석(f13), 이상 시 재가동 절차의 32. 예외 복구·재계획·업무 연속성과 48. 안전·위험 관리(f10), 요청 권한의 51. 인증·권한·격리(f2), 현장 협업의 31. 사람–로봇 협업(f12·f13), 운영 교육·전담 조직의 56. 운영 이관·확대·교육(f14·f17), 사용자 요구 표준의 50. 안전 표준·인증·사고 조사(f11), 부서·사업자 책임의 58. 다사업자 책임·계약·데이터(f17), 수용성의 60. 노동·수용성·접근성(f12·f17·f18), 적용 현장인 63. 병원·의료(f12~f15·f18)·64. 상업 시설(f16·f17)과 이어진다. | ref-1255, ref-1256, ref-1257, ref-1263, ref-1261, ref-1262, ref-1264, ref-1260, ref-1266, ref-1269, ref-1265 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1255 | Open-RMF (open-rmf/rmf_api_msgs 저장소) | rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-1256 | Open-RMF (open-rmf/rmf-web 저장소) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-1257 | Open-RMF (open-rmf/rmf_internal_msgs 저장소) | rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-1258 | UK Health and Safety Executive (HSE) (humanfactors101.com 게재본) | Human Factors Briefing Note No. 8 — Safety-Critical Communications | 2005 | 정부·연구기관 | medium | 2026-09-30 | https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf | 아니오 |
| ref-1259 | Brazier, A., & Pacitti, B. (IChemE Hazards XX) | Improving shift handover and maximising its value to the business | 2008 | 논문 | medium | 2026-09-30 | https://www.icheme.org/media/9743/xx-paper-48.pdf | 아니오 |
| ref-1260 | Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management) | The perils of hotel technology: The robot usage resistance model | 2022 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/ | 아니오 |
| ref-1261 | 지디넷코리아 | 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인) | 2024-09-19 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240919162124 | 아니오 |
| ref-1262 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인) | 2024-04 | 기사 | low | 2026-09-30 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 아니오 |
| ref-1263 | Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008-03 | 논문 | medium | 2026-09-30 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 아니오 |
| ref-1264 | 한국일보 | “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인) | 2017-04-18 | 기사 | low | 2026-09-30 | https://www.hankookilbo.com/news/article/201704180418820469 | 아니오 |
| ref-1265 | ANSI (The ANSI Blog) | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 미확인 | 표준 | medium | 2026-09-30 | https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/ | 예 |
| ref-1266 | Proof News (Varsha Bansal) | Meet the Robot That Nurses Unplugged | 2026-06-09 | 기사 | low | 2026-09-30 | https://www.proofnews.org/moxi/ | 아니오 |
| ref-1267 | Blazin, L. J. 외 (Pediatric Quality & Safety) | Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings | 2020-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/ | 아니오 |
| ref-1268 | OMRON Industrial Automation Europe | Autonomous Mobile Robots (AMR) | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://industrial.omron.eu/en/products/autonomous-mobile-robot | 아니오 |
| ref-1269 | 고용노동부 (국가법령정보센터) | 산업안전보건기준에 관한 규칙 제222조(교시 등) | 2025-09-01 | 정부·연구기관 | high | 2026-09-30 | https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f20(핵심 질문 답, 추정), f12·f17·f18(절차·역할이 불분명할 때의 문제) / 섹션 4: 작업 요청 스키마·요청자 f1, 역할 기반 권한 f2, 교대 인수인계 f6·f7, I-PASS f8, 호출 버튼 f19(벤더 주장 병기) / 섹션 5: 병원 — f12(예외·성과)·f13(시작 조건)·f14(수행 자원, 한국)·f15(시작 조건, 한국)·f18(예외·성과), 상업 시설 — f16(시작 조건)·f17(수행 자원). 제조 공장은 f10(법령)·f19(벤더 제품)뿐이고 물류창고·가정·실외 요청 창구 사례는 찾지 못했음을 명시 / 섹션 6: 요청 접수 형식 f1, 권한 f2, 구조화된 교대 인수인계 f6~f9, 전담 운영 조직 f14, 임시 통제 구역 절차 f4·f5 / 섹션 7: Open-RMF 작업 요청 API f1·f2, 차선 폐쇄 메시지 f4, VDA 5050 범위 f3, ANSI/A3 R15.08-3 f11(원문 미열람), 산업안전보건기준에 관한 규칙 제222조 f10, HSE 지침 f6 / 섹션 8: f6·f7·f8·f12·f17 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64 / 섹션 11: 기존 oq-203(f4·f5 로 부분 근거, 미해결 유지)과 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f12·f14·f15·f18, 64. 상업 시설 페이지에 f16·f17 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 교대 인수인계 | Shift Handover | 연속 운영 현장에서 나가는 근무조가 들어오는 근무조에게 설비·작업 상태와 위험 정보를 넘기는 절차로, 대면·양방향 확인과 교대 일지 기록이 권고된다. |
| I-PASS 인계 프로그램 | I-PASS Handoff Program | 질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인 다섯 항목으로 의료진 인계를 구조화한 프로그램이다. |
| 역할 모호성 | Role Ambiguity | 로봇 같은 새 설비의 운영·정비 책임이 어느 부서·사람에게 있는지 불분명한 상태로, 추가 업무와 사용 저항의 원인으로 보고된다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 37. 관제 화면·실행 기록 | 근거: f9 | 종류: 일반
- 병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 63. 병원·의료, 64. 상업 시설 | 근거: f15 | 종류: 일반
- ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? | 관련 영역: 40. 운영 절차·요청 창구, 50. 안전 표준·인증·사고 조사, 58. 다사업자 책임·계약·데이터 | 근거: f11 | 종류: 일반
- 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육, 60. 노동·수용성·접근성 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 2
- 예산 사용량: 검색 26회 · 신규 출처 15건
- 미확인 항목:
    - oq-203 미해결: 임시 통제 구역 선언·승인·해제 절차를 공개한 병원·상업 시설 사례를 찾지 못함(f4·f5 로 부분 근거만)
    - f11 ANSI/A3 R15.08-3-2026 은 ANSI 블로그·A3 상점 모두 403 으로 원문 미열람, 검색 요약 기준
    - f8 I-PASS 원 연구(Starmer 외, NEJM 2014)는 NEJM·WUSTL 저장소 403 으로 열지 못해 2차 서술(Blazin 2020)만 근거로 씀 — 교차 확인 아님
    - f13 Mutlu·Forlizzi PDF 추출 품질이 낮아 요청·인계 세부 절차 미확인
    - f14 한림대학교성심병원 로봇 규모는 2024년 보도 기준 7종 73대이며, 2025년 보도 검색 요약에는 11종 77대로 나옴(시점 차이로 보이나 미확인, 출처로 넣지 않음)
    - HSE 공식 사이트 교대 인수인계 페이지(communications.htm)는 열었으나 신규 출처 상한으로 넣지 않음. HSG256(교대 근무 관리) PDF 는 추출 실패
    - ISO/IEC 20000-1:2018 서비스 요청 관리(8.6.3) 조항은 공식 자료를 열지 못해 넣지 않음
    - Diligent Moxi 요청 창구(키오스크·문자·음성 버튼)는 기사 검색 요약에만 있고 벤더 페이지에서 확인되지 않아 넣지 않음
    - 가정(아파트 입주민 앱 로봇 호출) 사례는 기사 본문 확인이 불충분해 넣지 않음
- 범위 경계 위반 의심:
    - f10: 산업용 로봇 교시 작업 지침은 사업주·제조사의 로봇 작업 안전 절차로 원문 19장 '로봇 자체 지능·제어'·설비 안전 쪽에 가까워, ROP 직접 범위는 f21 에서 요청·권한·인수인계 기록으로 한정하고 f22 에서 연계 대상으로 구분함
    - f16·f18: 승강기·기송관 등 설비 연동은 원문 19장 '시설·설비 제어' 연계 대상이며 요청 창구 사례의 맥락으로만 씀
    - f6·f7·f8: 공정 산업·의료의 교대 인수인계 근거는 로봇 분야 자료가 아니므로 방법 참고로만 제안하고 로봇 관제 적용은 추정(f9)으로 둠
- 한계: web_fetch_available: true · fetch_mode full. 검색 26회/30, 신규 출처 15건/15(ref-1255~ref-1269, 예약 구간 안)로 신규 출처 상한에 도달해 HSE 공식 페이지·NEJM 원 연구를 출처로 넣지 않았다. 재사용 1건(ref-031): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-17 출처 표를 따랐고(요약 문장은 이번 확인 내용으로 작성), 이번에 GitHub 공식 저장소 원문을 다시 열어 사용자 요청 접수 방식이 범위 밖임을 확인했다. 원문 열람: 16건 중 15건을 열었고(github_raw 5, webfetch 10) ref-1265 만 403 으로 못 열어 source_unopened 로 표시했다. ref-1263·ref-1258·ref-1259 는 PDF 추출이 부분적이다. 교차 확인 2건(f6: HSE·Brazier, f14: 지디넷코리아·로봇신문). 벤더 주장 1건(f19). 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '요청 창구 기술과 사용자 측 운영 요구 표준·법령은 있으나 다중 제조사 관제의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인하지 못했고 현장마다 따로 정해진다'는 추정이다. 현장 유형 사례는 병원(f12~f15·f18, 한국 포함)·상업 시설(f16·f17)이며, 제조 공장은 법령(f10)과 벤더 제품(f19)뿐이고 물류창고·가정·실외·기타의 요청 창구 사례는 근거 있는 자료를 찾지 못했다. 국내 자료는 산업안전보건기준에 관한 규칙(ref-1269)·지디넷코리아·로봇신문·한국일보다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 서비스 수준 협약·역할 기반 접근 통제·차선 폐쇄·구역 집합·감독 제어·원격 조작은 후보로 내지 않았다. 기존 열린 질문 oq-203 은 부분 근거만 있어 해결 제안하지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```


## 스키마 불일치 (재실행)

직전 반환값이 JSON 스키마(schemas/research.schema.json)와 맞지 않아 퍼블리셔가 반려했다. 아래 오류를 모두 고친, 스키마에 맞는 JSON 객체 하나만 다시 반환한다. 내용을 새로 조사하지 말고 형식만 고친다.

- finding f9: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
