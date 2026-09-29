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
- verification_stage: second
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
        "ref-459"
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
        "ref-880"
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
        "ref-459",
        "ref-880"
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
        "ref-439"
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
        "ref-439"
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
        "ref-439",
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
        "ref-459",
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
        "ref-439"
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
        "ref-439",
        "ref-459",
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
      "id": "ref-459",
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
      "id": "ref-439",
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
      "id": "ref-880",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-886~ref-900, 예약 구간 안) 상한 도달로 Frontiers 'A survey of ontology-enabled processes for dependable robot autonomy'(2024, 32편 검토 — 연 원문에 검증·변경 관리 서술이 없어 finding 으로 쓰지 않음), Themis, Köcher 외 SHACL 스킬 검증, IDTA SMT 작성 지침, Dibowski 추적성 논문, MDPI 근거 기반 추출 논문은 넣지 못했다. 원문 열람 15건(github_raw 1: IDTA 서브모델 템플릿 README, webfetch 14: W3C 권고안 2건, arXiv 초록 9건, Cambridge 초록, UPM 기관 저장소 초록, KCI 초록), 재사용 3건(ref-465·ref-880 는 2026-09-29-08, ref-228 은 2026-09-29-07 의 값 그대로, 이번에 다시 열지 않아 fetched false). 교차 확인 4건(f4: 포즈난·케이프타운/암스테르담/국내, f8: W3C/그리스 연구진, f13: W3C/IDTA, f17: Zablith 외/Hegde 외/Qiang 외). 신뢰도 high 는 f8·f13 두 건(각각 이번 실행에서 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지)에는 완전성·정확성 쪽은 f1~f8(역량 질문·질의 실행, 추론기, 피트폴 스캐너, SHACL)과 f9·f10(언어 모델 결합 검증)으로, 변경 쪽은 f11~f19·f23(판 식별·호환 표기, 변경 표현·탐지, 재구성 허용성, 팩트시트 판 정보)으로 답했으며 결론은 '검증 수단과 판 표기 규칙은 여러 곳에서 확인되지만 로봇 능력 온톨로지에 대해 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차와 원문 절·줄 근거를 붙인 검토 구현은 확인되지 않았다'는 추정(f22·f24)이다. 분류 원문 1절의 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)를 정의한 출처는 찾지 못해 열린 질문으로 올렸다. 현장 유형: 가정(f2 OntoBOT 평가), 병원(f7 HERON 시뮬레이션 재인용)만 확인했고 제조 공장·물류창고·상업 시설·실외·기타 사례는 없다(제조 사례 후보 Köcher 외는 서지 미확인). 국내 자료는 KCI 논문(f3, 2015, 문헌정보학 온톨로지) 한 건이며 로봇 온톨로지 검증의 국내 사례는 찾지 못했다. 벤더 문서·벤더 주장 없음. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 용어집에 이미 있는 형상 제약 언어·의미적 버전 관리·회귀 시험·모델 검사·온톨로지 채우기·런타임 검증은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음(oq-147 은 f22 로 부분 진전만). 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 전체 885건과의 URL 중복을 대조하지 못했으므로 W3C OWL 2·SHACL·IDTA 저장소·arXiv 2406.07962 등은 퍼블리셔가 기존 id 로 합칠 수 있다."
  }
}
```

### runs/2026-09-29-09/verification.json

```json
{
  "run_id": "2026-09-29-09",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 1811.09529 초록에서 234 CQ·SPARQL-OWL 번역, 106 패턴·46 질의 서명, 형식화·실행·관리 지원 목적 일치. 단일 출처(데이터셋 논문 자체 기술)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2509.22434 초록: SOMA·DOLCE 확장, 가정·노인 돌봄 대상, 역량 질문 평가, TIAGo·HSR·UR3·Stretch. PDF 첫 장 소속은 VU 암스테르담 3명·토리노 공과대학 1명. 현장 배치가 아니라 네 로봇 대상 평가이므로 5절에서 그 점을 밝혀야 한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI 초록(한국문헌정보학회지 49(3), 2015, 성균관대): Pellet TBox 검증·추론규칙 모두 참·SPARQL 시나리오 평가 일치. 발행 2015 — 2년 초과, 월간 재검증 대상."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-890·ref-891·ref-899 세 출처를 각각 열어 종합이 맞음을 확인, 발행 주체 상이. 단 '포즈난 공과대학교·케이프타운 대학교'는 연 초록 페이지·PDF 에서 소속을 읽지 못해 미확인 — 본문에는 저자명만 쓴다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. UPM 기관 저장소(oa.upm.es/35873) 초록: 693개 이상 온톨로지, 구조·기능·사용성 프로파일링 차원, critical·important·minor 일치. 발행 2014-04 — 2년 초과."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. W3C SHACL 권고안(2017-07-20) 원문: 'a language for validating RDF graphs against a set of conditions', sh:conforms·sh:result·sh:resultSeverity(Violation·Warning·Info)·focusNode·resultPath·value·sourceShape 일치. 후속판: SHACL 1.2 Core 작업 초안(W3C WD 2026-06-22)이 진행 중이므로 기준 판(2017 권고안)을 명시해야 한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC12071619 전문(Healthcare, 2025-04-30)을 검증에서 직접 열어 SPARQL 자격·전제조건 검사, SHACL 역할 권한·오버라이드 정책 검증, Fundació Ave Maria 시뮬레이션, '임상 배치 없음' 문구 확인. 브리프의 source_unopened:true 는 이번 리서치 실행에서 다시 열지 않았다는 뜻이며 검증에서 열람함."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. W3C 권고안(원문 열람)과 HERON 전문(검증 열람) 두 독립 출처로 교차 확인. 코드 상한 규칙(서로 다른 출처 2개, 1개 이상 원문 열람) 충족 — high 유지 가능."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2406.07962(v2 2024-10-18) 초록: few-shot 프롬프트, 구문·모순·환각 점검 반복, 최종 사람 검토·수정만 필요 일치. 검증에서 초록을 직접 열었다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2604.16258 초록: Kimi K2-1T·Llama 3.1-8B·Llama 3.2-3B / Gemini 2.5 Pro·GPT-4.1, 가독성·관련성·구조 복잡성, '사용 사례에 따라 뚜렷한 생성 프로필' 일치. 모델명 표기는 'Kimi K2'로 쓴다(브리프 'KimiK2')."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. W3C OWL 2 구조 명세 2판(2012-12-11) 3.1절 '정확히 하나의 버전이 현재 버전', 3.5절 owl:priorVersion·backwardCompatibleWith·incompatibleWith 정의 일치. 발행 2012 — 2년 초과이나 현행 권고안."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 공식 저장소 raw README 를 검증에서 열어 6개월 뒤 deprecated 이동, 폐기 템플릿 유효·유지보수 중단, 주버전·리비전·버그 수정(Technical Data 2.0.1) 문구 확인. 브리프 sources[] 는 fetched:false 인데 self_check 는 github_raw 열람 1건이라 적어 서로 모순 — 검증 열람으로 실재·일치 확정. 발행일 미확인(README 에 날짜 없음)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. W3C(OWL 2)·IDTA(README) 두 발행 주체를 각각 열어 교차 확인. ref-886 원문 열람이므로 코드 상한 규칙 충족 — high 유지 가능."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Cambridge 초록(2013-08-28): '도메인 변화 또는 정보 시스템의 새 요구에 대응해 최신 유지', '자연어 처리·추론 등 여러 분야 기법을 결합한 다단계 과정' 일치. 단계 이름은 초록에 없음. 발행 2013 — 2년 초과."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2409.13906 초록(저널 Database 2025 baae133): 통제 자연어 명령, patch·diff, GitHub 에이전트, BioPortal 변경 요청 일치."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2409.20302 v19(2026-08-31) 초록: 'skewed measurements', cross-reference 메커니즘, Agent-OM 기반 일치. 정량 결과 없음."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-888·ref-892·ref-893 세 출처를 각각 열어 종합 확인. 단 '호주 국립대학교 계열'은 PDF 메타데이터의 이메일 도메인(anu.edu.au·monash.edu)으로만 짐작되고 인쇄된 소속을 읽지 못했으며 '유럽 연구진'·'생물의학 온톨로지 연구진'도 초록에 없음 — 본문에는 저자명만 쓴다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2406.14470 초록 원문: 'In February 2024, the IDTA announced 84 and released 18 AAS submodel specifications', 'generates API code and tests', 'more than 50000 lines', 'syntactical variations and issues ... require human intervention' 일치. '18개'는 발표 84개 중 '공개된(released) 18개'라는 뜻으로 쓴다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2605.08185 단독 저자 초록: 'identity-preserving reconfiguration criteria', 'compositional conditions ... globally admissible', 'dynamically governable' 일치. 실험 없음 — 저자의 이론적 제안임을 본문에 밝힌다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2609.08869 초록: 다섯 핵심 역량 질문이 온톨로지를 통제, 관찰·증거·출처 추적, 17명 패널에서 신뢰·완전성 증가, 신흥 주식시장(파키스탄·말레이시아·인도네시아) 일치. 금융 도메인이므로 선례로만 쓴다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(부분 뒷받침). arXiv 2604.03496 v2(2026-06-15, ICML 2026 GFM 워크숍) 초록은 '미리 정의된 온톨로지 없이 문맥 지식 그래프·유도 스키마 공동 구축'과 '원문 근거에 대한 완전한 추적 가능성 유지'만 말하고, '사람 검토자가 원문과 대조해 검증할 수 있게 한다'는 용도는 초록에 없다. 추적 가능성 문장만 따로 쓰면 [사실] 가능."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정). f9·f20·f21 종합으로 oq-147 부분 진전·미해결 판단은 세 출처 내용과 맞음. f21 강등에 따라 근거 문구를 '원문 근거 추적'으로 한정한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(문구 정정 조건). 입력 원문 data/source_texts/ref-228.txt: required 에 version 포함, mobileRobotConfiguration 은 required 밖(선택)이며 versions 배열에 하드웨어·소프트웨어 버전(key·value) 일치. 단 스키마의 version 설명은 'Version of the protocol [Major].[Minor].[Patch]'로 팩트시트 자체가 아니라 VDA 5050 프로토콜 판이다 — 본문에서 고친다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정). 인용한 다섯 출처 어디에도 로봇 능력 온톨로지의 개정 영향·재검증 절차 전체를 다룬 내용이 없음을 확인. 리서치 종합이며 low 유지."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정). 어느 출처도 ROP 책임 범위를 직접 말하지 않으므로 구축자·리서치 종합임을 9절에서 밝힌다. low 유지."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정). '연계 대상: ' 표시와 분류 원문 19장(로봇 자체 지능·제어, 업종별 조건) 적용이 적절. low 유지."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정). 연결 대상 영역 번호·이름이 부록 A 와 일치하고 교차 규칙(45·47 양쪽 연결) 적용이 맞음."
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
    "ok": false,
    "overlaps": [
      "참고문헌 id 충돌: 이 브리프의 ref-886(OWL 2)·ref-459(SHACL)·ref-888(Zablith)·ref-889(OOPS!)·ref-890(CQ 데이터셋)은 같은 날 실행 2026-09-29-08 이 다른 URL(vda5050_connector·Sidorenko·황선명·CGH·Järvenpää)에 부여한 번호와 겹친다. 퍼블리셔가 URL 기준으로 새 번호를 배정해야 하며 페이지 각주는 배정 뒤 번호를 따른다.",
      "ref-465(Vieira da Silva 2024)·ref-880(HERON)·ref-228(VDA 5050 팩트시트 스키마)은 2026-09-29-07·08 브리프의 기존 출처 재사용 — 새 각주를 만들지 않고 같은 id 를 쓴다(브리프가 이미 그렇게 함).",
      "f7(HERON 정책 검증)은 2026-09-29-08 f11 과 같은 사실을 같은 출처로 재인용 — 6. 온톨로지 기반 시스템·로봇 연동 페이지와 겹치므로 이 페이지에서는 SHACL 검증 적용 사례로만 짧게 다루고 그 페이지로 연결한다.",
      "f9(언어 모델 능력 온톨로지 생성·사람 최종 검토)는 2026-09-29-07 f20·2026-09-29-08 f24 와 같은 주장 — 여기서는 검증 단계 관점으로만 쓰고 4. 이기종 로봇 등록 페이지로 연결한다."
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f21: [사실] → [추정]으로 강등한다 — 출처 ref-897 초록은 '원문 근거에 대한 완전한 추적 가능성 유지'까지만 말하고 '사람 검토자가 원문과 대조해 검증할 수 있게 한다'는 용도는 없다. 추적 가능성 문장만 단독으로 쓰면 [사실]로 둘 수 있고, 검토자 대조 용도는 [추정]으로 나눠 쓴다.",
    "f23: '팩트시트 자체의 version' 문구를 'VDA 5050 프로토콜 판([Major].[Minor].[Patch])을 뜻하는 version' 으로 고친다 — 스키마 원문(ref-228) 의 version 설명이 'Version of the protocol' 이다. mobileRobotConfiguration.versions 의 하드웨어·소프트웨어 판 서술은 그대로 둔다.",
    "f4·f17: 연 초록 페이지·PDF 에서 확인되지 않은 소속 표현('포즈난 공과대학교·케이프타운 대학교 연구진', '유럽 연구진', '생물의학 온톨로지 연구진', '호주 국립대학교 계열')을 본문에 쓰지 않고 저자명(Wiśniewski 외, Zablith 외, Hegde 외, Qiang 외)으로 발행 주체를 구분한다. f2 의 '암스테르담 자유대학교'는 PDF 로 확인됐으므로 써도 된다(공저자 1명은 토리노 공과대학).",
    "f6·7절 SHACL 행: 기준 판을 'W3C 권고안 2017-07-20' 으로 명시한다 — W3C 가 SHACL 1.2 Core 작업 초안(2026-06-22)을 진행 중이나 이 사실은 브리프에 없으므로 본문에 쓰지 말고 additional_research_requests 에 'SHACL 1.2 작업 초안에서 검증 보고서 구조가 바뀌는지 확인'으로 올린다.",
    "f10: 모델명을 'Kimi K2' 로 표기한다(브리프 'KimiK2'). 출처 초록 표기는 Kimi K2-1T·Llama 3.1-8B·Llama 3.2-3B 다.",
    "f18: '84개 명세 가운데 18개'는 '2024년 2월 기준 발표 84개·공개 18개'로 쓴다 — 초록 원문이 'announced 84 and released 18' 이다.",
    "5절 적용 사례: 가정(f2)은 현장 배치가 아니라 네 로봇 플랫폼 대상 역량 질문 평가, 병원(f7)은 임상 배치 없는 시뮬레이션 시나리오임을 각 사례에 명시하고, 제조 공장·물류창고·상업 시설·실외·기타 사례는 확인되지 않았다고 적는다. site_matrix_updates 는 가정·병원 두 칸만 낸다.",
    "f7·f9: 6. 온톨로지 기반 시스템·로봇 연동 페이지(2026-09-29-08)와 4. 이기종 로봇 등록 페이지(2026-09-29-07)에 같은 출처로 이미 실린 주장이므로 이 페이지에서는 검증 관점으로 짧게 쓰고 해당 페이지로 링크한다. 각주 id 는 ref-880·ref-465 그대로 재사용한다.",
    "ref-439·ref-465·ref-880 각주에는 '(원문 미열람)' 을 붙이지 않고 reference_updates[] 의 source_unopened 를 false 로 낸다 — 검증에서 세 출처의 원문(raw README·arXiv 초록·PMC 전문)을 직접 열어 인용 문구를 확인했다. 브리프의 source_unopened:true 는 이번 리서치 실행에서 다시 열지 않았다는 표시였다.",
    "f19: 단독 저자의 이론적 제안이며 실험·현장 적용이 없음을 본문에 함께 적는다. f20: 금융(신흥 주식시장) 도메인의 선례임을 밝힌다.",
    "9절: f25·f26 이 리서치 에이전트의 종합(어느 출처도 ROP 책임 범위를 직접 말하지 않음)임을 밝히고 [추정]으로 둔다. f26 은 '연계 대상' 으로 짧게 다룬다.",
    "11절: oq-147 은 해결로 바꾸지 않고 '조사 중(부분 진전: 원문 근거 추적·사람 최종 검토 구성은 확인, 로봇 매뉴얼 절·줄 근거 구현은 미확인)' 으로 둔다. open_questions_new 4건은 형식·관련 영역 이름이 맞으므로 그대로 등록한다.",
    "참고문헌 번호: 이 브리프의 ref-886~ref-890 이 같은 날 실행 2026-09-29-08 의 다른 URL 과 번호가 겹치므로 changelog_entry 또는 verification 노트에 '퍼블리셔가 URL 기준으로 번호를 재배정해야 함'을 남긴다. 스토리텔러는 브리프 id 를 그대로 쓰되 reference_updates 에 URL 을 빠짐없이 적는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 26건, 미확인 1건(f21 부분 뒷받침), 교차 확인 4건(f4·f8·f13·f17). 강등: f21 사실 → 추정(원문 근거 추적까지만 초록에 있고 검토자 대조 용도는 없음). 원문 미열람 출처: 없음 — 브리프가 미열람으로 표시한 ref-439(IDTA 서브모델 템플릿 README)·ref-465·ref-880 는 검증에서 직접 열어 확인했으며, ref-228 은 입력 원문 텍스트로 대조했다. 주의: 검증 수단(역량 질문·SPARQL 실행, 추론기, 피트폴 스캐너, SHACL)과 판 식별·호환 표기 규칙(OWL 2 버전 IRI, IDTA 6개월 뒤 폐기)은 각 발행 기관 원문으로 확인됐으나, 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차와 ROP 책임 범위(9절)는 출처 없는 종합 추정이다. 적용 사례는 가정(OntoBOT, 네 로봇 평가·현장 배치 아님)과 병원(HERON, 임상 배치 없는 시뮬레이션) 두 건뿐이며 제조 공장·물류창고·상업 시설·실외 사례는 없다. 국내 자료는 문헌정보학 온톨로지 검증 연구 1건(2015)이다. OWL 2(2012)·Zablith(2013)·OOPS!(2014)·STNet(2015)·SHACL(2017)은 발행 2년 초과로 월간 재검증 대상이며, SHACL 은 W3C 가 1.2 Core 작업 초안(2026-06-22)을 진행 중이므로 2017 권고안을 기준 판으로 명시한다. 신뢰도 medium: 핵심 주장 가운데 f8·f13 은 교차 확인·원문 열람으로 high 요건을 갖췄으나 3·9절의 결론(f24·f25·f26)이 추정이다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-147 부분 진전). 참고문헌 id ref-886~ref-890 이 같은 날 실행 2026-09-29-08 과 번호가 겹쳐 퍼블리셔의 URL 기준 재배정이 필요하다. 검증 예산: 검색 1회(리서치 17회와 합쳐 18/30), 열람 20회(출처 18건 + 소속·초록 재확인 2건).",
  "retry_reason": null
}
```

### runs/2026-09-29-09/pages.json

```json
{
  "run_id": "2026-09-29-09",
  "outline": [
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "검증 수단과 판 표기 규칙은 여러 발행 주체에서 확인되지만 로봇 능력 온톨로지의 개정 영향·재검증 절차는 확인되지 않아 ROP 가 설계해야 할 것으로 보인다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228] 역량 질문·질의·추론기 기반 검증은 세 발행 주체에서 확인되고 표준 명세 자체의 변동이 재검증 부담이 된다. [사실][^ref-890][^ref-891][^ref-899][^ref-895]",
      "planned_findings": [
        "f4",
        "f18",
        "f24"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 750,
      "summary": "역량 질문·온톨로지 피트폴·SHACL 검증 보고서·온톨로지 IRI와 버전 IRI·온톨로지 진화·지식 그래프 변경 언어를 정의한다. [사실][^ref-890][^ref-889][^ref-459][^ref-886][^ref-888][^ref-892]",
      "planned_findings": [
        "f1",
        "f5",
        "f6",
        "f11",
        "f14",
        "f15"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1000,
      "summary": "가정(OntoBOT, 네 로봇 플랫폼 대상 역량 질문 평가, 현장 배치 아님)과 병원(HERON, 임상 배치 없는 시뮬레이션의 SHACL 정책 검증) 두 사례만 확인됐다. [사실][^ref-891][^ref-880]",
      "planned_findings": [
        "f2",
        "f7"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1700,
      "summary": "역량 질문 기반 완전성 확인, 추론기·피트폴 스캐너·SHACL 자동 평가, 언어 모델 결합 검증, 판 식별·호환 표기, 변경 표현·탐지·허용성 판단, 원문 근거를 붙인 검토의 여섯 갈래가 있다. [사실][^ref-890][^ref-459][^ref-886][^ref-892] 로봇 매뉴얼 절·줄 근거를 붙인 확정·반려 구현은 확인되지 않았다. [추정][^ref-896][^ref-897][^ref-465]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f15",
        "f16",
        "f17",
        "f19",
        "f20",
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 650,
      "summary": "OWL 2 버전 IRI, W3C SHACL 권고안(2017-07-20), OOPS!, IDTA 서브모델 템플릿 저장소 규칙, KGCL, VDA 5050 팩트시트의 판 정보를 표로 정리한다. [사실][^ref-886][^ref-459][^ref-889][^ref-439][^ref-892][^ref-228]",
      "planned_findings": [
        "f5",
        "f6",
        "f11",
        "f12",
        "f15",
        "f23"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1000,
      "summary": "역량 질문 데이터셋, OntoBOT, OOPS!, 온톨로지 진화 서베이, KGCL, OM4OV, IDTA 명세 모델 기반 구현, RoSO/SMGI, OntoKG-EQ, TRACE-KG, 국내 STNet 연구를 요약한다. [사실][^ref-890][^ref-891][^ref-889][^ref-888][^ref-892][^ref-893][^ref-895][^ref-900][^ref-896][^ref-897][^ref-899]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f14",
        "f15",
        "f16",
        "f18",
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 650,
      "summary": "ROP 는 역량 질문 목록·테스트 실행 기록·SHACL 형상과 검증 보고서·판 식별자·변경 기술·재검증 목록을 맡고, 펌웨어 릴리스 관리와 템플릿 개정·폐기 일정은 제조사·표준 발행 기관의 연계 대상으로 두는 것이 리서치 종합의 추정이다. [추정][^ref-890][^ref-459][^ref-886][^ref-892][^ref-228][^ref-439]",
      "planned_findings": [
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 550,
      "summary": "4·5·6번 온톨로지 영역, 21·57번 판 규칙, 54번 시험·형식 검증, 45·47번 언어 모델 방법, 63·65번 현장 유형 영역과 잇는다. [추정][^ref-439][^ref-459][^ref-465][^ref-898]",
      "planned_findings": [
        "f27"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "section": "11. 열린 질문",
      "budget_chars": 650,
      "summary": "oq-147 은 부분 진전으로 조사 중이며, 개정 감지·재검증 절차, 지원 단계 표시 체계, 국내 사례, IDTA 폐기 판 이관 기준의 새 질문 4건을 올린다. [추정][^ref-896][^ref-897][^ref-465]",
      "planned_findings": [
        "f22",
        "f24",
        "f25",
        "f3",
        "f12"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/robot-ontology/ontology-verification-and-change-management.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"6. 대표 접근법과 기술\" 절(2,811자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"8. 대표 연구와 자료\" 절(1,834자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"4. 핵심 개념과 용어\" 절(1,478자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"11. 열린 질문\" 절(1,150자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,053자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"3. 왜 중요한가\" 절(909자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area07-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 7. 온톨로지 검증·변경 관리 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(743자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 7. 온톨로지 검증·변경 관리 | 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건 이행), version 2; 참고문헌 ref-886~ref-890 이 같은 날 실행 2026-09-29-08 의 다른 URL 과 번호가 겹쳐 퍼블리셔가 URL 기준으로 번호를 재배정해야 함 | run 2026-09-29-09",
  "index_updates": {
    "home_recent": "2026-09-29 — 7. 온톨로지 검증·변경 관리: 역량 질문·SHACL·피트폴 스캐너 기반 검증과 OWL 2 버전 IRI·IDTA 템플릿 폐기 규칙 등 판 관리 관행을 정리하고, 로봇 능력 온톨로지의 개정 영향·재검증 절차는 미확인으로 남겼다(가정·병원 사례 2건, 신뢰도 medium)",
    "category_recent": "2026-09-29 — 7. 온톨로지 검증·변경 관리: 섹션 3~11 신규 작성(역량 질문·자동 평가·언어 모델 결합 검증·판 식별·변경 표현·원문 근거 검토 여섯 갈래), 열린 질문 4건 신규·oq-147 조사 중, 실행 2026-09-29-09",
    "area_recent": "2026-09-29 — 7. 온톨로지 검증·변경 관리: 영역 심화로 3~11절을 처음 채웠다. 검증 수단과 판 표기 규칙은 여러 발행 주체에서 확인됐으나 로봇 능력 온톨로지의 개정 감지·재검증 절차와 매뉴얼 절·줄 근거 검토 구현은 미확인이다(실행 2026-09-29-09)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "competency-question",
      "term_ko": "역량 질문",
      "term_en": "Competency Question (CQ)",
      "definition": "온톨로지가 답할 수 있어야 하는 질문으로 요구사항을 적은 것으로, SPARQL 같은 질의로 형식화해 온톨로지가 요구를 충족하는지 검증하는 데 쓴다.",
      "description": "Wiśniewski 외(2018)는 여러 도메인 온톨로지의 역량 질문 234개와 SPARQL-OWL 번역, 106개 질문 패턴과 46개 질의 서명의 대응을 공개해 역량 질문의 형식화·실행·관리를 지원하는 벤치마크로 제시했다. 로봇 온톨로지 OntoBOT 도 역량 질문으로 평가되었다.",
      "related_areas": [
        7,
        5,
        54
      ],
      "sources": [
        "ref-890",
        "ref-891"
      ]
    },
    {
      "action": "new",
      "slug": "ontology-pitfall",
      "term_ko": "온톨로지 피트폴",
      "term_en": "Ontology Pitfall",
      "definition": "온톨로지 모델링에서 흔히 생기는 결함 유형으로, 피트폴 스캐너(OOPS!)가 구조·기능·사용성 차원의 카탈로그와 심각·중요·경미 중요도로 자동 탐지한다.",
      "description": "OOPS!(OntOlogy Pitfall Scanner!)는 693개 이상의 온톨로지를 경험적으로 분석해 만든 카탈로그를 바탕으로 기술 논리에 익숙하지 않은 도메인 전문가도 온라인에서 결함을 탐지하게 한 도구다(2014).",
      "related_areas": [
        7
      ],
      "sources": [
        "ref-889"
      ]
    },
    {
      "action": "new",
      "slug": "version-iri",
      "term_ko": "버전 IRI",
      "term_en": "Version IRI (owl:versionIRI)",
      "definition": "OWL 2 에서 같은 온톨로지 IRI 를 공유하는 온톨로지 시리즈 가운데 특정 판을 식별하는 IRI 로, 이전 판·호환·비호환 주석과 함께 온톨로지 버전 관리에 쓴다.",
      "description": "W3C OWL 2 구조 명세 2판(2012-12-11)은 같은 온톨로지 시리즈에서 정확히 하나의 버전만 현재 버전으로 보고, owl:priorVersion·owl:backwardCompatibleWith·owl:incompatibleWith 주석으로 판 사이 관계를 표기한다.",
      "related_areas": [
        7,
        57
      ],
      "sources": [
        "ref-886"
      ]
    },
    {
      "action": "new",
      "slug": "ontology-evolution",
      "term_ko": "온톨로지 진화",
      "term_en": "Ontology Evolution",
      "definition": "도메인 변화나 정보 시스템 요구 변화에 대응해 온톨로지를 최신 상태로 유지하는 활동으로, 변경 감지·표현·적용·영향 관리를 포함하는 다단계 과정으로 다뤄진다.",
      "description": "Zablith 외(2013)의 프로세스 중심 서베이는 전형적 접근이 자연어 처리·추론 등 여러 분야 기법을 결합한 다단계 과정으로 설계된다고 정리했다. 단계 이름은 초록에서 확인되지 않았다.",
      "related_areas": [
        7
      ],
      "sources": [
        "ref-888"
      ]
    }
  ],
  "reference_updates": [
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
    },
    {
      "id": "ref-459",
      "org": "W3C (RDF Data Shapes Working Group)",
      "title": "Shapes Constraint Language (SHACL)",
      "published": "2017-07-20",
      "url": "https://www.w3.org/TR/shacl/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "RDF 데이터 그래프를 형상 그래프의 조건으로 검증하는 W3C 권고안. 검증 보고서 구조(sh:conforms·sh:result·sh:resultSeverity)를 정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
    },
    {
      "id": "ref-439",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "submodel-templates — IDTA Submodel Templates for AAS (README)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "IDTA 서브모델 템플릿 공식 저장소 README. published·deprecated 폴더, 주버전·리비전·버그 수정 표기, 새 판 6개월 뒤 이전 판 폐기 규칙을 적는다. 검증에서 raw README 원문을 열어 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "summary": "자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성하고 구문 검증·모순 탐지·환각·누락 점검을 자동 루프로 돌린 뒤 사람이 최종 검토하는 방법. 검증에서 초록을 직접 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
    },
    {
      "id": "ref-880",
      "org": "Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel)",
      "title": "HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics",
      "published": "2025-04-30",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "의료 로봇 상위 온톨로지 HERON. SPARQL 자격·전제조건 검사와 SHACL 정책 검증을 의료센터 물류·플릿 조정 시뮬레이션 시나리오로 시연. 검증에서 PMC 전문을 직접 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
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
      "summary": "VDA 5050 3.0.0 팩트시트 JSON 스키마. VDA 5050 프로토콜 판을 뜻하는 version 등 필수 속성과 하드웨어·소프트웨어 버전을 담는 선택 속성 mobileRobotConfiguration 을 정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/ontology-verification-and-change-management.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-147",
      "question": "문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가?",
      "areas": [
        4,
        45,
        7
      ],
      "status": "조사 중",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 능력 온톨로지에 대해 펌웨어·매뉴얼 개정을 감지해 영향받는 작업·현장을 찾고 재검증 대기열에 넣는 절차를 구현한 공개 구현이나 현장 사례가 있는가?",
      "areas": [
        7,
        57,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가?",
      "areas": [
        7,
        54,
        36
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내에서 역량 질문·추론기·SHACL 로 로봇 온톨로지를 검증하거나 버전을 관리한 연구·현장 사례가 있는가(이번 조사에서 확인된 국내 자료는 학술용어사전 온톨로지 검증 연구 1건이다)?",
      "areas": [
        7,
        5
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가?",
      "areas": [
        7,
        21,
        4
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "가정",
      "item": "완료·인계",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시",
      "title": "7. 온톨로지 검증·변경 관리"
    }
  ],
  "standards_updates": [
    {
      "name": "OWL 2 Web Ontology Language Structural Specification (Second Edition)",
      "kind": "표준",
      "org": "W3C",
      "url": "https://www.w3.org/TR/owl2-syntax/",
      "related_areas": [
        7,
        5,
        57
      ],
      "summary": "온톨로지 IRI·버전 IRI 로 판을 식별하고 owl:priorVersion·backwardCompatibleWith·incompatibleWith 주석으로 이전 판 관계를 표기하는 OWL 2 구조 명세 2판(2012-12-11).",
      "ref_id": "ref-886"
    },
    {
      "name": "IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/submodel-templates",
      "related_areas": [
        7,
        21,
        4
      ],
      "summary": "published·deprecated 폴더, 주버전·리비전·버그 수정 표기, 새 판 발행 6개월 뒤 이전 판을 deprecated 로 옮기는 규칙을 README 로 정한다.",
      "ref_id": "ref-439"
    },
    {
      "name": "KGCL (Knowledge Graph Change Language)",
      "kind": "프레임워크",
      "org": "Hegde, H. 외 (Database, Oxford)",
      "url": "https://arxiv.org/abs/2409.13906",
      "related_areas": [
        7
      ],
      "summary": "온톨로지·지식 그래프의 변경을 통제 자연어 명령·패치·diff 로 요청·기술하는 표준 데이터 모델. GitHub 저장소 에이전트와 BioPortal 변경 요청 인터페이스로 구현되었다.",
      "ref_id": "ref-892"
    }
  ],
  "additional_research_requests": [
    "7절 SHACL 행에 필요한 사실: W3C 가 진행 중인 SHACL 1.2 Core 작업 초안(2026-06-22)에서 검증 보고서 구조(sh:conforms·sh:result·sh:resultSeverity)가 바뀌는지 확인 — 검증이 언급했으나 브리프에 없어 본문에 쓰지 않았다",
    "5절에 필요한 사실: 제조 공장·물류창고·상업 시설·실외·기타 현장 유형의 온톨로지 검증·변경 관리 적용 사례 — 특히 Köcher·Vieira da Silva·Fay 'Constraint Checking of Skills using SHACL'(INDIN 2021)의 서지 확인(제조 공장 사례 후보)",
    "6·11절에 필요한 사실: 분류 원문의 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 검증 수준·성숙도 체계를 정의한 출처",
    "4절에 필요한 사실: Zablith 외(2013) 온톨로지 진화 서베이의 단계 이름(초록에서 확인되지 않아 본문에 쓰지 않았다)",
    "6·11절(oq-147)에 필요한 사실: 로봇 매뉴얼·URDF 에서 추출한 능력 항목에 매뉴얼 절·줄 근거를 붙여 확정·반려하는 공개 구현 — IDTA 'How to write a SMT v1.1' 지침, Dibowski 'Full Traceability and Provenance for Knowledge Graphs'(FOIS 2024), MDPI 'Grounded Knowledge Graph Extraction via LLMs' 원문 열람",
    "8절에 필요한 사실: 국내에서 로봇 온톨로지를 역량 질문·추론기·SHACL 로 검증하거나 버전을 관리한 연구·현장 사례(이번 조사는 문헌정보학 온톨로지 검증 연구 1건뿐)",
    "4·8절에 필요한 사실: 역량 질문의 원 제안(Grüninger·Fox 1995)과 요구사항 기반 검증 도구 Themis 의 서지 — 원문·서지를 확인하지 못해 쓰지 않았다"
  ],
  "fixes_applied": [
    "f21 강등 — 6절 '원문 근거를 붙인 검토'에서 TRACE-KG 의 '원문 근거에 대한 완전한 추적 가능성 유지' 문장만 [사실][^ref-897]로 두고, 사람 검토자가 원문과 대조해 검증하는 용도는 별도 문장으로 나눠 [추정][^ref-897]로 썼다",
    "f23 문구 정정 — 7절 VDA 5050 팩트시트 행을 'VDA 5050 프로토콜 판([Major].[Minor].[Patch])을 뜻하는 version 을 필수 속성으로 두고' 로 고쳤고, mobileRobotConfiguration 의 하드웨어·소프트웨어 판 서술은 그대로 두었다",
    "f4·f17 소속 표현 제거 — 3·6절에서 '포즈난 공과대학교·케이프타운 대학교 연구진', '유럽 연구진', '생물의학 온톨로지 연구진', '호주 국립대학교 계열'을 쓰지 않고 Wiśniewski 외·Martorana 외·고영만 외·Zablith 외·Hegde 외·Qiang 외 저자명으로 발행 주체를 구분했다. f2 는 '암스테르담 자유대학교'를 5절과 각주에 썼다",
    "SHACL 기준 판 명시 — 4·6·7절과 7절 표 아래 문장에서 'W3C 권고안 2017-07-20' 을 기준 판으로 적었고, SHACL 1.2 작업 초안은 본문에 쓰지 않고 additional_research_requests 첫 항목에 '검증 보고서 구조가 바뀌는지 확인'으로 올렸다",
    "f10 모델명 — 6절에서 'Kimi K2' 로 표기했다",
    "f18 문구 — 3·8절에서 '2024년 2월 기준 IDTA 가 발표한 84개·공개한 18개 명세' 로 썼다",
    "5절 적용 사례 — 가정 사례에 현장 배치가 아니라 네 로봇 플랫폼 대상 역량 질문 평가임을, 병원 사례에 임상 배치 없는 시뮬레이션 시나리오임을 표와 서술에 명시했고, 5절 첫 단락에 제조 공장·물류창고·상업 시설·실외·기타 사례는 확인되지 않았다고 적었다. site_matrix_updates 는 가정·병원 두 현장 유형만 냈다",
    "f7·f9 중복 처리 — HERON 은 5절 병원 사례와 6절 '자동 평가 도구'에서 SHACL 검증 관점으로만 짧게 다루고 6. 온톨로지 기반 시스템·로봇 연동 페이지로 링크했으며, Vieira da Silva 외는 6절 '언어 모델을 결합한 검증'에서 검증 단계 관점으로만 쓰고 4. 이기종 로봇 등록 페이지로 링크했다. 각주 id 는 ref-880·ref-465 를 그대로 재사용했다",
    "원문 미열람 표시 제거 — ref-439·ref-465·ref-880 의 13절 각주에 '(원문 미열람)' 을 붙이지 않았고 reference_updates 의 source_unopened 를 모두 false 로 냈다",
    "f19·f20 조건 — 6절과 8절에서 Osmani(2026)를 단독 저자의 이론적 프리프린트이며 실험·현장 적용이 없다고 적었고, OntoKG-EQ 를 금융(신흥 주식시장) 도메인의 선례라고 밝혔다",
    "9절 — 첫 문장에 어느 출처도 ROP 책임 범위를 직접 말하지 않아 리서치 에이전트의 종합이며 전부 추정임을 밝히고 f25·f26 을 [추정]으로 두었으며, f26 은 표의 '외부와 연계하는 것' 열에 '연계 대상:' 으로 짧게 다뤘다",
    "11절 — oq-147 을 해결로 바꾸지 않고 '상태: 조사 중' 에 부분 진전(원문 근거 추적·사람 최종 검토 구성은 확인, 로봇 매뉴얼 절·줄 근거 구현은 미확인)을 적었고, open_question_updates 에 update(조사 중)로 냈다. open_questions_new 4건은 질문 문장·관련 영역 번호를 그대로 new 로 등록했다",
    "참고문헌 번호 충돌 — changelog_entry 에 'ref-886~ref-890 이 같은 날 실행 2026-09-29-08 의 다른 URL 과 번호가 겹쳐 퍼블리셔가 URL 기준으로 번호를 재배정해야 함' 을 남겼고, 페이지 각주는 브리프 id 를 그대로 쓰되 reference_updates 18건 모두에 URL 을 적었다",
    "분량 초과 자동 분리: 7. 온톨로지 검증·변경 관리 본문 12,274자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,482자"
  ]
}
```

### runs/2026-09-29-09/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area07-s6.md (2,811자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area07-s8.md (1,834자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area07-s4.md (1,478자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area07-s11.md (1,150자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area07-s7.md (1,053자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area07-s3.md (909자)
    - docs/categories/robot-ontology/ontology-verification-and-change-management.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area07-s10.md (743자)
```

### runs/2026-09-29-09/pages/categories/robot-ontology/ontology-verification-and-change-management.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리"
type: area
category: "B. 로봇 온톨로지"
area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [역량 질문, SHACL, 버전 IRI, 온톨로지 진화, 피트폴 스캐너, 서브모델 템플릿 폐기]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-886, ref-459, ref-888, ref-889, ref-890, ref-891, ref-892, ref-893, ref-439, ref-895, ref-896, ref-897, ref-898, ref-899, ref-900, ref-465, ref-880, ref-228]
last_run: 2026-09-29
version: 2
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

온톨로지를 검증하는 수단과 판을 표기하는 규칙은 여러 발행 주체에서 확인되지만, 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없어 ROP 가 판 식별·변경 표현·펌웨어 판 보고를 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 왜 중요한가](../../topics/2026/2026-09-29-area07-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 검증 쪽(역량 질문·피트폴·형상 검증)과 변경 쪽(버전 IRI·온톨로지 진화·변경 언어)으로 나뉜다. [사실][^ref-890][^ref-889][^ref-459][^ref-886][^ref-888][^ref-892]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area07-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 적용 사례는 가정(네 로봇 플랫폼 대상 역량 질문 평가)과 병원(임상 배치 없는 시뮬레이션) 두 건뿐이며, 둘 다 현장 배치 사례가 아니다. [사실][^ref-891][^ref-880] 제조 공장·물류창고·상업 시설·실외·기타 현장 유형의 온톨로지 검증·변경 관리 사례는 확인되지 않았다.

**현장 유형:** 가정

**사례:** 가정용 개인 서비스 로봇 온톨로지를 네 로봇 플랫폼에 대해 역량 질문으로 평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 서로 다른 네 로봇 플랫폼의 작업·행동·환경·능력을 한 온톨로지에 통합 표현해야 할 때, 온톨로지가 요구를 충족하는지 역량 질문으로 평가한다. [사실][^ref-891] |
| 작업 대상 | 정보 — SOMA·DOLCE 를 확장한 온톨로지 OntoBOT 의 작업·행동·환경·능력 표현. [사실][^ref-891] |
| 수행 자원 | 평가 대상 로봇은 TIAGo·HSR·UR3·Stretch 네 종이며, 검증 수단은 역량 질문과 형식적 추론이다. [사실][^ref-891] |
| 제약 | 노인과 지원이 필요한 사람을 돕는 가정 내 개인 서비스 로봇이 대상이며, 현장 배치가 아니라 온톨로지 평가다. [사실][^ref-891] |
| 완료·인계 | 역량 질문에 온톨로지가 답할 수 있음이 확인되면 평가를 마친 것으로 본다. [사실][^ref-891] |
| 예외·성과 | 해당 없음 |

Martorana·Urgese·Tiddi·Schlobach(암스테르담 자유대학교, 2025)의 OntoBOT 은 SOMA·DOLCE 를 확장해 가정용 개인 서비스 로봇의 작업·행동·환경·능력을 통합 표현하는 온톨로지이며, 역량 질문으로 평가하고 TIAGo·HSR·UR3·Stretch 네 로봇에 대해 검증했다. [사실][^ref-891] 이 사례는 가정에 배치한 운영 사례가 아니라 네 로봇 플랫폼을 대상으로 한 온톨로지 평가이며, 가정 현장 배치 여부는 초록에서 확인되지 않았다. 이 영역의 관점에서 보면 역량 질문이 '온톨로지가 빠짐없는가'를 묻는 완료 기준 역할을 한다.

**현장 유형:** 병원

**사례:** 의료센터 물류 운반·다중 로봇 플릿 조정 시뮬레이션에서 온톨로지로 자격·정책을 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료센터의 물류 운반과 다중 로봇 플릿 조정 시뮬레이션 시나리오에서 작업이 요청된다. [사실][^ref-880] |
| 작업 대상 | 의료센터 물류 운반 대상과, 에이전트 자격·전제조건·기관 정책이라는 정보. [사실][^ref-880] |
| 수행 자원 | 시뮬레이션 안의 다중 로봇 플릿과 상위 온톨로지 HERON 의 SPARQL·SHACL 추론. [사실][^ref-880] |
| 제약 | SPARQL 질의로 작업에 대한 에이전트 자격·전제조건을 검사하고, SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증한다. [사실][^ref-880] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

Ioannidou 외(2025)의 의료 로봇 상위 온톨로지 HERON 은 임상 배치 없이 의료센터의 시뮬레이션 시나리오로 시연되었다. [사실][^ref-880] 이 페이지에서는 SHACL 형상 검증의 적용 사례로만 짧게 다루며, 온톨로지 기반 연동 자체는 [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)에 같은 출처로 실려 있다. 역할 기반 권한 정책의 내용은 [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)의 범위다.

## 6. 대표 접근법과 기술

확인된 접근법은 역량 질문 기반 완전성 확인, 자동 평가 도구, 언어 모델 결합 검증, 판 식별·호환 표기, 변경 표현·탐지·허용성 판단, 원문 근거를 붙인 검토의 여섯 갈래이며, 어느 것도 로봇 능력 온톨로지의 개정 영향·재검증 절차 전체를 다루지는 않는다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area07-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

판 식별은 OWL 2, 인스턴스 제약 검증은 SHACL 권고안(2017-07-20), 결함 탐지는 OOPS!, 템플릿 폐기 규칙은 IDTA 저장소, 변경 기술은 KGCL, 로봇 펌웨어·소프트웨어 판 보고는 VDA 5050 팩트시트가 맡는다. [사실][^ref-886][^ref-459][^ref-889][^ref-439][^ref-892][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area07-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 검증 쪽 5건, 변경 쪽 5건, 국내 1건이며 로봇 능력 온톨로지를 직접 다루는 것은 OntoBOT 과 RoSO/SMGI 뿐이다. [사실][^ref-890][^ref-891][^ref-889][^ref-888][^ref-892][^ref-893][^ref-895][^ref-900][^ref-896][^ref-897][^ref-899]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 대표 연구와 자료](../../topics/2026/2026-09-29-area07-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 절의 경계 판단은 어느 출처도 ROP 의 책임 범위를 직접 말하지 않으므로 리서치 에이전트가 확인된 수단을 묶은 종합이며, 전부 추정이다. [추정][^ref-890][^ref-459][^ref-886][^ref-892]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트의 하드웨어·소프트웨어 판 정보를 받아 온톨로지 재검증을 촉발하고, 영향받는 작업·현장의 재검증 목록을 관리한다. [추정][^ref-228] | 연계 대상: 로봇 펌웨어·소프트웨어의 릴리스 관리와 펌웨어 검증 자체는 제조사가 맡는다. [추정][^ref-228] |
| 업종별 조건 | 표준 발행 기관의 템플릿 폐기 통보를 받아 그 판에 묶인 능력 정의를 재검증 대기열에 넣는다. [추정][^ref-439] | 연계 대상: 서브모델 템플릿의 개정·폐기 일정과 유지보수는 IDTA 같은 표준 발행 기관이 맡는다. [추정][^ref-439] |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 능력 온톨로지의 역량 질문 목록과 그 SPARQL 테스트 실행 기록, SHACL 형상과 검증 보고서, 추론기 일관성 검사, 온톨로지 판 식별자와 이전 판 관계 표기, 변경 기술(변경 언어)과 영향받는 작업·현장의 재검증 목록이며, 원문 근거를 붙인 검토·확정 기록은 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md)의 검토·승인과 같은 기록을 공유해야 할 것으로 보인다. [추정][^ref-890][^ref-459][^ref-886][^ref-892] 이 경계는 제품 전략에 따라 이동할 수 있으며, 이종 제조사를 연결하는 ROP 는 펌웨어와 표준 템플릿을 만들지 않고 그 판 정보를 받아 재검증을 촉발하는 인터페이스와 실행 보장에 머무는 것이 분류 원문 19장의 취지와 맞다. 범위 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 앞뒤의 온톨로지 영역, 판 규칙을 다루는 표준·수명주기 영역, 테스트 방법을 다루는 검증 영역, 언어 모델 방법을 다루는 AI 영역과 이어진다. [추정][^ref-439][^ref-459][^ref-465][^ref-898]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area07-s10.md)에 있다.

## 11. 열린 질문

기존 질문 oq-147 은 원문 근거 추적과 사람 최종 검토 구성만 확인되어 조사 중으로 남고, 개정 감지·재검증 절차, 지원 단계 표시 체계, 국내 사례, IDTA 폐기 판 이관 기준의 새 질문 4건을 올린다. [추정][^ref-896][^ref-897][^ref-465]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 열린 질문](../../topics/2026/2026-09-29-area07-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-888]: Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review), Ontology evolution: a process-centric survey, 2013-08-28, https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article, 접근일 2026-09-29
[^ref-889]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-891]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-893]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-895]: Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?, 2024-06-20, https://arxiv.org/abs/2406.14470, 접근일 2026-09-29
[^ref-896]: Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying, 2026-09-08, https://arxiv.org/abs/2609.08869, 접근일 2026-09-29
[^ref-897]: Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation, 2026-04-03, https://arxiv.org/abs/2604.03496, 접근일 2026-09-29
[^ref-898]: Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models, 2026-04-17, https://arxiv.org/abs/2604.16258, 접근일 2026-09-29
[^ref-899]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29
[^ref-900]: Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance, 2026-05-05, https://arxiv.org/abs/2605.08185, 접근일 2026-09-29
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-880]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
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

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s6.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-465, ref-880, ref-886, ref-459, ref-888, ref-889, ref-890, ref-891, ref-892, ref-893, ref-439, ref-896, ref-897, ref-898, ref-899, ref-900]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#6
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술

# 7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인된 접근법은 역량 질문 기반 완전성 확인, 자동 평가 도구, 언어 모델 결합 검증, 판 식별·호환 표기, 변경 표현·탐지·허용성 판단, 원문 근거를 붙인 검토의 여섯 갈래이며, 어느 것도 로봇 능력 온톨로지의 개정 영향·재검증 절차 전체를 다루지는 않는다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인된 접근법은 역량 질문 기반 완전성 확인, 자동 평가 도구, 언어 모델 결합 검증, 판 식별·호환 표기, 변경 표현·탐지·허용성 판단, 원문 근거를 붙인 검토의 여섯 갈래이며, 어느 것도 로봇 능력 온톨로지의 개정 영향·재검증 절차 전체를 다루지는 않는다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]

### 역량 질문 기반 완전성 확인

역량 질문을 SPARQL 질의로 형식화해 온톨로지에 실행하면 요구를 충족하는지를 반복 확인할 수 있다. Wiśniewski 외(2018)의 데이터셋은 역량 질문 234개와 SPARQL-OWL 번역, 106개 질문 패턴과 46개 질의 서명의 대응을 공개해 이 형식화·실행·관리를 지원한다. [사실][^ref-890] 로봇 온톨로지 쪽에서는 OntoBOT 이 역량 질문으로 평가하고 네 로봇에 대해 검증했다. [사실][^ref-891] 국내에서는 고영만 외(한국문헌정보학회지 49권 3호, 2015)가 학술용어사전 STNet 에 온톨로지 구조를 도입하면서 Pellet 추론기로 TBox 를 검증해 생성한 추론규칙이 모두 참임을 확인하고 SPARQL 검색 시나리오로 의미 검색 성능을 평가했으며, 이는 이번 조사에서 확인된 유일한 국내 온톨로지 검증 연구다. [사실][^ref-899] 세 연구는 발행 주체가 다르고 서로 인용 관계가 아니므로 역량 질문·질의 기반 검증은 한 곳 이상에서 확인된다. [사실][^ref-890][^ref-891][^ref-899]

### 자동 평가 도구: 추론기, 피트폴 스캐너, 형상 검증

OOPS! 는 기술 논리에 익숙하지 않은 도메인 전문가를 위해 온톨로지의 모델링 결함을 온라인에서 탐지하는 도구다. [사실][^ref-889] SHACL 은 인스턴스 데이터가 형상의 조건을 지키는지 검증하고 적합 여부·개별 결과·심각도를 담은 보고서를 낸다. [사실][^ref-459] W3C 의 SHACL 권고안(2017-07-20)과 HERON 의 SHACL 정책 검증은 발행 주체가 다르므로, 온톨로지 인스턴스 데이터의 제약 검증 수단으로서 SHACL 은 한 곳 이상에서 확인된다. [사실][^ref-459][^ref-880] 세 도구는 잡아내는 것이 다르다. 추론기는 논리적 모순을, 피트폴 스캐너는 모델링 관행의 결함을, 형상 검증은 데이터 인스턴스의 제약 위반을 낸다.

### 언어 모델을 결합한 검증

Vieira da Silva 외(2024)는 자연어 능력 설명에서 언어 모델로 능력 온톨로지를 생성한 뒤 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행하고 사람이 최종 검토·수정만 하게 하여, 검증 단계에 자동 검사와 사람 검토를 결합했다. [사실][^ref-465] 생성 방법 자체는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)에 같은 출처로 실려 있다. Alharbi 외(2026)는 개방형(Kimi K2·Llama 3.1·3.2)과 폐쇄형(Gemini 2.5 Pro·GPT 4.1) 언어 모델이 생성한 역량 질문을 가독성·입력 텍스트 관련성·구조적 복잡성 지표로 여러 도메인에서 평가해, 모델의 생성 프로필이 사용 사례에 따라 뚜렷이 달라진다고 보고했다. [사실][^ref-898] 이 방법들은 교차 규칙에 따라 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)와 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)에도 연결된다.

