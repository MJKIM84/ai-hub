(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-02
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 25. 작업 배정 — MRTA (G. 계획·최적화)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 16건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-10-02/target.json

```json
{
  "run_id": "2026-10-10-02",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 162,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 25,
    "area_name": "25. 작업 배정 — MRTA",
    "category": "G. 계획·최적화",
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
  "selection_rationale": "CLI 지정 run_type=update, area=25"
}
```

### runs/2026-10-10-02/research.json

```json
{
  "run_id": "2026-10-10-02",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 25,
    "area_name": "25. 작업 배정 — MRTA",
    "category": "G. 계획·최적화"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오뿐이고, 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인'(oq-054)이 남아 있음. 운영 중 도착하는 작업과 용량·마감을 함께 다룬 다른 현장 유형 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 문헌 검토(ref-152)의 계열 구분·실험 플릿 규모가 '미확인'으로 남아 있고, LTAA(ref-168) 비교 결과가 출처 충돌(oq-030)로 11절에 미뤄져 있음. rmf_task TaskPlanner 최적 배정의 적용 범위(한 플릿)가 명시되지 않음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — Open-RMF 입찰(BidProposal)이 담는 필드가 구체적으로 적혀 있지 않고, 2026-09-26 rmf_fleet_adapter 2.14.0 의 플릿 이름 필터 수정이 반영되지 않음(바뀐 출처)",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 2024~2026 연구(마감 제약 SMT 배정, 혼잡 환경 재분배 배정 MRTA-RM, 최소 비용 흐름 기반 대규모 배정) 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 두 수준 배정에서 제조사 관제가 내야 할 비용·상태 정보(oq-053)가 미확인으로 남아 있음",
    "섹션 11. 열린 질문(주제 페이지로 분리) — oq-030·oq-053·oq-054 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]",
    "oq-030 LTAA(arXiv 2512.02810) 원문은 LLM 배정과 동적 계획법·강화학습의 성공률을 어떤 조건에서 비교했고, 초록의 '전통 기법을 모두 앞섰다'는 표현은 본문 수치와 맞는가? (섹션 6·11 겨냥)",
    "oq-053 ROP 가 플릿 단위로 배정하고 제조사 관제가 플릿 안에서 로봇을 고르는 두 수준 배정에서 제조사 관제는 어떤 비용·상태 정보를 내며, 한 플릿 안의 최적 배정은 어디까지 보장되는가? (섹션 6·7·9·11 겨냥)",
    "oq-054 출하 마감·납기 같은 상위 업무 제약을 배정과 결합하는 공개 설계가 있는가? (섹션 5·6·11 겨냥)",
    "이동로봇 플릿 작업 배정 문헌 검토(2025-01)는 방법을 어떤 계열로 나누고 실험 플릿 규모를 어떻게 보고하는가? (섹션 6 겨냥)",
    "배정 비용에 환경 구조·혼잡을 반영해 대규모로 배정하는 최근(2024~2026) 연구와 공개 구현은 무엇이며, 그 결과는 어떤 조건의 실험인가? (섹션 6·8 겨냥)",
    "바뀐 출처: Open-RMF rmf_fleet_adapter 의 입찰 동작은 최근 판에서 어떻게 바뀌었는가? (섹션 7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Meseguer Valenzuela·Blanes Noguera 의 2025 년 문헌 검토는 이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법을 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-152"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF §II Algorithms 의 소절 A. Heuristics, B. Meta-heuristics, C. Exact and matheuristic Methods, D. Market-based Approach (MBA), E. Artificial Intelligence (AI). 기존 6절 문장의 '계열 구분 미확인'을 채운다",
      "as_of": "2025-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "같은 문헌 검토의 표 I~V 는 계열별로 각 연구의 방법, 중앙·분산 구조, 구현 환경(프레임워크), 플릿 규모, 주요 결과를 함께 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-152"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§III Simulations 표 I~V 의 열: Method / Centralized / Decentralized / Framework / Fleet Size / Remarkable results. 총 검토 편수는 선정·제외 절차가 원문에 없어 새 수치로 내지 않음",
      "as_of": "2025-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "문헌 검토의 본문 설명과 표의 플릿 규모 값이 서로 달라, 검토된 연구의 최대 플릿 규모나 계열 간 우열을 하나의 수치로 요약하지 않는 편이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-152"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "§III 본문: 휴리스틱 연구의 시뮬레이션은 'up to 25 robots'(예외 Shi 외 2024 는 이동 랙 1,923개로 로봇 수가 아님). 그러나 표 I 의 L. Li 외 행은 최대 45 AMR, 표 IV(시장 기반)의 Teck 외 2023 행은 3~48 AMR 을 적는다. 표 I 페이지 렌더 확인",
      "as_of": "2025-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "LTAA 원문(Kaitha·Yu, 2025-12 프리프린트)의 그림 15 비교는 TEACh 데이터셋의 건설 작업에서 전체 성공률을 LTAA 75.97%, Q-learning 73%, DQN 77% 로 보고하며, 초록은 LTAA 값을 76% 로 반올림해 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-168"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "pp.57–58 그림 15 'Task Allocation Methods Comparison' 본문: \"overall success rate of 75.97%, positioning it between Q-learning (73%) and DQN (77%)\". 초록: 76% task completion rate. 논문의 실험·모델 보고값이며 건설 현장 실측 완료율이 아님",
      "as_of": "2025-12-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "같은 원문 p.61 은 결정적 비교군의 성공률을 brute force 0.77, greedy 0.81, 동적 계획법(Dynamic Programming, DP) 0.95 로 적고, 이 결정적 알고리즘들은 불확실성 모델이 없어 비교 그림에서 제외했으며 확률적 조건의 직접 비교 기준은 강화학습이라고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-168"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p.61(이미지 렌더 확인): 'Brute force, greedy, and DP obtained success rates of 0.77, 0.81, and 0.95. However, they are omitted from the comparison plots because these deterministic algorithms lack uncertainty modeling.' oq-030 관련",
      "as_of": "2025-12-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "LTAA 원문 초록은 로봇 전문화가 뚜렷한 Heavy Excels 설정에서 LTAA 가 77% 완료율과 더 나은 작업 부하 균형으로 전통 기법을 모두 앞섰다고 쓰고, 결론(p.62)은 이 설정의 성공률을 77.1% 로 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-168"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'In the Heavy Excels configuration ... reaches 77% completion with superior workload balance, exceeding all traditional methods.' p.62 결론: Heavy Excels setting (77.1% success with balanced workloads). 초록의 포괄적 우위 표현과 p.61 의 DP 제외 설명이 함께 있음",
      "as_of": "2025-12-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "f4~f6 을 함께 보면 원문에는 LTAA 전체 75.97%, Heavy Excels 77.1%, DP 95% 가 모두 있으나 DP 는 불확실성 모델 차이로 비교에서 빠졌으므로, 'LTAA 가 전통 배정법 전체보다 우수하다'는 결론은 지지되지 않으며 같은 조건의 LLM 대 DP 우열은 확정할 수 없고, Heavy Excels 결과와 전체 비교 결과는 분리해 적어야 한다(oq-030 부분 해소).",
      "tag": "의견",
      "source_ids": [
        "ref-168"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f5·f6 에서 도출. 기존 oq-030 의 두 요약은 각각 초록(Heavy Excels 우위)과 본문 p.61(DP 0.95)을 전한 것으로 보임. 결정적·확률적 비교군을 같은 조건으로 재평가한 자료는 원문에 없음",
      "as_of": "2025-12-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Open-RMF 의 입찰 제안 메시지 BidProposal.msg 는 입찰 공고(BidNotice)에 답해 플릿 어댑터가 내는 것으로, 플릿 이름(fleet_name), 작업을 수행할 것으로 예상되는 로봇 이름(expected_robot_name), 새 작업 수용 전·후의 전체 배정 비용(prev_cost·new_cost), 새 작업의 예상 완료 시각(finish_time) 다섯 필드를 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1453"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_task_msgs/msg/BidProposal.msg 전체 필드 5개: string fleet_name, string expected_robot_name, float64 prev_cost, float64 new_cost, builtin_interfaces/Time finish_time. 검증 시 BidResponse.msg 안에 담겨 쓰이는 것을 확인 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "BidProposal 의 필드(f8)는 두 수준 배정에서 제조사 관제(플릿)가 공개하는 비용·상태 정보의 구체적인 예이지만, 이 메시지는 각 플릿이 자기 안에서 계산한 비용만 전하므로 이것만으로 모든 플릿을 합친 최적 배정이 보장되지는 않으며, 이종 플릿의 최적성 손실을 수치로 제한하는 근거는 확인하지 못했다(oq-053 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1453",
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8 의 prev_cost·new_cost 는 '플릿의 전체 배정 비용'이고 rmf_task README 는 계획기 대상을 한 플릿으로 둠(f10). BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF rmf_task README 는 작업 계획기(TaskPlanner)의 최적 배정을 물리·운동 특성을 공유하는 한 플릿에 속한 로봇과 주어진 작업 집합에 대해, 요청된 시작 시각을 고려해 작업이 가장 짧은 시간에 끝나도록 순서를 정하는 문제로 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-404"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"For a given collection of tasks and robots belonging to a fleet (ie, they share physical and kinematic traits), the planner determines the best ordering of tasks across robots\". 배터리 제약과 충전 작업 삽입도 포함 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "TaskPlanner 의 '최적 배정'(f10)은 한 플릿의 주어진 작업 집합에 한정되므로, 앞으로 들어올 작업, 다른 제조사 관제의 내부 결정, 실제 혼잡까지 포함한 운영 전체의 전역 최적성으로 넓혀 해석해서는 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-404",
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10 과 Zhang 외 AAMAS 2026 §5 에서 도출: 선형 배정은 '최적 단발(one-shot) 배정'을 주지만 단위 이동 비용과 혼잡(traffic) 비용이 다르고(§5, §5.3), 장기 처리량은 §7.2 에서 따로 평가. 서로 다른 연구팀 자료를 대조한 범위 한정",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Tuck 외(2024, NFM 2024 게재 예정 프리프린트)는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 풀이를 써서, 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 표현하고 점진(incremental) 풀이로 새 작업을 배정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§1: 작업은 온라인 생성·엄격한 마감·로봇 1대 필요, 로봇 동시 작업 수 제한. §3.2 과업 튜플(출발·도착 위치 id, 도착 시각, 마감), 용량 K_n. Definition 6: 하차가 마감 전이어야 완료. §4.3 점진 풀이. arXiv comment: NFM 2024 게재 예정",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Tuck 외 방법의 목표는 주어진 모델에서 제약을 모두 만족하는 계획을 찾는 것이고 최소 이동 비용의 전역 최적해를 찾는 것과는 구별되며, 저자들은 알고리즘이 건전·완전하다고 증명하지만 이는 논문의 모델·인코딩 조건 안의 결과이고 국소 경로 계획·충돌 회피는 하위 계획기에 맡긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§1: 'even satisfying solutions without guaranteed optimality are relevant for this application', 국소 운동 계획·충돌 회피는 downstream planners 몫. §5 건전성(Thm 5.1)·완전성(D=D_max 가정, 사용 솔버의 건전·완전 가정)",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "납기·마감 준수가 필수인 작업은 높은 우선순위 점수만 주는 방식과 별도로, 마감을 필수 제약으로 두는 정식화(f12)를 검토할 필요가 있으나, 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못했다(oq-054 부분 근거).",
      "tag": "의견",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f12·f13 에서 도출. 원문은 마감을 Definition 6 의 완료 조건으로 강제하고 2절에서 휴리스틱 방법이 엄격한 마감의 완전성 보장을 못 한다고 지적. 병원 모사 환경 연구이며 창고 출하 마감 사례는 아님",
      "as_of": "2024-03-18",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "Tuck 외는 병원과 유사한 공간을 그래프(노드=구역, 가중치=최악 이동 시간)로 추상화한 다중 로봇 배송 벤치마크 200개(작업 10~30개, 로봇 5~20대, 최대 용량 2 또는 3, 마감 균등 분포)에서 용량 제한 로봇의 동적 작업 배정을 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'benchmarks encoding multi-robot delivery created from a graph abstraction of a hospital-like environment'. §1 그래프 추상화, §6 실험: 200 benchmarks, tasks 10–30, agents 5–20, capacity c=2·3. 병원 모사 계산 실험",
      "as_of": "2024-03-18",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "Tuck 외의 병원 모사 배송 문제에서 각 요청은 출발·도착 위치와 발생·마감 시각을 가지며, 새 요청이 들어오면 이미 실행한 동작과 현재 동작은 유지한 채 계획을 갱신한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.2 과업 m=(id, 시작 위치, 종료 위치, 도착 시각 t_m, 마감 T_m). Definition 9 갱신 계획: 'past actions and the current action are unchanged', 계획 갱신은 시스템 위치에서만",
      "as_of": "2024-03-18",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f17",
      "claim": "Tuck 외 연구는 병원 배송의 계산 실험 사례이며 병원 현장 실증으로 분류해서는 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15·f16 에서 도출. 원문은 그래프 추상화 벤치마크의 솔버 성능(풀이 수·시간)을 보고하고 실제 병원·로봇 운행 결과는 없음",
      "as_of": "2024-03-18",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f18",
      "claim": "Lee·Sim·Nam 의 MRTA-RM 은 장애물이 밀집하고 통로가 좁은 환경에서 일반화 보로노이 다이어그램(GVD)으로 로드맵을 만들고 이를 여러 구역으로 나눈 뒤 구역 사이에 로봇을 재분배하고 작업을 배정해, 충돌·교착을 줄이면서 전체 완료 시간(makespan)을 줄이려 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'considers the paths of the robots to avoid collisions and deadlocks ... constructs a roadmap using a Generalized Voronoi Diagram ... partitions the roadmap into several components'. 충돌 없는 경로를 직접 찾지 않고 충돌 가능성이 낮은 배정을 찾음",
      "as_of": "2025-06-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "MRTA-RM 저자들은 수백 대 규모 로봇의 동적 시뮬레이션 결과(무작위 시나리오 성공률 96% 초과, 분리 시나리오 58~100%)를 보고하고 Python 구현을 공개했으며, 결론에서 성공률 100% 달성(경로 추종 제어기)과 이종 로봇 팀 확장을 후속 과제로 남겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1455",
        "ref-1456"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문 실험 절: 'high success rates exceeding 96% in the random scenario', 'separated scenario ... 58 to 100%'. §6 Conclusion: 'we will achieve 100% of the success rate by implementing a controller', 이종 로봇 확장 계획. README: Python 3.9+, MIT, RAS 2025-12 표기. 논문과 코드는 같은 팀 산출물",
      "as_of": "2025-06-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "MRTA-RM 은 혼잡을 줄이는 배정의 재현 후보로 볼 수 있지만, 임의 환경에서 교착이 없다는 보장으로 소개해서는 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "본문: 'our method cannot achieve deadlock-free as our research aims to find a task allocation that is likely to prevent deadlocks'. 분리 시나리오 성공률 58% 사례 존재(f19)",
      "as_of": "2025-06-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Zhang 외의 AAMAS 2026 연구는 온라인 다중 에이전트 픽업·배송의 작업 배정을 환경 그래프 위의 최소 비용 흐름(Minimum-Cost Flow) 문제로 풀어, 선형 배정 방식이 요구하는 로봇·작업 사이 모든 쌍의 거리 행렬 계산을 피한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2 문제 정의, §5 흐름 정식화(격자 각 칸을 노드로, 더미 source·sink), §5.3.2 Network Flow: 명시적 에이전트–작업 쌍 거리 계산 회피. 초록: 'eliminates the need for pairwise distance' 행렬. DOI 10.65109/MQIK8423",
      "as_of": "2026-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "Zhang 외는 격자 지도 벤치마크(창고형 Sortation Large 포함)에서 1초 계획 예산으로 최대 20,000 에이전트와 30,000 작업까지 다뤘다고 보고하며, 이는 실제 로봇 배치가 아니라 계산 실험이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'scales to 20,000 agents and 30,000 tasks within 1-second planning' 시간. §7(§7.1 실행 시간, §7.2 처리량)·표 1: Sortation Large 20,000 에이전트 행. 단일 시점 배정 최적성과 장기 처리량은 §7.2 에서 따로 평가",
      "as_of": "2026-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Zhang 외의 흐름 정식화는 기본 간선 비용으로 단위 비용을 쓰고, 선택할 수 있는 대체 비용 모델로 경로 계획기의 혼잡 추정치나 실행 중 평균 대기 시간을 배정 비용에 반영할 수 있으며, 계획기와의 결합은 6절에서 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5: 기본은 지도 간선 비용(격자는 unit cost), 대체로 Traffic(계획기 혼잡 추정)·Avg Waiting Time 비용 모델. §6: 계획기의 FCost 로 간선 비용 설정(Algorithm 2). 표 1 열 Flow-Unit Cost / Flow-Traffic / Flow-Avg Waiting",
      "as_of": "2026-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "MRTA-RM(f18)과 Zhang 외(f21~f23)를 함께 보면 배정 비용에 환경 구조와 혼잡을 반영하는 연구 흐름은 확인되지만, 두 방법은 환경·규모·지표가 달라 성능 수치를 같은 조건의 순위로 비교할 수 없는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1455",
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "MRTA-RM: 연속 공간 GVD 로드맵·동적 시뮬레이션 성공률·makespan. Zhang 외: 격자 MAPD 벤치마크·처리량·1초 예산. 공통 벤치마크 비교 없음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 작업 요청에 지정된 플릿 이름이 문자열 또는 배열에 포함되기만 하면 입찰하도록 한 수정(#534)을 기록한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_ros2 2.14.0 태그 rmf_fleet_adapter/CHANGELOG.rst '2.14.0 (2026-09-26)': 'Submit bid as long as fleet name exists (in string or array) (#534)'. FleetUpdateHandle.cpp 의 fleet_name 문자열·배열 검사 코드와 일치",
      "as_of": "2026-09-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "요청에 후보 플릿을 제한하는 배정 사례를 적을 때는 #534 수정이 포함된 rmf_fleet_adapter 패키지 버전(2.14.0 이상)을 함께 적는 편이 좋으며, 이 변경이 모든 배포판에 자동 반영되었다는 뜻은 아니다.",
      "tag": "의견",
      "source_ids": [
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f25 에서 도출. 변경 이력은 패키지 태그 기준이며 ROS 배포판별 반영 시점은 확인하지 않음",
      "as_of": "2026-09-26",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-152",
      "org": "Meseguer Valenzuela, A., & Blanes Noguera, F.",
      "title": "Task Allocation in Mobile Robot Fleets: A review",
      "published": "2025-01",
      "url": "https://arxiv.org/abs/2501.08726",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "이동로봇 플릿 작업 배정 방법을 휴리스틱·메타휴리스틱·정확·수리 휴리스틱·시장 기반·인공지능 기반의 다섯 계열로 나누고 표 I~V 로 각 연구의 구조·구현 환경·플릿 규모·결과를 정리한 리뷰 프리프린트(arXiv 2025-01-15). 이번에 PDF 원문을 열어 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2501.08726",
      "source_unopened": false
    },
    {
      "id": "ref-168",
      "org": "Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810)",
      "title": "Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms",
      "published": "2025-12-02",
      "url": "https://arxiv.org/abs/2512.02810",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "LangGraph 기반 LLM 작업 배정 에이전트(LTAA)를 건설 작업(TEACh)에서 DP·Q-learning·DQN 과 비교한 프리프린트. 이번에 v1 PDF 원문을 열어 그림 15·p.61·결론을 확인했다. 기존 ref-168 의 저자 표기 'Yu, S.' 정정: Hongrui Yu(저자: Shyam prasad reddy Kaitha, Hongrui Yu). 발행일은 arXiv 2025-12-02(PDF 하단의 2025-12-01 표기와 다름).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2512.02810v1",
      "source_unopened": false
    },
    {
      "id": "ref-404",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_task — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_task",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "로봇 간 최적 작업 배정·순서를 푸는 TaskPlanner API 와 배터리 제약에 따른 충전 작업 자동 삽입을 설명한 README. 이번에 계획기 대상이 한 플릿의 로봇·작업 집합임을 원문으로 다시 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_task/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1453",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "플릿 어댑터가 입찰 공고(BidNotice)에 답해 내는 입찰 제안 메시지 정의. 플릿 이름·예상 수행 로봇·수용 전후 전체 배정 비용·예상 완료 시각 다섯 필드를 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_task_msgs/msg/BidProposal.msg",
      "source_unopened": false
    },
    {
      "id": "ref-1454",
      "org": "Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정)",
      "title": "SMT-Based Dynamic Multi-Robot Task Allocation",
      "published": "2024-03-18",
      "url": "https://arxiv.org/html/2403.11737v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "온라인으로 도착하는 마감 있는 픽업·배송 작업을 용량 제한 로봇에 배정하는 문제를 SMT 로 인코딩하고 건전성·완전성을 증명한 뒤 병원 모사 그래프 벤치마크로 평가한 논문(arXiv comment: NFM 2024 게재 예정).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1455",
      "org": "Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293)",
      "title": "Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution",
      "published": "2025-06-08",
      "url": "https://arxiv.org/html/2506.07293",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "GVD 로드맵을 구역으로 나누고 구역 사이 로봇 재분배 후 작업을 배정해 밀집 환경의 충돌·교착을 줄이는 대규모 배정 방법(MRTA-RM)과 수백 대 동적 시뮬레이션 결과. arXiv 초판 2025-06-08, 저자 README 는 RAS 2025-12 게재를 표기.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1456",
      "org": "Lee, S. 외 (SeBin-Lee-SG GitHub)",
      "title": "MRTA-RM_public — README",
      "published": null,
      "url": "https://github.com/SeBin-Lee-SG/MRTA-RM_public",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "MRTA-RM 저자 공개 구현의 README. 로드맵·구역 단위 배정 구조와 Python 실행 안내, RAS 2025-12 게재 표기를 담는다. 논문과 같은 팀 산출물이다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/SeBin-Lee-SG/MRTA-RM_public/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1457",
      "org": "Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS)",
      "title": "Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery",
      "published": "2026-05",
      "url": "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "온라인 MAPD 의 작업 배정을 환경 그래프 위 최소 비용 흐름으로 풀어 모든 쌍 거리 행렬을 피하고, 선택적으로 계획기 혼잡 비용을 반영해 최대 20,000 에이전트·30,000 작업을 1초 예산으로 다룬 AAMAS 2026(2026-05-25~29, Paphos) 논문. DOI 10.65109/MQIK8423.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1458",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지의 판별 변경 이력. 2.14.0(2026-09-26)에 요청의 플릿 이름이 문자열 또는 배열에 있으면 입찰하도록 한 수정 #534 가 기록되어 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 병원 모사 환경의 동적 배정 계산 실험 사례 추가(f15 수행 자원·f16 시작 조건·f17 현장 실증 아님 표시), 물류창고 표 제약 행의 '출하 마감 결합 미확인'에 마감 필수 제약 정식화 근거 보충(f12·f14) / 섹션 6(주제 페이지 2026-09-25-area13-s6 반영) — 문헌 검토 문장의 '미확인'을 계열 구분·표 구성으로 교체(f1·f2)하고 최대 규모를 한 수치로 요약하지 않음(f3), LTAA 문장을 원문 수치로 교체(f4·f5·f6·f7: 전체 75.97%·Heavy Excels 77.1%·결정적 비교군 brute force 0.77·greedy 0.81·DP 0.95 의 비교 제외), TaskPlanner 최적 배정의 범위 한정(f10·f11), SMT 기반 마감·용량 배정(f12·f13) / 섹션 7(주제 페이지 s7 반영) — BidProposal 다섯 필드(f8), 메시지만으로 전 플릿 최적이 보장되지 않음(f9), rmf_fleet_adapter 2.14.0 #534(f25·f26) / 섹션 8(주제 페이지 s8 반영) — Tuck 외 2024(f12·f13), MRTA-RM(f18·f19·f20), Zhang 외 AAMAS 2026(f21·f22·f23), 두 연구 비교 한계(f24) / 섹션 9 — 두 수준 배정에서 제조사 관제가 내는 정보의 예와 한계(f8·f9·f10·f11) / 섹션 11(주제 페이지 s11 반영) — oq-030 부분 해소(f4~f7, 출처 충돌의 원인: 초록과 본문 p.61 의 서로 다른 비교 조건), oq-053 부분 근거(f8·f9·f11), oq-054 부분 근거(f12·f14), 새 질문 4건. 참고문헌 ref-168 저자 표기 정정(Yu, S. → Yu, H.; Hongrui Yu)과 ref-152·ref-168 원문 열람 반영. 기존 내용 확인: Open-RMF 입찰이 비용을 담는다는 문장(s7, ref-376)과 TaskPlanner 의 배정·충전 삽입 문장(s6, ref-404)은 이미 있으므로 중복하지 않고 세부(필드·범위)만 더한다. 다음 실행 후보: 20. 로봇·제조사 관제 연동(f8·f9·f25), 27. 다중 로봇 경로·교통 관리 — MAPF(f18·f21~f24), 47. AI·학습·적응과 모델 운영(f4~f7)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "최소 비용 흐름",
      "term_en": "Minimum-Cost Flow",
      "definition": "간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다."
    },
    {
      "term_ko": "이론 모듈로 만족 가능성",
      "term_en": "Satisfiability Modulo Theories (SMT)",
      "definition": "산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다."
    }
  ],
  "open_questions_new": [
    "서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반",
    "플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반",
    "LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 47. AI·학습·적응과 모델 운영 | 근거: f5 | 종류: 일반",
    "최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가? | 관련 영역: 25. 작업 배정 — MRTA, 28. 공용 자원·충전·에너지 최적화 | 근거: f21 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 9,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-02/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "f1~f3: 문헌 검토의 총 검토 편수는 선정·제외 절차가 원문에 없어 확인하지 못함",
      "f4~f7: LTAA 결정적·확률적 비교군을 같은 조건으로 비교한 결과는 원문에 없음(oq-030 은 부분 해소에 그침). 초록의 '전통 기법 모두 우위' 표현과 p.61 의 DP 제외 설명의 불일치는 저자 설명이 없음",
      "f8·f9: BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님. 이종 플릿 두 수준 배정의 최적성 손실을 수치로 제한하는 근거는 찾지 못함(oq-053 미해결)",
      "f12: NFM 2024 게재 예정 표기는 arXiv comment 기준이며 게재본(쪽·DOI)은 확인하지 않음",
      "f14: 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못함(oq-054 미해결)",
      "f19: MRTA-RM 논문과 공개 구현은 같은 팀 산출물이라 독립 재현 근거가 아님. RAS 게재본은 README 표기로만 확인",
      "f25·f26: #534 수정이 ROS 배포판별 바이너리에 언제 반영되었는지는 확인하지 않음",
      "모든 사실 finding 은 단일 출처라 교차 확인 0건"
    ],
    "scope_violations": [
      "f13: 국소 경로 계획·충돌 회피는 로봇 자체 지능·제어(연계 대상) 몫이며, 원문도 하위 계획기에 맡긴다고 밝혀 배정 범위만 다룸",
      "f18~f24: 경로 충돌·교착·혼잡 비용은 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 배정 비용에 반영하는 부분만 이 영역에 쓰고 경로 계획 자체는 27 에 연결",
      "f4~f7: LLM 기반 배정은 교차 규칙상 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것으로 양쪽에 연결",
      "f15~f17: 병원 모사 환경의 계산 실험이므로 site_type 병원은 '모사 환경'으로 명시하고 현장 실증으로 쓰지 않음"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 6
    },
    "limits": "외부 조사 변환이라 검색 횟수 집계 없음(queries 0 은 미집계 표시). 신규 출처 6건(ref-1453~ref-1458, 예약 구간 ref-1453~ref-1482 안), 재사용 3건(ref-152 리뷰 논문·ref-168 LTAA·ref-404 rmf_task README, 모두 이번에 원문 열람). 원문 열람 9/9. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·6·7·8·9·11절)과 바뀐 출처(rmf_fleet_adapter 2.14.0)만 다뤘다. 검증 수정 반영: Zhang 외 절 번호(§2 문제 정의, §5 흐름 정식화·§5.3.2 거리 행렬 회피, §6 계획기 결합, §7·§7.2·표 1 실험)와 혼잡 비용을 '선택할 수 있는 대체 비용 모델'로 범위 한정(f21~f23), LTAA p.61 의 brute force 0.77·greedy 0.81·DP 0.95 병기와 초록 76% 반올림·arXiv 2025-12-02·저자 Hongrui Yu 정정(f4~f6, ref-168), 리뷰 본문 25대·표 I 45 AMR·표 IV 48 AMR 을 의견 근거에 병기(f3), Tuck 외 NFM 2024 게재 예정(f12, ref-1454), BidProposal 필드 5개와 같은 프로젝트 자료라 독립 확인 아님(f8·f9), #534 확인(f25). 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-030 근거 f4~f7, oq-053 근거 f8·f9·f11, oq-054 근거 f12·f14. 교차 확인 0건이라 사실 finding 신뢰도는 medium 이하. 현장 유형 사례 finding 은 병원 모사 환경(f15~f17)뿐이고 물류창고 실측 비교(2절 질문)는 이번에도 찾지 못함. 국내 자료 없음. L. AI·학습 기술 관련 f4~f7 은 47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안한다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md

```markdown
---
title: "25. 작업 배정 — MRTA"
type: area
category: "G. 계획·최적화"
area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [MRTA, 작업 배정, 시장 기반 배정, 최근접 배정, Open-RMF, LLM 기반 배정]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-006, ref-031, ref-059, ref-089, ref-090, ref-101, ref-105, ref-132, ref-152, ref-166, ref-167, ref-168, ref-181, ref-236, ref-237, ref-242, ref-393, ref-394, ref-395, ref-396, ref-397, ref-398, ref-399, ref-400, ref-376, ref-401, ref-402, ref-403, ref-404]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 25. 작업 배정 — MRTA

