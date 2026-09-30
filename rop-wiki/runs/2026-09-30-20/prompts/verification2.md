(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-20
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 19. 사람·보행자 모델 (E. 사물·사람·실시간 상태)
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

### runs/2026-09-30-20/target.json

```json
{
  "run_id": "2026-09-30-20",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 129,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 19,
    "area_name": "19. 사람·보행자 모델",
    "category": "E. 사물·사람·실시간 상태",
    "category_letter": "E"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=19"
}
```

### runs/2026-09-30-20/research.json

```json
{
  "run_id": "2026-09-30-20",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 19,
    "area_name": "19. 사람·보행자 모델",
    "category": "E. 사물·사람·실시간 상태"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 움직임 지도(Maps of Dynamics)·사회적 힘 모델·사람 궤적 예측·사회적 내비게이션·사람 표현(ROS4HRI) 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·상업 시설·실외·기타의 사람 흐름 반영 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 실시간 사람 검출·추적, 장기 시공간 흐름 지도, 단기 궤적 예측, 보행자 행동 모델(시뮬레이션), 운영 규칙 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — REP-155(ROS4HRI), HuNavSim, Open-RMF CrowdSim(Menge), 공개 데이터셋(THÖR·ATC) 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-256 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]",
    "사람의 위치·목적지·멈춤·교차를 표현하는 모델(움직임 지도, 궤적 예측, 사회적 힘 모델)에는 무엇이 있고 각각 무엇을 입력으로 받아 어디에 쓰는가? (섹션 4·6·8 겨냥)",
    "시간대·구역별 사람 흐름과 혼잡을 장기 관측으로 추정하는 방법과 그 효과를 로봇 경로·작업에 반영해 평가한 연구는 무엇인가? (섹션 6·8 겨냥)",
    "사람 정보를 로봇·시스템 사이에서 주고받는 공통 표현(ROS 규약 등)과 보행자 시뮬레이터·공개 데이터셋에는 무엇이 있는가? (섹션 7 겨냥)",
    "물류창고·병원·상업 시설·실외 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례는 무엇이며, 한국 사례(병원 로봇 운영, 공공 인파 밀집 관리)는 어떤가? (섹션 3·5 겨냥, 한국 자료 우선)",
    "oq-256 실제 운영 기록을 재생해 재현한 상황에서 조건을 바꿀 때 기록된 사람·다른 에이전트가 반응하지 않는 문제를 다른 분야(자율주행 시뮬레이션)는 어떻게 다루는가? (섹션 6·11 겨냥)",
    "사람·보행자 모델에서 ROP가 직접 맡을 것과 로봇 제조사(온보드 검출·국소 회피)·설비·공공 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Kucner 외(IJRR 42(11), 2023)의 서베이에 따르면 움직임 지도(Maps of Dynamics, MoD)는 환경의 전형적인 움직임 패턴을 저장하는 지도로, 궤적이나 짧고 끊긴 움직임 관측으로 만들 수 있으며 전역 경로 계획·위치 추정 개선·사람 움직임 예측에 쓰여 로봇이 감지 범위 밖과 미래의 움직임을 예상하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1204"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MoD 는 주어진 환경의 전형적 움직임 패턴에 관한 의미 정보를 저장하며, 일부는 궤적을, 일부는 짧고 끊긴 관측을 입력으로 쓴다. 용도: 전역 계획, 위치 추정 개선, 사람 움직임 예측(검색 요약 기준).",
      "as_of": "2023",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "Rudenko 외의 사람 움직임 궤적 예측 서베이(IJRR 2020)는 보행자 중심의 지상 2차원 궤적 예측 방법을 여러 연구 공동체에 걸쳐 정리하고, 움직임 모델링 방식과 사용하는 맥락 정보 수준이라는 두 축의 분류 체계를 제안하며 데이터셋과 성능 지표를 함께 검토한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1205"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 기존 방법을 'motion modeling approach and level of contextual information used' 로 분류하는 체계를 제안하고 데이터셋·지표를 검토한다(arXiv 초록 기준, 세부 분류 명칭은 미확인).",
      "as_of": "2019-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Helbing·Molnár(Physical Review E 51, 1995)의 사회적 힘 모델은 보행자 움직임을 원하는 속도로 가속하려는 항, 다른 보행자·경계와 거리를 두려는 반발 항, 끌림 항의 합으로 보고, 상호작용하는 군중 시뮬레이션에서 관측되는 집단 현상의 자기조직화를 재현한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1207"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원하는 속도로의 가속 항, 다른 보행자·경계와의 거리 유지 항, 끌림 항으로 구성되며 군중 시뮬레이션이 여러 집단 현상의 자기조직화를 현실적으로 묘사한다고 보고(검색 요약 기준).",
      "as_of": "1995-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "ROS REP-155(ROS4HRI, 2022-01-11 작성, 원문 상태 Draft)는 사람을 영속적인 person ID 와 추적 중에만 유효한 face·body·voice ID 의 조합으로 표현하고, /humans/persons/tracked 같은 토픽과 person_<ID> 좌표 프레임에 위치 신뢰도(1.0 지금 보임, 1 미만 이전에 보임, 0 추적된 적 없음)를 두며 아직 식별되지 않은 익명 사람도 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1206"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "REP 155 'Conventions, Topics, Interfaces for Perception in Human-Robot Interaction', 저자 Séverin Lemaignan, Status: Draft. person_<personID> 프레임에 location_confidence, /anonymous 하위 토픽.",
      "as_of": "2022-01-11",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "REP-155 에서 영속 person ID 는 얼굴 인식·음성 인식·옷 색 같은 신체 특징 기반 식별 노드가 부여해 세션을 넘어 같은 사람을 다시 알아보게 하므로, 사람 표현이 개인 식별 정보와 연결될 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1206"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "person ID 는 'normally assigned by a node able to perform person identification (face recognition node, voice recognition node, ...)' 이며 영속 UUID 로 세션 간 재인식에 쓰인다.",
      "as_of": "2022-01-11",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f6",
      "claim": "THÖR 데이터셋(Rudenko 외, RA-L 2020)은 실내 환경에서 사람 움직임 궤적과 시선 데이터를 모으고 위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표의 정답을 제공하며, 3차원 라이다 데이터와 공간을 주행하는 이동로봇을 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1208"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'accurate ground truth for position, head orientation, gaze direction, social grouping, obstacles map and goal coordinates', 3D 라이다·이동로봇 포함, 궤적 데이터셋 품질 지표(추적 지속 시간·노이즈 등) 제안.",
      "as_of": "2019-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "상업 시설 사례: 일본 오사카 ATC 쇼핑센터의 약 900㎡ 구역에 천장 3차원 거리 센서 49대를 두어 2012-10-24~2013-11-29 가운데 92일(매주 수·일요일 9:40~20:20) 보행자를 추적한 ATC 데이터셋은 시각·사람 id·x·y·높이·속도·이동 방향·몸 방향을 제공하며 연구 목적으로만 쓸 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1209"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "필드: 'time [ms], person id, position x [mm], position y [mm], position z (height) [mm], velocity [mm/s], angle of motion [rad], facing angle [rad]'. 공공 공간 사회적 로봇 연구(JST/CREST) 목적.",
      "as_of": "2026-09-30",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f8",
      "claim": "상업 시설 사례: Kidokoro 외(HRI 2013)는 쇼핑몰에서 사람을 모으는 로봇이 혼잡을 일으켜 지나가는 보행자의 보행 쾌적성을 해치는 문제에 대해, 보행자 행동 모델로 가상의 주행 상황을 시뮬레이션해 혼잡을 예상하고 미리 피하도록 계획하는 방법을 실제 쇼핑몰에서 시험해 영향을 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1218"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "세 능력: 보행자 혼잡 예상, 보행 쾌적성 이해, 혼잡을 미리 피하는 계획. 보행자 행동 모델을 결합해 가상 시나리오를 시뮬레이션, 실제 쇼핑몰 시험(검색 요약 기준, HRI 2013 최우수 논문상).",
      "as_of": "2013-03",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Vintr 외(Frontiers in Robotics and AI, 2022)는 대학 건물 복도(약 500㎡)에서 3차원 라이다로 한 달간(2019-03) 모은 600만 건 이상의 사람 검출로 FreMEn·HyperTime·GMM 등 20여 개 시공간 보행자 흐름 지도를 학습시키고, 경로 계획 시뮬레이션에서 예상 조우(Expected Encounters)와 예상 경로 길이로 비교해 공간과 시간을 따로 모델링한 방법(HyT×GMM 등)이 더 나았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1211"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "학습 2019-03 한 달, 시험 12월 7일, Velodyne HDL-32E 와 FLOBOT 추적. 지표 EE(방향이 충돌하는 조우 가중)·EL(경로 길이). 공간·시간 독립 모델링이 통합형보다 우수.",
      "as_of": "2022-07-04",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "같은 연구의 현장 실험(프랑스 UTBM 대학 홀, 2019-12-12~13, Toyota HSR, 40분 세션 네 번)에서 사람 흐름의 시간대 패턴을 따르는 예측형 주행은 두 세션 모두 불편을 드러낸 사람이 0명이었고 반응형 주행은 2명·1명이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1211"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "'the navigation system that follows human routines distracts people less than the one lacking this capability.' 로봇 없는 대조 측정에서는 통행자 211명 중 불만 0명. 표본이 매우 작다.",
      "as_of": "2022-07-04",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "Francis 외(2023, 저자 52명)는 사회적 내비게이션 로봇을 안전·쾌적·가독성·예의·사회적 역량·상대 이해·능동성·맥락 대응의 원칙을 지키는 로봇으로 정의하고, 지표·시나리오·데이터셋·시뮬레이터 사용 지침과 서로 다른 시뮬레이터·로봇·데이터셋 결과를 비교하기 위한 지표 프레임워크를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원칙: 'safety, comfort, legibility, politeness, social competency, agent understanding, proactivity, and responsiveness to context'. 최근 논문 177편 검토(검색 요약).",
      "as_of": "2023-09-19",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "HuNavSim(Pérez-Higueras 외, RA-L 2023)은 ROS 2 기반 오픈소스 도구로 Gazebo 같은 로봇 시뮬레이터와 함께 이동로봇 주변 사람 에이전트의 다양한 보행 행동을 시뮬레이션하고, 사회적 내비게이션 벤치마킹용 지표 묶음을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1213"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'a general human-navigation model' 과 'a rich set of individual and realistic human navigation behaviors and a complete set of metrics for social navigation benchmarking' (arXiv 초록).",
      "as_of": "2023-09-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Open-RMF 시뮬레이션에서 군중 시뮬레이션(CrowdSim)은 선택 기능으로 rmf_traffic_editor 에서 켤 수 있으며 Menge 를 핵심 엔진으로 써 시뮬레이션 세계의 에이전트를 제어한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'Crowd Simulation, aka CrowdSim is an optional feature in RMF simulation.' Menge 사용, 데모 실행 시 use_crowdsim:=1 로 켠다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "물류창고 사례: EU ILIAD 프로젝트(2017~2021)는 스웨덴 외레브로의 Orkla Foods 창고 두 곳(상온·냉장)에서 자율 지게차 플릿을 시연했으며, 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적하고, 현장별 사람 이동 패턴을 움직임 지도로 학습해 사람 흐름에 맞춘 경로 계획에 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1215"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "최종 시연 2021-06. 전원 투입부터 첫 임무까지 1시간 미만. 'qualitative trajectory calculus' 로 움직임별 '사회적 비용'을 추정해 속도 제약을 계산.",
      "as_of": "2021-06",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "병원 사례(한국): 조선비즈(2024-07) 보도에 따르면 한림대학교성심병원은 붐비지 않는 밤에 인식한 경로가 낮의 혼잡에서는 원활하지 않을 수 있어 로봇 통행 경로와 작업 정지 지점에 전용 스티커를 붙여 표시했고, 로봇은 사람이나 휠체어와 마주치면 무조건 기다리도록 설계되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1217"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "\"사람이나 휠체어와 마주치면 로봇은 무조건 기다리도록 설계됐다.\" 7종 73대, 20개월간 서비스 3만5천여 건.",
      "as_of": "2024-07-12",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "연계 대상: 행정안전부의 인파관리지원시스템은 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사의 기지국 접속정보로 인파 밀집도·혼잡도를 추정하고 협소 도로 비율 같은 공간 특성을 더해 위험도를 산출해 지도에 색으로 표시하며, 위험 수준에 따라 지자체 공무원에게 경보를 보낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1210"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기지국 접속정보 기반이라 별도 장비가 필요 없고 사각지대가 거의 없다고 설명. 2023-12-27 정책브리핑 보도자료.",
      "as_of": "2023-12-27",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f17",
      "claim": "Waymax(Gulino 외, 2023) 자율주행 시뮬레이터는 기록된 궤적을 그대로 따르는 로그 재생 에이전트와, 규칙 기반(지능형 운전자 모델, IDM)·학습 기반 행동 모델로 다른 참가자에 반응하는 모의 에이전트를 함께 제공하며, 강화학습 에이전트가 모의 에이전트의 행동에 과적합할 수 있음을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1128"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'learned and hard-coded behavior models that allow for realistic interaction within simulation'. RL 알고리즘이 모의 에이전트 행동에 과적합할 수 있음(arXiv 초록).",
      "as_of": "2023-10-12",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f18",
      "claim": "oq-256 에 대해 자율주행 시뮬레이션은 기록 재생 에이전트를 반응형 모델로 바꾸는 방식으로 비반응 문제를 다루지만 모델 편향이 생기므로, 로봇 플릿 재현에서도 기록된 사람을 사회적 힘 모델·HuNavSim·Menge 같은 보행자 모델로 기록 위치에서 이어받아 움직이게 하는 방식이 가능해 보이나, 로봇 플릿 재현에 적용한 공개 사례는 이번에 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1128",
        "ref-1207",
        "ref-1213",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Waymax 의 로그 재생·반응형 에이전트 구분과 과적합 보고(f17), 보행자 모델(f3)·시뮬레이터(f12·f13)를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 핵심 질문(현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가)에 대해, 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 반영하는 방식이 쓰이지만, 효과 근거는 소규모 실험·단일 사례 중심인 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1204",
        "ref-1205",
        "ref-1209",
        "ref-1211",
        "ref-1215",
        "ref-1217",
        "ref-1218"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f7·f9·f10·f14·f15·f8 종합. 효과 수치는 f10(표본 작음)과 f8(현장 시험)뿐이며 물류창고·병원 정량 효과는 미확인.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 19. 사람·보행자 모델에서 ROP가 직접 맡을 범위는 여러 로봇과 설비 센서가 보고한 사람 위치를 공통 좌표·시각·신뢰도로 모으고, 구역·시간대별로 집계·익명화한 사람 흐름·혼잡 모델을 유지해 경로·구역 비용, 작업 시간 추정, 배정·스케줄링에 넘기는 일로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1204",
        "ref-1206",
        "ref-1211",
        "ref-1215"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "위치 신뢰도 표현(f4), 흐름 지도의 계획 활용(f1·f9·f14)에서 도출. 개인 식별과 연결될 수 있어(f5) 집계·익명화가 필요하다는 판단 포함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f21",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇의 온보드 사람 검출·추적, 국소 회피와 정지·양보 동작, 사람 근접 안전 기능은 로봇 자체 지능·제어(제조사)에, CCTV·기지국 기반 인파 관리는 시설·공공 시스템에 속하므로, ROP는 그 결과를 받아 계획 제약으로 쓰고 로봇에 대기·우회 같은 운영 규칙을 요청하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1215",
        "ref-1217",
        "ref-1210"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ILIAD 의 온보드 검출(f14), 병원 로봇의 무조건 대기 설계(f15), 공공 인파관리 시스템(f16)을 원문 19장 경계에 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "이 영역은 사람 위치의 현재 상태와 신선도의 18. 실시간 세계 상태·데이터 일관성(f4), 가정한 미래를 실험하는 보행자 시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈(f3·f12·f13), 기록 재현의 36. 가상 시운전·실제 상황 재현(f17·f18, oq-256), 흐름 지도를 얹을 15. 지도·공간·위치 모델과 구역 의미의 16. 장소 의미·지도 관리(f1·f15), 작업 시간 추정의 26. 작업 순서·스케줄링(f20), 혼잡을 반영한 경로의 27. 다중 로봇 경로·교통 관리 — MAPF(f9·f14), 사람 근접 안전의 49. 사람 근접 안전(f21), 사람 식별 정보의 53. 개인정보·영상 데이터(f5), 학습 기반 예측의 46. 예측·학습 기반 최적화(f2·f9), 평가 지표의 54. 시험·형식 검증·벤치마크(f11), 현장 협업의 31. 사람–로봇 협업(f15), 적용 현장인 61. 물류창고(f14)·63. 병원·의료(f15)·64. 상업 시설(f7·f8)·66. 실외(f16·f17)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1206",
        "ref-1207",
        "ref-1213",
        "ref-406",
        "ref-1128",
        "ref-1204",
        "ref-1217",
        "ref-1211",
        "ref-1215",
        "ref-1205",
        "ref-1079",
        "ref-1209",
        "ref-1218",
        "ref-1210"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결의 근거 finding 을 괄호에 적었다. 18번(현재 상태 표현)과 34번(가정한 미래 실험)은 원문 구분에 따라 나눴다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    }
  ],
  "sources": [
    {
      "id": "ref-1204",
      "org": "Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11))",
      "title": "Survey of maps of dynamics for mobile robots",
      "published": "2023",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649231190428",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 움직임 지도(MoD)의 정의·입력·용도(전역 계획, 위치 추정, 사람 움직임 예측)를 정리한 서베이. SAGE·Lincoln 저장소 403, DARKO 프로젝트 소개 페이지에서 서지만 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1205",
      "org": "Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020)",
      "title": "Human Motion Trajectory Prediction: A Survey",
      "published": "2019-12-17",
      "url": "https://arxiv.org/abs/1905.06113",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사람 움직임 궤적 예측 방법을 움직임 모델링 방식과 맥락 정보 수준으로 분류하고 데이터셋·지표를 검토한 서베이. arXiv 초록만 확인(PDF 추출 실패).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1905.06113",
      "source_unopened": false
    },
    {
      "id": "ref-1206",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS4HRI 의 사람 표현 규약. person·face·body·voice 식별자, /humans/… 토픽, person_<ID> 프레임과 위치 신뢰도, 익명 사람 표시를 정한다. 원문 상태 표기는 Draft.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-0155.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1207",
      "org": "Helbing, D., & Molnár, P. (Physical Review E 51(5))",
      "title": "Social force model for pedestrian dynamics",
      "published": "1995-05-01",
      "url": "https://link.aps.org/doi/10.1103/PhysRevE.51.4282",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 보행자 움직임을 '사회적 힘'(원하는 속도로의 가속, 타인·경계와의 거리 유지, 끌림)으로 모델링한 고전 논문. 검색 요약으로만 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1208",
      "org": "Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020)",
      "title": "THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset",
      "published": "2019-12-11",
      "url": "https://arxiv.org/abs/1909.04403",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실내 환경의 사람 궤적·시선 데이터셋. 위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표 정답과 3D 라이다·이동로봇 데이터를 포함한다. arXiv 초록 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1909.04403",
      "source_unopened": false
    },
    {
      "id": "ref-1209",
      "org": "ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외",
      "title": "ATC shopping center tracking dataset",
      "published": null,
      "url": "https://dil.atr.jp/crest2010_HRI/ATC_dataset/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "오사카 ATC 쇼핑센터 약 900㎡ 구역에서 3D 거리 센서 49대로 92일간 보행자를 추적한 공개 데이터셋 소개 페이지. 데이터 필드와 연구 목적 전용 이용 조건을 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://dil.atr.jp/crest2010_HRI/ATC_dataset/",
      "source_unopened": false
    },
    {
      "id": "ref-1210",
      "org": "행정안전부 (대한민국 정책브리핑)",
      "title": "29일부터 인파관리지원시스템 본격 운영…다중운집 … (제목 일부만 확인)",
      "published": "2023-12-27",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148924176",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기지국 접속정보로 인파 밀집도를 추정해 위험도를 산출하고 지자체에 경보를 보내는 인파관리지원시스템의 전국 100곳 정식 운영을 알린 정부 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.korea.kr/news/policyNewsView.do?newsId=148924176",
      "source_unopened": false
    },
    {
      "id": "ref-1211",
      "org": "Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI)",
      "title": "Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation",
      "published": "2022-07-04",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "대학 복도 한 달 관측으로 20여 개 시공간 보행자 흐름 지도를 학습·비교하는 벤치마크 방법과, 흐름 예측을 쓴 주행이 사람을 덜 방해함을 보인 현장 실험.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full",
      "source_unopened": false
    },
    {
      "id": "ref-1079",
      "org": "Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction)",
      "title": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms",
      "published": "2023-09-19",
      "url": "https://arxiv.org/abs/2306.16740",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 내비게이션의 원칙 정의와 지표·시나리오·데이터셋·시뮬레이터 평가 지침, 지표 프레임워크를 제안한 공동 논문. arXiv 초록 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2306.16740",
      "source_unopened": false
    },
    {
      "id": "ref-1213",
      "org": "Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023)",
      "title": "HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation",
      "published": "2023-09-13",
      "url": "https://arxiv.org/abs/2305.01303",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 기반 오픈소스 사람 보행 행동 시뮬레이터와 사회적 내비게이션 지표 묶음을 소개. arXiv 초록 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2305.01303",
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics (osrf/ros2multirobotbook)",
      "title": "Programming Multiple Robots with ROS 2 — Simulation",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 시뮬레이션 장. 선택 기능인 CrowdSim 이 Menge 엔진으로 사람 에이전트를 제어하고 rmf_traffic_editor 에서 켠다고 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
      "source_unopened": false
    },
    {
      "id": "ref-1215",
      "org": "ILIAD 프로젝트 컨소시엄 (EU Horizon 2020)",
      "title": "Concluding ILIAD",
      "published": "2021-06",
      "url": "https://iliad-project.eu/concluding-iliad/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 자율 지게차 플릿 프로젝트 ILIAD 의 최종 시연(Orkla Foods 창고 두 곳), 다중 센서 작업자 검출, 움직임 지도 기반 사람 인식 계획을 정리한 프로젝트 결산 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://iliad-project.eu/concluding-iliad/",
      "source_unopened": false
    },
    {
      "id": "ref-1128",
      "org": "Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv)",
      "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research",
      "published": "2023-10-12",
      "url": "https://arxiv.org/abs/2310.08710",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제 주행 데이터로 장면을 초기화·재생하는 자율주행 시뮬레이터. 로그 재생 에이전트와 반응형 모의 에이전트(IDM·학습 모델)를 제공한다. arXiv 초록 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2310.08710",
      "source_unopened": false
    },
    {
      "id": "ref-1217",
      "org": "조선비즈 (이정아, 다음 뉴스 게재)",
      "title": "로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘",
      "published": "2024-07-12",
      "url": "https://v.daum.net/v/bc4riunbUE",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원의 로봇 운영 기사. 낮 혼잡 대응을 위한 전용 경로 스티커, 사람·휠체어를 만나면 무조건 기다리는 설계, 사람들의 양보·엘리베이터 도움을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://v.daum.net/v/bc4riunbUE?f=p",
      "source_unopened": false
    },
    {
      "id": "ref-1218",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013)",
      "title": "Will I bother here? - A robot anticipating its influence on pedestrian walking comfort",
      "published": "2013-03",
      "url": "https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 쇼핑몰 로봇이 보행자 행동 모델로 혼잡을 예상해 보행 쾌적성을 해치지 않게 위치를 계획하는 방법. Semantic Scholar 페이지 본문을 읽지 못해 검색 요약으로만 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
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
      "rationale": "섹션 3: f19(핵심 질문 답, 추정), f15(낮 혼잡으로 경로가 원활하지 않은 병원 사례), f8(로봇이 혼잡을 만드는 문제) / 섹션 4: 움직임 지도 f1, 사람 궤적 예측 f2, 사회적 힘 모델 f3, 사람 표현·위치 신뢰도 f4, 사회적 내비게이션 원칙 f11, 로그 재생·반응형 에이전트 f17 / 섹션 5: 물류창고 — f14(제약), 병원 — f15(제약, 한국), 상업 시설 — f7(작업 대상)·f8(제약), 실외 — f16(시작 조건, 한국, 연계 대상)·f17(예외·성과), 기타(대학 건물) — f9(제약)·f10(예외·성과). 제조 공장·가정 사례는 찾지 못했음을 명시 / 섹션 6: 실시간 검출·추적 f14·f7, 장기 시공간 흐름 지도 f1·f9·f10, 단기 궤적 예측 f2, 보행자 행동 모델과 시뮬레이션 f3·f8·f12·f13, 운영 규칙 f15, 기록 재현의 반응형 대체 f17·f18 / 섹션 7: REP-155(ROS4HRI) f4·f5, HuNavSim f12, Open-RMF CrowdSim(Menge) f13, 데이터셋 THÖR f6·ATC f7, 평가 지침 f11 / 섹션 8: f1·f2·f3·f8·f9·f11·f17 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66 (18번과 34번 구분 유지, L 대분류 46번 연결) / 섹션 11: 기존 oq-256(f17·f18 로 부분 근거, 미해결 유지)과 open_questions_new 3건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f15, 61. 물류창고 페이지에 f14, 36. 가상 시운전·실제 상황 재현 페이지 11절 oq-256 에 f17·f18 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "사회적 힘 모델",
      "term_en": "Social Force Model",
      "definition": "보행자 움직임을 원하는 속도로의 가속, 다른 보행자·벽과의 거리 유지(반발), 끌림을 나타내는 가상의 힘의 합으로 계산하는 보행자 행동 모델이다."
    },
    {
      "term_ko": "사람 움직임 궤적 예측",
      "term_en": "Human Motion Trajectory Prediction",
      "definition": "관측된 과거 위치와 주변 맥락(다른 사람·장애물·목적지)을 바탕으로 사람의 가까운 미래 이동 경로를 추정하는 기법이다."
    },
    {
      "term_ko": "사회적 내비게이션",
      "term_en": "Social Robot Navigation (Human-aware Navigation)",
      "definition": "로봇이 사람 사이를 이동할 때 안전뿐 아니라 쾌적성·가독성·예의 같은 사회적 원칙을 지키도록 경로와 행동을 정하는 주행 방식이다."
    },
    {
      "term_ko": "로그 재생 에이전트·반응형 에이전트",
      "term_en": "Log-replay Agent / Reactive Agent",
      "definition": "시뮬레이션에서 기록된 궤적을 그대로 따르는 배경 참가자(로그 재생)와, 제어 대상의 행동에 반응해 움직임을 바꾸는 모델 기반 참가자(반응형)를 구분하는 용어이다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? | 관련 영역: 19. 사람·보행자 모델, 18. 실시간 세계 상태·데이터 일관성, 53. 개인정보·영상 데이터 | 근거: f4 | 종류: 일반",
    "병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? | 관련 영역: 19. 사람·보행자 모델, 26. 작업 순서·스케줄링, 63. 병원·의료 | 근거: f15 | 종류: 일반",
    "기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? | 관련 영역: 19. 사람·보행자 모델, 66. 실외 | 근거: f16 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f1 Kucner 외 서베이 원문 미열람(SAGE·Lincoln 403, DARKO 페이지 초록이 다른 논문 문장으로 보여 채택하지 않음) — 검색 요약 범위만 사용",
      "f2 Rudenko 서베이의 세부 분류 명칭(물리 기반·패턴 기반·계획 기반 등) 미확인 — PDF 추출 실패",
      "f3 Helbing·Molnár 원문 미열람",
      "f8 Kidokoro 외 원문·초록 미열람, 혼잡 감소 효과 수치 미확인",
      "f4 REP-155 상태: 원문 파일은 Draft, 검색 요약(ROS4HRI 소개)은 '공식 채택'으로 표현 — 최종 상태 미확인",
      "f9 벤치마크 수치(600만 건 이상, 약 500㎡)는 요약 도구 경유로 읽어 원문 문구 대조 미확인",
      "f10 현장 실험은 40분 세션 4회로 표본이 매우 작음",
      "f14 ILIAD 의 창고 현장 정량 효과(사람 방해·처리 시간) 미확인",
      "f15 한림대학교성심병원 로봇의 사람 대기 규칙은 기사 1건 기준, 독립 확인 실패",
      "oq-256 부분 답: 로봇 플릿 재현에서 기록된 사람을 반응형 보행자 모델로 대체한 공개 사례 미발견",
      "제조 공장·가정 현장의 사람 흐름 반영 사례 미발견",
      "ILIAD Safety Stack 논문(RAM 2023) PDF 404 로 넣지 않음",
      "Patient–Robot Co-Navigation of Crowded Hospital Environments(Applied Sciences 2023) 403 으로 넣지 않음"
    ],
    "scope_violations": [
      "f14·f15·f21: 온보드 사람 검출·추적, 국소 회피, 정지·양보 동작은 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 f21 을 '연계 대상: '으로 두고 ROP 직접 범위는 f20 에서 흐름 모델 집계·계획 반영으로 한정함",
      "f16: 기지국 기반 공공 인파 관리는 ROP 밖 공공·시설 시스템이므로 '연계 대상: '으로 표시",
      "f17: 자율주행 차량 시뮬레이션은 '업종별 조건(실외 차량)' 쪽 자료로, 기록 재현 방법 참고로만 쓰고 로봇 플릿 적용은 추정(f18)으로 둠",
      "f3·f12·f13: 보행자 시뮬레이션은 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험) 쪽 기능이고, 현재 사람 위치 표현(f4)은 18. 실시간 세계 상태·데이터 일관성 쪽이므로 연결 제안(f22)에서 구분함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1204~ref-1218, 예약 구간 안)로 신규 출처 상한에 도달해 Mavrogiannis 외 사회적 내비게이션 서베이, ILIAD Safety Stack 논문, 병원 군중 동행 리뷰, Kairos(arXiv 2609.27467, 4D 장면 그래프 기반 존재·흐름 예측)를 출처로 넣지 않았다(다음 실행 후보). 재사용 출처 없음(참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요; 특히 ref-406 ros2multirobotbook 시뮬레이션 장). 원문 열람: 15건 중 12건을 열었고(webfetch 10, github_raw 2), ref-1204(403)·ref-1207·ref-1218 은 fetched false·원문 미열람이다. 논문 다수는 arXiv 초록 수준만 열었다. 교차 확인 0건. 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '실시간 검출·추적, 장기 흐름 지도, 궤적 예측, 보행자 행동 모델, 운영 규칙으로 반영하는 방식은 확인되나 효과 근거는 소규모 실험·단일 사례 중심'이라는 추정이다. 현장 유형 사례는 물류창고(f14)·병원(f15, 한국)·상업 시설(f7·f8)·실외(f16 한국, f17)·기타(f9·f10 대학 건물)이며 제조 공장·가정은 찾지 못했다. 국내 자료는 행정안전부 정책브리핑(ref-1210)과 조선비즈(ref-1217)다. 기존 열린 질문 oq-256 은 f17·f18 로 부분 근거만 있어 해결 제안하지 않았다. L. AI·학습 기술 관련(학습 기반 궤적 예측·흐름 지도 f2·f9)은 46. 예측·학습 기반 최적화와 이 영역 양쪽 연결을 f22 에서 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다. 용어집에 이미 있는 움직임 지도·인프라 장착 센서·통과 가능성·속도·분리 감시·보호 분리 거리·반정적 객체·침범 후 시간은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-20/verification.json

```json
{
  "run_id": "2026-09-30-20",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1204: SAGE·Aalto 저장소 PDF 모두 403이라 원문을 열지 못했다(원문 미열람). 검색 결과에서 기관·제목·IJRR 42(11) 977–1006, 2023이 일치했다. 초록에서 MoD 정의와 입력(궤적, 짧고 끊긴 관측)을 확인했고, 검색 요약에서 전역 경로 계획·위치 추정 개선·사람 움직임 예측 용도와 감지 범위 밖 움직임 정보를 확인했다. 단일 출처이고 원문 미열람이므로 medium이 상한이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1205: arXiv 초록을 열어 확인했다(v3 2019-12-17). 저자, 여러 연구 공동체의 연구 정리, 움직임 모델링 방식과 맥락 정보 수준의 두 축 분류 체계, 데이터셋·지표 검토가 일치한다. '보행자 중심의 지상 2차원'이라는 한정은 초록에서 확인되지 않는다. 본문 PDF는 추출에 실패했으므로 이 한정구는 빼야 한다(수정 지시). arXiv에는 IJRR 투고로 적혀 있고, 검색 결과에서 SAGE 게재본(10.1177/0278364920917446)을 확인했다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1207: APS 페이지가 403이라 원문을 열지 못했다(원문 미열람). 검색 결과에서 Helbing·Molnár, PRE 51, 4282, 1995-05-01을 확인했다. 초록 요약에서 가속 항·거리 유지 항·끌림 항과 군중 시뮬레이션에서 관측된 집단 현상의 자기조직화 기술을 확인했다. 발행 30년이 지난 고전 모델이므로 기준일을 적어야 한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1206: raw GitHub에서 열어 확인했다. REP 155, 저자 Lemaignan, Status Draft, Created 11-Jan-2022가 일치한다. location_confidence 세 구간(1.0 추적 중, 0~1 이전에 보임, 0 본 적 없음 — 이때 TF 프레임을 내지 않는다), /humans/persons/tracked, person_<ID> 프레임, /anonymous 하위 토픽도 일치한다. 채택된 표준이 아니라 초안(Draft) 규약이라는 점을 본문에 밝혀야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1206: 'normally assigned by a node able to perform person identification (face recognition node, voice recognition node, …)'와 세션을 넘는 영속 ID를 확인했다. '옷 색 같은 신체 특징'은 이번 열람 요약에 나타나지 않았다. 본문에서는 얼굴·음성 인식 노드 예시로 한정하는 것이 안전하다(수정 지시)."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1208: arXiv 초록을 열어 확인했다(v2 2019-12-11, RA-L). 실내 환경, 정답 여섯 종류(위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표), 3D 라이다, 이동로봇, 궤적 품질 지표가 일치한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1209: 원문을 열어 확인했다. 약 900㎡, 3D 거리 센서 49대, 2012-10-24~2013-11-29 가운데 92일, 매주 수·일요일 9:40~20:20, 필드 여덟 개, 연구 목적 전용, ATR·JST/CREST가 일치한다. 이 자료는 로봇 적용 사례가 아니라 보행자 관측 데이터셋이다(수정 지시)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1218: Semantic Scholar 본문을 열지 못했다(원문 미열람). 검색 결과(HRI 2013 수상 페이지, Springer 장 요약)에서 저자·HRI 2013·최우수 논문상을 확인했다. 사람을 끄는 로봇이 좁은 곳에 혼잡을 만드는 문제, 보행자 흐름·상호작용·보행 쾌적성의 세 모델로 가상 상황을 시뮬레이션하는 방법, 쇼핑몰 현장 시험도 확인했다. 효과는 '노출만 최대화한 로봇 주변보다 보행 쾌적성을 더 좋게 인식'이라는 비교이므로 비교 기준을 밝혀야 한다(수정 지시). 수치는 미확인이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1211: 원문을 열어 확인했다(2022-07-04). UTBM 홀 약 500㎡, 2019-03 한 달 학습, 600만 건 이상 검출, Velodyne HDL-32E, EE·EL 지표, 공간과 시간을 독립적으로 모델링한 연속 시공간 방법이 우수했다는 결론이 일치한다. 비교 방법 수는 원문 기준 26개이므로 '20여 개'를 고쳐야 한다. 'HyT×GMM 등'의 최우수 방법 이름은 이번 열람에서 확인하지 못했다(수정 지시)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1211: 세션별 결과를 확인했다. 예측형 9:20–10:00·16:00–16:40 모두 0명, 반응형 10:00–10:40 2명·16:40–17:20 1명, 2019-12-12~13, 40분 세션 네 번, 로봇 없는 대조군 211명 중 불만 0명. Toyota HSR 기종은 이번 열람 요약에 나타나지 않았다(미확인이지만 결론에 영향은 없다). 표본이 매우 작으므로 low가 맞다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1079: arXiv를 열어 확인했다(최종판 2023-09-19). Francis 외 공저자 51명(총 52명), 원칙 여덟 가지, 평가 지침, 지표 프레임워크가 일치한다. evidence_excerpt의 '논문 177편 검토'는 이번 열람에서 확인하지 못했으므로 본문에 쓰지 않는다. ACM THRI 게재 여부도 이번에 확인하지 않았다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1213: arXiv를 열어 확인했다(v3 2023-09-13, RA-L 채택 프리프린트). ROS 2, Gazebo 같은 시뮬레이터와의 연동, 개별 보행 행동, 사회적 내비게이션 벤치마킹 지표 묶음이 일치한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406: raw GitHub(simulation.md)에서 열어 확인했다. CrowdSim이 선택 기능이라는 점, Menge 엔진, traffic editor 설정과 use_crowdsim:=1 실행 인자가 일치한다. 같은 URL이 참고문헌에 이미 있으면 퍼블리셔가 병합해야 한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1215: 원문을 열어 확인했다. 2021-06 종료, 외레브로 Orkla Foods 창고 두 곳(상온·냉장), 2D·3D 레이저·컬러·깊이 카메라·안전조끼 검출 카메라, 움직임 지도(STeF-map)로 현장별 이동 패턴을 학습해 경로 계획에 쓴 점, qualitative trajectory calculus로 사회적 비용을 추정한 점, 전원 투입부터 첫 임무까지 1시간 미만이 일치한다. 프로젝트 기간 '2017~2021'은 이번 열람 요약에서 확인하지 못했다. 사람 검출·추적은 로봇 탑재 기능이므로 9절에서는 연계 대상으로 둔다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1217: 원문을 열어 확인했다(조선비즈 이정아, 2024-07-12, 다음 게재). 밤에 인식한 경로가 낮에는 원활하지 않을 수 있다는 서술, 경로·작업 지점 전용 스티커, '로봇은 무조건 기다리도록 설계됐다', 7종 73대, 20개월 35,492건이 일치한다. 1차 열람에서는 기다리는 대상이 '환자나 휠체어'로 읽혔으므로 '사람이나 휠체어'를 고쳐야 한다(수정 지시). 운영 규모는 ref-1261(지디넷코리아, 2022-08~2024-05 35,492건)과 맞지만, 대기 규칙은 기사 1건 기준이라 교차 확인이 아니다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1210: 원문을 열어 확인했다. 행정안전부 2023-12-27 보도자료, 2023-12-29 운영 시작, 중점관리지역 100곳, 이동통신 3사 기지국 접속정보, 협소 도로 비율 등 공간 특성(인구 특성 포함), 지도 색 표시, 지자체 공무원 경보가 일치한다. 정식 제목은 '29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방'이다. 로봇 적용 사례가 아니라 연계 대상이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1128: arXiv 초록과 HTML 본문을 열어 확인했다(2023-10-12). 로그 재생(logged trajectories), IDM 기반 규칙형 반응 에이전트(기록 경로를 따르며 속도만 조정), 학습·규칙 기반 행동 모델, RL이 IDM 에이전트에 과적합한다는 보고가 일치한다. IDM 에이전트는 기록된 경로를 따르면서 속도만 조정한다는 한정을 본문에 살릴 수 있다. 자율주행 차량 자료이므로 방법 참고로만 쓴다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f17·f3·f12·f13을 종합한 추정이다. 근거 finding이 모두 살아남았고, 공개 적용 사례가 없다는 점도 밝혔다. [추정]을 유지하고 oq-256은 미해결로 둔다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "핵심 질문에 답하는 종합 추정이다. 근거 finding f1·f2·f7·f8·f9·f10·f14·f15가 확인됐다. '효과 근거는 소규모 실험·단일 사례 중심'이라는 한계 서술도 f10·f8 확인 결과와 맞는다. [추정]을 유지한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ROP 직접 범위에 관한 종합 추정이다. 근거 f4·f1·f9·f14·f5는 확인됐다. '집계·익명화'는 f5에서 끌어낸 판단이므로 [추정]을 유지한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연계 대상 추정이다. 'CCTV·기지국 기반 인파 관리'의 CCTV는 ref-1210에 없다(ref-1210은 별도 장비 없이 기지국 정보만 쓴다고 설명한다). '사람 근접 안전 기능' 전체를 제조사 몫으로 쓴 것도 문제다. 원문 49. 사람 근접 안전에 구역별 속도·진입 제한이 있으므로 범위를 좁혀야 한다(수정 지시)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 제안이다. 18. 실시간 세계 상태·데이터 일관성(f4, 현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(f3·f12·f13, 가정한 미래)의 구분을 지켰고, L. AI·학습 기술의 46. 예측·학습 기반 최적화를 양쪽에 연결했다. 번호와 이름을 함께 표기한 것도 맞다."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f21: '사람 근접 안전 기능'을 통째로 로봇 자체 지능·제어(제조사) 몫으로 적었다. 로봇 탑재 안전 기능(안전 센서 기반 감속·정지, 국소 회피)만 연계 대상으로 두고, 구역별 속도·진입 제한 같은 운영 제약은 49. 사람 근접 안전과 연결되는 것으로 고쳐 쓴다(편집으로 해결 가능).",
      "f14·f16·f17: ILIAD의 탑재 사람 검출, 기지국 기반 공공 인파관리, 자율주행 차량 시뮬레이터는 모두 ROP 밖의 연계 대상·방법 참고다. 브리프가 이미 이렇게 표시했으므로 본문에서도 ROP 직접 기능처럼 쓰지 않는다."
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "용어 후보 '로그 재생 에이전트·반응형 에이전트'는 기존 용어집의 log-playback(로그 재생 (Log Playback))과 겹친다.",
      "ref-406(osrf/ros2multirobotbook simulation 장)는 참고문헌 전체 1157건 가운데 같은 URL이 이미 있을 수 있다. 퍼블리셔가 기존 id로 병합해야 한다.",
      "f15(한림대학교성심병원, 7종 73대·35,492건)는 2026-09-30-18 브리프의 40. 운영 절차·요청 창구 f14·f15(ref-1261·ref-1262)와 같은 병원 사례다. 수치가 서로 맞아 모순은 없다.",
      "f4 위치 신뢰도는 18. 실시간 세계 상태·데이터 일관성의 관측 신선도·신뢰도 주제와 겹친다. 연결만 하고 본문은 이 영역의 사람 표현으로 한정한다."
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
    "f2: '보행자 중심의 지상 2차원' 한정구를 뺀다. ref-1205 초록에서 확인되지 않았고 본문은 열지 못했다.",
    "f9: '20여 개 시공간 보행자 흐름 지도'를 '26개 방법'으로 고친다. 'HyT×GMM 등' 구체 방법 이름은 빼고 '공간과 시간을 독립적으로 모델링한 연속 시공간 방법이 우수했다'로 쓴다. ref-1211 원문 기준 비교 방법 수는 26개이고 최우수 방법 이름은 확인하지 못했다.",
    "f10: 같은 문장에 표본 한계(40분 세션 네 번, 방법당 두 세션)를 밝히고, 로봇 없는 대조 측정(통행자 211명 중 불만 0명)만 덧붙일 수 있다. Toyota HSR 기종은 이번 검증에서 확인하지 못했으므로 쓰지 않는다.",
    "f8: 효과 서술 '영향을 줄였다'를 '노출만 최대화한 로봇에 비해 주변 보행자가 보행 쾌적성을 더 좋게 인식했다'로 고쳐 비교 기준을 밝힌다. 효과 수치는 미확인으로 둔다. ref-1218은 원문 미열람이다.",
    "f15: '사람이나 휠체어와 마주치면'을 '환자나 휠체어와 마주치면'으로 고친다(1차 열람에서 대상이 환자로 읽혔다). 기사 1건(조선비즈, 2024-07-12) 기준임을 밝히고, 이 출처의 직접 인용은 짧은 구절 1회로 제한한다.",
    "f5: 영속 person ID 부여 노드 예시는 원문에서 확인된 얼굴 인식·음성 인식 노드로 한정한다. '옷 색 같은 신체 특징'은 이번 검증에서 확인하지 못했으므로 쓰지 않는다.",
    "f4: 7절에서 REP-155(ROS4HRI)를 '표준'이 아니라 원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안으로 쓴다. 최종 채택 여부는 미확인으로 둔다.",
    "f11: evidence_excerpt의 '논문 177편 검토'는 확인하지 못했으므로 본문에 쓰지 않는다.",
    "f14: 프로젝트 기간 '2017~2021'은 ref-1215 열람에서 확인하지 못했다. '2021-06 종료'로만 쓰거나 시작 연도를 미확인으로 둔다.",
    "f21: 'CCTV·기지국 기반 인파 관리'에서 CCTV를 뺀다(ref-1210은 기지국 접속정보만 쓴다). '사람 근접 안전 기능' 전체를 제조사 몫으로 쓰지 않는다. 로봇 탑재 안전 기능(감속·정지·국소 회피)은 연계 대상으로, 구역별 속도·진입 제한은 49. 사람 근접 안전과 연결되는 운영 제약으로 나눠 쓴다.",
    "5절 실외: f16(공공 인파관리지원시스템)은 로봇 적용 사례가 아니라 연계 대상이고, f17(Waymax)은 자율주행 차량 시뮬레이터다. 실외에서는 이 영역의 로봇 적용 사례를 찾지 못했음을 밝히고, site_matrix_updates에 실외 칸을 로봇 적용 사례로 넣지 않는다.",
    "5절 상업 시설: f7(ATC 데이터셋)은 로봇 적용이 아니라 보행자 관측 데이터셋임을 밝힌다. 로봇 적용 사례는 f8로 세운다. 제조 공장·가정 사례는 찾지 못했음을 명시한다.",
    "11절: 이 영역에 걸린 기존 열린 질문 oq-261(촬영 거부 의사의 로봇 간 공통 반영, 영역 53·19)도 싣고 열림을 유지한다. f5와 관련이 있지만 새 근거는 없다. oq-256은 f17·f18을 부분 근거로 싣되 해결로 바꾸지 않는다.",
    "용어집: 후보 '로그 재생 에이전트·반응형 에이전트'는 기존 용어 log-playback(로그 재생)과 겹치므로 신규 등록하지 않고 기존 용어에 연결한다. 사회적 힘 모델·사람 움직임 궤적 예측·사회적 내비게이션 세 후보는 등록할 수 있다.",
    "원문 미열람 표시: ref-1204, ref-1207, ref-1218 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates의 해당 항목에 source_unopened: true를 넣는다.",
    "ref-1210: 제목을 정식 제목 '29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방'으로 적는다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 22건, 미확인 0건, 교차 확인 0건. 강등: 없음. 수치·표현 정정 지시는 f2·f5·f8·f9·f10·f14·f15·f21에 있다(f9의 비교 방법 수는 원문 기준 26개, f15의 대기 대상은 환자나 휠체어). 원문 미열람 출처: ref-1204, ref-1207, ref-1218. 셋 다 검색 결과에서 기관·제목·서지와 주장 요지만 확인했다. 주의: 핵심 질문 답(f19)과 ROP 책임 경계(f20·f21)는 종합 추정이다. 효과 근거는 대학 홀 40분 세션 네 번의 소규모 현장 실험(f10)과 쇼핑몰 현장 시험(f8, 수치 미확인)뿐이다. 물류창고·병원의 정량 효과, 제조 공장·가정·실외의 로봇 적용 사례는 확인하지 못했다. REP-155는 원문 상태가 Draft인 규약이다. 보행자 시뮬레이션은 34. 시뮬레이션·예측용 디지털 트윈, 현재 사람 위치 표현은 18. 실시간 세계 상태·데이터 일관성으로 나눠 연결한다. oq-256은 부분 근거만 있어 열림을 유지하고, oq-261도 11절에 싣는다. 미사용 출처 없음. 정정 요청 없음. 검증 검색은 7회를 썼다(리서치 16회와 합쳐 23회/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-20/pages.json

```json
{
  "run_id": "2026-09-30-20",
  "outline": [
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "사람 위치·흐름은 실시간 검출·추적, 장기 흐름 지도, 궤적 예측·보행자 행동 모델로 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙에 반영하지만 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1211]",
      "planned_findings": [
        "f19",
        "f15",
        "f8"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1150,
      "summary": "핵심 개념은 움직임 지도, 사람 움직임 궤적 예측, 사회적 힘 모델, 사람 표현 규약(ROS4HRI), 사회적 내비게이션, 로그 재생·반응형 에이전트다. [사실][^ref-1204]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f11",
        "f17"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2000,
      "summary": "물류창고(ILIAD 자율 지게차), 병원(한림대학교성심병원, 기사 1건), 상업 시설(쇼핑몰 로봇의 혼잡 예상), 기타(대학 건물 흐름 지도 주행) 사례를 여섯 항목으로 정리했고, 실외·제조 공장·가정의 로봇 적용 사례는 찾지 못했다. [사실][^ref-1215]",
      "planned_findings": [
        "f14",
        "f15",
        "f8",
        "f7",
        "f9",
        "f10"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1700,
      "summary": "실시간 검출·추적, 장기 시공간 흐름 지도, 단기 궤적 예측, 보행자 행동 모델과 시뮬레이션, 운영 규칙, 기록 재현의 반응형 대체가 대표 접근이다. [사실][^ref-1211]",
      "planned_findings": [
        "f14",
        "f7",
        "f1",
        "f9",
        "f2",
        "f3",
        "f8",
        "f12",
        "f13",
        "f15",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "사람 표현은 원문 상태 Draft 인 ROS 규약 제안 REP-155(ROS4HRI)가 있고, 보행자 시뮬레이션에는 HuNavSim·Open-RMF CrowdSim(Menge), 데이터셋에는 THÖR·ATC가 있다. [사실][^ref-1206]",
      "planned_findings": [
        "f4",
        "f5",
        "f12",
        "f13",
        "f6",
        "f7",
        "f11"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "움직임 지도 서베이, 궤적 예측 서베이, 사회적 힘 모델, 쇼핑몰 혼잡 예상 로봇, 보행자 흐름 지도 벤치마크, 사회적 내비게이션 평가 지침, Waymax가 대표 자료다. [사실][^ref-1211]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f8",
        "f9",
        "f11",
        "f17"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1000,
      "summary": "ROP는 여러 로봇·설비가 보고한 사람 위치를 모아 집계·익명화한 흐름 모델로 계획에 넘기고, 온보드 검출·감속·정지·국소 회피와 공공 인파관리 시스템은 연계 대상으로 둔다. [추정][^ref-1206]",
      "planned_findings": [
        "f20",
        "f21",
        "f16"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "18번(현재 상태)과 34번(가정한 미래)을 구분해 연결하고, 지도·계획·안전·개인정보·AI·시험 영역과 네 현장 유형 영역에 잇는다. [추정][^ref-1206]",
      "planned_findings": [
        "f22"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "기존 oq-256(부분 근거만 있음)과 oq-261을 열림으로 두고, 사람 위치 통합 형식·혼잡의 스케줄 반영 효과·공공 인파 데이터 연동에 관한 새 질문 3건을 올린다. [추정][^ref-1128]",
      "planned_findings": [
        "f17",
        "f18",
        "f4",
        "f15",
        "f16"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주 15건, 1차 조건부 승인 수정 16건 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"6. 대표 접근법과 기술\" 절(1,457자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"4. 핵심 개념과 용어\" 절(1,175자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,049자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"8. 대표 연구와 자료\" 절(999자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(944자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"11. 열린 질문\" 절(865자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area19-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"3. 왜 중요한가\" 절(532자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 19. 사람·보행자 모델 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건), 1차 조건부 승인 수정 16건 이행 | run 2026-09-30-20",
  "index_updates": {
    "home_recent": "2026-09-30 — 19. 사람·보행자 모델: 영역 심화로 3~11절 신규 작성(움직임 지도·궤적 예측·보행자 시뮬레이션, 물류창고·병원·상업 시설·기타 사례)",
    "category_recent": "2026-09-30 — 19. 사람·보행자 모델: 영역 심화로 3~11절 신규 작성, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈을 나눠 연결",
    "area_recent": "2026-09-30 — 19. 사람·보행자 모델: 3~11절 신규 작성(신뢰도 low, 출처 15건, 열린 질문 신규 3건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "social-force-model",
      "term_ko": "사회적 힘 모델",
      "term_en": "Social Force Model",
      "definition": "보행자 움직임을 원하는 속도로의 가속, 다른 보행자·벽과의 거리 유지(반발), 끌림을 나타내는 가상의 힘의 합으로 계산하는 보행자 행동 모델이다.",
      "description": "Helbing·Molnár(1995)가 제안했으며 군중 시뮬레이션에서 집단 현상의 자기조직화를 재현한다.",
      "related_areas": [
        19,
        34
      ],
      "sources": [
        "ref-1207"
      ]
    },
    {
      "action": "new",
      "slug": "human-motion-trajectory-prediction",
      "term_ko": "사람 움직임 궤적 예측",
      "term_en": "Human Motion Trajectory Prediction",
      "definition": "관측된 과거 위치와 주변 맥락(다른 사람·장애물·목적지)을 바탕으로 사람의 가까운 미래 이동 경로를 추정하는 기법이다.",
      "description": "Rudenko 외 서베이는 방법을 움직임 모델링 방식과 사용하는 맥락 정보 수준의 두 축으로 분류한다.",
      "related_areas": [
        19,
        46
      ],
      "sources": [
        "ref-1205"
      ]
    },
    {
      "action": "new",
      "slug": "social-robot-navigation",
      "term_ko": "사회적 내비게이션",
      "term_en": "Social Robot Navigation (Human-aware Navigation)",
      "definition": "로봇이 사람 사이를 이동할 때 안전뿐 아니라 쾌적성·가독성·예의 같은 사회적 원칙을 지키도록 경로와 행동을 정하는 주행 방식이다.",
      "description": "Francis 외(2023)는 안전·쾌적·가독성·예의·사회적 역량·상대 이해·능동성·맥락 대응을 원칙으로 들었다.",
      "related_areas": [
        19,
        49,
        54
      ],
      "sources": [
        "ref-1079"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1204",
      "org": "Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11))",
      "title": "Survey of maps of dynamics for mobile robots",
      "published": "2023",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649231190428",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 움직임 지도(MoD)의 정의·입력·용도(전역 계획, 위치 추정, 사람 움직임 예측)를 정리한 서베이. 검색 결과에서 서지와 초록 요지만 확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1205",
      "org": "Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020)",
      "title": "Human Motion Trajectory Prediction: A Survey",
      "published": "2019-12-17",
      "url": "https://arxiv.org/abs/1905.06113",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사람 움직임 궤적 예측 방법을 움직임 모델링 방식과 맥락 정보 수준으로 분류하고 데이터셋·지표를 검토한 서베이. arXiv 초록 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1206",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS4HRI 의 사람 표현 규약 제안(원문 상태 Draft). person·face·body·voice 식별자, /humans/… 토픽, person_<ID> 프레임과 위치 신뢰도, 익명 사람 표시를 정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1207",
      "org": "Helbing, D., & Molnár, P. (Physical Review E 51(5))",
      "title": "Social force model for pedestrian dynamics",
      "published": "1995-05-01",
      "url": "https://link.aps.org/doi/10.1103/PhysRevE.51.4282",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 보행자 움직임을 '사회적 힘'(원하는 속도로의 가속, 타인·경계와의 거리 유지, 끌림)으로 모델링한 고전 논문. 검색 요약으로만 확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1208",
      "org": "Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020)",
      "title": "THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset",
      "published": "2019-12-11",
      "url": "https://arxiv.org/abs/1909.04403",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실내 환경의 사람 궤적·시선 데이터셋. 위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표 정답과 3D 라이다·이동로봇 데이터를 포함한다. arXiv 초록 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1209",
      "org": "ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외",
      "title": "ATC shopping center tracking dataset",
      "published": null,
      "url": "https://dil.atr.jp/crest2010_HRI/ATC_dataset/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "오사카 ATC 쇼핑센터 약 900㎡ 구역에서 3D 거리 센서 49대로 92일간 보행자를 추적한 공개 데이터셋 소개 페이지. 데이터 필드와 연구 목적 전용 이용 조건을 밝힌다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1210",
      "org": "행정안전부 (대한민국 정책브리핑)",
      "title": "29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방",
      "published": "2023-12-27",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148924176",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기지국 접속정보로 인파 밀집도를 추정해 위험도를 산출하고 지자체에 경보를 보내는 인파관리지원시스템의 전국 100곳 정식 운영을 알린 정부 보도자료.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1211",
      "org": "Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI)",
      "title": "Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation",
      "published": "2022-07-04",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "대학 건물 한 달 관측으로 26개 시공간 보행자 흐름 지도 방법을 학습·비교하는 벤치마크와, 흐름 예측을 쓴 주행이 사람을 덜 방해함을 보인 소규모 현장 실험.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1079",
      "org": "Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction)",
      "title": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms",
      "published": "2023-09-19",
      "url": "https://arxiv.org/abs/2306.16740",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 내비게이션의 원칙 정의와 지표·시나리오·데이터셋·시뮬레이터 평가 지침, 지표 프레임워크를 제안한 공동 논문. arXiv 초록 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1213",
      "org": "Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023)",
      "title": "HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation",
      "published": "2023-09-13",
      "url": "https://arxiv.org/abs/2305.01303",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 기반 오픈소스 사람 보행 행동 시뮬레이터와 사회적 내비게이션 지표 묶음을 소개. arXiv 초록 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-406",
      "org": "Open Robotics (osrf/ros2multirobotbook)",
      "title": "Programming Multiple Robots with ROS 2 — Simulation",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 시뮬레이션 장. 선택 기능인 CrowdSim 이 Menge 엔진으로 사람 에이전트를 제어하고 rmf_traffic_editor 에서 켠다고 설명한다. 같은 URL 이 이미 있으면 기존 id 로 병합.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1215",
      "org": "ILIAD 프로젝트 컨소시엄 (EU Horizon 2020)",
      "title": "Concluding ILIAD",
      "published": "2021-06",
      "url": "https://iliad-project.eu/concluding-iliad/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 자율 지게차 플릿 프로젝트 ILIAD 의 최종 시연(Orkla Foods 창고 두 곳), 다중 센서 작업자 검출, 움직임 지도 기반 사람 인식 계획을 정리한 프로젝트 결산 글.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1128",
      "org": "Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv)",
      "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research",
      "published": "2023-10-12",
      "url": "https://arxiv.org/abs/2310.08710",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제 주행 데이터로 장면을 초기화·재생하는 자율주행 시뮬레이터. 로그 재생 에이전트와 반응형 모의 에이전트(IDM·학습 모델)를 제공한다. arXiv 초록·본문 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1217",
      "org": "조선비즈 (이정아, 다음 뉴스 게재)",
      "title": "로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘",
      "published": "2024-07-12",
      "url": "https://v.daum.net/v/bc4riunbUE",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원의 로봇 운영 기사. 낮 혼잡 대응을 위한 전용 경로 스티커, 환자·휠체어를 만나면 무조건 기다리는 설계, 7종 73대·20개월 35,492건 운영을 전한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    },
    {
      "id": "ref-1218",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013)",
      "title": "Will I bother here? - A robot anticipating its influence on pedestrian walking comfort",
      "published": "2013-03",
      "url": "https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 쇼핑몰 로봇이 보행자 행동 모델로 혼잡을 예상해 보행 쾌적성을 해치지 않게 위치를 계획하는 방법. 검색 결과로 서지·요지만 확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가?",
      "areas": [
        19,
        18,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가?",
      "areas": [
        19,
        26,
        63
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가?",
      "areas": [
        19,
        66
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    }
  ],
  "additional_research_requests": [
    "5절 제조 공장·가정: 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 브리프에 없어 쓰지 못했다. 두 현장 유형의 사례 조사가 필요하다.",
    "5절 실외: 이 영역의 로봇 적용 사례(예: 실외 배송로봇이 보행자 흐름을 경로에 반영한 사례)가 없어 사례 묶음을 쓰지 못했다.",
    "5절 모든 사례: 시작 조건·완료·인계 칸이 미확인이다. 물류창고(ILIAD)·병원(한림대학교성심병원)의 사람 흐름 반영이 처리 시간·지연에 준 정량 효과도 미확인이다.",
    "6·8절: Kidokoro 외(HRI 2013) 원문을 열어 보행 쾌적성 효과 수치를 확인하고, Rudenko 외 서베이의 세부 분류 명칭과 Vintr 외의 최우수 방법 이름을 확인할 필요가 있다.",
    "7절: REP-155(ROS4HRI)의 최종 채택 상태(Draft 여부)와 ILIAD 프로젝트 시작 연도를 확인할 필요가 있다.",
    "5·8절: 병원 로봇의 대기 규칙(환자·휠체어를 만나면 무조건 대기)을 독립 출처로 교차 확인할 필요가 있다.",
    "브리프 self_check 에서 예산으로 빠진 Mavrogiannis 외 사회적 내비게이션 서베이, ILIAD Safety Stack 논문, 병원 군중 동행 리뷰, Kairos(4D 장면 그래프 기반 존재·흐름 예측)를 다음 실행에서 조사하면 6·8절을 보강할 수 있다."
  ],
  "fixes_applied": [
    "f2 '보행자 중심의 지상 2차원' 한정구 삭제 — 4절 궤적 예측 항목과 6절·8절에서 한정구 없이 '여러 연구 공동체의 궤적 예측 방법'으로 썼다.",
    "f9 비교 방법 수와 방법 이름 — 6절 장기 흐름 지도에 '26개 방법'으로 쓰고 HyT×GMM 등 구체 방법 이름을 빼고 '공간과 시간을 독립적으로 모델링한 연속 시공간 방법이 우수했다'로 썼으며, 8절도 '26개 흐름 지도 방법'으로 맞췄다.",
    "f10 표본 한계 — 5절 기타 사례의 예외·성과 칸과 서술 문장에 '40분 세션 네 번, 방법당 두 세션'과 로봇 없는 대조 측정(211명 중 불만 0명)을 같은 문장에 밝히고 Toyota HSR 기종은 쓰지 않았다(수행 자원 칸은 '기종 미확인').",
    "f8 효과 서술 — 5절 상업 시설 사례의 예외·성과 칸을 '노출만 최대화한 로봇에 비해 주변 보행자가 보행 쾌적성을 더 좋게 인식, 효과 수치는 미확인'으로 쓰고 원문 미열람을 밝혔다.",
    "f15 대기 대상과 출처 한계 — 5절 병원 사례·6절 운영 규칙에서 '환자나 휠체어와 마주치면'으로 고치고 기사 1건(조선비즈, 2024-07-12) 기준임을 밝혔으며, 직접 인용은 '무조건 기다리도록 설계됐다' 짧은 구절 1회로 제한했다.",
    "f5 person ID 부여 노드 — 7절 표 아래 문장에서 얼굴 인식·음성 인식 노드로만 예시하고 '옷 색 같은 신체 특징'은 쓰지 않았다.",
    "f4 REP-155 지위 — 4절과 7절 표에서 '표준'이 아니라 '원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안'으로 쓰고 최종 채택 여부를 미확인으로 두었다. standards_updates 도 종류를 프레임워크로 두고 요약에 Draft를 밝혔다.",
    "f11 '논문 177편 검토' — 본문 어디에도 쓰지 않았다.",
    "f14 프로젝트 기간 — 5절 물류창고 서술에 '2021-06 종료'로만 쓰고 '2017~2021'은 쓰지 않았다.",
    "f21 범위 수정 — 9절 표에서 CCTV를 빼고 기지국 접속정보 기반 공공 시스템만 연계 대상으로 두었으며, 로봇 탑재 안전 기능(안전 센서 기반 감속·정지, 국소 회피)은 연계 대상으로, 구역별 속도·진입 제한은 49. 사람 근접 안전과 연결되는 운영 제약으로 나눠 썼다.",
    "5절 실외 — 실외에서는 이 영역의 로봇 적용 사례를 찾지 못했음을 밝히고 f16은 9절 연계 대상, f17은 6절 방법 참고로만 두었으며 site_matrix_updates 에 실외 칸을 넣지 않았다.",
    "5절 상업 시설 — 로봇 적용 사례를 f8(Kidokoro 외)로 세우고 f7(ATC 데이터셋)은 서술에서 '로봇 적용 사례가 아니라 보행자 관측 데이터셋'으로 밝혔으며, 제조 공장·가정 사례를 찾지 못했음을 절 끝에 명시했다.",
    "11절 — 기존 oq-261을 열림으로 싣고 새 근거가 없음을 밝혔으며, oq-256은 f17·f18을 부분 근거로 싣되 열림을 유지했다(open_question_updates 에 상태 변경을 내지 않음).",
    "용어집 — '로그 재생 에이전트·반응형 에이전트'는 신규 등록하지 않고 4절에서 기존 용어 log-playback(로그 재생)으로 링크했으며, 사회적 힘 모델·사람 움직임 궤적 예측·사회적 내비게이션 세 용어만 glossary_updates 로 냈다.",
    "원문 미열람 표시 — ref-1204, ref-1207, ref-1218 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 세 항목에 source_unopened: true 를 넣었다.",
    "ref-1210 제목 — 각주 정의와 reference_updates 의 제목을 '29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방'으로 적었다.",
    "분량 초과 자동 분리: 19. 사람·보행자 모델 본문 10,329자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,332자"
  ],
  "standards_updates": [
    {
      "name": "REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI)",
      "kind": "프레임워크",
      "org": "ROS (ros-infrastructure/rep)",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "related_areas": [
        19,
        18,
        53
      ],
      "summary": "사람을 영속 person ID 와 얼굴·몸·음성 ID 로 표현하고 사람별 좌표 프레임과 위치 신뢰도, 익명 사람 표시를 정한 ROS 규약 제안이다. 2022-01-11 작성, 원문 상태 Draft이며 최종 채택 여부는 미확인이다.",
      "ref_id": "ref-1206"
    },
    {
      "name": "HuNavSim (ROS 2 사람 보행 시뮬레이터)",
      "kind": "오픈소스",
      "org": "Pérez-Higueras, N. 외 (Universidad Pablo de Olavide)",
      "url": "https://arxiv.org/abs/2305.01303",
      "related_areas": [
        19,
        34,
        54
      ],
      "summary": "ROS 2 기반으로 Gazebo 같은 로봇 시뮬레이터와 함께 이동로봇 주변 사람의 보행 행동을 시뮬레이션하고 사회적 내비게이션 벤치마킹 지표 묶음을 제공한다.",
      "ref_id": "ref-1213"
    },
    {
      "name": "Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션)",
      "kind": "오픈소스",
      "org": "Open Robotics",
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "related_areas": [
        19,
        34
      ],
      "summary": "Open-RMF 시뮬레이션의 선택 기능으로 rmf_traffic_editor 에서 켜며 Menge 엔진이 사람 에이전트를 제어한다.",
      "ref_id": "ref-406"
    },
    {
      "name": "사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms)",
      "kind": "프레임워크",
      "org": "Francis, A. 외",
      "url": "https://arxiv.org/abs/2306.16740",
      "related_areas": [
        19,
        54
      ],
      "summary": "사회적 내비게이션 원칙 여덟 가지와 지표·시나리오·데이터셋·시뮬레이터 사용 지침, 결과 비교용 지표 프레임워크를 제안한다(2023-09).",
      "ref_id": "ref-1079"
    }
  ]
}
```

### runs/2026-09-30-20/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area19-s6.md (1,457자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area19-s4.md (1,175자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area19-s7.md (1,049자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area19-s8.md (999자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area19-s10.md (944자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area19-s11.md (865자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area19-s3.md (532자)
```

### runs/2026-09-30-20/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md

```markdown
---
title: "19. 사람·보행자 모델"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [움직임 지도, 사람 궤적 예측, 사회적 힘 모델, 사회적 내비게이션, ROS4HRI]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1206, ref-1207, ref-1208, ref-1209, ref-1210, ref-1211, ref-1079, ref-1213, ref-406, ref-1215, ref-1128, ref-1217, ref-1218]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 19. 사람·보행자 모델

# 19. 사람·보행자 모델

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 현장 사람의 위치와 흐름은 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 계획과 안전에 반영된다. [추정][^ref-1204][^ref-1205][^ref-1211][^ref-1215]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 왜 중요한가](../../topics/2026/2026-09-30-area19-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 핵심 개념은 사람 흐름을 저장하는 지도, 가까운 미래 경로를 추정하는 예측, 보행자 행동을 계산하는 모델, 사람 정보를 주고받는 표현 규약이다. [추정][^ref-1204][^ref-1205][^ref-1207][^ref-1206]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

근거를 찾은 네 현장 유형(물류창고·병원·상업 시설·기타)의 사례를 나눠 적는다. 현장 유형 × 대분류 적용 사례는 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

**현장 유형:** 물류창고

**사례:** 창고 자율 지게차 플릿이 작업자 이동 패턴을 반영해 주행(EU ILIAD 프로젝트, 스웨덴 외레브로)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 창고 작업자의 위치와 현장별 사람 이동 패턴(정보) [사실][^ref-1215] |
| 수행 자원 | 자율 지게차 플릿. 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적 [사실][^ref-1215] |
| 제약 | 움직임 지도로 학습한 사람 흐름에 맞춘 경로 계획, 움직임별 사회적 비용으로 계산한 속도 제약 [사실][^ref-1215] |
| 완료·인계 | 미확인 |
| 예외·성과 | 전원 투입부터 첫 임무까지 1시간 미만. 사람 방해·처리 시간에 대한 정량 효과는 미확인 [사실][^ref-1215] |

ILIAD 프로젝트(2021-06 종료)는 외레브로의 Orkla Foods 창고 두 곳(상온·냉장)에서 자율 지게차 플릿을 시연했다. [사실][^ref-1215] 작업자 검출·추적은 로봇 탑재 기능이므로 ROP 관점에서는 연계 대상이고, 이 영역에서 볼 부분은 현장별 사람 이동 패턴을 지도로 학습해 경로 계획에 쓴 점이다. [추정][^ref-1215]

**현장 유형:** 병원

**사례:** 병원 복도에서 운반 로봇이 낮 시간 혼잡에 대응(한림대학교성심병원, 한국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 낮 시간 복도의 환자·휠체어와 로봇 통행 경로(사람·공간) [사실][^ref-1217] |
| 수행 자원 | 로봇 7종 73대(기사 기준) [사실][^ref-1217] |
| 제약 | 로봇 통행 경로와 작업 정지 지점에 전용 스티커 표시, 환자나 휠체어와 마주치면 로봇이 무조건 대기 [사실][^ref-1217] |
| 완료·인계 | 미확인 |
| 예외·성과 | 20개월간 서비스 35,492건(기사 기준). 대기 규칙이 처리 시간에 준 영향은 미확인 [사실][^ref-1217] |

조선비즈 기사(2024-07-12)에 따르면 이 병원은 밤에 인식한 경로가 낮의 혼잡에서는 원활하지 않을 수 있다고 보고 경로를 따로 표시했고, 로봇은 환자나 휠체어와 마주치면 “무조건 기다리도록 설계됐다”. [사실][^ref-1217] 이 대기 규칙은 기사 1건 기준이며 독립 출처로 확인되지 않았다. [사실][^ref-1217]

**현장 유형:** 상업 시설

**사례:** 쇼핑몰에서 사람을 모으는 로봇이 보행자 혼잡을 예상해 위치를 계획(Kidokoro 외, HRI 2013)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 로봇 주변을 지나가는 보행자와 그 흐름(사람) [사실][^ref-1218] |
| 수행 자원 | 사람을 모으는 로봇과, 보행자 행동 모델로 가상 주행 상황을 시뮬레이션하는 계획 기능 [사실][^ref-1218] |
| 제약 | 로봇이 모은 사람 때문에 생기는 혼잡으로 지나가는 보행자의 보행 쾌적성을 해치지 않을 것 [사실][^ref-1218] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 노출만 최대화한 로봇에 비해 주변 보행자가 보행 쾌적성을 더 좋게 인식. 효과 수치는 미확인 [사실][^ref-1218] |

이 연구는 혼잡을 예상하고 미리 피하도록 계획하는 방법을 실제 쇼핑몰에서 시험했다(원문 미열람, 검색 결과 기준). [사실][^ref-1218] 같은 상업 시설 유형의 ATC 데이터셋은 로봇 적용 사례가 아니라 보행자 관측 데이터셋이다. 오사카 ATC 쇼핑센터의 약 900㎡ 구역에 천장 3차원 거리 센서 49대를 두어 2012-10-24~2013-11-29 가운데 92일(매주 수·일요일 9:40~20:20) 보행자를 추적했고, 시각·사람 id·위치·높이·속도·이동 방향·몸 방향을 연구 목적으로만 제공한다. [사실][^ref-1209]

**현장 유형:** 기타

**사례:** 대학 건물에서 시간대별 사람 흐름을 따르는 로봇 주행(Vintr 외, 프랑스 UTBM)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 대학 건물 공간(약 500㎡)의 보행자 흐름. 2019-03 한 달간 3차원 라이다로 600만 건 이상 검출 [사실][^ref-1211] |
| 수행 자원 | 3차원 라이다(Velodyne HDL-32E) 관측과 흐름 지도를 쓰는 이동로봇(기종 미확인) [사실][^ref-1211] |
| 제약 | 사람과의 예상 조우(Expected Encounters)와 예상 경로 길이를 함께 따지는 경로 계획 [사실][^ref-1211] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 불편을 드러낸 사람: 예측형 주행 두 세션 모두 0명, 반응형 주행 2명·1명(40분 세션 네 번, 방법당 두 세션) [사실][^ref-1211] |

2019-12-12~13 UTBM 대학 홀 현장 실험에서 사람 흐름의 시간대 패턴을 따르는 예측형 주행은 두 세션 모두 불편을 드러낸 사람이 0명, 반응형 주행은 2명·1명이었지만, 40분 세션 네 번(방법당 두 세션)의 매우 작은 표본이며 로봇이 없는 대조 측정에서는 통행자 211명 중 불만이 0명이었다. [사실][^ref-1211]

**사례를 찾지 못한 현장 유형:** 실외에서는 이 영역의 로봇 적용 사례를 찾지 못했다. 행정안전부 인파관리지원시스템은 로봇 사례가 아닌 연계 대상으로 9절에서, 자율주행 시뮬레이터 Waymax는 기록 재현 방법 참고로 6절에서 다룬다. 제조 공장·가정 사례도 찾지 못했다.

## 6. 대표 접근법과 기술

사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1211][^ref-1215][^ref-1217]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 표현에는 원문 상태가 Draft 인 ROS 규약 제안이 있고, 보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다. [사실][^ref-1206][^ref-1213]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1204][^ref-1211]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 로봇과 설비 센서가 보고한 사람 위치를 공통 좌표·시각·신뢰도로 모으고, 구역·시간대별로 집계·익명화한 사람 흐름·혼잡 모델을 유지해 경로·구역 비용, 작업 시간 추정, 배정·스케줄링에 넘긴다 [추정][^ref-1206][^ref-1211] | 로봇의 온보드 사람 검출·추적, 안전 센서 기반 감속·정지, 국소 회피(연계 대상) [추정][^ref-1215] |
| 로봇 자체 지능·제어(운영 규칙) | 로봇에 대기·우회 같은 운영 규칙을 요청하고, 구역별 속도·진입 제한을 운영 제약으로 관리한다(49. 사람 근접 안전과 연결) [추정][^ref-1217] | 요청받은 규칙을 실제 동작으로 수행하는 로봇 제어(연계 대상) [추정][^ref-1217] |
| 업종별 조건 | 공공 인파 밀집 정보를 받으면 실외 로봇의 경로·운행 제약으로 반영하는 쪽을 맡는다(연동 사례 미확인) [추정][^ref-1210] | 행정안전부 인파관리지원시스템: 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사 기지국 접속정보로 인파 밀집도·혼잡도를 추정하고 협소 도로 비율 같은 공간 특성을 더해 위험도를 산출해 지도에 색으로 표시하며, 위험 수준에 따라 지자체 공무원에게 경보를 보낸다(연계 대상) [사실][^ref-1210] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

사람 표현의 영속 ID 가 얼굴·음성 인식과 연결될 수 있으므로, ROP가 보관하는 사람 정보는 개인이 아니라 구역·시간대 집계로 두는 것이 이 경계를 지키는 방식으로 보인다. [추정][^ref-1206] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1206][^ref-1213]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area19-s10.md)에 있다.

