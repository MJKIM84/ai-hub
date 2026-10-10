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
        "ref-1398"
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
        "ref-1398"
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
      "id": "ref-1398",
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
    "limits": "외부 조사 변환이라 검색 횟수 집계 없음(queries 0 은 미집계 표시). 신규 출처 6건(ref-1453~ref-1398, 예약 구간 ref-1453~ref-1482 안), 재사용 3건(ref-152 리뷰 논문·ref-168 LTAA·ref-404 rmf_task README, 모두 이번에 원문 열람). 원문 열람 9/9. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·6·7·8·9·11절)과 바뀐 출처(rmf_fleet_adapter 2.14.0)만 다뤘다. 검증 수정 반영: Zhang 외 절 번호(§2 문제 정의, §5 흐름 정식화·§5.3.2 거리 행렬 회피, §6 계획기 결합, §7·§7.2·표 1 실험)와 혼잡 비용을 '선택할 수 있는 대체 비용 모델'로 범위 한정(f21~f23), LTAA p.61 의 brute force 0.77·greedy 0.81·DP 0.95 병기와 초록 76% 반올림·arXiv 2025-12-02·저자 Hongrui Yu 정정(f4~f6, ref-168), 리뷰 본문 25대·표 I 45 AMR·표 IV 48 AMR 을 의견 근거에 병기(f3), Tuck 외 NFM 2024 게재 예정(f12, ref-1454), BidProposal 필드 5개와 같은 프로젝트 자료라 독립 확인 아님(f8·f9), #534 확인(f25). 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-030 근거 f4~f7, oq-053 근거 f8·f9·f11, oq-054 근거 f12·f14. 교차 확인 0건이라 사실 finding 신뢰도는 medium 이하. 현장 유형 사례 finding 은 병원 모사 환경(f15~f17)뿐이고 물류창고 실측 비교(2절 질문)는 이번에도 찾지 못함. 국내 자료 없음. L. AI·학습 기술 관련 f4~f7 은 47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안한다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-10-02/verification.json

