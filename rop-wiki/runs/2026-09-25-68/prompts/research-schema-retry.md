(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-68
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 27. AI·학습·적응과 모델 운영 (G. 안전·보안·지능·거버넌스)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 세부영역 반영 제안: 15건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- next_ref_id: ref-734
- 새 출처 id 구간: ref-734 ~ ref-763 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-734 부터 순서대로 쓰고 ref-763 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-09-25-68/target.json

```json
{
  "run_id": "2026-09-25-68",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 68,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 27,
    "area_name": "27. AI·학습·적응과 모델 운영",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=27"
}
```

### docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 27
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 27. AI·학습·적응과 모델 운영

# 27. AI·학습·적응과 모델 운영

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [분류원문]

## 2. SCM 관점의 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

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

### data/area_reflection_proposals.json (대상 영역 27. AI·학습·적응과 모델 운영 에 대한 트랙 반영 제안 15건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-05",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 1,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "도면 해석(교차 규칙상 6. 지도·공간·위치 모델에 적용되는 방법): 다중 작업 신경망(DeepFloorplan), 자기회귀 그래프 예측(Raster-to-Graph), 검출기·LLM·사람 검수를 잇는 반자동 주석 구축(DoorDet, 저자 의견), VLM 평면도 파싱(DeFazio 외 2024). 6. 지도·공간·위치 모델 페이지와 양쪽 연결. 근거 f4·f9·f15·f16.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-04",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 출력을 실행 전에 접지·점검하는 방법: 기술 가치 함수(SayCan), 고전 계획기에 PDDL 넘김(LLM+P), LTL 식 변환(Lang2LTL). 형식 명세 경유 구조가 오해석 방지와 이어진다는 [추정]. 적용 대상 13. 작업 배정 — MRTA와 양쪽 연결(교차 규칙: 학습 기반 배차). 센서 인식·제어는 연계 대상. 근거 ref-087, ref-088, ref-091, ref-092, ref-055, ref-056.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-04",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "Cohen 외(IJCAI-24) 로봇 언어 접지 서베이(형식 표현–임베딩 스펙트럼, 장단점 평가는 [의견])와 Huang 외(ICML 2022), SayCan, LLM+P, Lang2LTL을 대표 자료로 등록하고 13. 작업 배정 — MRTA 페이지와 연결. 근거 ref-058, ref-093, ref-087, ref-091, ref-055.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-21",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 다중 로봇 서베이의 네 층 분류(상위 작업 배정·중간 동작 계획·저수준 동작 생성·사람 개입)와 과제(수학적 추론 한계·환각·지연·벤치마크 부족), 사람이 정한 도구·함수 목록 안에서 명령·코드를 생성하는 LLM 에이전트(ChatGPT for Robotics, ROSA, RAI, 한국전자기술연구원 사례)와 연 문서 범위에서 실행 전 확인·권한 장치 설명이 없다는 관찰([추정]).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-21",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "LLM 다중 로봇 서베이(ref-165), ChatGPT for Robotics(ref-174)와 PromptCraft(ref-173), ROSA(ref-171·ref-172), RAI(ref-175), 한국전자기술연구원 초록(ref-180).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-21",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "summary": "교차 규칙에 따라 적용 대상 13. 작업 배정 — MRTA(학습 기반 배차)와 연결: LLM 직접 배정과 LLM 정식화 + 최적화 배정 연구.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-30",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 불확실성 정량화(등각 예측, KnowNo)로 필요할 때만 사람에게 묻는 방법, LLM 에이전트의 빠진 인자 지어내기와 Ask-when-Needed, 모호성 탐지의 낮은 구분 성능(AmbiK, 저자 보고값·주방 텍스트 작업 조건), 구조화 출력([추정] 벤더 주장). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-30",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "KnowNo(ref-350·ref-351), AmbiK 데이터셋·논문(ref-354·ref-355), Wang 외 Learning to Ask(EMNLP 2025, ref-359), LMCR(ICRA 2020, ref-358), OpenAI 구조화 출력 발표문(ref-362, [추정] 벤더 주장)",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-37",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 2,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 지시 해석이 뽑는 인자와 접지 방법: DELIVER 는 픽업·배송 위치 추출(화물·기한 추출은 요약 범위에서 미확인, f10), SayPlan 은 3D 장면 그래프 의미 탐색으로 계획을 접지(f11, 저자 보고), SafeGate 는 안전 속성 추출·결정적 게이트(f12). 적용 대상인 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-36",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "도면 해석 AI 방법으로 CAD 레이어·블록 계층을 이용한 자동 라벨링(ArchCAD-400K, ref-434), 텍스트 주석 유형·속성을 결합한 다중 모달 심볼 스포팅(arXiv 2607.12678, ref-433), YOLOv8·OFA-OCR 기반 래스터 축척 인식(ref-435)을 적용 대상 6. 지도·공간·위치 모델과 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-54",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "교차 규칙(도면 해석은 6. 지도·공간·위치 모델에 적용)에 따라 시각-언어 모델 벡터화(FloorplanVLM, 외벽 IoU 92.52% 저자 보고 단일 출처, f3), 불확실성 기반 사람 참여 루프(Jakubik 외 2022, f5), LLM 다중 에이전트와 사람 피드백·스키마 검증(Sketch2BIM, f6), 검출기·LLM·사람 검수 반자동 절차(DoorDet, f7)를 6. 지도·공간·위치 모델 페이지와 양쪽에 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-54",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "FloorplanVLM(ref-463), Jakubik 외 AAAI 2022(ref-458), Sketch2BIM(ref-457), DoorDet(ref-077)를 도면 해석 연구로 등재(모두 원문 미열람, 수치는 저자 보고).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-57",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 2,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "분류 원문 8장 교차 규칙에 따라 매뉴얼 해석은 이 영역의 방법이 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 것이다. 매뉴얼 대상 LLM 추출 방법으로 온톨로지 제약 RAG 기반 개체·관계 추출과 대화형 절차 안내를 결합한 프레임워크(ref-514, 원문 미열람)와 제조 문서 항목–속성–값 삼중항 추출 벤치마크 ManuExtract(ref-515, 원문 미열람)를 든다(f14·f15). 적용 대상 영역 페이지 양쪽에 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-57",
      "date": "2026-09-25",
      "track": "manual-capability-ontology",
      "stage": 2,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "범용 문서 파싱 벤치마크 OmniDocBench(1,651 PDF 페이지, 텍스트·표·수식·읽기 순서 평가, 문서 유형에 매뉴얼 없음, ref-513)와 매뉴얼 대상 추출 연구 두 건(ref-514·ref-515)을 자료로 추가한다. 로봇 매뉴얼 형태별 추출 난이도를 측정한 공개 자료는 이번 조사에서 찾지 못했다(부재 확정 아님, f12·f13). 교차 규칙에 따라 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에도 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-62",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 2,
      "area_no": 27,
      "section": "8. 대표 연구와 자료",
      "summary": "LLM 지시 해석·계획 평가 벤치마크(LoTa-Bench 자동 정량화, AmbiK 모호 지시 1000쌍, NoisyToolBench 불완전 지시, Lang2LTL 발화–LTL 말뭉치, Snips 의도·슬롯)와 해석 정확도·계획 목표 달성도를 나눠 재는 두 층 평가(추정)를 추가하고, 적용 대상 13. 작업 배정 — MRTA 와 18. 사람–로봇 협업·운영 인터페이스에 연결한다.",
      "status": "제안"
    }
  ]
}
```

### docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md (요약)

```markdown
# 25. 안전·위험 관리

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

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

### docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md (요약)

```markdown
# 28. 표준·상호운용성·다사업자 거버넌스

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 574건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 148개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
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

### docs/open-questions.md (요약: 대상 영역 [27] 에 걸린 1건 / 전체 93건)

```markdown
- oq-030 [열림] 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? (영역 13, 27)
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

### runs/2026-09-25-63/research.md

```markdown
# 리서치 브리프 2026-09-25-63

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-63 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 25. 안전·위험 관리 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(위험성평가, 3단계 위험 감소, 운용 구역, 안전 필드 침범, STPA)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 nl-task-chatbot 단계 2 반영 제안 SafeGate 1건 포함)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역 열린 질문 oq-064, oq-070 걸려 있음)

## 조사 질문

1. 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
2. 이동 로봇·산업용 로봇의 안전 표준(ISO 3691-4, ANSI/A3 R15.08, ISO 10218-2:2025, ISO 12100)은 제조사·통합자·사용자의 책임을 어떻게 나누는가? (섹션 3·7·9 겨냥)
3. 로봇 상호운용 규격과 오픈소스 오케스트레이션(VDA 5050, Open-RMF)은 비상정지·정지·재개·비상 대응을 어떤 메시지와 범위로 다루는가? (섹션 4·6·9 겨냥)
4. 여러 로봇이 함께 움직일 때 생기는 상호작용 위험을 분석하는 방법(STPA 등)과 대표 연구는 무엇인가? (섹션 6·8 겨냥)
5. oq-070 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가?
6. oq-064 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 국내 규제(산업안전보건기준에 관한 규칙)는 로봇 방호를 어떻게 요구하는가? (섹션 3·5·11 겨냥)
7. LLM 이 만든 작업 지시를 실행 전에 안전 판정하는 접근(SafeGate)은 무엇이며 ROP 에 어떤 한계로 적용되는가? (트랙 반영 제안, 섹션 6 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 범위 절에 명시한다. | ref-569 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 상태 메시지의 safetyState 는 비상정지 상태(eStop: AUTOACK·MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 보고하고, 즉시 동작 startPause·stopPause 로 자동 주행을 멈추고 재개하며, operatingMode 로 로봇이 자동 주문을 받는지(AUTOMATIC)·수동 제어 중인지(MANUAL)를 알린다. | ref-569 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | Open-RMF 핵심 설계에서 교통 충돌 예방은 RMF 의 교통 스케줄 데이터베이스와 협상이 맡고 경로 계획은 각 플릿 관리자가 맡으며, 비상 대응 같은 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | Open-RMF 공식 저장소의 기능 요청(이슈 #658)에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동하며, 현재 비상 신호 메시지는 어느 건물·플릿 대상인지 구분하지 않는 불리언 값이어서 대상 플릿 목록(fleet_names)을 지정하자는 제안이 올라와 있다. | ref-580 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f5 | [사실] | ISO 3691-4:2023 은 무인 산업 차량(AGV·AMR·자동 대차·견인차 포함)과 그 시스템의 안전 요구와 검증 방법을 정하며, 운용 구역(operating zone)의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. | ref-570 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f6 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR) 한 대 또는 플릿을 현장에 통합·구성·맞춤화할 때의 안전 요구를 정하는 시스템 통합자용 표준으로, 로봇 자체 요구는 Part 1 이, 사용자 요구는 예정된 Part 3 이 맡는다. | ref-571 | 아니오 | medium | 2023-10 | 수행 자원 | 원문 미열람 |
| f7 | [사실] | ISO 10218-2:2025(산업용 로봇 응용과 로봇 셀)는 2011년판을 대체해 2025년 2월 발행됐으며, 협동 운전 요구(종전 ISO/TS 15066)를 본문에 통합하고 사이버보안 요구를 더했으며 '로봇 시스템' 대신 공작물·작업 프로그램·지원 설비까지 포함하는 '로봇 응용'을 강조한다. | ref-572 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f8 | [사실] | 중소벤처기업부는 대구 이동식 협동로봇 규제자유특구 실증으로 안전성을 검증한 뒤 이동식 협동로봇 안전기준 한국산업표준(KS)을 제정해 2024-11-01 부터 산업현장에서 활용할 수 있게 했다고 밝혔고, 그 전에는 명확한 기준이 없어 작업공간 분리나 안전펜스 설치 때문에 이동 중 작업이 사실상 불가능했다고 설명했다. | ref-573 | 아니오 | medium | 2024-11-03 | 제약 | 원문 미열람 |
| f9 | [사실] | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 사업주에게 로봇 운전 중 위험을 막기 위해 높이 1.8m 이상 울타리 설치 등을 요구하되, 고용노동부장관이 해당 로봇의 안전기준이 한국산업표준 또는 국제적으로 통용되는 안전기준에 부합한다고 인정하면 울타리 등 조치를 생략할 수 있게 한다. | ref-574 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f10 | [사실] | SafeGate(arXiv 2604.05427)는 자연어 작업 명령에서 ISO 13482 에 근거한 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람에게 확인 요청·거부 중 하나를 내고, 승인한 작업은 불변 조건·가드·중단 조건으로 된 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했으며, 230개 벤치마크 작업·30개 AI2-THOR 시나리오·실로봇 실험으로 평가했다고 저자가 보고한다. | ref-575 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f11 | [사실] | 국내에는 협동로봇 기술규격 ISO/TS 15066 이 KS B ISO/TS 15066 로 부합화되어 한국표준정보망에 등재되어 있다. | ref-581 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f12 | [사실] | Belzile 외(arXiv 2502.20693)는 사람이 붐비는 작업장에 이동 로봇을 배치할 때의 안전 위험을 정량 지표로 평가하는 틀을 제안하고 ISO/TS 15066·ANSI/RIA R15.08 등 관련 표준을 검토했으며, 건설 현장 사례로 검증했다. | ref-576 | 아니오 | medium | 2025-02 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | STPA(System-Theoretic Process Analysis) 계층 제어 구조 비교 연구는 복잡한 다중 이동 로봇 시스템에 STPA 를 적용해 중앙집중·계층형 등 제어 구조별 위험 시나리오와 원인 요인을 도출했다. | ref-577 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | Reliability Engineering & System Safety 게재 연구는 다중 이동 로봇의 운반 작업에서 충돌 위험을 STPA 와 확률 페트리 넷(SPN)을 결합해 모델링·분석했다. | ref-578 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | ISO 12100:2010 은 기계 설계의 위험성평가와 위험 감소 일반 원칙을 정하며, 위험 감소는 본질적 안전 설계 → 방호·보완 보호 조치 → 사용 정보의 순서로 앞 단계를 다한 뒤 다음 단계로 가는 3단계 방법을 따른다. | ref-579 | 아니오 | medium | 2010 | — | 원문 미열람 |
| f16 | [추정] | 분류 원문 질문과 관련해, 확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08-1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025 의 로봇 응용)을 나누고 STPA 연구는 개별적으로 정상인 구성요소 간 상호작용에서 위험을 찾으므로, 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. | ref-570, ref-571, ref-572, ref-577 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f17 | [추정] | ROP 가 직접 맡을 안전 몫은 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집, 일시정지·재개 지시, 비상 신호에 따른 플릿별 대피·주차 조율, 구역·권한 제약을 경로·배정에 반영하는 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. | ref-569, ref-004, ref-580 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f18 | [추정] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증과 현장 방호 설비는 로봇 제조사와 설비 안전 제어(분류 원문 9장) 쪽이며, ROP 는 그 상태와 결과를 받는 쪽으로 보인다. | ref-569, ref-570, ref-572 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [추정] | 피킹 구역에 작업자가 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고하면, ROP 는 해당 로봇의 진행 중 피킹 작업을 보류·재배정하고 재개 조건(안전 상태 해제, 운용 모드 AUTOMATIC 복귀)을 확인한 뒤 stopPause 등으로 재개를 지시해야 할 것으로 보인다. | ref-569 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f20 | [추정] | 출하 마감 전에 화재경보 같은 비상 신호가 오면 로봇이 주차 위치로 이동해 출하 준비 작업이 중단되므로, 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 성과(마감 준수)에 영향을 주는 것으로 보인다. | ref-580, ref-004 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f21 | [추정] | 25. 안전·위험 관리는 사이버보안 요구가 안전 표준에 들어온 점에서 26. 사이버보안·접근권한·개인정보와, LLM 명령의 실행 전 안전 판정에서 27. AI·학습·적응과 모델 운영·18. 사람–로봇 협업·운영 인터페이스와, 교통 협상에서 15. 다중 로봇 경로·교통 관리 — MAPF 와, 정지·재개 지시의 확실한 전달에서 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. | ref-572, ref-575, ref-004, ref-569 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-569 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-570 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-571 | Association for Advancing Automation (A3) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-572 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/73934.html | 예 |
| ref-573 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 예 |
| ref-574 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-575 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-576 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2502.20693 | 예 |
| ref-577 | IEEE Xplore (저자 미확인) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System | 미확인 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/8910126/ | 예 |
| ref-578 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 예 |
| ref-579 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | 표준 | medium | 2026-09-25 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 예 |
| ref-580 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-581 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f16(분류 원문 질문, 추정), f8·f9(국내 규제 맥락) / 4절: f15(위험성평가·3단계), f5(운용 구역), f2(비상정지·보호 필드 침범), f13(STPA) / 5절: f19(피킹·예외·성과), f20(출하·예외·성과) / 6절: f13·f14(STPA 기반 다중 로봇 위험 분석), f12(정량 위험 지표), f10(SafeGate — 트랙 nl-task-chatbot 단계 2 반영 제안 2026-09-25-37 f12 반영; ISO 13482 는 개인 돌봄 로봇 표준·저자 보고 평가·물류 현장 아님 병기) / 7절: f1·f2(VDA 5050), f3·f4(Open-RMF), f5(ISO 3691-4), f6(R15.08-2), f7(ISO 10218-2:2025), f11(KS B ISO/TS 15066), f8(이동식 협동로봇 KS), f9(산안규칙 제223조), f15(ISO 12100) / 8절: f12·f13·f14·f10 / 9절: f17(ROP 직접), f18('연계 대상') / 10절: f21(26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스, 15. 다중 로봇 경로·교통 관리 — MAPF, 12. 명령·작업 실행의 신뢰성), 24. 자산·소프트웨어 수명주기 관리(2026-09-25-61 브리프의 변경 후 재평가) / 11절: oq-064·oq-070 유지와 open_questions_new 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 위험성평가 | Risk Assessment (ISO 12100) | 위험원을 찾고 위험을 추정·평가해 위험 감소가 필요한지 판단하는 절차로, ISO 12100 이 기계 설계의 일반 원칙으로 정한다. |
| 3단계 위험 감소 방법 | Three-Step Method (ISO 12100) | 본질적 안전 설계, 방호·보완 보호 조치, 사용 정보의 순서로 위험을 줄이는 ISO 12100 의 우선순위 원칙이다. |
| 운용 구역 | Operating Zone (ISO 3691-4) | 무인 산업 차량이 운행하는 구역으로, ISO 3691-4 는 사람 유무 등 구역 조건에 따라 준비와 안전 요구를 달리 둔다. |
| 시스템 이론적 프로세스 분석 | System-Theoretic Process Analysis (STPA) | 개별 부품 고장보다 정상 동작하는 구성요소 사이의 안전하지 않은 제어 상호작용에서 위험 시나리오를 찾는 위험 분석 기법이다. |

## 열린 질문

새로 생긴 질문:

- ROP 가 원격 비상정지(VDA 5050 eStop REMOTE)나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? | 관련 영역: 25. 안전·위험 관리, 12. 명령·작업 실행의 신뢰성 | 근거: f2 | 종류: 일반
- 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? | 관련 영역: 25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f6 | 종류: 일반
- 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? | 관련 영역: 25. 안전·위험 관리, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f9 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 11회 · 신규 출처 13건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - oq-070 이동식 협동로봇 KS 표준 번호 미확인(정부 보도자료 검색 요약에 번호 없음) — 미해결 유지
    - oq-064 R15.08-2 유형 C 대응 KS·인증 기준 미확인 — 미해결 유지
    - f7 ISO 10218-2:2025 변경 내용은 ISO 소개 페이지 원문 미열람, 검색 요약(인증기관·협회 해설) 기준
    - f10 SafeGate 평가 수치는 저자 보고, 원문 미열람
    - ref-575·ref-577·ref-578 저자, ref-577·ref-580·ref-581·ref-004·ref-569 발행일 미확인
    - ISO 3691-4 의 제조사–통합자 책임 분담은 2차 해설에만 있어 finding 에서 제외
- 범위 경계 위반 의심:
    - f18: 안전 기능 설계·방호 설비는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 쪽이라 '연계 대상:'으로 표시
    - f12: 건설 현장 사례라 방법론 근거로만 제안(업종별 조건 연계)
    - f10: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 현장 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f5 가 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 처음부터 다시 작성했다(검색 11회/30). 이번 브리프는 벤더 문서 출처를 하나도 쓰지 않았고, 모든 [사실] finding 은 표준·정부·오픈소스·논문 출처에 기대며, 벤더 문서만 근거로 한 [사실] finding 이 없다(관련 finding: f5 는 이제 ISO 3691-4 표준 근거). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 신규 ref-569(VDA 5050 3.0.0 명세), 재사용 ref-004(rmf-core). 나머지 12건은 검색 요약 기준(원문 미열람, 신뢰도 상한 medium). ref-004 는 참고문헌 목록 요약이 입력에 없어 리서치 규칙 예시의 값을 그대로 썼다. 신규 출처 13건(ref-569~ref-581, 예약 구간 안). 한국 자료: 이동식 협동로봇 KS 제정 보도자료(ref-573), 산안규칙 제223조(ref-574), KS B ISO/TS 15066(ref-581). 트랙 반영 제안(nl-task-chatbot 단계 2, SafeGate)은 f10 으로 확인해 6절에 제안했다. 교차 규칙: SafeGate 는 27. AI·학습·적응과 모델 운영과 적용 대상 영역에 함께 연결하도록 f21 로 제안. 8·22 구분 관련 주장 없음. 정정 요청 없음.
```

