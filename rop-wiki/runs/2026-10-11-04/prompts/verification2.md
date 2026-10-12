(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-04
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 48. 안전·위험 관리 (M. 안전)
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

### runs/2026-10-11-04/target.json

```json
{
  "run_id": "2026-10-11-04",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 170,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 48,
    "area_name": "48. 안전·위험 관리",
    "category": "M. 안전",
    "category_letter": "M"
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
  "selection_rationale": "CLI 지정 run_type=update, area=48"
}
```

### runs/2026-10-11-04/research.json

```json
{
  "run_id": "2026-10-11-04",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 48,
    "area_name": "48. 안전·위험 관리",
    "category": "M. 안전"
  },
  "gaps": [
    "섹션 3. 왜 중요한가(분리 2026-09-25-area25-s3) — 국내 위험성평가 실시 주체(도급·수급)·근로자 참여·수시평가 조건 근거 없음",
    "섹션 5. 적용 사례 — '출하 마감 전 화재경보' 제약 칸(107행)의 'RMF 비상 신호는 플릿을 구분하지 않는 불리언, 이후 구현 여부 미확인' 이 2.10.0 이후 상태와 맞지 않음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-25-area25-s6) — STPA 의 실제 분석 산출물(단계·위험한 제어 행동 유형), 근로자 참여 기록 방법, 감시와 대응의 구분이 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-25-area25-s7·2026-09-26-area25-s7) — R15.08 Part 3 '예정' 표현(2026-09-25-area25-s7.md 43행), ISO 3691-4 차기판 '제2판 초안' 표현(2026-09-26-area25-s7.md 46행), 이동식 협동로봇 KS '표준 번호 미확인'(같은 파일 46행 표)이 낡음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-25-area25-s8) — Bensaci 2020 Bowtie 결합 연구 없음, Belzile 사례 조건(현장·로봇)과 잔류 위험 추정 방식, SafeGate 평가 층위·분모 문제 미반영",
    "섹션 9. 책임 경계 — 제조사 매뉴얼의 인터록·PL 책임 구분, EU 실질적 변경 정의의 조건 미반영",
    "섹션 11. 열린 질문 — oq-064·oq-070·oq-093·oq-095·oq-096 부분 근거 미반영",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정 3건(f7·f10·f32)"
  ],
  "research_questions": [
    "여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]",
    "oq-070 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? (섹션 7·11 겨냥)",
    "oq-064 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? (섹션 7·11 겨냥)",
    "oq-096 여러 제조사 로봇이 섞인 현장에서 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (섹션 3·9·11 겨냥, 국내 고시 우선)",
    "oq-095 ROP 의 원격·플릿 일괄 정지 지시 경로가 성능 수준(PL) 요구를 받는가? (섹션 9·11 겨냥)",
    "oq-093 EU 기계 규정의 실질적 변경 판단이 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (섹션 9·11 겨냥)",
    "바뀐 출처: R15.08 Part 3 발행, ISO 3691-4·ISO 12100 개정 단계, KS B ISO 3691-4 개정, Open-RMF 비상 신호 구현 상태는 무엇인가? (섹션 5·7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "STPA Handbook 은 STPA 분석을 분석 목적 정의, 제어 구조 모델링, 위험한 제어 행동(Unsafe Control Action) 식별, 손실 시나리오 식별의 네 단계로 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 14쪽, Chapter 2 Method Overview: \"Defining the purpose of the analysis … Modeling the control structure … Identifying unsafe control actions … Identifying loss scenarios\". 방법론 안내서이며 항공기 예시가 중심이라 로봇 플릿 실증 결과가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "STPA Handbook 은 위험한 제어 행동을 제어 행동을 제공하지 않음, 위험하게 제공함, 너무 이르거나 늦게·순서가 틀리게 제공함, 지속 제어를 너무 오래 끌거나 너무 일찍 멈춤의 네 유형으로 나눠 찾게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 36쪽, Table 2.3 아래 네 유형: not providing … causes hazard / providing … causes hazard / \"too early, too late, or in the wrong order\" / \"stopped too soon or applied too long\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Bensaci 외(2020, Alexandria Engineering Journal)는 초록 기준으로 다중 로봇 시스템에 STPA 와 Bowtie 를 결합해, 서로 다른 계층형 조정 구조의 위험 시나리오와 요인을 STPA 로 도출한 뒤 Bowtie 로 평가하고 위험을 분류해 제어 구조 비교에 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1521"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"a risk identification study is done using STPA to extract a set of risk scenarios related to different types of hierarchical coordination architectures … an evaluation of the obtained scenarios is performed by the Bowtie method … provides a classification of risks\". 서지 59(5) pp.3799–3816, 2020-10, 온라인 2020-07-07, 저자 6명(Crossref). 본문 미열람이라 메모의 'semi quantitative'·'modified hierarchical'(수정 계층형) 표현은 확인하지 못함",
      "as_of": "2020-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Bensaci 외(2020)의 분석 대상은 기존 2018년 연구(ref-564)와 같이 화학 분석실에서 화학제품을 운반하는 다중 로봇(메모 기준 11대) 시스템인 것으로 보이나, 본문을 열지 못해 로봇 대수와 사례 조건은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1521"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모는 본문 §3(7쪽) \"eleven robots\" 를 인용했으나 이번 대조에서는 본문 미접근, 초록에 대수·현장 언급 없음. 메모 F05(일부 시나리오·원인 요인을 합쳐 평가했다는 한계)도 같은 이유로 확인 못 해 finding 에서 뺌",
      "as_of": "2020-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Belzile 외의 사례 연구는 캐나다 몬트리올의 건설사 Pomerleau 건설 현장에 Clearpath Jackal 을 배치하려는(intended deployment) 상황을 대상으로 위험성평가를 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-563"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 5쪽 §4 Case Study: Pomerleau·Montreal·Clearpath Jackal \"intended deployment\". arXiv v1 2025-02-28. 단일 로봇 현장 맥락",
      "as_of": "2025-02-28",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "Belzile 외의 잔류 위험지수는 실험으로 측정한 값이 아니라 제안한 완화 대책을 적용한다고 보고 다시 추정한 값이다.",
      "tag": "사실",
      "source_ids": [
        "ref-563"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 7쪽 §4.3, Table 3 앞 문단: \"a new risk index was estimated\" (제안 완화 대책 기준). 완화 효과를 현장 시험으로 검증했다는 서술은 없음",
      "as_of": "2025-02-28",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f7",
      "claim": "정정: 분리 페이지 2026-09-25-area25-s7.md 43행의 'R15.08-2 … 사용자 요구는 예정된 Part 3 이 맡는다' 는 표현은 낡았다. A3 판매 페이지는 ANSI/A3 R15.08-3-2026(Part 3: Use of IMR Applications)의 발행일을 2026-04-23 으로 표시하며, 이 내용은 위키에 이미 있다(ref-1255, safety/index.md 53행).",
      "tag": "추정",
      "source_ids": [
        "ref-1255"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기존 내용 확인: ref-1255(2026-10-09 원문 열람, \"Published April 23, 2026\", 77쪽), docs/categories/safety/index.md 53행. 이번 재열람은 A3 403. 새 사실 추가가 아니라 48영역 s7 문장의 '예정' 표현 정정만 제안. 사용자 의무 세부(oq-265)는 이번 메모가 답하지 않음",
      "as_of": "2026-04-23",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "메모에 따르면 ISO 3691-4 차기판 프로젝트는 ISO/DIS 3691-4(Edition 3)로 2026-09-10 단계 40.60(DIS 투표 종료)에 있으나, 이번 대조에서 iso.org 가 403 이라 확인하지 못했고 위키 ref-789 는 같은 URL 을 2026-09-26 'ISO/CD 3691-4' 로 기록해 서로 충돌한다.",
      "tag": "추정",
      "source_ids": [
        "ref-789"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 n5: 'Edition 3', '40.60 2026-09-10 Close of voting'. 위키 ref-789 제목 'ISO/CD 3691-4'(2026-09-26 기록). 원문 미확인이라 단계·날짜를 사실로 쓰지 않고 제목 갱신(CD→DIS)도 보류. 단계 40.60 은 발행·FDIS 완료가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "메모에 따르면 ISO 12100 개정 프로젝트(ISO/DIS 12100.3)는 2026-09-15 단계 40.60 에 있으나, iso.org 403 으로 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 n6: '40.60 2026-09-15 Close of voting', 2026-06-29 새 DIS 투표 결정·2026-07-20 투표 시작. 모두 미확인. 기존 위키(2026-09-26-area25-s7.md 47·48행)의 'ISO/DIS 12100:2024 기반 DIN 초안'·'2026 FDIS 도달 전망' 문장은 그대로 두고 단계 갱신은 확인 뒤로 미룸",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "정정 제안: 2026-09-26-area25-s7.md 46행은 ISO 3691-4 차기판을 '제2판 초안' 이라 적었으나, ISO 3691-4 는 2020 판이 제1판, 2023 판이 제2판이므로 차기판은 제3판이라고 쓰는 것이 정합적으로 보인다(차기판의 개발 단계와 날짜는 미확인).",
      "tag": "추정",
      "source_ids": [
        "ref-470",
        "ref-789"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ref-470(ISO 3691-4:2023, 현행) 과 메모 n5 의 'Edition 3' 표기가 일치. ISO 목록 원문은 이번에 열지 못해(403) 판 번호를 추정으로 둠. 단계는 ref-789 기록(CD)과 메모(DIS 40.60)가 충돌하므로 '위원회 검토 단계' 표현도 함께 재확인 필요",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "국가표준 목록에서 KS B 7327 의 표제는 '산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항'이고, 발행일 2024-11-01, 국가기술표준원 고시 제2024-0480호로 제정됐으며 61쪽이다. 고시 사유는 모바일 로봇과 협동로봇이 결합된 로봇에 적용할 표준·인증이 없다는 것이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1523"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세: \"KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항 … 발행일 : 2024-11-01\", \"국가기술표준원 (제2024-0480호)\", 고시사유 \"모바일 로봇과 협동로봇이결합된 형태의 로봇으로 현재 적용할 수 있는 로봇 표준 및 인증이 없으므로 본 표준 제정이 필요함\". 목록만 열람, 본문 미열람",
      "as_of": "2024-11-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "KS B 7327 목록의 적용범위는 통합 제조 시스템(IMS), 관제 시스템, 군집 관리 시스템, 기타 기계 설비류를 이 표준에서 다루지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1523"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 적용범위: \"통합 제조 시스템(IMS), 관제 시스템, 군집 관리 시스템, 기타 기계 설비류는 이 표준에서 다루지 않는다.\" 목록 기준",
      "as_of": "2024-11-01",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "KS B 7327 목록은 국제표준 부합화 칸이 비어 있고, 인용표준으로 KS B ISO 10218-1·KS B ISO 10218-2·KS B ISO 3691-4·KS B ISO 12100·KS B ISO 13849-1 을 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1523"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세의 '국제표준 부합화' 칸 공란, '인용표준' 표(목록 기준). 조항별 국제 대응표나 R15.08-2 와의 대응은 목록에 없음",
      "as_of": "2024-11-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "중소벤처기업부가 2024-11-03 발표한 '이동식 협동로봇 안전기준 KS'(2024-11-01 부터 활용)는 발행일과 고시 사유가 일치하는 KS B 7327 인 것으로 보인다(oq-070 의 표준 번호 부분 답변).",
      "tag": "추정",
      "source_ids": [
        "ref-1523",
        "ref-561"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ref-561 은 2024-11-01 활용·이동 중 작업 기준 부재를 설명하고, ref-1523 은 같은 날 발행·모바일 로봇+협동로봇 결합형 표준 부재를 고시 사유로 적음. 발표문에 번호가 없어 동일성은 추정. ISO 10218-2:2025·ISO 3691-4:2023 과의 조항 대응은 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "KS B 7327 은 이동 머니퓰레이터 응용의 안전 요구를 다루므로 R15.08-2 유형 C(모바일 매니퓰레이터) 통합 요구에 대응하는 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성이나 플릿 통합 전체를 포괄하는지는 확인되지 않는다(oq-064 부분 답변).",
      "tag": "추정",
      "source_ids": [
        "ref-1523"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f11~f13 에서 도출. R15.08-2 원문과 KS B 7327 본문을 모두 열지 않아 대응 관계는 미확인. 인증 기준 대응도 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "국가표준 목록에서 KS B ISO 3691-4 는 2026-09-14 개정(국가기술표준원 고시 제2026-0288호)됐고, 국제표준 부합화를 ISO 3691-4:2023(IDT)로 표시하며 81쪽이다. 구판은 2021-11-30 판이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1524"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세: 2026-09-14, 고시 제2026-0288호, \"ISO 3691-4:2023(IDT)\", 81쪽, 이전 판 2021-11-30. 국내 IDT 판(2023 판 부합)과 ISO 에서 개발 중인 차기판(f8)은 구별",
      "as_of": "2026-09-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "현행 「사업장 위험성평가에 관한 지침」(고용노동부고시 제2024-76호, 2024-12-18 일부개정, 2025-01-02 시행) 제5조제2항은 작업의 일부 또는 전부를 도급하는 사업에서 도급사업주와 수급사업주가 각각 위험성평가를 실시하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1525"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제5조(위험성평가 실시주체) ②: \"도급사업주 … 와 … 수급사업주 … 는 각각 제1항에 따른 위험성평가를 실시하여야 한다.\" 시행 2025-01-02 [고용노동부고시 제2024-76호, 2024-12-18, 일부개정]",
      "as_of": "2025-01-02",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "같은 지침 제6조는 위험성 수준 판단 기준 마련, 유해·위험요인 파악, 허용 가능 여부 결정, 감소대책 수립·실행, 감소대책 실행 여부 확인의 다섯 경우에 해당 작업에 종사하는 근로자를 참여시키도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1525"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제6조(근로자 참여) 1~5호, \"해당 작업에 종사하는 근로자를 참여시켜야 한다.\"",
      "as_of": "2025-01-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "같은 지침 제15조제2항은 건설물 설치·변경, 기계·기구·설비의 신규 도입 또는 변경, 정비·보수, 작업방법·절차의 신규 도입 또는 변경, 중대산업사고·산업재해 발생, 그 밖에 사업주가 필요하다고 판단한 경우로 추가적인 유해·위험요인이 생기면 수시 위험성평가를 하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1525"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제15조② 본문 \"추가적인 유해ㆍ위험요인이 생기는 경우에는 … 수시 위험성평가를 실시하여야 한다\" 와 1~6호(3호 정비·보수, 5호 재해 발생 시 작업 재개 전 실시, 6호 사업주 판단). 소프트웨어 버전 변경이 자동으로 수시평가 대상이라는 문구는 없음",
      "as_of": "2025-01-02",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f20",
      "claim": "같은 지침 제15조제4항은 사업주가 매월 1회 이상 근로자 제안제도 활용·아차사고 확인·사업장 순회점검 등으로 유해·위험요인을 발굴해 위험성 결정과 감소대책을 수립·실행하는 등 상시적 위험성평가를 이행하면 제2항·제3항의 수시평가와 정기평가를 실시한 것으로 본다(간주 규정).",
      "tag": "사실",
      "source_ids": [
        "ref-1525"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제15조④: \"… 다음 각 호의 사항을 이행하는 경우 제2항과 제3항의 수시평가와 정기평가를 실시한 것으로 본다. 1. 매월 1회 이상 근로자 제안제도 활용, 아차사고 확인, … 사업장 순회점검 등 …\". 메모의 '상시평가 인정 경로'를 원문대로 '수시·정기평가 실시 간주 규정'으로 바꿈",
      "as_of": "2025-01-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "고용노동부의 「위험성평가 근로자 참여 가이드」(2024-12)는 수급업체 근로자를 대상으로 청취조사를 해 아차사고 경험과 개선 의견을 모으는 방법을 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1527"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 9쪽(인쇄 6쪽) 핵심 포인트: 청취조사로 \"아차사고 사례\"·개선 의견 수집. 참여 방법 사례이며 사고 감소 효과를 검증한 자료가 아님. 고시(ref-1525)와 같은 고용노동부 계열이라 독립 출처가 아님",
      "as_of": "2024-12-31",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "같은 가이드는 일용근로자 사례로 문자와 QR코드를 활용해 익명으로 위험 요인을 제안받는 방식을 소개한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1527"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 10쪽(인쇄 7쪽) 일용근로자 사례 1: \"문자·QR코드를 활용하여 익명으로\" 제안. 메모의 '사례' 를 '일용근로자 사례' 로 명시",
      "as_of": "2024-12-31",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "고용노동부(산재예방지원과)는 2026-09-23 「사업장 위험성평가에 관한 지침」 전부개정고시(안)을 행정예고했다. 이는 예고안이며 최종 고시·시행이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1526"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고용노동부 입법·행정예고 게시: 제목 '사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고', 2026.09.23, 담당 산재예방지원과. 개정안 세부 요구는 시행 규정으로 인용하지 않음",
      "as_of": "2026-09-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "메모에 따르면 이 행정예고는 고용노동부 공고 제2026-461호이고 의견 제출 마감은 2026-10-13 이나, 이번 대조에서 공고 번호와 마감일은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1526"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 n10·F21 의 '공고2026-461', '13일까지'(공고 HWPX 첨부 기준)는 대조 범위 밖이라 미확인. 최종 발령·시행일은 후속 확인 필요(메모 U13)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "Monitoring ROS2 논문(Perez 외, EPTCS 371)은 관련 연구 절에서 DeRoS 와 비교하며, DeRoS 는 속성 위반을 어떻게 처리할지 지정하게 하지만 자기들의 방식은 위반의 탐지와 보고로 한정된다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1530"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3 Related work 안 DeRoS 비교 문장(PDF 7쪽, 인쇄 214쪽): \"DeRoS also allows users to specify how property violations must be handled, while our approach is limited to detecting and reporting violations.\" 서지 EPTCS 371 pp.208–216, DOI 10.4204/EPTCS.371.15",
      "as_of": "2022-09-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "OMRON LD Safety Guide(Rev H)는 플릿 안의 로봇들이 위치·크기·경로 계획 정보를 주고받아 장애물 회피에 쓰는 것을 충돌을 막는 인터록 방식으로 보지 않으며, 필요한 인터록은 사용자·통합자가 따로 갖춰야 한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: PDF 17쪽 Fleet 경고 \"This is not an interlocked method of preventing collisions\". 단일 벤더·특정 제품(2019-10 Rev H) 매뉴얼이라 타사 플릿이나 현행 모든 OMRON 모델로 일반화하지 않음",
      "as_of": "2019-10",
      "site_type": null,
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f27",
      "claim": "같은 매뉴얼은 외부 비상정지 회로에 사용자가 공급한 부품이 포함될 때 그 부품을 포함한 전체 PL·PFH 계산과 최종 위험성평가를 사용자 책임으로 둔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: PDF 18쪽 PL and PFH 표 주석 \"… PFH, inclusive of user-supplied components, and performing a final risk assessment.\" 제품 매뉴얼 기준이며 법적 의무 판단이 아님",
      "as_of": "2019-10",
      "site_type": null,
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f28",
      "claim": "Open-RMF issue #658(2025-04-04) 작성자는 두 건물에 로봇을 배치한 상황에서 한 건물의 화재경보가 모든 로봇을 주차시킨다는 문제를 보고한 것으로 보이나, 이번 재열람이 GitHub 403 으로 실패해 '두 건물' 같은 세부는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-567"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 F30 인용 \"ALL robots will go into parking\". 이슈의 핵심(화재경보 시 대상 플릿 구분 없는 주차)은 기존 위키 내용(safety-and-risk-management.md 106·107행, ref-567)과 일치. 세부 상황은 미확인",
      "as_of": "2025-04-04",
      "site_type": "기타",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "rmf_fleet_adapter 변경 이력(2.14.0 태그)은 2.10.0(2025-05-09) 절에 '플릿 이름으로 화재경보를 분리하는 선택지'를 추가한 #413 을 싣는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHANGELOG.rst 2.10.0 (2025-05-09): \"Giving options to separate fire alarm by fleet names (#413)\". 2.10.0 이 기능 최초 도입판인지는 변경 이력 기준이며 배포 시험은 아님",
      "as_of": "2025-05-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "rmf_ros2 2.14.0 의 플릿 어댑터는 대상 비상 신호(EmergencySignal)의 fleet_names 가 비어 있거나 자기 플릿 이름을 포함할 때만 handle_emergency 에 is_emergency 값을 넘긴다. 즉 빈 목록은 모든 플릿에 적용된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1529"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FleetUpdateHandle.cpp 1444~1465행 handle_target_emergency: \"if (emergency_signal->fleet_names.empty()) execute = true\" … \"if (fleet_name == name)\" … \"handle_emergency(emergency_signal->is_emergency)\". Node.cpp 77~79행 TargetEmergencyNotice 를 EmergencySignalTopicName 으로 구독. 코드 열람이며 배치 시험·대피 안전성 검증이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "같은 2.14.0 코드에는 플릿을 가리지 않는 기존 불리언 비상 알림(EmergencyNotice) 구독 경로도 함께 남아 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1529"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Node.cpp 73~75행: \"_emergency_notice_obs = create_observable<EmergencyNotice>(rmf_traffic_ros2::EmergencyTopicName, transient_qos)\" 와 77~79행 대상 비상 신호 구독이 공존",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "정정 제안: 48영역 페이지 5절 '출하 마감 전 화재경보' 표의 제약 칸(107행) '비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었고, 이후 구현 여부는 미확인' 은, 2.10.0(2025-05-09)부터 플릿 이름으로 대상을 고르는 비상 신호가 추가됐고 2.14.0 에는 기존 불리언 경로와 대상 지정 경로가 함께 있다는 내용으로 고치는 것이 맞아 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1398",
        "ref-1529",
        "ref-567"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f29~f31 에서 도출. 같은 주장이 docs/categories/safety/index.md 95행과 docs/categories/governance-law-and-society/index.md 84행에도 있음(다른 페이지라 후속 정리 대상). 세 출처 모두 Open-RMF 계열이라 독립 교차 확인 아님. 건물·구역 단위 구분은 플릿 이름 매핑 설계에 달림",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f33",
      "claim": "EU 기계 규정 2023/1230 제3조(16)의 실질적 변경은, 제조자가 예견·계획하지 않은 물리적·디지털 변경이 새 위험요인을 만들거나 기존 위험을 키워 안전에 영향을 주고, 그 결과 (a) 기존 안전 제어 시스템의 변경이 필요한 방호장치·보호장치 추가 또는 (b) 안정성·기계적 강도를 보장할 추가 보호조치 채택이 필요할 때로 한정된다.",
      "tag": "사실",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2026-07-27 통합본(02023R1230) Art.3(16): \"by physical or digital means … not foreseen or planned by the manufacturer … by creating a new hazard, or by increasing an existing risk, which requires: (a) the addition of guards or protective devices … necessitates the modification of the existing safety control system; or (b) the adoption of additional protective measures to ensure the stability or mechanical strength\". 디지털 변경 포함·일반 정의는 기존 위키 내용(2026-09-25-area24-s3.md 41행), (a)·(b) 조건이 새 내용",
      "as_of": "2026-07-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "같은 규정 제54조는 일반 적용일을 2027-01-20 으로 두되, 제26~42조는 2024-01-20, 제50조(1)은 2026-10-20, 제6조(7)·제48조·제52조는 2023-07-19, 제6조(2)~(6)·(8)·(11)·제47조·제53조(3)은 2024-07-20 부터 적용한다.",
      "tag": "사실",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통합본 Art.54: \"It shall apply from 20 January 2027. However … (a) Articles 26 to 42 from 20 January 2024; (b) Article 50(1) from 20 October 2026; (c) Article 6(7) and Articles 48 and 52 from 19 July 2023; (d) Article 6(2) to (6), (8) and (11) and Articles 47 and 53(3) from 20 July 2024\". 일반 적용일 2027-01-20 은 기존 위키 내용",
      "as_of": "2026-07-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "제3조(16)이 디지털 변경을 포함하되 새 위험·기존 위험 증가와 (a)·(b) 조치 필요성을 함께 요구하므로, ROP 정책·어댑터 업데이트가 실질적 변경인지는 업데이트마다 그 조건을 따져야 하며 '디지털 변경이므로 모두 재인증 대상' 이라고 볼 수는 없어 보인다. 특정 업데이트의 법적 분류와 누가 제조자 의무를 지는지(제18조)는 이번 자료로 판단하지 않았다(oq-093·oq-282 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f33 에서 도출. 집행 지침·사례 해석은 확인하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "SafeGate 논문의 평가는 세 층위로 나뉜다. 230개 합성 로봇 작업 벤치마크는 실행 전 단계 1~3(위험 분석·결합·결정 게이트)을 평가하고, 30개 AI2-THOR 시나리오는 시뮬레이션 실행을 평가하며, 실물 로봇 실험은 §VI-C 에서 정성 결과로만 보고하고 단계 4~6(계약 컴파일·정적 계획 검증·실행 중 감시)을 시험한다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 6쪽 §V-A \"synthetic benchmark of 230 robot tasks\"(Stage 1~3), §V 서두·§V-B \"30 AI2-THOR\", PDF 8쪽 §VI-C \"Qualitative results\". 230개·30개 수치 자체는 기존 위키 내용(2026-09-25-area25-s6.md 53행, safety/index.md 69행), 층위 구분과 실물 실험의 정성 보고가 새 내용",
      "as_of": "2026-04-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "SafeGate 논문의 충돌률(CR) 식(9)은 분모를 실행된 작업 수(T_exec)로 두는데, §VI-B 는 30개 시나리오를 모두 차단한 경우의 CR 을 0% 로 보고해, 실행 0건일 때의 산정 규칙이 논문에 명시되지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "식(9) 분모 T_exec, §VI-B \"blocking all 30 …\" 과 CR%=0 보고. 실행 0건 처리 규칙에 대한 설명 없음. 이 수치를 검증된 무사고율로 인용하지 않음",
      "as_of": "2026-04-07",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f38",
      "claim": "SafeGate 논문 표 II 의 혼동행렬 합계는 183건(TP 100, FN 0, FP 6, TN 77)으로 전체 230개 벤치마크와 47건 차이가 난다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표 II: TP100 + FN0 + FP6 + TN77 = 183. 230 과의 차이를 설명하는 문장은 확인하지 못함",
      "as_of": "2026-04-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "표 II 의 183건과 230건의 차이는 결정 게이트가 판단을 미룬(ambiguous·defer) 작업을 혼동행렬에서 뺀 결과로 보이나, 논문이 47건 제외를 명시하지 않아 확정할 수 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Stage 3 결정 게이트가 승인·거부·보류(defer)의 세 갈래를 낸다는 설명에서 추론. 저자 코드·원자료 미확인(메모 U09·U11)",
      "as_of": "2026-04-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "f1·f2 의 STPA 절차를 혼합 플릿에 쓰려면 제어 구조에 ROP·어댑터·로봇·설비·현장 운영자를 넣고, 정지 명령 누락뿐 아니라 잘못된 재개, 늦은 정지, 오래된 상태에 근거한 재배정을 위험한 제어 행동으로 등록해 손실→위험→제어 행동→안전 제약→시험으로 이어지는 연결표를 두는 방식이 필요해 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "STPA Handbook 의 네 단계·네 유형(f1·f2)을 ROP 제어 구조에 대입한 의견. 로봇 플릿 적용 실증 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "국내 지침은 도급·수급사업주가 각각 위험성평가를 하고 근로자를 참여시키게 하고(f17·f18), 제조사 매뉴얼은 시스템 통합 때 추가한 부품의 PL·PFH 계산과 최종 위험성평가를 사용자 몫으로 두므로(f27), 혼합 플릿 현장의 위험성평가는 현장 사업주(도급 구조에 따라 각각)가 주체가 되고 ROP 사업자·제조사·설비업체는 계약에 따라 자료와 분석을 제공하는 구조로 보이나, 실제 책임 배분은 현장의 법적 주체·계약에 따라 달라 확정되지 않는다(oq-096 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1525",
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f17·f18·f27 에서 도출. ROP 사업자 자체를 지칭하는 규정은 확인한 자료에 없음. R15.08-2 원문 미열람",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "VDA 5050 은 스스로 안전 표준이 아니라고 하고 activeEmergencyStop 의 REMOTE 는 비상정지 상태 보고 값일 뿐이며(기존 위키 내용), 제조사 매뉴얼은 플릿 정보 교환을 인터록으로 보지 않으므로(f26), ROP 의 원격·플릿 일괄 정지 지시 경로에 요구되는 PL 은 이들 문서로 정해지지 않고 기능별 위험성평가와 제조사 안전 인터페이스로 따로 정해야 하는 것으로 보인다(oq-095 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 3.0.0 범위 \"shall not be regarded or applied as a safety standard\", safetyState.activeEmergencyStop MANUAL/REMOTE/NONE(3.0.0 태그 본문·state.schema, 모두 기존 위키 내용: 2026-09-25-area25-s3.md 39행, safety/index.md 113행) 와 f26 에서 도출. 특정 경로의 PL 은 미결정",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "VDA 5050 의 startPause·stopPause 는 업무 일시정지·재개 명령이고 안전 기능 해제 절차가 아니므로, ROP 는 업무 pause 해제와 현장 안전정지 해제 승인을 별도 상태로 관리하고 제조사·설비의 해제 조건 충족을 확인하기 전에는 재개를 지시하지 않는 정책을 두는 것이 바람직하다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "startPause(\"other actions continue\")·stopPause(\"Deactivates the pause mode\") 정의는 기존 위키 내용(2026-09-25-area20-s4.md 42행). stopPause 가 비상정지 회로 리셋 명령이라는 근거는 없음",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "완료·인계"
    },
    {
      "id": "f44",
      "claim": "Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않고(기존 위키 내용) Ogma 생성 감시기는 위반의 탐지·보고로 한정되므로(f25), ROP 위험등록부에는 탐지 주체, 대응 결정자, 실제 정지 장치, 허용 지연, 감시 자체의 장애 시 대응을 따로 적어야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1077",
        "ref-1530"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "nav2_collision_monitor 1.5.2 README \"does not provide hard real-time safety certifications\"(기존 위키: 2026-09-30-area49-s6.md 47행·area49-s7.md 47행, ref-1077). 두 출처는 별개 구현이며 공통 제품 안전성을 교차 입증한 것이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "RMF 의 대상 비상 신호에서 빈 fleet_names 가 전체 플릿을 뜻하므로(f30), 운영 화면은 빈 목록을 '전체 플릿' 으로 명확히 표시하고, 잘못된 플릿 선택·지연·중복 신호·재개 전 승인 조건을 시험 항목으로 두는 것이 필요하다. 화재 시 로봇의 이동·정지 정책은 현장 대피 계획과 함께 정해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1529"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f30·f31 에서 도출한 운영 시사점",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f46",
      "claim": "SafeGate 처럼 실행 전 차단과 실행 결과를 함께 보고하는 평가에서는 위험 작업 차단률과 실제 실행된 작업의 안전 결과를 서로 다른 분모로 공개하고, 실행되지 않은 작업을 안전하게 실행된 작업으로 세지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f37·f38 의 분모 문제에서 도출",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1520",
      "org": "Leveson, N. G., Thomas, J. P. (MIT Partnership for Systems Approaches to Safety and Security)",
      "title": "STPA Handbook",
      "published": "2018-03",
      "url": "https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "STPA 방법 안내서. 분석 목적 정의→제어 구조 모델링→위험한 제어 행동 식별→손실 시나리오 식별의 4단계와 위험한 제어 행동 4유형을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1521",
      "org": "Bensaci, C., Zennir, Y., Pomorski, D., Innal, F., Liu, Y., Tolba, C. (Alexandria Engineering Journal)",
      "title": "STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison",
      "published": "2020-10",
      "url": "https://doi.org/10.1016/j.aej.2020.06.036",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "다중 로봇 시스템의 계층형 조정 구조별 위험 시나리오를 STPA 로 도출하고 Bowtie 로 평가·분류한 논문(59(5), pp.3799–3816, 온라인 2020-07-07). 이번에는 초록·서지만 확인했고 본문은 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1522",
      "org": "ISO",
      "title": "ISO/DIS 12100.3 - Safety of machinery — General principles for design — Risk assessment and risk reduction",
      "published": null,
      "url": "https://www.iso.org/standard/88578.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(iso.org 403). ISO 12100 개정 프로젝트 목록 페이지로, 메모는 2026-09-15 단계 40.60(DIS 투표 종료)이라고 적었으나 확인하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1523",
      "org": "한국표준협회 KSSN(국가기술표준원 고시)",
      "title": "KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항",
      "published": "2024-11-01",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010149365",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 발행일 2024-11-01, 고시 제2024-0480호(제정), 61쪽, 적용범위·제외 범위(관제·군집 관리 시스템 등)와 인용표준을 적는다. 표준 본문은 읽지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1524",
      "org": "한국표준협회 KSSN(국가기술표준원 고시)",
      "title": "KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템",
      "published": "2026-09-14",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158178",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 2026-09-14 개정(고시 제2026-0288호), 국제표준 부합화 ISO 3691-4:2023(IDT), 81쪽, 구판 2021-11-30. 표준 본문은 읽지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1525",
      "org": "고용노동부(국가법령정보센터)",
      "title": "사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호)",
      "published": "2024-12-18",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "현행 위험성평가 지침(2024-12-18 일부개정, 2025-01-02 시행). 도급·수급사업주의 각각 실시(제5조②), 근로자 참여(제6조), 수시·정기평가와 상시평가 간주 규정(제15조)을 정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1526",
      "org": "고용노동부(산재예방지원과)",
      "title": "사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고",
      "published": "2026-09-23",
      "url": "https://moel.go.kr/info/lawinfo/lawmaking/view.do?bbs_seq=20260900747",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "2026-09-23 게시된 위험성평가 지침 전부개정고시(안) 행정예고. 공고 번호와 의견 제출 마감일은 이번 대조에서 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1527",
      "org": "고용노동부",
      "title": "위험성평가 근로자 참여 가이드",
      "published": "2024-12",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20241202175",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "외국인·수급업체·일용근로자의 위험성평가 참여 사례를 담은 12쪽 가이드(표지 2024.12, 게시 2024-12-31). 청취조사로 아차사고·개선 의견을 모으는 방법과 문자·QR 익명 제안 사례를 싣는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1528",
      "org": "OMRON (Omron Adept Technologies)",
      "title": "Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H)",
      "published": "2019-10",
      "url": "https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OMRON LD 이동로봇 안전 매뉴얼(Rev H, 2019-10). 플릿 위치·경로 정보 교환은 충돌 방지 인터록이 아니며, 외부 비상정지에 사용자 부품이 들어가면 PL·PFH 계산과 최종 위험성평가를 사용자가 맡는다고 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1529",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_ros2 2.14.0 태그의 플릿 어댑터 소스. 대상 비상 신호(fleet_names) 처리기와, 기존 불리언 EmergencyNotice 구독 경로가 함께 있다. 커밋 일자는 확인하지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1530",
      "org": "Perez, I., Mavridou, A., Pressburger, T., Will, A., Martin, P. J. (EPTCS 371)",
      "title": "Monitoring ROS2: from Requirements to Autonomous Robots",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.14030",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "FRET 요구사항에서 Ogma 로 ROS 2 실행 시간 감시기를 생성하는 방법(FMAS/ASYDE 2022, EPTCS 371 pp.208–216, DOI 10.4204/EPTCS.371.15). 관련 연구 절에서 자기 방식이 위반의 탐지·보고로 한정된다고 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-563",
      "org": "Belzile, B. 외",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "건설 현장 이동 로봇 배치용 위험성평가 사례 논문(arXiv v1 2025-02-28). 이번에 PDF 본문에서 Pomerleau 현장·Clearpath Jackal 배치 맥락과 잔류 위험지수 재추정 방식을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2502.20693v1",
      "source_unopened": false
    },
    {
      "id": "ref-1255",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "A3 판매 페이지. 위키는 2026-10-09 열람 기록으로 발행일 2026-04-23·77쪽을 이미 갖고 있다. 이번 재열람은 403 으로 실패했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-789",
      "org": "ISO",
      "title": "ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": null,
      "url": "https://www.iso.org/standard/88615.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(iso.org 403). ISO 3691-4 차기판 프로젝트 페이지. 위키는 2026-09-26 'ISO/CD' 로 기록했고 메모는 'ISO/DIS, Edition 3, 40.60(2026-09-10)' 로 적어 서로 다르다. 제목 갱신은 확인 전까지 보류.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 현행 ISO 3691-4 제2판(2023) 목록 페이지(2020 판이 제1판).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-561",
      "org": "대한민국 정책브리핑(중소벤처기업부)",
      "title": "이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어",
      "published": "2024-11-03",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148935814",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(이번 실행). 이동식 협동로봇 안전기준 KS 를 2024-11-01 부터 활용할 수 있게 됐다는 정부 발표. 표준 번호는 적지 않는다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세. 이번에 3.0.0 태그 본문에서 안전 표준이 아니라는 범위 문장, startPause·stopPause, safetyState.activeEmergencyStop(MANUAL·REMOTE·NONE)을 다시 확인했다(모두 기존 위키 내용).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1077",
      "org": "Open Navigation (ros-navigation/navigation2)",
      "title": "nav2_collision_monitor — README",
      "published": null,
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Collision Monitor README. 1.5.2 태그 판에서도 하드 실시간 안전 인증을 제공하지 않는다고 적는다(기존 위키 내용).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-navigation/navigation2/1.5.2/nav2_collision_monitor/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(이번 재열람 GitHub 403). 화재경보가 대상 플릿 구분 없이 모든 로봇을 주차시킨다는 2025-04-04 기능 요청 이슈.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1398",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_fleet_adapter 변경 이력(2.14.0 태그). 2.10.0(2025-05-09) 절에 플릿 이름으로 화재경보를 분리하는 #413 이 실려 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    },
    {
      "id": "ref-555",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EU 기계 규정. 이번에 2026-07-27 통합본(02023R1230, Regulation (EU) 2026/1744 반영)에서 제3조(16) 실질적 변경 정의의 (a)·(b) 조건과 제54조 조항별 적용일을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eur-lex.europa.eu/eli/reg/2023/1230/2026-07-27/eng/pdf",
      "source_unopened": false
    },
    {
      "id": "ref-417",
      "org": "Obi, I. 외(arXiv)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "LLM 제어 로봇의 실행 전 안전 게이트(SafeGate) 논문(arXiv v1 2026-04-07). 이번에 평가 층위(230개 합성 벤치마크·30개 AI2-THOR·실물 정성 결과), 충돌률 식(9)의 분모, 표 II 집계를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2604.05427v1",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "sections": [
        "3",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3(분리 2026-09-25-area25-s3) — 국내 위험성평가 실시 주체와 변경 조건: 도급·수급사업주 각각 실시(f17), 근로자 참여 5개 경우(f18), 수시평가 1~6호(f19), 제15조④ 간주 규정(f20). 2026 전부개정안은 예고안으로만(f23, 공고 번호·마감일은 f24 [추정]) / 섹션 5 — '출하 마감 전 화재경보' 표 제약 칸(107행) 정정: 2.10.0(2025-05-09) #413 플릿 이름 선택(f29 [사실]), 2.14.0 대상 비상 신호 처리(f30 [사실])와 기존 불리언 EmergencyNotice 경로 병존(f31 [사실])을 함께 적고 '이후 구현 여부 미확인' 을 지움(f32). 이슈 세부(두 건물)는 f28 [추정]. 같은 주장이 docs/categories/safety/index.md 95행과 docs/categories/governance-law-and-society/index.md 84행에도 있으나 이번 실행 범위 밖이라 후속 정리 필요. 운영 시사점 f45. Belzile 사례는 현장 유형 '기타(건설 현장)' 로 8절에만 넣고 5절 시나리오로 만들지 않음 / 섹션 6(분리 2026-09-25-area25-s6) — STPA 산출물: 네 단계(f1)·위험한 제어 행동 네 유형(f2)과 ROP 적용 의견(f40); 운영자 참여 기록: 청취조사 아차사고·개선 의견(f21), 일용근로자 사례 문자·QR 익명 제안(f22), 제15조④ 간주 규정과 연결(f20); 감시와 대응 구분: Ogma 탐지·보고 한정(f25, 위치는 §3 Related work 의 DeRoS 비교 문장), 의견 f44. VDA 5050 pause 의견 f43. 기존 내용 확인(새로 넣지 않음): VDA 5050 안전 표준 아님(2026-09-25-area25-s3.md 39행, 2026-09-25-area25-s6.md 49행), startPause·stopPause(2026-09-25-area20-s4.md 42행, 2026-09-25-area25-s6.md 49행), activeEmergencyStop MANUAL·REMOTE·NONE(docs/categories/safety/index.md 113행), Nav2 하드 실시간 인증 미제공(2026-09-30-area49-s6.md 47행, 2026-09-30-area49-s7.md 47행, ref-1077) / 섹션 7(분리 2026-09-25-area25-s7·2026-09-26-area25-s7) — 2026-09-25-area25-s7.md 43행 R15.08-2 행의 '예정된 Part 3' 을 'Part 3(2026-04-23 발행)' 으로 정정(f7; 발행 사실은 기존 내용 확인 — ref-1255, safety/index.md 53행, 재추가하지 않음). 2026-09-26-area25-s7.md 46행 '차기판(제2판 초안)' 은 2023 판이 제2판이므로 '차기판(제3판)' 으로 정정 제안(f10 [추정], 단계·날짜는 미확인). ISO/DIS 3691-4 Edition 3·40.60(2026-09-10)과 ISO/DIS 12100.3 40.60(2026-09-15)은 확인 불가라 [추정]으로만(f8·f9) — ref-789 는 2026-09-26 'ISO/CD' 로 기록돼 메모와 충돌하므로 제목 갱신 보류. 이동식 협동로봇 KS 행(2026-09-25-area25-s7.md 46행 '표준 번호는 미확인'): KS B 7327 번호·표제·발행일·고시(f11), 관제·군집 관리 제외 범위(f12), 부합화 칸 공란·인용표준(f13), 발표 KS = KS B 7327(f14 [추정]). KS B ISO 3691-4 2026-09-14 개정·ISO 3691-4:2023(IDT) 행 추가(f16) / 섹션 8(분리 2026-09-25-area25-s8) — Bensaci 외 2020 AEJ(f3, 초록 범위로 축소; 11대·한계는 f4 [추정]/제외), Belzile 사례 조건: Pomerleau·몬트리올·Clearpath Jackal 배치 예정(f5), 잔류 위험지수는 재추정 값(f6) — 기존 '현장 전문가 검증을 거쳤다고 저자가 보고' [추정] 문장은 유지; ICAR 2021 판 날짜는 근거가 없어 쓰지 않음. SafeGate 평가 층위(f36: 230개·30개 수치는 기존 내용 확인 — 2026-09-25-area25-s6.md 53행, safety/index.md 69행, 실물 실험 정성 결과·단계 4~6 시험이 새 내용), CR 분모 문제(f37), 표 II 183건(f38)과 차이 해석(f39 [추정]), 의견 f46 / 섹션 9 — 로봇 자체·시설 경계에 제조사 매뉴얼의 플릿 정보≠인터록(f26)·사용자 부품 포함 PL·PFH·최종 위험성평가 사용자 책임(f27) 을 벤더 주장 [추정]으로; 업종별 조건 행에 국내 지침의 도급·수급 각각 실시(f17)와 책임 배분 추정(f41); EU 실질적 변경 정의의 (a)·(b) 조건(f33)·제54조 조항별 적용일(f34, 일반 적용일 2027-01-20 은 기존 내용 확인 — 2026-09-25-area24-s3.md 41행)과 해석(f35) / 섹션 11 — 부분 근거만(해결 제안 없음): oq-070 근거 f11·f14, oq-064 근거 f13·f15, oq-093 근거 f33~f35(oq-282 와 겹침), oq-095 근거 f42, oq-096 근거 f41. 메모의 '신규 질문' 3건(혼합 플릿 RA 수행·갱신 주체, VDA 원격/플릿 정지 경로 PL, 규칙 223 울타리 생략의 AMR 플릿 적용)은 질문 문구를 대조해 각각 기존 oq-096·oq-095·oq-097 과 같아 새로 만들지 않음. oq-092·oq-097 은 이번 메모가 답하지 못함(확인 못 함). 관련 기존 질문: oq-265(R15.08-3 사용자 의무, f7 은 발행 사실만), oq-123(KS 새 판 부합 — f16 은 3691-4 에 관한 것이라 10218-2·TS 15066 질문에는 답하지 않음), oq-170(ISO 3691-4 원문, 미해결). 새 질문 3건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사(f7~f16), 58. 다사업자 책임·계약·데이터(f17·f41), 59. 법·규제·보험·라이선스(f33~f35), 47. AI·학습·적응과 모델 운영(f36~f39)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "SafeGate 논문의 충돌률(CR)은 실행된 작업이 0건일 때 어떻게 산정되며, 표 II 의 183건과 전체 230건 사이에서 빠진 47건은 어떤 범주(판단 보류 등)인지 저자 코드·원자료로 재현할 수 있는가? | 관련 영역: 48. 안전·위험 관리, 47. AI·학습·적응과 모델 운영 | 근거: f37 | 종류: 일반",
    "Open-RMF 의 플릿 이름 기반 비상 신호(fleet_names)를 건물·구역 단위 대피 계획에 연결할 때, 여러 건물에 걸친 플릿 공유·재개 승인·네트워크 단절·기존 불리언 신호와의 충돌을 어떻게 시험·검증하는가? | 관련 영역: 48. 안전·위험 관리, 22. 설비·건물 시스템 연동 | 근거: f30 | 종류: 일반",
    "여러 제조사 로봇이 섞인 현장에서 STPA 제어 구조 분석, 변경 이력(수시 위험성평가), 근로자 아차사고 제보를 하나의 위험등록부로 연결해 운영한 공개 실증 사례가 있는가? | 관련 영역: 48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사 | 근거: f40 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 22,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-04/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f3·f4: Bensaci 외 2020 은 초록·Crossref 서지만 확인(본문 미접근). 메모 F03(11로봇·화학 분석실)은 [추정], F05(시나리오 병합 한계)는 확인 불가로 finding 에서 뺌. 'semi quantitative'·'modified hierarchical' 표현과 '2020-06-21 채택' 은 미확인",
      "f5·f6: Belzile 논문은 arXiv v1(2025-02-28) PDF 기준. 메모의 'ICAR 2021 워크숍판·2021-12-07' 은 근거가 없어 쓰지 않음(arXiv 에는 'Workshop … at ICAR' 표기만)",
      "f7: A3 판매 페이지 재열람 403 — 발행일은 기존 ref-1255(2026-10-09 열람) 기준",
      "f8~f10: iso.org 403 으로 ISO/DIS 3691-4(Edition 3, 40.60, 2026-09-10)·ISO/DIS 12100.3(40.60, 2026-09-15) 미확인. ref-789 의 2026-09-26 'ISO/CD' 기록과 충돌. 3691-4 의 판 번호(2020 제1판·2023 제2판)도 목록 원문으로 재확인 필요",
      "f13·f14: KS B 7327 과 R15.08-2·ISO 10218 의 조항별 대응·동등 인증 미확인(본문 미열람). 정책브리핑 발표 KS 와의 동일성은 날짜·고시 사유 일치에 근거한 추정",
      "f24: 행정예고 공고 번호(2026-461)와 의견 제출 마감(2026-10-13) 미확인. 최종 고시 발령·시행 상태 미확인",
      "f28: RMF issue #658 재열람 GitHub 403 — '두 건물' 등 세부 미확인",
      "f26·f27: OMRON 매뉴얼은 원문 대조로 문서 내용을 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 벤더 문서만 근거라 vendor_claim: true·[추정]으로 둔다",
      "f37~f39: SafeGate 저자 코드·원자료 미확인, 게재지 미확인(arXiv v1 프리프린트)",
      "메모의 VDA 5050 '2026-03' 날짜는 명세 안에 근거가 없어 쓰지 않음(ref-031 published null 유지)",
      "oq-092(펌웨어·안전 파라미터 변경 재심사)·oq-097(규칙 223 울타리 생략의 AMR 플릿 적용)은 이번 메모에 근거가 없어 확인 못 함",
      "f7(R15.08-3 발행일 2026-04-23)은 위키에 2026-10-09 원문 열람 기록(ref-1255)이 있으나 이번에 A3 페이지를 다시 열지 못해 [추정]으로 둔다."
    ],
    "scope_violations": [
      "f17~f24: 국내 위험성평가 고시·가이드는 사업장 안전보건 법규로 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스와 겹치므로 이 영역에는 위험성평가 실시 주체·참여·변경 조건 근거로만 씀",
      "f26·f27: 비상정지 회로·PL·PFH 설계는 로봇 제조사·통합자 쪽 안전 기능(연계 대상)이며, ROP 몫은 인터페이스 구분과 검증 자료 요구로 한정",
      "f33~f35: EU 기계 규정 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인과 판단 조건 정리까지만 하고 개별 업데이트의 법적 분류는 하지 않음",
      "f36~f39·f46: SafeGate 는 LLM 명령의 실행 전 판정으로 47. AI·학습·적응과 모델 운영과 겹치며, 이 영역에는 평가 분모·층위 해석만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 11
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 11건/15(ref-1520~ref-1530, 예약 구간 ref-1520~ref-1549 안), 재사용 11건(ref-563·ref-1255·ref-789·ref-470·ref-561·ref-031·ref-1077·ref-567·ref-1398·ref-555·ref-417). 출처 매핑(검증 결과 기준): 메모 n1→ref-1520, n2→ref-1521(DOI 서지·초록), n3→ref-563, n4→ref-1255, n5→ref-789(제목 CD→DIS 갱신 보류), n6→ref-1522(미열람), n7→ref-1523, n8→ref-1524, n9→ref-1525, n10→ref-1526, n11→ref-1527, n12→ref-031, n13→ref-1077, n14→ref-1528, n15→ref-567(미열람), n16→ref-1529, n17→ref-1398, n18→ref-555(2026-07-27 통합본으로 열람), n19→ref-417, n20→ref-1530. 추가 재사용: ref-470(판 번호 정정 근거), ref-561(발표 KS 대응). fetched: false 는 ref-1522·ref-1255·ref-789·ref-470·ref-561·ref-567(이번 재열람 403 또는 미열람). ref-1521 은 초록·서지만 확인. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: 고시·가이드는 고용노동부, CHANGELOG·코드·이슈는 Open-RMF) — 신뢰도 medium 이하. 중복 제거: 메모 F08(R15.08-3 발행일)·F22~F25(VDA 5050 안전 표준 아님·startPause·stopPause·activeEmergencyStop)·F26(Nav2 인증 미제공)·F33 일반 정의와 F35 일반 적용일·F36·F37 수치는 기존 위키에 있어 새 finding 으로 넣지 않고 위치만 rationale 에 적었다(f7·f42~f44 는 정정·추론·의견에서 참조). 검증 반영: F03·F05 [추정]/제외, F04 초록 범위로 축소, F09~F11 [추정](ref-789 충돌), 공고 번호·F21 마감일 [추정], F30 세부 [추정], F17 의 '상시평가 인정 경로' → '제15조④ 간주 규정', F19 '일용근로자 사례' 명시, F27 위치 '§3 Related work DeRoS 비교 문장', F28·F29 벤더 주장 [추정], 2.14.0 의 불리언 EmergencyNotice 병존(f31) 추가, 2026-09-26-area25-s7.md 46행 '제2판 초안' 정정 제안(f10). 현장 유형: 물류창고(f32·f43·f45, 기존 가상 시나리오의 정정·의견), 기타(건설 현장 f5·f6, 다중 건물 배치 f28). 국내 자료: 고용노동부 고시·가이드·행정예고(ref-1525~ref-1527), KS 목록(ref-1523·ref-1524). 열린 질문 해결 제안 없음 — 부분 근거만: oq-064(f13·f15), oq-070(f11·f14), oq-093·oq-282(f33~f35), oq-095(f42), oq-096(f41). 메모의 '신규 질문' 3건은 기존 oq-095·oq-096·oq-097 과 같은 질문임을 질문 문장으로 확인해 새로 만들지 않았고, '새로 생긴 열린 질문' 3건은 docs/open-questions.md 에 같은 질문이 없어 새로 올린다. 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 원문 절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음(STPA·위험성평가는 이미 용어집에 있음)."
  }
}
```

### runs/2026-10-11-04/verification.json

```json
{
  "run_id": "2026-10-11-04",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 핸드북 PDF 는 검증 측에서 압축 스트림이라 읽히지 않았으나, STPA 4단계(목적 정의·제어 구조·UCA·손실 시나리오)는 핸드북을 인용한 2차 자료(York AAIP 지침, arXiv 2506.01782 등) 검색 결과와 일치. 방법론 안내서이며 로봇 플릿 실증 아님."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. UCA 네 유형(미제공·위험 제공·너무 이르거나 늦게/순서 틀림·너무 일찍 멈춤/너무 오래)이 핸드북 인용 2차 자료와 일치. 핸드북 원문 쪽수(36쪽)는 검증 측 미대조."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검색 결과에서 AEJ 59(5) pp.3799–3816, DOI 10.1016/j.aej.2020.06.036, 초록의 'STPA 로 계층형 조정 구조별 위험 시나리오 도출 → Bowtie 평가' 일치(HAL hal-03508510 도 같은 제목). ScienceDirect 는 403. 공저자 6명 전원은 검증 측 미대조. 초록 범위로 축소한 서술 유지."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 본문 미열람으로 11대·화학 분석실 조건을 확인하지 못했다는 점을 주장 안에 밝힘. 단정 금지."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv HTML v1). 'a building construction site managed by the company Pomerleau in Montreal', 'the intended deployment of a Clearpath Jackal' 확인. 현장 유형 기타(건설) 적정."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §4.3 'a new risk index was estimated', 측정 근거 서술 없음. 저자는 초록·결론에서 현장 전문가 검증을 언급하므로 기존 '[추정] 전문가 검증 보고' 문장과 병존 가능."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1255 는 이번 재열람 403(원문 미열람). 발행일 2026-04-23 은 위키 기존 기록(2026-10-09 열람) 기준. 새 사실 추가가 아니라 '예정' 표현 정정."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 유지. ref-789 원문 미열람. 검증 검색에서 DIN 이 ISO/DIS 3691-4:2026 초안 의견수렴(2026-06-26~08-26)을 게시해 차기판이 DIS 단계라는 메모 쪽과 부합하는 정황이 있으나, 이는 브리프 밖 출처라 페이지에 넣지 않는다. ref-789 의 'ISO/CD' 기록과 충돌하므로 둘 다 제시·열린 질문 처리 필요."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 유지. ref-1522 원문 미열람(iso.org). 검색 결과에서 iso.org/standard/88578 은 ISO/DIS 12100 개정 프로젝트로 실재 확인, Certifico 가 ISO/DIS 12100.3 투표(2026-07-20 시작)를 보도해 메모와 부합하나 40.60·2026-09-15 는 미확인. 기존 위키 '2026 FDIS 도달 전망' 문장은 재확인 대상."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 유지. 2020 판 제1판·2023 판 제2판 구조와 'Edition 3' 표기 정합. ISO 목록 원문 미열람(ref-470·ref-789). 단계 표현은 f8 충돌과 함께 재확인."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KSSN 상세 페이지는 검증 측에서 제목만 렌더링됐으나, 검색 결과 요약에 표제·발행일 2024-11-01·고시 제2024-0480호·고시 사유(모바일 로봇+협동로봇 결합형 표준·인증 부재) 일치. 61쪽은 검증 측 미확인."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검색 결과 요약에 적용범위 제외 문장('통합 제조 시스템(IMS), 관제 시스템, 군집 관리 시스템, 기타 기계 설비류는 이 표준에서 다루지 않는다') 일치. 목록 기준·본문 미열람."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "출처 실재 확인. 부합화 칸 공란·인용표준 목록은 검증 측 재렌더링 실패로 직접 대조하지 못함(원문 열람은 리서치 기록 기준). 반대 근거 없음. 목록 기준 서술로 한정."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 발표문(ref-561, 이번 원문 미열람)과 KS B 7327 의 날짜·고시 사유 일치에 근거한 동일성 추정. 조항 대응 미확인 명시 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. R15.08-2 원문·KS B 7327 본문 모두 미열람이라 대응·동등성 미확인을 명시함."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. KSSN 상세는 검증 측에서 제목만 렌더링됐고, 검색에서 2026-09-14 개정·고시 제2026-0288호·ISO 3691-4:2023(IDT)·81쪽을 확인하지 못했다. 반대로 중국 표준 목록(ndls.org.cn)은 2021-11-30 판을 현행으로 표시한다(갱신 지연 가능). 리서치 원문 열람 기록은 있으나 검증 측 재확인 실패라 단일 미재확인 출처로 본다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 국가법령정보센터 페이지에서 고용노동부고시 제2024-76호·2024-12-18 일부개정·2025-01-02 시행 확인. 조문 본문 탭은 연결 재설정으로 재열람 실패했으나 제5조② '도급인·수급인 각각 실시'는 검색 결과의 지침 해설과 일치."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 제6조 다섯 경우(판단 기준 마련·요인 파악·허용 여부 결정·감소대책 수립·실행 여부 확인)에 해당 작업 근로자 참여가 검색 결과 지침 해설과 일치. 조문 원문은 검증 측 재열람 실패."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 고시 번호·시행일은 법령정보센터에서 확인, 제15조② 1~6호는 검증 측 조문 재열람 실패(연결 재설정)로 브리프 인용과 지침 해설 자료 범위에서 판단. 반대 근거 없음. '소프트웨어 변경이 자동으로 수시평가 대상이라는 문구 없음' 단서 유지."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 상시평가 간주 규정의 존재는 2023 개정 보도·해설로 확인(당시 보도는 건설업 중심으로 소개). 현행 제15조④ 문구는 검증 측 조문 재열람 실패. 현행 조문 문언대로만 쓰고 적용 업종 해석을 덧붙이지 않는다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 고용노동부 게시 페이지에서 제목·게시일 2024-12-31·외국인·수급업체·일용근로자 참여 사례 수록을 확인. 청취조사 세부는 첨부 PDF 라 검증 측 미대조. 고시(ref-1525)와 같은 기관이라 독립 교차 확인 아님. 효과 검증 자료 아님 단서 유지."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 일용근로자 사례 수록은 게시 페이지로 확인, 문자·QR 익명 제안 세부는 첨부 PDF 라 검증 측 미대조. 반대 근거 없음."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고용노동부 입법·행정예고 게시: 제목·등록일 2026-09-23·산재예방지원과 일치. 예고안이며 시행 규정 아님 단서 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 검증에서 게시 페이지가 '고용노동부 공고 제2026-461호'를 표시함을 확인했다(공고 번호는 확인됨). 의견 제출 마감일 2026-10-13 은 페이지에 표시되지 않아 미확인."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 초록 페이지에서 저자 5명·EPTCS 371 pp.208–216·DOI 10.4204/EPTCS.371.15·2022-09-28 확인. ar5iv 본문 §3 Related work 에 'DeRoS also allows users to specify how property violations must be handled, while our approach is limited …' 문장 확인."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장 유지. OMRON PDF 는 검증 측에서 압축 스트림이라 읽히지 않았고 검색으로도 해당 문구를 찾지 못했다(문서 실재는 OMRON 사이트의 LD Safety Guide 목록으로 확인). 리서치 원문 대조 기록 기준. 특정 제품·2019 판으로 한정."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장 유지. f26 과 같은 이유로 검증 측 문구 미대조. 법적 의무 판단이 아닌 제품 매뉴얼의 책임 구분 진술로 한정."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 유지. ref-567 은 이번 재열람 403(검증 측 GitHub API 도 403). 이슈 핵심은 기존 위키 내용과 일치, '두 건물' 세부 미확인 명시."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(raw.githubusercontent). 2.10.0 (2025-05-09) 절에 'Giving options to separate fire alarm by fleet names (#413)', 2.14.0 절 2026-09-26 확인. 최초 도입판 여부는 변경 이력 기준."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. FleetUpdateHandle.cpp handle_target_emergency: fleet_names.empty() 이면 execute=true, 이름 일치 시 execute=true, execute 이면 handle_emergency(is_emergency). 코드 열람이며 배치 시험 아님."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Node.cpp 에 EmergencyNotice(EmergencyTopicName)와 TargetEmergencyNotice(EmergencySignalTopicName) 구독이 공존."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f29~f31 로 기존 5절 제약 칸 '이후 구현 여부 미확인'이 낡았음 확인. 세 출처 모두 Open-RMF 계열이라 독립 교차 확인 아님. safety/index.md 95행·governance-law-and-society/index.md 84행에도 같은 낡은 주장 있음(후속 정리)."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(EUR-Lex 2026-07-27 통합본). 제3조(16)의 물리적·디지털 수단, 제조자 미예견, 새 위험·기존 위험 증가, (a) 기존 안전 제어 시스템 변경이 필요한 방호장치 추가 또는 (b) 안정성·기계적 강도 보호조치 조건 일치."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 제54조: 일반 2027-01-20, 제26~42조 2024-01-20, 제50조(1) 2026-10-20, 제6조(7)·제48조·제52조 2023-07-19, 제6조(2)~(6)·(8)·(11)·제47조·제53조(3) 2024-07-20 일치."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. f33 조문에서 도출한 해석이며 개별 업데이트 법적 분류·제18조 의무 주체는 판단하지 않았다고 밝힘. 집행 지침 미확인."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv HTML v1). 230개 벤치마크는 'Stage 1-3', 실물 실험은 §V-C 에서 단계 4~6 시험과 함께 전체 SafeGate 구조 실행도 적고 §VI-C 는 정량 지표 없이 정성 결과만 보고. 30개 AI2-THOR 가 어느 단계를 평가하는지는 논문이 명시하지 않음 — '시뮬레이션 실행 평가' 이상으로 단계를 특정하지 않는다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 식(9) 분모 T_exec(승인되어 시뮬레이터에서 실행된 작업), 거부·보류 작업은 지표에 들어가지 않는다고 명시. 30개 모두 차단 시 0/0 이지만 CR 0% 로 보고, 산정 규칙 설명 없음."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 표 II SafeGate TP100·FN0·FP6·TN77=183, 다른 방법 행도 모두 183. 230 과의 차이 설명 문장 없음."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. 결정 게이트 출력이 {authorize, defer, reject} 이고 §V-A 에 'ambiguous' 정답 범주 언급이 있어 추론 근거는 있으나 47건 제외는 논문이 명시하지 않음."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. STPA 절차를 ROP 제어 구조에 대입한 구축자 의견임을 밝혀야 함(수정 지시). 실증 아님."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. f17·f18·f27 에서 도출, ROP 사업자를 지칭하는 규정 없음·책임 배분 미확정 명시. 법적 의무 판단은 59. 법·규제·보험·라이선스 연계로만."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·low 적정. VDA 5050 3.0.0 범위 문장('shall not be regarded or applied as a safety standard')은 입력 원문 텍스트로 확인, f26 은 벤더 주장. 특정 경로 PL 미결정 명시."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지하되 구축자 의견 병기 필요. VDA 5050 표 4 는 stopPause 가 (설정된 경우) 하드웨어 버튼으로 startPause 된 로봇도 재시작할 수 있다고 적으므로, 'stopPause 는 안전 기능 해제 절차가 아니다'를 명세의 사실처럼 단정하지 않도록 수정 지시."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지, 구축자 의견 병기 필요. Nav2 README 의 하드 실시간 인증 미제공은 기존 위키 내용, Ogma 는 f25 로 확인. 별개 구현이라 교차 입증 아님."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지, 구축자 의견 병기 필요. f30·f31 에서 도출한 시험 항목 제안."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지, 구축자 의견 병기 필요. f37·f38 분모 문제에서 도출."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f17~f24·f41: 국내 위험성평가 고시는 현장 사업주의 법적 의무다. 브리프 rationale 은 9절 '업종별 조건' 행에 넣자고 하나, ROP 직접 열이 아니라 외부 연계 열(현장 사업주 의무)과 59. 법·규제·보험·라이선스 연결로만 다뤄야 한다(편집으로 해결 가능).",
      "f26·f27: 비상정지 회로·PL·PFH 계산·인터록은 원문 19장 '로봇 자체 지능·제어' 경계의 연계 대상(제조사·통합자)이다. ROP 몫은 인터페이스 구분과 검증 자료 요구로 한정한다.",
      "f33~f35: EU 기계 규정 조문은 조건 소개와 59. 법·규제·보험·라이선스 연결로 한정하고, 개별 ROP 업데이트의 법적 분류를 판단하지 않는다.",
      "f45: 화재 시 로봇 이동·정지 정책은 현장 대피 계획(시설·설비 경계의 연계 대상)과 함께 정해야 한다는 범위로 유지한다."
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "f32 가 정정하는 '비상 신호는 대상 플릿을 구분하지 않는 불리언, 이후 구현 여부 미확인' 주장은 대상 페이지 5절 외에 docs/categories/safety/index.md 95행·docs/categories/governance-law-and-society/index.md 84행에도 있다 — 이번 실행 범위 밖이므로 후속 갱신 대상으로 기록한다.",
      "f7·f10·f11~f15 의 정정 대상 문장은 분리 주제 페이지(docs/topics/2026/2026-09-25-area25-s7.md 43·46행, docs/topics/2026/2026-09-26-area25-s7.md 46행)에 있으나 page_proposals 는 세부영역 페이지 하나뿐이다.",
      "f8: ISO 3691-4 차기판 단계에 대해 기존 ref-789 기록(2026-09-26 'ISO/CD')과 메모('ISO/DIS, Edition 3, 40.60')가 충돌한다 — 한쪽을 고르지 않는다.",
      "f9: 기존 2026-09-26-area25-s7.md 47·48행의 'ISO/DIS 12100:2024 기반 DIN 초안'·'2026 FDIS 도달 전망'은 f9 의 DIS 12100.3 재투표 정황과 어긋날 수 있다(재확인 대상).",
      "f36 의 230개·30개 수치, f42 의 VDA 5050 안전 표준 아님·activeEmergencyStop, f44 의 Nav2 인증 미제공, f33 의 일반 정의·f34 의 일반 적용일은 기존 위키에 있다 — 기존 각주(ref-417·ref-031·ref-1077·ref-555)를 재사용하고 같은 문장을 새로 쓰지 않는다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f11~f15: KS B 7327 표제의 '이동 머니퓰레이터'는 표준 이름이므로 그대로 두되, 본문 일반 용어는 용어집 '모바일 매니퓰레이터 (Mobile Manipulator)'로 통일하고 링크한다.",
      "f1·f2·f40: '위험한 제어 행동(Unsafe Control Action)'은 용어집에 없으므로 첫 등장 때 영문을 함께 쓰고 용어집 STPA 항목에 링크한다(신규 등록은 하지 않음).",
      "f33~f35: '실질적 변경'은 용어집 substantial-modification(실질적 변경, Substantial Modification)에 링크한다."
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": [
      "ref-1525·ref-555·ref-417·ref-1529 는 evidence_excerpt 에 여러 구절이 있다. 페이지에서는 출처당 직접 인용 1회까지만 쓰고 나머지는 요약·재서술한다(수정 지시)."
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f16: [사실] → [추정]으로 강등한다 — 검증에서 KS B ISO 3691-4 의 2026-09-14 개정·고시 제2026-0288호·ISO 3691-4:2023(IDT)를 다시 확인하지 못했고, 다른 표준 목록은 2021-11-30 판을 현행으로 표시한다. 7절에 새 행을 넣을 때도 '국가표준 목록 기준, 검증 미재확인'을 밝힌다.",
    "f24: [추정] 태그는 유지한다. 검증에서 ref-1526 게시 페이지가 '고용노동부 공고 제2026-461호'를 표시함을 확인했으므로 '공고 번호를 확인하지 못했다'는 문구는 쓰지 않는다. 의견 제출 마감일(2026-10-13)만 미확인으로 남긴다.",
    "f40·f43·f44·f45·f46: [의견] 문장마다 '구축자 의견:'을 앞에 붙여 누구의 의견인지 밝힌다 — 공통 규칙 2절, 검증 항목 5.",
    "f43: VDA 5050 표 4 는 stopPause 가 (설정된 경우) 하드웨어 버튼으로 startPause 된 로봇도 재시작할 수 있다고 적는다. 그러므로 'stopPause 는 안전 기능 해제 절차가 아니다'를 명세가 말한 사실처럼 쓰지 않는다. '비상정지 회로 리셋과 같다는 근거가 없다'는 범위의 구축자 의견으로 쓴다.",
    "f26·f27: 9절 외부 연계 열(로봇 제조사·통합자)에만 [추정]으로 넣고 'OMRON LD Safety Guide Rev H(2019-10) 기준 벤더 주장'을 병기한다. 타사 플릿과 현행 모델로 일반화하지 않는다.",
    "f17~f22·f41: 국내 위험성평가 지침 내용을 9절 '업종별 조건' 행의 ROP 직접 열에 넣지 않는다. 외부 연계 열(현장 사업주의 법적 의무)과 3절·6절 근거로만 쓰고 59. 법·규제·보험·라이선스·58. 다사업자 책임·계약·데이터에 연결한다 — 범위 경계(원문 19장).",
    "f33~f35: 9절에서는 제3조(16)의 (a)·(b) 조건과 제54조 적용일 소개로 한정한다. f35 는 [추정]으로 두고, 개별 ROP 정책·어댑터 업데이트가 실질적 변경인지 단정하지 않는다. 59. 법·규제·보험·라이선스와 oq-093·oq-282 에 연결한다.",
    "f8·f9·f10: ref-789 의 'ISO/CD 3691-4'(2026-09-26 기록)와 메모의 'ISO/DIS 3691-4, Edition 3, 40.60'이 충돌한다. 본문에 둘 다 [추정]으로 제시하고, 11절에 '출처 충돌'로 적어 oq-170 에 연결한다. ref-789 제목은 바꾸지 않는다. ISO/DIS 12100.3 단계(f9)도 [추정]으로만 쓴다.",
    "정정 반영 위치: page_proposals 는 docs/categories/safety/safety-and-risk-management.md 하나뿐이다. 그러므로 f7(R15.08 Part 3 '예정' 표현)·f10(차기판 판 번호)·f11~f15(KS 번호)의 정정은 이 페이지 해당 절(7·11절) 패치 안에 쓰고, 분리 주제 페이지는 이번에 직접 고치지 않는다. 손대지 않은 정정 대상 위치(docs/topics/2026/2026-09-25-area25-s7.md 43행, docs/topics/2026/2026-09-26-area25-s7.md 46행, docs/categories/safety/index.md 95행, docs/categories/governance-law-and-society/index.md 84행)는 diff_summary·changelog_entry 에 '후속 갱신 필요'로 적는다.",
    "f32: 5절 '출하 마감 전 화재경보' 표 제약 칸의 기존 '[사실][^ref-567] … 이후 구현 여부는 미확인' 문장을 바꾼다. 2.10.0(2025-05-09) #413(f29)·2.14.0 대상 비상 신호의 빈 fleet_names=전체 플릿(f30)·기존 불리언 경로 병존(f31)을 각각 [사실]로 적고, 정정 판단(f32)과 이슈 세부(f28)는 [추정]으로 둔다. 세 출처가 모두 Open-RMF 계열이라는 점을 밝힌다.",
    "f36: 실물 로봇 실험을 '단계 4~6만 시험'으로 한정하지 않는다. 논문 §V-C 는 단계 4~6 시험과 함께 전체 SafeGate 구조 실행도 적는다. 30개 AI2-THOR 시나리오가 평가하는 단계는 논문이 명시하지 않으므로 특정하지 않는다.",
    "인용 길이: ref-1525·ref-555·ref-417·ref-1529 등 evidence_excerpt 에 여러 구절이 있는 출처는 페이지에서 출처당 직접 인용 1회까지만 쓰고 나머지는 재서술한다 — 공통 규칙 2절.",
    "원문 미열람 표시: 이번 실행에서 원문을 열지 못한 ref-1522·ref-1255·ref-789·ref-470·ref-561·ref-567 은 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 해당 항목에 source_unopened: true 를 넣는다.",
    "용어: 본문의 일반 용어 '이동 머니퓰레이터'는 용어집 '모바일 매니퓰레이터'로 통일하고 링크한다(KS B 7327 표제는 그대로 둔다). '위험한 제어 행동(Unsafe Control Action)'은 첫 등장 때 영문을 함께 쓴다. '실질적 변경'은 용어집 substantial-modification 에 링크한다.",
    "중복: 230개·30개 수치, VDA 5050 안전 표준 아님·activeEmergencyStop, Nav2 인증 미제공, 제3조(16) 일반 정의, 일반 적용일 2027-01-20 은 기존 각주(ref-417·ref-031·ref-1077·ref-555)를 재사용해 연결만 하고 같은 문장을 새로 추가하지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 45건, 미확인 1건, 교차 확인 0건. 강등: f16 사실 → 추정(KS B ISO 3691-4 의 2026-09-14 개정을 검증에서 다시 확인하지 못했고, 다른 목록은 2021-11-30 판을 현행으로 표시함). 원문 미열람 출처: ref-1522, ref-1255, ref-789, ref-470, ref-561, ref-567. 이번 검증에서 다시 확인하지 못한 출처: ref-1520·ref-1528(PDF 판독 불가), ref-1525 조문 본문(연결 재설정), ref-1527 첨부 PDF, ref-1523·ref-1524 상세(KSSN 렌더링). ref-1520 은 2차 자료, ref-1523 은 검색 결과 요약, ref-1525 는 고시 번호·시행일과 해설 자료 범위로 확인했다. ref-1520·ref-1521·ref-1523~ref-1528·ref-1530 은 fetched: true 인데 fetch_url 이 비어 있다(리서치 기록 보완 요청). 검증에서 확인한 사항: 행정예고 공고 번호 제2026-461호(f24, 의견 제출 마감일은 미확인). 주의: 모든 [사실] 주장이 단일 출처이거나 같은 기관 계열 출처(고용노동부 고시·가이드, Open-RMF 변경 이력·코드·이슈)에 기대며, 교차 확인된 주장은 없다. ISO 3691-4 차기판 단계는 기존 ref-789 기록(CD)과 메모(DIS)가 충돌해 둘 다 [추정]으로만 싣는다. Open-RMF 대상 비상 신호는 코드를 읽어 확인한 것이며 대피 안전성을 검증한 것이 아니다. SafeGate 의 충돌률 0%는 실행 0건(0/0)에서 나온 값이라 무사고율로 읽지 않는다. 정정 요청 없음. 새 열린 질문 3건은 형식에 맞고 기존 질문과 중복되지 않는다. 분리 주제 페이지와 다른 대분류 페이지에 남은 낡은 문장(R15.08 Part 3 '예정', ISO 3691-4 '제2판 초안', RMF 비상 신호 '구현 여부 미확인')은 후속 갱신 대상이다. 브리프의 검색 횟수는 집계되지 않았다(외부 조사 변환). 검증 검색은 16회다.",
  "retry_reason": null
}
```

### runs/2026-10-11-04/pages.json

```json
{
  "run_id": "2026-10-11-04",
  "outline": [
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1300,
      "summary": "기존 요약·링크를 유지하고, 국내 지침이 도급·수급사업주 각각 실시, 근로자 참여, 수시평가 조건, 상시평가 간주 규정을 정한다는 내용을 덧붙인다. [사실][^ref-1525] 2026-09-23 전부개정안은 예고안으로만 적는다. [사실][^ref-1526]",
      "planned_findings": [
        "f17",
        "f18",
        "f19",
        "f20",
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 0,
      "summary": "변경 없음.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "물류창고 화재경보 사례의 제약 칸을 Open-RMF 2.10.0 #413 과 2.14.0 대상 비상 신호로 정정한다. [사실][^ref-1398][^ref-1529] 정지·재개 분리와 비상 신호 시험 항목은 구축자 의견으로 덧붙인다.",
      "planned_findings": [
        "f28",
        "f29",
        "f30",
        "f31",
        "f32",
        "f43",
        "f45"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "STPA 네 단계와 위험한 제어 행동 네 유형을 정리하고 [사실][^ref-1520], 근로자 참여 기록 방법과 [사실][^ref-1527] 감시와 대응의 구분을 [사실][^ref-1530] 덧붙인다.",
      "planned_findings": [
        "f1",
        "f2",
        "f40",
        "f21",
        "f22",
        "f25",
        "f44"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1500,
      "summary": "R15.08 Part 3 발행, ISO 3691-4 차기판 판 번호·단계 충돌, ISO 12100 개정 단계를 [추정]으로 정정·보강하고, KS B 7327 의 번호·범위·인용표준을 적는다. [사실][^ref-1523]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "Bensaci 외 2020 STPA·Bowtie 결합 연구 [사실][^ref-1521], Belzile 사례 조건 [사실][^ref-563], SafeGate 평가 층위와 분모 문제 [사실][^ref-417]를 덧붙인다.",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f6",
        "f36",
        "f37",
        "f38",
        "f39",
        "f46"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1700,
      "summary": "외부 연계 열에 제조사 매뉴얼의 인터록·PL 책임 구분(벤더 주장)과 국내 지침의 사업주 의무를 넣고 [추정] 벤더 주장[^ref-1528], EU 실질적 변경 조건과 적용일을 소개한다. [사실][^ref-555]",
      "planned_findings": [
        "f26",
        "f27",
        "f17",
        "f41",
        "f33",
        "f34",
        "f35"
      ]
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 0,
      "summary": "변경 없음.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "section": "11. 열린 질문",
      "budget_chars": 1600,
      "summary": "oq-064·oq-070·oq-093·oq-095·oq-096 에 부분 근거를 달고 [추정][^ref-1523], ISO 3691-4 차기판 단계 출처 충돌과 새 질문 3건을 올린다.",
      "planned_findings": [
        "f8",
        "f14",
        "f15",
        "f35",
        "f41",
        "f42",
        "f37",
        "f30",
        "f40"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/safety/safety-and-risk-management.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3·5·6·7·8·9·11·13절 차등 갱신: 국내 위험성평가 지침(실시 주체·근로자 참여·수시평가), Open-RMF 대상 비상 신호로 화재경보 사례 제약 칸 정정, STPA 산출물·참여 기록·감시와 대응 구분, R15.08 Part 3·ISO 3691-4 판 번호·KS B 7327 정정·보강, Bensaci 2020·Belzile 사례 조건·SafeGate 분모, 책임 경계(벤더 주장·사업주 의무·EU 실질적 변경 조건), 열린 질문 부분 근거와 새 질문 4건. 후속 갱신 필요: docs/topics/2026/2026-09-25-area25-s7.md 43행, docs/topics/2026/2026-09-26-area25-s7.md 46행, docs/categories/safety/index.md 95행, docs/categories/governance-law-and-society/index.md 84행",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-004",
              "ref-031",
              "ref-417",
              "ref-470",
              "ref-472",
              "ref-555",
              "ref-560",
              "ref-561",
              "ref-563",
              "ref-564",
              "ref-566",
              "ref-567",
              "ref-789",
              "ref-1077",
              "ref-1255",
              "ref-1398",
              "ref-1520",
              "ref-1521",
              "ref-1522",
              "ref-1523",
              "ref-1524",
              "ref-1525",
              "ref-1526",
              "ref-1527",
              "ref-1528",
              "ref-1529",
              "ref-1530"
            ],
            "confidence": "medium",
            "last_run": "2026-10-11",
            "version": 4
          },
          "content": "(절 본문 생략 — runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"11. 열린 질문\" 절(1,870자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,600자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"8. 대표 연구와 자료\" 절(1,350자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"6. 대표 접근법과 기술\" 절(1,145자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"3. 왜 중요한가\" 절(996자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"4. 핵심 개념과 용어\" 절(691자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area48-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 48. 안전·위험 관리 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(462자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 48. 안전·위험 관리 | 3·5·6·7·8·9·11절 차등 갱신(국내 위험성평가 지침, Open-RMF 대상 비상 신호로 화재경보 사례 정정, STPA 산출물·근로자 참여·감시와 대응 구분, R15.08 Part 3·ISO 3691-4 판 번호 정정과 KS B 7327, SafeGate 평가 분모, 제조사 매뉴얼 책임 구분·EU 실질적 변경 조건), 후속 갱신 필요: docs/topics/2026/2026-09-25-area25-s7.md 43행, docs/topics/2026/2026-09-26-area25-s7.md 46행, docs/categories/safety/index.md 95행, docs/categories/governance-law-and-society/index.md 84행 | run 2026-10-11-04",
  "index_updates": {
    "home_recent": "2026-10-11 — 48. 안전·위험 관리: 국내 위험성평가 지침·KS B 7327·Open-RMF 대상 비상 신호·STPA 산출물을 반영해 3·5~9·11절 갱신",
    "category_recent": "2026-10-11 — 48. 안전·위험 관리: 화재경보 사례의 비상 신호 서술 정정(Open-RMF 2.10.0 이후 플릿 이름 지정), 국내 위험성평가 실시 주체·수시평가 조건, KS B 7327 과 ISO 3691-4 차기판 표기 정정, SafeGate 평가 분모 문제 추가",
    "area_recent": "2026-10-11 — 48. 안전·위험 관리: 3·5·6·7·8·9·11절 차등 갱신(정정 3건 반영, 새 열린 질문 4건). 분리 주제 페이지와 M. 안전·P. 거버넌스·법규·사회 대분류 페이지의 같은 낡은 문장은 후속 갱신 대상"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1520",
      "org": "Leveson, N. G., Thomas, J. P. (MIT Partnership for Systems Approaches to Safety and Security)",
      "title": "STPA Handbook",
      "published": "2018-03",
      "url": "https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "STPA 방법 안내서. 분석 목적 정의→제어 구조 모델링→위험한 제어 행동 식별→손실 시나리오 식별의 4단계와 위험한 제어 행동 4유형을 설명한다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1521",
      "org": "Bensaci, C., Zennir, Y., Pomorski, D., Innal, F., Liu, Y., Tolba, C. (Alexandria Engineering Journal)",
      "title": "STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison",
      "published": "2020-10",
      "url": "https://doi.org/10.1016/j.aej.2020.06.036",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "다중 로봇 시스템의 계층형 조정 구조별 위험 시나리오를 STPA 로 도출하고 Bowtie 로 평가·분류한 논문(59(5), pp.3799–3816, 온라인 2020-07-07). 이번에는 초록·서지만 확인했고 본문은 열지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1522",
      "org": "ISO",
      "title": "ISO/DIS 12100.3 - Safety of machinery — General principles for design — Risk assessment and risk reduction",
      "published": null,
      "url": "https://www.iso.org/standard/88578.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(iso.org 403). ISO 12100 개정 프로젝트 목록 페이지로, 메모는 2026-09-15 단계 40.60(DIS 투표 종료)이라고 적었으나 확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1523",
      "org": "한국표준협회 KSSN(국가기술표준원 고시)",
      "title": "KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항",
      "published": "2024-11-01",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010149365",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 발행일 2024-11-01, 고시 제2024-0480호(제정), 61쪽, 적용범위·제외 범위(관제·군집 관리 시스템 등)와 인용표준을 적는다. 표준 본문은 읽지 않았다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1524",
      "org": "한국표준협회 KSSN(국가기술표준원 고시)",
      "title": "KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템",
      "published": "2026-09-14",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158178",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 2026-09-14 개정(고시 제2026-0288호), 국제표준 부합화 ISO 3691-4:2023(IDT), 81쪽, 구판 2021-11-30. 표준 본문은 읽지 않았고, 1차 검증에서 개정 정보를 다시 확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1525",
      "org": "고용노동부(국가법령정보센터)",
      "title": "사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호)",
      "published": "2024-12-18",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "현행 위험성평가 지침(2024-12-18 일부개정, 2025-01-02 시행). 도급·수급사업주의 각각 실시(제5조②), 근로자 참여(제6조), 수시·정기평가와 상시평가 간주 규정(제15조)을 정한다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1526",
      "org": "고용노동부(산재예방지원과)",
      "title": "사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고",
      "published": "2026-09-23",
      "url": "https://moel.go.kr/info/lawinfo/lawmaking/view.do?bbs_seq=20260900747",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "2026-09-23 게시된 위험성평가 지침 전부개정고시(안) 행정예고(고용노동부 공고 제2026-461호). 의견 제출 마감일은 확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1527",
      "org": "고용노동부",
      "title": "위험성평가 근로자 참여 가이드",
      "published": "2024-12",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20241202175",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "외국인·수급업체·일용근로자의 위험성평가 참여 사례를 담은 12쪽 가이드(표지 2024.12, 게시 2024-12-31). 청취조사로 아차사고·개선 의견을 모으는 방법과 문자·QR 익명 제안 사례를 싣는다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1528",
      "org": "OMRON (Omron Adept Technologies)",
      "title": "Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H)",
      "published": "2019-10",
      "url": "https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OMRON LD 이동로봇 안전 매뉴얼(Rev H, 2019-10). 플릿 위치·경로 정보 교환은 충돌 방지 인터록이 아니며, 외부 비상정지에 사용자 부품이 들어가면 PL·PFH 계산과 최종 위험성평가를 사용자가 맡는다고 설명한다(벤더 주장).",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1529",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_ros2 2.14.0 태그의 플릿 어댑터 소스. 대상 비상 신호(fleet_names) 처리기와, 기존 불리언 EmergencyNotice 구독 경로가 함께 있다. 커밋 일자는 확인하지 않았다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1530",
      "org": "Perez, I., Mavridou, A., Pressburger, T., Will, A., Martin, P. J. (EPTCS 371)",
      "title": "Monitoring ROS2: from Requirements to Autonomous Robots",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.14030",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "FRET 요구사항에서 Ogma 로 ROS 2 실행 시간 감시기를 생성하는 방법(FMAS/ASYDE 2022, EPTCS 371 pp.208–216, DOI 10.4204/EPTCS.371.15). 관련 연구 절에서 자기 방식이 위반의 탐지·보고로 한정된다고 밝힌다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-563",
      "org": "Belzile, B. 외",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "건설 현장 이동 로봇 배치용 위험성평가 사례 논문(arXiv v1 2025-02-28). 이번에 PDF 본문에서 Pomerleau 현장·Clearpath Jackal 배치 맥락과 잔류 위험지수 재추정 방식을 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1255",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(이번 재열람 403). A3 판매 페이지. 위키는 2026-10-09 열람 기록으로 발행일 2026-04-23·77쪽을 이미 갖고 있다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-789",
      "org": "ISO",
      "title": "ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": null,
      "url": "https://www.iso.org/standard/88615.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(iso.org 403). ISO 3691-4 차기판 프로젝트 페이지. 위키는 2026-09-26 'ISO/CD' 로 기록했고 메모는 'ISO/DIS, Edition 3, 40.60(2026-09-10)' 로 적어 서로 다르다. 제목 갱신은 확인 전까지 보류.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 현행 ISO 3691-4 제2판(2023) 목록 페이지(2020 판이 제1판).",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-561",
      "org": "대한민국 정책브리핑(중소벤처기업부)",
      "title": "이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어",
      "published": "2024-11-03",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148935814",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(이번 실행). 이동식 협동로봇 안전기준 KS 를 2024-11-01 부터 활용할 수 있게 됐다는 정부 발표. 표준 번호는 적지 않는다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세. 이번에 3.0.0 태그 본문에서 안전 표준이 아니라는 범위 문장, startPause·stopPause, safetyState.activeEmergencyStop(MANUAL·REMOTE·NONE)을 다시 확인했다(모두 기존 위키 내용).",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-1077",
      "org": "Open Navigation (ros-navigation/navigation2)",
      "title": "nav2_collision_monitor — README",
      "published": null,
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Collision Monitor README. 1.5.2 태그 판에서도 하드 실시간 안전 인증을 제공하지 않는다고 적는다(기존 위키 내용).",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람(이번 재열람 GitHub 403). 화재경보가 대상 플릿 구분 없이 모든 로봇을 주차시킨다는 2025-04-04 기능 요청 이슈.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1398",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_fleet_adapter 변경 이력(2.14.0 태그). 2.10.0(2025-05-09) 절에 플릿 이름으로 화재경보를 분리하는 #413 이 실려 있다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-555",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EU 기계 규정. 이번에 2026-07-27 통합본(02023R1230, Regulation (EU) 2026/1744 반영)에서 제3조(16) 실질적 변경 정의의 (a)·(b) 조건과 제54조 조항별 적용일을 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    },
    {
      "id": "ref-417",
      "org": "Obi, I. 외(arXiv)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "LLM 제어 로봇의 실행 전 안전 게이트(SafeGate) 논문(arXiv v1 2026-04-07). 이번에 평가 층위(합성 벤치마크·AI2-THOR 시나리오·실물 정성 결과), 충돌률 식(9)의 분모, 표 II 집계를 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-and-risk-management.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "SafeGate 논문의 충돌률(CR)은 실행된 작업이 0건일 때 어떻게 산정되며, 표 II 의 183건과 전체 230건 사이에서 빠진 47건은 어떤 범주(판단 보류 등)인지 저자 코드·원자료로 재현할 수 있는가?",
      "areas": [
        48,
        47
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Open-RMF 의 플릿 이름 기반 비상 신호(fleet_names)를 건물·구역 단위 대피 계획에 연결할 때, 여러 건물에 걸친 플릿 공유·재개 승인·네트워크 단절·기존 불리언 신호와의 충돌을 어떻게 시험·검증하는가?",
      "areas": [
        48,
        22
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "여러 제조사 로봇이 섞인 현장에서 STPA 제어 구조 분석, 변경 이력(수시 위험성평가), 근로자 아차사고 제보를 하나의 위험등록부로 연결해 운영한 공개 실증 사례가 있는가?",
      "areas": [
        48,
        50
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: ISO 3691-4 차기판 프로젝트의 현재 단계는 위키 기록(2026-09-26, ISO/CD 3691-4)과 외부 조사 메모(ISO/DIS 3691-4 제3판, 2026-09-10 단계 40.60) 가운데 어느 쪽인가? (관련 기존 질문 oq-170)",
      "areas": [
        48,
        50
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/safety/safety-and-risk-management.md#5-적용-사례-현장-유형-명시",
      "title": "48. 안전·위험 관리"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/safety/safety-and-risk-management.md#5-적용-사례-현장-유형-명시",
      "title": "48. 안전·위험 관리"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/safety/safety-and-risk-management.md#5-적용-사례-현장-유형-명시",
      "title": "48. 안전·위험 관리"
    }
  ],
  "additional_research_requests": [
    "후속 정정(이번 실행 범위 밖): docs/topics/2026/2026-09-25-area25-s7.md 43행(R15.08 Part 3 '예정'), docs/topics/2026/2026-09-26-area25-s7.md 46행(ISO 3691-4 '제2판 초안', 이동식 협동로봇 KS '표준 번호 미확인'), docs/categories/safety/index.md 95행과 docs/categories/governance-law-and-society/index.md 84행(RMF 비상 신호 '이후 구현 여부 미확인')을 이번 페이지의 정정 내용에 맞춰 갱신해야 한다.",
    "7절·11절: ISO 3691-4 차기판의 현재 단계(ISO/CD 대 ISO/DIS 제3판, 단계 40.60·2026-09-10)를 ISO 원문 또는 국가 표준기관 공개 자료로 확인해야 출처 충돌을 해소할 수 있다.",
    "7절: ISO/DIS 12100.3 의 단계(40.60, 2026-09-15)를 확인하고, 분리 주제 페이지의 'ISO/DIS 12100:2024 기반 DIN 초안'·'2026 FDIS 도달 전망' 문장이 여전히 맞는지 재확인해야 한다.",
    "7절·11절(oq-064·oq-070): KS B 7327 본문의 조항과 R15.08-2·ISO 10218-2:2025·ISO 3691-4:2023 의 대응, 관련 인증 기준 유무가 필요하다.",
    "7절: KS B ISO 3691-4 의 2026-09-14 개정(고시 제2026-0288호, ISO 3691-4:2023 IDT)을 독립 출처로 다시 확인해야 [사실]로 쓸 수 있다.",
    "3절: 위험성평가 지침 전부개정고시(안)의 의견 제출 마감일과 최종 고시·시행일이 확인되면 반영할 수 있다.",
    "8절: Bensaci 외(2020) 본문의 로봇 대수·현장 조건과 한계, SafeGate 저자 코드·원자료(47건 제외 사유)를 확인해야 추정 문장을 정리할 수 있다.",
    "11절: oq-092(펌웨어·안전 파라미터 변경 재심사)와 oq-097(규칙 제223조 울타리 생략의 AMR 플릿 적용)은 이번 브리프에 근거가 없다."
  ],
  "fixes_applied": [
    "f16 강등 — 7절 KS B ISO 3691-4 항목을 [추정]으로 쓰고 '국가표준 목록 기준(검증 미재확인)'을 문장 안에 밝혔다.",
    "f24 — 3절에서 [추정]을 유지하고 공고 번호 제2026-461호는 그대로 적었으며, 의견 제출 마감일(2026-10-13)만 확인하지 못했다고 썼다.",
    "f40·f43·f44·f45·f46 — 각 [의견] 문장 앞에 '구축자 의견:'을 붙였다(6절 f40·f44, 5절 f43·f45, 8절 f46).",
    "f43 — 5절에서 stopPause 가 안전 기능 해제 절차가 아니라고 명세의 사실처럼 쓰지 않고, '비상정지 회로 리셋과 같다는 근거가 없다'는 범위의 구축자 의견으로 썼다.",
    "f26·f27 — 9절 로봇 자체 지능·제어 행의 외부 연계 열에만 [추정] 벤더 주장으로 넣고 'OMRON LD Safety Guide Rev H(2019-10) 기준'과 타사·현행 모델로 일반화하지 않는다는 단서를 병기했다.",
    "f17~f22·f41 — 국내 지침 내용을 9절 ROP 직접 열에 넣지 않고 업종별 조건 행의 외부 연계 열(현장 사업주의 법적 의무)과 3절·6절 근거로만 썼으며, 3절·9절에서 58. 다사업자 책임·계약·데이터와 59. 법·규제·보험·라이선스에 연결했다.",
    "f33~f35 — 9절에서 제3조(16)의 (a)·(b) 조건과 제54조 적용일 소개로 한정하고 f35 는 [추정]으로 두어 개별 업데이트의 법적 분류를 단정하지 않았으며, 59. 법·규제·보험·라이선스와 oq-093·oq-282 에 연결했다.",
    "f8·f9·f10 — 7절에 ref-789 의 'ISO/CD' 기록과 메모의 'ISO/DIS 제3판, 40.60'을 둘 다 [추정]으로 제시하고 11절에 출처 충돌 질문(oq-170 관련)을 올렸으며, ref-789 제목은 바꾸지 않았고 ISO/DIS 12100.3 단계도 [추정]으로만 썼다.",
    "정정 반영 위치 — f7·f10·f11~f15 의 정정을 이 페이지 7·11절 패치 안에 쓰고 분리 주제 페이지는 고치지 않았으며, 손대지 않은 네 위치를 diff_summary·changelog_entry 에 '후속 갱신 필요'로 적었다.",
    "f32 — 5절 화재경보 표 제약 칸에서 '이후 구현 여부는 미확인'을 지우고 2.10.0 #413(f29)·빈 fleet_names=전체 플릿(f30)·불리언 경로 병존(f31)을 각각 [사실]로, 정정 판단(f32)과 이슈 세부(f28)를 [추정]으로 쓰고 세 출처가 모두 Open-RMF 계열임을 밝혔다.",
    "f36 — 8절에서 실물 실험을 단계 4~6 시험과 전체 SafeGate 구조 실행을 함께 다룬 것으로 쓰고, AI2-THOR 시나리오는 '시뮬레이션 실행 평가'로만 적어 단계를 특정하지 않았다.",
    "인용 길이 — ref-1525·ref-555·ref-417·ref-1529 를 포함한 모든 출처를 직접 인용 없이 요약·재서술했다.",
    "원문 미열람 표시 — ref-1522·ref-1255·ref-789·ref-470·ref-561·ref-567 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "용어 — 본문 일반 용어는 '모바일 매니퓰레이터'로 쓰고 용어집에 링크했으며(KS B 7327 표제는 그대로), '위험한 제어 행동(Unsafe Control Action)'은 6절 첫 등장 때 영문을 함께 쓰고 STPA 용어집에 링크했고, '실질적 변경'은 9절에서 substantial-modification 용어집에 링크했다.",
    "중복 — 230개·30개 수치, VDA 5050 안전 표준 아님·activeEmergencyStop, Nav2 인증 미제공, 제3조(16) 일반 정의, 일반 적용일 2027-01-20 은 새 사실 문장으로 추가하지 않고 '앞서 위키가 확인한' 맥락 언급과 기존 각주(ref-417·ref-031·ref-1077·ref-555) 재사용으로만 연결했다.",
    "분량 초과 자동 분리: 48. 안전·위험 관리 본문 11,967자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,117자"
  ],
  "standards_updates": [
    {
      "name": "KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항",
      "kind": "표준",
      "org": "국가기술표준원(한국표준협회 KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010149365",
      "related_areas": [
        48,
        50,
        31
      ],
      "summary": "2024-11-01 제정(고시 제2024-0480호) 국가표준. 모바일 로봇과 협동로봇 결합형의 안전 요구를 다루며, 관제·군집 관리 시스템은 범위에서 뺀다. 중소벤처기업부 발표 '이동식 협동로봇 안전기준 KS'와 같은 표준으로 보인다(추정).",
      "ref_id": "ref-1523"
    },
    {
      "name": "KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템",
      "kind": "표준",
      "org": "국가기술표준원(한국표준협회 KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158178",
      "related_areas": [
        48,
        50
      ],
      "summary": "국가표준 목록은 2026-09-14 개정(고시 제2026-0288호), ISO 3691-4:2023(IDT) 부합으로 표시한다. 검증에서 개정 정보를 다시 확인하지 못했다.",
      "ref_id": "ref-1524"
    },
    {
      "name": "사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호)",
      "kind": "프레임워크",
      "org": "고용노동부",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202",
      "related_areas": [
        48,
        58,
        59
      ],
      "summary": "2025-01-02 시행 현행 지침. 도급·수급사업주의 각각 실시, 근로자 참여, 수시·정기평가와 상시평가 간주 규정을 정한다. 2026-09-23 전부개정안이 행정예고됐다.",
      "ref_id": "ref-1525"
    },
    {
      "name": "STPA Handbook",
      "kind": "프레임워크",
      "org": "MIT Partnership for Systems Approaches to Safety and Security",
      "url": "https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf",
      "related_areas": [
        48
      ],
      "summary": "STPA 분석의 네 단계(목적 정의·제어 구조·위험한 제어 행동·손실 시나리오)와 위험한 제어 행동 네 유형을 설명하는 방법 안내서(2018-03).",
      "ref_id": "ref-1520"
    }
  ]
}
```

### runs/2026-10-11-04/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/safety/safety-and-risk-management.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/safety/safety-and-risk-management.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area48-s11.md (1,870자)
    - docs/categories/safety/safety-and-risk-management.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area48-s7.md (1,600자)
    - docs/categories/safety/safety-and-risk-management.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area48-s8.md (1,350자)
    - docs/categories/safety/safety-and-risk-management.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area48-s6.md (1,145자)
    - docs/categories/safety/safety-and-risk-management.md "3. 왜 중요한가" → docs/topics/2026/2026-10-11-area48-s3.md (996자)
    - docs/categories/safety/safety-and-risk-management.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-11-area48-s4.md (691자)
    - docs/categories/safety/safety-and-risk-management.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-11-area48-s10.md (462자)
```

### runs/2026-10-11-04/pages/categories/safety/safety-and-risk-management.md

```markdown
---
title: "48. 안전·위험 관리"
type: area
category: "M. 안전"
area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [위험성평가, STPA, 운용 구역, 비상정지, VDA 5050, 안전 책임 경계]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-004, ref-031, ref-417, ref-470, ref-472, ref-555, ref-560, ref-561, ref-563, ref-564, ref-566, ref-567, ref-789, ref-1077, ref-1255, ref-1398, ref-1520, ref-1521, ref-1522, ref-1523, ref-1524, ref-1525, ref-1526, ref-1527, ref-1528, ref-1529, ref-1530]
last_run: 2026-10-11
version: 4
---

