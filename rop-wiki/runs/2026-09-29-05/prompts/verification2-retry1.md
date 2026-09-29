(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-05
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 12. 채팅으로 업무 지시·오케스트레이션 (C. 채팅 기반 구성·운영)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-29-05/target.json

```json
{
  "run_id": "2026-09-29-05",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 97,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 12,
    "area_name": "12. 채팅으로 업무 지시·오케스트레이션",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=12"
}
```

### runs/2026-09-29-05/research.json

```json
{
  "run_id": "2026-09-29-05",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 12,
    "area_name": "12. 채팅으로 업무 지시·오케스트레이션",
    "category": "C. 채팅 기반 구성·운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 사전 실행 계획 검증·감독 제어·실패 설명·로봇–작업 적합도 행렬 용어 없음(작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청·작업 상태 스키마, MCP 기반 관제 연결, ROSA·RobotFleet 같은 오픈소스 에이전트 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 짝 연결 필요, 13. 대화형 기능의 신뢰·기반·32. 예외 복구·재계획·업무 연속성·37. 관제 화면·실행 기록 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]",
    "언어 모델이 자연어 업무 지시를 여러 이기종 로봇의 하위 작업으로 분해하고 의존 관계·능력에 맞춰 배정·일정을 제안하는 연구는 무엇이 있고 결과는 어떻게 보고되는가? (섹션 4·6·8 겨냥)",
    "언어 모델이 만든 계획을 실행 전에 자동 검증하고 사람이 승인하게 하는 설계(사전 실행 검증, 감독 제어)는 어떤 것이 있으며 승인 부담은 어떻게 다뤄지는가? (섹션 3·6·11 겨냥)",
    "어디까지 했는지·왜 멈췄는지를 대화로 묻고 실행 기록을 근거로 답하는 연구와, 관제가 제공하는 작업 상태·단계·사건 기록은 무엇인가? (섹션 4·6·7 겨냥)",
    "관제·플랫폼의 작업 요청 API 와 언어 모델 도구 호출(MCP)을 잇는 오픈소스·프레임워크는 무엇이고 승인 단계를 두는가? (섹션 7 겨냥)",
    "병원·제조 공장·물류창고·실외 등 현장 유형별로 대화로 로봇 업무를 지시한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)",
    "채팅 업무 지시에서 ROP가 직접 맡을 것(대화→계획, 검증, 승인, 관제 작업 요청, 진행 설명)과 로봇 수준 코드 생성·스킬 실행·형식 최적화기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Li 외(2025)의 서베이는 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정, 중간 수준 동작 계획, 하위 수준 행동 생성, 사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다.",
      "tag": "사실",
      "source_ids": [
        "ref-165"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"systematically categorizes their applications across high-level task allocation, mid-level motion planning, low-level action generation, and human intervention.\" v1 2025-02-06, v5 2026-05-03.",
      "as_of": "2025-02-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Li 외(2025) 서베이의 사람 개입 절은 실행 전에 사람이 계획을 승인하는 방식(Hunt 외), 로봇이 막히면 도움을 요청하는 방식(VADER), 환각을 줄이는 사람 검증 방식(Li 외)을 예로 들고, 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머문다는 점과 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다는 점을 빈틈으로 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-165"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "HTML 본문 요약: Hunt 외는 실행 전 승인(pre-execution approval)을 두고, 운영자 한 사람이 여러 로봇을 감독할 수 있는지에 관한 인지 부담은 정량화되지 않았다고 정리(재서술).",
      "as_of": "2026-05-03",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-090"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"task decomposition, coalition formation, and task allocation, all guided by programmatic LLM prompts within the few-shot prompting paradigm.\" 벤치마크는 네 복잡도 범주.",
      "as_of": "2023-09-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "DART-LLM(Wang 외, 2024)은 자연어 지시를 방향 비순환 그래프(DAG)로 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀로, 질의응답형 분해 모듈·로봇 배정 함수·구동 모듈·시각-언어 물체 탐지 모듈로 구성되며 세 복잡도 수준에서 DeepSeek-r1-671B 가 최고 성공률을, Llama-3.1-8B 가 응답 시간 안정성을 보였고 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-059"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: DAG 로 작업 의존을 모델링해 자연어 지시를 조율된 하위 작업으로 분해; \"explicit dependency modeling notably enhances the performance of smaller models\"(절제 실험).",
      "as_of": "2024-11-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "FLEET(Rivera 외, 2025)은 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 능력을 반영한 로봇–작업 적합도 행렬을 만들고, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀어 배정하는 2단계 혼합 방식으로, 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했으며 능력이 다른 사족 로봇 실기로 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-242"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"An LLM front-end produces (i) a task graph with durations and precedence and (ii) a capability-aware robot–task fitness matrix.\" 이후 형식 최적화가 makespan 최소화.",
      "as_of": "2025-10-08",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "서로 다른 세 연구 그룹(SMART-LLM, DART-LLM, FLEET)이 자연어 업무 지시를 언어 모델로 하위 작업으로 분해하고 이기종 로봇에 배정하는 방법을 각각 보고해, '대화 지시→분해→배정' 접근이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-090",
        "ref-059",
        "ref-242"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "세 논문 모두 자연어 지시의 분해와 이기종 로봇 배정을 초록에서 명시(SMART-LLM: 분해·연합·배정, DART-LLM: DAG 분해·배정, FLEET: 작업 그래프·적합도 행렬).",
      "as_of": "2025-10-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "FLEET 가 배정·일정은 형식 최적화기에 맡기고 언어 모델은 작업 그래프·능력 매칭에만 쓴 점(f5)과 DART-LLM 이 의존 관계를 DAG 로 명시한 점(f4)을 함께 보면, 이 영역의 '업무 파악·분해·배정·일정 제안'은 언어 모델이 대화를 의존 관계 있는 작업 그래프와 능력 요구로 바꾸고, 실제 배정·일정은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 엔진에 넘겨 계산한 결과를 계획으로 제안하는 혼합 구조가 원문 주석의 짝 연결과 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-242",
        "ref-059"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "FLEET 절제 실험에서 MILP 는 시간 구조, LLM 은 능력 매칭을 각각 담당; DART-LLM 은 의존 모델링이 작은 모델의 성능을 높임. 이를 원문 주석(업무 지시는 25·26번 기능을 대화로 쓰게 함)과 대조한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈로, 복잡도가 다른 가정 작업 데이터셋에서 시험했으며 코드를 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-753"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 자연어 지시→LTL 변환 후 행동 순서열 분석으로 논리 불일치·누락 단계를 실행 전에 식별; 가정 작업 데이터셋으로 평가(재서술).",
      "as_of": "2025-07-07",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "HMCF(Li 외, 2025)는 로봇마다 자기 능력을 이해하고 작업을 실행 가능한 지시로 바꾸는 언어 모델 에이전트를 두고, 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀로, 시뮬레이션에서 기존 계획 방법보다 작업 성공률을 4.76% 높이고 실제 환경에서 최소한의 사람 개입으로 제로샷 일반화를 보였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-855"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"reducing hallucinations through task verification and human supervision\"; 시뮬레이션 성공률 +4.76%, 실세계 제로샷 일반화(저자 실험 조건).",
      "as_of": "2025-05-01",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "서로 다른 세 연구 그룹(Li 외 서베이가 정리한 Hunt 외의 실행 전 승인, HMCF 의 작업 검증·사람 감독, VerifyLLM 의 자동 사전 검증)이 언어 모델이 만든 로봇 계획을 실행 전에 검증하거나 사람이 승인하게 하는 설계를 각각 보고해, '실행 전 검증·승인' 접근이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-165",
        "ref-855",
        "ref-753"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "서베이 사람 개입 절(실행 전 승인·사람 검증), HMCF 초록(작업 검증·사람 감독), VerifyLLM 초록(실행 전 검증)이 같은 설계 방향을 독립적으로 보고.",
      "as_of": "2026-05-03",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f11",
      "claim": "자동 사전 검증(f8)과 사람 승인(f2·f9·f10)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이 낸 계획을 먼저 자동 검증(의존 관계·능력·논리 일관성)으로 걸러 승인자에게는 검토 가능한 구조(작업 그래프·배정·일정)로 보여 주는 방식으로 구현해야 서베이가 지적한 운영자 인지 부담을 줄일 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-165",
        "ref-753",
        "ref-855"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "서베이는 운영자 인지 부담 미정량화를 빈틈으로, VerifyLLM 은 자동 검증으로 실행 전 오류 감소를, HMCF 는 필요할 때만 개입을 보고. 이를 원문 '승인된 계획만 실행'과 결합한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f12",
      "claim": "CoMuRoS(Borate 외, 2025)는 중앙 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 작업 이력·로봇 상태 같은 동적 정보로 일을 배정하고, 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 만들며, 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획해 로봇이 동료를 돕거나 중단된 작업을 재개하거나 사람 도움을 요청하게 하는 중앙 숙고·분산 실행 구조로, 실기에서 협업 복구 9/10·협동 운반 8/8·사람 보조 복구 5/5, 22개 시나리오 벤치마크에서 정확도 최대 0.91 을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-677"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"centralized deliberation with decentralized execution\"; 사건 기반 재계획은 실패·사용자 의도 변경이 촉발; 실기 9/10, 8/8, 5/5(저자 실험 조건). v1 2025-11-27, v2 2026-06-18.",
      "as_of": "2025-11-27",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"specify high-level activities...using natural language, and to monitor their execution by querying a robot.\" 실제 정밀 농업 시나리오에서 시험.",
      "as_of": "2025-09-19",
      "site_type": "실외",
      "flow_item": "완료·인계"
    },
    {
      "id": "f14",
      "claim": "REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하는 틀로, 다양한 작업·실패 시나리오를 담은 RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-453"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"queries LLM for failure reasoning based on a hierarchical summary of robot past experiences generated from multisensory observations.\" RoboFail 데이터셋.",
      "as_of": "2023-06-27",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "서로 다른 두 연구 그룹(REFLECT, Argenziano 외)이 로봇의 실행 기록·경험 요약을 근거로 언어 모델이 무엇을 했고 왜 실패했는지를 자연어로 설명하거나 질의에 답하게 하는 방법을 각각 보고해, '실행 기록 근거의 진행·실패 설명' 접근이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-453",
        "ref-857"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "REFLECT 는 계층적 경험 요약→실패 설명, Argenziano 외는 로봇 질의로 과거·현재·미래 행동 진행 확인을 각각 초록에서 명시.",
      "as_of": "2025-09-19",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f16",
      "claim": "실행 기록 근거의 설명 연구(f14·f15)와 Open-RMF 작업 상태 스키마가 단계·사건·추정 시간·배정 로봇을 담는 점(f17)을 함께 보면, 이 영역의 '채팅으로 진행 상황 질의·결과 설명'은 언어 모델의 대화 기억이 아니라 관제의 작업 상태·단계 사건 기록(37. 관제 화면·실행 기록)을 조회해 시각과 함께 답하는 방식으로 구현해야 하며, 답에 근거 기록의 식별자·시각을 붙이는 것이 13. 대화형 기능의 신뢰·기반의 근거 표시 요구와 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-453",
        "ref-857",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "REFLECT·Argenziano 외는 기록 요약을 설명 근거로 씀; task_state 스키마는 phases 아래 events 와 estimate_millis·assigned_to 를 둠. 이를 결합한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f17",
      "claim": "Open-RMF 작업 상태 스키마(rmf_api_msgs task_state.json)는 작업 상태 값으로 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 를 두고, 활성 단계 id(active), 완료까지 남은 추정 시간(estimate_millis), 배정 로봇(assigned_to 의 group·name), 단계마다 시작·종료 시각·추정·사건(events)·건너뛰기 요청, 그리고 중단(interruptions)·취소(cancellation) 요청 기록을 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문(raw JSON) status enum: \"uninitialized\", \"blocked\", \"error\", \"failed\", \"queued\", \"standby\", \"underway\", \"delayed\", \"skipped\", \"canceled\", \"killed\", \"completed\"; estimate_millis 는 완료까지 걸릴 시간 추정 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f18",
      "claim": "Open-RMF 는 작업을 단계(phase)로 구성하고 Clean·Delivery·Patrol·Compose 범주의 작업 요청을 특정 로봇 지정(robot_task_request) 또는 최적 플릿 위임(dispatch_task_request)으로 보내며, 요청은 범주(category)와 플릿 지원 스키마를 따르는 설명(description)을 필수로, 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·수행 플릿 이름을 선택으로 두고, 이후 작업 취소나 단계 건너뛰기 요청으로 추가 제어를 할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-110",
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_new.md 원문: \"take additional control over your tasks by sending requests to RMF to cancel a task or skip a phase.\" task_request.json 원문: category·description 필수, 나머지 선택 (재인용: 2026-09-29-04) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f19",
      "claim": "Open Source Robotics Alliance(OSRA) 상호운용 SIG 는 2026-07-02 세션에서 Open-RMF REST API 를 언어 모델이 부를 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(MCP) 서버와 평이한 영어 명령을 여러 단계의 RMF 임무로 바꾸는 에이전트(Nayantra)를 다뤘으며, 공지 본문에는 실행 전 사람 확인·승인이나 작업 상태 질의에 관한 언급이 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-862"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공지 원문: \"I'll present an MCP server that exposes the Open-RMF REST API as LLM-callable tools, and an agent that turns plain-English commands into multi-step RMF missions\"",
      "as_of": "2026-07-02",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f20",
      "claim": "MCP 도구 호출로 언어 모델이 관제 API 를 직접 부르는 구현(f19)에는 승인 단계가 드러나지 않으므로, 분류 원문의 '대화 결과는 실행 명령이 아니라 계획'이라는 요구를 지키려면 ROP 는 언어 모델의 도구 호출 제안(작업 요청 초안)과 실제 dispatch_task_request 발행 사이에 계획 미리보기·승인 관문을 두고, 승인된 계획만 한 번 관제 작업 요청으로 변환해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-862",
        "ref-110",
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "OSRA 공지에 승인 언급 없음; Open-RMF 작업 요청은 category·description 만 필수라 언어 모델 출력으로 바로 만들 수 있음. 이를 원문 '승인된 계획만 실행'과 대조한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f21",
      "claim": "ROSA(Royce 외, NASA JPL, IEEE Aerospace 2025)는 ROS 1·ROS 2 로봇 시스템을 자연어로 점검·진단·조작하게 하는 오픈소스 언어 모델 에이전트로, 명령을 잘 정의된 도구로 ROS 에 연결하고 매개변수 검증과 제약 강제 같은 안전 장치를 두며 JPL 화성 실험장·실험실·시뮬레이션의 세 로봇으로 모의 운용을 시연했다.",
      "tag": "사실",
      "source_ids": [
        "ref-859"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: ROS 와 자연어 인터페이스의 간극을 잇고 매개변수 검증·제약 강제로 안전한 운용을 보장; Mars Yard·실험실·시뮬레이션에서 세 로봇으로 시연(재서술).",
      "as_of": "2024-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "RobotFleet(Gupta 외, 2025)은 이기종 로봇 플릿을 컨테이너 서비스로 배치하고 언어 모델로 중앙 집중식 다중 로봇 작업 계획·스케줄링을 하며, 공유 선언형 세계 상태와 실행·재계획을 위한 양방향 통신, 모듈형 자율 스택 층을 갖춘 오픈소스 프레임워크다.",
      "tag": "사실",
      "source_ids": [
        "ref-777"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 언어 모델 기반 \"centralized multi-robot task planning and scheduling\"; 공유 선언형 세계 상태, 실행·재계획용 양방향 통신, 컨테이너화된 로봇(재서술).",
      "as_of": "2025-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Henkel 외(2026)의 체계적 문헌 고찰(88편)은 산업 자동화의 기반 모델 에이전트가 사용자 지원·모니터링 용도에 강하고 사람 상호작용(+37%)·불확실성 처리(+35%)에서 기존 산업 에이전트보다 나으나, 보고된 시스템의 75.0% 가 기술 성숙도 4~6 의 프로토타입·초기 검증 단계이고 배포 지향 근거는 9.1% 에 그치며, 일반화 부족·환각과 출력 불안정·데이터 부족·추론 지연이 지속적 장애물이라고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-861"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"predominantly at prototype and early validation stages (75.0% at TRL 4-6), with deployment-oriented evidence remaining rare (9.1%).\"",
      "as_of": "2026-05-04",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f24",
      "claim": "ETRI 전자통신동향분석 39권 1호(2024-02)의 '거대언어모델 기반 로봇 인공지능 기술 동향'(이준기 외)은 언어 모델의 상식·추론 능력으로 명령을 이해하고 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획과 요소 기술을 수행하는 제어 코드 생성을 자동화하는 흐름을 정리했으며, 다중 로봇 조율이나 사람 승인 절차는 다루지 않고 대규모 계산 자원·데이터·시뮬레이션·물리 테스트베드가 소수 기업에 집중된 점을 한계로 적었다.",
      "tag": "사실",
      "source_ids": [
        "ref-858"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: \"거대언어모델의 추론 능력을 활용하여 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획\"; 다중 로봇·사람 확인은 다루지 않음(열람 확인).",
      "as_of": "2024-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-847"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 초록 범위: 간호 인력의 자연어 지시→실행 가능한 작업 순서열, 실행 중 추가 요청에 대한 유전 알고리즘 재스케줄링, 실패 복구는 시각-언어 추론·AI 제안 (재인용: 2026-09-29-04)",
      "as_of": "2026",
      "site_type": "병원",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "확인한 자료를 종합하면 12. 채팅으로 업무 지시·오케스트레이션에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-242",
        "ref-753",
        "ref-677",
        "ref-111",
        "ref-110"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "FLEET(작업 그래프+최적화), VerifyLLM(사전 검증), CoMuRoS(사건 기반 재계획·사람 도움 요청), Open-RMF 작업 요청·상태 스키마를 원문 정의 세 항목(지시·승인·진행 설명)에 대응시킨 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f27",
      "claim": "연계 대상: 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 생성하는 일(CoMuRoS)과 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 로봇 자체 지능·제어 쪽이며, 이종 제조사를 연결하는 ROP 는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-677",
        "ref-859",
        "ref-110"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "CoMuRoS 는 로봇별 지역 LLM 이 Python 실행 코드를 생성; ROSA 는 ROS 1·2 와 직접 연결. 원문 19장 경계표(로봇 자체 지능·제어는 연계)와 대조한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f28",
      "claim": "언어 모델 기반 다중 로봇 작업 분해·배정(SMART-LLM, DART-LLM, FLEET), 사전 계획 검증(VerifyLLM), 실패 설명(REFLECT)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 이 영역 양쪽에 연결하고, 승인·근거 표시·환각 관련 내용은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-165",
        "ref-861",
        "ref-753"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "서베이의 네 층 분류(상위 배정~사람 개입)와 Henkel 외의 환각·출력 불안정 과제를 원문 교차 규칙(학습 기반 배정은 25번, 업무 지시는 25·26번)에 대응시킨 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-165",
      "org": "Li, P., An, Z., Abrar, S., & Zhou, L.",
      "title": "Large Language Models for Multi-Robot Systems: A Survey",
      "published": "2025-02-06",
      "url": "https://arxiv.org/abs/2502.03814",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델을 다중 로봇 시스템에 쓰는 연구를 상위 작업 배정·중간 동작 계획·하위 행동 생성·사람 개입의 네 층으로 정리한 서베이. v5(2026-05-03)의 HTML 본문에서 사람 개입 절과 배정 프레임워크 비교를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2502.03814",
      "source_unopened": false
    },
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09-18",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "상위 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸는 소수 예시 프롬프트 틀. 네 복잡도의 벤치마크·시뮬레이션·실기로 평가.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-059",
      "org": "Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H.",
      "title": "DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models",
      "published": "2024-11-13",
      "url": "https://arxiv.org/abs/2411.09022",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 지시를 DAG 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀. 모델별 성공률·응답 시간과 의존 모델링 절제 실험을 보고.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-242",
      "org": "Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.",
      "title": "FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams",
      "published": "2025-10-08",
      "url": "https://arxiv.org/abs/2510.07417",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델이 작업 그래프와 로봇–작업 적합도 행렬을 만들고 형식 최적화기가 완료 시간 최소화로 배정하는 2단계 혼합 방식. 사족 로봇 실기 검증.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
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
      "summary": "자연어 지시를 LTL 로 옮긴 뒤 행동 순서열의 논리 일관성과 누락 단계를 실행 전에 찾는 검증 모듈. 가정 작업 데이터셋으로 평가, 코드 공개.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-777",
      "org": "Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J.",
      "title": "RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning",
      "published": "2025-10-12",
      "url": "https://arxiv.org/abs/2510.10379",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 기반 중앙 집중식 다중 로봇 작업 계획·스케줄링 오픈소스 프레임워크. 컨테이너화된 로봇, 공유 선언형 세계 상태, 실행·재계획용 양방향 통신.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-855",
      "org": "Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S.",
      "title": "HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models",
      "published": "2025-05-01",
      "url": "https://arxiv.org/abs/2505.00820",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇별 언어 모델 에이전트가 작업 검증으로 환각을 줄이고 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀. 시뮬레이션 성공률 +4.76%, 실세계 제로샷.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-677",
      "org": "Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정)",
      "title": "LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning",
      "published": "2025-11-27",
      "url": "https://arxiv.org/abs/2511.22354",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "CoMuRoS: 중앙 작업 관리자 언어 모델이 자연어 목표를 배정하고 로봇별 지역 언어 모델이 실행 코드를 만들며 실패·의도 변경 시 사건 기반으로 재계획하는 구조. 실기 복구·운반 결과와 22개 시나리오 벤치마크.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-857",
      "org": "Argenziano, F., Umili, E., Leotta, F., & Nardi, D.",
      "title": "Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning",
      "published": "2025-09-19",
      "url": "https://arxiv.org/abs/2509.16006",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델과 자동 계획을 결합해 자연어로 활동을 지정하고 로봇에 질문해 실행 진행을 확인하는 구조. 실제 정밀 농업 시나리오에서 시험.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-858",
      "org": "한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1))",
      "title": "거대언어모델 기반 로봇 인공지능 기술 동향",
      "published": "2024-02",
      "url": "https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "언어 모델로 로봇 명령 이해·요소 기술 분해 작업 계획·제어 코드 생성을 자동화하는 흐름(SayCan, PaLM-E, Code as Policies 등)을 정리한 ETRI 동향 논문. 다중 로봇·사람 승인은 다루지 않음.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-859",
      "org": "Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025)",
      "title": "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent",
      "published": "2024-10-09",
      "url": "https://arxiv.org/abs/2410.06472",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "ROS 1·2 로봇을 자연어로 점검·진단·조작하는 오픈소스 언어 모델 에이전트. 매개변수 검증·제약 강제 안전 장치, 화성 실험장·실험실·시뮬레이션 시연.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-453",
      "org": "Liu, Z., Bahety, A., & Song, S. (CoRL 2023)",
      "title": "REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction",
      "published": "2023-06-27",
      "url": "https://arxiv.org/abs/2306.15724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "다중 감각 관측의 계층적 경험 요약을 근거로 언어 모델이 실패를 설명하고 교정 계획을 돕게 하는 틀. RoboFail 데이터셋.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-861",
      "org": "Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y.",
      "title": "Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges",
      "published": "2026-05-04",
      "url": "https://arxiv.org/abs/2605.02592",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "산업 자동화의 기반 모델 에이전트 88편 체계적 문헌 고찰. 75.0% 가 TRL 4~6, 배포 근거 9.1%, 환각·출력 불안정·지연이 과제.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-862",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse",
      "title": "Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-07-02",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "OSRA 상호운용 SIG 공식 세션 공지. Open-RMF REST API 를 MCP 도구로 노출하고 영어 명령을 다단계 RMF 임무로 바꾸는 에이전트(Nayantra)를 다룬다. 승인·상태 질의 언급 없음.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-847",
      "org": "Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력",
      "title": "Agile assistive hospital robot for suboptimal Task execution in dynamic environments",
      "published": "2026",
      "url": "https://link.springer.com/article/10.1007/s10514-026-10255-6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 병원 보조 로봇이 간호 인력의 자연어 지시를 작업 순서열로 바꾸고 실행 중 추가 요청에 유전 알고리즘으로 재스케줄링하며 실패를 시각-언어 추론으로 복구하는 시스템(이전 실행 2026-09-29-04 의 ref-242 와 같은 URL, 퍼블리셔가 기존 id 로 합칠 수 있음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-110",
      "org": "Open Robotics",
      "title": "Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_new.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 구성(단계·범주·compose)과 robot_task_request·dispatch_task_request, 취소·단계 건너뛰기 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/task_new.md",
      "source_unopened": false
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 요청 JSON 스키마: category·description 필수, 시작 시각·우선순위·라벨·요청자·플릿 이름 선택.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
      "source_unopened": false
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 상태 JSON 스키마: 상태 값, 활성 단계, 추정 시간, 배정 로봇, 단계별 사건, 중단·취소 요청 기록.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
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
      "rationale": "섹션 3: f2(사람 개입이 반응적이고 승인 부담 미정량화), f23(산업 배포 근거 9.1%, 환각·출력 불안정), f19·f20(도구 호출 직결 구현에 승인 단계 부재) / 섹션 4: f3(작업 분해·연합 형성·배정), f4(의존 관계 DAG), f5(작업 그래프·로봇–작업 적합도 행렬), f8(사전 실행 계획 검증), f2(감독 제어·실행 전 승인), f14(실패 설명), f17(작업 상태·단계·사건) / 섹션 5: 병원 — f25(간호 인력 자연어 지시→작업 순서열·실행 중 재스케줄링, 원문 미열람 명시), 실외 — f13(정밀 농업에서 질의로 진행 확인), 가정 — f8(가정 작업 데이터셋 검증, 실제 현장이 아닌 데이터셋임을 명시) / 섹션 6: f3·f4·f5·f6·f7(대화 지시→분해·의존·능력 매칭→형식 배정), f8·f9·f10·f11(자동 검증 후 사람 승인), f12(사건 기반 재계획·사람 도움 요청), f13·f14·f15·f16(기록 근거의 진행·실패 설명), f20(승인 관문 위치) / 섹션 7: f17·f18(Open-RMF 작업 요청·상태 스키마), f19(OSRA Interop SIG, MCP 서버), f21(ROSA), f22(RobotFleet), f8(VerifyLLM 코드 공개) / 섹션 8: f1, f2, f3, f4, f5, f8, f9, f12, f13, f14, f23, 국내 f24 / 섹션 9: f26(직접 범위: 대화→작업 그래프, 엔진 결과의 계획 제안, 검증·승인, 관제 작업 요청 변환, 기록 근거 설명), f27(연계 대상: 로봇 내부 코드 생성·스킬 실행·ROS 직접 제어) / 섹션 10: 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링(f7·f28, 원문 주석의 짝), 13. 대화형 기능의 신뢰·기반(f11·f16·f28), 32. 예외 복구·재계획·업무 연속성(f12·f26), 37. 관제 화면·실행 기록(f16·f17), 20. 로봇·제조사 관제 연동(f18·f19·f20), 9. 채팅으로 시나리오 구성(f18 작업 요청에 없는 기한·반복은 시나리오 모델에), 10. 채팅으로 로봇 구성(f5 능력 매칭), 5. 로봇 능력·작업 표현(f5·f9 능력 이해), 24. 작업·워크플로 모델링(f4 DAG), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f28, 교차 규칙), 63. 병원·의료(f25) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 f5·f6·f7 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f2·f10·f11·f23 반영, 37. 관제 화면·실행 기록 페이지에 f17 반영, 32. 예외 복구·재계획·업무 연속성 페이지에 f12 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "사전 실행 계획 검증",
      "term_en": "Pre-execution Plan Verification",
      "definition": "언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다."
    },
    {
      "term_ko": "감독 제어",
      "term_en": "Supervisory Control",
      "definition": "사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다."
    },
    {
      "term_ko": "실패 설명",
      "term_en": "Failure Explanation",
      "definition": "로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다."
    },
    {
      "term_ko": "로봇–작업 적합도 행렬",
      "term_en": "Robot–Task Fitness Matrix",
      "definition": "로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다."
    }
  ],
  "open_questions_new": [
    "대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 13. 대화형 기능의 신뢰·기반 | 근거: f2 | 종류: 일반",
    "사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반",
    "언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 20. 로봇·제조사 관제 연동, 13. 대화형 기능의 신뢰·기반 | 근거: f19 | 종류: 일반",
    "국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 61. 물류창고, 63. 병원·의료, 62. 제조 공장 | 근거: f24 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 3,
    "unverified": [
      "f25 병원 논문 원문 미열람(이전 실행에서 Springer 인증 리다이렉트) — 저자·정량 결과·승인 절차 미확인, 검색 결과 초록 범위만 재인용",
      "f12 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)은 검색 결과 요약에서만 보여 claim 에 넣지 않음",
      "f2 서베이가 인용한 Hunt 외·VADER·Li 외 원 논문은 직접 열지 않아 서베이 본문 요약에만 기댐",
      "f4 DART-LLM 의 로봇 종류·성공률 수치는 초록에 없어 미확인",
      "f9 HMCF 의 사람 개입 횟수 등 정량값은 초록에 없어 미확인",
      "f6·f10·f15 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)",
      "f17·f18 Open-RMF 문서·스키마 발행일 미확인",
      "MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(제조 공장 사례 후보)는 403 으로 열지 못해 넣지 않음",
      "Eluna(arXiv 2607.08960, 창고 SOP 에이전트)는 로봇 지시가 아닌 업무 시스템 자동화라 적용 사례로 넣지 않음",
      "국내 산업 사례: 한국어 검색 3회에서 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 찾았으나 대화형 업무 지시가 아니어서 출처로 넣지 않음",
      "hellot SCM FAIR 2026 기사의 자연어 프롬프트는 영상 분석 조건 설정이라 이 영역과 무관해 제외"
    ],
    "scope_violations": [
      "f27: 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS 직접 제어 에이전트(ROSA)는 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함",
      "f7·f26: 배정·일정 계산 자체는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 범위이므로 이 영역에서는 대화→작업 그래프 변환과 계획 제안·승인의 근거로만 제안함",
      "f12·f26: 실행 중 재계획·복구는 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 승인된 계획과의 차이 표시·재승인 근거로만 제안함",
      "f8: VerifyLLM 의 가정 작업 데이터셋은 실제 가정 현장이 아니므로 site_type 가정 은 데이터셋 기준임을 서술에 밝혀야 함",
      "f23: 산업 자동화 일반(비로봇 포함) 문헌 고찰은 성숙도·과제 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-165~ref-847, 예약 구간 안) 상한 도달로 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, Hierarchical LLM multi-agent prompt optimization(arXiv 2602.21670), 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)는 확인했으나 넣지 못했다. 원문 열람 17건(webfetch 14, github_raw 3: task_new.md·task_request.json·task_state.json), 미열람 1건(ref-847, 이전 실행의 검색 결과 초록 재인용). ref-847 은 이전 실행 2026-09-29-04 가 ref-242 로 낸 병원 논문과 같은 URL 이나 참고문헌 목록 입력에 없어 새 id 로 냈으며 퍼블리셔가 기존 id 로 합칠 수 있다(이번 실행의 ref-242 는 FLEET 논문이다). 교차 확인 3건(f6: SMART-LLM·DART-LLM·FLEET, f10: Li 외 서베이·HMCF·VerifyLLM, f15: REFLECT·Argenziano 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록·HTML 본문 확인, high 신뢰도 출처는 ETRI 동향 1건이며 단일 출처). 분류 원문 핵심 질문(대화 지시→확인 가능한 계획→승인→실행·진행 설명)에는 f3·f4·f5·f6(분해·배정 가능), f8·f9·f10(실행 전 검증·승인 설계 존재), f13·f14·f15·f17(기록 근거 진행·실패 설명과 관제 상태 기록), f19·f20(도구 호출 직결 구현의 승인 부재)로 답했으며 결론은 '세 단계 각각의 연구·오픈소스는 있으나 셋을 하나의 승인 관문이 있는 흐름으로 이은 운영 사례는 확인되지 않았고 산업 배포 근거는 드물다'는 추정(f7·f11·f16·f20·f26)이다. 현장 유형: 병원(f25, 원문 미열람 명시), 실외(f13, 정밀 농업), 가정(f8, 데이터셋 기준)만 확인했고 물류창고·제조 공장·상업 시설 사례는 없다. L. AI·학습 기술 관련 finding(f1~f6·f8·f9·f12·f14·f28)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·13. 대화형 기능의 신뢰·기반 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 848건과의 URL 중복을 대조하지 못했으므로 서베이·SMART-LLM·ROSA 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시·구조화 출력·팬아웃·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-29-05/verification.json

```json
{
  "run_id": "2026-09-29-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2502.03814 초록(v1 2025-02-06, v5 2026-05-03)에 네 층 분류·'first dedicated review'·coordination·scalability·real-world adaptability 가 그대로 있다. 서베이 자체 진술이므로 단일 출처로 충분."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. HTML 본문(v5) 4.4절에서 Hunt 외의 실행 전 승인, VADER 의 도움 요청(HRFS), Li 외(HMCF)의 사람 검증, 사람 개입이 LLM 실패 완화용 반응적 역할이라는 지적, 팀 규모에 따른 인지 부담 미정량화 문장을 모두 봤다. 서베이가 인용한 원 논문은 열지 않음(브리프도 표시)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2309.10062 초록(v1 2023-09-18, v2 2024-03-23)에 작업 분해·연합 형성·작업 배정, 소수 예시 프로그램형 프롬프트, 네 복잡도 범주 벤치마크, 시뮬레이션·실기 평가가 있다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2411.09022 초록(v1 2024-11-13, v2 2025-03-04)과 글자 단위로 일치(DAG, 네 모듈, 세 복잡도, DeepSeek-r1-671B 최고 성공률, Llama-3.1-8B 응답 시간, 절제 실험). 수치는 저자 실험 조건."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2510.07417 초록(2025-10-08)과 일치. 원문은 'hybrid decentralized framework' 라고 하므로 페이지에서 '2단계 혼합 방식' 서술은 유지 가능."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인·교차 확인. SMART-LLM(Purdue)·DART-LLM(도쿄대)·FLEET(JHU APL) 세 출처를 각각 열어 자연어 지시의 분해와 이기종 로봇 배정을 초록에서 확인. 발행 주체가 다르고 서로 인용 관계가 아니다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 근거 f4·f5 가 살아남았고 원문 주석(업무 지시는 25·26번의 짝)과 대조한 구축자 추정임이 발췌에 드러나 있다. 페이지에서 추정 주체를 밝힌다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2507.05118 초록(2025-07-07, IROS 2025)에 자연어→LTL, 논리 일관성·누락 단계, 실행 전, 가정 작업 데이터셋, 코드 공개가 있다. site_type '가정' 은 데이터셋 기준이며 실제 현장 사례가 아니므로 5절 적용 사례로 세우지 않는다(required_fixes)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2505.00820 초록(2025-05-01)에 로봇별 LLM 에이전트, 작업 검증·사람 감독으로 환각 감소, 필요할 때만 개입, +4.76%, 실세계 제로샷이 있다. 수치는 저자 실험 조건, 단일 출처."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인·교차 확인(부분 정정). 서베이(Drexel)·HMCF(Southampton)·VerifyLLM(AIRI/MIPT) 세 출처를 열어 실행 전 검증·승인 설계를 확인. 다만 서베이가 정리한 Hunt 외의 실행 전 승인과 HMCF 는 저자(W. Hunt, S. Stein)가 겹쳐 같은 연구 그룹으로 봐야 하므로 '서로 다른 세 연구 그룹' 은 '서로 다른 두 연구 그룹 이상' 으로 고친다. VerifyLLM 이 독립 출처이므로 교차 확인은 성립."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 근거 f2·f8·f9 가 모두 살아남았다. 구축자 추정임을 페이지에서 밝힌다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2511.22354 초록(v1 2025-11-27, v2 2026-06-18, Frontiers in Robotics and AI 채택)에 중앙 숙고·분산 실행, 정적 규칙+동적 문맥, 로봇별 지역 LLM 코드 생성, 실패·의도 변경 촉발 재계획, 9/10·8/8·5/5, 22개 시나리오 0.91 이 있다. 지역 LLM 코드 생성 부분은 연계 대상(f27)으로 서술."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2509.16006 초록(2025-09-19)에 LLM+자동 계획, 자연어 활동 지정, 로봇 질의로 실행 모니터링, 실제 정밀 농업 시나리오가 있다. site_type 실외는 초록의 real-world precision agriculture 에 근거."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2306.15724 초록(v1 2023-06-27, v4 2023-10-16, CoRL 2023)에 계층적 경험 요약 기반 실패 추론, 교정 계획, RoboFail 데이터셋이 있다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인·교차 확인. REFLECT(Columbia)·Argenziano 외(Sapienza) 두 출처를 열어 실행 기록·경험 요약 근거의 설명·질의 응답을 각각 확인. 독립 연구 그룹."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 근거 f14·f15·f17 이 살아남았고 task_state.json 원문(입력 텍스트)에 phases/events/estimate_millis/assigned_to 가 있다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력의 data/source_texts/ref-111.txt(github_raw 원문)와 대조: status enum 12개 값, active, estimate_millis, assigned_to(group·name), phase 별 start/finish/estimate/events/skip_requests, interruptions, cancellation 모두 일치. 발행일 미확인(스키마 파일), 확인일 기준."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력의 ref-110.txt(task_new.md)·ref-125.txt(task_request.json) 원문과 대조: 단계(phase) 구성, Clean·Compose·Delivery·Patrol, robot_task_request/dispatch_task_request, required [category, description], 나머지 선택, 취소·단계 건너뛰기 문장 일치. 발행일 미확인."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(문구 정정 필요). Discourse 글을 열었다. MCP 서버·평이한 영어 명령→다단계 RMF 임무·Nayantra 언급과 승인·상태 질의 언급 부재를 확인. 다만 이 글은 2026-06-25 에 게시된 세션 '공지' 이며 세션이 실제로 그 내용을 다뤘는지는 확인할 수 없으므로 '세션에서 다뤘으며' 는 '세션 공지에서 다룬다고 밝혔으며' 로 고치고 ref-862 발행일을 2026-06-25(세션 2026-07-02)로 정정한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 근거 f18·f19 가 살아남았고 원문 '승인된 계획만 실행' 과 대조한 구축자 추정임이 드러나 있다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2410.06472 초록(v1 2024-10-09, v2 2025-02-13, IEEE Aerospace 2025)에 ROS 1·2, 매개변수 검증·제약 강제, 오픈소스, JPL Mars Yard·실험실·시뮬레이션 세 로봇 시연이 있다. ROS 직접 조작 에이전트이므로 7절에서는 연계 대상(f27)으로 표시."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2510.10379 초록(2025-10-12)과 일치(오픈소스, 컨테이너 서비스, LLM 중앙 계획·스케줄링, 공유 선언형 세계 상태, 양방향 통신, 모듈형 층)."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2605.02592 초록(2026-05-04)과 글자 단위로 일치(88편, 75.0% TRL 4-6, 9.1%, +37%·+35%, 네 가지 한계). 산업 자동화 일반(로봇 한정 아님) 문헌 고찰임을 페이지에서 밝힌다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ETRI 전자통신동향분석 39(1), 2024-02 를 열어 명령→요소 기술 분해 작업 계획·제어 코드 생성(SayCan, PaLM-E, Code as Policies), 다중 로봇·사람 승인 미언급, 계산 자원·데이터·시뮬레이션·테스트베드 집중 한계를 확인. 단일 출처."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(Springer 인증 리다이렉트, 재시도 실패). WebSearch 결과에서 기관(Autonomous Robots, Springer)·제목·URL 일치, 저자 Chiang, Y.-C., Lee, I.-P., Fu, L.-C., 2026 을 확인. 스니펫은 자연어 지시→작업 순서열, 유전 알고리즘 재스케줄링, 시각-언어 추론 복구, Temi·안드로이드 앱, 간호 인력 긍정 피드백을 담지만 '국립대만대학병원' 은 스니펫에 없으므로 그 구절은 삭제하거나 미확인 표시(required_fixes). 이 출처에 기댄 주장은 medium 상한."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 근거 f5·f8·f12·f17·f18 이 모두 살아남았다. 배정·일정 계산과 실행 중 재계획을 각각 25·26번, 32번 범위로 넘긴 서술이 원문 19장·교차 규칙과 맞는다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지, '연계 대상: ' 표시 적정. CoMuRoS 지역 LLM 코드 생성과 ROSA ROS 직접 제어는 원문 19장 '로봇 자체 지능·제어' 열에 해당한다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. [추정] 유지. 원문 교차 규칙(학습 기반 배정은 25번, 업무 지시는 25·26번)에 따른 연결 제안이며 근거 f1·f8·f23 이 살아남았다."
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
      "f25(ref-847) 는 이전 실행 2026-09-29-04 의 f21(ref-242 로 낸 병원 논문, 같은 URL)과 같은 주장이다 — 새 각주를 만들지 말고 퍼블리셔가 같은 URL 의 기존 id 로 합치며, 9. 채팅으로 시나리오 구성 페이지의 같은 문장과 충돌하지 않는다",
      "f17(ref-111 task_state 상태 값)은 이전 실행 2026-09-25-31 f12 와, f18(ref-110·ref-125 작업 요청)은 2026-09-29-04 f17·f18 과 같은 출처·같은 내용이다 — 기존 각주 id(ref-110·ref-111·ref-125)를 재사용하고 있으므로 문제 없음",
      "ref-165(서베이)·ref-090(SMART-LLM)·ref-859(ROSA)·ref-453(REFLECT)은 참고문헌 전체 목록(848건)과 URL 대조를 하지 못했다 — 같은 URL 이 있으면 퍼블리셔가 기존 id 로 합친다"
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
    "ref-862: 각주 발행일을 2026-07-02 에서 2026-06-25(게시일)로 고치고 제목 그대로 두며, f19 를 쓰는 문장은 '2026-07-02 세션에서 다뤘으며' 가 아니라 '2026-07-02 세션 공지(2026-06-25 게시)에서 … 다룬다고 밝혔으며' 로 쓴다 — 열어 본 출처는 세션 공지이고 세션의 실제 진행·내용은 확인되지 않았다.",
    "f25/ref-847: 본문과 5절 병원 사례에서 '국립대만대학병원' 구절을 삭제하거나 '(병원 이름 미확인)' 으로 바꾼다 — 원문 미열람이며 검색 결과 요약에는 '간호 인력의 긍정적 피드백' 만 있고 병원 이름은 없다. ref-847 의 저자는 검색 결과 기준 'Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer)' 로 적고, 각주 접근일 뒤에 ' (원문 미열람)' 을 붙이며 reference_updates 의 이 항목에 source_unopened: true 를 넣는다. 기준일은 '2026(발행월 미확인)' 으로 남긴다.",
    "f10: '서로 다른 세 연구 그룹' 을 '서로 다른 두 연구 그룹 이상' 으로 고친다 — 서베이가 정리한 Hunt 외의 실행 전 승인과 HMCF(ref-855)는 저자(W. Hunt, S. Stein)가 겹치는 같은 그룹이고, VerifyLLM(ref-753) 만 독립이다. [사실] 태그와 교차 확인 표시는 유지한다.",
    "f8: 5절 적용 사례에 '가정' 현장 유형 사례로 세우지 않고 site_matrix_updates 에 가정 칸을 넣지 않는다 — VerifyLLM 의 평가는 가정 작업 데이터셋이며 실제 현장 적용이 아니다. 6절(대표 접근법)에서만 다루고 '가정 작업 데이터셋으로 평가(실제 현장 아님)' 을 명시한다.",
    "5절 적용 사례: 병원(f25)·실외(f13) 두 사례만 세우고, 사례마다 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과) 가운데 출처로 확인되지 않은 항목은 채우지 말고 '미확인' 으로 남긴다 — 병원 사례는 원문 미열람, 실외 사례는 초록만 확인했다. 물류창고·제조 공장·상업 시설 사례는 없다고 밝힌다.",
    "f12(CoMuRoS 의 로봇별 지역 언어 모델 코드 생성)와 f21(ROSA 의 ROS 직접 조작)은 6절·7절에서 소개하되 f27 대로 '연계 대상(로봇 자체 지능·제어)' 임을 같은 문단에서 밝히고 ROP 가 직접 맡는 기능처럼 쓰지 않는다.",
    "f23: 3절·8절에서 '산업 자동화 일반(로봇 한정 아님)의 기반 모델 에이전트 문헌 고찰' 임을 명시하고, 75.0%·9.1% 수치는 그 문헌 집합에 대한 값임을 밝힌다.",
    "f7·f11·f16·f20·f26·f27·f28: [추정] 문장마다 '구축자 추정' 임을 밝히고 근거 finding 의 각주를 붙인다.",
    "f4·f9·f12 의 성공률·정확도 수치는 '저자 실험 조건' 을 병기한다 — 단일 출처이며 교차 확인되지 않았다.",
    "ref-165 각주는 열람한 판(v5, 2026-05-03)을 발행일 뒤 괄호로 밝힌다 — f2 는 v1 초록이 아니라 v5 HTML 본문 4.4절에 근거한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 28건(그중 f25 는 원문 미열람으로 검색 결과 일치만 확인), 미확인 0건, 교차 확인 3건(f6, f10, f15). 강등: 없음. 원문 미열람 출처: ref-847(Springer 인증 리다이렉트). 주의: [사실] 가운데 f6·f10·f15 를 뺀 나머지는 단일 출처(논문 초록·HTML 본문·오픈소스 스키마)라 페이지 신뢰도는 medium 이다. f10 의 Hunt 외와 HMCF 는 같은 연구 그룹이므로 '세 그룹' 이 아니라 '두 그룹 이상' 이다. ref-862 는 세션 공지(2026-06-25 게시)이며 세션 진행 내용은 확인되지 않았다. f25 의 '국립대만대학병원' 은 검색 결과 요약에 없어 삭제 지시했다. f8 의 site_type '가정' 은 데이터셋 기준이라 적용 사례로 인정하지 않았다. 셋(대화→계획, 승인, 진행 설명)을 하나의 승인 관문 흐름으로 이은 운영 사례는 이번 브리프에서 확인되지 않았고 결론(f7·f11·f16·f20·f26)은 구축자 추정이다. 검증 검색 1회·열람 17회 사용. 정정 요청 없음. 미사용 출처 없음.",
  "retry_reason": null
}
```

### runs/2026-09-29-05/pages.json

```json
{
  "run_id": "2026-09-29-05",
  "outline": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "대화 지시→계획→승인→실행 설명이 한 흐름이어야 하는데 사람 개입은 반응적이고 인지 부담은 미정량화이며(Li 외 서베이) 산업 배포 근거는 드물고(Henkel 외) MCP 도구 호출 직결 구현에는 승인 단계가 드러나지 않는다(OSRA 공지). [사실][^ref-165][^ref-861][^ref-862]",
      "planned_findings": [
        "f2",
        "f23",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "작업 분해·연합 형성·배정, 의존 관계 DAG, 로봇–작업 적합도 행렬, 사전 실행 계획 검증, 감독 제어·실행 전 승인, 실패 설명, 작업 상태·단계·사건 기록, MCP 도구 호출을 정의한다. [사실][^ref-090][^ref-059][^ref-242][^ref-753][^ref-165][^ref-453][^ref-111][^ref-862]",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f8",
        "f2",
        "f14",
        "f17",
        "f19"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1100,
      "summary": "병원(간호 인력의 자연어 지시→작업 순서열, 원문 미열람)과 실외(정밀 농업에서 자연어 활동 지정·질의로 진행 확인) 두 사례만 세우고 미확인 항목은 비운다. [사실][^ref-847][^ref-857]",
      "planned_findings": [
        "f25",
        "f13"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2400,
      "summary": "대화 지시→분해·의존·능력 매칭→형식 배정(SMART-LLM·DART-LLM·FLEET), 자동 검증 후 사람 승인(VerifyLLM·HMCF·서베이), 사건 기반 재계획(CoMuRoS, 코드 생성은 연계 대상), 기록 근거의 진행·실패 설명(Argenziano 외·REFLECT), 승인 관문 위치. [사실][^ref-090][^ref-059][^ref-242][^ref-753][^ref-855][^ref-677][^ref-857][^ref-453]",
      "planned_findings": [
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
        "f14",
        "f15",
        "f16",
        "f18",
        "f20",
        "f27"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "Open-RMF 작업 요청·작업 상태 스키마, OSRA 세션 공지의 MCP 서버, RobotFleet, VerifyLLM 코드, ROSA(연계 대상)를 표로 정리한다. [사실][^ref-125][^ref-110][^ref-111][^ref-862][^ref-777][^ref-753][^ref-859]",
      "planned_findings": [
        "f17",
        "f18",
        "f19",
        "f21",
        "f22",
        "f8",
        "f27"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "서베이·SMART-LLM·DART-LLM·FLEET·VerifyLLM·HMCF·CoMuRoS·Argenziano 외·REFLECT·Henkel 외·ETRI 동향 논문을 한두 문장씩 요약한다. [사실][^ref-165][^ref-090][^ref-059][^ref-242][^ref-753][^ref-855][^ref-677][^ref-857][^ref-453][^ref-861][^ref-858]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f7",
        "f8",
        "f9",
        "f12",
        "f13",
        "f14",
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 대화→작업 그래프, 엔진 결과의 계획 제안, 검증·승인, 관제 작업 요청 변환, 기록 근거 설명을 맡고 로봇 내부 코드 생성·스킬 실행·ROS 직접 제어는 연계 대상이라는 구축자 추정. [추정][^ref-242][^ref-753][^ref-677][^ref-111][^ref-110][^ref-859]",
      "planned_findings": [
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1000,
      "summary": "짝 엔진 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링, 13. 대화형 기능의 신뢰·기반, 32. 예외 복구·재계획·업무 연속성, 37. 관제 화면·실행 기록, 20. 로봇·제조사 관제 연동, 9·10·5·24·44·47·63·66번 영역을 이름과 함께 연결한다. 연결 해석은 모두 구축자 추정으로 표시한다. [추정][^ref-242][^ref-059][^ref-165]",
      "planned_findings": [
        "f7",
        "f28",
        "f11",
        "f16",
        "f12",
        "f17",
        "f18",
        "f19",
        "f20",
        "f26",
        "f5",
        "f9",
        "f4",
        "f25",
        "f13"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "승인 단위·검토 부담, 재계획 시 재승인 범위, MCP 직결 구현의 승인 관문 위치, 국내 운영 사례의 네 질문을 올린다. [사실][^ref-165][^ref-677][^ref-862][^ref-858]",
      "planned_findings": [
        "f2",
        "f12",
        "f19",
        "f24"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3~11절 신규 작성(seed → draft), 출처 18건(ref-165~ref-847, ref-110·ref-111·ref-125 재사용), 병원·실외 사례 2건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 10건과 2차 수정 지시 8건(10절 연결 다섯 항목·8절 FLEET·3절 의견 주체·11절 보조 문장의 태그·문구 수정) 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"6. 대표 접근법과 기술\" 절(3,807자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"8. 대표 연구와 자료\" 절(1,970자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,291자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,270자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"4. 핵심 개념과 용어\" 절(1,255자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"3. 왜 중요한가\" 절(1,149자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area12-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 \"11. 열린 질문\" 절(852자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 12. 채팅으로 업무 지시·오케스트레이션 | 3~11절 신규 작성(seed → draft), 출처 18건, 병원·실외 사례 2건, 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 10건과 2차 수정 지시 8건 이행 | run 2026-09-29-05",
  "index_updates": {
    "home_recent": "2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft). 언어 모델 작업 분해·배정(SMART-LLM·DART-LLM·FLEET), 실행 전 검증·승인(VerifyLLM·HMCF), 기록 근거의 진행·실패 설명, Open-RMF 작업 요청·상태 스키마와 MCP 서버 공지를 정리. 출처 18건, 병원·실외 사례 2건, 열린 질문 4건",
    "category_recent": "2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft), 출처 18건(ref-165~ref-847, ref-110·ref-111·ref-125 재사용), 병원·실외 사례 2건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 10건과 2차 수정 지시 8건 이행 (실행 2026-09-29-05)",
    "area_recent": "2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft). 대화 지시→작업 그래프→배정 엔진→사전 검증→사람 승인→관제 작업 요청→상태 기록 근거 설명의 흐름을 구축자 추정으로 정리하고, 승인 단위·재승인 범위·MCP 승인 관문·국내 사례의 열린 질문 4건을 올림 (실행 2026-09-29-05)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "pre-execution-plan-verification",
      "term_ko": "사전 실행 계획 검증",
      "term_en": "Pre-execution Plan Verification",
      "definition": "언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다.",
      "description": "VerifyLLM(IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈이며, 가정 작업 데이터셋으로 평가하고 코드를 공개했다. 분류 원문의 \"사람이 확인·승인한 계획만 실행\" 앞단에서 승인자의 검토 부담을 줄이는 자동 관문으로 쓸 수 있다는 것이 구축자 추정이다.",
      "related_areas": [
        12,
        13,
        44,
        54
      ],
      "sources": [
        "ref-753"
      ]
    },
    {
      "action": "new",
      "slug": "supervisory-control",
      "term_ko": "감독 제어",
      "term_en": "Supervisory Control",
      "definition": "사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다.",
      "description": "Li 외(2025)의 다중 로봇 언어 모델 서베이는 실행 전 사람 승인(Hunt 외), 로봇의 도움 요청(VADER), 사람 검증(HMCF)을 사람 개입의 예로 들면서, 사람이 반응적 역할에 머물고 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다고 지적했다.",
      "related_areas": [
        12,
        13,
        31
      ],
      "sources": [
        "ref-165",
        "ref-855"
      ]
    },
    {
      "action": "new",
      "slug": "failure-explanation",
      "term_ko": "실패 설명",
      "term_en": "Failure Explanation",
      "definition": "로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다.",
      "description": "REFLECT(CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하며, RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다.",
      "related_areas": [
        12,
        32,
        38
      ],
      "sources": [
        "ref-453"
      ]
    },
    {
      "action": "new",
      "slug": "robot-task-fitness-matrix",
      "term_ko": "로봇–작업 적합도 행렬",
      "term_en": "Robot–Task Fitness Matrix",
      "definition": "로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다.",
      "description": "FLEET(2025)에서 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 함께 만들며, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀 때 능력 매칭 근거로 쓴다. 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했다.",
      "related_areas": [
        12,
        25,
        5
      ],
      "sources": [
        "ref-242"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-165",
      "org": "Li, P., An, Z., Abrar, S., & Zhou, L.",
      "title": "Large Language Models for Multi-Robot Systems: A Survey",
      "published": "2025-02-06",
      "url": "https://arxiv.org/abs/2502.03814",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델을 다중 로봇 시스템에 쓰는 연구를 상위 작업 배정·중간 동작 계획·하위 행동 생성·사람 개입의 네 층으로 정리한 서베이. v5(2026-05-03)의 HTML 본문에서 사람 개입 절과 배정 프레임워크 비교를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09-18",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "상위 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸는 소수 예시 프롬프트 틀. 네 복잡도의 벤치마크·시뮬레이션·실기로 평가.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-059",
      "org": "Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H.",
      "title": "DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models",
      "published": "2024-11-13",
      "url": "https://arxiv.org/abs/2411.09022",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 지시를 DAG 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀. 모델별 성공률·응답 시간과 의존 모델링 절제 실험을 보고.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-242",
      "org": "Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.",
      "title": "FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams",
      "published": "2025-10-08",
      "url": "https://arxiv.org/abs/2510.07417",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델이 작업 그래프와 로봇–작업 적합도 행렬을 만들고 형식 최적화기가 완료 시간 최소화로 배정하는 2단계 혼합 방식. 사족 로봇 실기 검증.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
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
      "summary": "자연어 지시를 LTL 로 옮긴 뒤 행동 순서열의 논리 일관성과 누락 단계를 실행 전에 찾는 검증 모듈. 가정 작업 데이터셋으로 평가, 코드 공개.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-777",
      "org": "Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J.",
      "title": "RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning",
      "published": "2025-10-12",
      "url": "https://arxiv.org/abs/2510.10379",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 기반 중앙 집중식 다중 로봇 작업 계획·스케줄링 오픈소스 프레임워크. 컨테이너화된 로봇, 공유 선언형 세계 상태, 실행·재계획용 양방향 통신.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-855",
      "org": "Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S.",
      "title": "HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models",
      "published": "2025-05-01",
      "url": "https://arxiv.org/abs/2505.00820",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "로봇별 언어 모델 에이전트가 작업 검증으로 환각을 줄이고 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀. 시뮬레이션 성공률 +4.76%, 실세계 제로샷.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-677",
      "org": "Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정)",
      "title": "LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning",
      "published": "2025-11-27",
      "url": "https://arxiv.org/abs/2511.22354",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "CoMuRoS: 중앙 작업 관리자 언어 모델이 자연어 목표를 배정하고 로봇별 지역 언어 모델이 실행 코드를 만들며 실패·의도 변경 시 사건 기반으로 재계획하는 구조. 실기 복구·운반 결과와 22개 시나리오 벤치마크.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-857",
      "org": "Argenziano, F., Umili, E., Leotta, F., & Nardi, D.",
      "title": "Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning",
      "published": "2025-09-19",
      "url": "https://arxiv.org/abs/2509.16006",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델과 자동 계획을 결합해 자연어로 활동을 지정하고 로봇에 질문해 실행 진행을 확인하는 구조. 실제 정밀 농업 시나리오에서 시험.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-858",
      "org": "한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1))",
      "title": "거대언어모델 기반 로봇 인공지능 기술 동향",
      "published": "2024-02",
      "url": "https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "언어 모델로 로봇 명령 이해·요소 기술 분해 작업 계획·제어 코드 생성을 자동화하는 흐름(SayCan, PaLM-E, Code as Policies 등)을 정리한 ETRI 동향 논문. 다중 로봇·사람 승인은 다루지 않음.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-859",
      "org": "Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025)",
      "title": "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent",
      "published": "2024-10-09",
      "url": "https://arxiv.org/abs/2410.06472",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "ROS 1·2 로봇을 자연어로 점검·진단·조작하는 오픈소스 언어 모델 에이전트. 매개변수 검증·제약 강제 안전 장치, 화성 실험장·실험실·시뮬레이션 시연.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-453",
      "org": "Liu, Z., Bahety, A., & Song, S. (CoRL 2023)",
      "title": "REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction",
      "published": "2023-06-27",
      "url": "https://arxiv.org/abs/2306.15724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "다중 감각 관측의 계층적 경험 요약을 근거로 언어 모델이 실패를 설명하고 교정 계획을 돕게 하는 틀. RoboFail 데이터셋.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-861",
      "org": "Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y.",
      "title": "Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges",
      "published": "2026-05-04",
      "url": "https://arxiv.org/abs/2605.02592",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "산업 자동화 일반(로봇 한정 아님)의 기반 모델 에이전트 88편 체계적 문헌 고찰. 75.0% 가 TRL 4~6, 배포 근거 9.1%, 환각·출력 불안정·지연이 과제.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-862",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse",
      "title": "Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-06-25",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "OSRA 상호운용 SIG 2026-07-02 세션의 공지(2026-06-25 게시). Open-RMF REST API 를 MCP 도구로 노출하고 영어 명령을 다단계 RMF 임무로 바꾸는 에이전트(Nayantra)를 다룬다고 밝혔다. 승인·상태 질의 언급 없음. 세션의 실제 진행 내용은 확인되지 않았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-847",
      "org": "Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer)",
      "title": "Agile assistive hospital robot for suboptimal Task execution in dynamic environments",
      "published": "2026",
      "url": "https://link.springer.com/article/10.1007/s10514-026-10255-6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 병원 보조 로봇이 간호 인력의 자연어 지시를 작업 순서열로 바꾸고 실행 중 추가 요청에 유전 알고리즘으로 재스케줄링하며 실패를 시각-언어 추론으로 복구하는 시스템(Temi 로봇·안드로이드 앱). 병원 이름·정량 결과·승인 절차는 미확인. 이전 실행 2026-09-29-04 의 ref-242 와 같은 URL 이므로 퍼블리셔가 기존 id 로 합칠 수 있다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-110",
      "org": "Open Robotics",
      "title": "Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/task_new.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 구성(단계·범주·compose)과 robot_task_request·dispatch_task_request, 취소·단계 건너뛰기 설명.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 상태 JSON 스키마: 상태 값, 활성 단계, 추정 시간, 배정 로봇, 단계별 사건, 중단·취소 요청 기록.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 작업 요청 JSON 스키마: category·description 필수, 시작 시각·우선순위·라벨·요청자·플릿 이름 선택.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가?",
      "areas": [
        12,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가?",
      "areas": [
        12,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가?",
      "areas": [
        12,
        20,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)?",
      "areas": [
        12,
        61,
        63,
        62
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시",
      "title": "12. 채팅으로 업무 지시·오케스트레이션"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시",
      "title": "12. 채팅으로 업무 지시·오케스트레이션"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시",
      "title": "12. 채팅으로 업무 지시·오케스트레이션"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시",
      "title": "12. 채팅으로 업무 지시·오케스트레이션"
    },
    {
      "site_type": "실외",
      "item": "완료·인계",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시",
      "title": "12. 채팅으로 업무 지시·오케스트레이션"
    }
  ],
  "standards_updates": [
    {
      "name": "VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개)",
      "kind": "오픈소스",
      "org": "Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025)",
      "url": "https://arxiv.org/abs/2507.05118",
      "related_areas": [
        12,
        13,
        44,
        54
      ],
      "summary": "자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리 일관성과 누락 단계를 실행 전에 찾는 2단계 검증 모듈. 가정 작업 데이터셋으로 평가(실제 현장 아님)했으며 코드를 공개했다.",
      "ref_id": "ref-753"
    }
  ],
  "additional_research_requests": [
    "5절 적용 사례에 물류창고·제조 공장·상업 시설에서 대화로 여러 로봇에 업무를 지시한 실제 사례가 필요하다 — 이번 브리프는 병원(원문 미열람)·실외(초록만) 두 사례뿐이다. MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(403 으로 미열람)를 다시 열어 제조 공장 사례로 쓸 수 있는지 확인이 필요하다.",
    "5절 병원 사례(ref-847)의 작업 대상·제약·완료·인계 항목과 정량 결과, 실행 전 사람 승인 절차 유무가 필요하다 — Springer 원문을 열지 못해 검색 결과 요약 범위만 옮겼다. 원문 열람(또는 저자 공개 판) 뒤 여섯 항목을 채워야 한다.",
    "6절 실행 중 재계획 절에 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)이 필요하다 — 검색 결과 요약에서만 보여 finding 에 넣지 못했다. 논문 본문에서 확인이 필요하다.",
    "3절·11절의 승인 부담 논의에 승인 단위(전체 계획 1회·단계별·변경분만)와 로봇 수에 따른 검토 부담을 다룬 연구가 필요하다 — 서베이는 미정량화만 지적했다. 예산 상한으로 넣지 못한 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)를 다음 실행에서 확인하면 6·8절을 보강할 수 있다.",
    "7절에 OSRA 세션의 실제 발표 자료·MCP 서버 저장소 URL 이 필요하다 — 이번에는 세션 공지(2026-06-25 게시)만 확인했고 세션 진행 내용과 승인 관문 유무는 미확인이다.",
    "8절·11절의 국내 자료에 ETRI 동향 논문 외의 국내 대화형 업무 지시 사례가 필요하다 — 한국어 검색에서 찾은 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 대화형 지시가 아니어서 제외됐다.",
    "10절 연결 항목 가운데 '9. 채팅으로 시나리오 구성이 기한·반복·실패 처리 조건을 정해 이 영역의 지시에 넣는다'와 '로봇–작업 적합도 행렬(FLEET)·로봇별 능력 이해(HMCF)가 능력 표현을 전제한다'는 연결은 브리프에 finding 이 없어 [추정]으로 남겼다 — 두 연결을 뒷받침하는 출처(FLEET·HMCF 본문의 능력 표현 형식, 시나리오 모델과 작업 요청의 필드 대응)를 다음 실행에서 확인하면 [사실]로 올릴 수 있다."
  ],
  "fixes_applied": [
    "ref-862 발행일·f19 문구 — 13절 각주와 reference_updates 의 ref-862 발행일을 2026-06-25 로 고치고 제목은 그대로 두었으며, 3절·4절·7절에서 f19 를 쓰는 문장을 '2026-07-02 세션 공지(2026-06-25 게시)에서 … 다룬다고 밝혔으며' 형식으로 썼다. 7절 표에도 '공지에서 밝힘' 으로 적었다.",
    "f25/ref-847 병원 이름·저자·미열람 표시 — 5절 병원 사례 표와 서술, 10절 63. 병원·의료 연결에서 '국립대만대학병원' 을 빼고 '(병원 이름 미확인)' 으로 썼으며, 각주 저자를 'Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer)' 로 적고 접근일 뒤에 ' (원문 미열람)' 을 붙였고, reference_updates 의 ref-847 에 source_unopened: true 를 넣었다. 기준일은 '2026(발행월 미확인)' 으로 남겼다.",
    "f10 연구 그룹 수 — 6절 '실행 전 자동 검증과 사람 승인' 의 교차 확인 문장을 '서로 다른 두 연구 그룹 이상(Hunt 외의 실행 전 승인과 HMCF 는 저자가 겹치는 같은 그룹, VerifyLLM 은 독립 그룹)' 으로 고쳤다. [사실] 태그와 세 각주(ref-165·ref-855·ref-753)는 유지했다.",
    "f8 가정 현장 유형 제외 — 5절에 '가정' 사례를 세우지 않았고 site_matrix_updates 에 가정 칸을 넣지 않았다. VerifyLLM 은 4절 용어와 6절·7절·8절에서만 다루고 '가정 작업 데이터셋으로 평가(실제 현장 아님)' 을 명시했다.",
    "5절 사례 범위·미확인 처리 — 병원(f25)·실외(f13) 두 사례만 세우고, 병원 사례는 작업 대상·제약·완료·인계를, 실외 사례는 작업 대상·수행 자원·제약·예외·성과를 '미확인' 으로 남겼으며, 절 첫머리에 물류창고·제조 공장·상업 시설 사례가 없다고 밝혔다. site_matrix_updates 는 채운 칸(병원 3칸, 실외 2칸)만 냈다.",
    "f12·f21 연계 대상 표시 — 6절 '실행 중 재계획과 사람 도움 요청' 에서 CoMuRoS 의 로봇별 지역 언어 모델 코드 생성을 같은 문단에서 '로봇 자체 지능·제어 연계 대상' 으로 밝혔고, 7절 표 아래 문단에서 ROSA 를 같은 이유로 연계 대상이라고 적었으며 9절 표의 '외부와 연계하는 것' 열에도 두 항목을 두었다. ROP 가 직접 맡는 기능처럼 쓰지 않았다.",
    "f23 문헌 고찰 범위 — 3절과 8절에서 '산업 자동화 일반(로봇 한정 아님)의 기반 모델 에이전트 문헌 고찰(88편)' 임을 명시하고, 75.0%·9.1% 수치가 '그 문헌 집합에서 보고된 시스템' 에 대한 값임을 밝혔다.",
    "[추정] 문장의 구축자 추정 표시·각주 — f7(6절·10절), f11(6절), f16(6절), f20(3절·6절), f26(9절), f27(6절·7절·9절), f28(10절)을 쓴 모든 문장을 '…라는 것이 구축자 추정이다' 형식으로 쓰고 근거 finding 의 출처 각주(f7: ref-242·ref-059, f11: ref-165·ref-753·ref-855, f16: ref-453·ref-857·ref-111, f20: ref-862·ref-110·ref-125, f26: ref-242·ref-753·ref-677·ref-111·ref-110, f27: ref-677·ref-859·ref-110, f28: ref-165·ref-861·ref-753)를 붙였다.",
    "f4·f9·f12 수치의 저자 실험 조건 병기 — 6절과 8절에서 DART-LLM 의 모델별 성공률·응답 시간, HMCF 의 +4.76%, CoMuRoS 의 9/10·8/8·5/5·0.91 을 쓴 문장마다 '(저자 실험 조건)' 을 병기했다.",
    "ref-165 열람 판 표시 — 13절 각주를 '2025-02-06 (열람 판 v5 2026-05-03)' 으로 쓰고, 3절과 8절의 f2 서술에 '2026-05-03 판 기준' 을 밝혔다.",
    "2차: 10절 37. 관제 화면·실행 기록 항목 — 세부영역 페이지 10절 원문에서 '…작업 상태·단계·사건 기록(Open-RMF task_state)을 이 영역이 조회한다는 것이 구축자 추정이다. [추정][^ref-111]' 로 고쳤다(f16 태그 복원). 분리 페이지는 코드가 다시 만들도록 출력에 넣지 않았다.",
    "2차: 10절 20. 로봇·제조사 관제 연동 항목 — '…MCP 서버로 관제 API를 노출하는 구현이 이 연동을 통과한다는 것이 구축자 추정이다. [추정][^ref-110][^ref-125][^ref-862]' 로 고쳤다(f20 태그 복원, 각주 세 개 유지).",
    "2차: 10절 32. 예외 복구·재계획·업무 연속성 항목 — 두 문장으로 나눠 'CoMuRoS는 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획하고 필요하면 로봇이 사람 도움을 요청하게 한다고 보고했다. [사실][^ref-677]' 와 '이 재계획이 승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다는 것이 구축자 추정이다. [추정][^ref-677]' 로 썼다(f12 사실·f26 추정 분리).",
    "2차: 10절 9. 채팅으로 시나리오 구성 항목 — '…시나리오 모델에서 정해져 이 영역의 지시에 들어온다는 것이 구축자 추정이다. [추정][^ref-125]' 로 고쳤다(finding 없는 연결 해석을 추정으로 강등). 근거 확인 요청을 additional_research_requests 에 더했다.",
    "2차: 10절 10. 채팅으로 로봇 구성 · 5. 로봇 능력·작업 표현 항목 — '…능력 표현이 있어야 성립한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-855]' 로 고쳤다(초록에 없는 해석을 추정으로 강등).",
    "2차: 8절 FLEET 항목 — [사실] 문장을 '…2단계 혼합 방식. [사실][^ref-242]' 에서 끝내고, 역할 분담 구절을 '이 방식을 이 영역과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 역할 분담 근거로 삼는다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]' 로 따로 썼다(f7 추정 분리).",
    "2차: 3절 첫 문장 — 세부영역 페이지 3절 원문을 '…로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]' 으로 고쳤다. 코드가 다시 분리하는 주제 페이지의 1절·3절에도 같은 문장이 옮겨진다.",
    "2차: 11절 두 번째 열린 질문 보조 문장 — 'CoMuRoS는 사건 기반 재계획을 보고했지만 재승인 기준은 초록에서 확인되지 않았다. [사실][^ref-677]' 로 고쳤다(초록 범위를 넘는 부재 진술 제거).",
    "분량 초과 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 본문 13,989자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,201자"
  ]
}
```

### runs/2026-09-29-05/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area12-s6.md (3,807자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area12-s8.md (1,970자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area12-s7.md (1,291자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area12-s10.md (1,270자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area12-s4.md (1,255자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area12-s3.md (1,149자)
    - docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area12-s11.md (852자)
```

### runs/2026-09-29-05/pages/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [언어 모델 작업 분해, 실행 전 승인, 사전 실행 계획 검증, 작업 상태 질의, 모델 컨텍스트 프로토콜, 이기종 로봇 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-165, ref-090, ref-059, ref-242, ref-753, ref-777, ref-855, ref-677, ref-857, ref-858, ref-859, ref-453, ref-861, ref-862, ref-847, ref-110, ref-111, ref-125]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 12. 채팅으로 업무 지시·오케스트레이션

# 12. 채팅으로 업무 지시·오케스트레이션

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

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]

## 3. 왜 중요한가

대화로 받은 지시가 로봇 동작으로 이어지려면 지시를 계획으로 바꾸는 일, 그 계획을 사람이 확인·승인하는 일, 실행 뒤 진행을 설명하는 일이 한 흐름으로 이어져야 하며, 이 영역은 C. 채팅 기반 구성·운영 가운데 로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 왜 중요한가](../../topics/2026/2026-09-29-area12-s3.md)에 있다.

## 4. 핵심 개념과 용어

**[작업 분해](../../glossary/task-decomposition.md)·[연합 형성](../../glossary/coalition-formation.md)·작업 배정(Task Decomposition, Coalition Formation, Task Allocation)** — SMART-LLM은 상위 작업 지시를 이 세 단계로 나누어 다중 로봇 작업 계획으로 바꾸고, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시킨다. [사실][^ref-090]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area12-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 현장 유형은 병원과 실외(정밀 농업)뿐이며, 물류창고·제조 공장·상업 시설에서 대화로 로봇 업무를 지시한 사례는 확인되지 않았다. 병원 사례는 원문을 열지 못해 검색 결과 요약 범위만 옮겼고, 실외 사례는 논문 초록만 확인했으므로 출처로 확인되지 않은 항목은 "미확인"으로 남긴다.

**현장 유형:** 병원

**사례:** 병원에서 간호 인력이 보조 로봇에게 자연어로 업무를 지시하고 실행 중 추가 요청을 반영

| 항목 | 내용 |
|---|---|
| 시작 조건 | 간호 인력의 자연어 지시가 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바뀌고, 실행 중 들어오는 추가 요청이 재스케줄링을 촉발한다. [사실][^ref-847] |
| 작업 대상 | 미확인(원문 미열람) |
| 수행 자원 | Temi 로봇과 맞춤 안드로이드 앱, 지시를 내리는 간호 인력. [사실][^ref-847] |
| 제약 | 미확인(원문 미열람) |
| 완료·인계 | 미확인(원문 미열람) |
| 예외·성과 | 실행 실패는 시각-언어 추론과 AI 제안으로 복구하며, 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다(정량 결과 미확인). [사실][^ref-847] |

Autonomous Robots(Springer, 2026, 발행월 미확인) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패를 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치했다고 보고했다(병원 이름 미확인, 원문 미열람). [사실][^ref-847] 이 사례에서 이 영역이 관여하는 항목은 시작 조건(대화 지시→작업 순서열)과 예외·성과(실패 복구와 재스케줄링)이며, 실행 전 사람 승인 절차가 있었는지는 확인되지 않았다.

**현장 유형:** 실외

**사례:** 실외 정밀 농업 현장에서 자연어로 활동을 지정하고 로봇에 질의해 실행 진행을 확인

| 항목 | 내용 |
|---|---|
| 시작 조건 | 사람이 자연어로 상위 활동을 지정하면 언어 모델과 자동 계획이 결합된 구조가 이를 실행 가능한 형태로 만든다. [사실][^ref-857] |
| 작업 대상 | 미확인(초록에 없음) |
| 수행 자원 | 미확인(로봇 종류·대수는 초록에 없음) |
| 제약 | 미확인(초록에 없음) |
| 완료·인계 | 사람이 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있다. [사실][^ref-857] |
| 예외·성과 | 미확인(초록에 없음) |

Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다. [사실][^ref-857] 이 사례는 이 영역의 "채팅으로 진행 상황 질의·결과 설명"에 해당하며, 답의 근거가 되는 기록이 어떤 형식인지는 초록에서 확인되지 않았다.

## 6. 대표 접근법과 기술

대화 지시를 다중 로봇 계획으로 바꾸는 연구는 지시를 하위 작업으로 분해하고 의존 관계와 능력에 맞춰 로봇에 배정하는 공통 틀을 갖는다. SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. [사실][^ref-090]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area12-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

ROSA는 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트이므로 분류 원문 19장의 "로봇 자체 지능·제어"에 해당하는 연계 대상이며, CoMuRoS의 로봇별 지역 언어 모델 코드 생성과 마찬가지로 ROP가 직접 맡는 기능이 아니라는 것이 구축자 추정이다. [추정][^ref-859][^ref-677][^ref-110] Open-RMF 관련 항목은 [표준·프레임워크 목록](../../standards/index.md)의 기존 항목이며, 이번 실행에서 새로 든 것은 VerifyLLM이다.

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area12-s7.md)에 있다.

## 8. 대표 연구와 자료

Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey(2025, v5 2026-05-03) — 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정·중간 수준 동작 계획·하위 수준 행동 생성·사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. [사실][^ref-165]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료](../../topics/2026/2026-09-29-area12-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 대화로 받은 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보낸다 | 요청·기한·자원 제약을 내는 업무 시스템 자체(수요예측·구매·재무·전사 자원 계획) |
| 로봇 자체 지능·제어 | 플릿 작업 API 수준의 요청과 상태·실패·완료 확인, 관제의 작업 상태·단계 사건 기록을 근거로 한 진행·실패 설명, 실행 중 재계획을 승인된 계획과의 차이로 표시하는 일 | 로봇별 언어 모델의 실행 코드 생성·스킬 실행(CoMuRoS), ROS 토픽·서비스 직접 조작(ROSA), 센서 인식·SLAM·로컬 회피·모터 제어 |

확인한 자료를 종합하면 이 영역에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것이라는 것이 구축자 추정이다. [추정][^ref-242][^ref-753][^ref-677][^ref-111][^ref-110] 연계 대상인 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 "로봇 자체 지능·제어" 쪽이며, 이종 제조사를 연결하는 ROP는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 한다는 것이 구축자 추정이다. [추정][^ref-677][^ref-859][^ref-110] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) · [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md) — 원문 주석대로 업무 지시가 대화로 부르는 짝 엔진이다. 언어 모델은 작업 그래프·능력 요구를 만들고 실제 배정·일정은 이 두 영역의 엔진이 계산한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area12-s10.md)에 있다.

## 11. 열린 질문

**신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? 서베이는 운영자 인지 부담이 정량화되지 않았다고 지적했다. [사실][^ref-165]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 열린 질문](../../topics/2026/2026-09-29-area12-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-857]: Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning, 2025-09-19, https://arxiv.org/abs/2509.16006, 접근일 2026-09-29
[^ref-859]: Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025), Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent, 2024-10-09, https://arxiv.org/abs/2410.06472, 접근일 2026-09-29
[^ref-847]: Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer), Agile assistive hospital robot for suboptimal Task execution in dynamic environments, 2026, https://link.springer.com/article/10.1007/s10514-026-10255-6, 접근일 2026-09-29 (원문 미열람)
[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 12
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 12. 채팅으로 업무 지시·오케스트레이션

# 12. 채팅으로 업무 지시·오케스트레이션

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

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]

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

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s6.md

````markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-059, ref-090, ref-110, ref-111, ref-125, ref-165, ref-242, ref-453, ref-677, ref-753, ref-855, ref-857, ref-859, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술

# 12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화 지시를 다중 로봇 계획으로 바꾸는 연구는 지시를 하위 작업으로 분해하고 의존 관계와 능력에 맞춰 로봇에 배정하는 공통 틀을 갖는다. SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. [사실][^ref-090]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 대화 지시를 작업 그래프와 배정으로 바꾸기

대화 지시를 다중 로봇 계획으로 바꾸는 연구는 지시를 하위 작업으로 분해하고 의존 관계와 능력에 맞춰 로봇에 배정하는 공통 틀을 갖는다. SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. [사실][^ref-090] DART-LLM(Wang 외, 2024)은 자연어 지시를 DAG로 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀로, 질의응답형 분해 모듈·로봇 배정 함수·구동 모듈·시각-언어 물체 탐지 모듈로 구성되며, 세 복잡도 수준에서 DeepSeek-r1-671B가 최고 성공률을, Llama-3.1-8B가 응답 시간 안정성을 보였고 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다고 보고했다(저자 실험 조건). [사실][^ref-059] FLEET(Rivera 외, 2025)은 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 능력을 반영한 로봇–작업 적합도 행렬을 만들고, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀어 배정하는 2단계 혼합 방식으로, 절제 실험에서 [혼합 정수 계획](../../glossary/milp.md)은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했으며 능력이 다른 사족 로봇 실기로 검증했다. [사실][^ref-242]

서로 다른 세 연구 그룹(SMART-LLM, DART-LLM, FLEET)이 자연어 업무 지시를 언어 모델로 하위 작업으로 분해하고 이기종 로봇에 배정하는 방법을 각각 보고해, "대화 지시→분해→배정" 접근은 한 곳 이상에서 확인된다. [사실][^ref-090][^ref-059][^ref-242] FLEET가 배정·일정은 형식 최적화기에 맡기고 언어 모델은 작업 그래프·능력 매칭에만 쓴 점과 DART-LLM이 의존 관계를 DAG로 명시한 점을 함께 보면, 이 영역의 "업무 파악·분해·배정·일정 제안"은 언어 모델이 대화를 의존 관계 있는 작업 그래프와 능력 요구로 바꾸고 실제 배정·일정은 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)·[26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md)의 엔진에 넘겨 계산한 결과를 계획으로 제안하는 혼합 구조가 원문 주석의 짝 연결과 맞을 것이라는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]

### 실행 전 자동 검증과 사람 승인

언어 모델이 만든 계획을 실행 전에 거르는 설계는 자동 검증과 사람 승인 두 갈래로 보고된다. VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 LTL로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈로, 복잡도가 다른 가정 작업 데이터셋으로 평가(실제 현장 아님)했으며 코드를 공개했다. [사실][^ref-753] HMCF(Li 외, 2025)는 로봇마다 자기 능력을 이해하고 작업을 실행 가능한 지시로 바꾸는 언어 모델 에이전트를 두고, 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀로, 시뮬레이션에서 기존 계획 방법보다 작업 성공률을 4.76% 높이고 실제 환경에서 최소한의 사람 개입으로 제로샷 일반화를 보였다고 보고했다(저자 실험 조건). [사실][^ref-855]

서로 다른 두 연구 그룹 이상(Li 외 서베이가 정리한 Hunt 외의 실행 전 승인과 HMCF의 작업 검증·사람 감독은 저자가 겹치는 같은 그룹이고, VerifyLLM의 자동 사전 검증은 독립 그룹)이 언어 모델이 만든 로봇 계획을 실행 전에 검증하거나 사람이 승인하게 하는 설계를 각각 보고해, "실행 전 검증·승인" 접근은 한 곳 이상에서 확인된다. [사실][^ref-165][^ref-855][^ref-753] 자동 사전 검증과 사람 승인을 함께 보면, 분류 원문의 "사람이 확인·승인한 계획만 실행"은 언어 모델이 낸 계획을 먼저 자동 검증(의존 관계·능력·논리 일관성)으로 걸러 승인자에게는 검토 가능한 구조(작업 그래프·배정·일정)로 보여 주는 방식으로 구현해야 서베이가 지적한 운영자 인지 부담을 줄일 수 있을 것이라는 것이 구축자 추정이다. [추정][^ref-165][^ref-753][^ref-855]

### 실행 중 재계획과 사람 도움 요청

CoMuRoS(Borate 외, 2025)는 중앙 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 작업 이력·로봇 상태 같은 동적 정보로 일을 배정하고, 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 만들며, 실패나 사용자 의도 변경이 생기면 [사건 기반으로 재계획](../../glossary/event-driven-rescheduling.md)해 로봇이 동료를 돕거나 중단된 작업을 재개하거나 사람 도움을 요청하게 하는 중앙 숙고·분산 실행 구조로, 실기에서 협업 복구 9/10·협동 운반 8/8·사람 보조 복구 5/5, 22개 시나리오 벤치마크에서 정확도 최대 0.91을 보고했다(저자 실험 조건). [사실][^ref-677] 이 가운데 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 생성하는 부분은 분류 원문 19장의 "로봇 자체 지능·제어"에 해당하는 연계 대상이며, 이종 제조사를 연결하는 ROP는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 한다는 것이 구축자 추정이다. [추정][^ref-677][^ref-859][^ref-110] 사용자 의도 변경이 재계획을 촉발한다는 점은 이 영역의 대화 지시와 [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)이 맞닿는 지점이다.

### 실행 기록을 근거로 진행과 실패를 설명하기

"어디까지 했는지, 왜 멈췄는지"를 답하는 연구는 대화 기억이 아니라 로봇의 실행 기록을 근거로 삼는다. Argenziano 외(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있게 하는 구조를 실제 정밀 농업 시나리오에서 시험했다. [사실][^ref-857] REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하는 틀로, 다양한 작업·실패 시나리오를 담은 RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다. [사실][^ref-453] 서로 다른 두 연구 그룹이 실행 기록·경험 요약을 근거로 언어 모델이 무엇을 했고 왜 실패했는지를 자연어로 설명하거나 질의에 답하게 하는 방법을 각각 보고해, "실행 기록 근거의 진행·실패 설명" 접근은 한 곳 이상에서 확인된다. [사실][^ref-453][^ref-857]

이 설명 연구와 Open-RMF 작업 상태 스키마가 단계·사건·추정 시간·배정 로봇을 담는 점을 함께 보면, 이 영역의 "채팅으로 진행 상황 질의·결과 설명"은 언어 모델의 대화 기억이 아니라 관제의 작업 상태·단계 사건 기록([37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md))을 조회해 시각과 함께 답하는 방식으로 구현해야 하며, 답에 근거 기록의 식별자·시각을 붙이는 것이 [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)의 근거 표시 요구와 맞을 것이라는 것이 구축자 추정이다. [추정][^ref-453][^ref-857][^ref-111]

### 승인 관문의 위치

Open-RMF는 작업을 단계(phase)로 구성하고 Clean·Delivery·Patrol·Compose 범주의 작업 요청을 특정 로봇 지정(robot_task_request) 또는 최적 플릿 위임(dispatch_task_request)으로 보내며, 요청은 범주(category)와 플릿 지원 스키마를 따르는 설명(description)을 필수로, 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·수행 플릿 이름을 선택으로 두고, 이후 작업 취소나 단계 건너뛰기 요청으로 추가 제어를 할 수 있다(발행일 미확인, 확인일 2026-09-29 기준). [사실][^ref-110][^ref-125] 작업 요청이 범주와 설명만 필수라서 언어 모델 출력으로 바로 만들 수 있고 OSRA 세션 공지의 MCP 서버 구현에는 승인 언급이 없으므로, 승인 관문은 언어 모델의 도구 호출 제안(작업 요청 초안)과 실제 관제 작업 요청 발행 사이에 두어야 한다는 것이 구축자 추정이다. [추정][^ref-862][^ref-110][^ref-125] 위 접근법들을 이 추정에 따라 한 흐름으로 그리면 다음과 같다(구축자 추정을 도식화한 것이며 검증된 운영 사례가 아니다).

```mermaid
flowchart LR
    Chat[대화 지시] --> Graph[작업 그래프와 능력 요구]
    Graph --> Engine[25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링 엔진]
    Engine --> Verify[사전 실행 계획 검증]
    Verify --> Approve[사람 승인 관문]
    Approve --> Request[관제 작업 요청 발행]
    Request --> State[작업 상태·단계 사건 기록]
    State --> Explain[진행·실패 설명]
    Explain --> Chat
```

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-29
[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-453]: Liu, Z., Bahety, A., & Song, S. (CoRL 2023), REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023-06-27, https://arxiv.org/abs/2306.15724, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-855]: Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S., HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models, 2025-05-01, https://arxiv.org/abs/2505.00820, 접근일 2026-09-29
[^ref-857]: Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning, 2025-09-19, https://arxiv.org/abs/2509.16006, 접근일 2026-09-29
[^ref-859]: Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025), Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent, 2024-10-09, https://arxiv.org/abs/2410.06472, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s8.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-059, ref-090, ref-165, ref-242, ref-453, ref-677, ref-753, ref-855, ref-857, ref-858, ref-861]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료

# 12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey(2025, v5 2026-05-03) — 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정·중간 수준 동작 계획·하위 수준 행동 생성·사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. [사실][^ref-165]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey(2025, v5 2026-05-03) — 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정·중간 수준 동작 계획·하위 수준 행동 생성·사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. [사실][^ref-165] 사람 개입 절은 사람이 반응적 역할에 머물고 운영자 인지 부담이 정량화되지 않았다는 빈틈을 지적해 이 영역의 승인 설계 과제를 짚는다. [사실][^ref-165]
- Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM(2023) — 작업 분해·연합 형성·작업 배정의 세 단계를 소수 예시 프롬프트로 수행하는 다중 로봇 작업 계획 틀. 네 복잡도 벤치마크·시뮬레이션·실기 평가. [사실][^ref-090]
- Wang, Y. 외, DART-LLM(2024) — 의존 관계를 DAG로 명시해 다중 로봇이 병렬 실행하게 하는 분해 틀. 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다는 절제 실험(저자 실험 조건). [사실][^ref-059]
- Rivera, C. 외, FLEET(2025) — 언어 모델의 작업 그래프·적합도 행렬과 형식 최적화기의 완료 시간 최소화를 결합한 2단계 혼합 방식. [사실][^ref-242] 이 방식을 이 영역과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 역할 분담 근거로 삼는다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]
- Grigorev, D. S., Kovalev, A. K., & Panov, A. I., VerifyLLM(IROS 2025) — 자연어→LTL 변환과 언어 모델 추론으로 실행 전에 논리 불일치·누락 단계를 찾는 검증 모듈. 가정 작업 데이터셋 평가, 코드 공개. [사실][^ref-753]
- Li, Z. 외, HMCF(2025) — 로봇별 언어 모델 에이전트와 작업 검증·사람 감독으로 환각을 줄이는 사람 참여 루프 협업 틀. 시뮬레이션 성공률 +4.76%, 실세계 제로샷 일반화(저자 실험 조건). [사실][^ref-855]
- Borate, S. 외, CoMuRoS(2025) — 중앙 숙고·분산 실행 구조에서 실패·의도 변경이 촉발하는 사건 기반 재계획과 사람 도움 요청. 실기 복구·운반 결과와 22개 시나리오 벤치마크(저자 실험 조건). [사실][^ref-677]
- Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning(2025) — 자연어로 활동을 지정하고 로봇에 질의해 실행 진행을 확인하는 구조. 실제 정밀 농업 시나리오에서 시험. [사실][^ref-857]
- Liu, Z., Bahety, A., & Song, S., REFLECT(CoRL 2023) — 계층적 경험 요약을 근거로 한 실패 설명과 교정 계획. RoboFail 데이터셋. [사실][^ref-453]
- Henkel, V. 외, Foundation-Model-Based Agents in Industrial Automation(2026) — 산업 자동화 일반(로봇 한정 아님) 기반 모델 에이전트 88편의 체계적 문헌 고찰. 그 문헌 집합에서 사용자 지원·모니터링 용도에 강하고 사람 상호작용(+37%)·불확실성 처리(+35%)에서 기존 산업 에이전트보다 나으나, 75.0%가 TRL 4~6이고 배포 지향 근거는 9.1%에 그친다. [사실][^ref-861]
- 한국전자통신연구원(ETRI) 이준기 외, 거대언어모델 기반 로봇 인공지능 기술 동향(전자통신동향분석 39(1), 2024-02) — 언어 모델의 상식·추론 능력으로 명령을 이해하고 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획과 제어 코드 생성을 자동화하는 흐름을 정리한 국내 동향 논문. 다중 로봇 조율이나 사람 승인 절차는 다루지 않고, 대규모 계산 자원·데이터·시뮬레이션·물리 테스트베드가 소수 기업에 집중된 점을 한계로 적었다. [사실][^ref-858]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-453]: Liu, Z., Bahety, A., & Song, S. (CoRL 2023), REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023-06-27, https://arxiv.org/abs/2306.15724, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-855]: Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S., HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models, 2025-05-01, https://arxiv.org/abs/2505.00820, 접근일 2026-09-29
[^ref-857]: Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning, 2025-09-19, https://arxiv.org/abs/2509.16006, 접근일 2026-09-29
[^ref-858]: 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)), 거대언어모델 기반 로봇 인공지능 기술 동향, 2024-02, https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html, 접근일 2026-09-29
[^ref-861]: Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y., Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges, 2026-05-04, https://arxiv.org/abs/2605.02592, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s7.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-110, ref-111, ref-125, ref-677, ref-753, ref-777, ref-859, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스