```json
{
  "run_id": "2026-10-10-02",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2501.08726(2025-01-15, Meseguer Valenzuela·Blanes Noguera)의 §II 소절이 A. Heuristics, B. Meta-heuristics, C. Exact and matheuristic Methods, D. Market-based Approach, E. Artificial Intelligence 이다. PDF 는 텍스트 추출 서비스를 거쳐 열었다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 표 I~V 의 열이 Method / Centralized·Decentralized / Framework / Fleet Size / Remarkable results 이다. 단, 브리프 한계 기술의 '선정·제외 절차가 원문에 없어 총 검토 편수 미확인'은 원문과 다르다. 원문은 Google Scholar 1440건에서 가장 관련 있는 52편을 골랐다고 적는다. finding 밖이므로 수치를 페이지에 넣지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "근거를 확인했다: 본문의 'up to 25 robots'(예외 Shi 외 2024 의 1923 이동 랙), 표 I L. Li 외 최대 45 AMR, 표 IV Teck 외 2023 3~48 AMR. 의견 태그를 유지하고 주체를 '이 위키의 의견'으로 밝힌다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PDF v1 결과 절 'overall success rate of 75.97%, positioning it between Q-learning (73%) and DQN (77%)'. PDF v1 초록에 76% 가 있다. 다만 arXiv 초록 페이지(메타데이터)의 초록에는 76% 가 없어서, 기준을 'PDF v1 초록'으로 밝혀야 한다. 저자 보고(TEACh 건설 작업 실험)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PDF v1 후반부에 brute force·greedy·DP 성공률 0.77·0.81·0.95 와, 결정적 알고리즘이라 불확실성 모델이 없어 비교 그림에서 뺐다는 설명이 있다(텍스트 추출로 열람, 쪽 번호는 검증자가 확인하지 못함). 저자 보고."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PDF v1 초록 'reaches 77% completion with superior workload balance, exceeding all traditional methods', 결론 'Heavy Excels setting (77.1% success with balanced workloads)'. arXiv 초록 페이지는 같은 뜻을 'outperforming all traditional methods' 로 적어 판마다 표현이 다르다. 기준 판을 밝힌다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f4~f6 은 원문으로 확인했다. 이 finding 은 이 위키의 의견이다. 출처 충돌(oq-030)은 한쪽을 고르지 않고 초록의 표현과 본문의 DP 0.95 를 둘 다 제시하는 설명으로만 쓴다. oq-030 은 해결하지 않는다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw BidProposal.msg 의 주석('published by a Fleet Adapter in response to a BidNotice')과 다섯 필드 fleet_name·expected_robot_name·prev_cost·new_cost·finish_time 이 일치한다. 발행일 미확인, 확인일 2026-10-10. evidence 의 BidResponse 관련 내용은 검증자가 확인하지 않았으므로 본문에 쓰지 않는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 근거 두 건(ref-1453·ref-404)은 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아니다. 최적성 손실 수치 근거가 없다는 점을 남긴다. oq-053 은 부분 근거일 뿐이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README 'For a given collection of tasks and robots belonging to a fleet (ie, they share physical and kinematic traits)…', 요청된 시작 시각, 배터리 제약과 충전 작업 자동 삽입. 발행일 미확인, 확인일 2026-10-10."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. Zhang 외 arXiv 판(2508.05890v1)에서 선형 배정이 'optimal one-shot assignments' 를 준다는 서술을 확인했다. 선형 배정에 대한 진술을 TaskPlanner 의 성질로 옮기지 않도록 범위를 한정하는 의견으로만 쓴다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2403.11737v1(2024-03-18). comment 는 'to be published in NASA Formal Methods Symposium 2024'. 과업 튜플(id·출발·도착 위치·도착 시각·마감), 용량, 점진 풀이가 원문과 일치한다. 게재본(쪽·DOI)은 확인하지 않았다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'even satisfying solutions without guaranteed optimality are relevant', 국소 운동 계획·충돌 회피는 downstream planners 몫, 정리 5.1(건전)·5.2(완전). 완전성에는 솔버의 건전·완전성과 D=D_max 조건이 필요하고, 일부 증명은 부록에 '(Sketch)'로 되어 있다. 조건부 결과임을 밝힌다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 근거를 확인했다: §2 는 휴리스틱 방법이 엄격한 마감에서 완전성 보장을 못 한다고 적는다. 창고 출하 마감 사례가 없다는 한계를 그대로 남긴다. oq-054 는 해결하지 않는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 벤치마크 200개(작업 10~30 × 에이전트 5~20 × 각 10개), 용량 2·3, 마감 균등 분포, 최악 이동 시간 가중치. 초록은 'hospital-like environment', §6 은 복도와 방 20개의 실내 공간으로 적는다. 병원 '모사' 환경 계산 실험이다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 과업 튜플과 갱신 계획 정의('past actions and the current action are unchanged')."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 원문은 솔버 성능만 보고하고 실제 병원·로봇 운행 결과가 없다. 매트릭스와 사례 표에 '모사 환경 계산 실험'을 밝히게 한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2506.07293v1(2025-06-08) 초록. GVD 로드맵, 구역 분할, push-pop(FIFO) 재분배, makespan 최소화가 원문과 일치한다. 용어는 용어집의 '경로망 (Roadmap)'으로 맞춘다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 본문 'exceeding 96% in the random scenario', 분리 시나리오 58~100%, 결론의 제어기 구현과 이종 로봇 확장 계획. README 는 Python 3.9+, MIT, RAS 2025-12 를 표기한다. 논문과 코드는 같은 팀 산출물이라 독립 재현이 아니다. README 는 로드맵을 가시성 기반 로드맵(VBRM)으로 설명해 논문의 GVD 설명과 다르므로, 공개 구현을 'GVD 구현'으로 쓰지 않는다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 근거를 확인했다: 'our method cannot achieve deadlock-free'."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IFAAMAS AAMAS 2026 목록(Paphos, 2026-05-25~29, Monash 저자 5인)을 검색 결과로 확인했다. 초록에 쌍별 거리 계산 회피가 있다. IFAAMAS PDF 는 검증자가 텍스트를 추출하지 못해, 같은 논문의 arXiv 판(2508.05890v1)으로 내용을 대조했다. 단일 출처(같은 저자의 두 판)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록 '20,000 agents and 30,000 tasks within 1-second planning time'. arXiv v1 은 에이전트 4000~20000, 표 1 에 Sortation Large 20000 행이 있다. 저자 보고, 격자 계산 실험이다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv v1): 'The default edge cost for our flow model is the edge cost from the map, i.e., unit cost for grid maps' 와 대체 비용 모델 두 가지(계획기 혼잡 추정, 과거 실행 평균 대기 시간). 게재본의 절 번호는 검증자가 대조하지 못했으므로 페이지에 절 번호를 쓰지 않는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 두 연구의 환경·지표가 다르다는 점은 원문으로 확인했다. 공통 벤치마크 비교는 없다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw CHANGELOG 2.14.0 태그 '2.14.0 (2026-09-26)' 에 'Submit bid as long as fleet name exists (in string or array) (#534)' 항목이 있다. FleetUpdateHandle.cpp 코드 대조는 검증자가 하지 않았다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. ROS 배포판별 반영 시점은 확인하지 않았다는 한계를 병기한다."
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
      "f8 은 기존 7절(주제 페이지 s7)·5절의 'Open-RMF 입찰이 비용을 담는다' 문장(ref-376)과 겹친다. 기존 문장과 각주를 유지하고 필드 세부만 더한다.",
      "f10 은 기존 6절·10절의 rmf_task 배정·충전 삽입 문장(ref-404)과 겹친다. ref-404 각주를 재사용하고 범위(한 플릿)만 더한다.",
      "f4~f7 은 기존 oq-030(출처 충돌)과 연결된다. 해결이 아니라 근거 보강이다.",
      "f8·f9·f11 은 oq-053, f12·f14 는 oq-054 와 연결된다. 둘 다 부분 근거이고 해결이 아니다.",
      "트랙 반영 제안 2026-09-25-66(TaskPlanner 탐욕·A*)·2026-09-25-74(평가기 기본값 충돌)·2026-09-25-77(재배정은 같은 플릿 안)·2026-10-09-25(Choe 외 최근접 대비 26%)는 f9~f11 과 주제가 겹치지만 이번 브리프의 finding 이 아니다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f18 의 '로드맵'은 용어집 'roadmap: 경로망 (Roadmap)'과 다르다. 본문에서는 '경로망(roadmap)'으로 쓴다.",
      "f18 의 '일반화 보로노이 다이어그램(GVD)'은 용어집 'generalized-voronoi-graph: 일반화 보로노이 그래프 (GVG)'와 다른 용어다. 같은 개념으로 링크하지 말고 첫 등장 시 영문을 풀어 쓴다."
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": [
      "ref-168 은 f4·f5·f6 세 finding 의 evidence 에 직접 인용 구절이 있다. 페이지에서는 이 출처의 직접 인용을 1회 이하로 줄이고 나머지는 재서술해야 한다."
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f4·f6: 초록 인용(76%, Heavy Excels 77%·전통 기법 모두 우위)은 'arXiv PDF v1 초록 기준'이라고 밝힌다 — arXiv 초록 페이지 메타데이터에는 76% 가 없고 표현도 'outperforming' 이라 달라서, 판을 밝히지 않으면 독자 대조 때 어긋난다.",
    "f4~f6: 6절·11절에 쓰는 LTAA 수치(75.97%·73%·77%·77.1%·0.77·0.81·0.95)에는 '저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님'을 병기한다 — 논문의 실험 보고값이다.",
    "f4~f7(11절 oq-030): oq-030 을 해결로 바꾸지 않는다. 초록의 Heavy Excels '전통 기법 모두 우위' 표현(f6)과 본문의 DP 0.95 비교 제외 설명(f5)을 둘 다 [사실]로 제시하고, f7 은 '[의견](이 위키의 의견)'으로 충돌 원인 설명으로만 적는다 — 결정적·확률적 비교군을 같은 조건으로 비교한 자료가 원문에 없다.",
    "f3·f7·f11·f14·f17·f20·f26([의견])과 f9·f24([추정]): 문장에 '이 위키의 의견' 또는 '이 위키의 종합'을 밝힌다 — 의견의 주체를 표시해야 한다.",
    "6절(문헌 검토 문장): 기존의 '검토 편수·계열 구분·실험 플릿 규모 미확인' 문장을 f1·f2(다섯 계열, 표 I~V 의 열)로 바꾸고, 플릿 규모는 f3 의견대로 한 수치로 요약하지 않는다. 근거를 쓰려면 f3 evidence 의 세 값(본문 25대, 표 I 45대, 표 IV 3~48대)만 쓴다. 검토 편수는 '원문에 없다'고 쓰지 말고 언급하지 않는다 — 원문에 선정 서술이 있지만 이번 브리프 finding 이 아니므로 additional_research_requests 로 넘긴다.",
    "f8·f9(7절·9절): BidProposal(ref-1453)과 rmf_task README(ref-404)를 서로의 독립 교차 확인으로 쓰지 않는다. f9 는 [추정]으로 두고 oq-053 은 해결로 바꾸지 않고 부분 근거로만 연결한다 — 두 출처 모두 Open-RMF 프로젝트 자료다.",
    "f10·f11(6절·9절): TaskPlanner 의 최적 배정은 '한 플릿의 주어진 작업 집합'에 한정된다고 적고, Zhang 외의 '최적 단발 배정' 서술(f11 근거)을 TaskPlanner 의 성질로 옮기지 않는다.",
    "f12·f14(5절 물류창고 표 제약 행): '출하 마감을 배정 목적함수에 넣는 방법은 미확인이다'를 지우지 않는다. 마감을 필수 제약으로 두는 정식화가 병원 모사 연구에 있다는 점(f12, [사실])과 창고 출하 마감 연동 사례 미확인(f14, [의견])을 덧붙인다. oq-054 는 해결로 바꾸지 않는다.",
    "f15~f17(5절 신규 사례): 현장 유형을 '병원'으로 밝히되 '병원 모사 환경의 계산 실험(그래프 추상화 벤치마크)'이라고 함께 적는다. 여섯 항목은 finding 이 있는 시작 조건(f16)·수행 자원(f15)·제약(f12 마감·용량)·예외·성과(f17)만 채우고, 작업 대상·완료·인계는 '미확인'으로 둔다. 병원 현장 실증·운영 사례로 쓰지 않는다 — 원문에 실제 병원·로봇 운행 결과가 없다.",
    "site_matrix_updates: 병원 칸을 넣는다면 title 에 '모사 환경 계산 실험'을 병기하고 site_type 은 '병원', link 는 대상 세부영역 페이지로 한다 — f17 의 분류 한계를 매트릭스에도 반영한다.",
    "f13(6절·8절): '건전·완전'은 '논문의 모델·인코딩 가정(솔버의 건전·완전성, D=D_max) 아래의 결과'로 적고, 최소 이동 비용의 최적해를 보장한다고 쓰지 않는다. 국소 경로 계획·충돌 회피는 하위 계획기(연계 대상) 몫이라고 밝힌다.",
    "f18~f24(6절·8절): 경로·충돌·교착 처리 자체는 27. 다중 로봇 경로·교통 관리 — MAPF 로 연결만 하고, 이 영역 본문에는 배정 비용에 환경 구조·혼잡을 반영하는 부분만 쓴다. MRTA-RM 을 교착 없음 보장으로 쓰지 않는다(f20). MRTA-RM 과 Zhang 외의 수치를 순위로 비교하지 않는다(f24).",
    "f19·ref-1456(8절): 공개 구현은 '저자 공개 Python 구현(MIT, 같은 팀 산출물이라 독립 재현 아님)'까지만 쓰고 'GVD 로드맵 구현'이라고 쓰지 않는다 — 검증자가 연 README 는 로드맵을 다른 방식(가시성 기반)으로 설명해 논문 설명과 다르다.",
    "f21~f23(6절·8절): 20,000 에이전트·30,000 작업·1초 수치에 '저자 보고, 격자 지도 계산 실험(실제 로봇 배치 아님)'을 병기하고, 논문 내부 절 번호(§5·§6·§7)는 본문에 쓰지 않는다 — 게재본 절 번호를 검증자가 대조하지 못했다.",
    "f25·f26(7절): rmf_fleet_adapter 2.14.0(2026-09-26) #534 는 '패키지 태그 기준, ROS 배포판 반영 시점 미확인'을 병기한다.",
    "용어(f18): 'roadmap'은 용어집 표기 '경로망(roadmap)'으로 쓴다. GVD 는 첫 등장 시 '일반화 보로노이 다이어그램(Generalized Voronoi Diagram, GVD)'으로 풀어 쓰고, 용어집 '일반화 보로노이 그래프(GVG)'에 같은 개념으로 링크하지 않는다. makespan 은 첫 등장 시 '전체 완료 시간(makespan)'으로 쓴다.",
    "용어집 후보 '최소 비용 흐름(Minimum-Cost Flow)'·'이론 모듈로 만족 가능성(SMT)' 2건은 기존 용어와 겹치지 않으므로 신규 등록(action: add)한다.",
    "인용: ref-168 의 직접 인용은 페이지 전체에서 1회 이하로 하고, 나머지는 재서술한다 — 출처당 직접 인용 1회 규칙.",
    "참고문헌 ref-168: 각주와 reference_updates 를 '저자 Kaitha, S. p. r., & Yu, H., 발행일 2025-12-02, 접근일 2026-10-10'으로 고치고 '(원문 미열람)'을 뗀다 — 검증자가 arXiv 에서 저자 Hongrui Yu 와 v1 제출일 2025-12-02 를 확인했고, 이번에 원문을 열었다.",
    "참고문헌 ref-152·ref-404: 각주 접근일을 2026-10-10 으로 고치고, ref-152 는 '(원문 미열람)'을 뗀다 — 이번 실행에서 원문을 열었다.",
    "신규 참고문헌 ref-1453~ref-1398: 각주를 '기관, 제목, 발행일(모르면 미확인), URL, 접근일 2026-10-10' 형식으로 등록한다. ref-1453·ref-1456 은 발행일 '미확인', ref-1457 은 '2026-05'(AAMAS 2026)로 쓴다.",
    "open_questions_new 4건: 등록한다. 1번(입찰 비용 정규화)은 관련 기존 질문 oq-053·oq-082, 3번(LTAA 비교군 재평가)은 oq-030 을 관련 질문으로 표시하고, 기존 질문을 해결로 바꾸지 않는다.",
    "트랙 반영 제안 16건(data/area_reflection_proposals.json): 이번 브리프의 finding 이 다루지 않았으므로 본문에 반영하지 않고 상태 '제안'을 유지한다 — 브리프 밖 내용을 넣으면 드리프트다. 다음 25. 작업 배정 — MRTA 실행에서 처리한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 26건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: 없음(검증자는 arXiv PDF 2건을 텍스트 추출 서비스로 열었다. AAMAS 2026 PDF(ref-1457)는 텍스트를 추출하지 못해 같은 논문의 arXiv 판 2508.05890v1 과 IFAAMAS 목록 검색 결과로 대조했다). 주의: 모든 [사실] 주장이 단일 출처이고, LTAA·MRTA-RM·Zhang 외·Tuck 외의 수치는 저자가 보고한 시뮬레이션·계산 실험 값이라 현장 실측이 아니다. 병원 사례(Tuck 외)는 병원 모사 그래프 벤치마크다. BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 서로 독립 확인이 아니다. LTAA 초록은 판에 따라 표현이 다르다(PDF v1 초록: 76%·'exceeding', arXiv 초록 페이지: 76% 없음·'outperforming'). 열린 질문 oq-030·oq-053·oq-054 는 부분 근거만 더했고 해결 인정 없음. 브리프 기록 메모: ref-1454·ref-1455·ref-1457 은 fetched true 인데 fetch_url 이 비어 있다(앞의 두 건은 기록된 URL 이 원문 페이지라 열람을 확인했다). 브리프 한계 기술의 '문헌 검토의 선정 절차가 원문에 없다'는 원문과 다르다(원문은 1440건에서 52편을 골랐다고 적는다). 브리프는 한국어 검색과 국내 자료가 없고(외부 조사 변환, 검색 0회 미집계), 실행 컨텍스트의 트랙 반영 제안 16건(최근접 대 MILP 비교 Choe 외 포함)을 검토하지 않아 이번 페이지에 반영하지 않는다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-10-10-02/pages.json

```json
{
  "run_id": "2026-10-10-02",
  "outline": [
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1900,
      "summary": "기존 물류창고 사례의 제약 행에 마감 필수 제약 정식화(병원 모사 연구)와 창고 출하 마감 연동 사례 미확인을 더하고, 병원 모사 환경의 계산 실험 사례를 여섯 항목으로 더한다. [사실][^ref-1454]",
      "planned_findings": [
        "f12",
        "f14",
        "f15",
        "f16",
        "f17",
        "f13"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2700,
      "summary": "이동로봇 플릿 작업 배정 연구는 2025-01 문헌 검토에서 다섯 계열로 정리되며, 2026-09-25 정리분은 이전 주제 페이지로 잇고 한 플릿 안의 최적 배정, 마감·용량 제약 배정, 혼잡 반영 배정, LLM 배정의 원문 수치를 소제목으로 나눈다. [사실][^ref-152]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f10",
        "f12",
        "f13",
        "f18",
        "f20",
        "f21",
        "f23",
        "f24",
        "f4",
        "f5",
        "f6",
        "f7"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "Open-RMF 는 입찰 기반 배정을 구현하고 VDA 5050 은 배정을 관제 기능으로만 규정하며(이전 정리분은 2026-09-25 주제 페이지), 입찰 제안 메시지 다섯 필드와 rmf_fleet_adapter 2.14.0 의 플릿 이름 필터 수정을 더한다. [사실][^ref-1453][^ref-1398]",
      "planned_findings": [
        "f8",
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1100,
      "summary": "2026-09-25 에 고른 고전·시뮬레이션·국내 자료는 이전 주제 페이지로 잇고, 2024~2026 배정 연구로 SMT 기반 마감·용량 배정, MRTA-RM, 최소 비용 흐름 기반 대규모 배정을 저자 보고 조건과 함께 더한다. [사실][^ref-1454][^ref-1455][^ref-1457]",
      "planned_findings": [
        "f12",
        "f13",
        "f15",
        "f19",
        "f22"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 800,
      "summary": "두 수준 배정에서 플릿이 낼 수 있는 정보의 예로 입찰 제안 다섯 필드가 있으나, 플릿 안 최적 배정은 한 플릿의 작업 집합에 한정되어 전체 최적이 보장되지 않을 것으로 보인다. [추정][^ref-1453][^ref-404]",
      "planned_findings": [
        "f8",
        "f9",
        "f10",
        "f11"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "section": "11. 열린 질문",
      "budget_chars": 1200,
      "summary": "2026-09-25 까지의 질문 서술은 이전 주제 페이지로 잇고, oq-030·oq-053·oq-054 에 부분 근거를 더하되 모두 열림으로 두며, 새 질문 4건을 올린다.",
      "planned_findings": [
        "f5",
        "f6",
        "f7",
        "f9",
        "f14"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-optimization/task-allocation-mrta.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5·6·7·8·9·11·13절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 다섯 계열, LTAA 원문 수치, BidProposal 다섯 필드·rmf_fleet_adapter 2.14.0, 2024~2026 연구 3건, 새 열린 질문 4건, 각주 정정). 2차 수정: 6·7·8·11절을 replace 로 바꿔 첫 문단에 2026-09-25 주제 페이지 링크를 넣고 8절 첫 문단을 링크 대상과 맞췄으며, 분리 뒤 오해되는 'n절' 참조를 세부영역 페이지 절 이름 참조로 바꿈",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-006",
              "ref-031",
              "ref-090",
              "ref-105",
              "ref-132",
              "ref-152",
              "ref-168",
              "ref-236",
              "ref-237",
              "ref-376",
              "ref-393",
              "ref-394",
              "ref-398",
              "ref-399",
              "ref-400",
              "ref-402",
              "ref-403",
              "ref-404",
              "ref-1453",
              "ref-1454",
              "ref-1455",
              "ref-1456",
              "ref-1457",
              "ref-1398"
            ],
            "last_run": "2026-10-10"
          },
          "content": "(절 본문 생략 — runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"6. 대표 접근법과 기술\" 절(2,917자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"11. 열린 질문\" 절(1,653자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"8. 대표 연구와 자료\" 절(1,232자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(814자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(723자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area25-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 25. 작업 배정 — MRTA 의 \"3. 왜 중요한가\" 절(438자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 25. 작업 배정 — MRTA | 5·6·7·8·9·11·13절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 다섯 계열, LTAA 원문 수치와 oq-030 부분 근거, Open-RMF 입찰 제안 필드·rmf_fleet_adapter 2.14.0, 2024~2026 배정 연구 3건, 새 열린 질문 4건), 1차 수정 지시 23건·2차 수정 지시 2건(이전 주제 페이지 링크 복원, 절 상호참조 명시) 이행 | run 2026-10-10-02",
  "index_updates": {
    "home_recent": "2026-10-10 — 25. 작업 배정 — MRTA: 병원 모사 환경의 계산 실험 사례, 문헌 검토의 다섯 계열, LTAA 원문 수치(oq-030 부분 근거), Open-RMF 입찰 제안 필드, 2024~2026 배정 연구 3건을 더했다",
    "category_recent": "2026-10-10 — 25. 작업 배정 — MRTA: 마감·용량 제약 배정(SMT), 혼잡 반영 대규모 배정(MRTA-RM, 최소 비용 흐름), 두 수준 배정에서 플릿이 내는 입찰 정보와 한계를 갱신했다",
    "area_recent": "2026-10-10 — 25. 작업 배정 — MRTA: 5·6·7·8·9·11절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 계열, LTAA 원문 수치, BidProposal 다섯 필드, 2024~2026 연구 3건, 새 열린 질문 4건, 2026-09-25 주제 페이지 링크 유지)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "minimum-cost-flow",
      "term_ko": "최소 비용 흐름",
      "term_en": "Minimum-Cost Flow",
      "definition": "간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다.",
      "description": "온라인 다중 에이전트 픽업·배송의 작업 배정을 환경 그래프 위의 최소 비용 흐름으로 풀어 로봇·작업 모든 쌍의 거리 행렬 계산을 피하는 연구가 있다(AAMAS 2026).",
      "related_areas": [
        25,
        27
      ],
      "sources": [
        "ref-1457"
      ]
    },
    {
      "action": "new",
      "slug": "satisfiability-modulo-theories",
      "term_ko": "이론 모듈로 만족 가능성",
      "term_en": "Satisfiability Modulo Theories (SMT)",
      "definition": "산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다.",
      "description": "온라인으로 도착하는 픽업·배송 작업의 배정, 로봇 적재 용량, 엄격한 마감을 SMT 제약식으로 표현하고 점진 풀이로 배정하는 연구가 있다(2024-03 프리프린트).",
      "related_areas": [
        25
      ],
      "sources": [
        "ref-1454"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-152",
      "org": "Meseguer Valenzuela, A., & Blanes Noguera, F.",
      "title": "Task Allocation in Mobile Robot Fleets: A review",
      "published": "2025-01",
      "url": "https://arxiv.org/abs/2501.08726",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "이동로봇 플릿 작업 배정 방법을 휴리스틱·메타휴리스틱·정확·수리 휴리스틱·시장 기반·인공지능 기반의 다섯 계열로 나누고 표 I~V 로 각 연구의 구조·구현 환경·플릿 규모·결과를 정리한 리뷰 프리프린트(arXiv 2025-01-15). 2026-10-10 PDF 원문을 열어 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "LLM 작업 배정 에이전트(LTAA)를 TEACh 데이터셋 건설 작업에서 결정적 비교군(brute force·greedy·DP)과 강화학습(Q-learning·DQN)에 견준 프리프린트. 2026-10-10 v1 PDF 원문을 열어 결과·결정적 비교군 설명·결론을 확인했고, 저자 표기를 Kaitha, S. p. r., & Yu, H.(Hongrui Yu)로, 발행일을 arXiv v1 제출일 2025-12-02 로 정정했다. 초록 표현은 판(PDF v1 초록과 arXiv 초록 페이지)마다 다르다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "로봇 간 최적 작업 배정·순서를 푸는 TaskPlanner API 와 배터리 제약에 따른 충전 작업 자동 삽입을 설명한 README. 2026-10-10 계획기 대상이 물리·운동 특성을 공유하는 한 플릿의 로봇·작업 집합임을 원문으로 다시 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "온라인으로 도착하는 마감 있는 픽업·배송 작업을 용량 제한 로봇에 배정하는 문제를 SMT 로 인코딩하고 모델·인코딩 가정 아래 건전성·완전성을 증명한 뒤 병원 모사 그래프 벤치마크로 평가한 논문(arXiv comment: NFM 2024 게재 예정).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "GVD 경로망을 구역으로 나누고 구역 사이 로봇 재분배 후 작업을 배정해 밀집 환경의 충돌·교착을 줄이는 대규모 배정 방법(MRTA-RM)과 수백 대 동적 시뮬레이션 결과(저자 보고). 교착 없음은 보장하지 않는다고 밝힌다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "MRTA-RM 저자 공개 Python 구현(MIT)의 README. 논문과 같은 팀 산출물이라 독립 재현 근거가 아니며, 로드맵 설명이 논문의 GVD 설명과 다르다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
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
      "summary": "온라인 MAPD 의 작업 배정을 환경 그래프 위 최소 비용 흐름으로 풀어 모든 쌍 거리 행렬을 피하고, 선택적으로 계획기 혼잡 비용을 반영해 최대 20,000 에이전트·30,000 작업을 1초 예산으로 다뤘다고 보고한 AAMAS 2026 논문(격자 지도 계산 실험). DOI 10.65109/MQIK8423.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
    },
    {
      "id": "ref-1398",
      "org": "Open Robotics (open-rmf/rmf_ros2)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지의 판별 변경 이력. 2.14.0(2026-09-26)에 요청의 플릿 이름이 문자열 또는 배열에 있으면 입찰하도록 한 수정 #534 가 기록되어 있다(ROS 배포판 반영 시점 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/task-allocation-mrta.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? (관련 기존 질문: oq-053, oq-082)",
      "areas": [
        25,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가?",
      "areas": [
        25,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? (관련 기존 질문: oq-030)",
      "areas": [
        25,
        47
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가?",
      "areas": [
        25,
        28
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시",
      "title": "25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시",
      "title": "25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시",
      "title": "25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시",
      "title": "25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시",
      "title": "25. 작업 배정 — MRTA"
    }
  ],
  "standards_updates": [
    {
      "name": "Open-RMF 입찰 제안 메시지(rmf_internal_msgs의 rmf_task_msgs BidProposal)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg",
      "related_areas": [
        25,
        20
      ],
      "summary": "입찰 공고에 답해 플릿 어댑터가 내는 입찰 제안 메시지로, 플릿 이름·예상 수행 로봇·새 작업 수용 전후 전체 배정 비용·예상 완료 시각 다섯 필드를 담는다(2026-10-10 확인).",
      "ref_id": "ref-1453"
    }
  ],
  "additional_research_requests": [
    "6절·8절(문헌 검토 ref-152): 원문이 검토 대상을 고른 절차와 편수(검증 노트상 Google Scholar 1440건 중 52편)는 이번 브리프의 finding 이 아니어서 본문에 넣지 않았다. 다음 25. 작업 배정 — MRTA 실행에서 finding 으로 확인해 달라.",
    "주제 페이지 docs/topics/2026/2026-09-25-area13-s6.md·2026-09-25-area13-s7.md·2026-09-25-area13-s8.md·2026-09-25-area13-s11.md 는 이번 입력에 없어 고치지 못했다. 그 페이지에 남아 있을 수 있는 '문헌 검토 계열·플릿 규모 미확인' 문장, ref-152·ref-168 의 옛 각주(저자 Yu, S., 원문 미열람), LTAA 출처 충돌 서술을 이번 내용과 맞추려면 다음 갱신 실행 입력에 해당 주제 페이지를 넣어 달라.",
    "트랙 반영 제안 16건(data/area_reflection_proposals.json, 최근접 대 MILP 비교 Choe 외 포함)은 이번 브리프의 finding 이 아니어서 반영하지 않고 '제안' 상태로 남겼다. 다음 25. 작업 배정 — MRTA 실행에서 원문 확인과 함께 다뤄 달라.",
    "2절 핵심 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?)에 답할 물류창고·다른 현장 유형의 실측 비교 자료(oq-052)와 국내 자료가 이번에도 없다. 한국어 검색을 포함한 조사가 필요하다.",
    "5절 병원 모사 사례의 작업 대상(물품 종류)과 완료·인계(수령 확인) 조건, 그리고 실제 병원 배송 로봇의 배정 운영 사례가 없어 '미확인'으로 두었다.",
    "pipeline 담당 확인 요청: 자동 분리 코드가 append 패치 뒤 절에서 '자세한 내용은 주제 페이지'로 시작하는 기존 링크 줄을 지워 이전 주제 페이지로 가는 링크가 사라졌다(2차 검증 지적). 이번에는 6·7·8·11절을 replace 로 바꿔 첫 문단 둘째 문장에 이전 주제 페이지 링크를 넣어 우회했다. 분리 코드가 기존 링크 줄을 보존하도록 고치거나 이 규칙을 storyteller.md 에 명시해 달라."
  ],
  "fixes_applied": [
    "f4·f6 판 표기 — 6절과 11절에서 76%·Heavy Excels 77%·전통 기법 모두 우위 서술마다 'arXiv PDF v1 초록 기준'을 밝혔다.",
    "f4~f6 조건 병기 — 6절·11절의 LTAA 수치(75.97%·73%·77%·77.1%·0.77·0.81·0.95)를 담은 모든 문장에 '저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님'을 붙였다.",
    "oq-030 — 11절에서 상태를 열림으로 두고 초록의 Heavy Excels 우위 표현(f6)과 본문의 DP 0.95 비교 제외(f5)를 각각 [사실]로 제시했으며, f7 은 '이 위키의 의견' [의견]으로 충돌 원인 설명으로만 썼다.",
    "의견·추정 주체 표시 — f3·f7·f11·f14·f17·f20·f26 의 [의견] 문장에 '이 위키의 의견', f9·f24 의 [추정] 문장에 '이 위키의 종합'을 밝혔다.",
    "6절 문헌 검토 문장 — 기존 '검토 편수·계열 구분·실험 플릿 규모 미확인' [추정] 문장을 지우고 f1(다섯 계열)·f2(표 I~V 의 열)로 바꿨으며, 플릿 규모는 본문 25대·표 I 45대·표 IV 3~48대만 근거로 들어 한 수치로 요약하지 않았고 검토 편수는 언급하지 않고 추가 조사 요청으로 넘겼다.",
    "f8·f9 — 7절에는 f8 만 [사실]로 두고, 9절·11절의 f9 는 [추정]으로 두며 두 출처가 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님을 문장에 밝혔고 oq-053 은 부분 근거로만 연결했다.",
    "f10·f11 — 6절·9절에서 TaskPlanner 최적 배정이 '한 플릿의 주어진 작업 집합'에 한정된다고 적고, Zhang 외의 단발 배정 최적 서술은 TaskPlanner 의 성질로 쓰지 않았다(f11 은 범위 해석에 관한 의견으로만 9절에 둠).",
    "f12·f14 — 5절 물류창고 표 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인이다' 문장을 그대로 두고, 병원 모사 연구의 마감 필수 제약 정식화([사실], f12)와 창고 출하 마감 연동 사례 미확인([의견], f14)을 덧붙였으며 oq-054 는 열림으로 두었다.",
    "f15~f17 — 5절에 현장 유형 '병원' 사례를 더하고 사례 제목에 '병원 모사 환경의 계산 실험(그래프 추상화 벤치마크)'을 밝혔으며, 시작 조건(f16)·수행 자원(f15)·제약(f12)·예외·성과(f17)만 채우고 작업 대상·완료·인계는 '미확인'으로 두었고 실증·운영 사례로 쓰지 않았다.",
    "site_matrix_updates — 병원 칸 네 항목(시작 조건·수행 자원·제약·예외·성과)을 site_type '병원', link 대상 세부영역 페이지 5절 앵커, title '25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)'으로 냈다.",
    "f13 — 6절·5절·8절에서 건전·완전성을 '논문의 모델·인코딩 가정(사용 솔버의 건전·완전성, D=D_max 조건) 아래의 결과'로 적고 최소 이동 비용 최적해를 보장하지 않는다고 썼으며, 국소 경로 계획·충돌 회피는 하위 계획기(연계 대상) 몫으로 밝혔다.",
    "f18~f24 — 6절에서 배정 비용에 환경 구조·혼잡을 반영하는 부분만 쓰고 경로·충돌·교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 로 링크만 했으며, MRTA-RM 을 교착 없음 보장으로 쓰지 않고(f20) 두 연구 수치를 순위로 비교하지 않았다(f24, 8절에도 명시).",
    "f19·ref-1456 — 8절에서 공개 구현을 '저자 공개 Python 구현(MIT 라이선스), 같은 팀 산출물이라 독립 재현 아님'까지만 쓰고 GVD 구현이라고 쓰지 않았다.",
    "f21~f23 — 8절의 20,000 에이전트·30,000 작업·1초 수치에 '저자 보고, 격자 지도 계산 실험, 실제 로봇 배치 아님'을 병기했고, 6절·8절 어디에도 논문 내부 절 번호를 쓰지 않았다.",
    "f25·f26 — 7절의 rmf_fleet_adapter 2.14.0(2026-09-26) #534 문장에 '패키지 태그 기준, ROS 배포판 반영 시점 미확인'을 병기했다.",
    "용어(f18) — 6절에서 '경로망(roadmap)'으로 쓰고 용어집 roadmap 에 링크했으며, GVD 는 첫 등장 시 '일반화 보로노이 다이어그램(Generalized Voronoi Diagram, GVD)'으로 풀어 쓰고 일반화 보로노이 그래프 용어에 링크하지 않았고, makespan 은 '전체 완료 시간(makespan)'으로 썼다.",
    "용어집 — '최소 비용 흐름(Minimum-Cost Flow)'·'이론 모듈로 만족 가능성(SMT)' 2건을 glossary_updates 에 신규(action: new, 스키마의 신규 값)로 등록했다.",
    "인용 — ref-168 은 페이지 전체에서 직접 인용 없이 모두 재서술했다(0회).",
    "참고문헌 ref-168 — 13절 각주와 reference_updates 를 저자 'Kaitha, S. p. r., & Yu, H.', 발행일 2025-12-02, 접근일 2026-10-10 으로 고치고 '(원문 미열람)'을 뗐다.",
    "참고문헌 ref-152·ref-404 — 13절 각주 접근일을 2026-10-10 으로 고치고 ref-152 의 '(원문 미열람)'을 뗐다.",
    "신규 참고문헌 ref-1453~ref-1398 — 13절에 '기관, 제목, 발행일, URL, 접근일 2026-10-10' 형식으로 각주를 등록하고 ref-1453·ref-1456 은 발행일 '미확인', ref-1457 은 '2026-05'로 썼으며 reference_updates 에도 냈다.",
    "open_questions_new 4건 — open_question_updates 에 new 로 등록하고, 1번에 관련 기존 질문 oq-053·oq-082, 3번에 oq-030 을 표시했으며 기존 질문은 해결로 바꾸지 않았다(11절에도 같은 표시).",
    "트랙 반영 제안 16건 — 이번 브리프의 finding 이 아니므로 본문에 반영하지 않고 '제안' 상태로 남겼으며, additional_research_requests 에 다음 25. 작업 배정 — MRTA 실행에서 처리하도록 적었다.",
    "2차: 이전 주제 페이지 링크 — 7·8·11절 패치를 append 에서 replace 로 바꾸고(6절도 같은 방식으로 정리) 각 절 첫 문단 둘째 문장에 2026-09-25 주제 페이지(2026-09-25-area13-s6·s7·s8·s11)로 가는 링크 문장을 넣었으며, 어느 문장도 '자세한 내용은 주제 페이지'로 시작하지 않는다. 링크는 ../../topics/2026/… 경로라 세부영역 페이지와 분리 주제 페이지 양쪽에서 유효하다. 기존 7절 첫 문장([사실] 주장)은 유지했고, 8절 첫 문단은 2026-09-25 에 고른 고전 연구·시뮬레이션 연구·국내 자료와 2026-10-10 에 더한 2024~2026 연구 3건을 함께 밝혀 요약과 링크 대상이 어긋나지 않게 했으며, 11절 첫 문단도 이전 질문(oq-024·oq-052 등)과 이번 부분 근거·새 질문을 나눠 밝혔다.",
    "2차: 'n절' 상호참조 — 6절('9절에서 다룬다'), 7절('9절에 둔다'), 8절('5절 병원 모사 사례', '6절의 이 위키 종합 참고'), 11절(oq-030·oq-053·oq-054 의 '(6절)'·'(9절)'·'(5절)')을 모두 '세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '<번호. 절 제목>' 절' 형식의 이름 있는 참조로 바꿨다. 링크 경로는 분리 전후 어느 위치에서도 같은 세부영역 페이지를 가리키며, 이번 실행에서 다시 생길 분리 주제 페이지 경로에는 기대지 않았다.",
    "분량 초과 자동 분리: 25. 작업 배정 — MRTA 본문 11,425자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 5,008자"
  ]
}
```

### runs/2026-10-10-02/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/planning-and-optimization/task-allocation-mrta.md (7개 절)
- 분량 초과 자동 분리:
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-10-area25-s6.md (2,917자)
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area25-s11.md (1,653자)
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area25-s8.md (1,232자)
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area25-s7.md (814자)
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-10-area25-s10.md (723자)
    - docs/categories/planning-and-optimization/task-allocation-mrta.md "3. 왜 중요한가" → docs/topics/2026/2026-10-10-area25-s3.md (438자)
```

### runs/2026-10-10-02/pages/categories/planning-and-optimization/task-allocation-mrta.md

```markdown
---
title: "25. 작업 배정 — MRTA"
type: area
category: "G. 계획·최적화"
area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [MRTA, 작업 배정, 시장 기반 배정, 최근접 배정, Open-RMF, LLM 기반 배정]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-006, ref-031, ref-090, ref-105, ref-132, ref-152, ref-168, ref-236, ref-237, ref-376, ref-393, ref-394, ref-398, ref-399, ref-400, ref-402, ref-403, ref-404, ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1398]
last_run: 2026-10-10
version: 3
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

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 왜 중요한가](../../topics/2026/2026-10-10-area25-s3.md)에 있다.

## 4. 핵심 개념과 용어

**MRTA 분류 체계(Gerkey–Matarić taxonomy)** — [다중 로봇 작업 배정(MRTA)](../../glossary/mrta.md)을 단일 작업 로봇(ST)/다중 작업 로봇(MT), 단일 로봇 작업(SR)/다중 로봇 작업(MR), 즉시 배정(IA)/시간 확장 배정(TA)의 세 축으로 나누는 도메인 독립 분류다(2004). [사실][^ref-393]
- **최적 배정 문제(Optimal Assignment Problem)** — ST-SR-IA 유형은 이 문제의 한 사례로, 헝가리안 방법(Hungarian Method) 같은 다항 시간 해법으로 최적해를 구할 수 있다. [사실][^ref-393]

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 핵심 개념과 용어](../../topics/2026/2026-09-25-area13-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-10 갱신에서 병원 모사 환경의 계산 실험 사례를 그 아래에 더했고, 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹한 토트의 운반 작업을 여러 제조사 로봇 가운데 누구에게 맡길지 정하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템(WMS 등)이 피킹 주문을 내려 운반 작업이 생긴다. 주문·납기·재고 정책 자체는 ROP 밖의 연계 대상이다. [추정][^ref-031] |
| 작업 대상 | 피킹한 상품을 담은 토트(설명용 가정) |
| 수행 자원 | 작업자가 피킹하고 AMR(Autonomous Mobile Robot, 자율이동로봇)이 운반하는 협업 설정이 연구되어 있다. [사실][^ref-132] ROP 는 플릿별 입찰을 비교해 작업을 줄 플릿을 고르는 역할을 맡을 수 있다. [추정][^ref-376][^ref-031] |
| 제약 | 배터리가 설정 임계값(Open-RMF 템플릿 예시값 0.10) 아래인 로봇은 작업하지 않도록 해 배정 후보에서 빠진다. [사실][^ref-105] 출하 마감을 배정 목적함수에 넣는 방법은 미확인이다. 병원 모사 환경 연구(2024-03 프리프린트)에는 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 두는 정식화가 있다. [사실][^ref-1454] 이 위키의 의견으로는 마감 준수가 필수인 작업은 우선순위 점수만 높이는 방식과 별도로 마감을 필수 제약으로 두는 정식화를 검토할 만하지만, 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못했다(oq-054). [의견][^ref-1454] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | RMFS 이산 사건 시뮬레이션에서 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398] 최근접 배정이 전체 최적이라는 보장은 없다. [추정][^ref-400] |

다음은 설명을 위한 가상의 시나리오이다. 두 제조사의 AMR 플릿이 같은 피킹 구역을 쓰고, 작업자가 피킹한 토트를 다음 공정으로 옮길 운반 작업이 계속 들어온다. 이 영역이 관여하는 칸은 수행 자원(누구에게 맡길지), 제약(배터리·능력으로 후보 거르기), 예외·성과(배정 규칙이 처리량에 주는 영향)다.

Open-RMF 방식이라면 디스패처가 각 플릿 어댑터에 입찰 공고를 보내고, 처리할 수 있는 플릿이 비용을 담아 입찰하면 가장 빨리 끝나는 것 같은 설정 기준으로 비교해 작업을 준다. [사실][^ref-376] 가장 가까운 로봇을 고르는 규칙은 계산이 가볍지만 뒤이어 들어올 요청을 고려하지 않으므로 전체 이동이나 대기가 늘 수 있다. [추정][^ref-400]

**현장 유형:** 병원

**사례:** 병원과 비슷한 실내 공간에서 계속 들어오는 배송 요청을 적재 용량이 정해진 로봇들에 배정하기 — 병원 모사 환경의 계산 실험(그래프 추상화 벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배송 요청마다 출발·도착 위치와 발생·마감 시각이 있고, 새 요청이 들어오면 이미 실행한 동작과 현재 동작은 그대로 둔 채 계획을 갱신한다(병원 모사 환경의 계산 실험, 2024-03 프리프린트). [사실][^ref-1454] |
| 작업 대상 | 미확인 |
| 수행 자원 | 병원과 비슷한 실내 공간을 그래프(노드는 구역, 가중치는 최악 이동 시간)로 추상화한 다중 로봇 배송 벤치마크 200개에서 로봇 5~20대, 작업 10~30개, 로봇 최대 적재 용량 2 또는 3, 균등 분포의 마감으로 평가했다. [사실][^ref-1454] |
| 제약 | 작업은 엄격한 마감을 지켜야 하고, 로봇마다 동시에 맡을 수 있는 작업 수가 적재 용량으로 제한된다. [사실][^ref-1454] |
| 완료·인계 | 미확인 |
| 예외·성과 | 원문은 그래프 추상화 벤치마크에서의 솔버 성능만 보고하고 실제 병원·로봇 운행 결과는 없으므로, 이 위키의 의견으로는 병원 현장 실증이 아니라 병원 모사 환경의 계산 실험 사례로 분류해야 한다. [의견][^ref-1454] |

이 사례는 실제 병원 도입·운영 사례가 아니라, 병원과 비슷한 공간을 그래프로 추상화한 벤치마크에서 배정 알고리즘을 평가한 계산 실험이다. 이 영역이 관여하는 칸은 시작 조건(요청이 계속 도착할 때의 계획 갱신), 수행 자원(몇 대의 로봇에 어떤 용량으로 맡길지), 제약(마감·용량)이다.

이 연구는 제약을 모두 만족하는 배정 계획을 찾는 것을 목표로 하며 최소 이동 비용의 최적해를 보장하지 않고, 국소 경로 계획·충돌 회피는 하위 계획기(연계 대상)에 맡긴다. [사실][^ref-1454] 작업 대상(물품 종류)과 완료·인계(수령 확인) 조건은 원문에서 확인하지 못해 미확인으로 둔다.

## 6. 대표 접근법과 기술

이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법은 2025-01 문헌 검토에서 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리된다. [사실][^ref-152]

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 접근법과 기술](../../topics/2026/2026-10-10-area25-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준과 오픈소스는 배정을 어느 구성요소의 책임으로 두는지 보여 주며, Open-RMF 는 입찰 기반 배정을 구현하고 VDA 5050 은 배정을 관제의 기능으로만 규정한다. [사실][^ref-376][^ref-031] 2026-09-25 까지 정리한 Open-RMF·VDA 5050 의 세부는 주제 페이지 [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area13-s7.md)에 있다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area25-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 대표 자료로 이 위키는 2026-09-25 에 분류 체계와 시장 기반 방법의 고전 연구, 창고 결정 규칙의 시뮬레이션 연구, 국내 자료를 골랐고(이 위키의 선정), 2026-10-10 갱신에서 2024~2026 배정 연구 3건을 더했다. 2026-09-25 에 고른 자료 목록은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area13-s8.md)에 있다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료](../../topics/2026/2026-10-10-area25-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이종 제조사를 잇는 ROP 는 어느 플릿·로봇에 작업을 줄지의 배정 결정과 기준을 맡고, 플릿 내부 경로·주행은 제조사 관제나 로봇에 맡기는 분담이 가능할 것으로 보인다. [추정][^ref-376][^ref-031]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 주문·납기·재고 제약을 배정의 입력으로 받아 쓰고 결과를 되돌린다. [추정][^ref-031] | 수요예측·전사 재고정책(연계 대상) |
| 로봇 자체 지능·제어 | 플릿·로봇 사이 배정 결정과 기준(비용·완료 시각). [추정][^ref-376][^ref-031] | 플릿 내부 경로·주행, 로컬 회피(제조사 관제·로봇) |

VDA 5050 은 주문 배정을 관제의 기능으로 두지만 배정 알고리즘 자체는 규정하지 않는다. [사실][^ref-031] 두 수준으로 나눈 배정이 전체 최적성을 얼마나 잃는지는 확인하지 못해 11절에 질문으로 둔다.

연계 대상: VDA 5050 은 관제–이동로봇 통신과 무관한 외부 IT 시스템 인터페이스를 범위에서 제외하므로, 배정 입력이 되는 주문·납기·재고 제약은 WMS 등 상위 업무 시스템에서 오고 그 정책은 ROP 밖에 있다. [추정][^ref-031] 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

### 두 수준 배정에서 플릿이 내는 정보 (2026-10-10 갱신)

ROP 가 플릿 단위로 배정하고 제조사 관제가 플릿 안에서 로봇을 고르는 두 수준 배정에서, 플릿이 낼 수 있는 비용·상태 정보의 예로 Open-RMF 입찰 제안은 플릿 이름, 예상 수행 로봇, 새 작업 수용 전·후의 전체 배정 비용, 예상 완료 시각 다섯 필드를 담는다(2026-10-10 확인). [사실][^ref-1453] 플릿 안의 배정을 맡는 Open-RMF 작업 계획기의 최적 배정은 물리·운동 특성을 공유하는 한 플릿의 주어진 작업 집합에 한정된다(2026-10-10 확인). [사실][^ref-404]

이 위키의 종합으로는 입찰이 각 플릿이 자기 안에서 계산한 비용만 전하므로 이것만으로 모든 플릿을 합친 최적 배정이 보장되지는 않을 것으로 보이며, 이종 플릿의 최적성 손실을 수치로 제한하는 근거는 확인하지 못했다(oq-053 부분 근거. 근거 두 건은 같은 Open-RMF 프로젝트 자료라 서로의 독립 교차 확인이 아니다). [추정][^ref-1453][^ref-404] 이 위키의 의견으로는 작업 계획기의 최적 배정을 앞으로 들어올 작업, 다른 제조사 관제의 내부 결정, 실제 혼잡까지 포함한 운영 전체의 최적성으로 넓혀 해석해서는 안 된다. [의견][^ref-404][^ref-1457]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

배정은 로봇 능력 정보를 입력으로 받고 순서·경로·충전 결정과 맞물린다. 교차 규칙(분류 개정 전 원문 8장)에 따라 학습·LLM 기반 배차는 47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결한다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area25-s10.md)에 있다.

## 11. 열린 질문

이 위키의 열린 질문 현황이며, 2026-09-25 까지 올린 질문(oq-024·oq-052 등)의 서술은 주제 페이지 [25. 작업 배정 — MRTA — 열린 질문 (2026-09-25)](../../topics/2026/2026-09-25-area13-s11.md)에 있다. LLM 배정 결과의 출처 충돌과 선언·관측 능력 차이는 아직 풀리지 않았고, 2026-10-10 갱신에서 창고 비교 실측·두 수준 배정·납기 결합 질문 가운데 oq-030·oq-053·oq-054 에 부분 근거를 더하고 새 질문 4건을 올렸다.

자세한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 열린 질문](../../topics/2026/2026-10-10-area25-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [25. 작업 배정 — MRTA](task-allocation-mrta.md) — 섹션 3~11 신규 작성(분류 체계·배정 방식·Open-RMF 입찰·LLM 기반 배정·열린 질문), 트랙 반영 제안 반영, 페이지 상태 마커 추가. 2차 수정: 6·8·10·11절 첫 문장의 표기·태그 정리 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 대표 접근법과 기술](../../topics/2026/2026-09-25-area13-s6.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 내부 용어 '브리프' 삭제, 원 페이지 3절 참조를 링크로 명시 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 대표 연구와 자료](../../topics/2026/2026-09-25-area13-s8.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: '대표 자료' 선정 문장을 이 위키의 선정으로 밝힌 안내 문장으로 고침 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 열린 질문](../../topics/2026/2026-09-25-area13-s11.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 안내 문장의 태그·각주 제거, oq-024 항목의 단정을 [추정] 문장으로 고침 (실행 2026-09-25-33)
- 2026-09-25 · 생성 · [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area13-s7.md) — 자동 분리: 13. 작업 배정 — MRTA 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 대상 아님, 변경 없음) (실행 2026-09-25-33)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-152]: Meseguer Valenzuela, A., & Blanes Noguera, F., Task Allocation in Mobile Robot Fleets: A review, 2025-01, https://arxiv.org/abs/2501.08726, 접근일 2026-10-10
[^ref-393]: Gerkey, B. P., & Matarić, M. J., A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems, 2004-09, https://journals.sagepub.com/doi/10.1177/0278364904045564, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems (arXiv 2018-01 공개, Operations Research Perspectives 2019 게재, 이산 사건 시뮬레이션 조건), 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-400]: International Journal of Planning and Scheduling 게재 논문(저자 미확인), Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors, 2019, https://www.inderscience.com/info/inarticle.php?artid=103016, 접근일 2026-09-25 (원문 미열람)
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10
[^ref-1453]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg, 접근일 2026-10-10
[^ref-1454]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1457]: Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS), Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery, 2026-05, https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf, 접근일 2026-10-10
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

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s6.md

```markdown
---
title: "25. 작업 배정 — MRTA — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-1454, ref-1455, ref-1457, ref-152, ref-168, ref-404]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#6
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 대표 접근법과 기술

# 25. 작업 배정 — MRTA — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법은 2025-01 문헌 검토에서 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리된다. [사실][^ref-152]
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법은 2025-01 문헌 검토에서 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리된다. [사실][^ref-152] 2026-09-25 까지 이 위키가 여섯 갈래(중앙 최적화, 시장 기반 경매·분산 합의, 최근접 규칙, 학습 기반 배차, LLM 기반 배정, 배터리·충전 결합)로 정리한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 접근법과 기술 (2026-09-25)](2026-09-25-area13-s6.md)에 있다.

이 검토의 표 I~V 는 계열별로 각 연구의 방법, 중앙·분산 구조, 구현 환경(프레임워크), 플릿 규모, 주요 결과를 함께 제시한다. [사실][^ref-152] 다만 본문은 휴리스틱 연구의 시뮬레이션을 최대 25대로 설명하는 반면 표 I 에는 최대 45대, 표 IV 에는 3~48대 행이 있어, 이 위키의 의견으로는 검토된 연구의 최대 플릿 규모나 계열 간 우열을 하나의 수치로 요약하지 않는 편이 좋다. [의견][^ref-152]

### 한 플릿 안의 최적 배정

Open-RMF rmf_task README(2026-10-10 확인)는 작업 계획기(TaskPlanner)의 최적 배정을, 물리·운동 특성을 공유하는 한 플릿에 속한 로봇과 주어진 작업 집합에 대해 요청된 시작 시각을 고려해 작업이 가장 짧은 시간에 끝나도록 순서를 정하는 문제로 설명한다. [사실][^ref-404] 즉 이 최적 배정의 범위는 한 플릿의 주어진 작업 집합이며, 여러 제조사 플릿을 합친 배정에서 이 범위가 갖는 의미는 세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)' 절에서 다룬다.

### 마감·용량을 필수 제약으로 두는 배정

Tuck 외(2024-03, NFM 2024 게재 예정 프리프린트)는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 풀이를 써서, 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 표현하고 새 작업을 점진(incremental) 풀이로 배정한다. [사실][^ref-1454] 목표는 주어진 모델에서 제약을 모두 만족하는 계획을 찾는 것이며 최소 이동 비용의 최적해를 보장하지 않는다. 저자들은 알고리즘의 건전성·완전성을 증명했으나 이는 논문의 모델·인코딩 가정(사용 솔버의 건전·완전성, D=D_max 조건) 아래의 결과이고, 국소 경로 계획·충돌 회피는 하위 계획기(연계 대상)에 맡긴다. [사실][^ref-1454]

### 배정 비용에 환경 구조·혼잡 반영

Lee·Sim·Nam 의 MRTA-RM(2025-06 프리프린트)은 장애물이 밀집하고 통로가 좁은 환경에서 일반화 보로노이 다이어그램(Generalized Voronoi Diagram, GVD)으로 [경로망(roadmap)](../../glossary/roadmap.md)을 만들어 여러 구역으로 나눈 뒤, 구역 사이에 로봇을 재분배하고 작업을 배정해 충돌·교착을 줄이면서 전체 완료 시간(makespan)을 줄이려 한다. [사실][^ref-1455] 저자들은 이 방법이 교착 없음을 달성하지는 못하며 교착 가능성이 낮은 배정을 찾는 것이 목표라고 밝히므로, 이 위키의 의견으로는 혼잡을 줄이는 배정의 재현 후보로 볼 수 있지만 임의 환경에서 교착이 없다는 보장으로 소개해서는 안 된다. [의견][^ref-1455]

Zhang 외(AAMAS 2026)는 온라인 [다중 에이전트 픽업·배송](../../glossary/multi-agent-pickup-and-delivery.md)의 작업 배정을 환경 그래프 위의 최소 비용 흐름(Minimum-Cost Flow) 문제로 풀어, 선형 배정 방식이 요구하는 로봇·작업 사이 모든 쌍의 거리 행렬 계산을 피한다. [사실][^ref-1457] 기본 간선 비용은 지도의 간선 비용(격자 지도에서는 단위 비용)이고, 선택할 수 있는 대체 비용 모델로 경로 계획기의 혼잡 추정치나 과거 실행에서 관측한 평균 대기 시간을 배정 비용에 반영할 수 있다. [사실][^ref-1457]

이 위키의 종합으로는 두 연구에서 배정 비용에 환경 구조와 혼잡을 반영하는 흐름이 확인되지만, 환경·규모·지표가 달라 두 방법의 성능 수치를 같은 조건의 순위로 비교할 수는 없는 것으로 보인다. [추정][^ref-1455][^ref-1457] 경로·충돌·교착 처리 자체는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)에서 다루고, 이 영역에서는 배정 비용에 반영하는 부분만 다룬다.

### LLM 기반 배정의 원문 수치

LLM 기반 배정은 교차 규칙에 따라 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)과 함께 본다. 건설 로봇 작업 배정에 대규모 언어 모델(Large Language Model, LLM) 에이전트 LTAA 를 쓴 프리프린트(Kaitha·Yu, 2025-12-02)의 결과 절은 TEACh 데이터셋 건설 작업에서 전체 성공률을 LTAA 75.97%, Q-learning 73%, DQN 77% 로 보고하고, arXiv PDF v1 초록 기준으로는 LTAA 값을 76% 로 반올림해 적는다(저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님). [사실][^ref-168]

같은 원문은 결정적 비교군의 성공률을 brute force 0.77, greedy 0.81, 동적 계획법(Dynamic Programming, DP) 0.95 로 적으면서, 이 결정적 알고리즘들은 불확실성 모델이 없어 비교 그림에서 뺐고 확률적 조건의 직접 비교 기준은 강화학습이라고 설명한다(저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님). [사실][^ref-168] arXiv PDF v1 초록 기준으로는 로봇 전문화가 뚜렷한 Heavy Excels 설정에서 LTAA 가 77% 완료율과 더 나은 작업 부하 균형으로 전통 기법을 모두 앞섰다고 쓰고, 결론은 이 설정의 성공률을 77.1% 로 적는다(저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님). [사실][^ref-168]

이 위키의 의견으로는 원문에 LTAA 전체 75.97%, Heavy Excels 77.1%, DP 0.95 가 모두 있으나(모두 저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님) DP 는 불확실성 모델 차이로 비교에서 빠졌으므로, LTAA 가 전통 배정법 전체보다 낫다는 결론은 지지되지 않고 같은 조건의 LLM 대 DP 우열은 확정할 수 없으며, Heavy Excels 결과와 전체 비교 결과는 나눠 읽어야 한다. [의견][^ref-168]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1454]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1455]: Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293), Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution, 2025-06-08, https://arxiv.org/html/2506.07293, 접근일 2026-10-10
[^ref-1457]: Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS), Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery, 2026-05, https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf, 접근일 2026-10-10
[^ref-152]: Meseguer Valenzuela, A., & Blanes Noguera, F., Task Allocation in Mobile Robot Fleets: A review, 2025-01, https://arxiv.org/abs/2501.08726, 접근일 2026-10-10
[^ref-168]: Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12-02, https://arxiv.org/abs/2512.02810, 접근일 2026-10-10
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s11.md

