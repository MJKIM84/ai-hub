(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-03
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 14. 도면·BIM에서 지도 만들기 (D. 공간·지도 모델)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1010
- 새 출처 id 구간: ref-1010 ~ ref-1039 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1010 부터 순서대로 쓰고 ref-1039 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-30-03/target.json

```json
{
  "run_id": "2026-09-30-03",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 112,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 14,
    "area_name": "14. 도면·BIM에서 지도 만들기",
    "category": "D. 공간·지도 모델",
    "category_letter": "D"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=14"
}
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기"
type: area
category: "D. 공간·지도 모델"
area_no: 14
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 14. 도면·BIM에서 지도 만들기

# 14. 도면·BIM에서 지도 만들기

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

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

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/space-and-map-model/place-semantics-and-map-management.md (요약)

```markdown
# 16. 장소 의미·지도 관리

소속 대분류: D. 공간·지도 모델 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1009건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 267개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
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

### docs/open-questions.md (요약: 대상 영역 [14] 에 걸린 2건 / 전체 195건)

```markdown
- oq-126 [열림] 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? (영역 8, 14, 55)
- oq-193 [열림] 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? (영역 67, 14, 16)
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

### runs/2026-09-30-02/research.md

```markdown
# 리서치 브리프 2026-09-30-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-02 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 67. 기타 현장 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — SiLA 2·자율 실험실·브레인리스 로봇·정상 무인 시설 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 플랜트·변전소 점검, 건설 현장, 농업, 공항, 오피스 빌딩, 데이터센터, 연구실 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 점검 데이터 수집·AI 분석, BIM 비교, 작업자 추종·유도선 주행, 클라우드 두뇌 로봇 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 이동 로봇 화학자(Nature 2020) 등 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
2. 플랜트·변전소·데이터센터의 점검·순찰 로봇은 무엇을 점검하고 어떤 설비·통신 조건에서 운영되는가? (섹션 3·5·6 겨냥)
3. 건설 현장에서 로봇은 매일 바뀌는 현장 상태를 BIM(Building Information Modeling)과 어떻게 대조하고 무엇을 기록하는가? (섹션 5·6 겨냥, 한국 자료 우선)
4. 농업 현장에서 여러 로봇을 함께 운영하는 국내 사례와 관리 방식(통합 관리 프로그램, 수확·운반 분업, 작업자 추종)은 무엇인가? (섹션 5·6·8 겨냥)
5. 공항·오피스 빌딩·연구실 같은 공공시설·업무 공간에서 로봇은 무엇을 하고 승강기·출입문·실험 장비와 어떻게 연동되는가? (섹션 5·6 겨냥)
6. 기타 현장에 적용되는 표준·프레임워크(ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF)는 무엇을 다루는가? (섹션 7 겨냥)
7. 기타 현장에서 ROP 가 직접 맡을 것과 로봇 자체 기능·설비·업무 시스템·업종별 규정에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Offshore Technology(2025-11-21)에 따르면 Equinor 는 2024-11부터 평소 사람이 상주하지 않도록 설계된 노르웨이 Northern Lights 이산화탄소 포집·저장(CCS) 시설에 ANYbotics 의 4족 로봇 ANYmal('Roberta')을 배치해 계기 판독·밸브 위치 확인·CO2 농도 감시·누출 탐지를 맡겼으며, 현장 운영자가 연구개발 부서 지원 없이 직접 임무를 만들기 시작했다. | ref-995 | 아니오 | medium | 2025-11-21 | 기타 / 작업 대상 | — |
| f2 | [추정] | Equinor 는 로봇을 폭넓게 도입하면 연간 10억 노르웨이 크로네(약 9,910만 달러)를 넘는 비용을 절감할 것으로 추산한다. | ref-995 | 아니오 | low | 2025-11-21 | 기타 / 예외·성과 | — |
| f3 | [사실] | 넷매니아즈(2023-09-30)가 정리한 한국전력공사 실증 자료에 따르면 한전은 2022-12 신중부 변전소에 5G 특화망을 구축하고 4족 로봇이 아날로그·디지털 계기와 LED·밸브·램프 상태를 촬영하고 열화상 영상을 모아 AI 서버로 스트리밍하게 했으며, 무선 IoT 센서와 무선 CCTV(추락·쓰러짐·위험지역 접근·화재·침입 감지)를 함께 운영했다. | ref-1008 | 아니오 | medium | 2023-09-30 | 기타 / 작업 대상 | — |
| f4 | [추정] | Energy Robotics(2026-05 Korial 로 사명 변경)는 하드웨어에 독립적인 로봇 운영 소프트웨어와 클라우드 기반 플릿 관리, AI 데이터 분석을 결합한 산업 점검 플랫폼을 내세우며, Boston Dynamics Spot·ExRobotics ExR-1 을 포함해 20개가 넘는 하드웨어 플랫폼을 제어하도록 소프트웨어를 맞춰 왔다고 주장한다. | ref-1003 | 아니오 | low | 2021-01-15 | 수행 자원 | 벤더 주장 |
| f5 | [사실] | 서울신문(2022-11-15)에 따르면 현대건설은 건설 현장의 안전·품질 관리에 4족 보행 로봇 스팟을 투입해 현장 사진 촬영·기록 자동화, 영상·환경 센서 실시간 모니터링, 레이저 스캐닝 3D 데이터 수집, QR 코드 기반 자재 추적, 출입 제한 구역 위험 경보를 하게 하고, 사무실에서 현장을 실시간으로 확인하게 했으며, 2023년 김포–파주 고속도로 현장에서 시범 운영할 계획이었다. | ref-999 | 아니오 | medium | 2022-11-15 | 기타 / 작업 대상 | — |
| f6 | [사실] | 인더스트리뉴스에 따르면 GS건설은 2020-07 큐픽스와 함께 스팟을 국내 건설 현장에 처음 도입해 성남 아파트 현장(지하주차장 골조·세대 내부 마감)과 서울 공연장 신축 현장에서 실증했고, 로봇에 단 LiDAR·360도 카메라·IoT 센서로 모은 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다. | ref-1000 | 아니오 | medium | 2026-09-30 | 기타 / 완료·인계 | — |
| f7 | [사실] | 이코노미스트(2023-01-11)에 따르면 네이버 제2사옥 1784 에서는 로봇이 초기 40대에서 약 100대로 늘었고, 두뇌를 클라우드에 둔 '브레인리스' 배달 로봇 루키를 네이버 클라우드와 5G 특화망 기반의 멀티 로봇 시스템 ARC(AI·Robot·Cloud)가 제어하며, 루키는 로봇 전용 엘리베이터 로보포트로 층을 오가며 커피·택배를 자리까지 배달하고 충전소로 돌아간다. | ref-997 | 아니오 | medium | 2023-01-11 | 기타 / 수행 자원 | — |
| f8 | [추정] | 네이버는 1784 사옥 로봇 배달 시간이 초기 15~17분에서 5~10분으로 줄었다고 밝혔다. | ref-997 | 아니오 | low | 2023-01-11 | 기타 / 예외·성과 | 벤더 주장 |
| f9 | [사실] | 아주경제(2023-11-08)에 따르면 네이버 데이터센터 각 세종에서는 네이버랩스가 개발한 서버 관리 로봇 '세로'와 서버실·창고를 오가며 고중량 자산을 나르는 운반 로봇 '가로'가 협력해 자산 흐름을 실시간으로 추적·관리하고, 두 로봇은 ARC 와 ARM 시스템을 통해 공간·서비스 인프라와 실시간으로 연동된다. | ref-1002 | 아니오 | medium | 2023-11-08 | 기타 / 작업 대상 | — |
| f10 | [사실] | 로봇신문(2018-07-11)에 따르면 인천국제공항공사는 2018-07-21부터 푸른기술·LG CNS 컨소시엄이 만든 안내 로봇 에어스타를 제1여객터미널 8대·제2여객터미널 6대로 운영해 출국장·면세지역·입국장 수하물 수취 지역에서 항공편·체크인 카운터 안내, 목적지 에스코트, 4개 국어 음성 안내, 기내 반입 금지 물품 회수를 하게 했다. | ref-998 | 아니오 | medium | 2018-07-11 | 기타 / 작업 대상 | — |
| f11 | [사실] | The Robot Report(2025-10-29)에 따르면 싱가포르 국가 로봇 프로그램이 2018년 ROS 기반으로 함께 출범시킨 로봇 미들웨어 프레임워크(RMF, 현 Open-RMF)는 제조사가 다른 로봇과 시스템이 함께 일하게 하는 것으로, 창이 공항 같은 대형 시설에서 이미 운영되고 있다. | ref-1004 | 아니오 | medium | 2025-10-29 | 기타 / 수행 자원 | — |
| f12 | [사실] | 같은 기사에 따르면 싱가포르는 로봇·승강기·자동문 사이 데이터 교환 표준 SS 713 과 로봇·중앙 관제 시스템 상호운용 기술 참조 TR 130 을 두고 SS 713 을 ISO 국제표준으로 올리려 하며, BCA Braddell 캠퍼스의 ELEVATE 시험장에서 로봇·승강기·건물 시스템의 상호작용을 시험한다. | ref-1004 | 아니오 | medium | 2025-10-29 | 기타 / 제약 | — |
| f13 | [사실] | Burger 외(Nature 583, 2020)는 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 움직이며 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다고 보고했다. | ref-996 | 아니오 | medium | 2020-07 | 기타 / 수행 자원 | 원문 미열람 |
| f14 | [사실] | SiLA 컨소시엄의 SiLA 2 는 실험실 장비를 'SiLA 서버'로 보고 서버의 능력을 Command(매개변수를 받는 동작)와 Property(읽거나 구독하는 데이터)를 담은 Feature 로 기술하며, 서버·Feature 자동 탐색과 gRPC(HTTP/2·Protocol Buffers) 통신을 규정하고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했으나 워크플로 오케스트레이션은 표준 범위 밖이다. | ref-1001 | 아니오 | medium | 2026-09-30 | — | — |
| f15 | [사실] | 뉴스토마토(2025-04-23)에 따르면 농촌진흥청은 자체 개발한 방제 로봇(2022)·운반 로봇(2023)·모니터링 로봇(2024)을 개인용 컴퓨터나 휴대전화 하나로 함께 관리하는 통합 관리 프로그램을 개발했으며, 이 프로그램은 로봇의 위치·속도·이동 거리와 운영 통계를 보여 주고 작업 순서를 설정하며, 모니터링 로봇 영상으로 수확 가능한 열매 수·위치·익은 정도를 알려 주고 작업·작물 정보로 방제 횟수와 수확 시기를 조절하게 한다. | ref-1007 | 아니오 | medium | 2025-04-23 | 기타 / 수행 자원 | — |
| f16 | [사실] | 농민신문(2024-03-25)에 따르면 농촌진흥청이 스마트팜에 시범 보급한 작업자 추종 운반 로봇은 3D 카메라로 작업자와 10cm~1m 간격을 유지하며 따라가고, 최대 300kg 을 싣고 한 번 충전으로 10시간 운행하며, 바닥의 바코드 유도선을 따라 재배 현장과 집하장 사이를 자율로 오간다. 2024년에는 8개 지역 10개 농가를 대상으로 시범사업을 진행했고, 로봇 속도와 유도선 내구성이 개선 과제로 꼽혔다. | ref-1006 | 아니오 | medium | 2024-03-25 | 기타 / 예외·성과 | — |
| f17 | [추정] | 헬로디디 보도에 따르면 한국기계연구원은 온실에서 작물을 수확하는 수확 로봇과 수확물을 하역장까지 자율로 나르는 이송 로봇으로 수확부터 운반까지 나눠 맡는 원예작물 수확 다수 로봇 시스템을 개발했으며, 연구진은 작물 인식률 90% 이상, 24시간 운영을 가정하면 사람의 80% 효율로 수확할 수 있다고 밝혔다. | ref-1005 | 아니오 | low | 2026-09-30 | 기타 / 수행 자원 | — |
| f18 | [사실] | ISO 18497 은 2024년 판에서 부분 자동·반자율·자율 농업기계·트랙터의 안전을 설계 원칙·용어(1부), 장애물 보호 시스템(2부), 자율 운용 구역(3부), 검증 방법·타당성 확인 원칙(4부)의 네 부분으로 나눠 다룬다. | ref-1009 | 아니오 | medium | 2024 | 기타 / 제약 | 원문 미열람 |
| f19 | [추정] | 확인한 자료를 종합하면 67. 기타 현장의 로봇 작업은 (1) 플랜트·변전소 점검·순찰(f1·f3), (2) 건설 현장 공정·품질·안전 점검(f5·f6), (3) 농업의 방제·운반·모니터링·수확(f15~f17), (4) 공항 같은 공공시설의 안내·청소(f10·f11), (5) 오피스 빌딩 사내 배달(f7), (6) 데이터센터 서버 자산 운반·관리(f9), (7) 연구실 실험 수행(f13)의 일곱 형태로 나타난다. | ref-995, ref-1008, ref-999, ref-1000, ref-1007, ref-1006, ref-1005, ref-998, ref-1004, ref-997, ref-1002, ref-996 | 아니오 | low | 2026-09-30 | 기타 / 작업 대상 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(다른 현장은 무엇이 다른가)에는 다음과 같이 답할 수 있다. 점검·순찰 현장은 사람이 상주하지 않거나 위험한 설비에서 계기값·열화상·가스 농도 같은 '정보'를 작업 대상으로 삼는다(f1·f3). 건설 현장은 공간이 날마다 바뀌어 수집 데이터를 BIM 과 대조한다(f5·f6). 농업은 비정형 지면과 계절성 때문에 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다(f15·f16). 공항은 다국어 안내·에스코트처럼 사람을 대상으로 한다(f10). 오피스·데이터센터는 전용 승강기·클라우드·5G 같은 건물 인프라에 기댄다(f7·f9). 연구실은 분석 장비 조작과 실험 계획이 한 루프로 묶인다(f13·f14). | ref-995, ref-1008, ref-999, ref-1000, ref-1007, ref-1006, ref-998, ref-997, ref-1002, ref-996, ref-1001 | 아니오 | low | 2026-09-30 | 기타 | — |
| f21 | [추정] | 확인한 자료를 종합하면 기타 현장 로봇 작업의 여섯 항목은 다음처럼 채울 수 있다. 시작 조건은 점검 일정·현장 운영자가 만든 임무, 사내 배달 주문, 여객 질의, 실험 계획 알고리즘의 다음 실험 선택이다(f1·f7·f10·f13). 작업 대상은 계기·밸브·열화상 같은 설비 정보, 공사 공간과 자재, 작물·수확물, 서버 자산, 여객, 시료다(f3·f5·f9·f10·f15). 수행 자원은 4족 점검 로봇·클라우드 제어 배달 로봇·전용 승강기·농업 로봇과 작업자·실험 장비다(f1·f7·f13·f16). 제약은 위험 구역·방폭·통신망·유도선·자율 운용 구역이다(f3·f5·f16·f18). 완료·인계는 점검 영상의 AI 서버 전송과 BIM 대조 결과, 자리까지의 배달, 집하장 하역이다(f3·f6·f7·f16). 예외·성과는 출동 감소·비용 절감 추산·배달 시간 단축 같은 주장과 속도·유도선 내구성 문제다(f2·f8·f16). | ref-995, ref-997, ref-998, ref-996, ref-1008, ref-999, ref-1002, ref-1007, ref-1006, ref-1000, ref-1009 | 아니오 | low | 2026-09-30 | 기타 | — |
| f22 | [추정] | 확인한 자료를 종합하면 67. 기타 현장에서 ROP 가 직접 맡을 범위는 다음과 같다. 점검 일정·배달 주문·운반 요청을 받아 로봇에 배정하고 작업 순서를 정하며(f1·f7·f15), 승강기·자동문 연동을 요청·확인하고(f7·f12), 점검 영상·계기값·BIM 대조 결과 같은 작업 결과를 모아 요청한 시스템에 돌려주고(f3·f6), 위험 구역·자율 운용 구역을 운행 제약으로 반영한다(f5·f18). 확인한 국내 사례(네이버 ARC, 농촌진흥청 통합 관리 프로그램)는 한 기관이 만든 로봇을 자체 계층으로 묶은 것이고, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 창이 공항의 Open-RMF(f11)와 벤더 주장(f4) 수준에서만 확인됐다. | ref-995, ref-997, ref-1007, ref-1004, ref-1008, ref-1000, ref-999, ref-1009, ref-1003 | 아니오 | low | 2026-09-30 | 기타 | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 다음은 외부에 맡길 영역으로 보인다. 로봇의 SLAM·가스·음향 감지·계단 보행·파지는 로봇 자체 지능·제어에 속한다(f1·f5·f13). 승강기·자동문·5G 특화망·실험 분석 장비(SiLA 서버)는 시설·설비 제어에 속한다(f7·f12·f14). 설비 보전·공정 관리 시스템과 BIM 저작 도구는 상위 업무 시스템에 속한다(f6). 농업기계 안전(ISO 18497)·위험 시설 요건은 업종별 조건에 속한다(f18). 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·상태 확인만 걸고 주행·계측 성능과 설비 제어는 해당 제조사·설비 주체에 맡겨야 할 것으로 보인다. | ref-995, ref-999, ref-996, ref-997, ref-1004, ref-1001, ref-1000, ref-1009 | 아니오 | low | 2026-09-30 | 기타 | — |
| f24 | [추정] | 이 영역은 다음 영역들과 이어진다. 승강기·자동문 연동은 22. 설비·건물 시스템 연동(f7·f12)과 연결된다. 이기종 로봇 관제는 20. 로봇·제조사 관제 연동(f4·f11), 표준은 21. 상호운용 표준·적합성(f12·f14·f18)과 연결된다. BIM 대조는 14. 도면·BIM에서 지도 만들기·16. 장소 의미·지도 관리(f6), 자산·자재 추적은 17. 작업 대상·자산 식별과 인계 추적(f5·f9), 점검 이상 감지는 38. 모니터링·이상 탐지·원인 분석(f1·f3)과 연결되며, 계기 판독·열화상 분석은 45. 문서·도면·장면 이해(f3)와도 이어진다. 작업 순서 설정은 26. 작업 순서·스케줄링(f15), 수확·이송 분업은 25. 작업 배정 — MRTA(f17), 작업자 추종은 31. 사람–로봇 협업(f16), 5G·클라우드 두뇌는 42. 분산 시스템·통신·컴퓨팅 구조(f3·f7), 실험 계획 루프는 46. 예측·학습 기반 최적화(f13), 농업기계 안전은 50. 안전 표준·인증·사고 조사(f18)와 연결된다. 공항 안내는 64. 상업 시설(f10), 실외 농지·건설은 66. 실외(f16·f5), 벤더 동향은 1. 기술·시장·업체 동향(f4)과 이어진다. | ref-997, ref-1004, ref-1003, ref-1001, ref-1009, ref-1000, ref-999, ref-1002, ref-995, ref-1008, ref-1007, ref-1005, ref-1006, ref-996, ref-998 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and subsea drones | 2025-11-21 | 기사 | medium | 2026-09-30 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 아니오 |
| ref-996 | Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583) | A mobile robotic chemist | 2020-07 | 논문 | medium | 2026-09-30 | https://www.nature.com/articles/s41586-020-2442-2 | 예 |
| ref-997 | 이코노미스트 (송재민) | 로봇이 로봇들을 움직이는, 네이버 1784 | 2023-01-11 | 기사 | medium | 2026-09-30 | https://economist.co.kr/article/view/ecn202301110006 | 아니오 |
| ref-998 | 로봇신문 (정원영) | 인천국제공항, 안내 로봇 '에어스타' 본격 운영 | 2018-07-11 | 기사 | medium | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=14422 | 아니오 |
| ref-999 | 서울신문 | 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리 | 2022-11-15 | 기사 | medium | 2026-09-30 | https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118 | 아니오 |
| ref-1000 | 인더스트리뉴스 | GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입 | 미확인 | 기사 | medium | 2026-09-30 | https://www.industrynews.co.kr/news/articleView.html?idxno=38911 | 아니오 |
| ref-1001 | SiLA Consortium | SiLA Standards | 미확인 | 표준 | high | 2026-09-30 | https://sila-standard.com/standards/ | 아니오 |
| ref-1002 | 아주경제 (윤선훈) | 아시아 최대 규모 데이터센터…네이버 '각 세종' | 2023-11-08 | 기사 | medium | 2026-09-30 | https://www.ajunews.com/view/20231107091520837 | 아니오 |
| ref-1003 | Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고 | Game-changer: The rationale behind the investment in Energy Robotics | 2021-01-15 | 벤더 문서 | low | 2026-09-30 | https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics | 아니오 |
| ref-1004 | The Robot Report | Singapore's National Robotics Programme reveals initiatives to advance robot adoption | 2025-10-29 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/ | 아니오 |
| ref-1005 | 헬로디디 | 스스로 수확하고 운반···'로봇농부' 나왔다 | 미확인 | 기사 | medium | 2026-09-30 | https://www.hellodd.com/news/articleView.html?idxno=99827 | 아니오 |
| ref-1006 | 농민신문 (조영창) | 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 | 2024-03-25 | 기사 | medium | 2026-09-30 | https://www.nongmin.com/article/20240322500556 | 아니오 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합 관리 기술 개발 | 2025-04-23 | 기사 | medium | 2026-09-30 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 아니오 |
| ref-1008 | 넷매니아즈 (손장우) | 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리 | 2023-09-30 | 업계 보고서 | medium | 2026-09-30 | https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management | 아니오 |
| ref-1009 | ISO | ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones | 2024 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/82687.html | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/other-sites.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1(정상 무인 시설 점검), f3(노후 변전소 점검), f20(현장별 차이) / 섹션 4: SiLA 2(f14), 브레인리스 로봇(f7), 정상 무인 시설(f1), 자율 운용 구역(f18), 자율 실험실(f13) / 섹션 5(현장 유형 모두 기타): 점검·순찰 — f1·f2(Equinor, f2 는 운영사 추산), f3(한전 변전소); 건설 — f5(현대건설), f6(GS건설 BIM 통합); 농업 — f15(농촌진흥청 통합 관리), f16(작업자 추종 운반), f17(한국기계연구원, 연구기관 발표 수치); 공공시설 — f10(인천공항 에어스타), f11(창이 공항 Open-RMF); 오피스 — f7·f8(네이버 1784, f8 벤더 주장); 데이터센터 — f9(각 세종); 연구실 — f13; 작업 형태 f19, 여섯 항목 f21(완료·인계 확인 기준 근거 부족 명시) / 섹션 6: 점검 데이터 수집·AI 분석 f1·f3, BIM 대조 f6, 작업자 추종·유도선 f16, 클라우드 두뇌·5G f7, 통합 관리 프로그램 f15, 이기종 플랫폼 f4(벤더 주장) / 섹션 7: ISO 18497 f18(원문 미열람), SiLA 2 f14, SS 713·TR 130 f12, Open-RMF f11 / 섹션 8: f13(Nature 2020) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66 / 섹션 11: open_questions_new 5건. f4·f8 은 벤더 주장 병기 필수. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f7·f12 반영, 21. 상호운용 표준·적합성 페이지에 f12·f14 반영, 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| SiLA 2 | Standardization in Lab Automation 2 (SiLA 2) | SiLA 컨소시엄이 관리하는 실험실 장비 통신 표준으로, 장비를 서버로 보고 그 능력을 Command·Property 를 담은 Feature 로 기술하며 자동 탐색과 gRPC 통신을 규정한다. |
| 브레인리스 로봇 | Brainless Robot | 인식·판단 같은 연산을 로봇 본체가 아닌 클라우드에 두고 저지연 네트워크(5G 등)로 제어받는 로봇으로, 네이버 1784 의 배달 로봇 루키가 예다. |
| 정상 무인 시설 | Not Normally Manned (NNM) Facility | 평소 사람이 상주하지 않도록 설계한 플랜트·해상 설비로, 원격 감시와 점검 로봇으로 불필요한 현장 출동을 줄이는 운영 방식을 전제로 한다. |
| 자율 실험실 | Self-driving Laboratory (Autonomous Laboratory) | 로봇이 실험을 수행하고 알고리즘이 결과를 보고 다음 실험을 고르는 과정을 사람 개입 없이 반복하는 실험실로, 이동 로봇이 일반 실험실 장비를 다루는 형태도 포함한다. |

