(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-15
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 5. 로봇 능력·작업 온톨로지 (B. 공통 정보·환경 모델)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-25-15/target.json

```json
{
  "run_id": "2026-09-25-15",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 15,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 5,
    "area_name": "5. 로봇 능력·작업 온톨로지",
    "category": "B. 공통 정보·환경 모델",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=5"
}
```

### runs/2026-09-25-15/research.json

```json
{
  "run_id": "2026-09-25-15",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 5,
    "area_name": "5. 로봇 능력·작업 온톨로지",
    "category": "B. 공통 정보·환경 모델"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 트랙 반영 제안(능력·스킬 구분, 전제조건·효과, 광고 능력·운용 능력) 미반영",
    "섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안(IEEE 1872 계열, SSN/SOSA, CSS, IDTA 02020) 미반영이며 IDTA 02020 은 제3자 논문 경유 근거뿐",
    "섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안(KnowRob 2.0, SOMA, RCO, 서베이, 이종 자율 로봇 능력·스킬 모델, 국내 KCI 논문) 미반영",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-004 연결 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]",
    "로봇의 기능·제약·장착 장비·실행 조건을 공통으로 표현하는 표준·온톨로지(IEEE 1872 계열, W3C SSN/SOSA, CSS 모델, IDTA 02020, SOMA 등)는 무엇이며 각각 무엇을 표현하는가? (섹션 4·7, 트랙 반영 제안 4·7절 겨냥)",
    "물류 이동로봇 인터페이스(VDA 5050 팩트시트, MassRobotics, Open-RMF)는 적재·작업 능력을 어떤 필드로 선언하며, 무엇이 구조화되지 않고 남는가? (섹션 5·6 겨냥)",
    "작업 요구와 로봇 능력을 대조해 배정 가능성을 판단하는 연구는 무엇을 입력으로 쓰고 결과를 어떻게 배정기에 넘기는가? (섹션 6·8·10 겨냥)",
    "매뉴얼·로봇 기술 기술서에서 능력 모델을 자동으로 만드는 방법(교차 규칙에 따른 27. AI·학습·적응과 모델 운영의 적용)은 무엇이며 결과를 어떻게 검증하는가? (섹션 6·8 겨냥)",
    "oq-004 국내 표준(KS)이나 국내 연구에서 로봇 능력·모듈 정보 모델을 다룬 것이 있는가? (섹션 7·8·11, 한국 자료 우선)",
    "능력 모델에서 ROP가 직접 맡을 부분과 로봇 자체 지능·제어(파지·인식·로컬 회피)에 맡길 부분의 경계는 어디인가? (섹션 9 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 공식 저장소 main(3.0.0판)의 팩트시트 스키마는 헤더 항목과 함께 typeSpecification(로봇 등급·능력), physicalParameters, protocolLimits, protocolFeatures, mobileRobotGeometry, loadSpecification(적재 능력의 추상 명세)을 필수 블록으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "factsheet.schema 원문: typeSpecification 'These parameters generally specify the class and the capabilities', loadSpecification 'Abstract specification of load capabilities'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 팩트시트의 적재 명세 loadSets 는 적재 유형(loadType, 예 EPAL), 적재 치수, 최대 중량(maximumWeight), 최소·최대 적재 처리 높이, 픽·드롭 소요 시간(pickTime, dropTime)을 기술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "loadSets: setName, loadType 'Type of load e.g., EPAL, XLT1200', loadDimensions, maximumWeight(kg), minimum/maximumLoadhandlingHeight(m), pickTime·dropTime(초). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 팩트시트의 지원 동작 목록(mobileRobotActions)은 동작마다 actionType, 자유 문장 설명(actionDescription), 허용 범위(actionScopes), 파라미터(key·valueDataType·isOptional), 일시정지 가능 여부(pauseAllowed), 취소 가능 여부(cancelAllowed)를 기술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "actionDescription 'Free text: description of the action'; valueDataType 은 BOOL, NUMBER, INTEGER, STRING, OBJECT, ARRAY 중 하나. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 팩트시트의 동작 파라미터 기술에는 허용 값 범위나 실행 전제조건을 담는 구조화 필드가 없어, 그런 조건은 자유 문장 설명이나 적재 명세의 최소·최대 필드에 흩어져 기술될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "actionParameters 하위 필드는 key, valueDataType, isOptional 뿐임을 원문에서 확인한 데서 도출한 추론. 이전 실행과 같은 결론. (재인용: 2026-09-25-06)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "MassRobotics AMR 상호운용 표준 JSON 스키마는 식별 보고에 최대 속도·예상 가동 시간·충전기 유형·화물 설명(cargoType)·화물 최대 부피·최대 중량·제품 문서 링크를, 상태 보고에 운영 상태(navigating·idle·charging·waitingHumanEvent 등 9개 값)와 남은 적재 용량 비율을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "cargoMaxWeight 'Max weight of cargo in kg', productDocumentation 'Link to product documenation', loadPercentageStillAvailable 'Percentage of capacity still available'(0~100). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "VDA 5050 팩트시트의 loadType 과 MassRobotics 의 cargoType 은 모두 적재물 유형을 문자열로 적게 할 뿐 공통 어휘를 지정하지 않으므로, 제조사 간 화물 취급 가능 여부를 맞추려면 적재물 유형 사전이 별도로 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "loadType 설명은 예시('EPAL, XLT1200')만, cargoType 설명은 'Discription of cargo' 뿐임을 두 원문에서 확인한 데서 도출. 공통 어휘 부재의 확인은 아님.",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "작업 대상"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 플릿 어댑터 템플릿 설정은 플릿이 수행할 수 있는 RMF 작업 유형(task_capabilities: loop, delivery 등), 사용자 정의 동작 이름 목록(actions), 작업 종료 후 동작(finishing_request: park·charge·nothing)을 플릿 단위로 선언하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 주석: task_capabilities 'Specify the types of RMF Tasks that robots in this fleet are capable of performing'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "Open-RMF 에서 사용자 정의 동작은 설정의 actions 목록에 이름으로만 선언되고, 작업 요청의 category(동작 이름)와 JSON description 으로 호출되며, 어댑터가 로봇 API 의 완료를 확인한 뒤 execution.finished() 를 호출해 완료를 알린다.",
      "tag": "사실",
      "source_ids": [
        "ref-040"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "튜토리얼 원본 예: actions: [\"clean\"], description {\"zone\": \"clean_lobby\"}, is_command_completed() 확인 후 self.execution.finished(). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f9",
      "claim": "IDTA 02020 Capability Description 서브모델 1.0 은 능력을 속성(최대 속도·허용 오차·온도 범위 등), 전제조건·불변조건·사후조건 역할의 속성 제약과 순서·병렬 흐름을 정하는 전이 제약, 능력을 구현하는 스킬로 기술하며, 요구 능력과 제공 능력의 신뢰할 수 있는 비교를 목적으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-229"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IDTA 저장소 README 원문: 'reliable comparison between required and provided capabilities', 속성 제약은 'preconditions, invariants, or postconditions'. IDTA 첫 공식판 1.0. 이전 제3자 논문 경유 근거를 대체. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "능력(capability)은 구현과 무관한 기능 명세이고 스킬(skill)은 OPC UA 같은 호출 인터페이스를 가진 능력의 구현이라는 구분을 IDTA 02020 과 CaSkMan 온톨로지가 공통으로 쓰며, 두 자료 모두 Plattform Industrie 4.0 의 능력·스킬·서비스(CSS) 모델 계열이다.",
      "tag": "사실",
      "source_ids": [
        "ref-229",
        "ref-231",
        "ref-035"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "IDTA: 'implementation-independent specification of a function'. CaSkMan README: 스킬은 'An encapsulated implementation with a well-defined invocation interface (e.g., using OPC UA)', CSS 참조 모델 위에 구축. 발행 주체가 달라 독립으로 봄(같은 CSS 계열).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "CaSkMan 은 설비 구조, 추상 능력, 상태 기계를 가진 실행 스킬, 속성을 모델링하고 VDI 3682(공정 입출력), VDI 2860(취급 작업 분류), DIN 8580(제조 공정 분류), ISA 88(상태 기계), IEC 61360(속성 형식 기술)을 잇는 정렬 온톨로지이다.",
      "tag": "사실",
      "source_ids": [
        "ref-231"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: ISA 88 은 'a state machine which is widely used in automation', 스킬 인터페이스 기술은 WADL·OPC UA. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "IDTA 02047 Technical Data for AGV 1.0 은 여러 제조사·유형의 무인운반차를 한 생산 환경에서 운영하기 위해 제조사 독립적인 기술 데이터를 자산관리셸(AAS) 서브모델로 표준화하려는 명세이다.",
      "tag": "사실",
      "source_ids": [
        "ref-234"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: 'Different types of vehicles and vehicles from different manufacturers have to be operated in one production environment'. AAS 메타모델 3.0 호환. 세부 필드는 README 범위에서 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "W3C/OGC SSN 의 System Capabilities 모듈은 특정 조건(Condition) 아래 시스템의 정확도·범위 등 능력(SystemCapability), 정상 운용 범위(OperatingRange), 벗어나면 손상되는 생존 범위(SurvivalRange)를 hasSystemCapability·inCondition 관계로 기술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-235"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ssn-system.ttl: SurvivalRange 'If the SurvivalRange is violated, the System is damaged and SystemCapability specifications may no longer hold'. 작업반 저장소 편집본이라 /TR 권고안과 문구가 다를 수 있음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "SOMA 는 DUL(DOLCE+DnS Ultralite) 상위 온톨로지를 확장한 OWL 활동 온톨로지로, 로봇 에이전트의 의도·계획·움직임·물체와의 접촉 같은 활동 측면을 표현한다.",
      "tag": "사실",
      "source_ids": [
        "ref-233",
        "ref-028"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SOMA 공식 저장소 README: 'an ontological model of activities', 'fully implemented in form of an OWL ontology which is based on the DOLCE+DnS Ultralite (DUL)'. 논문(ref-028) 원문 미열람.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "헬무트 슈미트 대학 연구실이 공개한 IEEE 1872.2 AuR 온톨로지 OWL 구현은 로봇이 제공하고 기능 실행으로 수행되는 기능(function), 로봇 간·물체와의 상호작용, 환경을 기술하며 IEEE 1872 를 DUL·SUMO 상위 온톨로지로 확장하는 제3자 구현이다.",
      "tag": "사실",
      "source_ids": [
        "ref-232",
        "ref-026"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: 'A function is provided by a robot, which is actually executable via function execution.' IEEE 공식 산출물이라는 표시는 없음. 표준 원문(ref-026) 미열람.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f16",
      "claim": "IEEE 1872-2015 는 로봇·자동화 분야의 일반 개념·관계·공리를 담은 핵심 온톨로지(CORA)를 정한 IEEE 표준 온톨로지이다.",
      "tag": "사실",
      "source_ids": [
        "ref-025"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표준 제목 'IEEE Standard Ontologies for Robotics and Automation'(2015). 용어집 CORA 항목과 같은 근거. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2015",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "KnowRob 2.0(Beetz 외, 2018)은 인지 기반 로봇 에이전트를 위한 2세대 지식 처리 프레임워크이다.",
      "tag": "사실",
      "source_ids": [
        "ref-027"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "논문 제목 수준의 서지 확인. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2018",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "PDDL 은 행동을 파라미터·전제조건·효과로 기술하고 도메인과 문제 인스턴스를 분리해 표현하는 계획 언어이다.",
      "tag": "사실",
      "source_ids": [
        "ref-029"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "McDermott 외(1998) PDDL 문서. 용어집 PDDL 항목과 같은 근거. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "1998",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "Naqvi 외(Scientific Reports, 2025)는 제조사가 광고한 능력(advertised capabilities)과 운용 중 관측된 능력(operational capabilities)을 온톨로지로 구분해 통합하는 방법을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-041"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "논문 제목 'Ontology-driven integration of advertised and operational capabilities in robots'(2025-10-02). 세부 모델은 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2025-10-02",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "Aguado 외(2024)는 자율 로봇의 신뢰성(dependability)을 위해 온톨로지를 쓰는 프로세스를 정리한 서베이를 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-042"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Frontiers in Robotics and AI 2024-07 게재, 제목 수준 확인. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2024-07",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "Vieira da Silva·Köcher·Fay(2022)는 이종 자율 로봇을 위한 능력·스킬 모델을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-038"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2209.10900 'A Capability and Skill Model for Heterogeneous Autonomous Robots'. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2022-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "신민종·한영석·정재윤(2024)은 자산관리셸 표준을 이용한 자율이동로봇 모니터링 시스템 설계 논문을 국내 학술지에 게재했다.",
      "tag": "사실",
      "source_ids": [
        "ref-043"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 서지 기준 게재 사실만 확인, 능력 기술 포함 여부는 미확인. 원문 미열람. (재인용: 2026-09-25-02)",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "Electronics(2026-08) 게재 연구는 로봇·작업·장소의 의미 모델과 선언적·절차적 혼합 추론으로 다축 능력 조건과 적재 상태에 따른 장소 도달 가능성을 판정하고, 결과를 배정 알고리즘과 무관한 공통 입력(ReasonerOutput)으로 넘기는 이종 다중 로봇 작업 배정용 실행 가능성 추론을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-236"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 기존 연구는 실행 가능성을 특정 최적화기 안에서 다루고 통행 가능성을 'static criteria that cannot capture the changes induced by a robot's loaded state'로 평가. 15(16) 3562. 저자 미확인.",
      "as_of": "2026-08-11",
      "flow_step": "적치",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "Kluge-Wilkes 외의 CAPILANO 는 이종 조립 자원과 그 결합 능력을 OWL 온톨로지로 기술하고 SPARQL 질의와 가용성을 고려한 연속 작업 배정(Python)을 하나의 틀로 묶어 라인리스 이동 조립 시스템에 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-237"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: Protégé OWL 모델, SPARQL 기반 질의, 'consecutive and availability-aware task allocation', 배정의 선형 확장성 시연. 제조 조립 대상이며 물류는 아님.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "Vieira da Silva 외(ETFA 2024)는 여러 LLM 과 프롬프트 기법으로 복잡도가 다른 능력 온톨로지를 생성하고, RDF 구문 검사·OWL 추론·SHACL 제약에 기반한 반자동 품질 검사로 복잡한 능력에서도 오류가 거의 없었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-238"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2404.17524 검색 요약: 'semi-automated approach based on RDF syntax checking, OWL reasoning, and SHACL constraints', 'almost free of errors'. 저자 주장이며 실험 조건은 원문 미열람.",
      "as_of": "2024-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "Dussard·Sarthou(ICSR 2026)는 URDF 로봇 기술 파일의 식별자를 LLM 으로 해석해 기존 온톨로지 개념으로 분류·채우고, 여러 질의의 다수결과 구문·스키마 수준 검증으로 신뢰성을 높이는 파이프라인을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2606.17073 검색 요약: 'majority voting across multiple LLM queries along with syntactic and schema-level validation'. LAAS-CNRS. 초기 결과 단계.",
      "as_of": "2026-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "ISO 22166-201:2024 는 서비스 로봇 모듈의 상호운용성·재사용성·조립 가능성을 위해 모듈 공통 정보 모델(CIM)의 구조와 속성·하위 클래스의 의미를 정한 국제표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-240"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 소개 요약: CIM 으로 모듈을 쉽게 연결하고 데이터 교환, 'interoperability, reusability, and automatic composability'. Part 202:2025 는 소프트웨어 모듈 정보 모델. 원문 미열람.",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "국가표준 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 KSSN 에 등록되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-138"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 검색 결과 표제 기준. 제정일·ISO 22166 부합 여부·내용은 원문 미열람으로 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "같은 운반 로봇 가운데 어느 로봇이 특정 화물을 실제로 취급할 수 있는지는 적재 명세(적재 유형·최대 중량·처리 높이), 지원 동작, 현재 상태(남은 적재 용량·운영 상태), 적재 상태에서의 경로 통과 가능성을 함께 대조해야 판단할 수 있어 한 규격의 필드만으로는 결정되지 않을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-230",
        "ref-236"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3(팩트시트 적재·동작), f5(MassRobotics 상태의 남은 용량), f23(적재 상태 도달 가능성)을 분류 원문 SCM 질문에 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "수행 자원"
    },
    {
      "id": "f30",
      "claim": "기존 표준에서 능력 기술과 실행의 연결은 같은 인터페이스 안에서 선언한 동작 이름을 명령·완료 보고에 그대로 쓰는 방식(VDA 5050, Open-RMF)과, 별도 능력 모델을 상태 기계를 가진 스킬 인터페이스로 잇는 방식(IDTA 02020, CaSkMan)으로 나뉘는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-040",
        "ref-229",
        "ref-231"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f8(이름 기반 선언·호출)과 f9·f10·f11(능력–스킬–상태 기계)을 대조한 추론. 두 방식을 매핑한 표준은 확인하지 못함. (재인용: 2026-09-25-06)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f31",
      "claim": "매뉴얼·로봇 기술 파일에서 능력 온톨로지를 LLM 으로 만드는 연구들은 생성 결과를 기존 온톨로지 스키마·추론기·SHACL 같은 형식 검증에 통과시키는 절차를 공통으로 두는 것으로 보여, 문서 기반 능력 모델 구축에서도 생성과 검증을 분리한 구조가 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-238",
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f25(RDF·OWL·SHACL 반자동 검사)와 f26(다수결·스키마 검증)에서 도출. 물류 로봇 매뉴얼 대상 사례는 이번 검색에서 확인하지 못함.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "연계 대상: 파지·센서 인식·로컬 회피 같은 능력의 실제 구현과 성능 보장은 분류 원문 9장의 로봇 자체 지능·제어 쪽이며, 이종 제조사를 연결하는 ROP는 제조사가 선언한 능력·제약(팩트시트·능력 서브모델)을 공통 모델로 모아 작업 요구와 대조하고 실행 결과로 선언과 실제의 차이를 기록하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-229",
        "ref-041"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f9(제조사 선언 구조), f19(광고 능력과 운용 능력 구분)를 분류 원문 9장 '로봇 자체 지능·제어' 경계와 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f33",
      "claim": "Meseguer Valenzuela·Blanes Noguera(2025)는 의료·물류 등에서 쓰이는 이동로봇 플릿의 작업 배정 문제를 에너지 소비와 필요 로봇 수 최소화 관점에서 정리하고 AI 기반 방법을 포함한 주요 최적화 알고리즘을 검토했다.",
      "tag": "사실",
      "source_ids": [
        "ref-152"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2501.08726 검색 요약: TA 는 'minimization of energy consumption and quantity of necessary robots'를 위한 핵심 주제. 원문 미열람.",
      "as_of": "2025-01",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 공식 저장소 main(3.0.0판)의 팩트시트 JSON 스키마. 유형 명세·물리 파라미터·지원 동작·적재 명세 블록의 필드를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-229",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "IDTA 공식 서브모델 템플릿 저장소의 능력 기술 서브모델 1.0 안내. 능력 정의, 속성, 속성 제약·전이 제약, 스킬과의 관계, 요구·제공 능력 비교 목적을 설명한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Capability%20Description/1/0/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 식별 보고(최대 속도·화물 최대 중량·부피 등)와 상태 보고(운영 상태·남은 적재 용량) 필드를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-231",
      "org": "CaSkade-Automation (GitHub)",
      "title": "CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README)",
      "published": null,
      "url": "https://github.com/CaSkade-Automation/CaSkMan",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "제조 설비의 능력·스킬·스킬 인터페이스·속성을 기술하는 OWL 정렬 온톨로지 저장소 README. VDI 3682·VDI 2860·DIN 8580·ISA 88·IEC 61360 과 CSS 참조 모델을 잇는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/CaSkade-Automation/CaSkMan/master/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-232",
      "org": "Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub)",
      "title": "IndustrialStandard-ODP-IEEE1872-2 — README (IEEE 1872.2 AuR ontology OWL implementation)",
      "published": null,
      "url": "https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "IEEE 1872.2 AuR 온톨로지를 OWL 로 구현한 제3자 저장소 README. 로봇 기능과 기능 실행, 상호작용·환경 기술을 설명하며 IEEE 표준 본문은 아니다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-233",
      "org": "EASE CRC (ease-crc/soma)",
      "title": "SOMA — README (Socio-physical Model of Activities)",
      "published": null,
      "url": "https://github.com/ease-crc/soma",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "SOMA 공식 저장소 README. DUL 상위 온톨로지를 확장해 로봇 에이전트의 활동을 표현하는 OWL 온톨로지임을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ease-crc/soma/master/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-234",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "여러 제조사·유형의 무인운반차를 통합하기 위한 제조사 독립 기술 데이터 AAS 서브모델 1.0 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-235",
      "org": "W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub)",
      "title": "ssn/integrated/ssn-system.ttl (SSN System Capabilities module)",
      "published": null,
      "url": "https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "SSN 온톨로지의 System Capabilities 모듈 파일. 시스템 능력·운용 범위·생존 범위·조건과 관계를 정의한다. 작업반 저장소 편집본이라 /TR 권고안과 문구가 다를 수 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/w3c/sdw/gh-pages/ssn/integrated/ssn-system.ttl",
      "source_unopened": false
    },
    {
      "id": "ref-236",
      "org": "Electronics(MDPI) 게재 논문(저자 미확인)",
      "title": "Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation",
      "published": "2026-08-11",
      "url": "https://doi.org/10.3390/electronics15163562",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇·작업·장소 의미 모델과 혼합 추론으로 능력 조건과 적재 상태 도달 가능성을 판정하고 배정기 독립 출력으로 넘기는 방법을 제안한 논문(Electronics 15(16) 3562).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-237",
      "org": "Kluge-Wilkes, A. 외(RWTH Aachen WZL)",
      "title": "Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems",
      "published": null,
      "url": "https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이종 조립 자원의 능력을 OWL 온톨로지(CAPILANO)로 기술하고 SPARQL 질의와 가용성 기반 작업 배정을 결합한 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-238",
      "org": "Vieira da Silva, L. M., Köcher, A. 외",
      "title": "On the Use of Large Language Models to Generate Capability Ontologies",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.17524",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 능력 온톨로지를 생성하고 RDF 구문 검사·OWL 추론·SHACL 로 품질을 반자동 검사한 연구(IEEE ETFA 2024).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. URDF 로봇 기술을 LLM 으로 해석해 로봇 온톨로지를 채우고 다수결·스키마 검증으로 신뢰성을 높이는 파이프라인(ICSR 2026).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-240",
      "org": "ISO",
      "title": "ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules",
      "published": "2024",
      "url": "https://www.iso.org/standard/82334.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 모듈의 상호운용·재사용·조립을 위한 공통 정보 모델의 구조와 속성 의미를 정한 국제표준의 ISO 소개 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈의 정보 모델을 다루는 국내 KS 표준의 KSSN 상세 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-152",
      "org": "Meseguer Valenzuela, A., & Blanes Noguera, F.",
      "title": "Task Allocation in Mobile Robot Fleets: A review",
      "published": "2025-01",
      "url": "https://arxiv.org/abs/2501.08726",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 의료·물류 등 이동로봇 플릿의 작업 배정 문제와 AI 기반 방법을 포함한 최적화 알고리즘을 검토한 리뷰 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-025",
      "org": "IEEE",
      "title": "1872-2015 - IEEE Standard Ontologies for Robotics and Automation",
      "published": "2015",
      "url": "https://ieeexplore.ieee.org/document/7084073/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇·자동화 분야 핵심 온톨로지(CORA)를 정한 IEEE 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-026",
      "org": "IEEE",
      "title": "IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology",
      "published": "2022",
      "url": "https://standards.ieee.org/standard/1872_2-2021.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 분야 온톨로지(AuR)를 정한 IEEE 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-027",
      "org": "Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G.",
      "title": "KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents",
      "published": "2018",
      "url": "https://ai.uni-bremen.de/papers/beetz18knowrob.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 인지 기반 로봇 에이전트를 위한 2세대 지식 처리 프레임워크 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-028",
      "org": "Beßler, D. 외",
      "title": "Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents",
      "published": "2021",
      "url": "https://arxiv.org/pdf/2011.11972",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 에이전트의 활동 온톨로지 SOMA 의 기초를 제시한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-029",
      "org": "McDermott, D. 외",
      "title": "PDDL - The Planning Domain Definition Language",
      "published": "1998",
      "url": "https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 행동을 파라미터·전제조건·효과로 기술하는 계획 도메인 정의 언어 문서.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-035",
      "org": "Plattform Industrie 4.0",
      "title": "Information Model for Capabilities, Skills & Services",
      "published": "2022-11",
      "url": "https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 능력·스킬·서비스(CSS) 정보 모델을 제안한 Plattform Industrie 4.0 토론 문서.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-038",
      "org": "Vieira da Silva, L. M., Köcher, A., & Fay, A.",
      "title": "A Capability and Skill Model for Heterogeneous Autonomous Robots",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.10900",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이종 자율 로봇을 위한 능력·스킬 모델을 제안한 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-040",
      "org": "Open Robotics",
      "title": "PerformAction Tutorial - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정에 사용자 정의 동작을 선언하고 작업 요청으로 호출한 뒤 execution.finished() 로 완료를 알리는 방법을 설명하는 공식 튜토리얼(mdBook 원본).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets_action_tutorial.md",
      "source_unopened": false
    },
    {
      "id": "ref-041",
      "org": "Naqvi, M. R. 외(Scientific Reports)",
      "title": "Ontology-driven integration of advertised and operational capabilities in robots",
      "published": "2025-10-02",
      "url": "https://www.nature.com/articles/s41598-025-16649-3",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇의 광고 능력과 운용 능력을 온톨로지로 통합하는 방법을 제시한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-042",
      "org": "Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R.",
      "title": "A survey of ontology-enabled processes for dependable robot autonomy",
      "published": "2024-07",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 신뢰성을 위한 온톨로지 활용 프로세스 서베이.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-043",
      "org": "신민종, 한영석, 정재윤",
      "title": "자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자산관리셸 표준으로 자율이동로봇 모니터링 시스템을 설계한 국내 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 템플릿 설정 파일. 작업 능력(task_capabilities), 사용자 정의 동작, 작업 종료 후 동작, 배터리·충전 항목을 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/fleet_adapter_template/main/fleet_adapter_template/config.yaml",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "섹션 3: f29·f6·f19(화물 취급 가능 여부는 여러 규격 필드를 함께 대조해야 하고, 제조사 선언과 운용 능력이 다를 수 있음) / 섹션 4: f10(능력·스킬 구분, 트랙 반영 제안 CSS), f18(전제조건·효과, 트랙 반영 제안 PDDL), f19(광고 능력·운용 능력, 트랙 반영 제안 RCO), f9(속성 제약·전이 제약), f13(운용 범위·생존 범위) / 섹션 5: 적치 단계 — 작업 대상 f6, 제약 f2·f23, 수행 자원 f29(팔레트 유형·중량·처리 높이 대조), 완료·인계 f8·f30 / 섹션 6: f23·f24(온톨로지 기반 실행 가능성 추론·배정), f30(능력–실행 연결 두 방식), f25·f26·f31(문서·URDF 에서 LLM 으로 능력 온톨로지 생성과 형식 검증 — 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결), f4 / 섹션 7: f1·f2·f3(VDA 5050 팩트시트), f5(MassRobotics), f7·f8(Open-RMF), f9·f12(IDTA 02020·02047, 트랙 반영 제안의 IDTA 02020 [추정]을 IDTA 원문 근거로 대체), f11(CaSkMan), f13(SSN System Capabilities, 트랙 반영 제안 f6·f7), f15·f16(IEEE 1872 계열), f27·f28(ISO 22166-201, KS B 7321-2) / 섹션 8: f14(SOMA), f17(KnowRob 2.0), f19(RCO), f20(서베이), f21(이종 자율 로봇 능력·스킬 모델), f22(국내 KCI, 게재 사실만), f23·f24·f25·f26 / 섹션 9: f32(연계 대상: 능력의 실제 구현·성능은 제조사, ROP는 선언 수집·대조·차이 기록) / 섹션 10: 13. 작업 배정 — MRTA(f23·f24·f33), 9. 로봇·제조사 관제 연동(f1·f3·f7·f8), 7. 화물·재고·자산 식별과 추적(f2·f6), 8. 실시간 세계 상태·데이터 일관성(f5 상태 보고·f19 운용 능력), 21. 온보딩·설정·현장 시운전(f25·f26 매뉴얼 해석), 27. AI·학습·적응과 모델 운영(f25·f26·f31), 28. 표준·상호운용성·다사업자 거버넌스(f12·f27·f28), 12. 명령·작업 실행의 신뢰성(f8·f30) / 섹션 11: 기존 oq-004 연결(f27·f28 부분 근거), open_questions_new 2건. 트랙 반영 제안 3건(2026-09-25-02, 4·7·8절)은 이번 실행에서 재확인·보강해 반영 대상으로 넣음. 다음 실행 후보: 13. 작업 배정 — MRTA 페이지 6·8절에 f23·f24 반영"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "스킬",
      "term_en": "Skill",
      "definition": "구현과 무관하게 명세한 능력(capability)을 실제로 실행하는 캡슐화된 구현으로, OPC UA 같은 호출 인터페이스와 상태 기계를 가진다."
    },
    {
      "term_ko": "팩트시트",
      "term_en": "Factsheet (VDA 5050)",
      "definition": "VDA 5050에서 이동로봇이 유형 명세·물리 파라미터·지원 동작·적재 명세를 관제에 미리 알리는 메시지이다."
    },
    {
      "term_ko": "자산관리셸",
      "term_en": "Asset Administration Shell (AAS)",
      "definition": "산업 자산의 정보를 서브모델 단위로 표준화해 디지털로 표현·교환하게 하는 인더스트리 4.0의 디지털 표현 구조이다."
    },
    {
      "term_ko": "형상 제약 언어",
      "term_en": "Shapes Constraint Language (SHACL)",
      "definition": "RDF 그래프가 정해진 구조·값 조건을 지키는지 검증하는 W3C 제약 언어로, 생성된 온톨로지의 품질 검사에 쓰인다."
    }
  ],
  "open_questions_new": [
    "VDA 5050 팩트시트의 loadType 과 MassRobotics 의 cargoType 이 자유 문자열일 때 팔레트·용기 같은 적재물 유형을 제조사 사이에 같은 의미로 맞출 공통 어휘나 코드 체계가 있는가? | 관련 영역: 5. 로봇 능력·작업 온톨로지, 7. 화물·재고·자산 식별과 추적 | 근거: f6 | 종류: 일반",
    "제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가? | 관련 영역: 5. 로봇 능력·작업 온톨로지, 8. 실시간 세계 상태·데이터 일관성, 13. 작업 배정 — MRTA | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 27,
    "cross_checked_count": 1,
    "unverified": [
      "f10 외 모든 finding 교차 확인 실패: 규격·연구마다 발행 주체 한 곳의 자료만 확인",
      "f10 의 두 출처(IDTA 02020, CaSkMan)는 발행 주체가 다르나 같은 CSS 계열 연구진이 관여해 독립성이 약할 수 있음",
      "ref-236 저자 미확인, ref-237 발행 연도 미확인(2022~2023 추정이라 null)",
      "ref-138 KS B 7321-2 제정일·ISO 22166 부합 여부·제1부 존재 여부 미확인",
      "f12 IDTA 02047 의 세부 필드(적재량·치수·속도)는 README 범위에서 미확인",
      "f13 SSN 은 작업반 저장소 편집본(ttl)이며 /TR 권고안(ref-030)과 글자 단위 일치 미확인",
      "f16~f22 는 기존 참고문헌의 제목 수준 재인용이며 원문 미열람",
      "물류 로봇 매뉴얼에서 능력 모델을 LLM 으로 추출한 공개 사례는 찾지 못함(f31)",
      "OPC UA Robotics(ref-034)·KnowRob 저장소는 이번에 열지 않음"
    ],
    "scope_violations": [
      "f32: 파지·센서 인식·로컬 회피 능력의 실제 구현은 분류 원문 9장 '로봇 자체 지능·제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함",
      "f24: 제조 조립 시스템 대상 연구이므로 물류 적용 사례처럼 서술하지 않도록 방법 참고로만 제안"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 15
    },
    "limits": "fetch_mode mirror_only(web_fetch_available: false). raw.githubusercontent.com 공식 원문 8건(ref-228 VDA 5050 factsheet.schema, ref-229 IDTA 02020 README, ref-230 MassRobotics JSON, ref-231 CaSkMan README, ref-232 HSU IEEE 1872.2 OWL README, ref-233 SOMA README, ref-234 IDTA 02047 README, ref-235 SSN ssn-system.ttl)과 재사용 2건(ref-040, ref-105)은 원문을 열었다. 논문·ISO·KSSN 과 재사용 논문·표준 10건은 원문 미열람이라 신뢰도 상한 medium. 검색 19회/30, 신규 출처 15건/15(ref-228~ref-152, next_ref_id 기준)로 신규 출처 상한에 도달했다. 재사용 12건. 주의: 이전 트랙 실행 2026-09-25-06 이 VDA 5050 팩트시트·IDTA 02020·MassRobotics·CaSkMan 등을 ref-044~ref-056 으로 제안했으나 참고문헌 목록의 해당 id 는 다른 출처(GS1·VDA state.schema 등)이므로 이번에 새 id 로 부여했다. 퍼블리셔가 중복 여부를 확인해야 한다. 트랙 반영 제안 3건은 모두 다루었다. IDTA 02020 은 IDTA 원문(f9)으로 근거를 대체했고 SSN 은 System Capabilities 모듈 파일로 확인했다(f13). CORA·1872.2·KnowRob·RCO·서베이·KCI 는 기존 출처를 제목 수준으로 재인용했다. 한국 자료: KS B 7321-2(표제만), 기존 KCI 1건. oq-004 는 IEEE 1872 계열·AAS 능력 서브모델의 KS 부합 여부를 확인하지 못해 해결로 제안하지 않았다(국내 모듈 정보 모델 KS 존재만 부분 근거). 27. AI·학습·적응과 모델 운영 관련 finding(f25·f26·f31)은 교차 규칙에 따라 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 연결하도록 제안했다. 8. 실시간 세계 상태·데이터 일관성은 상태 보고·운용 능력 연결로만 다루었고 22. 시뮬레이션·예측용 디지털 트윈과 섞지 않았다. 검색 결과로 확인하지 못한 국내 ETRI·한국로봇산업진흥원 자료와 벤더 관제 규격(CRCS 등)은 출처로 넣지 않았다."
  }
}
```

### runs/2026-09-25-15/verification.json

```json
{
  "run_id": "2026-09-25-15",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: factsheet.schema 원문(raw.githubusercontent.com)을 검증자가 직접 열었다. 필수 블록 11개(headerId·timestamp·version·manufacturer·serialNumber·typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification)와 두 설명 문구가 일치한다. 규격 원문 단일 출처이며 발행일은 미확인(확인일 기준)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: loadSets 의 loadType('EPAL, XLT1200' 예시), maximumWeight, 최소·최대 적재 처리 높이, pickTime·dropTime(대략 소요 시간, 초)이 원문과 일치한다. 페이지에서는 pickTime·dropTime 을 '대략의 소요 시간'으로 적는 것이 원문에 더 가깝다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: actionType·actionDescription(자유 문장)·actionScopes(INSTANT·NODE·EDGE·ZONE)·actionParameters(key·valueDataType·isOptional, 선택 필드 description)·pauseAllowed·cancelAllowed 가 원문과 일치한다. valueDataType 6개 값도 일치한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 원문에서 actionParameters 에 값 범위·전제조건 필드가 없음을 검증자도 확인했다. '흩어져 기술될 것'은 추론이므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AMR_Interop_Standard.json 원문에 maxSpeed·maxRunTime·chargerType·cargoType('Discription of cargo')·cargoMaxVolume·cargoMaxWeight·productDocumentation, operationalState 9개 값, loadPercentageStillAvailable(0~100)이 있다. 발행일 미확인."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 원문에서 loadType 은 예시만, cargoType 은 설명 한 줄만 있고 어휘를 지정하지 않는다. 공통 어휘가 별도로 있는지는 확인하지 않은 추론이므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: config.yaml 원문의 task_capabilities 주석, loop·delivery 활성화, actions(자리표시 예시), finishing_request(park·charge·nothing)가 일치한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 data/source_texts/ref-040.txt 원문에 actions: [\"clean\"], category·description 호출, is_command_completed() 확인 뒤 execution.finished() 호출이 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IDTA 02020 README 를 검증자가 raw 경로로 열어 구현 독립 기능 명세, 속성 예(최대 속도·허용 오차·온도 범위), 속성 제약(전제·불변·사후조건), 전이 제약(순서·병렬), 스킬, 'reliable comparison between required and provided capabilities', 1.0 첫 공식판을 확인했다. 브리프는 ref-229 을 fetched false 로 적었지만 근거 발췌는 'README 원문'이라 서로 맞지 않는다. 검증자는 신뢰도를 올리지 않으므로 medium 을 유지한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IDTA README(구현 독립 명세, 스킬은 능력의 구현)와 CaSkMan README(스킬 = OPC UA 등 호출 인터페이스를 가진 캡슐화된 구현, CSS 참조 모델 기반)는 핵심 구분을 뒷받침한다. 다만 IDTA README 에서 CSS 계열이라는 문구는 확인하지 못했고, ref-035 는 원문 미열람이다. 두 저장소 모두 헬무트 슈미트 대학(HSU) 연구진이 관여해 독립성이 약하므로 cross_checked 는 false 로 둔다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CaSkMan README 원문에 VDI 3682(공정 입출력), VDI 2860(취급 작업), DIN 8580(제조 공정), ISA 88(상태 기계), IEC 61360(속성 형식 기술), WADL·OPC UA 가 있다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IDTA 02047 README 를 검증자가 열어 목적 문구, 1.0 첫 공식판, AAS 메타모델 3.0 호환을 확인했다. 세부 필드는 README 에 없다(브리프 기록과 같음). 브리프는 fetched false 로 적었으므로 medium 을 유지한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ssn-system.ttl 원문에 SystemCapability·OperatingRange·SurvivalRange·Condition·hasSystemCapability·inCondition 이 정의돼 있다. 발췌 인용은 원문('If, however, the SurvivalRange is violated, the System is \"damaged\" and SystemCapability specifications may no longer hold.')에서 'however'와 따옴표가 빠져 글자 단위로 다르다. 작업반 편집본이며 /TR 권고안(ref-030, 2017-10-19)과의 일치는 미확인."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: SOMA README 원문에 활동 온톨로지, DUL 기반 OWL 구현, 의도·계획·움직임·접촉이 있다. ref-028 논문은 원문 미열람이며 서지만 재인용했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 문구 수정 필요: README 는 기능(function)·기능 실행·상호작용·환경을 기술하고 '두 상위 온톨로지 DUL 과 SUMO 가 쓰인다'고 하지만, SUMO 는 OWL 표현이 없어 이 구현과 매핑에서 제외했다고 밝힌다. 따라서 'DUL·SUMO 로 확장하는 구현'은 부정확하다. 대상 표준도 IEEE 1872 가 아니라 IEEE 1872.2 다. IEEE 공식 산출물이라는 표시는 없다(제3자 구현)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(제목 수준): ref-025 는 참고문헌 목록에 있는 기존 출처이고 용어집 CORA 항목과 같은 근거다. 원문 미열람, 이번에는 다시 검색하지 않았다. 발행 2015 로 2년이 넘었으므로 월간 재검증 대상이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(서지 수준): ref-027 은 기존 참고문헌이며 제목과 주장이 일치한다. 원문 미열람(재인용)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(서지 수준): ref-029 는 기존 참고문헌이며 용어집 PDDL 정의와 같다. 원문 미열람(재인용)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검색 결과(Nature·PMC)에서 Scientific Reports 15권 34326, 저자 Naqvi·Sarkar·Ameri·Elmhadhbi·Louge·Karray, RCO 가 제조사가 명시한 광고 능력(advertised)과 실제 성능을 반영한 운용 능력(operational)을 정의한다는 점을 확인했다. 원문 미열람."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(제목 수준): ref-042 는 기존 참고문헌이다. 원문 미열람(재인용), 이번에는 다시 검색하지 않았다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(제목 수준): ref-038 은 기존 참고문헌(arXiv 2209.10900)이다. 원문 미열람(재인용)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(서지 수준): ref-043 은 기존 참고문헌(KCI)이며 게재 사실만 뒷받침한다. 능력 기술 포함 여부는 미확인이라고 페이지에 적어야 한다. 원문 미열람."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검색 결과에서 Electronics 15(16) 3562(2026-08-11), 로봇·작업·장소 의미 모델, 선언적 추론과 절차적 평가의 혼합, 다축 능력 조건과 적재 상태 장소 도달 가능성, 공통 입력 ReasonerOutput, 할당기 4종 실험을 확인했다. 저자 미확인, 원문 미열람."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검색 결과에서 CAPILANO(Protégé OWL), SPARQL 질의, 가용성을 고려한 연속 작업 배정(Python), 라인리스 이동 조립 시스템(LMAS) 적용, 2022년 MHI Colloquium·WGMHI 연보 게재를 확인했다. 브리프의 ref-237 published null 은 2022 로 고칠 수 있다. 제조 조립 대상이며 물류 사례가 아니다. 원문 미열람."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2404.17524 검색 결과에서 저자 Vieira da Silva·Köcher·Gehlhoff·Fay, ETFA 2024, RDF 구문 검사·OWL 추론·SHACL 기반 반자동 품질 검사, 'almost free of errors'를 확인했다. 저자 보고 결과이며 원문 미열람."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2606.17073 검색 결과에서 Dussard·Sarthou(LAAS-CNRS), URDF 에서 LLM 으로 온톨로지 채우기, 여러 질의의 다수결과 구문·스키마 수준 검증, ICSR 2026(2026-07, 런던) 채택을 확인했다. 원문 미열람."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ISO 소개 요약에서 모듈 공통 정보 모델(CIM)의 구조와 속성·하위 클래스의 쓰임과 의미, 상호운용성·재사용성·조립 가능성을 확인했다. 발행 2024-02(1판), 원문 미열람. Part 202:2025 는 소프트웨어 모듈 정보 모델이다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: KSSN 검색 결과의 표제가 일치한다. 제정일과 ISO 22166-202 부합 여부는 미확인이다. 국내가 ISO 에 먼저 제안했다는 기사가 있으나 브리프 밖 내용이라 페이지에 쓰지 않는다. 원문 미열람."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f2·f3·f5·f23 의 확인된 내용에서 도출한 추론이므로 [추정]을 유지한다. 분류 원문 SCM 관점 질문에 대응한다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f3·f8(이름 기반 선언·호출)과 f9·f11(능력–스킬–상태 기계)에서 도출한 추론이므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f25·f26 두 연구 모두 생성 뒤 형식 검증을 둔다는 점은 검색 결과로 확인했다. 물류 매뉴얼 사례는 없으므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '연계 대상:'으로 표시돼 있고 분류 원문 9장의 로봇 자체 지능·제어 경계와 맞는다. 추론이므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 문구 수정 필요: arXiv 2501.08726 검색 결과에서 저자, 에너지 소비와 필요 로봇 수 최소화, AI 기반 방법을 포함한 최적화 알고리즘 검토를 확인했다. 그러나 '의료·물류 등에서 쓰이는'은 검색 결과와 브리프 발췌 어디에도 없다. 원문 미열람."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "용어집 VDA 5050 항목(현행판 3.0.0)과 f1~f3 의 3.0.0 판 기술이 일치한다. 새 각주 ref-228(factsheet.schema)는 기존 ref-031(명세)·ref-051(state.schema)·ref-052(README)와 URL 이 달라 중복이 아니다.",
      "용어집 CSS·CORA·PDDL·플릿 어댑터 항목이 f10·f16·f18·f7 과 같은 내용이다. 용어는 새로 등록하지 않고 기존 용어 페이지로 연결한다.",
      "이전 트랙 실행 2026-09-25-06 이 제안한 ref-044~ref-056(팩트시트·IDTA 02020 등)은 게시된 참고문헌의 같은 id 와 출처가 다르다. 이번의 새 id ref-228~ref-152 와 URL 이 겹치는지는 퍼블리셔가 확인한다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "용어집 '능력·스킬·서비스 모델(CSS)' 항목은 이 위키의 온톨로지 초안이 CSS 의 capability 를 '기능(Capability)'으로 부른다고 적는다. 영역 페이지와 용어 후보 '스킬'은 '능력'을 쓰므로 첫 등장 때 둘의 대응을 밝혀야 한다.",
      "용어 후보 '스킬' 정의의 '상태 기계를 가진다'는 CaSkMan(f11)의 설계이지 IDTA 02020(f9)의 일반 정의가 아니다."
    ]
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "f13 발췌 인용이 원문 rdfs:comment('If, however, the SurvivalRange is violated, the System is \"damaged\" and SystemCapability specifications may no longer hold.')와 글자 단위로 다르다('however'와 따옴표 누락)."
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f15: 문장을 'IEEE 1872.2 AuR 온톨로지(표준은 상위 온톨로지 DUL·SUMO 를 씀)의 OWL 구현으로, SUMO 는 OWL 표현이 없어 제외하고 DUL 만 포함한 제3자 구현'으로 고친다 — ref-232 README 는 SUMO 를 이 구현과 매핑에서 제외했다고 밝히고, 대상 표준은 IEEE 1872 가 아니라 1872.2 다.",
    "f10: 'IDTA 02020 이 CSS 계열'이라는 부분은 [사실] 문장에서 빼고, CSS 참조 모델 기반은 CaSkMan(ref-231)에 대해서만 [사실]로 쓴다. IDTA 02020 과 CSS 의 관계를 쓰려면 ref-035 를 근거로 [추정]을 붙인다 — IDTA README 에서 CSS 언급을 확인하지 못했다.",
    "f33: '의료·물류 등에서 쓰이는'을 지우고 '이동로봇 플릿의 작업 배정 문제'로 쓴다 — 검색 결과와 브리프 발췌 어디에도 적용 분야 서술이 없다.",
    "f13: 페이지에서 원문을 직접 인용하려면 ref-235 원문 문구를 글자 그대로 쓰고(출처당 1회), 아니면 재서술한다 — 브리프 발췌는 'however'와 따옴표가 빠져 원문과 다르다.",
    "ref-237: 참고문헌 등록(reference_updates)과 각주의 발행일을 '미확인'이 아니라 2022 로 쓴다 — 검색 결과에서 2022년 MHI Colloquium·WGMHI 연보 게재를 확인했다.",
    "ref-240: 발행일을 2024-02 로 쓴다 — ISO 소개 정보에서 2024-02 발행 1판을 확인했다.",
    "ref-238: 기관(저자) 표기를 'Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.'로 쓴다 — 검색 결과의 저자 목록.",
    "각주·참고문헌 원문 미열람 표기: 브리프에서 fetched false 인 모든 출처(ref-229, ref-234, ref-236~ref-152, ref-025~ref-029, ref-035, ref-038, ref-041~ref-043)의 각주 정의에는 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 에는 source_unopened: true 를 넣는다. fetched true 인 출처(ref-228, ref-230~ref-233, ref-235, ref-040, ref-105)에는 붙이지 않는다.",
    "f16~f22·f28 은 제목·서지 수준의 재인용이다. 본문에서 이 출처들이 무엇을 '보였다'거나 '제안한다'고 세부를 풀어 쓰지 말고, 브리프 주장 범위(존재·제목·게재 사실)로만 쓴다. f22 는 '능력 기술 포함 여부 미확인'을 함께 적는다.",
    "f24: 5절 현장 시나리오에 넣지 말고 6·8절에서 '제조 조립(라인리스 이동 조립 시스템) 대상 연구'임을 밝혀 방법 참고로만 쓴다 — 물류 사례가 아니다.",
    "f25·f26·f31(문서·URDF 에서 LLM 으로 능력 온톨로지 생성): 교차 규칙에 따라 10절에 27. AI·학습·적응과 모델 운영, 21. 온보딩·설정·현장 시운전과 양쪽으로 연결한다. f25 의 '오류가 거의 없었다'는 저자 보고임을 밝힌다.",
    "f5·f19(상태 보고·운용 능력)를 8. 실시간 세계 상태·데이터 일관성에 연결할 때는 현재 상태 표현으로만 쓰고 22. 시뮬레이션·예측용 디지털 트윈과 섞지 않는다.",
    "용어: 4절에서 '능력(capability)'이 첫 등장할 때 용어집 CSS 항목의 표기(온톨로지 초안의 '기능(Capability)')와 같은 뜻임을 밝힌다. 용어 후보 '스킬' 정의의 '상태 기계를 가진다'는 '상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계)'로 고친다.",
    "oq-004 는 해결로 바꾸지 않는다 — f27·f28 은 국내 모듈 정보 모델 KS 가 있다는 부분 근거일 뿐이고, IEEE 1872 계열이나 AAS 능력 서브모델을 KS 로 부합화한 사실은 확인되지 않았다. 11절에서 oq-004 에 연결하고 f27·f28 을 부분 근거로 적는다.",
    "트랙 반영 제안 3건(2026-09-25-02; 4·7·8절)은 이번 브리프의 finding(f9·f10·f13·f15~f22)으로 반영하되, 7절의 IDTA 02020 은 제3자 논문 경유 [추정]이 아니라 f9(IDTA 저장소 README, 원문 미열람 표기)를 근거로 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only, raw.githubusercontent.com 만 열람 가능)에서 검증됐다. 확인 33건, 미확인 0건, 교차 확인 0건. 강등: 없음(f15·f33 은 문구 수정, f10 은 CSS 계열 부분 한정). 원문 미열람 출처: ref-025, ref-026, ref-027, ref-028, ref-029, ref-035, ref-038, ref-041, ref-042, ref-043, ref-229, ref-234, ref-236, ref-237, ref-238, ref-239, ref-240, ref-138, ref-152. 검증자는 ref-229·ref-234 README 를 raw 경로로 열어 내용이 일치함을 확인했지만, 브리프의 fetched false 기록에 따라 신뢰도를 올리지 않았다. 주의: VDA 5050 팩트시트·MassRobotics·Open-RMF·IDTA·CaSkMan·SSN 은 규격 원문마다 한 발행 주체의 근거이고, 여러 규격을 함께 대조해야 화물 취급 가능 여부가 정해진다는 판단(f29)과 능력–실행 연결 두 방식(f30)은 추론이다. f16~f22·f28 은 제목 수준 재인용이며, 물류 로봇 매뉴얼에서 능력 모델을 LLM 으로 만든 공개 사례는 확인하지 못했다. oq-004 는 해결 불인정(국내 모듈 정보 모델 KS 존재만 부분 근거). 정정 요청 없음. 검색은 리서치 19회와 검증 9회를 합쳐 28회/30이다.",
  "retry_reason": null
}
```

### runs/2026-09-25-15/pages.json

```json
{
  "run_id": "2026-09-25-15",
  "outline": [
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 500,
      "summary": "같은 운반 로봇 가운데 누가 화물을 취급할 수 있는지는 여러 규격 필드와 현재 상태를 함께 대조해야 판단할 수 있을 것으로 보인다. [추정][^ref-228][^ref-230][^ref-236]",
      "planned_findings": [
        "f29",
        "f6",
        "f19"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "핵심 개념은 구현과 무관한 기능 명세인 능력과 그 실행 구현인 스킬의 구분이며, 능력의 조건을 적는 제약·범위 개념이 더해진다. [사실][^ref-229][^ref-231]",
      "planned_findings": [
        "f10",
        "f9",
        "f18",
        "f13",
        "f19",
        "f1"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 800,
      "summary": "적치 단계에서 제조사가 다른 운반 로봇 가운데 팔레트를 취급할 로봇을 고르는 가상 시나리오로, 적재 명세·도달 가능성·완료 보고·선언과 운용 능력의 차이를 보여 준다. [사실][^ref-228]",
      "planned_findings": [
        "f6",
        "f29",
        "f2",
        "f23",
        "f8",
        "f30",
        "f19"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 900,
      "summary": "능력과 실행의 연결은 이름 기반 선언 방식과 능력–스킬 모델 방식으로 나뉘는 것으로 보이며, 의미 모델로 실행 가능성을 판정하거나 LLM으로 능력 온톨로지를 만든 뒤 형식 검증하는 접근이 있다. [추정][^ref-228][^ref-040][^ref-229][^ref-231]",
      "planned_findings": [
        "f30",
        "f3",
        "f8",
        "f4",
        "f9",
        "f11",
        "f23",
        "f24",
        "f25",
        "f26",
        "f31"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "물류 이동로봇 인터페이스(VDA 5050 팩트시트, MassRobotics, Open-RMF)와 능력 모델 표준·온톨로지(IDTA 02020, CaSkMan, SSN, IEEE 1872 계열, ISO 22166-201, KS B 7321-2)가 이 영역의 기반이다. [사실][^ref-228]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f7",
        "f8",
        "f9",
        "f12",
        "f11",
        "f13",
        "f15",
        "f16",
        "f27",
        "f28"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "로봇 지식 처리(KnowRob 2.0, SOMA), 광고·운용 능력 통합, 온톨로지 기반 배정과 LLM 기반 능력 온톨로지 생성 연구가 대표 자료다. [사실][^ref-233]",
      "planned_findings": [
        "f14",
        "f17",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f33"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 450,
      "summary": "능력의 실제 구현·성능은 로봇 자체 지능·제어에 맡기고, ROP는 제조사 선언을 공통 모델로 모아 작업 요구와 대조하고 선언과 실제의 차이를 기록하는 쪽을 맡는 것으로 보인다. [추정][^ref-228][^ref-229][^ref-041]",
      "planned_findings": [
        "f32"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 750,
      "summary": "7. 화물·재고·자산 식별과 추적, 8. 실시간 세계 상태·데이터 일관성, 9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성, 13. 작업 배정 — MRTA, 21. 온보딩·설정·현장 시운전, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스와 이어진다.",
      "planned_findings": [
        "f6",
        "f5",
        "f19",
        "f1",
        "f7",
        "f30",
        "f23",
        "f33",
        "f25",
        "f26",
        "f31",
        "f12",
        "f27",
        "f28"
      ]
    },
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "section": "11. 열린 질문",
      "budget_chars": 450,
      "summary": "국내 표준 부합화(oq-004), 적재물 유형 공통 어휘, 선언 능력과 운용 능력 중 배정 기준값이 열린 질문이다.",
      "planned_findings": [
        "f27",
        "f28",
        "f6",
        "f19"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 트랙 반영 제안 3건(4·7·8절) 반영. 2차 수정: 10절 태그 2건 조정·ref-152 문장 분리, 3·9절 의견 주체 명시"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area05-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 5. 로봇 능력·작업 온톨로지 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,658자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area05-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 5. 로봇 능력·작업 온톨로지 의 \"6. 대표 접근법과 기술\" 절(1,396자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area05-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 5. 로봇 능력·작업 온톨로지 의 \"4. 핵심 개념과 용어\" 절(1,115자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area05-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 5. 로봇 능력·작업 온톨로지 의 \"8. 대표 연구와 자료\" 절(1,010자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 5. 로봇 능력·작업 온톨로지 | 영역 심화: 3~11절 신규 작성(능력·스킬 구분, VDA 5050 팩트시트·MassRobotics·Open-RMF 능력 선언, IDTA 02020·CaSkMan·SSN·IEEE 1872 계열·ISO 22166-201·KS B 7321-2, 적치 시나리오, 열린 질문 2건 신규·oq-004 연결), 트랙 반영 제안 3건 반영 | run 2026-09-25-15",
  "index_updates": {
    "home_recent": "2026-09-25 — 5. 로봇 능력·작업 온톨로지: 영역 심화 초안 작성(능력·스킬 구분, 제조사 능력 선언 규격 비교, 적치 시나리오, 열린 질문 2건 추가)",
    "category_recent": "2026-09-25 — 5. 로봇 능력·작업 온톨로지: 3~11절 신규 작성, VDA 5050 팩트시트·MassRobotics·IDTA 02020 등 능력 표현 표준 정리",
    "area_recent": "2026-09-25 — 5. 로봇 능력·작업 온톨로지: 3~11절 신규 작성, 트랙 반영 제안 3건(4·7·8절) 반영, oq-004 연결"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "skill",
      "term_ko": "스킬",
      "term_en": "Skill",
      "definition": "구현과 무관하게 명세한 능력(capability)을 실제로 실행하는 캡슐화된 구현으로, OPC UA 같은 호출 인터페이스를 가지며 상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계).",
      "description": "IDTA 02020 능력 서브모델과 CaSkMan 온톨로지가 능력과 스킬을 구분해 쓴다. 이 위키의 온톨로지 초안이 '기능(Capability)'이라 부르는 개념이 여기의 능력에 해당한다.",
      "related_areas": [
        5,
        9,
        12
      ],
      "sources": [
        "ref-229",
        "ref-231"
      ]
    },
    {
      "action": "new",
      "slug": "vda-5050-factsheet",
      "term_ko": "팩트시트",
      "term_en": "Factsheet (VDA 5050)",
      "definition": "VDA 5050에서 이동로봇이 유형 명세·물리 파라미터·지원 동작·적재 명세를 관제에 미리 알리는 메시지이다.",
      "description": "3.0.0판 스키마는 typeSpecification, physicalParameters, protocolLimits, protocolFeatures, mobileRobotGeometry, loadSpecification 을 필수 블록으로 둔다(확인일 2026-09-25).",
      "related_areas": [
        5,
        9
      ],
      "sources": [
        "ref-228"
      ]
    },
    {
      "action": "new",
      "slug": "asset-administration-shell",
      "term_ko": "자산관리셸",
      "term_en": "Asset Administration Shell (AAS)",
      "definition": "산업 자산의 정보를 서브모델 단위로 표준화해 디지털로 표현·교환하게 하는 인더스트리 4.0의 디지털 표현 구조이다.",
      "description": "IDTA 02020(능력 기술), IDTA 02047(무인운반차 기술 데이터) 같은 서브모델 템플릿이 있다.",
      "related_areas": [
        5,
        28
      ],
      "sources": [
        "ref-229",
        "ref-234"
      ]
    },
    {
      "action": "new",
      "slug": "shacl",
      "term_ko": "형상 제약 언어",
      "term_en": "Shapes Constraint Language (SHACL)",
      "definition": "RDF 그래프가 정해진 구조·값 조건을 지키는지 검증하는 W3C 제약 언어로, 생성된 온톨로지의 품질 검사에 쓰인다.",
      "related_areas": [
        5,
        27
      ],
      "sources": [
        "ref-238"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 공식 저장소 main(3.0.0판)의 팩트시트 JSON 스키마. 유형 명세·물리 파라미터·지원 동작·적재 명세 블록의 필드를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-229",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IDTA 공식 서브모델 템플릿 저장소의 능력 기술 서브모델 1.0 안내. 능력 정의, 속성, 속성 제약·전이 제약, 스킬과의 관계, 요구·제공 능력 비교 목적을 설명한다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 식별 보고(최대 속도·화물 최대 중량·부피 등)와 상태 보고(운영 상태·남은 적재 용량) 필드를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-231",
      "org": "CaSkade-Automation (GitHub)",
      "title": "CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README)",
      "published": null,
      "url": "https://github.com/CaSkade-Automation/CaSkMan",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "제조 설비의 능력·스킬·스킬 인터페이스·속성을 기술하는 OWL 정렬 온톨로지 저장소 README. VDI 3682·VDI 2860·DIN 8580·ISA 88·IEC 61360 과 CSS 참조 모델을 잇는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-232",
      "org": "Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub)",
      "title": "IndustrialStandard-ODP-IEEE1872-2 — README (IEEE 1872.2 AuR ontology OWL implementation)",
      "published": null,
      "url": "https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "IEEE 1872.2 AuR 온톨로지를 OWL 로 구현한 제3자 저장소 README. SUMO 는 OWL 표현이 없어 제외하고 DUL 만 포함했으며, 로봇 기능과 기능 실행, 상호작용·환경 기술을 설명한다. IEEE 표준 본문은 아니다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-233",
      "org": "EASE CRC (ease-crc/soma)",
      "title": "SOMA — README (Socio-physical Model of Activities)",
      "published": null,
      "url": "https://github.com/ease-crc/soma",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "SOMA 공식 저장소 README. DUL 상위 온톨로지를 확장해 로봇 에이전트의 활동을 표현하는 OWL 온톨로지임을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-234",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 여러 제조사·유형의 무인운반차를 통합하기 위한 제조사 독립 기술 데이터 AAS 서브모델 1.0 안내.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-235",
      "org": "W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub)",
      "title": "ssn/integrated/ssn-system.ttl (SSN System Capabilities module)",
      "published": null,
      "url": "https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "SSN 온톨로지의 System Capabilities 모듈 파일. 시스템 능력·운용 범위·생존 범위·조건과 관계를 정의한다. 작업반 저장소 편집본이라 /TR 권고안과 문구가 다를 수 있다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-236",
      "org": "Electronics(MDPI) 게재 논문(저자 미확인)",
      "title": "Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation",
      "published": "2026-08-11",
      "url": "https://doi.org/10.3390/electronics15163562",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇·작업·장소 의미 모델과 혼합 추론으로 능력 조건과 적재 상태 도달 가능성을 판정하고 배정기 독립 출력으로 넘기는 방법을 제안한 논문(Electronics 15(16) 3562).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-237",
      "org": "Kluge-Wilkes, A. 외(RWTH Aachen WZL)",
      "title": "Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems",
      "published": "2022",
      "url": "https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이종 조립 자원의 능력을 OWL 온톨로지(CAPILANO)로 기술하고 SPARQL 질의와 가용성 기반 작업 배정을 결합한 연구(2022년 MHI Colloquium·WGMHI 연보 게재). 제조 조립 대상.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-238",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "On the Use of Large Language Models to Generate Capability Ontologies",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.17524",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 능력 온톨로지를 생성하고 RDF 구문 검사·OWL 추론·SHACL 로 품질을 반자동 검사한 연구(IEEE ETFA 2024).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. URDF 로봇 기술을 LLM 으로 해석해 로봇 온톨로지를 채우고 다수결·스키마 검증으로 신뢰성을 높이는 파이프라인(ICSR 2026).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-240",
      "org": "ISO",
      "title": "ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules",
      "published": "2024-02",
      "url": "https://www.iso.org/standard/82334.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 모듈의 상호운용·재사용·조립을 위한 공통 정보 모델의 구조와 속성 의미를 정한 국제표준(1판, 2024-02)의 ISO 소개 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈의 정보 모델을 다루는 국내 KS 표준의 KSSN 상세 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-152",
      "org": "Meseguer Valenzuela, A., & Blanes Noguera, F.",
      "title": "Task Allocation in Mobile Robot Fleets: A review",
      "published": "2025-01",
      "url": "https://arxiv.org/abs/2501.08726",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동로봇 플릿의 작업 배정 문제와 AI 기반 방법을 포함한 최적화 알고리즘을 검토한 리뷰 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-025",
      "org": "IEEE",
      "title": "1872-2015 - IEEE Standard Ontologies for Robotics and Automation",
      "published": "2015",
      "url": "https://ieeexplore.ieee.org/document/7084073/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇·자동화 분야 핵심 온톨로지(CORA)를 정한 IEEE 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-026",
      "org": "IEEE",
      "title": "IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology",
      "published": "2022",
      "url": "https://standards.ieee.org/standard/1872_2-2021.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 분야 온톨로지(AuR)를 정한 IEEE 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-027",
      "org": "Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G.",
      "title": "KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents",
      "published": "2018",
      "url": "https://ai.uni-bremen.de/papers/beetz18knowrob.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 인지 기반 로봇 에이전트를 위한 2세대 지식 처리 프레임워크 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-028",
      "org": "Beßler, D. 외",
      "title": "Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents",
      "published": "2021",
      "url": "https://arxiv.org/pdf/2011.11972",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 에이전트의 활동 온톨로지 SOMA 의 기초를 제시한 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-029",
      "org": "McDermott, D. 외",
      "title": "PDDL - The Planning Domain Definition Language",
      "published": "1998",
      "url": "https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 행동을 파라미터·전제조건·효과로 기술하는 계획 도메인 정의 언어 문서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-035",
      "org": "Plattform Industrie 4.0",
      "title": "Information Model for Capabilities, Skills & Services",
      "published": "2022-11",
      "url": "https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 능력·스킬·서비스(CSS) 정보 모델을 제안한 Plattform Industrie 4.0 토론 문서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-038",
      "org": "Vieira da Silva, L. M., Köcher, A., & Fay, A.",
      "title": "A Capability and Skill Model for Heterogeneous Autonomous Robots",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.10900",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이종 자율 로봇을 위한 능력·스킬 모델을 제안한 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-040",
      "org": "Open Robotics",
      "title": "PerformAction Tutorial - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "플릿 어댑터 설정에 사용자 정의 동작을 선언하고 작업 요청으로 호출한 뒤 execution.finished() 로 완료를 알리는 방법을 설명하는 공식 튜토리얼(mdBook 원본).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-041",
      "org": "Naqvi, M. R. 외(Scientific Reports)",
      "title": "Ontology-driven integration of advertised and operational capabilities in robots",
      "published": "2025-10-02",
      "url": "https://www.nature.com/articles/s41598-025-16649-3",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇의 광고 능력과 운용 능력을 온톨로지로 통합하는 방법을 제시한 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-042",
      "org": "Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R.",
      "title": "A survey of ontology-enabled processes for dependable robot autonomy",
      "published": "2024-07",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 신뢰성을 위한 온톨로지 활용 프로세스 서베이.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-043",
      "org": "신민종, 한영석, 정재윤",
      "title": "자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자산관리셸 표준으로 자율이동로봇 모니터링 시스템을 설계한 국내 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 플릿 어댑터 템플릿 설정 파일. 작업 능력(task_capabilities), 사용자 정의 동작, 작업 종료 후 동작, 배터리·충전 항목을 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "VDA 5050 팩트시트의 loadType 과 MassRobotics 의 cargoType 이 자유 문자열일 때 팔레트·용기 같은 적재물 유형을 제조사 사이에 같은 의미로 맞출 공통 어휘나 코드 체계가 있는가?",
      "areas": [
        5,
        7
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가?",
      "areas": [
        5,
        8,
        13
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "적치",
      "item": "시작 조건",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    },
    {
      "step": "적치",
      "item": "작업 대상",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    },
    {
      "step": "적치",
      "item": "수행 자원",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    },
    {
      "step": "적치",
      "item": "제약",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    },
    {
      "step": "적치",
      "item": "완료·인계",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    },
    {
      "step": "적치",
      "item": "예외·성과",
      "link": "docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "5. 로봇 능력·작업 온톨로지"
    }
  ],
  "additional_research_requests": [
    "7절: IDTA 02047 Technical Data for AGV 1.0 의 세부 필드(적재량·치수·속도 등)가 README 범위에서 미확인이라, 명세 본문을 열어 VDA 5050 팩트시트 적재 명세와 비교할 근거가 필요하다.",
    "7·11절: KS B 7321-2 의 제정일, ISO 22166-202 부합 여부, 제1부 존재 여부를 확인해야 oq-004 의 부분 근거를 보강할 수 있다.",
    "8절: ref-236(Electronics 2026) 저자 미확인 — 참고문헌 기관 표기를 채울 서지 확인이 필요하다.",
    "6절: 물류 로봇 매뉴얼에서 능력 모델을 LLM 으로 추출한 공개 사례를 찾지 못했다 — 매뉴얼 해석 적용 사례가 있으면 6절과 21. 온보딩·설정·현장 시운전 연결을 보강할 수 있다.",
    "출처 기록: ref-229·ref-234 은 1차 검증자가 raw 경로로 열어 일치를 확인했으나 브리프에 fetched false 로 기록돼 원문 미열람 표시를 유지했다. 다음 실행에서 fetched 기록을 바로잡을지 확인이 필요하다.",
    "6절: VDA 5050·Open-RMF 의 이름 기반 동작 선언과 IDTA 02020·CaSkMan 의 능력–스킬 모델을 서로 매핑한 표준·구현이 있는지 조사가 필요하다(현재 [추정]).",
    "10절: 상태 보고 값·운용 능력이 실제 배정 판단에 쓰이는 방식을 보여 주는 근거가 브리프에 없어 [추정]으로 두었다. 13. 작업 배정 — MRTA 연구에서 이를 뒷받침할 자료가 필요하다."
  ],
  "fixes_applied": [
    "f15 문구 수정 — 7절 표의 IEEE 1872.2 행을 'IEEE 1872.2 AuR 온톨로지(표준은 상위 온톨로지 DUL·SUMO를 씀)의 OWL 구현으로, SUMO는 OWL 표현이 없어 제외하고 DUL만 포함한 제3자 구현'으로 썼다.",
    "f10 CSS 계열 한정 — 4절 스킬 항목에서 능력·스킬 구분만 IDTA 02020·CaSkMan 공통 [사실]로 두고, CSS 참조 모델 기반은 CaSkMan(ref-231)에만 [사실]로, IDTA 02020 과 CSS 의 관계는 ref-035 근거 [추정]으로 썼다.",
    "f33 적용 분야 삭제 — 8절 Meseguer Valenzuela·Blanes Noguera 항목을 '이동로봇 플릿의 작업 배정 문제'로 쓰고 '의료·물류 등'을 넣지 않았다.",
    "f13 인용 — 4절 운용 범위·생존 범위 항목과 7절 SSN 행에서 원문을 직접 인용하지 않고 재서술했다.",
    "ref-237 발행일 — 각주와 reference_updates 의 발행일을 2022 로 썼다.",
    "ref-240 발행일 — 각주와 reference_updates 의 발행일을 2024-02 로 썼다.",
    "ref-238 저자 — 각주와 reference_updates 의 기관을 'Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.'로 썼다.",
    "원문 미열람 표기 — fetched false 출처(ref-025~ref-029, ref-035, ref-038, ref-041~ref-043, ref-229, ref-234, ref-236~ref-138, ref-152) 각주에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 와 '원문 미열람. ' 요약 머리를 넣었으며, fetched true 출처(ref-040, ref-105, ref-228, ref-230~ref-233, ref-235)에는 붙이지 않았다.",
    "재인용 범위 — f16~f22·f28 을 7·8절에서 존재·제목·게재 사실 범위로만 쓰고, f22(신민종 외) 항목에 '능력 기술을 포함하는지는 미확인'을 함께 적었다.",
    "f24 위치 — 5절 시나리오에 넣지 않고 6·8절에서 제조 조립(라인리스 이동 조립 시스템) 대상 연구로 밝혀 방법 참고로만 썼다.",
    "f25·f26·f31 교차 연결 — 6절에 교차 규칙을 밝히고 10절에 27. AI·학습·적응과 모델 운영과 21. 온보딩·설정·현장 시운전을 모두 연결했으며, f25 의 '오류가 거의 없었다'를 저자들의 보고로 썼다.",
    "f5·f19 연결 — 10절의 8. 실시간 세계 상태·데이터 일관성 항목을 현재 상태 표현으로만 쓰고 22. 시뮬레이션·예측용 디지털 트윈은 언급하지 않았다.",
    "용어 — 4절 능력 항목 첫 등장에서 용어집 CSS 항목·온톨로지 초안의 '기능(Capability)'과 같은 뜻임을 밝혔고, glossary_updates 의 스킬 정의를 '상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계)'로 고쳤다.",
    "oq-004 — 해결로 바꾸지 않고(open_question_updates 에 상태 변경 없음) 11절에서 열림으로 연결하며 f27·f28(ISO 22166-201, KS B 7321-2)을 부분 근거로 적었다.",
    "트랙 반영 제안 3건 — 4절(능력·스킬, 전제조건·효과, 광고·운용 능력), 7절(IEEE 1872 계열, SSN System Capabilities, IDTA 02020), 8절(KnowRob 2.0, SOMA, RCO, 서베이, 이종 자율 로봇 능력·스킬 모델, 국내 KCI)에 반영했고, 7절 IDTA 02020 은 제3자 논문 경유 [추정]이 아니라 f9(ref-229, 원문 미열람 표기)를 근거로 [사실]로 썼다.",
    "분량 초과 자동 분리: 5. 로봇 능력·작업 온톨로지 본문 8,395자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,815자",
    "2차: 10절 8. 실시간 세계 상태·데이터 일관성 항목 — 문장을 '… 배정 판단에 들어갈 것으로 보인다'로 고치고 태그를 [사실]에서 [추정]으로 내렸다.",
    "2차: 10절 13. 작업 배정 — MRTA 항목 — 실행 가능성 판정 문장에서 [^ref-152]를 빼고 [^ref-236]만 남겼으며, '이동로봇 플릿의 작업 배정 문제를 에너지 소비와 필요 로봇 수 최소화 관점에서 검토한 리뷰도 있다. [사실][^ref-152]'를 별도 문장으로 두어 13절 각주 정의와 프런트매터 sources 의 ref-152 를 유지했다.",
    "2차: 10절 9. 로봇·제조사 관제 연동 항목 — '팩트시트는 지원 동작·적재 명세를, 플릿 어댑터 설정은 수행 가능한 작업 유형·동작 이름을 선언한다. [사실][^ref-228][^ref-105]'로 f1·f7 범위의 사실로 고쳐 썼다.",
    "2차: 3절 마지막 문장과 9절 마지막 문장에 '구축자 의견으로는'을 넣어 [의견]의 주체를 밝혔다.",
    "2차: fixes_applied 의 '원문 미열람 표기' 항목에서 'ref-236~139'를 'ref-236~ref-138, ref-152'로 바로잡았다."
  ],
  "standards_updates": [
    {
      "name": "IDTA 02020 Capability Description 1.0",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description",
      "related_areas": [
        5,
        28
      ],
      "summary": "능력을 속성·속성 제약·전이 제약·스킬로 기술하고 요구 능력과 제공 능력의 비교를 목적으로 하는 자산관리셸 서브모델(원문 미열람).",
      "ref_id": "ref-229"
    },
    {
      "name": "IDTA 02047 Technical Data for Automated Guided Vehicles 1.0",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles",
      "related_areas": [
        5,
        28
      ],
      "summary": "여러 제조사·유형의 무인운반차를 한 환경에서 운영하기 위한 제조사 독립 기술 데이터 자산관리셸 서브모델(원문 미열람, 세부 필드 미확인).",
      "ref_id": "ref-234"
    },
    {
      "name": "CaSkMan",
      "kind": "오픈소스",
      "org": "CaSkade-Automation (GitHub)",
      "url": "https://github.com/CaSkade-Automation/CaSkMan",
      "related_areas": [
        5
      ],
      "summary": "제조 설비의 능력·스킬·스킬 인터페이스·속성을 기술하고 VDI 3682·VDI 2860·DIN 8580·ISA 88·IEC 61360 을 잇는 OWL 정렬 온톨로지.",
      "ref_id": "ref-231"
    },
    {
      "name": "SOMA (Socio-physical Model of Activities)",
      "kind": "오픈소스",
      "org": "EASE CRC",
      "url": "https://github.com/ease-crc/soma",
      "related_areas": [
        5
      ],
      "summary": "DUL 상위 온톨로지를 확장해 로봇 에이전트의 활동을 표현하는 OWL 온톨로지.",
      "ref_id": "ref-233"
    },
    {
      "name": "IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2)",
      "kind": "오픈소스",
      "org": "Helmut Schmidt University, Institute of Automation Technology",
      "url": "https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2",
      "related_areas": [
        5,
        28
      ],
      "summary": "IEEE 1872.2 AuR 온톨로지의 제3자 OWL 구현으로, SUMO 는 제외하고 DUL 만 포함한다.",
      "ref_id": "ref-232"
    },
    {
      "name": "ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/82334.html",
      "related_areas": [
        5,
        28
      ],
      "summary": "서비스 로봇 모듈의 상호운용성·재사용성·조립 가능성을 위한 모듈 공통 정보 모델의 구조와 속성 의미를 정한 국제표준(원문 미열람).",
      "ref_id": "ref-240"
    },
    {
      "name": "KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "kind": "표준",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "related_areas": [
        5,
        28
      ],
      "summary": "KSSN 에 등록된 서비스 로봇 소프트웨어 모듈 정보 모델 국가표준. 제정일·내용 미확인(원문 미열람).",
      "ref_id": "ref-138"
    }
  ]
}
```

### runs/2026-09-25-15/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-15/pages/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지"
type: area
category: "B. 공통 정보·환경 모델"
area_no: 5
related_areas: [7, 8, 9, 12, 13, 21, 27, 28]
tags: [능력 모델, 스킬, VDA 5050 팩트시트, 능력 온톨로지, 실행 가능성 판정]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-025, ref-026, ref-027, ref-028, ref-029, ref-035, ref-038, ref-040, ref-041, ref-042, ref-043, ref-105, ref-228, ref-229, ref-230, ref-231, ref-232, ref-233, ref-234, ref-235, ref-236, ref-237, ref-238, ref-239, ref-240, ref-138, ref-152]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [B. 공통 정보·환경 모델](index.md) › 5. 로봇 능력·작업 온톨로지

