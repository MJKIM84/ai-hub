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
- verification_stage: second
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
        "ref-1084"
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
        "ref-948"
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
        "ref-948"
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
        "ref-948"
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
        "ref-948"
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
        "ref-937"
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
        "ref-947"
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
        "ref-991"
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
        "ref-948",
        "ref-031",
        "ref-004",
        "ref-1084",
        "ref-991"
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
        "ref-937"
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
        "ref-1084",
        "ref-991",
        "ref-1196",
        "ref-1200",
        "ref-1201",
        "ref-948"
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
        "ref-947",
        "ref-1200",
        "ref-031",
        "ref-004",
        "ref-937",
        "ref-1084",
        "ref-991",
        "ref-1203",
        "ref-1195",
        "ref-948",
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
      "id": "ref-1084",
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
      "id": "ref-947",
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
      "id": "ref-937",
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
      "id": "ref-991",
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
      "id": "ref-948",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1195~ref-948, 예약 구간 안)로 신규 출처 상한에 도달해 ANSI 블로그(R15.08-3-2026)·IFR 서비스 로봇 정의 문서·RoMi-H 등재 프로그램 페이지를 출처로 더하지 못했다. 재사용 2건(ref-004, ref-031): 참고문헌 목록 전체가 입력에 없어 ref-004 값은 researcher.md 예시, ref-031 값은 이전 브리프 2026-09-25-09 출처 표를 따랐고 이번에 GitHub 공식 저장소 원본을 다시 열었다. 원문 열람: 16건 열었고(webfetch 14, github_raw 2) ISO/IEC/IEEE 29148(ref-1207)만 403 으로 못 열어 source_unopened 로 표시했다. PDF 출처(IFR 요약, DTU, WER 2017, ARIA 보고서)는 본문 추출에 실패해 쓰지 않았다. 교차 확인 1건(f14, 한림대성심병원 업무 종류: ZDNet·비즈한국 두 기사). 기사 근거 finding(f15·f16·f17·f19·f20·f22)은 low 로 두었고, 카카오모빌리티 성과 수치(f20)는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가)에는 f26 으로 답했고 결론은 '맡기는 일은 반복적 비임상·실내 운반과 정보 전달이 중심이고 사용자와 함께 선정하며, 플랫폼 책임 범위는 규격이 정하지 않아 제조사 연동 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해진다'는 추정이다. 현장 유형 사례는 병원(f10~f18)·상업 시설(f19·f20)·제조 공장(f21·f22)·물류창고(f24)·실외(f25)이며 가정·기타는 찾지 못했다. 국내 자료는 산업통상자원부 2건(ref-1196, ref-991)·한국로봇산업진흥원(ref-947)·로봇학회논문지(ref-1204)·기사 4건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음. 용어집에 이미 있는 플릿 제어 수준·서비스형 로봇·공공 영역 이동로봇·등재 프로그램·실외이동로봇 운행안전인증·의료 로봇 미들웨어 RoMi-H·로봇 친화형 건축물 인증·로봇–작업 적합도 행렬은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### runs/2026-09-30-14/verification.json

