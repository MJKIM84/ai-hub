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
- verification_stage: second
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
        "ref-470"
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
        "ref-470"
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
        "ref-980",
        "ref-992"
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
        "ref-992"
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
        "ref-031"
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
        "ref-031"
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
        "ref-470",
        "ref-980",
        "ref-992",
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
        "ref-470",
        "ref-1088",
        "ref-980",
        "ref-992",
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
        "ref-031",
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
        "ref-470",
        "ref-1088",
        "ref-980"
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
        "ref-980",
        "ref-1089",
        "ref-1087",
        "ref-031",
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
      "id": "ref-470",
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
      "id": "ref-031",
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
      "id": "ref-980",
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
      "id": "ref-992",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 ISO 13482·ISO 13855 원문, 상업 시설·가정 사례, 국내 서비스 로봇 기준을 더 넣지 못했다. 주의: 입력의 이전 브리프 2026-09-30-08 도 ref-1075~ref-1089 를 썼으나 실행 컨텍스트가 이 구간을 이 실행 전용으로 예약했다고 밝혀 그대로 썼다(퍼블리셔의 id 충돌 확인 필요). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건; VDA 5050·ISO 3691-4 가 기존 참고문헌에 있으면 퍼블리셔가 같은 URL 로 합쳐야 한다). 원문 열람: 14건 열었고(webfetch 12건, github_raw 2건) ISO 3691-4(ref-470)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Marvel·Norcross(ref-1075)·Rondoni 외(ref-1085)는 PMC 본문, 나머지는 초록 페이지다. 교차 확인 1건(f9: 15 km/h·500 kg 을 인증기관 페이지와 기사로 확인). 벤더 문서는 아마존(ref-1084) 1건이며 f14 는 vendor_claim·추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에는 f20 으로 답했고 결론은 '분리 거리는 계산값이고, 감속·정지 상한은 적용 유형별 표준·인증이 구역·속도로 정하며, 편안함 기준은 별도'라는 추정이다. 현장 유형 사례는 물류창고(f14·f18)·병원(f17, 시뮬레이션)·실외(f9·f10)이며 제조 공장은 규정 수준, 상업 시설·가정·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-980)·지디넷코리아 2건(ref-992·ref-1082)이다. 용어집에 이미 있는 운용 구역·구역 집합·위험성평가·협동 적용·실외이동로봇 운행안전인증·공공 영역 이동로봇·필터 마스크·해제 구역은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### runs/2026-09-30-10/verification.json

