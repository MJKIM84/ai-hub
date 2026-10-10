(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- 세부영역 반영 제안: 1건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- retry_count: 1
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

### docs/categories/planning-and-optimization/index.md

````markdown
---
title: "G. 계획·최적화"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-005, ref-006, ref-004, ref-031, ref-051, ref-079, ref-090, ref-104, ref-105, ref-109, ref-117, ref-125, ref-132, ref-133, ref-134, ref-146, ref-168, ref-186, ref-188, ref-199, ref-228, ref-236, ref-237, ref-267, ref-286, ref-312, ref-376, ref-381, ref-385, ref-388, ref-398, ref-399, ref-401, ref-402, ref-403, ref-405, ref-531, ref-533, ref-493, ref-494]
---

[홈](../../index.md) › G. 계획·최적화

# G. 계획·최적화

## 핵심 질문

누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

## 개요

작업을 모델링·분해하고, 로봇에 배정하고, 순서·경로·공용 자원·충전을 최적화하는 결정 알고리즘. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **24. 작업·워크플로 모델링** | 현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 | 현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? | [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) | published |
| **25. 작업 배정 — MRTA** | 작업을 로봇 또는 로봇 팀에 배정한다 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? | [25. 작업 배정 — MRTA](task-allocation-mrta.md) | published |
| **26. 작업 순서·스케줄링** | 순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 | 일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? | [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) | published |
| **27. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로·통과 시점·우선권을 조율한다 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? | [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) | published |
| **28. 공용 자원·충전·에너지 최적화** | 공용 자원을 예약·배분하고 충전·에너지를 계획한다 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? | [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

로봇 운영에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 요청이 계속 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 D. 계획·최적화 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


D. 계획·최적화의 네 세부영역은 다른 대분류에서 주문·능력·지도·상태를 입력으로 받고, 결정한 배정·순서·경로·충전 계획을 실행 기반에 넘긴다. 아래 연결은 게시된 세부영역 페이지의 검증된 주장과, 이번 실행에서 공식 저장소 원문을 다시 연 자료(확인일 2026-09-25)에 기댄다. 연결 대부분은 단일 출처에 기대고 교차 확인되지 않았다. E. 협업·현장 운영, F. 도입·검증·유지관리, G. 안전·보안·지능·거버넌스의 세부영역 다수가 아직 심화되지 않아 그쪽 연결은 D. 계획·최적화 쪽 근거에 기댄다.

```mermaid
flowchart LR
  A[A. 업무·공급망 설계] -->|주문·시작 시각·우선순위| D[D. 계획·최적화]
  B[B. 공통 정보·환경 모델] -->|능력·경로망·배터리 상태| D
  D -->|배정·순서·경로·충전 결정| C[C. 연결·실행 기반]
  C -->|입찰·제어 수준·세션 제약| D
  D ---|사람 협업·인계·모니터링·예외 복구| E[E. 협업·현장 운영]
  F[F. 도입·검증·유지관리] -->|시뮬레이션·벤치마크·현장 설정| D
  G[G. 안전·보안·지능·거버넌스] -->|안전·보안·AI·표준 제약| D
```

### [옛 A. 업무·공급망 설계](../planning-and-business/index.md)

- **[25. 작업 배정 — MRTA](task-allocation-mrta.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: VDA 5050 명세(3.0.0 판)는 이동로봇에 대한 주문 배정을 관제(fleet control)의 기능으로 두면서, 주변 설비·인프라·외부 IT 시스템과의 인터페이스는 명세 범위에서 뺀다. [사실][^ref-031] 로봇 인터페이스 표준이 상위 시스템 연동을 범위 밖에 두고 Open-RMF 작업 요청에도 마감 필드가 없으므로, 배정의 입력인 주문·납기·출하 마감 제약은 창고 관리 시스템(Warehouse Management System, WMS) 같은 상위 업무 시스템에서 받아 ROP가 배정 기준으로 옮겨야 할 것으로 보인다. [추정][^ref-031][^ref-125] 납기·출하 마감을 정하는 일 자체는 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이며, 결합 방법은 [열린 질문](../../open-questions.md) oq-054 로 남아 있다.
- **[26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) ↔ 23. 업무 시스템 연동**: Open-RMF 작업 요청 스키마는 시각·순서 관련 필드로 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후를 지정하는 필드는 두지 않는다(2026-09-25 확인). [사실][^ref-125] 웨이브·웨이브리스 출고 지시 정책 연구(2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. [추정][^ref-134][^ref-133]
- **26. 작업 순서·스케줄링 ↔ [24. 작업·워크플로 모델링](task-and-workflow-modeling.md)**: B2MML 공통 스키마의 Dependency1Type 은 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등)을 표현하며, 창고 물류 작업에 적용한 사례는 확인되지 않았다(oq-013). [사실][^ref-117]
- **26. 작업 순서·스케줄링 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: 랙 이동 로봇 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는, 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. 이는 저자 계산 실험 조건의 보고값이며 독립 재현은 확인되지 않았다. [사실][^ref-381]
- **26. 작업 순서·스케줄링 ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 풋월 주문 통합 연구(2019)는 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다고 보아, 포장 작업자 대기가 순서 결정의 성과 지표로 이어진다(지표 정의는 oq-051). [사실][^ref-385]
- **[28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) ↔ 35. 처리능력·규모·배치 설계**: 충전 정책 연구(2024)와 창고 충전소 배치 최적화 연구(2024)가 있어, 충전 정책 결정이 충전기 수·위치 같은 설비 계획으로 이어지는 것으로 보인다. [추정][^ref-533][^ref-109]
- **28. 공용 자원·충전·에너지 최적화 ↔ 39. 운영 성과 측정·개선**: Omega 게재 연구(2024)는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. 이 값은 모델·시뮬레이션 조건의 저자 보고값으로 현장 실측이 아니며 독립 재현은 확인되지 않았다. [사실][^ref-146]

### [옛 B. 공통 정보·환경 모델](../robot-ontology/index.md)

- **25. 작업 배정 — MRTA ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026-08). [사실][^ref-236][^ref-237]
- **28. 공용 자원·충전·에너지 최적화 ↔ 5. 로봇 능력·작업 표현**: VDA 5050 팩트시트는 임계 저충전 수준(criticalLowChargingLevel)과 최소·최대 희망 충전 수준·최소 충전 시간을 로봇 선언으로 두고, Open-RMF 플릿 어댑터 템플릿은 운영 설정 recharge_threshold(예시값 0.10)와 충전 목표 recharge_soc(예시값 1.0)를 둔다(2026-09-25 확인). [사실][^ref-228][^ref-105] 두 값 가운데 무엇을 충전 하한으로 삼을지는 oq-068 로 남아 있다.
- **[27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: Open-RMF traffic-editor 는 차선의 양방향 여부와 대기 지점·충전소·주차 지점 같은 경유점 속성, 문·승강기를 주석하게 하고, 이 그래프를 building_map_generator 로 주행 그래프로 내보내 플릿 어댑터의 경로 계획에 쓰게 한다. [사실][^ref-079]
- **28. 공용 자원·충전·에너지 최적화 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Open-RMF 는 로봇이 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 시점 계획은 로봇이 보고하는 현재 배터리 상태를 입력으로 쓰며, 이 현재 상태 표현은 18. 실시간 세계 상태·데이터 일관성 쪽에 속하는 것으로 보인다. [추정][^ref-104][^ref-051] 이 연결은 현재 상태를 표현하는 쪽이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 연결(아래 F. 도입·검증·유지관리)과 구분한다.

### [옛 C. 연결·실행 기반](../integration/index.md)

- **25. 작업 배정 — MRTA ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: Open-RMF 디스패처는 작업 요청을 받으면 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리 가능한 플릿이 비용을 담은 입찰(BidProposal)을 내면 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. [사실][^ref-376] 작업 요청 스키마의 fleet_name 필드는 작업을 수행할 수 있는 플릿 이름(하나 또는 목록)을 지정해, 요청 단계에서 배정 후보 플릿을 제한할 수 있게 한다. [사실][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 는 플릿 연동을 전체 제어·신호등(일시정지·재개)·읽기 전용으로 나누고 공유 공간마다 읽기 전용 플릿을 최대 하나만 허용하며, 충돌이 나면 플릿들이 선호 경로와 상대를 수용하는 경로를 내고 시스템 통합사가 배치한 제3자 판정자가 조합을 고른다. [사실][^ref-004] VDA 5050 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 명세에서 빼면서도, 막힘 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 관제 기능으로 둔다. [사실][^ref-031]
- **28. 공용 자원·충전·에너지 최적화 ↔ 20. 로봇·제조사 관제 연동**: VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다는 것을 관제의 에너지 관리 기능으로 두고, 과충전 보호는 이동로봇의 책임으로 명시한다. [사실][^ref-031] 과충전 보호는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이며, ROP는 충전 시작·중지 요청과 상태 확인만 맡는다.
- **28. 공용 자원·충전·에너지 최적화 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: Open-RMF 승강기 요청은 요청자 사이에서 유일한 세션 id 로 승강기를 점유하고 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남으며, AGV 모드에서는 승강기가 정지해 있는 동안 문이 열린 채 유지된다. [사실][^ref-312][^ref-286] 승강기 운행과 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 승강기 세션 요청과 운영 모드 확인만 맡는다.
- **26. 작업 순서·스케줄링 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)**: Lott·Honary(2026-09, 프리프린트, 원문 미열람)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 등 통신 저하 조건에서 비교했다. [사실][^ref-493] 이 비교와 클라우드에 연결된 로봇·로봇그룹의 작업 계획을 다룬 국내 과제 보고서가 있어, 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 영역을 잇는 설계 쟁점이 될 것으로 보이나, 물류센터 적용 근거는 없다. [추정][^ref-493][^ref-401]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- **25. 작업 배정 — MRTA ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**: 작업자가 피킹하고 자율이동로봇이 운반하는 동적 주문 피킹 연구(2025)가 있어, 로봇 배정이 사람 작업자의 배치와 맞물린다. [사실][^ref-132]
- **26. 작업 순서·스케줄링 ↔ 31. 사람–로봇 협업**: 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구(2025)가 있다(결과 수치는 미확인). [사실][^ref-388]
- **26. 작업 순서·스케줄링 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: Open-RMF 배정이 플릿 단위 입찰로 이루어지고 작업 요청 스키마에 작업 간 선후 필드가 없으므로, 피킹 로봇 완료 뒤 운반 로봇 출발 같은 제조사 간 인계 선후는 ROP가 작업 흐름 수준에서 관리해야 할 것으로 보인다(oq-049). [추정][^ref-376][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: 창고 MAPF 실행 연구(2019)는 지연이 쌓일 때 행동 의존 그래프로 순서를 지키며 실행을 이어가는 방법을 다루어, 계획 유지와 재계획의 판단이 두 영역을 잇는다. [사실][^ref-188]
- **25. 작업 배정 — MRTA ↔ 32. 예외 복구·재계획·업무 연속성**: VDA 5050 에서 브로커 연결이 끊긴 로봇은 받은 주문 정보를 유지한 채 마지막으로 해제된 노드까지 주문을 수행하므로, 통신 단절 때 ROP가 다시 배정할 수 있는 몫은 아직 해제하지 않은 구간과 새 작업으로 한정될 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터는 위치 신뢰도와 작업 실행 행동 증거를 결합해 에이전트를 분류하므로, 실행 기록으로 이상 로봇을 가려 배정 입력에서 빼는 일이 모니터링과 배정을 잇는 지점이 될 것으로 보인다. 이 연구는 GPS 스푸핑 데이터와 택시 수요로 실험했으며 물류센터 적용은 확인되지 않았다. [추정][^ref-494]

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- **25. 작업 배정 — MRTA ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: 로봇 이동형 풀필먼트 시스템(2019)과 국내 자동물류센터의 이산 사건 시뮬레이션 연구가 배정 규칙을 가정한 미래에서 실험하는 도구로 쓰였고, 한 연구에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398][^ref-402]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 34. 시뮬레이션·예측용 디지털 트윈**: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(2024)가 있어, 경로망 설계 평가는 가정한 미래를 실험하는 쪽에 속하는 것으로 보인다. [추정][^ref-267]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: 현장 도입 때 플릿별 경로망과 차선 방향, 대기·충전·주차 경유점을 traffic-editor 로 주석해 설정하는 일이 온보딩 작업이 될 것으로 보인다. [추정][^ref-079]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: MAPF 연구는 정의·변형·벤치마크를 정리한 공통 틀(2019)을 가지고 있으나, 격자·단위 시간 가정의 벤치마크 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). [사실][^ref-186]
- **25. 작업 배정 — MRTA ↔ 54. 시험·형식 검증·벤치마크**: 분산 배정기를 같은 사례 묶음과 통신 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크(2026-09, 프리프린트)가 있어, 배정 방식 선택을 시험 조건과 함께 평가하는 틀이 된다. [사실][^ref-493]
- **28. 공용 자원·충전·에너지 최적화 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 일정을 정하는 연구(2026-03)가 있어, 충전·배정 계획이 배터리 열화 관리와 이어진다. [사실][^ref-403]

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- **28. 공용 자원·충전·에너지 최적화 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있고(설정은 사람·AGV 모드만 가능), Open-RMF 데모는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. [사실][^ref-286][^ref-104] 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 운영 모드를 확인해 계획에 반영하는 쪽을 맡는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 48. 안전·위험 관리**: VDA 5050 은 진입 금지·속도 제한·해제·우선·벌점 등 구역 유형을 교통 관리 수단으로 정의하면서, 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031] 따라서 이 연결은 교통 관리 수단과 안전 기능을 구분하는 지점으로만 다룬다.
- **25. 작업 배정 — MRTA ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 계획 정보와 실행을 어긋나게 하면 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선이 사라질 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안한다. 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않았다. [사실][^ref-494] Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 구성요소의 권한을 나누고, 웹 대시보드는 TLS 로 제공하며 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용한다고 설명한다. [사실][^ref-405] 작업 요청이 대시보드·API 서버를 거쳐 디스패처로 들어가고 배정이 플릿의 입찰 비용과 위치 보고에 기대므로, 누가 작업을 요청·우선 지정할 수 있는지와 입찰·위치 보고를 얼마나 믿을지가 배정의 보안 경계가 될 것으로 보인다. 창고 배정의 보안 사례는 찾지 못했다. [추정][^ref-405][^ref-376][^ref-494]
- **25. 작업 배정 — MRTA ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)**: 분류 개정 전 원문 8장의 교차 규칙은 학습 기반 배차를 25. 작업 배정 — MRTA에 적용되는 47. AI·학습·적응과 모델 운영의 연구 방법으로 둔다. 학습 기반 배차(이종 그래프 어텐션 스케줄러)와 대규모 언어 모델(Large Language Model, LLM) 기반 다중 로봇 작업 배정 연구가 있어 이 교차 규칙에 따라 두 영역이 이어진다. [사실][^ref-399][^ref-090][^ref-168] LLM 배정의 결과 수치는 출처가 충돌해(oq-030) 여기서 쓰지 않는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 47. AI·학습·적응과 모델 운영**: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있어, 학습 기반 경로 계획이 두 영역을 잇는다. [사실][^ref-199]
- **28. 공용 자원·충전·에너지 최적화 ↔ 47. AI·학습·적응과 모델 운영**: 자율 피킹 로봇의 충전소 선택·충전 시간 결정에 심층 강화학습을 쓰는 연구(2026-07)가 있어, 학습 기반 충전 결정이 두 영역을 잇는 것으로 보인다. [추정][^ref-531]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: VDA 5050 은 구역·경로 해제로 교통 규칙을 정하되 조율 전략은 빼고, Open-RMF 는 여러 플릿의 교통 협상에서 시스템 통합사가 배치한 판정자가 조합을 고르게 하므로, 한 현장에서 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-057). [추정][^ref-031][^ref-004]