[홈](../../index.md) › [M. 안전](index.md) › 48. 안전·위험 관리

# 48. 안전·위험 관리

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-09-26 · 마지막 실행: 2026-09-26
<!-- auto:page-status:end -->

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]

## 3. 왜 중요한가

확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08 Part 1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025)을 나누어 다루고, STPA 연구는 개별적으로 정상인 구성요소 사이의 상호작용에서 위험을 찾는다. 그래서 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. [추정][^ref-470][^ref-472][^ref-560][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 왜 중요한가](../../topics/2026/2026-10-11-area48-s3.md)에 있다.

## 4. 핵심 개념과 용어

**위험성평가(Risk Assessment)** — ISO 12100:2010 이 기계 설계의 일반 원칙으로 정하는, 위험원을 찾고 위험을 평가해 위험 감소 필요성을 판단하는 절차다. [사실][^ref-566]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area48-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 두 장면 모두 ROP 가 안전 기능을 직접 수행하지 않고, 로봇·설비가 보고한 안전 상태를 받아 작업을 보류·재배정·재개하는 장면이다.

### 피킹 중 작업자 진입

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 구역에 작업자가 들어와 로봇이 멈춘 뒤 작업을 이어가기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업자가 피킹 구역에 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고한다. [추정][^ref-031] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 로봇은 안전 상태를 보고하고, ROP 는 진행 중 피킹 작업의 보류·재배정과 재개 지시를 맡는다. [추정][^ref-031] |
| 제약 | 안전 상태가 해제되고 운용 모드가 자동(AUTOMATIC)으로 돌아오기 전에는 재개하지 않는다. [추정][^ref-031] |
| 완료·인계 | 재개 조건을 확인한 뒤 즉시 동작 stopPause 등으로 재개를 지시한다. [추정][^ref-031] |
| 예외·성과 | 멈춘 로봇의 피킹 작업을 보류하거나 다른 로봇에 재배정해야 할 것으로 보인다. [추정][^ref-031] |