# 25. 작업 배정 — MRTA

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

[로봇 이동형 풀필먼트 시스템(RMFS)](../../glossary/robotic-mobile-fulfillment-system.md)의 이산 사건 시뮬레이션에서 피킹 주문을 작업대에 배정하는 규칙은 단위 처리량을 크게 바꾸었다고 보고됐다. [사실][^ref-398] 배정은 개별 로봇의 문제가 아니라 창고 전체 처리량의 문제가 될 수 있다. [추정][^ref-398]

2절의 질문처럼 가장 가까운 로봇에 맡기는 최근접 배정은 단순해서 다중 에이전트 픽업·배송 알고리즘과 국내 자동물류센터 시뮬레이션에서 기본 규칙으로 쓰였다. [사실][^ref-006][^ref-402] 그러나 작업장(shop floor) 사례 연구에서 앞으로의 운반 요청을 고려한 조합 최적화 배차가 무작위·최근접 규칙보다 작업 대기 시간을 더 잘 통제했다고 저자가 보고했다(2019). [사실][^ref-400]

두 결과를 함께 보면 최근접 배정이 전체 최적이라는 보장은 없다. 다만 근거는 작업장 사례 연구(지표: 작업 대기 시간)와 시뮬레이션뿐이며, 창고 현장에서 둘을 직접 비교한 실측 자료는 이번 조사에서 찾지 못했다. [추정][^ref-006][^ref-400][^ref-402][^ref-398]

