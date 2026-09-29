(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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

### docs/categories/site-type-applications/index.md

```markdown
---
title: "Q. 현장 유형별 적용"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › Q. 현장 유형별 적용

# Q. 현장 유형별 적용

## 핵심 질문

현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

## 개요

현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타)마다 다른 요구와 도입 사례를 모으는 곳. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **61. 물류창고** | 입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 | 물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? | [61. 물류창고](warehouse.md) | published |
| **62. 제조 공장** | 라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 | 여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? | [62. 제조 공장](manufacturing-plant.md) | published |
| **63. 병원·의료** | 검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 | 감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? | [63. 병원·의료](hospital-and-healthcare.md) | published |
| **64. 상업 시설** | 호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 | 손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? | [64. 상업 시설](commercial-facilities.md) | published |
| **65. 가정·공동주택** | 집안일 보조, 공동주택 배송, 사생활 | 가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? | [65. 가정·공동주택](home-and-apartment.md) | published |
| **66. 실외** | 실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 | 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? | [66. 실외](outdoor.md) | published |
| **67. 기타 현장** | 점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 | 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? | [67. 기타 현장](other-sites.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

물류창고는 여러 현장 유형 가운데 하나다. 현장마다 다른 요구는 여기에 모으고, **모든 현장에 공통인 기능은 A~P에 둔다**. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 95건이다(논문 29건 · 기사·보고서 37건 · 업체 발표 9건 · 표준·오픈소스·기관 자료 20건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-972](../../references/ref-972.md) — Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs (발행 2026-06)
- [ref-929](../../references/ref-929.md) — Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (발행 2026-04-24)
- [ref-964](../../references/ref-964.md) — Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation (발행 2026-04-22)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-982](../../references/ref-982.md) — Tong, X., & Simoni, M. D. (arXiv), Robust Route Planning for Sidewalk Delivery Robots (발행 2025-07-16)
- [ref-928](../../references/ref-928.md) — Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors (발행 2024-12-02)
- [ref-946](../../references/ref-946.md) — Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (발행 2024-06-05)
- [ref-971](../../references/ref-971.md) — Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation (발행 2024-03-14)
- [ref-933](../../references/ref-933.md) — Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35), Collaborative robots in manufacturing and assembly systems: literature review and future research agenda (발행 2023-05-30)
- [ref-990](../../references/ref-990.md) — Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists (발행 2023-03)
- 그 밖에 19건

**기사·보고서**

- [ref-975](../../references/ref-975.md) — 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다 (발행 2026-09-27)
- [ref-979](../../references/ref-979.md) — 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 (발행 2026-09-20)
- [ref-931](../../references/ref-931.md) — 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 (발행 2026-09-07)
- [ref-984](../../references/ref-984.md) — 스포츠경향, 뉴빌리티, 덕수궁 순찰부터 도쿄 시내 배달까지 (발행 2026-09-02)
- [ref-981](../../references/ref-981.md) — DC Velocity, Starship steers its delivery robots off college campuses and toward grocery sector (발행 2026-06-08)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-973](../../references/ref-973.md) — The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder (발행 2025-10-30)
- [ref-970](../../references/ref-970.md) — 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인 (발행 2025-10-06)
- [ref-983](../../references/ref-983.md) — 지디넷코리아, 배민, 차세대 배달로봇 ‘딜리’ 8월 투입…운행안전인증 획득 (발행 2025-06-23)
- [ref-948](../../references/ref-948.md) — 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까 (발행 2025-04-10)
- 그 밖에 27건

**업체 발표**

- [ref-965](../../references/ref-965.md) — 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 (발행 2026-01-15)
- [ref-974](../../references/ref-974.md) — LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026 (발행 2026-01-06)
- [ref-924](../../references/ref-924.md) — SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW (발행 2025-10-16)
- [ref-916](../../references/ref-916.md) — Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot (발행 2025-07)
- [ref-930](../../references/ref-930.md) — 현대자동차그룹, ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 (발행 2023-11-21)
- [ref-920](../../references/ref-920.md) — CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 (발행 2023-10-26)
- [ref-957](../../references/ref-957.md) — Otis Elevator Company, Elevators and service robots (발행 미확인)
- [ref-938](../../references/ref-938.md) — Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) (발행 미확인)
- [ref-926](../../references/ref-926.md) — Siemens, AGV fleet management integration with intralogistics (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-994](../../references/ref-994.md) — ISO, ISO/TR 4448-1:2024 Intelligent transport systems — Public-area mobile robots (PMR) — Part 1: Overview of paradigm (발행 2024-08)
- [ref-959](../../references/ref-959.md) — 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (발행 2024)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-977](../../references/ref-977.md) — Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board (발행 2023-10-23)
- [ref-978](../../references/ref-978.md) — CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) (발행 2023-03-14)
- [ref-985](../../references/ref-985.md) — 内閣府 (일본 내각부), 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について (발행 2023)
- [ref-945](../../references/ref-945.md) — 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 (발행 2021-11-11)
- [ref-942](../../references/ref-942.md) — Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare (발행 2021-02-10)
- [ref-988](../../references/ref-988.md) — Open Navigation (Nav2), Navigating Using GPS Localization — Nav2 documentation (발행 미확인)
- 그 밖에 10건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [66. 실외](outdoor.md) — 섹션 3~11 신규 작성(seed → draft): 현장 유형 실외 사례 3건(보도 배송 딜리, 덕수궁 순찰 뉴비, 피츠버그 캠퍼스 배송 Starship)을 여섯 항목으로 정리, 운행안전인증 항목 수 두 기준일 병기, 한국·일본·미국 보도 규정, ISO 4448, 책임 경계, 연결 영역 16개, 열린 질문 5건. 2차 수정: 4절 도입 문장을 태그 없는 안내문으로 교체, 5절 세 번째 사례 수행 자원의 '허가' 삭제, 9절 GPS·RTK·PDD 첫 등장 풀어 쓰기 (실행 2026-09-30-01)
- 2026-09-30 · 생성 · [66. 실외 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area66-s7.md) — 자동 분리: 66. 실외 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,761자)을 옮겼다. 2차 수정 원칙에 맞춰 표의 GPS 첫 등장을 풀어 썼다 (실행 2026-09-30-01)
- 2026-09-30 · 생성 · [66. 실외 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area66-s6.md) — 자동 분리: 66. 실외 의 "6. 대표 접근법과 기술" 절(1,280자)을 옮겼다. 2차 수정 지시로 위치 추정 소절의 GPS·RTK·UTM 첫 등장을 풀어 썼다 (실행 2026-09-30-01)
- 2026-09-30 · 생성 · [66. 실외 — 대표 연구와 자료](../../topics/2026/2026-09-30-area66-s8.md) — 자동 분리: 66. 실외 의 "8. 대표 연구와 자료" 절(1,110자)을 옮겼다 (실행 2026-09-30-01)
- 2026-09-30 · 생성 · [66. 실외 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area66-s4.md) — 자동 분리: 66. 실외 의 "4. 핵심 개념과 용어" 절(909자)을 옮겼다. 2차 수정 지시로 세 줄 요약·본문 첫 문장을 태그·각주 없는 안내 문장으로 바꿨다 (실행 2026-09-30-01)
<!-- auto:category-recent:end -->
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

### templates/category.md

```markdown
---
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 로봇 온톨로지"
type: category
category: "{{category}}"                    # title 과 같은 값
tags: [{{tags}}]                            # 선택. 없으면 []
status: {{status}}                          # seed | published. 시드 대분류 페이지는 seed 이며, "다른 대분류와의 연결"이 채워져 게시되면 published 로 바꾼다 [가정]
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 원문 주석의 [n] 에 대응하는 참고문헌 id. 예: [ref-003]
version: {{version}}                        # 정수
---
<!--
[템플릿] 대분류 페이지 (type: category)
경로: docs/categories/<대분류 slug>/index.md
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "이 대분류의 자료"(논문·기사·업체 발표·표준 묶음별 출처 목록, 2026-09-28 추가), "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
일곱 섹션(4.3 + 2026-09-28 추가): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 이 대분류의 자료 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

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

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
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
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]". 굵은 표기가 있으면 그대로 두고, 명사형으로 끝나는 문단도 고치지 않는다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표의 행(대분류마다 3~7행)을 모두 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
표 전체는 auto:category-area-table 마커 안에 있고 퍼블리셔(pipeline/lib/render.py render_category_area_table)가 원문 파서와 세부영역 페이지의 status 로 다시 쓴다. 스토리텔러는 마커 사이를 건드리지 않는다. 마커 위의 안내 문장은 마커 밖이므로 그대로 둔다. 이 key 는 사양서에 없는 구축자 추가 key 이며, 시드 대분류 페이지·agents/shared-rules.md 6절의 auto key 목록·퍼블리셔(pipeline/lib/autoregion.py AUTO_KEYS)가 같은 값을 쓴다 [가정 — 사용자 결정 항목: 표 전체를 자동 영역으로 둘지, 표는 마커 밖에 두고 현재 상태 열만 갱신할지].
-->

