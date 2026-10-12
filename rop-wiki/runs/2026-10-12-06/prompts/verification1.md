(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-06
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 46. 예측·학습 기반 최적화 (L. AI·학습 기술)
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

### runs/2026-10-12-06/target.json

```json
{
  "run_id": "2026-10-12-06",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 178,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 46,
    "area_name": "46. 예측·학습 기반 최적화",
    "category": "L. AI·학습 기술",
    "category_letter": "L"
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
  "selection_rationale": "CLI 지정 run_type=update, area=46"
}
```

### runs/2026-10-12-06/research.json

```json
{
  "run_id": "2026-10-12-06",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 46,
    "area_name": "46. 예측·학습 기반 최적화",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 5. 적용 사례 — 물류창고 사례 74행 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 이 원문의 미래형·지표 차이(이동 시간 대 배치 효율)를 반영하지 못함. 병원 사례가 초록 기준이라 평가 조건(층·기간·시뮬레이션)과 수치가 없음. 국내 학습 기반 배정 사례·연구가 없음(oq-224)",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area46-s6) — '학습 실패 시 고전 정책 복귀' 가 일반론이고, 대체 정책 호출·예측 가중치 조정의 평가 근거가 없음. 2026년 학습 기반 LMAPF(RL-RH-PP JAIR, SJRL)와 최신 고전 기준선(PUSH)의 조건 비교 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 지도·통신 한계 없음, League of Robot Runners 행이 SILLM 저자의 2023 우승 해법 비교만 근거로 함(2026 시즌 평가 구성·결과 없음), SILLM 공식 구현 없음, ISO 13381-1 서지(발행일·소관 SC) 불완전",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area46-s8) — SILLM '최고 탐색 기반 기준선보다 16.0%' 가 지도별 예외(WPPL 우세 3개 지도)·계획 시간·훈련 비용 없이 실림, Garces 외 '구체 수치는 초록에 없다', SPO '학술지 게재 연도 미확인'",
    "섹션 9. 책임 경계 — 158행 '수요 예측 경계는 아직 정하지 않았다'(oq-223), 배터리 SoC 물리 모델 추정과 학습 예측의 구분, WCS 통합 제어 발표와 학습 기반 배정의 구분 없음",
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area46-s4) — 예지 정비·충전 상태 항목이 인계 값의 종류(SoC 변화·이상 클래스·예지)를 구분하지 않음",
    "섹션 11. 열린 질문(분리 2026-09-30-area46-s11) — oq-220~oq-224 가 id 없이 실려 있고 부분 근거가 없음. 정정 요청 없음(target.json corrections 비어 있음)"
  ],
  "research_questions": [
    "학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]",
    "학습 기반 지속형 MAPF 의 평균 개선율(SILLM 16.0% 등)은 지도·밀도·계획 예산·훈련 비용 조건에서 어떻게 달라지며, 최신 대회(LoRR 2026)와 고전 기준선(PUSH)은 어떤 조건으로 평가하는가? (섹션 6·7·8 겨냥)",
    "oq-220 학습 기반 배정·경로 정책의 개선을 실제 운영 현장에서 제3자가 측정한 자료가 있는가, 시뮬레이션·혼합 현실·회사 주장은 각각 무엇을 보여 주는가? (섹션 5·8·11 겨냥)",
    "oq-222 학습·예측 정책이 실패하거나 요청 분포가 바뀔 때 대체 정책 호출과 예측 가중치 조정은 어떻게 설계·평가되는가? (섹션 6·8·11 겨냥)",
    "oq-221 배터리 잔량·이상 분류·예지 출력은 어떤 조건에서 나오며 플릿 일정에 어떤 값으로 인계되는가? (섹션 4·9·11 겨냥)",
    "oq-223·oq-224 상위 수요예측과 ROP 작업 요청의 경계는 어떻게 나누며, 국내 학습 기반 배정 연구·산업 발표는 무엇을 보여 주는가? (섹션 5·9·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "POGEMA 벤치마크의 분포 밖(Out-of-Distribution) 지표는 학습에 쓴 지도와 장애물 구조가 다른 Cities-tiles 지도 묶음(Cities 지도를 잘라 고친 것)으로 계산한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1056"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v3 §4.2·부록: \"Out-of-Distribution metric was calculated on Cities-tiles dataset\", 평가용 지도는 \"different structure of obstacles\"를 갖도록 Cities-tiles 를 쓴다. 기존 위키(2026-09-30-area46-s6·s7·s8)는 LaCAM·RHCR 우위만 적고 일반화 지표의 지도 분할은 적지 않음. 격자 MAPF 벤치마크 정의이며 실물 현장 검증 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "POGEMA 저자는 한계로 에이전트 간 통신이 현재 환경에서 분리(disentangled)되어 있지 않다고 밝혀, 통신 지연·손실을 따로 평가하는 구조가 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1056"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v3 §5(한계): \"communication between agents is not currently disentangled\". 플랫폼 자체의 명시 한계이며 통신 장애에서 안전하다는 보장이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "League of Robot Runners 2026 공식 평가는 7개 지도에 걸친 12개 인스턴스로 이루어지고, 인스턴스별 로봇(에이전트) 수 범위는 50~10,000이며, 평가 서버는 GPU 인스턴스(AMD EPYC 7R13 32 vCPU·128 GiB·Nvidia A10G)와 CPU 인스턴스(같은 CPU 32 vCPU·64 GiB)로 나뉜다.",
      "tag": "사실",
      "source_ids": [
        "ref-1637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "evaluation.md: \"12 instances across 7 maps spanning diverse domains: mazes, rooms, random grids, warehouses, and large-scale game maps\"; Benchmark Configuration Ranges 표 Team size \"50 – 10,000\"; Evaluation Process 의 GPU Instance·CPU Instance 사양. 저장소 고정 커밋 9d5e337 기준, 커밋 날짜 미확인. 시뮬레이션 평가 규칙이며 실제 창고 성과 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "LoRR 2026 본선 최종 결과는 2026-09-02 공지로 발표됐다(2026-07-23 공지는 8월 7일 발표 예정이라 했고 2026-08-10 공지로 지연을 알림). Combined Track 1위는 Team No Man's Sky(Task Scheduling Track 1위·Line Honours 도 같은 팀)이고, 2026-05-26 AAMAS Prize(Combined Track)는 Team SmartPath 로 별도 집계다. 수상 표에는 팀별 알고리즘(학습 사용 여부) 분류가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "updates.md: \"Results Announcement for Main Round 2026! `2 Sep 2026`\" 수상 표 First Place/Combined Track \"Team No Man's Sky\"; \"Delayed Announcement `10 August 2026`\"; \"Finish Line! `23 July 2026`\" 의 \"on **7 August 2026**\"; \"2026 AAMAS Prize Announcement `26 May 2026`\" Team **SmartPath**. 참가 69팀·제출 3,361건. rules.md 3항: 제출 코드는 결과 발표 뒤 공개",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "대회 순위는 팀별 최종 제출 코드에서 학습을 어디에 썼는지 확인하기 전에는 학습 대 고전 방법의 승률로 바꾸지 말고, 인용할 때 시즌·트랙·인스턴스 구성·CPU/GPU 조건을 함께 적는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f3·f4 에 근거한 판단. 수상 표에 알고리즘 분류가 없고 평가 자원이 GPU·CPU 두 구성으로 나뉜다(evaluation.md). LoRR 2026 의 주 위치는 27·54·25 영역이며 46 에는 요약·연결만 둔다",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "SILLM 논문 Table III(대형 지도·에이전트 10,000, 8회 평균 처리량)에서 WPPL 이 SILLM 보다 높은 지도가 6개 중 3개(Sortation 44.28 대 43.98, Warehouse 42.83 대 42.24, Random-1 54.38 대 53.74)이고, SILLM 은 Paris(31.00 대 23.74)·Berlin(30.52 대 20.35)·Random-2(44.37 대 37.30)에서 높았다. 단계당 평균 계획 시간은 SILLM 0.349초, WPPL 4.143초였다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v2 Table III 오른쪽(Large maps with 10,000 agents) SILLM 행 \"43.98 42.24 31.00 30.52 53.74 44.37 … 0.349\", WPPL 행 \"44.28 42.83 23.74 20.35 54.38 37.30 … 4.143\". 비교 WPPL 은 회전 동작 제거·LNS 반복 40,000회 제한 조건(부록 F.1, 기존 2026-10-10-area27-s8.md 42행에 있음)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "초록의 '최고 탐색 기반 기준선 대비 16.0%'는 Table III 대형 지도 6종에서 WPPL 대비 지도별 처리량 비율을 평균한 값(재계산 약 16.05%)과 일치하므로, 모든 지도에서 16% 앞섰다는 뜻이 아니라 지도별 비율의 평균으로 읽는 것이 맞아 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 \"throughput improvements of 137.7% and 16.0%, respectively\". Table III 값으로 (43.98/44.28+42.24/42.83+31.00/23.74+30.52/20.35+53.74/54.38+44.37/37.30)/6−1 ≈ 0.1605. 논문이 계산 방식을 명시하지 않아 해석은 추정(독립 검증 2026-10-12 재계산)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "SILLM 공식 부록은 지도마다 SILLM 모델 훈련에 12시간 미만이 걸렸다고 적으며, 훈련 서버는 72 vCPU AMD EPYC 9754·RTX 4090D(24GB) 4장·메모리 240GB였다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v2 부록 E. Computation Resources: \"trained on servers with 72 vCPU AMD EPYC 9754 128-Core Processor, 4 RTX 4090D (24GB), and 240 GB memory. Training on each map takes less than 12 hours.\" 프로젝트 부록 PDF 같은 문장",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "SILLM 공식 저장소(DiligentPanda/Scalable-Imitation-Learning-for-LMAPF) README 는 Backward Dijkstra·정적 안내(Static Guidance)·동적 안내(Dynamic Guidance) 버전을 별도 브랜치(static_guidance, dynamic_guidance)로 관리하며, Backward Dijkstra 는 정적 안내 설정에서 map_weights_path 를 비운 것과 거의 같다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1638"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(static_guidance·master 브랜치) \"Static Guidance Version\": \"we maintain Backward Dijkstra, Static Guidance and Dynamic Guidance versions in separate branches (`static_guidance`,`dynamic_guidance`)\", \"set the `map_weights_path` to `\"\"`\". 메모가 쓴 wuwen-T 저장소는 미러라 공식 저장소로 출처를 바꿈. 코드 실행·재현은 하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "공식 저장소의 1-GPU 예시 설정 파일(…sortation_small_a600_s500_none_annotated_1gpu.yaml)은 max_dagger_iterations 를 100으로 두지만 논문은 모방 학습을 12회 반복했다고 적어, 공개 예시 설정과 논문 실험 설정은 같은 것이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1638",
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "YAML framework 절 \"max_dagger_iterations: 100 # NOTE: how many iterations of imitation learning to run\"; README 는 이 파일을 RTX4090D 1장·16 vCPU 예시로 소개. 논문 §IV \"We iterate the imitation 12 times\". 같은 연구팀 자료라 교차 확인 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "학습 기반 경로 방법의 평균 개선율을 인용할 때는 지도별 우열, 단계당 계획 시간, 지도별 훈련 비용, 공개 구현의 브랜치·설정 파일을 함께 적어야 하며, 10,000 에이전트 시뮬레이션을 실물 플릿 규모로 읽지 않는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-199",
        "ref-1638"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f6~f10 에 근거한 판단. 기존 2026-10-10-area27-s8.md 42행도 10,000 을 계산 벤치마크 규모로 읽는다",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "RL-RH-PP(강화학습 안내 롤링 호라이즌 우선순위 계획, JAIR 85, 2026-03-24 게재)의 기준선 비교는 서로 다른 시드의 보류(held-out) 평가 환경 16개 평균이며, 800단계 창고 시뮬레이션(Amazon 풀필먼트 모사·Symbotic 모사 지도)에서 모든 해법에 계획 단계당 CPU 1초를 주고 시간 초과 해에는 같은 수리 기법을 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1639"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2603.23838v1 §5.1.3: \"Each solver is allocated a total time budget of 1s CPU time per planning step\", \"we apply the same repair mechanism … to any infeasible solution returned upon solver timeout\", \"averaged over 16 held-out evaluation environments with different random seeds\", \"T = 800\". JAIR 메타데이터 citation_date 2026/03/24, DOI 10.1613/jair.1.20611. MIT·Symbotic 공동 저자",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "RL-RH-PP 논문 Table 3 의 Symbotic 모사 지도에서 에이전트당 처리량은 80대일 때 RH-PBS 20.83 이 RL-RH-PP 18.38 보다 높았고, 100대(15.38 대 14.04)·120대(11.31 대 1.76)에서는 RL-RH-PP 가 높았다. 같은 표의 WPPL 은 16.29·13.73·10.05 였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1639"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Table 3 Symbotic 블록: \"RH-PBS 20.83 ± 1.32 … 14.04 ± 5.39 … 1.76 ± 1.10\", \"RL-RH-PP (ours) 18.38 ± 0.50 … 15.38 ± 1.85 … 11.31 ± 2.21\", \"WPPL 16.29 … 13.73 … 10.05\" (열 N=80·100·120, TPA). 동료 심사 학술지 게재지만 단일 연구의 자체 비교. 메모는 [추정]으로 냈으나 표 값 보고는 원문 확인이 되어 [사실], 해석은 밀도별로 한정",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "RL-RH-PP 는 에이전트 밀도마다 정책을 처음부터 따로 학습했고, 가장 긴 훈련(120대)은 RTX 6000 Ada GPU 한 장으로 약 4일 걸렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1639"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.1.2: \"For each agent density setting, we train a separate RL policy from scratch.\" \"The longest training duration, corresponding to N = 120, is approximately four days.\" \"a single NVIDIA RTX 6000 Ada GPU\". 온라인 추론 시간과 구별",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "LSMART 는 처리량과 함께, 계획 실패 때 대체(fail) 정책을 부른 횟수를 계획기 호출 횟수로 나눈 비율을 평가 지표로 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2602.15721v1 §4.1 Metrics: \"(1) throughput and (2) the ratio of fail policy calls\" (계획기 호출 대비). 600초×10회 실험 조건과 실패 정책 개념은 기존 2026-10-10-area27-s8.md 43행에 있음 — 새로운 것은 이 지표",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "LSMART 의 대체 정책 비교에서는 지도와 계획 창 조건에 따라 LRGW 또는 PIBT 가 가장 높은 처리량을 냈으며, 한 대체 정책이 모든 조건에서 최선은 아니었다.",
      "tag": "사실",
      "source_ids": [
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.4 Experiment Result: 대체 정책으로 \"(1) PIBT … and (2) LRGW\"를 비교하고 지도별로 \"LRGW and PIBT\"가 최고 처리량을 나눠 가짐. 차동구동 AGV 시뮬레이션이며 분포 이동 탐지 실험은 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "2026-08 프리프린트 PUSH(Path Updates over Staggered Horizons)의 비교 실험은 1,000단계 실행·단계당 1초 계획 예산·무작위 5회 평균으로, AMD Threadripper 3990X·192GB 메모리 장비에서 수행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1640"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2608.06702v1 §V-A.4 Evaluation Criteria: \"We run each experiment for 1,000 timesteps with a 1-second per-timestep planning budget … averaged over 5 randomized trials\"; §V \"AMD Threadripper 3990X 64-core processor with 192 GB of RAM\". 학습을 쓰지 않는 탐색 기반 알고리즘",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "PUSH 비교에서 RHCR 를 뺀 알고리즘은 시간 초과 시 계획 못 한 에이전트가 직전 단계 경로를 따르고, RHCR 는 K단계마다 K초를 받되 시간 초과 시 K단계 동안 PIBT 로 실행한 뒤 RHCR 로 돌아간다.",
      "tag": "사실",
      "source_ids": [
        "ref-1640"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§V-A.4: \"unplanned agents fall back on their paths from the previous timestep\", \"it receives K seconds of planning time per rolling horizon … If it times out, we default to PIBT for K steps before returning back to RHCR.\" 알고리즘마다 실패 처리가 같지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "PUSH 는 학습 요소가 없는 고전 탐색 알고리즘이므로 이 영역에서는 학습 정책을 평가할 때 맞춰야 할 고전 기준선의 예산·실패 처리 조건을 보여 주는 대조 사례로만 다루고, 학습 성과 근거로 쓰지 않는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1640"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f17·f18 에 근거한 판단. 독립 검증(2026-10-12): PUSH 는 학습과 무관해 46 에서는 대조군·경계 설명으로만",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "SJRL(탐색 보조 에이전트–환경 공동 강화학습, 2026-08 프리프린트)은 지도마다 256대로 정책을 학습해 같은 지도에서 32~320대(32대 간격)로 평가하며, 일반화는 초기 상태·목표·에이전트 수에 대해 보고 지도 간 일반화는 다루지 않는다. 각 평가는 512단계다.",
      "tag": "사실",
      "source_ids": [
        "ref-1641"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2608.05588v1 §5: \"For each map, we train a policy with 256 agents and evaluate it with 32–320 agents in increments of 32. Each evaluation runs for 512 timesteps\"; \"generalization across initial states, goal locations, and numbers of agents rather than across maps\". SILLM 과 공동 저자(Jiang·Li 등)라 독립 재현 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "SJRL 의 물리 로봇 검증은 실물 로봇 8대와 가상 로봇 248대를 섞은 혼합 현실 창고 환경에서 이루어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1641"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록·부록 C.3: \"a challenging mixed-reality warehouse environment with 8 physical robots and 248 virtual robots\". 256대 실물 운영이나 독립 창고 실측이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "SJRL 저자는 비교한 모방학습 방법들을 회전 동작을 포함한 LMAPF-R2 문제 모델에 맞게 고치는 일을 향후 과제로 남겨, 비교 방법들의 문제 모델이 같지 않다.",
      "tag": "사실",
      "source_ids": [
        "ref-1641"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.2: \"such an adaptation would require non-trivial modifications … We therefore leave the adaptation of IL methods to the LMAPF-R2 model for future work.\" 성능 차이를 모두 강화학습 자체의 이득으로 돌릴 수 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Amazon Robotics 의 DeepFleet 보고서(arXiv v3, 'Unpublished technical report')는 학습에서 제외한 7개 창고 층의 7일 자료에서 로봇 궤적을 60초 앞까지 반복 추론해 실제 궤적과 비교하는 오프라인 예측 평가를 보고한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1053"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: arXiv 2508.08574v3 §4 \"our test dataset, which consisted of 7 days across 7 warehouse floors that were held out during training\", \"roll out robot trajectories 60 seconds into the future\". arXiv 메타데이터 journal-ref \"Unpublished technical report, Amazon Robotics, Aug. 2025\" — 동료 심사 없는 회사 자체 보고서라 [추정]. 개입 대조 실험 아님",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f24",
      "claim": "DeepFleet 보고서 Table 2 에서 로봇 중심(RC) 모델의 혼잡 지연 오차(CDE)는 3.40%로 네 구조 가운데 가장 낮았다(RF 9.60%, GF 14.22%, IF 186.56%). 이는 예측한 혼잡 지연과 실제의 상대 오차이며 이동 시간 절감률이 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1053"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Table 2 \"Robot-Centric (RC) 97M 8.68 0.11 14.91 3.40\", RF \"9.60\", IF \"186.56\", GF \"14.22\" (열 CDE (%)). 회사 자체 보고서 수치",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f25",
      "claim": "Amazon 의 DeepFleet 10% 수치는 표현이 엇갈린다: About Amazon 발표(2025-07-01)는 핵심 요약에서 '이동 효율을 10% 높일 것(will improve)', 본문에서 '이동 시간을 10% 개선/줄여'라고 쓰고, Amazon Science 블로그(2025-08-11)는 '로봇 배치 효율을 10% 높이고 있다'고 쓴다. 비교 기간·대상 현장·분모는 공개하지 않아, 위키의 '이동 효율을 10% 높였다' 서술은 고쳐야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-916",
        "ref-1054"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: aboutamazon.com 요약 \"will improve robot fleet travel efficiency by 10%\", 본문 \"improving the travel time of our robotic fleet by 10%\", \"By reducing robot travel time by 10%\"(article:published_time 2025-07-01). amazon.science \"increasing the efficiency of our robot deployments by 10%\"(datePublished 2025-08-11). 두 자료 모두 Amazon 이라 독립 확인 아님",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f26",
      "claim": "예측 정확도(궤적·혼잡 오차), 오프라인 결정 손실, 온라인 운영 개선은 서로 다른 승인 지표로 두고, 운영 개선 수치는 개입 시점과 비교 플릿을 확인한 뒤에만 성과로 반영하는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1053",
        "ref-916"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f23~f25 에 근거한 판단",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "Garces 외의 병원 배정 평가는 BIDMC 서관 입원 병동 4개 층(층당 병상 약 25~30)의 2024-06-24~2025-06-29 요청 이력에서 층마다 수요 높음·중간·낮음 주를 2주씩 골라 층당 42일, 정책당 168개 층-일을 하루 12시간(오전 6시~오후 6시) 시뮬레이션한 것이며, 나머지 이력은 학습·검증에 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1062"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2608.21554v1 §5.1: \"four inpatient floors from the west wing of BIDMC\", \"The historical data span June 24, 2024 through June 29, 2025\", \"42 test days per floor and 168 floor-day evaluations per policy\", \"simulated over a 12 hour window starting at 6am\". 실물 로봇 병원 배치 아님",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f28",
      "claim": "Garces 외의 방법에서 예측 신뢰도 가중치는 표본 추출한 미래(예측) 요청에만 적용되고, 이미 관측된 요청과 예약 요청은 항상 가중치 1을 받는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1062"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.6: observed requests and scheduled requests \"always receive unit weight\", \"predicted requests are weighted according\" to 최근 예측 오차. 롤아웃의 미래 비용 평가에만 쓰이며 확정 요청을 바꾸지 않음",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f29",
      "claim": "Garces 외 Table 3 의 수요 높음 조건(요청 36,948건)에서 제안 방법과 탐욕 배정을 포함한 대부분 정책의 거절 건수는 0이었고, Token Passing 과 Token Passing with Task Swaps 만 28건을 거절했다. 저자는 처리 건수만으로는 강한 정책들을 구분할 수 없어 대기 시간으로 비교했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1062"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.5.3 Table 3 High demand: \"Greedy Assignment Policy 36,948 0\", \"Proposed Adaptive Rollout 36,948 0\", Token Passing 두 변형 \"36,920 28\"; 본문 \"aggregate rejection counts alone do not fully distinguish the stronger policies\"",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f30",
      "claim": "Garces 외는 수요 높은 주에서 제안 방법이 일별 평균 대기 시간의 중앙값을 약 5%, 일별 95분위 대기 시간의 중앙값을 약 10% 줄였고, 두 지표의 75분위와 최댓값은 기준선 대비 15% 넘게 줄였다고 보고했다. 모든 수요 구간에서 가장 크고 일관된 개선은 95분위 대기 시간 지표에서 나왔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1062"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.5.4: \"The median improvement is approximately 5% for the mean wait-time metric and approximately 10% for the 95-th percentile metric\", \"reduces the 75-th percentile and maximum values of both wait-time metrics by more than 15%\"; \"Across all demand regimes, the largest and most consistent gains appear in the 95-th percentile wait-time metric.\" 기존 s8 '구체 수치는 초록에 없다'를 본문 수치로 정정",
      "as_of": "2026-10-12",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f31",
      "claim": "분포 이동에 대응해 예측 가중치를 낮추는 장치와, 계획 실패·시간 초과 때 고전 정책으로 돌아가는 트리거는 따로 설계·기록하고, 이미 시작한 작업과 아직 시작하지 않은 배정을 구분해 다루는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1062",
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f16·f28 에 근거한 판단. 가중치 조정(Garces 외)과 대체 정책 호출(LSMART)은 다른 장치이며 공통 분포 이동 감지 임계값을 정한 근거는 확인하지 못함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "Pookkuttath 외의 실시간 진동 분류 정확도 91%는 Snail 청소 로봇에서 모바일 앱의 요청(request-based) 표본 방식으로 모은 시험 표본 100개(Table 5)로 계산한 값이며, 클래스별 정확도는 88.7~93.5%였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1057"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Europe PMC 전문(PMC8747287) §5.5: \"Table 5 shows the statistical measure result for 100 test samples collected from the real-time case study … on request-based sample mode\", \"88.9%, 93.5%, 91.8%, 92.1%, and 88.7%\", \"real-time tests is slightly less (91%)\". 기존 91%·92.2% 는 위키에 있음 — 새로운 것은 표본 수·수집 방식",
      "as_of": "2026-10-12",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f33",
      "claim": "ISO 13381-1:2025 는 ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행(단계 60.60)됐고 23쪽이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1060"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 공식 목록·공개 메타데이터: \"publicationDate\":\"2025-09-02\", \"edition\":3, \"ownerCommittee\":\"ISO/TC 108/SC 5\", \"pages\":{\"en\":23}, currentStage 6060. 규범 본문은 유료라 열지 않음. ref-1060 서지(발행 '2025', 'ISO/TC 108') 보정",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "Open-RMF rmf_battery 의 SimpleMotionPowerSink 는 로봇이 궤적을 따라 가감속하는 데 드는 에너지로 배터리 충전 상태(SoC) 변화를 추정하고, SimpleDevicePowerSink 는 탑재 장치의 소비 전력으로 SoC 변화를 추정하는 물리 모델 API 이며 학습 모델이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1642"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README API 목록: SimpleMotionPowerSink \"can estimate the change in state-of-charge of the battery from the energy consumed to accelerate/decelerate a robot as it moves along a trajectory\"; SimpleDevicePowerSink \"from the PowerSystem's energy consumption over a duration\". 고장 예지·잔여 수명 예측 성능 주장 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "배터리·고장 쪽 인계 값은 물리 모델의 SoC 변화 추정(Open-RMF rmf_battery, 28. 공용 자원·충전·에너지 최적화 맥락), 학습 모델의 현재 이상 클래스(진동 분류), 고장까지 남은 시간 같은 예지 출력을 서로 다른 값으로 구분해 넘기고, 이 영역은 학습·예측으로 얻은 값만 다루는 것이 경계로 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1642",
        "ref-1057",
        "ref-1060"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f32~f34 에 근거한 판단. 공통 고장 데이터 계약과 모델 소유권 합의는 확인하지 못함(oq-221 부분 근거)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "Open-RMF 작업 요청 스키마(task_request.json)의 fleet_name 은 플릿 이름 하나(문자열) 또는 이름 배열을 받을 수 있고, 지정하면 그 플릿(들)만 입찰한다.",
      "tag": "사실",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_request.json properties.fleet_name: \"The name of the fleet, or an array of fleet names, allowed to perform this task. If specified, only the named fleet(s) will bid for this task.\", oneOf string/array. 독립 검증: rmf_api_msgs 0.7.0 CHANGELOG(2026-09-18) \"Allow fleet_name to be either string or string array\". fleet_name 필드 자체는 기존 2026-09-29-area09-s7.md 40행에 있음 — 새로운 것은 배열 허용",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "상위 업무 시스템은 주문 전망과 시간 범위를 계획에 쓰고, ROP 는 실제로 들어온 요청을 플릿·능력·가장 이른 시작 시각 조건과 함께 받아 배정하는 것으로 책임을 나누며, 예측 요청을 확정 요청으로 자동 바꾸는 규칙은 별도 승인을 거치게 하는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-125",
        "ref-1063",
        "ref-1062"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f28·f36 에 근거한 판단. CJ대한통운 iFlex 주문 유형별 물량 예측(기존 5절·9절, ref-1063)은 상위 쪽 예시이고, Garces 외는 즉시 확정을 이미 들어온 요청에만 한다. 공통 표준으로 확인된 경계는 아님(oq-223 부분 근거)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "강민교·김인철(한국로봇학회 논문지 18(2), 2023)의 제조 물류 작업 안전성·효율성 학습 실험은 NVIDIA Isaac 시뮬레이터 안 가상 제조 물류 환경에서 이동 로봇 2대로 수행됐고, 실제 하드웨어 로봇 적용·검증은 향후 연구로 남겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1643"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.1(p.229): Isaac 시뮬레이터로 만든 실험 환경에 \"이동 로봇 2대\"·화물·이동 장애물 배치, Intel Xeon Silver 4210R·RTX A5000 3개; §5 결론: \"하드웨어 로봇들을 포함한 실제 제조 작업 환경에 적용하여 성능을 검증\"하는 것이 향후 연구. 심층 관계형 강화학습 기반 정책 규칙 학습",
      "as_of": "2026-10-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f39",
      "claim": "이 논문은 두 로봇의 정책 파라미터 등급이 같아 안전성·효율성 등급이 모두 같게 예측되는 드문 상태에서는 어느 로봇에 작업을 배정할지 판정하기 어렵다고 적고, 더 많은 정책 파라미터와 규칙이 필요하다고 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-1643"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.2(p.231): 네 번째 상태는 \"robot1과 robot2에 관해 추론된 정책 파라미터들의 등급이 모두 같아서\" … \"어느 로봇에게 작업을 할당해야 될지 판정하기 어려워진다\"",
      "as_of": "2026-10-12",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f40",
      "claim": "현대글로비스는 알티올과 공동 개발한 창고제어시스템(WCS) 플랫폼 오르카(ORCA)가 작업 계획을 실제 작업으로 바꾸고 각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정하며, 어댑터 인터페이스로 다른 제조사 설비를 같은 방식으로 연결한다고 설명한다. 학습 모델이나 고전 방법 대비 성과는 밝히지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-1644"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 현대자동차그룹 Story(2026-04-16) \"각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정합니다\", \"어댑터 인터페이스 구조를 통해 서로 다른 제조사의 설비도 동일한 방식으로 연결\". 학습되는 변수·비교 정책·현장 효과 분모 미공개",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f41",
      "claim": "오르카 같은 국내 통합 제어 발표는 학습 기반 배정·경로의 운영 효과 근거가 아니라 20. 로봇·제조사 관제 연동과 61. 물류창고 쪽 통합 운영 사례로 보고, 이 영역에서는 학습 요소가 확인되지 않은 경계 사례로만 다루는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-1644"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f40 에 근거한 판단. 독립 검증(2026-10-12): 학습 요소 없음 → 영역 20·61 맥락",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "Smart \"Predict, then Optimize\"(Elmachtoub·Grigas)는 Management Science 68권 1호 9–26쪽(2022-01)에 게재됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1061"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Crossref 서지: DOI 10.1287/mnsc.2020.3922, container-title \"Management Science\", volume 68, issue 1, page \"9-26\", published-print 2022-01. 기존 s8 '학술지 게재 연도 미확인' 정정",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "학습 기반 배정·경로 정책을 실제 운영 현장에서 탐색·규칙 기반 방법과 같은 조건으로 제3자가 측정한 자료는 이번에도 찾지 못했고, 확인한 근거는 시뮬레이션(SILLM·RL-RH-PP·Garces 외), 혼합 현실(SJRL 실물 8대+가상 248대), 회사 자체 주장(DeepFleet 10%)으로 나뉜다.",
      "tag": "추정",
      "source_ids": [
        "ref-199",
        "ref-1639",
        "ref-1062",
        "ref-1641",
        "ref-916"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f12·f27·f21·f25 를 묶은 판단. oq-220 부분 근거이며 해결 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "학습과 고전 방법의 우열은 지도·밀도·계획 예산·실패 처리(복귀 정책)를 같게 맞춘 조건에서만 판단하고, 한 논문의 평균 개선율을 다른 논문의 수치와 섞어 순위를 만들지 않는 것이 맞다고 본다.",
      "tag": "의견",
      "source_ids": [
        "ref-199",
        "ref-1639",
        "ref-1640",
        "ref-604"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f6·f13·f17·f18·f16 에 근거한 판단: SILLM 은 지도 6개 중 3개에서 WPPL 보다 낮고, RL-RH-PP 는 80대에서 RH-PBS 보다 낮으며, PUSH·LSMART 는 알고리즘마다 시간 초과 처리가 다르다",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1056",
      "org": "Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv)",
      "title": "POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding",
      "published": "2025-04",
      "url": "https://arxiv.org/abs/2407.14931",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "고전·학습·혼합 MAPF 방법 비교 벤치마크(arXiv v3, v1 2024-07-20). 이번에는 §4.2 분포 밖 평가용 Cities-tiles 지도와 §5 통신 미분리 한계를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2407.14931v3",
      "source_unopened": false
    },
    {
      "id": "ref-1637",
      "org": "League of Robot Runners 조직위원회 (MAPF-Competition/web_resource, GitHub)",
      "title": "League of Robot Runners 2026 — Evaluation Process(evaluation.md)·Updates(updates.md)·Competition Rules(rules.md)",
      "published": null,
      "url": "https://github.com/MAPF-Competition/web_resource/tree/9d5e3378979561a55645cb737ca5e71bc91f020b",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "LoRR 2026 공식 웹 자료 저장소(고정 커밋 9d5e337, 커밋 날짜 미확인). 평가 구성(7개 지도 12개 인스턴스, 50~10,000 에이전트, GPU·CPU 인스턴스)과 2026-09-02 최종 결과·2026-08-10 지연·2026-05-26 AAMAS Prize 공지를 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MAPF-Competition/web_resource/9d5e3378979561a55645cb737ca5e71bc91f020b/updates.md",
      "source_unopened": false
    },
    {
      "id": "ref-199",
      "org": "Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv)",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10-28",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "SILLM 논문(arXiv v2 2025-05-18, v1 2024-10-28). Table III 지도별 처리량·계획 시간과 부록 E(훈련 자원·12시간 미만)·F.1(WPPL 비교 조건)을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2410.21415v2",
      "source_unopened": false
    },
    {
      "id": "ref-1638",
      "org": "He Jiang (DiligentPanda, GitHub) — SILLM 저자 공식 저장소",
      "title": "Deploying Ten Thousand Robots: Scalable Imitaion Learning for Lifelong Multi-Agent Path Finding — README·예시 설정(Scalable-Imitation-Learning-for-LMAPF)",
      "published": null,
      "url": "https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "SILLM 프로젝트 페이지가 링크한 공식 코드 저장소. README 는 Backward Dijkstra·정적·동적 안내 버전을 별도 브랜치로 관리한다고 설명하고, 1-GPU 예시 YAML 은 max_dagger_iterations 100 을 둔다. 코드 실행은 하지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF/static_guidance/README.md",
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
      "accessed": "2026-10-12",
      "summary": "LSMART 프리프린트. §4.1 대체 정책 호출 비율 지표와 §4.4 LRGW·PIBT 대체 정책 비교 결과를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2602.15721v1",
      "source_unopened": false
    },
    {
      "id": "ref-1639",
      "org": "Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85)",
      "title": "Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation",
      "published": "2026-03-24",
      "url": "https://doi.org/10.1613/jair.1.20611",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "RL-RH-PP 를 제안한 JAIR 게재 논문(2026-03-24, arXiv 2603.23838 2026-03-25). 16개 보류 환경·800단계·단계당 CPU 1초 조건의 Amazon·Symbotic 모사 지도 비교(Table 3)와 밀도별 훈련 비용을 담는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2603.23838v1",
      "source_unopened": false
    },
    {
      "id": "ref-1640",
      "org": "Sanjay, V., & Li, J. (arXiv)",
      "title": "Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF",
      "published": "2026-08-07",
      "url": "https://arxiv.org/abs/2608.06702",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "학습 없는 지속형 MAPF 알고리즘 PUSH 를 제안한 프리프린트. 1,000단계·단계당 1초·5회 평균 조건과 알고리즘별 시간 초과 처리(RHCR 의 PIBT 대체)를 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.06702v1",
      "source_unopened": false
    },
    {
      "id": "ref-1641",
      "org": "Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv)",
      "title": "Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations",
      "published": "2026-08-06",
      "url": "https://arxiv.org/abs/2608.05588",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "회전을 포함한 지속형 MAPF 에 탐색 보조 공동 강화학습(SJRL)을 제안한 프리프린트. 지도별 학습·32~320대 평가와 실물 8대+가상 248대 혼합 현실 검증을 보고한다. SILLM 과 공동 저자.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.05588v1",
      "source_unopened": false
    },
    {
      "id": "ref-1053",
      "org": "Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv)",
      "title": "DeepFleet: Multi-Agent Foundation Models for Mobile Robots",
      "published": "2025-08",
      "url": "https://arxiv.org/abs/2508.08574",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Amazon Robotics 의 다중 로봇 기반 모델 보고서(arXiv v3 2026-04-13). arXiv 메타데이터상 'Unpublished technical report, Amazon Robotics' 로 동료 심사 없는 회사 자체 보고서다. 7개 층·7일 보류 자료의 60초 궤적 예측 평가와 Table 2 CDE 를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2508.08574v3",
      "source_unopened": false
    },
    {
      "id": "ref-916",
      "org": "Amazon",
      "title": "Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot",
      "published": "2025-07-01",
      "url": "https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Amazon 공식 발표(Scott Dresser, 페이지 메타 article:published_time 2025-07-01). DeepFleet 10% 를 요약은 '이동 효율을 높일 것', 본문은 '이동 시간 10% 개선/감소'로 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1054",
      "org": "Amazon Science",
      "title": "Amazon builds first foundation model for multirobot coordination",
      "published": "2025-08-11",
      "url": "https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Amazon Science 블로그. DeepFleet 이 작업 배정과 혼잡 회피 경로에 쓰여 '로봇 배치 효율을 10% 높이고 있다'고 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1062",
      "org": "Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv)",
      "title": "Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts",
      "published": "2026-08-21",
      "url": "https://arxiv.org/abs/2608.21554",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "병원 이기종 로봇 배정의 예측 인지형 모델 기반 강화학습 프리프린트. 본문에서 BIDMC 4개 층 168 층-일 평가, 확정 요청 가중치 1, Table 3 거절 건수, 대기 시간 개선 수치를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.21554v1",
      "source_unopened": false
    },
    {
      "id": "ref-1057",
      "org": "Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors)",
      "title": "AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots",
      "published": "2021-12-21",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "청소 로봇 IMU 진동 5종 분류 기반 예지 정비 프레임워크(Sensors 22(1):13). Europe PMC 전문으로 실시간 시험 표본 100개(Table 5)와 요청 방식 수집을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8747287/fullTextXML",
      "source_unopened": false
    },
    {
      "id": "ref-1060",
      "org": "ISO (ISO/TC 108/SC 5)",
      "title": "ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements",
      "published": "2025-09-02",
      "url": "https://www.iso.org/standard/88029.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "기계 상태 감시·진단의 예지 일반 지침 제3판. 공식 목록·공개 메타데이터로 발행 2025-09-02·23쪽·SC 5 소관을 확인했고 규범 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1642",
      "org": "Open-RMF 유지관리자 (open-rmf, GitHub)",
      "title": "rmf_battery — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Open-RMF 배터리 추정 라이브러리 README. 이동 궤적의 가감속 에너지(SimpleMotionPowerSink)와 장치 소비 전력(SimpleDevicePowerSink)으로 SoC 변화를 추정하는 API 를 설명한다(물리 모델, 학습 아님).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_battery/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md",
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
      "accessed": "2026-10-12",
      "summary": "Open-RMF 작업 요청 JSON 스키마. fleet_name 이 문자열 또는 문자열 배열을 받고 지정한 플릿만 입찰한다(0.7.0, CHANGELOG 2026-09-18 — 독립 검증 기준).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
      "source_unopened": false
    },
    {
      "id": "ref-1063",
      "org": "CJ대한통운",
      "title": "'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명",
      "published": "2021-07-28",
      "url": "https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "CJ대한통운 뉴스룸 게시물. 이플렉스가 주문 유형별 수요를 예측해 센터 인력 운영에 쓴다고 설명한다(기존 위키 5·9절에 이미 있음, 이번에는 책임 경계 의견의 참고로만 씀).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1643",
      "org": "강민교, 김인철 (한국로봇학회 논문지 18(2))",
      "title": "다중 로봇 제조 물류 작업을 위한 안전성과 효율성 학습 (Safety and Efficiency Learning for Multi-Robot Manufacturing Logistics Tasks)",
      "published": "2023-06",
      "url": "https://doi.org/10.7746/jkros.2023.18.2.225",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "심층 관계형 강화학습으로 제조 물류 작업의 안전성·효율성 등급을 예측해 로봇에 배정하는 국내 연구(pp.225–232). Isaac 시뮬레이터 안 이동 로봇 2대로 실험했고 실물 검증은 향후 과제다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://jkros.org/xml/36684/36684.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1644",
      "org": "현대자동차그룹 (현대글로비스)",
      "title": "현대글로비스가 그리는 자동화를 넘어선 물류의 미래",
      "published": "2026-04-16",
      "url": "https://www.hyundaimotorgroup.com/ko/story/hyundai-glovis-physical-ai-logistics",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "현대자동차그룹 Story 기업 게시물. AW 2026 전시와 현대글로비스·알티올의 WCS 플랫폼 오르카(설비 상태·우선순위에 따른 동선·작업 순서 실시간 조정, 어댑터 인터페이스)를 소개한다. 학습 모델·성과 분모는 밝히지 않는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1061",
      "org": "Elmachtoub, A. N., & Grigas, P. (arXiv; Management Science 68(1))",
      "title": "Smart \"Predict, then Optimize\"",
      "published": "2017-10",
      "url": "https://arxiv.org/abs/1710.08005",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "결정 손실(SPO)·SPO+ 로 예측을 학습하는 틀. Crossref 서지로 학술지 게재본(Management Science 68(1):9–26, 2022-01, DOI 10.1287/mnsc.2020.3922)을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.crossref.org/works?query.bibliographic=Smart+Predict+then+Optimize+Elmachtoub+Grigas",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "sections": [
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등, 정정 요청 없음): 섹션 4(분리 2026-09-30-area46-s4) — '예지와 예지 정비' 항목의 ISO 13381-1 서지를 2025-09-02 발행·제3판·ISO/TC 108/SC 5·23쪽으로 보강(f33, ref-1060 서지 보정). '충전 상태' 항목에 물리 모델 SoC 추정(rmf_battery, f34)과 학습 예측을 구분하는 경계 설명(f35)만 덧붙임(rmf_battery 는 28 맥락이며 학습 근거로 쓰지 않음) / 섹션 5 — 물류창고 사례: 74행 예외·성과 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 을 f25 로 정정(발표 2025-07-01 요약은 미래형 'will improve', 본문 '이동 시간 10%', 블로그 2025-08-11 '배치 효율 10%', 비교 기간·분모 미공개, [추정] 벤더 주장 유지). DeepFleet 오프라인 예측 평가 조건(7개 층·7일·60초, f23)과 CDE 3.40%(f24)는 Amazon 자체 기술보고서라 [추정] 벤더 주장으로; 의견 f26. 기존 ref-1053 근거 [사실] 문장(모델 구성 서술)은 보고서 자체 내용 서술이라 유지하되 성능 수치는 [추정]으로 다룬다(기준 엇갈림 표시). 병원 사례: 표·본문에 평가 조건(BIDMC 4개 층·168 층-일·12시간, f27), 확정 요청 가중치 1(f28, 제약 칸), 거절 0건 동률(f29), 대기 시간 수치(f30, 예외·성과 칸 '꼬리 지연 개선이 가장 컸다' 를 수치로 보강). 제조 공장: 국내 연구 강민교·김인철(f38·f39)을 시뮬레이션 연구로만 추가(실제 배치 사례 아님). 오르카(f40)는 학습 요소가 확인되지 않은 통합 제어 발표라 사례가 아니라 경계 설명 한 문장으로(f41). 기타: 91% 가 시험 표본 100개 기준임(f32) / 섹션 6(분리 2026-09-30-area46-s6) — '학습 기반 경로·교통 관리' 에 RL-RH-PP(f12~f14)와 SJRL(f20~f22, SILLM 공동 저자라 독립 재현 아님) 추가, 실패·복귀 처리 소절에 LSMART 대체 정책 호출 비율(f15)·LRGW/PIBT 지도별 최고(f16), 고전 대조군 PUSH 의 예산·폴백 조건(f17·f18)은 대조 설명으로만(f19); 의견 f31·f44. 첫 문장 '같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고' 는 f6·f13 처럼 지도·밀도별로 우열이 갈린다는 점으로 보강 / 섹션 7(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 평가 Cities-tiles(f1)·통신 미분리 한계(f2). League of Robot Runners 행: 기존 SILLM 2023 비교에 LoRR 2026 평가 구성(f3)과 최종 결과(f4)를 요약·연결만 추가(주 위치는 27·54·25 영역, 다음 실행 후보); 의견 f5. '기존 위키는 SILLM 비교만 소개' 류 서술은 쓰지 않음(기존 자료: ref-603 testing-formal-verification-and-benchmarking.md 115행, ref-191, ref-1306, standards/index.md 140·182행). SILLM 공식 구현 행 추가(f9·f10, 출처는 공식 DiligentPanda 저장소 ref-1638 — 메모의 wuwen-T 미러는 쓰지 않음). ISO 13381-1 행 서지 보정(f33) / 섹션 8(분리 2026-09-30-area46-s8) — SILLM 항목(대상 문장 '…최고 탐색 기반 기준선보다 16.0% 높았고…')은 삭제하지 않고 지도별 예외를 덧붙임: 대형 지도 6종 중 3종(Sortation·Warehouse·Random-1)에서 WPPL 이 높음과 단계당 0.349초 대 4.143초(f6), 16.0% 는 지도별 비율 평균으로 읽힌다는 해석은 [추정](f7), 지도별 훈련 12시간 미만·자원(f8); 의견 f11. Garces 외 항목의 '구체 수치는 초록에 없다' 를 본문 수치로 정정(f27~f30). SPO 항목 '학술지 게재 연도 미확인' → Management Science 68(1):9–26, 2022-01(f42). RL-RH-PP(f12~f14)·SJRL(f20~f22) 새 항목, PUSH(f17·f18)는 고전 대조 자료로 표시. Pookkuttath 항목 91% 표본 수(f32) / 섹션 9 — 상위 업무 시스템 행에 확정 요청 인계 경계(f36 fleet_name 문자열·배열, f37 의견), 로봇 자체 지능·제어 행에 SoC 물리 모델 추정은 28·제조사 쪽(f34·f35), 오르카 같은 WCS 통합 제어는 20·61 쪽 경계(f41). 158행 '경계는 아직 정하지 않았으며' 는 f37 의견으로 부분 보강하되 열린 질문 유지 / 섹션 11(분리 2026-09-30-area46-s11) — 해결 제안 없음. 부분 근거: oq-220(f43: 제3자 실측 없음, 근거 종류 구분), oq-221(f32·f33·f34·f35: 출력 종류만 확인, 공통 데이터 계약·모델 소유권 미확인), oq-222(f15·f16·f18·f28·f31: 가중치 조정과 대체 정책 호출은 확인, 공통 분포 이동 임계값 없음), oq-223(f36·f37: 의견 수준 경계), oq-224(f38·f39 국내 시뮬레이션 연구, f40 은 학습 성과 아님). 관련 근거: oq-058(f6·f13·f21, 벤치마크→실처리량 전이는 여전히 미확인). 분리 페이지 s11 의 질문 5개에 oq-220~oq-224 id 를 붙여 표기. 새 질문 3건 / 기존 내용 확인(새 finding 으로 넣지 않음): SILLM WPPL 비교의 회전 제거·LNS 40,000회 제한(메모 F09, 2026-10-10-area27-s8.md 42행), SILLM 실물 10대·가상 100대(s8 기존), LSMART 600초×10회·실패 정책 개념(2026-10-10-area27-s8.md 43행), CJ대한통운 iFlex 주문 유형별 수요 예측(메모 V05, 본문 5절 78행·9절 149행, ref-1063), DeepFleet 네 구조(s6·s8, ref-1053), Poskart 외 조정 결정계수 0.9629·0.9694·±0.1% 이내 약 50%·MiR100(s6·s8, ref-1058, 독립 검증 재확인), 현대차 5일·90%(5절, ref-1059 파이낸셜뉴스 — 1차 자료 미확인이라 [추정] 벤더 주장 유지), fleet_name 필드 자체(2026-09-29-area09-s7.md 40행) / 후속 정리 필요(대상 페이지 밖, 이번에 고치지 않음): docs/categories/ai-and-learning/index.md 107행 '로봇 이동 효율을 10% 높였다고 주장한다' 를 f25 로, 같은 행 Garces 요약에 f30 수치; docs/categories/site-type-applications/warehouse.md 107행 'Amazon 은 2025년 7월 발표(페이지에 발행일 표기 없음, 검색 결과 기준)' → 페이지 메타 2025-07-01 확인(ref-916); 다음 실행 후보: 27. 다중 로봇 경로·교통 관리 — MAPF·54. 시험·형식 검증·벤치마크·25. 작업 배정 — MRTA(f3·f4 LoRR 2026, f12~f22), 63. 병원·의료(f27~f30), 28. 공용 자원·충전·에너지 최적화(f34)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "학습 기반 배정·경로 정책과 고전 탐색 방법을 같은 실행 모델·지도·계획 예산·실패 처리(대체 정책) 조건으로 다시 돌려 학습의 순이득을 재현한 공개 자료가 있는가? (관련 기존 질문: oq-220, oq-058) | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f44 | 종류: 일반",
    "예측 요청의 가중치를 낮추는 것으로 충분한 경우와 실행 중인 계획을 중단·교체하거나 고전 정책으로 돌아가야 하는 경우를 누가 어떤 지표로 구분하는가? (관련 기존 질문: oq-222) | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f31 | 종류: 일반",
    "배터리 SoC 변화 추정·현재 이상 클래스·고장 예지 출력을 플릿 일정에 넘길 때 값의 유효기간·불확실성·책임 주체를 어떻게 표현하는가? (관련 기존 질문: oq-221) | 관련 영역: 46. 예측·학습 기반 최적화, 28. 공용 자원·충전·에너지 최적화 | 근거: f35 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 20,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-06/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f7: SILLM 초록 16.0% 의 계산 방식은 논문에 명시되지 않아 Table III 지도별 비율 평균(재계산 16.05%)과 일치한다는 해석만 [추정]으로 둠",
      "f3·f4: LoRR web_resource 고정 커밋(9d5e337)의 커밋 날짜와 최종 수상팀 제출 코드의 학습 사용 여부는 확인하지 못함(published null)",
      "f9·f10: SILLM 공식 저장소 README·예시 YAML 만 읽었고 코드를 실행해 논문 결과를 재현하지 않음. dynamic_guidance 브랜치 내용은 보지 않음",
      "f23·f24·f25: DeepFleet 은 Amazon 자체 기술보고서·회사 발표만 근거라 [추정] 벤더 주장. 10% 의 비교 기간·대상 층·분모·개입 대조와 제3자 확인은 없음",
      "f36: fleet_name 배열 허용의 도입 버전(rmf_api_msgs 0.7.0, CHANGELOG 2026-09-18)은 독립 검증 결과를 따랐고 이번 변환에서 CHANGELOG 를 다시 열지 않음. 스키마 본문(main)은 확인",
      "f42: SPO 학술지 서지는 Crossref 메타데이터로 확인했고 학술지 본문은 열지 않음",
      "f33: ISO 13381-1:2025 규범 본문(유료)은 열지 않아 조항 내용과 위키 시사점의 직접 대응은 미확인",
      "f40: 오르카에서 실제 학습되는 모델·정책과 그 성능 비교·운영 분모는 미공개. 현대차 예지정비 5일·90%(ref-1059)의 1차 자료도 확인하지 못함",
      "oq-220~oq-224 는 모두 부분 근거만 얻어 해결 제안하지 않음. 국내 실물 창고·병원에서 학습 기반 배정·경로를 고전 방법과 대조 실측한 자료, 이종 플릿 고장 데이터 계약·모델 소유권 합의, 공통 분포 이동 복귀 임계값은 찾지 못함"
    ],
    "scope_violations": [
      "f3·f4·f5: LoRR 2026 대회 평가 구성·결과는 27. 다중 로봇 경로·교통 관리 — MAPF, 54. 시험·형식 검증·벤치마크, 25. 작업 배정 — MRTA 가 주 위치이므로 이 영역에는 요약·연결만 둠",
      "f17·f18·f19(PUSH), f34(rmf_battery), f40·f41(오르카): 학습과 무관한 고전 알고리즘·물리 모델·통합 제어이므로 이 영역에서는 대조·경계 설명으로만 쓰고 학습 성과 근거로 쓰지 않음(각각 27, 28, 20·61 영역 맥락)",
      "f36·f37: 작업 요청 스키마와 상위 수요예측 경계는 23. 업무 시스템 연동과 겹치며, 이 영역에는 예측 요청과 확정 요청의 인계 경계로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 8
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 8건/15(ref-1637~ref-1644, 예약 구간 ref-1637~ref-1666 안), 재사용 12건(ref-1056·ref-199·ref-604·ref-1053·ref-916·ref-1054·ref-1062·ref-1057·ref-1060·ref-125·ref-1063·ref-1061). 출처 매핑(독립 검증 결과 기준): 메모 n1→ref-1056, n2+n3→ref-1637(한 출처로 묶음, raw 경로), n4→ref-199, n5→ref-1638(메모의 wuwen-T 저장소는 미러라 공식 DiligentPanda/Scalable-Imitation-Learning-for-LMAPF 로 교체), n6→ref-604, n7→ref-1639(JAIR DOI 10.1613/jair.1.20611, 2026-03-24), n8→ref-1640, n9→ref-1641, n10→ref-1053, n11→ref-916(발행 2025-07-01), n12→ref-1062, n13→ref-1060(서지 보정), n14→ref-1057(Europe PMC 전문), n15→ref-1642, n16→ref-1063, n17→ref-1643, n18→ref-1644(벤더 문서), n19→ref-125. 추가 재사용: ref-1054(10% 표현 대조), ref-1061(SPO 게재 서지, Crossref). 검증 반영: F08 을 Warehouse 한 지도에서 6개 지도 중 3개(Sortation·Warehouse·Random-1) WPPL 우세로 확장하고 계획 시간 병기(f6), 16.0% 해석은 [추정](f7); F09(LNS 40,000회)는 2026-10-10-area27-s8 중복이라 제외; V01 은 JAIR 표 값이라 [사실]로 두고 N100·N120 의 RL-RH-PP 우세를 병기(f13); V02·V03 은 Amazon 자체 기술보고서라 [추정]·벤더 주장(f23·f24); V04 는 '높였다'가 아니라 미래형·지표 차이로 정정(f25); A11 Garces 를 본문 정량 결과로 정정(f27~f30); V05 는 기존 내용과 완전 중복이라 제외(ref-1063 은 의견 f37 참고로만); PUSH·rmf_battery·오르카는 학습과 무관해 대조·경계 설명으로만(f19·f35·f41); U16 SPO 게재 서지 확인(f42); U09 Poskart 수치는 재확인만 하고 새 finding 없음; U15 현대차 5일·90% 는 [추정] 유지. LoRR 2026(F03~F07)은 f3~f5 로 요약해 연결만. 교차 확인 0건: 모든 [사실] finding 이 단일 출처이거나 같은 연구팀·같은 회사 자료(SILLM 논문·저장소, SILLM·SJRL·LSMART 공동 저자, Amazon 발표·블로그·보고서)라 독립이 아님 — 신뢰도 medium 이하. 열린 질문: oq-220~oq-224 는 docs/open-questions.md 242~246행 문구와 분리 페이지 s11 질문이 같음을 확인. 해결 제안 없음, 부분 근거만. 메모의 새 질문 3건은 oq-220·oq-058, oq-222, oq-221 과 겹치는 부분이 있으나 같은 질문은 아니어서(재현 조건, 판단 주체, 유효기간·책임) 관련 기존 질문을 밝혀 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호와 고정 위키 커밋 행 번호는 쓰지 않고 원문 절·표와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음. finding 44건(사실 29, 추정 6, 의견 9)."
  }
}
```

### docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md

```markdown
---
title: "46. 예측·학습 기반 최적화"
type: area
category: "L. AI·학습 기술"
area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [결정 중심 학습, 예지 정비, 모방 학습, 지속형 MAPF, 학습 기반 배정]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1053, ref-1054, ref-1055, ref-199, ref-1056, ref-623, ref-1057, ref-1058, ref-1059, ref-1060, ref-1061, ref-1062, ref-1063, ref-1064]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 46. 예측·학습 기반 최적화

# 46. 예측·학습 기반 최적화

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

학습 기반 배정·경로, 수요·고장 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **학습 기반 배정·경로**: 강화학습 같은 학습 방법으로 배정과 경로를 정한다
- **수요·고장 예측**: 일의 양과 고장을 예측해 계획과 정비에 쓴다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]

## 3. 왜 중요한가

예측·학습 기반 최적화는 플릿의 혼잡, 시간에 따라 바뀌는 작업 요청, 배터리 소모와 고장처럼 계획을 어긋나게 하는 요인을 미리 알아 배정·경로·정비 결정에 반영하려는 영역이다. [추정][^ref-1053][^ref-1062][^ref-1058]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 왜 중요한가](../../topics/2026/2026-09-30-area46-s3.md)에 있다.

## 4. 핵심 개념과 용어

아래는 이 페이지에서 쓰는 주요 용어다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area46-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 적용 사례는 물류창고·병원·제조 공장·기타(대학 캠퍼스) 네 현장 유형에서 확인했다.

**현장 유형:** 물류창고

**사례:** 물류창고(풀필먼트·분류 센터)에서 로봇 플릿의 혼잡을 예측해 작업 배정과 경로를 조정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(확인한 자료가 작업 발생 조건을 다루지 않는다) |
| 작업 대상 | 로봇의 위치·목표·상호작용 이동 데이터(정보) [사실][^ref-1053] |
| 수행 자원 | 풀필먼트·분류 센터의 이동 로봇 플릿과, 미래 교통 패턴·위치를 예측하는 DeepFleet 모델 [추정] 벤더 주장[^ref-1054] |
| 제약 | 혼잡·병목 구간. 예측한 혼잡을 피하도록 배정과 경로를 조정한다 [추정] 벤더 주장[^ref-1054] |
| 완료·인계 | 미확인 |
| 예외·성과 | 아마존은 로봇 이동 효율을 10% 높였다고 주장하며, 독립 측정은 확인하지 못했다 [추정] 벤더 주장[^ref-1054] |

아마존 연구진의 DeepFleet은 전 세계 아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 다중 로봇 기반 모델 모음이다(2025-08 공개, 2026-04 개정). [사실][^ref-1053] 아마존은 이 모델을 현재 혼잡 예측으로 작업 배정과 경로를 조정하는 데 쓰고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 한다고 밝혔다(2025-08-11). [추정] 벤더 주장[^ref-1054] 이 사례에서 이 영역이 관여하는 곳은 혼잡이라는 제약을 미리 알아 배정·경로에 넣는 부분이다. [추정][^ref-1054]

같은 현장 유형의 다른 예로, 연계 대상: CJ대한통운은 2021-07-28 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다. [추정] 벤더 주장[^ref-1063] 이는 상위 업무 시스템 쪽의 수요 예측이며, 로봇 배정에 쓴 근거는 이 자료에 없다. [추정][^ref-1063]

**현장 유형:** 병원

**사례:** 병원 입원 병동의 간호 업무 요청을 이기종 로봇에 배정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 병동에서 간호 업무 요청이 들어오면 작업이 발생한다 [사실][^ref-1062] |
| 작업 대상 | 간호 업무 요청에 딸린 작업. 운반 품목 같은 구체 대상은 초록에 없어 미확인이다 [사실][^ref-1062] |
| 수행 자원 | 이기종 다중 로봇. 배치 전에 과거 요청 데이터로 로봇 구성(차량 소요대수)을 고른다 [사실][^ref-1062] |
| 제약 | 즉시 확정은 이미 들어온 요청에만 하고, 표본 추출한 미래 요청 시나리오는 평가에만 쓴다 [사실][^ref-1062] |
| 완료·인계 | 미확인 |
| 예외·성과 | 요청 분포가 바뀌면 최근 예측 오차로 예측 요청을 다시 가중하고 아직 시작하지 않은 배정만 다시 최적화한다. 저자는 기준선보다 대기 시간을 줄였고 꼬리 지연 지표에서 개선이 가장 컸다고 보고했다 [사실][^ref-1062] |

Garces 외(2026-08, 동료 심사 전 프리프린트)는 병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 모델 기반 강화학습 롤아웃을 평가했다. [사실][^ref-1062] 이 사례에서 이 영역은 시작 조건(요청)을 예측해 수행 자원 구성과 배정에 넣고, 분포 이동이 생기면 재최적화 범위를 좁히는 부분에 관여한다. [추정][^ref-1062]

**현장 유형:** 제조 공장

**사례:** 제조 공장에서 산업용 로봇팔 고장을 미리 예측해 정비를 계획

| 항목 | 내용 |
|---|---|
| 시작 조건 | AI 고장예측 시스템이 로봇팔의 모터 부하·진동·전류 신호에서 이상을 감지한다 [추정] 벤더 주장[^ref-1059] |
| 작업 대상 | 생산 현장의 산업용 로봇팔(설비) [추정] 벤더 주장[^ref-1059] |
| 수행 자원 | 신호를 학습한 AI 고장예측 시스템. 정비는 사후 대응에서 계획적 예측 정비로 바꾸려 한다 [추정] 벤더 주장[^ref-1059] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 회사는 고장 약 5일 전에 90% 이상 정확도로 이상을 감지한다고 밝혔고, 정확도 산정 방법·데이터 규모는 기사에 없다 [추정] 벤더 주장[^ref-1059] |

파이낸셜뉴스(2026-05-28)가 전한 현대자동차 발표에 따르면 현대차는 이 시스템을 국내 생산 현장에 먼저 적용한 뒤 해외 생산거점으로 넓히려 한다. [추정] 벤더 주장[^ref-1059] 로봇팔의 부품 수준 신호 감시는 연계 대상이며, 이 영역이 관여하는 부분은 예측 결과를 정비 일정과 작업 배정에 넣는 쪽이다. [추정][^ref-1059]

**현장 유형:** 기타

**사례:** 대학 캠퍼스(로비·푸드코트·복도)에서 청소 로봇의 이상 진동을 분류해 예지 정비 지도를 만듦

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관성 측정 장치(Inertial Measurement Unit, IMU) 진동 신호가 충돌·조립 풀림·구조 불균형 같은 이상 클래스로 분류된다 [사실][^ref-1057] |
| 작업 대상 | 증기 걸레 청소 로봇과 청소 구역(로비·푸드코트·복도) [사실][^ref-1057] |
| 수행 자원 | 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망과 정비 팀 [사실][^ref-1057] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 정비 팀이 분류 결과를 동시적 위치 추정·지도 작성(Simultaneous Localization and Mapping, SLAM) 지도에 겹친 예지 정비 지도로 위험 구역을 격리하고 심각도를 판단한다. 저자는 실시간 현장 시험 정확도 91%를 보고했다 [사실][^ref-1057] |

Pookkuttath 외(Sensors, 2021-12-21)는 싱가포르 기술디자인대학(SUTD) 캠퍼스에서 이 방법을 현장 시험했다. [사실][^ref-1057] 이 사례에서 이 영역은 고장 징후를 공간 정보와 묶어 정비 판단에 넘기는 부분에 관여한다. [추정][^ref-1057]

상업 시설·가정·실외 현장의 학습·예측 적용 사례는 이번 조사에서 찾지 못했다. 현장 유형별 전체 현황은 [현장 유형 매트릭스](../../site-matrix.md)에 있다.

## 6. 대표 접근법과 기술

같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1056][^ref-199][^ref-1064]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area46-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 이 영역과 직접 관련된 것으로 확인한 표준·평가 프로그램은 아래 세 가지다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area46-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 수치는 모두 논문 저자가 보고한 단일 출처 값이며, 이번 조사에서 두 출처 이상으로 교차 확인한 수치는 없다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-30-area46-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 작업 요청 이력을 모아 예측에 공급하고, 예측한 요청·혼잡을 배정과 로봇 구성에 반영한다 [추정][^ref-1062][^ref-1053] | 전사 주문 수요예측과 그에 따른 인력 배치(예: 이커머스 플랫폼의 주문 유형별 물량 예측) [추정] 벤더 주장[^ref-1063] |
| 로봇 자체 지능·제어 | 배터리 소모·고장 위험 예측 결과를 받아 배정·충전·정비 일정에 반영한다 [추정][^ref-1058][^ref-1057] | 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시 [추정][^ref-1057][^ref-1059] |

ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델 공급, 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스, 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시, 학습 정책의 즉시 확정 범위 제한으로 보인다. [추정][^ref-1053][^ref-1054][^ref-1062][^ref-1058][^ref-1056]

연계 대상: 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다. [추정][^ref-1057][^ref-1059][^ref-1063]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역의 수요 예측(작업 요청·물동량 예측)과 외부 연계로 둔 전사 수요예측의 경계는 아직 정하지 않았으며 11절 열린 질문에 올렸다. 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1056][^ref-1057]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area46-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 다음 질문을 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](../../topics/2026/2026-09-30-area46-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md) — 영역 심화: 섹션 3~11 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 프런트매터 related_areas·tags·sources·confidence 추가(2차 재실행: 이 페이지 본문 변경 없음) (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area46-s6.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "6. 대표 접근법과 기술" 절(1,868자)을 옮겼다. 2차: DeepFleet·34. 시뮬레이션·예측용 디지털 트윈 구분 문장의 태그를 [의견]에서 [추정]으로 되돌렸다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-30-area46-s8.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "8. 대표 연구와 자료" 절(1,712자)을 옮겼다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area46-s4.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "4. 핵심 개념과 용어" 절(1,029자)을 옮겼다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area46-s10.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(942자)을 옮겼다 (실행 2026-09-30-09)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1053]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1054]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1058]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1059]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-09-30
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1063]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-09-30
[^ref-1064]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (요약)

