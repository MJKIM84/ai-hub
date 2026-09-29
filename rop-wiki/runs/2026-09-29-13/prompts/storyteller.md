(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-13
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 63. 병원·의료 (Q. 현장 유형별 적용)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko

## 입력

### runs/2026-09-29-13/target.json

```json
{
  "run_id": "2026-09-29-13",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 105,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 63,
    "area_name": "63. 병원·의료",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=63"
}
```

### runs/2026-09-29-13/research.json

```json
{
  "run_id": "2026-09-29-13",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 63,
    "area_name": "63. 병원·의료",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 의료 로봇 미들웨어(RoMi-H)·승강기 가동률·등재 프로그램·스마트병원 선도모델 용어 없음(승강기 어댑터·플릿 어댑터·오픈 RMF·이동형 영상정보처리기기는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 국내(분당서울대병원·한림대성심병원·고대구로병원·울산대병원)·해외(싱가포르 창이종합병원 RoMi-H, 중국 산시성 인민병원) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 승강기·자동문 연동, 이기종 로봇 미들웨어, 수령 인증(RFID·생체인증), 야간 배송, 승강기 혼잡 모델링 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 13482, KS 로봇 승강기 탑승 안전 요구사항, Open-RMF/RoMi-H, 스마트병원 선도모델 모듈 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 간호 협동로봇 체계적 문헌 검토, 병원 물류 로봇 효과 분석, 승강기 혼잡 타당성 연구, 국내 감염환자 이송 로봇 인식 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 17. 작업 대상·자산 식별과 인계 추적, 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동, 28. 공용 자원·충전·에너지 최적화, 32. 예외 복구·재계획·업무 연속성, 51. 인증·권한·격리, 53. 개인정보·영상 데이터, 50. 안전 표준·인증·사고 조사, 56. 운영 이관·확대·교육, 58. 다사업자 책임·계약·데이터 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-134·oq-138·oq-142·oq-149 미반영, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]",
    "병원 안 검체·약품·식사·린넨 이송과 감염환자 이송에 어떤 로봇이 들어가며, 학술 문헌은 그 효과와 근거 수준을 어떻게 평가하는가? (섹션 3·6·8 겨냥)",
    "국내(분당서울대병원·한림대성심병원·고대구로병원)와 해외(싱가포르 RoMi-H, 중국 병원) 사례에서 병원 로봇 작업의 시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과는 어떻게 나타나는가? (섹션 5 겨냥, 현장 유형 병원 명시, 한국 자료 우선)",
    "승강기·자동문 연동과 승강기 혼잡, 감염 관리 구역, 수령 인증(RFID·생체인증)은 병원 이송 로봇 운영에 어떤 제약과 완료 조건을 만들며 어떤 기술로 다루는가? (섹션 4·6 겨냥)",
    "병원 이송 로봇에 적용되는 안전·상호운용 표준(ISO 13482, KS 로봇 승강기 탑승 안전 요구사항)과 이기종 로봇 미들웨어(Open-RMF/RoMi-H), 국내 정부 사업(서비스로봇 실증사업, 스마트병원 선도모델)은 무엇을 규정·지원하며 ROP 의 위치를 어떻게 규정하는가? (섹션 7·9 겨냥)",
    "병원에서 ROP 가 직접 맡을 것(이송 요청 수신·배정·승강기 예약·수령 확인·결과 반환)과 병원 정보 시스템·승강기 제어·로봇 자체 안전 기능·감염 관리 규정에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)",
    "oq-149·oq-134·oq-138·oq-142: 싱가포르 RoMi-H 등재 프로그램 같은 벤더 사전 평가 제도가 국내 병원에 있는가, 그리고 국내 병원에서 운영 기록의 시뮬레이션 재현·대화형 시나리오 구성·대화형 다중 로봇 업무 지시 사례가 있는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Li 외(Scientific Reports, 2026-04-24)는 중국 산시성 인민병원(500병상, 22개 개방 병동)에서 적재 200kg·배터리 7시간의 자율이동로봇 10대로 약국→병동 약품 배송과 병동→검사실 검체 이송을 정기·수시 두 방식으로 6개월 운영한 결과, 수작업 대비 배송 시간이 32~36% 줄고 로봇 10대가 수작업 인력 19명보다 7.3배 많은 배송 횟수를 처리했으며 검증 정확도·물품 온전율 100%(수작업 97~99%)를 기록했다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-939"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Compared with manual delivery, robot delivery reduced delivery time by 32% to 36%\"; 10대 플릿이 6개월간 수작업 19명보다 7.3배 많은 배송 횟수, 검증 정확도·물품 온전율 100%(수작업 97~99%). 10년 누적 절감 692.8만 위안, 투자 회수 3.4년.",
      "as_of": "2026-04-24",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "같은 연구는 사물인터넷 기반 승강기 제어로 층간 자율 이동을, 픽업·배송 지점의 RFID 신원 확인으로 수령 인증을, 비접촉 배송으로 인력 이동과 교차 감염 위험 감소를 구현했고, 약국·병동·시스템 관리자·장비 정비 인력의 역할을 정한 협력 책임 체계를 운영 관리 틀로 두었으며 최대 수요 시간당 42건에서 로봇 10대의 이용률이 0.84였다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-939"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IoT 연동 승강기 제어로 층간 자율 주행, 픽업·배송 지점 RFID 신원 확인, 비접촉 배송으로 교차 감염 위험 감소, 스마트 충전소. 약국·병동·시스템 관리자·정비 인력의 역할을 정한 협력 책임 체계. 최대 수요 42건/시간, 이용률 0.84(10대).",
      "as_of": "2026-04-24",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f3",
      "claim": "Lee 외(고려대학교 구로병원·도구공간, Digital Health, 2026-03-31)는 고대구로병원에서 ISO 13482 적합 인증 시험을 거친 도구공간 IROI 로봇 1대로 2025-06-18~29 약국→응급실 비긴급 약품 배송 122건을 분석해 전체 성공률 87.03%, 승강기 가동률(EOR) 59% 미만에서 95.52%, 실패는 EOR 90% 초과 구간에 집중됐다고 보고했으며, 승강기 연동은 TK엘리베이터 TK50M 제어반에 부착한 전용 통신 모듈로 호출·탑승을 자동화했다.",
      "tag": "사실",
      "source_ids": [
        "ref-946"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Overall success rate: 87.03%\"; EOR 59% 미만 성공률 95.52%, 실패는 EOR 90% 초과에 집중, ROC AUC 0.779(95% CI 0.661–0.882). TK Elevator TK50M 제어반 전용 통신 모듈로 호출·탑승 자동화. 한계: 단일 기관·단일 로봇·몬테카를로 모형 단순화.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "RoMi-H(Robotic Middleware for Healthcare)는 싱가포르 창이종합병원 CHART 가 IHiS·GovTech·Hope Technik·Open Robotics 와 함께 만든 ROS 2·DDS 기반 오픈소스 미들웨어로 2018-07 보건부 장관 발표 뒤 2019-10-31 ROSCon 에서 공개됐고, 기계·제어·중앙·통합의 네 도메인으로 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 잇는 것을 목적으로 하며 Open-RMF 를 핵심 기반으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-940",
        "ref-945"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "CGH: \"To ensure that all robotics systems tested and subsequently deployed in Public Healthcare Institutions are interoperable via a standardised and recognised International and Singapore platform.\" Open Robotics 블로그: RMF(ROS 2) 위에 구축, 2018-07 시작, CHART·IHiS·HopeTechnik·GovTech 협력. (두 출처는 같은 프로젝트의 참여 기관이라 독립성 제한)",
      "as_of": "2021-02-10",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f5",
      "claim": "Open Robotics 는 2021-02-10 글에서 RoMi-H 가 여러 제조사의 로봇이 승강기 같은 병원의 물리 자산을 공유하고 경로 계획 시각화와 다른 로봇에 대한 출입 금지 구역으로 충돌을 피하게 하며 로봇 플랫폼·센서·기업 정보 시스템에 걸친 통일된 통신·모니터링을 제공한다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"uniform communication and monitoring across robot platforms, sensors, and enterprise information systems\"; 승강기 같은 물리 자산과 상호작용, 다른 로봇에 대한 keep-out 구역으로 충돌 회피. 싱가포르 보건부·국가로봇프로그램 지원.",
      "as_of": "2021-02-10",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "창이종합병원 CHART 의 RoMi-H 등재 프로그램(Empanelment Programme) 2025 는 싱가포르 보건부가 모든 공공 의료기관의 자동화 통합 플랫폼으로 인정한 RoMi-H 를 배치할 시스템 통합사의 기술 전문성과 배치 지식을 평가해 2025-05-01 부터 2년 유효한 인증을 주고 CHART 웹사이트에 게시해 공공 의료기관의 RFP·RFI 참여 목록으로 쓰며, 격년으로 운영되고 현재 등재 통합사는 HOPE Technik·Medisys Innovation·Panasonic Asia Pacific·QuikBot Technologies·Techfox 5개사다.",
      "tag": "사실",
      "source_ids": [
        "ref-944"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Applicants will undergo a series of evaluations, encompassing both technical expertise and deployment knowledge.\" 2025-05-01 효력, 2년 유효, CHART 사이트 게시·공공 의료기관 RFP/RFI 참여 목록, 등재 통합사 5개. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "이데일리(2023-07-06)에 따르면 분당서울대병원은 KT 의 5G 특화망 위에 자율주행 이송로봇(AMR) 6대를 두어 본관에서 헬스케어혁신파크까지 약 300m 의 연결 터널(워킹갤러리)로 진료재료·약품·린넨(환자복·침대 시트·이불) 카트를 옮기며, 승강기·자동문이 다중으로 연동돼 자동 작동하고 기존 1.5km 차량 운송을 대체했으며 야간 배송으로 환자 동선과 분리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-941"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"물품을 카트에 채워놓기만 하면 무거운 카트는 자율주행 이송로봇이 옮긴다.\" AMR 6대, 워킹갤러리 약 300m, 승강기·자동문 다중 연동, 충돌 방지, 야간 배송으로 환자 동선 분리, 기존 차량 운송 1.5km 대체.",
      "as_of": "2023-07-06",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "한림대성심병원은 2024-04 기준 7종 73대의 서비스 로봇(약제·검체·물품 배송로봇 '나르미', 안내로봇, 방역로봇, 비대면 협진·홈케어 로봇)을 운영하며 제조사가 다른 여러 로봇을 통합관제 시스템으로 커맨드센터에서 중앙 관리하고 2023년 27,300건(월평균 2,250건)의 로봇 배송을 처리했으며, 데일리팜(2024-07-15)은 이 병원에 LG전자와 빅웨이브로보틱스가 각각 배송로봇을 공급한다고 전해 서로 다른 제조사 로봇의 공존이 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-947",
        "ref-943"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "로봇신문: \"제조사마다 상이한 다종 다수의 로봇 관제를 통합관제 시스템을 이용해 중앙에서 효율적으로 관리할 수 있다\"; 7종 73대, 2023년 27,300건. 데일리팜: LG전자(한림대성심·용인세브란스 공급, 구독 서비스), 빅웨이브로보틱스(한림대성심 담당).",
      "as_of": "2024-07-15",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f9",
      "claim": "뉴스투데이(2025-02-11)에 따르면 한림대성심병원의 약제 배송로봇은 혼자 승강기를 타고 병동 간호사 스테이션 지정 장소에서 대기하고, 검체 운반 로봇은 포름알데히드 용액에 담긴 조직을 옮기며, 실외 배송로봇은 신호등을 인식해 본관과 별관 사이 횡단보도를 건너는데, 커맨드센터 부센터장은 시스템 정착에 약 3년이 걸렸고 사용자 공감대 형성과 보급형 로봇의 한계에 맞춘 병원 시스템 변경이 과제였다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-942"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"혼자서 엘리베이터를 타고 병동으로 이동해 간호사 스테이션의 지정된 장소에서 무한정 대기\"; 포름알데히드 용액 조직 운반, 신호등 인식 횡단보도 통과, 정착 약 3년, 사용자 공감대·병원 시스템 변경 필요.",
      "as_of": "2025-02-11",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "데일리팜(2024-07-15)에 따르면 양산부산대병원·용인세브란스병원·한림대성심병원·조선대병원·삼성서울병원·해운대백병원·의정부을지대병원·일산차병원이 원내 약 배송로봇을 도입했고 과학기술정보통신부 'XaaS 선도 프로젝트'(총 56억 원) 5개 과제 중 1개를 빅웨이브로보틱스가 맡았으며, 자동출입문 장치 필요·통로 협소·승강기 턱 때문에 도입을 포기한 병원이 있어 기존 건물보다 신축 병원 위주로 도입된다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "도입 병원 8곳 열거; 과기정통부 XaaS 선도 프로젝트 총 56억 원; \"자동출입문 장치 필요, 통로 협소, 엘리베이터 턱 문제로 이동 불가해 도입이 어려웠다\"; 구축 병원 공간 제약, 신축 병원 위주 도입.",
      "as_of": "2024-07-15",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "비즈한국(2025-04-10)에 따르면 한국로봇산업진흥원의 서비스로봇 실증사업과 한국보건산업진흥원의 스마트병원 사업이 2020년부터 병원 로봇 도입을 지원해 스마트병원 개별 선도모델 58개가 운영되고, 울산대학교병원은 2022년 항암제 이송 로봇을 도입했으며, 의료진은 약사의 대면 업무와 간호사의 약제실 왕복이 줄었다고 평가하는 한편 속도·안전성 부족과 병원 물류의 복잡성을 지적했고 대당 수억 원의 비용과 경사로·문·승강기 호환 같은 건축 구조가 주요 장애 요인으로 꼽힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-951"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"약사는 대면 업무가 줄고 간호사는 직접 약제실로 내려오지 않아 두 직군 모두 업무 효율성을 높일 수 있었다\"; 비용 대당 평균 수억 원, 경사로·문·승강기 호환 문제, 생체인증(지정맥)·AI 안면인식으로 출입 통제와 접촉 최소화.",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "한국로봇산업진흥원의 서비스로봇 실증사업은 수요 중심 실증으로 시장 창출 한계를 넘기 위해 2020년부터 물류(공공·민간 실내외 물류·이송 로봇)·웨어러블·의료·기타(협동·언택트 서비스 로봇) 네 분야를 지원하며 로봇 도입 비용의 50% 이내를 국비로 대고 총사업비의 50% 이상을 민간 현금 부담으로 하며, 공모 → 서류·발표·현장평가 → 과제 선정 → 협약 → 중간 점검 → 최종 평가 순서로 진행된다.",
      "tag": "사실",
      "source_ids": [
        "ref-950",
        "ref-951"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "진흥원: \"수요 중심의 로봇 활용 실증을 통해 시장창출 한계를 극복\", 2020년부터, 로봇 도입 비용 50% 이내 국비, 서류심사·발표평가·현장평가. 비즈한국: 2020년부터 운영 중인 서비스 로봇 실증사업(교차 확인은 사업 존재·시작 연도만).",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f13",
      "claim": "한국보건산업진흥원 스마트병원 확산지원센터는 개별 선도모델 58개를 9개 모듈로 재구성했으며, 그중 '지능형 원내 물류 배송' 모듈은 자율주행 로봇과 보안이 강화된 생체인증 시스템으로 약국·물품공급실·병동 간 무인 배송 체계를, '하나로 감염관리' 모듈은 방문객 출입 통제·동선 분석·혼잡도 관리·환경 소독까지 감염관리 업무 자동화를 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"자율주행 로봇과 보안이 강화된 생체인증 시스템을 이용하여 약국, 물품공급실, 병동 간 무인 배송 시스템을 구축합니다.\" 9개 모듈: 환자흐름 최적화·환자안전 강화·간호 업무 자동화·스마트수술실·원격중환자실·감염병 위기 대응·하나로 감염관리·지능형 원내 물류 배송·지능형 업무 자동화. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f14",
      "claim": "산업통상자원부 국가기술표준원은 2021-11-11 로봇의 승강기 탑승 시 안전 요구사항과 실내 배송 로봇에 관한 국가표준(KS)을 제정한다고 발표했으며, 이는 2020-10 '로봇산업 선제적 규제혁신 로드맵'에 따라 승강기 안전기준 소관인 행정안전부와 협력한 결과로 속도 제어·위험 상황의 보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-948"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"속도제어 ▲위험상황에서의 보호정지 ▲높낮이차·틈새극복 ▲추락·넘어짐 방지\"; 산업부 2020-10 로봇산업 선제적 규제혁신 로드맵, 행정안전부 협력. 자료에 KS 표준 번호·정식 명칭은 없음.",
      "as_of": "2021-11-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "Babalola 외(Frontiers in Robotics and AI, 2024-06-05)의 체계적 문헌 검토는 2018년 이후 간호 협동로봇 연구 28편을 검토해 대부분이 기술 성숙도 4~5 수준이고 환자 중심 설계가 많아 간호 업무 부담을 줄이는 물류·행정 보조 로봇은 드물며, 미국 병원에 TUG 같은 배송 로봇이 도입돼 있음에도 동료 심사 근거가 '두드러지게 부족'하고 비용·유지보수·사이버보안 분석이 미흡하다고 결론짓는다.",
      "tag": "사실",
      "source_ids": [
        "ref-949"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"evidence of nurse-assistive cobots in U.S. hospitals was generally strikingly lacking, despite the known adoption of general-purpose cobots like TUG Automated Robotic Delivery System by Aethon Inc.\" 28편, TRL 4~5 다수, TRL 9 는 1건, 비용·유지보수·사이버보안 분석 부족.",
      "as_of": "2024-06-05",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "최현철·서슬기·권재용·박상찬·장혜정(경희대학교·Korea SUNY, 품질경영학회지 51(3), 2023)은 감염병 대응 수단인 감염환자 이송 로봇에 대한 의료종사자 인식을 SERVQUAL 다섯 차원(유형성·신뢰성·반응성·보증성·공감성)과 AHP(유효 응답 23부)로 조사해, 환자 이송 과정의 안전이 최우선이고 이송 중 기기 오류 해결과 응급처치 제공 용이성, 환자 모니터링과 감염 인자 억제 능력이 중요하다는 결과를 얻었다.",
      "tag": "사실",
      "source_ids": [
        "ref-952"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록: 의료종사자 개입이 최소화되는 영역의 위험 요인 우려, 환자 이송 과정에서 안전이 최우선이라는 합의, 이송 중 기기 오류 해결·응급처치 제공 용이성 강조, 환자 모니터링·감염 인자 억제 능력 중요. 30부 배포·24부 회수·23부 분석.",
      "as_of": "2023",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "Fragapane 외(European Journal of Operational Research 294(2), 2021)의 자율이동로봇 계획·제어 문헌 검토는 제조·창고·크로스독·터미널과 함께 병원을 AMR 의 적용 분야로 들어, 병원이 인트라로지스틱스 AMR 연구의 대상 현장 가운데 하나임을 보인다.",
      "tag": "사실",
      "source_ids": [
        "ref-911"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제조·창고·크로스독·터미널·병원을 적용 분야로 들며 관리자를 위한 AMR 계획·제어 프레임워크와 연구 의제 제시 (재인용: 2026-09-29-11)",
      "as_of": "2021",
      "site_type": "병원",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "Open-RMF 는 플릿 어댑터로 서로 다른 제조사의 로봇 플릿을 붙이고 문·승강기 어댑터로 설비를 연동하는 오픈소스 미들웨어이며, RoMi-H 가 이를 핵심 기반으로 싱가포르 공공 병원에 적용됐으므로 병원 현장의 이기종 로봇·승강기 연동 참고 구조로 볼 수 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-004",
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RMF Core: 플릿 어댑터·문·승강기 연동·작업·교통 조율 구조(재인용: 2026-09-29-12). Open Robotics 블로그: RoMi-H 는 RMF(ROS 2) 위에 구축돼 승강기 같은 물리 자산 공유를 지원.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": false
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 병원의 로봇 작업은 (1) 약품 이송 — 야간 약제·항암제·마약류를 약국에서 병동·응급실로(f1·f3·f10·f11), (2) 검체 이송 — 병동·수술실에서 검사실로, 포름알데히드 조직 포함(f1·f9), (3) 린넨·진료재료·물품 카트 이송(f7·f8), (4) 감염환자 이송 — 사람을 작업 대상으로 하는 이송(f16), (5) 방역·환경 소독과 출입 통제(f8·f13)의 다섯 형태로 나타나며, 식사 이송 사례는 이번 조사에서 근거를 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-939",
        "ref-946",
        "ref-943",
        "ref-951",
        "ref-942",
        "ref-941",
        "ref-947",
        "ref-952",
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f3·f7·f8·f9·f10·f11·f13·f16 의 종합. 각 사례가 밝힌 이송 대상: 약품(항암제·마약류 포함), 검체(포름알데히드 조직), 린넨·진료재료·물품, 감염환자, 방역·출입 통제.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 병원 로봇 작업의 여섯 항목은 시작 조건이 약국·병동의 정기·수시 이송 요청과 야간 시간대 배송(f1·f7), 작업 대상이 약품·검체·린넨·진료재료와 감염환자(f19), 수행 자원이 AMR 과 약국·병동·시스템 관리자·정비 인력·커맨드센터(f2·f8), 제약이 승강기 혼잡·자동문·통로·턱(f3·f10), 감염 관리 구역과 비접촉(f2·f13), 생체인증 권한(f13), ISO 13482·KS 승강기 탑승 안전 요구(f3·f14), 완료·인계가 RFID 신원 확인·생체인증 개폐(f2·f13), 예외·성과가 승강기 혼잡 시 실패·기기 오류·응급처치 우려와 배송 시간·건수 지표(f1·f3·f16)로 채워질 수 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-939",
        "ref-941",
        "ref-947",
        "ref-946",
        "ref-943",
        "ref-953",
        "ref-948",
        "ref-952"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f3·f7·f8·f10·f13·f14·f16 의 종합. 수치는 각 연구·기사 조건(단일 병원·단일 로봇·특정 기간)에 한정된다.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 63. 병원·의료에서 ROP 가 직접 맡을 범위는 약국·병동·검사실이 내는 이송 요청을 받아 제조사가 다른 로봇에 배정하고, 승강기·자동문을 예약·연동하며(f2·f3·f7), 감염 관리 구역·야간 시간대·권한 제약을 경로·배정 제약으로 반영하고(f7·f13), RFID·생체인증 같은 수령 인증으로 완료를 확인해 병원 정보 시스템에 결과를 돌려주며(f2·f13), 승강기 혼잡 같은 실패를 받아 재계획하는 일(f3)이고, 싱가포르 RoMi-H 가 이를 공공 의료 전체의 통합 플랫폼으로 보였으며(f4·f6) 국내는 한림대성심병원의 통합관제(f8)가 가장 가까운 공개 사례다.",
      "tag": "추정",
      "source_ids": [
        "ref-939",
        "ref-946",
        "ref-941",
        "ref-953",
        "ref-940",
        "ref-944",
        "ref-947"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3·f4·f6·f7·f8·f13 의 종합. 국내에서 이기종 병원 로봇을 하나의 표준 계층으로 묶은 공개 사례는 통합관제 언급 수준이며 인터페이스·표준은 미확인.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "연계 대상: 병원에서 처방·조제·검사 지시를 내는 병원 정보 시스템(HIS·EMR·약국 시스템)은 분류 원문 19장의 상위 업무 시스템, 승강기 제어반·자동문은 시설·설비 제어, 로봇의 자율 주행·회피와 ISO 13482 안전 기능은 로봇 자체 지능·제어, 감염 관리 규정·환자 정보 보호·의료 관련 법령은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 처방 판단·승강기 제어·안전 기능 성능·감염 관리 기준 설정은 병원 정보 시스템·승강기 업체·로봇 제조사·병원 감염관리 조직에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-939",
        "ref-946",
        "ref-953",
        "ref-948"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(승강기 제어·RFID)·f3(TK50M 전용 모듈, ISO 13482)·f13(생체인증·감염관리 모듈)·f14(KS 안전 요구)에서 도출한 경계. 분류 원문 19장 표의 다섯 경계에 대응.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "이 영역은 승강기·자동문 연동을 다루는 22. 설비·건물 시스템 연동(f2·f3·f7·f14), 이기종 로봇 미들웨어와 등재 제도를 다루는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성·58. 다사업자 책임·계약·데이터(f4·f6·f8), RFID·생체인증 수령 확인을 다루는 17. 작업 대상·자산 식별과 인계 추적·51. 인증·권한·격리(f2·f13), 사이버보안·환자 정보를 다루는 53. 개인정보·영상 데이터(f15), ISO 13482·KS 승강기 탑승 요구와 감염환자 이송 안전을 다루는 49. 사람 근접 안전·50. 안전 표준·인증·사고 조사(f3·f14·f16), 승강기를 공용 자원으로 다루는 28. 공용 자원·충전·에너지 최적화와 혼잡 시 실패를 다루는 32. 예외 복구·재계획·업무 연속성(f3), 야간 동선 분리를 다루는 19. 사람·보행자 모델(f7), 배송 시간·건수를 다루는 39. 운영 성과 측정·개선(f1·f8), 구축 병원의 통로·턱 제약과 3년 정착을 다루는 55. 현장 조사·설치·시운전·56. 운영 이관·확대·교육(f9·f10·f11), 정부 실증·스마트병원 사업을 다루는 3. 경제성·조달·사업 모델(f12·f13)에 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-939",
        "ref-946",
        "ref-941",
        "ref-948",
        "ref-940",
        "ref-944",
        "ref-947",
        "ref-953",
        "ref-949",
        "ref-952",
        "ref-942",
        "ref-943",
        "ref-951",
        "ref-950"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f16 이 각각 근거가 되는 영역을 대응시킨 것. 승강기는 병원에서 로봇·사람·침대가 함께 쓰는 공용 자원이라는 점(f3)이 28. 공용 자원·충전·에너지 최적화 연결의 근거다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "oq-149 에 대해 싱가포르 RoMi-H 등재 프로그램은 2025-05-01 부터 2년 유효한 통합사 5개 등재로 계속 운용 중임이 확인되나(f6), 국내에서 벤더·통합사를 사전 평가해 병원 로봇 공급 자격을 주는 제도는 이번 조사에서 확인되지 않았고, 확인된 국내 제도는 과제 단위로 서류·발표·현장평가를 거치는 서비스로봇 실증사업(f12)과 스마트병원 선도모델 사업(f11·f13)뿐이며 이는 벤더 등록 자격 제도가 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-944",
        "ref-950",
        "ref-951",
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6(등재 프로그램 2025)·f12(실증사업 평가 절차)·f11·f13(스마트병원 사업)의 대조. 검색어 '스마트병원 선도모델 로봇 표준 가이드라인 상호운용'에서 국내 등재 제도 미확인.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "oq-134·oq-138·oq-142 에 대해 국내 병원에서 로봇 운영 기록으로 실제 상황을 시뮬레이션에 재현하거나 대화로 시나리오를 구성하거나 대화로 여러 로봇에 업무를 지시·승인한 사례는 이번 조사에서도 확인되지 않았으며, 가장 가까운 국내 자료는 고대구로병원 연구가 운영 기록의 승강기 가동률과 성공률 관계를 몬테카를로 모형으로 분석한 것(f3)과 한림대성심병원의 통합관제(f8)다.",
      "tag": "추정",
      "source_ids": [
        "ref-946",
        "ref-947"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3(122건 운영 기록·몬테카를로 모형, 단일 로봇)·f8(통합관제 시스템)의 대조. 검색어 '병원 로봇 디지털 트윈 시뮬레이션 운영 기록 재현 대화형 업무 지시 LLM' 결과는 임상 LLM·병원 운영 시뮬레이션이며 로봇 운영 재현·대화형 지시는 아님.",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-939",
      "org": "Li, M. 외 (Scientific Reports)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04-24",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "중국 산시성 인민병원에서 AMR 10대로 약품·검체 이송을 6개월 운영한 효과 분석. 배송 시간 32~36% 단축, 승강기 IoT 제어·RFID 신원 확인·협력 책임 체계·경제성 분석.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/",
      "source_unopened": false
    },
    {
      "id": "ref-940",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "ROMI-H | Changi General Hospital",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "싱가포르 공공 의료 로봇 미들웨어 RoMi-H 의 목적·네 도메인·DDS 기반·2019-10-31 공개를 설명하는 창이종합병원 CHART 공식 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "source_unopened": false
    },
    {
      "id": "ref-941",
      "org": "이데일리",
      "title": "분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입",
      "published": "2023-07-06",
      "url": "https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "분당서울대병원이 KT 5G 특화망 위에 AMR 6대로 워킹갤러리 300m 구간의 진료재료·약품·린넨 카트를 야간 배송하며 승강기·자동문을 연동한 사례.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896",
      "source_unopened": false
    },
    {
      "id": "ref-942",
      "org": "뉴스투데이",
      "title": "[한림대성심병원 로봇 사용기 (下)] 배송로봇, 엘리베이터 타고 횡단보도 건너 검체 운반",
      "published": "2025-02-11",
      "url": "https://www.news2day.co.kr/article/20250211500007",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한림대성심병원의 약제·검체·실외 배송로봇 운영 방식(승강기 단독 탑승, 횡단보도 통과)과 3년 정착 과정의 조직·시스템 변경 과제를 전한 탐방 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.news2day.co.kr/article/20250211500007",
      "source_unopened": false
    },
    {
      "id": "ref-943",
      "org": "데일리팜",
      "title": "원내 약 배송로봇 도입 확대...정부 지원에 변화 바람",
      "published": "2024-07-15",
      "url": "https://m.dailypharm.com/user/news/15128",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원내 약 배송로봇을 도입한 국내 병원 8곳, 과기정통부 XaaS 선도 프로젝트(56억 원), LG전자·빅웨이브로보틱스 공급, 구축 병원의 자동문·통로·승강기 턱 제약을 정리한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://m.dailypharm.com/user/news/15128",
      "source_unopened": false
    },
    {
      "id": "ref-944",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": null,
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "RoMi-H 배치 시스템 통합사를 기술·배치 역량으로 평가해 2년 유효 인증을 주고 공공 의료기관 RFP·RFI 참여 목록으로 게시하는 등재 프로그램 안내(2025-05-01 효력, 등재 통합사 5개).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "source_unopened": false
    },
    {
      "id": "ref-945",
      "org": "Open Robotics",
      "title": "ROMI-H: Bringing Robot Traffic Control to Healthcare",
      "published": "2021-02-10",
      "url": "https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "Open Robotics 가 RoMi-H 의 RMF(ROS 2) 기반, 이기종 로봇의 승강기 등 물리 자산 공유, 출입 금지 구역을 통한 충돌 회피, 협력 기관을 설명한 블로그 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare",
      "source_unopened": false
    },
    {
      "id": "ref-946",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "고대구로병원에서 ISO 13482 인증 시험을 거친 IROI 로봇 1대의 약국→응급실 배송 122건을 분석해 승강기 가동률과 성공률(전체 87.03%)의 관계를 밝힌 타당성 연구. 승강기 연동은 TK50M 전용 통신 모듈.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "source_unopened": false
    },
    {
      "id": "ref-947",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "한림대성심병원의 7종 73대 서비스 로봇, 제조사가 다른 로봇의 통합관제 시스템·커맨드센터, 2023년 로봇 배송 27,300건을 전한 탐방 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "source_unopened": false
    },
    {
      "id": "ref-948",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "국가기술표준원이 로봇의 승강기 탑승 안전 요구사항과 실내 배송 로봇 KS 를 제정한다고 알린 보도자료. 속도 제어·보호 정지·높낮이차·틈새·추락 방지 요구, 행정안전부 협력.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "source_unopened": false
    },
    {
      "id": "ref-949",
      "org": "Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI)",
      "title": "A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?",
      "published": "2024-06-05",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "2018년 이후 간호 협동로봇 연구 28편의 체계적 검토. TRL 4~5 다수, 미국 병원의 TUG 등 배송 로봇에 대한 동료 심사 근거 부족, 비용·유지보수·사이버보안 분석 미흡을 지적.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full",
      "source_unopened": false
    },
    {
      "id": "ref-950",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "2020년부터 물류·웨어러블·의료·기타 네 분야의 서비스로봇 도입을 국비 50% 이내로 지원하는 실증사업의 목적·분야·절차 안내.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "source_unopened": false
    },
    {
      "id": "ref-951",
      "org": "비즈한국",
      "title": "병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까",
      "published": "2025-04-10",
      "url": "https://bizhankook.com/articles/29394.html",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "국내 병원 로봇 도입 현황(한림대의료원·울산대병원·서울대병원), 서비스로봇 실증사업·스마트병원 사업(선도모델 58개), 의료진 평가와 비용·건축 구조 장애 요인을 정리한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://bizhankook.com/articles/29394.html",
      "source_unopened": false
    },
    {
      "id": "ref-952",
      "org": "최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3))",
      "title": "감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여",
      "published": "2023",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "감염환자 이송 로봇의 서비스 품질에 대한 의료종사자 인식을 SERVQUAL 다섯 차원과 AHP 로 조사해 안전 최우선, 기기 오류 해결·응급처치·환자 모니터링·감염 인자 억제의 중요성을 확인한 국내 논문(KCI 초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683",
      "source_unopened": false
    },
    {
      "id": "ref-953",
      "org": "한국보건산업진흥원 스마트병원 확산지원센터",
      "title": "선도모델 및 모듈 소개",
      "published": null,
      "url": "https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "스마트병원 선도모델 58개를 9개 모듈로 재구성한 안내. '지능형 원내 물류 배송'(자율주행 로봇+생체인증 무인 배송)과 '하나로 감염관리'(출입 통제·동선·혼잡도·환경 소독 자동화) 모듈 정의.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040",
      "source_unopened": false
    },
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "source_unopened": false,
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null
    },
    {
      "id": "ref-911",
      "org": "Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2))",
      "title": "Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda",
      "published": "2021",
      "url": "https://doi.org/10.1016/j.ejor.2021.01.019",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. AMR 의 분산 의사결정 특성과 제조·창고·크로스독·터미널·병원 적용 분야, 관리자용 계획·제어 프레임워크와 연구 의제를 제시한 문헌 검토(이전 실행 2026-09-29-11 등록).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
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
      "rationale": "섹션 3: f1(로봇 이송이 배송 시간·처리 건수·교차 감염 위험을 줄임), f11·f12(정부가 2020년부터 병원 로봇 도입을 지원), f15(상업 도입에 비해 동료 심사 근거가 부족) / 섹션 4: f4(의료 로봇 미들웨어 RoMi-H), f3(승강기 가동률), f6(등재 프로그램), f13(스마트병원 선도모델·지능형 원내 물류 배송 모듈), f16(감염환자 이송 로봇) / 섹션 5(현장 유형 모두 병원): 약품·린넨 이송 — f7(분당서울대병원, 야간·워킹갤러리), f8·f9(한림대성심병원 7종 73대·통합관제·검체·실외), f3(고대구로병원 승강기 혼잡), f10·f11(국내 도입 병원 목록·울산대병원 항암제 이송·도입 포기 사례), 해외 — f1·f2(중국 산시성 인민병원 10대), f4·f5·f6(싱가포르 창이종합병원 RoMi-H), 여섯 항목 정리는 f20, 작업 형태 지도는 f19 / 섹션 6: 승강기·자동문 연동 f2·f3·f7, 이기종 미들웨어 f4·f5·f18, 수령 인증 f2·f13, 야간 배송·동선 분리 f7, 승강기 혼잡 모델링 f3, 정착 과정 f9 / 섹션 7: f3(ISO 13482), f14(KS 로봇 승강기 탑승 안전 요구사항·실내 배송 로봇, 번호 미확인), f4·f18(Open-RMF/RoMi-H, ref-004 재사용), f6(등재 프로그램), f12·f13(서비스로봇 실증사업·스마트병원 선도모델) / 섹션 8: f15(간호 협동로봇 체계적 검토), f1·f2(효과 분석 논문), f3(승강기 타당성 논문), f16(국내 인식 연구), f17(AMR 문헌 검토, ref-911 재사용) / 섹션 9: f21(직접 범위: 이송 요청 수신·이기종 배정·승강기·자동문 예약·감염 구역·야간·권한 제약 반영·수령 인증 완료 확인·결과 반환·혼잡 시 재계획), f22(연계 대상: HIS·EMR·약국 시스템, 승강기 제어반·자동문, 로봇 자율 주행·안전 기능, 감염 관리 규정·환자 정보 보호 법령) / 섹션 10: f23 — 3. 경제성·조달·사업 모델, 17. 작업 대상·자산 식별과 인계 추적, 19. 사람·보행자 모델, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 28. 공용 자원·충전·에너지 최적화, 32. 예외 복구·재계획·업무 연속성, 39. 운영 성과 측정·개선, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사, 51. 인증·권한·격리, 53. 개인정보·영상 데이터, 55. 현장 조사·설치·시운전, 56. 운영 이관·확대·교육, 58. 다사업자 책임·계약·데이터 / 섹션 11: 기존 oq-149(f24, 부분 답이나 미해결)·oq-134·oq-138·oq-142(f25, 미해결)와 open_questions_new 5건. 벤더 주장 finding 없음(모든 성과 수치는 논문·정부 자료·기사 기준이며 f1·f3 수치는 단일 병원 조건임을 명시). 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f3·f14 반영, 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성 페이지에 f4·f6 반영, 58. 다사업자 책임·계약·데이터 페이지에 f6(등재 프로그램) 반영, 17. 작업 대상·자산 식별과 인계 추적 페이지에 f2·f13(RFID·생체인증 수령 확인) 반영, 53. 개인정보·영상 데이터 페이지에 이동형 영상정보처리기기 규정의 병원 로봇 적용 조사(이번 실행에서 원문 미열람) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "의료 로봇 미들웨어 RoMi-H",
      "term_en": "Robotic Middleware for Healthcare (RoMi-H)",
      "definition": "싱가포르 창이종합병원 CHART 가 Open-RMF(ROS 2·DDS) 위에 만든 오픈소스 미들웨어로, 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 기계·제어·중앙·통합 네 도메인으로 잇고 승강기 같은 공용 자산을 공유하게 하며 싱가포르 보건부가 공공 의료기관의 자동화 통합 플랫폼으로 인정한다."
    },
    {
      "term_ko": "승강기 가동률",
      "term_en": "Elevator Operating Rate (EOR)",
      "definition": "병원처럼 승강기를 사람·침대·로봇이 함께 쓰는 건물에서 승강기가 사용 중인 시간 비율로, 고대구로병원 연구는 가동률이 높을수록 배송 로봇의 승강기 대기가 길어지고 임무 실패가 늘어난다는 관계를 보여 로봇 배차·재계획의 제약 변수로 쓸 수 있다."
    },
    {
      "term_ko": "등재 프로그램",
      "term_en": "Empanelment Programme",
      "definition": "공공 기관이 벤더·시스템 통합사의 기술 전문성과 배치 역량을 사전에 평가해 일정 기간 유효한 자격을 주고 조달 제안 요청(RFP·RFI)에 참여할 수 있는 목록에 올리는 제도로, 싱가포르 CHART 가 RoMi-H 배치 통합사를 대상으로 격년 운영한다."
    },
    {
      "term_ko": "스마트병원 선도모델",
      "term_en": "Smart Hospital Leading Model",
      "definition": "보건복지부·한국보건산업진흥원이 2020년부터 정보통신기술로 환자 안전과 의료 질을 높이는 병원 모델을 개발·검증하도록 지원한 사업의 산출물로, 개별 선도모델 58개가 지능형 원내 물류 배송(자율주행 로봇+생체인증 무인 배송)·하나로 감염관리 등 9개 모듈로 재구성됐다."
    }
  ],
  "open_questions_new": [
    "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? | 관련 영역: 63. 병원·의료, 53. 개인정보·영상 데이터 | 근거: f22 | 종류: 일반",
    "격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가? | 관련 영역: 63. 병원·의료, 48. 안전·위험 관리 | 근거: f2 | 종류: 일반",
    "국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가? | 관련 영역: 63. 병원·의료, 22. 설비·건물 시스템 연동, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 일반",
    "한림대성심병원처럼 제조사가 다른 여러 로봇을 통합관제하는 국내 병원은 어떤 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API)으로 로봇과 승강기를 연결하며 그 구조가 공개돼 있는가? | 관련 영역: 63. 병원·의료, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반",
    "국내 병원에서 식사(환자식) 이송을 로봇이 맡은 운영 사례가 있으며, 식사 이송은 약품·검체 이송과 시작 조건·시간 제약·인계 방식이 어떻게 다른가? | 관련 영역: 63. 병원·의료 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 3,
    "unverified": [
      "f1·f2 산시성 인민병원 수치(32~36%·7.3배·이용률 0.84)는 단일 논문이며 독립 출처 교차 확인 실패",
      "f3 고대구로병원 성공률(87.03%·95.52%)은 단일 논문·단일 로봇·12일 기간이며 교차 확인 실패",
      "f4 의 두 출처(창이종합병원 CHART, Open Robotics)는 같은 프로젝트의 참여 기관이라 독립성이 제한적",
      "f6 RoMi-H 등재 프로그램 페이지의 발행일 미확인, 등재 통합사 목록의 기준 시점 미확인",
      "f7 분당서울대병원(이데일리)·f9·f10(뉴스투데이·데일리팜)·f11(비즈한국) 사례는 각각 발행 주체 한 곳",
      "f8 의 교차 확인은 '제조사가 다른 로봇의 공존'만이며 로봇 대수·건수(73대·27,300건)는 로봇신문 단독",
      "f13·f14 의 출처 페이지 발행일 미확인(스마트병원 모듈 소개), KS 표준 번호·정식 명칭 미확인",
      "f16 품질경영학회지 논문은 PDF 텍스트 추출 실패로 KCI 초록만 확인",
      "개인정보 보호법 제25조의2 원문(law.go.kr 연결 끊김, casenote 403)을 열지 못해 환자 정보 보호 법령 finding 을 내지 못하고 열린 질문으로 남김",
      "American Journal of Infection Control 2023 감염 예방 로봇 체계적 검토와 Journal of Hospital Infection 2025 응급실 AMR 소독 연구는 출판사 403·Semantic Scholar 429 로 열지 못해 출처 제외",
      "Panasonic HOSPI ISO 13482 인증 페이지 403 으로 제외(ISO 13482 근거는 f3 논문으로 대체)",
      "세계비즈 도구공간·고대구로병원 실증 기사는 프록시 거부로 열지 못함(같은 사례는 f3 논문으로 확인)",
      "메디칼타임즈(2026-02-03)의 삼성서울병원 야간 승강기 혼잡 회피 운영 사실과 머니투데이(2026-04-14)의 서울대병원·하버드의대 임상 환경 시뮬레이터는 열었으나 출처 상한 15건으로 제외",
      "oq-149 부분 답: 싱가포르 등재 프로그램의 현황은 확인했으나 국내 유사 제도는 미확인(f24)",
      "oq-134·oq-138·oq-142 미해결: 국내 병원의 운영 기록 시뮬레이션 재현·대화형 시나리오 구성·대화형 다중 로봇 지시 사례 미확인(f25)",
      "ref-004·ref-911 재사용 항목은 참고문헌 목록 입력이 0건이라 등록된 기관·제목·URL 과 글자 단위로 대조하지 못함"
    ],
    "scope_violations": [
      "f22: HIS·EMR·약국 시스템의 처방·조제 판단, 승강기 제어반·자동문 제어, 로봇의 자율 주행·회피와 ISO 13482 안전 기능, 감염 관리 규정·환자 정보 보호 법령은 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어·업종별 조건 쪽이므로 '연계 대상: '으로 표시함",
      "f3·f14: 승강기 연동 방식과 KS 안전 요구는 22. 설비·건물 시스템 연동·50. 안전 표준·인증·사고 조사 의 핵심이므로 이 영역에서는 병원 이송의 제약 근거로만 제안함",
      "f4·f5·f6: RoMi-H 미들웨어 구조와 등재 제도는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성·58. 다사업자 책임·계약·데이터 와 겹치므로 이 영역에서는 병원 현장의 이기종 로봇 운영 사례로만 제안함",
      "f2·f13: RFID·생체인증 수령 확인은 17. 작업 대상·자산 식별과 인계 추적·51. 인증·권한·격리 의 방법이므로 이 영역에서는 완료·인계 조건의 근거로만 제안함",
      "f15: 사이버보안 분석 부족 지적은 53. 개인정보·영상 데이터 와 연결하되 환자 정보 보호 법령 자체는 이번 실행에서 확인하지 못함"
    ],
    "budget_used": {
      "queries": 14,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 14회/30, 신규 출처 15건/15(ref-939~ref-953, 예약 구간 ref-939~ref-968 안) 상한 도달로 메디칼타임즈 삼성서울병원 야간 운영 기사, 머니투데이 서울대병원 임상 환경 시뮬레이터 기사, 개인정보 보호법 제25조의2 원문(열람 실패), AJIC·JHI 감염 관리 논문(열람 실패), Panasonic HOSPI ISO 13482 페이지(403), Aethon TUG 벤더 자료, 서울대병원 의료 LLM 보도자료는 넣지 못했다. 원문 열람 15건(모두 webfetch: PMC 논문 원문 2(ref-939·ref-946), Frontiers 원문 1, KCI 초록 1, 창이종합병원 CHART 페이지 2, Open Robotics 블로그 1, 국가기술표준원 보도자료(KDI 게재) 1, 한국로봇산업진흥원·한국보건산업진흥원 페이지 2, 기사 5), 재사용 미열람 2건(ref-004·ref-911 은 이번에 다시 열지 않아 fetched false·source_unopened true). 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 Open-RMF·Fragapane 검토·RoMi-H 관련 페이지가 전체 936건과 URL 이 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 합칠 때 확인해야 한다(ref-911 은 직전 실행 2026-09-29-11 이 부여한 id 를 그대로 썼다). 교차 확인 3건(f4: CHART/Open Robotics — 같은 프로젝트 참여 기관이라 독립성 제한, f8: 로봇신문/데일리팜 — 이기종 제조사 공존 사실만, f12: 한국로봇산업진흥원/비즈한국 — 사업 존재·시작 연도만). 신뢰도 high 는 f4(정부·연구기관 원문 열람 + 오픈소스 문서)·f12(정부·연구기관 원문 열람 + 기사) 두 건이며 검증에서 medium 으로 낮아질 수 있다. 벤더 주장 finding 없음: 도구공간 직원이 공저한 f3 은 병원이 주저자인 동료 심사 논문이라 벤더 문서로 보지 않았고, 성과 수치는 모두 논문·정부·기사 출처다. 분류 원문 핵심 질문(감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가)에는 작업 형태 지도 f19, 여섯 항목 정리 f20, 직접 범위 f21, 연계 대상 f22 로 답했으며 결론은 '감염 관리는 비접촉 배송·야간 동선 분리·감염 구역 제약·방역 모듈로, 환자·약품 정보 보호는 RFID·생체인증 수령 확인과 권한 통제로 다루고, 승강기 혼잡이 병원 특유의 핵심 제약이며, 이기종 로봇을 하나의 표준 계층으로 묶은 공개 사례는 싱가포르 RoMi-H 이고 국내는 통합관제 언급 수준'이라는 추정이다. 환자 정보 보호의 법령 근거(개인정보 보호법 제25조의2)는 원문을 열지 못해 finding 대신 열린 질문으로 남겼다. 현장 유형: 모두 병원(국내 분당서울대·한림대성심·고대구로·울산대 등, 해외 싱가포르 창이종합병원·중국 산시성 인민병원, 학술 검토)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다(f9 의 실외 배송로봇은 병원 부지 안 이동으로 병원 사례에 둠). 국내 자료는 고대구로병원 논문(f3)·품질경영학회지 논문(f16)·국가기술표준원(f14)·한국로봇산업진흥원(f12)·한국보건산업진흥원(f13)·이데일리(f7)·로봇신문(f8)·뉴스투데이(f9)·데일리팜(f10)·비즈한국(f11) 열 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다(f3 의 몬테카를로 모형은 사전 타당성 분석으로 34 쪽 성격이나 이번 연결 제안에는 넣지 않음). 용어집에 이미 있는 승강기 어댑터·플릿 어댑터·오픈 RMF·이동형 영상정보처리기기·플릿 관리 시스템·기술 성숙도·서비스형 로봇은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 4건(oq-134·oq-138·oq-142·oq-149)은 조사 질문에 넣고 검색 2회를 배분했으나 oq-149 는 부분 답(f24), 나머지는 미해결(f25)로 남긴다. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-13/verification.json

```json
{
  "run_id": "2026-09-29-13",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC 원문 열람: Scientific Reports 2026-04-24, Li M. 외, 산시성 인민병원 500병상·22개 개방 병동, 로봇 10대(R0033-A1, 200kg·약 7시간), 2025-06-01~11-30 6개월, 배송 시간 32~36% 단축(p<0.001), 19명 대비 7.3배, 검증 정확도·온전율 100% vs 97%·99%, 10년 692.8만 위안·회수 3.4년, 정기·수시 두 방식 모두 원문과 일치. 검색으로 Nature·PubMed 판을 찾았으나 같은 논문이라 독립 출처가 아니며 수치는 단일 병원·단일 연구 조건임을 본문에 병기해야 한다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 같은 원문에서 IoT 승강기 제어 모듈, RFID 신원 확인, 비접촉 배송, 약국·검사실/병동/시스템 관리자/장비 관리자의 협력 책임 체계, λ=42건/시간·ρ=0.84 확인. 원문은 'equipment administrators'라 '장비 정비 인력'은 '장비 관리자'로 고친다. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC 원문 열람: Digital Health 2026-03-31, Lee Y. 외(고려대 구로병원·DOGU), IROI 로봇, ISO 13482 적합 인증 시험, 2025-06-18~29, 122건, 약국→응급실, 성공률 87.03%, EOR 59% 미만 95.52%(최적 절단값 59.01%), AUC 0.779(0.661–0.882), TK50M 전용 통신 모듈, 단일 기관·단일 플랫폼 한계 모두 일치. 검색(ZDNet·바이오타임즈·영남일보 2025-02-18)으로 도구공간의 고대구로병원 실증 존재와 승강기 직접 통신은 확인되나 성공률 수치는 논문 단독이고, 언론은 실증에 이로이 2대 투입이라 전하므로 본문에서는 '논문이 분석한 로봇 1대'로 한정해 쓴다. 성공률 수치는 교차 확인되지 않아 단일 병원·12일 조건 병기 필요."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CHART 페이지: Robotic Middleware for Healthcare, 2018-07 보건부 장관 발표, 2019-10-31 ROSCon 공개, DDS 기반, 기계·제어·중앙·통합 네 도메인, 공공 의료기관 상호운용 목적 문구, Open-RMF 저장소 안내 확인. 협력 기관(IHiS·HopeTechnik·GovTech)과 RMF(ROS 2) 기반은 Open Robotics 블로그에서 확인되며 CHART 페이지에는 기관 목록이 없다. 두 출처가 같은 프로젝트의 참여 기관이라 독립 교차 확인으로 세지 않으며 finding 신뢰도 high 는 medium 으로 낮춘다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Open Robotics 블로그 원문 열람: RMF(ROS 2) 기반, 여러 제조사 로봇의 승강기·복도 공유, 경로 계획 시각화와 충돌 회피 구역, 'uniform communication and monitoring across robot platforms, sensors, and enterprise information systems', 보건부·국가로봇프로그램 지원 일치. 페이지 표시 날짜는 2월 11일이나 URL 경로가 2021/2/10 이라 브리프 발행일을 유지한다. 단일 출처(프로젝트 참여 기관 글)."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CHART 등재 프로그램 페이지 열람: 보건부가 공공 의료 자동화 통합 플랫폼으로 지정, 기술 전문성·배치 지식 평가, 2025-05-01 효력·2년 유효, CHART 사이트 게시·RFP/RFI 참여, 등재 통합사 5개(HOPE Technik·Medisys Innovation·Panasonic Asia Pacific·QuikBot Technologies·Techfox) 일치. 페이지에 발행일 2025-05-01(갱신 2026-08-24)이 표시되므로 브리프의 발행일 미확인은 오류다. 원문 표기 'bi-annual'은 2년 주기인지 연 2회인지 불명확해 '격년'으로 단정할 수 없다. 단일 출처(기관 공식 페이지)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 이데일리 2023-07-06 원문 열람: KT 5G 특화망, AMR 6대, 워킹갤러리 약 300m, 진료재료·약품·린넨(환자복·침대 시트·이불), 승강기·자동문 다중 연동, 1.5km 차량 운송 대체, 야간 배송, 인용문 일치. 검색으로 쿠키뉴스·아주경제·전자신문·의약뉴스(2023-07-06~07)가 AMR 6대·워킹갤러리·품목을 같은 내용으로 보도함을 확인(같은 보도자료 기반이라 독립성 제한, 300m·1.5km·야간 문구는 이데일리 단독)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 로봇신문 2024-04-15 원문 열람: 7종 73대, 통합관제 시스템 인용문, 2023년 2만 7,300여 건·월평균 2,250건 이상 일치(로봇 종류는 '배송·안내·물류·홈케어·방역'으로 적혀 있어 '비대면 협진'은 확인되지 않음). 데일리팜 2024-07-15 원문에서 LG전자(한림대성심·용인세브란스 공급)·빅웨이브로보틱스(한림대성심 담당) 확인. 검색으로 메디칼업저버·한림대 공지가 7종 73대(2022-08 도입 시작)·2023년 27,300건을 같은 수치로 보도함을 확인해 대수·건수 교차 확인. 비즈한국 2025-04-10 은 11종 77대라 전하므로 73대는 2024-04 기준임을 문장에 유지한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 뉴스투데이 2025-02-11 원문 열람: 약제나르미의 단독 승강기 탑승·간호사 스테이션 대기, 내시경실 세포조직을 포름알데히드 통에 담아 병리과로 운반, 실외 배송로봇의 신호등 인식 횡단보도 통과, 커맨드센터 부센터장(김영미)의 사용자 공감대·약 3년 정착·보급형 로봇 제약에 맞춘 시스템 변경 발언 일치. 단일 출처."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": false,
      "tag_decision": "유지",
      "cross_checked": false,
      "note": "부분 뒷받침. 데일리팜 원문 열람 결과 약 배송로봇을 시범 운영·정식 도입한 곳은 '양산부산대병원, 용인세브란스병원, 한림대성심병원, 조선대병원, 삼성서울병원 등'이고, 해운대백병원·의정부을지대병원·일산차병원은 '환자 안내용 로봇을 운영'한다고 적혀 있어 8곳을 약 배송로봇 도입 병원으로 묶은 것은 출처와 다르다. XaaS 선도 프로젝트 56억 원·5개 과제 중 빅웨이브로보틱스 선정, 자동출입문·통로 협소·승강기 턱 인용문, 신축 병원 위주 도입은 일치. 수정 지시대로 병원 목록을 고치는 조건으로 [사실] 유지(고친 문장은 출처가 직접 뒷받침한다)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 비즈한국 2025-04-10 원문 열람: 2020년부터 한국로봇산업진흥원·한국보건산업진흥원 사업, 선도모델 58개, 울산대학교병원 2022년 항암제 이송로봇 '케로', 약사·간호사 인용문, 속도·안전성·물류 복잡성 지적, 지정맥 생체인증·AI 안면인식 일치. 다만 비용은 '억 단위', 경사는 '경사 구간', 승강기는 '건물이 나뉘어 각기 다른 회사의 승강기가 설치'로 적혀 있어 '수억 원'·'경사로'·'승강기 호환'은 출처 표현으로 고친다. 울산대병원 뉴스룸 보도자료·데일리메디 검색 결과로 케로 도입 사실 교차 확인(수치 없음)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 한국로봇산업진흥원 페이지 열람: 시장창출 한계 극복 문구, 2020년 시작(2012~2019 보급사업 후속), 물류·웨어러블·의료·기타(협동·언택트) 네 분야, 국비 50% 이내·민간 현금 50% 이상, 공모→서류·발표·현장평가→선정→협약→중간점검→최종평가 일치. 비즈한국이 2020년 시작을 독립적으로 전해 사업 존재·시작 연도만 교차 확인. 세부 조건은 진흥원 단독이므로 finding 신뢰도 high 는 medium 으로 낮춘다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 한국보건산업진흥원 스마트병원 확산지원센터 페이지 열람: 선도모델 58개를 9개 모듈로 재구성, 모듈 이름 9개, '지능형 원내 물류 배송' 인용문, '하나로 감염관리'의 출입 통제·동선 분석·혼잡도 관리·환경 소독 일치. 페이지 발행일 없음(확인일 기준). 58개는 비즈한국과도 일치하나 비즈한국이 진흥원 자료를 인용한 것이라 독립 교차 확인으로 세지 않는다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KDI 경제정보센터 게재 국가기술표준원 보도자료(2021-11-11) 열람: 2020-10 로봇산업 선제적 규제혁신 로드맵, 행정안전부 협력, 속도제어·보호정지·높낮이차·틈새극복·추락·넘어짐 방지 일치, 표준 번호·정식 명칭 없음. 검색 결과(KSSN 표준 검색)에 'KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'이 나타나나 원문을 열지 않았으므로 페이지에 넣지 않고 열린 질문의 단서로만 남긴다. 발행 후 4년이 지나 월간 재검증 대상."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Frontiers 원문 열람: 2018년 이후 28편, TRL 4 가 6편·TRL 5 가 8편·TRL 7 이 5편·TRL 9 는 1편, 환자 중심 설계가 다수(간호사 명시 대상은 9편), 'generally strikingly lacking' 인용(TUG·Moxi), 비용·유지보수·적응성·사이버보안 분석 부족 일치. TRL 4~5 는 28편 중 14편이므로 '대부분'은 과장이며 '다수(14편)'로 고친다. 단일 출처(체계적 검토)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI 페이지 열람: 품질경영학회지 51(3), 2023, pp.381-401, 저자·소속(경희대·Korea SUNY), SERVQUAL 다섯 차원, AHP, 이송 안전 최우선·기기 오류 해결·응급처치·환자 모니터링·감염 인자 억제 일치. 다만 두 차례 열람에서 설문 배포·회수·분석 부수(30·24·23)는 표시된 초록에서 확인되지 않아 응답 수는 '미확인'으로 두거나 뺀다. 초록만 확인(본문 PDF 미열람)."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(doi 는 Elsevier 리다이렉트 페이지에서 멈춤). 검색 결과(RePub·SINTEF·ScienceDirect·Semantic Scholar)의 기관·제목·권호(EJOR 294(2), 405–426, 2021)가 일치하고 초록 스니펫이 'manufacturing, warehousing, cross-docks, terminals, and hospitals'를 적용 분야로 들어 주장 범위 안이다. 재사용 출처 ref-911, 브리프의 source_unopened 표시 적절. 각주에 ' (원문 미열람)' 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력의 data/source_texts/ref-004.txt(RMF Core 원문)가 플릿 어댑터, 문·승강기·디스펜서 연동, 교통 스케줄·협상 구조를 뒷받침하고 Open Robotics 블로그(ref-945)가 RoMi-H 의 RMF 기반과 승강기 공유를 뒷받침한다. 병원 참고 구조라는 부분은 추론이므로 [추정] 적절. ref-004 의 summary 가 '원문 미열람.'으로 시작하나 fetched true·원문 텍스트 입력이 있어 실제로는 열람한 것으로 본다(브리프 표기 불일치)."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정]. 다섯 작업 형태는 f1·f3·f7·f8·f9·f10·f11·f13·f16 으로 뒷받침되나, '마약류'는 어느 finding·출처 발췌에도 없고 '수술실' 검체 이송도 f1(병동→검사실)·f9(내시경실→병리과)에 없다(고대구로 실증의 수술실 검체 언급은 열지 않은 언론 자료에만 있음). 두 단어를 빼는 조건으로 유지. 식사 이송 미확인 명시는 적절."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정]. 여섯 항목 배정이 각 finding 의 확인 내용과 맞는다(f19 의 '마약류'를 이어받지 않도록 작업 대상 문구를 f19 수정에 맞춘다). 수치 조건 한정 문구 적절."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정]. 직접 범위 서술이 f2·f3·f4·f6·f7·f8·f13 의 확인 내용에서 벗어나지 않고 분류 원문 19장 왼쪽 열(요청 수신·예약·인계·상태 확인)에 대응한다. '국내는 통합관제 언급 수준'이라는 한정도 f8 원문과 맞는다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정], '연계 대상:' 표시 적절. HIS·EMR(상위 업무 시스템), 승강기 제어반·자동문(시설·설비 제어), 자율 주행·ISO 13482 안전 기능(로봇 자체 지능·제어), 감염 관리·환자 정보 법령(업종별 조건) 배치가 원문 19장 표와 맞는다. 환자 정보 보호 법령은 이번 실행에서 원문 미확인이므로 페이지에서 법령 조문 내용을 쓰지 않는다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정]. 열여섯 영역 연결이 각 finding 의 확인 내용에 근거하고 번호+이름 표기가 부록 A 와 일치한다. 19. 사람·보행자 모델 연결(야간 동선 분리, f7)은 이데일리 원문의 '환자 동선 최소화'로 뒷받침된다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]. oq-149 에 대한 부분 답: 싱가포르 등재 프로그램 현황(f6)은 확인됐고 국내 벤더 사전 평가 제도 미확인 진술은 조사 한계로 정직하게 적혀 있다. oq-149 는 해결로 바꾸지 않는다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]. oq-134·oq-138·oq-142 미해결 진술과 가장 가까운 국내 자료(f3 몬테카를로 모형, f8 통합관제) 대응이 확인 내용과 맞는다. 세 질문은 해결로 바꾸지 않는다."
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
      "f17(Fragapane 외 AMR 문헌 검토)은 61. 물류창고 브리프(2026-09-29-11) f3 과 같은 출처·같은 취지의 주장이므로 기존 각주 ref-911 을 재사용한다(브리프가 이미 그렇게 함)",
      "f18(Open-RMF 참고 구조)은 61. 물류창고 f23·62. 제조 공장 f21 과 같은 ref-004 재사용 주장이며 현장 유형만 다르다 — 각주 ref-004 재사용 유지",
      "RoMi-H·등재 프로그램(f4·f5·f6)은 열린 질문 oq-149 의 대상이자 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성·58. 다사업자 책임·계약·데이터 와 겹치므로 이 페이지에서는 병원 사례로만 쓰고 10절에서 연결한다(브리프 scope_violations 대로)"
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
    "ref-944(RoMi-H Empanelment Programme 2025): 각주와 reference_updates 의 발행일을 '미확인'이 아니라 2025-05-01 로 적는다 — 페이지에 게시일 2025-05-01(갱신 2026-08-24)이 표시돼 있다. f6 의 기준일도 2025-05-01 로 쓴다.",
    "f6·용어 후보 '등재 프로그램': '격년으로 운영'을 '정기적으로(원문 표기 bi-annual) 운영'으로 바꾼다 — 원문의 bi-annual 이 2년 주기인지 연 2회인지 확인되지 않는다.",
    "f10: 도입 병원 목록을 출처대로 고친다 — 원내 약 배송로봇을 시범 운영·정식 도입한 곳은 양산부산대병원·용인세브란스병원·한림대성심병원·조선대병원·삼성서울병원 등이고, 해운대백병원·의정부을지대병원·일산차병원은 환자 안내용 로봇을 운영한다. 고친 문장은 [사실][^ref-943] 로 쓴다.",
    "f11: '대당 수억 원'을 '대당 억 단위 비용'으로, '경사로·문·승강기 호환'을 '경사 구간, 문 호환, 건물마다 다른 회사의 승강기'로 출처 표현에 맞춰 고친다.",
    "f15: '대부분이 기술 성숙도 4~5 수준'을 '28편 중 14편이 기술 성숙도 4~5 수준(TRL 9 는 1편)'으로 고친다 — 원문 집계가 TRL 4 6편·TRL 5 8편이다.",
    "f16: 설문 응답 수(30부 배포·24부 회수·23부 분석)는 KCI 초록에서 확인되지 않으므로 본문에 쓰지 않거나 '응답 수 미확인'으로 둔다. 각주에는 'KCI 초록 확인, 본문 PDF 미열람' 취지를 유지한다.",
    "f19·f20: 작업 대상에서 '마약류'와 '수술실'을 뺀다 — 어느 finding·출처 발췌에도 없다. 검체 이송의 출발지는 병동(f1)·내시경실(f9)로 쓴다.",
    "f2: '장비 정비 인력'을 '장비 관리자'로 고친다 — 원문 표현은 equipment administrators 다.",
    "f3: 본문에서 '로봇 1대로 배송'이 아니라 '논문이 분석한 로봇 1대(IROI)의 배송 122건'으로 한정해 쓰고, 성공률 87.03%·95.52% 에는 단일 기관·2025-06-18~29 조건을 같은 문장에 병기한다.",
    "f1·f2: 배송 시간 32~36%·7.3배·이용률 0.84 에는 '중국 산시성 인민병원 단일 연구·2025-06-01~11-30' 조건을 같은 문장에 병기하고 [사실] 은 유지하되 교차 확인되지 않았음을 8절 또는 검증 노트 인용에 남긴다.",
    "f4: 두 출처(창이종합병원 CHART, Open Robotics)는 같은 프로젝트 참여 기관이므로 교차 확인으로 서술하지 않고 신뢰도는 medium 으로 쓴다. 협력 기관 목록(IHiS·GovTech·Hope Technik)은 ref-945 에만 있으므로 그 문장의 각주는 [^ref-945] 를 포함한다.",
    "f12: 신뢰도를 medium 으로 쓴다 — 국비 50%·절차 등 세부 조건은 한국로봇산업진흥원 단독이며 비즈한국은 사업 존재·시작 연도만 확인한다.",
    "f8: 로봇 종류 서술에서 '비대면 협진'을 빼고 로봇신문 원문대로 '배송·안내·물류·홈케어·방역'으로 쓴다. 7종 73대·27,300건은 '2024-04 기준'을 문장에 유지한다(비즈한국 2025-04 는 11종 77대라 전한다).",
    "용어 후보 '스마트병원 선도모델': 정의에서 '보건복지부'를 뺀다 — 근거 finding(f11·f13)에 보건복지부가 없고 한국보건산업진흥원만 확인됐다.",
    "용어 후보 '승강기 가동률': 정의를 '고대구로병원 연구가 쓴 지표로, 가동률이 높을수록 배송 실패가 늘었다'는 관계 서술로 한정하고 계산 방식(사용 중인 시간 비율)은 원문 확인 범위 밖이므로 쓰지 않는다.",
    "5. 적용 사례 절: 모든 사례에 현장 유형 '병원'을 명시하고, 국내(분당서울대·한림대성심·고대구로·울산대)와 해외(창이종합병원·산시성 인민병원)를 나눠 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과)에 놓는다. site_matrix_updates 의 site_type 은 모두 '병원'이다.",
    "f17(ref-911)의 각주 접근일 뒤에 ' (원문 미열람)' 을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 둔다.",
    "11. 열린 질문 절: oq-134·oq-138·oq-142·oq-149 는 해결로 바꾸지 않고 f24·f25 의 부분 답·미해결 결과를 적는다. open_questions_new 5건은 브리프 형식 그대로 등록한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 23건, 미확인 2건(f10 병원 목록 일부 불일치, f19 근거 없는 '마약류·수술실'), 교차 확인 4건(f7 분당서울대 AMR 6대·품목, f8 한림대성심 7종 73대·27,300건, f11 울산대병원 항암제 이송로봇 케로, f12 서비스로봇 실증사업 2020년 시작). 강등: 없음(f4·f12 의 finding 신뢰도 high 는 medium 으로 낮춤). 원문 미열람 출처: ref-911(검색 결과 일치). 주의: 핵심 성과 수치(f1 배송 시간 32~36%·7.3배, f3 성공률 87.03%·95.52%)는 각각 단일 병원·단일 연구의 결과로 독립 출처 교차 확인이 없으며, f4 의 두 출처는 같은 프로젝트 참여 기관이라 독립적이지 않다. ref-944 는 페이지에 발행일 2025-05-01 이 표시돼 브리프의 '미확인'이 오류다. ref-004 는 입력 원문 텍스트로 열람했으나 브리프 summary 가 '원문 미열람.'으로 시작해 표기가 어긋난다(퍼블리셔 확인 필요). 미사용 출처 없음. 정정 요청 없음. oq-149 는 부분 답(f24)이며 해결 인정하지 않음, oq-134·oq-138·oq-142 미해결 유지. 검증 검색 8회(리서치 14회와 합쳐 22/30). 열린 질문 단서: KSSN 표준 검색 결과에 'KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'이 나타나나 원문 미열람이라 페이지에 넣지 않았다. 페이지 신뢰도 medium.",
  "retry_reason": null
}
```

### docs/categories/site-type-applications/hospital-and-healthcare.md

```markdown
---
title: "63. 병원·의료"
type: area
category: "Q. 현장 유형별 적용"
area_no: 63
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 63. 병원·의료