### 판 식별과 호환·폐기 표기

OWL 2 는 버전 IRI 와 이전 판·호환·비호환 주석으로 판 사이 관계를 표기한다. [사실][^ref-886] IDTA 서브모델 템플릿 공식 저장소 README 는 템플릿을 published·deprecated 폴더로 관리하고 판을 주버전·리비전·버그 수정으로 표기하며, 새 판 발행 6개월 뒤 이전 판을 deprecated 로 옮기되 그 템플릿은 계속 유효하나 버그 수정·개선·갱신을 더 제공하지 않는다고 정한다. [사실][^ref-439] W3C 와 IDTA 가 각각 정의했으므로 '판 식별자 + 이전 판 관계 명시'는 온톨로지·모델 버전 관리의 관행으로 한 곳 이상에서 확인된다. [사실][^ref-886][^ref-439]

### 변경의 표현·탐지와 재구성 허용성

KGCL 은 변경을 통제 자연어 명령으로 요청·기술하며 GitHub 온톨로지 저장소 자동화 에이전트와 BioPortal 변경 요청 인터페이스로 구현되었다. [사실][^ref-892] Qiang·Taylor·Wang 의 OM4OV(2024, 2026 개정)는 온톨로지 매칭 시스템을 온톨로지 버전 간 변경 비교에 재사용할 수 있지만 확장 없이는 왜곡된 측정을 낸다고 분석하고, 기존 정렬을 활용해 후보를 줄이는 교차 참조 메커니즘을 더한 버전 비교 프레임워크를 제안했다. [사실][^ref-893] Zablith 외, Hegde 외, Qiang 외가 온톨로지 변경의 정의·표현·탐지를 각각 다루어 온톨로지 변경 관리가 별도 연구 분야로 존재함은 한 곳 이상에서 확인되나, 세 출처 모두 로봇 능력 온톨로지를 다루지는 않는다. [사실][^ref-888][^ref-892][^ref-893] Osmani(2026)는 로봇 서비스 온톨로지(RoSO)를 구조적 일반지능 모델(SMGI)의 의미 계층으로 두고, 서비스 재구성 뒤에도 서비스 기술이 유효하게 남기 위한 정체성 보존 재구성 기준과 지역적으로 허용되는 갱신이 전역적으로도 허용되는 조합 조건을 제시해 런타임 변경의 허용 여부를 판단하는 거버넌스를 제안했다. [사실][^ref-900] 이 제안은 단독 저자의 이론적 프리프린트이며 실험·현장 적용은 초록에 없다.