```markdown
# 44. 로봇 기반 모델·언어 모델 계획

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
```

### docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md (요약)

```markdown
# 45. 문서·도면·장면 이해

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **문서·도면 해석 AI**: 매뉴얼과 도면을 해석하는 모델을 다룬다
- **플랫폼 수준 장면 인식**: 고정 카메라와 여러 로봇의 인식 결과를 모아 공간 상태를 인식한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-12 · 버전: 3

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

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

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

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md (요약)

```markdown
# 35. 처리능력·규모·배치 설계

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]
```

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/other-sites.md (요약)

```markdown
# 67. 기타 현장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 14건 / 전체 1523건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | https://arxiv.org/abs/2410.21415 | 2026-09-25 | 아니오 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | https://arxiv.org/abs/2209.05738 | 2026-09-25 | 아니오 |
| ref-1053 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 2025-08 | https://arxiv.org/abs/2508.08574 | 2026-09-30 | 예 |
| ref-1054 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 2025-08-11 | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination | 2026-09-30 | 예 |
| ref-1055 | Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv) | MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale | 2024-08 | https://arxiv.org/abs/2409.00134 | 2026-09-30 | 예 |
| ref-1056 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 2025-04 | https://arxiv.org/abs/2407.14931 | 2026-09-30 | 예 |
| ref-1057 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 2021-12-21 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ | 2026-09-30 | 예 |
| ref-1058 | Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors) | Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems | 2022-12-15 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/ | 2026-09-30 | 예 |
| ref-1059 | 파이낸셜뉴스 | 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지 | 2026-05-28 | https://www.fnnews.com/news/202605280925297568 | 2026-09-30 | 예 |
| ref-1060 | ISO (ISO/TC 108) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements | 2025 | https://www.iso.org/standard/88029.html | 2026-09-30 | 아니오 |
| ref-1061 | Elmachtoub, A. N., & Grigas, P. (arXiv) | Smart "Predict, then Optimize" | 2017-10 | https://arxiv.org/abs/1710.08005 | 2026-09-30 | 예 |
| ref-1062 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 2026-08 | https://arxiv.org/abs/2608.21554 | 2026-09-30 | 예 |
| ref-1063 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명 | 2021-07-28 | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 | 2026-09-30 | 예 |
| ref-1064 | Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024) | Guidance Graph Optimization for Lifelong Multi-Agent Path Finding | 2024-02 | https://arxiv.org/abs/2402.01446 | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [46] 에 걸린 6건 / 전체 409건)

