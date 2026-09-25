(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-69
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 28. 표준·상호운용성·다사업자 거버넌스 (G. 안전·보안·지능·거버넌스)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 세부영역 반영 제안: 12건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- next_ref_id: ref-704
- 새 출처 id 구간: ref-704 ~ ref-733 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-704 부터 순서대로 쓰고 ref-733 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-25-69/target.json

```json
{
  "run_id": "2026-09-25-69",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 69,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 28,
    "area_name": "28. 표준·상호운용성·다사업자 거버넌스",
    "category": "G. 안전·보안·지능·거버넌스",
    "category_letter": "G"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=28"
}
```

### docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 28
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 28. 표준·상호운용성·다사업자 거버넌스

# 28. 표준·상호운용성·다사업자 거버넌스

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

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

### data/area_reflection_proposals.json (대상 영역 28. 표준·상호운용성·다사업자 거버넌스 에 대한 트랙 반영 제안 12건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-02",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "28. 표준·상호운용성·다사업자 거버넌스: 능력 기술 관련 표준의 발행 기관과 현재 판 — IEEE 1872 계열(f1·f2), VDA 5050 3.0.0 발행 2026-03(보도자료 2026-04, [사실]) 및 3.0 기능 목록(구역·경로 공유·오류 등급·절전 action — [추정], 검색 요약 기준·원문 미열람, f12), MassRobotics 1.0(f13), OPC 40010-1(판·발행일 미확인, f14), CSS 토론 문서(f15)를 반영한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-11",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "공간 정보 교환 형식 후보로 IFC(BIRS 가 BIM–ROS 교환 형식으로 사용, f13), IndoorGML(IFC 에서 자동 생성 도구 존재, f15), OSM 형식 osmAG(f7). IFC·IndoorGML 은 발행 기관 자료로 확인하지 않음.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-19",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "VDMA LIF(README 1.0.0·2023-09 대 VDA 5050 3.0.0 의 'VDMA 2024-03' 인용 충돌, 열린 질문), VDA 5050 의 LIF 경로 가져오기 규정, IFC 4.3 운송 요소 클래스와 콘센트·전기기기 유형 열거에 로봇 충전 설비 값 부재(개발 브랜치 기준) (ref-046, ref-031, ref-213, ref-214, ref-215).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-16",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "공통 참조 어휘(IEEE 1872-2015의 목적), 의미 식별자(AAS Part 3a IEC 61360, 인용 판 3.0.2·최신 3.1.1, IDTA 02047 의 일부 속성 ECLASS IRDI), 서비스 로봇 모듈 정보 모델(ISO 22166-202:2025, KS B 7321-2 — 부합화 미확인)을 반영한다(f24·f25·f27·f29·f30·f35).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-28",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "실내 공간 표준의 발행 상태를 더한다: IndoorGML 2.0 Part 1 발행·Part 2 인코딩 초안(JSON v0.5.0), ISO 19164:2024(표준 간 클래스 대응 부속서, 원문 미열람), ISO 16739-1:2024(IFC 4.3), ifcOWL(IFC4_ADD2까지, 4.3 목록 없음), BOT v0.3.2(커뮤니티 그룹 사양), IMDF 1.0.0(OGC 커뮤니티 표준). 근거 f1·f3·f5·f10·f11·f12·f15(실행 2026-09-25-28). 3D 장면 그래프(f20)는 로봇 자체 지능·제어 연계 대상이라 제외.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-35",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDTA 02047 템플릿은 제조사명·최대 적재 질량·실외 사용 적합 등 속성에 ECLASS 속성 IRDI 를, 측경사 각·기구학 유형 같은 무인운반차 고유 속성에 IDTA 자체 식별자를 쓰고, ECLASS 분류 클래스 코드는 일반 정보 요소·제품 이미지에만 나타난다(사실, ref-245·ref-392 원문 미열람). 범위 능력의 의미 식별자는 구현자가 정해야 할 것으로 보인다(추정, ref-247·ref-243·ref-245). 근거: 트랙 단계 1 실행 2026-09-25-35 f7·f9·f12.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-36",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "CAD 레이어 명명 표준 ISO 13567-1:2017(ref-427), 미국 NCS AIA 레이어 형식(V5 기준, V6 판 있음, ref-428), KS F 1542(ref-429)와 건설CALS/EC 전자도면 작성표준(한국건설기술연구원 공고, ref-430)을 따로 기재(파생 관계 미확인), 실무 IFC 모델의 IfcBuildingElementProxy 오용 점검(Noardo 외 2021, ref-432), 국토교통부 건설산업 BIM 시행지침(2022-07, ref-436).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-41",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "ECLASS Release 15.0 이 로봇 그룹 27-38-01 클래스를 재구성·속성 추가하고 전문가 그룹 'Robotic'이 2024-04-30 첫 회의를 열었으며(15.0 발행 2024-11-30, 검색 결과 기준) Release 16.0 이 2025-11-28 발행됐다는 사실(f1·f9), IEC TC 3 CDD 안내 페이지의 도메인(IEC 61987·62683·63213, 단위 62720)과 그 안에 로봇 도메인이 없다는 추정(안내 페이지 기준, 데이터베이스 미조회, f4·f5)을 반영 제안한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-47",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IEC 61360-7:2024 교차 도메인 사전(EN IEC 61360-7:2026 병기), IEC CDD 확인 도메인에 로봇 도메인이 없다는 추정(CDD 트리 미조회), IDTA 02003 제품 분류 항목의 ECLASS·IEC CDD 참조(ref-437, ref-183, ref-438)",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-44",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "VDA 5050 3.0.0 의 지도 식별·배포 동작과 구역 집합(zoneSet) 스키마 [사실][^ref-031][^ref-442], 이번에 읽은 명세 범위(6.3절)에서는 지도 파일 내용 형식이 정해지지 않은 것으로 보인다는 관찰(부재 확정 아님) [추정][^ref-031], VDMA LIF 레이아웃 교환과 판·발행일 충돌(oq-025) [사실][^ref-046][^ref-031]을 반영한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-53",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 1,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDTA 공식 저장소 README 게시 목록 이름 기준으로 로봇·스킬·충전·모바일 전용 게시 템플릿은 없고 배터리 관련은 Digital Battery Passport Part 1~7 이다 [사실][^ref-439]. ZVEI 기술 데이터 1.1 의 제품 분류 항목은 …/ProductClassificationItem/1/1 의미 식별자로 제품을 분류 체계·속성 사전의 제품 클래스와 연결한다(원문 미열람) [사실][^ref-444].",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-54",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 28,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IFC → 링크드 빌딩 데이터 RDF 변환기 IFCtoLBD(판 2.54.0, SHACL 검증 지원, f10), 적재 전 검증 언어 W3C SHACL(2017 권고안, 편집자 초안으로 확인, f11), IFC 정보 요구 명세 buildingSMART IDS(XML 기반, 판 미확인, f12).",
      "status": "제안"
    }
  ]
}
```

### docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md (요약)

```markdown
# 25. 안전·위험 관리

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [분류원문]