## 4. 핵심 개념과 용어

**MRTA 분류 체계(Gerkey–Matarić taxonomy)** — [다중 로봇 작업 배정(MRTA)](../../glossary/mrta.md)을 단일 작업 로봇(ST)/다중 작업 로봇(MT), 단일 로봇 작업(SR)/다중 로봇 작업(MR), 즉시 배정(IA)/시간 확장 배정(TA)의 세 축으로 나누는 도메인 독립 분류다(2004). [사실][^ref-393]
- **최적 배정 문제(Optimal Assignment Problem)** — ST-SR-IA 유형은 이 문제의 한 사례로, 헝가리안 방법(Hungarian Method) 같은 다항 시간 해법으로 최적해를 구할 수 있다. [사실][^ref-393]

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 핵심 개념과 용어](../../topics/2026/2026-09-25-area13-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹한 토트의 운반 작업을 여러 제조사 로봇 가운데 누구에게 맡길지 정하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템(WMS 등)이 피킹 주문을 내려 운반 작업이 생긴다. 주문·납기·재고 정책 자체는 ROP 밖의 연계 대상이다. [추정][^ref-031] |
| 작업 대상 | 피킹한 상품을 담은 토트(설명용 가정) |
| 수행 자원 | 작업자가 피킹하고 AMR(Autonomous Mobile Robot, 자율이동로봇)이 운반하는 협업 설정이 연구되어 있다. [사실][^ref-132] ROP 는 플릿별 입찰을 비교해 작업을 줄 플릿을 고르는 역할을 맡을 수 있다. [추정][^ref-376][^ref-031] |
| 제약 | 배터리가 설정 임계값(Open-RMF 템플릿 예시값 0.10) 아래인 로봇은 작업하지 않도록 해 배정 후보에서 빠진다. [사실][^ref-105] 출하 마감을 배정 목적함수에 넣는 방법은 미확인이다. |
| 완료·인계 | 해당 없음 |
| 예외·성과 | RMFS 이산 사건 시뮬레이션에서 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398] 최근접 배정이 전체 최적이라는 보장은 없다. [추정][^ref-400] |

다음은 설명을 위한 가상의 시나리오이다. 두 제조사의 AMR 플릿이 같은 피킹 구역을 쓰고, 작업자가 피킹한 토트를 다음 공정으로 옮길 운반 작업이 계속 들어온다. 이 영역이 관여하는 칸은 수행 자원(누구에게 맡길지), 제약(배터리·능력으로 후보 거르기), 예외·성과(배정 규칙이 처리량에 주는 영향)다.

Open-RMF 방식이라면 디스패처가 각 플릿 어댑터에 입찰 공고를 보내고, 처리할 수 있는 플릿이 비용을 담아 입찰하면 가장 빨리 끝나는 것 같은 설정 기준으로 비교해 작업을 준다. [사실][^ref-376] 가장 가까운 로봇을 고르는 규칙은 계산이 가볍지만 뒤이어 들어올 요청을 고려하지 않으므로 전체 이동이나 대기가 늘 수 있다. [추정][^ref-400]

## 6. 대표 접근법과 기술

이동로봇 플릿 작업 배정 연구를 알고리즘 계열별로 정리한 문헌 검토가 있으나(2025-01), 검토 편수·계열 구분·실험 플릿 규모에 관한 수치는 이 위키에서 확인하지 못했다(미확인). [추정][^ref-152] 주제 페이지에 여섯 갈래(중앙 최적화, 시장 기반 경매·분산 합의, 최근접 규칙, 학습 기반 배차, LLM 기반 배정, 배터리·충전 결합)로 정리했다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 접근법과 기술](../../topics/2026/2026-09-25-area13-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준과 오픈소스는 배정을 어느 구성요소의 책임으로 두는지 보여 주며, Open-RMF 는 입찰 기반 배정을 구현하고 VDA 5050 은 배정을 관제의 기능으로만 규정한다. [사실][^ref-376][^ref-031]

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area13-s7.md)에 있다.

## 8. 대표 연구와 자료

