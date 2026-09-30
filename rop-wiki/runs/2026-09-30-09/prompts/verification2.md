(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-09
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
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

## 입력

### runs/2026-09-30-09/target.json

```json
{
  "run_id": "2026-09-30-09",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 118,
  "run_type": "area_deep_dive",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=46"
}
```

### runs/2026-09-30-09/research.json

```json
{
  "run_id": "2026-09-30-09",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 46,
    "area_name": "46. 예측·학습 기반 최적화",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 결정 중심 학습(예측 후 최적화), 예지 정비·예지(prognostics), 모방 학습, 안내 그래프 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·제조 공장·기타 현장의 학습·예측 적용 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 학습 기반 배정, 학습 기반 경로(MAPF), 학습과 탐색의 결합, 수요 예측의 배정 반영, 고장·배터리 예측 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 13381(예지), POGEMA 벤치마크 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]",
    "강화학습·모방학습·그래프 신경망 기반 다중 로봇 작업 배정 연구는 어떤 기준선 대비 어떤 개선을 보고하며, 실제 현장 검증이 있는가? (섹션 6·8 겨냥)",
    "학습 기반 다중 로봇 경로·교통(MAPF) 방법은 탐색 기반 방법과 비교해 어디서 앞서고 어디서 뒤지는가? (섹션 6·8 겨냥)",
    "작업 요청·물동량 같은 수요 예측을 배정·로봇 구성·인력 계획에 쓴 사례는 무엇이며 예측 오차와 분포 이동은 어떻게 다루는가? (섹션 5·6 겨냥)",
    "로봇 고장·배터리 상태 예측(예지 정비)을 계획·정비에 쓰는 연구·사례와 관련 표준은 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)",
    "예측 정확도가 아니라 결정 품질을 기준으로 예측 모델을 학습하는 개념(예측 후 최적화, 결정 중심 학습)은 무엇인가? (섹션 4·6 겨냥)",
    "예측·학습 기반 최적화에서 ROP가 직접 맡을 것과 로봇 제조사·상위 업무 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Amazon 연구진(Agaskar 외, arXiv 2508.08574, 2025-08 제출·2026-04 개정)의 DeepFleet 는 전 세계 아마존 창고에서 수십만 대 로봇의 위치·목표·상호작용 이동 데이터로 학습한 다중 로봇 기반 모델 모음으로, 로봇 중심(RC)·로봇–바닥(RF)·이미지–바닥(IF)·그래프–바닥(GF) 네 구조 가운데 비동기 상태 갱신과 국지 상호작용 구조를 쓰는 RC 와 GF 가 가장 유망하다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"foundation models designed to support coordination and planning for large-scale mobile robot fleets\". 네 구조(RC 자기회귀 결정 트랜스포머, RF 교차 주의, IF 합성곱, GF 시간 주의+그래프 신경망), RC·GF 가 데이터 규모에 따라 잘 확장된다고 서술(초록 기준).",
      "as_of": "2025-08",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Amazon Science 블로그는 DeepFleet 가 풀필먼트·분류 센터 로봇의 미래 교통 패턴과 위치를 예측해 현재는 혼잡 예측으로 작업 배정과 경로를 병목 회피 쪽으로 조정하는 데 쓰이고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 하며, 로봇 이동 효율을 10% 높였다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1106"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"predicting future traffic patterns for fleets of mobile robots\". 효율 10% 개선, 모델 크기 1,300만~8억 4,000만 파라미터, 로봇 100만 대 배치를 함께 서술. 독립 출처 확인 없음.",
      "as_of": "2025-08-11",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f3",
      "claim": "Skrynnik 외의 POGEMA 벤치마크(ICLR 2025)는 고전 MAPF 에서 탐색 기반 중앙 계획기 LaCAM 이 다른 모든 방법보다 뚜렷이 앞서고 학습형 전용 해법(DCC·SCRIMP)이 그 뒤를 따르며 순수 다중 에이전트 강화학습(MARL)은 크게 뒤처지고 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했으며, 지속형(lifelong) MAPF 에서는 탐색 기반 RHCR 가 확장성 지표를 뺀 모든 경우에 우월했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실험 결과 절: LaCAM \"notably outperforms all other approaches\"; MARL 은 분포 밖 인스턴스를 풀지 못하고 DCC 가 분포 밖에서 가장 좋음; LMAPF 에서 MARL 은 고전 MAPF 보다 경쟁력이 있음(v2 HTML 본문 기준).",
      "as_of": "2025-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Andreychuk 외의 MAPF-GPT(arXiv 2409.00134, AAAI 2025)는 전문가 MAPF 해의 대규모 데이터셋을 트랜스포머로 모방학습한 경로 찾기 기반 모델로, 추가 휴리스틱이나 에이전트 간 통신 없이 행동을 생성하며 기존 최고 학습형 MAPF 해법보다 뚜렷이 앞서고 학습 데이터에 없는 문제에서도 제로샷으로 동작한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1107"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"capable of generating actions without additional heuristics or communication\". 비교 대상은 학습형 해법이며, 데이터셋 크기·전문가 해법 이름은 초록에 없음.",
      "as_of": "2024-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Jiang 외의 SILLM(arXiv 2410.21415, ICRA 2025)은 모방학습에 통신 모듈·충돌 해소·전역 안내를 결합한 지속형 MAPF 방법으로, 최대 1만 대·대형 지도 6종에서 최고 학습 기반 기준선보다 처리량 137.7%, 최고 탐색 기반 기준선보다 16.0% 높았고 2023 League of Robot Runners 우승 해법을 앞섰으며 실물 로봇 10대와 가상 로봇 100대로 검증했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 학습 기반 방법의 빠른 추론과 탐색 기반 방법의 해 품질을 함께 얻는다고 서술. 처리량 +137.7%(학습 기반 대비)·+16.0%(탐색 기반 대비), 1만 에이전트, 실물 10대+가상 100대(초록 기준).",
      "as_of": "2024-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Zhang 외의 안내 그래프 최적화(Guidance Graph Optimization, IJCAI 2024)는 지속형 MAPF 알고리즘이 따르는 격자 간선 가중치를 배치 전에 오프라인으로 최적화하거나 가중치를 생성하는 갱신 모델을 학습하는 방식으로, 대표적인 지속형 MAPF 알고리즘 3종의 처리량을 벤치마크 지도 8종에서 높였고 갱신 모델은 93×91 지도·에이전트 3,000개까지 적용됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1118"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"automatically generate guidance for arbitrary lifelong MAPF algorithms and maps\". 두 방법(간선 가중치 직접 최적화, 갱신 모델 최적화), 온라인 경로 계획기는 그대로 두고 안내만 학습(초록 기준).",
      "as_of": "2024-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Agrawal·Bedi·Manocha 의 RTAW(ICRA 2023)는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 두고 로봇·작업 수와 무관한 전역 임베딩을 쓰는 주의 기반 정책을 PPO 로 학습해, 시뮬레이션 창고(로봇 최대 1,000대)에서 픽업 거리 최소화 탐욕 규칙·후회(regret) 기반 방법보다 총 이동 지연을 최대 14% 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-623"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"global embeddings that are independent of the number of robots/tasks\". 총 이동 지연 최대 14%(25~1,000초) 감소, 수백~수천 작업 시나리오, 시뮬레이션만(초록 기준).",
      "as_of": "2022-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Garces 외(arXiv 2608.21554, 2026-08)는 병원 입원 병동의 실제 간호 업무 요청 데이터를 써서, 작업이 요청으로 발생하는 이기종 다중 로봇 배정을 미래 요청 시나리오를 표본 추출해 평가하되 즉시 확정은 이미 들어온 요청에만 하는 예측 인지형 모델 기반 강화학습 롤아웃으로 풀었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"restricting immediate commitments to requests already observed\". 입력은 병원 입원 병동의 실제 간호 업무 요청(초록 기준).",
      "as_of": "2026-08",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f9",
      "claim": "같은 연구(Garces 외)는 최근 예측 오차에 따라 예측 요청의 가중치를 다시 매기고 아직 시작하지 않은 배정만 다시 최적화하는 방식으로 분포 이동에 대응했으며, 배치 전에 과거 요청 데이터로 이기종 로봇 구성(차량 소요대수)을 고르는 절차를 두었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 요약: 적응형 재가중(adaptive reweighting)과 미시작 작업 선택적 재최적화, 이력 데이터 기반 이기종 플릿 구성 선택 절차(초록 기준).",
      "as_of": "2026-08",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "같은 연구(Garces 외)는 반응형·토큰 패싱·예측 위치 선배치·근시적 탐욕 기준선과 비교해 거의 모든 요청을 처리하면서 대기 시간을 줄였고, 개선 폭은 꼬리 지연 지표에서 가장 컸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 요약: near-complete service coverage, 대기 시간 감소, tail-delay 지표에서 개선이 가장 큼. 구체 수치는 초록에 없음(초록 기준).",
      "as_of": "2026-08",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "Elmachtoub·Grigas 의 Smart \"Predict, then Optimize\"(SPO)는 일반 기계학습이 예측 오차만 줄이고 예측이 어떻게 쓰일지 고려하지 않는다고 보고, 예측이 만든 결정 손실(SPO 손실)과 그 볼록 대리 손실 SPO+ 로 최적화 문제의 목적·제약을 학습에 반영했으며, 최단 경로·포트폴리오 실험에서 모형이 잘못 지정된 경우 특히 표준 예측 후 최적화보다 크게 나았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1115"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"machine learning tools are intended to minimize prediction error and do not account for how the predictions will be used\". SPO+ 로 학습한 선형 모형이 비선형 정답에서도 랜덤 포레스트를 앞섰다고 서술(arXiv 초록 기준).",
      "as_of": "2017-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Poskart 외(Sensors, 2022-12)는 사내 물류·유연 생산 환경을 대상으로 MiR100 자율이동로봇의 미션별 배터리 소모를 회전 수·이동 거리·충전 상태(SoC)·SoC×거리 항을 쓰는 일반화 선형 모형으로 예측해 조정 결정계수 0.9629·0.9694 를 얻었고, 이 예측을 실행 전 미션 가능 여부 판단과 다른 로봇으로의 위임, 로봇 추가 필요 판단에 쓸 수 있다고 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1112"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: \"can be used to determine which missions to delegate to other robots in the fleet, or if more robots are needed\". 예측의 약 50% 가 실제 소모 ±0.1% 이내(PMC 본문 기준).",
      "as_of": "2022-12-15",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "Pookkuttath 외(Sensors, 2021-12)는 증기 걸레 청소 로봇의 관성 측정 장치(IMU) 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망으로 오프라인 92.2%, 싱가포르 기술디자인대학(SUTD) 캠퍼스 로비·푸드코트·복도의 실시간 현장 시험 91% 정확도를 보고했고, 분류 결과를 SLAM 지도에 겹친 예지 정비 지도로 정비 팀이 위험 구역을 격리하고 심각도를 판단하게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: 진동 클래스를 cartographer SLAM 이 만든 2차원 지도에 융합한 predictive maintenance map 을 생성. 40 Hz, 9개 특징, 현장 4곳(PMC 본문 기준).",
      "as_of": "2021-12-21",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "파이낸셜뉴스(2026-05-28)가 전한 현대자동차 발표에 따르면 현대차는 산업용 로봇팔의 모터 부하·진동·전류 신호를 학습한 AI 고장예측 시스템으로 고장 약 5일 전에 90% 이상 정확도로 이상을 감지하며, 국내 생산 현장에 먼저 적용한 뒤 해외 생산거점으로 넓혀 사후 대응에서 계획적 예측 정비로 바꾸려 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1113"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기사 속 회사 관계자 인용 \"고장 발생 5일 전에 90% 수준으로 이상을 예측\". 정확도 산정 방법·데이터 규모는 기사에 없음.",
      "as_of": "2026-05-28",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "ISO 13381-1 은 기계 상태 감시·진단의 예지(prognostics) 일반 지침으로, 개발자·공급자·사용자·제조사가 예지 개념을 공유하고 정확한 예지에 필요한 데이터·특성·절차를 정하게 하는 것을 목적으로 하며, 2025년 3판이 2015년 2판을 대체했고 같은 시리즈의 다른 부는 성능 추세, 사이클 기반 수명 사용, 잔여 유효 수명 모델 같은 예지 접근을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1114"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: 2025판은 3판으로 ISO 13381-1:2015 를 취소·대체. 목적·다른 부(13381-2~4)의 범위도 검색 요약에 나타난 범위만 옮김.",
      "as_of": "2025",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "연계 대상: CJ대한통운은 2021년 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex 가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1117"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: iFlex 가 수요 예측으로 창고 인력 운영을 최적화하고 시스템 연결 시간을 90% 줄였다고 서술. 예측 정확도 수치는 이 게시물에서 확인하지 못함.",
      "as_of": "2021-07-28",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "확인한 자료를 종합하면 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에 대해, 개선 근거는 대부분 시뮬레이션·벤치마크이고(f3~f7) 실제 운영 개선 수치는 벤더 주장에 머물며(f2·f14·f16), 학습 단독 정책은 탐색 기반 방법보다 뒤지거나 분포 밖에서 실패할 수 있어(f3), 탐색·최적화와 결합하거나(f5·f6) 결정 손실로 예측을 학습하거나(f11) 관측된 요청만 확정하고 예측 오차로 재가중하는(f8·f9) 설계에서 개선이 보고되는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1109",
        "ref-1107",
        "ref-199",
        "ref-1118",
        "ref-623",
        "ref-1106",
        "ref-1113",
        "ref-1117",
        "ref-1115",
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2~f11·f14·f16 의 종합. 독립 현장 측정으로 학습 정책의 운영 개선을 확인한 공개 자료는 이번 조사에서 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 대규모 플릿에서 혼잡을 미리 알아야 배정·경로를 조정할 수 있고(f1·f2), 요청이 시간에 따라 달라지고 분포가 바뀌며(f8·f9), 예측 정확도가 높아도 결정 품질이 따라오지 않을 수 있고(f11), 배터리 소모와 고장이 계획을 어긋나게 하기 때문이다(f12~f14).",
      "tag": "추정",
      "source_ids": [
        "ref-1105",
        "ref-1106",
        "ref-1116",
        "ref-1115",
        "ref-1112",
        "ref-1111",
        "ref-1113"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f8·f9·f11~f14 의 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 46. 예측·학습 기반 최적화에서 ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델에의 공급(f1·f8·f12), 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스(f2·f12), 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시(f3·f9), 학습 정책의 즉시 확정 범위 제한(f8)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1105",
        "ref-1106",
        "ref-1116",
        "ref-1112",
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f3·f8·f9·f12 의 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "연계 대상: 분류 원문 19장 기준으로 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시와 배터리 셀 관리(f13·f14)는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측(f16)은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1111",
        "ref-1113",
        "ref-1117"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f13·f14·f16 과 분류 원문 19장 경계(수요예측, 모터·관절 제어)의 대조.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "이 영역은 학습 기반 배정의 25. 작업 배정 — MRTA(f7·f8), 학습 기반 경로의 27. 다중 로봇 경로·교통 관리 — MAPF(f3~f6), 결정 중심 예측의 26. 작업 순서·스케줄링(f11), 배터리 예측의 28. 공용 자원·충전·에너지 최적화(f12), 고장 예측의 38. 모니터링·이상 탐지·원인 분석(f13·f14), 분포 이동 감시의 47. AI·학습·적응과 모델 운영(f9), 벤치마크의 54. 시험·형식 검증·벤치마크(f3), 기반 모델 흐름의 44. 로봇 기반 모델·언어 모델 계획(f1·f4), 로봇 구성 산정의 35. 처리능력·규모·배치 설계(f9·f12), 정비 기준의 57. 자산·소프트웨어 수명주기 관리(f15), 수요 정보의 23. 업무 시스템 연동(f16), 적용 현장인 61. 물류창고(f1·f2·f16)·62. 제조 공장(f14)·63. 병원·의료(f8~f10)·67. 기타 현장(f13)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-623",
        "ref-1116",
        "ref-1109",
        "ref-1107",
        "ref-199",
        "ref-1118",
        "ref-1115",
        "ref-1112",
        "ref-1111",
        "ref-1113",
        "ref-1105",
        "ref-1106",
        "ref-1114",
        "ref-1117"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f16 의 영역 대응. DeepFleet 의 미래 교통 예측은 현재 운영 결정에 쓰는 예측으로 보고 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 섞지 않음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1105",
      "org": "Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv)",
      "title": "DeepFleet: Multi-Agent Foundation Models for Mobile Robots",
      "published": "2025-08",
      "url": "https://arxiv.org/abs/2508.08574",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 네 가지 구조의 다중 로봇 기반 모델을 비교한 프리프린트(2026-04 개정). 초록 페이지를 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1106",
      "org": "Amazon Science",
      "title": "Amazon builds first foundation model for multirobot coordination",
      "published": "2025-08-11",
      "url": "https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "DeepFleet 의 용도(혼잡 예측으로 작업 배정·경로 조정)와 효율 10% 개선 주장을 소개하는 아마존 블로그 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1107",
      "org": "Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv, AAAI 2025)",
      "title": "MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2409.00134",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "전문가 해를 트랜스포머로 모방학습한 MAPF 기반 모델. 학습형 해법 대비 우위와 제로샷 동작을 보고(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-199",
      "org": "Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025)",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "모방학습과 탐색 기법을 결합한 지속형 MAPF 방법 SILLM. 1만 대 규모에서 학습·탐색 기반 기준선 대비 처리량 개선과 실물 로봇 검증을 보고(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1109",
      "org": "Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv)",
      "title": "POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding",
      "published": "2025-04",
      "url": "https://arxiv.org/abs/2407.14931",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고전·학습·혼합 MAPF 방법을 같은 조건에서 비교하는 벤치마크 플랫폼과 비교 결과. v2 HTML 본문의 실험 결과 절을 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2407.14931v2",
      "source_unopened": false
    },
    {
      "id": "ref-623",
      "org": "Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023)",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 다중 로봇 작업 배정을 주의 기반 강화학습 정책으로 풀어 탐욕·후회 기반 방법 대비 총 이동 지연 감소를 보고한 시뮬레이션 연구(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1111",
      "org": "Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors)",
      "title": "AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots",
      "published": "2021-12-21",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "청소 로봇의 IMU 진동 신호를 1D CNN 으로 분류해 예지 정비 지도를 만든 연구. 대학 캠퍼스 현장 시험 결과 포함(PMC 본문).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1112",
      "org": "Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors)",
      "title": "Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems",
      "published": "2022-12-15",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "MiR100 의 미션별 배터리 방전을 일반화 선형 모형으로 예측하고 미션 위임·로봇 추가 판단에 쓰는 방법을 제시(PMC 본문).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1113",
      "org": "파이낸셜뉴스",
      "title": "현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지",
      "published": "2026-05-28",
      "url": "https://www.fnnews.com/news/202605280925297568",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대차가 산업용 로봇팔 고장을 AI 로 약 5일 전에 예측하는 시스템을 도입·확대한다는 회사 발표를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1114",
      "org": "ISO (ISO/TC 108)",
      "title": "ISO 13381-1:2025 Condition monitoring and diagnostics of machine … — Prognostics — Part 1: General guidelines (제목 일부는 검색 결과 기준)",
      "published": "2025",
      "url": "https://www.iso.org/standard/88029.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 기계 상태 감시·진단의 예지 일반 지침 3판(2015년 2판 대체). ISO 페이지가 403 이라 검색 결과 요약으로만 확인했다.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1115",
      "org": "Elmachtoub, A. N., & Grigas, P. (arXiv, Management Science)",
      "title": "Smart \"Predict, then Optimize\"",
      "published": "2017-10",
      "url": "https://arxiv.org/abs/1710.08005",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "예측 모델을 예측 오차가 아닌 하류 최적화의 결정 손실(SPO, SPO+)로 학습하는 틀. 2020-11 개정, Management Science 2022 게재(게재 연도는 검색 결과 기준). 초록 페이지를 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1116",
      "org": "Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv)",
      "title": "Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.21554",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 배정과 분포 이동 대응, 이력 기반 플릿 구성을 다룬 프리프린트(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1117",
      "org": "CJ대한통운",
      "title": "'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 … (제목 일부만 확인)",
      "published": "2021-07-28",
      "url": "https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "iFlex 수요 예측·인력 배치, RPA, 화물선 도착 예측 등 CJ대한통운의 AI 적용을 소개한 자사 뉴스룸 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1118",
      "org": "Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024)",
      "title": "Guidance Graph Optimization for Lifelong Multi-Agent Path Finding",
      "published": "2024-02",
      "url": "https://arxiv.org/abs/2402.01446",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "지속형 MAPF 의 안내 그래프 간선 가중치를 배치 전에 최적화·생성해 처리량을 높이는 방법(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
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
      "rationale": "섹션 3: f18(왜 중요한가), f17(핵심 질문 답, 추정) / 섹션 4: 결정 중심 학습 f11, 예지·예지 정비 f13·f15, 모방 학습 f4·f5, 안내 그래프 f6 / 섹션 5: 물류창고 — f1·f2(DeepFleet, 예외·성과는 벤더 주장 병기)·f16(수행 자원: 인력 배치, 연계 대상·벤더 주장 병기), 병원 — f8(시작 조건: 간호 업무 요청)·f9(수행 자원: 이력 기반 플릿 구성)·f10(예외·성과), 제조 공장 — f14(현대차 로봇팔 고장 예측, 벤더 주장 병기), 기타 — f13(대학 캠퍼스 청소 로봇 예지 정비). 상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 학습 기반 배정 f7·f8·f9, 학습 기반 경로 f3~f6(학습 단독 대 탐색 결합 대비), 예측을 결정 기준으로 학습 f11, 배터리·고장 예측 f12~f14 / 섹션 7: POGEMA 벤치마크 f3, ISO 13381-1 f15(원문 미열람) / 섹션 8: f1·f3~f13 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67 / 섹션 11: open_questions_new 5건. 교차 규칙에 따라 25. 작업 배정 — MRTA 페이지에 f7·f8·f17, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f3~f6, 38. 모니터링·이상 탐지·원인 분석 페이지에 f13·f14 반영을 다음 실행 후보로 남긴다."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "결정 중심 학습",
      "term_en": "Decision-Focused Learning (Smart Predict-then-Optimize)",
      "definition": "예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다."
    },
    {
      "term_ko": "예지 정비",
      "term_en": "Predictive Maintenance",
      "definition": "설비·로봇의 상태 신호로 고장이나 성능 저하를 미리 예측해 고장 전에 정비 시점과 조치를 정하는 정비 방식이다."
    },
    {
      "term_ko": "모방 학습",
      "term_en": "Imitation Learning",
      "definition": "전문가(예: 탐색 기반 계획기)가 만든 해나 행동 기록을 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다."
    },
    {
      "term_ko": "안내 그래프",
      "term_en": "Guidance Graph",
      "definition": "지속형 다중 에이전트 경로 찾기에서 로봇이 지나는 격자 간선에 가중치를 매겨 교통 흐름을 유도하는 그래프로, 배치 전에 최적화하거나 학습된 모델로 생성한다."
    }
  ],
  "open_questions_new": [
    "학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f2 | 종류: 일반",
    "제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? | 관련 영역: 46. 예측·학습 기반 최적화, 38. 모니터링·이상 탐지·원인 분석 | 근거: f14 | 종류: 일반",
    "학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f9 | 종류: 일반",
    "46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? | 관련 영역: 46. 예측·학습 기반 최적화, 23. 업무 시스템 연동 | 근거: f16 | 종류: 일반",
    "국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 61. 물류창고 | 근거: f16 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 14,
    "cross_checked_count": 0,
    "unverified": [
      "f2 DeepFleet 효율 10% 개선: 아마존 자체 자료뿐이며 독립 출처로 교차 확인하지 못함",
      "f14 현대차 고장 5일 전·정확도 90% 이상: 회사 발표를 전한 기사 1건뿐, 정확도 산정 방법 미확인",
      "f15 ISO 13381-1:2025: ISO·SCC 페이지 403 으로 원문 미열람, 제목 끝부분과 범위는 검색 결과 요약 기준",
      "f4 MAPF-GPT 데이터셋 크기·전문가 해법·지속형 MAPF 결과는 초록에 없어 미확인(검색 요약의 지속형 MAPF 제로샷 서술은 넣지 않음)",
      "f3~f8·f11 은 초록(POGEMA 는 HTML 본문 결과 절) 기준이며 실험 세부 조건 미확인",
      "f16 CJ대한통운 이커머스 주문량 예측 정확도 88%: 검색 요약에만 있고 연 자사 게시물에서 확인하지 못해 넣지 않음",
      "Malus 외 다중 에이전트 강화학습 AMR 주문 배차(CIRP Annals 2020, 제조 공장): ScienceDirect 403 으로 넣지 않음",
      "ACM Computing Surveys 다중 로봇 작업 배정 체계적 문헌 고찰(2024): ACM 403 으로 넣지 않음",
      "상업 시설·가정·실외 현장의 학습·예측 적용 사례는 찾지 못함(보도 배달 로봇 수요 예측 검색 1회에서 적합한 1차 자료 없음)",
      "국내 학술지의 강화학습 기반 다중 로봇 배정·경로 논문은 검색 1회에서 찾지 못함"
    ],
    "scope_violations": [
      "f13·f14: 로봇 부품 수준 진동·전류 기반 고장 감지는 로봇 제조사·설비 정비 쪽 기법이므로 예측 결과를 정비 계획에 쓰는 근거로만 제안하고, 경계는 f20 에서 '연계 대상: '으로 구분함",
      "f16: 전사 주문 수요예측은 분류 원문 19장의 상위 업무 시스템 연계 대상이므로 claim 을 '연계 대상: '으로 시작함. 46번 정의의 '수요·고장 예측'과의 경계는 열린 질문으로 올림",
      "f1·f2: DeepFleet 의 미래 교통 예측은 운영 결정용 예측으로 다루며 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)이나 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 섞지 않음"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 14
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 14건/15(ref-1105~ref-1118, 예약 구간 안). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건). 원문 열람: 13건 webfetch 로 열었고 ISO 13381-1(ref-1114)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Pookkuttath 외(ref-1111)·Poskart 외(ref-1112)는 PMC 본문, POGEMA(ref-1109)는 HTML 본문 결과 절, 나머지는 초록 페이지다. 교차 확인 0건: 핵심 수치가 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더·회사 발표만 근거로 한 f2·f14·f16 은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에는 f17 로 답했고 결론은 '개선 근거는 주로 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장이며, 학습 단독보다 탐색·최적화와 결합하거나 결정 손실로 학습하는 설계에서 개선이 보고된다'는 추정이다. 현장 유형 사례는 물류창고(f1·f2·f16)·병원(f8~f10)·제조 공장(f14)·기타(f13, 대학 캠퍼스)이며 상업 시설·가정·실외는 찾지 못했다. 국내 자료는 파이낸셜뉴스(ref-1113)·CJ대한통운(ref-1117) 두 건이고 국내 학술·표준 자료는 찾지 못했다. L. AI·학습 기술 교차 규칙에 따라 학습 기반 배정은 25. 작업 배정 — MRTA, 경로는 27. 다중 로봇 경로·교통 관리 — MAPF, 고장 예측은 38. 모니터링·이상 탐지·원인 분석과 함께 연결하도록 제안했다. 용어집에 이미 있는 상태 기반 정비·현실 격차·지속형 MAPF·MRTA·충전 상태·배터리 건강 상태는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### runs/2026-09-30-09/verification.json

```json
{
  "run_id": "2026-09-30-09",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2508.08574 초록 열람. 저자 Agaskar 외(Amazon), v1 2025-08-12, v3 2026-04-13. 수십만 대 로봇 이동 데이터, RC·RF·IF·GF 네 구조, RC·GF 가 비동기 상태 갱신·국지 상호작용 구조로 가장 유망하다는 서술이 초록과 일치. 단일 출처(같은 회사의 블로그 ref-1106 은 독립 출처가 아님)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Amazon Science 블로그(2025-08-11, Joey Durham) 열람. 혼잡 예측으로 작업 배정·경로를 조정해 효율 10% 개선, 장기 목표로 로봇별 작업 배정·목표 위치 출력, 1,300만~8억 4,000만 파라미터, 100만 번째 로봇 배치가 본문과 일치. 벤더 주장이며 독립 확인 없음 — [추정]·'벤더 주장' 병기 유지."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2407.14931 초록 페이지(v3 2025-04-08, 'Published as a conference paper at ICLR 2025')와 v2 HTML 결과 절을 열람. LaCAM 우세, DCC·SCRIMP 가 가까이 뒤따름, MARL(QPLEX·VDN·QMIX)이 크게 뒤처짐, LMAPF 에서 RHCR 가 확장성 지표만 빼고 우월하다는 서술이 원문과 일치. 다만 '분포 밖 데이터셋에서 한 인스턴스도 풀지 못함'은 원문에서 MAMBA 에 대한 진술이므로 순수 MARL 전체로 일반화하면 안 된다 — 수정 지시."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2409.00134 초록 열람(v1 2024-08-29, v5 2025-04-08). 전문가 해 모방학습, 트랜스포머, 추가 휴리스틱·통신 없이 행동 생성, 학습형 해법 대비 우위, 제로샷 일반화가 일치. AAAI 2025 게재 표기는 열람한 페이지에서 확인하지 못함 — 수정 지시."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2410.21415 초록 열람(2024-10-28 제출, ICRA 2025 채택 표기). 대형 지도 6종·최대 1만 에이전트, 처리량 +137.7%(학습 기반 대비)·+16.0%(탐색 기반 대비), 2023 League of Robot Runners 우승 해법 능가, 실물 10대+가상 100대 검증이 모두 일치. 단일 출처 저자 보고 수치."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2402.01446 초록 열람(IJCAI 2024). 간선 가중치 직접 최적화와 갱신 모델 두 방법, 지속형 MAPF 알고리즘 3종·지도 8종 처리량 개선, 93×91 지도·에이전트 3,000개 확장이 일치."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2209.05738 초록 열람(ICRA 2023). MDP 정식화, 로봇·작업 수와 무관한 전역 임베딩, PPO 학습, 탐욕·후회 기반 기준선 대비 총 이동 지연 최대 14%(25~1,000초) 감소, 시뮬레이션 최대 1,000대가 일치. 시뮬레이션 한정."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2608.21554 초록 열람(2026-08-21 제출). 'real nursing-task requests from hospital inpatient floors', 'restricting immediate commitments to requests already observed', 예측 인지형 적응 롤아웃이 일치. 프리프린트(동료 심사 전)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 초록에 최근 예측 오차에 따른 예측 재가중, 미시작 작업 재최적화, 배치 전 이력 데이터 기반 이기종 플릿 구성 선택 절차가 있음."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 초록의 기준선 목록은 reactive, token-passing, prediction-positioning, myopic greedy 이고 거의 완전한 서비스·대기 시간 감소·꼬리 지연 지표 개선이 일치. 구체 수치는 초록에 없음."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 1710.08005 초록 열람(2017-10-22 제출, 2020-11-19 개정). SPO 손실·볼록 대리 손실 SPO+, 최단 경로·포트폴리오 실험, 모형 오지정 시 큰 개선, 선형 모형이 랜덤 포레스트를 앞섬이 일치. Management Science 2022 게재는 열람 페이지에서 확인하지 못함(브리프도 검색 결과 기준으로 표시)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC9786877 본문 열람(Sensors, 2022-12). MiR100, 회전 수·거리·SoC·SoC×거리, 조정 결정계수 0.9629·0.9694, 예측의 약 50% 가 ±0.1% 이내, 미션 위임·로봇 추가 판단 문장이 일치. site_type 이 null 이므로 5절 현장 사례로 쓰지 않는다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC8747287 본문 열람(Sensors, 2021-12-21). 자체 개발 증기 걸레 로봇(Snail), IMU 진동 5종 1D CNN, 오프라인 92.2%·실시간 91%, 40 Hz·9개 특징, SUTD 캠퍼스(로비·푸드코트·복도·실험실) 현장 시험, SLAM 지도와 융합한 예지 정비 지도가 일치. 현장 유형 '기타' 적절."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 파이낸셜뉴스 2026-05-28 기사 열람. 모터 부하·진동·전류 신호 학습, 고장 약 5일 전 90% 이상 정확도, 국내 생산 현장 적용 후 전 세계 생산거점으로 단계적 확대, 예측 정비 체계로의 전환이 일치(기사는 마키나락스와의 협력도 언급). 회사 발표를 전한 기사 1건 — [추정]·'벤더 주장' 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람: iso.org 페이지 403(검증에서도 재현). 검색 결과(ISO·SCC·EVS 목록)와 EVS 목록 페이지로 제목 'Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements', 3판·ISO 13381-1:2015 취소·대체, 목적(개념 공유, 필요한 데이터·특성·절차 결정)을 확인. 다만 '같은 시리즈의 다른 부가 성능 추세·사이클 기반 수명 사용·잔여 유효 수명 모델을 다룬다'는 부분은 이번 검색 결과와 EVS 페이지에서 확인되지 않음 — 삭제 지시. 원문 미열람이라 high 불가."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CJ대한통운 뉴스룸 게시물 열람. 제목 \"'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명\", 게시일 2021-07-28. iFlex 가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 운영을 효율화하고 연결 시간을 1/10 로 줄였다는 서술이 일치. 자사 게시물 — [추정]·'벤더 주장'·'연계 대상' 유지."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 근거 finding(f2~f11·f14·f16)이 모두 검증을 통과했고 f3 은 수정 지시를 반영한 문구 기준. '학습 단독 정책이 분포 밖에서 실패할 수 있다'의 근거는 f3 수정 후 MAMBA 사례로 한정해 서술한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. f1·f2·f8·f9·f11~f14 와 대응. [추정] 유지."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 분류 원문 19장의 ROP 직접 범위(요청·제약을 받아 실행, 상태·실패 확인)와 맞고 근거 finding 과 대응."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연계 대상 구분은 분류 원문 19장(수요예측·모터·관절 제어)과 맞다. 다만 '배터리 셀 관리'는 인용한 f13·f14 가 다루지 않는 내용이므로 빼거나 근거 finding 을 바로잡아야 함 — 수정 지시."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연결 영역의 번호·이름이 부록 A 와 일치(23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67). L. AI·학습 기술 교차 규칙(학습 기반 배정 → 25. 작업 배정 — MRTA, 장애 분석 → 38. 모니터링·이상 탐지·원인 분석)을 따랐고, 34. 시뮬레이션·예측용 디지털 트윈과의 구분을 지켰다."
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
      "f1·f4(DeepFleet·MAPF-GPT 기반 모델 흐름)는 같은 날 실행 2026-09-30-07 의 44. 로봇 기반 모델·언어 모델 계획 브리프와 주제가 이어진다. 출처는 겹치지 않으므로 중복이 아니라 10절 연결로만 다룬다."
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
    "f3: 본문에서 '순수 MARL 이 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했다'를 'MARL 방법(QPLEX·VDN·QMIX 등)은 크게 뒤처졌고, 그 가운데 MAMBA 는 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했다'로 좁혀 쓴다 — 원문은 분포 밖 전면 실패를 MAMBA 에 대해서만 적는다. [사실][^ref-1109] 유지.",
    "f15: '같은 시리즈의 다른 부는 성능 추세, 사이클 기반 수명 사용, 잔여 유효 수명 모델 같은 예지 접근을 다룬다' 부분은 본문에 넣지 않는다 — 검색 결과와 EVS 목록 페이지에서 확인되지 않았다. 나머지(3판, 2015년 2판 대체, 목적)는 [사실] 로 유지한다.",
    "ref-1114: 참고문헌·각주 제목을 'ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements' 로 고친다. 원문을 열지 못했으므로 각주 접근일 뒤에 ' (원문 미열람)' 을 붙이고 reference_updates 의 이 항목에 source_unopened: true 를 넣는다.",
    "ref-1117: 제목을 \"'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명\" 으로 고친다(게시일 2021-07-28 확인).",
    "f4: 본문·각주에 AAAI 2025 게재를 사실로 적지 않는다 — 열람한 arXiv 페이지에서 확인하지 못했다. 'arXiv 2409.00134(2024-08 제출, 2025-04 개정)' 로 적고, 학회 표기가 필요하면 '(AAAI 2025 게재는 미확인)' 을 붙인다.",
    "f11: Management Science 게재 연도(2022)는 열람한 페이지에서 확인되지 않았으므로 본문·각주에 적지 않거나 '(게재 연도 미확인)' 을 붙인다.",
    "f20: '배터리 셀 관리' 를 9절 연계 대상 문장에서 뺀다 — 인용한 f13·f14 가 다루지 않는 내용이고, 배터리 예측 근거인 f12 는 ROP 직접 범위(f19)에 쓰였다.",
    "f2·f14·f16: 본문에서 [추정] 뒤에 '벤더 주장' 을 반드시 병기하고, 효율 10%·5일 전 90% 이상 같은 수치를 [사실] 로 쓰지 않는다. f16 은 '연계 대상:' 으로 시작한 서술을 유지한다.",
    "5절 적용 사례: 현장 유형은 물류창고(f1·f2·f16)·병원(f8~f10)·제조 공장(f14)·기타(f13, 대학 캠퍼스)로 쓴다. f12 는 현장 유형이 null 이므로 사례가 아니라 6절 근거로만 쓴다. 상업 시설·가정·실외 사례는 찾지 못했다고 적는다. site_matrix_updates 는 이 네 현장 유형의 칸만 낸다.",
    "glossary_candidates '결정 중심 학습': term_en 을 'Decision-Focused Learning' 으로 두고 Smart Predict-then-Optimize(SPO) 는 정의 안에서 대표 방법으로 적는다 — SPO 는 결정 중심 학습의 한 방법이지 같은 말이 아니다.",
    "8절: 논문 수치(f5 의 +137.7%·+16.0%, f7 의 14%, f13 의 91%, f12 의 결정계수)는 '저자 보고' 로 쓰고, 교차 확인된 수치가 없다는 점을 드러낸다(모두 단일 출처)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 21건, 미확인 0건, 교차 확인 0건. 강등: 없음(f3·f15 는 문구를 좁혀 [사실] 유지, f20 은 근거 없는 '배터리 셀 관리' 삭제). 원문 미열람 출처: ref-1114(ISO 13381-1:2025, iso.org 403. 검색 결과와 EVS 목록 페이지로 제목·판·대체 관계만 확인). 주의: 학습 기반 배정·경로의 개선 수치는 모두 논문 저자 보고(시뮬레이션·벤치마크 중심)의 단일 출처다. 실제 운영 개선 수치(DeepFleet 효율 10%, 현대차 고장 5일 전 90% 이상, CJ대한통운 iFlex)는 벤더·회사 발표뿐이고 독립 측정은 찾지 못했다. POGEMA 의 분포 밖 전면 실패는 MAMBA 에만 해당한다. 병원 사례(Garces 외)는 동료 심사 전 프리프린트다. 상업 시설·가정·실외 사례는 없다. 검증 검색은 1회를 썼다(리서치 포함 18/30). 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-09/pages.json

```json
{
  "run_id": "2026-09-30-09",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "예측·학습 기반 최적화는 혼잡·요청 변화·배터리 소모·고장처럼 계획을 어긋나게 하는 요인을 미리 알아 배정·경로·정비 결정에 반영하려는 영역이다. [추정][^ref-1105][^ref-1116][^ref-1112] 개선 근거는 대부분 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장에 머문다. [추정][^ref-1109][^ref-1106]",
      "planned_findings": [
        "f18",
        "f17",
        "f3"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "결정 중심 학습, 모방 학습, 안내 그래프, 예지·예지 정비, 분포 이동, 충전 상태, 다중 로봇 작업 배정을 정리한다. [사실][^ref-1115][^ref-1107][^ref-1118][^ref-1114]",
      "planned_findings": [
        "f11",
        "f4",
        "f5",
        "f6",
        "f13",
        "f15",
        "f9",
        "f12",
        "f7"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1800,
      "summary": "물류창고(DeepFleet 혼잡 예측, CJ대한통운 iFlex 연계 대상)·병원(간호 업무 요청 예측 인지형 배정)·제조 공장(현대차 로봇팔 고장 예측)·기타(대학 캠퍼스 청소 로봇 예지 정비) 사례를 여섯 항목으로 정리하고, 상업 시설·가정·실외 사례는 찾지 못했다고 밝힌다.",
      "planned_findings": [
        "f1",
        "f2",
        "f16",
        "f8",
        "f9",
        "f10",
        "f14",
        "f13"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "학습 기반 배정, 학습 기반 경로·교통 관리(탐색 기반 대비), 대규모 플릿 기반 모델, 결정 품질로 예측 학습, 배터리·고장 예측 다섯 접근을 정리한다. 같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고 학습은 탐색과 결합할 때 개선이 보고된다. [추정][^ref-1109][^ref-199][^ref-1118]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f3",
        "f4",
        "f5",
        "f6",
        "f1",
        "f11",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 450,
      "summary": "POGEMA 벤치마크, ISO 13381-1:2025(원문 미열람), League of Robot Runners 세 가지를 표로 정리한다. [사실][^ref-1109][^ref-1114][^ref-199]",
      "planned_findings": [
        "f3",
        "f15",
        "f5"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "DeepFleet, POGEMA, MAPF-GPT, SILLM, 안내 그래프 최적화, RTAW, Garces 외, SPO, Poskart 외, Pookkuttath 외를 저자 보고 수치와 함께 목록으로 둔다. 교차 확인된 수치는 없다.",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f10",
        "f11",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 플릿 수준 이력 수집·예측 결과를 계획에 넣는 인터페이스·학습 정책 평가와 분포 이동 감시·즉시 확정 범위 제한을 맡고, 부품 수준 상태 감시와 전사 주문 수요예측은 연계 대상이다. [추정][^ref-1116][^ref-1111][^ref-1117]",
      "planned_findings": [
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "G. 계획·최적화의 배정·순서·경로·충전 영역, 38. 모니터링·이상 탐지·원인 분석, 47. AI·학습·적응과 모델 운영, 54. 시험·형식 검증·벤치마크, Q. 현장 유형별 적용의 네 현장 영역 등 15개 영역과 잇는다. [추정][^ref-623][^ref-1109][^ref-1111]",
      "planned_findings": [
        "f21"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "section": "11. 열린 질문",
      "budget_chars": 650,
      "summary": "독립 현장 측정, 이종 플릿 고장 데이터 공통 항목, 분포 이동 시 되돌림 기준, 수요 예측 경계, 국내 적용 사례의 다섯 질문을 새로 올린다.",
      "planned_findings": [
        "open_questions_new"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 프런트매터 related_areas·tags·sources·confidence 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"6. 대표 접근법과 기술\" 절(1,868자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"8. 대표 연구와 자료\" 절(1,712자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"4. 핵심 개념과 용어\" 절(1,029자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(942자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"11. 열린 질문\" 절(669자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"3. 왜 중요한가\" 절(613자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area46-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 46. 예측·학습 기반 최적화 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(463자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 46. 예측·학습 기반 최적화 | 영역 심화: 3~11절 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 1차 수정 지시 11건 이행 | run 2026-09-30-09",
  "index_updates": {
    "home_recent": "2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 학습 기반 배정·경로(탐색 기반 대비), 결정 중심 학습, 배터리·고장 예측과 물류창고·병원·제조 공장·기타 현장 사례를 새로 정리했다",
    "category_recent": "2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 3~11절 신규 작성, 개선 근거는 주로 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장이라는 잠정 답을 정리했다",
    "area_recent": "2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 3~11절 신규 작성, 각주 14건, 열린 질문 5건 제기"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "decision-focused-learning",
      "term_ko": "결정 중심 학습",
      "term_en": "Decision-Focused Learning",
      "definition": "예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다. 대표 방법으로 Smart \"Predict, then Optimize\"(SPO)가 있다.",
      "description": "SPO 는 결정 손실(SPO 손실)과 그 볼록 대리 손실(SPO+)로 최적화 문제의 목적·제약을 학습에 반영한다. SPO 는 결정 중심 학습의 한 방법이며 같은 말이 아니다.",
      "related_areas": [
        46,
        26
      ],
      "sources": [
        "ref-1115"
      ]
    },
    {
      "action": "new",
      "slug": "predictive-maintenance",
      "term_ko": "예지 정비",
      "term_en": "Predictive Maintenance",
      "definition": "설비·로봇의 상태 신호로 고장이나 성능 저하를 미리 예측해 고장 전에 정비 시점과 조치를 정하는 정비 방식이다.",
      "description": "청소 로봇의 진동 분류 결과를 지도에 겹친 예지 정비 지도, 산업용 로봇팔의 신호 학습 기반 고장 예측(회사 발표) 같은 사례가 있다.",
      "related_areas": [
        46,
        38,
        57
      ],
      "sources": [
        "ref-1111",
        "ref-1113"
      ]
    },
    {
      "action": "new",
      "slug": "imitation-learning",
      "term_ko": "모방 학습",
      "term_en": "Imitation Learning",
      "definition": "전문가(예: 탐색 기반 계획기)가 만든 해나 행동 기록을 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다.",
      "description": "다중 에이전트 경로 찾기에서 전문가 해의 대규모 데이터셋을 트랜스포머로 모방학습한 연구와, 모방학습에 충돌 해소·전역 안내를 결합한 지속형 경로 찾기 연구가 있다.",
      "related_areas": [
        46,
        27
      ],
      "sources": [
        "ref-1107",
        "ref-199"
      ]
    },
    {
      "action": "new",
      "slug": "guidance-graph",
      "term_ko": "안내 그래프",
      "term_en": "Guidance Graph",
      "definition": "지속형 다중 에이전트 경로 찾기에서 로봇이 지나는 격자 간선에 가중치를 매겨 교통 흐름을 유도하는 그래프로, 배치 전에 최적화하거나 학습된 모델로 생성한다.",
      "related_areas": [
        46,
        27
      ],
      "sources": [
        "ref-1118"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1105",
      "org": "Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv)",
      "title": "DeepFleet: Multi-Agent Foundation Models for Mobile Robots",
      "published": "2025-08",
      "url": "https://arxiv.org/abs/2508.08574",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 네 가지 구조의 다중 로봇 기반 모델을 비교한 프리프린트(2026-04 개정). 초록 페이지를 열었다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1106",
      "org": "Amazon Science",
      "title": "Amazon builds first foundation model for multirobot coordination",
      "published": "2025-08-11",
      "url": "https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "DeepFleet 의 용도(혼잡 예측으로 작업 배정·경로 조정)와 효율 10% 개선 주장을 소개하는 아마존 블로그 글. 벤더 주장이며 독립 확인 없음.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1107",
      "org": "Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv)",
      "title": "MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2409.00134",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "전문가 해를 트랜스포머로 모방학습한 MAPF 기반 모델. 학습형 해법 대비 우위와 제로샷 동작을 보고(초록 기준, 2025-04 개정). 학회 게재(AAAI 2025)는 미확인.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-199",
      "org": "Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025)",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "모방학습과 탐색 기법을 결합한 지속형 MAPF 방법 SILLM. 1만 대 규모에서 학습·탐색 기반 기준선 대비 처리량 개선과 실물 로봇 검증을 보고(초록 기준).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1109",
      "org": "Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv)",
      "title": "POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding",
      "published": "2025-04",
      "url": "https://arxiv.org/abs/2407.14931",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고전·학습·혼합 MAPF 방법을 같은 조건에서 비교하는 벤치마크 플랫폼과 비교 결과. v2 HTML 본문의 실험 결과 절을 열었다. 분포 밖 전면 실패는 MAMBA 에 대한 진술이다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-623",
      "org": "Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023)",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 다중 로봇 작업 배정을 주의 기반 강화학습 정책으로 풀어 탐욕·후회 기반 방법 대비 총 이동 지연 감소를 보고한 시뮬레이션 연구(초록 기준).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1111",
      "org": "Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors)",
      "title": "AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots",
      "published": "2021-12-21",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "청소 로봇의 IMU 진동 신호를 1D CNN 으로 분류해 예지 정비 지도를 만든 연구. 대학 캠퍼스 현장 시험 결과 포함(PMC 본문).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1112",
      "org": "Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors)",
      "title": "Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems",
      "published": "2022-12-15",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "MiR100 의 미션별 배터리 방전을 일반화 선형 모형으로 예측하고 미션 위임·로봇 추가 판단에 쓰는 방법을 제시(PMC 본문).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1113",
      "org": "파이낸셜뉴스",
      "title": "현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지",
      "published": "2026-05-28",
      "url": "https://www.fnnews.com/news/202605280925297568",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대차가 산업용 로봇팔 고장을 AI 로 약 5일 전에 예측하는 시스템을 도입·확대한다는 회사 발표를 전한 기사. 정확도 산정 방법은 기사에 없다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1114",
      "org": "ISO (ISO/TC 108)",
      "title": "ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements",
      "published": "2025",
      "url": "https://www.iso.org/standard/88029.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 기계 상태 감시·진단의 예지 일반 지침 3판(2015년 2판 대체). ISO 페이지가 403 이라 검색 결과 요약과 EVS 목록 페이지로 제목·판·대체 관계와 목적만 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1115",
      "org": "Elmachtoub, A. N., & Grigas, P. (arXiv)",
      "title": "Smart \"Predict, then Optimize\"",
      "published": "2017-10",
      "url": "https://arxiv.org/abs/1710.08005",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "예측 모델을 예측 오차가 아닌 하류 최적화의 결정 손실(SPO, SPO+)로 학습하는 틀. 2020-11 개정. 학술지 게재 연도는 미확인. 초록 페이지를 열었다.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1116",
      "org": "Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv)",
      "title": "Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.21554",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 배정과 분포 이동 대응, 이력 기반 플릿 구성을 다룬 프리프린트(초록 기준, 동료 심사 전).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1117",
      "org": "CJ대한통운",
      "title": "'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명",
      "published": "2021-07-28",
      "url": "https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "iFlex 수요 예측·인력 배치, RPA, 화물선 도착 예측 등 CJ대한통운의 AI 적용을 소개한 자사 뉴스룸 글.",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1118",
      "org": "Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024)",
      "title": "Guidance Graph Optimization for Lifelong Multi-Agent Path Finding",
      "published": "2024-02",
      "url": "https://arxiv.org/abs/2402.01446",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "지속형 MAPF 의 안내 그래프 간선 가중치를 배치 전에 최적화·생성해 처리량을 높이는 방법(초록 기준).",
      "cited_by": [
        "docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가?",
      "areas": [
        46,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가?",
      "areas": [
        46,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가?",
      "areas": [
        46,
        47
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가?",
      "areas": [
        46,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가?",
      "areas": [
        46,
        61
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
      "name": "POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼)",
      "kind": "평가 프로그램",
      "org": "Skrynnik, A. 외 (ICLR 2025)",
      "url": "https://arxiv.org/abs/2407.14931",
      "related_areas": [
        27,
        46,
        54
      ],
      "summary": "고전·학습·혼합 MAPF 방법을 같은 조건에서 비교하는 벤치마크 플랫폼. 고전 MAPF 에서 LaCAM, 지속형 MAPF 에서 RHCR 가 앞서고 MARL 방법이 크게 뒤처진다는 비교 결과를 보고했다.",
      "ref_id": "ref-1109"
    },
    {
      "name": "ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항",
      "kind": "표준",
      "org": "ISO (ISO/TC 108)",
      "url": "https://www.iso.org/standard/88029.html",
      "related_areas": [
        38,
        46,
        57
      ],
      "summary": "원문 미열람. 기계 상태 감시·진단의 예지 일반 지침 3판(2015년 2판 대체). 이해관계자가 예지 개념을 공유하고 정확한 예지에 필요한 데이터·특성·절차를 정하게 하는 것이 목적이다.",
      "ref_id": "ref-1114"
    }
  ],
  "additional_research_requests": [
    "5절 적용 사례: 상업 시설·가정·실외 현장에서 학습·예측(수요·고장·배터리 예측, 학습 기반 배정·경로)을 로봇 운영에 적용한 1차 자료가 필요하다 — 이번 브리프에는 물류창고·병원·제조 공장·기타 사례만 있다.",
    "5절 적용 사례: 네 사례 모두 '완료·인계' 항목(무엇이 확인돼야 작업이 끝났다고 인정하는가)의 근거가 없고, 물류창고(DeepFleet)의 시작 조건과 제조 공장·기타 사례의 제약도 미확인이다. 해당 칸을 채울 자료가 필요하다.",
    "3·6·8절: 학습 기반 배정·경로 정책의 실제 운영 개선을 제3자가 측정한 공개 자료가 필요하다 — 현재 운영 수치(DeepFleet 효율 10%, 현대차 5일 전 90% 이상, iFlex)는 벤더·회사 발표뿐이고 교차 확인된 수치가 없다.",
    "7절: ISO 13381-1:2025 원문(또는 공식 요약) 열람과, 같은 시리즈 다른 부(13381-2 이후)의 범위 확인이 필요하다 — 이번 실행은 검색 결과·EVS 목록 페이지로만 확인했고 다른 부의 범위 서술은 수정 지시로 뺐다.",
    "8절: MAPF-GPT 의 학회 게재(AAAI 2025 여부)와 Smart \"Predict, then Optimize\" 의 학술지 게재 연도를 공식 페이지에서 확인해야 한다 — 이번 실행은 미확인으로 두었다.",
    "6·8절: 제조 공장의 다중 에이전트 강화학습 AMR 주문 배차(Malus 외, CIRP Annals 2020)와 다중 로봇 작업 배정 체계적 문헌 고찰(ACM Computing Surveys 2024)은 원문 접근 실패(403)로 넣지 못했다. 열람 가능한 판본으로 재확인이 필요하다.",
    "11절 관련: 국내 학술지·국내 현장의 학습 기반 다중 로봇 배정·경로 적용 사례와 국내 예지 정비 표준·지침 자료가 필요하다.",
    "교차 규칙에 따른 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 학습 기반 배정(RTAW, Garces 외)과 핵심 질문 잠정 답, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 POGEMA·MAPF-GPT·SILLM·안내 그래프 최적화, 38. 모니터링·이상 탐지·원인 분석 페이지에 청소 로봇 예지 정비·현대차 고장 예측 반영을 검토해야 한다(하루 갱신 예산 안에서)."
  ],
  "fixes_applied": [
    "f3 MARL 일반화 수정 — 6절 '학습 기반 경로·교통 관리'에서 'MARL 방법(QPLEX·VDN·QMIX 등)은 크게 뒤처졌고, 그 가운데 MAMBA 는 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했다'로 좁혀 [사실][^ref-1109]로 썼고, 3절 핵심 질문 답도 MAMBA 사례로 한정했다.",
    "f15 다른 부 범위 삭제 — 4절·7절의 ISO 13381-1 서술에서 '같은 시리즈의 다른 부가 성능 추세·사이클 기반 수명 사용·잔여 유효 수명 모델을 다룬다'는 부분을 넣지 않고 3판·2015년 2판 대체·목적만 [사실]로 썼다.",
    "ref-1114 제목·미열람 표시 — 13절 각주와 reference_updates·standards_updates 의 제목을 'ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements'로 고치고, 각주 접근일 뒤에 ' (원문 미열람)'을 붙였으며 reference_updates 항목에 source_unopened: true 를 넣고 summary 를 '원문 미열람. '으로 시작했다.",
    "ref-1117 제목 — 13절 각주와 reference_updates 의 제목을 \"'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명\"으로 고쳤다(게시일 2021-07-28).",
    "f4 AAAI 표기 — 6절·8절 본문에 'arXiv 2409.00134(2024-08 제출, 2025-04 개정)'로 적고, 각주·reference_updates 의 기관 표기에서 'AAAI 2025'를 뺐다(reference_updates summary 에는 'AAAI 2025 게재는 미확인'으로 적었다).",
    "f11 게재 연도 — 8절에 'arXiv 1710.08005, 2017-10 제출, 2020-11 개정, 학술지 게재 연도 미확인'으로 적고, 각주·reference_updates 기관 표기에서 Management Science 를 뺐으며 summary 를 '학술지 게재 연도는 미확인'으로 고쳤다.",
    "f20 배터리 셀 관리 삭제 — 9절 연계 대상 문장과 표에서 '배터리 셀 관리'를 빼고 로봇 부품 수준 상태 감시(모터 전류·진동·IMU)와 전사 주문 수요예측만 연계 대상으로 두었다. 배터리 예측(f12)은 ROP 직접 범위 쪽에만 썼다.",
    "f2·f14·f16 벤더 주장 병기 — 5절 표·서술과 9절 표에서 이 세 finding 을 쓴 모든 문장을 '[추정] 벤더 주장[^ref-…]'로 쓰고, 효율 10%·5일 전 90% 이상 수치를 [사실]로 쓰지 않았으며, iFlex 서술은 '연계 대상:'으로 시작했다.",
    "5절 현장 유형 — 사례를 물류창고(DeepFleet, iFlex 는 연계 대상 보충 서술)·병원(Garces 외)·제조 공장(현대차)·기타(대학 캠퍼스 청소 로봇) 네 묶음으로 쓰고, f12 는 6절 '배터리·고장 예측' 근거로만 썼으며, 상업 시설·가정·실외 사례는 찾지 못했다고 적었다. site_matrix_updates 는 이 네 현장 유형의 칸만 냈다.",
    "용어집 '결정 중심 학습' — term_en 을 'Decision-Focused Learning'으로 두고 SPO 는 정의 안에서 대표 방법으로 적었으며, 4절 본문도 같은 방식(대표 방법인 SPO)으로 썼다.",
    "8절 저자 보고 — 8절 도입에 모든 수치가 단일 출처 저자 보고이고 교차 확인된 수치가 없다고 밝히고, SILLM(+137.7%·+16.0%)·RTAW(14%)·Pookkuttath 외(91%)·Poskart 외(결정계수) 수치를 '저자 보고:'로 표시했다(5절·6절의 같은 수치도 '저자는 … 보고했다'로 썼다).",
    "분량 초과 자동 분리: 46. 예측·학습 기반 최적화 본문 10,784자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,283자"
  ]
}
```

### runs/2026-09-30-09/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area46-s6.md (1,868자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area46-s8.md (1,712자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area46-s4.md (1,029자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area46-s10.md (942자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area46-s11.md (669자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area46-s3.md (613자)
    - docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area46-s7.md (463자)
```

### runs/2026-09-30-09/pages/categories/ai-and-learning/prediction-and-learning-based-optimization.md

```markdown
---
title: "46. 예측·학습 기반 최적화"
type: area
category: "L. AI·학습 기술"
area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [결정 중심 학습, 예지 정비, 모방 학습, 지속형 MAPF, 학습 기반 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1105, ref-1106, ref-1107, ref-199, ref-1109, ref-623, ref-1111, ref-1112, ref-1113, ref-1114, ref-1115, ref-1116, ref-1117, ref-1118]
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
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

예측·학습 기반 최적화는 플릿의 혼잡, 시간에 따라 바뀌는 작업 요청, 배터리 소모와 고장처럼 계획을 어긋나게 하는 요인을 미리 알아 배정·경로·정비 결정에 반영하려는 영역이다. [추정][^ref-1105][^ref-1116][^ref-1112]

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
| 작업 대상 | 로봇의 위치·목표·상호작용 이동 데이터(정보) [사실][^ref-1105] |
| 수행 자원 | 풀필먼트·분류 센터의 이동 로봇 플릿과, 미래 교통 패턴·위치를 예측하는 DeepFleet 모델 [추정] 벤더 주장[^ref-1106] |
| 제약 | 혼잡·병목 구간. 예측한 혼잡을 피하도록 배정과 경로를 조정한다 [추정] 벤더 주장[^ref-1106] |
| 완료·인계 | 미확인 |
| 예외·성과 | 아마존은 로봇 이동 효율을 10% 높였다고 주장하며, 독립 측정은 확인하지 못했다 [추정] 벤더 주장[^ref-1106] |

아마존 연구진의 DeepFleet은 전 세계 아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 다중 로봇 기반 모델 모음이다(2025-08 공개, 2026-04 개정). [사실][^ref-1105] 아마존은 이 모델을 현재 혼잡 예측으로 작업 배정과 경로를 조정하는 데 쓰고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 한다고 밝혔다(2025-08-11). [추정] 벤더 주장[^ref-1106] 이 사례에서 이 영역이 관여하는 곳은 혼잡이라는 제약을 미리 알아 배정·경로에 넣는 부분이다. [추정][^ref-1106]

같은 현장 유형의 다른 예로, 연계 대상: CJ대한통운은 2021-07-28 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다. [추정] 벤더 주장[^ref-1117] 이는 상위 업무 시스템 쪽의 수요 예측이며, 로봇 배정에 쓴 근거는 이 자료에 없다. [추정][^ref-1117]

**현장 유형:** 병원

**사례:** 병원 입원 병동의 간호 업무 요청을 이기종 로봇에 배정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 병동에서 간호 업무 요청이 들어오면 작업이 발생한다 [사실][^ref-1116] |
| 작업 대상 | 간호 업무 요청에 딸린 작업. 운반 품목 같은 구체 대상은 초록에 없어 미확인이다 [사실][^ref-1116] |
| 수행 자원 | 이기종 다중 로봇. 배치 전에 과거 요청 데이터로 로봇 구성(차량 소요대수)을 고른다 [사실][^ref-1116] |
| 제약 | 즉시 확정은 이미 들어온 요청에만 하고, 표본 추출한 미래 요청 시나리오는 평가에만 쓴다 [사실][^ref-1116] |
| 완료·인계 | 미확인 |
| 예외·성과 | 요청 분포가 바뀌면 최근 예측 오차로 예측 요청을 다시 가중하고 아직 시작하지 않은 배정만 다시 최적화한다. 저자는 기준선보다 대기 시간을 줄였고 꼬리 지연 지표에서 개선이 가장 컸다고 보고했다 [사실][^ref-1116] |

Garces 외(2026-08, 동료 심사 전 프리프린트)는 병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 모델 기반 강화학습 롤아웃을 평가했다. [사실][^ref-1116] 이 사례에서 이 영역은 시작 조건(요청)을 예측해 수행 자원 구성과 배정에 넣고, 분포 이동이 생기면 재최적화 범위를 좁히는 부분에 관여한다. [추정][^ref-1116]

**현장 유형:** 제조 공장

**사례:** 제조 공장에서 산업용 로봇팔 고장을 미리 예측해 정비를 계획

| 항목 | 내용 |
|---|---|
| 시작 조건 | AI 고장예측 시스템이 로봇팔의 모터 부하·진동·전류 신호에서 이상을 감지한다 [추정] 벤더 주장[^ref-1113] |
| 작업 대상 | 생산 현장의 산업용 로봇팔(설비) [추정] 벤더 주장[^ref-1113] |
| 수행 자원 | 신호를 학습한 AI 고장예측 시스템. 정비는 사후 대응에서 계획적 예측 정비로 바꾸려 한다 [추정] 벤더 주장[^ref-1113] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 회사는 고장 약 5일 전에 90% 이상 정확도로 이상을 감지한다고 밝혔고, 정확도 산정 방법·데이터 규모는 기사에 없다 [추정] 벤더 주장[^ref-1113] |

파이낸셜뉴스(2026-05-28)가 전한 현대자동차 발표에 따르면 현대차는 이 시스템을 국내 생산 현장에 먼저 적용한 뒤 해외 생산거점으로 넓히려 한다. [추정] 벤더 주장[^ref-1113] 로봇팔의 부품 수준 신호 감시는 연계 대상이며, 이 영역이 관여하는 부분은 예측 결과를 정비 일정과 작업 배정에 넣는 쪽이다. [추정][^ref-1113]

**현장 유형:** 기타

**사례:** 대학 캠퍼스(로비·푸드코트·복도)에서 청소 로봇의 이상 진동을 분류해 예지 정비 지도를 만듦

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관성 측정 장치(Inertial Measurement Unit, IMU) 진동 신호가 충돌·조립 풀림·구조 불균형 같은 이상 클래스로 분류된다 [사실][^ref-1111] |
| 작업 대상 | 증기 걸레 청소 로봇과 청소 구역(로비·푸드코트·복도) [사실][^ref-1111] |
| 수행 자원 | 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망과 정비 팀 [사실][^ref-1111] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 정비 팀이 분류 결과를 동시적 위치 추정·지도 작성(Simultaneous Localization and Mapping, SLAM) 지도에 겹친 예지 정비 지도로 위험 구역을 격리하고 심각도를 판단한다. 저자는 실시간 현장 시험 정확도 91%를 보고했다 [사실][^ref-1111] |

Pookkuttath 외(Sensors, 2021-12-21)는 싱가포르 기술디자인대학(SUTD) 캠퍼스에서 이 방법을 현장 시험했다. [사실][^ref-1111] 이 사례에서 이 영역은 고장 징후를 공간 정보와 묶어 정비 판단에 넘기는 부분에 관여한다. [추정][^ref-1111]

상업 시설·가정·실외 현장의 학습·예측 적용 사례는 이번 조사에서 찾지 못했다. 현장 유형별 전체 현황은 [현장 유형 매트릭스](../../site-matrix.md)에 있다.

## 6. 대표 접근법과 기술

같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1109][^ref-199][^ref-1118]

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
| 상위 업무 시스템 | 작업 요청 이력을 모아 예측에 공급하고, 예측한 요청·혼잡을 배정과 로봇 구성에 반영한다 [추정][^ref-1116][^ref-1105] | 전사 주문 수요예측과 그에 따른 인력 배치(예: 이커머스 플랫폼의 주문 유형별 물량 예측) [추정] 벤더 주장[^ref-1117] |
| 로봇 자체 지능·제어 | 배터리 소모·고장 위험 예측 결과를 받아 배정·충전·정비 일정에 반영한다 [추정][^ref-1112][^ref-1111] | 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시 [추정][^ref-1111][^ref-1113] |

ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델 공급, 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스, 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시, 학습 정책의 즉시 확정 범위 제한으로 보인다. [추정][^ref-1105][^ref-1106][^ref-1116][^ref-1112][^ref-1109]

연계 대상: 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다. [추정][^ref-1111][^ref-1113][^ref-1117]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역의 수요 예측(작업 요청·물동량 예측)과 외부 연계로 둔 전사 수요예측의 경계는 아직 정하지 않았으며 11절 열린 질문에 올렸다. 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1109][^ref-1111]

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area46-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 다음 질문을 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [46. 예측·학습 기반 최적화 — 열린 질문](../../topics/2026/2026-09-30-area46-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1105]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1106]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1113]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1117]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30
```

### docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md

```markdown
---
title: "46. 예측·학습 기반 최적화"
type: area
category: "L. AI·학습 기술"
area_no: 46
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 46. 예측·학습 기반 최적화

