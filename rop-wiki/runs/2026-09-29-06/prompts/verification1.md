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
- verification_stage: first
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
        "ref-867"
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
        "ref-867",
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
        "ref-841"
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
      "id": "ref-867",
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
      "id": "ref-841",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-855~ref-869, 예약 구간 안) 상한 도달로 위 미확인 항목의 후보 출처(OpenTelemetry GenAI 규약, MiniScope, CURE, 산업 음성 제어 사례)를 넣지 못했다. 원문 열람 15건(webfetch 15; ref-868 은 arXiv HTML 전문, ref-869 는 PMC 전문, 나머지 논문은 arXiv 초록 페이지), 재사용 4건(ref-351·ref-841·ref-165·ref-753, 이전 브리프 2026-09-29-04·05 의 값 그대로, 이번에 다시 열지 않음). 이전 실행 2026-09-29-05 가 ref-855~ref-862 로 낸 출처(HMCF, ETRI 동향, ROSA, OSRA MCP 세션 등)는 이번 실행의 예약 구간과 번호가 겹치고 참고문헌 목록 입력(0건 요약)에 없어 재사용하지 않았으며, 그 가운데 OSRA Interop SIG MCP 세션(oq-141 근거)은 이번 finding 에 넣지 않았다 — 퍼블리셔가 URL 로 합칠 때 번호 충돌을 확인해야 한다. 교차 확인 2건(f5: OWASP·Robey 외·Huang 외, f12: KnowNo·LBAP — 모두 발행 주체가 다름). 모든 finding 신뢰도 medium 이하(high 신뢰도 출처 ref-856·ref-860·ref-863·ref-869 는 각각 단일 출처 finding 에만 쓰임). 분류 원문 핵심 질문(해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면)에는 f2·f6(호스트 쪽 승인 관문과 신뢰하지 않는 입력 처리), f7·f10·f11·f12(실행 전 자동 검증과 불확실도 보정 되묻기), f15·f17(도구 호출 수준의 결정적 권한 강제), f18·f21(자동 기록), f22·f23(모델 대체 감사)로 답했으며 결론은 '모델 밖의 검증·승인·권한·기록 층이 필요하고 승인 단위와 부담은 아직 정량화되지 않았다'는 추정(f6·f13·f17·f23·f28)이다. 현장 유형: 상업 시설(f25, 네덜란드 슈퍼마켓 연구)만 확인했고 물류창고·제조 공장·병원·가정·실외 사례는 없다. 국내 자료는 TTA 안내서(f20)와 개인정보위 안내서(f19) 두 건이며 국내 로봇 대화 기능 사례는 찾지 못했다. L. AI·학습 기술 관련 finding(f3·f4·f8·f10·f11·f30)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처 없음(OWASP 는 업계 보고서, MCP 명세는 오픈소스 문서로 분류). 용어집에 이미 있는 환각·과도한 에이전시·사람 참여 루프·모델 컨텍스트 프로토콜·구조화 출력·제약 디코딩·등각 예측·불확실도 정렬·자동화 편향·역할 기반 접근 통제·감사 추적·pass^k·사용자 시뮬레이터·명확화 질문은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음."
  }
}
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

### docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md (요약)

```markdown
# 8. 채팅으로 맵 작성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md (요약)

```markdown
# 10. 채팅으로 로봇 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md (요약)

