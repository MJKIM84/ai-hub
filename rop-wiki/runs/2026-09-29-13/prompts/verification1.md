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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/commercial-facilities.md (요약)

```markdown
# 64. 상업 시설

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/home-and-apartment.md (요약)

```markdown
# 65. 가정·공동주택

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
```

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/other-sites.md (요약)

```markdown
# 67. 기타 현장

소속 대분류: Q. 현장 유형별 적용 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
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

### runs/2026-09-29-12/research.md

```markdown
# 리서치 브리프 2026-09-29-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-12 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 62. 제조 공장 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 조립라인 공급 문제·인플랜트 밀크런·셀 생산 방식 용어 없음(ISA-95·VDA 5050·플러그 앤 프로듀스·협동 적용·운용 구역·종합설비효율은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 국내(LG전자 창원, 현대차그룹 HMGICS)·해외(BMW, 폭스바겐 하노버) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 라인 공급 정책, 밀크런·견인차 스케줄링, 생산 관리 시스템에서 운송 주문 생성, 다중 로봇 조립, 협동로봇 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISA-95, VDA 5050, ISO 3691-4, Open-RMF 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 조립라인 공급 분류 서베이, 협동로봇 서베이, 다중 로봇 조립 서베이, 국내 시뮬레이션 논문 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 21. 상호운용 표준·적합성, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 31. 사람–로봇 협업, 34. 시뮬레이션·예측용 디지털 트윈, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-142 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
2. 조립라인에 부품을 공급하는 방식(라인 적재, 상자 공급, 순서 공급, 키팅)과 무인 운반차·견인차 스케줄링은 학술 문헌에서 어떻게 분류·모델링되는가? (섹션 4·6·8 겨냥)
3. 생산 관리 시스템(MES·자재 관리)은 로봇 플릿에 어떤 방식으로 운송 주문을 내고 결과를 받으며, ISA-95 같은 표준 모델이 그 연결에 어떻게 쓰이는가? (섹션 6·7·9 겨냥)
4. 자동차·전자·배터리 공장의 실제 도입 사례(국내 LG전자·현대차그룹, 해외 BMW·폭스바겐)에서 로봇 작업의 시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과는 어떻게 나타나는가? (섹션 5 겨냥, 현장 유형 제조 공장 명시, 한국 자료 우선)
5. 여러 로봇이 함께 하는 공정 작업(다중 로봇 조립, 협동로봇, 모바일 매니퓰레이터)은 어떤 연구가 다루며 어떤 안전·인간 요인 조건이 붙는가? (섹션 6·8·10 겨냥)
6. 제조 공장의 무인 운반차 운영에 적용되는 상호운용 표준(VDA 5050)과 안전 표준(ISO 3691-4)은 무엇을 규정하며 ROP 의 위치를 어떻게 규정하는가? (섹션 7·9 겨냥)
7. oq-142: 국내 제조 공장에서 대화(자연어)로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Schmid·Limère(International Journal of Production Research 57(24), 2019)의 조립라인 공급 문제(assembly line feeding problem) 분류 연구는 대량 맞춤화와 제품 다양성이 조립라인 공급 시스템에 대한 관심을 키웠다고 보고, 부품을 라인 적재·상자 공급·순서 공급·정치식 키팅·이동식 키팅 같은 공급 정책에 배정하는 전술적 문제를 여러 차원으로 분류해 실무 문제와 학술 해법을 잇는 틀을 제시한다. | ref-922 | 아니오 | medium | 2019-02-23 | 제조 공장 / 작업 대상 | — |
| f2 | [사실] | 강명훈·곽춘종(부산대학교, Asia-Pacific Journal of Business & Commerce, 2014)은 R자동차 공장에서 도어·후드·트렁크 조립체를 유인 견인차 대신 AGV 기반 무인 물류 시스템으로 생산라인 사이에 공급하는 방안을 Witness 시뮬레이션으로 검토해 적정 AGV 대수, 단일 차선 양방향 AGV 도로의 타당성, 투자 타당성을 산정했다. | ref-935 | 아니오 | medium | 2014 | 제조 공장 / 수행 자원 | — |
| f3 | [사실] | 옥창훈·김득수·공정수·서윤호(고려대학교·현대자동차, 한국시뮬레이션학회 논문지 21(2), 2012)는 자동차 생산라인의 차체 버퍼 창고(WBS·PBS)가 각각 따로 운영되어 결품(starvation)과 막힘(blocking)이 생기는 문제에 대해 통합창고 시뮬레이션 모형을 제안하고 적정 스태커 크레인·AGV 대수와 운영 방식을 도출해 도장 라인 정지 상황에서 기존 창고보다 효율적임을 보였다. | ref-936 | 아니오 | medium | 2012 | 제조 공장 / 예외·성과 | — |
| f4 | [사실] | Wally 외(arXiv 1911.05481, 2019)는 모델 기반 공학으로 ISA-95 기반 생산 시스템 모델을 계획 도메인 정의 언어(PDDL) 파일로 변환해 범용 계획기가 목표 달성에 필요한 생산 단계 순서를 계산하게 하고 그 결과 계획을 다시 생산 시스템 모델에 통합하는 방법을 제안해, 생산 관리 표준 모델과 로봇·설비 작업 계획을 잇는 연구 사례를 보인다. | ref-925 | 아니오 | medium | 2019-11-13 | — | — |
| f5 | [추정] | 지멘스의 백서에 따르면 AGV 는 공장의 인트라로지스틱스·자재 관리 시스템과 통합되어 자재 관리 시스템이 자동으로 운송 주문을 생성해 AGV 에 보낼 때 사람 개입과 오류가 줄고 JIT·칸반 자재 공급이 이어질 수 있다. | ref-926 | 아니오 | low | 2026-09-29 | 제조 공장 / 시작 조건 | 벤더 주장 |
| f6 | [사실] | 독일자동차산업협회(VDA)의 VDA 5050 소개 글에 따르면 VDA 5050 은 VDA 가 VDMA 와 협력하고 KIT IFL 의 지원을 받아 2019년에 만든 인터페이스 표준으로 제조 공장에서 서로 다른 제조사의 무인 운반차를 하나의 관제 시스템 아래 두게 하며, AGV Mesh-Up 2021 실증에서 여섯 제조사의 차량이 다른 제조사의 관제 시스템 아래 운행됐고 2.0.0 판이 공개됐다. | ref-923 | 아니오 | medium | 2026-09-29 | 제조 공장 | — |
| f7 | [추정] | BMW 그룹 딩골핑·데브레첸 공장 물류기획 책임자 Peter Kiermaier 는 VDA 소개 글에서 BMW 그룹이 2021년 3월부터 VDA 5050 프로젝트 그룹 의장을 맡고 스마트 운반 로봇·자율 견인차·자율 지게차 여러 프로젝트에 VDA 5050 을 적용하며 새 AGV 시스템 입찰의 표준으로 정했다고 밝혔다. | ref-923 | 아니오 | low | 2026-09-29 | 제조 공장 / 수행 자원 | 벤더 주장 |
| f8 | [추정] | 관제 소프트웨어 업체 SYNAOS 는 2025-10-16 게시한 사례 글에서 폭스바겐 상용차 하노버-슈퇴켄 공장이 세계 최대 VDA 5050 플릿으로 MLR 언더라이드 로봇 약 100대와 괴팅·린데 자율 견인차 40대 등 135대 이상을 자사 인트라로지스틱스 관리 플랫폼으로 제조사 독립적으로 관제해 하루 9,000개 랙을 옮기고 연 30만 km 를 주행하며 트럭 하역장→내부 슈퍼마켓→작업자 준비→조립라인 자동 운반의 JIT·JIS 공급을 이룬다고 주장한다. | ref-924 | 아니오 | low | 2025-10-16 | 제조 공장 / 수행 자원 | 벤더 주장 |
| f9 | [사실] | 물류신문(2024-07-18)에 따르면 LG전자는 스마트팩토리 솔루션 사업에 자체 개발한 자율이동로봇(AMR)과 로봇팔을 결합한 자율주행 수직다관절로봇(MM)을 적용해 공장 내 부품·자재 공급을 맡기고, MM 은 운반뿐 아니라 조립·불량 검사와 다른 AMR 의 배터리 교체까지 수행하며, LG 그룹 40여 지역 60개 사업장에 적용됐고 2024년 외부 매출 2,000억 원을 목표로 한다. | ref-927 | 아니오 | medium | 2024-07-18 | 제조 공장 / 수행 자원 | — |
| f10 | [추정] | LG전자는 스마트팩토리 솔루션을 적용한 창원 공장에서 생산성 17% 향상, 에너지 효율 30% 개선, 품질 비용 70% 절감이라는 성과를 냈다고 밝혔다. | ref-927 | 아니오 | low | 2024-07-18 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f11 | [추정] | 현대자동차그룹은 2023-11-21 공개한 싱가포르 글로벌 혁신센터(HMGICS)가 컨베이어 대신 작업자와 로봇이 함께 일하는 타원형 셀에서 여러 차종을 동시에 생산하는 셀 기반 생산 방식과 디지털 트윈 메타 팩토리를 갖추고 AGV·AMR·스팟 점검 로봇·로봇팔 등 약 200대의 로봇으로 운송·조립 과정의 상당 부분을 자동화했으며 연 3만 대 이상의 전기차를 생산할 수 있다고 밝혔다. | ref-930, ref-937 | 아니오 | low | 2023-11-21 | 제조 공장 / 수행 자원 | 벤더 주장 |
| f12 | [사실] | Keshvarparast·Battini·Battaia·Pirayesh(Journal of Intelligent Manufacturing 35, 2023)의 체계적 문헌 검토는 조립·분해 작업에 투입되는 협동로봇 연구를 연구 대상·방법론·성과 지표·사람–협동로봇 상호작용 유형으로 분류하고, 제조가 맞춤화와 대응성으로 옮겨 가는 가운데 협동로봇이 유연성을 높이지만 작업자 안전과 일자리 대체 우려가 함께 다뤄져야 한다고 정리한다. | ref-933 | 아니오 | medium | 2023-05-30 | 제조 공장 | — |
| f13 | [사실] | Marvel·Bostelman·Falco(미국 국립표준기술연구소, ACM Computing Surveys 51, 2018)의 서베이는 산업용 로봇팔·다지 손·무인 운반차 같은 이동 플랫폼을 포함해 두 대 이상의 로봇 시스템이 치구 없이 조립하는 전략을 검토하며, 다중 로봇으로 가능한 조립 유형, 조립 중 로봇 동작을 맞추는 동기화 알고리즘, 조립 품질·효과를 평가하는 성능 지표의 세 갈래를 정리한다. | ref-934 | 아니오 | medium | 2018-01-01 | 제조 공장 | — |
| f14 | [사실] | Pietrantoni 외(Frontiers in Robotics and AI, 2024-12-02)는 유럽 기술 전문가 31명을 대상으로 한 혼합 방법 연구에서 차량 조립 사례의 협동로봇이 차량 지붕 같은 무거운 부품을 받쳐 주고 공구·부품을 골라 작업자에게 가져다주는 역할을 하며, 좁은 조립 공간에서 협동로봇끼리 그리고 외골격과의 충돌을 예측·회피하는 것이 핵심 안전·기술 과제라고 보고했다. | ref-928 | 아니오 | medium | 2024-12-02 | 제조 공장 / 제약 | — |
| f15 | [추정] | 시험·인증 기관 Applus+ Laboratories 의 서비스 안내에 따르면 ISO 3691-4:2023 은 무인 산업 차량(driverless industrial trucks)과 그 시스템의 안전 요구사항을 다루며 위험 분석·위험성 평가(부속서 B 표), 사람 감지, 제동·속도 제어, 안정성, 카테고리 대신 성능 수준(PL), 구역 정의·분류를 규정하고 이전 EN 1525 보다 구역 정의와 운송 시스템 간 상호작용을 개선했으며 EU 조화 표준으로 CE 인증에 쓰인다. | ref-938 | 아니오 | low | 2026-09-29 | 제조 공장 / 제약 | 벤더 주장 |
| f16 | [사실] | 테크데일리(2025-03-12)에 따르면 한국전자기술연구원(KETI)은 스마트공장·자동화산업전 AW 2025 에서 산업통상자원부·한국산업기술기획평가원 지원으로 개발한 'LLM 및 모방학습을 이용한 조립 공정 자동화 기술'을 공개해 사용자가 별도 작업 지시나 프로그래밍 없이 자연어로 양팔 로봇을 제어하는 것을 시연했으며, 이는 연구 단계 시연이고 현장 운영 사례는 아니다. | ref-932 | 아니오 | medium | 2025-03-12 | 제조 공장 / 시작 조건 | — |
| f17 | [사실] | 뉴시스(2026-09-07)에 따르면 과학기술정보통신부는 중소벤처기업부와 함께 중소 제조 현장에서 AI 가 자율이동로봇(AMR)·무인 운반차(AGV)의 적정 대수를 분석하고 가상 시뮬레이션으로 배치와 이동 경로를 정한 뒤 실제 투입하는 'AI 공장장' 사업을 대전 KAIST 시설과 전북·경남 시범 현장에서 추진하며, 2026년 개별 물류 작업에서 2027년 통합 물류, 2028년 생산 전 공정, 2029년 '다크팩토리 OS'로 범위를 넓힐 계획이고 기사에 자연어·언어 모델 지시는 언급되지 않는다. | ref-931 | 아니오 | medium | 2026-09-07 | 제조 공장 / 수행 자원 | — |
| f18 | [사실] | 장형준·이연주(건국대학교·오모로봇, 전기의 세계 67(8), 2018)의 동향 논문은 물류 로봇을 물류센터와 공장에서 운영 효율을 높이기 위해 쓰는 시스템으로 정의하고 AGV 가 1953년 미국 Barrett Electronics 의 첫 모델 이후 50년 넘게 자재 운반을 맡아 왔으며, 향후 로봇이 스스로 판단해 집고 싣는 단계로 나아가 AI·5G 와 결합할 것으로 전망한다. | ref-929 | 아니오 | medium | 2018 | 제조 공장 | — |
| f19 | [사실] | Interact Analysis(2023-01)는 독일 자동차 산업이 상호운용의 중요성을 먼저 인식해 VDA 5050 을 개발했고 Audi·VW·BMW 같은 완성차 업체가 이 표준을 따르는 마스터 컨트롤 업체를 지원하거나 분사시켜 공급사 전반의 채택을 이끌었다고 서술한다. | ref-257 | 아니오 | medium | 2023-01 | 제조 공장 | 원문 미열람 |
| f20 | [사실] | 서로 다른 세 발행 주체(독일자동차산업협회 VDA 의 소개 글, 시장조사 업체 Interact Analysis, 관제 소프트웨어 업체 SYNAOS)가 각각 BMW·VW 등 독일 완성차 공장이 VDA 5050 을 채택해 서로 다른 제조사의 무인 운반차를 하나의 관제 시스템 아래 운영한다고 전해, 제조 공장(특히 자동차 조립 공장)이 VDA 5050 기반 이기종 플릿 관제의 대표 현장임이 확인된다. | ref-923, ref-257, ref-924 | 예 | medium | 2025-10-16 | 제조 공장 / 수행 자원 | — |
| f21 | [추정] | Open-RMF 는 플릿 어댑터로 서로 다른 제조사의 로봇 플릿을 붙이고 작업·교통 조율과 문·승강기 같은 설비 연동을 제공하는 오픈소스 미들웨어로, 제조 공장의 라인 공급·공정 간 운반 로봇을 하나의 오케스트레이션 계층으로 묶는 참고 구조가 될 것으로 보이나 이번 조사에서 제조 공장 적용 사례는 확인하지 못했다. | ref-004 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f22 | [추정] | 확인한 자료를 종합하면 제조 공장의 로봇 작업은 세 형태로 들어간다: (1) 라인 공급 — 창고·슈퍼마켓에서 조립 스테이션으로 부품을 옮기는 AGV·견인차·AMR 로, 공급 정책(라인 적재·상자 공급·순서 공급·키팅)과 대수·경로 산정이 연구 대상이다(f1·f2·f8); (2) 공정 간 운반 — 차체·조립체를 라인과 버퍼 사이에서 옮기는 AGV·스태커 크레인으로, 결품·막힘 방지가 목표다(f2·f3); (3) 여러 로봇이 함께 하는 공정 작업 — 셀 안에서 작업자·로봇팔·이동 로봇이 함께 조립하거나(f11·f13) 협동로봇이 무거운 부품 지지·공구 전달을 맡는다(f14), 그리고 모바일 매니퓰레이터가 운반·조립·검사·다른 로봇의 배터리 교체까지 잇는다(f9). | ref-922, ref-935, ref-924, ref-936, ref-930, ref-937, ref-934, ref-928, ref-927 | 아니오 | low | 2026-09-29 | 제조 공장 | — |
| f23 | [추정] | 확인한 자료를 종합하면 제조 공장 로봇 작업의 여섯 항목은 시작 조건이 생산 계획·자재 관리 시스템이 내는 운송 주문과 칸반·JIT·JIS 호출(f5·f8), 작업 대상이 부품 상자·키트·랙·차체·조립체(f1·f2·f8), 수행 자원이 AGV·견인차·AMR·모바일 매니퓰레이터·협동로봇·로봇팔과 셀 작업자(f7·f9·f11·f14), 제약이 ISO 3691-4 의 운용 구역·사람 감지·성능 수준 요구와 좁은 조립 공간의 충돌 회피(f14·f15), 완료·인계가 스테이션 도착·하역과 생산 시스템으로의 상태 보고(f4·f5), 예외·성과가 라인 정지·결품·막힘과 생산성·품질 비용 지표(f3·f10)로 채워질 수 있으나, 각 사례의 수치는 회사 설명이라 성과 항목은 벤더 주장으로 남는다. | ref-926, ref-924, ref-922, ref-935, ref-923, ref-927, ref-930, ref-928, ref-938, ref-925, ref-936 | 아니오 | low | 2026-09-29 | 제조 공장 | — |
| f24 | [추정] | 확인한 자료를 종합하면 62. 제조 공장에서 ROP 가 직접 맡을 범위는 생산 관리·자재 관리 시스템(MES 등, ISA-95 의 3계층)이 내는 운송·공정 작업 요청을 받아 VDA 5050 같은 표준 인터페이스로 제조사가 다른 AGV·견인차·AMR·모바일 매니퓰레이터에 배정하고(f6·f20) 셀·라인 사이의 교통과 순서를 조율하며 도착·하역·조립 완료를 확인해 결과를 생산 시스템으로 돌려주는 일(f4·f5)이고, 라인 정지·결품 같은 예외를 받아 재계획하는 것(f3)까지가 경계 안이며, 이를 하나의 계층에서 묶은 국내 공개 사례는 확인되지 않았다. | ref-923, ref-924, ref-257, ref-925, ref-926, ref-936 | 아니오 | low | 2026-09-29 | 제조 공장 | — |
| f25 | [추정] | 연계 대상: 제조 공장에서 생산 계획·재고·칸반 규칙을 정하는 MES·ERP 는 분류 원문 19장의 상위 업무 시스템, 컨베이어·스태커 크레인·PLC 설비 제어와 무인 운반차의 사람 감지·제동 같은 안전 기능은 시설·설비 제어와 로봇 자체 지능·제어, 협동로봇의 힘 제한·충돌 회피와 로봇팔의 조립 동작은 로봇 자체 지능·제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 생산 계획 판단·설비 제어·안전 기능 성능은 MES 업체·설비 업체·로봇 제조사에 맡겨야 할 것으로 보인다. | ref-926, ref-936, ref-938, ref-928, ref-934 | 아니오 | low | 2026-09-29 | 제조 공장 | — |
| f26 | [추정] | 이 영역은 생산 관리 시스템과의 연결을 다루는 23. 업무 시스템 연동(f4·f5), VDA 5050 을 다루는 21. 상호운용 표준·적합성(f6·f20), 조립라인 공급 정책과 견인차·AGV 스케줄링을 다루는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링(f1·f2), 셀·다중 로봇 조립의 동기화를 다루는 30. 로봇 간 협업·물리적 인계(f13), 협동로봇과 셀 작업자를 다루는 31. 사람–로봇 협업·49. 사람 근접 안전(f12·f14), ISO 3691-4 를 다루는 50. 안전 표준·인증·사고 조사(f15), 결품·막힘과 라인 정지 대응을 다루는 32. 예외 복구·재계획·업무 연속성(f3), AGV 대수·통합창고 시뮬레이션과 디지털 트윈 메타 팩토리를 다루는 34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계(f2·f3·f11·f17), 자연어 로봇 제어 연구를 다루는 12. 채팅으로 업무 지시·오케스트레이션·44. 로봇 기반 모델·언어 모델 계획(f16), 시장 동향을 다루는 1. 기술·시장·업체 동향(f19)에 이어진다. | ref-925, ref-926, ref-923, ref-257, ref-922, ref-935, ref-934, ref-933, ref-928, ref-938, ref-936, ref-930, ref-931, ref-932 | 아니오 | low | 2026-09-29 | — | — |
| f27 | [추정] | oq-142 에 대해 국내 제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례는 이번 조사에서도 확인되지 않았으며, 확인된 국내 자료는 자연어로 로봇 한 대를 제어하는 KETI 의 전시 시연(f16)과 자연어 지시가 언급되지 않은 정부 'AI 공장장' 시범사업(f17)뿐이다. | ref-932, ref-931 | 아니오 | low | 2026-09-29 | 제조 공장 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-922 | Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)) | A classification of tactical assembly line feeding problems | 2019-02-23 | 논문 | medium | 2026-09-29 | https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957 | 아니오 |
| ref-923 | Verband der Automobilindustrie (VDA) | VDA 5050: Managing Transport in Manufacturing Plants | 미확인 | 표준 | medium | 2026-09-29 | https://www.vda.de/en/news/articles/vda-5050 | 아니오 |
| ref-924 | SYNAOS (IoT Use Case) | VDA 5050: unified AGV fleet control in real time at VW | 2025-10-16 | 벤더 문서 | low | 2026-09-29 | https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control | 아니오 |
| ref-925 | Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M. | Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL | 2019-11-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1911.05481 | 아니오 |
| ref-926 | Siemens | AGV fleet management integration with intralogistics | 미확인 | 벤더 문서 | low | 2026-09-29 | https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/ | 아니오 |
| ref-927 | 물류신문 (이경성) | LG전자, 스마트팩토리 솔루션 확대에 AMR 등 물류로봇 적극 활용한다 | 2024-07-18 | 기사 | medium | 2026-09-29 | https://www.klnews.co.kr/news/articleView.html?idxno=313143 | 아니오 |
| ref-928 | Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI) | Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors | 2024-12-02 | 논문 | high | 2026-09-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full | 아니오 |
| ref-929 | 장형준, 이연주 (건국대학교, 오모로봇; 전기의 세계 67(8)) | 물류 로봇(AGV) 동향 | 2018 | 논문 | medium | 2026-09-29 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201824236535732 | 아니오 |
| ref-930 | 현대자동차그룹 | ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다 | 2023-11-21 | 벤더 문서 | low | 2026-09-29 | https://www.hyundaimotorgroup.com/ko/news/hmgics-human-centric-mobility-solutions-new-era | 아니오 |
| ref-931 | 뉴시스 | "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 | 2026-09-07 | 기사 | medium | 2026-09-29 | https://www.newsis.com/view/NISX20260907_0003779780 | 아니오 |
| ref-932 | 테크데일리 | KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개 | 2025-03-12 | 기사 | medium | 2026-09-29 | https://www.techdaily.co.kr/news/articleView.html?idxno=25352 | 아니오 |
| ref-933 | Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35) | Collaborative robots in manufacturing and assembly systems: literature review and future research agenda | 2023-05-30 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10845-023-02137-w | 아니오 |
| ref-934 | Marvel, J. A., Bostelman, R., & Falco, J. (NIST; ACM Computing Surveys 51) | Multi-Robot Assembly Strategies and Metrics | 2018-01-01 | 논문 | medium | 2026-09-29 | https://dl.acm.org/doi/10.1145/3150225 | 아니오 |
| ref-935 | 강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce) | 시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례 | 2014 | 논문 | medium | 2026-09-29 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280 | 아니오 |
| ref-936 | 옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2)) | 자동차 생산을 위한 통합창고 연구 | 2012 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601 | 아니오 |
| ref-937 | 현대자동차 | From Root to Route: 싱가포르에 심은 혁신의 씨앗. 현대차그룹 싱가포르 글로벌 혁신센터(HMGICS) 공개 | 2023-11-21 | 벤더 문서 | low | 2026-09-29 | https://www.hyundai.com/worldwide/ko/brand-journal/mobility-solution/unveiling-hmgics-singapore | 아니오 |
| ref-938 | Applus+ Laboratories | ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) | 미확인 | 벤더 문서 | medium | 2026-09-29 | https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs | 아니오 |
| ref-257 | Interact Analysis (Rueben Scriven) | AMR Multi-Fleet Orchestration Software Explained | 2023-01 | 업계 보고서 | medium | 2026-09-29 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 예 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/manufacturing-plant.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1(대량 맞춤화가 라인 공급 관심을 키움), f20(자동차 공장이 이기종 플릿 관제의 대표 현장), f17(정부가 중소 제조 현장 로봇 배치를 사업화) / 섹션 4: f1(조립라인 공급 문제·공급 정책), f8(인플랜트 밀크런·JIS 공급, 벤더 주장), f11(셀 생산 방식, 벤더 주장), f13(치구 없는 다중 로봇 조립) / 섹션 5(현장 유형 모두 제조 공장): 라인 공급 — f8(VW 하노버, 벤더 주장), f7(BMW, 벤더 주장), 공정 간 운반 — f2·f3(국내 자동차 공장 시뮬레이션 연구), 여러 로봇 공정 작업 — f9·f10(LG전자, 성과는 벤더 주장), f11(현대차그룹 HMGICS, 벤더 주장), f14(차량 조립 협동로봇), 정부 시범 — f17, 여섯 항목 정리는 f23 / 섹션 6: 세 형태 지도 f22, 라인 공급·스케줄링 f1·f2, 생산 관리 연동 f4·f5, 다중 로봇 조립·협동로봇 f12·f13·f14, 자연어 제어 연구 f16(교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 함께) / 섹션 7: f6·f20(VDA 5050), f4(ISA-95 기반 모델), f15(ISO 3691-4, 인증 기관 설명이며 원문 미열람), f21(Open-RMF, ref-004 재사용) / 섹션 8: f1·f12·f13(서베이 3편), f14(전문가 연구), f4(ISA-95·PDDL), 국내 f2·f3·f18 / 섹션 9: f24(직접 범위: 생산 관리 요청 수신·표준 인터페이스 배정·교통·순서 조율·완료 확인·결과 반환·예외 재계획), f25(연계 대상: MES·ERP 생산 계획, 컨베이어·스태커 크레인·PLC, 무인 운반차 안전 기능, 협동로봇·로봇팔 동작) / 섹션 10: f26 — 1. 기술·시장·업체 동향, 12. 채팅으로 업무 지시·오케스트레이션, 21. 상호운용 표준·적합성, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성, 34. 시뮬레이션·예측용 디지털 트윈, 35. 처리능력·규모·배치 설계, 44. 로봇 기반 모델·언어 모델 계획, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사 / 섹션 11: 기존 oq-142(f27, 미해결)와 open_questions_new 4건. f5·f7·f8·f10·f11·f15 는 벤더 주장 병기 필수. 다음 실행 후보: 23. 업무 시스템 연동 페이지에 f4·f5 반영, 21. 상호운용 표준·적합성 페이지에 f6·f20 반영, 50. 안전 표준·인증·사고 조사 페이지에 f15 반영(ISO 원문 확인 후), 31. 사람–로봇 협업 페이지에 f12·f14 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 조립라인 공급 문제 | Assembly Line Feeding Problem (ALFP) | 조립라인의 각 부품을 라인 적재·상자 공급·순서 공급·정치식 키팅·이동식 키팅 같은 공급 정책 가운데 어디에 배정할지 정하는 전술적 의사결정 문제로, 대량 맞춤화와 제품 다양성이 커지면서 연구가 늘었다. |
| 인플랜트 밀크런 | In-plant Milk Run | 공장 안 창고·슈퍼마켓에서 조립 스테이션까지 견인차나 AGV 가 정해진 순회 경로와 주기로 여러 부품을 한꺼번에 배달하는 순환 공급 방식으로, 출발 시각과 정차 스테이션·적재량을 정하는 스케줄링이 연구 대상이다. |
| 셀 생산 방식 | Cell-based Production | 컨베이어 라인 대신 작업자와 로봇이 함께 일하는 독립된 셀에서 여러 차종·제품을 동시에 생산하는 방식으로, 셀마다 부품을 운반 로봇이 공급해야 하므로 라인 공급과 다중 로봇 조율이 결합된다. |

## 열린 질문

새로 생긴 질문:

- 국내 제조 공장에서 서로 다른 제조사의 AGV·AMR·모바일 매니퓰레이터를 VDA 5050 같은 표준 인터페이스로 하나의 관제 계층 아래 운영한 공개 사례가 있는가(확인된 국내 사례는 자체 로봇 도입과 정부 시범사업뿐이다)? | 관련 영역: 62. 제조 공장, 21. 상호운용 표준·적합성 | 근거: f24 | 종류: 일반
- 생산 관리 시스템(MES)이 로봇 플릿에 내는 운송·공정 작업 요청과 완료 보고에 ISA-95 의 작업 요청·작업 응답 모델을 실제로 쓴 공개 사례나 표준 매핑이 있는가? | 관련 영역: 62. 제조 공장, 23. 업무 시스템 연동 | 근거: f4 | 종류: 일반
- 셀 생산 방식에서 여러 셀이 동시에 같은 부품을 요청할 때 운반 로봇 배정과 셀 안 로봇팔·작업자의 조립 순서를 어떤 계층이 조율하며 라인 정지·결품 시 재계획 책임은 어디에 있는가? | 관련 영역: 62. 제조 공장, 32. 예외 복구·재계획·업무 연속성 | 근거: f22 | 종류: 일반
- ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가(이번 조사는 인증 기관 설명만 확인했다)? | 관련 영역: 62. 제조 공장, 50. 안전 표준·인증·사고 조사 | 근거: f15 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 1
- 예산 사용량: 검색 12회 · 신규 출처 17건
- 미확인 항목:
    - f20 외 모든 finding 교차 확인 실패(서베이·기사·회사 설명마다 발행 주체 한 곳)
    - f11 의 두 출처(현대차그룹 뉴스, 현대차 브랜드 저널)는 같은 회사 발행이라 독립 교차 확인이 아님
    - f1 Schmid·Limère 서베이와 f12 Keshvarparast 외 서베이, f13 Marvel 외 서베이는 출판사 페이지가 403·로그인 리다이렉트라 Semantic Scholar API 의 서지·초록만 확인
    - f15 ISO 3691-4:2023 은 ISO 페이지(iso.org/standard/83545.html)와 Pilz 해설이 403 이라 Applus+ 인증 기관 안내로만 확인해 벤더 주장·추정으로 둠
    - f5 지멘스 백서, f6 VDA 소개 글, f15 Applus+ 페이지 발행일 미확인
    - f8 SYNAOS 의 VW 하노버 수치(135대·일 9,000 랙·연 30만 km)와 f7 BMW 적용 범위는 회사 설명이며 독립 출처 없음
    - f9·f10 LG전자 사례는 기사 한 건이며 창원 공장 성과 수치는 회사 설명
    - Emde 외 자동차 조립라인 견인차 스케줄링 논문(EJOR 2017)은 ScienceDirect 403·Semantic Scholar 검색 429 로 열지 못해 출처 제외 — 밀크런 스케줄링의 학술 근거 후보
    - oq-142 미해결: 국내 제조 공장의 다중 로봇 대화 지시·승인 운영 사례 미확인(f27)
    - ref-257·ref-004 재사용 항목은 참고문헌 목록 입력이 0건이라 등록된 기관·제목·URL 과 글자 단위로 대조하지 못함
    - ref-923 VDA 소개 글은 표준 발행 기관의 페이지지만 표준 본문이 아니므로 신뢰도 medium 으로 둠
- 범위 경계 위반 의심:
    - f25: MES·ERP 의 생산 계획 판단, 컨베이어·스태커 크레인·PLC 설비 제어, 무인 운반차의 사람 감지·제동 안전 기능, 협동로봇·로봇팔의 동작 제어는 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어 쪽이므로 '연계 대상: '으로 표시함
    - f1·f2: 조립라인 공급 정책과 AGV 대수·경로 산정은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·35. 처리능력·규모·배치 설계 의 방법 영역과 겹치므로 이 영역에서는 제조 공장의 라인 공급 근거로만 제안함
    - f12·f13·f14: 협동로봇·다중 로봇 조립의 동기화·안전은 30. 로봇 간 협업·물리적 인계·31. 사람–로봇 협업·49. 사람 근접 안전 의 핵심이므로 이 영역에서는 공정 작업 형태와 제약의 근거로만 제안함
    - f16: 자연어 로봇 제어는 L. AI·학습 기술의 방법이므로 12. 채팅으로 업무 지시·오케스트레이션과 44. 로봇 기반 모델·언어 모델 계획에 함께 연결하도록 제안함
    - f15: ISO 3691-4 는 50. 안전 표준·인증·사고 조사 와 겹치므로 이 영역에서는 무인 운반차 운영 제약의 근거로만 제안함
- 한계: 재실행 1회차. 반려 사유 1(f4: 벤더 문서만 근거로 한 사실 태그에 vendor_claim 없음): 직전 반환값(runs/2026-09-29-12/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로 예산 안에서 브리프를 다시 작성했고, 벤더 문서(지멘스 ref-926, SYNAOS ref-924, 현대차그룹 ref-930·ref-937, Applus+ ref-938)만 근거로 한 finding 과 VDA 글·기사에 실린 기업 성능·적용 주장은 모두 vendor_claim true·태그 추정·신뢰도 low·evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다(관련 finding: f5, f7, f8, f10, f11, f15). 이번 브리프의 finding 번호는 직전 반환값과 대응하지 않는다. web_fetch_available: true · fetch_mode full. 검색 12회/30, 신규 출처 17건은 예약 구간 ref-922~ref-938 안이나 max_sources_per_run 15 를 2건 넘겼다 — ref-937(현대차 브랜드 저널, f11 보조)과 ref-929(국내 AGV 동향 논문, f18)를 퍼블리셔가 상한 초과분으로 제외해도 다른 finding 에는 영향이 없도록 두 출처는 각각 f11 의 보조 근거와 f18 단독 근거로만 썼다. 출처 상한으로 Emde 외 EJOR 2017 견인차 스케줄링 논문(열지 못함), Emerald 밀크런 견인차 스케줄링 논문, 삼일PwC Physical AI 이슈 브리프(2026-03), 인더스트리뉴스·현대차그룹 AGV·AMR 해설, 세방리튬배터리 광주 공장 AMR–MES 연동(이앤에스글로벌 벤더 블로그), 한국자동차산업협동조합 기고문은 넣지 못했다. 원문 열람 17건(모두 webfetch: Semantic Scholar API 초록 3(ref-922·ref-933·ref-934), arXiv 초록 1, KCI·DBpia·KISTI 초록 3, VDA·SYNAOS·지멘스·현대차그룹 2·Applus+ 페이지 6, 물류신문·뉴시스·테크데일리 기사 3, Frontiers 원문 1), 재사용 미열람 2건(ref-257·ref-004 는 이번에 다시 열지 않아 fetched false·source_unopened true). 주의: 같은 날 이전 실행 2026-09-29-11 이 ref-923·ref-924 를 다른 URL(CJ대한통운 보도자료, Robotics 24/7)에 부여했다고 그 브리프에 적혀 있으므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 하고, 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 VDA 5050·ISO 3691-4·Open-RMF 관련 페이지가 전체 921건과 URL 이 겹칠 수 있다(용어집에 '운용 구역 (ISO 3691-4)'·'VDA 5050' 이 이미 있어 기존 출처가 있을 가능성이 높다). 교차 확인 1건(f20: VDA/Interact Analysis/SYNAOS 의 독일 완성차 VDA 5050 채택 — 채택 사실만, 수치 제외). 신뢰도 high 는 f14 한 건(Frontiers 오픈 액세스 원문 열람이나 단일 출처이므로 검증에서 medium 으로 낮아질 수 있음). 분류 원문 핵심 질문(여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가)에는 세 형태 지도 f22, 여섯 항목 정리 f23, 직접 범위 f24 로 답했으며 결론은 '생산 관리·자재 관리 시스템이 내는 운송·공정 작업 요청을 표준 인터페이스(VDA 5050)로 이기종 플릿에 배정하고 완료를 생산 시스템에 돌려주는 계층이 필요하며, 독일 완성차 공장은 이를 VDA 5050 으로 구현했으나 국내 공개 사례는 자체 로봇 도입·정부 시범 수준'이라는 추정이다. 현장 유형: 모두 제조 공장(국내 LG전자 창원·현대차그룹 HMGICS·정부 AI 공장장·KETI 시연·자동차 공장 시뮬레이션 연구, 해외 BMW·VW 하노버, 학술 서베이)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다(f14 의 창고·농업 사례는 제외). 국내 자료는 부산대 논문(f2)·고려대·현대차 논문(f3)·전기의 세계 동향(f18)·물류신문 LG전자(f9·f10)·현대차그룹(f11)·뉴시스 정부 사업(f17)·테크데일리 KETI(f16) 일곱 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다(사전 시뮬레이션·메타 팩토리는 34 쪽으로만 연결). 용어집에 이미 있는 ISA-95·VDA 5050·플러그 앤 프로듀스·협동 적용·운용 구역·종합설비효율·모바일 매니퓰레이터·디지털 트윈·플릿 관리 시스템은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-142 는 조사 질문에 넣고 검색 1회를 배분했으나 미해결로 남긴다(f27). 해결된 열린 질문 없음.
```