## 11. 열린 질문

기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1206]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](../../topics/2026/2026-09-30-area19-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1206]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1207]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1210]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-09-30
[^ref-1211]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1213]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-1215]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1217]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1218]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md

```markdown
---
title: "19. 사람·보행자 모델"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 19
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 19. 사람·보행자 모델

# 19. 사람·보행자 모델

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]

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

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s6.md

```markdown
---
title: "19. 사람·보행자 모델 — 대표 접근법과 기술"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1207, ref-1209, ref-1211, ref-1213, ref-406, ref-1215, ref-1128, ref-1217, ref-1218]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#6
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 대표 접근법과 기술

# 19. 사람·보행자 모델 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1211][^ref-1215][^ref-1217]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1211][^ref-1215][^ref-1217]

### 실시간 사람 검출·추적

로봇 탑재 센서나 공간에 설치한 센서([인프라 장착 센서](../../glossary/infrastructure-mounted-sensing.md))로 사람의 현재 위치를 얻는다. ILIAD 창고 지게차는 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적했다. [사실][^ref-1215] ATC 데이터셋은 천장 3차원 거리 센서 49대로 쇼핑센터 보행자를 추적했다. [사실][^ref-1209] 로봇 탑재 검출은 제조사 쪽 기능이어서 ROP는 그 결과를 받아 쓰는 쪽이다. [추정][^ref-1215]