# 12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- ROSA는 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트이므로 분류 원문 19장의 "로봇 자체 지능·제어"에 해당하는 연계 대상이며, CoMuRoS의 로봇별 지역 언어 모델 코드 생성과 마찬가지로 ROP가 직접 맡는 기능이 아니라는 것이 구축자 추정이다. [추정][^ref-859][^ref-677][^ref-110] Open-RMF 관련 항목은 [표준·프레임워크 목록](../../standards/index.md)의 기존 항목이며, 이번 실행에서 새로 든 것은 VerifyLLM이다.
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Open-RMF 작업 요청 스키마(rmf_api_msgs task_request)와 작업 구성(task_new) | 오픈소스 | 승인된 계획을 관제 작업 요청으로 바꿀 때의 목표 형식. 범주·설명 필수, 시작 시각·우선순위·라벨·요청자·플릿 이름 선택, 취소·단계 건너뛰기 요청으로 추가 제어. [사실][^ref-125][^ref-110] | [ref-125](../../references/ref-125.md), [ref-110](../../references/ref-110.md) |
| Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) | 오픈소스 | 진행 상황 질의의 근거 기록. 12가지 상태 값, 활성 단계, 남은 추정 시간, 배정 로봇, 단계별 사건, 중단·취소 요청 기록. [사실][^ref-111] | [ref-111](../../references/ref-111.md) |
| Open-RMF MCP 서버와 Nayantra 에이전트(OSRA 상호운용 SIG 세션 공지) | 오픈소스 | Open-RMF REST API를 언어 모델 도구로 노출하고 영어 명령을 다단계 임무로 바꾼다고 공지에서 밝힘. 승인·상태 질의 언급 없음. [사실][^ref-862] | ref-862 (OSRA Interop SIG, 2026-06-25 게시) |
| RobotFleet | 오픈소스 | 이기종 로봇 플릿을 컨테이너 서비스로 배치하고 언어 모델로 중앙 집중식 다중 로봇 작업 계획·스케줄링을 하며, 공유 선언형 세계 상태와 실행·재계획용 양방향 통신을 갖춘 프레임워크. [사실][^ref-777] | ref-777 (Gupta 외, 2025) |
| VerifyLLM(코드 공개) | 오픈소스 | 자연어 지시→LTL 변환 뒤 행동 순서열의 논리 일관성·누락 단계를 실행 전에 찾는 검증 모듈. 가정 작업 데이터셋 평가(실제 현장 아님). [사실][^ref-753] | ref-753 (Grigorev 외, IROS 2025) |
| ROSA(Robot Operating System Agent) | 오픈소스 | ROS 1·ROS 2 로봇 시스템을 자연어로 점검·진단·조작하는 언어 모델 에이전트. 명령을 잘 정의된 도구로 ROS에 연결하고 매개변수 검증·제약 강제 안전 장치를 두며 JPL 화성 실험장·실험실·시뮬레이션의 세 로봇으로 시연. [사실][^ref-859] | ref-859 (Royce 외, NASA JPL, 2024) |

