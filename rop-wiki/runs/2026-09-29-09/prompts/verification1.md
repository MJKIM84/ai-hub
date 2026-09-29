(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-09
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 7. 온톨로지 검증·변경 관리 (B. 로봇 온톨로지)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-29-09/target.json

```json
{
  "run_id": "2026-09-29-09",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 101,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 7,
    "area_name": "7. 온톨로지 검증·변경 관리",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=7"
}
```

### runs/2026-09-29-09/research.json

```json
{
  "run_id": "2026-09-29-09",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 7,
    "area_name": "7. 온톨로지 검증·변경 관리",
    "category": "B. 로봇 온톨로지"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 역량 질문·온톨로지 피트폴·버전 IRI·온톨로지 진화 용어 없음(형상 제약 언어·의미적 버전 관리·회귀 시험·모델 검사·온톨로지 채우기는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 역량 질문 기반 완전성 확인, 추론기·피트폴 스캐너·형상 검증 같은 자동 평가, 버전 식별·호환성 표기, 변경 표현·탐지·영향 분석 네 갈래 모두 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — OWL 2 버전 IRI, W3C SHACL, OOPS!, IDTA 서브모델 템플릿 버전·폐기 규칙, 지식 그래프 변경 언어 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-147 미반영, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]",
    "역량 질문(competency question)을 SPARQL 질의·테스트로 형식화해 온톨로지의 완전성과 정확성을 확인하는 방법과 데이터셋·로봇 적용 사례는 무엇인가? (섹션 4·6·8 겨냥)",
    "추론기 일관성 검사, 피트폴 스캐너(OOPS!), 형상 검증(SHACL) 같은 자동 평가 도구는 각각 무엇을 잡아내고 검증 보고서를 어떤 구조로 내는가? (섹션 6·7 겨냥)",
    "온톨로지와 서브모델 템플릿의 버전은 어떻게 식별하고 이전 판과의 호환·비호환·폐기를 어떻게 표기하는가(OWL 2 버전 IRI, IDTA 서브모델 템플릿 규칙)? (섹션 4·7 겨냥)",
    "온톨로지 변경을 표현·탐지하고 의존 자원에 미치는 영향을 분석하는 연구(온톨로지 진화, 변경 언어, 버전 비교, 재구성 허용성)는 무엇이 보고되었으며, 언어 모델을 검증에 쓰는 방법은 어디에 연결되는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)",
    "oq-147 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (섹션 6·11 겨냥)",
    "온톨로지 검증·변경 관리에서 ROP가 직접 맡을 것(역량 질문 목록·테스트 실행·검증 보고서·버전 식별·재검증 목록)과 제조사·표준 발행 기관에 맡길 것의 경계는 어디이며, 현장 유형별 사례와 국내 자료는 무엇인가? (섹션 5·9·10 겨냥, 한국 자료 우선)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Wiśniewski·Potoniec·Ławrynowicz·Keet(2018)는 온톨로지 개발에서 역량 질문(competency question) 사용을 촉진하기 위해 여러 도메인 온톨로지에 대한 역량 질문 234개와 그 SPARQL-OWL 번역을 공개하고, 언어·의미 분석으로 106개의 역량 질문 패턴을 46개의 SPARQL-OWL 질의 서명과 대응시켜 역량 질문의 형식화·실행·관리를 지원하는 벤치마크로 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-890"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '234 CQs와 여러 도메인의 온톨로지를 위한 SPARQL-OWL 번역'을 공개하고 106개 역량 질문 패턴을 46개 SPARQL-OWL 질의 서명과 비교 분석. 용도는 역량 질문의 형식화·실행·관리 지원과 테스트·벤치마크.",
      "as_of": "2018-11-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Martorana·Urgese·Tiddi·Schlobach(2025)의 OntoBOT 은 SOMA·DOLCE 를 확장해 가정용 개인 서비스 로봇의 작업·행동·환경·능력을 통합 표현하는 온톨로지이며, 역량 질문으로 평가하고 TIAGo·HSR·UR3·Stretch 네 로봇에 대해 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-891"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 노인·지원이 필요한 사람을 돕는 가정 내 개인 서비스 로봇을 대상으로 과제·행동·환경·능력을 통합 표현하고 '형식적 추론을 지원'하며, '역량 질문을 통해 평가'하고 네 가지 구체화된 에이전트(TIAGo, HSR, UR3, Stretch)에서 검증.",
      "as_of": "2025-09-26",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "고영만 외(한국문헌정보학회지 49권 3호, 2015)는 학술용어사전 STNet 에 온톨로지 구조를 도입하면서 Pellet 추론기로 TBox 를 검증해 생성한 추론규칙이 모두 참임을 확인하고 SPARQL 검색 시나리오로 의미 검색 성능을 평가했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 검증 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-899"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '추론 엔진(Pellet)을 통해 TBox 검증을 수행한 결과 본 연구에서 생성한 추론규칙이 모두 참으로 나타났으며' 키워드 검색으로 파악하기 힘든 복잡한 검색 시나리오를 SPARQL 질의로 평가.",
      "as_of": "2015",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "서로 다른 세 발행 주체(포즈난 공과대학교·케이프타운 대학교 연구진의 역량 질문 데이터셋, 암스테르담 자유대학교 연구진의 OntoBOT, 국내 문헌정보학 연구진의 STNet)가 역량 질문 또는 SPARQL 질의 실행과 추론기 검증으로 온톨로지의 완전성·정확성을 확인하는 방식을 각각 보고해, 이 영역의 역량 질문·질의 기반 검증이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-890",
        "ref-891",
        "ref-899"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "f1(역량 질문→SPARQL-OWL 데이터셋), f2(역량 질문으로 로봇 온톨로지 평가), f3(Pellet TBox 검증과 SPARQL 시나리오)을 종합. 세 출처는 발행 기관·국가가 다르고 서로 인용 관계가 아니다.",
      "as_of": "2025-09-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Poveda-Villalón·Gómez-Pérez·Suárez-Figueroa(IJSWIS, 2014)의 OOPS!(OntOlogy Pitfall Scanner!)는 기술 논리에 익숙하지 않은 도메인 전문가를 위해 온톨로지의 모델링 결함(피트폴)을 온라인에서 탐지하는 도구로, 693개 이상의 온톨로지를 경험적으로 분석해 만든 카탈로그를 구조·기능·사용성 프로파일링 차원으로 분류하고 피트폴마다 심각·중요·경미의 중요도를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-889"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '온톨로지에서 결함을 탐지하기 위한 도구'로 693개 이상 온톨로지를 분석한 카탈로그를 구조적·기능적·사용성 프로파일링 차원으로 분류하고 각 피트폴에 중요도(critical·important·minor)와 탐지된 온톨로지 수를 포함.",
      "as_of": "2014-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "W3C 형상 제약 언어(SHACL) 권고안(2017-07-20)은 데이터 그래프를 형상 그래프의 조건 집합으로 검증하는 언어이며, 검증 보고서는 적합 여부(sh:conforms), 개별 결과(sh:result), 심각도(sh:resultSeverity: Violation·Warning·Info)와 초점 노드·경로·값·원인 형상을 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-887"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문: 'RDF 그래프를 조건의 집합으로 검증하는 언어'. 검증 결과는 sh:conforms(부울), sh:result, sh:resultSeverity(sh:Violation·sh:Warning·sh:Info), sh:focusNode·sh:resultPath·sh:value·sh:sourceShape 로 구성.",
      "as_of": "2017-07-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 작업에 대한 에이전트 자격·전제조건을 검사하고 SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다.",
      "tag": "사실",
      "source_ids": [
        "ref-885"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SPARQL 로 에이전트 자격·전제조건 검사, SHACL 형상으로 역할 기반 권한·오버라이드 승인 정책 검증, Fundació Ave Maria 의료센터 시뮬레이션 시나리오(임상 배치 아님). (재인용: 2026-09-29-08)",
      "as_of": "2025-04-30",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "서로 다른 두 발행 주체(W3C 의 SHACL 권고안, 그리스 연구진의 HERON)가 형상 제약 검증을 각각 정의하고 로봇 온톨로지 정책 검증에 적용해, 온톨로지 인스턴스 데이터의 제약 검증 수단으로서 SHACL 이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-887",
        "ref-885"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "f6(W3C 권고안의 검증 보고서 구조)과 f7(HERON 의 SHACL 정책 검증)을 종합. W3C 원문을 이번 실행에서 열었고 HERON 은 이전 실행에서 전문을 연 동료심사 논문이다.",
      "as_of": "2025-04-30",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성한 뒤 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행하고 사람이 최종 검토·수정만 하게 하여, 온톨로지 검증 단계에 자동 검사와 사람 검토를 결합했다.",
      "tag": "사실",
      "source_ids": [
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토. (재인용: 2026-09-29-08)",
      "as_of": "2024-10-18",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "Alharbi·Tamma·Payne·de Berardinis(2026)는 개방형(KimiK2·Llama 3.1·3.2)과 폐쇄형(Gemini 2.5 Pro·GPT 4.1) 언어 모델이 생성한 역량 질문을 가독성·입력 텍스트 관련성·구조적 복잡성 지표로 여러 도메인에서 평가해, 모델의 생성 프로필이 사용 사례에 따라 뚜렷이 달라진다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-898"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 전통적으로 수작업이던 역량 질문 생성을 생성형 AI 로 자동화; '가독성, 입력 텍스트와의 관련성, 생성된 질문의 구조적 복잡성' 지표; 'LLM 성능이 사용 사례에 의해 형성된 뚜렷한 생성 프로필을 반영'. 사람 검토 필요성은 초록에 명시되지 않음.",
      "as_of": "2026-04-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "W3C OWL 2 구조 명세 2판(2012-12-11)은 온톨로지를 온톨로지 IRI 로 식별하고 특정 판을 버전 IRI 로 구분하며 같은 온톨로지 시리즈에서 정확히 하나의 버전만 현재 버전으로 보고, 온톨로지 주석 owl:priorVersion(이전 판 IRI)·owl:backwardCompatibleWith(호환되는 이전 판)·owl:incompatibleWith(양립 불가능한 이전 판)로 판 사이 관계를 표기한다.",
      "tag": "사실",
      "source_ids": [
        "ref-886"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.1절: ontology IRI 는 온톨로지를, version IRI 는 특정 버전을 식별하며 '각 온톨로지 시리즈에서 정확히 하나의 버전이 현재 버전으로 간주'. 3.5절: owl:priorVersion·owl:backwardCompatibleWith·owl:incompatibleWith 정의.",
      "as_of": "2012-12-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "IDTA 서브모델 템플릿 공식 저장소 README 는 템플릿을 published·deprecated 폴더로 관리하고 판을 주버전·리비전·버그 수정으로 표기하며, 새 판 발행 6개월 뒤 이전 판을 deprecated 로 옮기되 그 템플릿은 계속 유효하나 버그 수정·개선·갱신을 더 제공하지 않는다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-894"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 'After six months from the publication of a new version of a Submodel Template (SMT), the previous version will be moved to the deprecated folder.' 폐기 템플릿은 사용 가능하나 유지보수되지 않음. Technical Data 2.0.1 = 주버전 2·리비전 0·패치 1.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "서로 다른 두 발행 주체(W3C, IDTA)가 온톨로지와 서브모델 템플릿의 판 식별자와 이전 판과의 호환·폐기 관계 표기를 각각 정의해, '판 식별자 + 이전 판 관계 명시'가 온톨로지·모델 버전 관리의 관행으로 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-886",
        "ref-894"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "f11(OWL 2 버전 IRI·이전 판 주석)과 f12(IDTA 주버전·리비전·deprecated 규칙)를 종합. 두 출처 모두 이번 실행에서 원문을 열었고 발행 주체가 다르다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Zablith 외(The Knowledge Engineering Review, 2013)의 프로세스 중심 서베이는 온톨로지 진화(ontology evolution)를 도메인 변화나 정보 시스템 요구에 대응해 온톨로지를 최신으로 유지하는 일로 정의하고, 전형적 접근이 자연어 처리·추론 등 여러 분야 기법을 결합한 다단계 과정으로 설계된다고 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-888"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '온톨로지 진화는 도메인 변화 또는 정보 시스템 요구사항에 대응하여 온톨로지를 유지하는 것을 목표'로 하며 자연언어처리와 추론 등 기법을 결합한 다단계 프로세스 접근. 단계 이름은 초록 페이지에서 확인하지 못함.",
      "as_of": "2013-08-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Hegde 외(Database, 2025)의 지식 그래프 변경 언어 KGCL 은 온톨로지·지식 그래프의 변경을 '동의어 추가'·'계층 재배치' 같은 통제 자연어 명령으로 요청하거나 기술하는 표준 데이터 모델로, 패치·diff 개념을 빌려 미래 변경 요청과 기존 변경 기술에 모두 쓰이며 GitHub 온톨로지 저장소 자동화 에이전트와 BioPortal 변경 요청 인터페이스로 구현되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-892"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'add synonym 'arm' to 'forelimb'' 같은 고수준 명령으로 변경을 요청·기술하는 표준 데이터 모델; 적용 패치와 diff 개념; GitHub 온톨로지 저장소 통합 에이전트, BioPortal UI 변경 요청. 영향 분석·감사는 초록에 없음.",
      "as_of": "2024-09-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Qiang·Taylor·Wang(2024, 2026 개정)의 OM4OV 는 온톨로지 매칭 시스템을 온톨로지 버전 간 변경 비교에 재사용할 수 있지만 확장 없이는 왜곡된 측정을 낸다고 분석하고, 기존 정렬을 활용해 후보를 줄이는 교차 참조 메커니즘을 더한 버전 비교 프레임워크를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-893"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'OM systems can be effectively reused for OV tasks, but without the necessary extensions, can produce skewed measurements'; Agent-OM 기반에 cross-reference 메커니즘 도입. 정량 결과는 초록에 없음.",
      "as_of": "2026-08-31",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "서로 다른 세 발행 주체(Zablith 외의 유럽 연구진 서베이, Hegde 외의 생물의학 온톨로지 연구진, 호주 국립대학교 계열 Qiang 외)가 온톨로지 변경의 정의·표현·탐지를 각각 다루어, 온톨로지 변경 관리가 별도 연구 분야로 존재함이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-888",
        "ref-892",
        "ref-893"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "f14(진화 서베이), f15(변경 언어), f16(버전 비교)을 종합. 세 출처는 기관·주제가 다르고 상호 재게시가 아니다. 다만 세 출처 모두 로봇 능력 온톨로지를 다루지는 않는다.",
      "as_of": "2026-08-31",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "Eichelberger·Weber(2024)는 2024년 2월 기준 IDTA 가 발표한 84개 명세 가운데 18개를 중간 메타모델로 변환해 5만 줄 이상의 API 코드·테스트를 자동 생성했으나 명세의 문법적 변동과 문제 때문에 수동 개입이 필요했다고 보고해, 표준 명세 자체의 변동성이 이를 소비하는 시스템의 재검증 부담이 됨을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-895"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '모든 현재 IDTA 명세를 성공적으로 처리'해 50,000줄 이상 생성했으나 '문법적 변동성과 문제'로 수동 개입 필요; 84개 중 18개 명세 분석. 버전 표시 비율 같은 수치는 초록에 없음.",
      "as_of": "2024-06-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Osmani(2026)는 로봇 서비스 온톨로지(RoSO)를 구조적 일반지능 모델(SMGI)의 의미 계층으로 두고, 서비스 재구성 뒤에도 서비스 기술이 유효하게 남기 위한 정체성 보존 재구성 기준과 지역적으로 허용되는 갱신이 전역적으로도 허용되는 조합 조건을 제시해 런타임 변경의 허용 여부를 판단하는 거버넌스를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-900"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "초록: 'identity-preserving reconfiguration criteria, and compositional conditions under which locally acceptable updates remain globally admissible'; 서비스 기술이 'dynamically governable' 하게 됨. 단독 저자 프리프린트이며 실험·현장 적용은 초록에 없음.",
      "as_of": "2026-05-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "Nasir 외(2026)의 OntoKG-EQ 는 다섯 개의 고정된 역량 질문으로 정당화된 핵심 온톨로지가 모든 클래스·속성·형상 제약·지표를 통제하고, 각 답에 관찰·증거·출처까지 추적하는 설명을 붙여 검증된 그래프에서 결정론적으로 만들며, 17명 패널 연구에서 증거 묶음이 인지된 신뢰도와 완전성을 크게 높였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-896"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '다섯 개의 동결된 질문으로 정당화된 핵심 온톨로지'; 각 결과가 '관찰, 증거, 출처, 출처까지 추적하는 설명을 생성'; 17명 패널에서 '증거 묶음이 인지된 신뢰도와 완전성을 크게 증가'. 도메인은 신흥 주식시장 분석.",
      "as_of": "2026-09-08",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f21",
      "claim": "Abolhasani·Ba·He·Pan(2026)의 TRACE-KG 는 미리 정의한 온톨로지 없이 문맥이 풍부한 지식 그래프와 유도 스키마를 함께 만들면서 원문 근거에 대한 완전한 추적 가능성을 유지해, 사람 검토자가 자동 추출 결과를 원문과 대조해 검증할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-897"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: '미리 정의된 온톨로지를 가정하지 않고 문맥이 풍부한 지식 그래프와 유도된 스키마를 공동으로 구축'하며 '원본 근거에 대한 완전한 추적 가능성을 유지'. ICML 2026 워크숍 발표.",
      "as_of": "2026-06-15",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f22",
      "claim": "oq-147 관련: 추출한 지식 항목마다 원문 근거를 붙여 검토자가 대조하게 하는 구성은 일반 문서 지식 그래프 추출(f20·f21)과 능력 온톨로지 생성의 사람 최종 검토(f9)에서 확인되지만, 로봇 매뉴얼·URDF 에서 뽑은 능력 항목에 매뉴얼의 절·줄 위치를 붙여 확정·반려하는 공개 구현은 이번 조사에서도 확인되지 않아 oq-147 은 부분 진전에 그친다.",
      "tag": "추정",
      "source_ids": [
        "ref-896",
        "ref-897",
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f20(증거·출처 추적 설명), f21(원문 근거 완전 추적), f9(사람 최종 검토)를 종합. 세 출처 모두 로봇 매뉴얼을 대상으로 하지 않는다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f23",
      "claim": "VDA 5050 공식 저장소(main, 3.0.0 판)의 팩트시트 JSON 스키마는 팩트시트 자체의 version 을 필수 속성으로 두고 선택 속성 mobileRobotConfiguration 에 하드웨어·소프트웨어 버전을 담아, 로봇 펌웨어·소프트웨어 판이 바뀐 사실을 등록 데이터에서 읽을 수 있는 자리를 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "팩트시트 스키마 필수 속성에 version 포함, 선택 속성 mobileRobotConfiguration 에 하드웨어·소프트웨어 버전과 네트워크·배터리 매개변수. (재인용: 2026-09-29-07)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "확인한 출처 어디에도 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없으며, 판 식별·호환 표기(f11·f12), 변경의 표현·탐지(f15·f16), 재구성 허용 판단(f19), 펌웨어 판 보고 자리(f23)가 흩어져 있어 ROP 는 이들을 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-886",
        "ref-894",
        "ref-892",
        "ref-893",
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f11·f12·f15·f16·f19·f23 의 종합. 영향 분석(impact analysis)은 f14 서베이가 다루는 분야이나 로봇 능력 온톨로지 적용 사례는 확인하지 못함.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f25",
      "claim": "확인한 자료를 종합하면 7. 온톨로지 검증·변경 관리에서 ROP가 직접 맡을 범위는 능력 온톨로지의 역량 질문 목록과 그 SPARQL 테스트 실행 기록, SHACL 형상과 검증 보고서, 추론기 일관성 검사, 온톨로지 판 식별자와 이전 판 관계 표기, 변경 기술(변경 언어)과 영향받는 작업·현장의 재검증 목록이며, 원문 근거를 붙인 검토·확정 기록은 4. 이기종 로봇 등록의 검토·승인과 같은 기록을 공유해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-890",
        "ref-887",
        "ref-886",
        "ref-892"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f6·f11·f15 의 수단을 ROP 산출물로 묶은 리서치 에이전트의 종합. 어느 출처도 로봇 오케스트레이션 플랫폼의 책임 범위를 직접 말하지 않는다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "연계 대상: 로봇 펌웨어·소프트웨어의 릴리스 관리 자체와 표준 발행 기관의 템플릿 개정·폐기 일정은 분류 원문 19장의 로봇 자체 지능·제어와 업종·규격 측 소유 사항이므로, 이종 제조사를 잇는 ROP 는 팩트시트의 판 정보와 템플릿 폐기 통보를 받아 온톨로지 재검증을 촉발하는 데 그치고 펌웨어 검증과 템플릿 유지보수는 제조사·IDTA 에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-894"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f23(팩트시트의 하드웨어·소프트웨어 판)과 f12(IDTA 의 6개월 뒤 deprecated 규칙)를 경계 판단에 적용한 종합.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f27",
      "claim": "이 영역은 등록 검토·승인 기록을 주는 4. 이기종 로봇 등록, 검증 대상 어휘를 주는 5. 로봇 능력·작업 표현, 검증된 연결만 실행하는 6. 온톨로지 기반 시스템·로봇 연동을 앞뒤로 두고, 판 규칙은 21. 상호운용 표준·적합성과 57. 자산·소프트웨어 수명주기 관리, 테스트·형식 검증 방법은 54. 시험·형식 검증·벤치마크에 이어지며, 언어 모델로 역량 질문·온톨로지를 생성·검증하는 방법(f9·f10)은 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에도 연결된다.",
      "tag": "추정",
      "source_ids": [
        "ref-894",
        "ref-887",
        "ref-465",
        "ref-898"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9·f10·f12·f6 과 분류 원문 교차 규칙(매뉴얼 해석은 4·55번)에 근거한 연결 판단.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-886",
      "org": "W3C (OWL Working Group)",
      "title": "OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)",
      "published": "2012-12-11",
      "url": "https://www.w3.org/TR/owl2-syntax/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "OWL 2 구조 명세. 온톨로지 IRI·버전 IRI 의 관계와 owl:priorVersion·backwardCompatibleWith·incompatibleWith 주석을 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-887",
      "org": "W3C (RDF Data Shapes Working Group)",
      "title": "Shapes Constraint Language (SHACL)",
      "published": "2017-07-20",
      "url": "https://www.w3.org/TR/shacl/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "RDF 데이터 그래프를 형상 그래프의 조건으로 검증하는 W3C 권고안. 검증 보고서 구조(sh:conforms·sh:result·sh:resultSeverity)를 정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-888",
      "org": "Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review)",
      "title": "Ontology evolution: a process-centric survey",
      "published": "2013-08-28",
      "url": "https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "온톨로지 진화를 도메인·요구 변화에 대응하는 유지 활동으로 정의하고 다단계 과정으로 정리한 서베이. 초록 페이지만 열었다(전문 PDF 403).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-889",
      "org": "Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2))",
      "title": "OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation",
      "published": "2014-04",
      "url": "https://oa.upm.es/35873/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "온톨로지 모델링 결함을 탐지하는 온라인 도구 OOPS! 와 693개 이상 온톨로지 분석에 기반한 피트폴 카탈로그. UPM 기관 저장소의 초록을 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-890",
      "org": "Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M.",
      "title": "Competency Questions and SPARQL-OWL Queries Dataset and Analysis",
      "published": "2018-11-23",
      "url": "https://arxiv.org/abs/1811.09529",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "역량 질문 234개와 SPARQL-OWL 번역, 106개 질문 패턴과 46개 질의 서명의 대응을 공개한 데이터셋 논문(프리프린트 초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-891",
      "org": "Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam)",
      "title": "An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics",
      "published": "2025-09-26",
      "url": "https://arxiv.org/abs/2509.22434",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "가정용 개인 서비스 로봇의 작업·행동·환경·능력을 통합 표현하는 OntoBOT 을 역량 질문으로 평가하고 네 로봇에서 검증한 프리프린트(초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-892",
      "org": "Hegde, H. 외 (Database, Oxford)",
      "title": "A Change Language for Ontologies and Knowledge Graphs",
      "published": "2024-09-20",
      "url": "https://arxiv.org/abs/2409.13906",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "온톨로지·지식 그래프 변경을 통제 자연어 명령으로 요청·기술하는 표준 데이터 모델 KGCL(프리프린트 초록, Database 2025 게재).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-893",
      "org": "Qiang, Z., Taylor, K., & Wang, W.",
      "title": "OM4OV: Leveraging Ontology Matching for Ontology Versioning",
      "published": "2024-09-30",
      "url": "https://arxiv.org/abs/2409.20302",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "온톨로지 매칭 시스템을 버전 간 변경 비교에 재사용하는 프레임워크와 교차 참조 메커니즘(프리프린트 초록, 2026-08-31 v19).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-894",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "submodel-templates — IDTA Submodel Templates for AAS (README)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "IDTA 서브모델 템플릿 공식 저장소 README. published·deprecated 폴더, 주버전·리비전·버그 수정 표기, 새 판 6개월 뒤 이전 판 폐기 규칙을 적는다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/README.md",
      "source_unopened": true
    },
    {
      "id": "ref-895",
      "org": "Eichelberger, H., & Weber, A.",
      "title": "Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?",
      "published": "2024-06-20",
      "url": "https://arxiv.org/abs/2406.14470",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "IDTA 명세 18개를 메타모델로 변환해 API 코드·테스트를 생성한 모델 기반 접근과 명세의 문법적 변동 문제(프리프린트 초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-896",
      "org": "Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M.",
      "title": "OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying",
      "published": "2026-09-08",
      "url": "https://arxiv.org/abs/2609.08869",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "다섯 개 고정 역량 질문이 온톨로지를 통제하고 각 답에 출처까지의 증거 추적을 붙이는 지식 그래프. 17명 패널 평가(프리프린트 초록, 금융 도메인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-897",
      "org": "Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026)",
      "title": "Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation",
      "published": "2026-04-03",
      "url": "https://arxiv.org/abs/2604.03496",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 근거에 대한 완전한 추적 가능성을 유지하며 문맥 지식 그래프와 유도 스키마를 함께 만드는 프레임워크(프리프린트 초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-898",
      "org": "Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J.",
      "title": "Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models",
      "published": "2026-04-17",
      "url": "https://arxiv.org/abs/2604.16258",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "개방형·폐쇄형 언어 모델이 생성한 역량 질문을 가독성·관련성·구조 복잡성으로 평가한 다중 도메인 연구(프리프린트 초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-899",
      "org": "고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3))",
      "title": "구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구",
      "published": "2015",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "학술용어사전에 온톨로지를 도입하고 Pellet 추론기 TBox 검증과 SPARQL 검색 시나리오로 평가한 국내 연구(KCI 초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-900",
      "org": "Osmani, A.",
      "title": "From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance",
      "published": "2026-05-05",
      "url": "https://arxiv.org/abs/2605.08185",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇 서비스 온톨로지의 재구성 뒤 유효성 유지 조건과 지역·전역 허용성을 다룬 이론적 단독 저자 프리프린트(초록).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-10-18",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하는 방법.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-885",
      "org": "Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel)",
      "title": "HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics",
      "published": "2025-04-30",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "의료 로봇 상위 온톨로지 HERON. SPARQL 자격·전제조건 검사와 SHACL 정책 검증을 의료센터 물류·플릿 조정 시뮬레이션 시나리오로 시연.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-228",
      "org": "VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소",
      "title": "VDA5050/json_schemas/factsheet.schema (main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDA 5050 3.0.0 팩트시트 JSON 스키마. version 등 필수 속성과 하드웨어·소프트웨어 버전을 담는 선택 속성 mobileRobotConfiguration 을 정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
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
      "rationale": "섹션 3: f4(역량 질문·질의 기반 검증이 여러 곳에서 확인), f18(표준 명세 변동이 재검증 부담), f24(개정 시 영향·재검증 절차는 흩어져 있어 ROP 가 설계해야 함) / 섹션 4: f1(역량 질문·SPARQL-OWL), f5(피트폴·중요도), f6(형상 검증 보고서), f11(온톨로지 IRI·버전 IRI·이전 판 주석), f14(온톨로지 진화) / 섹션 5: 가정 — f2(OntoBOT, 네 로봇 역량 질문 평가, 현장 배치 아님을 명시), 병원 — f7(HERON 의료센터 시뮬레이션 정책 검증, 임상 배치 아님), 제조 공장·물류창고·상업 시설·실외 사례는 확인되지 않음을 서술 / 섹션 6: 역량 질문 검증 f1·f2·f3·f4, 자동 평가 f5·f6·f8, 언어 모델 결합 검증 f9·f10(교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 함께 연결), 버전·호환 표기 f11·f12·f13, 변경 표현·탐지·허용성 f15·f16·f17·f19, 원문 근거 검토 f20·f21·f22 / 섹션 7: f11(OWL 2), f6(SHACL), f5(OOPS!), f12(IDTA 서브모델 템플릿 규칙), f15(KGCL), f23(VDA 5050 팩트시트 판 정보) / 섹션 8: f1, f2, f5, f14, f15, f16, f18, f19, f20, f21, 국내 f3 / 섹션 9: f25(직접 범위: 역량 질문 목록·테스트 기록·형상·검증 보고서·판 식별·재검증 목록), f26(연계 대상: 펌웨어 릴리스·템플릿 폐기 일정) / 섹션 10: f27 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리, 63. 병원·의료(f7), 65. 가정·공동주택(f2) / 섹션 11: 기존 oq-147(f22 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 57. 자산·소프트웨어 수명주기 관리 페이지에 f12·f23 반영, 54. 시험·형식 검증·벤치마크 페이지에 f1·f6 반영, 트랙 manual-capability-ontology 단계 5(완전성·정확성 검증)에 f1·f4·f5·f6 참고, 단계 6(변경 관리)에 f11·f12·f15 참고."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "역량 질문",
      "term_en": "Competency Question (CQ)",
      "definition": "온톨로지가 답할 수 있어야 하는 질문으로 요구사항을 적은 것으로, SPARQL 같은 질의로 형식화해 온톨로지가 요구를 충족하는지 검증하는 데 쓴다."
    },
    {
      "term_ko": "온톨로지 피트폴",
      "term_en": "Ontology Pitfall",
      "definition": "온톨로지 모델링에서 흔히 생기는 결함 유형으로, 피트폴 스캐너(OOPS!)가 구조·기능·사용성 차원의 카탈로그와 심각·중요·경미 중요도로 자동 탐지한다."
    },
    {
      "term_ko": "버전 IRI",
      "term_en": "Version IRI (owl:versionIRI)",
      "definition": "OWL 2 에서 같은 온톨로지 IRI 를 공유하는 온톨로지 시리즈 가운데 특정 판을 식별하는 IRI 로, 이전 판·호환·비호환 주석과 함께 온톨로지 버전 관리에 쓴다."
    },
    {
      "term_ko": "온톨로지 진화",
      "term_en": "Ontology Evolution",
      "definition": "도메인 변화나 정보 시스템 요구 변화에 대응해 온톨로지를 최신 상태로 유지하는 활동으로, 변경 감지·표현·적용·영향 관리를 포함하는 다단계 과정으로 다뤄진다."
    }
  ],
  "open_questions_new": [
    "로봇 능력 온톨로지에 대해 펌웨어·매뉴얼 개정을 감지해 영향받는 작업·현장을 찾고 재검증 대기열에 넣는 절차를 구현한 공개 구현이나 현장 사례가 있는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 57. 자산·소프트웨어 수명주기 관리, 4. 이기종 로봇 등록 | 근거: f24 | 종류: 일반",
    "분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 54. 시험·형식 검증·벤치마크, 36. 가상 시운전·실제 상황 재현 | 근거: f25 | 종류: 일반",
    "국내에서 역량 질문·추론기·SHACL 로 로봇 온톨로지를 검증하거나 버전을 관리한 연구·현장 사례가 있는가(이번 조사에서 확인된 국내 자료는 학술용어사전 온톨로지 검증 연구 1건이다)? | 관련 영역: 7. 온톨로지 검증·변경 관리, 5. 로봇 능력·작업 표현 | 근거: f3 | 종류: 일반",
    "IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? | 관련 영역: 7. 온톨로지 검증·변경 관리, 21. 상호운용 표준·적합성, 4. 이기종 로봇 등록 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 4,
    "unverified": [
      "Grüninger·Fox(1995) 'Methodology for the Design and Evaluation of Ontologies' 원문 PDF(토론토대학교 EIL)는 텍스트 추출이 되지 않고 Semantic Scholar API 는 429 로 서지를 확인하지 못해 출처에 넣지 않음 — 역량 질문의 원 제안자 인용은 스토리텔러가 쓰지 말 것",
      "Themis(UPM 온톨로지 공학 그룹의 요구사항 기반 온톨로지 검증 도구)는 도구 페이지를 열었으나 개발 기관·논문을 페이지에서 확인하지 못했고 논문 PDF·Semantic Scholar 페이지는 연결 끊김·빈 응답으로 미확인 — 출처 제외",
      "Köcher·Vieira da Silva·Fay 'Constraint Checking of Skills using SHACL'(INDIN 2021, 제조 스킬 검증)은 검색 결과 요약에서만 확인되고 HSU 페이지 404·Semantic Scholar 429 로 서지 미확인 — 제조 공장 현장 유형 사례 미확보",
      "IDTA 'How to write a SMT v1.1' 지침 PDF 와 Dibowski 'Full Traceability and Provenance for Knowledge Graphs'(FOIS 2024) PDF 는 텍스트 추출 실패, MDPI 'Grounded Knowledge Graph Extraction via LLMs'(Computers 15(3):178)는 403 — oq-147 의 로봇 문서 적용 사례 후보 미열람",
      "f14 Zablith 서베이의 진화 단계 이름은 초록 페이지에 없어 미확인(전문 PDF 403)",
      "f16 OM4OV·f18 Eichelberger 의 정량 결과(검색 요약의 'AASX 파일 44%만 대상 명세 판 표시')는 초록에 없어 claim 에 넣지 않음",
      "f2 OntoBOT 은 네 로봇에 대한 평가이며 가정 현장 배치 여부는 초록에서 확인하지 못함(site_type 은 출처가 밝힌 적용 대상 기준)",
      "f7 HERON·f9 Vieira da Silva·f23 팩트시트는 재사용 출처로 이번에 다시 열지 않음",
      "oq-147 미해결(f22 부분 진전)",
      "f4·f8·f13·f17 외 모든 finding 교차 확인 실패(표준·연구마다 발행 주체 한 곳)"
    ],
    "scope_violations": [
      "f26: 펌웨어 릴리스 관리와 표준 템플릿 유지보수는 분류 원문 19장의 로봇 자체 지능·제어와 규격 발행 기관 소유이므로 '연계 대상: '으로 표시함",
      "f7: HERON 의 역할 기반 권한 정책 검증은 51. 인증·권한·격리·48. 안전·위험 관리와 겹치므로 이 영역에서는 SHACL 검증 적용 사례로만 제안함",
      "f9·f10·f20·f21: 언어 모델 기반 온톨로지 생성·역량 질문 생성·지식 그래프 추출은 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f27)",
      "f18: IDTA 명세의 코드 생성은 21. 상호운용 표준·적합성의 범위와 겹치므로 표준 명세 변동이 재검증 부담이 된다는 근거로만 제안함",
      "f20: 금융 분석 도메인의 지식 그래프이므로 역량 질문 통제·증거 추적 구성의 선례로만 제안함"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-886~ref-900, 예약 구간 안) 상한 도달로 Frontiers 'A survey of ontology-enabled processes for dependable robot autonomy'(2024, 32편 검토 — 연 원문에 검증·변경 관리 서술이 없어 finding 으로 쓰지 않음), Themis, Köcher 외 SHACL 스킬 검증, IDTA SMT 작성 지침, Dibowski 추적성 논문, MDPI 근거 기반 추출 논문은 넣지 못했다. 원문 열람 15건(github_raw 1: IDTA 서브모델 템플릿 README, webfetch 14: W3C 권고안 2건, arXiv 초록 9건, Cambridge 초록, UPM 기관 저장소 초록, KCI 초록), 재사용 3건(ref-465·ref-885 는 2026-09-29-08, ref-228 은 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않아 fetched false). 교차 확인 4건(f4: 포즈난·케이프타운/암스테르담/국내, f8: W3C/그리스 연구진, f13: W3C/IDTA, f17: Zablith 외/Hegde 외/Qiang 외). 신뢰도 high 는 f8·f13 두 건(각각 이번 실행에서 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지)에는 완전성·정확성 쪽은 f1~f8(역량 질문·질의 실행, 추론기, 피트폴 스캐너, SHACL)과 f9·f10(언어 모델 결합 검증)으로, 변경 쪽은 f11~f19·f23(판 식별·호환 표기, 변경 표현·탐지, 재구성 허용성, 팩트시트 판 정보)으로 답했으며 결론은 '검증 수단과 판 표기 규칙은 여러 곳에서 확인되지만 로봇 능력 온톨로지에 대해 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차와 원문 절·줄 근거를 붙인 검토 구현은 확인되지 않았다'는 추정(f22·f24)이다. 분류 원문 1절의 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)를 정의한 출처는 찾지 못해 열린 질문으로 올렸다. 현장 유형: 가정(f2 OntoBOT 평가), 병원(f7 HERON 시뮬레이션 재인용)만 확인했고 제조 공장·물류창고·상업 시설·실외·기타 사례는 없다(제조 사례 후보 Köcher 외는 서지 미확인). 국내 자료는 KCI 논문(f3, 2015, 문헌정보학 온톨로지) 한 건이며 로봇 온톨로지 검증의 국내 사례는 찾지 못했다. 벤더 문서·벤더 주장 없음. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 용어집에 이미 있는 형상 제약 언어·의미적 버전 관리·회귀 시험·모델 검사·온톨로지 채우기·런타임 검증은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-147 은 f22 로 부분 진전만). 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 전체 885건과의 URL 중복을 대조하지 못했으므로 W3C OWL 2·SHACL·IDTA 저장소·arXiv 2406.07962 등은 퍼블리셔가 기존 id 로 합칠 수 있다."
  }
}
```

### docs/categories/robot-ontology/ontology-verification-and-change-management.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리"
type: area
category: "B. 로봇 온톨로지"
area_no: 7
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 7. 온톨로지 검증·변경 관리

# 7. 온톨로지 검증·변경 관리

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

온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **온톨로지 검증**: 역량 질문, 원문 대조, 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)로 완전성과 정확성을 확인한다
- **온톨로지 버전·변경 관리**: 문서·펌웨어 개정에 따라 능력 정의의 버전을 관리하고, 영향받는 작업·현장을 찾아 다시 검증한다

