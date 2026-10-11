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

### runs/2026-10-12-06/verification.json

```json
{
  "run_id": "2026-10-12-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv html v3 에서 분포 밖 지표가 Cities-tiles(학습에 쓰지 않았고 장애물 구조가 다른 지도)로 계산됨을 열람 확인. 단일 출처, 격자 벤치마크 정의."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 한계 절의 'communication between agents is not currently disentangled' 열람 확인. 통신 장애 안전성 주장으로 확대하지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 고정 커밋 9d5e337 evaluation.md 에서 7개 지도 12개 인스턴스, 팀 크기 50~10,000, GPU(EPYC 7R13 32 vCPU·128 GiB·A10G)·CPU(32 vCPU·64 GiB) 인스턴스 열람 확인. 다만 evaluation.md 본문에 '2026' 표기는 없어 '고정 커밋 기준'을 밝혀야 한다. 커밋 날짜 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: updates.md 에서 2026-09-02 결과 발표, 2026-08-10 지연, 2026-07-23 마감(8월 7일 발표 예정), 2026-05-26 AAMAS Prize(SmartPath), Combined·Task Scheduling·Line Honours 1위 No Man's Sky, 69팀·3,361건 열람 확인."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f3·f4 에 근거. 구축자 의견임을 밝혀야 한다. LoRR 주 위치는 27·54·25 영역."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv html v2 Table III 의 지도별 처리량 6쌍과 단계당 계획 시간 0.349초·4.143초가 브리프와 일치. '8회 평균'은 이번 검증에서 따로 확인하지 못함."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 초록 16.0% 확인, Table III 값으로 지도별 비율 평균을 다시 계산하면 약 16.05%로 일치. 논문이 계산 방식을 밝히지 않으므로 해석은 [추정]으로 둔다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 부록 E 의 72 vCPU EPYC 9754·RTX 4090D 4장·240GB, 지도당 12시간 미만(html 렌더링에 '1212'로 깨져 보임) 확인. 저장소 README 는 약 64 vCPU 로 적어 서버 표기가 조금 다르다. 브리프는 논문 기준이라 문제없다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: DiligentPanda 공식 저장소 static_guidance README 에서 브랜치별 버전 관리와 map_weights_path 를 빈 문자열로 두면 Backward Dijkstra 가 된다는 설명 열람 확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 1-GPU 예시 YAML max_dagger_iterations 100(주석 포함)과 논문 §IV 의 12회 반복 확인. 같은 연구팀 자료라 교차 확인이 아니다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f6~f10 에 근거. 구축자 의견임을 밝힌다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv html §5.1 에서 단계당 CPU 1초, 시간 초과 해에 같은 수리 기법, 보류 환경 16개 평균, T=800 확인. JAIR 기사 페이지에서 게재일 2026-03-24, 85권 확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Table 3 Symbotic 블록의 RH-PBS·RL-RH-PP·WPPL 에이전트당 처리량(80·100·120대) 일치. 단일 연구 안의 자체 비교라 밀도별 해석으로 한정한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5.1.2 의 밀도별 정책 처음부터 학습, 120대에서 약 4일, RTX 6000 Ada 1장 확인."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.1 지표가 처리량과 계획기 호출 대비 대체(fail) 정책 호출 비율임을 확인. 600초×10회 조건은 2026-10-10-area27-s8 기존 내용과 겹치므로 기존 각주(ref-604)를 재사용한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.4 에서 'LRGW and PIBT achieve the best performance on different maps and at different values of W' 확인. 원문은 Guided PIBT 도 비교했고(어느 조건에서도 최선이 아님), 브리프 근거 발췌가 비교 대상을 두 개로 적은 것은 부정확하다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §V-A.4 의 1,000단계, 단계당 1초, 무작위 5회 평균, Threadripper 3990X·192GB, CMU 저자 확인. 학습이 없는 고전 알고리즘이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: RHCR 외 알고리즘은 직전 단계 경로를 쓰고, RHCR 는 K초를 받아 시간 초과 시 K단계 동안 PIBT 로 실행한다는 설명 확인."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f17·f18 에 근거. 구축자 의견. PUSH 는 대조군·경계 설명으로만 쓴다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5 의 지도별 256대 학습, 32~320대(32 간격) 평가, 512단계, 지도 간 일반화는 다루지 않음 확인. SILLM 과 공동 저자(Jiang·Li 등)라 독립 재현이 아니다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 부록 C.3 의 실물 8대·가상 248대 혼합 현실 창고 확인. 실물 256대 운영이 아니다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5.2 의 'leave the adaptation of IL methods to the LMAPF-R2 model for future work' 확인."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지: arXiv v3(2026-04-13) §4 의 7개 층·7일 보류 자료와 60초 궤적 추론 확인. arXiv 페이지에 'Unpublished technical report, Amazon Robotics, Aug. 2025' 표기(journal-ref 가 아니라 report number 칸)."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지: Table 2 열 구성(파라미터 수, DTW 위치·상태·시점, CDE %)을 다시 열어 RC 3.40·RF 9.60·IF 186.56·GF 14.22 가 CDE 열임을 확인. 같은 행의 DTW 시점 값(14.91 등)과 섞지 않아야 한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지: aboutamazon 요약 'will improve robot fleet travel efficiency by 10%', 본문 'improving the travel time…by 10%', 'By reducing robot travel time by 10%' 확인. amazon.science(2025-08-11) 'efficiency of our robot deployments by 10%' 확인. aboutamazon 페이지 본문에는 발행일 표기가 없고 업계 매체는 2025-06-30 으로 적어, 2025-07-01 은 페이지 메타 기준으로만 쓴다. 두 출처 모두 Amazon 이라 독립이 아니다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f23~f25 에 근거. 구축자 의견임을 밝힌다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5.1 의 BIDMC(Beth Israel Deaconess Medical Center) 서관 입원 병동 4개 층, 층당 약 25~30병상, 2024-06-24~2025-06-29, 층당 42일, 정책당 168 층-일, 오전 6시~오후 6시 12시간 확인. 실물 로봇 배치가 아닌 이력 기반 시뮬레이션이다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §4.6 의 관측 요청·예약 요청 가중치 1, 예측 요청은 신뢰도 가중치(하한 λ_min) 확인."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Table 3 수요 높음에서 Greedy·Proposed 등 36,948/0, Token Passing·Token Passing with Task Swaps 만 36,920/28 확인."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §5.5.4 의 평균 대기 중앙값 약 5%, 95분위 대기 약 10%, 75분위·최댓값 15% 넘게 감소, 95분위 지표에서 가장 크고 일관된 개선 확인. 기존 s8 의 '구체 수치는 초록에 없다' 정정 근거로 쓸 수 있다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f16·f28 에 근거. 구축자 의견. 공통 분포 이동 임계값의 근거는 없다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Europe PMC 전문에서 Snail 로봇, 요청 방식 수집, 시험 표본 100개(Table 5), 클래스별 88.7~93.5%, 실시간 약 91% 확인."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ISO 공식 페이지에서 제3판, 발행 2025-09, 단계 이력의 2025-09-02, 60.60, 23쪽, ISO/TC 108/SC 5 확인. 규범 본문은 유료라 열지 않았다(서지 메타데이터 주장이라 문제없다)."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_battery README(고정 커밋)의 SimpleMotionPowerSink·SimpleDevicePowerSink 설명 확인. 물리 모델 API 이며 28. 공용 자원·충전·에너지 최적화 맥락에 둔다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f32~f34 에 근거. 구축자 의견. oq-221 부분 근거일 뿐이다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-125.txt)의 fleet_name oneOf string/array 설명과 rmf_api_msgs CHANGELOG 0.7.0(2026-09-18) 확인. 둘 다 open-rmf 자료라 독립 교차 확인은 아니다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f28·f36 에 근거. 구축자 의견. oq-223 은 열린 채로 둔다. 상위 수요예측은 19장의 외부 연계 대상으로만 서술한다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: jkros 전문 페이지(DOI 리디렉션)에서 Isaac 시뮬레이터, 이동 로봇 2대, Xeon Silver 4210R·RTX A5000 3개, 실제 하드웨어 검증이 향후 연구임을 확인. PDF 는 압축돼 읽지 못했다. 발행일은 2023-05-31 이며 브리프의 '2023-06'과 다르다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.2절의 '정책 파라미터들의 등급이 모두 같아서 … 판정하기 어려워진다' 서술 확인."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지: 현대자동차그룹 Story(2026-04-16)의 알티올 공동 개발 WCS 오르카, 설비 상태·우선순위에 따른 동선·작업 순서 실시간 조정, 어댑터 인터페이스 문장 확인. 학습 모델과 성과 수치에 대한 언급은 없다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f40 에 근거. 구축자 의견. 오르카는 20. 로봇·제조사 관제 연동과 61. 물류창고 쪽 경계 사례로만 쓴다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Crossref DOI 10.1287/mnsc.2020.3922 의 Management Science 68(1):9–26, 2022-01 확인."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 근거 출처 다섯 개(ref-199·ref-1639·ref-1062·ref-1641·ref-916)는 모두 확인. '찾지 못했다'는 리서치 범위 안의 진술이며, oq-220 을 해결한 것이 아니다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견: f6·f13·f16·f17·f18 에 근거하며 해당 사실은 모두 확인. 구축자 의견임을 밝힌다."
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
      "f6: SILLM 의 WPPL 비교 조건(회전 제거·LNS 40,000회)은 2026-10-10-area27-s8 42행에 이미 있음 — 같은 ref-199 각주 재사용, 재서술하지 않음",
      "f15: LSMART 600초×10회·실패 정책 개념은 2026-10-10-area27-s8 43행에 이미 있음 — 새 내용은 대체 정책 호출 비율 지표뿐, ref-604 재사용",
      "f36: fleet_name 필드 자체는 2026-09-29-area09-s7 40행에 이미 있음 — 새 내용은 배열 허용뿐, ref-125 재사용",
      "f25: 기존 5절 물류창고 예외·성과 칸 '아마존은 로봇 이동 효율을 10% 높였다고 주장'(ref-1054)과 충돌 — 출처 표현(미래형·이동 시간·배치 효율)으로 정정 대상",
      "f30: 기존 분리 페이지 s8 의 'Garces 외 구체 수치는 초록에 없다'를 본문 수치로 정정 대상",
      "f6·f13: 기존 6절 첫 문장 '같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고'([추정])를 지도·밀도별로 우열이 갈린다는 근거로 보강 대상(기존 문장을 뒤집지 않고 조건을 덧붙임)"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "브리프의 'SoC' 표기가 용어집 '충전 상태 (State of Charge (SOC))'의 약어 표기 SOC 와 다르다",
      "'지속형 MAPF'는 용어집 '지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))'와 맞추어 첫 등장 시 풀어 쓴다"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f25(5절 물류창고 예외·성과 칸): '아마존은 로봇 이동 효율을 10% 높였다고 주장하며' 문장을 f25 내용(발표 요약은 '높일 것'이라는 미래형, 본문은 '이동 시간 10%', Amazon Science 블로그는 '로봇 배치 효율 10%', 비교 기간·대상 현장·분모 미공개)으로 바꾸고 [추정] 벤더 주장[^ref-916][^ref-1054]을 유지한다 — 두 출처의 표현이 서로 다르고 기존 문장의 과거형 '높였다'를 뒷받침하지 않는다.",
    "ref-916: 각주 발행일은 2025-07-01 로 두되, 본문에서 발표일을 적을 때는 '2025-07-01(페이지 메타 기준)'으로 쓴다 — 검증 열람에서 페이지 본문에 날짜 표기가 없었고, 업계 매체는 2025-06-30 으로 적는다.",
    "f23·f24(5절·8절): DeepFleet 오프라인 예측 평가와 CDE 3.40% 는 [추정] 벤더 주장으로 쓰고, ref-1053 이 Amazon Robotics 의 동료 심사 없는 기술보고서임을 밝힌다. CDE 는 Table 2 의 CDE 열 값(RC 3.40·RF 9.60·GF 14.22·IF 186.56)만 쓰고 같은 행의 DTW 값과 섞지 않는다 — 회사 자체 보고서이고 표에 지표가 여러 열 있다.",
    "f6(6·8절): 'Table III 8회 평균' 가운데 '8회 평균'은 본문에서 뺀다 — 검증에서 확인하지 못했다. 지도별 값과 계획 시간(0.349초·4.143초)은 그대로 쓴다.",
    "f7: 16.0% 를 지도별 처리량 비율의 평균으로 읽는 해석은 [추정]으로 두고, 논문이 계산 방식을 밝히지 않았음을 같은 문장에 적는다 — 재계산(약 16.05%)과 일치하지만 저자 진술은 아니다.",
    "f3·f4(7절 League of Robot Runners 행): 평가 구성은 'web_resource 고정 커밋 9d5e337 의 evaluation.md 기준'임을 밝히고(그 문서에 연도 표기가 없다), 이 영역에는 요약과 27. 다중 로봇 경로·교통 관리 — MAPF·54. 시험·형식 검증·벤치마크·25. 작업 배정 — MRTA 로의 연결만 둔다 — 대회 평가의 주 위치가 그 영역들이다.",
    "f16(6절 실패·복귀 처리 소절): LSMART 가 비교한 대체 정책을 PIBT·LRGW 둘로 적지 말고 '여러 대체 정책 가운데 조건에 따라 LRGW 또는 PIBT 가 최고'로 쓴다 — 원문은 Guided PIBT 도 비교했다.",
    "f13: RL-RH-PP 는 80대에서 RH-PBS 보다 낮고 100·120대에서 높았다는 점을 함께 적고, 단일 연구 안의 자체 비교임을 밝힌다 — 밀도에 따라 우열이 갈린다.",
    "f20~f22(6·8절 SJRL): SILLM 과 공동 저자(Jiang·Li 등)의 연구라 독립 재현이 아님과, 물리 검증이 실물 8대·가상 248대 혼합 현실이라는 점을 함께 적는다.",
    "f17·f18·f19(PUSH), f34(rmf_battery), f40·f41(오르카): 학습 성과의 근거로 쓰지 않고 대조·경계 설명으로만 둔다. 각각 27. 다중 로봇 경로·교통 관리 — MAPF, 28. 공용 자원·충전·에너지 최적화, 20. 로봇·제조사 관제 연동·61. 물류창고 로 연결하고, 오르카 문장은 [추정] 벤더 주장[^ref-1644]으로 쓴다 — 셋 다 학습 요소가 없다.",
    "f38·f39(5절 제조 공장): 강민교·김인철 연구는 'Isaac 시뮬레이터 안 이동 로봇 2대의 시뮬레이션 연구'로 표시하고 실제 배치 사례로 쓰지 않는다. 각주 발행일은 2023-05-31 로 고친다(브리프 '2023-06'은 부정확하다).",
    "f27~f30(5절 병원, 8절 Garces 외): BIDMC 는 첫 등장 시 Beth Israel Deaconess Medical Center 로 풀어 쓰고, 평가가 실물 로봇 배치가 아닌 요청 이력 기반 시뮬레이션임을 밝힌다.",
    "f5·f11·f19·f26·f31·f35·f37·f41·f44: [의견] 문장마다 구축자 의견임을 밝힌다 — 출처 저자의 주장이 아니다.",
    "f36·f37(9절): 상위 업무 시스템 행은 예측 요청과 확정 요청의 인계 경계로만 쓰고, 전사 수요예측은 '연계 대상'으로 짧게 둔다. 158행의 '경계는 아직 정하지 않았으며'는 oq-223 열림 상태를 유지한 채 f37 의견으로만 보강한다.",
    "용어: 충전 상태는 용어집 표기 '충전 상태(State of Charge, SOC)'를 따르고, 지속형 MAPF 는 첫 등장 시 '지속형 다중 에이전트 경로 찾기(Lifelong MAPF)'로 풀어 쓴다.",
    "reference_updates: ref-199 기관을 'Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv)', 발행일을 2024-10-28 로, ref-1060 을 'ISO (ISO/TC 108/SC 5)', 발행 2025-09-02 로, ref-1061 에 Management Science 68(1):9–26(2022-01) 게재 서지를 보정한다. 재사용 출처의 각주 접근일은 2026-10-12 로 바꾼다.",
    "11절: oq-220~oq-224 는 해결로 바꾸지 않고 부분 근거만 연결한다. 분리 페이지 s11 의 질문 5개에는 해당 oq id 를 붙인다 — 답이 되는 finding 이 없다.",
    "인용: 페이지에서 출처 원문의 직접 인용은 출처당 1회 짧은 구절로 제한하고, ref-1062·ref-1640·ref-1639 처럼 여러 finding 의 근거 발췌가 인용문인 출처는 요약·재서술한다. Table III·Table 3 은 표를 복제하지 않고 필요한 값만 문장으로 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 44건, 미확인 0건, 교차 확인 0건. 강등: 없음(벤더 주장 f23·f24·f25·f40 과 해석 f7·f43 은 브리프 단계에서 이미 [추정]). 원문 미열람 출처: 없음. ref-1060 은 ISO 공식 목록 메타데이터만, ref-1061 은 Crossref 서지만 확인했고 ref-1643 은 PDF 대신 전문 페이지로 확인했다. 주의: 모든 [사실]이 단일 출처이거나 같은 연구팀·회사 자료(SILLM 논문·저장소, SILLM·SJRL·LSMART 공동 저자, Amazon 발표·블로그·기술보고서)라 신뢰도는 medium 이다. 학습 기반 경로·배정의 우열은 지도·밀도·계획 예산·실패 처리 조건에 따라 갈린다(SILLM 은 대형 지도 6종 중 3종에서 WPPL 보다 낮고, RL-RH-PP 는 80대에서 RH-PBS 보다 낮다). 실제 운영 현장에서 제3자가 측정한 근거는 여전히 없다. DeepFleet 10% 는 Amazon 자료끼리도 표현(미래형 이동 효율, 이동 시간, 배치 효율)이 엇갈리고 분모가 공개되지 않았다. aboutamazon 발표일은 페이지 본문에 표기가 없어(업계 매체는 2025-06-30) 페이지 메타 기준 2025-07-01 로 둔다. 브리프 참고: ref-916·ref-1054·ref-1060·ref-1063·ref-1644 는 fetched: true 인데 fetch_url 이 null 이다(검증에서 ref-916·ref-1054·ref-1060·ref-1644 는 직접 열어 확인했다). ref-1643 발행일 '2023-06'은 실제 2023-05-31 이다. LSMART 근거 발췌가 비교 대상에서 Guided PIBT 를 빠뜨렸다. 검증 검색 1회, 열람 약 30회. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-220~oq-224 부분 근거만).",
  "retry_reason": null
}
```