# 5. 로봇 능력·작업 온톨로지

!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [분류원문]

## 2. SCM 관점의 질문

같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

같은 운반 로봇 가운데 어느 로봇이 특정 화물을 실제로 취급할 수 있는지는 적재 명세(적재 유형·최대 중량·처리 높이), 지원 동작, 현재 상태(남은 적재 용량·운영 상태), 적재 상태에서의 경로 통과 가능성을 함께 대조해야 판단할 수 있어, 한 규격의 필드만으로는 정해지지 않을 것으로 보인다. [추정][^ref-228][^ref-230][^ref-236]

제조사마다 능력을 적는 방식도 맞춰져 있지 않다. VDA 5050 팩트시트의 적재 유형(loadType)과 MassRobotics 표준의 화물 설명(cargoType)은 모두 문자열로 적게 할 뿐 공통 어휘를 지정하지 않으므로, 제조사 사이에서 화물 취급 가능 여부를 맞추려면 적재물 유형 사전이 따로 필요할 것으로 보인다. [추정][^ref-228][^ref-230]

문서에 선언된 능력과 현장에서 관측되는 능력이 다를 수 있다는 점도 연구 대상이다. Naqvi 외(2025)는 제조사가 광고한 능력(advertised capabilities)과 운용 중 관측된 능력(operational capabilities)을 온톨로지로 구분해 통합하는 방법을 제시했다. [사실][^ref-041] 따라서 구축자 의견으로는 이 영역을 흩어진 선언을 한 모델로 모아 작업 요구와 연결하는, 배정·실행 판단의 공통 기반으로 볼 수 있다. [의견]