## 2. SCM 관점의 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
```

### docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md (요약)

```markdown
# 26. 사이버보안·접근권한·개인정보

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [분류원문]

## 2. SCM 관점의 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
```

### docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 27. AI·학습·적응과 모델 운영

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [분류원문]

## 2. SCM 관점의 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 593건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 153개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
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
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
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
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- lane-closure: 차선 폐쇄 (Lane Closure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- model-checking: 모델 검사 (Model Checking)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
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
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
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
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
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
```

### docs/open-questions.md (요약: 대상 영역 [28] 에 걸린 14건 / 전체 98건)

```markdown
- oq-004 [열림] IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? (영역 28, 5)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 9, 28)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 1, 9, 28)
- oq-025 [열림] 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? (영역 28, 6)
- oq-026 [열림] KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) (영역 28, 5)
- oq-027 [열림] ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? (영역 6, 28)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 10, 28)
- oq-044 [열림] 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? (영역 6, 28)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 16, 28)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 22, 28)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 23, 28)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 24, 9, 28)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 25, 28)
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
# area_no 는 1~28 의 세부영역 번호다. 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 7. 화물·재고·자산 식별과 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 7            # 7. 화물·재고·자산 식별과 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "팔레트 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 7            # 주 연구영역: 7. 화물·재고·자산 식별과 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 팔레트 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 7            # 7. 화물·재고·자산 식별과 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1~7). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
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

### runs/2026-09-25-68/research.md

```markdown
# 리서치 브리프 2026-09-25-68

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-68 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 27. AI·학습·적응과 모델 운영 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(LLM 에이전트·환각은 용어집에 있으나 등각 예측·AI 관리 시스템·모델 레지스트리 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 반영 제안 6건 대기)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 반영 제안 8건 대기)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(교차 규칙 적용 대상 5·6·13·19·21 연결 필요)
- 섹션 11. 열린 질문 비어 있음(oq-030 걸려 있음)

## 조사 질문

1. AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
2. AI 시스템의 위험 관리·거버넌스를 다루는 표준·법(NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, EU AI Act, 한국 인공지능 기본법)은 무엇을 요구하며 로봇 운영 AI에 어떻게 걸리는가? (섹션 3·7·9 겨냥)
3. LLM 이 만든 계획·해석을 실행 전에 접지·검증하고 불확실할 때 사람에게 묻는 방법(SayCan, LLM+P, Code as Policies, KnowNo, SafeGate)은 무엇인가? (섹션 4·6·8 겨냥, 트랙 nl-task-chatbot 반영 제안 확인)
4. 창고 다중 로봇 작업 배정에 학습 기반 방법(강화학습)은 어떻게 쓰이며 어떤 성능이 보고되는가? (섹션 6·8·10 겨냥, 교차 규칙상 13. 작업 배정 — MRTA)
5. 운영 중인 학습 모델의 변경·버전·시험·감시를 관리하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)
6. oq-030 LTAA(arXiv 2512.02810)의 LLM 배정 완료율 77% 주장과 동적 계획법 우위라는 2차 요약 중 어느 쪽이 원문 결과인가?
7. 국내 물류 현장에서 AI 예측·계획을 운영에 쓴 사례와 국내 규제 요구는 무엇인가? (섹션 3·5 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST 는 2023-01-26 AI 위험관리 프레임워크(AI RMF 1.0)를 자율 적용 프레임워크로 발표했으며, 핵심은 거버넌스(Govern)·맵(Map)·측정(Measure)·관리(Manage) 네 기능이고 거버넌스가 나머지 세 기능을 가로지른다. | ref-734 | 아니오 | medium | 2023-01-26 | — | 원문 미열람 |
| f2 | [사실] | ISO/IEC 42001:2023 은 AI 시스템을 개발·제공·사용하는 조직이 AI 관리 시스템(AIMS)을 수립·실행·유지·지속 개선하기 위한 요구사항을 정하는 관리 시스템 표준이다. | ref-735 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f3 | [사실] | ISO/IEC 23894:2023 은 ISO 31000 의 위험관리 원칙을 AI 에 맞게 적용한 지침으로, AI 를 개발·배치·사용하는 조직이 위험 평가·처리·감시·검토·기록을 AI 관련 활동에 통합하도록 안내한다. | ref-736 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f4 | [사실] | 한국의 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI 를 고영향 인공지능으로 두어 별도 책무를 부과한다. | ref-737 | 아니오 | medium | 2026-01-22 | 제약 | 원문 미열람 |
| f5 | [사실] | EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I 의 EU 조화 법령(기계류 등)이 적용되는 제품의 안전 구성요소로 쓰이며 제3자 적합성 평가를 받아야 하는 AI 시스템을 고위험 AI 로 분류한다. | ref-738 | 아니오 | medium | 2024-06-13 | 제약 | 원문 미열람 |
| f6 | [사실] | SayCan 은 LLM 이 상위 지시에 유용한 행동을 고르는 과제 접지(Say)와, 사전 학습된 기술의 가치 함수가 현재 실행 가능성을 판정하는 세계 접지(Can)를 곱해 실행 가능하고 맥락에 맞는 기술만 선택하게 한다. | ref-739 | 아니오 | medium | 2022-04 | — | 원문 미열람 |
| f7 | [사실] | LLM+P 는 자연어 문제 설명을 LLM 으로 PDDL 파일로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 구조로, 저자는 LLM 단독으로는 대부분 문제에서 실행 가능한 계획도 못 냈으나 LLM+P 는 대부분에서 최적 해를 냈다고 보고한다. | ref-740 | 아니오 | medium | 2023-04 | — | 원문 미열람 |
| f8 | [사실] | KnowNo 는 등각 예측(conformal prediction)으로 LLM 계획기의 불확실성을 보정해, 과제 완수에 통계적 보장을 두면서 후보 행동이 하나로 좁혀지지 않을 때만 사람에게 도움을 요청하게 하며, 모델 미세조정 없이 쓸 수 있다고 저자가 보고한다. | ref-741 | 아니오 | medium | 2023-07 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | Code as Policies 는 코드 생성 LLM 이 자연어 명령과 소수 예시를 받아 인식 출력 처리와 제어 기본 API 호출을 조합한 로봇 정책 코드를 쓰게 하는 방법으로, 사람이 정한 API 범위 안에서 명령을 재조합한다. | ref-742 | 아니오 | medium | 2022-09 | — | 원문 미열람 |
| f10 | [사실] | AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍(보정 100, 시험 900)에 모호성 유형, 명확화 질문과 답, 작업 계획을 필드로 두어 LLM 의 모호성 탐지·되묻기를 평가하게 한다. | ref-354 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | Wang 외(Learning to Ask)는 도구 호출 LLM 에이전트가 불완전한 지시에서 빠진 인자를 지어내는 문제를 다루고, 불명확 지시 벤치마크 NoisyToolBench 와 필요할 때 되묻는 방법(Ask-when-Needed)을 제안했다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f12 | [사실] | Lang2LTL 연구는 자연어 명령을 선형 시간 논리(LTL) 식으로 바꿔 접지하는 방법과, LTL 식 템플릿에서 나온 식에 영어 발화를 대응시킨 말뭉치를 제시했다. | ref-056 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f13 | [사실] | LoTa-Bench 는 언어 기반 작업 계획기의 성능을 시뮬레이터(AI2-THOR 기반 ALFRED, VirtualHome 기반 Watch-And-Help 확장)의 성공률로 자동 정량화하는 벤치마크다. | ref-541 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f14 | [사실] | SafeGate 는 자연어 작업 명령에서 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람 확인 요청·거부를 정하고, 승인된 작업을 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했다. | ref-575 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f15 | [사실] | RTAW 는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 정식화하고 주의(attention) 기반 정책을 PPO 로 학습해 총 이동 지연을 줄이며, 저자는 500개 작업에서 탐욕·후회 기반 기준 대비 최대 10% 개선과 로봇·작업 수에 독립적인 정책 크기를 보고한다. | ref-743 | 아니오 | medium | 2022-09 | 수행 자원 | 원문 미열람 |
| f16 | [사실] | Sculley 외(NeurIPS 2015)는 실제 ML 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성, 설정 문제, 외부 세계 변화 같은 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. | ref-744 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f17 | [사실] | Breck 외의 ML Test Score(IEEE Big Data 2017)는 데이터·모델·인프라 시험과 감시를 1급 관심사로 두는 28개 시험·감시 항목으로 ML 시스템의 운영 준비도를 점수화하는 기준표를 제시했다. | ref-745 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f18 | [사실] | 오픈소스 MLflow 의 모델 레지스트리는 등록 모델마다 버전·별칭·태그와 계보(어느 실험·실행이 만들었는지)를 관리하며, 운영 대상 버전에 별칭(예: champion)을 붙이고 별칭을 다른 버전으로 옮겨 운영 모델을 교체하게 한다. | ref-746 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [추정] | 국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. | ref-747 | 아니오 | low | 2026-09-19 | 출하 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | 분류 원문 질문과 관련해, 확인한 접근을 종합하면 AI 가 만든 계획·해석을 실행에 쓰는 기준은 (1) 실행 가능성 접지(SayCan), (2) 형식 명세·계획기 경유 검증(LLM+P, Lang2LTL), (3) 불확실할 때 사람 확인(KnowNo, Ask-when-Needed), (4) 실행 전 안전 판정(SafeGate), (5) 승인된 모델 버전·시험 기준(ML Test Score, 모델 레지스트리, ISO/IEC 42001)의 겹 구조로 정리될 수 있어 보인다. | ref-739, ref-740, ref-056, ref-741, ref-359, ref-575, ref-745, ref-746, ref-735 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f21 | [추정] | 피킹 단계에서 관리자가 '오늘 마감 주문을 B구역부터 피킹'처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. | ref-740, ref-741, ref-354 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | 원문 미열람 |
| f22 | [추정] | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려면 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고, 교체 전 시험·감시 기준을 통과시켜야 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. | ref-746, ref-745, ref-743, ref-744 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f23 | [추정] | ROP 가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리이고, 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 이를 둘러싼 운영 틀로 보인다. | ref-735, ref-734, ref-736, ref-741, ref-746 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f24 | [추정] | 연계 대상: 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(Code as Policies 의 저수준 정책 코드, SayCan 의 사전 학습 기술)과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP 는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. | ref-742, ref-739 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f25 | [추정] | 27. AI·학습·적응과 모델 운영의 방법은 교차 규칙에 따라 학습 기반 배차로 13. 작업 배정 — MRTA(RTAW), 실행 전 안전 판정과 제품 안전 구성요소 규제로 25. 안전·위험 관리(SafeGate, EU AI Act), 사람 확인 요청으로 18. 사람–로봇 협업·운영 인터페이스(KnowNo), 모델 버전·변경으로 24. 자산·소프트웨어 수명주기 관리, 평가 벤치마크로 23. 시험·형식 검증·벤치마크(LoTa-Bench)와 맞물리는 것으로 보인다. | ref-743, ref-575, ref-738, ref-741, ref-746, ref-541 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-734 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | 정부·연구기관 | medium | 2026-09-25 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 예 |
| ref-735 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/42001 | 예 |
| ref-736 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/77304.html | 예 |
| ref-737 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 예 |
| ref-738 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-739 | Ahn, M. 외 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2204.01691 | 예 |
| ref-740 | Liu, B. 외 | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2304.11477 | 예 |
| ref-741 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-742 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.07753 | 예 |
| ref-743 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.05738 | 예 |
| ref-744 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | 논문 | medium | 2026-09-25 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 예 |
| ref-745 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | 논문 | medium | 2026-09-25 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 예 |
| ref-746 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry \| MLflow AI Platform | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://mlflow.org/docs/latest/ml/model-registry/ | 예 |
| ref-747 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | 기사 | low | 2026-09-25 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 예 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/cog-model/AmbiK-dataset | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2302.11649 | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-575 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f20(분류 원문 질문, 추정), f4·f5(국내외 규제 맥락), f16 / 4절: f8(등각 예측), f2(AIMS), f18(모델 레지스트리), f6(접지) / 5절: f21(피킹·시작 조건), f22(출하·예외·성과), f19(출하, 벤더 주장 병기) / 6절: f6·f7·f9·f8·f11·f14(LLM 계획 접지·검증·되묻기·안전 판정 — 트랙 nl-task-chatbot 반영 제안 2026-09-25-04·21·30·37 확인분), f15(학습 기반 배차), f16·f17·f18(모델 운영) / 7절: f1·f2·f3·f4·f5, f18 / 8절: f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17(트랙 반영 제안 2026-09-25-04·30·62 확인분) / 9절: f23(직접), f24('연계 대상') / 10절: f25와 교차 규칙 원문(5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석) / 11절: oq-030 유지와 open_questions_new 3건. 다음 실행 후보: 도면 해석(2026-09-25-05·36·54)과 매뉴얼 추출(2026-09-25-57) 반영 제안, LLM 다중 로봇 서베이·ROSA·RAI(2026-09-25-21)는 출처 메타데이터가 입력에 없어 이번 브리프에서 재확인하지 못함 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 등각 예측 | Conformal Prediction | 보정 데이터로 예측 집합의 크기를 정해, 정답이 집합에 들어갈 확률을 사용자가 정한 수준 이상으로 통계적으로 보장하는 불확실성 정량화 방법이다. |
| AI 관리 시스템 | Artificial Intelligence Management System (AIMS) | 조직이 AI 의 책임 있는 개발·제공·사용을 위한 정책·목표·프로세스를 세우고 운영하는 관리 체계로, ISO/IEC 42001 이 요구사항을 정한다. |
| 고영향 인공지능 | High-impact AI (Korea AI Basic Act) | 한국 인공지능 기본법에서 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있어 별도 책무가 부과되는 영역의 AI 시스템이다. |
| 모델 레지스트리 | Model Registry | 학습된 모델의 버전·별칭·태그·계보를 한곳에서 관리해 어떤 버전을 운영에 쓰는지 정하고 교체·되돌림을 추적하게 하는 저장소다. |

## 열린 질문

새로 생긴 질문:

- 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반
- LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 25. 안전·위험 관리 | 근거: f5 | 종류: 일반
- KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f8 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처 또는 종합 추정)
    - oq-030 LTAA 출처 충돌 미조사: 예산 배분상 이번 실행에서 원문 결과 확인 못 함(미해결 유지)
    - f5 EU AI Act 고위험 적용 시점은 개정 논의로 요약 간 차이가 있어 넣지 않음
    - f4 인공지능 기본법 고영향 영역 목록과 개정 법률 시행일(2026-07-21 언급) 원문 미확인
    - f15 RTAW 개선 수치는 저자 보고, 원문 미열람
    - f19 한진 사례의 수치·검증 조건 미확인(기사, 벤더 주장)
    - ref-737·ref-738·ref-746·ref-354·ref-541 발행일 미확인
    - 현대자동차·마키나락스 로봇 고장 예측 사례는 검색 요약에만 있고 출처 기사를 특정하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f24: 저수준 정책·파지 학습과 수요예측은 분류 원문 9장 로봇 자체 지능·제어, 상위 업무 시스템 쪽이라 '연계 대상:'으로 표시
    - f19: 간선차량 상·하차 시점 예측은 거점 간 운송과 맞닿아 있어 입출고 시간·접안 동기화 범위로만 제안
    - f14: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f8 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 다시 작성했다(검색 12회/30). 이번 브리프의 f8 은 KnowNo 논문(ref-741) 근거이며 벤더 문서가 아니다. 벤더·기업 주장은 f19 한 건뿐이고 vendor_claim: true, 태그 추정, evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다. web_fetch_available: false · fetch_mode mirror_only: 이번 출처는 GitHub 공식 저장소 미러가 없어 모두 원문 미열람(fetched false, 신뢰도 상한 medium). 신규 출처 14건(ref-734~ref-747, 예약 구간 안), 재사용 5건(ref-354·ref-359·ref-056·ref-541·ref-575, 참고문헌 목록 요약이 입력에 없어 이전 브리프 표의 값 사용, 신뢰도는 high 금지 규칙으로 medium). 트랙 반영 제안 15건 중 LLM 접지·검증·불확실성·안전 판정·평가 벤치마크 관련(2026-09-25-04·30·37·62 일부)은 f6~f14 로 확인했고, 도면 해석(2026-09-25-05·36·54)·매뉴얼 추출(2026-09-25-57)·LLM 다중 로봇 서베이(2026-09-25-21) 제안은 출처 메타데이터가 입력에 없고 예산 배분상 재확인하지 못해 '다음 실행 후보'로 남겼다. 교차 규칙: 학습 배차는 13. 작업 배정 — MRTA 와 양쪽 연결(f15·f25). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 한국 자료: 인공지능 기본법(ref-737), 국내 물류 AI 기사(ref-747). 정정 요청 없음.