## 열린 질문

새로 생긴 질문:

- 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? | 관련 영역: 67. 기타 현장, 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반
- 농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? | 관련 영역: 67. 기타 현장, 20. 로봇·제조사 관제 연동 | 근거: f15 | 종류: 일반
- 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? | 관련 영역: 67. 기타 현장, 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리 | 근거: f6 | 종류: 일반
- 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? | 관련 영역: 67. 기타 현장, 23. 업무 시스템 연동, 38. 모니터링·이상 탐지·원인 분석 | 근거: f3 | 종류: 일반
- SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? | 관련 영역: 67. 기타 현장, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f2 Equinor 비용 절감 추산은 운영사 추산이며 산정 근거 미확인
    - f3 한전 변전소 실증은 넷매니아즈 정리본 기준, 한전 원자료 미열람
    - f4 Korial(구 Energy Robotics)의 20개 이상 플랫폼 제어는 벤더 주장이며 독립 확인 없음
    - f6 인더스트리뉴스 기사 발행일 미확인
    - f8 네이버 배달 시간 단축은 벤더 주장이며 측정 조건 미확인
    - f11 창이 공항 Open-RMF 운영 규모(로봇 대수·제조사 수)는 미확인 — 창이 공항 매거진 페이지는 본문이 렌더링되지 않아 열지 못함
    - f12 SS 713·TR 130 표준 원문 미열람
    - f13 Nature 논문은 저장소 PDF 본문 추출 실패로 검색 결과 요약 범위만 사용(원문 미열람)
    - f15 농촌진흥청 보도자료 원문(korea.kr·rda.go.kr)은 연결 재설정으로 열지 못해 뉴스토마토 기사 기준
    - f17 한국기계연구원 성능 수치의 시험 조건과 기사 발행일 미확인
    - f18 ISO 18497-3 원문 미열람(ISO 페이지 403)
    - Ju 외(2022) 농업 다중 로봇 리뷰는 ScienceDirect·ADS 접근 실패로 넣지 않음
    - 완료·인계 확인 기준(점검 결과 승인 주체 등)은 어느 사례에서도 확인되지 않음