### 원문 근거를 붙인 검토

Nasir 외(2026)의 OntoKG-EQ 는 다섯 개의 고정된 역량 질문으로 정당화된 핵심 온톨로지가 모든 클래스·속성·형상 제약·지표를 통제하고, 각 답에 관찰·증거·출처까지 추적하는 설명을 붙여 검증된 그래프에서 결정론적으로 만들며, 17명 패널 연구에서 증거 묶음이 인지된 신뢰도와 완전성을 크게 높였다고 보고했다. [사실][^ref-896] 이 연구는 금융(신흥 주식시장) 도메인의 선례다. Abolhasani 외(2026)의 TRACE-KG 는 미리 정의한 온톨로지 없이 문맥이 풍부한 지식 그래프와 유도 스키마를 함께 만들면서 원문 근거에 대한 완전한 추적 가능성을 유지한다. [사실][^ref-897] 이 추적 가능성을 사람 검토자가 자동 추출 결과를 원문과 대조해 검증하는 데 쓸 수 있다는 것은 초록에 없는 용도 해석이다. [추정][^ref-897] 원문 근거 추적 구성과 사람 최종 검토 구성은 각각 확인되지만, 로봇 매뉴얼·URDF(Unified Robot Description Format)에서 뽑은 능력 항목에 매뉴얼의 절·줄 위치를 붙여 확정·반려하는 공개 구현은 이번 조사에서도 확인되지 않아 열린 질문 oq-147 은 부분 진전에 그친다. [추정][^ref-896][^ref-897][^ref-465]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-880]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-888]: Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review), Ontology evolution: a process-centric survey, 2013-08-28, https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article, 접근일 2026-09-29
[^ref-889]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-891]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-893]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-896]: Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying, 2026-09-08, https://arxiv.org/abs/2609.08869, 접근일 2026-09-29
[^ref-897]: Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation, 2026-04-03, https://arxiv.org/abs/2604.03496, 접근일 2026-09-29
[^ref-898]: Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models, 2026-04-17, https://arxiv.org/abs/2604.16258, 접근일 2026-09-29
[^ref-899]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29
[^ref-900]: Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance, 2026-05-05, https://arxiv.org/abs/2605.08185, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s8.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 대표 연구와 자료"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-888, ref-889, ref-890, ref-891, ref-892, ref-893, ref-895, ref-896, ref-897, ref-899, ref-900]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#8
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 대표 연구와 자료