### 장기 시공간 흐름 지도

장기 관측으로 시간대·구역별 사람 흐름을 학습해 전역 경로 계획에 쓴다. [사실][^ref-1204] Vintr 외(2022-07)는 대학 건물에서 한 달간 모은 600만 건 이상의 사람 검출로 26개 방법을 학습시키고 경로 계획 시뮬레이션에서 예상 조우와 예상 경로 길이로 비교해, 공간과 시간을 독립적으로 모델링한 연속 시공간 방법이 우수했다고 보고했다. [사실][^ref-1211] ILIAD는 현장별 사람 이동 패턴을 움직임 지도로 학습하고, 질적 궤적 계산(qualitative trajectory calculus)으로 움직임별 사회적 비용을 추정해 속도 제약을 계산했다. [사실][^ref-1215]

### 단기 궤적 예측

관측된 과거 위치와 맥락으로 사람의 가까운 미래 경로를 추정한다. Rudenko 외 서베이는 방법을 움직임 모델링 방식과 맥락 정보 수준으로 분류하고 데이터셋·지표를 검토한다. [사실][^ref-1205] 세부 분류 명칭은 이번에 확인하지 못했다.

### 보행자 행동 모델과 시뮬레이션

사회적 힘 모델(1995)은 가속·반발·끌림 항의 합으로 보행자 움직임을 계산한다. [사실][^ref-1207] Kidokoro 외(2013)는 보행자 행동 모델로 가상의 주행 상황을 시뮬레이션해 혼잡을 예상하고 미리 피하도록 계획했다. [사실][^ref-1218] HuNavSim은 ROS 2 기반 오픈소스 도구로 이동로봇 주변 사람의 다양한 보행 행동을 시뮬레이션한다. [사실][^ref-1213] Open-RMF 시뮬레이션은 Menge 엔진을 쓰는 선택 기능 CrowdSim 으로 사람 에이전트를 움직인다. [사실][^ref-406] 이런 쓰임은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 기능이다. [추정][^ref-1213][^ref-406]