### 아직 다루지 않은 연결

- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)과 D. 계획·최적화를 잇는 근거는 이번 조사에서 확보하지 못했다.
- 42. 분산 시스템·통신·컴퓨팅 구조, 38. 모니터링·이상 탐지·원인 분석, 51. 인증·권한·격리와의 연결은 물류센터 조건이 아닌 2026년 프리프린트 두 편에 기대므로, 물류 현장 근거가 나오면 다시 확인한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 108건이다(논문 66건 · 기사·보고서 0건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 40건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-493](../../references/ref-493.md) — Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation (발행 2026-09)
- [ref-192](../../references/ref-192.md) — Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (발행 2026-09)
- [ref-236](../../references/ref-236.md) — Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation (발행 2026-08-11)
- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-531](../../references/ref-531.md) — arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers (발행 2026-07)
- [ref-403](../../references/ref-403.md) — Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots (발행 2026-03)
- [ref-116](../../references/ref-116.md) — Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis (발행 2026-03)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-168](../../references/ref-168.md) — Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms (발행 2025-12)
- [ref-268](../../references/ref-268.md) — Rüdt, M., Enke, C., & Furmans, K. (KIT), Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) (발행 2025-11)
- 그 밖에 56건

**기사·보고서**

- 아직 없음

**업체 발표**

- [ref-219](../../references/ref-219.md) — Mobile Industrial Robots(MiR) (ManualsLib 게재본), MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) (발행 미확인)
- [ref-113](../../references/ref-113.md) — Camunda, Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-117](../../references/ref-117.md) — MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd (발행 2023)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-119](../../references/ref-119.md) — IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management (발행 2016)
- [ref-538](../../references/ref-538.md) — Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub) (발행 미확인)
- [ref-537](../../references/ref-537.md) — Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp (발행 미확인)
- [ref-536](../../references/ref-536.md) — Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp (발행 미확인)
- [ref-405](../../references/ref-405.md) — Open Robotics, Security - Programming Multiple Robots with ROS 2 (발행 미확인)
- [ref-404](../../references/ref-404.md) — Open Robotics (open-rmf), rmf_task — README (발행 미확인)
- [ref-401](../../references/ref-401.md) — KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 (발행 미확인)
- [ref-390](../../references/ref-390.md) — Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp (발행 미확인)
- 그 밖에 30건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [G. 계획·최적화](index.md) — '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 아직 다루지 않은 연결에 7. 화물·재고·자산 식별과 추적 명시), '참고 자료' 끝에 새 각주 정의 38건 추가 (실행 2026-09-25-55)
- 2026-09-25 · 요약 · [G. 계획·최적화](index.md) — D. 계획·최적화: '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 1차 수정 지시 14건 이행) (실행 2026-09-25-55)
- 2026-09-25 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-535 제목 원문 복원 (실행 2026-09-25-40)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [5]는 참고문헌 [ref-005](../../references/ref-005.md)에 해당한다.[^ref-005] 원문의 [6]은 참고문헌 [ref-006](../../references/ref-006.md)에 해당한다.[^ref-006]

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-09-25 (원문 미열람)
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-09-25 (원문 미열람)
````

### data/area_reflection_proposals.json (대상 영역 27. 다중 로봇 경로·교통 관리 — MAPF 에 대한 트랙 반영 제안 1건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-58",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 27,
      "section": "6. 대표 접근법과 기술",
      "summary": "traffic-editor 플릿별 주행 그래프(기본 9개)와 VDA 5050 엣지 통과 조건·관제 보유 통행 제한(f4·f7·f8), 방향 경로망 최적화 ODRM(f12), 도면 차선 그래프를 경로망 자동 생성의 입력 초안으로 두는 관점(추정, f18).",
      "status": "제안"
    }
  ]
}
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "17. 작업 대상·자산 식별과 인계 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
area_no: {{area_no}}                        # 1~67 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [18, 29, 30]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개. 예: [EPCIS, 인계 확인, 자산 추적]. 시드면 []
status: {{status}}                          # seed | draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여. 시드면 이 줄을 뺀다
created: {{created}}                        # YYYY-MM-DD. 페이지를 처음 만든 날
updated: {{updated}}                        # YYYY-MM-DD. 마지막으로 내용을 바꾼 날
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id. 예: [ref-003, ref-021]. 없으면 []
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜 YYYY-MM-DD. 시드면 이 줄을 뺀다
version: {{version}}                        # 정수. 시드 1, 갱신마다 +1
---
<!--
[템플릿] 세부 연구영역 페이지 (type: area)
경로: docs/categories/<대분류 slug>/<영역 slug>.md  (아래 경로 규약 표. 2026-09-28 개정부터 폴더·파일 이름에 대분류 문자·영역 번호를 붙이지 않는다)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석, C. 채팅 기반 구성·운영의 엔진 짝 주석), 1절 아래 "이 영역이 다루는 일(2026-09-28 리스트업 기준)" 목록(data/area_items.json)과 옛 영역에서 이어받은 경우의 계보 안내(data/area_lineage.json)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/<트랙 slug>/index.md(예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition) 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 67페이지(예: docs/categories/robot-ontology/robot-capability-and-task-representation.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 로봇 온톨로지):
!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 67페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]

{{area_items_block}}
<!--
첫 내용 줄: 분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않는다. 원문 주석(현재 원문)은 이 절이 아니라 2절의 인용 블록에 둔다.
{{area_items_block}}: 시드가 넣은 위키 문구를 그대로 둔다(pipeline/scaffold.py area_items_block). (1) "이 영역이 다루는 일(2026-09-28 리스트업 기준):" 과 그 아래 "- **일 이름**: 정의" 목록(data/area_items.json), (2) 옛 영역에서 일부를 이어받은 영역이면 계보 안내 문장(data/area_lineage.json), (3) 옛 영역 본문을 이어받은 영역이면 옛 영역 안내 문장과 옛 정의·질문·주석 인용 블록("> 옛 정의: … [옛 분류원문]", "> 옛 질문: … [옛 분류원문]", "> 옛 원문 주석: … [옛 분류원문]"). 옛 인용 블록은 보관한 옛 원문(_source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)과 글자 단위로 같아야 하며(protect_source.py check_tagged_lines), 이력 기록이므로 에이전트가 고치거나 새 문장을 [옛 분류원문] 으로 태그하지 않는다. 해당 내용이 없는 영역은 이 자리 표시 줄을 지운다.
이 절의 원문 문장과 옛 원문 인용은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. 핵심 질문