# 7. 온톨로지 검증·변경 관리 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 검증 쪽 5건, 변경 쪽 5건, 국내 1건이며 로봇 능력 온톨로지를 직접 다루는 것은 OntoBOT 과 RoSO/SMGI 뿐이다. [사실][^ref-890][^ref-891][^ref-889][^ref-888][^ref-892][^ref-893][^ref-895][^ref-900][^ref-896][^ref-897][^ref-899]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 검증 쪽 5건, 변경 쪽 5건, 국내 1건이며 로봇 능력 온톨로지를 직접 다루는 것은 OntoBOT 과 RoSO/SMGI 뿐이다. [사실][^ref-890][^ref-891][^ref-889][^ref-888][^ref-892][^ref-893][^ref-895][^ref-900][^ref-896][^ref-897][^ref-899]

- Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis(2018) — 역량 질문 234개와 SPARQL-OWL 번역, 106개 패턴과 46개 질의 서명의 대응을 공개한 데이터셋으로, 능력 온톨로지의 역량 질문을 테스트로 바꾸는 출발점이다. [사실][^ref-890]
- Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S., An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics(2025) — 역량 질문으로 평가하고 네 로봇에 대해 검증한 가정용 서비스 로봇 온톨로지 OntoBOT. [사실][^ref-891]
- Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C., OOPS!: an on-line tool for ontology evaluation(2014) — 피트폴 카탈로그와 중요도 분류를 갖춘 온라인 평가 도구. [사실][^ref-889]
- Zablith, F. 외, Ontology evolution: a process-centric survey(2013) — 온톨로지 진화를 유지 활동으로 정의하고 다단계 과정으로 정리한 서베이. 단계 이름은 초록에서 확인하지 못했다. [사실][^ref-888]
- Hegde, H. 외, A Change Language for Ontologies and Knowledge Graphs(2024) — 변경 요청·기술을 위한 표준 데이터 모델 KGCL 과 GitHub·BioPortal 구현. [사실][^ref-892]
- Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning(2024, 2026 개정) — 온톨로지 매칭을 버전 비교에 재사용하는 프레임워크와 교차 참조 메커니즘. [사실][^ref-893]
- Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications(2024) — 2024년 2월 기준 발표 84개·공개 18개 IDTA 명세를 메타모델로 변환해 코드·테스트를 생성했으나 문법적 변동으로 수동 개입이 필요했다는 보고. [사실][^ref-895]
- Osmani, A., From Ontology Conformance to Admissible Reconfiguration(2026) — 로봇 서비스 온톨로지의 정체성 보존 재구성 기준과 지역·전역 허용성 조건을 제시한 단독 저자의 이론적 프리프린트로, 실험·현장 적용은 없다. [사실][^ref-900]
- Nasir, F. 외, OntoKG-EQ(2026) — 다섯 개 고정 역량 질문이 온톨로지를 통제하고 각 답에 출처까지의 증거 추적을 붙이는 지식 그래프. 금융 도메인의 선례다. [사실][^ref-896]
- Abolhasani, M. S., Ba, Y., He, Y., & Pan, R., TRACE-KG(2026) — 원문 근거에 대한 완전한 추적 가능성을 유지하며 지식 그래프와 유도 스키마를 함께 만드는 프레임워크. [사실][^ref-897]
- 고영만·송민선·이승준·김비연·민혜령, 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구(2015) — Pellet 추론기 TBox 검증과 SPARQL 시나리오 평가를 수행한 국내 연구. 로봇 온톨로지는 아니지만 검증 절차의 국내 선례다. [사실][^ref-899]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-888]: Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review), Ontology evolution: a process-centric survey, 2013-08-28, https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article, 접근일 2026-09-29
[^ref-889]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-891]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-893]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-895]: Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?, 2024-06-20, https://arxiv.org/abs/2406.14470, 접근일 2026-09-29
[^ref-896]: Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying, 2026-09-08, https://arxiv.org/abs/2609.08869, 접근일 2026-09-29
[^ref-897]: Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation, 2026-04-03, https://arxiv.org/abs/2604.03496, 접근일 2026-09-29
[^ref-899]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29
[^ref-900]: Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance, 2026-05-05, https://arxiv.org/abs/2605.08185, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s4.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-886, ref-459, ref-888, ref-889, ref-890, ref-892]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#4
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어