```markdown
- oq-220 [열림] 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? (영역 46, 54)
- oq-221 [열림] 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? (영역 46, 38)
- oq-222 [열림] 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? (영역 46, 47)
- oq-223 [열림] 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? (영역 46, 23)
- oq-224 [열림] 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? (영역 46, 61)
- oq-323 [열림] 지속성 필터처럼 마지막 관측 뒤 시간에 따라 믿음을 낮추는 확률 모델을 문·승강기·충전기 같은 설비 상태의 허용 경과 시간 판단에 적용한 연구나 사례가 있는가? (영역 18, 46)
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

### runs/2026-10-12-05/research.md

```markdown
# 리서치 브리프 2026-10-12-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-05 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 44. 로봇 기반 모델·언어 모델 계획 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 제조 공장 사례가 BMW 보도자료(ref-1051) 하나에 기대며, 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'가 Figure AI 발표(2025-11-19, 2026-06-30)의 존재와 맞지 않음. 10개월·11개월 문구의 출처 위치(CEO 인용·본문)와 Figure 쪽 기간 축, 99% 성공률이 목표치라는 구분이 없음. 연구 실물 사례(IMR-LLM 로봇 팔 3대)도 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area44-s6) — SMART-LLM·IMR-LLM 은 초록 수준 서술뿐이라 평가 규모(36 지시, 23장면·50작업)·실패 양상(불가능 과제, 도달 불가 배정)·풀이 방식(FIFO)이 없고, LLM+P·KnowNo 류 보장의 입력 전제(사람이 준 도메인, i.i.d., 무오류 실행)가 적혀 있지 않음. 다중 로봇 등각 예측 계획(S-ATLAS) 없음. disjunctive graph 번역어가 위키 안에서 셋으로 갈림
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area44-s7) — 'OpenVLA의 라이선스는 확인하지 못했다'(표 바로 아래)와 GR00T N1 '오픈소스(공개 모델)' 표기에 코드·가중치 라이선스 구분과 문서 간 충돌이 없음. VLA 배포물의 입출력 계약(정규화·행동 청크·개방 루프)과 GR00T N1.7 EA 상태, ROSA 의 물리 실행 조건이 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area44-s8) — 최근 로봇 기반 모델(π0.7)과 VLA 견고성 벤치마크(LIBERO-Plus)가 없고, 국내 동향이 2025-05 기사 하나뿐(산업부 M.AX 휴머노이드 과제 표 없음)
- 섹션 9. 책임 경계 — 도구 호출(MCP)로 로봇을 움직일 때 힌트·권한·승인·세션 종료·물리 정지의 관계가 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area44-s11) — oq-216~oq-219 모두 열림. 부분 근거(배포물별 입출력, 연구 벤치마크 규모, Figure 기간 축)가 연결돼 있지 않음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s7 OpenVLA 라이선스 문장, 5절 93행 Figure 자체 발표 문장