# 46. 예측·학습 기반 최적화

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s6.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 대표 접근법과 기술"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1105, ref-1106, ref-1107, ref-199, ref-1109, ref-623, ref-1111, ref-1112, ref-1115, ref-1116, ref-1118]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#6
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 대표 접근법과 기술

# 46. 예측·학습 기반 최적화 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1109][^ref-199][^ref-1118]
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고된다. [추정][^ref-1109][^ref-199][^ref-1118]

### 학습 기반 작업 배정

학습 기반 배정은 작업을 로봇에 나누는 결정을 강화학습 정책으로 내리는 접근이며, 공개 근거는 주로 시뮬레이션이다. [추정][^ref-623][^ref-1116] Agrawal·Bedi·Manocha의 RTAW(ICRA 2023)는 창고 작업 배정을 마르코프 결정 과정으로 두고, 로봇·작업 수와 무관한 전역 임베딩을 쓰는 주의 기반 정책을 근접 정책 최적화(Proximal Policy Optimization, PPO)로 학습했다. [사실][^ref-623] Garces 외는 미래 요청 시나리오를 표본 추출해 평가하되 즉시 확정은 이미 들어온 요청에만 하고, 최근 예측 오차로 예측 요청을 다시 가중하며 아직 시작하지 않은 배정만 다시 최적화했다. [사실][^ref-1116] 한계는 RTAW가 시뮬레이션 결과만 보고했고 Garces 외가 동료 심사 전 프리프린트라는 점이다. [사실][^ref-623][^ref-1116]