## 4. 핵심 개념과 용어

이 영역의 중심 개념은 구현과 무관한 기능 명세인 능력과, 그 능력을 실제로 실행하는 구현인 스킬의 구분이며, 여기에 능력의 조건을 적는 제약·범위 개념이 더해진다. [사실][^ref-229][^ref-231]

자세한 내용은 주제 페이지 [5. 로봇 능력·작업 온톨로지 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area05-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 적치

**시나리오:** 입고된 팔레트를 적치 위치로 옮길 운반 로봇 고르기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고가 확정된 팔레트에 적치 작업이 생긴다(가상 설정). |
| 작업 대상 | 팔레트 한 개. 적재 유형을 VDA 5050 팩트시트는 loadType(예: EPAL)으로, MassRobotics 표준은 cargoType 문자열로 적지만 공통 어휘는 정하지 않은 것으로 보인다. [추정][^ref-228][^ref-230] |
| 수행 자원 | 제조사가 다른 운반 로봇 두 대(가상 설정). 어느 쪽이 취급할 수 있는지는 적재 명세·지원 동작·남은 적재 용량·운영 상태를 함께 대조해야 할 것으로 보인다. [추정][^ref-228][^ref-230][^ref-236] |
| 제약 | 팩트시트의 적재 명세(loadSets)는 최대 중량, 최소·최대 적재 처리 높이, 대략의 픽·드롭 소요 시간을 적는다. [사실][^ref-228] 적재 상태에 따라 달라지는 장소 도달 가능성을 판정하는 연구도 있다. [사실][^ref-236] |
| 완료·인계 | Open-RMF에서는 어댑터가 로봇 API의 완료를 확인한 뒤 execution.finished()를 호출해 완료를 알린다. [사실][^ref-040] |
| 예외·성과 | 선언된 능력과 운용 중 관측된 능력이 다를 수 있다. [사실][^ref-041] 어느 값을 배정 기준으로 삼을지는 열린 질문이다. |

다음은 설명을 위한 가상의 시나리오이다. 적치 작업이 생기면 ROP는 두 로봇의 팩트시트에서 팔레트 유형·중량·처리 높이를 비교하고, 상태 보고에서 남은 적재 용량과 운영 상태를 확인한다. 적재 유형 문자열이 제조사마다 다르면 이 비교 자체가 막힐 수 있다. [추정][^ref-228][^ref-230]

작업이 끝나면 완료 보고는 인터페이스 안에서 선언한 동작 이름을 그대로 쓰는 방식으로 돌아오는 것으로 보인다. [추정][^ref-228][^ref-040] 적재 후 속도처럼 선언과 다른 운용 값이 쌓이면 능력 모델을 어떻게 갱신할지가 다음 과제로 남는다.

## 6. 대표 접근법과 기술

능력 기술과 실행의 연결은 같은 인터페이스 안에서 선언한 동작 이름을 명령·완료 보고에 그대로 쓰는 방식과, 별도 능력 모델을 상태 기계를 가진 스킬 인터페이스로 잇는 방식으로 나뉘는 것으로 보인다. [추정][^ref-228][^ref-040][^ref-229][^ref-231]

자세한 내용은 주제 페이지 [5. 로봇 능력·작업 온톨로지 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area05-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

물류 이동로봇 인터페이스는 적재·동작 능력을 필드로 선언하게 하고, 능력 모델 표준·온톨로지는 능력·스킬·조건을 구조화한다. [사실][^ref-228][^ref-229] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [5. 로봇 능력·작업 온톨로지 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area05-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 로봇 지식 처리·활동 온톨로지, 능력·스킬 모델, 광고·운용 능력 통합, 온톨로지 기반 배정, LLM 기반 능력 온톨로지 생성 연구로 나뉜다. [사실][^ref-233][^ref-038][^ref-041]

자세한 내용은 주제 페이지 [5. 로봇 능력·작업 온톨로지 — 대표 연구와 자료](../../topics/2026/2026-09-25-area05-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사가 선언한 능력·제약(팩트시트·능력 서브모델)을 공통 모델로 모아 작업 요구와 대조하고, 실행 결과로 선언과 실제의 차이를 기록한다. [추정][^ref-228][^ref-229][^ref-041] | 연계 대상: 파지·센서 인식·로컬 회피 같은 능력의 실제 구현과 성능 보장은 제조사 쪽에 둔다. [추정][^ref-228][^ref-229][^ref-041] |

이 경계는 제품 전략에 따라 옮겨질 수 있다. 분류 원문은 "이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다"고 적는다([범위 경계](../../about/scope-boundary.md)). 구축자 의견으로는 이 영역에서 ROP가 맡는 인터페이스는 제조사 선언을 읽는 공통 능력 모델과 요구–능력 대조이며, 능력 자체를 구현하는 일은 포함하지 않는다고 본다. [의견]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 능력 모델은 화물 식별, 현재 상태, 관제 연동, 실행 신뢰성, 배정, 온보딩, AI 방법, 표준 거버넌스 영역과 맞물린다. [추정][^ref-228][^ref-236]

- [7. 화물·재고·자산 식별과 추적](07-cargo-inventory-and-asset-identification-and-tracking.md) — 팩트시트 적재 유형과 MassRobotics 화물 설명을 맞추려면 적재물 유형 어휘가 필요할 것으로 보인다. [추정][^ref-228][^ref-230]
- [8. 실시간 세계 상태·데이터 일관성](08-real-time-world-state-and-data-consistency.md) — 상태 보고의 운영 상태·남은 적재 용량과 운용 중 관측된 능력은 현재 상태 표현으로서 배정 판단에 들어갈 것으로 보인다. [추정][^ref-230][^ref-041]
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 팩트시트는 지원 동작·적재 명세를, 플릿 어댑터 설정은 수행 가능한 작업 유형·동작 이름을 선언한다. [사실][^ref-228][^ref-105]
- [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 선언한 동작 이름이 명령·완료 보고로 이어지는 방식이 실행 확인과 맞닿는다. [추정][^ref-040][^ref-228]
- [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md) — 실행 가능성 판정 결과를 배정기 독립 입력으로 넘기는 연구가 두 영역을 잇는다. [사실][^ref-236] 이동로봇 플릿의 작업 배정 문제를 에너지 소비와 필요 로봇 수 최소화 관점에서 검토한 리뷰도 있다. [사실][^ref-152]
- [21. 온보딩·설정·현장 시운전](../f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 매뉴얼·로봇 기술 파일 해석으로 능력 모델을 만드는 일은 온보딩 때 필요하다. [추정][^ref-238][^ref-239]
- [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — LLM 기반 능력 온톨로지 생성과 형식 검증은 이 영역에 적용되는 AI 방법이다. [사실][^ref-238][^ref-239]
- [28. 표준·상호운용성·다사업자 거버넌스](../g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — IDTA 02047, ISO 22166-201, KS B 7321-2 같은 제조사 독립 정보 모델 표준이 걸려 있다. [사실][^ref-234][^ref-240][^ref-138]
- [매뉴얼 기반 로봇 기능 온톨로지 트랙](../../tracks/manual-capability-ontology/index.md) — 이 영역을 중심으로 한 중점 연구 트랙이다.

## 11. 열린 질문

국내 표준 부합화, 적재물 유형 공통 어휘, 선언 능력과 운용 능력 가운데 배정 기준이 아직 풀리지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-004** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-02) IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? 부분 근거로 서비스 로봇 모듈 정보 모델 국제표준과 국내 KS가 확인됐으나, 로봇 온톨로지·능력 서브모델의 부합화는 확인되지 않았다.[^ref-240][^ref-138]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-15) VDA 5050 팩트시트의 loadType과 MassRobotics의 cargoType이 자유 문자열일 때 팔레트·용기 같은 적재물 유형을 제조사 사이에 같은 의미로 맞출 공통 어휘나 코드 체계가 있는가?[^ref-228][^ref-230]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-15) 제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가?[^ref-041]

트랙 전용 질문은 [질문 백로그](../../tracks/manual-capability-ontology/question-backlog.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-25 (원문 미열람)
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-233]: EASE CRC (ease-crc/soma), SOMA — README (Socio-physical Model of Activities), 미확인, https://github.com/ease-crc/soma, 접근일 2026-09-25
[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)
[^ref-240]: ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules, 2024-02, https://www.iso.org/standard/82334.html, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)
[^ref-152]: Meseguer Valenzuela, A., & Blanes Noguera, F., Task Allocation in Mobile Robot Fleets: A review, 2025-01, https://arxiv.org/abs/2501.08726, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지"
type: area
category: "B. 공통 정보·환경 모델"
area_no: 5
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [B. 공통 정보·환경 모델](index.md) › 5. 로봇 능력·작업 온톨로지

# 5. 로봇 능력·작업 온톨로지

!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [분류원문]

## 2. SCM 관점의 질문

같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]

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

### runs/2026-09-25-15/pages/topics/2026/2026-09-25-area05-s7.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "B. 공통 정보·환경 모델"
primary_area_no: 5
related_areas: [7, 8, 9, 12, 13, 21, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-025, ref-026, ref-105, ref-228, ref-229, ref-230, ref-231, ref-232, ref-234, ref-235, ref-240, ref-138]
last_run: 2026-09-25
version: 1
split_from: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#7
---

[홈](../../index.md) › [주제](../index.md) › 5. 로봇 능력·작업 온톨로지 — 관련 표준·프레임워크·오픈소스

# 5. 로봇 능력·작업 온톨로지 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 물류 이동로봇 인터페이스는 적재·동작 능력을 필드로 선언하게 하고, 능력 모델 표준·온톨로지는 능력·스킬·조건을 구조화한다. [사실][^ref-228][^ref-229] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

물류 이동로봇 인터페이스는 적재·동작 능력을 필드로 선언하게 하고, 능력 모델 표준·온톨로지는 능력·스킬·조건을 구조화한다. [사실][^ref-228][^ref-229] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 팩트시트 스키마(3.0.0판) | 표준 | 유형 명세(등급·능력), 물리 파라미터, 프로토콜 한계·기능, 기하, 적재 명세를 필수 블록으로 둔다(확인일 2026-09-25). [사실][^ref-228] | 공식 저장소 스키마 원문 |
| MassRobotics AMR 상호운용 표준 JSON 스키마 | 표준 | 식별 보고에 최대 속도·예상 가동 시간·충전기 유형·화물 설명·화물 최대 부피·최대 중량·제품 문서 링크를, 상태 보고에 운영 상태(9개 값)와 남은 적재 용량 비율을 둔다. [사실][^ref-230] | 공식 저장소 스키마 원문 |
| Open-RMF 플릿 어댑터 설정 | 오픈소스 | 플릿 단위로 수행 가능한 작업 유형(task_capabilities: loop, delivery 등), 사용자 정의 동작 이름, 작업 종료 후 동작(park·charge·nothing)을 선언한다. [사실][^ref-105] | 공식 템플릿 원문 |
| IDTA 02020 Capability Description 1.0 | 표준 | 능력을 속성·속성 제약·전이 제약·스킬로 기술하고 요구·제공 능력 비교를 목적으로 하는 자산관리셸(AAS) 서브모델이다. [사실][^ref-229] | IDTA 저장소 안내문, 원문 미열람 |
| IDTA 02047 Technical Data for AGV 1.0 | 표준 | 여러 제조사·유형의 무인운반차를 한 생산 환경에서 운영하기 위해 제조사 독립 기술 데이터를 AAS 서브모델로 표준화하려는 명세다. 세부 필드는 미확인이다. [사실][^ref-234] | IDTA 저장소 안내문, 원문 미열람 |
| CaSkMan | 오픈소스 | 제조 설비의 능력·스킬·스킬 인터페이스·속성을 기술하는 OWL 정렬 온톨로지다. [사실][^ref-231] | 공식 저장소 원문 |
| W3C/OGC SSN System Capabilities 모듈 | 표준 | 조건별 시스템 능력, 운용 범위, 생존 범위를 hasSystemCapability·inCondition 관계로 기술한다. 작업반 저장소 편집본이며 권고안과 문구 일치는 미확인이다. [사실][^ref-235] | 작업반 저장소 원문 |
| IEEE 1872-2015 (CORA) | 표준 | 로봇·자동화 분야의 일반 개념·관계·공리를 담은 핵심 온톨로지를 정한 표준 온톨로지다([용어: CORA](../../glossary/cora.md)). [사실][^ref-025] | 원문 미열람 |
| IEEE 1872.2 AuR 온톨로지 OWL 구현(헬무트 슈미트 대학) | 오픈소스 | IEEE 1872.2 AuR 온톨로지(표준은 상위 온톨로지 DUL·SUMO를 씀)의 OWL 구현으로, SUMO는 OWL 표현이 없어 제외하고 DUL만 포함한 제3자 구현이다. 로봇이 제공하고 기능 실행으로 수행되는 기능, 상호작용, 환경을 기술한다. [사실][^ref-232][^ref-026] | 구현 저장소 원문, 표준 원문 미열람 |
| ISO 22166-201:2024 | 표준 | 서비스 로봇 모듈의 상호운용성·재사용성·조립 가능성을 위해 모듈 공통 정보 모델의 구조와 속성·하위 클래스의 의미를 정한다. [사실][^ref-240] | 원문 미열람 |
| KS B 7321-2 | 표준 | '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 KSSN에 등록되어 있다. 제정일·내용은 미확인이다. [사실][^ref-138] | 원문 미열람 |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)
- 관련 영역: [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-025]: IEEE, 1872-2015 - IEEE Standard Ontologies for Robotics and Automation, 2015, https://ieeexplore.ieee.org/document/7084073/, 접근일 2026-09-25 (원문 미열람)
[^ref-026]: IEEE, IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology, 2022, https://standards.ieee.org/standard/1872_2-2021.html, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-232]: Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub), IndustrialStandard-ODP-IEEE1872-2 — README (IEEE 1872.2 AuR ontology OWL implementation), 미확인, https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2, 접근일 2026-09-25
[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-235]: W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub), ssn/integrated/ssn-system.ttl (SSN System Capabilities module), 미확인, https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl, 접근일 2026-09-25
[^ref-240]: ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules, 2024-02, https://www.iso.org/standard/82334.html, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-15 | 5. 로봇 능력·작업 온톨로지 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-15/pages/topics/2026/2026-09-25-area05-s6.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지 — 대표 접근법과 기술"
type: topic
category: "B. 공통 정보·환경 모델"
primary_area_no: 5
related_areas: [7, 8, 9, 12, 13, 21, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-040, ref-228, ref-229, ref-231, ref-236, ref-237, ref-238, ref-239]
last_run: 2026-09-25
version: 1
split_from: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#6
---

[홈](../../index.md) › [주제](../index.md) › 5. 로봇 능력·작업 온톨로지 — 대표 접근법과 기술

# 5. 로봇 능력·작업 온톨로지 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 능력 기술과 실행의 연결은 같은 인터페이스 안에서 선언한 동작 이름을 명령·완료 보고에 그대로 쓰는 방식과, 별도 능력 모델을 상태 기계를 가진 스킬 인터페이스로 잇는 방식으로 나뉘는 것으로 보인다. [추정][^ref-228][^ref-040][^ref-229][^ref-231]
- 이 페이지는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

능력 기술과 실행의 연결은 같은 인터페이스 안에서 선언한 동작 이름을 명령·완료 보고에 그대로 쓰는 방식과, 별도 능력 모델을 상태 기계를 가진 스킬 인터페이스로 잇는 방식으로 나뉘는 것으로 보인다. [추정][^ref-228][^ref-040][^ref-229][^ref-231]

### 인터페이스 안의 이름 기반 선언

VDA 5050 3.0.0 팩트시트의 지원 동작 목록은 동작마다 actionType, 자유 문장 설명, 허용 범위, 파라미터(key·데이터형·선택 여부), 일시정지·취소 가능 여부를 적는다. [사실][^ref-228] Open-RMF의 사용자 정의 동작은 설정의 actions 목록에 이름으로만 선언되고, 작업 요청의 category(동작 이름)와 JSON description으로 호출된다. [사실][^ref-040] 한계로, 팩트시트 파라미터에는 허용 값 범위나 실행 전제조건을 담는 구조화 필드가 없어 그런 조건은 자유 문장이나 적재 명세의 최소·최대 필드에 흩어질 것으로 보인다. [추정][^ref-228]

### 능력–스킬 모델

IDTA 02020 능력 서브모델 1.0은 속성·제약·스킬로 능력을 기술하며, 요구 능력과 제공 능력을 신뢰성 있게 비교하는 것을 목적으로 한다. [사실][^ref-229] CaSkMan은 설비 구조, 추상 능력, 상태 기계를 가진 실행 스킬, 속성을 모델링하고 VDI 3682·VDI 2860·DIN 8580·ISA 88·IEC 61360을 잇는 정렬 온톨로지다. [사실][^ref-231] 이번 조사에서는 두 방식을 서로 매핑한 표준을 확인하지 못했다.

### 의미 모델로 실행 가능성을 판정한 뒤 배정기로 넘기기

Electronics(2026-08) 게재 연구는 로봇·작업·장소의 의미 모델과 선언적·절차적 혼합 추론으로 다축 능력 조건과 적재 상태에 따른 장소 도달 가능성을 판정하고, 그 결과를 배정 알고리즘과 무관한 공통 입력(ReasonerOutput)으로 넘긴다. [사실][^ref-236] CAPILANO는 이종 조립 자원과 결합 능력을 OWL 온톨로지로 기술하고 SPARQL 질의와 가용성을 고려한 연속 작업 배정을 한 틀로 묶었다. [사실][^ref-237] 이 연구는 제조 조립(라인리스 이동 조립 시스템) 대상이므로 물류 사례가 아니라 방법 참고로만 본다.

### 문서·로봇 기술 파일에서 능력 온톨로지 만들기

분류 원문 교차 규칙에 따라 매뉴얼 해석은 27. AI·학습·적응과 모델 운영의 연구 방법을 이 영역과 21. 온보딩·설정·현장 시운전에 적용하는 경우다. Vieira da Silva 외(ETFA 2024)는 여러 LLM과 프롬프트 기법으로 능력 온톨로지를 생성하고 RDF 구문 검사·OWL 추론·SHACL 제약에 기반한 반자동 품질 검사를 적용해, 복잡한 능력에서도 오류가 거의 없었다고 저자들이 보고했다. [사실][^ref-238] Dussard·Sarthou(ICSR 2026)는 URDF 로봇 기술 파일의 식별자를 LLM으로 해석해 기존 온톨로지 개념을 채우고, 여러 질의의 다수결과 구문·스키마 수준 검증으로 신뢰성을 높이는 파이프라인을 제안했다. [사실][^ref-239] 두 연구 모두 생성 결과를 형식 검증에 통과시키므로, 문서 기반 능력 모델 구축에서도 생성과 검증을 분리한 구조가 필요할 것으로 보인다. [추정][^ref-238][^ref-239] 물류 로봇 매뉴얼을 대상으로 한 공개 사례는 이번 조사에서 확인하지 못했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)
- 관련 영역: [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-15 | 5. 로봇 능력·작업 온톨로지 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-15/pages/topics/2026/2026-09-25-area05-s4.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지 — 핵심 개념과 용어"
type: topic
category: "B. 공통 정보·환경 모델"
primary_area_no: 5
related_areas: [7, 8, 9, 12, 13, 21, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-029, ref-035, ref-041, ref-228, ref-229, ref-231, ref-235]
last_run: 2026-09-25
version: 1
split_from: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#4
---

[홈](../../index.md) › [주제](../index.md) › 5. 로봇 능력·작업 온톨로지 — 핵심 개념과 용어

# 5. 로봇 능력·작업 온톨로지 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 중심 개념은 구현과 무관한 기능 명세인 능력과, 그 능력을 실제로 실행하는 구현인 스킬의 구분이며, 여기에 능력의 조건을 적는 제약·범위 개념이 더해진다. [사실][^ref-229][^ref-231]
- 이 페이지는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 중심 개념은 구현과 무관한 기능 명세인 능력과, 그 능력을 실제로 실행하는 구현인 스킬의 구분이며, 여기에 능력의 조건을 적는 제약·범위 개념이 더해진다. [사실][^ref-229][^ref-231]

- **능력(Capability)** — 구현과 무관한 기능 명세다. [사실][^ref-229] 이 위키의 [능력·스킬·서비스 모델(CSS)](../../glossary/capabilities-skills-services.md) 용어 항목과 매뉴얼 기반 로봇 기능 온톨로지 트랙의 온톨로지 초안이 '기능(Capability)'이라 부르는 개념과 같은 뜻이며, 이 페이지에서는 '능력'으로 쓴다.
- **스킬(Skill)** — OPC UA 같은 호출 인터페이스를 가진, 능력의 캡슐화된 구현이다. IDTA 02020과 CaSkMan 온톨로지가 이 구분을 공통으로 쓴다. [사실][^ref-229][^ref-231] CaSkMan은 Plattform Industrie 4.0의 CSS 참조 모델 위에 구축됐다. [사실][^ref-231] IDTA 02020도 같은 CSS 계열의 구분을 따르는 것으로 보이나, IDTA 안내문에서 CSS 언급은 확인되지 않았다. [추정][^ref-035]
- **속성 제약·전이 제약(Property Constraint·Transition Constraint)** — IDTA 02020은 능력의 속성(최대 속도·허용 오차·온도 범위 등)에 전제조건·불변조건·사후조건 역할의 제약을 붙이고, 순서·병렬 흐름을 전이 제약으로 정한다. [사실][^ref-229]
- **전제조건·효과(Precondition·Effect)** — [계획 도메인 정의 언어(PDDL)](../../glossary/pddl.md)는 행동을 파라미터·전제조건·효과로 기술하고 도메인과 문제 인스턴스를 분리한다. [사실][^ref-029]
- **운용 범위·생존 범위(Operating Range·Survival Range)** — W3C/OGC SSN의 System Capabilities 모듈은 특정 조건에서의 시스템 능력, 정상 운용 범위, 그리고 벗어나면 시스템이 손상되어 능력 명세가 더 이상 성립하지 않을 수 있는 생존 범위를 구분한다. [사실][^ref-235]
- **광고 능력·운용 능력(Advertised·Operational Capability)** — 제조사가 광고한 능력과 운용 중 관측된 능력을 나누는 구분이다. [사실][^ref-041]
- **팩트시트(Factsheet)** — [VDA 5050](../../glossary/vda-5050.md) 3.0.0판에서 이동로봇이 유형·능력 명세, 물리 파라미터, 지원 동작, 적재 명세 등을 관제에 미리 알리는 스키마다(확인일 2026-09-25). [사실][^ref-228]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)
- 관련 영역: [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-029]: McDermott, D. 외, PDDL - The Planning Domain Definition Language, 1998, https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language, 접근일 2026-09-25 (원문 미열람)
[^ref-035]: Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services, 2022-11, https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-235]: W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub), ssn/integrated/ssn-system.ttl (SSN System Capabilities module), 미확인, https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-15 | 5. 로봇 능력·작업 온톨로지 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-15/pages/topics/2026/2026-09-25-area05-s8.md