{{core_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 세부영역 표의 "핵심 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]". 수정 금지. (대분류 페이지의 핵심 질문과 다른 문장이다. 소속 대분류의 핵심 질문은 H1 아래 admonition 에 둔다.)
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 해당 영역(2026-09-28 원문 기준): 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 36. 가상 시운전·실제 상황 재현, 38. 모니터링·이상 탐지·원인 분석, 55. 현장 조사·설치·시운전. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14~16번의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석("매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번"), C. 채팅 기반 구성·운영의 엔진 짝 주석("맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번").
굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다. 문단이 여럿인 영역(예: 14. 도면·BIM에서 지도 만들기는 셋, 15. 지도·공간·위치 모델과 25. 작업 배정 — MRTA는 둘)은 인용 블록도 원문 순서대로 그 수만큼 둔다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다. 정확한 목록은 pipeline/lib/source.py 의 area_notes(번호)가 정한다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 ROP를 구현·운영할 때 무엇이 막히는지, 로봇 개별 성능과 업무 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 핵심 질문에서 출발한다. 특정 현장 유형(예: 물류창고)에만 해당하는 이야기로 좁히지 말고, 현장 유형에 따라 달라지는 점이 있으면 어느 현장 유형인지 밝힌다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "VDA 5050(독일자동차산업협회 무인운반차 인터페이스)", "WMS(Warehouse Management System, 창고 관리 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** {{site_types}}
<!-- 이 사례가 놓이는 현장 유형을 분류 원문 21장의 일곱 가지(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 가운데 하나로 명시한다. 예: "병원". 물류창고는 일곱 현장 유형 가운데 하나일 뿐이므로 기본값으로 쓰지 않고, 브리프 근거가 있는 현장 유형을 고른다. 물류창고 사례라면 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 중 어느 단계인지를 사례 제목이나 서술에 덧붙일 수 있다. -->

**사례:** {{case_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "병원에서 검체를 검사실로 운반", "제조 공장에서 공정 사이 부품 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
여섯 항목은 분류 원문 21장의 정의를 따른다. 시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가? / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가? / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가? / 제약: 시간·공간·적재량·설비·권한·안전 제약은 무엇인가? / 완료·인계: 무엇이 확인돼야 일이 끝났다고 인정하는가? / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?
표 아래에 1~3단락으로 사례를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 실제 도입 사례는 출처 각주와 함께 쓰고, 설명용 가상 사례이면 첫 문장에 밝힌다(예: "다음은 설명을 위한 가상의 사례이다."). 지어낸 현장 수치는 쓰지 않는다.
사례가 여럿이면 "**현장 유형:** … / **사례:** … / 여섯 항목 표 / 서술" 묶음을 사례마다 반복한다(서로 다른 현장 유형의 사례를 우선한다). 2026-09-28 개정 전에 쓴 물류창고 시나리오는 "현장 유형: 물류창고" 사례로 유지한다.
다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 함께 낸다(항목마다 site_type·item·link·title. 대분류는 퍼블리셔가 link 에서 정한다). 현장 유형 매트릭스 페이지: ../../site-matrix.md
-->

## 6. 대표 접근법과 기술

{{approaches}}
<!--
소제목(###)별로 접근법을 2~5개 정리한다. 각 접근법: 무엇을 해결하는가, 어떻게 동작하는가, 한계는 무엇인가. 주장마다 태그·각주.
벤더 제품의 기능·성능은 [추정]에 "벤더 주장"을 병기한다. 표·그림은 복제하지 않고 필요하면 mermaid 로 직접 그린다.
-->

## 7. 관련 표준·프레임워크·오픈소스

{{standards}}
<!--
표 형식: | 이름 | 유형(표준 / 오픈소스 / 평가 프로그램 / 프레임워크) | 이 영역과의 관계 | 출처 |. 각 행의 출처 칸에 각주.
표준·규격은 발행 기관의 공식 자료를 근거로 하고, 원문을 못 열었으면 "원문 미열람"을 표기한다. 대체·개정된 표준은 현재 버전을 확인해 기준일을 쓴다. 표준 목록 페이지(../../standards/index.md)와 용어집 링크를 함께 둔다.
-->

## 8. 대표 연구와 자료

{{key_research}}
<!--
목록 형식: "- 저자 또는 기관, 제목(연도) — 한두 문장 요약과 이 영역에서의 의미. [태그][^ref]". 3~8건. 학술 논문·표준·정부·연구기관 보고서를 우선하고 기사·벤더 문서는 보조로 둔다.
-->

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 현장 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 19장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장"(같은 대분류 E. 사물·사람·실시간 상태 안의 예). 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 L. AI·학습 기술의 해당 영역(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)을 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 영역이면 짝이 되는 엔진 영역(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 연결한다. 현장 유형별 요구·도입 사례는 Q. 현장 유형별 적용의 해당 영역(61. 물류창고 ~ 67. 기타 현장)을 연결한다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/<트랙 slug>/index.md. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/<트랙 slug>/question-backlog.md)로 링크만 둔다.
출처가 충돌한 주장, 확인하지 못한 수치, "분류 확장 제안"은 여기에 질문으로 올린다.
-->

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:area-recent:end -->
<!-- 퍼블리셔가 이 영역을 다룬 실행과 주제 페이지를 최신순으로 넣는다(날짜 | 실행 id | 변경 요약 | 페이지 링크). 스토리텔러는 마커 사이를 건드리지 않는다. -->

## 13. 참고 자료 (각주)

{{footnotes}}
<!--
각주 정의만 둔다. 형식: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"(공통 규칙 9). 본문에서 쓴 각주는 모두 여기에 정의하고, 정의만 있고 본문에 없는 각주는 지운다. 프런트매터 sources 와 일치시킨다.
시드 페이지는 2절 원문 주석의 [n] 에 대응하는 각주 정의만 둔다(없으면 "아직 작성되지 않음"). 각주 정의는 이 절에만 두고 [분류원문] 이 붙은 줄에는 붙이지 않는다.
-->
```

### templates/topic.md

```markdown
---
title: "{{title}}"                          # 주제 제목. 질문형 또는 명사구. 예: "로봇 도착과 작업 대상 인계 확인은 어떻게 다른가"
type: topic
category: "{{category}}"                    # 주 연구영역이 속한 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
primary_area_no: {{primary_area_no}}        # 주 연구영역 번호(1~67). 반드시 하나
track: {{track_slug}}                       # 트랙 실행에서 나온 주제 페이지만. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition. 아니면 이 줄을 뺀다
related_areas: [{{related_areas}}]          # 관련 영역 번호 0개 이상. 예: [18, 29]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개
status: {{status}}                          # draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜
version: {{version}}                        # 정수. 신규 1, 갱신마다 +1
---
<!--
[템플릿] 주제 페이지 (type: topic)
경로: docs/topics/YYYY/YYYY-MM-DD-slug.md  (YYYY-MM-DD 는 생성한 실행 날짜, slug 는 영문 소문자·하이픈)
쓰임: 파이프라인 2주기부터의 주제 조사 실행, 세부영역 페이지가 4,000자를 넘어 분리한 글, 트랙 실행에서 하나의 질문을 깊게 다룬 글. 하루 신규 주제 페이지 상한은 daily_budget.new_topic_pages 를 따른다.
필수: 주 연구영역 하나(primary_area_no)와 0개 이상의 관련 영역. 트랙 실행에서 나온 페이지는 프런트매터에 track 을 넣고, 해당 트랙 단계 페이지의 3절(조사 결과)에서 이 페이지를 링크한다.
분량: 1~7절 텍스트 합계(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 1,500~2,500자.
서사 골격: 왜 중요한가 → 현장에서 무슨 일이 벌어지는가(현장 유형을 밝힌 적용 사례) → 무엇이 알려져 있는가(검증된 사실) → ROP는 무엇을 맡고 무엇을 연계하는가 → 다른 영역과 어떻게 이어지는가 → 아직 모르는 것.
브리프의 발견 사항(finding)만 쓴다. 새 사실을 더하지 않는다. 필요한 사실이 브리프에 없으면 본문에 넣지 않고 pages.json 의 additional_research_requests 에 기록한다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 주제 목록은 ../index.md, 세부영역 페이지는 ../../categories/<대분류 slug>/<파일>, 대분류 페이지는 ../../categories/<대분류 slug>/index.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 트랙은 ../../tracks/<트랙 slug>/<파일>.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [주제](../index.md) › {{title}}

# {{title}}

**주 연구영역:** [{{primary_area_no}}. {{primary_area_name}}](../../categories/{{category_slug}}/{{area_file}}.md) · **관련 영역:** {{related_area_links_or_없음}} · **실행:** {{run_id}}
<!-- 관련 영역 링크는 "[18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)" 형식으로 쉼표 구분. 트랙 페이지면 "· **트랙:** [트랙 이름](../../tracks/<트랙 slug>/index.md) 단계 n" 을 덧붙인다(예: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)). -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 새 페이지에는 빈 마커 두 줄만 둔다. -->

## 1. 세 줄 요약

- {{summary_line_1}}
- {{summary_line_2}}
- {{summary_line_3}}
<!-- 정확히 세 줄. 각 줄은 한 문장. 첫 줄은 무엇을 밝혔는가, 둘째 줄은 ROP 운영에 무엇을 뜻하는가, 셋째 줄은 무엇이 아직 확인되지 않았는가. 요약에도 핵심 주장에는 태그를 붙인다. -->

## 2. 배경

{{background}}
<!--
어느 연구영역의 어떤 질문에서 출발했는지 쓴다. 주 연구영역의 원문 "핵심 질문"을 인용하면 그대로 옮기고 [분류원문] 을 붙인다. 출발점이 열린 질문(oq-NNN)이나 트랙 백로그 질문(q1-01), 정정 요청, priority.yaml 의 우선 주제이면 그 id 와 링크를 적는다. 1~2단락.
-->

## 3. 본문

### {{subheading_1}}

{{body_1}}

### {{subheading_2}}

{{body_2}}
<!--
소제목은 자유(2~5개). 주장마다 태그·각주. 검증된 발견 사항만 쓰고 순서는 서사 골격을 따른다. 출처가 충돌하면 둘 다 제시하고 7절 열린 질문에 올린다.
표·그림 복제 금지. 도식이 필요하면 mermaid 로 그리고 도식 안에서도 이름을 쓴다. 벤더 주장은 [추정]에 "벤더 주장" 병기. 조건부 승인의 수정 목록을 모두 반영하고 pages.json 의 fixes_applied 에 표시한다.
-->

## 4. 현장 시나리오

**현장 유형:** {{site_types}}

**사례:** {{case_title}}

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
절 제목 "4. 현장 시나리오"는 파이프라인(pipeline/lib/validate.py)이 쓰는 고정 문자열이므로 바꾸지 않는다. 내용은 분류 원문 21장의 방법대로 쓴다: 현장 유형(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 하나를 명시하고, 여섯 항목(시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가 / 수행 자원 / 제약 / 완료·인계 / 예외·성과)을 채운다. 물류창고는 일곱 현장 유형 가운데 하나이므로 기본값으로 쓰지 않는다. 이 주제와 직접 관련 없는 항목은 "해당 없음"으로 둔다. 실제 사례는 출처 각주와 함께, 설명용 가상 사례이면 첫 문장에 밝히고 지어낸 수치는 쓰지 않는다. 다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 낸다.
-->

## 5. ROP 관점의 시사점

**직접 범위:**
{{direct_scope_implications}}

**연계 범위:**
{{external_scope_implications}}
<!-- 분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 경계를 기준으로 ROP가 직접 맡는 것과 외부와 연계하는 것을 나누어 쓴다. 각 항목은 목록으로, 주장마다 태그·각주. 외부 연계 영역을 ROP 직접 범위처럼 쓰지 않는다. -->

## 6. 연결되는 연구영역

{{connected_areas}}
<!-- 목록 형식: "- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 연결 이유 한 문장". 주 연구영역을 첫 줄에, 관련 영역을 그 아래에. 번호와 이름을 함께 쓴다. 여기 적은 번호는 프런트매터 primary_area_no·related_areas 와 일치시킨다. AI를 다루면 27. AI·학습·적응과 모델 운영을 함께 연결한다. -->

## 7. 열린 질문

{{open_questions}}
<!-- 목록 형식: "- **oq-012** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 이 글에서 새로 생긴 질문과 답한(해결한) 질문을 나누어 적고, 해결한 질문에는 답이 있는 절을 표시한다. 트랙 질문(q1-01)은 트랙 백로그 링크만 둔다. pages.json 의 open_question_updates 로도 낸다. 없으면 "없음"과 이유. -->

## 8. 출처

{{footnotes}}
<!-- 각주 정의만 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". 본문의 각주와 프런트매터 sources 를 일치시킨다. 새 출처는 pages.json 의 reference_updates 로도 낸다. -->

## 9. 검증 노트

- 판정: 1차 {{first_verdict}} / 2차 {{second_verdict}}
- 확인·미확인: 확인 {{confirmed_count}}건 · 미확인 {{unconfirmed_count}}건 · 교차 확인 {{cross_checked_count}}건
- 강등된 주장: {{downgraded_claims_or_없음}}
- 검증자 주의: {{verification_note}}
- 신뢰도: {{confidence}}
<!-- 내용 검증 에이전트의 verification.json 에서 옮긴다. 판정 값: 1차 = 승인 | 조건부 승인 | 반려, 2차 = 통과 | 수정 후 재검증 | 불통과. 강등된 주장은 finding id 와 "사실 → 추정" 같은 변경을 적는다. "검증자 주의"는 verification_note 문구를 그대로 쓴다. 스토리텔러는 여기에 자기 의견을 넣지 않는다. -->

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| {{date}} | {{run_id}} | {{change_summary}} | {{version}} |
<!-- 신규 작성은 "신규 작성". 갱신마다 한 행을 위에 추가하고 프런트매터 version 을 올린다. 정정 요청을 반영했으면 corr-NNN id 를 적는다. -->
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

### docs/standards/index.md (요약: 341개 — 이름 · 종류 · 발행 기관)

```markdown
- SCOR (SCOR Digital Standard) · 표준 · ASCM(Association for Supply Chain Management)
- ISA-95 (ANSI/ISA-95) · 표준 · ISA(International Society of Automation)
- GS1 EPCIS · 표준 · GS1
- Open-RMF · 오픈소스 · Open Robotics
- ROS 2 DDS-Security (ROS 2 DDS-Security Integration) · 프레임워크 · ROS 2 Design
- ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) · 프레임워크 · ROS 2 Design
- NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) · 평가 프로그램 · NIST(National Institute of Standards and Technology)
- ARIAC · 평가 프로그램 · NIST
- GS1 EPCIS 2.0 (ISO/IEC 19987:2024) · ISO/IEC · GS1 · 표준
- GS1 CBV (Core Business Vocabulary) · GS1 · 표준
- SSCC (Serial Shipping Container Code) · GS1 · 표준
- GS1 Logistic Label Guideline · GS1 · 표준
- GRAI (Global Returnable Asset Identifier) · GS1 · 표준
- GIAI (Global Individual Asset Identifier) · GS1 · 표준
- EPC Tag Data Standard (1.11판) · GS1 · 표준
- VDA 5050 (2.0.0) · VDA(Verband der Automobilindustrie) · 표준
- OpenEPCIS · OpenEPCIS · 오픈소스
- IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) · IEEE · 표준
- IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology · IEEE · 표준
- W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) · W3C / OGC · 표준
- VDA 5050 (3.0.0) · VDA(Verband der Automobilindustrie) · 표준
- MassRobotics AMR Interoperability Standard (1.0) · MassRobotics · 표준
- OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) · OPC Foundation / VDMA · 표준
- Information Model for Capabilities, Skills & Services (CSS) · Plattform Industrie 4.0 · 프레임워크
- Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) · Auto-ID Labs Korea(세종대학교) · 오픈소스
- RAWSim-O · Merschformann, M. (RAWSim-O GitHub) · 오픈소스
- 스마트물류센터 인증제 · 한국교통연구원(인증스마트물류센터) · 평가 프로그램
- BPMN 2.0 (ISO/IEC 19510:2013) · OMG(Object Management Group) · ISO/IEC · 표준
- IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 · IEC / ISO · 표준
- B2MML (Business To Manufacturing Markup Language, 판 0701) · MESA International · 표준
- OCEL 2.0 (Object-Centric Event Log) · arXiv:2403.01975 저자(미확인) · 표준
- ISO 22400-2:2014 제조 운영 관리 KPI 정의 · ISO · 표준
- WERC DC Measures · WERC(Warehousing Education and Research Council) · 평가 프로그램
- PM4Py · Process Intelligence Solutions · 오픈소스
- OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) · OPC Foundation / ISA · 표준
- osmAG-from-cad (CAD-to-osmAG 파이프라인) · Zhang, J. (jiajiezhang7 GitHub) · 오픈소스
- Ogm2Pgbm · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- ifc2indoorgml · Diakité, A. A. 외 · 오픈소스
- IDTA 02020 Capability Description 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- CaSkMan · CaSkade-Automation (GitHub) · 오픈소스
- SOMA (Socio-physical Model of Activities) · EASE CRC · 오픈소스
- IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) · Helmut Schmidt University, Institute of Automation Technology · 오픈소스
- ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 · ISO · 표준
- KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- VDMA LIF (Layout Interchange Format) · VDMA · 표준
- IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) · buildingSMART · 표준
- Nav2 Docking Framework (nav2_docking) · ROS Navigation (Open Navigation) · 오픈소스
- IDTA 02020 Capability Description (AAS 서브모델 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 · ISO · 표준
- KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- SkiROS2 · RVMI lab, Aalborg University · 오픈소스
- LIF (Layout Interchange Format) 1.0.0 · VDMA · 표준
- ISO 21423 Industrial mobile robots — Communications and interoperability · ISO · 표준
- IFC 4.3 (IfcSpace) · buildingSMART International · 표준
- OGC IndoorGML 2.0 · OGC · 표준
- ISO 19164:2024 Indoor feature model · ISO · 표준
- GS1 GLN (Global Location Number) · GS1 · 표준
- REP 105 Coordinate Frames for Mobile Platforms · ROS (ros-infrastructure/rep) · 프레임워크
- ROSA (ROS Agent) · NASA Jet Propulsion Laboratory · 오픈소스
- RAI · Robotec.ai · 오픈소스
- free_fleet (Open-RMF 플릿 어댑터) · Open Robotics (open-rmf) · 오픈소스
- ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) · InOrbit · 오픈소스
- Open-RMF fleet_adapter_template · Open Robotics (open-rmf) · 오픈소스
- SLAM Toolbox · Macenski, S. (SteveMacenski GitHub) · 오픈소스
- ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) · Open Robotics (ROS 2 Documentation) · 오픈소스
- Eclipse Sparkplug (Chapter 5 Operational Behavior) · Eclipse Foundation · 표준
- OPC UA Part 4: Services (7.11 DataValue) · OPC Foundation · 표준
- ISO 23247 제조 디지털 트윈 프레임워크 · ISO (NIST 해설 경유) · 표준
- ROS 2 설계 문서 — ROS on DDS · QoS 정책 · ROS 2 Design · 프레임워크
- rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) · ROS 2 (ros2/rmw_zenoh) · 오픈소스
- KubeEdge · KubeEdge (CNCF) · 오픈소스
- Open-RMF rmf-web (대시보드·API 서버) · Open Robotics (open-rmf) · 오픈소스
- MQTT Version 5.0 · OASIS · 표준
- NIST SP 500-325 Fog Computing Conceptual Model · NIST · 프레임워크
- KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 · 산업통상자원부 국가기술표준원 · 표준
- Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) · Open Robotics (open-rmf) · 오픈소스
- KnowRob (하이브리드 지식 베이스) · KnowRob (knowrob GitHub) · 오픈소스
- IEEE1872-owl (CORA 공개 OWL 번역, 제3자) · srfiorini (IEEE1872-owl GitHub) · 오픈소스
- CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) · OGC · 표준
- IMDF (Indoor Mapping Data Format) 1.0.0 · OGC / Apple · 표준
- BOT (Building Topology Ontology) 0.3.2 · W3C Linked Building Data Community Group · 프레임워크
- ifcOWL · buildingSMART · 표준
- Brick Schema · Brick Consortium · 오픈소스
- ISO 16739-1:2024 (IFC 4.3) · ISO · 표준
- Rasa 폼(Forms, Rasa 3.x) · Rasa Technologies · 오픈소스
- ROS 2 액션 설계(Actions) · ROS 2 Design · 프레임워크
- ROS 2 관리형 노드 수명주기(Managed nodes) · ROS 2 Design · 프레임워크
- Open-RMF rmf_task · Open Robotics (open-rmf) · 오픈소스
- IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) · IETF HTTPAPI Working Group · 표준
- OPC UA Part 10: Programs (v1.04) · OPC Foundation · 표준
- ISA-TR88.00.02 Machine and Unit States (PackML) · ISA · 표준
- BehaviorTree.CPP · BehaviorTree (GitHub) · 오픈소스
- OR-Tools CP-SAT (스케줄링 레시피) · Google · 오픈소스
- Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) · Open Robotics (open-rmf) · 오픈소스
- rmf_task (Open-RMF 작업 계획기 TaskPlanner) · Open Robotics (open-rmf) · 오픈소스
- ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 · ISO · 표준
- 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) · National Institute of Building Sciences · 표준
- KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 · 국가표준인증통합정보시스템(KSSN) · 표준
- 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) · 한국건설기술연구원(건설CALS 체계) · 표준
- ezdxf (DXF 읽기·쓰기 라이브러리) · Moitzi, M. (mozman/ezdxf GitHub) · 오픈소스
- ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) · ECLASS e.V. · 표준
- IEC 공통 데이터 사전(IEC CDD) · IEC · 표준
- rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF Traffic Editor · Open Robotics · 오픈소스
- MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) · DiligentPanda (Team Pikachu, GitHub) · 오픈소스
- SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface · SEMI · 표준
- ASTM F3499-21 A-UGV 도킹 성능 시험 방법 · ASTM International · 표준
- ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 · ANSI / A3 · 표준
- KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 · 국가표준인증통합정보시스템(KSSN) · 표준
- Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_reservation (실험적 예약 라이브러리) · Open Robotics (open-rmf) · 오픈소스
- ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 · ISO · 표준
- ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) · ISO (A3 해설 경유) · 표준
- ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 · A3(Association for Advancing Automation) · 표준
- 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 · 고용노동부·한국산업안전보건공단 · 프레임워크
- 이동식 협동로봇 안전기준 KS(표준 번호 미확인) · 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) · 표준
- Open-RMF rmf_demos · Open Robotics (open-rmf) · 오픈소스
- IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) · IEC · 표준
- IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) · IDTA(Industrial Digital Twin Association) · 표준
- Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- ROS 2 diagnostics · ROS (ros/diagnostics GitHub) · 오픈소스
- ros2_tracing · ROS 2 (ros2/ros2_tracing GitHub) · 오픈소스
- OpenTelemetry Specification · OpenTelemetry (CNCF) · 오픈소스
- Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 경보 메시지(rmf_task_msgs Alert) · Open Robotics (open-rmf) · 오픈소스
- IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) · Oraskari, J. (jyrkioraskari GitHub) · 오픈소스
- SHACL (Shapes Constraint Language) · W3C · 표준
- IDS (Information Delivery Specification) · buildingSMART · 표준
- RMF Site Editor (rmf_site) · Open Robotics (open-rmf) · 오픈소스
- ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) · ISO · 표준
- 기업재난관리표준·재해경감 우수기업 인증제 · 행정안전부 · 평가 프로그램
- 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) · 고용노동부 · 프레임워크
- 보상 트랜잭션 패턴(Compensating Transaction pattern) · Microsoft (Azure Architecture Center) · 프레임워크
- Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) · Open Robotics (open-rmf) · 오픈소스
- IEEE 1872.1-2024 Standard for Robot Task Representation · IEEE Standards Association · 표준
- Serverless Workflow (Open Workflow Specification) DSL · CNCF Serverless Workflow · 오픈소스
- HDDL (Hierarchical Domain Definition Language) · Höller 외(IPC 2020 계층 계획 부문) · 프레임워크
- FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) · Pettinari, S. (UNICAM PROS) · 오픈소스
- ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 · ISO · 표준
- IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 · IEC / IEEE / ISO · 표준
- OmniDocBench (PDF 문서 파싱 벤치마크) · OpenDataLab · 오픈소스
- ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합 · ISO · 표준
- KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등) · 국가표준인증종합정보센터(KSSN) · 표준
- Open-RMF rmf_simulation (시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- OFacT (Open Factory Twin) · OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) · 오픈소스
- League of Robot Runners · League of Robot Runners (Amazon Robotics 후원) · 평가 프로그램
- ASTM F45 위원회(무인 자동 유도 산업 차량) · ASTM International (NIST 참여) · 표준
- KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 · 국가표준인증종합정보센터(KSSN) · 표준
- 한국로봇산업진흥원 로봇 시험평가 · 한국로봇산업진흥원(KIRIA) · 평가 프로그램
- ros2_fault_injection · reeceholland (GitHub) · 오픈소스
- ROSMonitoring · University of Liverpool Autonomy and Verification · 오픈소스
- LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) · Yan, J. 외(arXiv 2602.15721) · 오픈소스
- IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 17359:2018 기계 상태 감시·진단 일반 지침 · ISO · 표준
- ISO 55000:2024 자산 관리 — 용어·개요·원칙 · ISO (ISO/TC 251) · 표준
- IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 · IEC · 표준
- REP 2000 ROS 2 Releases and Target Platforms · Open Robotics (ROS REP) · 프레임워크
- rmf_simulation (Open-RMF 시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- 협동로봇 설치 작업장 안전인증 · 한국로봇사용자협회 · 평가 프로그램
- ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 · ISO (CEN EN ISO 12100:2010) · 표준
- KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 · 국가기술표준원(KSSN) · 표준
- Nav2 Route Server (nav2_route) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security · NIST · 프레임워크
- Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) · Eclipse Foundation · 오픈소스
- SROS 2 접근 제어 정책(ROS 2 Access Control Policies) · ROS 2 Design · 프레임워크
- ROS 2 보안 인클레이브(ROS 2 Security Enclaves) · ROS 2 Design · 프레임워크
- KISA 로봇 보안취약점 점검 체크리스트 해설서 · 한국인터넷진흥원(KISA) · 프레임워크
- NIST AI RMF 1.0 (NIST AI 100-1) · NIST · 프레임워크
- ISO/IEC 42001:2023 AI 관리 시스템 · ISO/IEC · 표준
- ISO/IEC 23894:2023 AI 위험관리 지침 · ISO/IEC · 표준
- MLflow 모델 레지스트리 · MLflow (Linux Foundation 오픈소스 프로젝트) · 오픈소스
- LoTa-Bench · lbaa2022 (LoTa-Bench 공식 저장소) · 오픈소스
- AmbiK 데이터셋 · cog-model (AmbiK 저자) · 오픈소스
- SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) · SISO(Simulation Interoperability Standards Organization) · 표준
- SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) · Rinciog, A. 외 (malerinc/slapstack GitHub) · 오픈소스
- Semantic Versioning 2.0.0 · Semantic Versioning (semver.org) · 프레임워크
- IETF RFC 9745 The Deprecation HTTP Response Header Field · IETF · 표준
- IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 · IEC · 표준
- ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 · ISO/IEC · 표준
- KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 · 한국지능형로봇표준포럼(KOROS) · 표준
- OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) · OPC Foundation · 평가 프로그램
- Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) · Open Robotics (open-rmf) · 오픈소스
- Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) · Rasa Technologies · 오픈소스
- nudged (2D 유사 변환 추정 라이브러리) · Palonen, A. (axelpale/nudged GitHub) · 오픈소스
- Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) · Rasa Technologies · 오픈소스
- IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) · IfcOpenShell · 오픈소스
- BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) · UK BIM Framework · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) · OWASP · 프레임워크
- Model Context Protocol 명세 2025-06-18 (Server Features: Tools) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- LangChain Human-in-the-loop 미들웨어 · LangChain · 오픈소스
- ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 · ISO · 표준
- ASTM F3244 Standard Test Method for Navigation: Defined Area · ASTM International · 표준
- SSIG (평면도 구조 유사도 지표) · van Engelenburg, C. 외 (caspervanengelenburg GitHub) · 오픈소스
- SLABIM (SLAM–BIM 결합 데이터셋) · HKUST Aerial Robotics Group · 오픈소스
- vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) · gpue (vda5050-sim GitHub, 개인 저장소) · 오픈소스
- vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) · coatyio · 오픈소스
- τ-bench (도구–에이전트–사용자 상호작용 벤치마크) · sierra-research · 평가 프로그램
- SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) · SafeAgentBench 저자(shengyin1224 공식 저장소) · 평가 프로그램
- JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) · JSON Schema (json-schema-org) · 표준
- VAL (PDDL 계획 검증 도구) · KCL-Planning · 오픈소스
- JSONSchemaBench · guidance-ai · 오픈소스
- Model Context Protocol 명세 2025-06-18 (Basic: Authorization) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 · NIST · 프레임워크
- RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) · therohangupta (RobotFleet 공식 저장소) · 오픈소스
- rosbag2 · ROS 2 (ros2/rosbag2 GitHub) · 오픈소스
- Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구) · Camargo, M., Dumas, M., & González-Rojas, O. · 오픈소스
- Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) · Open Robotics · 오픈소스
- VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) · Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) · 오픈소스
- EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) · 개인정보보호위원회 · 프레임워크
- 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 · 과학기술정보통신부·한국정보통신기술협회(TTA) · 프레임워크
- Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) · Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) · van Dam, H. G. W. · 오픈소스
- IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA-01002 Asset Administration Shell Specification — API (3.2.0) · IDTA(Industrial Digital Twin Association) · 표준
- RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 평가 프로그램
- CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) · CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) · 오픈소스
- OWL 2 Web Ontology Language Structural Specification (Second Edition) · W3C · 표준
- IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 · IDTA(Industrial Digital Twin Association) · 표준
- KGCL (Knowledge Graph Change Language) · Hegde, H. 외 (Database, Oxford) · 프레임워크
- ISO 13482 (서비스 로봇 안전 요구사항) · ISO · 표준
- RoMi-H (Robotic Middleware for Healthcare) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 오픈소스
- 서비스로봇 실증사업 · 한국로봇산업진흥원 · 평가 프로그램
- 스마트병원 선도모델(9개 모듈) · 한국보건산업진흥원 스마트병원 확산지원센터 · 프레임워크
- 로봇 친화형 건축물 인증 · 스마트도시협회 · 평가 프로그램
- Matter 1.2 (로봇청소기 장치 유형 포함) · Connectivity Standards Alliance (CSA) · 표준
- 실외이동로봇 운행안전인증 (지능형로봇법 제40조의2) · 한국로봇산업진흥원 · 평가 프로그램
- ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm · ISO (ISO/TC 204) · 표준
- ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중) · ISO/TC 204 · 표준
- Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도) · Open Navigation (Nav2) · 오픈소스
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
- ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) · ISO (ISO/TC 299 Robotics) · 표준
- ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) · ISO (ISO/TC 178 Lifts, escalators and moving walks) · 표준
- 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 · 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) · 표준
- Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_obstacle (사람 검출·lane_blocker) · Open Robotics (open-rmf) · 오픈소스
- Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) · Pasch, F. 외 (Intel Labs 외) · 오픈소스
- RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) · Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. · 프레임워크
- ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 · ISO · 표준
- IEEE 7001-2021 자율 시스템 투명성 표준 · IEEE Standards Association · 표준
- W3C Trace Context (traceparent·tracestate, 권고안 2021-11-23) · W3C · 표준
- EU AI Act 제19조 자동 생성 로그 (Article 19) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 (설명서 언어·원본·번역 표기) · European Parliament and Council (legislation.gov.uk 게재본) · 프레임워크
- MMLongBench-Doc (긴 문서 이해 벤치마크) · Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- NVIDIA Isaac Mission Dispatch · NVIDIA (nvidia-isaac) · 오픈소스
- NVIDIA Isaac Mission Control · NVIDIA (nvidia-isaac) · 오픈소스
- PlanSys2 (ROS 2 Planning System) · PlanSys2 프로젝트 · 오픈소스
- crossflow · Open Robotics (open-rmf) · 오픈소스
- Open BIM Object standard (OBOS) V1.0 · Construction Information Limited (Masterspec, 뉴질랜드) · 표준
- W3C SKOS (Simple Knowledge Organization System) Reference · W3C · 표준
```

### runs/2026-10-10-04/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/simulator.md
about/what-is-rop.md
categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md
categories/ai-and-learning/document-drawing-and-scene-understanding.md
categories/ai-and-learning/index.md
categories/ai-and-learning/prediction-and-learning-based-optimization.md
categories/ai-and-learning/robot-foundation-models-and-llm-planning.md
categories/chat-based-configuration-and-operation/chat-map-authoring.md
categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md
categories/chat-based-configuration-and-operation/chat-robot-configuration.md
categories/chat-based-configuration-and-operation/chat-scenario-composition.md
categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md
categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md
categories/chat-based-configuration-and-operation/index.md
categories/design-and-simulation/capacity-sizing-and-layout-design.md
categories/design-and-simulation/index.md
categories/design-and-simulation/scenario-model-and-editing.md
categories/design-and-simulation/simulation-and-predictive-digital-twin.md
categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md
categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md
categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md
categories/execution-collaboration-and-recovery/human-robot-collaboration.md
categories/execution-collaboration-and-recovery/index.md
categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md
categories/field-operations-and-monitoring/control-screen-and-execution-records.md
categories/field-operations-and-monitoring/index.md
categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md
categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md
categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md
categories/governance-law-and-society/index.md
categories/governance-law-and-society/labor-acceptance-and-accessibility.md
categories/governance-law-and-society/law-regulation-insurance-and-licensing.md
categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md
categories/integration/business-system-integration.md
categories/integration/facility-and-building-system-integration.md
categories/integration/index.md
categories/integration/interoperability-standards-and-conformance.md
categories/integration/robot-and-vendor-fleet-manager-integration.md
categories/objects-people-and-live-state/index.md
categories/objects-people-and-live-state/people-and-pedestrian-model.md
categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md
categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md
categories/planning-and-business/economics-procurement-and-business-models.md
categories/planning-and-business/index.md
categories/planning-and-business/technology-market-and-vendor-trends.md
categories/planning-and-business/use-cases-requirements-and-scope.md
categories/planning-and-optimization/index.md
categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md
categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md
categories/planning-and-optimization/task-allocation-mrta.md
categories/planning-and-optimization/task-and-workflow-modeling.md
categories/planning-and-optimization/task-sequencing-and-scheduling.md
categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md
categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md
categories/platform-architecture-and-infrastructure/index.md
categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md
categories/robot-ontology/heterogeneous-robot-registration.md
categories/robot-ontology/index.md
categories/robot-ontology/ontology-based-system-and-robot-integration.md
categories/robot-ontology/ontology-verification-and-change-management.md
categories/robot-ontology/robot-capability-and-task-representation.md
categories/safety/human-proximity-safety.md
categories/safety/index.md
categories/safety/safety-and-risk-management.md
categories/safety/safety-standards-certification-and-incident-investigation.md
categories/security-and-privacy/authentication-authorization-and-isolation.md
categories/security-and-privacy/communication-protection-threat-management-and-audit.md
categories/security-and-privacy/index.md
categories/security-and-privacy/privacy-and-video-data.md
categories/site-type-applications/commercial-facilities.md
categories/site-type-applications/home-and-apartment.md
categories/site-type-applications/hospital-and-healthcare.md
categories/site-type-applications/index.md
categories/site-type-applications/manufacturing-plant.md
categories/site-type-applications/other-sites.md
categories/site-type-applications/outdoor.md
categories/site-type-applications/warehouse.md
categories/space-and-map-model/index.md
categories/space-and-map-model/map-space-and-location-model.md
categories/space-and-map-model/maps-from-floor-plans-and-bim.md
categories/space-and-map-model/place-semantics-and-map-management.md
categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md
categories/verification-deployment-and-lifecycle/index.md
categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md
categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md
categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md
changelog.md
corrections.md
glossary/3d-scene-graph.md
glossary/4d-scene-graph.md
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/abstract-and-concrete-scenario.md
glossary/action-dependency-graph.md
glossary/action-status.md
glossary/actively-exploited-vulnerability.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/alert-tier.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-recording-of-events.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/average-displacement-error.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-element-proxy.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/buildingsmart-data-dictionary.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-description-submodel.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/cell-based-production.md
glossary/clarification-question.md
glossary/cloud-robotics.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/competency-question.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/connection-state.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/data-provenance.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/domain-shift.md
glossary/door-to-door-robot-delivery.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/generalized-voronoi-graph.md
glossary/giai.md
glossary/gln-extension-component.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/integrity-risk.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/it-ot-convergence.md
glossary/jailbreak.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lease-expiry.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic-on-finite-traces.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/management-of-change.md
glossary/map-alignment.md
glossary/map-distribution.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
glossary/mqtt-quality-of-service-level.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/oauth2-client-credentials-grant.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/online-simulation.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry-genai-semantic-conventions.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/operational-state.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/original-instructions.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/persistence-filter.md
glossary/personal-delivery-device.md
glossary/phased-rollout.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/precision-time-protocol.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-attestation.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-tracing.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/safety-guardrail.md
glossary/safety-state-report.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/skos.md
glossary/slot-filling.md
glossary/slotcar.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/state-script.md
glossary/stpa.md
glossary/strict-schema.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/surrogate-model.md
glossary/synchronization-loss.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/task-dependency-graph.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/trace-context.md
glossary/transparency-level-ieee-7001.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-defined-property-set.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050-hibernation.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/wireless-safety-rated-emergency-stop.md
glossary/workflow-diagram.md
glossary/workflow-net.md
glossary/zone-set.md
glossary/zones-and-conduits.md
ideas/chat-based-configuration-and-operation.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/daily/2026-09-26.md
logs/daily/2026-09-29.md
logs/daily/2026-09-30.md
logs/daily/2026-10-09.md
logs/index.md
logs/weekly/2026-W39.md
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
references/ref-046.md
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
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
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
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-1239.md
references/ref-124.md
references/ref-1240.md
references/ref-1241.md
references/ref-1242.md
references/ref-1243.md
references/ref-1244.md
references/ref-1245.md
references/ref-1246.md
references/ref-1247.md
references/ref-1248.md
references/ref-1249.md
references/ref-125.md
references/ref-1250.md
references/ref-1251.md
references/ref-1252.md
references/ref-1253.md
references/ref-1254.md
references/ref-1255.md
references/ref-1256.md
references/ref-1257.md
references/ref-1258.md
references/ref-1259.md
references/ref-126.md
references/ref-1260.md
references/ref-1261.md
references/ref-1262.md
references/ref-1263.md
references/ref-1264.md
references/ref-1265.md
references/ref-1266.md
references/ref-1267.md
references/ref-1268.md
references/ref-1269.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-1272.md
references/ref-1273.md
references/ref-1274.md
references/ref-1275.md
references/ref-1276.md
references/ref-1277.md
references/ref-1278.md
references/ref-1279.md
references/ref-128.md
references/ref-1280.md
references/ref-1281.md
references/ref-1282.md
references/ref-1283.md
references/ref-1284.md
references/ref-1285.md
references/ref-1286.md
references/ref-1287.md
references/ref-1288.md
references/ref-1289.md
references/ref-129.md
references/ref-1290.md
references/ref-1291.md
references/ref-1292.md
references/ref-1293.md
references/ref-1294.md
references/ref-1295.md
references/ref-1296.md
references/ref-1297.md
references/ref-1298.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-1303.md
references/ref-1304.md
references/ref-1305.md
references/ref-1306.md
references/ref-1307.md
references/ref-1308.md
references/ref-1309.md
references/ref-131.md
references/ref-1310.md
references/ref-1311.md
references/ref-1312.md
references/ref-1313.md
references/ref-1314.md
references/ref-1315.md
references/ref-1316.md
references/ref-1317.md
references/ref-1318.md
references/ref-1319.md
references/ref-132.md
references/ref-1320.md
references/ref-1321.md
references/ref-1322.md
references/ref-1323.md
references/ref-1324.md
references/ref-1325.md
references/ref-1326.md
references/ref-1327.md
references/ref-1328.md
references/ref-1329.md
references/ref-133.md
references/ref-1330.md
references/ref-1331.md
references/ref-1332.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
references/ref-1337.md
references/ref-1338.md
references/ref-1339.md
references/ref-134.md
references/ref-1340.md
references/ref-1341.md
references/ref-1342.md
references/ref-1343.md
references/ref-1344.md
references/ref-1345.md
references/ref-1346.md
references/ref-1347.md
references/ref-1348.md
references/ref-1349.md
references/ref-135.md
references/ref-1350.md
references/ref-1351.md
references/ref-1352.md
references/ref-1353.md
references/ref-1354.md
references/ref-1355.md
references/ref-1356.md
references/ref-1357.md
references/ref-1358.md
references/ref-1359.md
references/ref-136.md
references/ref-1360.md
references/ref-1361.md
references/ref-1362.md
references/ref-1363.md
references/ref-1364.md
references/ref-1365.md
references/ref-1366.md
references/ref-1367.md
references/ref-1368.md
references/ref-1369.md
references/ref-137.md
references/ref-1370.md
references/ref-1371.md
references/ref-1372.md
references/ref-1373.md
references/ref-1374.md
references/ref-1375.md
references/ref-1376.md
references/ref-1377.md
references/ref-1378.md
references/ref-1379.md
references/ref-138.md
references/ref-1380.md
references/ref-1381.md
references/ref-1382.md
references/ref-1383.md
references/ref-1384.md
references/ref-1385.md
references/ref-1386.md
references/ref-1387.md
references/ref-1388.md
references/ref-1389.md
references/ref-139.md
references/ref-1390.md
references/ref-1391.md
references/ref-1392.md
references/ref-1393.md
references/ref-1394.md
references/ref-1395.md
references/ref-1396.md
references/ref-1397.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-1421.md
references/ref-1422.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-493.md
references/ref-494.md
references/ref-495.md
references/ref-496.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-500.md
references/ref-501.md
references/ref-502.md
references/ref-503.md
references/ref-504.md
references/ref-505.md
references/ref-506.md
references/ref-507.md
references/ref-508.md
references/ref-509.md
references/ref-510.md
references/ref-511.md
references/ref-512.md
references/ref-513.md
references/ref-514.md
references/ref-515.md
references/ref-516.md
references/ref-517.md
references/ref-518.md
references/ref-519.md
references/ref-520.md
references/ref-521.md
references/ref-522.md
references/ref-523.md
references/ref-524.md
references/ref-525.md
references/ref-526.md
references/ref-527.md
references/ref-528.md
references/ref-529.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
references/ref-539.md
references/ref-540.md
references/ref-541.md
references/ref-542.md
references/ref-543.md
references/ref-544.md
references/ref-545.md
references/ref-546.md
references/ref-547.md
references/ref-548.md
references/ref-549.md
references/ref-550.md
references/ref-551.md
references/ref-552.md
references/ref-553.md
references/ref-554.md
references/ref-555.md
references/ref-556.md
references/ref-557.md
references/ref-558.md
references/ref-559.md
references/ref-560.md
references/ref-561.md
references/ref-562.md
references/ref-563.md
references/ref-564.md
references/ref-565.md
references/ref-566.md
references/ref-567.md
references/ref-568.md
references/ref-569.md
references/ref-570.md
references/ref-571.md
references/ref-572.md
references/ref-573.md
references/ref-574.md
references/ref-575.md
references/ref-576.md
references/ref-577.md
references/ref-578.md
references/ref-579.md
references/ref-580.md
references/ref-581.md
references/ref-582.md
references/ref-583.md
references/ref-584.md
references/ref-585.md
references/ref-586.md
references/ref-587.md
references/ref-588.md
references/ref-589.md
references/ref-590.md
references/ref-591.md
references/ref-592.md
references/ref-593.md
references/ref-594.md
references/ref-595.md
references/ref-596.md
references/ref-597.md
references/ref-598.md
references/ref-599.md
references/ref-600.md
references/ref-601.md
references/ref-602.md
references/ref-603.md
references/ref-604.md
references/ref-605.md
references/ref-606.md
references/ref-607.md
references/ref-608.md
references/ref-609.md
references/ref-610.md
references/ref-611.md
references/ref-612.md
references/ref-613.md
references/ref-614.md
references/ref-615.md
references/ref-616.md
references/ref-617.md
references/ref-618.md
references/ref-619.md
references/ref-620.md
references/ref-621.md
references/ref-622.md
references/ref-623.md
references/ref-624.md
references/ref-625.md
references/ref-626.md
references/ref-627.md
references/ref-628.md
references/ref-629.md
references/ref-630.md
references/ref-631.md
references/ref-632.md
references/ref-633.md
references/ref-634.md
references/ref-635.md
references/ref-636.md
references/ref-637.md
references/ref-638.md
references/ref-639.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
references/ref-644.md
references/ref-645.md
references/ref-646.md
references/ref-647.md
references/ref-648.md
references/ref-649.md
references/ref-650.md
references/ref-651.md
references/ref-652.md
references/ref-653.md
references/ref-654.md
references/ref-655.md
references/ref-656.md
references/ref-657.md
references/ref-658.md
references/ref-659.md
references/ref-660.md
references/ref-661.md
references/ref-662.md
references/ref-663.md
references/ref-664.md
references/ref-665.md
references/ref-666.md
references/ref-667.md
references/ref-668.md
references/ref-669.md
references/ref-670.md
references/ref-671.md
references/ref-672.md
references/ref-673.md
references/ref-674.md
references/ref-675.md
references/ref-676.md
references/ref-677.md
references/ref-678.md
references/ref-679.md
references/ref-680.md
references/ref-681.md
references/ref-682.md
references/ref-683.md
references/ref-684.md
references/ref-685.md
references/ref-686.md
references/ref-687.md
references/ref-688.md
references/ref-689.md
references/ref-690.md
references/ref-691.md
references/ref-692.md
references/ref-693.md
references/ref-694.md
references/ref-695.md
references/ref-696.md
references/ref-697.md
references/ref-698.md
references/ref-699.md
references/ref-700.md
references/ref-701.md
references/ref-702.md
references/ref-703.md
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
references/ref-711.md
references/ref-712.md
references/ref-713.md
references/ref-714.md
references/ref-715.md
references/ref-716.md
references/ref-717.md
references/ref-718.md
references/ref-719.md
references/ref-720.md
references/ref-721.md
references/ref-722.md
references/ref-723.md
references/ref-724.md
references/ref-725.md
references/ref-726.md
references/ref-727.md
references/ref-728.md
references/ref-729.md
references/ref-730.md
references/ref-731.md
references/ref-732.md
references/ref-733.md
references/ref-734.md
references/ref-735.md
references/ref-736.md
references/ref-737.md
references/ref-738.md
references/ref-739.md
references/ref-740.md
references/ref-741.md
references/ref-742.md
references/ref-743.md
references/ref-744.md
references/ref-745.md
references/ref-746.md
references/ref-747.md
references/ref-748.md
references/ref-749.md
references/ref-750.md
references/ref-751.md
references/ref-752.md
references/ref-753.md
references/ref-754.md
references/ref-755.md
references/ref-756.md
references/ref-757.md
references/ref-758.md
references/ref-759.md
references/ref-760.md
references/ref-761.md
references/ref-762.md
references/ref-763.md
references/ref-764.md
references/ref-765.md
references/ref-766.md
references/ref-767.md
references/ref-768.md
references/ref-769.md
references/ref-770.md
references/ref-771.md
references/ref-772.md
references/ref-773.md
references/ref-774.md
references/ref-775.md
references/ref-776.md
references/ref-777.md
references/ref-778.md
references/ref-779.md
references/ref-780.md
references/ref-781.md
references/ref-782.md
references/ref-783.md
references/ref-784.md
references/ref-785.md
references/ref-786.md
references/ref-787.md
references/ref-788.md
references/ref-789.md
references/ref-790.md
references/ref-791.md
references/ref-792.md
references/ref-793.md
references/ref-794.md
references/ref-795.md
references/ref-796.md
references/ref-797.md
references/ref-798.md
references/ref-799.md
references/ref-800.md
references/ref-801.md
references/ref-802.md
references/ref-803.md
references/ref-804.md
references/ref-805.md
references/ref-806.md
references/ref-807.md
references/ref-808.md
references/ref-809.md
references/ref-810.md
references/ref-811.md
references/ref-812.md
references/ref-813.md
references/ref-814.md
references/ref-815.md
references/ref-816.md
references/ref-817.md
references/ref-818.md
references/ref-819.md
references/ref-820.md
references/ref-821.md
references/ref-822.md
references/ref-823.md
references/ref-824.md
references/ref-825.md
references/ref-826.md
references/ref-827.md
references/ref-828.md
references/ref-829.md
references/ref-830.md
references/ref-831.md
references/ref-832.md
references/ref-833.md
references/ref-834.md
references/ref-835.md
references/ref-836.md
references/ref-837.md
references/ref-838.md
references/ref-839.md
references/ref-840.md
references/ref-841.md
references/ref-842.md
references/ref-843.md
references/ref-844.md
references/ref-845.md
references/ref-846.md
references/ref-847.md
references/ref-848.md
references/ref-849.md
references/ref-850.md
references/ref-851.md
references/ref-852.md
references/ref-853.md
references/ref-854.md
references/ref-855.md
references/ref-856.md
references/ref-857.md
references/ref-858.md
references/ref-859.md
references/ref-860.md
references/ref-861.md
references/ref-862.md
references/ref-863.md
references/ref-864.md
references/ref-865.md
references/ref-866.md
references/ref-867.md
references/ref-868.md
references/ref-869.md
references/ref-870.md
references/ref-871.md
references/ref-872.md
references/ref-873.md
references/ref-874.md
references/ref-875.md
references/ref-876.md
references/ref-877.md
references/ref-878.md
references/ref-879.md
references/ref-880.md
references/ref-881.md
references/ref-882.md
references/ref-883.md
references/ref-884.md
references/ref-885.md
references/ref-886.md
references/ref-887.md
references/ref-888.md
references/ref-889.md
references/ref-890.md
references/ref-891.md
references/ref-892.md
references/ref-893.md
references/ref-894.md
references/ref-895.md
references/ref-896.md
references/ref-897.md
references/ref-898.md
references/ref-899.md
references/ref-900.md
references/ref-901.md
references/ref-902.md
references/ref-903.md
references/ref-904.md
references/ref-905.md
references/ref-906.md
references/ref-907.md
references/ref-908.md
references/ref-909.md
references/ref-910.md
references/ref-911.md
references/ref-912.md
references/ref-913.md
references/ref-914.md
references/ref-915.md
references/ref-916.md
references/ref-917.md
references/ref-918.md
references/ref-919.md
references/ref-920.md
references/ref-921.md
references/ref-922.md
references/ref-923.md
references/ref-924.md
references/ref-925.md
references/ref-926.md
references/ref-927.md
references/ref-928.md
references/ref-929.md
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-937.md
references/ref-938.md
references/ref-939.md
references/ref-940.md
references/ref-941.md
references/ref-942.md
references/ref-943.md
references/ref-944.md
references/ref-945.md
references/ref-946.md
references/ref-947.md
references/ref-948.md
references/ref-949.md
references/ref-950.md
references/ref-951.md
references/ref-952.md
references/ref-953.md
references/ref-954.md
references/ref-955.md
references/ref-956.md
references/ref-957.md
references/ref-958.md
references/ref-959.md
references/ref-960.md
references/ref-961.md
references/ref-962.md
references/ref-963.md
references/ref-964.md
references/ref-965.md
references/ref-966.md
references/ref-967.md
references/ref-968.md
references/ref-969.md
references/ref-970.md
references/ref-971.md
references/ref-972.md
references/ref-973.md
references/ref-974.md
references/ref-975.md
references/ref-976.md
references/ref-977.md
references/ref-978.md
references/ref-979.md
references/ref-980.md
references/ref-981.md
references/ref-982.md
references/ref-983.md
references/ref-984.md
references/ref-985.md
references/ref-986.md
references/ref-987.md
references/ref-988.md
references/ref-989.md
references/ref-990.md
references/ref-991.md
references/ref-992.md
references/ref-993.md
references/ref-994.md
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
site-matrix.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
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
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-area22-s10.md
topics/2026/2026-09-25-area22-s4.md
topics/2026/2026-09-25-area22-s6.md
topics/2026/2026-09-25-area22-s7.md
topics/2026/2026-09-25-area22-s8.md
topics/2026/2026-09-25-area23-s10.md
topics/2026/2026-09-25-area23-s11.md
topics/2026/2026-09-25-area23-s4.md
topics/2026/2026-09-25-area23-s6.md
topics/2026/2026-09-25-area23-s7.md
topics/2026/2026-09-25-area24-s10.md
topics/2026/2026-09-25-area24-s3.md
topics/2026/2026-09-25-area24-s4.md
topics/2026/2026-09-25-area24-s6.md
topics/2026/2026-09-25-area24-s7.md
topics/2026/2026-09-25-area25-s11.md
topics/2026/2026-09-25-area25-s3.md
topics/2026/2026-09-25-area25-s6.md
topics/2026/2026-09-25-area25-s7.md
topics/2026/2026-09-25-area25-s8.md
topics/2026/2026-09-25-area26-s10.md
topics/2026/2026-09-25-area26-s11.md
topics/2026/2026-09-25-area26-s3.md
topics/2026/2026-09-25-area26-s4.md
topics/2026/2026-09-25-area26-s6.md
topics/2026/2026-09-25-area26-s7.md
topics/2026/2026-09-25-area26-s8.md
topics/2026/2026-09-25-area27-s10.md
topics/2026/2026-09-25-area27-s4.md
topics/2026/2026-09-25-area27-s6.md
topics/2026/2026-09-25-area27-s7.md
topics/2026/2026-09-25-area27-s8.md
topics/2026/2026-09-25-area28-s11.md
topics/2026/2026-09-25-area28-s3.md
topics/2026/2026-09-25-area28-s4.md
topics/2026/2026-09-25-area28-s6.md
topics/2026/2026-09-25-area28-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/2026/2026-09-26-area04-s10.md
topics/2026/2026-09-26-area25-s7.md
topics/2026/2026-09-29-area01-s10.md
topics/2026/2026-09-29-area01-s11.md
topics/2026/2026-09-29-area01-s3.md
topics/2026/2026-09-29-area01-s4.md
topics/2026/2026-09-29-area01-s6.md
topics/2026/2026-09-29-area01-s7.md
topics/2026/2026-09-29-area01-s8.md
topics/2026/2026-09-29-area04-s10.md
topics/2026/2026-09-29-area04-s11.md
topics/2026/2026-09-29-area04-s3.md
topics/2026/2026-09-29-area04-s4.md
topics/2026/2026-09-29-area04-s6.md
topics/2026/2026-09-29-area04-s7.md
topics/2026/2026-09-29-area04-s8.md
topics/2026/2026-09-29-area06-s10.md
topics/2026/2026-09-29-area06-s11.md
topics/2026/2026-09-29-area06-s3.md
topics/2026/2026-09-29-area06-s4.md
topics/2026/2026-09-29-area06-s6.md
topics/2026/2026-09-29-area06-s7.md
topics/2026/2026-09-29-area06-s8.md
topics/2026/2026-09-29-area07-s10.md
topics/2026/2026-09-29-area07-s11.md
topics/2026/2026-09-29-area07-s3.md
topics/2026/2026-09-29-area07-s4.md
topics/2026/2026-09-29-area07-s6.md
topics/2026/2026-09-29-area07-s7.md
topics/2026/2026-09-29-area07-s8.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area09-s10.md
topics/2026/2026-09-29-area09-s11.md
topics/2026/2026-09-29-area09-s3.md
topics/2026/2026-09-29-area09-s4.md
topics/2026/2026-09-29-area09-s6.md
topics/2026/2026-09-29-area09-s7.md
topics/2026/2026-09-29-area09-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/2026/2026-09-29-area11-s10.md
topics/2026/2026-09-29-area11-s11.md
topics/2026/2026-09-29-area11-s3.md
topics/2026/2026-09-29-area11-s4.md
topics/2026/2026-09-29-area11-s6.md
topics/2026/2026-09-29-area11-s7.md
topics/2026/2026-09-29-area11-s8.md
topics/2026/2026-09-29-area12-s10.md
topics/2026/2026-09-29-area12-s11.md
topics/2026/2026-09-29-area12-s3.md
topics/2026/2026-09-29-area12-s4.md
topics/2026/2026-09-29-area12-s6.md
topics/2026/2026-09-29-area12-s7.md
topics/2026/2026-09-29-area12-s8.md
topics/2026/2026-09-29-area13-s10.md
topics/2026/2026-09-29-area13-s11.md
topics/2026/2026-09-29-area13-s3.md
topics/2026/2026-09-29-area13-s4.md
topics/2026/2026-09-29-area13-s6.md
topics/2026/2026-09-29-area13-s7.md
topics/2026/2026-09-29-area13-s8.md
topics/2026/2026-09-29-area61-s10.md
topics/2026/2026-09-29-area61-s11.md
topics/2026/2026-09-29-area61-s3.md
topics/2026/2026-09-29-area61-s4.md
topics/2026/2026-09-29-area61-s6.md
topics/2026/2026-09-29-area61-s7.md
topics/2026/2026-09-29-area61-s8.md
topics/2026/2026-09-29-area62-s10.md
topics/2026/2026-09-29-area62-s11.md
topics/2026/2026-09-29-area62-s3.md
topics/2026/2026-09-29-area62-s4.md
topics/2026/2026-09-29-area62-s6.md
topics/2026/2026-09-29-area62-s7.md
topics/2026/2026-09-29-area62-s8.md
topics/2026/2026-09-29-area63-s10.md
topics/2026/2026-09-29-area63-s11.md
topics/2026/2026-09-29-area63-s3.md
topics/2026/2026-09-29-area63-s4.md
topics/2026/2026-09-29-area63-s6.md
topics/2026/2026-09-29-area63-s7.md
topics/2026/2026-09-29-area63-s8.md
topics/2026/2026-09-29-area64-s10.md
topics/2026/2026-09-29-area64-s11.md
topics/2026/2026-09-29-area64-s3.md
topics/2026/2026-09-29-area64-s4.md
topics/2026/2026-09-29-area64-s6.md
topics/2026/2026-09-29-area64-s7.md
topics/2026/2026-09-29-area64-s8.md
topics/2026/2026-09-29-area65-s10.md
topics/2026/2026-09-29-area65-s11.md
topics/2026/2026-09-29-area65-s3.md
topics/2026/2026-09-29-area65-s4.md
topics/2026/2026-09-29-area65-s6.md
topics/2026/2026-09-29-area65-s7.md
topics/2026/2026-09-29-area65-s8.md
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
topics/2026/2026-10-09-area18-s10.md
topics/2026/2026-10-09-area18-s11.md
topics/2026/2026-10-09-area18-s6.md
topics/2026/2026-10-09-area18-s7.md
topics/2026/2026-10-09-area18-s8.md
topics/2026/2026-10-09-area19-s10.md
topics/2026/2026-10-09-area19-s11.md
topics/2026/2026-10-09-area19-s6.md
topics/2026/2026-10-09-area19-s7.md
topics/2026/2026-10-09-area19-s8.md
topics/2026/2026-10-09-area33-s10.md
topics/2026/2026-10-09-area33-s11.md
topics/2026/2026-10-09-area33-s3.md
topics/2026/2026-10-09-area33-s6.md
topics/2026/2026-10-09-area33-s7.md
topics/2026/2026-10-09-area33-s8.md
topics/2026/2026-10-09-area37-s11.md
topics/2026/2026-10-09-area37-s3.md
topics/2026/2026-10-09-area37-s7.md
topics/2026/2026-10-09-area38-s10.md
topics/2026/2026-10-09-area38-s11.md
topics/2026/2026-10-09-area38-s3.md
topics/2026/2026-10-09-area38-s7.md
topics/2026/2026-10-09-area41-s11.md
topics/2026/2026-10-09-area41-s6.md
topics/2026/2026-10-09-area41-s7.md
topics/2026/2026-10-09-area42-s10.md
topics/2026/2026-10-09-area42-s11.md
topics/2026/2026-10-09-area42-s3.md
topics/2026/2026-10-09-area42-s7.md
topics/2026/2026-10-09-area43-s10.md
topics/2026/2026-10-09-area43-s11.md
topics/2026/2026-10-09-area43-s6.md
topics/2026/2026-10-09-area43-s7.md
topics/2026/2026-10-09-area43-s8.md
topics/index.md
tracks/chat-based-configuration-and-operation/experiments.md
tracks/chat-based-configuration-and-operation/index.md
tracks/chat-based-configuration-and-operation/log.md
tracks/chat-based-configuration-and-operation/question-backlog.md
tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md
tracks/chat-based-configuration-and-operation/stage-10-integrated-verification.md
tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md
tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md
tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md
tracks/chat-based-configuration-and-operation/stage-6-chat-map-authoring.md
tracks/chat-based-configuration-and-operation/stage-7-chat-scenario-composition.md
tracks/chat-based-configuration-and-operation/stage-8-chat-robot-configuration.md
tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md
tracks/chat-based-configuration-and-operation/task-model-draft.md
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
          "content": "> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더하며, 2026-10-10 실행에서 아래 제조 공장 사례를 더했다.\n\n**물류 흐름 단계:** 피킹\n\n**시나리오:** 피킹 구역의 좁은 통로에서 서로 다른 제조사의 보충 로봇과 피킹 운반 로봇이 마주침\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 피킹 운반 작업과 보충 작업이 비슷한 시각에 배정되어 두 로봇의 경로가 같은 좁은 통로를 지나게 된다(설명용 가정). |\n| 작업 대상 | 해당 없음(이 영역은 화물보다 로봇의 이동과 통과 시점을 다룬다). |\n| 수행 자원 | 제조사가 다른 두 로봇과 각 제조사 관제, 여러 플릿을 조율하는 ROP(설명용 가정). Open-RMF 기준으로 플릿은 제어 수준에 따라 경로 지시, 일시정지·재개, 상태 수신만 가능할 수 있고, 읽기 전용 플릿은 공유 공간마다 하나만 허용된다. [사실][^ref-004] |\n| 제약 | 차선의 양방향 여부·방향 제약과 대기 지점 같은 경로망 속성 [사실][^ref-079], 해제된 노드·간선만 주행할 수 있다는 규칙과 해제 구역의 진입 요청·응답 [사실][^ref-031] |\n| 완료·인계 | 해당 없음 |\n| 예외·성과 | 지연이 쌓이면 행동 의존 그래프로 순서를 지키며 실행을 이어갈지 재계획할지를 판단해야 하며 [사실][^ref-188], 재계획 여부와 교착 해소 주체가 처리량을 좌우할 것으로 보인다. [추정][^ref-188][^ref-031][^ref-192] |\n\n다음은 설명을 위한 가상의 시나리오이며, 확인된 현장 사례가 아니다. 이 영역은 여섯 항목 가운데 수행 자원·제약·예외·성과에 주로 관여한다.\n\n두 로봇이 마주치는 상황은 대기 지점·차선 방향 같은 경로망 제약과 구역 진입 허가로 먼저 막고, 그래도 생기면 협상이나 일시정지로 한쪽을 대기시키는 순서로 다룰 수 있을 것으로 이 위키는 추정한다. [추정][^ref-079][^ref-031][^ref-004] Open-RMF에서는 충돌이 감지되면 관련 플릿이 선호 경로와 상대를 수용하는 경로를 내고 제3자 판정자가 조합을 고르는 협상을 한다. [사실][^ref-004]\n\n### 제조 공장 사례\n\n**현장 유형:** 제조 공장\n\n**사례:** 생산라인 말단의 팔레타이징·보관·팔레트 포장 구역에서 이종 대형 AGV가 좁은 복도를 지나 팔레트를 나른다\n\n> 이 사례는 Bonetti 외의 교통 관리 연구(The International Journal of Robotics Research 2026 게재)에서 가져왔다. 이 연구는 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발했고, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 소·중·대 규모 세 배치에서 했으며, 공동저자 가운데 업체 소속이 있다. [사실][^ref-192] 논문의 공장 실험 사진은 그림 9 한 장이고 그림 10–12는 업체 관제 소프트웨어의 2D 재구성 화면이다. [사실][^ref-192]\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 업체 관제 소프트웨어(TecnoFerrari Supervisor) 안에서 작업을 연속으로 배정하는 조건으로 시나리오마다 약 10시간 실행하며 성과 지표를 모았다. [사실][^ref-192] |\n| 작업 대상 | 배치 1에서 AGV는 팔레타이저에서 포장기로 팔레트를 나르고, 포장기가 바쁘거나 쓸 수 없으면 임시 보관 구역으로 돌리며, 빈 팔레트를 디스펜서에서 받아 팔레타이저에 보충한다. [사실][^ref-192] |\n| 수행 자원 | AGV 플릿과 업체 관제 소프트웨어. 교통 관리는 NURBS 곡선 경로망 위 지속형 MAPF(L-MAPF) 조율기(수정 Bounded Horizon CBS를 순환 지평 충돌 해소에 넣고 복도 구간에 시간 지평을 늘림), 조율된 궤적을 실행 중 안전하게 할당하는 경로 할당기, 교착 탐지·처리기를 결합해 업체 관제 소프트웨어에 C#으로 통합했다. [사실][^ref-192] |\n| 제약 | 배치 1은 같은 등급 AGV가 복도 4개를 포함한 8개 구역의 좁은 비정형 공간을, 배치 2는 두 등급의 이종 AGV가 고밀도 중형 공간을, 배치 3은 이종 AGV가 좁은 양방향 복도가 없는 넓은 공간을 다니며, 논문 그림 10·11은 막다른 복도를 표시한다. [사실][^ref-192] |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 작업 갱신 같은 예측 못 한 사건이나 시간 지평 부족으로 생기는 교착은 AGV 사이 선행 관계 그래프로 탐지해 관련 AGV의 경로를 갱신해 해소한다. [사실][^ref-192] 처리량은 비교 기준 대비 최대 약 11% 높았다고 저자가 보고한다. [사실][^ref-192] |\n\nBonetti 외는 업체가 배치한 규칙 기반 교통 관리, Pratissoli 외(2023)의 산업용 방법, 우선순위 기반 탐색(PBS)으로 바꾼 L-MAPF 변형과 비교해 처리량이 최대 약 11% 높았다고 보고한다. [사실][^ref-192] 배치별로는 배치 1에서 규칙 기반·Pratissoli 외·PBS 변형 대비 약 10·7·6%, 배치 2에서 약 11·7·10%로 보고되지만, 이는 저자 보고이며 검증 단계에서 원문을 다시 확인하지 못한 값이다. [추정][^ref-192]\n\n배치별 수치는 업체가 제공한 실제 배치를 모사한 실행 결과로 제시되고 실제 운행은 사진 한 장으로만 보이며 업체 소속 공동저자가 있고 독립 재현은 확인하지 못했으므로, 이 위키는 처리량 최대 약 11%를 상용 공장 실측 개선율이나 다른 현장의 일반 개선율로 옮기지 않는다. [의견][^ref-192]\n\n이 사례의 교착 탐지와 경로 할당은 한 업체 관제 안의 기능이다. 그래서 여러 제조사 플릿을 조율하는 ROP의 책임 경계(9절)를 정하는 근거로 쓰지 않고, 교통 관리 구성의 예로만 읽는다. 이 영역은 이 사례에서 수행 자원·제약·예외·성과에 주로 관여한다."
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "MAPF 해법은 여러 로봇의 경로를 함께 최적으로 찾는 충돌 기반 탐색(Conflict-Based Search, CBS)부터 대규모 반복 상황을 겨냥한 우선순위 상속·되돌림(Priority Inheritance with Backtracking, PIBT)까지 폭이 넓고, 계획을 실제 로봇 실행에 맞추는 후처리 연구가 함께 있다. [사실][^ref-187][^ref-189][^ref-196] 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 이와 달리 다른 로봇의 예정 궤적 같은 동적 장애물의 예측 궤적이 주어졌다고 보고 로봇 한 대의 경로를 찾는 저수준 계획이다. [사실][^ref-195]\n\n자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술](../../topics/2026/2026-09-25-area15-s6.md)에 있다. 주제 페이지 본문(2026-09-25 기준)이 SIPP를 CBS와 함께 최적해를 보장하는 다중 로봇 탐색으로 묶은 서술은 아래 내용으로 바로잡는다.\n\n### SIPP의 보장 범위\n\n- Phillips·Likhachev(ICRA 2011)의 SIPP는 상태를 위치와 안전 구간의 쌍으로 묶어 로봇 한 대의 경로를 찾으며, 시간 차원을 더한 계획과 같은 최적성·완전성 보장을 준다고 밝힌다. [사실][^ref-195]\n- 이 보장은 주어진 장애물 궤적에 대해 로봇 한 대의 시간 최소 경로를 찾는 범위의 결과이므로, 여러 로봇의 경로를 함께 정하는 MAPF 전체의 최적성 보장으로 옮길 수 없는 것으로 보인다. [추정][^ref-195][^ref-192]\n- Bonetti 외(2026)는 우선순위 기반 탐색(Priority Based Search, PBS)·SIPP·베지에 곡선 최적화를 결합한 Yan·Li(2024)의 3단 다중 로봇 계획기가 우선순위 탐색에 기대므로 전역 최적성을 보장하지 않는다고 평가한다. 이는 SIPP가 상위 다중 로봇 조율 아래의 저수준 계획으로 쓰이는 예다. [사실][^ref-192]\n- 그래서 이 위키는 SIPP를 최적해를 보장하는 다중 로봇 탐색으로 묶지 않고, 다른 로봇의 예정 궤적 같은 동적 장애물을 피하는 단일 로봇 저수준 경로 탐색으로 분리해 소개한다. [의견][^ref-195][^ref-192]\n\n### PIBT의 보장 범위\n\n- PIBT 논문(Artificial Intelligence 2022 게재판, 초판 IJCAI-19)은 PIBT가 MAPF에 대해 완전하지도 최적이지도 않다고 밝히고, 도달성은 모든 에이전트가 동시에 목표에 있음을 보장하지 않으므로 일반 MAPF에는 불완전하다고 설명한다. [사실][^ref-189]\n- PIBT의 도달 보장은 그래프 조건과 지속형 설정을 전제로 하므로, 막다른 통로가 있는 실제 경로망에는 그 보장을 그대로 적용하지 말고 후퇴 공간과 별도 교착 탐지·해소 장치를 함께 확인해야 한다고 이 위키는 본다. [의견][^ref-189][^ref-192]\n\n### 교착 탐지·해소 모듈 (제조 공장 사례)\n\n- Bonetti 외는 작업 갱신 같은 예측 못 한 사건과, 시간 지평이 부족해 복도 밖 구역의 시공간 충돌을 다 풀지 못할 때 교착이 생긴다고 보고, AGV 사이 선행 관계 그래프로 순환·비순환(중첩) 교착을 탐지한 뒤 관련 AGV의 경로를 갱신해 해소하는 별도 모듈을 둔다. [사실][^ref-192] 이 모듈은 한 업체 관제 안의 기능이며, 사례는 5절 제조 공장 사례에 있다.\n\n### 마감을 목적으로 하는 정식화\n\n- Ma 외의 마감이 있는 다중 에이전트 경로 찾기(MAPF with Deadlines, MAPF-DL, IJCAI 2018)는 모든 에이전트에 공통 마감 하나를 두고 그 시점에 자기 목표 정점을 점유한 에이전트를 성공으로 보아, 충돌 없는 성공 에이전트 수를 최대화하는 문제로 정식화한다. 최적 풀이가 NP-hard임을 보이고 흐름 문제 환원 정수 계획법과 탐색 기반 해법을 낸다. [사실][^ref-1514]\n- 이 목적함수는 도착 시각 합이나 전체 완료 시각(makespan)을 줄이는 일반 MAPF 목적과 달리 마감 안 성공 대수를 최대화하며, 교통 계획에 마감을 넣는 공개 정식화의 예다. [사실][^ref-1514]\n- MAPF-DL은 모든 에이전트에 공통 마감 하나만 두므로, 작업별로 다른 출하 마감이나 업무 중요도를 이종 플릿의 통로 양보 규칙으로 바꾸는 산업 기준으로 볼 수는 없다고 이 위키는 본다. [의견][^ref-1514][^ref-031]"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "Open-RMF는 여러 플릿의 교통 스케줄과 협상을 구현하고, VDA 5050은 경로 해제와 구역 규칙을 정하되 경로 결정·우선순위 같은 교통 조율 전략은 규격 범위에서 뺀다. [사실][^ref-004][^ref-031]\n\n자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area15-s7.md)에 있다. 아래는 2026-10-10 실행에서 VDA 5050 3.0.0 판(GitHub 3.0.0 태그 판, 확인일 2026-10-10)과 Open-RMF 변경 이력으로 더한 내용이다.\n\n### VDA 5050 3.0.0의 예정 경로 공유와 구역 요청\n\n- VDA 5050 3.0.0 §6.8은 자유 주행 이동 로봇이 상태(state) 메시지로 관제에 예정 궤적을 알리게 한다. 상태 메시지의 plannedPath(NURBS, 최소한 현재 베이스를 덮고 지날 nodeId를 담을 수 있음)와, 센서로 볼 수 있는 가까운 경유점별 예상 도착 시각(Estimated Time of Arrival, ETA)을 담은 폴리라인 intermediatePath를 매 상태 메시지마다 공유하게 한다. [사실][^ref-031]\n- 같은 판 §6.4.3은 로봇이 협조 재계획(COORDINATED_REPLANNING) 구역에 들어가거나 구역 안에서 경로를 바꿀 때 zoneRequest의 requestType을 REPLANNING으로 하고 예정 경로를 NURBS 궤적으로 실어 요청하게 하며, 응답을 제때 받지 못하면 구역에 들어가지 않게 한다. [사실][^ref-031]\n- VDA 5050 3.0.0이 경로·우선순위·혼잡·교착 해소 같은 교통 관리 로직을 범위에서 빼므로, 예정 경로 공유·구역 요청 메시지의 상호운용성과 그 정보를 쓰는 현장 교통 최적화의 성능은 따로 검토해야 한다고 이 위키는 본다. [의견][^ref-031]\n\n### Open-RMF 플릿 어댑터의 EasyTrafficLight 수정\n\n- Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 EasyTrafficLight의 플릿 상태 발행 수정과 누적 지연 계산 수정을 기록한다. [사실][^ref-1513]\n- Open-RMF의 신호등(일시정지·재개) 수준 연동을 비교·시험할 때는 제어 수준뿐 아니라 이 수정이 포함된 rmf_fleet_adapter 판도 기록해야 하며, 이 변경 이력은 수정의 존재를 보여 줄 뿐 제어 수준별 처리량 비교 실험은 아니라고 이 위키는 본다. [의견][^ref-1513]"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "분류 원문이 참고 자료로 든 Li 외(2020)와 Ma 외(2017)는 각각 대규모 창고의 지속형 MAPF와 픽업·배송 작업이 온라인으로 들어오는 MAPD의 경로 계획을 다룬다. [사실][^ref-005][^ref-006] 아래 연구의 성능·순위 수치는 모두 단일 출처의 저자·팀 보고이며 이 위키가 확인한 성능이 아니다.\n\n자세한 내용은 주제 페이지 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료](../../topics/2026/2026-09-25-area15-s8.md)에 있다. 주제 페이지(2026-09-25 기준)의 SILLM 항목('2024, 프리프린트')과 Bonetti 외 항목은 아래 내용으로 바로잡는다.\n\n- Bonetti, A. 외, A traffic management system for large and heterogeneous vehicles in narrow industrial environments(The International Journal of Robotics Research 2026 게재, arXiv 2026-09-09) — 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발한 이종 대형 AGV 교통 관리 시스템이며, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치에서 했다. [사실][^ref-192] 사례와 성과 수치의 해석 한정은 5절 제조 공장 사례에 있다.\n- Jiang, H. 외, Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding(SILLM, ICRA 2025 채택, arXiv 초판 2024-10-28, v2 2025-05-18) — 최대 10,000 에이전트의 6개 대형 지도 벤치마크와 별도로, 초록과 서론에서 실물 로봇 10대·가상 로봇 100대로 모사 창고에서 검증했다고 적는다. [사실][^ref-199] 실물 검증은 계획이 모든 에이전트 위치를 정확히 안다고 가정하므로 실물 로봇 위치를 외부 모션 캡처로 얻고, 교란·제어 오차로 생기는 실행 오차는 행동 의존 그래프(Action Dependency Graph, ADG)로 없앤 실험 조건이었다. [사실][^ref-199] 2023 League of Robot Runners 우승 해법 WPPL과의 비교는 다른 기준선에 맞추려고 회전 동작을 없애고, 단계당 계획 시간 1초 제한 대신 대규모 이웃 탐색 개선 반복을 40,000회로 제한한 조건이었다. [사실][^ref-199] 그래서 이 위키는 제목의 10,000을 실물 배치 대수가 아닌 계산 벤치마크 규모로, WPPL 비교를 원래 대회 조건의 재현이 아닌 바꾼 조건의 결과로 읽는다. [의견][^ref-199]\n- Yan, J. 외, LSMART(Lifelong Scalable Multi-Agent Realistic Testbed, 2026-02-17 프리프린트) — 운동 제약·통신 지연·실행 불확실성·계획과 실행의 동시 진행·계획 실패 복구를 고려해 AGV 플릿 관리 시스템(Fleet Management System, FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터이며, 계획기·인스턴스 생성기·계획 호출 정책·실패 정책을 설계 선택으로 비교한다. [사실][^ref-604] 실험은 지도와 에이전트 수 조건마다 600초 시뮬레이션을 10회 돌려 평균과 95% 신뢰구간을 낸다. [사실][^ref-604] 재계획을 더 자주 하는 것은 모든 지도·밀도에서 유리하지 않았고(room-64-64-16과 낮은 밀도에서 이점이 일관되지 않음), 저자들은 ADG로 추정한 확정 지점이 실제 진행과 맞지 않는 실행–계획 불일치를 원인으로 든다. [사실][^ref-604] 더 정확한 로봇 모델과 더 강한 최적성 보장은 계획기의 확장성을 떨어뜨려, 저자들은 이를 계획기의 해 품질과 확장성(solution quality and scalability) 사이의 절충으로 설명한다. [사실][^ref-604] LSMART는 4-연결 격자 기반 시뮬레이션이고 논문에 실물 로봇 실험이 없으며, 저자들은 4-연결 격자를 넘는 그래프 지원을 향후 과제로 든다. [사실][^ref-604] 따라서 이종 제조사 로봇이 섞인 실물 창고에서의 개선율을 직접 제공하지는 않는 것으로 보인다. [추정][^ref-604]"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "- [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — LSMART는 플릿 관리 시스템 안에서 MAPF 알고리즘을 통신 지연·실행 불확실성 같은 실행 조건과 함께 평가하는 시뮬레이터여서, 교통 관리 알고리즘의 시험 방법이 두 영역을 잇는 것으로 보인다. [추정][^ref-604]\n- [62. 제조 공장](../site-type-applications/manufacturing-plant.md) — 5절의 제조 공장 사례(팔레타이징·보관·팔레트 포장 공장을 모사한 배치의 이종 대형 AGV 교통 관리)가 이 현장 유형의 교통 관리 적용 예가 되는 것으로 보인다. [추정][^ref-192]",
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
          "content": "- **oq-032** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? — 부분 근거로 Open-RMF 문서는 신호등 수준 플릿은 일시정지·재개만 가능하고 공유 공간마다 읽기 전용 플릿을 하나만 허용한다고 적지만, 제어 수준별 교통 성능을 측정한 연구는 찾지 못해 열린 채로 둔다. [사실][^ref-004] 2026-10-10 실행에서 확인한 rmf_fleet_adapter 2.14.0 변경 이력(EasyTrafficLight 수정)은 관련 판 정보만 주며 제어 수준별 처리량 비교 실험이 아니므로 이 질문에 답하지 않는다고 이 위키는 본다. [의견][^ref-1513]\n- **oq-057** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가?\n- **oq-058** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? — 부분 근거로 SILLM의 실물 10대 모사 창고 검증과 LSMART의 실행 불확실성을 넣은 처리량 실험(8절)이 있지만, 벤치마크 개선율을 상용 물류센터 실측 개선율로 환산한 자료나 국내 사례는 확인하지 못해 정량 전이 질문은 열린 채로 둔다고 이 위키는 본다. [의견][^ref-199][^ref-604]\n- **oq-059** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-39) 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? — 부분 근거로 MAPF-DL은 공통 마감을 교통 계획의 목적함수에 넣는 정식화를 주지만 작업별 업무 우선순위를 통로 양보 우선권으로 바꾸는 규칙은 다루지 않고, VDA 5050 3.0.0도 우선순위·교착 해소 같은 교통 관리 로직을 범위에서 뺀다. [사실][^ref-1514][^ref-031]\n- (신규 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-04) 막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가?\n- (신규 · 상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-04) 실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가?\n\n전체 목록은 [열린 질문](../../open-questions.md)에 있다."
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25\n[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-25 (원문 미열람)\n[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-25 (원문 미열람)\n[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10\n[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25\n[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)\n[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)\n[^ref-187]: Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R., Conflict-based search for optimal multi-agent pathfinding, 2015, https://dl.acm.org/doi/10.1016/j.artint.2014.11.006, 접근일 2026-09-25 (원문 미열람)\n[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)\n[^ref-189]: Okumura, K., Machida, M., Défago, X., & Tamura, Y., Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding (열람판 arXiv v5 2022-06-27, Artificial Intelligence 게재판, DOI 10.1016/j.artint.2022.103752; 초판 IJCAI-19), 2019-01, https://arxiv.org/abs/1901.11282, 접근일 2026-10-10\n[^ref-190]: Yu, J., & LaValle, S. M., Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity, 2015-07, https://arxiv.org/abs/1507.03289, 접근일 2026-09-25 (원문 미열람)\n[^ref-192]: Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (The International Journal of Robotics Research, 2026, DOI 10.1177/02783649261470035; arXiv 2609.10400 v1 2026-09-09), 2026-09-09, https://arxiv.org/abs/2609.10400, 접근일 2026-10-10\n[^ref-195]: Phillips, M., & Likhachev, M., SIPP: Safe interval path planning for dynamic environments (ICRA 2011, pp.5628–5635), 2011, https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments, 접근일 2026-10-10\n[^ref-196]: Ma, H., Koenig, S. 외, Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios, 2017-02, https://arxiv.org/abs/1702.05515, 접근일 2026-09-25 (원문 미열람)\n[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J., Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (ICRA 2025 채택, arXiv v1 2024-10-28, v2 2025-05-18), 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-10\n[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-10-10\n[^ref-1513]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10\n[^ref-1514]: Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S., Multi-Agent Path Finding with Deadlines (IJCAI 2018, pp.417–423, DOI 10.24963/ijcai.2018/58), 2018, https://www.ijcai.org/proceedings/2018/0058.pdf, 접근일 2026-10-10"
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

### runs/2026-10-10-04/verification2.json

```json
{
  "run_id": "2026-10-10-04",
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
    "ok": false,
    "overlaps": [
      "새 주제 페이지 2026-10-10-area27-s6·s7·s8 은 2026-09-25 기준 주제 페이지(2026-09-25-area15-s6·s7·s8)를 '바로잡는다'고 하지만 링크가 없다. 세부영역 6·7·8절 replace 패치가 기존 주제 페이지 링크 줄을 지워, 이미 게시된 검증 내용(s6 의 PIBT 그래프 조건, s7 의 VDA 5050 구역 4종 표·§2 범위 제외, s8 의 기존 연구 목록)에 세부영역 본문에서 닿을 수 없다. 브리프와 1차 판정은 이 내용들을 '기존 s6·s7 에 있어 다시 싣지 않는다'고 처리했다",
      "ref-1513 은 같은 URL 의 기존 id(ref-1458·ref-1487)와 겹칠 수 있다. 스토리텔러가 reference_updates 요약과 additional_research_requests 로 퍼블리셔의 URL 기준 병합을 요청했으므로 이번 판정에서는 지적하지 않는다"
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
    "'6. 대표 접근법과 기술' 패치(replace): 본문의 '주제 페이지 본문(2026-09-25 기준)이 SIPP를 … 바로잡는다' 문장에서 '주제 페이지 본문(2026-09-25 기준)'을 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area15-s6.md) 링크로 바꾼다. 절 첫 문단 뒤에는 'CBS·PIBT 그래프 조건 등 2026-09-25 기준 내용은 이 링크의 주제 페이지에 있고, 아래 내용이 그 페이지의 SIPP 서술을 바로잡는다'는 연결 문장을 둔다. 이유: replace 패치가 기존 6절의 주제 페이지 링크를 지워, 이미 게시된 검증 내용(1차가 '기존 s6 에 있어 다시 싣지 않는다'고 처리한 PIBT 그래프 조건 등)에 본문에서 닿을 수 없다. 세부영역 페이지와 분리될 주제 페이지가 모두 docs 아래 두 단계 깊이라서 '../../topics/2026/…' 상대 경로는 두 곳에서 똑같이 유효하다.",
    "'7. 관련 표준·프레임워크·오픈소스' 패치(replace): '아래는 2026-10-10 실행에서 … 더한 내용이다' 문장 앞에 'VDA 5050 구역 4종과 §2 범위 제외 등 2026-09-25 기준 내용은 [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area15-s7.md)에 있다'는 연결 문장을 둔다. 이유: 패치가 기존 7절의 주제 페이지 링크를 지웠다. f19·f20 은 그 페이지 내용을 전제로 다시 싣지 않았다.",
    "'8. 대표 연구와 자료' 패치(replace): '주제 페이지(2026-09-25 기준)의 SILLM 항목 … 바로잡는다' 문장의 '주제 페이지(2026-09-25 기준)'를 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area15-s8.md) 링크로 바꾼다. 이유: 패치가 기존 8절의 주제 페이지 링크를 지워, 세부영역 프런트매터 sources 에 남은 ref-191·ref-193·ref-194·ref-268 등 기존 연구 목록에 본문에서 닿을 수 없다.",
    "세부영역 페이지 프런트매터: 10절 패치의 frontmatter 에 last_run: 2026-10-10 을 넣는다. 이유: 이번 실행이 페이지를 갱신했는데도 last_run 이 2026-09-25 로 남아 있다. 분리된 주제 페이지 5건은 last_run 2026-10-10 이고, 퍼블리셔가 이 값으로 page-status 줄의 '마지막 실행'을 채우므로 두 쪽이 어긋난다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인 / 2차 수정 후 재검증. 확인 33건, 미확인 1건(f13 배치별 수치), 교차 확인 0건. 강등: f13 사실 → 일부 추정(배치별 처리량 수치. 최대 약 11%는 사실 유지). 원문 미열람 출처: 없음. 리서치가 8건 모두 원문을 열었고, 1차 검증에서 ref-192·ref-199·ref-604·ref-031·ref-1513 본문을 다시 확인했다. ref-195·ref-189는 서지·초록과 검색 결과로, ref-1514는 본문 텍스트 사본과 IJCAI 공식 목록으로 확인했다. 주의: 모든 사실 주장이 단일 출처이며 교차 확인은 없다. Bonetti 외의 처리량 개선은 업체 소속 공동저자가 있는 논문의 저자 보고이고, 원문은 성과 지표가 실물 운행에서 나왔는지 모사 실행에서 나왔는지 구분하지 않는다. SILLM의 10,000은 계산 벤치마크 규모다. LSMART는 격자 시뮬레이션만 다룬 프리프린트다. 기존 6절의 'CBS·SIPP 최적해 보장' 문장은 고쳤다. 다만 2026-09-25 기준 주제 페이지(area15-s6·s8)의 본문에는 같은 오류와 '프리프린트' 표기가 남아 있어 다음 갱신 실행에서 고쳐야 한다(추가 조사 요청). ref-1513은 같은 URL의 기존 id(ref-1458·ref-1487)가 있으면 퍼블리셔가 합친다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-058·oq-059는 부분 근거만 있음, oq-032·oq-057은 근거 없음). 새 열린 질문 2건(f7·f29 근거)을 등록한다. 트랙 반영 제안 1건(2026-09-25-58)은 근거 finding이 없어 반영하지 않았다. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 17건은 모두 이행됐다. [분류원문] 보존, 섹션 순서 준수. 링크: 6·7·8절 replace 패치가 2026-09-25 기준 주제 페이지 링크를 지워 기존 검증 내용에 닿을 수 없으므로, 링크를 복원하라고 지시했다. 세부영역 프런트매터 last_run 갱신도 지시했다.",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - '6. 대표 접근법과 기술' 패치(replace): 본문의 '주제 페이지 본문(2026-09-25 기준)이 SIPP를 … 바로잡는다' 문장에서 '주제 페이지 본문(2026-09-25 기준)'을 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area15-s6.md) 링크로 바꾼다. 절 첫 문단 뒤에는 'CBS·PIBT 그래프 조건 등 2026-09-25 기준 내용은 이 링크의 주제 페이지에 있고, 아래 내용이 그 페이지의 SIPP 서술을 바로잡는다'는 연결 문장을 둔다. 이유: replace 패치가 기존 6절의 주제 페이지 링크를 지워, 이미 게시된 검증 내용(1차가 '기존 s6 에 있어 다시 싣지 않는다'고 처리한 PIBT 그래프 조건 등)에 본문에서 닿을 수 없다. 세부영역 페이지와 분리될 주제 페이지가 모두 docs 아래 두 단계 깊이라서 '../../topics/2026/…' 상대 경로는 두 곳에서 똑같이 유효하다.
    - '7. 관련 표준·프레임워크·오픈소스' 패치(replace): '아래는 2026-10-10 실행에서 … 더한 내용이다' 문장 앞에 'VDA 5050 구역 4종과 §2 범위 제외 등 2026-09-25 기준 내용은 [27. 다중 로봇 경로·교통 관리 — MAPF — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area15-s7.md)에 있다'는 연결 문장을 둔다. 이유: 패치가 기존 7절의 주제 페이지 링크를 지웠다. f19·f20 은 그 페이지 내용을 전제로 다시 싣지 않았다.
    - '8. 대표 연구와 자료' 패치(replace): '주제 페이지(2026-09-25 기준)의 SILLM 항목 … 바로잡는다' 문장의 '주제 페이지(2026-09-25 기준)'를 [27. 다중 로봇 경로·교통 관리 — MAPF — 대표 연구와 자료 (2026-09-25)](../../topics/2026/2026-09-25-area15-s8.md) 링크로 바꾼다. 이유: 패치가 기존 8절의 주제 페이지 링크를 지워, 세부영역 프런트매터 sources 에 남은 ref-191·ref-193·ref-194·ref-268 등 기존 연구 목록에 본문에서 닿을 수 없다.
    - 세부영역 페이지 프런트매터: 10절 패치의 frontmatter 에 last_run: 2026-10-10 을 넣는다. 이유: 이번 실행이 페이지를 갱신했는데도 last_run 이 2026-09-25 로 남아 있다. 분리된 주제 페이지 5건은 last_run 2026-10-10 이고, 퍼블리셔가 이 값으로 page-status 줄의 '마지막 실행'을 채우므로 두 쪽이 어긋난다.
- 검증 노트: 판정: 1차 조건부 승인 / 2차 수정 후 재검증. 확인 33건, 미확인 1건(f13 배치별 수치), 교차 확인 0건. 강등: f13 사실 → 일부 추정(배치별 처리량 수치. 최대 약 11%는 사실 유지). 원문 미열람 출처: 없음. 리서치가 8건 모두 원문을 열었고, 1차 검증에서 ref-192·ref-199·ref-604·ref-031·ref-1513 본문을 다시 확인했다. ref-195·ref-189는 서지·초록과 검색 결과로, ref-1514는 본문 텍스트 사본과 IJCAI 공식 목록으로 확인했다. 주의: 모든 사실 주장이 단일 출처이며 교차 확인은 없다. Bonetti 외의 처리량 개선은 업체 소속 공동저자가 있는 논문의 저자 보고이고, 원문은 성과 지표가 실물 운행에서 나왔는지 모사 실행에서 나왔는지 구분하지 않는다. SILLM의 10,000은 계산 벤치마크 규모다. LSMART는 격자 시뮬레이션만 다룬 프리프린트다. 기존 6절의 'CBS·SIPP 최적해 보장' 문장은 고쳤다. 다만 2026-09-25 기준 주제 페이지(area15-s6·s8)의 본문에는 같은 오류와 '프리프린트' 표기가 남아 있어 다음 갱신 실행에서 고쳐야 한다(추가 조사 요청). ref-1513은 같은 URL의 기존 id(ref-1458·ref-1487)가 있으면 퍼블리셔가 합친다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-058·oq-059는 부분 근거만 있음, oq-032·oq-057은 근거 없음). 새 열린 질문 2건(f7·f29 근거)을 등록한다. 트랙 반영 제안 1건(2026-09-25-58)은 근거 finding이 없어 반영하지 않았다. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 17건은 모두 이행됐다. [분류원문] 보존, 섹션 순서 준수. 링크: 6·7·8절 replace 패치가 2026-09-25 기준 주제 페이지 링크를 지워 기존 검증 내용에 닿을 수 없으므로, 링크를 복원하라고 지시했다. 세부영역 프런트매터 last_run 갱신도 지시했다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