### runs/2026-09-29-11/research.md

```markdown
# 리서치 브리프 2026-09-29-11

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-11 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 61. 물류창고 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 상품-대-사람(GTP)·셔틀 기반 저장·회수 시스템·AMR 협업 피킹·스마트물류센터 인증 용어 없음(로봇 이동형 풀필먼트 시스템·주문 배치·풋월·웨이브리스 출고 지시·창고 실행·창고 제어·창고 관리 시스템은 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 입고(하역)·적치·보충·피킹·포장·출하·반품 단계별 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 로봇 이동형 풀필먼트·셔틀·AMR 협업 피킹·트레일러 하역·소팅 로봇, 다중 에이전트 픽업·배송(MAPD)·지속형 MAPF 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 국토교통부 스마트물류센터 인증 심사기준, GS1 EPCIS, Open-RMF, RAWSim-O 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 로봇화 창고 서베이, 전자상거래 창고 서베이, AMR 계획·제어 서베이, 국내 논문 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 17. 작업 대상·자산 식별과 인계 추적, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 27. 다중 로봇 경로·교통 관리 — MAPF, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-134·oq-138·oq-142·oq-146 미반영, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
2. 입고(하역·검수)·적치·보관·보충·피킹·포장·출하·반품 각 단계에 어떤 로봇 시스템(트레일러 하역 로봇, 로봇 이동형 풀필먼트 시스템, 셔틀, AMR 협업 피킹, 소팅 로봇, 무인지게차)이 들어가며, 학술 서베이는 이를 어떻게 분류하는가? (섹션 4·6·8 겨냥)
3. 단계별 로봇 작업의 시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과는 실제 도입 사례(국내 쿠팡·CJ대한통운, 해외 DHL·Amazon)에서 어떻게 나타나는가? (섹션 5 겨냥, 현장 유형 물류창고 명시, 한국 자료 우선)
4. 물류창고 로봇 운영의 계획·제어 문제(온라인 픽업·배송 작업 배정, 대규모 경로 계획, 보충 최적화, 반품 재적치 통합)는 어떤 연구가 다루며 오픈소스 시뮬레이터가 있는가? (섹션 6·7·8 겨냥)
5. 국내 규제·인증(국토교통부 스마트물류센터 인증 심사기준)은 물류처리 과정별 자동화와 정보시스템(WMS·WCS)을 어떻게 평가하며, 이것이 ROP 의 위치를 어떻게 규정하는가? (섹션 7·9 겨냥)
6. 물류창고에서 ROP 가 직접 맡을 것(흐름 단계별 작업 요청의 수신·배정·인계 확인·결과 반환)과 WMS·소터·컨베이어 PLC·로봇 파지 인식에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)
7. oq-134·oq-138·oq-142·oq-146: 국내 물류창고에서 운영 기록의 시뮬레이션 재현, 대화로 시나리오 구성·업무 지시, 소음 조건 음성 지시 인식률을 보고한 자료가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Azadeh·de Koster·Roy(Transportation Science 53(4), 2019)의 서베이는 배송센터에 로봇 취급 시스템이 늘어나는 이유로 작은 공간·수요 변동 대응 유연성·24시간 가동을 들고, 셔틀 기반 저장·회수 시스템, 셔틀 기반 압축 저장 시스템, 로봇 이동형 풀필먼트 시스템(RMFS)을 새 범주로 검토하며 문헌을 시스템 분석·설계 최적화·운영 계획·제어의 세 갈래로 나누고, 통합 로봇 창고에서는 레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정 같은 설계·계획·제어 논리를 다시 세워야 한다고 결론짓는다. | ref-910 | 아니오 | medium | 2019-06-28 | 물류창고 | — |
| f2 | [사실] | Boysen·Weidinger·de Koster(European Journal of Operational Research 277(2), 2019)의 전자상거래 창고 서베이는 소량·소수 라인의 시간 민감 피킹 주문이 대량으로 발생하는 조건에서 전통적 피커-대-상품 창고가 부족해 자동 피킹 워크스테이션·로봇·AGV 지원 피킹 같은 자동화 시스템과 혼합 선반 저장·동적 주문 처리·배치·존 분할·분류 시스템 같은 조직적 적응이 채택된다고 정리해, 물류창고 로봇 작업의 시작 조건이 전자상거래 주문 특성임을 보인다. | ref-382 | 아니오 | medium | 2019 | 물류창고 / 시작 조건 | — |
| f3 | [사실] | Fragapane·de Koster·Sgarbossa·Strandhagen(European Journal of Operational Research 294(2), 2021)의 문헌 검토는 자율이동로봇(AMR)이 중앙 장치가 스케줄링·라우팅·배차를 모두 맡는 AGV 시스템과 달리 다른 자원과 독립적으로 통신·협상해 의사결정을 분산할 수 있다고 보고, 제조·창고·크로스독·터미널·병원을 적용 분야로 들며 관리자를 위한 AMR 계획·제어 프레임워크와 연구 의제를 제시한다. | ref-911 | 아니오 | medium | 2021 | 수행 자원 | — |
| f4 | [사실] | Ma·Li·Kumar·Koenig(AAMAS 2017)의 다중 에이전트 픽업·배송(MAPD) 문제는 자동화 창고에서 에이전트가 온라인으로 도착하는 배송 작업 스트림을 픽업 위치와 배송 위치로 충돌 없이 이동하며 계속 처리하는 지속형 경로 계획 문제이며, 토큰 전달(TP)과 작업 교환 토큰 전달(TPTS) 알고리즘으로 수백 대의 에이전트·작업을 다룬다. | ref-006 | 아니오 | medium | 2017-05-30 | 물류창고 | — |
| f5 | [사실] | Li·Tinka·Kiesel·Durham·Kumar·Koenig(AAAI 2021)의 롤링 호라이즌 충돌 해결(RHCR)은 지속형 다중 에이전트 경로 찾기를 시간창 단위의 순차 문제로 나눠 시뮬레이션 창고에서 최대 1,000대(지도 빈 칸의 38.9%)의 에이전트에 대해 높은 품질의 해를 내어, 대규모 물류창고 로봇 교통 관리의 규모 기준을 제공한다. | ref-005 | 아니오 | medium | 2021-03-12 | 물류창고 | — |
| f6 | [사실] | RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS)의 의사결정 문제를 연구하기 위한 이산 사건 시뮬레이션 프레임워크로 GNU GPL v3 이상으로 공개돼 있으며, 2D·3D 시각화, 다층 창고 시뮬레이션, 경로 계획 시각화, 로봇 이동 히트맵 기능을 갖추고 새 의사결정 방법을 컨트롤러로 확장할 수 있게 하며, 대표 논문은 Logistics Research 11(1)(2018)이다. | ref-101 | 아니오 | medium | 2026-09-29 | 물류창고 | — |
| f7 | [사실] | Schrotenboer·Wruck·Vis·Roodbergen(arXiv, 2019)은 전자상거래 창고에서 반품 상품의 재적치를 일반 주문 피커의 경로에 통합하면 비용이 10~15% 절감되고, 고객 주문을 여러 배치로 분해하는 것까지 허용하면 절감이 44%에 이른다고 보고해, 반품 단계가 피킹 단계와 함께 최적화될 수 있음을 보였다(피커 기반 창고의 최적화 연구이며 로봇 피킹 적용은 아니다). | ref-913 | 아니오 | medium | 2019-09-01 | 물류창고 / 예외·성과 | — |
| f8 | [사실] | 곽경민·박범·고은지·윤철주·김경훈(CJ대한통운, 로봇학회 논문지 17(4), 2022)은 물류 현장의 로봇 적용을 계약물류·소포·풀필먼트의 차이에 따라 논의하며 적용 유형으로 로봇 낱개 피킹(piece picking), 로봇 박스 취급(디팔레타이징), AGV·AMR 이송, 자동창고(ASRS), 로봇 웨어러블 장치를 들어, 국내 물류창고의 흐름 단계별 로봇 작업 유형을 정리한 국내 문헌이다. | ref-915 | 아니오 | medium | 2022 | 물류창고 / 수행 자원 | — |
| f9 | [사실] | 김태현·송상화(인천대학교, 한국디지털산업학회지 26(1), 2021)는 온라인 주문 풀필먼트 센터의 오더피킹 설비에서 재고 보충을 최적화하는 혼합정수계획 모형을 개발해 실제 운영 프로세스·데이터와 시뮬레이션으로 효과를 검증했으며, 이는 물류창고 보충 단계를 다룬 국내 연구다. | ref-916 | 아니오 | medium | 2021 | 물류창고 | — |
| f10 | [추정] | 로봇신문(2022-05-06)이 전한 CJ대한통운의 설명에 따르면 자사 물류 자동화 기술 3종 가운데 QPS 는 피킹·이송·분류 컨베이어를 분리해 시간당 최대 2,000건을 처리하며 기존 DPS 대비 생산성 48% 증가, 지능형 스캐너(ITS)는 시간당 약 7,000건 인식으로 검수 시간 35% 이상 단축, AMR 은 12시간 배터리·50kg 적재·최대 7.2km/h 로 AMR 기반 오더피킹에서 작업자 1명이 시간당 120 오더라인을 처리한다. | ref-917 | 아니오 | low | 2022-05-06 | 물류창고 / 예외·성과 | 벤더 주장 |
| f11 | [사실] | 로봇신문(2023-02-07)에 따르면 쿠팡 대구 풀필먼트센터는 바닥 QR 코드를 따라 최대 1,000kg 의 선반을 작업자에게 2분 안에 가져오는 AGV 1,000대 이상, 포장 라벨 바코드를 읽어 목적지별로 분류·이송하는 소팅봇 수백 대, 버튼 한 번으로 대용량 제품을 옮기며 사람 출입을 막은 구역에서만 움직이는 무인지게차 수십 대를 갖추고 사람-대-상품(PTG)에서 상품-대-사람(GTP) 방식으로 전환했으며 투자액은 3,200억 원 이상이다. | ref-919 | 아니오 | medium | 2023-02-07 | 물류창고 / 수행 자원 | — |
| f12 | [사실] | 서로 다른 두 전문지(로봇신문, 물류신문)가 2023-02-07 쿠팡 대구 풀필먼트센터 현장 공개를 각각 보도하며 7층의 AGV 1,000대 이상(최대 1,000kg 선반 운반), 1층의 소팅봇 수백 대(8kg 이하 상품 분류), 5층의 무인지게차(작업자 구역과 분리, 경계 침범 시 안전 센서로 정지)를 같은 내용으로 전해, 국내 물류창고에서 적치·피킹(AGV 선반 운반), 출하 분류(소팅봇), 대용량 운반(무인지게차)에 서로 다른 로봇이 층별로 나뉘어 투입된 사례가 확인된다. | ref-919, ref-920 | 예 | medium | 2023-02-07 | 물류창고 / 제약 | — |
| f13 | [추정] | 쿠팡은 대구 풀필먼트센터의 AGV 가 연중 24시간 가동되고 필요 시 자동 충전하며 이를 통해 전체 업무 단계를 65% 줄였다고 설명했다. | ref-919, ref-920 | 아니오 | low | 2023-02-07 | 물류창고 / 예외·성과 | 벤더 주장 |
| f14 | [사실] | Robotics 24/7(2023-02-01)에 따르면 DHL Supply Chain 은 Boston Dynamics 의 Stretch 로봇을 트레일러·컨테이너 하역에 상업 배치한 첫 회사로, 로봇이 트레일러 뒤쪽에서 상자를 집어 유연 컨베이어에 올리며 DHL 은 1년 전 Boston Dynamics 로봇에 1,500만 달러를 투자했고 이후 여러 창고로 확대하고 하역 외 작업으로 넓힐 계획이라고 보도됐다. | ref-924 | 아니오 | medium | 2023-02-01 | 물류창고 / 수행 자원 | — |
| f15 | [추정] | DHL 과 Boston Dynamics 는 Stretch 의 하역 속도가 시험한 모든 환경에서 수작업을 넘어섰다고 밝히고, 향후 개선 목표로 사람 개입 감소와 떨어진 상자의 자동 복구 개선을 들었다. | ref-924 | 아니오 | low | 2023-02-01 | 물류창고 / 예외·성과 | 벤더 주장 |
| f16 | [추정] | Amazon 은 2025년 7월 발표에서 100만 번째 로봇을 일본의 풀필먼트센터에 배치해 300개 이상 시설에 로봇 100만 대를 운용하며, 최대 1,250파운드의 재고를 옮기는 Hercules, 정밀 컨베이어로 개별 패키지를 다루는 Pegasus, 직원 주변을 안전하게 주행하며 주문 카트를 옮기는 자율 로봇 Proteus 를 예로 들고, 플릿 이동을 조율하는 생성형 AI 기반 모델 DeepFleet 을 도입했다고 밝혔다. | ref-918 | 아니오 | low | 2025-07 | 물류창고 / 수행 자원 | 벤더 주장 |
| f17 | [추정] | Amazon 은 DeepFleet 이 풀필먼트 네트워크 전체에서 로봇 플릿의 이동 시간을 10% 개선한다고 주장한다. | ref-918 | 아니오 | low | 2025-07 | 물류창고 / 예외·성과 | 벤더 주장 |
| f18 | [사실] | 스마트물류시설인증센터(한국교통연구원 운영)의 스마트물류센터 인증 심사기준(일반)은 기능영역 600점을 하차·입고(입고예정정보 확인, 하역작업, 상품검수, 제품정보 인식·등록), 운반·적치(작업정보 제공, 적치장소 이동, 경로관리, 장소식별), 보관·재고관리(재고조사, 보충정보 생성, 위치조정, 모니터링, 품질관리), 피킹·분류(작업정보 생성, 확인방법, 실시간 경로관리, 분류작업), 검품·검수·포장, 상차·출고(발주처별 분류, 차량입차, 상차순서관리, 출고정보전달)의 6개 프로세스 각 100점으로 나누고, 기반영역 400점을 구조적 성능 100점·성과관리 100점·정보시스템 200점(WMS 150점, WCS/MCS 50점)으로 두며 우수물류신기술 적용 가산점은 최대 50점이다. | ref-921 | 아니오 | medium | 2026-09-29 | 물류창고 / 완료·인계 | — |
| f19 | [사실] | 국토교통부의 스마트물류센터 인증제는 물류시설의 개발 및 운영에 관한 법률 제21조의4에 근거해 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하고, 인증을 받으면 건축·설비 구입 비용을 저리로 융자받고 정부가 최대 2%p 의 이자 비용을 지원하며 용적률·높이 제한 완화 혜택을 받는다(2020-10-08 법 개정, 2021-01-01 시행). | ref-124, ref-921 | 예 | high | 2026-09-29 | 물류창고 / 제약 | — |
| f20 | [추정] | CJ대한통운은 2023-10-26 보도자료에서 안성 MP허브터미널(연면적 12,000㎡)이 국토교통부 스마트물류센터 1등급 인증을 받았고 크로스벨트 소터, 컨베이어 센서로 화물을 분산하는 로드 밸런싱, 120개 이상 도크의 차량 배정을 맡는 AI 기반 도크 관리 시스템(DMS)과 오류 자동 복구 기술로 하루 200만 건의 소형 상품을 처리하며 이것이 자사의 9번째 1등급 인증이라고 밝혔다. | ref-923 | 아니오 | low | 2023-10-26 | 물류창고 / 완료·인계 | 벤더 주장 |
| f21 | [사실] | GS1 EPCIS 는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준으로, 물류창고 입고·출하 단계의 완료·인계 기록(무엇이 어디서 누구에게 넘어갔는가)을 로봇 작업 결과와 함께 남기는 데 쓸 수 있는 후보 형식이다. | ref-003 | 아니오 | medium | 2026-09-29 | 완료·인계 | 원문 미열람 |
| f22 | [사실] | Interact Analysis(2023-01)는 다중 플릿 오케스트레이션 소프트웨어를 서로 다른 제조사의 AMR 플릿 여럿을 하나의 창고 시스템 안에서 관리하는 소프트웨어로 정의하고, 로봇을 직접 통합하는 저수준 제어와 제조사 플릿 매니저를 관리하는 고수준 제어로 접근을 나누며 상호운용은 표준 또는 미들웨어로 푼다고 정리해, 물류창고를 이 소프트웨어 범주의 기본 현장으로 놓는다. | ref-257 | 아니오 | medium | 2023-01 | 물류창고 / 수행 자원 | 원문 미열람 |
| f23 | [추정] | Open-RMF 는 플릿 어댑터로 서로 다른 제조사의 로봇 플릿을 붙이고 작업·교통 조율과 문·승강기 같은 설비 연동을 제공하는 오픈소스 미들웨어로, 물류창고의 AGV·AMR·소팅 로봇처럼 제조사가 다른 플릿을 하나의 오케스트레이션 계층으로 묶는 참고 구조가 될 것으로 보인다. | ref-004 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f24 | [추정] | 확인한 자료를 종합하면 물류창고의 로봇 작업은 흐름 단계마다 다른 형태로 들어간다: 입고 단계는 트레일러 하역 로봇(f14)과 고속 검수 스캐너(f10), 적치·보관·피킹 단계는 선반(pod)을 작업자에게 가져오는 로봇 이동형 풀필먼트 시스템과 셔틀·압축 저장 시스템(f1·f11·f12), 사람과 함께 걷는 AMR 협업 피킹과 로봇 낱개 피킹(f2·f8·f10), 보충 단계는 보충 정보 생성과 보충 최적화(f9·f18), 출하 단계는 소팅봇·크로스벨트 소터·도크 배정(f12·f20), 반품 단계는 재적치를 피킹 경로에 통합하는 최적화(f7)로 나타나며, 무인지게차는 대용량 운반을 사람 출입이 막힌 구역에서 맡는다(f12). | ref-910, ref-382, ref-913, ref-915, ref-916, ref-917, ref-919, ref-920, ref-921, ref-923, ref-924 | 아니오 | low | 2026-09-29 | 물류창고 | — |
| f25 | [추정] | 확인한 자료를 종합하면 물류창고 로봇 작업의 여섯 항목은 시작 조건이 전자상거래 주문(f2)과 입고예정정보(f18), 작업 대상이 선반(pod)·토트·박스·팔레트·반품 상품(f7·f11·f14), 수행 자원이 AGV·AMR·소팅봇·무인지게차·하역 로봇과 상품-대-사람 스테이션의 작업자(f11·f12·f14), 제약이 적재 한계(선반 1,000kg, 소팅봇 8kg 이하, AMR 50kg)·배터리·사람 출입이 막힌 무인지게차 구역(f10·f12·f13), 완료·인계가 바코드 인식·검수·출고정보 전달과 인계 이벤트 기록(f18·f21), 예외·성과가 떨어진 상자 복구와 처리량·오더라인 지표(f10·f15·f17)로 채워질 수 있으나, 각 사례의 수치는 회사 설명이라 성과 항목은 벤더 주장으로 남는다. | ref-382, ref-913, ref-917, ref-919, ref-920, ref-921, ref-924, ref-003, ref-918 | 아니오 | low | 2026-09-29 | 물류창고 | — |
| f26 | [추정] | 확인한 자료를 종합하면 61. 물류창고에서 ROP 가 직접 맡을 범위는 인증 심사기준의 정보시스템 계층(WMS 와 WCS/MCS, f18) 사이에서 흐름 단계별 작업 요청(입고예정·주문·보충·출고 정보)을 받아 제조사가 다른 AGV·AMR·소팅봇·무인지게차·하역 로봇에 배정하고(f4·f22·f23) 경로·교통을 조율하며(f5) 바코드 인식·인계 이벤트로 완료를 확인해 결과를 WMS 로 돌려주는 일이며, 다중 플릿 오케스트레이션 소프트웨어가 창고 제어 시스템에 비견된다는 시장 정의(f22)와 맞는 것으로 보인다. | ref-921, ref-257, ref-004, ref-006, ref-005, ref-003 | 아니오 | low | 2026-09-29 | 물류창고 | — |
| f27 | [추정] | 연계 대상: 물류창고에서 주문·재고·보충 규칙을 정하는 WMS 는 분류 원문 19장의 상위 업무 시스템, 크로스벨트 소터·컨베이어·로드 밸런싱과 도크 배정은 시설·설비 제어, 하역 로봇의 상자 인식·파지와 로봇 낱개 피킹의 비전·파지는 로봇 자체 지능·제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 재고 판단·설비 제어·파지 성능은 WMS·설비 업체·로봇 제조사에 맡겨야 할 것으로 보인다. | ref-921, ref-923, ref-924, ref-915 | 아니오 | low | 2026-09-29 | 물류창고 | — |
| f28 | [추정] | 이 영역은 작업 대상의 식별·인계 기록을 다루는 17. 작업 대상·자산 식별과 인계 추적(f21), 소터·컨베이어·도크 연동을 다루는 22. 설비·건물 시스템 연동(f20), WMS·WCS 연동을 다루는 23. 업무 시스템 연동(f18), 온라인 픽업·배송 작업 배정과 대규모 경로 계획을 다루는 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF(f4·f5), 로봇 밀도·처리능력 설계를 다루는 35. 처리능력·규모·배치 설계(f1·f6), 무인지게차 구역 분리와 사람 협업 피킹을 다루는 49. 사람 근접 안전·31. 사람–로봇 협업(f12·f2), 떨어진 상자 복구 같은 예외를 다루는 32. 예외 복구·재계획·업무 연속성(f15), 시장 동향을 다루는 1. 기술·시장·업체 동향(f16·f22)에 이어진다. | ref-003, ref-923, ref-921, ref-006, ref-005, ref-910, ref-101, ref-919, ref-382, ref-924, ref-918, ref-257 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-910 | Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)) | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019-06-28 | 논문 | medium | 2026-09-29 | https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873 | 아니오 |
| ref-911 | Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)) | Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda | 2021 | 논문 | medium | 2026-09-29 | https://doi.org/10.1016/j.ejor.2021.01.019 | 아니오 |
| ref-382 | Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)) | Warehousing in the e-commerce era: A survey | 2019 | 논문 | medium | 2026-09-29 | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ | 아니오 |
| ref-913 | Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J. | Integration of returns and decomposition of customer orders in e-commerce warehouses | 2019-09-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1909.01794 | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub 공식 저장소) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/merschformann/RAWSim-O | 아니오 |
| ref-915 | 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)) | 급속 확산되는 물류현장의 로봇적용 사례 | 2022 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267 | 아니오 |
| ref-916 | 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)) | 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구 | 2021 | 논문 | medium | 2026-09-29 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327 | 아니오 |
| ref-917 | 로봇신문 (장길수) | CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3' | 2022-05-06 | 기사 | low | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=28424 | 아니오 |
| ref-918 | Amazon | Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot | 2025-07 | 벤더 문서 | medium | 2026-09-29 | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model | 아니오 |
| ref-919 | 로봇신문 (장길수) | 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이... | 2023-02-07 | 기사 | medium | 2026-09-29 | https://www.irobotnews.com/news/articleView.html?idxno=30736 | 아니오 |
| ref-920 | 물류신문 (석한글) | ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니 | 2023-02-07 | 기사 | medium | 2026-09-29 | https://www.klnews.co.kr/news/articleView.html?idxno=306994 | 아니오 |
| ref-921 | 스마트물류시설인증센터 (한국교통연구원) | 인증스마트물류센터 : 인증심사 > 심사기준 > 일반 | 미확인 | 정부·연구기관 | high | 2026-09-29 | https://cslc.koti.re.kr/new_sub2/new_sub2_2_1 | 아니오 |
| ref-124 | 국토교통부 (국가물류통합정보센터) | 스마트물류센터 인증제 안내 | 미확인 | 정부·연구기관 | high | 2026-09-29 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 아니오 |
| ref-923 | CJ대한통운 | CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 | 2023-10-26 | 벤더 문서 | medium | 2026-09-29 | https://cjlogistics.com/ko/newsroom/news/NR_00001109 | 아니오 |
| ref-924 | Robotics 24/7 (Eugene Demaitre) | DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers | 2023-02-01 | 기사 | medium | 2026-09-29 | https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers | 아니오 |
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 미확인 | 표준 | medium | 2026-09-29 | https://ref.gs1.org/epcis/ | 예 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021) | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2021-03-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2005.07371 | 아니오 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017) | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017-05-30 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/1705.10868 | 아니오 |
| ref-257 | Interact Analysis (Rueben Scriven) | AMR Multi-Fleet Orchestration Software Explained | 2023-01 | 업계 보고서 | medium | 2026-09-29 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/warehouse.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1(로봇 취급 시스템이 늘고 설계·계획·제어 논리를 다시 세워야 함), f2(전자상거래 주문 특성이 시작 조건), f22(다중 플릿 오케스트레이션의 기본 현장이 창고) / 섹션 4: f2·f11(상품-대-사람·AMR 협업 피킹), f1(셔틀 기반 저장·회수·RMFS), f4(MAPD), f19(스마트물류센터 인증) / 섹션 5(현장 유형 모두 물류창고): 입고 — f14·f15(DHL 트레일러 하역, 성과는 벤더 주장), 적치·피킹·출하 — f11·f12·f13(쿠팡 대구: 층별 AGV·소팅봇·무인지게차, 65% 는 벤더 주장), 피킹·검수 — f10(CJ대한통운 QPS·ITS·AMR, 벤더 주장), 출하·도크 — f20(CJ대한통운 안성, 벤더 주장), 반품 — f7(반품 재적치 통합 연구, 로봇 적용 아님을 명시), 전체 — f16·f17(Amazon, 벤더 주장), 여섯 항목 정리는 f25 / 섹션 6: 흐름 단계별 로봇 작업 지도 f24, 계획·제어 f3·f4·f5·f9, 반품 f7, 국내 유형 분류 f8 / 섹션 7: f18·f19(국토교통부 스마트물류센터 인증 심사기준·법적 근거), f21(GS1 EPCIS, ref-003 재사용), f23(Open-RMF, ref-004 재사용), f6(RAWSim-O) / 섹션 8: f1·f2·f3(서베이 3편), f4·f5(MAPD·지속형 MAPF), f7(반품), f6(시뮬레이터), 국내 f8·f9 / 섹션 9: f26(직접 범위: WMS 와 WCS/MCS 사이에서 단계별 작업 요청 수신·이기종 플릿 배정·경로 조율·인계 확인·결과 반환), f27(연계 대상: WMS 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지) / 섹션 10: f28 — 1. 기술·시장·업체 동향, 17. 작업 대상·자산 식별과 인계 추적, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 25. 작업 배정 — MRTA, 27. 다중 로봇 경로·교통 관리 — MAPF, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전 / 섹션 11: 기존 oq-134·oq-138·oq-142·oq-146(이번 조사에서도 국내 물류창고 자료 미확인, 미해결)과 open_questions_new 4건. f10·f13·f15·f16·f17·f20 은 벤더 주장 병기 필수. 다음 실행 후보: 23. 업무 시스템 연동 페이지에 f18(WMS·WCS/MCS 배점) 반영, 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f4·f5 반영, 35. 처리능력·규모·배치 설계 페이지에 f6 반영, 49. 사람 근접 안전 페이지에 f12(무인지게차 구역 분리) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 상품-대-사람 | Goods-to-Person (GTP) | 로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비되며 로봇 이동형 풀필먼트 시스템이 대표 구현이다. |
| 셔틀 기반 저장·회수 시스템 | Shuttle-Based Storage and Retrieval System (SBS/RS) | 층마다 움직이는 셔틀 차량과 리프트로 토트·상자를 랙에 넣고 꺼내는 자동 창고 시스템으로, 로봇화 창고 서베이가 로봇 이동형 풀필먼트 시스템·셔틀 기반 압축 저장 시스템과 함께 새 범주로 검토한다. |
| AMR 협업 피킹 | AMR-assisted Order Picking | 자율이동로봇이 피킹 경로를 따라 작업자와 함께 움직이며 상품을 싣고 나르고 작업자는 집는 일만 맡는 방식으로, 기존 피커-대-상품 창고에 큰 개조 없이 도입할 수 있어 전자상거래 창고 서베이가 자동화 선택지의 하나로 든다. |
| 스마트물류센터 인증 | Smart Logistics Center Certification | 물류시설의 개발 및 운영에 관한 법률 제21조의4에 따라 국토교통부가 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하는 제도로, 하차·입고부터 상차·출고까지 6개 프로세스의 기능영역과 구조·성과·정보시스템의 기반영역을 심사한다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)? | 관련 영역: 61. 물류창고, 20. 로봇·제조사 관제 연동 | 근거: f12 | 종류: 일반
- 스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가? | 관련 영역: 61. 물류창고, 23. 업무 시스템 연동 | 근거: f18 | 종류: 일반
- 반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가? | 관련 영역: 61. 물류창고, 25. 작업 배정 — MRTA | 근거: f7 | 종류: 일반
- 트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가? | 관련 영역: 61. 물류창고, 32. 예외 복구·재계획·업무 연속성 | 근거: f15 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 20 · 교차 확인: 2
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f12 외 사례 finding 교차 확인 실패(CJ대한통운·DHL·Amazon 사례는 발행 주체 한 곳)
    - f12 의 두 기사는 같은 현장 공개 행사에 기반해 회사 제공 정보를 공유하므로 독립성이 제한적임
    - f1 Azadeh 외 서베이는 출판사 페이지 403 으로 Semantic Scholar API 의 초록만 확인
    - f3 Fragapane 외 서베이는 RePub 저장소의 초록만 확인(권호·쪽수는 검색 결과 기준 294(2) 405–426)
    - f14·f15 DHL 원 보도자료(dhl.com 2023-02, group.dhl.com 2025-05·2025-07)는 세 차례 모두 연결 끊김으로 열지 못해 전문지 기사로 대신함
    - f16·f17 Amazon 페이지의 발행일은 페이지에 없어 검색 결과(2025-07)로 적음
    - f18 인증 심사기준의 등급 구분 점수 기준은 페이지에 없어 미확인
    - f20 CJ대한통운 안성 1등급 인증 사실을 인증센터 목록으로 대조하지 못함
    - 쿠팡 뉴스룸 보도자료(news.coupang.com)는 403 으로 열지 못함
    - 국토교통부 인증제 안내의 세부 기준 첨부 파일 미열람
    - 특허청·한국로봇산업협회 '물류로봇 특집편' PDF 와 로봇학회 논문지 PDF(jkros.org)는 텍스트 추출 실패로 출처 제외
    - 포장 단계의 로봇 사례는 이번 실행에서 확인하지 못함(직전 실행 2026-09-29-10 의 CJ대한통운 양팔 로봇 사례는 이번 출처 상한으로 재인용하지 않음)
    - oq-134 미해결: 국내 물류창고 운영 기록의 시뮬레이션 재현 사례 미확인
    - oq-138 미해결: 국내 물류창고의 대화형 시나리오 구성 사례 미확인
    - oq-142 미해결: 국내 물류창고의 대화형 업무 지시·승인 사례 미확인
    - oq-146 미해결: 물류창고 소음 조건 음성 지시 인식률 자료 미확인(예산 안에서 별도 검색은 하지 못함)
    - ref-005·ref-006·ref-003·ref-004·ref-257 재사용 항목은 참고문헌 목록 입력이 0건이라 등록된 기관·제목·URL 과 글자 단위로 대조하지 못함(ref-005·ref-006 은 arXiv URL 로 적음)
- 범위 경계 위반 의심:
    - f27: WMS 의 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지는 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어 쪽이므로 '연계 대상: '으로 표시함
    - f7·f9: 피커 경로·보충 최적화는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·28. 공용 자원·충전·에너지 최적화 의 방법 영역과 겹치므로 이 영역에서는 반품·보충 단계의 연구 근거로만 제안함
    - f4·f5: MAPD·지속형 MAPF 는 27. 다중 로봇 경로·교통 관리 — MAPF 의 핵심이므로 이 영역에서는 물류창고 규모 기준과 연결 근거로만 제안함
    - f16·f17: Amazon DeepFleet 은 L. AI·학습 기술의 방법(46. 예측·학습 기반 최적화)과 겹치므로 벤더 주장으로만 제안함
    - f18·f19: 스마트물류센터 인증은 59. 법·규제·보험·라이선스·23. 업무 시스템 연동과 겹치므로 이 영역에서는 흐름 단계 정의와 정보시스템 계층의 근거로만 제안함
- 한계: 재실행 1회차. 반려 사유 1(f11: 벤더 문서만 근거로 한 사실 태그에 vendor_claim 없음): 직전 반환값(runs/2026-09-29-11/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로 예산 안에서 브리프를 다시 작성했고, 벤더 문서(Amazon ref-918, CJ대한통운 보도자료 ref-923)만 근거로 한 finding 과 기사에 실린 기업 성능 수치는 모두 vendor_claim true·태그 추정·신뢰도 low·evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다(관련 finding: f10, f13, f15, f16, f17, f20). 이번 브리프의 finding 번호는 직전 반환값과 대응하지 않는다. web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-910~ref-924, 예약 구간 ref-910~ref-939 안) 상한 도달로 RAWSim-O 논문 arXiv 초록(1710.04726, 열었으나 README 로 대체), 국토교통부 인증제 상세 첨부, 콜드체인뉴스·물류신문의 인증제 해설, Locus Robotics·Optoro 의 반품 자동화 글(벤더 문서), DHL Group 2025 보도자료 2건(연결 끊김), 쿠팡 뉴스룸 보도자료(403), ISO 3691-4 계열 물류 로봇 안전 규격은 넣지 못했다. 원문 열람 17건(github_raw 1: RAWSim-O README, webfetch 16: Semantic Scholar API 초록 1, RePub·Pure 초록 2, arXiv 초록 3(ref-913·ref-005·ref-006), KCI 초록 2, 인증센터·국토교통부 페이지 2, 기사 4, 벤더 페이지 2), 재사용 미열람 3건(ref-003·ref-004·ref-257 은 이번에 다시 열지 않아 fetched false·source_unopened true; ref-005·ref-006 은 재사용이지만 arXiv 초록을 열어 fetched true). 주의: 같은 날 이전 실행 2026-09-29-10 이 ref-910~ref-913 을 다른 URL(The Robot Report, 아시아경제, 서울신문)에 부여했다고 그 브리프에 적혀 있으므로 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 하고, 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 학술 서베이·Amazon·인증센터 페이지가 전체 909건과 URL 이 겹칠 수 있다. 교차 확인 2건(f12: 로봇신문/물류신문 — 같은 현장 공개에 기반해 독립성 제한, f19: 국토교통부/한국교통연구원 인증센터). 신뢰도 high 는 f19 한 건(정부·연구기관 원문 2건 열람). 분류 원문 핵심 질문(물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가)에는 단계별 로봇 작업 지도 f24 와 여섯 항목 정리 f25 로 답했으며 결론은 '입고 하역·검수, 적치·피킹의 상품-대-사람 운반, 보충 최적화, 출하 분류·도크 배정, 반품 재적치 통합까지 단계마다 다른 로봇·설비가 들어가고 국내 인증 심사기준이 같은 6단계 구분을 쓰며, 이들을 한 계층에서 묶은 공개 사례는 확인되지 않았고 성과 수치는 회사 설명 수준'이라는 추정이다. 현장 유형: 모두 물류창고(국내 쿠팡 대구·CJ대한통운, 해외 DHL·Amazon, 학술 서베이)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다(f3 의 병원·제조 등 적용 분야 언급만 있음). 국내 자료는 로봇학회 논문지(f8)·한국디지털산업학회지(f9)·인증 심사기준과 안내(f18·f19)·쿠팡(f11~f13)·CJ대한통운(f10·f20) 여덟 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(RAWSim-O 는 설계 연구용 시뮬레이터로 35. 처리능력·규모·배치 설계에 연결). 용어집에 이미 있는 로봇 이동형 풀필먼트 시스템·주문 배치·풋월·웨이브리스 출고 지시·창고 실행·창고 제어·창고 관리 시스템·다중 에이전트 픽업·배송·지속형 다중 에이전트 경로 찾기·플릿 관리 시스템은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 4건(oq-134·oq-138·oq-142·oq-146)은 조사 질문에 넣었으나 별도 검색 예산을 배분하지 못해 미해결로 남긴다. 해결된 열린 질문 없음.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
```