```json
{
  "run_id": "2026-09-30-14",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IFR 뉴스 페이지(World Robotics 2025 서비스 로봇 편)를 열어 약 20만 대(+9%), 운송·물류 102,900대(+14%), 접객 42,000대 이상(-11%), 전문 청소 25,000대 이상(+34%), 농업 19,500대(-6%)를 대조했다. 집계 주체인 IFR의 1차 발표라서 단일 출처지만 [사실]을 유지한다. 본문에 2024년 판매 기준과 IFR 발표임을 밝힌다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 인력 부족이 주요 동기라는 문장과 운송·물류 RaaS 42% 성장이 같은 IFR 페이지에 있다. 직접 인용은 이 출처에서 1회만 한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ISO 페이지 403). 검색 결과로 ISO OBP 항목과 제목·기관이 일치함을 확인했다. 요구 공정·정보 항목·StRS(수용 기준 포함, 구현 방법 없음) 서술은 스니펫 범위 안이다. 신뢰도는 medium이 상한이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IEC SyC Smart Energy 페이지에 기원(IEC PAS 62559:2008, IntelliGrid), 2부(2015) 템플릿, 3부(2017) XML 직렬화, 4부 기업 프로젝트 적용 지침이 있다. 1부(2019)는 브리프에 없지만 문제되지 않는다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. evidence_excerpt의 'Industrie 4.0'은 IEC 페이지에 없다. 페이지가 드는 적용 분야는 스마트그리드·스마트시티·스마트홈/빌딩·AAL이며, 로봇 적용 언급은 없다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: The Robot Report(2023-10-26)에서 위험성평가를 통합자가 한다는 인용과 사용 정보 제공, 사용자의 교육·안전 작업, 개조한 사용자가 제조사·통합자 역할을 맡는다는 내용을 대조했다. 표준 원문은 미열람이고 전문지 기사 기준이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-031.txt(VDA 5050 3.0.0)의 5.3절(관제 기능), 5.4절(로봇 기능), 2절(범위 밖 항목: 안전 요구, 교통 관리 로직, 다른 통신 인터페이스, 프로젝트·시운전 절차, 운영 책임, 사이버보안)과 일치한다. 발행일은 미확인이며 3.0.0 판을 기준으로 적는다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-004.txt(rmf-core.md)의 Fleet adapter type 표(Full Control, Traffic Light, Read Only, No Interface)와 일치한다. 공유 공간당 Read Only 플릿은 최대 1개이고, 인터페이스 없음은 교착 가능성이 크다는 서술도 원문에 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f7·f8을 근거로 한 추정이며 두 근거 모두 원문으로 확인했다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문에서 샤리테 RoMi 프로젝트, 반휴머노이드 로봇, 정보 전달·물품 배달·음료 배급, 간호 인력의 적용 시나리오·능력 요구·평가 기준 공동 개발을 확인했다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: n=30, 상관계수 rs 0.740·0.628·0.505·-0.516과 투명한 전달·직접 체험 결론이 원문과 같다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "핵심 내용 확인: 병원 직원과 협업해 검체 운반을 과제로 정했고, 중환자실에서 검사실로 운반했으며, 검사실 직원이 꺼낸 뒤 터치스크린으로 확인했다. 다만 병원 현장에는 TIAGo 한 종만 투입했고 TIAGo·Jackal 이기종 관리는 시험 환경에서 확인했으므로 '이기종 로봇 플릿은 RMF로 조율했다'는 문구를 정정해야 한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 반자동문(RFID·근접 센서), 좁은 복도·혼잡, 문 열기 장치 전원 소진이 원문에 있다. 저자들은 'Safe integration of legacy infrastructure'와 혼잡 시 안전 구역 대기(RMF 미지원)를 과제로 들었다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: ZDNet(2024-09-19)과 비즈한국(2025-04-10) 두 매체가 모두 약제·검체 운반, 물품 배송, 환자 안내를 전해 교차 확인했다. 두 기사가 전하는 업무 목록은 일부 다르다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ZDNet은 7종 73대와 누적 35,492건(2022-08~2024-05 말)과 전용 승강기를, 비즈한국은 11종 77대를 전한다. 기준 시점이 다른 두 값을 모두 제시하고 한쪽을 고르지 않는다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 기사는 발언자를 '상급종합병원의 A 교수'(익명)로 적었고, 검체 이송은 컨베이어·인력 운송이 더 빠르고 안전하며 병원 물류가 복잡하다고 전한다. '시간에 민감한 업무'라는 표현은 기사에 없다(기사에는 '시간이 중요하지 않은 업무'라는 표현이 있다). 발언자 표기와 문구를 정정해야 한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 기사는 한국보건산업진흥원의 '디지털시대 의료서비스 혁신을 위한 스마트병원 육성방안 연구' 보고서를 인용해 경사 구간, 수동문, 건물이 나뉜 경우 건물마다 다른 회사 승강기를 든다. 보고서 원문은 미확인(재인용)이다. '구역마다 다른 승강기 시스템'은 기사 표현에 맞게 고쳐야 한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CGH CHART 페이지에 상호운용 요구 문장, 네 도메인(Machine·Control·Central·Integration), 2018-07 발표와 2019-10-31 ROSCon 공개가 있다. 페이지 발행일은 미확인이다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 강등. 로보티즈(제조)·카카오모빌리티(플랫폼·배송 서비스 운영)·호텔(서비스 적용·운영)의 역할 분담은 기사 보도로 확인했으므로 [사실](기사 보도)로 둘 수 있다. 플랫폼 기능 목록(QR 주문, 수요–공급 예측, 이기종 통합 관제, 인프라·보안·장애 관리, 운영 컨설팅)은 회사 설명이므로 [추정]으로 낮추고 '벤더 주장'을 병기한다. 기사 표현은 '매칭'이 아니라 '실시간 수요–공급 예측 알고리즘'이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 기사도 모든 수치를 회사 발표로 적는다. 추정·벤더 주장 표시가 적절하다. 측정 기간과 산정 방법은 미공개다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 산업통상자원부 보도자료(2020-06-25)에 표준공정모델 14개, 뿌리·섬유·식음료·자동차 업종, 60개 기업, 패키지 지원 문구, 지원단 6개 기관이 있다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇신문 기사 제목은 '제조 로봇 표준공정 모델 적용 사업 국내를 넘어 해외 공장까지 진출'(2025-09-15)이다. 64종, 148건, 수요기업 135·공급기업 89, 베트남 적용이 기사와 같다. 기관 수치이며 low를 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 한국로봇산업진흥원 페이지에서 수요처 주관·로봇기업 참여, 국비는 도입 비용의 50% 이내, 민간 부담은 총사업비의 50% 이상, 수요기관 부담은 25% 이상임을 확인했다. 지원 분야는 '물류·웨어러블·의료·기타'가 아니라 물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료(수술·재활)·협동로봇·언택트 서비스로 게시돼 있어 정정해야 한다. 게시일은 미확인이며 확인일(2026-09-30)을 기준으로 한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇학회논문지 17(4), 2022-11-30 초록에 계약물류·택배·풀필먼트, 이송·핸들링·지원(하차 자동화·웨어러블 슈트) 분류, 물류 특성에 맞는 기술·운영 방법 선택이 있다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 정책브리핑(2023-11-16, 산업통상자원부·경찰청)에서 11-17 시행, 500kg·15km/h 이하, 16개 시험항목, 배달·순찰 허용, 보험·공제 가입 의무, 범칙금 3만 원을 확인했다. '연계 대상:' 표시가 적절하다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지, 문구 정정 필요. f14에 실외 배송이 있어 '실내' 한정은 근거가 없다. f16 인용은 정정한 발언자 표기('상급종합병원의 한 교수 의견')에 맞춘다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 근거 finding(f3·f4·f7·f8·f10·f11·f18)은 모두 확인했다. '플릿 연동 수준'은 용어집 표기 '플릿 제어 수준'으로 통일한다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 분류 원문 19장 경계(시설·설비 제어, 업종별 조건, 로봇 자체 지능)에 맞게 연계 대상을 구분했다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 연결 영역의 번호와 이름이 부록 A와 일치한다."
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
      "ref-031(VDA 5050 VDA5050_EN.md)은 같은 날 실행 2026-09-30-13의 ref-1170과 URL이 같다. 이번 페이지는 기존 id인 ref-031을 쓰고, 두 id는 퍼블리셔가 합친다.",
      "ref-004는 참고문헌 목록에 등록된 URL을 입력으로 받지 못했다. 이번 실행이 인용한 RMF Core Overview 장(rmf-core.html)과 같은 문서인지 확인이 필요하다.",
      "f8의 네 단계는 용어집 fleet-control-level(플릿 제어 수준)과 같은 개념이다. 새로 정의하지 말고 용어집에 링크한다.",
      "f18 RoMi-H, f2 RaaS, f25 운행안전인증, f6 위험성평가·사용 정보는 용어집에 이미 있다(robotic-middleware-for-healthcare, robot-as-a-service, outdoor-mobile-robot-operational-safety-certification, risk-assessment, information-for-use). 새로 등록하지 않고 링크한다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "브리프 f8·f9·f27·f29와 페이지 제안의 '플릿 연동 수준'은 용어집의 '플릿 제어 수준(Fleet Control Level)'과 다른 표기다. 용어집 표기로 통일한다.",
      "용어 후보 '사용 사례 템플릿'의 정의에 있는 '목표·시나리오와 함께'는 이번에 확인한 IEC 페이지 범위(사용 사례·행위자 목록·요구사항 목록 템플릿)를 넘는다. 템플릿 세부 필드는 미확인이다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f19: 역할 분담(로보티즈 제조, 카카오모빌리티 플랫폼·배송 서비스 운영, 호텔 서비스 적용·운영)만 [사실](아시아경제 보도)로 쓴다. 플랫폼 기능 목록은 [추정]으로 강등하고 '벤더 주장'을 병기한다. '수요–공급 매칭'은 기사 표현인 '실시간 수요–공급 예측 알고리즘'으로 고친다 — 기능 설명의 출처가 회사 발표이고 독립 확인이 없다.",
    "f16: 발언자를 '의대 교수'에서 '상급종합병원의 한 교수(기사에 익명 표기)'로 고친다. 내용은 '검체 이송은 컨베이어·인력 운송이 더 빠르고 안전하며 병원 물류가 복잡해 로봇이 맡기 어렵다'는 [의견]으로 쓰고 '시간에 민감한 업무'라는 표현은 쓰지 않는다 — 비즈한국 원문과 대조한 결과다.",
    "f26: '반복적인 비임상·실내 운반'에서 '실내'를 빼고, f16 인용은 정정한 발언자 표기에 맞춘다 — f14에 실외 배송이 포함돼 있다.",
    "f12: '이기종 로봇 플릿은 RMF로 조율했다'를 '병원 현장에는 TIAGo를 투입했고, RMF로 TIAGo·Jackal 이기종 로봇을 관리하는 것은 시험 환경에서 확인했다'로 고친다 — Valner 외 원문 기준이다.",
    "f17: '건물 구역마다 다른 승강기 시스템'을 '건물이 나뉜 경우 건물마다 다른 회사의 승강기가 설치돼 통신 연동이 어렵다'로 고친다. 인용된 보고서를 한국보건산업진흥원의 '디지털시대 의료서비스 혁신을 위한 스마트병원 육성방안 연구'로 밝히고 '보고서 원문 미확인(기사 재인용)'을 병기한다.",
    "f23: 지원 분야를 '물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료(수술·재활)·협동로봇·언택트 서비스'로 고친다. 민간 부담 50% 이상과 수요기관 부담 25% 이상은 '총사업비 대비'로 적고, 기준일은 확인일 2026-09-30으로 둔다 — 한국로봇산업진흥원 게시 내용과 대조했다.",
    "f5: 본문에 'Industrie 4.0'을 적용 분야로 쓰지 않는다. IEC 페이지가 드는 분야는 스마트그리드·스마트시티·스마트홈/빌딩·능동형 생활 보조(AAL)다.",
    "f3(ref-1207): 본문에서 ISO/IEC/IEEE 29148의 내용은 '검색 결과 요약 기준'임을 밝힌다. ref-1207 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates의 ref-1207 항목에 source_unopened: true를 넣는다 — ISO 페이지 403으로 원문을 열지 못했다.",
    "f6: 본문에서 ANSI/A3 R15.08-2의 역할 규정은 'The Robot Report 기사(2023-10-26)에 따르면'으로 출처를 밝히고 '표준 원문 미열람'을 적는다. 이 내용은 48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사로 연결하는 연계 대상으로만 짧게 다룬다.",
    "f7(ref-031): VDA 5050 내용은 '3.0.0 판 기준'임을 본문에 밝히고 기존 ref-031 각주를 재사용한다(새 id를 만들지 않는다).",
    "f8(ref-004): 각주는 docs/references/ref-004.md의 '각주 형식' 줄을 그대로 쓰고, 본문에 인용 위치(Programming Multiple Robots with ROS 2의 RMF Core Overview 장)를 밝힌다.",
    "용어: '플릿 연동 수준'을 모두 '플릿 제어 수준(Fleet Control Level)'으로 바꾸고 용어집 fleet-control-level에 링크한다. RoMi-H·서비스형 로봇·실외이동로봇 운행안전인증·위험성평가·사용 정보도 기존 용어집 항목에 링크하고 새로 등록하지 않는다.",
    "용어 후보 '사용 사례 템플릿'의 정의를 'IEC 62559-2가 정한 양식으로, 사용 사례·행위자 목록·요구사항 목록을 구조화해 기록하게 한다'로 줄이고 '목표·시나리오'는 뺀다 — 템플릿 세부 필드는 미확인이다.",
    "열린 질문 2번의 '시간에 민감한 업무에서'를 '검체 이송 같은 업무에서'로 고친다 — f16 정정에 맞춘다.",
    "5절: 현장 유형을 병원(f10~f18, f18은 싱가포르 공공 의료기관의 조달 제약)·상업 시설(f19·f20)·제조 공장(f21·f22)·물류창고(f24)·실외(f25, 연계 대상으로 표시)로 나눠 쓰고, 가정·기타 현장 사례는 찾지 못했음을 적는다. f15의 두 규모 수치는 보도 시점과 함께 둘 다 제시한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 29건, 미확인 0건, 교차 확인 1건(f14). 강등: f19의 플랫폼 기능 목록 부분을 사실 → 추정(벤더 주장)으로 낮췄다. 역할 분담 보도는 [사실]로 둔다. 원문 미열람 출처: ref-1207(ISO/IEC/IEEE 29148, 검색 결과 일치로 실재 확인). 정정한 문구: f12(병원 현장은 TIAGo 한 종, 이기종 관리는 시험 환경), f16(발언자 '상급종합병원의 한 교수'), f17(건물마다 다른 회사 승강기), f23(지원 분야), f26('실내' 삭제). 주의: 핵심 수치와 사례가 대부분 단일 출처다. 한국 병원·호텔 사례는 기사 중심이고 카카오모빌리티 성과 수치는 벤더 주장이다. ANSI/A3 R15.08-2는 전문지 기사 기준이다. 플랫폼 책임 범위에 관한 결론(f9·f26·f27·f28)은 추정이다. 가정·기타 현장 사례는 찾지 못했다. ref-031은 같은 날 등록된 ref-1170과 URL이 같아 퍼블리셔가 합쳐야 한다. ref-004는 등록된 URL과 이번에 인용한 RMF Core Overview 장이 같은 문서인지 확인하지 못했다. 정정 요청과 해결 제안된 열린 질문은 없다. 검증 검색 1회(리서치와 합쳐 17회/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-14/pages.json

```json
{
  "run_id": "2026-09-30-14",
  "outline": [
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1100,
      "summary": "로봇에게 맡겨지는 일은 반복적인 비임상 운반과 정보 전달이 중심이고, 일은 현장 사용자와 함께 고르며, 플랫폼 책임 범위는 규격이 정해 주지 않아 도입 단계에서 정해지는 것으로 보인다. [추정][^ref-1195][^ref-031][^ref-004]",
      "planned_findings": [
        "f26",
        "f1",
        "f2",
        "f16",
        "f7",
        "f8",
        "f9"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "사용 사례 템플릿(IEC 62559-2), 이해관계자 요구사항 명세(StRS), 제조사·통합자·사용자 역할, 플릿 제어 수준, 로봇활용 표준공정모델이 이 영역의 기본 용어다. [사실][^ref-1206][^ref-1207][^ref-004]",
      "planned_findings": [
        "f4",
        "f3",
        "f6",
        "f8",
        "f21"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3200,
      "summary": "병원 세 사례(타르투·샤리테·한림대성심)와 싱가포르 조달 요구, 상업 시설(호텔 룸서비스), 제조 공장(표준공정모델), 물류창고(물류 유형별 로봇 분류), 실외(보도 배달·순찰, 연계 대상)를 여섯 항목으로 정리했다. 가정·기타 현장 사례는 찾지 못했다. [사실][^ref-1200][^ref-1203][^ref-991]",
      "planned_findings": [
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1100,
      "summary": "현장 사용자와의 공동 설계, 업종별 표준공정 목록, 수요처 주관 실증이 사례로 확인됐고, 사용 사례 템플릿 표준의 로봇 적용 사례는 찾지 못했다. [사실][^ref-1195][^ref-1196][^ref-947]",
      "planned_findings": [
        "f10",
        "f11",
        "f12",
        "f21",
        "f22",
        "f23",
        "f4",
        "f5"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1300,
      "summary": "IEC 62559, ISO/IEC/IEEE 29148, ANSI/A3 R15.08-2(연계 대상), VDA 5050 3.0.0, Open-RMF, RoMi-H, 로봇활용 표준공정모델, 서비스로봇 실증사업을 이 영역과의 관계로 정리했다. [사실][^ref-1206][^ref-031]",
      "planned_findings": [
        "f4",
        "f3",
        "f6",
        "f7",
        "f8",
        "f18",
        "f21",
        "f23"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 800,
      "summary": "샤리테 간호사 수용성 연구, 타르투 병원 현장 시험, 국내 물류현장 로봇적용 논문, IFR 서비스 로봇 발표, 산업통상자원부 표준공정모델 발표, RoMi-H 자료가 대표 자료다. [사실][^ref-1195][^ref-1200]",
      "planned_findings": [
        "f10",
        "f12",
        "f24",
        "f1",
        "f21",
        "f18"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1000,
      "summary": "ROP는 사용 사례·요구 명세의 틀, 플릿마다의 조율 범위 명시, 상호운용 요구 제시, 평가 기준 관리를 맡고, 위험성평가·설비 개조·인증·보험·공정 컨설팅은 외부 주체에 연계하는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-1084]",
      "planned_findings": [
        "f27",
        "f28",
        "f7",
        "f8",
        "f25"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "시장 동향·경제성·관제 연동·상호운용·설비 연동·워크플로·안전·현장 조사·다사업자 책임·법규·수용성과 현장 유형 다섯 영역으로 이어진다. [추정][^ref-1198][^ref-031]",
      "planned_findings": [
        "f29"
      ]
    },
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "책임 분담 계약 사례, 검체 이송 수단 비교 연구, 사용 사례 템플릿의 로봇 적용, 한국 공공 조달의 상호운용 요구, 가정·기타 현장 사례가 열린 질문이다.",
      "planned_findings": [
        "f7",
        "f16",
        "f5",
        "f18",
        "f26"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(현장 유형 사례 7건: 병원 3·상업 시설·제조 공장·물류창고·실외, 표준·프레임워크 8건, 자료 6건, 경계 3행, 연결 17개, 열린 질문 5건), 프런트매터 related_areas·tags·confidence·sources·last_run 채움, 13절 각주 17건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,461자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,149자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"8. 대표 연구와 자료\" 절(954자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"6. 대표 접근법과 기술\" 절(951자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"3. 왜 중요한가\" 절(890자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"4. 핵심 개념과 용어\" 절(878자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area02-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 2. 사용 사례·요구·책임 범위 의 \"11. 열린 질문\" 절(669자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 2. 사용 사례·요구·책임 범위 | 섹션 3~11 신규 작성(병원·상업 시설·제조 공장·물류창고·실외 사례 7건, 표준·프레임워크 8건, 연결 17개, 열린 질문 5건), 1차 조건부 승인 수정 15건 이행 | run 2026-09-30-14",
  "index_updates": {
    "home_recent": "2026-09-30 — 2. 사용 사례·요구·책임 범위: 섹션 3~11 신규 작성(병원·상업 시설·제조 공장·물류창고·실외 사례 7건, 표준·프레임워크 8건, 연결 17개, 열린 질문 5건)",
    "category_recent": "2026-09-30 — 2. 사용 사례·요구·책임 범위: 섹션 3~11 신규 작성(사용 사례 템플릿·요구 명세 표준, 플릿 제어 수준에 따른 책임 범위, 현장 유형 사례 7건, 열린 질문 5건)",
    "area_recent": "2026-09-30 — 2. 사용 사례·요구·책임 범위: 섹션 3~11 신규 작성, 신뢰도 medium, 각주 17건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "use-case-template",
      "term_ko": "사용 사례 템플릿",
      "term_en": "Use Case Template (IEC 62559-2)",
      "definition": "IEC 62559-2가 정한 양식으로, 사용 사례·행위자 목록·요구사항 목록을 구조화해 기록하게 한다.",
      "description": "IEC 62559 사용 사례 방법론의 2부(2015)가 정한다. 템플릿의 세부 필드는 이번 조사에서 확인하지 못했다. 로봇 오케스트레이션에 적용한 사례는 확인되지 않았다.",
      "related_areas": [
        2,
        24
      ],
      "sources": [
        "ref-1206"
      ]
    },
    {
      "action": "new",
      "slug": "stakeholder-requirements-specification",
      "term_ko": "이해관계자 요구사항 명세",
      "term_en": "Stakeholder Requirements Specification (StRS)",
      "definition": "ISO/IEC/IEEE 29148이 정한 요구공학 산출물의 하나로, 사용자와 이해관계자가 시스템에 기대하는 것을 구현 방법 없이 수용 기준과 함께 적은 문서다.",
      "description": "표준 원문 미열람, 검색 결과 요약 기준의 정의다.",
      "related_areas": [
        2
      ],
      "sources": [
        "ref-1207"
      ]
    },
    {
      "action": "new",
      "slug": "robot-standard-process-model",
      "term_ko": "로봇활용 표준공정모델",
      "term_en": "Robot Standard Process Model (Korea)",
      "definition": "업종별 제조 공정에 로봇을 적용하는 방법을 표준화한 국내 참조 모델로, 수요기업이 공정을 골라 로봇 도입·실증에 쓰도록 정부 지원 사업과 연계해 개발·보급된다.",
      "description": "산업통상자원부는 2020년 뿌리·섬유·식음료·자동차 업종의 14종 개발과 패키지 지원을 발표했다.",
      "related_areas": [
        2,
        62
      ],
      "sources": [
        "ref-1196",
        "ref-1197"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. 이번 실행에서 플릿 제어 수준(Full Control·Traffic Light·Read Only·No Interface) 절을 확인했다.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1084",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ANSI/A3 R15.08-2(산업용 이동로봇 시스템·적용 안전 요구) 발행 소식과 제조사·통합자·사용자 역할 요약. 표준 원문과 ANSI 블로그는 403 으로 열지 못했고 ANSI 블로그 검색 요약과 내용이 일치한다.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "summary": "타르투 대학병원에서 중환자실→검사실 혈액 검체 운반을 시험한 현장 연구. 병원 현장에는 TIAGo 를 투입했고 RMF 로 TIAGo·Jackal 이기종 로봇을 관리하는 것은 시험 환경에서 확인했다.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-947",
      "org": "한국로봇산업진흥원",
      "title": "서비스로봇 실증사업",
      "published": null,
      "url": "https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "수요처 주관·로봇기업 참여 컨소시엄, 국비·민간 부담 비율(총사업비 대비), 지원 분야와 선정 절차를 설명한 사업 소개 페이지.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-937",
      "org": "Changi General Hospital, CHART",
      "title": "ROMI-H",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "싱가포르 공공 의료기관 로봇의 상호운용 요구와 RoMi-H 네 도메인 구조, 공개 연혁을 설명한 창이종합병원 CHART 페이지.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
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
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-991",
      "org": "산업통상자원부·경찰청 (대한민국 정책브리핑)",
      "title": "‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인)",
      "published": "2023-11-16",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922726",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개정 지능형로봇법 시행(2023-11-17)으로 운행안전인증 실외이동로봇의 보도 통행과 배달·순찰을 허용하고 운영자 보험 가입 의무를 둔다는 정부 보도자료.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-948",
      "org": "비즈한국",
      "title": "병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인)",
      "published": "2025-04-10",
      "url": "https://bizhankook.com/articles/29394.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원 등 국내 병원의 서비스 로봇 운용(11종 77대)과 의료진 의견, 한국보건산업진흥원 보고서의 도입 장애 요인을 전한 기사.",
      "cited_by": [
        "docs/categories/planning-and-business/use-cases-requirements-and-scope.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가?",
      "areas": [
        2,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원 검체 이송 같은 업무에서 로봇·컨베이어·사람 운반을 같은 조건으로 비교해 로봇에게 맡길 업무를 정한 정량 연구가 있는가?",
      "areas": [
        2,
        63
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가?",
      "areas": [
        2,
        24
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가?",
      "areas": [
        2,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "가정·공동주택과 기타 현장(공공시설·연구실 등)에서 여러 로봇에게 맡길 일과 요구를 사용자와 함께 도출한 연구나 실증 사례가 있는가?",
      "areas": [
        2,
        65,
        67
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시",
      "title": "2. 사용 사례·요구·책임 범위"
    }
  ],
  "standards_updates": [
    {
      "name": "IEC 62559 사용 사례 방법론 (Part 1~4)",
      "kind": "표준",
      "org": "IEC",
      "url": "https://syc-se.iec.ch/deliveries/iec-62559-use-cases/",
      "related_areas": [
        2,
        24
      ],
      "summary": "IEC PAS 62559:2008(IntelliGrid)에서 나온 사용 사례 방법론. 2부(2015)는 사용 사례·행위자 목록·요구사항 목록 템플릿, 3부(2017)는 XML 직렬화, 4부는 표준화·기업 프로젝트 모범 사례를 다룬다.",
      "ref_id": "ref-1206"
    },
    {
      "name": "ISO/IEC/IEEE 29148:2018 요구공학",
      "kind": "표준",
      "org": "ISO / IEC / IEEE",
      "url": "https://www.iso.org/standard/72089.html",
      "related_areas": [
        2
      ],
      "summary": "원문 미열람. 시스템·소프트웨어 수명주기 전체에 걸친 요구사항 도출·분석·문서화·검증·관리 공정과 이해관계자 요구사항 명세(StRS) 등 산출 정보 항목을 규정한다(검색 결과 요약 기준).",
      "ref_id": "ref-1207"
    },
    {
      "name": "로봇활용 표준공정모델",
      "kind": "프레임워크",
      "org": "산업통상자원부",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C",
      "related_areas": [
        2,
        62
      ],
      "summary": "업종별 제조 공정에 로봇을 적용하는 국내 참조 모델. 2020년 뿌리·섬유·식음료·자동차 업종 14종을 개발하고 컨설팅·실증 보급·교육·협동로봇 안전인증과 묶어 지원한다고 발표했다.",
      "ref_id": "ref-1196"
    }
  ],
  "additional_research_requests": [
    "13절 ref-004 각주: 지시대로 docs/references/ref-004.md 의 '각주 형식' 줄을 그대로 써야 하나 그 파일이 입력에 없어 브리프 출처 값(RMF Core Overview 장, rmf-core.html, 접근일 2026-09-30)으로 각주를 만들었다. 퍼블리셔 또는 다음 실행에서 ref-004 등록 URL·각주 줄과 이번 인용 장이 같은 문서인지 확인이 필요하다.",
    "ref-031 과 같은 날 등록된 ref-1170 은 URL 이 같아 퍼블리셔가 합쳐야 한다(1차 검증 지적).",
    "4절·7절: IEC 62559-2 사용 사례 템플릿의 세부 필드 목록(원문 미열람으로 미확인). 여섯 항목과의 대응을 구체적으로 쓰려면 필요하다.",
    "5절: 가정·공동주택과 기타 현장의 사용 사례 발굴·요구 정의 사례를 찾지 못했다. 현장 유형 균형을 위해 필요하다.",
    "5절 병원 사례: 한림대성심병원 서비스로봇 운용 규모의 최신 값(7종 73대 대 11종 77대, 기준 시점 상이)과 완료 확인 방식.",
    "5절 병원 사례: 한국보건산업진흥원 '디지털시대 의료서비스 혁신을 위한 스마트병원 육성방안 연구' 보고서 원문(현재 기사 재인용).",
    "4·7·9절: ANSI/A3 R15.08-2 표준 원문 또는 발행 기관 자료로 제조사·통합자·사용자 역할 규정을 재확인(현재 전문지 기사 기준).",
    "5절 상업 시설 사례: 카카오모빌리티 가동률·배송 성공률·매출 수치의 독립 출처와 측정 기간·산정 방법."
  ],
  "fixes_applied": [
    "f19 — 5절 상업 시설 사례의 수행 자원 칸에서 역할 분담(로보티즈 제조, 카카오모빌리티 플랫폼·배송 서비스 운영, 호텔 서비스 적용·운영)만 아시아경제 보도 기준 [사실]로 쓰고, 플랫폼 기능 목록은 별도 문장으로 [추정] 벤더 주장으로 낮췄으며 '수요–공급 매칭'을 '실시간 수요–공급 예측 알고리즘'으로 고쳤다(시작 조건 칸의 QR 주문도 벤더 주장 표시).",
    "f16 — 3절과 5절 국내 병원 사례 예외·성과 칸에서 발언자를 '상급종합병원의 한 교수(기사에 익명 표기)'로 고치고, 내용을 '검체 이송은 컨베이어·인력 운송이 더 빠르고 안전하며 병원 물류가 복잡해 로봇이 맡기 어렵다'는 [의견]으로 썼으며 '시간에 민감한 업무' 표현은 쓰지 않았다.",
    "f26 — 3절 첫 단락에서 '실내'를 빼 '반복적인 비임상 운반과 정보 전달'로 쓰고, f16 인용을 '상급종합병원의 한 교수 의견'으로 맞췄다.",
    "f12 — 5절 병원(타르투) 사례 수행 자원 칸과 8절 Valner 외 요약을 '병원 현장에는 TIAGo를 투입했고, RMF로 TIAGo·Jackal 이기종 로봇을 관리하는 것은 시험 환경에서 확인했다'로 썼다.",
    "f17 — 5절 국내 병원 사례 제약 칸을 '건물이 나뉜 경우 건물마다 다른 회사의 승강기가 설치돼 통신 연동이 어렵다'로 고치고 보고서명 '디지털시대 의료서비스 혁신을 위한 스마트병원 육성방안 연구'(한국보건산업진흥원)와 '보고서 원문 미확인, 기사 재인용'을 병기했다.",
    "f23 — 6절 수요처 주관 실증에서 지원 분야를 '물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료(수술·재활)·협동로봇·언택트 서비스'로 고치고, 민간 부담 50% 이상·수요기관 부담 25% 이상을 '총사업비 대비'로 적었으며 기준일을 '2026-09-30 확인 기준'으로 밝혔다.",
    "f5 — 6절 사용 사례 템플릿 소절에서 Industrie 4.0 을 쓰지 않고, IEC 페이지가 드는 적용 분야를 스마트그리드·스마트시티·스마트홈/빌딩·능동형 생활 보조(AAL)로 적고 로봇 적용 언급이 없음을 밝혔다.",
    "f3(ref-1207) — 4절 용어 항목과 7절 표에 '검색 결과 요약 기준'(7절은 '원문 미열람' 병기)을 밝히고, 13절 ref-1207 각주 접근일 뒤에 ' (원문 미열람)'을 붙였으며 reference_updates 의 ref-1207 에 source_unopened: true 를 넣었다.",
    "f6 — 4절 용어 항목과 7절 표에서 'The Robot Report 기사(2023-10-26)에 따르면'으로 출처를 밝히고 '표준 원문 미열람'을 적었으며, 7절 표는 '연계 대상'으로 표시하고 9절·10절에서 48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사로 짧게 연결했다.",
    "f7(ref-031) — 3·7·9절의 VDA 5050 내용에 '3.0.0 판 기준'을 밝히고, 새 id 없이 기존 ref-031 각주(A. 기획·사업 대분류 페이지 참고 자료의 줄, 접근일 2026-09-25)를 그대로 썼다.",
    "f8(ref-004) — 7절 표 Open-RMF 행에 인용 위치 'Programming Multiple Robots with ROS 2의 RMF Core Overview 장'을 밝혔다. 다만 docs/references/ref-004.md 가 입력에 없어 '각주 형식' 줄을 복사하지 못했고 브리프 출처 값으로 각주를 만들었다 — 퍼블리셔 확인 필요(additional_research_requests 에 기록).",
    "용어 — '플릿 연동 수준'을 쓰지 않고 3·4·7·9·10절 모두 '플릿 제어 수준(Fleet Control Level)'으로 통일해 용어집 fleet-control-level 에 링크했다. RoMi-H(robotic-middleware-for-healthcare)·서비스형 로봇(robot-as-a-service)·실외이동로봇 운행안전인증·위험성평가·사용 정보도 기존 용어집 항목에 링크하고 glossary_updates 에 새로 넣지 않았다.",
    "용어 후보 '사용 사례 템플릿' — 정의를 'IEC 62559-2가 정한 양식으로, 사용 사례·행위자 목록·요구사항 목록을 구조화해 기록하게 한다'로 줄여 glossary_updates 와 4절에 썼고 '목표·시나리오'는 뺐다.",
    "열린 질문 2번 — '시간에 민감한 업무에서'를 '검체 이송 같은 업무에서'로 고쳐 11절과 open_question_updates 에 반영했다.",
    "5절 — 현장 유형을 병원(타르투·샤리테·한림대성심 세 사례, 싱가포르 공공 의료기관의 조달 제약은 국내 병원 사례 서술에 명시)·상업 시설·제조 공장·물류창고·실외(사례 제목과 서술에 '연계 대상' 표시)로 나눠 쓰고, 절 첫머리에 가정·공동주택과 기타 현장 사례를 찾지 못했다고 적었으며, 한림대성심병원 규모 두 값을 보도 시점(2024-09-19, 2025-04-10)과 함께 모두 제시했다.",
    "분량 초과 자동 분리: 2. 사용 사례·요구·책임 범위 본문 11,737자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,624자"
  ]
}
```

### runs/2026-09-30-14/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area02-s7.md (1,461자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area02-s10.md (1,149자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area02-s8.md (954자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area02-s6.md (951자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area02-s3.md (890자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area02-s4.md (878자)
    - docs/categories/planning-and-business/use-cases-requirements-and-scope.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area02-s11.md (669자)
```

### runs/2026-09-30-14/pages/categories/planning-and-business/use-cases-requirements-and-scope.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위"
type: area
category: "A. 기획·사업"
area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [사용 사례, 요구공학, 책임 범위, 플릿 제어 수준, 수요처 주관 실증]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-004, ref-031, ref-1195, ref-1196, ref-1197, ref-1198, ref-1084, ref-1200, ref-1201, ref-947, ref-1203, ref-1204, ref-937, ref-1206, ref-1207, ref-991, ref-948]
last_run: 2026-09-30
version: 2
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

확인한 자료를 종합하면, 실제로 로봇에게 맡겨지는 일은 반복적인 비임상 운반과 정보 전달이 중심이다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 왜 중요한가](../../topics/2026/2026-09-30-area02-s3.md)에 있다.

## 4. 핵심 개념과 용어

로봇에게 맡길 일과 책임을 적는 데 쓰이는 용어는 요구공학 표준, 안전 표준의 역할 구분, 플랫폼 연동 구분, 국내 지원 사업에서 나온다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area02-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 병원·상업 시설·제조 공장·물류창고·실외 다섯 현장 유형에서 찾은 것이다. 가정·공동주택과 기타 현장의 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 병원

**사례:** 병원에서 혈액 검체를 중환자실에서 검사실로 운반(에스토니아 타르투 대학병원 현장 시험)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 중환자실 직원이 로봇의 터치스크린으로 운반을 시작했다. [사실][^ref-1200] |
| 작업 대상 | 혈액 검체. 연구진은 병원 직원과 협업해 검체·장비 운반을 자동화 대상으로 정했다. [사실][^ref-1200] |
| 수행 자원 | 병원 현장에는 TIAGo를 투입했고, RMF로 TIAGo·Jackal 이기종 로봇을 관리하는 것은 시험 환경에서 확인했다. 검체를 싣고 꺼내는 일은 사람이 맡았다. [사실][^ref-1200] |
| 제약 | RFID 카드나 근접 센서로 여는 반자동문, 좁은 복도, 많은 사람. [사실][^ref-1200] |
| 완료·인계 | 검사실 직원이 검체를 꺼낸 뒤 터치스크린으로 확인하는 방식으로 완료를 확인했다. [사실][^ref-1200] |
| 예외·성과 | 직접 만든 문 열기 장치의 전원이 떨어져 사람이 개입했다. [사실][^ref-1200] 처리량·시간·비용 영향은 확인하지 못했다. |

이 사례는 로봇에게 맡길 일을 정한 방식을 보여 준다. 연구진은 의료진이 검체·의료 장비 운반 같은 부차 업무에 시간을 쓴다는 점을 자동화 기회로 보고 병원 직원과 함께 과제를 정했다. [사실][^ref-1200] 저자들은 혼잡할 때의 대기와 기존 설비의 안전한 연동을 미해결 과제로 남겼다. [사실][^ref-1200]

**현장 유형:** 병원

**사례:** 병동에서 메시지·소형 물품·음료 전달(독일 샤리테 베를린 의대병원 RoMi 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병실 메시지 전달, 소형 물품 배달, 음료 배급 같은 비임상 업무. [사실][^ref-1195] |
| 수행 자원 | 반휴머노이드 서비스 로봇과 간호 인력. [사실][^ref-1195] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 간호사 30명의 기술 사용 목록(TUI) 응답에서 사용 의도는 지각된 유용성(rs=0.74)·접근성(rs=0.628)·사용성(rs=0.505)과 양의 상관을, 회의감(rs=-0.516)과 음의 상관을 보였다. [사실][^ref-1195] |

이 연구(2026-04 발표)는 간호 인력과 함께 적용 시나리오·능력 요구·평가 기준을 공동으로 정했다. [사실][^ref-1195] 연구진은 시스템 능력과 한계의 투명한 전달과 직접 체험 기회가 도입에 필요하다고 결론지었다. [사실][^ref-1195]

**현장 유형:** 병원

**사례:** 국내 병원의 약제·검체·물품 운반과 환자 안내(한림대성심병원 서비스로봇 실증)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 약제 배송, 검체 이송, 부서 간 물품 배송, 환자 안내 등. 두 기사가 전하는 업무 목록은 일부 다르다. [사실][^ref-1201][^ref-948] |
| 수행 자원 | ZDNet 기사(2024-09-19)는 7종 73대, 누적 35,492건(2022-08~2024-05)과 서비스로봇 전용 승강기 구축을, 비즈한국 기사(2025-04-10)는 11종 77대를 전했다. 기준 시점이 달라 두 값을 모두 적는다. [사실][^ref-1201][^ref-948] |
| 제약 | 비즈한국 기사는 한국보건산업진흥원의 '디지털시대 의료서비스 혁신을 위한 스마트병원 육성방안 연구' 보고서를 인용해 경사 구간, 수동문, 그리고 건물이 나뉜 경우 건물마다 다른 회사의 승강기가 설치돼 통신 연동이 어렵다는 점을 도입 장애로 들었다(보고서 원문 미확인, 기사 재인용). [사실][^ref-948] |
| 완료·인계 | 미확인 |
| 예외·성과 | 상급종합병원의 한 교수(기사에 익명 표기)는 검체 이송은 컨베이어·인력 운송이 더 빠르고 안전하며 병원 물류가 복잡해 로봇이 맡기 어렵다고 보았다. [의견][^ref-948] |

최신 운용 규모는 확인하지 못했다. 병원의 조달 조건도 사용 사례의 제약이 된다. 싱가포르는 공공 의료기관에서 시험·배치하는 로봇 시스템이 표준화되고 인정된 플랫폼으로 상호운용되도록 요구한다. [사실][^ref-937] 창이종합병원 CHART가 개발한 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)는 기계·제어·중앙(플릿 관리·로봇 간·설비 연동)·통합(응용 프로그램 인터페이스, API) 네 도메인으로 구성되고 2019-10-31 ROSCon에서 공개되었다. [사실][^ref-937]

**현장 유형:** 상업 시설

**사례:** 호텔 룸서비스 로봇 배송(신라스테이 서초·반얀트리 클럽 앤 스파 서울)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 룸서비스 주문. QR 주문은 카카오모빌리티가 설명한 플랫폼 기능이다. [추정] 벤더 주장[^ref-1203] |
| 작업 대상 | 호텔 룸서비스 배송 물품. [사실][^ref-1203] |
| 수행 자원 | 아시아경제 보도(2026-03-16)에 따르면 로보티즈는 배송 로봇을 만들고, 카카오모빌리티는 플랫폼과 배송 서비스를 운영하며, 호텔은 서비스를 적용·운영한다. [사실][^ref-1203] 플랫폼 기능으로 든 QR 주문, 실시간 수요–공급 예측 알고리즘, 이기종 로봇 통합 관제, 인프라·보안·장애 관리, 운영 컨설팅은 회사 설명이다. [추정] 벤더 주장[^ref-1203] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 카카오모빌리티는 플랫폼 도입 뒤 일평균 로봇 가동률이 도입 초기 대비 약 8배 오르고 배송 성공률 100%, 룸서비스 매출 약 3배 증가를 이뤘다고 주장한다. [추정] 벤더 주장[^ref-1203] |

이 사례는 로봇 제조사·플랫폼 사업자·현장 운영자가 역할을 나눈 구조다. 성과 수치의 측정 기간과 산정 방법은 공개되지 않아 독립 확인이 필요하다.

**현장 유형:** 제조 공장

**사례:** 업종별 로봇활용 표준공정모델로 로봇 적용 공정 고르기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 정부 지원 사업. 산업통상자원부는 2020년 표준공정모델 개발·공정개선 컨설팅·실증 보급·재직자 교육·협동로봇 안전인증을 묶은 패키지 지원을 발표했다. [사실][^ref-1196] |
| 작업 대상 | 뿌리·섬유·식음료·자동차 업종 60개 기업의 공정을 대상으로 표준공정모델 14종을 개발했다. [사실][^ref-1196] |
| 수행 자원 | 6개 연구기관이 지원단을 구성했다. [사실][^ref-1196] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

로봇신문 기사(2025-09-15)에 따르면 한국생산기술연구원은 2019년부터 뿌리산업·바이오화학 등 업종의 제조로봇 표준공정모델 64종을 개발해 실증사업에 148건을 공급했고, 2025년 베트남으로 첫 해외 적용을 넓혔다. [사실][^ref-1197] 이 수치는 한 기관의 수치이며 전체 사업 누계는 확인하지 못했다.

**현장 유형:** 물류창고

**사례:** 물류 서비스 유형별로 로봇 적용 고르기(계약물류·택배·풀필먼트)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 계약물류(팔레트·박스·낱개), 택배(분류·상하차), 풀필먼트(수백~수천 품목, 변동 수요). [사실][^ref-1204] |
| 수행 자원 | 이송 자동화(무인운반차(Automated Guided Vehicle, AGV)·자율이동로봇(Autonomous Mobile Robot, AMR)·자동 창고(ASRS)), 핸들링(박스 디팔레타이징·팔레타이징, 낱개 피킹), 지원(트럭 하역, 착용형 기기). [사실][^ref-1204] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

곽경민 외(2022)는 물류 특성에 맞는 기술과 운영 방식을 골라야 한다고 보았다. [사실][^ref-1204] 흐름 단계로 보면 트럭 하역은 입고, 분류·상차는 출하, 낱개 피킹은 피킹 단계에 해당하는 것으로 보인다. [추정][^ref-1204]

**현장 유형:** 실외

**사례:** 보도에서 실외이동로봇으로 배달·순찰(연계 대상)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 배달과 순찰. [사실][^ref-991] |
| 수행 자원 | [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)을 받은 실외이동로봇과 보도에서 로봇을 운영하려는 운영자. [사실][^ref-991] |
| 제약 | 2023-11-17 시행된 개정 지능형로봇법에 따라 인증 대상은 질량 500kg 이하·속도 15km/h 이하이고 운행구역 준수·횡단보도 통행 등 16개 시험항목을 거치며, 보도 운영자에게 보험 또는 공제 가입 의무가 있다. [사실][^ref-991] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

연계 대상: 실외 로봇의 인증과 보험은 분류 원문 19장의 업종별 조건(실외 차량 등)에 해당하는 외부 요구이며, ROP는 그 결과를 작업·경로·권한 제약으로 받아 반영하는 쪽인 것으로 보인다. [추정][^ref-991]

## 6. 대표 접근법과 기술

로봇에게 맡길 일과 요구를 정하는 방법으로는 현장 사용자와의 공동 설계, 업종별 표준공정 목록, 수요처가 주관하는 실증이 사례로 확인됐다. [사실][^ref-1195][^ref-1196][^ref-947] 사용 사례 템플릿 표준을 로봇에 적용한 사례는 찾지 못했다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area02-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사용 사례와 요구를 적는 표준, 역할과 범위를 나누는 로봇 규격, 국내 지원 틀이 이 영역과 이어진다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area02-s7.md)에 있다.

## 8. 대표 연구와 자료

사용자와 함께 일을 정한 병원 연구와 현장 유형별 적용 자료가 대표 자료다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 대표 연구와 자료](../../topics/2026/2026-09-30-area02-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 것은 사용 사례 목록과 요구 명세(행위자·시작 조건·완료 확인·수용 기준)의 틀, 제조사 플릿마다 플릿 제어 수준과 플랫폼이 맡는 조율 범위의 명시, 조달 조건으로서 상호운용 요구의 제시, 현장 사용자와 함께 정한 평가 기준의 관리로 보인다. [추정][^ref-1207][^ref-1206][^ref-1195][^ref-031][^ref-004][^ref-937]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 플릿마다 플릿 제어 수준과 플랫폼이 맡는 조율 범위를 명시한다. [추정][^ref-031][^ref-004] | 경로·동작 실행과 상태 보고는 이동로봇이 맡는다(VDA 5050 3.0.0 판 기준). [사실][^ref-031] |
| 시설·설비 제어 | 문·승강기 조건을 작업·경로 제약으로 받아 반영한다. [추정][^ref-1200][^ref-1201][^ref-948] | 전용 승강기·출입문 같은 건물 설비 개조는 ROP 밖의 주체가 맡는 것으로 보인다. [추정][^ref-1200][^ref-1201][^ref-948] |
| 업종별 조건 | 조달 조건이 될 상호운용 요구를 제시하고, 인증·보험 결과를 작업·경로·권한 제약으로 반영한다. [추정][^ref-937][^ref-991] | 연계 대상: 보도 운행 로봇의 운행안전인증과 운영자의 보험·공제 가입. [사실][^ref-991] |

이동로봇 적용의 위험성평가와 사용 정보 제공(통합자·제조사), 제조 공정 자체의 개선 컨설팅도 ROP 밖의 주체가 맡고, ROP는 그 결과를 작업·경로·권한 제약과 책임 분담표로 받아 반영하는 것으로 보인다. [추정][^ref-1084][^ref-1196] 안전 역할의 상세는 [48. 안전·위험 관리](../safety/safety-and-risk-management.md)와 [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)에서 다룬다. 범위 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시장·비용 판단, 제조사·설비 연동, 안전·법규·계약, 현장 유형별 적용 영역과 이어진다. 아래 연결은 이번 조사 근거를 영역별로 대응시킨 것이다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area02-s10.md)에 있다.

## 11. 열린 질문

이번 조사에서 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [2. 사용 사례·요구·책임 범위 — 열린 질문](../../topics/2026/2026-09-30-area02-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1195]: Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study, 2026-04-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/, 접근일 2026-09-30
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1197]: 로봇신문, “제조 로봇 표준공정 모델 적용 사업 국내를 넘어 ... (제목 일부만 확인), 2025-09-15, https://www.irobotnews.com/news/articleView.html?idxno=42376, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1200]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1201]: ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-1203]: 아시아경제, 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인), 2026-03-16, https://view.asiae.co.kr/article/2026031610244491183, 접근일 2026-09-30
[^ref-1204]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (로봇학회논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022-11, https://jkros.org/_PR/view/?aidx=34724&bidx=3204, 접근일 2026-09-30
[^ref-937]: Changi General Hospital, CHART, ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1206]: IEC SyC Smart Energy, IEC 62559 - use case methodology, 미확인, https://syc-se.iec.ch/deliveries/iec-62559-use-cases/, 접근일 2026-09-30
[^ref-1207]: ISO / IEC / IEEE, ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering, 2018, https://www.iso.org/standard/72089.html, 접근일 2026-09-30 (원문 미열람)
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-948]: 비즈한국, 병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인), 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-30
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

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s7.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-1196, ref-1084, ref-947, ref-937, ref-1206, ref-1207]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#7
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 관련 표준·프레임워크·오픈소스

# 2. 사용 사례·요구·책임 범위 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사용 사례와 요구를 적는 표준, 역할과 범위를 나누는 로봇 규격, 국내 지원 틀이 이 영역과 이어진다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사용 사례와 요구를 적는 표준, 역할과 범위를 나누는 로봇 규격, 국내 지원 틀이 이 영역과 이어진다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| IEC 62559 사용 사례 방법론 | 표준 | 에너지 시스템 요구 도출용 IntelliGrid 방법론에 기반한 IEC PAS 62559:2008에서 나왔다. 2부(2015)는 사용 사례·행위자 목록·요구사항 목록 템플릿을, 3부(2017)는 템플릿 내용을 다른 엔지니어링 시스템으로 옮기는 XML(Extensible Markup Language) 직렬화 형식을 정하고, 4부는 표준화와 기업 프로젝트용 모범 사례를 다룬다. [사실][^ref-1206] | [^ref-1206] |
| ISO/IEC/IEEE 29148:2018 | 표준 | 시스템·소프트웨어 수명주기 전체에 걸쳐 요구사항을 도출·분석·문서화·검증·관리하는 공정과 그 산출 정보 항목(이해관계자 요구사항 명세 등)의 내용과 형식을 규정한다(검색 결과 요약 기준, 원문 미열람). [사실][^ref-1207] | [^ref-1207] |
| ANSI/A3 R15.08-2(2023) | 표준 | 연계 대상. The Robot Report 기사(2023-10-26)에 따르면 산업용 이동로봇 시스템을 특정 적용에 맞게 바꾸고 특정 현장에 배치할 때의 안전 요구를 다루며, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다(표준 원문 미열람). [사실][^ref-1084] | [^ref-1084] |
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0 | 표준 | 3.0.0 판 기준으로 관제(fleet control)는 주문 배정·경로 계산·막힘 감지와 해소·교통 제어를, 이동로봇은 경로·동작 실행과 지속적인 상태 보고를 맡는다. [사실][^ref-031] 교통 조율 전략·알고리즘, 안전 요구, 보안 대책, 시운전 같은 프로젝트 수행 절차, 운영자·통합자·제조사 사이의 운영 책임 배분은 명세 범위 밖이다. [사실][^ref-031] | [^ref-031] |
| [Open-RMF](../../glossary/open-rmf.md) | 오픈소스 | Programming Multiple Robots with ROS 2의 RMF Core Overview 장은 제조사 플릿을 플릿 제어 수준에 따라 Full Control(경로를 RMF가 지정), Traffic Light(상태와 일시정지·재개만), Read Only(상태 보고만, 공유 공간당 최대 1개 플릿), No Interface(공유 공간·자원에서 교착 가능성)로 나누고, 플랫폼이 맡을 수 있는 조율 범위가 수준에 따라 달라진다고 설명한다. [사실][^ref-004] | [^ref-004] |
| RoMi-H | 오픈소스 | 창이종합병원 CHART가 개발한 의료 로봇 미들웨어로 기계·제어·중앙·통합 네 도메인으로 구성되며, 싱가포르는 공공 의료기관 로봇 시스템의 상호운용을 요구한다. [사실][^ref-937] | [^ref-937] |
| 로봇활용 표준공정모델 | 프레임워크 | 업종별 제조 공정에 로봇을 적용하는 국내 참조 모델로, 2020년 뿌리·섬유·식음료·자동차 업종 14종이 개발되었다. [사실][^ref-1196] | [^ref-1196] |
| 서비스로봇 실증사업 | 평가 프로그램 | 수요처가 주관기관이 되는 로봇 활용 실증 사업이다(6절). [사실][^ref-947] | [^ref-947] |

표준 목록 전체는 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-937]: Changi General Hospital, CHART, ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1206]: IEC SyC Smart Energy, IEC 62559 - use case methodology, 미확인, https://syc-se.iec.ch/deliveries/iec-62559-use-cases/, 접근일 2026-09-30
[^ref-1207]: ISO / IEC / IEEE, ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering, 2018, https://www.iso.org/standard/72089.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s10.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 다른 연구영역과의 연결"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-1195, ref-1196, ref-1197, ref-1198, ref-1084, ref-1200, ref-1201, ref-947, ref-1203, ref-1204, ref-937, ref-991, ref-948]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#10
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 다른 연구영역과의 연결

# 2. 사용 사례·요구·책임 범위 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 시장·비용 판단, 제조사·설비 연동, 안전·법규·계약, 현장 유형별 적용 영역과 이어진다. 아래 연결은 이번 조사 근거를 영역별로 대응시킨 것이다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 시장·비용 판단, 제조사·설비 연동, 안전·법규·계약, 현장 유형별 적용 영역과 이어진다. 아래 연결은 이번 조사 근거를 영역별로 대응시킨 것이다.

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 적용 분류별 서비스 로봇 판매 규모는 어떤 일이 로봇에게 맡겨지는지 보는 시장 근거가 될 것으로 보인다. [추정][^ref-1198]
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 실증사업의 국비·민간 부담 구조, RaaS 성장, 호텔 사례의 성과 주장은 도입 비용 분담과 과금 판단으로 이어질 것으로 보인다. [추정][^ref-947][^ref-1198][^ref-1203]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플랫폼이 맡을 조율 범위는 관제 규격의 기능 구분과 제조사 플릿의 플릿 제어 수준에 따라 정해지는 것으로 보인다. [추정][^ref-031][^ref-004]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 싱가포르 공공 의료기관처럼 상호운용 플랫폼 연동이 조달 요구가 될 수 있다. [추정][^ref-937]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 병원 사례의 반자동문·수동문·승강기가 사용 사례의 제약이 된다. [추정][^ref-1200][^ref-1201][^ref-948]
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — 수령자의 터치스크린 확인 같은 완료·인계 조건을 작업 모델로 표현해야 할 것으로 보인다. [추정][^ref-1200]
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md)·[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 통합자의 위험성평가와 제조사·통합자의 사용 정보 제공이 책임 범위를 나누는 근거가 된다. [추정][^ref-1084]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 현장 시험에서 드러난 문·복도·인파 제약은 현장 조사에서 확인할 항목이 될 것으로 보인다. [추정][^ref-1200]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 관제 규격이 범위 밖에 둔 운영 책임 배분과 호텔 사례의 3자 역할 분담은 계약으로 정할 몫으로 보인다. [추정][^ref-031][^ref-1203]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 실외이동로봇 운영자의 보험·공제 가입 의무와 운행안전인증이 사용 사례의 법적 조건이 된다. [추정][^ref-991]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 간호사 수용성 평가와 의료진의 회의적 의견은 맡길 일을 정할 때의 수용성 근거가 된다. [추정][^ref-1195][^ref-948]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 물류 서비스 유형별 로봇 분류가 이어진다. [추정][^ref-1204]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 로봇활용 표준공정모델이 이어진다. [추정][^ref-1196][^ref-1197]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 세 사례와 싱가포르 조달 요구가 이어진다. [추정][^ref-1195][^ref-1200][^ref-1201][^ref-948][^ref-937]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 호텔 룸서비스 배송 사례가 이어진다. [추정][^ref-1203]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 보도 배달·순찰 로봇의 인증·보험 조건이 이어진다. [추정][^ref-991]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1195]: Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study, 2026-04-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/, 접근일 2026-09-30
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1197]: 로봇신문, “제조 로봇 표준공정 모델 적용 사업 국내를 넘어 ... (제목 일부만 확인), 2025-09-15, https://www.irobotnews.com/news/articleView.html?idxno=42376, 접근일 2026-09-30
[^ref-1198]: International Federation of Robotics (IFR), Service Robots See Global Growth Boom, 2025-10, https://ifr.org/news/service-robots-see-global-growth-boom/, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1200]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1201]: ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-1203]: 아시아경제, 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인), 2026-03-16, https://view.asiae.co.kr/article/2026031610244491183, 접근일 2026-09-30
[^ref-1204]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (로봇학회논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022-11, https://jkros.org/_PR/view/?aidx=34724&bidx=3204, 접근일 2026-09-30
[^ref-937]: Changi General Hospital, CHART, ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-948]: 비즈한국, 병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인), 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s8.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 대표 연구와 자료"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1195, ref-1196, ref-1198, ref-1200, ref-1204, ref-937]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#8
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 대표 연구와 자료

# 2. 사용 사례·요구·책임 범위 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사용자와 함께 일을 정한 병원 연구와 현장 유형별 적용 자료가 대표 자료다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사용자와 함께 일을 정한 병원 연구와 현장 유형별 적용 자료가 대표 자료다.

- Friese, C. 외, Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study(JMIR Nursing, 2026) — 샤리테 베를린 RoMi 프로젝트에서 간호 인력과 적용 시나리오·능력 요구·평가 기준을 공동 개발하고, 비임상 업무를 맡은 서비스 로봇에 대한 간호사 30명의 수용성을 평가했다. [사실][^ref-1195]
- Valner, R. 외, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022) — 병원 직원과 함께 검체 운반을 자동화 대상으로 정하고 중환자실에서 검사실로 혈액 검체를 운반했다. 병원 현장에는 TIAGo를 투입했고, RMF로 TIAGo·Jackal 이기종 로봇을 관리하는 것은 시험 환경에서 확인했다. [사실][^ref-1200]
- 곽경민 외, 급속 확산되는 물류현장의 로봇적용 사례(로봇학회논문지 17(4), 2022) — 물류 서비스를 계약물류·택배·풀필먼트로 나누고 로봇 적용을 이송·핸들링·지원으로 분류했다. [사실][^ref-1204]
- IFR, Service Robots See Global Growth Boom(2025) — 2024년 전문 서비스 로봇의 적용 분류별 판매량과 인력 부족이라는 도입 동기를 발표했다. [사실][^ref-1198]
- 산업통상자원부, 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수(2020) — 표준공정모델 14종 개발과 60개 기업 대상 패키지 지원을 알렸다. [사실][^ref-1196]
- Changi General Hospital CHART, ROMI-H — 싱가포르 공공 의료기관 로봇의 상호운용 요구와 RoMi-H의 네 도메인 구조를 설명한다. [사실][^ref-937]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1195]: Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study, 2026-04-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/, 접근일 2026-09-30
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1198]: International Federation of Robotics (IFR), Service Robots See Global Growth Boom, 2025-10, https://ifr.org/news/service-robots-see-global-growth-boom/, 접근일 2026-09-30
[^ref-1200]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1204]: 곽경민, 박범, 고은지, 윤철주, 김경훈 (로봇학회논문지 17(4)), 급속 확산되는 물류현장의 로봇적용 사례, 2022-11, https://jkros.org/_PR/view/?aidx=34724&bidx=3204, 접근일 2026-09-30
[^ref-937]: Changi General Hospital, CHART, ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s6.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 대표 접근법과 기술"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1195, ref-1196, ref-1200, ref-947, ref-1206]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#6
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 대표 접근법과 기술