여기서 ROP 의 몫은 정지 자체가 아니라 정지 뒤의 업무 처리다. 어떤 주문을 기다리게 하고 어떤 주문을 다른 로봇에 넘길지가 이 영역과 [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)이 만나는 지점이다.

구축자 의견: VDA 5050 의 업무 일시정지·재개 명령(startPause·stopPause)이 비상정지 회로 리셋과 같다는 근거는 없으므로, ROP 는 업무 일시정지 해제와 현장 안전정지 해제 승인을 별도 상태로 관리하고 제조사·설비의 해제 조건 충족을 확인하기 전에는 재개를 지시하지 않는 정책을 두는 것이 바람직하다. [의견][^ref-031]

### 출하 마감 전 화재경보

**물류 흐름 단계:** 출하

**시나리오:** 출하 준비 중 비상 신호로 로봇이 주차한 뒤 작업 재개

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 전에 화재경보 같은 비상 신호가 온다. [추정][^ref-567] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | Open-RMF 기능 요청에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동한다. [사실][^ref-567] |
| 제약 | 이슈 #658 작성 시점(2025-04-04) 기준으로 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다. [사실][^ref-567] 이슈 작성자는 두 건물에 로봇을 둔 상황에서 한 건물의 화재경보가 모든 로봇을 주차시킨다고 보고한 것으로 보이나, 세부 상황은 확인하지 못했다. [추정][^ref-567] rmf_fleet_adapter 변경 이력은 2.10.0(2025-05-09) 절에 플릿 이름으로 화재경보를 분리하는 선택지(#413)를 싣는다. [사실][^ref-1398] 2.14.0 코드에서 플릿 어댑터는 대상 비상 신호의 플릿 이름 목록(fleet_names)이 비어 있거나 자기 플릿 이름을 포함할 때만 비상 처리를 하므로, 빈 목록은 모든 플릿에 적용된다. [사실][^ref-1529] 같은 2.14.0 코드에는 플릿을 가리지 않는 기존 불리언 비상 알림(EmergencyNotice) 구독 경로도 함께 남아 있다. [사실][^ref-1529] 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 마감 준수에 영향을 주는 것으로 보인다. [추정][^ref-567][^ref-004] |