- 범위 경계 위반 의심:
    - f1·f5·f13: SLAM·가스 감지·계단 보행·장비 조작은 분류 원문 19장의 로봇 자체 지능·제어이므로 사례 설명으로만 쓰고 f23 에서 '연계 대상: '으로 구분함
    - f7·f12·f14: 승강기·자동문·5G 망·실험 장비는 시설·설비 제어이므로 ROP 는 요청·예약·상태 확인만 맡는 것으로 제안함
    - f18: 농업기계 안전 표준은 업종별 조건이므로 운행 제약 근거로만 제안함
    - f3·f1: 계기 판독·열화상 AI 분석을 로봇·플랫폼 어느 쪽이 맡는지는 사례마다 달라 직접 범위로 단정하지 않음
- 한계: 재실행 1회차. 반려 사유(스키마 불일치: f1·f6·f8·f15·f18 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음)에 대응함. 직전 반환값(runs/2026-09-30-02/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었다. 그래서 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었고, finding·출처 번호가 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-1003)만 근거로 한 finding 은 f4 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 회사 성능 주장 f8 도 같은 방식으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f4, f8). web_fetch_available: true · fetch_mode full. 사용량은 검색 16회/30, 신규 출처 15건/15(ref-995~ref-1009, 예약 구간 안)로, 출처 상한에 도달했다. 그래서 정책브리핑 농업로봇 기사(2025-03-10, 열었으나 통합 관리 프로그램 서술 없음), 한전KPS 정비 보조 로봇, LS일렉트릭 변압기 공장 순찰(제조 공장 사례), 역·지하철 사례, 해외 건설·농업 상용 사례는 넣지 못했다. 원문 열람은 13건이 webfetch 로 열렸고(ref-1003 은 korial.com 으로 리디렉션), 2건은 미열람(ref-996 PDF 추출 실패, ref-1009 ISO 403)이다. 교차 확인 0건, 신뢰도 high finding 없음. 분류 원문 핵심 질문(점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가)에는 작업 형태 f19, 현장별 차이 f20, 여섯 항목 f21, 직접 범위 f22, 연계 대상 f23 으로 답했다. 결론은 추정이다. 기타 현장은 점검 현장처럼 정보가 작업 대상이거나, 건설처럼 공간이 매일 바뀌거나, 농업처럼 비정형 지면·계절성이 있거나, 오피스·데이터센터처럼 건물 인프라에 기대는 점에서 다르다. 국내 사례는 대부분 한 기관이 자체 로봇을 자체 계층으로 묶은 형태다. 현장 유형은 f4·f14·f24 를 빼고 모두 기타다. 국내 자료는 이코노미스트·로봇신문·서울신문·인더스트리뉴스·아주경제·헬로디디·농민신문·뉴스토마토·넷매니아즈 아홉 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련(계기 판독·열화상 분석, 베이지안 실험 계획)은 45. 문서·도면·장면 이해·46. 예측·학습 기반 최적화와 적용 대상 38. 모니터링·이상 탐지·원인 분석에 함께 연결했다. 입력 누락은 없고 정정 요청·우선 지정 질문도 없다. 이 영역에 걸린 기존 열린 질문은 없으며 해결된 열린 질문도 없다.
```

### runs/2026-09-30-01/research.md

```markdown
# 리서치 브리프 2026-09-30-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-01 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 66. 실외 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 공공 영역 이동로봇(PMR)·개인 배송 장치(PDD)·원격 조작형 소형차·실시간 이동 측위(RTK)·침범 후 시간(PET) 용어 없음(실외이동로봇 운행안전인증·원격 조작은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 보도 배송(배민 딜리), 순찰(뉴빌리티 뉴비), 캠퍼스 배송(Starship·NAU), 접근성 사고(피츠버그), 눈 속 고립(탈린)과 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 위성 위치·센서 융합, 불확실성을 고려한 경로 계획, 날씨·사람 도움에 기대는 예외 처리 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법 운행안전인증, 도로교통법 보행자 지위, 일본 원격 조작형 소형차, 미국 주 PDD 법, ISO 4448 시리즈, Nav2 GPS 항법 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 보도 로봇–보행자 상충 관측 연구, 눈 속 로봇 연구, 강건 경로 계획 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
2. 국내에서 실외 로봇이 보도를 다니려면 어떤 법적 요건(지능형로봇법 운행안전인증, 도로교통법상 보행자 지위, 보험)을 갖춰야 하며 그 기준은 어떻게 바뀌어 왔는가? (섹션 3·7 겨냥, 한국 자료 우선)
3. 일본·미국 등 다른 나라는 보도 주행 로봇의 크기·속도·신고를 어떻게 규정하고, 관할마다 다른 규정은 운영에 어떤 제약을 주는가? (섹션 7·9 겨냥)
4. 실외 배송·순찰·캠퍼스 운영의 실제 사례(국내외)는 어떤 작업을 어디서 어떻게 하고 있으며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥, 현장 유형 실외 명시)
5. 눈·비 같은 날씨와 보행자·장애물은 실외 로봇의 운행·경로·예외 처리에 어떤 영향을 주며 이를 다루는 방법은 무엇인가? (섹션 6·8 겨냥)
6. 실외 로봇의 위치 추정(위성 위치·RTK·센서 융합)은 어떤 한계가 있고, 공공 영역 이동로봇 표준(ISO 4448 등)은 무엇을 다루는가? (섹션 6·7 겨냥)
7. 실외에서 ROP 가 직접 맡을 것(요청 수신·배정·관할별 규정과 날씨를 경로·속도 제약으로 반영·예외 인계)과 로봇 자체 주행·위치 추정·배달 앱·법적 인증에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 따른 의무인증으로, 최대 속도 15km/h·최대 질량 500kg 이하의 배송 등 자율주행(원격제어 포함) 로봇과 관제장치의 조합을 대상으로 하며, 현재 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개 항목을 심사하고 신청일로부터 30일 이내에 처리한다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f2 | [사실] | 개정 지능형로봇법과 도로교통법은 2023-11-17 시행됐으며, 질량 500kg·시속 15km 이하 실외이동로봇은 16가지 시험항목의 운행안전인증을 받아야 보도를 다닐 수 있게 됐다. | ref-991, ref-992 | 예 | high | 2023-11-16 | 실외 / 제약 | — |
| f3 | [사실] | 정책브리핑에 따르면 개정 도로교통법은 운행안전인증을 받은 실외이동로봇에 보행자 지위를 주어 보도 통행을 허용하되 신호위반·무단횡단 금지 등 보행자 의무를 지키게 하고 위반 시 운용자에게 범칙금 3만 원을 부과하며, 보도에서 운영하려는 자에게 보험 또는 공제 가입 의무를 지우고 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다. | ref-991 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f4 | [사실] | 지디넷코리아(2023-07-28)가 전한 운행안전 기준안은 질량에 따라 최고 속도를 230kg 초과 5km/h, 100kg 초과~230kg 10km/h, 100kg 이하 15km/h로 나누고, 로봇 폭은 기본 80cm·보도 폭 250cm 이상이면 최대 120cm로 하며, 보험 보장액을 사망·후유장애 1억 5천만 원, 부상 3천만 원, 재물 피해 사고당 10억 원으로 정했다. | ref-992 | 아니오 | medium | 2023-07-28 | 실외 / 제약 | — |
| f5 | [추정] | 2023년 시행 당시 16개였던 운행안전인증 시험항목이 현재 한국로봇산업진흥원 안내에는 8개 심사항목으로 적혀 있어 심사항목이 통폐합된 것으로 보이나, 개정 시점·근거 고시와 세부 기준이 완화됐는지는 이번 조사에서 원문으로 확인하지 못했다. | ref-991, ref-980 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f6 | [사실] | 일본은 2023-04-01 시행한 개정 도로교통법에서 최고 속도 6km/h 이하, 길이 120cm·폭 70cm·높이 120cm 이하의 자동배송 로봇 등을 원격 조작형 소형차(遠隔操作型小型車)로 정의해 보도·노측대를 보행자에 준하는 규칙으로 다니게 하고, 차체 표지 부착과 통행 장소를 관할하는 도도부현 공안위원회에 대한 사전 신고를 요구한다. | ref-985 | 아니오 | medium | 2023 | 실외 / 제약 | — |
| f7 | [사실] | Supply Chain Dive(2023-04-26)에 따르면 2022년 말까지 미국 최소 23개 주가 배송 로봇(개인 배송 장치, PDD) 법을 제정했으나 주마다 기준이 달라 조지아는 최대 500파운드·보도 4mph, 뉴햄프셔는 최대 80파운드·10mph를 허용하며, 이 차이는 가벼운 로봇을 쓰는 Starship 과 무거운 장치를 원한 Amazon·FedEx 가 각 주 입법에 준 영향에서 비롯됐다고 분석했다. | ref-986 | 아니오 | medium | 2023-04-26 | 실외 / 제약 | — |
| f8 | [의견] | Ottonomy CEO 는 미국 주별 배송 로봇 규정의 차이가 커서 모든 주를 같은 기준으로 맞추는 일이 악몽이 될 것이라고 평가했다. | ref-986 | 아니오 | low | 2023-04-26 | 실외 / 제약 | — |
| f9 | [사실] | DC Velocity 에 따르면 Starship Technologies 는 2026-06-08 미국 대학 캠퍼스 운영을 종료하고 캠퍼스 로봇 1,200대 이상을 유럽·미국의 식료품 배송으로 옮긴다고 발표했으며, 식료품 시장이 더 크고 로봇이 개방된 도심 환경에서 안정적으로 운행한다는 점과 2018년부터의 캠퍼스 운영 경험을 이유로 들었다. | ref-981 | 아니오 | medium | 2026-06 | 실외 / 수행 자원 | — |
| f10 | [추정] | Starship 은 핀란드에서 자사 로봇이 식료품 배송의 약 20%를 처리하고 일반 배달원보다 건당 3~4달러 싸게 배송하며 식료품 사업이 2년간 10배 성장 궤도에 있다고 주장한다. | ref-981 | 아니오 | low | 2026-06 | 실외 / 예외·성과 | 벤더 주장 |
| f11 | [추정] | 우아한형제들은 배달로봇 딜리 신규 모델이 바퀴를 키워 낮은 연석을 넘고 경사로 주행이 나아졌으며 적재량이 2L 생수 6병에서 18병으로, 배터리 용량이 약 30% 늘었고 LED 깃대로 이면도로 시인성을 높였으며, 시범 운영에서 평균 배달 시간 약 30분과 응답자 90%의 재이용 의사를 얻었다고 밝혔다. | ref-983 | 아니오 | low | 2025-06-23 | 실외 / 예외·성과 | 벤더 주장 |
| f12 | [사실] | 지디넷코리아(2025-06-23)에 따르면 배민 배달로봇 딜리 신규 모델은 2025-06-17 한국로봇산업진흥원의 실외이동로봇 운행안전인증을 받았고, 딜리는 2025년 2월부터 서울 강남구 논현동·역삼동에서 배민B마트 배달을 시범 운영했으며 신규 모델은 2025년 8월부터 현장에 투입될 예정이었다. | ref-983 | 아니오 | medium | 2025-06-23 | 실외 / 시작 조건 | — |
| f13 | [사실] | 스포츠경향(2026-09-02)에 따르면 뉴빌리티의 자율주행 로봇 뉴비는 덕수궁에서 주·야간 순찰과 화재·쓰러짐 같은 이상 상황 감지를 지원하고 서울숲·충남대학교병원·도쿄 시부야 등에서 운영되며, 5방향 카메라 영상으로 지도를 만들고 위치를 파악하는 V-SLAM 방식을 쓴다. | ref-984 | 아니오 | medium | 2026-09-02 | 실외 / 작업 대상 | — |
| f14 | [추정] | 뉴빌리티는 2026년 상반기까지 국내외 150여 개 현장에서 로봇을 운영해 누적 14만 6,721km 이상을 주행했고 2025년 한 해 4만 4,638회 서비스를 수행했으며 연간 약 1억 4,500만 건의 데이터를 만든다고 밝혔다. | ref-984 | 아니오 | low | 2026-09-02 | 실외 / 예외·성과 | 벤더 주장 |
| f15 | [사실] | Pitt News(2019-10-21)에 따르면 피츠버그 포브스 애비뉴에서 길을 건너려 대기하던 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇히는 일이 생기자 피츠버그 대학이 몇 시간 만에 시험 운행을 멈췄고, Starship 은 로봇이 원래 경사로 뒤에서 기다리도록 설계됐으며 해당 교차로의 지도 오류 때문이라며 소프트웨어를 고치고 다른 교차로를 점검했다고 밝혔다. | ref-987 | 아니오 | medium | 2019-10-21 | 실외 / 예외·성과 | — |
| f16 | [사실] | Gehrke·Phair·Russo·Smaglik(Transportation Research Interdisciplinary Perspectives 18, 2023-03)은 노던애리조나대학 캠퍼스 10개 지점의 1주일 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용을 침범 후 시간(PET) 대리 안전 지표로 분석하고, 상충 수준·지점 특성을 예측 요인으로 모형화해 공유 통로의 시설 관리 전략을 제시하려 했다. | ref-990 | 아니오 | medium | 2023-03 | 실외 / 제약 | — |
| f17 | [사실] | Dobrosovestnova·Schwaninger·Weiss(RO-MAN 2022)는 에스토니아 탈린에서 상업 운영 중인 배송로봇이 겨울에 눈에 갇혔을 때 지나가던 사람들이 자발적으로 도와 운행을 이어 가게 한 사례를 관찰·자기민속지·온라인 콘텐츠 분석으로 연구하고, 사람의 도움이 현실적 완화책이 될 수 있지만 회사가 무급 행인의 도움에 운영을 기대서는 안 된다고 지적했다. | ref-993 | 아니오 | medium | 2022 | 실외 / 예외·성과 | — |
| f18 | [사실] | Tong·Simoni(arXiv 2507.12067, 2025-07; 2026-03 개정)는 보행자·장애물·날씨·혼잡 때문에 보도 배송로봇의 이동 시간이 크게 불확실하다고 보고 강건 최적화와 시뮬레이션을 결합한 경로 계획을 스톡홀름 도심 자료로 시험해, 타원 불확실성 집합과 분포 강건 최단경로(DRSP) 방법이 평균·최악 지연에서 가장 나았고 그 이점은 폭이 넓고 느린 로봇, 궂은 날씨·혼잡 조건에서 가장 컸다고 보고했다. | ref-982 | 아니오 | medium | 2025-07-16 | 실외 / 제약 | — |
| f19 | [사실] | 연계 대상: Nav2 공식 튜토리얼은 실외 항법에 GPS 를 쓰되 일반 GPS 정확도가 좋은 조건에서 1~2m, 최대 10m이고 위치가 자주 튀며, RTK 는 약 1cm까지 줄이지만 기준국이 필요하고 도심·숲에서는 정확도가 더 떨어진다고 적으며, 바퀴 주행거리계·IMU·GPS 를 두 개의 확장 칼만 필터로 융합하고 위경도 목표점을 UTM 좌표로 바꾸며 사전 지도 없이 로봇을 따라 움직이는 전역 비용 지도(rolling costmap)를 쓰는 구성을 안내한다. | ref-988 | 아니오 | medium | 2026-09-30 | 실외 / 수행 자원 | — |
| f20 | [사실] | ISO/TC 204(지능형 교통 시스템)가 개발하는 ISO 4448 시리즈는 보도 등 공공 영역에서 보행자 곁을 다니는 공공 영역 이동로봇(PMR)을 다루며, 개요(Part 1) 외에 경로 계획 충분성(Part 6), 운행 데이터 기록기(Part 9), 안전·신뢰성(Part 16) 부분이 위원회 초안 단계로 준비되고 있다고 표준 책임자가 밝혔다. | ref-989 | 아니오 | medium | 2025-04-20 | 실외 / 제약 | — |
| f21 | [사실] | ISO/TR 4448-1:2024 는 2024-08 발행된 기술 보고서로, 연석에서 사람·화물을 싣고 내리는 로봇 도로 차량과 보호받지 않는 보행자 사이에서 배송·점검·유지보수·감시 같은 일을 하는 로봇 장치의 배치 체계를 개관한다. | ref-994 | 아니오 | medium | 2024-08 | 실외 / 제약 | 원문 미열람 |
| f22 | [추정] | 확인한 자료를 종합하면 66. 실외의 로봇 작업은 (1) 보도 배송 — 음식·장보기 물품을 매장에서 주문자 문 앞까지(f9·f12), (2) 순찰 — 궁궐·공원·역 주변·병원 부지의 주·야간 이상 감지(f13), (3) 캠퍼스 배송 — 대학 캠퍼스 음식 배달(f9·f15·f16)의 세 형태로 나타나며, 대표 업체가 2026년 캠퍼스에서 식료품·도심 배송으로 방향을 바꾼 점(f9)은 캠퍼스 모델이 실외 운영의 시험장 역할을 했음을 시사한다. | ref-981, ref-983, ref-984, ref-987, ref-990 | 아니오 | low | 2026-09-30 | 실외 / 작업 대상 | — |
| f23 | [추정] | 확인한 자료를 종합하면 실외 로봇 작업의 여섯 항목은 시작 조건이 배달 앱·장보기 주문과 순찰 일정(f12·f13), 작업 대상이 음식·식료품과 순찰 구역·이상 상황·보행자(f9·f13), 수행 자원이 배송·순찰 로봇과 관제장치·원격 제어자, 때로 도움을 주는 행인(f1·f17), 제약이 인증·보행자 의무·속도·폭·보험과 관할별 크기·속도·신고 기준, 연석 경사로·좁은 보도·눈·위치 오차(f1~f7·f15·f18·f19), 완료·인계가 주문자 문 앞 전달(f12), 예외·성과가 눈 속 고립·접근성 사고와 운행 중단·배달 시간·비용(f10·f11·f15·f17)으로 채워질 수 있으나, 완료·인계의 확인 방식은 이번 자료에서 명시적으로 확인되지 않았다. | ref-983, ref-984, ref-981, ref-980, ref-993, ref-991, ref-992, ref-985, ref-986, ref-987, ref-982, ref-988 | 아니오 | low | 2026-09-30 | 실외 | — |
| f24 | [추정] | 확인한 자료를 종합하면 날씨는 실외 로봇 운영에서 인증 요건(방수 성능, f1), 이동 시간 불확실성과 경로 선택(f18), 눈 속 고립과 사람 개입(f17)의 세 층위로 나타나므로, 운영 계층은 날씨·혼잡을 배정·경로의 제약과 예외 복구 조건으로 다뤄야 할 것으로 보인다. | ref-980, ref-982, ref-993 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f25 | [추정] | 확인한 자료를 종합하면 66. 실외에서 ROP 가 직접 맡을 범위는 배달·장보기 주문과 순찰 일정을 받아 인증받은 로봇에 배정하고(f1·f12·f13), 관할마다 다른 속도·크기·보행자 의무·신고 조건과 날씨·혼잡을 경로·속도·운행 가능 구역 제약으로 반영하며(f2·f6·f7·f18·f24), 연석 경사로 같은 접근성 민감 지점의 대기 규칙을 지도 제약으로 관리하고(f15), 눈 속 고립·위치 오차 같은 예외를 원격 제어자·현장 인력에게 넘기는 일(f17·f19)이며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. | ref-980, ref-983, ref-984, ref-991, ref-985, ref-986, ref-982, ref-987, ref-993, ref-988 | 아니오 | low | 2026-09-30 | 실외 | — |
| f26 | [추정] | 연계 대상: 분류 원문 19장 기준으로 배달 앱·식료품 주문 시스템은 상위 업무 시스템, 로봇의 위치 추정(GPS·RTK·V-SLAM)·장애물 회피·연석 주행은 로봇 자체 지능·제어, 운행안전인증·도로교통법·일본 신고제·미국 주 PDD 법·보험은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·상태 확인·제약 반영만 걸고 주행 안전 성능과 법적 인증 취득은 로봇 제조사·운영사에 맡겨야 할 것으로 보인다. | ref-983, ref-988, ref-984, ref-980, ref-991, ref-985, ref-986 | 아니오 | low | 2026-09-30 | 실외 | — |
| f27 | [추정] | 이 영역은 보도 통행 규정·인증을 다루는 59. 법·규제·보험·라이선스와 50. 안전 표준·인증·사고 조사(f1~f7·f20·f21), 보행자·자전거와의 상충을 다루는 19. 사람·보행자 모델과 49. 사람 근접 안전(f15·f16), 위경도 좌표와 운행 구역을 다루는 15. 지도·공간·위치 모델과 16. 장소 의미·지도 관리(f15·f19), 날씨·혼잡 아래 경로를 다루는 27. 다중 로봇 경로·교통 관리 — MAPF 와 26. 작업 순서·스케줄링(f18), 눈 속 고립·원격 개입을 다루는 32. 예외 복구·재계획·업무 연속성과 31. 사람–로봇 협업(f17), 순찰 이상 감지를 다루는 38. 모니터링·이상 탐지·원인 분석(f13), 접근성을 다루는 60. 노동·수용성·접근성(f15), 배달 앱 연동을 다루는 23. 업무 시스템 연동(f12), 이기종 관제를 다루는 20. 로봇·제조사 관제 연동(f1·f25), 사업 전환을 다루는 1. 기술·시장·업체 동향과 3. 경제성·조달·사업 모델(f9·f10)과 이어진다. | ref-980, ref-991, ref-985, ref-986, ref-989, ref-994, ref-987, ref-990, ref-988, ref-982, ref-993, ref-984, ref-983, ref-981 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-981 | DC Velocity | Starship steers its delivery robots off college campuses and toward grocery sector | 2026-06 | 기사 | medium | 2026-09-30 | https://www.dcvelocity.com/transportation/trucking/last-mile/starship-steers-its-delivery-robots-off-college-campuses-and-toward-grocery-sector | 아니오 |
| ref-982 | Tong, X., & Simoni, M. D. (arXiv) | Robust Route Planning for Sidewalk Delivery Robots | 2025-07-16 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.12067 | 아니오 |
| ref-983 | 지디넷코리아 | 배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득 | 2025-06-23 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20250623095742 | 아니오 |
| ref-984 | 스포츠경향 | 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 | 2026-09-02 | 기사 | medium | 2026-09-30 | https://sports.khan.co.kr/article/202609020605003/ | 아니오 |
| ref-985 | 内閣府 (일본 내각부) | 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について | 2023 | 정부·연구기관 | high | 2026-09-30 | https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html | 아니오 |
| ref-986 | Supply Chain Dive | Why delivery robots face a regulatory ‘nightmare’ | 2023-04-26 | 기사 | medium | 2026-09-30 | https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/ | 아니오 |
| ref-987 | The Pitt News | Pitt pauses testing of Starship robots due to safety concerns | 2019-10-21 | 기사 | medium | 2026-09-30 | https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/ | 아니오 |
| ref-988 | Open Navigation (Nav2) | Navigating Using GPS Localization — Nav2 documentation | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html | 아니오 |
| ref-989 | Urban Robotics Foundation (Bern Grush) | ISO-4448 Update Winter 2024 | 2024-02-04 | 업계 보고서 | medium | 2026-09-30 | https://www.urbanroboticsfoundation.org/post/iso-4448-update-winter-2024 | 아니오 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03 | 논문 | medium | 2026-09-30 | https://doi.org/10.1016/j.trip.2023.100789 | 아니오 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | 정부·연구기관 | high | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-993 | Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022) | With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow | 2022 | 논문 | medium | 2026-09-30 | https://ieeexplore.ieee.org/abstract/document/9900588/ | 아니오 |
| ref-994 | ISO | ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm | 2024-08 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/81068.html | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/outdoor.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f2·f3(2023-11 보도 통행 허용), f9(대표 업체의 캠퍼스 철수와 도심 전환), f15(접근성 사고) / 섹션 4: f3(보행자 지위), f6(원격 조작형 소형차), f7(PDD), f16(침범 후 시간), f19(RTK), f20·f21(PMR) / 섹션 5(현장 유형 모두 실외): 보도 배송 — f12(딜리), f11(벤더 주장); 순찰 — f13, f14(벤더 주장); 캠퍼스 — f9, f10(벤더 주장), f15, f16; 날씨 — f17; 작업 형태 f22, 여섯 항목 f23(완료·인계 근거 부족 명시) / 섹션 6: 위치 추정·센서 융합 f19(연계 대상 표시), 강건 경로 계획 f18, 날씨 대응 f24, 사람 도움·원격 개입 f17 / 섹션 7: 운행안전인증 f1·f2·f4·f5, 도로교통법 f3, 일본 f6, 미국 f7·f8, ISO 4448 f20·f21(원문 미열람), Nav2 f19 / 섹션 8: f16, f17, f18 / 섹션 9: f25(직접 범위), f26(연계 대상) / 섹션 10: f27 — 1, 3, 15, 16, 19, 20, 23, 26, 27, 31, 32, 38, 49, 50, 59, 60 / 섹션 11: open_questions_new 5건. f10·f11·f14 는 벤더 주장 병기 필수. 다음 실행 후보: 59. 법·규제·보험·라이선스 페이지에 f2~f7 반영, 19. 사람·보행자 모델 페이지에 f15·f16 반영, 50. 안전 표준·인증·사고 조사 페이지에 f20·f21 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 공공 영역 이동로봇 | Public-area Mobile Robot (PMR) | 보도·연석 같은 공공 공간에서 보호받지 않는 보행자 곁을 다니며 배송·점검·감시 등을 하는 로봇으로, ISO/TC 204 의 ISO 4448 시리즈가 쓰는 용어다. |
| 개인 배송 장치 | Personal Delivery Device (PDD) | 미국 여러 주 법에서 보도·횡단보도를 다니며 물건을 나르는 배송 로봇을 가리키는 법적 범주로, 무게·속도 상한이 주마다 다르다. |
| 원격 조작형 소형차 | Remote-controlled Small Vehicle (遠隔操作型小型車) | 일본 개정 도로교통법(2023-04 시행)이 정한 최고 6km/h·120×70×120cm 이하의 자동배송 로봇 등의 범주로, 보도를 보행자에 준하는 규칙으로 다니며 공안위원회에 사전 신고해야 한다. |
| 침범 후 시간 | Post-Encroachment Time (PET) | 한 이동체가 충돌 가능 지점을 떠난 뒤 다른 이동체가 그 지점에 도착하기까지의 시간 차로, 실제 충돌 없이 상충의 심각도를 재는 대리 안전 지표다. |