## 이 대분류의 핵심 포인트

{{key_point_paragraphs}}
<!--
분류 원문에서 이 대분류 장의 표 아래 설명 문단들을 순서대로 모두 옮긴다. 문단마다 끝에 " [분류원문]" 을 붙이고, 그 줄에는 태그 뒤에 아무것도(각주 포함) 붙이지 않는다. 원문의 [n] 번호 표기는 문장 안에 그대로 둔다. 예: "... 참고 표준이다. [3] [분류원문]". 대응 각주 [^ref-00n] 은 이 절이 아니라 "참고 자료" 절의 별도 문장에 둔다. 굵게·기울임 표기를 유지한다. 에이전트는 이 절의 원문 문장을 고치지 않고, 원문 문단 뒤에 자기 문장을 덧붙이지도 않는다.
퍼블리셔(pipeline/checks/protect_source.py check_category)는 이 절에서 " [분류원문]" 으로 끝나는 줄만 모아 원문 문단 목록과 글자 단위로 대조한다. 태그 뒤에 각주를 붙이면 그 줄이 빠져 "핵심 포인트 문단 불일치"로 반려된다.
-->

## 다른 대분류와의 연결

{{category_connections}}
<!--
에이전트가 채운다. 목록 형식: "- [F. 연동](../integration/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회처럼 여러 대분류에 걸쳐 적용되는 대분류는 그 적용 관계를 드러낸다. Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고 모든 현장에 공통인 기능은 A~P에 둔다는 원문 취지를 지킨다. L. AI·학습 기술의 교차 규칙(매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석)과 C. 채팅 기반 구성·운영의 엔진 짝(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 여기서도 지킨다.
-->