```

### runs/2026-09-25-67/research.md

```markdown
# 리서치 브리프 2026-09-25-67

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-67 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- F. 도입·검증·유지관리 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태
- E. 협업·현장 운영 페이지가 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈, E ↔ 21. 온보딩·설정·현장 시운전, E ↔ 24. 자산·소프트웨어 수명주기 관리를 '근거 없음'으로 남김(이번 실행에서도 근거 미확보)
- B. 공통 정보·환경 모델 페이지가 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리와의 연결을 '아직 다루지 않은 연결'로 둠 — 이번 실행 f11·f15 가 근거가 될 수 있음
- G. 안전·보안·지능·거버넌스 쪽 세부영역 페이지(25~28)가 seed 이거나 심화 전이라 G 연결은 F 쪽 근거에 기댐

## 조사 질문

1. 새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]
2. 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
3. 21. 온보딩·설정·현장 시운전이 등록·설정하는 정보(팩트시트, 어댑터 설정, 경로망·지도 정합)는 B. 공통 정보·환경 모델과 C. 연결·실행 기반, D. 계획·최적화의 어느 세부영역으로 넘어가는가?
4. 22. 시뮬레이션·예측용 디지털 트윈은 A. 업무·공급망 설계(처리능력·성과)와 D. 계획·최적화(배정·경로망)의 어떤 결정을 가정한 미래로 실험하며, 8. 실시간 세계 상태·데이터 일관성과 어떻게 구분되는가?
5. 23. 시험·형식 검증·벤치마크는 C. 연결·실행 기반의 인터페이스·설비 연동, D. 계획·최적화의 교착·경로 알고리즘, E. 협업·현장 운영의 장애 대응을 어떤 시험·검증으로 잇는가? (oq-055, oq-058, oq-087 관련)
6. 24. 자산·소프트웨어 수명주기 관리의 지도·펌웨어 버전과 배터리 열화 정보는 B. 공통 정보·환경 모델, C. 연결·실행 기반, D. 계획·최적화, G. 안전·보안·지능·거버넌스의 어느 규칙·제약과 맞물리는가? (oq-090, oq-091 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS) 운영의 여러 결정 문제가 미치는 효과를 연구하기 위한 이산 사건 시뮬레이션 프레임워크다. | ref-101 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 및 D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 22. 시뮬레이션·예측용 디지털 트윈: Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f3 | [추정] | 연계 대상: 22. 시뮬레이션·예측용 디지털 트윈의 성수기 시나리오 입력(주문·물동량 전망)은 A. 업무·공급망 설계의 1. 주문·업무 시스템 연계를 거쳐 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 수요예측 자체는 분류 원문 9장의 상위 업무 시스템 경계에 속한다. | ref-521 | 아니오 | low | 2024 | 피킹 / 시작 조건 | 원문 미열람 |
| f4 | [추정] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ 21. 온보딩·설정·현장 시운전: 다중 AGV 도입이 정밀 지도 작성·좌표 지정·수작업 경로망 설계로 오래 걸린다는 연구와 설치 기간을 6개월에서 2개월로 줄일 수 있다는 과제 측 보고가 있어, 온보딩 기간이 증차한 로봇이 처리능력으로 바뀌는 시점을 좌우하는 것으로 보인다. | ref-217, ref-265 | 아니오 | low | 2017 | 적치 / 예외·성과 | 원문 미열람 |
| f5 | [추정] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ 23. 시험·형식 검증·벤치마크: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있어 공정 모델의 형식적 점검이 형식 검증과 이어질 것으로 보이나, 물류 로봇 공정 적용 사례는 확인되지 않았다. | ref-121 | 아니오 | low | 2022 | — | 원문 미열람 |
| f6 | [사실] | B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지 ↔ 21. 온보딩·설정·현장 시운전: IDTA 02020 능력 기술(Capability Description) 서브모델은 공정이 요구하는 능력과 자원이 제공하는 능력을 비교하게 하고, 능력을 속성·제약(전제조건·순서)·스킬로 구조화해 자원의 매칭과 시운전을 돕는다고 설명한다. | ref-229 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f7 | [사실] | Vieira da Silva 외(2024-06)는 자연어 능력 설명에서 대규모 언어 모델(LLM)을 이용해 능력 온톨로지를 생성하는 방법을 제안했다. | ref-465 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f8 | [추정] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 21. 온보딩·설정·현장 시운전: 분류 원문 8장 교차 규칙이 매뉴얼 해석을 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 AI 연구 방법으로 두므로, LLM 기반 능력 온톨로지 생성은 새 로봇 등록 작업을 줄이는 방법으로 두 대분류를 잇는 것으로 보인다. | ref-465, ref-229 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f9 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 RMF 좌표계 사이 변환을 위한 기준 좌표(대응 경유점)를 설정에 두고, 대응 경유점을 최소 4개 둘 것을 권한다. | ref-153 | 아니오 | medium | 2026-09-25 | 적치 / 수행 자원 | — |
| f10 | [사실] | 21. 온보딩·설정·현장 시운전 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델, C. 연결·실행 기반의 10. 설비·건물 시스템 연동, D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF traffic-editor 는 차선·경유점·충전소·주차 지점·문·승강기·층과 기준점(fiducial)을 이용한 층간 정렬을 주석하게 하고, 주석한 그래프는 building_map_generator 로 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 지도 내려받기·활성화·삭제 즉시 동작(downloadMap·enableMap·deleteMap)을 두고 같은 mapId 에서는 한 번에 한 버전만 활성화하게 하며, 상태 스키마는 로봇이 mapId·mapVersion·mapStatus(ENABLED·DISABLED)를 보고하게 한다. | ref-031, ref-051 | 아니오 | medium | 2026-09-25 | 적치 / 시작 조건 | — |
| f12 | [추정] | 분류 원문이 6. 지도·공간·위치 모델에 '지도 버전 관리'를, 24. 자산·소프트웨어 수명주기 관리의 정의에 '지도 버전'을 함께 넣고 VDA 5050 이 지도 배포·활성화를 관제의 지시로 두므로, 지도 버전의 내용 정의는 B. 공통 정보·환경 모델 쪽, 배포·활성화 시점 조율과 이력 관리는 F. 도입·검증·유지관리 쪽이 맡는 분담이 될 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f13 | [사실] | Kritzinger 외(2018)는 제조 분야 문헌을 검토해 물리 객체와 디지털 객체 사이 데이터 흐름의 자동화 정도에 따라 디지털 모델·디지털 섀도·디지털 트윈을 구분했다. | ref-291 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f14 | [추정] | B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 8번은 현재 상태를 표현하고 22번은 그 모델을 이용해 가정한 미래를 실험한다는 분류 원문 구분에 따라, 22번은 8번의 현재 상태(로봇·설비·배터리 상태)를 시나리오 초기값으로 받는 쪽이 될 것으로 보이며, 근거 분류 자료가 물류가 아닌 제조 대상이라는 한계가 있다. | ref-291, ref-406 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [사실] | B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 상태 스키마는 충전 상태(stateOfCharge), 배터리 건강 상태(batteryHealth, 0~100%), 현재 충전량으로 추정한 도달 거리(range), 충전 여부(charging)를 로봇이 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 출하 / 수행 자원 | — |
| f16 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 및 C. 연결·실행 기반의 10. 설비·건물 시스템 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션 문서에 따르면 building_map_generator 는 traffic-editor 로 주석한 건물 지도에서 Gazebo 시뮬레이션 세계와 주행 그래프를 만들고, 문·승강기 플러그인, 워크셀을 흉내 내는 TeleportDispenser·TeleportIngestor, 여러 플릿 어댑터의 승강기 요청을 조율하는 lift_supervisor 를 둔다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f17 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Sommer 외(2023)는 건물 환경 스캔과 객체 검출을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 제시했다. | ref-241 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f18 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: VDA 5050 3.0.0 은 팩트시트를 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보로 두고, 초기 설정과 관제–이동로봇 능력 사이의 지속적인 호환성 평가에 쓰도록 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f19 | [사실] | VDA 5050 팩트시트 스키마는 적재 명세(loadSpecification.loadSets), 로봇 구성의 버전 목록(mobileRobotConfiguration.versions, 예: softwareVersion), 충전 설정(batteryCharging: criticalLowChargingLevel·minimumDesiredChargingLevel·maximumDesiredChargingLevel·minimumChargingTime)을 담아, 한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화에 함께 쓰인다. | ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 설정은 최대 선·각속도와 가속도, 수행 가능한 작업 유형(loop·delivery·clean), 로봇 외곽 반경, 배터리·재충전 임계값, 제조사 관제 API 연결 정보(주소·계정)를 요구한다. | ref-153 | 아니오 | medium | 2026-09-25 | 적치 / 수행 자원 | — |
| f21 | [사실] | 22. 시뮬레이션·예측용 디지털 트윈·23. 시험·형식 검증·벤치마크 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 시뮬레이션 문서는 시뮬레이션 속 로봇이 배터리 소모나 충돌 비용 없이 장시간·가속 조건으로 드문 예외 상황을 시험할 수 있고, 장시간 시뮬레이션이 배치 전 시설 소유자의 확신을 높인다고 설명한다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f22 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션의 slotcar 플러그인은 경로·모드 요청을 받아 레일식으로 움직이고 센서 기반 주행 스택 없이 로봇 상태를 발행하는 전체 제어(full control) 로봇 모델이다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f23 | [추정] | slotcar 같은 단순화 모델은 제조사 관제·로봇 고유 거동을 재현하지 않으므로, 9. 로봇·제조사 관제 연동 방식(전체 제어·신호등·읽기 전용)과 제조사별 거동 차이가 22. 시뮬레이션·예측용 디지털 트윈의 처리량 예측 오차 원인이 될 것으로 보인다(oq-086). | ref-406 | 아니오 | low | 2026-09-25 | — | — |
| f24 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 오류를 CRITICAL 수준과 오류 필드 참조로 보고하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 적치 / 예외·성과 | — |
| f25 | [사실] | C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성 ↔ 24. 자산·소프트웨어 수명주기 관리: ROS 2 관리형 노드는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate 같은 전이를 두어, 감독 도구가 구성요소 준비를 확인한 뒤 실행을 허용하게 한다. | ref-364 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f26 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동·12. 명령·작업 실행의 신뢰성 ↔ 23. 시험·형식 검증·벤치마크: 공개 개인 프로젝트 vda5050-sim 은 VDA 5050 3.0.0 주문 수명주기·동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을, vda5050-lab 은 MQTT 기록에서 반복 주문 id·재연결·취소 불일치를 진단한다고 README 에 적으며, 둘 다 VDA·VDMA 공식 적합성 시험이 아니다. | ref-407, ref-408 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f27 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 여러 관제 업체와 VDA 5050 인증을 마쳤다고 2026-04 발표했으나, 인증의 시험 항목은 확인되지 않았다. | ref-608 | 아니오 | low | 2026-04 | — | 원문 미열람, 벤더 주장 |
| f28 | [추정] | 연계 대상: ros2_fault_injection 은 오도메트리·레이저 스캔·IMU·점군 같은 센서 신호와 속도 명령을 조작하는 로봇 수준 장애 주입 도구이며, 23. 시험·형식 검증·벤치마크에서 ROP 쪽 장애 주입은 같은 프록시 방식을 C. 연결·실행 기반의 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. | ref-601 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f29 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 22. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망(roadmap)을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있다. | ref-267 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f30 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 23. 시험·형식 검증·벤치마크: Stern 외(2019)는 MAPF 의 가정·목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했으나, 그 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). | ref-186 | 아니오 | medium | 2019-06 | — | 원문 미열람 |
| f31 | [사실] | Yan 외(2026-02)는 기존 MAPF 연구가 단순한 운동 모델과 완전한 실행·통신을 가정한다고 지적하고, 플릿 관리 시스템 안에서 계획 시점·방법·복구 설계 선택을 비교하는 시험대(LSMART)를 제안해 D. 계획·최적화의 경로 알고리즘과 23. 시험·형식 검증·벤치마크를 잇는다. | ref-604 | 아니오 | medium | 2026-02-17 | — | 원문 미열람 |
| f32 | [사실] | von Berg 외(2026-05)는 창고 물류 AGV 의 교착 회피를 전이 시스템 인코딩과 BDD 로 분석한 사례 연구를 발표해, 15. 다중 로봇 경로·교통 관리 — MAPF 의 교착 문제가 23. 시험·형식 검증·벤치마크의 형식 검증 대상이 됨을 보인다(계산 규모 한계는 oq-088). | ref-609 | 아니오 | medium | 2026-05 | — | 원문 미열람 |
| f33 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 23. 시험·형식 검증·벤치마크: Lott·Honary(2026-09 프리프린트)는 분산 작업 배정기 6종을 패킷 손실·페이딩 같은 통신 저하 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크를 제시했다. | ref-493 | 아니오 | medium | 2026-09 | — | 원문 미열람 |
| f34 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ 24. 자산·소프트웨어 수명주기 관리: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 작업 배정·충전 일정을 정하는 연구(2026-03, 프리프린트)가 있다. | ref-403 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f35 | [추정] | 로봇이 보고하는 batteryHealth 가 낮아지면 같은 충전 상태에서도 도달 거리(range)가 짧아질 수 있어, 24. 자산·소프트웨어 수명주기 관리의 배터리 열화 정보가 D. 계획·최적화의 13. 작업 배정 — MRTA·16. 공용 자원·충전·에너지 최적화의 제약 입력이 되는 것으로 보인다(물류센터 실측 자료 미확인). | ref-051, ref-403 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f36 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ 23. 시험·형식 검증·벤치마크: NIST ARIAC 2025 문서는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급(고우선) 주문을 과제로 두어 설비·로봇 장애와 긴급 주문 대응을 평가한다. | ref-528 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f37 | [추정] | ARIAC 같은 장애 과제 정의와 장애 주입 도구를 결합하면, 20. 예외 복구·재계획·업무 연속성의 재배정·수동 전환·제한 운영 동작을 업데이트마다 다시 돌리는 회귀 시험 시나리오로 만들 수 있을 것으로 보이나, 물류 오케스트레이션에 적용해 공개한 사례는 확인되지 않았다(oq-087). | ref-528, ref-601 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f38 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ 23. 시험·형식 검증·벤치마크: ASTM F3499-21 은 자율 무인 지상 차량(A-UGV)의 도킹 성능을 확인하는 시험 방법이며, 그 결과를 로봇팔 파지 허용 오차와 잇는 기준은 확인되지 않았다(oq-063). | ref-204 | 아니오 | medium | 2021 | 완료·인계 | 원문 미열람 |
| f39 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 24. 자산·소프트웨어 수명주기 관리: Lei 외(2025)는 산업용 로봇의 고장 모드·데이터 수집·모델 기반과 데이터 기반 진단을 상태 기반 정비 관점에서 정리한 검토를 발표했다. | ref-553 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f40 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 23. 시험·형식 검증·벤치마크: ROSMonitoring 은 ROS 시스템의 런타임 검증 프레임워크로, 운영 중 감시가 사전 시험을 보완하는 연결 지점이 된다. | ref-602 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f41 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하며, 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | 적치 / 제약 | 원문 미열람 |
| f42 | [추정] | 연계 대상: 국내에는 바퀴형 서비스 로봇의 이동 성능 시험방법 KS B ISO 18646-1 과 한국로봇산업진흥원의 시험평가 서비스가 있어, 로봇 자체 성능 시험은 시험기관 쪽이고 23. 시험·형식 검증·벤치마크의 ROP 몫은 그 결과를 등록·배정 조건으로 받는 쪽으로 보인다(oq-089). | ref-606, ref-607 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f43 | [추정] | 한국산업기술시험원(KTL)과 통합물류협회가 물류로봇 시험인증 협력을 강화하기로 했다고 2026-07 보도되어, 국내 물류로봇 시험·인증 체계가 23. 시험·형식 검증·벤치마크와 28. 표준·상호운용성·다사업자 거버넌스를 잇는 후보가 될 것으로 보인다. | ref-466 | 아니오 | low | 2026-07-24 | — | 원문 미열람 |
| f44 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ 24. 자산·소프트웨어 수명주기 관리: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템(IACS) 환경의 패치 관리를 다루는 기술 보고서다. | ref-554 | 아니오 | medium | 2015-06 | — | 원문 미열람 |
| f45 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 24. 자산·소프트웨어 수명주기 관리: 로봇 시스템 위험성평가 가이드는 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로, 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 미확인이다(oq-092, oq-093). | ref-559 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f46 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 23. 시험·형식 검증·벤치마크: ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과(목표 조건·성공률)로 자동 평가하는 공개 벤치마크다. | ref-539, ref-541 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f47 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고, 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나 물류센터 적용 여부는 미확인이다(oq-085). | ref-516, ref-518 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f48 | [추정] | 이번에 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 새 로봇 연동 승인 기준으로 쓰고 판 차이(2.x·3.0.0)로 생기는 UNSUPPORTED_PARAMETER 같은 미지원 오류를 누가 판정·수정할지가 23. 시험·형식 검증·벤치마크·24. 자산·소프트웨어 수명주기 관리에서 28. 표준·상호운용성·다사업자 거버넌스로 넘어가는 과제가 될 것으로 보인다(oq-055, oq-091). | ref-407, ref-408, ref-608, ref-031 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 예 |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2201.05588 | 예 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-204 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | 표준 | medium | 2026-09-25 | https://www.astm.org/f3499-21.html | 예 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 예 |
| ref-265 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-364 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-466 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | 기사 | low | 2026-09-25 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-493 | Lott, J., & Honary, V.(University of San Diego) | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 2026-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2609.13711 | 예 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/87426.html | 예 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 예 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/askforalfred/alfred | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-553 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 예 |
| ref-554 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | 표준 | medium | 2026-09-25 | https://webstore.iec.ch/en/publication/22811 | 예 |
| ref-559 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | 벤더 문서 | low | 2026-09-25 | https://doc.safetics.io/insight-risk-assessment/ | 예 |
| ref-601 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/reeceholland/ros2_fault_injection | 예 |
| ref-602 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 예 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.15721 | 예 |
| ref-606 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 예 |
| ref-607 | 한국로봇산업진흥원(KIRIA) | 시험평가 \| KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kiria.org/rp/kiria/tva/inr/page.dn | 예 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-609 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/index.md | 5. 다른 대분류와의 연결 | '다른 대분류와의 연결' 절만 patches 로 채운다. A. 업무·공급망 설계: f1·f2(22↔3·4), f3(22↔1, 연계 대상), f4(21↔3), f5(23↔2) / B. 공통 정보·환경 모델: f6·f7(21↔5), f9·f10(21↔6), f11·f12(24↔6 지도 버전), f13·f14(22↔8, 8·22 구분 유지), f15(24↔8), f16·f17(22↔6) / C. 연결·실행 기반: f18·f19·f20(21↔9), f10(21↔10), f16·f21(22·23↔10), f22·f23(22↔9, oq-086), f24(24↔9), f25(24↔12), f26·f27(23↔9·12, f27 벤더 주장 병기), f28(23↔12, 연계 대상) / D. 계획·최적화: f2(22↔13), f29(22↔15), f10(21↔15), f30·f31·f32(23↔15), f33(23↔13), f19·f34·f35(24↔13·16) / E. 협업·현장 운영: f36·f37(23↔20), f38(23↔17), f39(24↔19), f40(23↔19) / G. 안전·보안·지능·거버넌스: f41(21·23↔25), f42·f43(23↔28, 연계 대상), f44(24↔26), f45(24↔25), f8·f46(21·23↔27, 교차 규칙), f47(22↔28), f48(23·24↔28) / '아직 다루지 않은 연결': 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(oq-081), 21. 온보딩·설정·현장 시운전 ↔ E. 협업·현장 운영, 22 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적과의 연결은 근거 미확보. 다음 실행 후보: B. 공통 정보·환경 모델 페이지의 '아직 다루지 않은 연결'(23·24)을 f11·f15 로 보강. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 23. 시험·형식 검증·벤치마크, 10. 설비·건물 시스템 연동, 21. 온보딩·설정·현장 시운전 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 38 · 교차 확인: 0
- 예산 사용량: 검색 1회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f11 은 VDA 명세와 VDA 스키마로 독립 출처 아님)
    - f27 OTTO VDA 5050 인증의 시험 항목 미확인(벤더 주장)
    - f43 KTL·통합물류협회 협력 내용은 기사 기준, 1차 출처 미확인
    - f45 국내 변경 후 재평가 공식 규정 미확인(oq-092)
    - 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거 미확보(oq-081)
    - ref-407·ref-408·ref-121·ref-204·ref-539·ref-541 은 이번 입력의 참고문헌 요약 목록에 없어 게시 페이지 각주·이전 브리프 값을 옮겼고, 유형·신뢰도는 이번 실행의 판단