```markdown
# 12. 채팅으로 업무 지시·오케스트레이션

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
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

### runs/2026-09-29-05/research.md

```markdown
# 리서치 브리프 2026-09-29-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-05 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 사전 실행 계획 검증·감독 제어·실패 설명·로봇–작업 적합도 행렬 용어 없음(작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청·작업 상태 스키마, MCP 기반 관제 연결, ROSA·RobotFleet 같은 오픈소스 에이전트 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 짝 연결 필요, 13. 대화형 기능의 신뢰·기반·32. 예외 복구·재계획·업무 연속성·37. 관제 화면·실행 기록 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. 언어 모델이 자연어 업무 지시를 여러 이기종 로봇의 하위 작업으로 분해하고 의존 관계·능력에 맞춰 배정·일정을 제안하는 연구는 무엇이 있고 결과는 어떻게 보고되는가? (섹션 4·6·8 겨냥)
3. 언어 모델이 만든 계획을 실행 전에 자동 검증하고 사람이 승인하게 하는 설계(사전 실행 검증, 감독 제어)는 어떤 것이 있으며 승인 부담은 어떻게 다뤄지는가? (섹션 3·6·11 겨냥)
4. 어디까지 했는지·왜 멈췄는지를 대화로 묻고 실행 기록을 근거로 답하는 연구와, 관제가 제공하는 작업 상태·단계·사건 기록은 무엇인가? (섹션 4·6·7 겨냥)
5. 관제·플랫폼의 작업 요청 API 와 언어 모델 도구 호출(MCP)을 잇는 오픈소스·프레임워크는 무엇이고 승인 단계를 두는가? (섹션 7 겨냥)
6. 병원·제조 공장·물류창고·실외 등 현장 유형별로 대화로 로봇 업무를 지시한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
7. 채팅 업무 지시에서 ROP가 직접 맡을 것(대화→계획, 검증, 승인, 관제 작업 요청, 진행 설명)과 로봇 수준 코드 생성·스킬 실행·형식 최적화기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Li 외(2025)의 서베이는 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정, 중간 수준 동작 계획, 하위 수준 행동 생성, 사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. | ref-165 | 아니오 | medium | 2025-02-06 | — | — |
| f2 | [사실] | Li 외(2025) 서베이의 사람 개입 절은 실행 전에 사람이 계획을 승인하는 방식(Hunt 외), 로봇이 막히면 도움을 요청하는 방식(VADER), 환각을 줄이는 사람 검증 방식(Li 외)을 예로 들고, 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머문다는 점과 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다는 점을 빈틈으로 지적했다. | ref-165 | 아니오 | medium | 2026-05-03 | 제약 | — |
| f3 | [사실] | SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. | ref-090 | 아니오 | medium | 2023-09-18 | — | — |
| f4 | [사실] | DART-LLM(Wang 외, 2024)은 자연어 지시를 방향 비순환 그래프(DAG)로 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀로, 질의응답형 분해 모듈·로봇 배정 함수·구동 모듈·시각-언어 물체 탐지 모듈로 구성되며 세 복잡도 수준에서 DeepSeek-r1-671B 가 최고 성공률을, Llama-3.1-8B 가 응답 시간 안정성을 보였고 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다고 보고했다. | ref-059 | 아니오 | medium | 2024-11-13 | — | — |
| f5 | [사실] | FLEET(Rivera 외, 2025)은 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 능력을 반영한 로봇–작업 적합도 행렬을 만들고, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀어 배정하는 2단계 혼합 방식으로, 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했으며 능력이 다른 사족 로봇 실기로 검증했다. | ref-242 | 아니오 | medium | 2025-10-08 | 수행 자원 | — |
| f6 | [사실] | 서로 다른 세 연구 그룹(SMART-LLM, DART-LLM, FLEET)이 자연어 업무 지시를 언어 모델로 하위 작업으로 분해하고 이기종 로봇에 배정하는 방법을 각각 보고해, '대화 지시→분해→배정' 접근이 한 곳 이상에서 확인된다. | ref-090, ref-059, ref-242 | 예 | medium | 2025-10-08 | — | — |
| f7 | [추정] | FLEET 가 배정·일정은 형식 최적화기에 맡기고 언어 모델은 작업 그래프·능력 매칭에만 쓴 점(f5)과 DART-LLM 이 의존 관계를 DAG 로 명시한 점(f4)을 함께 보면, 이 영역의 '업무 파악·분해·배정·일정 제안'은 언어 모델이 대화를 의존 관계 있는 작업 그래프와 능력 요구로 바꾸고, 실제 배정·일정은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 엔진에 넘겨 계산한 결과를 계획으로 제안하는 혼합 구조가 원문 주석의 짝 연결과 맞을 것으로 보인다. | ref-242, ref-059 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f8 | [사실] | VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈로, 복잡도가 다른 가정 작업 데이터셋에서 시험했으며 코드를 공개했다. | ref-753 | 아니오 | medium | 2025-07-07 | 가정 / 제약 | — |
| f9 | [사실] | HMCF(Li 외, 2025)는 로봇마다 자기 능력을 이해하고 작업을 실행 가능한 지시로 바꾸는 언어 모델 에이전트를 두고, 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀로, 시뮬레이션에서 기존 계획 방법보다 작업 성공률을 4.76% 높이고 실제 환경에서 최소한의 사람 개입으로 제로샷 일반화를 보였다고 보고했다. | ref-855 | 아니오 | medium | 2025-05-01 | 예외·성과 | — |
| f10 | [사실] | 서로 다른 세 연구 그룹(Li 외 서베이가 정리한 Hunt 외의 실행 전 승인, HMCF 의 작업 검증·사람 감독, VerifyLLM 의 자동 사전 검증)이 언어 모델이 만든 로봇 계획을 실행 전에 검증하거나 사람이 승인하게 하는 설계를 각각 보고해, '실행 전 검증·승인' 접근이 한 곳 이상에서 확인된다. | ref-165, ref-855, ref-753 | 예 | medium | 2026-05-03 | 시작 조건 | — |
| f11 | [추정] | 자동 사전 검증(f8)과 사람 승인(f2·f9·f10)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이 낸 계획을 먼저 자동 검증(의존 관계·능력·논리 일관성)으로 걸러 승인자에게는 검토 가능한 구조(작업 그래프·배정·일정)로 보여 주는 방식으로 구현해야 서베이가 지적한 운영자 인지 부담을 줄일 수 있을 것으로 보인다. | ref-165, ref-753, ref-855 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f12 | [사실] | CoMuRoS(Borate 외, 2025)는 중앙 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 작업 이력·로봇 상태 같은 동적 정보로 일을 배정하고, 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 만들며, 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획해 로봇이 동료를 돕거나 중단된 작업을 재개하거나 사람 도움을 요청하게 하는 중앙 숙고·분산 실행 구조로, 실기에서 협업 복구 9/10·협동 운반 8/8·사람 보조 복구 5/5, 22개 시나리오 벤치마크에서 정확도 최대 0.91 을 보고했다. | ref-677 | 아니오 | medium | 2025-11-27 | 예외·성과 | — |
| f13 | [사실] | Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다. | ref-857 | 아니오 | medium | 2025-09-19 | 실외 / 완료·인계 | — |
| f14 | [사실] | REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하는 틀로, 다양한 작업·실패 시나리오를 담은 RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다. | ref-453 | 아니오 | medium | 2023-06-27 | 예외·성과 | — |
| f15 | [사실] | 서로 다른 두 연구 그룹(REFLECT, Argenziano 외)이 로봇의 실행 기록·경험 요약을 근거로 언어 모델이 무엇을 했고 왜 실패했는지를 자연어로 설명하거나 질의에 답하게 하는 방법을 각각 보고해, '실행 기록 근거의 진행·실패 설명' 접근이 한 곳 이상에서 확인된다. | ref-453, ref-857 | 예 | medium | 2025-09-19 | 완료·인계 | — |
| f16 | [추정] | 실행 기록 근거의 설명 연구(f14·f15)와 Open-RMF 작업 상태 스키마가 단계·사건·추정 시간·배정 로봇을 담는 점(f17)을 함께 보면, 이 영역의 '채팅으로 진행 상황 질의·결과 설명'은 언어 모델의 대화 기억이 아니라 관제의 작업 상태·단계 사건 기록(37. 관제 화면·실행 기록)을 조회해 시각과 함께 답하는 방식으로 구현해야 하며, 답에 근거 기록의 식별자·시각을 붙이는 것이 13. 대화형 기능의 신뢰·기반의 근거 표시 요구와 맞을 것으로 보인다. | ref-453, ref-857, ref-111 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f17 | [사실] | Open-RMF 작업 상태 스키마(rmf_api_msgs task_state.json)는 작업 상태 값으로 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 를 두고, 활성 단계 id(active), 완료까지 남은 추정 시간(estimate_millis), 배정 로봇(assigned_to 의 group·name), 단계마다 시작·종료 시각·추정·사건(events)·건너뛰기 요청, 그리고 중단(interruptions)·취소(cancellation) 요청 기록을 담는다. | ref-111 | 아니오 | medium | 2026-09-29 | 완료·인계 | — |
| f18 | [사실] | Open-RMF 는 작업을 단계(phase)로 구성하고 Clean·Delivery·Patrol·Compose 범주의 작업 요청을 특정 로봇 지정(robot_task_request) 또는 최적 플릿 위임(dispatch_task_request)으로 보내며, 요청은 범주(category)와 플릿 지원 스키마를 따르는 설명(description)을 필수로, 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·수행 플릿 이름을 선택으로 두고, 이후 작업 취소나 단계 건너뛰기 요청으로 추가 제어를 할 수 있다. | ref-110, ref-125 | 아니오 | medium | 2026-09-29 | 시작 조건 | — |
| f19 | [사실] | Open Source Robotics Alliance(OSRA) 상호운용 SIG 는 2026-07-02 세션에서 Open-RMF REST API 를 언어 모델이 부를 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(MCP) 서버와 평이한 영어 명령을 여러 단계의 RMF 임무로 바꾸는 에이전트(Nayantra)를 다뤘으며, 공지 본문에는 실행 전 사람 확인·승인이나 작업 상태 질의에 관한 언급이 없다. | ref-862 | 아니오 | medium | 2026-07-02 | 시작 조건 | — |
| f20 | [추정] | MCP 도구 호출로 언어 모델이 관제 API 를 직접 부르는 구현(f19)에는 승인 단계가 드러나지 않으므로, 분류 원문의 '대화 결과는 실행 명령이 아니라 계획'이라는 요구를 지키려면 ROP 는 언어 모델의 도구 호출 제안(작업 요청 초안)과 실제 dispatch_task_request 발행 사이에 계획 미리보기·승인 관문을 두고, 승인된 계획만 한 번 관제 작업 요청으로 변환해야 할 것으로 보인다. | ref-862, ref-110, ref-125 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f21 | [사실] | ROSA(Royce 외, NASA JPL, IEEE Aerospace 2025)는 ROS 1·ROS 2 로봇 시스템을 자연어로 점검·진단·조작하게 하는 오픈소스 언어 모델 에이전트로, 명령을 잘 정의된 도구로 ROS 에 연결하고 매개변수 검증과 제약 강제 같은 안전 장치를 두며 JPL 화성 실험장·실험실·시뮬레이션의 세 로봇으로 모의 운용을 시연했다. | ref-859 | 아니오 | medium | 2024-10-09 | — | — |
| f22 | [사실] | RobotFleet(Gupta 외, 2025)은 이기종 로봇 플릿을 컨테이너 서비스로 배치하고 언어 모델로 중앙 집중식 다중 로봇 작업 계획·스케줄링을 하며, 공유 선언형 세계 상태와 실행·재계획을 위한 양방향 통신, 모듈형 자율 스택 층을 갖춘 오픈소스 프레임워크다. | ref-777 | 아니오 | medium | 2025-10-12 | — | — |
| f23 | [사실] | Henkel 외(2026)의 체계적 문헌 고찰(88편)은 산업 자동화의 기반 모델 에이전트가 사용자 지원·모니터링 용도에 강하고 사람 상호작용(+37%)·불확실성 처리(+35%)에서 기존 산업 에이전트보다 나으나, 보고된 시스템의 75.0% 가 기술 성숙도 4~6 의 프로토타입·초기 검증 단계이고 배포 지향 근거는 9.1% 에 그치며, 일반화 부족·환각과 출력 불안정·데이터 부족·추론 지연이 지속적 장애물이라고 보고했다. | ref-861 | 아니오 | medium | 2026-05-04 | 예외·성과 | — |
| f24 | [사실] | ETRI 전자통신동향분석 39권 1호(2024-02)의 '거대언어모델 기반 로봇 인공지능 기술 동향'(이준기 외)은 언어 모델의 상식·추론 능력으로 명령을 이해하고 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획과 요소 기술을 수행하는 제어 코드 생성을 자동화하는 흐름을 정리했으며, 다중 로봇 조율이나 사람 승인 절차는 다루지 않고 대규모 계산 자원·데이터·시뮬레이션·물리 테스트베드가 소수 기업에 집중된 점을 한계로 적었다. | ref-858 | 아니오 | medium | 2024-02 | — | — |
| f25 | [사실] | Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. | ref-847 | 아니오 | medium | 2026 | 병원 / 시작 조건 | 원문 미열람 |
| f26 | [추정] | 확인한 자료를 종합하면 12. 채팅으로 업무 지시·오케스트레이션에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것으로 보인다. | ref-242, ref-753, ref-677, ref-111, ref-110 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f27 | [추정] | 연계 대상: 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 생성하는 일(CoMuRoS)과 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 로봇 자체 지능·제어 쪽이며, 이종 제조사를 연결하는 ROP 는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 할 것으로 보인다. | ref-677, ref-859, ref-110 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f28 | [추정] | 언어 모델 기반 다중 로봇 작업 분해·배정(SMART-LLM, DART-LLM, FLEET), 사전 계획 검증(VerifyLLM), 실패 설명(REFLECT)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 이 영역 양쪽에 연결하고, 승인·근거 표시·환각 관련 내용은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다. | ref-165, ref-861, ref-753 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 2025-02-06 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2502.03814 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-059 | Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H. | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D. | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10-08 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.07417 | 아니오 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.05118 | 아니오 |
| ref-777 | Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J. | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.10379 | 아니오 |
| ref-855 | Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S. | HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models | 2025-05-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.00820 | 아니오 |
| ref-677 | Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2511.22354 | 아니오 |
| ref-857 | Argenziano, F., Umili, E., Leotta, F., & Nardi, D. | Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning | 2025-09-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2509.16006 | 아니오 |
| ref-858 | 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)) | 거대언어모델 기반 로봇 인공지능 기술 동향 | 2024-02 | 정부·연구기관 | high | 2026-09-29 | https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html | 아니오 |
| ref-859 | Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025) | Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent | 2024-10-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.06472 | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. (CoRL 2023) | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023-06-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.15724 | 아니오 |
| ref-861 | Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y. | Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges | 2026-05-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2605.02592 | 아니오 |
| ref-862 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-07-02 | 오픈소스 문서 | medium | 2026-09-29 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |
| ref-847 | Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력 | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 2026 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10514-026-10255-6 | 예 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f2(사람 개입이 반응적이고 승인 부담 미정량화), f23(산업 배포 근거 9.1%, 환각·출력 불안정), f19·f20(도구 호출 직결 구현에 승인 단계 부재) / 섹션 4: f3(작업 분해·연합 형성·배정), f4(의존 관계 DAG), f5(작업 그래프·로봇–작업 적합도 행렬), f8(사전 실행 계획 검증), f2(감독 제어·실행 전 승인), f14(실패 설명), f17(작업 상태·단계·사건) / 섹션 5: 병원 — f25(간호 인력 자연어 지시→작업 순서열·실행 중 재스케줄링, 원문 미열람 명시), 실외 — f13(정밀 농업에서 질의로 진행 확인), 가정 — f8(가정 작업 데이터셋 검증, 실제 현장이 아닌 데이터셋임을 명시) / 섹션 6: f3·f4·f5·f6·f7(대화 지시→분해·의존·능력 매칭→형식 배정), f8·f9·f10·f11(자동 검증 후 사람 승인), f12(사건 기반 재계획·사람 도움 요청), f13·f14·f15·f16(기록 근거의 진행·실패 설명), f20(승인 관문 위치) / 섹션 7: f17·f18(Open-RMF 작업 요청·상태 스키마), f19(OSRA Interop SIG, MCP 서버), f21(ROSA), f22(RobotFleet), f8(VerifyLLM 코드 공개) / 섹션 8: f1, f2, f3, f4, f5, f8, f9, f12, f13, f14, f23, 국내 f24 / 섹션 9: f26(직접 범위: 대화→작업 그래프, 엔진 결과의 계획 제안, 검증·승인, 관제 작업 요청 변환, 기록 근거 설명), f27(연계 대상: 로봇 내부 코드 생성·스킬 실행·ROS 직접 제어) / 섹션 10: 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링(f7·f28, 원문 주석의 짝), 13. 대화형 기능의 신뢰·기반(f11·f16·f28), 32. 예외 복구·재계획·업무 연속성(f12·f26), 37. 관제 화면·실행 기록(f16·f17), 20. 로봇·제조사 관제 연동(f18·f19·f20), 9. 채팅으로 시나리오 구성(f18 작업 요청에 없는 기한·반복은 시나리오 모델에), 10. 채팅으로 로봇 구성(f5 능력 매칭), 5. 로봇 능력·작업 표현(f5·f9 능력 이해), 24. 작업·워크플로 모델링(f4 DAG), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f28, 교차 규칙), 63. 병원·의료(f25) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 f5·f6·f7 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f2·f10·f11·f23 반영, 37. 관제 화면·실행 기록 페이지에 f17 반영, 32. 예외 복구·재계획·업무 연속성 페이지에 f12 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사전 실행 계획 검증 | Pre-execution Plan Verification | 언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다. |
| 감독 제어 | Supervisory Control | 사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다. |
| 실패 설명 | Failure Explanation | 로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다. |
| 로봇–작업 적합도 행렬 | Robot–Task Fitness Matrix | 로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다. |

