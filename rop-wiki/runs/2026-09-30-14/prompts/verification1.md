(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-14
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 2. 사용 사례·요구·책임 범위 (A. 기획·사업)
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

### runs/2026-09-30-14/target.json

```json
{
  "run_id": "2026-09-30-14",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 123,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 2,
    "area_name": "2. 사용 사례·요구·책임 범위",
    "category": "A. 기획·사업",
    "category_letter": "A"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=2"
}
```

### runs/2026-09-30-14/research.json

```json
{
  "run_id": "2026-09-30-14",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 2,
    "area_name": "2. 사용 사례·요구·책임 범위",
    "category": "A. 기획·사업"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 사용 사례 템플릿, 이해관계자 요구사항 명세, 제조사·통합자·사용자 역할, 플릿 제어 수준, 로봇활용 표준공정모델 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설·제조 공장·물류창고·실외 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 사용자 공동 설계, 현장 직원 면담, 업종별 표준공정 목록, 수요처 주관 실증 구조 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IEC 62559, ISO/IEC/IEEE 29148, ANSI/A3 R15.08-2, VDA 5050 범위, Open-RMF 플릿 제어 수준, RoMi-H 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]",
    "로봇에게 맡길 일을 고르고 요구·수용 기준을 정의할 때 쓰는 방법과 표준(사용 사례 템플릿, 요구공학 표준, 사용자 공동 설계)은 무엇인가? (섹션 4·6·7 겨냥)",
    "현장 유형별로 실제 어떤 일이 로봇에게 맡겨지고 있으며, 어떤 요구·제약·완료 확인 방식이 드러났는가? (섹션 5 겨냥, 병원·상업 시설·제조 공장·물류창고·실외, 한국 사례 우선)",
    "로봇 관제 규격과 오케스트레이션 도구는 플랫폼·제조사 관제·로봇 사이의 책임을 어떻게 나누고, 무엇을 규격 범위 밖에 두는가? (섹션 7·9 겨냥)",
    "안전 표준과 법규는 제조사·통합자·사용자·운영자의 책임을 어떻게 정하는가? (섹션 9·10 겨냥)",
    "한국 정부 사업은 수요처의 사용 사례 발굴과 요구 정의를 어떤 구조로 지원하는가? (섹션 5·6 겨냥, 한국 자료 우선)",
    "어떤 종류의 전문 서비스 로봇 적용이 많이 도입되고 있으며, 도입 동기는 무엇인가? (섹션 3 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "국제로봇연맹(IFR)의 World Robotics 2025 서비스 로봇 발표에 따르면 2024년 전문 서비스 로봇 판매는 약 20만 대(전년 대비 9% 증가)이며, 적용 분류별로 운송·물류 102,900대(+14%)가 가장 많고 접객 4만2천여 대(-11%), 전문 청소 2만5천여 대(+34%), 농업 약 19,500대(-6%) 순이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IFR 발표문: 2024년 전문 서비스 로봇 판매 거의 200,000대(+9%), 운송·물류 102,900대(+14%), 접객 42,000대 이상(-11%), 전문 청소 25,000대 이상(+34%), 농업 약 19,500대(-6%). 공급사 응답 기준 집계.",
      "as_of": "2025-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "같은 IFR 발표는 인력 부족을 기업이 전문 서비스 로봇을 쓰는 주요 동기로 들고, 운송·물류 분류에서 서비스형 로봇(RaaS) 방식이 2024년 42% 늘었다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"staff shortages are a key driver for companies to use robots designed for trained professionals\"; 운송·물류 RaaS 42% 성장.",
      "as_of": "2025-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "ISO/IEC/IEEE 29148:2018 은 시스템·소프트웨어의 수명주기 전체에 걸쳐 요구사항을 도출·분석·문서화·검증·관리하는 공정과 그 산출 정보 항목(이해관계자 요구사항 명세(StRS) 등)의 내용과 형식을 규정하는 요구공학 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1207"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: 요구공학 공정과 산출물을 수명주기 전체에 걸쳐 통합적으로 다루며, 요구 공정의 필수 정보 항목과 그 내용을 규정한다. StRS 는 이해관계자 요구를 수용 기준과 함께 담는다.",
      "as_of": "2018",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "IEC 62559 사용 사례 방법론은 에너지 시스템 요구 도출용 IntelliGrid 방법론에 기반한 IEC PAS 62559:2008 에서 나왔으며, 2부(IEC 62559-2:2015)는 사용 사례·행위자 목록·요구사항 목록의 템플릿을, 3부(IEC 62559-3:2017)는 템플릿 내용을 다른 엔지니어링 시스템으로 옮기는 XML 직렬화 형식을 정의하고, 4부는 표준화와 기업 프로젝트용 모범 사례를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1206"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEC SyC Smart Energy 페이지: Part 2 \"Definition of the templates for use cases, actor list and requirements list\", Part 3 XML 직렬화, Part 4 표준화·기업 프로젝트 모범 사례. 기원은 IEC PAS 62559:2008(IntelliGrid).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "IEC 62559-2 의 사용 사례·행위자 목록·요구사항 목록 템플릿 구조는 분류 원문 21장의 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과)으로 ROP 사용 사례를 기술할 때 행위자(로봇·사람·설비)와 요구 목록을 분리해 관리하는 틀로 쓸 수 있을 것으로 보이나, 로봇 오케스트레이션에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1206"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "IEC 62559 는 스마트그리드·Industrie 4.0 등 시스템 오브 시스템 분야의 사용 사례 기술에 쓰인다고 소개된다. 로봇 적용 사례는 이번 검색에서 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "ANSI/A3 R15.08-2(2023)는 산업용 이동로봇(IMR) 시스템을 특정 적용에 맞게 바꾸고 특정 현장에 배치할 때의 안전 요구를 다루며, 위험성평가는 IMR 시스템 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 제공하며, 교육과 안전 작업 절차는 사용자 책임이고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1199"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"the risk assessment shall be performed by the IMR system integrator\"; 교육·안전 작업 절차는 사용자 책임, 개조한 사용자는 제조사·통합자 역할을 맡음. 표준 원문 미열람, 전문지 기사 기준.",
      "as_of": "2023-10-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 명세는 관제(fleet control)가 이동로봇에 대한 주문 배정, 경로 계산, 막힘 감지·해소, 교통 제어를 맡고 이동로봇은 경로·동작을 실행하며 상태를 계속 보고한다고 나누되, 교통 조율 전략·알고리즘, 안전 요구, 보안 대책, 시운전 같은 프로젝트 수행 절차, 운영자·통합자·제조사 사이의 운영 책임 배분은 명세 범위 밖에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 저장소 VDA5050_EN.md(3.0.0) 범위 절: 관제 기능(주문 배정·경로 계산·막힘 해소·교통 제어)과 로봇 기능(경로·동작 실행, 상태 보고)을 구분하고 안전·보안·프로젝트 절차·운영 책임을 범위 밖으로 명시.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "Open-RMF 는 제조사 플릿을 연동 수준에 따라 완전 제어(경로를 RMF 가 지정), 신호등(상태와 일시정지·재개만), 읽기 전용(상태 보고만, 공유 공간당 최대 1개 플릿), 인터페이스 없음(공유 공간·자원에서 교착 가능성)으로 나누어 플랫폼이 맡을 수 있는 조율 범위가 연동 수준에 따라 달라진다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf-core 원본: 읽기 전용은 \"any shared space is allowed to have a maximum of just one 'Read Only' fleet in operation\", 인터페이스 없음은 교착 가능성이 높다고 설명.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f9",
      "claim": "로봇 관제 규격이 운영 책임 배분을 범위 밖에 두고(f7) 오케스트레이션 도구의 조율 범위가 제조사 플릿의 연동 수준에 따라 달라지므로(f8), 플랫폼이 직접 책임질 범위는 규격이 정해 주지 않고 사용 사례·현장·제조사 연동 수준마다 도입 단계에서 정해야 하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f7 의 범위 밖 항목(운영 책임 배분)과 f8 의 네 연동 수준을 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "병원 사례로, 독일 샤리테 베를린 의대병원의 RoMi 연구(Friese 외, JMIR Nursing 2026-04)는 간호 인력과 함께 적용 시나리오·능력 요구·평가 기준을 공동으로 정하고, 반휴머노이드 서비스 로봇에 병실 메시지 전달, 소형 물품 배달, 음료 배급의 비임상 업무를 맡겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1195"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "간호 인력이 \"codevelopment of application scenarios, capability requirements, and evaluation criteria\"에 참여. 로봇 업무: 정보 전달, 물품 배달, 내장 디스펜서 음료 배급.",
      "as_of": "2026-04-14",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f11",
      "claim": "같은 연구는 간호사 30명의 기술 사용 목록(TUI) 응답에서 사용 의도가 지각된 유용성(rs=0.74), 접근성(rs=0.628), 사용성(rs=0.505)과 양의 상관을, 회의감(rs=-0.516)과 음의 상관을 보였고, 시스템 능력과 한계의 투명한 전달과 직접 체험 기회가 도입에 필요하다고 결론지었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1195"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "n=30. 사용성 중앙값 20(3~21 척도), 사용 의도 중앙값 224.5(0~300). 유용성–사용 의도 rs=0.74, P<.001. 이전 로봇 경험에 따른 차이 없음(P=.62).",
      "as_of": "2026-04-14",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "병원 사례로, 에스토니아 타르투 대학병원 현장 시험(Valner 외, Frontiers in Robotics and AI 2022-08)은 병원 직원과의 협업으로 검체·장비 운반을 자동화 대상으로 정하고, 중환자실 직원이 로봇 터치스크린으로 시작한 혈액 검체 운반을 검사실 직원이 꺼내 터치스크린으로 확인하는 방식으로 완료를 확인했으며, 이기종 로봇 플릿은 RMF 로 조율했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1200"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "의료진이 검체·의료 장비 운반 같은 부차 업무에 시간을 쓴다는 점을 자동화 기회로 정의. 중환자실→검사실 혈액 검체, 사람이 싣고 꺼내며 터치스크린으로 확인. TIAGo·Jackal 사용.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f13",
      "claim": "같은 현장 시험에서는 RFID 카드나 근접 센서로 여는 반자동문, 좁은 복도와 많은 사람이 제약이었고, 직접 만든 문 열기 장치가 전원이 떨어져 사람이 개입했으며, 저자들은 혼잡 대기와 기존 설비의 안전한 연동을 미해결 과제로 남겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1200"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "반자동문(RFID·근접 센서), 좁은 복도·인파가 제약. 서보·카드키 문 열기 장치 전원 소진으로 수동 개입. 혼잡 대기와 기존 인프라의 안전한 통합이 미해결 과제.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "병원 사례로, 한림대성심병원의 서비스로봇 실증은 약제 배송, 검체 이송, 부서 간 물품 배송, 환자 안내 등을 로봇에게 맡기고 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1201",
        "ref-1209"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "ZDNet(2024-09): 약제 배송·검체 이송·부서 내 물품 배송·문서 수거·고중량 물류 이송·실외 배송·환자 안내. 비즈한국(2025-04): 약제·검체 운반, 방역, 환자 안내, 병동 간 물류, 환자 교육.",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f15",
      "claim": "한림대성심병원의 로봇 운용 규모는 ZDNet 기사(2024-09-19)가 7종 73대·누적 35,492건(2022-08~2024-05)과 서비스로봇 전용 승강기 구축을, 비즈한국 기사(2025-04-10)가 11종 77대를 전해 기준 시점마다 다르게 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1201",
        "ref-1209"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ZDNet: 7종 73대, 2022년 8월~2024년 5월 누적 35,492건, 전용 승강기 구축. 비즈한국: 11종 77대. 기준 시점이 다른 보도.",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "비즈한국 기사에 인용된 한 의대 교수는 검체 이송처럼 시간에 민감한 업무에서는 기존 컨베이어와 사람 운반이 속도와 안전 면에서 로봇보다 낫다는 의견을 냈다.",
      "tag": "의견",
      "source_ids": [
        "ref-1209"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "지원 인력 만족도는 높지만 의료진은 회의적이며, 시간 민감 업무에는 기존 컨베이어·인편이 더 빠르고 안전하다는 교수 발언.",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f17",
      "claim": "같은 기사는 한국보건산업진흥원 보고서를 인용해 병원의 로봇 도입 장애로 수동 출입문, 건물 구역마다 다른 승강기 시스템, 통로 경사를 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1209"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국보건산업진흥원 보고서 인용: 수동 출입문, 구역마다 다른 승강기 시스템, 통로 경사가 로봇 접근을 어렵게 함. 보고서 원문 미확인(기사 재인용).",
      "as_of": "2025-04-10",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "싱가포르는 공공 의료기관에서 시험·배치하는 모든 로봇 시스템이 표준화되고 인정된 플랫폼으로 상호운용되도록 요구하며, 창이종합병원 CHART 가 개발한 RoMi-H 는 기계·제어·중앙(플릿 관리·로봇 간·설비 연동)·통합(API) 네 도메인으로 구성되고 2019-10-31 ROSCon 에서 공개되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1205"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"all robotics systems tested and subsequently deployed in Public Healthcare Institutions are interoperable via a standardised and recognised International and Singapore platform\"",
      "as_of": "2026-09-30",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "상업 시설 사례로, 신라스테이 서초·반얀트리 클럽 앤 스파 서울의 호텔 룸서비스 로봇 배송에서 로보티즈는 배송 로봇을 만들고, 카카오모빌리티는 QR 주문과 수요–공급 매칭, 이기종 로봇 통합 관제, 인프라·보안, 운영 컨설팅을 맡는 플랫폼을 제공하며, 호텔은 서비스를 운영한다고 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1203"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "아시아경제(2026-03-16): 로보티즈=로봇 제조, 카카오모빌리티=플랫폼·통합 관제·운영 컨설팅, 호텔=서비스 운영. 2024년 협약 뒤 상용 서비스.",
      "as_of": "2026-03-16",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "같은 기사에 따르면 카카오모빌리티는 플랫폼 도입 뒤 일평균 로봇 가동률이 도입 초기 대비 약 8배 오르고 배송 성공률 100%, 룸서비스 매출 약 3배 증가를 이뤘다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1203"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 가동률 \"약 8배\", 배송 성공률 100%, 룸서비스 매출 약 3배. 측정 기간·산정 방법 미공개.",
      "as_of": "2026-03-16",
      "site_type": "상업 시설",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "제조 공장 사례로, 산업통상자원부는 2020년 뿌리·섬유·식음료·자동차 업종의 60개 기업을 대상으로 로봇활용 표준공정모델 14종을 개발하고, 표준공정모델 개발·공정개선 컨설팅·실증 보급·재직자 교육·협동로봇 안전인증을 묶은 패키지로 지원한다고 발표했으며, 6개 연구기관이 지원단을 구성했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1196"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"표준공정모델 개발, 공정개선 컨설팅, 실증보급, 재직자 교육 및 협동로봇 안전 인증 등의 패키지 지원\". 14개 모델, 60개 기업, 6개월 구축·운영.",
      "as_of": "2020-06-25",
      "site_type": "제조 공장",
      "flow_item": "시작 조건"
    },
    {
      "id": "f22",
      "claim": "로봇신문 기사(2025-09-15)에 따르면 한국생산기술연구원은 2019년부터 뿌리산업·바이오화학 등 업종의 제조로봇 표준공정모델 64종을 개발해 실증사업에 148건을 공급했고, 2025년 베트남으로 첫 해외 적용을 넓혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1197"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국생산기술연구원 표준공정모델 64종(2019~), 실증사업 공급 148건, 수요기업 제공 135건, 공급기업 제공 89건, 2025년 베트남 적용. 기관별 수치이며 전체 사업 누계와 다를 수 있음.",
      "as_of": "2025-09-15",
      "site_type": "제조 공장",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "한국로봇산업진흥원의 서비스로봇 실증사업은 로봇 도입이 필요한 수요처(민간·공공)가 주관기관, 로봇기업이 참여기관이 되는 컨소시엄으로 운영되고, 국비는 로봇 도입 비용의 50% 이내이며 민간 부담 50% 이상 중 수요기관이 25% 이상을 부담하고, 분야는 물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료·기타다.",
      "tag": "사실",
      "source_ids": [
        "ref-1202"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "사업 목적 \"수요 중심의 로봇 활용 실증을 통해 시장창출 한계를 극복\". 주관기관=수요처, 참여기관=로봇기업. 절차: 공모→서류·발표·현장평가→선정→협약. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "물류창고 사례로, 곽경민 외(로봇학회논문지 17(4), 2022-11)는 물류 서비스를 계약물류·택배·풀필먼트로 나누고 로봇 적용을 이송 자동화(AGV·AMR·ASRS), 핸들링(박스 디팔레타이징·팔레타이징, 낱개 피킹), 지원(트럭 하역, 착용형 기기)으로 분류하며, 물류 특성에 맞는 기술과 운영 방식을 골라야 한다고 보았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1204"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: 계약물류(팔레트·박스·낱개), 택배(분류·상하차 자동화), 풀필먼트(수백~수천 품목·변동 수요). 로봇 분류 이송·핸들링·지원.",
      "as_of": "2022-11",
      "site_type": "물류창고",
      "flow_item": "작업 대상"
    },
    {
      "id": "f25",
      "claim": "연계 대상: 실외 사례로, 2023-11-17 시행된 개정 지능형로봇법은 운행안전인증(질량 500kg 이하·속도 15km/h 이하 대상, 운행구역 준수·횡단보도 통행 등 16개 시험항목)을 받은 실외이동로봇의 배달·순찰을 허용하고, 보도에서 로봇을 운영하려는 자에게 보험 또는 공제 가입 의무를 부과한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1208"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "산업통상자원부·경찰청(2023-11-16): 보도 운영자 \"보험 또는 공제 가입 의무를 부과\", 위반 시 범칙금 3만 원. 인증 대상 500kg·15km/h 이하, 16개 시험항목.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f26",
      "claim": "확인한 자료를 종합하면 핵심 질문(로봇에게 어떤 일을 맡기고 플랫폼은 어디까지 책임질 것인가)에 대해, 실제 로봇에 맡겨지는 일은 반복적인 비임상·실내 운반과 정보 전달이 중심이며(f1·f10·f12·f14), 시간 민감 업무는 기존 수단이 낫다는 의견도 있어(f16) 일 선정은 현장 사용자와 함께 기준을 정하는 방식이 쓰이고(f10·f12), 플랫폼의 책임 범위는 규격이 정해 주지 않고 제조사 연동 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해지는 것으로 보인다(f6~f9·f25).",
      "tag": "추정",
      "source_ids": [
        "ref-1198",
        "ref-1195",
        "ref-1200",
        "ref-1201",
        "ref-1209",
        "ref-031",
        "ref-004",
        "ref-1199",
        "ref-1208"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f10·f12·f14·f16 과 f6~f9·f25 를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "확인한 자료를 종합하면 2. 사용 사례·요구·책임 범위에서 ROP가 직접 맡을 것은 오케스트레이션 대상 사용 사례의 목록과 요구 명세(행위자·시작 조건·완료 확인·수용 기준)의 틀(f3·f4·f10), 제조사 플릿마다 연동 수준과 플랫폼이 맡는 조율 범위의 명시(f7·f8), 조달 조건으로서 상호운용 요구의 제시(f18), 현장 사용자와 함께 정한 평가 기준의 관리(f10·f11)로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1207",
        "ref-1206",
        "ref-1195",
        "ref-031",
        "ref-004",
        "ref-1205"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f4·f7·f8·f10·f11·f18 을 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "연계 대상: 분류 원문 19장 기준으로 이동로봇 적용의 위험성평가와 사용 정보 제공(통합자·제조사, f6), 보도 운행 로봇의 보험 가입과 인증(운영자·로봇 제조사, f25), 제조 공정 자체의 개선 컨설팅(f21), 전용 승강기·출입문 같은 건물 설비 개조(f13·f14·f17)는 ROP 밖의 주체가 맡고, ROP는 그 결과를 작업·경로·권한 제약과 책임 분담표로 받아 반영하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1199",
        "ref-1208",
        "ref-1196",
        "ref-1200",
        "ref-1201",
        "ref-1209"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 19장의 시설·설비 제어, 업종별 조건, 로봇 자체 지능 경계와 f6·f13·f14·f17·f21·f25 를 대조한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "이 영역은 시장 규모의 1. 기술·시장·업체 동향(f1), 도입 비용 분담과 과금의 3. 경제성·조달·사업 모델(f2·f20·f23), 완료·인계 단계를 표현하는 24. 작업·워크플로 모델링(f12), 제조사 관제 연동 수준의 20. 로봇·제조사 관제 연동(f7·f8), 조달 요구로서의 21. 상호운용 표준·적합성(f18), 문·승강기의 22. 설비·건물 시스템 연동(f13·f14·f17), 통합자 위험성평가의 48. 안전·위험 관리·50. 안전 표준·인증·사고 조사(f6), 운영자 보험·인증의 59. 법·규제·보험·라이선스(f25), 운영 책임 배분의 58. 다사업자 책임·계약·데이터(f7·f19), 사용자 수용성의 60. 노동·수용성·접근성(f11·f16), 현장 조사의 55. 현장 조사·설치·시운전(f13), 적용 현장인 61. 물류창고(f24)·62. 제조 공장(f21·f22)·63. 병원·의료(f10~f18)·64. 상업 시설(f19·f20)·66. 실외(f25)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1198",
        "ref-1202",
        "ref-1200",
        "ref-031",
        "ref-004",
        "ref-1205",
        "ref-1199",
        "ref-1208",
        "ref-1203",
        "ref-1195",
        "ref-1209",
        "ref-1204",
        "ref-1196",
        "ref-1197",
        "ref-1201"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f25 의 근거를 영역별로 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. 이번 실행에서 플릿 연동 수준(완전 제어·신호등·읽기 전용·인터페이스 없음) 절을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 명세(현재 main 3.0.0). 이번 실행에서 관제와 이동로봇의 기능 구분, 범위 밖 항목(안전·보안·프로젝트 절차·운영 책임)을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1195",
      "org": "Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing)",
      "title": "Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study",
      "published": "2026-04-14",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "샤리테 베를린 RoMi 프로젝트에서 간호 인력과 적용 시나리오·능력 요구·평가 기준을 공동 개발하고 서비스 로봇의 비임상 업무에 대한 간호사 30명의 수용성을 평가했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/",
      "source_unopened": false
    },
    {
      "id": "ref-1196",
      "org": "산업통상자원부 (KDI 경제정보센터 게재)",
      "title": "로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수",
      "published": "2020-06-25",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇활용 표준공정모델 14종 개발과 60개 기업 대상 표준공정모델·컨설팅·실증 보급·교육·안전인증 패키지 지원을 알린 정부 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C",
      "source_unopened": false
    },
    {
      "id": "ref-1197",
      "org": "로봇신문",
      "title": "“제조 로봇 표준공정 모델 적용 사업 국내를 넘어 ... (제목 일부만 확인)",
      "published": "2025-09-15",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=42376",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국생산기술연구원의 제조로봇 표준공정모델 개발·공급 누계와 해외(베트남) 확대를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.irobotnews.com/news/articleView.html?idxno=42376",
      "source_unopened": false
    },
    {
      "id": "ref-1198",
      "org": "International Federation of Robotics (IFR)",
      "title": "Service Robots See Global Growth Boom",
      "published": "2025-10",
      "url": "https://ifr.org/news/service-robots-see-global-growth-boom/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "World Robotics 2025 서비스 로봇 편 발표문. 2024년 전문 서비스 로봇 적용 분류별 판매량, 인력 부족 동기, RaaS 성장.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://ifr.org/news/service-robots-see-global-growth-boom/",
      "source_unopened": false
    },
    {
      "id": "ref-1199",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ANSI/A3 R15.08-2(산업용 이동로봇 시스템·적용 안전 요구) 발행 소식과 제조사·통합자·사용자 역할 요약. 표준 원문과 ANSI 블로그는 403 으로 열지 못했고 ANSI 블로그 검색 요약과 내용이 일치한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "source_unopened": false
    },
    {
      "id": "ref-1200",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원에서 이기종 이동로봇 플릿을 RMF 로 조율해 중환자실→검사실 혈액 검체 운반을 시험한 현장 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/",
      "source_unopened": false
    },
    {
      "id": "ref-1201",
      "org": "ZDNet Korea",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원 서비스로봇 실증(7종 73대, 누적 35,492건)과 업무 종류, 전용 승강기 구축, 설비 연동 어려움을 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://zdnet.co.kr/view/?no=20240919162124",
      "source_unopened": false
    },
    {
      "id": "ref-1202",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "수요처 주관·로봇기업 참여 컨소시엄, 국비·민간 부담 비율, 지원 분야와 선정 절차를 설명한 사업 소개 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "source_unopened": false
    },
    {
      "id": "ref-1203",
      "org": "아시아경제",
      "title": "호텔 룸서비스도 카카오모빌리티 로봇이…\"가동률 ... (제목 일부만 확인)",
      "published": "2026-03-16",
      "url": "https://view.asiae.co.kr/article/2026031610244491183",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "카카오모빌리티·로보티즈의 호텔 룸서비스 로봇 배송 사례와 역할 분담, 회사가 밝힌 가동률·성공률·매출 수치를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://view.asiae.co.kr/article/2026031610244491183",
      "source_unopened": false
    },
    {
      "id": "ref-1204",
      "org": "곽경민, 박범, 고은지, 윤철주, 김경훈 (로봇학회논문지 17(4))",
      "title": "급속 확산되는 물류현장의 로봇적용 사례",
      "published": "2022-11",
      "url": "https://jkros.org/_PR/view/?aidx=34724&bidx=3204",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "계약물류·택배·풀필먼트 물류 유형별 로봇 적용 사례와 이송·핸들링·지원 로봇 분류를 정리한 국내 학술지 논문(초록 페이지 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://jkros.org/_PR/view/?aidx=34724&bidx=3204",
      "source_unopened": false
    },
    {
      "id": "ref-1205",
      "org": "Changi General Hospital, CHART",
      "title": "ROMI-H",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "싱가포르 공공 의료기관 로봇의 상호운용 요구와 RoMi-H 네 도메인 구조, 공개 연혁을 설명한 창이종합병원 CHART 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "source_unopened": false
    },
    {
      "id": "ref-1206",
      "org": "IEC SyC Smart Energy",
      "title": "IEC 62559 - use case methodology",
      "published": null,
      "url": "https://syc-se.iec.ch/deliveries/iec-62559-use-cases/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "IEC 62559 사용 사례 방법론의 기원과 1~4부(개념·템플릿·XML 직렬화·모범 사례) 구성을 설명한 IEC 공식 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://syc-se.iec.ch/deliveries/iec-62559-use-cases/",
      "source_unopened": false
    },
    {
      "id": "ref-1207",
      "org": "ISO / IEC / IEEE",
      "title": "ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering",
      "published": "2018",
      "url": "https://www.iso.org/standard/72089.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 요구공학 공정과 산출 정보 항목(StRS·SyRS·SRS 등)을 규정하는 국제 표준. ISO 페이지와 OBP 는 403 으로 열지 못해 검색 결과 요약 기준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1208",
      "org": "산업통상자원부·경찰청 (대한민국 정책브리핑)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인)",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법 시행(2023-11-17)으로 운행안전인증 실외이동로봇의 보도 통행과 배달·순찰을 허용하고 운영자 보험 가입 의무를 둔다는 정부 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "source_unopened": false
    },
    {
      "id": "ref-1209",
      "org": "비즈한국",
      "title": "병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인)",
      "published": "2025-04-10",
      "url": "https://bizhankook.com/articles/29394.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원 등 국내 병원의 서비스 로봇 운용(11종 77대)과 의료진 의견, 한국보건산업진흥원 보고서의 도입 장애 요인을 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://bizhankook.com/articles/29394.html",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
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
      "rationale": "섹션 3: f1·f2(적용 분류별 도입 규모와 인력 부족 동기), f9(책임 범위를 규격이 정해 주지 않음), f26(핵심 질문 답, 추정) / 섹션 4: 사용 사례 템플릿 f4, 이해관계자 요구사항 명세 f3, 제조사·통합자·사용자 역할 f6, 플릿 연동 수준 f8, 로봇활용 표준공정모델 f21 / 섹션 5: 병원 — f10(작업 대상: 메시지·물품·음료)·f11(예외·성과: 수용성)·f12(완료·인계: 터치스크린 확인)·f13(제약: 반자동문·인파)·f14·f15(작업 대상·수행 자원)·f16(의견)·f17(제약)·f18(제약: 상호운용 조달 요구), 상업 시설 — f19(수행 자원: 역할 분담)·f20(벤더 주장 병기), 제조 공장 — f21·f22(표준공정모델), 물류창고 — f24(물류 유형·로봇 분류), 실외 — f25(연계 대상: 운행안전인증·운영자 보험). 가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 사용자 공동 설계 f10·f11, 현장 직원 협업 f12, 업종별 표준공정 목록 f21·f22, 수요처 주관 실증 f23, 사용 사례 템플릿 적용 f5(추정) / 섹션 7: IEC 62559 f4, ISO/IEC/IEEE 29148 f3(원문 미열람), ANSI/A3 R15.08-2 f6, VDA 5050 범위 f7, Open-RMF 연동 수준 f8, RoMi-H f18 / 섹션 8: f10~f13·f24 / 섹션 9: f27(직접 범위), f28(연계 대상), f7·f8 / 섹션 10: f29 — 1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66 / 섹션 11: open_questions_new 5건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10~f18, 58. 다사업자 책임·계약·데이터 페이지에 f6·f7·f19 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "사용 사례 템플릿",
      "term_en": "Use Case Template (IEC 62559-2)",
      "definition": "IEC 62559-2 가 정한 사용 사례 기술 양식으로, 사용 사례의 목표·시나리오와 함께 행위자 목록과 요구사항 목록을 구조화해 기록하게 한다."
    },
    {
      "term_ko": "이해관계자 요구사항 명세",
      "term_en": "Stakeholder Requirements Specification (StRS)",
      "definition": "ISO/IEC/IEEE 29148 이 정한 요구공학 산출물의 하나로, 사용자와 이해관계자가 시스템에 기대하는 것을 구현 방법 없이 수용 기준과 함께 적은 문서다."
    },
    {
      "term_ko": "로봇활용 표준공정모델",
      "term_en": "Robot Standard Process Model (Korea)",
      "definition": "업종별 제조 공정에 로봇을 적용하는 방법을 표준화한 국내 참조 모델로, 수요기업이 공정을 골라 로봇 도입·실증에 쓰도록 정부 지원 사업과 연계해 개발·보급된다."
    }
  ],
  "open_questions_new": [
    "로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 58. 다사업자 책임·계약·데이터 | 근거: f7 | 종류: 일반",
    "병원 검체 이송처럼 시간에 민감한 업무에서 로봇·컨베이어·사람 운반을 같은 조건으로 비교해 로봇에게 맡길 업무를 정한 정량 연구가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 63. 병원·의료 | 근거: f16 | 종류: 일반",
    "IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 24. 작업·워크플로 모델링 | 근거: f5 | 종류: 일반",
    "싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 21. 상호운용 표준·적합성 | 근거: f18 | 종류: 일반",
    "가정·공동주택과 기타 현장(공공시설·연구실 등)에서 여러 로봇에게 맡길 일과 요구를 사용자와 함께 도출한 연구나 실증 사례가 있는가? | 관련 영역: 2. 사용 사례·요구·책임 범위, 65. 가정·공동주택, 67. 기타 현장 | 근거: f26 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 1,
    "unverified": [
      "f3 ISO/IEC/IEEE 29148:2018: ISO 페이지·OBP 403 으로 원문 미열람, 범위와 정보 항목은 검색 결과 요약 기준",
      "f6 ANSI/A3 R15.08-2: 표준 원문과 ANSI 블로그 403, 전문지 기사 기준(ANSI 블로그 검색 요약과 내용 일치하나 출처 상한으로 넣지 않음)",
      "f1·f2 IFR 수치: 공식 요약 PDF 는 추출 실패, IFR 뉴스 페이지 기준. 운송·물류 안에서 공공 교통 없는 실내 운송이 가장 중요한 분류라는 서술은 검색 요약에만 있어 넣지 않음",
      "f15 한림대성심병원 규모는 보도 시점마다 달라(7종 73대 대 11종 77대) 최신값 미확인",
      "f17 한국보건산업진흥원 보고서 원문 미확인(기사 재인용)",
      "f20 카카오모빌리티 가동률·성공률·매출 수치는 회사 주장이며 측정 기간·방법 미확인",
      "f22 제조로봇 표준공정모델 전체 누계: 다른 기사 검색 요약의 '2020년부터 109개 공정 + 34개' 수치는 열지 않아 넣지 않았고 한국생산기술연구원 기관 수치(64종)만 기재",
      "IEC 62559-2 템플릿의 세부 필드 목록은 원문 미열람으로 미확인",
      "García 외 서비스 로보틱스 소프트웨어 공학 연구(ESEC/FSE 2020)는 초록에 요구·임무 명세 관련 결과가 없어 넣지 않음",
      "WER 2017 로봇 시스템 요구공학 체계적 매핑 연구와 DTU 병원 운반 업무 사례 연구는 PDF 추출 실패로 넣지 않음",
      "가정·기타 현장의 사용 사례·요구 도출 자료는 찾지 못함"
    ],
    "scope_violations": [
      "f6: 이동로봇 위험성평가·안전 절차 책임은 M. 안전 대분류(48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사)의 내용이므로 이 영역에서는 책임 배분 근거로만 쓰고 f28 에서 '연계 대상: '으로 구분함",
      "f25: 실외 로봇 인증·보험은 원문 19장 '업종별 조건'(실외 차량 등) 연계 대상이므로 claim 을 '연계 대상: '으로 시작함",
      "f13·f14·f17: 전용 승강기·출입문 개조는 원문 19장 '시설·설비 제어' 연계 대상이며 ROP 는 요청·상태 확인 인터페이스만 맡는 것으로 f28 에서 구분함",
      "f21·f22: 제조 공정 자체의 개선 컨설팅은 ROP 범위 밖이며 사용 사례 발굴 방법의 근거로만 제안함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1195~ref-1209, 예약 구간 안)로 신규 출처 상한에 도달해 ANSI 블로그(R15.08-3-2026)·IFR 서비스 로봇 정의 문서·RoMi-H 등재 프로그램 페이지를 출처로 더하지 못했다. 재사용 2건(ref-004, ref-031): 참고문헌 목록 전체가 입력에 없어 ref-004 값은 researcher.md 예시, ref-031 값은 이전 브리프 2026-09-25-09 출처 표를 따랐고 이번에 GitHub 공식 저장소 원본을 다시 열었다. 원문 열람: 16건 열었고(webfetch 14, github_raw 2) ISO/IEC/IEEE 29148(ref-1207)만 403 으로 못 열어 source_unopened 로 표시했다. PDF 출처(IFR 요약, DTU, WER 2017, ARIA 보고서)는 본문 추출에 실패해 쓰지 않았다. 교차 확인 1건(f14, 한림대성심병원 업무 종류: ZDNet·비즈한국 두 기사). 기사 근거 finding(f15·f16·f17·f19·f20·f22)은 low 로 두었고, 카카오모빌리티 성과 수치(f20)는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가)에는 f26 으로 답했고 결론은 '맡기는 일은 반복적 비임상·실내 운반과 정보 전달이 중심이고 사용자와 함께 선정하며, 플랫폼 책임 범위는 규격이 정하지 않아 제조사 연동 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해진다'는 추정이다. 현장 유형 사례는 병원(f10~f18)·상업 시설(f19·f20)·제조 공장(f21·f22)·물류창고(f24)·실외(f25)이며 가정·기타는 찾지 못했다. 국내 자료는 산업통상자원부 2건(ref-1196, ref-1208)·한국로봇산업진흥원(ref-1202)·로봇학회논문지(ref-1204)·기사 4건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음. 용어집에 이미 있는 플릿 제어 수준·서비스형 로봇·공공 영역 이동로봇·등재 프로그램·실외이동로봇 운행안전인증·의료 로봇 미들웨어 RoMi-H·로봇 친화형 건축물 인증·로봇–작업 적합도 행렬은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### docs/categories/planning-and-business/use-cases-requirements-and-scope.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위"
type: area
category: "A. 기획·사업"
area_no: 2
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [A. 기획·사업](index.md) › 2. 사용 사례·요구·책임 범위

# 2. 사용 사례·요구·책임 범위

!!! info "소속 대분류"
    [A. 기획·사업](index.md) — 핵심 질문:
    어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **책임 범위 정의**: 플랫폼이 직접 맡을 범위와 외부(업무 시스템·로봇 자체 지능·설비 제어·현장 간 운송·업종별 조건)에 맡길 범위를 정한다
- **사용 사례 발굴·요구 정의**: 로봇에게 맡길 일과 성공 기준·수용 기준을 정한다
- **현장 유형별 요구 정리**: 물류창고·제조 공장·병원·상업 시설·가정·실외 같은 현장 유형마다 공통 요구와 고유 요구를 정리한다

## 2. 핵심 질문

로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]

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

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md (요약)

```markdown
# 1. 기술·시장·업체 동향

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
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

### docs/open-questions.md (요약: 대상 영역 [2] 에 걸린 0건 / 전체 228건)

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

### runs/2026-09-30-13/research.md

```markdown
# 리서치 브리프 2026-09-30-13

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-13 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 37. 관제 화면·실행 기록 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 작업 상태 모델, 로그 수준, 시간 색인 기록 형식, 상황 인식 기반 에이전트 투명성, 설명 가능한 경로 계획 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설 관제 화면·배송 이력 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 지도 위 상태 표시, 설명 가능한 표시, 실행 기록 저장·시간축 재생 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 시각화·웹 대시보드·작업 상태/로그 스키마, VDA 5050 시각화 토픽, MCAP, ISA-101 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
2. 여러 제조사 로봇·설비·작업 상태를 지도 위에, 층을 나눠 보여 주는 공개 구현(오픈소스·표준)은 무엇을 어떤 형식으로 표시하는가? (섹션 6·7 겨냥)
3. 로봇이 무엇을 왜 하고 있는지 운영자가 알아보게 하는 설명 가능한 표시에 관한 연구(에이전트 투명성, 계획 설명)는 무엇을 보고하는가? (섹션 4·6·8 겨냥)
4. 실행 기록을 어떤 구조로 저장하고 시간축으로 재생·검색하는가, 그리고 플릿 실행 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식이 있는가? (oq-131, 섹션 6·7 겨냥)
5. 관제 화면 설계에 쓸 수 있는 표준·지침과 다중 로봇 관제 화면에 관한 사용자 연구는 무엇인가? (섹션 7·8 겨냥)
6. 병원·상업 시설·물류창고 같은 현장에서 로봇 관제 화면과 실행 이력을 운영에 쓴 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)
7. 관제 화면·실행 기록에서 ROP가 직접 맡을 것과 로봇 제조사·시설 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 rmf_visualization 은 승강기·문의 위치와 상태, 플릿 관리자가 보고한 로봇 현재 위치, 닫힌 차선(회색)·속도 제한 차선(좁은 폭)을 구분한 주행 그래프, 초록 선으로 그린 로봇 예측 일정 궤적, 층 평면도를 한 화면에 겹쳐 보여 주며, 일정 궤적은 시작 시점과 조회 기간을 매개변수로 정해 시간 구간별로 조회한다. | ref-1165 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | Open-RMF 의 rmf-web 은 사용자가 Open-RMF 배치 전체를 시각화하고 제어하는 웹 인터페이스 묶음으로 API 서버·API 클라이언트·대시보드 프레임워크로 이루어지며, 기본 설정의 API 서버는 비영속 내부 데이터베이스를 쓰므로 실행 기록을 남기려면 영속 저장소를 따로 설정해야 한다. | ref-1166 | 아니오 | medium | 2026-09-30 | — | — |
| f3 | [사실] | Open-RMF API 메시지의 작업 상태(task_state) 스키마는 작업 상태를 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 12개 값으로 표현하고, 처음 추정 소요 시간과 현재 추정 소요 시간, 배정 로봇, 완료·진행·대기 단계 목록, 일시정지(interruptions)·취소·강제 종료 요청 정보를 함께 담는다. | ref-1167 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f4 | [사실] | Open-RMF API 메시지의 작업 로그(task_log) 스키마는 로그를 작업 수준·단계(phase) 수준·사건(event) 수준으로 계층화하고, 각 로그 항목(log_entry)은 단조 증가하는 순번(seq), 중요도 tier(uninitialized·info·warning·error), 밀리초 단위 유닉스 시각, 본문 텍스트를 필수로 가진다. | ref-1168, ref-1169 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 명세는 차량의 위치와 계획 경로를 시각화 시스템에 높은 빈도로 보내는 visualization 토픽을 주문 확인·오류·운용 상태를 담는 state 토픽과 분리해 두며, state 메시지는 사건이 생길 때 또는 최소 30초 간격으로 보내게 한다. | ref-1170 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | MCAP 은 임의 직렬화 형식의 타임스탬프 발행·구독 메시지를 기록하는 모듈형 컨테이너 형식으로, 스키마·채널·메시지·청크 레코드와 메시지 색인·청크 색인·요약 레코드를 두어 시각 기준 임의 접근(탐색)을 지원하고 첨부·메타데이터 레코드를 함께 담을 수 있다. | ref-1171 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [추정] | Foxglove 문서는 기록 재생 기능으로 시간축 막대 탐색, 재생 속도 조절, 재생 구간 자르기, 사건(event) 주석의 생성·검색, 반복 재생을 제공하고, 임의 시점으로 이동할 때 구독 토픽마다 가장 최근 메시지를 불러와(lookback) 모든 패널이 같은 시점 상태를 보이게 한다고 설명한다. | ref-1172 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f8 | [사실] | Kottinger·Almagor·Lahijanian(ICAPS 2022)은 다중 에이전트 경로 계획을 사람이 눈으로 검증할 수 있도록 에이전트 궤적이 서로 겹치지 않는 시간 구간별 이미지 몇 장으로 설명하는 방식을 채택하고, 이 설명 가능한 MAPF 가 환경 크기에 대해 NP-난해임을 보인 뒤 CBS 에 설명 가능성 제약을 더한 XG-CBS 를 제안해 계획 시간과 설명 가능성의 절충을 분석했다. | ref-1173 | 아니오 | medium | 2022-02 | — | — |
| f9 | [사실] | Chen 외(Theoretical Issues in Ergonomics Science, 2018)는 지능형 에이전트와 함께 일하는 운영자의 임무 환경 상황 인식을 돕기 위한 상황 인식 기반 에이전트 투명성(SAT) 모델을 Autonomous Squad Member·IMPACT 두 시스템의 사람 참여 시뮬레이션 실험에 적용했고, 에이전트가 더 투명해질수록 운영자의 작업 수행이 일관되게 나아졌다고 보고했다. | ref-1174 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f10 | [사실] | Roldán 외(Sensors, 2017-07)는 드론 2대·지상 로봇 1대의 화재 감시·진압 임무 8개를 운영자 24명이 감독하는 실험에서 기존·예측형 기존·가상현실·예측형 가상현실 인터페이스를 비교해, 가상현실 인터페이스가 상황 인식(SAGAT)을 높이고 작업 부하(NASA-TLX)를 낮췄으나 예측 요소의 효과는 유의하지 않았고 오히려 부하를 늘렸다고 보고했으며, 다중 로봇 인터페이스 요건으로 정보량 줄이기, 관련 정보로 주의 유도, 로봇 위치·건강·상태·측정값을 같은 화면에 통합하기, 지도 활용을 들었다. | ref-1175 | 아니오 | medium | 2017-07-27 | — | — |
| f11 | [사실] | ISA 는 공정 자동화 시스템의 인간–기계 인터페이스(HMI) 표준으로 ISA-101.01-2015 와 기술 보고서 TR101.01-2022(HMI 철학)·TR101.02-2019(HMI 사용성과 성능)를 두며, ISA-101.01 은 설계·구현·운영·지속 개선에 이르는 HMI 수명주기를 다루고 연속·배치·이산 산업 모두에 적용된다고 밝힌다. | ref-1176 | 아니오 | medium | 2026-09-30 | — | — |
| f12 | [추정] | 현대자동차그룹 로보틱스랩은 통합 관제 시스템 나콘(NARCHON)을 다수 이기종 로봇의 실시간 모니터링, BPMN 2.0 기반 워크플로·시나리오 관리, 이상 탐지·보고가 있는 실시간 대시보드, 승강기·자동문·보안 게이트 연동과 층간 이동을 지원하는 시스템으로 소개하며 적용처로 건물·상업 시설을 든다. | ref-1177 | 아니오 | low | 2026-09-30 | 상업 시설 / 수행 자원 | 벤더 주장 |
| f13 | [추정] | 네이버클라우드의 ARC brain 사용 가이드는 서비스 기능으로 여러 제조사 로봇의 제어와 충돌 방지, 로봇 실시간 상태 모니터링과 알림, 실시간 태스크와 운영 이력 조회, 제3자 로봇 등록, 승강기·자동문 연동, 맵 에디터 기반 동선 설정, 로봇 상태 기반 알림 설정을 든다. | ref-1178 | 아니오 | low | 2026-09-17 | — | 벤더 주장 |
| f14 | [사실] | 아주경제(2025-04-07) 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다. | ref-1179 | 아니오 | low | 2025-04-07 | 병원 / 완료·인계 | — |
| f15 | [추정] | 확인한 자료를 종합하면 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에 대해, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만(f1·f3·f4·f5), '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이고(f8·f9·f10) 실제 다중 제조사 플릿 관제 화면에서 효과를 측정한 공개 자료는 찾지 못했다. | ref-1165, ref-1167, ref-1168, ref-1170, ref-1173, ref-1174, ref-1175 | 아니오 | low | 2026-09-30 | — | — |
| f16 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇을 감독하는 운영자는 정보량이 많을수록 상황 인식과 작업 부하가 나빠지고(f10), 에이전트의 판단이 투명할수록 운영자 수행이 나아지며(f9), 공정 산업 HMI 표준이 화면을 수명주기 전체에 걸쳐 관리할 대상으로 보고(f11), 병원처럼 배송 이력을 남겨야 하는 현장에서는 실행 기록이 인계 확인의 근거가 되기 때문이다(f14). | ref-1175, ref-1174, ref-1176, ref-1179 | 아니오 | low | 2026-09-30 | — | — |
| f17 | [추정] | 확인한 자료를 종합하면 37. 관제 화면·실행 기록에서 ROP가 직접 맡을 범위는 여러 제조사 플릿과 승강기·문 같은 설비 상태를 하나의 층별 지도에 겹쳐 보여 주는 통합 화면(f1·f12·f13), 제조사마다 다른 상태를 공통 작업 상태 값·단계·수준별 로그로 정규화한 실행 기록(f3·f4), 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색(f2·f6·f7), 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시(f8·f9)다. | ref-1165, ref-1177, ref-1178, ref-1167, ref-1168, ref-1166, ref-1171, ref-1172, ref-1173, ref-1174 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록)과 로컬 회피 시각화는 로봇 제조사에, 승강기·자동문·CCTV 같은 시설 설비의 자체 관제 화면은 시설·설비 쪽에 속하므로, ROP 는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태와 설비 상태를 받아 통합 표시·기록하는 인터페이스를 맡을 것으로 보인다. | ref-1170, ref-1171, ref-1165 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 이 영역은 알림·이상 탐지의 38. 모니터링·이상 탐지·원인 분석(f4·f12·f13), 작업 시각 기록을 지표로 쓰는 39. 운영 성과 측정·개선(f3), 층별 지도의 15. 지도·공간·위치 모델(f1), 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f5), 기록 재생의 36. 가상 시운전·실제 상황 재현과 11. 채팅으로 실제 상황 시뮬레이션 재현(f6·f7, oq-131), 경로 설명의 27. 다중 로봇 경로·교통 관리 — MAPF(f8), 투명성의 13. 대화형 기능의 신뢰·기반·31. 사람–로봇 협업(f9·f10), 상태 메시지의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f5), 문·승강기 표시의 22. 설비·건물 시스템 연동(f1), 기록 저장의 43. 데이터·관측성·배포(f2·f6), 배송 이력의 17. 작업 대상·자산 식별과 인계 추적(f14), 적용 현장인 63. 병원·의료(f14)·64. 상업 시설(f12)과 이어진다. | ref-1165, ref-1166, ref-1167, ref-1168, ref-1170, ref-1171, ref-1172, ref-1173, ref-1174, ref-1175, ref-1177, ref-1178, ref-1179 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1165 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_visualization | 아니오 |
| ref-1166 | Open Robotics (open-rmf/rmf-web) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-1167 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-1168 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json | 아니오 |
| ref-1169 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 아니오 |
| ref-1170 | VDA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0) | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1171 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://mcap.dev/spec | 아니오 |
| ref-1172 | Foxglove | Playback — Foxglove Documentation | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://docs.foxglove.dev/docs/visualization/playback | 아니오 |
| ref-1173 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 2022-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2202.09930 | 아니오 |
| ref-1174 | Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 2018 | 논문 | medium | 2026-09-30 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 예 |
| ref-1175 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 아니오 |
| ref-1176 | ISA (International Society of Automation) | ISA-101 Series of Standards | 미확인 | 표준 | medium | 2026-09-30 | https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards | 아니오 |
| ref-1177 | 현대자동차그룹 로보틱스랩 | PROJECTS — Robot Fleet Management (NARCHON) | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://robotics.hyundai.com/projects/research/view.do?seq=102 | 아니오 |
| ref-1178 | 네이버클라우드 | ARC brain 개요 - 사용 가이드 | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://guide.ncloud-docs.com/docs/arc-brain-overview | 아니오 |
| ref-1179 | 아주경제 | 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 (제목은 검색 결과 기준) | 2025-04-07 | 기사 | low | 2026-09-30 | https://www.ajunews.com/view/20250407084333272 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f16(왜 중요한가), f15(핵심 질문 답, 추정) / 섹션 4: 작업 상태 모델 f3, 수준별 로그 f4, 시각 색인 기록 형식 f6, 에이전트 투명성 f9, 설명 가능한 MAPF f8 / 섹션 5: 병원 — f14(완료·인계: 특수 물품 배송 이력·안면 인식 수령 인증, 계획 단계임을 명시), 상업 시설 — f12(수행 자원: 건물 설비 연동 통합 관제, 벤더 주장 병기). 물류창고·제조 공장·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 지도 위 상태 표시 f1·f5, 설명 가능한 표시 f8·f9·f10, 실행 기록·재생 f2·f3·f4·f6·f7 / 섹션 7: Open-RMF rmf_visualization·rmf-web·rmf_api_msgs f1~f4, VDA 5050 visualization 토픽 f5, MCAP f6, ISA-101 f11, 상용 도구 예 f7·f13(벤더 주장) / 섹션 8: f8·f9·f10 / 섹션 9: f17(직접 범위), f18(연계 대상) / 섹션 10: f19 — 11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 36, 38, 39, 43, 63, 64 / 섹션 11: 기존 oq-131(미해결 유지)과 open_questions_new 4건. 다음 실행 후보: 36. 가상 시운전·실제 상황 재현 페이지에 f6·f7(기록 재생) 반영, 38. 모니터링·이상 탐지·원인 분석 페이지에 f4(로그 수준)·f11(ISA-101) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 설명 가능한 다중 에이전트 경로 찾기 | Explainable Multi-Agent Path Finding (Explainable MAPF) | 여러 에이전트의 충돌 없는 경로를 찾으면서, 궤적이 서로 겹치지 않는 시간 구간 이미지 몇 장만으로 사람이 계획의 안전을 눈으로 확인할 수 있게 하는 경로 계획 문제다. |
| HMI 철학 | HMI Philosophy (ISA-TR101.01) | 한 조직의 인간–기계 인터페이스 화면을 일관되게 설계·운영하기 위해 원칙과 규칙을 정해 둔 상위 문서로, ISA-101 계열에서 기술 보고서로 다룬다. |
| 로그 재생 | Log Playback | 타임스탬프가 붙은 기록 데이터를 기록 시각 순서대로 다시 흘려 보내며 시간축을 탐색·가감속해 과거 시점의 상태를 다시 보는 기능이다. |
| 상황 인식 | Situation Awareness (SA) | 운영자가 주변 요소를 지각하고, 그 의미를 이해하며, 가까운 미래 상태를 예측하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 21. 상호운용 표준·적합성 | 근거: f3 | 종류: 일반
- 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 31. 사람–로봇 협업 | 근거: f10 | 종류: 일반
- 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 일반
- 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? | 관련 영역: 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 근거: f11 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f9 SAT 모델 논문(ref-1174): 출판사·DTIC·ADS 페이지가 403/405 로 열리지 않아 검색 결과 요약 범위로만 서술했고, SAT 세 수준의 정의는 출처 귀속이 불분명해 넣지 않음(용어집의 기존 SAT 항목 참조)
    - f5 VDA 5050 state 메시지 최소 30초 간격: 원문을 열었으나 요약 도구를 거친 확인이라 판 번호별 문구는 검증 필요
    - f11 ISA-101.01 본문 미열람(유료). 비정상 상황 감지·진단·대응 개선 목적, 변경 관리(MOC)·감사 작업 과정은 제3자 요약에만 있어 넣지 않음
    - ISO 11064(관제실 인간공학 설계) 각 부의 범위: ISO 페이지 403 으로 원문을 열지 못해 출처로 넣지 않음
    - oq-131: 플릿 실행 기록을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식은 찾지 못함. RoboCup Logistics League 경기 기록을 객체 중심 이벤트 로그(OCEL)로 만든 연구(Springer 2026 챕터)는 페이지가 열리지 않아 넣지 않음
    - Rohrer 외(arXiv 2207.10017) 객체 중심 프로세스 예측이 RCLL 데이터를 쓰는지 초록에서 확인하지 못함(PDF 추출 실패)
    - f12·f13·f7 벤더 기능 주장: 독립 출처로 교차 확인하지 못함
    - f14 병원 관제·배송 이력 시스템: 협약 단계 보도뿐이며 실제 운영 여부 미확인. 계명대 동산의료원 배송 로봇 기사(병원신문 2023-04-24)는 관제 화면 내용이 없어 넣지 않음
    - 물류창고·제조 공장·가정·실외 현장의 관제 화면·실행 기록 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f18: 로봇 온보드 센서·주행 기록과 로컬 회피 시각화, 시설 설비 자체 관제 화면은 연계 대상으로 표시함
    - f6·f7: 기록 재생은 과거 실행을 다시 보는 기능으로 다루며 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 섞지 않음. 재생을 시뮬레이션 재현으로 넓히는 부분은 36. 가상 시운전·실제 상황 재현 연결로만 제안함
    - f1·f5: 지도 위 현재 상태 표시는 18. 실시간 세계 상태·데이터 일관성의 상태를 보여 주는 화면으로 보고, 상태 모델 자체는 18번 소관으로 연결만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 출처 상한에 도달해 ISO 11064, RCLL 객체 중심 이벤트 로그, 물류창고·제조 공장 관제 화면 사례를 더 넣지 못했다. 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건이고 전체 목록 id 를 받지 못함. VDA 5050·MCAP 이 기존 목록에 같은 URL 로 있으면 퍼블리셔가 합친다). 원문 열람: 14건 열었고(github_raw 6건, webfetch 8건) SAT 논문(ref-1174)만 열지 못해 source_unopened 로 표시했다. 논문은 Roldán 외(PMC 본문) 외에 Kottinger 외는 초록만 봤다. 교차 확인 0건: 핵심 내용이 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더 문서 기능 주장(f7·f12·f13)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에는 f15 로 답했고 결론은 '무엇을 보여 주는 요소는 공개 구현·표준에 있으나 왜를 보여 주는 설명 표시는 실험실 연구 수준이며 현장 평가 자료를 찾지 못했다'는 추정이다. 현장 유형 사례는 병원(f14, 협약 단계)·상업 시설(f12, 벤더 주장)뿐이며 물류창고·제조 공장·가정·실외는 찾지 못했다. 국내 자료는 현대차 로보틱스랩(ref-1177)·네이버클라우드(ref-1178)·아주경제(ref-1179) 3건이다. oq-131 은 근거를 찾지 못해 해결 제안하지 않았다. 용어집에 이미 있는 백 파일·MCAP·상황 인식 기반 에이전트 투명성·감사 추적·관측성·오픈 RMF·VDA 5050 은 후보로 내지 않았다. 페이지 제안은 대상 영역 갱신 1건이고 36·38번 반영은 다음 실행 후보로 적었다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-12/research.md

```markdown
# 리서치 브리프 2026-09-30-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-12 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 33. 시나리오 모델·편집 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 시나리오 기술 언어, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 장애 주입 선언, 반증 기반 시험 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(호텔·공항)·병원(클리닉)·실외(캠퍼스)·가정(가정 활동)·제조 공장(배터리 생산) 시나리오 예제와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 확률적 시나리오 언어, 건물 주석 편집기, 행동 트리·BPMN 같은 미션 형식, LLM 기반 환경·시나리오 생성 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ASAM OpenSCENARIO, SDFormat, VDMA LIF, Open-RMF rmf_demos·traffic-editor, BEHAVIOR-1K·BDDL, NIST ARIAC, MovingAI MAPF 벤치마크, Groot2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131·oq-135 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]
2. 로봇 시뮬레이션·자율 시스템 시험에서 쓰는 시나리오 기술 형식·언어는 무엇이며 환경·개체·작업·사건·장애를 어떻게 나누어 담고 판(버전)을 어떻게 관리하는가? (섹션 4·6·7 겨냥)
3. 현장 유형별(호텔·병원·공장·가정·실외·물류창고) 시나리오 예제·템플릿 라이브러리로 공개된 것은 무엇이고 각각 무엇을 담는가? (섹션 5·7 겨냥, 한국 자료 우선)
4. 사람이 화면에서 시나리오·워크플로·미션을 그리고 고치는 편집기와 미션 기술 형식(행동 트리·상태 기계·BPMN 등)은 무엇이며 비교 연구는 무엇을 말하는가? (섹션 6·7·8 겨냥)
5. 언어 모델로 시뮬레이션 환경·시나리오를 자동 생성하는 연구는 무엇을 입력으로 받아 무엇을 만들고 어떻게 평가했는가? (섹션 6·8 겨냥, 9. 채팅으로 시나리오 구성과의 연결)
6. oq-131 플릿 관제 실행 기록을 시나리오 사양으로 바꾸는 공개 형식·변환 규칙, oq-135 시나리오 구성 시 되물어야 할 항목의 표준 목록이 있는가? (섹션 11 겨냥)
7. 33. 시나리오 모델·편집에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·로봇 제조사·설비 쪽에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Vin 외의 Scenic 3.0(CAV 2023)은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어 Scenic 에 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, 선형 시간 논리(LTL)로 쓰는 시간 요구사항을 더해 반증(falsification) 기반 시험에 쓸 수 있게 했다. | ref-1135 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | ASAM OpenSCENARIO XML 은 주행·교통 시뮬레이터의 동적 내용(차량·보행자 등 여러 개체의 동기화된 기동)을 계층 구조의 XML 파일(.xosc)로 기술하는 표준으로, 2026-05-19 에 1.4.0 판이 나왔고, 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화할 수 있게 한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f3 | [사실] | ASAM 은 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO XML 은 그 위의 동적 내용만 담게 나누며, 병행 표준 OpenSCENARIO DSL 은 대규모 검증용, XML 은 예측 가능한 정밀 시나리오용으로 역할을 구분한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f4 | [사실] | Open-RMF 의 rmf_demos 는 호텔 월드로 로비와 객실 2개 층, 승강기 2대, 여러 문, 로봇 플릿 3개(로봇 4대)가 층을 오가며 순찰(loop)·청소 작업을 하는 다중 플릿 시나리오를 예제로 제공한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 상업 시설 / 수행 자원 | — |
| f5 | [사실] | rmf_demos 의 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 여러 플릿과 설비·이용자의 상호작용을 보이며, 선택적으로 군중 시뮬레이션을 켜고 사람이 직접 모는 읽기 전용(read_only) 카트를 함께 두고 순찰·배송·청소 작업을 실행한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 상업 시설 / 제약 | — |
| f6 | [사실] | rmf_demos 의 클리닉 월드는 승강기 2대가 있는 2개 층 시설에서 역할이 다른 로봇 플릿 2개가 층을 오가며 간호 스테이션 사이를 순찰하는 병원형 시나리오 예제다. | ref-1136 | 아니오 | medium | 2026-09-30 | 병원 / 제약 | — |
| f7 | [사실] | rmf_demos 의 캠퍼스 월드는 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스에서 여러 배송 로봇이 장거리 순찰을 하는 실외 시나리오 예제이고, 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다. | ref-1136 | 아니오 | medium | 2026-09-30 | 실외 / 작업 대상 | — |
| f8 | [사실] | rmf_demos 에서 시나리오는 월드(건물 구성·차선·승강기·문·충전 위치)를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣는 구조이며, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f9 | [사실] | Open-RMF 의 traffic-editor 는 시설 지도 위에 벽·문(여닫이·미닫이·양문)·층·승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, 층 정렬용 기준점을 그려 넣는 GUI 편집기로, 결과를 .building.yaml 파일로 저장하고 building_map_generator 가 이를 물리 시뮬레이션 월드로 자동 생성한다. | ref-1137 | 아니오 | medium | 2026-09-30 | — | — |
| f10 | [사실] | Stanford 등의 BEHAVIOR-1K(arXiv 2403.09227, 예비판 CoRL 2022)는 '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(BDDL)로 형식 명세하고, 주택·정원·식당·사무실 등 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상, 강체·변형체·액체를 다루는 OmniGibson 시뮬레이터 위에 구현한 활동 라이브러리다. | ref-1138 | 아니오 | medium | 2024-03 | 가정 / 작업 대상 | — |
| f11 | [사실] | NIST ARIAC 문서의 시나리오는 전기차 배터리 생산 시설로, 배터리 셀 4개를 트레이에 담는 키팅과 셀 4개와 상하 케이스로 모듈을 조립하는 두 작업을 주문으로 받고, 우선순위가 높은 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않게 정한다. | ref-1140 | 아니오 | medium | 2026-09-30 | 제조 공장 / 작업 대상 | — |
| f12 | [사실] | NIST ARIAC 는 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(시작·지속·대상 TESTER), 진공 그리퍼 파지 실패(TOOL·몇 번째 파지인지 GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID) 네 가지 민첩성 과제를 매개변수로 선언해, 장애와 긴급 요청을 시각 또는 발생 횟수 조건으로 시나리오에 주입한다. | ref-1139 | 아니오 | medium | 2026-09-30 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Kästner 외의 Arena-Bench(RA-L 2022)는 동적 환경의 시나리오·월드 생성 도구와 평가 지표를 갖춘 벤치마크 모음으로, 3차원 환경에서 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오로 비교하고 실물 로봇 배치까지 보였다. | ref-1142 | 아니오 | medium | 2022-06 | — | — |
| f14 | [사실] | Shcherbyna 외의 Arena 4.0(arXiv 2409.12471)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다. | ref-1143 | 아니오 | medium | 2024-09 | — | — |
| f15 | [사실] | Yang 외의 Holodeck(CVPR 2024)은 GPT-4 가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하는 방식으로 오락실·스파·박물관 같은 상호작용 가능한 환경을 자동 생성하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했고 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다. | ref-1144 | 아니오 | medium | 2023-12 | — | — |
| f16 | [추정] | 행동 트리 편집기 Groot2 는 끌어놓기로 트리를 만들며 XML 을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다. | ref-1145 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [사실] | Filippone·Pettinari·Pelliccione(IEEE TSE, arXiv 2603.15427)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·표현력·도구 지원 측면에서 비교하며, 미션을 명세하는 표준이나 널리 받아들여진 형식이 없고 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다고 지적했다. | ref-1146 | 아니오 | medium | 2026-03 | — | — |
| f18 | [사실] | Moving AI 연구실의 MAPF 벤치마크는 도시·게임·창고형·무작위·미로·방 등 격자 지도 36개마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 모두 1,800개의 시나리오 파일을 공개한 재사용 가능한 시나리오 라이브러리다. | ref-1147 | 아니오 | medium | 2026-09-30 | — | — |
| f19 | [사실] | SDFormat(Simulation Description Format)은 로봇 시뮬레이터·시각화·제어용으로 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo 에서 시작했고 Open Source Robotics Foundation 이 Apache 2.0 으로 관리한다. | ref-1148 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰는 비구속적 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받아 만들어졌다. | ref-1149 | 아니오 | medium | 2023-09 | — | — |
| f21 | [추정] | 확인한 형식들은 공통으로 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃, OpenDRIVE 도로망)과 동적 내용(작업 명령, OpenSCENARIO 스토리보드, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하며, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 두지만 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다. | ref-1148, ref-1137, ref-1149, ref-1141, ref-1136, ref-1139, ref-1138 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 공개 형식은 분야별로 나뉘어(자율주행 OpenSCENARIO, 가정 활동 BDDL, 시설 다중 로봇 Open-RMF 건물 파일과 작업 명령, 제조 ARIAC 과제 설정, MAPF .scen) 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 찾지 못했고 미션 기술에도 표준이 없으며(f17), 재사용은 매개변수화·카탈로그(f2), 확률 분포 표본 추출(f1), 현장 유형별 예제 월드(f4~f7), 대규모 활동·시나리오 라이브러리(f10·f18), 언어 모델 생성(f14·f15)으로 이루어지는 것으로 보인다. | ref-1141, ref-1138, ref-1136, ref-1139, ref-1147, ref-1146, ref-1135, ref-1143, ref-1144 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 계획기·정책을 같은 조건에서 비교하려면 고정된 시나리오 파일이 있어야 하고(f13·f18), 장애·긴급 요청을 시나리오에 선언해야 예외 대응 시험을 반복할 수 있으며(f12), 매개변수화가 없으면 조건별 시나리오 파일이 불어나고(f2), 비전문가가 미션과 환경을 정의해야 하는데 공통 형식이 없기 때문이다(f17). | ref-1142, ref-1147, ref-1139, ref-1141, ref-1146 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 확인한 자료를 종합하면 33. 시나리오 모델·편집에서 ROP가 직접 맡을 범위는 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 버전 있는 시나리오 모델(f8·f12·f21), 현장 유형별 예제 라이브러리(f4~f7), 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택(f9·f16·f17), 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환(f9·f19)으로 보인다. | ref-1136, ref-1139, ref-1137, ref-1145, ref-1146, ref-1148 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 로봇 기구학·센서 모델(SDFormat 로봇 기술, f19)은 시뮬레이터·로봇 제조사 쪽에, 컨베이어·작업셀 같은 설비 제어(f7·f12)는 설비 쪽에, 도로 교통 시나리오 표준(f2·f3)은 자율주행 분야에 속하므로, ROP 는 이들을 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. | ref-1148, ref-1136, ref-1139, ref-1141 | 아니오 | low | 2026-09-30 | — | — |
| f26 | [추정] | 이 영역은 시나리오를 대화로 만드는 9. 채팅으로 시나리오 구성(f14·f15)과 11. 채팅으로 실제 상황 시뮬레이션 재현, 시나리오를 실행하는 34. 시뮬레이션·예측용 디지털 트윈(f19), 기록 재생·재현의 36. 가상 시운전·실제 상황 재현(f16), 규모 산정의 35. 처리능력·규모·배치 설계, 건물·레이아웃 주석의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f9·f20), 군중·보행자의 19. 사람·보행자 모델(f5·f14), 승강기 연동의 22. 설비·건물 시스템 연동(f4·f6), 미션 형식의 24. 작업·워크플로 모델링(f17), 장애 주입의 32. 예외 복구·재계획·업무 연속성(f12), 경로 시나리오의 27. 다중 로봇 경로·교통 관리 — MAPF(f18), 언어 모델 생성의 44. 로봇 기반 모델·언어 모델 계획(f15), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f13·f18), 적용 현장인 62. 제조 공장(f11·f12)·63. 병원·의료(f6)·64. 상업 시설(f4·f5)·65. 가정·공동주택(f10)·66. 실외(f7)와 이어진다. | ref-1143, ref-1144, ref-1148, ref-1145, ref-1137, ref-1149, ref-1136, ref-1146, ref-1139, ref-1147, ref-1135, ref-1142, ref-1140, ref-1138 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1135 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.03325 | 아니오 |
| ref-1136 | Open-RMF (open-rmf/rmf_demos) | rmf_demos — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-1137 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Traffic Editor | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-1138 | Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.09227 | 아니오 |
| ref-1139 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Challenges | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1140 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 아니오 |
| ref-1141 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | high | 2026-09-30 | https://www.asam.net/standards/detail/openscenario-xml/ | 아니오 |
| ref-1142 | Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv) | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2206.05728 | 아니오 |
| ref-1143 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.12471 | 아니오 |
| ref-1144 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-1145 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.behaviortree.dev/groot/ | 아니오 |
| ref-1146 | Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1147 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://movingai.com/benchmarks/mapf/index.html | 아니오 |
| ref-1148 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | http://sdformat.org/ | 아니오 |
| ref-1149 | VDMA (Intralogistics-2X-LIF) | Layout Interchange Format (LIF) — README | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f23(왜 중요한가), f22(핵심 질문 답, 추정) / 섹션 4: 확률적 시나리오 언어·반증 f1, 매개변수화·카탈로그 f2, 정적 환경과 동적 내용 분리 f3·f21, 장애 주입 선언 f12, 미션 기술 형식 f17 / 섹션 5: 상업 시설 — f4(호텔, 수행 자원)·f5(공항 터미널, 제약: 군중·수동 카트), 병원 — f6(클리닉, 제약: 층간 승강기), 실외 — f7(캠퍼스, 작업 대상: WGS84 공간), 가정 — f10(일상 활동 라이브러리), 제조 공장 — f11(배터리 생산 작업 대상)·f12(장애 주입 예외·성과). 물류창고는 f18 격자 지도와 f20 레이아웃 형식뿐이고 실제 현장 사례는 찾지 못함을 명시 / 섹션 6: 확률적 언어 f1, 건물 주석 편집 f9, 월드+작업 명령 구조 f8, 미션 형식 비교 f17, 행동 트리 편집·재생 f16(벤더 주장 병기), 언어 모델 기반 환경 생성 f14·f15 / 섹션 7: ASAM OpenSCENARIO f2·f3, SDFormat f19, VDMA LIF f20, Open-RMF rmf_demos·traffic-editor f4~f9, BEHAVIOR-1K·BDDL f10, NIST ARIAC f11·f12, MovingAI MAPF f18, Arena f13·f14, Groot2 f16 / 섹션 8: f1·f10·f13·f14·f15·f17 / 섹션 9: f24(직접 범위), f25(연계 대상) / 섹션 10: f26 — 9, 11, 14, 15, 19, 22, 24, 27, 32, 34, 35, 36, 44, 54, 62, 63, 64, 65, 66 / 섹션 11: 기존 oq-131·oq-135(미해결)와 open_questions_new 4건. 다음 실행 후보: 9. 채팅으로 시나리오 구성 페이지에 f14·f15, 36. 가상 시운전·실제 상황 재현 페이지에 f12·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 오픈시나리오 | ASAM OpenSCENARIO | ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다. |
| 행동 영역 정의 언어 | Behavior Domain Definition Language (BDDL) | BEHAVIOR 벤치마크가 가정 활동을 시뮬레이션된 물리 상태와 연결된 논리 술어로 형식 명세하는 데 쓰는 도메인 특화 언어다. |
| 시뮬레이션 기술 형식 | Simulation Description Format (SDFormat) | Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다. |
| 반증 기반 시험 | Falsification | 시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다. |