```markdown
---
title: "25. 작업 배정 — MRTA — 열린 질문"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-1453, ref-1454, ref-168, ref-404]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#11
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 열린 질문

# 25. 작업 배정 — MRTA — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 위키의 열린 질문 현황이며, 2026-09-25 까지 올린 질문(oq-024·oq-052 등)의 서술은 주제 페이지 [25. 작업 배정 — MRTA — 열린 질문 (2026-09-25)](2026-09-25-area13-s11.md)에 있다. LLM 배정 결과의 출처 충돌과 선언·관측 능력 차이는 아직 풀리지 않았고, 2026-10-10 갱신에서 창고 비교 실측·두 수준 배정·납기 결합 질문 가운데 oq-030·oq-053·oq-054 에 부분 근거를 더하고 새 질문 4건을 올렸다.
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 위키의 열린 질문 현황이며, 2026-09-25 까지 올린 질문(oq-024·oq-052 등)의 서술은 주제 페이지 [25. 작업 배정 — MRTA — 열린 질문 (2026-09-25)](2026-09-25-area13-s11.md)에 있다. LLM 배정 결과의 출처 충돌과 선언·관측 능력 차이는 아직 풀리지 않았고, 2026-10-10 갱신에서 창고 비교 실측·두 수준 배정·납기 결합 질문 가운데 oq-030·oq-053·oq-054 에 부분 근거를 더하고 새 질문 4건을 올렸다.

### 기존 질문의 부분 근거 (2026-10-10 갱신)

- **oq-030** (상태: 열림) LTAA 결과의 출처 충돌. arXiv PDF v1 초록 기준으로 LTAA 는 Heavy Excels 설정에서 77% 완료율로 전통 기법을 모두 앞섰다고 적혀 있다(저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님). [사실][^ref-168] 같은 원문 본문은 결정적 비교군인 동적 계획법의 성공률을 0.95 로 적고, 불확실성 모델이 없어 비교 그림에서 뺐다고 설명한다(저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님). [사실][^ref-168] 이 위키의 의견으로는 기존의 두 2차 요약이 각각 초록과 본문을 전한 것으로 보여 충돌은 비교 조건의 차이에서 온 것이지만, 결정적·확률적 비교군을 같은 조건으로 비교한 자료가 원문에 없으므로 이 질문은 열어 둔다(세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '6. 대표 접근법과 기술' 절). [의견][^ref-168]
- **oq-053** (상태: 열림) 두 수준 배정의 최적성 손실. 이 위키의 종합으로는 Open-RMF 입찰 제안의 다섯 필드가 제조사 관제가 내는 비용·상태 정보의 예이지만, 손실을 수치로 제한하는 근거는 아직 없다(세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)' 절). [추정][^ref-1453][^ref-404]
- **oq-054** (상태: 열림) 납기·마감과 배정의 결합. 이 위키의 의견으로는 마감을 필수 제약으로 두는 SMT 정식화가 병원 모사 연구에 있으나 출하 마감을 배정에 연동한 창고 사례는 확인하지 못했으므로 질문을 열어 둔다(세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '5. 적용 사례 (현장 유형 명시)' 절). [의견][^ref-1454]

### 새 질문 (2026-10-10)

- (새 질문 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-02) 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? (관련 기존 질문: oq-053, oq-082)
- (새 질문 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-02) 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가?
- (새 질문 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-02) LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? (관련 기존 질문: oq-030)
- (새 질문 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-02) 최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1453]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg, 접근일 2026-10-10
[^ref-1454]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-168]: Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12-02, https://arxiv.org/abs/2512.02810, 접근일 2026-10-10
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s8.md

```markdown
---
title: "25. 작업 배정 — MRTA — 대표 연구와 자료"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-1454, ref-1455, ref-1456, ref-1457]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#8
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 대표 연구와 자료