## 열린 질문

새로 생긴 질문:

- 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? | 관련 영역: 66. 실외, 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f5 | 종류: 일반
- 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? | 관련 영역: 66. 실외, 20. 로봇·제조사 관제 연동, 59. 법·규제·보험·라이선스 | 근거: f1 | 종류: 일반
- 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? | 관련 영역: 66. 실외, 60. 노동·수용성·접근성, 16. 장소 의미·지도 관리 | 근거: f15 | 종류: 일반
- 국내 실외 로봇 운영사는 강설·결빙·폭우 때 운행 중단·재개 기준과 고립 로봇 회수 절차를 어떻게 정하고 있으며, 그 기준이 공개된 자료가 있는가? | 관련 영역: 66. 실외, 32. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반
- 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? | 관련 영역: 66. 실외, 21. 상호운용 표준·적합성, 16. 장소 의미·지도 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f5 운행안전인증 심사항목 16→8 개정 시점·근거 고시 원문 미확인(검색 요약에만 2025-11 개정 언급)
    - f6 일본 규정은 내각부 백서 단독, 경찰청 원문 PDF 는 본문 추출 실패
    - f7 미국 주 PDD 법 개수(23개 이상)는 2023-04 기사 기준이며 이후 변화 미확인
    - f10·f11·f14 는 회사 발표 수치(벤더 주장)이며 독립 확인 없음
    - f16 NAU 연구의 상충 비율 수치는 초록에 없어 넣지 않음(ScienceDirect 403)
    - f17 탈린 연구는 초록 기준, 운영 업체명 미확인
    - f18 은 동료심사 전 프리프린트
    - f21 ISO/TR 4448-1 은 원문 미열람(ISO 페이지 403), 검색 요약 범위만 사용
    - 뉴빌리티·딜리의 관제·원격 제어 방식과 수령 확인(완료·인계) 방식 미확인
    - 국내 실외 로봇의 강설·폭우 운영 기준 자료 미확인