## 조사 질문

1. 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
2. oq-217 언어 모델 기반 다중 로봇 계획기의 공개 평가는 어떤 규모·조건(시뮬레이션/실물, 로봇 수)이며 어떤 실패 양상(능력 밖 배정)을 보고하는가? (섹션 5·6 겨냥)
3. 기호 계획기 결합·등각 예측 기반 계획의 검증·보장은 어떤 입력 전제(도메인 제공자, 분포 가정, 스킬 실행 성공)에 기대는가? (섹션 6 겨냥)
4. oq-216 VLA 를 등록하려면 배포물마다 어떤 입출력(행동 공간·정규화·행동 청크·제어 모드)과 공개 상태(EA/GA)를 확인해야 하는가? (섹션 7·8 겨냥)
5. OpenVLA·GR00T N1.7·openpi 의 코드와 가중치 사용 조건은 각 문서에서 무엇이라 적혀 있고 서로 맞는가? (섹션 7 겨냥)
6. 언어 모델 도구 호출(MCP·ROSA)로 로봇을 움직일 때 권한·승인·세션 종료와 물리 정지는 어떻게 나뉘는가(oq-141 관련)? (섹션 7·9 겨냥)
7. oq-218·oq-219 BMW–Figure 와 국내 물류 실증 발표에서 목표·기간·첫 시연과 실측 성과는 어떻게 구분되는가? (섹션 5·8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | SMART-LLM 의 평가 데이터셋은 AI2-THOR 가정 시뮬레이션의 고수준 지시 36개로 구성되며, 과제마다 로봇 1~4대를 쓴다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | SMART-LLM 의 불가능 과제 시험(어떤 로봇도 필요한 스킬을 갖지 않은 과제)에서 GPT-4·Claude-3 기반 구성은 배정 계획을 만들지 않았고, GPT-3.5·Llama2 기반 구성은 과제에 맞지 않는 로봇이 들어간 배정 계획을 만들었다. 이 시험은 표 I 집계에 들어 있지 않고 과제 수도 보고되지 않았다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | IMR-Bench 는 생산 라인 설계 전문가가 실제 산업 현장에서 수집·각색한 장면 23개(장면당 로봇 1~7대)를 바탕으로 제조 작업 50개를 구성한 벤치마크이며, KunWu 플랫폼 위에 만들어졌다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | IMR-LLM 구현은 언어 모델이 구성을 도운 이접 그래프(disjunctive graph)의 일정을 휴리스틱 FIFO(선입선출) 알고리즘으로 푼다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | IMR-LLM 의 실물 시험은 컨베이어에 공작물을 옮기는 로봇 팔 3대의 단일 장면이었고, 전문가가 약 15분 걸려 장면 설명을 손으로 작성해 입력했다. 반복 횟수는 보고되지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | IMR-LLM 저자는 복잡한 다중 로봇 작업에서 성공률이 떨어진 주된 이유로 언어 모델의 잘못된 분해·배정(예: 팔이 닿지 않는 로봇에 작업 배정)을 들었으나, 그 빈도는 정량화하지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | LLM+P 는 행동의 전제·효과를 담은 PDDL 도메인 파일을 사람 전문가가 제공한다는 것을 입력 전제로 둔다. 언어 모델은 문제(problem) 파일만 만든다. | ref-092 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | S-ATLAS(등각 예측 기반 다중 로봇 언어 계획기)의 임무 성공률 보장은 보정(calibration) 시나리오와 시험 시나리오가 독립·동일분포(i.i.d.)라는 조건 아래에서만 성립한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | S-ATLAS 의 임무 완료율 정리(Theorem IV.2(a))는 계획 실행에 오류가 없다는 전제를 두며, 증명은 예측 집합이 단일 원소가 아닐 때 사람이 정확한 도움을 준다는 것도 전제한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | S-ATLAS 는 AI2-THOR 시뮬레이션의 검증 시나리오 110개로 평가했고 로봇 수는 1·3·10·15대였다. 열람한 본문에서 실물 로봇 실험은 확인되지 않았다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | OpenVLA 모델 카드에 따르면 OpenVLA 는 언어 지시와 카메라 영상 한 장을 입력받아 정규화된 7자유도 엔드이펙터 변위(x, y, z, roll, pitch, yaw, gripper)를 출력하며, 실제 로봇에서 실행하려면 로봇·데이터셋별로 계산한 통계로 역정규화해야 한다. | ref-1609 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | OpenVLA 공식 저장소(고정 커밋 c8f03f4)의 코드 라이선스는 MIT 다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [사실] | 같은 OpenVLA README 는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있으며, 두 모델이 Llama 2 에서 파생됐으므로 Llama Community License 가 적용될 수 있다고 적는다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [사실] | OpenVLA 의 Hugging Face 모델 카드는 "모든 OpenVLA 체크포인트와 학습 코드가 MIT 라이선스로 공개된다"고 적어, 저장소 README 의 Llama Community License 적용 가능 문구와 충돌한다. 현재 main 판(커밋 47a0ec7, 2026-02-17)도 같은 문구이며, 두 문서는 같은 개발팀 자료라 어느 쪽이 맞는지는 문서만으로 정할 수 없다. | ref-1609, ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | openpi 원격 추론 예시는 정책 서버가 (action_horizon, action_dim) 형태의 행동 청크(action chunk)를 돌려준다고 설명한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 openpi 예시는 다음 추론 호출 전까지 예측된 행동 청크의 나머지 행동을 개방 루프(open-loop)로 실행하도록 안내한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | openpi README(커밋 215abfb)가 제공하는 기반 체크포인트는 π0, π0-FAST, π0.5 뿐이며, π0.7 가중치는 목록에 없다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | NVIDIA Isaac GR00T 저장소의 n1.7-release README 는 GR00T N1.7 을 Early Access(EA) 릴리스로 명시하고, GA(정식) 릴리스 전까지 지원·안정성 보장이 제한되며 상용 지원을 포함한 운영 배치는 GA 대상이라고 적는다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [사실] | 같은 GR00T README 의 License 절은 코드는 Apache 2.0, 모델 가중치는 NVIDIA Open Model License 로 구분한다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [추정] | GR00T README 소개 문단은 "GR00T N1.7 은 Apache 2.0 으로 완전히 상용 라이선스가 가능하다"고 적지만, 이는 같은 README 의 License 절(가중치는 별도 라이선스)·가중치 저장소 LICENSE(3.3절 비상업 한정)와 맞지 않는 벤더 소개 문구다. | ref-1611, ref-1612 | 아니오 | low | 2026-10-12 | — | — |
| f21 | [사실] | Hugging Face nvidia/GR00T-N1.7-3B 저장소의 LICENSE 파일(커밋 6949d5d, 현재 main 과 같음)은 'NVIDIA License' 표제 아래 3.3절에서 저작물과 파생물을 연구·평가 목적의 비상업 용도로만 쓸 수 있게 하고, NVIDIA 와 그 계열사는 상업적으로 쓸 수 있다는 예외를 둔다. | ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | GR00T N1.7 가중치의 사용 조건은 세 문서가 서로 다르게 적는다: README 소개(Apache 2.0 으로 상용 가능), README License 절과 3B 모델 카드(NVIDIA Open Model License, 카드는 '상업·비상업 사용 준비'), 3B 저장소 LICENSE 파일(NVIDIA License 3.3절 비상업 한정). 어느 문서가 우선하는지는 문서에 적혀 있지 않다. | ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [추정] | Physical Intelligence 의 π0.7 기술 보고서는 관절(joint)·엔드이펙터(ee) 행동을 함께 학습하고 프롬프트의 텍스트 식별자 c∈{joint, ee} 로 실행 제어 모드를 지정해 실행 시 과제에 따라 고른다고 설명한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f24 | [추정] | π0.7 보고서는 추론 지연에 대비해 학습 중 0~12 타임스텝의 지연을 모사했고, 이는 50 Hz 로봇에서 최대 240 ms 에 해당한다고 적는다. 이는 학습 조건이며 측정된 추론 지연이 아니고, 보고서의 UR5e 로봇은 20 Hz 로 동작한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f25 | [추정] | π0.7 저자들은 학습 데이터가 매우 커서 평가 과제가 학습 때 본(seen) 과제인지 처음 보는(unseen) 과제인지 확정하기 어렵다고 스스로 밝힌다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f26 | [사실] | LIBERO-Plus 는 LIBERO 시뮬레이션 조작 과제에서 물체 배치, 카메라 시점, 로봇 초기 상태, 언어 지시, 조명, 배경 질감, 센서 잡음의 7개 축으로 입력을 하나씩 교란해 VLA 모델의 견고성을 평가한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | LIBERO-Plus 에서 OpenVLA-OFT 의 성공률은 교란 없는 원본 97.1% 에서 로봇 초기 상태 교란 시 크게 떨어진다. 수치는 판마다 다르다: arXiv v3 표 1 은 로봇 초기 상태 37.2%·카메라 시점 59.7%, CVPR 2026 게재본(제목 'LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models') 표 2 는 로봇 초기 상태 31.9%·카메라 시점 56.4% 다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f28 | [사실] | ROSA FAQ 는 핵심 ROSA 에이전트가 텍스트 상호작용에 한정되어 물리 세계와 상호작용할 수 없으며, 물리적 상호작용에는 사용자가 맞춤 도구와 프롬프트를 만들어야 한다고 설명한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f29 | [사실] | 같은 ROSA FAQ 는 로봇 능력을 넘는 행동을 막으려면 맞춤 도구 안에 실행 전 로봇 상태·능력 확인 제약과 매개변수 검증·행동 제한 같은 안전 검사를 직접 넣으라고 권고한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f30 | [사실] | MCP 공식 블로그(2026-03-16)는 도구 어노테이션(readOnlyHint·destructiveHint 등)이 위험을 알리는 힌트일 뿐 실행 강제 수단이 아니며, 확실한 보장이 필요하면 네트워크 통제나 샌드박스로 해야 한다고 설명한다. | ref-1617 | 아니오 | medium | 2026-10-12 | — | — |
| f31 | [추정] | PickNik 의 MoveIt Pro MCP 서버 문서는 공유되는 배포(deployment) MCP 키는 읽기 전용이고, 로봇 동작은 호스트 사용자 세션에서 기존 Objective 를 시작·취소하는 것으로만 한정된다고 설명한다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [추정] | 같은 문서는 MCP 서버가 별도의 실행 확인 프롬프트를 추가하지 않으며, 도구 승인은 MCP 클라이언트 설정에 달려 있고 클라이언트가 자동 승인할 수도 있다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [추정] | 같은 문서는 run_objective 로 시작한 로봇이 세션이 끝나도 계속 움직일 수 있고, cancel_objective 는 최선 노력(best effort)일 뿐 비상 정지가 아니며 MCP 취소·소프트웨어 정지는 물리적 비상 정지를 대체하지 않는다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [추정] | Figure AI 의 2025-11-19 발표는 BMW 스파턴버그의 Figure 02 를 '11개월 배치'라고 부르면서, 개발 착수 뒤 6개월 안에 공장에 납품·시험을 시작하고 10개월 안에 생산 라인 전면 배치를 시작했으며 '6개월의 일일 가동'과 1,250시간 이상 가동을 적는다. 세 기간의 기점·종점이 달라 BMW 보도자료의 10개월·11개월 차이를 해소하지 못한다. | ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [추정] | 같은 Figure 발표에서 '교대당 99% 초과 성공률'과 '교대당 개입 0회'는 목표(target·goal)로 제시되며, 달성한 실측치로 보고되지 않았다. | ref-1619 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [추정] | Figure AI 는 2026-06-30 발표에서 BMW 스파턴버그 공장에서 Figure 03 이 물류 작업 흐름을 수행한 것을 '첫 시연'으로 설명하고, 자사 VLA 인 Helix 02 가 손·팔·몸통·발을 함께 제어해 무거운 대차를 끌었다고 적는다. | ref-1620 | 아니오 | low | 2026-10-12 | — | — |
| f37 | [추정] | 기존 위키 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'(Figure 03 착수 문단)는 고쳐야 한다. Figure AI 자체 발표(2026-06-30, 2025-11-19)가 있으나, BMW 와 같은 프로젝트의 당사자 자료라 독립 교차 확인으로는 세지 않는다. | ref-1620, ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [사실] | 산업통상부 2025-11-24 보도자료에 따르면 산업부와 서울대가 M.AX 얼라이언스 협력 MOU 를 맺었고, 지원 과제 표의 휴머노이드 분과 과제는 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 핵심 연구진 장병탁·박재흥 서울대 교수)이다. | ref-1621 | 아니오 | medium | 2026-10-12 | — | — |
| f39 | [의견] | 스킬 목록이 없거나 로봇 능력 밖인 요청을 계획기가 거절하는지(또는 닿지 않는 로봇에 배정하지 않는지)를 일반 성공률과 별도의 수용 시험 항목으로 두어야 한다. | ref-090, ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f40 | [의견] | 언어 모델 다중 로봇 계획의 검증 결과에는 일정 풀이 통과와 분해·배정의 정확성을 따로 적고, 계획 검증이 기대는 전제(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행, 정확한 사람 도움)를 함께 기록해 전제가 깨질 때 보장 상태를 다시 평가해야 하며, 이 보장을 플릿의 물리적 안전 보장과 섞지 않아야 한다. | ref-170, ref-092, ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f41 | [의견] | 연구 논문의 실물 시험(예: 로봇 팔 3대 단일 장면)은 사례 표에 장면 작성자·시뮬레이션 확인·복구 책임을 함께 적고 장기 운영 실적으로 표시하지 않아야 한다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [의견] | VLA 탑재 로봇의 능력 등록에는 모델·가중치 revision(해시), 로봇 기종·카메라, 좌표계·행동 단위·제어 모드, 정규화 통계, 행동 청크의 형태·관측 시각·유효기간·중단 조건, 허용 과제와 완료 판정을 두고, 명령 완료는 로봇 외부 상태로 확인하는 것이 필요해 보인다. 이는 ROP 설계 제안이며 표준이 아니다. | ref-1609, ref-1610, ref-1613 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [의견] | 공개 VLA 를 도입할 때 코드 라이선스와 가중치 사용 조건을 따로 확인하고, README 소개 문구만으로 상용 허용을 확정하지 않으며, 문서끼리 충돌하는 조건은 배포자에게 서면으로 확인할 항목으로 남겨야 한다. | ref-1608, ref-1609, ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [의견] | 카메라 교체·로봇 초기 자세 변경 같은 교란을 로봇별 수용 시험에 넣고, 벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며, 단일 팔 시뮬레이션 벤치마크 순위를 제조사 혼합 플릿 순위로 환산하지 않아야 한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [의견] | 언어 모델이 도구 호출로 로봇을 움직이는 구성에서는 어노테이션 힌트나 클라이언트 자동 승인에 기대지 말고, ROP 쪽 런타임에서 읽기/실행 권한·실행 대상·승인된 계획 revision·goal id 와 물리적 완료 판정을 검사하며, 세션 종료를 별도의 정지 절차에 연결해야 한다. | ref-1617, ref-1618, ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f46 | [의견] | 벤더·도입 기업 발표는 목표·기간·첫 시연과 실측 성과를 다른 열로 나누고, 운영 기간의 기점·종점, 성공률의 분모, 개입·실패 로그, 인계 신호가 공개될 때까지 도입 KPI 비교에 쓰지 않아야 한다. 국내 실증 목표(자동화율 80%·성공률 90%)도 같다. | ref-1619, ref-1620, ref-1051, ref-1621 | 아니오 | medium | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-1051 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | 벤더 문서 | medium | 2026-10-12 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 아니오 |
| ref-1607 | Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1)) | Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction | 2025-01 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2402.15368 | 아니오 |
| ref-1608 | OpenVLA 개발팀 (openvla/openvla GitHub) | OpenVLA — README 및 LICENSE (커밋 c8f03f4) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/README.md | 아니오 |
| ref-1609 | OpenVLA 개발팀 (Hugging Face openvla/openvla-7b) | openvla/openvla-7b — Model Card | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/openvla/openvla-7b | 아니오 |
| ref-1610 | Physical Intelligence (Physical-Intelligence/openpi GitHub) | openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md | 아니오 |
| ref-1611 | NVIDIA (NVIDIA/Isaac-GR00T GitHub) | Isaac GR00T N1.7 — README 및 LICENSE (n1.7-release 브랜치) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md | 아니오 |
| ref-1612 | NVIDIA (Hugging Face nvidia/GR00T-N1.7-3B) | GR00T-N1.7-3B — LICENSE 및 모델 카드 | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/nvidia/GR00T-N1.7-3B/blob/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE | 아니오 |
| ref-1613 | Physical Intelligence (Ai, B. 외, arXiv) | π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities | 2026-04-16 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2604.15483 | 아니오 |
| ref-1614 | Fei, S., Wang, S., Shi, J. 외 (arXiv) | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | 2025-10-15 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2510.13626 | 아니오 |
| ref-1615 | Fei, S., Wang, S., Shi, J. 외 (CVPR 2026, Computer Vision Foundation Open Access) | LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models | 2026 | 논문 | high | 2026-10-12 | https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html | 아니오 |
| ref-1616 | NASA Jet Propulsion Laboratory (nasa-jpl) | FAQ · nasa-jpl/rosa Wiki | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/nasa-jpl/rosa/wiki/FAQ | 아니오 |
| ref-1617 | Model Context Protocol (Hungerford, O., Morrow, S., & Chang, L.) | Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do | 2026-03-16 | 오픈소스 문서 | medium | 2026-10-12 | https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/ | 아니오 |
| ref-1618 | PickNik Robotics | Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10) | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/ | 아니오 |
| ref-1619 | Figure AI | F.02 Contributed to the Production of 30,000 Cars at BMW | 2025-11-19 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/production-at-bmw | 아니오 |
| ref-1620 | Figure AI | F.03 Arrives at BMW | 2026-06-30 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/f-03-at-bmw | 아니오 |
| ref-1621 | 산업통상부 | 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다. | 2025-11-24 | 정부·연구기관 | medium | 2026-10-12 | https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 제조 공장: 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 'Figure AI 자체 발표(2026-06-30 F.03 첫 시연, 2025-11-19 F.02 회고)가 같은 내용을 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 정정(f37, 벤더 주장 [추정]). 89·91행 10/11개월 충돌은 기존 내용 확인(5절 89·91행, oq-219) — 새로 넣지 말고 11개월은 Figure CEO 인용·10개월은 본문이라는 위치와 Figure 쪽 세 기간 축(6·10·11개월, 6개월 일일 가동·1,250시간)만 보탬(f34). 예외·성과 칸에 99% 초과 성공률·개입 0회는 목표치(f35), Figure 03 은 첫 시연(f36). 연구 실물 사례로 IMR-LLM 로봇 팔 3대 단일 장면(전문가 15분 장면 작성, 반복 미보고, f5)을 '연구 평가'로 표시해 추가할 수 있음. 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제와 동일성 미확인이라 별도 문장으로, 80/90 실측 없음 유지; 의견 f41·f46 / 섹션 6(분리 2026-09-30-area44-s6) — 다중 로봇 계획 소절: SMART-LLM 36개 지시·1~4대·AI2-THOR(f1, C 트랙 stage-2 166행의 '원문 미열람' 수치를 원문 확인으로 보강), 불가능 과제의 모델별 차이(f2). IMR-LLM 23장면·50작업(f3), FIFO 휴리스틱(f4), 복잡 과제 성공률 하락과 도달 불가 배정(f6). 57행 '선택 그래프(disjunctive graph)'는 위키 안에서 '선언 그래프'(C 트랙 stage-1 112행)·'이접 그래프'(같은 파일 240행)와 갈리므로 한 용어로 통일 제안(이번 갱신은 s6 만, 트랙 페이지는 후속 정리). 기호 계획기 소절: LLM+P 의 사람 제공 도메인 전제(f7). 불확실도 소절: S-ATLAS 의 i.i.d.·무오류 실행·정확한 도움 전제와 110개 시뮬레이션 시나리오(f8~f10)를 KnowNo 다음에 추가; 의견 f39·f40 / 섹션 7(분리 2026-09-30-area44-s7) — 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정: 코드 MIT(f12), README 의 Llama Community License '적용될 수 있다'(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하고 해소하지 않음. 입출력 계약: OpenVLA 역정규화(f11), openpi 행동 청크·개방 루프(f15·f16), openpi 체크포인트에 π0.7 없음(f17). GR00T 행: N1.7 은 EA(f18), README License 절 코드/가중치 구분(f19), README 71행 '상용 가능' 문구는 벤더 주장(f20), 3B LICENSE 3.3절 비상업·NVIDIA 예외(f21), 세 문서 충돌(f22) — 표의 'GR00T N1 오픈소스(공개 모델)' 유형 칸에 '코드 Apache 2.0, 가중치 별도 라이선스' 주석. ROSA 행: FAQ 의 물리 상호작용 조건(f28)과 맞춤 도구 안전 검사 권고(f29). MCP 어노테이션 한계(f30)는 7절 또는 9절에 두되 기존 MCP 명세 서술(2026-09-29-area13-s6.md 45행 ref-856, C 트랙 stage-4 253행 ref-696)과 보완 관계로 적고 재서술하지 않음; 의견 f42·f43 / 섹션 8(분리 2026-09-30-area44-s8) — π0.7 항목 추가: 제어 모드 프롬프트(f23), 학습 중 지연 모사 240 ms(50 Hz)·UR5e 20 Hz(f24), seen/unseen 판정 어려움(f25) — 모두 회사 자체 보고서라 [추정]. LIBERO-Plus 항목 추가: 7개 교란 축(f26), OpenVLA-OFT 수치는 판을 밝혀 arXiv v3(로봇 37.2·카메라 59.7)와 CVPR 2026 게재본(로봇 31.9·카메라 56.4) 병기(f27). 국내 동향에 산업부 M.AX 휴머노이드 AI 파운데이션 모델 과제(f38); 의견 f44 / 섹션 9 — 로봇 자체 지능·제어 경계 아래에 도구 호출 실행 경계 문단: MCP 힌트는 강제 수단이 아님(f30), MoveIt Pro 의 읽기 전용 배포 키·서버 확인 프롬프트 없음·세션 종료 뒤 계속 이동·cancel 은 비상 정지 아님(f31~f33, 벤더 주장 [추정]), ROSA 맞춤 도구 조건(f28·f29); 의견 f45 / 섹션 11(분리 2026-09-30-area44-s11) — 부분 답(열린 채 둠): oq-216(배포물별 입출력 f11·f15·f16·f23, 의견 f42; 공통 등록 표준·적합성 시험 미확인), oq-217(연구 벤치마크 규모·조건 f1~f6·f8~f10·f26·f27; 설비·안전·시간창 통합 공통 기준 미확인), oq-219(Figure 기간 축 f34; 기점·종점 없어 미해소), oq-141(MoveIt Pro 는 승인을 클라이언트에 맡김 f32, 벤더). 관련 근거만: oq-104(f24 학습 조건 지연, 실측 아님), oq-218(f38, 실측 결과 없음). 답하지 못함: oq-314, oq-161. 메모 새 질문 1번(VLA 공통 최소 항목)은 문구 대조로 oq-216 과 같아 새로 만들지 않음; 2·3번과 라이선스 출처 충돌 2건을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/standards/index.md 287·288행 OpenVLA·GR00T N1 '오픈소스' 유형에 코드·가중치 라이선스 구분(f12~f14, f19~f22); docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md 118행 ROSA [추정] '확인·권한 장치 설명 없음'을 FAQ(f29)로 정리, 같은 파일 112·240행과 2026-09-30-area44-s6.md 57행의 disjunctive graph 번역어 통일, 같은 파일 310행 'IMR-Bench 규모 미확인'에 f3 연결; stage-2-data-and-standards.md 166·370행 SMART-LLM '원문 미열람'에 f1 연결; task-model-draft.md 133행 LLM+P 부분에 f7 연결. 다음 실행 후보: 59. 법·규제·보험·라이선스(f12~f22), 13. 대화형 기능의 신뢰·기반(f30~f33), 54. 시험·형식 검증·벤치마크(f26·f27) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반
- 원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반
- 출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 출처 충돌
- 출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f22 | 종류: 출처 충돌

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 15건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-05/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f14·f22: OpenVLA·GR00T N1.7 의 라이선스 문서 충돌은 문서끼리 대조한 것이며 배포자의 정정·법적 우선순위는 확인하지 못함. OpenVLA 카드는 메모의 고정 리비전 258bd1d 가 현재 main 이력에 없어 main(47a0ec7) 기준
    - ref-1608·ref-1610: OpenVLA 커밋 c8f03f4, openpi 커밋 215abfb 의 커밋 날짜 미확인. ref-1611: GR00T n1.7-release 는 브랜치 이름으로만 열어 커밋 sha 고정 못 함. ref-1618: MoveIt Pro 문서 세부 빌드·발행일 미확인
    - f17: openpi 에 π0.7 가중치가 없음을 README 목록으로 확인했을 뿐, π0.7 보고서와 공개 배포물의 대응(U10)·실제 네트워크 포함 최대 지연(U11)은 미확인
    - f10: S-ATLAS 실물 실험이 없다는 것은 열람 본문 검색 기준이며 보충 자료는 보지 않음. SMART-LLM 실물 시험 대수·반복 수(U03), IMR-LLM 장기 운영(U04) 미확인
    - f34: BMW–Figure 10/11개월의 기점·종점과 집계 관계, 교대별 실측 성공률·개입 분모(U13·U14), Figure 03 첫 시연 이후 가동률(U15) 미확인
    - f38: 산업부 M.AX 휴머노이드 과제와 로보티즈–BGF로지스 물류 과제의 동일성(U17), 자동화율 80%·성공률 90% 실측 결과(U16, oq-218) 미확인
    - 메모 V01(GR00T-N1.7-ApplePnP-V1 모델 카드)와 V11(BGF로지스 매거진 회고)은 신규 출처 예산(15건) 때문에 출처째 넣지 않음. 둘 다 벤더 [추정]이며 ROP 판단에 쓰는 내용(라이선스 충돌·80/90 실측 부재)은 다른 finding 이 담음
    - 병원·상업시설·실외에서 로봇 기반 모델·언어 모델 계획을 쓴 이기종 플릿 현장 실증(U18), 벤더 혼합 장기 운영 플릿의 독립 재현 로그(U02), VLA 공통 능력 등록 표준·적합성 시험(U06) 미확인
    - 메모가 진단에 쓴 위키 고정 커밋(85960d2)과 현재 배포판의 동일성 미확인(U01)