## 열린 질문

새로 생긴 질문:

- 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 관련 영역: 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f21 | 종류: 일반
- 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 65. 가정·공동주택 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f10 BDDL 이 활동을 초기 조건·목표 조건 쌍으로 정의한다는 세부 구조는 검색 요약에만 있어 claim 에 넣지 않음
    - f1 Scenic 이 한 프로그램에서 표본 추출로 여러 장면을 만든다는 설명과 로봇 적용 사례(암석 지대)는 검색 요약에만 있어 넣지 않음
    - f15 Holodeck 3D 자산 수(약 5만 개)는 검색 요약에만 있어 넣지 않음
    - f13 Arena 시나리오 편집기의 끌어놓기 배치·보행자 웨이포인트 기능은 검색 요약에만 있어 넣지 않음
    - f16 Groot2 기능은 제품 페이지뿐이며 독립 출처로 교차 확인하지 못함
    - f2 OpenSCENARIO XML 1.4.0 명세 본문은 열지 않았고 공식 소개 페이지 기준
    - oq-131 미해결: 플릿 실행 기록을 시나리오로 바꾸는 공개 형식은 찾지 못함(찾은 JoyAI-Sim arXiv 2606.16776 은 탁상 조작 과제 재구성이라 제외)
    - oq-135 미해결: 시나리오 구성 시 되물을 항목의 표준 목록은 이번 조사에서 찾지 못함(검색하지 못함)
    - 물류창고 실제 현장의 시나리오 예제·템플릿 사례와 국내 자료는 찾지 못함
    - Bourr·Tiezzi 의 BPMN→X-Klaim 변환(arXiv 2311.04126)은 철회된 논문이라 제외
    - Moskovskaya 외 안내 로봇 LLM 시나리오 생성(arXiv 2509.10317)은 대화 행동 대본 의미의 시나리오라 제외