### 운영 규칙

모델 대신 규칙으로 사람 흐름에 대응하기도 한다. 한림대학교성심병원은 전용 경로·작업 정지 지점 표시와 환자·휠체어를 만나면 대기하는 설계를 썼다(기사 1건 기준). [사실][^ref-1217] 대기 규칙이 처리 시간에 준 영향은 미확인이다.

### 기록 재현에서 사람을 반응하게 만들기

Waymax(2023-10)는 기록된 궤적을 따르는 로그 재생 에이전트와, 규칙 기반(지능형 운전자 모델, IDM)·학습 기반 행동 모델로 다른 참가자에 반응하는 모의 에이전트를 함께 제공한다. IDM 에이전트는 기록된 경로를 따르면서 속도만 조정하며, 강화학습 에이전트가 모의 에이전트의 행동에 과적합할 수 있음이 보고됐다. [사실][^ref-1128] 로봇 플릿 재현에서도 기록된 사람을 사회적 힘 모델·HuNavSim·Menge 같은 보행자 모델로 기록 위치에서 이어받아 움직이게 하는 방식이 가능해 보이지만, 모델 편향이 생기며 로봇 플릿 재현에 적용한 공개 사례는 이번에 찾지 못했다. [추정][^ref-1128][^ref-1207][^ref-1213][^ref-406]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1207]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1211]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1213]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-406]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Simulation, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-1215]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1217]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1218]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s4.md

