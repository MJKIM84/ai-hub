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
- 세부영역 반영 제안: 1건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
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

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
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

### docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md (요약)

```markdown
# 55. 현장 조사·설치·시운전

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 조사, 설치·설정, 교정, 시운전, 인수 시험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 설치·설정**: 로봇·충전기·네트워크·설비를 설치하고 설정하며, 반복되는 설치 절차를 자동화한다
- **교정**: 센서·좌표·지도를 현장에 맞게 교정한다
- **현장 시운전**: 연동과 작업을 현장에서 시험 운전하며 문제를 잡는다
- **현장 조사**: 설치 전에 현장 치수·네트워크·설비·동선을 조사한다
- **인수 시험**: 합의한 수용 기준으로 인수 여부를 판정한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 21번 영역 ‘온보딩·설정·현장 시운전’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [옛 분류원문]

> 옛 질문: 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

새 현장에 설치하고 시운전할 때 반복 작업을 얼마나 줄일 수 있는가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
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

### runs/2026-10-10-03/research.md

```markdown
# 리서치 브리프 2026-10-10-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-03 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 26. 작업 순서·스케줄링 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 시작 조건 칸의 'Open-RMF 요청에 마감·선후 필드는 없다'가 공통 최상위 스키마 범위인지 밝혀져 있지 않고, 유형별 description 확장 경로를 다루지 않음. 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — Open-RMF 기본 비용이 무엇을 최소화하는지(완료 시각 합 vs 메이크스팬), 누적 용량 제약, 진행 중 동작을 고정하는 재계획 방식이 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — BinaryPriorityScheme 행이 '비용 반영 방식은 미확인'으로 남아 있고, 2026-09-25 이후 rmf_fleet_adapter 변경(2.14.0) 미반영
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 성능 수치가 모두 원문 미열람이며 2024~2025년 동적·협업 일정 연구가 없음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-019·oq-049 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]
2. Open-RMF task_request 스키마의 마감·선후 필드 부재는 공통 최상위 스키마에 한정되는가, 유형별 확장 경로는 무엇인가? (섹션 5·7 겨냥)
3. Open-RMF 이진 우선순위는 비용 계산에 어떻게 반영되며, 기본 비용은 어떤 지표를 최소화하는가? (섹션 6·7 겨냥)
4. 마감·공용 자원 용량·선택 작업을 제약으로 표현하는 공개 도구와, 진행 중 동작을 보존하며 재계획하는 연구는 무엇인가? (섹션 6·8 겨냥)
5. oq-019 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? (섹션 11 겨냥)
6. oq-049 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF task_request.json 의 공통 최상위 필드는 unix_millis_earliest_start_time·unix_millis_request_time·priority·category·description·labels·requester·fleet_name 의 8개이고 필수는 category·description 뿐이며, 마감 시각이나 다른 작업 ID 를 가리키는 선후 필드는 공통 최상위 스키마에 정의되어 있지 않다. | ref-125 | 아니오 | medium | 2026-10-10 | 시작 조건 | — |
| f2 | [사실] | 같은 스키마에서 description 은 그 작업 유형(category)에 대해 플릿이 지원하는 스키마를, priority 는 플릿이 지원하는 우선순위 스키마를 따라야 한다고 설명하며, 최상위에 additionalProperties 제한은 두지 않는다. | ref-125 | 아니오 | medium | 2026-10-10 | 시작 조건 | — |
| f3 | [추정] | 공통 최상위 스키마에 마감·선후 필드가 없다는 것이 유형별 description 확장이나 플릿별 우선순위 스키마로 그런 조건을 구현하는 것이 불가능하다는 뜻은 아닐 것으로 보인다. | ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f4 | [의견] | 출하 마감이나 다른 작업 완료를 시작 조건으로 쓰려면, 문법상 추가 필드를 넣을 수 있다는 것과 계획기가 그 필드를 집행한다는 것을 구분해 그 확장 계약과 집행 주체를 별도로 명시해야 한다. | ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f5 | [사실] | rmf_task 의 BinaryPriorityScheme.cpp 는 make_low_priority() 에서 nullptr 를, make_high_priority() 에서 BinaryPriority(1) 객체를 돌려주고, make_cost_calculator() 로 BinaryPriorityCostCalculator 를 만든다. | ref-1484 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [사실] | BinaryPriorityCostCalculator 의 valid_assignment_priority() 는 같은 계획 노드 안의 로봇(에이전트) 사이에서 한 로봇이 높은 우선순위 작업을 2개 이상 받았는데 높은 작업을 하나도 받지 않은 로봇이 있으면 위반으로 보고, 같은 로봇의 배정 순서 안에서는 충전 작업을 건너뛴 뒤 낮은 작업 다음에 높은 작업이 오면 위반으로 본다. | ref-1483 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f7 | [사실] | compute_cost(Node, time_now, check_priority) 는 우선순위 검사가 켜져 있고 배정이 위반이면 비용을 _priority_penalty × (g + h) 로, 그렇지 않으면 g + h 로 계산한다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f8 | [의견] | 이 우선순위 처리는 납기 제약을 직접 검사하는 코드가 아니라 배정 비용에 벌점을 곱하는 방식이므로, 높은 우선순위를 마감 보장으로 해석해서는 안 되며 로봇 사이 배분 조건이 있어 단순한 선입선출 정렬로 설명해서도 안 된다. | ref-1483, ref-125 | 아니오 | low | 2026-10-10 | 제약 | — |
| f9 | [사실] | BinaryPriorityCostCalculator 의 기본 실비용(g)은 각 일반 작업의 완료 시각(finish_state 시각)에서 그 요청의 가장 이른 시작 시각을 뺀 값을 모든 로봇·모든 배정에 걸쳐 합산한 값이다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [사실] | 같은 계산기는 충전 작업(ChargeBattery) 배정 자체의 비용을 0 으로 계산한다. | ref-1483 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [추정] | 충전 작업 자체의 비용은 0 이지만, 충전 때문에 같은 로봇의 뒤 작업 완료가 늦어지면 그 작업의 비용(완료 시각 − 가장 이른 시작 시각)은 커질 수 있을 것으로 보인다. | ref-1483 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [의견] | 이 비용은 작업별 (완료 시각 − 가장 이른 시작 시각)의 합이므로, Dai 외가 정의한 메이크스팬(Makespan, 차고지 복귀를 포함한 모든 로봇의 총 작업 시간 중 최댓값)이나 납기 지연 합과 같은 지표라고 부르면 안 된다. | ref-1483, ref-1486 | 아니오 | low | 2026-10-10 | — | — |
| f13 | [사실] | OR-Tools CP-SAT 스케줄링 문서는 구간 변수, 실행 여부를 리터럴로 정하는 선택 구간, 구간 사이 시간 관계, 겹침 금지(NoOverlap)에 더해, 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약을 다룬다. | ref-379 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f14 | [추정] | 이 표현으로 '이전 작업 종료 뒤 시작'(시간 관계), '도크는 한 번에 한 작업'(겹침 금지), '작업대 동시 사용량은 용량 이하'(누적 용량)를 서로 다른 제약으로 작성할 수 있을 것으로 보인다. | ref-379 | 아니오 | low | 2026-10-10 | 제약 | — |
| f15 | [사실] | Tuck 외(2024)의 동적 다중 로봇 작업 배정 정식화는 Definition 6(완료된 작업)에서 내려놓기 동작이 마감 전에 일어나야 작업을 완료한 것으로 보아, 마감을 필수 완료 조건으로 둔다. | ref-1485 | 아니오 | medium | 2024-03-18 | 제약 | — |
| f16 | [의견] | 마감을 반드시 지킬 조건으로 둘지, 어겼을 때 비용을 주는 조건으로 둘지는 목적함수와 제약식을 나눠 설계해야 한다. | ref-379, ref-1485 | 아니오 | low | 2026-10-10 | 제약 | — |
| f17 | [사실] | Tuck 외(2024)는 마감이 있는 작업이 온라인으로 들어오고 로봇이 여러 작업을 동시에 실을 수 있는 동적 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA)을 다루며, Definition 9 의 갱신 계획(Updated plan)은 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 새 작업을 반영하도록 정의한다. | ref-1485 | 아니오 | medium | 2024-03-18 | — | — |
| f18 | [사실] | 같은 연구는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 해법기의 push·pop 기능으로 앞선 풀이 정보를 유지하는 증분 풀이를 쓰지만, 증분·비증분 풀이의 시간 성능은 해법기와 배치 크기에 따라 크게 달랐다(Z3-BV 와 Bitwuzla-BV 비교). | ref-1485 | 아니오 | medium | 2024-03-18 | — | — |
| f19 | [추정] | 이를 참고하면 긴급 작업 삽입 정책을 '현재 동작 고정'과 '아직 실행하지 않은 구간의 재배열'로 나눠 기술할 수 있을 것으로 보인다. | ref-1485 | 아니오 | low | 2024-03-18 | 예외·성과 | — |
| f20 | [사실] | Dai 외(2025)는 탐색·구조 같은 협업 과제를 모사한 계산 실험에서, 배정된 로봇 연합의 능력 벡터 합이 작업 요구를 충족해야 작업을 시작할 수 있고 모든 배정 로봇이 실행 기간 내내 작업 위치에 함께 있어야 하며 먼저 도착한 로봇은 나머지가 올 때까지 기다리는 작업을 모델링한다. | ref-1486 | 아니오 | medium | 2025 | 기타 / 시작 조건 | — |
| f21 | [추정] | 이런 협업 작업에서는 개별 로봇이 빨리 도착해도 다른 팀원이 늦으면 작업 시작이 늦어지므로, 개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지는 않을 것으로 보인다. | ref-1486 | 아니오 | low | 2025 | 기타 / 제약 | — |
| f22 | [의견] | 이 사례를 이용하면 일정 설명에서 도착 동기화, 공동 작업 시간, 다음 작업으로의 이동을 구분해 적을 수 있다. | ref-1486 | 아니오 | low | 2025 | 기타 | — |
| f23 | [사실] | Dai 외(2025)는 강화학습(Reinforcement Learning, RL)으로 이종 로봇이 다음 작업을 분산적으로 고르는 협업 일정 정책을 학습하고, 계산 실험에서 최대 150 에이전트·500 작업·5종 능력 조건까지 다뤘다고 보고한다. | ref-1486 | 아니오 | medium | 2025 | — | — |
| f24 | [사실] | Open-RMF TaskPlanner.hpp 의 Options 주석은 탐욕 방식은 최적성을 보장하지 않지만 더 빨리 풀 수 있고, A* 기반 방식은 최적성을 보장하지만 풀이에 더 오래 걸릴 수 있다고 설명한다. | ref-377 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [의견] | Dai 외의 강화학습 방식과 Open-RMF 계획기는 목적·모델·평가 환경이 달라, 규모나 풀이 시간만으로 우열을 정하기보다 실행 가능한 일정 비율과 목적값을 같은 조건에서 비교하는 편이 좋다. | ref-1486, ref-377 | 아니오 | low | 2026-10-10 | — | — |
| f26 | [사실] | rmf_fleet_adapter 2.14.0(2026-09-26) 변경 이력은 단계 건너뛰기 요청의 단계 키 수정(#543)과 EasyTrafficLight 의 누적 지연 계산 수정(#524)을 포함한다. | ref-1487 | 아니오 | medium | 2026-09-26 | 예외·성과 | — |
| f27 | [의견] | 일정의 예외 조정과 지연 기반 추정에 의존하는 구현은 사용하는 Open-RMF 패키지 버전을 함께 기록하는 편이 좋다. | ref-1487 | 아니오 | low | 2026-09-26 | — | — |
| f28 | [의견] | oq-019 부분 답변: 이진 우선순위의 표현과 비용 벌점 구현은 공개되어 있지만, 납기·운송 마감을 이진 값으로 바꾸고 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못해 질문을 닫을 수 없다. | ref-125, ref-1483, ref-1484 | 아니오 | low | 2026-10-10 | — | — |
| f29 | [추정] | oq-049 부분 답변: 공통 task_request 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 제조사 간 선후 집행이 구현되었다고 볼 수 없으며 범용 표준 필드나 완성된 공개 구현은 확인하지 못했다. | ref-125 | 아니오 | low | 2026-10-10 | 완료·인계 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-379 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md | 아니오 |
| ref-1483 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp | 아니오 |
| ref-1484 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp | 아니오 |
| ref-1485 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America) | SMT-Based Dynamic Multi-Robot Task Allocation | 2024-03-18 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2403.11737v1 | 아니오 |
| ref-1486 | Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. | Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning | 2025 | 논문 | medium | 2026-10-10 | https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf | 아니오 |
| ref-1487 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md | 5, 6, 7, 8, 11 | 갱신(차등): 섹션 5 — 시작 조건 칸 문장을 공통 최상위 스키마 범위로 한정(f1)하고 description·priority 의 플릿 스키마 위임(f2), 확장 가능성(f3, 추정), 확장 계약·집행 주체 명시 필요(f4, 의견)를 제약 칸에 반영; 물류창고 표와 별도로 '현장 유형: 기타(탐색·구조 모사 계산 실험)' 협업 사례를 추가(f20 사실, f21 추정, f22 의견) / 섹션 6(주제 페이지 2026-09-25-area14-s6 요약) — 플릿 안 일정 계획에 기본 비용 정의(f9·f10, f11 추정)와 메이크스팬과의 구분(f12, 의견), 제약 프로그래밍에 누적 용량 제약(f13; 구간·선택 구간·선후·겹침 금지는 기존 내용 확인)과 창고 제약 대응(f14 추정)·마감의 필수/비용 설계 구분(f15·f16), 온라인 재계획에 Tuck 외 갱신 계획·증분 풀이(f17·f18, f19 추정) / 섹션 7 — BinaryPriorityScheme 행의 '비용 반영 방식은 미확인'을 f5~f7 로 교체하고 마감 보장 해석 금지(f8, 의견), Open-RMF 작업 요청 스키마 행 문구를 공통 최상위 필드 기준으로(f1·f2), rmf_fleet_adapter 2.14.0 변경 이력 행 추가(f26, f27 의견) / 섹션 8(주제 페이지 2026-09-25-area14-s8 요약) — Tuck 외(f17·f18), Dai 외(f23) 추가와 접근법 비교 방식(f24·f25; f24 의 탐욕·A* 설명은 기존 6절 분리 페이지 내용 확인) / 섹션 11(주제 페이지 2026-09-25-area14-s11) — oq-019 부분 근거(f28), oq-049 부분 근거(f29), 새 질문 3건. 두 열린 질문 모두 해결 제안 없음. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 메이크스팬 | Makespan | 작업 집합 전체를 끝내는 데 걸린 시간으로, 다중 로봇 일정에서는 보통 모든 로봇 가운데 가장 늦게 일을 마친 로봇의 종료 시각(또는 총 작업 시간)을 뜻한다. |
| 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 정수·비트벡터 산술 같은 배경 이론 위에서 논리식을 만족하는 값의 존재를 판정하는 문제와 그 해법기로, 일정·배정 제약을 논리식으로 풀 때 쓴다. |