```markdown
---
title: "5. 로봇 능력·작업 온톨로지 — 대표 연구와 자료"
type: topic
category: "B. 공통 정보·환경 모델"
primary_area_no: 5
related_areas: [7, 8, 9, 12, 13, 21, 27, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-027, ref-028, ref-038, ref-041, ref-042, ref-043, ref-233, ref-236, ref-237, ref-238, ref-239, ref-152]
last_run: 2026-09-25
version: 1
split_from: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#8
---

[홈](../../index.md) › [주제](../index.md) › 5. 로봇 능력·작업 온톨로지 — 대표 연구와 자료

# 5. 로봇 능력·작업 온톨로지 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 로봇 지식 처리·활동 온톨로지, 능력·스킬 모델, 광고·운용 능력 통합, 온톨로지 기반 배정, LLM 기반 능력 온톨로지 생성 연구로 나뉜다. [사실][^ref-233][^ref-038][^ref-041]
- 이 페이지는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 로봇 지식 처리·활동 온톨로지, 능력·스킬 모델, 광고·운용 능력 통합, 온톨로지 기반 배정, LLM 기반 능력 온톨로지 생성 연구로 나뉜다. [사실][^ref-233][^ref-038][^ref-041]

- Beetz 외, KnowRob 2.0(2018) — 인지 기반 로봇 에이전트를 위한 2세대 지식 처리 프레임워크다. [사실][^ref-027]
- EASE CRC, SOMA — DUL(DOLCE+DnS Ultralite) 상위 온톨로지를 확장한 OWL 활동 온톨로지로, 로봇 에이전트의 의도·계획·움직임·물체와의 접촉 같은 활동 측면을 표현한다. [사실][^ref-233][^ref-028]
- Vieira da Silva·Köcher·Fay, 이종 자율 로봇을 위한 능력·스킬 모델(2022) — 이종 자율 로봇용 능력·스킬 모델을 제안한 프리프린트다. [사실][^ref-038]
- Naqvi 외, 광고 능력과 운용 능력의 온톨로지 기반 통합(2025) — 두 능력을 온톨로지로 구분해 통합하는 방법을 제시했다. [사실][^ref-041]
- Aguado 외, 신뢰할 수 있는 로봇 자율성을 위한 온톨로지 활용 프로세스 서베이(2024) — 이 주제의 서베이 논문이다. [사실][^ref-042]
- 신민종·한영석·정재윤, 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계(2024) — 국내 학술지 게재 논문이며, 능력 기술을 포함하는지는 미확인이다. [사실][^ref-043]
- Electronics 게재 논문, 이종 다중 로봇 작업 배정을 위한 의미 기반 실행 가능성 추론(2026) — 6절 참고. 저자 미확인. [사실][^ref-236]
- Kluge-Wilkes 외, CAPILANO(2022) — 제조 조립(라인리스 이동 조립 시스템) 대상 온톨로지 기반 배정 연구로, 방법 참고용이다. [사실][^ref-237]
- Vieira da Silva 외(2024), Dussard·Sarthou(2026) — LLM으로 능력 온톨로지를 생성·채우고 형식 검증하는 연구다(6절 참고). [사실][^ref-238][^ref-239]
- Meseguer Valenzuela·Blanes Noguera, 이동로봇 플릿 작업 배정 리뷰(2025) — 이동로봇 플릿의 작업 배정 문제를 에너지 소비와 필요 로봇 수 최소화 관점에서 정리하고 AI 기반 방법을 포함한 최적화 알고리즘을 검토했다. [사실][^ref-152]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)
- 관련 영역: [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md), [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-027]: Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G., KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents, 2018, https://ai.uni-bremen.de/papers/beetz18knowrob.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-028]: Beßler, D. 외, Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents, 2021, https://arxiv.org/pdf/2011.11972, 접근일 2026-09-25 (원문 미열람)
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-042]: Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R., A survey of ontology-enabled processes for dependable robot autonomy, 2024-07, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full, 접근일 2026-09-25 (원문 미열람)
[^ref-043]: 신민종, 한영석, 정재윤, 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-25 (원문 미열람)
[^ref-233]: EASE CRC (ease-crc/soma), SOMA — README (Socio-physical Model of Activities), 미확인, https://github.com/ease-crc/soma, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)
[^ref-152]: Meseguer Valenzuela, A., & Blanes Noguera, F., Task Allocation in Mobile Robot Fleets: A review, 2025-01, https://arxiv.org/abs/2501.08726, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-15 | 5. 로봇 능력·작업 온톨로지 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-15/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/association-event.md
glossary/b2mml.md
glossary/behavior-tree.md
glossary/bpmn.md
glossary/business-location.md
glossary/capabilities-skills-services.md
glossary/cbv.md
glossary/cora.md
glossary/dds-security.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/epcis.md
glossary/fleet-adapter.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/giai.md
glossary/grai.md
glossary/index.md
glossary/isa-95.md
glossary/lifelong-mapf.md
glossary/linear-temporal-logic.md
glossary/mapf.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/ocel.md
glossary/open-rmf.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/robotic-mobile-fulfillment-system.md
glossary/scor.md
glossary/semi-open-queueing-network.md
glossary/sscc.md
glossary/task-decomposition.md
glossary/vda-5050.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
standards/index.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/index.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/glossary/index.md

```markdown
---
title: "용어집"
type: glossary
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../index.md) › 용어집