- 범위 경계 위반 의심:
    - f19: GPS·RTK·센서 융합은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·위치 추정)이므로 '연계 대상: '으로 표시하고 위치 오차가 운영 제약이 되는 근거로만 제안함
    - f13: V-SLAM 위치 추정 언급은 로봇 자체 지능·제어이며 순찰 사례의 설명으로만 씀
    - f26: 배달 앱, 로봇 주행·위치 추정, 인증·법령·보험은 상위 업무 시스템·로봇 자체 지능·제어·업종별 조건이므로 '연계 대상: '으로 표시함
    - f2~f7: 법령·인증 내용은 59. 법·규제·보험·라이선스와 겹치므로 이 영역에서는 실외 운영의 제약 근거로만 제안함
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f11 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 이전 반환값(runs/2026-09-30-01/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. 이번 브리프의 회사 성능·실적 주장(f10 Starship, f11 배민 딜리, f14 뉴빌리티)은 모두 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈고, 벤더 문서 유형 출처만 근거로 한 [사실] finding 은 없다(관련 finding: f10, f11, f14). 이전 실행과 finding·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-980~ref-994, 예약 구간 안)로 출처 상한에 도달해 Knightscope 등 해외 순찰 사례, 공원·골프장 등 다른 실외 작업, 한국 강설 운영 기준은 조사하지 못했다. 원문 열람: 14건 webfetch(논문 2건은 초록 페이지), 1건 미열람(ref-994 ISO 403). 열지 못해 쓰지 않은 것: 경찰청 PDF(본문 추출 실패), MDPI 피츠버그 파일럿 논문·ACM 논문·ScienceDirect(403), 한국로봇학회지 RTK 논문(PDF 손상). 교차 확인 1건(f2: 정책브리핑·지디넷코리아). 신뢰도 high finding 1건(f2). 분류 원문 핵심 질문(보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가)에는 작업 형태 f22, 여섯 항목 f23, 날씨 f24, 직접 범위 f25, 연계 대상 f26 으로 답했으며, 결론은 '보도 운영은 관할마다 다른 인증·보행자 의무·속도·크기 조건 위에서 이루어지고, 날씨·보행자·접근성 민감 지점이 경로·대기·예외 처리의 제약이 되며, 제조사가 다른 실외 로봇을 한 계층에서 묶은 공개 사례는 확인되지 않았다'는 추정이다. 현장 유형은 f27(연결)을 빼고 모두 실외이며 캠퍼스·궁궐·공원·도심 보도 사례다. 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 한국로봇산업진흥원·정책브리핑·지디넷코리아 2건·스포츠경향 다섯 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(f18 의 시뮬레이션은 경로 계획 평가용으로 26·27 쪽에만 연결). 용어집에 이미 있는 실외이동로봇 운행안전인증·원격 조작·비용 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음.
```

### runs/2026-09-25-34/research.md

```markdown
# 리서치 브리프 2026-09-25-34

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-34 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 14. 작업 순서·스케줄링 |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(주문 배치, 선후 제약, 시간창, 풋월, 가장 이른 시작 시각 등)
- 섹션 5. 현장 시나리오 비어 있음(피킹→포장 동기화, 긴급 주문 삽입)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(기존 oq-013·oq-019 가 이 영역을 관련 영역으로 둠)