# 7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 검증 쪽(역량 질문·피트폴·형상 검증)과 변경 쪽(버전 IRI·온톨로지 진화·변경 언어)으로 나뉜다. [사실][^ref-890][^ref-889][^ref-459][^ref-886][^ref-888][^ref-892]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 검증 쪽(역량 질문·피트폴·형상 검증)과 변경 쪽(버전 IRI·온톨로지 진화·변경 언어)으로 나뉜다. [사실][^ref-890][^ref-889][^ref-459][^ref-886][^ref-888][^ref-892]

- **역량 질문(Competency Question, CQ)** — 온톨로지가 답할 수 있어야 하는 질문으로 요구사항을 적은 것이다. Wiśniewski 외(2018)는 여러 도메인 온톨로지에 대한 역량 질문 234개와 그 SPARQL-OWL 번역을 공개하고 106개의 역량 질문 패턴을 46개의 SPARQL-OWL 질의 서명과 대응시켜, 역량 질문의 형식화·실행·관리를 지원하는 벤치마크로 제시했다. [사실][^ref-890]
- **온톨로지 피트폴(Ontology Pitfall)** — 온톨로지 모델링에서 흔히 생기는 결함 유형이다. OOPS!(OntOlogy Pitfall Scanner!)는 693개 이상의 온톨로지를 경험적으로 분석해 만든 카탈로그를 구조·기능·사용성 프로파일링 차원으로 분류하고 피트폴마다 심각·중요·경미의 중요도를 둔다. [사실][^ref-889]
- **[형상 제약 언어(SHACL)](../../glossary/shacl.md) 검증 보고서** — W3C 형상 제약 언어(Shapes Constraint Language, SHACL) 권고안(2017-07-20)은 데이터 그래프를 형상 그래프의 조건 집합으로 검증하는 언어이며, 검증 보고서는 적합 여부(sh:conforms), 개별 결과(sh:result), 심각도(sh:resultSeverity: Violation·Warning·Info)와 초점 노드·경로·값·원인 형상을 담는다. [사실][^ref-459]
- **온톨로지 IRI 와 버전 IRI(Version IRI)** — W3C OWL(Web Ontology Language) 2 구조 명세 2판(2012-12-11)은 온톨로지를 온톨로지 IRI(Internationalized Resource Identifier)로 식별하고 특정 판을 버전 IRI 로 구분하며, 같은 온톨로지 시리즈에서 정확히 하나의 버전만 현재 버전으로 본다. 판 사이 관계는 owl:priorVersion(이전 판)·owl:backwardCompatibleWith(호환되는 이전 판)·owl:incompatibleWith(양립 불가능한 이전 판) 주석으로 표기한다. [사실][^ref-886]
- **온톨로지 진화(Ontology Evolution)** — Zablith 외(2013)의 서베이는 도메인 변화나 정보 시스템 요구에 대응해 온톨로지를 최신으로 유지하는 일로 정의하고, 전형적 접근이 자연어 처리·추론 등 여러 분야 기법을 결합한 다단계 과정으로 설계된다고 정리했다. [사실][^ref-888]
- **지식 그래프 변경 언어(KGCL)** — Hegde 외의 KGCL(Knowledge Graph Change Language)은 온톨로지·지식 그래프의 변경을 '동의어 추가'·'계층 재배치' 같은 통제 자연어 명령으로 요청하거나 기술하는 표준 데이터 모델로, 패치·diff 개념을 빌려 미래 변경 요청과 기존 변경 기술에 모두 쓰인다. [사실][^ref-892]