- 범위 경계 위반 의심:
    - f12~f22: 코드·가중치 라이선스 문구는 59. 법·규제·보험·라이선스 쪽 내용이므로 문서 원문 대조까지만 하고 상용 사용 가능 여부의 법적 판단은 하지 않음
    - f30~f33: 도구 호출 권한·승인·세션 종료는 13. 대화형 기능의 신뢰·기반, 29. 명령·작업 실행의 신뢰성과 겹치며, 이 영역에는 언어 모델 계획이 로봇 실행으로 넘어가는 경계 관점으로만 씀
    - f26·f27: LIBERO-Plus 는 단일 팔 조작 시뮬레이션 벤치마크로 54. 시험·형식 검증·벤치마크와 겹치며, 이 영역에는 VLA 수용 시험 설계의 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1607~ref-1621, 예약 구간 ref-1607~ref-1636 안), 재사용 4건(ref-090·ref-170·ref-092·ref-1051). 출처 매핑(검증 결과 기준): 메모 n1→ref-090, n2→ref-170, n3→ref-092, n4→ref-1607, n5→ref-1608, n6→ref-1609(main 47a0ec7 기준), n7→ref-1610, n8(ApplePnP 카드)→예산 초과로 제외, n9→ref-1611, n10→ref-1613, n11→ref-1612(같은 저장소 모델 카드 포함), n12→ref-1617, n13→ref-1616(ref-171·172 와 다른 페이지), n14→ref-1618, n15→ref-1051(글로벌 URL, 캐나다판 대신), n16→ref-1619, n17→ref-1620, n18→ref-1621, n19(BGF 매거진)→예산 초과로 제외, n20→ref-1614, 추가: CVPR 2026 게재본→ref-1615. 모든 출처 원문 열람(fetched true). 출처 type: OpenVLA·openpi·GR00T 저장소와 Hugging Face 모델 저장소 파일은 프로젝트가 관리하는 저장소라 '오픈소스 문서'로 두어 인터페이스·라이선스 원문 옮김(f11~f19, f21·f22)은 [사실]; MoveIt Pro·Figure·BMW 는 '벤더 문서'라 해당 finding 은 모두 [추정]·vendor_claim. 교차 확인 0건(SMART-LLM/IMR-LLM/S-ATLAS 는 조건이 달라 같은 주장 아님, OpenVLA 문서쌍·GR00T 문서셋·openpi/π0.7·LIBERO-Plus 두 판·BMW/Figure 는 같은 팀·기관·프로젝트). 검증 반영: F21 은 arXiv v3 값(37.2)에 판을 명시하고 CVPR 2026 게재본 값(로봇 31.9·카메라 56.4) 병기(f27); F13 '적용된다'→'적용될 수 있다'(f13); F14 현재 main 도 같은 문구라 충돌 지속(f14); F18/README 71행 '상용 가능'은 벤더 주장으로 분리(f20)하고 README·LICENSE·카드 3자 충돌 기록(f22); F06 은 성공률 하락의 예시이며 정량화 없음; F02 에 GPT-4·Claude-3 거절과 표 I 밖 명시; F05 에 15분 수동 장면 작성·반복 미보고; U10 을 f17 로; U13 Figure 세 기간을 f34 로; 위키 5절 93행 정정 제안(f37). 중복 제거: F01 은 C 트랙 stage-2 166행 기존 수치의 원문 확인 보강으로만(f1), F07 은 기존 [추정] 보강, F23 은 기존 MCP 명세 서술과 보완 관계로 서술, V08(BMW 10/11개월 충돌)은 기존 5절·oq-219 에 있어 새 finding 으로 넣지 않고 f34 근거 메모와 rationale 에 위치만 적음. 열린 질문: 부분 답 oq-216·oq-217·oq-219·oq-141, 관련 근거 oq-104·oq-218, 해결 제안 없음(open_questions_resolved 비움). 메모 새 질문 1번은 oq-216 과 같아 만들지 않고, 2·3번과 출처 충돌 2건을 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·표·행(저장 원문 기준)과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-10-12-04/research.md