분류 체계와 시장 기반 방법의 고전 연구, 창고 결정 규칙의 시뮬레이션 연구, 국내 자료를 이 영역의 대표 자료로 골랐다(이 위키의 선정).

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료](../../topics/2026/2026-09-25-area13-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이종 제조사를 잇는 ROP 는 어느 플릿·로봇에 작업을 줄지의 배정 결정과 기준을 맡고, 플릿 내부 경로·주행은 제조사 관제나 로봇에 맡기는 분담이 가능할 것으로 보인다. [추정][^ref-376][^ref-031]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 주문·납기·재고 제약을 배정의 입력으로 받아 쓰고 결과를 되돌린다. [추정][^ref-031] | 수요예측·전사 재고정책(연계 대상) |
| 로봇 자체 지능·제어 | 플릿·로봇 사이 배정 결정과 기준(비용·완료 시각). [추정][^ref-376][^ref-031] | 플릿 내부 경로·주행, 로컬 회피(제조사 관제·로봇) |

VDA 5050 은 주문 배정을 관제의 기능으로 두지만 배정 알고리즘 자체는 규정하지 않는다. [사실][^ref-031] 두 수준으로 나눈 배정이 전체 최적성을 얼마나 잃는지는 확인하지 못해 11절에 질문으로 둔다.

연계 대상: VDA 5050 은 관제–이동로봇 통신과 무관한 외부 IT 시스템 인터페이스를 범위에서 제외하므로, 배정 입력이 되는 주문·납기·재고 제약은 WMS 등 상위 업무 시스템에서 오고 그 정책은 ROP 밖에 있다. [추정][^ref-031] 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

배정은 로봇 능력 정보를 입력으로 받고 순서·경로·충전 결정과 맞물린다. 교차 규칙(분류 개정 전 원문 8장)에 따라 학습·LLM 기반 배차는 47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결한다.

- [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md) — 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026). [사실][^ref-236][^ref-237]
- [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) — Open-RMF 플릿 어댑터 입찰과 VDA 5050 관제 기능이 배정의 인터페이스가 된다. [사실][^ref-376][^ref-031]
- [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) — 작업 간 의존(ID·XD)과 rmf_task 의 배정·순서 동시 결정이 두 영역을 잇는다. [사실][^ref-394][^ref-404]
- [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) — MAPD 토큰 패싱은 작업 선택과 충돌 없는 경로 계획을 함께 다룬다. [사실][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 배터리 임계값·충전 작업 삽입·충전기 조율이 배정 후보와 일정에 들어간다. [사실][^ref-105][^ref-404][^ref-403]
- [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md) — RMFS·자동물류센터 시뮬레이션은 배정 규칙을 가정한 미래에서 실험하는 도구다. [사실][^ref-398][^ref-402]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 학습 기반 배차(ScheduleNet)와 LLM 기반 배정은 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것이다. [사실][^ref-399][^ref-090][^ref-168]
- [23. 업무 시스템 연동](../integration/business-system-integration.md) — 배정 입력인 주문·납기 제약이 상위 업무 시스템에서 온다. [추정][^ref-031]

## 11. 열린 질문

이 위키의 열린 질문 현황이다. LLM 배정 결과의 출처 충돌과 선언·관측 능력 차이가 아직 풀리지 않았고, 창고 비교 실측·두 수준 배정·납기 결합에 관한 질문을 새로 올렸다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 열린 질문](../../topics/2026/2026-09-25-area13-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [25. 작업 배정 — MRTA](task-allocation-mrta.md) — 섹션 3~11 신규 작성(분류 체계·배정 방식·Open-RMF 입찰·LLM 기반 배정·열린 질문), 트랙 반영 제안 반영, 페이지 상태 마커 추가. 2차 수정: 6·8·10·11절 첫 문장의 표기·태그 정리 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 대표 접근법과 기술](../../topics/2026/2026-09-25-area13-s6.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 내부 용어 '브리프' 삭제, 원 페이지 3절 참조를 링크로 명시 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 대표 연구와 자료](../../topics/2026/2026-09-25-area13-s8.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: '대표 자료' 선정 문장을 이 위키의 선정으로 밝힌 안내 문장으로 고침 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 열린 질문](../../topics/2026/2026-09-25-area13-s11.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 안내 문장의 태그·각주 제거, oq-024 항목의 단정을 [추정] 문장으로 고침 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area13-s7.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 대상 아님, 변경 없음) (실행 2026-09-25-33)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-152]: Meseguer Valenzuela, A., & Blanes Noguera, F., Task Allocation in Mobile Robot Fleets: A review, 2025-01, https://arxiv.org/abs/2501.08726, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-393]: Gerkey, B. P., & Matarić, M. J., A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems, 2004-09, https://journals.sagepub.com/doi/10.1177/0278364904045564, 접근일 2026-09-25 (원문 미열람)
[^ref-394]: Korsah, G. A., Stentz, A., & Dias, M. B., A comprehensive taxonomy for multi-robot task allocation, 2013, https://journals.sagepub.com/doi/10.1177/0278364913496484, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems (arXiv 2018-01 공개, Operations Research Perspectives 2019 게재, 이산 사건 시뮬레이션 조건), 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-400]: International Journal of Planning and Scheduling 게재 논문(저자 미확인), Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors, 2019, https://www.inderscience.com/info/inarticle.php?artid=103016, 접근일 2026-09-25 (원문 미열람)
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-09-25
```

### data/area_reflection_proposals.json (대상 영역 25. 작업 배정 — MRTA 에 대한 트랙 반영 제안 16건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-37",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 25,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "Open-RMF 작업 요청 스키마(필수 category·description, 선택 가장 이른 시작 시각·우선순위, 기한 필드 없음)와 배송 작업 기술(픽업·하역 사건의 장소·적재물 sku·수량), VDA 5050 3.0.0 팩트시트 적재 명세·지원 동작이 배정 입력이 되는 구조(단계 2 실행 2026-09-25-37, f1·f2·f6). 채팅 지시만으로는 기한·우선순위·화물 제약이 비기 쉬워 업무 시스템과 팩트시트에서 보완해야 한다는 추론(f15·f18, [추정])을 SCM 질문과 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-51",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 25,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "Open-RMF 작업 상태 스키마는 배정 결과를 assigned_to(그룹·이름)로, 배정 과정을 queued·selected·dispatched·failed_to_assign·canceled_in_flight 의 dispatch 상태로 표현한다(f2). VDA 5050 3.0.0 은 주문 배정을 관제 최소 기능으로 두되 주문 단위는 로봇 한 대의 노드–간선 그래프 구간이다(f4). 표준 형식의 배정 결과는 누가 맡았는지만 남겨, 최근접 배정과 다른 기준의 전체 효과를 비교하려면 ROP 가 배정 근거·목적함수 값을 따로 기록해야 할 것으로 보인다(f19, 추정, oq-052 연결).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-62",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 25,
      "section": "8. 대표 연구와 자료",
      "summary": "LLM 다중 로봇 계획·배정 평가 데이터셋(SMART-LLM 네 범주 상위 지시와 가용 로봇·최종 상태, MAT-THOR 정답 PDDL·목표 조건)과 지표(목표 조건 재현율 GCR, 정답 전이 수 대비 로봇 활용도 RU, 논문 기준 저자 보고)를 추가하고, 이 벤치마크들이 배정의 전체 최적성(이동거리·납기)을 정답으로 두지 않는 것으로 보인다는 점(추정)을 분류 원문 질문·oq-052 와 연결한다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-65",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "능력별 통행 가능 경로를 먼저 구해 배정 후보를 거르거나 이종 차량 경로·배정 문제에 넣는 접근(연계 대상 사례 CHORAL, 점검 임무 대상·환경 조건 미확인, f19)과 ‘3층 출하 대기장’ 배정 후보를 로봇별 통행 가능 부분 그래프로 거르는 방식(추정, f24).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-66",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "TaskPlanner 의 탐욕(최적성 미보장)·A*(최적성 보장) 선택과 기본 비용 계산기 BinaryPriorityCostCalculator(f2), LLM 정식화+선형·정수계획·MILP·makespan 최소화 해법 배정 분담(f21), 분류 원문 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 목적함수 기반 해법의 비교 가능성([추정] f25, 30.5% 조건 병기).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-71",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "트랙 자연어 업무 지시 챗봇 단계 3(실행 2026-09-25-71): 온톨로지 기반 실행 가능성 판정 결과를 배정기에 묶이지 않는 ReasonerOutput 으로 넘기는 방법(Electronics 2026, ref-236, 원문 미열람), Open-RMF 입찰 비교가 배정 단계에 놓이는 위치(ref-376), LiP-LLM 처럼 LLM 이 분해하고 선형계획이 배정하는 분담(ref-166), 지시 해석–능력 판정–결정적 배정 흐름과 분류 원문 SCM 질문의 연결은 목적 기준에 달렸다는 판단([추정]). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-74",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "Open-RMF 디스패처는 무입찰 시 FailedToAssign·오류(코드 10)를 기록하고 작업을 수행하지 않는다(f1). 여러 입찰은 평가기로 고르며 기본값은 디스패처 코드(QuickestFinishEvaluator 지정)와 Auctioneer.hpp 문서(미지정 시 LeastFleetDiffCostEvaluator)를 병기, 순위 기준 미확인(f4). 작업 요청 fleet_name 으로 허용 플릿 지정(f5). 실행 불가 작업의 일시 배제 학습(f13, 운반 능력은 연계 대상). 후보 여럿일 때 계산 가능한 목적 기준은 평가기로 자동 결정하고 사용자만 아는 정보에 걸릴 때만 되묻는 경계와 분류 원문 질문과의 연결(f23·f24, 추정). 27. AI·학습·적응과 모델 운영과 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-77",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "긴급 지시·우선순위 변경 때 처음 가장 가까웠던 로봇이 이미 묶여 있을 수 있어 남은 요청 전체를 다시 배정해야 전체 목적을 따를 수 있으나(추정), Open-RMF RobotUpdateHandle 의 재배정은 현재 구현 기준 같은 플릿 안으로 한정되고(사실, ref-537) rmf_task plan() 이 현재 로봇 상태와 요청 집합으로 배정을 새로 생성한다(사실, ref-377). oq-053 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-79",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 이 만든 배정 결과를 실행 전에 불변·전제·사후 조건으로 검사하는 연구(SafePlan, 저자 보고·원문 미열람)와, 디스패처의 무입찰 FailedToAssign·로봇의 수행 불가 동작 거절(로봇 쪽은 연계 대상)을 마지막 거절 장치로 소개하고, 확인 화면이 배정 기준을 보여 주고 전체 기준 일관성은 결정적 배정기가 지키는 분담([추정])을 분류 원문 질문과 연결한다. 27. AI·학습·적응과 모델 운영과 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-98",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "배정 결과를 실행 가능 배정 비율과 해법기 기준값 대비 최적성 간격으로 나눠 평가하는 방식(ConstraintBench 시설 입지 85.0%·0%·9.41%, 저자 보고), 창고 배정의 총 이동 지연(TTD) 지표와 탐욕 픽업 거리 기준선(RTAW, 저자 보고), 분류 원문 질문을 최근접 기준선·해법기 기준값과 비교하는 설계(추정, oq-052 연결). RTAW 의 강화학습 배차는 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결로만 적는다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-99",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "가상 현장에서 같은 지시 흐름과 같은 교란을 최근접 배정 기준선과 ROP 배정(해법기 기반)에 똑같이 재생해 총 이동 지연·납기 지연을 비교하는 설계(추정). 공개 데모에 창고 레이아웃이 없어 자체 구축 필요, 창고 실측 비교 부재는 oq-052. 27. AI·학습·적응과 모델 운영과 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-81",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "배정 결과의 실행 전 검사: 온톨로지 기반 실행 가능성 판정(ref-236), 불변·전제·사후 조건 추론기(SafePlan, ref-702), 정수계획 배정과 LLM 의 자연어 기반 제약 갱신(건설 사례, ref-758), 배치 전 모의 실행·제약 검사로 최근접 배정의 대기·충돌 영향을 드러낼 가능성([추정], 물류 실측 없음, oq-052). 27. AI·학습·적응과 모델 운영과 양쪽 연결. 근거 f7·f8·f18·f21·f25(실행 2026-09-25-81).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-83",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "사용자 권한이 지시할 수 있는 플릿·구역을 제한하면 가장 가까운 로봇이 후보에서 빠질 수 있으므로, 권한은 Open-RMF fleet_name 처럼 배정 전 후보를 거르는 제약으로 넘기고 후보 가운데 선택 기준은 디스패처가 지키는 분담이 선택지로 보인다([추정], f25). fleet_name 이 수행 가능 플릿을 지정하고 requester 는 인증 필드가 없는 선택 문자열이라는 점은 [사실](f4, ref-125). 권한 제약의 최적성 손실을 잰 자료는 없다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 함께 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-85",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "트랙 자연어 업무 지시 챗봇 q4-04(f19·f21, 추정): 해석 되묻기·사람 승인·실행 보류 동안에는 배정을 확정하지 않고, 해소 뒤 그 시점 로봇 상태로 배정을 계산하는 분담을 둔다. 실행 보류는 VDA 5050 베이스를 풀어 주기 전에 걸어야 한다. 분류 원문 질문(가장 가까운 로봇)과의 연결도 적는다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에서 잇는다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-86",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 25,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 직접 배정 대 해법기 배정 비교 근거(LiP-LLM 선형계획 배정의 배정 실패 거의 없음, 시뮬레이션 과제·저자 보고; RobotFleet 은 LLM·MILP 배정기를 두나 같은 저자 자료이고 비교 결과 미확인)와 반례(CoMuRoS 정답률 최대 0.91, 실험실 텍스트 벤치마크; LTAA 는 2차 요약 충돌 oq-030), LLM 설계 규칙이 롤링 MILP 를 앞선 보고(제조·AGV 시뮬레이션 조건, 저자 보고, 롤링 MILP 는 AGV 운송 하위 문제의 추상화, 물류 창고 적용 미확인), 최근접 배정 기준선을 둔 판정 실험 설계(추정). 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결",
      "status": "제안"
    },
    {
      "run_id": "2026-10-09-25",
      "date": "2026-10-09",
      "track": "chat-based-configuration-and-operation",
      "stage": 2,
      "area_no": 25,
      "section": "8. 대표 연구와 자료",
      "summary": "핵심 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 관련해 Choe 외(arXiv 2505.13376): 창고 동기 지게차 6대 격자 시뮬레이션 100회에서 MILP 로 후보 도우미마다 경로·시간 비용을 계산하고 요청 로봇이 최저 비용 제안을 고른 시스템 전체 영향 기준 선택이 최근접 로봇 선택 대비 약 26% 효율 향상, 최근접 선택이 최적과 일치한 비율 42%(저자 보고, 시뮬레이션·프리프린트 조건, 동료심사 게재처 미확인, f5). 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 연결.",
      "status": "제안"
    }
  ]
}
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 순서·스케줄링**: 작업 묶음, 선후관계, 시간 제약, 작업 간 동기화, 긴급 작업 삽입을 다룬다
- **계속 들어오는 작업의 재계획**: 새 작업과 지연이 계속 생기는 조건에서 계획을 이어서 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 14번 영역 ‘작업 순서·스케줄링’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 [옛 분류원문]

> 옛 질문: 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [옛 분류원문]

## 2. 핵심 질문

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (요약)

```markdown
# 28. 공용 자원·충전·에너지 최적화

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
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

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md (요약)

```markdown
# 34. 시뮬레이션·예측용 디지털 트윈

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시뮬레이션 엔진**: 로봇·설비·물품·사람을 물리·센서 수준에서 가상으로 재현한다(MuJoCo·Gazebo·Isaac Sim 등)
- **운영 정책·수요 변화 예측**: 배치·운영 정책·일의 양이 바뀔 때의 효과를 가상 환경에서 미리 본다
- **시뮬레이션 관측 모델**: 잡음·지연이 있는 관측을 만들어 시뮬레이션 시험이 현실의 불확실성을 반영하게 한다
- **시뮬레이션 자산 관리**: 로봇·물품·환경의 3D 모델과 물성 값을 출처·라이선스와 함께 관리해 시뮬레이션에 쓴다

이전 분류(2026-09-24)에서 이 페이지는 옛 22번 영역 ‘시뮬레이션·예측용 디지털 트윈’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [옛 분류원문]

> 옛 질문: 성수기 주문량이 늘면 어디가 먼저 막힐까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 29건 / 전체 1399건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | https://arxiv.org/abs/1705.10868 | 2026-09-24 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | https://arxiv.org/abs/2411.09022 | 2026-09-25 | 아니오 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | https://github.com/SMARTlab-Purdue/SMART-LLM | 2026-09-25 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | https://arxiv.org/abs/2309.10062 | 2026-09-25 | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | https://github.com/merschformann/RAWSim-O | 2026-09-25 | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 2026-09-25 | 예 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 2026-09-25 | 아니오 |
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | https://arxiv.org/abs/2501.08726 | 2026-09-25 | 아니오 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | https://arxiv.org/abs/2410.21040 | 2026-09-25 | 아니오 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 2025-03 | https://arxiv.org/abs/2503.13813 | 2026-09-25 | 아니오 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | https://arxiv.org/abs/2512.02810 | 2026-09-25 | 아니오 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | https://arxiv.org/abs/2510.22784 | 2026-09-25 | 아니오 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | https://doi.org/10.3390/electronics15163562 | 2026-09-25 | 아니오 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 2026-09-25 | 아니오 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10 | https://arxiv.org/abs/2510.07417 | 2026-09-25 | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task.html | 2026-09-25 | 예 |
| ref-393 | Gerkey, B. P., & Matarić, M. J. | A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems | 2004-09 | https://journals.sagepub.com/doi/10.1177/0278364904045564 | 2026-09-25 | 아니오 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 2026-09-25 | 아니오 |
| ref-395 | Choi, H.-L., Brunet, L., & How, J. P. | Consensus-Based Decentralized Auctions for Robust Task Allocation | 2009 | https://dl.acm.org/doi/10.1109/tro.2009.2022423 | 2026-09-25 | 아니오 |
| ref-396 | Dias, M. B., Zlot, R., Kalra, N., & Stentz, A. | Market-Based Multirobot Coordination: A Survey and Analysis | 2006-07 | https://www.ri.cmu.edu/pub_files/2006/7/01677943-1.pdf | 2026-09-25 | 아니오 |
| ref-397 | Aziz, H., Chan, H., Cseh, Á., Li, B., Ramezani, F., & Wang, C. | Multi-Robot Task Allocation—Complexity and Approximation | 2021-05 | https://arxiv.org/abs/2103.12370 | 2026-09-25 | 아니오 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 2026-09-25 | 아니오 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 2026-09-25 | 아니오 |
| ref-400 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 2019 | https://www.inderscience.com/info/inarticle.php?artid=103016 | 2026-09-25 | 아니오 |
| ref-401 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 미확인 | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 | 2026-09-25 | 아니오 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 2026-09-25 | 아니오 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | https://arxiv.org/abs/2603.22731 | 2026-09-25 | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | https://github.com/open-rmf/rmf_task | 2026-09-25 | 예 |
```

### docs/glossary/index.md (요약: 용어 396개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [25] 에 걸린 13건 / 전체 348건)