- 범위 경계 위반 의심:
    - f3: 수요예측은 분류 원문 9장 상위 업무 시스템 경계라 '연계 대상:' 표시
    - f28: 센서 신호 장애 주입은 로봇 자체 인식·주행 견고성 시험이라 '연계 대상:' 표시
    - f42: 로봇 자체 성능 시험은 시험기관·제조사 쪽이라 '연계 대상:' 표시
    - f13·f17·f47: 제조 대상 자료라 물류 적용은 미확인으로 명시
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-228(factsheet.schema), ref-079(traffic-editor.md), ref-153(fleet adapter tutorial), ref-406(simulation.md), ref-229(IDTA 02020 README), ref-528(ARIAC challenges.rst). 나머지 30건은 게시 페이지 각주·이전 브리프 재사용이며 원문 미열람(신뢰도 상한 medium). 대분류 연결 실행 규칙(R-3)에 따라 근거를 게시된 21~24 세부영역 페이지와 A·B·C·D·E 대분류 페이지 각주에서 먼저 찾았고 신규 출처는 0건이다. 한국어 검색 1회(물류센터 AMR 가상 시운전 디지털 트윈)는 기사·업체 블로그뿐이라 쓰지 않았다. 한국 자료: KS B ISO 18646-1(ref-606), KIRIA 시험평가(ref-607), KTL 협력 보도(ref-466), KS X ISO 23247-1(ref-516). 교차 규칙: 매뉴얼 해석 AI 는 f8 로 21. 온보딩·설정·현장 시운전·5. 로봇 능력·작업 온톨로지·27. AI·학습·적응과 모델 운영에 함께 연결했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f14 에서 원문 구분대로 나눴다. 페이지 절 번호는 대분류 페이지 절 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)로 5를 붙였다 [가정]. 정정 요청 없음. 해결된 열린 질문 없음.
```
