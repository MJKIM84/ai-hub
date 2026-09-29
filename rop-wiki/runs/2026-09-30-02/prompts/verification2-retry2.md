(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-02
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 67. 기타 현장 (Q. 현장 유형별 적용)
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
- retry_count: 2
- max_retries: 2

## 입력

### runs/2026-09-30-02/target.json

```json
{
  "run_id": "2026-09-30-02",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 111,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 67,
    "area_name": "67. 기타 현장",
    "category": "Q. 현장 유형별 적용",
    "category_letter": "Q"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=67"
}
```

### runs/2026-09-30-02/research.json

```json
{
  "run_id": "2026-09-30-02",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 67,
    "area_name": "67. 기타 현장",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — SiLA 2·자율 실험실·브레인리스 로봇·정상 무인 시설 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 플랜트·변전소 점검, 건설 현장, 농업, 공항, 오피스 빌딩, 데이터센터, 연구실 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 점검 데이터 수집·AI 분석, BIM 비교, 작업자 추종·유도선 주행, 클라우드 두뇌 로봇 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 이동 로봇 화학자(Nature 2020) 등 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]",
    "플랜트·변전소·데이터센터의 점검·순찰 로봇은 무엇을 점검하고 어떤 설비·통신 조건에서 운영되는가? (섹션 3·5·6 겨냥)",
    "건설 현장에서 로봇은 매일 바뀌는 현장 상태를 BIM(Building Information Modeling)과 어떻게 대조하고 무엇을 기록하는가? (섹션 5·6 겨냥, 한국 자료 우선)",
    "농업 현장에서 여러 로봇을 함께 운영하는 국내 사례와 관리 방식(통합 관리 프로그램, 수확·운반 분업, 작업자 추종)은 무엇인가? (섹션 5·6·8 겨냥)",
    "공항·오피스 빌딩·연구실 같은 공공시설·업무 공간에서 로봇은 무엇을 하고 승강기·출입문·실험 장비와 어떻게 연동되는가? (섹션 5·6 겨냥)",
    "기타 현장에 적용되는 표준·프레임워크(ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF)는 무엇을 다루는가? (섹션 7 겨냥)",
    "기타 현장에서 ROP 가 직접 맡을 것과 로봇 자체 기능·설비·업무 시스템·업종별 규정에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Offshore Technology(2025-11-21)에 따르면 Equinor 는 2024-11부터 평소 사람이 상주하지 않도록 설계된 노르웨이 Northern Lights 이산화탄소 포집·저장(CCS) 시설에 ANYbotics 의 4족 로봇 ANYmal('Roberta')을 배치해 계기 판독·밸브 위치 확인·CO2 농도 감시·누출 탐지를 맡겼으며, 현장 운영자가 연구개발 부서 지원 없이 직접 임무를 만들기 시작했다.",
      "tag": "사실",
      "source_ids": [
        "ref-995"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Roberta 는 광학 줌·열화상·가스·음향 센서와 3D LiDAR·SLAM 을 갖추고 IP67 등급이며, 과제는 계기 판독·밸브 위치·누출 탐지 등이다. 'Operators have begun creating their own missions without R&D support'",
      "as_of": "2025-11-21",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f2",
      "claim": "Equinor 는 로봇을 폭넓게 도입하면 연간 10억 노르웨이 크로네(약 9,910만 달러)를 넘는 비용을 절감할 것으로 추산한다.",
      "tag": "추정",
      "source_ids": [
        "ref-995"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사가 전한 운영사(Equinor)의 추산이며 산정 방법은 공개되지 않았다. 과제 선정 기준으로 '지루하고 더럽고 멀고 위험한 일(4D)'을 든다.",
      "as_of": "2025-11-21",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "넷매니아즈(2023-09-30)가 정리한 한국전력공사 실증 자료에 따르면 한전은 2022-12 신중부 변전소에 5G 특화망을 구축하고 4족 로봇이 아날로그·디지털 계기와 LED·밸브·램프 상태를 촬영하고 열화상 영상을 모아 AI 서버로 스트리밍하게 했으며, 무선 IoT 센서와 무선 CCTV(추락·쓰러짐·위험지역 접근·화재·침입 감지)를 함께 운영했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1008"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원출처: 한전 '5G 특화망 기반 변전소 과제서비스 구축 및 실증'(2022-12-20). 도입 배경으로 900여 개 변전소 가운데 50% 이상이 20년 넘은 설비라는 점을 든다. 영상은 FHD·30fps 로 AI 서버에 전송.",
      "as_of": "2023-09-30",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f4",
      "claim": "Energy Robotics(2026-05 Korial 로 사명 변경)는 하드웨어에 독립적인 로봇 운영 소프트웨어와 클라우드 기반 플릿 관리, AI 데이터 분석을 결합한 산업 점검 플랫폼을 내세우며, Boston Dynamics Spot·ExRobotics ExR-1 을 포함해 20개가 넘는 하드웨어 플랫폼을 제어하도록 소프트웨어를 맞춰 왔다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1003"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사 사이트에 실린 투자사(Earlybird) 글(2021-01-15). 창업팀이 20개 이상 하드웨어 플랫폼을 제어하도록 소프트웨어를 맞췄고 200개 이상의 소프트웨어 구성 요소를 갖췄다고 적는다. 독립 확인 없음.",
      "as_of": "2021-01-15",
      "site_type": null,
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f5",
      "claim": "서울신문(2022-11-15)에 따르면 현대건설은 건설 현장의 안전·품질 관리에 4족 보행 로봇 스팟을 투입해 현장 사진 촬영·기록 자동화, 영상·환경 센서 실시간 모니터링, 레이저 스캐닝 3D 데이터 수집, QR 코드 기반 자재 추적, 출입 제한 구역 위험 경보를 하게 하고, 사무실에서 현장을 실시간으로 확인하게 했으며, 2023년 김포–파주 고속도로 현장에서 시범 운영할 계획이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-999"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "계단·좁은 공간 등 사람이 접근하기 어려운 곳을 다니며, 아파트 공사에서는 하루 최대 2만 장의 사진 비교가 필요해 자동화 효과가 크다고 회사가 설명했다.",
      "as_of": "2022-11-15",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f6",
      "claim": "인더스트리뉴스에 따르면 GS건설은 2020-07 큐픽스와 함께 스팟을 국내 건설 현장에 처음 도입해 성남 아파트 현장(지하주차장 골조·세대 내부 마감)과 서울 공연장 신축 현장에서 실증했고, 로봇에 단 LiDAR·360도 카메라·IoT 센서로 모은 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1000"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "활용 목표로 입주 전 하자 품질 검토, 교량 공사 현장 공정·품질 점검도 적었다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": "완료·인계"
    },
    {
      "id": "f7",
      "claim": "이코노미스트(2023-01-11)에 따르면 네이버 제2사옥 1784 에서는 로봇이 초기 40대에서 약 100대로 늘었고, 두뇌를 클라우드에 둔 '브레인리스' 배달 로봇 루키를 네이버 클라우드와 5G 특화망 기반의 멀티 로봇 시스템 ARC(AI·Robot·Cloud)가 제어하며, 루키는 로봇 전용 엘리베이터 로보포트로 층을 오가며 커피·택배를 자리까지 배달하고 충전소로 돌아간다.",
      "tag": "사실",
      "source_ids": [
        "ref-997"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ARC 가 실시간으로 로봇·공간·서비스·사용자를 연결·제어하며, 5G 로 클라우드에 연결해 로봇 제작비를 줄인다고 설명한다.",
      "as_of": "2023-01-11",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "네이버는 1784 사옥 로봇 배달 시간이 초기 15~17분에서 5~10분으로 줄었다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-997"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 로봇·플랫폼을 직접 개발·운영하는 회사의 설명을 기사가 전한 수치이며 측정 조건은 공개되지 않았다.",
      "as_of": "2023-01-11",
      "site_type": "기타",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f9",
      "claim": "아주경제(2023-11-08)에 따르면 네이버 데이터센터 각 세종에서는 네이버랩스가 개발한 서버 관리 로봇 '세로'와 서버실·창고를 오가며 고중량 자산을 나르는 운반 로봇 '가로'가 협력해 자산 흐름을 실시간으로 추적·관리하고, 두 로봇은 ARC 와 ARM 시스템을 통해 공간·서비스 인프라와 실시간으로 연동된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1002"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "로봇이 운영 효율화를 맡고 사람은 고차원 관리 업무에 집중하게 한다는 설명. 위성 위치를 쓸 수 없는 실내에서 위치 파악·경로 계획을 한다.",
      "as_of": "2023-11-08",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f10",
      "claim": "로봇신문(2018-07-11)에 따르면 인천국제공항공사는 2018-07-21부터 푸른기술·LG CNS 컨소시엄이 만든 안내 로봇 에어스타를 제1여객터미널 8대·제2여객터미널 6대로 운영해 출국장·면세지역·입국장 수하물 수취 지역에서 항공편·체크인 카운터 안내, 목적지 에스코트, 4개 국어 음성 안내, 기내 반입 금지 물품 회수를 하게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-998"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "하계 성수기에 맞춘 정식 운영. 여객 기념사진 촬영·이메일 전송 기능도 갖췄다.",
      "as_of": "2018-07-11",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f11",
      "claim": "The Robot Report(2025-10-29)에 따르면 싱가포르 국가 로봇 프로그램이 2018년 ROS 기반으로 함께 출범시킨 로봇 미들웨어 프레임워크(RMF, 현 Open-RMF)는 제조사가 다른 로봇과 시스템이 함께 일하게 하는 것으로, 창이 공항 같은 대형 시설에서 이미 운영되고 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RMF 가 통합 복잡도를 줄여 더 안전하고 효율적인 배치를 돕는다고 설명한다. 창이 공항의 로봇 대수·제조사 수는 이 기사에 없다.",
      "as_of": "2025-10-29",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "같은 기사에 따르면 싱가포르는 로봇·승강기·자동문 사이 데이터 교환 표준 SS 713 과 로봇·중앙 관제 시스템 상호운용 기술 참조 TR 130 을 두고 SS 713 을 ISO 국제표준으로 올리려 하며, BCA Braddell 캠퍼스의 ELEVATE 시험장에서 로봇·승강기·건물 시스템의 상호작용을 시험한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SS 713: Data Exchange Between Robots, Lifts and Automated Doorways / TR 130: Interoperability Between Robots and Central Command Systems. 표준 원문은 열지 않았다.",
      "as_of": "2025-10-29",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "Burger 외(Nature 583, 2020)는 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 움직이며 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-996"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "장비를 자동화하는 대신 연구자를 자동화하는 접근이라고 설명한다(검색 결과 요약 범위). 저장소 PDF 는 본문 추출에 실패해 원문 미열람.",
      "as_of": "2020-07",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "SiLA 컨소시엄의 SiLA 2 는 실험실 장비를 'SiLA 서버'로 보고 서버의 능력을 Command(매개변수를 받는 동작)와 Property(읽거나 구독하는 데이터)를 담은 Feature 로 기술하며, 서버·Feature 자동 탐색과 gRPC(HTTP/2·Protocol Buffers) 통신을 규정하고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했으나 워크플로 오케스트레이션은 표준 범위 밖이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1001"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세는 Core·Mapping·Features 세 부분으로 구성된다. 'SiLA Robotics & mobile Robotics' 작업반이 활동 중이며, 오케스트레이션은 Camunda 같은 외부 구현 예로만 언급된다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "뉴스토마토(2025-04-23)에 따르면 농촌진흥청은 자체 개발한 방제 로봇(2022)·운반 로봇(2023)·모니터링 로봇(2024)을 개인용 컴퓨터나 휴대전화 하나로 함께 관리하는 통합 관리 프로그램을 개발했으며, 이 프로그램은 로봇의 위치·속도·이동 거리와 운영 통계를 보여 주고 작업 순서를 설정하며, 모니터링 로봇 영상으로 수확 가능한 열매 수·위치·익은 정도를 알려 주고 작업·작물 정보로 방제 횟수와 수확 시기를 조절하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1007"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사는 안전무결성 수준(SIL) 2등급 제어기를 적용했다고 전한다. 관리 대상은 농촌진흥청이 개발한 로봇 3종이며, 다른 제조사 로봇의 연결 여부는 언급되지 않는다.",
      "as_of": "2025-04-23",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "농민신문(2024-03-25)에 따르면 농촌진흥청이 스마트팜에 시범 보급한 작업자 추종 운반 로봇은 3D 카메라로 작업자와 10cm~1m 간격을 유지하며 따라가고, 최대 300kg 을 싣고 한 번 충전으로 10시간 운행하며, 바닥의 바코드 유도선을 따라 재배 현장과 집하장 사이를 자율로 오간다. 2024년에는 8개 지역 10개 농가를 대상으로 시범사업을 진행했고, 로봇 속도와 유도선 내구성이 개선 과제로 꼽혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1006"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2024년 시범사업은 강원·충북·충남·전북·경북·경남·부산·인천 8개 지역 10개 농가를 대상으로 하며 국비·지방비 5억 원을 지원한다.",
      "as_of": "2024-03-25",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f17",
      "claim": "헬로디디 보도에 따르면 한국기계연구원은 온실에서 작물을 수확하는 수확 로봇과 수확물을 하역장까지 자율로 나르는 이송 로봇으로 수확부터 운반까지 나눠 맡는 원예작물 수확 다수 로봇 시스템을 개발했으며, 연구진은 작물 인식률 90% 이상, 24시간 운영을 가정하면 사람의 80% 효율로 수확할 수 있다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1005"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "성능 수치는 연구기관의 발표이며 시험 조건은 기사에 없다. 국립농산물품질관리원·대학과 공동 연구. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "ISO 18497 은 2024년 판에서 부분 자동·반자율·자율 농업기계·트랙터의 안전을 설계 원칙·용어(1부), 장애물 보호 시스템(2부), 자율 운용 구역(3부), 검증 방법·타당성 확인 원칙(4부)의 네 부분으로 나눠 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1009"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 페이지가 403 으로 열리지 않아 검색 결과 요약 범위만 썼다. 2018년 판(ISO 18497:2018)은 고도 자동화 농업기계 설계 원칙 단일 문서였다.",
      "as_of": "2024",
      "site_type": "기타",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 67. 기타 현장의 로봇 작업은 (1) 플랜트·변전소 점검·순찰(f1·f3), (2) 건설 현장 공정·품질·안전 점검(f5·f6), (3) 농업의 방제·운반·모니터링·수확(f15~f17), (4) 공항 같은 공공시설의 안내·청소(f10·f11), (5) 오피스 빌딩 사내 배달(f7), (6) 데이터센터 서버 자산 운반·관리(f9), (7) 연구실 실험 수행(f13)의 일곱 형태로 나타난다.",
      "tag": "추정",
      "source_ids": [
        "ref-995",
        "ref-1008",
        "ref-999",
        "ref-1000",
        "ref-1007",
        "ref-1006",
        "ref-1005",
        "ref-998",
        "ref-1004",
        "ref-997",
        "ref-1002",
        "ref-996"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 형태는 단일 출처 사례이며, 형태 구분은 분류 원문 1절 정의(점검·순찰, 건설, 농업, 공공시설, 오피스, 연구실)에 맞춰 이번 자료를 묶은 것이다.",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": "작업 대상"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(다른 현장은 무엇이 다른가)에는 다음과 같이 답할 수 있다. 점검·순찰 현장은 사람이 상주하지 않거나 위험한 설비에서 계기값·열화상·가스 농도 같은 '정보'를 작업 대상으로 삼는다(f1·f3). 건설 현장은 공간이 날마다 바뀌어 수집 데이터를 BIM 과 대조한다(f5·f6). 농업은 비정형 지면과 계절성 때문에 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다(f15·f16). 공항은 다국어 안내·에스코트처럼 사람을 대상으로 한다(f10). 오피스·데이터센터는 전용 승강기·클라우드·5G 같은 건물 인프라에 기댄다(f7·f9). 연구실은 분석 장비 조작과 실험 계획이 한 루프로 묶인다(f13·f14).",
      "tag": "추정",
      "source_ids": [
        "ref-995",
        "ref-1008",
        "ref-999",
        "ref-1000",
        "ref-1007",
        "ref-1006",
        "ref-998",
        "ref-997",
        "ref-1002",
        "ref-996",
        "ref-1001"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "현장별 차이는 이번에 확인한 개별 사례에서 도출한 해석이며, 현장 유형별로 대표성을 측정한 자료는 없다.",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 기타 현장 로봇 작업의 여섯 항목은 다음처럼 채울 수 있다. 시작 조건은 점검 일정·현장 운영자가 만든 임무, 사내 배달 주문, 여객 질의, 실험 계획 알고리즘의 다음 실험 선택이다(f1·f7·f10·f13). 작업 대상은 계기·밸브·열화상 같은 설비 정보, 공사 공간과 자재, 작물·수확물, 서버 자산, 여객, 시료다(f3·f5·f9·f10·f15). 수행 자원은 4족 점검 로봇·클라우드 제어 배달 로봇·전용 승강기·농업 로봇과 작업자·실험 장비다(f1·f7·f13·f16). 제약은 위험 구역·방폭·통신망·유도선·자율 운용 구역이다(f3·f5·f16·f18). 완료·인계는 점검 영상의 AI 서버 전송과 BIM 대조 결과, 자리까지의 배달, 집하장 하역이다(f3·f6·f7·f16). 예외·성과는 출동 감소·비용 절감 추산·배달 시간 단축 같은 주장과 속도·유도선 내구성 문제다(f2·f8·f16).",
      "tag": "추정",
      "source_ids": [
        "ref-995",
        "ref-997",
        "ref-998",
        "ref-996",
        "ref-1008",
        "ref-999",
        "ref-1002",
        "ref-1007",
        "ref-1006",
        "ref-1000",
        "ref-1009"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "완료·인계의 확인 기준(누가 점검 결과를 승인하는지 등)은 이번 자료에서 명시적으로 확인되지 않았다. f2·f8 은 운영사·벤더 추산이다.",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 67. 기타 현장에서 ROP 가 직접 맡을 범위는 다음과 같다. 점검 일정·배달 주문·운반 요청을 받아 로봇에 배정하고 작업 순서를 정하며(f1·f7·f15), 승강기·자동문 연동을 요청·확인하고(f7·f12), 점검 영상·계기값·BIM 대조 결과 같은 작업 결과를 모아 요청한 시스템에 돌려주고(f3·f6), 위험 구역·자율 운용 구역을 운행 제약으로 반영한다(f5·f18). 확인한 국내 사례(네이버 ARC, 농촌진흥청 통합 관리 프로그램)는 한 기관이 만든 로봇을 자체 계층으로 묶은 것이고, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 창이 공항의 Open-RMF(f11)와 벤더 주장(f4) 수준에서만 확인됐다.",
      "tag": "추정",
      "source_ids": [
        "ref-995",
        "ref-997",
        "ref-1007",
        "ref-1004",
        "ref-1008",
        "ref-1000",
        "ref-999",
        "ref-1009",
        "ref-1003"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "직접 범위는 분류 원문 19장의 경계 표를 이번 사례에 대입한 해석이다.",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "연계 대상: 분류 원문 19장 기준으로 다음은 외부에 맡길 영역으로 보인다. 로봇의 SLAM·가스·음향 감지·계단 보행·파지는 로봇 자체 지능·제어에 속한다(f1·f5·f13). 승강기·자동문·5G 특화망·실험 분석 장비(SiLA 서버)는 시설·설비 제어에 속한다(f7·f12·f14). 설비 보전·공정 관리 시스템과 BIM 저작 도구는 상위 업무 시스템에 속한다(f6). 농업기계 안전(ISO 18497)·위험 시설 요건은 업종별 조건에 속한다(f18). 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·상태 확인만 걸고 주행·계측 성능과 설비 제어는 해당 제조사·설비 주체에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-995",
        "ref-999",
        "ref-996",
        "ref-997",
        "ref-1004",
        "ref-1001",
        "ref-1000",
        "ref-1009"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경계 구분은 해석이다. 계기 판독 같은 AI 분석을 로봇 쪽에 둘지 플랫폼 쪽에 둘지는 사례마다 달라(f1 은 로봇 탑재, f3 은 AI 서버) 미정이다.",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "이 영역은 다음 영역들과 이어진다. 승강기·자동문 연동은 22. 설비·건물 시스템 연동(f7·f12)과 연결된다. 이기종 로봇 관제는 20. 로봇·제조사 관제 연동(f4·f11), 표준은 21. 상호운용 표준·적합성(f12·f14·f18)과 연결된다. BIM 대조는 14. 도면·BIM에서 지도 만들기·16. 장소 의미·지도 관리(f6), 자산·자재 추적은 17. 작업 대상·자산 식별과 인계 추적(f5·f9), 점검 이상 감지는 38. 모니터링·이상 탐지·원인 분석(f1·f3)과 연결되며, 계기 판독·열화상 분석은 45. 문서·도면·장면 이해(f3)와도 이어진다. 작업 순서 설정은 26. 작업 순서·스케줄링(f15), 수확·이송 분업은 25. 작업 배정 — MRTA(f17), 작업자 추종은 31. 사람–로봇 협업(f16), 5G·클라우드 두뇌는 42. 분산 시스템·통신·컴퓨팅 구조(f3·f7), 실험 계획 루프는 46. 예측·학습 기반 최적화(f13), 농업기계 안전은 50. 안전 표준·인증·사고 조사(f18)와 연결된다. 공항 안내는 64. 상업 시설(f10), 실외 농지·건설은 66. 실외(f16·f5), 벤더 동향은 1. 기술·시장·업체 동향(f4)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-997",
        "ref-1004",
        "ref-1003",
        "ref-1001",
        "ref-1009",
        "ref-1000",
        "ref-999",
        "ref-1002",
        "ref-995",
        "ref-1008",
        "ref-1007",
        "ref-1005",
        "ref-1006",
        "ref-996",
        "ref-998"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "연결 관계는 이번 finding 들의 주제에서 도출한 것이다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-995",
      "org": "Offshore Technology (Eve Thomas)",
      "title": "Equinor's autonomous robotics: inspection 'dogs' and subsea drones",
      "published": "2025-11-21",
      "url": "https://www.offshore-technology.com/features/equinor-autonomous-robotics/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Equinor 의 ANYmal 'Roberta'(Northern Lights CCS 시설, 2024-11) 점검 운영과 수중 드론 Hydrone-R, 4D 과제 선정 기준, 비용 절감 추산을 다룬 기획 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-996",
      "org": "Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583)",
      "title": "A mobile robotic chemist",
      "published": "2020-07",
      "url": "https://www.nature.com/articles/s41586-020-2442-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 이동 매니퓰레이터가 개조하지 않은 실험실에서 8일간 688회 실험을 자율 수행해 광촉매를 탐색한 연구(검색 결과 요약 기준).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-997",
      "org": "이코노미스트 (송재민)",
      "title": "로봇이 로봇들을 움직이는, 네이버 1784",
      "published": "2023-01-11",
      "url": "https://economist.co.kr/article/view/ecn202301110006",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "네이버 1784 사옥의 로봇 약 100대, 브레인리스 로봇 루키, ARC·5G 특화망, 로보포트, 배달 시간 변화를 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-998",
      "org": "로봇신문 (정원영)",
      "title": "인천국제공항, 안내 로봇 '에어스타' 본격 운영",
      "published": "2018-07-11",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=14422",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "인천공항 안내 로봇 에어스타 14대의 운영 개시(2018-07-21), 제작사, 안내·에스코트·금지물품 회수 기능을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-999",
      "org": "서울신문",
      "title": "로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리",
      "published": "2022-11-15",
      "url": "https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "현대건설의 스팟 건설 현장 투입과 사진 기록 자동화·3D 스캔·QR 자재 추적·위험 구역 경보 기능, 2023년 시범 운영 계획을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1000",
      "org": "인더스트리뉴스",
      "title": "GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입",
      "published": null,
      "url": "https://www.industrynews.co.kr/news/articleView.html?idxno=38911",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GS건설이 2020-07 큐픽스와 스팟을 도입해 수집 데이터를 3차원 BIM 과 통합하고 간섭 확인·안전관리에 쓴 실증을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1001",
      "org": "SiLA Consortium",
      "title": "SiLA Standards",
      "published": null,
      "url": "https://sila-standard.com/standards/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "실험실 자동화 통신 표준 SiLA 2 의 Feature·Command·Property 구조, 자동 탐색, gRPC 기반 통신, 1.1 판, 작업반을 소개하는 공식 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1002",
      "org": "아주경제 (윤선훈)",
      "title": "아시아 최대 규모 데이터센터…네이버 '각 세종'",
      "published": "2023-11-08",
      "url": "https://www.ajunews.com/view/20231107091520837",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "네이버 각 세종 데이터센터의 서버 관리 로봇 세로와 운반 로봇 가로의 협업, ARC·ARM 연동을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1003",
      "org": "Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고",
      "title": "Game-changer: The rationale behind the investment in Energy Robotics",
      "published": "2021-01-15",
      "url": "https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "하드웨어 독립 로봇 운영 소프트웨어·클라우드 플릿 관리·AI 분석을 내세운 산업 점검 플랫폼 투자 사유 글. 기능 주장은 벤더 주장이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.korial.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics",
      "source_unopened": false
    },
    {
      "id": "ref-1004",
      "org": "The Robot Report",
      "title": "Singapore's National Robotics Programme reveals initiatives to advance robot adoption",
      "published": "2025-10-29",
      "url": "https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "싱가포르 국가 로봇 프로그램의 RMF(Open-RMF) 출범·창이 공항 운영, SS 713·TR 130 표준, ELEVATE 시험장을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1005",
      "org": "헬로디디",
      "title": "스스로 수확하고 운반···'로봇농부' 나왔다",
      "published": null,
      "url": "https://www.hellodd.com/news/articleView.html?idxno=99827",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한국기계연구원의 원예작물 수확 로봇·이송 로봇 다수 로봇 시스템과 발표 성능을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1006",
      "org": "농민신문 (조영창)",
      "title": "농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고",
      "published": "2024-03-25",
      "url": "https://www.nongmin.com/article/20240322500556",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "농촌진흥청 스마트팜 작업자 추종 운반 로봇의 사양, 바코드 유도선 주행, 2024년 시범사업 규모와 개선 과제를 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1007",
      "org": "뉴스토마토 (이규하)",
      "title": "방제·운반·점검 '농업 로봇' 하나로 연결…통합 관리 기술 개발",
      "published": "2025-04-23",
      "url": "https://www.newstomato.com/ReadNews.aspx?no=1259970",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "농촌진흥청이 방제·운반·모니터링 로봇 3종을 한 프로그램으로 관리하는 통합 관리 기술을 개발했다는 보도자료 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1008",
      "org": "넷매니아즈 (손장우)",
      "title": "한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리",
      "published": "2023-09-30",
      "url": "https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한전 신중부 변전소 5G 특화망 실증(2022-12)의 IoT 예방진단, 4족 로봇 순시점검 항목, CCTV 안전관리를 한전 자료를 바탕으로 정리한 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1009",
      "org": "ISO",
      "title": "ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones",
      "published": "2024",
      "url": "https://www.iso.org/standard/82687.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 부분 자동·반자율·자율 농업기계 안전 표준 2024년 판의 3부(자율 운용 구역). 1~4부 구성은 검색 결과 요약 기준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/other-sites.md",
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
      "rationale": "섹션 3: f1(정상 무인 시설 점검), f3(노후 변전소 점검), f20(현장별 차이) / 섹션 4: SiLA 2(f14), 브레인리스 로봇(f7), 정상 무인 시설(f1), 자율 운용 구역(f18), 자율 실험실(f13) / 섹션 5(현장 유형 모두 기타): 점검·순찰 — f1·f2(Equinor, f2 는 운영사 추산), f3(한전 변전소); 건설 — f5(현대건설), f6(GS건설 BIM 통합); 농업 — f15(농촌진흥청 통합 관리), f16(작업자 추종 운반), f17(한국기계연구원, 연구기관 발표 수치); 공공시설 — f10(인천공항 에어스타), f11(창이 공항 Open-RMF); 오피스 — f7·f8(네이버 1784, f8 벤더 주장); 데이터센터 — f9(각 세종); 연구실 — f13; 작업 형태 f19, 여섯 항목 f21(완료·인계 확인 기준 근거 부족 명시) / 섹션 6: 점검 데이터 수집·AI 분석 f1·f3, BIM 대조 f6, 작업자 추종·유도선 f16, 클라우드 두뇌·5G f7, 통합 관리 프로그램 f15, 이기종 플랫폼 f4(벤더 주장) / 섹션 7: ISO 18497 f18(원문 미열람), SiLA 2 f14, SS 713·TR 130 f12, Open-RMF f11 / 섹션 8: f13(Nature 2020) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66 / 섹션 11: open_questions_new 5건. f4·f8 은 벤더 주장 병기 필수. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f7·f12 반영, 21. 상호운용 표준·적합성 페이지에 f12·f14 반영, 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "SiLA 2",
      "term_en": "Standardization in Lab Automation 2 (SiLA 2)",
      "definition": "SiLA 컨소시엄이 관리하는 실험실 장비 통신 표준으로, 장비를 서버로 보고 그 능력을 Command·Property 를 담은 Feature 로 기술하며 자동 탐색과 gRPC 통신을 규정한다."
    },
    {
      "term_ko": "브레인리스 로봇",
      "term_en": "Brainless Robot",
      "definition": "인식·판단 같은 연산을 로봇 본체가 아닌 클라우드에 두고 저지연 네트워크(5G 등)로 제어받는 로봇으로, 네이버 1784 의 배달 로봇 루키가 예다."
    },
    {
      "term_ko": "정상 무인 시설",
      "term_en": "Not Normally Manned (NNM) Facility",
      "definition": "평소 사람이 상주하지 않도록 설계한 플랜트·해상 설비로, 원격 감시와 점검 로봇으로 불필요한 현장 출동을 줄이는 운영 방식을 전제로 한다."
    },
    {
      "term_ko": "자율 실험실",
      "term_en": "Self-driving Laboratory (Autonomous Laboratory)",
      "definition": "로봇이 실험을 수행하고 알고리즘이 결과를 보고 다음 실험을 고르는 과정을 사람 개입 없이 반복하는 실험실로, 이동 로봇이 일반 실험실 장비를 다루는 형태도 포함한다."
    }
  ],
  "open_questions_new": [
    "싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? | 관련 영역: 67. 기타 현장, 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반",
    "농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? | 관련 영역: 67. 기타 현장, 20. 로봇·제조사 관제 연동 | 근거: f15 | 종류: 일반",
    "건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? | 관련 영역: 67. 기타 현장, 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리 | 근거: f6 | 종류: 일반",
    "플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? | 관련 영역: 67. 기타 현장, 23. 업무 시스템 연동, 38. 모니터링·이상 탐지·원인 분석 | 근거: f3 | 종류: 일반",
    "SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? | 관련 영역: 67. 기타 현장, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f14 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f2 Equinor 비용 절감 추산은 운영사 추산이며 산정 근거 미확인",
      "f3 한전 변전소 실증은 넷매니아즈 정리본 기준, 한전 원자료 미열람",
      "f4 Korial(구 Energy Robotics)의 20개 이상 플랫폼 제어는 벤더 주장이며 독립 확인 없음",
      "f6 인더스트리뉴스 기사 발행일 미확인",
      "f8 네이버 배달 시간 단축은 벤더 주장이며 측정 조건 미확인",
      "f11 창이 공항 Open-RMF 운영 규모(로봇 대수·제조사 수)는 미확인 — 창이 공항 매거진 페이지는 본문이 렌더링되지 않아 열지 못함",
      "f12 SS 713·TR 130 표준 원문 미열람",
      "f13 Nature 논문은 저장소 PDF 본문 추출 실패로 검색 결과 요약 범위만 사용(원문 미열람)",
      "f15 농촌진흥청 보도자료 원문(korea.kr·rda.go.kr)은 연결 재설정으로 열지 못해 뉴스토마토 기사 기준",
      "f17 한국기계연구원 성능 수치의 시험 조건과 기사 발행일 미확인",
      "f18 ISO 18497-3 원문 미열람(ISO 페이지 403)",
      "Ju 외(2022) 농업 다중 로봇 리뷰는 ScienceDirect·ADS 접근 실패로 넣지 않음",
      "완료·인계 확인 기준(점검 결과 승인 주체 등)은 어느 사례에서도 확인되지 않음"
    ],
    "scope_violations": [
      "f1·f5·f13: SLAM·가스 감지·계단 보행·장비 조작은 분류 원문 19장의 로봇 자체 지능·제어이므로 사례 설명으로만 쓰고 f23 에서 '연계 대상: '으로 구분함",
      "f7·f12·f14: 승강기·자동문·5G 망·실험 장비는 시설·설비 제어이므로 ROP 는 요청·예약·상태 확인만 맡는 것으로 제안함",
      "f18: 농업기계 안전 표준은 업종별 조건이므로 운행 제약 근거로만 제안함",
      "f3·f1: 계기 판독·열화상 AI 분석을 로봇·플랫폼 어느 쪽이 맡는지는 사례마다 달라 직접 범위로 단정하지 않음"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유(스키마 불일치: f1·f6·f8·f15·f18 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음)에 대응함. 직전 반환값(runs/2026-09-30-02/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었다. 그래서 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었고, finding·출처 번호가 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-1003)만 근거로 한 finding 은 f4 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 회사 성능 주장 f8 도 같은 방식으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f4, f8). web_fetch_available: true · fetch_mode full. 사용량은 검색 16회/30, 신규 출처 15건/15(ref-995~ref-1009, 예약 구간 안)로, 출처 상한에 도달했다. 그래서 정책브리핑 농업로봇 기사(2025-03-10, 열었으나 통합 관리 프로그램 서술 없음), 한전KPS 정비 보조 로봇, LS일렉트릭 변압기 공장 순찰(제조 공장 사례), 역·지하철 사례, 해외 건설·농업 상용 사례는 넣지 못했다. 원문 열람은 13건이 webfetch 로 열렸고(ref-1003 은 korial.com 으로 리디렉션), 2건은 미열람(ref-996 PDF 추출 실패, ref-1009 ISO 403)이다. 교차 확인 0건, 신뢰도 high finding 없음. 분류 원문 핵심 질문(점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가)에는 작업 형태 f19, 현장별 차이 f20, 여섯 항목 f21, 직접 범위 f22, 연계 대상 f23 으로 답했다. 결론은 추정이다. 기타 현장은 점검 현장처럼 정보가 작업 대상이거나, 건설처럼 공간이 매일 바뀌거나, 농업처럼 비정형 지면·계절성이 있거나, 오피스·데이터센터처럼 건물 인프라에 기대는 점에서 다르다. 국내 사례는 대부분 한 기관이 자체 로봇을 자체 계층으로 묶은 형태다. 현장 유형은 f4·f14·f24 를 빼고 모두 기타다. 국내 자료는 이코노미스트·로봇신문·서울신문·인더스트리뉴스·아주경제·헬로디디·농민신문·뉴스토마토·넷매니아즈 아홉 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련(계기 판독·열화상 분석, 베이지안 실험 계획)은 45. 문서·도면·장면 이해·46. 예측·학습 기반 최적화와 적용 대상 38. 모니터링·이상 탐지·원인 분석에 함께 연결했다. 입력 누락은 없고 정정 요청·우선 지정 질문도 없다. 이 영역에 걸린 기존 열린 질문은 없으며 해결된 열린 질문도 없다."
  }
}
```

### runs/2026-09-30-02/verification.json

```json
{
  "run_id": "2026-09-30-02",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-995 열람 확인(Eve Thomas, 2025-11-21. 원제목 끝에 'and record-holding subsea drones'가 더 붙음). 2024-11 Northern Lights 배치, 계기·밸브 판독(20배 줌), CO2 농도 감시·경보, 누출 탐지, 운영자의 자체 임무 작성은 원문과 일치. 다만 원문은 시설을 'will eventually be unmanned'(장차 무인화될 예정)로 적어, '평소 사람이 상주하지 않도록 설계된'은 과장이므로 문구 수정을 조건으로 유지한다. evidence_excerpt의 영어 인용문은 원문 문장과 달라 직접 인용으로 쓰면 안 된다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-995 확인: 원문은 'broad implementation of robots and drones'에 대해 연간 Nkr1bn(9,910만 달러)을 넘는 절감을 추산한다. 주장에서 '드론'이 빠졌으므로 '로봇·드론'으로 고친다. 운영사 추산이므로 [추정] 유지."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1008 열람 확인(손장우, 2023-09-30, 원출처 한전 2022-12-20 자료). 계기·LED·밸브·램프·열화상 촬영, FHD 30fps 스트리밍, AI 영상 분석을 통한 추락·쓰러짐·위험지역 접근·화재·침입 탐지, 20년 넘은 설비 50% 이상이 원문과 일치. 한전 원자료는 미열람이며 2차 정리본이 근거다. 단일 출처."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1003 열람 확인(korial.com 리디렉션, Andre Retterath, 2021-01-15). 20개 이상 하드웨어 플랫폼, 200개 이상 소프트웨어 구성 요소, 하드웨어 독립 운영 소프트웨어·클라우드 플릿 관리·AI 분석, Spot·ExR-1이 원문에 있다. 사명 변경 안내는 페이지 머리에 있다. 벤더 주장 [추정]과 vendor_claim 표시 적정. 기준일이 2021-01-15로 오래되었으므로 본문에 기준일을 밝혀야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-999 열람 확인(서울신문, 2022-11-15). 다섯 기능, 2023년 김포·파주 고속국도 현장 시범 적용 계획, 공동주택 현장의 하루 최대 2만여 회 사진 비교가 원문과 일치. 단일 출처."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1000 열람 확인. 발행일은 2020-07-13(정형우 기자)이다. 브리프에는 '미확인'과 as_of 2026-09-30으로 되어 있어 고쳐야 한다. 이달 초 실증시험 진행, 3차원 BIM 통합으로 전기·설비 공사 간섭 확인과 안전관리계획 수립에 '활용하는 데 성공'했다는 문장이 원문에 있다. 하자 검토·교량 현장 활용은 원문에서 '예정'으로 적었다. 기사 원제목은 '…도입하기로'로 끝난다. 단일 출처."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-997 열람 확인(송재민, 2023-01-11). 원문은 '루키'가 40대에서 100여 대로 늘었다고 적는다. 주장의 '로봇이 …약 100대로'는 루키 대수로 고친다. 원문은 ARC를 네이버 클라우드 기반 '멀티 로봇 인텔리전스 시스템'으로 설명하고, 5G 클라우드 연결로 제작비를 낮춘다는 설명과 로보포트 이동·충전소 복귀를 적는다. 단일 출처."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-997 확인: 2022년 4월 서비스를 시작할 때 평균 15~17분이던 배달 시간이 기사 시점에 5~10분이 되었다는 서술이 있다. 회사 설명이므로 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1002 열람 확인(윤선훈, 2023-11-08. 원제목 끝에 '본격 가동'). 세로·가로를 통한 자산 흐름 실시간 추적, ARC·ARM(Adaptive Robot Management) 시스템 연동, GPS가 닿지 않는 곳의 위치·경로 처리가 원문과 일치. 단일 출처."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-998 열람 확인(정원영, 2018-07-11). 7월 21일 정식 운영, 제1·제2여객터미널 8대·6대, 푸른기술·LG CNS 컨소시엄, 체크인 카운터 안내·에스코트·한영중일 음성·금지물품 회수·기념사진이 원문과 일치. 2018년 자료이므로 현재 운영 여부는 확인하지 않았다(기준일 명시 필요)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1004 열람 확인(The Robot Report Staff, 2025-10-29). 2018년 ROS 기반 RMF 개발, 제조사가 다른 로봇의 협업, Open-RMF로 발전, 창이 공항 배치가 원문에 있다. 원문은 창이 공항에서 '청소 로봇'이 시설 관리 시스템의 일부로 운영된다고 적을 뿐, 여러 제조사 로봇을 묶었는지나 대수는 적지 않는다. 단일 출처."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1004 확인: SS 713·TR 130의 표제, SS 713의 ISO 격상 추진, BCA Braddell 캠퍼스 ELEVATE 시험장이 원문과 일치. 표준 원문(싱가포르 표준 기관 자료)은 미열람이며 기사가 근거다. 본문에서는 '기사에 따르면'으로 밝힌다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-996은 Nature 페이지가 로그인 리디렉션으로 열리지 않았다. 검색 결과(Nature 583, 237–241쪽, 2020)로 8일, 688회, 10개 변수, 배치 베이지안 탐색, 6배 활성, 기기가 아닌 연구자를 자동화한다는 설명을 확인했다. Strathclyde 저장소 PDF는 추출이 불완전했지만 사람 팔 수준의 도달 거리와 기존 실험실을 개조하지 않은 운영을 가리켰다. 원문 미열람 취급을 유지하고 medium 상한을 둔다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1001 열람 확인(SiLA Consortium, 발행일 없음). SiLA 서버·Feature·자동 탐색, gRPC(HTTP/2·Protocol Buffers), 1.1 판의 서버 주도 연결(클라우드 연결), SiLA Robotics & mobile Robotics 작업반(Greifswald 대학 Mark Doerr)이 원문과 일치. 원문은 명세를 'Core와 Mapping 두 부분'으로 설명하므로, 발췌의 'Core·Mapping·Features 세 부분'은 본문에 쓰지 않는다. '오케스트레이션은 범위 밖'은 Camunda를 외부 구현 예로 든 데서 나온 해석이므로 단정하지 않는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1007 열람 확인(이규하, 2025-04-23. 원제목은 '…통합관리기술 가동'). 로봇 3종(2022·2023·2024년 개발), PC·휴대전화 관리, 위치·속도·이동 거리와 운영 통계, 작업 순서 설정, 열매 수량·위치·익은 정도, 방제 횟수·수확 시기 조절, SIL 2등급 제어기가 원문과 일치. 단일 출처(농촌진흥청 보도자료 원문은 미열람)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1006 열람 확인(조영창, 2024-03-25. 원제목은 '…옮기고 자동 하역'). AI 분석 제어기와 3차원 카메라, 10cm~1m 간격, 300kg, 10시간, 바코드 유도선, 8개 지역 10개 농가, 느린 속도와 스티커 유도선이 벗겨지는 문제가 원문과 일치. 원문은 시범사업을 '진행한다'(계획)로 적으므로 '진행했고'는 '진행할 계획이었다'로 고친다. 검색 결과에 다른 매체의 같은 사양(0.1~1m, 300kg, 10시간)이 보였지만 출처를 특정하지 못해 교차 확인으로 세지 않았다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1005 열람 확인. 발행일은 2023-03-09(이유진 기자)다. 브리프의 '미확인'과 as_of 2026-09-30은 고친다. 수확 로봇·이송 로봇 구성, 인식률 90% 이상, 24시간 동작 가정 시 사람의 80% 효율은 원문과 일치한다. 원문의 공동 참여 기관은 하다·국립농업과학원·충북대·충남대로, 발췌의 '국립농산물품질관리원'은 틀렸다. 연구기관 발표 수치이므로 [추정] 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1009(ISO 페이지)은 403으로 열리지 않았다. 검색 결과(ISO·BSI·SCC·iTeh 목록)로 ISO 18497-3:2024 '자율 운용 구역'(2024-07 발행), 18497-2:2024 장애물 보호 시스템, 18497-1:2024·18497-4:2024의 존재를 확인했다. 1부·4부의 세부 범위(설계 원칙·용어, 검증 방법·타당성 확인 원칙)는 검색 결과 요약 범위를 넘어 확인하지 못했다. 원문 미열람, medium 상한."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 해석이며 각 형태의 근거 finding은 위에서 확인했다. 형태마다 단일 출처 사례라는 한계를 본문에 밝힌다. [추정] 유지."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 해석이다. '농업은 비정형 지면과 계절성 때문에'라는 이유는 인용한 f15·f16 어디에도 없으므로 삭제하는 것을 조건으로 유지한다. 원문은 '운영자가 자체 임무를 만든다'는 운영 사실만 뒷받침하고, 점검 현장을 '사람이 상주하지 않는' 곳으로 부르는 표현은 f1 수정에 맞춰 '무인화 예정·위험 설비'로 고친다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 해석이다. 제약의 '방폭'(ref-995 원문은 IP67 방수·방진만 적음)과 예외·성과의 '출동 감소'는 어느 finding에도 근거가 없으므로 삭제하는 것을 조건으로 유지한다. 완료·인계 기준 근거가 부족하다는 명시는 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "19장 경계 표를 대입한 해석으로 범위 경계에 맞다. 다만 ref-1004는 창이 공항에서 RMF가 청소 로봇 운영에 쓰인다고만 적고 여러 제조사를 묶었는지는 적지 않는다. '제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 창이 공항의 Open-RMF'를 '창이 공항에서 RMF가 청소 로봇 운영에 쓰인다는 기사 수준'으로 고치는 것을 조건으로 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상:'으로 표시되어 있고 19장의 네 경계에 맞게 나눴다. 해석이므로 [추정] 유지. 'BIM 저작 도구'와 '설비 보전 시스템'은 사례 출처에 없는 일반 범주이므로 예시로만 쓴다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 관계 해석이다. 번호와 이름을 함께 썼고 부록 A 명칭과 일치한다. L. AI·학습 기술(45·46)과 적용 대상(38)을 양쪽에 연결했다. [추정] 유지."
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
      "f11·Open-RMF 일반 설명: 기존 참고문헌 ref-004(Open-RMF)와 용어집 open-rmf가 있다. Open-RMF 자체를 소개하는 문장은 ref-004를 재사용하고, ref-1004는 싱가포르 출범·창이 공항 사례에만 쓴다",
      "f6 BIM 대조: 용어집 building-information-modeling·scan-vs-bim과 연결한다(새 용어 등록 없음)",
      "f3·f7 5G 특화망: 용어집 private-5g-network(5G 특화망(이음5G))와 같은 뜻이다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "용어 후보 '정상 무인 시설 (Not Normally Manned (NNM) Facility)': 근거 출처 ref-995는 이 용어를 쓰지 않고 시설을 'will eventually be unmanned'로만 적는다. 근거 없는 용어이므로 등록하지 않는다",
      "'5G 특화망'은 용어집 표기 '5G 특화망(이음5G)'에 맞추고 첫 등장 시 용어집에 링크한다"
    ]
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "f1 evidence_excerpt의 영어 인용 'Operators have begun creating their own missions without R&D support'는 ref-995 원문 문장('The operators have started using it themselves and creating missions on their own, without the research and development team there')과 다르다. 페이지에는 직접 인용으로 싣지 말고 한국어로 재서술한다"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f1: '평소 사람이 상주하지 않도록 설계된 … 시설'을 '장차 무인화될 예정인 … 시설'로 고친다 — ref-995 원문은 'will eventually be unmanned'로 적는다. 운영자 발언은 직접 인용하지 말고 재서술한다(브리프 발췌가 원문과 다르다).",
    "용어 후보 '정상 무인 시설(NNM)': glossary_updates에 넣지 않고 4절에서도 이 용어를 정의하지 않는다 — 근거 출처에 이 용어가 없다.",
    "f2: '로봇을 폭넓게 도입하면'을 '로봇과 드론을 폭넓게 도입하면'으로 고친다 — 원문 추산의 대상은 로봇·드론이다. [추정]과 '운영사 추산' 표시는 유지한다.",
    "ref-1000(f6): 각주와 reference_updates의 발행일을 2020-07-13으로, 기관을 '인더스트리뉴스 (정형우)'로 적고, f6의 기준일을 2020-07-13으로 쓴다. 하자 검토·교량 현장 활용은 '예정'으로 서술한다.",
    "ref-1005(f17): 각주와 reference_updates의 발행일을 2023-03-09로, 기관을 '헬로디디 (이유진)'로 적고 f17 기준일을 2023-03-09로 쓴다. 공동 연구 기관을 적는다면 '국립농산물품질관리원'이 아니라 하다·국립농업과학원·충북대·충남대로 쓴다.",
    "f7: '로봇이 초기 40대에서 약 100대로 늘었고'를 '배달 로봇 루키가 초기 40대에서 100여 대로 늘었고'로 고친다 — 원문 대수는 루키에 대한 것이다.",
    "f16: '2024년에는 … 시범사업을 진행했고'를 '2024년 … 시범사업을 진행할 계획이었고(2024-03 기준)'로 고친다 — 원문은 계획 시제다.",
    "f20: '농업은 비정형 지면과 계절성 때문에'에서 이유 부분을 삭제하고 '농업은 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다(f15·f16)'로만 쓴다 — 인용 finding에 그 이유가 없다. 점검 현장의 설명도 f1 수정에 맞춘다.",
    "f21: 제약 목록의 '방폭'과 예외·성과 목록의 '출동 감소'를 삭제한다 — 어느 finding에도 근거가 없다(ref-995는 IP67만 적는다).",
    "f22: '제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 창이 공항의 Open-RMF(f11)와 벤더 주장(f4) 수준에서만 확인됐다'를 '제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. 창이 공항에서 RMF가 청소 로봇 운영에 쓰인다는 기사(f11)와 벤더 주장(f4)이 있을 뿐이다'로 고친다 — ref-1004는 창이 공항의 다제조사 운영을 적지 않는다.",
    "f14: SiLA 2 명세를 'Core와 Mapping 두 부분'으로 쓰고 'Features 세 부분'은 쓰지 않는다. '워크플로 오케스트레이션은 표준 범위 밖'은 [추정]으로 낮춰 쓰거나 'Camunda 같은 외부 구현이 예로 언급된다'로만 쓴다 — 원문은 범위 밖이라고 명시하지 않는다.",
    "f18: ISO 18497 1부·4부의 세부 범위는 '검색 결과 요약 기준'임을 밝히고, 3부(자율 운용 구역, 2024-07 발행)와 2부(장애물 보호 시스템)만 이름을 단정해 쓴다.",
    "ref-996·ref-1009: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 두 항목에 source_unopened: true를 넣는다.",
    "f12: 7절에서 SS 713·TR 130은 'The Robot Report 기사에 따르면'으로 서술하고 표준 원문을 열지 않았음을 밝힌다.",
    "f4·f8: 본문에서 [추정]에 '벤더 주장'을 병기하고, f4의 기준일(2021-01-15)을 밝힌다. f17은 '연구기관 발표 수치'임을 병기한다.",
    "Open-RMF 일반 설명(7절): 기존 각주 ref-004를 재사용하고, ref-1004는 싱가포르 출범 경위·창이 공항·SS 713·TR 130에만 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 0건. 강등: 없음. 다만 f1·f2·f7·f16·f20·f21·f22의 과장·근거 없는 문구는 수정을 조건으로 유지했고, 용어 후보 '정상 무인 시설'은 근거가 없어 등록하지 않았다. 원문 미열람 출처: ref-996(Nature 로그인 리디렉션. 검색 결과와 저장소 PDF 일부로 확인), ref-1009(ISO 403. 검색 결과 목록으로 확인). 발행일 정정: ref-1000 2020-07-13, ref-1005 2023-03-09. 주의: 모든 사례가 단일 출처이고 대부분 국내외 기사다. f4·f8은 벤더 주장, f2는 운영사 추산, f17은 연구기관 발표 수치다. 현장 간 차이(f20), 여섯 항목(f21), 책임 경계(f22·f23)는 이번 사례에서 도출한 해석(추정)이다. 제조사가 다른 로봇을 한 계층에서 묶은 운영 사례는 이번 조사에서 확인되지 않았다. 에어스타(2018)와 Energy Robotics(2021) 자료는 기준일이 오래되었다. 검증 검색 3회(리서치 16회와 합쳐 19/30). 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-02/pages.json

```json
{
  "run_id": "2026-09-30-02",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "확인한 67. 기타 현장의 로봇 작업은 점검·순찰, 건설, 농업, 공공시설, 오피스, 데이터센터, 연구실의 일곱 형태로 나타나며, 현장마다 작업 대상과 기대는 인프라가 다르다. [추정][^ref-995][^ref-1008]",
      "planned_findings": [
        "f19",
        "f20",
        "f3",
        "f22"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "5G 특화망(이음5G), 브레인리스 로봇, 스캔 대 BIM 비교, SiLA 2, 자율 실험실, 자율 운용 구역, Open-RMF 를 정리한다. [사실][^ref-997][^ref-1001]",
      "planned_findings": [
        "f3",
        "f7",
        "f6",
        "f14",
        "f13",
        "f18",
        "f11"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2800,
      "summary": "현장 유형 기타의 사례 네 가지(Equinor CCS 시설 점검, GS건설·현대건설 건설 현장 점검, 농촌진흥청 스마트팜 운반·통합 관리, 네이버 1784 사내 배달)를 여섯 항목으로 정리한다. [사실][^ref-995][^ref-1007]",
      "planned_findings": [
        "f1",
        "f2",
        "f5",
        "f6",
        "f15",
        "f16",
        "f17",
        "f7",
        "f8",
        "f9",
        "f21"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1400,
      "summary": "점검 데이터 수집·분석, 로봇 데이터와 BIM 대조, 작업자 추종·유도선 주행과 통합 관리, 클라우드 두뇌와 건물 인프라 연동, 사람 대상 안내, 하드웨어 독립 점검 플랫폼(벤더 주장)으로 나눠 정리한다. [추정][^ref-1008][^ref-1003]",
      "planned_findings": [
        "f1",
        "f3",
        "f6",
        "f15",
        "f16",
        "f7",
        "f9",
        "f10",
        "f4",
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1100,
      "summary": "ISO 18497(2024년 판), SiLA 2, 싱가포르 SS 713·TR 130(기사 기준, 원문 미열람), Open-RMF 를 표로 정리한다. [사실][^ref-1001][^ref-1004]",
      "planned_findings": [
        "f18",
        "f14",
        "f12",
        "f11"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "이동 로봇 화학자(Nature 2020), 싱가포르 국가 로봇 프로그램 기사, 한전 5G 특화망 실증 정리, SiLA 표준 페이지를 소개한다. [사실][^ref-996]",
      "planned_findings": [
        "f13",
        "f11",
        "f12",
        "f3",
        "f14"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1100,
      "summary": "ROP는 요청 배정·작업 순서·승강기와 자동문 연동 요청·결과 반환·운행 제약 반영을 맡고, 로봇 자체 기능·설비 제어·업무 시스템·업종별 요건은 연계 대상으로 둔다. [추정][^ref-995][^ref-1009]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "1·14·16·17·20·21·22·25·26·31·38·42·45·46·50·64·66번 영역과 연결한다. [추정][^ref-1004]",
      "planned_findings": [
        "f24"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "SS 713·TR 130 내용, 농촌진흥청 프로그램의 개방성, 건설 현장 지도와 BIM 동기화, 점검 결과의 보전 시스템 반환, SiLA 이동 로봇 작업반 결과물 다섯 질문을 올린다.",
      "planned_findings": []
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/other-sites.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 접근법 6가지, 표준 5건, 책임 경계, 연결 영역 17개, 열린 질문 5건. 2차 수정: 출처 5건 제목 정정, 9절 태그 추가, BIM·라이다·RMF 첫 등장 풀어 쓰기. 2차 재검증 수정: 9절 RMF 풀이를 Robotics Middleware Framework 로 정정"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"6. 대표 접근법과 기술\" 절(1,209자)을 옮겼다. 2차 수정: 출처 제목 정정(ref-995·1000·1002·1006·1007)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,102자)을 옮겼다. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,022자)을 옮겼다. 2차 수정: 20. 로봇·제조사 관제 연동 항목의 창이 공항 서술을 기사 수준으로 고치고 출처 제목 정정"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"4. 핵심 개념과 용어\" 절(903자)을 옮겼다. 2차 수정: ref-1000 제목 정정. ref-004 각주 줄은 참고문헌 페이지가 입력에 없어 이전 값을 유지했다(퍼블리셔 대조 요청)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"11. 열린 질문\" 절(866자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"3. 왜 중요한가\" 절(716자)을 옮겼다. 2차 수정: 출처 제목 정정(ref-995·1000·1002·1006·1007)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area67-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 67. 기타 현장 의 \"8. 대표 연구와 자료\" 절(629자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 67. 기타 현장 | 섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농촌진흥청 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 표준 5건(ISO 18497·SiLA 2·SS 713·TR 130·Open-RMF), 책임 경계, 연결 영역 17개, 열린 질문 5건. 1차 조건부 승인 수정 16건·2차 수정 5건(출처 제목 정정, 창이 공항 서술 완화, 태그 보완, 약어 풀어 쓰기, ref-004 각주는 대조 요청)·2차 재검증 수정 1건(RMF 풀이를 Robotics Middleware Framework 로 정정) 이행 | run 2026-09-30-02",
  "index_updates": {
    "home_recent": "2026-09-30 — 67. 기타 현장: 섹션 3~11 신규 작성. 점검·건설·농업·오피스 사례 4건을 여섯 항목으로 정리하고, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 확인되지 않았음을 밝혔다",
    "category_recent": "2026-09-30 — 67. 기타 현장: 섹션 3~11 신규 작성(seed → draft). 현장 유형 기타 사례 4건, 표준 5건(ISO 18497·SiLA 2·SS 713·TR 130·Open-RMF), 연결 영역 17개, 열린 질문 5건",
    "area_recent": "2026-09-30 — 67. 기타 현장: 섹션 3~11 신규 작성. Equinor CCS 시설 점검, GS건설·현대건설 건설 현장 점검, 농촌진흥청 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달 사례와 책임 경계를 정리했다"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "sila-2",
      "term_ko": "SiLA 2",
      "term_en": "Standardization in Lab Automation 2 (SiLA 2)",
      "definition": "SiLA 컨소시엄이 관리하는 실험실 장비 통신 표준으로, 장비를 서버로 보고 그 능력을 Command·Property 를 담은 Feature 로 기술하며 자동 탐색과 gRPC 통신을 규정한다.",
      "description": "명세는 Core 와 Mapping 두 부분으로 이뤄지고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했다. 워크플로 오케스트레이션은 Camunda 같은 외부 구현이 예로 언급된다.",
      "related_areas": [
        67,
        21
      ],
      "sources": [
        "ref-1001"
      ]
    },
    {
      "action": "new",
      "slug": "brainless-robot",
      "term_ko": "브레인리스 로봇",
      "term_en": "Brainless Robot",
      "definition": "인식·판단 같은 연산을 로봇 본체가 아닌 클라우드에 두고 저지연 네트워크(5G 등)로 제어받는 로봇으로, 네이버 1784 의 배달 로봇 루키가 예다.",
      "related_areas": [
        67,
        42
      ],
      "sources": [
        "ref-997"
      ]
    },
    {
      "action": "new",
      "slug": "self-driving-laboratory",
      "term_ko": "자율 실험실",
      "term_en": "Self-driving Laboratory (Autonomous Laboratory)",
      "definition": "로봇이 실험을 수행하고 알고리즘이 결과를 보고 다음 실험을 고르는 과정을 사람 개입 없이 반복하는 실험실로, 이동 로봇이 일반 실험실 장비를 다루는 형태도 포함한다.",
      "description": "Burger 외(Nature 583, 2020)는 이동 매니퓰레이터가 개조하지 않은 실험실에서 8일간 688회 실험을 자율 수행한 사례를 보고했다.",
      "related_areas": [
        67,
        46
      ],
      "sources": [
        "ref-996"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-995",
      "org": "Offshore Technology (Eve Thomas)",
      "title": "Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones",
      "published": "2025-11-21",
      "url": "https://www.offshore-technology.com/features/equinor-autonomous-robotics/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Equinor 의 ANYmal 'Roberta'(Northern Lights CCS 시설, 2024-11) 점검 운영과 수중 드론 Hydrone-R, 4D 과제 선정 기준, 로봇·드론 도입에 따른 비용 절감 추산을 다룬 기획 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-996",
      "org": "Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583)",
      "title": "A mobile robotic chemist",
      "published": "2020-07",
      "url": "https://www.nature.com/articles/s41586-020-2442-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 이동 매니퓰레이터가 개조하지 않은 실험실에서 8일간 688회 실험을 자율 수행해 광촉매를 탐색한 연구(검색 결과 요약 기준).",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-997",
      "org": "이코노미스트 (송재민)",
      "title": "로봇이 로봇들을 움직이는, 네이버 1784",
      "published": "2023-01-11",
      "url": "https://economist.co.kr/article/view/ecn202301110006",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "네이버 1784 사옥의 배달 로봇 루키(40대 → 100여 대), 브레인리스 로봇, ARC·5G 특화망, 로보포트, 배달 시간 변화(회사 설명)를 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-998",
      "org": "로봇신문 (정원영)",
      "title": "인천국제공항, 안내 로봇 '에어스타' 본격 운영",
      "published": "2018-07-11",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=14422",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "인천공항 안내 로봇 에어스타 14대의 운영 개시(2018-07-21), 제작사, 안내·에스코트·금지물품 회수 기능을 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-999",
      "org": "서울신문",
      "title": "로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리",
      "published": "2022-11-15",
      "url": "https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "현대건설의 스팟 건설 현장 투입과 사진 기록 자동화·3D 스캔·QR 자재 추적·위험 구역 경보 기능, 2023년 시범 운영 계획을 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1000",
      "org": "인더스트리뉴스 (정형우)",
      "title": "GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로",
      "published": "2020-07-13",
      "url": "https://www.industrynews.co.kr/news/articleView.html?idxno=38911",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GS건설이 2020-07 큐픽스와 스팟을 도입해 수집 데이터를 3차원 BIM 과 통합하고 간섭 확인·안전관리에 쓴 실증과, 하자 검토·교량 현장 활용 예정을 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1001",
      "org": "SiLA Consortium",
      "title": "SiLA Standards",
      "published": null,
      "url": "https://sila-standard.com/standards/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "실험실 자동화 통신 표준 SiLA 2 의 Feature·Command·Property 구조, 자동 탐색, gRPC 기반 통신, Core·Mapping 두 부분의 명세, 1.1 판, 작업반을 소개하는 공식 페이지.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1002",
      "org": "아주경제 (윤선훈)",
      "title": "아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동",
      "published": "2023-11-08",
      "url": "https://www.ajunews.com/view/20231107091520837",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "네이버 각 세종 데이터센터의 서버 관리 로봇 세로와 운반 로봇 가로의 협업, ARC·ARM 연동을 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1003",
      "org": "Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고",
      "title": "Game-changer: The rationale behind the investment in Energy Robotics",
      "published": "2021-01-15",
      "url": "https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "하드웨어 독립 로봇 운영 소프트웨어·클라우드 플릿 관리·AI 분석을 내세운 산업 점검 플랫폼 투자 사유 글. 기능 주장은 벤더 주장이다.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1004",
      "org": "The Robot Report",
      "title": "Singapore's National Robotics Programme reveals initiatives to advance robot adoption",
      "published": "2025-10-29",
      "url": "https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "싱가포르 국가 로봇 프로그램의 RMF(Robotics Middleware Framework, 현 Open-RMF) 출범·창이 공항 청소 로봇 운영, SS 713·TR 130 표준, ELEVATE 시험장을 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1005",
      "org": "헬로디디 (이유진)",
      "title": "스스로 수확하고 운반···'로봇농부' 나왔다",
      "published": "2023-03-09",
      "url": "https://www.hellodd.com/news/articleView.html?idxno=99827",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한국기계연구원의 원예작물 수확 로봇·이송 로봇 다수 로봇 시스템과 연구기관이 발표한 성능 수치를 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1006",
      "org": "농민신문 (조영창)",
      "title": "농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역",
      "published": "2024-03-25",
      "url": "https://www.nongmin.com/article/20240322500556",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "농촌진흥청 스마트팜 작업자 추종 운반 로봇의 사양, 바코드 유도선 주행, 2024년 시범사업 계획과 개선 과제를 다룬 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1007",
      "org": "뉴스토마토 (이규하)",
      "title": "방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동",
      "published": "2025-04-23",
      "url": "https://www.newstomato.com/ReadNews.aspx?no=1259970",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "농촌진흥청이 방제·운반·모니터링 로봇 3종을 한 프로그램으로 관리하는 통합 관리 기술을 개발했다는 보도자료 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1008",
      "org": "넷매니아즈 (손장우)",
      "title": "한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리",
      "published": "2023-09-30",
      "url": "https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "한전 신중부 변전소 5G 특화망 실증(2022-12)의 IoT 예방진단, 4족 로봇 순시점검 항목, CCTV 안전관리를 한전 자료를 바탕으로 정리한 글.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1009",
      "org": "ISO",
      "title": "ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones",
      "published": "2024",
      "url": "https://www.iso.org/standard/82687.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 부분 자동·반자율·자율 농업기계 안전 표준 2024년 판의 3부(자율 운용 구역, 2024-07 발행). 1부·4부의 범위는 검색 결과 요약 기준.",
      "cited_by": [
        "docs/categories/site-type-applications/other-sites.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가?",
      "areas": [
        67,
        22,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가?",
      "areas": [
        67,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가?",
      "areas": [
        67,
        14,
        16
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가?",
      "areas": [
        67,
        23,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가?",
      "areas": [
        67,
        21,
        5
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    },
    {
      "site_type": "기타",
      "item": "완료·인계",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시",
      "title": "67. 기타 현장"
    }
  ],
  "additional_research_requests": [
    "5절 완료·인계 칸: Equinor 점검 사례와 건설 현장 사례에서 점검 결과를 누가 확인·승인해야 작업이 끝난 것으로 보는지(승인 주체·기록 형식)가 브리프에 없어 '미확인'으로 두었다. 기타 현장 사례의 완료 확인 기준 조사가 필요하다.",
    "5절 시작 조건 칸: 건설 현장 점검과 네이버 1784 배달에서 작업을 발생시키는 요청 경로(점검 일정 시스템, 주문 앱 등)가 브리프에 없어 미확인으로 두었다.",
    "7절·9절: 창이 공항 Open-RMF 운영 규모(로봇 대수·제조사 수)와 다제조사 운영 여부가 미확인이다. 제조사가 다른 로봇을 한 계층에서 묶은 기타 현장의 공개 사례 조사가 필요하다.",
    "7절: SS 713·TR 130 표준 원문과 발행 기관, ISO 18497 1부·4부의 공식 범위(원문 미열람), 한전 변전소 실증 원자료(한전 2022-12-20 자료) 열람이 필요하다.",
    "6절 사람 대상 안내: 인천공항 에어스타(2018) 이후의 현재 운영 여부와 역·지하철 같은 공공시설 사례가 브리프에 없다(출처 상한으로 조사하지 못함).",
    "ref-004 각주(분리 페이지 s4·s7): docs/references/ref-004.md 의 '각주 형식' 줄을 그대로 복사해야 하나, 이번 재실행 입력에도 그 파일이 없어 이전 줄을 유지했다. pipeline/agent_runner.py 담당은 재실행 입력에 인용된 기존 참고문헌 페이지를 넣고, 넣지 못하면 퍼블리셔가 두 페이지의 ref-004 각주 정의와 s7 표 Open-RMF 행 출처 칸 기관명을 참고문헌 페이지 값으로 덮어써야 한다."
  ],
  "fixes_applied": [
    "f1 문구 수정 — 5절 첫 사례의 제약 칸과 서술, 3절에서 시설을 '장차 무인화될 예정인 시설'로 썼고, 운영자 발언은 직접 인용하지 않고 '연구개발 부서의 도움 없이 로봇을 직접 쓰며 스스로 임무를 만들기 시작했다'로 재서술했다.",
    "용어 후보 '정상 무인 시설(NNM)' 제외 — glossary_updates 에 넣지 않았고 4절에서도 정의하지 않았다.",
    "f2 문구 수정 — 5절 첫 사례 예외·성과 칸을 '로봇과 드론을 폭넓게 도입하면'으로 쓰고 [추정]과 '운영사 추산' 표시를 유지했다.",
    "ref-1000(f6) 정정 — 각주와 reference_updates 의 발행일을 2020-07-13, 기관을 '인더스트리뉴스 (정형우)'로 적었고, 본문 기준일을 2020-07 로 밝혔으며 하자 검토·교량 현장 활용은 '활용할 예정'으로 서술했다.",
    "ref-1005(f17) 정정 — 각주와 reference_updates 의 발행일을 2023-03-09, 기관을 '헬로디디 (이유진)'로 적고 본문에 '2023-03 보도'로 기준일을 밝혔다. 공동 연구 기관은 본문에 적지 않았다.",
    "f7 문구 수정 — 5절 네 번째 사례 수행 자원 칸에 '브레인리스 배달 로봇 루키(초기 40대에서 100여 대로 늘었다)'로 썼다.",
    "f16 시제 수정 — 5절 세 번째 사례 서술에 '2024년 8개 지역 10개 농가를 대상으로 시범사업을 진행할 계획이었다(2024-03 기준)'로 썼다.",
    "f20 수정 — 3절에서 농업의 이유(비정형 지면·계절성)를 빼고 '농업은 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다'로만 썼으며, 점검 현장은 '무인화 예정이거나 위험한 설비'로 고쳤다.",
    "f21 수정 — 5절 표와 본문 어디에도 '방폭'과 '출동 감소'를 쓰지 않았다(제약 칸에는 IP67 만 적었다).",
    "f22 수정 — 9절에 '제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. 창이 공항에서 RMF가 청소 로봇 운영에 쓰인다는 기사와 벤더 주장이 있을 뿐이다'로 썼다(본문에는 finding id 를 쓰지 않았다).",
    "f14 수정 — 7절에서 SiLA 2 명세를 'Core와 Mapping 두 부분'으로 썼고, 오케스트레이션은 'Camunda 같은 외부 구현이 예로 언급된다'로만 썼다. 4절 정의와 glossary_updates 에도 '세 부분'·'범위 밖' 표현을 넣지 않았다.",
    "f18 수정 — 7절에서 3부(자율 운용 구역, 2024-07 발행)와 2부(장애물 보호 시스템)만 이름을 단정했고, 1부·4부 범위는 '검색 결과 요약 기준으로만 확인했고 원문은 열지 못했다'고 밝혔다.",
    "ref-996·ref-1009 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 두 항목에 source_unopened: true 를 넣었다.",
    "f12 수정 — 7절 SS 713·TR 130 행을 'The Robot Report 기사(2025-10-29)에 따르면'·'같은 기사에 따르면'으로 서술하고 표준 원문을 열지 않았음을 밝혔다.",
    "f4·f8·f17 표시 — 6절 f4 문장에 '[추정] 벤더 주장'과 기준일 '2021-01-15 투자사 글 기준'을, 5절 f8 칸에 '[추정] 벤더 주장'을, 5절 f17 문장에 '[추정] 연구기관 발표 수치'를 병기했다.",
    "Open-RMF 각주 — 4절과 7절의 Open-RMF 일반 설명에는 기존 각주 ref-004 를 쓰고, ref-1004 는 싱가포르 출범 경위·창이 공항·SS 713·TR 130 서술에만 썼다.",
    "분량 초과 자동 분리: 67. 기타 현장 본문 10,489자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,402자",
    "2차: 출처 5건 제목 정정 — ref-995·ref-1000·ref-1002·ref-1006·ref-1007 의 제목을 지시된 원문 제목으로 바꿨다. 원 페이지 13절 각주, 분리 페이지 s3·s6·s10 의 각주(s4 는 ref-1000), reference_updates 의 title 을 모두 같게 고쳤다.",
    "2차: ref-004 각주 정의 — 이행 불가(대체 근거 없음): 이번 재실행 입력에도 docs/references/ref-004.md 가 없어 '각주 형식' 줄을 복사할 수 없었다. 추정 값을 새로 만들지 않고 이전 줄과 s7 표 출처 칸(Open Robotics — docs/standards/index.md 의 Open-RMF 발행 기관과 같음)을 그대로 두었으며, 퍼블리셔 덮어쓰기와 입력 추가를 additional_research_requests 에 요청했다.",
    "2차: 10절 20. 로봇·제조사 관제 연동 항목 — 분리 페이지 s10 에서 '창이 공항의 RMF 사례처럼 여러 로봇을 한 관제로 묶는 일'을 '창이 공항에서 RMF가 청소 로봇 운영에 쓰인다는 기사'로 고쳤다.",
    "2차: 9절 태그 보완 — 원 페이지 9절 마지막 단락의 '제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다.' 끝에 [추정][^ref-1004][^ref-1003] 을 붙였다.",
    "2차: 약어 풀어 쓰기 — 원 페이지 5절 GS건설 사례 완료·인계 칸의 첫 BIM 을 '건물 정보 모델링(Building Information Modeling, BIM)', 5절 Equinor 표 수행 자원 칸의 첫 라이다를 '라이다(Light Detection and Ranging, LiDAR)', 9절의 첫 RMF 를 풀어 썼다(RMF 풀이는 아래 재검증 항목으로 정정).",
    "2차(재검증): RMF 풀이 정정 — 원 페이지 9절 마지막 단락의 'RMF(Robot Middleware Framework, 현 Open-RMF)'를 'RMF(Robotics Middleware Framework, 현 Open-RMF)'로 고쳤다. 다른 곳은 바꾸지 않았다(reference_updates 의 ref-1004 요약에 같은 풀이를 함께 적었다)."
  ],
  "standards_updates": [
    {
      "name": "SiLA 2 (Standardization in Lab Automation 2)",
      "kind": "표준",
      "org": "SiLA Consortium",
      "url": "https://sila-standard.com/standards/",
      "related_areas": [
        67,
        21
      ],
      "summary": "실험실 장비를 SiLA 서버로 보고 능력을 Command·Property 를 담은 Feature 로 기술하는 실험실 자동화 통신 표준. 서버·Feature 자동 탐색과 gRPC 통신을 규정하고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했다.",
      "ref_id": "ref-1001"
    },
    {
      "name": "ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/82687.html",
      "related_areas": [
        67,
        50,
        21
      ],
      "summary": "자율 농업기계·트랙터 안전 표준 2024년 판(1~4부) 가운데 자율 운용 구역을 다루는 3부(2024-07 발행). 원문 미열람, 검색 결과 기준.",
      "ref_id": "ref-1009"
    },
    {
      "name": "SS 713 Data Exchange Between Robots, Lifts and Automated Doorways",
      "kind": "표준",
      "org": "싱가포르(발행 기관명 미확인, The Robot Report 보도 기준)",
      "url": "https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/",
      "related_areas": [
        67,
        22,
        21
      ],
      "summary": "기사에 따르면 로봇·승강기·자동문 사이 데이터 교환을 다루는 싱가포르 표준이며, 싱가포르가 ISO 국제표준으로 올리려 한다. 표준 원문 미열람.",
      "ref_id": "ref-1004"
    },
    {
      "name": "TR 130 Interoperability Between Robots and Central Command Systems",
      "kind": "표준",
      "org": "싱가포르(발행 기관명 미확인, The Robot Report 보도 기준)",
      "url": "https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/",
      "related_areas": [
        67,
        20,
        21
      ],
      "summary": "기사에 따르면 로봇과 중앙 관제 시스템의 상호운용을 다루는 싱가포르 기술 참조. 원문 미열람.",
      "ref_id": "ref-1004"
    }
  ]
}
```

### runs/2026-09-30-02/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-30-02/pages/categories/site-type-applications/other-sites.md

```markdown
---
title: "67. 기타 현장"
type: area
category: "Q. 현장 유형별 적용"
area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [점검·순찰 로봇, 건설 현장 BIM 대조, 농업 로봇 통합 관리, 브레인리스 로봇, SiLA 2, 자율 실험실]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-004, ref-995, ref-996, ref-997, ref-998, ref-999, ref-1000, ref-1001, ref-1002, ref-1003, ref-1004, ref-1005, ref-1006, ref-1007, ref-1008, ref-1009]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 67. 기타 현장

# 67. 기타 현장

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]

## 3. 왜 중요한가

이번 조사에서 확인한 67. 기타 현장의 로봇 작업은 플랜트·변전소 점검·순찰, 건설 현장 공정·품질·안전 점검, 농업의 방제·운반·모니터링·수확, 공항 같은 공공시설의 안내·청소, 오피스 빌딩 사내 배달, 데이터센터 서버 자산 운반·관리, 연구실 실험 수행의 일곱 형태로 나타나며, 형태마다 근거는 단일 출처 사례다. [추정][^ref-995][^ref-1008][^ref-999][^ref-1007][^ref-998][^ref-1004][^ref-997][^ref-1002][^ref-996]

자세한 내용은 주제 페이지 [67. 기타 현장 — 왜 중요한가](../../topics/2026/2026-09-30-area67-s3.md)에 있다.

## 4. 핵심 개념과 용어

**5G 특화망(이음5G)(Private 5G Network)** — [용어집](../../glossary/private-5g-network.md) 참조. 이번 사례에서는 한전 변전소 로봇의 점검 영상을 인공지능(AI) 서버로 보내는 통신과, 네이버 1784 배달 로봇을 클라우드에서 제어하는 통신에 쓰였다. [사실][^ref-1008][^ref-997]

자세한 내용은 주제 페이지 [67. 기타 현장 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area67-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 네 사례의 현장 유형은 모두 기타이며, 사례마다 근거는 단일 출처 보도다.

**현장 유형:** 기타

**사례:** 이산화탄소 포집·저장 시설에서 4족 로봇으로 계기·밸브·누출 점검 (Equinor, 노르웨이)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 현장 운영자가 직접 만든 점검 임무. [사실][^ref-995] |
| 작업 대상 | 계기 판독, 밸브 위치 확인, 이산화탄소 농도 감시, 누출 탐지 같은 설비 정보. [사실][^ref-995] |
| 수행 자원 | ANYbotics의 4족 로봇 ANYmal('Roberta'). 광학 줌·열화상·가스·음향 센서와 3D 라이다(Light Detection and Ranging, LiDAR)를 갖췄다. [사실][^ref-995] |
| 제약 | 장차 무인화될 예정인 시설에서 운영되며, 로봇은 IP67(방진·방수) 등급이다. [사실][^ref-995] |
| 완료·인계 | 점검 결과를 누가 확인·승인해야 끝났다고 보는지는 미확인. |
| 예외·성과 | Equinor는 로봇과 드론을 폭넓게 도입하면 연간 10억 노르웨이 크로네(약 9,910만 달러)를 넘는 비용을 절감할 것으로 추산한다. [추정] 운영사 추산[^ref-995] |

Equinor는 2024-11부터 장차 무인화될 예정인 노르웨이 Northern Lights 이산화탄소 포집·저장(Carbon Capture and Storage, CCS) 시설에 이 로봇을 배치했다. [사실][^ref-995] 2025-11 기사에 따르면 현장 운영자들은 연구개발 부서의 도움 없이 로봇을 직접 쓰며 스스로 임무를 만들기 시작했다. [사실][^ref-995] 비용 절감 추산의 산정 방법은 공개되지 않았다. [추정] 운영사 추산[^ref-995]

**현장 유형:** 기타

**사례:** 건설 현장에서 4족 로봇으로 공정·품질·안전 점검 데이터 수집 (GS건설·현대건설)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 점검을 발생시키는 요청·일정은 미확인. |
| 작업 대상 | 지하주차장 골조와 세대 내부 마감 같은 공사 공간(GS건설 실증), 현장 사진·환경 데이터와 QR 코드로 추적하는 자재(현대건설). [사실][^ref-1000][^ref-999] |
| 수행 자원 | 4족 보행 로봇 스팟과 그에 단 라이다·360도 카메라·사물인터넷(Internet of Things, IoT) 센서. 사무실의 담당자는 현장을 실시간으로 확인한다. [사실][^ref-1000][^ref-999] |
| 제약 | 계단·좁은 공간처럼 사람이 접근하기 어려운 곳을 다니고, 출입 제한 구역에서는 위험 경보를 낸다. [사실][^ref-999] |
| 완료·인계 | 로봇이 모은 데이터를 기존 3차원 건물 정보 모델링(Building Information Modeling, BIM) 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다. [사실][^ref-1000] |
| 예외·성과 | 현대건설은 공동주택 현장에서 하루 최대 2만여 장의 사진 비교가 필요하다고 설명했다. [사실][^ref-999] 로봇 도입의 성과 수치는 미확인. |

GS건설은 2020-07 큐픽스와 함께 스팟을 국내 건설 현장에 처음 도입해 성남 아파트 현장과 서울 공연장 신축 현장에서 실증했고, 입주 전 하자 품질 검토와 교량 공사 현장 공정·품질 점검에도 활용할 예정이라고 밝혔다. [사실][^ref-1000] 현대건설은 스팟으로 현장 사진 촬영·기록 자동화, 영상·환경 센서 실시간 모니터링, 레이저 스캐닝 3D 데이터 수집, QR 코드 기반 자재 추적, 출입 제한 구역 위험 경보를 하게 했고, 2023년 김포–파주 고속도로 현장에서 시범 운영할 계획이었다(2022-11 기준). [사실][^ref-999]

**현장 유형:** 기타

**사례:** 스마트팜에서 방제·운반·모니터링 로봇을 함께 운영하고 수확물을 집하장으로 운반 (농촌진흥청)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 통합 관리 프로그램에서 작업 순서를 설정하고, 작업·작물 정보로 방제 횟수와 수확 시기를 조절한다. [사실][^ref-1007] |
| 작업 대상 | 작물(모니터링 로봇 영상으로 본 수확 가능한 열매 수·위치·익은 정도)과 수확물. [사실][^ref-1007][^ref-1006] |
| 수행 자원 | 농촌진흥청이 개발한 방제 로봇(2022)·운반 로봇(2023)·모니터링 로봇(2024), 작업자를 따라가는 운반 로봇과 작업자. [사실][^ref-1007][^ref-1006] |
| 제약 | 운반 로봇은 3D 카메라로 작업자와 10cm~1m 간격을 유지하고, 최대 300kg을 싣고, 한 번 충전으로 10시간 운행하며, 바닥의 바코드 유도선을 따라 움직인다. [사실][^ref-1006] 통합 관리 기술에는 안전무결성 수준(Safety Integrity Level, SIL) 2등급 제어기가 적용됐다. [사실][^ref-1007] |
| 완료·인계 | 운반 로봇이 재배 현장과 집하장 사이를 자율로 오가며 수확물을 집하장으로 옮긴다. [사실][^ref-1006] |
| 예외·성과 | 로봇 속도가 느린 점과 바닥에 붙인 유도선이 벗겨지는 점이 개선 과제로 꼽혔다. [사실][^ref-1006] |

농촌진흥청의 통합 관리 프로그램(2025-04 보도)은 로봇 3종을 개인용 컴퓨터나 휴대전화 하나로 관리하며 로봇의 위치·속도·이동 거리와 운영 통계를 보여 준다. [사실][^ref-1007] 관리 대상은 농촌진흥청이 개발한 로봇이며, 다른 제조사 로봇의 연결 여부는 보도에 없다. [사실][^ref-1007] 작업자 추종 운반 로봇은 2024년 8개 지역 10개 농가를 대상으로 시범사업을 진행할 계획이었다(2024-03 기준). [사실][^ref-1006]

한국기계연구원은 온실에서 수확 로봇이 작물을 따고 이송 로봇이 수확물을 하역장까지 자율로 나르는 원예작물 수확 다수 로봇 시스템을 개발했으며, 연구진은 작물 인식률 90% 이상, 24시간 운영을 가정하면 사람의 80% 효율로 수확할 수 있다고 밝혔다(2023-03 보도). [추정] 연구기관 발표 수치[^ref-1005]

**현장 유형:** 기타

**사례:** 오피스 빌딩에서 클라우드 제어 로봇이 커피·택배를 자리까지 배달 (네이버 제2사옥 1784)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 커피·택배를 임직원 자리까지 보내는 배달. [사실][^ref-997] 요청이 들어오는 경로는 미확인. |
| 작업 대상 | 커피와 택배. [사실][^ref-997] |
| 수행 자원 | 브레인리스 배달 로봇 루키(초기 40대에서 100여 대로 늘었다), 이를 제어하는 네이버 클라우드 기반 멀티 로봇 시스템 ARC(AI·Robot·Cloud), 로봇 전용 엘리베이터 로보포트. [사실][^ref-997] |
| 제약 | 층간 이동은 로보포트에, 제어는 5G 특화망을 통한 클라우드 연결에 기댄다. [사실][^ref-997] |
| 완료·인계 | 루키는 자리까지 배달한 뒤 충전소로 돌아간다. [사실][^ref-997] 수령 확인 방식은 미확인. |
| 예외·성과 | 네이버는 2022-04 서비스 시작 때 평균 15~17분이던 배달 시간이 5~10분으로 줄었다고 밝혔다. [추정] 벤더 주장[^ref-997] |

네이버는 로봇을 5G로 클라우드에 연결하면 로봇 제작비를 줄일 수 있다고 설명한다. [추정] 벤더 주장[^ref-997] 같은 회사의 데이터센터 각 세종에서는 서버 관리 로봇 '세로'와 서버실·창고를 오가며 고중량 자산을 나르는 운반 로봇 '가로'가 협력해 자산 흐름을 실시간으로 추적·관리하고, 두 로봇은 ARC와 ARM(Adaptive Robot Management) 시스템을 통해 공간·서비스 인프라와 연동된다(2023-11 기준). [사실][^ref-1002]

## 6. 대표 접근법과 기술

67. 기타 현장의 사례에서 확인한 접근법은 점검 데이터 수집·분석, 로봇 데이터와 BIM 대조, 작업자 추종·유도선 주행과 통합 관리, 클라우드 두뇌와 건물 인프라 연동, 사람 대상 안내, 하드웨어 독립 점검 플랫폼으로 묶인다. [추정][^ref-1008][^ref-1000][^ref-1007][^ref-997][^ref-998][^ref-1003]

자세한 내용은 주제 페이지 [67. 기타 현장 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area67-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 절은 이번 조사에서 확인한 표준·프레임워크를 정리한다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [67. 기타 현장 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area67-s7.md)에 있다.

## 8. 대표 연구와 자료

Burger, B. 외, A mobile robotic chemist(Nature 583, 2020) — 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다. [사실][^ref-996] 저자들은 이를 장비가 아니라 연구자를 자동화하는 접근으로 설명한다. [사실][^ref-996]

자세한 내용은 주제 페이지 [67. 기타 현장 — 대표 연구와 자료](../../topics/2026/2026-09-30-area67-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 점검 일정·배달 주문·운반 요청을 받아 로봇에 배정하고 작업 순서를 정하며, 점검 영상·계기값·BIM 대조 결과 같은 작업 결과를 모아 요청한 시스템에 돌려준다. [추정][^ref-995][^ref-997][^ref-1007][^ref-1008][^ref-1000] | 연계 대상: 설비 보전·공정 관리 시스템, BIM 저작 도구 같은 업무 시스템(예시). [추정][^ref-1000] |
| 로봇 자체 지능·제어 | 로봇에 작업 요청을 걸고 상태를 확인한다. [추정][^ref-995] | 연계 대상: 동시적 위치 추정·지도 작성(Simultaneous Localization and Mapping, SLAM), 가스·음향 감지, 계단 보행, 파지. [추정][^ref-995][^ref-999][^ref-996] |
| 시설·설비 제어 | 승강기·자동문 연동을 요청하고 결과를 확인한다. [추정][^ref-997][^ref-1004] | 연계 대상: 승강기·자동문, 5G 특화망, 실험 분석 장비(SiLA 서버). [추정][^ref-997][^ref-1004][^ref-1001] |
| 업종별 조건 | 위험 구역·자율 운용 구역을 운행 제약으로 반영한다. [추정][^ref-999][^ref-1009] | 연계 대상: 농업기계 안전(ISO 18497)과 위험 시설 요건. [추정][^ref-1009] |

경계는 제품 전략에 따라 옮겨질 수 있지만([범위 경계](../../about/scope-boundary.md)), 이종 제조사를 잇는 ROP는 외부 영역에 작업 요청·예약·상태 확인만 걸고 주행·계측 성능과 설비 제어는 해당 제조사·설비 주체에 맡겨야 할 것으로 보인다. [추정][^ref-995][^ref-1004] 계기 판독 같은 AI 분석을 로봇 쪽과 플랫폼 쪽 가운데 어디에 둘지는 정해지지 않았다. [추정][^ref-995][^ref-1008]

확인한 국내 사례(네이버 ARC, 농촌진흥청 통합 관리 프로그램)는 한 기관이 만든 로봇을 자체 계층으로 묶은 것이다. [추정][^ref-997][^ref-1007] 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. [추정][^ref-1004][^ref-1003] 창이 공항에서 RMF(Robotics Middleware Framework, 현 Open-RMF)가 청소 로봇 운영에 쓰인다는 기사와 벤더 주장이 있을 뿐이다. [추정][^ref-1004][^ref-1003]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md) — 하드웨어 독립 산업 점검 플랫폼 같은 벤더 동향이 이어진다. [추정][^ref-1003] - [14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md) — 건설 현장 로봇 데이터를 BIM과 대조하는 일이 이어진다. [추정][^ref-1000]

자세한 내용은 주제 페이지 [67. 기타 현장 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area67-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 한국산업표준(KS)과는 어떻게 다른가? 관련: 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성

자세한 내용은 주제 페이지 [67. 기타 현장 — 열린 질문](../../topics/2026/2026-09-30-area67-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-09-30
[^ref-996]: Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583), A mobile robotic chemist, 2020-07, https://www.nature.com/articles/s41586-020-2442-2, 접근일 2026-09-30 (원문 미열람)
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-09-30
[^ref-998]: 로봇신문 (정원영), 인천국제공항, 안내 로봇 '에어스타' 본격 운영, 2018-07-11, https://www.irobotnews.com/news/articleView.html?idxno=14422, 접근일 2026-09-30
[^ref-999]: 서울신문, 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리, 2022-11-15, https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118, 접근일 2026-09-30
[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-09-30
[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1002]: 아주경제 (윤선훈), 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동, 2023-11-08, https://www.ajunews.com/view/20231107091520837, 접근일 2026-09-30
[^ref-1003]: Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고, Game-changer: The rationale behind the investment in Energy Robotics, 2021-01-15, https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics, 접근일 2026-09-30
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-09-30
[^ref-1005]: 헬로디디 (이유진), 스스로 수확하고 운반···'로봇농부' 나왔다, 2023-03-09, https://www.hellodd.com/news/articleView.html?idxno=99827, 접근일 2026-09-30
[^ref-1006]: 농민신문 (조영창), 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역, 2024-03-25, https://www.nongmin.com/article/20240322500556, 접근일 2026-09-30
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-1009]: ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones, 2024, https://www.iso.org/standard/82687.html, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/site-type-applications/other-sites.md

```markdown
---
title: "67. 기타 현장"
type: area
category: "Q. 현장 유형별 적용"
area_no: 67
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 67. 기타 현장

# 67. 기타 현장

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]

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

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s6.md

```markdown
---
title: "67. 기타 현장 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1000, ref-1002, ref-1003, ref-1006, ref-1007, ref-1008, ref-995, ref-997, ref-998]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#6
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 대표 접근법과 기술

# 67. 기타 현장 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 67. 기타 현장의 사례에서 확인한 접근법은 점검 데이터 수집·분석, 로봇 데이터와 BIM 대조, 작업자 추종·유도선 주행과 통합 관리, 클라우드 두뇌와 건물 인프라 연동, 사람 대상 안내, 하드웨어 독립 점검 플랫폼으로 묶인다. [추정][^ref-1008][^ref-1000][^ref-1007][^ref-997][^ref-998][^ref-1003]
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

67. 기타 현장의 사례에서 확인한 접근법은 점검 데이터 수집·분석, 로봇 데이터와 BIM 대조, 작업자 추종·유도선 주행과 통합 관리, 클라우드 두뇌와 건물 인프라 연동, 사람 대상 안내, 하드웨어 독립 점검 플랫폼으로 묶인다. [추정][^ref-1008][^ref-1000][^ref-1007][^ref-997][^ref-998][^ref-1003]

### 점검 데이터 수집과 분석

한전 신중부 변전소 실증(2022-12)에서는 5G 특화망을 구축하고 4족 로봇이 아날로그·디지털 계기와 LED·밸브·램프 상태를 촬영하고 열화상 영상을 모아 AI 서버로 스트리밍했으며, 무선 IoT 센서와 무선 폐쇄회로 텔레비전(CCTV)으로 추락·쓰러짐·위험지역 접근·화재·침입을 감지했다. [사실][^ref-1008] 분석 위치는 사례마다 달라, Equinor 사례는 센서를 로봇에 싣고 한전 사례는 영상을 AI 서버로 보내 분석한다. [추정][^ref-995][^ref-1008] 판정 결과가 설비 보전 기록으로 어떻게 넘어가는지는 미확인이다.

### 로봇 데이터와 BIM 대조

GS건설 실증(2020-07)은 로봇에 단 라이다·360도 카메라·IoT 센서로 모은 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다. [사실][^ref-1000] 날마다 바뀌는 현장에서 대조 주기와 방식은 확인하지 못했다.

### 작업자 추종·유도선 주행과 통합 관리

농업 운반 로봇은 3D 카메라로 작업자를 따라가는 방식과 바닥의 바코드 유도선을 따라 자율로 오가는 방식을 함께 쓴다. [사실][^ref-1006] 여러 로봇은 통합 관리 프로그램 하나에서 위치·통계를 보고 작업 순서를 정한다. [사실][^ref-1007] 유도선 내구성과 로봇 속도가 한계로 지적됐다. [사실][^ref-1006]

### 클라우드 두뇌와 건물 인프라 연동

네이버 1784는 두뇌를 클라우드에 둔 배달 로봇을 5G 특화망 기반 ARC로 제어하고 전용 엘리베이터로 층을 오가게 한다. [사실][^ref-997] 이 방식은 통신망과 전용 승강기 같은 건물 인프라가 갖춰진 곳을 전제로 한다. [추정][^ref-997][^ref-1002]

### 사람을 대상으로 한 안내

인천국제공항공사는 2018-07-21부터 푸른기술·LG CNS 컨소시엄이 만든 안내 로봇 에어스타를 제1여객터미널 8대·제2여객터미널 6대로 운영해 출국장·면세지역·입국장 수하물 수취 지역에서 항공편·체크인 카운터 안내, 목적지 에스코트, 4개 국어 음성 안내, 기내 반입 금지 물품 회수를 맡겼다. [사실][^ref-998] 2018년 자료이며 현재 운영 여부는 미확인이다.

### 하드웨어 독립 점검 플랫폼

Energy Robotics(2026-05 Korial로 사명 변경)는 하드웨어에 독립적인 로봇 운영 소프트웨어, 클라우드 기반 플릿 관리, AI 데이터 분석을 결합한 산업 점검 플랫폼을 내세우며, Boston Dynamics Spot·ExRobotics ExR-1을 포함한 20개가 넘는 하드웨어 플랫폼을 제어하도록 소프트웨어를 맞춰 왔다고 주장한다(2021-01-15 투자사 글 기준). [추정] 벤더 주장[^ref-1003]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-09-30
[^ref-1002]: 아주경제 (윤선훈), 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동, 2023-11-08, https://www.ajunews.com/view/20231107091520837, 접근일 2026-09-30
[^ref-1003]: Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고, Game-changer: The rationale behind the investment in Energy Robotics, 2021-01-15, https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics, 접근일 2026-09-30
[^ref-1006]: 농민신문 (조영창), 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역, 2024-03-25, https://www.nongmin.com/article/20240322500556, 접근일 2026-09-30
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-09-30
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-09-30
[^ref-998]: 로봇신문 (정원영), 인천국제공항, 안내 로봇 '에어스타' 본격 운영, 2018-07-11, https://www.irobotnews.com/news/articleView.html?idxno=14422, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s7.md

```markdown
---
title: "67. 기타 현장 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-1001, ref-1004, ref-1009]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#7
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 관련 표준·프레임워크·오픈소스

# 67. 기타 현장 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 절은 이번 조사에서 확인한 표준·프레임워크를 정리한다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 절은 이번 조사에서 확인한 표준·프레임워크를 정리한다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 18497(2024년 판) | 표준 | 부분 자동·반자율·자율 농업기계·트랙터의 안전을 다루며, 3부는 자율 운용 구역(2024-07 발행), 2부는 장애물 보호 시스템을 다룬다. 1부(설계 원칙·용어)와 4부(검증 방법·타당성 확인 원칙)의 범위는 검색 결과 요약 기준으로만 확인했고 원문은 열지 못했다. [사실][^ref-1009] | ISO(원문 미열람) |
| SiLA 2 | 표준 | 실험실 장비를 SiLA 서버로 보고 능력을 Command·Property를 담은 Feature로 기술하며, 서버·Feature 자동 탐색과 gRPC(HTTP/2·Protocol Buffers) 통신을 규정한다. 명세는 Core와 Mapping 두 부분으로 이뤄지고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했다. 'SiLA Robotics & mobile Robotics' 작업반이 활동 중이며, 워크플로 오케스트레이션은 Camunda 같은 외부 구현이 예로 언급된다. [사실][^ref-1001] | SiLA Consortium |
| SS 713 | 표준 | The Robot Report 기사(2025-10-29)에 따르면 로봇·승강기·자동문 사이 데이터 교환을 다루는 싱가포르 표준이며, 싱가포르는 이를 ISO 국제표준으로 올리려 하고 BCA Braddell 캠퍼스의 ELEVATE 시험장에서 로봇·승강기·건물 시스템의 상호작용을 시험한다. 표준 원문은 열지 않았다. [사실][^ref-1004] | The Robot Report |
| TR 130 | 표준 | 같은 기사에 따르면 로봇과 중앙 관제 시스템의 상호운용을 다루는 싱가포르 기술 참조다. 원문은 열지 않았다. [사실][^ref-1004] | The Robot Report |
| Open-RMF | 오픈소스 | 제조사가 다른 로봇과 시스템이 함께 일하게 하는 프레임워크다. [사실][^ref-004] 싱가포르 국가 로봇 프로그램이 2018년 ROS(Robot Operating System) 기반으로 RMF를 함께 출범시켰고, 창이 공항에서는 청소 로봇 운영에 쓰인다. [사실][^ref-1004] | Open Robotics, The Robot Report |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, Open-RMF, 미확인, https://www.open-rmf.org/, 접근일 2026-09-24
[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-09-30
[^ref-1009]: ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones, 2024, https://www.iso.org/standard/82687.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s10.md

```markdown
---
title: "67. 기타 현장 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1000, ref-1001, ref-1002, ref-1003, ref-1004, ref-1005, ref-1006, ref-1007, ref-1008, ref-1009, ref-995, ref-996, ref-997, ref-998, ref-999]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#10
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 다른 연구영역과의 연결

# 67. 기타 현장 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 하드웨어 독립 산업 점검 플랫폼 같은 벤더 동향이 이어진다. [추정][^ref-1003] - [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 건설 현장 로봇 데이터를 BIM과 대조하는 일이 이어진다. [추정][^ref-1000]
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 하드웨어 독립 산업 점검 플랫폼 같은 벤더 동향이 이어진다. [추정][^ref-1003]
- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 건설 현장 로봇 데이터를 BIM과 대조하는 일이 이어진다. [추정][^ref-1000]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 날마다 바뀌는 건설 현장의 공간을 지도에 반영하는 일이 이어진다. [추정][^ref-1000]
- [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) — QR 코드 기반 자재 추적과 데이터센터 서버 자산 흐름 추적이 이어진다. [추정][^ref-999][^ref-1002]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 하드웨어 독립 점검 플랫폼(벤더 주장)과, 창이 공항에서 RMF가 청소 로봇 운영에 쓰인다는 기사가 이어진다. [추정][^ref-1003][^ref-1004]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — SS 713·TR 130, SiLA 2, ISO 18497이 이어진다. [추정][^ref-1004][^ref-1001][^ref-1009]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 로봇 전용 승강기 이용과 SS 713의 로봇·승강기·자동문 데이터 교환이 이어진다. [추정][^ref-997][^ref-1004]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 수확 로봇과 이송 로봇의 분업이 이어진다. [추정][^ref-1005]
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 농업 로봇 통합 관리 프로그램의 작업 순서 설정이 이어진다. [추정][^ref-1007]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 작업자를 따라가는 운반 로봇이 이어진다. [추정][^ref-1006]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 점검 로봇의 누출 탐지·계기 이상 감지가 이어진다. [추정][^ref-995][^ref-1008]
- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) — 5G 특화망과 클라우드에 두뇌를 둔 로봇이 이어진다. [추정][^ref-1008][^ref-997]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 계기 판독·열화상 영상 분석은 L. AI·학습 기술의 방법이 38. 모니터링·이상 탐지·원인 분석에 쓰이는 예다. [추정][^ref-1008]
- [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) — 배치 베이지안 탐색으로 다음 실험을 고르는 실험 계획 루프가 이어진다. [추정][^ref-996]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 자율 농업기계 안전 표준 ISO 18497이 이어진다. [추정][^ref-1009]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 공항 안내 로봇처럼 방문객을 상대하는 운영이 이어진다. [추정][^ref-998]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 농지·건설 현장의 주행 조건이 이어진다. [추정][^ref-1006][^ref-999]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-09-30
[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1002]: 아주경제 (윤선훈), 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동, 2023-11-08, https://www.ajunews.com/view/20231107091520837, 접근일 2026-09-30
[^ref-1003]: Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고, Game-changer: The rationale behind the investment in Energy Robotics, 2021-01-15, https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics, 접근일 2026-09-30
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-09-30
[^ref-1005]: 헬로디디 (이유진), 스스로 수확하고 운반···'로봇농부' 나왔다, 2023-03-09, https://www.hellodd.com/news/articleView.html?idxno=99827, 접근일 2026-09-30
[^ref-1006]: 농민신문 (조영창), 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역, 2024-03-25, https://www.nongmin.com/article/20240322500556, 접근일 2026-09-30
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-1009]: ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones, 2024, https://www.iso.org/standard/82687.html, 접근일 2026-09-30 (원문 미열람)
[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-09-30
[^ref-996]: Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583), A mobile robotic chemist, 2020-07, https://www.nature.com/articles/s41586-020-2442-2, 접근일 2026-09-30 (원문 미열람)
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-09-30
[^ref-998]: 로봇신문 (정원영), 인천국제공항, 안내 로봇 '에어스타' 본격 운영, 2018-07-11, https://www.irobotnews.com/news/articleView.html?idxno=14422, 접근일 2026-09-30
[^ref-999]: 서울신문, 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리, 2022-11-15, https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s4.md

```markdown
---
title: "67. 기타 현장 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-1000, ref-1001, ref-1008, ref-1009, ref-996, ref-997]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#4
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 핵심 개념과 용어

# 67. 기타 현장 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **5G 특화망(이음5G)(Private 5G Network)** — [용어집](../../glossary/private-5g-network.md) 참조. 이번 사례에서는 한전 변전소 로봇의 점검 영상을 인공지능(AI) 서버로 보내는 통신과, 네이버 1784 배달 로봇을 클라우드에서 제어하는 통신에 쓰였다. [사실][^ref-1008][^ref-997]
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **5G 특화망(이음5G)(Private 5G Network)** — [용어집](../../glossary/private-5g-network.md) 참조. 이번 사례에서는 한전 변전소 로봇의 점검 영상을 인공지능(AI) 서버로 보내는 통신과, 네이버 1784 배달 로봇을 클라우드에서 제어하는 통신에 쓰였다. [사실][^ref-1008][^ref-997]
- **브레인리스 로봇(Brainless Robot)** — 두뇌를 로봇 본체가 아니라 클라우드에 두고 통신망으로 제어받는 로봇이며, 네이버 제2사옥 1784의 배달 로봇 루키가 예다. [사실][^ref-997]
- **스캔 대 BIM 비교(Scan-vs-BIM)** — [용어집](../../glossary/scan-vs-bim.md) 참조. 건설 현장에서 로봇이 라이다(Light Detection and Ranging, LiDAR)·360도 카메라로 모은 데이터를 3차원 BIM 데이터와 통합해 공사 간섭을 확인한 실증이 있다(2020-07). [사실][^ref-1000]
- **SiLA 2(Standardization in Lab Automation 2)** — 실험실 장비를 'SiLA 서버'로 보고, 서버의 능력을 Command(매개변수를 받는 동작)와 Property(읽거나 구독하는 데이터)를 담은 Feature로 기술하는 실험실 자동화 통신 표준이다. [사실][^ref-1001]
- **자율 실험실(Self-driving Laboratory)** — 로봇이 실험을 수행하고 알고리즘이 결과를 보고 다음 실험을 고르는 실험실로, 이동 매니퓰레이터가 개조하지 않은 일반 실험실에서 8일 동안 자율로 실험한 사례가 보고됐다. [사실][^ref-996]
- **자율 운용 구역(Autonomous Operating Zone)** — ISO 18497-3:2024가 다루는 주제로, 자율 농업기계가 운용되는 구역의 안전을 다룬다. [사실][^ref-1009]
- **Open-RMF(Open Robotics Middleware Framework)** — [용어집](../../glossary/open-rmf.md) 참조. 제조사가 다른 로봇과 시스템이 함께 일하게 하는 오픈소스 프레임워크다. [사실][^ref-004]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, Open-RMF, 미확인, https://www.open-rmf.org/, 접근일 2026-09-24
[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-09-30
[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-1009]: ISO, ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones, 2024, https://www.iso.org/standard/82687.html, 접근일 2026-09-30 (원문 미열람)
[^ref-996]: Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583), A mobile robotic chemist, 2020-07, https://www.nature.com/articles/s41586-020-2442-2, 접근일 2026-09-30 (원문 미열람)
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s11.md

```markdown
---
title: "67. 기타 현장 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#11
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 열린 질문

# 67. 기타 현장 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 한국산업표준(KS)과는 어떻게 다른가? 관련: 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 한국산업표준(KS)과는 어떻게 다른가? 관련: 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? 관련: 20. 로봇·제조사 관제 연동
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? 관련: 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? 관련: 23. 업무 시스템 연동, 38. 모니터링·이상 탐지·원인 분석
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-02) SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? 관련: 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s3.md

```markdown
---
title: "67. 기타 현장 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1000, ref-1001, ref-1002, ref-1004, ref-1006, ref-1007, ref-1008, ref-995, ref-996, ref-997, ref-998, ref-999]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#3
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 왜 중요한가

# 67. 기타 현장 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 확인한 67. 기타 현장의 로봇 작업은 플랜트·변전소 점검·순찰, 건설 현장 공정·품질·안전 점검, 농업의 방제·운반·모니터링·수확, 공항 같은 공공시설의 안내·청소, 오피스 빌딩 사내 배달, 데이터센터 서버 자산 운반·관리, 연구실 실험 수행의 일곱 형태로 나타나며, 형태마다 근거는 단일 출처 사례다. [추정][^ref-995][^ref-1008][^ref-999][^ref-1007][^ref-998][^ref-1004][^ref-997][^ref-1002][^ref-996]
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 확인한 67. 기타 현장의 로봇 작업은 플랜트·변전소 점검·순찰, 건설 현장 공정·품질·안전 점검, 농업의 방제·운반·모니터링·수확, 공항 같은 공공시설의 안내·청소, 오피스 빌딩 사내 배달, 데이터센터 서버 자산 운반·관리, 연구실 실험 수행의 일곱 형태로 나타나며, 형태마다 근거는 단일 출처 사례다. [추정][^ref-995][^ref-1008][^ref-999][^ref-1007][^ref-998][^ref-1004][^ref-997][^ref-1002][^ref-996]

현장마다 작업 대상과 기대는 인프라가 다르다. 점검 현장은 무인화 예정이거나 위험한 설비에서 계기값·열화상·가스 농도 같은 정보를 작업 대상으로 삼는다. [추정][^ref-995][^ref-1008] 건설 현장은 공간이 날마다 바뀌어 로봇이 모은 데이터를 [건물 정보 모델링(Building Information Modeling, BIM)](../../glossary/building-information-modeling.md) 데이터와 대조한다. [추정][^ref-999][^ref-1000] 농업은 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다. [추정][^ref-1007][^ref-1006]

공항은 다국어 안내·에스코트처럼 사람을 작업 대상으로 삼는다. [추정][^ref-998] 오피스·데이터센터는 로봇 전용 승강기·클라우드·5G 통신 같은 건물 인프라에 기댄다. [추정][^ref-997][^ref-1002] 연구실은 분석 장비 조작과 실험 계획이 한 루프로 묶인다. [추정][^ref-996][^ref-1001]

설비 노후화도 도입 배경으로 제시된다. 한국전력공사는 900여 개 변전소 가운데 50% 이상이 20년 넘은 설비라는 점을 변전소 로봇 순시점검 실증(2022-12)의 배경으로 들었다. [사실][^ref-1008] 확인한 국내 사례는 대부분 한 기관이 만든 로봇을 자체 관리 계층으로 묶은 형태여서, 제조사가 다른 로봇을 잇는 역할은 이 현장들에서 아직 공개 사례로 확인되지 않았다(9절 참조). [추정][^ref-997][^ref-1007]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1000]: 인더스트리뉴스 (정형우), GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로, 2020-07-13, https://www.industrynews.co.kr/news/articleView.html?idxno=38911, 접근일 2026-09-30
[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1002]: 아주경제 (윤선훈), 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동, 2023-11-08, https://www.ajunews.com/view/20231107091520837, 접근일 2026-09-30
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-09-30
[^ref-1006]: 농민신문 (조영창), 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 자동 하역, 2024-03-25, https://www.nongmin.com/article/20240322500556, 접근일 2026-09-30
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-09-30
[^ref-996]: Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583), A mobile robotic chemist, 2020-07, https://www.nature.com/articles/s41586-020-2442-2, 접근일 2026-09-30 (원문 미열람)
[^ref-997]: 이코노미스트 (송재민), 로봇이 로봇들을 움직이는, 네이버 1784, 2023-01-11, https://economist.co.kr/article/view/ecn202301110006, 접근일 2026-09-30
[^ref-998]: 로봇신문 (정원영), 인천국제공항, 안내 로봇 '에어스타' 본격 운영, 2018-07-11, https://www.irobotnews.com/news/articleView.html?idxno=14422, 접근일 2026-09-30
[^ref-999]: 서울신문, 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리, 2022-11-15, https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-02/pages/topics/2026/2026-09-30-area67-s8.md

```markdown
---
title: "67. 기타 현장 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 67
related_areas: [1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1001, ref-1004, ref-1008, ref-996]
last_run: 2026-09-30
version: 1
split_from: docs/categories/site-type-applications/other-sites.md#8
---

[홈](../../index.md) › [주제](../index.md) › 67. 기타 현장 — 대표 연구와 자료

# 67. 기타 현장 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Burger, B. 외, A mobile robotic chemist(Nature 583, 2020) — 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다. [사실][^ref-996] 저자들은 이를 장비가 아니라 연구자를 자동화하는 접근으로 설명한다. [사실][^ref-996]
- 이 페이지는 [67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[67. 기타 현장](../../categories/site-type-applications/other-sites.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Burger, B. 외, A mobile robotic chemist(Nature 583, 2020) — 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다. [사실][^ref-996] 저자들은 이를 장비가 아니라 연구자를 자동화하는 접근으로 설명한다. [사실][^ref-996]
- The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption(2025) — RMF의 출범 경위, 창이 공항 운영, SS 713·TR 130, ELEVATE 시험장을 한곳에서 정리한 기사다. [사실][^ref-1004]
- 넷매니아즈, 한전의 5G 특화망 기반 응용(2023) — 한전 신중부 변전소 실증(2022-12)의 IoT 예방진단, 4족 로봇 순시점검, CCTV 안전관리를 한전 자료를 바탕으로 정리한 2차 자료이며 한전 원자료는 열지 않았다. [사실][^ref-1008]
- SiLA Consortium, SiLA Standards — 실험실 장비 통신 표준 SiLA 2의 구조와 작업반을 소개하는 공식 페이지다. [사실][^ref-1001]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/other-sites.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [67. 기타 현장](../../categories/site-type-applications/other-sites.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/other-sites.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1001]: SiLA Consortium, SiLA Standards, 미확인, https://sila-standard.com/standards/, 접근일 2026-09-30
[^ref-1004]: The Robot Report, Singapore's National Robotics Programme reveals initiatives to advance robot adoption, 2025-10-29, https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/, 접근일 2026-09-30
[^ref-1008]: 넷매니아즈 (손장우), 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리, 2023-09-30, https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management, 접근일 2026-09-30
[^ref-996]: Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583), A mobile robotic chemist, 2020-07, https://www.nature.com/articles/s41586-020-2442-2, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-02 | 67. 기타 현장 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 994건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 264개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
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
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
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
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
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
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
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
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [67] 에 걸린 0건 / 전체 190건)

```markdown
없음
```

### runs/2026-09-30-02/verification2.json

```json
{
  "run_id": "2026-09-30-02",
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
    "overlaps": [
      "Open-RMF 일반 설명은 1차 지시대로 기존 ref-004 를 재사용했다. ref-004 각주 정의 줄은 참고문헌 페이지와 대조하지 못했다. 입력에 docs/references/ref-004.md 가 없어 스토리텔러가 고칠 수 없으므로 수정 지시에서 빼고, 퍼블리셔가 덮어쓰도록 요청한다(verification_note 참조)",
      "5G 특화망(이음5G)·스캔 대 BIM 비교·건물 정보 모델링·Open-RMF 는 기존 용어집 항목에 링크했고 새로 등록하지 않았다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "원 페이지 9절 'RMF(Robot Middleware Framework, 현 Open-RMF)': ref-1004 원문은 RMF 를 'Robotics Middleware Framework'로 풀어 쓴다. 직전 2차 수정 지시가 틀린 풀이를 제시했고, 스토리텔러는 그 지시를 그대로 이행했다"
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "원 페이지(docs/categories/site-type-applications/other-sites.md) 9절 마지막 단락: 'RMF(Robot Middleware Framework, 현 Open-RMF)'를 'RMF(Robotics Middleware Framework, 현 Open-RMF)'로 고친다. 이유: ref-1004 원문(The Robot Report, 2025-10-29)은 RMF 를 'Robotics Middleware Framework'로 풀어 쓴다. 직전 2차 수정 지시의 풀이가 틀렸으며, 이 지시는 그 오류를 바로잡는 것이다. 다른 곳은 바꾸지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 0건. 강등: 없음. f1·f2·f7·f16·f20·f21·f22 의 과장이나 근거 없는 문구는 1차에서 수정을 조건으로 유지했다. 용어 후보 '정상 무인 시설'은 근거가 없어 등록하지 않았다. 원문 미열람 출처: ref-996(Nature 로그인 리디렉션 때문에 검색 결과와 저장소 PDF 일부로 확인), ref-1009(ISO 페이지 403 때문에 검색 결과 목록으로 확인). 발행일 정정: ref-1000 은 2020-07-13, ref-1005 는 2023-03-09. 주의: 모든 사례가 단일 출처이고 대부분 국내외 기사다. f4·f8 은 벤더 주장, f2 는 운영사 추산, f17 은 연구기관이 발표한 수치다. 현장 간 차이(f20), 여섯 항목(f21), 책임 경계(f22·f23)는 이번 사례에서 끌어낸 해석(추정)이다. 제조사가 다른 로봇을 한 계층에서 묶은 운영 사례는 이번 조사에서 확인되지 않았다. 에어스타(2018)와 Energy Robotics(2021) 자료는 기준일이 오래됐다. 검증 검색 3회(리서치 16회와 합쳐 19/30). 정정 요청은 없다. / 2차 수정 후 재검증(재검증 1회차). 브리프 밖 주장(드리프트)은 없다. 직전 2차 지시 5건 가운데 4건은 이행을 확인했다. 출처 5건의 제목 정정은 원 페이지·분리 페이지·reference_updates 에 모두 반영됐다. 10절 창이 공항 서술은 기사 수준으로 고쳐졌고, 9절 문장에 태그가 붙었으며, BIM·라이다·RMF 약어도 처음 나올 때 풀어 썼다. 남은 1건은 ref-004 각주 대조다. 입력에 docs/references/ref-004.md 가 없어 스토리텔러가 이행할 수 없으므로 수정 지시에서 뺐다. 퍼블리셔는 원 페이지와 분리 페이지 s4·s7 의 ref-004 각주 정의, s7 표의 Open-RMF 출처 칸 기관명을 참고문헌 페이지 값으로 덮어써야 한다. pipeline/agent_runner.py 담당에게는 재실행 입력에 인용된 기존 참고문헌 페이지를 넣도록 요청한다. 새로 고칠 것 1건: 직전 2차 지시가 RMF 풀이를 'Robot Middleware Framework'로 잘못 제시했다. ref-1004 원문을 다시 열어 'Robotics Middleware Framework'임을 확인했고, 9절 표기 정정을 지시한다. 이 문제는 이전 지시에 없던 것이며, 원인은 검증 쪽 지시 오류다. [분류원문] 블록과 1·2절, auto 마커는 입력 시드와 같다. 참고(분리 코드 담당): 10절 원 페이지 요약과 s10 세 줄 요약에서 두 목록 항목이 ' - '로 한 줄에 이어 붙어 있다. 분리 주제 페이지의 세 줄 요약도 두 줄뿐이다. 이번 재검증에서는 검색 없이 ref-1004 원문 1건만 열람했다.",
  "retry_reason": null
}
```
