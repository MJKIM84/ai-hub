(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
        "ref-872"
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
        "ref-872",
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
        "ref-872",
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
        "ref-872",
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
      "id": "ref-872",
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
    "ref-872(RoMi-H Empanelment Programme 2025): 각주와 reference_updates 의 발행일을 '미확인'이 아니라 2025-05-01 로 적는다 — 페이지에 게시일 2025-05-01(갱신 2026-08-24)이 표시돼 있다. f6 의 기준일도 2025-05-01 로 쓴다.",
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
  "verification_note": "판정: 조건부 승인. 확인 23건, 미확인 2건(f10 병원 목록 일부 불일치, f19 근거 없는 '마약류·수술실'), 교차 확인 4건(f7 분당서울대 AMR 6대·품목, f8 한림대성심 7종 73대·27,300건, f11 울산대병원 항암제 이송로봇 케로, f12 서비스로봇 실증사업 2020년 시작). 강등: 없음(f4·f12 의 finding 신뢰도 high 는 medium 으로 낮춤). 원문 미열람 출처: ref-911(검색 결과 일치). 주의: 핵심 성과 수치(f1 배송 시간 32~36%·7.3배, f3 성공률 87.03%·95.52%)는 각각 단일 병원·단일 연구의 결과로 독립 출처 교차 확인이 없으며, f4 의 두 출처는 같은 프로젝트 참여 기관이라 독립적이지 않다. ref-872 는 페이지에 발행일 2025-05-01 이 표시돼 브리프의 '미확인'이 오류다. ref-004 는 입력 원문 텍스트로 열람했으나 브리프 summary 가 '원문 미열람.'으로 시작해 표기가 어긋난다(퍼블리셔 확인 필요). 미사용 출처 없음. 정정 요청 없음. oq-149 는 부분 답(f24)이며 해결 인정하지 않음, oq-134·oq-138·oq-142 미해결 유지. 검증 검색 8회(리서치 14회와 합쳐 22/30). 열린 질문 단서: KSSN 표준 검색 결과에 'KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'이 나타나나 원문 미열람이라 페이지에 넣지 않았다. 페이지 신뢰도 medium.",
  "retry_reason": null
}
```

### runs/2026-09-29-13/pages.json

```json
{
  "run_id": "2026-09-29-13",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "병원 이송은 감염 관리·환자 정보 보호·승강기 공유 조건 아래 놓여 로봇 개별 성능보다 승강기·수령 인증·병원 정보 시스템을 잇는 운영 계층이 성과를 가른다. [추정][^ref-946][^ref-939] 효과 근거는 단일 병원 연구 중심이며 동료 심사 근거가 부족하다. [사실][^ref-939][^ref-949]",
      "planned_findings": [
        "f1",
        "f10",
        "f11",
        "f12",
        "f15",
        "f21"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1100,
      "summary": "RoMi-H, Open-RMF 어댑터, 승강기 가동률, 등재 프로그램, 스마트병원 선도모델, 서비스로봇 실증사업, 수령 인증, 감염환자 이송 로봇, 기술 성숙도를 정의한다. [사실][^ref-940][^ref-946][^ref-872][^ref-953]",
      "planned_findings": [
        "f2",
        "f3",
        "f4",
        "f6",
        "f12",
        "f13",
        "f15",
        "f16",
        "f18"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3000,
      "summary": "현장 유형 병원의 국내(분당서울대·한림대성심·고대구로·울산대)·해외(산시성 인민병원·창이종합병원) 사례를 여섯 항목 표로 정리한다. [사실][^ref-941][^ref-947][^ref-946][^ref-951][^ref-939][^ref-940]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "승강기·자동문 연동, 이기종 미들웨어·통합관제, 수령 인증·비접촉 배송, 야간 동선 분리, 승강기 혼잡 사전 분석, 정착 과정을 다룬다. [사실][^ref-946][^ref-945][^ref-939][^ref-941][^ref-942]",
      "planned_findings": [
        "f2",
        "f3",
        "f5",
        "f7",
        "f8",
        "f9",
        "f13",
        "f14",
        "f18"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 700,
      "summary": "ISO 13482, 로봇 승강기 탑승 KS(번호 미확인), Open-RMF, RoMi-H, 등재 프로그램, 서비스로봇 실증사업, 스마트병원 선도모델을 표로 둔다. [사실][^ref-946][^ref-948][^ref-940][^ref-872][^ref-950][^ref-953]",
      "planned_findings": [
        "f3",
        "f4",
        "f6",
        "f12",
        "f13",
        "f14",
        "f18"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "간호 협동로봇 체계적 검토, 산시성 효과 분석, 고대구로 승강기 타당성, 국내 감염환자 이송 인식 연구, AMR 문헌 검토를 요약하고 교차 확인 한계를 남긴다. [사실][^ref-949][^ref-939][^ref-946][^ref-952][^ref-911]",
      "planned_findings": [
        "f1",
        "f3",
        "f12",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP 는 이송 요청 수신·이기종 배정·승강기 예약·수령 인증 확인·결과 반환·재계획을 맡고, 처방 판단·승강기 제어·안전 기능·감염 관리 기준은 연계 대상이다. [추정][^ref-939][^ref-946][^ref-953][^ref-948]",
      "planned_findings": [
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 900,
      "summary": "3·17·19·20·21·22·28·32·39·49·50·51·53·55·56·58 열여섯 영역과 연결 이유를 적는다. [추정][^ref-946][^ref-945][^ref-939]",
      "planned_findings": [
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "section": "11. 열린 질문",
      "budget_chars": 900,
      "summary": "oq-149 부분 답·oq-134·oq-138·oq-142 미해결 결과와 새 질문 5건을 둔다. [추정][^ref-872][^ref-946][^ref-947]",
      "planned_findings": [
        "f24",
        "f25"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/hospital-and-healthcare.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft), 프런트매터 related_areas·tags·confidence·sources·last_run 채움, 13절 각주 17건, 1차 수정 지시 18건 이행; 2차 수정(1회차): 8절 첫 항목의 태그·각주를 결론 문장 뒤로 옮기고 해석 문장을 [추정]으로 분리, 3절 '운영 계층은 … 받아야 한다'를 [추정] 문장으로 분리, 5절 울산대병원 제약 칸에 '기사가 전한 국내 병원 일반의 장애 요인:' 귀속 표시, 용어집 RoMi-H 출처에 ref-872 추가·승강기 가동률 정의 한정(분리 전 전체 본문으로 반환, 분리는 코드가 다시 한다)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"11. 열린 질문\" 절(1,575자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"4. 핵심 개념과 용어\" 절(1,525자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"6. 대표 접근법과 기술\" 절(1,495자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"8. 대표 연구와 자료\" 절(1,439자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,068자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"3. 왜 중요한가\" 절(858자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area63-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 63. 병원·의료 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(805자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 63. 병원·의료 | 섹션 3~11 신규 작성(seed → draft), 병원 사례 6건 여섯 항목 정리, 각주 17건, 1차 수정 지시 18건 이행; 2차 수정(1회차): 8절 태그·각주 정리, 3절 추론 문장 [추정] 분리, 5절 울산대병원 제약 칸 귀속 표시, 용어집 RoMi-H 출처·승강기 가동률 정의 수정 | run 2026-09-29-13",
  "index_updates": {
    "home_recent": "2026-09-29 — 63. 병원·의료: 섹션 3~11 신규 작성(seed → draft). 국내(분당서울대·한림대성심·고대구로·울산대)·해외(산시성 인민병원·싱가포르 RoMi-H) 병원 이송 사례를 여섯 항목으로 정리하고 승강기 연동·수령 인증·감염 관리·정부 지원 제도를 다뤘다",
    "category_recent": "2026-09-29 — 63. 병원·의료: 섹션 3~11 신규 작성(seed → draft), 병원 사례 6건·각주 17건, 1차 수정 지시 18건 이행; 2차 수정(1회차): 8절 태그·각주 정리, 3절 추론 문장 [추정] 분리, 5절 울산대병원 제약 칸 귀속 표시, 용어집 정의·출처 수정 (실행 2026-09-29-13)",
    "area_recent": "2026-09-29 — 63. 병원·의료: 섹션 3~11 신규 작성. 승강기 가동률·RoMi-H·등재 프로그램·스마트병원 선도모델 용어와 병원 사례 6건을 추가했고 oq-149 는 부분 답, oq-134·oq-138·oq-142 는 미해결로 남았다; 2차 수정(1회차)으로 태그·귀속 표시를 정리했다 (실행 2026-09-29-13)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "robotic-middleware-for-healthcare",
      "term_ko": "의료 로봇 미들웨어 RoMi-H",
      "term_en": "Robotic Middleware for Healthcare (RoMi-H)",
      "definition": "싱가포르 창이종합병원 CHART 가 Open-RMF(ROS 2·DDS) 위에 만든 오픈소스 미들웨어로, 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 기계·제어·중앙·통합 네 도메인으로 잇고 승강기 같은 공용 자산을 공유하게 하며 싱가포르 보건부가 공공 의료기관의 자동화 통합 플랫폼으로 인정한다.",
      "description": "2018-07 보건부 장관 발표 뒤 2019-10-31 ROSCon 에서 공개됐다. 협력 기관(IHiS·GovTech·Hope Technik·Open Robotics)과 RMF 기반은 Open Robotics 블로그가 전하며, CHART 페이지와 같은 프로젝트 참여 기관의 자료라 독립 교차 확인으로 세지 않는다. 보건부의 공공 의료기관 통합 플랫폼 인정은 CHART 등재 프로그램 안내(ref-872)에 근거한다.",
      "related_areas": [
        63,
        20,
        21,
        22
      ],
      "sources": [
        "ref-940",
        "ref-945",
        "ref-872"
      ]
    },
    {
      "action": "new",
      "slug": "elevator-operating-rate",
      "term_ko": "승강기 가동률",
      "term_en": "Elevator Operating Rate (EOR)",
      "definition": "고대구로병원 연구가 쓴 지표로, 가동률이 높을수록 배송 로봇의 임무 실패가 늘어난다는 관계를 보여 로봇 배차·재계획의 제약 변수로 쓸 수 있다.",
      "description": "단일 기관·단일 로봇·2025-06-18~29 조건의 배송 122건에서 EOR 59% 미만 성공률 95.52%, 실패는 EOR 90% 초과 구간에 집중됐다. 계산 방식은 원문 확인 범위 밖이라 적지 않는다.",
      "related_areas": [
        63,
        22,
        28,
        32
      ],
      "sources": [
        "ref-946"
      ]
    },
    {
      "action": "new",
      "slug": "empanelment-programme",
      "term_ko": "등재 프로그램",
      "term_en": "Empanelment Programme",
      "definition": "공공 기관이 벤더·시스템 통합사의 기술 전문성과 배치 역량을 사전에 평가해 일정 기간 유효한 자격을 주고 조달 제안 요청(RFP·RFI)에 참여할 수 있는 목록에 올리는 제도로, 싱가포르 CHART 가 RoMi-H 배치 통합사를 대상으로 정기적으로(원문 표기 bi-annual) 운영한다.",
      "description": "2025 프로그램은 2025-05-01 부터 2년 유효한 인증을 주며 등재 통합사는 HOPE Technik·Medisys Innovation·Panasonic Asia Pacific·QuikBot Technologies·Techfox 5개사다.",
      "related_areas": [
        63,
        58,
        21
      ],
      "sources": [
        "ref-872"
      ]
    },
    {
      "action": "new",
      "slug": "smart-hospital-leading-model",
      "term_ko": "스마트병원 선도모델",
      "term_en": "Smart Hospital Leading Model",
      "definition": "한국보건산업진흥원이 2020년부터 정보통신기술로 환자 안전과 의료 질을 높이는 병원 모델을 개발·검증하도록 지원한 사업의 산출물로, 개별 선도모델 58개가 지능형 원내 물류 배송(자율주행 로봇+생체인증 무인 배송)·하나로 감염관리 등 9개 모듈로 재구성됐다.",
      "related_areas": [
        63,
        3,
        17,
        51
      ],
      "sources": [
        "ref-953",
        "ref-951"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-939",
      "org": "Li, M. 외 (Scientific Reports)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04-24",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "중국 산시성 인민병원에서 AMR 10대로 약품·검체 이송을 6개월 운영한 효과 분석. 배송 시간 32~36% 단축, 승강기 IoT 제어·RFID 신원 확인·협력 책임 체계·경제성 분석(단일 연구, 교차 확인 없음).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "원내 약 배송로봇을 시범·정식 도입한 국내 병원(양산부산대·용인세브란스·한림대성심·조선대·삼성서울 등)과 환자 안내용 로봇 운영 병원, 과기정통부 XaaS 선도 프로젝트(56억 원), LG전자·빅웨이브로보틱스 공급, 구축 병원의 자동문·통로·승강기 턱 제약을 정리한 기사.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "RoMi-H 배치 시스템 통합사를 기술·배치 역량으로 평가해 2년 유효 인증을 주고 공공 의료기관 RFP·RFI 참여 목록으로 게시하는 등재 프로그램 안내(2025-05-01 효력, 갱신 2026-08-24, 등재 통합사 5개, 정기 운영(원문 표기 bi-annual)).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "고대구로병원에서 ISO 13482 인증 시험을 거친 IROI 로봇 1대의 약국→응급실 배송 122건을 분석해 승강기 가동률과 성공률(전체 87.03%)의 관계를 밝힌 타당성 연구(단일 기관·2025-06-18~29). 승강기 연동은 TK50M 전용 통신 모듈.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "한림대성심병원의 7종 73대 서비스 로봇(배송·안내·물류·홈케어·방역, 2024-04 기준), 제조사가 다른 로봇의 통합관제 시스템·커맨드센터, 2023년 로봇 배송 27,300건을 전한 탐방 기사.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "국가기술표준원이 로봇의 승강기 탑승 안전 요구사항과 실내 배송 로봇 KS 를 제정한다고 알린 보도자료. 속도 제어·보호 정지·높낮이차·틈새·추락 방지 요구, 행정안전부 협력. 표준 번호·정식 명칭 없음.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "2018년 이후 간호 협동로봇 연구 28편의 체계적 검토. 28편 중 14편이 TRL 4~5(TRL 9 는 1편), 미국 병원의 TUG 등 배송 로봇에 대한 동료 심사 근거 부족, 비용·유지보수·사이버보안 분석 미흡을 지적.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "국내 병원 로봇 도입 현황(한림대의료원·울산대병원·서울대병원), 서비스로봇 실증사업·스마트병원 사업(선도모델 58개), 의료진 평가와 억 단위 비용·경사 구간·문 호환·건물마다 다른 승강기 같은 국내 병원 일반의 건축 구조 장애 요인을 정리한 기사.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "감염환자 이송 로봇의 서비스 품질에 대한 의료종사자 인식을 SERVQUAL 다섯 차원과 AHP 로 조사해 안전 최우선, 기기 오류 해결·응급처치·환자 모니터링·감염 인자 억제의 중요성을 확인한 국내 논문(KCI 초록 확인, 본문 PDF 미열람, 설문 응답 수 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "summary": "RMF Core 개요. 작업·교통 조율, Fleet Adapter, 문·승강기 설비 연동 구조 참고(이번 실행은 입력 원문 텍스트 data/source_texts/ref-004.txt 로 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
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
      "cited_by": [
        "docs/categories/site-type-applications/hospital-and-healthcare.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)?",
      "areas": [
        63,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가?",
      "areas": [
        63,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가?",
      "areas": [
        63,
        22,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "한림대성심병원처럼 제조사가 다른 여러 로봇을 통합관제하는 국내 병원은 어떤 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API)으로 로봇과 승강기를 연결하며 그 구조가 공개돼 있는가?",
      "areas": [
        63,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 병원에서 식사(환자식) 이송을 로봇이 맡은 운영 사례가 있으며, 식사 이송은 약품·검체 이송과 시작 조건·시간 제약·인계 방식이 어떻게 다른가?",
      "areas": [
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시",
      "title": "63. 병원·의료"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 13482 (서비스 로봇 안전 요구사항)",
      "kind": "표준",
      "org": "ISO",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "related_areas": [
        63,
        50,
        49
      ],
      "summary": "고대구로병원 약품 배송 연구의 로봇이 ISO 13482 적합 인증 시험을 거쳤다. 표준 원문은 열지 않았고 근거는 논문(ref-946)이며 URL 도 그 논문이다.",
      "ref_id": "ref-946"
    },
    {
      "name": "RoMi-H (Robotic Middleware for Healthcare)",
      "kind": "오픈소스",
      "org": "Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology)",
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "related_areas": [
        63,
        20,
        21,
        22
      ],
      "summary": "Open-RMF(ROS 2·DDS) 기반 오픈소스 의료 로봇 미들웨어로, 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 네 도메인으로 잇고 싱가포르 보건부가 공공 의료기관의 자동화 통합 플랫폼으로 인정했다.",
      "ref_id": "ref-940"
    },
    {
      "name": "서비스로봇 실증사업",
      "kind": "평가 프로그램",
      "org": "한국로봇산업진흥원",
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "related_areas": [
        63,
        3
      ],
      "summary": "2020년부터 물류·웨어러블·의료·기타 네 분야의 로봇 도입 비용 50% 이내를 국비로 지원하며 서류·발표·현장평가로 과제를 선정한다.",
      "ref_id": "ref-950"
    },
    {
      "name": "스마트병원 선도모델(9개 모듈)",
      "kind": "프레임워크",
      "org": "한국보건산업진흥원 스마트병원 확산지원센터",
      "url": "https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040",
      "related_areas": [
        63,
        17,
        51
      ],
      "summary": "개별 선도모델 58개를 9개 모듈로 재구성한 틀로, '지능형 원내 물류 배송'(자율주행 로봇+생체인증 무인 배송)과 '하나로 감염관리' 모듈이 병원 로봇 이송·감염관리 자동화를 정의한다.",
      "ref_id": "ref-953"
    }
  ],
  "additional_research_requests": [
    "5. 적용 사례 절의 완료·인계 항목에 필요한 사실: 분당서울대병원·고대구로병원·울산대병원 사례에서 무엇이 확인돼야 이송이 끝난 것으로 인정하는지(수령 확인 방식) — 이번 브리프에 없어 '미확인'으로 두었다.",
    "5. 적용 사례 절의 식사(환자식) 이송 사례: 국내 병원에서 로봇이 식사 이송을 맡은 운영 사례와 약품·검체 이송과의 시작 조건·시간 제약·인계 방식 차이 — 이번 조사에서 근거를 확인하지 못했다.",
    "9. 책임 경계 절의 업종별 조건에 필요한 사실: 개인정보 보호법 제25조의2(이동형 영상정보처리기기)의 원문과 병원 이송 로봇 적용 해석 — 법령 원문 열람 실패로 법령 조문 내용을 쓰지 못했다.",
    "7. 관련 표준 절에 필요한 사실: 국가기술표준원이 2021-11-11 제정을 발표한 로봇 승강기 탑승 안전 요구사항 KS·실내 배송 로봇 KS 의 표준 번호·정식 명칭·조항(검증 노트의 단서: KS B 7317, 원문 미열람) — 이번 자료에 번호가 없어 '미확인'으로 두었다.",
    "6. 대표 접근법 절에 필요한 사실: 한림대성심병원 통합관제 시스템이 로봇·승강기를 잇는 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API) — 통합관제 언급 수준만 확인됐다.",
    "6. 대표 접근법 절의 감염 관리 구역 처리에 필요한 사실: 격리 병동·감염 관리 구역의 로봇 출입 규칙과 표면 소독 절차를 플릿 관제가 제약으로 받는 공개 지침·연구(AJIC 2023·JHI 2025 논문은 열람 실패로 제외됐다).",
    "5. 적용 사례 절 울산대학교병원 사례에 필요한 사실: 비즈한국 기사의 장애 요인(속도·안전성·비용·건축 구조)이 울산대병원에도 해당하는지 병원별 근거 — 이번 브리프는 국내 병원 일반의 장애 요인으로만 전해 귀속 표시를 붙였다.",
    "5·6절 보강 후보(출처 상한으로 미룸): 메디칼타임즈(2026-02-03)의 삼성서울병원 야간 승강기 혼잡 회피 운영 기사, 머니투데이(2026-04-14)의 서울대병원·하버드의대 임상 환경 시뮬레이터 기사, Panasonic HOSPI ISO 13482 인증 페이지(403), Aethon TUG 벤더 자료.",
    "7. 관련 표준 절·standards_updates 의 ISO 13482 항목: 표준 발행 기관(ISO)의 공식 페이지 URL 과 현재 판 확인 — 이번 근거는 논문(ref-946)뿐이라 URL 도 논문으로 두었다."
  ],
  "fixes_applied": [
    "ref-872 발행일 — 13절 각주와 reference_updates 의 발행일을 2025-05-01 로 적었고, 4절 등재 프로그램 정의·7절 표·11절 oq-149 답에 기준일 2025-05-01 을 썼다.",
    "f6·용어 '등재 프로그램'의 '격년' — 4절 정의와 glossary_updates 정의를 '정기적으로(원문 표기 bi-annual) 운영'으로 바꿨다.",
    "f10 도입 병원 목록 — 5절 국내 사례 머리 문장을 '원내 약 배송로봇을 시범 운영하거나 정식 도입한 곳은 양산부산대병원·용인세브란스병원·한림대성심병원·조선대병원·삼성서울병원 등이고, 해운대백병원·의정부을지대병원·일산차병원은 환자 안내용 로봇을 운영'으로 고치고 [사실][^ref-943] 을 붙였다.",
    "f11 표현 — 5절 울산대병원 사례 제약 칸과 10절 3. 경제성·조달·사업 모델 연결에 '대당 억 단위 비용', '경사 구간·문 호환·건물마다 다른 회사의 승강기'로 썼다.",
    "f15 TRL 집계 — 4절 기술 성숙도 항목과 8절 첫 항목을 '28편 중 14편이 TRL 4~5 수준(TRL 9 는 1편)'으로 썼다.",
    "f16 응답 수 — 본문 어디에도 30·24·23부를 쓰지 않고 8절에 '설문 응답 수는 미확인'과 'KCI 초록만 확인, 본문 PDF 미열람'을 적었으며 13절 각주 접근일 뒤에 '(KCI 초록 확인, 본문 PDF 미열람)'을 붙였고 reference_updates summary 에도 같은 취지를 남겼다.",
    "f19·f20 작업 대상 — 5절 머리 문장과 여섯 항목 종합에서 '마약류'와 '수술실'을 빼고 검체 이송 출발지를 '병동·내시경실'로 썼다.",
    "f2 인력 표현 — 4절 수령 인증 설명, 5절 산시성 사례 수행 자원 칸, 6절 수령 인증 소절, 10절 58. 다사업자 책임·계약·데이터 연결에서 모두 '장비 관리자'로 썼다.",
    "f3 한정 — 5절 고대구로병원 사례 수행 자원 칸을 '논문이 분석한 로봇 1대(도구공간 IROI)'로, 예외·성과 칸을 '단일 기관·2025-06-18~29 조건의 배송 122건에서 전체 성공률 87.03%, EOR 59% 미만에서 95.52%'로 같은 문장에 병기했고 6절·8절에도 같은 조건을 붙였다.",
    "f1·f2 조건 병기 — 3절과 5절 산시성 사례 예외·성과 칸에서 32~36%·7.3배·이용률 0.84 와 같은 문장에 '단일 연구(2025-06-01~11-30)'를 병기하고 [사실] 을 유지했으며, 3절·8절에 독립 출처로 교차 확인되지 않았음을 적었다.",
    "f4 출처 독립성 — 4절 RoMi-H 항목을 CHART 페이지 근거 문장([^ref-940])과 협력 기관·RMF 기반 문장([^ref-945])으로 나누고 '두 출처는 같은 프로젝트의 참여 기관이라 독립 교차 확인으로 세지 않는다'를 적었으며 어디에도 교차 확인으로 서술하지 않았다.",
    "f12 신뢰도 — 8절 기관 자료 항목에 '국비 50%·절차 같은 세부 조건은 진흥원 단독 자료이며 기사는 사업 존재와 시작 연도만 확인한다'를 적어 medium 근거임을 남겼다(페이지 신뢰도는 verification.json 의 medium).",
    "f8 로봇 종류·기준일 — 5절 한림대성심병원 사례 수행 자원 칸을 '2024-04 기준 7종 73대(배송·안내·물류·홈케어·방역)'로 쓰고 '비대면 협진'을 뺐으며 예외·성과 칸의 27,300건에도 '2024-04 기준'을 유지했다.",
    "용어 '스마트병원 선도모델' — glossary_updates 정의와 4절 항목에서 '보건복지부'를 빼고 한국보건산업진흥원만 썼다.",
    "용어 '승강기 가동률' — glossary_updates 정의와 4절 항목을 '고대구로병원 연구가 쓴 지표로, 가동률이 높을수록 배송 실패가 늘었다'는 관계 서술로 한정하고 계산 방식(사용 중인 시간 비율)은 쓰지 않았다.",
    "5. 적용 사례 절 — 사례 6건 모두 '현장 유형: 병원'을 명시하고 '국내 사례'(분당서울대·한림대성심·고대구로·울산대)와 '해외 사례'(산시성 인민병원·창이종합병원)로 나눠 여섯 항목 표로 놓았으며 site_matrix_updates 의 site_type 은 모두 '병원'이다.",
    "f17(ref-911) — 13절 각주 접근일 뒤에 ' (원문 미열람)' 을 붙이고 reference_updates 의 ref-911 항목에 source_unopened: true 를 두었으며 8절 항목에도 '(원문 미열람)'을 적었다.",
    "11. 열린 질문 절 — oq-149 는 열림·부분 답으로, oq-134·oq-138·oq-142 는 열림·미해결로 f24·f25 의 결과를 적고 해결로 바꾸지 않았으며(open_question_updates 에 update 없음), open_questions_new 5건을 규약대로 question·areas 로 옮겨 new 로 등록하고 11절에도 '(신규, id 는 퍼블리셔가 부여)'로 두었다.",
    "2차: 8절 첫 항목(Babalola 외 체계적 검토) — '…분석이 부족하다고 결론짓는다.' 바로 뒤에 [사실][^ref-949] 를 붙이고, 이어지는 '이 영역에서는 운영 성과를 근거로 만드는 일의 출발점이다.' 는 [추정][^ref-949] 로 바꿨다. 분리 전 전체 본문으로 반환하므로 코드가 다시 분리할 때 세부영역 페이지에 남는 요약 문장에도 태그·각주가 따라간다.",
    "2차: 3절 세 번째 단락 — '자동출입문 장치 필요·통로 협소·승강기 턱 때문에 도입을 포기한 병원이 있어 기존 건물보다 신축 병원 위주로 도입된다. [사실][^ref-943]' 와 '그러므로 운영 계층은 건물·설비 조건을 처음부터 제약으로 받아야 한다. [추정][^ref-943]' 두 문장으로 나눴다.",
    "2차: 5절 울산대학교병원 표 제약 칸 — '기사가 전한 국내 병원 일반의 장애 요인: 속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기 같은 건축 구조 [사실][^ref-951]' 로 귀속 표시를 앞에 붙였다.",
    "2차: glossary_updates '의료 로봇 미들웨어 RoMi-H' — sources 에 ref-872 를 더하고 description 에 보건부 인정 문구의 근거가 ref-872 임을 적었다.",
    "2차: glossary_updates '승강기 가동률' — 정의에서 '승강기 대기가 길어지고' 를 빼고 '가동률이 높을수록 배송 로봇의 임무 실패가 늘어난다는 관계' 로 한정했다(4절 본문과 같은 범위).",
    "분량 초과 자동 분리: 63. 병원·의료 본문 13,033자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,833자"
  ]
}
```

### runs/2026-09-29-13/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/site-type-applications/hospital-and-healthcare.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area63-s11.md (1,575자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area63-s4.md (1,525자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area63-s6.md (1,495자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area63-s8.md (1,439자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area63-s10.md (1,068자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area63-s3.md (858자)
    - docs/categories/site-type-applications/hospital-and-healthcare.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area63-s7.md (805자)
```

### runs/2026-09-29-13/pages/categories/site-type-applications/hospital-and-healthcare.md

```markdown
---
title: "63. 병원·의료"
type: area
category: "Q. 현장 유형별 적용"
area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [병원 이송 로봇, 승강기 연동, 감염 관리, 수령 인증, RoMi-H, 스마트병원]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-004, ref-911, ref-939, ref-940, ref-941, ref-942, ref-943, ref-872, ref-945, ref-946, ref-947, ref-948, ref-949, ref-950, ref-951, ref-952, ref-953]
last_run: 2026-09-29
version: 2
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

병원은 약품·검체·린넨을 옮기는 일이 감염 관리와 환자 정보 보호라는 조건 아래 놓이고 승강기와 복도를 환자·침대·직원과 함께 쓰는 현장이어서, 로봇 한 대의 주행 성능보다 승강기·자동문·수령 인증·병원 정보 시스템을 하나로 잇는 운영 계층이 이송 성과를 가른다. [추정][^ref-946][^ref-939]

자세한 내용은 주제 페이지 [63. 병원·의료 — 왜 중요한가](../../topics/2026/2026-09-29-area63-s3.md)에 있다.

## 4. 핵심 개념과 용어

**의료 로봇 미들웨어 RoMi-H(Robotic Middleware for Healthcare)** — 싱가포르 창이종합병원 CHART(Centre for Healthcare Assistive & Robotics Technology)가 만든 ROS 2·DDS(Data Distribution Service) 기반 오픈소스 미들웨어로, 2018-07 보건부 장관 발표 뒤 2019-10-31 ROSCon 에서 공개됐고 기계·제어·중앙·통합의 네 도메인으로 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 잇는 것을 목적으로 한다. [사실][^ref-940]

자세한 내용은 주제 페이지 [63. 병원·의료 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area63-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

확인한 자료를 종합하면 병원의 로봇 작업은 (1) 약품 이송 — 야간 약제·항암제를 약국에서 병동·응급실로, (2) 검체 이송 — 병동·내시경실에서 검사실로, 포름알데히드 용액에 담긴 조직 포함, (3) 린넨·진료재료·물품 카트 이송, (4) 감염환자 이송 — 사람을 작업 대상으로 하는 이송, (5) 방역·환경 소독과 출입 통제의 다섯 형태로 나타나며, 식사 이송 사례는 이번 조사에서 근거를 확인하지 못했다. [추정][^ref-939][^ref-946][^ref-943][^ref-951][^ref-942][^ref-941][^ref-947][^ref-952][^ref-953] 아래 사례는 모두 현장 유형 병원이며, 국내와 해외로 나눠 여섯 항목에 놓는다.

### 국내 사례

원내 약 배송로봇을 시범 운영하거나 정식 도입한 곳은 양산부산대병원·용인세브란스병원·한림대성심병원·조선대병원·삼성서울병원 등이고, 해운대백병원·의정부을지대병원·일산차병원은 환자 안내용 로봇을 운영하며, 과학기술정보통신부 'XaaS 선도 프로젝트'(총 56억 원) 5개 과제 중 1개를 빅웨이브로보틱스가 맡았다. [사실][^ref-943]

**현장 유형:** 병원

**사례:** 분당서울대병원에서 본관과 헬스케어혁신파크 사이 진료재료·약품·린넨 카트를 야간에 이송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 물품을 카트에 채워 놓으면 로봇이 옮기며, 야간 시간대에 배송한다. [사실][^ref-941] |
| 작업 대상 | 진료재료·약품·린넨(환자복·침대 시트·이불) 카트 [사실][^ref-941] |
| 수행 자원 | KT [5G 특화망](../../glossary/private-5g-network.md) 위의 AMR 6대, 다중 연동된 승강기·자동문 [사실][^ref-941] |
| 제약 | 본관에서 헬스케어혁신파크까지 약 300m 연결 터널(워킹갤러리), 야간 배송으로 환자 동선과 분리 [사실][^ref-941] |
| 완료·인계 | 미확인 |
| 예외·성과 | 기존 1.5km 차량 운송을 대체했다. [사실][^ref-941] |

이 사례는 승강기·자동문 연동과 야간 시간대라는 시간 제약이 이송 계층의 조건이 되는 형태를 보여 준다. [추정][^ref-941]

**현장 유형:** 병원

**사례:** 한림대성심병원에서 제조사가 다른 여러 로봇으로 약제·검체·물품을 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 약제, 검체(포름알데히드 용액에 담긴 조직), 물품 [사실][^ref-942][^ref-947] |
| 수행 자원 | 2024-04 기준 7종 73대의 서비스 로봇(배송·안내·물류·홈케어·방역)을 통합관제 시스템으로 커맨드센터에서 중앙 관리하며, LG전자와 빅웨이브로보틱스가 각각 배송로봇을 공급한다. [사실][^ref-947][^ref-943] |
| 제약 | 약제 배송로봇은 혼자 승강기를 타고, 실외 배송로봇은 신호등을 인식해 본관과 별관 사이 횡단보도를 건넌다. [사실][^ref-942] |
| 완료·인계 | 병동 간호사 스테이션의 지정 장소에서 대기한다. [사실][^ref-942] |
| 예외·성과 | 2023년 27,300건(월평균 2,250건)의 로봇 배송을 처리했고(2024-04 기준), 시스템 정착에 약 3년이 걸렸으며 사용자 공감대 형성과 보급형 로봇의 한계에 맞춘 병원 시스템 변경이 과제였다. [사실][^ref-947][^ref-942] |

제조사가 다른 로봇의 공존이 확인된 국내 사례이지만, 통합관제가 어떤 인터페이스·표준으로 로봇과 승강기를 잇는지는 확인되지 않았다. [추정][^ref-947][^ref-943]

**현장 유형:** 병원

**사례:** 고대구로병원에서 약국에서 응급실로 비긴급 약품을 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 약국에서 응급실로 가는 비긴급 약품 배송 요청 [사실][^ref-946] |
| 작업 대상 | 비긴급 약품 [사실][^ref-946] |
| 수행 자원 | 논문이 분석한 로봇 1대(도구공간 IROI, ISO 13482 적합 인증 시험을 거침), TK엘리베이터 TK50M 제어반에 부착한 전용 통신 모듈로 승강기 호출·탑승 자동화 [사실][^ref-946] |
| 제약 | 사람·침대와 함께 쓰는 승강기의 가동률(EOR) [사실][^ref-946] |
| 완료·인계 | 미확인 |
| 예외·성과 | 단일 기관·2025-06-18~29 조건의 배송 122건에서 전체 성공률 87.03%, EOR 59% 미만에서 95.52%였고 실패는 EOR 90% 초과 구간에 집중됐다. [사실][^ref-946] |

승강기 혼잡이 병원 특유의 핵심 제약임을 운영 기록으로 보인 사례다. [추정][^ref-946]

**현장 유형:** 병원

**사례:** 울산대학교병원에서 항암제를 이송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 항암제 [사실][^ref-951] |
| 수행 자원 | 2022년 도입한 항암제 이송 로봇 [사실][^ref-951] |
| 제약 | 기사가 전한 국내 병원 일반의 장애 요인: 속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기 같은 건축 구조 [사실][^ref-951] |
| 완료·인계 | 미확인 |
| 예외·성과 | 의료진은 약사의 대면 업무와 간호사의 약제실 왕복이 줄었다고 평가했다. [사실][^ref-951] |

### 해외 사례

**현장 유형:** 병원

**사례:** 중국 산시성 인민병원에서 약국에서 병동으로 약품을, 병동에서 검사실로 검체를 이송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 약국·병동의 정기·수시 이송 요청, 최대 수요 시간당 42건 [사실][^ref-939] |
| 작업 대상 | 약품(약국→병동), 검체(병동→검사실) [사실][^ref-939] |
| 수행 자원 | 적재 200kg·배터리 7시간의 AMR 10대, 약국·병동·시스템 관리자·장비 관리자의 역할을 정한 협력 책임 체계 [사실][^ref-939] |
| 제약 | 500병상·22개 개방 병동, 층간 이동은 사물인터넷 기반 승강기 제어, 비접촉 배송 [사실][^ref-939] |
| 완료·인계 | 픽업·배송 지점의 RFID 신원 확인 [사실][^ref-939] |
| 예외·성과 | 단일 연구(2025-06-01~11-30) 조건에서 배송 시간 32~36% 단축, 수작업 인력 19명 대비 7.3배 건수, 검증 정확도·물품 온전율 100%, 최대 수요에서 로봇 10대의 이용률 0.84 [사실][^ref-939] |

이 사례는 여섯 항목이 모두 한 연구에서 확인되는 드문 경우이며, 수치는 단일 병원·단일 연구 조건에 한정된다. [추정][^ref-939]

**현장 유형:** 병원

**사례:** 싱가포르 공공 병원에서 여러 제조사의 로봇이 RoMi-H 로 승강기를 공유하며 이송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 여러 제조사의 로봇·센서·병원 정보 시스템을 RoMi-H 로 연결하며, 배치는 등재된 시스템 통합사(HOPE Technik·Medisys Innovation·Panasonic Asia Pacific·QuikBot Technologies·Techfox)가 맡는다. [사실][^ref-940][^ref-872] |
| 제약 | 승강기 같은 물리 자산을 공유하고, 경로 계획 시각화와 다른 로봇에 대한 출입 금지 구역으로 충돌을 피한다. [사실][^ref-945] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

확인한 자료를 종합하면 병원 로봇 작업의 여섯 항목은 시작 조건이 약국·병동의 정기·수시 이송 요청과 야간 시간대 배송, 작업 대상이 약품·검체·린넨·진료재료와 감염환자, 수행 자원이 AMR 과 약국·병동·시스템 관리자·장비 관리자·커맨드센터, 제약이 승강기 혼잡·자동문·통로·턱과 감염 관리 구역·비접촉·생체인증 권한·ISO 13482·KS 승강기 탑승 안전 요구, 완료·인계가 RFID 신원 확인·생체인증, 예외·성과가 승강기 혼잡 시 실패·기기 오류·응급처치 우려와 배송 시간·건수 지표로 채워질 수 있다. [추정][^ref-939][^ref-941][^ref-947][^ref-946][^ref-943][^ref-953][^ref-948][^ref-952] 다룬 칸은 [현장 유형 매트릭스](../../site-matrix.md)에 반영된다.

## 6. 대표 접근법과 기술

승강기는 병원에서 로봇이 사람·침대와 함께 쓰는 공용 자원이므로, 층간 이송은 승강기 호출·탑승을 자동화하는 연동 계층 없이 성립하지 않는다. [추정][^ref-946][^ref-939]

자세한 내용은 주제 페이지 [63. 병원·의료 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area63-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [63. 병원·의료 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area63-s7.md)에 있다.

## 8. 대표 연구와 자료

Babalola, G. T. 외, A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (2024) — 2018년 이후 간호 협동로봇 연구 28편을 검토해 28편 중 14편이 TRL 4~5 수준(TRL 9 는 1편)이고 환자 중심 설계가 많아 간호 업무 부담을 줄이는 물류·행정 보조 로봇은 드물며, 배송 로봇의 동료 심사 근거와 비용·유지보수·사이버보안 분석이 부족하다고 결론짓는다. [사실][^ref-949]

자세한 내용은 주제 페이지 [63. 병원·의료 — 대표 연구와 자료](../../topics/2026/2026-09-29-area63-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 약국·병동·검사실이 내는 이송 요청을 받아 제조사가 다른 로봇에 배정하고, 수령 확인 결과를 병원 정보 시스템에 돌려준다. [추정][^ref-939][^ref-947] | 연계 대상: 처방·조제·검사 지시를 내는 병원 정보 시스템(HIS·EMR·약국 시스템)의 판단 [추정][^ref-939] |
| 시설·설비 제어 | 승강기·자동문을 예약·연동하고 탑승·통과 상태를 확인한다. [추정][^ref-946][^ref-941] | 연계 대상: 승강기 제어반·자동문의 제어 자체(고대구로병원의 TK50M 전용 통신 모듈처럼 설비 쪽 장치) [추정][^ref-946] |
| 로봇 자체 지능·제어 | 로봇이 할 수 있는 이송 기능과 실행 조건, 상태·실패·완료를 확인한다. [추정][^ref-946] | 연계 대상: 자율 주행·회피와 ISO 13482 안전 기능의 성능 [추정][^ref-946][^ref-948] |
| 업종별 조건 | 감염 관리 구역·야간 시간대·권한을 경로·배정 제약으로 반영하고, RFID·생체인증 같은 수령 인증으로 완료를 확인한다. [추정][^ref-939][^ref-953][^ref-941] | 연계 대상: 감염 관리 기준 설정(병원 감염관리 조직), 환자 정보 보호·의료 관련 법령(이번 실행에서 법령 원문 미확인) [추정][^ref-953] |

이 경계는 분류 원문 19장의 표를 이 영역에 맞게 옮긴 것이며 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)). 이종 제조사를 잇는 ROP 는 이송 요청 수신·배정·승강기 예약·수령 인증 확인·결과 반환과 승강기 혼잡 같은 실패를 받아 재계획하는 일까지를 인터페이스와 실행 보장으로 맡고, 처방 판단·승강기 제어·안전 기능 성능·감염 관리 기준 설정은 병원 정보 시스템·승강기 업체·로봇 제조사·병원 감염관리 조직에 맡긴다. [추정][^ref-939][^ref-946][^ref-953][^ref-948] 싱가포르 RoMi-H 가 이를 공공 의료 전체의 통합 플랫폼으로 보였고, 국내는 한림대성심병원의 통합관제가 가장 가까운 공개 사례이나 통합관제 언급 수준이며 인터페이스·표준은 미확인이다. [추정][^ref-940][^ref-872][^ref-947]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md) — 서비스로봇 실증사업·스마트병원 선도모델 같은 정부 지원과 대당 억 단위 비용이 도입 여부를 가른다. [추정][^ref-950][^ref-953][^ref-951]

자세한 내용은 주제 페이지 [63. 병원·의료 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area63-s10.md)에 있다.

## 11. 열린 질문

**oq-149** (상태: 열림 · 실행 2026-09-29-13 부분 답) 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? — 싱가포르 등재 프로그램은 2025-05-01 부터 2년 유효한 통합사 5개 등재로 계속 운용 중임이 확인되나, 국내에서 벤더·통합사를 사전 평가해 병원 로봇 공급 자격을 주는 제도는 이번 조사에서 확인되지 않았고, 확인된 국내 제도는 과제 단위로 서류·발표·현장평가를 거치는 서비스로봇 실증사업과 스마트병원 선도모델 사업뿐이며 이는 벤더 등록 자격 제도가 아니다. [추정][^ref-872][^ref-950][^ref-951][^ref-953]

자세한 내용은 주제 페이지 [63. 병원·의료 — 열린 질문](../../topics/2026/2026-09-29-area63-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-940]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-29
[^ref-941]: 이데일리, 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입, 2023-07-06, https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896, 접근일 2026-09-29
[^ref-942]: 뉴스투데이, [한림대성심병원 로봇 사용기 (下)] 배송로봇, 엘리베이터 타고 횡단보도 건너 검체 운반, 2025-02-11, https://www.news2day.co.kr/article/20250211500007, 접근일 2026-09-29
[^ref-943]: 데일리팜, 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람, 2024-07-15, https://m.dailypharm.com/user/news/15128, 접근일 2026-09-29
[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-945]: Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare, 2021-02-10, https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-947]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-29
[^ref-948]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-949]: Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?, 2024-06-05, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29
[^ref-952]: 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)), 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683, 접근일 2026-09-29 (KCI 초록 확인, 본문 PDF 미열람)
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29
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

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s11.md

```markdown
---
title: "63. 병원·의료 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-872, ref-946, ref-947, ref-950, ref-951, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#11
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 열린 질문

# 63. 병원·의료 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-149** (상태: 열림 · 실행 2026-09-29-13 부분 답) 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? — 싱가포르 등재 프로그램은 2025-05-01 부터 2년 유효한 통합사 5개 등재로 계속 운용 중임이 확인되나, 국내에서 벤더·통합사를 사전 평가해 병원 로봇 공급 자격을 주는 제도는 이번 조사에서 확인되지 않았고, 확인된 국내 제도는 과제 단위로 서류·발표·현장평가를 거치는 서비스로봇 실증사업과 스마트병원 선도모델 사업뿐이며 이는 벤더 등록 자격 제도가 아니다. [추정][^ref-872][^ref-950][^ref-951][^ref-953]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-149** (상태: 열림 · 실행 2026-09-29-13 부분 답) 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? — 싱가포르 등재 프로그램은 2025-05-01 부터 2년 유효한 통합사 5개 등재로 계속 운용 중임이 확인되나, 국내에서 벤더·통합사를 사전 평가해 병원 로봇 공급 자격을 주는 제도는 이번 조사에서 확인되지 않았고, 확인된 국내 제도는 과제 단위로 서류·발표·현장평가를 거치는 서비스로봇 실증사업과 스마트병원 선도모델 사업뿐이며 이는 벤더 등록 자격 제도가 아니다. [추정][^ref-872][^ref-950][^ref-951][^ref-953]
- **oq-134** (상태: 열림 · 실행 2026-09-29-13 미해결) 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가? — 가장 가까운 국내 자료는 고대구로병원 연구가 운영 기록의 승강기 가동률과 성공률 관계를 몬테카를로 모형으로 분석한 것이며 운영 기록의 시뮬레이션 재현은 아니다. [추정][^ref-946]
- **oq-138** (상태: 열림 · 실행 2026-09-29-13 미해결) 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가? — 국내 병원에서는 이번 조사에서도 확인되지 않았다. [추정][^ref-946][^ref-947]
- **oq-142** (상태: 열림 · 실행 2026-09-29-13 미해결) 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가? — 국내 병원에서 가장 가까운 자료는 한림대성심병원의 통합관제이며 대화형 지시 사례는 확인되지 않았다. [추정][^ref-947]
- (신규, id 는 퍼블리셔가 부여) 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)?
- (신규, id 는 퍼블리셔가 부여) 격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가?
- (신규, id 는 퍼블리셔가 부여) 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가?
- (신규, id 는 퍼블리셔가 부여) 한림대성심병원처럼 제조사가 다른 여러 로봇을 통합관제하는 국내 병원은 어떤 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API)으로 로봇과 승강기를 연결하며 그 구조가 공개돼 있는가?
- (신규, id 는 퍼블리셔가 부여) 국내 병원에서 식사(환자식) 이송을 로봇이 맡은 운영 사례가 있으며, 식사 이송은 약품·검체 이송과 시작 조건·시간 제약·인계 방식이 어떻게 다른가?

전체 목록: [열린 질문](../../open-questions.md)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-947]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s4.md

```markdown
---
title: "63. 병원·의료 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-872, ref-939, ref-940, ref-945, ref-946, ref-949, ref-950, ref-951, ref-952, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#4
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 핵심 개념과 용어

# 63. 병원·의료 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **의료 로봇 미들웨어 RoMi-H(Robotic Middleware for Healthcare)** — 싱가포르 창이종합병원 CHART(Centre for Healthcare Assistive & Robotics Technology)가 만든 ROS 2·DDS(Data Distribution Service) 기반 오픈소스 미들웨어로, 2018-07 보건부 장관 발표 뒤 2019-10-31 ROSCon 에서 공개됐고 기계·제어·중앙·통합의 네 도메인으로 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 잇는 것을 목적으로 한다. [사실][^ref-940]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **의료 로봇 미들웨어 RoMi-H(Robotic Middleware for Healthcare)** — 싱가포르 창이종합병원 CHART(Centre for Healthcare Assistive & Robotics Technology)가 만든 ROS 2·DDS(Data Distribution Service) 기반 오픈소스 미들웨어로, 2018-07 보건부 장관 발표 뒤 2019-10-31 ROSCon 에서 공개됐고 기계·제어·중앙·통합의 네 도메인으로 서로 다른 제조사의 로봇·센서·병원 정보 시스템을 잇는 것을 목적으로 한다. [사실][^ref-940] IHiS·GovTech·Hope Technik·Open Robotics 가 협력했고 [오픈 RMF](../../glossary/open-rmf.md)(Open-RMF)를 핵심 기반으로 한다. [사실][^ref-945] 두 출처는 같은 프로젝트의 참여 기관이라 독립 교차 확인으로 세지 않는다.
- **Open-RMF 의 [플릿 어댑터](../../glossary/fleet-adapter.md)와 [승강기 어댑터](../../glossary/lift-adapter.md)** — 서로 다른 제조사의 로봇 플릿과 문·승강기를 붙이는 오픈소스 구조로, RoMi-H 가 이를 기반으로 싱가포르 공공 병원에 적용됐으므로 병원의 이기종 로봇·승강기 연동 참고 구조로 볼 수 있다. [추정][^ref-004][^ref-945]
- **승강기 가동률(Elevator Operating Rate, EOR)** — 고대구로병원 연구가 쓴 지표로, 가동률이 높을수록 배송 로봇의 임무 실패가 늘었다. [사실][^ref-946]
- **등재 프로그램(Empanelment Programme)** — 창이종합병원 CHART 가 RoMi-H 를 배치할 시스템 통합사의 기술 전문성과 배치 지식을 평가해 2025-05-01 부터 2년 유효한 인증을 주고 공공 의료기관의 RFP·RFI 참여 목록으로 게시하는 제도이며 정기적으로(원문 표기 bi-annual) 운영된다. [사실][^ref-872]
- **스마트병원 선도모델과 '지능형 원내 물류 배송' 모듈** — 한국보건산업진흥원 스마트병원 확산지원센터가 개별 선도모델 58개를 9개 모듈로 재구성한 것으로, 이 모듈은 자율주행 로봇과 보안이 강화된 생체인증 시스템으로 약국·물품공급실·병동 간 무인 배송 체계를 정의한다. [사실][^ref-953]
- **서비스로봇 실증사업** — 한국로봇산업진흥원이 2020년부터 물류·웨어러블·의료·기타 네 분야의 로봇 도입 비용 50% 이내를 국비로 지원하는 사업으로, 공모 → 서류·발표·현장평가 → 과제 선정 → 협약 → 중간 점검 → 최종 평가 순서로 진행된다. [사실][^ref-950][^ref-951]
- **수령 인증** — 픽업·배송 지점에서 RFID(Radio-Frequency Identification)로 신원을 확인하거나 생체인증 시스템으로 무인 배송을 통제해 인계를 확인하는 방식이다. [사실][^ref-939][^ref-953]
- **감염환자 이송 로봇** — 감염병 대응 수단으로 사람을 작업 대상으로 하는 이송 로봇이며, 의료종사자 인식 조사에서 환자 이송 과정의 안전이 최우선이고 이송 중 기기 오류 해결·응급처치 제공 용이성·환자 모니터링·감염 인자 억제 능력이 중요하다는 결과가 나왔다. [사실][^ref-952]
- **[기술 성숙도](../../glossary/technology-readiness-level.md)(Technology Readiness Level, TRL)** — 간호 협동로봇 체계적 검토는 28편 중 14편이 TRL 4~5 수준(TRL 9 는 1편)이라고 집계했다. [사실][^ref-949]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-940]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-29
[^ref-945]: Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare, 2021-02-10, https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-949]: Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?, 2024-06-05, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29
[^ref-952]: 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)), 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683, 접근일 2026-09-29 (KCI 초록 확인, 본문 PDF 미열람)
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s6.md

```markdown
---
title: "63. 병원·의료 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-939, ref-941, ref-942, ref-945, ref-946, ref-947, ref-948, ref-952, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#6
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 대표 접근법과 기술

# 63. 병원·의료 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 승강기는 병원에서 로봇이 사람·침대와 함께 쓰는 공용 자원이므로, 층간 이송은 승강기 호출·탑승을 자동화하는 연동 계층 없이 성립하지 않는다. [추정][^ref-946][^ref-939]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 승강기·자동문 연동

승강기는 병원에서 로봇이 사람·침대와 함께 쓰는 공용 자원이므로, 층간 이송은 승강기 호출·탑승을 자동화하는 연동 계층 없이 성립하지 않는다. [추정][^ref-946][^ref-939] 고대구로병원 연구는 TK엘리베이터 TK50M 제어반에 부착한 전용 통신 모듈로 호출·탑승을 자동화했고, 산시성 인민병원 연구는 사물인터넷(Internet of Things, IoT) 기반 승강기 제어로 층간 자율 이동을 구현했으며, 분당서울대병원은 승강기·자동문이 다중으로 연동돼 자동 작동한다. [사실][^ref-946][^ref-939][^ref-941] 산업통상자원부 국가기술표준원은 2021-11-11 로봇의 승강기 탑승 시 안전 요구사항(속도 제어·위험 상황의 보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지)과 실내 배송 로봇에 관한 국가표준(KS) 제정을 발표했으나, 이번 조사 자료에는 표준 번호·정식 명칭이 없다. [사실][^ref-948]

### 이기종 로봇 미들웨어와 통합관제

제조사가 다른 로봇을 한 병원에서 함께 쓰려면 로봇·센서·병원 정보 시스템을 잇는 공통 계층이 필요하다. RoMi-H 는 여러 제조사의 로봇이 승강기 같은 병원의 물리 자산을 공유하고, 경로 계획 시각화와 다른 로봇에 대한 출입 금지 구역으로 충돌을 피하며, 로봇 플랫폼·센서·기업 정보 시스템에 걸친 통일된 통신·모니터링을 제공한다. [사실][^ref-945] 그 기반인 Open-RMF 는 플릿 어댑터로 로봇 플릿을, 문·승강기 어댑터로 설비를 붙이는 구조여서 병원의 이기종 연동 참고 구조로 볼 수 있다. [추정][^ref-004][^ref-945] 국내에서는 한림대성심병원이 제조사가 다른 여러 로봇을 통합관제 시스템으로 커맨드센터에서 중앙 관리하는 것이 가장 가까운 공개 사례이나, 인터페이스·표준은 확인되지 않았다. [추정][^ref-947]

### 수령 인증과 비접촉 배송

감염 관리와 약품 보안은 '누가 받았는가'를 로봇 쪽에서 확인하는 방식으로 다뤄진다. 산시성 인민병원 연구는 픽업·배송 지점의 RFID 신원 확인으로 수령을 인증하고 비접촉 배송으로 인력 이동과 교차 감염 위험을 줄였으며, 약국·병동·시스템 관리자·장비 관리자의 역할을 정한 협력 책임 체계를 운영 관리 틀로 두었다. [사실][^ref-939] 스마트병원 '지능형 원내 물류 배송' 모듈은 자율주행 로봇과 보안이 강화된 생체인증 시스템으로 약국·물품공급실·병동 간 무인 배송 체계를, '하나로 감염관리' 모듈은 방문객 출입 통제·동선 분석·혼잡도 관리·환경 소독까지 감염관리 업무 자동화를 정의한다. [사실][^ref-953]

### 야간 배송과 동선 분리

분당서울대병원은 야간 배송으로 로봇 이동을 환자 동선과 분리했다. [사실][^ref-941] 감염환자 이송 로봇에 대한 의료종사자 인식 조사에서도 환자 이송 과정의 안전이 최우선이었다. [사실][^ref-952]

### 승강기 혼잡의 사전 타당성 분석

고대구로병원 연구는 배송 122건의 운영 기록에서 승강기 가동률과 성공률의 관계를 몬테카를로 모형으로 분석해 EOR 59% 미만에서 성공률 95.52%, 실패는 EOR 90% 초과 구간에 집중된다는 결과를 얻었다(단일 기관·2025-06-18~29, 단일 로봇). [사실][^ref-946] 이는 운영 기록으로 배차·재계획 제약을 정하는 사전 분석이며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 실시간 모델과는 구분된다. [추정][^ref-946]

### 정착 과정

한림대성심병원 커맨드센터는 시스템 정착에 약 3년이 걸렸고, 사용자 공감대 형성과 보급형 로봇의 한계에 맞춘 병원 시스템 변경이 과제였다고 밝혔다. [사실][^ref-942]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-941]: 이데일리, 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입, 2023-07-06, https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896, 접근일 2026-09-29
[^ref-942]: 뉴스투데이, [한림대성심병원 로봇 사용기 (下)] 배송로봇, 엘리베이터 타고 횡단보도 건너 검체 운반, 2025-02-11, https://www.news2day.co.kr/article/20250211500007, 접근일 2026-09-29
[^ref-945]: Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare, 2021-02-10, https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-947]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-29
[^ref-948]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-952]: 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)), 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683, 접근일 2026-09-29 (KCI 초록 확인, 본문 PDF 미열람)
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s8.md

```markdown
---
title: "63. 병원·의료 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-911, ref-939, ref-946, ref-949, ref-950, ref-951, ref-952, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#8
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 대표 연구와 자료

# 63. 병원·의료 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Babalola, G. T. 외, A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (2024) — 2018년 이후 간호 협동로봇 연구 28편을 검토해 28편 중 14편이 TRL 4~5 수준(TRL 9 는 1편)이고 환자 중심 설계가 많아 간호 업무 부담을 줄이는 물류·행정 보조 로봇은 드물며, 배송 로봇의 동료 심사 근거와 비용·유지보수·사이버보안 분석이 부족하다고 결론짓는다. [사실][^ref-949]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Babalola, G. T. 외, A systematic review of collaborative robots for nurses: where are we now, and where is the evidence? (2024) — 2018년 이후 간호 협동로봇 연구 28편을 검토해 28편 중 14편이 TRL 4~5 수준(TRL 9 는 1편)이고 환자 중심 설계가 많아 간호 업무 부담을 줄이는 물류·행정 보조 로봇은 드물며, 배송 로봇의 동료 심사 근거와 비용·유지보수·사이버보안 분석이 부족하다고 결론짓는다. [사실][^ref-949] 이 영역에서는 운영 성과를 근거로 만드는 일의 출발점이다. [추정][^ref-949]
- Li, M. 외, Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (2026) — 산시성 인민병원의 AMR 10대 6개월 운영 효과 분석으로, 승강기 IoT 제어·RFID 신원 확인·협력 책임 체계·이용률까지 한 연구가 다룬다. 배송 시간 32~36%·7.3배·이용률 0.84 는 단일 연구 수치이며 독립 출처로 교차 확인되지 않았다. [사실][^ref-939]
- Lee, Y. 외, Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (2026) — 고대구로병원의 국내 연구로, 승강기 가동률을 배송 성공률의 제약 변수로 보였다. 성공률 87.03%·95.52% 는 단일 기관·단일 로봇·2025-06-18~29 조건이며 교차 확인되지 않았다. [사실][^ref-946]
- 최현철·서슬기·권재용·박상찬·장혜정, 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여 (2023) — 국내 의료종사자 인식을 SERVQUAL 다섯 차원(유형성·신뢰성·반응성·보증성·공감성)과 AHP 로 조사한 논문이며, KCI 초록만 확인했고 본문 PDF 는 열지 못해 설문 응답 수는 미확인이다. [사실][^ref-952]
- Fragapane, G. 외, Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda (2021) — 제조·창고·크로스독·터미널과 함께 병원을 AMR 적용 분야로 들어 병원이 인트라로지스틱스 AMR 연구의 대상 현장 가운데 하나임을 보인다(원문 미열람). [사실][^ref-911]
- 한국로봇산업진흥원 서비스로봇 실증사업 안내와 한국보건산업진흥원 스마트병원 선도모델·모듈 소개 — 국내 병원 로봇 도입의 정부 지원 구조를 보여 주는 기관 자료다. 실증사업의 국비 50%·절차 같은 세부 조건은 진흥원 단독 자료이며 기사는 사업 존재와 시작 연도만 확인한다. [사실][^ref-950][^ref-953][^ref-951]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-911]: Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)), Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda, 2021, https://doi.org/10.1016/j.ejor.2021.01.019, 접근일 2026-09-29 (원문 미열람)
[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-949]: Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?, 2024-06-05, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29
[^ref-952]: 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)), 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683, 접근일 2026-09-29 (KCI 초록 확인, 본문 PDF 미열람)
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s10.md

```markdown
---
title: "63. 병원·의료 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-872, ref-939, ref-940, ref-941, ref-942, ref-943, ref-946, ref-947, ref-948, ref-949, ref-950, ref-951, ref-952, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#10
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 다른 연구영역과의 연결

# 63. 병원·의료 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 서비스로봇 실증사업·스마트병원 선도모델 같은 정부 지원과 대당 억 단위 비용이 도입 여부를 가른다. [추정][^ref-950][^ref-953][^ref-951]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 서비스로봇 실증사업·스마트병원 선도모델 같은 정부 지원과 대당 억 단위 비용이 도입 여부를 가른다. [추정][^ref-950][^ref-953][^ref-951]
- [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) — RFID 신원 확인·생체인증이 약품·검체의 수령 확인 방법이다. [추정][^ref-939][^ref-953]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 야간 배송으로 환자 동선과 분리하는 운영이 사람 흐름 모델과 이어진다. [추정][^ref-941]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — RoMi-H 와 한림대성심병원 통합관제가 제조사가 다른 로봇을 잇는 사례다. [추정][^ref-940][^ref-947]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — Open-RMF 기반 RoMi-H 와 등재 프로그램이 공공 의료의 상호운용 기준으로 쓰인다. [추정][^ref-940][^ref-872]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기·자동문 연동과 로봇 승강기 탑승 KS 안전 요구가 이 영역의 핵심 제약이다. [추정][^ref-946][^ref-941][^ref-948]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 승강기는 로봇·사람·침대가 함께 쓰는 공용 자원이며 가동률이 성공률을 좌우한다. [추정][^ref-946]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 승강기 혼잡 시 임무 실패를 받아 재계획해야 한다. [추정][^ref-946]
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 배송 시간·건수·성공률이 병원 이송의 성과 지표로 쓰인다. [추정][^ref-939][^ref-947]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 감염환자 이송 안전과 승강기 탑승 시 보호 정지 요구가 사람 근접 조건이다. [추정][^ref-952][^ref-948]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — ISO 13482 적합 인증 시험과 KS 승강기 탑승 안전 요구사항이 적용된다. [추정][^ref-946][^ref-948]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 생체인증 기반 무인 배송 통제가 권한 관리와 이어진다. [추정][^ref-953]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 체계적 검토가 지적한 사이버보안 분석 부족과 환자 정보 보호가 이어진다(법령 원문은 이번 실행에서 미확인). [추정][^ref-949]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 구축 병원의 자동문·통로·승강기 턱 제약이 설치 가능성을 가른다. [추정][^ref-943][^ref-951]
- [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) — 정착에 약 3년이 걸리고 사용자 공감대 형성이 과제였다. [추정][^ref-942]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 등재 프로그램과 약국·병동·시스템 관리자·장비 관리자의 협력 책임 체계가 다사업자 책임 구조다. [추정][^ref-872][^ref-939]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-940]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-29
[^ref-941]: 이데일리, 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입, 2023-07-06, https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896, 접근일 2026-09-29
[^ref-942]: 뉴스투데이, [한림대성심병원 로봇 사용기 (下)] 배송로봇, 엘리베이터 타고 횡단보도 건너 검체 운반, 2025-02-11, https://www.news2day.co.kr/article/20250211500007, 접근일 2026-09-29
[^ref-943]: 데일리팜, 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람, 2024-07-15, https://m.dailypharm.com/user/news/15128, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-947]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-29
[^ref-948]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-949]: Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?, 2024-06-05, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29
[^ref-952]: 최현철, 서슬기, 권재용, 박상찬, 장혜정 (경희대학교, Korea SUNY; 품질경영학회지 51(3)), 감염환자 이송 로봇에 대한 의료종사자의 인식: SERVQUAL과 AHP를 활용하여, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002997683, 접근일 2026-09-29 (KCI 초록 확인, 본문 PDF 미열람)
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s3.md

```markdown
---
title: "63. 병원·의료 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-939, ref-943, ref-946, ref-949, ref-950, ref-951]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#3
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 왜 중요한가

# 63. 병원·의료 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 병원은 약품·검체·린넨을 옮기는 일이 감염 관리와 환자 정보 보호라는 조건 아래 놓이고 승강기와 복도를 환자·침대·직원과 함께 쓰는 현장이어서, 로봇 한 대의 주행 성능보다 승강기·자동문·수령 인증·병원 정보 시스템을 하나로 잇는 운영 계층이 이송 성과를 가른다. [추정][^ref-946][^ref-939]
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

병원은 약품·검체·린넨을 옮기는 일이 감염 관리와 환자 정보 보호라는 조건 아래 놓이고 승강기와 복도를 환자·침대·직원과 함께 쓰는 현장이어서, 로봇 한 대의 주행 성능보다 승강기·자동문·수령 인증·병원 정보 시스템을 하나로 잇는 운영 계층이 이송 성과를 가른다. [추정][^ref-946][^ref-939]

효과의 근거는 아직 단일 병원 연구가 중심이다. 중국 산시성 인민병원의 단일 연구(2025-06-01~11-30)는 자율이동로봇(Autonomous Mobile Robot, AMR) 10대로 약품·검체를 6개월 이송한 결과 수작업 대비 배송 시간이 32~36% 줄고 로봇 10대가 수작업 인력 19명보다 7.3배 많은 배송 횟수를 처리했으며 검증 정확도·물품 온전율 100%(수작업 97~99%)를 기록했다고 보고하는데, 이 수치는 독립 출처로 교차 확인되지 않았다. [사실][^ref-939]

국내에서는 한국로봇산업진흥원의 서비스로봇 실증사업과 한국보건산업진흥원의 스마트병원 사업이 2020년부터 병원 로봇 도입을 지원해 왔고, 의료진은 약사의 대면 업무와 간호사의 약제실 왕복이 줄었다고 평가하는 한편 속도·안전성 부족과 병원 물류의 복잡성을 지적했다. [사실][^ref-951][^ref-950] 자동출입문 장치 필요·통로 협소·승강기 턱 때문에 도입을 포기한 병원이 있어 기존 건물보다 신축 병원 위주로 도입된다. [사실][^ref-943] 그러므로 운영 계층은 건물·설비 조건을 처음부터 제약으로 받아야 한다. [추정][^ref-943]

한편 2018년 이후 간호 협동로봇 연구 28편을 검토한 체계적 문헌 검토는 미국 병원에 TUG 같은 배송 로봇이 도입돼 있음에도 동료 심사 근거가 '두드러지게 부족'하고 비용·유지보수·사이버보안 분석이 미흡하다고 결론짓는다. [사실][^ref-949] 이 영역은 상업 도입이 학술 근거보다 앞서 있는 현장이며, 운영 기록을 근거로 바꾸는 일 자체가 과제로 남아 있다. [추정][^ref-949]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-939]: Li, M. 외 (Scientific Reports), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04-24, https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/, 접근일 2026-09-29
[^ref-943]: 데일리팜, 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람, 2024-07-15, https://m.dailypharm.com/user/news/15128, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-949]: Babalola, G. T., Gaston, J.-M., Trombetta, J., & Tulk Jesso, S. (Frontiers in Robotics and AI), A systematic review of collaborative robots for nurses: where are we now, and where is the evidence?, 2024-06-05, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1398140/full, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-951]: 비즈한국, 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까, 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-13/pages/topics/2026/2026-09-29-area63-s7.md

```markdown
---
title: "63. 병원·의료 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 63
related_areas: [3, 17, 19, 20, 21, 22, 28, 32, 39, 49, 50, 51, 53, 55, 56, 58]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-872, ref-940, ref-945, ref-946, ref-948, ref-950, ref-953]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/hospital-and-healthcare.md#7
---

[홈](../../index.md) › [주제](../index.md) › 63. 병원·의료 — 관련 표준·프레임워크·오픈소스

# 63. 병원·의료 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO 13482 | 표준 | 고대구로병원 연구의 배송 로봇이 ISO 13482 적합 인증 시험을 거쳤다. [사실][^ref-946] | Lee 외(Digital Health) |
| 로봇의 승강기 탑승 안전 요구사항·실내 배송 로봇 KS(표준 번호·정식 명칭 미확인) | 표준 | 국가기술표준원이 2021-11-11 제정을 발표했으며 2020-10 '로봇산업 선제적 규제혁신 로드맵'에 따라 승강기 안전기준 소관인 행정안전부와 협력한 결과다. [사실][^ref-948] | 국가기술표준원 |
| Open-RMF | 오픈소스 | 플릿 어댑터·문·승강기 어댑터 구조로 RoMi-H 의 핵심 기반이다. [추정][^ref-004][^ref-945] | Open Robotics |
| RoMi-H | 오픈소스 | 싱가포르 보건부가 공공 의료기관의 자동화 통합 플랫폼으로 인정한 의료 로봇 미들웨어다. [사실][^ref-940][^ref-872] | 창이종합병원 CHART |
| RoMi-H 등재 프로그램 2025 | 평가 프로그램 | 시스템 통합사를 사전 평가해 2025-05-01 부터 2년 유효한 인증을 주고 공공 의료기관 RFP·RFI 참여 목록으로 쓴다. [사실][^ref-872] | 창이종합병원 CHART |
| 서비스로봇 실증사업 | 평가 프로그램 | 2020년부터 의료 분야를 포함해 로봇 도입 비용 50% 이내를 국비로 지원하며 서류·발표·현장평가를 거친다. [사실][^ref-950] | 한국로봇산업진흥원 |
| 스마트병원 선도모델(9개 모듈) | 프레임워크 | '지능형 원내 물류 배송'·'하나로 감염관리' 모듈이 병원 로봇 이송과 감염관리 자동화를 정의한다. [사실][^ref-953] | 한국보건산업진흥원 |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/hospital-and-healthcare.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/hospital-and-healthcare.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-940]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-29
[^ref-945]: Open Robotics, ROMI-H: Bringing Robot Traffic Control to Healthcare, 2021-02-10, https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare, 접근일 2026-09-29
[^ref-946]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-29
[^ref-948]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-950]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-29
[^ref-953]: 한국보건산업진흥원 스마트병원 확산지원센터, 선도모델 및 모듈 소개, 미확인, https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-13 | 63. 병원·의료 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
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

### runs/2026-09-29-13/verification2.json

```json
{
  "run_id": "2026-09-29-13",
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
      "f17(ref-911)·f18(ref-004)은 61. 물류창고·62. 제조 공장 페이지와 같은 출처를 재사용한 주장이며 페이지가 기존 각주 id 를 그대로 썼다(신규 각주 없음)",
      "RoMi-H·등재 프로그램(f4·f5·f6)은 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성·58. 다사업자 책임·계약·데이터 와 겹치나 페이지가 병원 사례로만 쓰고 10절에서 연결했다(1차 지시대로)"
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
    "8. 대표 연구와 자료 절 첫 항목(Babalola 외 체계적 검토): [사실][^ref-949] 를 '…분석이 부족하다고 결론짓는다.' 바로 뒤에 붙이고, 이어지는 '이 영역에서는 운영 성과를 근거로 만드는 일의 출발점이다.' 는 [추정][^ref-949] 로 바꾸거나 뺀다 — 자동 분리 뒤 세부영역 페이지 8절에 남은 요약 문장(…결론짓는다.)에 태그·각주가 없고, 분리 주제 페이지(2026-09-29-area63-s8.md) 3절에서는 구축자 해석 문장이 [사실] 로 태그돼 있다.",
    "3. 왜 중요한가 절(2026-09-29-area63-s3.md 3절 세 번째 단락): '자동출입문 장치 필요·통로 협소·승강기 턱 때문에 도입을 포기한 병원이 있어 기존 건물보다 신축 병원 위주로 도입되므로, 운영 계층은 건물·설비 조건을 처음부터 제약으로 받아야 한다. [사실][^ref-943]' 을 두 문장으로 나눠 앞 문장(도입 포기·신축 병원 위주)만 [사실][^ref-943] 로 두고 '운영 계층은 … 받아야 한다' 는 [추정][^ref-943] 로 태그한다 — 뒤 절은 출처(f10)에 없는 구축자 추론이다.",
    "5. 적용 사례 절 울산대학교병원 표의 제약 칸: '속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기 같은 건축 구조' 앞에 '기사가 전한 국내 병원 일반의 장애 요인:' 을 붙인다 — f11(비즈한국)은 이 장애 요인을 국내 병원 로봇 도입 일반의 문제로 전하며 울산대병원 사례에 한정해 적지 않았다.",
    "glossary_updates '의료 로봇 미들웨어 RoMi-H': sources 에 ref-872 를 더한다 — 정의의 '싱가포르 보건부가 공공 의료기관의 자동화 통합 플랫폼으로 인정한다' 는 f6(ref-872)의 내용이며 ref-940·ref-945 에는 없다(7절 표는 이미 [^ref-940][^ref-872] 로 바르게 인용했다).",
    "glossary_updates '승강기 가동률': 정의에서 '승강기 대기가 길어지고' 를 빼고 '가동률이 높을수록 배송 로봇의 임무 실패가 늘어난다는 관계' 로 한정한다 — 1차 수정 지시 15 가 확인 범위를 '실패가 늘었다' 관계로 한정했고, 4절 본문(2026-09-29-area63-s4.md)은 이미 그렇게 썼으나 용어집 정의만 대기 시간 증가를 남겼다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 23건, 미확인 2건(f10 병원 목록 일부 불일치, f19 근거 없는 '마약류·수술실'), 교차 확인 4건(f7 분당서울대 AMR 6대·품목, f8 한림대성심 7종 73대·27,300건, f11 울산대병원 항암제 이송로봇 케로, f12 서비스로봇 실증사업 2020년 시작). 강등: 없음(f4·f12 의 finding 신뢰도 high 는 medium 으로 낮춤). 원문 미열람 출처: ref-911(검색 결과 일치). 주의: 핵심 성과 수치(f1 배송 시간 32~36%·7.3배, f3 성공률 87.03%·95.52%)는 각각 단일 병원·단일 연구의 결과로 독립 출처 교차 확인이 없으며, f4 의 두 출처는 같은 프로젝트 참여 기관이라 독립적이지 않다. 미사용 출처 없음. 정정 요청 없음. oq-149 는 부분 답(f24)이며 해결 인정하지 않음, oq-134·oq-138·oq-142 미해결 유지. 페이지 신뢰도 medium. / 2차 수정 후 재검증. 드리프트 없음(브리프 밖 사실·수치·사례 추가 없음, 처분 finding 잔존 없음), 1차 수정 지시 18건 이행 확인(ref-872 발행일 2025-05-01, bi-annual 표기, f10 병원 목록, f11·f15·f16·f19·f20·f2·f3·f8 문구, f1·f2·f3 단일 연구 조건 병기, f4 출처 분리, f17 원문 미열람 표기, 5절 현장 유형 병원 명시·여섯 항목 표, 11절 열린 질문 처리), [분류원문] 보존(admonition 세 줄·1절·2절 시드와 글자 단위 일치), 섹션 순서·링크·분량은 형식 검증 코드 통과를 따름(10절 링크 16건은 부록 A 경로와 일치). 수정 지시 5건은 태그 누락 1건(8절 분리 요약), 추론 문장의 [사실] 태그 2건(8절 마지막 문장, 3절 '받아야 한다'), 사례 귀속 표시 1건(울산대 제약 칸), 용어집 정의·출처 2건이며 finding 태그 처분 변경은 없다. 퍼블리셔 참고: 자동 분리 뒤 세부영역 페이지 프런트매터 sources 에 남은 ref-004·ref-911·ref-949 는 세부영역 페이지 본문·13절에는 더 이상 인용되지 않고 분리 주제 페이지(s4·s6·s7·s8)에만 각주가 있으며 reference_updates 의 cited_by 도 세부영역 페이지만 적혀 있어 인용 페이지 목록을 만들 때 분리 페이지를 포함해야 한다; standards_updates 의 ISO 13482 항목 url 이 표준 페이지가 아니라 근거 논문(PMC) URL 이다; 분리 주제 페이지의 9. 검증 노트는 코드가 넣은 고정 문구('원 페이지와 함께 … 검증을 거쳤다')이며 1차 판정·건수 문구가 아니다. 2차 도구 사용 없음(검색 0회).",
  "retry_reason": null
}
```