# 63. 병원·의료

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]

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
| **63. 병원·의료** | 검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 | 감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? | [63. 병원·의료](hospital-and-healthcare.md) | seed |
| **64. 상업 시설** | 호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 | 손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? | [64. 상업 시설](commercial-facilities.md) | seed |
| **65. 가정·공동주택** | 집안일 보조, 공동주택 배송, 사생활 | 가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? | [65. 가정·공동주택](home-and-apartment.md) | seed |
| **66. 실외** | 실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 | 보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? | [66. 실외](outdoor.md) | seed |
| **67. 기타 현장** | 점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 | 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? | [67. 기타 현장](other-sites.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

물류창고는 여러 현장 유형 가운데 하나다. 현장마다 다른 요구는 여기에 모으고, **모든 현장에 공통인 기능은 A~P에 둔다**. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 35건이다(논문 15건 · 기사·보고서 8건 · 업체 발표 6건 · 표준·오픈소스·기관 자료 6건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-928](../../references/ref-928.md) — Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors (발행 2024-12-02)
- [ref-933](../../references/ref-933.md) — Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35), Collaborative robots in manufacturing and assembly systems: literature review and future research agenda (발행 2023-05-30)
- [ref-913](../../references/ref-913.md) — 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례 (발행 2022)
- [ref-914](../../references/ref-914.md) — 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)), 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구 (발행 2021)
- [ref-911](../../references/ref-911.md) — Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)), Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda (발행 2021)
- [ref-005](../../references/ref-005.md) — Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses (발행 2020)
- [ref-925](../../references/ref-925.md) — Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M., Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL (발행 2019-11-13)
- [ref-912](../../references/ref-912.md) — Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J., Integration of returns and decomposition of customer orders in e-commerce warehouses (발행 2019-09-01)
- [ref-910](../../references/ref-910.md) — Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)), Robotized and Automated Warehouse Systems: Review and Recent Developments (발행 2019-06-28)
- [ref-922](../../references/ref-922.md) — Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)), A classification of tactical assembly line feeding problems (발행 2019-02-23)
- 그 밖에 5건

