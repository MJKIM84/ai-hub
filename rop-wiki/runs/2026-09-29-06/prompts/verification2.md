(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-06
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 13. 대화형 기능의 신뢰·기반 (C. 채팅 기반 구성·운영)
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

### runs/2026-09-29-06/target.json

```json
{
  "run_id": "2026-09-29-06",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 98,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 13,
    "area_name": "13. 대화형 기능의 신뢰·기반",
    "category": "C. 채팅 기반 구성·운영",
    "category_letter": "C"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=13"
}
```

### runs/2026-09-29-06/research.json

```json
{
  "run_id": "2026-09-29-06",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 13,
    "area_name": "13. 대화형 기능의 신뢰·기반",
    "category": "C. 채팅 기반 구성·운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 프롬프트 주입·탈옥·승인 피로·모델 대체 용어 없음(환각·과도한 에이전시·사람 참여 루프·모델 컨텍스트 프로토콜·구조화 출력·제약 디코딩·등각 예측·불확실도 정렬·자동화 편향·역할 기반 접근 통제·감사 추적·pass^k·사용자 시뮬레이터는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 오해석 방지·권한·모델 연결·평가·화면 연동·음성 여섯 갈래 모두 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — OWASP LLM Top 10, MCP 보안 원칙, EU AI Act 기록 조항, 국내 안내서(TTA·개인정보위) 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 8~12번 채팅 영역, 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 6건(oq-125, oq-127, oq-133, oq-136, oq-139, oq-141) 미반영",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]",
    "언어 모델이 없는 물품·장소를 지어내거나 외부 입력(프롬프트 주입·탈옥)에 조종당해 로봇 동작으로 이어지는 위협은 무엇이 보고되었고, 근거 표시·불확실도 보정·사전 검증 같은 방어는 어떤 것이 있는가? (섹션 3·4·6 겨냥)",
    "사용자별로 대화로 지시할 수 있는 로봇·구역·작업 범위를 제한하고 승인 관문을 두는 권한 설계와 승인 부담(승인 피로)은 어떻게 다뤄지는가? (섹션 6·11 겨냥, oq-139·oq-141 관련)",
    "대화 기록의 보존·보호와 자동 로그에 관한 규제·안내서(EU AI Act, 국내 개인정보위·TTA 안내서)는 무엇을 요구하는가? (섹션 7·9 겨냥)",
    "언어 모델 공급자를 고르고 바꾸며 장애 때 임의 대체를 막으려면 무엇을 알아야 하는가(게이트웨이의 모델 대체·희석)? (섹션 6·11 겨냥)",
    "대화형 기능의 해석·분해 정확도, 질문 횟수, 신뢰성(반복 시행)을 재는 공개 벤치마크·지표는 무엇인가? (섹션 6·8 겨냥, oq-125·oq-127 관련)",
    "음성·다국어·현장 단말 대화와 화면 선택–대화 연동을 다룬 연구·현장 사례(현장 유형 명시)와 국내 자료는 무엇이며, ROP가 직접 맡을 것과 음성 인식·모델 공급자에 맡길 것의 경계는 어디인가? (섹션 5·9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리하고, 과도한 에이전시를 언어 모델 기반 시스템에 필요 이상의 기능·권한·자율이 주어진 상태로 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-855"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목록 페이지의 LLM06:2025 Excessive Agency 항목: \"An LLM-based system is often granted a degree of agency\" 이고, LLM01 Prompt Injection 은 사용자 프롬프트가 의도치 않은 방식으로 모델 행동을 바꾸는 위험으로 적혀 있다.",
      "as_of": "2025",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "모델 컨텍스트 프로토콜(MCP) 명세 2025-06-18 판의 '보안과 신뢰·안전' 절은 호스트가 어떤 도구든 호출하기 전에 사용자의 명시적 동의를 얻어야 하고, 도구 설명·주석은 신뢰할 수 있는 서버에서 온 것이 아니면 신뢰하지 말아야 하며, 프로토콜 자체는 이 원칙을 강제할 수 없으므로 구현자가 동의·인가 흐름을 응용 프로그램에 만들어야 한다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-856"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Tool Safety 항목: \"Hosts must obtain explicit user consent before invoking any tool\". 구현 지침은 MCP 가 프로토콜 수준에서 보안 원칙을 강제할 수 없으므로 구현자가 견고한 동의·인가 흐름을 만들어야(SHOULD) 한다고 적는다.",
      "as_of": "2025-06-18",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f3",
      "claim": "Robey 외(2024)의 RoboPAIR 는 언어 모델로 제어되는 로봇을 탈옥시키는 알고리즘으로, 자율주행 언어 모델(화이트박스)·GPT-4o 계획기를 단 Clearpath Jackal(그레이박스)·Unitree Go2 로봇 개(블랙박스)의 세 설정에서 100% 공격 성공률을 보고했고, 배치된 상용 로봇 시스템에 대한 첫 탈옥 성공이라고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"jailbroken robots could cause physical damage in the real world\". 세 설정 모두에서 100% attack success rate 를 보고하고, Unitree Go2 사례를 배치된 상용 로봇 시스템의 첫 탈옥으로 적었다(2024-10-17 제출, 2024-11-09 개정).",
      "as_of": "2024-11-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "Huang 외(2025)의 서베이 '언어 모델 제어 로봇의 신뢰'는 추상 추론과 물리 동작 사이의 체화 격차(embodiment gap)를 중심으로 탈옥·백도어·다중 모달 프롬프트 주입을 포함한 공격 벡터 분류와, 형식 안전 명세·런타임 강제·다중 언어 모델 감독·프롬프트 강화를 포함한 방어 분류, 그리고 강건성 평가용 데이터셋·벤치마크를 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-859"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록은 \"a comprehensive taxonomy of attack vectors\"(탈옥·백도어·다중 모달 프롬프트 주입)와 방어(형식 안전 명세와 런타임 강제부터 다중 LLM 감독·프롬프트 강화까지)를 다룬다고 적는다(2025-12-17 제출).",
      "as_of": "2025-12-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 언어 모델에 대한 프롬프트 주입·탈옥이 도구 호출이나 로봇의 물리 동작으로 이어지는 위협을 각각 보고해, 언어 모델의 오해석뿐 아니라 외부 조작이 잘못된 실행의 원인이 된다는 점이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-855",
        "ref-857",
        "ref-859"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "OWASP 는 프롬프트 주입·과도한 에이전시를 위험 목록에 두고, RoboPAIR 는 실제 로봇에서 탈옥으로 유해 동작을 끌어냈으며, Huang 외 서베이는 공격·방어 분류를 정리한다. 세 출처는 발행 기관이 다르다.",
      "as_of": "2025-12-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "MCP 가 도구 호출 전 사용자 동의를 호스트의 책임으로 두고 프로토콜이 강제하지 못한다는 점(f2)과 탈옥이 배치된 로봇에서도 성공한다는 점(f3·f5)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이나 도구 서버 안이 아니라 ROP 쪽 호스트에 승인 관문을 두고, 도구 설명·검색 문서·현장 입력을 신뢰하지 않는 입력으로 다루어야 지켜질 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-856",
        "ref-857",
        "ref-855"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2 의 '호스트가 명시적 동의를 얻어야 한다'와 f3 의 100% 탈옥 성공, f1 의 과도한 에이전시 정의를 결합한 추정이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f7",
      "claim": "VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리로 옮긴 뒤 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 검증 모듈로, 승인 전에 계획을 자동으로 거르는 층의 사례다.",
      "tag": "사실",
      "source_ids": [
        "ref-753"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실행 전 계획 검증(pre-execution task plan verification) 모듈로 가정 작업 데이터셋에서 시험하고 코드를 공개했다 (재인용: 2026-09-29-05)",
      "as_of": "2025-07-07",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "Li 외(NeurIPS 2024 데이터셋·벤치마크 트랙, 구두 발표)의 Embodied Agent Interface 는 체화 의사결정 과제를 목표 해석·하위 목표 분해·행동 순서화·전이 모델링의 네 모듈로 나누고, 최종 성공률 대신 환각 오류·어포던스 오류·여러 계획 오류를 구분하는 세분화 지표로 언어 모델을 평가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-858"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 지표가 \"hallucination errors, affordance errors, various types of planning errors\" 를 구분한다. 네 모듈은 goal interpretation, subgoal decomposition, action sequencing, transition modeling(2024-10-09 제출, 2025-01-19 개정).",
      "as_of": "2025-01-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Yao 외(2024)의 τ-bench 는 언어 모델이 흉내 내는 사용자와 도구·정책 지침을 가진 에이전트의 대화를 시뮬레이션해 대화 종료 시 데이터베이스 상태를 목표 상태와 비교하고, 같은 과제를 여러 번 시행해 모두 성공할 확률 pass^k 로 신뢰성을 재며, GPT-4o 같은 최신 함수 호출 에이전트도 과제 성공률 50% 미만·소매 도메인 pass^8 25% 미만이라고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-738"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 평가는 \"the database state at the end of a conversation with the annotated goal state\" 비교이며, gpt-4o 가 과제의 50% 미만에 성공하고 소매 도메인 pass^8 이 25% 미만이라고 적는다(2024-06-17 제출).",
      "as_of": "2024-06-17",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "KnowNo(Ren 외, CoRL 2023)는 등각 예측으로 언어 모델 계획기의 불확실도를 보정해 후보 행동 집합이 하나로 좁혀지면 실행하고 여러 개가 남으면 사람에게 되묻는 틀로, 목표 성공률을 보장하면서 도움 요청을 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "불확실도 정렬(uncertainty alignment)로 예측 집합 크기에 따라 자율 실행과 되묻기를 가른다 (재인용: 2026-09-29-04)",
      "as_of": "2023-09-04",
      "site_type": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Mullen·Manocha(2024, 2025 개정)의 LBAP 는 베이즈 추론으로 장면 근거(scene grounding)와 세계 지식을 함께 반영해 로봇의 확신도를 보정함으로써 언어 모델 환각에 대응하며, 실제 환경 시험에서 성공률 70% 조건에서 이전 방법보다 사람 도움 요청률을 33% 넘게 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-864"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"decreases the human help rate of previous methods by over 33% at a success rate of 70%\". 방법은 장면 근거와 세계 지식을 모두 고려해 확신도를 보정한다(2024-03-19 제출, 2025-06-17 개정).",
      "as_of": "2025-06-17",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, '불확실도 보정 기반 되묻기'로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-351",
        "ref-864"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "KnowNo 는 등각 예측, LBAP 는 베이즈 추론과 장면 근거로 확신도를 보정하고 둘 다 도움 요청률을 성공률과 함께 보고한다. 두 연구는 소속 기관이 다르다.",
      "as_of": "2025-06-17",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f13",
      "claim": "세분화 오류 지표(f8), 반복 시행 신뢰성 pass^k(f9), 성공률 대비 도움 요청률(f10·f11)을 함께 보면, 이 영역의 '대화형 기능 평가'는 해석·분해 정확도를 오류 유형별로 나누고 같은 과제를 여러 번 시행한 신뢰성과 질문 횟수를 성공률과 짝지어 재는 방식으로 구성할 수 있으나, 로봇 지도 작성·로봇 구성 대화에 특화된 벤치마크는 이번 조사에서 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-858",
        "ref-738",
        "ref-864"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8·f9·f11 의 지표를 조합한 추정이며 oq-125·oq-127 이 묻는 특화 벤치마크의 부재는 검색 범위 안의 판단이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Laban 외(2025)는 20만 건 이상의 시뮬레이션 대화에서 언어 모델의 다중 턴 성능이 단일 턴보다 평균 39% 낮았고 원인이 초기 가정에 대한 과도한 의존 같은 신뢰성 저하라고 보고해, 대화가 길어질수록 오해석 위험이 커진다는 근거가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-840"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "여섯 생성 과제에서 다중 턴 성능이 평균 39% 낮았고 능력 저하보다 신뢰성 저하가 원인이라고 적었다 (재인용: 2026-09-29-04)",
      "as_of": "2025-05-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "Michael·Roesner(2026)는 AI 에이전트의 사용자 수준 권한 제안 21건과 상용 에이전트 5종을 조사해 권한 정책 명세(자연어·권한 라벨·고정 선택지·구조화 제약·임의 규칙)와 강제 방식(에이전트 자율 준수·언어 모델 가드레일·결정적 위반 탐지·실시간 사용자 승인·형식 검증 강제)의 분류를 만들고, 상용 에이전트가 부담이 큰 실시간 승인과 투명성 없는 언어 모델 자동 검토 사이의 선택을 강요하며 낮은 사용자 부담·형식 근거·결정적 강제를 함께 갖춘 학술 시스템은 21건 중 하나도 없다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-868"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: \"Commercial agents often force users to choose between high-overhead user-in-the-loop permissions enforcement, and LLM auto-reviewers with little transparency or user control.\" 분석 대상은 Claude·Claude Cowork·ChatGPT 채팅·ChatGPT 에이전트 모드·Codex(2026-07-20 개정).",
      "as_of": "2026-07-20",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "Li 외(2025)의 다중 로봇 언어 모델 서베이는 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머물고 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다고 지적해, 승인 관문의 검토 부담이 열린 문제임을 뒷받침한다.",
      "tag": "사실",
      "source_ids": [
        "ref-165"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "사람 개입 절이 실행 전 승인·도움 요청·사람 검증 방식을 정리하면서 운영자 인지 부담 미정량화를 빈틈으로 적었다 (재인용: 2026-09-29-05)",
      "as_of": "2025-02-06",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "권한 강제 방식의 분류(f15)와 승인 부담 미정량화(f16), 호스트 책임의 동의 원칙(f2)을 함께 보면, 이 영역의 '대화 권한'은 프롬프트 안내가 아니라 도구 호출 수준에서 사용자·로봇·구역·작업 범위를 결정적으로 검사하는 정책으로 두고, 실행 전 승인은 위험도가 낮은 조회는 자동 허용하고 로봇을 움직이는 요청만 사람이 승인하는 식으로 단위를 나누어야 승인 피로를 줄일 수 있을 것으로 보이나, 로봇 대수·계획 크기에 따른 승인 단위를 정한 연구는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-868",
        "ref-165",
        "ref-856"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15 의 '결정적 강제'와 '실시간 승인의 높은 부담', f16 의 인지 부담 미정량화, f2 의 호스트 동의 원칙을 결합한 추정이며 oq-139 의 답은 아니다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "EU AI Act 제12조(기록 보관)는 고위험 AI 시스템이 수명 기간 내내 사건을 자동으로 기록(로그)할 수 있어야 하고, 로그가 위험 상황 식별·시장 출시 후 모니터링·운영 모니터링에 필요한 사건을 담아 의도된 목적에 맞는 추적 가능성을 보장해야 한다고 규정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-863"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제1항: \"High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.\" 제2항은 추적 가능성 수준에 맞는 사건 기록 요건을 둔다(유럽위원회 AI Act 서비스 데스크 게재, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f19",
      "claim": "개인정보보호위원회는 2025년 8월 '생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서'를 내어(공식 사이트 게시 2025-08-22) 생성형 AI 수명주기 각 단계에서 고려할 개인정보 처리·보호 이슈를 체계화하고 법적 기준과 안전조치를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-862"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "게시물: 생성형 AI 수명주기 각 단계의 개인정보 처리·보호 이슈를 체계화하고 법적 기준 및 안전조치를 제시한다고 적는다. 안내서 PDF 본문은 이번 실행에서 열지 못했다.",
      "as_of": "2025-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "과학기술정보통신부와 한국정보통신기술협회(TTA)의 '2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야'는 2024년 2월 발간되어 웹 문서로 2025-08-14까지 갱신되었고, 인공지능 서비스·제품 개발 과정의 기술적 신뢰성 확보 방안을 다루며 2024년에는 생성 AI 기반 서비스 분야 안내서가 함께 나왔다.",
      "tag": "사실",
      "source_ids": [
        "ref-860"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "일러두기: \"기술적 측면의 신뢰성 확보 방안을 다루고 있습니다\". 2023년 자율주행·의료·공공사회, 2024년 채용·스마트치안·생성 AI 기반 서비스 분야 안내서를 더했다고 적는다.",
      "as_of": "2025-08-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "대화 기록의 보존·보호 요구는 EU AI Act 의 자동 로그 조항(f18), 국내 개인정보위 안내서(f19), TTA 신뢰성 안내서(f20)에 근거를 둘 수 있으나, ROP 의 로봇 대화 기능이 고위험·고영향 AI 에 해당하는지와 로그 항목·보존 기간을 어떻게 정할지는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-863",
        "ref-862",
        "ref-860"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18~f20 을 이 영역의 '대화 기록 보존·보호' 요구에 대응시킨 추정이며, 적용 여부는 열린 질문으로 남긴다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f22",
      "claim": "Zhang·Zhang·Qin(2026)의 IRIS 는 언어 모델 게이트웨이가 광고한 모델 대신 더 싼 모델을 내보내는 모델 대체(substitution)와 일부 요청만 약속한 백엔드로 보내는 라우팅 희석(dilution)을 응답 텍스트만으로 감사하는 방법으로, 상용 라이브러리에서 희석을 평균 탐지력 0.85·오탐률 0.017 로 잡고 교차 제공자 감사에서 문제 모델 쌍 15개 중 14개를 표시했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-865"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"an audit that needs only the returned text\". 희석 탐지력 0.85(오탐 0.017), 희석 비율 오차 0.04 이내, 교차 제공자 14/15 (2026-07-23 제출).",
      "as_of": "2026-07-23",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f23",
      "claim": "게이트웨이의 무단 모델 대체·희석이 실제로 관측된다는 점(f22)과 OWASP 가 공급망을 위험 항목으로 둔 점(f1)을 함께 보면, 이 영역의 '모델 장애 때 임의로 다른 모델로 넘기지 않는다'는 요구는 ROP 가 요청·응답마다 실제 제공 모델 식별자를 기록하고 대체를 사전에 정한 정책으로만 허용하며 게이트웨이 계층의 대체를 감사하는 절차로 구현해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-865",
        "ref-855"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f22 의 대체·희석 관측과 f1 의 공급망 위험을 이 영역의 모델 연결·교체 요구에 대응시킨 추정이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f24",
      "claim": "Li 외(2026)의 서베이는 로봇 시스템의 음성 인식이 온라인 API 서비스에만 의존해야 하는지를 물으며 Whisper 같은 심층 학습 모델까지의 발전과 ROS 기반·클라우드 기반·혼합 배치 전략, 다양하고 동적인 환경에서 강건한 음성 인식을 배치하는 과제를 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-866"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록은 ROS-based, cloud-based, hybrid 배치 전략과 \"challenges of deploying robust speech recognition\" 를 다룬다고 적는다(2026-07-13 제출). 소음·다국어 수치는 초록에 없다.",
      "as_of": "2026-07-13",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f25",
      "claim": "Nandkumar·Peternel(Frontiers in Robotics and AI, 2025-04-29)은 네덜란드 슈퍼마켓의 상품 안내·회수 로봇을 위한 음성 대화 인터페이스에서 네 가지 음성 인식 기술을 영어·네덜란드어와 성별 집단(참가자 40명)으로 비교해 Whisper 가 가장 낮은 단어 오류율을 보였고, 질의 분류기와 상·중·하 세 층의 언어 모델이 1,612개 상품 데이터베이스에 근거해 답하게 한 다층 구조가 참가자 16명 평가에서 GPT-4 Turbo 보다 13개 항목 중 4개에서 유의하게 높았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: \"Whisper leads in speech recognition accuracy between genders and languages.\" 질의 분류기 정확도 약 87%(영어·네덜란드어), 모든 응답이 상품 DB 항목을 참조해 환각을 줄였다고 적는다.",
      "as_of": "2025-04-29",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f26",
      "claim": "van Dam(2025)의 다중 모달 GUI 아키텍처는 응용 프로그램의 화면 이동 그래프와 의미를 모델 컨텍스트 프로토콜로 노출하고 뷰모델이 현재 보이는 화면에 적용되는 도구와 전역 도구를 언어 모델에 제공해 음성 입력과 시각 인터페이스의 정렬과 양쪽 모달리티의 일관된 피드백을 목표로 하며, 참조 구현(langbar)을 공개하고 로컬 배치 가능한 개방 가중치 모델이 전체 정확도에서 선도 상용 모델에 근접한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-861"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"makes an application's navigation graph and semantics available through the Model Context Protocol (MCP)\". 목표는 음성 입력과 시각 인터페이스의 신뢰할 수 있는 정렬과 모달리티 간 일관된 피드백(2025-10-09 개정).",
      "as_of": "2025-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "화면 상태와 가능한 동작을 도구로 노출해 음성·대화와 화면을 맞추는 구조(f26)와 화면 선택을 대화에 반영하는 이 영역의 요구를 함께 보면, 지도에서 고른 장소·로봇을 대화가 참조하고 대화로 바꾼 값이 편집 화면에 바로 보이게 하려면 편집기의 현재 선택·화면 상태를 언어 모델에 자원으로 주고 변경은 같은 상태 저장소를 거치게 하는 구조가 필요할 것으로 보이나, 로봇 지도·시나리오 편집기에 특화된 공개 구현은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-861",
        "ref-856"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f26 의 GUI–MCP 구조와 f2 의 MCP 자원·도구 개념을 이 영역의 '대화와 화면 편집 연동' 요구에 대응시킨 추정이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "확인한 자료를 종합하면 13. 대화형 기능의 신뢰·기반에서 ROP가 직접 맡을 범위는 해석 결과에 근거(장소·물품·문서 식별자)를 붙이고 불확실한 항목만 되묻는 흐름, 도구 호출 수준의 권한 검사와 실행 전 승인 관문, 대화·도구 호출·실제 제공 모델의 기록, 모델 공급자 연결·교체 정책, 오류 유형별 평가 시나리오이며, 음성 인식 엔진의 정확도와 언어 모델 자체의 안전 정렬은 연계 대상으로 두는 것이 분류 원문 19장의 경계에 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-856",
        "ref-868",
        "ref-865",
        "ref-866",
        "ref-858"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f15·f22·f24·f8 을 원문 19장의 '로봇 자체 지능·제어'와 외부 도구 경계에 대응시킨 추정이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "연계 대상: 음성 인식 모델의 소음·다국어 강건성(Whisper 등)과 언어 모델 공급자의 탈옥 방어·안전 학습은 분류 원문 19장의 로봇 자체 지능 및 외부 도구 쪽이며, 이종 제조사를 잇는 ROP 는 인식 결과의 확인 절차와 모델 출력의 검증·승인·기록을 맡고 인식·모델 내부 성능은 공급자에게 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-866",
        "ref-869",
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f24 의 배치 전략, f25 의 음성 인식 비교, f3 의 모델 수준 탈옥을 경계 판단에 쓴 추정이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f30",
      "claim": "불확실도 보정·되묻기(KnowNo, LBAP), 세분화 벤치마크(Embodied Agent Interface), 탈옥 공격·방어(RoboPAIR, Huang 외)는 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 이 영역과 함께 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 영역, 권한·기록은 51. 인증·권한·격리와 52. 통신 보호·위협 관리·감사, 대화 기록의 개인정보는 53. 개인정보·영상 데이터, 평가는 54. 시험·형식 검증·벤치마크에 연결해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-858",
        "ref-857",
        "ref-863"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "finding 의 주제를 분류 원문의 대분류·세부영역과 교차 규칙에 대응시킨 판단이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-855",
      "org": "OWASP GenAI Security Project",
      "title": "OWASP Top 10 for LLM Applications 2025",
      "published": "2025",
      "url": "https://genai.owasp.org/llm-top-10/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 응용 프로그램의 열 가지 위험 목록(프롬프트 주입, 민감 정보 노출, 공급망, 부적절한 출력 처리, 과도한 에이전시, 잘못된 정보 등)을 항목별 한 줄 설명과 함께 게시한 목록 페이지다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-856",
      "org": "Model Context Protocol (Anthropic 주도 오픈소스 프로젝트)",
      "title": "Specification — Model Context Protocol (2025-06-18)",
      "published": "2025-06-18",
      "url": "https://modelcontextprotocol.io/specification/2025-06-18",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "MCP 명세 개요 페이지. '보안과 신뢰·안전' 절에 사용자 동의·제어, 데이터 프라이버시, 도구 안전(도구 호출 전 명시적 동의, 도구 설명 불신), 샘플링 제어 원칙과 구현 지침을 둔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J.",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-11-09",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 제어 로봇을 탈옥시키는 RoboPAIR 를 제안하고 자율주행 언어 모델·Jackal UGV·Unitree Go2 의 세 설정에서 100% 공격 성공률과 유해 물리 동작을 보고한 프리프린트(2024-10-17 제출).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-858",
      "org": "Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks)",
      "title": "Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making",
      "published": "2025-01-19",
      "url": "https://arxiv.org/abs/2410.07166",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "체화 의사결정을 목표 해석·하위 목표 분해·행동 순서화·전이 모델링의 네 모듈로 나누고 환각·어포던스·계획 오류를 구분하는 세분화 지표로 언어 모델을 평가하는 벤치마크(2024-10-09 제출).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-859",
      "org": "Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R.",
      "title": "Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges",
      "published": "2025-12-17",
      "url": "https://arxiv.org/abs/2601.02377",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 제어 로봇의 체화 격차를 중심으로 탈옥·백도어·다중 모달 프롬프트 주입 등 공격 벡터 분류와 형식 안전 명세·런타임 강제·다중 언어 모델 감독·프롬프트 강화 등 방어, 평가 데이터셋·벤치마크를 정리한 서베이.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-860",
      "org": "과학기술정보통신부·한국정보통신기술협회(TTA)",
      "title": "2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기)",
      "published": "2024-02",
      "url": "https://tta-trustworthy-ai.gitbook.io/general",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "인공지능 서비스·제품 개발 과정의 기술적 신뢰성 확보 방안을 다루는 안내서의 웹 문서판. 2024년 2월 발간 뒤 2025-08-14까지 갱신되었고, 2024년 생성 AI 기반 서비스 분야 안내서가 추가되었다고 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-861",
      "org": "van Dam, H. G. W.",
      "title": "A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants",
      "published": "2025-10-09",
      "url": "https://arxiv.org/abs/2510.06223",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "응용 프로그램의 화면 이동 그래프와 의미를 MCP 로 노출해 음성 대화 비서와 GUI 를 맞추는 아키텍처를 제안하고 참조 구현(langbar)과 개방 가중치 모델 평가를 담은 프리프린트(2025-08-31 제출).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-862",
      "org": "개인정보보호위원회",
      "title": "생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.)",
      "published": "2025-08",
      "url": "https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "개인정보보호위원회 공식 사이트 게시물(2025-08-22). 생성형 AI 수명주기 단계별 개인정보 처리·보호 이슈와 법적 기준·안전조치를 제시하는 안내서의 PDF 배포 안내이며, PDF 본문은 이번 실행에서 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-863",
      "org": "European Commission — AI Act Service Desk",
      "title": "Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act)",
      "published": null,
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "유럽위원회 서비스 데스크가 게재한 AI Act 제12조 조문. 고위험 AI 시스템의 수명 기간 자동 사건 기록(로그)과 추적 가능성 요건, 원격 생체 식별 시스템의 최소 로그 항목을 규정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-864",
      "org": "Mullen, J. F., Jr., & Manocha, D.",
      "title": "Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners",
      "published": "2025-06-17",
      "url": "https://arxiv.org/abs/2403.13198",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "장면 근거와 세계 지식을 베이즈 추론으로 결합해 언어 모델 계획기의 확신도를 보정하는 LBAP 를 제안하고 성공률 70%에서 사람 도움 요청률을 33% 넘게 줄였다고 보고한 프리프린트(2024-03-19 제출).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-865",
      "org": "Zhang, Y., Zhang, Z.-H., & Qin, H.",
      "title": "Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways",
      "published": "2026-07-23",
      "url": "https://arxiv.org/abs/2607.20860",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 게이트웨이의 모델 대체와 라우팅 희석을 응답 텍스트만으로 감사하는 IRIS 를 제안하고 상용 라이브러리·교차 제공자 감사 결과를 보고한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-866",
      "org": "Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E.",
      "title": "Is That All We Can Do? Relying on Online API Services: A Survey of Localized Speech Recognition Model Integration in Robotic Systems",
      "published": "2026-07-13",
      "url": "https://arxiv.org/abs/2607.11792",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇 시스템의 음성 인식 통합을 온라인 API 의존과 로컬 배치 관점에서 정리한 서베이. Whisper 등 심층 학습 모델, ROS 기반·클라우드·혼합 배치 전략, 동적 환경의 강건성 과제를 다룬다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-738",
      "org": "Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra)",
      "title": "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains",
      "published": "2024-06-17",
      "url": "https://arxiv.org/abs/2406.12045",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델이 흉내 내는 사용자와 도구·정책을 가진 에이전트의 대화를 시뮬레이션해 최종 데이터베이스 상태로 성공을 판정하고 반복 시행 신뢰성 지표 pass^k 를 제안한 벤치마크.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-868",
      "org": "Michael, A. E., & Roesner, F.",
      "title": "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement",
      "published": "2026-07-20",
      "url": "https://arxiv.org/abs/2607.13718",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AI 에이전트의 사용자 수준 권한 제안 21건과 상용 에이전트 5종을 조사해 권한 정책 명세와 강제 방식의 분류를 만들고 실시간 승인 부담과 자동 검토 불투명성의 상충을 보고한 프리프린트(2026-07-15 제출).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2607.13718",
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI",
      "title": "Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents",
      "published": "2025-04-29",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "네덜란드 슈퍼마켓 로봇의 음성 대화 인터페이스에서 네 가지 음성 인식 기술을 영어·네덜란드어·성별로 비교하고, 상품 데이터베이스에 근거한 다층 언어 모델 챗봇을 GPT-4 Turbo 와 사용자 평가로 비교한 학술지 논문(PMC 전문).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023)",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-09-04",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "등각 예측으로 언어 모델 계획기의 불확실도를 보정해 후보 행동 집합이 하나면 실행하고 여러 개면 사람에게 되묻는 KnowNo 틀을 제안한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-840",
      "org": "Laban, P., Hayashi, H., Zhou, Y., & Neville, J.",
      "title": "LLMs Get Lost In Multi-Turn Conversation",
      "published": "2025-05-09",
      "url": "https://arxiv.org/abs/2505.06120",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "20만 건 이상의 시뮬레이션 대화로 언어 모델의 다중 턴 성능이 단일 턴보다 평균 39% 낮고 원인이 신뢰성 저하임을 보고한 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-165",
      "org": "Li, P., An, Z., Abrar, S., & Zhou, L.",
      "title": "Large Language Models for Multi-Robot Systems: A Survey",
      "published": "2025-02-06",
      "url": "https://arxiv.org/abs/2502.03814",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "다중 로봇 시스템에 언어 모델을 쓰는 연구를 작업 배정·동작 계획·행동 생성·사람 개입의 네 층으로 정리하고 사람 개입의 반응적 역할과 운영자 인지 부담 미정량화를 빈틈으로 지적한 서베이.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-753",
      "org": "Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025)",
      "title": "VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots",
      "published": "2025-07-07",
      "url": "https://arxiv.org/abs/2507.05118",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 지시를 선형 시간 논리로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 검증 모듈을 제안한 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
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
      "rationale": "섹션 3: f3·f5(탈옥이 배치된 로봇의 물리 동작으로 이어짐), f14(다중 턴에서 신뢰성 저하), f9(도구 에이전트의 낮은 반복 신뢰성), f15·f16(승인 부담과 자동 검토의 불투명성) / 섹션 4: f1(프롬프트 주입·과도한 에이전시), f3(탈옥), f10·f11(불확실도 보정·되묻기), f8(환각·어포던스·계획 오류), f9(pass^k), f15(권한 명세·강제 방식, 승인 피로), f22(모델 대체·라우팅 희석) / 섹션 5: 상업 시설 — f25(슈퍼마켓 로봇의 음성 대화, 다국어 음성 인식 비교, 상품 DB 근거 응답; 네덜란드 사례임을 명시), 그 밖의 현장 유형 사례는 이번 조사에서 확인되지 않음을 서술 / 섹션 6: 오해석 방지·근거 표시 f10·f11·f12·f7·f25(불확실한 항목만 되묻기, 실행 전 자동 검증, DB 근거 응답), 권한·승인 f2·f6·f15·f17, 모델 연결·교체 f22·f23, 평가 f8·f9·f13, 화면 연동 f26·f27, 음성·다국어 f24·f25 / 섹션 7: f1(OWASP LLM Top 10 2025), f2(MCP 명세 보안 원칙), f18(EU AI Act 제12조), f19(개인정보위 생성형 AI 안내서), f20(TTA 신뢰할 수 있는 AI 개발 안내서), f26(langbar 참조 구현), f8·f9(공개 벤치마크) / 섹션 8: f3, f4, f8, f9, f10, f11, f14, f15, f16, f22, f24, f25, f26, 국내 f19·f20 / 섹션 9: f28(직접 범위: 근거 표시·되묻기, 권한 검사·승인 관문, 기록, 모델 정책, 평가), f29(연계 대상: 음성 인식 엔진 성능, 언어 모델 공급자의 안전 정렬) / 섹션 10: 8. 채팅으로 맵 작성·9. 채팅으로 시나리오 구성·10. 채팅으로 로봇 구성·11. 채팅으로 실제 상황 시뮬레이션 재현·12. 채팅으로 업무 지시·오케스트레이션(f6·f13·f27, 이 영역이 다섯 대화 영역의 공통 기반), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f30, 교차 규칙), 51. 인증·권한·격리(f15·f17), 52. 통신 보호·위협 관리·감사(f1·f3·f4·f18), 53. 개인정보·영상 데이터(f19·f21), 54. 시험·형식 검증·벤치마크(f8·f9), 20. 로봇·제조사 관제 연동(f2·f6 승인 관문 위치), 48. 안전·위험 관리(f3), 57. 자산·소프트웨어 수명주기 관리(f23 모델 교체), 64. 상업 시설(f25) / 섹션 11: 기존 oq-125·oq-127(f13 으로 부분 진전, 미해결), oq-133·oq-136(미조사), oq-139(f15·f16·f17 로 부분 진전, 미해결), oq-141(f2·f6 으로 부분 진전, 공개 구현 미확인)과 open_questions_new 4건. 다음 실행 후보: 52. 통신 보호·위협 관리·감사 페이지에 f1·f3·f4 반영, 51. 인증·권한·격리 페이지에 f15 반영, 54. 시험·형식 검증·벤치마크 페이지에 f8·f9 반영, 12. 채팅으로 업무 지시·오케스트레이션 페이지에 f2·f6 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "프롬프트 주입",
      "term_en": "Prompt Injection",
      "definition": "사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다."
    },
    {
      "term_ko": "탈옥",
      "term_en": "Jailbreak",
      "definition": "언어 모델의 안전 제한을 우회하도록 유도하는 입력 기법으로, 로봇을 제어하는 언어 모델에서는 유해한 물리 동작을 끌어내는 데 쓰일 수 있다."
    },
    {
      "term_ko": "승인 피로",
      "term_en": "Approval Fatigue (Consent Fatigue)",
      "definition": "에이전트의 동작마다 사람에게 승인을 묻는 방식이 반복되어 사용자가 검토 없이 허용하거나 자동 승인으로 바꾸게 되는 현상으로, 실시간 승인 관문의 실효성을 떨어뜨린다."
    },
    {
      "term_ko": "모델 대체·라우팅 희석",
      "term_en": "Model Substitution / Routing Dilution",
      "definition": "언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다."
    }
  ],
  "open_questions_new": [
    "ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 59. 법·규제·보험·라이선스, 53. 개인정보·영상 데이터 | 근거: f21 | 종류: 일반",
    "로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 52. 통신 보호·위협 관리·감사, 48. 안전·위험 관리 | 근거: f4 | 종류: 일반",
    "언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터 | 근거: f22 | 종류: 일반",
    "국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? | 관련 영역: 13. 대화형 기능의 신뢰·기반, 60. 노동·수용성·접근성, 61. 물류창고 | 근거: f24 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 2,
    "unverified": [
      "f19 개인정보위 안내서 PDF 원문 미열람(smartcity.go.kr 사본 ECONNRESET 뒤 404, pipc.go.kr ECONNRESET, kisa.or.kr 인증서 오류) — 4단계 구성·AI 에이전트 관련 내용은 검색 결과 요약에서만 보여 claim 에 넣지 않음",
      "f20 TTA 안내서의 개발 요구사항 15개·검증항목 67개 수치는 검색 결과 요약에만 있고 연 페이지에 없어 claim 에 넣지 않음; 생성 AI 기반 서비스 분야 페이지의 세부 검증항목도 요약 도구 응답이 불명확해 인용하지 않음",
      "f18 EU AI Act 조문 게재 페이지에 발행일·적용일 표시 없음(published null)",
      "f8 Embodied Agent Interface 의 시뮬레이터·모델별 결과 수치는 초록에 없어 미확인",
      "f24 음성 인식 서베이의 소음·다국어 수치는 초록에 없어 미확인",
      "f3 RoboPAIR 의 방어 제안은 초록에 없어 미확인",
      "f12·f5 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)",
      "산업 현장 음성 제어 사례(ScienceDirect·SSRN 게재 'LLM-driven agent for speech-enabled control of industrial robots', 눈게 검사)는 403 으로 열지 못해 넣지 않음",
      "SMaRTAban(영어·슬로바키아어 음성 제어 사족 로봇, Springer)은 인증 리다이렉트로 열지 못해 넣지 않음",
      "CURE(arXiv 2510.08044, 결합 불확실도 추정)는 열었으나 되묻기·실행 결정을 초록이 밝히지 않아 출처 상한 때문에 제외",
      "OpenTelemetry GenAI 시맨틱 규약(도구 호출·에이전트 스팬 기록)은 검색 결과에서만 확인했고 출처 상한으로 넣지 못함 — 대화·도구 호출 기록 형식의 후보",
      "MiniScope(arXiv 2512.11147, 도구 호출 최소 권한)는 열었으나 출처 상한으로 제외(f17 의 결정적 권한 강제 근거로는 ref-868 만 씀)",
      "oq-139·oq-141 은 f15·f16·f17·f2·f6 으로 부분 진전만 있고 승인 단위를 정한 연구나 공개 구현은 확인하지 못해 해결 제안하지 않음",
      "oq-133·oq-136 은 이번 실행에서 조사하지 않음"
    ],
    "scope_violations": [
      "f29: 음성 인식 엔진의 소음·다국어 성능과 언어 모델 공급자의 안전 학습은 분류 원문 19장의 로봇 자체 지능·외부 도구 쪽이므로 '연계 대상: '으로 표시함",
      "f3: RoboPAIR 의 자율주행 언어 모델 사례는 로봇 자체 지능 수준의 공격이므로 위협 근거로만 제안하고 ROP 직접 범위로 서술하지 않음",
      "f18·f19·f20: 법·규제·안내서 내용은 59. 법·규제·보험·라이선스와 53. 개인정보·영상 데이터의 범위와 겹치므로 이 영역에서는 대화 기록 보존·보호 요구의 근거로만 제안함",
      "f9·f15: 로봇이 아닌 일반 도구 에이전트 연구는 평가 지표·권한 설계의 선례로만 제안함",
      "f25: 슈퍼마켓 안내·회수 로봇 사례는 다중 로봇 오케스트레이션이 아니므로 음성·다국어·근거 응답 사례로만 제안함"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-855~ref-869, 예약 구간 안) 상한 도달로 위 미확인 항목의 후보 출처(OpenTelemetry GenAI 규약, MiniScope, CURE, 산업 음성 제어 사례)를 넣지 못했다. 원문 열람 15건(webfetch 15; ref-868 은 arXiv HTML 전문, ref-869 는 PMC 전문, 나머지 논문은 arXiv 초록 페이지), 재사용 4건(ref-351·ref-840·ref-165·ref-753, 이전 브리프 2026-09-29-04·05 의 값 그대로, 이번에 다시 열지 않음). 이전 실행 2026-09-29-05 가 ref-855~ref-862 로 낸 출처(HMCF, ETRI 동향, ROSA, OSRA MCP 세션 등)는 이번 실행의 예약 구간과 번호가 겹치고 참고문헌 목록 입력(0건 요약)에 없어 재사용하지 않았으며, 그 가운데 OSRA Interop SIG MCP 세션(oq-141 근거)은 이번 finding 에 넣지 않았다 — 퍼블리셔가 URL 로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 2건(f5: OWASP·Robey 외·Huang 외, f12: KnowNo·LBAP — 모두 발행 주체가 다름). 모든 finding 신뢰도 medium 이하(high 신뢰도 출처 ref-856·ref-860·ref-863·ref-869 는 각각 단일 출처 finding 에만 쓰임). 분류 원문 핵심 질문(해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면)에는 f2·f6(호스트 쪽 승인 관문과 신뢰하지 않는 입력 처리), f7·f10·f11·f12(실행 전 자동 검증과 불확실도 보정 되묻기), f15·f17(도구 호출 수준의 결정적 권한 강제), f18·f21(자동 기록), f22·f23(모델 대체 감사)로 답했으며 결론은 '모델 밖의 검증·승인·권한·기록 층이 필요하고 승인 단위와 부담은 아직 정량화되지 않았다'는 추정(f6·f13·f17·f23·f28)이다. 현장 유형: 상업 시설(f25, 네덜란드 슈퍼마켓 연구)만 확인했고 물류창고·제조 공장·병원·가정·실외 사례는 없다. 국내 자료는 TTA 안내서(f20)와 개인정보위 안내서(f19) 두 건이며 국내 로봇 대화 기능 사례는 찾지 못했다. L. AI·학습 기술 관련 finding(f3·f4·f8·f10·f11·f30)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처 없음(OWASP 는 업계 보고서, MCP 명세는 오픈소스 문서로 분류). 용어집에 이미 있는 환각·과도한 에이전시·사람 참여 루프·모델 컨텍스트 프로토콜·구조화 출력·제약 디코딩·등각 예측·불확실도 정렬·자동화 편향·역할 기반 접근 통제·감사 추적·pass^k·사용자 시뮬레이터·명확화 질문은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-06/verification.json

```json
{
  "run_id": "2026-09-29-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. genai.owasp.org 목록 페이지에서 LLM01~LLM10 열 항목과 LLM01·LLM06 한 줄 설명 확인(발행 주체 OWASP Gen AI Security Project, 2025년판). 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 명세 2025-06-18 개요 페이지 'Security and Trust & Safety' 절에서 'Hosts must obtain explicit user consent before invoking any tool', 도구 설명·주석은 신뢰 서버가 아니면 untrusted, 'MCP itself cannot enforce these security principles at the protocol level, implementors SHOULD build robust consent and authorization flows' 원문 확인. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. arXiv 2410.13691 초록(2024-10-17 제출, 2024-11-09 개정)에서 세 설정(NVIDIA Dolphins 화이트박스·Jackal+GPT-4o 그레이박스·Unitree Go2 블랙박스)과 '첫 배치 상용 로봇 탈옥' 문구 확인. 단 초록은 'often achieving 100% attack success rates'(종종 100%)로 적으므로 무조건 100%로 읽히지 않게 표현을 고쳐야 한다. 교차 확인: The Register(2024-11-16)·Hackster.io 의 독립 보도가 같은 세 설정과 수치를 전한다(2차 보도)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2601.02377 초록(2025-12-17 제출)에서 embodiment gap, 공격 분류(탈옥·백도어·다중 모달 프롬프트 주입), 방어(형식 안전 명세·런타임 강제·다중 LLM 감독·프롬프트 강화), 데이터셋·벤치마크 검토 확인. 단일 출처."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-855·ref-857·ref-859 를 각각 열어 세 발행 주체(OWASP, Penn 연구진, Sydney 등 연구진)가 프롬프트 주입·탈옥 위협을 독립적으로 보고함을 확인."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f2·f3·f1 의 확인된 내용을 결합한 구축자 추정이며 근거 범위를 넘지 않는다. 신뢰도 low 적정."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 재사용 출처 ref-753(arXiv 2507.05118, IROS 2025)을 이번 검증에서 열어 자연어→LTL 변환 뒤 행동 순서열의 일관성·누락 단계 검사, 가정 작업 데이터셋, 코드 공개(verifyllm.github.io) 확인. 브리프는 이번 실행에서 열지 않아 source_unopened: true 로 표시했고 그 표시는 유지한다. 단일 출처."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2410.07166 초록(2024-10-09 제출, 2025-01-19 개정, NeurIPS 2024 D&B 구두)에서 네 모듈과 환각·어포던스·계획 오류 세분화 지표 확인. 단일 출처."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2406.12045 초록(2024-06-17)에서 시뮬레이션 사용자, 최종 DB 상태 비교, pass^k, gpt-4o 과제 성공률 50% 미만·소매 pass^8 25% 미만 확인. Sierra 블로그(2024-06-20)도 같은 수치를 적지만 같은 발행 주체이므로 독립 교차 확인으로 세지 않았다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 재사용 출처 ref-351(arXiv 2307.01928, CoRL 2023 구두, 2023-09-04 개정)을 열어 등각 예측 기반 불확실도 정렬과 도움 요청 최소화 확인. 브리프의 source_unopened: true 표시는 유지. 단일 출처."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2403.13198 초록(2024-03-19 제출, 2025-06-17 v3)에서 LBAP, 베이즈 추론으로 장면 근거·세계 지식 결합, 환각 대응, '성공률 70%에서 도움 요청률 33% 넘게 감소' 확인. 단일 출처."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-351(Princeton·Google 연구진)과 ref-864(Maryland 연구진)를 각각 열어 두 독립 연구 그룹이 불확실도 보정 기반 되묻기를 보고함을 확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f8·f9·f11 의 지표를 조합한 구축자 추정이며 특화 벤치마크 부재는 검색 범위 안의 판단으로 표시돼 있다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 재사용 출처 ref-840(arXiv 2505.06120, 2025-05-09)을 열어 20만 건 이상 시뮬레이션 대화, 여섯 생성 과제, 평균 39% 하락, 초기 가정 과의존 확인. ICLR 2026 게재본과 제3자 요약(beam.ai)이 같은 수치를 전한다(2차 보도). 브리프의 source_unopened: true 표시는 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2607.13718 HTML 본문(2026-07-15 제출, 2026-07-20 v2)에서 21건 제안·상용 5종(Claude, Claude Cowork, ChatGPT 채팅, ChatGPT 에이전트 모드, Codex), 인용문 'Commercial agents often force users to choose between…' 원문 일치, '세 목표를 모두 이루는 시스템 없음' 확인. 단 강제 방식 다섯째 항목은 본문에서 'AI 생성 강제 코드'로 읽히며 브리프의 '형식 검증 강제'는 확인되지 않아 표현 정정이 필요하다. 단일 출처."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 재사용 출처 ref-165 의 arXiv HTML v5(2026-05-03) 4.4절에서 'the human's role remains reactive rather than collaborative'와 'none quantify the cognitive load of different intervention modes as team size scales' 확인. 초록에는 없는 내용이므로 기준일을 v5 개정일로 적어야 한다. 브리프의 source_unopened: true 표시는 유지. 단일 출처."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f15·f16·f2 의 확인된 내용에서 도출한 구축자 추정이며 oq-139 의 답이 아님을 밝히고 있다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 유럽위원회 AI Act 서비스 데스크 페이지에서 제12조 제1항·제2항 조문 원문 확인(페이지는 'Official version of 13 June 2024'를 표시). 독립 출처 artificialintelligenceact.eu(Future of Life Institute)의 제12조 조문과 일치. 발행일은 규정 공식본 날짜로 보완 가능."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 개인정보보호위원회 게시물(2025-08-22, 제목 '…안내서(2025.8.)_파일수정게시')에서 '생성형 AI 수명주기 각 단계… 법적 기준 및 안전조치 제시' 문장 원문 확인. 독립 출처(김앤장·법무법인 화우 뉴스레터 검색 결과)가 2025-08-06 배포와 4단계 구성을 전한다. 안내서 PDF 본문은 이번 검증에서도 열지 않았다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. tta-trustworthy-ai.gitbook.io 일러두기에서 발행 기관, 2024년 2월 발간, 2025-08-14 갱신, '기술적 측면의 신뢰성 확보 방안' 문구, 2023·2024 분야별 안내서 추가 확인. TTA 공식 게시판(안내서 4종)과 FAIR AI 페이지가 2024년 생성 AI 기반 서비스 분야 안내서를 확인."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f18~f20 을 대화 기록 보존·보호 요구에 대응시킨 구축자 추정이며 적용 여부는 열린 질문으로 남겼다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2607.20860 초록(2026-07-23)에서 응답 텍스트만으로 감사, 희석 탐지력 0.85·오탐 0.017, 희석 비율 오차 0.04 이내 확인. 단 교차 제공자 결과는 '같은 모델을 내는 제공자 쌍 15개 중 14개를 실제 양자화·커널 차이로 표시'이며 브리프의 '문제 모델 쌍'은 초록과 다르므로 표현 정정이 필요하다. 단일 출처."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f22·f1 에서 도출한 구축자 추정. f22 의 표현 정정 뒤에도 성립한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2607.11792(2026-07-13, 저자 Li·Li·Schijve·Hu·Barakova) 초록에서 온라인 API 의존 질문, Whisper, ROS 기반·클라우드·혼합 배치, 동적 환경 강건성 과제 확인. 단 실제 제목은 'Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems'이며 브리프 ref-866 제목과 다르다. 단일 출처."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC12069059(Frontiers in Robotics and AI, 2025-04-29, TU Delft) 전문에서 음성 인식 4종(Vosk·Whisper·Google·Azure), 영어·네덜란드어·성별 참가자 40명, Whisper 최저 단어 오류율, 상품 1,612개, 분류기 정확도 86.79%, 참가자 16명 평가에서 13개 항목 중 4개 유의 우세 확인. 단일 출처."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2510.06223 초록(2025-08-31 제출, 2025-10-09 v2, 저자 van Dam)에서 MCP 로 화면 이동 그래프·의미 노출, 뷰모델의 화면별·전역 도구, 음성–화면 정렬·일관 피드백, langbar 참조 구현, 개방 가중치 모델 정확도 근접 확인. 단일 출처."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f26·f2 를 화면 편집 연동 요구에 대응시킨 구축자 추정."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 원문 19장 경계에 맞춘 직접 범위 추정이며 인용 finding 이 모두 확인됐다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. '연계 대상: ' 표시가 있고 음성 인식·모델 안전 정렬을 외부 범위로 둔 판단이 원문 19장과 맞는다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 교차 규칙 적용 판단이며 연결 대상 영역의 번호·이름이 부록 A 와 일치한다."
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
      "ref-855~ref-862 id 구간이 이전 실행 2026-09-29-05 의 출처(HMCF, Argenziano 외, ETRI 동향, ROSA, Henkel 외, OSRA MCP 세션)와 번호가 겹친다 — 퍼블리셔가 URL 기준으로 합칠 때 이번 브리프의 OWASP·MCP 명세·RoboPAIR·Embodied Agent Interface·Huang 외·TTA 안내서·van Dam·개인정보위 게시물에 새 번호를 주어야 한다",
      "f10(KnowNo)·f14(Laban 외)는 2026-09-29-04 브리프 f1·f4, f7(VerifyLLM)·f16(Li 외 서베이)은 2026-09-29-05 브리프 f8·f2 와 같은 주장이며 기존 ref-351·ref-840·ref-753·ref-165 를 재사용했으므로 중복 각주 없음"
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
    "ref-866: 제목을 'Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems'로 고친다(각주 정의와 reference_updates 모두) — arXiv 2607.11792 실제 제목이며 브리프 제목은 다른 문구다.",
    "f22: '교차 제공자 감사에서 문제 모델 쌍 15개 중 14개를 표시했다'를 '같은 모델을 내는 제공자 쌍 15개 중 14개를 실제 양자화·커널 차이로 표시했다'로 고친다 — 초록은 문제(사기) 쌍이 아니라 동일 모델 제공자 쌍의 실제 서빙 차이를 잡았다고 적는다.",
    "f15: 강제 방식 분류의 다섯째 항목 '형식 검증 강제'를 본문 표기대로 'AI 생성 강제 코드'로 고치거나 다섯 항목 열거를 빼고 '다섯 가지 강제 방식'으로만 쓴다 — 원문 본문에서 '형식 검증 강제'는 확인되지 않았다.",
    "f3: '세 설정에서 100% 공격 성공률을 보고했고'를 '세 설정에서 종종(often) 100%에 이르는 공격 성공률을 보고했고'로 고친다 — 초록 문구가 'often achieving 100% attack success rates'다.",
    "f16: 기준일을 2026-05-03(arXiv v5)으로 적고 각주 ref-165 정의에 판(v5, 2026-05-03 개정)을 병기한다 — 반응적 역할·인지 부담 미정량화 문장은 초록이 아니라 v5 본문 4.4절에 있다.",
    "ref-863: 발행일을 '미확인' 대신 2024-06-13(규정 공식본 날짜, 페이지 표기 'Official version of 13 June 2024')으로 적는다 — 검증에서 페이지 표기를 확인했다.",
    "각주: ref-351·ref-840·ref-165·ref-753 의 접근일 뒤 ' (원문 미열람)' 표기와 reference_updates[].source_unopened: true 를 브리프 표시대로 유지한다 — 리서치 실행이 이번에 열지 않았으므로 코드의 신뢰도 상한이 적용된다(검증에서는 네 건 모두 열어 내용 일치를 확인했다)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 30건, 미확인 0건, 교차 확인 7건(f3·f5·f12·f14·f18·f19·f20). 강등: 없음. 원문 미열람 출처: 브리프 기준 ref-351, ref-840, ref-165, ref-753(재사용, 리서치 실행에서 열지 않음; 검증에서는 네 건 모두 열어 주장 일치를 확인했다). 신규 출처 15건(ref-855~ref-869)은 모두 열어 기관·제목·발행일이 일치함을 확인했고, ref-866 은 제목이 실제와 달라 정정을 지시했다. 주의: 핵심 주장 대부분이 단일 출처 논문·문서에 기대고 결론(f6·f13·f17·f23·f28)이 구축자 추정이므로 신뢰도는 medium 이다. f3 은 초록이 '종종 100%'로 적어 표현을 고치게 했고, f22 의 교차 제공자 결과와 f15 의 강제 방식 다섯째 항목도 원문에 맞게 정정을 지시했다. 로봇 대화 기능 전용 벤치마크와 국내 현장 사례는 이번 조사에서 확인되지 않았으며 현장 유형 사례는 상업 시설(네덜란드 슈퍼마켓 연구) 하나뿐이다. 개인정보위 안내서(ref-862)는 배포일이 2025-08-06 이고 게시물은 2025-08-22 파일수정게시본이며 PDF 본문은 미열람이다. ref-855~ref-862 번호가 이전 실행 2026-09-29-05 의 출처와 겹치므로 퍼블리셔가 URL 기준으로 새 번호를 배정해야 한다. oq-125·oq-127·oq-139·oq-141 은 부분 진전만 있어 해결로 인정하지 않는다. 정정 요청 없음. 검증 검색 4회(리서치 17회와 합쳐 21/30), 열람 22회.",
  "retry_reason": null
}
```

### runs/2026-09-29-06/pages.json

```json
{
  "run_id": "2026-09-29-06",
  "outline": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "오해석뿐 아니라 프롬프트 주입·탈옥 같은 외부 조작이 도구 호출·로봇 동작으로 이어짐을 세 발행 주체가 각각 보고했다. [사실][^ref-855][^ref-857][^ref-859] 다중 턴에서 신뢰성이 떨어지고 승인 관문의 부담은 정량화되지 않았다. [사실][^ref-840][^ref-165]",
      "planned_findings": [
        "f5",
        "f3",
        "f14",
        "f9",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "OWASP 2025년판 LLM Top 10 은 프롬프트 주입·과도한 에이전시 등 열 가지 위험을 정리한다. [사실][^ref-855] 탈옥·체화 격차·불확실도 보정 되묻기·오류 유형·pass^k·승인 피로·모델 대체 용어를 정의한다.",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f12",
        "f8",
        "f9",
        "f15",
        "f22",
        "f2"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 900,
      "summary": "상업 시설(네덜란드 슈퍼마켓) 로봇의 음성 대화에서 Whisper 가 가장 낮은 단어 오류율을 보였고 상품 DB 근거 다층 언어 모델이 GPT-4 Turbo 보다 13개 중 4개 항목에서 우세했다. [사실][^ref-869]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2200,
      "summary": "불확실도 보정 되묻기(KnowNo·LBAP)와 실행 전 자동 검증(VerifyLLM), 호스트 쪽 승인 관문(MCP), 결정적 권한 강제, 모델 대체 감사(IRIS), 자동 로그, 세분화 평가, 화면–대화 연동, 음성 배치 전략을 정리한다. [사실][^ref-351][^ref-864][^ref-856][^ref-865]",
      "planned_findings": [
        "f2",
        "f6",
        "f7",
        "f10",
        "f11",
        "f12",
        "f13",
        "f15",
        "f17",
        "f18",
        "f21",
        "f22",
        "f23",
        "f24",
        "f26",
        "f27",
        "f8",
        "f9",
        "f14",
        "f25"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "OWASP LLM Top 10, MCP 명세 보안 원칙, EU AI Act 제12조, 개인정보위·TTA 안내서, Embodied Agent Interface·τ-bench, VerifyLLM·langbar 를 표로 둔다. [사실][^ref-855][^ref-856][^ref-863][^ref-862][^ref-860]",
      "planned_findings": [
        "f1",
        "f2",
        "f18",
        "f19",
        "f20",
        "f8",
        "f9",
        "f7",
        "f26"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "RoboPAIR, Huang 외 서베이, KnowNo, LBAP, VerifyLLM, Embodied Agent Interface, τ-bench, Laban 외, Michael·Roesner, Li 외 서베이, IRIS, 음성 인식 서베이, 슈퍼마켓 로봇 연구, van Dam, 국내 안내서 2건. [사실][^ref-857][^ref-859]",
      "planned_findings": [
        "f3",
        "f4",
        "f10",
        "f11",
        "f7",
        "f8",
        "f9",
        "f14",
        "f15",
        "f16",
        "f22",
        "f24",
        "f25",
        "f26",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 800,
      "summary": "ROP 는 근거 표시·되묻기, 도구 호출 수준 권한 검사와 승인 관문, 대화·도구 호출·제공 모델 기록, 모델 교체 정책, 평가 시나리오를 맡고, 음성 인식 엔진 성능과 언어 모델의 안전 정렬은 연계 대상으로 둔다. [추정][^ref-856][^ref-868][^ref-865][^ref-866][^ref-858]",
      "planned_findings": [
        "f28",
        "f29",
        "f2"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 900,
      "summary": "8~12번 대화 영역의 공통 기반이며 44·47(교차 규칙), 51·52·53(권한·기록·개인정보), 54(평가), 20(승인 관문 위치), 48(안전), 57(모델 교체), 59(규제), 64(상업 시설)과 잇는다. [추정][^ref-858][^ref-857][^ref-863]",
      "planned_findings": [
        "f30",
        "f6",
        "f13",
        "f27",
        "f15",
        "f17",
        "f1",
        "f3",
        "f4",
        "f18",
        "f19",
        "f21",
        "f8",
        "f9",
        "f2",
        "f23",
        "f25"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "section": "11. 열린 질문",
      "budget_chars": 900,
      "summary": "기존 6건(oq-125·127·133·136·139·141)은 부분 진전만 있어 열림으로 두고, 고위험 AI 해당 여부·탈옥 방어 벤치마크·모델 대체 실무 절차·국내 음성 지시 사례 4건을 새로 올린다.",
      "planned_findings": [
        "f13",
        "f17",
        "f6",
        "f21",
        "f4",
        "f22",
        "f24"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-869 신규, ref-351·ref-840·ref-165·ref-753 재사용), 상업 시설 사례 1건, 열린 질문 4건 추가, 1차 조건부 승인 수정 7건 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"6. 대표 접근법과 기술\" 절(3,607자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"8. 대표 연구와 자료\" 절(1,988자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"11. 열린 질문\" 절(1,562자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"4. 핵심 개념과 용어\" 절(1,495자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,267자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,256자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area13-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 13. 대화형 기능의 신뢰·기반 의 \"3. 왜 중요한가\" 절(1,085자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 13. 대화형 기능의 신뢰·기반 | 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-869 신규, 4건 재사용), 상업 시설 사례 1건, 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 7건 이행 | run 2026-09-29-06",
  "index_updates": {
    "home_recent": "2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성(seed → draft). 프롬프트 주입·탈옥 위협, 불확실도 보정 되묻기, 호스트 쪽 승인 관문, 모델 대체 감사, 대화 기록 규제를 정리하고 상업 시설 사례 1건·열린 질문 4건·용어 4건을 더했다",
    "category_recent": "2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성(seed → draft), 출처 19건, 상업 시설(네덜란드 슈퍼마켓) 사례 1건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-06)",
    "area_recent": "2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성. 위협(OWASP·RoboPAIR·Huang 외), 되묻기·자동 검증(KnowNo·LBAP·VerifyLLM), 승인 관문·권한(MCP·Michael·Roesner), 모델 대체 감사(IRIS), 기록 규제(EU AI Act 제12조·국내 안내서), 평가(Embodied Agent Interface·τ-bench), 화면 연동·음성 사례를 정리 (실행 2026-09-29-06)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "prompt-injection",
      "term_ko": "프롬프트 주입",
      "term_en": "Prompt Injection",
      "definition": "사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다.",
      "description": "OWASP 2025년판 LLM 응용 프로그램 Top 10 의 첫 항목(LLM01). MCP 명세는 도구 설명·주석을 신뢰 서버에서 온 것이 아니면 신뢰하지 말라고 적어 주입 경로를 좁힌다.",
      "related_areas": [
        13,
        52,
        12
      ],
      "sources": [
        "ref-855",
        "ref-856"
      ]
    },
    {
      "action": "new",
      "slug": "jailbreak",
      "term_ko": "탈옥",
      "term_en": "Jailbreak",
      "definition": "언어 모델의 안전 제한을 우회하도록 유도하는 입력 기법으로, 로봇을 제어하는 언어 모델에서는 유해한 물리 동작을 끌어내는 데 쓰일 수 있다.",
      "description": "Robey 외(2024)의 RoboPAIR 는 세 설정의 언어 모델 제어 로봇에서 종종 100%에 이르는 공격 성공률을 보고했고, Huang 외(2025) 서베이는 탈옥을 공격 벡터 분류의 한 축으로 둔다.",
      "related_areas": [
        13,
        48,
        52,
        44
      ],
      "sources": [
        "ref-857",
        "ref-859"
      ]
    },
    {
      "action": "new",
      "slug": "approval-fatigue",
      "term_ko": "승인 피로",
      "term_en": "Approval Fatigue (Consent Fatigue)",
      "definition": "에이전트의 동작마다 사람에게 승인을 묻는 방식이 반복되어 사용자가 검토 없이 허용하거나 자동 승인으로 바꾸게 되는 현상으로, 실시간 승인 관문의 실효성을 떨어뜨린다.",
      "description": "Michael·Roesner(2026)는 실시간 사용자 승인을 부담이 큰 강제 방식으로 분류하고 상용 에이전트가 이 부담과 불투명한 자동 검토 사이의 선택을 강요한다고 보고했다. 로봇 대수·계획 크기에 따른 승인 단위는 열린 질문(oq-139)이다.",
      "related_areas": [
        13,
        12,
        51
      ],
      "sources": [
        "ref-868",
        "ref-165"
      ]
    },
    {
      "action": "new",
      "slug": "model-substitution-and-routing-dilution",
      "term_ko": "모델 대체·라우팅 희석",
      "term_en": "Model Substitution / Routing Dilution",
      "definition": "언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다.",
      "description": "Zhang·Zhang·Qin(2026)의 IRIS 는 응답 텍스트만으로 이를 감사해 상용 라이브러리에서 희석을 탐지력 0.85·오탐률 0.017 로 잡았다.",
      "related_areas": [
        13,
        47,
        57
      ],
      "sources": [
        "ref-865"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-855",
      "org": "OWASP GenAI Security Project",
      "title": "OWASP Top 10 for LLM Applications 2025",
      "published": "2025",
      "url": "https://genai.owasp.org/llm-top-10/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 응용 프로그램의 열 가지 위험 목록(프롬프트 주입, 민감 정보 노출, 공급망, 부적절한 출력 처리, 과도한 에이전시, 잘못된 정보 등)을 항목별 한 줄 설명과 함께 게시한 목록 페이지다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-856",
      "org": "Model Context Protocol (Anthropic 주도 오픈소스 프로젝트)",
      "title": "Specification — Model Context Protocol (2025-06-18)",
      "published": "2025-06-18",
      "url": "https://modelcontextprotocol.io/specification/2025-06-18",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "MCP 명세 개요 페이지. '보안과 신뢰·안전' 절에 사용자 동의·제어, 데이터 프라이버시, 도구 안전(도구 호출 전 명시적 동의, 도구 설명 불신), 샘플링 제어 원칙과 구현 지침을 둔다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J.",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-11-09",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 제어 로봇을 탈옥시키는 RoboPAIR 를 제안하고 자율주행 언어 모델·Jackal UGV·Unitree Go2 의 세 설정에서 종종 100%에 이르는 공격 성공률과 유해 물리 동작을 보고한 프리프린트(2024-10-17 제출).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-858",
      "org": "Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks)",
      "title": "Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making",
      "published": "2025-01-19",
      "url": "https://arxiv.org/abs/2410.07166",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "체화 의사결정을 목표 해석·하위 목표 분해·행동 순서화·전이 모델링의 네 모듈로 나누고 환각·어포던스·계획 오류를 구분하는 세분화 지표로 언어 모델을 평가하는 벤치마크(2024-10-09 제출).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-859",
      "org": "Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R.",
      "title": "Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges",
      "published": "2025-12-17",
      "url": "https://arxiv.org/abs/2601.02377",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 제어 로봇의 체화 격차를 중심으로 탈옥·백도어·다중 모달 프롬프트 주입 등 공격 벡터 분류와 형식 안전 명세·런타임 강제·다중 언어 모델 감독·프롬프트 강화 등 방어, 평가 데이터셋·벤치마크를 정리한 서베이.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-860",
      "org": "과학기술정보통신부·한국정보통신기술협회(TTA)",
      "title": "2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기)",
      "published": "2024-02",
      "url": "https://tta-trustworthy-ai.gitbook.io/general",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "인공지능 서비스·제품 개발 과정의 기술적 신뢰성 확보 방안을 다루는 안내서의 웹 문서판. 2024년 2월 발간 뒤 2025-08-14까지 갱신되었고, 2024년 생성 AI 기반 서비스 분야 안내서가 추가되었다고 적는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-861",
      "org": "van Dam, H. G. W.",
      "title": "A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants",
      "published": "2025-10-09",
      "url": "https://arxiv.org/abs/2510.06223",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "응용 프로그램의 화면 이동 그래프와 의미를 MCP 로 노출해 음성 대화 비서와 GUI 를 맞추는 아키텍처를 제안하고 참조 구현(langbar)과 개방 가중치 모델 평가를 담은 프리프린트(2025-08-31 제출).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-862",
      "org": "개인정보보호위원회",
      "title": "생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.)",
      "published": "2025-08",
      "url": "https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "개인정보보호위원회 공식 사이트 게시물(2025-08-22 파일수정게시, 배포 2025-08-06). 생성형 AI 수명주기 단계별 개인정보 처리·보호 이슈와 법적 기준·안전조치를 제시하는 안내서의 PDF 배포 안내이며, PDF 본문은 이번 실행에서 열지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-863",
      "org": "European Commission — AI Act Service Desk",
      "title": "Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act)",
      "published": "2024-06-13",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "유럽위원회 서비스 데스크가 게재한 AI Act 제12조 조문(페이지 표기 'Official version of 13 June 2024'). 고위험 AI 시스템의 수명 기간 자동 사건 기록(로그)과 추적 가능성 요건, 원격 생체 식별 시스템의 최소 로그 항목을 규정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-864",
      "org": "Mullen, J. F., Jr., & Manocha, D.",
      "title": "Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners",
      "published": "2025-06-17",
      "url": "https://arxiv.org/abs/2403.13198",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "장면 근거와 세계 지식을 베이즈 추론으로 결합해 언어 모델 계획기의 확신도를 보정하는 LBAP 를 제안하고 성공률 70%에서 사람 도움 요청률을 33% 넘게 줄였다고 보고한 프리프린트(2024-03-19 제출).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-865",
      "org": "Zhang, Y., Zhang, Z.-H., & Qin, H.",
      "title": "Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways",
      "published": "2026-07-23",
      "url": "https://arxiv.org/abs/2607.20860",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 게이트웨이의 모델 대체와 라우팅 희석을 응답 텍스트만으로 감사하는 IRIS 를 제안하고 상용 라이브러리 감사(희석 탐지력 0.85·오탐 0.017)와 같은 모델을 내는 제공자 쌍 15개 중 14개의 양자화·커널 차이 표시 결과를 보고한 프리프린트.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-866",
      "org": "Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E.",
      "title": "Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems",
      "published": "2026-07-13",
      "url": "https://arxiv.org/abs/2607.11792",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇 시스템의 음성 인식 통합을 온라인 API 의존과 로컬 배치 관점에서 정리한 서베이. Whisper 등 심층 학습 모델, ROS 기반·클라우드·혼합 배치 전략, 동적 환경의 강건성 과제를 다룬다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-738",
      "org": "Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra)",
      "title": "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains",
      "published": "2024-06-17",
      "url": "https://arxiv.org/abs/2406.12045",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델이 흉내 내는 사용자와 도구·정책을 가진 에이전트의 대화를 시뮬레이션해 최종 데이터베이스 상태로 성공을 판정하고 반복 시행 신뢰성 지표 pass^k 를 제안한 벤치마크.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-868",
      "org": "Michael, A. E., & Roesner, F.",
      "title": "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement",
      "published": "2026-07-20",
      "url": "https://arxiv.org/abs/2607.13718",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AI 에이전트의 사용자 수준 권한 제안 21건과 상용 에이전트 5종을 조사해 권한 정책 명세와 다섯 가지 강제 방식의 분류를 만들고 실시간 승인 부담과 자동 검토 불투명성의 상충을 보고한 프리프린트(2026-07-15 제출).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-869",
      "org": "Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI",
      "title": "Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents",
      "published": "2025-04-29",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "네덜란드 슈퍼마켓 로봇의 음성 대화 인터페이스에서 네 가지 음성 인식 기술을 영어·네덜란드어·성별로 비교하고, 상품 데이터베이스에 근거한 다층 언어 모델 챗봇을 GPT-4 Turbo 와 사용자 평가로 비교한 학술지 논문(PMC 전문).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023)",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-09-04",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 등각 예측으로 언어 모델 계획기의 불확실도를 보정해 후보 행동 집합이 하나면 실행하고 여러 개면 사람에게 되묻는 KnowNo 틀을 제안한 논문(재사용 출처, 이번 리서치 실행에서 열지 않음).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-840",
      "org": "Laban, P., Hayashi, H., Zhou, Y., & Neville, J.",
      "title": "LLMs Get Lost In Multi-Turn Conversation",
      "published": "2025-05-09",
      "url": "https://arxiv.org/abs/2505.06120",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 20만 건 이상의 시뮬레이션 대화로 언어 모델의 다중 턴 성능이 단일 턴보다 평균 39% 낮고 원인이 신뢰성 저하임을 보고한 프리프린트(재사용 출처, 이번 리서치 실행에서 열지 않음).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-165",
      "org": "Li, P., An, Z., Abrar, S., & Zhou, L.",
      "title": "Large Language Models for Multi-Robot Systems: A Survey",
      "published": "2025-02-06",
      "url": "https://arxiv.org/abs/2502.03814",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 다중 로봇 시스템에 언어 모델을 쓰는 연구를 네 층으로 정리하고 사람 개입의 반응적 역할과 운영자 인지 부담 미정량화를 빈틈으로 지적한 서베이(인용 문장은 v5, 2026-05-03 개정 본문 4.4절 기준. 재사용 출처, 이번 리서치 실행에서 열지 않음).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    },
    {
      "id": "ref-753",
      "org": "Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025)",
      "title": "VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots",
      "published": "2025-07-07",
      "url": "https://arxiv.org/abs/2507.05118",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 자연어 지시를 선형 시간 논리로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 검증 모듈을 제안한 논문(재사용 출처, 이번 리서치 실행에서 열지 않음).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가?",
      "areas": [
        13,
        59,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가?",
      "areas": [
        13,
        52,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가?",
      "areas": [
        13,
        57,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)?",
      "areas": [
        13,
        60,
        61
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    },
    {
      "site_type": "상업 시설",
      "item": "완료·인계",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시",
      "title": "13. 대화형 기능의 신뢰·기반"
    }
  ],
  "standards_updates": [
    {
      "name": "EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping)",
      "kind": "프레임워크",
      "org": "European Union (유럽위원회 AI Act Service Desk 게재)",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "related_areas": [
        13,
        52,
        53,
        59
      ],
      "summary": "법규(EU 규정). 고위험 AI 시스템이 수명 기간 내내 사건을 자동으로 기록하고 위험 상황 식별·시장 출시 후 모니터링·운영 모니터링에 필요한 추적 가능성을 보장하도록 규정한다. 대화 기록 자동 로그의 근거 후보.",
      "ref_id": "ref-863"
    },
    {
      "name": "생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.)",
      "kind": "프레임워크",
      "org": "개인정보보호위원회",
      "url": "https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836",
      "related_areas": [
        13,
        53
      ],
      "summary": "생성형 AI 수명주기 각 단계의 개인정보 처리·보호 이슈를 체계화하고 법적 기준과 안전조치를 제시하는 국내 정부 안내서(공식 사이트 게시 2025-08-22). PDF 본문은 미열람.",
      "ref_id": "ref-862"
    },
    {
      "name": "2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야",
      "kind": "프레임워크",
      "org": "과학기술정보통신부·한국정보통신기술협회(TTA)",
      "url": "https://tta-trustworthy-ai.gitbook.io/general",
      "related_areas": [
        13,
        47,
        54
      ],
      "summary": "AI 서비스·제품 개발 과정의 기술적 신뢰성 확보 방안을 다루는 국내 안내서. 2024년 2월 발간, 웹 문서로 2025-08-14까지 갱신, 2024년 생성 AI 기반 서비스 분야 안내서 추가.",
      "ref_id": "ref-860"
    },
    {
      "name": "Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크)",
      "kind": "평가 프로그램",
      "org": "Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks)",
      "url": "https://arxiv.org/abs/2410.07166",
      "related_areas": [
        13,
        44,
        54
      ],
      "summary": "목표 해석·하위 목표 분해·행동 순서화·전이 모델링 네 모듈로 나누고 환각·어포던스·계획 오류를 구분하는 세분화 지표로 언어 모델을 평가한다.",
      "ref_id": "ref-858"
    },
    {
      "name": "langbar (다중 모달 GUI–MCP 아키텍처 참조 구현)",
      "kind": "오픈소스",
      "org": "van Dam, H. G. W.",
      "url": "https://arxiv.org/abs/2510.06223",
      "related_areas": [
        13,
        8,
        9
      ],
      "summary": "응용 프로그램의 화면 이동 그래프와 의미를 MCP 로 노출해 음성 대화 비서와 GUI 를 맞추는 아키텍처의 참조 구현.",
      "ref_id": "ref-861"
    }
  ],
  "additional_research_requests": [
    "5절에 물류창고·병원·제조 공장·가정·실외의 대화 기능 실제 사례와 국내 현장 자료가 필요하다. 이번 브리프에는 상업 시설(네덜란드 슈퍼마켓 연구) 하나뿐이어서 다른 현장 유형 사례를 쓰지 못했다.",
    "6·8절(대화형 기능 평가)에 로봇 지도 작성·로봇 구성 대화에 특화된 벤치마크나 지표(oq-125·oq-127)가 필요하다. 이번 브리프는 일반 체화 벤치마크(Embodied Agent Interface)와 도구 에이전트 벤치마크(τ-bench)만 확인했다.",
    "6절(대화 권한과 승인 관문)에 로봇 대수·계획 크기에 따른 승인 단위를 정한 연구나 지침(oq-139)과, MCP 도구 호출 경로에서 승인 관문을 둔 공개 구현·운영 사례(oq-141. 브리프가 언급한 OSRA Interop SIG MCP 세션 포함)가 필요하다.",
    "6절(대화 기록의 보존·보호)에 대화·도구 호출·제공 모델 기록 형식의 근거(브리프가 출처 상한으로 넣지 못한 OpenTelemetry GenAI 시맨틱 규약)와 개인정보보호위원회 안내서 PDF 본문(4단계 구성, AI 에이전트 관련 내용)이 필요하다.",
    "6절(음성·다국어)에 산업 현장 음성 제어 사례(브리프가 403·인증 리다이렉트로 열지 못한 ScienceDirect·SSRN 게재 논문과 SMaRTAban)와 소음·한국어 조건 인식률 수치가 필요하다.",
    "참고문헌 id 확인 요청: 브리프와 1차 검증은 ref-840 을 Laban 외(2025) 'LLMs Get Lost In Multi-Turn Conversation'(arXiv 2505.06120)으로 쓰지만, 입력의 C. 채팅 기반 구성·운영 대분류 페이지 자료 목록에는 ref-840 이 Tack·Laban·Neville 'LLMs Get Lost in Evolving User Intent'(2026-07-22)로 실려 있다. 퍼블리셔가 URL 기준으로 합칠 때 두 논문이 다른 id 를 갖는지 확인해야 한다.",
    "참고문헌 번호 충돌 확인 요청: 1차 검증 지적대로 ref-855~ref-862 가 이전 실행 2026-09-29-05 의 출처와 번호가 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 새 번호를 배정해야 하며, 본문 각주도 그에 맞춰 바뀌어야 한다."
  ],
  "fixes_applied": [
    "ref-866 제목 정정 — 13절 각주 정의와 reference_updates 의 제목을 'Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems'로 고쳤고, 8절 목록에서도 이 제목으로 적었다.",
    "f22 표현 정정 — 6절 '언어 모델 연결·교체와 대체 감사'의 IRIS 문장을 '같은 모델을 내는 제공자 쌍 15개 중 14개를 실제 양자화·커널 차이로 표시했다'로 썼고 reference_updates 요약도 같은 표현으로 맞췄다.",
    "f15 강제 방식 다섯째 항목 정정 — 6절 '대화 권한과 실행 전 승인 관문'에서 강제 방식을 '다섯 가지 강제 방식(에이전트 자율 준수·언어 모델 가드레일·결정적 위반 탐지·실시간 사용자 승인·AI 생성 강제 코드)'로 적어 '형식 검증 강제'를 쓰지 않았다.",
    "f3 표현 정정 — 3절과 8절의 RoboPAIR 문장을 '세 설정에서 종종(often) 100%에 이르는 공격 성공률을 보고했고'로 썼고, 4절 탈옥 용어와 용어집 설명에서도 무조건 100%로 읽히지 않게 했다.",
    "f16 기준일 정정 — 3절과 8절의 Li 외 서베이 문장에 'v5, 2026-05-03 개정 기준'을 적고, 13절 각주 ref-165 정의의 제목 뒤에 '(v5, 2026-05-03 개정)'을 병기했으며 reference_updates 요약에도 같은 판을 적었다.",
    "ref-863 발행일 정정 — 13절 각주와 reference_updates 의 발행일을 '미확인' 대신 2024-06-13 으로 적었고, 6절 EU AI Act 제12조 문장에 '규정 공식본 2024-06-13 기준'을 남겼다.",
    "원문 미열람 표기 유지 — ref-351·ref-840·ref-165·ref-753 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true, summary 를 '원문 미열람. '으로 시작하게 했다. 나머지 15건은 false 로 두었다.",
    "분량 초과 자동 분리: 13. 대화형 기능의 신뢰·기반 본문 14,247자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,311자"
  ]
}
```

### runs/2026-09-29-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area13-s6.md (3,607자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area13-s8.md (1,988자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area13-s11.md (1,562자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area13-s4.md (1,495자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area13-s10.md (1,267자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area13-s7.md (1,256자)
    - docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area13-s3.md (1,085자)
```

### runs/2026-09-29-06/pages/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [프롬프트 주입, 승인 관문, 불확실도 보정, 모델 대체, 대화 기록, 대화형 기능 평가]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-855, ref-856, ref-857, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863, ref-864, ref-865, ref-866, ref-738, ref-868, ref-869, ref-351, ref-840, ref-165, ref-753]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 13. 대화형 기능의 신뢰·기반

# 13. 대화형 기능의 신뢰·기반

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]

## 3. 왜 중요한가

언어 모델의 오해석뿐 아니라 프롬프트 주입·탈옥 같은 외부 조작이 도구 호출이나 로봇의 물리 동작으로 이어진다는 위협을 서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 각각 보고했다. [사실][^ref-855][^ref-857][^ref-859] 이 영역이 없으면 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 기능은 편리한 만큼 위험해진다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 왜 중요한가](../../topics/2026/2026-09-29-area13-s3.md)에 있다.

## 4. 핵심 개념과 용어

OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리한다. [사실][^ref-855] 아래 용어는 이 위험 목록과 그 방어·평가에서 이 영역이 자주 쓰는 것이다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area13-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 상업 시설

**사례:** 네덜란드 슈퍼마켓에서 고객의 음성 질의에 상품 위치·정보를 안내하고 회수 요청을 받는 로봇

| 항목 | 내용 |
|---|---|
| 시작 조건 | 매장 고객이 로봇에게 영어 또는 네덜란드어 음성으로 상품을 묻거나 상품 회수를 요청한다. [사실][^ref-869] |
| 작업 대상 | 1,612개 상품 데이터베이스의 상품 정보와 고객의 질의(정보와 사람). [사실][^ref-869] |
| 수행 자원 | 로봇이 음성 인식(네 가지 기술을 비교해 Whisper 채택 근거 확보), 질의 분류기, 상·중·하 세 층의 언어 모델로 답한다. 사람은 고객으로서 질문하고 답을 평가한다. [사실][^ref-869] |
| 제약 | 영어·네덜란드어 두 언어와 성별 집단에 따른 음성 인식 정확도 차이, 모든 응답이 상품 데이터베이스 항목에 근거해야 한다는 조건. [사실][^ref-869] |
| 완료·인계 | 질의 분류기가 의도를 분류하고 상품 데이터베이스 항목을 참조한 답이 고객에게 전달되면 한 질의가 끝난다. [사실][^ref-869] |
| 예외·성과 | Whisper 가 성별·언어 집단(참가자 40명)에서 가장 낮은 단어 오류율을 보였고, 질의 분류기 정확도는 약 87%, 다층 구조는 참가자 16명 평가에서 GPT-4 Turbo 보다 13개 항목 중 4개에서 유의하게 높았다. 오인식·오답 때의 복구 절차는 이번 조사에서 확인되지 않았다. [사실][^ref-869] |

이 사례는 Nandkumar·Peternel(Frontiers in Robotics and AI, 2025-04-29)이 보고한 실제 연구다. 다중 로봇 오케스트레이션이 아니라 로봇 한 대의 음성 대화 인터페이스를 다루지만, 이 영역의 세 가지 일이 한 현장에 함께 나타난다. 모든 응답을 상품 데이터베이스 항목에 근거하게 해 환각을 줄인 점은 오해석 방지·근거 표시에, 두 언어와 성별 집단으로 음성 인식 기술을 비교한 점은 음성·다국어·현장 단말 대화에, 단어 오류율·분류 정확도·사용자 평가로 결과를 잰 점은 대화형 기능 평가에 해당한다. [사실][^ref-869]

ROP 관점에서 여섯 항목 가운데 이 영역이 관여하는 칸은 수행 자원(음성 인식 엔진과 언어 모델을 어디에 어떻게 두는가), 제약(근거 응답 조건), 예외·성과(평가 지표)다. 물류창고·제조 공장·병원·가정·실외의 대화 기능 사례와 국내 현장 자료는 이번 조사에서 확인되지 않았다(11. 열린 질문 참조).

## 6. 대표 접근법과 기술

서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, 불확실도 보정 기반 되묻기로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다. [사실][^ref-351][^ref-864]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 규범 문서는 위협 목록(OWASP), 프로토콜 보안 원칙(MCP), 기록·개인정보 규제·안내서(EU AI Act, 개인정보보호위원회, TTA), 공개 벤치마크와 참조 구현으로 나뉜다. [사실][^ref-855][^ref-856][^ref-863] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area13-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 위협·방어 연구, 되묻기·검증 연구, 평가 벤치마크, 권한·승인 연구, 모델 공급망·음성·화면 연동 연구, 국내 안내서로 나뉜다. [사실][^ref-859][^ref-858]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료](../../topics/2026/2026-09-29-area13-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 해석 결과에 근거(장소·물품·문서 식별자)를 붙이고 불확실한 항목만 되묻는 흐름, 음성 인식 결과의 확인 절차, 언어 모델 출력의 검증·승인·기록 | 음성 인식 모델의 소음·다국어 강건성(Whisper 등), 언어 모델 공급자의 탈옥 방어·안전 학습 |
| 업종별 조건 | 대화 기록 자동 로그와 보존·보호 요구를 기록 항목·권한 제약으로 반영 | 고위험·고영향 AI 해당 여부 판단과 개인정보 법령 해석(59. 법·규제·보험·라이선스, 53. 개인정보·영상 데이터) |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 해석 결과에 근거를 붙이고 불확실한 항목만 되묻는 흐름, 도구 호출 수준의 권한 검사와 실행 전 승인 관문, 대화·도구 호출·실제 제공 모델의 기록, 모델 공급자 연결·교체 정책, 오류 유형별 평가 시나리오이며, 음성 인식 엔진의 정확도와 언어 모델 자체의 안전 정렬은 연계 대상으로 두는 것이 [분류 원문 19장의 경계](../../about/scope-boundary.md)에 맞을 것으로 보인다. [추정][^ref-856][^ref-868][^ref-865][^ref-866][^ref-858] MCP 명세가 도구 호출 전 동의를 프로토콜이 아니라 호스트의 책임으로 둔다는 점은 승인 관문이 ROP 쪽에 놓여야 한다는 판단을 뒷받침한다. [사실][^ref-856]

연계 대상은 짧게 다룬다. 음성 인식 모델의 소음·다국어 강건성과 언어 모델 공급자의 탈옥 방어·안전 학습은 원문 19장의 로봇 자체 지능 및 외부 도구 쪽이며, 이종 제조사를 잇는 ROP 는 인식 결과의 확인 절차와 모델 출력의 검증·승인·기록을 맡고 인식·모델 내부 성능은 공급자에게 맡겨야 할 것으로 보인다. [추정][^ref-866][^ref-869][^ref-857] 자사 로봇과 모델까지 만드는 제품 전략이라면 이 경계는 안쪽으로 이동할 수 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 C. 채팅 기반 구성·운영의 다섯 대화 영역이 공유하는 기반이며, 위협·방어·평가 연구는 원문 교차 규칙에 따라 L. AI·학습 기술의 해당 영역과, 권한·기록·개인정보는 N. 보안·개인정보의 영역과 함께 연결한다. [추정][^ref-858][^ref-857][^ref-863]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area13-s10.md)에 있다.

## 11. 열린 질문

기존 질문 여섯 건은 이번 실행에서 부분 진전만 있어 열림으로 둔다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 열린 질문](../../topics/2026/2026-09-29-area13-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-866]: Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E., Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems, 2026-07-13, https://arxiv.org/abs/2607.11792, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29
[^ref-869]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-09-29
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29 (원문 미열람)
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 13
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 13. 대화형 기능의 신뢰·기반

# 13. 대화형 기능의 신뢰·기반

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]

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

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s6.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-165, ref-351, ref-753, ref-855, ref-856, ref-857, ref-858, ref-860, ref-861, ref-862, ref-863, ref-864, ref-865, ref-866, ref-738, ref-868, ref-869]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#6
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술

# 13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, 불확실도 보정 기반 되묻기로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다. [사실][^ref-351][^ref-864]
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 오해석을 실행 전에 거르기: 되묻기와 자동 검증

서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, 불확실도 보정 기반 되묻기로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다. [사실][^ref-351][^ref-864] KnowNo(Ren 외, CoRL 2023)는 등각 예측으로 후보 행동 집합을 만들어 집합이 하나로 좁혀지면 실행하고 여러 개가 남으면 되묻는 틀로, 목표 성공률을 보장하면서 도움 요청을 줄였다고 보고했다. [사실][^ref-351] LBAP(Mullen·Manocha, 2024, 2025 개정)는 베이즈 추론으로 장면 근거(scene grounding)와 세계 지식을 함께 반영해 확신도를 보정함으로써 환각에 대응하며, 실제 환경 시험에서 성공률 70% 조건에서 이전 방법보다 사람 도움 요청률을 33% 넘게 줄였다고 보고했다. [사실][^ref-864]

되묻기와 별도로 계획 자체를 자동으로 검사하는 층도 있다. VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 [선형 시간 논리](../../glossary/linear-temporal-logic.md)로 옮긴 뒤 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 검증 모듈로, 승인 전에 계획을 자동으로 거르는 층의 사례다. [사실][^ref-753] 용어집: [사전 실행 계획 검증](../../glossary/pre-execution-plan-verification.md). 근거 표시 쪽에서는 슈퍼마켓 로봇 연구가 모든 응답을 상품 데이터베이스 항목에 근거하게 해 환각을 줄였다. [사실][^ref-869]

### 대화 권한과 실행 전 승인 관문

MCP 명세 2025-06-18 판의 보안과 신뢰·안전 절은 호스트가 어떤 도구든 호출하기 전에 사용자의 명시적 동의를 얻어야 하고, 도구 설명·주석은 신뢰할 수 있는 서버에서 온 것이 아니면 신뢰하지 말아야 하며, 프로토콜 자체는 이 원칙을 강제할 수 없으므로 구현자가 동의·인가 흐름을 응용 프로그램에 만들어야 한다고 적는다. [사실][^ref-856] 이 점과 탈옥이 배치된 로봇에서도 성공한다는 점을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이나 도구 서버 안이 아니라 ROP 쪽 호스트에 승인 관문을 두고, 도구 설명·검색 문서·현장 입력을 신뢰하지 않는 입력으로 다루어야 지켜질 것으로 보인다. [추정][^ref-856][^ref-857][^ref-855]

권한을 어떻게 적고 강제할지는 Michael·Roesner(2026)가 정리했다. 이들은 AI 에이전트의 사용자 수준 권한 제안 21건과 상용 에이전트 5종을 조사해 권한 정책 명세(자연어·권한 라벨·고정 선택지·구조화 제약·임의 규칙)와 다섯 가지 강제 방식(에이전트 자율 준수·언어 모델 가드레일·결정적 위반 탐지·실시간 사용자 승인·AI 생성 강제 코드)의 분류를 만들고, 상용 에이전트가 부담이 큰 실시간 승인과 투명성 없는 언어 모델 자동 검토 사이의 선택을 강요하며 낮은 사용자 부담·형식 근거·결정적 강제를 함께 갖춘 학술 시스템은 21건 중 하나도 없다고 보고했다. [사실][^ref-868] 이 분류와 승인 부담이 정량화되지 않았다는 지적, 호스트 책임의 동의 원칙을 함께 보면, 이 영역의 대화 권한은 프롬프트 안내가 아니라 도구 호출 수준에서 사용자·로봇·구역·작업 범위를 결정적으로 검사하는 정책으로 두고, 실행 전 승인은 위험도가 낮은 조회는 자동 허용하고 로봇을 움직이는 요청만 사람이 승인하는 식으로 단위를 나누어야 승인 피로를 줄일 수 있을 것으로 보이나, 로봇 대수·계획 크기에 따른 승인 단위를 정한 연구는 확인되지 않았다. [추정][^ref-868][^ref-165][^ref-856] 용어집: [역할 기반 접근 통제](../../glossary/role-based-access-control.md), [자동화 편향](../../glossary/automation-bias.md)

### 언어 모델 연결·교체와 대체 감사

Zhang·Zhang·Qin(2026)의 IRIS 는 언어 모델 게이트웨이가 광고한 모델 대신 더 싼 모델을 내보내는 모델 대체와 일부 요청만 약속한 백엔드로 보내는 라우팅 희석을 응답 텍스트만으로 감사하는 방법으로, 상용 라이브러리에서 희석을 평균 탐지력 0.85·오탐률 0.017 로 잡고, 교차 제공자 감사에서 같은 모델을 내는 제공자 쌍 15개 중 14개를 실제 양자화·커널 차이로 표시했다고 보고했다. [사실][^ref-865] 게이트웨이의 무단 대체·희석이 실제로 관측된다는 점과 OWASP 가 공급망을 위험 항목으로 둔 점을 함께 보면, 이 영역의 '모델 장애 때 임의로 다른 모델로 넘기지 않는다'는 요구는 ROP 가 요청·응답마다 실제 제공 모델 식별자를 기록하고, 대체를 사전에 정한 정책으로만 허용하며, 게이트웨이 계층의 대체를 감사하는 절차로 구현해야 할 것으로 보인다. [추정][^ref-865][^ref-855]

### 대화 기록의 보존·보호

EU AI Act 제12조(기록 보관)는 고위험 AI 시스템이 수명 기간 내내 사건을 자동으로 기록(로그)할 수 있어야 하고, 로그가 위험 상황 식별·시장 출시 후 모니터링·운영 모니터링에 필요한 사건을 담아 의도된 목적에 맞는 추적 가능성을 보장해야 한다고 규정한다(규정 공식본 2024-06-13 기준). [사실][^ref-863] 대화 기록의 보존·보호 요구는 이 조항과 국내 개인정보보호위원회 안내서, TTA 신뢰성 안내서에 근거를 둘 수 있으나, ROP 의 로봇 대화 기능이 고위험·고영향 AI 에 해당하는지와 로그 항목·보존 기간을 어떻게 정할지는 확인되지 않았다. [추정][^ref-863][^ref-862][^ref-860] 용어집: [감사 추적](../../glossary/audit-trail.md), [고영향 인공지능](../../glossary/high-impact-ai.md)

### 대화형 기능의 평가

Li 외(NeurIPS 2024 데이터셋·벤치마크 트랙)의 Embodied Agent Interface 는 체화 의사결정 과제를 목표 해석·하위 목표 분해·행동 순서화·전이 모델링의 네 모듈로 나누고, 최종 성공률 대신 환각 오류·어포던스 오류·여러 계획 오류를 구분하는 세분화 지표로 언어 모델을 평가한다. [사실][^ref-858] τ-bench 는 언어 모델이 흉내 내는 사용자와 도구·정책 지침을 가진 에이전트의 대화를 시뮬레이션해 대화 종료 시 데이터베이스 상태를 목표 상태와 비교하고, 같은 과제를 여러 번 시행해 모두 성공할 확률 pass^k 로 신뢰성을 잰다. [사실][^ref-738] 세분화 오류 지표, 반복 시행 신뢰성, 성공률 대비 도움 요청률을 함께 보면 이 영역의 평가는 해석·분해 정확도를 오류 유형별로 나누고 같은 과제를 여러 번 시행한 신뢰성과 질문 횟수를 성공률과 짝지어 재는 방식으로 구성할 수 있으나, 로봇 지도 작성·로봇 구성 대화에 특화된 벤치마크는 이번 조사에서 확인되지 않았다. [추정][^ref-858][^ref-738][^ref-864]

### 대화와 화면 편집의 연동

van Dam(2025)의 다중 모달 GUI 아키텍처는 응용 프로그램의 화면 이동 그래프와 의미를 MCP 로 노출하고, 뷰모델이 현재 보이는 화면에 적용되는 도구와 전역 도구를 언어 모델에 제공해 음성 입력과 시각 인터페이스의 정렬과 양쪽 모달리티의 일관된 피드백을 목표로 하며, 참조 구현(langbar)을 공개하고 로컬 배치 가능한 개방 가중치 모델이 전체 정확도에서 선도 상용 모델에 근접한다고 보고했다. [사실][^ref-861] 이 구조를 이 영역의 요구에 대응시키면, 지도에서 고른 장소·로봇을 대화가 참조하고 대화로 바꾼 값이 편집 화면에 바로 보이게 하려면 편집기의 현재 선택·화면 상태를 언어 모델에 자원으로 주고 변경은 같은 상태 저장소를 거치게 하는 구조가 필요할 것으로 보이나, 로봇 지도·시나리오 편집기에 특화된 공개 구현은 확인되지 않았다. [추정][^ref-861][^ref-856]

### 음성·다국어·현장 단말

Li 외(2026)의 서베이는 로봇 시스템의 음성 인식이 온라인 API 서비스에만 의존해야 하는지를 물으며, Whisper 같은 심층 학습 모델까지의 발전과 ROS 기반·클라우드 기반·혼합 배치 전략, 다양하고 동적인 환경에서 강건한 음성 인식을 배치하는 과제를 정리했다. [사실][^ref-866] 현장 비교로는 슈퍼마켓 로봇 연구가 네 가지 음성 인식 기술을 영어·네덜란드어와 성별 집단으로 비교해 Whisper 가 가장 낮은 단어 오류율을 보였다고 보고했다. [사실][^ref-869] 소음·한국어 조건의 인식률과 오인식 시 확인 절차는 이번 조사에서 확인되지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey (v5, 2026-05-03 개정), 2025-02-06, https://arxiv.org/abs/2502.03814, 접근일 2026-09-29 (원문 미열람)
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29 (원문 미열람)
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29 (원문 미열람)
[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-860]: 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기), 2024-02, https://tta-trustworthy-ai.gitbook.io/general, 접근일 2026-09-29
[^ref-861]: van Dam, H. G. W., A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants, 2025-10-09, https://arxiv.org/abs/2510.06223, 접근일 2026-09-29
[^ref-862]: 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.), 2025-08, https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-866]: Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E., Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems, 2026-07-13, https://arxiv.org/abs/2607.11792, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29
[^ref-869]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s8.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-165, ref-351, ref-753, ref-840, ref-857, ref-858, ref-859, ref-860, ref-861, ref-862, ref-864, ref-865, ref-866, ref-738, ref-868, ref-869]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#8
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료