```markdown
---
title: "19. 사람·보행자 모델 — 핵심 개념과 용어"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1206, ref-1207, ref-1079, ref-1128]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#4
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 핵심 개념과 용어

# 19. 사람·보행자 모델 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 핵심 개념은 사람 흐름을 저장하는 지도, 가까운 미래 경로를 추정하는 예측, 보행자 행동을 계산하는 모델, 사람 정보를 주고받는 표현 규약이다. [추정][^ref-1204][^ref-1205][^ref-1207][^ref-1206]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 핵심 개념은 사람 흐름을 저장하는 지도, 가까운 미래 경로를 추정하는 예측, 보행자 행동을 계산하는 모델, 사람 정보를 주고받는 표현 규약이다. [추정][^ref-1204][^ref-1205][^ref-1207][^ref-1206]

- **[움직임 지도](../../glossary/maps-of-dynamics.md)(Maps of Dynamics, MoD)** — 환경의 전형적인 움직임 패턴을 저장하는 지도로, 궤적이나 짧고 끊긴 움직임 관측으로 만들 수 있으며 전역 경로 계획·위치 추정 개선·사람 움직임 예측에 쓰여 로봇이 감지 범위 밖과 미래의 움직임을 예상하게 한다(2023년 서베이 기준). [사실][^ref-1204]
- **사람 움직임 궤적 예측(Human Motion Trajectory Prediction)** — 사람의 가까운 미래 이동 경로를 추정하는 기법이다. Rudenko 외 서베이(arXiv 2019-12판, IJRR 2020)는 여러 연구 공동체의 궤적 예측 방법을 움직임 모델링 방식과 사용하는 맥락 정보 수준이라는 두 축으로 분류하고 데이터셋과 성능 지표를 함께 검토한다. [사실][^ref-1205]
- **사회적 힘 모델(Social Force Model)** — 보행자 움직임을 원하는 속도로 가속하려는 항, 다른 보행자·경계와 거리를 두려는 반발 항, 끌림 항의 합으로 보는 모델이며, 1995-05에 발표되어 군중 시뮬레이션에서 관측되는 집단 현상의 자기조직화를 재현한다. [사실][^ref-1207]
- **사람 표현과 위치 신뢰도(ROS4HRI)** — ROS 규약 제안 REP-155(2022-01-11 작성, 원문 상태 Draft)는 사람을 영속적인 person ID 와 추적 중에만 유효한 얼굴·몸·음성 ID 의 조합으로 나타내고, 사람마다 좌표 프레임과 위치 신뢰도(1.0 지금 보임, 1 미만 이전에 보임, 0 추적된 적 없음)를 두며 아직 식별되지 않은 익명 사람도 표시한다. [사실][^ref-1206]
- **사회적 내비게이션(Social Robot Navigation)** — Francis 외(2023-09)는 안전·쾌적·가독성·예의·사회적 역량·상대 이해·능동성·맥락 대응의 원칙을 지키는 로봇을 사회적 내비게이션 로봇으로 정의했다. [사실][^ref-1079]
- **로그 재생 에이전트와 반응형 에이전트(Log-replay Agent / Reactive Agent)** — 시뮬레이션에서 기록된 궤적을 그대로 따르는 참가자와, 다른 참가자에 반응해 움직임을 바꾸는 모델 기반 참가자를 구분하는 말로, 자율주행 시뮬레이터 Waymax(2023-10)가 둘을 함께 제공한다. [사실][^ref-1128] 관련 용어: [로그 재생](../../glossary/log-playback.md).

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1206]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1207]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-09-19, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s7.md

```markdown
---
title: "19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1206, ref-1208, ref-1209, ref-1079, ref-1213, ref-406]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#7
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스