### runs/2026-09-25-62/research.md

```markdown
# 리서치 브리프 2026-09-25-62

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-62 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 2 · 답한 질문 q2-03

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-03 열림(target.json 지정, CLI 지정 질문 id). 단계 2 페이지 3절에 q2-03 소제목 없음
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 4절에 평가 데이터(지시–정답 작업 쌍) 소절 없음(q2-03 미조사로 명시됨)
- 완료 조건: 업무 분해·배정 설계 초안의 작업 요구 적재물 속성·업무 완료 조건 미확정(이번 질문 범위 밖)
- 13. 작업 배정 — MRTA 섹션 8. 대표 연구와 자료(주제 페이지)에 LLM 배정 평가 데이터셋·지표 근거 없음
- 23. 시험·형식 검증·벤치마크 페이지 seed 상태: 지시 해석·계획 평가 벤치마크 근거 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q2-03 해석·분해의 정확도를 평가하려면 어떤 지시–정답 작업 쌍 데이터가 필요하며, 쓸 수 있는 공개 데이터셋이 있는가?
3. 지시를 행동 순서·목표 조건으로 바꾸는 체화 에이전트 벤치마크(ALFRED, TEACh, LoTa-Bench)는 지시와 정답을 어떤 형식(목표 조건, 전문가 시연, 최종 상태)으로 짝지우는가? (단계 2 페이지 3절 겨냥)
4. 다중 로봇 LLM 계획·배정 벤치마크(SMART-LLM 데이터셋, MAT-THOR)는 정답과 지표(성공률, 목표 조건 재현율, 로봇 활용도)를 어떻게 두는가? (13. 작업 배정 — MRTA 섹션 8, 23. 시험·형식 검증·벤치마크 연결)
5. 모호·불완전 지시와 슬롯 추출을 평가하는 데이터셋(AmbiK, NoisyToolBench, Snips NLU 벤치마크, Lang2LTL 말뭉치)은 무엇을 정답으로 두는가? (27. AI·학습·적응과 모델 운영 연결)
6. 물류·창고 지시를 대상으로 한 지시–정답 데이터셋이나 국내 공개 데이터(AI Hub)가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ALFRED 는 자연어 지시와 1인칭 시각 입력을 가정 작업의 행동 순서로 대응시키는 학습 벤치마크로, AI2-THOR 2.1.0 시뮬레이터 위에서 상위 목표 기술과 단계별 지시를 함께 제공한다. | ref-539 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | ALFRED 논문(CVPR 2020)은 25,743개의 영어 지시와 8,055개의 전문가 시연을 담고, 시연은 PDDL 로 기술한 환경 동역학과 작업별 PDDL 목표 조건을 고전 계획기에 주어 생성했다고 밝힌다. | ref-540 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f3 | [사실] | LoTa-Bench(ICLR 2024)는 가정 서비스 에이전트의 언어 기반 작업 계획 성능을 자동으로 정량화하는 벤치마크로, ALFRED·AI2-THOR 와 Watch-And-Help 확장·VirtualHome 두 쌍에서 성공률로 계획기를 비교한다. | ref-541, ref-542 | 아니오 | medium | 2024-02 | — | — |
| f4 | [사실] | TEACh 는 AI2-THOR 가정 환경에서 지시하는 사람(Commander)과 수행하는 사람(Follower)이 대화하며 작업을 완수한 사람–사람 대화 세션 데이터셋으로, EDH·TfD·TATC 세 벤치마크를 두고 데이터는 CDLA-Sharing 1.0 으로 공개된다. | ref-543 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | SMART-LLM 공식 저장소는 작업 복잡도가 다른 네 범주의 상위 지시로 이루어진 다중 로봇 작업 계획 벤치마크 데이터셋을 두고, 평가용으로 작업마다 사용 가능한 로봇과 작업 후 환경의 최종 상태를 함께 제공한다. | ref-089 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | SMART-LLM 논문은 AI2-THOR 기반 36개 상위 지시 데이터셋에서 성공률, 작업 완료율, 정답 최종 상태 조건 대비 목표 조건 재현율(GCR), 정답 전이 수와 비교한 로봇 활용도(RU), 실행 가능 동작 비율(Exe)의 다섯 지표로 평가한다. | ref-090 | 아니오 | medium | 2023-09 | — | 원문 미열람 |
| f7 | [사실] | LaMMA-P 의 MAT-THOR 는 AI2-THOR 기반 다중 에이전트 가정 작업 벤치마크로, 논문은 5개 평면도의 70개 작업(복합 30, 복잡 20, 모호한 지시 20)마다 자연어 지시·정답 PDDL 도메인·목표 조건을 붙였다고 밝힌다. | ref-164, ref-544 | 아니오 | medium | 2024-09 | — | — |
| f8 | [사실] | AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍을 보정용 100건·시험용 900건으로 나누고, 환경 설명, 직접·간접·모호 지시문, 모호성 유형, 명확화 질문과 답, 작업 계획, 계획 안에서 모호성이 나타나는 지점을 필드로 둔다. | ref-354 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | NoisyToolBench 는 ToolBench 의 정상 표본 200건을 사람이 불완전하게 바꿔 만든 불명확 지시 벤치마크로, 핵심 인자 누락 등 지시 문제 유형을 나누고, 자동 평가기 ToolEvaluator 로 정확도와 되묻기 상호작용 효율을 함께 잰다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f10 | [사실] | Snips 의 NLU 벤치마크(2017-06)는 7개 의도마다 크라우드소싱으로 만든 2000개 이상의 질의를 두고 슬롯별 정밀도·재현율로 비교해, 의도 인식·슬롯 채우기 평가용 지시–정답 쌍의 형식을 보여 준다. | ref-545 | 아니오 | medium | 2017-06 | — | — |
| f11 | [사실] | Lang2LTL 연구는 47개 LTL 식 템플릿에서 나온 2,125개의 고유 LTL 식에 약 5만 개 영어 발화를 대응시킨 말뭉치와, 22개 OSM 환경의 1만 개 이상 명령으로 된 접지 평가 자료를 만들었다고 보고한다. | ref-056 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f12 | [사실] | AI Hub 의 '일상생활 작업 및 명령 수행 데이터(임무수행 명령어)'는 3D 일상생활 공간에서 에이전트가 자연어 명령을 이해해 일련의 행동을 예측하고 상호작용할 객체 위치를 1인칭 시점 이미지에서 찾도록 구축한 국내 공개 학습 데이터다. | ref-546 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [사실] | 연계 대상: OpenBench 는 주거 지역 실외 라스트마일 배송 로봇의 의미 기반 항법 벤치마크로, LLM 이 배송 지시를 이해하고 OpenStreetMap 지도를 쓰는 기준 시스템(OPEN)을 함께 공개했다. | ref-547 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f14 | [사실] | 물류 AMR 임무 명세에 LLM 을 번역 인터페이스로 쓰는 스웨덴 Högskolan Väst 학위논문은 LLM 이 신호 시간 논리(STL) 식의 구문·논리를 만들 수는 있으나 구문상 유효한 STL 식을 일관되게 만들지 못한다고 보고했다. | ref-548 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | 확인한 공개 데이터셋을 종합하면 해석·분해 평가용 지시–정답 쌍은 (1) 지시문, (2) 초기 환경 상태, (3) 정답 목표 조건·최종 상태 또는 형식 명세(PDDL·LTL), (4) 선택적으로 정답 계획·전이 수, (5) 모호 지시의 경우 모호성 유형과 명확화 질문·답을 담는 구조로 보인다. | ref-540, ref-541, ref-090, ref-544, ref-354, ref-056 | 아니오 | low | 2026-09-25 | — | — |
| f16 | [추정] | 이번에 확인한 지시–정답 데이터셋의 환경은 가정·주방(ALFRED, TEACh, SMART-LLM, MAT-THOR, AmbiK), 도구 호출 API(NoisyToolBench), 개인 비서(Snips), 실외 내비게이션·배송(Lang2LTL, OpenBench)이었고, 화물 식별자·로케이션·기한·배정 로봇을 정답으로 둔 물류 창고 지시 데이터셋은 검색 범위에서 찾지 못해 ROP 는 평가 자료를 자체 구축해야 할 것으로 보인다(부재의 확인은 아님). | ref-539, ref-543, ref-089, ref-544, ref-354, ref-359, ref-545, ref-547, ref-548 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f17 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 확인한 다중 로봇 벤치마크는 목표 상태 달성과 정답 전이 수 대비 로봇 활용도를 재지만 누구에게 배정했는지의 전체 최적성(이동거리·납기)을 정답으로 두지 않으므로, 배정 적합성을 평가하려면 정답 배정이나 목적함수 기준값을 따로 마련해야 할 것으로 보인다. | ref-090, ref-544 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f18 | [추정] | 확인한 평가 방식은 해석 단계(의도·슬롯별 정밀도·재현율, Snips)와 계획·실행 단계(시뮬레이터 최종 상태·목표 조건 달성, LoTa-Bench·SMART-LLM)로 나뉘어, 챗봇 평가도 해석 정확도와 분해·배정 결과의 목표 달성도를 따로 재는 두 층 구조가 필요할 것으로 보인다. | ref-545, ref-541, ref-090 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/askforalfred/alfred | 아니오 |
| ref-540 | Shridhar, M. 외 | ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | 2020 | 논문 | medium | 2026-09-25 | https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 아니오 |
| ref-542 | LoTa-Bench 저자(arXiv 2402.08178) | LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.08178 | 예 |
| ref-543 | Amazon Alexa (alexa/teach GitHub) | TEACh: Task-driven Embodied Agents that Chat (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/alexa/teach | 아니오 |
| ref-544 | Zhang, X. 외(LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.20560 | 예 |
| ref-545 | Snips (sonos/nlu-benchmark GitHub) | nlu-benchmark — 2017-06-custom-intent-engines (README) | 2017-06 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/sonos/nlu-benchmark/tree/master/2017-06-custom-intent-engines | 아니오 |
| ref-546 | 한국지능정보사회진흥원(AI Hub) | 일상생활 작업 및 명령 수행 데이터(임무수행 명령어) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71547 | 예 |
| ref-547 | OpenBench 저자(arXiv 2502.09238) | OpenBench: A New Benchmark and Baseline for Semantic Navigation in Smart Logistics | 2025-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2502.09238 | 예 |
| ref-548 | Högskolan Väst (DiVA 학위논문, 저자 미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 미확인 | 논문 | low | 2026-09-25 | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf | 예 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/SMARTlab-Purdue/SMART-LLM | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-164 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/tasl-lab/LaMMA-P | 아니오 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/cog-model/AmbiK-dataset | 아니오 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2302.11649 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 low) — 2절 q2-03 상태 답함, 3절 q2-03 소제목 신설({#q2-03}): 체화 에이전트 벤치마크(ALFRED f1·f2, LoTa-Bench f3, TEACh f4), 다중 로봇 벤치마크와 지표(SMART-LLM f5·f6, MAT-THOR f7), 모호·불완전 지시(AmbiK f8, NoisyToolBench f9), 해석 단계 데이터(Snips f10, Lang2LTL f11), 국내 데이터(AI Hub f12), 물류 인접 자료(OpenBench f13 연계 대상, STL 학위논문 f14), 필요한 쌍 구조(f15), 물류 데이터셋 공백(f16), SCM 질문 연결(f17), 두 층 평가(f18) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 4 | 아이디어 페이지 4절: '해석·분해 평가 데이터' 소절 신설 — 공개 데이터셋 비교(f1·f3·f4·f5·f7·f8·f9·f10·f11·f12), 필요한 지시–정답 쌍 구조(f15, 추정), 물류 데이터셋 공백(f16, 추정), 배정 적합성 정답 부재(f17). 6절(검증 방법)로 이어지는 지표(f6·f18)는 단계 5 에서 다룸을 명시 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f5, f6, f7, f17): LLM 다중 로봇 배정 평가 데이터셋(SMART-LLM, MAT-THOR)과 지표(목표 조건 재현율·로봇 활용도), 배정 최적성 정답이 없다는 점과 분류 원문 질문 연결. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f3, f8, f9, f11, f18): LLM 지시 해석·계획 평가 벤치마크(LoTa-Bench, AmbiK, NoisyToolBench, Lang2LTL 말뭉치)와 해석·계획 두 층 평가. 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결 |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f1, f3, f6, f16): 지시 수행 벤치마크(ALFRED, LoTa-Bench)와 시뮬레이터 최종 상태 기반 자동 평가, 물류 지시 평가 자료 부재(추정) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 목표 조건 | Goal Condition | 작업이 끝났을 때 환경이 만족해야 하는 상태 조건의 집합으로, 지시 수행 벤치마크에서 계획·실행 결과가 맞았는지를 판정하는 정답으로 쓰인다. |
| 신호 시간 논리 | Signal Temporal Logic (STL) | 연속 시간 신호에 대해 시간 구간이 붙은 조건(예: 10초 안에 도착)을 기술하는 형식 논리로, 로봇 임무 명세에 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터의 작업 지시(피킹·운반·출하 준비)를 자연어 지시와 정답 작업·배정 결과로 짝지은 공개 데이터셋이나 구축 사업이 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 10건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 데이터셋마다 공식 저장소와 같은 저자 논문 쌍이거나 단일 출처
    - f2 ALFRED 수치(25,743·8,055)는 논문 원문 미열람, 검색 요약 기준 저자 보고값
    - f6 SMART-LLM 36개 지시·지표 정의는 논문 원문 미열람(README 는 네 범주만 기재)
    - f7 MAT-THOR 70개 작업 구성은 논문 원문 미열람. README 는 '두 복잡도 수준'이라고만 적어 범주 수 표현이 다름
    - f9 NoisyToolBench 문제 유형 비율은 2차 요약에만 있어 넣지 않음
    - f11 Lang2LTL 말뭉치 수치는 판마다 다른 요약(1,156개 명령 말뭉치 등)이 있어 판 차이 미확인
    - f12 AI Hub 데이터의 구축 기관·규모·정답 형식 미확인
    - f14 학위논문 저자·발행일·평가 자료 규모 미확인
    - f16 물류 지시 데이터셋 부재는 검색 범위의 관찰이며 부재 확인 아님
    - PlanBench(자연어·PDDL 프롬프트, Blocksworld 계열)는 README 가 리더보드만 보여 Logistics 도메인 포함 여부를 확인하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f13: OpenBench 는 실외 라스트마일 배송(분류 원문 9장 업종별 조건·실외 차량 연계 영역)이라 '연계 대상: '으로 표시하고 평가 자료 사례로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 신규 ref-539(ALFRED README)·ref-541(LoTa-Bench README)·ref-543(TEACh README)·ref-545(Snips NLU 벤치마크 README), 재사용 ref-089(SMART-LLM README)·ref-164(LaMMA-P README)·ref-354(AmbiK README). 논문·AI Hub·학위논문(ref-540·ref-542·ref-544·ref-546·ref-547·ref-548, 재사용 ref-090·ref-359·ref-056)은 원문 미열람(신뢰도 상한 medium). 검색 17회/40, 신규 출처 10건/20(ref-539~ref-548, 예약 구간 안), 재사용 6건. 질문 선택: target.json 지정 q2-03 1건. q2-03 은 공개 데이터셋의 지시–정답 형식과 지표(사실 finding)로 답했으나 필요한 쌍 구조·물류 공백·배정 정답 부재(f15~f18)는 이 위키의 종합이라 질문 종합 신뢰도를 low 로 두었다. 한국 자료: AI Hub 국내 공개 데이터(ref-546, 가정 환경)를 찾았고 국내 물류 지시 데이터셋은 찾지 못해 일반 열린 질문 1건으로 올렸다. 교차 규칙: LLM 해석·계획 평가 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA 양쪽에 반영 제안했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(시뮬레이터는 평가 도구로만 언급). 정정 요청 없음. 온톨로지 변경 없음: 평가 데이터는 업무 분해·배정 설계 초안의 개념·관계가 아니라 검증 자료이므로 초안 변경 근거가 되지 않는다. 후속 질문 2건. 백로그 참고: q3-09 와 q3-10 이 사실상 같은 질문으로 중복 등록되어 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 2
- 답한 질문 id: q2-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 물류 지시 평가 자료를 자체 구축할 때 지시–정답 쌍의 정답을 무엇(업무 분해·배정 설계 초안의 작업 모델 인스턴스, 최종 상태·목표 조건, 배정 결과)으로 두고, ALFRED 목표 조건·SMART-LLM 최종 상태·AmbiK 명확화 질문 형식을 화물·로케이션·기한 항목으로 어떻게 확장하는가? (q2-03 에서 파생) | 5 | f16 |
| — | 배정 적합성을 평가하려면 목표 상태 달성 외에 정답 배정이나 목적함수 기준값이 필요한데, 이를 최적화 해법기(MILP 등)로 생성해 LLM 배정 결과와 비교하는 정답으로 쓸 수 있는가? (q2-03 에서 파생) | 5 | f17 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 아이디어 2. 자연어 업무 지시 챗봇 4절에 평가 데이터 소절은 이번 제안 검증 승인 전
    - 작업 모델 정보 항목 일부 미반영(작업 요구 적재물 속성·업무 완료 조건 미확정)
    - 열린 질문 q2-04, q2-05, q2-06, q2-07
```


## 스키마 불일치 (재실행)

직전 반환값이 JSON 스키마(schemas/research.schema.json)와 맞지 않아 퍼블리셔가 반려했다. 아래 오류를 모두 고친, 스키마에 맞는 JSON 객체 하나만 다시 반환한다. 내용을 새로 조사하지 말고 형식만 고친다.

- finding f8: 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시가 없다(6.2 항목 13)