### 학습 기반 경로·교통 관리

Skrynnik 외의 POGEMA 벤치마크(ICLR 2025)에 따르면 고전 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)에서 탐색 기반 중앙 계획기 LaCAM이 다른 모든 방법보다 뚜렷이 앞섰고 학습형 전용 해법(DCC·SCRIMP)이 그 뒤를 따랐다. [사실][^ref-1109] 다중 에이전트 강화학습(Multi-Agent Reinforcement Learning, MARL) 방법(QPLEX·VDN·QMIX 등)은 크게 뒤처졌고, 그 가운데 MAMBA는 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했다. [사실][^ref-1109] 지속형 MAPF에서는 탐색 기반 RHCR가 확장성 지표를 뺀 모든 경우에 우월했다. [사실][^ref-1109]

학습 쪽에서는 전문가 해를 모방하는 방법이 두드러진다. Andreychuk 외의 MAPF-GPT(arXiv 2409.00134, 2024-08 제출, 2025-04 개정)는 전문가 해의 대규모 데이터셋을 트랜스포머로 모방학습해 추가 휴리스틱이나 에이전트 간 통신 없이 행동을 내며, 저자는 기존 최고 학습형 해법보다 앞서고 학습 데이터에 없는 문제에서도 제로샷으로 동작한다고 보고했다. [사실][^ref-1107] 이 비교의 대상은 학습형 해법이다. [사실][^ref-1107] Jiang 외의 SILLM(ICRA 2025)은 모방학습에 통신 모듈·충돌 해소·전역 안내를 결합한 지속형 MAPF 방법이다. [사실][^ref-199] Zhang 외의 안내 그래프 최적화(IJCAI 2024)는 온라인 경로 계획기는 그대로 두고 그 계획기가 따르는 간선 가중치만 배치 전에 최적화하거나 학습된 모델로 생성한다. [사실][^ref-1118]