## 열린 질문

새로 생긴 질문:

- 이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가? | 관련 영역: 26. 작업 순서·스케줄링, 25. 작업 배정 — MRTA | 근거: f6 | 종류: 일반
- 제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? | 관련 영역: 26. 작업 순서·스케줄링, 20. 로봇·제조사 관제 연동 | 근거: f16 | 종류: 일반
- 작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? | 관련 영역: 26. 작업 순서·스케줄링, 39. 운영 성과 측정·개선 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 8 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 5건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-03/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - ref-1486(Dai 외): 게재지 IEEE Robotics and Automation Letters 2025 는 PDF 파일명(73-RAL2025-HetMRTA) 기준이며 본문에서 확인하지 못함 — published 는 '2025'로만 둠, 동료심사 여부 미확인이라 신뢰도 medium
    - f3·f29: 유형별 description 확장으로 마감·선후 조건을 실제 집행하는 Open-RMF 구현은 확인하지 못함(다른 작업 유형 스키마 전체는 대조하지 않음)
    - f11: 충전 작업이 뒤 작업 비용을 늘리는 효과는 코드 정의에서 도출한 추론이며 실행 결과로 확인하지 않음
    - f21: '개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지 않는다'는 원문 직접 진술이 아니라 추론(검증에서 사실→추정 강등)
    - f23: Dai 외 성능 비교(MIP·휴리스틱 대비)는 저자 실험이며 독립 재현 미확인
    - oq-019·oq-049: 부분 근거만 확보, 재정렬 현장 설계와 제조사 간 선후 집행의 공개 구현은 미확인
    - 교차 확인 0건: rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않음