## 이 대분류의 자료

<!-- auto:category-sources:start -->
(퍼블리셔가 자동 생성: 이 대분류 페이지·소속 세부영역·주제 페이지가 인용한 출처를 논문 / 기사·보고서 / 업체 발표(벤더 문서) / 표준·오픈소스·기관 자료로 묶어 최근 발행순으로 보인다)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:category-recent:end -->
<!-- 퍼블리셔가 이 대분류에 속한 세부영역·주제 페이지의 최근 변경을 최신순으로 넣는다(날짜 | 실행 id | 페이지 | 변경 요약). 마커 사이는 스토리텔러가 건드리지 않는다. -->

## 참고 자료

{{source_footnote_sentences}}

{{footnotes}}
<!-- "이 대분류의 핵심 포인트" 원문 문단의 [n] 에 대응하는 각주를 별도 문장으로 두고(예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]"), 그 아래에 각주 정의를 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". "다른 대분류와의 연결"에서 쓴 각주도 여기에 둔다. 각주가 없으면 "없음". 이 절은 사양서 4.3 의 여섯 섹션 밖의 보조 절로, 5.3 의 각주 정의 자리를 위해 구축자가 추가했으며 번호를 붙이지 않는다 [가정]. -->
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

### docs/standards/index.md (요약: 237개 — 이름 · 종류 · 발행 기관)

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
```

### runs/2026-09-30-02/docs_tree.txt

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
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/amr-assisted-order-picking.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
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
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explicit-implicit-confirmation.md
glossary/failure-explanation.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/giai.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
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
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/prompt-injection.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-friendly-building-certification.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/semantic-id.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/similarity-transformation.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/software-nameplate.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/structured-output.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/user-simulator.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
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
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
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
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
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
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 접근법 6가지, 표준 5건, 책임 경계, 연결 영역 17개, 열린 질문 5건. 2차 수정: 출처 5건 제목 정정, 9절 태그 추가, BIM·라이다·RMF 첫 등장 풀어 쓰기"
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
  "changelog_entry": "2026-09-30 | 67. 기타 현장 | 섹션 3~11 신규 작성(seed → draft): 현장 유형 기타 사례 4건(Equinor CCS 시설 점검, 건설 현장 점검, 농촌진흥청 농업 로봇 통합 관리·운반, 네이버 1784 사내 배달)을 여섯 항목으로 정리, 표준 5건(ISO 18497·SiLA 2·SS 713·TR 130·Open-RMF), 책임 경계, 연결 영역 17개, 열린 질문 5건. 1차 조건부 승인 수정 16건·2차 수정 5건(출처 제목 정정, 창이 공항 서술 완화, 태그 보완, 약어 풀어 쓰기, ref-004 각주는 대조 요청) 이행 | run 2026-09-30-02",
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
      "summary": "싱가포르 국가 로봇 프로그램의 RMF(Open-RMF) 출범·창이 공항 청소 로봇 운영, SS 713·TR 130 표준, ELEVATE 시험장을 다룬 기사.",
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
    "ref-004 각주(분리 페이지 s4·s7): 2차 수정 지시대로 docs/references/ref-004.md 의 '각주 형식' 줄을 그대로 복사해야 하나, 이번 재실행 입력에도 그 파일이 없어 이전 줄을 유지했다. pipeline/agent_runner.py 담당은 재실행 입력에 docs/references/ref-004.md 를 넣고, 넣지 못하면 퍼블리셔가 두 페이지의 ref-004 각주 정의와 s7 표 Open-RMF 행 출처 칸 기관명을 참고문헌 페이지 값으로 덮어써야 한다."
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
    "2차: 약어 풀어 쓰기 — 원 페이지 5절 GS건설 사례 완료·인계 칸의 첫 BIM 을 '건물 정보 모델링(Building Information Modeling, BIM)', 5절 Equinor 표 수행 자원 칸의 첫 라이다를 '라이다(Light Detection and Ranging, LiDAR)', 9절의 첫 RMF 를 'RMF(Robot Middleware Framework, 현 Open-RMF)'로 풀어 썼다."
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

확인한 국내 사례(네이버 ARC, 농촌진흥청 통합 관리 프로그램)는 한 기관이 만든 로봇을 자체 계층으로 묶은 것이다. [추정][^ref-997][^ref-1007] 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 이번 조사에서 확인되지 않았다. [추정][^ref-1004][^ref-1003] 창이 공항에서 RMF(Robot Middleware Framework, 현 Open-RMF)가 청소 로봇 운영에 쓰인다는 기사와 벤더 주장이 있을 뿐이다. [추정][^ref-1004][^ref-1003]

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


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 원 페이지(docs/categories/site-type-applications/other-sites.md) 9절 마지막 단락: 'RMF(Robot Middleware Framework, 현 Open-RMF)'를 'RMF(Robotics Middleware Framework, 현 Open-RMF)'로 고친다. 이유: ref-1004 원문(The Robot Report, 2025-10-29)은 RMF 를 'Robotics Middleware Framework'로 풀어 쓴다. 직전 2차 수정 지시의 풀이가 틀렸으며, 이 지시는 그 오류를 바로잡는 것이다. 다른 곳은 바꾸지 않는다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 0건. 강등: 없음. f1·f2·f7·f16·f20·f21·f22 의 과장이나 근거 없는 문구는 1차에서 수정을 조건으로 유지했다. 용어 후보 '정상 무인 시설'은 근거가 없어 등록하지 않았다. 원문 미열람 출처: ref-996(Nature 로그인 리디렉션 때문에 검색 결과와 저장소 PDF 일부로 확인), ref-1009(ISO 페이지 403 때문에 검색 결과 목록으로 확인). 발행일 정정: ref-1000 은 2020-07-13, ref-1005 는 2023-03-09. 주의: 모든 사례가 단일 출처이고 대부분 국내외 기사다. f4·f8 은 벤더 주장, f2 는 운영사 추산, f17 은 연구기관이 발표한 수치다. 현장 간 차이(f20), 여섯 항목(f21), 책임 경계(f22·f23)는 이번 사례에서 끌어낸 해석(추정)이다. 제조사가 다른 로봇을 한 계층에서 묶은 운영 사례는 이번 조사에서 확인되지 않았다. 에어스타(2018)와 Energy Robotics(2021) 자료는 기준일이 오래됐다. 검증 검색 3회(리서치 16회와 합쳐 19/30). 정정 요청은 없다. / 2차 수정 후 재검증(재검증 1회차). 브리프 밖 주장(드리프트)은 없다. 직전 2차 지시 5건 가운데 4건은 이행을 확인했다. 출처 5건의 제목 정정은 원 페이지·분리 페이지·reference_updates 에 모두 반영됐다. 10절 창이 공항 서술은 기사 수준으로 고쳐졌고, 9절 문장에 태그가 붙었으며, BIM·라이다·RMF 약어도 처음 나올 때 풀어 썼다. 남은 1건은 ref-004 각주 대조다. 입력에 docs/references/ref-004.md 가 없어 스토리텔러가 이행할 수 없으므로 수정 지시에서 뺐다. 퍼블리셔는 원 페이지와 분리 페이지 s4·s7 의 ref-004 각주 정의, s7 표의 Open-RMF 출처 칸 기관명을 참고문헌 페이지 값으로 덮어써야 한다. pipeline/agent_runner.py 담당에게는 재실행 입력에 인용된 기존 참고문헌 페이지를 넣도록 요청한다. 새로 고칠 것 1건: 직전 2차 지시가 RMF 풀이를 'Robot Middleware Framework'로 잘못 제시했다. ref-1004 원문을 다시 열어 'Robotics Middleware Framework'임을 확인했고, 9절 표기 정정을 지시한다. 이 문제는 이전 지시에 없던 것이며, 원인은 검증 쪽 지시 오류다. [분류원문] 블록과 1·2절, auto 마커는 입력 시드와 같다. 참고(분리 코드 담당): 10절 원 페이지 요약과 s10 세 줄 요약에서 두 목록 항목이 ' - '로 한 줄에 이어 붙어 있다. 분리 주제 페이지의 세 줄 요약도 두 줄뿐이다. 이번 재검증에서는 검색 없이 ref-1004 원문 1건만 열람했다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