용어집에 이미 있는 [의미적 버전 관리](../../glossary/semantic-versioning.md), [회귀 시험](../../glossary/regression-testing.md), [모델 검사](../../glossary/model-checking.md), [온톨로지 채우기](../../glossary/ontology-population.md)도 이 영역과 이어진다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-888]: Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review), Ontology evolution: a process-centric survey, 2013-08-28, https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article, 접근일 2026-09-29
[^ref-889]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s11.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 열린 질문"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-465, ref-886, ref-892, ref-893, ref-439, ref-896, ref-897, ref-899]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#11
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 열린 질문

# 7. 온톨로지 검증·변경 관리 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기존 질문 oq-147 은 원문 근거 추적과 사람 최종 검토 구성만 확인되어 조사 중으로 남고, 개정 감지·재검증 절차, 지원 단계 표시 체계, 국내 사례, IDTA 폐기 판 이관 기준의 새 질문 4건을 올린다. [추정][^ref-896][^ref-897][^ref-465]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기존 질문 oq-147 은 원문 근거 추적과 사람 최종 검토 구성만 확인되어 조사 중으로 남고, 개정 감지·재검증 절차, 지원 단계 표시 체계, 국내 사례, IDTA 폐기 판 이관 기준의 새 질문 4건을 올린다. [추정][^ref-896][^ref-897][^ref-465]