이 표의 제약 칸은 2026-10-11 갱신에서 고쳤다. 이전 판은 이슈 작성 뒤의 구현 여부를 미확인으로 두었으나, 변경 이력과 코드로 보면 2.10.0 부터 플릿 이름으로 대상을 고르는 비상 신호가 있고 2.14.0 에는 기존 불리언 경로와 대상 지정 경로가 함께 있다고 쓰는 것이 맞아 보인다. 다만 세 출처가 모두 Open-RMF 계열이라 독립 교차 확인이 아니고, 코드 열람이므로 대피 안전성을 검증한 것도 아니며, 건물·구역 단위 구분은 플릿 이름 매핑 설계에 달려 있다. [추정][^ref-1398][^ref-1529][^ref-567]

구축자 의견: 빈 플릿 이름 목록이 전체 플릿을 뜻하므로 운영 화면은 빈 목록을 '전체 플릿'으로 분명히 표시하고, 잘못된 플릿 선택·신호 지연·중복 신호·재개 전 승인 조건을 시험 항목으로 두며, 화재 때 로봇의 이동·정지 정책은 시설·설비 경계의 연계 대상인 현장 대피 계획과 함께 정해야 한다. [의견][^ref-1529]

## 6. 대표 접근법과 기술

안전을 다루는 접근은 위험을 찾는 방법, 운영 중 안전 상태를 주고받는 방법, 실행 전에 명령을 거르는 방법으로 나뉜다. [추정][^ref-566][^ref-031][^ref-417]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area48-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준은 대부분 발행 기관 소개·발표 자료 기준이며 본문은 열람하지 않았다(각주의 원문 미열람 표시). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area48-s7.md)에 있다.