### 대규모 플릿 기반 모델

DeepFleet은 로봇 중심(RC)·로봇–바닥(RF)·이미지–바닥(IF)·그래프–바닥(GF) 네 구조를 비교했고, 비동기 상태 갱신과 국지 상호작용 구조를 쓰는 RC와 GF가 가장 유망하다고 보고했다. [사실][^ref-1105] 이 모델의 미래 교통 예측은 지금의 배정·경로 결정에 쓰는 운영용 예측이므로, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 구분해 다룬다. [의견][^ref-1106]

### 결정 품질로 예측을 학습

SPO는 일반 기계학습이 예측 오차만 줄이고 예측이 어떻게 쓰일지 고려하지 않는다고 보고, 결정 손실을 학습 목표로 삼았다. [사실][^ref-1115] 최단 경로·포트폴리오 실험에서 모형이 잘못 지정된 경우 특히 표준 예측 후 최적화보다 크게 나았고, SPO+로 학습한 선형 모형이 비선형 정답에서도 랜덤 포레스트를 앞섰다고 저자는 보고했다. [사실][^ref-1115]

### 배터리·고장 예측

Poskart 외(Sensors, 2022-12-15)는 사내 물류·유연 생산 환경을 대상으로 MiR100 자율이동로봇의 미션별 배터리 소모를 회전 수·이동 거리·충전 상태·충전 상태×거리 항의 일반화 선형 모형으로 예측했다. [사실][^ref-1112] 저자는 이 예측을 실행 전 미션 가능 여부 판단, 다른 로봇으로의 위임, 로봇 추가 필요 판단에 쓸 수 있다고 제시했다. [사실][^ref-1112] 고장 예측 연구로는 청소 로봇의 IMU 진동 신호를 1차원 합성곱 신경망으로 분류하고 그 결과를 지도에 겹쳐 정비 판단에 쓰는 사례가 있다. [사실][^ref-1111] 현장 사례는 5절의 제조 공장·기타 사례에 정리했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1105]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1106]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-09-30
[^ref-1107]: Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv), MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale, 2024-08, https://arxiv.org/abs/2409.00134, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1115]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s8.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 대표 연구와 자료"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1105, ref-1107, ref-199, ref-1109, ref-623, ref-1111, ref-1112, ref-1115, ref-1116, ref-1118]
last_run: 2026-09-30
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