# 용어집

이 위키에서 쓰는 용어의 한글·영문 표기와 한 줄 정의를 모은다. 용어마다 개별 페이지에 설명, 관련 연구영역, 출처를 둔다. 시드 용어는 SCOR, ISA-95, EPCIS, Open-RMF, Fleet Adapter, WES/WCS/WMS/MES/TMS, MRTA, MAPF, Lifelong MAPF, Multi-Agent Pickup and Delivery, ARIAC, DDS-Security, 디지털 트윈이다. 새 용어는 스토리텔러 에이전트가 제안하고 퍼블리셔가 반영한다.

아래 표는 용어 페이지의 프런트매터(term_ko, term_en, definition, related_areas)에서 자동으로 만든다.

## 용어 목록

<!-- auto:glossary-index:start -->
| 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 |
|---|---|---|---|
| [B2MML](b2mml.md) | Business To Manufacturing Markup Language (B2MML) | MESA International이 ISA-95(IEC 62264)의 데이터 모델을 XML 스키마로 구현한 교환 형식이다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) |
| [DDS 보안 규격](dds-security.md) | DDS Security (DDS-Security) | DDS(Data Distribution Service)의 보안 규격으로, ROS 2가 인증·암호화·접근통제 구조의 기반으로 통합했다. | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [IndoorGML](indoorgml.md) | IndoorGML | IFC 데이터에서 자동 생성하는 도구(ifc2indoorgml)의 대상이 되는 실내 공간 정보 표준이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [VDA 5050](vda-5050.md) | VDA 5050 | 독일자동차산업협회(VDA)와 VDMA가 정한 이동로봇(AGV·AMR)과 상위 관제(fleet control) 사이의 통신 인터페이스 권고안이며 현행판은 3.0.0이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) |
| [객체 중심 이벤트 로그](ocel.md) | Object-Centric Event Log (OCEL) | 이벤트와 여러 객체 사이 관계, 관계의 한정자, 시간에 따라 바뀌는 객체 속성을 기록하는 이벤트 로그 교환 표준이며, 2.0판은 SQLite·XML·JSON 형식을 둔다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) |
| [계획 도메인 정의 언어](pddl.md) | Planning Domain Definition Language (PDDL) | 자동 계획 문제에서 행동을 파라미터·전제조건·효과로 기술하고 도메인과 문제 인스턴스를 분리해 표현하는 언어이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) |
| [공급망 운영 참조 모델](scor.md) | Supply Chain Operations Reference (SCOR) | ASCM이 관리하는 공급망 프로세스 참조 모델로, 공급망을 계획·주문·조달·생산/가공·이행·반품 프로세스와 이를 아우르는 오케스트레이션 프로세스로 기술한다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) |
| [글로벌 개별 자산 식별자](giai.md) | Global Individual Asset Identifier (GIAI) | 컨테이너·트럭·트레일러 같은 개별 자산을 식별하는 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [글로벌 반환형 자산 식별자](grai.md) | Global Returnable Asset Identifier (GRAI) | 팔레트·상자·트레이·케그처럼 여러 번 재사용되는 운반구를 식별하는 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [기업–제어 시스템 통합 표준](isa-95.md) | ISA-95 Enterprise-Control System Integration | ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [능력·스킬·서비스 모델](capabilities-skills-services.md) | Capabilities, Skills and Services (CSS) Model | Plattform Industrie 4.0 작업반이 제안한 정보 모델로, 구현과 무관한 기능 명세(능력)와 그 실행 가능한 구현(스킬), 제공 형태(서비스)를 구분한다. 이 위키의 온톨로지 초안에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [다중 로봇 작업 배정](mrta.md) | Multi-Robot Task Allocation (MRTA) | 여러 로봇과 여러 작업이 있을 때 어떤 로봇(또는 로봇 팀)이 어떤 작업을 맡을지 정하는 문제이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [다중 에이전트 경로 찾기](mapf.md) | Multi-Agent Path Finding (MAPF) | 여러 에이전트(로봇)가 각자의 출발지에서 목적지까지 서로 충돌하지 않고 동시에 따라갈 수 있는 경로들을 계획하는 문제이다. | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [다중 에이전트 픽업·배송](multi-agent-pickup-and-delivery.md) | Multi-Agent Pickup and Delivery (MAPD) | 픽업 위치와 배송 위치가 있는 작업이 온라인으로 계속 들어올 때, 에이전트에 작업을 배정하고 충돌 없는 경로를 함께 계획하는 문제이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) |
| [디지털 트윈](digital-twin.md) | Digital Twin | 물리적 대상(장비·자재·공정·설비·제품 등)을 데이터로 연결된 가상 모델로 표현한 것이다. | [22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) |
| [래스터–벡터 변환](raster-to-vector-conversion.md) | Raster-to-Vector Conversion | 픽셀 이미지로 된 평면도를 벽 선분·교차점·방 다각형 같은 기하 요소의 벡터 표현으로 바꾸는 처리이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [로봇 이동형 풀필먼트 시스템](robotic-mobile-fulfillment-system.md) | Robotic Mobile Fulfillment System (RMFS) | 로봇이 상품을 담은 이동식 선반(pod)을 작업대까지 옮기고 작업자가 그 앞에서 피킹·보충하는 부품-작업자(parts-to-picker) 방식의 자동화 창고 시스템이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [로봇·자동화 핵심 온톨로지](cora.md) | Core Ontology for Robotics and Automation (CORA) | IEEE 1872-2015가 정한 로봇·자동화 분야의 가장 일반적인 개념·관계·공리를 담은 핵심 온톨로지이다. | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [리틀의 법칙](littles-law.md) | Little's Law | 재공품(WIP)이 처리량(TH)과 사이클 타임(CT)의 곱과 같다는 관계로, 처리량·재공품·리드타임을 함께 해석하는 기준이 된다. | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) |
| [물류 단위 일련 코드](sscc.md) | Serial Shipping Container Code (SSCC) | 케이스·팔레트·소포 등 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 식별 키이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [반개방형 대기행렬 네트워크](semi-open-queueing-network.md) | Semi-Open Queueing Network (SOQN) | 외부에서 주문이 들어오되 로봇 같은 한정된 자원 수가 고정된 채 순환하는 시스템의 처리량·대기 시간을 해석적으로 추정하는 대기행렬 모델이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [비즈니스 프로세스 모델 및 표기법](bpmn.md) | Business Process Model and Notation (BPMN) | OMG가 정한 업무 프로세스 표기법으로, ISO/IEC 19510:2013은 OMG BPMN 2.0.1을 PAS 절차로 국제표준화한 것이다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) |
| [산업 기초 클래스](ifc.md) | Industry Foundation Classes (IFC) | IfcSpace·IfcDoor 같은 클래스로 건물 요소를 담는 BIM 교환 형식이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |
| [산업 자동화용 민첩 로봇 경진대회](ariac.md) | Agile Robotics for Industrial Automation Competition (ARIAC) | NIST가 운영하는 로봇 경진대회로, 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가한다. | [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) |
| [선형 시간 논리](linear-temporal-logic.md) | Linear Temporal Logic (LTL) | 작업의 순서·시간 제약을 명확한 의미로 기술하는 형식 논리이다. | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [업무 위치](business-location.md) | Business Location (EPCIS bizLocation) | EPCIS 이벤트 뒤 다른 이벤트가 반박할 때까지 객체가 있다고 보는 업무상 위치를 나타내는 선택 필드이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) |
| [연결 이벤트](association-event.md) | AssociationEvent | 물리 객체를 상위 객체나 특정 물리 위치와 연결하거나 연결을 해제한 사실을 기록하는 EPCIS 2.0 이벤트 유형이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [오픈 RMF](open-rmf.md) | Open-RMF (Open Robotics Middleware Framework) | ROS 2 기반의 다중 로봇 조율 프레임워크로, 제조사별 플릿 어댑터와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결하고 작업·교통을 조율한다. | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [완전 주문 이행률](perfect-order-fulfillment.md) | Perfect Order Fulfillment | 완전 주문 수를 전체 주문 수로 나눈 비율로, 주문의 모든 품목 줄이 완전해야 완전 주문으로 보는 SCOR의 신뢰성 대표 지표(RL.1.1)이다. | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) |
| [워크플로 넷](workflow-net.md) | Workflow Net (WF-net) | 워크플로를 모델링·분석하는 표준적 방법 가운데 하나로 쓰이는 페트리 넷의 한 부류이다. | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) |
| [웨이브리스 출고 지시](waveless-order-release.md) | Waveless Order Release | 주문을 큰 묶음(웨이브)으로 모아 내리지 않고 도착·여유 용량에 따라 연속으로 현장에 내려보내는 출고 지시 방식이다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) |
| [위상 지도](topological-map.md) | Topological Map | 정확한 좌표 대신 방·구역 같은 장소를 노드로, 통로·문 같은 연결을 엣지로 두어 공간의 연결 관계를 표현하는 지도이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) |
| [이산 사건 시뮬레이션](discrete-event-simulation.md) | Discrete Event Simulation (DES) | 주문 도착·작업 완료 같은 사건이 일어나는 시점마다 시스템 상태를 갱신해 처리량·대기·가동률을 실험하는 시뮬레이션 방식이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) |
| [작업 분해](task-decomposition.md) | Task Decomposition | 상위 지시나 목표를 로봇이 실행할 수 있는 하위 작업·동작의 순서나 구조로 나누는 일이다. | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [전자 제품 코드 정보 서비스](epcis.md) | Electronic Product Code Information Services (EPCIS) | GS1이 정한, 제품·자산의 상태·위치·이동·인계에 관한 이벤트를 기록하고 공유하기 위한 표준이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) |
| [점유 격자 지도](occupancy-grid-map.md) | Occupancy Grid Map (OGM) | 공간을 일정 크기 칸으로 나누고 칸마다 점유·빈 공간·미지 여부를 적어 로봇 위치추정과 경로계획에 쓰는 지도 표현이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) |
| [종합설비효율](overall-equipment-effectiveness.md) | Overall Equipment Effectiveness (OEE) | 설비의 가용성·효과성(성능)·품질률을 곱해 구하는 지표로, ISO 22400-2(2014판)가 제조 운영 관리 KPI의 하나로 정의한다. | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [지속형 다중 에이전트 경로 찾기](lifelong-mapf.md) | Lifelong Multi-Agent Path Finding (Lifelong MAPF) | 에이전트가 목적지에 도착하면 곧바로 새 목적지를 받아 계속 이동하는 조건에서 충돌 없는 경로를 계속 계획하는 MAPF의 변형이다. | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
| [집계 이벤트](aggregation-event.md) | AggregationEvent | 상자를 팔레트에 싣거나 내리는 것처럼 상위 객체와 하위 객체의 물리적 결합·분리를 기록하는 EPCIS 이벤트 유형이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [차량 소요대수 산정](fleet-sizing.md) | Fleet Sizing | 예상 물동량과 서비스 수준(대기 시간·처리량) 목표를 만족하는 데 필요한 로봇·운반 차량의 최소 대수를 정하는 계획 문제이다. | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| [창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템](wes-wcs-wms-mes-tms.md) | Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System | 창고·생산·운송의 주문·재고·설비·공정을 관리하거나 실행하는 업무·실행 시스템 계열의 약어이며, ROP는 이들에서 작업 요청을 받아 로봇 작업으로 바꾸고 결과를 되돌려 주는 관계에 있다. | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) |
| [파놉틱 심볼 스포팅](panoptic-symbol-spotting.md) | Panoptic Symbol Spotting | CAD 도면의 선 요소마다 문·창문 같은 셀 수 있는 기호의 개별 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 판별하는 과제이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [판독 지점](read-point.md) | Read Point (EPCIS readPoint) | EPCIS 이벤트가 일어난 지점을 나타내는 선택 필드이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) |
| [평면도 인식](floor-plan-recognition.md) | Floor Plan Recognition | 평면도 이미지나 CAD 도면에서 벽·문·창문·계단 같은 건축 요소와 방 영역·유형을 자동으로 찾아내 구조화하는 작업이다. | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) |
| [프로세스 마이닝](process-mining.md) | Process Mining | 시스템에 남은 이벤트 로그로 실제 업무 흐름을 발견하고 대기·병목을 분석하는 기법이다. | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) |
| [플릿 어댑터](fleet-adapter.md) | Fleet Adapter | Open-RMF에서 제조사별 로봇 플릿(같은 관제 아래 묶인 로봇 무리)을 연결하기 위해 두는 제조사별 연결 구성요소이다. | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) |
| [핵심 업무 어휘](cbv.md) | Core Business Vocabulary (CBV) | EPCIS 이벤트의 업무 단계·상태·인계 유형 등에 채울 표준 어휘 값을 정한 GS1 표준(ISO/IEC 19988)이다. | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) |
| [행동 트리](behavior-tree.md) | Behavior Tree | 로봇 동작과 조건 확인을 트리 노드로 조합해 실행 구조를 표현하는 형식이다. | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) |
<!-- auto:glossary-index:end -->
```

### docs/references/index.md

```markdown
---
title: "참고문헌"
type: reference
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../index.md) › 참고문헌

