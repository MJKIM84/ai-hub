(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-04
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 27. 다중 로봇 경로·교통 관리 — MAPF (G. 계획·최적화)
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

### runs/2026-10-10-04/target.json

```json
{
  "run_id": "2026-10-10-04",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 164,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 27,
    "area_name": "27. 다중 로봇 경로·교통 관리 — MAPF",
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
  "selection_rationale": "CLI 지정 run_type=update, area=27"
}
```

### runs/2026-10-10-04/research.json

```json
{
  "run_id": "2026-10-10-04",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 27,
    "area_name": "27. 다중 로봇 경로·교통 관리 — MAPF",
    "category": "G. 계획·최적화"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 설명용 가정 시나리오뿐이며 확인된 다른 현장 유형(제조 공장 등) 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 첫 문장이 단일 로봇 계획인 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶음. PIBT의 '완전·최적 아님' 명시와 마감을 목적으로 하는 정식화(MAPF-DL) 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 은 main 판 기준(2026-09-25 확인)이며 3.0.0 태그의 예정 경로 공유(§6.8)·구역 요청 통신(§6.4.3) 미반영. Open-RMF 2026-09-25 이후 변경(신호등 수준 연동 수정) 미반영",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — SILLM 이 '2024, 프리프린트'로 적혀 있고 계산 규모(10,000)와 실물 검증 규모, WPPL 비교 조건이 구분돼 있지 않음. 실행 조건을 평가한 LSMART 미수록. ref-189·ref-192·ref-195·ref-199 원문 미열람",
    "섹션 11. 열린 질문 — oq-058·oq-059 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]",
    "SIPP·PIBT의 이론 보장(완전성·최적성·도달성)은 어떤 문제 설정과 그래프 조건에서 성립하며, 다중 로봇 현장 경로망에 그대로 옮길 수 있는가? (섹션 6 겨냥)",
    "좁은 통로와 이종 대형 AGV가 있는 산업 현장에 MAPF 기반 교통 관리를 적용한 공개 사례는 현장 유형·평가 방식·교착 처리를 어떻게 밝히는가? (섹션 5·6 겨냥)",
    "VDA 5050 3.0.0 과 Open-RMF 의 최신 판은 교통 관리에 쓰이는 어떤 정보(예정 경로·구역 요청·신호등 수준 연동)를 바꾸거나 더했는가? (섹션 7 겨냥)",
    "oq-058 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (섹션 8·11 겨냥)",
    "oq-059 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? (섹션 6·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Phillips·Likhachev(ICRA 2011)의 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 동적 장애물마다 예측 궤적(predicted trajectories)이 주어졌다고 보고, 상태를 위치와 안전 구간의 쌍으로 묶어 로봇 한 대의 경로를 찾으며, 시간 차원을 더한 계획과 같은 최적성·완전성 보장을 준다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-195"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§I: 동적 장애물이 가까운 미래에 어디로 갈지 예측(predicted trajectory)해야 한다는 전제. §III Notations and Assumptions: 반경과 궤적(시각별 위치 목록)을 가진 동적 장애물 목록이 주어짐. 초록: \"the same optimality and completeness guarantees as planning with time as an additional dimension\". §III 정리 1~2에서 완전성·최적성 증명 개요. 저자 연구실 PDF 열람",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "SIPP의 완전성·최적성은 주어진 장애물 궤적에 대해 로봇 한 대의 시간 최소 경로를 찾는 범위의 결과이므로, 여러 로봇의 경로를 함께 정하는 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF) 전체의 최적성 보장으로 옮길 수 없는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-195",
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "SIPP §II: 주어진 장애물 궤적 전체에 대해 최적이며 비용은 그 로봇의 도착 시간. SIPP 논문은 다중 로봇 전체 최적성을 직접 다루지 않음. Bonetti 외 §2.1은 SIPP를 결합한 우선순위 기반 다중 로봇 계획기에 전역 최적성 보장이 없다고 평가(f3). 두 출처에서 도출",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Bonetti 외(2026)의 관련 연구 절은 Yan·Li(2024)가 우선순위 기반 탐색(Priority Based Search, PBS)·SIPP·베지에 곡선 최적화를 결합한 3단 다중 로봇 계획기를 우선순위 탐색에 기대므로 전역 최적성을 보장하지 않는다고 평가해, SIPP가 상위 다중 로봇 조율 아래의 저수준 계획으로 쓰이는 예를 보여 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2.1 Related Works: Yan and Li (2024)의 three-level MAPF-based motion planner(PBS + SIPP + Bézier 최적화)는 \"does not provide any global optimality guarantees\". Kasaura 외(2022)의 우선순위 SIPP(PSIPP/CTCs)도 최적성 보장이 없다고 설명",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "기존 6절 첫 문장처럼 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶기보다, SIPP는 다른 로봇의 예정 궤적 같은 동적 장애물을 피하는 단일 로봇 저수준 경로 탐색으로 분리해 소개하는 편이 정확하다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-195",
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1(SIPP 문제 설정: 로봇 한 대·주어진 예측 궤적)과 f3(다중 로봇 계획기 안 저수준 계층으로 쓰인 예)에서 도출한 서술 권고. 대상 문장: 6절·s6 첫 문장 'MAPF 해법은 최적해를 보장하는 탐색(CBS·SIPP)부터…'",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Okumura 외의 우선순위 상속과 되돌리기(Priority Inheritance with Backtracking, PIBT) 논문(arXiv v5 2022-06-27, Artificial Intelligence 2022 게재판, 초판 IJCAI-19)은 §2.1에서 PIBT가 MAPF에 대해 완전하지도 최적이지도 않다고 명시하고, 도달성은 모든 에이전트가 동시에 목표에 있음을 보장하지 않으므로 일반 MAPF에는 불완전하다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-189"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2.1: \"PIBT, is neither complete nor optimal for MAPF\". §1: 도달성(reachability)은 동시 목표 도달을 보장하지 않아 일반 MAPF에 불완전하나 지속형 배송(MAPD)에는 완전성을 확보한다고 설명. DOI 10.1016/j.artint.2022.103752. 그래프 조건(인접 정점 쌍의 단순 순환)은 기존 s6 에 있어 이번에 다시 싣지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Bonetti 외 §9는 작업 갱신 같은 예측 못 한 사건과, 시간 지평이 부족해 복도 밖 구역의 시공간 충돌을 다 풀지 못할 때 교착이 생긴다고 보고, AGV 사이 선행 관계 그래프로 순환·비순환(중첩) 교착을 탐지한 뒤 관련 AGV의 경로를 갱신해 해소하는 별도 모듈을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§9 Deadlock Detector and Handler: 교착 원인 (1) task updates 등 예측 못 한 사건 (2) bounded horizon 부족. Pratissoli 외(2023)의 분류로 cyclic·acyclic 교착을 나누고 precedence graph 로 탐지, 관련 AGV 경로 갱신으로 해소(그림 8)",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f7",
      "claim": "PIBT의 도달 보장은 그래프 조건과 지속형 설정을 전제로 하므로, 막다른 통로가 있는 실제 경로망에는 그 보장을 그대로 적용하지 말고 후퇴 공간과 별도 교착 탐지·해소 장치(f6)를 함께 확인해야 한다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-189",
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "PIBT 정리 1의 그래프 조건(인접 정점 쌍마다 단순 순환)과 §2.1의 불완전성 명시(f5), Bonetti 외 그림 10·11의 막다른 좁은 복도(magenta)와 §9 교착 처리(f6)에서 도출한 설계 권고",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Bonetti 외의 교통 관리 연구(The International Journal of Robotics Research 2026 게재, DOI 10.1177/02783649261470035; arXiv 2609.10400, 2026-09-09)는 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발했으며, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 소·중·대 규모 세 배치에서 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§10: developed in collaboration with Gruppo TecnoFerrari S.p.A. §10.1: \"three realistic layouts that simulate a palletizing, storage, and pallet-wrapping plant located at the end of a production line\". 경로망·배치는 업체 제공. 저자 Guidetti 는 업체 소속. arXiv 초록 페이지에 저널 게재·DOI 표시",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Bonetti 외의 배치 1에서 AGV는 팔레타이저에서 포장기로 팔레트를 나르고 포장기가 바쁘거나 쓸 수 없으면 임시 보관 구역으로 돌리며, 빈 팔레트를 디스펜서에서 받아 팔레타이저에 보충한다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§10.1 배치 1 설명: palletizers → wrapping machine, 포장기 점유 시 temporary storage, 빈 팔레트는 dispenser 에서 공급. 배치 2도 팔레타이저 → 포장기, 불가 시 창고 구역, 빈 팔레트 디스펜서 2대",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "작업 대상"
    },
    {
      "id": "f10",
      "claim": "Bonetti 외의 배치 1은 같은 등급 AGV가 복도 4개를 포함한 8개 구역의 좁은 비정형 공간을, 배치 2는 두 등급의 이종 AGV가 고밀도 중형 공간을, 배치 3은 이종 AGV가 좁은 양방향 복도가 없는 넓은 공간을 다니며, 그림 10·11은 막다른 좁은 복도를 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§10.1: 배치 1 homogeneous AGV, 8 sectors including 4 corridors. 배치 2 heterogeneous 두 등급, 7 sectors including 4 corridors. 배치 3은 넓고 덜 제약된 환경(§10.2.3: 좁은 양방향 복도 없음). 그림 10·11 캡션: magenta = dead-end (narrow) corridors",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "Bonetti 외의 시스템은 NURBS 곡선 경로망 위 지속형 MAPF(L-MAPF) 조율기(수정 Bounded Horizon CBS를 순환 지평 충돌 해소에 넣고 복도 구간에 시간 지평을 늘림), 조율된 궤적을 실행 중 안전하게 할당하는 경로 할당기(§8), 교착 탐지·처리기(§9)를 결합하고 업체의 AGV 관제 소프트웨어(TecnoFerrari Supervisor)에 C#으로 통합됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: L-MAPF on NURBS roadmaps, modified Bounded Horizon CBS within Rolling Horizon Conflict Resolution, extended time horizon in corridors. §4 구조, §8 Path Allocator, §9 Deadlock Detector and Handler. §10.1: implemented in C#, integrated into the TecnoFerrari Supervisor software",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "Bonetti 외 논문의 공장 실험 사진은 자동화 공장에서 찍은 그림 9 한 장이고 그림 10–12는 TecnoFerrari Supervisor 소프트웨어의 2D 재구성 화면이며, 성과 지표는 Supervisor 안에서 연속 작업 배정으로 시나리오당 약 10시간 실행하며 수집했다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§10.1: 실험은 \"validated in a real industrial environment in collaboration with the company (see Fig. 9)\". 그림 9 캡션: 자동화 공장 실험 사진. 그림 10–12 캡션: 2D reconstruction of the plant. KPI 는 Supervisor 실행 중 수집, 시나리오당 약 10시간",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Bonetti 외는 업체가 배치한 규칙 기반 교통 관리, Pratissoli 외(2023)의 산업용 방법, PBS로 바꾼 L-MAPF 변형과 비교해 처리량이 최대 약 11% 높았다고 보고하며, 배치 2에서는 규칙 기반 대비 약 11%, PBS 변형 대비 약 10%, Pratissoli 외 대비 약 7%였다.",
      "tag": "사실",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록·§11: improvements of up to 11%. §10.2.4 Comparative Evaluation: 배치 1 규칙 기반 대비 약 10%·Pratissoli 대비 7%·PBS 대비 6%, 배치 2 약 11%·7%·10%. 저자 보고 수치",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "Bonetti 외의 배치별 수치는 업체가 제공한 실제 배치를 모사한 실행 결과로 제시되고 실제 운행은 사진 한 장으로만 보이며 업체 소속 공동저자가 있고 독립 재현은 확인하지 못했으므로, 처리량 최대 11%를 상용 공장 실측 개선율이나 다른 현장의 일반 개선율로 옮기지 않아야 한다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-192"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8·f12·f13에서 도출. 원문은 세 배치를 공장을 모사한(simulate) 현실적 배치로 설명하면서 실제 산업 환경에서 검증했다고도 적어, 배치별 계산·모사 결과와 실제 운행 결과를 나눈 수치는 확인 못 함",
      "as_of": "2026-10-10",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "Ma 외의 마감이 있는 다중 에이전트 경로 찾기(MAPF with Deadlines, MAPF-DL, IJCAI 2018, pp.417–423)는 공통 마감 시점에 자기 목표 정점을 점유한 에이전트를 성공으로 보고 충돌 없는 성공 에이전트 수를 최대화하는 문제로 정식화하며, 최적 풀이가 NP-hard임을 보이고 흐름 문제 환원 정수 계획법과 탐색 기반 해법을 낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1514"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2: 에이전트 ai 는 \"successful iff it occupies its goal vertex at the deadline Tend\". 목적은 성공 에이전트 수 Msucc 최대화(실패 수 최소화). NP-hard 증명, §3 CBS-DL 등 탐색 해법과 흐름 환원 ILP. 학회 공식 PDF",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "MAPF-DL의 목적함수는 도착 시각 합이나 전체 완료 시각(makespan)을 줄이는 일반 MAPF 목적과 달리 마감 안 성공 대수를 최대화하는, 교통 계획에 마감을 넣는 공개 정식화의 예다.",
      "tag": "사실",
      "source_ids": [
        "ref-1514"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§1: 일반 MAPF 목적은 도착 시각 합 또는 makespan 최소화. 기존 일반화는 마감 충족을 직접 다루지 않으며 G-TAPF 도 마감 안 완료 대수를 직접 최대화하지 않는다고 설명",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "MAPF-DL은 모든 에이전트에 공통 마감 하나를 두므로, 작업별로 다른 출하 마감이나 업무 중요도를 이종 플릿의 통로 양보 규칙으로 바꾸는 산업 기준으로 볼 수는 없다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1514",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "MAPF-DL §2 정의(공통 마감 Tend 하나, 성공 대수 최대화)와 VDA 5050 3.0.0 §2 Scope(교통 관리 로직의 우선순위·교착 해소 제외)에서 도출",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "VDA 5050 3.0.0 §6.8은 자유 주행 이동 로봇이 상태(state) 메시지로 관제에 예정 궤적을 알리게 하며, 주문 안의 긴 경로 plannedPath(NURBS, 최소한 현재 베이스를 포함하고 지날 nodeId 를 담을 수 있음)와 센서로 볼 수 있는 가까운 경유점별 예상 도착 시각(ETA)을 담은 폴리라인 intermediatePath를 매 상태 메시지마다 공유하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.8 Sharing of planned paths for freely navigating mobile robots: 두 경로 모두 로봇의 현재 위치에서 시작하고 길이는 로봇이 정함. 더 높은 빈도는 visualization 토픽. 두 필드는 로봇이 스스로 계획한 궤적에만 쓰고 edgeState 의 trajectory 는 미리 정한 궤적의 확인용. 3.0.0 태그 명세 원문 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "VDA 5050 3.0.0 §6.4.3은 로봇이 협조 재계획(COORDINATED_REPLANNING) 구역에 들어가거나 구역 안에서 경로를 바꿀 때 zoneRequest 의 requestType 을 REPLANNING 으로 하고 예정 경로를 NURBS 궤적으로 실어 요청하게 하며, 응답을 제때 받지 못하면 구역에 들어가지 않게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.4.3 Communication for interactive zones: 해제 구역은 ACCESS, 협조 재계획 구역은 REPLANNING 요청, 같은 구역에 서로 다른 궤적으로 여러 요청 가능, 응답은 responses 토픽. 구역 4종 표와 §2 범위 제외는 기존 s7 에 있어 다시 싣지 않음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "VDA 5050 3.0.0은 §2 Scope에서 경로·우선순위·혼잡·교착 해소 같은 교통 관리 로직을 다루지 않으므로, 예정 경로 공유·구역 요청 메시지의 상호운용성과 그 정보를 쓰는 현장 교통 최적화의 성능은 따로 검토해야 한다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "§2 Scope 'Traffic Management Logic' 제외(기존 s7 에 같은 사실 있음)와 §6.8·§6.4.3(f18·f19)에서 도출한 검토 권고",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 EasyTrafficLight의 플릿 상태 발행 수정(#525)과 EasyTrafficLight 누적 지연 계산 수정(#524)을 기록한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1513"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "태그 2.14.0 CHANGELOG.rst: 'Fix EasyTrafficLight publish fleet state (#525)', 'Fix cumulative delay calculation in EasyTrafficLight (#524)'. 같은 판에 #558·#543·#534 등 다른 수정도 있음. 2.13.0(2026-06-15)에는 누적 지연을 expected_finish_state 에 반영(#518)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "Open-RMF의 신호등(일시정지·재개) 수준 연동을 비교·시험할 때는 제어 수준뿐 아니라 EasyTrafficLight 수정(f21)이 포함된 rmf_fleet_adapter 판도 기록해야 하며, 이 변경 이력은 수정의 존재를 보여 줄 뿐 제어 수준별 처리량 비교 실험은 아니라고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1513"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21에서 도출. oq-032(제어 수준에 따른 교통 성능 차이)는 이 자료로 답해지지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Jiang 외의 SILLM 논문(Deploying Ten Thousand Robots, ICRA 2025 채택, arXiv 초판 2024-10-28, v2 2025-05-18)은 최대 10,000 에이전트의 6개 대형 지도 벤치마크와 별도로, 초록과 서론에서 실물 로봇 10대·가상 로봇 100대로 모사 창고(mock warehouse)에서 검증했다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv comment: Accepted by ICRA 2025. 초록: six large-scale maps with up to 10,000 agents; \"validated SILLM with 10 real robots and 100 virtual robots in a mock warehouse environment\"(서론 끝에도 같은 문장). §V-C 본문은 대수 없이 프로젝트 웹페이지를 가리킴",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "SILLM의 실물 검증(부록 VI-D)은 계획이 모든 에이전트 위치를 정확히 안다고 가정하므로 실물 로봇 위치를 외부 모션 캡처(Optitrack)로 얻고, 교란·제어 오차로 생기는 실행 오차는 행동 의존 그래프(Action Dependency Graph, ADG)로 없앴다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "부록 VI-D Real-World Mini Example: 가상 로봇은 참값 위치, 실물은 Optitrack Motion Capture 외부 위치 추정, 실행 오차는 ADG 로 제거. 가상 실험에서 Learnable PIBT 가 PIBT 보다 처리량이 높았다고 보고",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "SILLM 논문은 2023 League of Robot Runners 우승 해법 WPPL과 비교할 때 다른 기준선에 맞추려고 회전 동작을 없애고, 원래의 단계당 계획 시간 1초 제한 대신 대규모 이웃 탐색 개선 반복 횟수를 40,000회로 제한했다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "부록 VI-F1(WPPL): \"We remove the rotation action to align with the settings in other baselines\". 단계당 1초 대신 LNS 개선 반복 40,000회(모방 학습에 쓴 총 반복 수 수준)로 제한. 공개 저장소 MAPF-LRR2023 기반 구현",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "SILLM 제목의 10,000은 계산 벤치마크의 에이전트 수이지 실물 배치 대수가 아니고, WPPL 비교는 회전 제거·반복 수 제한으로 바꾼 조건의 결과이므로 원래 대회 조건의 재현으로 읽어서는 안 된다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f23·f25에서 도출. 성능 우위는 같은 논문의 저자 보고",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "Yan 외의 LSMART(2026-02-17 프리프린트)는 운동 제약·통신 지연·실행 불확실성·계획과 실행의 동시 진행·계획 실패 복구를 고려해 AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터이며, 계획기·인스턴스 생성기·계획 호출 정책·실패 정책을 설계 선택으로 비교한다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2–3 모델·구조: FMS 는 (1) 통신 지연 (2) 행동 완료 시각의 실행 불확실성 (3) 동시 계획·실행 (4) 계획 실패 복구를 고려. §5: 네 가지 설계 선택을 모듈로 제공. arXiv v1 HTML 본문 열람",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "LSMART 실험은 지도와 에이전트 수 조건마다 600초 시뮬레이션을 10회 돌려 평균과 95% 신뢰구간을 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.1 General Experiment Setup: 'we run 10 simulations, each lasting for 600 simulation seconds', 평균은 실선, 95% 신뢰구간은 음영. warehouse-33-36 과 MAPF 벤치마크 지도 5종",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "LSMART 실험에서 재계획을 더 자주 하는 것은 모든 지도·밀도에서 유리하지 않았으며(room-64-64-16과 낮은 밀도에서 이점이 일관되지 않음), 저자들은 ADG로 추정한 확정 지점이 실제 진행과 맞지 않는 실행–계획 불일치를 원인으로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.3 Planner Invocation Policy, 그림 4·5: 에이전트가 적으면 짧은 지평·잦은 호출, 많으면 덜 잦은 호출·긴 지평이 유리. 재계획 빈도 이점은 room-64-64-16·저밀도에서 일관되지 않음. 원인: commit cut 추정 불일치",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "LSMART 실험에서 더 정확한 로봇 모델과 더 강한 최적성 보장은 계획기의 확장성을 떨어뜨려, 저자들은 이를 계획기의 해 품질과 확장성(solution quality and scalability) 사이의 절충으로 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.5 Optimality and Robot Model Accuracy, 그림 7: 실패 정책을 쓰지 않으면 정확한 모델이 항상 처리량이 높고, 최적·준최적 계획기는 둘 다 풀 수 있을 때 해 품질이 비슷함. room-64-64-16·warehouse-10-20-10-2-1 에서 절충이 뚜렷",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "LSMART는 4-연결 격자 기반 시뮬레이션이며 논문에 실물 로봇 실험은 없고, 저자들은 4-연결 격자를 넘는 그래프 지원을 향후 과제로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3: 2D 작업 공간을 격자로 나누고 AGV 는 한 칸 점유, 대기·회전·인접 칸 이동. §5 Conclusion: 'Future work includes adding support for graphs beyond the 4-connected grid'. 본문에 실물 로봇 실험 없음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "LSMART가 격자 시뮬레이션만 다루므로(f31), 이종 제조사 로봇이 섞인 실물 창고에서의 개선율을 직접 제공하지는 않는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f31에서 도출. 실험 지도는 격자 벤치마크이고 AGV 모델은 한 종류 기준",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "oq-058에 대해 SILLM의 실물 10대 모사 창고 검증(f23·f24)과 LSMART의 실행 불확실성을 넣은 처리량 실험(f27~f29)이 부분 근거가 되지만, 벤치마크 개선율을 상용 물류센터 실측 개선율로 환산한 자료나 국내 사례는 확인하지 못해 정량 전이 질문은 열린 채로 둔다고 이 위키는 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-199",
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 자료 모두 모사 창고 또는 격자 시뮬레이션이며 상용 물류센터 처리량 실측과의 비교를 담지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "oq-059에 대해 MAPF-DL은 공통 마감을 교통 계획의 목적함수에 넣는 정식화를 주지만 작업별 업무 우선순위를 통로 양보 우선권으로 바꾸는 규칙은 다루지 않고, VDA 5050 3.0.0도 우선순위·교착 해소 같은 교통 관리 로직을 범위에서 뺀다.",
      "tag": "사실",
      "source_ids": [
        "ref-1514",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MAPF-DL §2: 공통 마감 Tend 하나와 성공 대수 최대화만 정의. VDA 5050 §2 Scope: 'Traffic Management Logic: … routing, prioritization, congestion handling, or deadlock resolution … are not included'",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-195",
      "org": "Phillips, M., & Likhachev, M.",
      "title": "SIPP: Safe interval path planning for dynamic environments",
      "published": "2011",
      "url": "https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "동적 장애물의 예측 궤적이 주어질 때 위치·안전 구간 상태로 로봇 한 대의 경로를 찾는 SIPP 를 제시한 ICRA 2011 논문. 이번에 저자 연구실 PDF로 원문을 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cs.cmu.edu/~maxim/files/sipp_icra11.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-189",
      "org": "Okumura, K., Machida, M., Défago, X., & Tamura, Y.",
      "title": "Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding",
      "published": "2019-01",
      "url": "https://arxiv.org/abs/1901.11282",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "우선순위 상속과 되돌림으로 반복형 MAPF 를 푸는 PIBT 논문. 이번에 Artificial Intelligence 2022 게재판인 arXiv v5(2022-06-27, DOI 10.1016/j.artint.2022.103752)를 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/1901.11282v5",
      "source_unopened": false
    },
    {
      "id": "ref-192",
      "org": "Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L.",
      "title": "A traffic management system for large and heterogeneous vehicles in narrow industrial environments",
      "published": "2026-09-09",
      "url": "https://arxiv.org/abs/2609.10400",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "NURBS 경로망 위 지속형 MAPF·경로 할당·교착 탐지·해소로 좁은 산업 현장의 이종 대형 AGV 를 조율하는 교통 관리 시스템. The International Journal of Robotics Research 2026 게재(DOI 10.1177/02783649261470035)이며 이번에 arXiv v1 본문을 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2609.10400v1",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 공식 명세 본문. 이번에 3.0.0 태그 판을 열어 §2 범위, §6.4 구역, §6.8 예정 경로 공유를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1513",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그 고정). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행·누적 지연 계산 수정이 기록돼 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    },
    {
      "id": "ref-199",
      "org": "Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J.",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10-28",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "지속형 MAPF 에 확장형 모방 학습(SILLM)을 적용한 ICRA 2025 채택 논문. 이번에 v2(2025-05-18) 본문을 열람해 계산 벤치마크와 실물 10대·가상 100대 검증, WPPL 비교 조건을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2410.21415v2",
      "source_unopened": false
    },
    {
      "id": "ref-604",
      "org": "Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02-17",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "AGV 플릿 관리 시스템 안에서 MAPF 알고리즘을 현실적으로 평가하는 오픈소스 시뮬레이터 LSMART 와 설계 선택 비교 연구(프리프린트). 이번에 v1 본문을 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2602.15721v1",
      "source_unopened": false
    },
    {
      "id": "ref-1514",
      "org": "Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S.",
      "title": "Multi-Agent Path Finding with Deadlines",
      "published": "2018",
      "url": "https://www.ijcai.org/proceedings/2018/0058.pdf",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "공통 마감까지 목표에 도달하는 에이전트 수를 최대화하는 MAPF-DL 을 정식화하고 NP-hard 증명과 흐름 환원·탐색 해법을 낸 IJCAI 2018 논문(pp.417–423). 학회 공식 PDF를 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 제조 공장 사례 추가: Bonetti 외(IJRR 2026) 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 Gruppo TecnoFerrari 제공)(f8), 팔레트 운반 흐름(f9), 배치별 차량·복도 제약(f10), 시스템 구성(f11), 그림 9 실험 사진 한 장·그림 10–12 Supervisor 2D 재구성·10시간 실행(f12), 처리량 최대 약 11%는 저자 보고(f13), 현장 일반 개선율로 옮기지 않음(f14). 기존 ref-192 의 '프리프린트' 표기를 IJRR 게재로 고친다 / 섹션 6(주제 페이지 s6 요약) — 첫 문장 수정: SIPP 는 예측 궤적이 주어진 단일 로봇 경로 탐색(f1)이며 MAPF 전체 최적성으로 옮길 수 없음(f2), 다중 로봇 계획기 안 저수준 계층 예(f3), 서술 분리 권고(f4). PIBT '완전·최적 아님'(f5)과 현장 권고(f7), 교착 탐지·해소 모듈(f6). 그래프 조건 문장은 s6 기존 내용 확인(중복 추가 안 함). MAPF-DL 정식화(f15·f16)와 산업 기준이 아니라는 한정(f17) / 섹션 7(주제 페이지 s7 요약) — VDA 5050 3.0.0 §6.8 예정 경로 공유(f18), §6.4.3 협조 재계획 구역 REPLANNING 요청(f19), 메시지 상호운용성과 교통 최적화 성능 별도 검토(f20). 구역 4종 표·§2 범위 제외는 s7 기존 내용 확인(중복 추가 안 함), 발표일은 쓰지 않음. Open-RMF rmf_fleet_adapter 2.14.0 EasyTrafficLight 수정(f21)과 판 기록 권고(f22) / 섹션 8(주제 페이지 s8 요약) — SILLM 항목 수정: '2024, 프리프린트' → ICRA 2025 채택, 계산 벤치마크 10,000과 실물 10대·가상 100대(초록·서론 기준) 구분(f23), 모션 캡처·ADG(f24), WPPL 비교 조건 변경(f25), 해석 한정(f26). LSMART 추가(f27~f32): 시뮬레이터 구성, 600초×10회, 재계획 빈도 결과, 해 품질과 확장성 절충, 4-연결 격자·실물 실험 없음(사실)과 실물 창고 개선율 미제공(추정) / 섹션 11 — oq-058 부분 근거(f33), oq-059 부분 근거(f34), oq-032 는 f21·f22 가 관련 판 정보만 주며 답하지 않음. 새 질문 2건. 출처: ref-189·ref-192·ref-195·ref-199·ref-604·ref-031 원문 열람으로 갱신, 신규 ref-1513·ref-1514. 다음 실행 후보: 62. 제조 공장(f8~f14 사례 연결), 54. 시험·형식 검증·벤치마크(f27~f32), 20. 로봇·제조사 관제 연동(f18·f19·f21)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f7 | 종류: 일반",
    "실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF, 32. 예외 복구·재계획·업무 연속성 | 근거: f29 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 8,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-04/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "VDA 5050 3.0.0 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 쓰지 않았고(published null), GitHub release notes 출처(메모 n4)는 원문 확인이 안 돼 제외했다. '주요 변경' 서술은 명세 본문 §6.8·§6.4.3 으로 근거를 옮겼다",
      "ref-031 은 main 판 URL 의 기존 출처이며 이번 열람은 3.0.0 태그 판이다. main 판이 3.0.0 과 같은지는 다시 대조하지 않았다",
      "f13·f14: Bonetti 외의 배치별 처리량 수치가 모사 실행인지 실제 공장 운행인지 원문이 수치 단위로 구분하지 않아 확인 못 함. 독립 현장 재현 미확인",
      "f23: SILLM 의 실물 10대·가상 100대는 초록과 서론 끝 문장 기준이며 §V-C 본문은 대수 없이 프로젝트 웹페이지를 가리킨다(웹페이지 미열람)",
      "모든 사실 finding 은 단일 출처라 교차 확인 0건",
      "oq-058·oq-059 는 부분 근거만 있어 해결 제안하지 않음. oq-032·oq-057 근거 없음"
    ],
    "scope_violations": [
      "f6·f11: 교착 탐지·해소와 경로 할당은 ROP 직접 범위(여러 플릿의 공유 공간 조율)에 해당하나, Bonetti 외 시스템은 단일 업체 관제 안의 기능이므로 9절 책임 경계와 섞지 않도록 사례 근거로만 쓴다",
      "f24: 실물 로봇 위치 추정(모션 캡처)과 실행 오차 보정은 로봇 쪽 위치 인식·제어(외부 연계 대상)와 맞닿아 있어 실험 조건 설명으로만 쓴다"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 2
    },
    "limits": "외부 조사 변환이라 검색 집계 없음(queries 0 은 이 실행 안의 WebSearch 호출이 없다는 뜻이며, 외부 AI의 검색 횟수는 알 수 없다). 원문 대조는 2026-10-10 검증 서브에이전트가 WebFetch·GitHub raw 로 연 사본(9건 중 release notes 제외 8건)으로 했다. 출처 8건: 기존 6건(ref-031·ref-189·ref-192·ref-195·ref-199·ref-604, 이번에 원문 열람으로 fetched true), 신규 2건(ref-1513 rmf_fleet_adapter 변경 이력, ref-1514 MAPF-DL; 예약 구간 ref-1513~ref-1542 안). 동료심사 게재가 확인된 논문(ref-189 AIJ 2022, ref-192 IJRR 2026, ref-195 ICRA 2011, ref-199 ICRA 2025, ref-1514 IJCAI 2018)은 원문 열람 기준에 따라 신뢰도 high 로 적었고 프리프린트 ref-604 는 medium. 검증 수정 반영: ref-192 를 프리프린트가 아닌 IJRR 게재로, 현장 유형을 '팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 제공)'로, 사진은 그림 9 한 장·그림 10–12 는 Supervisor 2D 재구성으로 정정. PIBT 는 v5=AIJ 게재판으로 적고 그래프 조건은 s6 기존 문장이 있어 다시 넣지 않음. SILLM ICRA 2025 채택 반영. VDA 5050 발표일 null·release notes 제외, 구역 4종·§2 범위 제외는 s7 기존 내용이라 사실 finding 으로 다시 내지 않음. LSMART 마지막 문장을 사실(f31: 4-연결 격자·실물 실험 없음)과 추정(f32: 실물 창고 개선율 미제공)으로 나누고 절충 표현은 원문 'solution quality and scalability'. SIPP 는 '예측 궤적'으로. 현장 유형 finding 은 제조 공장(f6·f8~f14)뿐이며 물류창고 사례는 모사 창고(SILLM)라 site_type null. 국내 자료 없음. 용어 후보 없음(MAPF·SIPP·PIBT·ADG 계열 용어는 기존 페이지에 있고 MAPF-DL 은 본문 정의로 충분). 입력 누락 없음. 정정 요청·우선 지정 질문 없음."
  }
}
```

### runs/2026-10-10-04/verification.json

```json
{
  "run_id": "2026-10-10-04",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CMU RI 출판 페이지(publications.ri.cmu.edu)에서 Phillips·Likhachev, ICRA 2011, pp.5628–5635와 초록의 'same optimality and completeness guarantees as planning with time as an additional dimension'을 확인했다. 검증 단계에서 저자 연구실 PDF(cs.cmu.edu)는 판독하지 못해 §I·§III의 '예측 궤적' 문구는 리서치 열람에 기댄다. 검색 결과로 '장애물 궤적이 미리 주어진다'는 전제와 단일 에이전트 계획임은 확인했다. 단일 출처라 medium."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f1(단일 로봇·주어진 궤적)과 f3(Bonetti 외 §2.1)에서 도출한 추론이며 [추정] 태그가 적정하다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2609.10400v1 HTML §2.1에서 Yan·Li(2024) 3단 계획기(PBS+SIPP+베지에)가 'does not provide any global optimality guarantees'라는 문장과 Kasaura 외 PSIPP/CTCs의 최적성 무보장 서술을 확인했다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f1·f3에서 도출한 위키(구축자) 의견이다. 기존 6절 첫 문장(SIPP를 CBS와 함께 최적해 보장 다중 로봇 탐색으로 묶은 [사실] 문장)을 고치는 근거로 쓴다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 페이지에서 v5 2022-06-27, 주석 'to appear in AIJ, previously presented at IJCAI-19', 관련 DOI 10.1016/j.artint.2022.103752를 확인했다. 검색 결과로 '준최적 알고리즘'이라는 설명과 그래프 조건부 도달성을 확인했다. §2.1의 정확한 문구('neither complete nor optimal')는 검증 단계에서 PDF를 판독하지 못해 리서치 열람에 기댄다. 용어는 용어집 표기 '우선순위 상속·되돌림'으로 맞춘다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §9에서 교착 원인(작업 갱신 같은 예측 못 한 사건, 시간 지평 부족), Pratissoli 외(2023)의 순환·비순환 분류, 선행 관계 그래프, 관련 AGV 경로 갱신으로 해소하는 내용을 확인했다. 단일 업체 관제 안의 기능이므로 9절 책임 경계의 근거로 쓰지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f5(그래프 조건·불완전성)와 f10(그림 10·11의 막다른 복도)·f6에서 도출한 위키 의견이다. 그림 11 캡션에는 'narrow'가 없고 그림 10 캡션에만 있다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 페이지의 저널 참조 'The International Journal of Robotics Research, 2026'과 관련 DOI 10.1177/02783649261470035, v1 2026-09-09, §10의 Gruppo TecnoFerrari 협업, 업체가 제공한 경로망·배치, 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치를 확인했다. Guidetti의 업체 소속도 확인했다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §10.1 배치 1의 흐름(팔레타이저 → 포장기, 포장기가 바쁘면 임시 보관, 디스펜서에서 빈 팔레트 공급)을 확인했다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 배치 1(동종 C1, 복도 4개 포함 8개 구역), 배치 2(C1·C2 두 등급, 복도 4개 포함 7개 구역), 배치 3(복도 구역 없음·단방향 트랙의 넓은 공간)을 확인했다. 그림 10 캡션은 'dead-end narrow corridors', 그림 11 캡션은 'dead-end corridors'다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록(NURBS 경로망 위 L-MAPF, 수정 Bounded Horizon CBS, Rolling Horizon Conflict Resolution, 실행 계층, 교착 처리), §8 경로 할당기, §10.1의 C# 구현과 TecnoFerrari Supervisor 통합을 확인했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'validated in a real industrial environment', 그림 9 자동화 공장 실험 사진, 그림 10–12 Supervisor 2D 재구성, Supervisor 실행 중 연속 작업 배정으로 KPI를 수집한 것, 시나리오당 약 10시간을 확인했다. 원문은 KPI 실행이 실물 AGV인지 시뮬레이션인지 명시하지 않는다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 확인: 초록의 'up to 11%'와 세 비교 기준(규칙 기반, 최신 산업 해법, 우선순위 기반 L-MAPF 변형)은 확인했다. 배치별 수치(배치 1 약 10·7·6%, 배치 2 약 11·7·10%)는 arXiv HTML 렌더링에 §10.2.4가 보이지 않고 PDF도 판독하지 못해 검증 단계에서 재확인하지 못했다. 최대 약 11%만 [사실]로 두고 배치별 수치는 [추정](저자 보고, 검증 미재확인)으로 강등한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f8·f12·f13에서 도출한 위키 의견이다. 원문이 '실제 산업 환경에서 검증'이라고 쓰면서도 KPI 실행의 실물·모사 구분을 밝히지 않는다는 점은 검증 결과와 맞다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 논문 본문 텍스트(IJCAI 2018 텍스트 사본)에서 공통 마감 Tend, 성공 정의('occupies its goal vertex at the deadline Tend'), 성공 에이전트 수 최대화, 3-SAT 환원 NP-hard 증명(정리 1), 다중 상품 흐름 ILP, CBS-DL·DBS·MA-DBS를 확인했다. 서지(pp.417–423, DOI 10.24963/ijcai.2018/58)는 IJCAI 공식 목록 기준이다. 학회 PDF는 검증 단계에서 판독하지 못했다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 서론의 'minimize the sum of the arrival times of the agents or the makespan'과, G-TAPF가 'does not directly maximize the number of agents that can finish the tasks by the deadlines'라는 서술을 확인했다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MAPF-DL의 공통 마감 정의(f15)와 VDA 5050 3.0.0 §2의 교통 관리 로직 제외(입력 원문 텍스트 ref-031)에서 도출한 위키 의견이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 태그 원문 §6.8에서 상태 메시지로 예정 궤적을 알리는 것, plannedPath(NURBS, 최소한 현재 베이스를 포함, nodeId 포함 가능), intermediatePath(경유점별 ETA를 담은 폴리라인), 매 상태 메시지 공유, 현재 위치에서 시작, 길이는 로봇이 정함, visualization 토픽, edgeState trajectory는 미리 정한 궤적의 확인용임을 확인했다. 주장의 '주문 안의 긴 경로'는 원문과 다르다(plannedPath는 상태 메시지 필드이며 주문의 베이스를 최소한 덮는다). 표현을 고친다. §7.8 표는 두 필드를 선택 필드로 표시한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 원문 §6.4.3에서 협조 재계획 구역 진입·구역 안 재계획 때 requestType 'REPLANNING', zoneRequest trajectory 필드의 NURBS 예정 경로, 응답을 제때 받지 못하면 진입 금지, 해제 구역은 'ACCESS'임을 확인했다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §2 Scope의 'Traffic Management Logic … not included'(입력 원문 텍스트)와 f18·f19에서 도출한 위키 의견이다. 같은 §2 사실은 기존 7절(s7)에 있으므로 새 각주를 만들지 않고 ref-031을 재사용한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2.14.0 태그 CHANGELOG.rst에서 2.14.0(2026-09-26)의 #525·#524와 2.13.0(2026-06-15)의 #518(expected_finish_state에 누적 지연 반영)을 확인했다. 같은 URL이 2026-10-10-02(ref-1458)·2026-10-10-03(ref-1487) 브리프에 이미 다른 id로 올라 있다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f21에서 도출한 위키 의견이다. oq-032에 답하지 않는다는 한정이 적절하다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 페이지에서 v1 2024-10-28, v2 2025-05-18, 주석 'Accepted by ICRA 2025', 저자 6명을 확인했다. v2 HTML에서 초록의 6개 지도·최대 10,000 에이전트와 실물 10대·가상 100대 모사 창고 검증, §V-C가 프로젝트 웹페이지를 가리키는 것을 확인했다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 부록 VI-D에서 Optitrack 모션 캡처로 실물 위치를 얻고 ADG로 실행 오차를 없앤 것을 확인했다. 로봇 쪽 위치 인식은 연계 대상이므로 실험 조건 설명으로만 쓴다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 부록 VI-F1에서 회전 동작을 없앤 것('to align with the settings in other baselines')과 단계당 1초 대신 LNS 반복 40,000회로 제한한 것을 확인했다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f23·f25에서 도출한 위키 의견이다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: v1 HTML(2026-02-17, CMU·Symbotic 저자 8명)에서 FMS 안에서 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터, 통신 지연·실행 불확실성·동시 계획·실행·계획 실패 복구를 확인했다. 프리프린트이며 저자 일부가 Symbotic 소속이다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.1에서 조건마다 600초 시뮬레이션 10회, 평균과 95% 신뢰구간을 확인했다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.3에서 room-64-64-16과 낮은 밀도에서 재계획 빈도의 이점이 일관되지 않다는 것과 ADG 확정 지점(commit cut) 추정 불일치를 원인으로 든 것을 확인했다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.5에서 'both more accurate models and stronger optimality guarantees degrade the planners' scalability'를 확인했다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4-연결 격자, 결론의 '4-연결 격자를 넘는 그래프 지원' 향후 과제, 실물 로봇 실험 없음(모든 결과가 물리 기반 시뮬레이션)을 확인했다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f31에서 도출한 [추정]이며 태그가 적정하다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f23·f24·f27~f29에서 도출한 위키 의견이다. oq-058은 열린 채로 둔다(해결 제안 없음)."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MAPF-DL §2 정의(공통 마감 하나, 성공 대수 최대화)와 VDA 5050 3.0.0 §2 Scope의 교통 관리 로직 제외를 각각 원문으로 확인했다. 두 출처가 서로 다른 부분 주장을 뒷받침하므로 교차 확인으로 세지 않는다. oq-059는 부분 근거이고 해결이 아니다."
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
      "ref-1513(rmf_fleet_adapter CHANGELOG.rst, 2.14.0 태그)은 같은 URL이 2026-10-10-02 브리프의 ref-1458, 2026-10-10-03 브리프의 ref-1487로 이미 등록돼 있다. 퍼블리셔가 같은 URL을 기존 id로 합치므로 새 id를 만들지 않는다",
      "f20의 근거인 VDA 5050 §2 교통 관리 로직 제외와 f19의 구역 4종 표는 기존 7절(주제 페이지 s7)에 이미 있다. ref-031 각주를 재사용하고 같은 사실을 다시 싣지 않는다",
      "f5의 PIBT 그래프 조건은 기존 6절(주제 페이지 s6)에 이미 있다(브리프도 중복 추가하지 않는다고 밝힘)",
      "기존 6절 첫 문장 'MAPF 해법은 최적해를 보장하는 탐색(CBS·SIPP)부터…'([사실][^ref-187][^ref-195][^ref-189][^ref-196])은 f1~f4와 어긋난다. SIPP는 주어진 궤적에 대한 단일 로봇 계획이다",
      "기존 5절 표의 예외·성과 칸과 각주가 ref-192를 2026-09 프리프린트로 적고 있으나, f8로 IJRR 2026 게재가 확인됐다",
      "기존 11절의 신규 질문 3건은 열린 질문 목록의 oq-057·oq-058·oq-059와 같은 질문이다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f5·ref-189 요약의 '우선순위 상속과 되돌리기'는 용어집 priority-inheritance-with-backtracking의 '우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))'과 다르다. 용어집 표기로 맞춘다"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "6절(주제 페이지 s6 요약) 첫 문장: 'MAPF 해법은 최적해를 보장하는 탐색(CBS·SIPP)부터…'를 고친다. CBS(ref-187)는 최적 다중 에이전트 탐색으로 두고, SIPP는 주어진 장애물(다른 로봇의 예정 궤적 포함) 궤적에 대해 로봇 한 대의 경로를 찾는 저수준 계획으로 분리한다. SIPP의 최적성·완전성은 그 단일 로봇 문제에 대한 것이다(f1 [사실], f2 [추정], f3 [사실], f4 [의견]). 근거: 기존 문장이 출처 ref-195가 말하는 범위를 넘는다.",
    "f13: 처리량 개선은 '최대 약 11%'(초록 확인, 저자 보고)만 [사실]로 둔다. 배치별 수치(배치 1 약 10·7·6%, 배치 2 약 11·7·10%)는 싣지 않거나 [추정]으로 강등하고 '저자 보고, 검증 단계 원문 미재확인'을 병기한다. 근거: 검증에서 §10.2.4를 다시 확인하지 못했다.",
    "f18: '주문 안의 긴 경로 plannedPath'를 '상태 메시지의 plannedPath(NURBS, 최소한 현재 베이스를 덮고 지날 nodeId를 담을 수 있음)'로 고친다. 근거: §6.8은 plannedPath를 주문이 아니라 상태 메시지 필드로 정의한다.",
    "5절: 기존 물류창고 표와 별도로 '현장 유형: 제조 공장' 사례를 여섯 항목으로 추가한다. 작업 대상은 f9, 수행 자원은 f11, 제약은 f10, 예외·성과는 f6·f12·f13(강등 반영)·f14를 쓰고, 시작 조건은 f12의 '연속 작업 배정'만 근거로 쓴다. 완료·인계 칸은 근거 finding이 없으므로 '미확인'으로 둔다. 사례 머리에 '업체가 제공한 실제 배치를 모사한 세 배치로 평가했고 실제 운행은 그림 9 사진 한 장으로 제시됨, 업체 소속 공동저자 있음'(f8·f12·f14)을 밝힌다. site_matrix_updates에는 site_type '제조 공장'으로 실제로 채운 칸만 낸다.",
    "f6·f11: Bonetti 외의 교착 탐지·경로 할당은 단일 업체 관제(TecnoFerrari Supervisor) 안의 기능이므로 5·6절 사례 근거로만 쓴다. 9절 책임 경계 표의 ROP 직접 범위 근거로 쓰지 않는다.",
    "f24: 모션 캡처 위치 추정과 실행 오차 보정은 로봇 자체 위치 인식·제어(연계 대상)와 맞닿으므로 SILLM 실험 조건 설명으로만 쓴다.",
    "ref-192 각주와 참고문헌 갱신: 'The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09'로 고친다. 접근일은 2026-10-10이고 원문 미열람 표시를 지운다. 기존 5절 등의 '프리프린트' 표기를 고친다.",
    "ref-199 각주: 저자를 'Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J.'로 하고 'ICRA 2025 채택(arXiv v1 2024-10-28, v2 2025-05-18)'을 적는다. 접근일은 2026-10-10이고 원문 미열람 표시를 지운다. 8절의 SILLM 항목에서 계산 벤치마크 10,000과 실물 10대·가상 100대(초록·서론 기준)를 구분한다(f23·f26).",
    "ref-189 각주: 열람판을 'arXiv v5 2022-06-27(AIJ 게재 예정 표기, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19)'로 밝힌다. 접근일은 2026-10-10이고 원문 미열람 표시를 지운다. PIBT 표기는 용어집의 '우선순위 상속·되돌림'으로 맞춘다.",
    "ref-195 각주: 접근일을 2026-10-10으로 바꾸고 원문 미열람 표시를 지운다(리서치가 저자 연구실 PDF를 열람). ICRA 2011, pp.5628–5635를 병기할 수 있다.",
    "ref-031: 이번 인용이 3.0.0 판 기준임을 본문 또는 각주에 밝힌다('3.0.0 태그 판, 확인일 2026-10-10'). 입력 원문 텍스트(main 판)의 머리가 Version 3.0.0이므로 main과 3.0.0의 판은 같다. 발표일은 쓰지 않는다.",
    "ref-1513: 같은 URL이 참고문헌 목록에 이미 등록돼 있으면(ref-1458 또는 ref-1487) 그 id를 쓴다. 새로 등록하지 않는다.",
    "ref-1514 참고문헌 등록: 'Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S., Multi-Agent Path Finding with Deadlines, IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58, https://www.ijcai.org/proceedings/2018/0058.pdf'로 적는다. MAPF-DL은 '모든 에이전트에 공통 마감 하나'로 쓰고 에이전트별 마감으로 쓰지 않는다(f15·f17).",
    "직접 인용은 출처당 1회만 쓴다. ref-192(f3·f8·f12 발췌에 영어 인용 여러 개), ref-604(f28·f30), ref-031(f34)은 한 구절만 원문으로 남기고 나머지는 한국어로 다시 서술한다.",
    "11절: oq-058에는 f33, oq-059에는 f34를 부분 근거로 반영하고 두 질문 모두 열림을 유지한다. oq-032는 f21·f22가 답하지 않는다고 적는다. 기존 11절의 '(신규 · …)' 질문 3건은 oq-057·oq-058·oq-059 id로 표기한다. 새 질문 2건(f7·f29 근거)을 등록한다.",
    "트랙 반영 제안(2026-09-25-58, 건축 도면 자동 인식 단계 3, 6절 '경로망 자동 생성 입력 초안')은 이번 브리프에 근거 finding이 없으므로 6절에 반영하지 않는다. 제안 상태로 다음 해당 영역 실행에 넘기고 changelog_entry에 '근거 없음으로 미반영'을 적는다.",
    "corr: 이 영역에 걸린 정정 요청이 없음을 changelog_entry에 적는다(처리할 corr id 없음)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 33건, 미확인 1건(f13 배치별 수치), 교차 확인 0건. 강등: f13 사실 → 일부 추정(배치별 처리량 수치. 최대 약 11%는 사실 유지). 원문 미열람 출처: 없음. 리서치가 8건 모두 원문을 열었고, 검증에서는 ref-192·ref-199·ref-604·ref-031·ref-1513 본문을 직접 다시 확인했다. ref-195·ref-189는 PDF를 판독하지 못해 서지·초록과 검색 결과로, ref-1514는 본문 텍스트 사본과 IJCAI 공식 목록으로 확인했다. 검증 검색은 4회 했다(리서치 0회). 주의: 모든 사실 주장이 단일 출처이고 교차 확인이 없다. Bonetti 외의 처리량 개선은 업체 공동저자가 있는 저자 보고이며, 원문은 KPI가 실물 운행인지 모사 실행인지 구분하지 않는다. SILLM의 10,000은 계산 벤치마크 규모다. LSMART는 격자 시뮬레이션 프리프린트다. 기존 6절의 'CBS·SIPP 최적해 보장' 문장은 SIPP가 단일 로봇 계획이라는 원문과 어긋나 고친다. 리서치 브리프의 ref-1514는 fetched: true인데 fetch_url이 비어 있다. ref-1513은 같은 URL의 기존 id(ref-1458·ref-1487)와 겹친다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-058·oq-059 부분 근거, oq-032·oq-057 근거 없음). 트랙 반영 제안 1건(2026-09-25-58)은 근거 finding이 없어 이번에 반영하지 않는다.",
  "retry_reason": null
}
```

### runs/2026-10-10-04/pages.json

```json
{
  "run_id": "2026-10-10-04",
  "outline": [
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "기존 물류창고 설명용 시나리오는 그대로 두고, Bonetti 외(IJRR 2026)가 산업체 제공 배치로 모사한 팔레타이징·보관·팔레트 포장 공장의 이종 대형 AGV 교통 관리 사례를 여섯 항목으로 더한다. [사실][^ref-192]",
      "planned_findings": [
        "f6",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1900,
      "summary": "MAPF 해법은 최적 다중 에이전트 탐색 CBS부터 반복형 PIBT까지 폭이 넓고, SIPP는 주어진 예측 궤적에 대한 단일 로봇 저수준 계획이다. [사실][^ref-187][^ref-195]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1100,
      "summary": "Open-RMF는 교통 스케줄·협상을, VDA 5050은 경로 해제·구역 규칙을 정하며 3.0.0 판은 예정 경로 공유와 협조 재계획 구역 요청을 둔다. [사실][^ref-004][^ref-031]",
      "planned_findings": [
        "f18",
        "f19",
        "f20",
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1900,
      "summary": "Li 외(2020)·Ma 외(2017)를 기준 자료로 두고, Bonetti 외의 IJRR 게재, SILLM의 계산 규모와 실물 검증 구분, LSMART의 실행 조건 평가를 정리한다. [사실][^ref-005][^ref-006]",
      "planned_findings": [
        "f8",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f31",
        "f32"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 300,
      "summary": "기존 연결에 54. 시험·형식 검증·벤치마크(LSMART)와 62. 제조 공장(Bonetti 외 사례)을 더한다. [추정][^ref-604][^ref-192]",
      "planned_findings": [
        "f27",
        "f8"
      ]
    },
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "section": "11. 열린 질문",
      "budget_chars": 1300,
      "summary": "oq-032·oq-057·oq-058·oq-059를 id로 표기하고 oq-058·oq-059에 부분 근거를 더하며 새 질문 2건을 올린다. [의견][^ref-199][^ref-604]",
      "planned_findings": [
        "f21",
        "f22",
        "f33",
        "f34",
        "f7",
        "f29"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5절 제조 공장 사례 추가, 6절 첫 문장 정정(SIPP를 단일 로봇 저수준 계획으로 분리)·PIBT 보장 범위·교착 모듈·MAPF-DL 보강, 7절 VDA 5050 3.0.0 예정 경로·구역 요청과 Open-RMF 2.14.0, 8절 Bonetti 외 게재·SILLM 정정·LSMART 추가, 10절 54·62 연결, 11절 oq id 표기·부분 근거·새 질문 2건, 13절 각주 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)",
          "frontmatter": {
            "related_areas": [
              15,
              20,
              25,
              28,
              34,
              47,
              54,
              55,
              62
            ],
            "sources": [
              "ref-004",
              "ref-005",
              "ref-006",
              "ref-031",
              "ref-079",
              "ref-253",
              "ref-267",
              "ref-268",
              "ref-186",
              "ref-187",
              "ref-188",
              "ref-189",
              "ref-190",
              "ref-191",
              "ref-192",
              "ref-193",
              "ref-194",
              "ref-195",
              "ref-196",
              "ref-197",
              "ref-199",
              "ref-604",
              "ref-1513",
              "ref-1514"
            ]
          }
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-area27-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 의 \"8. 대표 연구와 자료\" 절(1,947자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area27-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 의 \"6. 대표 접근법과 기술\" 절(1,872자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area27-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 의 \"11. 열린 질문\" 절(1,370자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area27-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,076자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area27-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(848자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 27. 다중 로봇 경로·교통 관리 — MAPF | 갱신: 5절 제조 공장 사례 추가, 6절 SIPP·CBS 묶음 서술 정정과 PIBT 보장 범위·교착 모듈·MAPF-DL 보강, 7절 VDA 5050 3.0.0 예정 경로 공유·구역 요청과 Open-RMF rmf_fleet_adapter 2.14.0, 8절 Bonetti 외 IJRR 게재·SILLM 정정·LSMART 추가, 11절 oq-057~059 id 표기와 새 질문 2건; 트랙 반영 제안(2026-09-25-58, 건축 도면 자동 인식)은 근거 없음으로 미반영; 정정 요청 없음(처리할 corr id 없음) | run 2026-10-10-04",
  "index_updates": {
    "home_recent": "2026-10-10 — 27. 다중 로봇 경로·교통 관리 — MAPF: 제조 공장 적용 사례(이종 대형 AGV 교통 관리)를 더하고 SIPP 서술 정정, VDA 5050 3.0.0 예정 경로 공유, SILLM·LSMART 해석 한정을 반영",
    "category_recent": "2026-10-10 — 27. 다중 로봇 경로·교통 관리 — MAPF: 5·6·7·8·11절 갱신(제조 공장 사례, SIPP·PIBT 보장 범위, MAPF-DL, VDA 5050 3.0.0, LSMART)",
    "area_recent": "2026-10-10 — 27. 다중 로봇 경로·교통 관리 — MAPF: 5절 제조 공장 사례 추가, 6절 첫 문장 정정(SIPP는 단일 로봇 저수준 계획), 7·8절 보강, 11절 열린 질문 정리"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 공식 명세 본문. 2026-10-10 실행에서 3.0.0 태그 판을 열어 §2 범위, §6.4.3 구역 요청 통신, §6.8 예정 경로 공유를 확인했다(발표일 미기재).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-189",
      "org": "Okumura, K., Machida, M., Défago, X., & Tamura, Y.",
      "title": "Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding",
      "published": "2019-01",
      "url": "https://arxiv.org/abs/1901.11282",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "우선순위 상속·되돌림(PIBT)으로 반복형 MAPF 를 푸는 논문. 열람판은 Artificial Intelligence 게재판인 arXiv v5(2022-06-27, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19)다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-192",
      "org": "Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L.",
      "title": "A traffic management system for large and heterogeneous vehicles in narrow industrial environments",
      "published": "2026-09-09",
      "url": "https://arxiv.org/abs/2609.10400",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "NURBS 경로망 위 지속형 MAPF·경로 할당·교착 탐지·해소로 좁은 산업 현장의 이종 대형 AGV 를 조율하는 교통 관리 시스템. The International Journal of Robotics Research 2026 게재(DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-195",
      "org": "Phillips, M., & Likhachev, M.",
      "title": "SIPP: Safe interval path planning for dynamic environments",
      "published": "2011",
      "url": "https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "동적 장애물의 예측 궤적이 주어질 때 위치·안전 구간 상태로 로봇 한 대의 경로를 찾는 SIPP 를 제시한 ICRA 2011 논문(pp.5628–5635). 2026-10-10 실행에서 저자 연구실 PDF로 원문을 열람했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-199",
      "org": "Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J.",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10-28",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "지속형 MAPF 에 확장형 모방 학습(SILLM)을 적용한 ICRA 2025 채택 논문(arXiv v1 2024-10-28, v2 2025-05-18). 계산 벤치마크(최대 10,000 에이전트)와 실물 10대·가상 100대 모사 창고 검증, WPPL 비교 조건을 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-604",
      "org": "Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02-17",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "AGV 플릿 관리 시스템 안에서 MAPF 알고리즘을 실행 조건과 함께 평가하는 오픈소스 시뮬레이터 LSMART 와 설계 선택 비교 연구(프리프린트, 4-연결 격자 시뮬레이션, 실물 실험 없음).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-1513",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그 고정). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행·누적 지연 계산 수정이 기록돼 있다. 같은 URL 이 기존 id(ref-1458·ref-1487)로 등록돼 있으면 그 id 로 합친다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    },
    {
      "id": "ref-1514",
      "org": "Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S.",
      "title": "Multi-Agent Path Finding with Deadlines",
      "published": "2018",
      "url": "https://www.ijcai.org/proceedings/2018/0058.pdf",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58. 모든 에이전트에 공통 마감 하나를 두고 그 시점에 목표에 있는 에이전트 수를 최대화하는 MAPF-DL 을 정식화하고 NP-hard 증명과 흐름 환원 정수 계획법·탐색 해법을 냈다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가?",
      "areas": [
        27
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가?",
      "areas": [
        27,
        32
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시",
      "title": "27. 다중 로봇 경로·교통 관리 — MAPF"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시",
      "title": "27. 다중 로봇 경로·교통 관리 — MAPF"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시",
      "title": "27. 다중 로봇 경로·교통 관리 — MAPF"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시",
      "title": "27. 다중 로봇 경로·교통 관리 — MAPF"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시",
      "title": "27. 다중 로봇 경로·교통 관리 — MAPF"
    }
  ],
  "additional_research_requests": [
    "주제 페이지 docs/topics/2026/2026-09-25-area15-s6.md 의 본문 첫 문장('최적해를 보장하는 탐색(CBS·SIPP)')과 docs/topics/2026/2026-09-25-area15-s8.md 의 SILLM 항목('2024, 프리프린트')·Bonetti 외 '프리프린트' 표기는 이번 입력에 두 페이지 본문이 없어 직접 고치지 못했다. 세부영역 6·8절에 정정 내용을 실었으므로 다음 갱신 실행에서 두 주제 페이지 본문을 입력으로 받아 같은 정정을 반영해야 한다(차등 갱신 대상).",
    "5절 제조 공장 사례의 '완료·인계' 칸: Bonetti 외 시스템에서 팔레트 운반 완료를 무엇으로 확인하는지(포장기·보관 구역 인계 확인 방식)에 대한 근거가 브리프에 없어 '미확인'으로 두었다.",
    "f13 배치별 처리량 수치(배치 1 약 10·7·6%, 배치 2 약 11·7·10%)를 원문 §10.2.4(PDF)로 다시 확인해 [사실] 승격 여부를 판단해야 한다. 성과 지표 실행이 실물 운행인지 모사 실행인지 구분하는 근거도 함께 필요하다.",
    "ref-1513 과 같은 URL 의 기존 id(ref-1458·ref-1487, 2026-10-10-02·03 실행)가 게시돼 있는지 확인해 퍼블리셔가 하나로 합치도록 한다. 이번 입력의 docs_tree·참고문헌 색인 요약에서는 두 id 를 확인하지 못했다.",
    "트랙 반영 제안(2026-09-25-58, 건축 도면 자동 인식 단계 3: traffic-editor 플릿별 주행 그래프, VDA 5050 엣지 통과 조건, ODRM, 도면 차선 그래프를 경로망 자동 생성 입력 초안으로 두는 관점)을 6절에 반영하려면 해당 finding 을 이 영역 실행의 브리프에 다시 가져와 검증받아야 한다."
  ],
  "fixes_applied": [
    "6절 첫 문장 — CBS·PIBT·후처리 연구 문장에서 SIPP와 ref-195 를 빼 CBS(ref-187)를 최적 다중 에이전트 탐색으로 두고, SIPP를 주어진 동적 장애물(다른 로봇의 예정 궤적 포함) 궤적에 대한 단일 로봇 저수준 계획으로 분리한 둘째 문장과 'SIPP의 보장 범위' 소절(f1 [사실], f2 [추정], f3 [사실], f4 [의견])을 더했다.",
    "f13 — 처리량 '최대 약 11%'만 [사실]로 5절 표·서술에 두고, 배치별 수치는 5절 서술에 [추정]으로 강등해 '저자 보고이며 검증 단계에서 원문을 다시 확인하지 못한 값'을 병기했다.",
    "f18 — '주문 안의 긴 경로'를 '상태 메시지의 plannedPath(NURBS, 최소한 현재 베이스를 덮고 지날 nodeId를 담을 수 있음)'로 고쳐 7절에 썼다.",
    "5절 — 기존 물류창고 사례는 유지하고 '현장 유형: 제조 공장' 사례를 여섯 항목으로 더했다(작업 대상 f9, 수행 자원 f11, 제약 f10, 예외·성과 f6·f12·f13 강등 반영·f14, 시작 조건은 f12의 연속 작업 배정만). 완료·인계는 '미확인'으로 두고, 사례 머리 인용 블록에 업체 제공 배치를 모사한 세 배치 평가·그림 9 사진 한 장·업체 소속 공동저자(f8·f12)를 밝혔으며, site_matrix_updates 는 제조 공장의 실제로 채운 다섯 칸만 냈다.",
    "f6·f11 — Bonetti 외의 교착 탐지·경로 할당은 5절 사례 표와 6절 '교착 탐지·해소 모듈 (제조 공장 사례)' 소절에서만 쓰고, 5절 서술에 한 업체 관제 안의 기능이라 9절 책임 경계 근거로 쓰지 않는다고 적었으며 9절은 고치지 않았다.",
    "f24 — 모션 캡처 위치 추정과 ADG 실행 오차 제거는 8절 SILLM 항목의 '실험 조건' 설명으로만 썼다.",
    "ref-192 — 각주를 'The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09', 접근일 2026-10-10, 원문 미열람 표시 삭제로 고쳤고 reference_updates 에 같은 내용을 냈다. 8절 Bonetti 외 항목에 게재 정보를 적고, 주제 페이지의 '프리프린트' 표기는 6·8절 안내 문장으로 바로잡는다고 밝혔다(주제 페이지 본문 수정은 additional_research_requests).",
    "ref-199 — 각주 저자를 'Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J.'로, 'ICRA 2025 채택(arXiv v1 2024-10-28, v2 2025-05-18)'을 적고 접근일 2026-10-10, 원문 미열람 표시를 지웠다. 8절 SILLM 항목에서 계산 벤치마크 10,000과 실물 10대·가상 100대(초록·서론 기준)를 구분했다(f23·f26).",
    "ref-189 — 각주에 열람판 'arXiv v5 2022-06-27, Artificial Intelligence 게재판, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19'를 밝히고 접근일 2026-10-10, 원문 미열람 표시를 지웠다. PIBT 표기는 용어집의 '우선순위 상속·되돌림'으로 맞췄다.",
    "ref-195 — 각주 접근일을 2026-10-10으로 바꾸고 원문 미열람 표시를 지웠으며 'ICRA 2011, pp.5628–5635'를 병기했다.",
    "ref-031 — 7절 본문에 'VDA 5050 3.0.0 판(GitHub 3.0.0 태그 판, 확인일 2026-10-10)' 기준임을 밝히고 각주 접근일을 2026-10-10으로 바꿨으며 발표일은 쓰지 않았다(각주 발행일 '미확인' 유지).",
    "ref-1513 — 입력의 docs_tree·참고문헌 색인 요약에서 ref-1458·ref-1487 을 확인할 수 없어 페이지에는 브리프 id ref-1513 으로 적되, reference_updates 요약에 같은 URL 의 기존 id 로 합친다고 적어 퍼블리셔가 URL 기준으로 기존 id 에 합치게 했고 additional_research_requests 에 확인을 요청했다.",
    "ref-1514 — 'Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S., Multi-Agent Path Finding with Deadlines, IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58, https://www.ijcai.org/proceedings/2018/0058.pdf'로 각주와 reference_updates 에 등록했고, 6·11절에서 MAPF-DL 을 '모든 에이전트에 공통 마감 하나'로만 썼다.",
    "직접 인용 — ref-604 는 'solution quality and scalability' 한 구절만 원문으로 남기고, ref-192·ref-031 을 비롯한 나머지 출처는 영어 인용 없이 한국어로 다시 서술했다.",
    "11절 — 기존 '(신규 · …)' 질문 3건을 oq-057·oq-058·oq-059 id로 표기하고, oq-058 에 f33 [의견], oq-059 에 f34 [사실]을 부분 근거로 더해 둘 다 열림을 유지했으며, oq-032 에는 f21·f22 가 답하지 않는다고 적었다. 새 질문 2건(f7·f29 근거)을 11절과 open_question_updates 에 등록했다.",
    "트랙 반영 제안(2026-09-25-58, 건축 도면 자동 인식 단계 3, 6절 경로망 자동 생성 입력 초안)은 브리프에 근거 finding 이 없어 6절에 반영하지 않았고 changelog_entry 에 '근거 없음으로 미반영'을 적었다.",
    "정정 요청 — 이 영역에 걸린 정정 요청이 없음을 changelog_entry 에 '정정 요청 없음(처리할 corr id 없음)'으로 적었다.",
    "분량 초과 자동 분리: 27. 다중 로봇 경로·교통 관리 — MAPF 본문 10,713자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,692자"
  ]
}
```

### runs/2026-10-10-04/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (7개 절)
- 분량 초과 자동 분리:
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area27-s8.md (1,947자)
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-10-area27-s6.md (1,872자)
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area27-s11.md (1,370자)
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area27-s7.md (1,076자)
    - docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-10-area27-s10.md (848자)
```

### runs/2026-10-10-04/pages/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF"
type: area
category: "G. 계획·최적화"
area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [MAPF, 교통 관리, 교착, Open-RMF, VDA 5050]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-004, ref-005, ref-006, ref-031, ref-079, ref-253, ref-267, ref-268, ref-186, ref-187, ref-188, ref-189, ref-190, ref-191, ref-192, ref-193, ref-194, ref-195, ref-196, ref-197, ref-199, ref-604, ref-1513, ref-1514]
last_run: 2026-09-25
version: 3
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF

# 27. 다중 로봇 경로·교통 관리 — MAPF

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

여러 로봇이 같은 공간에서 서로 부딪히지 않는 경로와 통과 시점을 정하는 일은 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)로 연구되며, 목적마다 최적해를 계산하기 어려운 문제로 알려져 있다. [사실][^ref-186][^ref-190]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 왜 중요한가](../../topics/2026/2026-09-25-area15-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 기본 개념은 충돌 없는 경로 집합을 찾는 MAPF와, 현장에서 로봇이 달리는 경로망과 그 위의 교통 규칙을 표현하는 개념들이다. [사실][^ref-186][^ref-079]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 핵심 개념과 용어](../../topics/2026/2026-09-25-area15-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더하며, 2026-10-10 실행에서 아래 제조 공장 사례를 더했다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 구역의 좁은 통로에서 서로 다른 제조사의 보충 로봇과 피킹 운반 로봇이 마주침

| 항목 | 내용 |
|---|---|
| 시작 조건 | 피킹 운반 작업과 보충 작업이 비슷한 시각에 배정되어 두 로봇의 경로가 같은 좁은 통로를 지나게 된다(설명용 가정). |
| 작업 대상 | 해당 없음(이 영역은 화물보다 로봇의 이동과 통과 시점을 다룬다). |
| 수행 자원 | 제조사가 다른 두 로봇과 각 제조사 관제, 여러 플릿을 조율하는 ROP(설명용 가정). Open-RMF 기준으로 플릿은 제어 수준에 따라 경로 지시, 일시정지·재개, 상태 수신만 가능할 수 있고, 읽기 전용 플릿은 공유 공간마다 하나만 허용된다. [사실][^ref-004] |
| 제약 | 차선의 양방향 여부·방향 제약과 대기 지점 같은 경로망 속성 [사실][^ref-079], 해제된 노드·간선만 주행할 수 있다는 규칙과 해제 구역의 진입 요청·응답 [사실][^ref-031] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 지연이 쌓이면 행동 의존 그래프로 순서를 지키며 실행을 이어갈지 재계획할지를 판단해야 하며 [사실][^ref-188], 재계획 여부와 교착 해소 주체가 처리량을 좌우할 것으로 보인다. [추정][^ref-188][^ref-031][^ref-192] |

다음은 설명을 위한 가상의 시나리오이며, 확인된 현장 사례가 아니다. 이 영역은 여섯 항목 가운데 수행 자원·제약·예외·성과에 주로 관여한다.

두 로봇이 마주치는 상황은 대기 지점·차선 방향 같은 경로망 제약과 구역 진입 허가로 먼저 막고, 그래도 생기면 협상이나 일시정지로 한쪽을 대기시키는 순서로 다룰 수 있을 것으로 이 위키는 추정한다. [추정][^ref-079][^ref-031][^ref-004] Open-RMF에서는 충돌이 감지되면 관련 플릿이 선호 경로와 상대를 수용하는 경로를 내고 제3자 판정자가 조합을 고르는 협상을 한다. [사실][^ref-004]

### 제조 공장 사례

**현장 유형:** 제조 공장

**사례:** 생산라인 말단의 팔레타이징·보관·팔레트 포장 구역에서 이종 대형 AGV가 좁은 복도를 지나 팔레트를 나른다

> 이 사례는 Bonetti 외의 교통 관리 연구(The International Journal of Robotics Research 2026 게재)에서 가져왔다. 이 연구는 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발했고, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 소·중·대 규모 세 배치에서 했으며, 공동저자 가운데 업체 소속이 있다. [사실][^ref-192] 논문의 공장 실험 사진은 그림 9 한 장이고 그림 10–12는 업체 관제 소프트웨어의 2D 재구성 화면이다. [사실][^ref-192]

| 항목 | 내용 |
|---|---|
| 시작 조건 | 업체 관제 소프트웨어(TecnoFerrari Supervisor) 안에서 작업을 연속으로 배정하는 조건으로 시나리오마다 약 10시간 실행하며 성과 지표를 모았다. [사실][^ref-192] |
| 작업 대상 | 배치 1에서 AGV는 팔레타이저에서 포장기로 팔레트를 나르고, 포장기가 바쁘거나 쓸 수 없으면 임시 보관 구역으로 돌리며, 빈 팔레트를 디스펜서에서 받아 팔레타이저에 보충한다. [사실][^ref-192] |
| 수행 자원 | AGV 플릿과 업체 관제 소프트웨어. 교통 관리는 NURBS 곡선 경로망 위 지속형 MAPF(L-MAPF) 조율기(수정 Bounded Horizon CBS를 순환 지평 충돌 해소에 넣고 복도 구간에 시간 지평을 늘림), 조율된 궤적을 실행 중 안전하게 할당하는 경로 할당기, 교착 탐지·처리기를 결합해 업체 관제 소프트웨어에 C#으로 통합했다. [사실][^ref-192] |
| 제약 | 배치 1은 같은 등급 AGV가 복도 4개를 포함한 8개 구역의 좁은 비정형 공간을, 배치 2는 두 등급의 이종 AGV가 고밀도 중형 공간을, 배치 3은 이종 AGV가 좁은 양방향 복도가 없는 넓은 공간을 다니며, 논문 그림 10·11은 막다른 복도를 표시한다. [사실][^ref-192] |
| 완료·인계 | 미확인 |
| 예외·성과 | 작업 갱신 같은 예측 못 한 사건이나 시간 지평 부족으로 생기는 교착은 AGV 사이 선행 관계 그래프로 탐지해 관련 AGV의 경로를 갱신해 해소한다. [사실][^ref-192] 처리량은 비교 기준 대비 최대 약 11% 높았다고 저자가 보고한다. [사실][^ref-192] |

Bonetti 외는 업체가 배치한 규칙 기반 교통 관리, Pratissoli 외(2023)의 산업용 방법, 우선순위 기반 탐색(PBS)으로 바꾼 L-MAPF 변형과 비교해 처리량이 최대 약 11% 높았다고 보고한다. [사실][^ref-192] 배치별로는 배치 1에서 규칙 기반·Pratissoli 외·PBS 변형 대비 약 10·7·6%, 배치 2에서 약 11·7·10%로 보고되지만, 이는 저자 보고이며 검증 단계에서 원문을 다시 확인하지 못한 값이다. [추정][^ref-192]

배치별 수치는 업체가 제공한 실제 배치를 모사한 실행 결과로 제시되고 실제 운행은 사진 한 장으로만 보이며 업체 소속 공동저자가 있고 독립 재현은 확인하지 못했으므로, 이 위키는 처리량 최대 약 11%를 상용 공장 실측 개선율이나 다른 현장의 일반 개선율로 옮기지 않는다. [의견][^ref-192]

이 사례의 교착 탐지와 경로 할당은 한 업체 관제 안의 기능이다. 그래서 여러 제조사 플릿을 조율하는 ROP의 책임 경계(9절)를 정하는 근거로 쓰지 않고, 교통 관리 구성의 예로만 읽는다. 이 영역은 이 사례에서 수행 자원·제약·예외·성과에 주로 관여한다.

## 6. 대표 접근법과 기술

MAPF 해법은 여러 로봇의 경로를 함께 최적으로 찾는 충돌 기반 탐색(Conflict-Based Search, CBS)부터 대규모 반복 상황을 겨냥한 우선순위 상속·되돌림(Priority Inheritance with Backtracking, PIBT)까지 폭이 넓고, 계획을 실제 로봇 실행에 맞추는 후처리 연구가 함께 있다. [사실][^ref-187][^ref-189][^ref-196]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술](../../topics/2026/2026-10-10-area27-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

Open-RMF는 여러 플릿의 교통 스케줄과 협상을 구현하고, VDA 5050은 경로 해제와 구역 규칙을 정하되 경로 결정·우선순위 같은 교통 조율 전략은 규격 범위에서 뺀다. [사실][^ref-004][^ref-031]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area27-s7.md)에 있다.

## 8. 대표 연구와 자료

분류 원문이 참고 자료로 든 Li 외(2020)와 Ma 외(2017)는 각각 대규모 창고의 지속형 MAPF와 픽업·배송 작업이 온라인으로 들어오는 MAPD의 경로 계획을 다룬다. [사실][^ref-005][^ref-006] 아래 연구의 성능·순위 수치는 모두 단일 출처의 저자·팀 보고이며 이 위키가 확인한 성능이 아니다.

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료](../../topics/2026/2026-10-10-area27-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 위키는 ROP가 직접 맡을 교통 관리 범위를 여러 제조사 플릿에 걸친 공유 공간의 경로망·구역 단위 조율로 추정한다. [추정][^ref-031][^ref-004]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 제조사 플릿에 걸친 공유 공간의 경로 예약·해제(베이스 확장), 구역 진입 허가, 우선권과 교착 탐지·해소 [추정][^ref-031][^ref-004] | 연계 대상: 개별 로봇의 로컬 장애물 회피·주행 제어, 제조사 플릿 내부의 경로 계획 [추정][^ref-004][^ref-031] |

이 직접 범위는 VDA 5050이 관제 기능으로 두는 교착 탐지·해소·교통 제어와, Open-RMF가 교통 스케줄·협상으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-004]

연계 대상으로 보는 로컬 회피와 플릿 내부 경로 계획은 로봇·제조사 관제가 맡고, ROP는 제어 수준(Full Control·신호등·읽기 전용)에 따라 경로 지시·일시정지·상태 수신만 할 수 있는 것으로 이 위키는 추정한다(로컬 회피 책임을 명시한 문구는 이번에 확인한 문서 범위에서 찾지 못했다). [추정][^ref-004][^ref-031] 분류 원문 19장은 이종 제조사를 연결하는 ROP가 로컬 주행 기능을 「제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다」고 보며, 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 작업 배정, 공유 자원, 경로망과 지도, 제조사 관제 연동, 시뮬레이션, AI 영역과 이어지는 것으로 이 위키는 정리한다. [추정][^ref-006][^ref-079][^ref-267][^ref-004]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area27-s10.md)에 있다.

## 11. 열린 질문

**oq-032** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? — 부분 근거로 Open-RMF 문서는 신호등 수준 플릿은 일시정지·재개만 가능하고 공유 공간마다 읽기 전용 플릿을 하나만 허용한다고 적지만, 제어 수준별 교통 성능을 측정한 연구는 찾지 못해 열린 채로 둔다. [사실][^ref-004]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 열린 질문](../../topics/2026/2026-10-10-area27-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) — 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 트랙 반영 제안 2건(경로망 자동 설계)을 6·8절에 반영 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술](../../topics/2026/2026-09-25-area15-s6.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "6. 대표 접근법과 기술" 절(2,051자)을 옮겼다. 2차 수정: SIPP 가정 한계 문장을 [추정]으로 고쳐 썼다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료](../../topics/2026/2026-09-25-area15-s8.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "8. 대표 연구와 자료" 절(1,679자)을 옮겼다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area15-s7.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,155자)을 옮겼다. 형식 수정: 아직 참고문헌 페이지가 없는 ref-197·ref-191 링크를 텍스트 id 로 바꿨다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 핵심 개념과 용어](../../topics/2026/2026-09-25-area15-s4.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "4. 핵심 개념과 용어" 절(969자)을 옮겼다 (실행 2026-09-25-39)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-25 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-187]: Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R., Conflict-based search for optimal multi-agent pathfinding, 2015, https://dl.acm.org/doi/10.1016/j.artint.2014.11.006, 접근일 2026-09-25 (원문 미열람)
[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-189]: Okumura, K., Machida, M., Défago, X., & Tamura, Y., Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding (열람판 arXiv v5 2022-06-27, Artificial Intelligence 게재판, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19), 2019-01, https://arxiv.org/abs/1901.11282, 접근일 2026-10-10
[^ref-190]: Yu, J., & LaValle, S. M., Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity, 2015-07, https://arxiv.org/abs/1507.03289, 접근일 2026-09-25 (원문 미열람)
[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09), 2026-09-09, https://arxiv.org/abs/2609.10400, 접근일 2026-10-10
[^ref-196]: Ma, H., Koenig, S. 외, Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios, 2017-02, https://arxiv.org/abs/1702.05515, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF"
type: area
category: "G. 계획·최적화"
area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 55]
tags: [MAPF, 교통 관리, 교착, Open-RMF, VDA 5050]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-005, ref-006, ref-031, ref-079, ref-253, ref-267, ref-268, ref-186, ref-187, ref-188, ref-189, ref-190, ref-191, ref-192, ref-193, ref-194, ref-195, ref-196, ref-197, ref-199]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF

# 27. 다중 로봇 경로·교통 관리 — MAPF

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

여러 로봇이 같은 공간에서 서로 부딪히지 않는 경로와 통과 시점을 정하는 일은 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)로 연구되며, 목적마다 최적해를 계산하기 어려운 문제로 알려져 있다. [사실][^ref-186][^ref-190]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 왜 중요한가](../../topics/2026/2026-09-25-area15-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 기본 개념은 충돌 없는 경로 집합을 찾는 MAPF와, 현장에서 로봇이 달리는 경로망과 그 위의 교통 규칙을 표현하는 개념들이다. [사실][^ref-186][^ref-079]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 핵심 개념과 용어](../../topics/2026/2026-09-25-area15-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 구역의 좁은 통로에서 서로 다른 제조사의 보충 로봇과 피킹 운반 로봇이 마주침

| 항목 | 내용 |
|---|---|
| 시작 조건 | 피킹 운반 작업과 보충 작업이 비슷한 시각에 배정되어 두 로봇의 경로가 같은 좁은 통로를 지나게 된다(설명용 가정). |
| 작업 대상 | 해당 없음(이 영역은 화물보다 로봇의 이동과 통과 시점을 다룬다). |
| 수행 자원 | 제조사가 다른 두 로봇과 각 제조사 관제, 여러 플릿을 조율하는 ROP(설명용 가정). Open-RMF 기준으로 플릿은 제어 수준에 따라 경로 지시, 일시정지·재개, 상태 수신만 가능할 수 있고, 읽기 전용 플릿은 공유 공간마다 하나만 허용된다. [사실][^ref-004] |
| 제약 | 차선의 양방향 여부·방향 제약과 대기 지점 같은 경로망 속성 [사실][^ref-079], 해제된 노드·간선만 주행할 수 있다는 규칙과 해제 구역의 진입 요청·응답 [사실][^ref-031] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 지연이 쌓이면 행동 의존 그래프로 순서를 지키며 실행을 이어갈지 재계획할지를 판단해야 하며 [사실][^ref-188], 재계획 여부와 교착 해소 주체가 처리량을 좌우할 것으로 보인다. [추정][^ref-188][^ref-031][^ref-192] |

다음은 설명을 위한 가상의 시나리오이며, 확인된 현장 사례가 아니다. 이 영역은 여섯 항목 가운데 수행 자원·제약·예외·성과에 주로 관여한다.

두 로봇이 마주치는 상황은 대기 지점·차선 방향 같은 경로망 제약과 구역 진입 허가로 먼저 막고, 그래도 생기면 협상이나 일시정지로 한쪽을 대기시키는 순서로 다룰 수 있을 것으로 이 위키는 추정한다. [추정][^ref-079][^ref-031][^ref-004] Open-RMF에서는 충돌이 감지되면 관련 플릿이 선호 경로와 상대를 수용하는 경로를 내고 제3자 판정자가 조합을 고르는 협상을 한다. [사실][^ref-004]

## 6. 대표 접근법과 기술

MAPF 해법은 최적해를 보장하는 탐색(CBS·SIPP)부터 대규모 반복 상황을 겨냥한 방법(PIBT)까지 폭이 넓고, 계획을 실제 로봇 실행에 맞추는 후처리 연구가 함께 있다. [사실][^ref-187][^ref-195][^ref-189][^ref-196]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술](../../topics/2026/2026-09-25-area15-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

Open-RMF는 여러 플릿의 교통 스케줄과 협상을 구현하고, VDA 5050은 경로 해제와 구역 규칙을 정하되 경로 결정·우선순위 같은 교통 조율 전략은 규격 범위에서 뺀다. [사실][^ref-004][^ref-031]

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area15-s7.md)에 있다.

## 8. 대표 연구와 자료

분류 원문이 참고 자료로 든 Li 외(2020)와 Ma 외(2017)는 각각 대규모 창고의 지속형 MAPF와 픽업·배송 작업이 온라인으로 들어오는 MAPD의 경로 계획을 다룬다. [사실][^ref-005][^ref-006] 아래 연구의 성능·순위 수치는 모두 단일 출처의 저자·팀 보고이며 이 위키가 확인한 성능이 아니다.

자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료](../../topics/2026/2026-09-25-area15-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 위키는 ROP가 직접 맡을 교통 관리 범위를 여러 제조사 플릿에 걸친 공유 공간의 경로망·구역 단위 조율로 추정한다. [추정][^ref-031][^ref-004]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 제조사 플릿에 걸친 공유 공간의 경로 예약·해제(베이스 확장), 구역 진입 허가, 우선권과 교착 탐지·해소 [추정][^ref-031][^ref-004] | 연계 대상: 개별 로봇의 로컬 장애물 회피·주행 제어, 제조사 플릿 내부의 경로 계획 [추정][^ref-004][^ref-031] |

이 직접 범위는 VDA 5050이 관제 기능으로 두는 교착 탐지·해소·교통 제어와, Open-RMF가 교통 스케줄·협상으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-004]

연계 대상으로 보는 로컬 회피와 플릿 내부 경로 계획은 로봇·제조사 관제가 맡고, ROP는 제어 수준(Full Control·신호등·읽기 전용)에 따라 경로 지시·일시정지·상태 수신만 할 수 있는 것으로 이 위키는 추정한다(로컬 회피 책임을 명시한 문구는 이번에 확인한 문서 범위에서 찾지 못했다). [추정][^ref-004][^ref-031] 분류 원문 19장은 이종 제조사를 연결하는 ROP가 로컬 주행 기능을 「제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다」고 보며, 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 작업 배정, 공유 자원, 경로망과 지도, 제조사 관제 연동, 시뮬레이션, AI 영역과 이어지는 것으로 이 위키는 정리한다. [추정][^ref-006][^ref-079][^ref-267][^ref-004]

- [25. 작업 배정 — MRTA](task-allocation-mrta.md) — MAPD는 작업 배정과 충돌 없는 경로 계획을 함께 다루므로 두 영역이 맞물린다. [추정][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 충전소·대기 지점 같은 공유 자원이 경로망의 경유점 속성으로 표현된다. [추정][^ref-079]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) — 경로망·차선 그래프가 교통 관리의 공간 기반이다. [추정][^ref-079]
- [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 현장 도입 때 플릿별 경로망과 차선 속성을 설정한다. [추정][^ref-079]
- [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) — 플릿의 제어 수준이 ROP가 교통에 개입할 수 있는 범위를 정한다. [추정][^ref-004]
- [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md) — 경로망 설계를 평가하는 MAPF 시뮬레이션은 가정한 미래를 실험하므로 이 영역에 속하며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과는 구분한다. [추정][^ref-267]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 모방 학습을 적용한 지속형 MAPF 연구가 있어, 학습 기반 경로 계획은 이 영역과 47. AI·학습·적응과 모델 운영 양쪽에 연결한다. [사실][^ref-199]

## 11. 열린 질문

- **oq-032** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? — 부분 근거로 Open-RMF 문서는 신호등 수준 플릿은 일시정지·재개만 가능하고 공유 공간마다 읽기 전용 플릿을 하나만 허용한다고 적지만, 제어 수준별 교통 성능을 측정한 연구는 찾지 못해 열린 채로 둔다. [사실][^ref-004]
- (신규 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가?
- (신규 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가?
- (신규 · 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) — 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 트랙 반영 제안 2건(경로망 자동 설계)을 6·8절에 반영 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술](../../topics/2026/2026-09-25-area15-s6.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "6. 대표 접근법과 기술" 절(2,051자)을 옮겼다. 2차 수정: SIPP 가정 한계 문장을 [추정]으로 고쳐 썼다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료](../../topics/2026/2026-09-25-area15-s8.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "8. 대표 연구와 자료" 절(1,679자)을 옮겼다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area15-s7.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,155자)을 옮겼다. 형식 수정: 아직 참고문헌 페이지가 없는 ref-197·ref-191 링크를 텍스트 id 로 바꿨다 (실행 2026-09-25-39)
- 2026-09-25 · 생성 · [27. 다중 로봇 경로·교통 관리 — MAPF — 핵심 개념과 용어](../../topics/2026/2026-09-25-area15-s4.md) — 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "4. 핵심 개념과 용어" 절(969자)을 옮겼다 (실행 2026-09-25-39)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-25 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-187]: Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R., Conflict-based search for optimal multi-agent pathfinding, 2015, https://dl.acm.org/doi/10.1016/j.artint.2014.11.006, 접근일 2026-09-25 (원문 미열람)
[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-189]: Okumura, K., Machida, M., Défago, X., & Tamura, Y., Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding, 2019-01, https://arxiv.org/abs/1901.11282, 접근일 2026-09-25 (원문 미열람)
[^ref-190]: Yu, J., & LaValle, S. M., Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity, 2015-07, https://arxiv.org/abs/1507.03289, 접근일 2026-09-25 (원문 미열람)
[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments, 2026-09, https://arxiv.org/abs/2609.10400, 접근일 2026-09-25 (원문 미열람)
[^ref-195]: Phillips, M., & Likhachev, M. (ICRA 2011), SIPP: Safe interval path planning for dynamic environments, 2011, https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments, 접근일 2026-09-25 (원문 미열람)
[^ref-196]: Ma, H., Koenig, S. 외, Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios, 2017-02, https://arxiv.org/abs/1702.05515, 접근일 2026-09-25 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-10-04/pages/topics/2026/2026-10-10-area27-s8.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료"
type: topic
category: "G. 계획·최적화"
primary_area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-005, ref-006, ref-192, ref-199, ref-604]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#8
---

[홈](../../index.md) › [주제](../index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료

# 27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 분류 원문이 참고 자료로 든 Li 외(2020)와 Ma 외(2017)는 각각 대규모 창고의 지속형 MAPF와 픽업·배송 작업이 온라인으로 들어오는 MAPD의 경로 계획을 다룬다. [사실][^ref-005][^ref-006] 아래 연구의 성능·순위 수치는 모두 단일 출처의 저자·팀 보고이며 이 위키가 확인한 성능이 아니다.
- 이 페이지는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

분류 원문이 참고 자료로 든 Li 외(2020)와 Ma 외(2017)는 각각 대규모 창고의 지속형 MAPF와 픽업·배송 작업이 온라인으로 들어오는 MAPD의 경로 계획을 다룬다. [사실][^ref-005][^ref-006] 아래 연구의 성능·순위 수치는 모두 단일 출처의 저자·팀 보고이며 이 위키가 확인한 성능이 아니다.

주제 페이지(2026-09-25 기준)의 SILLM 항목('2024, 프리프린트')과 Bonetti 외 항목은 아래 내용으로 바로잡는다.

- Bonetti, A. 외, A traffic management system for large and heterogeneous vehicles in narrow industrial environments(The International Journal of Robotics Research 2026 게재, arXiv 2026-09-09) — 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발한 이종 대형 AGV 교통 관리 시스템이며, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치에서 했다. [사실][^ref-192] 사례와 성과 수치의 해석 한정은 5절 제조 공장 사례에 있다.
- Jiang, H. 외, Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding(SILLM, ICRA 2025 채택, arXiv 초판 2024-10-28, v2 2025-05-18) — 최대 10,000 에이전트의 6개 대형 지도 벤치마크와 별도로, 초록과 서론에서 실물 로봇 10대·가상 로봇 100대로 모사 창고에서 검증했다고 적는다. [사실][^ref-199] 실물 검증은 계획이 모든 에이전트 위치를 정확히 안다고 가정하므로 실물 로봇 위치를 외부 모션 캡처로 얻고, 교란·제어 오차로 생기는 실행 오차는 행동 의존 그래프(Action Dependency Graph, ADG)로 없앤 실험 조건이었다. [사실][^ref-199] 2023 League of Robot Runners 우승 해법 WPPL과의 비교는 다른 기준선에 맞추려고 회전 동작을 없애고, 단계당 계획 시간 1초 제한 대신 대규모 이웃 탐색 개선 반복을 40,000회로 제한한 조건이었다. [사실][^ref-199] 그래서 이 위키는 제목의 10,000을 실물 배치 대수가 아닌 계산 벤치마크 규모로, WPPL 비교를 원래 대회 조건의 재현이 아닌 바꾼 조건의 결과로 읽는다. [의견][^ref-199]
- Yan, J. 외, LSMART(Lifelong Scalable Multi-Agent Realistic Testbed, 2026-02-17 프리프린트) — 운동 제약·통신 지연·실행 불확실성·계획과 실행의 동시 진행·계획 실패 복구를 고려해 AGV 플릿 관리 시스템(Fleet Management System, FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터이며, 계획기·인스턴스 생성기·계획 호출 정책·실패 정책을 설계 선택으로 비교한다. [사실][^ref-604] 실험은 지도와 에이전트 수 조건마다 600초 시뮬레이션을 10회 돌려 평균과 95% 신뢰구간을 낸다. [사실][^ref-604] 재계획을 더 자주 하는 것은 모든 지도·밀도에서 유리하지 않았고(room-64-64-16과 낮은 밀도에서 이점이 일관되지 않음), 저자들은 ADG로 추정한 확정 지점이 실제 진행과 맞지 않는 실행–계획 불일치를 원인으로 든다. [사실][^ref-604] 더 정확한 로봇 모델과 더 강한 최적성 보장은 계획기의 확장성을 떨어뜨려, 저자들은 이를 계획기의 해 품질과 확장성(solution quality and scalability) 사이의 절충으로 설명한다. [사실][^ref-604] LSMART는 4-연결 격자 기반 시뮬레이션이고 논문에 실물 로봇 실험이 없으며, 저자들은 4-연결 격자를 넘는 그래프 지원을 향후 과제로 든다. [사실][^ref-604] 따라서 이종 제조사 로봇이 섞인 실물 창고에서의 개선율을 직접 제공하지는 않는 것으로 보인다. [추정][^ref-604]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-25 (원문 미열람)
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09), 2026-09-09, https://arxiv.org/abs/2609.10400, 접근일 2026-10-10
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J., Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (ICRA 2025 채택, arXiv v1 2024-10-28, v2 2025-05-18), 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-10
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-04 | 27. 다중 로봇 경로·교통 관리 — MAPF 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-10-04/pages/topics/2026/2026-10-10-area27-s6.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술"
type: topic
category: "G. 계획·최적화"
primary_area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-1514, ref-187, ref-189, ref-192, ref-195, ref-196]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#6
---

[홈](../../index.md) › [주제](../index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술

# 27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- MAPF 해법은 여러 로봇의 경로를 함께 최적으로 찾는 충돌 기반 탐색(Conflict-Based Search, CBS)부터 대규모 반복 상황을 겨냥한 우선순위 상속·되돌림(Priority Inheritance with Backtracking, PIBT)까지 폭이 넓고, 계획을 실제 로봇 실행에 맞추는 후처리 연구가 함께 있다. [사실][^ref-187][^ref-189][^ref-196]
- 이 페이지는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

MAPF 해법은 여러 로봇의 경로를 함께 최적으로 찾는 충돌 기반 탐색(Conflict-Based Search, CBS)부터 대규모 반복 상황을 겨냥한 우선순위 상속·되돌림(Priority Inheritance with Backtracking, PIBT)까지 폭이 넓고, 계획을 실제 로봇 실행에 맞추는 후처리 연구가 함께 있다. [사실][^ref-187][^ref-189][^ref-196] 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 이와 달리 다른 로봇의 예정 궤적 같은 동적 장애물의 예측 궤적이 주어졌다고 보고 로봇 한 대의 경로를 찾는 저수준 계획이다. [사실][^ref-195]

주제 페이지 본문(2026-09-25 기준)이 SIPP를 CBS와 함께 최적해를 보장하는 다중 로봇 탐색으로 묶은 서술은 아래 내용으로 바로잡는다.

### SIPP의 보장 범위

- Phillips·Likhachev(ICRA 2011)의 SIPP는 상태를 위치와 안전 구간의 쌍으로 묶어 로봇 한 대의 경로를 찾으며, 시간 차원을 더한 계획과 같은 최적성·완전성 보장을 준다고 밝힌다. [사실][^ref-195]
- 이 보장은 주어진 장애물 궤적에 대해 로봇 한 대의 시간 최소 경로를 찾는 범위의 결과이므로, 여러 로봇의 경로를 함께 정하는 MAPF 전체의 최적성 보장으로 옮길 수 없는 것으로 보인다. [추정][^ref-195][^ref-192]
- Bonetti 외(2026)는 우선순위 기반 탐색(Priority Based Search, PBS)·SIPP·베지에 곡선 최적화를 결합한 Yan·Li(2024)의 3단 다중 로봇 계획기가 우선순위 탐색에 기대므로 전역 최적성을 보장하지 않는다고 평가한다. 이는 SIPP가 상위 다중 로봇 조율 아래의 저수준 계획으로 쓰이는 예다. [사실][^ref-192]
- 그래서 이 위키는 SIPP를 최적해를 보장하는 다중 로봇 탐색으로 묶지 않고, 다른 로봇의 예정 궤적 같은 동적 장애물을 피하는 단일 로봇 저수준 경로 탐색으로 분리해 소개한다. [의견][^ref-195][^ref-192]

### PIBT의 보장 범위

- PIBT 논문(Artificial Intelligence 2022 게재판, 초판 IJCAI-19)은 PIBT가 MAPF에 대해 완전하지도 최적이지도 않다고 밝히고, 도달성은 모든 에이전트가 동시에 목표에 있음을 보장하지 않으므로 일반 MAPF에는 불완전하다고 설명한다. [사실][^ref-189]
- PIBT의 도달 보장은 그래프 조건과 지속형 설정을 전제로 하므로, 막다른 통로가 있는 실제 경로망에는 그 보장을 그대로 적용하지 말고 후퇴 공간과 별도 교착 탐지·해소 장치를 함께 확인해야 한다고 이 위키는 본다. [의견][^ref-189][^ref-192]

### 교착 탐지·해소 모듈 (제조 공장 사례)

- Bonetti 외는 작업 갱신 같은 예측 못 한 사건과, 시간 지평이 부족해 복도 밖 구역의 시공간 충돌을 다 풀지 못할 때 교착이 생긴다고 보고, AGV 사이 선행 관계 그래프로 순환·비순환(중첩) 교착을 탐지한 뒤 관련 AGV의 경로를 갱신해 해소하는 별도 모듈을 둔다. [사실][^ref-192] 이 모듈은 한 업체 관제 안의 기능이며, 사례는 5절 제조 공장 사례에 있다.

### 마감을 목적으로 하는 정식화

- Ma 외의 마감이 있는 다중 에이전트 경로 찾기(MAPF with Deadlines, MAPF-DL, IJCAI 2018)는 모든 에이전트에 공통 마감 하나를 두고 그 시점에 자기 목표 정점을 점유한 에이전트를 성공으로 보아, 충돌 없는 성공 에이전트 수를 최대화하는 문제로 정식화한다. 최적 풀이가 NP-hard임을 보이고 흐름 문제 환원 정수 계획법과 탐색 기반 해법을 낸다. [사실][^ref-1514]
- 이 목적함수는 도착 시각 합이나 전체 완료 시각(makespan)을 줄이는 일반 MAPF 목적과 달리 마감 안 성공 대수를 최대화하며, 교통 계획에 마감을 넣는 공개 정식화의 예다. [사실][^ref-1514]
- MAPF-DL은 모든 에이전트에 공통 마감 하나만 두므로, 작업별로 다른 출하 마감이나 업무 중요도를 이종 플릿의 통로 양보 규칙으로 바꾸는 산업 기준으로 볼 수는 없다고 이 위키는 본다. [의견][^ref-1514][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-1514]: Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S., Multi-Agent Path Finding with Deadlines (IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58), 2018, https://www.ijcai.org/proceedings/2018/0058.pdf, 접근일 2026-10-10
[^ref-187]: Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R., Conflict-based search for optimal multi-agent pathfinding, 2015, https://dl.acm.org/doi/10.1016/j.artint.2014.11.006, 접근일 2026-09-25 (원문 미열람)
[^ref-189]: Okumura, K., Machida, M., Défago, X., & Tamura, Y., Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding (열람판 arXiv v5 2022-06-27, Artificial Intelligence 게재판, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19), 2019-01, https://arxiv.org/abs/1901.11282, 접근일 2026-10-10
[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09), 2026-09-09, https://arxiv.org/abs/2609.10400, 접근일 2026-10-10
[^ref-195]: Phillips, M., & Likhachev, M., SIPP: Safe interval path planning for dynamic environments (ICRA 2011, pp.5628–5635), 2011, https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments, 접근일 2026-10-10
[^ref-196]: Ma, H., Koenig, S. 외, Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios, 2017-02, https://arxiv.org/abs/1702.05515, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-04 | 27. 다중 로봇 경로·교통 관리 — MAPF 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-04/pages/topics/2026/2026-10-10-area27-s11.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF — 열린 질문"
type: topic
category: "G. 계획·최적화"
primary_area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-004, ref-031, ref-1513, ref-1514, ref-199, ref-604]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#11
---

[홈](../../index.md) › [주제](../index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF — 열린 질문

# 27. 다중 로봇 경로·교통 관리 — MAPF — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-032** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? — 부분 근거로 Open-RMF 문서는 신호등 수준 플릿은 일시정지·재개만 가능하고 공유 공간마다 읽기 전용 플릿을 하나만 허용한다고 적지만, 제어 수준별 교통 성능을 측정한 연구는 찾지 못해 열린 채로 둔다. [사실][^ref-004]
- 이 페이지는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-032** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? — 부분 근거로 Open-RMF 문서는 신호등 수준 플릿은 일시정지·재개만 가능하고 공유 공간마다 읽기 전용 플릿을 하나만 허용한다고 적지만, 제어 수준별 교통 성능을 측정한 연구는 찾지 못해 열린 채로 둔다. [사실][^ref-004] 2026-10-10 실행에서 확인한 rmf_fleet_adapter 2.14.0 변경 이력(EasyTrafficLight 수정)은 관련 판 정보만 주며 제어 수준별 처리량 비교 실험이 아니므로 이 질문에 답하지 않는다고 이 위키는 본다. [의견][^ref-1513]
- **oq-057** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가?
- **oq-058** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? — 부분 근거로 SILLM의 실물 10대 모사 창고 검증과 LSMART의 실행 불확실성을 넣은 처리량 실험(8절)이 있지만, 벤치마크 개선율을 상용 물류센터 실측 개선율로 환산한 자료나 국내 사례는 확인하지 못해 정량 전이 질문은 열린 채로 둔다고 이 위키는 본다. [의견][^ref-199][^ref-604]
- **oq-059** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? — 부분 근거로 MAPF-DL은 공통 마감을 교통 계획의 목적함수에 넣는 정식화를 주지만 작업별 업무 우선순위를 통로 양보 우선권으로 바꾸는 규칙은 다루지 않고, VDA 5050 3.0.0도 우선순위·교착 해소 같은 교통 관리 로직을 범위에서 뺀다. [사실][^ref-1514][^ref-031]
- (신규 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-04) 막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가?
- (신규 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-04) 실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-1513]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-1514]: Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S., Multi-Agent Path Finding with Deadlines (IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58), 2018, https://www.ijcai.org/proceedings/2018/0058.pdf, 접근일 2026-10-10
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J., Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (ICRA 2025 채택, arXiv v1 2024-10-28, v2 2025-05-18), 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-10
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-04 | 27. 다중 로봇 경로·교통 관리 — MAPF 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-04/pages/topics/2026/2026-10-10-area27-s7.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 계획·최적화"
primary_area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-004, ref-031, ref-1513]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#7
---

[홈](../../index.md) › [주제](../index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스

# 27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF는 여러 플릿의 교통 스케줄과 협상을 구현하고, VDA 5050은 경로 해제와 구역 규칙을 정하되 경로 결정·우선순위 같은 교통 조율 전략은 규격 범위에서 뺀다. [사실][^ref-004][^ref-031]
- 이 페이지는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF는 여러 플릿의 교통 스케줄과 협상을 구현하고, VDA 5050은 경로 해제와 구역 규칙을 정하되 경로 결정·우선순위 같은 교통 조율 전략은 규격 범위에서 뺀다. [사실][^ref-004][^ref-031]

아래는 2026-10-10 실행에서 VDA 5050 3.0.0 판(GitHub 3.0.0 태그 판, 확인일 2026-10-10)과 Open-RMF 변경 이력으로 더한 내용이다.

### VDA 5050 3.0.0의 예정 경로 공유와 구역 요청

- VDA 5050 3.0.0 §6.8은 자유 주행 이동 로봇이 상태(state) 메시지로 관제에 예정 궤적을 알리게 한다. 상태 메시지의 plannedPath(NURBS, 최소한 현재 베이스를 덮고 지날 nodeId를 담을 수 있음)와, 센서로 볼 수 있는 가까운 경유점별 예상 도착 시각(Estimated Time of Arrival, ETA)을 담은 폴리라인 intermediatePath를 매 상태 메시지마다 공유하게 한다. [사실][^ref-031]
- 같은 판 §6.4.3은 로봇이 협조 재계획(COORDINATED_REPLANNING) 구역에 들어가거나 구역 안에서 경로를 바꿀 때 zoneRequest의 requestType을 REPLANNING으로 하고 예정 경로를 NURBS 궤적으로 실어 요청하게 하며, 응답을 제때 받지 못하면 구역에 들어가지 않게 한다. [사실][^ref-031]
- VDA 5050 3.0.0이 경로·우선순위·혼잡·교착 해소 같은 교통 관리 로직을 범위에서 빼므로, 예정 경로 공유·구역 요청 메시지의 상호운용성과 그 정보를 쓰는 현장 교통 최적화의 성능은 따로 검토해야 한다고 이 위키는 본다. [의견][^ref-031]

### Open-RMF 플릿 어댑터의 EasyTrafficLight 수정

- Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 EasyTrafficLight의 플릿 상태 발행 수정과 누적 지연 계산 수정을 기록한다. [사실][^ref-1513]
- Open-RMF의 신호등(일시정지·재개) 수준 연동을 비교·시험할 때는 제어 수준뿐 아니라 이 수정이 포함된 rmf_fleet_adapter 판도 기록해야 하며, 이 변경 이력은 수정의 존재를 보여 줄 뿐 제어 수준별 처리량 비교 실험은 아니라고 이 위키는 본다. [의견][^ref-1513]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-1513]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-04 | 27. 다중 로봇 경로·교통 관리 — MAPF 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-04/pages/topics/2026/2026-10-10-area27-s10.md

```markdown
---
title: "27. 다중 로봇 경로·교통 관리 — MAPF — 다른 연구영역과의 연결"
type: topic
category: "G. 계획·최적화"
primary_area_no: 27
related_areas: [15, 20, 25, 28, 34, 47, 54, 55, 62]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-004, ref-006, ref-079, ref-192, ref-199, ref-267, ref-604]
last_run: 2026-10-10
version: 1
split_from: docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#10
---