- Agaskar 외(Amazon), DeepFleet: Multi-Agent Foundation Models for Mobile Robots(arXiv 2508.08574, 2025-08 제출, 2026-04 개정) — 아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 다중 로봇 기반 모델 네 구조를 비교했다. [사실][^ref-1105]
- Skrynnik 외, POGEMA(ICLR 2025) — 고전·학습·혼합 MAPF 방법을 같은 조건에서 비교해, 탐색 기반 LaCAM·RHCR가 앞서고 MARL 방법이 크게 뒤처진다고 보고했다. [사실][^ref-1109]
- Andreychuk 외, MAPF-GPT(arXiv 2409.00134, 2024-08 제출, 2025-04 개정) — 전문가 해를 모방학습한 경로 찾기 기반 모델로, 학습형 해법 대비 우위와 제로샷 동작을 저자가 보고했다. [사실][^ref-1107]
- Jiang 외, Deploying Ten Thousand Robots(SILLM, ICRA 2025) — 저자 보고: 대형 지도 6종·최대 1만 대에서 처리량이 최고 학습 기반 기준선보다 137.7%, 최고 탐색 기반 기준선보다 16.0% 높았고, 실물 로봇 10대와 가상 로봇 100대로 검증했다. [사실][^ref-199]
- Zhang 외, Guidance Graph Optimization for Lifelong Multi-Agent Path Finding(IJCAI 2024) — 저자 보고: 대표 지속형 MAPF 알고리즘 3종의 처리량을 벤치마크 지도 8종에서 높였고, 갱신 모델은 93×91 지도·에이전트 3,000개까지 적용됐다. [사실][^ref-1118]
- Agrawal·Bedi·Manocha, RTAW(ICRA 2023) — 저자 보고: 시뮬레이션 창고(로봇 최대 1,000대)에서 픽업 거리 최소화 탐욕 규칙·후회 기반 방법보다 총 이동 지연을 최대 14% 줄였다. 시뮬레이션 한정이다. [사실][^ref-623]
- Garces 외, Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts(arXiv 2608.21554, 2026-08, 프리프린트) — 저자 보고: 반응형·토큰 패싱·예측 위치 선배치·근시적 탐욕 기준선과 비교해 거의 모든 요청을 처리하면서 대기 시간을 줄였고, 개선 폭은 꼬리 지연 지표에서 가장 컸다. 구체 수치는 초록에 없다. [사실][^ref-1116]
- Elmachtoub·Grigas, Smart "Predict, then Optimize"(arXiv 1710.08005, 2017-10 제출, 2020-11 개정, 학술지 게재 연도 미확인) — 예측을 결정 손실로 학습하는 틀을 제시했다. [사실][^ref-1115]
- Poskart 외, Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge(Sensors, 2022-12-15) — 저자 보고: 조정 결정계수 0.9629·0.9694, 예측의 약 50%가 실제 소모 ±0.1% 이내였다. [사실][^ref-1112]
- Pookkuttath 외, AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots(Sensors, 2021-12-21) — 저자 보고: 진동 5종 분류 정확도가 오프라인 92.2%, 캠퍼스 실시간 현장 시험 91%였다. [사실][^ref-1111]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1105]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1107]: Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv), MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale, 2024-08, https://arxiv.org/abs/2409.00134, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1115]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s4.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 핵심 개념과 용어"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1107, ref-199, ref-623, ref-1111, ref-1112, ref-1114, ref-1115, ref-1116, ref-1118]
last_run: 2026-09-30
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