ROSA는 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트이므로 분류 원문 19장의 "로봇 자체 지능·제어"에 해당하는 연계 대상이며, CoMuRoS의 로봇별 지역 언어 모델 코드 생성과 마찬가지로 ROP가 직접 맡는 기능이 아니라는 것이 구축자 추정이다. [추정][^ref-859][^ref-677][^ref-110] Open-RMF 관련 항목은 [표준·프레임워크 목록](../../standards/index.md)의 기존 항목이며, 이번 실행에서 새로 든 것은 VerifyLLM이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-777]: Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J., RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning, 2025-10-12, https://arxiv.org/abs/2510.10379, 접근일 2026-09-29
[^ref-859]: Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025), Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent, 2024-10-09, https://arxiv.org/abs/2410.06472, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s10.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-059, ref-110, ref-111, ref-125, ref-165, ref-242, ref-677, ref-753, ref-847, ref-855, ref-857, ref-861, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결

# 12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) · [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 원문 주석대로 업무 지시가 대화로 부르는 짝 엔진이다. 언어 모델은 작업 그래프·능력 요구를 만들고 실제 배정·일정은 이 두 영역의 엔진이 계산한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) · [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 원문 주석대로 업무 지시가 대화로 부르는 짝 엔진이다. 언어 모델은 작업 그래프·능력 요구를 만들고 실제 배정·일정은 이 두 영역의 엔진이 계산한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 실행 전 승인, 자동 검증, 답에 근거 기록의 식별자·시각을 붙이는 근거 표시, 환각·출력 불안정 대응이 이 영역의 신뢰 기반이라는 것이 구축자 추정이다. [추정][^ref-165][^ref-753][^ref-861]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — CoMuRoS는 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획하고 필요하면 로봇이 사람 도움을 요청하게 한다고 보고했다. [사실][^ref-677] 이 재계획이 승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다는 것이 구축자 추정이다. [추정][^ref-677]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 진행 상황 질의의 근거가 되는 작업 상태·단계·사건 기록(Open-RMF task_state)을 이 영역이 조회한다는 것이 구축자 추정이다. [추정][^ref-111]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 승인된 계획이 관제 작업 요청(Open-RMF task_request, dispatch_task_request)으로 변환되는 지점이며, MCP 서버로 관제 API를 노출하는 구현이 이 연동을 통과한다는 것이 구축자 추정이다. [추정][^ref-110][^ref-125][^ref-862]
- [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) — Open-RMF 작업 요청에 없는 기한·반복·실패 처리 조건은 시나리오 모델에서 정해져 이 영역의 지시에 들어온다는 것이 구축자 추정이다. [추정][^ref-125]
- [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md) · [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 로봇–작업 적합도 행렬(FLEET)과 로봇별 능력 이해(HMCF)는 능력 표현이 있어야 성립한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-855]
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — 의존 관계 DAG(DART-LLM)와 소요 시간·선후 관계가 붙은 작업 그래프(FLEET)는 작업 모델의 한 형식이다. [사실][^ref-059][^ref-242]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) · [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 언어 모델 기반 분해·배정, 사전 계획 검증, 실패 설명은 L. AI·학습 기술에 속하는 연구 방법이며, 원문 교차 규칙에 따라 이 영역과 양쪽에 연결한다는 것이 구축자 추정이다. [추정][^ref-165][^ref-861][^ref-753]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 간호 인력의 자연어 지시를 작업 순서열로 바꾸는 병원 보조 로봇 사례(원문 미열람). [사실][^ref-847]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 실제 정밀 농업 시나리오에서 자연어 활동 지정과 질의로 진행을 확인한 사례. [사실][^ref-857]
- 이 영역은 [채팅 기반 구성·운영 트랙](../../tracks/chat-based-configuration-and-operation/index.md)의 중심 영역이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-29
[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-847]: Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer), Agile assistive hospital robot for suboptimal Task execution in dynamic environments, 2026, https://link.springer.com/article/10.1007/s10514-026-10255-6, 접근일 2026-09-29 (원문 미열람)
[^ref-855]: Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S., HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models, 2025-05-01, https://arxiv.org/abs/2505.00820, 접근일 2026-09-29
[^ref-857]: Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning, 2025-09-19, https://arxiv.org/abs/2509.16006, 접근일 2026-09-29
[^ref-861]: Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y., Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges, 2026-05-04, https://arxiv.org/abs/2605.02592, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s4.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 핵심 개념과 용어"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-059, ref-090, ref-111, ref-165, ref-242, ref-453, ref-753, ref-855, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#4
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 핵심 개념과 용어