# 2. 사용 사례·요구·책임 범위 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇에게 맡길 일과 요구를 정하는 방법으로는 현장 사용자와의 공동 설계, 업종별 표준공정 목록, 수요처가 주관하는 실증이 사례로 확인됐다. [사실][^ref-1195][^ref-1196][^ref-947] 사용 사례 템플릿 표준을 로봇에 적용한 사례는 찾지 못했다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇에게 맡길 일과 요구를 정하는 방법으로는 현장 사용자와의 공동 설계, 업종별 표준공정 목록, 수요처가 주관하는 실증이 사례로 확인됐다. [사실][^ref-1195][^ref-1196][^ref-947] 사용 사례 템플릿 표준을 로봇에 적용한 사례는 찾지 못했다.

### 현장 사용자와 함께 정하기

샤리테 베를린 의대병원 RoMi 연구는 간호 인력과 함께 적용 시나리오·능력 요구·평가 기준을 정했고, 간호사 30명의 수용성을 평가했다. [사실][^ref-1195] 타르투 대학병원 현장 시험도 병원 직원과 협업해 검체·장비 운반을 자동화 대상으로 정했다. [사실][^ref-1200] 사용 의도는 지각된 유용성과 가장 강한 양의 상관을 보였으며, 연구진은 능력과 한계의 투명한 전달과 직접 체험 기회를 권했다. [사실][^ref-1195]