## 2. 핵심 질문

온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]

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

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md (요약)

```markdown
# 6. 온톨로지 기반 시스템·로봇 연동

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 885건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 235개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
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
- skill-interface: 스킬 인터페이스 (Skill Interface)
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

### docs/open-questions.md (요약: 대상 영역 [7] 에 걸린 1건 / 전체 154건)

```markdown
- oq-147 [열림] 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (영역 4, 45, 7)
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

### runs/2026-09-29-08/research.md

```markdown
# 리서치 브리프 2026-09-29-08

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-08 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 대분류 | B. 로봇 온톨로지 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 스킬 인터페이스·전제·유지·사후 조건·수행 가능 동작 용어 없음(스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·자산관리셸은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 능력 기반 로봇 후보 질의, 능력–실행 연결(능력→스킬→인터페이스), 온톨로지 기반 연동 자동화(모델 매핑·설정 초안 생성), 실행 시점 조건 판단(전제조건·상태 검사) 네 갈래 모두 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 능력·스킬·서비스 모델 온톨로지, IDTA 02020 능력 기술 서브모델, Open-RMF 사용자 정의 작업, VDA 5050 커넥터, OPC UA 스킬 실행 프로토콜, SkiROS2 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-150 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]
2. 작업 요구에 맞는 로봇·자원 후보를 온톨로지 질의로 찾고 근거와 함께 돌려주는 능력 매칭 접근에는 무엇이 있는가? (섹션 4·6·8 겨냥)
3. 온톨로지의 능력을 실제 로봇 명령·어댑터·스킬 인터페이스에 묶는 모델(능력·스킬·서비스 모델, 자산관리셸 능력 기술, OPC UA 스킬, Open-RMF 사용자 정의 작업)은 무엇을 정하며, 검토되지 않은 연결의 실행을 어떻게 막는가? (섹션 6·7 겨냥)
4. 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만드는 방법(모델 간 매핑, 계획 도메인 자동 생성, 모델 기반 생성)은 무엇이 보고되었는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)
5. 배터리·적재·문·승강기 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단하는 전제조건·정책 검사(SPARQL·SHACL, 전제·유지·사후 조건)는 어떻게 구현되는가? (섹션 4·6 겨냥)
6. oq-150 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (섹션 5·11 겨냥, 현장 유형 명시·한국 자료 우선)
7. 온톨로지 기반 연동에서 ROP가 직접 맡을 것(후보 질의·매핑·설정 초안·조건 검사)과 스킬 내부 구현·설비 API 에 맡길 것의 경계는 어디이며, 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Plattform Industrie 4.0 의 능력·스킬·서비스(CSS) 참조 모델을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, 스킬을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의하고, 모든 스킬이 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다. | ref-882 | 아니오 | medium | 2026-09-29 | — | — |
| f2 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 판은 생산 공정의 요구 능력과 가용 자원의 제공 능력을 비교하는 기반을 목적으로 하며, 능력을 속성(최대 속도·허용 공차 등), 제약(전제조건·불변·사후조건의 속성 제약과 순서·병렬의 전이 제약), 능력을 구현하는 스킬(기술·소프트웨어 모듈)의 세 관계로 모델링한다. | ref-229 | 아니오 | medium | 2026-09-29 | 제약 | 원문 미열람 |
| f3 | [사실] | 서로 다른 두 발행 주체(헬무트 슈미트 대학 계열 CaSkade 의 CSS 온톨로지, IDTA 의 능력 기술 서브모델)가 구현 독립적 능력과 실행 구현인 스킬을 분리하고 요구 능력–제공 능력 매칭을 모델의 목적으로 각각 정의해, 이 영역의 능력–실행 분리 구조가 한 곳 이상에서 확인된다. | ref-882, ref-229 | 예 | medium | 2026-09-29 | — | — |
| f4 | [사실] | Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. | ref-038 | 아니오 | medium | 2023-02-09 | — | — |
| f5 | [사실] | Dussard·Sarthou·Clodic(2023, 2025 개정)은 로봇이 보유한 물리 구성요소와 하위 능력으로부터 상위 능력을 온톨로지 추론으로 도출해 로봇이 어떤 작업에 배정될 수 있고 없는지를 스스로 판단하게 하고, 능력과 외부 객체 속성 사이의 어포던스 관계까지 추론하는 방법을 제안했다. | ref-249 | 아니오 | medium | 2025-09-10 | 수행 자원 | — |
| f6 | [사실] | Järvenpää·Siltala·Hylli·Lanz(Procedia CIRP 97, 2021)의 능력 매치메이킹 소프트웨어는 제품 요구와 자원 능력의 매칭을 자동화해 기존 생산 시스템이 새 제품 요구를 충족하는지 확인하고 대형 카탈로그에서 후보 자원을 찾으며, 외부 설계 도구와의 연동을 사례로 설명했다. | ref-890 | 아니오 | medium | 2021 | 수행 자원 | — |
| f7 | [사실] | 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)이 온톨로지 기반 능력 기술로 작업·요구에 맞는 로봇·자원 후보를 찾는 접근을 각각 보고해, 능력 기반 로봇 후보 질의가 한 곳 이상에서 확인된다. | ref-249, ref-890, ref-038 | 예 | medium | 2025-09-10 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 의 사용자 정의 작업 문서는 플릿 설정의 action_categories 로 지원 동작을 선언하고, add_performable_action 의 consider 콜백이 동작 설명을 보고 수락 여부를 정하며 set_action_executor 가 실행을 맡는 두 부분 API 를 정하고, 사용자 정의 동작 중 로봇은 읽기 전용 교통 참여자가 되어 교통 협상에 참여하지 않으며 문·승강기 사용은 사용자 정의 로직에서 바꿀 수 없다고 적는다. | ref-880 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f9 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 새 플릿 설정에 작업 능력(loop·delivery·clean)과 재충전 임계값, 배터리·기계 시스템 매개변수를 적게 하고 로봇 측 API 가 battery_soc 를 보고하게 하여, 능력 선언과 실행 시점 배터리 상태가 같은 설정·API 에 담긴다. | ref-153 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f10 | [사실] | Mayr·Rovida·Krueger 의 SkiROS2(IROS 2023)는 스킬을 전제·유지·사후 조건으로 정의하고 OWL 세계 모델(지식 베이스)로 세계 상태와 개체를 추론하며 확장 행동 트리로 작업 계획과 반응적 실행을 합쳐, 서로 다른 작업과 로봇 시스템 사이에서 스킬을 교체해 쓰는 사례(작업 계획·추론·다중 센서 통합·제조 실행 시스템 연결 등)를 보였다. | ref-881 | 아니오 | medium | 2023-06-29 | 제약 | — |
| f11 | [사실] | Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 특정 작업에 대한 에이전트 자격과 전제조건을 검사하고 SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 Fundació Ave Maria 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다. | ref-885 | 아니오 | medium | 2025-04-30 | 병원 / 제약 | — |
| f12 | [사실] | 서로 다른 세 발행 주체(룬드대학교의 SkiROS2, 그리스 연구진의 HERON, IDTA 의 능력 기술 서브모델)가 능력·스킬에 전제조건과 사후조건 같은 실행 조건을 붙이고 실행 전에 이를 검사하는 구조를 각각 두어, 이 영역의 실행 시점 조건 판단이 한 곳 이상에서 확인된다. | ref-881, ref-885, ref-229 | 예 | high | 2025-04-30 | 제약 | — |
| f13 | [사실] | Vieira da Silva 외(2023, 2024 개정)는 자산관리셸 서브모델과 능력·스킬 온톨로지가 서로 호환되지 않는 두 모델링 틀임을 분석하고, 비교 가능한 요소와 다른 요소를 가려낸 뒤 두 개의 단방향 선언적 매핑으로 이루어진 양방향 매핑 개념을 제시했다. | ref-037 | 아니오 | medium | 2024-04-28 | — | — |
| f14 | [사실] | Nabizada 외(IEEE CASE 2026 채택)는 네 가지 Industrie 4.0 표준으로 구조화한 자산관리셸 능력 모델에 완전한 PDDL 계획 문제를 자동 생성할 정보가 충분함을 보이고, PDDL 전용 서브모델 없이 분산 다중 자산관리셸 구조를 계획 문제로 변환하는 추출 알고리즘을 실험실 생산 시스템의 레이아웃 변형 4개 비교로 검증했다. | ref-201 | 아니오 | medium | 2026-06-01 | — | — |
| f15 | [사실] | Nagrath·Blender·Shaik·Schlegel(2022)은 서비스 로봇에서 소프트웨어 컴포넌트의 자산관리셸을 표준화된 디지털 데이터 시트로, 시스템 수준 자산관리셸을 런타임 운영 데이터 수집과 스킬 수준 명령의 창구로 쓰며, 자산관리셸을 손으로 만들지 않고 모델 기반 개발·조합 워크플로에서 생성·채운다고 보고했다. | ref-883 | 아니오 | medium | 2022-08-02 | — | — |
| f16 | [사실] | Sidorenko 외(FAIM 2021)는 스킬을 유한 상태 기계로 OPC UA 에 노출하고 Industrie 4.0 언어 메시지와 상호작용 상태 기계를 능동 자산관리셸 안에 모델링한 스킬 실행 상호작용 프로토콜을 제시해, 두 Industrie 4.0 컴포넌트가 계층적 제어 대신 동등 협력 방식으로 스킬을 함께 실행하는 예시를 시연했다. | ref-887 | 아니오 | medium | 2021-11-03 | 완료·인계 | — |
| f17 | [사실] | 서로 다른 세 발행 주체(Schlegel 연구진, SmartFactory-KL 계열 Sidorenko 연구진, CaSkade 의 CSS 온톨로지)가 능력 모델과 별도로 스킬 실행 인터페이스(OPC UA 서버·상태 기계·자산관리셸 스킬 명령)를 두고 능력→스킬→인터페이스 순으로 실제 명령에 묶는 구조를 각각 보고해, 이 영역의 능력–실행 연결 방식이 한 곳 이상에서 확인된다. | ref-883, ref-887, ref-882 | 예 | medium | 2022-08-02 | — | — |
| f18 | [사실] | ROS 2 패키지 vda5050_connector(1.1.1, BSD-3, VDA 5050 2.0 지원)는 MQTT 브리지·컨트롤러(주문 검증·실행·피드백)·어댑터의 세 부분으로 로봇을 VDA 5050 관제에 연결하며, 어댑터는 상태·노드 주행·VDA 동작의 세 핸들러를 플러그인으로 두어 로봇 플랫폼마다 사용자가 핸들러 패키지를 직접 만들어야 한다. | ref-886 | 아니오 | medium | 2026-09-29 | 수행 자원 | — |
| f19 | [추정] | 등록된 능력 모델에서 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 자동으로 만들었다고 직접 보고한 자료는 이번 조사에서 확인되지 않았으며, 확인된 것은 모델 간 선언적 매핑(f13), 자산관리셸에서 계획 도메인 자동 생성(f14), 모델 기반 자산관리셸 생성(f15), 어댑터의 고정된 핸들러 구조(f18·f9)이므로 이를 결합하면 능력 모델에서 핸들러·설정 초안을 만드는 경로가 가능해 보이나 사례는 미확인이다. | ref-037, ref-201, ref-886, ref-153 | 아니오 | low | 2026-09-29 | — | — |
| f20 | [사실] | 서로 다른 두 발행 주체(Open Robotics 의 플릿 어댑터·사용자 정의 작업 문서, ROS 패키지 색인의 vda5050_connector)가 로봇 연동 어댑터를 '플릿·능력 설정'과 '로봇별 핸들러·API 구현'의 두 부분으로 각각 구성해, 온톨로지로 자동화할 수 있는 부분(설정·매핑)과 손작업이 남는 부분(로봇별 구현)의 경계가 한 곳 이상에서 확인된다. | ref-880, ref-153, ref-886 | 예 | high | 2026-09-29 | 수행 자원 | — |
| f21 | [사실] | 창이종합병원 CHART 는 KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 와 함께 캐피털랜드 Galen 오피스 빌딩에서 개방 API 를 가진 KONE DX 급 승강기와 RMF 로 자율이동로봇이 여러 층을 오가는 시험 환경을 만들고, 청소·보안·배송·컨시어지 등 여러 업체 로봇으로 시험을 확대할 계획을 밝혔으나 업체 수와 정량 결과는 공개 페이지에 없다. | ref-889 | 아니오 | medium | 2026-09-29 | 기타 / 수행 자원 | — |
| f22 | [사실] | Valner 외(2022)의 타르투대학교병원 현장 시험에서는 프로그램 제어가 없는 병원 문을 카드 인식·근접 센서를 대신 작동시키는 서보 장치로 보완해야 했으므로, 온톨로지·설정만으로 연동되지 않는 설비가 남아 손작업 없는 연동의 한계를 보여준다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 제약 | 원문 미열람 |
| f23 | [사실] | 황선명(보안공학연구논문지 8권 1호, 2011)은 컴포넌트 온톨로지와 환경 온톨로지를 구축해 사람의 명령을 사전 정의된 작업에 연결하고 환경 온톨로지에서 매개변수를 얻어 필요한 컴포넌트 목록을 구성·실행하는 로봇 컴포넌트 동적 재구성 방법을 제안했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 기반 로봇 연동 연구다. | ref-888 | 아니오 | medium | 2011 | — | — |
| f24 | [사실] | Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하게 하여, 온톨로지 기반 연동의 앞 단계인 능력 모델 작성 부담을 줄이는 방법을 제안했다. | ref-465 | 아니오 | medium | 2024-10-18 | 완료·인계 | 원문 미열람 |
| f25 | [추정] | 확인한 자료를 종합하면 6. 온톨로지 기반 시스템·로봇 연동에서 ROP가 직접 맡을 범위는 능력 온톨로지 질의로 후보 로봇을 찾아 근거와 함께 돌려주는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안 생성, 실행 전 전제조건·정책 검사(배터리·문·승강기 상태)이며, 근거를 함께 돌려주는 설명 기능과 검토되지 않은 연결의 실행 차단은 확인한 출처 어디에도 명시되지 않아 ROP 가 따로 설계해야 할 요구로 보인다. | ref-882, ref-880, ref-886, ref-885 | 아니오 | low | 2026-09-29 | — | — |
| f26 | [추정] | 연계 대상: 스킬의 내부 구현과 상태 기계 실행(OPC UA 서버·로봇 SDK 쪽)과 승강기 제조사의 개방 API 자체는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 쪽이므로, 이종 제조사를 잇는 ROP 는 스킬 인터페이스 호출·상태 확인·완료 판정과 승강기 사용 요청·인계만 맡고 구현 성능은 제조사·설비 측에 맡겨야 할 것으로 보인다. | ref-887, ref-889, ref-882 | 아니오 | low | 2026-09-29 | 제약 | — |
| f27 | [추정] | 이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 어댑터·규격은 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성, 문·승강기 상태는 22. 설비·건물 시스템 연동, 후보 질의 결과는 25. 작업 배정 — MRTA, 실행 조건과 완료 판정은 29. 명령·작업 실행의 신뢰성과 18. 실시간 세계 상태·데이터 일관성에 이어지며, 언어 모델로 능력 온톨로지를 만드는 방법(f24)은 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에도 연결된다. | ref-880, ref-229, ref-885, ref-465 | 아니오 | low | 2026-09-29 | — | — |
| f28 | [추정] | oq-150 관련: Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서(f8·f9)로 확인되지만 문·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 oq-150 은 미해결로 남는다. | ref-880, ref-229, ref-153 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University) | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2023-02-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2209.10900 | 아니오 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택) | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 2026-06-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.02167 | 아니오 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2024-04-28 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2307.00827 | 아니오 |
| ref-249 | Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS) | Ontological Component-based Description of Robot Capabilities | 2025-09-10 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.07569 | 아니오 |
| ref-880 | Open Robotics (Programming Multiple Robots with ROS 2) | User-defined Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_userdefined.html | 아니오 |
| ref-881 | Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023) | SkiROS2: A skill-based Robot Control Platform for ROS | 2023-06-29 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.17030 | 아니오 |
| ref-882 | CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소 | CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README) | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/CaSkade-Automation/CSS | 아니오 |
| ref-883 | Nagrath, V., Blender, T., Shaik, N., & Schlegel, C. (Technische Hochschule Ulm) | Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots | 2022-08-02 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2208.01273 | 아니오 |
| ref-229 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0) | 미확인 | 표준 | medium | 2026-09-29 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-885 | Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel) | HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics | 2025-04-30 | 논문 | high | 2026-09-29 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/ | 아니오 |
| ref-886 | ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda) | vda5050_connector - ROS Package Overview | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://index.ros.org/p/vda5050_connector/ | 아니오 |
| ref-887 | Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo) | An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell | 2021-11-03 | 논문 | medium | 2026-09-29 | https://zenodo.org/records/5648095 | 아니오 |
| ref-888 | 황선명 (대전대학교, 보안공학연구논문지 8(1)) | 온톨로지 기반의 로봇 동적재구성에 관한 연구 | 2011 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001533055 | 아니오 |
| ref-889 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART) | Robot-Lift Integration Challenge \| Changi General Hospital | 미확인 | 정부·연구기관 | medium | 2026-09-29 | https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge | 아니오 |
| ref-890 | Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97) | Capability matchmaking software for rapid production system design and reconfiguration planning | 2021 | 논문 | medium | 2026-09-29 | https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/ | 아니오 |
| ref-153 | Open Robotics (Programming Multiple Robots with ROS 2) | Fleet Adapter Tutorial (integration_fleets_action_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-09-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-10-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2406.07962 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4(이기종 로봇 기능을 일관되게 기술할 방법 부재), f20(어댑터가 설정과 로봇별 구현으로 나뉘어 손작업이 남음), f22(설비가 프로그램 제어를 못 하면 온톨로지·설정만으로 연동되지 않음) / 섹션 4: f1(능력·스킬·서비스·스킬 인터페이스), f2(속성·제약·스킬, 전제조건·불변·사후조건), f10(전제·유지·사후 조건), f8(수행 가능 동작·action_categories), f5(구성요소 기반 능력 추론·어포던스) / 섹션 5: 병원 — f11(HERON 의료센터 시뮬레이션: 물류 운반·다중 로봇 조정, 임상 배치 아님을 명시), f22(타르투대학교병원 문 보완 장치), 기타 — f21(싱가포르 Galen 오피스 빌딩 승강기 연동 시험 환경), 제조 공장·물류창고 현장 사례는 확인되지 않음을 서술(f6·f14 는 생산 시스템 설계·실험실 수준) / 섹션 6: 능력 기반 후보 질의 f5·f6·f7, 능력–실행 연결 f1·f15·f16·f17·f8, 연동 자동화 f13·f14·f15·f19(자동 생성 사례 미확인은 추정), 실행 시점 조건 판단 f9·f10·f11·f12, 앞 단계 능력 모델 생성 f24(교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 함께 연결) / 섹션 7: f1(CSS 온톨로지), f2(IDTA 02020), f8·f9(Open-RMF 사용자 정의 작업·플릿 어댑터), f18(vda5050_connector), f16(OPC UA 스킬 실행 프로토콜), f10(SkiROS2) / 섹션 8: f4, f5, f6, f13, f14, f15, f16, f11, 국내 f23 / 섹션 9: f25(직접 범위: 후보 질의·매핑표·검토 승인 기록·설정 초안·전제조건 검사), f26(연계 대상: 스킬 내부 구현·승강기 API) / 섹션 10: f27 — 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 7. 온톨로지 검증·변경 관리, 18. 실시간 세계 상태·데이터 일관성, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 25. 작업 배정 — MRTA, 29. 명령·작업 실행의 신뢰성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 63. 병원·의료(f11·f22) / 섹션 11: 기존 oq-150(f28 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f8·f21 반영, 21. 상호운용 표준·적합성 페이지에 f2·f13·f18 반영, 25. 작업 배정 — MRTA 페이지에 f5·f7 반영, 트랙 manual-capability-ontology 단계 4(실행 연결)에 f1·f16·f17 참고. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 스킬 인터페이스 | Skill Interface | 능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다. |
| 전제·유지·사후 조건 | Pre-, Hold-, Post-condition | 스킬이 시작될 때 참이어야 하는 조건(전제), 실행 중 계속 유지되어야 하는 조건(유지), 끝난 뒤 성립해야 하는 조건(사후)으로 스킬을 정의해 실행 가능 여부 판단과 완료 확인에 쓰는 방식이다. |
| 수행 가능 동작 | Performable Action (Open-RMF perform_action) | Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다. |

## 열린 질문

새로 생긴 질문:

- 등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 20. 로봇·제조사 관제 연동, 4. 이기종 로봇 등록 | 근거: f19 | 종류: 일반
- Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 바꿀 수 없을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 28. 공용 자원·충전·에너지 최적화, 29. 명령·작업 실행의 신뢰성 | 근거: f8 | 종류: 일반
- 국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 25. 작업 배정 — MRTA | 근거: f23 | 종류: 일반
- 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? | 관련 영역: 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f13 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 5
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f6 탐페레 매치메이킹의 OWL 온톨로지·SPIN 규칙 구현 세부는 검색 결과 요약에서만 보였고 연 초록 페이지에 없어 claim 에 넣지 않음(Procedia CIRP ScienceDirect 원문 403)
    - f3 CSS 온톨로지와 IDTA 02020 은 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립성이 제한적임(신뢰도 medium 으로 둠)
    - f2 IDTA 02020 1.0 판 발행일 미확인(README 에 날짜 없음), f1·f8·f18·f21 출처 발행일 미확인
    - f11 HERON 은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 같은 구체 상태 조건은 전문에서 확인하지 못함
    - f14 AAS→PDDL 생성의 정량 결과와 f10 SkiROS2 의 실기 배치 결과는 초록에 없어 미확인
    - f16 Sidorenko 외 논문은 Zenodo 초록만 확인(상태 기계 세부 미확인)
    - MDPI Electronics 15(16):3562 'Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation'(배터리·층 접근 조건의 의미 기반 실행 가능성 추론)은 두 경로 모두 403 으로 열지 못해 넣지 않음 — 실행 시점 조건 판단의 핵심 후보 출처
    - Järvenpää 외 'Semantic rules for capability matchmaking'(IJCIM 2022, tandfonline)과 'development of an ontology for describing the capabilities of manufacturing resources'(Springer JIM 2018)는 403·인증 리다이렉트로 열지 못함
    - Plattform Industrie 4.0 CSS 토론 문서는 웹 페이지가 보안 검증으로 막히고 PDF 는 텍스트 추출이 되지 않아 CSS 온톨로지 README(ref-882)로 대신함 — 참조 모델 원문 미열람
    - RoboCaSk 온톨로지 저장소 raw README 는 404 로 확인하지 못해 f1 에 이름만 적음
    - f7·f17 외 능력 기반 후보 질의가 '근거와 함께' 후보를 돌려주는 설명 기능은 어느 출처에서도 확인하지 못함
    - oq-150 미해결(f28)
    - f3·f7·f12·f17·f20 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
- 범위 경계 위반 의심:
    - f26: 스킬 내부 구현·OPC UA 상태 기계 실행과 승강기 제조사 API 는 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어 연계 영역이므로 '연계 대상: '으로 표시함
    - f21: 승강기 개방 API 연동은 22. 설비·건물 시스템 연동의 범위와 겹치므로 이 영역에서는 온톨로지·플랫폼 기반 이기종 로봇의 층간 이동 시험 환경 사례로만 제안함
    - f11: HERON 의 역할 기반 권한·오버라이드 정책 검사는 48. 안전·위험 관리·51. 인증·권한·격리와 겹치므로 실행 시점 조건 판단 사례로만 제안함
    - f14·f6: 제조 생산 시스템 설계·계획 도메인 생성 연구는 이동로봇 플랫폼이 아니므로 능력 모델에서 실행 산출물을 자동 생성하는 방법의 선례로만 제안함
    - f24: 언어 모델 능력 온톨로지 생성은 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f27)
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-038~ref-890, 예약 구간 안) 상한 도달로 CSS 참조 모델 논문(arXiv 2209.09632), ETFA 능력·스킬 서베이(arXiv 2204.12908), MiR VDA 5050 어댑터 벤더 블로그, RoSO/SMGI(arXiv 2605.08185), 온톨로지 기반 로봇 사양 합성(arXiv 2602.05456), 국내 클라우드 기반 이기종 다중로봇 플랫폼(제어로봇시스템학회 2023, 온톨로지 언급 없음)은 열었으나 넣지 않았다. 원문 열람 15건(github_raw 2: CSS 온톨로지 README·IDTA 02020 README, webfetch 13: arXiv 초록 7건, PMC 전문 1건, Open-RMF 문서, ROS Index, Zenodo, KCI 초록, CGH 페이지, 탐페레 연구 포털), 재사용 3건(ref-153·ref-869·ref-465, 이전 브리프 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않음). 주의: 실행 컨텍스트가 예약한 ref-038~ref-905 구간은 같은 날 이전 실행 2026-09-29-07 이 ref-038·ref-037·ref-880·ref-881·ref-883 으로 낸 다른 URL 과 번호가 겹치므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 5건(f3: CaSkade·IDTA — 공통 참조 모델 파생이라 medium, f7: LAAS·탐페레·HSU, f12: 룬드·그리스 연구진·IDTA, f17: Schlegel 연구진·Sidorenko 연구진·CaSkade, f20: Open Robotics·ROS Index/InOrbit). 신뢰도 high 는 f12·f20 두 건(각각 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지로 새 로봇·새 시스템을 손작업 없이 연동)에는 f1·f2·f3(능력–스킬–인터페이스 분리와 요구/제공 매칭 모델), f5·f6·f7(능력 기반 후보 질의), f13·f14·f15(모델 매핑·계획 도메인·자산관리셸 자동 생성), f8·f18·f20(어댑터의 설정 부분과 로봇별 구현 부분), f9~f12(실행 조건 검사)로 답했으며 결론은 '능력 모델과 실행 인터페이스를 잇는 구조와 조건 검사는 여러 곳에서 확인되지만, 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성해 손작업을 없앤 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다'는 추정(f19·f25)이다. 현장 유형: 병원(f11 시뮬레이션, f22 타르투대학교병원 재인용), 기타(f21 싱가포르 오피스 빌딩)만 확인했고 제조 공장·물류창고·상업 시설·가정·실외 현장 사례는 없다(제조 관련 출처는 생산 시스템 설계·실험실 수준). 국내 자료는 KCI 논문(f23, 2011) 한 건이며 국내 운영 사례는 찾지 못했다. 벤더 문서 출처 없음(MiR 블로그는 출처 상한으로 제외). L. AI·학습 기술 관련 finding(f24)은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성은 실행 조건의 현재 상태 연결로만 제안했고 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 없다. 용어집에 이미 있는 스킬·능력 매칭·요구 능력·제공 능력·능력·스킬·서비스 모델·능력 기술 서브모델·형상 제약 언어·플릿 어댑터·어포던스·자산관리셸·계획 도메인 정의 언어·행동 트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-150 은 f28 로 부분 진전만).
```

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