- 범위 경계 위반 의심:
    - f20~f23: Dai 외는 탐색·구조를 모사한 계산 실험이라 물류창고 사례가 아님 — 5절에는 현장 유형 '기타'로 따로 두고 창고 피킹–포장 인계와 같다고 쓰지 않는다
    - f13·f14·f16: OR-Tools 는 일반 스케줄링 도구이며 로봇 관제용 스케줄러가 아님 — 제약 표현 근거로만 쓴다
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 5건(ref-1483~ref-1487, 예약 구간 ref-1483~ref-1512 안), 재사용 3건(ref-125 task_request.json, ref-377 TaskPlanner.hpp, ref-379 OR-Tools scheduling.md). 메모의 n3(BinaryPriorityScheme.cpp)은 기존 ref-390(BinaryPriorityScheme.hpp)과 다른 파일이라 새 id 로 등록. 8개 출처 모두 원문 대조 확인(GitHub 파일은 github_raw, 논문 2건은 webfetch). 검증 수정 반영: (1) Tuck 외 증분 풀이 이득의 조건을 '해법기와 배치 크기'로 정정(f18), (2) '공통 필드의 부재가 확장 구현의 불가능을 뜻하지 않는다'를 추정으로 분리(f3), (3) Dai 외 '빠른 도착만으로 전체 종료 시간이 줄지 않는다'를 추정으로 분리(f21), 앞부분은 §III 사실(f20), (4) 이진 우선순위 배분 조건을 같은 계획기 안 로봇 사이 조건과 같은 로봇 안 순서 조건으로 정정하고 벌점식 _priority_penalty × (g + h) 명시(f6·f7), (5) TaskPlanner 의 A* 최적성 보장 명시(f24), (6) 메이크스팬을 Dai 외 정의(차고지 복귀 포함 모든 로봇의 최대 총 작업 시간)로 맞춤(f12), (7) task_request.json 최상위 필드 8개·필수 2개·additionalProperties 없음 명시(f1·f2), (8) Dai 외 게재지 미확인·published 2025·저자 5명(ref-1486), (9) 기존 id 연결. 열린 질문은 해결 제안 없이 oq-019(f28)·oq-049(f29) 부분 근거만 냈다. 메모의 출처 집계 문장('원문 열람 8/8')은 검증 결과와 일치. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-10-10-02/research.md