### 업종별 표준공정 목록

산업통상자원부는 2020년 뿌리·섬유·식음료·자동차 업종의 로봇활용 표준공정모델 14종을 개발하고 컨설팅·실증 보급·교육·협동로봇 안전인증과 묶어 지원한다고 발표했다. [사실][^ref-1196] 공정 개선 컨설팅 자체는 ROP 범위 밖이다(9절).

### 수요처 주관 실증

한국로봇산업진흥원 서비스로봇 실증사업은 로봇 도입이 필요한 수요처(민간·공공)가 주관기관, 로봇기업이 참여기관이 되는 컨소시엄으로 운영되며, 공모 뒤 서류·발표·현장평가를 거쳐 선정·협약한다. [사실][^ref-947] 국비는 로봇 도입 비용의 50% 이내이고, 민간 부담은 총사업비 대비 50% 이상, 그중 수요기관 부담은 총사업비 대비 25% 이상이다(2026-09-30 확인 기준). [사실][^ref-947] 지원 분야는 물류(제조공장·유통물류·음식점·실외배송)·웨어러블·의료(수술·재활)·협동로봇·언택트 서비스다. [사실][^ref-947]

### 사용 사례 템플릿과 요구 명세 표준

IEC 62559-2의 사용 사례·행위자 목록·요구사항 목록 템플릿 구조는 분류 원문 21장의 여섯 항목으로 ROP 사용 사례를 적을 때 행위자(로봇·사람·설비)와 요구 목록을 나눠 관리하는 틀로 쓸 수 있을 것으로 보이나, 로봇 오케스트레이션에 적용한 사례는 확인하지 못했다. [추정][^ref-1206] IEC 페이지가 드는 적용 분야는 스마트그리드·스마트시티·스마트홈/빌딩·능동형 생활 보조(Active Assisted Living, AAL)이며 로봇 적용 언급은 없다. [사실][^ref-1206]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1195]: Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study, 2026-04-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/, 접근일 2026-09-30
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1200]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-1206]: IEC SyC Smart Energy, IEC 62559 - use case methodology, 미확인, https://syc-se.iec.ch/deliveries/iec-62559-use-cases/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s3.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 왜 중요한가"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-1195, ref-1198, ref-1084, ref-1200, ref-1201, ref-991, ref-948]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#3
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 왜 중요한가