## 8. 대표 연구와 자료

Bensaci, C.·Zennir, Y.·Pomorski, D., A Comparative Study of STPA Hierarchical Structures in Risk Analysis(2018) — 다중 이동 로봇 시스템의 제어 구조별 위험 시나리오를 STPA 로 비교했다. 대상은 화학 분석 실험실의 다중 로봇이며 물류 현장이 아니다. [사실][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 연구와 자료](../../topics/2026/2026-10-11-area48-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집과 일시정지·재개 지시 [추정][^ref-031] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증(로봇 제조사) [추정][^ref-470][^ref-560] OMRON LD Safety Guide Rev H(2019-10)는 플릿 안의 로봇들이 위치·크기·경로 계획 정보를 주고받아 장애물 회피에 쓰는 것을 충돌을 막는 인터록 방식으로 보지 않고, 필요한 인터록은 사용자·통합자가 따로 갖춰야 한다고 설명한다(이 제품 매뉴얼 기준, 타사 플릿이나 현행 모델로 일반화하지 않음). [추정] 벤더 주장[^ref-1528] 같은 매뉴얼은 외부 비상정지 회로에 사용자 부품이 들어가면 그 부품을 포함한 성능 수준(Performance Level, PL)·시간당 위험 고장 확률(PFH) 계산과 최종 위험성평가를 사용자 책임으로 둔다(OMRON LD Safety Guide Rev H 기준 벤더 주장, 법적 의무 판단 아님). [추정] 벤더 주장[^ref-1528] |
| 시설·설비 제어 | 비상 신호에 따른 플릿별 대피·주차 조율 [추정][^ref-567][^ref-004] | 연계 대상: 현장 방호 설비와 설비 안전 제어 [추정][^ref-560] |
| 업종별 조건 | 구역·권한 제약을 경로·배정에 반영하는 운영 조율 [추정][^ref-004] | 연계 대상: 업종별 전문 안전 요구 [추정][^ref-563] 현장 사업주의 법적 의무로, 국내 지침은 도급사업주와 수급사업주가 각각 위험성평가를 하게 한다. [사실][^ref-1525] 이를 제조사 매뉴얼의 사용자 책임 구분과 함께 보면 혼합 플릿 현장의 위험성평가는 현장 사업주(도급 구조이면 각각)가 주체가 되고 ROP 사업자·제조사·설비업체는 계약에 따라 자료와 분석을 제공하는 구조로 보이나, ROP 사업자를 지칭하는 규정은 확인한 자료에 없어 실제 배분은 현장의 법적 주체·계약에 따라 달라 확정되지 않는다(oq-096). [추정][^ref-1525][^ref-1528] |

ROP 가 맡는 것은 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-567] 이 경계는 제품 전략에 따라 이동할 수 있으며, 이종 제조사를 연결하는 ROP 는 안전 기능을 제조사에 맡기고 그 상태와 결과를 받는 쪽에 설 수 있는 것으로 보인다([범위 경계](../../about/scope-boundary.md)). [추정][^ref-031][^ref-470][^ref-560] 국내 지침의 해석과 다사업자 책임 배분은 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)와 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)의 연계 범위다.