# 12. 채팅으로 업무 지시·오케스트레이션 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **[작업 분해](../../glossary/task-decomposition.md)·[연합 형성](../../glossary/coalition-formation.md)·작업 배정(Task Decomposition, Coalition Formation, Task Allocation)** — SMART-LLM은 상위 작업 지시를 이 세 단계로 나누어 다중 로봇 작업 계획으로 바꾸고, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시킨다. [사실][^ref-090]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **[작업 분해](../../glossary/task-decomposition.md)·[연합 형성](../../glossary/coalition-formation.md)·작업 배정(Task Decomposition, Coalition Formation, Task Allocation)** — SMART-LLM은 상위 작업 지시를 이 세 단계로 나누어 다중 로봇 작업 계획으로 바꾸고, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시킨다. [사실][^ref-090]
- **의존 관계 그래프(Directed Acyclic Graph, DAG)** — DART-LLM은 자연어 지시를 의존 관계를 가진 하위 작업의 방향 비순환 그래프로 분해해 여러 로봇이 병렬로 실행하게 한다. [사실][^ref-059]
- **로봇–작업 적합도 행렬(Robot–Task Fitness Matrix)** — FLEET에서 언어 모델 전단이 만드는, 로봇마다 각 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 매긴 행렬로, 형식 최적화기가 배정 계산의 입력으로 쓴다. [사실][^ref-242]
- **사전 실행 계획 검증(Pre-execution Plan Verification)** — VerifyLLM처럼 자연어 지시를 [선형 시간 논리](../../glossary/linear-temporal-logic.md)(Linear Temporal Logic, LTL)로 옮긴 뒤 행동 순서열의 논리 일관성과 빠진 단계를 실행 전에 찾는 절차다. [사실][^ref-753]
- **감독 제어(Supervisory Control)·실행 전 승인** — 서베이가 정리한 Hunt 외의 방식처럼 사람이 실행 전에 계획을 승인하고, HMCF처럼 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 [사람 참여 루프](../../glossary/human-in-the-loop.md) 감독 형태다. [사실][^ref-165][^ref-855]
- **실패 설명(Failure Explanation)** — REFLECT처럼 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델이 실패 원인을 설명하고, 그 설명으로 계획기가 실패를 바로잡게 하는 기법이다. [사실][^ref-453]
- **작업 상태·단계·사건 기록** — [Open-RMF](../../glossary/open-rmf.md) 작업 상태 스키마는 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 의 상태 값과 활성 단계, 완료까지 남은 추정 시간, 배정 로봇, 단계별 시작·종료 시각·사건·건너뛰기 요청, 중단·취소 요청 기록을 담는다(발행일 미확인, 확인일 2026-09-29 기준). [사실][^ref-111]
- **[모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md) 도구 호출** — 관제 REST API를 언어 모델이 부를 수 있는 도구로 노출하는 방식으로, OSRA 상호운용 SIG 세션 공지가 Open-RMF 사례를 다룬다고 밝혔다. [사실][^ref-862]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-453]: Liu, Z., Bahety, A., & Song, S. (CoRL 2023), REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023-06-27, https://arxiv.org/abs/2306.15724, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-855]: Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S., HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models, 2025-05-01, https://arxiv.org/abs/2505.00820, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s3.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 왜 중요한가"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-110, ref-125, ref-165, ref-861, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 왜 중요한가