## 조사 질문

1. 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [분류원문]
2. 주문 묶음(배치)과 작업대 처리 순서 결정은 어떻게 연구되었고, 로봇이 선반을 나르는 창고에서 어떤 효과가 보고되었는가? (섹션 3·6·8 겨냥)
3. 작업 선후관계와 시간 제약(시간창)은 연구·표준·도구에서 어떻게 분류·표현되는가(MRTA 시간·순서 제약 분류, ISA-95 의존 유형, 제약 프로그래밍)? (섹션 4·6·7 겨냥, oq-013 관련)
4. 피킹과 분류·포장 공정 사이 동기화를 다룬 연구와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
5. 긴급 작업 삽입과 재배정을 오픈소스 로봇 관제(Open-RMF)는 어떤 필드·기능으로 지원하고 무엇이 비어 있는가? (섹션 6·7·9 겨냥, oq-019 관련)
6. 작업 순서·스케줄링에서 ROP가 직접 맡을 것과 상위 업무 시스템·로봇 제조사에 맡길 것의 경계는 무엇인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 주문 피킹은 대부분 창고에서 가장 노동집약적이고 비용이 큰 활동으로 알려져 있으며, 그 비용은 창고 운영비의 최대 55% 로 추정되고, 배치·구역화·경로·보관 배정이 주요 설계·통제 결정 문제로 다뤄진다. | ref-682 | 아니오 | medium | 2007 | 피킹 / 예외·성과 | 원문 미열람 |
| f2 | [사실] | 이커머스 창고는 주문 줄이 적은 시간 임박 주문을 대량으로 처리해야 하며, 로봇·자동 피킹 작업대 같은 자동화와 함께 동적 주문 처리·배치·구역화·분류 시스템 같은 조직 적응이 쓰인다고 조사 논문이 정리한다. | ref-684 | 아니오 | medium | 2019 | 피킹 / 시작 조건 | 원문 미열람 |
| f3 | [사실] | 로봇이 선반(랙)을 작업대로 옮기는 부품-작업자 방식 창고에서 작업대의 주문 배치·순서와 그에 맞물린 랙 도착 순서를 함께 정하는 문제가 연구되었고, 저자 계산 실험에서 최적화된 주문 처리는 현장에서 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다. | ref-683 | 아니오 | medium | 2017 | 피킹 / 수행 자원 | 원문 미열람 |
| f4 | [사실] | 작업대가 여럿인 KIVA 방식 창고에서 주문을 작업대에 할당하고 작업대별 주문·랙 처리 순서를 함께 정하는 모델이 제안되었고, 저자 실험에서 랙 방문 수를 규칙 기반 탐욕 정책보다 3분의 1 넘게, 작업대별 독립 스케줄링보다 5분의 1 넘게 줄였다. | ref-686 | 아니오 | medium | 2021-08 | 피킹 / 예외·성과 | 원문 미열람 |
| f5 | [사실] | 배치·구역 피킹 뒤에는 고객 주문별 통합이 필요하며, 풋월(put wall) 수동 통합에서 자동창고의 빈 방출 순서를 최적화해 주문 완료 시간을 줄이고 포장 작업자의 유휴 대기를 줄이는 문제가 단일 기계 스케줄링과 가까운 문제로 정식화되었다. | ref-687 | 아니오 | medium | 2019 | 포장 / 제약 | 원문 미열람 |
| f6 | [사실] | 로봇 전방-예비(forward-reserve) 창고에서 배송 요구를 조건으로 수동 피킹과 로봇 분류 작업을 동기화하는 문제가 제안되었고, 저자 실험에서 작업 완료 시간(makespan)과 전방 구역 면적이 줄었다. | ref-688 | 아니오 | medium | 2022 | 출하 / 제약 | 원문 미열람 |
| f7 | [사실] | 국내 연구(신희철 외, 2024)는 물류센터 피킹 스케줄링을 분배·포장까지 포함한 주문 처리 전체 관점에서 다루었고, 배치 피킹이 오더 피킹보다 분배·포장 작업시간 절감에 긍정적 영향을 준다고 보고했다. | ref-689 | 아니오 | medium | 2024 | 포장 / 예외·성과 | 원문 미열람 |
| f8 | [사실] | 국내 대한산업공학회지에 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 가는 정책)을 운영하는 물류센터의 작업자 스케줄링을 다룬 연구(2025)가 있다. | ref-690 | 아니오 | medium | 2025 | 포장 / 수행 자원 | 원문 미열람 |
| f9 | [사실] | Nunes 외(2017)는 시간·순서 제약이 있는 다중 로봇 작업 배정(MRTA/TOC)의 분류를 제안했으며, 시간 제약은 작업이 실행되어야 하는 시간창으로 표현되고 이 문제군은 차량 경로 문제·잡숍 스케줄링과 관련된다. | ref-685 | 아니오 | medium | 2017 | 제약 | 원문 미열람 |
| f10 | [사실] | 선후 제약 다중 에이전트 경로 찾기(PC-MAPF)는 작업 사이에 'ti 가 끝나야 tj 가 시작한다'는 선후 제약을 두는 확장으로, 여러 로봇의 협업 픽업이나 입력 자원이 먼저 도착해야 하는 창고 조립 작업에서 생기며, PC-CBS 가 작업 완료 시간 최적 해를 찾는다고 제안된다. | ref-691 | 아니오 | medium | 2022-02 | 적치 / 제약 | 원문 미열람 |
| f11 | [추정] | 작업 간 선후 의존이 있으면 배정·시간 순서·충돌 없는 경로가 서로 강하게 얽히므로, 14. 작업 순서·스케줄링은 13. 작업 배정 — MRTA와 15. 다중 로봇 경로·교통 관리 — MAPF와 분리해 풀기 어려운 경우가 생길 것으로 보인다. | ref-691, ref-685 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f12 | [사실] | B2MML 공통 스키마의 의존 유형(Dependency1Type)은 두 요소 사이 실행 의존 제약으로 NotFollow·PossibleParallel·NotInParallel·AtStart·AfterStart·AfterEnd·NoLaterAfterStart·NoEarlierAfterStart·NoLaterAfterEnd·NoEarlierAfterEnd·Other 값을 정의하며, 일부는 의존 계수(dependency factor)로 시간 간격을 준다. | ref-117 | 아니오 | medium | 2023 | 제약 | — |
| f13 | [사실] | Open-RMF 작업 요청 스키마는 선택 필드로 작업의 가장 이른 시작 시각(unix_millis_earliest_start_time)과 플릿이 지원하는 우선순위 스키마에 맞아야 하는 우선순위(priority)를 두지만, 마감 시각이나 다른 작업과의 선후 관계 필드는 두지 않는다. | ref-125 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f14 | [사실] | Open-RMF 에서는 디스패처가 새 작업 요청을 BidNotice 로 모든 플릿 어댑터에 알리고, 처리할 수 있는 플릿이 비용을 담은 BidProposal 을 보내면 이를 비교해 낙찰 플릿에 DispatchRequest 를 보내며, 평가 방식(가장 빨리 끝내기·최소 비용 등)은 설정할 수 있고 기본값은 QuickestFinishEvaluator 이다. | ref-678, ref-680 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f15 | [사실] | Open-RMF 플릿 어댑터는 rmf_task 의 TaskPlanner 로 새 요청을 로봇 일정에 어떻게 넣을지 정하며, 배터리가 모자라면 충전 작업을 일정에 끼워 넣고, 탐욕 방식(빠르나 최적 보장 없음)과 A* 기반 방식(최적 보장, 더 오래 걸림) 중에서 고를 수 있다. | ref-678, ref-679 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f16 | [사실] | Open-RMF rmf_task 의 BinaryPriorityScheme 은 요청에 높음·낮음 두 단계 우선순위만 부여하며, 현재 구현에서 낮음 우선순위는 빈 값(nullptr)으로 반환된다. | ref-692 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f17 | [사실] | Open-RMF 작업 V2 에서 작업은 단계(phase)를 만들어 내는 객체이며, 여러 단계의 연쇄나 조합으로 구성된다. | ref-110 | 아니오 | medium | 2026-09-25 | — | — |
| f18 | [사실] | 제약 프로그래밍 해법기 OR-Tools CP-SAT 은 작업을 시작·길이·끝이 'start + size == end' 로 묶인 구간 변수로 두고, 공용 자원의 겹침 금지(NoOverlap), 실행 여부를 리터럴로 정하는 선택 구간, 시작·끝 사이 선형 부등식으로 쓰는 선후 관계로 스케줄링 문제를 표현한다. | ref-681 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f19 | [추정] | Open-RMF 작업 요청에 마감 시각 필드가 없고 기본 우선순위 체계가 높음·낮음 두 단계이므로, 출하 마감에 따라 긴급 작업을 끼워 넣고 대기 작업을 재정렬하는 규칙은 ROP 쪽에서 따로 정해야 할 것으로 보인다(oq-019 와 연결). | ref-125, ref-692 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f20 | [사실] | 자동 분류기(sorter)가 있는 창고에서 주문을 웨이브로 묶어 내릴지, 웨이브 없이 연속으로 내릴지의 출고 지시 정책을 비교한 연구가 있다. | ref-134 | 아니오 | medium | 2010 | 출하 / 시작 조건 | 원문 미열람 |
| f21 | [사실] | 주문이 동적으로 도착하는 창고 피킹에서 재최적화가 얼마나 효과적인지를 다룬 연구(Networks, 2025)가 있다. | ref-133 | 아니오 | medium | 2025 | 피킹 / 시작 조건 | 원문 미열람 |
| f22 | [사실] | 픽업·배송 작업이 온라인으로 계속 들어오는 조건에서 에이전트에 작업을 배정하고 충돌 없는 경로를 함께 계획하는 다중 에이전트 픽업·배송(MAPD) 문제가 연구되어, 작업 순서 결정이 한 번의 계획이 아니라 연속 재계획이 되는 상황을 다룬다. | ref-006 | 아니오 | medium | 2017 | 적치 / 시작 조건 | 원문 미열람 |
| f23 | [추정] | Open-RMF 의 배정은 플릿 단위 입찰과 플릿 안 일정 계획으로 이루어지고 요청 스키마에 작업 간 선후 필드가 없으므로, 제조사가 다른 플릿 사이의 선후·동기화(예: 피킹 로봇 완료 뒤 운반 로봇 출발)는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다. | ref-678, ref-125, ref-117 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f24 | [추정] | 연계 대상: 출하 마감 시각의 결정, 배송 배차·운송 계획은 상위 업무 시스템(WMS·TMS)의 영역이며, ROP 는 이를 가장 이른 시작 시각·우선순위·배송 요구 같은 작업 제약으로 받아 현장 작업 순서에 반영하는 쪽에 가까울 것으로 보인다. | ref-125, ref-688 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f25 | [추정] | 분류 원문 질문에 대해, 연구들은 피킹 작업대의 주문·랙 순서를 정할 때 뒤 공정(통합·포장)의 주문 완료 시간과 작업자 대기를 목적에 넣는 방식으로 피킹·운반·포장의 대기를 줄이려 하므로, ROP 의 순서 결정도 포장대 도착 순서를 기준 제약으로 삼는 형태가 될 것으로 보인다. | ref-687, ref-683, ref-689 | 아니오 | low | 2026-09-25 | 포장 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1705.10868 | 예 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-678 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 아니오 |
| ref-679 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-680 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 아니오 |
| ref-681 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md | 아니오 |
| ref-682 | de Koster, R., Le-Duc, T., & Roodbergen, K. J. | Design and control of warehouse order picking: A literature review | 2007 | 논문 | medium | 2026-09-25 | https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/ | 예 |
| ref-683 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 예 |
| ref-684 | Boysen, N., de Koster, R., & Weidinger, F. | Warehousing in the e-commerce era: A survey | 2019 | 논문 | medium | 2026-09-25 | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ | 예 |
| ref-685 | Nunes, E., Manner, M., Mitiche, H., & Gini, M. | A taxonomy for task allocation problems with temporal and ordering constraints | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157 | 예 |
| ref-686 | Yang, X., Hua, G., Zhang, L., Cheng, T. C. E., & Choi, T. M. | Joint order assignment and picking station scheduling in KIVA warehouses with multiple stations | 2021-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2108.09056 | 예 |
| ref-687 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2192437620300315 | 예 |
| ref-688 | Jiang, M., & Huang, G. Q. | Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery | 2022 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175 | 예 |
| ref-689 | 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지) | 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구 | 2024 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116 | 예 |
| ref-690 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 2025 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 | 예 |
| ref-691 | arXiv 2202.10449 저자(미확인) | Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks | 2022-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2202.10449 | 예 |
| ref-692 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3(왜 중요한가): f1·f2·f3·f4 — 피킹 비용 비중, 이커머스의 시간 임박 주문, 순서 최적화의 로봇 대수·랙 방문 절감. 섹션 4(핵심 개념과 용어): 주문 배치(f1·f7), 시간창·선후 제약(f9·f10), 실행 의존 유형(f12), 가장 이른 시작 시각·우선순위(f13·f16), 풋월(f5), 웨이브리스 출고(f20). 섹션 5(현장 시나리오): 피킹 작업대 순서(f3·f4, 피킹), 피킹→포장 통합(f5·f7·f8·f25, 포장), 피킹–분류–출하 동기화(f6, 출하), 긴급 주문 삽입(f19, 출하 / 시작 조건). 섹션 6(대표 접근법과 기술): 배치·순서 동시 최적화(f3·f4), 뒤 공정 기준 순서(f5·f6), 시간·순서 제약 분류(f9), 선후 제약 경로 결합(f10·f11), 입찰 기반 배정과 플릿 내 일정 계획(f14·f15), 제약 프로그래밍(f18), 온라인 재계획(f21·f22). 섹션 7(관련 표준·프레임워크·오픈소스): B2MML 의존 유형(f12), Open-RMF 요청·디스패처·TaskPlanner·우선순위·작업 단계(f13~f17), OR-Tools CP-SAT(f18). 섹션 8(대표 연구와 자료): f1~f10, f20·f21·f22. 섹션 9(ROP가 직접 맡는 것과 외부와 연계하는 것): f23(이종 플릿 사이 선후·동기화는 직접 범위), f24(연계 대상: 출하 마감·운송 계획), f19. 섹션 10(다른 연구영역과의 연결): 13. 작업 배정 — MRTA(f9·f11·f14), 15. 다중 로봇 경로·교통 관리 — MAPF(f10·f11·f22), 16. 공용 자원·충전·에너지 최적화(f15 충전 삽입), 1. 주문·업무 시스템 연계(f13·f19·f20·f24, oq-019), 2. 공정·워크플로 모델링(f12, oq-013), 3. 처리능력·거점·설비 계획(f3 로봇 대수), 18. 사람–로봇 협업·운영 인터페이스(f5·f8 작업자 대기). 섹션 11(열린 질문): 기존 oq-013·oq-019 와 이번 새 질문. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 주문 배치 | Order Batching | 여러 고객 주문을 한 번의 피킹 작업으로 묶어 이동·방문 횟수를 줄이는 창고 운영 결정이다. |
| 선후 제약 | Precedence Constraint | 한 작업이 끝나야 다른 작업을 시작할 수 있는 것처럼 두 작업의 실행 순서를 제한하는 조건이다. |
| 시간창 | Time Window | 작업이 시작되거나 실행되어야 하는 가장 이른 시각과 가장 늦은 시각 사이의 허용 구간이다. |
| 풋월 | Put Wall | 앞뒤로 열린 칸막이 선반으로, 한쪽에서 묶음 피킹한 물품을 주문별 칸에 넣고 반대쪽에서 완성된 주문을 꺼내 포장하는 주문 통합 설비이다. |