```markdown
- oq-024 [열림] 제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가? (영역 5, 18, 25)
- oq-030 [열림] 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? (영역 25, 47)
- oq-049 [열림] 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (영역 20, 25, 26)
- oq-052 [열림] 국내외 물류센터에서 최근접 배정 규칙과 전역 최적화(또는 LLM 기반) 배정을 같은 조건에서 비교해 총 이동거리·처리량·납기 준수를 실측한 자료가 있는가? (영역 25, 39)
- oq-053 [열림] ROP 가 플릿 단위로 작업을 입찰·배정하고 제조사 관제가 플릿 안에서 다시 로봇을 고르는 두 수준 배정에서 전체 최적성이 얼마나 손실되며, 이를 줄이려면 제조사 관제가 어떤 비용·상태 정보를 내야 하는가? (관련 기존 질문: oq-031) (영역 20, 25)
- oq-054 [열림] 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? (관련 기존 질문: oq-019) (영역 23, 25, 26)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 25, 38, 51)
- oq-083 [열림] 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? (영역 25, 42)
- oq-114 [열림] 로봇 관제가 배정 실패(수행 가능한 로봇·플릿 없음)를 WMS 등 상위 업무 시스템에 어떤 필드로 되돌리고, 상위 시스템이 이를 사람 작업 지시로 전환하는 표준이나 국내 물류센터 사례가 있는가? (영역 23, 25)
- oq-118 [열림] 국내 물류센터 로봇 관제에서 작업 지시나 배정 결과를 배치 전에 시뮬레이션(디지털 트윈)으로 모의 실행해 확인하는 운영 사례나 연구가 있는가? (영역 25, 34)
- oq-153 [열림] 국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? (영역 6, 25)
- oq-165 [열림] 반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가? (영역 61, 25)
- oq-286 [열림] 로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가? (영역 60, 31, 25)
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

### runs/2026-10-10-01/research.md

```markdown
# 리서치 브리프 2026-10-10-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-01 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 24. 작업·워크플로 모델링 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 첫 문단이 drop 완료·IngestorResult SUCCESS 를 CBV arriving 수준이라고 [추정]으로 묶어, 각 규격 정의(CBV 세 단계, VDA 5050 표 5, IngestorResult 기본 필드)의 원문 위치와 범위가 드러나지 않음
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오 2건뿐이고 다른 현장 유형(농업·지상 로봇 협업 등)의 공개 작업 모델링 사례가 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — BPMN 메시지 대기 근거가 벤더 문서(Camunda, ref-113)와 미열람 소개 페이지(ref-112)뿐이고, 취소 후 정리·보상, rmf_task_sequence 의 단계·이벤트 구성이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 3.0.0 의 blockingType(SINGLE 추가)과 rmf_fleet_adapter 의 최근 변경(2026-09-26)이 반영되지 않음
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — Filippone 외(ref-116)가 원문 미열람 상태로 2026-03 초판 표기만 있고 연구 방법·게재처가 없음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-001·oq-014 에 근거가 붙지 않았음

## 조사 질문

1. 현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
2. 로봇의 하역 완료 신호(VDA 5050 drop FINISHED, IngestorResult SUCCESS)와 GS1 CBV 업무 단계(arriving·accepting·receiving)는 원문 정의상 어떻게 다른가? (섹션 3 겨냥)
3. 인수 확인 대기·상관·시간 초과를 BPMN 규범 원문은 어떤 요소로 정의하며, 취소 후 정리와 보상은 어떻게 다루는가? (섹션 6 겨냥)
4. Open-RMF rmf_task_sequence 는 작업을 어떤 단계·이벤트로 구성하며, 최근 변경(단계 건너뛰기)은 무엇인가? (섹션 6·7 겨냥)
5. VDA 5050 3.0.0 은 동작의 병행 가능성(blockingType)에서 무엇이 바뀌었는가? (섹션 7 겨냥)
6. oq-001 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? (섹션 11 겨냥)
7. oq-014 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (섹션 5·8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | GS1 핵심 업무 어휘(CBV) 2.0 온톨로지는 arriving 을 물체가 위치에 도착하는 활동, accepting 을 점유 또는 소유가 바뀌는 활동, receiving 을 위치에서 수령되어 수령자 재고에 편입되는 활동으로 구분하고, receiving 의 사용은 arriving·accepting 의 사용과 상호 배타적이라고 적는다. | ref-044 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 미리 정의된 drop 동작의 FINISHED 상태를 하역이 끝나 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. | ref-031 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f3 | [사실] | Open-RMF IngestorResult 메시지의 기본 정의 필드(time·request_guid·source_guid·status, status 는 ACKNOWLEDGED·SUCCESS·FAILED)에는 수령자 재고 편입 여부를 나타내는 필드가 없다. | ref-049 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f4 | [의견] | 로봇의 하역 완료(drop FINISHED, IngestorResult SUCCESS)를 특정 CBV 업무 단계와 자동으로 동일시하지 말고, 해당 업무의 인수·재고 확정 조건을 별도 완료 조건으로 모델링하는 편이 타당하다. | ref-044, ref-031, ref-049 | 아니오 | medium | 2026-10-10 | 완료·인계 | — |
| f5 | [사실] | BPMN 2.0.2 규범 문서는 외부 참여자의 메시지가 도착하면 완료되는 수신 작업(Receive Task), 메시지를 프로세스 인스턴스에 연결하는 상관 키(CorrelationKey), 지연·시간 조건을 표현하는 타이머 이벤트(Timer Event)를 정의한다. | ref-502 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [추정] | 운반 뒤 인수 확인 메시지를 기다리고 시간 초과 시 분기하는 구조는 BPMN 규범 요소(수신 작업·상관 키·타이머 이벤트)로 표현할 수 있어 특정 벤더 엔진에 한정되지 않지만, 로봇 작업 식별자나 화물 식별자를 어떤 상관 키로 쓸지는 구현에서 정해야 하는 것으로 보인다. | ref-502, ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [사실] | FaMe 연구팀(University of Camerino PROS Lab)은 공식 페이지에서 지상 로봇 협업(ground vehicle cooperation)과 농업(agriculture scenario) 두 시나리오의 시뮬레이션 패키지와 엔진 패키지 빌드·실행 절차(colcon build, ros2 launch)를 공개한다. | ref-1423 | 아니오 | medium | 2026-10-10 | 기타 | — |
| f8 | [사실] | FaMe 모델링 지침은 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타내고, 병렬 동작은 AND 게이트웨이, 내부 선택은 XOR 게이트웨이, 시간 대기는 타이머 이벤트, 실행 오류는 오류 이벤트로 표현하게 한다. | ref-1423 | 아니오 | medium | 2026-10-10 | 기타 / 수행 자원 | — |
| f9 | [의견] | FaMe 예제는 창고 밖(농업·지상 로봇 협업)의 작업 모델링 사례로 5절에 추가할 수 있지만, 시뮬레이션 실험이므로 국내 상용 운영 실적이나 현장 성능 근거로 분류하지 않는 편이 좋다. | ref-1423 | 아니오 | low | 2026-10-10 | 기타 | — |
| f10 | [사실] | Open-RMF rmf_task 의 Task::Active::cancel() 주석은 취소 뒤에도 작업이 로봇을 짐 없는 상태로 되돌리기 위한 단계를 계속 수행할 수 있고(대기 단계가 그런 단계로 바뀔 수 있음), 완료 콜백이 호출되어야 취소가 끝난다고 설명한다. | ref-366 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f11 | [사실] | BPMN 2.0.2 는 이미 성공적으로 완료한 단계의 효과를 되돌리는 보상(Compensation)을 별도 개념으로 정의한다. | ref-502 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f12 | [의견] | 워크플로에는 취소 요청과 취소 후 정리 완료를 서로 다른 상태로 나누고, 실제 물건의 이동을 되돌릴 수 있는지에 따라 보상 단계를 따로 정의하는 편이 좋다. | ref-502, ref-366 | 아니오 | medium | 2026-10-10 | 예외·성과 | — |
| f13 | [사실] | Open-RMF rmf_task_sequence::Task 는 작업 완료를 위해 순서대로 실행할 단계(Phase)의 연쇄이고, 각 단계는 이벤트(Event)들로 구성되며, 모델은 rmf_task_sequence 에, 실제 로봇 명령 구현은 rmf_fleet_adapter 에 둔다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f14 | [사실] | rmf_task README 는 rmf_task_sequence 가 기본 제공하는 이벤트로 Bundle, DropOff, GoToPlace, PerformAction, PickUp, Placeholder, WaitFor 일곱 가지를 열거한다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f15 | [추정] | 기본 이벤트 목록과 단계 연쇄 구조만으로는 rmf_task_sequence 를 임의의 업무 병렬 분기·합류를 실행하는 범용 BPMN 엔진으로 보기 어려워 보인다. | ref-502, ref-404 | 아니오 | low | 2026-10-10 | — | — |
| f16 | [사실] | VDA 5050 3.0.0 은 동작의 blockingType 을 NONE·SINGLE·SOFT·HARD 네 값으로 두며, SINGLE 은 주행은 허용하되 다른 동작의 병렬 실행은 허용하지 않고 HARD 는 그 시점에 허용되는 유일한 동작이다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f17 | [사실] | VDA 5050 2.1.0 명세의 blockingType 은 NONE·SOFT·HARD 세 값뿐이어서, SINGLE 은 3.0.0 에서 추가된 값이다. | ref-031, ref-1425 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f18 | [의견] | 주행과 작업 활동의 동시 수행 가능성을 공정 모델의 제약으로 표현할 때 VDA 5050 의 SINGLE 과 HARD 를 구별해 다루는 편이 좋다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f19 | [사실] | Open-RMF rmf_fleet_adapter 패키지 2.14.0(2026-09-26) 변경 이력에는 단계 건너뛰기 요청의 키를 고친 항목 'Fix phase key for skip requests (#543)' 이 있다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | 단계 건너뛰기를 운영 정책에 넣는 구현은 rmf_fleet_adapter 패키지 버전과 건너뛰기 요청 스키마를 함께 기록해 두는 편이 좋다. | ref-1424, ref-366 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | Filippone·Pettinari·Pelliccione 의 비교 연구(arXiv 2603.15427, v1 2026-03-16, v2 2026-08-17, Journal ref IEEE Transactions on Software Engineering (2026))는 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·임무 개념 표현(표현력)·도구 지원 기준으로 비교한다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [사실] | 이 연구는 2026년 1월 4주 동안 83명에게 설문을 요청해 29개 완성 응답(응답률 34.94%)을 받고 일부 참여자와 후속 인터뷰(3명 실시간, 1명 서면)를 했으며, 같은 로봇 현장에서 형식별 처리량을 측정한 성능 비교가 아니라 분석 비교를 전문가 설문으로 검증한 연구다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [의견] | Filippone 외 비교 연구는 임무 기술 형식 선택의 검토 자료로 쓰되, 특정 형식이 항상 우수하다는 결론으로 옮기지 않는 편이 좋다. | ref-116 | 아니오 | medium | 2026-10-10 | — | — |
| f24 | [사실] | FaMe 는 BPMN 협업 다이어그램으로 다중 로봇 임무를 정의하고 모델링·구성·실행 단계를 거쳐 각 로봇에서 ROS 2 위에 그 협업을 직접 실행하는 공개 프레임워크이며, 구성 단계에서 신호 이벤트의 type 속성에 ROS 메시지 형을 지정해 BPMN 이벤트와 ROS 메시지를 잇는다. | ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [의견] | FaMe 는 BPMN 과 ROS 2 를 잇는 공개 구현이지만 Open-RMF 작업 상태나 VDA 5050 동작 상태와 BPMN 단계 상태 사이의 표준 매핑으로 볼 근거는 확인하지 못했으므로, oq-014 는 열린 상태로 두는 것이 맞다. | ref-1423, ref-031, ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [추정] | 확인한 원문들(CBV.ttl, VDA 5050 3.0.0, IngestorResult.msg)은 로봇 동작 완료와 업무 단계 각각의 정의까지만 제공하며, 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 표준 변환은 확인되지 않는다. | ref-044, ref-031, ref-049 | 아니오 | medium | 2026-10-10 | — | — |
| f27 | [의견] | VDA 5050 drop 완료를 곧바로 CBV arriving 또는 receiving 으로 단정하지 않고, 업무 측 확인으로 어느 단계인지 정하는 수준까지만 oq-001 의 답을 보강하는 것이 적절하다. | ref-044, ref-031 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-10-10 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | high | 2026-10-10 | https://www.omg.org/spec/BPMN/2.0.2/ | 아니오 |
| ref-1423 | University of Camerino PROS Lab | FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침) | 2022-05-03 | 정부·연구기관 | medium | 2026-10-10 | https://pros.unicam.it/fame/ | 아니오 |
| ref-366 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03-16 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-1425 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-and-workflow-modeling.md | 3, 5, 6, 7, 8, 11 | 갱신(차등, 외부 조사 메모 변환): 섹션 3 — 첫 문단의 근거를 원문 정의로 구체화: CBV 세 단계(f1), drop FINISHED 표 5(f2), IngestorResult 기본 필드 범위(f3), 별도 완료 조건 권고(f4, 의견) / 섹션 5 — 창고 밖 사례로 FaMe 농업·지상 로봇 협업 시뮬레이션(f7·f8, site_type 기타)과 분류 한계(f9) 추가 / 섹션 6(주제 페이지 2026-09-25-area02-s6 요약) — BPMN 규범 근거로 수신 작업·상관 키·타이머(f5·f6, 기존 Camunda 문장 보완), 취소 후 정리·보상(f10~f12), rmf_task_sequence 단계·이벤트 7종(f13~f15) / 섹션 7(주제 페이지 2026-09-25-area02-s7 요약) — VDA 5050 3.0.0 blockingType SINGLE(f16·f17, 발표일 언급 없음)과 SINGLE·HARD 구별 권고(f18, 의견), rmf_fleet_adapter 2.14.0 단계 건너뛰기 키 수정(f19·f20); 표의 BPMN 행을 2.0.2 규범판(ref-502)으로 보강 / 섹션 8(주제 페이지 2026-09-25-area02-s8 요약) — Filippone 외(ref-116) 항목을 v2·게재처·연구 방법으로 보강(f21~f23); FaMe 항목(ref-114)은 기존 내용 확인 / 섹션 11(주제 페이지 2026-09-25-area02-s11) — oq-014 부분 근거(f24·f25), oq-001 부분 근거(f26·f27), 새 질문 3건. 섹션 4·9·10 은 바꾸지 않는다. 다음 실행 후보: 32. 예외 복구·재계획·업무 연속성(f10~f12), 20. 로봇·제조사 관제 연동(f16~f18), 17. 작업 대상·자산 식별과 인계 추적(f1~f4). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 수신 작업 | Receive Task (BPMN) | 외부 참여자가 보낸 메시지가 도착할 때까지 기다리다가 메시지를 받으면 완료되는 BPMN 작업 유형이다. |
| 보상 | Compensation (BPMN) | 이미 성공적으로 끝난 단계의 결과가 더는 필요 없을 때 그 효과를 되돌리는 처리를 별도 활동으로 표현하는 BPMN 개념이다. |