- **oq-147** (상태: 조사 중 · 제기 2026-09-29 · 실행 2026-09-29-09) 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? 부분 진전: 원문 근거 추적(OntoKG-EQ·TRACE-KG)과 사람 최종 검토(Vieira da Silva 외) 구성은 확인됐으나 로봇 매뉴얼의 절·줄 근거를 붙인 구현은 미확인이다. [추정][^ref-896][^ref-897][^ref-465]
- (신규, 이번 실행 제안) 로봇 능력 온톨로지에 대해 펌웨어·매뉴얼 개정을 감지해 영향받는 작업·현장을 찾고 재검증 대기열에 넣는 절차를 구현한 공개 구현이나 현장 사례가 있는가? 관련 영역: 7. 온톨로지 검증·변경 관리, 57. 자산·소프트웨어 수명주기 관리, 4. 이기종 로봇 등록. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]
- (신규, 이번 실행 제안) 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? 관련 영역: 7. 온톨로지 검증·변경 관리, 54. 시험·형식 검증·벤치마크, 36. 가상 시운전·실제 상황 재현.
- (신규, 이번 실행 제안) 국내에서 역량 질문·추론기·SHACL 로 로봇 온톨로지를 검증하거나 버전을 관리한 연구·현장 사례가 있는가? 이번 조사에서 확인된 국내 자료는 학술용어사전 온톨로지 검증 연구 1건이다. [사실][^ref-899] 관련 영역: 7. 온톨로지 검증·변경 관리, 5. 로봇 능력·작업 표현.
- (신규, 이번 실행 제안) IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? [사실][^ref-439] 관련 영역: 7. 온톨로지 검증·변경 관리, 21. 상호운용 표준·적합성, 4. 이기종 로봇 등록.

