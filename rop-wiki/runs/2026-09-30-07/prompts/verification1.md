(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-07
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 44. 로봇 기반 모델·언어 모델 계획 (L. AI·학습 기술)
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

### runs/2026-09-30-07/target.json

```json
{
  "run_id": "2026-09-30-07",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 116,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 44,
    "area_name": "44. 로봇 기반 모델·언어 모델 계획",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=44"
}
```

### runs/2026-09-30-07/research.json

```json
{
  "run_id": "2026-09-30-07",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 44,
    "area_name": "44. 로봇 기반 모델·언어 모델 계획",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 로봇 기반 모델, 교차 형태 학습, 행동 토큰화, LLM-모듈로, 불확실도 정렬 연결 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정·제조 공장·물류창고 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 시각–언어–행동 모델, 언어 모델 계획과 기호 계획기 결합, 다중 로봇 계획, 불확실도 기반 도움 요청 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open X-Embodiment, OpenVLA, GR00T N1, ROSA 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]",
    "시각–언어–행동(Vision-Language-Action, VLA) 모델과 로봇 기반 모델은 무엇이며 어떤 데이터·구조로 여러 로봇·작업에 일반화하는가? (섹션 4·6·8 겨냥)",
    "대규모 언어 모델(LLM)로 작업을 계획·분해할 때의 한계는 무엇이고, 기호 계획기·외부 검증기·불확실도 기반 도움 요청으로 어떻게 보완하는가? (섹션 3·6·8 겨냥)",
    "언어 모델로 여러 로봇의 작업 분해·연합 형성·배정을 계획하는 연구와 공개 오픈소스(ROS 연동 에이전트 포함)는 무엇인가? (섹션 6·7 겨냥)",
    "가정·제조 공장·물류창고 등 현장(국내 포함)에서 로봇 기반 모델을 적용한 사례와 그 조건·성과는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)",
    "로봇 기반 모델·언어 모델 계획에서 ROP가 직접 맡을 것과 로봇 제조사·모델 제공자에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Brohan 외의 RT-2(arXiv 2307.15818, 2023-07)는 로봇 행동을 텍스트 토큰으로 표현해 자연어 토큰과 같은 방식으로 학습 데이터에 넣고, 시각–언어 모델을 로봇 궤적 데이터와 웹 시각 질의응답 과제에 함께 미세조정한 시각–언어–행동(VLA) 모델로, 6,000회 평가에서 새 물체·학습에 없던 명령에 대한 일반화가 좋아졌다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1045"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "행동을 텍스트 토큰으로 표현하고 자연어 토큰과 같은 방식으로 학습 세트에 넣는다. 6,000회 평가, 새 물체·새 명령 일반화, 연쇄 사고 프롬프트로 다단계 추론(초록 기준).",
      "as_of": "2023-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Open X-Embodiment 협력단(arXiv 2310.08864, 2023-10)은 21개 기관이 모은 22종 로봇의 데이터(527개 스킬, 160,266개 작업)를 표준 형식으로 공개하고, 이 데이터로 학습한 RT-X 모델이 다른 로봇의 경험을 활용해 여러 로봇의 능력을 높이는 긍정적 전이를 보였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1048"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "22종 로봇, 21개 기관, 527개 스킬, 160,266개 작업. RT-X 는 다른 플랫폼의 경험으로 여러 로봇의 능력을 높이는 긍정적 전이를 보임(초록 기준, v9 2025-05 개정).",
      "as_of": "2023-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Kim 외의 OpenVLA(arXiv 2406.09246, 2024-06)는 Llama 2 에 DINOv2·SigLIP 시각 특징을 결합한 70억 매개변수 공개 VLA 모델로 실제 로봇 시연 97만 건으로 학습했고, 29개 작업에서 매개변수가 7배 많은 RT-2-X(550억)보다 절대 성공률이 16.5%p 높았으며, 모델 체크포인트·미세조정 노트북·PyTorch 코드를 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "7B 매개변수, Llama 2 + DINOv2·SigLIP, 97만 건 실제 로봇 시연. 29개 작업에서 RT-2-X(55B) 대비 절대 성공률 16.5% 높음, 미세조정 시 Diffusion Policy 대비 20.4% 높음(초록 기준).",
      "as_of": "2024-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Physical Intelligence 의 π0.5(arXiv 2504.16054, 2025-04)는 여러 로봇의 데이터·고수준 의미 예측·웹 데이터 등 이질적 과제를 함께 학습(co-training)해, 처음 보는 가정집에서 부엌·침실 정리 같은 장기·정교한 조작 작업을 수행했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1047"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"cleaning a kitchen or bedroom, in entirely new homes\". 영상 관측·언어 명령·물체 검출·의미 하위 작업 예측·저수준 행동을 섞은 예제로 공동 학습(초록 기준).",
      "as_of": "2025-04",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "NVIDIA 의 GR00T N1(arXiv 2503.14734, 2025-03)은 환경을 해석하는 시각–언어 모듈(System 2)과 실시간 운동 명령을 만드는 확산 트랜스포머(System 1)를 나눈 이중 시스템 구조의 공개 휴머노이드용 VLA 모델로, 실제 로봇 궤적·사람 영상·합성 데이터를 섞어 학습하고 Fourier GR-1 휴머노이드의 양손 조작에 배치했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1054"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "System 2 시각–언어 모듈 + System 1 확산 트랜스포머. 실제 로봇 궤적·사람 영상·합성 데이터의 이질적 혼합으로 학습, Fourier GR-1 양손 조작 배치(초록 기준, 성능 비교 주장은 제외).",
      "as_of": "2025-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Ahn 외의 SayCan(arXiv 2204.01691, 2022-04)은 언어 모델이 긴 추상적 지시를 수행하는 절차 지식을 제공하고, 로봇이 미리 학습한 스킬의 가치 함수가 현재 물리 환경에서 그 스킬이 실행 가능한 정도를 제공해 둘을 결합하는 방식으로 언어 모델 계획을 로봇 능력에 접지(grounding)했으며, 모바일 매니퓰레이터로 실험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1049"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "언어 모델은 고수준 절차 지식, 스킬의 가치 함수는 특정 물리 환경에 연결하는 접지를 제공. 모바일 매니퓰레이터로 장기·추상 자연어 지시 수행(초록 기준).",
      "as_of": "2022-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Liu 외의 LLM+P(arXiv 2304.11477, 2023-04)는 자연어 문제 설명을 언어 모델로 PDDL(계획 도메인 정의 언어) 문제로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 3단계 방식으로, 대부분의 벤치마크 문제에서 최적해를 낸 반면 언어 모델 단독은 대부분 실행 가능한 계획조차 내지 못했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1050"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자연어→PDDL 변환, 고전 계획기로 풀이, 결과를 자연어로 역변환. LLM+P 는 대부분 문제에 최적해, LLM 단독은 대부분 실행 가능한 계획도 못 냄(초록 기준).",
      "as_of": "2023-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Kambhampati 외(ICML 2024, arXiv 2402.01817)는 자기회귀 언어 모델이 스스로 계획하거나 자기 검증할 수 없다고 보고, 언어 모델을 근사적 지식원으로 두고 외부 기호 검증기와 양방향으로 상호작용하게 하는 LLM-모듈로(LLM-Modulo) 프레임워크를 제안했다.",
      "tag": "의견",
      "source_ids": [
        "ref-1051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"auto-regressive LLMs cannot, by themselves, do planning or self-verification\". 언어 모델은 보편적 근사 지식원, 외부 기호 검증기와 양방향 결합(ICML 2024, PMLR 235).",
      "as_of": "2024-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Ren 외의 KnowNo(CoRL 2023, arXiv 2307.01928)는 언어 모델 계획기가 확신에 찬 환각 예측을 내는 문제에 대해 등각 예측으로 불확실도를 측정해, 공간·수량·선호·언어 모호성이 있을 때 사람에게 도움을 요청하게 하고 사람 도움을 최소화하면서 작업 완료에 통계적 보장을 주며, 모델 미세조정이 필요 없다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1053"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "등각 예측으로 작업 완료의 통계적 보장과 사람 도움 최소화. 공간·수량·선호·언어 모호성 대상, 미세조정 불필요(초록 기준, CoRL 2023 구두 발표).",
      "as_of": "2023-07",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "Kannan·Venkatesh·Min 의 SMART-LLM(arXiv 2309.10062, IROS 2024 투고)은 프로그램 형식의 퓨샷 프롬프트로 언어 모델이 고수준 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸게 하고, 복잡도가 다른 네 범주의 지시로 된 벤치마크를 만들어 시뮬레이션과 실제 로봇으로 시험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1052"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "작업 분해, 연합 형성, 작업 배정의 3단계. 프로그램형 퓨샷 프롬프트, 네 범주 지시 벤치마크, 시뮬레이션·실제 로봇 실험(초록 기준).",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Su 외의 IMR-LLM(arXiv 2603.02669, 2026-03)은 가정용보다 제약이 엄격한 산업 다중 로봇 생산 작업을 대상으로, 언어 모델이 선택 그래프(disjunctive graph) 구성을 돕고 결정적 풀이 방법으로 실행 가능한 고수준 계획을 얻은 뒤 공정 트리를 따라 실행 가능한 저수준 프로그램을 생성하게 했으며, 세 난이도의 벤치마크 IMR-Bench 로 평가했다(초록에는 실제 공장 배치가 적혀 있지 않다).",
      "tag": "사실",
      "source_ids": [
        "ref-1055"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LLM 이 disjunctive graph 구성을 돕고 결정적 풀이로 고수준 계획, 공정 트리로 저수준 프로그램 생성. IMR-Bench 세 난이도. 초록에 실제 배치 언급 없음.",
      "as_of": "2026-03",
      "site_type": "제조 공장",
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "NASA 제트추진연구소(JPL)가 관리하는 오픈소스 ROSA(ROS Agent)는 LangChain 위에 만든 에이전트로, ROS 1(Noetic)과 ROS 2(Humble·Iron·Jazzy) 기반 로봇 시스템에 자연어로 질의하고 명령하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1056"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ROS 기반 로봇 시스템과 자연어 질의로 상호작용하는 에이전트. LangChain 기반, ROS 1 Noetic·ROS 2 Humble/Iron/Jazzy 지원, TurtleSim 데모(README 기준).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "BMW 그룹은 2025년 스파턴버그 공장에 Figure AI 의 휴머노이드 Figure 02 를 11개월 동안 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1058"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 2025년 11개월 배치, 용접 공정용 판금 부품 삽입, X3 3만 대 이상 생산 지원(BMW 그룹 보도자료, 2026-06-25). Figure AI 자체 발표 페이지는 열지 못해 교차 확인 못 함.",
      "as_of": "2026-06-25",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "같은 BMW 그룹 자료는 후속 Figure 03 이 스파턴버그 공장에서 대용량 용기에 섞여 들어온 부품을 집어 순서 대차(sequencing trolley)에 정리하고, 대차가 자동화 시스템으로 조립 공정에 운반되는 순서 공급(just in sequence) 물류 작업을 맡으며, 음성 대화 기능과 무선 충전을 갖췄다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1058"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 미분류 부품을 대용량 용기에서 받아 순서 대차에 정리, 대차는 자동화 시스템으로 조립 공정에 운반. 촉각 센서 손, 음성 대화, 무선 충전.",
      "as_of": "2026-06-25",
      "site_type": "제조 공장",
      "flow_item": "완료·인계",
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "지디넷코리아 보도(2025-05-01)에 따르면 2025-04-10 출범한 산업통상자원부 주도 K-휴머노이드 연합에서 레인보우로보틱스·에이로봇·홀리데이로보틱스·로보티즈·로브로스 5개 로봇기업이 개발 중인 휴머노이드를 서울대 AI연구원에 제공해 로봇 AI 파운데이션 모델 개발을 지원하기로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1057"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "산업부 설명을 인용한 기사. 4월 10일 출범, 3주 만에 MOU 4건. 5개 로봇기업이 휴머노이드를 서울대 AI연구원에 제공해 로봇 AI 파운데이션 모델 개발 지원. 정부 보도자료(korea.kr) 본문은 첨부 파일에만 있어 교차 확인 못 함.",
      "as_of": "2025-05-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "헬로티 보도(2025-11-26)에 따르면 로보티즈는 산업통상부 과제 'AI 파운데이션 모델 기반 유통 공정 특화 휴머노이드 로봇 개발'(정부 출연금 약 60억 원)로 VLA 모델을 넣은 상체형 휴머노이드 AI 워커를 BGF로지스 물류센터에 투입해 입·출고, 오발주 재분류, 비정형 상품 분류, 반품 처리 작업을 수행하게 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1059"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: VLA 모델을 내재화한 상체형 휴머노이드 AI 워커, BGF로지스와 협력해 입·출고·오발주·비정형 상품 분류·반품 처리 수행. 기사가 전한 회사·과제 설명이며 1차 출처 미확인.",
      "as_of": "2025-11-26",
      "site_type": "물류창고",
      "flow_item": "작업 대상",
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "같은 보도에 따르면 이 과제는 물류센터 핵심 공정 자동화율 80% 이상과 오발주 재분류·피킹 작업 성공률 90% 이상을 목표로 한다(달성 결과가 아니라 목표치다).",
      "tag": "추정",
      "source_ids": [
        "ref-1059"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 핵심 공정 자동화율 80% 이상, 오발주 재분류 및 피킹 작업 성공률 90% 이상 달성 목표. 실측 결과는 기사에 없음.",
      "as_of": "2025-11-26",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f18",
      "claim": "확인한 자료를 종합하면 핵심 질문(범용 로봇 모델과 언어 모델이 오케스트레이션의 무엇을 바꾸는가)에 대해, 로봇 기반 모델은 로봇 쪽 기능을 고정된 스킬 목록에서 새 물체·지시에 일반화하는 학습된 정책으로 바꾸고(f1~f5), 언어 모델은 지시 해석·작업 분해·다중 로봇 배정의 입력 방식을 바꾸지만(f6·f10·f11), 언어 모델 단독 계획은 실행 가능성·검증이 약해 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 형태가 연구의 공통 방향으로 보인다(f7·f8·f9).",
      "tag": "추정",
      "source_ids": [
        "ref-1045",
        "ref-1048",
        "ref-1046",
        "ref-1047",
        "ref-1054",
        "ref-1049",
        "ref-1052",
        "ref-1055",
        "ref-1050",
        "ref-1051",
        "ref-1053"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f11 의 종합 판단. 개별 근거는 각 finding 참조.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇의 데이터를 모아 하나의 정책을 학습하는 흐름(f2·f3)이 이종 로봇의 능력 표현과 등록 방식에 영향을 주고, 언어 모델 계획이 확신에 찬 오류를 낼 수 있어(f8·f9) 대화로 받은 지시를 실행 전에 검증할 장치가 필요하며, 제조 공장·물류창고에서 휴머노이드·VLA 적용이 시작됐다고 발표되고 있기 때문이다(f13·f16).",
      "tag": "추정",
      "source_ids": [
        "ref-1048",
        "ref-1046",
        "ref-1051",
        "ref-1053",
        "ref-1058",
        "ref-1059"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3·f8·f9·f13·f16 의 종합 판단. f13·f16 은 벤더 주장이다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 44. 로봇 기반 모델·언어 모델 계획에서 ROP 가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층(f7·f8·f11), 불확실할 때 사람에게 확인을 요청하는 절차(f9), 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇에 계획을 내리는 인터페이스(f6·f10·f12)다.",
      "tag": "추정",
      "source_ids": [
        "ref-1050",
        "ref-1051",
        "ref-1055",
        "ref-1053",
        "ref-1049",
        "ref-1052",
        "ref-1056"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6~f12 의 종합 판단. 분류 원문 C. 채팅 기반 구성·운영 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 같은 방향.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "연계 대상: 분류 원문 19장 기준으로 VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(f1·f3·f4·f5)은 로봇 자체 지능·제어(파지·모터·관절 제어)에 속하므로 로봇 제조사·모델 제공자가 맡고, 이종 제조사를 잇는 ROP 는 그런 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1045",
        "ref-1046",
        "ref-1047",
        "ref-1054"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f3·f4·f5 의 모델은 영상·언어에서 로봇 행동(저수준 운동 명령)을 직접 출력한다. 원문 19장 '로봇 자체 지능·제어' 경계에 대응시킨 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "이 영역은 학습된 범용 기능을 표현해야 하는 5. 로봇 능력·작업 표현과 4. 이기종 로봇 등록(f2·f3), 언어 모델 계획을 대화로 부르는 12. 채팅으로 업무 지시·오케스트레이션과 13. 대화형 기능의 신뢰·기반(f9·f12), 작업 분해의 24. 작업·워크플로 모델링(f7·f11), 연합 형성·배정의 25. 작업 배정 — MRTA(f10), 공정 순서의 26. 작업 순서·스케줄링(f11), 계획 검증의 29. 명령·작업 실행의 신뢰성과 54. 시험·형식 검증·벤치마크(f7·f8·f11), 사람 확인의 31. 사람–로봇 협업(f9), 실행 기준의 47. AI·학습·적응과 모델 운영(f8·f9), 업체 동향의 1. 기술·시장·업체 동향(f13·f15·f16), 적용 현장인 61. 물류창고(f16)·62. 제조 공장(f11·f13)·65. 가정·공동주택(f4)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1048",
        "ref-1046",
        "ref-1053",
        "ref-1056",
        "ref-1050",
        "ref-1055",
        "ref-1052",
        "ref-1051",
        "ref-1058",
        "ref-1057",
        "ref-1059",
        "ref-1047"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결의 근거 finding 을 괄호로 표시한 종합 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1045",
      "org": "Brohan, A., Brown, N. 외 (Google DeepMind, arXiv)",
      "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
      "published": "2023-07-28",
      "url": "https://arxiv.org/abs/2307.15818",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "행동을 텍스트 토큰으로 표현해 시각–언어 모델을 로봇 데이터·웹 데이터로 공동 미세조정한 VLA 모델. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1046",
      "org": "Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv)",
      "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
      "published": "2024-06-13",
      "url": "https://arxiv.org/abs/2406.09246",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "97만 건 실제 로봇 시연으로 학습한 70억 매개변수 공개 VLA 모델과 RT-2-X 비교. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1047",
      "org": "Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv)",
      "title": "π0.5: a Vision-Language-Action Model with Open-World Generalization",
      "published": "2025-04-22",
      "url": "https://arxiv.org/abs/2504.16054",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이질적 데이터 공동 학습으로 처음 보는 가정집에서 부엌·침실 정리를 수행한 VLA 모델. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1048",
      "org": "Open X-Embodiment Collaboration (arXiv)",
      "title": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models",
      "published": "2023-10-13",
      "url": "https://arxiv.org/abs/2310.08864",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "21개 기관·22종 로봇의 데이터셋과 교차 형태 전이를 보인 RT-X 모델. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1049",
      "org": "Ahn, M., Brohan, A., Brown, N. 외 (arXiv)",
      "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
      "published": "2022-04-04",
      "url": "https://arxiv.org/abs/2204.01691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "언어 모델의 절차 지식과 스킬 가치 함수를 결합해 계획을 로봇 능력에 접지한 SayCan. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1050",
      "org": "Liu, B., Jiang, Y., Zhang, X. 외 (arXiv)",
      "title": "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency",
      "published": "2023-04-22",
      "url": "https://arxiv.org/abs/2304.11477",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자연어를 PDDL 로 옮겨 고전 계획기로 풀고 다시 자연어로 옮기는 LLM+P. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1051",
      "org": "Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv)",
      "title": "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks",
      "published": "2024-02-02",
      "url": "https://arxiv.org/abs/2402.01817",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "언어 모델 단독 계획·자기 검증의 한계를 논하고 외부 검증기와 결합하는 LLM-모듈로 프레임워크를 제안. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1052",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv)",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09-18",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "언어 모델로 작업 분해·연합 형성·작업 배정을 하는 다중 로봇 계획 프레임워크와 벤치마크. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1053",
      "org": "Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv)",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07-04",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "등각 예측으로 언어 모델 계획기의 불확실도를 측정해 도움을 요청하게 하는 KnowNo. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1054",
      "org": "NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv)",
      "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
      "published": "2025-03-18",
      "url": "https://arxiv.org/abs/2503.14734",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "시각–언어 모듈과 확산 트랜스포머를 나눈 이중 시스템 구조의 공개 휴머노이드 VLA 모델. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1055",
      "org": "Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv)",
      "title": "IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models",
      "published": "2026-03-03",
      "url": "https://arxiv.org/abs/2603.02669",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "언어 모델과 선택 그래프·결정적 풀이를 결합한 산업 다중 로봇 계획·프로그램 생성과 IMR-Bench. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1056",
      "org": "NASA Jet Propulsion Laboratory (nasa-jpl)",
      "title": "ROSA — README",
      "published": null,
      "url": "https://github.com/nasa-jpl/rosa",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "LangChain 기반으로 ROS 1·ROS 2 시스템에 자연어로 질의·명령하는 ROS 에이전트의 저장소 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/nasa-jpl/rosa/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1057",
      "org": "지디넷코리아",
      "title": "K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과",
      "published": "2025-05-01",
      "url": "https://zdnet.co.kr/view/?no=20250501140356",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업부 설명을 인용해 K-휴머노이드 연합의 초기 성과와 로봇 AI 파운데이션 모델 개발 협력을 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1058",
      "org": "BMW Group",
      "title": "BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg",
      "published": "2026-06-25",
      "url": "https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Figure 02 의 2025년 스파턴버그 배치 결과와 Figure 03 의 순서 공급 물류 작업 계획을 밝힌 BMW 그룹 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1059",
      "org": "헬로티",
      "title": "VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입",
      "published": "2025-11-26",
      "url": "https://www.hellot.net/news/article.html?no=107567",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "VLA 모델을 넣은 로보티즈 AI 워커의 BGF로지스 물류센터 투입과 과제 목표를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
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
      "rationale": "섹션 3: f19(왜 중요한가), f18(핵심 질문 답, 추정) / 섹션 4: VLA·행동 토큰화 f1, 교차 형태 학습 f2, 이중 시스템 구조 f5, 접지 f6, LLM-모듈로 f8, 불확실도 정렬 f9 / 섹션 5: 가정 — f4, 제조 공장 — f11(벤치마크 한정)·f13·f14(벤더 주장 병기), 물류창고 — f16·f17(국내, 벤더 주장·목표치 병기). 병원·상업 시설·실외 사례는 찾지 못함을 명시 / 섹션 6: 로봇 기반 모델 f1~f5, 언어 모델 계획과 기호 계획기·검증기 결합 f6~f8, 다중 로봇 계획 f10·f11, 불확실도 기반 도움 요청 f9 / 섹션 7: Open X-Embodiment f2, OpenVLA f3, GR00T N1 f5, ROSA f12, PDDL f7 / 섹션 8: f1~f11, 국내 동향 f15 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65 / 섹션 11: open_questions_new 3건. 다음 실행 후보: 12. 채팅으로 업무 지시·오케스트레이션 페이지에 f7~f9 반영, 25. 작업 배정 — MRTA 페이지에 f10 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "로봇 기반 모델",
      "term_en": "Robot Foundation Model",
      "definition": "여러 로봇·작업·환경의 대규모 데이터로 사전 학습해 새 작업·물체·로봇에 미세조정하거나 바로 쓸 수 있게 한 범용 로봇 모델로, 시각–언어–행동 모델이 대표적이다."
    },
    {
      "term_ko": "교차 형태 학습",
      "term_en": "Cross-embodiment Learning",
      "definition": "형태·센서·구동 방식이 다른 여러 로봇의 데이터를 함께 학습해 한 로봇의 경험이 다른 로봇의 성능을 높이게 하는 학습 방식이다."
    },
    {
      "term_ko": "이중 시스템 구조",
      "term_en": "Dual-system Architecture (System 1 / System 2)",
      "definition": "느린 시각–언어 추론 모듈(System 2)이 상황을 해석하고 빠른 행동 생성 모듈(System 1)이 실시간 운동 명령을 만드는 로봇 기반 모델 구조다."
    }
  ],
  "open_questions_new": [
    "로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 5. 로봇 능력·작업 표현 | 근거: f3 | 종류: 일반",
    "언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f11 | 종류: 일반",
    "국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 61. 물류창고 | 근거: f17 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f1~f11 은 arXiv 초록 기준이며 본문 실험 조건 미확인",
      "f13·f14: Figure AI 자체 발표 페이지(figure.ai/news/production-at-bmw)는 연결 오류로 열지 못해 교차 확인 실패",
      "f15: 산업통상자원부 보도자료(korea.kr, 2025-04-10) 본문은 첨부 파일에만 있어 교차 확인 실패, '2028년까지 로봇 AI 파운데이션 모델 구축' 목표는 검색 요약에만 있어 넣지 않음",
      "f16·f17: 로보티즈·BGF로지스 1차 발표 미확인, 목표치는 실측 결과 아님",
      "OpenVLA 라이선스는 요약 결과가 모호해 넣지 않음",
      "병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 실배치 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f1·f3·f4·f5: VLA 의 저수준 조작 정책은 로봇 자체 지능·제어 영역이므로 동향 근거로만 쓰고 f21 에서 '연계 대상: '으로 구분함",
      "f11: 공정 프로그램 생성은 로봇 제어 코드에 닿으므로 계획 검증 근거로만 제안함",
      "f13·f14·f16·f17: 벤더·기사 주장이므로 vendor_claim: true·태그 추정으로 냄"
    ],
    "budget_used": {
      "queries": 5,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치 — f15·f17 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON(runs/2026-09-30-07/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상으로 브리프를 다시 만들고 벤더·기사가 전한 기능·성능 주장(f13·f14·f16·f17)을 모두 vendor_claim: true·태그 추정·evidence_excerpt 첫머리 '벤더 주장: '으로 냈다. 새 브리프의 f15 는 기사(ref-1057)의 정부 협력 사실 보도로 벤더 문서가 아니며 신뢰도 low 로 두었다. 직전 브리프와 finding 번호·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 5회/30, 신규 출처 15건/15(ref-1045~ref-1059, 예약 구간 안)로 출처 상한 도달. 원문 열람: 15건 모두 열었다(webfetch 14건, github_raw 1건). 논문은 초록 페이지다. 교차 확인 0건. 분류 원문 핵심 질문에는 f18 로 답했고 결론은 '로봇 기반 모델은 로봇 쪽 기능을 학습된 범용 정책으로 바꾸고, 언어 모델은 지시·분해·배정의 입력을 바꾸되 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 방향'이라는 추정이다. 현장 유형 사례는 가정(f4)·제조 공장(f11 벤치마크, f13·f14 벤더 주장)·물류창고(f16·f17 국내, 벤더 주장)다. 국내 자료는 지디넷코리아(ref-1057)·헬로티(ref-1059) 두 건이다. 교차 규칙에 따라 이 영역의 L. AI·학습 기술 내용은 적용 대상인 25. 작업 배정 — MRTA(f10)와 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션(f7~f9)에 함께 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 VLA·LLM 에이전트·LLM-모듈로·PDDL·등각 예측·불확도 정렬·작업 분해·어포던스·연합 형성은 후보로 내지 않았다. 입력 누락: runs/2026-09-30-07/research.json(직전 반환값) 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획"
type: area
category: "L. AI·학습 기술"
area_no: 44
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 44. 로봇 기반 모델·언어 모델 계획

# 44. 로봇 기반 모델·언어 모델 계획

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]

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

### docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md (요약)

```markdown
# 45. 문서·도면·장면 이해

소속 대분류: L. AI·학습 기술 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **문서·도면 해석 AI**: 매뉴얼과 도면을 해석하는 모델을 다룬다
- **플랫폼 수준 장면 인식**: 고정 카메라와 여러 로봇의 인식 결과를 모아 공간 상태를 인식한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
```

### docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md (요약)

```markdown
# 46. 예측·학습 기반 최적화

소속 대분류: L. AI·학습 기술 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

학습 기반 배정·경로, 수요·고장 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **학습 기반 배정·경로**: 강화학습 같은 학습 방법으로 배정과 경로를 정한다
- **수요·고장 예측**: 일의 양과 고장을 예측해 계획과 정비에 쓴다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
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

### docs/open-questions.md (요약: 대상 영역 [44] 에 걸린 0건 / 전체 215건)

```markdown
없음
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

### runs/2026-09-30-06/research.md

```markdown
# 리서치 브리프 2026-09-30-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-06 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 43. 데이터·관측성·배포 |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 관측성, OpenTelemetry, MCAP, FinOps·FOCUS, A/B 분할 업데이트 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(운영 로그 기반 실패 분석)·물류창고(배포 전 시뮬레이션 검증) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 기록 형식, 추적·지표·로그 수집, 컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 비용 계측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — rosbag2·MCAP, ros2_tracing, OpenTelemetry, Mender, FOCUS 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
2. 로봇·플랫폼의 로그·이벤트·텔레메트리를 기록·저장하는 형식과 도구(rosbag2·MCAP, 플랫폼 기록 DB)는 무엇이며, 보존 기간을 정하는 국내 규제 근거는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
3. 플랫폼 관측성을 구현하는 표준·오픈소스(OpenTelemetry, ros2_tracing, 커널 기반 관찰)는 무엇이며 관찰 자체의 성능 부담은 얼마로 보고되는가? (섹션 6·7·8 겨냥)
4. 현장 서버·로봇·클라우드에 플랫폼 소프트웨어를 배포하고 되돌리는 방법(컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 배포 전 시뮬레이션 검증)은 무엇이며 어떤 결과가 보고되는가? (섹션 6·7·8 겨냥)
5. 클라우드와 언어 모델 호출 비용을 측정·할당·관리하는 기준(FinOps 주기, FOCUS 청구 데이터 명세, OpenTelemetry 생성형 AI 토큰 지표)은 무엇인가? (섹션 4·6·7 겨냥)
6. 병원·물류창고 등 현장에서 운영 데이터를 수집해 실패 원인을 분석하거나 소프트웨어 변경을 배포 전에 검증한 사례는 무엇인가? (섹션 5 겨냥)
7. 데이터·관측성·배포에서 ROP가 직접 맡을 것과 로봇 제조사·클라우드 사업자·법규에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Bédard·Lütkebohle·Dagenais 의 ros2_tracing(IEEE RA-L 7(3), 2022-07)은 저부하 추적기 LTTng 를 써서 ROS 2 의 실행 정보를 수집하는 계측·추적 도구 모음으로, ROS 2 추적 데이터를 운영체제 추적과 결합할 수 있고, ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f2 | [사실] | ros2_tracing 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목에 관한 정보가 충분하지 않다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f3 | [사실] | Yu·Lee·Choi·Park 의 ros2probe(arXiv 2606.10746, 2026-06)는 ROS 2 도메인에 구독자로 참여하는 관찰 도구가 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다고 보고, 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰하는 방식으로 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고, 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 메시지 손실 0을 보고했다. | ref-1039 | 아니오 | medium | 2026-06 | — | — |
| f4 | [사실] | ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식을 sqlite3 에서 MCAP 로 바꿨고, 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능이 더해졌다. | ref-1040, ref-1041 | 예 | high | 2023-05-23 | — | — |
| f5 | [추정] | Foxglove 는 MCAP 이 SQLite3 의 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고, zstd·lz4 압축을 고를 수 있으며, 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 주장한다. | ref-1041 | 아니오 | low | 2022-12-22 | — | 벤더 주장 |
| f6 | [사실] | OpenTelemetry 명세 상태 요약에 따르면 추적(tracing)은 API·SDK·프로토콜이 모두 안정(stable)이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표(metrics)는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일(profiles)은 프로토콜이 개발(development) 단계다. | ref-1042 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenTelemetry 생성형 AI 의미 규약 저장소의 토큰 지표 문서는 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터(gen_ai.client.inference.usage.*)와 호출별 입력·출력 토큰 히스토그램(gen_ai.client.inference.operation.*)을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 두며, 모든 지표가 개발(Development) 단계다. | ref-1043 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | 오픈소스 ros-opentelemetry 는 송신 측이 추적 문맥을 ROS 2 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 이어 붙이는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다. | ref-1044 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Zhang·Yu·Westerlund(Sensors, 2025-08)는 TurtleBot4 에 얹은 Jetson Nano 5대를 작업 노드로, 노트북 1대를 마스터로 둔 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB 상대 위치 추정을 운영했고, 오차 보정용 LSTM 파드 5개를 모두 종료시킨 경우에도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다고 보고했다. | ref-1045 | 아니오 | medium | 2025-08-14 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: 오픈소스 Mender 는 임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선(OTA) 업데이트 관리자로, 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 해 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있게 하며, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다. | ref-1046 | 아니오 | medium | 2026-09-30 | — | — |
| f11 | [사실] | 개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행) 제8조는 개인정보처리자가 개인정보취급자의 개인정보처리시스템 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관·관리하고, 월 1회 이상 점검하며, 위조·변조·도난·분실되지 않도록 안전하게 보관하게 한다. | ref-766 | 아니오 | medium | 2023-09-22 | 제약 | — |
| f12 | [사실] | FinOps 재단의 FinOps 프레임워크는 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보(Inform), 사용량 최적화와 요금 최적화를 찾는 최적화(Optimize), 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영(Operate)의 세 단계를 반복하는 방식으로 설명하며, 대상 기술 범주에 공용 클라우드·SaaS 와 함께 AI 서비스를 든다. | ref-1048 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | FinOps 재단의 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화(PricingCurrency 등), 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다. | ref-1049 | 아니오 | medium | 2025-05-29 | — | — |
| f14 | [사실] | Bruno·Sim·Hagiwara(arXiv 2609.29043, 2026-09)는 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다고 보고, 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높였으며 클라우드 모델(Claude Sonnet 4.6)과 함께 비교했다. | ref-1051 | 아니오 | medium | 2026-09 | 예외·성과 | — |
| f15 | [사실] | 고려대학교 구로병원의 자율 약품 배송 로봇 실증(Lee 외, Digital Health, 2026-03)에서 배송 임무는 응급실 직원이 웹 애플리케이션으로 요청하면 시작됐다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 시작 조건 | — |
| f16 | [사실] | 같은 병원 실증은 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 넘겨 간호사가 받는 것을 배송 성공으로 정의했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 완료·인계 | — |
| f17 | [사실] | 같은 병원 실증은 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자가 적은 수기 기록지(탑승객·화물·결과)를 함께 모아 분석했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 작업 대상 | — |
| f18 | [사실] | 같은 병원 실증에서 전체 배송 성공률은 87.03%, 승강기 가동률 59% 미만일 때 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었으며, 승강기 가동률이 높을수록 실패가 많았다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f19 | [추정] | Ocado 는 물류창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 초당 10회 로봇 통신 같은 실제 운영 데이터로 모델을 다듬으며, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. | ref-1052 | 아니오 | low | 2025-06-04 | 물류창고 / 예외·성과 | 벤더 주장 |
| f20 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다. | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에 대해, 데이터는 자기 기술형 기록 형식(MCAP)과 플랫폼 기록 DB 로 남기고(f4·f20), 상태는 OpenTelemetry 의 추적·지표·로그로 플랫폼 서비스를 관찰하면서 로봇 내부 실행은 저부하 추적·커널 필터로 교란 없이 보며(f1·f3·f6·f8), 배포는 컨테이너 오케스트레이션의 자동 재시작과 이미지 기반 A/B 롤백, 배포 전 시뮬레이션 검증을 조합하고(f9·f10·f19), 비용은 표준 청구 데이터(FOCUS)와 토큰 지표를 FinOps 주기로 관리하는 조합이 공개 자료의 공통 형태로 보인다(f7·f12·f13). | ref-1040, ref-762, ref-1038, ref-1039, ref-1042, ref-1044, ref-1045, ref-1046, ref-1052, ref-1043, ref-1048, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 미들웨어 기록만으로는 내부 병목을 알 수 없고(f2) 관찰 도구 자체가 시스템을 교란할 수 있으며(f3), 병원 실증처럼 실패 원인이 로봇·승강기 로그를 함께 모아야 드러나고(f17·f18), 클라우드 언어 모델 호출 비용이 반복 작업에서 누적되며(f14), 개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 지기 때문이다(f11). | ref-1038, ref-1039, ref-943, ref-1051, ref-766 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 43. 데이터·관측성·배포에서 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책(f6·f11), 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스(f4·f8·f17), 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증(f9·f19), 클라우드·언어 모델 호출 비용의 계측·배분(f7·f13)이다. | ref-1042, ref-766, ref-1040, ref-1044, ref-943, ref-1045, ref-1052, ref-1043, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 운영체제·펌웨어의 무선 업데이트와 로봇 내부 ROS 2 실행 추적(f1·f10)은 로봇 제조사에, 클라우드 청구 데이터 생성(f13)은 클라우드 사업자에, 승강기 통신 로그(f17)는 설비 제어 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 내는 기록·업데이트 상태·청구 데이터를 받아 모으는 인터페이스를 맡을 것으로 보인다. | ref-1038, ref-1046, ref-1049, ref-943 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 실행 기록을 보여 주는 37. 관제 화면·실행 기록(f17·f20), 로그로 원인을 찾는 38. 모니터링·이상 탐지·원인 분석(f2·f18), 성과 지표의 39. 운영 성과 측정·개선(f18), 컨테이너·DDS 통신의 42. 분산 시스템·통신·컴퓨팅 구조(f9), 기록 DB 를 두는 41. 플랫폼 아키텍처·외부 API(f20), 업데이트·버전의 57. 자산·소프트웨어 수명주기 관리(f10), 배포 전 검증의 54. 시험·형식 검증·벤치마크와 34. 시뮬레이션·예측용 디지털 트윈(f19), 접속기록의 53. 개인정보·영상 데이터와 52. 통신 보호·위협 관리·감사(f11), 비용의 3. 경제성·조달·사업 모델(f12·f13), 언어 모델 비용의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영·13. 대화형 기능의 신뢰·기반(f7·f14), 승강기 로그의 22. 설비·건물 시스템 연동(f17), 적용 현장인 63. 병원·의료(f15~f18)·61. 물류창고(f19)와 이어진다. | ref-943, ref-762, ref-1038, ref-1045, ref-1046, ref-1052, ref-766, ref-1048, ref-1049, ref-1043, ref-1051 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1038 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2201.00393 | 아니오 |
| ref-1039 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.10746 | 아니오 |
| ref-1040 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 아니오 |
| ref-1041 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | 벤더 문서 | medium | 2026-09-30 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 아니오 |
| ref-1042 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://opentelemetry.io/docs/specs/status/ | 아니오 |
| ref-1043 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 아니오 |
| ref-1044 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/szobov/ros-opentelemetry | 아니오 |
| ref-1045 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 아니오 |
| ref-1046 | Northern.tech (mendersoftware) | mender — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/mendersoftware/mender | 아니오 |
| ref-766 | 개인정보보호위원회 (국가법령정보센터) | 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호) | 2023-09-22 | 정부·연구기관 | high | 2026-09-30 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 아니오 |
| ref-1048 | FinOps Foundation | FinOps Phases | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.finops.org/framework/phases/ | 아니오 |
| ref-1049 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 미확인 | 표준 | medium | 2026-09-30 | https://www.finops.org/insights/focus-1-2-available/ | 아니오 |
| ref-943 | Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-1051 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.29043 | 아니오 |
| ref-1052 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies | 2025-06-04 | 벤더 문서 | medium | 2026-09-30 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 관측성·실행 추적 f1·f2, MCAP f4·f5(벤더 주장 병기), OpenTelemetry f6, 토큰 지표 f7, A/B 분할 업데이트 f10, FinOps·FOCUS f12·f13 / 섹션 5: 병원 — f15(시작 조건)·f16(완료·인계)·f17(작업 대상: 로봇·승강기 로그 정보)·f18(예외·성과), 물류창고 — f19(배포 전 시뮬레이션 검증, 벤더 주장 병기). 제조 공장·상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 기록 f4·f20, 관찰 f1·f3·f6·f8, 배포 f9·f10·f19, 비용 f7·f12·f13·f14 / 섹션 7: rosbag2·MCAP f4·f5, ros2_tracing f1, ros2probe f3, OpenTelemetry f6·f7, ros-opentelemetry f8, K3s f9, Mender f10, FOCUS f13, 개인정보 고시 f11 / 섹션 8: f1·f3·f9·f14·f15~f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3·f17·f18 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 관측성 | Observability | 시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다. |
| 오픈텔레메트리 | OpenTelemetry (OTel) | 추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다. |
| MCAP | MCAP | 여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다. |
| 핀옵스 | FinOps | 클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 38. 모니터링·이상 탐지·원인 분석 | 근거: f8 | 종류: 일반
- 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반
- OpenTelemetry 생성형 AI 토큰 지표가 개발 단계에서 이름이 바뀌고 있는데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 관련 영역: 43. 데이터·관측성·배포, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리 | 근거: f10 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - f1·f3·f14 는 논문 초록(또는 HTML 일부) 기준이며 본문 실험 조건 미확인
    - f7: 검색 결과 요약의 다른 문서들은 gen_ai.client.token.usage 히스토그램을 설명하지만, 열어 본 현재 저장소는 gen_ai.client.inference.usage.* 로 정의함. 이름 변경 시점과 이전 이름의 폐기 여부 미확인
    - f11 의 '5만 명 이상' 조건 문구는 검색 요약으로 보완했고 법령 페이지 요약에서는 1년/2년 구분만 확인
    - f13 FOCUS 1.2 명세 본문(PDF) 미열람, 발표 글만 열람
    - f8 ros-opentelemetry 라이선스·유지 주체 미확인(개인 관리 저장소)
    - ref-1049·ref-1052 제목 일부는 검색 결과 제목 기준
    - Zampetti 외 CPS CI/CD 인터뷰 연구(ACM TOSEM 2023)는 ACM 403·PDF 본문 추출 실패로 넣지 않음
    - Docker·Kubernetes 기반 ROS 설계 흐름 논문(ACM 10.1145/3594539)은 403 으로 넣지 않음
    - 실외이동로봇 운행안전인증에서 관제·소프트웨어 원격 업데이트 시 변경 인증 필요 여부는 KIRIA 안내 페이지에 없어 확인하지 못함
    - 제조 공장·상업 시설·가정·실외 현장의 데이터·배포 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3: ROS 2 내부 실행 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓰고, 이종 제조사 로봇 내부 추적은 f24 에서 연계 대상으로 구분함
    - f10: 로봇 운영체제·펌웨어 OTA 는 로봇 제조사 영역이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 언어 모델 계획 자체는 44. 로봇 기반 모델·언어 모델 계획의 내용이며 이 영역에는 비용·지연 근거로만 제안함
    - f17: 승강기 통신 로그 생성은 설비 제어 쪽이며 ROP 는 수집·결합만 맡는 것으로 f24 에서 구분함
    - f19: 시뮬레이션·디지털 트윈 자체는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 내용이며 이 영역에는 배포 전 검증 근거로만 제안함. 18. 실시간 세계 상태·데이터 일관성과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 22회/30, 신규 출처 15건/15(출처 상한 도달). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1032 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-04·2026-09-30-05)가 ref-1032~ref-1037 을 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1038~ref-1052 를 순서대로 썼다. 재사용 1건(ref-762, 이전 브리프 2026-09-30-05 재인용, 이번에 다시 열지 않음; 값은 그 브리프의 출처 표를 따랐고 참고문헌 목록 전체는 입력에 없음). 원문 열람: 신규 15건 모두 열었다(webfetch 11건, github_raw 4건). 논문 가운데 Zhang 외(ref-1045)·Lee 외(ref-943)는 PMC 본문을, 나머지는 초록 페이지를 열었다. 교차 확인 1건(f4: ROS 2 공식 릴리스 노트와 Foxglove 블로그). 벤더 문서만 근거로 한 f5·f19 는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에는 f21 로 답했고 결론은 '자기 기술형 기록 형식과 기록 DB + OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적 + 컨테이너 자동 재시작·A/B 롤백·배포 전 시뮬레이션 검증 + 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기'라는 추정이다. 현장 유형 사례는 병원(f15~f18, 국내 고려대학교 구로병원)·물류창고(f19, 벤더 주장)뿐이다. 국내 자료는 개인정보보호위원회 고시(ref-766)와 국내 병원 실증 논문(ref-943) 두 건이다. L. AI·학습 기술 관련 f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안했다. 용어집에 이미 있는 분산 추적·백 파일·무선 업데이트·서비스 수준 협약·감사 추적·모델 레지스트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### runs/2026-09-30-05/research.md