## 열린 질문

새로 생긴 질문:

- 로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가? | 관련 영역: 24. 작업·워크플로 모델링, 32. 예외 복구·재계획·업무 연속성 | 근거: f10 | 종류: 일반
- Open-RMF rmf_task_sequence 의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 54. 시험·형식 검증·벤치마크 | 근거: f15 | 종류: 일반
- 운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가? | 관련 영역: 24. 작업·워크플로 모델링, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 10 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 3건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-01/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 의 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 적지 않았고(ref-031 published null), 릴리스 노트 페이지(메모 n10)는 원문 확인이 안 돼 출처에서 뺐다
    - f19: 'Fix phase key for skip requests (#543)' 에서 고친 키의 실제 이름은 변경 이력만으로 확인하지 않았다(#543 본문 미열람)
    - f15: rmf_task_sequence Bundle 이벤트의 병렬·합류 의미는 API 문서를 열지 않아 미확인
    - f7~f9: FaMe 시뮬레이션 시나리오가 실외 현장인지, 실물 로봇 실험의 규모는 공식 페이지에서 확인하지 못했다(site_type 기타)
    - f26: 로봇 하역 완료를 EPCIS 이벤트로 옮기는 공개 구현 사례는 이번 메모 범위에서 검색하지 않았다(확인 못 함)
    - ref-1425(VDA 5050 2.1.0) 발행일 미확인
- 범위 경계 위반 의심:
    - f16~f18: VDA 5050 blockingType 은 로봇·제조사 관제 인터페이스(20. 로봇·제조사 관제 연동) 쪽 정의이므로 이 영역에서는 공정 모델의 병행 제약 근거로만 쓴다
    - f10~f12: 취소·보상 처리 절차는 32. 예외 복구·재계획·업무 연속성과 겹치며, 이 영역에서는 워크플로의 상태·완료 조건 구분으로 한정한다
    - f1~f4: 재고 확정(CBV receiving)은 상위 업무 시스템(WMS) 연계 대상이며 ROP 는 완료 조건 구분과 대기만 맡는다
- 한계: 외부 조사 변환이라 검색·열람 집계 없음(queries 0 은 실제 검색 수가 아니다). web_fetch_available: true. 신규 출처 3건(ref-1423~ref-1425, 예약 구간 ref-1423~ref-1452 안), 기존 id 재사용 7건(ref-044·ref-031·ref-049·ref-502·ref-366·ref-404·ref-116). 메모의 출처 10개 중 n10(VDA 5050 3.0.0 릴리스 노트)은 원문 미확인으로 제외하고, SINGLE 추가의 대조 근거로 VDA 5050 2.1.0 명세(ref-1425)를 더했다. 메모의 n2(3.0.0 태그 명세)는 main 판 ref-031 과 같은 문서로 보아 ref-031 에 3.0.0 태그 raw 경로를 fetch_url 로 적었고, n4(BPMN 2.0.2 PDF)는 ref-502 와 같은 문서다. 검증 수정 반영: SINGLE 정의는 사실(f16)·'구별해야 한다'는 의견(f18)으로 분리, 발표일 삭제, IngestorResult 범위를 기본 정의 필드로 한정(f3), rmf_task_sequence 이벤트 7개(Placeholder 포함, f14), 변경 이력 키 이름 단정 안 함(f19), Filippone 외 v1·v2 날짜와 IEEE TSE 게재 정보 추가(f21), drop FINISHED 근거 위치 §6.2.3.2 표 5(f2), BPMN 2.0.2 서지(formal/2013-12-09, 2014-01)와 절 위치(f5·f11), FaMe 공식 페이지는 ref-503·ref-114 와 같은 연구팀 자료라 독립 교차 확인으로 세지 않음(f8). 교차 확인 0건이며 사실 finding 은 단일 출처라 신뢰도 medium 이하. 현장 유형 사례 finding 은 FaMe 농업·지상 로봇 협업 시뮬레이션(f7~f9, 기타)뿐이다. 열린 질문 해결 제안 없음: oq-001(f26·f27)·oq-014(f24·f25) 부분 근거만 냈다. oq-012·oq-013 근거 없음. 국내 자료 없음.
```

### runs/2026-10-09-27/research.md

```markdown
# 리서치 브리프 2026-10-09-27

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-27 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

트랙 실행: 트랙 `chat-based-configuration-and-operation` · 단계 2 · 답한 질문 q2-05, q2-06

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-05·q2-06·q2-07 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 3건 중 오래된 순), 단계 2 페이지 3절에 {#q2-05}·{#q2-06}·{#q2-07} 소절 없음
- 단계 2 완료 조건: 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정(초안 6절 '작업 요구에 적재물 식별 … 더할 것인가' 질문 열림)
- 업무 분해·배정 설계 초안 6절: 현장 장소 용어와 경유점 이름·지도 id·WMS 로케이션 코드를 잇는 이름 대응 규칙 미정(oq-029와 겹침)
- 단계 2 페이지 2절 q2-01 항목–원천 대응표의 '대상 화물' 행: 품목 단위와 적재 단위의 대응 원천 미확인
- IEEE 1872.1-2024 본문 미열람으로 작업 모델 대조 없음(단계 2 페이지 4절 남은 불확실성)

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. q2-05 지시 속 현장 장소 용어(예: 3층 출하 대기장, 2번 도크)와 공간 그래프 경유점 이름·지도 id·WMS 로케이션 코드를 대응시키는 이름 사전은 어떤 형식으로 두고 누가 관리하는가?
3. q2-06 채팅 지시의 '대상 화물'을 품목 단위(sku·수량)로 받을지 적재 단위(loadId·SSCC)로 받을지, 둘 사이 대응은 어느 시스템에서 가져오는가?
4. q2-07 IEEE 1872.1-2024 로봇 작업 표현 온톨로지는 작업 분해·선후 의존·배정 대상을 어떤 개념으로 표현하며, 업무 분해·배정 설계 초안의 업무·작업·배정 개념과 어떻게 대응하는가?
5. 실내 지도·용어 표준(IMDF, W3C SKOS, GS1 GLN 확장 성분)은 같은 장소의 정식 이름·별칭·코드를 어떤 구조로 담는가? (q2-05 의 이름 사전 형식, 단계 2 페이지 3절 겨냥)
6. 로봇이 보고하는 적재물 식별(VDA 5050 loads)과 물류 단위–품목 대응(GS1 EPCIS 집계 이벤트)은 어떤 필드로 표현되는가? (q2-06, 초안 6절 작업 요구 적재물 질문 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 교통 편집기(traffic-editor) 문서는 경유점(vertex)을 x·y·고도·이름·선택 파라미터로 저장하고 이름 기본값을 비워 두되 로봇이 작업을 끝내야 하는 경유점에는 이름을 요구하며, dock_name·pickup_dispenser·dropoff_ingestor·is_charger 같은 속성과 이름 붙은 층(L1 등)을 두고 승강기는 층을 이름으로 참조하지만, 별칭이나 다국어 이름 기능은 서술하지 않는다. | ref-079 | 아니오 | medium | 2026-10-09 | — | — |
| f2 | [사실] | Open-RMF 장소 스키마는 장소를 경유점 이름, 경유점 번호, 경유점과 방향을 담은 객체 가운데 하나로 지정한다. | ref-412 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | Open-RMF 건물 지도 그래프의 노드 메시지(GraphNode)는 x·y 좌표, 이름, 파라미터 목록을 가진다. | ref-414 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | OGC 커뮤니티 표준 IMDF 1.0.0 의 Unit 은 장소 운영 조직(Venue Organization)이 선언한 이름(name)과 그 조직이 인정하는 대체 이름(alt_name)을 언어 태그별 값 묶음(LABELS)으로 두고, 층 식별자(level_id)와 점 표현(display_point)을 함께 둔다. | ref-1393 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | W3C SKOS 권고안(2009-08-18)은 개념에 언어별 대표 이름(prefLabel), 대체 이름(altLabel), 화면에 보이지 않는 검색용 이름(hiddenLabel, 오탈자 포함)을 두고, 한 언어 태그당 대표 이름은 하나만 허용하며, 개념 체계 안에서 개념을 가리키는 코드(notation)를 따로 둔다. | ref-1394 | 아니오 | medium | 2009-08-18 | — | — |
| f6 | [사실] | GS1 은 시설 안 하위 위치(구역·선반 등)를 GLN 단독 또는 GLN 과 확장 성분(extension component)으로 식별하게 하며, 확장 성분은 물리적 위치를 가리키는 GLN 과 함께일 때만 유효하다. | ref-1400 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f7 | [사실] | Murata 외(arXiv 2509.12838, v2 2025-09-30, AROB-ISBC 2026 투고)는 사용자가 로봇마다 지정한 영역에서 학습한 공간 개념을 언어 모델의 작업 분해·다중 로봇 배정에 쓰는 틀을 제안하고, 배정 성공을 50회 중 47회(무작위 28회, 상식 기반 26회)로 보고했다(저자 보고). | ref-1398 | 아니오 | medium | 2025-09 | 수행 자원 | — |
| f8 | [추정] | q2-05 에 대해 확인한 형식을 종합하면, 이름 사전은 로봇 관제가 받는 정본 키(Open-RMF 경유점 이름·층 이름, VDA 5050 지도 id, WMS 로케이션 코드 또는 GLN·확장 성분)를 SKOS 의 notation 처럼 코드로 두고, 현장 호칭은 IMDF name·alt_name 이나 SKOS prefLabel·altLabel·hiddenLabel 같은 언어별 대표 이름·별칭으로 붙이는 형식이 선택지로 보이며, IMDF 가 이름을 장소 운영 조직이 선언하게 하듯 정본 이름은 현장 운영 조직이 정하고 ROP 는 대응표를 보관·검증하는 분담이 맞아 보인다(이 위키의 종합, 물류 현장 사례 미확인). | ref-079, ref-412, ref-414, ref-1393, ref-1394, ref-1400 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f9 | [추정] | 이번 검색 범위(한국어·영어)에서 물류창고 현장 호칭을 로봇 경유점 이름·WMS 로케이션 코드와 잇는 이름 사전을 정한 표준이나 공개 사례, 국내 WMS 로케이션 코드(동·열·연·단) 체계의 공식 자료는 찾지 못했고, 가장 가까운 연구는 가정 환경에서 학습한 공간 개념을 쓰는 Murata 외였다(부재 확인 아님). | ref-1398, ref-079 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | VDA 5050 공식 저장소의 상태 스키마(main 브랜치)는 로봇이 다루는 적재물 배열(loads)을 선택 필드로 두고, 적재물 객체에 필수 필드 없이 loadId(바코드·RFID 값 같은 고유 id, 감지했으나 식별 못 하면 빈 값)·loadType·loadPosition·boundingBoxReference·loadDimensions·weight 를 두며, 품목 코드·수량·SSCC 필드는 없다. | ref-051 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f11 | [사실] | Open-RMF 배송 작업의 적재물 항목은 품목 코드(sku)와 수량(quantity)을 필수로, 칸(compartment)을 선택으로 둔다. | ref-411 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f12 | [사실] | GS1 EPCIS 공식 저장소의 집계 이벤트(AggregationEvent) JSON 스키마는 type·action 을 필수로 두고 상위 단위 식별자(parentID, URI)와 개체 단위 하위 목록(childEPCs)·품목 수량 목록(childQuantityList)을 두며, action 이 DELETE 가 아니면 두 하위 목록 가운데 하나 이상을 비우지 않게 한다. | ref-1392 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f13 | [사실] | GS1 Belgium & Luxembourg 는 SSCC 를 추적할 수 있는 물류 단위(예: 여러 거래 단위를 묶은 팔레트)를 유일하게 식별하는 코드로 설명하며, 물류 단위는 같은 품목 또는 여러 품목으로 이루어질 수 있고 단위마다 SSCC 를 하나씩 붙이며, SSCC 와 내용물(품목·수량)의 연결 방식은 그 페이지에서 서술하지 않는다. | ref-1395 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f14 | [사실] | OPC UA for ISA-95 작업 제어 노드셋(모델 발행일 2024-01-31)의 자재 데이터형은 자재 정의 id·로트 id·하위 로트 id·수량·단위 등을 선택 필드로 둔다. | ref-130 | 아니오 | medium | 2024-01-31 | 작업 대상 | 원문 미열람 |
| f15 | [추정] | q2-06 에 대해 확인한 형식을 종합하면, 로봇 관제 인터페이스는 Open-RMF 배송이 품목 단위(sku·수량), VDA 5050 이 적재 단위(loadId)만 받고 둘 사이 대응 필드가 없으므로, ROP 작업 모델은 지시의 대상 화물을 품목 단위와 적재 단위 두 갈래로 받을 수 있게 두고 대응(어느 SSCC 단위에 어느 품목이 몇 개인가)은 EPCIS 집계 이벤트(parentID–childQuantityList)나 업무 시스템의 자재·로트 기록에서 가져오며, VDA 5050 loadId 는 SSCC 형식을 강제하지 않으므로 지시한 SSCC 와 로봇 보고 loadId 의 대조는 ROP 몫이 되는 구성이 선택지로 보인다(이 위키의 종합). | ref-411, ref-051, ref-1392, ref-130, ref-1395 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f16 | [추정] | 연계 대상: 품목과 물류 단위의 대응(포장·적재 구성)과 재고 정본은 상위 업무 시스템(WMS 등)과 EPCIS 이벤트 저장소가 관리하는 정보이며, ROP 는 그 대응을 읽어 작업 대상을 확인하는 쪽으로 보인다(이 위키의 종합). | ref-1392, ref-130 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f17 | [사실] | IEEE SA 는 IEEE 1872.1-2024(2024-06-18 발행)를 학습·로봇·자동화 분야의 작업 지식을 표현·추론·교환하는 온톨로지로 소개하며, 핵심 용어의 정의·속성·유형·구조·성질·제약·관계와 계층 계획기·설계자의 작업 지식 표현 방식을 다루고, 실무 구현 지침 P1872.1.1 이 따로 개발되고 있다고 밝힌다. | ref-504 | 아니오 | medium | 2024-06-18 | — | 원문 미열람 |
| f18 | [사실] | Balakirsky 외(MSEC 2017)는 로봇 작업 온톨로지 표준을 준비하는 국제 연구 그룹의 작업을 소개하며, 작업 구조(하위 클래스·범주·관계로의 분해)와 작업 공통·작업별 속성을 다루고 작업을 플랫폼·사용자와 잇는 공통 표현을 목표로 한다고 밝혔다. | ref-1396 | 아니오 | medium | 2017-06-08 | — | — |
| f19 | [사실] | Aguado 외(Frontiers in Robotics and AI 11권, 2024-07-10)는 IEEE 로봇·자동화 온톨로지 작업반의 로봇 작업 표현 하위 그룹이 목표에서 하위 목표로 가는 작업 분해를 담은 중간 수준 온톨로지를 만들고, 작업과 그 속성, 성능 관련 능력 용어, 산업 공정 작업 목록을 정의한다고 정리했다. | ref-042 | 아니오 | medium | 2024-07-10 | — | — |
| f20 | [추정] | q2-07 에 대해 공개 자료로 보면 IEEE 1872.1 계열 작업 온톨로지는 목표에서 하위 목표로 가는 분해를 핵심 구조로 두고 작업을 플랫폼(로봇)·능력과 잇는 것으로 보여 초안의 업무(목표)–작업(하위 목표·실행 단위)–배정(작업–로봇)과 대응 후보가 되지만, 표준 본문을 열람하지 못해 작업 사이 선후 의존과 배정 대상을 어떤 개념으로 표현하는지는 확인하지 못했다(이 위키의 종합). | ref-504, ref-1396, ref-042 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-1392 | GS1 (gs1/EPCIS GitHub) | EPCIS — JSON-Schema/schemas/AggregationEvent-JSON-Schema.json | 미확인 | 표준 | high | 2026-10-09 | https://github.com/gs1/EPCIS/blob/master/JSON-Schema/schemas/AggregationEvent-JSON-Schema.json | 아니오 |
| ref-1393 | OGC (Apple Inc. 기여) | Indoor Mapping Data Format (IMDF) 1.0.0 — Unit | 미확인 | 표준 | high | 2026-10-09 | https://docs.ogc.org/cs/20-094/Unit/index.html | 아니오 |
| ref-1394 | W3C (Miles, A., & Bechhofer, S. 편집) | SKOS Simple Knowledge Organization System Reference | 2009-08-18 | 표준 | high | 2026-10-09 | https://www.w3.org/TR/skos-reference/ | 아니오 |
| ref-1395 | GS1 Belgium & Luxembourg | Logistic units | 미확인 | 표준 | medium | 2026-10-09 | https://www.gs1belu.org/en/logistic-units | 아니오 |
| ref-1396 | Balakirsky, S. B., Schlenoff, C. I., Fiorini, S. R. 외 (NIST 게시, MSEC 2017) | Towards a Robot Task Ontology Standard | 2017-06-08 | 논문 | medium | 2026-10-09 | https://www.nist.gov/publications/towards-robot-task-ontology-standard | 아니오 |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. (Frontiers in Robotics and AI 11) | A survey of ontology-enabled processes for dependable robot autonomy | 2024-07-10 | 논문 | high | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full | 아니오 |
| ref-1398 | Murata, K., Hasegawa, S., Ishikawa, T., Hagiwara, Y., Taniguchi, A., El Hafi, L., & Taniguchi, T. | Multi-Robot Task Planning for Multi-Object Retrieval Tasks with Distributed On-Site Knowledge via Large Language Models | 2025-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2509.12838 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-1400 | GS1 | GLN extension component | 미확인 | 표준 | medium | 2026-10-09 | https://gs1.org/standards/id-keys/gln/extension-component | 예 |
| ref-411 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 아니오 |
| ref-412 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/place.json | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json | 아니오 |
| ref-414 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-10-09 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 예 |
| ref-504 | IEEE Standards Association | IEEE 1872.1-2024 — IEEE Standard for Robot Task Representation | 2024-06-18 | 표준 | medium | 2026-10-09 | https://standards.ieee.org/ieee/1872.1/6993/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-05 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 (신뢰도 low) / q2-06 답: f10·f11·f12·f13·f14·f15·f16 (신뢰도 low) / q2-07 부분 답: f17·f18·f19·f20 — 2절 q2-05·q2-06 답함(답한 실행 2026-10-09-27, #q2-05·#q2-06), q2-07 은 열림 유지; 3절 소제목 신설({#q2-05}: 로봇 관제 쪽 이름 f1~f3, 실내 지도·용어 표준의 이름·별칭 구조 f4·f5, GS1 하위 위치 f6(원문 미열람), 학습 공간 개념 연구 f7, 종합 f8(추정)·공백 f9 / {#q2-06}: VDA 5050 loads f10, Open-RMF 품목 단위 f11(#q2-01 기존 서술 가리킴), EPCIS 집계 이벤트 f12, SSCC f13, ISA-95 자재 f14, 종합 f15·연계 대상 f16 / {#q2-07}: 부분 답 f17~f20, 표준 본문 미열람 명시); 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건(조건 2 미충족, 전환 아니오), 8절 출처, 9절 이력 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(상황 개념의 대상 표현에 해석 결과 '대상 화물 참조' 짝 추가) 승인 시 2절 반영과 초안 v1.0 → v1.1(f10·f11·f12·f13). 6절 '작업 요구에 적재물 식별 … 더할 것인가' 질문에 q2-06 답(f15) 연결, '현장 장소 용어와 경유점 이름 … 이름 대응 규칙' 항목에 q2-05 답(f8) 연결, 'IEEE 1872.1-2024 … 대조하지 못했다' 항목에 부분 답(f20) 연결 |
| update | docs/ideas/chat-based-configuration-and-operation.md | 4 | 아이디어 페이지 4절: '필요한 데이터 항목과 원천' 소절의 장소·대상 화물 행 아래에 이름 사전 형식(f4·f5·f8)과 대상 화물 두 단위·대응 원천(f10·f12·f15) 소절 추가, 표준·형식 소절의 IEEE 1872.1 행 '미확인'은 지우지 않고 공개 자료 범위의 분해 구조(f18·f19·f20) 병기 |
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | 6, 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f1, f4, f5, f6, f8): IMDF name·alt_name, SKOS 대표·대체·숨은 이름과 notation, GLN 확장 성분을 장소 이름·별칭 사전 형식 후보로. 짝 엔진 영역 12. 채팅으로 업무 지시·오케스트레이션과 연결. 반영은 다음 해당 영역 실행에서. |
| update | docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f10, f12, f13, f15): VDA 5050 상태 loads 의 loadId(SSCC 형식 비강제)와 EPCIS 집계 이벤트의 parentID–childQuantityList, SSCC 물류 단위를 작업 대상 식별 단위 대응 근거로. |
| update | docs/categories/robot-ontology/robot-capability-and-task-representation.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f17, f18, f19): IEEE 1872.1-2024 의 공개 범위 설명(목표→하위 목표 분해, 작업–플랫폼·능력 연결, P1872.1.1 구현 지침 개발 중), 본문 미열람 명시. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 단순 지식 조직 체계 | Simple Knowledge Organization System (SKOS) | 개념에 언어별 대표 이름(prefLabel)·대체 이름(altLabel)·검색용 숨은 이름(hiddenLabel)과 코드(notation)를 붙여 용어 체계를 표현하는 W3C 권고안(2009)이다. |
| GLN 확장 성분 | GLN Extension Component | 물리적 위치를 가리키는 GS1 위치 코드(GLN)에 덧붙여 그 시설 안의 구역·선반 같은 하위 위치를 식별하는 GS1 의 코드 성분이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 10건
- 미확인 항목:
    - q2-07 부분 답: IEEE 1872.1-2024 본문(유료)과 P1872.1.1 미열람으로 작업 사이 선후 의존·배정 대상 개념의 표현 방식을 확인하지 못함
    - f6 GS1 GLN 확장 성분 페이지는 gs1.org 403 으로 원문 미열람(검색 요약 기준)
    - f17 IEEE SA 소개 페이지는 검색 요약 기준(원문 미열람)
    - ref-1396 NIST 게시 PDF 본문은 텍스트 추출 실패로 초록만 확인
    - ref-042 Frontiers 서베이는 본문 앞부분(10만 자)만 열람
    - 국내 WMS 로케이션 코드 체계(동·열·연·단) 공식 자료와 국내 물류센터의 SSCC–로봇 작업 연동 사례 미발견(부재 확인 아님)
    - IMDF LABELS 자료형의 정식 정의는 참조 절을 열지 않아 예시 기준
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
- 범위 경계 위반 의심:
    - f16: 품목–물류 단위 대응과 재고 정본은 분류 원문 19장의 상위 업무 시스템 경계라 '연계 대상: '으로 표시
    - f10: 로봇의 적재물 감지·식별(바코드·RFID 판독)은 로봇 자체 지능·제어 쪽이며, ROP 근거로는 보고 필드 구조만 씀
    - f7: 공간 개념 학습은 로봇 쪽 인식 기능이며, 장소 이름을 배정에 쓰는 구조만 근거로 씀