### runs/2026-09-25-07/research.md

```markdown
# 리서치 브리프 2026-09-25-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-07 |
| 날짜 | 2026-09-25 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 7. 화물·재고·자산 식별과 추적 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- corr-001: 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 행이 2.0.0만 적고 현행판(3.0.0)이 없으며, 공식 저장소 원문을 열 수 있는데도 '원문 미열람'으로 표시됨
- corr-002: 섹션 1. 한 줄 정의 — 분류원문 문장의 수정 요청(정정 대상 아님, 반영하지 않을 근거 필요)
- 섹션 11. 열린 질문 — oq-007(3.0.0 loadId 형식 규정)의 근거가 3.0.0 상태 스키마로 재확인되지 않음
- 용어집 VDA 5050 항목의 한 줄 정의가 팩트시트(factsheet) 메시지 정의로 되어 있고 현행판 표시 없음(대상 페이지 밖, 갱신 후보)

## 조사 질문

1. 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]
2. corr-001 VDA 5050의 현행판은 무엇이며, 적재물 보고(state 메시지의 loads 배열과 loadId)가 3.0.0에도 유지되는가? (섹션 7 겨냥)
3. corr-001 공식 저장소의 2.0.0 태그·main 원문을 열면 7절 VDA 5050 행의 '원문 미열람' 표시를 어떻게 바꿔야 하는가? (섹션 7 겨냥)
4. corr-002 한 줄 정의에 바코드·RFID 식별 수단을 넣어 달라는 요청은 분류원문 보호 규칙에 비추어 반영 가능한가, 식별 수단은 페이지 어디에서 이미 다루는가? (섹션 1·4·6 겨냥)
5. oq-007 VDA 5050 3.0.0에서 loadId의 형식(SSCC 같은 GS1 키)을 정하거나 제약하는 규정이 있는가? (섹션 11 겨냥)
6. oq-005 VDA 5050 3.0.0의 발행 시점은 언제인가? (섹션 7 현행판 표기 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | corr-001 관련: VDA 5050 공식 GitHub 저장소 main 브랜치의 명세 제목은 'Version 3.0.0'이며, 저장소 README는 main 브랜치가 최신 발행판(현재 3.0.0)을 담는다고 밝힌다. | ref-031, ref-052 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | corr-001 관련: VDA 5050 3.0.0(main)의 state 스키마에도 선택 배열 loads가 있으며 loadId(바코드·RFID 등 고유 식별 번호, 식별 가능하나 아직 식별 전이면 빈 값), loadType, loadPosition, weight(kg), boundingBoxReference, loadDimensions를 담고, 로봇이 적재 상태를 판단할 수 없으면 배열을 생략한다. | ref-051 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f3 | [사실] | corr-001 관련: VDA 5050 공식 저장소 2.0.0 태그의 명세 마크다운은 머리에 'Version 2.0.0 RELEASE CANDIDATE, FOR REVIEW' 문구를 두고, state 메시지의 선택 배열 loads와 loadId·loadType·loadPosition·weight를 3.0.0과 같은 의미로 정의한다. | ref-022 | 아니오 | medium | 2022-01 | 작업 대상 | 원문 미열람 |
| f4 | [사실] | corr-001 관련: VDA 5050 3.0.0 명세는 pick 완료를 '적재물이 이동로봇에 들어오고 새 적재 상태를 보고함', drop 완료를 '적재물이 이동로봇을 떠나고 새 적재 상태를 보고함'으로 정의하고, 두 동작의 선택 파라미터로 lhd·stationType·stationName·loadType·loadId를 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f5 | [사실] | VDA는 2026년에 VDA 5050 3.0판을 발표해 자율도가 높은 이동로봇 통합을 위한 구역(zone) 개념 등을 더했으며, 정확한 발행일(2026-03-19 대 보도자료 2026-04 계열)은 여전히 확인되지 않았다. | ref-032, ref-052 | 아니오 | medium | 2026 | — | — |
| f6 | [의견] | corr-001 관련: 7절 VDA 5050 행은 현행판 3.0.0(공식 저장소 main 명세·state 스키마)과 2.0.0을 함께 적고, 열람 표시를 '공식 저장소 원문 확인(2.0.0은 태그의 RELEASE CANDIDATE 마크다운이며 VDA 게시 PDF와 일치 미확인)'으로 바꾸며, 적재물 식별 보고가 두 판 모두에 있다고 적는 것이 근거와 맞다. | ref-022, ref-031, ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [추정] | 이번 실행에서 연 VDA 5050 3.0.0 state 스키마의 loadId 설명은 형식을 바코드·RFID 예시로만 들 뿐 SSCC 같은 GS1 키를 지정하거나 제약하지 않으며, 식별 결과가 지시한 loadId와 다를 때의 보고 규칙은 열람 범위에서 확인되지 않았다. | ref-051, ref-031 | 아니오 | low | 2026-09-25 | 작업 대상 | — |
| f8 | [의견] | corr-002 관련: 한 줄 정의 문장은 분류원문이라 정정 대상이 아니므로 반영하지 않으며, 요청이 말한 식별 수단(GS1-128 바코드로 표시하는 SSCC, RFID 태그용 EPC 인코딩)은 정의를 바꾸지 않고도 이미 4절·6절에서 출처와 함께 다루고 있다. | ref-018, ref-021 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-25 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 예 |
| ref-018 | GS1 | GS1 Logistic Label Guideline | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf | 예 |
| ref-021 | GS1 | EPC Tag Data Standard | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/README.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | 7, 11 | corr-001 반영: f1·f2·f3·f4·f6 을 섹션 7 VDA 5050 행에(현행판 3.0.0 과 2.0.0 병기, 적재물 식별 보고가 두 판 모두에 있음, 열람 표시를 공식 저장소 원문 확인으로 교체하되 2.0.0 은 RELEASE CANDIDATE 태그 마크다운이라 게시 PDF 일치 미확인 명시, 각주 ref-031·ref-051 추가) / f5 는 현행판 표기 근거(발행일은 oq-005 로 미확인 유지) / f7 을 섹션 11 oq-007 항목 보강에(3.0.0 state 스키마 loadId 설명에 GS1 키 형식 규정 없음, 불일치 보고 규칙 미확인). corr-002 는 반영하지 않음: f8(분류원문 정의는 정정 대상 아님, 식별 수단은 4·6절에 이미 있음) — 섹션 1 변경 없음 |
| update | docs/glossary/vda-5050.md | — | 다음 실행 후보 겸 갱신 제안: 용어집의 VDA 5050 한 줄 정의가 팩트시트 메시지 정의('차량이 자신의 기능 정보를 상위 관제에 미리 알리는 메시지')로 되어 있어 규격 자체 정의(AGV·이동로봇과 상위 관제 사이 통신 인터페이스)와 맞지 않음. f1·f5 로 현행판 3.0.0 표기 추가 |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 7 · 교차 확인: 0
- 예산 사용량: 검색 2회 · 신규 출처 2건
- 미확인 항목:
    - f7 VDA 5050 3.0.0 명세 마크다운의 7장(메시지 명세) 이후는 열람 도구 응답이 잘려 loadId 불일치 보고 규정 존재 여부 미확인
    - 이전 실행 2026-09-25-03 f12 의 3.0.0 loadId 문구('Set by fleet control or mobile robot ...')는 이번에 잘린 응답 범위에서 다시 찾지 못함 — 3.0.0 state 스키마 설명은 '바코드·RFID 예시'로 2.0.0 과 같음. 두 문구가 서로 다른 위치(action 파라미터 설명 대 state 필드 설명)에 있는지 확인 필요
    - f3 2.0.0 태그 마크다운과 VDA 게시 PDF(ref-022 URL)의 글자 단위 일치 미확인
    - f5 VDA 5050 3.0.0 정확한 발행일(2026-03-19 대 2026-04 보도자료) 미확인 — oq-005 유지
    - ref-031·ref-051·ref-052 발행일 미확인
- 범위 경계 위반 의심:
    - 없음
- 한계: fetch_mode mirror_only: VDA 5050 공식 저장소 raw 원문(main 명세·README·state.schema, 2.0.0 태그 명세)을 열었고 VDA 게시 PDF·보도자료·GS1 페이지는 열지 못했다(ref-032·ref-018·ref-021 원문 미열람). 모든 근거가 같은 발행 주체(VDA/VDMA 또는 GS1)의 산출물이라 교차 확인 0건, finding 신뢰도 상한 medium. 갱신 실행이라 정정 요청 2건과 그에 걸린 열린 질문(oq-005, oq-007)만 차등 조사했다. corr-001: 반영 근거 f1~f6. corr-002: 반영하지 않을 근거 f8(분류원문 정의 보호). 검색 2회/30(한·영 각 1회), 신규 출처 2건/15(ref-051, ref-052), 재사용 5건(ref-022, ref-031, ref-032, ref-018, ref-021). oq-005·oq-007 은 해결하지 못해 해결 제안 없음. 용어집 VDA 5050 항목 정의 불일치를 발견해 갱신 제안으로 올렸다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 바코드·RFID 판독 자체는 연계 대상이라 다루지 않았다.
```