EU 기계 규정 2023/1230 제3조(16)의 [실질적 변경](../../glossary/substantial-modification.md)은 제조자가 예견·계획하지 않은 물리적·디지털 변경이 새 위험요인을 만들거나 기존 위험을 키워 안전에 영향을 주고, 그 결과 (a) 기존 안전 제어 시스템의 변경이 필요한 방호장치·보호장치 추가나 (b) 안정성·기계적 강도를 보장할 추가 보호조치가 필요한 경우로 한정된다(2026-07-27 통합본 기준). [사실][^ref-555] 같은 규정 제54조는 일반 적용일(2027-01-20)과 별도로 제26~42조는 2024-01-20, 제50조(1)은 2026-10-20, 제6조(7)·제48조·제52조는 2023-07-19, 제6조(2)~(6)·(8)·(11)·제47조·제53조(3)은 2024-07-20 부터 적용한다. [사실][^ref-555] 이 조건을 보면 ROP 정책·어댑터 업데이트가 실질적 변경인지는 업데이트마다 조건을 따져야 하며 디지털 변경이라는 이유만으로 모두 재인증 대상이라고 볼 수는 없어 보이나, 개별 업데이트의 법적 분류와 누가 제조자 의무를 지는지는 이번 자료로 판단하지 않았다(oq-093, oq-282). [추정][^ref-555] 이 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어지는 연계 범위다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) — ISO 10218-2:2025 에 사이버보안 요구가 들어오면서 안전과 보안이 맞물리는 것으로 보인다. [추정][^ref-560]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area48-s10.md)에 있다.

## 11. 열린 질문

**oq-064** (상태: 열림) 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 부분 근거: KS B 7327 이 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성과 인증 기준 대응은 확인되지 않는다(7절). [추정][^ref-1523]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 열린 질문](../../topics/2026/2026-10-11-area48-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-26 · 갱신 · [48. 안전·위험 관리](safety-and-risk-management.md) — 월간 재검증: 7절 재검증 내용은 주제 페이지로 분리되어 요약·링크만 남김. 2차: 프런트매터 last_run 2026-09-26 (실행 2026-09-26-02)
- 2026-09-26 · 생성 · [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-26-area25-s7.md) — 자동 분리: 25. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: ref-783 각주 정의 제목을 ISO 페이지 전체 제목으로 고침 (실행 2026-09-26-02)
- 2026-09-25 · 갱신 · [48. 안전·위험 관리](safety-and-risk-management.md) — seed → draft: 3~11절 첫 작성(표준 책임 분담, 정지·재개·비상 대응, STPA, SafeGate 트랙 반영), 페이지 상태 자동 영역 추가, 각주 11건(3·6·7·8·11절 상세는 주제 페이지로 분리). 2차: 9절 마지막 문장 어미를 추정형으로 수정 (실행 2026-09-25-63)
- 2026-09-25 · 생성 · [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area25-s6.md) — 자동 분리: 25. 안전·위험 관리 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '운영 조율 수단' 문장을 [사실]·[추정] 두 문장으로 나눴다 (실행 2026-09-25-63)
- 2026-09-25 · 생성 · [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area25-s7.md) — 자동 분리: 25. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: VDA 5050 행의 관계 칸을 [사실]·[추정]으로 나눴다 (실행 2026-09-25-63)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-10-11 (원문 미열람)
[^ref-472]: Association for Advancing Automation (A3), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-11
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-10-11
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)
[^ref-566]: CEN (iTeh Standards 카탈로그), EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction, 2010, https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010, 접근일 2026-09-25 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-10-11 (원문 미열람)
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-1398]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-11
[^ref-1523]: 한국표준협회 KSSN(국가기술표준원 고시), KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항, 2024-11-01, https://www.kssn.net/search/stddetail.do?itemNo=K001010149365, 접근일 2026-10-11
[^ref-1525]: 고용노동부(국가법령정보센터), 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호), 2024-12-18, https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202, 접근일 2026-10-11
[^ref-1528]: OMRON (Omron Adept Technologies), Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H), 2019-10, https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1, 접근일 2026-10-11
[^ref-1529]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독), 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
```

### docs/categories/safety/safety-and-risk-management.md

```markdown
---
title: "48. 안전·위험 관리"
type: area
category: "M. 안전"
area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [위험성평가, STPA, 운용 구역, 비상정지, VDA 5050, 안전 책임 경계]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-26
sources: [ref-004, ref-031, ref-470, ref-472, ref-560, ref-561, ref-417, ref-563, ref-564, ref-566, ref-567]
last_run: 2026-09-26
version: 3
---

