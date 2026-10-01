(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-10
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 49. 사람 근접 안전 (M. 안전)
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

### runs/2026-09-30-10/target.json

```json
{
  "run_id": "2026-09-30-10",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 119,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 49,
    "area_name": "49. 사람 근접 안전",
    "category": "M. 안전",
    "category_letter": "M"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=49"
}
```

### runs/2026-09-30-10/research.json

```json
{
  "run_id": "2026-09-30-10",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 49,
    "area_name": "49. 사람 근접 안전",
    "category": "M. 안전"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 속도·분리 감시(SSM), 동력·힘 제한(PFL), 보호 분리 거리, 운용 구역, 속도 제한·진입 금지 구역, 움직임 지도(Maps of Dynamics) 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·실외·제조 공장 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 인지형 배정·교통 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙 제223조, VDA 5050 구역, Nav2 Collision Monitor 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]",
    "로봇과 사람 사이의 분리 거리는 표준에서 어떤 변수(사람 속도, 반응 시간, 정지 거리, 측정 불확실도)로 계산하며, 실제 구현에서 어떤 한계가 보고되는가? (섹션 4·6·8 겨냥)",
    "이동 로봇·협동로봇·실외 로봇의 사람 근접 안전을 다루는 국내외 표준·법규·인증(ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙)은 구역·속도·감지·정지를 어떻게 규정하는가? (섹션 7 겨냥, 한국 자료 우선)",
    "구역별 속도 제한과 진입 금지를 플릿 관제 수준에서 표현·전달하는 인터페이스와 오픈소스(VDA 5050 구역, Nav2 Collision Monitor 등)는 무엇이며 안전 기능으로 인정되는가? (섹션 6·7·9 겨냥)",
    "물류창고·병원·실외·상업 시설 같은 현장에서 사람 근접 시 감속·정지·양보를 적용한 사례와 그 속도 기준은 무엇인가? (섹션 5 겨냥)",
    "안전 거리와 별개로 사람이 편안하게 느끼는 거리·속도, 사람의 움직임을 배정·교통에 반영하는 연구는 무엇을 보고하는가? (섹션 6·8 겨냥)",
    "사람 근접 안전에서 ROP가 직접 맡을 것과 로봇 제조사·시스템 통합자·설비에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Marvel·Norcross(NIST, Robotics and Computer-Integrated Manufacturing)는 ISO/TS 15066 의 속도·분리 감시(SSM)에서 보호 분리 거리가 사람 이동 속도, 로봇 반응 시간, 로봇 정지 시간(정지 거리), 침입 거리, 로봇·사람 위치 측정 불확실도로 계산되며, 분리 거리가 이 값 이하가 되면 안전 감시 정지를 건다고 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보호 분리 거리 구성요소: 사람 속도 vH, 로봇 반응 시간 TR, 로봇 정지 시간 TS, 침입 거리 C, 위치 불확실도 ZR·ZS. 로봇 정지 시간은 속도·하중·자세·브레이크 마모에 따라 비선형으로 변한다.",
      "as_of": "2016",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "같은 연구는 사람 속도로 ISO 13855 의 1,600 mm/s(최악 조건 2,000 mm/s), 침입 거리로 ISO 13855 기준 850~1,200 mm 를 들고, NIST 시험에서 레일 장착 로봇의 반응 시간을 약 0.113초로 측정했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 13855 사람 속도 1,600 mm/s(최악 2,000 mm/s); 생체역학 연구의 평지 보행 속도 1,250~1,510 mm/s; 침입 거리 850~1,200 mm; NIST 측정 반응 시간 약 0.113 s(레일 장착 로봇).",
      "as_of": "2016",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "같은 연구는 SSM 식이 속도의 방향을 무시하고 크기만 써서 멀어지는 로봇도 불필요한 정지를 일으킬 수 있고, 센서 잡음이 속도 추정 오차를 키우며, 갱신 주기가 낮을수록 로봇 평균 속도가 떨어지고, 보호 거리는 주로 로봇 제동 거리와 반응 시간이 좌우한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "속도를 크기로만 다뤄 정지한 작업자 옆에서 멀어지는 로봇도 정지를 유발(오탐); mm 단위 위치 오차가 수백 mm/s 속도 오차로 증폭; 30 Hz 대 1,000 Hz 갱신에서 평균 속도 차이.",
      "as_of": "2016",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "Hartmann 외(arXiv 2602.17822, 2026-02)는 ISO 10218-1/2 의 2025년 개정판이 협동 작업 기술 시방서 ISO/TS 15066 을 선택적 지침에서 규범적 요구로 본문에 통합하고, 로봇·협동 적용의 새 분류와 사이버보안 요구를 더했다고 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1076"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO/TS 15066 이 선택적 지침에서 'normative integration'으로 올라가 주 안전 체계의 필수 요소가 됨; 협동 적용의 새 분류, 네트워크 로봇의 무단 접근 방지 요구 확대.",
      "as_of": "2026-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "국내 산업안전보건기준에 관한 규칙 제223조는 산업용 로봇 운전 중 위험 방지를 위해 높이 1.8미터 이상의 울타리와 안전매트 설치를 기본으로 하되 2016년부터 한국산업표준 등 안전기준에 맞는 협동 운전 로봇은 울타리 설치를 면제하며, 협동 작업 방식은 속도·분리 감시(SSM), 핸드 가이딩(HGC), 동력·힘 제한(PFL)으로 나뉜다고 지디넷코리아가 전했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1082"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사: 산업용 로봇은 '안전매트와 높이 1.8미터 이상의 울타리 설치'가 기본이나 2016년부터 특정 안전기준 충족 시 면제. SSM=작업자 접근 시 속도 감소·정지, PFL=제한된 힘으로 작동. 법령 원문은 열지 못함.",
      "as_of": "2024-03",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "ISO 3691-4:2023(무인 산업용 트럭과 그 시스템의 안전 요구·검증)은 사람이 있는 운용 구역에서는 인력 감지를 요구하고, 훈련된 인원만 들어가는 제한 구역과 울타리 등으로 사람을 배제한 구역을 구분해 구역에 따라 보호 조치를 달리하는 것으로 알려져 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-1077"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 결과 요약 기준: operating zone(사람 있음, 인력 감지 필수), restricted zone(훈련 인원만), confined zone(사람 배제, 보호 조치 완화). ISO 페이지 403 으로 원문 미열람.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "같은 표준은 인력 감지를 끄거나 완전히 작동하지 않는 상황(예: 도킹)에서 속도를 0.3 m/s 이하로 제한하고, 인력 감지 성능을 서 있는 사람(지름 200 mm·높이 600 mm 원통)과 누운 사람(지름 70 mm·길이 400 mm 원통) 시험편으로 확인하는 것으로 알려져 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-1077"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 결과 요약 기준(원문 미확인): 감지 무효화 시 0.3 m/s 이하, 시험편 수직 원통 200×600 mm·바닥 수평 원통 70×400 mm, 접촉 전 정지.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR)을 특정 적용과 현장에 맞춰 통합·배치할 때의 안전 요구를 다루며, 배치 시스템의 위험성 평가는 IMR 시스템 통합자가 수행하도록 하고 모바일 매니퓰레이터와 잔여 위험, 최종 사용자 정보·교육을 포함한다고 The Robot Report 가 전했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1088"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "\"The risk assessment shall be performed by the IMR system integrator\". Part 1 은 IMR 제조 요구·용어, Part 2 는 시스템·적용, Part 3 은 사용자 요구(발행 예정).",
      "as_of": "2023-10-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "한국로봇산업진흥원의 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거해 배송 등 목적의 자율주행·원격제어 로봇과 관제장치의 조합을 대상으로 최고 속도 15 km/h 이하·최대 질량 500 kg 이하를 요구하고, 주변 인식·비상정지·횡단보도 통행·관제장치 등을 심사하며 2년 주기 정기점검을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1080",
        "ref-1081"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "KIRIA 페이지: 심사 항목 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치; 15 km/h·500 kg 은 지디넷코리아 기사(2023-07-28)와 일치.",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "지디넷코리아(2023-07-28)는 산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준이 로봇과 적재물 질량 합계에 따라 최고 속도를 230 kg 초과 5 km/h, 100 kg 초과 10 km/h, 그 이하 15 km/h 로 나누고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단하게 하며 심사 항목을 16가지로 두었다고 전했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"보행 신호 중에 로봇이 도착하면 정지 상태로 대기 후 다음 보행 신호에 횡단할 수 있도록 제한\"; 질량별 5/10/15 km/h; 16가지 심사 항목.",
      "as_of": "2023-07-28",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "VDA 5050 3.0.0 은 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 진입 금지(BLOCKED), 플릿 관제 승인 후 진입(RELEASE), 최고 속도 제한(SPEED_LIMIT), 자율 재계획 금지, 동작 유발, 우선·벌점·방향 구역을 정의하며, 속도 제한 구역에서는 로봇이 정해진 최고 속도보다 빠르게 달려서는 안 된다고 규정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Mobile robots shall not drive faster than the defined maximum speed within this zone.\" 윤곽 기반: BLOCKED·LINE_GUIDED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT·ACTION; 중심점 기반: PRIORITY·PENALTY·DIRECTED·BIDIRECTED.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "VDA 5050 3.0.0 은 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 밝혀, 구역·속도 제한 전달이 안전 기능 자체를 대신하지 않음을 명시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 면책 문구: 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 적용하지 않는다(원문 영어, 재서술).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "ROS 2 내비게이션 스택 Nav2 의 Collision Monitor 는 컨트롤러 속도 명령을 거르는 독립 노드로, 영역 안 장애물 점 수에 따른 정지·감속(비율)·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두고 여러 영역이 동시에 걸리면 가장 강한 조치를 쓰지만, 하드 실시간 안전 인증을 제공하지 않아 안전 등급 하드웨어를 대신하지 않는다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1078"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"When multiple zones trigger at once, the most aggressive one is used (e.g. stop > slow 50% > slow 10%)\"; 입력은 레이저·포인트클라우드·IR/초음파·비용 지도; 하드 실시간 안전 인증 없음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "아마존은 풀필먼트 센터에서 로봇 구역에 들어가는 직원이 로보틱스 테크 조끼를 착용·활성화하면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 조끼를 켜면 접근 경로가 생겨 로봇이 자동으로 감속·우회; 직원 인용 \"If they get too close to me, they stop.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "물류창고",
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "Francis 외 52명(ACM Transactions on Human-Robot Interaction, arXiv 2306.16740)은 사회적 로봇 주행의 원칙을 안전·편안함·가독성·예의·사회적 역량·상대 이해·능동성·맥락 적합성 8가지로 정하고, 알고리즘을 공정하게 비교하기 위한 지표·시나리오·벤치마크·시뮬레이터 지침을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "8원칙: \"safety, comfort, legibility, politeness, social competency, agent understanding, proactivity, and responsiveness to context\"; 지표·시나리오·데이터셋·시뮬레이터 4축 지침.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Jafari·Nguyen·Liu(arXiv 2604.13677, 2026-04)는 이동 로봇과 자원 보행자의 일대일 조우 실험에서 보행자가 보고한 편안함이 최소 거리와 최소 예상 충돌 시간 같은 운동학 변수와 중간 정도의 유의한 상관을 보였고, 이들을 합친 복합 지표가 오즈비 3.67 로 가장 잘 예측했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1089"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"moderate but significant correlations for most variables\"; 복합 지표 오즈비 3.67; 실험 장소·참가자 수는 초록에 없음.",
      "as_of": "2026-04",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "Rondoni 외(Scientific Reports, 2024-08)는 병원 물류용 HOSBOT 과 TIAGo 를 시뮬레이션 병원 환경에서 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 속도가 높을수록 정확도가 떨어졌다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "속도 선정 근거로 사람 보행 하한 0.6~1.3 m/s 인용; 두 로봇 모두 성공률 거의 100%; 속도 증가 시 성능 저하; 시뮬레이션 환경 평가.",
      "as_of": "2024-08-07",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "Farrell 외(UC San Diego, arXiv 2503.21141, 2025-03)는 학습 기반 제어 장벽 함수(CBF)를 Open-RMF 에 통합해 창고의 다중 로봇·다중 행위자 상황에서 보행자를 포함한 정적·동적 장애물을 피하는 안전 강화 제어를 제안하고 로봇 수·속도·장애물 수를 바꿔 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CBF 를 OpenRMF 에 통합해 \"adaptive and safety-enhanced controls in multi-robot, multi-agent scenarios\"; 정량 수치는 초록에 없음.",
      "as_of": "2025-03-27",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Kazemi Eskeri 외(IROS 2025)의 사람 인지형 작업 배정(HATA)은 과거 사람 이동 패턴을 담은 시공간 질의형 움직임 지도(Maps of Dynamics)로 사람이 작업 실행 시간에 주는 영향을 확률적 비용으로 추정해 배정에 반영했고, 사람 움직임을 고려하지 않는 기준선보다 임무 완료 시간을 26%, 기존 기준선보다 19% 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1087"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MoD 기반 확률적 비용 함수; 동역학 무시 기준선 대비 26%, 기존 기준선 대비 19% 완료 시간 감소; 창고·자율 배송을 적용처로 제시(실험 환경 세부는 초록에 없음).",
      "as_of": "2025-08-27",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에 대해, 분리 거리는 고정값이 아니라 사람 속도·반응 시간·정지 거리·측정 불확실도로 그때그때 계산되고(f1~f3), 감속·정지 기준은 적용 유형별 표준·인증이 구역·속도 상한으로 정하며(f6·f7·f9·f10), 사람이 편안하게 느끼는 거리·충돌 시간은 안전 정지 거리와 별도의 기준이 필요한 것으로 보인다(f15·f16).",
      "tag": "추정",
      "source_ids": [
        "ref-1075",
        "ref-1077",
        "ref-1080",
        "ref-1081",
        "ref-1083",
        "ref-1089"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정: 계산형 보호 거리(f1~f3), 구역별 속도 상한(f6·f7·f9·f10), 편안함 지표(f15·f16).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 안전 거리가 로봇 정지 성능과 센서 갱신에 따라 달라져 로봇·현장마다 다르고(f1~f3), 협동로봇·무인 트럭·실외 로봇이 각기 다른 표준·법규로 울타리 면제·구역·속도 상한을 정하며(f4~f10), 보수적인 감속·정지가 처리량과 수용성에 영향을 주기 때문이다(f3·f16·f19).",
      "tag": "추정",
      "source_ids": [
        "ref-1075",
        "ref-1076",
        "ref-1082",
        "ref-1077",
        "ref-1088",
        "ref-1080",
        "ref-1081",
        "ref-1089",
        "ref-1087"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정: 로봇별 보호 거리 차이, 적용 유형별 규정 차이, 감속·정지의 효율 영향.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 49. 사람 근접 안전에서 ROP가 직접 맡을 범위는 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하는 것(f11), 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하는 것(f14·f18·f19), 그 조정과 정지·재개 이력을 기록하는 것이며, 이는 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다(f12·f13).",
      "tag": "추정",
      "source_ids": [
        "ref-1079",
        "ref-1084",
        "ref-1086",
        "ref-1087",
        "ref-1078"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정: 구역·속도 제한 전달, 사람 인지형 배정·교통, 기록은 플랫폼 몫; VDA 5050·Nav2 모두 안전 기능·인증이 아님을 명시.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "연계 대상: 분류 원문 19장 기준으로 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(f1·f5·f6·f7)은 로봇 제조사와 시스템 통합자에, 현장 배치의 위험성 평가(f8)는 시스템 통합자에, 울타리·안전매트·인터록(f5)은 설비 안전 쪽에, 실외 인증 대상인 로봇·관제장치 조합의 적합성(f9)은 운영 사업자에 속하므로, ROP 는 그 설정값과 상태를 받아 계획에 반영하는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1075",
        "ref-1082",
        "ref-1077",
        "ref-1088",
        "ref-1080"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정: 로봇 자체 안전 기능·통합자 위험성 평가·설비 안전 제어는 외부 연계 대상.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "이 영역은 위험성 평가·정지·재개의 48. 안전·위험 관리(f8), 표준·인증의 50. 안전 표준·인증·사고 조사(f4~f10), 사람 이동 모델의 19. 사람·보행자 모델(f16·f19), 구역을 담는 16. 장소 의미·지도 관리(f11), 구역을 전달하는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f11·f12), 사람 인지형 배정의 25. 작업 배정 — MRTA(f19), 구역·속도를 반영하는 27. 다중 로봇 경로·교통 관리 — MAPF(f11·f18), 협동 작업의 31. 사람–로봇 협업(f1·f5), 법규의 59. 법·규제·보험·라이선스(f5·f9), 수용성의 60. 노동·수용성·접근성(f15·f16), 평가의 54. 시험·형식 검증·벤치마크(f15·f17), 적용 현장인 61. 물류창고(f14·f18)·63. 병원·의료(f17)·66. 실외(f9·f10)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1088",
        "ref-1076",
        "ref-1080",
        "ref-1089",
        "ref-1087",
        "ref-1079",
        "ref-1086",
        "ref-1075",
        "ref-1082",
        "ref-1083",
        "ref-1085",
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "연결 제안 종합.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1075",
      "org": "Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing)",
      "title": "Implementing Speed and Separation Monitoring in Collaborative Robot Workcells",
      "published": "2016",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ISO/TS 15066 속도·분리 감시의 보호 분리 거리 식을 구성요소별로 분해하고 NIST 시험 결과와 구현 지침·한계를 제시한 논문(PMC 저자 원고 본문).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1076",
      "org": "Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv)",
      "title": "Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066",
      "published": "2026-02-19",
      "url": "https://arxiv.org/abs/2602.17822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISO 10218-1/2 2011판과 2025판을 비교해 ISO/TS 15066 의 규범적 통합, 새 분류, 사이버보안 요구 확대를 분석한 프리프린트(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1077",
      "org": "ISO (ISO/TC 110)",
      "title": "ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (제목 일부는 검색 결과 기준)",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 무인 산업용 트럭(AGV·AMR)과 그 시스템의 안전 요구·검증 표준. ISO 페이지가 403 이라 구역·인력 감지·속도 관련 내용은 검색 결과 요약으로만 확인했다.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1078",
      "org": "Open Navigation (ros-navigation/navigation2)",
      "title": "nav2_collision_monitor — README",
      "published": null,
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Nav2 Collision Monitor 의 정지·감속·제한·접근 모델, 다중 영역 우선순위, 입력 센서, 하드 실시간 안전 인증이 없다는 주의를 설명하는 공식 저장소 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-navigation/navigation2/main/nav2_collision_monitor/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1079",
      "org": "VDA / VDMA (VDA5050/VDA5050)",
      "title": "VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 3.0.0 명세 원문. 6.4.1절의 구역 유형(BLOCKED·RELEASE·SPEED_LIMIT 등)과 안전 표준이 아니라는 면책 문구를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1080",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "지능형 로봇법 제40조의2 에 따른 실외이동로봇 운행안전인증의 대상, 최고 속도·질량 기준, 8개 심사 항목, 처리기간, 사후관리를 안내하는 인증기관 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1081",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준)",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준(질량별 속도 상한, 횡단보도 통행, 16가지 심사 항목)을 전한 기사. 15 km/h 상한은 인증기관 페이지와 일치한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1082",
      "org": "지디넷코리아",
      "title": "\"협동로봇 충돌 안전 계산하고 써야죠\"",
      "published": "2024-03",
      "url": "https://zdnet.co.kr/view/?no=20240305160245",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업안전보건기준에 관한 규칙 제223조의 울타리·안전매트 기본 요구와 2016년 협동 운전 예외, SSM·HGC·PFL 협동 방식, 충돌 안전 계산을 한국로봇산업협회·세이프틱스 인터뷰로 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv)",
      "title": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms",
      "published": "2023-06-29",
      "url": "https://arxiv.org/abs/2306.16740",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사회적 로봇 주행의 8가지 원칙과 지표·시나리오·벤치마크·시뮬레이터 평가 지침을 제시한 공동 논문(초록 확인, 학술지판 ACM THRI 2025).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1084",
      "org": "Amazon",
      "title": "Ever wonder how people and robots team up on your Amazon order?",
      "published": null,
      "url": "https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "풀필먼트 센터에서 직원과 로봇이 함께 일하는 방식을 소개하며 로보틱스 테크 조끼로 로봇이 감속·우회·정지한다고 설명하는 아마존 자사 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1085",
      "org": "Rondoni 외 (Scientific Reports)",
      "title": "Navigation benchmarking for autonomous mobile robots in hospital environments",
      "published": "2024-08-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "병원용 HOSBOT 과 TIAGo 의 주행을 시뮬레이션 병원 환경에서 세 속도·7개 지표로 벤치마크한 논문(PMC 본문).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1086",
      "org": "Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv)",
      "title": "Safe Human Robot Navigation in Warehouse Scenario",
      "published": "2025-03-27",
      "url": "https://arxiv.org/abs/2503.21141",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "학습 기반 제어 장벽 함수를 Open-RMF 에 통합해 창고 다중 로봇 환경에서 보행자 포함 장애물 회피를 강화한 프리프린트(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1087",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "사람 이동 패턴을 담은 움직임 지도(Maps of Dynamics)로 사람이 작업 시간에 주는 영향을 추정해 다중 로봇 배정에 반영한 연구(초록 확인, 제목 일부는 검색 결과 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1088",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "ANSI/A3 R15.08-2(산업용 이동 로봇 시스템·적용 안전 요구) 발행과 통합자 위험성 평가 책임, 시리즈 구성을 전한 전문지 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1089",
      "org": "Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv)",
      "title": "Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters",
      "published": "2026-04-15",
      "url": "https://arxiv.org/abs/2604.13677",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이동 로봇–보행자 일대일 조우 실험에서 최소 거리·최소 예상 충돌 시간 등 운동학 변수로 보행자 편안함을 예측한 프리프린트(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/human-proximity-safety.md",
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
      "rationale": "섹션 3: f21(왜 중요한가), f20(핵심 질문 답, 추정) / 섹션 4: 속도·분리 감시·보호 분리 거리 f1·f2, 동력·힘 제한 f5, 운용 구역 f6, 속도 제한·진입 금지·승인 구역 f11, 움직임 지도 f19, 제어 장벽 함수 f18, 사회적 주행 원칙 f15 / 섹션 5: 물류창고 — f14(제약: 조끼 신호로 감속·우회·정지, 벤더 주장 병기)·f18(연구, 창고 시나리오), 병원 — f17(제약: 보행 속도 기반 0.2~1.0 m/s, 시뮬레이션 병원임을 명시), 실외 — f9·f10(제약: 15 km/h·질량별 속도 상한·횡단보도 대기). 제조 공장은 f5(산업용 로봇 사업장 규정)로 서술하되 현장 사례가 아님을 밝히고, 상업 시설·가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 계산형 보호 거리 f1~f3, 로봇 측 감속·정지 영역 f13, 플릿 수준 구역·속도 제한 f11·f12, 착용형 신호 f14, 사람 인지형 배정·교통 f18·f19, 편안함 지표 f16 / 섹션 7: ISO 10218·ISO/TS 15066 f4, ISO 3691-4 f6·f7(원문 미열람), ANSI/A3 R15.08-2 f8, 실외이동로봇 운행안전인증 f9·f10, 산업안전보건기준에 관한 규칙 제223조 f5, VDA 5050 구역 f11·f12, Nav2 Collision Monitor f13 / 섹션 8: f1·f3·f15·f16·f17·f18·f19·f4 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 19, 20, 21, 25, 27, 31, 48, 50, 54, 59, 60, 61, 63, 66 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사 페이지 섹션 7 에 f4·f6~f10 반영, 16. 장소 의미·지도 관리 페이지에 f11 구역 유형 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "속도·분리 감시",
      "term_en": "Speed and Separation Monitoring (SSM)",
      "definition": "로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다."
    },
    {
      "term_ko": "보호 분리 거리",
      "term_en": "Protective Separation Distance",
      "definition": "사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다."
    },
    {
      "term_ko": "동력·힘 제한",
      "term_en": "Power and Force Limiting (PFL)",
      "definition": "로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다."
    },
    {
      "term_ko": "움직임 지도",
      "term_en": "Maps of Dynamics (MoD)",
      "definition": "과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다."
    },
    {
      "term_ko": "제어 장벽 함수",
      "term_en": "Control Barrier Function (CBF)",
      "definition": "로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다."
    }
  ],
  "open_questions_new": [
    "플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? | 관련 영역: 49. 사람 근접 안전, 48. 안전·위험 관리 | 근거: f12 | 종류: 일반",
    "실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? | 관련 영역: 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사 | 근거: f10 | 종류: 출처 충돌",
    "국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? | 관련 영역: 49. 사람 근접 안전, 59. 법·규제·보험·라이선스 | 근거: f9 | 종류: 일반",
    "착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 21. 상호운용 표준·적합성 | 근거: f14 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 1,
    "unverified": [
      "f6·f7 ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s, 시험편 치수: ISO·ANSI 블로그 페이지 403 으로 원문 미열람, 검색 결과 요약 기준이라 추정·low 로 둠",
      "f5 산업안전보건기준에 관한 규칙 제223조 조문: law.go.kr 페이지에서 조문 본문을 읽지 못했고 yeslaw 는 인증서 오류로 열지 못해 기사(ref-1082)만 근거",
      "f8 ANSI/A3 R15.08-2 원문 미열람(유료). 플릿(IMRF) 포함 여부는 검색 요약에만 있어 claim 에 넣지 않음",
      "f14 아마존 조끼: 2018년 25개 창고 도입 등 수치는 검색 요약(위키백과)에만 있어 넣지 않음. 독립 출처 교차 확인 실패",
      "f15 근접학 거리(0.45 m·1.2 m) 예시는 검색 요약에만 있어 넣지 않음",
      "f16 실험 장소·참가자 수, f18 정량 결과, f19 실험 환경은 초록에 없어 미확인",
      "f10 심사 항목 16가지와 f9 인증기관 페이지 8개 항목의 차이: 출처 충돌로 열린 질문에 올림",
      "ISO 13482(개인 돌봄 로봇) 개정판 내용: 검색 1회에서 2025년 개정 세부를 확인하지 못해 넣지 않음",
      "상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례는 찾지 못함(쇼핑몰·공항 검색 1회, 찾은 소매점 배치 연구 arXiv 2601.01946 은 근접 안전 내용이 없어 제외)",
      "제조 공장 현장 사례는 규정(f5)과 작업셀 연구(f1~f3)만 있고 현장 유형을 밝힌 적용 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f1~f3·f5~f7: 안전 등급 인력 감지·보호 정지·SSM·PFL 은 로봇 제조사·시스템 통합자의 안전 기능(원문 19장 로봇 자체 지능·제어, 설비 안전 제어 연계 대상)이므로 개념·기준 근거로만 쓰고 f23 에서 '연계 대상: '으로 구분함",
      "f13: Nav2 Collision Monitor 는 로봇 측 로컬 회피 계층(연계 대상)이며 안전 인증이 없음을 명시; ROP 직접 범위로 서술하지 않도록 주의",
      "f9·f10: 실외이동로봇 인증 대상은 로봇과 관제장치의 조합이라 관제장치 쪽이 ROP 범위와 겹칠 수 있음. 인증 책임은 운영 사업자 몫으로 f23 에서 구분",
      "f18: 제어 장벽 함수는 로봇 제어 계층 기법이지만 Open-RMF 플릿 계층에 통합한 사례로만 인용"
    ],
    "budget_used": {
      "queries": 13,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 ISO 13482·ISO 13855 원문, 상업 시설·가정 사례, 국내 서비스 로봇 기준을 더 넣지 못했다. 주의: 입력의 이전 브리프 2026-09-30-08 도 ref-1075~ref-1089 를 썼으나 실행 컨텍스트가 이 구간을 이 실행 전용으로 예약했다고 밝혀 그대로 썼다(퍼블리셔의 id 충돌 확인 필요). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건; VDA 5050·ISO 3691-4 가 기존 참고문헌에 있으면 퍼블리셔가 같은 URL 로 합쳐야 한다). 원문 열람: 14건 열었고(webfetch 12건, github_raw 2건) ISO 3691-4(ref-1077)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Marvel·Norcross(ref-1075)·Rondoni 외(ref-1085)는 PMC 본문, 나머지는 초록 페이지다. 교차 확인 1건(f9: 15 km/h·500 kg 을 인증기관 페이지와 기사로 확인). 벤더 문서는 아마존(ref-1084) 1건이며 f14 는 vendor_claim·추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에는 f20 으로 답했고 결론은 '분리 거리는 계산값이고, 감속·정지 상한은 적용 유형별 표준·인증이 구역·속도로 정하며, 편안함 기준은 별도'라는 추정이다. 현장 유형 사례는 물류창고(f14·f18)·병원(f17, 시뮬레이션)·실외(f9·f10)이며 제조 공장은 규정 수준, 상업 시설·가정·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-1080)·지디넷코리아 2건(ref-1081·ref-1082)이다. 용어집에 이미 있는 운용 구역·구역 집합·위험성평가·협동 적용·실외이동로봇 운행안전인증·공공 영역 이동로봇·필터 마스크·해제 구역은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### docs/categories/safety/human-proximity-safety.md

```markdown
---
title: "49. 사람 근접 안전"
type: area
category: "M. 안전"
area_no: 49
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [M. 안전](index.md) › 49. 사람 근접 안전

# 49. 사람 근접 안전

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]

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