```markdown
# 리서치 브리프 2026-10-12-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-04 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 47. AI·학습·적응과 모델 운영 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 67행 규제 문단이 한국 인공지능기본법을 '2026-01-22 시행'으로만 두고 '개정 법률의 시행일 … 미확인'으로 남김. EU AI Act 를 '부속서 I(기계류 등) 제품의 안전 구성요소 → 고위험'으로만 적어 2026/1744 개정(기계류의 Section B 이동, 제2조 2항 적용 조문 한정)을 반영하지 못함
- 섹션 4. 핵심 개념과 용어(분리 2026-09-25-area27-s4) — 등각 예측 항목(41행)에 보장의 전제(i.i.d. 보정, 정확한 사람 도움)가 없고, 모델 레지스트리 항목(44행)이 별칭 반영 시점을 말하지 않음. 정책·데이터 형식 호환성(전처리·보정판) 개념 없음
- 섹션 5. 적용 사례 — 가상 시나리오 두 개와 한진 기사뿐이고, 실제 플릿 단계 배포·운영 중 학습·국내 학습–운영 연계 사례가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행)이 ML Test Score 항목 수와 MLflow 별칭 교체 두 문장뿐이라 승인·카나리·롤백 연습, 배포 중단·롤백 실패 상태가 없음. KnowNo 문장(57행)이 보장 조건 없이 [사실]
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-25-area27-s7) — 모든 행이 원문 미열람, 로봇 정책 배포 호환성(LeRobot)·국내 공개 학습 데이터 판 관리 행 없음, NIST AI RMF 는 보도자료(ref-617)만 근거. 관련 법 문단(48행)이 3절과 같은 낡은 서술
- 섹션 8. 대표 연구와 자료(분리 2026-09-25-area27-s8) — 분포 이동 아래 재보정 연구와 플릿 규모 운영 중 학습 연구가 없음
- 섹션 9. 책임 경계 — 배포 후 감시·변경관리·복구 실패 처리의 책임 분담이 없음
- 섹션 11. 열린 질문 — oq-030 이 '이번 실행에서는 조사하지 않았다'로 남아 있으나 2026-10-10 영역 25 갱신에서 원문 수치가 이미 정리됨. 세 질문이 oq id 없이 '(신규 …)'로 표시됨. oq-105·oq-106·oq-107 근거 없음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 한국 법 개정 시행일, EU AI Act 기계류 Section B 이동, KnowNo 보장 조건, ref-168 저자 표기(후속)

## 조사 질문

1. AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
2. 모델 레지스트리의 별칭 교체·정책 정규화·데이터 형식 변경은 로봇에서 실제로 실행되는 모델 판과 어떻게 어긋날 수 있으며, 단계 배포·중단·롤백 실패는 어떤 상태로 기록되는가? (섹션 4·6·7 겨냥, oq-213)
3. oq-107 KnowNo 등각 예측 보장의 전제는 무엇이며, 분포가 바뀔 때 재보정은 어떤 조건(정답 관측·피드백)을 요구하는가? (섹션 4·6·8 겨냥, oq-222)
4. 플릿 규모 운영 중 학습과 국내 학습–운영 연계 발표는 어떤 조건·증거 수준의 사례인가, 국내 공개 로봇 조작 데이터의 판·분할 메타데이터는 믿을 만한가? (섹션 5·7·8 겨냥)
5. oq-106 2026-07-27 AI Act 통합판에서 기계류 연계 로봇 AI 에 어떤 조문이 적용되며, 중대한 변경 재평가·시판 후 감시 조문은 무엇을 정하는가? (섹션 3·7·11 겨냥)
6. oq-105 한국 인공지능기본법의 현행 판 시행일과 고영향 AI 사업자의 문서화 책무는 무엇인가? (섹션 3·7·11 겨냥)
7. oq-030 LTAA 원문 수치 충돌은 위키 안에서 어디까지 정리됐는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | MLflow v3.1.0 모델 레지스트리 문서는 별칭(alias)을 새 모델 버전으로 재지정하면 같은 별칭 기반 모델 로딩 코드가 다음에 실행될 때 새 버전을 자동으로 가져온다고 설명한다. 이미 실행 중인 프로세스나 연결이 끊긴 장치의 모델이 바로 바뀐다는 뜻은 아니다. | ref-1577 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [의견] | ROP 는 레지스트리의 목표 모델 버전과 각 로봇이 실제로 실행 중인 버전을 따로 기록하고, 별칭 변경 뒤 장치별 로딩·검증 응답을 받아야 교체가 끝났다고 볼 수 있다. | ref-1577 | 아니오 | low | 2026-10-12 | — | — |
| f3 | [사실] | LeRobot v0.6.0 하위 호환성 문서는 PR #1452 이후 정책 가중치에 내장되던 정규화 계층을 없애고 외부 PolicyProcessorPipeline 구성요소가 정규화를 맡도록 바꾼 변경을 '호환성 깨짐(Breaking Change)'으로 명시하고, 이전 모델은 이전(migration)이 필요하다고 적는다. | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | 같은 문서는 하드웨어 API 재설계(PR #777) 이전의 보정 방식으로 기록한 궤적을 그대로 불러오면 잘못 재생된다고 경고한다(SO100/SO101 예시의 관절 보정·입출력 변환). | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | LeRobotDataset v3.0 형식은 여러 에피소드의 표 행과 영상 프레임을 큰 파일로 이어 붙이고, 에피소드별 구간은 파일 경계가 아니라 메타데이터로 복원한다. | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [의견] | 학습 정책을 로봇에 배포할 때는 가중치 해시, 전·후처리기와 정규화 통계, 학습 데이터 커밋과 데이터 형식 판, 카메라·관절 스키마, 하드웨어 보정판, 런타임 판을 하나의 배포 묶음으로 기록하고 이전 묶음을 보존해야 되돌림이 가능하다. | ref-1578 | 아니오 | low | 2026-10-12 | — | — |
| f7 | [추정] | Mender 문서는 사용자 정의 업데이트 모듈(Update Module)이 롤백을 지원하려면 SupportsRollback 질의에 Yes 로 답하고, 설치 전에 '알려진 정상 상태(known good state)'를 저장했다가 롤백 때 복원하는 구현을 모듈 작성자가 넣어야 한다고 설명한다. | ref-1579 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f8 | [추정] | Mender 문서는 전원 상실 뒤 업데이트 상태가 다시 실행될 수 있으므로 업데이트 모듈을 멱등(idempotent)하게 만들어야 한다고 권고한다(should). | ref-1579 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f9 | [추정] | AWS IoT Jobs 문서는 작업 배포 속도(rollout)와 중단(abort) 설정을 두고, 실패한 장치 수 등이 지정한 기준에 도달하면 작업 배포를 취소할 수 있다고 설명한다. 이는 새 배포를 멈추는 것이며 이미 설치된 장치의 원복과는 별개다. | ref-1581 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f10 | [추정] | AWS IoT Greengrass v2 문서는 장치별 배포 실패 상태를 롤백 미요청(FAILED_ROLLBACK_NOT_REQUESTED), 이전 정상 구성으로 롤백 완료(FAILED_ROLLBACK_COMPLETE), 롤백 실패(FAILED_UNABLE_TO_ROLLBACK)로 나누고, 롤백하지 않았거나 롤백에 실패한 장치는 정상 동작하지 않을 수 있다고 적는다. | ref-1580 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f11 | [의견] | 모델 배포는 배포 중단, 이전 모델 복원 시도, 복원 확인을 서로 다른 상태로 기록하고, 확대 배포 여부는 집단 성공률만이 아니라 장치별 현재 버전·실패 사유·복구 결과로 판단하며, 복구하지 못한 로봇은 새 작업 배정에서 빼는 운영 정책을 두는 것이 맞다. | ref-1579, ref-1580, ref-1581 | 아니오 | low | 2026-10-12 | — | — |
| f12 | [추정] | Viam 문서는 새 모델을 플릿에 내보낼 때 갱신한 구성 조각(fragment)을 먼저 첫 집단(예: 카나리 위치)에만 적용해 관찰한 뒤 나머지 집단으로 넓히는 절차를 제시한다. | ref-1582 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f13 | [추정] | 같은 Viam 문서는 새 모델이 잘못 보이면 구성 조각에서 이전 판을 고정해 되돌리며, 장치들은 다음 구성 동기화 때(정상 운영에서는 수 초 안에) 이전 판으로 수렴한다고 설명한다. 연결이 끊긴 장치의 즉시 변경은 아니다. | ref-1582 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f14 | [사실] | ML Test Score 의 Infra4 항목은 모델이 실제 요청에 영향을 주기 전에 품질을 자동 검사해 모델을 승인(bless)하거나 거부(veto)해 운영 투입을 막는 절차를 권한다. | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | 같은 논문의 Infra6 항목은 오프라인 시험이 아무리 광범위해도 그것만으로는 운영 환경에서의 모델 성능을 보장할 수 없다고 밝히고, 소수 트래픽에 먼저 내보내는 카나리 방식을 완화책으로 든다. | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 논문의 Infra7 항목은 운영 모델을 이전 정상판으로 되돌리는 롤백을 비상 절차로 두고, 운영자가 비상 상황이 아닐 때 미리 연습해야 한다고 권고한다(should). | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [의견] | 로봇 모델의 운영 투입 승인 기록에는 장치·현장별 성능 하한, 기존 판 대비 퇴행, 로딩·추론 지연, 개입·실패 사례, 실제 롤백 연습 결과를 연결하고, 위험한 행동의 시험은 현장 안전 절차와 분리하지 않아야 한다. | ref-625 | 아니오 | low | 2026-10-12 | — | — |
| f18 | [사실] | KnowNo(Ren 외, CoRL 2023, PMLR 229) §3.1 의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 미지의 분포 D 에서 독립·동일 분포(i.i.d.)로 뽑힌다는 가정 위에 선다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [사실] | KnowNo 의 과제 성공 보장(§3.2 명제)의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [사실] | KnowNo 는 다단계 계획에서 시점 사이 의존성 때문에 i.i.d. 가정이 깨지는 문제를 다루려고 개별 시점 대신 시퀀스 수준에서 보정(sequence-level calibration)한다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f21 | [사실] | 적응형 등각 추론(Adaptive Conformal Inference, Gibbs·Candès, NeurIPS 2021)의 명제 4.1 은 분포가 시간에 따라 바뀌어도 장기간의 경험적 포함 빈도가 목표값에 맞는다는 장기 평균 보장을 준다. 논문 실험은 주가 변동성·선거 데이터이며 로봇 실험은 없다. | ref-1583 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | 같은 방법의 온라인 갱신은 직전 예측 집합들이 정답을 놓친 경험적 빈도(empirical miscoverage)를 보고 임계값을 조정하므로, 운영 중 정답(Y_t)을 관측할 수 있어야 쓸 수 있다. | ref-1583 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [의견] | 물류 지시 분포가 바뀌는 현장에서는 고정 간격(예: 매월) 재보정을 근거 없는 기본값으로 두지 말고, 지시 유형별 보정 오차와 데이터 변화 신호를 감시하며 피드백 지연·정답 수집 비용을 고려한 재보정 정책을 시험해야 한다. | ref-351, ref-1583 | 아니오 | low | 2026-10-12 | — | — |
| f24 | [사실] | 제조사 연구(저자 전원 AGIBOT 소속, 저자 보고)인 Learning While Deploying(LWD, arXiv v4)은 자사 Agibot G1 양팔 로봇 16대 플릿(식료품 보충 작업 4대, 장기 작업마다 3대)으로 8개 실물 조작 작업에서 온라인 학습을 했고, 방법마다 실험당 4시간 벽시계 예산(플릿 합계 약 60시간)을 줬다. | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f25 | [사실] | LWD 의 학습기는 50 학습 단계마다 갱신 정책을 플릿에 내보내고, 로봇 액터는 에피소드 경계에서 새 정책을 다시 불러온다(제조사 연구, 저자 보고). | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f26 | [사실] | LWD 저자는 한계 절에서 현재 정책 학습 틀이 실행 안전을 명시적으로 모델링하지 않으며, 단순한 실시간 갱신 일정이 대규모·장기 배포에 최적이 아닐 수 있다고 밝힌다. | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [의견] | 운영 중 학습하는 정책을 쓰는 플릿에서는 작업 이력마다 실행한 정책 판을 붙이고, 새 정책을 적용하는 경계(예: 에피소드·임무 단위)와 승인 주체를 명시해야 임무 도중 모델이 바뀌는 문제를 관리할 수 있다. | ref-1585 | 아니오 | low | 2026-10-12 | — | — |
| f28 | [추정] | LG CNS 는 2026-05-07 발표에서 로봇 학습·운영 플랫폼 '피지컬웍스'의 포지(Forge)에서 학습·검증한 로봇을 바통(Baton)으로 운영·관제하고, 이 과정에서 축적한 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 밝혔다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f29 | [추정] | 같은 발표는 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 '기대된다'고 적으며, 이는 실측 비교 결과가 아니라 회사의 기대치다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f30 | [추정] | 같은 발표는 포지가 20곳 이상 고객사와 로봇 개념검증(PoC)을 진행 중이고, 바통이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다고 주장한다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f31 | [의견] | 학습·운영 연계 플랫폼을 도입 검토할 때는 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청해야 한다. | ref-1584 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [사실] | AI-Hub '대규모 물리환경 로봇조작 데이터'(dataSetSn 71825)의 변경이력은 v1.0 을 2025-04-16 데이터 개방(Beta), v1.1 을 2025-06-30 데이터 최종 개방으로 표시한다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f33 | [사실] | 같은 페이지의 데이터 히스토리에서 2026-05-06 항목은 '기타 – 태그 추가'로만 표시돼 새 데이터 판 발행으로 볼 근거가 없다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f34 | [사실] | 같은 데이터의 학습용 구성표(라벨링 JSON 기준)는 총 262,166 건 중 학습 238,266 건, 테스트 23,900 건을 적으면서 표제는 '학습 데이터 (80%)', '테스트 데이터 (10%)'로 달아, 실제 비율(약 90.9%·9.1%)과 맞지 않고 검증 분할은 표기하지 않는다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f35 | [사실] | 같은 데이터의 원천 데이터는 실제환경 77,984 장, 가상환경 184,182 장(RGB 기준, Depth 같은 수)으로, 전체 262,166 장 가운데 약 70% 가 가상환경에서 취득됐다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f36 | [사실] | 같은 페이지의 분포 표는 원천 데이터 분포 비율을 실제 14.29%·가상 85.71% 로 적어 수량(약 29.7%·70.3%)과 맞지 않고, 라벨링 JSON 수량(77,984 + 184,182 = 262,166)의 합계를 524,332 로 적는다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f37 | [의견] | 공개 데이터의 분할비·합계가 서로 맞지 않으면 제공자 확인 전에는 표제 분할비를 모델 승인 근거로 쓰지 말고, 실물·가상 구분, 중복, 평가용 누출을 실제 파일로 따로 검사해야 한다. | ref-1588 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [사실] | NIST AI RMF 1.0(NIST AI 100-1)의 MANAGE 4.1 은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화(override), 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 한다(자율 적용 프레임워크). | ref-1586 | 아니오 | medium | 2026-10-12 | — | — |
| f39 | [의견] | 모델 공급자의 학습·검증 책임, ROP 의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할은 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다. | ref-1586 | 아니오 | low | 2026-10-12 | — | — |
| f40 | [사실] | EUR-Lex 의 AI Act(Regulation (EU) 2024/1689) 2026-07-27 통합판은 Regulation (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24 게재) 개정을 반영하며, 이 개정으로 부속서 I Section A 에서 기계류(1번 항목)가 삭제되고 Section B 21번에 기계류 규정 (EU) 2023/1230 이 추가됐다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f41 | [사실] | 개정된 AI Act 제2조 2항은 부속서 I Section B 의 조화 법령 대상 제품과 관련해 제6조 1항으로 고위험이 되는 AI 시스템에는 제6조 1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 해당 법령에 고위험 요구사항이 통합된 범위에서만 적용한다고 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [사실] | AI Act 제43조 4항은 적합성 평가를 거친 고위험 AI 시스템이 중대한 변경(substantial modification)을 겪으면, 변경된 시스템을 다시 유통하든 같은 배포자가 계속 쓰든 새 적합성 평가 절차를 거치도록 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [사실] | 같은 항은 출시·사용 개시 뒤에도 계속 학습하는 고위험 AI 시스템에서, 제공자가 최초 적합성 평가 때 미리 정하고 부속서 IV 2(f) 기술문서에 담은 시스템·성능 변경은 중대한 변경으로 보지 않는다고 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [사실] | AI Act 제72조 2항은 제공자의 시판 후 감시 체계가 배포자 제공 등으로 얻은 고위험 AI 시스템의 성능 관련 데이터를 수명 전반에 걸쳐 능동적·체계적으로 수집·문서화·분석하고, 관련되는 경우 다른 AI 시스템과의 상호작용 분석을 포함하도록 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [추정] | 제2조 2항 개정에 따라 기계류 규정 대상 로봇의 안전 구성요소로서 부속서 I 경로로 고위험이 되는 AI 에는 제43조(중대한 변경 시 재평가)와 제72조(시판 후 감시)가 AI Act 조문으로 바로 적용된다고 볼 수 없으며, 이 두 조문은 Section A 법령·부속서 III 경로의 고위험 AI 에 해당하는 내용으로만 소개해야 한다. 위키의 '부속서 I(기계류 등) 고위험' 서술도 이 이동을 반영해야 한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f46 | [의견] | EU 시장을 대상으로 할 때는 적용 관할·시스템 분류·공급자 지위를 먼저 정하고, 그 뒤 최초 평가에서 허용한 변경 범위와 실제 모델 변경 내역을 대조할 수 있도록 변경 기록을 보존하는 것이 맞다. | ref-1587 | 아니오 | low | 2026-10-12 | — | — |
| f47 | [사실] | 한국 인공지능기본법 제34조 1항은 고영향 인공지능 또는 이를 이용한 제품·서비스를 제공하는 인공지능사업자가 대통령령으로 정하는 바에 따라 각 호의 안전성·신뢰성 확보 조치를 이행하도록 하며, 5호는 그 조치 내용을 확인할 수 있는 문서의 작성과 보관이다. | ref-620 | 아니오 | medium | 2026-10-12 | — | — |
| f48 | [사실] | 국가법령정보센터의 현행 조문은 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」을 법률 제21311호(2026-01-20 공포·일부개정), 시행 2026-07-21 판으로 표시한다. 위키의 '2026-01-22 시행'은 최초 법률·시행령 기준이고 개정 법률의 시행일은 2026-07-21 이다. | ref-620 | 아니오 | medium | 2026-10-12 | — | — |
| f49 | [추정] | 제34조의 문서 작성·보관 책무가 물류 현장의 작업 계획·배정 AI 를 쓰는 ROP 에 걸리는지는 고영향 인공지능 해당성과 사업자 지위(제공자·이용자) 판단이 먼저이며, 시행령상 보존 기간도 이번에 확인하지 못했다. | ref-620 | 아니오 | low | 2026-10-12 | — | — |
| f50 | [의견] | ROP 는 학습용 데이터 개요, 모델 판, 위험 조치, 사람 감독, 승인·복구 기록을 서로 연결해 두어, 고영향 해당성이 판단되면 제34조 문서로 낼 수 있는 구조를 미리 갖추는 것이 좋다. | ref-620 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1577 | MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트) | Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0) | 2025-06-10 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx | 아니오 |
| ref-1578 | Hugging Face LeRobot 기여자 (huggingface/lerobot) | Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0) | 2026-07-06 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx | 아니오 |
| ref-1579 | Northern.tech (Mender documentation) | Create a custom Update Module | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.mender.io/artifact-creation/create-a-custom-update-module | 아니오 |
| ref-1580 | Amazon Web Services (AWS IoT Greengrass V2 Developer Guide) | Check deployment status | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html | 아니오 |
| ref-1581 | Amazon Web Services (AWS IoT Core Developer Guide) | How job configurations work | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html | 아니오 |
| ref-1582 | Viam | Roll out a new model to a fleet | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/ | 아니오 |
| ref-1583 | Gibbs, I., & Candès, E. J. (NeurIPS 2021) | Adaptive Conformal Inference Under Distribution Shift | 2021-12-06 | 논문 | high | 2026-10-12 | https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf | 아니오 |
| ref-1584 | LG CNS | LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개 | 2026-05-07 | 벤더 문서 | low | 2026-10-12 | https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1 | 아니오 |
| ref-1585 | Wang, Y. 외 (AGIBOT) | Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies | 2026-09-16 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2605.00416v4 | 아니오 |
| ref-1586 | NIST | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | 2023-01 | 정부·연구기관 | high | 2026-10-12 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 아니오 |
| ref-1587 | European Union (EUR-Lex) | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744) | 2026-07-27 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727 | 아니오 |
| ref-1588 | AI-Hub (한국지능정보사회진흥원) | 대규모 물리환경 로봇조작 데이터 | 2025-06-30 | 정부·연구기관 | medium | 2026-10-12 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100 | 아니오 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017-12 | 논문 | medium | 2026-10-12 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 아니오 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 2026-01-20 | 정부·연구기관 | medium | 2026-10-12 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md | 3, 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 3 — 67행 법·규제 문단 정정: 한국 인공지능기본법은 '2026-01-22 시행(최초 법률·시행령)'에 개정 법률 제21311호(2026-01-20 공포, 2026-07-21 시행, f48)를 더해 '개정 법률의 시행일 … 미확인'을 지움, 제34조 1항 5호 문서 작성·보관(f47, 해당성은 f49 [추정]). EU AI Act '부속서 I(기계류 등) … 고위험' 문장은 2026-07-27 통합판 기준으로 기계류 규정 (EU) 2023/1230 이 Section B(21번)로 옮겨졌고(f40) 제2조 2항이 Section B 관련 고위험 AI 에는 제6조 1항·제60a조·제102~112조만 적용한다(f41)는 점을 덧붙이고, 제43·72조를 로봇(기계류) AI 에 바로 연결하지 않음(f45 [추정]) / 섹션 4(분리 2026-09-25-area27-s4) — '등각 예측' 항목(41행)에 i.i.d. 보정 조건(f18)과 사람 도움 정확성 가정(f19) 추가, '모델 레지스트리' 항목(44행)에 별칭 반영 시점이 다음 로딩(f1)임을 보충, 배포 묶음 호환성(정규화 외부화 f3, 보정 방식 변경 f4, 메타데이터 기반 에피소드 f5) 항목 추가 / 섹션 5 — 출하 시나리오 '예외·성과' 칸(105행)에 별칭 반영 시점(f1)·오프라인 시험 한계와 카나리(f15)·롤백 연습(f16) 보강; 사례 추가: Viam 단계 배포·이전 판 고정(f12·f13, 벤더 주장 [추정]), LWD 플릿 온라인 학습(f24·f25·f26, '제조사 연구·저자 보고' 표기, 이종 플릿 아님), LG CNS 피지컬웍스 학습–운영 연계(f28~f30, 벤더 주장 [추정], 15%·18% 는 회사 기대치); 의견 f27·f31 / 섹션 6(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행): MLflow 별칭 문장에 반영 시점 범위(f1, 기존 문장은 틀리지 않음 — 범위 보충), ML Test Score 28개 항목 문장 뒤에 Infra4 승인·거부(f14), Infra6 오프라인 시험 한계(f15), Infra7 롤백 연습(f16); 롤백 구현 책임·배포 중단 상태(Mender f7·f8, AWS IoT Jobs f9, Greengrass f10 — 모두 벤더 주장 [추정]) 새 소절; '필요할 때 되묻기' 소절(57행) KnowNo 문장에 보장 조건(f18·f19·f20); 의견 f2·f11·f17·f23. 기존 내용 확인(새로 넣지 않음): Mender 상태 스크립트·롤백 표시·A/B 원자 배포·단계적 배포(2026-10-09-area43-s6.md 48~50행, 2026-09-30-area43-s6.md 57행; ref-1323·ref-1324·ref-1040), aws-samples ROS 2 OTA 자동 롤백(ref-556) / 섹션 7(분리 2026-09-25-area27-s7) — 표: MLflow 행(44행)에 v3.1.0 고정 문서 근거(f1, ref-1577, ref-626 은 latest 판), LeRobot v0.6.0 호환성·LeRobotDataset v3.0 행 추가(f3~f5), NIST AI RMF 행에 MANAGE 4.1(f38, 본문 PDF ref-1586), AI-Hub 71825 행 추가(f32~f36: v1.1 2025-06-30, 2026-05-06 은 태그만, 표제 80%/10% 와 실제 약 90.9%/9.1% 불일치·검증 분할 없음, 가상환경 약 70%, 분포 비율·JSON 합계 불일치; 의견 f37). 48행 관련 법 문단: 한국 법 시행일·제34조(f47·f48·f49, 의견 f50), EU AI Act 문장에 Section B 이동·제2조 2항(f40·f41)과 제43조 4항 재평가·사전 정한 지속학습 변경 예외(f42·f43)·제72조 2항(f44)을 '조문 내용 소개'로만 넣고 기계류 연계 로봇 AI 에 바로 적용되지 않음을 명시(f45 [추정]); 의견 f46. ISO/IEC 42001 행은 그대로(이번 원문 미확인) / 섹션 8(분리 2026-09-25-area27-s8) — KnowNo 항목(41행)에 PMLR 229 학회판과 가정(f18·f19·f20), ML Test Score 항목(50행)에 Infra4·6·7(f14~f16), ACI 항목 추가(f21·f22, 로봇 실험 없음), LWD 항목 추가(f24~f26, 제조사 연구·프리프린트) / 섹션 9 — 책임 경계: 배포 후 감시·변경관리(f38)와 공급자·ROP·현장 운영자 역할 분리(의견 f39), 배포 중단·복원 상태 기록과 복구 실패 로봇의 배정 제외(의견 f11) / 섹션 11 — oq-030: '이번 실행에서는 조사하지 않았다'를 기존 내용 확인으로 갱신(2026-10-10-area25-s6.md 59~63행, 2026-10-10-area25-s11.md 41행, 후속 질문 oq-356; LTAA 75.97%·77.1%·DP 0.95 는 새 finding 으로 넣지 않음), 상태 열림 유지. id 없이 '(신규 …)'로 적힌 세 질문은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같으므로 id 를 붙임. 부분 답(열림 유지): oq-105(f47·f48·f49), oq-106(f40~f45: 제품 안전 구성요소 해당성은 판단하지 않고, 기계류는 Section B·제2조 2항 경로임만 확인), oq-107(f18~f23: 가정 확인, 재보정 주기 미해결), oq-213(f12·f13 Viam 단계 배포·되돌림, 벤더 주장), oq-222(f21·f22 분포 이동 아래 온라인 재보정의 조건, 배정 정책 되돌림 기준은 아님). 새 질문 4건 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/categories/ai-and-learning/index.md 131행·160행과 docs/categories/safety/index.md 149행의 'EU AI Act 부속서 I(기계류 등) 고위험' 서술에 Section B 이동·제2조 2항(f40·f41) 반영, index.md 160행 '2026-01-22 시행'에 개정 법률 2026-07-21 시행(f48) 반영, ref-168 저자 표기('Kaitha, S., & Yu, S. 외' → Shyam prasad reddy Kaitha·Hongrui Yu 2명), ref-626 은 latest 판이라 고정 판 ref-1577 과 구분. 다음 실행 후보: 43. 데이터·관측성·배포(f7~f13), 57. 자산·소프트웨어 수명주기 관리(f3~f6), 59. 법·규제·보험·라이선스(f40~f49) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 57. 자산·소프트웨어 수명주기 관리 | 근거: f6 | 종류: 일반
- 운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 43. 데이터·관측성·배포 | 근거: f25 | 종류: 일반
- 출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825)의 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166) 가운데 어느 값이 맞으며 실제 배포 파일과 일치하는가? | 관련 영역: 47. AI·학습·적응과 모델 운영 | 근거: f36 | 종류: 출처 충돌
- 모델 공급자와 ROP 가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 59. 법·규제·보험·라이선스 | 근거: f39 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 12건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-04/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f45: EU AI Act 제2조 2항 개정에 따른 기계류 연계 로봇 AI 의 적용 조문 해석은 조문 범위에서 이끈 [추정]이다. 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지(제102~112조 개정 내용)와 개별 ROP 의 분류·제공자 지위는 확인하지 않음
    - f48: 인공지능기본법 시행령의 개정 판(독립 검증 보고상 2026-08-18 공포)과 고영향 영역 목록·보존 기간은 원문 확인하지 않음. 최초 법률·시행령의 2026-01-22 시행은 기존 위키 기준(ref-620)이며 이번에 다시 대조하지 않음
    - f32~f36: AI-Hub 71825 는 설명 페이지 메타데이터만 확인했고 실제 데이터 파일(건수·분할·실제/가상 구분)은 열지 않음. 표의 비율·합계 불일치의 정답은 제공자 확인 필요
    - f24~f26: LWD 는 저자 전원 AGIBOT 소속의 제조사 연구 프리프린트이며 독립 재현·안전 검증·이기종 장기 운영 성과는 없음
    - f7~f13, f28~f30: Mender·AWS·Viam·LG CNS 문서·발표만 근거라 벤더 주장 [추정]. 기존 위키는 Mender ref-1323 을 [사실]로 두었으나 이번 변환은 저장소 규칙(벤더 문서 단독 → 추정)을 적용. LG CNS 의 15%·18% 기대 효과와 PoC 현황은 독립 측정·확인 없음
    - 메모 F21(ISO/IEC 42001 공식 FAQ)은 독립 검증에서 원문을 열지 못했고(Cloudflare) 기존 위키(s7 42행, ref-618)와 중복이라 넣지 않음. ISO/IEC 42001·23894 유료 본문과 국내 로봇기업 인증 범위는 미확인
    - 메모 A15(LTAA 75.97%·77.1%·DP 0.95)는 2026-10-10 영역 25 갱신(2026-10-10-area25-s6.md 59~63행, area25-s11.md 41행, oq-356)과 완전 중복이라 새 finding 으로 넣지 않음. DP 0.95 와 Heavy Excels 77.1% 의 동일 조건 비교는 여전히 미해결
    - MLflow 별칭 변경이 이기종 플릿 전체에 원자적으로 반영되거나 연결이 끊긴 장치에서 즉시 복구되는지, 모델·전처리·보정판을 묶은 실물 전원 차단·복구 시험 결과는 확인하지 못함
    - KnowNo 의 물류 현장 재보정 주기(oq-107), ACI 의 피드백 지연 환경 로봇 성능, 로봇 모델별 보편 회귀 허용 임계값은 미확인
    - 메모가 조사 기준으로 쓴 고정 위키 커밋과 현재 배포판의 동일성은 확인하지 않음
- 범위 경계 위반 의심:
    - f40~f49: EU AI Act·한국 인공지능기본법의 적용 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인과 적용 범위 주의까지만 하고 개별 제품·사업자의 의무 발생 여부는 판단하지 않음
    - f7~f13: 장치 업데이트·단계 배포 도구(Mender·AWS IoT·Viam)는 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리와 겹치며, 이 영역에는 모델 교체·되돌림 관점으로만 씀
    - f24~f26: LWD 의 저수준 조작 정책 학습 자체는 로봇 자체 지능·제어(연계 대상)이며, 이 영역에는 정책 판 갱신 경계와 운영 기록 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 12건/15(ref-1577~ref-1588, 예약 구간 ref-1577~ref-1606 안), 재사용 3건(ref-625·ref-351·ref-620). 출처 매핑(검증 결과 기준): 메모 n1→ref-1577(MLflow v3.1.0 고정 문서; ref-626 은 latest 판이라 새 id), n2→ref-1578, n3→ref-1579, n4→ref-1580, n5→ref-1581(URL 을 /iot/latest/developerguide/ 표준 경로로), n6→ref-1582, n7→ref-351(PMLR 229 학회판으로 열람), n8→ref-1583, n9→ref-1584(뉴스와이어 재게시는 같은 출처), n10→ref-1585, n11→ref-625(DOI 10.1109/BigData.2017.8258038), n12→ref-1586(본문 PDF; 기존 ref-617 은 보도자료), n13→ref-1587(M1 Regulation (EU) 2026/1744 명시), n14→ref-620(법률 제21311호 조문), n15(ISO/IEC 42001)·n17(LTAA, ref-168)은 finding 이 없어 출처에서 뺌. 교차 확인 0건(모든 사실 finding 이 단일 출처, AWS 두 문서는 같은 기관). 검증 반영: (a) A13 에 옴니버스 2026/1744 의 Section B 이동·제2조 2항(f40·f41)을 넣고 제43·72조(f42~f44)는 조문 내용 소개로 한정, 로봇(기계류) AI 에 바로 연결하지 않는다는 점을 f45 [추정]으로 명시, oq-106 부분 답; (b) A15 LTAA 수치는 완전 중복이라 제외하고 11절 oq-030 문장 갱신만 제안; A11 의 '학습 80%' 표제를 사실로 옮기지 않고 불일치(f34·f36)와 가상환경 약 70%(f35)를 추가; LWD 는 '제조사 연구·저자 보고' 표기(f24~f26); 한국 법 시행일 2026-07-21·법률 제21311호(f48); 벤더 문서(Mender·AWS·Viam·LG CNS) 단독 finding 은 추정+벤더 주장(f7~f10, f12·f13, f28~f30); Mender 상태 스크립트·단계 배포·A/B 원자 배포, AWS ROS 2 OTA 샘플, ISO 42001 정의는 기존 내용 확인으로만 rationale 에 적음. 열린 질문: 해결 없음. 부분 답 oq-105·oq-106·oq-107·oq-213·oq-222, oq-030 은 기존 내용 확인(열림 유지). 메모 '답한 열린 질문'의 new-1~new-3 은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 4건은 기존 질문과 문구가 겹치지 않아 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 2026-10-10-area27-* 는 다른 영역이라 쓰지 않음. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-09/research.md

```markdown
# 리서치 브리프 2026-09-30-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-09 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 46. 예측·학습 기반 최적화 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 결정 중심 학습(예측 후 최적화), 예지 정비·예지(prognostics), 모방 학습, 안내 그래프 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·제조 공장·기타 현장의 학습·예측 적용 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 학습 기반 배정, 학습 기반 경로(MAPF), 학습과 탐색의 결합, 수요 예측의 배정 반영, 고장·배터리 예측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 13381(예지), POGEMA 벤치마크 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
2. 강화학습·모방학습·그래프 신경망 기반 다중 로봇 작업 배정 연구는 어떤 기준선 대비 어떤 개선을 보고하며, 실제 현장 검증이 있는가? (섹션 6·8 겨냥)
3. 학습 기반 다중 로봇 경로·교통(MAPF) 방법은 탐색 기반 방법과 비교해 어디서 앞서고 어디서 뒤지는가? (섹션 6·8 겨냥)
4. 작업 요청·물동량 같은 수요 예측을 배정·로봇 구성·인력 계획에 쓴 사례는 무엇이며 예측 오차와 분포 이동은 어떻게 다루는가? (섹션 5·6 겨냥)
5. 로봇 고장·배터리 상태 예측(예지 정비)을 계획·정비에 쓰는 연구·사례와 관련 표준은 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)
6. 예측 정확도가 아니라 결정 품질을 기준으로 예측 모델을 학습하는 개념(예측 후 최적화, 결정 중심 학습)은 무엇인가? (섹션 4·6 겨냥)
7. 예측·학습 기반 최적화에서 ROP가 직접 맡을 것과 로봇 제조사·상위 업무 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Amazon 연구진(Agaskar 외, arXiv 2508.08574, 2025-08 제출·2026-04 개정)의 DeepFleet 는 전 세계 아마존 창고에서 수십만 대 로봇의 위치·목표·상호작용 이동 데이터로 학습한 다중 로봇 기반 모델 모음으로, 로봇 중심(RC)·로봇–바닥(RF)·이미지–바닥(IF)·그래프–바닥(GF) 네 구조 가운데 비동기 상태 갱신과 국지 상호작용 구조를 쓰는 RC 와 GF 가 가장 유망하다고 보고했다. | ref-1105 | 아니오 | medium | 2025-08 | 물류창고 | — |
| f2 | [추정] | Amazon Science 블로그는 DeepFleet 가 풀필먼트·분류 센터 로봇의 미래 교통 패턴과 위치를 예측해 현재는 혼잡 예측으로 작업 배정과 경로를 병목 회피 쪽으로 조정하는 데 쓰이고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 하며, 로봇 이동 효율을 10% 높였다고 주장한다. | ref-1106 | 아니오 | low | 2025-08-11 | 물류창고 / 예외·성과 | 벤더 주장 |
| f3 | [사실] | Skrynnik 외의 POGEMA 벤치마크(ICLR 2025)는 고전 MAPF 에서 탐색 기반 중앙 계획기 LaCAM 이 다른 모든 방법보다 뚜렷이 앞서고 학습형 전용 해법(DCC·SCRIMP)이 그 뒤를 따르며 순수 다중 에이전트 강화학습(MARL)은 크게 뒤처지고 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했으며, 지속형(lifelong) MAPF 에서는 탐색 기반 RHCR 가 확장성 지표를 뺀 모든 경우에 우월했다고 보고했다. | ref-1109 | 아니오 | medium | 2025-04 | — | — |
| f4 | [사실] | Andreychuk 외의 MAPF-GPT(arXiv 2409.00134, AAAI 2025)는 전문가 MAPF 해의 대규모 데이터셋을 트랜스포머로 모방학습한 경로 찾기 기반 모델로, 추가 휴리스틱이나 에이전트 간 통신 없이 행동을 생성하며 기존 최고 학습형 MAPF 해법보다 뚜렷이 앞서고 학습 데이터에 없는 문제에서도 제로샷으로 동작한다고 보고했다. | ref-1107 | 아니오 | medium | 2024-08 | — | — |
| f5 | [사실] | Jiang 외의 SILLM(arXiv 2410.21415, ICRA 2025)은 모방학습에 통신 모듈·충돌 해소·전역 안내를 결합한 지속형 MAPF 방법으로, 최대 1만 대·대형 지도 6종에서 최고 학습 기반 기준선보다 처리량 137.7%, 최고 탐색 기반 기준선보다 16.0% 높았고 2023 League of Robot Runners 우승 해법을 앞섰으며 실물 로봇 10대와 가상 로봇 100대로 검증했다고 보고했다. | ref-199 | 아니오 | medium | 2024-10 | — | — |
| f6 | [사실] | Zhang 외의 안내 그래프 최적화(Guidance Graph Optimization, IJCAI 2024)는 지속형 MAPF 알고리즘이 따르는 격자 간선 가중치를 배치 전에 오프라인으로 최적화하거나 가중치를 생성하는 갱신 모델을 학습하는 방식으로, 대표적인 지속형 MAPF 알고리즘 3종의 처리량을 벤치마크 지도 8종에서 높였고 갱신 모델은 93×91 지도·에이전트 3,000개까지 적용됐다. | ref-1118 | 아니오 | medium | 2024-02 | — | — |
| f7 | [사실] | Agrawal·Bedi·Manocha 의 RTAW(ICRA 2023)는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 두고 로봇·작업 수와 무관한 전역 임베딩을 쓰는 주의 기반 정책을 PPO 로 학습해, 시뮬레이션 창고(로봇 최대 1,000대)에서 픽업 거리 최소화 탐욕 규칙·후회(regret) 기반 방법보다 총 이동 지연을 최대 14% 줄였다고 보고했다. | ref-623 | 아니오 | medium | 2022-09 | — | — |
| f8 | [사실] | Garces 외(arXiv 2608.21554, 2026-08)는 병원 입원 병동의 실제 간호 업무 요청 데이터를 써서, 작업이 요청으로 발생하는 이기종 다중 로봇 배정을 미래 요청 시나리오를 표본 추출해 평가하되 즉시 확정은 이미 들어온 요청에만 하는 예측 인지형 모델 기반 강화학습 롤아웃으로 풀었다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 시작 조건 | — |
| f9 | [사실] | 같은 연구(Garces 외)는 최근 예측 오차에 따라 예측 요청의 가중치를 다시 매기고 아직 시작하지 않은 배정만 다시 최적화하는 방식으로 분포 이동에 대응했으며, 배치 전에 과거 요청 데이터로 이기종 로봇 구성(차량 소요대수)을 고르는 절차를 두었다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 수행 자원 | — |
| f10 | [사실] | 같은 연구(Garces 외)는 반응형·토큰 패싱·예측 위치 선배치·근시적 탐욕 기준선과 비교해 거의 모든 요청을 처리하면서 대기 시간을 줄였고, 개선 폭은 꼬리 지연 지표에서 가장 컸다고 보고했다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 예외·성과 | — |
| f11 | [사실] | Elmachtoub·Grigas 의 Smart "Predict, then Optimize"(SPO)는 일반 기계학습이 예측 오차만 줄이고 예측이 어떻게 쓰일지 고려하지 않는다고 보고, 예측이 만든 결정 손실(SPO 손실)과 그 볼록 대리 손실 SPO+ 로 최적화 문제의 목적·제약을 학습에 반영했으며, 최단 경로·포트폴리오 실험에서 모형이 잘못 지정된 경우 특히 표준 예측 후 최적화보다 크게 나았다. | ref-1115 | 아니오 | medium | 2017-10 | — | — |
| f12 | [사실] | Poskart 외(Sensors, 2022-12)는 사내 물류·유연 생산 환경을 대상으로 MiR100 자율이동로봇의 미션별 배터리 소모를 회전 수·이동 거리·충전 상태(SoC)·SoC×거리 항을 쓰는 일반화 선형 모형으로 예측해 조정 결정계수 0.9629·0.9694 를 얻었고, 이 예측을 실행 전 미션 가능 여부 판단과 다른 로봇으로의 위임, 로봇 추가 필요 판단에 쓸 수 있다고 제시했다. | ref-1112 | 아니오 | medium | 2022-12-15 | 제약 | — |
| f13 | [사실] | Pookkuttath 외(Sensors, 2021-12)는 증기 걸레 청소 로봇의 관성 측정 장치(IMU) 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망으로 오프라인 92.2%, 싱가포르 기술디자인대학(SUTD) 캠퍼스 로비·푸드코트·복도의 실시간 현장 시험 91% 정확도를 보고했고, 분류 결과를 SLAM 지도에 겹친 예지 정비 지도로 정비 팀이 위험 구역을 격리하고 심각도를 판단하게 했다. | ref-1111 | 아니오 | medium | 2021-12-21 | 기타 / 예외·성과 | — |
| f14 | [추정] | 파이낸셜뉴스(2026-05-28)가 전한 현대자동차 발표에 따르면 현대차는 산업용 로봇팔의 모터 부하·진동·전류 신호를 학습한 AI 고장예측 시스템으로 고장 약 5일 전에 90% 이상 정확도로 이상을 감지하며, 국내 생산 현장에 먼저 적용한 뒤 해외 생산거점으로 넓혀 사후 대응에서 계획적 예측 정비로 바꾸려 한다. | ref-1113 | 아니오 | low | 2026-05-28 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f15 | [사실] | ISO 13381-1 은 기계 상태 감시·진단의 예지(prognostics) 일반 지침으로, 개발자·공급자·사용자·제조사가 예지 개념을 공유하고 정확한 예지에 필요한 데이터·특성·절차를 정하게 하는 것을 목적으로 하며, 2025년 3판이 2015년 2판을 대체했고 같은 시리즈의 다른 부는 성능 추세, 사이클 기반 수명 사용, 잔여 유효 수명 모델 같은 예지 접근을 다룬다. | ref-1114 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f16 | [추정] | 연계 대상: CJ대한통운은 2021년 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex 가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다. | ref-1117 | 아니오 | low | 2021-07-28 | 물류창고 / 수행 자원 | 벤더 주장 |
| f17 | [추정] | 확인한 자료를 종합하면 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에 대해, 개선 근거는 대부분 시뮬레이션·벤치마크이고(f3~f7) 실제 운영 개선 수치는 벤더 주장에 머물며(f2·f14·f16), 학습 단독 정책은 탐색 기반 방법보다 뒤지거나 분포 밖에서 실패할 수 있어(f3), 탐색·최적화와 결합하거나(f5·f6) 결정 손실로 예측을 학습하거나(f11) 관측된 요청만 확정하고 예측 오차로 재가중하는(f8·f9) 설계에서 개선이 보고되는 것으로 보인다. | ref-1109, ref-1107, ref-199, ref-1118, ref-623, ref-1106, ref-1113, ref-1117, ref-1115, ref-1116 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 대규모 플릿에서 혼잡을 미리 알아야 배정·경로를 조정할 수 있고(f1·f2), 요청이 시간에 따라 달라지고 분포가 바뀌며(f8·f9), 예측 정확도가 높아도 결정 품질이 따라오지 않을 수 있고(f11), 배터리 소모와 고장이 계획을 어긋나게 하기 때문이다(f12~f14). | ref-1105, ref-1106, ref-1116, ref-1115, ref-1112, ref-1111, ref-1113 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 확인한 자료를 종합하면 46. 예측·학습 기반 최적화에서 ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델에의 공급(f1·f8·f12), 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스(f2·f12), 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시(f3·f9), 학습 정책의 즉시 확정 범위 제한(f8)이다. | ref-1105, ref-1106, ref-1116, ref-1112, ref-1109 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 연계 대상: 분류 원문 19장 기준으로 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시와 배터리 셀 관리(f13·f14)는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측(f16)은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다. | ref-1111, ref-1113, ref-1117 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 이 영역은 학습 기반 배정의 25. 작업 배정 — MRTA(f7·f8), 학습 기반 경로의 27. 다중 로봇 경로·교통 관리 — MAPF(f3~f6), 결정 중심 예측의 26. 작업 순서·스케줄링(f11), 배터리 예측의 28. 공용 자원·충전·에너지 최적화(f12), 고장 예측의 38. 모니터링·이상 탐지·원인 분석(f13·f14), 분포 이동 감시의 47. AI·학습·적응과 모델 운영(f9), 벤치마크의 54. 시험·형식 검증·벤치마크(f3), 기반 모델 흐름의 44. 로봇 기반 모델·언어 모델 계획(f1·f4), 로봇 구성 산정의 35. 처리능력·규모·배치 설계(f9·f12), 정비 기준의 57. 자산·소프트웨어 수명주기 관리(f15), 수요 정보의 23. 업무 시스템 연동(f16), 적용 현장인 61. 물류창고(f1·f2·f16)·62. 제조 공장(f14)·63. 병원·의료(f8~f10)·67. 기타 현장(f13)과 이어진다. | ref-623, ref-1116, ref-1109, ref-1107, ref-199, ref-1118, ref-1115, ref-1112, ref-1111, ref-1113, ref-1105, ref-1106, ref-1114, ref-1117 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1105 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 2025-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2508.08574 | 아니오 |
| ref-1106 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 2025-08-11 | 벤더 문서 | medium | 2026-09-30 | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination | 아니오 |
| ref-1107 | Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv, AAAI 2025) | MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale | 2024-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.00134 | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-1109 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 2025-04 | 논문 | high | 2026-09-30 | https://arxiv.org/abs/2407.14931 | 아니오 |
| ref-623 | Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023) | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2209.05738 | 아니오 |
| ref-1111 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 2021-12-21 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ | 아니오 |
| ref-1112 | Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors) | Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems | 2022-12-15 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/ | 아니오 |
| ref-1113 | 파이낸셜뉴스 | 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지 | 2026-05-28 | 기사 | low | 2026-09-30 | https://www.fnnews.com/news/202605280925297568 | 아니오 |
| ref-1114 | ISO (ISO/TC 108) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine … — Prognostics — Part 1: General guidelines (제목 일부는 검색 결과 기준) | 2025 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/88029.html | 예 |
| ref-1115 | Elmachtoub, A. N., & Grigas, P. (arXiv, Management Science) | Smart "Predict, then Optimize" | 2017-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1710.08005 | 아니오 |
| ref-1116 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 2026-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2608.21554 | 아니오 |
| ref-1117 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 … (제목 일부만 확인) | 2021-07-28 | 벤더 문서 | medium | 2026-09-30 | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 | 아니오 |
| ref-1118 | Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024) | Guidance Graph Optimization for Lifelong Multi-Agent Path Finding | 2024-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2402.01446 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f18(왜 중요한가), f17(핵심 질문 답, 추정) / 섹션 4: 결정 중심 학습 f11, 예지·예지 정비 f13·f15, 모방 학습 f4·f5, 안내 그래프 f6 / 섹션 5: 물류창고 — f1·f2(DeepFleet, 예외·성과는 벤더 주장 병기)·f16(수행 자원: 인력 배치, 연계 대상·벤더 주장 병기), 병원 — f8(시작 조건: 간호 업무 요청)·f9(수행 자원: 이력 기반 플릿 구성)·f10(예외·성과), 제조 공장 — f14(현대차 로봇팔 고장 예측, 벤더 주장 병기), 기타 — f13(대학 캠퍼스 청소 로봇 예지 정비). 상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 학습 기반 배정 f7·f8·f9, 학습 기반 경로 f3~f6(학습 단독 대 탐색 결합 대비), 예측을 결정 기준으로 학습 f11, 배터리·고장 예측 f12~f14 / 섹션 7: POGEMA 벤치마크 f3, ISO 13381-1 f15(원문 미열람) / 섹션 8: f1·f3~f13 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67 / 섹션 11: open_questions_new 5건. 교차 규칙에 따라 25. 작업 배정 — MRTA 페이지에 f7·f8·f17, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f3~f6, 38. 모니터링·이상 탐지·원인 분석 페이지에 f13·f14 반영을 다음 실행 후보로 남긴다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 결정 중심 학습 | Decision-Focused Learning (Smart Predict-then-Optimize) | 예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다. |
| 예지 정비 | Predictive Maintenance | 설비·로봇의 상태 신호로 고장이나 성능 저하를 미리 예측해 고장 전에 정비 시점과 조치를 정하는 정비 방식이다. |
| 모방 학습 | Imitation Learning | 전문가(예: 탐색 기반 계획기)가 만든 해나 행동 기록을 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다. |
| 안내 그래프 | Guidance Graph | 지속형 다중 에이전트 경로 찾기에서 로봇이 지나는 격자 간선에 가중치를 매겨 교통 흐름을 유도하는 그래프로, 배치 전에 최적화하거나 학습된 모델로 생성한다. |