[홈](../../index.md) › [M. 안전](index.md) › 48. 안전·위험 관리

# 48. 안전·위험 관리

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-09-26 · 마지막 실행: 2026-09-26
<!-- auto:page-status:end -->

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]

## 3. 왜 중요한가

확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08 Part 1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025)을 나누어 다루고, STPA 연구는 개별적으로 정상인 구성요소 사이의 상호작용에서 위험을 찾는다. 그래서 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. [추정][^ref-470][^ref-472][^ref-560][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area25-s3.md)에 있다.

## 4. 핵심 개념과 용어

- **위험성평가(Risk Assessment)** — ISO 12100:2010 이 기계 설계의 일반 원칙으로 정하는, 위험원을 찾고 위험을 평가해 위험 감소 필요성을 판단하는 절차다. [사실][^ref-566]
- **3단계 위험 감소 방법(Three-Step Method)** — 본질적 안전 설계 → 방호·보완 보호 조치 → [사용 정보](../../glossary/information-for-use.md)의 순서로, 앞 단계를 다한 뒤 다음 단계로 간다. [사실][^ref-566]
- **운용 구역(Operating Zone)** — ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. [사실][^ref-470] 로봇의 제어 상태를 뜻하는 [운용 모드](../../glossary/operating-mode.md)와는 다른 개념이다.
- **안전 상태 보고(safetyState)** — [VDA 5050](../../glossary/vda-5050.md) 3.0.0 상태 메시지가 비상정지 상태와 보호 필드 침범 여부(fieldViolation)를 알리는 항목이다. [추정][^ref-031]
- **[협동 적용](../../glossary/collaborative-application.md)(Collaborative Application)** — ISO 10218-2:2025 는 종전 ISO/TS 15066 의 협동 적용 요구를 본문에 통합했다. [사실][^ref-560]
- **시스템 이론적 프로세스 분석(System-Theoretic Process Analysis, STPA)** — 제어 구조를 기준으로 위험 시나리오와 원인 요인을 도출하는 위험 분석 기법으로, 다중 이동 로봇 시스템에도 적용됐다. [사실][^ref-564]

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 두 장면 모두 ROP 가 안전 기능을 직접 수행하지 않고, 로봇·설비가 보고한 안전 상태를 받아 작업을 보류·재배정·재개하는 장면이다.

### 피킹 중 작업자 진입

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 구역에 작업자가 들어와 로봇이 멈춘 뒤 작업을 이어가기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업자가 피킹 구역에 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고한다. [추정][^ref-031] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 로봇은 안전 상태를 보고하고, ROP 는 진행 중 피킹 작업의 보류·재배정과 재개 지시를 맡는다. [추정][^ref-031] |
| 제약 | 안전 상태가 해제되고 운용 모드가 자동(AUTOMATIC)으로 돌아오기 전에는 재개하지 않는다. [추정][^ref-031] |
| 완료·인계 | 재개 조건을 확인한 뒤 즉시 동작 stopPause 등으로 재개를 지시한다. [추정][^ref-031] |
| 예외·성과 | 멈춘 로봇의 피킹 작업을 보류하거나 다른 로봇에 재배정해야 할 것으로 보인다. [추정][^ref-031] |

여기서 ROP 의 몫은 정지 자체가 아니라 정지 뒤의 업무 처리다. 어떤 주문을 기다리게 하고 어떤 주문을 다른 로봇에 넘길지가 이 영역과 [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)이 만나는 지점이다.

### 출하 마감 전 화재경보

**물류 흐름 단계:** 출하

**시나리오:** 출하 준비 중 비상 신호로 로봇이 주차한 뒤 작업 재개

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 전에 화재경보 같은 비상 신호가 온다. [추정][^ref-567] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | Open-RMF 기능 요청에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동한다. [사실][^ref-567] |
| 제약 | 이슈 작성 시점(2025-04-04) 기준으로 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었고, 이후 구현 여부는 미확인이다. [사실][^ref-567] 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 마감 준수에 영향을 주는 것으로 보인다. [추정][^ref-567][^ref-004] |

## 6. 대표 접근법과 기술

안전을 다루는 접근은 위험을 찾는 방법, 운영 중 안전 상태를 주고받는 방법, 실행 전에 명령을 거르는 방법으로 나뉜다. [추정][^ref-566][^ref-031][^ref-417]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area25-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준은 대부분 발행 기관 소개·발표 자료 기준이며 본문은 열람하지 않았다(각주의 원문 미열람 표시). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-26-area25-s7.md)에 있다.

## 8. 대표 연구와 자료

Bensaci, C.·Zennir, Y.·Pomorski, D., A Comparative Study of STPA Hierarchical Structures in Risk Analysis(2018) — 다중 이동 로봇 시스템의 제어 구조별 위험 시나리오를 STPA 로 비교했다. 대상은 화학 분석 실험실의 다중 로봇이며 물류 현장이 아니다. [사실][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 연구와 자료](../../topics/2026/2026-09-25-area25-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집과 일시정지·재개 지시 [추정][^ref-031] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증(로봇 제조사) [추정][^ref-470][^ref-560] |
| 시설·설비 제어 | 비상 신호에 따른 플릿별 대피·주차 조율 [추정][^ref-567][^ref-004] | 연계 대상: 현장 방호 설비와 설비 안전 제어 [추정][^ref-560] |
| 업종별 조건 | 구역·권한 제약을 경로·배정에 반영하는 운영 조율 [추정][^ref-004] | 연계 대상: 업종별 전문 안전 요구 [추정][^ref-563] |

ROP 가 맡는 것은 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-567] 이 경계는 제품 전략에 따라 이동할 수 있으며, 이종 제조사를 연결하는 ROP 는 안전 기능을 제조사에 맡기고 그 상태와 결과를 받는 쪽에 설 수 있는 것으로 보인다([범위 경계](../../about/scope-boundary.md)). [추정][^ref-031][^ref-470][^ref-560]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) — ISO 10218-2:2025 에 사이버보안 요구가 들어오면서 안전과 보안이 맞물리는 것으로 보인다. [추정][^ref-560]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) — LLM 명령의 실행 전 안전 판정(SafeGate)이 AI 결과를 실행에 쓰는 기준 문제와 이어지는 것으로 보인다. [추정][^ref-417]
- [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md) — 사람이 자연어로 내린 지시를 실행 전에 거르는 지점에서 맞물리는 것으로 보인다. [추정][^ref-417]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 교통 충돌 예방과 긴급 작업의 우선 협상에서 맞물리는 것으로 보인다. [추정][^ref-004]
- [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 정지·재개 지시를 확실하게 전달하는 문제에서 맞물리는 것으로 보인다. [추정][^ref-031]
- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 펌웨어·정책 변경 뒤 안전 재평가가 필요한지의 문제로 이어진다. 관련 질문은 11절의 oq-092·oq-093 이다.

## 11. 열린 질문

**oq-064** (상태: 열림) 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 이번 실행에서도 확인하지 못했다. - **oq-070** (상태: 열림) 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? 제정 발표는 확인했지만 표준 번호는 미확인이다. [사실][^ref-561]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 열린 질문](../../topics/2026/2026-09-25-area25-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-26 · 갱신 · [48. 안전·위험 관리](safety-and-risk-management.md) — 월간 재검증: 7절 재검증 내용은 주제 페이지로 분리되어 요약·링크만 남김. 2차: 프런트매터 last_run 2026-09-26 (실행 2026-09-26-02)
- 2026-09-26 · 생성 · [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-26-area25-s7.md) — 자동 분리: 25. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: ref-783 각주 정의 제목을 ISO 페이지 전체 제목으로 고침 (실행 2026-09-26-02)
- 2026-09-25 · 갱신 · [48. 안전·위험 관리](safety-and-risk-management.md) — seed → draft: 3~11절 첫 작성(표준 책임 분담, 정지·재개·비상 대응, STPA, SafeGate 트랙 반영), 페이지 상태 자동 영역 추가, 각주 11건(3·6·7·8·11절 상세는 주제 페이지로 분리). 2차: 9절 마지막 문장 어미를 추정형으로 수정 (실행 2026-09-25-63)
- 2026-09-25 · 생성 · [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area25-s6.md) — 자동 분리: 25. 안전·위험 관리 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '운영 조율 수단' 문장을 [사실]·[추정] 두 문장으로 나눴다 (실행 2026-09-25-63)
- 2026-09-25 · 생성 · [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area25-s7.md) — 자동 분리: 25. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: VDA 5050 행의 관계 칸을 [사실]·[추정]으로 나눴다 (실행 2026-09-25-63)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-472]: Association for Advancing Automation (A3), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-561]: 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어, 2024-11-03, https://www.korea.kr/news/policyNewsView.do?newsId=148935814, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-09-25 (원문 미열람)
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)
[^ref-566]: CEN (iTeh Standards 카탈로그), EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction, 2010, https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010, 접근일 2026-09-25 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), Feature request — Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s11.md

```markdown
---
title: "48. 안전·위험 관리 — 열린 질문"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1523, ref-1525, ref-1528, ref-555, ref-561, ref-789]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#11
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 열린 질문

# 48. 안전·위험 관리 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-064** (상태: 열림) 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 부분 근거: KS B 7327 이 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성과 인증 기준 대응은 확인되지 않는다(7절). [추정][^ref-1523]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-064** (상태: 열림) 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 부분 근거: KS B 7327 이 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성과 인증 기준 대응은 확인되지 않는다(7절). [추정][^ref-1523]
- **oq-070** (상태: 열림) 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? 제정 발표는 확인했다. [사실][^ref-561] 부분 근거: 표준 번호는 발행일과 고시 사유가 일치하는 KS B 7327 로 보이나, 두 국제표준과의 조항 대응은 미확인이다(7절). [추정][^ref-1523][^ref-561]
- **oq-093** (상태: 열림) EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? 부분 근거: 제3조(16)이 디지털 변경을 포함하되 새 위험·기존 위험 증가와 (a)·(b) 조치 필요성을 함께 요구하므로 업데이트마다 조건을 따져야 하는 것으로 보이며, 개별 분류는 판단하지 않았다(9절, oq-282 와 겹침). [추정][^ref-555]
- **oq-095** (상태: 열림) ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? 부분 근거: VDA 5050 은 스스로 안전 표준이 아니라고 하고 원격 비상정지는 상태 보고 값이며, 제조사 매뉴얼은 플릿 정보 교환을 인터록으로 보지 않으므로, 이 경로에 요구되는 PL 은 이 문서들로 정해지지 않고 기능별 위험성평가와 제조사 안전 인터페이스로 따로 정해야 하는 것으로 보인다. [추정][^ref-031][^ref-1528]
- **oq-096** (상태: 열림) 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? 부분 근거: 국내 지침과 제조사 매뉴얼로 보면 현장 사업주가 주체가 되고 다른 사업자는 계약에 따라 자료를 제공하는 구조로 보이나 확정되지 않는다(9절, R15.08-2 원문 미열람). [추정][^ref-1525][^ref-1528]
- 출처 충돌(새 질문, 관련 기존 질문 oq-170): ISO 3691-4 차기판 프로젝트의 현재 단계는 위키 기록(2026-09-26, ISO/CD)과 외부 조사 메모(ISO/DIS 제3판, 2026-09-10 단계 40.60) 가운데 어느 쪽인가? 두 기록 모두 원문을 다시 확인하지 못했다(7절). [추정][^ref-789]
- 새 질문: SafeGate 논문의 충돌률(CR)은 실행된 작업이 0건일 때 어떻게 산정되며, 표 II 의 183건과 전체 230건 사이에서 빠진 47건은 어떤 범주(판단 보류 등)인지 저자 코드·원자료로 재현할 수 있는가? 관련 영역은 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)이다.
- 새 질문: Open-RMF 의 플릿 이름 기반 비상 신호(fleet_names)를 건물·구역 단위 대피 계획에 연결할 때, 여러 건물에 걸친 플릿 공유·재개 승인·네트워크 단절·기존 불리언 신호와의 충돌을 어떻게 시험·검증하는가? 관련 영역은 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)이다.
- 새 질문: 여러 제조사 로봇이 섞인 현장에서 STPA 제어 구조 분석, 변경 이력(수시 위험성평가), 근로자 아차사고 제보를 하나의 위험등록부로 연결해 운영한 공개 실증 사례가 있는가? 관련 영역은 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)이다.

새 질문의 번호는 [열린 질문](../../open-questions.md) 목록에서 부여된다. oq-092·oq-097 은 이번 실행에서 근거를 찾지 못했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1523]: 한국표준협회 KSSN(국가기술표준원 고시), KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항, 2024-11-01, https://www.kssn.net/search/stddetail.do?itemNo=K001010149365, 접근일 2026-10-11
[^ref-1525]: 고용노동부(국가법령정보센터), 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호), 2024-12-18, https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202, 접근일 2026-10-11
[^ref-1528]: OMRON (Omron Adept Technologies), Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H), 2019-10, https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1, 접근일 2026-10-11
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-561]: 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어, 2024-11-03, https://www.korea.kr/news/policyNewsView.do?newsId=148935814, 접근일 2026-10-11 (원문 미열람)
[^ref-789]: ISO, ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 미확인, https://www.iso.org/standard/88615.html, 접근일 2026-10-11 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s7.md

```markdown
---
title: "48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1255, ref-1522, ref-1523, ref-1524, ref-470, ref-561, ref-789]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#7
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스

# 48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준은 대부분 발행 기관 소개·발표 자료 기준이며 본문은 열람하지 않았다(각주의 원문 미열람 표시). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준은 대부분 발행 기관 소개·발표 자료 기준이며 본문은 열람하지 않았다(각주의 원문 미열람 표시). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.


### 2026-10-11 정정과 보강

아래는 분리 주제 페이지의 일부 표현을 이 실행에서 정정·보강한 내용이다. 분리 주제 페이지 본문은 이번에 고치지 않았다.

- **ANSI/A3 R15.08-3**: 주제 페이지는 R15.08-2 를 설명하며 사용자 요구를 '예정된' Part 3 이 맡는다고 적었으나, A3 판매 페이지는 Part 3(Use of IMR Applications)의 발행일을 2026-04-23 으로 표시한다(이번 재열람은 실패했고 2026-10-09 열람 기록 기준이다). [추정][^ref-1255]
- **ISO 3691-4 차기판**: 2020 판이 제1판, 2023 판이 제2판이므로 주제 페이지의 '차기판(제2판 초안)'은 '차기판(제3판)'으로 쓰는 것이 정합적으로 보인다. [추정][^ref-470][^ref-789] 차기판의 개발 단계는 출처가 엇갈린다. 위키 참고문헌은 2026-09-26 이 프로젝트를 'ISO/CD 3691-4'로 기록했다. [추정][^ref-789] 외부 조사 메모는 ISO/DIS 3691-4(제3판)가 2026-09-10 단계 40.60(DIS 투표 종료, 발행이나 최종안 완료가 아님)에 있다고 적었으나, ISO 페이지를 열지 못해 확인하지 못했다. [추정][^ref-789] 어느 쪽인지는 11절의 출처 충돌 질문으로 넘긴다.
- **ISO 12100 개정**: 외부 조사 메모는 개정 프로젝트 ISO/DIS 12100.3 이 2026-09-15 단계 40.60 에 있다고 적었으나 확인하지 못했다. [추정][^ref-1522]
- **KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항**: 국가표준 목록에서 발행일 2024-11-01, 국가기술표준원 고시 제2024-0480호로 제정된 61쪽 표준이며, 모바일 로봇과 협동로봇이 결합된 로봇에 적용할 표준·인증이 없다는 것을 고시 사유로 든다. [사실][^ref-1523] 목록의 적용범위는 통합 제조 시스템(IMS), 관제 시스템, 군집 관리 시스템, 기타 기계 설비류를 다루지 않는다고 적는다. [사실][^ref-1523] 국제표준 부합화 칸은 비어 있고, 인용표준으로 KS B ISO 10218-1·KS B ISO 10218-2·KS B ISO 3691-4·KS B ISO 12100·KS B ISO 13849-1 을 든다(목록 기준, 본문 미열람). [사실][^ref-1523] 중소벤처기업부가 2024-11-03 발표한 이동식 협동로봇 안전기준 KS 는 발행일과 고시 사유가 일치해 KS B 7327 로 보이나, 발표문에 번호가 없어 동일성은 추정이다. [추정][^ref-1523][^ref-561] 이 표준은 [모바일 매니퓰레이터](../../glossary/mobile-manipulator.md) 응용의 안전 요구를 다루므로 R15.08-2 유형 C 통합 요구에 대응하는 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성이나 플릿 통합 전체를 포괄하는지는 확인되지 않는다. [추정][^ref-1523]
- **KS B ISO 3691-4**: 국가표준 목록 기준(검증 미재확인)으로 2026-09-14 개정(고시 제2026-0288호)됐고 국제표준 부합화를 ISO 3691-4:2023(IDT)로 표시하며 81쪽, 구판은 2021-11-30 판이다. 이 국내 판은 ISO 에서 개발 중인 차기판과 구별된다. [추정][^ref-1524]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1255]: A3(Association for Advancing Automation), ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications, 2026-04-23, https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download, 접근일 2026-10-11 (원문 미열람)
[^ref-1522]: ISO, ISO/DIS 12100.3 - Safety of machinery — General principles for design — Risk assessment and risk reduction, 미확인, https://www.iso.org/standard/88578.html, 접근일 2026-10-11 (원문 미열람)
[^ref-1523]: 한국표준협회 KSSN(국가기술표준원 고시), KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항, 2024-11-01, https://www.kssn.net/search/stddetail.do?itemNo=K001010149365, 접근일 2026-10-11
[^ref-1524]: 한국표준협회 KSSN(국가기술표준원 고시), KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템, 2026-09-14, https://www.kssn.net/search/stddetail.do?itemNo=K001010158178, 접근일 2026-10-11
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-10-11 (원문 미열람)
[^ref-561]: 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어, 2024-11-03, https://www.korea.kr/news/policyNewsView.do?newsId=148935814, 접근일 2026-10-11 (원문 미열람)
[^ref-789]: ISO, ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 미확인, https://www.iso.org/standard/88615.html, 접근일 2026-10-11 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s8.md