### runs/2026-10-12-06/pages.json

```json
{
  "run_id": "2026-10-12-06",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 700,
      "summary": "ISO 13381-1:2025는 ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행됐다. [사실][^ref-1060] rmf_battery의 SOC 변화 추정은 물리 모델이며, 학습·예측 값과 구분해 넘긴다는 것이 구축자 의견이다. [의견][^ref-1642]",
      "planned_findings": [
        "f33",
        "f34",
        "f35"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 4200,
      "summary": "물류창고 사례의 DeepFleet 10%는 Amazon 자료끼리도 표현이 엇갈리고 분모가 공개되지 않았다. [추정] 벤더 주장[^ref-916][^ref-1054] 병원 사례는 BIDMC 요청 이력 재생 시뮬레이션에서 95분위 대기 시간 개선이 가장 컸다. [사실][^ref-1062]",
      "planned_findings": [
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f32",
        "f38",
        "f39",
        "f40",
        "f41"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2400,
      "summary": "SILLM 비교에서는 지도에 따라, RL-RH-PP 비교에서는 로봇 밀도에 따라 학습 기반과 탐색 기반 방법의 우열이 갈렸다. [사실][^ref-199][^ref-1639] 대체 정책 호출과 예측 가중치 조정은 서로 다른 장치다. [사실][^ref-604][^ref-1062]",
      "planned_findings": [
        "f6",
        "f12",
        "f13",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f28",
        "f31",
        "f44"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1400,
      "summary": "POGEMA의 분포 밖 지표는 Cities-tiles 지도로 계산하고 통신은 분리되어 있지 않다. [사실][^ref-1056] LoRR 평가 구성은 고정 커밋 9d5e337 evaluation.md 기준이다. [사실][^ref-1637]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f9",
        "f10",
        "f33"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 2300,
      "summary": "SILLM의 16.0%는 대형 지도 6종 가운데 3종에서 WPPL보다 낮은 결과를 포함한다. [사실][^ref-199] 지도별 비율 평균으로 읽힌다는 해석은 추정이다. [추정][^ref-199]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f11",
        "f12",
        "f14",
        "f17",
        "f20",
        "f21",
        "f23",
        "f27",
        "f30",
        "f32",
        "f42"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 2200,
      "summary": "확정 요청은 fleet_name 같은 요청 필드로 인계하고 전사 수요예측은 연계 대상이다. [사실][^ref-125] 경계는 의견 수준이며 oq-223은 열려 있다. [의견][^ref-125][^ref-1062]",
      "planned_findings": [
        "f34",
        "f35",
        "f36",
        "f37",
        "f41"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 700,
      "summary": "20. 로봇·제조사 관제 연동, 27·54·25, 28, 63 영역과의 연결을 보강한다. [의견][^ref-1644][^ref-1637]",
      "planned_findings": [
        "f5",
        "f35",
        "f41"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "11. 열린 질문",
      "budget_chars": 1600,
      "summary": "oq-220~oq-224는 해결하지 않고 부분 근거만 연결하며 새 질문 세 건을 더한다. [추정][^ref-199][^ref-1062]",
      "planned_findings": [
        "f31",
        "f35",
        "f43",
        "f44"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 4절 예측 출력 종류 소절 추가(ISO 13381-1 서지, SOC 물리 모델 구분), 5절 물류창고 10% 표현 정정·DeepFleet 평가 조건·CDE, 병원 BIDMC 평가 조건·대기 시간 수치, 제조 공장 국내 시뮬레이션 연구 사례 추가, 기타 91% 표본 수, 6·7·8절 갱신 소절 추가(SILLM 지도별 우열·훈련 비용, RL-RH-PP, SJRL, LSMART 대체 정책, PUSH 대조, POGEMA·LoRR·SILLM 구현·ISO 행, Garces·SPO 정정), 9절 확정 요청 인계·SOC·오르카 경계, 10절 연결 4건, 11절 oq id 부여·부분 근거·새 질문 3건, 13절 각주 갱신(신규 8건). 2차: 4·6·7·8·10절 갱신 소절 앞에 2026-09-30 분리 페이지 링크 줄 추가, 6절 우열 문장을 두 연구로 한정, SOC·Lifelong MAPF 첫 등장 풀이, last_run 2026-10-12",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "last_run": "2026-10-12",
            "related_areas": [
              20,
              23,
              25,
              26,
              27,
              28,
              35,
              38,
              44,
              47,
              54,
              57,
              61,
              62,
              63,
              67
            ],
            "sources": [
              "ref-1053",
              "ref-1054",
              "ref-916",
              "ref-199",
              "ref-1056",
              "ref-623",
              "ref-1057",
              "ref-1058",
              "ref-1059",
              "ref-1060",
              "ref-1061",
              "ref-1062",
              "ref-1063",
              "ref-1064",
              "ref-125",
              "ref-604",
              "ref-1637",
              "ref-1638",
              "ref-1639",
              "ref-1640",
              "ref-1641",
              "ref-1642",
              "ref-1643",
              "ref-1644"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"8. 대표 연구와 자료\" 절(2,207자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"6. 대표 접근법과 기술\" 절(2,118자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,696자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"11. 열린 질문\" 절(1,664자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(684자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area46-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"4. 핵심 개념과 용어\" 절(677자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 46. 예측·학습 기반 최적화 | 차등 갱신: DeepFleet 10% 표현 정정(미래형·이동 시간·배치 효율, 벤더 주장), 병원 사례 BIDMC 평가 조건·대기 시간 수치, 국내 제조 물류 시뮬레이션 연구, SILLM 지도별 우열·훈련 비용, RL-RH-PP·SJRL·LSMART·PUSH 조건, LoRR 2026 요약, ISO 13381-1·SPO 서지 보정, 확정 요청·SOC·오르카 경계, oq-220~oq-224 부분 근거와 새 질문 3건 | run 2026-10-12-06",
  "index_updates": {
    "home_recent": "2026-10-12 — 46. 예측·학습 기반 최적화: SILLM·RL-RH-PP 비교에서 학습 기반 경로 방법의 우열이 지도·로봇 밀도에 따라 갈린 결과와 LSMART·PUSH의 실패 처리 조건을 보강하고, DeepFleet 10% 서술을 Amazon 자료의 실제 표현으로 정정했다",
    "category_recent": "2026-10-12 — 46. 예측·학습 기반 최적화: 5절 사례 정정·보강(DeepFleet 10% 표현, BIDMC 병동 시뮬레이션 수치, 국내 제조 물류 시뮬레이션 연구), 6·7·8절 갱신 소절, 9절 확정 요청·SOC·오르카 경계, 11절 oq id·새 질문 3건",
    "area_recent": "2026-10-12 — 46. 예측·학습 기반 최적화: 차등 갱신(4·5·6·7·8·9·10·11·13절), 신규 출처 8건(ref-1637~ref-1644), 열린 질문 해결 없음·새 질문 3건"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1056",
      "org": "Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv)",
      "title": "POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding",
      "published": "2025-04",
      "url": "https://arxiv.org/abs/2407.14931",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "고전·학습·혼합 MAPF 방법 비교 벤치마크(arXiv v3). §4.2 분포 밖 평가용 Cities-tiles 지도와 §5 에이전트 간 통신 미분리 한계를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "LoRR 공식 웹 자료 저장소(고정 커밋 9d5e337, 커밋 날짜 미확인). evaluation.md(연도 표기 없음)의 평가 구성(7개 지도 12개 인스턴스, 50~10,000 에이전트, GPU·CPU 인스턴스)과 2026-09-02 최종 결과·2026-08-10 지연·2026-05-26 AAMAS Prize 공지를 담는다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "SILLM 논문(arXiv v2 2025-05-18, v1 2024-10-28). Table III 지도별 처리량·계획 시간과 부록 E(훈련 자원·지도당 12시간 미만)·F.1(WPPL 비교 조건)을 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "SILLM 공식 코드 저장소. README 는 Backward Dijkstra·정적·동적 안내 버전을 별도 브랜치로 관리한다고 설명하고, 1-GPU 예시 YAML 은 max_dagger_iterations 100 을 둔다. 코드 실행은 하지 않았다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "LSMART 프리프린트. §4.1 대체 정책 호출 비율 지표와 §4.4 여러 대체 정책 비교(조건에 따라 LRGW 또는 PIBT 최고, Guided PIBT 도 비교)를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "RL-RH-PP 를 제안한 JAIR 게재 논문(arXiv 2603.23838). 16개 보류 환경·800단계·단계당 CPU 1초 조건의 Amazon·Symbotic 모사 지도 비교와 밀도별 훈련 비용을 담는다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "학습 없는 지속형 MAPF 알고리즘 PUSH 프리프린트. 1,000단계·단계당 1초·5회 평균 조건과 알고리즘별 시간 초과 처리(RHCR 의 PIBT 대체)를 적는다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "회전을 포함한 지속형 MAPF 의 SJRL 프리프린트. 지도별 학습·32~320대 평가와 실물 8대+가상 248대 혼합 현실 검증을 보고한다. SILLM 과 공동 저자.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "Amazon Robotics 의 다중 로봇 기반 모델 보고서(arXiv v3 2026-04-13). arXiv 표기상 'Unpublished technical report, Amazon Robotics' 로 동료 심사 없는 회사 자체 보고서다. 7개 층·7일 보류 자료의 60초 궤적 예측 평가와 Table 2 CDE 를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "Amazon 공식 발표(발행일은 페이지 메타 기준 2025-07-01, 본문에는 날짜 표기 없음, 업계 매체는 2025-06-30 으로 적음). DeepFleet 10% 를 요약은 '이동 효율을 높일 것', 본문은 '이동 시간 10% 개선/감소'로 적는다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "병원 이기종 로봇 배정의 예측 인지형 모델 기반 강화학습 프리프린트. BIDMC 4개 층 168 층-일 요청 이력 재생 시뮬레이션, 확정 요청 가중치 1, Table 3 거절 건수, 대기 시간 개선 수치를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "기계 상태 감시·진단의 예지 일반 지침 제3판. 공식 목록·공개 메타데이터로 발행 2025-09-02·23쪽·ISO/TC 108/SC 5 소관을 확인했고 규범 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "Open-RMF 배터리 추정 라이브러리 README. 이동 궤적의 가감속 에너지(SimpleMotionPowerSink)와 장치 소비 전력(SimpleDevicePowerSink)으로 SOC 변화를 추정하는 물리 모델 API 를 설명한다(학습 모델 아님).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "Open-RMF 작업 요청 JSON 스키마. fleet_name 이 문자열 또는 문자열 배열을 받고 지정한 플릿만 입찰한다(rmf_api_msgs 0.7.0, CHANGELOG 2026-09-18).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "CJ대한통운 뉴스룸 게시물. 이플렉스가 주문 유형별 수요를 예측해 센터 인력 운영에 쓴다고 설명한다(상위 업무 시스템 쪽 수요예측의 예).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1643",
      "org": "강민교, 김인철 (한국로봇학회 논문지 18(2))",
      "title": "다중 로봇 제조 물류 작업을 위한 안전성과 효율성 학습 (Safety and Efficiency Learning for Multi-Robot Manufacturing Logistics Tasks)",
      "published": "2023-05-31",
      "url": "https://doi.org/10.7746/jkros.2023.18.2.225",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "심층 관계형 강화학습으로 제조 물류 작업의 안전성·효율성 등급을 예측해 로봇에 배정하는 국내 연구(pp.225–232). Isaac 시뮬레이터 안 이동 로봇 2대로 실험한 시뮬레이션 연구이며 실물 검증은 향후 과제다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "현대자동차그룹 Story 기업 게시물. 현대글로비스·알티올의 WCS 플랫폼 오르카(설비 상태·우선순위에 따른 동선·작업 순서 실시간 조정, 어댑터 인터페이스)를 소개한다. 학습 모델·성과 분모는 밝히지 않는다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
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
      "summary": "결정 손실(SPO)·SPO+ 로 예측을 학습하는 틀. 학술지 게재본은 Management Science 68(1):9–26(2022-01, DOI 10.1287/mnsc.2020.3922)이며 Crossref 서지로 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "학습 기반 배정·경로 정책과 고전 탐색 방법을 같은 실행 모델·지도·계획 예산·실패 처리(대체 정책) 조건으로 다시 돌려 학습의 순이득을 재현한 공개 자료가 있는가? (관련 기존 질문: oq-220, oq-058)",
      "areas": [
        46,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "예측 요청의 가중치를 낮추는 것으로 충분한 경우와 실행 중인 계획을 중단·교체하거나 고전 정책으로 돌아가야 하는 경우를 누가 어떤 지표로 구분하는가? (관련 기존 질문: oq-222)",
      "areas": [
        46,
        47
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "배터리 SOC 변화 추정·현재 이상 클래스·고장 예지 출력을 플릿 일정에 넘길 때 값의 유효기간·불확실성·책임 주체를 어떻게 표현하는가? (관련 기존 질문: oq-221)",
      "areas": [
        46,
        28
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시",
      "title": "46. 예측·학습 기반 최적화"
    }
  ],
  "standards_updates": [
    {
      "name": "Scalable-Imitation-Learning-for-LMAPF (SILLM 저자 공식 구현)",
      "kind": "오픈소스",
      "org": "He Jiang (DiligentPanda, GitHub)",
      "url": "https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF",
      "related_areas": [
        46,
        27
      ],
      "summary": "확장형 모방 학습 기반 지속형 다중 에이전트 경로 찾기(SILLM)의 저자 공식 저장소. Backward Dijkstra·정적·동적 안내 버전을 별도 브랜치로 관리하며, 1-GPU 예시 설정은 논문 실험 설정(모방 학습 12회)과 다르다.",
      "ref_id": "ref-1638"
    }
  ],
  "additional_research_requests": [
    "11절 — 분리 주제 페이지 docs/topics/2026/2026-09-30-area46-s11.md 의 질문 5개에 oq-220~oq-224 id 를 붙이라는 지시(1차 required_fixes)는 그 페이지가 이번 입력에 없어 세부영역 페이지 11절에 id·부분 근거를 표기하는 것으로 이행했다. 분리 페이지 본문을 입력으로 넣어 다음 갱신에서 그 페이지에도 id 를 반영해야 한다.",
    "8절 — 분리 주제 페이지 docs/topics/2026/2026-09-30-area46-s8.md 의 기존 문장('최고 탐색 기반 기준선보다 16.0%', 'Garces 외 구체 수치는 초록에 없다', 'SPO 학술지 게재 연도 미확인')은 입력에 없어 세부영역 페이지 8절의 갱신 소절로 정정하고 기존 페이지 링크를 달았다. 다음 갱신에서 분리 페이지 s8·s6·s7·s4 자체에 같은 정정을 반영할 수 있도록 그 페이지들을 입력으로 넣어야 한다.",
    "대상 페이지 밖 후속 정리(예산·범위로 미룸): docs/categories/ai-and-learning/index.md 의 '로봇 이동 효율을 10% 높였다고 주장한다'를 이번 정정(미래형·이동 시간·배치 효율, 분모 미공개)으로, 같은 대분류 페이지의 Garces 요약에 대기 시간 수치를, docs/categories/site-type-applications/warehouse.md 의 Amazon 발표일 표기를 페이지 메타 기준 2025-07-01 로 고쳐야 한다.",
    "5·8절 — DeepFleet 구조 약어 RF·GF·IF 의 풀이와 각 구조의 정의, RH-PBS·WPPL·RHCR·LRGW 의 풀이가 브리프에 없어 약어만 썼다. 다음 조사에서 원문의 정의를 확인해야 한다.",
    "5절 물류창고 예외·성과 — DeepFleet 10% 의 비교 기간·대상 층·분모와 제3자 독립 측정 자료가 필요하다(벤더 주장을 사실로 올릴 근거).",
    "다음 실행 후보: 27. 다중 로봇 경로·교통 관리 — MAPF, 54. 시험·형식 검증·벤치마크, 25. 작업 배정 — MRTA 에 League of Robot Runners 2026 평가 구성·결과와 RL-RH-PP·SJRL·PUSH 를 주 위치로 반영하고, 수상팀 제출 코드의 학습 사용 여부를 확인해야 한다. 63. 병원·의료 에 Garces 외 평가 조건, 28. 공용 자원·충전·에너지 최적화 에 rmf_battery 를 반영할 것을 제안한다.",
    "5절 제조 공장 — 현대차 로봇팔 고장예측 5일·90%(ref-1059)의 1차 자료(회사 발표 원문)와 정확도 산정 방법을 확인해야 한다."
  ],
  "fixes_applied": [
    "f25(5절 물류창고 예외·성과 칸) — '아마존은 로봇 이동 효율을 10% 높였다고 주장하며' 문장을 발표 요약의 미래형, 본문의 이동 시간 10%, Amazon Science 블로그의 로봇 배치 효율 10%, 비교 기간·대상 현장·분모 미공개로 바꾸고 [추정] 벤더 주장[^ref-916][^ref-1054]로 표기했다.",
    "ref-916 — 각주 발행일을 2025-07-01 로 두고, 5절 본문의 발표일은 '2025-07-01, 페이지 메타 기준'으로 썼으며 reference_updates 요약에 본문 날짜 없음·업계 매체 2025-06-30 을 적었다.",
    "f23·f24(5·8절) — DeepFleet 오프라인 예측 평가와 CDE 3.40% 를 [추정] 벤더 주장[^ref-1053]으로 쓰고 Amazon Robotics 의 동료 심사 없는 기술보고서임을 5·8절에 밝혔으며, CDE 열 값(RC 3.40·RF 9.60·GF 14.22·IF 186.56)만 쓰고 DTW 값은 쓰지 않았다.",
    "f6(6·8절) — '8회 평균'을 빼고 지도별 처리량 값과 단계당 계획 시간 0.349초·4.143초만 썼다.",
    "f7(8절) — 16.0% 를 지도별 처리량 비율 평균으로 읽는 해석을 [추정]으로 두고, 같은 문장에 논문이 계산 방식을 밝히지 않았음을 적었다.",
    "f3·f4(7절 League of Robot Runners 행) — 평가 구성을 'web_resource 고정 커밋 9d5e337 의 evaluation.md 기준(연도 표기 없음)'으로 밝히고, 요약과 27. 다중 로봇 경로·교통 관리 — MAPF·54. 시험·형식 검증·벤치마크·25. 작업 배정 — MRTA 로의 연결만 두었다(10절에도 연결).",
    "f16(6절 실패·복귀 처리 소절) — '여러 대체 정책 가운데 지도와 계획 창 조건에 따라 LRGW 또는 PIBT 가 가장 높은 처리량'으로 쓰고 비교 대상을 둘로 한정하지 않았다.",
    "f13(6절) — RL-RH-PP 가 80대에서 RH-PBS 보다 낮고 100·120대에서 높았다는 점을 수치와 함께 쓰고 단일 연구 안의 자체 비교임을 밝혔다.",
    "f20~f22(6·8절 SJRL) — SILLM 과 공동 저자(Jiang·Li 등)의 연구라 독립 재현이 아님과 물리 검증이 실물 8대·가상 248대 혼합 현실임을 두 절 모두에 적었다.",
    "PUSH·rmf_battery·오르카 — 세 가지를 학습 성과 근거로 쓰지 않고 대조·경계 설명으로만 두었으며, 각각 27. 다중 로봇 경로·교통 관리 — MAPF, 28. 공용 자원·충전·에너지 최적화, 20. 로봇·제조사 관제 연동·61. 물류창고 로 연결했고 오르카 문장은 [추정] 벤더 주장[^ref-1644]로 썼다.",
    "f38·f39(5절 제조 공장) — 강민교·김인철 연구를 'Isaac 시뮬레이터 안 이동 로봇 2대의 시뮬레이션 연구, 실제 배치 사례 아님'으로 사례 제목과 서술에 표시하고 각주 발행일을 2023-05-31 로 고쳤다.",
    "f27~f30(5절 병원, 8절 Garces 외) — BIDMC 를 두 절에서 Beth Israel Deaconess Medical Center 로 풀어 쓰고, 평가가 실물 로봇 배치가 아닌 요청 이력 재생 시뮬레이션임을 사례 제목·서술·8절 항목에 밝혔다.",
    "의견 문장(f5·f11·f19·f26·f31·f35·f37·f41·f44) — 모든 [의견] 문장을 '구축자 의견으로는'으로 시작해 출처 저자의 주장이 아님을 밝혔다.",
    "f36·f37(9절) — 상위 업무 시스템 행을 확정 요청의 인계 경계(fleet_name)로만 쓰고 전사 수요예측은 '연계 대상'으로 짧게 두었으며, '경계는 아직 정하지 않았으며' 문장과 oq-223 열림 상태를 유지한 채 f37 의견으로만 보강했다.",
    "용어 — 충전 상태를 용어집 표기 '충전 상태(State of Charge, SOC)'로 쓰고, 지속형 MAPF 를 6절 첫 등장에서 '지속형 다중 에이전트 경로 찾기(Lifelong Multi-Agent Path Finding, Lifelong MAPF)'로 풀어 썼다.",
    "reference_updates — ref-199 기관·발행일(2024-10-28), ref-1060 기관(ISO/TC 108/SC 5)·발행일(2025-09-02), ref-1061 의 Management Science 68(1):9–26(2022-01) 서지를 보정했고, 재사용 출처의 각주 접근일을 2026-10-12 로 바꿨다.",
    "11절 — oq-220~oq-224 를 해결로 바꾸지 않고 id 와 부분 근거만 연결했다. 분리 페이지 s11 은 입력에 없어 세부영역 페이지 11절에 id 를 표기했고, 분리 페이지 반영은 additional_research_requests 에 적었다.",
    "인용 — 페이지에 출처 원문의 직접 인용을 넣지 않고 ref-1062·ref-1640·ref-1639 등은 모두 요약·재서술했으며, Table III·Table 3 은 표로 복제하지 않고 필요한 값만 문장으로 썼다.",
    "2차: 기존 분리 페이지 링크 — 4·6·7·8·10절 append 패치 맨 앞에 2026-09-30-area46-s4·s6·s7·s8·s10 로 가는 링크 줄을 번호와 이름을 함께 쓴 기존 페이지 제목으로 넣었고, 7절 링크 줄에는 서두 '아래 세 가지'의 항목이 그 페이지에 있다고 밝혔으며, 8절 링크 줄에는 정정·보강 대상 기존 항목(SILLM·Garces 외·SPO)이 그 페이지에 있다고 적었다.",
    "2차: 6절 우열 문장 — '조건에 따라 갈리는 우열' 소절 첫 문장을 'SILLM 비교에서는 지도에 따라, RL-RH-PP 비교에서는 로봇 밀도에 따라 우열이 갈렸다 [사실][^ref-199][^ref-1639]'로 두 연구에 한정했다.",
    "2차: 용어 첫 등장 — 9절 표의 '충전 상태(SOC)'를 '충전 상태(State of Charge, SOC)'로, 10절 패치의 SOC 첫 등장을 '충전 상태(State of Charge, SOC)'로, 11절 oq-221 부분 근거의 SOC 첫 등장을 '물리 모델의 충전 상태(State of Charge, SOC) 변화 추정'으로, 8절 PUSH 항목의 '지속형 MAPF'를 '지속형 다중 에이전트 경로 찾기(Lifelong MAPF)'로 고쳤다.",
    "2차: last_run — 13절 패치 frontmatter 에 last_run: 2026-10-12 를 넣었다.",
    "분량 초과 자동 분리: 46. 예측·학습 기반 최적화 본문 15,643자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 7,359자"
  ]
}
```