- 범위 경계 위반 의심:
    - f19: SDFormat 의 로봇 기구학·센서 기술은 로봇 제조사·시뮬레이터 쪽 내용이므로 형식 참조 근거로만 쓰고 f25 에서 연계 대상으로 구분함
    - f2·f3: OpenSCENARIO 는 자율주행 도로 시나리오 표준이므로 ROP 직접 범위가 아니라 참조 설계 사례로만 제안함
    - f7·f12: 컨베이어·작업셀 설비 제어는 설비 쪽 연계 대상이며 시나리오에 장애를 선언하는 방식만 근거로 씀
    - f8·f21: 시나리오는 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 섞지 않음
    - f14·f15: 언어 모델 기반 생성은 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획)과 9. 채팅으로 시나리오 구성에도 연결하도록 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1135~ref-1149, 예약 구간 안)로 출처 상한에 도달해 물류창고 실제 현장 시나리오와 국내 자료, oq-135 조사를 더 하지 못했다. 재사용 출처 없음: NIST ARIAC 는 공통 규칙상 ref-008 이지만 입력 참고문헌 요약에 ref-008 의 등록 URL·제목이 없어 이번에 연 개별 문서 페이지(challenges·scenario)를 새 id(ref-1139·ref-1140)로 적었다. 같은 URL 이면 퍼블리셔가 합치고, 다르면 ref-008 과의 관계를 검증에서 확인해 주기 바란다. 원문 열람: 15건 모두 열었다(webfetch 10건, github_raw 5건). 논문은 모두 초록 페이지 기준이다. VDMA LIF 지침 PDF 는 본문 추출에 실패해 공식 저장소 README 로 대신했다. 교차 확인 0건: 각 형식·사례가 한 출처에만 기술되어 있어 finding 신뢰도는 medium 이하로 두었다. Groot2 기능(f16)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에는 f22 로 답했고 결론은 '공개 형식은 분야별로 나뉘고 공통 표준은 없으며, 재사용은 매개변수화·표본 추출·예제 라이브러리·언어 모델 생성으로 이루어진다'는 추정이다. 현장 유형 사례는 상업 시설(f4·f5)·병원(f6)·실외(f7)·가정(f10)·제조 공장(f11·f12)이며 물류창고는 격자 지도 벤치마크(f18)와 레이아웃 교환 형식(f20)만 있고 현장 사례는 찾지 못했다. 국내 자료는 한국어 검색 2회에서 이 영역에 맞는 것을 찾지 못했다(찾은 한국지능시스템학회 시뮬레이터 리뷰는 시나리오 정의를 다루지 않아 제외). 기존 열린 질문 oq-131·oq-135 는 해결 근거가 없어 해결 제안하지 않았다. 용어집에 이미 있는 행동 트리·BPMN·HTN·레이아웃 교환 형식·가상 시운전·시나리오 재구성·미션 명세 패턴은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-09/research.md