## 열린 질문

새로 생긴 질문:

- 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f2 | 종류: 일반
- 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? | 관련 영역: 46. 예측·학습 기반 최적화, 38. 모니터링·이상 탐지·원인 분석 | 근거: f14 | 종류: 일반
- 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f9 | 종류: 일반
- 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? | 관련 영역: 46. 예측·학습 기반 최적화, 23. 업무 시스템 연동 | 근거: f16 | 종류: 일반
- 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 61. 물류창고 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 14건
- 미확인 항목:
    - f2 DeepFleet 효율 10% 개선: 아마존 자체 자료뿐이며 독립 출처로 교차 확인하지 못함
    - f14 현대차 고장 5일 전·정확도 90% 이상: 회사 발표를 전한 기사 1건뿐, 정확도 산정 방법 미확인
    - f15 ISO 13381-1:2025: ISO·SCC 페이지 403 으로 원문 미열람, 제목 끝부분과 범위는 검색 결과 요약 기준
    - f4 MAPF-GPT 데이터셋 크기·전문가 해법·지속형 MAPF 결과는 초록에 없어 미확인(검색 요약의 지속형 MAPF 제로샷 서술은 넣지 않음)
    - f3~f8·f11 은 초록(POGEMA 는 HTML 본문 결과 절) 기준이며 실험 세부 조건 미확인
    - f16 CJ대한통운 이커머스 주문량 예측 정확도 88%: 검색 요약에만 있고 연 자사 게시물에서 확인하지 못해 넣지 않음
    - Malus 외 다중 에이전트 강화학습 AMR 주문 배차(CIRP Annals 2020, 제조 공장): ScienceDirect 403 으로 넣지 않음
    - ACM Computing Surveys 다중 로봇 작업 배정 체계적 문헌 고찰(2024): ACM 403 으로 넣지 않음
    - 상업 시설·가정·실외 현장의 학습·예측 적용 사례는 찾지 못함(보도 배달 로봇 수요 예측 검색 1회에서 적합한 1차 자료 없음)
    - 국내 학술지의 강화학습 기반 다중 로봇 배정·경로 논문은 검색 1회에서 찾지 못함