```json
{
  "run_id": "2026-09-30-10",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 저자 원고 본문을 열었다. 보호 분리 거리가 사람 속도(vH), 반응 시간(TR), 정지 시간(TS), 제동 거리(B), 침입 거리(C), 위치 불확실도(ZR·ZS)로 나뉜다는 서술이 본문과 일치한다. 단일 출처이고 발행 2016(2년 초과)이라 월간 재검증 대상이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 표현을 고친다: 본문은 ISO 13855 가 최대 2,000 mm/s 를 쓰고 분리 거리가 500 mm 보다 클 때만 1,600 mm/s 를 선택할 수 있다고 적는다. 침입 거리 850·1,200 mm 는 센서 구성·접근 방향에 따라 다른 값이다. 반응 시간 0.113 s(0.999 신뢰구간 +0.019 s)는 레일 장착 6자유도 매니퓰레이터의 값이다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 방향 무시로 인한 불필요한 정지, 수 mm 위치 잡음이 수백 mm/s 속도 오차로 커지는 문제, 1,000 Hz 1.6 m/s 대 100·30 Hz 약 1.5 m/s 의 평균 속도 차이가 본문에 있다. '주로 좌우한다'는 본문의 '크게 영향을 준다'보다 조금 강하다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2602.17822(2026-02-19 제출) 초록에 ISO/TS 15066 의 규범적 통합, 로봇·협동 적용의 새 분류, 네트워크 로봇의 사이버보안·무단 접근 방지 요구가 있다. 표준 원문이 아닌 프리프린트의 분석이므로 'Hartmann 외는 … 분석했다'는 귀속을 유지해야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 법령 내용을 신뢰도 low 인 기사(ref-1082) 하나로 전하고 조문 원문을 열지 못했다. 기사는 실재하며 claim 대로 전한다. 다만 검증 중 확인한 제3자 조문 사본에 따르면 제223조는 1.8 m 이상 울타리가 기본이고, 안전매트·광전자식 방호장치는 울타리를 설치할 수 없는 일부 구간에만 요구한다. 면제는 고용노동부장관이 그 로봇의 안전기준이 한국산업표준이나 국제 기준에 맞다고 인정한 경우이며 '협동 운전 로봇'에 한정하지 않는다. 기사는 SSM·HGC·PFL 을 제223조가 아니라 '국제기준'의 방식으로 소개한다. 기사 발행일은 2024-03-09 로 표시된다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ISO 403). 검색 결과에서 ISO 3691-4:2023 페이지(iso.org/standard/83545)의 제목·URL 이 일치했다. 운용·제한·격리 구역 구분은 검색 요약 범위 안에 있다. [추정]·low·source_unopened 를 유지한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 0.3 m/s 제한, 200×600 mm 수직 원통, 70×400 mm 수평 원통 시험편, 접촉 전 정지는 검색 요약(제3자 블로그)과 일치한다. 표준 원문으로 확인하지 못했으므로 [추정]을 유지하고, 본문에 '원문 미확인 수치'임을 밝혀야 한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(2023-10-26, Mike Oitzman). 통합자의 위험성 평가 책임 인용, 모바일 매니퓰레이터를 처음 정의한 점, 사용자 정보·교육, Part 1~3 구성이 기사에 있다. '잔여 위험'은 열람 결과에서 확인하지 못해 삭제를 지시한다. 표준 본문은 유료라 미열람이므로 'The Robot Report 가 전했다'는 귀속을 유지한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인·교차 확인: KIRIA 인증 페이지에 제40조의2 의무인증, 로봇 제품과 관제장치의 조합, 15 km/h 이하·500 kg 이하, 8개 심사 항목, 30일 처리, 2년 주기 정기점검·불시점검이 있다. 15 km/h·500 kg 은 지디넷코리아(2023-07-28)와 일치한다. 두 출처 모두 원문을 열었다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 230 kg 초과 5 km/h, 100 kg 초과 10 km/h, 그 이하 15 km/h, 보행 신호 중 도착 시 정지 대기, 16가지 심사 항목이 기사와 일치한다. 기사는 2023-07 당시 '개정안'을 전한 것이다. 현행 인증기관 페이지에는 질량별 속도 구간이 없고 심사 항목이 8개로 표시돼 출처 충돌이 있다(열린 질문 2)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA5050_EN.md(3.0.0, github_raw)를 열었다. 6.4.1 표에 윤곽 기반 BLOCKED·LINE_GUIDED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT·ACTION과 중심점 기반 PRIORITY·PENALTY·DIRECTED·BIDIRECTED가 있다. 인용 문장 'Mobile robots shall not drive faster than the defined maximum speed within this zone.'이 원문과 같다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 원문의 면책 문구가 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용하지 않는다고 적는다. claim 은 재서술이며 원문과 일치한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 공식 README(github_raw)에 cmd_vel 을 거르는 독립 노드, 정지·감속·접근 모델, 다중 영역 동시 발동 시 가장 강한 조치, 레이저·포인트클라우드·IR/초음파·비용 지도 입력, 'does not provide hard real-time safety certifications' 문장이 있다. '안전 등급 하드웨어를 대신하지 않는다'는 README 의 직접 표현이 아니라 해석이다. README 는 안전 등급 센서·제어기가 없는 사용자를 위한 기능이라고 적는다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 아마존 자사 글에 조끼가 접근 경로를 그려 로봇이 감속·경로 변경하고 가까워지면 정지한다는 서술과 직원 인용이 있다. 발행일은 페이지에 없다. 벤더 문서이며 독립 확인이 없으므로 [추정]·'벤더 주장' 병기를 유지한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2306.16740(2023-06-29 제출, v4 2023-09-19) 저자 52명, 8원칙, 지표·시나리오·벤치마크·데이터셋·시뮬레이터 지침이 있다. 검색 결과로 ACM THRI 14(2) Article 34(2025-02, DOI 10.1145/3700599) 게재를 확인했다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록에 로봇–자원자 일대일 시행, 대부분 변수의 'moderate but significant' 상관, 최소 거리·최소 예상 충돌 시간·복합 추정기, 복합 지표 오즈비 3.67 이 있다. 맥락은 공공 보도의 보행자 편안함이다. 실험 장소·참가자 수는 미확인이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(PMC 본문, Scientific Reports 2024-08-07): HOSBOT·TIAGo, 실제 병동 배치를 재현한 모의 병원 환경, 0.2·0.6·1.0 m/s, 사람 보행 하한 0.6~1.3 m/s 근거, 7개 지표, 두 로봇 모두 높은 성공률이 본문에 있다. 다만 '속도가 높을수록 정확도가 떨어졌다'는 단조 표현은 부정확하다. 본문은 최고 속도에서 방향 오차가 커지고 정확도가 중간 속도에서 가장 높았다고 적는다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2503.21141(2025-03-27) 초록에 학습 기반 CBF 의 OpenRMF 통합, 다중 로봇·다중 행위자, 보행자 포함 정적·동적 장애물 회피가 있다. 평가 변수는 로봇 수·로봇 플랫폼·속도·장애물 수다. 정량 결과와 평가 환경(현장 여부)은 미확인이다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2508.19731(2025-08-27, IROS 2025 채택) 초록에 움직임 지도(MoD) 기반 확률적 비용 함수가 있다. 개선 폭은 '최대(up to)' 26%(동역학 무시 방법 대비)·19%(기준선 대비)다. claim 에 '최대'가 빠져 추가를 지시한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다. 근거 finding 가운데 f6·f7 은 원문 미열람 표준, f10 은 2023 개정안 기사이므로 '적용 유형별 표준·인증이 구역·속도 상한을 정한다'는 서술에 그 한계를 함께 적어야 한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다. 근거 f5 가 추정으로 강등됐으므로 '울타리 면제' 부분은 기사 전달 수준으로만 쓴다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다. 구역·속도 제한 전달(f11)과 VDA 5050·Nav2 가 안전 기능이 아니라는 근거(f12·f13)는 원문으로 확인됐다. 사람 위치 신호 기반 조정은 벤더 주장(f14)과 연구(f18·f19)에 기대므로 '보조 계층'이라는 한정을 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다('연계 대상: ' 표기). 실외 인증 적합성을 '운영 사업자'의 몫으로 본 것은 KIRIA 페이지에 신청 주체가 없으므로 구축자 추론이다. 인증 대상에 관제장치가 포함돼 ROP 범위와 겹칠 수 있다는 점을 9절에 밝힌다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 제안이다. 세부영역 번호·이름 15개가 부록 A 원문 명칭과 일치한다."
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
      "참고문헌 id 충돌: 이전 브리프 2026-09-30-08 이 ref-1075~ref-1089 를 다른 출처에 썼다(예: ref-1075 = Robinson 외 CCTV 창고 논문, ref-1088 = AECV-Bench). 이번 브리프는 같은 id 를 Marvel·Norcross, The Robot Report 등에 썼다. 입력의 참고문헌 목록은 1,074건이라 아직 등록되지 않았지만, 두 실행이 모두 게시되면 충돌한다.",
      "URL 중복 가능성: VDA 5050 명세(ref-031), ISO 3691-4:2023(ref-470), KIRIA 실외이동로봇 운행안전인증(ref-980)은 용어집에 관련 항목(vda-5050, operating-zone, outdoor-mobile-robot-operational-safety-certification)이 있어 기존 참고문헌에 이미 있을 가능성이 높다. 입력 요약에는 목록이 없어 확인하지 못했다.",
      "내용 겹침: 7절 표준 서술(f4·f6~f10)은 50. 안전 표준·인증·사고 조사(seed)의 범위와 겹친다. 위험성 평가 책임(f8)은 48. 안전·위험 관리와 겹친다. 모순은 없다."
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
    "f5: [사실] → [추정]으로 강등한다. '지디넷코리아 기사(2024-03-09)에 따르면'으로 귀속하고, '울타리와 안전매트 설치를 기본'을 '높이 1.8미터 이상 울타리 설치를 기본으로 하되 일정 안전기준을 충족하면 면제될 수 있다'로 줄인다 — 제3자 조문 사본상 안전매트는 울타리를 설치할 수 없는 구간에만 요구되고 면제 요건이 협동로봇에 한정되지 않으며, 법령 원문을 확인하지 못했다.",
    "f5: SSM·HGC·PFL 협동 방식은 제223조의 내용이 아니라 기사가 소개한 국제 기준(ISO/TS 15066 계열)의 분류로 분리해 쓴다 — 기사가 '국제기준에서 규정한 방식'으로 전한다.",
    "ref-1082: 발행일을 2024-03 에서 2024-03-09 로 고쳐 각주에 적는다 — 기사 페이지 표시 날짜다.",
    "f2: 사람 속도를 'ISO 13855 는 최대 2,000 mm/s 를 쓰고 분리 거리가 500 mm 보다 크면 1,600 mm/s 를 선택할 수 있다'로 고친다. 침입 거리 850·1,200 mm 는 센서 구성·접근 방향에 따라 달라지는 값으로, 반응 시간 0.113 s 는 '레일 장착 6자유도 매니퓰레이터'의 측정값으로 적는다 — 원문 본문과 맞춘다.",
    "f3: '보호 거리는 주로 로봇 제동 거리와 반응 시간이 좌우한다'를 '제동 거리와 반응 시간이 보호 거리에 크게 영향을 준다'로 낮춘다 — 원문 표현이 그 정도다.",
    "f6·f7: 본문에서 [추정]을 유지하고 '표준 원문 미확인, 검색 요약 기준'을 밝힌다. ref-470 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-470 에 source_unopened: true 를 넣는다 — ISO 페이지가 403 이었다.",
    "f8: '잔여 위험'을 빼고, 'The Robot Report 가 전했다'는 귀속과 표준 본문 미열람(유료) 사실을 유지한다 — 열람한 기사에서 잔여 위험 서술을 확인하지 못했다.",
    "f10: 질량별 속도 구간·횡단보도 대기·16가지 항목은 '2023-07-28 기사가 전한 당시 개정안 기준'으로 적는다. 인증기관 페이지(ref-980)의 8개 항목과 함께 제시하고, 한쪽을 고르지 않은 채 열린 질문 2와 연결한다 — 출처 충돌이다.",
    "f13: '하드 실시간 안전 인증을 제공하지 않는다고 밝힌다'로 한정한다. '안전 등급 하드웨어를 대신하지 않는다'는 README 의 직접 표현이 아니므로 쓰지 않거나 [추정]의 해석으로 분리한다.",
    "f14: 5절 물류창고 사례와 6절에서 [추정]에 '벤더 주장'을 병기하고, 발행일은 '미확인'으로 적는다.",
    "f17: '속도가 높을수록 정확도가 떨어졌다'를 '최고 속도에서 방향 오차가 커졌고 정확도는 중간 속도에서 가장 높았다'로 고친다. 5절 병원 사례에는 실제 병원이 아닌 모의 병원 환경 평가임을 밝힌다.",
    "f18: 5절 물류창고 사례로 쓸 때 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가임을 밝히고, 정량 결과는 '미확인'으로 둔다.",
    "f19: 26%·19% 앞에 '최대'를 넣는다 — 초록이 'up to'로 적는다.",
    "f15: ref-1083 각주에 학술지판(ACM Transactions on Human-Robot Interaction 14(2), 2025-02)을 병기할 수 있다. 발행일은 arXiv 제출일 2023-06-29 를 유지한다.",
    "7절: 표준·인증은 사람 근접 안전과 관련된 구역·속도·감지·정지 항목으로 한정해 요약하고, 표준 상세는 '50. 안전 표준·인증·사고 조사'로 연결한다 — 50번 영역과 범위가 겹친다.",
    "9절: f13(Nav2 Collision Monitor)과 f1~f3·f5~f7 의 안전 등급 기능은 '연계 대상'(로봇 자체 지능·제어, 설비 안전 제어)으로 쓴다. f23 의 실외 인증 대상에 관제장치가 포함된다는 점을 ROP 범위와 겹칠 수 있는 경계로 밝힌다(f9)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 1건(f9: 15 km/h·500 kg, 인증기관 페이지와 기사). 강등: f5 사실 → 추정(법령 내용을 기사 1건으로만 전하고 조문 원문을 확인하지 못함. 제3자 조문 사본과 표현이 다름). 원문 미열람 출처: ref-470(ISO 3691-4:2023, 403. f6·f7 은 검색 요약 기준 추정). 주의: 핵심 수치(보호 분리 거리 변수 f1~f3, VDA 5050 구역 f11, Nav2 f13, 병원·보행자 연구 f16·f17, 배정 f19)는 대부분 단일 출처이고, 3절·9절은 종합 추정이다. 질량별 실외 속도 구간과 심사 항목 16가지(f10)는 2023-07 개정안을 전한 기사 기준이며, 현행 인증기관 페이지는 8개 항목으로 표시해 출처가 충돌한다. 병원 사례(f17)는 모의 병원 환경, 물류창고 사례는 벤더 주장(f14)과 연구 평가(f18)다. 상업 시설·가정·기타 현장 사례는 없다. 참고문헌 id 가 이전 브리프 2026-09-30-08(ref-1075~ref-1089)과 충돌하므로 퍼블리셔가 id 충돌과 같은 URL 병합(VDA 5050·ISO 3691-4·KIRIA)을 확인해야 한다. 검증 검색 3회, 출처 15건 모두 열람 또는 검색 확인. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-10/pages.json

```json
{
  "run_id": "2026-09-30-10",
  "outline": [
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 750,
      "summary": "안전 거리는 로봇 정지 성능·센서 갱신에 따라 로봇·현장마다 달라지고, 적용 유형별로 표준·인증이 다르며, 보수적 감속·정지는 처리량과 수용성에 영향을 준다. [추정][^ref-1075]",
      "planned_findings": [
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "속도·분리 감시(SSM)와 보호 분리 거리, 동력·힘 제한(PFL), 운용 구역, VDA 5050 의 속도 제한·진입 금지·승인 구역, 움직임 지도를 정리한다. [사실][^ref-1075]",
      "planned_findings": [
        "f1",
        "f5",
        "f6",
        "f11",
        "f19"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1900,
      "summary": "물류창고(조끼 신호로 감속·정지, 벤더 주장), 병원(모의 병원 환경의 속도별 주행 평가), 실외(운행안전인증의 속도·질량 상한과 횡단보도 대기) 세 사례를 여섯 항목으로 정리한다. [사실][^ref-980]",
      "planned_findings": [
        "f14",
        "f18",
        "f17",
        "f9",
        "f10"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1900,
      "summary": "보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눠 동작과 한계를 정리한다. [의견][^ref-1075]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f11",
        "f12",
        "f13",
        "f14",
        "f16",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1500,
      "summary": "사람 근접 안전과 관련된 표준·인증은 협동로봇·무인 산업용 트럭·산업용 이동 로봇·실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f11",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "SSM 구현 연구, ISO 10218 개정 분석, 사회적 주행 평가 원칙, 보행자 편안함 예측, 병원·창고 주행 연구, 사람 인지형 배정 연구 7건을 소개한다. [사실][^ref-1075]",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1100,
      "summary": "ROP는 구역·속도 제한 전달과 사람 위치 기반 감속·우회·배정 조정, 기록을 맡고, 안전 등급 감지·정지와 SSM·PFL, 로컬 회피, 위험성 평가는 연계 대상으로 둘 것으로 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f22",
        "f23",
        "f12",
        "f13",
        "f9"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1300,
      "summary": "위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 물류창고·병원·실외 현장 영역에 이어진다. [추정][^ref-1088]",
      "planned_findings": [
        "f24"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "플릿 수준 속도 제한의 위험 감소 조치 인정, 실외 인증 심사 항목 수 충돌, 국내 실내 서비스 로봇 기준, 이종 플릿 사람 위치 전달 인터페이스 네 질문을 올린다.",
      "planned_findings": [
        "f10",
        "f12",
        "f14",
        "f9"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계, 연결 16건, 열린 질문 4건), 각주 15건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"6. 대표 접근법과 기술\" 절(1,762자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,599자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"8. 대표 연구와 자료\" 절(1,128자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,041자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"4. 핵심 개념과 용어\" 절(888자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"11. 열린 질문\" 절(579자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area49-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"3. 왜 중요한가\" 절(545자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 49. 사람 근접 안전 | seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계), 각주 15건, 열린 질문 4건 | run 2026-09-30-10",
  "index_updates": {
    "home_recent": "2026-09-30 — 49. 사람 근접 안전: 3~11절 첫 작성(보호 분리 거리 계산, 구역별 속도 제한·진입 금지, 물류창고·병원·실외 사례, ROP 책임 경계)",
    "category_recent": "2026-09-30 — 49. 사람 근접 안전: seed → draft, 보호 분리 거리·구역별 속도 제한·적용 유형별 표준·인증과 물류창고·병원·실외 사례 작성",
    "area_recent": "2026-09-30 — 49. 사람 근접 안전: 3~11절 첫 작성(각주 15건, 열린 질문 4건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "speed-and-separation-monitoring",
      "term_ko": "속도·분리 감시",
      "term_en": "Speed and Separation Monitoring (SSM)",
      "definition": "로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다.",
      "related_areas": [
        49,
        31
      ],
      "sources": [
        "ref-1075",
        "ref-1082"
      ]
    },
    {
      "action": "new",
      "slug": "protective-separation-distance",
      "term_ko": "보호 분리 거리",
      "term_en": "Protective Separation Distance",
      "definition": "사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다.",
      "related_areas": [
        49
      ],
      "sources": [
        "ref-1075"
      ]
    },
    {
      "action": "new",
      "slug": "power-and-force-limiting",
      "term_ko": "동력·힘 제한",
      "term_en": "Power and Force Limiting (PFL)",
      "definition": "로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다.",
      "related_areas": [
        49,
        31
      ],
      "sources": [
        "ref-1082"
      ]
    },
    {
      "action": "new",
      "slug": "maps-of-dynamics",
      "term_ko": "움직임 지도",
      "term_en": "Maps of Dynamics (MoD)",
      "definition": "과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다.",
      "related_areas": [
        49,
        19,
        25
      ],
      "sources": [
        "ref-1087"
      ]
    },
    {
      "action": "new",
      "slug": "control-barrier-function",
      "term_ko": "제어 장벽 함수",
      "term_en": "Control Barrier Function (CBF)",
      "definition": "로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다.",
      "related_areas": [
        49,
        27
      ],
      "sources": [
        "ref-1086"
      ]
    }
  ],
  "reference_updates": [
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO (ISO/TC 110)",
      "title": "ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 무인 산업용 트럭(AGV·AMR)과 그 시스템의 안전 요구·검증 표준. ISO 페이지가 403 이라 구역·인력 감지·속도 관련 내용은 검색 결과 요약으로만 확인했다(제목 일부는 검색 결과 기준).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050/VDA5050)",
      "title": "VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 3.0.0 명세 원문. 6.4.1절의 구역 유형(BLOCKED·RELEASE·SPEED_LIMIT 등)과 안전 표준이 아니라는 면책 문구를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "지능형 로봇법 제40조의2 에 따른 실외이동로봇 운행안전인증의 대상, 최고 속도·질량 기준, 8개 심사 항목, 처리기간, 사후관리를 안내하는 인증기관 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준)",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준(당시 개정안: 질량별 속도 상한, 횡단보도 통행, 16가지 심사 항목)을 전한 기사. 15 km/h 상한은 인증기관 페이지와 일치한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    },
    {
      "id": "ref-1082",
      "org": "지디넷코리아",
      "title": "\"협동로봇 충돌 안전 계산하고 써야죠\"",
      "published": "2024-03-09",
      "url": "https://zdnet.co.kr/view/?no=20240305160245",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업안전보건기준에 관한 규칙 제223조의 울타리 기본 요구와 면제, 국제 기준의 SSM·HGC·PFL 협동 방식, 충돌 안전 계산을 한국로봇산업협회·세이프틱스 인터뷰로 전한 기사(법령 원문은 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "summary": "사회적 로봇 주행의 8가지 원칙과 지표·시나리오·벤치마크·시뮬레이터 평가 지침을 제시한 공동 논문(초록 확인, 학술지판 ACM THRI 14(2), 2025-02).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "summary": "풀필먼트 센터에서 직원과 로봇이 함께 일하는 방식을 소개하며 로보틱스 테크 조끼로 로봇이 감속·우회·정지한다고 설명하는 아마존 자사 글(벤더 주장, 발행일 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "summary": "병원용 HOSBOT 과 TIAGo 의 주행을 모의 병원 환경에서 세 속도·7개 지표로 벤치마크한 논문(PMC 본문).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "summary": "ANSI/A3 R15.08-2(산업용 이동 로봇 시스템·적용 안전 요구) 발행과 통합자 위험성 평가 책임, 시리즈 구성을 전한 전문지 기사(표준 본문은 유료라 미열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가?",
      "areas": [
        49,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가?",
      "areas": [
        49,
        50
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가?",
      "areas": [
        49,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가?",
      "areas": [
        49,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    }
  ],
  "standards_updates": [
    {
      "name": "Nav2 Collision Monitor (nav2_collision_monitor)",
      "kind": "오픈소스",
      "org": "Open Navigation (ros-navigation/navigation2)",
      "url": "https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md",
      "related_areas": [
        49,
        27
      ],
      "summary": "컨트롤러 속도 명령을 거르는 독립 노드로, 영역별 정지·감속·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두며 여러 영역이 걸리면 가장 강한 조치를 쓴다. 하드 실시간 안전 인증을 제공하지 않는다고 밝힌다.",
      "ref_id": "ref-1078"
    }
  ],
  "additional_research_requests": [
    "7절·3절: 산업안전보건기준에 관한 규칙 제223조 조문 원문(국가법령정보센터)을 열어 울타리 기본 요구·안전매트 요구 범위·면제 요건을 확인해야 한다. 이번 본문은 기사(ref-1082) 전달 수준의 [추정]으로만 썼다. 기존 참고문헌 ref-562 가 같은 조문을 가리키는지도 함께 확인이 필요하다.",
    "4절·7절: ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s 제한, 시험편 치수를 표준 원문 또는 공식 해설로 확인해야 한다(ref-470 원문 미열람, 기존 참고문헌 ref-470 과 같은 표준).",
    "5절: 제조 공장·상업 시설·가정·기타 현장에서 사람 근접 감속·정지·양보를 적용한 실제 도입 사례(속도·거리 값 포함)가 없다. 물류창고 사례도 벤더 주장뿐이라 독립 출처와 완료·인계·예외·성과 칸의 근거가 필요하다.",
    "7절·11절: 실외이동로봇 운행안전인증의 현행 심사 항목 목록과 질량별 속도 구간이 현행 기준에 들어갔는지(2023-07 개정안 이후) 확인해야 한다.",
    "7절: ISO 13482(개인 돌봄 로봇)와 ISO 13855 원문의 사람 근접 관련 요구가 이번 브리프에 없어 넣지 못했다.",
    "운영 참고: 참고문헌 id ref-1075~ref-1089 가 이전 브리프 2026-09-30-08 과 충돌하고 VDA 5050·ISO 3691-4·KIRIA 인증 페이지가 기존 참고문헌과 같은 URL 일 가능성이 있어 퍼블리셔의 id 충돌·병합 확인이 필요하다(1차 검증 지적)."
  ],
  "fixes_applied": [
    "f5 [사실]→[추정] 강등·귀속·울타리 문구 축소 — 3절과 7절 표 '산업안전보건기준에 관한 규칙 제223조' 행을 '지디넷코리아 기사(2024-03-09)에 따르면 … 높이 1.8미터 이상 울타리 설치를 기본으로 하되 일정 안전기준을 충족하면 면제될 수 있다(법령 원문 미확인). [추정]'으로 쓰고 안전매트·협동로봇 한정 면제·2016년 표현을 넣지 않았다.",
    "f5 협동 방식 분리 — 7절 표에서 SSM·HGC·PFL 을 제223조의 내용이 아니라 기사가 소개한 국제 기준(ISO/TS 15066 계열)의 협동 방식으로 별도 문장에 썼고, 4절 동력·힘 제한 항목도 같은 귀속으로 [추정] 표기했다.",
    "ref-1082 발행일 — 13절 각주 정의와 reference_updates 의 published 를 2024-03-09 로 고쳤다.",
    "f2 표현 수정 — 6절에 'ISO 13855 가 사람 속도로 최대 2,000 mm/s 를 쓰고 분리 거리가 500 mm 보다 크면 1,600 mm/s 를 선택할 수 있다', 침입 거리는 센서 구성·접근 방향에 따라 850 mm·1,200 mm 처럼 달라지는 값, 반응 시간 약 0.113초는 '레일 장착 6자유도 매니퓰레이터'의 측정값으로 썼다.",
    "f3 표현 완화 — 6절에서 '제동 거리와 반응 시간이 보호 거리에 크게 영향을 준다'로 썼다.",
    "f6·f7 원문 미확인 표시 — 4절 운용 구역과 7절 ISO 3691-4 행을 [추정]으로 두고 '표준 원문 미확인, 검색 요약 기준'을 밝혔으며, ref-470 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-470 에 source_unopened: true 를 넣었다.",
    "f8 수정 — 7절 ANSI/A3 R15.08-2 행에서 '잔여 위험'을 빼고 'The Robot Report(2023-10-26)가 전했다'는 귀속과 '표준 본문은 유료라 열람하지 못했다'를 유지했다.",
    "f10 개정안 표기와 출처 충돌 — 5절 실외 사례 제약 칸에서 질량별 속도 구간·횡단보도 대기를 '2023-07-28 기사가 전한 당시 개정안 기준'으로 쓰고, 심사 항목 수를 인증기관 페이지(8개 항목)와 기사(16가지)로 함께 제시해 한쪽을 고르지 않은 채 11절 두 번째 열린 질문과 연결했다.",
    "f13 한정 — 6절·7절에서 'README 는 이 기능이 하드 실시간 안전 인증을 제공하지 않는다고 밝힌다'로만 썼고, '안전 등급 하드웨어를 대신하지 않는다'는 표현은 쓰지 않았다(9절의 보조 계층 판단은 f22 의 [추정]으로 분리).",
    "f14 벤더 주장 병기 — 5절 물류창고 사례 표·서술과 6절에서 모두 '[추정] 벤더 주장'으로 쓰고 발행일을 '미확인'으로 적었다(각주 발행일도 미확인).",
    "f17 수정 — 5절 병원 사례에서 '최고 속도에서 방향 오차가 커졌고 정확도는 중간 속도에서 가장 높았다'로 고치고, 실제 병원이 아닌 모의 병원 환경의 시뮬레이션 평가임을 사례 제목과 서술에 밝혔다.",
    "f18 표시 — 5절 물류창고 서술에서 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가임을 밝히고 정량 결과를 '미확인'으로 두었으며, 사례 표 칸에는 넣지 않았다(6절·8절도 정량 결과 미확인 표기).",
    "f19 '최대' 추가 — 6절과 8절에서 '최대 26%', '최대 19%'로 썼다.",
    "f15 학술지판 병기 — ref-1083 각주에 학술지판(ACM Transactions on Human-Robot Interaction 14(2), 2025-02)을 병기하고 발행일은 arXiv 제출일 2023-06-29 를 유지했다.",
    "7절 범위 한정 — 표를 사람 근접 안전과 관련된 구역·속도·감지·정지 항목으로 한정해 요약하고, 절 첫머리에서 표준 상세를 '50. 안전 표준·인증·사고 조사' 페이지로 연결했다.",
    "9절 경계 — 표의 '외부와 연계하는 것' 칸에 Nav2 Collision Monitor(f13)와 안전 등급 인력 감지·보호 정지·SSM·PFL·울타리(f1~f3·f5~f7)를 '연계 대상:'으로 썼고, 표 아래에 실외 인증 대상이 로봇과 관제장치의 조합이라 ROP 범위와 겹칠 수 있는 경계임(f9)과 운영 사업자 몫이라는 판단이 추론임을 밝혔다.",
    "분량 초과 자동 분리: 49. 사람 근접 안전 본문 10,522자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,209자"
  ]
}
```

### runs/2026-09-30-10/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/safety/human-proximity-safety.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area49-s6.md (1,762자)
    - docs/categories/safety/human-proximity-safety.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area49-s7.md (1,599자)
    - docs/categories/safety/human-proximity-safety.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area49-s8.md (1,128자)
    - docs/categories/safety/human-proximity-safety.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area49-s10.md (1,041자)
    - docs/categories/safety/human-proximity-safety.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area49-s4.md (888자)
    - docs/categories/safety/human-proximity-safety.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area49-s11.md (579자)
    - docs/categories/safety/human-proximity-safety.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area49-s3.md (545자)
```

### runs/2026-09-30-10/pages/categories/safety/human-proximity-safety.md

```markdown
---
title: "49. 사람 근접 안전"
type: area
category: "M. 안전"
area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [속도·분리 감시, 보호 분리 거리, 구역별 속도 제한, 운용 구역, 실외이동로봇 운행안전인증, 사람 인지형 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1075, ref-1076, ref-470, ref-1078, ref-031, ref-980, ref-992, ref-1082, ref-1083, ref-1084, ref-1085, ref-1086, ref-1087, ref-1088, ref-1089]
last_run: 2026-09-30
version: 2
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

확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 왜 중요한가](../../topics/2026/2026-09-30-area49-s3.md)에 있다.

## 4. 핵심 개념과 용어

**속도·분리 감시(Speed and Separation Monitoring, SSM)** — 협동로봇 기술 시방서 ISO/TS 15066 의 방식으로, 로봇과 사람의 분리 거리가 보호 분리 거리 이하가 되면 안전 감시 정지를 건다(2016년 논문 기준). [사실][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area49-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 물류창고

**사례:** 로봇 구역에 들어간 직원 주변에서 로봇이 감속·우회·정지(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 로봇 구역에 들어가며 로보틱스 테크 조끼를 착용·활성화한다. [추정] 벤더 주장[^ref-1084] |
| 작업 대상 | 로봇 구역(공간)과 그 안에서 일하는 직원(사람). [추정] 벤더 주장[^ref-1084] |
| 수행 자원 | 조끼를 켠 직원과 그 신호에 반응하는 로봇. [추정] 벤더 주장[^ref-1084] |
| 제약 | 조끼를 켜면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다. [추정] 벤더 주장[^ref-1084] 감속 속도·거리 값은 미확인이다. |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(처리량 영향 자료 없음) |

이 사례는 아마존이 자사 풀필먼트 센터 운영을 설명한 글(발행일 미확인, 2026-09-30 확인)에 근거하며, 독립 출처로 확인하지 못했다. [추정] 벤더 주장[^ref-1084] 이 영역은 제약 칸, 곧 사람 위치 신호를 받아 어느 로봇을 감속·정지시킬지 정하는 부분에 관여한다. [의견][^ref-1084]

창고를 대상으로 한 연구로는 Farrell 외(2025-03)가 학습 기반 제어 장벽 함수(Control Barrier Function, CBF)를 [Open-RMF](../../glossary/open-rmf.md) 에 통합해 보행자를 포함한 정적·동적 장애물 회피를 평가한 것이 있다. [사실][^ref-1086] 이는 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가이며, 정량 결과는 미확인이다. [사실][^ref-1086]

**현장 유형:** 병원

**사례:** 병원 물류 로봇의 사람 보행 속도 수준 주행 평가(모의 병원 환경)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병원 물류 로봇이 주행하는 모의 병원 환경의 공간. [사실][^ref-1085] |
| 수행 자원 | 병원 물류용 HOSBOT 과 TIAGo 두 로봇. [사실][^ref-1085] |
| 제약 | 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켰고, 속도 선정 근거로 사람 보행 하한 0.6~1.3 m/s 를 인용했다. [사실][^ref-1085] |
| 완료·인계 | 미확인 |
| 예외·성과 | 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 최고 속도에서 방향 오차가 커졌으며 정확도는 중간 속도에서 가장 높았다. [사실][^ref-1085] |

이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다(Scientific Reports, 2024-08-07). [사실][^ref-1085] 로봇 속도를 사람 보행 속도에 맞춰 고른 점이 이 영역의 '언제 느려져야 하는가'와 이어진다. [의견][^ref-1085]

**현장 유형:** 실외

**사례:** 배송 로봇의 보도·횡단보도 운행(실외이동로봇 운행안전인증 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배송 등 목적으로 자율주행·원격제어 로봇이 실외를 운행한다. [사실][^ref-980] |
| 작업 대상 | 횡단보도를 포함한 실외 통행 공간. [사실][^ref-980] |
| 수행 자원 | 자율주행·원격제어 로봇과 관제장치의 조합(인증 단위). [사실][^ref-980] |
| 제약 | 최고 속도 15 km/h 이하·최대 질량 500 kg 이하(인증기관 페이지, 2026-09-30 확인). [사실][^ref-980][^ref-992] 2023-07-28 기사가 전한 당시 개정안 기준으로는 로봇과 적재물 질량 합계가 230 kg 초과면 5 km/h, 100 kg 초과면 10 km/h, 그 이하면 15 km/h 이고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단한다. [사실][^ref-992] |
| 완료·인계 | 미확인 |
| 예외·성과 | 주변 인식과 비상정지가 심사 항목이고, 인증 뒤 2년 주기 정기점검을 받는다. [사실][^ref-980] |

이 사례는 특정 도입 현장이 아니라 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 따른 인증 요구를 여섯 항목으로 옮긴 것이다. [사실][^ref-980] 심사 항목 수는 인증기관 페이지(8개 항목)와 2023-07-28 기사(16가지)가 달라, 한쪽을 고르지 않고 11절 열린 질문으로 올렸다. [사실][^ref-980][^ref-992] 인증 대상에 관제장치가 포함된다는 점은 9절에서 ROP 범위와 겹칠 수 있는 경계로 다룬다.

제조 공장은 산업용 로봇 사업장 규정(7절)과 협동 작업셀 연구(6절)만 확인했고 현장 유형을 밝힌 적용 사례는 찾지 못했다. 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례도 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1078][^ref-031][^ref-1087][^ref-1089]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area49-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1088][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)에서 다룬다.

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area49-s7.md)에 있다.

## 8. 대표 연구와 자료

Marvel·Norcross(NIST), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells(2016) — SSM 의 보호 분리 거리를 구성요소별로 나누고 NIST 시험 결과와 구현 한계(방향 무시에 따른 불필요한 정지, 센서 잡음, 갱신 주기)를 제시했다. [사실][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-09-30-area49-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하고, 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하며, 그 조정과 정지·재개 이력을 기록한다. [추정][^ref-031][^ref-1084][^ref-1086][^ref-1087] | 연계 대상: 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(로봇 제조사·시스템 통합자), Nav2 Collision Monitor 같은 로봇 측 로컬 회피 계층. [추정][^ref-1075][^ref-470][^ref-1078][^ref-1082] |
| 시설·설비 제어 | 설비·로봇의 안전 설정값과 상태를 받아 계획에 반영하는 인터페이스. [추정][^ref-1082][^ref-1088] | 연계 대상: 울타리 같은 설비 안전 조치, 현장 배치의 위험성 평가(IMR 시스템 통합자). [추정][^ref-1082][^ref-1088] |
| 업종별 조건 | 실외 속도 상한·횡단보도 대기 같은 조건을 작업·경로 제약으로 반영한다. [추정][^ref-980][^ref-992] | 연계 대상: 실외 인증 대상인 로봇·관제장치 조합의 적합성(운영 사업자). [추정][^ref-980] |

VDA 5050 명세는 스스로 안전 표준이 아니라고 밝히고 Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않는다고 밝히므로, ROP 가 내리는 구역·속도 제한과 사람 인지형 조정은 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다. [추정][^ref-031][^ref-1078] 사람 위치 신호에 따른 조정은 벤더 주장과 연구 평가에 기대고 있어 현장 효과는 아직 확인되지 않았다. [추정][^ref-1084][^ref-1086][^ref-1087]

실외이동로봇 운행안전인증의 대상은 로봇과 관제장치의 조합이므로, ROP 가 실외 로봇의 관제 역할을 맡으면 인증 범위와 겹칠 수 있다. [추정][^ref-980] 인증 적합성을 운영 사업자의 몫으로 본 것도 확인된 규정이 아니라 추론이다. [추정][^ref-980]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1088][^ref-031][^ref-1087]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가?[^ref-031]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 열린 질문](../../topics/2026/2026-09-30-area49-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1078]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1082]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1084]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-09-30
[^ref-1085]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-09-30
[^ref-1086]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1088]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1089]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30
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

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s6.md

```markdown
---
title: "49. 사람 근접 안전 — 대표 접근법과 기술"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1078, ref-031, ref-1084, ref-1086, ref-1087, ref-1089]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#6
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 대표 접근법과 기술

# 49. 사람 근접 안전 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1078][^ref-031][^ref-1087][^ref-1089]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1078][^ref-031][^ref-1087][^ref-1089]

### 계산으로 정하는 보호 분리 거리

Marvel·Norcross(NIST, 2016)는 SSM 의 보호 분리 거리를 사람 이동 속도, 로봇 반응 시간, 정지 시간(정지 거리), 침입 거리, 위치 측정 불확실도로 나누어 정리했다. [사실][^ref-1075] 같은 연구는 ISO 13855 가 사람 속도로 최대 2,000 mm/s 를 쓰고 분리 거리가 500 mm 보다 크면 1,600 mm/s 를 선택할 수 있다고 소개했고, 침입 거리는 센서 구성·접근 방향에 따라 850 mm·1,200 mm 처럼 달라지며, NIST 시험에서 레일 장착 6자유도 매니퓰레이터의 반응 시간은 약 0.113초였다고 보고했다. [사실][^ref-1075]

한계도 보고됐다. SSM 식은 속도의 방향을 무시하고 크기만 써서 멀어지는 로봇도 불필요한 정지를 일으킬 수 있고, 센서 잡음이 속도 추정 오차를 키우며, 갱신 주기가 낮을수록 로봇 평균 속도가 떨어지고, 제동 거리와 반응 시간이 보호 거리에 크게 영향을 준다. [사실][^ref-1075]

### 로봇 측 감속·정지 영역

ROS 2 내비게이션 스택 Nav2 의 Collision Monitor 는 컨트롤러 속도 명령을 거르는 독립 노드로, 영역 안 장애물 점 수에 따른 정지·감속(비율)·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두며, 여러 영역이 동시에 걸리면 가장 강한 조치를 쓴다. [사실][^ref-1078] README 는 이 기능이 하드 실시간 안전 인증을 제공하지 않는다고 밝힌다. [사실][^ref-1078] 이 계층은 로봇 쪽 로컬 회피에 속하므로 ROP 에게는 연계 대상이다. [추정][^ref-1078]

### 플릿 수준 구역·속도 제한

VDA 5050 3.0.0(2026-09-30 확인)은 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 진입 금지(BLOCKED), 플릿 관제 승인 후 진입(RELEASE), 최고 속도 제한(SPEED_LIMIT), 자율 재계획 금지, 동작 유발, 우선·벌점·방향 구역을 정의한다. [사실][^ref-031] 속도 제한 구역에 대해서는 "Mobile robots shall not drive faster than the defined maximum speed within this zone." 이라고 규정한다. [사실][^ref-031] 동시에 명세는 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 밝혀, 구역·속도 제한 전달이 안전 기능 자체를 대신하지 않음을 명시한다. [사실][^ref-031]

### 사람 위치를 반영한 배정·교통

아마존은 직원이 로보틱스 테크 조끼를 착용·활성화하면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명한다(발행일 미확인). [추정] 벤더 주장[^ref-1084] Farrell 외(2025-03)는 학습 기반 CBF 를 Open-RMF 에 통합해 창고 시나리오의 다중 로봇·다중 행위자 상황에서 보행자를 포함한 장애물 회피를 강화하는 제어를 제안하고 로봇 수·속도·장애물 수를 바꿔 평가했다(정량 결과 미확인). [사실][^ref-1086]

Kazemi Eskeri 외(IROS 2025)의 사람 인지형 작업 배정(Human-Aware Task Allocation, HATA)은 움직임 지도로 사람이 작업 실행 시간에 주는 영향을 확률적 비용으로 추정해 배정에 반영했고, 사람 움직임을 고려하지 않는 기준선보다 임무 완료 시간을 최대 26%, 기존 기준선보다 최대 19% 줄였다고 보고했다. [사실][^ref-1087]

### 안전 거리와 별개인 편안함 지표

Jafari·Nguyen·Liu(2026-04)는 이동 로봇과 자원 보행자의 일대일 조우 실험에서 보행자가 보고한 편안함이 최소 거리·최소 예상 충돌 시간 같은 운동학 변수와 중간 정도의 유의한 상관을 보였고, 이를 합친 복합 지표가 오즈비 3.67 로 가장 잘 예측했다고 보고했다(실험 장소·참가자 수 미확인). [사실][^ref-1089]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1078]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1084]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-09-30
[^ref-1086]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1089]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s7.md

```markdown
---
title: "49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1076, ref-470, ref-1078, ref-031, ref-980, ref-992, ref-1082, ref-1088]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#7
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스

# 49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1088][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)에서 다룬다.
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1088][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)에서 다룬다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 10218-1/2:2025, ISO/TS 15066 | 표준 | Hartmann 외(2026-02)는 2025년 개정판이 협동 작업 기술 시방서 ISO/TS 15066 을 선택적 지침에서 규범적 요구로 본문에 통합하고, 로봇·협동 적용의 새 분류와 사이버보안 요구를 더했다고 분석했다. [사실][^ref-1076] | Hartmann 외(arXiv 프리프린트) |
| ISO 3691-4:2023 | 표준 | 인력 감지를 끄거나 감지가 온전히 작동하지 않는 상황(예: 도킹)에서 속도를 0.3 m/s 이하로 제한하고, 서 있는 사람(지름 200 mm·높이 600 mm 원통)과 누운 사람(지름 70 mm·길이 400 mm 원통) 시험편으로 인력 감지 성능을 확인하는 것으로 알려져 있다(표준 원문 미확인, 검색 요약 기준). [추정][^ref-470] 구역 구분은 4절. | ISO(원문 미열람) |
| ANSI/A3 R15.08-2(2023) | 표준 | 산업용 이동 로봇(Industrial Mobile Robot, IMR)을 특정 적용·현장에 맞춰 통합·배치할 때의 안전 요구를 다루며, 배치 시스템의 위험성 평가는 IMR 시스템 통합자가 수행하도록 하고 [모바일 매니퓰레이터](../../glossary/mobile-manipulator.md)와 최종 사용자 정보·교육을 포함한다고 The Robot Report(2023-10-26)가 전했다. 표준 본문은 유료라 열람하지 못했다. [사실][^ref-1088] | The Robot Report |
| [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md) | 평가 프로그램 | 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거해 배송 등 목적의 로봇과 관제장치의 조합에 최고 속도 15 km/h 이하·최대 질량 500 kg 이하를 요구하고, 주변 인식·비상정지·횡단보도 통행·관제장치 등을 심사하며 2년 주기 정기점검을 둔다(2026-09-30 확인). [사실][^ref-980][^ref-992] 질량별 속도 구간은 5절 실외 사례. | 한국로봇산업진흥원, 지디넷코리아 |
| 산업안전보건기준에 관한 규칙 제223조 | 법규 | 지디넷코리아 기사(2024-03-09)에 따르면 산업용 로봇 운전 중 위험 방지를 위해 높이 1.8미터 이상 울타리 설치를 기본으로 하되 일정 안전기준을 충족하면 면제될 수 있다(법령 원문 미확인). [추정][^ref-1082] 같은 기사는 SSM·HGC·PFL 을 이 조문의 내용이 아니라 국제 기준(ISO/TS 15066 계열)이 정한 협동 방식으로 소개한다. [추정][^ref-1082] | 지디넷코리아 |
| VDA 5050 3.0.0 구역 | 표준 | 진입 금지·승인·속도 제한 구역을 플릿 관제가 로봇에 전달하는 형식이며(6절), 명세 스스로 안전 표준이 아니라고 밝힌다. [사실][^ref-031] | VDA / VDMA |
| Nav2 Collision Monitor | 오픈소스 | 로봇 측 정지·감속·속도 제한 영역을 두는 노드이며(6절), 하드 실시간 안전 인증을 제공하지 않는다고 밝힌다. [사실][^ref-1078] | Open Navigation |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1078]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1082]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1088]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s8.md

```markdown
---
title: "49. 사람 근접 안전 — 대표 연구와 자료"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1076, ref-1083, ref-1085, ref-1086, ref-1087, ref-1089]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#8
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 대표 연구와 자료

# 49. 사람 근접 안전 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Marvel·Norcross(NIST), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells(2016) — SSM 의 보호 분리 거리를 구성요소별로 나누고 NIST 시험 결과와 구현 한계(방향 무시에 따른 불필요한 정지, 센서 잡음, 갱신 주기)를 제시했다. [사실][^ref-1075]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Marvel·Norcross(NIST), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells(2016) — SSM 의 보호 분리 거리를 구성요소별로 나누고 NIST 시험 결과와 구현 한계(방향 무시에 따른 불필요한 정지, 센서 잡음, 갱신 주기)를 제시했다. [사실][^ref-1075]
- Hartmann 외, ISO 10218-1/2(2011 대 2025) 비교와 ISO/TS 15066 통합 분석(2026-02, 프리프린트) — 협동 작업 요구가 선택적 지침에서 규범적 요구로 바뀐 점을 분석했다. [사실][^ref-1076]
- Francis 외 52명, Principles and Guidelines for Evaluating Social Robot Navigation Algorithms(2023, 학술지판 2025) — 사회적 로봇 주행 원칙을 안전·편안함·가독성·예의·사회적 역량·상대 이해·능동성·맥락 적합성 8가지로 정하고 지표·시나리오·벤치마크·시뮬레이터 지침을 제시했다. [사실][^ref-1083]
- Jafari·Nguyen·Liu, Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters(2026-04, 프리프린트) — 최소 거리·최소 예상 충돌 시간 등으로 보행자 편안함을 예측했다(6절). [사실][^ref-1089]
- Rondoni 외, Navigation benchmarking for autonomous mobile robots in hospital environments(2024-08) — 모의 병원 환경에서 두 병원 로봇을 세 속도·7개 지표로 비교했다(5절). [사실][^ref-1085]
- Farrell 외, Safe Human Robot Navigation in Warehouse Scenario(2025-03, 프리프린트) — 학습 기반 CBF 를 Open-RMF 에 통합한 창고 시나리오 연구다(정량 결과 미확인). [사실][^ref-1086]
- Kazemi Eskeri 외, Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments(IROS 2025) — 움직임 지도 기반 사람 인지형 배정으로 임무 완료 시간을 최대 26% 줄였다고 보고했다. [사실][^ref-1087]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-1083]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (arXiv; 학술지판 ACM Transactions on Human-Robot Interaction 14(2), 2025-02), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1085]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-09-30
[^ref-1086]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1089]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s10.md

```markdown
---
title: "49. 사람 근접 안전 — 다른 연구영역과의 연결"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1076, ref-470, ref-031, ref-980, ref-992, ref-1082, ref-1083, ref-1084, ref-1085, ref-1086, ref-1087, ref-1088, ref-1089]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#10
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 다른 연구영역과의 연결

# 49. 사람 근접 안전 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1088][^ref-031][^ref-1087]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1088][^ref-031][^ref-1087]

- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 속도 제한·진입 금지·승인 구역을 지도 위 장소 의미로 담는다. [추정][^ref-031]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 움직임 지도와 보행자 편안함 예측이 사람 이동 모델에 기댄다. [추정][^ref-1087][^ref-1089]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 구역·속도 제한을 제조사 관제와 로봇에 전달하는 통로다. [추정][^ref-031]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — VDA 5050 의 구역 유형과 '안전 표준이 아님' 명시가 상호운용 표준의 범위를 보여 준다. [추정][^ref-031]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 사람 움직임을 비용으로 반영하는 사람 인지형 배정이 이어진다. [추정][^ref-1087]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 구역·속도 제한과 보행자 회피를 경로·교통 계획에 반영한다. [추정][^ref-031][^ref-1086]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — SSM·PFL 같은 협동 작업 방식이 협업의 안전 조건이다. [추정][^ref-1075][^ref-1082]
- [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) — 학습 기반 CBF 와 사람 움직임 예측을 쓰는 배정은 학습·예측 기법을 적용한 예다. [의견][^ref-1086][^ref-1087]
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 통합자 위험성 평가와 정지·재개 판단이 이 영역의 전제다. [추정][^ref-1088]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — ISO 10218·ISO/TS 15066·ISO 3691-4·실외 인증의 상세를 다룬다. [추정][^ref-1076][^ref-470][^ref-980]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 사회적 주행 평가 지침과 병원 주행 벤치마크가 평가 방법을 준다. [추정][^ref-1083][^ref-1085]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 산업용 로봇 울타리 규정과 실외이동로봇 운행안전인증이 법규 측면이다. [추정][^ref-1082][^ref-980]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 사람이 느끼는 편안함과 사회적 주행 원칙이 수용성과 이어진다. [추정][^ref-1083][^ref-1089]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 조끼 신호 기반 감속·정지와 창고 시나리오 연구가 이 현장 유형의 사례다. [추정][^ref-1084][^ref-1086]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 모의 병원 환경의 속도별 주행 평가가 이 현장 유형의 근거다. [추정][^ref-1085]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 실외 속도·질량 상한과 횡단보도 대기 규칙이 이 현장 유형의 조건이다. [추정][^ref-980][^ref-992]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1082]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1083]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (arXiv; 학술지판 ACM Transactions on Human-Robot Interaction 14(2), 2025-02), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1084]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-09-30
[^ref-1085]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-09-30
[^ref-1086]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1088]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1089]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s4.md

```markdown
---
title: "49. 사람 근접 안전 — 핵심 개념과 용어"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-470, ref-031, ref-1082, ref-1087]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#4
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 핵심 개념과 용어

# 49. 사람 근접 안전 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **속도·분리 감시(Speed and Separation Monitoring, SSM)** — 협동로봇 기술 시방서 ISO/TS 15066 의 방식으로, 로봇과 사람의 분리 거리가 보호 분리 거리 이하가 되면 안전 감시 정지를 건다(2016년 논문 기준). [사실][^ref-1075]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **속도·분리 감시(Speed and Separation Monitoring, SSM)** — 협동로봇 기술 시방서 ISO/TS 15066 의 방식으로, 로봇과 사람의 분리 거리가 보호 분리 거리 이하가 되면 안전 감시 정지를 건다(2016년 논문 기준). [사실][^ref-1075]
- **보호 분리 거리(Protective Separation Distance)** — 사람 이동 속도, 로봇 반응 시간, 로봇 정지 시간(정지 거리), 침입 거리, 로봇·사람 위치 측정 불확실도로 계산하는 거리다. [사실][^ref-1075]
- **동력·힘 제한(Power and Force Limiting, PFL)** — 기사(2024-03-09)는 국제 기준(ISO/TS 15066 계열)의 협동 방식을 SSM·핸드 가이딩(Hand Guiding, HGC)·PFL 로 소개하고, PFL 을 제한된 힘으로 작동하는 방식으로 설명한다. [추정][^ref-1082] 관련 용어: [협동 적용](../../glossary/collaborative-application.md)
- **[운용 구역](../../glossary/operating-zone.md)(Operating Zone)** — ISO 3691-4:2023 은 사람이 있어 인력 감지가 필요한 운용 구역, 훈련된 인원만 들어가는 제한 구역, 울타리 등으로 사람을 배제한 구역을 나눠 보호 조치를 달리하는 것으로 알려져 있다(표준 원문 미확인, 검색 요약 기준). [추정][^ref-470]
- **속도 제한·진입 금지·승인 구역** — VDA 5050(독일자동차산업협회 무인운반차 인터페이스) 3.0.0 이 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 정의한 SPEED_LIMIT·BLOCKED·RELEASE 등이다. [사실][^ref-031] 관련 용어: [구역 집합](../../glossary/zone-set.md), [해제 구역](../../glossary/release-zone.md)
- **움직임 지도(Maps of Dynamics, MoD)** — 과거 사람 이동 패턴을 담아 장소·시간별로 질의하는 시공간 지도로, 사람 인지형 작업 배정에서 사람이 작업 시간에 주는 영향을 추정하는 데 쓰였다. [사실][^ref-1087]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1082]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s11.md