### runs/2026-09-25-03/research.md

```markdown
# 리서치 브리프 2026-09-25-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-03 |
| 날짜 | 2026-09-25 |
| 실행 유형 | topic (주제 조사) |
| 대상 영역 | 7. 화물·재고·자산 식별과 추적 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- 주제 미지정(target.json topic null): 7. 화물·재고·자산 식별과 추적 11절 열린 질문 oq-001(로봇 완료 신호 → EPCIS 인계 이벤트 매핑)을 주제로 선정
- 섹션 6. 대표 접근법과 기술 — 이벤트 기반 추적 소제목이 bizStep 대응 추정 1문장뿐이고 readPoint·bizLocation·source/destination 을 로봇 작업에 쓰는 방법이 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — 모든 행이 원문 미열람, 국내 오픈소스 구현 없음
- 섹션 5. 현장 시나리오 — 완료·인계 행이 표준 매핑 미확인 추정에 기댐
- oq-002 국내 사례 자료 부족

## 조사 질문

1. 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]
2. oq-001 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? (주제 페이지 전체 겨냥)
3. CBV 2.0 의 업무 단계(bizStep)·처분 상태(disposition)·source/destination 유형 가운데 로봇 적재·운반·하역에 대응할 수 있는 값은 무엇이며 정의상 한계는 무엇인가? (섹션 6 겨냥)
4. EPCIS 2.0 의 readPoint·bizLocation·parentID·sourceList/destinationList 는 로봇 인계의 '어디서·어디로·누구에게'를 어떻게 나눠 담는가? (섹션 5·6 겨냥)
5. VDA 5050 2.0·3.0 과 Open-RMF 워크셀 메시지는 화물을 개체 단위(SSCC 등)로 식별하는가, 유형·수량 단위로만 다루는가? (섹션 5·9 겨냥)
6. oq-002 국내에서 EPCIS 2.0 을 구현·운영할 수 있는 공개 구현이나 로봇 작업 결과와 연결한 사례가 있는가? (섹션 7·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | CBV 2.0 온톨로지는 업무 단계 loading 을 '운송 수단에 싣는 것', unloading 을 '운송 수단에서 내리는 것', departing 을 '목적지로 가기 위해 위치를 떠나는 것', arriving 을 '위치에 도착하는 것'으로 정의한다. | ref-044 | 아니오 | medium | 2021-09-30 | 출하 / 시작 조건 | — |
| f2 | [사실] | CBV 2.0 에서 shipping(출하)은 staging_outbound(출하 대기 구역 이동)·loading·departing 을 합친 전체 과정을 가리키며, receiving 은 위치에 도착한 객체를 받아 수령자의 재고에 더하는 단계, accepting 은 점유 또는 소유가 바뀌는 단계, storing 은 위치 안에서 보관 구역으로 넣고 빼는 단계로 정의된다. | ref-044 | 아니오 | medium | 2021-09-30 | 출하 / 완료·인계 | — |
| f3 | [사실] | CBV 2.0 의 source/destination 유형 세 가지는 location(업무 이전 끝점의 물리적 위치), owning_party(끝점에서 객체를 소유한 당사자), possessing_party(끝점에서 물리적으로 점유한 당사자)로 정의된다. | ref-044, ref-015 | 아니오 | medium | 2021-09-30 | 출하 / 완료·인계 | — |
| f4 | [사실] | CBV 2.0 의 처분 상태(disposition) 값에는 두 거래 당사자 사이에 운송 중인 in_transit, 공급망 지점을 지나 진행 중인 선택 값 in_progress, 컨테이너에 실리고 문이 닫혀 봉인된 container_closed 가 있다. | ref-044 | 아니오 | medium | 2021-09-30 | 출하 / 완료·인계 | — |
| f5 | [사실] | EPCIS 2.0 온톨로지에서 readPoint 는 이벤트가 일어난 지점이고, bizLocation 은 이후 다른 이벤트가 반박할 때까지 객체가 있다고 보는 업무 위치이며, 둘 다 선택 항목이다. | ref-045, ref-015 | 아니오 | medium | 2021-09-30 | 완료·인계 | — |
| f6 | [사실] | GS1 EPCIS·CBV 구현 가이드라인은 객체가 문 A를 지나 방 1에서 방 2로 옮겨 가면 readPoint 는 문 A, bizLocation 은 방 2가 된다고 설명하고, 출하(shipping) 이벤트에서는 수령 이벤트 전까지 업무 위치를 알 수 없으므로 bizLocation 을 생략한다고 안내한다. | ref-015 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f7 | [사실] | EPCIS 2.0 온톨로지에서 AggregationEvent 는 '담는' 개체 안의 '담긴' 객체를 다루고, parentID 는 action 이 OBSERVE 일 때만 선택이며 ADD·DELETE 에서는 필수이고, AssociationEvent 는 물리 객체를 상위 객체나 특정 물리 위치와 연결·해제하는 이벤트다. | ref-045 | 아니오 | medium | 2021-09-30 | 작업 대상 | — |
| f8 | [사실] | EPCIS 2.0 온톨로지에서 sourceList·destinationList 는 업무 이전(business transfer)의 출발·도착 끝점 맥락을 주는 선택 목록이며, bizTransaction 은 구매주문·출하통지(Despatch Advice) 같은 업무 거래 문서를 가리킨다. | ref-045 | 아니오 | medium | 2021-09-30 | 출하 / 완료·인계 | — |
| f9 | [사실] | GS1 EPCIS 2.0 JSON 스키마의 이벤트 공통 필수 항목은 eventTime, eventTimeZoneOffset, action 이며 readPoint·bizLocation·sourceList·destinationList·sensorElementList 등은 이벤트 유형별 하위 스키마가 정한다. | ref-046 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | VDA 5050 2.0.0(공식 저장소 2.0.0 태그)의 상태 메시지 loads 는 적재 상태를 판단할 수 없는 차량이면 생략하는 선택 배열이고, loadId 는 바코드·RFID 같은 적재물의 고유 식별 번호이며 식별할 수 있으나 아직 식별하지 않았으면 빈 값이다. | ref-022 | 아니오 | medium | 2022-01 | 작업 대상 | 원문 미열람 |
| f11 | [사실] | VDA 5050 2.0.0과 3.0.0 모두 pick 동작의 FINISHED 는 적재물이 차량에 들어오고 새 적재 상태를 보고한 때, drop 동작의 FINISHED 는 적재물이 차량을 떠나고 새 적재 상태를 보고한 때로 정하며, 두 동작은 선택 파라미터로 loadType·loadId·stationType 등을 받는다. | ref-022, ref-031 | 아니오 | medium | 2022-01 | 완료·인계 | — |
| f12 | [사실] | VDA 5050 3.0.0(공식 저장소 main)은 loadId 를 시스템 설계와 적재물 추적 능력에 따라 관제(fleet control) 또는 이동로봇이 정하는 고유 식별자로 설명하고, loads 가 비어 있으면 적재물 없음, 생략하면 적재 상태를 판단할 수 없음을 뜻한다. | ref-031 | 아니오 | medium | 2026 | 작업 대상 | — |
| f13 | [사실] | Open-RMF 의 DispenserRequest 메시지는 요청 id(request_guid)·대상 워크셀(target_guid)·운반체 유형과 품목 목록을 담고, 품목(DispenserRequestItem)은 개체 식별자가 아니라 유형 id(type_guid)·수량(quantity)·구획 이름(compartment_name)으로만 기술된다. | ref-047, ref-048 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f14 | [사실] | Open-RMF 의 IngestorResult 메시지는 요청 id(request_guid)·결과를 보낸 워크셀 id(source_guid)·상태(ACKNOWLEDGED, SUCCESS, FAILED)를 담는다. | ref-049 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f15 | [사실] | Open-RMF 의 배송 작업에서 로봇은 pickup_waypoint 로 가서 DispenserResult 를 받을 때까지 DispenserRequest 를 보내고, dropoff_waypoint 로 가서 IngestorResult 를 받을 때까지 IngestorRequest 를 보낸다. | ref-023 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f16 | [추정] | CBV 의 loading·unloading 은 운송 수단(shipping conveyance)에 싣고 내리는 것으로 정의되어 있어, 시설 안에서 로봇이 팔레트를 싣고 내리는 동작에 그대로 붙이면 의미가 어긋나며 시설 내 운반은 storing·staging_outbound 같은 단계나 readPoint·bizLocation 변화로 표현하는 편이 정의에 가까워 보인다. | ref-044, ref-045 | 아니오 | low | 2026-09-25 | 적치 / 시작 조건 | — |
| f17 | [추정] | 로봇 하역 완료(VDA 5050 drop FINISHED 또는 Open-RMF IngestorResult SUCCESS)를 EPCIS 이벤트로 옮길 때 하역 지점은 readPoint, 하역 뒤 화물이 머무는 구역은 bizLocation, 인계 당사자가 바뀌는 경우에만 possessing_party 를 담은 source/destination 목록으로 나눠 기록하는 구조가 표준 정의와 맞을 것으로 보인다. | ref-045, ref-044, ref-022, ref-049 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f18 | [추정] | Open-RMF 워크셀 요청·결과는 품목을 유형·수량으로만 다루므로, 개체 단위 식별자(SSCC 등)를 담은 EPCIS 이벤트를 만들려면 식별자를 WMS 작업 정보나 별도 판독 결과에서 가져와 요청 id 와 연결해야 할 것으로 보인다. | ref-048, ref-049, ref-023 | 아니오 | low | 2026-09-25 | 작업 대상 | — |
| f19 | [추정] | VDA 5050 2.0 에서는 loadId 가 식별 전이면 빈 값이고 loads 는 생략될 수 있으므로, drop 완료만으로 개체 단위 인계 이벤트를 만들 수 없는 경우가 생기며 이때 이벤트 생성을 보류하거나 다른 식별 근거로 보완하는 규칙이 필요할 것으로 보인다. | ref-022 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f20 | [추정] | VDA 5050 3.0.0 은 loadId 를 관제가 정할 수도 있다고 하므로, 관제 역할을 하는 ROP가 WMS 의 SSCC 를 loadId 로 내려보내 로봇 보고와 EPCIS 이벤트의 식별자를 맞추는 설계가 가능할 수 있으나, 규격이 그 값의 형식을 SSCC 로 정하지는 않는다. | ref-031 | 아니오 | low | 2026-09-25 | 작업 대상 | — |
| f21 | [추정] | 이번 검색 범위(한·영 7회)에서는 VDA 5050 이나 Open-RMF 의 적재·하역 완료를 EPCIS 이벤트로 옮기는 표준 매핑이나 공개 구현이 확인되지 않았다. | ref-031, ref-045 | 아니오 | low | 2026-09-25 | — | — |
| f22 | [사실] | 세종대학교 Auto-ID Labs Korea 는 2014년부터 GS1 EPCIS 오픈소스 구현 Oliot EPCIS 를 개발·유지하고 있으며, 2세대는 EPCIS/CBV 2.0 표준 개발 작업반(MSWG) 과정에 맞춰 새로 개발되었다. | ref-050 | 아니오 | medium | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf | 예 |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl | 아니오 |
| ref-046 | GS1 | gs1/EPCIS — JSON-Schema/EPCIS-JSON-Schema-root.json | 미확인 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/JSON-Schema/EPCIS-JSON-Schema-root.json | 아니오 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 아니오 |
| ref-048 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-050 | Auto-ID Labs Korea(세종대학교), Byun, J. | Oliot EPCIS for GS1 EPCIS/CBV 2.0.0 (GitHub JaewookByun/epcis README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/JaewookByun/epcis | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| new | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md | — | 주제: 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 기록하는 방법(oq-001 심화). 주 연구영역 7. 화물·재고·자산 식별과 추적, 관련 영역 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 17. 로봇 간 협업·물리적 인계, 1. 주문·업무 시스템 연계. 표준 정의 f1~f9, 로봇·설비 쪽 식별 수준 f10~f15, 대응 추론 f16~f20, 매핑 부재 f21, 국내 구현 f22. 기존 주제 페이지(2026-09-25-robot-load-reporting-handover-confirmation)는 인터페이스 보고를 다루므로 이 페이지는 EPCIS 쪽 필드 설계로 구분하고 서로 링크 |
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | 6, 7, 11 | f5·f6·f16 을 섹션 6 이벤트 기반 추적에(readPoint·bizLocation 구분과 loading 정의 한계, 새 주제 페이지 링크) / f22·ref-044·ref-045 를 섹션 7에(Oliot EPCIS 국내 오픈소스 행 추가, EPCIS·CBV 행에 공식 저장소 원문 확인 표시) / 섹션 11에 open_questions_new 2건 추가, oq-001 은 f21 로 '조사 중' 유지 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 판독 지점 | Read Point (EPCIS readPoint) | EPCIS 이벤트가 일어난 지점을 나타내는 필드로, 객체가 이벤트 시점에 있던 위치(예: 문, 도크, 하역 지점)를 가리킨다. |
| 업무 위치 | Business Location (EPCIS bizLocation) | EPCIS 이벤트 뒤 다른 이벤트가 반박할 때까지 객체가 있다고 보는 업무상 위치를 나타내는 필드이다. |
| 연결 이벤트 | AssociationEvent | 물리 객체를 상위 객체나 특정 물리 위치와 연결하거나 연결을 해제한 사실을 기록하는 EPCIS 2.0 이벤트 유형이다. |

## 열린 질문

새로 생긴 질문:

- CBV 의 loading·unloading 이 운송 수단 적재로 정의되어 있을 때 시설 안 로봇의 적재·운반·하역은 어떤 업무 단계(bizStep) 값이나 사용자 정의 어휘로 기록해야 하는가? | 관련 영역: 7. 화물·재고·자산 식별과 추적, 17. 로봇 간 협업·물리적 인계 | 근거: f16 | 종류: 일반
- VDA 5050 3.0.0 에서 관제가 loadId 를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? | 관련 영역: 7. 화물·재고·자산 식별과 추적, 9. 로봇·제조사 관제 연동 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 11 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 7건
- 미확인 항목:
    - f1~f9 교차 확인 실패: 근거가 모두 GS1 발행(온톨로지·스키마·가이드라인)이라 독립 출처 아님
    - f6 가이드라인의 방·문 비유와 출하 이벤트 bizLocation 생략 안내는 검색 요약만 확인(ref-015 원문 미열람)
    - f9 이벤트 유형별 하위 스키마(AggregationEvent 등)의 필수 항목 미확인
    - f12 VDA 5050 3.0.0 loadId 문구는 WebFetch 요약 모델을 거친 인용이라 글자 단위 일치 미확인
    - CBV bizStep 전체 목록(시설 내 이동에 쓸 값 존재 여부) 미확인
    - oq-002 국내 물류센터에서 로봇 작업 결과와 EPCIS 를 연결한 운영 사례는 찾지 못함(국내 구현 오픈소스만 확인)
    - ref-044·ref-045 는 GS1 초안 저장소 파일이라 ref.gs1.org 비준판과 문구가 같은지 미확인
- 범위 경계 위반 의심:
    - 없음
- 한계: fetch_mode mirror_only: raw.githubusercontent.com 의 공식 저장소 원문(GS1 EPCIS 온톨로지·JSON 스키마, VDA 5050 2.0.0 태그·main(3.0.0), Open-RMF 메시지 정의, Oliot EPCIS README)은 열었고 ref-023 은 inbox 원문 텍스트로 읽었다. ref-015(GS1 가이드라인)만 원문 미열람이다. ref-022 는 VDA 게시 PDF 가 아니라 공식 저장소 2.0.0 태그 마크다운(RELEASE CANDIDATE 문구 포함)을 읽은 것이다. 모든 핵심 정의가 발행 기관 한 곳(GS1 또는 VDA)의 산출물이라 교차 확인 0건, finding 신뢰도 상한을 medium 으로 두었다. 주제는 target.json 에 없어 11절 열린 질문 oq-001 을 골랐다. oq-001 은 표준 매핑·공개 구현을 찾지 못해(f21) 해결 제안하지 않았다. 검색 7회/30, 신규 출처 7건/15(ref-044~ref-050). 재사용 출처 4건(ref-015, ref-022, ref-023, ref-031). 27. AI·학습·적응과 모델 운영 관련 finding 없음. 바코드·RFID 판독 자체는 다루지 않았다(연계 대상). oq-003 은 f19 에서 연결만 했고 조사하지 않았다.
```