# 참고문헌

이 위키가 인용한 출처의 목록이다. 출처마다 id, 기관, 제목, 발행일, URL, 유형, 신뢰도, 접근일, 요약, 인용된 페이지를 개별 페이지에 둔다. 시드 10건(ref-001 ~ ref-010)은 분류 원문 12장의 참고 자료 1~10번에 그대로 대응한다. 새 출처는 리서치 에이전트가 제안하고 내용 검증 에이전트가 실재를 확인한 뒤 퍼블리셔가 추가한다.

신뢰도는 출처 유형을 기준으로 한다. 표준·정부·연구기관·논문·오픈소스 공식 문서는 high, 기사·보도자료·벤더 문서는 medium 이며, 내용 검증 에이전트가 원문을 열어 확인하면 조정할 수 있다. 다만 URL 을 열어 확인하지 못한 출처(원문 미열람)에는 유형과 무관하게 high 를 주지 않고 medium 상한을 적용한다. 시드 10건은 구축 환경의 네트워크 정책으로 URL 을 열지 못했으므로 모두 원문 미열람 상태이며, 각 페이지의 "원문 열람" 행에 그 사실을 적어 둔다. 외부 접속이 가능한 환경에서 `ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh` 를 실행한 뒤 `python3 pipeline/scaffold.py --apply-url-check` 를 실행하면 열림이 확인된 출처의 신뢰도가 유형 기준값으로 올라간다.