# 19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 표현에는 원문 상태가 Draft 인 ROS 규약 제안이 있고, 보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다. [사실][^ref-1206][^ref-1213]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 표현에는 원문 상태가 Draft 인 ROS 규약 제안이 있고, 보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다. [사실][^ref-1206][^ref-1213]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| REP-155 (ROS4HRI) | 프레임워크(ROS 규약 제안, 원문 상태 Draft) | 사람을 person·face·body·voice ID로 표현하고 `/humans/persons/tracked` 같은 토픽, `person_<ID>` 좌표 프레임과 위치 신뢰도, 익명 사람 표시를 정한다. 2022-01-11 작성, 최종 채택 여부 미확인 [사실][^ref-1206] | ROS REP 저장소 |
| HuNavSim | 오픈소스 | ROS 2 기반으로 Gazebo 같은 로봇 시뮬레이터와 함께 사람 보행 행동을 시뮬레이션하고 사회적 내비게이션 벤치마킹 지표 묶음을 제공(2023-09 arXiv판) [사실][^ref-1213] | 논문(RA-L 2023) |
| [Open-RMF](../../glossary/open-rmf.md) CrowdSim (Menge 엔진) | 오픈소스 | Open-RMF 시뮬레이션의 선택 기능으로 rmf_traffic_editor 에서 켜며 Menge 가 사람 에이전트를 제어 [사실][^ref-406] | Open-RMF 문서 |
| THÖR 데이터셋 | 공개 데이터셋 | 실내 사람 궤적·시선 데이터와 위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표 정답, 3차원 라이다와 이동로봇 데이터 포함(2019-12 arXiv판, RA-L 2020) [사실][^ref-1208] | 논문 |
| ATC 쇼핑센터 추적 데이터셋 | 공개 데이터셋 | 쇼핑센터 92일 보행자 추적, 연구 목적 전용 [사실][^ref-1209] | ATR |
| 사회적 내비게이션 평가 원칙·지침(Francis 외) | 프레임워크 | 지표·시나리오·데이터셋·시뮬레이터 사용 지침과, 서로 다른 시뮬레이터·로봇·데이터셋 결과를 비교하는 지표 프레임워크(2023-09) [사실][^ref-1079] | 논문 |