## 열린 질문

새로 생긴 질문:

- 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 13. 대화형 기능의 신뢰·기반 | 근거: f2 | 종류: 일반
- 사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 20. 로봇·제조사 관제 연동, 13. 대화형 기능의 신뢰·기반 | 근거: f19 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 61. 물류창고, 63. 병원·의료, 62. 제조 공장 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 3
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f25 병원 논문 원문 미열람(이전 실행에서 Springer 인증 리다이렉트) — 저자·정량 결과·승인 절차 미확인, 검색 결과 초록 범위만 재인용
    - f12 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)은 검색 결과 요약에서만 보여 claim 에 넣지 않음
    - f2 서베이가 인용한 Hunt 외·VADER·Li 외 원 논문은 직접 열지 않아 서베이 본문 요약에만 기댐
    - f4 DART-LLM 의 로봇 종류·성공률 수치는 초록에 없어 미확인
    - f9 HMCF 의 사람 개입 횟수 등 정량값은 초록에 없어 미확인
    - f6·f10·f15 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f17·f18 Open-RMF 문서·스키마 발행일 미확인
    - MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(제조 공장 사례 후보)는 403 으로 열지 못해 넣지 않음
    - Eluna(arXiv 2607.08960, 창고 SOP 에이전트)는 로봇 지시가 아닌 업무 시스템 자동화라 적용 사례로 넣지 않음
    - 국내 산업 사례: 한국어 검색 3회에서 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 찾았으나 대화형 업무 지시가 아니어서 출처로 넣지 않음
    - hellot SCM FAIR 2026 기사의 자연어 프롬프트는 영상 분석 조건 설정이라 이 영역과 무관해 제외
- 범위 경계 위반 의심:
    - f27: 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS 직접 제어 에이전트(ROSA)는 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f7·f26: 배정·일정 계산 자체는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 범위이므로 이 영역에서는 대화→작업 그래프 변환과 계획 제안·승인의 근거로만 제안함
    - f12·f26: 실행 중 재계획·복구는 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 승인된 계획과의 차이 표시·재승인 근거로만 제안함
    - f8: VerifyLLM 의 가정 작업 데이터셋은 실제 가정 현장이 아니므로 site_type 가정 은 데이터셋 기준임을 서술에 밝혀야 함
    - f23: 산업 자동화 일반(비로봇 포함) 문헌 고찰은 성숙도·과제 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-165~ref-847, 예약 구간 안) 상한 도달로 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, Hierarchical LLM multi-agent prompt optimization(arXiv 2602.21670), 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)는 확인했으나 넣지 못했다. 원문 열람 17건(webfetch 14, github_raw 3: task_new.md·task_request.json·task_state.json), 미열람 1건(ref-847, 이전 실행의 검색 결과 초록 재인용). ref-847 은 이전 실행 2026-09-29-04 가 ref-242 로 낸 병원 논문과 같은 URL 이나 참고문헌 목록 입력에 없어 새 id 로 냈으며 퍼블리셔가 기존 id 로 합칠 수 있다(이번 실행의 ref-242 는 FLEET 논문이다). 교차 확인 3건(f6: SMART-LLM·DART-LLM·FLEET, f10: Li 외 서베이·HMCF·VerifyLLM, f15: REFLECT·Argenziano 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록·HTML 본문 확인, high 신뢰도 출처는 ETRI 동향 1건이며 단일 출처). 분류 원문 핵심 질문(대화 지시→확인 가능한 계획→승인→실행·진행 설명)에는 f3·f4·f5·f6(분해·배정 가능), f8·f9·f10(실행 전 검증·승인 설계 존재), f13·f14·f15·f17(기록 근거 진행·실패 설명과 관제 상태 기록), f19·f20(도구 호출 직결 구현의 승인 부재)로 답했으며 결론은 '세 단계 각각의 연구·오픈소스는 있으나 셋을 하나의 승인 관문이 있는 흐름으로 이은 운영 사례는 확인되지 않았고 산업 배포 근거는 드물다'는 추정(f7·f11·f16·f20·f26)이다. 현장 유형: 병원(f25, 원문 미열람 명시), 실외(f13, 정밀 농업), 가정(f8, 데이터셋 기준)만 확인했고 물류창고·제조 공장·상업 시설 사례는 없다. L. AI·학습 기술 관련 finding(f1~f6·f8·f9·f12·f14·f28)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·13. 대화형 기능의 신뢰·기반 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 848건과의 URL 중복을 대조하지 못했으므로 서베이·SMART-LLM·ROSA 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시·구조화 출력·팬아웃·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-29-04/research.md