### runs/2026-10-12-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md (9개 절)
- 분량 초과 자동 분리:
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area46-s8.md (2,207자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area46-s6.md (2,118자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area46-s7.md (1,696자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area46-s11.md (1,664자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-12-area46-s10.md (684자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-12-area46-s4.md (677자)
```

### runs/2026-10-12-06/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md

```markdown
---
title: "46. 예측·학습 기반 최적화"
type: area
category: "L. AI·학습 기술"
area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [결정 중심 학습, 예지 정비, 모방 학습, 지속형 MAPF, 학습 기반 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-12
sources: [ref-1053, ref-1054, ref-916, ref-199, ref-1056, ref-623, ref-1057, ref-1058, ref-1059, ref-1060, ref-1061, ref-1062, ref-1063, ref-1064, ref-125, ref-604, ref-1637, ref-1638, ref-1639, ref-1640, ref-1641, ref-1642, ref-1643, ref-1644]
last_run: 2026-10-12
version: 3
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

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area46-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 적용 사례는 물류창고·병원·제조 공장·기타(대학 캠퍼스) 네 현장 유형에서 확인했다. 근거의 성격(회사 자체 발표·보고서, 요청 이력 재생 시뮬레이션, 시뮬레이션 연구, 현장 시험)이 사례마다 다르므로 표와 서술에 함께 적는다.

**현장 유형:** 물류창고

**사례:** 물류창고(풀필먼트·분류 센터)에서 로봇 플릿의 혼잡을 예측해 작업 배정과 경로를 조정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(확인한 자료가 작업 발생 조건을 다루지 않는다) |
| 작업 대상 | 로봇의 위치·목표·상호작용 이동 데이터(정보) [사실][^ref-1053] |
| 수행 자원 | 풀필먼트·분류 센터의 이동 로봇 플릿과, 미래 교통 패턴·위치를 예측하는 DeepFleet 모델 [추정] 벤더 주장[^ref-1054] |
| 제약 | 혼잡·병목 구간. 예측한 혼잡을 피하도록 배정과 경로를 조정한다 [추정] 벤더 주장[^ref-1054] |
| 완료·인계 | 미확인 |
| 예외·성과 | Amazon 발표(2025-07-01, 페이지 메타 기준)는 요약에서 로봇 플릿의 이동 효율을 10% 높일 것이라고 미래형으로 쓰고, 본문에서는 로봇 이동 시간을 10% 개선·감소한다고 쓴다. Amazon Science 블로그(2025-08-11)는 로봇 배치 효율을 10% 높이고 있다고 쓴다. 두 자료 모두 Amazon 자료이고 비교 기간·대상 현장·분모를 공개하지 않았으며, 독립 측정은 확인하지 못했다 [추정] 벤더 주장[^ref-916][^ref-1054] |

아마존 연구진의 DeepFleet은 전 세계 아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 다중 로봇 기반 모델 모음이다(2025-08 공개, 2026-04 개정). [사실][^ref-1053] Amazon Robotics의 동료 심사 없는 기술보고서인 DeepFleet 보고서(arXiv v3, 2026-04-13)는 학습에서 제외한 7개 창고 층의 7일 자료에서 로봇 궤적을 60초 앞까지 반복 추론해 실제 궤적과 비교하는 오프라인 예측 평가를 보고한다. [추정] 벤더 주장[^ref-1053] 같은 보고서의 구조 비교에서 로봇 중심(Robot-Centric, RC) 모델의 혼잡 지연 오차(CDE)는 3.40%로 네 구조 가운데 가장 낮았고, 나머지 구조는 RF 9.60%, GF 14.22%, IF 186.56%였다. 이 값은 예측한 혼잡 지연과 실제의 상대 오차이며 이동 시간 절감률이 아니다. [추정] 벤더 주장[^ref-1053]

아마존은 이 모델을 현재 혼잡 예측으로 작업 배정과 경로를 조정하는 데 쓰고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 한다고 밝혔다(2025-08-11). [추정] 벤더 주장[^ref-1054] 이 사례에서 이 영역이 관여하는 곳은 혼잡이라는 제약을 미리 알아 배정·경로에 넣는 부분이다. [추정][^ref-1054] 구축자 의견으로는, 예측 정확도(궤적·혼잡 오차), 오프라인 결정 손실, 온라인 운영 개선은 서로 다른 승인 지표로 두고, 운영 개선 수치는 개입 시점과 비교 플릿을 확인한 뒤에만 성과로 반영하는 것이 맞다. [의견][^ref-1053][^ref-916]

같은 현장 유형의 다른 예로, 연계 대상: CJ대한통운은 2021-07-28 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다. [추정] 벤더 주장[^ref-1063] 이는 상위 업무 시스템 쪽의 수요 예측이며, 로봇 배정에 쓴 근거는 이 자료에 없다. [추정][^ref-1063]

국내에서는 현대글로비스가 알티올과 공동 개발한 창고제어시스템(Warehouse Control System, WCS) 플랫폼 오르카(ORCA)가 각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정하고 어댑터 인터페이스로 다른 제조사 설비를 같은 방식으로 연결한다고 설명했으나(2026-04-16), 학습 모델이나 고전 방법 대비 성과는 밝히지 않았다. [추정] 벤더 주장[^ref-1644] 구축자 의견으로는, 이 발표는 학습 기반 배정·경로의 운영 효과 근거가 아니라 [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)과 [61. 물류창고](../site-type-applications/warehouse.md) 쪽 통합 운영 사례로 보고, 이 영역에서는 학습 요소가 확인되지 않은 경계 사례로만 다루는 것이 맞다. [의견][^ref-1644]

**현장 유형:** 병원

**사례:** 병원 입원 병동의 간호 업무 요청을 이기종 로봇에 배정(요청 이력 재생 시뮬레이션)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 병동에서 간호 업무 요청이 들어오면 작업이 발생한다 [사실][^ref-1062]. 평가는 Beth Israel Deaconess Medical Center(BIDMC) 서관 입원 병동 4개 층(층당 병상 약 25~30)의 2024-06-24~2025-06-29 요청 이력에서 층마다 수요 높음·중간·낮음 주를 2주씩 골라 층당 42일, 정책당 168개 층-일을 하루 12시간(오전 6시~오후 6시) 시뮬레이션했고, 나머지 이력은 학습·검증에 썼다 [사실][^ref-1062] |
| 작업 대상 | 간호 업무 요청에 딸린 작업. 운반 품목 같은 구체 대상은 초록에 없어 미확인이다 [사실][^ref-1062] |
| 수행 자원 | 이기종 다중 로봇. 배치 전에 과거 요청 데이터로 로봇 구성(차량 소요대수)을 고른다 [사실][^ref-1062] |
| 제약 | 즉시 확정은 이미 들어온 요청에만 하고, 표본 추출한 미래 요청 시나리오는 평가에만 쓴다. 예측 신뢰도 가중치는 표본 추출한 미래 요청에만 적용되고, 이미 관측된 요청과 예약 요청은 항상 가중치 1을 받는다 [사실][^ref-1062] |
| 완료·인계 | 미확인 |
| 예외·성과 | 요청 분포가 바뀌면 최근 예측 오차로 예측 요청을 다시 가중하고 아직 시작하지 않은 배정만 다시 최적화한다. 수요 높음 조건(요청 36,948건)에서는 제안 방법과 탐욕 배정을 포함한 대부분 정책의 거절이 0건이었고 Token Passing 계열 두 정책만 28건을 거절해, 저자는 대기 시간으로 정책을 비교했다. 수요 높은 주에서 일별 평균 대기 시간의 중앙값은 약 5%, 일별 95분위 대기 시간의 중앙값은 약 10% 줄었고, 두 지표의 75분위와 최댓값은 기준선 대비 15% 넘게 줄었으며, 모든 수요 구간에서 가장 크고 일관된 개선은 95분위 대기 시간 지표에서 나왔다 [사실][^ref-1062] |

Garces 외(2026-08-21, 동료 심사 전 프리프린트)는 병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 모델 기반 강화학습 롤아웃을 평가했으며, 이 평가는 실물 로봇 배치가 아니라 요청 이력을 재생한 시뮬레이션이다. [사실][^ref-1062] 이 사례에서 이 영역은 시작 조건(요청)을 예측해 수행 자원 구성과 배정에 넣고, 분포 이동이 생기면 재최적화 범위를 좁히는 부분에 관여한다. [추정][^ref-1062]

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

**현장 유형:** 제조 공장

**사례:** 제조 물류 작업을 이동 로봇 2대에 배정하는 안전성·효율성 학습(Isaac 시뮬레이터 안 시뮬레이션 연구, 실제 배치 사례 아님)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(시뮬레이션 실험 설계 밖의 작업 발생 조건은 확인하지 못했다) |
| 작업 대상 | 제조 물류 작업의 화물. 실험 환경에는 화물과 이동 장애물을 배치했다 [사실][^ref-1643] |
| 수행 자원 | NVIDIA Isaac 시뮬레이터 안 가상 제조 물류 환경의 이동 로봇 2대와, 심층 관계형 강화학습으로 작업의 안전성·효율성 등급을 예측해 배정하는 정책 규칙 학습 모델 [사실][^ref-1643] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 두 로봇의 정책 파라미터 등급이 같아 안전성·효율성 등급이 모두 같게 예측되는 드문 상태에서는 어느 로봇에 작업을 배정할지 판정하기 어렵다고 저자가 적고, 더 많은 정책 파라미터와 규칙이 필요하다고 보았다 [사실][^ref-1643] |

강민교·김인철(한국로봇학회 논문지 18(2), 2023-05-31)의 이 연구는 Isaac 시뮬레이터 안 이동 로봇 2대로 수행한 시뮬레이션 연구이며, 실제 하드웨어 로봇을 포함한 제조 작업 환경 검증은 향후 연구로 남겼다. [사실][^ref-1643] 국내 학습 기반 배정 연구의 예로 11절 oq-224와 이어진다.

**현장 유형:** 기타

**사례:** 대학 캠퍼스(로비·푸드코트·복도)에서 청소 로봇의 이상 진동을 분류해 예지 정비 지도를 만듦

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관성 측정 장치(Inertial Measurement Unit, IMU) 진동 신호가 충돌·조립 풀림·구조 불균형 같은 이상 클래스로 분류된다 [사실][^ref-1057] |
| 작업 대상 | 증기 걸레 청소 로봇과 청소 구역(로비·푸드코트·복도) [사실][^ref-1057] |
| 수행 자원 | 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망과 정비 팀 [사실][^ref-1057] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 정비 팀이 분류 결과를 동시적 위치 추정·지도 작성(Simultaneous Localization and Mapping, SLAM) 지도에 겹친 예지 정비 지도로 위험 구역을 격리하고 심각도를 판단한다. 저자가 보고한 실시간 현장 시험 정확도 91%는 Snail 청소 로봇에서 모바일 앱의 요청 방식으로 모은 시험 표본 100개 기준이며, 클래스별 정확도는 88.7~93.5%였다 [사실][^ref-1057] |

Pookkuttath 외(Sensors, 2021-12-21)는 싱가포르 기술디자인대학(SUTD) 캠퍼스에서 이 방법을 현장 시험했다. [사실][^ref-1057] 이 사례에서 이 영역은 고장 징후를 공간 정보와 묶어 정비 판단에 넘기는 부분에 관여한다. [추정][^ref-1057]

상업 시설·가정·실외 현장의 학습·예측 적용 사례는 이번 조사에서 찾지 못했다. 현장 유형별 전체 현황은 [현장 유형 매트릭스](../../site-matrix.md)에 있다.

## 6. 대표 접근법과 기술

같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1056][^ref-199][^ref-1064]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area46-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 이 영역과 직접 관련된 것으로 확인한 표준·평가 프로그램은 아래 세 가지다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area46-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 수치는 모두 논문 저자가 보고한 단일 출처 값이며, 이번 조사에서 두 출처 이상으로 교차 확인한 수치는 없다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 대표 연구와 자료](../../topics/2026/2026-10-12-area46-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 작업 요청 이력을 모아 예측에 공급하고, 예측한 요청·혼잡을 배정과 로봇 구성에 반영한다 [추정][^ref-1062][^ref-1053]. 확정 요청의 인계 예로, Open-RMF 작업 요청 스키마의 fleet_name은 플릿 이름 하나 또는 이름 배열을 받고, 지정하면 그 플릿만 입찰한다(rmf_api_msgs 0.7.0, 2026-09-18 변경 기록 기준) [사실][^ref-125] | 연계 대상: 전사 주문 수요예측과 그에 따른 인력 배치(예: 이커머스 플랫폼의 주문 유형별 물량 예측) [추정] 벤더 주장[^ref-1063] |
| 로봇 자체 지능·제어 | 배터리 소모·고장 위험 예측 결과를 받아 배정·충전·정비 일정에 반영한다 [추정][^ref-1058][^ref-1057]. 구축자 의견으로는, 이 영역은 학습·예측으로 얻은 값(현재 이상 클래스, 고장까지 남은 시간 같은 예지 출력)만 다루고, 물리 모델로 충전 상태(State of Charge, SOC) 변화를 추정하는 Open-RMF rmf_battery 같은 도구의 값은 28. 공용 자원·충전·에너지 최적화 쪽 값으로 구분해 받는 것이 맞다 [의견][^ref-1642][^ref-1057][^ref-1060] | 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시 [추정][^ref-1057][^ref-1059] |

ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델 공급, 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스, 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시, 학습 정책의 즉시 확정 범위 제한으로 보인다. [추정][^ref-1053][^ref-1054][^ref-1062][^ref-1058][^ref-1056]

연계 대상: 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다. [추정][^ref-1057][^ref-1059][^ref-1063]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역의 수요 예측(작업 요청·물동량 예측)과 외부 연계로 둔 전사 수요예측의 경계는 아직 정하지 않았으며 11절 열린 질문(oq-223)에 올렸다. 구축자 의견으로는, 상위 업무 시스템은 주문 전망과 시간 범위를 계획에 쓰고, ROP는 실제로 들어온 요청을 플릿·능력·가장 이른 시작 시각 조건과 함께 받아 배정하는 것으로 책임을 나누며, 예측 요청을 확정 요청으로 자동 바꾸는 규칙은 별도 승인을 거치게 하는 것이 맞다. 이는 공통 표준으로 확인된 경계가 아니므로 oq-223은 열린 채로 둔다. [의견][^ref-125][^ref-1062][^ref-1063]

5절의 오르카 같은 창고제어시스템 통합 제어 발표는 학습 요소가 확인되지 않았으므로, 구축자 의견으로는 이 영역의 직접 범위가 아니라 [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) 쪽 경계 사례로 두는 것이 맞다. [의견][^ref-1644] 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1056][^ref-1057]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-10-12-area46-s10.md)에 있다.

## 11. 열린 질문

이 영역의 열린 질문 다섯 건(oq-220~oq-224)은 2026-09-30 실행에서 올렸고, 처음 올린 맥락은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](../../topics/2026/2026-09-30-area46-s11.md)에 있다. 이번 갱신에서는 어느 질문도 해결로 바꾸지 않고 부분 근거만 연결하며, 새 질문 세 건을 더했다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](../../topics/2026/2026-10-12-area46-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md) — 영역 심화: 섹션 3~11 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 프런트매터 related_areas·tags·sources·confidence 추가(2차 재실행: 이 페이지 본문 변경 없음) (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area46-s6.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "6. 대표 접근법과 기술" 절(1,868자)을 옮겼다. 2차: DeepFleet·34. 시뮬레이션·예측용 디지털 트윈 구분 문장의 태그를 [의견]에서 [추정]으로 되돌렸다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-30-area46-s8.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "8. 대표 연구와 자료" 절(1,712자)을 옮겼다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area46-s4.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "4. 핵심 개념과 용어" 절(1,029자)을 옮겼다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area46-s10.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(942자)을 옮겼다 (실행 2026-09-30-09)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1053]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-10-12
[^ref-1054]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-10-12
[^ref-916]: Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot, 2025-07-01, https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model, 접근일 2026-10-12
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-12
[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-10-12
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-10-12
[^ref-1058]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1059]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-09-30
[^ref-1060]: ISO (ISO/TC 108/SC 5), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025-09-02, https://www.iso.org/standard/88029.html, 접근일 2026-10-12
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08-21, https://arxiv.org/abs/2608.21554, 접근일 2026-10-12
[^ref-1063]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-10-12
[^ref-1064]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-12
[^ref-1642]: Open-RMF 유지관리자 (open-rmf, GitHub), rmf_battery — README, 미확인, https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md, 접근일 2026-10-12
[^ref-1643]: 강민교, 김인철 (한국로봇학회 논문지 18(2)), 다중 로봇 제조 물류 작업을 위한 안전성과 효율성 학습 (Safety and Efficiency Learning for Multi-Robot Manufacturing Logistics Tasks), 2023-05-31, https://doi.org/10.7746/jkros.2023.18.2.225, 접근일 2026-10-12
[^ref-1644]: 현대자동차그룹 (현대글로비스), 현대글로비스가 그리는 자동화를 넘어선 물류의 미래, 2026-04-16, https://www.hyundaimotorgroup.com/ko/story/hyundai-glovis-physical-ai-logistics, 접근일 2026-10-12
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

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s8.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 대표 연구와 자료"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1053, ref-1057, ref-1061, ref-1062, ref-1638, ref-1639, ref-1640, ref-1641, ref-199]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#8
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 대표 연구와 자료

# 46. 예측·학습 기반 최적화 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 수치는 모두 논문 저자가 보고한 단일 출처 값이며, 이번 조사에서 두 출처 이상으로 교차 확인한 수치는 없다.
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 수치는 모두 논문 저자가 보고한 단일 출처 값이며, 이번 조사에서 두 출처 이상으로 교차 확인한 수치는 없다.


아래에서 정정·보강하는 기존 항목(SILLM, Garces 외, Smart ‘Predict, then Optimize’ 등)의 본문은 [46. 예측·학습 기반 최적화 — 대표 연구와 자료](2026-09-30-area46-s8.md)에 있다.

### 2026-10-12 갱신: 조건·비용과 정정

이번 갱신은 기존 항목의 평균 수치에 지도별 예외·계획 시간·훈련 비용을 덧붙이고, 확인하지 못했던 수치와 서지를 정정한다.

- **Jiang 외, SILLM(ICRA 2025, arXiv 2024-10-28)** — 초록이 밝힌 최고 탐색 기반 기준선 대비 16.0% 처리량 개선은 모든 지도에서 앞섰다는 뜻이 아니다. 대형 지도·에이전트 10,000 조건의 6개 지도 가운데 Sortation(WPPL 44.28 대 SILLM 43.98)·Warehouse(42.83 대 42.24)·Random-1(54.38 대 53.74)에서는 WPPL이 높았고, SILLM은 Paris(31.00 대 23.74)·Berlin(30.52 대 20.35)·Random-2(44.37 대 37.30)에서 높았으며, 단계당 평균 계획 시간은 SILLM 0.349초, WPPL 4.143초였다. [사실][^ref-199] 논문은 16.0%의 계산 방식을 밝히지 않았으며, 지도별 처리량 비율(SILLM/WPPL)을 평균하면 약 16.05%로 일치해 지도별 비율의 평균으로 읽힌다. [추정][^ref-199] 공식 부록에 따르면 지도마다 모델 훈련에 12시간 미만이 걸렸고, 훈련 서버는 72 vCPU AMD EPYC 9754, RTX 4090D(24GB) 4장, 메모리 240GB였다. [사실][^ref-199] 구축자 의견으로는, 학습 기반 경로 방법의 평균 개선율을 인용할 때 지도별 우열, 단계당 계획 시간, 지도별 훈련 비용, 공개 구현의 브랜치·설정 파일을 함께 적고, 10,000 에이전트 시뮬레이션을 실물 플릿 규모로 읽지 않는 것이 맞다. [의견][^ref-199][^ref-1638]
- **Zheng 외, RL-RH-PP(JAIR 85, 2026-03-24)** — MIT·Symbotic 공동 연구로, 서로 다른 시드의 보류 평가 환경 16개 평균, 800단계 창고 시뮬레이션(Amazon 풀필먼트 모사·Symbotic 모사 지도)에서 기준선과 비교했다. [사실][^ref-1639] 에이전트 밀도마다 정책을 처음부터 따로 학습했고, 가장 긴 훈련(120대)은 RTX 6000 Ada GPU 한 장으로 약 4일 걸렸다. [사실][^ref-1639] 밀도별 우열은 6절에 적었다.
- **Jiang 외, SJRL(arXiv, 2026-08-06)** — 각 평가는 512단계이며, 일반화는 초기 상태·목표·에이전트 수에 대해 보고 지도 간 일반화는 다루지 않는다. SILLM과 공동 저자의 연구라 독립 재현이 아니며, 물리 검증은 실물 8대·가상 248대의 혼합 현실 창고 환경이다. [사실][^ref-1641]
- **Sanjay·Li, PUSH(arXiv, 2026-08-07, 고전 대조 자료)** — 학습 요소가 없는 지속형 다중 에이전트 경로 찾기(Lifelong MAPF) 알고리즘으로, AMD Threadripper 3990X·192GB 메모리 장비에서 비교 실험을 수행했다. [사실][^ref-1640] 예산·실패 처리 조건은 6절에 적었다.
- **Garces 외(arXiv, 2026-08-21)** — 기존 항목의 '구체 수치는 초록에 없다'는 본문 확인으로 정정한다. Beth Israel Deaconess Medical Center(BIDMC) 4개 층, 정책당 168개 층-일의 요청 이력 재생 시뮬레이션(실물 로봇 배치 아님)에서 수요 높은 주의 일별 평균 대기 시간 중앙값을 약 5%, 일별 95분위 대기 시간 중앙값을 약 10% 줄였다(조건은 5절 병원 사례). [사실][^ref-1062]
- **Elmachtoub·Grigas, Smart ‘Predict, then Optimize’** — 기존 항목의 '학술지 게재 연도 미확인'을 정정한다. Management Science 68권 1호 9–26쪽(2022-01)에 게재됐다. [사실][^ref-1061]
- **Pookkuttath 외(Sensors, 2021-12-21)** — 실시간 정확도 91%는 Snail 청소 로봇에서 요청 방식으로 모은 시험 표본 100개 기준이다. [사실][^ref-1057]
- **Agaskar 외, DeepFleet(arXiv v3)** — Amazon Robotics의 동료 심사 없는 기술보고서이며, 7개 층·7일 보류 자료의 60초 궤적 예측 평가와 로봇 중심 모델의 혼잡 지연 오차 3.40%는 5절에 적었다. [추정] 벤더 주장[^ref-1053]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1053]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-10-12
[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-10-12
[^ref-1061]: Elmachtoub, A. N., & Grigas, P. (arXiv; Management Science 68(1)), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-10-12
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08-21, https://arxiv.org/abs/2608.21554, 접근일 2026-10-12
[^ref-1638]: He Jiang (DiligentPanda, GitHub) — SILLM 저자 공식 저장소, Deploying Ten Thousand Robots: Scalable Imitaion Learning for Lifelong Multi-Agent Path Finding — README·예시 설정(Scalable-Imitation-Learning-for-LMAPF), 미확인, https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF, 접근일 2026-10-12
[^ref-1639]: Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85), Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation, 2026-03-24, https://doi.org/10.1613/jair.1.20611, 접근일 2026-10-12
[^ref-1640]: Sanjay, V., & Li, J. (arXiv), Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF, 2026-08-07, https://arxiv.org/abs/2608.06702, 접근일 2026-10-12
[^ref-1641]: Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv), Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations, 2026-08-06, https://arxiv.org/abs/2608.05588, 접근일 2026-10-12
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s6.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 대표 접근법과 기술"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1056, ref-1062, ref-1064, ref-1639, ref-1640, ref-1641, ref-199, ref-604]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 대표 접근법과 기술