# 2. 사용 사례·요구·책임 범위 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료를 종합하면, 실제로 로봇에게 맡겨지는 일은 반복적인 비임상 운반과 정보 전달이 중심이다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료를 종합하면, 실제로 로봇에게 맡겨지는 일은 반복적인 비임상 운반과 정보 전달이 중심이다. 검체 이송은 기존 수단이 낫다는 상급종합병원의 한 교수 의견도 있어 일을 고를 때는 현장 사용자와 함께 기준을 정하는 방식이 쓰이고, 플랫폼의 책임 범위는 규격이 정해 주지 않아 플릿 제어 수준·안전 역할·법적 운영자 의무와 함께 도입 단계에서 정해지는 것으로 보인다. [추정][^ref-1198][^ref-1195][^ref-1200][^ref-1201][^ref-948][^ref-031][^ref-004][^ref-1084][^ref-991]

국제로봇연맹(International Federation of Robotics, IFR)의 World Robotics 2025 서비스 로봇 편 발표(2025-10)에 따르면 2024년 전문 서비스 로봇 판매는 약 20만 대로 전년보다 9% 늘었다. [사실][^ref-1198] 적용 분류별로는 운송·물류가 102,900대(+14%)로 가장 많았고, 접객 4만2천여 대(-11%), 전문 청소 2만5천여 대(+34%), 농업 약 19,500대(-6%)가 뒤를 이었다. [사실][^ref-1198] 같은 발표는 인력 부족을 기업이 전문 서비스 로봇을 쓰는 주요 동기로 들었고, 운송·물류 분류에서 [서비스형 로봇](../../glossary/robot-as-a-service.md)(Robot-as-a-Service, RaaS) 방식이 2024년 42% 늘었다고 밝혔다. [사실][^ref-1198]