```markdown
---
title: "49. 사람 근접 안전 — 열린 질문"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-980, ref-992, ref-1084]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#11
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 열린 질문

# 49. 사람 근접 안전 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가?[^ref-031]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가?[^ref-031]
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사(2023-07-28)는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가?[^ref-980][^ref-992]
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가?[^ref-1084]

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1084]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-10/pages/topics/2026/2026-09-30-area49-s3.md

```markdown
---
title: "49. 사람 근접 안전 — 왜 중요한가"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1076, ref-470, ref-980, ref-992, ref-1082, ref-1083, ref-1087, ref-1088, ref-1089]
last_run: 2026-09-30
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#3
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 왜 중요한가

# 49. 사람 근접 안전 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]

협동로봇·무인 산업용 트럭·산업용 이동 로봇·실외 이동 로봇은 서로 다른 표준·법규·인증이 구역과 속도 상한을 정하므로, 적용 유형마다 따라야 할 기준이 다르다. [추정][^ref-1076][^ref-470][^ref-1088][^ref-980] 국내 산업용 로봇의 울타리 면제는 기사(2024-03-09)가 전한 수준으로만 확인했다. [추정][^ref-1082]

보수적인 감속·정지는 처리량과 사람의 수용성에도 영향을 준다. [추정][^ref-1075][^ref-1089][^ref-1087]

핵심 질문에 대한 지금까지의 답은 세 가지다. 분리 거리는 고정값이 아니라 사람 속도·반응 시간·정지 거리·측정 불확실도로 그때그때 계산되고, 감속·정지 기준은 적용 유형별 표준·인증이 구역·속도 상한으로 정하며, 사람이 편안하게 느끼는 거리·충돌 시간은 안전 정지 거리와 별도의 기준이 필요한 것으로 보인다. [추정][^ref-1075][^ref-470][^ref-980][^ref-992][^ref-1083][^ref-1089] 이 답의 근거 가운데 무인 산업용 트럭 표준(ISO 3691-4)의 구역·속도 내용은 표준 원문을 확인하지 못한 것이고, 실외 로봇의 질량별 속도 구간은 2023-07-28 기사가 전한 당시 개정안이다. [추정][^ref-470][^ref-992]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1082]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1083]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (arXiv; 학술지판 ACM Transactions on Human-Robot Interaction 14(2), 2025-02), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-09-30
[^ref-1087]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1088]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1089]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-10 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-10 | 49. 사람 근접 안전 의 "왜 중요한가" 절에서 분리 |
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