# 13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 자료는 위협·방어 연구, 되묻기·검증 연구, 평가 벤치마크, 권한·승인 연구, 모델 공급망·음성·화면 연동 연구, 국내 안내서로 나뉜다. [사실][^ref-859][^ref-858]
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 자료는 위협·방어 연구, 되묻기·검증 연구, 평가 벤치마크, 권한·승인 연구, 모델 공급망·음성·화면 연동 연구, 국내 안내서로 나뉜다. [사실][^ref-859][^ref-858]

- Robey, A. 외, Jailbreaking LLM-Controlled Robots(2024) — RoboPAIR 로 세 설정의 언어 모델 제어 로봇을 탈옥시켜 종종 100%에 이르는 공격 성공률과 배치된 상용 로봇의 첫 탈옥을 보고했다. 대화 기능의 출력이 물리 동작이 되는 위험의 직접 근거다. [사실][^ref-857]
- Huang, X. 외, Trust in LLM-controlled Robotics(2025) — 체화 격차를 중심으로 탈옥·백도어·다중 모달 프롬프트 주입의 공격 분류와 형식 안전 명세·런타임 강제·다중 언어 모델 감독·프롬프트 강화의 방어 분류, 평가 데이터셋·벤치마크를 정리한 서베이다. [사실][^ref-859]
- Ren, A. Z. 외, Robots That Ask For Help(CoRL 2023) — 등각 예측으로 불확실도를 보정하는 KnowNo. 되묻기의 통계적 근거를 준 연구다. [사실][^ref-351]
- Mullen, J. F., Jr. & Manocha, D., Towards Robots That Know When They Need Help(2024, 2025 개정) — 장면 근거와 세계 지식을 결합한 LBAP 로 성공률 70%에서 도움 요청률을 33% 넘게 줄였다. [사실][^ref-864]
- Grigorev, D. S. 외, VerifyLLM(IROS 2025) — 실행 전 계획 검증 모듈. 승인 전에 계획을 자동으로 거르는 층의 사례다. [사실][^ref-753]
- Li, M. 외, Embodied Agent Interface(NeurIPS 2024) — 오류 유형을 구분하는 세분화 평가 벤치마크. 해석·분해 정확도 지표의 출발점이다. [사실][^ref-858]
- Yao, S. 외, τ-bench(2024) — 시뮬레이션 사용자 기반 평가와 pass^k. GPT-4o 도 과제 성공률 50% 미만, 소매 pass^8 25% 미만이었다. [사실][^ref-738]
- Laban, P. 외, LLMs Get Lost In Multi-Turn Conversation(2025) — 다중 턴 성능이 단일 턴보다 평균 39% 낮고 원인이 신뢰성 저하임을 보고했다. [사실][^ref-840]
- Michael, A. E. & Roesner, F., How Agents Ask for Permission(2026) — 권한 명세와 강제 방식의 분류, 실시간 승인 부담과 자동 검토 불투명성의 상충. [사실][^ref-868]
- Li, P. 외, Large Language Models for Multi-Robot Systems: A Survey(2025, v5 2026-05-03 개정) — 사람 개입의 반응적 역할과 운영자 인지 부담 미정량화를 빈틈으로 지적했다. [사실][^ref-165]
- Zhang, Y. 외, IRIS(2026) — 게이트웨이의 모델 대체·라우팅 희석을 응답 텍스트만으로 감사한다. [사실][^ref-865]
- Li, S. 외, Casting Everything to Online API Services?(2026) — 로봇 음성 인식의 온라인 API 의존과 로컬·혼합 배치를 정리한 서베이다. [사실][^ref-866]
- Nandkumar, C. & Peternel, L., Enhancing supermarket robot interaction(Frontiers in Robotics and AI, 2025) — 다국어 음성 인식 비교와 상품 데이터베이스 근거 다층 언어 모델의 사용자 평가. 이 영역의 유일한 현장 사례다. [사실][^ref-869]
- van Dam, H. G. W., A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants(2025) — 화면 상태를 MCP 로 노출해 음성·화면을 맞추는 아키텍처와 참조 구현. [사실][^ref-861]
- 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) — 국내 대화 기록 개인정보 처리의 기준 문서. [사실][^ref-862]
- 과학기술정보통신부·TTA, 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 — 국내 AI 신뢰성 확보 방안 안내서. [사실][^ref-860]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey (v5, 2026-05-03 개정), 2025-02-06, https://arxiv.org/abs/2502.03814, 접근일 2026-09-29 (원문 미열람)
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29 (원문 미열람)
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29 (원문 미열람)
[^ref-840]: Laban, P., Hayashi, H., Zhou, Y., & Neville, J., LLMs Get Lost In Multi-Turn Conversation, 2025-05-09, https://arxiv.org/abs/2505.06120, 접근일 2026-09-29 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-860]: 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기), 2024-02, https://tta-trustworthy-ai.gitbook.io/general, 접근일 2026-09-29
[^ref-861]: van Dam, H. G. W., A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants, 2025-10-09, https://arxiv.org/abs/2510.06223, 접근일 2026-09-29
[^ref-862]: 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.), 2025-08, https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-866]: Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E., Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems, 2026-07-13, https://arxiv.org/abs/2607.11792, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29
[^ref-869]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s11.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 열린 질문"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-165, ref-856, ref-858, ref-859, ref-860, ref-862, ref-863, ref-864, ref-865, ref-866, ref-738, ref-868, ref-869]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#11
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 열린 질문