반대 의견도 있다. 국내 기사에 인용된 상급종합병원의 한 교수(기사에 익명 표기)는 검체 이송은 컨베이어·인력 운송이 더 빠르고 안전하며 병원 물류가 복잡해 로봇이 맡기 어렵다고 보았다. [의견][^ref-948]

책임 범위 쪽을 보면, VDA 5050 3.0.0 판은 운영자·통합자·제조사 사이의 운영 책임 배분을 명세 범위 밖에 둔다. [사실][^ref-031] Open-RMF에서 플랫폼이 맡을 수 있는 조율 범위는 제조사 플릿의 [플릿 제어 수준](../../glossary/fleet-control-level.md)(Fleet Control Level)에 따라 달라진다. [사실][^ref-004] 따라서 플랫폼이 직접 책임질 범위는 사용 사례·현장·플릿 제어 수준마다 도입 단계에서 정해야 하는 것으로 보인다. [추정][^ref-031][^ref-004]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1195]: Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study, 2026-04-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC13078706/, 접근일 2026-09-30
[^ref-1198]: International Federation of Robotics (IFR), Service Robots See Global Growth Boom, 2025-10, https://ifr.org/news/service-robots-see-global-growth-boom/, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1200]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://pmc.ncbi.nlm.nih.gov/articles/PMC9445435/, 접근일 2026-09-30
[^ref-1201]: ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-948]: 비즈한국, 병원에 늘어나는 ‘로봇’, 의사·간호사도 ... (제목 일부만 확인), 2025-04-10, https://bizhankook.com/articles/29394.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s4.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 핵심 개념과 용어"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-1196, ref-1084, ref-947, ref-1206, ref-1207]
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#4
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 핵심 개념과 용어