[홈](../../index.md) › [주제](../index.md) › 27. 다중 로봇 경로·교통 관리 — MAPF — 다른 연구영역과의 연결

# 27. 다중 로봇 경로·교통 관리 — MAPF — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 작업 배정, 공유 자원, 경로망과 지도, 제조사 관제 연동, 시뮬레이션, AI 영역과 이어지는 것으로 이 위키는 정리한다. [추정][^ref-006][^ref-079][^ref-267][^ref-004]
- 이 페이지는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 작업 배정, 공유 자원, 경로망과 지도, 제조사 관제 연동, 시뮬레이션, AI 영역과 이어지는 것으로 이 위키는 정리한다. [추정][^ref-006][^ref-079][^ref-267][^ref-004]

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — MAPD는 작업 배정과 충돌 없는 경로 계획을 함께 다루므로 두 영역이 맞물린다. [추정][^ref-006]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 충전소·대기 지점 같은 공유 자원이 경로망의 경유점 속성으로 표현된다. [추정][^ref-079]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 경로망·차선 그래프가 교통 관리의 공간 기반이다. [추정][^ref-079]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 현장 도입 때 플릿별 경로망과 차선 속성을 설정한다. [추정][^ref-079]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플릿의 제어 수준이 ROP가 교통에 개입할 수 있는 범위를 정한다. [추정][^ref-004]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 경로망 설계를 평가하는 MAPF 시뮬레이션은 가정한 미래를 실험하므로 이 영역에 속하며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과는 구분한다. [추정][^ref-267]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 모방 학습을 적용한 지속형 MAPF 연구가 있어, 학습 기반 경로 계획은 이 영역과 47. AI·학습·적응과 모델 운영 양쪽에 연결한다. [사실][^ref-199]

- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — LSMART는 플릿 관리 시스템 안에서 MAPF 알고리즘을 통신 지연·실행 불확실성 같은 실행 조건과 함께 평가하는 시뮬레이터여서, 교통 관리 알고리즘의 시험 방법이 두 영역을 잇는 것으로 보인다. [추정][^ref-604]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 5절의 제조 공장 사례(팔레타이징·보관·팔레트 포장 공장을 모사한 배치의 이종 대형 AGV 교통 관리)가 이 현장 유형의 교통 관리 적용 예가 되는 것으로 보인다. [추정][^ref-192]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09), 2026-09-09, https://arxiv.org/abs/2609.10400, 접근일 2026-10-10
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J., Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (ICRA 2025 채택, arXiv v1 2024-10-28, v2 2025-05-18), 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-10
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-04 | 27. 다중 로봇 경로·교통 관리 — MAPF 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1399건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | https://arxiv.org/abs/2005.07371 | 2026-09-24 | 아니오 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | https://arxiv.org/abs/1705.10868 | 2026-09-24 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | https://arxiv.org/abs/1906.08291 | 2026-09-25 | 아니오 |
| ref-187 | Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R. | Conflict-based search for optimal multi-agent pathfinding | 2015 | https://dl.acm.org/doi/10.1016/j.artint.2014.11.006 | 2026-09-25 | 아니오 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 2026-09-25 | 아니오 |
| ref-189 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 2019-01 | https://arxiv.org/abs/1901.11282 | 2026-09-25 | 아니오 |
| ref-190 | Yu, J., & LaValle, S. M. | Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity | 2015-07 | https://arxiv.org/abs/1507.03289 | 2026-09-25 | 아니오 |
| ref-191 | DiligentPanda (Team Pikachu, GitHub) | MAPF-LRR2023 — README (Team Pikachu's solution in the League of Robot Runners Competition 2023) | 미확인 | https://github.com/DiligentPanda/MAPF-LRR2023 | 2026-09-25 | 예 |
| ref-192 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 2026-09 | https://arxiv.org/abs/2609.10400 | 2026-09-25 | 아니오 |
| ref-193 | IEEE 게재 논문 저자(미확인) | Hierarchical Traffic Management of Multi-AGV Systems With Deadlock Prevention Applied to Industrial Environments | 2023 | https://ieeexplore.ieee.org/document/10132864/ | 2026-09-25 | 아니오 |
| ref-194 | 전진표, 강재호, 류광렬, 김갑환, 윤항묵(한국항해항만학회지) | 자동화 컨테이너 터미널에서 AGV 교착 방지와 회귀 분석을 이용한 경로 선정 방안 | 2005 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001130155 | 2026-09-25 | 아니오 |
| ref-195 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 2011 | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments | 2026-09-25 | 아니오 |
| ref-196 | Ma, H., Koenig, S. 외 | Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios | 2017-02 | https://arxiv.org/abs/1702.05515 | 2026-09-25 | 아니오 |
| ref-197 | Open Robotics (open-rmf) | rmf_traffic — README | 미확인 | https://github.com/open-rmf/rmf_traffic | 2026-09-25 | 예 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | https://arxiv.org/abs/2410.21415 | 2026-09-25 | 아니오 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 2026-09-25 | 아니오 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | https://ieeexplore.ieee.org/document/10287275/ | 2026-09-25 | 아니오 |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 2025-11 | https://arxiv.org/abs/2511.07175 | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [27] 에 걸린 8건 / 전체 348건)

```markdown
- oq-032 [열림] 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? (영역 20, 27)
- oq-057 [열림] VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가? (영역 20, 27)
- oq-058 [열림] 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (영역 27, 54)
- oq-059 [열림] 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? (영역 26, 27)
- oq-088 [열림] BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? (영역 27, 54)
- oq-298 [열림] 시간대별 사람 흐름을 담은 움직임 지도(maps of dynamics)를 ROP 의 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? (영역 16, 19, 27)
- oq-327 [열림] 시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가? (영역 19, 27, 18)
- oq-340 [열림] VDA 5050 해제 구역(RELEASE 구역)의 허가 만료 시각(leaseExpiry)과 허가 상실 시 동작(releaseLossBehavior)을 관제 장애·통신 단절 대책으로 쓸 때 만료 시간과 동작 값을 어떤 기준으로 정하는지 공개한 현장 사례나 지침이 있는가? (영역 42, 27)
```