- 한계: 스키마 불일치 재실행. 반려 사유(f5·f17 이 벤더 문서만 근거인 [사실]인데 vendor_claim 표시 없음)에 대응하려 했으나 직전 반환값이 프롬프트에 들어 있지 않아 같은 세 질문(q2-05·q2-06·q2-07)으로 브리프를 다시 구성했다. 이번 브리프에는 출처 유형 '벤더 문서'가 없고, 모든 [사실] finding 은 표준·오픈소스 문서·논문에 기대므로 vendor_claim 대상이 없다. 트랙 실행(단계 2), web_fetch_available: true · fetch_mode full. 검색 12회/40, 신규 출처 10건/20(ref-051~ref-1400, 예약 구간 안), 재사용 5건(ref-411·ref-412·ref-414·ref-130 은 이번에 다시 열지 않아 fetched false, ref-504 는 검색 요약만). gs1.org·gs1uk.org 는 403 으로 열지 못했다. 질문 선택: target.json 지정 q2-05·q2-06·q2-07(현재 단계 열린 질문 오래된 순). 답한 질문: q2-05(이름 사전 형식은 표준 원문 근거, 관리 분담·물류 적용은 종합이라 low), q2-06(필드 구조는 원문, 대응 원천 결론은 종합이라 low). q2-07 은 표준 본문 미열람으로 부분 답이며 answered_question_ids 에서 뺐다. 한국 자료: 국내 WMS 로케이션 코드·GS1 Korea SSCC 적용 자료를 한국어 검색 2회로 찾았으나 공식 자료를 찾지 못했다. 교차 규칙: L. AI·학습 기술 관련 f7 은 44. 로봇 기반 모델·언어 모델 계획과 적용 대상 25. 작업 배정 — MRTA 에 함께 연결할 수 있다. 18. 실시간 세계 상태·데이터 일관성·34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음, 입력 누락 없음, 우선 지정 질문 없음. 후속 질문 3건. 온톨로지 변경 1건(상황 개념의 대상 표현에 '대상 화물 참조' 짝, 작업 요구는 능력 온톨로지 초안 대조 전이라 건드리지 않음). 열린 질문(oq) 신규 없음: 장소 이름 대응은 oq-029·oq-201, 적재 단위 판독 불일치는 oq-003·oq-036 과 겹친다. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 3건(갱신 상한과 별도).

## 트랙 블록

- 트랙: chat-based-configuration-and-operation · 단계: 2
- 답한 질문 id: q2-05, q2-06

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 이름 사전의 별칭(altLabel·hiddenLabel)이 여러 장소에 겹칠 때(예: '2번 도크'가 두 층에 있음) 챗봇은 층·구역 맥락으로 좁힐지 되물을지를 어떤 규칙으로 정하고, 그 규칙을 이름 사전에 어떻게 기록하는가? (q2-05 에서 파생) (관련: q4-20, q4-07) | 4 | f8 |
| — | SSCC 같은 적재 단위로 받은 지시에서 로봇이 보고한 loadId 가 지시한 SSCC 와 다르거나 빈 값일 때 ROP 는 진행·보류·재스캔·사람 확인 가운데 무엇을 하는가? (q2-06 에서 파생) (관련: oq-003, oq-036) | 4 | f10 |
| — | IEEE 1872.1-2024 의 실무 구현 지침 P1872.1.1 이나 공개 사용 사례·OWL 파일이 있어 작업 분해·선후 의존·배정 대상 개념을 본문 없이 확인할 수 있는가? (q2-07 에서 파생) | 2 | f17 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 상황 (Situation) | f10, f11, f12, f13 | 대상 표현에 해석 결과 '대상 화물 참조'를 짝으로 더한다: 품목 단위(sku·GTIN 과 수량, Open-RMF 배송 f11) / 적재 단위(SSCC 또는 로봇 보고 loadId, VDA 5050 loads f10, SSCC 물류 단위 f13). 장소 표현–공간 노드 참조 짝(v0.4)과 같은 방식이다. 두 단위 사이 대응 원천(EPCIS 집계 이벤트 f12, 업무 시스템)은 추정 근거(f15)라 정의에 넣지 않고 메모로만 둔다. 작업 요구의 적재물 속성(초안 6절 질문)은 능력 온톨로지 초안과 대조하지 않았으므로 건드리지 않는다. 기존 상태 '확정' 유지. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정
    - q2-07 부분 답(IEEE 1872.1-2024 본문 미열람)
    - q2-05·q2-06 답과 아이디어 페이지 4절 반영은 검증 승인 전