# 46. 예측·학습 기반 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1056][^ref-199][^ref-1064]
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1056][^ref-199][^ref-1064]


기존에 정리한 접근법과 기술은 [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](2026-09-30-area46-s6.md)에 있다. 아래는 이번 갱신에서 더한 내용이다.

### 2026-10-12 갱신: 조건에 따라 갈리는 우열

[지속형 다중 에이전트 경로 찾기(Lifelong Multi-Agent Path Finding, Lifelong MAPF)](../../glossary/lifelong-mapf.md)에서 학습 기반 방법과 탐색 기반 방법을 비교한 두 연구를 보면, SILLM 비교에서는 지도에 따라, RL-RH-PP 비교에서는 로봇 밀도에 따라 우열이 갈렸다. [사실][^ref-199][^ref-1639]

- **SILLM(확장형 모방 학습)** — 대형 지도·에이전트 10,000 조건의 6개 지도 가운데 3개(Sortation·Warehouse·Random-1)에서 WPPL보다 처리량이 낮았고, 단계당 평균 계획 시간은 SILLM 0.349초, WPPL 4.143초였다(지도별 값은 8절). [사실][^ref-199]
- **RL-RH-PP(강화학습 안내 롤링 호라이즌 우선순위 계획)** — MIT·Symbotic 연구진의 이 방법(JAIR 85, 2026-03-24)은 Symbotic 모사 지도에서 80대일 때 RH-PBS보다 에이전트당 처리량이 낮았고(18.38 대 20.83), 100대(15.38 대 14.04)와 120대(11.31 대 1.76)에서는 높았다. 이는 단일 연구 안의 자체 비교다. [사실][^ref-1639]
- **SJRL(탐색 보조 에이전트–환경 공동 강화학습)** — 2026-08 프리프린트로, 지도마다 256대로 정책을 학습해 같은 지도에서 32~320대로 평가하며 지도 간 일반화는 다루지 않는다. SILLM과 공동 저자(Jiang·Li 등)의 연구라 독립 재현이 아니고, 물리 검증은 실물 로봇 8대와 가상 로봇 248대를 섞은 혼합 현실 창고 환경이다. [사실][^ref-1641] 저자는 비교한 모방학습 방법들을 회전 동작을 포함한 문제 모델(LMAPF-R2)에 맞게 고치는 일을 향후 과제로 남겨, 비교 방법들의 문제 모델이 같지 않다. [사실][^ref-1641]