# 25. 작업 배정 — MRTA — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 대표 자료로 이 위키는 2026-09-25 에 분류 체계와 시장 기반 방법의 고전 연구, 창고 결정 규칙의 시뮬레이션 연구, 국내 자료를 골랐고(이 위키의 선정), 2026-10-10 갱신에서 2024~2026 배정 연구 3건을 더했다. 2026-09-25 에 고른 자료 목록은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료 (2026-09-25)](2026-09-25-area13-s8.md)에 있다.
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 대표 자료로 이 위키는 2026-09-25 에 분류 체계와 시장 기반 방법의 고전 연구, 창고 결정 규칙의 시뮬레이션 연구, 국내 자료를 골랐고(이 위키의 선정), 2026-10-10 갱신에서 2024~2026 배정 연구 3건을 더했다. 2026-09-25 에 고른 자료 목록은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료 (2026-09-25)](2026-09-25-area13-s8.md)에 있다.

### 2024~2026 배정 연구 (2026-10-10 갱신)

- Tuck 외, SMT-Based Dynamic Multi-Robot Task Allocation(2024-03, NFM 2024 게재 예정 프리프린트) — 마감·용량을 필수 제약으로 두고 온라인으로 도착하는 작업을 점진 풀이로 배정하며, 병원과 비슷한 공간을 그래프로 추상화한 다중 로봇 배송 벤치마크로 평가했다(세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '5. 적용 사례 (현장 유형 명시)' 절의 병원 모사 사례). [사실][^ref-1454] 건전·완전성 증명은 논문의 모델·인코딩 가정 아래의 결과이며 최소 이동 비용의 최적해를 보장하지 않는다. [사실][^ref-1454]
- Lee·Sim·Nam, Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution(MRTA-RM, 2025-06 프리프린트) — 저자들은 수백 대 규모 로봇의 동적 시뮬레이션에서 무작위 시나리오 성공률 96% 초과, 분리 시나리오 58~100% 를 보고했고(저자 보고, 시뮬레이션 조건), 결론에서 경로 추종 제어기 구현으로 성공률 100% 를 달성하는 것과 이종 로봇 팀 확장을 후속 과제로 남겼다. [사실][^ref-1455] 저자 공개 Python 구현(MIT 라이선스)이 있으나 같은 팀 산출물이라 독립 재현이 아니다. [사실][^ref-1456]
- Zhang 외, Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery(AAMAS 2026, 2026-05) — 최소 비용 흐름 기반 배정으로, 창고형 Sortation Large 를 포함한 격자 지도 벤치마크에서 1초 계획 예산으로 최대 20,000 에이전트와 30,000 작업까지 다뤘다고 보고한다(저자 보고, 격자 지도 계산 실험, 실제 로봇 배치 아님). [사실][^ref-1457]
- 두 대규모 배정 연구의 수치는 환경·규모·지표가 달라 순위로 비교하지 않는다(세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '6. 대표 접근법과 기술' 절에 둔 이 위키의 종합 참고).

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1454]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1455]: Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293), Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution, 2025-06-08, https://arxiv.org/html/2506.07293, 접근일 2026-10-10
[^ref-1456]: Lee, S. 외 (SeBin-Lee-SG GitHub), MRTA-RM_public — README, 미확인, https://github.com/SeBin-Lee-SG/MRTA-RM_public, 접근일 2026-10-10
[^ref-1457]: Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS), Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery, 2026-05, https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s7.md