**기사·보고서**

- [ref-931](../../references/ref-931.md) — 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 (발행 2026-09-07)
- [ref-932](../../references/ref-932.md) — 테크데일리, KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개 (발행 2025-03-12)
- [ref-927](../../references/ref-927.md) — 물류신문 (이경성), LG전자, 스마트팩토리 솔루션 확대에 AMR 등 물류로봇 적극 활용한다 (발행 2024-07-18)
- [ref-918](../../references/ref-918.md) — 물류신문 (석한글), ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니 (발행 2023-02-07)
- [ref-917](../../references/ref-917.md) — 로봇신문 (장길수), 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이... (발행 2023-02-07)
- [ref-921](../../references/ref-921.md) — Robotics 24/7 (Eugene Demaitre), DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers (발행 2023-02-01)
- [ref-915](../../references/ref-915.md) — 로봇신문 (장길수), CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3' (발행 2022-05-06)
- [ref-257](../../references/ref-257.md) — Interact Analysis, AMR Multi-Fleet Orchestration Software Explained (발행 미확인)

**업체 발표**

- [ref-924](../../references/ref-924.md) — SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW (발행 2025-10-16)
- [ref-916](../../references/ref-916.md) — Amazon, Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot (발행 2025-07)
- [ref-930](../../references/ref-930.md) — 현대자동차그룹, ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 (발행 2023-11-21)
- [ref-920](../../references/ref-920.md) — CJ대한통운, CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 (발행 2023-10-26)
- [ref-938](../../references/ref-938.md) — Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) (발행 미확인)
- [ref-926](../../references/ref-926.md) — Siemens, AGV fleet management integration with intralogistics (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-923](../../references/ref-923.md) — Verband der Automobilindustrie (VDA), VDA 5050: Managing Transport in Manufacturing Plants (발행 미확인)
- [ref-919](../../references/ref-919.md) — 스마트물류시설인증센터 (한국교통연구원), 인증스마트물류센터 : 인증심사 > 심사기준 > 일반 (발행 미확인)
- [ref-124](../../references/ref-124.md) — 국가물류통합정보센터(국토교통부), 스마트물류센터 인증제 안내 (발행 미확인)
- [ref-101](../../references/ref-101.md) — Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) (발행 미확인)
- [ref-004](../../references/ref-004.md) — Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2 (발행 미확인)
- [ref-003](../../references/ref-003.md) — GS1, EPCIS and CBV Linked Data Model (발행 미확인)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [62. 제조 공장](manufacturing-plant.md) — 섹션 3~11 신규 작성(seed → draft), 프런트매터 related_areas·tags·confidence·sources·last_run 채움, 13절 각주 16건(분리 후), 1차 수정 지시 18건 이행; 2차 수정(1회차): 4·8절 추론 [추정] 분리, 6절 세 형태 문장 정리, 약어 병기; 2차 수정(2회차): 9절 표의 PLC·ERP 첫 등장을 풀어 씀 (실행 2026-09-29-12)
- 2026-09-29 · 생성 · [62. 제조 공장 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area62-s4.md) — 자동 분리: 62. 제조 공장 의 "4. 핵심 개념과 용어" 절을 옮겼다; 2차 수정(2회차): 두 번째 자동 분리로 소실된 4절 전체 내용(견인차·언더라이드 로봇 기반 라인 공급, 운송 주문, 셀 생산 방식, 치구 없는 다중 로봇 조립, 협동로봇, 운용 구역·ISO 3691-4)을 복구하고 자기 참조 링크 줄을 삭제, 출처·프런트매터 sources·세 줄 요약을 맞춤 (실행 2026-09-29-12)
- 2026-09-29 · 생성 · [62. 제조 공장 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area62-s6.md) — 자동 분리: 62. 제조 공장 의 "6. 대표 접근법과 기술" 절을 옮겼다; 2차 수정(1회차): 1절·3절 첫 문장의 세 형태 (3) 을 '작업자와 로봇이 함께 조립하거나 두 대 이상의 로봇(로봇팔·이동 플랫폼)이 치구 없이 조립하거나'로 고침(2회차 변경 없음) (실행 2026-09-29-12)
- 2026-09-29 · 생성 · [62. 제조 공장 — 대표 연구와 자료](../../topics/2026/2026-09-29-area62-s8.md) — 자동 분리: 62. 제조 공장 의 "8. 대표 연구와 자료" 절을 옮겼다; 2차 수정(1회차): 첫 항목(1절·3절)의 '라인 공급 작업 단위 기준' 문장을 [추정] 별도 문장으로 분리(2회차 변경 없음) (실행 2026-09-29-12)
- 2026-09-29 · 생성 · [62. 제조 공장 — 열린 질문](../../topics/2026/2026-09-29-area62-s11.md) — 자동 분리: 62. 제조 공장 의 "11. 열린 질문" 절을 옮겼다; 2차 수정(1회차): KETI 첫 등장을 '한국전자기술연구원(KETI)'로 병기(2회차 변경 없음) (실행 2026-09-29-12)
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 936건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 249개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
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

### docs/open-questions.md (요약: 대상 영역 [63] 에 걸린 4건 / 전체 170건)

```markdown
- oq-134 [열림] 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? (영역 11, 61, 63)
- oq-138 [열림] 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? (영역 9, 61, 63)
- oq-142 [열림] 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? (영역 12, 61, 63, 62)
- oq-149 [열림] 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? (영역 4, 63, 58)
```

### docs/standards/index.md (요약: 227개 — 이름 · 종류 · 발행 기관)

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
```

### runs/2026-09-29-13/docs_tree.txt

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
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/plug-and-produce.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/prompt-injection.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-task-fitness-matrix.md
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
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-938.md
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