### runs/2026-09-25-01/research.md

```markdown
# 리서치 브리프 2026-09-25-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-01 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 7. 화물·재고·자산 식별과 추적 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 기존 출처는 ref-003 GS1 EPCIS 1건뿐
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음

## 조사 질문

1. 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]
2. 제품·박스·팔레트·운반구·로봇은 각각 어떤 표준 식별자(GS1 키, RFID 인코딩)로 식별되는가? (섹션 4·7 겨냥)
3. GS1 EPCIS·CBV 는 적재 관계(집계), 위치, 소유·점유 인계를 어떤 이벤트·필드로 표현하는가? (섹션 6·7 겨냥)
4. 로봇 관제 인터페이스(VDA 5050, Open-RMF)는 로봇이 싣고 있는 화물의 식별과 적재·하역 완료를 어떻게 보고하는가? (섹션 5·6·9 겨냥)
5. 바코드·RFID 판독의 현장 한계(판독 실패 요인)는 무엇이며 인계 확인에 어떤 영향을 주는가? (섹션 5·8 겨냥)
6. 화물 식별·추적에서 ROP가 직접 맡을 부분과 WMS·로봇·판독 설비에 맡길 부분의 경계는 어디인가? (섹션 9·10 겨냥)
7. 국내(GS1 Korea, 국내 물류센터) 자료에서 물류 단위 식별·라벨 규칙과 적용 사례는 무엇인가? (섹션 5·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EPCIS 2.0 은 ISO/IEC 19987:2024 로 국제표준화되어 있으며, 서로 다른 애플리케이션이 기업 내·기업 간에 가시성 이벤트 데이터(visibility event data)를 만들고 공유하게 하는 것을 목표로 한다. | ref-011 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f2 | [사실] | GS1 CBV(Core Business Vocabulary, 핵심 업무 어휘)는 ISO/IEC 19988:2024 로도 발행되었고, EPCIS 이벤트의 데이터 구조에 채워 넣을 어휘 요소와 표준 값을 정의한다. | ref-012, ref-014 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f3 | [사실] | EPCIS 2.0 은 ObjectEvent, AggregationEvent, AssociationEvent, TransformationEvent, TransactionEvent 의 다섯 가지 이벤트 유형을 둔다. | ref-013 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f4 | [사실] | EPCIS 의 AggregationEvent 는 상자를 팔레트에 싣거나 내리는 것처럼 '담는 쪽(parent)'과 '담긴 쪽(children)' 객체의 물리적 결합·분리를 기록하며, 결합된 객체들이 분리 전까지 같은 위치에 있다고 본다. | ref-013 | 아니오 | medium | 2026-09-25 | 포장 / 작업 대상 | 원문 미열람 |
| f5 | [사실] | EPCIS 2.0 에서 새로 도입된 AssociationEvent 는 물리·디지털 객체를 상위 객체나 위치에 연결(또는 해제)한 사실을 기록하며, 센서를 컨테이너·자산에 붙이는 것 같은 장기적 연결에 쓰인다. | ref-013 | 아니오 | medium | 2026-09-25 | 작업 대상 | 원문 미열람 |
| f6 | [사실] | EPCIS 2.0·CBV 2.0 은 2022년 6월 GS1 에서 비준되었고, JSON/JSON-LD 형식, REST API, 센서 데이터와 기존 무엇·언제·어디서·왜에 더한 '어떻게(How)' 차원을 추가했다. | ref-013 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f7 | [사실] | EPCIS 이벤트가 소유·책임·점유(custody) 이전의 일부일 때 source/destination 목록으로 업무 맥락을 붙이며, CBV 는 그 유형으로 owning_party(소유 당사자), possessing_party(점유 당사자), location(위치) 세 가지를 정한다. | ref-014, ref-015 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f8 | [사실] | CBV 의 업무 단계(bizStep) 표준 값에는 receiving(입고), putting_away(적치), picking(피킹), shipping(출하) 같은 창고 업무 단계가 포함되어 있어 EPCIS 이벤트를 물류 흐름 단계에 대응시킬 수 있다. | ref-014 | 아니오 | medium | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f9 | [사실] | SSCC(Serial Shipping Container Code, 물류 단위 일련 코드)는 케이스·팔레트·소포처럼 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 키로, 확장 자리·GS1 업체코드·일련 참조번호·검증 숫자로 구성된다. | ref-016, ref-017 | 아니오 | medium | 2019-09 | 출하 / 작업 대상 | 원문 미열람 |
| f10 | [사실] | GS1 물류 라벨(Logistic Label)에는 SSCC 가 반드시 들어가며, SSCC 는 응용식별자(AI) 00 을 붙여 GS1-128 바코드로 표시한다. | ref-018, ref-017 | 아니오 | medium | 2026-09-25 | 입고 / 작업 대상 | 원문 미열람 |
| f11 | [사실] | GS1 Korea 자료는 팔레트 라벨의 바코드 하단이 팔레트 기단부에서 400~800mm 높이에 오도록 하고, 같은 데이터의 라벨을 두 면에 붙이는 것을 권장한다. | ref-017 | 아니오 | medium | 2019-09 | 입고 / 제약 | 원문 미열람 |
| f12 | [사실] | GS1 은 팔레트·상자·트레이·케그 같은 재사용 운반구에 GRAI(Global Returnable Asset Identifier)를, 컨테이너·트럭·트레일러 같은 개별 자산에 GIAI(Global Individual Asset Identifier)를 쓰도록 구분한다. | ref-019, ref-020 | 아니오 | medium | 2026-09-25 | 반품 / 작업 대상 | 원문 미열람 |
| f13 | [사실] | GS1 EPC 태그 데이터 표준(Tag Data Standard, TDS)은 SSCC·GRAI·SGLN·GIAI 등 GS1 키를 UHF RFID 태그에 싣는 EPC 인코딩(예: SSCC-96, GRAI-96)을 정의한다. | ref-021 | 아니오 | medium | 2026-09-25 | 작업 대상 | 원문 미열람 |
| f14 | [사실] | VDA 5050 2.0 의 state 메시지에는 선택 항목인 loads 배열이 있어 차량이 현재 싣고 있는 적재물의 loadId(바코드·RFID 등 고유 식별), loadType, loadPosition, weight(kg)를 보고하며, 적재 상태를 판단할 수 없는 차량은 이 필드를 보내지 않고 빈 배열은 '적재물 없음'을 뜻한다. | ref-022 | 아니오 | medium | 2022-01 | 완료·인계 | 원문 미열람 |
| f15 | [추정] | VDA 5050 은 pick·drop 같은 적재 처리 동작을 주문의 노드·엣지에 붙이는 action 으로 다루고, 그 진행 상태를 state 메시지로 보고하게 한다. | ref-022 | 아니오 | medium | 2022-01 | 완료·인계 | 원문 미열람 |
| f16 | [사실] | Open-RMF 의 배송(Delivery) 작업에서 플릿 어댑터는 적재 설비(dispenser)에 DispenserRequest 를 보내 DispenserResult SUCCESS 를 받은 뒤 로봇을 하역 지점으로 보내고, 하역 설비(ingestor)에 IngestorRequest 를 보내 IngestorResult SUCCESS 로 하역 완료를 확인한다. | ref-023 | 아니오 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f17 | [사실] | 창고 도크 도어를 모사한 RFID 게이트 실험에서 팔레트 적재 소비재의 태그 판독성은 제품·포장 유형, 태그 종류·부착 위치, 적재 패턴에 따라 달라졌고, 음료가 든 금속 캔이 가장 낮았으며 일반적인 지게차 속도는 판독성에 거의 영향을 주지 않았다. | ref-024 | 아니오 | medium | 2009 | 입고 / 예외·성과 | 원문 미열람 |
| f18 | [의견] | AMR·AGV 산업 물류 방법론 조사 논문은 로봇 플릿의 산업적 가치가 WMS·MES·ERP·PLC 연동, 안전 구역, 충전 관리와 함께 추적 가능한 이벤트 로그 유지에 달려 있다고 평가한다. | ref-025 | 아니오 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f19 | [추정] | 로봇 관제 인터페이스의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)는 로봇·설비의 행동 완료를 알릴 뿐이므로, '어떤 팔레트가 누구에게 인계됐는가'를 확정하려면 화물 식별자(SSCC 등)와 인계 당사자·위치를 담은 이벤트(EPCIS 의 source/destination·집계 이벤트 등)와 결합해야 한다. | ref-022, ref-023, ref-013, ref-014, ref-003 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f20 | [추정] | 연계 대상: 바코드·RFID 태그 판독 자체(센서 인식)는 로봇·판독 설비 쪽 기능이며, VDA 5050 은 로봇이 식별한 결과(loadId)를 상태로 보고하는 인터페이스만 정하므로 ROP는 판독 방법이 아니라 식별 결과의 수신·대조·기록을 맡는 구조가 된다. | ref-022 | 아니오 | low | 2022-01 | 수행 자원 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 미확인 | 표준 | medium | 2026-09-25 | https://ref.gs1.org/epcis/ | 예 |
| ref-011 | ISO/IEC | ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) | 2024 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/85557.html | 예 |
| ref-012 | ISO/IEC | ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) | 2024 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/85558.html | 예 |
| ref-013 | OpenEPCIS | EPCIS 2.0 and EPCIS 1.2 \| OpenEPCIS Docs | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://openepcis.io/docs/epcis/ | 예 |
| ref-014 | GS1 | Core Business Vocabulary (CBV) Standard | 미확인 | 표준 | medium | 2026-09-25 | https://ref.gs1.org/standards/cbv/ | 예 |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf | 예 |
| ref-016 | GS1 | Serial Shipping Container Code (SSCC) | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/standards/id-keys/sscc | 예 |
| ref-017 | GS1 Korea(대한상공회의소 유통물류진흥원) | SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 | 2019-09 | 표준 | medium | 2026-09-25 | http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf | 예 |
| ref-018 | GS1 | GS1 Logistic Label Guideline | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf | 예 |
| ref-019 | GS1 | Global Returnable Asset Identifier (GRAI) | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/standards/id-keys/grai | 예 |
| ref-020 | GS1 | Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal) | 미확인 | 표준 | medium | 2026-09-25 | https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods- | 예 |
| ref-021 | GS1 | EPC Tag Data Standard | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf | 예 |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 예 |
| ref-024 | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 2009 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864 | 예 |
| ref-025 | MDPI Encyclopedia | A Methodological Survey of Autonomous Mobile Robots and Automated Guided Vehicles in Industrial Logistics | 미확인 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/encyclopedia6090197 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f18·f19(로봇 위치 추적과 화물 인계 추적의 차이) / 섹션 4: f3·f4·f5·f7·f9·f12·f13(EPCIS 이벤트 유형, SSCC·GRAI·GIAI, EPC 인코딩) / 섹션 5: f10·f11(입고 라벨 판독), f14·f16·f19(출하 인계 완료·인계), f12(반품 운반구), f17(입고 예외·성과) — 흐름 단계와 여섯 항목 명시 / 섹션 6: f4·f7·f8·f14·f15·f16 / 섹션 7: f1·f2·f6·f9·f10·f13·f14·f16(GS1 EPCIS·CBV·SSCC·물류 라벨·EPC TDS, VDA 5050, Open-RMF) / 섹션 8: f17·f18 / 섹션 9: f20(판독은 연계 대상, ROP는 식별 결과 수신·대조·기록), f19 / 섹션 10: 17. 로봇 간 협업·물리적 인계(f16·f19), 9. 로봇·제조사 관제 연동(f14·f15), 8. 실시간 세계 상태·데이터 일관성(f14 적재 상태), 6. 지도·공간·위치 모델(f7 location), 1. 주문·업무 시스템 연계(f18), 20. 예외 복구·재계획·업무 연속성(f17) / 섹션 11: open_questions_new 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 물류 단위 일련 코드 | Serial Shipping Container Code (SSCC) | 케이스·팔레트·소포 등 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 식별 키이다. |
| 글로벌 반환형 자산 식별자 | Global Returnable Asset Identifier (GRAI) | 팔레트·상자·트레이·케그처럼 여러 번 재사용되는 운반구를 식별하는 GS1 식별 키이다. |
| 글로벌 개별 자산 식별자 | Global Individual Asset Identifier (GIAI) | 컨테이너·트럭·트레일러 같은 개별 자산을 식별하는 GS1 식별 키이다. |
| 핵심 업무 어휘 | Core Business Vocabulary (CBV) | EPCIS 이벤트의 업무 단계·상태·인계 유형 등에 채울 표준 어휘 값을 정한 GS1 표준(ISO/IEC 19988)이다. |
| 집계 이벤트 | AggregationEvent | 상자를 팔레트에 싣거나 내리는 것처럼 상위 객체와 하위 객체의 물리적 결합·분리를 기록하는 EPCIS 이벤트 유형이다. |
| VDA 5050 | VDA 5050 | 독일자동차산업협회(VDA)가 정한 AGV·AMR 과 상위 관제 사이의 통신 인터페이스 권고안이다. |

## 열린 질문

새로 생긴 질문:

- 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? | 관련 영역: 7. 화물·재고·자산 식별과 추적, 17. 로봇 간 협업·물리적 인계, 9. 로봇·제조사 관제 연동 | 근거: f19 | 종류: 일반
- 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? | 관련 영역: 7. 화물·재고·자산 식별과 추적, 1. 주문·업무 시스템 연계 | 근거: f9 | 종류: 일반
- 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? | 관련 영역: 7. 화물·재고·자산 식별과 추적, 20. 예외 복구·재계획·업무 연속성 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f6 EPCIS 2.0 비준 시점(2022년 6월)을 GS1 원문으로 교차 확인하지 못함(OpenEPCIS 단일 출처)
    - f8 CBV bizStep 개별 값 목록을 원문으로 직접 확인하지 못함
    - f9·f10 SSCC 18자리·AI 00 은 GS1 계열 출처만 있어 독립 교차 확인 실패
    - f15 VDA 5050 pick/drop 의 actionParameters(loadId) 규정이 원문 규정인지 구현 라이브러리 설명인지 미확인
    - EPCIS readPoint 와 bizLocation 의 구분은 벤더·블로그 요약만 확인되어 finding 으로 내지 않음
    - 국토교통부 스마트물류센터 인증의 평가 항목(입고·보관·피킹·출고 자동화, 정보시스템 수준)은 기사 요약만 확인되어 finding 으로 내지 않음
    - 국내 KCI 논문(RFID 기반 자동 검수 시스템, 2014)은 서지 정보만 확인되고 내용 요약을 얻지 못해 출처로 넣지 않음
    - ref-013·ref-014·ref-015·ref-016·ref-018·ref-019·ref-020·ref-021·ref-023·ref-025 발행일 미확인
- 범위 경계 위반 의심:
    - f20: 태그 판독(센서 인식)은 분류 원문 9장 '로봇 자체 지능·제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f17: RFID 판독 성능 자체는 판독 설비 영역이며, 인계 확인의 예외·성과 조건으로만 쓰도록 제안함
- 한계: web_fetch_available: false 로 모든 출처(재사용 ref-003 포함) 원문 미열람. 검색 결과의 기관·제목·URL 일치로만 실재를 확인했고 수치·구절은 검색 요약 범위를 넘지 않았다. 신뢰도 상한 medium. 주요 표준 출처가 모두 GS1 계열(ISO/IEC 판도 GS1 원문 기반)이라 독립 교차 확인이 가능한 조합을 찾지 못해 cross_checked_count 0. 신규 출처 상한 15건에 도달해 국내 스마트물류센터 인증 자료와 국내 논문을 출처로 넣지 못했다. 한국 자료는 GS1 Korea 1건뿐이다. 검색 17회 사용(상한 30). 로봇 작업 완료와 EPCIS 인계 이벤트를 잇는 1차 자료는 찾지 못해 f19 는 추정으로 두고 열린 질문으로 올렸다. 입력의 이전 실행 research.md 는 없었다(첫 실행으로 간주). 27. AI·학습·적응과 모델 운영 관련 finding 없음.
```