```markdown
# 리서치 브리프 2026-09-29-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-04 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 9. 채팅으로 시나리오 구성 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 불확실도 정렬·과소명세·미션 명세 패턴·상황 상태 추적 용어 없음(명확화 질문·슬롯 채우기·명시적 확인·행동 트리·BPMN·LTL 은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 구성(compose)·작업 요청 스키마, BPMN, 미션 명세 패턴 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 짝 연결 필요, 24. 작업·워크플로 모델링·13. 대화형 기능의 신뢰·기반 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
2. 언어 모델이 과소명세된 지시에서 빠진 조건을 알아채고 되묻는 시점과 질문 내용을 어떻게 정하며, 되묻기의 효과는 어떻게 측정되는가? (섹션 3·4·6 겨냥)
3. 여러 턴에 걸친 대화에서 이미 합의한 단계·값을 보존하고 바뀐 부분만 반영하며 사용자가 정한 값을 모델 추정보다 우선하려면 무엇이 필요한가? (섹션 3·6·11 겨냥)
4. 자연어 설명에서 순서·분기·반복을 가진 워크플로(BPMN·행동 트리·시간 논리)를 만들고 실행 가능성을 검증하는 연구는 무엇이 있고 정확도는 어떻게 보고되는가? (섹션 4·6·8 겨냥)
5. 시나리오가 담아야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)을 관제·플랫폼의 작업 요청·작업 구성 형식은 어떤 필드로 받는가? (섹션 4·7 겨냥)
6. 병원·물류창고·제조 공장 등 현장 유형별로 대화로 작업 시나리오를 정한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
7. 채팅 시나리오 구성에서 ROP가 직접 맡을 것(대화→구조화 시나리오·되묻기·검증·승인)과 로봇 수준 실행·형식 계획기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | KnowNo(Ren 외, CoRL 2023)는 언어 모델 계획기의 불확실도를 등각 예측(conformal prediction)으로 측정해 후보 행동의 예측 집합이 하나로 좁혀지면 자율 실행하고 여러 개가 남으면 사람에게 되묻는 틀로, 공간·수량·속성·대명사 지시·선호·안전의 여러 모호성 유형에서 목표 성공률을 보장하면서 사람의 도움 요청을 줄였다고 보고했다. | ref-351 | 아니오 | medium | 2023-09-04 | — | — |
| f2 | [사실] | Deng 외(2026)는 되묻기 질문의 가치를 정답 목표에 대한 베이즈 믿음 갱신량으로 재는 정보 이득 보상(Information Gain Reward)으로 명확화 모델을 학습해, 명확화를 더한 τ-Bench 환경에서 다섯 종의 에이전트 모델 모두에서 되묻기 없는 기준선보다 성공률을 평균 3.7% 높이면서 상호작용 단계는 평균 0.3회만 늘렸다고 보고했다. | ref-840 | 아니오 | medium | 2026-06-02 | — | — |
| f3 | [추정] | 불확실도로 되묻기 시점을 정하는 연구(f1)와 질문의 정보 이득으로 질문 내용을 고르는 연구(f2)를 함께 보면, 이 영역의 '모자란 조건은 선택지와 이유를 붙인 질문으로 채운다'는 기능은 모든 항목을 순서대로 묻는 서식이 아니라 시나리오 항목마다 불확실도를 재어 실행 결과가 갈리는 항목만 후보 선택지와 함께 되묻는 방식으로 구현해야 질문 횟수를 줄일 수 있을 것으로 보인다. | ref-351, ref-840 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f4 | [사실] | Laban 외(2025)는 20만 건 이상의 시뮬레이션 대화로 상위 공개·비공개 언어 모델을 비교해 여섯 가지 생성 과제에서 다중 턴 성능이 단일 턴보다 평균 39% 낮았고, 그 원인이 능력 저하보다 신뢰성 저하이며 모델이 초기 턴에서 가정을 세우고 성급히 최종 답을 낸 뒤 그것에 과도하게 의존하기 때문이라고 보고했다. | ref-841 | 아니오 | medium | 2025-05-09 | — | — |
| f5 | [사실] | Tack·Laban·Neville(2026)은 사용자가 의도를 처음에 다 밝히지 않고 점진적으로 드러내고 수정하며 중간에 방향을 바꾸는 다중 턴 대화로 기존 단일 턴 벤치마크를 변환하는 틀을 제안했고, 정적 설정의 높은 성능이 의도가 바뀌는 설정으로 옮겨지지 않아 여러 모델 계열에서 큰 폭의 성능 하락이 나타난다고 보고했다. | ref-842 | 아니오 | medium | 2026-07-22 | — | — |
| f6 | [사실] | Tao·Tao·Wang(2026)의 IDSS(Intent-Driven Situation States)는 대화 이력과 별도로 도구가 확인한 사실과 작업 상태 판단을 분리한 명시적 상황 상태(사용자 의도·필요 변수·제약·실행 상태)를 학습 없이 유지하는 틀로, 세 개의 상호작용 벤치마크와 여덟 개 언어 모델에서 작업 완료·선호 도출·상호작용 효율이 개선됐고 특히 다중 개체 조정·바뀌는 제약·제약 인식 재계획 과제에서 이득이 컸다고 보고했다. | ref-843 | 아니오 | medium | 2026-08-16 | — | — |
| f7 | [추정] | 다중 턴에서 모델이 초기 가정에 묶이고(f4) 바뀌는 의도를 따라가지 못하며(f5) 명시적 상황 상태가 이를 완화한다는 연구(f6)를 함께 보면, 이 영역의 '합의 내용 보존·변경 표시·사용자 값 우선'은 언어 모델의 대화 문맥에 맡길 것이 아니라 시나리오를 대화 밖의 구조화 상태로 두고 값마다 출처(사용자 확정·모델 추정·미정)를 기록해 턴마다 바뀐 부분만 갱신·표시하는 방식으로 구현해야 할 것으로 보인다. | ref-841, ref-842, ref-843 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f8 | [사실] | Kourani·Berti·Schuster·van der Aalst(2024)는 텍스트 설명에서 프로세스 모델을 자동 생성하고 반복 정제하는 언어 모델 기반 틀을 제안해 프롬프트 전략, 안전한 모델 생성 규약, 오류 처리 기제를 두고, 생성 모델의 품질 보장과 BPMN·페트리 넷 표준 표기 내보내기를 지원하는 시스템으로 구현했으며 예비 결과만 보고했다. | ref-844 | 아니오 | medium | 2024-03-12 | — | — |
| f9 | [사실] | Matei 외(2026)는 다국어 BPMN 파일을 번역·SpiffWorkflow 실행 지향 적합성 검사·언어 모델 반복 수정으로 정답 말뭉치를 만들고 그 설명문에서 실행 가능한 BPMN 2.0 XML 을 재구성하는 다단계 파이프라인으로, 공개 BPMN 750개 중 검증된 정답 387개를 얻고 평균 재구성 유사도 0.75 이상과 이름만 다른 거의 완전한 재구성 약 50건을 보고했다. | ref-845 | 아니오 | medium | 2026-04-13 | — | — |
| f10 | [사실] | 서로 다른 두 연구 그룹(Kourani 외, Matei 외)이 자연어 텍스트에서 BPMN 프로세스 모델을 언어 모델로 생성하되 실행 지향 검사나 오류 처리로 생성 결과의 유효성을 확보하는 방법을 각각 보고해, 텍스트에서 실행 가능한 워크플로 모델을 만드는 접근이 한 곳 이상에서 확인된다. | ref-844, ref-845 | 예 | medium | 2026-04-13 | — | — |
| f11 | [추정] | 할 일·순서·반복·실패 처리 조건을 가진 시나리오는 프로세스 모델과 같은 구조이므로, 텍스트→BPMN 생성 연구(f8·f9·f10)가 쓰는 '생성 후 실행 지향 검사로 유효성 확보' 흐름은 9. 채팅으로 시나리오 구성이 대화 결과를 24. 작업·워크플로 모델링의 워크플로 모델로 내고 검증하는 방식의 선례가 될 것으로 보인다. | ref-844, ref-845 | 아니오 | low | 2026-09-29 | — | — |
| f12 | [사실] | BTGenBot(Izzo·Bardaro·Matteucci, 2024)은 최대 70억 매개변수의 경량 언어 모델을 기존 행동 트리에서 GPT-3.5 로 만든 데이터셋으로 미세조정해 자연어 작업 설명에서 로봇 행동 트리를 생성하며, llama2·llama-chat·code-llama 변형을 아홉 과제에서 구문 분석·검증 시스템·시뮬레이션·실제 로봇으로 평가했다. | ref-061 | 아니오 | medium | 2024-03-19 | — | — |
| f13 | [사실] | ConformalNL2LTL(Sundarsingh 외, 2025)은 자연어 지시를 선형 시간 논리 공식으로 옮길 때 번역을 질의응답 단계로 나누고 각 단계의 불확실도를 등각 예측으로 재어, 사용자가 정한 신뢰 문턱에 못 미치면 보조 모델에, 그래도 부족하면 사용자에게 되물어 사용자 지정 번역 성공률을 보장하는 방법이다. | ref-847 | 아니오 | medium | 2026-02-20 | — | — |
| f14 | [사실] | 서로 다른 세 연구 그룹(KnowNo, ConformalNL2LTL, Deng 외)이 언어 모델이 해석에 확신이 없을 때만 사람에게 되묻도록 불확실도나 정보 이득을 기준으로 되묻기를 제한하는 설계를 각각 보고해, '확신 없는 항목만 되묻기' 접근이 한 곳 이상에서 확인된다. | ref-351, ref-847, ref-840 | 예 | medium | 2026-06-02 | 시작 조건 | — |
| f15 | [사실] | Menghi 외(2019)는 로봇 문헌의 현실적 임무 요구 245건에서 이동 로봇 미션 명세 패턴 22개를 뽑아 사용 의도·알려진 용례·패턴 간 관계·시간 논리 템플릿과 함께 목록으로 정리하고, 패턴을 인스턴스화·조합·LTL/CTL 로 컴파일하는 도구를 만들어 실제 임무 요구 441건과 명세 1,251건, 산업 파트너 시나리오 5건, 시뮬레이터와 실제 로봇 2대로 검증했다. | ref-848 | 아니오 | medium | 2019-01-07 | — | — |
| f16 | [추정] | 반복되는 임무 요구를 패턴 목록으로 정리한 연구(f15)와 자연어를 시간 논리로 옮길 때 불확실한 단계만 되묻는 연구(f13)를 함께 보면, 이 영역의 핵심 질문인 '무엇을 되물어야 하는가'는 시나리오 항목(순서·반복·기한·회피·실패 처리)마다 대응하는 명세 패턴의 빈 자리를 채우는 질문 목록으로 구성하고 그중 해석이 불확실한 자리만 실제로 묻는 방식으로 답할 수 있을 것으로 보인다. | ref-848, ref-847 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f17 | [사실] | Open-RMF 문서는 작업(task)을 단계(phase)를 만들어 내는 객체로 정의하고 공개 API 단계로 GoToPlace·PickUp·DropOff·PerformAction 을, 내부 자동 추가 단계로 RequestLift 를 두며, 'compose' 범주의 작업은 활동(activity)의 순서열로 단계를 엮고, 작업 요청은 특정 로봇에 직접 배정하는 robot_task_request 와 최적 플릿에 맡기는 dispatch_task_request 로 보내며 Clean·Delivery·Patrol·Compose 범주의 JSON 스키마를 따른다. | ref-110 | 아니오 | medium | 2026-09-29 | 작업 대상 | — |
| f18 | [사실] | Open-RMF 작업 요청 스키마(rmf_api_msgs task_request.json)는 필수 필드로 범주(category)와 플릿이 지원하는 스키마를 따르는 설명(description)을, 선택 필드로 가장 이른 시작 가능 시각(unix_millis_earliest_start_time)·요청 시각·플릿 우선순위 스키마를 따르는 priority·용도 라벨(labels)·요청자(requester)·수행 허용 플릿 이름(fleet_name)을 두며, 완료 기한이나 반복 주기 필드는 두지 않는다. | ref-125 | 아니오 | medium | 2026-09-29 | 제약 | — |
| f19 | [추정] | 이 영역이 대화로 정하려는 값 가운데 할 일·순서(compose 활동 순서열)·물품 인계(PickUp·DropOff)·시작 조건(가장 이른 시작 시각)·우선순위·요청자·수행 플릿은 Open-RMF 작업 구성과 작업 요청에 이미 자리가 있으나, 완료 기한·반복·실패 처리 조건은 작업 요청 스키마에 자리가 없으므로 채팅 시나리오 구성의 결과물은 관제 작업 요청보다 넓은 시나리오 모델(33. 시나리오 모델·편집, 24. 작업·워크플로 모델링)에 담고 실행 시점에 작업 요청으로 변환해야 할 것으로 보인다. | ref-110, ref-125 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f20 | [사실] | University West(스웨덴) 학위논문 'An LLM-Interface for Robot Mission Specification in Logistics'는 물류 현장의 자율이동로봇 임무 계획에서 사람의 자연어와 계획기가 요구하는 신호 시간 논리(STL) 사이의 번역 인터페이스로 언어 모델을 쓰는 신뢰성을 조사해, 현재 언어 모델이 공식의 구문과 논리는 만들지만 구문상 유효한 STL 공식을 일관되게 내지 못하는 것이 핵심 병목이라고 밝혔다. | ref-548 | 아니오 | medium | 2026-09-29 | 제약 | 원문 미열람 |
| f21 | [사실] | Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. | ref-852 | 아니오 | medium | 2026 | 병원 / 예외·성과 | 원문 미열람 |
| f22 | [사실] | 손승아·강태민·하동수(한국과학기술원)는 정보과학회지 2024년 10월호에 '자연어 로봇 제어 기술 동향: 분류, 기술, 응용'을 실어 인지 수준에 따른 시스템 분류, 사용 기술, 자연어 로봇 작업의 범위를 정리했다. | ref-853 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f23 | [추정] | 병원 사례(f21)에서 실행 중 들어온 추가 요청이 재스케줄링으로 이어진 점과 다중 턴에서 합의가 흔들리는 문제(f4·f5)를 함께 보면, 채팅 시나리오 구성은 실행 전 합의된 시나리오를 확정본으로 잠그고 실행 중 대화로 들어온 변경은 확정본에 대한 차이로 표시해 다시 승인받는 절차를 두어야 하며, 그 실행·재계획 자체는 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성이 맡는 것이 원문 구분에 맞을 것으로 보인다. | ref-852, ref-841, ref-842 | 아니오 | low | 2026-09-29 | 병원 / 완료·인계 | — |
| f24 | [추정] | 확인한 자료를 종합하면 9. 채팅으로 시나리오 구성에서 ROP가 직접 맡을 범위는 대화를 값마다 출처가 붙은 구조화 시나리오(할 일·물품·사람·순서·반복·기한·실패 처리 조건)로 바꾸고, 불확실한 항목만 선택지와 이유를 붙여 되묻고, 워크플로 모델과 실행 지향 검사로 시나리오의 유효성을 확인하며, 합의본을 보존·차이 표시하고 사람이 승인한 시나리오만 실행 단계로 넘기는 일로 보인다. | ref-351, ref-843, ref-845, ref-110 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f25 | [추정] | 연계 대상: 자연어에서 로봇 수준 행동 트리를 생성해 로봇에서 실행하는 일(BTGenBot)과 자연어를 LTL·STL 공식으로 옮겨 형식 계획기·모델 검사기로 계획을 만드는 일(ConformalNL2LTL, University West 학위논문)은 분류 원문 19장의 로봇 자체 지능·제어와 외부 계획 도구 쪽이며, ROP는 시나리오의 순서·기한·실패 처리 조건을 이들 도구가 읽을 수 있는 인터페이스로 넘기고 그 결과(실행 가능 여부·검증 결과)를 받아 대화로 설명하는 데 그쳐야 할 것으로 보인다. | ref-061, ref-847, ref-548 | 아니오 | low | 2026-09-29 | — | — |
| f26 | [추정] | 불확실도 정렬과 명확화 학습(KnowNo, Deng 외), 텍스트→프로세스 모델 생성(Kourani 외, Matei 외), 자연어→시간 논리 번역(ConformalNL2LTL)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 이 영역 양쪽에 연결하고, 오해석 방지·평가 부분은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다. | ref-351, ref-844, ref-847 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-09-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-840 | Deng, M., Li, Z., Li, X., Zhu, T., Zhao, Y., Guo, Z., & Wang, W. | Uncertainty-Aware Clarification in LLM Agents with Information Gain | 2026-06-02 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2606.03135 | 아니오 |
| ref-841 | Laban, P., Hayashi, H., Zhou, Y., & Neville, J. | LLMs Get Lost In Multi-Turn Conversation | 2025-05-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.06120 | 아니오 |
| ref-842 | Tack, J., Laban, P., & Neville, J. | LLMs Get Lost in Evolving User Intent | 2026-07-22 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2607.20734 | 아니오 |
| ref-843 | Tao, M., Tao, Y., & Wang, P. | Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents | 2026-08-16 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2608.15755 | 아니오 |
| ref-844 | Kourani, H., Berti, A., Schuster, D., & van der Aalst, W. M. P. | Process Modeling With Large Language Models | 2024-03-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.07541 | 아니오 |
| ref-845 | Matei, I., Zhenirovskyy, M., Menaka Sekar, P. K., & Wong, H. Y. | Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach | 2026-04-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2604.12105 | 아니오 |
| ref-061 | Izzo, R. A., Bardaro, G., & Matteucci, M. | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 2024-03-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2403.12761 | 아니오 |
| ref-847 | Sundarsingh, D. S., Wang, J., Deshmukh, J. V., & Kantaros, Y. | ConformalNL2LTL: Translating Natural Language Instructions into Temporal Logic Formulas with Conformal Correctness Guarantees | 2026-02-20 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2504.21022 | 아니오 |
| ref-848 | Menghi, C., Tsigkanos, C., Pelliccione, P., Ghezzi, C., & Berger, T. | Specification Patterns for Robotic Missions | 2019-01-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1901.02077 | 아니오 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-548 | University West (Högskolan Väst, DiVA) 학위논문 저자(미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 미확인 | 논문 | medium | 2026-09-29 | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf | 예 |
| ref-852 | Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력 | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 2026 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10514-026-10255-6 | 예 |
| ref-853 | 손승아, 강태민, 하동수 (한국과학기술원), 정보과학회지 42(10) | 자연어 로봇 제어 기술 동향: 분류, 기술, 응용 | 2024-10 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11940459 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f4·f5(다중 턴에서 합의가 흔들림), f14(확신 없는 항목만 되묻기), f20(자연어→형식 명세의 병목) / 섹션 4: f1(불확실도 정렬·예측 집합), f2(정보 이득), f6(상황 상태), f15(미션 명세 패턴), f17(작업·단계·활동), f4(과소명세) / 섹션 5: 병원 — f21·f23(자연어 지시→작업 순서열, 실행 중 추가 요청, 원문 미열람 명시), 물류 — f20(물류 AMR 임무 명세 학위논문, 현장 유형은 '물류'로만 서술) / 섹션 6: f1·f2·f3·f13·f14(되묻기 시점·내용), f6·f7(합의 보존·값 출처), f8·f9·f10·f11(텍스트→워크플로 생성과 실행 지향 검사), f12(행동 트리 생성), f15·f16(패턴 기반 질문 목록) / 섹션 7: f17·f18·f19(Open-RMF compose·task_request), f8(BPMN·페트리 넷), f15(패턴 도구·LTL/CTL), f12(행동 트리) / 섹션 8: f1, f2, f4, f5, f6, f8, f9, f13, f15, f21, 국내 f22 / 섹션 9: f24(직접 범위), f25(연계 대상: 로봇 수준 행동 트리 실행·형식 계획기) / 섹션 10: 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현(f19·f26, 원문 주석의 짝), 24. 작업·워크플로 모델링(f11·f19), 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성(f23), 13. 대화형 기능의 신뢰·기반(f14·f26), 10. 채팅으로 로봇 구성(f17 수행 플릿), 26. 작업 순서·스케줄링(f18 시작 시각·우선순위), 20. 로봇·제조사 관제 연동(f17·f18), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f26, 교차 규칙), 63. 병원·의료(f21) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 24. 작업·워크플로 모델링 페이지에 f8·f9·f10 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f1·f4·f14 반영, 33. 시나리오 모델·편집 페이지에 f15·f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 불확실도 정렬 | Uncertainty Alignment | 언어 모델 계획기가 자신의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻도록 맞추는 것으로, 등각 예측으로 후보 집합을 만들어 집합 크기로 되묻기를 정한다. |
| 과소명세 | Underspecification | 사용자 지시에 실행에 필요한 조건(대상·장소·수량·기한 등)이 빠져 여러 해석이 가능한 상태로, 명확화 질문이나 기본값 규칙으로 채워야 한다. |
| 미션 명세 패턴 | Mission Specification Pattern | 이동 로봇 임무 요구에서 반복되는 명세 문제와 그 시간 논리 템플릿을 목록으로 정리한 것으로, 패턴을 채우고 조합해 형식 명세를 만든다. |
| 상황 상태 추적 | Situation State Tracking | 다중 턴 대화에서 대화 이력과 별도로 사용자 의도·필요 변수·제약·실행 상태를 명시적 상태로 유지해 확인된 사실과 판단을 구분하는 기법이다. |

## 열린 질문

새로 생긴 질문:

- 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 33. 시나리오 모델·편집 | 근거: f16 | 종류: 일반
- 대화로 정한 시나리오에서 사용자가 확정한 값과 모델이 추정한 값을 구분해 저장·표시하고 턴마다 바뀐 부분만 보여 주는 공개 데이터 형식이나 편집기 구현이 있는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 20. 로봇·제조사 관제 연동 | 근거: f19 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? | 관련 영역: 9. 채팅으로 시나리오 구성, 61. 물류창고, 63. 병원·의료 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 2
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f1 KnowNo 의 '10~24% 도움 감소' 범위는 HTML 본문 요약에서 봤으나 실험별 조건을 확인하지 못해 claim 에는 넣지 않고 발췌의 단계별 14%·시행별 8% 인용만 씀
    - f12 BTGenBot 의 실패 처리(fallback) 노드 생성 방식은 초록에 없어 미확인
    - f15 미션 명세 패턴 22개의 개별 이름·분류(이동·트리거·회피 등)는 초록에서 확인하지 못함
    - f20 University West 학위논문 원문 미열람(DiVA PDF·기록 페이지 5회 연결 재설정) — 저자·연도·실험 결과 미확인, 검색 결과 초록 범위만 사용
    - f21 Autonomous Robots 병원 논문 원문 미열람(Springer 인증 리다이렉트, MDPI 대안 403) — 저자·정량 결과·확인 절차 미확인
    - f22 정보과학회지 동향 논문 본문 미열람(DBpia 서지만 확인) — 초록·분류 내용 미확인
    - f8 Kourani 외의 정량 결과는 초록에 없어 미확인
    - f10·f14 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f17·f18 Open-RMF 문서·스키마 발행일 미확인
    - BPMNGen(Springer BISE 2025, 대화형 BPMN 생성)과 MDPI Applied Sciences 로봇 건강 보조원 프레임워크는 인증·403 으로 열지 못해 넣지 않음
    - OATH(arXiv 2510.14063)는 검색 요약과 달리 초록에 되묻기 대화 내용이 없어 제외
    - 대화만으로 로봇 작업 시나리오를 구성한 실제 현장 운영 사례는 찾지 못함(연구 프로토타입·병원 시범 배치·학위논문뿐)
- 범위 경계 위반 의심:
    - f25: 로봇 수준 행동 트리 실행과 LTL·STL 형식 계획기는 분류 원문 19장 '로봇 자체 지능·제어'·외부 도구 쪽이므로 '연계 대상: '으로 표시함
    - f21·f23: 병원 로봇의 실행 중 재스케줄링·실패 복구는 12. 채팅으로 업무 지시·오케스트레이션과 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 시나리오 변경·재승인 절차의 근거로만 제안함
    - f8·f9·f10·f11: 업무 프로세스(비로봇) 대상 연구는 워크플로 생성·검증 방법의 선례로만 제안함
    - f2·f4·f5·f6: 일반 언어 모델 에이전트 연구(로봇 아님)는 대화 설계 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-351~ref-853, 예약 구간 안) 상한 도달로 Cao·Lee 행동 트리 생성(arXiv 2302.12927), Choe 외 창고 협동 로봇 LLM-to-TL(arXiv 2505.13376), SEQUOR 다중 턴 제약 준수 벤치마크(arXiv 2605.06353), Bettencourt·Guerreiro BPMN 문헌 리뷰(arXiv 2604.14034), Purdue 'Human in the loop' 학위논문은 열었거나 확인했으나 넣지 못했다. 원문 열람 12건(webfetch 10, github_raw 2: task_new.md·task_request.json), 미열람 3건(ref-548·ref-852·ref-853, 검색 결과·서지 페이지로 기관·제목 확인). 교차 확인 2건(f10: Kourani 외·Matei 외, f14: KnowNo·ConformalNL2LTL·Deng 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록 페이지 확인, 오픈소스 문서는 단일 출처). 분류 원문 핵심 질문(무엇을 되물어야 하는가)에는 f1·f2·f13·f14(불확실한 항목만 되묻기), f15·f16(명세 패턴의 빈 자리를 질문 목록으로), f17·f18·f19(관제 작업 형식에 있는 항목과 없는 항목)로 답했으며 결론은 '되묻기 대상은 시나리오 항목의 빈 자리 가운데 해석이 불확실하고 실행 결과가 갈리는 것으로 제한하고, 기한·반복·실패 처리처럼 관제 요청에 자리가 없는 항목은 시나리오 모델에서 보관해야 한다'는 추정(f3·f16·f19·f24)이다. 현장 유형: 병원(f21·f23, 원문 미열람 명시)만 확인했고 물류는 학위논문(f20)이 '물류' 일반을 말해 site_type 을 채우지 않았으며 제조 공장·상업 시설·가정·실외 사례는 없다. 합의 내용 보존·변경 표시(f7)는 로봇 시나리오가 아닌 일반 언어 모델 대화 연구(f4·f5·f6)에서 도출한 추정이다. L. AI·학습 기술 관련 finding(f1·f2·f8·f9·f13·f26)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현·24. 작업·워크플로 모델링 양쪽에 연결하도록 제안했다. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 838건과의 URL 중복을 대조하지 못했으므로 KnowNo·Open-RMF task_new·rmf_api_msgs 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 명확화 질문·슬롯 채우기·명시적 확인·행동 트리·BPMN·LTL·구조화 출력·작업 분해·사람 참여 루프·등각 예측은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-33/research.md

```markdown
# 리서치 브리프 2026-09-25-33

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-33 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(MRTA 분류 체계·배정 방식 용어 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 미지정)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 반영 제안 3건 대기: LLM 기반 분해·배정, LLM+해법기 분담)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 반영 제안 2건 대기)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(트랙 반영 제안: 27. AI·학습·적응과 모델 운영 연결)
- 섹션 11. 열린 질문 비어 있음(oq-024, oq-030 관련, 트랙 반영 제안 1건)
- 섹션 13. 참고 자료 각주 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. MRTA 문제는 어떤 기준(로봇·작업의 단일/다중, 즉시/시간 확장 배정, 작업 간 의존)으로 분류되며, 각 유형은 어떤 최적화 문제에 대응하는가? (섹션 4·6 겨냥)
3. 중앙 최적화, 시장 기반 경매, 분산 합의, 규칙(최근접 등), 학습 기반 배정은 각각 어떻게 동작하며 창고 로봇 운영에서 어떤 결과가 보고되었는가? (섹션 6·8 겨냥, 교차 규칙: 학습 기반 배차는 27. AI·학습·적응과 모델 운영)
4. Open-RMF·VDA 5050 같은 오픈소스·표준은 작업 배정을 어느 구성요소의 책임으로 두고 배터리·충전 제약을 어떻게 배정에 반영하는가? (섹션 7·9 겨냥)
5. LLM 기반 배정(분해·팀 구성·배정)과 LLM이 정식화하고 해법기가 배정하는 방식의 대표 연구는 무엇이며, LTAA 결과의 출처 충돌(oq-030)은 해소되는가? (트랙 반영 제안, 섹션 6·8·11)
6. 로봇 능력(적재·장착 장비)과 실제 운용 능력의 차이는 배정 후보를 어떻게 거르는가? (oq-024, 5. 로봇 능력·작업 온톨로지 연결, 섹션 10)
7. 국내 물류센터·국책 과제에서 다중 로봇 작업 배정 규칙이나 기술을 다룬 자료가 있는가? (한국 자료 우선, 섹션 5·8)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Gerkey와 Matarić(2004)는 MRTA 문제를 단일 작업 로봇(ST)/다중 작업 로봇(MT), 단일 로봇 작업(SR)/다중 로봇 작업(MR), 즉시 배정(IA)/시간 확장 배정(TA)의 세 축으로 분류하는 도메인 독립 분류 체계를 제시했다. | ref-648 | 아니오 | medium | 2004-09 | — | 원문 미열람 |
| f2 | [사실] | Gerkey와 Matarić의 분류에서 ST-SR-IA(단일 작업 로봇·단일 로봇 작업·즉시 배정) 문제는 조합 최적화의 최적 배정 문제(optimal assignment problem)의 한 사례로, 헝가리안 방법 같은 다항 시간 해법으로 최적해를 구할 수 있는 유형이다. | ref-648 | 아니오 | medium | 2004-09 | — | 원문 미열람 |
| f3 | [사실] | Korsah·Stentz·Dias(2013)의 iTax 분류는 작업이 독립이라고 본 기존 분류가 다루지 못한 효용·제약의 상호 의존을 더해, 같은 로봇 일정 안의 의존(ID)과 서로 다른 로봇 일정 사이의 의존(XD, 선후 제약 등)을 구분하고 각 범주를 조합 최적화·운영과학 모델에 대응시킨다. | ref-649 | 아니오 | medium | 2013 | — | 원문 미열람 |
| f4 | [사실] | Aziz 외(AAMAS 2021)는 작업마다 최소 로봇 수가 필요한 ST-MR-IA 설정에서 총예산·작업 예산·로봇 예산 제약 아래 완료 작업 수를 최대화하는 배정의 계산 복잡도를 분석하고 근사 알고리즘과 근사 하한을 제시했다. | ref-652 | 아니오 | medium | 2021-05 | — | 원문 미열람 |
| f5 | [사실] | Dias 외(2006)는 로봇들이 작업을 경매·입찰로 사고파는 시장 기반(market-based) 다중 로봇 조율 연구를 탐사·지도 작성·로봇 축구 등 여러 응용에 걸쳐 정리한 서베이를 IEEE 회보 다중 로봇 조율 특집호에 냈다. | ref-651 | 아니오 | medium | 2006-07 | — | 원문 미열람 |
| f6 | [사실] | Choi·Brunet·How(2009)의 합의 기반 경매 알고리즘(CBAA)과 다중 배정용 합의 기반 번들 알고리즘(CBBA)은 시장 기반 작업 선택과 국소 통신 합의로 낙찰가 충돌을 풀며, 점수 체계 가정 아래 충돌 없는 배정으로 수렴하고 로봇 간 상황 인식 불일치와 통신망 변화에 강건하다고 증명·보고한다. | ref-650 | 아니오 | medium | 2009 | — | 원문 미열람 |
| f7 | [사실] | Open-RMF 는 작업 요청이 오면 디스패처가 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리할 수 있는 플릿 어댑터가 비용을 담은 입찰(BidProposal)을 내면 디스패처가 가장 빨리 끝나는 것·가장 비용이 낮은 것 같은 설정 기준으로 비교해 작업을 준다. | ref-376 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF 의 rmf_task TaskPlanner 는 요청된 시작 시각을 고려해 작업이 가장 짧은 시간 안에 끝나도록 로봇들 사이 작업 배정과 순서를 정하고, 배터리 같은 자원 제약을 반영해 필요하면 충전 작업을 로봇 일정에 자동으로 끼워 넣는다. | ref-660, ref-376 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | Open-RMF 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold(예 0.10) 아래인 로봇은 작업하지 않게 하고 충전 목표(recharge_soc), 로봇별 충전기, 작업 종료 후 동작(park·charge·nothing)을 두어 배정 후보를 배터리 상태로 제한한다. | ref-105 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f10 | [사실] | VDA 5050 명세는 '이동로봇에 대한 주문 배정'을 관제 시스템(fleet control)의 최소 기능으로 두고, 로봇은 크기·적재 장착부 같은 물리 특성을 팩트시트로 알리지만, 배정 알고리즘 자체는 정하지 않고 관제–로봇 통신만 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f11 | [사실] | Ma 외(2017)의 다중 에이전트 픽업·배송(MAPD) 알고리즘 토큰 패싱(TP)에서는 토큰을 받은 에이전트가 픽업 위치가 자기 위치에서 가장 가까운 미배정 작업을 스스로 맡고 충돌 없는 경로를 계획하며, 작업 교환을 더한 변형(TPTS)도 제시된다. | ref-006 | 아니오 | medium | 2017 | 수행 자원 | 원문 미열람 |
| f12 | [사실] | AGV 배차 연구에서 최근접 차량 우선(NVF) 규칙은 요청 위치까지 가장 가까운 유휴 차량을 보내는 방식인데, 순차적 최근접 배정이 전체 이동 시간을 줄이는 배정 조합을 놓칠 수 있어, 앞으로의 운반 요청까지 고려한 조합 최적화 배차가 무작위·최근접 규칙보다 효율적이라는 결과가 공장 현장 조건에서 보고되었다. | ref-655 | 아니오 | medium | 2019 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Merschformann 외(2019)는 로봇 이동형 풀필먼트 시스템(RMFS) 이산 사건 시뮬레이션에서 피킹 주문을 작업대에 배정하는 규칙은 단위 처리량에 큰 영향을 주었지만 보충 주문 배정·선반 선택·선반 보관 위치 규칙은 그렇지 않았다고 보고하고, 규칙 코드를 RAWSim-O 로 공개했다. | ref-653, ref-101 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f14 | [사실] | 국내 자동물류센터 설계 최적화 연구는 자동창고(ASRS)와 AGV 를 포함한 시뮬레이션에서 빈 상태가 된 AGV 가 가장 가까운 화물을 회수하는 최근접 규칙(Closest Rule)을 운영 규칙으로 두고 반응표면 메타모델로 설계 요인을 최적화했다. | ref-658 | 아니오 | medium | 2026-09-25 | 적치 / 수행 자원 | 원문 미열람 |
| f15 | [사실] | 국내 과제 보고서 '클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발'은 클라우드·클라우드렛 환경에서 개별·다중 로봇의 작업 수립·할당·재조정·학습 기술을 개발해 제조·물류 분야에서 실증하는 것을 목표로 한다. | ref-657 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | Meseguer Valenzuela와 Blanes Noguera(2025)의 이동로봇 플릿 작업 배정 문헌 검토는 52편을 휴리스틱, 메타휴리스틱, 정확해·매스휴리스틱, 시장 기반, 인공지능(주로 강화학습) 다섯 계열로 묶고, 연구 대부분이 중앙집중·시뮬레이션 기반이며 30대 미만 플릿 실험이 많다고 지적한다. | ref-152 | 아니오 | medium | 2025-01 | — | 원문 미열람 |
| f17 | [사실] | Wang과 Gombolay의 ScheduleNet(이종 그래프 어텐션 네트워크)은 시간 제약 네트워크에 로봇·근접 노드를 더한 이종 그래프로 다중 로봇 배정·일정 정책을 학습하며, 작은 문제에서 모방 학습으로 훈련해 더 큰 미학습 문제에 일반화되었다고 저자들이 보고한다. | ref-654 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f18 | [사실] | 2026년 프리프린트는 AMR 플릿의 배터리 열화를 고려한 작업 배정, 작업 순서, 충전 방식 선택, 공용 충전기 조율을 함께 푸는 틀을 제안하며, 플릿 수준 주문제가 배정·충전기 순서를 정하고 로봇 수준 부문제가 배터리 일정을 최적화하는 2단계 방법을 쓴다. | ref-659 | 아니오 | medium | 2026-03 | 제약 | 원문 미열람 |
| f19 | [사실] | SMART-LLM(Kannan 외 2023)은 LLM 에 프로그램 형식의 few-shot 프롬프트를 주어 지시를 하위 작업으로 분해하고, 로봇 팀을 구성한 뒤 하위 작업을 배정하는 다중 로봇 작업 계획 파이프라인이다. | ref-090, ref-089 | 아니오 | medium | 2023-09 | — | 원문 미열람 |
| f20 | [사실] | DART-LLM(2024)은 LLM 으로 하위 작업 사이 의존 관계를 방향 비순환 그래프(DAG)로 만들고 이를 바탕으로 다중 로봇에 작업을 배정·실행하는 프리프린트이다. | ref-059 | 아니오 | medium | 2024-11 | — | 원문 미열람 |
| f21 | [사실] | LLM 이 의존 그래프나 수리 정식화를 만들고 배정·일정은 해법기가 푸는 연구로 선형계획을 쓰는 LiP-LLM, PDDL 과 정수계획을 결합한 PIP-LLM, 형식 언어로 이종 로봇 팀 일정을 정하는 FLEET, MRTA·스케줄링용 MILP 모델을 LLM 으로 자동 구성하는 Peng 외(2025)가 있다. | ref-166, ref-181, ref-242, ref-167 | 아니오 | medium | 2025-10 | — | 원문 미열람 |
| f22 | [사실] | LTAA(arXiv 2512.02810)는 LangGraph 기반 LLM 작업 배정 에이전트로 단계 적응 배정 전략·다단계 검증·계층적 재시도를 두고 건설 로봇 시나리오에서 동적 계획법·강화학습과 비교한 연구이지만, 완료율 비교 결과에 관한 출처 충돌(oq-030)은 이번 검색에서도 해소되지 않았다. | ref-168 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f23 | [사실] | 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(이종 다중 로봇 배정의 의미 기반 가능성 추론 2026, 라인리스 이동 조립 시스템의 온톨로지 기반 배정 2022). | ref-236, ref-237 | 아니오 | medium | 2026-08 | 수행 자원 | 원문 미열람 |
| f24 | [사실] | 작업자가 피킹하고 AMR 이 운반하는 동적 주문 피킹 연구(Yu & Srinivas 2025)는 AMR 가용성에 따른 개입 전략을 다루어, 주문 변동과 로봇 배정이 맞물리는 피킹 단계의 사례가 된다. | ref-132 | 아니오 | medium | 2025 | 피킹 / 수행 자원 | 원문 미열람 |
| f25 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)에 대해, 최근접 배정은 MAPD 토큰 패싱·AGV 최근접 규칙·국내 물류센터 시뮬레이션에서 기본 규칙으로 쓰일 만큼 단순하지만, 앞으로의 요청을 고려한 조합 최적화가 총 이동을 줄이고 RMFS 에서는 배정 규칙 선택이 처리량을 크게 바꾼다는 보고가 있어, 최근접이 전체 최적이라는 보장은 없고 창고 현장에서 둘을 직접 비교한 실측 자료는 이번 검색에서 찾지 못한 것으로 보인다. | ref-006, ref-655, ref-658, ref-653 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |
| f26 | [추정] | Open-RMF 디스패처가 여러 플릿 어댑터의 입찰을 비교하고 VDA 5050 이 주문 배정을 관제의 기능으로 두는 구조로 보아, 이종 제조사를 잇는 ROP 는 어느 플릿·로봇에 작업을 줄지의 배정 결정과 기준(비용·완료 시각)을 직접 맡고, 플릿 내부 경로·주행은 제조사 관제나 로봇에 맡기는 분담이 가능할 것으로 보인다. | ref-376, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f27 | [추정] | 연계 대상: VDA 5050 은 관제–이동로봇 통신과 무관한 외부 IT 시스템 인터페이스를 범위에서 제외하므로, 배정의 입력이 되는 주문·납기·재고 제약은 WMS 등 상위 업무 시스템에서 오고 그 정책(수요예측·전사 재고정책)은 ROP 밖의 연계 대상이다. | ref-031 | 아니오 | low | 2026-09-25 | 시작 조건 | — |
| f28 | [추정] | LLM 기반 배정 연구들을 보면 LLM 이 지시 해석·분해·정식화를 맡고 전체 최적 배정은 선형·정수계획 해법기가 맡는 분담이 제안되고 있으나, 창고 물류 조건에서 LLM 배정·해법기 배정·최근접 규칙을 비교한 연구는 이번 검색에서 확인되지 않았다. | ref-166, ref-181, ref-167, ref-090 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-648 | Gerkey, B. P., & Matarić, M. J. | A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems | 2004-09 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/0278364904045564 | 예 |
| ref-649 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 예 |
| ref-650 | Choi, H.-L., Brunet, L., & How, J. P. | Consensus-Based Decentralized Auctions for Robust Task Allocation | 2009 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1109/tro.2009.2022423 | 예 |
| ref-651 | Dias, M. B., Zlot, R., Kalra, N., & Stentz, A. | Market-Based Multirobot Coordination: A Survey and Analysis | 2006-07 | 논문 | medium | 2026-09-25 | https://www.ri.cmu.edu/pub_files/2006/7/01677943-1.pdf | 예 |
| ref-652 | Aziz, H., Chan, H., Cseh, Á., Li, B., Ramezani, F., & Wang, C. | Multi-Robot Task Allocation—Complexity and Approximation | 2021-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2103.12370 | 예 |
| ref-653 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-654 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 예 |
| ref-655 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 2019 | 논문 | medium | 2026-09-25 | https://www.inderscience.com/info/inarticle.php?artid=103016 | 예 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 아니오 |
| ref-657 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 | 예 |
| ref-658 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | 논문 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 예 |
| ref-659 | arXiv 2603.22731 저자(미확인) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-660 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1705.10868 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 예 |
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2501.08726 | 예 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 예 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/SMARTlab-Purdue/SMART-LLM | 예 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2411.09022 | 예 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21040 | 예 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.22784 | 예 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.07417 | 예 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.13813 | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | 논문 | medium | 2026-09-25 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3(왜 중요한가): f12·f13·f25 — 배정 규칙이 총 이동·처리량을 바꾸고 최근접이 전체 최적을 보장하지 않음 / 섹션 4(핵심 개념): f1·f2(ST/MT·SR/MR·IA/TA, 최적 배정 문제), f3(ID·XD 의존), f4(다중 로봇 작업·예산) / 섹션 5(현장 시나리오): 피킹 f13·f24·f25, 적치 f14, 배터리 제약 f9·f18 / 섹션 6(대표 접근법): 중앙 최적화 f2·f12, 시장·경매 f5·f6·f7, 규칙 f11·f14, 학습 기반 배차 f17(27. AI·학습·적응과 모델 운영 교차 규칙), LLM 기반 f19·f20·f21·f22·f28(트랙 nl-task-chatbot 반영 제안 2026-09-25-04·2026-09-25-21 두 건 반영), 문헌 동향 f16 / 섹션 7(표준·오픈소스): Open-RMF 입찰·TaskPlanner f7·f8·f9, VDA 5050 관제 기능 f10 / 섹션 8(대표 연구): f1·f3·f4·f5·f6·f11·f13·f16·f17·f18, 국내 f14·f15, LLM f19~f22(반영 제안 SMART-LLM·DART-LLM·LiP-LLM·PIP-LLM·FLEET·Peng 외·LTAA; COHERENT·LaMMA-P·IMR-LLM 은 이번에 재확인하지 않아 제외) / 섹션 9(직접 범위·연계): f26(배정 결정은 ROP, 플릿 내부 주행은 제조사), f27(연계 대상: 상위 업무 시스템) / 섹션 10(연결): 5. 로봇 능력·작업 온톨로지 f23·oq-024, 14. 작업 순서·스케줄링 f3·f8, 15. 다중 로봇 경로·교통 관리 — MAPF f11, 16. 공용 자원·충전·에너지 최적화 f8·f9·f18, 9. 로봇·제조사 관제 연동 f7·f10·f26, 27. AI·학습·적응과 모델 운영 f17·f19~f22(트랙 반영 제안 2026-09-25-21) / 섹션 11(열린 질문): oq-030(LTAA 출처 충돌, f22 로 미해소), oq-024, 새 질문 3건(트랙 반영 제안의 창고 비교 연구 부재 포함) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 헝가리안 방법 | Hungarian Method | 작업과 수행자 사이 일대일 배정에서 총비용을 최소로 하는 최적 배정 문제를 다항 시간에 푸는 고전 알고리즘이다. |
| 시장 기반 작업 배정 | Market-based Task Allocation | 로봇이 작업에 대한 비용·효용을 입찰하고 경매로 낙찰자를 정해 작업을 나누는 배정 방식이다. |
| 합의 기반 번들 알고리즘 | Consensus-Based Bundle Algorithm (CBBA) | 각 로봇이 작업 묶음에 입찰하고 이웃과의 국소 통신 합의로 낙찰 충돌을 풀어 중앙 없이 충돌 없는 배정에 이르는 분산 배정 알고리즘이다. |
| 최근접 차량 우선 규칙 | Nearest Vehicle First (NVF) Rule | 운반 요청이 생기면 요청 위치까지 이동 거리가 가장 짧은 유휴 차량·로봇에 작업을 맡기는 배차 규칙이다. |