```markdown
# 리서치 브리프 2026-10-10-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-02 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 25. 작업 배정 — MRTA |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오뿐이고, 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인'(oq-054)이 남아 있음. 운영 중 도착하는 작업과 용량·마감을 함께 다룬 다른 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 문헌 검토(ref-152)의 계열 구분·실험 플릿 규모가 '미확인'으로 남아 있고, LTAA(ref-168) 비교 결과가 출처 충돌(oq-030)로 11절에 미뤄져 있음. rmf_task TaskPlanner 최적 배정의 적용 범위(한 플릿)가 명시되지 않음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — Open-RMF 입찰(BidProposal)이 담는 필드가 구체적으로 적혀 있지 않고, 2026-09-26 rmf_fleet_adapter 2.14.0 의 플릿 이름 필터 수정이 반영되지 않음(바뀐 출처)
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 2024~2026 연구(마감 제약 SMT 배정, 혼잡 환경 재분배 배정 MRTA-RM, 최소 비용 흐름 기반 대규모 배정) 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 두 수준 배정에서 제조사 관제가 내야 할 비용·상태 정보(oq-053)가 미확인으로 남아 있음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-030·oq-053·oq-054 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. oq-030 LTAA(arXiv 2512.02810) 원문은 LLM 배정과 동적 계획법·강화학습의 성공률을 어떤 조건에서 비교했고, 초록의 '전통 기법을 모두 앞섰다'는 표현은 본문 수치와 맞는가? (섹션 6·11 겨냥)
3. oq-053 ROP 가 플릿 단위로 배정하고 제조사 관제가 플릿 안에서 로봇을 고르는 두 수준 배정에서 제조사 관제는 어떤 비용·상태 정보를 내며, 한 플릿 안의 최적 배정은 어디까지 보장되는가? (섹션 6·7·9·11 겨냥)
4. oq-054 출하 마감·납기 같은 상위 업무 제약을 배정과 결합하는 공개 설계가 있는가? (섹션 5·6·11 겨냥)
5. 이동로봇 플릿 작업 배정 문헌 검토(2025-01)는 방법을 어떤 계열로 나누고 실험 플릿 규모를 어떻게 보고하는가? (섹션 6 겨냥)
6. 배정 비용에 환경 구조·혼잡을 반영해 대규모로 배정하는 최근(2024~2026) 연구와 공개 구현은 무엇이며, 그 결과는 어떤 조건의 실험인가? (섹션 6·8 겨냥)
7. 바뀐 출처: Open-RMF rmf_fleet_adapter 의 입찰 동작은 최근 판에서 어떻게 바뀌었는가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Meseguer Valenzuela·Blanes Noguera 의 2025 년 문헌 검토는 이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법을 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f2 | [사실] | 같은 문헌 검토의 표 I~V 는 계열별로 각 연구의 방법, 중앙·분산 구조, 구현 환경(프레임워크), 플릿 규모, 주요 결과를 함께 제시한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f3 | [의견] | 문헌 검토의 본문 설명과 표의 플릿 규모 값이 서로 달라, 검토된 연구의 최대 플릿 규모나 계열 간 우열을 하나의 수치로 요약하지 않는 편이 좋다. | ref-152 | 아니오 | low | 2025-01 | — | — |
| f4 | [사실] | LTAA 원문(Kaitha·Yu, 2025-12 프리프린트)의 그림 15 비교는 TEACh 데이터셋의 건설 작업에서 전체 성공률을 LTAA 75.97%, Q-learning 73%, DQN 77% 로 보고하며, 초록은 LTAA 값을 76% 로 반올림해 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f5 | [사실] | 같은 원문 p.61 은 결정적 비교군의 성공률을 brute force 0.77, greedy 0.81, 동적 계획법(Dynamic Programming, DP) 0.95 로 적고, 이 결정적 알고리즘들은 불확실성 모델이 없어 비교 그림에서 제외했으며 확률적 조건의 직접 비교 기준은 강화학습이라고 설명한다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f6 | [사실] | LTAA 원문 초록은 로봇 전문화가 뚜렷한 Heavy Excels 설정에서 LTAA 가 77% 완료율과 더 나은 작업 부하 균형으로 전통 기법을 모두 앞섰다고 쓰고, 결론(p.62)은 이 설정의 성공률을 77.1% 로 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f7 | [의견] | f4~f6 을 함께 보면 원문에는 LTAA 전체 75.97%, Heavy Excels 77.1%, DP 95% 가 모두 있으나 DP 는 불확실성 모델 차이로 비교에서 빠졌으므로, 'LTAA 가 전통 배정법 전체보다 우수하다'는 결론은 지지되지 않으며 같은 조건의 LLM 대 DP 우열은 확정할 수 없고, Heavy Excels 결과와 전체 비교 결과는 분리해 적어야 한다(oq-030 부분 해소). | ref-168 | 아니오 | low | 2025-12-02 | — | — |
| f8 | [사실] | Open-RMF 의 입찰 제안 메시지 BidProposal.msg 는 입찰 공고(BidNotice)에 답해 플릿 어댑터가 내는 것으로, 플릿 이름(fleet_name), 작업을 수행할 것으로 예상되는 로봇 이름(expected_robot_name), 새 작업 수용 전·후의 전체 배정 비용(prev_cost·new_cost), 새 작업의 예상 완료 시각(finish_time) 다섯 필드를 담는다. | ref-1453 | 아니오 | medium | 2026-10-10 | — | — |
| f9 | [추정] | BidProposal 의 필드(f8)는 두 수준 배정에서 제조사 관제(플릿)가 공개하는 비용·상태 정보의 구체적인 예이지만, 이 메시지는 각 플릿이 자기 안에서 계산한 비용만 전하므로 이것만으로 모든 플릿을 합친 최적 배정이 보장되지는 않으며, 이종 플릿의 최적성 손실을 수치로 제한하는 근거는 확인하지 못했다(oq-053 부분 근거). | ref-1453, ref-404 | 아니오 | low | 2026-10-10 | — | — |
| f10 | [사실] | Open-RMF rmf_task README 는 작업 계획기(TaskPlanner)의 최적 배정을 물리·운동 특성을 공유하는 한 플릿에 속한 로봇과 주어진 작업 집합에 대해, 요청된 시작 시각을 고려해 작업이 가장 짧은 시간에 끝나도록 순서를 정하는 문제로 설명한다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | TaskPlanner 의 '최적 배정'(f10)은 한 플릿의 주어진 작업 집합에 한정되므로, 앞으로 들어올 작업, 다른 제조사 관제의 내부 결정, 실제 혼잡까지 포함한 운영 전체의 전역 최적성으로 넓혀 해석해서는 안 된다. | ref-404, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [사실] | Tuck 외(2024, NFM 2024 게재 예정 프리프린트)는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 풀이를 써서, 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 표현하고 점진(incremental) 풀이로 새 작업을 배정한다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f13 | [사실] | Tuck 외 방법의 목표는 주어진 모델에서 제약을 모두 만족하는 계획을 찾는 것이고 최소 이동 비용의 전역 최적해를 찾는 것과는 구별되며, 저자들은 알고리즘이 건전·완전하다고 증명하지만 이는 논문의 모델·인코딩 조건 안의 결과이고 국소 경로 계획·충돌 회피는 하위 계획기에 맡긴다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f14 | [의견] | 납기·마감 준수가 필수인 작업은 높은 우선순위 점수만 주는 방식과 별도로, 마감을 필수 제약으로 두는 정식화(f12)를 검토할 필요가 있으나, 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못했다(oq-054 부분 근거). | ref-1454 | 아니오 | low | 2024-03-18 | 제약 | — |
| f15 | [사실] | Tuck 외는 병원과 유사한 공간을 그래프(노드=구역, 가중치=최악 이동 시간)로 추상화한 다중 로봇 배송 벤치마크 200개(작업 10~30개, 로봇 5~20대, 최대 용량 2 또는 3, 마감 균등 분포)에서 용량 제한 로봇의 동적 작업 배정을 평가했다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 수행 자원 | — |
| f16 | [사실] | Tuck 외의 병원 모사 배송 문제에서 각 요청은 출발·도착 위치와 발생·마감 시각을 가지며, 새 요청이 들어오면 이미 실행한 동작과 현재 동작은 유지한 채 계획을 갱신한다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 시작 조건 | — |
| f17 | [의견] | Tuck 외 연구는 병원 배송의 계산 실험 사례이며 병원 현장 실증으로 분류해서는 안 된다. | ref-1454 | 아니오 | low | 2024-03-18 | 병원 / 예외·성과 | — |
| f18 | [사실] | Lee·Sim·Nam 의 MRTA-RM 은 장애물이 밀집하고 통로가 좁은 환경에서 일반화 보로노이 다이어그램(GVD)으로 로드맵을 만들고 이를 여러 구역으로 나눈 뒤 구역 사이에 로봇을 재분배하고 작업을 배정해, 충돌·교착을 줄이면서 전체 완료 시간(makespan)을 줄이려 한다. | ref-1455 | 아니오 | medium | 2025-06-08 | — | — |
| f19 | [사실] | MRTA-RM 저자들은 수백 대 규모 로봇의 동적 시뮬레이션 결과(무작위 시나리오 성공률 96% 초과, 분리 시나리오 58~100%)를 보고하고 Python 구현을 공개했으며, 결론에서 성공률 100% 달성(경로 추종 제어기)과 이종 로봇 팀 확장을 후속 과제로 남겼다. | ref-1455, ref-1456 | 아니오 | medium | 2025-06-08 | — | — |
| f20 | [의견] | MRTA-RM 은 혼잡을 줄이는 배정의 재현 후보로 볼 수 있지만, 임의 환경에서 교착이 없다는 보장으로 소개해서는 안 된다. | ref-1455 | 아니오 | low | 2025-06-08 | — | — |
| f21 | [사실] | Zhang 외의 AAMAS 2026 연구는 온라인 다중 에이전트 픽업·배송의 작업 배정을 환경 그래프 위의 최소 비용 흐름(Minimum-Cost Flow) 문제로 풀어, 선형 배정 방식이 요구하는 로봇·작업 사이 모든 쌍의 거리 행렬 계산을 피한다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f22 | [사실] | Zhang 외는 격자 지도 벤치마크(창고형 Sortation Large 포함)에서 1초 계획 예산으로 최대 20,000 에이전트와 30,000 작업까지 다뤘다고 보고하며, 이는 실제 로봇 배치가 아니라 계산 실험이다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f23 | [사실] | Zhang 외의 흐름 정식화는 기본 간선 비용으로 단위 비용을 쓰고, 선택할 수 있는 대체 비용 모델로 경로 계획기의 혼잡 추정치나 실행 중 평균 대기 시간을 배정 비용에 반영할 수 있으며, 계획기와의 결합은 6절에서 다룬다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f24 | [추정] | MRTA-RM(f18)과 Zhang 외(f21~f23)를 함께 보면 배정 비용에 환경 구조와 혼잡을 반영하는 연구 흐름은 확인되지만, 두 방법은 환경·규모·지표가 달라 성능 수치를 같은 조건의 순위로 비교할 수 없는 것으로 보인다. | ref-1455, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f25 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 작업 요청에 지정된 플릿 이름이 문자열 또는 배열에 포함되기만 하면 입찰하도록 한 수정(#534)을 기록한다. | ref-1458 | 아니오 | medium | 2026-09-26 | — | — |
| f26 | [의견] | 요청에 후보 플릿을 제한하는 배정 사례를 적을 때는 #534 수정이 포함된 rmf_fleet_adapter 패키지 버전(2.14.0 이상)을 함께 적는 편이 좋으며, 이 변경이 모든 배포판에 자동 반영되었다는 뜻은 아니다. | ref-1458 | 아니오 | low | 2026-09-26 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2501.08726 | 아니오 |
| ref-168 | Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12-02 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2512.02810 | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-1453 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg | 아니오 |
| ref-1454 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정) | SMT-Based Dynamic Multi-Robot Task Allocation | 2024-03-18 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2403.11737v1 | 아니오 |
| ref-1455 | Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293) | Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution | 2025-06-08 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2506.07293 | 아니오 |
| ref-1456 | Lee, S. 외 (SeBin-Lee-SG GitHub) | MRTA-RM_public — README | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/SeBin-Lee-SG/MRTA-RM_public | 아니오 |
| ref-1457 | Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS) | Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery | 2026-05 | 논문 | high | 2026-10-10 | https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf | 아니오 |
| ref-1458 | Open Robotics (open-rmf/rmf_ros2) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-allocation-mrta.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 병원 모사 환경의 동적 배정 계산 실험 사례 추가(f15 수행 자원·f16 시작 조건·f17 현장 실증 아님 표시), 물류창고 표 제약 행의 '출하 마감 결합 미확인'에 마감 필수 제약 정식화 근거 보충(f12·f14) / 섹션 6(주제 페이지 2026-09-25-area13-s6 반영) — 문헌 검토 문장의 '미확인'을 계열 구분·표 구성으로 교체(f1·f2)하고 최대 규모를 한 수치로 요약하지 않음(f3), LTAA 문장을 원문 수치로 교체(f4·f5·f6·f7: 전체 75.97%·Heavy Excels 77.1%·결정적 비교군 brute force 0.77·greedy 0.81·DP 0.95 의 비교 제외), TaskPlanner 최적 배정의 범위 한정(f10·f11), SMT 기반 마감·용량 배정(f12·f13) / 섹션 7(주제 페이지 s7 반영) — BidProposal 다섯 필드(f8), 메시지만으로 전 플릿 최적이 보장되지 않음(f9), rmf_fleet_adapter 2.14.0 #534(f25·f26) / 섹션 8(주제 페이지 s8 반영) — Tuck 외 2024(f12·f13), MRTA-RM(f18·f19·f20), Zhang 외 AAMAS 2026(f21·f22·f23), 두 연구 비교 한계(f24) / 섹션 9 — 두 수준 배정에서 제조사 관제가 내는 정보의 예와 한계(f8·f9·f10·f11) / 섹션 11(주제 페이지 s11 반영) — oq-030 부분 해소(f4~f7, 출처 충돌의 원인: 초록과 본문 p.61 의 서로 다른 비교 조건), oq-053 부분 근거(f8·f9·f11), oq-054 부분 근거(f12·f14), 새 질문 4건. 참고문헌 ref-168 저자 표기 정정(Yu, S. → Yu, H.; Hongrui Yu)과 ref-152·ref-168 원문 열람 반영. 기존 내용 확인: Open-RMF 입찰이 비용을 담는다는 문장(s7, ref-376)과 TaskPlanner 의 배정·충전 삽입 문장(s6, ref-404)은 이미 있으므로 중복하지 않고 세부(필드·범위)만 더한다. 다음 실행 후보: 20. 로봇·제조사 관제 연동(f8·f9·f25), 27. 다중 로봇 경로·교통 관리 — MAPF(f18·f21~f24), 47. AI·학습·적응과 모델 운영(f4~f7). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 최소 비용 흐름 | Minimum-Cost Flow | 간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다. |
| 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 47. AI·학습·적응과 모델 운영 | 근거: f5 | 종류: 일반
- 최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가? | 관련 영역: 25. 작업 배정 — MRTA, 28. 공용 자원·충전·에너지 최적화 | 근거: f21 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 9 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-02/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - f1~f3: 문헌 검토의 총 검토 편수는 선정·제외 절차가 원문에 없어 확인하지 못함
    - f4~f7: LTAA 결정적·확률적 비교군을 같은 조건으로 비교한 결과는 원문에 없음(oq-030 은 부분 해소에 그침). 초록의 '전통 기법 모두 우위' 표현과 p.61 의 DP 제외 설명의 불일치는 저자 설명이 없음
    - f8·f9: BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님. 이종 플릿 두 수준 배정의 최적성 손실을 수치로 제한하는 근거는 찾지 못함(oq-053 미해결)
    - f12: NFM 2024 게재 예정 표기는 arXiv comment 기준이며 게재본(쪽·DOI)은 확인하지 않음
    - f14: 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못함(oq-054 미해결)
    - f19: MRTA-RM 논문과 공개 구현은 같은 팀 산출물이라 독립 재현 근거가 아님. RAS 게재본은 README 표기로만 확인
    - f25·f26: #534 수정이 ROS 배포판별 바이너리에 언제 반영되었는지는 확인하지 않음
    - 모든 사실 finding 은 단일 출처라 교차 확인 0건
- 범위 경계 위반 의심:
    - f13: 국소 경로 계획·충돌 회피는 로봇 자체 지능·제어(연계 대상) 몫이며, 원문도 하위 계획기에 맡긴다고 밝혀 배정 범위만 다룸
    - f18~f24: 경로 충돌·교착·혼잡 비용은 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 배정 비용에 반영하는 부분만 이 영역에 쓰고 경로 계획 자체는 27 에 연결
    - f4~f7: LLM 기반 배정은 교차 규칙상 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것으로 양쪽에 연결
    - f15~f17: 병원 모사 환경의 계산 실험이므로 site_type 병원은 '모사 환경'으로 명시하고 현장 실증으로 쓰지 않음
- 한계: 외부 조사 변환이라 검색 횟수 집계 없음(queries 0 은 미집계 표시). 신규 출처 6건(ref-1453~ref-1458, 예약 구간 ref-1453~ref-1482 안), 재사용 3건(ref-152 리뷰 논문·ref-168 LTAA·ref-404 rmf_task README, 모두 이번에 원문 열람). 원문 열람 9/9. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·6·7·8·9·11절)과 바뀐 출처(rmf_fleet_adapter 2.14.0)만 다뤘다. 검증 수정 반영: Zhang 외 절 번호(§2 문제 정의, §5 흐름 정식화·§5.3.2 거리 행렬 회피, §6 계획기 결합, §7·§7.2·표 1 실험)와 혼잡 비용을 '선택할 수 있는 대체 비용 모델'로 범위 한정(f21~f23), LTAA p.61 의 brute force 0.77·greedy 0.81·DP 0.95 병기와 초록 76% 반올림·arXiv 2025-12-02·저자 Hongrui Yu 정정(f4~f6, ref-168), 리뷰 본문 25대·표 I 45 AMR·표 IV 48 AMR 을 의견 근거에 병기(f3), Tuck 외 NFM 2024 게재 예정(f12, ref-1454), BidProposal 필드 5개와 같은 프로젝트 자료라 독립 확인 아님(f8·f9), #534 확인(f25). 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-030 근거 f4~f7, oq-053 근거 f8·f9·f11, oq-054 근거 f12·f14. 교차 확인 0건이라 사실 finding 신뢰도는 medium 이하. 현장 유형 사례 finding 은 병원 모사 환경(f15~f17)뿐이고 물류창고 실측 비교(2절 질문)는 이번에도 찾지 못함. 국내 자료 없음. L. AI·학습 기술 관련 f4~f7 은 47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안한다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-68/research.md

```markdown
# 리서치 브리프 2026-09-25-68

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-68 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 27. AI·학습·적응과 모델 운영 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(LLM 에이전트·환각은 용어집에 있으나 등각 예측·AI 관리 시스템·모델 레지스트리 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 반영 제안 6건 대기)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 반영 제안 8건 대기)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(교차 규칙 적용 대상 5·6·13·19·21 연결 필요)
- 섹션 11. 열린 질문 비어 있음(oq-030 걸려 있음)