- **결정 중심 학습(Decision-Focused Learning)** — 예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다. 대표 방법인 Smart "Predict, then Optimize"(SPO)는 결정 손실(SPO 손실)과 그 볼록 대리 손실(SPO+)로 최적화 문제의 목적·제약을 학습에 반영한다. [사실][^ref-1115]
- **모방 학습(Imitation Learning)** — 전문가(예: 탐색 기반 계획기)가 만든 해를 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다. 경로 찾기에서는 전문가 해의 대규모 데이터셋을 트랜스포머로 모방학습한 연구가 있다. [사실][^ref-1107][^ref-199]
- **안내 그래프(Guidance Graph)** — [지속형 다중 에이전트 경로 찾기](../../glossary/lifelong-mapf.md)(Lifelong Multi-Agent Path Finding, Lifelong MAPF) 알고리즘이 따르는 격자 간선 가중치다. 배치 전에 오프라인으로 최적화하거나 가중치를 생성하는 모델을 학습해 교통 흐름을 유도한다. [사실][^ref-1118]
- **예지(Prognostics)와 예지 정비(Predictive Maintenance)** — ISO 13381-1은 기계 상태 감시·진단에서 예지의 일반 지침을 정한 표준이다. [사실][^ref-1114] 예지 정비는 상태 신호로 고장을 미리 예측해 정비 시점과 조치를 정하는 방식이며, 청소 로봇의 진동 분류 결과를 지도에 겹친 예지 정비 지도가 그 예다. [사실][^ref-1111] 관련 용어: [상태 기반 정비](../../glossary/condition-based-maintenance.md).
- **분포 이동(Distribution Shift)** — 운영 중 들어오는 요청의 양상이 학습·예측 때와 달라지는 상황이다. 병원 배정 연구는 최근 예측 오차에 따라 예측 요청의 가중치를 다시 매겨 이에 대응했다. [사실][^ref-1116]
- **[충전 상태](../../glossary/state-of-charge.md)(State of Charge, SoC)** — 배터리 소모 예측 모형의 입력 항목으로 쓰였다. [사실][^ref-1112]
- **[다중 로봇 작업 배정](../../glossary/mrta.md)(Multi-Robot Task Allocation, MRTA)** — 학습 기반 배정은 이 문제를 강화학습 정책으로 푼다. [사실][^ref-623]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1107]: Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv), MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale, 2024-08, https://arxiv.org/abs/2409.00134, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1114]: ISO (ISO/TC 108), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025, https://www.iso.org/standard/88029.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1115]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s10.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1105, ref-1106, ref-1107, ref-199, ref-1109, ref-623, ref-1111, ref-1112, ref-1113, ref-1114, ref-1115, ref-1116, ref-1117, ref-1118]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#10
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결