## 목록

<!-- auto:references-index:start -->
| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL |
|---|---|---|---|---|---|---|---|
| [ref-001](ref-001.md) | ASCM | SCOR Digital Standard | 미확인 | 표준 | medium | 2026-09-24 | <https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/> |
| [ref-002](ref-002.md) | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | 기사 | medium | 2026-09-24 | <https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of> |
| [ref-003](ref-003.md) | GS1 | EPCIS and CBV Linked Data Model | 미확인 | 표준 | medium | 2026-09-24 | <https://ref.gs1.org/epcis/> |
| [ref-004](ref-004.md) | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/rmf-core.html> |
| [ref-005](ref-005.md) | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | 논문 | medium | 2026-09-24 | <https://arxiv.org/abs/2005.07371> |
| [ref-006](ref-006.md) | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-09-24 | <https://arxiv.org/abs/1705.10868> |
| [ref-007](ref-007.md) | NIST | Performance of Collaborative Robot Systems | 미확인 | 정부·연구기관 | medium | 2026-09-24 | <https://www.nist.gov/programs-projects/performance-collaborative-robot-systems> |
| [ref-008](ref-008.md) | NIST | ARIAC Documentation | 미확인 | 정부·연구기관 | high | 2026-09-25 | <https://pages.nist.gov/ARIAC_docs/en/latest/> |
| [ref-009](ref-009.md) | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://design.ros2.org/articles/ros2_dds_security.html> |
| [ref-010](ref-010.md) | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://design.ros2.org/articles/ros2_threat_model.html> |
| [ref-011](ref-011.md) | ISO/IEC | ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) | 2024-03 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/85557.html> |
| [ref-012](ref-012.md) | ISO/IEC | ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) | 2024 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/85558.html> |
| [ref-013](ref-013.md) | OpenEPCIS | EPCIS 2.0 and EPCIS 1.2 \| OpenEPCIS Docs | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://openepcis.io/docs/epcis/> |
| [ref-014](ref-014.md) | GS1 | Core Business Vocabulary (CBV) Standard | 미확인 | 표준 | medium | 2026-09-25 | <https://ref.gs1.org/standards/cbv/> |
| [ref-015](ref-015.md) | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf> |
| [ref-016](ref-016.md) | GS1 | Serial Shipping Container Code (SSCC) | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/standards/id-keys/sscc> |
| [ref-017](ref-017.md) | GS1 Korea(대한상공회의소 유통물류진흥원) | SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 | 2019-09 | 표준 | medium | 2026-09-25 | <http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf> |
| [ref-018](ref-018.md) | GS1 | GS1 Logistic Label Guideline | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf> |
| [ref-019](ref-019.md) | GS1 | Global Returnable Asset Identifier (GRAI) | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/standards/id-keys/grai> |
| [ref-020](ref-020.md) | GS1 | Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal) | 미확인 | 표준 | medium | 2026-09-25 | <https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods-> |
| [ref-021](ref-021.md) | GS1 | EPC Tag Data Standard | 미확인 | 표준 | medium | 2026-09-25 | <https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf> |
| [ref-022](ref-022.md) | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | <https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf> |
| [ref-023](ref-023.md) | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/integration_workcells.html> |
| [ref-024](ref-024.md) | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 2009 | 논문 | medium | 2026-09-25 | <https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864> |
| [ref-025](ref-025.md) | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 2015 | 표준 | medium | 2026-09-25 | <https://ieeexplore.ieee.org/document/7084073/> |
| [ref-026](ref-026.md) | IEEE | IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology | 2022 | 표준 | medium | 2026-09-25 | <https://standards.ieee.org/standard/1872_2-2021.html> |
| [ref-027](ref-027.md) | Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G. | KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents | 2018 | 논문 | medium | 2026-09-25 | <https://ai.uni-bremen.de/papers/beetz18knowrob.pdf> |
| [ref-028](ref-028.md) | Beßler, D. 외 | Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents | 2021 | 논문 | medium | 2026-09-25 | <https://arxiv.org/pdf/2011.11972> |
| [ref-029](ref-029.md) | McDermott, D. 외 | PDDL - The Planning Domain Definition Language | 1998 | 논문 | medium | 2026-09-25 | <https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language> |
| [ref-030](ref-030.md) | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-09-25 | <https://www.w3.org/TR/vocab-ssn/> |
| [ref-031](ref-031.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md> |
| [ref-032](ref-032.md) | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-25 | <https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN> |
| [ref-033](ref-033.md) | MassRobotics | Autonomous Mobile Robot Standards Published by MassRobotics | 2021-05 | 표준 | medium | 2026-09-25 | <https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/> |
| [ref-034](ref-034.md) | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 미확인 | 표준 | medium | 2026-09-25 | <https://reference.opcfoundation.org/specs/OPC-40010-1> |
| [ref-035](ref-035.md) | Plattform Industrie 4.0 | Information Model for Capabilities, Skills & Services | 2022-11 | 정부·연구기관 | medium | 2026-09-25 | <https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html> |
| [ref-036](ref-036.md) | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 2022 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.09632> |
| [ref-037](ref-037.md) | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | 논문 | low | 2026-09-25 | <https://arxiv.org/abs/2307.00827> |
| [ref-038](ref-038.md) | Vieira da Silva, L. M., Köcher, A., & Fay, A. | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2022-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.10900> |
| [ref-039](ref-039.md) | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/task_types.html> |
| [ref-040](ref-040.md) | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html> |
| [ref-041](ref-041.md) | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | 논문 | medium | 2026-09-25 | <https://www.nature.com/articles/s41598-025-16649-3> |
| [ref-042](ref-042.md) | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. | A survey of ontology-enabled processes for dependable robot autonomy | 2024-07 | 논문 | medium | 2026-09-25 | <https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full> |
| [ref-043](ref-043.md) | 신민종, 한영석, 정재윤 | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 2024 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560> |
| [ref-044](ref-044.md) | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | <https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl> |
| [ref-045](ref-045.md) | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | <https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl> |
| [ref-047](ref-047.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg> |
| [ref-048](ref-048.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg> |
| [ref-049](ref-049.md) | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg> |
| [ref-050](ref-050.md) | Auto-ID Labs Korea(세종대학교), Byun, J. | Oliot EPCIS for GS1 EPCIS/CBV 2.0.0 (GitHub JaewookByun/epcis README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/JaewookByun/epcis> |
| [ref-051](ref-051.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema> |
| [ref-052](ref-052.md) | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/VDA5050/VDA5050/blob/main/README.md> |
| [ref-053](ref-053.md) | NVIDIA Research (NVlabs) | progprompt-vh — ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/NVlabs/progprompt-vh> |
| [ref-054](ref-054.md) | Singh, I. 외 | ProgPrompt: Generating Situated Robot Task Plans using Large Language Models | 2022-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2209.11302> |
| [ref-055](ref-055.md) | Brown University H2R Lab | Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/h2r/Lang2LTL> |
| [ref-056](ref-056.md) | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2302.11649> |
| [ref-057](ref-057.md) | Tellex, S. 외 | Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation | 2011-08 | 논문 | medium | 2026-09-25 | <https://ojs.aaai.org/index.php/AAAI/article/view/7979> |
| [ref-058](ref-058.md) | Cohen, V., Liu, J. X., Mooney, R., Tellex, S., & Watkins, D. | A Survey of Robotic Language Grounding: Tradeoffs between Symbols and Embeddings | 2024-08 | 논문 | medium | 2026-09-25 | <https://www.ijcai.org/proceedings/2024/885> |
| [ref-059](ref-059.md) | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2411.09022> |
| [ref-060](ref-060.md) | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | <https://doi.org/10.1177/20552076261437181> |
| [ref-061](ref-061.md) | Izzo, R. A., Bardaro, G., & Matteucci, M. (Politecnico di Milano AIRLab) | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 2024-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2403.12761> |
| [ref-062](ref-062.md) | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/CubiCasa/CubiCasa5k> |
| [ref-063](ref-063.md) | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/1904.01920> |
| [ref-064](ref-064.md) | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 2019 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/zlzeng/DeepFloorplan> |
| [ref-065](ref-065.md) | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 2017 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/art-programmer/FloorplanTransformation> |
| [ref-066](ref-066.md) | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 2021 | 오픈소스 문서 | medium | 2026-09-25 | <https://floorplancad.github.io/> |
| [ref-067](ref-067.md) | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2105.07147> |
| [ref-068](ref-068.md) | Voxel51 (Hugging Face) | Voxel51/FloorPlanCAD · Datasets at Hugging Face | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://huggingface.co/datasets/Voxel51/FloorPlanCAD> |
| [ref-069](ref-069.md) | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 2023 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/MLSTRUCT/MLStructFP> |
| [ref-070](ref-070.md) | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 2024 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/SizheHu/Raster-to-Graph> |
| [ref-071](ref-071.md) | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 2025-08 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/m-agour/ResPlan> |
| [ref-072](ref-072.md) | van Engelenburg, C. 외 (MSD) | msd — README (MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes) | 2024 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/caspervanengelenburg/msd> |
| [ref-073](ref-073.md) | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 2025-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2503.22346> |
| [ref-074](ref-074.md) | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465> |
| [ref-075](ref-075.md) | de las Heras, L.-P., Terrades, O. R., Robles, S., & Sánchez, G. | CVC-FP and SGT: a new database for structural floor plan analysis and its groundtruthing tool | 2015 | 논문 | medium | 2026-09-25 | <https://www.researchgate.net/publication/270597635_CVC-FP_and_SGT_a_new_database_for_structural_floor_plan_analysis_and_its_groundtruthing_tool> |
| [ref-076](ref-076.md) | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 2024-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2409.12842> |
| [ref-077](ref-077.md) | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 2025-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2508.07714> |
| [ref-078](ref-078.md) | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 2024-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2408.01526> |
| [ref-079](ref-079.md) | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/traffic-editor.html> |
| [ref-080](ref-080.md) | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html> |
| [ref-081](ref-081.md) | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2023-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2308.05443> |
| [ref-082](ref-082.md) | Vega-Torres, M. A. (MigVega GitHub) | Ogm2Pgbm — README (Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/MigVega/Ogm2Pgbm> |
| [ref-083](ref-083.md) | Zhang, J. 외 | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2507.00552> |
| [ref-084](ref-084.md) | Zhang, J. (jiajiezhang7 GitHub) | osmAG-from-cad — README (CAD-to-osmAG pipeline) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/jiajiezhang7/osmAG-from-cad> |
| [ref-085](ref-085.md) | Braga, R. G., Tahir, M. O., Karimi, S., Dah-Achinanon, U., Iordanova, I., & St-Onge, D. | Intuitive BIM-aided robotic navigation and assets localization with semantic user interfaces | 2025-03-26 | 논문 | medium | 2026-09-25 | <https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1548684/full> |
| [ref-086](ref-086.md) | Palacz, W., Ślusarczyk, G., Strug, B., & Grabska, E. | Indoor Robot Navigation Using Graph Models Based on BIM/IFC | 2019 | 논문 | medium | 2026-09-25 | <https://www.researchgate.net/publication/333410520_Indoor_Robot_Navigation_Using_Graph_Models_Based_on_BIMIFC> |
| [ref-087](ref-087.md) | Google Research | SayCan (google-research/saycan README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/google-research/google-research/blob/master/saycan/README.md> |
| [ref-088](ref-088.md) | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2204.01691> |
| [ref-089](ref-089.md) | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/SMARTlab-Purdue/SMART-LLM> |
| [ref-090](ref-090.md) | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2309.10062> |
| [ref-091](ref-091.md) | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/Cranial-XIX/llm-pddl> |
| [ref-092](ref-092.md) | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2304.11477> |
| [ref-093](ref-093.md) | Huang, W., Abbeel, P., Pathak, D., & Mordatch, I. | Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022-07 | 논문 | medium | 2026-09-25 | <https://proceedings.mlr.press/v162/huang22a.html> |
| [ref-094](ref-094.md) | Huang, W. (language-planner 공식 저장소) | language-planner — Official Code for "Language Models as Zero-Shot Planners" (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/huangwl18/language-planner> |
| [ref-095](ref-095.md) | Google Research | Code as Policies: Language Model Programs for Embodied Control (google-research/code_as_policies README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/google-research/google-research/blob/master/code_as_policies/README.md> |
| [ref-096](ref-096.md) | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | 논문 | medium | 2026-09-25 | <https://repub.eur.nl/pub/107376/> |
| [ref-097](ref-097.md) | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | 논문 | medium | 2026-09-25 | <https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517> |
| [ref-098](ref-098.md) | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901> |
| [ref-099](ref-099.md) | Le-Anh, T., & de Koster, M. B. M. | A review of design and control of automated guided vehicle systems | 2006 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840> |
| [ref-100](ref-100.md) | Vis, I. F. A. | Survey of research in the design and control of automated guided vehicle systems | 2006 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459> |
| [ref-101](ref-101.md) | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/merschformann/RAWSim-O> |
| [ref-102](ref-102.md) | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-09-25 | <https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69> |
| [ref-103](ref-103.md) | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/> |
| [ref-104](ref-104.md) | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_demos> |
| [ref-105](ref-105.md) | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml> |
| [ref-106](ref-106.md) | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://cslc.koti.re.kr/> |
| [ref-107](ref-107.md) | 법제처 국가법령정보센터 | 물류시설의 개발 및 운영에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://www.law.go.kr/LSW/lsInfoP.do?lsId=000091> |
| [ref-108](ref-108.md) | 이문수, 채준재(로지스틱스연구) | AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 - | 2010 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142> |
| [ref-109](ref-109.md) | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2406.17003> |
| [ref-110](ref-110.md) | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://osrf.github.io/ros2multirobotbook/task_new.html> |
| [ref-111](ref-111.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json> |
| [ref-112](ref-112.md) | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | 표준 | medium | 2026-09-25 | <https://www.omg.org/spec/BPMN/2.0/About-BPMN> |
| [ref-113](ref-113.md) | Camunda | Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | 벤더 문서 | medium | 2026-09-25 | <https://docs.camunda.io/docs/components/concepts/messages/> |
| [ref-114](ref-114.md) | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111> |
| [ref-115](ref-115.md) | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 2023 | 논문 | medium | 2026-09-25 | <https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031> |
| [ref-116](ref-116.md) | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2603.15427> |
| [ref-117](ref-117.md) | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | high | 2026-09-25 | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd> |
| [ref-118](ref-118.md) | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | 표준 | high | 2026-09-25 | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd> |
| [ref-119](ref-119.md) | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/67480.html> |
| [ref-120](ref-120.md) | Boniardi, F., Valada, A., Mohan, R., Caselitz, T., & Burgard, W. | Robot Localization in Floor Plans Using a Room Layout Edge Extraction Network | 2019-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/1903.01804> |
| [ref-121](ref-121.md) | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2201.05588> |
| [ref-122](ref-122.md) | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 2024-03 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2403.01975> |
| [ref-123](ref-123.md) | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | 표준 | medium | 2026-09-25 | <https://scor.ascm.org/processes/fulfill/F1.3> |
| [ref-124](ref-124.md) | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | <https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW> |
| [ref-125](ref-125.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json> |
| [ref-126](ref-126.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json> |
| [ref-127](ref-127.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json> |
| [ref-128](ref-128.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json> |
| [ref-129](ref-129.md) | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | medium | 2026-09-25 | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd> |
| [ref-130](ref-130.md) | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | <https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL> |
| [ref-131](ref-131.md) | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 미확인 | 표준 | medium | 2026-09-25 | <https://reference.opcfoundation.org/specs/OPC-10031-4/6.2> |
| [ref-132](ref-132.md) | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231> |
| [ref-133](ref-133.md) | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | <https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281> |
| [ref-134](ref-134.md) | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | <https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291> |
| [ref-135](ref-135.md) | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 2025 | 표준 | medium | 2026-09-25 | <https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf> |
| [ref-136](ref-136.md) | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | 논문 | medium | 2026-09-25 | <https://www.mdpi.com/2076-3417/15/13/7235> |
| [ref-137](ref-137.md) | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 2025-01 | 기사 | low | 2026-09-25 | <https://news.mt.co.kr/mtview.php?no=2025012116183583251> |
| [ref-139](ref-139.md) | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | 표준 | medium | 2026-09-25 | <https://www.iso.org/standard/54497.html> |
| [ref-140](ref-140.md) | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 미확인 | 표준 | medium | 2026-09-25 | <https://scor.ascm.org/performance/reliability/RL.1.1> |
| [ref-141](ref-141.md) | WERC(Warehousing Education and Research Council) | WERC DC Measures Survey - 2025 | 2025 | 업계 보고서 | medium | 2026-09-25 | <https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf> |
| [ref-142](ref-142.md) | Computers & Industrial Engineering 게재 논문(저자 미확인) | Overall Equipment Effectiveness: consistency of ISO standard with literature | 2020 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527> |
| [ref-143](ref-143.md) | Project Production Institute | Little’s Law – A Practical Approach to Understanding Production System Performance | 미확인 | 업계 보고서 | medium | 2026-09-25 | <https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/> |
| [ref-144](ref-144.md) | Azadeh, K., de Koster, R., & Roy, D. | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019 | 논문 | medium | 2026-09-25 | <https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873> |
| [ref-145](ref-145.md) | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 2021 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/pii/S0307904X20305801> |
| [ref-146](ref-146.md) | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | <https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336> |
| [ref-147](ref-147.md) | Process Intelligence Solutions (PM4Py GitHub) | pm4py — Official public repository for PM4Py (Process Mining for Python) (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/process-intelligence-solutions/pm4py> |
| [ref-148](ref-148.md) | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | <https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json> |
| [ref-149](ref-149.md) | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 2015 | 논문 | medium | 2026-09-25 | <https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9> |
| [ref-150](ref-150.md) | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 미확인 | 기사 | low | 2026-09-25 | <https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html> |
| [ref-151](ref-151.md) | 박정수, 안영효(유통경영학회지) | 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구 | 2010 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387> |
| [ref-220](ref-220.md) | Pointr | IMDF from Floor Plan & CAD Conversion Services | 미확인 | 벤더 문서 | low | 2026-09-25 | <https://www.pointr.tech/technology/imdf> |
| [ref-221](ref-221.md) | Vega Torres, M. A., Braun, A., & Borrmann, A. | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 2024-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2408.15870> |
| [ref-222](ref-222.md) | Navitec Systems | Universal Fleet Control Software for AGVs & AMRs | 미확인 | 벤더 문서 | low | 2026-09-25 | <https://navitecsystems.com/universal-fleet-control/> |
| [ref-223](ref-223.md) | Boniardi, F., Caselitz, T., Kümmerle, R., & Burgard, W. | Robust LiDAR-based localization in architectural floor plans | 2017 | 논문 | medium | 2026-09-25 | <http://ais.informatik.uni-freiburg.de/publications/papers/boniardi17iros.pdf> |
| [ref-224](ref-224.md) | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 2024-08 | 논문 | medium | 2026-09-25 | <https://arxiv.org/abs/2408.01737> |
| [ref-225](ref-225.md) | Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S. | IFC2INDOORGML: An Open-Source Tool for Generating IndoorGML from IFC | 2022 | 논문 | medium | 2026-09-25 | <https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/> |
| [ref-226](ref-226.md) | 박근홍, 박병준, 이슬기(한국산학기술학회논문지) | BIM-건설로봇 통합 연구의 체계적 문헌고찰 (한국산학기술학회논문지 26(11), 218-225, DOI 10.5762/KAIS.2025.26.11.218) | 2025 | 논문 | medium | 2026-09-25 | <https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003269295> |
| [ref-227](ref-227.md) | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 2025-01 | 벤더 문서 | low | 2026-09-25 | <https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330> |
<!-- auto:references-index:end -->
```

### docs/open-questions.md

```markdown
---
title: "열린 질문"
type: questions
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](index.md) › 열린 질문

# 열린 질문

아직 해결되지 않은 질문의 목록이다. 질문마다 관련 영역, 제기일, 제기한 실행, 상태(열림 / 조사 중 / 해결 / 보류), 해결 시 링크를 둔다. 세 에이전트 모두 질문을 제기할 수 있고, 해결 판정은 내용 검증 에이전트가 한다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시한 뒤 여기에 올린다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 "분류 확장 제안"으로 여기에 기록한다.

중점 연구 트랙 전용 질문은 트랙의 질문 백로그에 두고, 여기에는 링크만 둔다. 이 표는 `data/open_questions.json` 에서 자동으로 만든다.

## 목록

<!-- auto:open-questions:start -->
| id | 질문 | 관련 영역 | 제기일 | 제기한 실행 | 상태 | 해결 시 링크 |
|---|---|---|---|---|---|---|
| oq-001 | 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-002 | 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-003 | 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-004 | IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-005 | 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-006 | CBV의 loading·unloading이 운송 수단 적재로 정의되어 있을 때 시설 안 로봇의 적재·운반·하역은 어떤 업무 단계(bizStep) 값이나 사용자 정의 어휘로 기록해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-007 | VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-008 | 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-009 | 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-010 | 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-011 | 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-012 | 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-013 | ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-014 | 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-015 | 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-016 | 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-017 | 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-018 | 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-019 | 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-020 | ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-021 | 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-022 | 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | 2026-09-25 | 2026-09-25-11 | 열림 | — |

상태별 건수: 열림 22건

**트랙 전용 질문(트랙 백로그)**

- 매뉴얼 기반 로봇 기능 온톨로지: [질문 백로그](tracks/manual-capability-ontology/question-backlog.md) (열린 질문 39건)
- 자연어 업무 지시 챗봇: [질문 백로그](tracks/nl-task-chatbot/question-backlog.md) (열린 질문 21건)
- 건축 도면 자동 인식: [질문 백로그](tracks/floorplan-recognition/question-backlog.md) (열린 질문 23건)
<!-- auto:open-questions:end -->
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```

### runs/2026-09-25-15/verification2.json

```json
{
  "run_id": "2026-09-25-15",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": []
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "세부영역 페이지 10절의 '8. 실시간 세계 상태·데이터 일관성' 항목: '… 현재 상태 표현으로서 배정 판단에 들어간다. [사실][^ref-230][^ref-041]'의 태그를 [추정]으로 내린다. 이유: f5는 상태 보고 필드만 기술하고 f19는 논문이 광고 능력과 운용 능력을 구분했다는 사실만 말한다. 이 값들이 배정 판단에 들어간다는 연결은 브리프에 없는 추론이므로 [사실]로 쓰면 태그를 올리는 것이다.",
    "세부영역 페이지 10절의 '13. 작업 배정 — MRTA' 항목: '실행 가능성 판정 결과를 배정기 독립 입력으로 넘기는 연구가 두 영역을 잇는다. [사실][^ref-236][^ref-152]'에서 [^ref-152]를 뺀다. 이유: ref-152(f33, 이동로봇 플릿 작업 배정 리뷰)는 실행 가능성 판정 결과를 배정기로 넘기는 연구가 아니다. ref-152를 이 페이지에 남기려면 f33의 1차 수정 문구 그대로 별도 문장을 둔다('이동로봇 플릿의 작업 배정 문제를 에너지 소비와 필요 로봇 수 최소화 관점에서 검토한 리뷰도 있다. [사실][^ref-152]'). 남기지 않으면 13절의 [^ref-152] 각주 정의와 프런트매터 sources는 그대로 둔다. ref-152는 분리된 주제 페이지(2026-09-25-area05-s8.md)에서 계속 인용되기 때문이다.",
    "세부영역 페이지 10절의 '9. 로봇·제조사 관제 연동' 항목: '팩트시트와 플릿 어댑터 설정이 제조사 능력 선언의 입구다. [사실]'은 해석이다. 태그를 [추정]으로 내리거나, 문장을 f1·f7 범위의 사실로 고쳐 쓴다(예: '팩트시트는 지원 동작·적재 명세를, 플릿 어댑터 설정은 수행 가능한 작업 유형·동작 이름을 선언한다. [사실][^ref-228][^ref-105]').",
    "세부영역 페이지 3절 마지막 문장('따라서 이 영역은 … 공통 기반으로 볼 수 있다. [의견]')과 9절 마지막 문장('… 포함하지 않는 것으로 본다. [의견]')에 의견의 주체를 밝힌다(예: 문장 안에 '구축자 의견으로는'을 넣는다). 이유: [의견]은 누구의 의견인지 밝혀야 한다(verifier.md 3절 항목 5).",
    "pages.json fixes_applied의 '원문 미열람 표기' 항목에서 'ref-236~139'를 'ref-236~ref-138, ref-152'로 바로잡는다. 이유: ref-139는 이번 실행의 출처가 아니다(ISO 22400-2). 반면 ref-152는 실제로 원문 미열람 표기가 돼 있는데 보고 문구에서 빠졌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인 / 2차 수정 후 재검증. 이번 실행은 원문 열람이 차단된 환경(mirror_only, raw.githubusercontent.com 만 열람 가능)에서 검증됐다. 확인 33건, 미확인 0건, 교차 확인 0건. 강등: 없음(f15·f33 은 문구 수정, f10 은 CSS 계열 부분 한정). 원문 미열람 출처: ref-025, ref-026, ref-027, ref-028, ref-029, ref-035, ref-038, ref-041, ref-042, ref-043, ref-229, ref-234, ref-236, ref-237, ref-238, ref-239, ref-240, ref-138, ref-152. 주의: VDA 5050 팩트시트·MassRobotics·Open-RMF·IDTA·CaSkMan·SSN 은 규격마다 한 발행 주체의 근거다. 화물 취급 가능 여부를 여러 규격을 대조해 정해야 한다는 판단(f29)과 능력–실행 연결의 두 방식(f30)은 추론이다. f16~f22·f28 은 제목 수준 재인용이고, 물류 로봇 매뉴얼에서 LLM 으로 능력 모델을 만든 공개 사례는 확인하지 못했다. oq-004 는 해결 불인정(국내 모듈 정보 모델 KS 존재만 부분 근거). 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 4건을 처리하도록 지시했다. 10절의 태그 상향 2건(8. 실시간 세계 상태·데이터 일관성, 9. 로봇·제조사 관제 연동 항목), 10절 13. 작업 배정 — MRTA 항목의 각주 불일치 1건(ref-152), 3·9절의 주체 없는 [의견] 2문장이다. 1차 수정 지시 15건은 페이지와 필드에 반영된 것을 확인했다. f15 SUMO 제외, f10 CSS 한정, f33 적용 분야 삭제, f13 재서술, 발행일·저자 정정, 원문 미열람 표기, 재인용 범위, f24 위치, 교차 규칙 연결, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 용어 대응, oq-004 유지, 트랙 반영 제안 반영이 이에 해당한다. [분류원문] 보존, 범위 경계 준수. 분리된 주제 페이지 4건은 원 절 내용을 옮긴 것으로 새 주장이 없다. 사소한 표기 의견: 7·8절 요약 문장('…로 나뉜다')은 서술자의 분류 정리이므로 [사실]보다 [의견]에 가깝다.",
  "retry_reason": null
}
```