## 조사 질문

1. AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
2. AI 시스템의 위험 관리·거버넌스를 다루는 표준·법(NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, EU AI Act, 한국 인공지능 기본법)은 무엇을 요구하며 로봇 운영 AI에 어떻게 걸리는가? (섹션 3·7·9 겨냥)
3. LLM 이 만든 계획·해석을 실행 전에 접지·검증하고 불확실할 때 사람에게 묻는 방법(SayCan, LLM+P, Code as Policies, KnowNo, SafeGate)은 무엇인가? (섹션 4·6·8 겨냥, 트랙 nl-task-chatbot 반영 제안 확인)
4. 창고 다중 로봇 작업 배정에 학습 기반 방법(강화학습)은 어떻게 쓰이며 어떤 성능이 보고되는가? (섹션 6·8·10 겨냥, 교차 규칙상 13. 작업 배정 — MRTA)
5. 운영 중인 학습 모델의 변경·버전·시험·감시를 관리하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)
6. oq-030 LTAA(arXiv 2512.02810)의 LLM 배정 완료율 77% 주장과 동적 계획법 우위라는 2차 요약 중 어느 쪽이 원문 결과인가?
7. 국내 물류 현장에서 AI 예측·계획을 운영에 쓴 사례와 국내 규제 요구는 무엇인가? (섹션 3·5 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST 는 2023-01-26 AI 위험관리 프레임워크(AI RMF 1.0)를 자율 적용 프레임워크로 발표했으며, 핵심은 거버넌스(Govern)·맵(Map)·측정(Measure)·관리(Manage) 네 기능이고 거버넌스가 나머지 세 기능을 가로지른다. | ref-586 | 아니오 | medium | 2023-01-26 | — | 원문 미열람 |
| f2 | [사실] | ISO/IEC 42001:2023 은 AI 시스템을 개발·제공·사용하는 조직이 AI 관리 시스템(AIMS)을 수립·실행·유지·지속 개선하기 위한 요구사항을 정하는 관리 시스템 표준이다. | ref-592 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f3 | [사실] | ISO/IEC 23894:2023 은 ISO 31000 의 위험관리 원칙을 AI 에 맞게 적용한 지침으로, AI 를 개발·배치·사용하는 조직이 위험 평가·처리·감시·검토·기록을 AI 관련 활동에 통합하도록 안내한다. | ref-593 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f4 | [사실] | 한국의 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI 를 고영향 인공지능으로 두어 별도 책무를 부과한다. | ref-594 | 아니오 | medium | 2026-01-22 | 제약 | 원문 미열람 |
| f5 | [사실] | EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I 의 EU 조화 법령(기계류 등)이 적용되는 제품의 안전 구성요소로 쓰이며 제3자 적합성 평가를 받아야 하는 AI 시스템을 고위험 AI 로 분류한다. | ref-595 | 아니오 | medium | 2024-06-13 | 제약 | 원문 미열람 |
| f6 | [사실] | SayCan 은 LLM 이 상위 지시에 유용한 행동을 고르는 과제 접지(Say)와, 사전 학습된 기술의 가치 함수가 현재 실행 가능성을 판정하는 세계 접지(Can)를 곱해 실행 가능하고 맥락에 맞는 기술만 선택하게 한다. | ref-088 | 아니오 | medium | 2022-04 | — | 원문 미열람 |
| f7 | [사실] | LLM+P 는 자연어 문제 설명을 LLM 으로 PDDL 파일로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 구조로, 저자는 LLM 단독으로는 대부분 문제에서 실행 가능한 계획도 못 냈으나 LLM+P 는 대부분에서 최적 해를 냈다고 보고한다. | ref-092 | 아니오 | medium | 2023-04 | — | 원문 미열람 |
| f8 | [사실] | KnowNo 는 등각 예측(conformal prediction)으로 LLM 계획기의 불확실성을 보정해, 과제 완수에 통계적 보장을 두면서 후보 행동이 하나로 좁혀지지 않을 때만 사람에게 도움을 요청하게 하며, 모델 미세조정 없이 쓸 수 있다고 저자가 보고한다. | ref-351 | 아니오 | medium | 2023-07 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | Code as Policies 는 코드 생성 LLM 이 자연어 명령과 소수 예시를 받아 인식 출력 처리와 제어 기본 API 호출을 조합한 로봇 정책 코드를 쓰게 하는 방법으로, 사람이 정한 API 범위 안에서 명령을 재조합한다. | ref-596 | 아니오 | medium | 2022-09 | — | 원문 미열람 |
| f10 | [사실] | AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍(보정 100, 시험 900)에 모호성 유형, 명확화 질문과 답, 작업 계획을 필드로 두어 LLM 의 모호성 탐지·되묻기를 평가하게 한다. | ref-354 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | Wang 외(Learning to Ask)는 도구 호출 LLM 에이전트가 불완전한 지시에서 빠진 인자를 지어내는 문제를 다루고, 불명확 지시 벤치마크 NoisyToolBench 와 필요할 때 되묻는 방법(Ask-when-Needed)을 제안했다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f12 | [사실] | Lang2LTL 연구는 자연어 명령을 선형 시간 논리(LTL) 식으로 바꿔 접지하는 방법과, LTL 식 템플릿에서 나온 식에 영어 발화를 대응시킨 말뭉치를 제시했다. | ref-056 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f13 | [사실] | LoTa-Bench 는 언어 기반 작업 계획기의 성능을 시뮬레이터(AI2-THOR 기반 ALFRED, VirtualHome 기반 Watch-And-Help 확장)의 성공률로 자동 정량화하는 벤치마크다. | ref-541 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f14 | [사실] | SafeGate 는 자연어 작업 명령에서 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람 확인 요청·거부를 정하고, 승인된 작업을 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했다. | ref-417 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f15 | [사실] | RTAW 는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 정식화하고 주의(attention) 기반 정책을 PPO 로 학습해 총 이동 지연을 줄이며, 저자는 500개 작업에서 탐욕·후회 기반 기준 대비 최대 10% 개선과 로봇·작업 수에 독립적인 정책 크기를 보고한다. | ref-597 | 아니오 | medium | 2022-09 | 수행 자원 | 원문 미열람 |
| f16 | [사실] | Sculley 외(NeurIPS 2015)는 실제 ML 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성, 설정 문제, 외부 세계 변화 같은 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. | ref-598 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f17 | [사실] | Breck 외의 ML Test Score(IEEE Big Data 2017)는 데이터·모델·인프라 시험과 감시를 1급 관심사로 두는 28개 시험·감시 항목으로 ML 시스템의 운영 준비도를 점수화하는 기준표를 제시했다. | ref-610 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f18 | [사실] | 오픈소스 MLflow 의 모델 레지스트리는 등록 모델마다 버전·별칭·태그와 계보(어느 실험·실행이 만들었는지)를 관리하며, 운영 대상 버전에 별칭(예: champion)을 붙이고 별칭을 다른 버전으로 옮겨 운영 모델을 교체하게 한다. | ref-611 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [추정] | 국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. | ref-612 | 아니오 | low | 2026-09-19 | 출하 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | 분류 원문 질문과 관련해, 확인한 접근을 종합하면 AI 가 만든 계획·해석을 실행에 쓰는 기준은 (1) 실행 가능성 접지(SayCan), (2) 형식 명세·계획기 경유 검증(LLM+P, Lang2LTL), (3) 불확실할 때 사람 확인(KnowNo, Ask-when-Needed), (4) 실행 전 안전 판정(SafeGate), (5) 승인된 모델 버전·시험 기준(ML Test Score, 모델 레지스트리, ISO/IEC 42001)의 겹 구조로 정리될 수 있어 보인다. | ref-088, ref-092, ref-056, ref-351, ref-359, ref-417, ref-610, ref-611, ref-592 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f21 | [추정] | 피킹 단계에서 관리자가 '오늘 마감 주문을 B구역부터 피킹'처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. | ref-092, ref-351, ref-354 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | 원문 미열람 |
| f22 | [추정] | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려면 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고, 교체 전 시험·감시 기준을 통과시켜야 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. | ref-611, ref-610, ref-597, ref-598 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f23 | [추정] | ROP 가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리이고, 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 이를 둘러싼 운영 틀로 보인다. | ref-592, ref-586, ref-593, ref-351, ref-611 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f24 | [추정] | 연계 대상: 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(Code as Policies 의 저수준 정책 코드, SayCan 의 사전 학습 기술)과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP 는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. | ref-596, ref-088 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f25 | [추정] | 27. AI·학습·적응과 모델 운영의 방법은 교차 규칙에 따라 학습 기반 배차로 13. 작업 배정 — MRTA(RTAW), 실행 전 안전 판정과 제품 안전 구성요소 규제로 25. 안전·위험 관리(SafeGate, EU AI Act), 사람 확인 요청으로 18. 사람–로봇 협업·운영 인터페이스(KnowNo), 모델 버전·변경으로 24. 자산·소프트웨어 수명주기 관리, 평가 벤치마크로 23. 시험·형식 검증·벤치마크(LoTa-Bench)와 맞물리는 것으로 보인다. | ref-597, ref-417, ref-595, ref-351, ref-611, ref-541 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-586 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | 정부·연구기관 | medium | 2026-09-25 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 예 |
| ref-592 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/42001 | 예 |
| ref-593 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/77304.html | 예 |
| ref-594 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 예 |
| ref-595 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-088 | Ahn, M. 외 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2204.01691 | 예 |
| ref-092 | Liu, B. 외 | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2304.11477 | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-596 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.07753 | 예 |
| ref-597 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.05738 | 예 |
| ref-598 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | 논문 | medium | 2026-09-25 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 예 |
| ref-610 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | 논문 | medium | 2026-09-25 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 예 |
| ref-611 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry \| MLflow AI Platform | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://mlflow.org/docs/latest/ml/model-registry/ | 예 |
| ref-612 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | 기사 | low | 2026-09-25 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 예 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/cog-model/AmbiK-dataset | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2302.11649 | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-417 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f20(분류 원문 질문, 추정), f4·f5(국내외 규제 맥락), f16 / 4절: f8(등각 예측), f2(AIMS), f18(모델 레지스트리), f6(접지) / 5절: f21(피킹·시작 조건), f22(출하·예외·성과), f19(출하, 벤더 주장 병기) / 6절: f6·f7·f9·f8·f11·f14(LLM 계획 접지·검증·되묻기·안전 판정 — 트랙 nl-task-chatbot 반영 제안 2026-09-25-04·21·30·37 확인분), f15(학습 기반 배차), f16·f17·f18(모델 운영) / 7절: f1·f2·f3·f4·f5, f18 / 8절: f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17(트랙 반영 제안 2026-09-25-04·30·62 확인분) / 9절: f23(직접), f24('연계 대상') / 10절: f25와 교차 규칙 원문(5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석) / 11절: oq-030 유지와 open_questions_new 3건. 다음 실행 후보: 도면 해석(2026-09-25-05·36·54)과 매뉴얼 추출(2026-09-25-57) 반영 제안, LLM 다중 로봇 서베이·ROSA·RAI(2026-09-25-21)는 출처 메타데이터가 입력에 없어 이번 브리프에서 재확인하지 못함 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 등각 예측 | Conformal Prediction | 보정 데이터로 예측 집합의 크기를 정해, 정답이 집합에 들어갈 확률을 사용자가 정한 수준 이상으로 통계적으로 보장하는 불확실성 정량화 방법이다. |
| AI 관리 시스템 | Artificial Intelligence Management System (AIMS) | 조직이 AI 의 책임 있는 개발·제공·사용을 위한 정책·목표·프로세스를 세우고 운영하는 관리 체계로, ISO/IEC 42001 이 요구사항을 정한다. |
| 고영향 인공지능 | High-impact AI (Korea AI Basic Act) | 한국 인공지능 기본법에서 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있어 별도 책무가 부과되는 영역의 AI 시스템이다. |
| 모델 레지스트리 | Model Registry | 학습된 모델의 버전·별칭·태그·계보를 한곳에서 관리해 어떤 버전을 운영에 쓰는지 정하고 교체·되돌림을 추적하게 하는 저장소다. |

## 열린 질문

새로 생긴 질문:

- 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반
- LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 25. 안전·위험 관리 | 근거: f5 | 종류: 일반
- KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f8 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처 또는 종합 추정)
    - oq-030 LTAA 출처 충돌 미조사: 예산 배분상 이번 실행에서 원문 결과 확인 못 함(미해결 유지)
    - f5 EU AI Act 고위험 적용 시점은 개정 논의로 요약 간 차이가 있어 넣지 않음
    - f4 인공지능 기본법 고영향 영역 목록과 개정 법률 시행일(2026-07-21 언급) 원문 미확인
    - f15 RTAW 개선 수치는 저자 보고, 원문 미열람
    - f19 한진 사례의 수치·검증 조건 미확인(기사, 벤더 주장)
    - ref-594·ref-595·ref-611·ref-354·ref-541 발행일 미확인
    - 현대자동차·마키나락스 로봇 고장 예측 사례는 검색 요약에만 있고 출처 기사를 특정하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f24: 저수준 정책·파지 학습과 수요예측은 분류 원문 9장 로봇 자체 지능·제어, 상위 업무 시스템 쪽이라 '연계 대상:'으로 표시
    - f19: 간선차량 상·하차 시점 예측은 거점 간 운송과 맞닿아 있어 입출고 시간·접안 동기화 범위로만 제안
    - f14: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f8 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 다시 작성했다(검색 12회/30). 이번 브리프의 f8 은 KnowNo 논문(ref-351) 근거이며 벤더 문서가 아니다. 벤더·기업 주장은 f19 한 건뿐이고 vendor_claim: true, 태그 추정, evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다. web_fetch_available: false · fetch_mode mirror_only: 이번 출처는 GitHub 공식 저장소 미러가 없어 모두 원문 미열람(fetched false, 신뢰도 상한 medium). 신규 출처 14건(ref-586~ref-612, 예약 구간 안), 재사용 5건(ref-354·ref-359·ref-056·ref-541·ref-417, 참고문헌 목록 요약이 입력에 없어 이전 브리프 표의 값 사용, 신뢰도는 high 금지 규칙으로 medium). 트랙 반영 제안 15건 중 LLM 접지·검증·불확실성·안전 판정·평가 벤치마크 관련(2026-09-25-04·30·37·62 일부)은 f6~f14 로 확인했고, 도면 해석(2026-09-25-05·36·54)·매뉴얼 추출(2026-09-25-57)·LLM 다중 로봇 서베이(2026-09-25-21) 제안은 출처 메타데이터가 입력에 없고 예산 배분상 재확인하지 못해 '다음 실행 후보'로 남겼다. 교차 규칙: 학습 배차는 13. 작업 배정 — MRTA 와 양쪽 연결(f15·f25). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 한국 자료: 인공지능 기본법(ref-594), 국내 물류 AI 기사(ref-612). 정정 요청 없음.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
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

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope
…(발췌: 전체 207,642자 중 앞 48,820자)
````

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |

A vertex is a fundamental component of multiple annotations.
Walls, measurements, doors, floor polygons and traffic lanes are created from two or more vertices.
To create a vertex, click on the vertex icon in the `Toolbar` and then click anywhere on the canvas.
The default attributes of a vertex are its coordinates along with an empty name field.
Additional attributes may be added by first selecting the vertex (which will turn it red), and then clicking the `Add` button in the figure.
Short descriptions of these are presented below:
* **is_holding_point:** if true and if the waypoint is part of a traffic lane,
  the `rmf_fleet_adapter` will treat this as a _holding point_ during path
  planning, i.e., the robot is allowed to wait at this waypoint for an indefinite
  period of time.
* **is_parking_spot:** robot's parking spot. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L73-L76)
* **is_passthrough_point:** waypoint which the robot shouldnt stop. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L63-L68)
* **is_charger:** if true and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will treat this as a charging station.
* **is_cleaning_zone** indicate if current waypoint is a cleaning zone, specifically for `Clean` Task.
* **dock_name:** if specified and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will issue an `rmf_fleet_msgs::ModeRequest` message with
  `MODE_DOCKING` and `task_id` equal to the specified name to the robot as it approaches this waypoint. This is used when the robot is executing their custom docking sequence (or custom travel path).
* **spawn_robot_type:** the name of the robot model to spawn at this waypoint in
  simulation. The value must match the model's folder name in the assets
  repository. More details on the robot model and plugin required for simulation
  can be found in [Simulation](simulation.md)