# 12. 채팅으로 업무 지시·오케스트레이션 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화로 받은 지시가 로봇 동작으로 이어지려면 지시를 계획으로 바꾸는 일, 그 계획을 사람이 확인·승인하는 일, 실행 뒤 진행을 설명하는 일이 한 흐름으로 이어져야 하며, 이 영역은 C. 채팅 기반 구성·운영 가운데 로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대화로 받은 지시가 로봇 동작으로 이어지려면 지시를 계획으로 바꾸는 일, 그 계획을 사람이 확인·승인하는 일, 실행 뒤 진행을 설명하는 일이 한 흐름으로 이어져야 하며, 이 영역은 C. 채팅 기반 구성·운영 가운데 로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]

연구 쪽 근거는 이 흐름의 사람 쪽이 아직 약하다는 점을 보여 준다. Li 외(2025)의 다중 로봇 언어 모델 서베이(2026-05-03 판 기준)는 실행 전에 사람이 계획을 승인하는 방식, 로봇이 막히면 도움을 요청하는 방식, 사람 검증으로 환각을 줄이는 방식을 예로 들면서도, 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머물고 로봇 수가 늘 때 운영자의 인지 부담이 정량화되지 않았다는 점을 빈틈으로 지적했다. [사실][^ref-165]

배포 근거도 드물다. Henkel 외(2026)의 산업 자동화 일반(로봇 한정 아님) 기반 모델 에이전트 문헌 고찰(88편)은 그 문헌 집합에서 보고된 시스템의 75.0%가 기술 성숙도(Technology Readiness Level, TRL) 4~6의 프로토타입·초기 검증 단계이고 배포 지향 근거는 9.1%에 그치며, 일반화 부족·환각과 출력 불안정·데이터 부족·추론 지연이 지속적 장애물이라고 보고했다. [사실][^ref-861]