- 범위 경계 위반 의심:
    - f13·f14: 로봇 부품 수준 진동·전류 기반 고장 감지는 로봇 제조사·설비 정비 쪽 기법이므로 예측 결과를 정비 계획에 쓰는 근거로만 제안하고, 경계는 f20 에서 '연계 대상: '으로 구분함
    - f16: 전사 주문 수요예측은 분류 원문 19장의 상위 업무 시스템 연계 대상이므로 claim 을 '연계 대상: '으로 시작함. 46번 정의의 '수요·고장 예측'과의 경계는 열린 질문으로 올림
    - f1·f2: DeepFleet 의 미래 교통 예측은 운영 결정용 예측으로 다루며 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)이나 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 14건/15(ref-1105~ref-1118, 예약 구간 안). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건). 원문 열람: 13건 webfetch 로 열었고 ISO 13381-1(ref-1114)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Pookkuttath 외(ref-1111)·Poskart 외(ref-1112)는 PMC 본문, POGEMA(ref-1109)는 HTML 본문 결과 절, 나머지는 초록 페이지다. 교차 확인 0건: 핵심 수치가 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더·회사 발표만 근거로 한 f2·f14·f16 은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에는 f17 로 답했고 결론은 '개선 근거는 주로 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장이며, 학습 단독보다 탐색·최적화와 결합하거나 결정 손실로 학습하는 설계에서 개선이 보고된다'는 추정이다. 현장 유형 사례는 물류창고(f1·f2·f16)·병원(f8~f10)·제조 공장(f14)·기타(f13, 대학 캠퍼스)이며 상업 시설·가정·실외는 찾지 못했다. 국내 자료는 파이낸셜뉴스(ref-1113)·CJ대한통운(ref-1117) 두 건이고 국내 학술·표준 자료는 찾지 못했다. L. AI·학습 기술 교차 규칙에 따라 학습 기반 배정은 25. 작업 배정 — MRTA, 경로는 27. 다중 로봇 경로·교통 관리 — MAPF, 고장 예측은 38. 모니터링·이상 탐지·원인 분석과 함께 연결하도록 제안했다. 용어집에 이미 있는 상태 기반 정비·현실 격차·지속형 MAPF·MRTA·충전 상태·배터리 건강 상태는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### data/source_texts/ref-125.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
  "title": "Task Request",
  "description": "Describe a task request",
  "type": "object",
  "properties": {
    "unix_millis_earliest_start_time": {
      "description": "(Optional) The earliest time that this task may start",
      "type": "integer"
    },
    "unix_millis_request_time": {
      "description": "(Optional) The time that this request was initiated",
      "type": "integer"
    },
    "priority": {
      "description": "(Optional) The priority of this task. This must match a priority schema supported by a fleet.",
      "type": "object"
    },
    "category": { "type": "string" },
    "description": {
      "description": "A description of the task. This must match a schema supported by a fleet for the category of this task request."
    },
    "labels": {
      "description": "Labels to describe the purpose of the task dispatch request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
      "type": "array",
      "items": { "type": "string" }
    },
    "requester": {
      "description": "(Optional) An identifier for the entity that requested this task",
      "type": "string"
    },
    "fleet_name": {
      "description": "(Optional) The name of the fleet, or an array of fleet names, allowed to perform this task. If specified, only the named fleet(s) will bid for this task.",
      "oneOf": [
        { "type": "string" },
        { "type": "array", "items": { "type": "string" } }
      ]
    }
  },
  "required": ["category", "description"]
}
```