REP-155 의 영속 person ID 는 얼굴 인식·음성 인식 노드 같은 식별 노드가 부여해 세션을 넘어 같은 사람을 다시 알아보게 하므로, 사람 표현이 개인 식별 정보와 연결될 수 있다. [사실][^ref-1206] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1206]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1208]: Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020), THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset, 2019-12-11, https://arxiv.org/abs/1909.04403, 접근일 2026-09-30
[^ref-1209]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-09-19, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1213]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-406]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Simulation, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s8.md

```markdown
---
title: "19. 사람·보행자 모델 — 대표 연구와 자료"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1207, ref-1211, ref-1079, ref-1128, ref-1218]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#8
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 대표 연구와 자료

# 19. 사람·보행자 모델 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1204][^ref-1211]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1204][^ref-1211]

- Kucner 외, Survey of maps of dynamics for mobile robots(IJRR, 2023) — 움직임 지도의 정의·입력·용도(전역 계획, 위치 추정 개선, 사람 움직임 예측)를 정리한 서베이다(원문 미열람). [사실][^ref-1204]
- Rudenko 외, Human Motion Trajectory Prediction: A Survey(IJRR 2020, arXiv 2019-12판) — 궤적 예측 방법의 두 축 분류 체계와 데이터셋·지표 검토. [사실][^ref-1205]
- Helbing·Molnár, Social force model for pedestrian dynamics(Physical Review E, 1995-05) — 보행자 시뮬레이션에 널리 쓰이는 사회적 힘 모델의 원 논문이며 기준일은 1995-05다(원문 미열람). [사실][^ref-1207]
- Kidokoro 외, Will I bother here?(HRI 2013) — 쇼핑몰 로봇이 보행자 혼잡을 예상해 보행 쾌적성을 해치지 않게 계획하는 방법으로, HRI 2013 최우수 논문상을 받았다(원문 미열람). [사실][^ref-1218]
- Vintr 외, Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation(Frontiers in Robotics and AI, 2022-07) — 26개 흐름 지도 방법의 벤치마크와 소규모 현장 실험. [사실][^ref-1211]
- Francis 외(저자 52명), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms(2023-09) — 사회적 내비게이션 원칙과 평가 지침. [사실][^ref-1079]
- Gulino 외, Waymax(2023-10) — 로그 재생·반응형 에이전트를 함께 쓰는 자율주행 시뮬레이터로, 기록 재현 방법의 참고 자료다. [사실][^ref-1128]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1207]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1211]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-09-19, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1218]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s10.md

```markdown
---
title: "19. 사람·보행자 모델 — 다른 연구영역과의 연결"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1206, ref-1207, ref-1209, ref-1210, ref-1211, ref-1079, ref-1213, ref-406, ref-1215, ref-1128, ref-1217, ref-1218]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#10
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 다른 연구영역과의 연결

