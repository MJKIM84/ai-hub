(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-17
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 65. 가정·공동주택 (Q. 현장 유형별 적용)
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

### runs/2026-09-29-17/target.json

```json
{
  "run_id": "2026-09-29-17",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 109,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 65,
    "area_name": "65. 가정·공동주택",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=65"
}
```

### runs/2026-09-29-17/research.json

```json
{
  "run_id": "2026-09-29-17",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 65,
    "area_name": "65. 가정·공동주택",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 매터(Matter)·실외이동로봇 운행안전인증·비전 언어 행동 모델·원격 조작 용어 없음(이동형 영상정보처리기기·로봇 친화형 건축물 인증은 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 공동주택 배송(삼성물산 래미안 리더스원·현대건설·롯데글로벌로지스), 세대 내 가사 로봇(로봇청소기·LG 클로이드·1X NEO), 사생활 사고(iRobot 이미지 유출)와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 공동현관·승강기 연동 방식, 단지 집하 방식, 수령 인증, 원격 조작 보조, 가정 기기 연동 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Matter 로봇청소기 장치 유형, 개인정보 보호법 제25조의2, 개정 지능형로봇법, 이동로봇 특별법안 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — BEHAVIOR-1K, 공동주택 서비스 로봇 인식 연구, 가정 로봇 데이터 유출 탐사 보도 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]",
    "국내 공동주택에서 배송로봇은 단지 입구·지하주차장·공동현관·승강기를 거쳐 세대 현관까지 어떻게 이동하며, 공동현관·승강기 연동과 수령 확인은 어떤 방식으로 구현되는가? (섹션 5·6 겨냥, 현장 유형 가정 명시, 한국 자료 우선)",
    "세대 안의 집안일(정리·청소·세탁·주방) 로봇은 제품과 연구에서 어디까지 와 있으며 무엇이 아직 어려운가? (섹션 3·5·8 겨냥)",
    "가정 로봇의 카메라·지도·원격 조작은 어떤 사생활 위험을 만들었고(유출 사고·보안 조사), 이를 막는 법·설계 수단은 무엇인가? (섹션 3·6·7 겨냥)",
    "공동주택·단지 도로를 다니는 로봇에 적용되는 국내 제도(개정 지능형로봇법 실외이동로봇 운행안전인증, 이동로봇 특별법안, 개인정보 보호법 제25조의2)는 무엇을 규정하는가? (섹션 7 겨냥)",
    "가정 기기와 로봇을 제조사와 무관하게 연결하는 스마트홈 표준(Matter)은 로봇에 대해 무엇을 정의하는가? (섹션 7 겨냥)",
    "가정·공동주택에서 ROP 가 직접 맡을 것(배송 요청 수신·이기종 배정·공동현관·승강기 예약·수령 확인·사생활 제약 반영)과 배달 앱·택배사·승강기·월패드·로봇 자체 기능·법령에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "삼성물산은 2026-01 서울 서초구 래미안 리더스원에서 뉴빌리티·요기요와 함께 단지 인근까지 운영하던 음식배달로봇 서비스를 세대 현관까지 확장했으며, 공동현관 자동문 개폐와 엘리베이터 호출 연동을 해결해 도어 투 도어로 배달하고 주문자만 음식을 꺼낼 수 있게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-965",
        "ref-966",
        "ref-979"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "삼성물산 뉴스룸(2026-01-15): 반경 1.2km 식음료점 130여 곳 대상, \"주문자만 배달음식 픽업이 가능\". 지디넷코리아(2025-01-19)는 삼성물산×뉴빌리티 래미안 리더스원을, 미디어펜(2026-09-20)은 공동현관 자동문 개폐·승강기 호출 연결을 따로 전한다.",
      "as_of": "2026-01-15",
      "site_type": "가정",
      "flow_item": "완료·인계"
    },
    {
      "id": "f2",
      "claim": "삼성물산은 래미안 리더스원 실증 기간에 서비스를 이용한 입주민 113명의 만족도가 95%이고 서비스 필요성 공감 99%, 유료 이용 의사 74%였다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-965"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 삼성물산 뉴스룸 본문 \"입주민의 만족도는 95%\", 각주 '서비스를 이용한 입주민 113명 대상 조사', 조사 시기 미표기. 외부인 출입 갈등·단지 내 배달 이동수단 위험 감소도 회사 설명이다.",
      "as_of": "2026-01-15",
      "site_type": "가정",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f3",
      "claim": "현대건설은 모빈과 함께 공동주택 배송로봇 서비스를 추진해, 로봇이 단지 입구에서 지하주차장과 공동출입문을 지나 승강기를 타고 세대 현관까지 식음료 등을 나르게 했다(적용 예정 단지로 DH 대치 에델루이가 보도됐다).",
      "tag": "사실",
      "source_ids": [
        "ref-966",
        "ref-979"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "지디넷코리아(2025-01-19): 현대건설×모빈 → DH 대치 에델루이, 이동 경로 지하주차장→공동출입문→엘리베이터→세대 현관. 미디어펜(2026-09-20)도 같은 경로를 전한다.",
      "as_of": "2026-09-20",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f4",
      "claim": "미디어펜(2026-09-20)에 따르면 현대건설 배송로봇은 승강기 시스템과 연동해 자동 호출·목적층 재호출·정원 초과 여부 판단을 구현했고, 업계는 공동출입문이 열리지 않거나 승강기를 호출할 수 없으면 단지 안 운행이 끊기며 관제시스템과 충전시설도 갖춰야 한다고 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-979"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"로봇과 승강기 시스템을 연동해 자동 호출과 목적층 재호출, 정원 초과 여부 판단 등의 기능을 구현했다.\" 기사는 공동출입문·승강기 호출 실패 시 운행 단절, 관제시스템·충전시설 필요도 함께 적는다.",
      "as_of": "2026-09-20",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "롯데글로벌로지스는 로보티즈와 함께 고양·파주 아파트 단지에서 택배 배송로봇을 실증했으며(한국로봇산업진흥원 규제혁신 로봇 실증사업), 로보티즈의 자율주행로봇 '개미'는 로봇팔로 승강기 버튼을 직접 눌러 타고 내리는 시험을 마쳤다.",
      "tag": "사실",
      "source_ids": [
        "ref-966",
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "지디넷코리아(2025-01-19): 롯데글로벌로지스×로보티즈 고양·파주 단지, 규제혁신 로봇 실증사업. 정보통신신문(2024-07-18): 개미의 로봇 팔로 승강기 버튼을 직접 조작해 타고 내리는 시험 완료.",
      "as_of": "2025-01-19",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "정보통신신문(2024-07-18)은 공동주택 로봇 택배 운영 방식을 단지 단위 중앙집하(집하장 1개소), 동 단위 분산집하(동마다 물품보관함), 구역 단위 분산집하(N개 동마다 보관함 1개소)의 세 가지로 나누고, 택배 차량이 집하처에서 송장번호를 인식시키면 관제실이 거주자와 통신하며 로봇을 통제해 배송하는 흐름을 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "세 가지 시나리오: 단지단위 중앙집하 / 동단위 분산집하 / 지역(Zone)단위 분산집하. 송장번호 인식 → 관제실이 거주자와 통신해 로봇 통제·배송.",
      "as_of": "2024-07-18",
      "site_type": "가정",
      "flow_item": "시작 조건"
    },
    {
      "id": "f7",
      "claim": "같은 기사는 배송로봇이 좁은 보도에서 행인과 충돌하거나 통신 장애로 급정지할 위험을 지적하고, 개인영상정보 촬영은 불특정 다수의 동의 대신 불빛·소리·안내판으로 촬영 사실을 알리고 업무 목적에 불필요한 영상은 즉시 삭제해야 한다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통신장애 시 급정지 사고 우려, 촬영 사실을 '불빛, 소리, 안내판 등을 통해' 고지, '업무목적 달성에 불필요한 영상은 즉시 삭제' 필요.",
      "as_of": "2024-07-18",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "2023-09-15 시행된 개인정보 보호법 제25조의2는 업무 목적의 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영하는 것을 원칙적으로 막고, 촬영 사실을 명확히 표시했는데도 거부 의사가 없는 경우 등만 예외로 두며, 목욕실·화장실·탈의실처럼 사생활 침해 우려가 큰 장소 내부를 볼 수 있는 곳의 촬영을 금지하고, 촬영 시 불빛·소리·안내판 등으로 표시하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-978"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제25조의2(이동형 영상정보처리기기의 운영 제한) 제1~4항, 법률 제19234호(2023-03-14 일부개정), 시행 2023-09-15. CaseNote 게재 조문 기준(국가법령정보센터 원문은 이번에 열지 못함).",
      "as_of": "2023-09-15",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "제25조의2가 '업무 목적'과 '공개된 장소'를 요건으로 두므로, 단지 도로·공동현관·승강기를 다니는 공동주택 배송로봇의 촬영은 이 조항의 관리 대상이 될 가능성이 크지만, 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 촬영은 이 조항의 직접 대상이 아닐 수 있어 제조사의 영상 수집·처리는 다른 규율(동의 기반 처리 등)에 기대야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-978",
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "조문 제1항의 요건('업무를 목적으로', '공개된 장소')에서 도출한 해석이다. 개인정보보호위원회 해석·가이드라인은 이번에 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "2023-11-17 시행된 개정 지능형로봇법은 질량 500kg·시속 15km 이하의 배송·순찰 로봇을 실외이동로봇으로 정의하고, 운행구역 준수·횡단보도 통행 등 16개 시험항목의 운행안전인증과 보험(공제) 가입을 요구하며, 인증받은 로봇은 개정 도로교통법에 따라 보행자와 같은 지위로 보도를 다닐 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-967"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AI타임스(2023-11-16): \"운행구역 준수, 횡단보도 통행 등 16가지 시험항목에서 안전성을 검증받아야\" 함. 손해보장사업 실시기관 한국로봇산업협회, 안전운용의무 위반 시 운용자에게 범칙금.",
      "as_of": "2023-11-16",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "한병도 의원이 2026-09 초 대표 발의한 국토교통부 마련 '이동로봇의 안전한 이용 및 상용화 촉진을 위한 특별법안'은 건축법·국토계획법·공동주택관리법·주차장법에 흩어진 이동로봇 규제를 손질해, 시행되면 아파트가 입주자대표회의 의결로 배송·보안·순찰·청소·충전·주차로봇을 도입할 수 있게 하고 배송로봇의 공동현관 통과·엘리베이터 이용을 위한 통신 시스템 연동 절차를 간소화·표준화한다.",
      "tag": "사실",
      "source_ids": [
        "ref-975"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "한국경제(2026-09-27): \"아파트는 입주자대표회의 의결을 거쳐 배송·보안·순찰·청소·충전·주차로봇을 도입할 수 있다\". 법안은 발의 단계이며 국회 통과 여부는 미확인.",
      "as_of": "2026-09-27",
      "site_type": "가정",
      "flow_item": "시작 조건"
    },
    {
      "id": "f12",
      "claim": "Hwang·Kim·Kwag(한국생활환경학회지 30, 2026-06)은 공동주택 거주자 63명과 업계 종사자 65명(23개 기관)을 조사해 거주자의 95.2%가 서비스 로봇 도입에 긍정적이나 실제 체험 의향은 88.9%로 차이가 있고, 자녀가 있는 가구가 단지 내 배송을 유의하게 우선시하며, 거주자는 충돌 방지·개인정보 보호·사용자 인터페이스를, 업계는 시스템 통합·운영 안정성을 더 중시한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-972"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자녀 가구 단지 내 배송 우선 p=0.005, 기술 요구 차이 p=0.036. 사생활 우려는 20대 72.7%→40대 31.0%, 안전 우려는 18.2%→44.8%로 달랐으나 통계적으로 유의하지 않았다.",
      "as_of": "2026-06",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "MIT Technology Review(2022-12-19)는 iRobot 이 개발용 Roomba J7 로 가정 내부에서 수집한 이미지가 AI 학습용 라벨링을 위해 Scale AI 를 거쳐 베네수엘라 등의 외주 작업자에게 넘어갔고, 화장실의 여성과 복도의 아이가 찍힌 사진을 포함한 스크린숏 15장이 Facebook·Discord 등에 게시됐다고 보도했다.",
      "tag": "사실",
      "source_ids": [
        "ref-968"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "대상은 소비자 제품이 아닌 개발용 기기이며 동의서에 서명한 유료 데이터 수집자·직원의 집이다. iRobot 은 기기에 'video recording in progress' 스티커가 있었고 민감한 것은 수집자가 치울 책임이 있었다고 밝혔다.",
      "as_of": "2022-12-19",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "한국소비자원과 한국인터넷진흥원(KISA)이 국내 판매 로봇청소기 6개 모델(삼성전자·LG전자 2종, 드리미·로보락·에코백스·나르왈 4종)을 40개 보안 항목으로 조사한 결과, 일부 중국 브랜드 제품에서 사용자 인증 미흡으로 외부에서 촬영 사진을 열람하거나 카메라를 강제로 켤 수 있는 취약점이 발견됐고 국산 2종은 상대적으로 양호했다.",
      "tag": "사실",
      "source_ids": [
        "ref-969",
        "ref-970"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "바이라인네트워크(2025-10-31)·매일신문(2025-10-06) 모두 6개 모델·40개 항목을 전한다. 바이라인은 게시판 ID 로 이름·전화번호 조회, 데이터 암호화 미흡도 적는다. 한국소비자원·KISA 보도자료 원문은 인증서 오류로 열지 못했다.",
      "as_of": "2025-10",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "Connectivity Standards Alliance(CSA)가 2023-10-23 공개한 Matter 1.2 는 새 장치 유형 9종 가운데 하나로 로봇청소기를 넣어 원격 시작·진행 알림, 건식·습식 청소 모드, 브러시·오류·충전 상태 같은 정보를 제조사와 무관하게 다루게 했으며, 이 발표에는 지도나 구역 청소가 언급되지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-977"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "로봇청소기는 \"remote start and progress notifications\"와 청소 모드(dry vacuum vs wet mopping), 상태 정보(brush status, error reporting, charging status)를 지원한다. 냉장고·식기세척기·세탁기 등도 함께 추가됐다.",
      "as_of": "2023-10-23",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "Matter 가 로봇청소기의 시작·상태·모드를 제조사 공통 모델로 정의하므로, 세대 안의 제조사가 다른 청소 로봇을 하나의 제어 계층에서 일정·상태 수준으로 다루는 연동 경로가 될 수 있지만, 발표 범위에는 물건 운반·조작 같은 다른 가사 로봇 능력이 없어 가사 로봇 전반의 능력 표현으로는 부족할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-977"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Matter 1.2 발표의 장치 유형 목록(가전 8종+로봇청소기)에서 도출한 해석이다. 이후 판(1.3 이후)의 로봇 관련 변경은 이번에 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": "수행 자원"
    },
    {
      "id": "f17",
      "claim": "Li 외(arXiv 2403.09227, CoRL 2022 예비판)의 BEHAVIOR-1K 는 '로봇이 무엇을 해 주길 원하는가'를 묻는 설문에서 고른 일상 활동 1,000개를 집·정원·식당·사무실 50개 장면과 주석 달린 물체 9,000여 개로 OmniGibson 시뮬레이터에 구현한 벤치마크이며, 이 활동들은 길고 복잡한 조작이 필요해 최신 로봇 학습 방법에도 어렵다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"long-horizon and dependent on complex manipulation skills\"로 최신 방법에도 과제라고 적고, 모바일 매니퓰레이터로 예비 시뮬레이션-실물 전이 실험을 했다(arXiv 2024-03-14 제출).",
      "as_of": "2024-03-14",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f18",
      "claim": "LG전자는 CES 2026 에서 7자유도 팔 두 개·다섯 손가락 손·바퀴 기반 자율주행을 갖춘 가정용 로봇 LG 클로이드(CLOiD)가 냉장고에서 우유 꺼내기, 오븐에 크루아상 넣기, 세탁 시작, 건조된 옷 개기를 시연하며, 비전 언어 모델(VLM)과 비전 언어 행동 모델(VLA)을 쓰고 ThinQ·ThinQ ON 허브로 가전 서비스를 조율한다고 발표했다.",
      "tag": "추정",
      "source_ids": [
        "ref-974"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 두 모델은 \"trained on tens of thousands of hours of household task data\". 출시일·가격은 발표에 없고 사생활·안전 관련 언급도 없다.",
      "as_of": "2026-01-06",
      "site_type": "가정",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "1X 는 2025-10-28 가정용 휴머노이드 NEO 의 사전 주문(2만 달러 또는 월 499달러, 2026년 미국 가정 배송)을 받으며, 모르는 작업은 소유자가 1X 원격 조작자를 예약해 로봇을 안내하게 하는 '전문가 모드'와 로봇이 들어가지 않는 금지 구역·얼굴 흐림 같은 사생활 기능을 내세웠다.",
      "tag": "추정",
      "source_ids": [
        "ref-973"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: The Robot Report(2025-10-30)가 전한 회사 발표. 첫날부터 문 열기·물건 가져오기·조명 끄기, 이후 빨래 개기·선반 정리 등을 할 수 있다고 하며, 출시 때 완전 자율이 아니라 학습 능력을 강조한다.",
      "as_of": "2025-10-30",
      "site_type": "가정",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 65. 가정·공동주택의 로봇 작업은 (1) 공동주택 단지 배송 — 음식·택배를 공동현관·승강기를 거쳐 세대 현관까지(f1·f3·f5·f6), (2) 세대 안 청소 — 로봇청소기(f14·f15), (3) 정리·세탁·주방 같은 조작 가사 — 연구·시연 단계(f17·f18·f19), (4) 단지 공용 서비스 — 보안·순찰·청소·충전·주차(f11)의 네 형태로 나타난다.",
      "tag": "추정",
      "source_ids": [
        "ref-965",
        "ref-966",
        "ref-979",
        "ref-976",
        "ref-969",
        "ref-977",
        "ref-971",
        "ref-974",
        "ref-973",
        "ref-975"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "이번 실행의 finding 들을 작업 형태로 묶은 분류다. 국내 공동주택 배송은 상용·실증 단계이고, 조작 가사는 제품 시연·사전 주문·벤치마크 단계다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 가정·공동주택 로봇 작업의 여섯 항목은 다음처럼 채울 수 있다. 시작 조건은 배달 앱 주문·택배 송장 인식·입주자대표회의 의결·거주자 앱 일정(f1·f6·f11·f19), 작업 대상은 음식·택배·세탁물·바닥 같은 물건·공간과 거주자 영상·개인정보(f1·f13·f17·f18), 수행 자원은 배송로봇·관제실·공동현관·승강기와 가사 로봇·원격 조작자(f4·f6·f19)다. 제약은 공동현관·승강기 연동, 보도 통행 인증, 촬영 표시·금지 구역·민감 장소 촬영 금지(f4·f8·f10·f19), 완료·인계는 주문자만 꺼낼 수 있는 수령 방식과 세대 현관 하차(f1·f5), 예외·성과는 공동출입문·승강기 실패 시 운행 중단과 영상 유출·보안 취약점(f4·f13·f14)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-965",
        "ref-976",
        "ref-975",
        "ref-973",
        "ref-968",
        "ref-971",
        "ref-974",
        "ref-979",
        "ref-978",
        "ref-967",
        "ref-966",
        "ref-969"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "여섯 항목(원문 21장)에 finding 을 대응시킨 것이다. 수령 인증의 구체 방식(비밀번호·앱·QR)과 결과를 배달 앱에 돌려주는 방식은 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 65. 가정·공동주택에서 ROP 가 직접 맡을 범위는 다음과 같다. 배달 앱·택배 관제의 요청을 받아 배송·청소·순찰 로봇에 배정하고(f1·f6·f11), 공동현관·승강기를 예약·호출·재호출하며(f4), 수령 확인 결과를 돌려주고(f1), 촬영 표시·금지 구역·원격 조작 승인 같은 사생활 조건을 경로·권한 제약으로 반영한다(f8·f19). 확인한 국내 사례는 모두 건설사 한 곳과 로봇 업체 한 곳의 짝이며, 여러 제조사 로봇을 한 단지에서 묶은 공개 사례는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-965",
        "ref-976",
        "ref-975",
        "ref-979",
        "ref-978",
        "ref-973",
        "ref-966"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "삼성물산×뉴빌리티, 현대건설×모빈, 롯데글로벌로지스×로보티즈 짝(f1·f3·f5)과 특별법안의 연동 표준화 계획(f11)에서 도출했다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "연계 대상: 이종 제조사를 잇는 ROP 는 아래 외부 영역에 작업 요청·예약·인계·상태 확인만 걸고, 메뉴·결제·택배 배차, 승강기·자동문 제어, 주행·조작 안전 성능, 법적 판단은 해당 시스템·설비 업체·로봇 제조사·관리 주체에 맡겨야 할 것으로 보인다. 분류 원문 19장 기준으로 배달 앱·택배사 시스템은 상위 업무 시스템, 공동현관 자동문·승강기 제어반·월패드는 시설·설비 제어, 로봇의 자율주행·파지·VLA 모델은 로봇 자체 지능·제어, 개인정보 보호법·지능형로봇법·공동주택관리법상 절차는 업종별 조건에 속한다.",
      "tag": "추정",
      "source_ids": [
        "ref-965",
        "ref-979",
        "ref-974",
        "ref-978",
        "ref-967",
        "ref-975"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 19장의 다섯 경계에 이번 finding 의 외부 시스템을 대응시킨 해석이다. 월패드(홈네트워크) 연동 사례는 이번에 직접 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": "가정",
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "이 영역은 여러 세부영역과 이어진다. 공동현관·승강기 연동은 22. 설비·건물 시스템 연동(f1·f4·f11), 배달 앱·택배 관제는 23. 업무 시스템 연동(f1·f6), 이기종 로봇 관제는 20. 로봇·제조사 관제 연동(f22), 수령 확인은 17. 작업 대상·자산 식별과 인계 추적(f1)과 연결된다. 영상 촬영·유출은 53. 개인정보·영상 데이터(f8·f9·f13), 보안 취약점은 52. 통신 보호·위협 관리·감사(f14), 원격 조작 승인은 51. 인증·권한·격리·31. 사람–로봇 협업(f19), 금지 구역은 16. 장소 의미·지도 관리(f19), Matter 는 21. 상호운용 표준·적합성(f15·f16)과 이어진다. VLA 는 44. 로봇 기반 모델·언어 모델 계획(f18), 학습 데이터 라벨링은 47. AI·학습·적응과 모델 운영(f13), BEHAVIOR-1K 는 54. 시험·형식 검증·벤치마크(f17), 법령·특별법안은 59. 법·규제·보험·라이선스(f8·f10·f11), 거주자 수용성은 60. 노동·수용성·접근성(f12), 보도 통행은 66. 실외(f10)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-965",
        "ref-979",
        "ref-975",
        "ref-976",
        "ref-978",
        "ref-968",
        "ref-969",
        "ref-973",
        "ref-977",
        "ref-974",
        "ref-971",
        "ref-967",
        "ref-972"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "finding 과 세부영역 원문 명칭을 대응시킨 연결 목록이다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-965",
      "org": "삼성물산 뉴스룸",
      "title": "삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영",
      "published": "2026-01-15",
      "url": "https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "래미안 리더스원에서 뉴빌리티·요기요와 음식배달로봇을 세대 현관까지 확장했다. 공동현관 자동문·엘리베이터 호출 연동, 주문자만 꺼낼 수 있는 수령 방식을 설명하고 입주민 만족도 조사 결과를 회사가 밝혔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-966",
      "org": "지디넷코리아 (신영빈)",
      "title": "로봇이 문앞까지 택배 가져다 주는 미래 곧 온다",
      "published": "2025-01-19",
      "url": "https://zdnet.co.kr/view/?no=20250119062609",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "삼성물산×뉴빌리티, 현대건설×모빈, 롯데글로벌로지스×로보티즈의 공동주택 배송로봇 추진 현황을 다룬다. 지하주차장→공동출입문→엘리베이터→세대 현관 이동 경로와 규제혁신 로봇 실증사업을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-967",
      "org": "AI타임스",
      "title": "실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행",
      "published": "2023-11-16",
      "url": "https://www.aitimes.com/news/articleView.html?idxno=155217",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "개정 지능형로봇법의 실외이동로봇 정의(500kg·15km/h 이하), 16개 시험항목 운행안전인증, 보험 가입 의무, 도로교통법상 보행자 지위를 정리한 보도자료 기사다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-968",
      "org": "MIT Technology Review (Eileen Guo)",
      "title": "A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?",
      "published": "2022-12-19",
      "url": "https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "iRobot 개발용 Roomba J7 이 가정에서 찍은 이미지가 Scale AI 를 거쳐 외주 라벨링 작업자에게 넘어가 SNS 에 게시된 경위를 추적한 탐사 보도다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크",
      "title": "'로봇청소기' 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한국소비자원·KISA 의 로봇청소기 6종 40개 항목 보안 조사 결과(사진 열람·카메라 강제 활성화·개인정보 조회 취약점)와 정부·기업 대응을 정리했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-970",
      "org": "매일신문",
      "title": "사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인",
      "published": "2025-10-06",
      "url": "https://www.imaeil.com/page/view/2025100618362463025",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한국소비자원의 로봇청소기 6개 모델 40개 항목 조사에서 일부 중국산 제품의 카메라 강제 활성화·초기 비밀번호 미흡 취약점이 확인됐다고 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-971",
      "org": "Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판)",
      "title": "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation",
      "published": "2024-03-14",
      "url": "https://arxiv.org/abs/2403.09227",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "설문으로 고른 일상 활동 1,000개를 50개 장면·9,000여 물체로 OmniGibson 에 구현한 벤치마크다. 긴 과제와 복잡한 조작이 최신 로봇 학습에도 어렵다고 보고한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-972",
      "org": "Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30)",
      "title": "Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs",
      "published": "2026-06",
      "url": "https://journal.ksles.org/articles/xml/g9G5/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "공동주택 거주자 63명과 업계 65명을 비교해 서비스 로봇 수용 태도·우려·기술 요구의 차이를 분석한 국내 학술지 논문이다(309~322쪽).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-973",
      "org": "The Robot Report (Mike Oitzman)",
      "title": "NEO humanoid designed for household use, available for preorder",
      "published": "2025-10-30",
      "url": "https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "1X 의 가정용 휴머노이드 NEO 사전 주문(가격·구독·배송 시기)을 전한다. 원격 조작자가 안내하는 전문가 모드와 금지 구역·얼굴 흐림 같은 사생활 기능을 회사 발표로 소개한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-974",
      "org": "LG Electronics USA",
      "title": "LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE \"ZERO LABOR HOME\" AT CES 2026",
      "published": "2026-01-06",
      "url": "https://www.lg.com/us/press-release/lg-cloid-home-robot",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "가정용 로봇 LG 클로이드의 하드웨어 구성(7자유도 팔 2개·다섯 손가락·바퀴 기반)과 CES 2026 가사 시연, VLM·VLA 모델, ThinQ·ThinQ ON 연동을 설명한 보도자료다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-975",
      "org": "한국경제 (김익환)",
      "title": "배송·주차·청소까지…로봇 아파트 뜬다",
      "published": "2026-09-27",
      "url": "https://www.hankyung.com/article/2026092776141",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "국토부가 마련하고 한병도 의원이 대표 발의한 이동로봇 특별법안을 다룬다. 입주자대표회의 의결을 통한 아파트 로봇 도입과 공동현관·엘리베이터 통신 연동 절차 표준화 등을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-976",
      "org": "정보통신신문 (김연균)",
      "title": "로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’",
      "published": "2024-07-18",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=123976",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "공동주택 로봇 택배의 세 가지 집하 시나리오, 관제실·거주자 통신 흐름, 로보티즈 개미의 승강기 버튼 조작 시험, 보도 충돌·영상 촬영 고지 문제를 다룬 기획 기사다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-977",
      "org": "Connectivity Standards Alliance (CSA)",
      "title": "Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board",
      "published": "2023-10-23",
      "url": "https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Matter 1.2 의 새 장치 유형 9종(로봇청소기·냉장고·식기세척기·세탁기 등)을 알리는 표준 기관 공식 발표다. 로봇청소기의 원격 시작·청소 모드·상태 정보 지원을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-978",
      "org": "CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관)",
      "title": "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)",
      "published": "2023-03-14",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이동형 영상정보처리기기의 공개 장소 촬영 제한·예외, 민감 장소 촬영 금지, 불빛·소리·안내판 표시 의무를 정한 조문이다(법률 제19234호, 시행 2023-09-15). 민간 법령 DB 게재본이며 국가법령정보센터 원문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-979",
      "org": "미디어펜 (조태민)",
      "title": "로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도",
      "published": "2026-09-20",
      "url": "https://www.mediapen.com/news/view/1124680",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "현대건설 배송로봇의 이동 경로와 승강기 연동 기능(자동 호출·목적층 재호출·정원 초과 판단), 삼성물산의 공동현관·승강기 연결을 다룬다. 공동출입문·승강기 연동 실패 시 운행이 끊긴다는 제약도 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
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
      "rationale": "섹션 3: f12(거주자 95.2% 긍정·자녀 가구 단지 내 배송 선호), f13·f14(가정 로봇 영상 유출·보안 취약점이 보여 주는 사생활 위험), f11(국회 발의된 이동로봇 특별법안) / 섹션 4: f8(이동형 영상정보처리기기 — 용어집 기존), f10(실외이동로봇 운행안전인증), f15(Matter), f18(VLA), f19(원격 조작·금지 구역) / 섹션 5(현장 유형 모두 가정): 공동주택 배송 — f1(래미안 리더스원), f2(만족도, 벤더 주장), f3·f4(현대건설), f5(롯데글로벌로지스·로보티즈), f6(집하 방식); 세대 안 가사 — f14·f15(로봇청소기), f18(LG 클로이드, 벤더 주장), f19(1X NEO, 벤더 주장); 사생활 사고 — f13(iRobot); 작업 형태 지도 f20, 여섯 항목 정리 f21 / 섹션 6: 공동현관·승강기 연동 f1·f4·f5(버튼 조작 팔 대 시스템 연동), 집하 방식과 관제 흐름 f6, 수령 인증 f1, 원격 조작 보조와 사생활 기능 f19, 가전 연동 f15·f16·f18 / 섹션 7: f15·f16(Matter 1.2), f8·f9(개인정보 보호법 제25조의2), f10(개정 지능형로봇법), f11(이동로봇 특별법안, 발의 단계임을 명시) / 섹션 8: f17(BEHAVIOR-1K), f12(공동주택 서비스 로봇 인식 연구), f13(MIT Technology Review 탐사 보도) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66 / 섹션 11: open_questions_new 5건(기존 열린 질문 없음). f2·f18·f19 는 벤더 주장 병기 필수. 다음 실행 후보: 53. 개인정보·영상 데이터 페이지에 f8·f9·f13·f14 반영, 22. 설비·건물 시스템 연동 페이지에 f4·f11 반영, 59. 법·규제·보험·라이선스 페이지에 f10·f11 반영, 21. 상호운용 표준·적합성 페이지에 f15 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "매터",
      "term_en": "Matter (Connectivity Standards Alliance smart home standard)",
      "definition": "Connectivity Standards Alliance 가 관리하는 스마트홈 기기 상호운용 표준으로, 1.2 판(2023-10)부터 로봇청소기를 장치 유형으로 정의해 제조사가 달라도 시작·청소 모드·상태 정보를 같은 방식으로 다루게 한다."
    },
    {
      "term_ko": "실외이동로봇 운행안전인증",
      "term_en": "Outdoor Mobile Robot Operational Safety Certification",
      "definition": "2023-11-17 시행된 개정 지능형로봇법에 따라 질량 500kg·시속 15km 이하의 배송·순찰 로봇이 운행구역 준수·횡단보도 통행 등 16개 시험항목을 통과해야 받는 인증으로, 인증받은 로봇은 보도를 보행자 지위로 다닐 수 있다."
    },
    {
      "term_ko": "비전 언어 행동 모델",
      "term_en": "Vision-Language-Action Model (VLA)",
      "definition": "카메라 영상과 언어 지시를 입력으로 받아 로봇의 물리 동작을 직접 출력하도록 학습한 모델로, 가정용 로봇이 우유 꺼내기·빨래 개기 같은 조작 가사를 수행하는 데 쓰인다고 발표되고 있다."
    },
    {
      "term_ko": "원격 조작",
      "term_en": "Teleoperation",
      "definition": "사람이 떨어진 곳에서 로봇의 센서 영상을 보며 로봇을 직접 조종하는 방식으로, 가정용 로봇에서는 로봇이 스스로 못 하는 작업을 원격 조작자가 대신 수행하며 학습 데이터를 모으는 데 쓰여 사생활 통제(승인·금지 구역·얼굴 흐림)가 함께 논의된다."
    }
  ],
  "open_questions_new": [
    "세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? | 관련 영역: 65. 가정·공동주택, 53. 개인정보·영상 데이터 | 근거: f9 | 종류: 일반",
    "이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? | 관련 영역: 65. 가정·공동주택, 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성 | 근거: f11 | 종류: 일반",
    "한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? | 관련 영역: 65. 가정·공동주택, 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반",
    "공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가? | 관련 영역: 65. 가정·공동주택, 17. 작업 대상·자산 식별과 인계 추적, 23. 업무 시스템 연동 | 근거: f1 | 종류: 일반",
    "원격 조작자가 가정 로봇을 대신 조종하는 방식(1X NEO 전문가 모드 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? | 관련 영역: 65. 가정·공동주택, 53. 개인정보·영상 데이터, 58. 다사업자 책임·계약·데이터 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 3,
    "unverified": [
      "f2 삼성물산 만족도 95%(113명)·필요성 99%·유료 이용 74%는 회사 발표(벤더 주장)이며 독립 확인 없음",
      "f4 현대건설 승강기 연동 기능(자동 호출·재호출·정원 초과 판단)은 미디어펜 단독",
      "f5 롯데글로벌로지스 실증의 기간·규모와 개미의 실제 단지 내 버튼 조작 운영 여부 미확인",
      "f6·f7 집하 방식과 영상 고지 제언은 정보통신신문 단독",
      "f8 개인정보 보호법 조문은 CaseNote 게재본으로 확인했고 국가법령정보센터 원문은 열지 않음",
      "f9 가정 내부 로봇 촬영에 대한 제25조의2 적용 여부는 조문 요건에서 도출한 해석이며 개인정보보호위원회 해석 미확인",
      "f10 지능형로봇법 내용은 AI타임스(보도자료 기사) 단독, 법령 원문 미열람",
      "f11 이동로봇 특별법안은 발의 단계이며 법안 원문·국회 의안 정보 미열람, 통과 여부 미확인",
      "f14 한국소비자원·KISA 보도자료 원문(kca.go.kr·kisa.or.kr)은 인증서 오류로 열지 못함. 발표일은 매일신문 2025-10-06 보도, 바이라인은 조사기간 2025-03~07 로 적어 보도 시점과 조사 시점이 다름",
      "f15 Matter 1.3 이후 판의 로봇 관련 변경(구역 청소 등) 미확인",
      "f18·f19 LG 클로이드·1X NEO 기능은 회사 발표(벤더 주장)이며 출시·실사용 성능 미확인",
      "홈네트워크(월패드) 연동 사례, 가정 돌봄 로봇, 세대 내 로봇청소기 보급률 수치는 이번에 조사하지 못함"
    ],
    "scope_violations": [
      "f23: 배달 앱·택배사 시스템, 공동현관 자동문·승강기 제어반·월패드, 로봇 자율주행·파지·VLA, 개인정보 보호법·지능형로봇법·공동주택관리법 절차는 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어·업종별 조건이므로 '연계 대상: '으로 표시함",
      "f18·f19: VLA·원격 조작·빨래 개기 같은 조작 능력은 로봇 자체 지능·제어이므로 이 영역에서는 가사 로봇 현황과 사생활 제약의 근거로만 제안함",
      "f15·f16: Matter 는 가전 제어 표준이며 ROP 는 연동 대상으로만 다룬다. 21. 상호운용 표준·적합성과 짝으로 제안함",
      "f4·f11: 공동현관·승강기 통신 연동은 22. 설비·건물 시스템 연동의 핵심이므로 이 영역에서는 공동주택 배송의 제약·사례 근거로만 제안함",
      "f10: 보도 통행 규정은 66. 실외 영역과 겹치므로 단지 도로를 지나는 배송의 제약 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 14,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 14회/30, 신규 출처 15건/15(ref-965~ref-979, 예약 구간 ref-965~ref-994 안)로 출처 상한에 도달했다. 그래서 Lutz·Schöttler·Hoffmann(2019) 소셜 로봇 사생활 검토(원문 PDF 프록시 거부), 이투데이(2026-08-12) 이동로봇 특별법 설명회 기사(43개 기업 참석), 파이낸셜뉴스(2026-09-08) 현대건설–한국교통안전공단 공동주택 모빌리티 안전기준 MOU 기사, 개인정보보호위원회 로봇청소기 점검 기사는 열었거나 찾았으나 넣지 않았다. 번호 충돌 주의: 같은 날 이전 실행 2026-09-29-16 브리프가 ref-965 를 Karlsen 외 Frontiers 논문(식당 서비스 로봇)에 이미 부여했다고 적혀 있다. 이번 실행 컨텍스트가 ref-965~ref-994 를 이 실행 전용으로 예약했으므로 지시대로 ref-965 부터 썼다. 퍼블리셔가 병합할 때 ref-965 충돌을 확인해야 한다. 또 이전 브리프들은 국가기술표준원 KS 로봇 승강기 탑승 보도자료(KDI 게재)를 ref-945(2026-09-29-16)와 ref-948(2026-09-29-13)로 서로 다르게 적어, 이번에는 그 출처를 재사용하지 않았다. 원문 열람: 15건 모두 webfetch 로 본문을 열었다. 한국소비자원·KISA 보도자료는 인증서 오류로 열지 못해 기사 두 건(바이라인·매일신문)으로 교차 확인했다. 한 기사(이투데이)는 요약 모델이 없는 공동주택 조항을 만들어 내어, 원문 문장을 다시 추출해 확인한 뒤 finding 에서 뺐다. 교차 확인 3건: f1 삼성물산 세대 현관 배송 사실(뉴스룸·지디넷코리아·미디어펜), f3 현대건설 이동 경로(지디넷코리아·미디어펜), f14 로봇청소기 보안 조사(바이라인·매일신문). 신뢰도 high finding 은 없다. 벤더 주장 finding 3건(f2 삼성물산 만족도, f18 LG 클로이드, f19 1X NEO). 분류 원문 핵심 질문(가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가)에는 작업 형태 f20, 여섯 항목 f21, 직접 범위 f22, 연계 대상 f23 으로 답했다. 결론은 다음과 같은 추정이다. 공동주택 배송은 공동현관·승강기 연동과 수령 인증이 운영 성패를 가르고 제도(특별법안의 입주자대표회의 의결·연동 표준화)가 막 정비되는 중이다. 세대 안 조작 가사는 시연·사전 주문·벤치마크 단계이며, 사생활은 촬영 표시·금지 구역·원격 조작 승인·학습 데이터 처리와 기기 보안 문제로 나타난다. 현장 유형은 f8·f10·f24(일반 법령·연결)를 빼고 모두 가정이다. 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 삼성물산·지디넷코리아·AI타임스·바이라인·매일신문·한국생활환경학회지·한국경제·정보통신신문·CaseNote(개인정보 보호법)·미디어펜 열 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(BEHAVIOR-1K 는 54. 시험·형식 검증·벤치마크로만 연결). L. AI·학습 기술 관련(f13 학습 데이터 라벨링, f18 VLA)은 47·44 와 적용 대상인 이 영역 양쪽에 연결했다. 용어집에 이미 있는 이동형 영상정보처리기기·로봇 친화형 건축물 인증·승강기 어댑터는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-17/verification.json

```json
{
  "run_id": "2026-09-29-17",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-965 뉴스룸(2026-01-15) 열람: 공동 현관 자동문 개폐·엘리베이터 호출 연동 해결, 도어 투 도어 상용 서비스, '주문자만 배달음식 픽업이 가능', 요기요 연계 반경 1.2km 130여 곳. ref-966(지디넷코리아 2025-01-19)은 래미안 리더스원 세대 현관 배달 시범 운영을, ref-979(미디어펜 2026-09-20)는 공동현관 자동문·승강기 호출 연결을 따로 전해 독립 교차 확인됨. 다만 시점 서술이 원문과 다르다: 세대 현관 배달은 2024-12 시범 운영(지디넷)과 2025년 실증에서 이미 이뤄졌고, 2026년 확장은 요기요 연계·반경 1.2km 130여 곳으로 가맹점 범위를 넓힌 것이다. '2026-01 단지 인근 서비스를 세대 현관까지 확장'이라는 표현은 고쳐야 한다(required_fixes)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 뉴스룸 원문에 '서비스 만족도 95%, 서비스 필요성 공감 99%, 유료서비스 이용 의사 74% (서비스를 이용한 입주민 113명 대상 조사)'가 있고, 조사 시점은 '실증기간'이라고만 적혀 있다. 회사 발표이므로 [추정]과 '벤더 주장' 병기를 유지한다. 외부인 출입 갈등·이동수단 위험 감소도 회사 설명이다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 지디넷코리아(2025-01-19): 현대건설×모빈 로봇을 '오는 6월 준공 예정인 디에이치 대치 에델루이'에 처음 적용할 예정이며 도로·지하 주차장·공동 출입문·엘리베이터·세대 현관 전 구간을 이동한다. 미디어펜(2026-09-20): 강남 대치지구에서 같은 경로의 배송로봇을 상용화했다. 발행 주체가 달라 독립 교차 확인으로 본다. 모빈이라는 이름은 지디넷에만 있다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 미디어펜 원문에 승강기 연동의 자동 호출·목적층 재호출·정원 초과 판단이 있고, '공동출입문이 열리지 않거나 승강기를 호출할 수 없으면 단지 내부에서 운행이 끊긴다'는 문제와 동선·통신망·관제시스템·충전시설을 설계에 반영해야 한다는 내용도 있다. 단일 기사이므로 본문에 '미디어펜에 따르면'으로 출처를 밝혀야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 지디넷코리아: 롯데글로벌로지스가 로보티즈와 '경기도 고양·파주 아파트 단지에서 택배 배송로봇 실증사업을 진행했다'고 하며, 한국로봇산업진흥원 규제혁신 사업 참여도 적는다. 정보통신신문(2024-07-18): 로보티즈 '개미' 시연을 마쳤고 '로봇 팔을 활용한 승강기 버튼 직접 조작 탑승 및 하차 테스트'를 했다. 두 출처는 서로 다른 사실을 뒷받침하므로 교차 확인은 아니다. 실증 기간·규모와 실제 단지 운영 여부는 미확인이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 정보통신신문(입력 2024-07-18, 수정 2024-07-23. 페이지 상단의 2026-09-29는 사이트 날짜 표시다) 원문에 세 가지 집하 시나리오와 '송장번호를 인식시켜 관제실로 물품정보를 전송하면' 관제실이 거주자와 통신해 로봇을 배송시키는 흐름이 있다. 다만 세 시나리오와 서비스 정의는 기사가 LH토지주택연구원(LHRI) 자료를 인용한 것이므로 본문에서 그 출처를 밝혀야 한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 원문: '보도가 좁은 공간에서 배달로봇과 행인이 출동할 경우 …', '통신장애가 올 경우 급정지로 인한 사고도 배제할 수 없다', '불빛, 소리, 안내판 등을 통해 촬영 사실을 고지…', '업무목적 달성에 불필요한 영상은 즉시 삭제하도록'. 기사 속 인용·제언이다. 보도 통행 위험은 66. 실외와 겹치므로 공동주택 단지 배송의 제약 근거로만 쓴다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CaseNote 게재 조문(법률 제19234호, 2023-03-14 개정, 2023-09-15 시행): 제1항은 업무 목적 운영자의 공개된 장소 촬영 제한과 예외, 제2항은 목욕실·화장실·발한실·탈의실 등 내부를 볼 수 있는 곳의 촬영 금지와 인명구조 등 예외, 제3항은 불빛·소리·안내판 등의 표시 의무를 정한다. 발행 기관 원문(국가법령정보센터)이 아니라 민간 법령 DB 게재본이므로 각주와 본문에 이를 밝혀야 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "조문 요건('업무를 목적으로', '공개된 장소')에서 도출한 해석이며 [추정]을 유지한다. 개인정보보호위원회 해석은 미확인이다. 법 해석이 아니라 조문 문언에 기댄 리서치 해석임을 본문에 밝히고, 열린 질문 1과 짝을 이루게 한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. AI타임스(2023-11-16): 2023-11-17 시행, 질량 500kg·시속 15km 이하, 운행구역 준수·횡단보도 통행 등 16가지 시험항목의 운행안전인증, 보험·공제 가입, 개정 도로교통법상 보행자 지위, 범칙금 3만원. 정보통신신문(ref-976)도 뉴빌리티 뉴비의 실외이동로봇 운행안전인증 '16개 항목 평가'를 적어 16개 항목은 부분적으로 뒷받침되지만, ref-976 이 f10 의 source_ids 에 없으므로 cross_checked 는 false 로 둔다. 법령 원문은 미열람이며 보도자료 기사 기반이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 한국경제(2026-09-27, 김익환): 한병도 의원 발의, 건축법·국토계획법·공동주택관리법·주차장법 등에 흩어진 이동로봇 규제를 한꺼번에 손질, 입주자대표회의 의결로 배송·보안·순찰·청소·충전·주차로봇 도입, 공동현관 통과·엘리베이터 이용을 위한 통신 시스템 연동 절차의 간소화·표준화, 9월 초 발의. 법안 내용에 대한 [사실]로만 유지하고, 발의 단계이며 국회 통과·시행은 미확인임을 본문에 반드시 적는다. 의안 원문은 미열람이다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 한국생활환경학회지 논문 페이지 열람: 거주자 63명·업계 65명, 긍정 95.2% 대 실제 체험 의향 88.9%, 자녀 가구의 단지 내 배송 우선 p=0.005, 기술 요구 차이 p=0.036, 거주자는 충돌 방지·개인정보 보호·사용자 인터페이스를, 업계는 시스템 통합·운영 안정성을 중시, 연령별 차이는 유의하지 않음. '23개 기관'은 이번 열람 요약에서 따로 확인하지 못했다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. MIT Technology Review(2022-12-19, Eileen Guo): 개발용 Roomba J7, 유료 수집자·직원의 동의, 'video recording in progress' 스티커, Scale AI 를 통한 베네수엘라 긱 워커, 스크린숏 15장, Facebook·Discord 게시, 화장실의 여성·복도의 아이. 소비자 제품이 아닌 개발용 기기이고 동의한 사람의 집이라는 조건을 본문에 유지해야 한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 바이라인네트워크(2025-10-31)와 매일신문(2025-10-06)이 각각 6개 모델·40개 항목 조사를 전한다. 매일신문은 국산(삼성·LG) 2종과 중국 4종(드리미·로보락·에코백스·나르왈)을, 바이라인은 나르왈·드리미·에코백스의 사진 열람·카메라 강제 활성화 취약점과 게시판 ID 로 이름·전화번호를 조회할 수 있는 문제를 적는다. 두 기사는 같은 정부 발표를 옮긴 2차 자료다. 한국소비자원·KISA 원 보도자료는 미열람이다. '일부 중국 브랜드'라는 표현은 적절하다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CSA(2023-10-23): Matter 1.2 의 새 장치 유형 9종(냉장고·룸 에어컨·식기세척기·세탁기·로봇청소기·연기/일산화탄소 경보기·공기질 센서·공기청정기·팬). 로봇청소기는 원격 시작·진행 알림, 청소 모드(건식/습식), 브러시·오류·충전 상태를 지원하고 지도·구역 청소는 언급하지 않는다. 최신성: 이후 판(Matter 1.4)에 로봇청소기용 Service Area 클러스터(구역·방 단위 청소)가 더해졌다는 2차 보도가 검색된다(미확인). 따라서 본문은 반드시 '1.2 발표(2023-10) 기준'으로 한정해야 한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "1.2 발표 목록에서 도출한 [추정]이며 유지한다. 다만 이후 판에서 구역 청소 기능이 더해졌을 수 있어(2차 보도, 미확인) '로봇청소기의 시작·상태·모드'라는 범위는 1.2 기준이다. 물건 운반·조작 같은 다른 가사 로봇 능력이 없다는 판단도 1.2 발표 범위에 한정해 쓴다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2403.09227(2024-03-14 제출, CoRL 2022 예비판): 'what do you want robots to do for you?' 설문, 활동 1,000개, 집·정원·식당·사무실 등 50개 장면, 물체 9,000여 개, OmniGibson, 'long-horizon and dependent on complex manipulation skills', 모바일 매니퓰레이터의 시뮬레이션→실물 전이 초기 연구."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. LG Electronics USA 보도자료(CES 2026): 7자유도 팔, 독립 구동 다섯 손가락 손, 바퀴 기반 자율주행, VLM·VLA 가 'tens of thousands of hours of household task data'로 학습됨, ThinQ 연동, 출시일·가격 없음. 회사 발표이므로 [추정]과 '벤더 주장' 병기를 유지한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "대체로 확인. The Robot Report(2025-10-30, Mike Oitzman): 사전 주문 2만 달러(보증금 200달러) 또는 월 499달러, 2026년 미국 배송, 'owners could schedule a 1X teleoperator to guide it', 'no go' 구역·얼굴 흐림, 초기 작업(문 열기·물건 가져오기·조명 끄기)과 빨래 개기·선반 정리. 그러나 인용 출처 본문에는 '전문가 모드(Expert Mode)'라는 이름이 없다. 이 이름을 빼고 '원격 조작자를 예약해 안내하게 하는 기능'으로 서술해야 한다. 벤더 주장 병기는 유지한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "finding 들을 작업 형태 네 가지로 묶은 [추정] 종합이다. 각 형태의 근거 finding 이 모두 확인됐다. 조작 가사(3)는 시연·사전 주문·벤치마크 단계라는 단서를 유지한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "여섯 항목 대응은 [추정]이며 근거 finding 이 확인됐다. 수행 자원의 원격 조작자(f19)는 벤더 주장에 기댄다는 점, 수령 인증의 구체 방식은 미확인이라는 점을 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 '확인한 국내 사례는 모두 건설사 한 곳과 로봇 업체 한 곳의 짝'은 부정확하다. 롯데글로벌로지스(f5)는 건설사가 아니라 물류사다. '건설사 또는 물류사 한 곳과 로봇 업체 한 곳'으로 고쳐야 한다. '원격 조작 승인'은 출처의 '원격 조작자 예약'을 ROP 제약으로 해석한 것임을 [추정] 문맥에 둔다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상'으로 표시돼 있고, 분류 원문 19장의 다섯 경계 가운데 상위 업무 시스템·로봇 자체 지능·제어·시설·설비 제어·업종별 조건에 맞게 대응시켰다. 월패드 연동 사례는 미확인임을 유지한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 목록의 세부영역 번호와 원문 명칭(16·17·20·21·22·23·31·44·47·51·52·53·54·59·60·66)이 부록 A 와 일치한다. L. AI·학습 기술 교차 규칙(44·47 과 적용 대상 양쪽 연결)을 지켰다."
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
      "ref-965 번호 충돌: 같은 날 2026-09-29-16 브리프(64. 상업 시설)가 ref-965 를 Karlsen 외 Frontiers 논문(식당 서비스 로봇)에 부여했고, 이번 브리프는 같은 id 를 삼성물산 뉴스룸에 부여했다. URL 이 달라 퍼블리셔의 URL 기준 병합으로는 풀리지 않으므로 퍼블리셔가 게시 전에 번호를 다시 매겨야 한다(리서치 self_check.limits 에도 기록됨).",
      "f10(실외이동로봇 운행안전인증·보도 보행자 지위)과 f7(보도 충돌 위험)은 66. 실외(현재 seed)의 핵심 내용과 겹친다. 이 페이지에서는 단지 도로를 지나는 배송의 제약 근거로만 쓰고 66. 실외로 연결한다.",
      "f4·f11(공동현관·승강기 통신 연동)은 22. 설비·건물 시스템 연동, f15(Matter)는 21. 상호운용 표준·적합성, f8·f13·f14 는 53. 개인정보·영상 데이터와 겹친다. 연결만 하고 본문을 옮겨 쓰지 않는다. 기존 게시 페이지와 모순되는 주장은 없다.",
      "이동형 영상정보처리기기는 용어집에 이미 있다(mobile-video-information-processing-device). 새로 등록하지 않고 기존 용어를 링크한다."
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
    "f1: 시점 서술을 고친다. '2026-01 단지 인근까지 운영하던 서비스를 세대 현관까지 확장'이 아니라 '세대 현관까지 가는 도어 투 도어 배달은 2024-12 시범 운영(ref-966)과 2025년 실증을 거쳐 구축됐고, 2026년부터 요기요 연계로 반경 1.2km 식음료점 130여 곳으로 범위를 넓혔다(ref-965)'로 쓴다. 이유: 뉴스룸 원문은 실증을 '지난 해' 마쳤다고 적고, 2026년 확장 대상은 가맹점 범위다.",
    "f2·f18·f19: 본문에 [추정] 태그와 '벤더 주장'을 함께 적는다. f2 에는 조사 시점이 '실증기간'으로만 표기돼 있다는 점을 덧붙인다. 이유: 회사 발표이며 독립 확인이 없다.",
    "f19: '전문가 모드(Expert Mode)'라는 이름을 본문·용어 정의·열린 질문(5번째 항목의 '1X NEO 전문가 모드 등')에서 빼고, '소유자가 1X 원격 조작자를 예약해 로봇을 안내하게 하는 기능'으로 쓴다. 이유: 인용 출처 ref-973 본문에 그 이름이 없다.",
    "f6: 세 가지 집하 시나리오와 '관제실이 거주자와 통신해 로봇을 배송'하는 서비스 정의는 '정보통신신문이 LH토지주택연구원 자료를 인용해 전한 것'으로 출처를 밝힌다. 이유: ref-976 원문이 LHRI 를 출처로 적는다.",
    "f4: 본문 문장에 '미디어펜(2026-09-20)에 따르면'을 유지하고, 승강기 연동 기능(자동 호출·목적층 재호출·정원 초과 판단)이 단일 기사 근거임을 드러낸다.",
    "f8: 13. 참고 자료의 ref-978 각주와 7절 본문에 '민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람'을 밝히고, 법률 제19234호·시행 2023-09-15 기준일을 남긴다.",
    "f9: 본문에서 '조문 문언(업무 목적·공개된 장소)에서 도출한 해석이며 개인정보보호위원회 해석은 확인하지 못했다'고 밝히고, 11절 열린 질문 1번과 연결한다. 법 해석처럼 단정하지 않는다.",
    "f10: 7절에서 '보도자료 기사(AI타임스 2023-11-16) 기준, 법령 원문 미열람'임을 밝히고, 보도 통행 규정은 66. 실외와 연결하며 이 페이지에서는 단지 도로 배송의 제약으로만 쓴다.",
    "f11: 모든 서술에 '2026-09 초 발의된 법안(발의 단계)이며 국회 통과·시행 여부는 확인되지 않았다'를 붙이고, 확정된 제도처럼 쓰지 않는다('시행되면 …할 수 있게 된다' 형식).",
    "f14: 두 기사가 같은 정부 조사 발표를 옮긴 2차 자료이고 한국소비자원·KISA 원 보도자료는 미열람임을 각주·본문에 밝힌다. 취약점이 확인된 대상은 '일부 중국 브랜드 제품'으로 두고 브랜드별로 단정하지 않는다.",
    "f15·f16: Matter 서술을 'Matter 1.2 발표(2023-10-23) 기준'으로 한정하고, '이후 판의 로봇청소기 관련 변경은 확인하지 못했다'를 명시한다. f16 의 '구역·운반·조작 능력 부재' 판단을 현재 Matter 전반으로 일반화하지 않는다. Matter 1.3 이후 판(특히 1.4 의 Service Area 클러스터 여부)의 확인은 additional_research_requests 로 넘긴다.",
    "f13: 사례를 '미국 기업 iRobot 의 개발용 기기, 동의서에 서명한 유료 수집자·직원의 집'이라는 조건과 함께 서술하고, 소비자 제품의 일반 사례처럼 쓰지 않는다.",
    "f5: 롯데글로벌로지스·로보티즈 실증의 기간·규모는 미확인이고, 개미의 승강기 버튼 조작은 '시연·시험을 마친 단계'라고 쓴다. 상용 운영처럼 서술하지 않는다.",
    "f22: '확인한 국내 사례는 모두 건설사 한 곳과 로봇 업체 한 곳의 짝'을 '건설사 또는 물류사 한 곳과 로봇 업체 한 곳의 짝'으로 고친다. 이유: 롯데글로벌로지스는 물류사다.",
    "인용: 출처당 직접 인용은 1회만 쓴다. ref-965(주문자만 픽업·만족도 문구)와 ref-976(불빛·소리·안내판 문구, 불필요한 영상 즉시 삭제 문구)은 각각 한 구절만 직접 인용하고 나머지는 재서술한다.",
    "5. 적용 사례: 모든 사례의 현장 유형을 '가정'으로 명시하고 여섯 항목(f21)에 놓는다. site_matrix_updates 의 site_type 은 '가정'만 쓴다. f8·f10(일반 법령)은 적용 사례로 세우지 않고 7절에 둔다.",
    "용어: 이동형 영상정보처리기기는 새로 등록하지 않고 기존 용어집 항목(mobile-video-information-processing-device)을 링크한다. 새 후보 4개(매터·실외이동로봇 운행안전인증·비전 언어 행동 모델·원격 조작)는 등록하되, 매터 정의에는 '1.2 판 기준' 표현을 유지한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 3건(f1 삼성물산 세대 현관 배달, f3 현대건설 이동 경로, f14 로봇청소기 보안 조사). 강등: 없음. 대신 f1 시점 서술 정정, f19 '전문가 모드' 명칭 삭제, f22 '건설사' → '건설사 또는 물류사' 정정, f15·f16 을 Matter 1.2 기준으로 한정하도록 지시했다. 원문 미열람 출처: 없음. 15건 모두 검증 단계에서 다시 열었다. 다만 f8 은 민간 법령 DB(CaseNote) 게재 조문이고 국가법령정보센터 원문은 열지 않았다. f10 은 보도자료 기사 기준이며 법령 원문은 열지 않았다. f14 는 한국소비자원·KISA 원 보도자료를 열지 못해 기사 두 건으로 확인했다. 주의: 벤더 주장 3건(f2 삼성물산 만족도 95%, f18 LG 클로이드, f19 1X NEO)은 [추정]으로 둔다. f11 이동로봇 특별법안은 발의 단계이며 국회 통과·시행은 확인되지 않았다. Matter 는 1.2 발표 기준이며, 이후 판(1.4 Service Area 클러스터)에서 구역 청소가 더해졌다는 2차 보도가 있어 재확인이 필요하다. 국내 공동주택 배송 사례는 모두 기사·회사 발표에 기대며, 여러 제조사 로봇을 한 단지에서 묶은 공개 사례는 확인되지 않았다. ref-965 는 같은 날 2026-09-29-16 이 다른 출처(Karlsen 외)에 부여한 id 와 충돌하므로 퍼블리셔가 게시 전에 번호를 다시 매겨야 한다. 정정 요청 없음. 기존 열린 질문 해결 없음. 검증 검색 1회를 썼다(리서치 14회와 합쳐 15회/30).",
  "retry_reason": null
}
```

### runs/2026-09-29-17/pages.json

```json
{
  "run_id": "2026-09-29-17",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "가정·공동주택의 로봇 작업은 단지 배송·세대 안 청소·조작 가사·단지 공용 서비스의 네 형태로 나타나며, 거주자 수용성·사생활 사고·공동현관·승강기 연동과 발의 단계의 특별법안이 운영을 좌우한다. [추정][^ref-965][^ref-972][^ref-968]",
      "planned_findings": [
        "f20",
        "f12",
        "f13",
        "f14",
        "f4",
        "f11"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 700,
      "summary": "이동형 영상정보처리기기, 실외이동로봇 운행안전인증, 매터(1.2 판 기준), VLA, 원격 조작, 도어 투 도어 배달, 단지 집하 방식을 정리한다. [사실][^ref-978][^ref-967][^ref-977]",
      "planned_findings": [
        "f8",
        "f10",
        "f15",
        "f18",
        "f19",
        "f1",
        "f6"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1400,
      "summary": "현장 유형 가정의 세 사례(공동주택 음식 배송, 단지 택배 배송, 세대 안 청소·가사 로봇)를 여섯 항목으로 채운다. [추정][^ref-965][^ref-976][^ref-973]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f13",
        "f14",
        "f15",
        "f18",
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 700,
      "summary": "공동현관·승강기는 시스템 연동과 로봇팔 버튼 조작 두 방식이 확인되고, 단지 집하·관제 흐름, 수령 인증, 원격 조작 보조·사생활 기능, Matter 1.2 기반 가전 연동이 제시된다. [사실][^ref-979][^ref-976][^ref-977]",
      "planned_findings": [
        "f1",
        "f4",
        "f5",
        "f6",
        "f11",
        "f15",
        "f16",
        "f18",
        "f19",
        "f7"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 600,
      "summary": "Matter 1.2, 개인정보 보호법 제25조의2, 개정 지능형로봇법 실외이동로봇 운행안전인증, 발의 단계의 이동로봇 특별법안을 기준일·원문 열람 여부와 함께 정리한다. [사실][^ref-977][^ref-978][^ref-967][^ref-975]",
      "planned_findings": [
        "f8",
        "f9",
        "f10",
        "f11",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 400,
      "summary": "BEHAVIOR-1K, 공동주택 서비스 로봇 인식 연구, iRobot 영상 유출 탐사 보도, 로봇청소기 보안 조사 보도, 정보통신신문 기획 기사를 소개한다. [사실][^ref-971][^ref-972][^ref-968][^ref-969]",
      "planned_findings": [
        "f17",
        "f12",
        "f13",
        "f14",
        "f6"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 500,
      "summary": "ROP는 요청 수신·배정, 공동현관·승강기 예약·호출, 수령 확인 반환, 사생활 제약 반영을 맡고, 배달 앱·택배사, 승강기·자동문·월패드, 로봇 자율주행·VLA, 법령 판단은 연계 대상으로 둔다. [추정][^ref-965][^ref-979][^ref-978]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 350,
      "summary": "설비·업무 시스템 연동, 개인정보·보안, AI·학습 기술, 법·수용성, 실외 영역 16개와 연결한다. [추정][^ref-979][^ref-978][^ref-974][^ref-972]",
      "planned_findings": [
        "f24"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "section": "11. 열린 질문",
      "budget_chars": 350,
      "summary": "세대 안 촬영의 법 적용, 공동현관·승강기 연동 표준, 다제조사 단지 관제, 수령 인증 방식, 원격 조작 규율의 다섯 질문을 올린다.",
      "planned_findings": [
        "f9",
        "f11",
        "f22",
        "f1",
        "f19"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/home-and-apartment.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 공동주택 음식 배송·단지 택배 배송·세대 안 청소·가사 로봇 세 사례(현장 유형 가정)를 여섯 항목으로 정리, 공동현관·승강기 연동·집하 방식·수령 인증·사생활 기능·Matter 1.2, 관련 법령·법안, 책임 경계, 연결 영역 16개, 열린 질문 5건, 각주 15건, 1차 수정 지시 17건 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,508자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"6. 대표 접근법과 기술\" 절(1,202자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"4. 핵심 개념과 용어\" 절(1,119자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"8. 대표 연구와 자료\" 절(949자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(885자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"11. 열린 질문\" 절(858자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area65-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 65. 가정·공동주택 의 \"3. 왜 중요한가\" 절(826자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 65. 가정·공동주택 | 섹션 3~11 신규 작성(seed → draft): 공동주택 음식·택배 배송과 세대 안 청소·가사 로봇 세 사례(현장 유형 가정), 공동현관·승강기 연동·수령 인증·사생활 기능·Matter 1.2, 관련 법령·발의 단계 특별법안, 책임 경계, 연결 영역 16개, 열린 질문 5건, 1차 수정 지시 17건 이행 | run 2026-09-29-17",
  "index_updates": {
    "home_recent": "2026-09-29 — 65. 가정·공동주택: 섹션 3~11 신규 작성 — 공동주택 음식·택배 배송과 세대 안 청소·가사 로봇 세 사례를 여섯 항목으로 정리하고 공동현관·승강기 연동, 수령 인증, 사생활 제약(개인정보 보호법 제25조의2), Matter 1.2, 책임 경계를 다뤘다",
    "category_recent": "2026-09-29 — 65. 가정·공동주택: 섹션 3~11 신규 작성(seed → draft) — 현장 유형 가정 사례 3건(래미안 리더스원·현대건설 음식 배송, 롯데글로벌로지스·로보티즈 택배 실증, 로봇청소기·가사 로봇과 사생활), 연결 영역 16개, 열린 질문 5건, 각주 15건",
    "area_recent": "2026-09-29 — 65. 가정·공동주택: 섹션 3~11 신규 작성 — 적용 사례 3건(현장 유형 가정), 공동현관·승강기 연동 두 방식, 단지 집하 방식, 관련 법령·발의 단계 특별법안, 책임 경계 4행, 열린 질문 5건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "matter",
      "term_ko": "매터",
      "term_en": "Matter (Connectivity Standards Alliance smart home standard)",
      "definition": "Connectivity Standards Alliance 가 관리하는 스마트홈 기기 상호운용 표준으로, 1.2 판(2023-10)부터 로봇청소기를 장치 유형으로 정의해 제조사가 달라도 시작·청소 모드·상태 정보를 같은 방식으로 다루게 한다.",
      "description": "1.2 판 발표(2023-10-23) 기준 로봇청소기 장치 유형은 원격 시작·진행 알림, 건식·습식 청소 모드, 브러시·오류·충전 상태를 다루며 이 발표에는 지도·구역 청소가 언급되지 않는다. 이후 판의 로봇청소기 관련 변경은 확인하지 못했다.",
      "related_areas": [
        21,
        65
      ],
      "sources": [
        "ref-977"
      ]
    },
    {
      "action": "new",
      "slug": "outdoor-mobile-robot-operational-safety-certification",
      "term_ko": "실외이동로봇 운행안전인증",
      "term_en": "Outdoor Mobile Robot Operational Safety Certification",
      "definition": "2023-11-17 시행된 개정 지능형로봇법에 따라 질량 500kg·시속 15km 이하의 배송·순찰 로봇이 운행구역 준수·횡단보도 통행 등 16개 시험항목을 통과해야 받는 인증으로, 인증받은 로봇은 보도를 보행자 지위로 다닐 수 있다.",
      "description": "보험(공제) 가입도 요구된다. 보도자료 기사 기준이며 법령 원문은 확인하지 않았다.",
      "related_areas": [
        59,
        65,
        66
      ],
      "sources": [
        "ref-967"
      ]
    },
    {
      "action": "new",
      "slug": "vision-language-action-model",
      "term_ko": "비전 언어 행동 모델",
      "term_en": "Vision-Language-Action Model (VLA)",
      "definition": "카메라 영상과 언어 지시를 입력으로 받아 로봇의 물리 동작을 직접 출력하도록 학습한 모델로, 가정용 로봇이 우유 꺼내기·빨래 개기 같은 조작 가사를 수행하는 데 쓰인다고 발표되고 있다.",
      "description": "LG전자는 CES 2026 에서 가정용 로봇 LG 클로이드가 비전 언어 모델(VLM)과 VLA를 쓴다고 발표했다(벤더 주장).",
      "related_areas": [
        44,
        65
      ],
      "sources": [
        "ref-974"
      ]
    },
    {
      "action": "new",
      "slug": "teleoperation",
      "term_ko": "원격 조작",
      "term_en": "Teleoperation",
      "definition": "사람이 떨어진 곳에서 로봇의 센서 영상을 보며 로봇을 직접 조종하는 방식으로, 가정용 로봇에서는 로봇이 스스로 못 하는 작업을 원격 조작자가 대신 수행하며 학습 데이터를 모으는 데 쓰여 사생활 통제(승인·금지 구역·얼굴 흐림)가 함께 논의된다.",
      "description": "1X는 소유자가 1X 원격 조작자를 예약해 가정용 로봇 NEO를 안내하게 하는 기능을 내세웠다(벤더 주장).",
      "related_areas": [
        31,
        53,
        65
      ],
      "sources": [
        "ref-973"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-965",
      "org": "삼성물산 뉴스룸",
      "title": "삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영",
      "published": "2026-01-15",
      "url": "https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "래미안 리더스원에서 뉴빌리티·요기요와 음식배달로봇을 세대 현관까지 운영한다. 공동현관 자동문·엘리베이터 호출 연동, 주문자만 꺼낼 수 있는 수령 방식을 설명하고 입주민 만족도 조사 결과를 회사가 밝혔다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-966",
      "org": "지디넷코리아 (신영빈)",
      "title": "로봇이 문앞까지 택배 가져다 주는 미래 곧 온다",
      "published": "2025-01-19",
      "url": "https://zdnet.co.kr/view/?no=20250119062609",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "삼성물산×뉴빌리티, 현대건설×모빈, 롯데글로벌로지스×로보티즈의 공동주택 배송로봇 추진 현황을 다룬다. 지하주차장→공동출입문→엘리베이터→세대 현관 이동 경로와 규제혁신 로봇 실증사업을 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-967",
      "org": "AI타임스",
      "title": "실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행",
      "published": "2023-11-16",
      "url": "https://www.aitimes.com/news/articleView.html?idxno=155217",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "개정 지능형로봇법의 실외이동로봇 정의(500kg·15km/h 이하), 16개 시험항목 운행안전인증, 보험 가입 의무, 도로교통법상 보행자 지위를 정리한 보도자료 기사다. 법령 원문은 열지 않았다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-968",
      "org": "MIT Technology Review (Eileen Guo)",
      "title": "A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?",
      "published": "2022-12-19",
      "url": "https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "iRobot 개발용 Roomba J7 이 동의한 유료 수집자·직원의 집에서 찍은 이미지가 Scale AI 를 거쳐 외주 라벨링 작업자에게 넘어가 SNS 에 게시된 경위를 추적한 탐사 보도다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크",
      "title": "'로봇청소기' 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한국소비자원·KISA 의 로봇청소기 6종 40개 항목 보안 조사 결과(사진 열람·카메라 강제 활성화·개인정보 조회 취약점)와 정부·기업 대응을 정리했다. 정부 발표를 옮긴 2차 자료이며 원 보도자료는 열지 못했다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-970",
      "org": "매일신문",
      "title": "사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인",
      "published": "2025-10-06",
      "url": "https://www.imaeil.com/page/view/2025100618362463025",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한국소비자원의 로봇청소기 6개 모델 40개 항목 조사에서 일부 중국산 제품의 카메라 강제 활성화·초기 비밀번호 미흡 취약점이 확인됐다고 전한다. 정부 발표를 옮긴 2차 자료다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-971",
      "org": "Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판)",
      "title": "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation",
      "published": "2024-03-14",
      "url": "https://arxiv.org/abs/2403.09227",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "설문으로 고른 일상 활동 1,000개를 50개 장면·9,000여 물체로 OmniGibson 에 구현한 벤치마크다. 긴 과제와 복잡한 조작이 최신 로봇 학습에도 어렵다고 보고한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-972",
      "org": "Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30)",
      "title": "Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs",
      "published": "2026-06",
      "url": "https://journal.ksles.org/articles/xml/g9G5/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "공동주택 거주자 63명과 업계 65명을 비교해 서비스 로봇 수용 태도·우려·기술 요구의 차이를 분석한 국내 학술지 논문이다(309~322쪽).",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-973",
      "org": "The Robot Report (Mike Oitzman)",
      "title": "NEO humanoid designed for household use, available for preorder",
      "published": "2025-10-30",
      "url": "https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "1X 의 가정용 휴머노이드 NEO 사전 주문(가격·구독·배송 시기)을 전한다. 소유자가 원격 조작자를 예약해 로봇을 안내하게 하는 기능과 금지 구역·얼굴 흐림 같은 사생활 기능을 회사 발표로 소개한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-974",
      "org": "LG Electronics USA",
      "title": "LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE \"ZERO LABOR HOME\" AT CES 2026",
      "published": "2026-01-06",
      "url": "https://www.lg.com/us/press-release/lg-cloid-home-robot",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "가정용 로봇 LG 클로이드의 하드웨어 구성(7자유도 팔 2개·다섯 손가락·바퀴 기반)과 CES 2026 가사 시연, VLM·VLA 모델, ThinQ·ThinQ ON 연동을 설명한 보도자료다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-975",
      "org": "한국경제 (김익환)",
      "title": "배송·주차·청소까지…로봇 아파트 뜬다",
      "published": "2026-09-27",
      "url": "https://www.hankyung.com/article/2026092776141",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "국토부가 마련하고 한병도 의원이 대표 발의한 이동로봇 특별법안(발의 단계)을 다룬다. 입주자대표회의 의결을 통한 아파트 로봇 도입과 공동현관·엘리베이터 통신 연동 절차 표준화 등을 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-976",
      "org": "정보통신신문 (김연균)",
      "title": "로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’",
      "published": "2024-07-18",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=123976",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "LH토지주택연구원 자료를 인용한 공동주택 로봇 택배의 세 가지 집하 시나리오와 관제실·거주자 통신 흐름, 로보티즈 개미의 승강기 버튼 조작 시험, 보도 충돌·영상 촬영 고지 문제를 다룬 기획 기사다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-977",
      "org": "Connectivity Standards Alliance (CSA)",
      "title": "Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board",
      "published": "2023-10-23",
      "url": "https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Matter 1.2 의 새 장치 유형 9종(로봇청소기·냉장고·식기세척기·세탁기 등)을 알리는 표준 기관 공식 발표다. 로봇청소기의 원격 시작·청소 모드·상태 정보 지원을 설명한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-978",
      "org": "CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관)",
      "title": "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)",
      "published": "2023-03-14",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이동형 영상정보처리기기의 공개 장소 촬영 제한·예외, 민감 장소 촬영 금지, 불빛·소리·안내판 표시 의무를 정한 조문이다(법률 제19234호, 시행 2023-09-15). 민간 법령 DB 게재본이며 국가법령정보센터 원문은 열지 않았다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-979",
      "org": "미디어펜 (조태민)",
      "title": "로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도",
      "published": "2026-09-20",
      "url": "https://www.mediapen.com/news/view/1124680",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "현대건설 배송로봇의 이동 경로와 승강기 연동 기능(자동 호출·목적층 재호출·정원 초과 판단), 삼성물산의 공동현관·승강기 연결을 다룬다. 공동출입문·승강기 연동 실패 시 운행이 끊긴다는 제약도 전한다.",
      "cited_by": [
        "docs/categories/site-type-applications/home-and-apartment.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가?",
      "areas": [
        65,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가?",
      "areas": [
        65,
        22,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가?",
      "areas": [
        65,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가?",
      "areas": [
        65,
        17,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가?",
      "areas": [
        65,
        53,
        58
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    },
    {
      "site_type": "가정",
      "item": "완료·인계",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시",
      "title": "65. 가정·공동주택"
    }
  ],
  "standards_updates": [
    {
      "name": "Matter 1.2 (로봇청소기 장치 유형 포함)",
      "kind": "표준",
      "org": "Connectivity Standards Alliance (CSA)",
      "url": "https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/",
      "related_areas": [
        21,
        65
      ],
      "summary": "스마트홈 기기 상호운용 표준 Matter 의 1.2 판(2023-10-23)으로, 로봇청소기를 장치 유형으로 넣어 원격 시작·진행 알림·건식/습식 청소 모드·브러시·오류·충전 상태를 제조사와 무관하게 다룬다. 이후 판의 로봇청소기 관련 변경은 확인하지 못했다.",
      "ref_id": "ref-977"
    }
  ],
  "additional_research_requests": [
    "7절·6절: Matter 1.3 이후 판(특히 1.4 의 로봇청소기용 Service Area 클러스터, 구역·방 단위 청소)의 공식 사양·발표를 확인해 Matter 서술을 최신 판 기준으로 갱신할 근거가 필요하다(1차 검증이 1.2 기준으로 한정하도록 지시).",
    "6절·11절: 공동주택 배송로봇의 수령 인증 수단(비밀번호·앱·QR)과 완료 결과를 배달 앱·택배사 시스템에 돌려주는 방식의 공개 자료가 없어 완료·인계 칸을 '미확인'으로 두었다.",
    "9절: 홈네트워크(월패드) 연동 사례를 확인하지 못해 시설·설비 제어 경계의 월패드 항목을 미확인으로 두었다.",
    "5절: 롯데글로벌로지스·로보티즈 고양·파주 실증의 기간·규모와 개미의 실제 단지 운영 여부, 공동주택 배송 성과 수치(독립 출처)가 필요하다.",
    "7절: 개정 지능형로봇법 운행안전인증 조항과 이동로봇 특별법안 의안 원문(국가법령정보센터·국회 의안정보시스템), 개인정보 보호법 제25조의2 국가법령정보센터 원문과 개인정보보호위원회 해석·가이드라인을 확인해야 한다.",
    "5절·8절: 한국소비자원·KISA 로봇청소기 보안 조사 원 보도자료(발표일·조사 기간 2025-03~07 여부)를 열어 두 기사의 2차 인용을 대체할 필요가 있다.",
    "3절·5절: 가정 돌봄 로봇 사례와 세대 내 로봇청소기 보급률 수치는 브리프에 없어 쓰지 못했다.",
    "퍼블리셔 참고: 1차 검증이 지적한 대로 ref-965 가 같은 날 2026-09-29-16 실행의 다른 출처(Karlsen 외)와 id 충돌하므로 게시 전 번호 재부여가 필요하다. 본문 각주도 함께 바뀌어야 한다."
  ],
  "fixes_applied": [
    "f1 시점 정정 — 5절 첫 사례 서술을 '2024-12 시범 운영과 2025년 실증을 거쳐 구축, 2026년부터 요기요 연계로 반경 1.2km 식음료점 130여 곳으로 범위 확대'로 고쳐 ref-966·ref-965·ref-979 를 붙였다.",
    "f2·f18·f19 벤더 주장 병기 — 해당 문장(4·5·6절)에 모두 '[추정] 벤더 주장'을 붙였고, f2 에는 조사 시점이 실증 기간이라고만 적혀 있다는 점을 덧붙였다.",
    "f19 '전문가 모드' 명칭 삭제 — 4·5·6절 본문, 용어 정의(원격 조작), 11절 다섯째 열린 질문에서 이름을 빼고 '소유자가 1X 원격 조작자를 예약해 로봇을 안내하게 하는 기능'으로 썼다.",
    "f6 출처 명시 — 4절 단지 집하 방식, 5절 둘째 사례 표·서술, 6절 관제 흐름에 '정보통신신문이 LH토지주택연구원 자료를 인용해 전한 것'임을 밝혔다.",
    "f4 단일 기사 명시 — 3·5·6절의 승강기 연동 기능 문장에 '미디어펜(2026-09-20)에 따르면'과 단일 기사 근거임을 적었다.",
    "f8 CaseNote 명시 — 7절 표·본문과 13절 ref-978 각주에 '민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람', 법률 제19234호·시행 2023-09-15 를 남겼다.",
    "f9 해석 명시 — 7절에서 '조문 문언(업무 목적·공개된 장소)에서 도출한 해석이며 개인정보보호위원회 해석은 확인하지 못했다'고 밝히고 11절 첫 질문과 연결했다.",
    "f10 — 7절 표·본문에 '보도자료 기사(AI타임스 2023-11-16) 기준, 법령 원문 미열람'을 밝히고 66. 실외로 연결했으며, 5절에서는 단지 도로 배송의 제약으로만 썼다.",
    "f11 — 3·6·7절의 모든 서술에 '2026-09 초 발의된 법안(발의 단계), 국회 통과·시행 미확인'을 붙이고 '시행되면 …할 수 있게 된다' 형식으로 썼다.",
    "f14 — 5절 셋째 사례 서술과 13절 ref-969·ref-970 각주에 '같은 정부 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람'을 밝히고, 취약점 대상은 '일부 중국 브랜드 제품'으로만 썼다.",
    "f15·f16 — 4·6·7절의 Matter 서술을 'Matter 1.2 발표(2023-10-23) 기준'으로 한정하고 '이후 판의 로봇청소기 관련 변경은 확인하지 못했다'를 명시했으며, f16 판단을 1.2 발표 범위로 한정했다. 1.3 이후 판(1.4 Service Area 클러스터) 확인은 additional_research_requests 로 넘겼다.",
    "f13 — 3·5·8절에서 '미국 기업 iRobot 의 개발용 기기, 동의서에 서명한 유료 수집자·직원의 집' 조건과 함께 썼고 5절에 소비자 제품이 아닌 개발용 기기 사례임을 적었다.",
    "f5 — 5절 둘째 사례 서술과 6절에 실증 기간·규모 미확인, 개미의 버튼 조작은 '시연·시험을 마친 단계'이며 상용 운영 여부 미확인이라고 썼다.",
    "f22 — 9절의 문장을 '건설사 또는 물류사 한 곳과 로봇 업체 한 곳의 짝'으로 고치고, '원격 조작 승인'이 원격 조작자 예약 기능을 해석한 것임을 [추정] 문장으로 밝혔다.",
    "인용 — ref-965 는 ‘주문자만 배달음식 픽업이 가능’ 한 구절, ref-976 은 ‘업무목적 달성에 불필요한 영상은 즉시 삭제’ 한 구절만 직접 인용하고 불빛·소리·안내판 고지와 실증 기간 등 나머지는 재서술했다.",
    "5. 적용 사례 — 세 사례의 현장 유형을 모두 '가정'으로 명시하고 여섯 항목을 채웠으며 site_matrix_updates 의 site_type 은 '가정'만 썼다. f8·f10 은 사례로 세우지 않고 7절에 두었다.",
    "용어 — 이동형 영상정보처리기기는 새로 등록하지 않고 4·7절에서 기존 용어집 항목(mobile-video-information-processing-device)을 링크했으며, 매터·실외이동로봇 운행안전인증·비전 언어 행동 모델·원격 조작 4개를 glossary_updates 로 등록하고 매터 정의에 '1.2 판 기준'을 유지했다.",
    "분량 초과 자동 분리: 65. 가정·공동주택 본문 11,590자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,305자"
  ]
}
```

### runs/2026-09-29-17/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/site-type-applications/home-and-apartment.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area65-s7.md (1,508자)
    - docs/categories/site-type-applications/home-and-apartment.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area65-s6.md (1,202자)
    - docs/categories/site-type-applications/home-and-apartment.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area65-s4.md (1,119자)
    - docs/categories/site-type-applications/home-and-apartment.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area65-s8.md (949자)
    - docs/categories/site-type-applications/home-and-apartment.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area65-s10.md (885자)
    - docs/categories/site-type-applications/home-and-apartment.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area65-s11.md (858자)
    - docs/categories/site-type-applications/home-and-apartment.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area65-s3.md (826자)
```

### runs/2026-09-29-17/pages/categories/site-type-applications/home-and-apartment.md

```markdown
---
title: "65. 가정·공동주택"
type: area
category: "Q. 현장 유형별 적용"
area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [공동주택 배송, 공동현관·승강기 연동, 사생활, 가사 로봇, 이동형 영상정보처리기기, Matter]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-965, ref-966, ref-967, ref-968, ref-969, ref-970, ref-971, ref-972, ref-973, ref-974, ref-975, ref-976, ref-977, ref-978, ref-979]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 65. 가정·공동주택

# 65. 가정·공동주택

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]

## 3. 왜 중요한가

가정·공동주택의 로봇 작업은 공동주택 단지 배송, 세대 안 청소, 정리·세탁·주방 같은 조작 가사, 보안·순찰·청소·충전·주차 같은 단지 공용 서비스의 네 형태로 나타나며, 단지 배송은 상용·실증 단계이고 조작 가사는 시연·사전 주문·벤치마크 단계로 보인다. [추정][^ref-965][^ref-976][^ref-977][^ref-971][^ref-975]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 왜 중요한가](../../topics/2026/2026-09-29-area65-s3.md)에 있다.

## 4. 핵심 개념과 용어

가정·공동주택 로봇에는 촬영 제한(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 가전 연동 표준(Matter) 같은 제도·표준 용어와 가사 로봇의 동작 모델·원격 조작 용어가 함께 쓰인다. [사실][^ref-978][^ref-967][^ref-977]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area65-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 사례는 모두 현장 유형 가정에 속하며, 공동주택 단지의 음식 배송·택배 배송과 세대 안 청소·가사 로봇으로 나눠 여섯 항목을 채운다. 여섯 항목 대응은 확인한 자료를 묶은 것이며, 수령 인증의 구체 방식과 결과를 배달 앱에 돌려주는 방식은 확인하지 못했다. [추정][^ref-965][^ref-976][^ref-973]

**현장 유형:** 가정

**사례:** 공동주택 단지에서 배달 음식을 세대 현관까지 로봇으로 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입주민이 배달 앱(요기요)으로 단지 반경 1.2km 식음료점 130여 곳 가운데 한 곳에 주문한다. [사실][^ref-965] |
| 작업 대상 | 음식·식음료(물건)와 단지 입구에서 세대 현관까지의 공용 공간 [사실][^ref-965][^ref-979] |
| 수행 자원 | 배송로봇(삼성물산과 뉴빌리티, 현대건설과 모빈의 짝), 공동현관 자동문, 승강기 [사실][^ref-966][^ref-979] |
| 제약 | 공동출입문 개폐와 승강기 호출이 연동돼야 단지 안을 다닐 수 있다. [사실][^ref-979] 공개된 장소를 지나는 로봇 카메라 촬영은 촬영 표시 의무 등의 제한을 받을 가능성이 크다(7절). [추정][^ref-978] |
| 완료·인계 | 세대 현관에서 주문자만 음식을 꺼낼 수 있는 방식으로 넘긴다. [사실][^ref-965] 인증 수단은 미확인이다. |
| 예외·성과 | 공동출입문·승강기 연동이 실패하면 운행이 끊긴다. [사실][^ref-979] 삼성물산은 실증 기간에 서비스를 이용한 입주민 113명 조사에서 만족도 95%, 필요성 공감 99%, 유료 이용 의사 74%라고 밝혔으며, 조사 시점은 실증 기간이라고만 적었다. [추정] 벤더 주장[^ref-965] |

서울 서초구 래미안 리더스원에서 삼성물산은 뉴빌리티와 함께 공동현관 자동문 개폐와 엘리베이터 호출 연동을 해결해 세대 현관까지 가는 도어 투 도어 배달을 만들었다. 이 배달은 2024-12 시범 운영과 2025년 실증을 거쳐 구축됐고, 2026년부터 요기요 연계로 반경 1.2km 식음료점 130여 곳으로 범위를 넓혔다. [사실][^ref-966][^ref-965][^ref-979] 회사는 이 방식을 ‘주문자만 배달음식 픽업이 가능’한 서비스로 설명한다. [사실][^ref-965]

현대건설은 모빈과 함께 로봇이 단지 입구에서 지하주차장과 공동출입문을 지나 승강기를 타고 세대 현관까지 식음료 등을 나르게 했고, 첫 적용 단지로 디에이치 대치 에델루이가 보도됐다. [사실][^ref-966][^ref-979] 미디어펜(2026-09-20)에 따르면 이 로봇은 승강기 시스템과 연동해 자동 호출·목적층 재호출·정원 초과 여부 판단을 구현했으며, 이 기능 서술은 이 기사 하나에 기댄다. [사실][^ref-979]

**현장 유형:** 가정

**사례:** 공동주택 단지 택배를 로봇으로 세대까지 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 택배 차량이 단지 집하처에서 송장번호를 인식시키면 물품 정보가 관제실로 간다(정보통신신문이 LH토지주택연구원 자료를 인용). [사실][^ref-976] |
| 작업 대상 | 택배 물품과 동·세대로 이어지는 단지 도로·승강기 구간 [사실][^ref-976] |
| 수행 자원 | 택배 배송로봇(롯데글로벌로지스와 로보티즈의 짝), 관제실, 승강기 [사실][^ref-966][^ref-976] |
| 제약 | 좁은 보도에서 행인과 충돌할 위험과 통신 장애 시 급정지 위험이 지적된다. [사실][^ref-976] 단지 밖 보도 구간을 지나면 실외이동로봇 운행안전인증이 걸릴 수 있다(7절, 66. 실외). [추정][^ref-967] |
| 완료·인계 | 집하 방식에 따라 동·구역 물품보관함에 두거나 로봇이 세대까지 가져간다. [사실][^ref-976] 수령 확인 방식은 미확인이다. |
| 예외·성과 | 관제실이 거주자와 통신하며 로봇을 통제한다. [사실][^ref-976] 실증 기간·규모와 성과 수치는 미확인이다. |

롯데글로벌로지스는 로보티즈와 함께 한국로봇산업진흥원 규제혁신 로봇 실증사업으로 경기도 고양·파주 아파트 단지에서 택배 배송로봇을 실증했으며, 실증의 기간·규모는 확인되지 않았다. [사실][^ref-966] 로보티즈의 자율주행로봇 ‘개미’는 로봇팔로 승강기 버튼을 직접 눌러 타고 내리는 시험을 마친 단계이며, 상용 운영 여부는 확인되지 않았다. [사실][^ref-976]

정보통신신문(2024-07-18)은 LH토지주택연구원 자료를 인용해 단지 로봇 택배를 단지 단위 중앙집하(집하장 1개소), 동 단위 분산집하(동마다 물품보관함), 구역 단위 분산집하(여러 동마다 보관함 1개소)의 세 시나리오로 나눈다. [사실][^ref-976] 같은 기사는 촬영 사실을 불빛·소리·안내판으로 알리고 ‘업무목적 달성에 불필요한 영상은 즉시 삭제’해야 한다는 제언을 싣는다. [사실][^ref-976] 보도 통행 위험은 [66. 실외](outdoor.md)와 겹치므로 여기서는 단지 도로를 지나는 배송의 제약으로만 다룬다.

**현장 유형:** 가정

**사례:** 세대 안에서 청소·가사 로봇을 운용하며 사생활 지키기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 거주자가 로봇청소기를 원격으로 시작한다(Matter 1.2 기준). [사실][^ref-977] 로봇이 모르는 작업은 소유자가 원격 조작자를 예약해 안내하게 한다고 1X는 밝혔다. [추정] 벤더 주장[^ref-973] |
| 작업 대상 | 바닥(공간), 우유·세탁물 같은 물건, 집 안 영상과 거주자 개인정보 [추정][^ref-974][^ref-968] |
| 수행 자원 | 로봇청소기, 조작 가사 로봇(LG 클로이드, 1X NEO), 원격 조작자 [추정] 벤더 주장[^ref-974][^ref-973] |
| 제약 | 1X는 로봇이 들어가지 않는 금지 구역과 얼굴 흐림 기능을 내세웠다. [추정] 벤더 주장[^ref-973] 세대 안 촬영에 개인정보 보호법 제25조의2가 직접 적용되는지는 확인되지 않았다(7절). [추정][^ref-978] |
| 완료·인계 | Matter 1.2 기준 로봇청소기는 진행 알림과 브러시·오류·충전 상태를 보고한다. [사실][^ref-977] |
| 예외·성과 | 영상 유출(iRobot 개발용 기기)과 기기 보안 취약점(일부 중국 브랜드 제품)이 실제로 드러났다. [사실][^ref-968][^ref-969][^ref-970] |

한국소비자원과 한국인터넷진흥원(KISA)이 국내 판매 로봇청소기 6개 모델(삼성전자·LG전자 2종, 드리미·로보락·에코백스·나르왈 4종)을 40개 보안 항목으로 조사한 결과, 일부 중국 브랜드 제품에서 사용자 인증 미흡으로 외부에서 촬영 사진을 열람하거나 카메라를 강제로 켤 수 있는 취약점이 발견됐고 국산 2종은 상대적으로 양호했다. [사실][^ref-969][^ref-970] 두 기사는 같은 정부 조사 발표를 옮긴 2차 자료이며, 한국소비자원·KISA 원 보도자료는 열지 못했다.

MIT Technology Review(2022-12-19)에 따르면 미국 기업 iRobot 의 개발용 Roomba J7 이 동의서에 서명한 유료 데이터 수집자·직원의 집에서 찍은 이미지가 AI 학습용 라벨링을 위해 Scale AI 를 거쳐 베네수엘라 등의 외주 작업자에게 넘어갔고, 화장실의 여성과 복도의 아이가 찍힌 사진을 포함한 스크린숏 15장이 Facebook·Discord 등에 게시됐다. [사실][^ref-968] 소비자 제품이 아니라 개발용 기기에서 일어난 사례다.

정리·세탁·주방 같은 조작 가사는 시연·사전 주문·벤치마크 단계로 보인다. [추정][^ref-974][^ref-973][^ref-971] LG전자는 CES 2026 에서 7자유도 팔 두 개·다섯 손가락 손·바퀴 기반 자율주행을 갖춘 LG 클로이드가 냉장고에서 우유 꺼내기, 오븐에 크루아상 넣기, 세탁 시작, 건조된 옷 개기를 시연한다고 발표했으며, 출시일·가격은 밝히지 않았다. [추정] 벤더 주장[^ref-974] 1X는 2025-10-28 가정용 휴머노이드 NEO 의 사전 주문(2만 달러 또는 월 499달러, 2026년 미국 가정 배송)을 받기 시작했다. [추정] 벤더 주장[^ref-973]

## 6. 대표 접근법과 기술

공동주택 배송에서는 공동현관·승강기를 시스템 연동으로 여는 방식과 로봇팔로 버튼을 누르는 방식이 확인되고, 세대 안 로봇에는 원격 조작 보조·사생활 기능과 가전 표준 연동이 함께 제시된다. [사실][^ref-979][^ref-976][^ref-977]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area65-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 걸린 표준·제도는 가전 연동 표준 Matter 1.2, 촬영 제한 조항(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 발의 단계의 이동로봇 특별법안이다. [사실][^ref-977][^ref-978][^ref-967][^ref-975]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area65-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 조작 가사의 어려움을 보여 주는 벤치마크, 공동주택 거주자·업계 인식 조사, 가정 로봇 영상 유출 탐사 보도와 로봇청소기 보안 조사 보도로 나뉜다. [사실][^ref-971][^ref-972][^ref-968][^ref-969]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 대표 연구와 자료](../../topics/2026/2026-09-29-area65-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

가정·공동주택에서 ROP는 배송·청소·순찰 요청을 받아 로봇에 배정하고, 공동현관·승강기를 예약·호출·재호출하며, 수령 확인 결과를 돌려주고, 촬영 표시·금지 구역·원격 조작 승인 같은 사생활 조건을 경로·권한 제약으로 반영하는 일을 맡을 것으로 보인다. [추정][^ref-965][^ref-976][^ref-979][^ref-978]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 배달 앱·택배 관제의 배송 요청을 받아 배송·청소·순찰 로봇에 배정하고 수령 확인 결과를 돌려준다. [추정][^ref-965][^ref-976] | 연계 대상: 메뉴·결제·택배 배차를 맡는 배달 앱·택배사 시스템 [추정][^ref-965] |
| 시설·설비 제어 | 공동현관·승강기 예약·호출·재호출 요청과 상태 확인 [추정][^ref-979] | 연계 대상: 공동현관 자동문·승강기 제어반·월패드 제어(월패드 연동 사례는 미확인) [추정][^ref-979] |
| 로봇 자체 지능·제어 | 로봇이 할 수 있는 작업과 실행 조건, 완료·실패 확인 [추정][^ref-974] | 연계 대상: 자율주행·파지·VLA 모델과 주행·조작 안전 성능은 로봇 제조사가 맡는다. [추정][^ref-974] |
| 업종별 조건 | 촬영 표시·금지 구역·원격 조작 승인 같은 사생활 조건을 경로·권한 제약으로 반영 [추정][^ref-978][^ref-973] | 연계 대상: 개인정보 보호법·지능형로봇법·공동주택관리법상 절차와 법적 판단은 관리 주체·법령에 맡긴다. [추정][^ref-978][^ref-967][^ref-975] |

표의 ‘원격 조작 승인’은 출처가 밝힌 원격 조작자 예약 기능을 ROP의 권한 제약으로 해석한 것이다. [추정][^ref-973] 확인한 국내 사례는 모두 건설사 또는 물류사 한 곳과 로봇 업체 한 곳의 짝이며, 여러 제조사 로봇을 한 단지에서 묶은 공개 사례는 확인되지 않았다. [추정][^ref-966][^ref-965][^ref-979] 경계를 나누는 원칙은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

가정·공동주택은 설비·업무 시스템 연동, 개인정보·보안, L. AI·학습 기술, 법·수용성, 실외 영역과 이어진다. [추정][^ref-979][^ref-978][^ref-974][^ref-972]

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area65-s10.md)에 있다.

## 11. 열린 질문

이 영역의 열린 질문은 세대 안 촬영의 법 적용, 공동현관·승강기 연동 표준, 다제조사 단지 관제, 수령 인증 방식, 원격 조작의 규율 다섯 가지다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [65. 가정·공동주택 — 열린 질문](../../topics/2026/2026-09-29-area65-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-965]: 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영, 2026-01-15, https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/, 접근일 2026-09-29
[^ref-966]: 지디넷코리아 (신영빈), 로봇이 문앞까지 택배 가져다 주는 미래 곧 온다, 2025-01-19, https://zdnet.co.kr/view/?no=20250119062609, 접근일 2026-09-29
[^ref-967]: AI타임스, 실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행(보도자료 기사, 법령 원문 미열람), 2023-11-16, https://www.aitimes.com/news/articleView.html?idxno=155217, 접근일 2026-09-29
[^ref-968]: MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-29
[^ref-969]: 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은?(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-09-29
[^ref-970]: 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-06, https://www.imaeil.com/page/view/2025100618362463025, 접근일 2026-09-29
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-09-29
[^ref-972]: Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs, 2026-06, https://journal.ksles.org/articles/xml/g9G5/, 접근일 2026-09-29
[^ref-973]: The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder, 2025-10-30, https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/, 접근일 2026-09-29
[^ref-974]: LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026, 2026-01-06, https://www.lg.com/us/press-release/lg-cloid-home-robot, 접근일 2026-09-29
[^ref-975]: 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다, 2026-09-27, https://www.hankyung.com/article/2026092776141, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-09-29
[^ref-978]: CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)(법률 제19234호, 시행 2023-09-15; 민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람), 2023-03-14, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982, 접근일 2026-09-29
[^ref-979]: 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도, 2026-09-20, https://www.mediapen.com/news/view/1124680, 접근일 2026-09-29
```

### docs/categories/site-type-applications/home-and-apartment.md

```markdown
---
title: "65. 가정·공동주택"
type: area
category: "Q. 현장 유형별 적용"
area_no: 65
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 65. 가정·공동주택

# 65. 가정·공동주택

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]

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

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s7.md

```markdown
---
title: "65. 가정·공동주택 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-967, ref-975, ref-976, ref-977, ref-978]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#7
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 관련 표준·프레임워크·오픈소스

# 65. 가정·공동주택 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 표준·제도는 가전 연동 표준 Matter 1.2, 촬영 제한 조항(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 발의 단계의 이동로봇 특별법안이다. [사실][^ref-977][^ref-978][^ref-967][^ref-975]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 표준·제도는 가전 연동 표준 Matter 1.2, 촬영 제한 조항(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 발의 단계의 이동로봇 특별법안이다. [사실][^ref-977][^ref-978][^ref-967][^ref-975]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Matter 1.2 | 표준 | 로봇청소기 장치 유형을 정의한다(원격 시작·진행 알림·청소 모드·상태 정보). 1.2 발표(2023-10-23) 기준이며 이후 판의 로봇청소기 관련 변경은 확인하지 못했다. [사실][^ref-977] | CSA 발표 |
| 개인정보 보호법 제25조의2 | 법령 | 업무 목적 이동형 영상정보처리기기의 공개 장소 촬영 제한, 민감 장소 촬영 금지, 촬영 표시 의무(법률 제19234호, 시행 2023-09-15). 민간 법령 DB(CaseNote) 게재 조문 기준이며 국가법령정보센터 원문은 열지 않았다. [사실][^ref-978] | CaseNote 게재 조문 |
| 실외이동로봇 운행안전인증 | 법령·인증 제도 | 단지 밖 보도를 지나는 배송로봇의 인증·보험 요건(2023-11-17 시행). 보도자료 기사(AI타임스 2023-11-16) 기준이며 법령 원문은 열지 않았다. [사실][^ref-967] | AI타임스 |
| 이동로봇 특별법안 | 법안(발의 단계) | 공동주택 로봇 도입 절차와 공동현관·엘리베이터 통신 연동 절차의 간소화·표준화. 2026-09 초 발의, 국회 통과·시행 미확인. [사실][^ref-975] | 한국경제 |

개인정보 보호법 제25조의2는 업무 목적의 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영하는 것을 원칙적으로 막고, 촬영 사실을 명확히 표시했는데도 거부 의사가 없는 경우 등만 예외로 두며, 목욕실·화장실·탈의실처럼 사생활 침해 우려가 큰 장소 내부를 볼 수 있는 곳의 촬영을 금지하고, 촬영 시 불빛·소리·안내판 등으로 표시하게 한다. [사실][^ref-978] 조문 문언(업무 목적·공개된 장소)에서 도출한 해석으로는, 단지 도로·공동현관·승강기를 다니는 배송로봇의 촬영은 이 조항의 관리 대상이 될 가능성이 크지만 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 촬영은 직접 대상이 아닐 수 있어 제조사의 영상 처리는 동의 기반 처리 같은 다른 규율에 기댈 것으로 보인다. [추정][^ref-978][^ref-976] 이 해석은 법 해석이 아니며 개인정보보호위원회 해석은 확인하지 못했다. 이 문제는 11. 열린 질문의 첫 질문으로 올렸다.

개정 지능형로봇법은 질량 500kg·시속 15km 이하의 배송·순찰 로봇을 실외이동로봇으로 정의하고, 운행구역 준수·횡단보도 통행 등 16개 시험항목의 운행안전인증과 보험(공제) 가입을 요구하며, 인증받은 로봇은 개정 도로교통법에 따라 보행자와 같은 지위로 보도를 다닐 수 있다. [사실][^ref-967] 보도 통행 규정은 [66. 실외](../../categories/site-type-applications/outdoor.md)에서 다루고, 이 페이지에서는 단지 도로를 지나는 배송의 제약으로만 쓴다.

이동로봇 특별법안은 한병도 의원이 2026-09 초 대표 발의한 국토교통부 마련 법안으로, 건축법·국토계획법·공동주택관리법·주차장법에 흩어진 이동로봇 규제를 손질하는 내용이다. 발의 단계이며 국회 통과·시행 여부는 확인되지 않았다. [사실][^ref-975]

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-967]: AI타임스, 실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행(보도자료 기사, 법령 원문 미열람), 2023-11-16, https://www.aitimes.com/news/articleView.html?idxno=155217, 접근일 2026-09-29
[^ref-975]: 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다, 2026-09-27, https://www.hankyung.com/article/2026092776141, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-09-29
[^ref-978]: CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)(법률 제19234호, 시행 2023-09-15; 민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람), 2023-03-14, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s6.md

````markdown
---
title: "65. 가정·공동주택 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-965, ref-973, ref-974, ref-975, ref-976, ref-977, ref-979]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#6
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 대표 접근법과 기술

# 65. 가정·공동주택 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공동주택 배송에서는 공동현관·승강기를 시스템 연동으로 여는 방식과 로봇팔로 버튼을 누르는 방식이 확인되고, 세대 안 로봇에는 원격 조작 보조·사생활 기능과 가전 표준 연동이 함께 제시된다. [사실][^ref-979][^ref-976][^ref-977]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공동주택 배송에서는 공동현관·승강기를 시스템 연동으로 여는 방식과 로봇팔로 버튼을 누르는 방식이 확인되고, 세대 안 로봇에는 원격 조작 보조·사생활 기능과 가전 표준 연동이 함께 제시된다. [사실][^ref-979][^ref-976][^ref-977]

### 공동현관·승강기 연동

시스템 연동 방식은 로봇과 공동현관 자동문·승강기를 통신으로 잇는다. 삼성물산 래미안 리더스원은 공동현관 자동문 개폐와 엘리베이터 호출을 연동했다. [사실][^ref-965][^ref-979] 미디어펜(2026-09-20)에 따르면 현대건설 사례의 승강기 연동은 자동 호출·목적층 재호출·정원 초과 여부 판단을 포함하며, 이 내용은 단일 기사 근거다. [사실][^ref-979] 버튼 조작 방식은 로봇팔로 승강기 버튼을 직접 누르는 것으로, 로보티즈 ‘개미’가 시연·시험을 마친 단계다. [사실][^ref-976] 2026-09 초 발의된 이동로봇 특별법안(발의 단계, 국회 통과·시행 미확인)은 시행되면 배송로봇의 공동현관 통과·엘리베이터 이용을 위한 통신 시스템 연동 절차를 간소화·표준화하게 된다. [사실][^ref-975]

```mermaid
flowchart LR
    order[배달 앱 주문] --> robot[배송로봇 출발]
    robot --> gate[단지 입구]
    gate --> parking[지하주차장]
    parking --> door[공동출입문 개폐 연동]
    door --> lift[승강기 호출·재호출 연동]
    lift --> home[세대 현관]
    home --> pickup[주문자 수령 확인]
```

### 단지 집하 방식과 관제 흐름

정보통신신문이 LH토지주택연구원 자료를 인용해 전한 서비스 흐름에서는 택배 차량이 집하처에서 송장번호를 인식시켜 물품 정보를 관제실로 보내면, 관제실이 거주자와 통신하며 로봇을 통제해 배송한다. [사실][^ref-976] 집하 위치는 단지·동·구역 단위 세 가지로 나뉜다. [사실][^ref-976]

### 수령 인증

래미안 리더스원 배송은 주문자만 음식을 꺼낼 수 있게 해 수령인을 제한한다. [사실][^ref-965] 비밀번호·앱·QR 가운데 어떤 수단을 쓰는지와 완료 결과가 배달 앱으로 어떻게 돌아가는지는 확인하지 못해 11. 열린 질문에 올렸다.

### 원격 조작 보조와 사생활 기능

1X는 NEO 가 모르는 작업을 소유자가 1X 원격 조작자를 예약해 안내하게 하는 기능과, 로봇이 들어가지 않는 금지 구역·얼굴 흐림 같은 사생활 기능을 함께 내세웠다. [추정] 벤더 주장[^ref-973] 단지를 다니는 배송로봇에는 촬영 사실을 불빛·소리·안내판으로 알리는 방법이 제언됐다. [사실][^ref-976]

### 가전 표준 연동

Matter 1.2 발표(2023-10-23) 기준 로봇청소기 장치 유형은 원격 시작·진행 알림, 건식·습식 청소 모드, 브러시·오류·충전 상태를 제조사와 무관하게 다루며, 이 발표에는 지도나 구역 청소가 언급되지 않는다. [사실][^ref-977] 따라서 1.2 기준으로는 제조사가 다른 청소 로봇을 일정·상태 수준에서 한 제어 계층으로 다루는 경로가 될 수 있지만, 1.2 발표 범위에 물건 운반·조작 같은 다른 가사 로봇 능력이 없어 가사 로봇 전반의 능력 표현으로는 부족할 것으로 보인다. [추정][^ref-977] 이후 판의 로봇청소기 관련 변경은 확인하지 못했다. LG전자는 클로이드가 ThinQ·ThinQ ON 허브로 가전 서비스를 조율한다고 발표했다. [추정] 벤더 주장[^ref-974]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-965]: 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영, 2026-01-15, https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/, 접근일 2026-09-29
[^ref-973]: The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder, 2025-10-30, https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/, 접근일 2026-09-29
[^ref-974]: LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026, 2026-01-06, https://www.lg.com/us/press-release/lg-cloid-home-robot, 접근일 2026-09-29
[^ref-975]: 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다, 2026-09-27, https://www.hankyung.com/article/2026092776141, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-09-29
[^ref-979]: 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도, 2026-09-20, https://www.mediapen.com/news/view/1124680, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s4.md

```markdown
---
title: "65. 가정·공동주택 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-965, ref-967, ref-973, ref-974, ref-976, ref-977, ref-978]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#4
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 핵심 개념과 용어

# 65. 가정·공동주택 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 가정·공동주택 로봇에는 촬영 제한(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 가전 연동 표준(Matter) 같은 제도·표준 용어와 가사 로봇의 동작 모델·원격 조작 용어가 함께 쓰인다. [사실][^ref-978][^ref-967][^ref-977]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

가정·공동주택 로봇에는 촬영 제한(개인정보 보호법 제25조의2), 보도 통행 인증(개정 지능형로봇법), 가전 연동 표준(Matter) 같은 제도·표준 용어와 가사 로봇의 동작 모델·원격 조작 용어가 함께 쓰인다. [사실][^ref-978][^ref-967][^ref-977]

- **[이동형 영상정보처리기기](../../glossary/mobile-video-information-processing-device.md)(Mobile Video Information Processing Device)** — 2023-09-15 시행된 개인정보 보호법 제25조의2가 업무 목적의 공개 장소 촬영을 제한하고 촬영 표시를 요구하는 기기 유형이다. [사실][^ref-978]
- **실외이동로봇 운행안전인증(Outdoor Mobile Robot Operational Safety Certification)** — 2023-11-17 시행된 개정 지능형로봇법에 따라 질량 500kg·시속 15km 이하 배송·순찰 로봇이 16개 시험항목을 통과해야 받는 인증으로, 인증받은 로봇은 보도를 보행자 지위로 다닐 수 있다. [사실][^ref-967]
- **매터(Matter)** — Connectivity Standards Alliance(CSA)의 스마트홈 기기 상호운용 표준으로, 1.2 판(2023-10-23 발표) 기준 로봇청소기를 장치 유형으로 정의해 제조사가 달라도 시작·청소 모드·상태 정보를 같은 방식으로 다루게 한다. [사실][^ref-977]
- **비전 언어 행동 모델(Vision-Language-Action Model, VLA)** — 영상과 언어 지시를 받아 로봇 동작을 직접 출력하도록 학습한 모델로, LG전자는 가정용 로봇 클로이드가 비전 언어 모델(Vision-Language Model, VLM)과 VLA를 쓴다고 발표했다. [추정] 벤더 주장[^ref-974]
- **원격 조작(Teleoperation)** — 사람이 떨어진 곳에서 로봇 영상을 보며 조종하는 방식으로, 1X는 소유자가 1X 원격 조작자를 예약해 가정용 로봇 NEO를 안내하게 하는 기능을 내세웠다. [추정] 벤더 주장[^ref-973]
- **도어 투 도어 배달(Door-to-door Delivery)** — 로봇이 공동현관 자동문과 승강기를 거쳐 세대 현관까지 물건을 가져다주는 공동주택 배송 방식이다. [사실][^ref-965]
- **단지 집하 방식** — 공동주택 로봇 택배를 단지 단위 중앙집하, 동 단위 분산집하, 구역(Zone) 단위 분산집하로 나눈 운영 시나리오로, 정보통신신문이 LH토지주택연구원 자료를 인용해 전했다. [사실][^ref-976]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-965]: 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영, 2026-01-15, https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/, 접근일 2026-09-29
[^ref-967]: AI타임스, 실외이동로봇 시대 개막...개정 지능형로봇법 17일 시행(보도자료 기사, 법령 원문 미열람), 2023-11-16, https://www.aitimes.com/news/articleView.html?idxno=155217, 접근일 2026-09-29
[^ref-973]: The Robot Report (Mike Oitzman), NEO humanoid designed for household use, available for preorder, 2025-10-30, https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/, 접근일 2026-09-29
[^ref-974]: LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026, 2026-01-06, https://www.lg.com/us/press-release/lg-cloid-home-robot, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-09-29
[^ref-978]: CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)(법률 제19234호, 시행 2023-09-15; 민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람), 2023-03-14, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s8.md

```markdown
---
title: "65. 가정·공동주택 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-968, ref-969, ref-970, ref-971, ref-972, ref-976]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#8
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 대표 연구와 자료

# 65. 가정·공동주택 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 자료는 조작 가사의 어려움을 보여 주는 벤치마크, 공동주택 거주자·업계 인식 조사, 가정 로봇 영상 유출 탐사 보도와 로봇청소기 보안 조사 보도로 나뉜다. [사실][^ref-971][^ref-972][^ref-968][^ref-969]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 자료는 조작 가사의 어려움을 보여 주는 벤치마크, 공동주택 거주자·업계 인식 조사, 가정 로봇 영상 유출 탐사 보도와 로봇청소기 보안 조사 보도로 나뉜다. [사실][^ref-971][^ref-972][^ref-968][^ref-969]

- Li, C., Zhang, R., Wong, J. 외, BEHAVIOR-1K(arXiv 2024-03-14 제출, CoRL 2022 예비판) — 설문으로 고른 일상 활동 1,000개를 집·정원·식당·사무실 등 50개 장면과 주석 달린 물체 9,000여 개로 OmniGibson 시뮬레이터에 구현한 벤치마크이며, 이 활동들은 길고 복잡한 조작이 필요해 최신 로봇 학습 방법에도 어렵다고 보고한다. [사실][^ref-971] [모바일 매니퓰레이터](../../glossary/mobile-manipulator.md)로 시뮬레이션에서 실물로 옮기는 초기 실험도 했다. [사실][^ref-971]
- Hwang, I. T., Kim, G. T., & Kwag, B. C., 공동주택 서비스 로봇 도입에 대한 거주자·업계 인식 비교(한국생활환경학회지 30, 2026-06) — 거주자 63명과 업계 65명을 비교해 수용 태도·우려·기술 요구의 차이를 보였고, 연령별 사생활·안전 우려 차이는 통계적으로 유의하지 않았다. [사실][^ref-972]
- MIT Technology Review(Eileen Guo), 로봇청소기 이미지 유출 탐사 보도(2022-12-19) — 미국 기업 iRobot 의 개발용 기기, 동의서에 서명한 유료 수집자·직원의 집이라는 조건에서 학습 데이터 라벨링 외주가 사생활 유출 경로가 된 과정을 추적했다. [사실][^ref-968]
- 바이라인네트워크(2025-10-31)·매일신문(2025-10-06), 한국소비자원·KISA 로봇청소기 보안 조사 보도 — 6개 모델·40개 항목 조사 결과를 전하며, 바이라인은 게시판 ID 로 이름·전화번호를 조회할 수 있는 문제도 적는다. 두 기사는 같은 정부 발표를 옮긴 2차 자료다. [사실][^ref-969][^ref-970]
- 정보통신신문(2024-07-18), 로봇배송 기획 기사 — LH토지주택연구원 자료를 인용한 단지 집하 시나리오와 영상 촬영 고지 제언을 담았다. [사실][^ref-976]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-968]: MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-29
[^ref-969]: 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은?(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-09-29
[^ref-970]: 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-06, https://www.imaeil.com/page/view/2025100618362463025, 접근일 2026-09-29
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-09-29
[^ref-972]: Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs, 2026-06, https://journal.ksles.org/articles/xml/g9G5/, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s10.md

```markdown
---
title: "65. 가정·공동주택 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-972, ref-974, ref-978, ref-979]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#10
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 다른 연구영역과의 연결

# 65. 가정·공동주택 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 가정·공동주택은 설비·업무 시스템 연동, 개인정보·보안, L. AI·학습 기술, 법·수용성, 실외 영역과 이어진다. [추정][^ref-979][^ref-978][^ref-974][^ref-972]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

가정·공동주택은 설비·업무 시스템 연동, 개인정보·보안, L. AI·학습 기술, 법·수용성, 실외 영역과 이어진다. [추정][^ref-979][^ref-978][^ref-974][^ref-972]

- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 공동현관 자동문·승강기 호출·재호출 연동이 단지 배송의 전제다.
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 배달 앱·택배 관제에서 배송 요청을 받고 결과를 돌려준다.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 한 단지에서 제조사가 다른 로봇을 묶는 관제와 이어진다.
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — Matter 1.2 의 로봇청소기 장치 유형과 이어진다.
- [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) — 주문자만 꺼내는 수령 확인이 인계 확인에 해당한다.
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 가정 로봇의 금지 구역을 장소 의미로 다룬다.
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 원격 조작자가 로봇 작업을 안내한다.
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 원격 조작 승인과 수령 인증의 권한 문제다.
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 로봇청소기 보안 취약점과 이어진다.
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 이동형 영상정보처리기기 촬영 제한과 가정 영상 유출을 다룬다.
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 가사 로봇의 VLA 모델이 적용 대상인 이 영역과 이어진다.
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 가정 영상을 학습 데이터로 라벨링하는 과정의 처리 기준과 이어진다.
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — BEHAVIOR-1K 같은 가사 활동 벤치마크.
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 개인정보 보호법·지능형로봇법·이동로봇 특별법안.
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 거주자의 수용 태도와 기술 요구.
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 단지 밖 보도 통행과 실외이동로봇 운행안전인증.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-972]: Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs, 2026-06, https://journal.ksles.org/articles/xml/g9G5/, 접근일 2026-09-29
[^ref-974]: LG Electronics USA, LG ELECTRONICS PRESENTS LG CLOiD HOME ROBOT TO DEMONSTRATE "ZERO LABOR HOME" AT CES 2026, 2026-01-06, https://www.lg.com/us/press-release/lg-cloid-home-robot, 접근일 2026-09-29
[^ref-978]: CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)(법률 제19234호, 시행 2023-09-15; 민간 법령 DB(CaseNote) 게재 조문 기준, 국가법령정보센터 원문 미열람), 2023-03-14, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982, 접근일 2026-09-29
[^ref-979]: 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도, 2026-09-20, https://www.mediapen.com/news/view/1124680, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s11.md

```markdown
---
title: "65. 가정·공동주택 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: []
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#11
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 열린 질문

# 65. 가정·공동주택 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 열린 질문은 세대 안 촬영의 법 적용, 공동현관·승강기 연동 표준, 다제조사 단지 관제, 수령 인증 방식, 원격 조작의 규율 다섯 가지다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 열린 질문은 세대 안 촬영의 법 적용, 공동현관·승강기 연동 표준, 다제조사 단지 관제, 수령 인증 방식, 원격 조작의 규율 다섯 가지다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (열림 · 제기 2026-09-29 · 실행 2026-09-29-17) 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-17) 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-17) 한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-17) 공동주택 배송로봇의 수령 확인(주문자만 꺼낼 수 있는 방식)은 어떤 인증 수단(비밀번호·앱·QR)으로 이루어지며, 그 결과가 배달 앱·택배사 시스템에 완료 이벤트로 어떻게 돌아가는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-17) 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-17/pages/topics/2026/2026-09-29-area65-s3.md

```markdown
---
title: "65. 가정·공동주택 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 65
related_areas: [16, 17, 20, 21, 22, 23, 31, 44, 47, 51, 52, 53, 54, 59, 60, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-965, ref-968, ref-969, ref-970, ref-971, ref-972, ref-975, ref-976, ref-977, ref-979]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/home-and-apartment.md#3
---

[홈](../../index.md) › [주제](../index.md) › 65. 가정·공동주택 — 왜 중요한가

# 65. 가정·공동주택 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 가정·공동주택의 로봇 작업은 공동주택 단지 배송, 세대 안 청소, 정리·세탁·주방 같은 조작 가사, 보안·순찰·청소·충전·주차 같은 단지 공용 서비스의 네 형태로 나타나며, 단지 배송은 상용·실증 단계이고 조작 가사는 시연·사전 주문·벤치마크 단계로 보인다. [추정][^ref-965][^ref-976][^ref-977][^ref-971][^ref-975]
- 이 페이지는 [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

가정·공동주택의 로봇 작업은 공동주택 단지 배송, 세대 안 청소, 정리·세탁·주방 같은 조작 가사, 보안·순찰·청소·충전·주차 같은 단지 공용 서비스의 네 형태로 나타나며, 단지 배송은 상용·실증 단계이고 조작 가사는 시연·사전 주문·벤치마크 단계로 보인다. [추정][^ref-965][^ref-976][^ref-977][^ref-971][^ref-975]

거주자의 기대와 요구는 한 방향이 아니다. 공동주택 거주자 63명과 업계 종사자 65명을 비교한 국내 연구(2026-06)에서 거주자의 95.2%가 서비스 로봇 도입에 긍정적이었지만 실제 체험 의향은 88.9%였고, 자녀가 있는 가구는 단지 내 배송을 유의하게 우선시했다. [사실][^ref-972] 거주자는 충돌 방지·개인정보 보호·사용자 인터페이스를, 업계는 시스템 통합·운영 안정성을 더 중시했다. [사실][^ref-972]

집 안을 찍는 로봇은 사생활 사고로 이어진 적이 있다. 2022-12 보도에 따르면 미국 기업 iRobot 의 개발용 로봇청소기가 동의서에 서명한 유료 수집자·직원의 집에서 찍은 이미지가 학습 데이터 라벨링 외주 과정을 거쳐 소셜 미디어에 게시됐다. [사실][^ref-968] 2025년 국내 판매 로봇청소기 6개 모델 보안 조사에서는 일부 중국 브랜드 제품에서 외부에서 촬영 사진을 열람하거나 카메라를 강제로 켤 수 있는 취약점이 확인됐다. [사실][^ref-969][^ref-970]

공동주택 배송은 건물 설비와 제도에 묶여 있다. 미디어펜(2026-09-20)에 따르면 업계는 공동출입문이 열리지 않거나 승강기를 호출할 수 없으면 단지 안 운행이 끊기고, 관제시스템과 충전시설도 갖춰야 한다고 본다. [사실][^ref-979] 2026-09 초 발의된 이동로봇 특별법안은 발의 단계이며 국회 통과·시행 여부는 확인되지 않았지만, 시행되면 아파트가 입주자대표회의 의결로 배송·보안·순찰·청소·충전·주차로봇을 도입할 수 있게 된다. [사실][^ref-975]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/home-and-apartment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/home-and-apartment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-965]: 삼성물산 뉴스룸, 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영, 2026-01-15, https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/, 접근일 2026-09-29
[^ref-968]: MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-29
[^ref-969]: 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은?(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-09-29
[^ref-970]: 매일신문, 사생활 훔치는 로봇청소기…중국산 제품서 `무단 촬영` 가능성 확인(한국소비자원·KISA 조사 발표를 옮긴 2차 자료, 원 보도자료 미열람), 2025-10-06, https://www.imaeil.com/page/view/2025100618362463025, 접근일 2026-09-29
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-09-29
[^ref-972]: Hwang, I. T., Kim, G. T., & Kwag, B. C. (한국생활환경학회지 30), Comparing Perceptions of Service Robot Adoption in Multi-Family Housing Between Residents and Industry Stakeholders: Focusing on Acceptance Attitudes, Concerns, and Technological Needs, 2026-06, https://journal.ksles.org/articles/xml/g9G5/, 접근일 2026-09-29
[^ref-975]: 한국경제 (김익환), 배송·주차·청소까지…로봇 아파트 뜬다, 2026-09-27, https://www.hankyung.com/article/2026092776141, 접근일 2026-09-29
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-09-29
[^ref-977]: Connectivity Standards Alliance (CSA), Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board, 2023-10-23, https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/, 접근일 2026-09-29
[^ref-979]: 미디어펜 (조태민), 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도, 2026-09-20, https://www.mediapen.com/news/view/1124680, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-17 | 65. 가정·공동주택 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 964건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 256개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
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
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [65] 에 걸린 0건 / 전체 180건)

```markdown
없음
```