```markdown
---
title: "48. 안전·위험 관리 — 대표 연구와 자료"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1521, ref-417, ref-563, ref-564]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#8
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 대표 연구와 자료

# 48. 안전·위험 관리 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Bensaci, C.·Zennir, Y.·Pomorski, D., A Comparative Study of STPA Hierarchical Structures in Risk Analysis(2018) — 다중 이동 로봇 시스템의 제어 구조별 위험 시나리오를 STPA 로 비교했다. 대상은 화학 분석 실험실의 다중 로봇이며 물류 현장이 아니다. [사실][^ref-564]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Bensaci, C.·Zennir, Y.·Pomorski, D., A Comparative Study of STPA Hierarchical Structures in Risk Analysis(2018) — 다중 이동 로봇 시스템의 제어 구조별 위험 시나리오를 STPA 로 비교했다. 대상은 화학 분석 실험실의 다중 로봇이며 물류 현장이 아니다. [사실][^ref-564]


### 2026-10-11 보강

- Bensaci, C. 외, STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison(Alexandria Engineering Journal, 2020-10) — 초록 기준으로 다중 로봇 시스템의 서로 다른 계층형 조정 구조에 대해 STPA 로 위험 시나리오와 요인을 도출한 뒤 Bowtie 로 평가하고 위험을 분류해 제어 구조 비교에 쓴다. [사실][^ref-1521] 분석 대상은 2018년 연구처럼 화학 분석실에서 화학제품을 나르는 다중 로봇으로 보이나, 본문을 열지 못해 로봇 대수와 사례 조건은 확인하지 못했다. [추정][^ref-1521]
- Belzile, B. 외(2025-02)의 사례 조건 — 위험성평가 사례는 캐나다 몬트리올의 건설사 Pomerleau 건설 현장에 Clearpath Jackal 을 배치하려는 상황(단일 로봇, 현장 유형 기타)을 대상으로 한다. [사실][^ref-563] 사례의 잔류 위험지수는 실험으로 측정한 값이 아니라 제안한 완화 대책을 적용한다고 보고 다시 추정한 값이다. [사실][^ref-563]
- Obi 외, SafeGate(2026-04)의 평가 층위 — 앞서 위키에 실린 합성 작업 벤치마크는 실행 전 단계 1~3(위험 분석·결합·결정 게이트)을 평가하고, AI2-THOR 시나리오는 시뮬레이션 실행을 평가하며, 실물 로봇 실험은 단계 4~6(계약 컴파일·정적 계획 검증·실행 중 감시) 시험과 전체 SafeGate 구조 실행을 다루되 결과를 정량 지표 없이 정성적으로만 보고한다. [사실][^ref-417] 충돌률 식의 분모는 실행된 작업 수인데, 논문은 30개 시나리오를 모두 차단한 경우의 충돌률을 0% 로 보고해 실행 0건일 때의 산정 규칙을 밝히지 않는다. [사실][^ref-417] 표 II 의 혼동행렬 합계는 183건(TP 100, FN 0, FP 6, TN 77)으로 전체 230개 벤치마크와 47건 차이가 난다. [사실][^ref-417] 이 차이는 결정 게이트가 판단을 미룬 작업을 혼동행렬에서 뺀 결과로 보이나 논문이 이를 명시하지 않아 확정할 수 없다. [추정][^ref-417] 구축자 의견: 실행 전 차단과 실행 결과를 함께 보고하는 평가에서는 위험 작업 차단률과 실제 실행된 작업의 안전 결과를 서로 다른 분모로 공개하고, 실행되지 않은 작업을 안전하게 실행된 작업으로 세지 않아야 한다. [의견][^ref-417]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1521]: Bensaci, C., Zennir, Y., Pomorski, D., Innal, F., Liu, Y., Tolba, C. (Alexandria Engineering Journal), STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison, 2020-10, https://doi.org/10.1016/j.aej.2020.06.036, 접근일 2026-10-11
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-11
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-10-11
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s6.md

```markdown
---
title: "48. 안전·위험 관리 — 대표 접근법과 기술"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1077, ref-1520, ref-1525, ref-1527, ref-1530, ref-417, ref-566]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#6
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 대표 접근법과 기술

# 48. 안전·위험 관리 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 안전을 다루는 접근은 위험을 찾는 방법, 운영 중 안전 상태를 주고받는 방법, 실행 전에 명령을 거르는 방법으로 나뉜다. [추정][^ref-566][^ref-031][^ref-417]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

안전을 다루는 접근은 위험을 찾는 방법, 운영 중 안전 상태를 주고받는 방법, 실행 전에 명령을 거르는 방법으로 나뉜다. [추정][^ref-566][^ref-031][^ref-417]


### STPA 분석 산출물

[STPA](../../glossary/stpa.md) Handbook(2018-03)은 분석을 분석 목적 정의, 제어 구조 모델링, 위험한 제어 행동(Unsafe Control Action) 식별, 손실 시나리오 식별의 네 단계로 제시한다(항공기 예시 중심의 방법론 안내서이며 로봇 플릿 실증 결과가 아니다). [사실][^ref-1520] 위험한 제어 행동은 제어 행동을 제공하지 않음, 위험하게 제공함, 너무 이르거나 늦게 또는 순서가 틀리게 제공함, 지속 제어를 너무 일찍 멈추거나 너무 오래 끎의 네 유형으로 나눠 찾는다. [사실][^ref-1520]

구축자 의견: 이 절차를 여러 제조사 로봇이 섞인 플릿에 쓰려면 제어 구조에 ROP·어댑터·로봇·설비·현장 운영자를 넣고, 정지 명령 누락뿐 아니라 잘못된 재개, 늦은 정지, 오래된 상태에 근거한 재배정을 위험한 제어 행동으로 등록해 손실 → 위험 → 제어 행동 → 안전 제약 → 시험으로 이어지는 연결표를 두는 방식이 필요해 보인다. [의견][^ref-1520]

### 현장 근로자 참여 기록

고용노동부 「위험성평가 근로자 참여 가이드」(2024-12)는 수급업체 근로자를 대상으로 청취조사를 해 아차사고 경험과 개선 의견을 모으는 방법을 제시한다(참여 방법 사례 모음이며 사고 감소 효과를 검증한 자료는 아니다). [사실][^ref-1527] 같은 가이드는 일용근로자 사례로 문자와 QR코드를 써서 익명으로 위험 요인을 제안받는 방식을 소개한다. [사실][^ref-1527] 아차사고 확인은 지침 제15조제4항이 상시적 위험성평가의 이행 수단으로 드는 항목 가운데 하나다. [사실][^ref-1525] 가이드와 지침은 같은 기관 자료라 서로 독립된 교차 확인은 아니다.

### 감시와 대응의 구분

Perez 외(2022-09)는 요구사항에서 ROS 2 실행 시간 감시기를 생성하는 방법을 제시하면서, 위반 처리 방법까지 지정하게 하는 DeRoS 와 달리 자기 방식은 위반의 탐지와 보고로 한정된다고 관련 연구 절에서 밝힌다. [사실][^ref-1530] 구축자 의견: 앞서 위키가 확인한 Nav2 Collision Monitor 의 하드 실시간 안전 인증 미제공과 이 한계를 함께 보면, ROP 위험등록부에는 탐지 주체, 대응 결정자, 실제 정지 장치, 허용 지연, 감시 자체가 고장 났을 때의 대응을 따로 적어야 한다(두 자료는 별개 구현이며 서로를 입증하지 않는다). [의견][^ref-1077][^ref-1530]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1077]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-10-11
[^ref-1520]: Leveson, N. G., Thomas, J. P. (MIT Partnership for Systems Approaches to Safety and Security), STPA Handbook, 2018-03, https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf, 접근일 2026-10-11
[^ref-1525]: 고용노동부(국가법령정보센터), 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호), 2024-12-18, https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202, 접근일 2026-10-11
[^ref-1527]: 고용노동부, 위험성평가 근로자 참여 가이드, 2024-12, https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20241202175, 접근일 2026-10-11
[^ref-1530]: Perez, I., Mavridou, A., Pressburger, T., Will, A., Martin, P. J. (EPTCS 371), Monitoring ROS2: from Requirements to Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.14030, 접근일 2026-10-11
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-11
[^ref-566]: CEN (iTeh Standards 카탈로그), EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction, 2010, https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s3.md

```markdown
---
title: "48. 안전·위험 관리 — 왜 중요한가"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1525, ref-1526, ref-470, ref-472, ref-560, ref-564]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#3
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 왜 중요한가

# 48. 안전·위험 관리 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08 Part 1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025)을 나누어 다루고, STPA 연구는 개별적으로 정상인 구성요소 사이의 상호작용에서 위험을 찾는다. 그래서 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. [추정][^ref-470][^ref-472][^ref-560][^ref-564]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08 Part 1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025)을 나누어 다루고, STPA 연구는 개별적으로 정상인 구성요소 사이의 상호작용에서 위험을 찾는다. 그래서 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. [추정][^ref-470][^ref-472][^ref-560][^ref-564]


### 국내 위험성평가 지침이 정한 실시 주체와 변경 조건

현행 「사업장 위험성평가에 관한 지침」(고용노동부고시 제2024-76호, 2024-12-18 일부개정, 2025-01-02 시행)은 작업의 일부나 전부를 도급하는 사업에서 도급사업주와 수급사업주가 각각 위험성평가를 하도록 한다(제5조제2항). [사실][^ref-1525] 같은 지침은 위험성 수준 판단 기준 마련, 유해·위험요인 파악, 허용 가능 여부 결정, 감소대책 수립·실행, 감소대책 실행 여부 확인의 다섯 경우에 해당 작업 근로자를 참여시키도록 한다(제6조). [사실][^ref-1525]

지침은 건설물 설치·변경, 기계·기구·설비의 신규 도입이나 변경, 정비·보수, 작업방법·절차의 신규 도입이나 변경, 재해 발생 등으로 추가 유해·위험요인이 생기면 수시 위험성평가를 하게 하며, 소프트웨어 버전 변경을 자동으로 수시평가 대상으로 정한 문구는 없다(제15조제2항). [사실][^ref-1525] 매월 1회 이상 근로자 제안제도·아차사고 확인·사업장 순회점검 등으로 상시적 위험성평가를 이행하면 수시평가와 정기평가를 실시한 것으로 본다(제15조제4항). [사실][^ref-1525]

고용노동부는 2026-09-23 이 지침의 전부개정고시(안)을 행정예고했으며, 이는 예고안이고 최종 고시·시행이 아니다. [사실][^ref-1526] 이 행정예고는 고용노동부 공고 제2026-461호이며, 의견 제출 마감일(2026-10-13)은 확인하지 못했다. [추정][^ref-1526]

이 지침은 현장 사업주의 법적 의무를 정한 것이며, 여러 사업자 사이의 책임 배분은 [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), 법령 해석은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)에서 다룬다. ROP 쪽 경계는 9절에 적었다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1525]: 고용노동부(국가법령정보센터), 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호), 2024-12-18, https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202, 접근일 2026-10-11
[^ref-1526]: 고용노동부(산재예방지원과), 사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고, 2026-09-23, https://moel.go.kr/info/lawinfo/lawmaking/view.do?bbs_seq=20260900747, 접근일 2026-10-11
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-10-11 (원문 미열람)
[^ref-472]: Association for Advancing Automation (A3), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s4.md

```markdown
---
title: "48. 안전·위험 관리 — 핵심 개념과 용어"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-470, ref-560, ref-564, ref-566]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#4
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 핵심 개념과 용어

# 48. 안전·위험 관리 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **위험성평가(Risk Assessment)** — ISO 12100:2010 이 기계 설계의 일반 원칙으로 정하는, 위험원을 찾고 위험을 평가해 위험 감소 필요성을 판단하는 절차다. [사실][^ref-566]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **위험성평가(Risk Assessment)** — ISO 12100:2010 이 기계 설계의 일반 원칙으로 정하는, 위험원을 찾고 위험을 평가해 위험 감소 필요성을 판단하는 절차다. [사실][^ref-566]
- **3단계 위험 감소 방법(Three-Step Method)** — 본질적 안전 설계 → 방호·보완 보호 조치 → [사용 정보](../../glossary/information-for-use.md)의 순서로, 앞 단계를 다한 뒤 다음 단계로 간다. [사실][^ref-566]
- **운용 구역(Operating Zone)** — ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. [사실][^ref-470] 로봇의 제어 상태를 뜻하는 [운용 모드](../../glossary/operating-mode.md)와는 다른 개념이다.
- **안전 상태 보고(safetyState)** — [VDA 5050](../../glossary/vda-5050.md) 3.0.0 상태 메시지가 비상정지 상태와 보호 필드 침범 여부(fieldViolation)를 알리는 항목이다. [추정][^ref-031]
- **[협동 적용](../../glossary/collaborative-application.md)(Collaborative Application)** — ISO 10218-2:2025 는 종전 ISO/TS 15066 의 협동 적용 요구를 본문에 통합했다. [사실][^ref-560]
- **시스템 이론적 프로세스 분석(System-Theoretic Process Analysis, STPA)** — 제어 구조를 기준으로 위험 시나리오와 원인 요인을 도출하는 위험 분석 기법으로, 다중 이동 로봇 시스템에도 적용됐다. [사실][^ref-564]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-10-11 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)
[^ref-566]: CEN (iTeh Standards 카탈로그), EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction, 2010, https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-10-11-04/pages/topics/2026/2026-10-11-area48-s10.md

```markdown
---
title: "48. 안전·위험 관리 — 다른 연구영역과의 연결"
type: topic
category: "M. 안전"
primary_area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-004, ref-031, ref-417, ref-560]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-and-risk-management.md#10
---

[홈](../../index.md) › [주제](../index.md) › 48. 안전·위험 관리 — 다른 연구영역과의 연결

# 48. 안전·위험 관리 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — ISO 10218-2:2025 에 사이버보안 요구가 들어오면서 안전과 보안이 맞물리는 것으로 보인다. [추정][^ref-560]
- 이 페이지는 [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — ISO 10218-2:2025 에 사이버보안 요구가 들어오면서 안전과 보안이 맞물리는 것으로 보인다. [추정][^ref-560]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — LLM 명령의 실행 전 안전 판정(SafeGate)이 AI 결과를 실행에 쓰는 기준 문제와 이어지는 것으로 보인다. [추정][^ref-417]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 사람이 자연어로 내린 지시를 실행 전에 거르는 지점에서 맞물리는 것으로 보인다. [추정][^ref-417]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 교통 충돌 예방과 긴급 작업의 우선 협상에서 맞물리는 것으로 보인다. [추정][^ref-004]
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 정지·재개 지시를 확실하게 전달하는 문제에서 맞물리는 것으로 보인다. [추정][^ref-031]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 펌웨어·정책 변경 뒤 안전 재평가가 필요한지의 문제로 이어진다. 관련 질문은 11절의 oq-092·oq-093 이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-and-risk-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)
- 관련 영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-and-risk-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-11
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-04 | 48. 안전·위험 관리 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 12건 / 전체 1454건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | https://arxiv.org/abs/2604.05427 | 2026-09-25 | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 2026-09-25 | 아니오 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 2026-09-25 | 아니오 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 2026-09-25 | 아니오 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 2026-09-25 | 아니오 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | https://arxiv.org/abs/2502.20693 | 2026-09-25 | 아니오 |
| ref-564 | Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회) | 2018-12 | https://ieeexplore.ieee.org/document/8910126/ | 2026-09-25 | 아니오 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 2026-09-25 | 아니오 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | https://github.com/open-rmf/rmf/issues/658 | 2026-09-25 | 아니오 |
| ref-783 | ISO | ISO/AWI 15066-1 - Collaborative Safety – Physical contact with robots — Part 1: Biomechanical thresholds and data | 미확인 | https://www.iso.org/standard/91522.html | 2026-09-26 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
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
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-element-proxy: 건물 요소 프록시 (Building Element Proxy (IfcBuildingElementProxy))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- buildingsmart-data-dictionary: buildingSMART 데이터 사전 (buildingSMART Data Dictionary (bSDD))
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
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
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
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
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
- domain-shift: 도메인 이동 (Domain Shift)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
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
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
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
- generalized-voronoi-graph: 일반화 보로노이 그래프 (Generalized Voronoi Graph (GVG))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- gln-extension-component: GLN 확장 성분 (GLN Extension Component)
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
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
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
- integrity-risk: 무결성 위험 (Integrity Risk)
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
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic-on-finite-traces: 유한 트레이스 선형 시간 논리 (Linear Temporal Logic on Finite Traces (LTLf))
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- makespan: 메이크스팬 (Makespan)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- original-instructions: 원본 설명서 (Original Instructions)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- phased-rollout: 단계적 배포 (Phased Rollout (Staged Rollout))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-attestation: 원격 증명 (Remote Attestation)
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
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
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
- shift-handover: 교대 인수인계 (Shift Handover)
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
- skos: 단순 지식 조직 체계 (Simple Knowledge Organization System (SKOS))
- slot-filling: 슬롯 채우기 (Slot Filling)
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
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
- state-script: 상태 스크립트 (State Script (Mender))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- task-dependency-graph: 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- trace-context: 추적 문맥 (Trace Context (W3C traceparent / tracestate))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-defined-property-set: 사용자 정의 속성 세트 (User-defined Property Set)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050-hibernation: 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-diagram: 워크플로 다이어그램 (Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안))
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [48] 에 걸린 21건 / 전체 380건)

```markdown
- oq-064 [열림] 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? (영역 30, 48)
- oq-070 [열림] 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? (영역 31, 48)
- oq-092 [열림] 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? (영역 48, 57)
- oq-093 [열림] EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (영역 48, 57)
- oq-095 [열림] ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? (영역 29, 48)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 21, 48)
- oq-097 [열림] 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? (영역 31, 48)
- oq-102 [열림] ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? (영역 48, 51)
- oq-103 [열림] EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? (영역 48, 51)
- oq-106 [열림] LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? (영역 47, 48)
- oq-123 [열림] ISO 10218-2:2025 발행 뒤 국내 KS B ISO 10218-2 와 KS B ISO/TS 15066 은 새 판으로 부합 개정되었거나 개정 예고되었는가, 국내 협동로봇 설치 작업장 안전인증은 어느 판을 기준으로 하는가? (관련 기존 질문: oq-070, oq-092) (영역 31, 48)
- oq-144 [열림] 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (영역 13, 52, 48)
- oq-172 [열림] 격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가? (영역 63, 48)
- oq-229 [열림] 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (영역 49, 48)
- oq-253 [열림] 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? (영역 50, 48)
- oq-282 [열림] 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? (영역 58, 59, 48)
- oq-302 [열림] RoboGuard 처럼 안전 규칙을 시간 논리 제약으로 바꿔 언어 모델 계획을 고치는 안전 가드레일을 다중 로봇 오케스트레이션의 승인 전 검사에 두면 사람 승인 부담을 얼마나 줄일 수 있으며, 가드레일이 계획을 수정했을 때 무엇을 사람에게 다시 승인받아야 하는가? (영역 12, 48, 13)
- oq-307 [열림] 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? (영역 48, 34, 19)
- oq-310 [열림] 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? (영역 48, 42, 29)
- oq-312 [열림] 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? (영역 48, 38, 54)
- oq-314 [열림] RoboGuard 같은 언어 모델 로봇용 안전 가드레일을 다중 로봇 플릿의 배정·경로·구역 계획에 적용해 위험 계획 차단율을 측정한 연구나 제품이 있는가? (영역 44, 48, 13)
```