### docs/categories/safety/safety-and-risk-management.md (요약)

```markdown
# 48. 안전·위험 관리

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
```

### docs/categories/safety/safety-standards-certification-and-incident-investigation.md (요약)

```markdown
# 50. 안전 표준·인증·사고 조사

소속 대분류: M. 안전 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1074건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 293개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- guidance-graph: 안내 그래프 (Guidance Graph)
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
- imitation-learning: 모방 학습 (Imitation Learning)
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
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
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
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
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
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
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

### docs/open-questions.md (요약: 대상 영역 [49] 에 걸린 0건 / 전체 228건)

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

### runs/2026-09-30-08/research.md

```markdown
# 리서치 브리프 2026-09-30-08

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-08 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 45. 문서·도면·장면 이해 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 문서 레이아웃 분석, 표 구조 인식, 출처 근거 연결, 패놉틱 심볼 스포팅, 외부 인프라 카메라 인식 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(도면 인식)·제조 공장(고정 카메라 인식)·물류창고(CCTV 기반 다중 로봇 조율)·실외(다중 로봇 장면 그래프) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 문서 파싱, LLM 기반 데이터시트 추출, 도면 심볼 인식, 고정 카메라·로봇 인식 융합 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Docling, OmniDocBench, LangExtract, CubiCasa5K, FloorPlanCAD, AI Hub 건축 도면 데이터 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-147·oq-196·oq-197 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
2. 매뉴얼·데이터시트 같은 기술 문서를 파싱하고 LLM으로 구조화 정보(예: 자산관리셸 속성)를 뽑을 때 보고된 정확도와 실패 원인은 무엇인가? (섹션 3·6·8 겨냥)
3. 추출한 항목마다 원문 위치를 근거로 붙여 사람이 대조·확정하게 하는 공개 구현이나 연구가 있는가? (oq-147, 섹션 6·7 겨냥)
4. 건축 도면(평면도·CAD) 인식의 대표 데이터셋·벤치마크와 성능은 무엇이며, 병원·공장·물류창고·상업 시설 같은 비주거 도면에서도 확인됐는가? (oq-196, oq-197, 섹션 5·7·8 겨냥, 한국 자료 우선)
5. 고정 카메라(CCTV·인프라 카메라)와 여러 로봇의 인식 결과를 모아 플랫폼 수준에서 공간 상태를 인식한 연구·현장 사례와 그 한계는 무엇인가? (섹션 5·6·8 겨냥)
6. 문서·도면·장면 이해에 쓰는 오픈소스·데이터셋·벤치마크는 무엇이며 라이선스·언어 범위는 어떤가? (섹션 4·7 겨냥)
7. 문서·도면·장면 이해에서 ROP가 직접 맡을 것과 로봇 자체 인식·설비·설계 도구에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | AECV-Bench(Kondratenko 외, arXiv 2601.04819, 2026-01)는 평면도 120장의 문·창·침실·화장실 개수 세기와 질의응답 192쌍으로 최신 멀티모달 모델의 건축·엔지니어링 도면 이해를 평가해, 글자 인식·텍스트 추출은 정확도 최대 0.95로 가장 높고 공간 추론은 중간, 심볼 이해·개수 세기는 0.40~0.55로 가장 낮다고 보고했다. | ref-1088 | 아니오 | medium | 2026-01 | — | — |
| f2 | [사실] | CubiCasa5K(Kalervo 외, arXiv 1904.01920, 2019-04)는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 단위 조밀 주석을 단 데이터셋과 다중 작업 합성곱 신경망 모델을 공개했다. | ref-063 | 아니오 | medium | 2019-04 | — | — |
| f3 | [사실] | FloorPlanCAD(Fan 외, arXiv 2105.07147, 2021-11 개정)는 주거·상업 건물의 CAD 평면도 1만 장 이상을 벡터 그래픽으로 담고 30개 객체 범주를 주석한 데이터셋으로, 셀 수 있는 심볼 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 찾는 패놉틱 심볼 스포팅 과제를 제안했다. | ref-067 | 아니오 | medium | 2021-11 | — | — |
| f4 | [사실] | 상업 시설 사례로, Su 외(Sensors, 2022-03)는 쇼핑몰 평면도 25장(점포 1,340개)을 대상으로 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고 2단계 영역 성장 분할과 문자 인식으로 평면도의 각 점포 공간을 식별해 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%를 보고했으며 실내 로봇 주행을 활용처로 들었다. | ref-1078 | 아니오 | medium | 2022-03-25 | 상업 시설 / 작업 대상 | — |
| f5 | [사실] | 과학기술정보통신부·한국지능정보사회진흥원의 AI Hub 「건축 도면 데이터」(2022년 구축, 주관 에이치씨아이플러스)는 도면 48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620)을 아파트·연립다세대·단독주택의 주거 용도로만 구성하고, 구조 8종(출입문·창호·벽체 등)·공간 12종(거실·침실·주방 등)·객체 5종(변기·세면대·싱크대·욕조·가스레인지) 라벨을 두며, 유효성 검증 모델 성능으로 YOLOv5 객체 탐지 mAP 90.33%, DeepLabV3+ 분할 mIoU 71.2%, 문자 인식 CER 4.95%를 제시한다. | ref-1012 | 아니오 | medium | 2022 | 가정 / 작업 대상 | — |
| f6 | [추정] | AI Hub 건축 도면 데이터의 라벨은 주거 건축 요소와 위생·주방 설비로 이루어져 있어 충전 위치·승강기 앞 대기 구역 같은 로봇 운영용 클래스는 들어 있지 않고 비주거 건물 도면은 포함되지 않은 것으로 보이므로, 병원·공장·물류창고 도면에 쓰려면 별도 라벨과 데이터가 필요할 것으로 추정된다. | ref-1012 | 아니오 | low | 2026-09-30 | — | — |
| f7 | [사실] | OmniDocBench(Ouyang 외, CVPR 2025)는 학술 논문·교과서·손글씨 노트·밀집 조판 신문 등 9개 문서 출처에 19개 레이아웃 범주와 15개 속성 라벨을 달아, 파이프라인 방식과 시각–언어 모델 방식의 PDF 문서 파싱을 전체·모듈·속성 수준에서 비교 평가하는 벤치마크다. | ref-1080 | 아니오 | medium | 2025-03-25 | — | — |
| f8 | [사실] | OmniDocBench 공식 저장소 README 는 2026-04 판(v1.6) 기준 PDF 1,651쪽·10개 문서 유형·영어와 중국어(간체)·혼합 언어로 구성된다고 밝히고, 종단 평가 상위 모델(TeleOCR)의 종합 점수 96.91·텍스트 편집 거리 0.0267·표 TEDS 96.82 를 싣으며, 데이터는 연구 목적으로만 쓰고 상업적 사용을 허용하지 않는다. | ref-513 | 아니오 | medium | 2026-04 | — | — |
| f9 | [사실] | IBM Research 가 공개한 Docling(Livathinos 외, arXiv 2501.17887, 2025-01)은 여러 문서 형식을 하나의 구조화 표현으로 바꾸는 MIT 라이선스 오픈소스 도구로, 레이아웃 분석에 DocLayNet 기반 모델을, 표 구조 인식에 TableFormer 를 쓰고 일반 하드웨어에서 적은 자원으로 동작하며 LangChain·LlamaIndex·spaCy 에 통합되어 있다. | ref-1082 | 아니오 | medium | 2025-01-27 | — | — |
| f10 | [사실] | Xia·Xiao·Jazdi·Weyrich(IEEE Access, 2024)는 데이터시트 원문에서 '의미 노드'를 뽑아 LLM 에이전트로 자산관리셸(AAS) 인스턴스 모델을 생성하는 시스템을 만들고, 원문 정보가 오류 없이 AAS 로 옮겨진 비율(유효 생성률)을 62~79%로 보고했다. | ref-1087 | 아니오 | medium | 2024-06 | — | — |
| f11 | [사실] | Groß·Heidrich 의 AAS-RAIL(arXiv 2609.07334, 2026-09)은 전기공학·유체동력 분야 4개 제조사의 제품 데이터시트–AAS 쌍 200건에서, 비슷한 기존 AAS 로부터 추출 지침을 검색해 문맥 예시로 쓰는 방식으로 속성 추출 정확도를 평균 51.8%에서 71.7%로 높였으나, 원문 데이터시트에서 정답 속성값을 찾을 수 있는 경우가 전체 속성의 56.2%뿐이어서 전문가 검토가 여전히 필요하다고 밝혔다. | ref-1086 | 아니오 | medium | 2026-09-07 | — | — |
| f12 | [추정] | 독립된 두 연구(f10·f11)를 종합하면 LLM 으로 기술 데이터시트를 표준 자산 모델로 옮길 때 오류 없이 옮겨지는 비율은 대략 5~8할 수준이고, 원문 자체에 정보가 없거나 이름과 값이 떨어져 있는 경우가 많아 사람의 검토 없이 등록 정보로 확정하기는 어려운 것으로 보인다. | ref-1087, ref-1086 | 아니오 | low | 2026-09-30 | — | — |
| f13 | [사실] | 오픈소스 LangExtract(google/langextract, Apache 2.0)는 LLM 으로 비정형 텍스트에서 구조화 정보를 뽑으면서 추출한 항목마다 원문 텍스트의 정확한 위치를 연결하고, 그 위치를 원문 맥락에 강조해 보여 주는 HTML 검토 화면을 만들어 사람이 대조할 수 있게 하며, 구글의 공식 지원 제품은 아니라고 밝힌다. | ref-1089 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f14 | [사실] | Dussard·Sarthou(LAAS, arXiv 2606.17073, 2026-06)는 URDF 의 구조·기구학 기술 안 식별자를 LLM 이 상식으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 파이프라인을 제안했으나, 초록에는 정량 평가 결과를 밝히지 않았다. | ref-239 | 아니오 | medium | 2026-06-10 | — | — |
| f15 | [사실] | 제조 공장 사례로, Brorsson 외(arXiv 2512.15215)의 인프라 기반 이동 로봇 시스템은 천장 카메라가 로봇에 붙인 ArUco 표식을 검출해 로봇 위치·방향을 계산하고, 저해상도 영상의 이진 의미 분할로 장애물과 빈 공간을 격자 단위로 구분하며, 카메라별 점유 지도를 전역 지도로 합치되 시야가 겹치는 곳은 가장 가까운 카메라 하나의 결과만 쓴다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 수행 자원 | — |
| f16 | [사실] | 같은 연구의 대형 상용차 제조 현장 배치에서는 약 8 m 높이에 단 카메라 15대(대당 약 60 m²)가 바닥을 덮고, 로봇 6대가 약 150 m 구간에서 머플러를 운반하며 하루 약 130회 운반(주기 7분)을 수행했다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 작업 대상 | — |
| f17 | [사실] | 같은 연구는 인프라 카메라 인식의 한계로 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류, 가림·센서 고장·제한된 시야 범위로 인한 위치 추정 중단, 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제를 든다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 제약 | — |
| f18 | [사실] | 물류창고 사례로, Robinson 외(Oxford, arXiv 2606.06762, 2026-06)는 로봇에 작업용 주행 장비를 싣지 않고 외부 CCTV 카메라망과 외부 계산만으로, 보정하지 않은 화소 단위 위상 카메라 그래프 위 영상 공간에서 다중 로봇을 계획·제어하며 카메라 시야가 겹치는 구역을 공유 자원으로 순차 배정해 교착을 막는 방식을 실제 창고(로봇 4대, 카메라 30대, 길이 27 m 통로 6개)에서 시연하고 이를 첫 현장 시연이라고 밝혔다. | ref-1075 | 아니오 | medium | 2026-06-04 | 물류창고 / 수행 자원 | — |
| f19 | [사실] | Modi 외(arXiv 2605.18197, 2026-05)는 RGB 카메라만으로 3차원 장면 그래프를 만드는 능동 탐색 방법을 제안하고, 시뮬레이션(ReplicaCAD)에서 천장 쪽 고정 외부 카메라 1대로 초기화하면 기준 방법의 장면 그래프 노드 수가 16개에서 37개로, 재현율이 0.12에서 0.27로 늘었으며, 로봇 없이 고정 카메라 3대만 쓰면 F1 이 0.421(복잡한 아파트)·0.516(가구 배치 방)으로 30단계 능동 탐색의 재현율에는 못 미치지만 환경의 주요 구조는 잡는다고 보고했다. | ref-1083 | 아니오 | medium | 2026-05-18 | — | — |
| f20 | [사실] | 실외 사례로, Strader 외(MIT 등, arXiv 2506.07454, 2025-07 개정)는 로봇마다 만든 장면 그래프와 개방형 객체 지도를 대응점으로 정합해 하나의 공유 3차원 장면 그래프로 합치고, LLM 이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 운영자의 자연어 의도를 PDDL 목표로 바꾸는 다중 로봇 계획·실행 시스템을 대규모 실외 환경의 실제 작업으로 평가했다. | ref-1084 | 아니오 | medium | 2025-07-10 | 실외 / 시작 조건 | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽는가)에 대해, 문서의 글자·표를 읽는 파싱은 공개 벤치마크에서 높은 점수를 내지만(f1·f8), 데이터시트에서 속성값을 표준 모델로 옮기는 정확도는 5~8할 수준이고(f10·f11), 도면의 심볼 개수 세기는 멀티모달 모델에서 0.40~0.55 에 그치며(f1), 전용 도면 인식 모델도 상업 시설 평면도에서 전체 검출 약 84% 수준이고(f4), 고정 카메라 장면 인식은 구조는 잡되 세부 객체 재현율이 낮아(f19) 어느 쪽도 사람 확인 없이 실행 정보로 쓰기에는 부족한 것으로 보인다. | ref-1088, ref-513, ref-1087, ref-1086, ref-1078, ref-1083 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 이기종 로봇 등록과 능력 표현에 필요한 정보가 제조사 문서·데이터시트·URDF 에 흩어져 있어 이를 자동으로 읽어야 하고(f10·f11·f14), 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며(f1·f4), 여러 로봇·고정 카메라의 인식을 모아야 로봇 한 대로는 가려지는 공간 상태를 알 수 있는데(f15·f18·f19), 각 단계의 오류가 그대로 등록 정보·지도·세계 상태의 오류로 이어지기 때문이다. | ref-1087, ref-1086, ref-239, ref-1088, ref-1078, ref-308, ref-1075, ref-1083 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 45. 문서·도면·장면 이해에서 ROP 가 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가(f7·f9·f11), 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름(f13), 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 플랫폼 수준 융합(f15·f17·f20)이다. | ref-1080, ref-1082, ref-1086, ref-1089, ref-308, ref-1084 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서 인식·SLAM·국지 회피(f15·f20의 로봇 측 인식)는 로봇 제조사에, CCTV·영상 관리 시스템과 카메라 설치·동기화(f17·f18)는 시설·보안 설비 쪽에, 도면·BIM 작성 도구와 원본 도면(f3·f5)은 설계·건축 쪽에 속하므로, ROP 는 이들이 내는 인식 결과·영상·도면을 받아 해석·융합하는 인터페이스와 검토 절차를 맡을 것으로 보인다. | ref-308, ref-1084, ref-1075, ref-067, ref-1012 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 매뉴얼 해석이 적용되는 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전(f10·f11·f14), 능력 항목을 받는 5. 로봇 능력·작업 표현(f14), 추출 결과 검토의 7. 온톨로지 검증·변경 관리(f13), 도면 해석이 적용되는 14. 도면·BIM에서 지도 만들기(f1~f5), 지도와 장소 의미의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리(f4·f20), 융합된 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f15·f19), 사람 인식의 19. 사람·보행자 모델(f15), 언어 모델 계획의 44. 로봇 기반 모델·언어 모델 계획(f20), AI 결과 사용 기준의 47. AI·학습·적응과 모델 운영(f12·f21), 영상 개인정보의 53. 개인정보·영상 데이터(f17), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f7), 적용 현장인 61. 물류창고(f18)·62. 제조 공장(f15~f17)·64. 상업 시설(f4)·66. 실외(f20)와 이어진다. | ref-1087, ref-1086, ref-239, ref-1089, ref-1088, ref-1078, ref-1084, ref-308, ref-1083, ref-1080, ref-1075 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1075 | Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv) | Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse | 2026-06-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.06762 | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. (arXiv) | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-1012 | 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-1078 | Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)) | A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans | 2022-03-25 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/ | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.17073 | 아니오 |
| ref-1080 | Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv) | OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations | 2025-03-25 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2412.07626 | 아니오 |
| ref-513 | OpenDataLab (opendatalab/OmniDocBench) | OmniDocBench — README | 2026-04 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/opendatalab/OmniDocBench | 아니오 |
| ref-1082 | Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv) | Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion | 2025-01-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2501.17887 | 아니오 |
| ref-1083 | Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv) | RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots | 2026-05-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2605.18197 | 아니오 |
| ref-1084 | Strader, J., Ray, A., Arkin, J. 외 (arXiv) | Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs | 2025-07-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2506.07454 | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-11-29 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-1086 | Groß, J., & Heidrich, J. (arXiv) | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 2026-09-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.07334 | 아니오 |
| ref-1087 | Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv) | Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0 | 2024-06-24 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.17209 | 아니오 |
| ref-1088 | Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv) | AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding | 2026-01-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2601.04819 | 아니오 |
| ref-1089 | Google (google/langextract) | LangExtract — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/google/langextract | 아니오 |
| ref-308 | Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2512.15215 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 문서 레이아웃 분석·표 구조 인식 f7·f9, 출처 근거 연결 f13, 패놉틱 심볼 스포팅 f3, 인프라 카메라 인식·공유 장면 그래프 f15·f20 / 섹션 5: 상업 시설 — f4(쇼핑몰 평면도 인식, 작업 대상: 공간), 제조 공장 — f15(수행 자원: 천장 카메라)·f16(작업 대상: 머플러 운반)·f17(제약: 동기화·가림·개인정보), 물류창고 — f18(수행 자원: CCTV 망만으로 다중 로봇 조율), 실외 — f20(시작 조건: 운영자 자연어 의도), 가정 — f5(주거 도면 데이터). 병원 사례는 찾지 못함을 명시 / 섹션 6: 문서 파싱 f7·f8·f9, LLM 데이터시트 추출 f10·f11·f12, URDF 해석 f14, 원문 위치 근거 f13, 도면 인식 f1~f4, 카메라·로봇 인식 융합 f15·f18·f19·f20 / 섹션 7: Docling f9, OmniDocBench f7·f8, LangExtract f13, CubiCasa5K f2, FloorPlanCAD f3, AI Hub 건축 도면 데이터 f5, AECV-Bench f1 / 섹션 8: f1·f4·f10·f11·f15·f18·f19·f20 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 4, 5, 7, 14, 15, 16, 18, 19, 44, 47, 53, 54, 55, 61, 62, 64, 66 / 섹션 11: 기존 oq-147·oq-196 과 open_questions_new 4건. 다음 실행 후보: 4. 이기종 로봇 등록 페이지에 f10·f11·f13 반영, 18. 실시간 세계 상태·데이터 일관성 페이지에 f15·f17 반영. |
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 5, 8, 11 | 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 f4 를 섹션 5(상업 시설 사례)에, f1·f3·f5 를 섹션 8 에, f5·f6(oq-197 해결 근거)·f4(oq-196 부분 근거)를 섹션 11 에 반영 제안. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 문서 레이아웃 분석 | Document Layout Analysis | 문서 페이지 이미지나 PDF 에서 본문·제목·표·그림·수식 같은 영역을 찾아 종류를 구분하고 읽는 순서를 정하는 문서 이해의 첫 단계다. |
| 표 구조 인식 | Table Structure Recognition | 문서 속 표의 행·열·병합 셀 구조를 복원해 표 내용을 기계가 읽을 수 있는 형식으로 바꾸는 기술로, TEDS 같은 트리 편집 거리 지표로 평가한다. |
| 출처 근거 연결 | Source Grounding | 언어 모델이 문서에서 추출한 항목마다 원문 속 정확한 위치(문자 범위·쪽·절)를 함께 기록해 사람이 원문과 대조해 확인할 수 있게 하는 방식이다. |
| 인프라 장착 센서 | Infrastructure-mounted Sensing | 천장·벽 같은 시설에 고정한 카메라·센서로 로봇 밖에서 넓은 영역의 위치·장애물·사람을 인식해 로봇 온보드 센서의 가림과 시야 한계를 보완하는 방식이다. |

