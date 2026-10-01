(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-21
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 56. 운영 이관·확대·교육 (O. 검증·도입·수명주기)
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

### runs/2026-09-30-21/target.json

```json
{
  "run_id": "2026-09-30-21",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 130,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 56,
    "area_name": "56. 운영 이관·확대·교육",
    "category": "O. 검증·도입·수명주기",
    "category_letter": "O"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=56"
}
```

### runs/2026-09-30-21/research.json

```json
{
  "run_id": "2026-09-30-21",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 56,
    "area_name": "56. 운영 이관·확대·교육",
    "category": "O. 검증·도입·수명주기"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 단계적 인계·사후 지원(소프트 랜딩), 법정 특별안전보건교육, 운영 전담 조직, 역할 모호성 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설·물류창고·제조 공장·기타 현장의 이관·확대·교육 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 단계적 인계·초기 사후 지원, 단계적 시험·확대, 설정 기반 플릿 추가, 운영 인력 교육 과정, 참여형 변화 관리 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육, ANSI/A3 R15.08-3, BSRIA 소프트 랜딩 프레임워크, Open-RMF 플릿 어댑터 템플릿, VDA 5050 팩트시트 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가? [분류원문]",
    "구축 팀에서 운영 팀으로 넘기는 단계적 인계와 초기 사후 지원을 정한 프레임워크(건물 인계의 소프트 랜딩 등)는 무엇이며 로봇 운영 이관에 옮길 수 있는가? (섹션 4·6·7 겨냥)",
    "로봇 운영자·작업자 교육에 관해 한국 법령(산업안전보건법 시행규칙 별표 5 특별교육)과 표준(ANSI/A3 R15.08-3)은 무엇을 요구하며, 서비스 로봇에도 적용되는가? (섹션 7 겨냥, 한국 법령 우선)",
    "병원·상업 시설·물류창고·제조 공장에서 로봇을 시범 운영에서 넓힐 때 어떤 단계와 운영 조직·지원 체계를 두었고, 확대에서 어떤 문제가 보고되었는가? (섹션 3·5 겨냥, 한국 사례 우선)",
    "새 로봇·새 플릿·새 현장을 추가하는 반복 작업을 줄이는 기술적 수단(플릿 어댑터 설정, 팩트시트)은 무엇인가? (섹션 6·7 겨냥)",
    "로봇 도입의 변화 관리(작업자 참여, 저항 요인, 역할 배정, 지속 교육)에 관한 연구 근거는 무엇인가? (섹션 6·8 겨냥)",
    "운영 이관·확대·교육에서 ROP가 직접 맡을 것과 사업주·제조사·통합자·인사 조직에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "법제처는 2023-11-21 법령해석(법제처-23-0872)에서 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 산업용 로봇을 사용하는 작업으로 한정되지 않는다고 회신했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1315"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "질의: 별표 5 제1호라목 36란의 '로봇작업'이 산업용 로봇만을 대상으로 한정되는지 여부. 회답 요지: 산업용 로봇을 사용하는 작업으로 한정되지 않는다.",
      "as_of": "2023-11-21",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "같은 별표의 로봇작업 특별교육 내용은 로봇의 기본원리·구조와 작업방법, 이상 발생 시 응급조치, 안전시설과 안전기준, 조작방법과 작업순서에 관한 사항이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1315"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "법령해석 본문이 인용한 별표 5 로봇작업 교육내용 4개 항목(기본원리·구조 및 작업방법, 이상 발생 시 응급조치, 안전시설 및 안전기준, 조작방법 및 작업순서). 교육시간은 별표 4 소관.",
      "as_of": "2023-11-21",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "기타 현장 사례(한국 급식실): 한국노동연구원 연구보고서(2024-13)는 서비스 로봇이 산업안전보건법상 산업용 로봇·협동로봇 규제를 받지 않고 조리로봇 도입 작업장의 노동자 안전 관리체계가 없으며, 비상정지 버튼 활용 교육과 로봇 청소 시 안전이 미흡해 정기 교육 병행이 필요하다고 제언했다.",
      "tag": "사실",
      "source_ids": [
        "ref-959"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약 기준: 서비스 로봇은 산업용 로봇 및 협동로봇 규제 밖, 조리로봇 작업장 안전 관리체계 부재, 비상정지 버튼 활용 교육·로봇 청소 시 안전 미흡, 정기 교육 병행 제언.",
      "as_of": "2024",
      "site_type": "기타",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "f1 의 법제처 해석은 특별교육 대상 로봇작업을 산업용 로봇에 한정하지 않지만 f3 의 한국노동연구원 보고서는 서비스 로봇이 산업용 로봇 규제 밖에 있다고 지적하므로, 서비스 로봇을 운영하는 인력에게 어떤 법정 교육이 어디까지 적용되는지는 현장에서 불명확할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1315",
        "ref-959"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "법제처-23-0872 회답(로봇작업은 산업용 로봇 작업으로 한정되지 않음)과 한국노동연구원 2024-13 요약(서비스 로봇은 산업용 로봇·협동로봇 규제 밖)을 대조한 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f5",
      "claim": "BSRIA 의 소프트 랜딩 프레임워크(BG 54/2018)는 건축 프로젝트를 착수·요구 정의, 설계, 시공, 인계 전, 초기 사후 지원, 연장 사후 지원과 사용 후 평가의 여섯 단계로 나누며 2014년판을 대체한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1318"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NBS 출판물 색인 설명: 여섯 단계(Inception and briefing / Design / Construction / Pre-handover / Initial aftercare / Extended aftercare and POE), 체크리스트·활동 템플릿 포함, BG 54/2014 대체.",
      "as_of": "2018-08",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f6",
      "claim": "소프트 랜딩처럼 인계 전 준비와 인계 뒤 초기·연장 사후 지원을 구축 측이 함께 맡는 방식은 구축 팀에서 운영 팀으로 로봇 운영을 넘기는 이관에 참고할 수 있을 것으로 보이나, 로봇 오케스트레이션 플랫폼에 이를 적용한 공개 사례는 이번 조사에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1318"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "BSRIA BG 54/2018 의 단계 구성(인계 전·초기 사후 지원·연장 사후 지원)에서 도출한 추론. 로봇 분야 적용 사례 검색 결과 없음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f7",
      "claim": "병원 사례: Valner 외(2022)는 타르투 대학병원 집중치료실에서 검사실로 혈액 검체를 운반하는 이기종 로봇 플릿을 배치하면서 시뮬레이션, 비슷한 물리 공간, 실제 배치 구역 순서로 시험해 현장 시험 시간을 아끼고 문제를 일찍 찾으라는 교훈을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "교훈: 'Test your system starting from simulation, then in a similar physical location and finally in the actual deployment area.'",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "병원 사례: 같은 연구에서 의료진은 로봇에 달린 터치스크린으로 요청을 시작하고 검체를 통에 넣은 뒤 버튼 하나로 확인하는 수동 인계를 했으며, 의료진이 로봇을 멈추고 비킬 수 있어야 한다는 점이 필수 조건으로 꼽혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "터치스크린 요청, 검체를 통에 넣고 단일 버튼으로 확인하는 수동 인계, 비상 정지 능력 필요.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f9",
      "claim": "병원 사례: 같은 연구는 Open-RMF(RMF) 로 서로 다른 로봇(PAL Robotics TIAGo, Clearpath Jackal)을 함께 조율했고, 플릿 어댑터로 로봇 특성을 설정하며 FreeFleet 으로 제조사 전용 플릿 관리자가 없는 로봇도 관리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "학술 논문의 실험 보고: RMF 가 TIAGo 와 Jackal 을 조율, 플릿 어댑터로 로봇 특성 설정, FreeFleet 미들웨어로 전용 플릿 관리자 없이 관리.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "Open-RMF 의 fleet_adapter_template 은 Python 기반 full_control 플릿 어댑터의 참조 구현으로, 새 플릿을 붙일 때 RobotClientAPI.py 의 API 호출 부분을 채우고 config.yaml 의 rmf_fleet(로봇 파라미터)·fleet_manager(관제 API 연결)·reference_coordinates(좌표 변환) 세 절을 설정하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1319"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 'Fill up certain blocks of code which make API calls to your mobile robotic fleet.' config.yaml 은 rmf_fleet, fleet_manager, reference_coordinates 로 구성.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "VDA 5050 명세의 팩트시트(factsheet) 메시지는 플릿 관제에서 이동로봇을 설정하는 데 도움이 되는 파라미터와 제조사별 정보를 전하며, 플릿 관제가 factsheetRequest 즉시 동작으로 요청하면 로봇이 보낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 원문: 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control' / factsheetRequest: 'Requests the mobile robot to send a factsheet'. (재인용: 2026-09-30-19)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "병원 사례(한국): 한림대학교성심병원은 전담 부서인 커맨드센터가 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했으며, 커맨드센터는 사용 시나리오 개발, 업무 프로세스 조율, 실시간 모니터링과 문제 대응을 맡는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1199",
        "ref-944"
      ],
      "cross_checked": true,
      "confidence": "low",
      "evidence_excerpt": "2024년 보도 기준 7종 73대, 전담 부서 커맨드센터가 시나리오 개발·업무 조율·모니터링·문제 대응 담당. (재인용: 2026-09-30-18)",
      "as_of": "2024-09-19",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "병원 사례(한국): 주간한국 보도에 따르면 한림대학교성심병원은 2025-07-18 한국장애인고용공단 경기남부직업능력개발원과 협약을 맺고, 2022-08부터 운영한 11종 77대 의료서비스로봇의 상태 점검·에러 대응·관제화면 모니터링을 맡을 운영 인력을 기르는 실무 중심 교육 과정을 함께 만들기로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1317"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "협약(2025-07-18) 교육 초점: 로봇 상태 점검, 에러 대응 절차, 커맨드센터 화면 모니터링, 실습 중심 운영 훈련. 로봇 규모 11종 77대. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "병원 사례: Mutlu·Forlizzi(HRI 2008)의 민족지 연구에서 같은 병원의 자율 배송 로봇(TUG)이 내과 병동에서는 업무 흐름을 방해하고 직원 저항을 낳았지만 산후 병동에서는 업무 흐름과 사회적 맥락에 통합되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1151"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "15개월 민족지 연구, 병동별 업무 중단 허용도·비용 인식 차이로 결과가 갈림. (재인용: 2026-09-30-18)",
      "as_of": "2008-03",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "f14 와 f7 로 보아 한 병동·한 구역의 시범 성공이 다른 단위로의 확대를 보장하지 않으므로, 단계적 확대에서는 단위마다 업무 흐름·수용성을 다시 확인하고 시험 단계를 거쳐야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1151",
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "병동별로 결과가 갈린 TUG 사례와 시뮬레이션→유사 공간→실제 구역 순 시험 교훈에서 도출한 추론.",
      "as_of": "2026-09-30",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f16",
      "claim": "상업 시설 사례: Fu·Zheng·Wong(2022)의 중국 고급 호텔 직원 면담에서 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육·동료 교육·고장 처리 같은 추가 업무가 로봇 사용 저항으로 이어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1150"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "직원 19명 면담, 역할 모호성과 추가 업무(교육·고장 처리)가 사용 저항 요인. (재인용: 2026-09-30-18)",
      "as_of": "2022",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "병원 사례(싱가포르): 창이종합병원의 CHART 는 의료 로봇 미들웨어 RoMi-H 통합을 맡을 시스템 통합자를 등재 프로그램으로 평가·인증하며, 공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-872"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RoMi-H 등재 프로그램 2025, 연 2회 평가, 등재 통합자 활용. (재인용: 2026-09-30-19)",
      "as_of": "2025-05",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "병원 사례: Li 외(Scientific Reports, 2026)는 중국 3차 병원의 약품·검체 배송에 자율이동로봇 10대를 6개월 동안 수작업과 병행 대조로 평가해 배송 시간이 32~36% 줄었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1161"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: 10대 AMR, 6개월 병행 대조 평가, 배송 시간 32~36% 감소. (재인용: 2026-09-30-19)",
      "as_of": "2026-04",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "물류창고 사례(피킹): Pasparakis·De Vries·De Koster(2026)의 네덜란드 실험 창고(피킹 위치 300곳, 직업학교 학생 60명) 실험에서 사람이 로봇을 이끌면 생산성이 높고 오류가 많았으며 로봇이 사람을 이끌면 정확도가 높았고, 저자들은 속도·정확도 우선순위와 작업자 성향에 맞춰 역할을 배정하라고 제언했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1320"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "20분 라운드 3회(수작업 기준 1회, 협업 2회). 로봇 선도 시 'physically stopping at the correct pick location' 으로 오류 감소. 초록·요약 기준.",
      "as_of": "2026-07",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "Pietrantoni 외(2024)가 유럽 9개국 전문가 31명을 조사한 결과, 전문가들은 포괄적 안전 교육과 사용하기 쉬운 인터페이스, 지속적 직업 훈련을 필수로 보았고, 일자리 대체 우려와 이점 이해 부족을 변화 저항의 원인으로, 효과적 소통과 리더십 지원을 대응책으로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1323"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "혼합 방법, 차량 조립·창고 물류·농업 분야 전문가 31명. 'continuous vocational training' 필요, 재교육·역량 향상 부담 지적.",
      "as_of": "2024-12-02",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f21",
      "claim": "물류창고 사례(벤더 주장): Locus Robotics 는 Locus Origin 의 태블릿 화면 덕분에 신규 작업자가 몇 분 안에 생산적으로 일할 수 있고 수십 개 언어를 지원한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1321"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'new associates can often be productive within minutes', 수십 개 언어 지원. 독립 측정 자료 없음.",
      "as_of": "2026-09-30",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f22",
      "claim": "제조 공장 사례(한국): 로봇신문에 따르면 한국로봇산업진흥원의 2026년 로봇활용 제조혁신 지원사업은 국비 450억원 규모로 로봇 자동화 시스템 도입비용과 컨설팅·로봇 교육을 지원하며, 선정 과제 컨소시엄 담당자 400여명에게 사업 관리지침·안전 컨설팅·현장 감리 점검사항 통합교육을 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1324"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "도입비용과 컨설팅, 로봇 교육 등 지원. 선정기업 통합교육(사업 관리지침, 로봇 엔지니어링·안전 컨설팅, 현장 감리 주요 점검사항).",
      "as_of": "2026-05-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "ANSI/A3 R15.08-3-2026 은 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구사항을 정하며, 위험성평가와 응용·운영 환경의 변경 관리, 수명주기 전반의 인원 안전을 강조한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약 기준(원문 미열람): 사용자 측 운용·정비 요구, 위험성평가, 변경 관리. (재인용: 2026-09-30-18)",
      "as_of": "2026-04-23",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "확인한 자료를 종합하면 핵심 질문(시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가)에 대해, 인계 전 준비와 초기·연장 사후 지원을 두는 단계적 인계 틀(건물 분야)과 단계적 시험·확대 교훈, 전담 운영 조직과 운영 인력 교육 과정 사례(한국 병원), 법정 로봇작업 특별교육이 있으나, 여러 제조사 로봇 플랫폼의 운영 이관 완료 기준이나 확대 절차를 정한 공개 표준은 확인하지 못했고 역할이 불분명하면 저항이 생기는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1318",
        "ref-1198",
        "ref-1199",
        "ref-1317",
        "ref-1151",
        "ref-1150",
        "ref-1315",
        "ref-959",
        "ref-1323"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5·f7·f12·f13·f14·f16·f1·f3·f20 의 종합. 로봇 플랫폼 이관 표준은 검색에서 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "확인한 자료를 종합하면 56. 운영 이관·확대·교육에서 ROP가 직접 맡을 범위는 새 플릿·로봇·현장 추가를 설정 파일과 팩트시트 기반 등록으로 반복 가능하게 하는 것, 이관 때 넘길 운영 상태·설정·인계 기록의 제공, 운영자 역할과 권한 정의, 단계적 확대 전후의 성과 기록, 교육·시험에 쓸 시뮬레이션 모드 제공으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1319",
        "ref-031",
        "ref-1198",
        "ref-1199"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9·f10·f11(설정 기반 플릿 추가·팩트시트), f7(시뮬레이션부터 단계 시험), f12(전담 조직의 관제 업무)에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f26",
      "claim": "연계 대상: 분류 원문 19장 기준으로 법정 안전보건교육 실시와 작업 지침(사업주), 로봇 조작·정비 교육(제조사), 통합자 인증과 현장 통합(통합자), 인력 편성·직무 설계·노사 협의(현장 조직·인사)는 외부가 맡으므로, ROP는 그들에게 운영 상태·교육용 자료·기록을 제공하고 역할·권한을 반영하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1315",
        "ref-1153",
        "ref-872",
        "ref-1323"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2(사업주 특별교육), f23(사용자 측 운용 요구), f17(통합자 인증), f20(교육·변화 관리)에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": false
    },
    {
      "id": "f27",
      "claim": "이 영역은 이관 직전 단계인 55. 현장 조사·설치·시운전(f7), 단계 시험의 54. 시험·형식 검증·벤치마크(f7), 이관 뒤 버전·장비 교체의 57. 자산·소프트웨어 수명주기 관리(f10), 새 로봇 추가의 4. 이기종 로봇 등록과 20. 로봇·제조사 관제 연동(f9·f10·f11), 팩트시트의 21. 상호운용 표준·적합성(f11), 운영 조직·교대의 40. 운영 절차·요청 창구(f12), 관제 업무 교육의 37. 관제 화면·실행 기록(f13), 작업자 역할 배정의 31. 사람–로봇 협업(f19), 확대 전후 성과의 39. 운영 성과 측정·개선(f18), 법정 교육·표준의 50. 안전 표준·인증·사고 조사와 59. 법·규제·보험·라이선스(f1·f3·f23), 통합자·사업자 책임의 58. 다사업자 책임·계약·데이터(f17), 수용성·변화 저항의 60. 노동·수용성·접근성(f16·f20), 지원 사업의 3. 경제성·조달·사업 모델(f22), 적용 현장인 61. 물류창고(f19·f21)·62. 제조 공장(f22)·63. 병원·의료(f7~f9·f12~f14·f17·f18)·64. 상업 시설(f16)·67. 기타 현장(f3)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1198",
        "ref-1319",
        "ref-031",
        "ref-1199",
        "ref-1317",
        "ref-1320",
        "ref-1161",
        "ref-1315",
        "ref-959",
        "ref-1153",
        "ref-872",
        "ref-1150",
        "ref-1323",
        "ref-1324",
        "ref-1321",
        "ref-1151"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 의 대응 영역을 묶은 연결 제안.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    }
  ],
  "sources": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 명세 원문. 이번에는 팩트시트 메시지의 목적과 factsheetRequest 즉시 동작을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1150",
      "org": "Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management)",
      "title": "The perils of hotel technology: The robot usage resistance model",
      "published": "2022",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중국 고급 호텔 직원 면담으로 로봇 사용 저항 요인(역할 모호성, 추가 업무 등)을 정리한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1199",
      "org": "지디넷코리아",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원 커맨드센터의 서비스 로봇 통합 운영을 다룬 기사.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인)",
      "published": "2024-04",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원의 서비스 로봇 운영과 커맨드센터 역할을 다룬 기사.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008-03",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 배송 로봇 TUG 의 병동별 수용 차이를 15개월 민족지로 분석한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1153",
      "org": "ANSI (The ANSI Blog)",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": null,
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 산업용 이동로봇 응용의 사용자 측 운용·정비 요구사항을 정한 ANSI/A3 R15.08-3-2026 소개 글.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "RoMi-H 통합을 맡을 시스템 통합자를 평가·등재하는 싱가포르 병원 프로그램 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1161",
      "org": "Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04",
      "url": "https://www.nature.com/articles/s41598-026-49800-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "중국 3차 병원의 약품·검체 배송 AMR 10대를 6개월 병행 대조로 평가한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1315",
      "org": "법제처",
      "title": "로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872)",
      "published": "2023-11-21",
      "url": "https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업안전보건법 시행규칙 별표 5 특별교육 대상 로봇작업이 산업용 로봇 작업으로 한정되지 않는다는 법령해석과 로봇작업 교육내용.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638",
      "source_unopened": false
    },
    {
      "id": "ref-1198",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원에서 RMF 로 이기종 로봇 플릿을 배치해 검체를 운반한 현장 시험과 교훈.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/",
      "source_unopened": false
    },
    {
      "id": "ref-1317",
      "org": "주간한국",
      "title": "한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인)",
      "published": null,
      "url": "https://weekly.hankooki.com/news/articleView.html?idxno=7120747",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원과 한국장애인고용공단 경기남부직업능력개발원의 병원 로봇 운영 인력 양성 협약(2025-07-18) 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://weekly.hankooki.com/news/articleView.html?idxno=7120747",
      "source_unopened": false
    },
    {
      "id": "ref-1318",
      "org": "BSRIA (NBS 출판물 색인)",
      "title": "BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings",
      "published": "2018-08",
      "url": "https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "건물 인계와 사후 지원을 여섯 단계로 정리한 BSRIA 소프트 랜딩 프레임워크의 출판물 색인 설명(본문은 유료, 색인 페이지만 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192",
      "source_unopened": false
    },
    {
      "id": "ref-1319",
      "org": "Open-RMF (open-rmf/fleet_adapter_template 저장소)",
      "title": "fleet_adapter_template README",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Python 기반 full_control 플릿 어댑터 참조 템플릿과 config.yaml 구성, 새 플릿 연동 절차.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/fleet_adapter_template/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1320",
      "org": "Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1))",
      "title": "In control or under control? Human–robot collaboration in warehouse order picking",
      "published": "2026-07",
      "url": "https://doi.org/10.1108/LORE-03-2025-0028",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실험 창고에서 사람 선도·로봇 선도 협업 피킹의 생산성·정확도를 비교한 연구(초록·요약 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.emerald.com/lore/article/19/1/89/1342937/In-control-or-under-control-Human-robot",
      "source_unopened": false
    },
    {
      "id": "ref-1321",
      "org": "Locus Robotics",
      "title": "Locus Origin: Collaborative Robots Warehouse",
      "published": null,
      "url": "https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "Locus Origin 협업 피킹 로봇 제품 페이지. 신규 작업자 교육 시간과 다국어 지원에 관한 벤더 주장.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot",
      "source_unopened": false
    },
    {
      "id": "ref-959",
      "org": "한국노동연구원",
      "title": "음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13)",
      "published": "2024",
      "url": "https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 급식·조리 로봇 도입이 직무와 작업장 안전에 미친 영향을 현장 관찰로 분석하고 안전 관리체계·교육을 제언한 보고서(403 으로 열지 못해 검색 요약 기준).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1323",
      "org": "Pietrantoni, L. 외 (Frontiers in Robotics and AI)",
      "title": "Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors",
      "published": "2024-12-02",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "유럽 9개국 전문가 31명의 혼합 방법 조사로 협동로봇 통합의 기술·안전·인적 요인(교육, 변화 저항)을 정리한 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/",
      "source_unopened": false
    },
    {
      "id": "ref-1324",
      "org": "로봇신문",
      "title": "한국로봇산업진흥원, 450억 규모 '2026년 로봇활용 제조혁신 지원사업' 착수",
      "published": "2026-05-12",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=46336",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2026년 로봇활용 제조혁신 지원사업(국비 450억원)의 지원 내용과 선정기업 통합교육 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.irobotnews.com/news/articleView.html?idxno=46336",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
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
      "rationale": "섹션 3: f24(핵심 질문 답, 추정), f14·f16(확대·역할 불명확 시 문제), f4(교육 적용 범위 불명확) / 섹션 4: 소프트 랜딩 f5·f6, 로봇작업 특별교육 f1·f2, 운영 전담 조직 f12, 역할 모호성 f16, 팩트시트 f11 / 섹션 5: 병원 — f7(예외·성과)·f8(완료·인계)·f9(수행 자원)·f12·f13(수행 자원, 한국)·f14(예외·성과)·f17(수행 자원, 싱가포르)·f18(예외·성과), 상업 시설 — f16(수행 자원), 물류창고 — f19(수행 자원, 피킹)·f21(수행 자원, 벤더 주장 병기), 제조 공장 — f22(수행 자원, 한국), 기타 — f3(제약, 한국 급식실). 가정·실외 사례는 찾지 못했음을 명시 / 섹션 6: 단계적 인계·사후 지원 f5·f6, 단계적 시험·확대 f7·f15·f18, 설정 기반 플릿 추가 f9·f10·f11, 운영 전담 조직과 운영 인력 교육 f12·f13, 참여형 변화 관리와 역할 배정 f19·f20 / 섹션 7: 산업안전보건법 시행규칙 별표 5 f1·f2, ANSI/A3 R15.08-3 f23(원문 미열람), BSRIA BG 54/2018 f5, Open-RMF fleet_adapter_template f10, VDA 5050 팩트시트 f11 / 섹션 8: f3·f7·f14·f16·f19·f20 / 섹션 9: f25(직접 범위), f26(연계 대상) / 섹션 10: f27 — 3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f7·f13, 67. 기타 현장 페이지에 f3 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "소프트 랜딩",
      "term_en": "Soft Landings (BSRIA BG 54)",
      "definition": "설계·시공 팀이 인계 전 준비부터 인계 뒤 초기·연장 사후 지원과 사용 후 평가까지 함께 맡아 시설을 운영 단계로 단계적으로 넘기는 프레임워크이다."
    },
    {
      "term_ko": "특별안전보건교육",
      "term_en": "Special Occupational Safety and Health Training (Korea)",
      "definition": "산업안전보건법 시행규칙 별표 5 가 정한 유해·위험 작업(로봇작업 포함)에 근로자를 배치하거나 작업 내용을 바꿀 때 사업주가 추가로 실시해야 하는 안전보건교육이다."
    },
    {
      "term_ko": "사용 후 평가",
      "term_en": "Post-Occupancy Evaluation (POE)",
      "definition": "시설이나 시스템을 넘겨받아 실제로 쓰기 시작한 뒤 성능과 사용자 경험을 점검해 개선점을 찾는 평가이다."
    }
  ],
  "open_questions_new": [
    "서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? | 관련 영역: 56. 운영 이관·확대·교육, 59. 법·규제·보험·라이선스, 50. 안전 표준·인증·사고 조사 | 근거: f4 | 종류: 일반",
    "여러 제조사 로봇을 묶는 오케스트레이션 플랫폼을 구축 팀에서 운영 팀으로 넘길 때의 완료 기준(운영 인수 조건, 초기 사후 지원 기간, 지원 책임 이전 시점)을 정한 공개 표준이나 사례가 있는가? | 관련 영역: 56. 운영 이관·확대·교육, 55. 현장 조사·설치·시운전 | 근거: f6 | 종류: 일반",
    "한 현장의 시범 운영을 다른 현장으로 넓힐 때 재사용되는 설정(지도·플릿 어댑터·능력 정의)과 현장마다 다시 해야 하는 작업의 비율이나 소요 시간을 측정한 연구가 있는가? | 관련 영역: 56. 운영 이관·확대·교육, 55. 현장 조사·설치·시운전, 4. 이기종 로봇 등록 | 근거: f10 | 종류: 일반",
    "로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가? | 관련 영역: 56. 운영 이관·확대·교육, 40. 운영 절차·요청 창구, 60. 노동·수용성·접근성 | 근거: f13 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 1,
    "unverified": [
      "로봇작업 특별교육 시간(16시간 이상, 최초 4시간 등)은 국가법령정보센터 별표 PDF 추출 실패로 확인하지 못해 finding 에서 뺌",
      "f3 한국노동연구원 보고서는 403 으로 원문 미열람, 검색 요약 범위만 사용. 조사 현장이 학교 급식실인지 세부 미확인",
      "f13 주간한국 기사 제목 전체와 발행일 미확인",
      "f5 BSRIA 프레임워크 본문(유료) 미열람, 초기 사후 지원 기간(4~6주)·연장 사후 지원(1~3년) 수치는 제3자 위키 요약에만 있어 넣지 않음",
      "f19 는 초록·요약 기준이며 수작업 피킹 숙련의 전이 여부는 확인하지 못함",
      "f21 Locus 교육 시간 주장은 독립 측정 자료로 교차 확인 실패",
      "ITIL 4 초기 운영 지원(Early Life Support)·하이퍼케어 개념은 공식 AXELOS 자료를 열지 못하고 컨설팅 블로그만 있어 넣지 않음",
      "EU-OSHA 협동로봇 사례 PDF 는 본문 추출 품질이 낮아 넣지 않음",
      "MDPI Robotics 14(12) 병원 AMR 리뷰는 403 으로 넣지 않음",
      "가정·실외 현장의 운영 이관·교육 사례를 찾지 못함"
    ],
    "scope_violations": [
      "f3: 조리로봇 청소·비상정지 안전은 원문 19장 '로봇 자체 지능·제어'·설비 안전 쪽에 가까워 교육 요구의 근거로만 쓰고 ROP 직접 범위로 쓰지 않음",
      "f1·f2·f23: 법정 교육과 사용자 측 안전 운용 요구는 사업주·현장 조직의 책임이므로 f26 에서 연계 대상으로 구분함",
      "f9·f10: 플릿 어댑터 구현 세부는 20. 로봇·제조사 관제 연동의 범위와 겹쳐 확대 수단의 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 13,
      "sources": 10
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치 — 직전 산출물의 f9 가 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 산출물(runs/2026-09-30-21/research.json)이 이번 프롬프트 입력에 들어 있지 않아 형식만 고칠 수 없었으므로, 같은 대상으로 브리프 전체를 다시 작성했다. 이번 브리프에서 벤더 문서만 근거로 한 주장은 f21(Locus Robotics) 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈고, f9 는 학술 논문(ref-1198) 근거의 [사실]이다. 모든 finding 의 id·내용은 직전 산출물과 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 10건/15(ref-1315~ref-1324, 예약 구간 안). 재사용 8건(ref-031, ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-18·2026-09-30-19 출처 표를 따랐고 요약 문장은 새로 썼다. ref-031 만 GitHub 공식 저장소 원문을 다시 열어 팩트시트 문장을 확인했다(나머지 재사용 출처는 이번에 다시 열지 않아 fetched false). 원문 열람: 신규 10건 중 9건을 열었고(webfetch 8, github_raw 1) ref-959 는 403 으로 원문 미열람. ref-1318 은 유료 표준 가이드의 출판물 색인 페이지만 열었다. 교차 확인 1건(f12: 지디넷코리아·로봇신문). 분류 원문 핵심 질문에는 f24 로 답했고 결론은 '단계적 인계 틀·단계적 시험 교훈·전담 운영 조직과 교육 과정 사례·법정 로봇작업 특별교육은 있으나 다중 제조사 로봇 플랫폼의 이관 완료 기준·확대 절차 공개 표준은 확인하지 못했다'는 추정이다. 현장 유형 사례는 병원(f7~f9·f12~f14·f17·f18, 한국·에스토니아·싱가포르·중국)·상업 시설(f16)·물류창고(f19, f21 벤더)·제조 공장(f22, 한국)·기타(f3, 한국 급식실)이며 가정·실외는 찾지 못했다. 국내 자료는 법제처(ref-1315)·한국노동연구원(ref-959)·주간한국(ref-1317)·로봇신문(ref-1324) 등이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 플릿 어댑터·VDA 5050 팩트시트·등재 프로그램·서비스 수준 협약·위험성평가는 후보로 내지 않았다. 기존 열린 질문 중 이 영역에 걸린 것은 없다. 입력 누락: 직전 산출물 research.json 미수신. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-21/verification.json

```json
{
  "run_id": "2026-09-30-21",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 법제처 법령해석 페이지를 열어 안건번호 법제처-23-0872, 회신일 2023-11-21, 회답 요지('산업용 로봇을 사용하는 작업으로 한정되지 않는다')가 일치함. 발행 기관 원문이며 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 법령해석 페이지에 별표 5 로봇작업 교육내용 4개 항목(기본원리·구조 및 작업방법, 이상 발생 시 응급조치, 안전시설 및 안전기준, 조작방법 및 작업순서)이 있음."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "원문 미열람(검증자 열람도 403). 검색 결과 요약에서는 서비스 로봇이 산업용 로봇·협동로봇 안전기준을 받지 않고 식품위생법상 위생 규제만 받는다는 점, 조리로봇 도입 작업장의 노동자 안전 관리체계 부재, 로봇 활용 교육 필요만 확인됨. 비상정지 버튼 활용 교육, 로봇 청소 시 안전 미흡, 정기 교육 병행 제언은 스니펫에서 확인하지 못함. 조사 대상은 외식업 종사자 FGI와 학교급식(중학교 3곳 현장관찰)이므로 '기타(학교 급식실)'로 두는 것은 타당함."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 대조 추론. 근거가 된 f1(원문 확인)과 f3 의 '서비스 로봇은 산업용·협동로봇 안전기준 밖' 부분(검색 요약 확인)이 모두 살아 있어 추론 근거가 유효함."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: NBS 출판물 색인 페이지를 열어 발행 2018-08, 여섯 단계 구성(인계 전·초기 사후 지원·연장 사후 지원과 사용 후 평가 포함), BG 54/2014 대체가 일치함. BSRIA 가이드 본문(유료)은 미열람이며 색인 설명 기준."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 구축자 추론. 로봇 분야 적용 사례 미발견을 명시해 적절함."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Frontiers 원문(PMC 는 캡차)을 열어 타르투 대학병원, 집중치료실→검사실 혈액 검체 운반, '시뮬레이션 → 비슷한 물리 공간 → 실제 배치 구역' 순 시험 교훈이 일치함. 다만 병원에 실제 배치된 로봇은 TIAGo 한 대이므로 '이기종 로봇 플릿을 배치하면서'라는 표현은 고쳐야 함(수정 지시)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇 터치스크린 요청, 검체를 통에 넣고 버튼으로 확인하는 수동 인계, '의료진이 로봇을 멈추고 비킬 수 있어야 한다'는 요구가 원문에 있음."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 불일치: 원문은 RMF 의 이기종 로봇(TIAGo·Clearpath Jackal) 관리를 '시험 환경에서' 검증했고 병원 안에서는 아직 여러 배송 로봇을 적용하지 않았다고 밝힘(병원 배치는 TIAGo). '병원에서 서로 다른 로봇을 함께 조율했다'는 부분은 맥락 이탈. 플릿 어댑터 설정 파일에 로봇 특성을 기술한다는 점과 FreeFleet 이 전용 플릿 관리자가 없는 로봇용이라는 점은 원문과 일치함. 과장된 부분을 삭제하고 좁힌 문장만 쓰도록 지시함."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub raw README 를 열어 Python 기반 full_control 참조 템플릿, RobotClientAPI.py 채우기, config.yaml 의 rmf_fleet·fleet_manager·reference_coordinates 세 절이 일치함. 저장소 문서라 발행일이 없어 기준일은 접근일 2026-09-30."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력의 data/source_texts/ref-031.txt(VDA 5050 3.0.0) 4.3절 표에 factsheet 토픽 용도 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control'과 factsheetRequest 'Requests the mobile robot to send a factsheet'가 있음. 판은 3.0.0 으로 명시할 것. evidence_excerpt 에 같은 출처 직접 인용이 두 구절이라 페이지에서는 한 번만 인용."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "검증자가 두 기사를 직접 열어 확인: 지디넷코리아(2024-09-19, '7가지 종류의 서비스로봇 73대', 센터장 발언 '의료진이 로봇을 직접 운용하느라 골머리를 쓸 필요가 없다')와 로봇신문(2024-04-15, 7종 73대, 커맨드센터의 통합 관제로 다제조사 로봇 관리). 두 매체는 발행 주체가 달라 독립. 다만 커맨드센터 역할로 기사에 나온 것은 운영 인프라 설정·변경, 시나리오별 프로세스 가이드, 병원 맞춤형 프로세스 구축, 활용 효과 정량 평가이며 '실시간 모니터링과 문제 대응'은 이번 열람 요약에서 확인하지 못함(수정 지시). 브리프의 fetched 표시는 false(이번 리서치에서는 미열람)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 주간한국 기사를 열어 협약일 2025-07-18, 한국장애인고용공단 경기남부직업능력개발원, 2022-08부터 11종 77대, 교육 초점(로봇 상태 점검·에러 대응·관제화면 모니터링, 실무 중심)이 일치함. 기사 발행일은 2025-07-23 으로 확인되어 브리프의 published null·as_of 2026-09-30 을 고쳐야 함(수정 지시). 단일 기사."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 저자 PDF 는 텍스트 추출이 부실했으나 WebSearch 결과의 초록(내과 병동은 업무 중단 허용도가 낮고 비용·효용 인식 차이, 통행 혼잡으로 업무 흐름에 부정적 영향과 직원 저항, 산후 병동은 업무 흐름·사회적 맥락에 통합)이 주장과 일치함. HRI 2008. 15개월 기간은 이번에 확인하지 못해 본문 수치로 쓰지 않는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] f14·f7 에서 도출한 추론이며 근거 finding 이 유지됨."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 PMC 원문을 열어 중국 고급·럭셔리 호텔 직원 19명 면담, 로봇 소속 부서 불분명('robotics department' 없음)으로 부서 간 조율 부담, 근무 중 학습·동료 교육·고장 처리(고객 불만·제조사 연락) 추가 업무가 저항으로 이어짐을 확인함. 브리프의 fetched 표시는 false."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 불일치: CGH 페이지(2025-05-01 게시, 2026-08-24 갱신)는 CHART 가 연 2회 RoMi-H 배치 역량을 평가해 통합자를 인증하고 명단을 공개해 공공 의료기관(PHI)이 RFP/RFI 로 연락할 수 있게 한다고만 적고, 공공 의료기관이 등재 통합자를 '써야 한다'는 의무는 명시하지 않음. 의무 부분을 삭제하도록 지시함. 이전 실행 2026-09-30-19 의 같은 주장(3. 경제성·조달·사업 모델 페이지)에도 같은 문제가 있을 수 있음."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(nature.com 인증 리다이렉트). WebSearch 결과로 Scientific Reports 2026-04-24 게재, AMR 10대, 수작업 대비 배송 시간 32~36% 감소를 확인함. '6개월 병행 대조'는 이번 검색 요약에 나타나지 않아 이전 실행 2026-09-30-19 초록 확인에 기댐. 신뢰도는 medium 이하."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Emerald 페이지를 열어 Logistics Research 19(1), 저자, 피킹 위치 300곳·직업학교 학생 60명·20분 라운드 3회, 사람 선도 시 생산성 우위, 로봇 선도 시 정확도 우위('physically stopping at the correct pick location'), 속도·정확도 절충과 작업자 특성에 맞춘 구성 제언이 일치함. 발행일은 2026-02-24 로 표시되어 브리프의 2026-07 과 다름(수정 지시). '네덜란드' 실험 장소는 이번 열람에서 확인하지 못함."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 원문을 열어 2024-12, 유럽 9개국 전문가 31명, 차량 조립·창고 물류·포도 수확, 포괄적 안전 교육·사용하기 쉬운 인터페이스·지속적 직업 훈련, 일자리 대체 우려와 이점 이해 부족, 효과적 소통과 리더십이 일치함."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제품 페이지에 'new associates can often be productive within minutes'와 수십 개 언어 지원 문구가 있음. 벤더 문서 단독이며 vendor_claim: true·[추정]·'벤더 주장: ' 표시가 되어 있어 적절함."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇신문 기사(2026-05-12)를 열어 국비 450억원, 도입비용·컨설팅·로봇 교육 지원, 선정 과제 컨소시엄 담당자 약 400명 통합교육(사업 관리지침, 로봇 엔지니어링·안전 컨설팅, 사업비 관리·정산, 현장 감리 점검사항)이 일치함. 단일 기사."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ANSI 블로그 403). WebSearch 결과의 ANSI 블로그 요약이 사용자 측 운용·정비 요구, 위험성평가, IMR 응용·현재 운영 환경의 변경 관리, 기계 수명주기 전반의 인원 안전을 담아 주장과 일치함. A3 스토어의 같은 표준 판매 페이지도 검색됨. 브리프의 as_of 2026-04-23 은 근거를 확인하지 못함(발행일 미확인)."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 종합. 근거 finding 대부분이 유지됨. 강등된 f3 의 교육 세부는 종합 문장에 쓰이지 않음."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 직접 범위 제안. f9 는 범위를 좁혀도 '플릿 어댑터 설정 파일로 로봇 특성 기술'이 남으므로 근거가 유지됨."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 연계 대상 구분. 분류 원문 19장 경계와 맞음. f17 근거는 '통합자 인증·명단 공개'로 좁혀 읽는다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정] 연결 제안. 영역 번호와 이름이 부록 A 원문 명칭과 일치함."
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
      "f17(ref-872)·f18(ref-1161)은 실행 2026-09-30-19 의 f11·f10(3. 경제성·조달·사업 모델 페이지)과 같은 주장이다 — 같은 참고문헌 id 를 재사용하고 새 각주를 만들지 않는다",
      "f12·f14·f16·f23(ref-1199·ref-944·ref-1151·ref-1150·ref-1153)은 실행 2026-09-30-18 에서 재인용한 주장이다 — 기존 참고문헌 id 를 재사용한다",
      "f11 의 팩트시트는 용어집 vda-5050-factsheet 와, f9·f10 의 플릿 어댑터는 용어집 fleet-adapter 와 겹친다 — 새 용어로 등록하지 않고 연결만 한다",
      "f12(2024 보도, 7종 73대)와 f13(2025-07 보도, 11종 77대)은 같은 병원의 다른 시점 수치이다 — 모순이 아니므로 기준일을 각각 밝혀 제시한다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "f11 의 evidence_excerpt 가 ref-031 에서 직접 인용 두 구절('Parameters or vendor-specific information …', 'Requests the mobile robot to send a factsheet')을 담고 있다 — 출처당 1회 규칙"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f9: '병원에서 서로 다른 로봇(TIAGo, Jackal)을 함께 조율했다'는 부분을 삭제하고, 출처가 직접 말한 범위 — RMF 의 이기종 로봇(TIAGo·Clearpath Jackal) 관리는 시험 환경에서 검증했고 병원 배치는 TIAGo 로 했으며 여러 배송 로봇의 병원 적용은 아직이라고 저자가 밝힘, 로봇 특성은 RMF 플릿 어댑터 설정 파일에 기술, FreeFleet 은 전용 플릿 관리자가 없는 로봇용 — 로 좁혀 쓴다 — 원문(ref-1198)이 이기종 관리를 시험 환경 결과로 한정한다.",
    "f7: '이기종 로봇 플릿을 배치하면서'를 'RMF 기반 플릿 체계로 TIAGo 로봇을 배치하면서'처럼 병원에 실제 배치된 로봇이 한 대였음을 드러내게 고친다 — 원문은 병원 현장 배치를 TIAGo 로만 보고한다.",
    "f17: '공공 의료기관은 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 되어 있다'를 삭제하고 'CHART 가 연 2회 RoMi-H 배치 역량을 평가해 통합자를 인증하고 명단을 공개해 공공 의료기관이 제안요청(RFP/RFI)에 활용하게 한다'로 좁힌다 — ref-872 페이지에 의무 사용 문구가 없다. ref-872 발행일은 2025-05-01(2026-08-24 갱신)로 적는다.",
    "f3: 검색 요약으로 확인된 부분(서비스 로봇은 산업용 로봇·협동로봇 안전기준을 받지 않고 식품위생법상 위생 규제만 받음, 조리로봇 도입 작업장의 노동자 안전 관리체계 부재, 로봇 활용 교육 필요)만 [사실]로 쓰고, '비상정지 버튼 활용 교육·로봇 청소 시 안전 미흡·정기 교육 병행 제언'은 [추정]으로 강등하거나 뺀다 — ref-959 는 원문 미열람이고 해당 세부가 검색 요약에 나타나지 않는다. 현장 유형은 기타(학교 급식실)로 쓰고 외식업 FGI 를 병원·상업 시설 사례로 옮기지 않는다.",
    "f12: 커맨드센터 역할을 출처 표현대로 '로봇 운영 인프라 설정·변경, 시나리오별 프로세스 가이드, 병원 맞춤형 프로세스 구축, 활용 효과 정량 평가'로 쓰고 '실시간 모니터링과 문제 대응'은 빼거나 미확인으로 둔다 — 두 기사에서 그 문구를 확인하지 못했다. 로봇 규모 7종 73대는 2024 보도 기준임을 밝힌다.",
    "f13·ref-1317: 발행일을 2025-07-23 으로 적고(각주의 '미확인'을 바꾼다) f13 의 기준일도 2025-07-23 으로 쓴다. 로봇 규모 11종 77대는 2025-07 보도 기준임을 밝힌다.",
    "f19·ref-1320: 발행일을 2026-02-24 로 고치고, '네덜란드 실험 창고'의 장소 표현은 빼거나 미확인으로 둔다 — Emerald 게재 페이지의 발행일이 2026-02-24 이고 장소는 이번 확인 범위에 없다.",
    "f23·ref-1153: 기준일을 2026-04-23 이 아니라 발행일 미확인·접근일 2026-09-30 으로 적는다 — 브리프의 날짜 근거를 확인하지 못했다.",
    "f11·ref-031: 페이지에서 ref-031 의 직접 인용은 한 번만 쓰고 나머지는 재서술한다. 판은 VDA 5050 3.0.0 으로 밝힌다.",
    "원문 미열람 표기: 브리프에서 fetched false·source_unopened true 인 ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161, ref-959 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다.",
    "f21: 5절(물류창고)·6절에서 '[추정]'과 '벤더 주장'을 병기하고 교육 시간 효과를 사실처럼 쓰지 않는다.",
    "9절: f1·f2(법정 특별교육 실시), f23(사용자 측 운용·정비 요구), f3(조리로봇 청소·비상정지 안전)은 사업주·현장 조직·제조사가 맡는 연계 대상으로 짧게 쓰고 ROP 직접 범위처럼 서술하지 않는다(분류 원문 19장).",
    "용어 후보 '특별안전보건교육': 정의에서 '작업 내용을 바꿀 때'를 빼고 '산업안전보건법 시행규칙 별표 5 가 정한 유해·위험 작업(로봇작업 포함)의 근로자에게 사업주가 추가로 실시하는 안전보건교육'처럼 f1·f2 로 확인한 범위만 쓴다 — 작업내용 변경 시 교육은 별도 교육이며 이번 finding 이 뒷받침하지 않는다.",
    "5절: 병원(f7·f8·f9·f12·f13·f14·f17·f18)·상업 시설(f16)·물류창고(f19·f21)·제조 공장(f22)·기타(f3) 사례마다 현장 유형을 밝히고, 가정·실외 사례는 찾지 못했음을 명시한다. 병원 사례의 국가(에스토니아·한국·싱가포르·중국)와 기준일을 각각 밝힌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 3건, 교차 확인 1건(f12: 지디넷코리아·로봇신문). 강등: f3 사실 → 부분 강등(비상정지 버튼 교육·청소 시 안전·정기 교육 병행은 추정 또는 삭제), f9 사실 → 범위 축소(병원 현장 이기종 조율 삭제, 시험 환경 검증으로 한정), f17 사실 → 범위 축소(공공 의료기관의 등재 통합자 의무 사용 삭제). 원문 미열람 출처: ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161, ref-959(브리프 기준. 검증자가 ref-1150·ref-1199·ref-944·ref-872 는 이번에 열어 주장을 대조했고 ref-1153·ref-959 는 403, ref-1161 은 인증 리다이렉트로 검색 결과 일치만 확인). 발행일 정정: ref-1317 2025-07-23, ref-1320 2026-02-24, ref-872 2025-05-01. ref-1318 은 BSRIA 가이드 본문이 아니라 NBS 출판물 색인 설명 기준이다. 검증 검색 5회(리서치 13회 포함 합계 18회/30). 정정 요청 없음. 주의: 여러 제조사 로봇 플랫폼의 운영 이관 완료 기준·확대 절차를 정한 공개 표준은 확인되지 않았고, 핵심 질문에 대한 답(f24)과 책임 경계(f25·f26)는 구축자 추론([추정])이다. 사례 근거는 대부분 단일 출처이고 로봇 분야에 소프트 랜딩을 적용한 공개 사례는 없다. 가정·실외 현장 사례는 찾지 못했다.",
  "retry_reason": null
}
```

### runs/2026-09-30-21/pages.json

```json
{
  "run_id": "2026-09-30-21",
  "outline": [
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "단계적 인계 틀·단계적 시험 교훈·전담 운영 조직과 교육 사례·법정 로봇작업 특별교육은 있으나 다중 제조사 로봇 플랫폼의 이관 완료 기준·확대 절차 공개 표준은 확인되지 않았다. [추정][^ref-1318][^ref-1198]",
      "planned_findings": [
        "f24",
        "f15",
        "f14",
        "f16",
        "f4"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "소프트 랜딩(BSRIA BG 54/2018)은 인계 전·초기 사후 지원·연장 사후 지원을 포함한 여섯 단계 틀이고, 로봇작업 특별교육은 산업용 로봇에 한정되지 않는다. [사실][^ref-1318][^ref-1315]",
      "planned_findings": [
        "f5",
        "f1",
        "f2",
        "f12",
        "f16",
        "f10",
        "f11"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "병원(에스토니아·한국 사례와 싱가포르·중국 근거), 상업 시설, 물류창고(피킹), 제조 공장, 기타(학교 급식실) 사례를 여섯 항목으로 정리했고 가정·실외 사례는 찾지 못했다. [사실][^ref-1198][^ref-1317]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f12",
        "f13",
        "f14",
        "f15",
        "f17",
        "f18",
        "f16",
        "f19",
        "f21",
        "f22",
        "f3"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1400,
      "summary": "단계적 인계·사후 지원, 시뮬레이션→유사 공간→실제 구역 순 단계 시험, 설정 기반 플릿 추가, 전담 조직과 운영 인력 교육, 참여형 변화 관리·역할 배정이 대표 접근이다. [추정][^ref-1318][^ref-1198]",
      "planned_findings": [
        "f5",
        "f6",
        "f7",
        "f15",
        "f18",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f22",
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "별표 5 로봇작업 특별교육, ANSI/A3 R15.08-3-2026, BSRIA BG 54/2018, Open-RMF fleet_adapter_template, VDA 5050 3.0.0 팩트시트, RoMi-H 등재 프로그램이 관련된다. [사실][^ref-1315][^ref-1319]",
      "planned_findings": [
        "f1",
        "f2",
        "f23",
        "f5",
        "f10",
        "f11",
        "f17"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "병원 현장 시험(Valner 외 2022), 병동별 수용 차이(Mutlu·Forlizzi 2008), 호텔 사용 저항(Fu 외 2022), 협업 피킹 역할(Pasparakis 외 2026), 전문가 조사(Pietrantoni 외 2024), 급식 로봇 보고서(한국노동연구원 2024)가 대표 자료다. [사실][^ref-1198][^ref-1323]",
      "planned_findings": [
        "f3",
        "f7",
        "f14",
        "f16",
        "f19",
        "f20",
        "f18"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 설정 기반 로봇·현장 추가, 이관용 상태·설정·기록, 역할·권한, 확대 전후 성과 기록, 교육·시험용 시뮬레이션을 맡고 법정 교육·조작 교육·통합·인력 편성은 외부와 연계하는 것으로 보인다. [추정][^ref-1319][^ref-1315]",
      "planned_findings": [
        "f25",
        "f26",
        "f1",
        "f2",
        "f23",
        "f3"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1500,
      "summary": "이관 직전의 55. 현장 조사·설치·시운전, 새 로봇 추가의 4. 이기종 로봇 등록·20. 로봇·제조사 관제 연동, 수용성의 60. 노동·수용성·접근성, 적용 현장인 Q. 현장 유형별 적용 영역들과 이어진다. [추정][^ref-1198][^ref-1319]",
      "planned_findings": [
        "f27"
      ]
    },
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "서비스 로봇 운영 인력의 법정 교육 적용, 이관 완료 기준, 현장 간 재사용 비율, 관제 인력 직무 표준, 운영 책임 조직 위치(oq-266)가 열려 있다. [추정][^ref-1315]",
      "planned_findings": [
        "f4",
        "f6",
        "f10",
        "f13"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: seed → draft, 섹션 3~11 신규 작성(병원·상업 시설·물류창고·제조 공장·기타 사례, 조건부 승인 수정 14건 반영), 각주 18건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,411자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"6. 대표 접근법과 기술\" 절(1,317자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"4. 핵심 개념과 용어\" 절(1,116자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"8. 대표 연구와 자료\" 절(1,044자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(824자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"11. 열린 질문\" 절(779자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area56-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 56. 운영 이관·확대·교육 의 \"3. 왜 중요한가\" 절(676자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 56. 운영 이관·확대·교육 | 영역 심화: seed → draft, 3~11절 신규 작성(병원·상업 시설·물류창고·제조 공장·기타 사례, 조건부 승인 수정 14건 반영) | run 2026-09-30-21",
  "index_updates": {
    "home_recent": "2026-09-30 — 56. 운영 이관·확대·교육: 영역 심화 초안 작성(단계적 인계·사후 지원, 단계적 시험·확대, 설정 기반 플릿 추가, 운영 인력 교육, 로봇작업 특별교육, 현장 유형 사례 5종)",
    "category_recent": "2026-09-30 — 56. 운영 이관·확대·교육: 3~11절 신규 작성(병원·상업 시설·물류창고·제조 공장·기타 사례, 이관 완료 기준 공개 표준 미확인)",
    "area_recent": "2026-09-30 — 56. 운영 이관·확대·교육: 영역 심화, seed → draft, 섹션 3~11 신규 작성(실행 2026-09-30-21)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "soft-landings",
      "term_ko": "소프트 랜딩",
      "term_en": "Soft Landings (BSRIA BG 54)",
      "definition": "건축 프로젝트를 착수·요구 정의, 설계, 시공, 인계 전, 초기 사후 지원, 연장 사후 지원과 사용 후 평가의 여섯 단계로 나누어 시설을 운영 단계로 단계적으로 넘기는 BSRIA 프레임워크이다.",
      "description": "BG 54/2018(2018-08)이 2014년판을 대체했다. 출판물 색인 설명 기준이며 가이드 본문은 미열람이다. 로봇 운영 이관에 적용한 공개 사례는 확인되지 않았다.",
      "related_areas": [
        56,
        55
      ],
      "sources": [
        "ref-1318"
      ]
    },
    {
      "action": "new",
      "slug": "special-occupational-safety-and-health-training",
      "term_ko": "특별안전보건교육",
      "term_en": "Special Occupational Safety and Health Training (Korea)",
      "definition": "산업안전보건법 시행규칙 별표 5 가 정한 유해·위험 작업(로봇작업 포함)의 근로자에게 사업주가 추가로 실시하는 안전보건교육이다.",
      "description": "로봇작업 교육 내용은 로봇의 기본원리·구조와 작업방법, 이상 발생 시 응급조치, 안전시설과 안전기준, 조작방법과 작업순서이며, 법제처 해석(2023-11-21)상 로봇작업은 산업용 로봇 작업에 한정되지 않는다.",
      "related_areas": [
        56,
        50,
        59
      ],
      "sources": [
        "ref-1315"
      ]
    },
    {
      "action": "new",
      "slug": "post-occupancy-evaluation",
      "term_ko": "사용 후 평가",
      "term_en": "Post-Occupancy Evaluation (POE)",
      "definition": "시설이나 시스템을 넘겨받아 실제로 쓰기 시작한 뒤 성능과 사용자 경험을 점검해 개선점을 찾는 평가이다.",
      "description": "BSRIA 소프트 랜딩 프레임워크에서는 연장 사후 지원 단계와 함께 묶인다.",
      "related_areas": [
        56,
        39
      ],
      "sources": [
        "ref-1318"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 명세 원문(3.0.0). 이번에는 팩트시트 메시지의 목적과 factsheetRequest 즉시 동작을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1150",
      "org": "Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management)",
      "title": "The perils of hotel technology: The robot usage resistance model",
      "published": "2022",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 중국 고급 호텔 직원 면담으로 로봇 사용 저항 요인(역할 모호성, 추가 업무 등)을 정리한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1199",
      "org": "지디넷코리아",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 한림대학교성심병원 커맨드센터의 서비스 로봇 통합 운영을 다룬 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인)",
      "published": "2024-04",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 한림대학교성심병원의 서비스 로봇 운영과 커맨드센터 역할을 다룬 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008-03",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 병원 배송 로봇 TUG 의 병동별 수용 차이를 민족지로 분석한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1153",
      "org": "ANSI (The ANSI Blog)",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": null,
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 산업용 이동로봇 응용의 사용자 측 운용·정비 요구사항을 정한 ANSI/A3 R15.08-3-2026 소개 글.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-872",
      "org": "Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. RoMi-H 배치 역량을 연 2회 평가해 통합자를 인증하고 명단을 공개하는 싱가포르 병원 프로그램 안내(2026-08-24 갱신).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1161",
      "org": "Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16)",
      "title": "Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios",
      "published": "2026-04",
      "url": "https://www.nature.com/articles/s41598-026-49800-9",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 중국 3차 병원의 약품·검체 배송 AMR 10대를 6개월 병행 대조로 평가한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1315",
      "org": "법제처",
      "title": "로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872)",
      "published": "2023-11-21",
      "url": "https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업안전보건법 시행규칙 별표 5 특별교육 대상 로봇작업이 산업용 로봇 작업으로 한정되지 않는다는 법령해석과 로봇작업 교육내용.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1198",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원에서 RMF 기반 플릿 체계로 TIAGo 를 배치해 혈액 검체를 운반한 현장 시험과 교훈. 이기종 로봇 관리는 시험 환경에서 검증했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1317",
      "org": "주간한국",
      "title": "한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인)",
      "published": "2025-07-23",
      "url": "https://weekly.hankooki.com/news/articleView.html?idxno=7120747",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원과 한국장애인고용공단 경기남부직업능력개발원의 병원 로봇 운영 인력 양성 협약(2025-07-18) 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1318",
      "org": "BSRIA (NBS 출판물 색인)",
      "title": "BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings",
      "published": "2018-08",
      "url": "https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "건물 인계와 사후 지원을 여섯 단계로 정리한 BSRIA 소프트 랜딩 프레임워크의 출판물 색인 설명(본문은 유료, 색인 페이지만 열람).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1319",
      "org": "Open-RMF (open-rmf/fleet_adapter_template 저장소)",
      "title": "fleet_adapter_template README",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Python 기반 full_control 플릿 어댑터 참조 템플릿과 config.yaml 구성, 새 플릿 연동 절차.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1320",
      "org": "Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1))",
      "title": "In control or under control? Human–robot collaboration in warehouse order picking",
      "published": "2026-02-24",
      "url": "https://doi.org/10.1108/LORE-03-2025-0028",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실험 창고에서 사람 선도·로봇 선도 협업 피킹의 생산성·정확도를 비교한 연구(초록·요약 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1321",
      "org": "Locus Robotics",
      "title": "Locus Origin: Collaborative Robots Warehouse",
      "published": null,
      "url": "https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "Locus Origin 협업 피킹 로봇 제품 페이지. 신규 작업자 교육 시간과 다국어 지원에 관한 벤더 주장.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-959",
      "org": "한국노동연구원",
      "title": "음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13)",
      "published": "2024",
      "url": "https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 급식·조리 로봇 도입이 직무와 작업장 안전에 미친 영향을 분석하고 안전 관리체계·교육 필요를 지적한 보고서(403 으로 열지 못해 검색 요약 기준).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1323",
      "org": "Pietrantoni, L. 외 (Frontiers in Robotics and AI)",
      "title": "Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors",
      "published": "2024-12-02",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "유럽 9개국 전문가 31명의 혼합 방법 조사로 협동로봇 통합의 기술·안전·인적 요인(교육, 변화 저항)을 정리한 연구.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    },
    {
      "id": "ref-1324",
      "org": "로봇신문",
      "title": "한국로봇산업진흥원, 450억 규모 '2026년 로봇활용 제조혁신 지원사업' 착수",
      "published": "2026-05-12",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=46336",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "2026년 로봇활용 제조혁신 지원사업(국비 450억원)의 지원 내용과 선정기업 통합교육 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가?",
      "areas": [
        56,
        59,
        50
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "여러 제조사 로봇을 묶는 오케스트레이션 플랫폼을 구축 팀에서 운영 팀으로 넘길 때의 완료 기준(운영 인수 조건, 초기 사후 지원 기간, 지원 책임 이전 시점)을 정한 공개 표준이나 사례가 있는가?",
      "areas": [
        56,
        55
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "한 현장의 시범 운영을 다른 현장으로 넓힐 때 재사용되는 설정(지도·플릿 어댑터·능력 정의)과 현장마다 다시 해야 하는 작업의 비율이나 소요 시간을 측정한 연구가 있는가?",
      "areas": [
        56,
        55,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가?",
      "areas": [
        56,
        40,
        60
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시",
      "title": "56. 운영 이관·확대·교육"
    }
  ],
  "standards_updates": [
    {
      "name": "BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크)",
      "kind": "프레임워크",
      "org": "BSRIA",
      "url": "https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192",
      "related_areas": [
        56,
        55
      ],
      "summary": "건축 프로젝트를 착수·요구 정의부터 인계 전, 초기 사후 지원, 연장 사후 지원과 사용 후 평가까지 여섯 단계로 나눈 인계 틀(2018-08, 2014년판 대체). 출판물 색인 설명 기준이며 로봇 분야 적용 사례는 미확인이다.",
      "ref_id": "ref-1318"
    },
    {
      "name": "산업안전보건법 시행규칙 별표 5 로봇작업 특별교육",
      "kind": "프레임워크",
      "org": "법제처(법령해석 법제처-23-0872 경유)",
      "url": "https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638",
      "related_areas": [
        56,
        50,
        59
      ],
      "summary": "로봇작업 특별교육 내용(기본원리·구조와 작업방법, 이상 발생 시 응급조치, 안전시설과 안전기준, 조작방법과 작업순서)을 정하며, 법제처 해석(2023-11-21)상 대상 로봇작업은 산업용 로봇 작업에 한정되지 않는다.",
      "ref_id": "ref-1315"
    }
  ],
  "additional_research_requests": [
    "7절: 산업안전보건법 시행규칙 별표 4 의 로봇작업 특별교육 시간(국가법령정보센터 별표 원문) — 교육 기준의 핵심 수치이나 이번 브리프에서 확인하지 못했다.",
    "4·6절: BSRIA BG 54/2018 본문의 초기·연장 사후 지원 기간과 활동 — 색인 설명만 확인되어 기간을 미확인으로 두었다.",
    "6절: ITIL 4 초기 운영 지원(Early Life Support)·하이퍼케어 개념의 공식 자료 — 소프트웨어 운영 이관 틀로 비교가 필요하나 공식 자료를 열지 못했다.",
    "5절: 가정·실외 현장의 로봇 운영 이관·확대·교육 사례 — 두 현장 유형의 사례가 없다.",
    "5절: Mutlu·Forlizzi(2008) 연구 병원의 소재 국가와 연구 기간 — 이번 확인 범위에 없어 미확인으로 두었다.",
    "5·8절: 한국노동연구원 연구보고서 2024-13 원문의 교육 관련 세부 제언(비상정지 버튼 활용 교육, 로봇 청소 시 안전, 정기 교육) — 원문 미열람으로 본문에서 뺐다.",
    "5절: 한림대학교성심병원 커맨드센터가 실시간 모니터링·문제 대응을 맡는지에 대한 1차 자료 — 두 기사에서 확인하지 못했다.",
    "9절: 여러 제조사 로봇 플랫폼의 운영 이관 완료 기준·확대 절차를 정한 공개 표준이나 사례 — 책임 경계가 추정으로만 남아 있다."
  ],
  "fixes_applied": [
    "f9 범위 축소 — 5절 병원 사례(타르투) 수행 자원 칸·서술과 6절 설정 기반 플릿 추가, 8절 Valner 항목에서 '병원에서 서로 다른 로봇을 함께 조율'을 삭제하고, 이기종 관리(TIAGo·Clearpath Jackal)는 시험 환경 검증·병원 배치는 TIAGo·여러 배송 로봇의 병원 적용은 아직, 로봇 특성은 RMF 플릿 어댑터 설정 파일에 기술, FreeFleet 은 전용 플릿 관리자가 없는 로봇용으로 좁혀 썼다(검증 노트가 원문과 일치한다고 확인한 범위만 [사실]로 둠).",
    "f7 표현 수정 — 5절 서술에 'RMF 기반 플릿 체계로 TIAGo 로봇을 병원에 배치하면서'로 쓰고 수행 자원 칸도 TIAGo 로봇으로 적어 병원 배치 로봇이 TIAGo 였음을 드러냈다.",
    "f17 범위 축소 — 5절 병원 보충 서술과 7절 표에서 공공 의료기관의 등재 통합자 의무 사용 문구를 빼고 'CHART 가 연 2회 RoMi-H 배치 역량을 평가해 통합자를 인증하고 명단을 공개해 공공 의료기관이 제안요청(RFP/RFI)에 활용하게 한다'로 썼으며, ref-872 발행일을 2025-05-01 로 각주·reference_updates 에 적었다.",
    "f3 부분 강등 — 5절 기타(학교 급식실) 사례·8절에 검색 요약으로 확인된 부분(산업용·협동로봇 안전기준 밖, 식품위생법상 위생 규제만, 조리로봇 작업장 노동자 안전 관리체계 부재, 로봇 활용 교육 필요)만 [사실]로 쓰고, 비상정지 버튼 교육·청소 시 안전·정기 교육 병행 제언은 본문에서 빼고 '세부 제언 미확인'으로 적었으며, 현장 유형은 기타(학교 급식실)로 두고 다른 현장 유형으로 옮기지 않았다.",
    "f12 역할 수정 — 4·5·6절에서 커맨드센터 역할을 '로봇 운영 인프라 설정·변경, 시나리오별 프로세스 가이드, 병원 맞춤형 프로세스 구축, 활용 효과 정량 평가'로 쓰고 실시간 모니터링·문제 대응은 미확인으로 두었으며, 7종 73대는 2024 보도 기준임을 밝혔다.",
    "f13·ref-1317 날짜 수정 — 각주 발행일을 2025-07-23 으로 바꾸고 5·6절 본문 기준일을 2025-07-23 보도로, 11종 77대는 2025-07 보도 기준으로 밝혔다.",
    "f19·ref-1320 수정 — 발행일을 2026-02-24 로 각주·본문·reference_updates 에 고치고 '네덜란드' 장소 표현을 뺐다.",
    "f23·ref-1153 날짜 수정 — 7절 표에 '발행일 미확인, 확인일 2026-09-30, 원문 미열람'으로 적고 2026-04-23 기준일을 쓰지 않았다(각주 발행일 미확인).",
    "f11·ref-031 인용 — 페이지 전체에서 ref-031 직접 인용은 6절 한 곳('assist set-up of the mobile robot in fleet control')만 두고 4·7절은 재서술했으며, 판을 VDA 5050 3.0.0 으로 밝혔다.",
    "원문 미열람 표기 — ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161, ref-959 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 와 '원문 미열람. ' 요약 첫머리를 넣었다.",
    "f21 벤더 주장 — 5절 물류창고 사례(수행 자원 칸·서술)와 6절 참여형 변화 관리에서 '[추정] 벤더 주장'을 병기하고 독립 측정이 없음을 밝혀 교육 시간 효과를 사실처럼 쓰지 않았다.",
    "9절 경계 — 법정 특별교육 실시(f1·f2), 사용자 측 운용·정비 요구(f23), 조리로봇 청소·비상정지 안전(f3)을 표의 '외부와 연계하는 것' 칸에 '연계 대상'으로 짧게 두고 ROP 직접 범위 칸에는 역할·권한 반영과 기록 제공만 적었다.",
    "용어 '특별안전보건교육' 정의 — glossary_updates 정의에서 '작업 내용을 바꿀 때'를 빼고 '별표 5 가 정한 유해·위험 작업(로봇작업 포함)의 근로자에게 사업주가 추가로 실시하는 안전보건교육'으로 f1·f2 범위만 썼다.",
    "5절 현장 유형 명시 — 병원(에스토니아 타르투·한국 한림대학교성심병원 표, 싱가포르 2025-05-01·중국 2026-04 보충 서술, TUG 연구는 국가 미확인 명시)·상업 시설·물류창고(피킹)·제조 공장·기타(학교 급식실) 사례마다 현장 유형 줄을 두고 기준일을 밝혔으며, 절 첫머리에 가정·실외 사례를 찾지 못했음을 적었다.",
    "분량 초과 자동 분리: 56. 운영 이관·확대·교육 본문 11,512자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,288자"
  ]
}
```

### runs/2026-09-30-21/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area56-s10.md (1,411자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area56-s6.md (1,317자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area56-s4.md (1,116자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area56-s8.md (1,044자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area56-s7.md (824자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area56-s11.md (779자)
    - docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area56-s3.md (676자)
```

### runs/2026-09-30-21/pages/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md

```markdown
---
title: "56. 운영 이관·확대·교육"
type: area
category: "O. 검증·도입·수명주기"
area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [운영 이관, 소프트 랜딩, 로봇작업 특별교육, 단계적 확대, 변화 관리, 운영 인력 교육]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161, ref-1315, ref-1198, ref-1317, ref-1318, ref-1319, ref-1320, ref-1321, ref-959, ref-1323, ref-1324]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [O. 검증·도입·수명주기](index.md) › 56. 운영 이관·확대·교육

# 56. 운영 이관·확대·교육

!!! info "소속 대분류"
    [O. 검증·도입·수명주기](index.md) — 핵심 질문:
    만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

운영 이관·지원, 단계적 확대, 교육·변화 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 이관·지원 체계**: 구축 팀에서 운영 팀으로 넘기고 지원·장애 대응 체계를 정한다
- **단계적 확대**: 시범 운영에서 넓혀 가며 새 현장과 새 로봇을 추가한다
- **사용자 교육·변화 관리**: 운영자·작업자를 교육하고 일하는 방식의 변화를 관리한다

## 2. 핵심 질문

시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가? [분류원문]

## 3. 왜 중요한가

시범 운영을 넓힐 때 운영을 누구에게 넘기고 사람을 어떻게 준비시킬지에 관해, 확인한 자료에는 건물 분야의 단계적 인계 틀, 단계적 시험·확대 교훈, 전담 운영 조직과 운영 인력 교육 사례, 법정 로봇작업 특별교육이 있으나 여러 제조사 로봇을 묶는 플랫폼의 운영 이관 완료 기준이나 확대 절차를 정한 공개 표준은 확인되지 않았다. [추정][^ref-1318][^ref-1198][^ref-1199][^ref-1317][^ref-1315]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 왜 중요한가](../../topics/2026/2026-09-30-area56-s3.md)에 있다.

## 4. 핵심 개념과 용어

운영 이관·확대·교육을 이해하는 데 필요한 용어는 인계 틀, 법정 교육, 운영 조직, 확대 수단에 걸쳐 있다. [의견][^ref-1318][^ref-1315]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area56-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

운영 이관·확대·교육의 사례는 병원에 가장 많고, 상업 시설·물류창고·제조 공장·기타 현장의 근거가 뒤따른다. 가정·실외 현장의 운영 이관·교육 사례는 이번 조사에서 찾지 못했다. [사실][^ref-1198][^ref-1150]

**현장 유형:** 병원

**사례:** 병원(에스토니아 타르투 대학병원)에서 집중치료실의 혈액 검체를 검사실로 운반하는 로봇을 단계적으로 시험·배치

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료진이 로봇에 달린 터치스크린으로 운반 요청을 시작한다. [사실][^ref-1198] |
| 작업 대상 | 집중치료실에서 검사실로 보내는 혈액 검체. [사실][^ref-1198] |
| 수행 자원 | Open-RMF 기반 플릿 체계로 배치한 TIAGo 로봇과 의료진이 맡는다. 로봇 특성은 RMF 플릿 어댑터 설정 파일에 기술한다. [사실][^ref-1198] |
| 제약 | 의료진이 로봇을 멈추고 비킬 수 있어야 한다는 점이 필수 조건으로 꼽혔다. [사실][^ref-1198] |
| 완료·인계 | 의료진이 검체를 통에 넣은 뒤 버튼 하나로 확인하는 수동 인계. [사실][^ref-1198] |
| 예외·성과 | 시뮬레이션, 비슷한 물리 공간, 실제 배치 구역 순서로 시험해 현장 시험 시간을 아끼고 문제를 일찍 찾으라는 교훈이 보고되었다(2022-08-23). [사실][^ref-1198] |

Valner 외(2022)는 RMF 기반 플릿 체계로 TIAGo 로봇을 병원에 배치하면서 이 교훈을 보고했다. [사실][^ref-1198] 저자들은 서로 다른 로봇(TIAGo·Clearpath Jackal)을 RMF 로 관리하는 것은 시험 환경에서 검증했고, 여러 배송 로봇을 병원에 적용하는 것은 아직이라고 밝혔다. [사실][^ref-1198] 이 사례에서 56. 운영 이관·확대·교육이 관여하는 부분은 확대 전 시험 순서와, 의료진이 새로 맡는 요청·정지·인계 조작이다. [의견][^ref-1198]

**현장 유형:** 병원

**사례:** 병원(한국 한림대학교성심병원)에서 서비스 로봇 운영을 전담 조직에 맡기고 운영 인력을 양성

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 병원의 서비스 로봇 운영 업무. 로봇 규모는 2024 보도 기준 7종 73대 [사실][^ref-1199][^ref-944], 2025-07 보도 기준 11종 77대(2022-08부터 운영)다. [사실][^ref-1317] |
| 수행 자원 | 전담 부서인 커맨드센터가 통합 관제로 운영하며, 보도된 역할은 로봇 운영 인프라 설정·변경, 시나리오별 프로세스 가이드, 병원 맞춤형 프로세스 구축, 활용 효과 정량 평가다. [사실][^ref-1199][^ref-944] 2025-07-18 한국장애인고용공단 경기남부직업능력개발원과 협약을 맺고 로봇 상태 점검·에러 대응·관제화면 모니터링을 맡을 운영 인력의 실무 중심 교육 과정을 함께 만들기로 했다(2025-07-23 보도). [사실][^ref-1317] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 에러 대응 절차가 운영 인력 교육 과정의 초점 가운데 하나다. [사실][^ref-1317] 커맨드센터가 실시간 모니터링·문제 대응을 맡는지는 이번 확인 범위에서 미확인이다. |

이 사례는 의료진이 아니라 전담 조직과 교육받은 운영 인력에게 로봇 운영을 넘긴 형태다. [사실][^ref-1199][^ref-1317] 두 보도의 로봇 규모 차이는 시점이 다른 수치이므로 모순이 아니다. [의견][^ref-1199][^ref-1317]

병원 확대에는 다른 근거도 있다. Mutlu·Forlizzi(HRI 2008)의 민족지 연구에서는 같은 병원의 자율 배송 로봇(TUG)이 병동에 따라 저항을 낳거나 업무에 통합되었다(병원 소재 국가 미확인). [사실][^ref-1151] 싱가포르 창이종합병원의 CHART 는 연 2회 의료 로봇 미들웨어 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md) 배치 역량을 평가해 통합자를 인증하고 명단을 공개해 공공 의료기관이 제안요청(RFP/RFI)에 활용하게 한다(2025-05-01 게시). [사실][^ref-872] 중국 3차 병원에서는 약품·검체 배송 자율이동로봇(Autonomous Mobile Robot, AMR) 10대를 6개월 동안 수작업과 병행 대조로 평가해 배송 시간이 32~36% 줄었다는 보고가 있다(2026-04). [사실][^ref-1161] 이런 근거로 보면 단계적 확대에서는 단위마다 업무 흐름·수용성을 다시 확인하고 시험 단계를 거쳐야 할 것으로 보인다. [추정][^ref-1151][^ref-1198]

**현장 유형:** 상업 시설

**사례:** 상업 시설(중국 고급 호텔)에서 로봇을 들인 뒤 현장 직원이 운영·교육을 떠맡는 경우

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼다(직원 19명 면담, 2022). [사실][^ref-1150] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 근무 중 로봇 교육·동료 교육·고장 처리 같은 추가 업무가 로봇 사용 저항으로 이어졌다. [사실][^ref-1150] |

이 사례는 운영 이관을 받을 조직이 정해지지 않으면 교육과 고장 처리가 현장 직원의 추가 업무로 남는다는 점을 보여 준다. [의견][^ref-1150]

**현장 유형:** 물류창고

**사례:** 물류창고(피킹 단계) 실험 창고에서 작업자와 협업 로봇의 선도 역할 배정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 실험 창고의 피킹 위치 300곳에서 주문 품목을 피킹한다. [사실][^ref-1320] |
| 수행 자원 | 직업학교 학생 60명이 협업 로봇과 함께 사람 선도 또는 로봇 선도 방식으로 일했다. [사실][^ref-1320] 신규 작업자가 태블릿 화면 덕분에 몇 분 안에 생산적으로 일할 수 있고 수십 개 언어를 지원한다는 업체 주장도 있으나 독립 측정은 확인되지 않았다. [추정] 벤더 주장[^ref-1321] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 사람이 로봇을 이끌면 생산성이 높고 오류가 많았으며, 로봇이 올바른 피킹 위치에 멈춰 사람을 이끌면 정확도가 높았다(2026-02-24 발행). [사실][^ref-1320] |

Pasparakis·De Vries·De Koster 는 속도·정확도 우선순위와 작업자 성향에 맞춰 역할을 배정하라고 제언했다. [사실][^ref-1320] 교육 시간 단축에 관한 업체 주장은 이 실험과 별개이며 효과로 확인된 것이 아니다. [추정] 벤더 주장[^ref-1321]

**현장 유형:** 제조 공장

**사례:** 제조 공장(한국) 로봇 도입 지원사업 참여 기업의 도입·교육

| 항목 | 내용 |
|---|---|
| 시작 조건 | 한국로봇산업진흥원의 2026년 로봇활용 제조혁신 지원사업(국비 450억원) 과제 선정. [사실][^ref-1324] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 사업은 로봇 자동화 시스템 도입비용과 컨설팅·로봇 교육을 지원하며, 선정 과제 컨소시엄 담당자 400여명에게 사업 관리지침·안전 컨설팅·현장 감리 점검사항 통합교육을 했다(2026-05-12 보도). [사실][^ref-1324] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례에서 교육은 도입 지원 사업의 한 구성 요소로 묶여 있다. [사실][^ref-1324]

**현장 유형:** 기타

**사례:** 기타 현장(한국 학교 급식실)에서 조리로봇을 들인 작업장의 안전 관리와 교육

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 로봇 활용 교육이 필요하다고 지적되었다(2024). [사실][^ref-959] |
| 제약 | 서비스 로봇은 산업용 로봇·협동로봇 안전기준을 받지 않고 식품위생법상 위생 규제만 받으며, 조리로봇을 도입한 작업장에 노동자 안전 관리체계가 없다고 지적되었다. [사실][^ref-959] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

근거인 한국노동연구원 보고서(2024-13)는 원문을 열지 못해 검색 요약으로 확인한 범위만 썼고, 교육 방식에 관한 세부 제언은 미확인이다. [사실][^ref-959]

## 6. 대표 접근법과 기술

확인한 접근법은 단계적 인계와 사후 지원, 단계적 시험·확대, 설정 기반 플릿 추가, 전담 조직과 운영 인력 교육, 참여형 변화 관리의 다섯 갈래다. [추정][^ref-1318][^ref-1198][^ref-1319][^ref-1317][^ref-1323]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area56-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 직접 걸리는 기준은 법정 교육, 사용자 측 운용 표준, 인계 프레임워크, 새 플릿 연동 도구로 나뉜다. [추정][^ref-1315][^ref-1153][^ref-1318][^ref-1319]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area56-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 병원 현장 시험과 조직 연구, 협업 피킹 실험, 전문가 조사, 국내 급식 로봇 보고서다. [사실][^ref-1198][^ref-1151][^ref-1320][^ref-1323][^ref-959]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 대표 연구와 자료](../../topics/2026/2026-09-30-area56-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 새 로봇·플릿·현장 추가를 반복 가능하게 하고 이관에 필요한 상태·기록·역할을 제공하는 쪽을 맡고, 교육 실시·조작 교육·통합·인력 편성은 외부와 연계하는 것으로 보인다. [추정][^ref-1319][^ref-031][^ref-1315]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 새 플릿·로봇 추가를 설정 파일과 팩트시트 기반 등록으로 반복 가능하게 하고, 교육·시험에 쓸 시뮬레이션 모드를 제공한다. [추정][^ref-1319][^ref-031][^ref-1198] | 연계 대상: 로봇 조작·정비 교육(제조사), 조리로봇 청소·비상정지 같은 로봇·설비 자체 안전. [추정][^ref-1315][^ref-959] |
| 업종별 조건 | 법정 교육·작업 지침에서 나온 조건을 운영자 역할과 권한 정의로 반영하고, 이관 때 넘길 운영 상태·설정·인계 기록과 단계적 확대 전후의 성과 기록을 제공한다. [추정][^ref-1199][^ref-1198] | 연계 대상: 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 실시와 작업 지침(사업주), ANSI/A3 R15.08-3 의 사용자 측 운용·정비 요구(사용자 현장 조직), 식품위생 규제(급식 현장). [추정][^ref-1315][^ref-1153][^ref-959] |

분류 원문 19장의 다섯 경계 밖에서도 연계가 있다. 통합자 인증과 현장 통합은 통합자가, 인력 편성·직무 설계·노사 협의는 현장 조직·인사가 맡으므로 ROP는 그들에게 운영 상태·교육용 자료·기록을 제공하고 역할·권한을 반영하는 쪽을 맡는 것으로 보인다. [추정][^ref-872][^ref-1323] 이 경계는 제품 전략에 따라 움직일 수 있으며, 이종 제조사를 연결하는 ROP는 로봇 조작 교육을 제조사에 맡기고 여러 로봇을 한 체계로 운영하는 데 필요한 인터페이스와 기록을 맡는 형태가 될 것으로 보인다. [추정][^ref-1319] 범위 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 이관 직전의 시운전, 새 로봇 추가, 운영 조직, 법정 교육, 수용성, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1198][^ref-1319][^ref-1315]

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area56-s10.md)에 있다.

## 11. 열린 질문

운영 이관 완료 기준과 교육 의무 범위처럼 이번 조사에서 답을 찾지 못한 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [56. 운영 이관·확대·교육 — 열린 질문](../../topics/2026/2026-09-30-area56-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30 (원문 미열람)
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1153]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1161]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30 (원문 미열람)
[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-1198]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1317]: 주간한국, 한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인), 2025-07-23, https://weekly.hankooki.com/news/articleView.html?idxno=7120747, 접근일 2026-09-30
[^ref-1318]: BSRIA (NBS 출판물 색인), BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings, 2018-08, https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192, 접근일 2026-09-30
[^ref-1319]: Open-RMF (open-rmf/fleet_adapter_template 저장소), fleet_adapter_template README, 미확인, https://github.com/open-rmf/fleet_adapter_template, 접근일 2026-09-30
[^ref-1320]: Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1)), In control or under control? Human–robot collaboration in warehouse order picking, 2026-02-24, https://doi.org/10.1108/LORE-03-2025-0028, 접근일 2026-09-30
[^ref-1321]: Locus Robotics, Locus Origin: Collaborative Robots Warehouse, 미확인, https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot, 접근일 2026-09-30
[^ref-959]: 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13), 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1323]: Pietrantoni, L. 외 (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/, 접근일 2026-09-30
[^ref-1324]: 로봇신문, 한국로봇산업진흥원, 450억 규모 '2026년 로봇활용 제조혁신 지원사업' 착수, 2026-05-12, https://www.irobotnews.com/news/articleView.html?idxno=46336, 접근일 2026-09-30
```

### docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md

```markdown
---
title: "56. 운영 이관·확대·교육"
type: area
category: "O. 검증·도입·수명주기"
area_no: 56
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [O. 검증·도입·수명주기](index.md) › 56. 운영 이관·확대·교육

# 56. 운영 이관·확대·교육

!!! info "소속 대분류"
    [O. 검증·도입·수명주기](index.md) — 핵심 질문:
    만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

운영 이관·지원, 단계적 확대, 교육·변화 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 이관·지원 체계**: 구축 팀에서 운영 팀으로 넘기고 지원·장애 대응 체계를 정한다
- **단계적 확대**: 시범 운영에서 넓혀 가며 새 현장과 새 로봇을 추가한다
- **사용자 교육·변화 관리**: 운영자·작업자를 교육하고 일하는 방식의 변화를 관리한다

## 2. 핵심 질문

시범 운영을 넓히면서 운영을 누구에게 어떻게 넘기고 사람을 어떻게 준비시킬 것인가? [분류원문]

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

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s10.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 다른 연구영역과의 연결"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1150, ref-1199, ref-944, ref-1151, ref-1153, ref-872, ref-1161, ref-1315, ref-1198, ref-1317, ref-1319, ref-1320, ref-1321, ref-959, ref-1323, ref-1324]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#10
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 다른 연구영역과의 연결

# 56. 운영 이관·확대·교육 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 이관 직전의 시운전, 새 로봇 추가, 운영 조직, 법정 교육, 수용성, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1198][^ref-1319][^ref-1315]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 이관 직전의 시운전, 새 로봇 추가, 운영 조직, 법정 교육, 수용성, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1198][^ref-1319][^ref-1315]

- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 이관 직전 단계이며, 시운전을 마친 시스템을 운영 쪽으로 넘기는 경계가 두 영역 사이에 있다. [추정][^ref-1198]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 시뮬레이션부터 실제 구역까지 단계적으로 시험하라는 교훈이 두 영역에 걸친다. [추정][^ref-1198]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 이관 뒤 버전·장비를 바꿀 때 플릿 어댑터 설정을 다시 다루게 된다. [추정][^ref-1319]
- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 새 로봇 추가를 설정과 팩트시트 기반 등록으로 반복 가능하게 하는 일이 확대의 반복 작업을 줄인다. [추정][^ref-1319][^ref-031]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 새 플릿을 붙일 때 제조사 관제 API 연결을 채우는 플릿 어댑터가 두 영역에 걸친다. [추정][^ref-1319][^ref-1198]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — VDA 5050 팩트시트가 관제의 로봇 설정을 돕는 표준 메시지다. [추정][^ref-031]
- [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) — 전담 운영 조직의 프로세스 가이드·병원 맞춤형 프로세스 구축이 운영 절차와 겹친다. [추정][^ref-1199][^ref-944]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 운영 인력 교육이 관제화면 모니터링을 다룬다. [추정][^ref-1317]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 확대 때 작업자와 로봇의 선도 역할을 우선순위와 작업자 성향에 맞춰 배정하는 문제가 이어진다. [추정][^ref-1320]
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 확대 전후 효과를 수작업과 병행 대조로 평가한 사례가 있다. [추정][^ref-1161]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 로봇작업 특별교육과 ANSI/A3 R15.08-3 의 사용자 측 요구가 교육 내용의 기준이 된다. [추정][^ref-1315][^ref-1153]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 법정 교육의 적용 범위와 서비스 로봇 규제 공백이 법·규제의 질문으로 이어진다. [추정][^ref-1315][^ref-959]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 통합자 인증·명단 공개 같은 통합자 선정이 사업자 간 책임 분담으로 이어진다. [추정][^ref-872]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 역할 모호성, 일자리 대체 우려, 이점 이해 부족이 변화 저항 요인으로 보고되었다. [추정][^ref-1150][^ref-1323]
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 도입비용·컨설팅·로봇 교육을 함께 지원하는 정부 지원사업처럼 교육이 조달·지원에 묶이는 경우가 있다. [추정][^ref-1324]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 협업 피킹의 역할 배정 실험과 신규 작업자 교육에 관한 업체 주장이 있다. [추정][^ref-1320][^ref-1321]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 제조혁신 지원사업의 컨소시엄 통합교육 사례가 있다. [추정][^ref-1324]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 검체 운반 현장 시험, 전담 운영 조직, 운영 인력 양성, 병동별 수용 차이, 통합자 등재, 배송 성과 평가가 모두 병원 근거다. [추정][^ref-1198][^ref-1199][^ref-1317][^ref-1151][^ref-872][^ref-1161]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 호텔 로봇의 소속 부서 불분명과 추가 업무가 저항으로 이어진 사례가 있다. [추정][^ref-1150]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 학교 급식실 조리로봇의 안전 관리체계와 교육 공백이 지적되었다. [추정][^ref-959]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30 (원문 미열람)
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1153]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1161]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30 (원문 미열람)
[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-1198]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1317]: 주간한국, 한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인), 2025-07-23, https://weekly.hankooki.com/news/articleView.html?idxno=7120747, 접근일 2026-09-30
[^ref-1319]: Open-RMF (open-rmf/fleet_adapter_template 저장소), fleet_adapter_template README, 미확인, https://github.com/open-rmf/fleet_adapter_template, 접근일 2026-09-30
[^ref-1320]: Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1)), In control or under control? Human–robot collaboration in warehouse order picking, 2026-02-24, https://doi.org/10.1108/LORE-03-2025-0028, 접근일 2026-09-30
[^ref-1321]: Locus Robotics, Locus Origin: Collaborative Robots Warehouse, 미확인, https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot, 접근일 2026-09-30
[^ref-959]: 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13), 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1323]: Pietrantoni, L. 외 (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/, 접근일 2026-09-30
[^ref-1324]: 로봇신문, 한국로봇산업진흥원, 450억 규모 '2026년 로봇활용 제조혁신 지원사업' 착수, 2026-05-12, https://www.irobotnews.com/news/articleView.html?idxno=46336, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s6.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 대표 접근법과 기술"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1199, ref-944, ref-1151, ref-1161, ref-1198, ref-1317, ref-1318, ref-1319, ref-1320, ref-1321, ref-1323, ref-1324]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#6
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 대표 접근법과 기술

# 56. 운영 이관·확대·교육 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 접근법은 단계적 인계와 사후 지원, 단계적 시험·확대, 설정 기반 플릿 추가, 전담 조직과 운영 인력 교육, 참여형 변화 관리의 다섯 갈래다. [추정][^ref-1318][^ref-1198][^ref-1319][^ref-1317][^ref-1323]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 접근법은 단계적 인계와 사후 지원, 단계적 시험·확대, 설정 기반 플릿 추가, 전담 조직과 운영 인력 교육, 참여형 변화 관리의 다섯 갈래다. [추정][^ref-1318][^ref-1198][^ref-1319][^ref-1317][^ref-1323]

### 단계적 인계와 초기 사후 지원

소프트 랜딩 프레임워크는 인계 전 단계와 인계 뒤 초기·연장 사후 지원을 프로젝트 단계로 둔다. [사실][^ref-1318] 인계 전 준비와 인계 뒤 사후 지원을 구축 측이 함께 맡는 이런 방식은 구축 팀에서 운영 팀으로 로봇 운영을 넘기는 이관에 참고할 수 있을 것으로 보이나, 로봇 오케스트레이션 플랫폼에 적용한 공개 사례는 찾지 못했다. [추정][^ref-1318]

### 시뮬레이션에서 실제 구역까지 단계적 시험·확대

병원 현장 시험은 시뮬레이션, 비슷한 물리 공간, 실제 배치 구역 순서로 시험하라는 교훈을 남겼다. [사실][^ref-1198] 확대 효과는 수작업과 병행 대조로 평가한 사례가 있다(중국 3차 병원, 배송 시간 32~36% 감소). [사실][^ref-1161] 다만 병동마다 수용 결과가 갈린 사례가 있어 단위마다 다시 확인해야 할 것으로 보인다. [추정][^ref-1151][^ref-1198]

### 설정 기반 플릿·로봇 추가

Open-RMF 의 fleet_adapter_template 은 Python 기반 전체 제어(full_control) 플릿 어댑터의 참조 구현으로, 새 플릿을 붙일 때 RobotClientAPI.py 의 API 호출 부분을 채우고 config.yaml 의 rmf_fleet(로봇 파라미터)·fleet_manager(관제 API 연결)·reference_coordinates(좌표 변환) 세 절을 설정하게 한다. [사실][^ref-1319] 병원 현장 시험에서도 로봇 특성은 플릿 어댑터 설정 파일에 기술했고, FreeFleet 은 제조사 전용 플릿 관리자가 없는 로봇에 쓰였다. [사실][^ref-1198] VDA 5050 3.0.0 은 팩트시트를 “assist set-up of the mobile robot in fleet control” 하는 정보로 둔다. [사실][^ref-031] 새 현장마다 다시 해야 하는 작업의 비율은 측정 자료를 찾지 못했다.

### 운영 전담 조직과 운영 인력 교육

한국의 한 병원은 커맨드센터라는 전담 부서가 로봇을 통합 관제로 운영한다(2024 보도 기준). [사실][^ref-1199][^ref-944] 같은 병원은 장애인 직업능력개발 기관과 로봇 상태 점검·에러 대응·관제화면 모니터링 중심의 운영 인력 교육 과정을 만들기로 했다(2025-07-23 보도). [사실][^ref-1317] 제조 분야에서는 정부 도입 지원사업이 로봇 교육을 함께 지원한다(2026-05-12 보도). [사실][^ref-1324]

### 참여형 변화 관리와 역할 배정

Pietrantoni 외(2024-12-02)가 유럽 9개국 전문가 31명을 조사한 결과, 전문가들은 포괄적 안전 교육, 사용하기 쉬운 인터페이스, 지속적 직업 훈련을 필수로 보았고, 일자리 대체 우려와 이점 이해 부족을 변화 저항의 원인으로, 효과적 소통과 리더십 지원을 대응책으로 들었다. [사실][^ref-1323] 협업 피킹 실험은 속도·정확도 우선순위와 작업자 성향에 맞춘 역할 배정을 제언했다. [사실][^ref-1320] 화면 설계로 신규 작업자 교육을 몇 분 수준으로 줄인다는 주장은 업체 자료뿐이다. [추정] 벤더 주장[^ref-1321]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1161]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30 (원문 미열람)
[^ref-1198]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1317]: 주간한국, 한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인), 2025-07-23, https://weekly.hankooki.com/news/articleView.html?idxno=7120747, 접근일 2026-09-30
[^ref-1318]: BSRIA (NBS 출판물 색인), BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings, 2018-08, https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192, 접근일 2026-09-30
[^ref-1319]: Open-RMF (open-rmf/fleet_adapter_template 저장소), fleet_adapter_template README, 미확인, https://github.com/open-rmf/fleet_adapter_template, 접근일 2026-09-30
[^ref-1320]: Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1)), In control or under control? Human–robot collaboration in warehouse order picking, 2026-02-24, https://doi.org/10.1108/LORE-03-2025-0028, 접근일 2026-09-30
[^ref-1321]: Locus Robotics, Locus Origin: Collaborative Robots Warehouse, 미확인, https://locusrobotics.com/locusone/fleet/locus-origin-collaborative-robot, 접근일 2026-09-30
[^ref-1323]: Pietrantoni, L. 외 (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/, 접근일 2026-09-30
[^ref-1324]: 로봇신문, 한국로봇산업진흥원, 450억 규모 '2026년 로봇활용 제조혁신 지원사업' 착수, 2026-05-12, https://www.irobotnews.com/news/articleView.html?idxno=46336, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s4.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 핵심 개념과 용어"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1150, ref-1199, ref-944, ref-1315, ref-1318, ref-1319]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#4
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 핵심 개념과 용어

# 56. 운영 이관·확대·교육 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 운영 이관·확대·교육을 이해하는 데 필요한 용어는 인계 틀, 법정 교육, 운영 조직, 확대 수단에 걸쳐 있다. [의견][^ref-1318][^ref-1315]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

운영 이관·확대·교육을 이해하는 데 필요한 용어는 인계 틀, 법정 교육, 운영 조직, 확대 수단에 걸쳐 있다. [의견][^ref-1318][^ref-1315]

- **소프트 랜딩(Soft Landings)** — BSRIA 가이드 BG 54/2018(2018-08)은 건축 프로젝트를 착수·요구 정의, 설계, 시공, 인계 전, 초기 사후 지원, 연장 사후 지원과 사용 후 평가의 여섯 단계로 나누며 2014년판을 대체한다(출판물 색인 설명 기준). [사실][^ref-1318]
- **초기·연장 사후 지원(Initial / Extended Aftercare)** — 소프트 랜딩에서 인계 뒤에 두는 두 단계이며, 연장 사후 지원은 사용 후 평가(Post-Occupancy Evaluation, POE)와 함께 묶인다. [사실][^ref-1318] 단계별 기간은 원문을 열지 못해 미확인이다.
- **로봇작업 특별교육** — 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상이며, 교육 내용은 로봇의 기본원리·구조와 작업방법, 이상 발생 시 응급조치, 안전시설과 안전기준, 조작방법과 작업순서다. [사실][^ref-1315] 법제처는 2023-11-21 법령해석(법제처-23-0872)에서 이 로봇작업이 산업용 로봇을 사용하는 작업으로 한정되지 않는다고 회신했다. [사실][^ref-1315]
- **운영 전담 조직(커맨드센터)** — 한국의 한 병원은 전담 부서인 커맨드센터가 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다(2024 보도 기준). [사실][^ref-1199][^ref-944]
- **역할 모호성(Role Ambiguity)** — 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생긴 상태로, 호텔 직원 연구에서 사용 저항 요인으로 보고되었다. [사실][^ref-1150]
- **[플릿 어댑터](../../glossary/fleet-adapter.md)(Fleet Adapter)** — Open-RMF 의 fleet_adapter_template 은 새 플릿을 붙일 때 제조사 관제 API 호출 부분을 채우고 로봇 파라미터·관제 API 연결·좌표 변환을 설정 파일에 적게 하는 참조 구현이다(확인일 2026-09-30). [사실][^ref-1319]
- **[VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)(factsheet)** — VDA 5050 3.0.0 에서 플릿 관제가 이동로봇을 설정하는 데 도움이 되는 파라미터와 제조사별 정보를 담는 메시지이며, 관제가 factsheetRequest 즉시 동작으로 요청하면 로봇이 보낸다. [사실][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30 (원문 미열람)
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30 (원문 미열람)
[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-1318]: BSRIA (NBS 출판물 색인), BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings, 2018-08, https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192, 접근일 2026-09-30
[^ref-1319]: Open-RMF (open-rmf/fleet_adapter_template 저장소), fleet_adapter_template README, 미확인, https://github.com/open-rmf/fleet_adapter_template, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s8.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 대표 연구와 자료"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1150, ref-1151, ref-1161, ref-1198, ref-1320, ref-959, ref-1323]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#8
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 대표 연구와 자료

# 56. 운영 이관·확대·교육 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 병원 현장 시험과 조직 연구, 협업 피킹 실험, 전문가 조사, 국내 급식 로봇 보고서다. [사실][^ref-1198][^ref-1151][^ref-1320][^ref-1323][^ref-959]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 병원 현장 시험과 조직 연구, 협업 피킹 실험, 전문가 조사, 국내 급식 로봇 보고서다. [사실][^ref-1198][^ref-1151][^ref-1320][^ref-1323][^ref-959]

- Valner 외, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments(2022) — 에스토니아 병원에서 TIAGo 로 혈액 검체 운반을 현장 시험하고 단계적 시험 교훈을 정리했으며, 이기종 로봇 관리는 시험 환경에서 검증했다. [사실][^ref-1198]
- Mutlu·Forlizzi, Robots in Organizations(HRI 2008) — 병원 배송 로봇의 수용이 병동의 업무 흐름·사회적 맥락에 따라 갈렸음을 보였다. [사실][^ref-1151]
- Fu·Zheng·Wong, The perils of hotel technology(2022) — 호텔 직원 면담으로 역할 모호성과 추가 업무를 로봇 사용 저항 요인으로 정리했다. [사실][^ref-1150]
- Pasparakis·De Vries·De Koster, In control or under control?(Logistics Research, 2026-02-24) — 협업 피킹에서 사람 선도는 생산성, 로봇 선도는 정확도에 유리했다. [사실][^ref-1320]
- Pietrantoni 외, Integrating collaborative robots in manufacturing, logistics, and agriculture(2024-12-02) — 교육·지속 훈련과 변화 저항 요인·대응책을 전문가 조사로 정리했다. [사실][^ref-1323]
- Li 외, Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios(Scientific Reports, 2026-04) — 병원 배송 AMR 의 효과를 병행 대조로 평가했다. [사실][^ref-1161]
- 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향(연구보고서 2024-13) — 서비스 로봇의 안전기준 공백과 교육 필요를 지적했다(원문 미열람). [사실][^ref-959]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1161]: Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios, 2026-04, https://www.nature.com/articles/s41598-026-49800-9, 접근일 2026-09-30 (원문 미열람)
[^ref-1198]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1320]: Pasparakis, A., De Vries, J., & De Koster, R. (Logistics Research 19(1)), In control or under control? Human–robot collaboration in warehouse order picking, 2026-02-24, https://doi.org/10.1108/LORE-03-2025-0028, 접근일 2026-09-30
[^ref-959]: 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13), 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1323]: Pietrantoni, L. 외 (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s7.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1153, ref-872, ref-1315, ref-1318, ref-1319]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#7
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 관련 표준·프레임워크·오픈소스

# 56. 운영 이관·확대·교육 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 직접 걸리는 기준은 법정 교육, 사용자 측 운용 표준, 인계 프레임워크, 새 플릿 연동 도구로 나뉜다. [추정][^ref-1315][^ref-1153][^ref-1318][^ref-1319]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 직접 걸리는 기준은 법정 교육, 사용자 측 운용 표준, 인계 프레임워크, 새 플릿 연동 도구로 나뉜다. [추정][^ref-1315][^ref-1153][^ref-1318][^ref-1319]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 | 프레임워크 | 로봇작업 교육 내용 4개 항목의 법정 기준이며, 법제처 해석(2023-11-21)상 산업용 로봇 작업에 한정되지 않는다. 교육시간은 미확인이다. | [사실][^ref-1315] |
| ANSI/A3 R15.08-3-2026 | 표준 | 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구를 정하며 위험성평가, 응용·운영 환경의 변경 관리, 수명주기 전반의 인원 안전을 강조한다(발행일 미확인, 확인일 2026-09-30, 원문 미열람). | [사실][^ref-1153] |
| BSRIA BG 54/2018 소프트 랜딩 프레임워크 | 프레임워크 | 인계 전·초기 사후 지원·연장 사후 지원을 둔 여섯 단계 인계 틀(2018-08). 로봇 분야 적용 사례는 확인되지 않았다. | [사실][^ref-1318] |
| Open-RMF fleet_adapter_template | 오픈소스 | 새 플릿을 붙이는 설정·코드 참조 구현(확인일 2026-09-30). | [사실][^ref-1319] |
| VDA 5050 3.0.0 팩트시트 | 표준 | 관제의 로봇 설정을 돕는 파라미터·제조사 정보 메시지. | [사실][^ref-031] |
| RoMi-H 등재 프로그램(CHART) | 평가 프로그램 | 통합자의 RoMi-H 배치 역량을 연 2회 평가·인증하고 명단을 공개한다(2025-05-01 게시). | [사실][^ref-872] |

위험성평가는 [용어집](../../glossary/risk-assessment.md), 전체 표준 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1153]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-1318]: BSRIA (NBS 출판물 색인), BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings, 2018-08, https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192, 접근일 2026-09-30
[^ref-1319]: Open-RMF (open-rmf/fleet_adapter_template 저장소), fleet_adapter_template README, 미확인, https://github.com/open-rmf/fleet_adapter_template, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s11.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 열린 질문"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1315, ref-959]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#11
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 열린 질문

# 56. 운영 이관·확대·교육 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 운영 이관 완료 기준과 교육 의무 범위처럼 이번 조사에서 답을 찾지 못한 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

운영 이관 완료 기준과 교육 의무 범위처럼 이번 조사에서 답을 찾지 못한 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-266** (상태: 열림) 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-21) 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? 법제처 해석과 한국노동연구원 보고서의 지적을 대조하면 적용 범위가 불명확해 보인다. [추정][^ref-1315][^ref-959]
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-21) 여러 제조사 로봇을 묶는 오케스트레이션 플랫폼을 구축 팀에서 운영 팀으로 넘길 때의 완료 기준(운영 인수 조건, 초기 사후 지원 기간, 지원 책임 이전 시점)을 정한 공개 표준이나 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-21) 한 현장의 시범 운영을 다른 현장으로 넓힐 때 재사용되는 설정(지도·플릿 어댑터·능력 정의)과 현장마다 다시 해야 하는 작업의 비율이나 소요 시간을 측정한 연구가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-21) 로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-959]: 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13), 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-21/pages/topics/2026/2026-09-30-area56-s3.md

```markdown
---
title: "56. 운영 이관·확대·교육 — 왜 중요한가"
type: topic
category: "O. 검증·도입·수명주기"
primary_area_no: 56
related_areas: [3, 4, 20, 21, 31, 37, 39, 40, 50, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1150, ref-1199, ref-1151, ref-1315, ref-1198, ref-1317, ref-1318, ref-959, ref-1323]
last_run: 2026-09-30
version: 1
split_from: docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#3
---

[홈](../../index.md) › [주제](../index.md) › 56. 운영 이관·확대·교육 — 왜 중요한가

# 56. 운영 이관·확대·교육 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시범 운영을 넓힐 때 운영을 누구에게 넘기고 사람을 어떻게 준비시킬지에 관해, 확인한 자료에는 건물 분야의 단계적 인계 틀, 단계적 시험·확대 교훈, 전담 운영 조직과 운영 인력 교육 사례, 법정 로봇작업 특별교육이 있으나 여러 제조사 로봇을 묶는 플랫폼의 운영 이관 완료 기준이나 확대 절차를 정한 공개 표준은 확인되지 않았다. [추정][^ref-1318][^ref-1198][^ref-1199][^ref-1317][^ref-1315]
- 이 페이지는 [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시범 운영을 넓힐 때 운영을 누구에게 넘기고 사람을 어떻게 준비시킬지에 관해, 확인한 자료에는 건물 분야의 단계적 인계 틀, 단계적 시험·확대 교훈, 전담 운영 조직과 운영 인력 교육 사례, 법정 로봇작업 특별교육이 있으나 여러 제조사 로봇을 묶는 플랫폼의 운영 이관 완료 기준이나 확대 절차를 정한 공개 표준은 확인되지 않았다. [추정][^ref-1318][^ref-1198][^ref-1199][^ref-1317][^ref-1315]

한 단위에서 거둔 시범 성공이 다른 단위로의 확대를 보장하지는 않는 것으로 보인다. [추정][^ref-1151][^ref-1198] 한 병원의 자율 배송 로봇이 내과 병동에서는 업무 흐름을 방해하고 직원 저항을 낳았지만 산후 병동에서는 업무 흐름과 사회적 맥락에 통합되었다는 연구(2008)가 있다. [사실][^ref-1151]

역할과 교육 부담이 정리되지 않으면 저항이 생기는 것으로 보인다. [추정][^ref-1150][^ref-1323] 중국 고급 호텔 직원 면담 연구(2022)에서는 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육·동료 교육·고장 처리 같은 추가 업무가 사용 저항으로 이어졌다. [사실][^ref-1150]

교육 의무의 범위도 현장에서 분명하지 않다. 법제처 해석(2023-11-21)은 특별교육 대상 로봇작업을 산업용 로봇에 한정하지 않지만 한국노동연구원 보고서(2024)는 서비스 로봇이 산업용 로봇·협동로봇 안전기준 밖에 있다고 지적하므로, 서비스 로봇을 운영하는 인력에게 어떤 법정 교육이 어디까지 적용되는지는 현장에서 불명확할 것으로 보인다. [추정][^ref-1315][^ref-959]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30 (원문 미열람)
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1315]: 법제처, 로봇작업의 범위 - 산업용 로봇으로 한정되는지 여부 (안건번호 법제처-23-0872), 2023-11-21, https://opinion.lawmaking.go.kr/nl4li/lsItptEmp/438638, 접근일 2026-09-30
[^ref-1198]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1317]: 주간한국, 한림대성심병원, 장애인 고용 연계 병원 로봇 운영 … (제목 일부만 확인), 2025-07-23, https://weekly.hankooki.com/news/articleView.html?idxno=7120747, 접근일 2026-09-30
[^ref-1318]: BSRIA (NBS 출판물 색인), BSRIA Guide BG 54/2018 Soft landings framework 2018. Six phases for better buildings, 2018-08, https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSRIA&DocId=324192, 접근일 2026-09-30
[^ref-959]: 한국노동연구원, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향 (연구보고서 2024-13), 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1323]: Pietrantoni, L. 외 (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11646840/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-21 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-21 | 56. 운영 이관·확대·교육 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1179건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 330개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
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
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
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
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
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

### docs/open-questions.md (요약: 대상 영역 [56] 에 걸린 1건 / 전체 271건)

```markdown
- oq-266 [열림] 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? (영역 40, 56, 60)
```