## 열린 질문

새로 생긴 질문:

- 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? | 관련 영역: 14. 작업 순서·스케줄링, 13. 작업 배정 — MRTA, 9. 로봇·제조사 관제 연동 | 근거: f23 | 종류: 일반
- 로봇 작업대의 주문·랙 순서 최적화 연구가 보고한 로봇 대수·랙 방문 절감 효과를 이종 로봇과 사람 포장대가 섞인 국내 물류센터에서 검증한 자료가 있는가? | 관련 영역: 14. 작업 순서·스케줄링, 3. 처리능력·거점·설비 계획 | 근거: f3 | 종류: 일반
- 피킹–포장 동기화의 성과를 포장 작업자 대기시간이나 주문 완료 시간 분산 같은 지표로 재는 합의된 정의가 있는가, ROP 가 순서 결정의 목적함수로 쓸 수 있는가? | 관련 영역: 14. 작업 순서·스케줄링, 4. 성과·경제성·프로세스 개선 | 근거: f5 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 논문마다 단일 출처이고, Open-RMF 자료는 같은 기관 파일이라 독립 교차가 아님
    - f3·f4·f6·f7 의 효과 수치·결과는 검색 요약 기준이며 논문 원문 미열람
    - f8 연구의 결과 수치 미확인(제목·서지만 확인)
    - f10 PC-MAPF 논문 저자 미확인
    - f16 이진 우선순위가 비용 계산에 어떻게 반영되는지와 Open-RMF 가 우선순위로 기존 배정을 재계획하는지는 소스 코드로 확인하지 않음
    - f12 의존 유형을 창고 물류 작업에 적용한 사례 미확인(oq-013 열림 유지)
    - 긴급 주문 삽입·재스케줄링을 다룬 국내 학술 자료는 한국어 검색에서 찾지 못함(벤더·블로그 자료뿐)