## 열린 질문

새로 생긴 질문:

- OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 4. 이기종 로봇 등록 | 근거: f8 | 종류: 일반
- 일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 5. 로봇 능력·작업 표현 | 근거: f11 | 종류: 일반
- 하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 18. 실시간 세계 상태·데이터 일관성 | 근거: f17 | 종류: 일반
- 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? | 관련 영역: 45. 문서·도면·장면 이해, 53. 개인정보·영상 데이터 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-197

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f2 CubiCasa5K 의 수집 지역(핀란드)·주거 전용 여부와 성능 수치: 검색 요약에만 나오고 초록·README 에서 확인하지 못함(본문 PDF 추출 실패)
    - f3 FloorPlanCAD 규모·범주 수: 초록은 1만 장 이상·30개 범주·주거와 상업, 검색 요약은 1만5천 장·35개 범주·병원·학교 포함으로 판에 따라 다름. PQ 0.561 은 검색 요약에만 있어 넣지 않음
    - f6 AI Hub 구조 8종·공간 12종 라벨의 전체 목록은 페이지에 일부만 보여 미확인
    - f18 임무 시간·조율 통계 수치는 초록에 없어 미확인
    - f20 로봇 대수·실험 수치는 초록에 없어 미확인
    - f10 데이터셋 규모는 초록에 없어 미확인
    - ETRI 전자통신동향분석 '스마트제조 분야 LLM 기반 안전성 평가' 글(공장 매뉴얼 기반 질의응답 평가)은 ECONNRESET 으로 두 번 열지 못해 넣지 않음
    - Belfadel 외(arXiv 2609.31663) 산업 보고서 온톨로지 추출은 정량 수치가 초록에 없어 넣지 않음
    - 병원 현장의 고정 카메라·로봇 인식 융합 사례는 찾지 못함(찾은 arXiv 2509.26106 은 시뮬레이션 병원·저가 하드웨어라 제외)
    - oq-196 은 부분 근거만(f4 상업 시설 평면도 83.81~92.54%, f3 상업 건물 포함 데이터셋) 확보해 해결 제안하지 않음
    - oq-147 은 범용 도구 LangExtract(f13)만 찾았고 로봇 매뉴얼·URDF 능력 항목에 원문 위치를 붙인 공개 구현은 찾지 못함