### 실패·복귀 처리와 예측 가중치

- LSMART(Lifelong Scalable Multi-Agent Realistic Testbed, 2026-02 프리프린트)는 처리량과 함께, 계획 실패 때 대체(fail) 정책을 부른 횟수를 계획기 호출 횟수로 나눈 비율을 평가 지표로 쓴다. [사실][^ref-604] 여러 대체 정책 가운데 지도와 계획 창 조건에 따라 LRGW 또는 [PIBT(우선순위 상속·되돌림, Priority Inheritance with Backtracking)](../../glossary/priority-inheritance-with-backtracking.md)가 가장 높은 처리량을 냈고, 한 대체 정책이 모든 조건에서 최선은 아니었다. [사실][^ref-604]
- Garces 외는 예측 신뢰도 가중치를 표본 추출한 미래 요청에만 적용하고, 이미 관측된 요청과 예약 요청은 항상 가중치 1로 둔다. [사실][^ref-1062]
- 구축자 의견으로는, 분포 이동에 대응해 예측 가중치를 낮추는 장치와 계획 실패·시간 초과 때 고전 정책으로 돌아가는 트리거는 따로 설계·기록하고, 이미 시작한 작업과 아직 시작하지 않은 배정을 구분해 다루는 것이 맞다. 두 장치에 공통으로 쓸 분포 이동 감지 임계값의 근거는 찾지 못했다. [의견][^ref-1062][^ref-604]