## 열린 질문

새로 생긴 질문:

- 국내외 물류센터에서 최근접 배정 규칙과 전역 최적화(또는 LLM 기반) 배정을 같은 조건에서 비교해 총 이동거리·처리량·납기 준수를 실측한 자료가 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 4. 성과·경제성·프로세스 개선 | 근거: f25 | 종류: 일반
- ROP 가 플릿 단위로 작업을 입찰·배정하고 제조사 관제가 플릿 안에서 다시 로봇을 고르는 두 수준 배정에서 전체 최적성이 얼마나 손실되며, 이를 줄이려면 제조사 관제가 어떤 비용·상태 정보를 내야 하는가? | 관련 영역: 13. 작업 배정 — MRTA, 9. 로봇·제조사 관제 연동 | 근거: f26 | 종류: 일반
- 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 14. 작업 순서·스케줄링, 1. 주문·업무 시스템 연계 | 근거: f7 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 29 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 13건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 대부분 단일 출처이거나 같은 저자·기관 계열 출처
    - f2 헝가리안 방법 적용은 Gerkey 원문이 아닌 검색 요약(관련 문헌)에 기댐
    - f11 토큰 패싱의 최근접 픽업 선택은 후속 연구의 설명 요약에 기댐(ref-006 원문 미열람)
    - f14 ref-658 저자·발행연도 미확인, f15 ref-657 수행기관·발행연도 미확인
    - ref-654 발행 연도(Autonomous Robots 게재년) 미확인, ref-655·ref-659 저자 미확인
    - oq-030 LTAA 완료율 출처 충돌 미해소(원문 미열람, 검색 요약에 수치 없음)
    - 트랙 반영 제안 가운데 COHERENT(ref-169)·LaMMA-P(ref-164)·IMR-LLM(ref-170)은 이번에 재확인하지 않아 finding 에 넣지 않음
    - f19~f21 LLM 연구 내용은 제목·이전 브리프 요약 수준(재인용)