# 2. 사용 사례·요구·책임 범위 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇에게 맡길 일과 책임을 적는 데 쓰이는 용어는 요구공학 표준, 안전 표준의 역할 구분, 플랫폼 연동 구분, 국내 지원 사업에서 나온다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇에게 맡길 일과 책임을 적는 데 쓰이는 용어는 요구공학 표준, 안전 표준의 역할 구분, 플랫폼 연동 구분, 국내 지원 사업에서 나온다.

- **사용 사례 템플릿(Use Case Template)** — IEC 62559-2가 정한 양식으로, 사용 사례·행위자 목록·요구사항 목록을 구조화해 기록하게 한다. [사실][^ref-1206] 템플릿의 세부 필드는 이번 조사에서 확인하지 못했다.
- **이해관계자 요구사항 명세(Stakeholder Requirements Specification, StRS)** — ISO/IEC/IEEE 29148이 정한 요구공학 산출물의 하나로, 사용자와 이해관계자가 시스템에 기대하는 것을 구현 방법 없이 수용 기준과 함께 적는다(검색 결과 요약 기준). [사실][^ref-1207]
- **제조사·통합자·사용자 역할** — The Robot Report 기사(2023-10-26)에 따르면 ANSI/A3 R15.08-2는 산업용 이동로봇(Industrial Mobile Robot, IMR) 시스템의 [위험성평가](../../glossary/risk-assessment.md)는 통합자가, [사용 정보](../../glossary/information-for-use.md) 제공은 제조사와 통합자가, 교육과 안전 작업 절차는 사용자가 맡게 한다(표준 원문 미열람). [사실][^ref-1084]
- **[플릿 제어 수준](../../glossary/fleet-control-level.md)(Fleet Control Level)** — Open-RMF가 제조사 플릿을 연동 정도에 따라 Full Control·Traffic Light·Read Only·No Interface로 나눈 구분이다. [사실][^ref-004]
- **로봇활용 표준공정모델** — 업종별 제조 공정에 로봇을 적용하는 방법을 정리한 국내 참조 모델로, 산업통상자원부가 2020년 14종 개발과 패키지 지원을 발표했다. [사실][^ref-1196]
- **수요처 주관 실증** — 로봇을 도입할 수요처가 주관기관, 로봇기업이 참여기관이 되는 한국로봇산업진흥원 서비스로봇 실증사업의 운영 방식이다. [사실][^ref-947]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-1196]: 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수, 2020-06-25, https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=202113&pg=&pp=20&recommend=&topic=C, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-947]: 한국로봇산업진흥원, 서비스로봇 실증사업, 미확인, https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do, 접근일 2026-09-30
[^ref-1206]: IEC SyC Smart Energy, IEC 62559 - use case methodology, 미확인, https://syc-se.iec.ch/deliveries/iec-62559-use-cases/, 접근일 2026-09-30
[^ref-1207]: ISO / IEC / IEEE, ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering, 2018, https://www.iso.org/standard/72089.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-14/pages/topics/2026/2026-09-30-area02-s11.md