### 고전 기준선의 조건(대조)

학습 요소가 없는 탐색 알고리즘 PUSH(Path Updates over Staggered Horizons, 2026-08 프리프린트)의 비교 실험은 1,000단계 실행, 단계당 1초 계획 예산, 무작위 5회 평균으로 이루어졌다. [사실][^ref-1640] 이 비교에서 RHCR을 뺀 알고리즘은 시간 초과 시 계획하지 못한 에이전트가 직전 단계 경로를 따르고, RHCR은 K단계마다 K초를 받되 시간 초과 시 K단계 동안 PIBT로 실행한 뒤 RHCR로 돌아간다. [사실][^ref-1640] RL-RH-PP 비교는 서로 다른 시드의 보류 평가 환경 16개 평균, 800단계 창고 시뮬레이션에서 모든 해법에 계획 단계당 CPU 1초를 주고 시간 초과 해에 같은 수리 기법을 적용했다. [사실][^ref-1639]

구축자 의견으로는, PUSH는 학습 성과의 근거가 아니라 학습 정책을 평가할 때 맞춰야 할 고전 기준선의 예산·실패 처리 조건을 보여 주는 대조 사례이며 주 위치는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)다. 학습과 고전 방법의 우열은 지도·밀도·계획 예산·실패 처리를 같게 맞춘 조건에서만 판단하고, 한 논문의 평균 개선율을 다른 논문의 수치와 섞어 순위를 만들지 않는 것이 맞다. [의견][^ref-1640][^ref-199][^ref-1639][^ref-604]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-10-12
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08-21, https://arxiv.org/abs/2608.21554, 접근일 2026-10-12
[^ref-1064]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30
[^ref-1639]: Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85), Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation, 2026-03-24, https://doi.org/10.1613/jair.1.20611, 접근일 2026-10-12
[^ref-1640]: Sanjay, V., & Li, J. (arXiv), Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF, 2026-08-07, https://arxiv.org/abs/2608.06702, 접근일 2026-10-12
[^ref-1641]: Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv), Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations, 2026-08-06, https://arxiv.org/abs/2608.05588, 접근일 2026-10-12
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-12
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s7.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1056, ref-1060, ref-1637, ref-1638, ref-199]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#7
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스