# 46. 예측·학습 기반 최적화 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1109][^ref-1111]
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 G. 계획·최적화의 배정·순서·경로·충전 영역에 학습·예측 방법을 제공하고, 고장 예측으로 J. 현장 운영·관제와, 현장 사례로 Q. 현장 유형별 적용과 이어진다. [추정][^ref-623][^ref-1109][^ref-1111]

- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 작업 요청·물동량 같은 수요 정보는 상위 업무 시스템에서 온다. [추정][^ref-1117]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 학습 기반 배정(주의 기반 강화학습, 예측 인지형 배정)이 적용되는 영역이다. [추정][^ref-623][^ref-1116]
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 결정 중심 학습은 예측을 순서·일정 결정의 품질로 평가하는 방법이다. [추정][^ref-1115]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 학습 기반·혼합 경로 방법과 안내 그래프가 적용되는 영역이다. [추정][^ref-1109][^ref-1107][^ref-199][^ref-1118]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 배터리 소모 예측을 미션 위임·충전 판단에 쓴다. [추정][^ref-1112]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 과거 요청 데이터로 로봇 구성을 고르고 로봇 추가 필요를 판단한다. [추정][^ref-1116][^ref-1112]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 고장 예측은 장애 분석에 쓰이는 연구 방법이다. [추정][^ref-1111][^ref-1113]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — DeepFleet·MAPF-GPT 같은 기반 모델 흐름과 이어진다. [추정][^ref-1105][^ref-1107]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 예측 오차·분포 이동 감시와 학습 정책 운영을 다룬다. [추정][^ref-1116]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 학습 정책을 탐색 기반 방법과 같은 조건에서 비교하는 벤치마크가 필요하다. [추정][^ref-1109]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 예지 표준은 정비 기준을 정할 때 쓰인다. [추정][^ref-1114]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 대규모 플릿 혼잡 예측과 물량 예측 사례가 있다. [추정][^ref-1105][^ref-1106][^ref-1117]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 산업용 로봇팔 고장 예측 사례가 있다. [추정][^ref-1113]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 간호 업무 요청의 예측 인지형 배정 사례가 있다. [추정][^ref-1116]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 대학 캠퍼스 청소 로봇의 예지 정비 사례가 있다. [추정][^ref-1111]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1105]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1106]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-09-30
[^ref-1107]: Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv), MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale, 2024-08, https://arxiv.org/abs/2409.00134, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1113]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-09-30
[^ref-1114]: ISO (ISO/TC 108), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025, https://www.iso.org/standard/88029.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1115]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1117]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s11.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 열린 질문"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#11
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 열린 질문