반면 구현 쪽은 대화를 관제 API에 바로 잇는 방향으로 움직이고 있다. Open Source Robotics Alliance(OSRA) 상호운용 SIG의 2026-07-02 세션 공지(2026-06-25 게시)는 Open-RMF REST API를 언어 모델이 부를 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와 평이한 영어 명령을 여러 단계의 RMF 임무로 바꾸는 에이전트(Nayantra)를 다룬다고 밝혔으며, 공지 본문에는 실행 전 사람 확인·승인이나 작업 상태 질의에 관한 언급이 없다. [사실][^ref-862] 도구 호출로 관제 API를 직접 부르는 구현에는 승인 단계가 드러나지 않으므로, 분류 원문의 "대화 결과는 실행 명령이 아니라 계획"이라는 요구를 지키려면 ROP는 언어 모델의 작업 요청 초안과 실제 dispatch_task_request 발행 사이에 계획 미리보기·승인 관문을 두고 승인된 계획만 한 번 관제 작업 요청으로 변환해야 한다는 것이 구축자 추정이다. [추정][^ref-862][^ref-110][^ref-125]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-29
[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-861]: Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y., Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges, 2026-05-04, https://arxiv.org/abs/2605.02592, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-05/pages/topics/2026/2026-09-29-area12-s11.md