# 13. 대화형 기능의 신뢰·기반 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기존 질문 여섯 건은 이번 실행에서 부분 진전만 있어 열림으로 둔다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기존 질문 여섯 건은 이번 실행에서 부분 진전만 있어 열림으로 둔다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-125** (상태: 열림) 언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? — 세분화 오류 지표·pass^k·도움 요청률로 구성할 수 있다는 추정까지 진전했으나 특화 벤치마크는 확인되지 않았다. [추정][^ref-858][^ref-738][^ref-864]
- **oq-127** (상태: 열림) 대화로 로봇 종류·대수·장비·역할을 정하고 수행 가능 여부를 판정하는 기능을 평가할 공개 벤치마크나 지표가 있는가? — 위와 같은 상태다.
- **oq-133** (상태: 열림) 대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가? — 이번 실행에서 조사하지 않았다.
- **oq-136** (상태: 열림) 대화로 정한 시나리오에서 사용자가 확정한 값과 모델이 추정한 값을 구분해 저장·표시하고 턴마다 바뀐 부분만 보여 주는 공개 데이터 형식이나 편집기 구현이 있는가? — 이번 실행에서 조사하지 않았다.
- **oq-139** (상태: 열림) 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위를 정한 공개 연구나 지침이 있는가? — 권한 강제 방식의 분류와 인지 부담 미정량화 지적으로 부분 진전했으나 승인 단위를 정한 연구는 확인되지 않았다. [사실][^ref-868][^ref-165]
- **oq-141** (상태: 열림) 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지 공개 구현이나 운영 사례가 있는가? — MCP 명세가 동의를 호스트 책임으로 둔다는 점까지 확인했으나 공개 구현은 확인되지 않았다. [사실][^ref-856]
- **새 질문** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-06) ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? [추정][^ref-863][^ref-862][^ref-860]
- **새 질문** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-06) 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? [사실][^ref-859]
- **새 질문** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-06) 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? [사실][^ref-865]
- **새 질문** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-06) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다. [사실][^ref-866][^ref-869]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey (v5, 2026-05-03 개정), 2025-02-06, https://arxiv.org/abs/2502.03814, 접근일 2026-09-29 (원문 미열람)
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-860]: 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기), 2024-02, https://tta-trustworthy-ai.gitbook.io/general, 접근일 2026-09-29
[^ref-862]: 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.), 2025-08, https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-866]: Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E., Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems, 2026-07-13, https://arxiv.org/abs/2607.11792, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29
[^ref-869]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s4.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-351, ref-855, ref-856, ref-857, ref-858, ref-859, ref-864, ref-865, ref-738, ref-868]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#4
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어