* **spawn_robot_name:** a unique identifier for the robot spawned at this
  waypoint. The `rmf_fleet_msgs::RobotState` message published by this robot
  will have `name` field equal to this value.
* **pickup_dispenser** name of the dispenser workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **dropoff_ingestor** name of the ingestor workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **human_goal_set_name** The `goal_sets.set_area` name, used by crowd simulation. For more info about `crowd_sim`, please see the [Crowdsim section] (https://osrf.github.io/ros2multirobotbook/simulation.html#crowdsim) of the Simulation Chapter for more details.

![Vertex attributes](images/traffic_editor/add_vertex.png)

Each vertex is stored in the `tutorial.building.yaml` file as a list of x-coordinate, y-coordinate, elevation, vertex_name and a set of additional parameters.

```yaml
  vertices:
    - [1364.76, 1336.717, 0, magni1_charger, {is_charger: [4, true], is_parking_spot: [4, true], spawn_robot_name: [1, magni1], spawn_robot_type: [1, Magni]}]
```
### Adding a measurement
|                    Icon                    |
|:------------------------------------------:|
| ![Measurement icon](images/traffic_editor/icons/measurement.svg)|

Adding a measurement sets the scale of the imported 2D drawing, which is essential for planning and simulation accuracy.
Scalebars or reference dimensions in the floor plan aid with the process. Often, you can draw the measurement line directly on top of a reference scale bar in a drawing.
With the editor in _Building_ mode, select the _Add Measurement_ tool and click on two points with known dimensions.
A pink line is rendered on the map with two vertices at its ends at the selected points.

Note:
A measurement line may be drawn by clicking on existing vertices.
In this scenario, no additional vertices are created at its ends.

Selecting the line populates various parameters in the Properties window of the `Sidebar`.
Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.
Currently, you must save the project and restart `traffic-editor` to see the changes reflected (todo: fix this...).

![Measurement properties](images/traffic_editor/add_measurement.png)

The above process adds two `vertices` and a `measurement` field to the `tutorial.building.yaml` file as seen below.
For the measurement field, the first two elements represent the indices of vertices representing the ends of
the line.
The `distance` value is stored in a sub-list of parameters.

```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
    measurements:
      - [1, 0, {distance: [3, 8.409]}]
    vertices:
      - [2951.728, 368.353, 0, ""]
      - [2808.142, 1348.9, 0, ""]

lifts:
  {}
name: building
```

### Adding a wall
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Wall icon](images/traffic_editor/icons/wall.svg)| `w` |