# 19. 사람·보행자 모델 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1206][^ref-1213]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1206][^ref-1213]

- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 사람 위치의 현재 상태와 신선도·위치 신뢰도 표현을 공유한다. [추정][^ref-1206]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 보행자 행동 모델·군중 시뮬레이션으로 가정한 미래를 실험한다. [추정][^ref-1207][^ref-1213][^ref-406]
- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 기록 재현에서 사람을 반응형으로 바꾸는 문제(oq-256)가 걸려 있다. [추정][^ref-1128]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 사람 흐름 지도를 얹을 공간 모델이다. [추정][^ref-1204]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 로봇 전용 경로·작업 정지 지점 같은 구역 의미와 이어진다. [추정][^ref-1217]
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 혼잡을 반영한 작업 시간 추정에 쓰인다. [추정][^ref-1211]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 사람 흐름을 경로 비용·속도 제약으로 반영한다. [추정][^ref-1211][^ref-1215]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 현장에서 사람과 마주칠 때의 대기·양보가 협업 문제와 겹친다. [추정][^ref-1217]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 구역별 속도·진입 제한 같은 운영 제약과 이어진다. [추정][^ref-1215][^ref-1217]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 영속 사람 ID 가 개인 식별 정보와 연결될 수 있다. [추정][^ref-1206]
- [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) — 학습 기반 궤적 예측·흐름 지도는 L. AI·학습 기술의 방법을 이 영역에 적용한 것이다. [추정][^ref-1205][^ref-1211]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 사회적 내비게이션 평가 지표와 흐름 지도 벤치마크가 이어진다. [추정][^ref-1079][^ref-1211]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — ILIAD 창고 사례. [추정][^ref-1215]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 복도 혼잡 대응 사례. [추정][^ref-1217]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 쇼핑몰 로봇과 ATC 데이터셋. [추정][^ref-1218][^ref-1209]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 공공 인파관리 시스템이 연계 대상이며, 로봇 적용 사례는 찾지 못했다. [추정][^ref-1210]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1206]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1207]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1210]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-09-30
[^ref-1211]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-09-19, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1213]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-406]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Simulation, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-1215]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1217]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1218]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s11.md

```markdown
---
title: "19. 사람·보행자 모델 — 열린 질문"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1206, ref-1128]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#11
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 열린 질문

# 19. 사람·보행자 모델 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1206]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1206]

- **oq-256** (상태: 열림) 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? 자율주행 시뮬레이터는 기록 재생 에이전트를 반응형 모델로 바꾸지만 모델 편향이 생기며, 로봇 플릿 재현에 적용한 공개 사례는 찾지 못해 부분 근거만 있다(6절). [추정][^ref-1128]
- **oq-261** (상태: 열림) 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? 영속 사람 ID 가 얼굴·음성 인식과 연결될 수 있다는 점(7절)과 관련되지만 이번에 새 근거는 없다.
- **신규** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-20) 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가?
- **신규** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-20) 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가?
- **신규** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-20) 기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1206]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-20/pages/topics/2026/2026-09-30-area19-s3.md

```markdown
---
title: "19. 사람·보행자 모델 — 왜 중요한가"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1204, ref-1205, ref-1211, ref-1215, ref-1217, ref-1218]
last_run: 2026-09-30
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#3
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 왜 중요한가

# 19. 사람·보행자 모델 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료를 종합하면, 현장 사람의 위치와 흐름은 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 계획과 안전에 반영된다. [추정][^ref-1204][^ref-1205][^ref-1211][^ref-1215]
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료를 종합하면, 현장 사람의 위치와 흐름은 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 계획과 안전에 반영된다. [추정][^ref-1204][^ref-1205][^ref-1211][^ref-1215]

사람 흐름을 모르면 생기는 문제는 현장에서 이미 드러난다. 한국 병원 사례 기사에 따르면 붐비지 않는 밤에 인식한 로봇 경로가 낮의 혼잡에서는 원활하지 않을 수 있어, 병원이 로봇 통행 경로와 작업 정지 지점을 따로 표시했다(조선비즈 2024-07-12 기사 1건 기준). [사실][^ref-1217]

반대로 로봇이 혼잡을 만들기도 한다. 쇼핑몰에서 사람을 모으는 로봇이 혼잡을 일으켜 지나가는 보행자의 보행 쾌적성을 해치는 문제가 2013년 연구에서 다뤄졌다. [사실][^ref-1218]

다만 효과 근거는 아직 얇다. 사람 흐름을 반영한 주행의 효과를 보인 자료는 대학 건물의 소규모 현장 실험과 쇼핑몰 현장 시험 정도이고, 물류창고·병원의 정량 효과는 확인되지 않았다. [추정][^ref-1211][^ref-1218]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1204]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1211]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1215]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1217]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1218]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-20 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-20 | 19. 사람·보행자 모델 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1167건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 326개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
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
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
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
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
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
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
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
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
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
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
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
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
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
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
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
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
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

### docs/open-questions.md (요약: 대상 영역 [19] 에 걸린 2건 / 전체 266건)

```markdown
- oq-256 [열림] 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? (영역 36, 19, 33)
- oq-261 [열림] 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? (영역 53, 19)
```