# 46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 이 영역과 직접 관련된 것으로 확인한 표준·평가 프로그램은 아래 세 가지다.
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 이 영역과 직접 관련된 것으로 확인한 표준·평가 프로그램은 아래 세 가지다.


위 서두의 '아래 세 가지'에 해당하는 기존 표준·평가 프로그램 세 항목은 [46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스](2026-09-30-area46-s7.md)에 있다. 아래 표는 그 항목의 보강과 이번 갱신의 새 항목이다.

### 2026-10-12 갱신 항목

표준 목록은 [표준·프레임워크](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| POGEMA | 평가 프로그램 | 분포 밖(Out-of-Distribution) 지표는 학습에 쓴 지도와 장애물 구조가 다른 Cities-tiles 지도 묶음(Cities 지도를 잘라 고친 것)으로 계산한다. 저자는 한계로 에이전트 간 통신이 현재 환경에서 분리되어 있지 않다고 밝혀, 통신 지연·손실을 따로 평가하는 구조가 아니다 [사실] | [^ref-1056] |
| League of Robot Runners | 평가 프로그램 | 공식 웹 자료 저장소(MAPF-Competition/web_resource) 고정 커밋 9d5e337의 evaluation.md 기준(그 문서에 연도 표기는 없다) 평가는 7개 지도의 12개 인스턴스이고, 인스턴스별 로봇 수는 50~10,000대이며, 평가 서버는 GPU 인스턴스(AMD EPYC 7R13 32 vCPU·128 GiB·Nvidia A10G)와 CPU 인스턴스(같은 CPU 32 vCPU·64 GiB)로 나뉜다. 2026 본선 최종 결과는 2026-09-02 공지로 발표됐고(2026-07-23 공지는 8월 7일 발표 예정이라 했고 2026-08-10 공지로 지연을 알렸다), Combined Track 1위는 Team No Man's Sky, 2026-05-26 AAMAS Prize(Combined Track)는 Team SmartPath로 별도 집계다. 수상 표에는 팀별 알고리즘(학습 사용 여부) 분류가 없다 [사실]. 대회 평가의 주 위치는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)·[54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)·[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)이며 이 영역에는 요약과 연결만 둔다 | [^ref-1637] |
| SILLM 공식 구현(DiligentPanda/Scalable-Imitation-Learning-for-LMAPF) | 오픈소스 | 저자 공식 저장소 README는 Backward Dijkstra·정적 안내(Static Guidance)·동적 안내(Dynamic Guidance) 버전을 별도 브랜치(static_guidance, dynamic_guidance)로 관리한다고 설명한다. 1-GPU 예시 설정 파일은 모방 학습 반복 횟수(max_dagger_iterations)를 100으로 두지만 논문은 모방 학습을 12회 반복했다고 적어, 공개 예시 설정과 논문 실험 설정은 같지 않다 [사실]. 코드를 실행해 재현하지는 않았다 | [^ref-1638][^ref-199] |
| ISO 13381-1:2025 | 표준 | 기계 시스템 상태 감시·진단의 예지 일반 지침과 요구사항. ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행, 23쪽이다. 규범 본문은 열지 않았다 [사실] | [^ref-1060] |

구축자 의견으로는, 팀별 최종 제출 코드에서 학습을 어디에 썼는지 확인하기 전에는 대회 순위를 학습 대 고전 방법의 승률로 바꾸지 않고, 인용할 때 시즌·트랙·인스턴스 구성·CPU/GPU 조건을 함께 적는 것이 맞다. [의견][^ref-1637]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-10-12
[^ref-1060]: ISO (ISO/TC 108/SC 5), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025-09-02, https://www.iso.org/standard/88029.html, 접근일 2026-10-12
[^ref-1637]: League of Robot Runners 조직위원회 (MAPF-Competition/web_resource, GitHub), League of Robot Runners 2026 — Evaluation Process(evaluation.md)·Updates(updates.md)·Competition Rules(rules.md), 미확인, https://github.com/MAPF-Competition/web_resource/tree/9d5e3378979561a55645cb737ca5e71bc91f020b, 접근일 2026-10-12
[^ref-1638]: He Jiang (DiligentPanda, GitHub) — SILLM 저자 공식 저장소, Deploying Ten Thousand Robots: Scalable Imitaion Learning for Lifelong Multi-Agent Path Finding — README·예시 설정(Scalable-Imitation-Learning-for-LMAPF), 미확인, https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF, 접근일 2026-10-12
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s11.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 열린 질문"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1062, ref-1639, ref-1641, ref-199, ref-916]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#11
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 열린 질문

# 46. 예측·학습 기반 최적화 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 열린 질문 다섯 건(oq-220~oq-224)은 2026-09-30 실행에서 올렸고, 처음 올린 맥락은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](2026-09-30-area46-s11.md)에 있다. 이번 갱신에서는 어느 질문도 해결로 바꾸지 않고 부분 근거만 연결하며, 새 질문 세 건을 더했다.
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 열린 질문 다섯 건(oq-220~oq-224)은 2026-09-30 실행에서 올렸고, 처음 올린 맥락은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](2026-09-30-area46-s11.md)에 있다. 이번 갱신에서는 어느 질문도 해결로 바꾸지 않고 부분 근거만 연결하며, 새 질문 세 건을 더했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

### 기존 질문과 부분 근거

- **oq-220** (상태: 열림) 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? — 부분 근거: 이번 조사에서도 그런 자료를 찾지 못했고, 확인한 근거는 시뮬레이션(SILLM·RL-RH-PP·Garces 외), 혼합 현실(SJRL 실물 8대와 가상 248대), 회사 자체 주장(DeepFleet 10%)으로 나뉜다. [추정][^ref-199][^ref-1639][^ref-1062][^ref-1641][^ref-916]
- **oq-221** (상태: 열림) 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? — 부분 근거: 4절에서 인계 값의 종류(물리 모델의 충전 상태(State of Charge, SOC) 변화 추정, 학습 이상 클래스, 예지 출력)를 구분했다. 공통 데이터 항목과 모델 소유권 합의는 확인하지 못했다.
- **oq-222** (상태: 열림) 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? — 부분 근거: 대체 정책 호출 비율 지표(LSMART), 예측 가중치 조정(Garces 외), 알고리즘별 시간 초과 처리(PUSH 비교)를 6절에 적었다. 공통 분포 이동 감지 임계값은 찾지 못했다.
- **oq-223** (상태: 열림) 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? — 부분 근거: 9절의 확정 요청 인계 예(fleet_name)와 구축자 의견. 공통 표준으로 확인된 경계는 없다.
- **oq-224** (상태: 열림) 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? — 부분 근거: 5절 제조 공장의 국내 시뮬레이션 연구(강민교·김인철). 현대글로비스 오르카 발표는 학습 요소가 확인되지 않아 근거로 쓰지 않았고, 국내 실물 현장의 대조 실측은 찾지 못했다.
- 관련: **oq-058** — SILLM의 지도별 우열, RL-RH-PP의 밀도별 우열, SJRL의 혼합 현실 검증을 확인했지만, 벤치마크 성과가 실제 처리량으로 이어지는지는 여전히 확인하지 못했다.

### 새 질문(2026-10-12, id는 열린 질문 목록에서 부여)

- 학습 기반 배정·경로 정책과 고전 탐색 방법을 같은 실행 모델·지도·계획 예산·실패 처리(대체 정책) 조건으로 다시 돌려 학습의 순이득을 재현한 공개 자료가 있는가? (관련 기존 질문: oq-220, oq-058)
- 예측 요청의 가중치를 낮추는 것으로 충분한 경우와 실행 중인 계획을 중단·교체하거나 고전 정책으로 돌아가야 하는 경우를 누가 어떤 지표로 구분하는가? (관련 기존 질문: oq-222)
- 배터리 SOC 변화 추정·현재 이상 클래스·고장 예지 출력을 플릿 일정에 넘길 때 값의 유효기간·불확실성·책임 주체를 어떻게 표현하는가? (관련 기존 질문: oq-221)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08-21, https://arxiv.org/abs/2608.21554, 접근일 2026-10-12
[^ref-1639]: Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85), Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation, 2026-03-24, https://doi.org/10.1613/jair.1.20611, 접근일 2026-10-12
[^ref-1641]: Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv), Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations, 2026-08-06, https://arxiv.org/abs/2608.05588, 접근일 2026-10-12
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10-28, https://arxiv.org/abs/2410.21415, 접근일 2026-10-12
[^ref-916]: Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot, 2025-07-01, https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s10.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1056, ref-1057, ref-1062, ref-1637, ref-1642, ref-1644, ref-623]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#10
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결

# 46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1056][^ref-1057]
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1056][^ref-1057]


기존 연결 목록은 [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](2026-09-30-area46-s10.md)에 있다. 아래는 이번 갱신에서 더한 연결이다.

### 2026-10-12 갱신

- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 구축자 의견으로는, 학습 요소가 확인되지 않은 창고제어시스템 통합 제어 발표(오르카)는 이 영역이 아니라 연동 쪽 경계 사례로 둔다. [의견][^ref-1644]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)·[54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)·[25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 구축자 의견으로는, League of Robot Runners 2026 평가 구성·결과의 주 위치가 이 영역들이며 이 페이지에는 요약과 연결만 둔다. [의견][^ref-1637]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 구축자 의견으로는, 물리 모델의 충전 상태(State of Charge, SOC) 변화 추정(rmf_battery)은 이 영역의 맥락이고 46. 예측·학습 기반 최적화는 학습·예측 값만 다룬다. [의견][^ref-1642]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 요청 이력을 재생한 시뮬레이션으로 평가한 예측 인지형 배정 연구(Garces 외)가 있다. [사실][^ref-1062]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-10-12
[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-10-12
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08-21, https://arxiv.org/abs/2608.21554, 접근일 2026-10-12
[^ref-1637]: League of Robot Runners 조직위원회 (MAPF-Competition/web_resource, GitHub), League of Robot Runners 2026 — Evaluation Process(evaluation.md)·Updates(updates.md)·Competition Rules(rules.md), 미확인, https://github.com/MAPF-Competition/web_resource/tree/9d5e3378979561a55645cb737ca5e71bc91f020b, 접근일 2026-10-12
[^ref-1642]: Open-RMF 유지관리자 (open-rmf, GitHub), rmf_battery — README, 미확인, https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md, 접근일 2026-10-12
[^ref-1644]: 현대자동차그룹 (현대글로비스), 현대글로비스가 그리는 자동화를 넘어선 물류의 미래, 2026-04-16, https://www.hyundaimotorgroup.com/ko/story/hyundai-glovis-physical-ai-logistics, 접근일 2026-10-12
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-12-06/pages/topics/2026/2026-10-12-area46-s4.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 핵심 개념과 용어"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [20, 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1057, ref-1060, ref-1642]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#4
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 핵심 개념과 용어

# 46. 예측·학습 기반 최적화 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래는 이 페이지에서 쓰는 주요 용어다.
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래는 이 페이지에서 쓰는 주요 용어다.


이 페이지에서 쓰는 주요 용어의 기존 목록은 [46. 예측·학습 기반 최적화 — 핵심 개념과 용어](2026-09-30-area46-s4.md)에 있다. 아래는 이번 갱신에서 더한 항목이다.

### 2026-10-12 갱신: 예측 출력의 종류

- **예지(Prognostics)와 [예지 정비](../../glossary/predictive-maintenance.md)** — 기계 시스템 상태 감시·진단의 예지 일반 지침인 ISO 13381-1:2025는 ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행됐고 23쪽이다(규범 본문은 유료라 열지 않았다). [사실][^ref-1060]
- **[충전 상태(State of Charge, SOC)](../../glossary/state-of-charge.md) 변화 추정** — Open-RMF rmf_battery의 SimpleMotionPowerSink는 로봇이 궤적을 따라 가감속하는 데 드는 에너지로, SimpleDevicePowerSink는 탑재 장치의 소비 전력으로 SOC 변화를 추정하는 물리 모델 API이며 학습 모델이 아니다. [사실][^ref-1642]
- **인계 값의 종류** — 구축자 의견으로는, 물리 모델의 SOC 변화 추정([28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) 맥락), 학습 모델이 내는 현재 이상 클래스(진동 분류), 고장까지 남은 시간 같은 예지 출력을 서로 다른 값으로 구분해 플릿 일정에 넘기고, 이 영역은 학습·예측으로 얻은 값만 다루는 것이 경계로 맞다. [의견][^ref-1642][^ref-1057][^ref-1060]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-10-12
[^ref-1060]: ISO (ISO/TC 108/SC 5), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025-09-02, https://www.iso.org/standard/88029.html, 접근일 2026-10-12
[^ref-1642]: Open-RMF 유지관리자 (open-rmf, GitHub), rmf_battery — README, 미확인, https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-06 | 46. 예측·학습 기반 최적화 의 "핵심 개념과 용어" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 14건 / 전체 1553건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [46] 에 걸린 6건 / 전체 415건)

```markdown
- oq-220 [열림] 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? (영역 46, 54)
- oq-221 [열림] 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? (영역 46, 38)
- oq-222 [열림] 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? (영역 46, 47)
- oq-223 [열림] 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? (영역 46, 23)
- oq-224 [열림] 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? (영역 46, 61)
- oq-323 [열림] 지속성 필터처럼 마지막 관측 뒤 시간에 따라 믿음을 낮추는 확률 모델을 문·승강기·충전기 같은 설비 상태의 허용 경과 시간 판단에 적용한 연구나 사례가 있는가? (영역 18, 46)
```

### runs/2026-10-12-06/verification2.json

```json
{
  "run_id": "2026-10-12-06",
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
    "overlaps": []
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "세부영역 페이지 9절은 4절이 분리된 뒤 '충전 상태'가 처음 나오는 자리인데 '충전 상태(SOC)'로만 써서, 용어집 표기 '충전 상태(State of Charge, SOC)'와 다르다. fixes_applied 는 4·9절에서 이행했다고 보고했지만 9절에는 반영되지 않았다",
      "분리 페이지 2026-10-12-area46-s10·s11 은 'SOC'를 풀어 쓰지 않았고, 2026-10-12-area46-s8 은 '지속형 MAPF'가 처음 나올 때(PUSH 항목) 용어집 표기 '지속형 다중 에이전트 경로 찾기(Lifelong MAPF)'로 풀어 쓰지 않았다"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "4·6·7·8·10절 append 패치(분리 페이지 docs/topics/2026/2026-10-12-area46-s4·s6·s7·s8·s10.md): 각 갱신 소절 앞에 기존 분리 페이지로 가는 링크 줄을 하나씩 넣는다. 대상은 ../../topics/2026/2026-09-30-area46-s4.md·-s6.md·-s7.md·-s8.md·-s10.md 이고, 링크 텍스트는 번호와 이름을 함께 쓴 기존 페이지 제목(예: '46. 예측·학습 기반 최적화 — 대표 연구와 자료')으로 한다. 7절에서는 서두 '아래 세 가지다'의 세 항목이 그 링크된 페이지에 있다는 것을 링크 줄에서 밝힌다. 이유: 자동 분리 뒤 세부영역 페이지가 2026-10-12 분리 페이지만 링크해서, 2026-09-30 실행에서 검증된 기존 본문(SILLM 16.0%, Garces 외, SPO 항목, 7절 기존 세 항목, 4절 용어 목록 등)으로 들어가는 길이 끊겼다(남은 길은 곧 밀려날 auto:area-recent 목록뿐이다). 그 결과 새 소절의 '기존 항목의 … 정정한다'(s8), '기존 항목의 보강'(s7), '아래 세 가지다'(s7), '아래는 이 페이지에서 쓰는 주요 용어다'(s4)가 독자에게 보이지 않는 내용을 가리킨다. 11절은 2026-09-30-area46-s11 링크를 남겨 이미 이렇게 처리했다.",
    "6절 append 패치(분리 페이지 2026-10-12-area46-s6 '조건에 따라 갈리는 우열' 소절 첫 문장): '학습 기반 지속형 다중 에이전트 경로 찾기 방법과 탐색 기반 방법의 우열은 지도와 로봇 밀도에 따라 갈린다. [사실]'을 두 연구로 범위를 좁힌 진술로 바꾼다(SILLM 비교에서는 지도에 따라, RL-RH-PP 비교에서는 로봇 밀도에 따라 우열이 갈렸다 [사실][^ref-199][^ref-1639]). 아니면 일반화 문장을 그대로 두고 태그를 [추정]으로 고친다. 이유: f6·f13 은 연구 한 편씩의 결과이고, 학습 기반·탐색 기반 방법 전체로 넓힌 일반화는 브리프에 [사실] finding 으로 없다(이에 가장 가까운 f43·f44 는 [추정]·[의견]). 세부영역 페이지 6절 요약 문장의 [추정] 태그와도 맞지 않는다.",
    "용어(9절 replace 패치·분리 페이지 s10·s11·s8): 세부영역 페이지 9절에서 '충전 상태'가 처음 나오는 곳을 '충전 상태(State of Charge, SOC)'로 쓴다. 분리 페이지 2026-10-12-area46-s10·s11 에서는 'SOC'가 처음 나올 때 같은 방식으로 풀어 쓴다. 2026-10-12-area46-s8 의 PUSH 항목에서 '지속형 MAPF'가 처음 나오는 곳은 '지속형 다중 에이전트 경로 찾기(Lifelong MAPF)'로 쓴다. 이유: 1차 용어 지시는 이행했다고 보고됐지만, 4절 분리 뒤 페이지마다 첫 등장 위치가 바뀌었다.",
    "13절 패치 frontmatter: 세부영역 페이지 프런트매터 last_run 을 2026-10-12 로 고친다. 이유: updated·version 은 이번 실행으로 바꿨는데 last_run 만 2026-09-30 으로 남아 있고, 이번 실행의 분리 페이지들은 last_run 2026-10-12 로 적혀 있다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 44건, 미확인 0건, 교차 확인 0건. 강등: 없음(벤더 주장 f23·f24·f25·f40 과 해석 f7·f43 은 브리프 단계에서 이미 [추정]). 원문 미열람 출처: 없음. ref-1060 은 ISO 공식 목록 메타데이터만, ref-1061 은 Crossref 서지만 확인했고, ref-1643 은 PDF 대신 전문 페이지로 확인했다. 주의: 모든 [사실]이 단일 출처이거나 같은 연구팀·회사 자료(SILLM 논문·저장소, SILLM·SJRL·LSMART 공동 저자, Amazon 발표·블로그·기술보고서)라 신뢰도는 medium 이다. SILLM 은 대형 지도 6종 가운데 3종에서 WPPL 보다 처리량이 낮았고, RL-RH-PP 는 80대에서 RH-PBS 보다 낮았다. 실제 운영 현장에서 제3자가 측정한 근거는 여전히 없다. DeepFleet 10% 는 Amazon 자료끼리도 표현(미래형 이동 효율, 이동 시간, 배치 효율)이 엇갈리고 분모가 공개되지 않았다. aboutamazon 발표일은 페이지 메타 기준 2025-07-01 이다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-220~oq-224 는 부분 근거만). / 2차 수정 후 재검증. 1차 수정 지시 18건은 모두 다뤄졌다. 다만 용어 지시는 9절·분리 페이지 일부에서 이행되지 않았고, 분리 페이지 s11 의 id 표기는 입력 부재로 세부영역 11절과 새 분리 페이지에 대신 반영하고 후속 요청으로 넘겼다. 드리프트 1건: 6절 분리 페이지의 '우열은 지도와 로봇 밀도에 따라 갈린다 [사실]'은 두 연구 결과를 일반화한 문장이다. 형식은 코드가 통과시켰지만, 자동 분리 뒤 세부영역 페이지에서 2026-09-30 분리 페이지(s4·s6·s7·s8·s10)로 가는 링크가 사라져 기존 검증 본문과 '기존 항목 정정' 문장의 대상이 보이지 않는다. 그 밖에 [분류원문] 보존, 섹션 순서 준수, 범위 경계 준수(PUSH·rmf_battery·오르카는 대조·경계 설명으로만, 전사 수요예측은 연계 대상), 직접 인용 없음, 벤더 주장 병기 유지를 확인했다. 참고(수정 지시 대상 아님): 세부영역 6절 요약 문장 '같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고'([추정], 기존 검증 문장)는 새 소절의 조건별 결과와 함께 읽어야 한다. RH-PBS·WPPL·RHCR·LRGW, DeepFleet 의 RF·GF·IF·CDE 영문 풀이는 브리프에 없어 약어로 남았다(DeepFleet 약어는 additional_research_requests 에 등록됨). ref-1061 각주의 기관 칸(학술지 쪽수 포함)이 reference_updates 의 org 와 조금 다르다. 2차 검증에서는 웹 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