```markdown
---
title: "12. 채팅으로 업무 지시·오케스트레이션 — 열린 질문"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-165, ref-677, ref-858, ref-862]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 12. 채팅으로 업무 지시·오케스트레이션 — 열린 질문

# 12. 채팅으로 업무 지시·오케스트레이션 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? 서베이는 운영자 인지 부담이 정량화되지 않았다고 지적했다. [사실][^ref-165]
- 이 페이지는 [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? 서베이는 운영자 인지 부담이 정량화되지 않았다고 지적했다. [사실][^ref-165]
- **신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? CoMuRoS는 사건 기반 재계획을 보고했지만 재승인 기준은 초록에서 확인되지 않았다. [사실][^ref-677]
- **신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 언어 모델이 MCP 도구 호출로 관제 작업 API를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? OSRA 세션 공지에는 승인 언급이 없다. [사실][^ref-862]
- **신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가? 이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이며 그 논문은 다중 로봇 조율과 사람 승인을 다루지 않았다. [사실][^ref-858]

전체 목록은 [열린 질문](../../open-questions.md)에 있다. 트랙 전용 질문은 [채팅 기반 구성·운영 트랙 질문 백로그](../../tracks/chat-based-configuration-and-operation/question-backlog.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-858]: 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)), 거대언어모델 기반 로봇 인공지능 기술 동향, 2024-02, https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html, 접근일 2026-09-29
[^ref-862]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-05 | 12. 채팅으로 업무 지시·오케스트레이션 의 "열린 질문" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 848건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 219개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [12] 에 걸린 0건 / 전체 138건)

```markdown
없음
```

### runs/2026-09-29-05/verification2.json

```json
{
  "run_id": "2026-09-29-05",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "1차 처분은 [추정] 유지였으나 10절(분리 페이지 2026-09-29-area12-s10.md 3절) 37. 관제 화면·실행 기록 항목에서 '작업 상태·단계·사건 기록을 이 영역이 조회한다'를 [사실][^ref-111]로 써 태그를 올렸다. [추정]으로 되돌리고 구축자 추정임을 밝힌다. 6절(s6)에서는 [추정]으로 바르게 썼다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "1차 처분은 [추정] 유지였으나 10절 20. 로봇·제조사 관제 연동 항목에서 '승인된 계획이 관제 작업 요청으로 변환되는 지점이며 MCP 서버 구현이 이 연동을 통과한다'를 [사실][^ref-110][^ref-125][^ref-862]로 써 태그를 올렸다. 3절·6절에서는 [추정]으로 바르게 썼다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "1차 처분은 [추정] 유지였으나 10절 32. 예외 복구·재계획·업무 연속성 항목에서 '승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다'를 [사실][^ref-677]로 써 태그를 올렸다. CoMuRoS 의 사건 기반 재계획 자체는 f12 [사실]이지만 '차이 표시·재승인' 연결은 f26 의 구축자 추정이다. 9절에서는 [추정]으로 바르게 썼다."
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
      "f25(ref-847)는 이전 실행 2026-09-29-04 가 같은 URL 로 낸 병원 논문과 같은 주장이다 — 페이지는 ref-847 로 인용했으며 퍼블리셔가 같은 URL 의 기존 id 로 합친다(1차 판정과 같음)"
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
    "10절 37. 관제 화면·실행 기록 항목(자동 분리 뒤 docs/topics/2026/2026-09-29-area12-s10.md 3절에 실림): '진행 상황 질의의 근거가 되는 작업 상태·단계·사건 기록(Open-RMF task_state)을 이 영역이 조회한다. [사실][^ref-111]' 을 '…조회한다는 것이 구축자 추정이다. [추정][^ref-111]' 로 고친다 — 이 문장은 브리프 f16([추정])의 내용이며 태그를 올렸다. 수정은 세부영역 페이지 10절 원문에 하고 코드가 다시 분리하게 한다.",
    "10절 20. 로봇·제조사 관제 연동 항목: '승인된 계획이 관제 작업 요청(Open-RMF task_request, dispatch_task_request)으로 변환되는 지점이며, MCP 서버로 관제 API를 노출하는 구현이 이 연동을 통과한다. [사실][^ref-110][^ref-125][^ref-862]' 을 [추정] 으로 내리고 '…라는 것이 구축자 추정이다' 형식으로 쓴다 — 브리프 f20([추정])의 내용이며 태그를 올렸다. 각주 세 개는 유지한다.",
    "10절 32. 예외 복구·재계획·업무 연속성 항목: '실패·의도 변경이 촉발하는 사건 기반 재계획과 사람 도움 요청(CoMuRoS)은 승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다. [사실][^ref-677]' 을 두 문장으로 나눈다 — CoMuRoS 가 실패·의도 변경 시 사건 기반 재계획과 사람 도움 요청을 보고했다는 부분만 [사실][^ref-677] 로 두고, '승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다' 는 '…라는 것이 구축자 추정이다. [추정][^ref-677]' 로 쓴다 — 연결 부분은 브리프 f26([추정])의 내용이다.",
    "10절 9. 채팅으로 시나리오 구성 항목: 'Open-RMF 작업 요청에 없는 기한·반복·실패 처리 조건은 시나리오 모델에서 정해져 이 영역의 지시에 들어온다. [사실][^ref-125]' 을 '…들어온다는 것이 구축자 추정이다. [추정][^ref-125]' 로 고친다 — 작업 요청 스키마에 그 필드가 없다는 점(f18)은 사실이지만 시나리오 모델이 그것을 정해 준다는 연결은 브리프에 finding 이 없는 구축자 추정이다.",
    "10절 10. 채팅으로 로봇 구성 · 5. 로봇 능력·작업 표현 항목: '로봇–작업 적합도 행렬(FLEET)과 로봇별 능력 이해(HMCF)는 능력 표현이 있어야 성립한다. [사실][^ref-242][^ref-855]' 을 '…성립한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-855]' 로 고친다 — 두 논문이 능력 표현을 전제한다는 해석은 초록에 없는 구축자 추정이다.",
    "8절 FLEET 항목(자동 분리 뒤 docs/topics/2026/2026-09-29-area12-s8.md 3절에 실림): '…2단계 혼합 방식. 이 영역과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 역할 분담 근거. [사실][^ref-242]' 에서 '이 영역과 25. …·26. … 의 역할 분담 근거' 구절을 [사실] 문장에서 빼고, 남기려면 '…역할 분담 근거로 삼는다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]' 로 따로 쓴다 — 역할 분담은 브리프 f7([추정])의 내용이다.",
    "3절 첫 문장(세부영역 페이지 본문과 자동 분리 페이지 docs/topics/2026/2026-09-29-area12-s3.md 1절·3절에 같은 문장): '…이 영역은 C. 채팅 기반 구성·운영 가운데 로봇 동작과 가장 가까운 자리에 있다. [의견]' 에 누구의 의견인지 밝혀 '…자리에 있다는 것이 구축자 의견이다. [의견]' 로 고친다 — 사양서 5.3·1차 항목 5 는 [의견] 에 의견 주체를 밝히도록 한다.",
    "11절 두 번째 열린 질문(자동 분리 뒤 docs/topics/2026/2026-09-29-area12-s11.md 3절에 실림)의 보조 문장 'CoMuRoS는 사건 기반 재계획을 보고했지만 재승인 기준은 다루지 않았다. [사실][^ref-677]' 을 '…보고했지만 재승인 기준은 초록에서 확인되지 않았다. [사실][^ref-677]' 로 고친다 — 브리프 f12 는 초록 범위만 확인했고 논문 전체가 재승인 기준을 다루지 않는다는 진술은 브리프에 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 28건(그중 f25 는 원문 미열람으로 검색 결과 일치만 확인), 미확인 0건, 교차 확인 3건(f6, f10, f15). 강등: 없음. 원문 미열람 출처: ref-847(Springer 인증 리다이렉트). 주의: [사실] 가운데 f6·f10·f15 를 뺀 나머지는 단일 출처(논문 초록·HTML 본문·오픈소스 스키마)라 페이지 신뢰도는 medium 이다. f10 의 Hunt 외와 HMCF 는 같은 연구 그룹이므로 '세 그룹' 이 아니라 '두 그룹 이상' 이다. ref-862 는 세션 공지(2026-06-25 게시)이며 세션 진행 내용은 확인되지 않았다. f25 의 '국립대만대학병원' 은 검색 결과 요약에 없어 삭제 지시했다. f8 의 site_type '가정' 은 데이터셋 기준이라 적용 사례로 인정하지 않았다. 셋(대화→계획, 승인, 진행 설명)을 하나의 승인 관문 흐름으로 이은 운영 사례는 이번 브리프에서 확인되지 않았고 결론(f7·f11·f16·f20·f26)은 구축자 추정이다. 검증 검색 1회·열람 17회 사용. 정정 요청 없음. 미사용 출처 없음. / 2차 수정 후 재검증. 1차 수정 지시 10건은 모두 이행됐다(ref-862 발행일·문구, f25 병원 이름·저자·원문 미열람 표시, f10 그룹 수, f8 가정 사례 제외, 5절 병원·실외 두 사례와 미확인 항목, f12·f21 연계 대상 표시, f23 문헌 고찰 범위, [추정] 구축자 추정 표시, 저자 실험 조건 병기, ref-165 열람 판). 드리프트 8건 처리: 10절 연결 항목 다섯 곳(37·20·32·9·10·5번 영역)이 브리프에서 [추정]인 f16·f20·f26 과 finding 이 없는 연결 해석을 [사실]로 써 태그를 올렸고, 8절 FLEET 항목이 f7 의 역할 분담 추정을 [사실] 문장에 넣었으며, 3절 [의견] 문장에 의견 주체가 없고, 11절 보조 문장이 초록 범위를 넘는 부재 진술을 담았다. 모두 국소 수정이라 수정 후 재검증으로 돌려보낸다. [분류원문] 보존(admonition 세 줄·1절·2절이 시드와 글자 단위로 같음), 섹션 순서 준수(세부영역 13절, 주제 10절), 링크는 docs_tree.txt 가 없어 부록 A 경로·용어집 색인·이번 실행 생성 페이지로만 대조했고 모두 유효하며 docs/about/scope-boundary.md·docs/references/ref-110·111·125.md·docs/topics/index.md·트랙 질문 백로그는 존재를 확인하지 못했다. 자동 분리 페이지 6건은 원 절 내용을 그대로 옮긴 것으로 확인했으나, 분리 뒤 각 페이지에서 MCP·OSRA·LTL·DAG·ROS 약어의 첫 등장 풀어쓰기가 사라졌고, 세부영역 페이지 프런트매터 sources(18건)가 남은 본문의 각주 정의(11건)보다 많으며, 분리 페이지 9. 검증 노트가 정본 형식('1차 조건부 승인 / 2차 대기', 건수·신뢰도)이 아니다 — 세 가지는 코드 분리(pipeline/validate_run.py)의 산출물이므로 수정 지시 대상으로 두지 않고 pipeline 담당에게 전달한다. 신뢰도 medium 유지.",
  "retry_reason": null
}
```