```markdown
---
title: "25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-1453, ref-1398, ref-376]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#7
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스

# 25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준과 오픈소스는 배정을 어느 구성요소의 책임으로 두는지 보여 주며, Open-RMF 는 입찰 기반 배정을 구현하고 VDA 5050 은 배정을 관제의 기능으로만 규정한다. [사실][^ref-376][^ref-031] 2026-09-25 까지 정리한 Open-RMF·VDA 5050 의 세부는 주제 페이지 [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스 (2026-09-25)](2026-09-25-area13-s7.md)에 있다.
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준과 오픈소스는 배정을 어느 구성요소의 책임으로 두는지 보여 주며, Open-RMF 는 입찰 기반 배정을 구현하고 VDA 5050 은 배정을 관제의 기능으로만 규정한다. [사실][^ref-376][^ref-031] 2026-09-25 까지 정리한 Open-RMF·VDA 5050 의 세부는 주제 페이지 [25. 작업 배정 — MRTA — 관련 표준·프레임워크·오픈소스 (2026-09-25)](2026-09-25-area13-s7.md)에 있다.

### Open-RMF 입찰 제안 메시지와 플릿 이름 필터 (2026-10-10 갱신)

Open-RMF 의 입찰 제안 메시지 BidProposal 은 입찰 공고(BidNotice)에 답해 플릿 어댑터가 내는 것으로, 플릿 이름(fleet_name), 작업을 수행할 것으로 예상되는 로봇 이름(expected_robot_name), 새 작업 수용 전·후의 전체 배정 비용(prev_cost·new_cost), 새 작업의 예상 완료 시각(finish_time) 다섯 필드를 담는다(발행일 미확인, 2026-10-10 확인). [사실][^ref-1453] 두 수준 배정에서 이 필드들이 갖는 의미와 한계는 세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)' 절에 둔다.

Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 작업 요청에 지정된 플릿 이름이 문자열 또는 배열에 포함되기만 하면 입찰하도록 한 수정(#534)을 기록한다(패키지 태그 기준, ROS 배포판 반영 시점 미확인). [사실][^ref-1398] 이 위키의 의견으로는 요청에서 후보 플릿을 제한하는 배정 사례를 적을 때 이 수정이 포함된 패키지 버전(2.14.0 이상)을 함께 적는 편이 좋으며, 이 변경이 모든 ROS 배포판에 자동 반영되었다는 뜻은 아니다. [의견][^ref-1398]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1453]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg, 접근일 2026-10-10
[^ref-1398]: Open Robotics (open-rmf/rmf_ros2), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s10.md

```markdown
---
title: "25. 작업 배정 — MRTA — 다른 연구영역과의 연결"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-006, ref-031, ref-090, ref-105, ref-168, ref-236, ref-237, ref-376, ref-394, ref-398, ref-399, ref-402, ref-403, ref-404]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#10
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 다른 연구영역과의 연결