To annotate walls in the map, select the _Add Wall_ icon from the `Toolbar` and click on consecutive vertices that represent the corners of the wall.
The process of adding wall segments is continuous, and can be exited by pressing the `Esc` key.
Blue lines between vertices are rendered on the map which represent the drawn walls.
If the corner vertices are not present, they will automatically be created when using this tool.
Meshes of the annotated walls are automatically generated during 3D world generation using `building_map_generator`.
By default, the walls are of thickness of 10cm and height 2.5m.
The `wall_height` and `wall_thickness` attributes may be
modified [in the source code](https://github.com/open-rmf/rmf_traffic_editor/blob/main/rmf_building_map_tools/building_map/wall.py#L16-L17).

Wall texture options are available [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) in the source code.

![Annotating walls](images/traffic_editor/add_wall.png)

Walls are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices of the wall segment along with an empty parameter set.
```yaml
    walls:
      - [3, 4, {}]
      - [4, 5, {}]
      - [5, 6, {}]
      - [6, 7, {}]
      - [6, 8, {}]
      - [8, 9, {}]
```

### Adding a floor
|                    Icon                    |
|:------------------------------------------:|
| ![Floor icon](images/traffic_editor/icons/floor.svg)|

Flooring is essential for simulations as it provides a ground plane for the robots to travel over.
Floors are annotated using the _Add floor polygon_ tool from the `Main Toolbar` in _Building_ edit mode.
To define a floor, select consecutive vertices to create a polygon that accurately represents the flooring area as seen below.
These vertices will need to be added manually prior to this step.
Once created, save the project and reload.
Selecting the defined floor highlights its texture attributes. Similarly, [default list of available textures](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) is available in the source code.

![Highlighting floor's textures](images/traffic_editor/add_floor.png)

Certain scenarios may call for floors with cavities, for example, to represent elevator shafts.
The _Add hole polygon_ tool may be used for this purpose.
Additionally, the shape of a drawn polygon (floor or hole) may be modified using the _Edit polygon_ tool.
Clicking on the tool after selecting an existing polygon enables the user to modify vertices of the polygon.

Each polygon is stored in the `tutorial.building.yaml` file in the format below:
```yaml
    floors:
      - parameters: {texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [11, 10, 14, 15, 13, 12]
```

### Adding a door
|                    Icon                    |
|:------------------------------------------:|
| ![Door icon](images/traffic_editor/icons/door.svg)|

A door between two vertices can be added in _Building_ edit mode by selecting the _Add door_ tool from the `Main Toolbar`, and clicking on vertices representing the ends of the door.
Selecting an annotated door highlights its properties as seen in the figure below.
Presently, four door `types` are supported: "hinged", "double_hinged", "sliding" and "double_sliding".
The `motion_degrees` parameter specifies the range of motion in the case of hinged doors while the `motion_direction` dictates the direction of swing.
In order for the door to work in simulation, a `name` must be given to the door.

![Door type properties](images/traffic_editor/add_door.png)

Doors are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices along with the set of parameters that describes the door.

```yaml
 doors:
      - [24, 25, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, 1], name: [1, D001], type: [1, double_sliding]}]
```

### Adding a traffic lane
One of the most important tools in the `traffic_editor` GUI is the _Add lane_ tool.
The allowable motions of each fleet operating in the facility is conveyed through its respective Graph which consists of waypoints and connecting lanes.
In this approach, we assume that robots travel along effectively straight-line paths between waypoints.
While this may be perceived as an oversimplification of paths taken by robots that are capable of autonomous navigation, in practice the assumption holds fairly well given that these robots mostly travel along corridors or hallways and seldom in unconstrained open spaces.
For example, even in theoretically unconstrained spaces like building lobbies or shopping-mall atriums, it is likely that the site operator would prefer for the robots to operate in a "traffic lane" on the edge of the space, in order to not impede typical human traffic flows.

The `traffic` tab in the `Sidebar` has a default of nine Graphs for nine different fleets. To annotate lanes for a graph, say Graph 0, select the Graph from the `traffic` tab and click the _Add lane_ tool.
Lanes for this graph can be drawn by clicking vertices to be connected.
If a vertex is not present, it will automatically be added. Properties may be assigned to each vertex as described in the preceding section.
To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint.

![Graphs' lane colors](images/traffic_editor/add_lane.png)

Each Graph has a unique color for its lanes, and their visibility may be toggled using the checkbox in the `traffic` tab.
A lane that is defined between two waypoints may be configured with these additional properties:
* **bidirectional:** if `true`, the `rmf_fleet_adapter` will plan routes for its
  robot assuming the lanes can be traversed in both directions. Lanes that are
  not bidirectional have arrows indicating their directionality (indigo lanes in
  figure above). A handy shortcut is that when a lane segment is selected, you can
  press the `b` key to toggle between unidirectional and bidirectional motion along that lane.
* **graph_idx**: the Graph number a lane corresponds to
* **orientation**: constrain the lane to make the robot travel in `forward` or `backward` orientation. This can be useful for the final lane segment approaching a docking point or charger, for example.

While lifts that move between levels are now supported in the `traffic_editor`, the **demo_mock_floor_name** and **demo_mock_lift_name** properties were originally engineered to showcase shared lift access in a single floor demonstration environment with a "mock" lift that receives lift commands and transmits lift states but does not actually move between any different floors in a building.
However, as there may be interest in such functionality for testing single-floor hardware setups that seek to emulate multi-floor scenarios, these properties were retained.

* **demo_mock_floor_name**: name of the floor that the robot is on while
  traversing the lane
* **demo_mock_lift_name**: name of the lift that is being entered or exited
  while the robot traverses the lane

To further explain these properties, consider this representation of a
navigation graph where numbers are waypoints and letters are lanes:
```
1 <---a---> 2 <---b---> 3

Waypoint 1 is on floor L1
Waypoint 2 is inside the "lift" named LIFT001
Waypoint 3 is on floor L3
The properties of edge "a" are:
    bidirectional: true
    demo_mock_floor_name: L1
    demo_mock_lift_name: LIFT001
The properties of edge "b" are:
    bidirectional: true
    demo_mock_floor_name: L3
    demo_mock_lift_name: LIFT001
```

If the robot is to travel from waypoint 1 to waypoint 3, the `rmf_fleet_adapter` will request for the "mock lift" to arrive at L1 when the robot approaches waypoint 1.
With confirmation of the "lift" at L1 and its doors in "open" state, the robot will be instructed to move into the "lift" to waypoint 2.
Once the "lift" indicates that it has reached L3, the robot will exit along lane b toward waypoint 3.

Note: when annotating graphs, it is highly recommended to follow an ascending sequence of graph indices without skipping intermediate numbers. Drawn lanes can only be interacted with if their associated Graph is first selected in the `traffic` tab.

The annotated Graphs are eventually exported as `navigation graphs` using the `building_map_generator` which are then used by respective `rmf_fleet_adapters` for path planning.

Lanes are stored in the following format in `tutorial.building.yaml`.
The data structure is a list with the first two elements representing the indices of the two vertices of the lane and a set of parameters with configured properties.
```yaml
    lanes:
      - [32, 33, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 2], orientation: [1, forward]}]
```

### Deriving coordinate-space transforms

Coordinate spaces are confusing!
For historical reasons, the GUI internally creates traffic maps by annotating images, so the "raw" annotations are actually encoded in pixel coordinates of the "base" floorplan image, in pixel coordinates, with +X=right and +Y=down, with the origin in the upper-left of the base floorplan image.
However, during the building map generation step, the vertical axis is flipped to end up in a Cartesian plane, so the vast majority of RMF (that is, everything downstream of traffic-editor and the building map generators) uses a "normal" Cartesian coordinate system. (As an aside -- the next version of traffic-editor is intended to be more flexible in this respect, and will default to a normal Cartesian coordinate system (not an image-based coordinate system), or even global coordinates (lat/lon). Although preliminary work is underway, there is not a hard schedule for this next-gen editor at time of writing, so the rest of this chapter will describe the existing `traffic-editor`.)

Although `traffic-editor` currently uses the upper-left corner of the base floorplan image as the reference frame, maps generated by robots likely will have their origin elsewhere, and will likely be oriented and scaled differently.
It is critical to derive the correct transform between coordinate frames in `traffic_editor` maps and robot maps as
`rmf_fleet_adapters` expect all robots to publish their locations in the RMF coordinate system while the `rmf_fleet_adapters` also issue path requests in the same frame.

To derive such transforms, the `traffic_editor` GUI allows users to overlay robot maps on a floor plan and apply scale, translation and rotation transformations such that the two maps align correctly.
The user can then apply the same transformations to convert between robot map and RMF coordinates when programming interfaces for their robot.

The robot map can be imported by clicking the `Add` button from the `layers` tab in the `Sidebar`.
A dialog box will then prompt the user to upload the robot map image.
The same box contains fields for setting the scale for the image along with applying translations and rotation.
Through visual feedback, the user can determine appropriate values for these fields.
As seen in the image below, importing the robot-generated map into the GUI has it located and oriented
differently than the floor plan.
With the right transformation values, the two maps can be made to overlap.

![Overlap robot-generated map](images/traffic_editor/coordinate_transform.png)

### Adding fiducials
|                    Icon                    |
|:------------------------------------------:|
| ![Fiducial icon](images/traffic_editor/icons/fiducial.svg)|

For maps with multiple levels, fiducials provide a means to scale and align different levels with respect to a reference level.
This is crucial for ensuring dimensional accuracy of annotations across different levels and aligning the
same for simulation.
Fiducials are reference markers placed at locations which are expected to be vertically aligned between two or more levels.
For example, structural columns may run through multiple floors and their locations are often indicated on floor plans.
With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived between the two levels.
This transformation can then be applied to all the vertices and models in the newly defined level.

To begin, add two or more non-collinear fiducials to the reference level with unique `name` attributes using the _Add fiducial_ tool (left image in figure below).
In the newly created level, add the same number of fiducials at locations that are expected to be vertically aligned with matching names as the reference level (right image in figure below).
Saving and reloading the project computes the transformation between the levels which is evident from the Scale
and X-Y offsets for the new level as seen in the `levels` tab.
This level is now ready to be annotated.

![Adding fiducials](images/traffic_editor/add_fiducial.png)

For each level, fiducials are stored in a list of their X & Y coordinates along with their name.
```yaml
    fiducials:
      - [936.809, 1323.141, F1]
      - [1622.999, 1379.32, F2]
      - [2762.637, 346.69, F3]
```

### Adding a lift
Lifts are integral resources that are shared between humans and robot fleets in multi-level facilities.
To add a lift to a building, click the `Add` button in the `lifts` tab in the `Sidebar`.
A dialog box with various configurable properties will load.
It is essential to specify the Name, Reference level and the X&Y coordinates (pixel units) of its cabin center.
A yaw (radians) may further be added to orient the lift as desired.
The width and depth of the cabin (meters) can also be customized.
Lifts can be designed to have multiple cabin doors which may open at more than one level.
To add a cabin door, click the `Add` button in the box below the cabin image.
Each cabin door requires a name along with positional and orientational information.
Here, the X&Y coordinates are relative to the cabin center.

![Configuring lift properties](images/traffic_editor/add_lift.png)

The configured lift is stored in the `tutorial.building.yaml` file as described below:
```yaml
lifts:
  LF001:
    depth: 2
    doors:
      door1:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: 1
        y: 0
      door2:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: -1
        y: 0
    level_doors:
      L1: [door1]
      L2: [door2]
    reference_floor_name: L1
    width: 2
    x: 827
    y: 357.7
    yaw: 1.09
```

After adding the lift, we would also wish to let our robots to transverse through the lift.
To achieve that, the user needs to create vertices/waypoints which are located within the lift cabin on each floor.
Once done, connect the waypoint within the lift cabin to other vertices via __add_lane__.

### Adding environment assets
Levels may be annotated with thumbnails of models available for simulation using the __Add model__ tool in __Building__ edit mode.
Selecting this tool opens a dialog box with a list of model names and matching thumbnails which can be imported to the map.
Once on the map, their positions and orientations can be adjusted using the _Move_ and _Rotate_ tools. Sample models are provided [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor_assets/assets/thumbnails/images/cropped/OpenRobotics)

The [thumbnail_generator documentation](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor#generating-custom-thumbnails) contains instructions on expanding the list of thumbnails for other models.

> Note: If no models are shown on the __add models__ window, Go to "Edit -> Preference", then indicate the thumbnail path. (`e.g. $HOME/rmf_ws/src/rmf/rmf_traffic_editor/rmf_traffic_editor_assets/assets/thumbnails`)

![Model name and thumbnails dialog](images/traffic_editor/add_model.png)

## Conclusion
This chapter covered various capabilities of the `traffic_editor` which are useful for annotating maps of facilities while adhering to a standardized set of semantics.
Examples of other traffic editor projects can be found in the [rmf_demos](https://github.com/open-rmf/rmf_demos) repository.
Running physics based simulations with RMF in the annotated sites is described in the [Simulation](simulation.md) chapter.
````