# 13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리한다. [사실][^ref-855] 아래 용어는 이 위험 목록과 그 방어·평가에서 이 영역이 자주 쓰는 것이다.
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리한다. [사실][^ref-855] 아래 용어는 이 위험 목록과 그 방어·평가에서 이 영역이 자주 쓰는 것이다.

- **프롬프트 주입(Prompt Injection)** — 사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격이다. OWASP 목록은 사용자 프롬프트가 의도치 않은 방식으로 모델 행동을 바꾸는 위험을 첫 항목(LLM01)으로 둔다. [사실][^ref-855]
- **과도한 에이전시(Excessive Agency)** — 언어 모델 기반 시스템에 필요 이상의 기능·권한·자율이 주어진 상태로, 같은 목록의 LLM06 항목이다. [사실][^ref-855] 용어집: [과도한 에이전시](../../glossary/excessive-agency.md)
- **탈옥(Jailbreak)** — 언어 모델의 안전 제한을 우회하도록 유도하는 입력 기법이다. 로봇을 제어하는 언어 모델에서는 유해한 물리 동작을 끌어내는 데 쓰였다. [사실][^ref-857]
- **체화 격차(embodiment gap)** — 추상 추론과 물리 동작 사이의 간격으로, Huang 외(2025)의 서베이가 언어 모델 제어 로봇의 공격 벡터·방어 분류의 중심에 둔 개념이다. [사실][^ref-859]
- **불확실도 보정 기반 되묻기** — [등각 예측](../../glossary/conformal-prediction.md)이나 베이즈 추론으로 언어 모델 계획기의 확신도를 보정해, 확신이 없을 때만 사람에게 되묻는 설계다. 서로 다른 두 연구 그룹(KnowNo, LBAP)이 각각 보고했다. [사실][^ref-351][^ref-864] 용어집: [불확실도 정렬](../../glossary/uncertainty-alignment.md), [명확화 질문](../../glossary/clarification-question.md), [사람 참여 루프](../../glossary/human-in-the-loop.md)
- **환각 오류·어포던스 오류·계획 오류** — Embodied Agent Interface 가 최종 성공률 대신 구분해 재는 오류 유형이다. [사실][^ref-858] 용어집: [환각](../../glossary/hallucination.md), [어포던스](../../glossary/affordance.md)
- **pass^k** — 같은 과제를 여러 번 시행해 모두 성공할 확률로 반복 신뢰성을 재는 지표로, τ-bench 가 제안했다. [사실][^ref-738] 용어집: [pass^k 지표](../../glossary/pass-k.md), [사용자 시뮬레이터](../../glossary/user-simulator.md)
- **승인 피로(Approval Fatigue)** — 동작마다 사람에게 승인을 묻는 방식이 반복되어 검토 없이 허용하거나 자동 승인으로 바꾸게 되는 현상이다. Michael·Roesner(2026)는 실시간 사용자 승인을 부담이 큰 강제 방식으로 분류했다. [사실][^ref-868]
- **모델 대체·라우팅 희석(Model Substitution / Routing Dilution)** — 언어 모델 게이트웨이가 광고한 모델 대신 더 싼 모델을 내보내거나(대체) 일부 요청만 약속한 백엔드로 보내는(희석) 현상이다. [사실][^ref-865]
- **모델 컨텍스트 프로토콜(Model Context Protocol, MCP)** — 언어 모델 응용 프로그램이 도구·자원을 부르는 개방 명세다. 2025-06-18 판의 보안 절은 호스트가 어떤 도구든 호출하기 전에 사용자의 명시적 동의를 얻어야 한다고 적는다. [사실][^ref-856] 용어집: [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29 (원문 미열람)
[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s10.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 다른 연구영역과의 연결"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-857, ref-858, ref-863]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#10
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 다른 연구영역과의 연결

# 13. 대화형 기능의 신뢰·기반 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 C. 채팅 기반 구성·운영의 다섯 대화 영역이 공유하는 기반이며, 위협·방어·평가 연구는 원문 교차 규칙에 따라 L. AI·학습 기술의 해당 영역과, 권한·기록·개인정보는 N. 보안·개인정보의 영역과 함께 연결한다. [추정][^ref-858][^ref-857][^ref-863]
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 C. 채팅 기반 구성·운영의 다섯 대화 영역이 공유하는 기반이며, 위협·방어·평가 연구는 원문 교차 규칙에 따라 L. AI·학습 기술의 해당 영역과, 권한·기록·개인정보는 N. 보안·개인정보의 영역과 함께 연결한다. [추정][^ref-858][^ref-857][^ref-863]

- [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) — 지도 요소 대화의 해석 정확도·확인 질문 횟수 평가(oq-125)와 화면 선택–대화 연동이 이 영역의 평가·연동 기반에 기댄다.
- [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) — 사용자가 확정한 값과 모델이 추정한 값의 구분 표시(oq-136)는 이 영역의 근거 표시 요구다.
- [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md) — 적합성 판정 정확도·질문 횟수 지표(oq-127)를 이 영역의 평가 방식으로 잰다.
- [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 시뮬레이션 결과 해석 오류를 막는 검증·승인 절차(oq-133)가 이 영역의 승인 관문과 이어진다.
- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 호스트 쪽 승인 관문과 신뢰하지 않는 입력 처리(oq-139·oq-141)를 이 영역이 뒷받침한다.
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 불확실도 보정·되묻기(KnowNo, LBAP)와 탈옥 공격·방어(RoboPAIR, Huang 외)는 이 영역에 속하는 연구 방법이다.
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 모델 공급자 선택·교체와 게이트웨이 대체 감사는 모델 운영의 일부다.
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 도구 호출 수준의 결정적 권한 강제와 사용자·로봇·구역·작업 범위 제한.
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 프롬프트 주입·탈옥 위협 목록과 자동 로그의 감사 요건.
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 대화 기록의 개인정보 처리(개인정보보호위원회 안내서).
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — Embodied Agent Interface·τ-bench 같은 벤치마크와 실행 전 형식 검증.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 언어 모델이 관제 작업 API 를 부를 때 승인 관문을 두는 위치(oq-141).
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 탈옥이 유해한 물리 동작으로 이어지는 위험의 위험성 평가.
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 모델 교체 정책과 제공 모델 식별자 기록.
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — EU AI Act 고위험 AI 와 국내 고영향 인공지능 해당 여부.
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 슈퍼마켓 로봇 음성 대화 사례.
- 관련 트랙: [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 오해석 방지 장치 단계가 이 영역과 겹친다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s7.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-753, ref-855, ref-856, ref-858, ref-860, ref-861, ref-862, ref-863, ref-738]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#7
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 관련 표준·프레임워크·오픈소스

# 13. 대화형 기능의 신뢰·기반 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 규범 문서는 위협 목록(OWASP), 프로토콜 보안 원칙(MCP), 기록·개인정보 규제·안내서(EU AI Act, 개인정보보호위원회, TTA), 공개 벤치마크와 참조 구현으로 나뉜다. [사실][^ref-855][^ref-856][^ref-863] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 규범 문서는 위협 목록(OWASP), 프로토콜 보안 원칙(MCP), 기록·개인정보 규제·안내서(EU AI Act, 개인정보보호위원회, TTA), 공개 벤치마크와 참조 구현으로 나뉜다. [사실][^ref-855][^ref-856][^ref-863] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| OWASP Top 10 for LLM Applications 2025 | 프레임워크 | 프롬프트 주입·민감 정보 노출·공급망·부적절한 출력 처리·과도한 에이전시·잘못된 정보를 포함한 열 가지 위험 목록. 대화 기능의 위협 점검표로 쓸 수 있다 | [사실][^ref-855] |
| Model Context Protocol 명세 2025-06-18 (보안과 신뢰·안전 절) | 표준(오픈소스 명세) | 도구 호출 전 사용자 동의, 도구 설명 불신, 구현자의 동의·인가 흐름 책임을 정한다 | [사실][^ref-856] |
| EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689) | 법규(EU 규정) | 고위험 AI 시스템의 수명 기간 자동 사건 기록과 추적 가능성 요건. 대화 기록 자동 로그의 근거 후보 | [사실][^ref-863] |
| 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) | 프레임워크(정부 안내서) | 개인정보보호위원회가 생성형 AI 수명주기 각 단계의 개인정보 처리·보호 이슈를 체계화하고 법적 기준과 안전조치를 제시(공식 사이트 게시 2025-08-22). 안내서 PDF 본문은 미열람 | [사실][^ref-862] |
| 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 | 프레임워크(정부 안내서) | 과학기술정보통신부·TTA 가 2024년 2월 발간, 웹 문서로 2025-08-14까지 갱신. 기술적 신뢰성 확보 방안을 다루며 2024년 생성 AI 기반 서비스 분야 안내서가 함께 나왔다 | [사실][^ref-860] |
| Embodied Agent Interface | 평가 프로그램 | 목표 해석·하위 목표 분해·행동 순서화·전이 모델링 네 모듈과 환각·어포던스·계획 오류 세분화 지표 | [사실][^ref-858] |
| τ-bench | 평가 프로그램 | 시뮬레이션 사용자와 도구·정책 에이전트의 대화를 최종 데이터베이스 상태로 판정하고 pass^k 로 반복 신뢰성을 잰다 | [사실][^ref-738] |
| VerifyLLM | 오픈소스 | 자연어 지시를 선형 시간 논리로 옮겨 실행 전에 계획의 일관성·누락 단계를 검사하는 모듈, 코드 공개 | [사실][^ref-753] |
| langbar | 오픈소스 | 화면 이동 그래프와 의미를 MCP 로 노출해 음성 대화와 GUI 를 맞추는 아키텍처의 참조 구현 | [사실][^ref-861] |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29 (원문 미열람)
[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-860]: 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기), 2024-02, https://tta-trustworthy-ai.gitbook.io/general, 접근일 2026-09-29
[^ref-861]: van Dam, H. G. W., A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants, 2025-10-09, https://arxiv.org/abs/2510.06223, 접근일 2026-09-29
[^ref-862]: 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.), 2025-08, https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-06/pages/topics/2026/2026-09-29-area13-s3.md