# 25. 작업 배정 — MRTA — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 배정은 로봇 능력 정보를 입력으로 받고 순서·경로·충전 결정과 맞물린다. 교차 규칙(분류 개정 전 원문 8장)에 따라 학습·LLM 기반 배차는 47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결한다.
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

배정은 로봇 능력 정보를 입력으로 받고 순서·경로·충전 결정과 맞물린다. 교차 규칙(분류 개정 전 원문 8장)에 따라 학습·LLM 기반 배차는 47. AI·학습·적응과 모델 운영과 이 영역 양쪽에 연결한다.

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026). [사실][^ref-236][^ref-237]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — Open-RMF 플릿 어댑터 입찰과 VDA 5050 관제 기능이 배정의 인터페이스가 된다. [사실][^ref-376][^ref-031]
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 작업 간 의존(ID·XD)과 rmf_task 의 배정·순서 동시 결정이 두 영역을 잇는다. [사실][^ref-394][^ref-404]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — MAPD 토큰 패싱은 작업 선택과 충돌 없는 경로 계획을 함께 다룬다. [사실][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 배터리 임계값·충전 작업 삽입·충전기 조율이 배정 후보와 일정에 들어간다. [사실][^ref-105][^ref-404][^ref-403]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — RMFS·자동물류센터 시뮬레이션은 배정 규칙을 가정한 미래에서 실험하는 도구다. [사실][^ref-398][^ref-402]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 학습 기반 배차(ScheduleNet)와 LLM 기반 배정은 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것이다. [사실][^ref-399][^ref-090][^ref-168]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 배정 입력인 주문·납기 제약이 상위 업무 시스템에서 온다. [추정][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12-02, https://arxiv.org/abs/2512.02810, 접근일 2026-10-10
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-394]: Korsah, G. A., Stentz, A., & Dias, M. B., A comprehensive taxonomy for multi-robot task allocation, 2013, https://journals.sagepub.com/doi/10.1177/0278364913496484, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems (arXiv 2018-01 공개, Operations Research Perspectives 2019 게재, 이산 사건 시뮬레이션 조건), 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-404]: Open Robotics (open-rmf), rmf_task — README, 미확인, https://github.com/open-rmf/rmf_task, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-10-02/pages/topics/2026/2026-10-10-area25-s3.md

```markdown
---
title: "25. 작업 배정 — MRTA — 왜 중요한가"
type: topic
category: "G. 계획·최적화"
primary_area_no: 25
related_areas: [5, 20, 23, 26, 27, 28, 34, 47]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-006, ref-398, ref-400, ref-402]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/task-allocation-mrta.md#3
---

[홈](../../index.md) › [주제](../index.md) › 25. 작업 배정 — MRTA — 왜 중요한가

# 25. 작업 배정 — MRTA — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [로봇 이동형 풀필먼트 시스템(RMFS)](../../glossary/robotic-mobile-fulfillment-system.md)의 이산 사건 시뮬레이션에서 피킹 주문을 작업대에 배정하는 규칙은 단위 처리량을 크게 바꾸었다고 보고됐다. [사실][^ref-398] 배정은 개별 로봇의 문제가 아니라 창고 전체 처리량의 문제가 될 수 있다. [추정][^ref-398]
- 이 페이지는 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

[로봇 이동형 풀필먼트 시스템(RMFS)](../../glossary/robotic-mobile-fulfillment-system.md)의 이산 사건 시뮬레이션에서 피킹 주문을 작업대에 배정하는 규칙은 단위 처리량을 크게 바꾸었다고 보고됐다. [사실][^ref-398] 배정은 개별 로봇의 문제가 아니라 창고 전체 처리량의 문제가 될 수 있다. [추정][^ref-398]

2절의 질문처럼 가장 가까운 로봇에 맡기는 최근접 배정은 단순해서 다중 에이전트 픽업·배송 알고리즘과 국내 자동물류센터 시뮬레이션에서 기본 규칙으로 쓰였다. [사실][^ref-006][^ref-402] 그러나 작업장(shop floor) 사례 연구에서 앞으로의 운반 요청을 고려한 조합 최적화 배차가 무작위·최근접 규칙보다 작업 대기 시간을 더 잘 통제했다고 저자가 보고했다(2019). [사실][^ref-400]

두 결과를 함께 보면 최근접 배정이 전체 최적이라는 보장은 없다. 다만 근거는 작업장 사례 연구(지표: 작업 대기 시간)와 시뮬레이션뿐이며, 창고 현장에서 둘을 직접 비교한 실측 자료는 이번 조사에서 찾지 못했다. [추정][^ref-006][^ref-400][^ref-402][^ref-398]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/task-allocation-mrta.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/task-allocation-mrta.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems (arXiv 2018-01 공개, Operations Research Perspectives 2019 게재, 이산 사건 시뮬레이션 조건), 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-400]: International Journal of Planning and Scheduling 게재 논문(저자 미확인), Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors, 2019, https://www.inderscience.com/info/inarticle.php?artid=103016, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-02 | 25. 작업 배정 — MRTA 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 29건 / 전체 1401건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [25] 에 걸린 13건 / 전체 350건)

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

### runs/2026-10-10-02/verification2.json

```json
{
  "run_id": "2026-10-10-02",
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
    "overlaps": [
      "새 주제 페이지 2026-10-10-area25-s6 은 이전 주제 페이지 2026-09-25-area13-s6 으로 링크한다. 스토리텔러가 additional_research_requests 에 적은 대로, 이전 페이지에는 '문헌 검토 계열·플릿 규모 미확인' 문장과 ref-168 의 옛 각주(Yu, S., 원문 미열람)가 남아 있을 수 있다. 이번 입력에 없는 페이지라 고치라고 지시하지 않았고, 다음 갱신 실행에서 맞춘다.",
      "f8 은 기존 ref-376 의 입찰 문장과, f10 은 기존 ref-404 의 배정·충전 삽입 문장과 겹친다. 기존 문장과 각주를 유지하고 세부만 더한 것을 확인했다."
    ]
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
    "7·8·11절(append 패치)과 자동 분리 주제 페이지 2026-10-10-area25-s7·s8·s11: 기존 절에 있던 이전 주제 페이지 링크(2026-09-25-area13-s7.md·2026-09-25-area13-s8.md·2026-09-25-area13-s11.md)가 분리 뒤에 사라졌다. 세 절의 패치 내용에 이전 주제 페이지로 가는 링크 문장을 넣는다(예: '2026-09-25 까지 정리한 내용은 주제 페이지 [25. 작업 배정 — MRTA — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area13-s8.md)에 있다.'). 6절 패치는 이 링크를 남겨 두었다. 이유: 지금은 세부영역 페이지에서 이미 게시·검증된 이전 내용(고전 연구 목록, Open-RMF·VDA 5050 세부, oq-024·oq-052 등의 열린 질문 서술)에 닿을 수 없다. 또 8절 요약('분류 체계와 시장 기반 방법의 고전 연구, … 국내 자료를 … 골랐다')이 링크된 s8 주제 페이지의 내용(2024~2026 연구만 있음)과 맞지 않는다. 문장을 줄머리 '자세한 내용은 주제 페이지'로 시작하지 않는다. 자동 분리 코드가 그런 줄을 지운 것으로 보이며, pipeline 담당의 확인이 필요하다.",
    "분리되는 절 안의 'n절' 상호참조: 분리 뒤 주제 페이지에서는 'n절'이 그 주제 페이지 자신의 절(5. ROP 관점의 시사점, 6. 연결되는 연구영역, 9. 검증 노트)을 가리키게 되어 독자가 잘못 읽는다. 해당하는 곳은 6절 패치('9절에서 다룬다'), 7절 패치('9절에 둔다'), 8절 패치('5절 병원 모사 사례', '6절의 이 위키 종합 참고'), 11절 패치(oq-030·oq-053·oq-054 항목의 '(6절)'·'(9절)'·'(5절)')다. 'n절'을 '세부영역 페이지 25. 작업 배정 — MRTA 의 9. ROP가 직접 맡는 것과 외부와 연계하는 것 절', '주제 페이지 25. 작업 배정 — MRTA — 대표 접근법과 기술'처럼 이름을 밝힌 참조로 바꾼다. 링크를 넣을 때는 분리 뒤에도 유효한 경로로 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 26건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: 없음(검증자는 arXiv PDF 2건을 텍스트 추출 서비스로 열었다. AAMAS 2026 PDF(ref-1457)는 텍스트를 추출하지 못해 같은 논문의 arXiv 판 2508.05890v1 과 IFAAMAS 목록 검색 결과로 대조했다). 주의: 모든 [사실] 주장이 단일 출처다. LTAA·MRTA-RM·Zhang 외·Tuck 외의 수치는 저자가 보고한 시뮬레이션·계산 실험 값이며 현장 실측이 아니다. 병원 사례(Tuck 외)는 병원 모사 그래프 벤치마크다. BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 서로 독립 확인이 아니다. LTAA 초록은 판에 따라 표현이 다르다(PDF v1 초록: 76%·'exceeding', arXiv 초록 페이지: 76% 없음·'outperforming'). 열린 질문 oq-030·oq-053·oq-054 는 부분 근거만 더했고 해결로 인정하지 않았다. 정정 요청 없음. 2차: 드리프트 없음. 1차 수정 지시 23건이 모두 이행됐다: 판 표기, 실험 조건 병기, 의견·추정 주체 표시, 병원 모사 사례의 여섯 항목과 미확인 칸, 건전·완전성의 가정 병기, 용어(경로망·GVD·전체 완료 시간) 통일, ref-168 직접 인용 0회, 참고문헌 정정. [분류원문]·[옛 분류원문] 줄은 보존됐고 섹션 순서를 지켰으며 auto 마커는 그대로다. 남은 문제는 두 가지다. 첫째, 7·8·11절이 자동 분리되면서 이전 주제 페이지(2026-09-25-area13-s7·s8·s11)로 가는 링크가 빠져, 이미 게시된 내용에 세부영역 페이지에서 닿을 수 없다. 8절 요약도 링크 대상의 내용과 맞지 않는다. 둘째, 분리된 주제 페이지 안의 'n절' 참조가 주제 페이지 자신의 절을 가리키게 됐다. 참고: 세부영역 페이지 프런트매터 sources 에는 본문 각주에 없는 ref-006·ref-090·ref-1455·ref-1456·ref-1398 등이 남아 있다. 이는 자동 분리로 각주가 주제 페이지로 옮겨 간 결과로 보인다. 이전 주제 페이지 area13-s6 의 옛 서술·옛 ref-168 각주는 다음 갱신 실행에서 맞춰야 한다.",
  "retry_reason": null
}
```