```markdown
---
title: "2. 사용 사례·요구·책임 범위 — 열린 질문"
type: topic
category: "A. 기획·사업"
primary_area_no: 2
related_areas: [1, 3, 20, 21, 22, 24, 48, 50, 55, 58, 59, 60, 61, 62, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/planning-and-business/use-cases-requirements-and-scope.md#11
---

[홈](../../index.md) › [주제](../index.md) › 2. 사용 사례·요구·책임 범위 — 열린 질문

# 2. 사용 사례·요구·책임 범위 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 답하지 못한 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-14) 로봇 오케스트레이션 도입 계약에서 운영자·통합자·로봇 제조사·플랫폼 사업자 사이의 운영 책임을 나누는 책임 분담표나 표준 계약 조항을 공개한 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-14) 병원 검체 이송 같은 업무에서 로봇·컨베이어·사람 운반을 같은 조건으로 비교해 로봇에게 맡길 업무를 정한 정량 연구가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-14) IEC 62559 사용 사례 템플릿이나 ISO/IEC/IEEE 29148 요구 명세 형식을 다중 로봇·로봇 오케스트레이션 사용 사례 정의에 적용한 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-14) 싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-14) 가정·공동주택과 기타 현장(공공시설·연구실 등)에서 여러 로봇에게 맡길 일과 요구를 사용자와 함께 도출한 연구나 실증 사례가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/planning-and-business/use-cases-requirements-and-scope.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-14 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-14 | 2. 사용 사례·요구·책임 범위 의 "열린 질문" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1085건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 298개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
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
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
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

### docs/open-questions.md (요약: 대상 영역 [2] 에 걸린 0건 / 전체 232건)

```markdown
없음
```