- 범위 경계 위반 의심:
    - f15·f20: 로봇 측 인식·SLAM·재위치 추정은 로봇 자체 지능(연계 대상)이므로 플랫폼 수준 융합 근거로만 쓰고 f24 에서 구분함
    - f18: 로봇에 주행 장비 없이 외부 카메라·외부 계산으로 주행을 제어하는 방식은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례('경계는 제품 전략에 따라 이동할 수 있다')이며 ROP 기본 범위로 서술하지 않도록 주의
    - f19·f15: 장면 인식 결과가 표현하는 현재 상태는 18. 실시간 세계 상태·데이터 일관성의 내용이며 34. 시뮬레이션·예측용 디지털 트윈과 섞지 않음(f19 의 시뮬레이션은 평가 환경일 뿐 예측 실험이 아님)
    - f24: CCTV·영상 관리 시스템, 설계 도구·원본 도면을 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 병원 사례와 한국어 문서 이해 자료를 더 넣지 못했다. 재사용 1건(ref-308: 참고문헌 목록 전체가 입력에 없어 값은 이전 브리프 2026-09-30-05 의 출처 표를 따랐고, 이번에 HTML 본문을 다시 열었다). 원문 열람: 16건 모두 열었다(webfetch 14건, github_raw 2건). 논문은 대부분 초록 페이지이고 Su 외(PMC 본문)·Modi 외·AAS-RAIL·Brorsson 외(arXiv HTML 본문)만 본문을 봤다. 교차 확인 0건: 수치마다 데이터·지표가 달라 같은 값을 두 출처로 확인할 수 없었고, f12·f21 은 종합 추정(low)으로 냈다. 벤더 문서는 쓰지 않았다. 분류 원문 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽어 내는가)에는 f21 로 답했고 결론은 '글자·표 파싱은 벤치마크에서 높지만 속성 추출 5~8할, 도면 심볼 세기 0.40~0.55, 고정 카메라 장면 인식은 구조 수준이라 사람 확인 없이 실행 정보로 쓰기 어렵다'는 추정이다. 현장 유형 사례는 상업 시설(f4)·제조 공장(f15~f17)·물류창고(f18)·실외(f20)·가정(f5, 주거 도면 데이터)이며 병원·기타 사례는 찾지 못했다. 국내 자료는 AI Hub 건축 도면 데이터(ref-1012) 1건이다. oq-197 해결 근거: f5·f6(비주거 도면 미포함, 공개된 객체 5종에 로봇 운영 클래스 없음; 구조·공간 라벨 전체 목록은 미확인이라 검증 판단 필요). oq-196·oq-147 은 부분 근거만 있어 해결 제안하지 않았다. 교차 규칙에 따라 매뉴얼 해석 finding(f10·f11·f13·f14)은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에, 도면 해석 finding(f1~f6)은 14. 도면·BIM에서 지도 만들기에 연결하도록 제안했다. 용어집에 이미 있는 평면도 인식·패놉틱 심볼 스포팅·파놉틱 품질·3차원 장면 그래프·협동 인지·래스터–벡터 변환·자산관리셸·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