- 범위 경계 위반 의심:
    - f27 은 상위 업무 시스템(외부 연계 영역)에 관한 내용이라 '연계 대상: '으로 표시함
    - f18 배터리 열화 모델링은 16. 공용 자원·충전·에너지 최적화와 겹치며 13. 작업 배정 — MRTA 에서는 배정 결합 부분만 다루도록 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문 3건을 열었다(ref-376 Open-RMF task 장, ref-660 rmf_task README, 재사용 ref-031 VDA 5050 명세). 논문·보고서 등 나머지는 원문 미열람으로 신뢰도 상한 medium 이며, 재사용 출처 중 이번에 열지 않은 것(ref-105, ref-101 등)도 medium 으로 적었다. 검색 20회/30, 신규 출처 13건/15(ref-648~ref-660, 예약 구간 안), 재사용 16건. 교차 확인 0건. 트랙 반영 제안 6건 중 섹션 6·8·10·11 제안은 f19~f22·f28 과 열린 질문으로 반영 근거를 냈고, LTAA 출처 충돌(oq-030)은 해소하지 못해 열린 질문으로 유지한다. 한국 자료: 국내 과제 보고서(ref-657)와 자동물류센터 시뮬레이션 논문(ref-658)을 찾았으나 국내 물류센터의 실제 배정 규칙 운영 사례는 찾지 못했다. 교차 규칙: 학습 기반 배차(f17)와 LLM 배정(f19~f22)은 27. AI·학습·적응과 모델 운영과 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 구분: 시뮬레이션 결과(f13·f14)는 설계·평가 도구로만 서술. 정정 요청 없음. 해결된 열린 질문 없음.
```