```markdown
# 리서치 브리프 2026-09-25-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-09 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 2. 공정·워크플로 모델링 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 페이지 각주 0건(용어집의 SCOR·ISA-95·EPCIS 항목만 이 영역에 연결됨)
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음

## 조사 질문

1. ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [분류원문]
2. 업무 흐름을 작업 단계·선후관계·완료 조건으로 표현하는 표준 모델(BPMN, ISA-95/IEC 62264와 그 XML 구현 B2MML, SCOR)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)
3. 선후관계·병렬·대기 같은 제어 흐름을 교착 없이 설계했는지 형식적으로 점검하는 방법(워크플로 넷의 건전성 등)은 무엇인가? (섹션 6·8 겨냥)
4. 로봇 오케스트레이션 쪽 도구(Open-RMF 작업·단계, VDA 5050 동작 상태, BPMN 엔진 기반 다중 로봇 연구)는 작업 단계와 완료·실패를 어떻게 표현하는가? (섹션 5·6·7·8 겨냥)
5. 실행된 공정을 주문·화물·로봇 여러 객체에 걸친 이벤트 로그로 남겨 분석하는 표준(OCEL 2.0)은 무엇을 담는가? (섹션 8·10 겨냥)
6. 공정·워크플로 모델링에서 ROP가 직접 맡을 부분과 WMS·ERP·로봇 내부 제어에 맡길 부분의 경계는 어디인가? (섹션 9 겨냥)
7. 국내 제도·자료는 물류센터 처리 과정을 어떤 단계로 나누어 평가하는가? (한국 자료 우선 규칙, 섹션 3·5 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO/IEC 19510은 OMG의 BPMN(Business Process Model and Notation, 비즈니스 프로세스 모델 및 표기법) 2.0.x를 공개 규격(PAS) 절차로 국제표준화한 것이며, BPMN은 업무 분석가부터 구현 개발자·운영 관리자까지 이해할 수 있는 프로세스 표기법을 목표로 한다. | ref-112 | 아니오 | medium | 2013 | — | 원문 미열람 |
| f2 | [추정] | Camunda 8 문서는 BPMN 메시지 대기 지점(수신 작업·메시지 중간 이벤트)이 활성화되면 메시지 이름과 상관 키(correlation key)로 구독을 만들고, 들어온 메시지를 이 구독에 맞춰 공정 인스턴스에 연결하며, 유지 시간(TTL) 동안 메시지를 보관하고 같은 이름·키·메시지 ID의 중복 메시지는 거부한다고 설명한다. | ref-113 | 아니오 | medium | 2026-09-25 | 완료·인계 | 벤더 주장 |
| f3 | [추정] | BPMN 모델에서 로봇 운반을 하나의 작업 단계로 두고 그 뒤에 WMS의 인수 확인 메시지를 기다리는 수신 단계를 두어 작업 id나 화물 식별자로 상관시키면, ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 완료 조건을 가진 연속 단계로 표현할 수 있을 것으로 보인다. | ref-112, ref-113, ref-044 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |
| f4 | [사실] | IEC 62264-3:2016(ISA-95 Part 3)은 수준 4(업무 계획·물류)와 수준 2(공정 제어) 사이의 제조 운영 관리 활동을 생산·유지보수·품질·재고 운영 관리의 네 활동 모델로 정의하며, 재고 운영 관리는 수준 3에서 재고와 자재 이동을 조정·지시·관리·추적하는 활동이다. | ref-119 | 아니오 | medium | 2016 | — | 원문 미열람 |
| f5 | [사실] | B2MML은 MESA International이 ISA-95(IEC/ISO 62264)의 데이터 모델을 XML 스키마(XSD)로 구현한 것이며, 공식 저장소의 공통 스키마 머리말은 판 0701(2023)이고 ANSI/ISA-95.00.02-2018과 ANSI/ISA-95.00.05-2018을 기반으로 한다. | ref-117 | 아니오 | medium | 2023 | — | — |
| f6 | [사실] | B2MML의 운영 정의 스키마는 운영 세그먼트 사이 선후관계를 SegmentDependency 요소(의존 대상 DependentOperationsSegmentID)로 두고, 공통 스키마의 의존 유형은 NotFollow, PossibleParallel, NotInParallel, AtStart, AfterStart, AfterEnd, NoLaterAfterStart, NoEarlierAfterStart, NoLaterAfterEnd, NoEarlierAfterEnd, Other 값을 둔다. | ref-117, ref-118 | 아니오 | medium | 2023 | 제약 | — |
| f7 | [사실] | B2MML 공통 스키마의 자재 사용 유형(MaterialUse)에는 Consumed, Produced, Consumable, By-product Produced, Co-product Produced, Inventoried 등이 있어 공정 세그먼트가 자재를 소비하는지 생산하는지 재고로 두는지를 구분한다. | ref-117 | 아니오 | medium | 2023 | 작업 대상 | — |
| f8 | [추정] | ISA-95 세그먼트 의존 유형(예: AfterEnd, NotInParallel, NoLaterAfterEnd)을 창고 작업에 쓰면 ‘검수 종료 후 적치 시작’, ‘같은 도크의 상차와 하차 병행 금지’, ‘하역 종료 후 일정 시간 안에 입고 확정’ 같은 선후·병행·시간 제약을 단순 순서보다 세밀하게 표현할 수 있을 것으로 보인다. | ref-117, ref-118 | 아니오 | low | 2026-09-25 | 적치 / 제약 | — |
| f9 | [사실] | Open-RMF 문서는 작업(task)을 단계(phase)를 만들어 내는 객체로 보고, 배송 작업을 픽업 지점 이동·화물 수령·하역 지점 이동·화물 인도·복귀 단계로 나누며, Compose 유형으로 단계·활동의 순서를 직접 조합하게 하고, 여러 층 배송의 승강기 요청 같은 필수 단계는 필요할 때 자동으로 더한다. | ref-110 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f10 | [사실] | Open-RMF API의 작업 상태 스키마는 작업 상태를 uninitialized, blocked, error, failed, queued, standby, underway, delayed, skipped, canceled, killed, completed 12개 값으로 두고, 작업의 단계를 완료(completed)·진행(active)·대기(pending)로 나눠 보고하며 단계마다 이벤트 목록과 소요 시간 추정값을 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f11 | [사실] | VDA 5050 3.0.0 명세는 drop 동작의 완료(FINISHED)를 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의해, 로봇 쪽 완료가 화물의 물리적 인도까지만 가리킨다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f12 | [사실] | Open-RMF 배송 작업에서 로봇은 하역 지점에서 IngestorResult를 받을 때까지 IngestorRequest를 보내며, IngestorResult는 요청 id·결과를 보낸 워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)만 담는다. | ref-023, ref-049 | 아니오 | medium | 2026-09-25 | 입고 / 완료·인계 | — |
| f13 | [사실] | GS1 CBV 2.0 온톨로지는 업무 단계 arriving을 ‘객체가 위치에 도착함’, receiving을 ‘객체를 위치에서 받아 수령자의 재고에 더함’, accepting을 ‘객체의 점유 또는 소유가 바뀜’, storing을 ‘위치 안에서 보관 구역으로 넣고 빼는 이동’으로 서로 다르게 정의한다. | ref-044 | 아니오 | medium | 2021-09-30 | 입고 / 완료·인계 | — |
| f14 | [추정] | 로봇 관제 규격의 완료 신호(VDA 5050 drop FINISHED, Open-RMF IngestorResult SUCCESS)는 CBV의 arriving 수준의 물리적 인도만 나타내고, 수령자 재고 반영(receiving)과 점유·소유 변경(accepting)은 다른 규격이 정의하므로, 공정 모델은 ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 단계와 완료 조건으로 두고 둘을 잇는 식별 키를 명시해야 할 것으로 보인다. | ref-031, ref-049, ref-044 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |
| f15 | [사실] | ASCM의 SCOR 모델 Fulfill 프로세스는 B2C 이행(F1)을 Pick Product(F1.3), Pack Product(F1.4), Stage Product(F1.5) 등을 거쳐 Obtain Proof of Delivery or Customer Acceptance(F1.11)로 끝나는 단계로 나누고, B2B 이행(F2)에도 같은 계열의 단계(F2.3 피킹, F2.12 배송 증빙·고객 인수)를 둔다. | ref-123 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f16 | [사실] | 워크플로 넷(workflow net)은 워크플로의 제어 흐름을 모델링·분석하는 표준적 방법으로 쓰이는 페트리 넷의 한 부류이며, 그 건전성(soundness) 속성은 도메인 지식 없이 찾을 수 있는 교착(deadlock)·라이브락(livelock) 같은 이상이 없음을 보장한다. | ref-120, ref-121 | 아니오 | medium | 2022 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | OCEL(Object-Centric Event Log) 2.0은 이벤트와 여러 객체(주문·품목·출하 등) 사이 관계를 명시적으로 기록하는 이벤트 로그 교환 표준으로, 객체 간 관계, 관계의 한정자(qualifier), 시간에 따라 바뀌는 객체 속성을 담고 SQLite·XML·JSON 세 교환 형식을 둔다. | ref-122 | 아니오 | medium | 2024-03 | 예외·성과 | 원문 미열람 |
| f18 | [추정] | 로봇 하역 한 건이 작업·로봇·팔레트·주문 여러 객체에 동시에 걸리는 ROP 실행 기록은 단일 사례 중심 로그보다 OCEL 2.0 같은 객체 중심 로그 구조에 맞아, 설계한 공정 모델과 실제 실행 흐름의 차이를 분석하는 근거가 될 수 있을 것으로 보인다. | ref-122, ref-111 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f19 | [사실] | Corradini 외(2023)의 FaMe는 BPMN 요소 일부와 모델링 지침으로 다중 로봇 임무를 기술하고, 그 협업 모델을 로봇별 실행 프로세스로 자동 분할해 각 로봇에 내장한 ROS 2 연동 BPMN 엔진이 분산 실행하게 하는 프레임워크이다. | ref-114 | 아니오 | medium | 2023 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 스위스 장크트갈렌 대학 저장소의 경험 보고는 BPMN 2.0을 지원하는 Camunda Platform 7로 자율이동로봇 TurtleBot 4 Pro 두 대를 조율하면서, 업무 프로세스 관리 시스템(BPMS)을 로봇 안에서 돌리는 구성과 외부 노트북에서 돌리는 구성을 비교했다. | ref-115 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f21 | [사실] | arXiv 2603.15427 비교 연구는 로봇 임무 기술 형식으로 행동 트리(Behavior Tree), 상태 기계, 계층적 작업 네트워크(HTN), BPMN 네 가지를 임무 수준에서 제어 구조·표현력·한계·도구 지원 기준으로 비교하고 전문가 검증으로 결과를 확인했다. | ref-116 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f22 | [추정] | 연계 대상: 로봇 내부의 동작 실행 흐름(행동 트리·상태 기계로 구현되는 주행·파지 등)은 제조사 쪽 영역이고, ROP의 공정·워크플로 모델은 업무 단계(BPMN·ISA-95·SCOR 수준)와 로봇 작업 단위(Open-RMF 단계, VDA 5050 동작) 사이의 순서·대기·완료 조건을 맡는 층으로 나누는 것이 분류 원문 9장 경계와 맞아 보인다. | ref-116, ref-110, ref-112 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f23 | [사실] | 국토교통부 스마트물류센터 인증은 입고·보관·피킹·출고 등 물류처리 과정별 첨단·자동화 정도를 보는 기능영역과 시설 구조 성능·성과관리 체계·정보시스템 도입 수준을 보는 기반영역으로 평가해 1~5등급을 부여한다. | ref-124 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 연계 대상: 수령자 재고에 더하는 재고 반영(CBV receiving)과 재고·자재 이동을 추적하는 재고 운영 관리(IEC 62264-3)는 WMS·MES 같은 상위 업무 시스템의 책임이며, ROP는 운반 완료 이벤트를 전달하고 인수 확인을 기다리거나 예외로 분기하는 공정 단계까지만 맡는 구조가 될 것으로 보인다. | ref-044, ref-119 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-112 | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | 표준 | medium | 2026-09-25 | https://www.omg.org/spec/BPMN/2.0/About-BPMN | 예 |
| ref-113 | Camunda | Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://docs.camunda.io/docs/components/concepts/messages/ | 아니오 |
| ref-114 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 | 예 |
| ref-115 | University of St. Gallen (Alexandria 저장소), 저자 미확인 | Autonomous Mobile Robots with Business Process Management Systems at the Edge | 미확인 | 논문 | medium | 2026-09-25 | https://alexandria.unisg.ch/server/api/core/bitstreams/3b1a80df-f89a-46d2-bbf3-118aac764282/content | 예 |
| ref-116 | arXiv:2603.15427 저자(미확인) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 아니오 |
| ref-118 | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd | 아니오 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/67480.html | 예 |
| ref-120 | Formal Aspects of Computing 게재 논문(저자 미확인) | Soundness of workflow nets: classification, decidability, and analysis | 2011 | 논문 | medium | 2026-09-25 | https://doi.org/10.1007/S00165-010-0161-4 | 예 |
| ref-121 | LICS 2022 논문(arXiv:2201.05588) 저자 미확인 | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2201.05588 | 예 |
| ref-122 | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 2024-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.01975 | 예 |
| ref-123 | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | 표준 | medium | 2026-09-25 | https://scor.ascm.org/processes/fulfill/F1.3 | 예 |
| ref-124 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f14·f15·f23(로봇 완료와 업무 완료의 차이, SCOR 이행 단계가 인수로 끝남, 국내 인증이 처리 과정별로 평가) / 섹션 4: f1(BPMN)·f6(세그먼트 의존)·f9(작업·단계)·f13(arriving·receiving·accepting)·f16(워크플로 넷·건전성)·f17(OCEL) / 섹션 5: 입고 완료·인계 f11·f12·f13·f14·f3, 적치 제약 f8, 출하 완료·인계 f15 — 흐름 단계와 여섯 항목 명시 / 섹션 6: f1·f2·f3·f6·f8·f9·f16·f19·f20·f21 / 섹션 7: f1(BPMN·ISO/IEC 19510), f4·f5·f6·f7(IEC 62264-3·B2MML), f9·f10(Open-RMF 작업·상태 스키마), f15(SCOR), f17(OCEL 2.0), f2(Camunda, 벤더 주장 병기) / 섹션 8: f16·f17·f19·f20·f21 / 섹션 9: f22·f24(로봇 내부 동작 흐름과 재고 확정은 연계 대상, ROP는 단계 순서·대기·완료 조건) / 섹션 10: 1. 주문·업무 시스템 연계(f4·f5·f24), 7. 화물·재고·자산 식별과 추적(f13·f14), 9. 로봇·제조사 관제 연동(f11·f12), 12. 명령·작업 실행의 신뢰성(f2·f10), 14. 작업 순서·스케줄링(f6·f8), 4. 성과·경제성·프로세스 개선(f17·f18), 23. 시험·형식 검증·벤치마크(f16) / 섹션 11: open_questions_new 3건과 기존 oq-001 연결(f14). 다음 실행 후보: 1. 주문·업무 시스템 연계 페이지 7절에 B2MML(f5) 반영 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 비즈니스 프로세스 모델 및 표기법 | Business Process Model and Notation (BPMN) | OMG가 정하고 ISO/IEC 19510으로도 발행된 업무 프로세스 표기법으로, 작업·이벤트·게이트웨이·흐름으로 업무 단계와 순서를 그리고 실행 의미를 정의한다. |
| 워크플로 넷 | Workflow Net (WF-net) | 시작·끝 장소를 하나씩 가진 페트리 넷으로 워크플로의 제어 흐름을 표현하며, 건전성 검사로 교착·라이브락 같은 설계 이상을 찾는 데 쓰인다. |
| 객체 중심 이벤트 로그 | Object-Centric Event Log (OCEL) | 하나의 이벤트를 주문·품목·출하 같은 여러 객체와 관계로 함께 기록하는 프로세스 마이닝용 이벤트 로그 표준 형식이다. |
| B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International이 ISA-95(IEC 62264)의 데이터 모델을 XML 스키마로 구현한 교환 형식이다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | 관련 영역: 2. 공정·워크플로 모델링, 1. 주문·업무 시스템 연계 | 근거: f14 | 종류: 일반
- ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | 관련 영역: 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링 | 근거: f8 | 종류: 일반
- 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 2. 공정·워크플로 모델링, 9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·규격별로 발행 기관 한 곳의 자료만 확인(B2MML 두 파일, Open-RMF 두 출처는 같은 발행 주체)
    - f1 BPMN 명세 본문(OMG formal PDF) 원문 미열람 — 게이트웨이·수신 작업의 토큰 의미는 제3자 설명만 봐서 finding 으로 내지 않음
    - f4 IEC 62264-3 의 활동 세부 목록(정의 관리·배차·실행·추적 등)은 제3자 논문 요약에만 있어 finding 으로 내지 않음
    - ISA-88 절차 모델(절차·단위 절차·운영·단계)은 위키·블로그 요약만 확인되어 finding 으로 내지 않음
    - f15 SCOR Fulfill 단계 번호는 scor.ascm.org 검색 요약만 확인
    - f16 ref-120·ref-121 저자 목록 미확인, 워크플로 넷 정의 세부는 강의 슬라이드 요약이라 인용하지 않음
    - f17 ref-122 저자 목록 미확인
    - f19 FaMe 는 공식 저장소 README 로 서지(RAS 160, 104322)만 원문 확인, 기능 설명은 검색 요약
    - f20 ref-115 저자·발행일 미확인
    - f23 스마트물류센터 인증 세부 평가 항목·배점 미확인
    - ref-031·ref-023 은 이번 실행에서 다시 열지 않아 재인용
- 범위 경계 위반 의심:
    - f22: 로봇 내부 행동 트리·상태 기계는 분류 원문 9장 '로봇 자체 지능·제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f24: 재고 확정·재고 운영 관리는 상위 업무 시스템(WMS·MES) 영역이므로 '연계 대상: '으로 표시함
- 한계: fetch_mode mirror_only(web_fetch_available: false): raw.githubusercontent.com 공식 저장소 원문(Open-RMF task_new 원본·task_state.json·IngestorResult.msg, B2MML 스키마 2건, GS1 CBV.ttl, Camunda 문서 원본, FaMe README)은 열어 fetched=true 로 표시했다. OMG·ISO·ASCM·arXiv·ScienceDirect·국가물류통합정보센터 페이지는 원문 미열람이라 신뢰도 상한 medium. 모든 finding 이 단일 발행 주체 근거여서 교차 확인 0건이다. 검색 22회/30, 신규 출처 15건/15(ref-110~ref-124, next_ref_id 기준; 신규 출처 상한 도달로 ISA-88/PackML 원문 출처와 FaMe README 를 출처로 넣지 못함). 재사용 출처 4건(ref-023, ref-031, ref-044, ref-049). 주의: 이전 브리프 2026-09-25-04·05·06 도 ref-110~ref-118 을 다른 출처에 부여했으나 참고문헌 목록에 없으므로 실행 컨텍스트 next_ref_id 를 따랐다 — id 충돌 여부는 퍼블리셔 확인 필요. 한국 자료는 국토교통부 스마트물류센터 인증 안내 1건뿐이며, 국내 BPMN·물류 로봇 공정 모델링 학술 자료는 한·영 검색에서 찾지 못했다(검색된 국내 WMS 자료는 벤더 블로그·개인 저장소라 제외). 정정 요청·이 영역 열린 질문·priority 지정 없음. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. Camunda 문서의 기능 설명(f2)은 벤더 주장으로 표시했다.
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

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope

action type | counter action | description | idempotent | parameters | linked state | instant | node | edge | zone
---|---|---|---|---|---|---|---|---|---
startPause | stopPause | Activates the pause mode. <br>A linked state is required, because many mobile robots can be paused by using a hardware switch. <br>No more automatic driving - reaching next node is not necessary. Actions that can be paused (`pauseAllowed`=`true`), shall be paused, other actions continue. Order execution is resumed after stopPause. | yes | - | paused | yes | no | no | no
stopPause | startPause | Deactivates the pause mode. <br>Movement and all other actions will be resumed (if any). <br>A linked state is required because many mobile robots can be paused by using a hardware switch. <br>stopPause can also restart mobile robots that were stopped with a hardware button that triggered startPause (if configured). | yes | - | paused | yes | no | no | no
startHibernation | stopHibernation | Initiates hibernate mode, in which the mobile robot shall remain connected to the MQTT broker but no longer needs to send state messages. The mobile robot shall report this action as 'FINISHED' before discontinuing publishing state messages and publish a connection state of 'HIBERNATING'. If the mobile robot has an active order, it shall clear it. Reaching the next node is not required.<br>While in 'HIBERNATING' connection state, mobile robot shall not be moving. The mobile robot shall only receive and respond to the instant action 'stopHibernation' and shall not respond to any other commands, such as orders or additional instant actions. <br>If the mobile robot's battery becomes critically low while in this mode, the mobile robot may stop 'HIBERNATING' autonomously to report an error. In case a wake‑up time is set, the mobile robot is able to autonomously exit the 'HIBERNATING' connection state at the specified time and will publish the corresponding connection state transition before resuming normal operation. | yes | wakeUpTime (string, optional) | - | yes | no | no
stopHibernation | startHibernation | Ends hibernate mode. To initiate wake‑up while the mobile robot is in the 'HIBERNATING' state, a control device (onboard or external) shall subscribe to the `instantAction` topic and remain connected to the MQTT broker. Because the mobile robots standard control device may be partially shut down during hibernation, the wake‑up may be triggered by a distinct MQTT client (separate from the mobile robots usual communication client).<br>Upon success, the mobile robot shall publish the connection state ONLINE.| yes | - | - | yes | no | no
shutdown | - | Initiates a coordinated shutdown of the mobile robot, where it disconnects from the MQTT broker. The execution of the shutdown action requires the mobile robot to be in an idle state. There is no way using the VDA 5050 protocol to automatically restart due to the connection being terminated.<br>If a mobile robot is in hibernate mode but should be shut down, it shall first exit hibernation (via stopHibernation) before executing shutdown.| yes | - | - | yes | no | no | no
startCharging | stopCharging | Activates the charging process. <br>Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). <br>Protection against overcharging is the responsibility of the mobile robot. | yes | - | powerSupply.charging | yes | yes | no | no
stopCharging | startCharging | Discontinues the charging process. <br>The charging process can also be interrupted by the mobile robot or the charging station, e.g., if the battery is full. | yes | - | powerSupply.charging | yes | yes | no | no
initializePosition | - | Resets (overrides) the pose of the mobile robot with the given parameters. | yes | x (float64)<br>y (float64)<br>theta (float64)<br>mapId (string)<br>lastNodeId (string) | mobileRobotPosition.x<br>mobileRobotPosition.y<br>mobileRobotPosition.theta<br>mobileRobotPosition.mapId<br>lastNodeId<br> maps | yes | yes<br>(Elevator) | no | no
enableMap | - | Enable a previously downloaded map explicitly to be used in orders without initializing a new position. | yes | mapId (string)<br>mapVersion (string) | maps | yes | yes | no | no
downloadMap | - | Trigger the download of a new map. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the map for use and setting the map in the state. | yes | mapId (string)<br>mapVersion (string)<br>mapDownloadLink (string)<br>mapHash (string, optional) | maps | yes | no | no | no
deleteMap | - | Trigger the removal of a map from the mobile robot's memory. | yes | mapId (string)<br>mapVersion (string) | maps | yes | no | no | no
downloadZoneSet | - | Trigger the download of a zone set. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the zone set for use and setting the zone set in the state. | yes | zoneSetId (string)<br>zoneSetDownloadLink (string)<br>zoneSetHash (string, optional) | zoneSets | yes | no | no | no
enableZoneSet | - | Enable a previously downloaded zone set explicitly to be used in orders. | yes | zoneSetId (string)<br> | zoneSets | yes | yes | no | no
deleteZoneSet | - | Trigger the removal of a zone set from the mobile robot's memory. | yes | zoneSetId (string) | zoneSets | yes | no | no | no
clearInstantActions | - | Removes all finished or failed instant actions from the mobile robot state. | yes | - | instantActionStates | yes | yes | no | no
clearZoneActions | - | Removes all finished or failed zone actions from the mobile robot's state. | yes | - | zoneActionStates | yes | yes | no | no
stateRequest | - | Requests the mobile robot to send a new state message. | yes | - | - | yes | no | no | no
logReport | - | Requests the mobile robot to generate and store a log report. | yes | reason<br>(string) | - | yes | no | no | no
pick | drop<br><br>(if automated) | Request the mobile robot to pick a load. <br>Mobile robots with multiple load handling devices can process multiple pick operations in parallel. <br>In this case, the parameter lhd needs to be present (e.g., LHD1). <br>The parameter stationType informs how the pick operation is handled in detail (e.g., floor location, rack location, passive conveyor, active conveyor, etc.). <br>The load type informs about the load unit and can be used to switch field for example (e.g., EPAL, INDU, etc). <br>For preparing the load handling device (e.g., pre-lift operations based on the height parameter), the action could be announced in the horizon in advance. <br>But, pre-Lift operations, etc., are not reported as 'RUNNING' in the mobile robot state, because the associated node is not released yet.<br>If on an edge, the mobile robot can use its sensing device to detect the position for picking the node. | no |lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional) <br>loadId (string, optional)<br>height (float64, optional)<br>defines bottom of the load related to the floor<br>depth (float64, optional) for forklifts<br>side (string, optional) e.g., conveyor | .load | no | yes | yes | no
drop | pick<br><br>(if automated) | Request the mobile robot to drop a load. <br>See action pick for more details. | no | lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional)<br>loadId (string, optional)<br>height (float64, optional)<br>depth (float64, optional) <br>… | .load | no | yes | yes | no
detectObject | - | Mobile robot detects object (e.g., load, charging spot, free parking position). | yes | objectType (string, optional) | - | no | yes | yes | yes
finePositioning | - | On a node, mobile robot will position exactly on a target.<br>The mobile robot is allowed to deviate from its node position.<br>On an edge, the mobile robot will e.g., align on stationary equipment while traversing an edge. | yes | stationType (string, optional)<br>stationName (string, optional) | - | no | yes | yes | yes
waitForTrigger | - | Mobile robot shall wait for a trigger of the type defined specified in the triggerType parameter, which is an array of strings. Two predefined values shall be used when semantically appropriate: 'FLEET_CONTROL' if the trigger originates from the fleet control, and 'LOCAL' if the trigger comes from an input on the mobile robot (e.g., button press, manual loading). If none of the predefined values meet the specific requirements, custom values can be defined. <br>Fleet control is responsible for handling the timeout and shall cancel the order if necessary. | yes | triggerType [string] (array) | - | no | yes | no | yes
trigger | - | Fleet control system notifies the mobile robot that a waitForTrigger action has been released. Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed. | yes | - | - | yes | no | no | no
retry | - | Mobile robot retries action defined via actionId that is currently in state RETRIABLE. | yes | actionId (string) | - | yes | no | no | no
skipRetry | - | Mobile robot shall skip the action defined via actionId that is currently in state RETRIABLE, setting action to FAILED. | yes | actionId (string) | - | yes | no | no | no
cancelOrder | - | Mobile robot stops as soon as possible. This could be immediately or on the next node. See Chapter 6.1.3 Order cancellation. | yes | orderId (string, optional) | - | yes | no | no | no
factsheetRequest | - | Requests the mobile robot to send a factsheet | yes | - | - | yes | no | no | no
updateCertificate | - | Request the mobile robot to download and activate a new certificate set, the service parameter is an extensible enum with the predefined parameter 'MQTT' to be used for mqtt connection. | yes | service (string)<br>keyDownloadLink (string)<br>certificateDownloadLink (string)<br>certificateAuthorityDownloadLink (string, optional) | - | yes | no | no | no

>Table 4 - Predefined actions and their scope (instant, node, edge, zone)

#### 6.2.3.2 Action states

action type | 'INITIALIZING' | 'RUNNING' | 'PAUSED' | 'FINISHED' | 'FAILED' | 'RETRIABLE'
---|---|---|---|---|---|---
startPause | - | Activation of the mode is in preparation.<br>If the mobile robot supports an instant transition, this state can be omitted. | - | Mobile robot is not moving. <br>All pauseable actions are paused. <br> The pause mode has been activated. <br>The mobile robot reports paused: "true". | The pause mode cannot be activated for some reason (e.g., overridden by hardware switch).
stopPause | - | Deactivation of the mode is in preparation. <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pause mode has been deactivated. <br>All paused actions are resumed. <br>The mobile robot reports paused: "false". | The pause mode cannot be deactivated for some reason (e.g., overridden by hardware switch). | -
startHibernation | - | Activation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The active order has been cleared, if any. No state messages are sent by the mobile robot. <br>Hibernate mode has been activated. The mobile robot reports connection state "HIBERNATING".| The HIBERNATING connection state could not be published (e.g., overridden by a hardware switch).| -
stopHibernation | - | Deactivation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Hibernate mode has been deactivated.<br>The mobile robot reports connectionState "ONLINE".| The hibernate mode could not be deactivated (e.g., overridden by a hardware switch).| -
shutdown | - | Activation of the OFFLINE connection state is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The connection between mobile robot and broker is terminated in a coordinated way.<br>The mobile robot reports connection state "OFFLINE".| The shutdown cannot be executed for some reason (e.g., mobile robot is not in idle state, overridden by a hardware switch).| -
startCharging | - | Activation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been started. <br>The mobile robot reports powerSupply.charging: "true". | The charging process could not be started for some reason (e.g., not aligned to charger). Charging problems should correspond with an error. | The charging process could not be initiated. The mobile robot is waiting for intervention from fleet control or an operator.
stopCharging | - | Deactivation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been stopped. <br>The mobile robot reports powerSupply.charging: "false" | The charging process could not be stopped for some reason (e.g., not aligned to charger).<br> Charging problems should correspond with an error. | -
initializePosition | - | Initializing of the new pose in progress (confidence checks, etc.). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pose has been reset. <br>The mobile robot reports <br>mobileRobotPosition.x = x, <br>mobileRobotPosition.y = y, <br>mobileRobotPosition.theta = theta <br>mobileRobotPosition.mapId = mapId <br>mobileRobotPosition.lastNodeId = lastNodeId | The pose is not valid or cannot be reset. <br>General localization problems should correspond with an error. | -
downloadMap | Initialize the connection to the map server. | Mobile robot is downloading the map. | - | The download has finished. Mobile robot updates its state by setting the mapId/mapVersion and the corresponding mapStatus to 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, Map server unreachable, mapId/mapVersion not existing on map server). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableMap | - | The mobile robot enables the map with the requested mapId and mapVersion and disables any other map with the same mapId. | - | The map has been enabled. The mobile robot updates the corresponding mapStatus of the requested map to 'ENABLED' and the other versions with same mapId to 'DISABLED'. | The requested combination of mapId/mapVersion does not exist.| -
deleteMap | - | Mobile robot deletes map with requested mapId and mapVersion from its internal memory. | - | The map has been deleted. The mobile robot removes mapId/mapVersion from its state. | The map could not be deleted, e.g., because map is currently in use or requested combination of mapId/mapVersion has already been deleted before. | -
downloadZoneSet | Initialize the connection to the zone set server. | Mobile robot is downloading the zone set. | - | The download has finished. The mobile robot updates its state by setting a corresponding zoneSet object in its state with zoneSetStatus 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, server unreachable, zone set not existing, zone set with same zoneSetId already on mobile robot). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableZoneSet | - | Mobile robot enables the zone set with the requested zoneSetId and disables any other zone set for the same mapId. | - | The zone set has been enabled. The mobile robot updates the corresponding zoneSetStatus of the requested zoneSet to 'ENABLED' and the other zone sets for the same mapId to 'DISABLED'. | The requested zone set does not exist.| -
deleteZoneSet | - | Mobile robot deletes the zone set with requested zoneSetId from its internal memory. | - | The zone set has been deleted. The mobile robot removes zoneSet object from its state. | The zone set could not be deleted, deleted, e.g., because zone set is currently in use or the requested zone set has already been deleted before. | -
clearInstantActions | - | | - | The instant actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
clearZoneActions | - | | - | The zone actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
stateRequest | - | - | - | The state has been communicated | - | -
logReport | - | The report is being generated. <br>If the mobile robot supports an instant generation, this state can be omitted. | - | The report has been stored. <br>The name of the log is reported as part of the action state. | The report can not be stored (e.g., no space).| -
pick | Initializing of the pick process, e.g., outstanding lift operations. | The pick process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The pick process is being paused, e.g., if a safety field is violated. <br>After removing the violation, the pick process continues. | Pick has been done. <br>Load has entered the mobile robot and mobile robot reports new load state. | Pick failed, e.g., station is unexpected empty. <br> Failed pick operations should correspond with an error. | Pick failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
drop | Initializing of the drop process, e.g., outstanding lift operations. | The drop process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The drop process is being paused, e.g., if a safety field is violated. <br>After removing the violation the drop process continues. | Drop has been done. <br>Load has left the mobile robot and mobile robot reports new load state. | Drop failed, e.g., station is unexpected occupied. <br>Failed drop operations should correspond with an error. | Drop failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
detectObject | - | Object detection is running. | - | Object has been detected. | Could not detect the object. | Object detection failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
finePositioning | - | Mobile robot positions itself exactly on a target. | The fine positioning process is being paused, e.g., if a safety field is violated. <br> The fine positioning continues after e.g. the violation had been resolved. | Goal position in reference to the station has been reached. | Goal position in reference to the station could not be reached. | Fine positioning failed but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
waitForTrigger | - | Mobile robot is waiting for the trigger | - | Trigger has been triggered. | waitForTrigger fails, if order has been canceled. | -
cancelOrder | - | Mobile robot is stopping or driving, until it reaches the next node. | - | Mobile robot is not moving. Mobile robot has canceled executing the order and is in idle state. | <br>Mobile robot has no active order<br>The previous order has already been canceled.<br>Passed orderId does not match the currently active orderId. | -
factsheetRequest | - | - | - | The factsheet has been communicated | - | -
updateCertificate | - | Mobile robot is downloading and installing certificates | - | Certificates have been downloaded, installed and are active. | Download or installation failed. | -

>Table 5 - Expected behavior in action states of predefined actions

#### 6.2.3.3 Update mobile robot certificate

For security reasons, mobile robot communication (at least for fleet management) should be secured. Typically, communication to the MQTT broker is secured via TLS, which requires one or more root certificates and a mobile robot-specific key pair. The parameter `service` specifies the service (e.g., 'MQTT') for which the certificates are to be used. The parameter `certificateAuthorityDownloadLink` specifies the URL for the root certificate(s). The parameters `certificateDownloadLink` and `keyDownloadLink` specify the URLs for the mobile robot-specific public and private keys.

The download shall be secured via TLS as well, since the sender of the instantAction cannot be verified. It is also advisable to validate the certificate chain before it is activated.

## 6.3 Maps

To ensure consistent navigation among different types of mobile robots, the position is always specified in reference to the project-specific coordinate system (see Figure 12). The project-specific coordinate system is referring to the coordinate system that is defined for the interaction between fleet control and the mobile robot.
For the differentiation between different levels of a site or location, a unique `mapId` is used.
The map coordinate system is to be specified as a right-handed coordinate system with the z-axis pointing skywards.
A positive rotation therefore is to be understood as a counterclockwise rotation.
The mobile robot coordinate system is also specified as a right-handed coordinate system (ISO 9787 4.1) with the x-axis pointing in the forward direction of the mobile robot and the z-axis pointing upward (ISO 9787 5.5). The mobile robot reference point is defined as (0,0,0) in the mobile robot reference frame, unless specified otherwise.

![Figure 12 Coordinate system with sample mobile robot and orientation](./assets/coordinate_system_vehicle_orientation.png)
>Figure 12 - Coordinate system with sample mobile robot and orientation

The X, Y, and Z coordinates shall be given in meters.
The orientation shall be in radians and shall be within -Pi and +Pi.

### 6.3.1 Map distribution

To enable an automatic map distribution and intelligent management of restarting the mobile robots if necessary, fleet control can manage the maps on the mobile robot.

The map files to be distributed are stored on a dedicated map server that is accessible by the mobile robots. To ensure efficient transmission, each transmission should consist of a single file. If multiple maps or files are required, they should be bundled or packed into a single file. The process of transferring a map from the map server to a mobile robot is a pull operation, initiated by the fleet control triggering a download command using an `instantAction`.

Each map is uniquely identified by a combination of a map identifier (field `mapId`) and a map version (field `mapVersion`). The map identifier describes a specific area of the mobile robot's physical workspace, and the map version indicates updates to previous versions. Before accepting a new order, the mobile robot shall check that there is a map on the mobile robot for each map identifier in the requested order. If a corresponding `mapId` is missing in the list of available maps, the mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'. It is the responsibility of the fleet control to ensure that the correct maps are enabled to operate the mobile robot.

In order to minimize downtime and make it easier for the fleet control to synchronize the process of enabling of new maps, maps shall be pre-loaded or buffered on the mobile robots. The status of the maps on the mobile robot is reflected in the mobile robot's state. Transferring a map to a mobile robot and enabling the map are different processes. To enable a pre-loaded map on a mobile robot, the fleet control shall send an instant action. As a result, any other map with the same map identifier but a different map version shall be disabled by the mobile robot.

Deletion of maps can also be done by the fleet control via an instant action.

The map distribution process is shown in Figure 13.

![Figure 13 Map distribution process](./assets/map_distribution_process.png)
>Figure 13 - Communication required between fleet control, mobile robot and map server to download, enable, and delete a map.

### 6.3.2 Maps in the mobile robot state

The `mapId` field in the `mobileRobotPosition` of the state represents the currently active map.

Information about the maps available on a mobile robot is presented in the `maps` array, which is a component of the state message. Each entry in this array is a JSON object consisting of the mandatory fields `mapId`, `mapVersion`, and `mapStatus`, which can be either 'ENABLED' or 'DISABLED'. An 'ENABLED' map can be used by the mobile robot if necessary. A 'DISABLED' map shall not be used. The status of the download process is indicated by the current action not being completed. Errors are also reported in the state.
Note that multiple maps with different `mapId` can be enabled at the same time. There shall only be one version of maps with the same `mapId` enabled at a time. If the `maps` array is empty, no maps are currently available on the mobile robot.

### 6.3.3 Map download

The map download shall be triggered by the `downloadMap` instant action from the fleet control. It shall contain the mandatory parameters `mapId` and `mapDownloadLink` under which the map is stored on the map server and which can be accessed by the mobile robot.

The mobile robot sets the `actionStatus` to 'RUNNING' as soon as it starts downloading the map file. If the download is successful, the `actionStatus` is updated to 'FINISHED'. If the download is unsuccessful, the status is set to 'FAILED'. Once the download has been successfully completed, the map shall be added to the array of `maps` in the state. Maps shall not be reported in the state until they are ready to be enabled.

The process of downloading a map shall not modify, delete, enable, or disable any existing maps on the mobile robot.
The mobile robot shall reject the download of a map with a `mapId` and `mapVersion` that is already on the mobile robot. An error of type 'DUPLICATE_MAP' and level 'WARNING' shall be reported, and the status of the instant action shall be set to 'FAILED'. The fleet control shall first delete the map on the mobile robot and then restart the download.

### 6.3.4 Enable downloaded maps

There are two ways to enable a map on a mobile robot:

1. **Fleet control enables map**: Use the `enableMap` instant action to set a map to 'ENABLED' on the mobile robot. Other Versions of the same `mapId` with different `mapVersion` are set to 'DISABLED'.
2. **Manually enable a map on the mobile robot**: In some cases, it might be necessary to enable the maps on the mobile robot directly. The result shall be reported in the mobile robot state.

Fleet control shall ensure that the correct maps are activated on the mobile robot when sending the corresponding `mapId` as part of a `nodePosition` in an order.
If the mobile robot is to be set to a specific position on a new map, the `initializePosition` instant action shall be used.

### 6.3.5 Delete maps on the mobile robot

The fleet control can request the deletion of a specific map from a mobile robot. This shall be done by using the instant action `deleteMap`. When a mobile robot runs out of memory, it should report this to the fleet control, which can then initiate the deletion of maps. The mobile robot itself shall not delete maps.
After successfully deleting a map, the mobile robot shall remove the corresponding entry from its `maps` array in the state message.

## 6.4 Zones

Zones are used to define rules for specific areas of the mobile robot workspace. In this way, zones allow mobile robots to navigate freely between nodes while giving the fleet control the ability to manage traffic. Zones can be used to locally deny mobile robots access to areas or to link access to conditions (zone types: 'BLOCKED' and 'RELEASE'). It is also possible to enforce specific behavior while within the zone (zone types: 'LINE_GUIDED', 'SPEED_LIMIT', 'COORDINATED_REPLANNING', and 'ACTION') or influence the driving behavior by incentivizing or penalizing certain areas (zone types: 'PRIORITY' and 'PENALTY') or giving a predefined driving direction (zone types: 'DIRECTED', 'BIDIRECTED'). The zone types are defined in the following sections.

Potential conflicts in orders due to overlapping of zones or combination of zone and edge properties and how to resolve them are addressed in section [6.4.4 Interaction between zones](#644-interactions-between-zones). For released nodes that are part of the order but are restricted due to zones (e.g., node located within a 'BLOCKED' or 'RELEASE' zone), the robot is expected to act according to the zones (e.g., not enter or wait for 'GRANTED' state of the request).
Some mobile robots cannot process zones at all, while other mobile robots might only be able to work with a certain subset of zone types, such as 'BLOCKED'. All mobile robots shall therefore report to fleet control which zones they are able to understand by adding the according zone names to the `supportedZones` array under `typeSpecifications` in their factsheet.
Also (virtually) line-guided mobile robots can choose to support zone-based navigation if they can implement the logic of the corresponding zone types defined in the following.
A zone set shall only be changed and distributed by fleet control to keep consistency in the system.

### 6.4.1 Zone types

Two categories of zones are distinguished: contour-based zones and kinematic center-based zones. This distinction is based on the different conditions for when the mobile robot is considered to be entering and exiting zones.

#### 6.4.1.1 Contour-based zones

For contour-based zones, the contour of the mobile robot (including its load) determines zone entry and exit. Any part of the contour entering the zone is a zone entry. As soon as no part of the mobile robot's contour remains within the zone, it is a zone exit.

![Figure 14 Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)](./assets/contour_entry.png)
>Figure 14 - Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)

The following contour-based zones are defined:

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| BLOCKED | none | | Mobile robots shall not enter this zone. If a mobile robot has entered the zone or finds itself within one, it shall stop and throw an 'BLOCKED_ZONE_VIOLATION' error with level set to 'CRITICAL'.|
| LINE_GUIDED | none | | No free navigation is allowed in this zone, mobile robots shall follow the predefined trajectories on edges. Mobile robots may only enter this zone if the route is explicitly specified by the fleet control in the form of a node-edge graph. Any movement of the mobile robot that requires it to enter this zone shall follow a predefined trajectory. When entering the zone, the mobile robot shall be on the trajectory of the edge that crosses the zone. The edges that enter and are inside the line-guided zone require a trajectory sent from the fleet control or a predefined trajectory on the mobile robot. A corridor can be sent to allow the mobile robot to deviate from the trajectory. |
| RELEASE | | - | Mobile robots are only allowed entering this zone once they have been granted access through fleet control. |
| | releaseLossBehavior | string | Enum {'STOP', 'CONTINUE', 'EVACUATE'}<br>When the access to this zone is revoked or expired, the mobile robot can either 'STOP', 'CONTINUE', or 'EVACUATE' the zone. This action is only executed, when the mobile robot is already in the zone and the release expires or is revoked. If not defined, the mobile robot is expected to STOP and report an error.<br>'STOP': Mobile robot stops and sends a 'RELEASE_LOST' error with level 'CRITICAL'.<br>'EVACUATE': Execute the evacuation behavior of the mobile robot to leave the zone, keeping the `zoneRequest` object granting release in its state until the zone is left.<br>'CONTINUE': If the release is revoked or expires after the mobile robot has already entered the zone, the mobile robot continues its path, keeping the `zoneRequest` object granting the zone release in its state. If the order ends inside the zone, the mobile robot waits for a new order.|
| COORDINATED_REPLANNING | none | | No autonomous replanning is allowed within this zone. Mobile robots are only allowed adjusting their path if granted permission by fleet control. |
| SPEED_LIMIT | | | Mobile robots shall not drive faster than the defined maximum speed within this zone. |
| | maximumSpeed | float64 | Maximum permitted speed for mobile robot within the zone in m/s. The speed limit shall already be reached upon entering the zone.|
| ACTION | | | The mobile robot shall perform predefined actions when entering, traversing, or exiting the zone. The factsheet defines which actions can be executed when. |
| | entryActions[action] | array | Actions to be triggered when entering the zone. Empty array, if no actions required. |
| | duringActions[action] | array | Actions to be executed while crossing the zone. Empty array, if no actions required. |
| | exitActions[action] | array | Actions to be triggered when leaving the zone. Empty array, if no actions required. |

>Table 6 - Contour-based zone types and their parameters

#### 6.4.1.2 Kinematic center-based zones

In kinematic center-based zones, the mobile robot's kinematic center determines its entry and exit of the zones. When the mobile robot's kinematic center is inside a zone, the mobile robot shall follow the defined behavior.
'PRIORITY' and 'PENALTY' zones are zones which only influence the path planning of mobile robots.
'DIRECTED' zones define a preferred direction of travel within the zone. 'BIDIRECTED' zones define a travel direction and its opposite direction to be used. Other directions shall be avoided. The `directedLimitation` and `bidirectedLimitation` enums specify the limits within which the mobile robot may deviate from its direction of travel. The direction of travel is the velocity vector in the project-specific coordinate system.

![Figure 15 Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)](./assets/kinematic_center_entry.png)
>Figure 15 - Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| PRIORITY | | | The workspace encompassed by this zone is associated with an incentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | priorityFactor | float64 | [0.0...1.0]<br>Relative factor that determines the preference of the zone over a workspace without a zone. 0.0 means no preference, as if there was no zone, 1.0 is maximum preference.|
| PENALTY | | | The workspace encompassed by this zone is associated with a disincentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | penaltyFactor | float64 | [0.0...1.0]<br> Relative factor that determines the penalty of the zone compared to a workspace without that zone. 0.0 means no penalty, as if there was no zone, 1.0 is the maximum penalty, causing the mobile robot to take this path only if it cannot find any other feasible route. |
| DIRECTED | | | Mobile robots shall traverse this zone in a specific direction of travel. |
| | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system. |
| | directedLimitation | string | Enum {'SOFT','RESTRICTED','STRICT'}<br>SOFT: Mobile robots may deviate from the defined direction of travel, but should avoid it, RESTRICTED: The mobile robot may deviate from the defined direction of travel, e.g., to avoid an obstacle, but shall never traverse opposite to the defined direction of travel, STRICT: The mobile robot shall maintain the defined direction of travel as precisely as its technical capabilities allow. |
| BIDIRECTED | | | While in this zone, mobile robots shall only move in the defined direction of travel and its direct opposite (+ Pi), mobile robots should not cross this zone in any other direction. |
 | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system.|
| | bidirectedLimitation | string | Enum {'SOFT', 'RESTRICTED'}<\br>SOFT: Mobile robots may deviate from the defined directions of travel, but should avoid it, RESTRICTED: The mobile robot shall not traverse in any other direction than the directions of travel, except for obstacle avoidance. |

>Table 7 - Kinematic center-based zone types and their parameters

### 6.4.2 Zone set transfer

Zone sets shall only be changed and distributed by fleet control to keep consistency in the system. The preferred way to distribute zone sets is via the `zoneSet` topic. If the mobile robot supports zones, the update via the `zoneSet` topic shall be supported. Larger zone sets can also be shared through the `downloadZoneSet` instant action, following the map distribution concept in figure 13.

A `zoneSet` is an array of `zone` objects with a globally unique identifier, `zoneSetId`. It is associated with a single map referenced through the `mapId`. The `mapVersion` shall not be referenced, as the same zone set might be intended to be used for several versions of one map. In general, several zone sets can be defined in addition to a single map and it is upon fleet control to ensure that the right zone set is enabled for each map on the mobile robot. As with maps, the `zoneSetStatus` indicates which zone set is currently used by the mobile robot. Only a single zone set can be active at once for each `mapId` on the mobile robot. Zones shall not extend beyond the spatial boundaries of a map.
The content of a zone set with a unique `zoneSetId` shall not change. If changes are required within a zone set, it shall be referenced with a new `zoneSetId`.

The `zoneSetStatus` of a newly added zone set shall always be set to 'DISABLED' and shall be enabled through the `enableZoneSet` instant action before use.

If the mobile robot receives a new zone set via the `zoneSet` topic or `downloadZoneSet` instant action with the same `zoneSetId` as an existing one, it shall not take over the zone set in its internal memory and report an error of type 'DUPLICATE_ZONE_SET' and level 'WARNING' for a reasonable amount of time for the fleet control to notice that the zone update failed.

## 6.4.3 Communication for interactive zones

For communicating requests for the interactive zones 'RELEASE' and 'COORDINATED_REPLANNING', the field `zoneRequests` in the state message is used. The separate topic `responses` is used by fleet control to respond to these requests.

Before entering an interactive zone, the mobile robot shall state a request.
A request before entry of an interactive zone is necessary, even if the order contains released nodes within the zone.
The mobile robot decides at which point before entering the zone to make its requests.
If the response is not received in time, the mobile robot shall not enter the zone.

Requests shall only be made for zones of enabled zone sets. Zone requests can also be made for zone sets belonging to maps that the mobile robot is not currently on.

The `requestId` allows fleet control to distinguish between different requests and allows the mobile robot to issue several alternative requests for the same zone at the same time.
Each request attempt shall use a unique identifier per mobile robot. Ids can be reused after a mobile robot restart.

For requests to enter a 'RELEASE' zone, a `zoneRequest` object of `requestType` 'ACCESS' shall be added to the state message.
For permission to enter a 'COORINATED_REPLANNING' zone with a planned path or for replanning its path within the zone, the `requestType` shall be set to 'REPLANNING'.
For a 'REPLANNING' request, the planned path shall be added as NURBS to the `trajectory` field of the `zoneRequest`. Multiple requests with different trajectories for the same zone can be made. Each path shall be requested with its own `zoneRequest` object.
If a mobile robot requires access to a workspace covered by two or more 'RELEASE' zones, it shall request access and receive approval for all necessary zones before entering the area.
If a mobile robot navigates through a workspace on the map that is covered by two or more 'COORDINATED REPLANNING' zones, it shall request its path within this area individually for each zone and receive approval from the fleet control before entering or changing paths.

The parameter `requestStatus` shall be initially set to 'REQUESTED' by the mobile robot when stating its request.

Fleet control responds to zone requests via the `responses` topic.
The response message contains an array of `response` objects. Each `response` shall only respond to a single request referenced by the `requestId`.
Each response has a `responseType` that is either 'GRANTED', 'QUEUED', 'REVOKED', or 'REJECTED'.
If the `responseType` is 'GRANTED', the mobile robot is allowed to enter the zone or use the requested trajectory.
Fleet control can set the `responseType` to 'QUEUED' to acknowledge the mobile robot's request without giving permission, informing the mobile robot that its request is being processed.
If the `responseType` is 'REJECTED', the mobile robot shall not enter the zone or use the requested trajectory.
The `responseType` 'REVOKED' indicates that the permission is no longer valid. The fleet control shall assume a 'REVOKED' request as still being 'GRANTED', until the `requestStatus` of the mobile robot is set to 'REVOKED'.
The `response` object can include a `leaseExpiry` which specifies until when a 'GRANTED' request is valid. To extend the `leaseExpiry` fleet control can resend a response message with an updated `leaseExpiry` time.

The mobile robot shall acknowledge the fleet controls response by setting the `requestStatus` accordingly and keep the request for as long as it considers the information relevant. See also Section [6.9 Request/response mechanism](#69-requestresponse-mechanism).

The interaction between the mobile robot and the fleet control for 'RELEASE' zones shall be according to Figure 16.

While the mobile robot remains in the 'RELEASE' zone, it keeps the `zoneRequest` object in its state and continues to report `requestStatus` as 'GRANTED' to inform fleet control that it is still inside the zone. After mobile robot has exited the zone, it shall remove the corresponding `zoneRequest` entry from its state message.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state. When the `leaseExpiry` has passed, the requestStatus shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall report a warning and react according to the `releaseLossBehavior` defined in the zone definition.

![Figure 16 Zone request behavior for a RELEASE zone.](./assets/request_release_zone_access.png)
>Figure 16 - Zone request behavior for a RELEASE zone.

The interaction between the mobile robot and the fleet control for 'COORDINATED_REPLANNING' zones shall be according to Figure 17.

The mobile robot shall choose one of the trajectories of all 'GRANTED' requests to the zone and set the corresponding `requestStatus`to 'GRANTED' while removing all other requests from its state.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state and not enter the 'COORDINATED_REPLANNING' zone. When the `leaseExpiry` has passed, the `requestStatus` shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall stop driving and report a warning. To continue, the mobile robot shall state a new request.

![Figure 17 Zone request behavior for a COORDINATED_REPLANNING zone.](./assets/request_coordinated_replanning_zone_replanning.png)
>Figure 17 - Zone request behavior for a COORDINATED_REPLANNING zone.

### 6.4.4 Interactions between zones

In the following matrix possible interactions between zones are described. The matrix is symmetric, as the interaction between two zones is the same, regardless of the order in which they are considered. For each combination, there is either a zone behavior that is overrulling the other (e.g., a 'BLOCKED' zone overrules a 'LINE_GUIDED' zone) or there is no conflict (e.g., a 'LINE_GUIDED' zone and a 'COORDINATED_REPLANNING' zone). 'DIRECTED' and 'BIDIRECTED' zones shall not overlap, since this might lead to an undefined behavior. The column No Zone defines the behavior for contour-based zones, where mobile robots can be inside a defined zone type and an area without a zone at the same time. For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so there is no possible interaction.

| |**BLOCKED**|**RELEASE**|**LINE_GUIDED**|**COORDINATED_REPLANNING**|**SPEED_LIMIT**|**ACTION**|**PRIORITY**|**PENALTY**|**DIRECTED**|**BIDIRECTED**|**No Zone**|**EDGE-PROPERTIES**
---|---|---|---|---|---|---|---|---|---|---|---|---
**BLOCKED**|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|
**RELEASE**||No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict
**LINE_GUIDED**|||No conflict|LINE_GUIDED|No Conflict| (1) |LINE_GUIDED|LINE_GUIDED|LINE_GUIDED|No conflict|LINE_GUIDED|No conflict
**COORDINATED_REPLANNING**||||(2)|No conflict|(1)|No conflict|No conflict|No conflict|No conflict|COORDINATED_REPLANNING|(3)
**SPEED_LIMIT** |||||(4)|No conflict|No conflict|No conflict|No conflict|No conflict|SPEED_LIMIT|(4)
**ACTION** ||||||(5)|No conflict|No conflict|No conflict|No conflict|ACTION|(5)
**PRIORITY** |||||||(6)|(6)|No conflict|No conflict|(7)|No conflict
**PENALTY** ||||||||(6)|No conflict|No conflict|(7)|No conflict
**DIRECTED** |||||||||(8)|(8)|(7)|(9)
**BIDIRECTED** ||||||||||(8)|(7)|(9)

>Table 8 - Interaction matrix for zones

1) If actions would conflict with other zones' behavior, report a 'ZONE_ACTION_CONFLICT' error with level 'CRITICAL' (order error) and stop the mobile robot.
2) Planned trajectory required to be granted for all 'COORDINATED_REPLANNING' zones.
3) If a trajectory is predefined for the edge, it shall be sent in the zone request.
4) The lowest of the competing `maximumSpeed` values applies.
5) Execute all actions.
6) The most restrictive one is always selected here; for PRIORITY zones, the lowest `priorityFactor` is used; for overlapping PRIORITY and PENALTY zones, the highest `penaltyFactor` is used; for overlapping PENALTY zones, the highest `penaltyFactor` is used.
7) For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so this overlap is not possible.
8) Zones shall not overlap, since the behavior is not defined.
9) A `trajectory` as part of the edge properties shall override the directed and bidirected zones.

### 6.4.5 Error handling within zones

If at any point of the order execution, a mobile robot realizes, that it can not reach a node in its order, it shall report a 'NODE_UNREACHABLE' error with level 'CRITICAL' to the fleet control. The fleet control shall then decide how to proceed. The mobile robot shall not try to reach the node again, but wait for further instructions from the fleet control.

## 6.5 Connection

During the connection of a mobile robot client to the broker, a last will topic and message shall be set, which is published by the broker upon disconnection of the mobile robot client from the broker.
Thus, the fleet control can detect a disconnection event by subscribing the connection topics of all mobile robots.
The disconnection is detected via a heartbeat that is exchanged between the broker and the client.
Thus, the fleet control can detect a disconnection event by subscribing to the `connection` topic of each mobile robot.

As a result, the timestamp and headerId fields will always be outdated.

Mobile robot wants to disconnect gracefully:

1. Mobile robot sends "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to `OFFLINE`.
2. Disconnect the MQTT connection with a disconnect command.

Mobile robot comes online:

1. Set the last will to "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN', when the MQTT connection is created.
2. Send the topic "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to 'ONLINE'.

All messages on this topic shall be sent with a `retained` flag.

When connection between the mobile robot and the broker stops unexpectedly, the broker will send the last will to the topic: "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN'.

## 6.6 State

The mobile robot state shall be published on a single topic.
Compared to separate messages (e.g., for current order progress, battery state and errors), using a single topic reduces the workload of both the broker and the fleet control system when handling messages, while also keeping the mobile robot state information synchronized.

The mobile robot state message shall be published when relevant events occur or at least every 30 seconds.

The following events shall trigger a transmission of the state message:

- Receiving an order
- Receiving an order update
- Changes in the `load` object
- Change in the `errors` array
- Change in the `operatingMode` field
- Change in the `driving` field
- Change in the `paused` field
- Change in the `safetyState` object
- Change in the `newBaseRequest` field
- Change in the `lastNodeId` or `lastNodeSequenceId` field
- Change in the `edgeRequests` or `zoneRequests` arrays
- Change in the `powerSupply.charging` field
- Change in the `nodeStates` or `edgeStates` arrays
- Change in the `actionStates`, `instantActionStates` or `zoneActionStates` arrays
- Change in the `zoneSets` array
- Change in the `maps` array

*Remark: For above mentioned arrays, changes in the individual items of the array as well as adding or removing entries shall trigger a state message transmission.*

There should be an effort to curb the amount of communication.
If two events correlate with each other (e.g., the receiving of a new order usually forces an update of the `nodeStates` and `edgeStates`; as does the driving over a node), it is sensible to trigger one state update instead of multiple. The minimum time between two consecutive state messages is defined by the factsheet ([7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) `protocolLimits.timing.minimumStateInterval`) .

### 6.6.1 Concept and logic

The order progress is tracked by the `nodeStates` and `edgeStates`.
Additionally, if the mobile robot is capable of determining its current position, it shall publish it via the `mobileRobotPosition` field.

The `nodeStates` and `edgeStates` include all upcoming nodes and edges for the mobile robot to traverse.

![Figure 18 Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted](./assets/order_information_state_topic.png)
>Figure 18 - Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted

### 6.6.2 Traversal of nodes and edges

The mobile robot decides on its own when a node should count as traversed.
A requirement for the traversal is that the mobile robot's control point shall be within the node's `allowedDeviationXY` and its orientation within `allowedDeviationTheta`.
The `allowedDeviationXY` defines at what point a line-guided mobile robot can deviate from its predefined trajectory, to cut the corner along a smoother path rather than reaching the node's exact position. When leaving the `allowedDeviationXY` the mobile robot shall be back on its predefined trajectory of the subsequent edge.
If the edge attribute `corridor` of the subsequent edge is set, these boundaries should be met additionally.

In case the mobile robot is located too far away from the first node of an order, the fleet control can add an extended `allowedDeviationXY` to this node to include the mobile robot's current position.

The mobile robot shall report the traversal of a node by removing its `nodeState` from the `nodeStates` array and setting the `lastNodeId` and `lastNodeSequenceId` to the traversed node's values.

As soon as the mobile robot reports the node as traversed, the mobile robot shall trigger the actions associated with the node, if any.
The traversal of a node also necessarily implies leaving the edge that is leading up to the node.
The edge shall then also be removed from the `edgeStates` and the actions that were active on the edge shall be finished.

The traversal of the node also marks the moment when the mobile robot enters the following edge, if there is one.
The edge's actions shall be triggered, if any.
An exception to this rule is if the mobile robot shall stop on the node (because of a soft or hard blocking action) – then the mobile robot only enters the following edge once it begins driving again.

When an active order exists, the fields `lastNodeId` and `lastNodeSequenceId` shall be updated only when the mobile robot traverses a released node that is part of this order. For example if a physically line‑guided mobile robot detects a physical marker/tag that is not part of the active order’s `nodes`, this detection shall not lead to a change of `lastNodeId` or `lastNodeSequenceId`.

![Figure 19 Depiction of nodeStates, edgeStates, and actionStates during order handling](./assets/states_during_order_handling.png)
>Figure 19 - Depiction of `nodeStates`, `edgeStates`, and `actionStates` during order handling

#### 6.6.2.1 Definition of allowedDeviationXY as an ellipse

The allowedDeviationXY is defined as an ellipse around the node position to allow more flexible approaches to the node.

![Figure 20 allowedDeviationXY ellipse](./assets/ellipse.png)
>Figure 20 - allowedDeviation ellipse

### 6.6.3 Base request

If the mobile robot detects that its base is running short, it can set the `newBaseRequest` flag to "true" to attempt to prevent unnecessary braking.

### 6.6.4 Information

The mobile robot can submit arbitrary additional information to the fleet control via the `information` array.
It is up to the mobile robot to decide how long it reports information via an information message.

The fleet control shall not use the information for logic; they shall only be used for visualization and debugging purposes.

### 6.6.5 Errors

The mobile robot reports any issues via the `errors` array.

#### 6.6.5.1 Error levels

The issues can have four levels: 'WARNING', 'URGENT', 'CRITICAL', and 'FATAL'.

- A 'WARNING' level issue does not require immediate attention. The mobile robot can continue its current order and is able to take new orders. The error might be self-resolving, e.g., a dirty LiDar-scanner.
- An 'URGENT' level issue, e.g., a low battery level, requires immediate attention. The mobile robot can continue its current order and is able to take new orders.
- A 'CRITICAL' level issue requires immediate attention, e.g., trying to pick an object, that is not there. The mobile robot shall not continue driving since it can not continue its current order but is able to take new orders.
- A 'FATAL' level issue requires user intervention, e.g., losing localization. The mobile robot shall not continue driving since it can neither continue its currently active order nor take any new orders.

The mobile robot can add references that help with finding the cause of the error via the `errorReferences` array.
The fields `errorDescription` and `errorHint` may provide human-readable text explaining the error or suggesting a possible resolution.

Regardless of the level of the issue, the mobile robot shall never clear its order due to it.

#### 6.6.5.2 Error references

If an error occurs due to an erroneous order or execution failure, the mobile robot can return meaningful error references in the field `errorReferences` to support finding the cause of the error.
This can include the following information:

- `headerId`
- Topic (`order` or `instantAction`)
- `orderId` and `orderUpdateId` if error was caused by an order update
- `actionId` if error was caused by an action
- List of parameters if error was caused by erroneous action parameters

#### 6.6.5.3 Error translations

For both `errorDescription` and `errorHint`, the mobile robot can provide translations by using the `errorDescriptionTranslations` and `errorHintTranslations` arrays.
Each translation consists of an ISO 639-1 language code and the corresponding translated text.

#### 6.6.5.4 Predefined error types

The mobile robot shall use predefined error types to report specific issues. The following table lists the predefined error types and their description.

Error Type | Error level | Description | Reference | Report duration
---|---|---|---|---
'UNSUPPORTED_PARAMETER' | 'CRITICAL' | Receival of message with an unsupported optional parameter. | Name of parameter | Until new order is accepted.
'NO_ORDER_TO_CANCEL' | 'WARNING'  | The mobile robot received a `cancelOrder` action, but it does not have an active order to cancel. | `actionId` of `cancelOrder` | Until new order is accepted.
'VALIDATION_FAILURE'|'WARNING'| Receival of malformed order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_ORDER_ACTION' | 'WARNING' | Receival of an order containing unsupported actions. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_INSTANT_ACTION' | 'WARNING' | Receival of an unsupported instant action. | `actionId` of `instantAction` | Until new instant action is accepted.
'OUTDATED_ORDER_UPDATE'| 'WARNING' | Receival of an order with correct `orderId` but outdated `orderUpdateId`. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'SAME_ORDER_UPDATE_ID' | 'WARNING' | Receival of a duplicate order message (same `orderId` and `orderUpdateId`) | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'ORDER_UPDATE_FOLLOWING_CANCEL' | 'WARNING' | Receival of an order update for an order that has already been cancelled. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'OUTSIDE_OF_CORRIDOR' | 'CRITICAL' | Leaving the corridor defined for an edge. | `edgeId` | Until the mobile robot is no longer violating the corridor boundaries.
'INSUFFICIENT_MEMORY' | 'URGENT' | Mobile robot does not have enough memory to process received order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'DUPLICATE_MAP' | 'WARNING' | Receival of a map with `mapId` and `mapVersion` already existing. | `mapId` and `mapVersion` of duplicate | Until a new map related instantAction was accepted.
'BLOCKED_ZONE_VIOLATION' | 'CRITICAL' | Entering a 'BLOCKED' zone. | `zoneId` | Until the mobile robot is no longer violating the blocked zone.
'DUPLICATE_ZONE_SET' | 'WARNING' | Receival of a zone set with `zoneSetId` already existing. | `zoneSetId` or `actionId` of `instantAction` | Reasonable amount of time for the fleet control to notice that the zone update failed.
'RELEASE_LOST' | 'CRITICAL' | Losing the release for a 'RELEASE' zone. | `zoneId` | Until the mobile robot is no longer within the 'RELEASE' zone or is granted a the release again.
'ZONE_ACTION_CONFLICT' | 'CRITICAL' | Conflict between zone behavior and zone actions. | `zoneId` of 'ACTION' zone | Until the mobile robot is no longer violating the zone behavior.
'NODE_UNREACHABLE'|'CRITICAL'| The mobile robot cannot reach a node in its order. | `nodeId` | Until new order is accepted.
'LOCALIZATION_ERROR'|'FATAL'| The mobile robot is not localized. | | Until localization is regained.
'NO_ROUTE_TO_TARGET' | 'WARNING' | Receival of an order with at least one unreachable node. | `orderId` | Until new order is accepted.
'OTHER_ORDER_ACTIVE' | 'WARNING' | Receival of a new order while another order is still active. | `orderId` | Until new order is accepted.
'START_NODE_OUT_OF_RANGE' | 'WARNING' | Receival of an order with unreachable first node. | `orderId` | Until new order is accepted.
'MOBILE_ROBOT_NOT_AVAILABLE' | 'WARNING' | Receival of an order while not in 'AUTOMATIC', 'SEMIAUTOMATIC' or 'INTERVENED' operating mode. | `orderId` | Until operating mode allows for new orders
'UNKNOWN_MAP_ID' | 'WARNING' | Receival of an order containing nodes referencing an unknown `mapId`. | `orderId` | Until new order is accepted.

> Table 9 - Predefined error types

### 6.6.6 Operating Mode
…(발췌: 전체 207,642자 중 앞 110,737자)
````