```markdown
---
title: "13. 대화형 기능의 신뢰·기반 — 왜 중요한가"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-165, ref-840, ref-855, ref-857, ref-859, ref-738, ref-868]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#3
---

[홈](../../index.md) › [주제](../index.md) › 13. 대화형 기능의 신뢰·기반 — 왜 중요한가

# 13. 대화형 기능의 신뢰·기반 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 언어 모델의 오해석뿐 아니라 프롬프트 주입·탈옥 같은 외부 조작이 도구 호출이나 로봇의 물리 동작으로 이어진다는 위협을 서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 각각 보고했다. [사실][^ref-855][^ref-857][^ref-859] 이 영역이 없으면 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 기능은 편리한 만큼 위험해진다.
- 이 페이지는 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

언어 모델의 오해석뿐 아니라 프롬프트 주입·탈옥 같은 외부 조작이 도구 호출이나 로봇의 물리 동작으로 이어진다는 위협을 서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 각각 보고했다. [사실][^ref-855][^ref-857][^ref-859] 이 영역이 없으면 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 기능은 편리한 만큼 위험해진다. 2절의 핵심 질문, 곧 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가는 이 위협에서 출발한다.

위협은 실험실 밖에서도 확인됐다. Robey 외(2024)의 RoboPAIR 는 언어 모델로 제어되는 로봇을 탈옥시키는 알고리즘으로, 자율주행 언어 모델(화이트박스), GPT-4o 계획기를 단 Clearpath Jackal(그레이박스), Unitree Go2 로봇 개(블랙박스)의 세 설정에서 종종(often) 100%에 이르는 공격 성공률을 보고했고, 배치된 상용 로봇 시스템에 대한 첫 탈옥 성공이라고 밝혔다(2024-11-09 개정 기준). [사실][^ref-857]

대화가 길어질수록 오해석 위험은 커진다. Laban 외(2025)는 20만 건 이상의 시뮬레이션 대화에서 언어 모델의 다중 턴 성능이 단일 턴보다 평균 39% 낮았고, 원인이 초기 가정에 대한 과도한 의존 같은 신뢰성 저하라고 보고했다. [사실][^ref-840] 도구를 부르는 에이전트의 반복 신뢰성도 낮다. Yao 외(2024)의 τ-bench 에서는 GPT-4o 같은 최신 함수 호출 에이전트도 과제 성공률이 50% 미만이고 소매 도메인의 pass^8 이 25% 미만이었다(2024-06-17 기준). [사실][^ref-738]

사람의 승인을 두는 것만으로 끝나지도 않는다. Michael·Roesner(2026)는 상용 에이전트가 부담이 큰 실시간 승인과 투명성 없는 언어 모델 자동 검토 사이의 선택을 강요한다고 보고했다. [사실][^ref-868] Li 외(2025)의 다중 로봇 언어 모델 서베이는 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머물고, 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다고 지적했다(v5, 2026-05-03 개정 기준). [사실][^ref-165] 그래서 이 영역은 모델 밖에 검증·승인·권한·기록 층을 두는 방법과, 그 층이 사람에게 지우는 부담을 함께 다룬다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey (v5, 2026-05-03 개정), 2025-02-06, https://arxiv.org/abs/2502.03814, 접근일 2026-09-29 (원문 미열람)
[^ref-840]: Laban, P., Hayashi, H., Zhou, Y., & Neville, J., LLMs Get Lost In Multi-Turn Conversation, 2025-05-09, https://arxiv.org/abs/2505.06120, 접근일 2026-09-29 (원문 미열람)
[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-738]: Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra), τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains, 2024-06-17, https://arxiv.org/abs/2406.12045, 접근일 2026-09-29
[^ref-868]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-06 | 13. 대화형 기능의 신뢰·기반 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 854건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 223개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
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

### docs/open-questions.md (요약: 대상 영역 [13] 에 걸린 6건 / 전체 142건)

```markdown
- oq-125 [열림] 언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? (영역 8, 13)
- oq-127 [열림] 대화로 로봇 종류·대수·장비·역할을 정하고 수행 가능 여부를 판정하는 기능을 평가할 공개 벤치마크나 지표(적합성 판정 정확도, 질문 횟수, 구성 완료 시간)가 있는가? (영역 10, 13)
- oq-133 [열림] 대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가? (영역 11, 13)
- oq-136 [열림] 대화로 정한 시나리오에서 사용자가 확정한 값과 모델이 추정한 값을 구분해 저장·표시하고 턴마다 바뀐 부분만 보여 주는 공개 데이터 형식이나 편집기 구현이 있는가? (영역 9, 13)
- oq-139 [열림] 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? (영역 12, 13)
- oq-141 [열림] 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? (영역 12, 20, 13)
```