# 46. 예측·학습 기반 최적화 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 실행에서 다음 질문을 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 실행에서 다음 질문을 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-09) 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-09) 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-09) 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-09) 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-09) 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s3.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 왜 중요한가"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1105, ref-1106, ref-199, ref-1109, ref-623, ref-1111, ref-1112, ref-1113, ref-1115, ref-1116, ref-1117, ref-1118]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#3
---

[홈](../../index.md) › [주제](../index.md) › 46. 예측·학습 기반 최적화 — 왜 중요한가

# 46. 예측·학습 기반 최적화 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 예측·학습 기반 최적화는 플릿의 혼잡, 시간에 따라 바뀌는 작업 요청, 배터리 소모와 고장처럼 계획을 어긋나게 하는 요인을 미리 알아 배정·경로·정비 결정에 반영하려는 영역이다. [추정][^ref-1105][^ref-1116][^ref-1112]
- 이 페이지는 [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

예측·학습 기반 최적화는 플릿의 혼잡, 시간에 따라 바뀌는 작업 요청, 배터리 소모와 고장처럼 계획을 어긋나게 하는 요인을 미리 알아 배정·경로·정비 결정에 반영하려는 영역이다. [추정][^ref-1105][^ref-1116][^ref-1112]

대규모 플릿에서는 혼잡을 미리 알아야 작업 배정과 경로를 병목 밖으로 돌릴 수 있다. [추정][^ref-1105][^ref-1106] 병원처럼 요청이 시간에 따라 달라지고 분포가 바뀌는 현장에서는 들어온 요청에만 반응하는 방식보다 앞으로 올 요청을 고려한 배정이 대기 시간을 줄였다는 보고가 있다. [추정][^ref-1116] 예측 정확도가 높아도 그 예측으로 내린 결정의 품질이 따라오지 않을 수 있다는 점도 이 영역이 따로 필요한 까닭이다. [추정][^ref-1115] 배터리 소모와 고장은 실행 도중 계획을 어긋나게 하므로 미리 예측해 배정·정비에 넣어야 한다. [추정][^ref-1112][^ref-1111][^ref-1113]

2절의 핵심 질문에 대한 이번 조사의 잠정 답은 다음과 같다. 개선 근거는 대부분 시뮬레이션·벤치마크에서 나왔고, 실제 운영 개선 수치는 벤더·회사 발표에 머문다. [추정][^ref-1109][^ref-199][^ref-623][^ref-1106][^ref-1113][^ref-1117] 학습 단독 정책은 탐색 기반 방법보다 뒤질 수 있고, 한 강화학습 방법(MAMBA)은 분포 밖 문제에서 한 인스턴스도 풀지 못했다. [추정][^ref-1109] 개선은 학습을 탐색·최적화와 결합하거나, 결정 손실로 예측을 학습하거나, 관측된 요청만 확정하고 예측 오차로 가중치를 다시 매기는 설계에서 주로 보고된다. [추정][^ref-199][^ref-1118][^ref-1115][^ref-1116]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1105]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-09-30
[^ref-1106]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-09-30
[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-623]: Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023), RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-30
[^ref-1111]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-09-30
[^ref-1112]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-09-30
[^ref-1113]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-09-30
[^ref-1115]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-09-30
[^ref-1116]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-09-30
[^ref-1117]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-09-30
[^ref-1118]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-09/pages/topics/2026/2026-09-30-area46-s7.md

```markdown
---
title: "46. 예측·학습 기반 최적화 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 46
related_areas: [23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-199, ref-1109, ref-1114]
last_run: 2026-09-30
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

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| POGEMA | 평가 프로그램 | 고전·학습·혼합 MAPF 방법을 같은 조건에서 비교하는 벤치마크 플랫폼. 학습 기반 경로 방법과 탐색 기반 방법의 비교 결과를 제공한다 | [사실][^ref-1109] |
| ISO 13381-1:2025 | 표준 | 기계 상태 감시·진단의 예지 일반 지침(3판, 2015년 2판 대체). 개발자·공급자·사용자·제조사가 예지 개념을 공유하고 정확한 예지에 필요한 데이터·특성·절차를 정하게 하는 것이 목적이다. 원문 미열람 | [사실][^ref-1114] |
| League of Robot Runners | 평가 프로그램 | 지속형 MAPF 경진대회. SILLM은 2023년 대회 우승 해법을 앞섰다고 저자가 보고했다 | [사실][^ref-199] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md)
- 관련 영역: [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-199]: Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-30
[^ref-1109]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-09-30
[^ref-1114]: ISO (ISO/TC 108), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025, https://www.iso.org/standard/88029.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-09 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-09 | 46. 예측·학습 기반 최적화 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1044건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 282개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
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
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
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
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
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
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
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
- finops: 핀옵스 (FinOps)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
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
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
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
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
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
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [46] 에 걸린 0건 / 전체 215건)

```markdown
없음
```