전체 목록은 [열린 질문](../../open-questions.md)에 있다. 제조 공장 사례 후보(SHACL 로 제조 스킬을 검증한 연구)는 서지를 확인하지 못해 이 페이지에 싣지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-893]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-896]: Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying, 2026-09-08, https://arxiv.org/abs/2609.08869, 접근일 2026-09-29
[^ref-897]: Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation, 2026-04-03, https://arxiv.org/abs/2604.03496, 접근일 2026-09-29
[^ref-899]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s7.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-886, ref-459, ref-889, ref-892, ref-439]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#7
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 관련 표준·프레임워크·오픈소스

# 7. 온톨로지 검증·변경 관리 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 판 식별은 OWL 2, 인스턴스 제약 검증은 SHACL 권고안(2017-07-20), 결함 탐지는 OOPS!, 템플릿 폐기 규칙은 IDTA 저장소, 변경 기술은 KGCL, 로봇 펌웨어·소프트웨어 판 보고는 VDA 5050 팩트시트가 맡는다. [사실][^ref-886][^ref-459][^ref-889][^ref-439][^ref-892][^ref-228]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

판 식별은 OWL 2, 인스턴스 제약 검증은 SHACL 권고안(2017-07-20), 결함 탐지는 OOPS!, 템플릿 폐기 규칙은 IDTA 저장소, 변경 기술은 KGCL, 로봇 펌웨어·소프트웨어 판 보고는 VDA 5050 팩트시트가 맡는다. [사실][^ref-886][^ref-459][^ref-889][^ref-439][^ref-892][^ref-228]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| OWL 2 구조 명세 2판(2012-12-11) | 표준 | 온톨로지 IRI·버전 IRI 로 판을 식별하고 owl:priorVersion·backwardCompatibleWith·incompatibleWith 로 이전 판 관계를 표기한다 | [사실][^ref-886] |
| W3C SHACL 권고안(기준 판 2017-07-20) | 표준 | 데이터 그래프를 형상으로 검증하고 sh:conforms·sh:result·sh:resultSeverity 를 담은 검증 보고서를 낸다 | [사실][^ref-459] |
| OOPS!(OntOlogy Pitfall Scanner!) | 프레임워크 | 693개 이상 온톨로지 분석에 기반한 피트폴 카탈로그로 모델링 결함을 온라인 탐지하고 중요도를 매긴다 | [사실][^ref-889] |
| IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) | 표준 | published·deprecated 폴더, 주버전·리비전·버그 수정 표기, 새 판 6개월 뒤 이전 판 폐기 규칙을 정한다 | [사실][^ref-439] |
| KGCL(지식 그래프 변경 언어) | 프레임워크 | 온톨로지 변경을 통제 자연어 명령·패치·diff 로 요청·기술하는 표준 데이터 모델 | [사실][^ref-892] |
| [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md) JSON 스키마(main, 3.0.0 판) | 표준 | VDA 5050 프로토콜 판([Major].[Minor].[Patch])을 뜻하는 version 을 필수 속성으로 두고 선택 속성 mobileRobotConfiguration 에 하드웨어·소프트웨어 버전을 담아, 로봇 펌웨어·소프트웨어 판이 바뀐 사실을 등록 데이터에서 읽을 수 있는 자리를 제공한다 | [사실][^ref-228] |

전체 표준 목록은 [표준·프레임워크](../../standards/index.md)에 있다. SHACL 은 W3C 권고안 2017-07-20 판을 기준으로 적었다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-889]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s3.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 왜 중요한가"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-886, ref-890, ref-891, ref-892, ref-893, ref-439, ref-895, ref-899]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#3
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 왜 중요한가

# 7. 온톨로지 검증·변경 관리 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 온톨로지를 검증하는 수단과 판을 표기하는 규칙은 여러 발행 주체에서 확인되지만, 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없어 ROP 가 판 식별·변경 표현·펌웨어 판 보고를 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

온톨로지를 검증하는 수단과 판을 표기하는 규칙은 여러 발행 주체에서 확인되지만, 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없어 ROP 가 판 식별·변경 표현·펌웨어 판 보고를 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다. [추정][^ref-886][^ref-439][^ref-892][^ref-893][^ref-228]

2. 핵심 질문의 앞부분, 곧 온톨로지가 빠짐없고 정확한지는 검증의 문제다. 서로 다른 세 연구(Wiśniewski 외의 역량 질문 데이터셋, Martorana 외의 OntoBOT, 고영만 외의 STNet)가 역량 질문(competency question, CQ) 또는 SPARQL(SPARQL Protocol and RDF Query Language) 질의 실행과 추론기 검증으로 온톨로지의 완전성·정확성을 확인하는 방식을 각각 보고했으므로, 이 검증 방식은 한 곳 이상에서 확인된다. [사실][^ref-890][^ref-891][^ref-899] [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md)이 만든 어휘는 이 검증을 거쳐야 [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md)이 믿고 쓸 수 있다.

질문의 뒷부분, 곧 문서가 바뀌면 무엇을 다시 확인할지는 변경 관리의 문제다. Eichelberger·Weber(2024)는 2024년 2월 기준 IDTA(Industrial Digital Twin Association, 산업 디지털 트윈 협회)가 발표한 84개·공개한 18개 명세 가운데 18개를 중간 메타모델로 변환해 5만 줄 이상의 API 코드·테스트를 자동 생성했으나 명세의 문법적 변동과 문제 때문에 수동 개입이 필요했다고 보고해, 표준 명세 자체의 변동성이 이를 소비하는 시스템의 재검증 부담이 됨을 보였다. [사실][^ref-895] 로봇 온톨로지가 기대는 표준·매뉴얼·펌웨어가 모두 바뀌는 대상이므로, 무엇이 바뀌었고 어디에 영향을 주는지를 추적하지 못하면 검증 결과가 곧 낡는다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-891]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-892]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-893]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-895]: Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?, 2024-06-20, https://arxiv.org/abs/2406.14470, 접근일 2026-09-29
[^ref-899]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-09/pages/topics/2026/2026-09-29-area07-s10.md

```markdown
---
title: "7. 온톨로지 검증·변경 관리 — 다른 연구영역과의 연결"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-465, ref-880, ref-886, ref-459, ref-890, ref-891, ref-439, ref-895, ref-898]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/ontology-verification-and-change-management.md#10
---

[홈](../../index.md) › [주제](../index.md) › 7. 온톨로지 검증·변경 관리 — 다른 연구영역과의 연결

# 7. 온톨로지 검증·변경 관리 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 앞뒤의 온톨로지 영역, 판 규칙을 다루는 표준·수명주기 영역, 테스트 방법을 다루는 검증 영역, 언어 모델 방법을 다루는 AI 영역과 이어진다. [추정][^ref-439][^ref-459][^ref-465][^ref-898]
- 이 페이지는 [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 앞뒤의 온톨로지 영역, 판 규칙을 다루는 표준·수명주기 영역, 테스트 방법을 다루는 검증 영역, 언어 모델 방법을 다루는 AI 영역과 이어진다. [추정][^ref-439][^ref-459][^ref-465][^ref-898]

- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 등록 때의 검토·승인 기록과 언어 모델 생성 뒤 사람 최종 검토가 이 영역의 검증 기록과 같은 기록을 공유한다. [추정][^ref-465]
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 검증 대상이 되는 능력·작업 어휘를 준다.
- [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) — 검증된 연결만 실행하며, HERON 의 SHACL 정책 검증이 같은 출처로 실려 있다. [사실][^ref-880]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — IDTA 템플릿의 판·폐기 규칙과 명세 변동이 적합성 확인에 이어진다. [사실][^ref-439][^ref-895]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) · [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 언어 모델로 역량 질문·온톨로지를 생성·검증하는 방법은 교차 규칙에 따라 두 영역에도 연결한다. [사실][^ref-465][^ref-898]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 역량 질문의 테스트화와 SHACL 검증 보고서는 테스트·형식 검증 방법과 겹친다. [사실][^ref-890][^ref-459]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — OWL 2 버전 IRI 와 팩트시트의 소프트웨어 판이 자산·소프트웨어 판 관리와 이어진다. [사실][^ref-886][^ref-228]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) · [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 5절의 병원·가정 사례가 속하는 현장 유형 영역이다. [사실][^ref-880][^ref-891]
- [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) 트랙 — 단계 5(완전성·정확성 검증)와 단계 6(변경 관리)이 이 영역의 자료를 참고한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/ontology-verification-and-change-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-880]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-890]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-891]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-895]: Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?, 2024-06-20, https://arxiv.org/abs/2406.14470, 접근일 2026-09-29
[^ref-898]: Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models, 2026-04-17, https://arxiv.org/abs/2604.16258, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-09 | 7. 온톨로지 검증·변경 관리 의 "다른 연구영역과의 연결" 절에서 분리 |
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