```markdown
# 리서치 브리프 2026-09-30-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-05 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 41. 플랫폼 아키텍처·외부 API |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 클라우드 로보틱스, 온프레미스(현장) 클라우드, OpenAPI, AsyncAPI, 웹훅, 이벤트 기반 아키텍처 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·제조 공장·물류창고·기타 현장의 아키텍처 배치 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 클라우드·현장 서버·로봇 역할 분담, 계산 오프로딩, 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, REST·이벤트·SDK 조합 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF(rmf-web API 서버·rmf_api_msgs), VDA 5050 전송 구조, OpenAPI, AsyncAPI, RoMi-H, FogROS2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]
2. 클라우드·현장(온프레미스) 서버·로봇 사이의 계산·판단 배치를 다룬 연구와 오픈소스(클라우드 로보틱스, 계산 오프로딩, 현장 클라우드 기준 아키텍처)는 무엇이며 어떤 결과를 보고하는가? (섹션 3·6·8 겨냥)
3. 제조사 중립적인 플랫폼 기준 아키텍처(서비스 분리, 이벤트 구조, 제조사 어댑터 계층)는 Open-RMF·RoMi-H·VDA 5050 에서 어떻게 구성되는가? (섹션 6·7 겨냥)
4. 외부 시스템과 개발자에게 여는 API·웹훅·SDK 를 기계가 읽을 수 있게 기술하는 표준(OpenAPI, AsyncAPI)과 오픈소스·제품의 제공 형태(REST, 이벤트 스트림, 인증·권한)는 무엇인가? (섹션 4·6·7 겨냥)
5. 병원·제조 공장·물류창고·기타 현장(국내 포함)에서 플랫폼을 어디에 두고 무엇을 외부에 열었는지 보여 주는 사례는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)
6. 클라우드 장애·네트워크 품질 저하가 역할 분담 결정에 주는 제약과 대응 방법은 무엇인가? (섹션 3·6·11 겨냥)
7. 플랫폼 아키텍처·외부 API 에서 ROP가 직접 맡을 것과 로봇 자체 지능·업무 시스템·클라우드 인프라에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 Open-RMF 배치와 웹 대시보드·외부 클라이언트 사이에 REST 엔드포인트를 두고 그 정의를 서버의 /docs 경로에 OpenAPI 형식 문서로 제공하며, 기록용 데이터베이스는 tortoise-orm 으로 PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다(기본값은 메모리 SQLite). | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | rmf-web API 서버는 OpenID Connect 로 발급된 JWT 접근 토큰을 독립적으로 검증해 사용자를 식별하고, 사용자–역할–권한 그룹의 3단 구조(역할이 그룹에 대한 동작을 허용하고 자원은 그룹에 속함)로 접근을 통제하며 관리자는 모든 그룹에 모든 동작을 할 수 있다. | ref-762 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f3 | [사실] | Open-RMF 의 rmf_api_msgs 는 C++·Python 으로 된 RMF 구성 요소와 웹 인터페이스 사이를 잇는 JSON 메시지 스키마 모음으로, 작업 요청·예약, 작업 상태, 플릿 상태 스키마를 담고 스키마에서 타입 있는 데이터 모델을 생성할 수 있게 한다. | ref-1033 | 아니오 | medium | 2026-09-30 | — | — |
| f4 | [사실] | Open-RMF 핵심 구조는 모든 플릿 관리자가 예상 경로를 보고하는 중앙 교통 일정 데이터베이스와 충돌 시 플릿 관리자 간 협상을 두고, 제조사 고유 API 를 표준 인터페이스로 잇는 플릿 어댑터를 제어 수준(Full Control·Traffic Light·Read Only·No Interface)으로 나누며, 재사용 가능한 C++ API(파이썬 바인딩 포함)는 Full Control 에만 있다. | ref-004 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f5 | [사실] | VDA 5050 3.0.0 은 플릿 관제와 이동 로봇 사이의 제조사 중립 인터페이스로 MQTT 3.1.1 이상과 JSON 을 쓰고, 주제를 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조(예 vda5050/v3/…/order)로 정하며 order·instantActions·state·visualization·connection·factsheet·responses·zoneSet 주제를 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 명세는 플릿 관제–이동 로봇 통신과 무관한 인터페이스, 곧 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스를 범위 밖으로 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenAPI 명세 3.1.0(2021-02-15)은 사람과 컴퓨터가 서비스의 기능을 발견·이해하게 하는 HTTP API 의 언어 중립 표준 인터페이스 기술 형식이며, 3.1.0 에서 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드가 새로 들어갔다. | ref-1028 | 아니오 | medium | 2021-02-15 | — | — |
| f8 | [사실] | AsyncAPI 명세 3.1.0 은 메시지 기반 API 를 기계가 읽을 수 있게 기술하는 프로토콜 중립 형식으로 MQTT·AMQP·WebSocket·Kafka·HTTP 등에 쓰이며, 채널·동작(send/receive)·메시지·서버(브로커)·프로토콜별 바인딩을 핵심 객체로 두고 Apache 2.0 라이선스로 공개된다. | ref-1027 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Ichnowski 외의 FogROS2(arXiv 2205.09778, 2023-04 개정)는 연산 능력이 제한된 로봇이 ROS 2 노드를 AWS·GCP·Azure 같은 원격 클라우드로 옮겨 실행하게 하는 ROS 2 배포판 포함 플랫폼으로, SLAM 지연 50% 감소, 파지 계획 14초→1.2초, 모션 계획 45배 가속, 영상 압축으로 이미지 전송 지연 97% 개선을 보고했다. | ref-304 | 아니오 | medium | 2023-04 | 예외·성과 | — |
| f10 | [사실] | Chen 외의 FogROS2-FT(IROS 2024)는 클라우드 제공자 장애, 네트워크 서비스 품질(QoS) 변동, 신뢰성 높은 인스턴스의 비용을 클라우드 로보틱스의 약점으로 보고, 상태 없는 로봇 서비스를 여러 클라우드에 복제해 가장 먼저 온 응답을 쓰는 방식으로 모션 계획 P99 지연을 최대 5.53배 줄이고 비용을 최대 2.2배 낮췄다고 보고했다. | ref-1037 | 아니오 | medium | 2024-12 | 예외·성과 | — |
| f11 | [사실] | 독립된 두 연구(Singhal 외 2017, Brorsson 외 2025)는 모두 로봇 밖의 중앙 계산 자원(클라우드 또는 현장 클라우드)이 플릿 조율·전역 계획을 맡고 각 로봇이 국지 주행 같은 온보드 자율 기능을 유지하는 혼합 구조를 제시한다. | ref-1032, ref-308 | 예 | medium | 2025-12 | 수행 자원 | — |
| f12 | [사실] | Brorsson 외(arXiv 2512.15215, 2025-12)의 RAIL 기준 아키텍처는 사내 물류 이동 로봇을 위해 설비에 단 외부 센서·계산 자원(기반 시설), 지연·연결 문제를 다루는 현장 클라우드(on-premise cloud), 로봇 온보드 자율의 세 층을 두며, 대형 상용차 제조 현장 실배치와 사용자 경험 평가로 이를 보였다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 수행 자원 | — |
| f13 | [사실] | 싱가포르 창이종합병원 CHART 의 RoMi-H(Robotic Middleware for Healthcare)는 OMG DDS 를 쓰는 미들웨어로 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리와 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·ICT 시스템용 API)의 네 영역으로 구성되며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. | ref-937 | 아니오 | medium | 2026-09-30 | 병원 / 수행 자원 | — |
| f14 | [추정] | 네이버는 로봇 안이 아니라 클라우드에서 연산·판단을 하는 브레인리스 로봇 구조의 ARC(AI-Robot-Cloud)를 이동 계획·위치 추정·작업 수행과 기반 시설 연동을 맡는 ARC brain, 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정하는 ARC eye, 웹 개발자가 로봇 서비스를 만들게 하는 웹 기반 OS 인 ARC mind 로 나누고, 제2사옥 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. | ref-1025 | 아니오 | low | 2026-09-30 | 기타 / 수행 자원 | 벤더 주장 |
| f15 | [추정] | MiR 은 MiR Fleet Enterprise 가 Windows Server 에서 돌며 가상화·클라우드 배치를 지원하고, ERP·MES·WMS 연동용 REST API 와 이벤트 기반 아키텍처를 갖추며, IEC 62443-4-2(SL-C 3)에 맞춰 단일 로그인·감사 기록·세분화된 사용자 권한을 제공한다고 주장한다. | ref-774 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f16 | [추정] | InOrbit 개발자 문서는 로봇 데이터 조회·원격 동작·미션 추적·감사 기록용 REST·스트리밍 API, 사고 관리용 외부 발신 웹훅과 수신 API, 서비스 사용자와 역할 기반 권한에 묶인 API 키, 로봇에 넣는 Robot SDK(C++·Python)와 현장 애플리케이션 연동용 Edge SDK, 임베드 가능한 대시보드를 제공한다고 적는다. | ref-1034 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [추정] | 물류창고 피킹에서 Locus Robotics 는 LocusONE 플랫폼이 API 로 창고 관리 시스템(WMS)과 연결돼 WMS 에서 주문을 받아 피킹 효율을 기준으로 최적화한 뒤 로봇 작업으로 내린다고 주장한다. | ref-1036 | 아니오 | low | 2026-09-30 | 물류창고 / 시작 조건 | 벤더 주장 |
| f18 | [추정] | 같은 Locus Robotics 자료는 피킹 완료 확인을 WMS 로 즉시 되돌려 보내고 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 같은 운영 성과 데이터를 제공한다고 주장한다. | ref-1036 | 아니오 | low | 2026-09-30 | 물류창고 / 완료·인계 | 벤더 주장 |
| f19 | [추정] | 뉴스핌(2026-05-12) 보도에 따르면 카카오모빌리티는 로봇–인프라–사용자를 잇는 플랫폼으로 서비스 요청을 로봇 실행 단위로 바꾸는 작업 추상화, 이종 로봇이 통신하게 하는 통합 API 인 제어 인터페이스, 고장 감지 시 다른 로봇으로 작업을 넘기는 재배정, 건물 인프라와 ERP·물류 자동화 시스템을 잇는 연동 기반을 추진한다. | ref-1029 | 아니오 | low | 2026-05-12 | — | 벤더 주장 |
| f20 | [추정] | 로봇신문 보도에 따르면 클로봇은 다중 로봇 통합관제 플랫폼 CROMS 가 서로 다른 제조사 로봇 50대 이상을 동시에 제어하고 승강기 연동으로 다층 건물에서 운용할 수 있으며 국내 첫 이기종 로봇 통합관제 솔루션이라고 밝힌다. | ref-870 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에 대해, 국지 주행·즉각적 안전 반응은 로봇에, 지연·연결에 민감한 플릿 조율·교통·설비 연동은 현장 서버(현장 클라우드)에, 무거운 계산 오프로딩과 여러 현장 집계·개발자 서비스는 클라우드에 두는 혼합 배치가 연구·오픈소스의 공통 형태이고(f4·f9·f11·f12·f14), 외부에는 동기식 REST(OpenAPI 로 기술)와 이벤트·메시지 API(AsyncAPI·웹훅), SDK 를 인증·권한 통제와 함께 여는 조합이 쓰이는 것으로 보인다(f1·f2·f7·f8·f16). | ref-004, ref-304, ref-1032, ref-308, ref-1025, ref-762, ref-1028, ref-1027, ref-1034 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇–관제 표준(VDA 5050)이 업무 IT 시스템·설비와의 인터페이스를 범위 밖에 두고(f6) 제조사 관제마다 자체 REST API 를 따로 내므로(f15·f17) 이종 로봇을 묶는 플랫폼의 외부 API 가 업무 시스템과 개발자가 만나는 단일 접점이 되며, 클라우드 장애·네트워크 품질 변동(f10)이 있어 판단을 어디에 두느냐가 운영 연속성을 좌우하기 때문이다. | ref-031, ref-774, ref-1036, ref-1037 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 41. 플랫폼 아키텍처·외부 API 에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처(f4·f13), 작업 요청·작업 상태·플릿 상태의 기계가독 스키마(f3), REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기(f5·f7·f8), API 호출의 인증·권한(f2), 판단·데이터를 로봇·현장 서버·클라우드 중 어디에 둘지 정하는 배치 정책이다. | ref-004, ref-937, ref-1033, ref-031, ref-1028, ref-1027, ref-762 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능(f9·f11)은 로봇 제조사에, 주문·재고 같은 업무 판단(f17)은 상위 업무 시스템(WMS·ERP)에, 클라우드 제공자 인프라와 현장 네트워크(f10·f17)는 클라우드 사업자와 42. 분산 시스템·통신·컴퓨팅 구조 영역에 속하므로, ROP 는 이들을 부르고 받는 인터페이스와 배치 결정을 맡을 것으로 보인다. | ref-304, ref-1032, ref-1036, ref-1037 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 현장 네트워크·연결 끊김 운영을 다루는 42. 분산 시스템·통신·컴퓨팅 구조(f10·f12), 기록 DB·감사 기록·배포를 다루는 43. 데이터·관측성·배포(f1·f16), 플릿 어댑터를 다루는 20. 로봇·제조사 관제 연동(f4·f15), VDA 5050 을 다루는 21. 상호운용 표준·적합성(f5·f6), 승강기·기반 시설 연동의 22. 설비·건물 시스템 연동(f13·f14·f20), WMS·ERP 연동의 23. 업무 시스템 연동(f15·f17·f18), API 인증·권한의 51. 인증·권한·격리(f2·f16), IEC 62443 을 다루는 52. 통신 보호·위협 관리·감사(f15), 대시보드의 37. 관제 화면·실행 기록(f1·f16), 재배정의 32. 예외 복구·재계획·업무 연속성(f19), 업체 동향의 1. 기술·시장·업체 동향(f14·f19·f20), 적용 현장인 61. 물류창고(f17)·62. 제조 공장(f12)·63. 병원·의료(f13)·67. 기타 현장(f14)과 이어진다. | ref-1037, ref-308, ref-762, ref-1034, ref-004, ref-774, ref-031, ref-937, ref-1025, ref-870, ref-1036, ref-1029 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-304 | Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2205.09778 | 아니오 |
| ref-1025 | NAVER Corp. | 로보틱스 l NAVER Corp. | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.navercorp.com/tech/robotics | 아니오 |
| ref-937 | Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology) | ROMI-H | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.cgh.com.sg/chart/projects/romi-h | 아니오 |
| ref-1027 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 미확인 | 표준 | high | 2026-09-30 | https://www.asyncapi.com/docs/reference/specification/v3.1.0 | 아니오 |
| ref-1028 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 2021-02-15 | 표준 | high | 2026-09-30 | https://spec.openapis.org/oas/v3.1.0 | 아니오 |
| ref-1029 | 뉴스핌 | 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 … (제목 일부만 확인) | 2026-05-12 | 기사 | low | 2026-09-30 | https://www.newspim.com/news/view/20260512001077 | 아니오 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 … (제목 일부만 확인) | 미확인 | 기사 | low | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 아니오 |
| ref-308 | Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2512.15215 | 아니오 |
| ref-1032 | Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv) | Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform | 2017-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1706.08931 | 아니오 |
| ref-1033 | Open Robotics (open-rmf) | rmf_api_msgs — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs | 아니오 |
| ref-1034 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://developer.inorbit.ai/docs | 아니오 |
| ref-774 | Mobile Industrial Robots (MiR) | MiR Fleet | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://mobile-industrial-robots.com/products/software/mir-fleet | 아니오 |
| ref-1036 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://locusrobotics.com/locusone/automated-warehouse-software/integrations | 아니오 |
| ref-1037 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 2024-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2412.05408 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(업무 시스템 인터페이스가 로봇–관제 표준 밖이고 클라우드 장애가 배치를 좌우), f21(핵심 질문 답, 추정) / 섹션 4: 클라우드 로보틱스·오프로딩 f9, 현장 클라우드 f12, OpenAPI·웹훅 f7, AsyncAPI f8, 플릿 어댑터·제어 수준 f4 / 섹션 5: 병원 — f13(창이종합병원 RoMi-H), 제조 공장 — f12(대형 상용차 제조 현장 RAIL), 물류창고 — f17(시작 조건: WMS 주문 수신)·f18(완료·인계: 확인 회신, 벤더 주장 병기), 기타 — f14(네이버 1784 사옥 ARC, 벤더 주장 병기). 여섯 항목 중 제약·예외 근거가 사례별로 부족함을 명시 / 섹션 6: 역할 분담 f11(교차 확인)·f12·f14, 계산 오프로딩 f9, 다중 클라우드 장애 대응 f10, 제조사 중립 어댑터 계층 f4·f13, REST·이벤트·SDK 조합 f1·f5·f16, 인증·권한 f2, 제품 사례 f15·f19·f20(벤더 주장 병기) / 섹션 7: Open-RMF f1~f4, VDA 5050 f5·f6, OpenAPI f7, AsyncAPI f8, RoMi-H f13, FogROS2 f9·f10 / 섹션 8: f9~f12 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조 페이지에 f10·f12 반영, 20. 로봇·제조사 관제 연동 페이지에 f15·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| OpenAPI 명세 | OpenAPI Specification (OAS) | HTTP API 의 경로·요청·응답·보안 방식을 사람과 컴퓨터가 함께 읽을 수 있게 기술하는 언어 중립 표준 형식으로, 3.1.0 부터 웹훅도 기술한다. |
| AsyncAPI 명세 | AsyncAPI Specification | MQTT·AMQP·WebSocket·Kafka 같은 메시지 기반 API 의 채널·동작·메시지·브로커를 기계가독 형식으로 기술하는 프로토콜 중립 명세다. |
| 웹훅 | Webhook | 어떤 사건이 일어났을 때 서비스가 미리 등록된 외부 URL 로 HTTP 요청을 보내 알리는 방식의 이벤트 전달 인터페이스다. |
| 클라우드 로보틱스 | Cloud Robotics | 로봇이 인터넷으로 연결된 원격 계산·저장 자원에 계산이나 데이터를 맡겨 온보드 능력의 한계를 보완하는 구조와 연구 분야다. |

## 열린 질문

새로 생긴 질문:

- 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드나 5G 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f14 | 종류: 일반
- 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 57. 자산·소프트웨어 수명주기 관리 | 근거: f5 | 종류: 일반
- 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반
- 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f9 FogROS2 모션 계획 가속 배수: arXiv 개정판 초록은 45배, 검색 요약의 ICRA 2023 판 서술은 28배로 보여 판에 따라 다를 수 있음(ICRA 카메라 레디 PDF 는 열지 않음)
    - f9·f10·f11·f12 는 논문 초록 기준이며 본문 실험 조건 미확인
    - f14 네이버 1784 로봇 대수: 회사 페이지는 100여 대, 검색 요약의 기사 문구는 40여 대로 기준 시점이 다를 수 있으나 기사 원문을 열지 않아 출처 충돌로 확정하지 않음
    - f14 5G 특화망 사용은 검색 요약에만 나오고 ITDaily 기사 원문은 ECONNRESET 으로 열지 못해 넣지 않음
    - f15 MiR 페이지 안에서 지원 대수 표현('최대 100대'와 '100대 넘는 배치')이 엇갈림
    - ref-1029·ref-870 기사 제목 전체 미확인, ref-870 발행일 미확인
    - ref-1027 AsyncAPI 3.1.0 발행일 미확인
    - Kehoe 외 클라우드 로보틱스 조사 논문(IEEE T-ASE 2015)은 PDF 본문 추출 실패·eScholarship 빈 페이지로 넣지 않음
    - AWS IoT RoboRunner 의 현재 서비스 상태(종료 여부)는 확인하지 못해 넣지 않음
    - MiR Fleet Enterprise 문서 PDF 는 크기 초과로 열지 못함
    - 국내 클라우드 로봇 참조 구조 표준(TTA·KS)은 검색 1회에서 찾지 못함
- 범위 경계 위반 의심:
    - f9: FogROS2 의 SLAM·파지 계획 오프로딩은 로봇 자체 지능·제어 기능의 실행 위치 선택이므로 배치 방식의 근거로만 쓰고 ROP 직접 범위로 서술하지 않도록 f24 에서 구분함
    - f11: 국지 주행·장애물 회피는 로봇 자체 지능(연계 대상)으로, 전역 조율만 이 영역 근거로 씀
    - f14: 네이버 ARC 는 위치 추정·이동 계획까지 클라우드에 두어 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례이며 원문의 '경계는 제품 전략에 따라 이동할 수 있다'는 문장에 해당함
    - f17·f18: 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽이며 ROP 는 연동 인터페이스만 다룸
    - f24: 로봇 자체 지능·업무 시스템·클라우드 인프라를 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-762~ref-1037, 예약 구간 안)로 출처 상한에 도달해 더 넣지 못했다. 재사용 2건(ref-004·ref-031 은 github_raw 로 다시 열었다; 참고문헌 목록 전체가 입력에 없어 ref-004 의 값은 규칙 파일 예시, ref-031 의 값은 같은 날 이전 브리프 2026-09-30-04 의 출처 표를 따랐다). 원문 열람: 17건 모두 열었다(webfetch 12건, github_raw 5건). 논문은 초록 페이지다. 교차 확인 1건(f11, 두 arXiv 논문이라 신뢰도 medium). 벤더 문서·기사만 근거로 한 finding(f14~f20)은 모두 vendor_claim: true·태그 추정·'벤더 주장' 첫머리로 냈다. 분류 원문 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에는 f21 로 답했고 결론은 '로봇–현장 서버–클라우드 혼합 배치 + REST·이벤트 API·웹훅·SDK 를 인증·권한과 함께 여는 조합'이라는 추정이다. 현장 유형 사례는 병원(f13)·제조 공장(f12)·물류창고(f17·f18, 벤더 주장)·기타(f14, 사무 건물, 벤더 주장)이며 상업 시설·가정·실외 사례는 찾지 못했다. 국내 자료는 네이버(ref-1025)·뉴스핌(ref-1029)·로봇신문(ref-870) 세 건이고 국내 표준은 찾지 못했다. L. AI·학습 기술 관련 finding 은 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(네이버 ARC eye 의 디지털 트윈 언급은 위치 추정용 현재 상태 표현으로만 인용). 용어집에 이미 있는 포그 컴퓨팅·브레인리스 로봇·플릿 어댑터·플릿 제어 수준·MQTT·JSON 스키마·의미적 버전 관리·멱등성 키는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```