- 범위 경계 위반 의심:
    - f24: 출하 마감 결정·운송 계획은 분류 원문 9장 '상위 업무 시스템'·'거점 간 운송' 연계 영역이라 '연계 대상: '으로 표시함
    - f8: 작업자 스케줄링 연구는 18. 사람–로봇 협업·운영 인터페이스와 겹치므로 14번 페이지에는 포장 공정 동기화의 근거로만 쓰도록 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-110·ref-117·ref-125, 신규 ref-678·ref-679·ref-680·ref-681·ref-692. rmf-core.md(ref-004)도 열었으나 배정 관련 내용이 없어 쓰지 않았다. priority_description_Binary.json 은 404 로 열지 못했다. 나머지 신규 10건(ref-682~ref-691)과 재사용 ref-006·ref-133·ref-134 는 원문 미열람이라 신뢰도 상한 medium. 모든 finding 신뢰도 medium 이하, 교차 확인 0건. 검색 19회/30, 신규 출처 15건/15(ref-678~ref-692, 예약 구간 안), 재사용 6건. 신규 출처 예산 도달로 Ulusoy·Bilge 의 기계·AGV 동시 스케줄링 고전 연구(검증된 URL 미확보)와 주문 배치 분류 검토(EJOR 2023, 저자 미확인)는 넣지 않았다. 한국어 검색 3회에서 국내 학술 자료 2건(ref-689·ref-690)을 찾았다. 27. AI·학습·적응과 모델 운영 관련 finding 없음(강화학습 기반 배치·순서 연구가 검색에 보였으나 출처로 넣지 않음). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 기존 oq-013(의존 유형 창고 적용)·oq-019(출고 우선순위의 Open-RMF 반영)는 관련 근거(f12, f13·f16·f19)가 늘었으나 해결되지 않았다.
```