```

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
| f1 | [사실] | VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 범위 절에 명시한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 상태 메시지의 safetyState 는 비상정지 상태(eStop: AUTOACK·MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 보고하고, 즉시 동작 startPause·stopPause 로 자동 주행을 멈추고 재개하며, operatingMode 로 로봇이 자동 주문을 받는지(AUTOMATIC)·수동 제어 중인지(MANUAL)를 알린다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | Open-RMF 핵심 설계에서 교통 충돌 예방은 RMF 의 교통 스케줄 데이터베이스와 협상이 맡고 경로 계획은 각 플릿 관리자가 맡으며, 비상 대응 같은 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | Open-RMF 공식 저장소의 기능 요청(이슈 #658)에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동하며, 현재 비상 신호 메시지는 어느 건물·플릿 대상인지 구분하지 않는 불리언 값이어서 대상 플릿 목록(fleet_names)을 지정하자는 제안이 올라와 있다. | ref-580 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f5 | [사실] | ISO 3691-4:2023 은 무인 산업 차량(AGV·AMR·자동 대차·견인차 포함)과 그 시스템의 안전 요구와 검증 방법을 정하며, 운용 구역(operating zone)의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f6 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR) 한 대 또는 플릿을 현장에 통합·구성·맞춤화할 때의 안전 요구를 정하는 시스템 통합자용 표준으로, 로봇 자체 요구는 Part 1 이, 사용자 요구는 예정된 Part 3 이 맡는다. | ref-472 | 아니오 | medium | 2023-10 | 수행 자원 | 원문 미열람 |
| f7 | [사실] | ISO 10218-2:2025(산업용 로봇 응용과 로봇 셀)는 2011년판을 대체해 2025년 2월 발행됐으며, 협동 운전 요구(종전 ISO/TS 15066)를 본문에 통합하고 사이버보안 요구를 더했으며 '로봇 시스템' 대신 공작물·작업 프로그램·지원 설비까지 포함하는 '로봇 응용'을 강조한다. | ref-572 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f8 | [사실] | 중소벤처기업부는 대구 이동식 협동로봇 규제자유특구 실증으로 안전성을 검증한 뒤 이동식 협동로봇 안전기준 한국산업표준(KS)을 제정해 2024-11-01 부터 산업현장에서 활용할 수 있게 했다고 밝혔고, 그 전에는 명확한 기준이 없어 작업공간 분리나 안전펜스 설치 때문에 이동 중 작업이 사실상 불가능했다고 설명했다. | ref-573 | 아니오 | medium | 2024-11-03 | 제약 | 원문 미열람 |
| f9 | [사실] | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 사업주에게 로봇 운전 중 위험을 막기 위해 높이 1.8m 이상 울타리 설치 등을 요구하되, 고용노동부장관이 해당 로봇의 안전기준이 한국산업표준 또는 국제적으로 통용되는 안전기준에 부합한다고 인정하면 울타리 등 조치를 생략할 수 있게 한다. | ref-574 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f10 | [사실] | SafeGate(arXiv 2604.05427)는 자연어 작업 명령에서 ISO 13482 에 근거한 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람에게 확인 요청·거부 중 하나를 내고, 승인한 작업은 불변 조건·가드·중단 조건으로 된 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했으며, 230개 벤치마크 작업·30개 AI2-THOR 시나리오·실로봇 실험으로 평가했다고 저자가 보고한다. | ref-417 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f11 | [사실] | 국내에는 협동로봇 기술규격 ISO/TS 15066 이 KS B ISO/TS 15066 로 부합화되어 한국표준정보망에 등재되어 있다. | ref-581 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f12 | [사실] | Belzile 외(arXiv 2502.20693)는 사람이 붐비는 작업장에 이동 로봇을 배치할 때의 안전 위험을 정량 지표로 평가하는 틀을 제안하고 ISO/TS 15066·ANSI/RIA R15.08 등 관련 표준을 검토했으며, 건설 현장 사례로 검증했다. | ref-576 | 아니오 | medium | 2025-02 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | STPA(System-Theoretic Process Analysis) 계층 제어 구조 비교 연구는 복잡한 다중 이동 로봇 시스템에 STPA 를 적용해 중앙집중·계층형 등 제어 구조별 위험 시나리오와 원인 요인을 도출했다. | ref-577 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | Reliability Engineering & System Safety 게재 연구는 다중 이동 로봇의 운반 작업에서 충돌 위험을 STPA 와 확률 페트리 넷(SPN)을 결합해 모델링·분석했다. | ref-578 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | ISO 12100:2010 은 기계 설계의 위험성평가와 위험 감소 일반 원칙을 정하며, 위험 감소는 본질적 안전 설계 → 방호·보완 보호 조치 → 사용 정보의 순서로 앞 단계를 다한 뒤 다음 단계로 가는 3단계 방법을 따른다. | ref-579 | 아니오 | medium | 2010 | — | 원문 미열람 |
| f16 | [추정] | 분류 원문 질문과 관련해, 확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08-1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025 의 로봇 응용)을 나누고 STPA 연구는 개별적으로 정상인 구성요소 간 상호작용에서 위험을 찾으므로, 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. | ref-470, ref-472, ref-572, ref-577 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f17 | [추정] | ROP 가 직접 맡을 안전 몫은 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집, 일시정지·재개 지시, 비상 신호에 따른 플릿별 대피·주차 조율, 구역·권한 제약을 경로·배정에 반영하는 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. | ref-031, ref-004, ref-580 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f18 | [추정] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증과 현장 방호 설비는 로봇 제조사와 설비 안전 제어(분류 원문 9장) 쪽이며, ROP 는 그 상태와 결과를 받는 쪽으로 보인다. | ref-031, ref-470, ref-572 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [추정] | 피킹 구역에 작업자가 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고하면, ROP 는 해당 로봇의 진행 중 피킹 작업을 보류·재배정하고 재개 조건(안전 상태 해제, 운용 모드 AUTOMATIC 복귀)을 확인한 뒤 stopPause 등으로 재개를 지시해야 할 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f20 | [추정] | 출하 마감 전에 화재경보 같은 비상 신호가 오면 로봇이 주차 위치로 이동해 출하 준비 작업이 중단되므로, 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 성과(마감 준수)에 영향을 주는 것으로 보인다. | ref-580, ref-004 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f21 | [추정] | 25. 안전·위험 관리는 사이버보안 요구가 안전 표준에 들어온 점에서 26. 사이버보안·접근권한·개인정보와, LLM 명령의 실행 전 안전 판정에서 27. AI·학습·적응과 모델 운영·18. 사람–로봇 협업·운영 인터페이스와, 교통 협상에서 15. 다중 로봇 경로·교통 관리 — MAPF 와, 정지·재개 지시의 확실한 전달에서 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. | ref-572, ref-417, ref-004, ref-031 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-472 | Association for Advancing Automation (A3) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-572 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/73934.html | 예 |
| ref-573 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 예 |
| ref-574 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-417 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
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
    - ref-417·ref-577·ref-578 저자, ref-577·ref-580·ref-581·ref-004·ref-031 발행일 미확인
    - ISO 3691-4 의 제조사–통합자 책임 분담은 2차 해설에만 있어 finding 에서 제외
- 범위 경계 위반 의심:
    - f18: 안전 기능 설계·방호 설비는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 쪽이라 '연계 대상:'으로 표시
    - f12: 건설 현장 사례라 방법론 근거로만 제안(업종별 조건 연계)
    - f10: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 현장 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f5 가 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 처음부터 다시 작성했다(검색 11회/30). 이번 브리프는 벤더 문서 출처를 하나도 쓰지 않았고, 모든 [사실] finding 은 표준·정부·오픈소스·논문 출처에 기대며, 벤더 문서만 근거로 한 [사실] finding 이 없다(관련 finding: f5 는 이제 ISO 3691-4 표준 근거). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 신규 ref-031(VDA 5050 3.0.0 명세), 재사용 ref-004(rmf-core). 나머지 12건은 검색 요약 기준(원문 미열람, 신뢰도 상한 medium). ref-004 는 참고문헌 목록 요약이 입력에 없어 리서치 규칙 예시의 값을 그대로 썼다. 신규 출처 13건(ref-031~ref-581, 예약 구간 안). 한국 자료: 이동식 협동로봇 KS 제정 보도자료(ref-573), 산안규칙 제223조(ref-574), KS B ISO/TS 15066(ref-581). 트랙 반영 제안(nl-task-chatbot 단계 2, SafeGate)은 f10 으로 확인해 6절에 제안했다. 교차 규칙: SafeGate 는 27. AI·학습·적응과 모델 운영과 적용 대상 영역에 함께 연결하도록 f21 로 제안. 8·22 구분 관련 주장 없음. 정정 요청 없음.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:
…(발췌: 전체 207,642자 중 앞 39,837자)
````

### data/source_texts/ref-105.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# FLEET CONFIG =================================================================
# RMF Fleet parameters

rmf_fleet:
  name: "tinyRobot"
  limits:
    linear: [0.5, 0.75] # velocity, acceleration
    angular: [0.6, 2.0] # velocity, acceleration
  profile: # Robot profile is modelled as a circle
    footprint: 0.3 # radius in m
    vicinity: 0.5 # radius in m
  reversible: True # whether robots in this fleet can reverse
  battery_system:
    voltage: 12.0 # V
    capacity: 24.0 # Ahr
    charging_current: 5.0 # A
  mechanical_system:
    mass: 20.0 # kg
    moment_of_inertia: 10.0 #kgm^2
    friction_coefficient: 0.22
  ambient_system:
    power: 20.0 # W
  tool_system:
    power: 0.0 # W
  recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate
  recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks
  publish_fleet_state: 10.0 # Publish frequency for fleet state, ensure that it is same as robot_state_update_frequency
  account_for_battery_drain: True
  task_capabilities: # Specify the types of RMF Tasks that robots in this fleet are capable of performing
    loop: True
    delivery: True
  actions: ["some_action_here"]
  finishing_request: "park" # [park, charge, nothing]
  responsive_wait: True # Should responsive wait be on/off for the whole fleet by default? False if not specified.
  robots:
    tinyRobot1:
        charger: "tinyRobot1_charger"
        responsive_wait: False # Should responsive wait be on/off for this specific robot? Overrides the fleet-wide setting.
    tinyRobot2:
        charger: "tinyRobot2_charger"
        # No mention of responsive_wait means the fleet-wide setting will be used

  robot_state_update_frequency: 10.0 # Hz

fleet_manager:
  prefix: "http://127.0.0.1:8080"
  user: "some_user"
  password: "some_password"

# TRANSFORM CONFIG =============================================================
# For computing transforms between Robot and RMF coordinate systems

# Optional
reference_coordinates:
  L1:
    rmf: [[20.33, -3.156],
          [8.908, -2.57],
          [13.02, -3.601],
          [21.93, -4.124]]
    robot: [[59, 399],
          [57, 172],
          [68, 251],
          [75, 429]]
```

### data/source_texts/ref-376.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# Tasks in RMF

RMF simplifies task allocation and management across multi-fleet systems.
When a user submits a new task request, RMF will intelligently assign it to the robot in the fleet that can best perform the task. When

RMF supports three types of task requests out of the box:
* Clean: For robots capable of cleaning floor spaces in facilities
* Delivery: For robots capable of delivering items between locations in facilities
* Loop: For robots capable to navigating back and forth between locations in facilities
> Note: A single robot may be capable of performing one of more of the above tasks and fleet adapters can be configured to reflect the capability of its robots.
For more information on the supported task types, [click here](./task_types.md)

In RMF version 21.04 and above, tasks are awarded to robot fleets based on the outcome of a bidding process that is orchestrated by a Dispatcher node, `rmf_dispatcher_node`.
When the Dispatcher receives a new task request from a dashboard or terminal, it sends out a `rmf_task_msgs/BidNotice` message to all the fleet adapters. If a fleet adapter is able to process that request, it submits a `rmf_task_msgs/BidProposal` message back to the Dispatcher with a cost to accommodate the task. An instance of `rmf_task::agv::TaskPlanner` is used by the fleet adapters to determine how best to accommodate the new request. For more information on the task planner, [click here](./task_planner.md)

The Dispatcher then compares all the `BidProposals` received and submits a `rmf_task_msgs/DispatchRequest` message with the fleet name of the robot that the bid is awarded to. There are a couple different ways the Dispatcher evaluates the proposals such as fastest to finish, lowest cost, etc which can be configured.

Battery recharging is tightly integrated with the new task planner. `ChargeBattery` tasks are optimally injected into a robot's schedule when the robot has insufficient charge to fulfill a series of tasks. Currently we assume each robot in the map has a dedicated charging location as annotated with the `is_charger` option in the traffic editor map.

![RMF Bidding Diagram](images/rmf_core/rmf_bidding.png)
```