### data/source_texts/ref-228.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Mobile Robot Factsheet",
    "description": "The factsheet provides basic information about a specific mobile robot type series. This information allows comparison of different mobile robot types and can be applied for the planning, dimensioning and simulation of a mobile robot system. The factsheet also includes information about mobile robot communication interfaces which are required for the integration of a mobile robot type series into a VD[M]A-5050-compliant fleet control.",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "typeSpecification",
        "physicalParameters",
        "protocolLimits",
        "protocolFeatures",
        "mobileRobotGeometry",
        "loadSpecification"
    ],
    "subtopic": "/factsheet",
    "type": "object",
    "properties":{
        "headerId": {
            "type": "integer",
            "description": "Header ID of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message.",
            "minimum": 0
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "title": "Version",
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot"
        },
        "typeSpecification": {
            "type": "object",
            "required": [
                "seriesName",
                "mobileRobotKinematics",
                "mobileRobotClass",
                "maximumLoadMass",
                "localizationTypes",
                "navigationTypes"
            ],
            "description": "These parameters generally specify the class and the capabilities of the mobile robot",
            "properties": {
                "seriesName": {
                    "type": "string",
                    "description": "Free text generalized series name as specified by manufacturer"
                },
                "seriesDescription": {
                    "type": "string",
                    "description": "Free text human readable description of the mobile robot type series"
                },
                "mobileRobotKinematics": {
                    "type": "string",
                    "description": "Simplified description of mobile robots kinematics-type. Extensible enum: DIFFERENTIAL, OMNIDIRECTIONAL, THREE_WHEEL"
                },
                "mobileRobotClass": {
                    "type": "string",
                    "description": "Simplified description of mobile robot class. Extensible enum: FORKLIFT, CONVEYOR, TUGGER, CARRIER"
                },
                "maximumLoadMass": {
                    "type": "number",
                    "description": "Maximum loadable mass",
                    "unit": "kg",
                    "minimum": 0
                },
                "localizationTypes": {
                    "type": "array",
                    "description": "Simplified description of localization type.",
                    "items": {
                        "type": "string",
                        "description": "Simplified description of localization type. Extensible enum: NATURAL, REFLECTOR, RFID, DMC, SPOT, GRID"
                    }
                },
                "navigationTypes": {
                    "type": "array",
                    "description": "List of path planning types supported by the mobile robot, sorted by priority",
                    "items": {
                        "type": "string",
						"description": "Planning type. Extensible enum: PHYSICAL_LINE_GUIDED, VIRTUAL_LINE_GUIDED, FREELY_NAVIGATING"
                    }
                },
                "supportedZones": {
                    "type": "array",
                    "description": "Array of zone types supported by the mobile robot.",
                    "items": {
                        "type": "string",
                        "enum": [
                            "BLOCKED",
                            "LINE_GUIDED",
                            "RELEASE",
                            "COORDINATED_REPLANNING",
                            "SPEED_LIMIT",
                            "ACTION",
                            "PRIORITY",
                            "PENALTY",
                            "DIRECTED",
                            "BIDIRECTED"
                        ]
                    }
                }
            }
        },
        "physicalParameters": {
            "type": "object",
            "required": [
                "minimumSpeed",
                "maximumSpeed",
                "maximumAcceleration",
                "maximumDeceleration",
                "minimumHeight",
                "maximumHeight",
                "width",
                "length"
            ],
            "description": "These parameters specify the basic physical properties of the mobile robot",
            "properties": {
                "minimumSpeed": {
                    "type": "number",
                    "description": "Minimal controlled continuous speed of the mobile robot",
                    "unit": "m/s",
					"minimum": 0.0
                },
                "maximumSpeed": {
                    "type": "number",
                    "description": "Maximum speed of the mobile robot",
                    "unit": "m/s",
					"minimum": 0.0
                },
                "minimumAngularSpeed": {
                    "type": "number",
                    "description": "Minimal controlled continuous rotation speed of the mobile robot",
                    "unit": "rad/s",
					"minimum": 0.0
                },
                "maximumAngularSpeed": {
                    "type": "number",
                    "description": "Maximum rotation speed of the mobile robot",
                    "unit": "rad/s",
					"minimum": 0.0
                },
                "maximumAcceleration": {
                    "type": "number",
                    "description": "Maximum acceleration with maximum load",
                    "unit": "m/s^2",
					"minimum": 0.0
                },
                "maximumDeceleration": {
                    "type": "number",
                    "description": "Maximum deceleration with maximum load",
                    "unit": "m/s^2"
                },
                "minimumHeight": {
                    "type": "number",
                    "description": "Minimum height of mobile robot",
                    "unit": "m"
                },
                "maximumHeight": {
                    "type": "number",
                    "description": "Maximum height of mobile robot",
                    "unit": "m"
                },
                "width": {
                    "type": "number",
                    "description": "Width of the mobile robot",
                    "unit": "m"
                },
                "length": {
                    "type": "number",
                    "description": "Length of the mobile robot",
                    "unit": "m"
                }
            }
        },
        "protocolLimits": {
            "type": "object",
            "required": [
                "maximumStringLengths",
                "maximumArrayLengths",
                "timing"
            ],
            "description": "This JSON-object describes the protocol limitations of the mobile robot. If a parameter is not defined or set to zero then there is no explicit limit for this parameter.",
            "properties": {
                "maximumStringLengths": {
                    "type": "object",
                    "description": "Maximum lengths of strings",
                    "properties": {
                        "maximumMessageLength": {
                            "type": "integer",
                            "description": "Maximum MQTT Message length",
							"minimum": 0
                        },
                        "maximumTopicSerialLength": {
                            "type": "integer",
                            "description": "Maximum length of serial-number part in MQTT-topics. Affected Parameters: order.serialNumber, instantActions.serialNumber, state.SerialNumber, visualization.serialNumber, connection.serialNumber",
							"minimum": 0
                        },
                        "maximumTopicElementLength": {
                            "type": "integer",
                            "description": "Maximum length of all other parts in MQTT-topics. Affected parameters: order.timestamp, order.version, order.manufacturer, instantActions.timestamp, instantActions.version, instantActions.manufacturer, state.timestamp, state.version, state.manufacturer, visualization.timestamp, visualization.version, visualization.manufacturer, connection.timestamp, connection.version, connection.manufacturer",
							"minimum": 0
                        },
                        "maximumIdLength": {
                            "type": "integer",
                            "description": "Maximum length of ID-Strings. Affected parameters: order.orderId, node.nodeId, nodePosition.mapId, action.actionId, edge.edgeId",
							"minimum": 0
                        },
                        "idNumericalOnly": {
                            "type": "boolean",
                            "description": "If true ID-strings need to contain numerical values only"
                        },
                        "maximumLoadIdLength": {
                            "type": "integer",
                            "description": "Maximum length of loadId Strings",
							"minimum": 0
                        }
                    }
                },
                "maximumArrayLengths": {
                    "type": "object",
                    "description": "Maximum lengths of arrays",
                    "properties": {
                        "order.nodes": {
                            "type": "integer",
                            "description": "Maximum number of nodes per order processable by the mobile robot",
							"minimum": 0
                        },
                        "order.edges": {
                            "type": "integer",
                            "description": "Maximum number of edges per order processable by the mobile robot",
							"minimum": 0
                        },
                        "node.actions": {
                            "type": "integer",
                            "description": "Maximum number of actions per node processable by the mobile robot",
							"minimum": 0
                        },
                        "edge.actions": {
                            "type": "integer",
                            "description": "Maximum number of actions per edge processable by the mobile robot",
							"minimum": 0
                        },
                        "actions.actionsParameters": {
                            "type": "integer",
                            "description": "Maximum number of parameters per action processable by the mobile robot",
							"minimum": 0
                        },
                        "instantActions": {
                            "type": "integer",
                            "description": "Maximum number of instant actions per message processable by the mobile robot",
							"minimum": 0
                        },
                        "trajectory.knotVector": {
                            "type": "integer",
                            "description": "Maximum number of knots per trajectory processable by the mobile robot",
							"minimum": 0
                        },
                        "trajectory.controlPoints": {
                            "type": "integer",
                            "description": "Maximum number of control points per trajectory processable by the mobile robot",
							"minimum": 0
                        },
                        "zoneSet.zones": {
                            "type": "integer",
                            "description": "Maximum number of zones per zoneSet processable by the mobile robot",
							"minimum": 0
                        },
                        "state.nodeStates": {
                            "type": "integer",
                            "description": "Maximum number of nodeStates sent by the mobile robot, maximum number of nodes in base of mobile robot",
							"minimum": 0
                        },
                        "state.edgeStates": {
                            "type": "integer",
                            "description": "Maximum number of edgeStates sent by the mobile robot, maximum number of edges in base of mobile robot",
							"minimum": 0
                        },
                        "state.loads": {
                            "type": "integer",
                            "description": "Maximum number of load-objects sent by the mobile robot",
							"minimum": 0
                        },
                        "state.actionStates": {
                            "type": "integer",
                            "description": "Maximum number of actionStates sent by the mobile robot",
							"minimum": 0
                        },
                        "state.instantActionStates": {
                            "type": "integer",
                            "description": "Maximum number of instantActionStates sent by the mobile robot",
							"minimum": 0
                        },
                        "state.zoneActionStates": {
                            "type": "integer",
                            "description": "Maximum number of zoneActionStates sent by the mobile robot",
							"minimum": 0
                        },
                        "state.errors": {
                            "type": "integer",
                            "description": "Maximum number of errors sent by the mobile robot in one state-message",
							"minimum": 0
                        },
                        "state.information": {
                            "type": "integer",
                            "description": "Maximum number of information objects sent by the mobile robot in one state-message",
							"minimum": 0
                        },
                        "error.errorReferences": {
                            "type": "integer",
                            "description": "Maximum number of error references sent by the mobile robot for each error",
							"minimum": 0
                        },
                        "information.infoReferences": {
                            "type": "integer",
                            "description": "Maximum number of info references sent by the mobile robot for each information",
							"minimum": 0
                        }
                    }
                },
                "timing": {
                    "type": "object",
                    "required": [
                        "minimumOrderInterval",
                        "minimumStateInterval"
                    ],
                    "description": "Timing information",
                    "properties": {
                        "minimumOrderInterval": {
                            "type": "number",
                            "description": "Minimum interval sending order messages to the mobile robot",
                            "unit": "s",
							"minimum": 0.0
                        },
                        "minimumStateInterval": {
                            "type": "number",
                            "description": "Minimum interval for sending state-messages",
                            "unit": "s",
							"minimum": 0.0
                        },
                        "defaultStateInterval": {
                            "type": "number",
                            "description": "Default interval for sending state-messages if not defined, the default value from the main document is used",
                            "unit": "s",
							"minimum": 0.0
                        },
                        "visualizationInterval": {
                            "type": "number",
                            "description": "Default interval for sending messages on visualization topic",
                            "unit": "s",
							"minimum": 0.0
                        }
                    }
                }
            }
        },
        "protocolFeatures": {
            "type": "object",
            "required": [
                "optionalParameters",
                "mobileRobotActions"
            ],
            "description": "Supported features of VDA5050 protocol",
            "properties": {
                "optionalParameters": {
                    "type": "array",
                    "description": "List of supported and/or required optional parameters. Optional parameters, that are not listed here, are assumed to be not supported by the mobile robot.",
                    "items": {
                        "type": "object",
                        "required": [
                            "parameter",
                            "support"
                        ],
                        "properties": {
                            "parameter": {
                                "type": "string",
                                "description": "Full name of optional parameter, e.g., “order.nodes.nodePosition.allowedDeviationTheta”"
                            },
                            "support": {
                                "type": "string",
                                "description": "Type of support for the optional parameter, the following values are possible: SUPPORTED: optional parameter is supported like specified. REQUIRED: optional parameter is required for proper mobile robot operation.",
                                "enum": [
                                    "SUPPORTED",
                                    "REQUIRED"
                                ]
                            },
                            "description": {
                                "type": "string",
                                "description": "Free text. Description of optional parameter. E.g., reason, why the optional parameter ‚direction‘ is necessary for this mobile robot type and which values it can contain. The parameter ‘nodeMarker’ must contain unsigned interger-numbers only. Nurbs-Support is limited to straight lines and circle segments."
                            }
                        }
                    }
                },
                "mobileRobotActions": {
                    "type": "array",
                    "description": "List of all actions with parameters supported by this mobile robot. This includes standard actions specified in VDA 5050 and manufacturer-specific actions",
                    "items": {
                        "required": [
                            "actionType",
                            "actionScopes",
                            "pauseAllowed",
                            "cancelAllowed"
                        ],
                        "type": "object",
                        "properties": {
                            "actionType": {
                                "type": "string",
                                "description": "Unique actionType corresponding to action.actionType"
                            },
                            "actionDescription": {
                                "type": "string",
                                "description": "Free text: description of the action"
                            },
                            "actionScopes": {
                                "type": "array",
                                "description": "List of allowed scopes for using this action-type. INSTANT: usable as instantAction, NODE: usable on nodes, EDGE: usable on edges, ZONE: usable as zone action.",
                                "items": {
                                    "type": "string",
                                    "enum": [
                                        "INSTANT",
                                        "NODE",
                                        "EDGE",
                                        "ZONE"
                                    ]
                                }
                            },
                            "actionParameters": {
                                "type": "array",
                                "description": "Kist of parameters. if not defined, the action has no parameters",
                                "items": {
                                    "type": "object",
                                    "required": [
                                        "key",
                                        "valueDataType"
                                    ],
                                    "properties": {
                                        "key": {
                                            "type": "string",
                                            "description": "Key-String for Parameter"
                                        },
                                        "valueDataType": {
                                            "type": "string",
                                            "description": "Data type of Value, possible data types are: BOOL, NUMBER, INTEGER, STRING, OBJECT, ARRAY",
                                            "enum": [
                                                "BOOL",
                                                "NUMBER",
                                                "INTEGER",
                                                "STRING",
                                                "OBJECT",
                                                "ARRAY"
                                            ]
                                        },
                                        "description": {
                                            "type": "string",
                                            "description": "Free text: description of the parameter"
                                        },
                                        "isOptional": {
                                            "type": "boolean",
                                            "description": "True: optional parameter"
                                        }
                                    }
                                }
                            },
                            "actionResult": {
                                "type": "string",
                                "description": "Free text: description of the result"
                            },
                            "blockingTypes": {
                                "type": "array",
                                "description": "Array of possible blocking types for defined action.",
                                "items": {
                                   "type":"string",
                                   "enum": [
                                      "NONE",
                                      "SOFT",
                                      "SINGLE",
                                      "HARD"
                                   ]
                                }
                            },
                            "pauseAllowed": {
                                "type": "boolean",
                                "description": "True: action can be paused via startPause. False: action cannot be paused."
                            },
                            "cancelAllowed": {
                                "type": "boolean",
                                "description": "True: action can be cancelled via cancelOrder. False: action cannot be cancelled."
                            }
                        }
                    }
                }
            }
        },
        "mobileRobotGeometry": {
            "type": "object",
            "description": "Detailed definition of mobile robot geometry",
            "properties": {
                "wheelDefinitions": {
                    "type": "array",
                    "description": "List of wheels, containing wheel-arrangement and geometry",
                    "items": {
                        "type": "object",
                        "required": [
                            "type",
                            "isActiveDriven",
                            "isActiveSteered",
                            "position",
                            "diameter",
                            "width"
                        ],
                        "properties": {
                            "type": {
                                "type": "string",
                                "description": "Wheel type. Extensible enum: DRIVE, CASTER, FIXED, MECANUM"
                            },
                            "isActiveDriven": {
                                "type": "boolean",
                                "description": "True: wheel is actively driven"
                            },
                            "isActiveSteered": {
                                "type": "boolean",
                                "description": "True: wheel is actively steered"
                            },
                            "position": {
                                "type": "object",
                                "required": [
                                    "x",
                                    "y"
                                ],
                                "properties": {
                                    "x": {
                                        "type": "number",
                                        "description": "X-position in mobile robot coordinate system",
                                        "unit": "m"
                                    },
                                    "y": {
                                        "type": "number",
                                        "description": "Y-position in mobile robot coordinate system",
                                        "unit": "m"
                                    },
                                    "theta": {
                                        "type": "number",
                                        "description": "Orientation of wheel in mobile robot coordinate system Necessary for fixed wheels",
                                        "unit": "rad"
                                    }
                                }
                            },
                            "diameter": {
                                "type": "number",
                                "description": "Nominal diameter of wheel",
                                "unit": "m"
                            },
                            "width": {
                                "type": "number",
                                "description": "Nominal width of wheel",
                                "unit": "m"
                            },
                            "centerDisplacement": {
                                "type": "number",
                                "unit": "m",
                                "description": "Nominal displacement of the wheel’s center to the rotation point (necessary for caster wheels). If the parameter is not defined, it is assumed to be 0"
                            },
                            "constraints": {
                                "type": "string",
                                "description": "Free text: can be used by the manufacturer to define constraints"
                            }
                        }
                    }
                },
                "envelopes2d": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "envelope2dId",
                            "vertices"
                        ],
                        "properties": {
                            "envelope2dId": {
                                "type": "string",
                                "description": "Identifier of the envelope curve set."
                            },
                            "vertices": {
                                "type": "array",
                                "description": "The envelope curve in defined as a polygon. It shall be assumed as closed. Only simple polygons shall be used.",
                                "items": {
                                    "type": "object",
                                    "required": [
                                        "x",
                                        "y"
                                    ],
                                    "properties": {
                                        "x": {
                                            "type": "number",
                                            "description": "X-position of polygon-point",
                                            "unit": "m"
                                        },
                                        "y": {
                                            "type": "number",
                                            "description": "Y-position of polygon-point",
                                            "unit": "m"
                                        }
                                    }
                                }
                            },
                            "description": {
                                "type": "string",
                                "description": "Free text: description of envelope curve set"
                            }
                        }
                    }
                },
                "envelopes3d": {
                    "type": "array",
                    "description": "List of mobile robot envelope curves in 3D (german: „Hüllkurven“)",
                    "items": {
                        "type": "object",
                        "required": [
                            "envelope3dId",
                            "format"
                        ],
                        "properties": {
                            "envelope3dId": {
                                "type": "string",
                                "description": "Identifier of the envelope curve set."
                            },
                            "format": {
                                "type": "string",
                                "description": "Format of data, e.g., DXF"
                            },
                            "data": {
                                "type": "object",
                                "description": "3D-envelope curve data, format specified in ‚format‘"
                            },
                            "url": {
                                "type": "string",
                                "description": "Protocol and url-definition for downloading the 3D-envelope curve data, e.g., ftp://xxx.yyy.com/ac4dgvhoif5tghji"
                            },
                            "description": {
                                "type": "string",
                                "description": "Free text: description of envelope curve set"
                            }
                        }
                    }
                }
            }
        },
        "loadSpecification": {
            "type": "object",
            "description": "Abstract specification of load capabilities",
            "properties": {
                "loadPositions": {
                    "type": "array",
                    "description": "List of load positions / load handling devices. This lists contains the valid values for the parameter “state.loads[].loadPosition” and for the action parameter “lhd” of the actions pick and drop. If this list doesn’t exist or is empty, the mobile robot has no load handling device.",
                    "items": {
                        "type": "string"
                    }
                },
                "loadSets": {
                    "type": "array",
                    "description": "List of load-sets that can be handled by the mobile robot",
                    "items": {
                        "type": "object",
                        "required": [
                            "setName",
                            "loadType"
                        ],
                        "properties": {
                            "setName": {
                                "type": "string",
                                "description": "Unique name of the load set, e.g., DEFAULT, SET1, ..."
                            },
                            "loadType": {
                                "type": "string",
                                "description": "Type of load e.g., EPAL, XLT1200, …."
                            },
                            "loadPositions": {
                                "type": "array",
                                "description": "List of load positions btw. load handling devices, this load-set is valid for. If this parameter does not exist or is empty, this load-set is valid for all load handling devices on this mobile robot.",
                                "items": {
                                    "type": "string"
                                }
                            },
                            "boundingBoxReference": {
                                "type": "object",
                                "required": [
                                    "x",
                                    "y",
                                    "z"
                                ],
                                "description": "Bounding box reference as defined in parameter loads[] in state-message",
                                "properties": {
                                    "x": {
                                        "type": "number",
                                        "description": "X-coordinate of the point of reference."
                                    },
                                    "y": {
                                        "type": "number",
                                        "description": "Y-coordinate of the point of reference."
                                    },
                                    "z": {
                                        "type": "number",
                                        "description": "Z-coordinate of the point of reference."
                                    },
                                    "theta": {
                                        "type": "number",
                                        "description": "Orientation of the loads bounding box. Important for tugger trains, etc."
                                    }
                                }
                            },
                            "loadDimensions": {
                                "type": "object",
                                "required": [
                                    "length",
                                    "width"
                                ],
                                "properties": {
                                    "length": {
                                        "type": "number",
                                        "description": "Absolute length (along the mobile robot’s coordinate system’s x-axis) of the load's bounding box in meters."
                                    },
                                    "width": {
                                        "type": "number",
                                        "description": "Absolute width (along the mobile robot’s coordinate system’s y-axis) of the load's bounding box in meters."
                                    },
                                    "height": {
                                        "type": "number",
                                        "description": "Absolute height of the load´s bounding box. Optional: Set value only if known."
                                    }
                                }
                            },
                            "maximumWeight": {
                                "type": "number",
                                "description": "Maximum weight of loadtype",
                                "unit": "kg",
								"minimum": 0.0
                            },
                            "minimumLoadhandlingHeight": {
                                "type": "number",
                                "unit": "m",
                                "description": "Minimum allowed height for handling of this load-type and –weight. References to boundingBoxReference",
								"minimum": 0.0
                            },
                            "maximumLoadhandlingHeight": {
                                "type": "number",
                                "unit": "m",
                                "description": "Maximum allowed height for handling of this load-type and –weight. references to boundingBoxReference",
								"minimum": 0.0
                            },
                            "minimumLoadhandlingDepth": {
                                "type": "number",
                                "unit": "m",
                                "description": "Minimum allowed depth for this load-type and –weight. references to boundingBoxReference"
                            },
                            "maximumLoadhandlingDepth": {
                                "type": "number",
                                "unit": "m",
                                "description": "Maximum allowed depth for this load-type and –weight. references to boundingBoxReference"
                            },
                            "minimumLoadhandlingTilt": {
                                "type": "number",
                                "unit": "rad",
                                "description": "Minimum allowed tilt for this load-type and –weight"
                            },
                            "maximumLoadhandlingTilt": {
                                "type": "number",
                                "unit": "rad",
                                "description": "Maximum allowed tilt for this load-type and –weight"
                            },
                            "maximumSpeed": {
                                "type": "number",
                                "unit": "m/s^2",
                                "description": "Maximum allowed speed for this load-type and –weight",
								"minimum": 0.0
                            },
                            "maximumAcceleration": {
                                "type": "number",
                                "unit": "m/s^2",
                                "description": "Maximum allowed acceleration for this load-type and –weight",
								"minimum": 0.0
                            },
                            "maximumDeceleration": {
                                "type": "number",
                                "unit": "m/s^2",
                                "description": "Maximum allowed deceleration for this load-type and –weight"
                            },
                            "pickTime": {
                                "type": "number",
                                "unit": "s",
                                "description": "Approximate time for picking up the load",
								"minimum": 0.0
                            },
                            "dropTime": {
                                "type": "number",
                                "unit": "s",
                                "description": "Approximate time for dropping the load",
								"minimum": 0.0
                            },
                            "description": {
                                "type": "string",
                                "description": "Free text description of the load handling set"
                            }
                        }
                    }
                }
            }
        },
         "mobileRobotConfiguration": {
            "type": "object",
            "properties": {
                "versions": {
                    "type": "array",
                    "description": "Array containing various hardware and software versions running on the mobile robot.",
                    "items": {
                        "title": "version",
                        "type": "object",
                        "required": [
                            "key",
                            "value"
                        ],
                        "properties": {
                            "key": {
                                "type": "string",
                                "description": "The key of the version.",
                                "examples": [
                                    "softwareVersion",
                                    "cameraVersion",
                                    "plcSoftChecksum"
                                ]
                            },
                            "value": {
                                "type": "string",
                                "description": "The value of the version.",
                                "examples": [
                                    "v1.03.2",
                                    "0620NL51805A0",
                                    "0x4297F30C"
                                ]
                            }
                        }
                    }
                },
                "network": {
                    "type": "object",
                    "description": "Information about the mobile robot's network connection. The listed information shall not be updated while the mobile robot is operating.",
                    "properties": {
                        "dnsServers": {
                            "type": "array",
                            "description": "List of DNS servers used by the mobile robot.",
                            "items": {
                                "type": "string"
                            }
                        },
                        "ntpServers": {
                            "type": "array",
                            "description": "List of NTP servers used by the mobile robot.",
                            "items": {
                                "type": "string"
                            }
                        },
                        "localIpAddress": {
                            "type": "string",
                            "description": "A priori assigned IP address of the mobile robot used to communicate with the MQTT broker. Note that this IP address should not be modified/changed during operations."
                        },
                        "netmask": {
                            "type": "string",
                            "description": "Network subnet mask."
                        },
                        "defaultGateway": {
                            "type": "string",
                            "description": "Default gateway used by the mobile robot."
                        }
                    }
                },
                "batteryCharging": {
                    "type": "object",
                    "description": "Information about battery charging parameters.",
                    "properties": {
                        "criticalLowChargingLevel": {
                            "type": "number",
                            "description": "Specifies the critical charging level in percent at or below which the fleet control should only send orders that command the mobile robot to a charging station.",
                            "minimum": 0.0,
                            "maximum": 100.0
                        },
                        "minimumDesiredChargingLevel": {
                            "type": "number",
                            "description": "Specifies the minimum desired charging level in percent.",
                            "minimum": 0.0,
                            "maximum": 100.0
                        },
                        "maximumDesiredChargingLevel": {
                            "type": "number",
                            "description": "Specifies the maximum desired charging level in percent.",
                            "minimum": 0.0,
                            "maximum": 100.0
                        },
                        "minimumChargingTime": {
                            "type": "number",
                            "description": "Specifies the desired minimum charging time in seconds.",
                            "unit": "s",
							"minimum": 0.0
                        }
                    }
                }
            }
        }
    }
}
```
