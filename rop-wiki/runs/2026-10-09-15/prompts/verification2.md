(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-15
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 37. 관제 화면·실행 기록 (J. 현장 운영·관제)
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

### runs/2026-10-09-15/target.json

```json
{
  "run_id": "2026-10-09-15",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 148,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 37,
    "area_name": "37. 관제 화면·실행 기록",
    "category": "J. 현장 운영·관제",
    "category_letter": "J"
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
  "selection_rationale": "CLI 지정 run_type=update, area=37"
}
```

### runs/2026-10-09-15/research.json

```json
{
  "run_id": "2026-10-09-15",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 37,
    "area_name": "37. 관제 화면·실행 기록",
    "category": "J. 현장 운영·관제"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 병원 협약 단계 보도 1건뿐이고 물류창고·제조 공장·상업 시설·가정·실외·기타 사례가 '찾지 못했다'로 남아 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — 공통 상태 값 표준이 Open-RMF 작업 상태 스키마뿐이고(oq-237) MassRobotics·VDA 5050 의 상태·오류 수준 정의, 관제실 설계 표준(ISO 11064), 투명성 표준(IEEE 7001)이 없음. rmf-web 저장 설정(바뀐 출처) 확인 필요",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 실행 기록 보관 주체·기간 근거(oq-316, oq-239)와 사고 조사용 최소 기록 항목(oq-252) 없음",
    "섹션 11. 열린 질문 — oq-131·oq-237·oq-238·oq-239·oq-240·oq-252·oq-316 해결 근거 미조사",
    "정정 요청 없음, 발행 2년이 지난 표준 수치 재확인 대상은 ISA-101 계열(본문 유료, 이번에 재열람하지 않음)"
  ],
  "research_questions": [
    "운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]",
    "oq-237 여러 제조사 로봇의 작업 상태·실행 로그를 한 화면·한 기록으로 모을 때 Open-RMF 작업 상태 스키마 말고 공통 상태 값과 로그·오류 수준을 정한 공개 규약이 있는가? (섹션 7·9 겨냥)",
    "oq-238·oq-240 설명 가능한 표시를 실제 플릿 관제 화면에서 측정한 연구가 있는가, 다중 로봇 관제 화면에 쓸 수 있는 화면·관제실 설계 표준이나 투명성 표준은 무엇인가? (섹션 7·11 겨냥)",
    "oq-252·oq-316·oq-239 사고 조사용 최소 기록 항목, 고위험 AI 자동 사건 기록의 보관 기간·주체, 병원 특수 물품 배송 기록의 국내 보관 요건은 무엇인가? (섹션 9·11 겨냥)",
    "물류창고·실외·가정·기타 현장과 국내 병원에서 여러 로봇을 하나의 관제 화면으로 운영한 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)",
    "바뀐 출처와 oq-131: Open-RMF rmf-web 의 실행 기록 저장 설정은 바뀌었는가, 로봇 물류 실행 기록을 객체 중심 이벤트 로그로 만든 공개 사례가 있는가? (섹션 7·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 은 로봇이 보고하는 동작 상태 값을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 로, 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고, 오류마다 사람이 읽는 설명(errorDescription)·조치 힌트(errorHint)와 ISO 639-1 언어 코드별 번역을 담을 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.6.5.1 오류 수준 4단계(WARNING 은 즉시 조치 불필요, FATAL 은 사용자 개입 필요), 표 5 동작 상태 열, 6.6.5.3 errorDescriptionTranslations·errorHintTranslations (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 로봇이 state 메시지의 information 배열로 보내는 부가 정보를 플릿 관제가 로직에 쓰지 말고 시각화·디버깅에만 쓰게 하며, logReport 즉시 동작으로 로봇에 로그 보고서 생성·저장을 요청하고 저장된 로그 이름을 동작 상태로 보고받게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.6.4: fleet control shall not use the information for logic; only for visualization and debugging. 표 4·5 logReport(reason) — 보고서 저장 시 FINISHED, 로그 이름을 동작 상태에 포함 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "MassRobotics AMR 상호운용 표준의 statusReport 는 uuid·timestamp·operationalState·location 을 필수로 하고, operationalState 를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 정하며, 오류 코드 배열, 약 10초의 단기 경로(예측 위치 최대 10개), 목적지, 배터리 잔량을 선택 항목으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-253"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AMR_Interop_Standard.json statusReport: required uuid, timestamp, operationalState, location; errorCodes 는 정상 운행 중 생략; path 는 short-term path of about 10 seconds (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "Open-RMF 작업 상태 스키마는 작업 상태 값 12개와 별도로 배차 상태를 queued·selected·dispatched·failed_to_assign·canceled_in_flight 로 기록하고, 요청자(requester)·예약 라벨과 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다 요청 시각과 라벨(예: dashboard)을 남기게 해, 누가 어떤 창구로 작업에 개입했는지를 실행 기록에 담을 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_state.json $defs.dispatch.status enum, booking.requester, interruptions·cancellation·killed·skip_requests 의 unix_millis_request_time 과 labels(`dashboard` 또는 `app=dashboard`) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f5",
      "claim": "Open-RMF 작업 상태 스키마 말고도 VDA 5050(동작 상태·오류 수준)과 MassRobotics 상호운용 표준(운용 상태)이 공개된 상태 값 집합을 정하지만 세 규약의 값 집합과 단위(작업·동작·로봇)가 서로 달라, 37. 관제 화면·실행 기록에서 여러 제조사 상태를 한 기록으로 모으려면 ROP 가 대응표를 만들어 정규화해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-253",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 은 동작 단위 상태와 오류 수준, MassRobotics 는 로봇 단위 운용 상태, Open-RMF 는 작업·단계·사건 단위 상태를 정한다. 세 규약 사이의 공식 대응표는 이번 조사에서 확인하지 못했다",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Open-RMF rmf-web 의 API 서버는 기본으로 메모리 안의 SQLite 를 써서 실행 기록이 남지 않지만, 설정의 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 지정해 영속 저장할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-762",
        "ref-302"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "api-server README: \"by default it uses a in-memory sqlite instance\"; db_url 형식 DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME, PostgreSQL 은 rmf-server[postgres] 설치. 상위 README 도 기본은 internal non-persistent database (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Open-RMF 로그 항목(log_entry) 스키마는 오늘 기준으로도 순번(seq)·수준(tier)·밀리초 유닉스 시각·본문을 필수로 하고 수준 값을 uninitialized·info·warning·error 로 두어, 페이지 7절의 로그 수준 서술이 그대로 유효하다.",
      "tag": "사실",
      "source_ids": [
        "ref-1095"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "log_entry.json required: seq, tier, unix_millis_time, text; tier enum uninitialized, info, warning, error (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "IEEE 7001-2021(자율 시스템 투명성 표준)은 사용자, 검증·인증 담당자, 고장·사고 조사자, 소송·행정 절차의 전문 자문가, 일반 대중의 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 객관적으로 평가할 수 있는 다섯 단계의 투명성 수준을 정하며, IEEE 로봇·자동화 학회가 공동 후원했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1338"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEEE SA 기사(2022-05-11): \"specific, measurable levels of transparency that can be assessed objectively\". 표준 본문은 열지 않았고 기사 기준",
      "as_of": "2022-05-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "IEEE 7001-2021 이 운영자(사용자)와 사고 조사자를 별도 이해관계자로 두므로, 37. 관제 화면·실행 기록의 설명 가능한 표시는 운영자용 투명성으로, 실행 기록은 조사자용 투명성으로 나눠 평가하는 근거가 될 수 있을 것으로 보이나, 표준이 화면 설계나 기록 항목을 정하는지는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1338"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사는 사용자에게 시스템이 무엇을 왜 하는지 이해할 간단한 방법이 필요하다고 쓰지만 이벤트 기록 장치나 화면 요건을 표준이 정한다고는 쓰지 않는다",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "ISO 11064(관제 센터 인간공학 설계) 계열은 설계 원칙, 관제 공간 배치, 관제실 배치, 작업대 배치·치수, 표시 장치와 조작기, 환경 요건, 관제 센터 평가 원칙, 특정 적용의 인간공학 요건의 여러 부로 나뉜다.",
      "tag": "사실",
      "source_ids": [
        "ref-1349"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 11064-1:2000 미리보기의 머리말: Part 5 \"Displays and controls\", Part 7 \"Principles for the evaluation of control centres\" 등 8개 부. 적용 범위 절은 미리보기에 없어 확인하지 못함",
      "as_of": "2000",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Winfield 외(2022-05, ICRES 2022 제출)는 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 같은 운용 데이터를 안전하게 기록하는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스의 공개 표준 초안을 첫 초안으로 내놓았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1120"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: securely recording operational data (sensor, actuator and control decisions) for a social robot, 사고 조사를 위한 비행 기록 장치에 상응. 부록의 기록 항목·보관 기간은 PDF 를 읽지 못해 미확인",
      "as_of": "2022-05-13",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "윤리적 블랙박스 초안은 로봇 한 대의 내부 기록을 대상으로 하므로, 여러 제조사 로봇을 지휘하는 플랫폼 수준의 명령·정지·재가동 기록 항목을 정한 공개 규약은 이번 조사에서도 확인하지 못해 oq-252 는 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1120",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "초안은 단일 소셜 로봇 기준. VDA 5050 의 logReport 는 로봇 쪽 로그 생성을 요청할 뿐 기록 항목을 정하지 않는다",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "EU AI Act 제12조는 고위험 AI 시스템이 수명 동안 사건을 자동 기록(로그)할 수 있게 기술적으로 갖추고, 그 기록이 위험 상황·실질적 변경의 식별, 출시 후 모니터링, 배포자의 운용 모니터링(제26조 제5항)을 뒷받침하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-863"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Article 12(1): \"automatic recording of events (logs) over the lifetime of the system\"; 12(2) 세 목적(제79조 제1항 위험·실질적 변경, 제72조 출시 후 모니터링, 제26조 제5항 운용 모니터링)",
      "as_of": "2024-07-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "EU AI Act 는 고위험 AI 의 자동 생성 로그를 공급자(제19조 제1항)와 배포자(제26조 제6항)가 각자 통제하는 범위에서 목적에 맞는 기간, 최소 6개월 보관하게 하고, 다른 EU·회원국 법(특히 개인정보 보호법)이 다르게 정하면 그에 따르게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1341",
        "ref-1342"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Art.19(1) logs kept for a period appropriate to the intended purpose, of at least six months, 공급자가 계약·법에 따라 통제하는 범위. Art.26(6) 배포자도 to the extent such logs are under their control",
      "as_of": "2024-07-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "연계 대상: 로봇 플랫폼의 AI 구성요소가 고위험 AI 인지의 판단은 법무·규제 영역이며, 해당한다면 플랫폼 실행 기록의 보관 의무는 그 로그를 공급자와 배포자 중 누가 통제하는지에 따라 나뉘므로 ROP 는 보관 기간 설정과 통제 주체 표시를 기록 기능으로 갖추는 쪽을 맡을 것으로 보인다(oq-316 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-863",
        "ref-1341",
        "ref-1342"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "제19조·제26조가 모두 '통제하는 범위에서' 보관하게 하므로 계약상 통제 주체가 보관 주체를 가른다. 로봇 플랫폼에 대한 적용 해석 자료는 찾지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "한림대학교성심병원은 2024-04 기준 안내·배송·방역 로봇 등 7종 73대의 서비스 로봇을 커맨드센터의 통합관제시스템으로 운영하며, 커맨드센터 담당자는 서로 다른 제조사 로봇을 하나의 관제시스템으로 연결하는 일이 중요하다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1344",
        "ref-944"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "코메디닷컴(2024-04-20): \"각기 다른 제조사의 로봇들을 하나의 관제시스템으로 연결하는 일이 중요하다\", 7종 73대. 로봇신문(2024-04-15)도 7종 73대·통합관제 보도(재인용: 2026-10-09-14)",
      "as_of": "2024-04-20",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": false
    },
    {
      "id": "f17",
      "claim": "같은 보도에 따르면 한림대학교성심병원의 로봇 서비스는 2022-08 부터 2024-03 까지 3만 1607건 시행되었으나, 관제 화면 항목이나 배송 이력 조회 방식은 공개되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1344"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2022년 8월~2024년 3월 3만 1607건 서비스 시행. 실시간 모니터링·문제 대응 업무 서술이나 화면 구성은 기사에 없음",
      "as_of": "2024-04-20",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f18",
      "claim": "LG CNS 는 Open-RMF 를 바탕으로 한 로봇 통합운영 플랫폼에서 고객이 로봇의 이동 동선과 작업 처리 결과를 실시간으로 한눈에 확인할 수 있고 AGV·AMR·오토스토어·소팅로봇이 연계되어 있으며, G마켓 동탄 물류센터에서 기술검증에 착수했다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1343"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 2023-07-06 보도자료. 로봇 이동 동선·작업 처리 결과 실시간 확인, G마켓과 동탄 물류센터 PoC 착수, 로보셔틀·소형 피킹로봇 연동 검증 예정. 운영 결과는 미공개",
      "as_of": "2023-07-06",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "국내 실외이동로봇 운행안전인증은 속도 제어·비상정지·장애물 감지·횡단보도 통행·운행구역 준수·관제 장치 등 16개 항목을 평가하고 로봇과 관제장치의 조합에 인증을 주므로, 실외 현장에서는 관제 장치가 운행 제약의 하나가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1345",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "바이라인네트워크(2024-01-31): 16개 항목 평가, 모든 기준을 만족해야 인증. 로봇·관제장치 조합 인증은 한국로봇산업진흥원 안내(재인용: 2026-10-09-14). 관제 장치 항목의 세부 요건은 미확인",
      "as_of": "2024-01-31",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f20",
      "claim": "농촌진흥청의 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1007"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "뉴스토마토(2025-04-23) 보도 기준 (재인용: 2026-10-09-14)",
      "as_of": "2025-04-23",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "LH토지주택연구원 자료를 인용한 보도는 공동주택 단지 로봇 택배에서 택배 차량이 단지 집하처에 송장번호를 인식시키면 물품 정보가 관제실로 전달된다고 전한다.",
      "tag": "사실",
      "source_ids": [
        "ref-976"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "정보통신신문(2024-07-18) 보도 기준, 시나리오 단계 서술 (재인용: 2026-10-09-14)",
      "as_of": "2024-07-18",
      "site_type": "가정",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "Patel 외(2021)는 여러 운영자가 다중 로봇을 함께 감독할 때의 투명성을 다루며, 자기 작업 정보만 보이는 방식·다른 운영자 작업 정보를 공유하는 방식·둘을 섞은 방식·없음의 네 모드를 참가자 18명의 사용자 연구로 비교해 인식·신뢰·작업 부하를 쟀다.",
      "tag": "사실",
      "source_ids": [
        "ref-1347"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2101.10495 초록: transparency modes none, central, peripheral, mixed; user study with 18 participants on a complex multi-robot task. 현장 평가는 없음",
      "as_of": "2021-05-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "이번에 확인한 설명 가능한 표시·투명성 연구도 실험실 사용자 연구 수준이어서, 실제 운영 중인 로봇 플릿 관제 화면에서 운영자의 상황 인식과 대응 시간을 측정한 공개 연구는 여전히 확인하지 못해 oq-238 은 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1347",
        "ref-1099"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Patel 외 18명 사용자 연구, Roldán 외 24명 실험실 비교(재인용: 2026-09-30-13). 현장 측정 자료는 검색 2회(영어)로 찾지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Rohrer 외(2022)는 공장 물류를 모사한 RoboCup Logistics League 시뮬레이션의 사건을 데이터베이스에서 꺼내 로봇·주문·부품 객체와 11개 활동을 담은 객체 중심 이벤트 로그(OCEL JSON)로 만들고, 다음 사건과 그 시각을 예측하는 데 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1348"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: RCLL 은 \"a simulation of factory logistics\", 활동 예 deliver·mount-first-ring·fill-cap, 이벤트 id·활동·시각·객체 유형을 OCEL JSON 으로 저장. 로그 규모는 표가 깨져 미확인",
      "as_of": "2022-07-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "로봇 물류 실행 기록을 로봇·주문·부품 객체 중심 이벤트 로그로 만든 공개 사례는 있으나 그 로그를 시뮬레이션 시나리오 사양으로 되돌리는 변환 규칙은 이번에도 확인하지 못해, oq-131 에는 기록 쪽 형식만 부분 근거가 된 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1348"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Rohrer 외는 예측 모니터링 목적이며 시나리오 생성은 다루지 않음",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문(입력의 원문 텍스트). 동작 상태 값, 오류 수준 4단계와 번역, information 배열의 시각화·디버깅 전용 규칙, logReport 즉시 동작을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 작업 상태 JSON 스키마(입력의 원문 텍스트). 배차 상태 값, 요청자·라벨, 일시정지·취소·강제 종료·건너뛰기 요청 기록 구조를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-web 저장소 README. API 서버·API 클라이언트·대시보드 프레임워크 구성과 기본 비영속 내부 데이터베이스 사용을 다시 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1095",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — log_entry.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 로그 항목 스키마. 필수 필드 seq·tier·unix_millis_time·text 와 수준 값 네 개를 다시 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/log_entry.json",
      "source_unopened": false
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 한림대성심병원의 7종 73대 서비스 로봇 통합관제 운영 보도(이전 실행 2026-10-09-14 확인 내용 재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1007",
      "org": "뉴스토마토 (이규하)",
      "title": "방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동",
      "published": "2025-04-23",
      "url": "https://www.newstomato.com/ReadNews.aspx?no=1259970",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 농촌진흥청이 자체 개발 농업 로봇 3종을 하나의 화면으로 관리하는 통합 관리 프로그램 보도(재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-976",
      "org": "정보통신신문 (김연균)",
      "title": "로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’",
      "published": "2024-07-18",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=123976",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LH토지주택연구원 자료를 인용한 공동주택 로봇 택배 관제실 연동 시나리오 보도(재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 안내. 인증이 로봇과 관제장치의 조합에 주어진다(재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1099",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 운영자 24명이 다중 로봇 임무를 감독한 실험실 인터페이스 비교 연구(이전 실행 2026-09-30-13 확인 내용 재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-253",
      "org": "MassRobotics (MassRobotics-AMR/AMR_Interop_Standard)",
      "title": "AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "MassRobotics 공식 저장소의 상호운용 표준 JSON 스키마. identityReport·statusReport 필드와 operationalState 아홉 값을 정한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": true
    },
    {
      "id": "ref-1338",
      "org": "IEEE Standards Association",
      "title": "How To Make Autonomous Systems More Transparent and Trustworthy",
      "published": "2022-05-11",
      "url": "https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "IEEE 7001-2021(자율 시스템 투명성 표준)을 소개하는 IEEE SA 공식 글. 이해관계자 범주 다섯과 범주별 다섯 단계 투명성 수준을 설명한다. 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록해 사고·아차 사고 조사를 돕는 윤리적 블랙박스의 공개 표준 초안. 초록만 확인했고 부록(표준 본문)은 PDF 추출 실패로 읽지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-863",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 12: Record-keeping",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제12조. 고위험 AI 의 수명 동안 자동 사건 기록 기능과 기록이 뒷받침해야 할 세 목적을 정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1341",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 19: Automatically generated logs",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제19조. 공급자가 통제하는 자동 생성 로그를 목적에 맞는 기간, 최소 6개월 보관하게 한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1342",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 26: Obligations of deployers of high-risk AI systems",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제26조. 제6항이 배포자가 통제하는 자동 생성 로그를 최소 6개월 보관하게 한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1343",
      "org": "LG CNS (LG 미디어 보도자료)",
      "title": "‘로봇 통합운영 플랫폼’ 개발",
      "published": "2023-07-06",
      "url": "https://lg.co.kr/media/release/26480",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "LG CNS 의 Open-RMF 기반 로봇 통합운영 플랫폼 발표와 G마켓 동탄 물류센터 기술검증 착수 보도자료. 기능 서술은 벤더 주장이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1344",
      "org": "코메디닷컴",
      "title": "[메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠",
      "published": "2024-04-20",
      "url": "https://kormedi.com/1682189/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대의료원 커맨드센터 파트장 인터뷰. 7종 73대 서비스 로봇, 통합관제시스템, 2022-08~2024-03 누적 3만 1607건 서비스.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1345",
      "org": "바이라인네트워크 (이진호)",
      "title": "뉴빌리티, 실외이동 로봇 운행안전 인증 획득",
      "published": "2024-01-31",
      "url": "https://byline.network/2024/01/240131_00004/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "실외이동로봇 운행안전인증이 관제 장치를 포함한 16개 항목을 평가한다는 보도. 관제 장치 항목의 세부는 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf/rmf-web)",
      "title": "rmf-web packages/api-server — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-web API 서버 README. 기본은 메모리 내 SQLite 이고 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 설정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/packages/api-server/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1347",
      "org": "Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv)",
      "title": "Transparency in Multi-Human Multi-Robot Interaction",
      "published": "2021-05-14",
      "url": "https://arxiv.org/abs/2101.10495",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "여러 운영자–다중 로봇 상호작용에서 네 가지 투명성 모드를 참가자 18명 사용자 연구로 비교한 프리프린트(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1348",
      "org": "Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv)",
      "title": "Predictive Object-Centric Process Monitoring",
      "published": "2022-07-20",
      "url": "https://arxiv.org/abs/2207.10017",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RoboCup Logistics League 시뮬레이션 사건을 객체 중심 이벤트 로그(OCEL)로 만들어 다음 사건·시각을 예측한 프리프린트. 본문은 ar5iv 로 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://ar5iv.labs.arxiv.org/html/2207.10017",
      "source_unopened": false
    },
    {
      "id": "ref-1349",
      "org": "ISO (ANSI Webstore 미리보기)",
      "title": "ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview)",
      "published": "2000",
      "url": "https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 11064-1:2000 미리보기(표지·목차·머리말·서론). 계열의 8개 부 제목을 확인했고 적용 범위 절과 본문은 미리보기에 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "sections": [
        "5",
        "7",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 병원 사례에 f16(7종 73대 통합관제, 교차 확인)·f17(누적 3만 1607건) 추가, 물류창고 f18('벤더 주장' 병기, 흐름 단계는 서술하지 않음), 실외 f19(관제 장치가 인증 항목·제약), 기타 f20, 가정 f21 을 현장 유형마다 나눠 '찾지 못했다' 문장 교체. 제조 공장·상업 시설은 이번에도 찾지 못함 / 섹션 7 — 표에 MassRobotics statusReport(f3), VDA 5050 동작 상태·오류 수준·information·logReport(f1·f2), Open-RMF 배차 상태·개입 기록(f4), IEEE 7001-2021(f8), ISO 11064(f10), 윤리적 블랙박스 초안(f11) 행 추가, rmf-web 행을 '기본은 메모리 내 SQLite, db_url 로 영속 DB 설정'으로 갱신(f6, 바뀐 출처), 로그 수준 재확인(f7) / 섹션 9 — 상태 값 정규화를 직접 범위에(f5), EU AI Act 로그 보관 기간·주체를 연계 대상으로(f13·f14·f15) / 섹션 11 — oq-237 해결 제안(f1·f3·f4·f5), oq-238 미해결(f22·f23), oq-240 부분 근거(f8·f9·f10), oq-252 부분 근거(f11·f12), oq-316 부분 근거(f13·f14·f15), oq-131 부분 근거(f24·f25), oq-239 미해결, 새 질문 2건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석(f1 오류 수준·f10 ISO 11064), 59. 법·규제·보험·라이선스(f13·f14), 50. 안전 표준·인증·사고 조사(f11), 66. 실외(f19) 페이지 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "운용 상태",
      "term_en": "Operational State (MassRobotics statusReport operationalState)",
      "definition": "MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다."
    },
    {
      "term_ko": "동작 상태",
      "term_en": "Action Status (VDA 5050 actionStatus)",
      "definition": "VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다."
    },
    {
      "term_ko": "자율 시스템 투명성 수준",
      "term_en": "Transparency Level (IEEE 7001-2021)",
      "definition": "IEEE 7001-2021 이 사용자·인증 담당자·사고 조사자 등 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 다섯 단계로 정한, 객관적으로 평가할 수 있는 투명성 등급이다."
    }
  ],
  "open_questions_new": [
    "VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? | 관련 영역: 37. 관제 화면·실행 기록, 21. 상호운용 표준·적합성 | 근거: f5 | 종류: 일반",
    "국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? | 관련 영역: 37. 관제 화면·실행 기록, 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [
    "oq-237"
  ],
  "self_check": {
    "source_count": 22,
    "cross_checked_count": 1,
    "unverified": [
      "oq-239 미해결: 마약류 관리에 관한 법률 시행규칙의 장부·기록 2년 보존 조문을 국가법령정보센터에서 열지 못했고(본문 미표시) 검색 결과는 기사·비공식 법령 사이트뿐이라 근거로 쓰지 않음. 로봇 배송 이력 자체의 보관 요건은 확인하지 못함",
      "f11 윤리적 블랙박스 초안 부록(기록 항목·보관 시간 창·보안 요건): PDF 텍스트 추출 실패로 미확인",
      "f8 IEEE 7001-2021 본문 미열람(IEEE SA 소개 글 기준), 화면·기록 요건 포함 여부 미확인",
      "f10 ISO 11064-1 적용 범위 절 미확인(미리보기에 없음). 검색 요약에 나온 '교통·물류 관제 시스템 포함' 범위 문구는 원문으로 확인하지 못해 넣지 않음",
      "f19 운행안전인증 16개 항목 중 관제 장치 항목의 세부 요건 미확인, ref-980 이번 실행에서 다시 열지 않음",
      "f16 의 ref-944 와 f20·f21 출처는 이전 실행 확인 내용 재인용이며 이번에 다시 열지 않음",
      "f18 LG CNS 플랫폼 기능과 G마켓 동탄 기술검증 결과는 벤더 보도자료뿐이며 독립 확인하지 못함",
      "제조 공장·상업 시설의 관제 화면·실행 기록 사례는 이번에도 찾지 못함",
      "f24 RCLL 로그 규모는 표가 깨져 미확인"
    ],
    "scope_violations": [
      "f15: 고위험 AI 해당 여부와 로그 보관 의무 해석은 법무·규제 쪽 연계 대상이라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 보관 기간 설정·통제 주체 표시로 한정",
      "f19: 운행안전인증 판단은 인증 기관·운영자 쪽이며 ROP 에는 실외 현장 제약으로만 반영 제안",
      "f11·f12: 윤리적 블랙박스의 센서·구동기 기록은 로봇 자체 지능·제어 쪽 기록이므로 ROP 직접 범위가 아니라 플랫폼 수준 기록 항목의 비교 대상으로만 씀",
      "f2: VDA 5050 logReport 로 만드는 로그는 로봇 쪽 기록(연계 대상)이며 ROP 는 요청과 결과 이름 수신만 맡는다고 서술해야 함"
    ],
    "budget_used": {
      "queries": 14,
      "sources": 13
    },
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청이 없어 빈·약한 절(5절 현장 사례, 7절 표준, 9절 기록 보관 경계, 11절 열린 질문)과 바뀐 출처(rmf-web 저장 설정)만 조사했다. 검색 14회/30, 신규 출처 13건/15(ref-253~ref-1349, 예약 구간 안), 재사용 9건. 신규 출처는 모두 원문 또는 공식 페이지를 열었다(webfetch 10, github_raw 2, 미리보기 1). 재사용 가운데 ref-031·ref-111 은 입력의 원문 텍스트(inbox), ref-302·ref-1095 는 github_raw 로 다시 열었고, ref-944·ref-1007·ref-976·ref-980·ref-1099 는 다시 열지 않아 source_unopened 로 표시했다. 교차 확인 1건(f16, 7종 73대 통합관제: 코메디닷컴·로봇신문). oq-237 해결 근거: f1·f3·f4·f5(Open-RMF 외에 VDA 5050 과 MassRobotics 가 공개 상태 값을 정함, 대응표는 없음 — 새 질문으로 올림). oq-238·oq-239 는 미해결, oq-131·oq-240·oq-252·oq-316 은 부분 근거만. 현장 유형: 병원(f16·f17), 물류창고(f18, 벤더 주장), 실외(f19), 기타(f20), 가정(f21). 제조 공장·상업 시설 사례는 검색 1회로 찾지 못했다. 벤더 주장 1건(f18). 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 섞지 않았고 f24·f25 는 기록 형식으로만 다뤘다. 핵심 질문에 대한 새 결론은 없으며 '무엇'의 표시 근거(상태 값 규약)만 보강되었다. 용어집에 이미 있는 윤리적 블랙박스·자동 사건 기록·HMI 철학·객체 중심 이벤트 로그는 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-15/verification.json

```json
{
  "run_id": "2026-10-09-15",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력의 VDA 5050 3.0.0 원문 텍스트(data/source_texts/ref-031.txt)의 표 5 동작 상태 열(INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE), 6.6.5.1 오류 수준 4단계, errorDescription·errorHint, 6.6.5.3 ISO 639-1 번역과 일치. 단일 출처(표준 원문). 발행일 미확인이므로 판(3.0.0, main)과 확인일 2026-10-09 를 기준일로 둔다. 브리프는 fetched_via github_raw·fetch_url null 로 적었으나 실제 근거는 입력 원문 텍스트(inbox)다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.6.4 'shall not use the information for logic; ... only be used for visualization and debugging', 표 4 logReport(reason), 표 5 'The report has been stored. The name of the log is reported as part of the action state.' 와 일치. 로봇 쪽 로그 자체는 연계 대상이고 ROP 는 요청과 로그 이름 수신만 맡는다고 서술해야 한다(브리프 scope_violations 와 같음)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw.githubusercontent.com 의 AMR_Interop_Standard.json 을 열어 statusReport 필수 uuid·timestamp·operationalState·location, operationalState 9개 값, errorCodes('should be omitted for normal operation'), path(최대 10개, 'Short term path of AGV ~10 sec'), destinations, batteryPercentage 를 확인했다. 공식 저장소의 JSON 스키마(공식 산출물)이며 표준 본문 PDF 는 아님. 브리프는 원문 미열람(source_unopened: true)으로 표시했다. 발행일 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 텍스트의 task_state.json — status enum 12개, $defs.dispatch.status enum 5개, booking.requester·labels, interruptions(resumed_by 포함)·cancellation·killed·skip_requests 의 unix_millis_request_time·labels 와 일치. 다만 개입 요청(일시정지·취소 등)에는 요청자 필드가 없고 라벨만 있으므로 '누가 ... 개입했는지'는 과장이다 — 수정 지시 참조."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 세 출처가 각각 동작 단위(VDA 5050)·로봇 단위(MassRobotics)·작업·단계·사건 단위(Open-RMF) 상태 값을 정한다는 점은 f1·f3·f4 검증으로 확인. '대응표가 필요할 것'은 추론이므로 [추정] 유지."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: api-server README 'by default it uses a in-memory sqlite instance', db_url 형식, 지원 DB PostgreSQL·SQLite·MySQL·MariaDB(postgres·mysql·maria 추가 설치), 상위 README 'In the default scenario, the API server will use an internal non-persistent database.' 두 출처는 같은 저장소라 독립 교차 확인이 아니다. '실행 기록이 남지 않지만'은 원문에 없는 표현이므로 '기본은 비영속 저장'으로 고친다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: log_entry.json 필수 seq·tier·unix_millis_time·text, tier enum uninitialized·info·warning·error 를 검증자가 열어 재확인. 2026-09-30 서술과 같아 기존 각주 ref-1095 재사용."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IEEE SA 글(2022-05-11) — 이해관계자 다섯 범주, 범주별 다섯 단계(minimally acceptable ~ stringent), 'specific, measurable levels of transparency that can be assessed objectively'. 공동 후원은 IEEE Vehicular Technology Society·Intelligent Transportation Systems Society·Robotics and Automation Society 셋이므로 로봇·자동화 학회는 '공동 후원 학회 가운데 하나'로 써야 한다. 표준 본문 미열람(발행 기관 소개 자료 기준)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이해관계자 범주에 사용자와 조사자가 따로 있음은 IEEE SA 글로 확인. 화면·기록 요건 포함 여부 미확인이라는 단서가 있어 [추정] 유지."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ISO 11064-1:2000 미리보기 머리말의 8개 부(Part 1~8) 제목과 일치. 발행 2000년(2년 경과) 자료이며 각 부의 이후 개정 여부는 확인하지 않았으므로 'ISO 11064-1:2000 머리말 기준'을 기준일로 밝힌다. 적용 범위 절 미확인."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2205.06564 v1 2022-05-13, ICRES 2022 제출, 초록의 소셜 로봇 센서·구동기·제어 결정 안전 기록, 사고·아차 사고 조사, 첫 초안(draft for discussion) 과 일치. 부록(기록 항목·보관 기간) 미확인."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초안이 단일 소셜 로봇 대상(f11), VDA 5050 logReport 는 생성·저장 요청과 로그 이름 보고만 정함(f2). '확인하지 못했다'는 조사 범위 진술이므로 [추정] 유지, oq-252 는 열림 유지."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AI Act Service Desk 제12조 제1항 'automatic recording of events (logs) over the lifetime of the system', 제2항 (a) 제79조 제1항 위험·실질적 변경, (b) 제72조 출시 후 모니터링, (c) 제26조 제5항 운용 모니터링과 일치. 규정 2024/1689 발행 2024-07-12. 법 해석은 연계 대상."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제19조 제1항(공급자, 'to the extent such logs are under their control', 'at least six months', 개인정보 보호법 등 다른 법 우선)과 제26조 제6항(배포자, 같은 기간 규정) 일치. 두 조문은 같은 규정이라 독립 교차 확인이 아니다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '통제하는 범위에서' 문구는 제19조·제26조로 확인. 로봇 플랫폼 적용 해석은 자료 없음 — '연계 대상: ' 표시와 [추정] 유지. oq-316 은 부분 근거일 뿐 해결 아님."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인·교차 확인: 코메디닷컴(2024-04-20) 7종 73대, 통합관제시스템, '각기 다른 제조사의 로봇들을 하나의 관제시스템으로 연결하는 일이 중요하다'(커맨드센터 파트장). 검증자가 로봇신문(ref-944, 2024-04-15)을 열어 '7종 73대', '제조사마다 상이한 다종 다수의 로봇 관제를 통합관제 시스템을 이용해 중앙에서' 관리한다는 서술을 확인했다. 브리프는 ref-944 를 원문 미열람으로 표시했다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 코메디닷컴에 2022-08~2024-03 3만 1607건, 관제 화면 항목·배송 이력 미공개. 단일 기사 수치이므로 '보도 기준'을 밝힌다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LG 보도자료(2023-07-06) — Open-RMF 기반, '로봇들의 동선과 작업 처리결과 등도 실시간으로 한눈에 모니터링', AGV·오토스토어·소팅로봇 연계(AMR 지원 서술), G마켓 동탄 물류센터 PoC 착수. 벤더 주장 표시(vendor_claim·첫머리 '벤더 주장: ')와 [추정] 적정. 운영 결과 미공개."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: 바이라인네트워크(2024-01-31) '총 16개 항목 ... 모든 기준을 만족', 평가 대상에 '관제 장치' 포함. 검증자가 한국로봇산업진흥원 안내(ref-980)를 열어 인증 대상이 '실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체'이고 관제장치가 심사 항목임을 확인 — 관제장치 평가·조합 인증은 독립 2출처 교차 확인. 다만 진흥원 페이지는 심사 항목을 8개(규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치)로 나열해 기사 '16개 항목'과 표현이 다르다 — 둘 다 제시 지시. 관제 장치 세부 요건(화면·기록)은 두 출처 모두 없음."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 뉴스토마토(2025-04-23)를 열어 방제(2022)·운반(2023)·모니터링(2024) 로봇 3종, 농촌진흥청 자체 개발, 개인용 컴퓨터·휴대전화 하나로 관리, 다른 제조사 언급 없음을 확인. 2026-10-09-14 브리프 f45 와 같은 주장이므로 기존 각주 ref-1007 재사용. 브리프는 원문 미열람으로 표시."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 정보통신신문(2024-07-18)을 열어 '택배차량이 물류집합처에 도착해 송장번호를 인식시켜 관제실로 물품정보를 전송' 서술(LH토지주택연구원 인용)을 확인. 시나리오 단계 서술임을 밝힌다. 2026-10-09-14 f34 와 같은 출처 재사용."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2101.10495 v2(2021-05-14, v1 2021-01-26) 초록 — none·central·peripheral·mixed 네 모드, 18명 사용자 연구, awareness·trust·workload 측정. 프리프린트."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Patel 외 18명(f22), Roldán 외 24명 실험실 비교(ref-1099, 2026-09-30-13 검증분 재사용, 이번에 다시 열지 않음). 현장 측정 자료 미발견은 조사 범위 진술이므로 [추정] 유지, oq-238 열림 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ar5iv 본문 'The RoboCup Logisitcs League (RCLL) is a simulation of factory logistics', 활동 11개(clear-mps ~ produce-cx), OCEL JSON 저장, 활동·시각 예측. 세 번째 객체 유형을 본문이 'components'와 'products'로 섞어 쓰므로 '부품(제품)'으로 적는다. 예측 대상은 다음 사건뿐 아니라 남은 사건 순서(접미 예측)까지다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Rohrer 외는 예측 모니터링 목적이며 시나리오 생성을 다루지 않음. oq-131 은 부분 근거일 뿐 해결 아님 — [추정] 유지."
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
      "f16·f20·f21 은 2026-10-09-14 브리프(f19·f45·f34)와 같은 주장·출처(ref-944·ref-1007·ref-976)다 — 새 각주를 만들지 않고 기존 id 를 재사용한다(브리프가 이미 재사용).",
      "f6 은 현재 페이지 7절 표의 rmf-web 행('기본은 비영속 저장', ref-302)을 갱신하는 내용이며 모순이 아니다.",
      "f7 은 현재 페이지 7절의 log_entry 서술(ref-1095)을 재확인한 것으로 새 사실이 아니다.",
      "현재 페이지 5절 '관제 화면·실행 기록의 현장 근거를 찾은 것은 병원 한 건' 문장과 마지막 '찾지 못했다' 문장은 이번 사례(f16~f21)로 바뀌어야 하며 모순이 남지 않게 해야 한다."
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
    "f4: '누가 어떤 창구로 작업에 개입했는지'를 '작업 요청자(booking.requester)와, 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다의 요청 시각·라벨(예: dashboard)로 어떤 창구에서 개입했는지'로 고친다 — 원문 task_state.json 에서 개입 요청에는 요청자 필드가 없고 라벨만 있다.",
    "f6: '실행 기록이 남지 않지만'을 '기본 설정은 메모리 안의 SQLite(비영속 내부 데이터베이스)를 쓰며'로 고친다 — 두 README 는 비영속이라고만 쓰고 실행 기록 소실을 직접 말하지 않는다. 7절 rmf-web 행 갱신에 ref-762 각주를 더한다.",
    "f19: '16개 항목'은 바이라인네트워크 기사(ref-1345) 기준임을 밝히고, 한국로봇산업진흥원 안내(ref-980)는 심사 항목을 8개(관제장치 포함)로 나열한다는 점을 함께 적어 어느 한쪽을 고르지 않는다 — 두 출처의 항목 수 표현이 다르다. 이 차이를 open_questions_new 둘째 질문(운행안전인증 관제 장치 항목)에 덧붙여 열린 질문으로 남긴다. 로봇·관제장치 조합 인증과 관제장치 평가는 두 출처로 확인됐으므로 [사실] 유지.",
    "f19: 5절 실외 사례에서 인증 판단은 인증 기관·운영자 쪽 연계 대상이고 ROP 에는 실외 현장의 제약으로만 반영된다고 쓴다(분류 원문 19장 업종별 조건).",
    "f10: 7절 ISO 11064 행에 'ISO 11064-1:2000 미리보기 머리말 기준(확인일 2026-10-09), 각 부의 이후 개정 여부·적용 범위는 미확인'을 적는다 — 발행 2000년 자료다.",
    "f8: 'IEEE 로봇·자동화 학회가 공동 후원했다'를 'IEEE 로봇·자동화 학회가 공동 후원 학회 가운데 하나다'로 고친다 — IEEE SA 글은 차량기술학회·지능형교통시스템학회와 함께 셋을 공동 후원으로 든다. 표준 본문이 아니라 IEEE SA 소개 글 기준임을 밝힌다.",
    "f2: 7·9절에서 VDA 5050 logReport 로 생성되는 로그 자체는 로봇 쪽 기록(연계 대상)이고 ROP 는 생성 요청과 로그 이름(동작 상태) 수신만 맡는다고 쓴다.",
    "f13·f14·f15: 9절에서 EU AI Act 로그 보관 의무의 해당 여부·해석은 연계 대상(59. 법·규제·보험·라이선스)으로 짧게 다루고, ROP 몫은 보관 기간 설정과 로그 통제 주체 표시 기능으로 한정해 [추정]으로 쓴다. f14 의 두 조문은 같은 규정이므로 교차 확인으로 표시하지 않는다.",
    "f17: '3만 1607건'은 코메디닷컴 단일 보도 기준(2024-04-20)임을 밝힌다.",
    "f18: 5절 물류창고 사례는 [추정] 뒤에 '벤더 주장'을 병기하고, PoC 착수 발표뿐이며 운영 결과는 확인되지 않았다고 쓴다. 흐름 단계는 서술하지 않는다(근거 없음).",
    "f24: 객체 유형을 '로봇·주문·부품(제품)'으로 적고 예측 대상을 '이후 사건과 그 시각(남은 사건 순서 포함)'으로 쓴다 — 본문이 세 번째 객체 유형을 components 와 products 로 섞어 쓴다.",
    "f1·f2: 7절 VDA 5050 행의 기준을 '3.0.0(main), 발행일 미확인, 확인일 2026-10-09'로 적고 기존 각주 ref-031 을 재사용한다.",
    "각주·참고문헌: 브리프가 원문 미열람(source_unopened: true)으로 표시한 ref-944·ref-1007·ref-976·ref-980·ref-1099·ref-253 의 각주 정의에는 접근일 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다.",
    "11절: oq-237 은 해결로 바꾼다(근거 f1·f3·f4, 남은 대응표 문제는 새 질문으로 잇는다). oq-238·oq-239 는 열림 유지, oq-131·oq-240·oq-252·oq-316 은 해결로 바꾸지 않고 부분 근거(각 finding id)만 덧붙인다. 기존 11절의 '(새 질문, 상태: 열림)' 네 줄은 실제 id(oq-237·oq-238·oq-239·oq-240)로 표기한다.",
    "용어집: '운용 상태'(MassRobotics operationalState) 정의에 기존 용어 '운용 모드 (Operating Mode (VDA 5050 operatingMode))'와 다른 개념임을 한 문장으로 밝힌다 — 이름이 비슷해 혼동될 수 있다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 25건, 미확인 0건, 교차 확인 2건(f16 한림대학교성심병원 7종 73대 통합관제: 코메디닷컴·로봇신문 / f19 실외이동로봇 운행안전인증의 로봇·관제장치 조합 인증: 바이라인네트워크·한국로봇산업진흥원). 강등: 없음. 원문 미열람 출처(브리프 표시): ref-944, ref-1007, ref-976, ref-980, ref-1099, ref-253 — 이 가운데 ref-944·ref-1007·ref-976·ref-980·ref-253 은 검증자가 이번 검증에서 열어 주장과 일치함을 확인했고 ref-1099 는 2026-09-30-13 검증분 재사용이다. oq-237 해결 인정(f1·f3·f4: VDA 5050 동작 상태·오류 수준과 MassRobotics 운용 상태가 Open-RMF 밖의 공개 상태 값 규약이며, 세 규약 사이 대응표는 새 질문으로 남김). oq-238·oq-239 열림 유지, oq-131·oq-240·oq-252·oq-316 은 부분 근거만. 정정 요청 없음. 주의: 새 사실은 대부분 단일 출처(표준 원문·공식 스키마·조문)이고 9절의 책임 경계와 현장 적용 해석은 [추정]이다. 실외 운행안전인증의 평가 항목 수는 기사(16개)와 진흥원 안내(8개 심사 항목)의 표현이 달라 둘 다 제시한다. ISO 11064 는 2000년판 머리말 기준이며 IEEE 7001-2021 은 표준 본문이 아니라 IEEE SA 소개 글 기준이다. 물류창고 사례(LG CNS)는 벤더 주장이고 제조 공장·상업 시설 사례는 이번에도 찾지 못했다. 브리프는 ref-031·ref-111 을 fetched_via github_raw(fetch_url 없음)로 적었으나 실제 근거는 입력 원문 텍스트다(판정에는 영향 없음). 검증 검색 0회, 열람 19회.",
  "retry_reason": null
}
```

### runs/2026-10-09-15/pages.json

```json
{
  "run_id": "2026-10-09-15",
  "outline": [
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "관제 화면·실행 기록의 현장 근거는 병원·물류창고·실외·가정·기타에서 찾았지만 대부분 보도·발표 단계이며, 화면 항목과 기록 형식을 공개한 사례는 확인하지 못했다. [추정][^ref-1344][^ref-1343]",
      "planned_findings": [
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2200,
      "summary": "Open-RMF 작업 상태 스키마 외에 VDA 5050 3.0.0 동작 상태·오류 수준과 MassRobotics 운용 상태가 공개 상태 값 규약이며, 관제실 설계(ISO 11064)·투명성(IEEE 7001-2021)·윤리적 블랙박스 초안을 더했다. [사실][^ref-031][^ref-253]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f6",
        "f7",
        "f8",
        "f10",
        "f11"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1700,
      "summary": "ROP는 여러 규약의 상태 값을 대응표로 정규화하고 logReport 요청·로그 이름 수신을 맡으며, 로봇 쪽 로그·인증 판단·로그 보관 의무 해석은 연계 대상이다. [추정][^ref-031][^ref-1341]",
      "planned_findings": [
        "f2",
        "f5",
        "f13",
        "f14",
        "f15",
        "f19"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "11. 열린 질문",
      "budget_chars": 1800,
      "summary": "oq-237 은 해결, oq-131·oq-240·oq-252·oq-316 은 부분 근거만 더했고 oq-238·oq-239 는 열림이며 새 질문 2건을 올린다. [추정][^ref-031][^ref-253]",
      "planned_findings": [
        "f5",
        "f9",
        "f12",
        "f15",
        "f22",
        "f23",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "13. 참고 자료 (각주)",
      "budget_chars": 0,
      "summary": "각주 정의 37건(신규 13건, 재사용 출처의 접근일·원문 미열람 표시 갱신)."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5절 현장 사례를 6건(병원 2·물류창고·실외·가정·기타)으로 늘리고 '찾지 못했다' 문장 교체, 7절에 VDA 5050 동작 상태·오류 수준·logReport, MassRobotics 운용 상태, Open-RMF 배차·개입 기록, ISO 11064, IEEE 7001-2021, 윤리적 블랙박스 초안 행 추가와 rmf-web 행 갱신, 9절에 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계 추가, 11절 oq-237 해결·부분 근거·새 질문 2건, 13절 각주 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md 의 해당 절을 본다)",
          "frontmatter": {
            "sources": [
              "ref-1093",
              "ref-302",
              "ref-111",
              "ref-1094",
              "ref-1095",
              "ref-031",
              "ref-1096",
              "ref-1097",
              "ref-1098",
              "ref-477",
              "ref-1099",
              "ref-1100",
              "ref-1101",
              "ref-1102",
              "ref-1103",
              "ref-253",
              "ref-1338",
              "ref-1120",
              "ref-863",
              "ref-1341",
              "ref-1342",
              "ref-1343",
              "ref-1344",
              "ref-944",
              "ref-1345",
              "ref-980",
              "ref-1007",
              "ref-976",
              "ref-762",
              "ref-1347",
              "ref-1348",
              "ref-1349"
            ],
            "confidence": "low",
            "last_run": "2026-10-09"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area37-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,936자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area37-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"11. 열린 질문\" 절(2,787자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area37-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"3. 왜 중요한가\" 절(485자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 37. 관제 화면·실행 기록 | 갱신: 5절 현장 사례 6건(병원 2·물류창고·실외·가정·기타), 7절 VDA 5050·MassRobotics 상태 값 규약·ISO 11064·IEEE 7001-2021·윤리적 블랙박스 초안 추가와 rmf-web 저장 설정 갱신, 9절 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계, 11절 oq-237 해결·새 질문 2건 | run 2026-10-09-15",
  "index_updates": {
    "home_recent": "2026-10-09 — 37. 관제 화면·실행 기록: 공개 상태 값 규약(VDA 5050 동작 상태·오류 수준, MassRobotics 운용 상태)과 현장 사례 6건을 더하고 oq-237 을 해결로 정리",
    "category_recent": "2026-10-09 — 37. 관제 화면·실행 기록: 5·7·9·11절 갱신(병원·물류창고·실외·가정·기타 사례, 상태 값 규약·관제실·투명성 표준, EU AI Act 로그 보관 연계 경계, oq-237 해결)",
    "area_recent": "2026-10-09 — 37. 관제 화면·실행 기록: 갱신(차등) 5절 사례 6건, 7절 표준 행 7개 추가·rmf-web 행 갱신, 9절 경계 2행·로그 보관 단락, 11절 oq-237 해결·부분 근거·새 질문 2건, 13절 각주 32건(1차 조건부 승인 수정 15건 반영)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "operational-state",
      "term_ko": "운용 상태",
      "term_en": "Operational State (MassRobotics statusReport operationalState)",
      "definition": "MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다.",
      "description": "값은 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 이며 statusReport 의 필수 항목이다. 이름이 비슷한 기존 용어 '운용 모드'(Operating Mode, VDA 5050 operatingMode)와는 다른 개념으로, 운용 상태는 MassRobotics 상태 보고가 로봇 단위로 알리는 상태 값이다.",
      "related_areas": [
        37,
        20,
        21
      ],
      "sources": [
        "ref-253"
      ]
    },
    {
      "action": "new",
      "slug": "action-status",
      "term_ko": "동작 상태",
      "term_en": "Action Status (VDA 5050 actionStatus)",
      "definition": "VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다.",
      "description": "VDA 5050 3.0.0 기준이다. logReport 즉시 동작에서는 보고서가 저장되면 FINISHED 와 함께 저장된 로그 이름을 동작 상태로 보고한다.",
      "related_areas": [
        37,
        20,
        29
      ],
      "sources": [
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "transparency-level-ieee-7001",
      "term_ko": "자율 시스템 투명성 수준",
      "term_en": "Transparency Level (IEEE 7001-2021)",
      "definition": "IEEE 7001-2021 이 사용자·인증 담당자·사고 조사자 등 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 다섯 단계로 정한, 객관적으로 평가할 수 있는 투명성 등급이다.",
      "description": "이해관계자 범주는 사용자, 검증·인증 담당자, 고장·사고 조사자, 소송·행정 절차의 전문 자문가, 일반 대중이다. 표준 본문이 아니라 IEEE SA 소개 글(2022-05-11) 기준이다.",
      "related_areas": [
        37,
        31,
        50
      ],
      "sources": [
        "ref-1338"
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 동작 상태 값, 오류 수준 4단계와 번역, information 배열의 시각화·디버깅 전용 규칙, logReport 즉시 동작을 확인했다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 작업 상태 JSON 스키마. 배차 상태 값, 요청자·라벨, 일시정지·취소·강제 종료·건너뛰기 요청 기록 구조를 확인했다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-web 저장소 README. API 서버·API 클라이언트·대시보드 프레임워크 구성과 기본 비영속 내부 데이터베이스 사용을 다시 확인했다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1095",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — log_entry.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 로그 항목 스키마. 필수 필드 seq·tier·unix_millis_time·text 와 수준 값 네 개를 다시 확인했다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 한림대성심병원의 7종 73대 서비스 로봇 통합관제 운영 보도(이전 실행 2026-10-09-14 확인 내용 재인용).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1007",
      "org": "뉴스토마토 (이규하)",
      "title": "방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동",
      "published": "2025-04-23",
      "url": "https://www.newstomato.com/ReadNews.aspx?no=1259970",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 농촌진흥청이 자체 개발 농업 로봇 3종을 하나의 화면으로 관리하는 통합 관리 프로그램 보도(재인용).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-976",
      "org": "정보통신신문 (김연균)",
      "title": "로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’",
      "published": "2024-07-18",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=123976",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LH토지주택연구원 자료를 인용한 공동주택 로봇 택배 관제실 연동 시나리오 보도(재인용).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 안내. 인증이 로봇과 관제장치의 조합에 주어진다(재인용).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1099",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 운영자 24명이 다중 로봇 임무를 감독한 실험실 인터페이스 비교 연구(이전 실행 2026-09-30-13 확인 내용 재인용).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-253",
      "org": "MassRobotics (MassRobotics-AMR/AMR_Interop_Standard)",
      "title": "AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. MassRobotics 공식 저장소의 상호운용 표준 JSON 스키마. identityReport·statusReport 필드와 operationalState 아홉 값을 정한다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1338",
      "org": "IEEE Standards Association",
      "title": "How To Make Autonomous Systems More Transparent and Trustworthy",
      "published": "2022-05-11",
      "url": "https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "IEEE 7001-2021(자율 시스템 투명성 표준)을 소개하는 IEEE SA 공식 글. 이해관계자 범주 다섯과 범주별 다섯 단계 투명성 수준을 설명한다. 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록해 사고·아차 사고 조사를 돕는 윤리적 블랙박스의 공개 표준 초안. 초록만 확인했고 부록(표준 본문)은 읽지 못했다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-863",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 12: Record-keeping",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제12조. 고위험 AI 의 수명 동안 자동 사건 기록 기능과 기록이 뒷받침해야 할 세 목적을 정한다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1341",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 19: Automatically generated logs",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제19조. 공급자가 통제하는 자동 생성 로그를 목적에 맞는 기간, 최소 6개월 보관하게 한다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1342",
      "org": "European Commission, AI Act Service Desk (Regulation (EU) 2024/1689)",
      "title": "Article 26: Obligations of deployers of high-risk AI systems",
      "published": "2024-07-12",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제26조. 제6항이 배포자가 통제하는 자동 생성 로그를 최소 6개월 보관하게 한다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1343",
      "org": "LG CNS (LG 미디어 보도자료)",
      "title": "‘로봇 통합운영 플랫폼’ 개발",
      "published": "2023-07-06",
      "url": "https://lg.co.kr/media/release/26480",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "LG CNS 의 Open-RMF 기반 로봇 통합운영 플랫폼 발표와 G마켓 동탄 물류센터 기술검증 착수 보도자료. 기능 서술은 벤더 주장이다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1344",
      "org": "코메디닷컴",
      "title": "[메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠",
      "published": "2024-04-20",
      "url": "https://kormedi.com/1682189/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대의료원 커맨드센터 파트장 인터뷰. 7종 73대 서비스 로봇, 통합관제시스템, 2022-08~2024-03 누적 3만 1607건 서비스.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1345",
      "org": "바이라인네트워크 (이진호)",
      "title": "뉴빌리티, 실외이동 로봇 운행안전 인증 획득",
      "published": "2024-01-31",
      "url": "https://byline.network/2024/01/240131_00004/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "실외이동로봇 운행안전인증이 관제 장치를 포함한 16개 항목을 평가한다는 보도. 관제 장치 항목의 세부는 없다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf/rmf-web)",
      "title": "rmf-web packages/api-server — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-web API 서버 README. 기본은 메모리 내 SQLite 이고 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 설정한다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1347",
      "org": "Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv)",
      "title": "Transparency in Multi-Human Multi-Robot Interaction",
      "published": "2021-05-14",
      "url": "https://arxiv.org/abs/2101.10495",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "여러 운영자–다중 로봇 상호작용에서 네 가지 투명성 모드를 참가자 18명 사용자 연구로 비교한 프리프린트(초록 확인).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1348",
      "org": "Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv)",
      "title": "Predictive Object-Centric Process Monitoring",
      "published": "2022-07-20",
      "url": "https://arxiv.org/abs/2207.10017",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RoboCup Logistics League 시뮬레이션 사건을 객체 중심 이벤트 로그(OCEL)로 만들어 이후 사건·시각을 예측한 프리프린트. 본문은 ar5iv 로 열었다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1349",
      "org": "ISO (ANSI Webstore 미리보기)",
      "title": "ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview)",
      "published": "2000",
      "url": "https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 11064-1:2000 미리보기(표지·목차·머리말·서론). 계열의 8개 부 제목을 확인했고 적용 범위 절과 본문은 미리보기에 없다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-237",
      "question": "여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가?",
      "areas": [
        37,
        21
      ],
      "status": "해결",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#11-열린-질문"
    },
    {
      "action": "new",
      "question": "VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가?",
      "areas": [
        37,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? 평가 항목 수가 바이라인네트워크 보도(16개 항목)와 한국로봇산업진흥원 안내(관제장치를 포함한 8개 심사 항목)에서 다르게 표현되므로 현행 기준도 함께 확인해야 한다.",
      "areas": [
        37,
        59,
        66
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열",
      "kind": "표준",
      "org": "ISO",
      "url": "https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf",
      "related_areas": [
        37,
        38
      ],
      "summary": "설계 원칙, 관제 공간·관제실 배치, 작업대 배치·치수, 표시 장치와 조작기, 환경 요건, 관제 센터 평가 원칙 등 여러 부로 관제 센터의 인간공학 설계를 다룬다. ISO 11064-1:2000 미리보기 머리말 기준이며 각 부의 이후 개정 여부·적용 범위는 미확인이다.",
      "ref_id": "ref-1349"
    },
    {
      "name": "IEEE 7001-2021 자율 시스템 투명성 표준",
      "kind": "표준",
      "org": "IEEE Standards Association",
      "url": "https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy",
      "related_areas": [
        37,
        31,
        50
      ],
      "summary": "사용자, 검증·인증 담당자, 고장·사고 조사자, 전문 자문가, 일반 대중의 이해관계자 범주마다 객관적으로 평가할 수 있는 다섯 단계 투명성 수준을 정한다. IEEE SA 소개 글(2022-05-11) 기준이며 표준 본문은 미열람이다.",
      "ref_id": "ref-1338"
    }
  ],
  "additional_research_requests": [
    "5절 적용 사례: 제조 공장·상업 시설에서 여러 로봇을 하나의 관제 화면·실행 기록으로 운영한 사례가 이번에도 없다. 두 현장 유형의 사례(한국 사례 우선)를 조사해 달라.",
    "5절 실외 사례·새 열린 질문: 실외이동로봇 운행안전인증의 관제 장치 항목이 화면 표시·운행 기록 저장·보관을 어디까지 요구하는지, 평가 항목 수(기사 16개, 진흥원 안내 심사 항목 8개) 가운데 현행 기준이 무엇인지 인증 고시 원문으로 확인이 필요하다.",
    "11절 oq-252: 윤리적 블랙박스 초안 부록(기록 항목·보관 시간 창·보안 요건)을 PDF 원문으로 읽어 플랫폼 수준 기록 항목과 비교할 근거가 필요하다.",
    "11절 oq-239: 마약류 관리에 관한 법률 시행규칙 등 국내 법령 원문으로 병원 특수 물품 로봇 배송 이력의 보관 기간·무결성 요건을 확인해야 한다.",
    "7절·11절 oq-240: IEEE 7001-2021 표준 본문과 ISO 11064 각 부의 적용 범위·현행 개정판을 확인해야 화면·기록 요건 포함 여부를 판단할 수 있다.",
    "프런트매터 related_areas 는 10절(주제 페이지로 분리됨)과 맞추려고 바꾸지 않았다. 이번에 9·11절에서 연결한 21. 상호운용 표준·적합성, 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스, 66. 실외를 다음 갱신에서 10절 연결에 더할지 검토가 필요하다.",
    "참고문헌 중복 확인(퍼블리셔 담당): 브리프의 ref-1120 는 기존 ref-1120 과, ref-762 은 기존 ref-762 와 같은 URL 이다. 브리프 id 를 그대로 썼으므로 퍼블리셔의 같은 URL 병합이 적용되는지 확인을 요청한다."
  ],
  "fixes_applied": [
    "f4 '누가 개입했는지' 과장 수정 — 7절 'Open-RMF 작업 상태 스키마의 배차 상태·개입 기록' 행을 '작업 요청자(booking.requester)와, 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다의 요청 시각·라벨(예: dashboard)로 어떤 창구에서 개입했는지'로 쓰고 개입 요청에는 요청자 필드가 없다고 밝혔다.",
    "f6 '실행 기록이 남지 않지만' 수정 — 7절 rmf-web 행을 '기본 설정은 메모리 안의 SQLite(비영속 내부 데이터베이스)를 쓰며 db_url 로 영속 저장 가능'으로 고치고 ref-762 각주를 ref-302 와 함께 달았으며 두 문서가 같은 저장소라 독립 출처가 아님을 적었다.",
    "f19 항목 수 차이 — 5절 실외 사례 표와 서술에서 '16개 항목'은 바이라인네트워크 보도 기준, 한국로봇산업진흥원 안내는 관제장치를 포함한 8개 심사 항목을 나열한다고 둘 다 제시했고, 이 차이를 둘째 새 열린 질문(11절과 open_question_updates)에 덧붙였으며 조합 인증·관제장치 평가는 [사실] 유지했다.",
    "f19 범위 경계 — 5절 실외 사례 서술과 9절 '업종별 조건(실외)' 행에 인증 판단은 인증 기관·운영자 쪽 연계 대상이고 ROP 에는 실외 현장의 운행 제약으로만 반영된다고 [추정]으로 썼다.",
    "f10 기준일 — 7절 ISO 11064 행에 'ISO 11064-1:2000 미리보기 머리말 기준(확인일 2026-10-09), 각 부의 이후 개정 여부와 적용 범위는 미확인'을 적었다.",
    "f8 공동 후원 표현 — 7절 IEEE 7001-2021 행을 'IEEE 로봇·자동화 학회가 공동 후원 학회 가운데 하나다'로 고치고 표준 본문이 아니라 IEEE SA 소개 글(2022-05-11) 기준임을 밝혔다(11절 oq-240 항목에도 소개 글 기준 표기).",
    "f2 logReport 경계 — 7절 표 아래 문장과 9절 '로봇 자체 지능·제어(상태 값·로봇 로그)' 행에서 logReport 로 생성되는 로그 자체는 로봇 쪽 기록(연계 대상)이고 ROP 는 생성 요청과 로그 이름(동작 상태) 수신만 맡는다고 썼다.",
    "f13·f14·f15 EU AI Act — 9절 표 아래 단락에서 조문 내용은 [사실]로, 고위험 AI 해당 여부와 보관 의무 해석은 59. 법·규제·보험·라이선스 쪽 연계 대상으로 짧게 다루고 ROP 몫을 보관 기간 설정과 로그 통제 주체 표시 기능으로 한정해 [추정]으로 썼으며, 제19조·제26조는 '같은 규정'이라고 밝히고 교차 확인으로 표시하지 않았다.",
    "f17 단일 보도 — 5절 둘째 병원 사례 표와 서술에 '3만 1607건'이 코메디닷컴 단일 보도 기준(2024-04-20)임을 밝혔다.",
    "f18 벤더 주장 — 5절 물류창고 사례의 표와 서술에 [추정] 뒤 '벤더 주장'을 병기하고 기술검증 착수 발표뿐이며 운영 결과는 확인되지 않았다고 썼으며, 물류 흐름 단계는 서술하지 않았다.",
    "f24 객체 유형·예측 대상 — 11절 oq-131 항목에서 객체 유형을 '로봇·주문·부품(제품)'으로, 예측 대상을 '이후 사건과 그 시각(남은 사건 순서 포함)'으로 썼다.",
    "f1·f2 VDA 5050 기준 — 7절 VDA 5050 세 행에 '기준 3.0.0(main), 발행일 미확인, 확인일 2026-10-09'를 적고 기존 각주 ref-031 을 재사용했다(13절 접근일 2026-10-09로 갱신).",
    "각주 원문 미열람 표시 — 13절에서 ref-944·ref-1007·ref-976·ref-980·ref-1099·ref-253 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "11절 열린 질문 정리 — oq-237 을 해결(근거 f1·f3·f4, 대응표 문제는 새 질문으로 이음)로 바꾸고, oq-238·oq-239 는 열림 유지, oq-131·oq-240·oq-252·oq-316 은 해결로 바꾸지 않고 부분 근거(f24·f25, f8·f9·f10, f11·f12, f13·f14·f15)만 덧붙였으며, 기존 '(새 질문, 상태: 열림)' 네 줄을 oq-237·oq-238·oq-239·oq-240 으로 표기했다.",
    "용어집 혼동 방지 — '운용 상태'(operational-state) 항목 설명에 기존 용어 '운용 모드'(Operating Mode, VDA 5050 operatingMode)와 다른 개념임을 한 문장으로 밝혔다.",
    "분량 초과 자동 분리: 37. 관제 화면·실행 기록 본문 11,771자 > 기준 4,000자 → 3개 절을 주제 페이지로 옮김, 남은 본문 5,946자"
  ]
}
```

### runs/2026-10-09-15/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (5개 절)
- 분량 초과 자동 분리:
    - docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area37-s7.md (2,936자)
    - docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area37-s11.md (2,787자)
    - docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md "3. 왜 중요한가" → docs/topics/2026/2026-10-09-area37-s3.md (485자)
```

### runs/2026-10-09-15/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md

```markdown
---
title: "37. 관제 화면·실행 기록"
type: area
category: "J. 현장 운영·관제"
area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [관제 화면, 실행 기록, 작업 상태, 로그 재생, 설명 가능한 표시, Open-RMF]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-10-09
sources: [ref-1093, ref-302, ref-111, ref-1094, ref-1095, ref-031, ref-1096, ref-1097, ref-1098, ref-477, ref-1099, ref-1100, ref-1101, ref-1102, ref-1103, ref-253, ref-1338, ref-1120, ref-863, ref-1341, ref-1342, ref-1343, ref-1344, ref-944, ref-1345, ref-980, ref-1007, ref-976, ref-762, ref-1347, ref-1348, ref-1349]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 37. 관제 화면·실행 기록

# 37. 관제 화면·실행 기록

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]

## 3. 왜 중요한가

관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 왜 중요한가](../../topics/2026/2026-10-09-area37-s3.md)에 있다.

## 4. 핵심 개념과 용어

관제 화면과 실행 기록에 관련된 개념을 정리한다.

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area37-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

관제 화면·실행 기록의 현장 근거는 병원·물류창고·실외·가정·기타 현장에서 찾았지만 대부분 보도·발표 단계 자료여서, 화면 항목과 기록 형식까지 공개한 사례는 2026-10-09 기준으로 확인하지 못했다. [추정][^ref-1103][^ref-1344][^ref-1343][^ref-1345][^ref-976][^ref-1007]

### 병원 — 특수 물품 배송 이력 관리 계획

**현장 유형:** 병원

**사례:** 병원에서 특수 물품을 로봇으로 배송하고 수령 인증과 배송 이력을 남기는 계획(한림대학교의료원 협약, 2025-04-07 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 특수 물품(품목 범위는 미확인) [사실][^ref-1103] |
| 수행 자원 | 병원 맞춤형 배송 로봇과 관제 시스템(공동 개발 계획) [사실][^ref-1103] |
| 제약 | 미확인 |
| 완료·인계 | 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템(개발 계획) [사실][^ref-1103] |
| 예외·성과 | 미확인(운영 결과 보도 없음) |

아주경제 2025-04-07 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다. [사실][^ref-1103] 이 보도는 협약·개발 계획 단계이며, 실제 운영 여부와 처리량·시간 같은 결과는 확인되지 않았다.

이 사례에서 37. 관제 화면·실행 기록은 완료·인계 칸에 관여한다. 배송 이력을 남겨야 하는 현장에서는 실행 기록이 '누구에게 넘겨졌는가'를 나중에 확인하는 근거가 된다. [추정][^ref-1103]

### 병원 — 여러 제조사 서비스 로봇의 통합 관제

**현장 유형:** 병원

**사례:** 커맨드센터가 7종 73대의 서비스 로봇을 하나의 통합관제시스템으로 운영(한림대학교성심병원, 2024-04 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인(로봇 종류는 안내·배송·방역 등) |
| 수행 자원 | 안내·배송·방역 로봇 등 7종 73대의 서비스 로봇과 커맨드센터의 통합관제시스템 [사실][^ref-1344][^ref-944] |
| 제약 | 미확인 |
| 완료·인계 | 미확인(관제 화면 항목·배송 이력 조회 방식 미공개) |
| 예외·성과 | 2022-08부터 2024-03까지 로봇 서비스 3만 1607건 시행(코메디닷컴 단일 보도 기준, 2024-04-20) [사실][^ref-1344] |

한림대학교성심병원은 2024-04 기준 안내·배송·방역 로봇 등 7종 73대의 서비스 로봇을 커맨드센터의 통합관제시스템으로 운영하며, 이 내용은 코메디닷컴(2024-04-20)과 로봇신문(2024-04-15) 두 보도가 함께 전한다. [사실][^ref-1344][^ref-944] 커맨드센터 담당자는 “각기 다른 제조사의 로봇들을 하나의 관제시스템으로 연결하는 일이 중요하다”고 밝혔다. [사실][^ref-1344] 같은 코메디닷컴 보도에 따르면 로봇 서비스는 2022-08부터 2024-03까지 3만 1607건 시행되었고, 이 수치는 단일 보도 기준이다. [사실][^ref-1344] 관제 화면 항목이나 배송 이력 조회 방식은 공개되지 않았다. [사실][^ref-1344]

이 사례에서 37. 관제 화면·실행 기록은 서로 다른 제조사 로봇을 한 관제시스템으로 묶는 수행 자원 칸에 관여하는 것으로 보인다. [추정][^ref-1344]

### 물류창고 — 통합운영 플랫폼 기술검증 착수

**현장 유형:** 물류창고

**사례:** Open-RMF 기반 로봇 통합운영 플랫폼의 물류센터 기술검증 착수(LG CNS·G마켓 동탄 물류센터, 2023-07-06 발표)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | AGV·AMR·오토스토어·소팅로봇을 연계한 로봇 통합운영 플랫폼 [추정] 벤더 주장[^ref-1343] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(기술검증 착수 발표뿐이며 운영 결과 미공개) |

LG CNS 는 2023-07-06 보도자료에서 Open-RMF 를 바탕으로 한 로봇 통합운영 플랫폼에서 고객이 로봇의 이동 동선과 작업 처리 결과를 실시간으로 한눈에 확인할 수 있고, AGV·AMR·오토스토어·소팅로봇이 연계되어 있으며, G마켓 동탄 물류센터에서 기술검증에 착수했다고 밝혔다. [추정] 벤더 주장[^ref-1343] 이는 기술검증 착수 발표뿐이며, 운영 결과는 확인되지 않았다.

### 실외 — 운행안전인증과 관제 장치

**현장 유형:** 실외

**사례:** 실외이동로봇을 운행하기 전에 로봇과 관제장치의 조합으로 운행안전인증을 받는 경우(2024-01 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 미확인 |
| 제약 | 운행안전인증은 로봇과 관제장치의 조합에 주어지고 관제 장치가 평가 대상에 든다. 평가 항목 수는 기사(16개)와 한국로봇산업진흥원 안내(심사 항목 8개)의 표현이 다르다 [사실][^ref-1345][^ref-980] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

국내 [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)은 로봇과 관제장치의 조합에 주어지고 관제 장치가 평가 대상에 들며, 이는 바이라인네트워크 보도(2024-01-31)와 한국로봇산업진흥원 안내 두 출처로 확인된다. [사실][^ref-1345][^ref-980] 평가 항목 수는 출처마다 표현이 다르다. 바이라인네트워크 보도는 속도 제어·비상정지·장애물 감지·횡단보도 통행·운행구역 준수·관제 장치 등 16개 항목을 평가하고 모든 기준을 만족해야 인증한다고 전한다. [사실][^ref-1345] 한국로봇산업진흥원 안내는 관제장치를 포함한 8개 심사 항목을 나열한다. [사실][^ref-980]

어느 쪽이 현행 기준인지와 관제 장치 항목이 화면 표시·운행 기록을 어디까지 요구하는지는 확인하지 못해 11절 열린 질문으로 올렸다. 인증 판단은 인증 기관과 운영자 쪽의 연계 대상이며, ROP 에는 실외 현장에서 관제 장치가 운행 제약의 하나가 된다는 점으로만 반영될 것으로 보인다. [추정][^ref-1345][^ref-980]

### 가정 — 공동주택 로봇 택배의 관제실 연동

**현장 유형:** 가정

**사례:** 공동주택 단지 로봇 택배에서 집하처의 송장번호 인식으로 관제실에 물품 정보를 전달하는 시나리오(LH토지주택연구원 자료 인용 보도, 2024-07-18)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 택배 차량이 단지 집하처에 송장번호를 인식시키면 물품 정보가 관제실로 전달된다(시나리오 단계 서술) [사실][^ref-976] |
| 작업 대상 | 택배 물품과 송장번호로 인식한 물품 정보 [사실][^ref-976] |
| 수행 자원 | 미확인 |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

정보통신신문 보도(2024-07-18)는 LH토지주택연구원 자료를 인용해, 공동주택 단지 로봇 택배에서 택배 차량이 단지 집하처에 송장번호를 인식시키면 물품 정보가 관제실로 전달된다고 전하며, 이는 시나리오 단계 서술이다. [사실][^ref-976] 이 사례에서 37. 관제 화면·실행 기록은 관제실이 받은 물품 정보로 배송 작업 기록이 시작되는 시작 조건 칸에 관여하는 것으로 보인다. [추정][^ref-976]

### 기타 — 농업 로봇 통합 관리 프로그램

**현장 유형:** 기타

**사례:** 농촌진흥청이 자체 개발한 농업 로봇 3종을 하나의 화면으로 관리(2025-04-23 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 자체 개발한 방제·운반·모니터링 로봇 3종과 이를 하나의 화면으로 관리하는 통합 관리 프로그램 [사실][^ref-1007] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

농촌진흥청의 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리한다(2025-04-23 보도 기준). [사실][^ref-1007] 다른 제조사 로봇의 연결 여부는 보도에 없다. [사실][^ref-1007]

제조 공장·상업 시설 현장의 관제 화면·실행 기록 사례는 이번 조사(2026-10-09)에서도 찾지 못했다.

## 6. 대표 접근법과 기술

접근법은 지도 위 통합 상태 표시, 실행 기록 저장과 시간축 재생, 설명 가능한 표시의 세 갈래로 나뉜다. 앞의 두 갈래는 공개 구현이 있고, 셋째는 연구 단계다. [추정][^ref-1093][^ref-302][^ref-1098]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area37-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

관제 화면·실행 기록에 쓸 수 있는 공개 구현과 명세는 다음과 같다(확인일 2026-09-30, 상태 값 규약·관제실·투명성·기록 장치 행은 2026-10-09 추가). [사실][^ref-1093][^ref-031][^ref-1096]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area37-s7.md)에 있다.

## 8. 대표 연구와 자료

설명 가능한 표시와 다중 로봇 관제 인터페이스에 관한 연구는 다음 세 건이 대표적이며, 모두 실험실·알고리즘 수준이다. [추정][^ref-1098][^ref-477][^ref-1099]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 연구와 자료](../../topics/2026/2026-09-30-area37-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 제조사 플릿과 설비가 내보내는 상태를 받아 하나의 화면과 기록으로 묶는 쪽을 맡고, 로봇 내부 기록과 설비 자체 관제 화면은 연계 대상으로 둘 것으로 보인다. [추정][^ref-1093][^ref-031]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 제조사 플릿이 보고한 위치·계획 경로·작업 상태를 하나의 층별 지도에 표시하고, 공통 작업 상태 값·단계·수준별 로그로 정규화해 기록 [추정][^ref-1093][^ref-111][^ref-1094] | 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록), 로컬 회피 시각화 — 로봇 제조사 [추정][^ref-1096][^ref-031] |
| 로봇 자체 지능·제어(상태 값·로봇 로그) | VDA 5050 동작 상태·오류 수준, MassRobotics 운용 상태, Open-RMF 작업 상태처럼 값 집합과 단위(동작·로봇·작업)가 다른 상태 값을 대응표로 맞추는 정규화 [추정][^ref-031][^ref-253][^ref-111]; VDA 5050 logReport 생성 요청과 로그 이름(동작 상태) 수신 [추정][^ref-031] | logReport 로 생성되는 로그 자체와 로봇 내부의 센서·구동기·제어 결정 기록(윤리적 블랙박스 초안이 다루는 대상) — 로봇 제조사 [추정][^ref-031][^ref-1120] |
| 시설·설비 제어 | 승강기·문 상태를 같은 지도에 겹쳐 표시하고 기록 [추정][^ref-1093] | 승강기·자동문·CCTV 같은 설비의 자체 관제 화면 — 시설·설비 쪽 [추정][^ref-1093] |
| 업종별 조건(실외) | 실외이동로봇 운행안전인증이 로봇과 관제장치의 조합에 주어지는 점을 실외 현장의 운행 제약으로 반영 [추정][^ref-1345][^ref-980] | 인증 여부 판단과 관제 장치 항목의 세부 요건 충족 — 인증 기관·운영자 [추정][^ref-980] |

이번 자료를 종합하면 ROP가 직접 맡을 범위는 통합 화면, 정규화한 실행 기록, 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색, 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시다. [추정][^ref-1093][^ref-302][^ref-111][^ref-1094][^ref-1096][^ref-1098][^ref-477] 6절에서 예로 든 나콘·ARC brain·Foxglove도 같은 범위의 기능을 내세우지만 독립 확인이 없다. [추정] 벤더 주장[^ref-1101][^ref-1102][^ref-1097] ROP는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태를 받는 인터페이스를 맡는다. [추정][^ref-031]

실행 기록의 보관 의무는 연계 대상이다. EU AI Act 제12조는 고위험 AI 시스템이 수명 동안 [자동 사건 기록](../../glossary/automatic-recording-of-events.md)을 할 수 있게 기술적으로 갖추고, 그 기록이 위험 상황·실질적 변경의 식별, 출시 후 모니터링, 배포자의 운용 모니터링을 뒷받침하게 한다(규정 2024/1689, 2024-07-12 발행). [사실][^ref-863] 같은 규정의 제19조 제1항과 제26조 제6항은 자동 생성 로그를 공급자와 배포자가 각자 통제하는 범위에서 목적에 맞는 기간, 최소 6개월 보관하게 하고, 개인정보 보호법 등 다른 법이 다르게 정하면 그에 따르게 한다(두 조문은 같은 규정이다). [사실][^ref-1341][^ref-1342] 로봇 플랫폼의 AI 구성요소가 고위험 AI 에 해당하는지와 보관 의무의 해석은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) 쪽 연계 대상이며, ROP 몫은 실행 기록의 보관 기간 설정과 로그 통제 주체 표시 기능으로 한정될 것으로 보인다. [추정][^ref-863][^ref-1341][^ref-1342]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 화면과 기록은 운영·지도·연동·재현 영역과 두루 이어진다. 아래 연결은 이번 조사 자료를 바탕으로 한 판단이다. [추정][^ref-1093][^ref-111][^ref-1094][^ref-031][^ref-1099][^ref-1103]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area37-s10.md)에 있다.

## 11. 열린 질문

공통 상태 값 규약을 묻던 oq-237 은 해결로 보고, 나머지 질문에는 부분 근거만 더했다(2026-10-09 기준). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 열린 질문](../../topics/2026/2026-10-09-area37-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) — 영역 심화: 3~11절 신규 작성, 13절 각주 정의 15건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 15건 반영). 2차: 3절 첫 문장을 태그 없는 연결 문장으로, 4절 도입 문장의 [사실] 태그 제거, 9절 '상용 예로'를 '6절에서 예로'로 고침 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area37-s6.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로 고침 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 대표 연구와 자료](../../topics/2026/2026-09-30-area37-s8.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "8. 대표 연구와 자료" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area37-s4.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차: 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 뗀 연결 문장으로 바꿈 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area37-s10.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차: 짝 엔진을 번호와 이름으로 표기, 39. 운영 성과 측정·개선 항목의 '실제 소요 시간' 드리프트 수정 (실행 2026-09-30-13)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-302]: Open Robotics (open-rmf/rmf-web), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-10-09
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-09-30
[^ref-1097]: Foxglove, Playback — Foxglove Documentation, 미확인, https://docs.foxglove.dev/docs/visualization/playback, 접근일 2026-09-30
[^ref-1098]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-10-09 (원문 미열람)
[^ref-1101]: 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON), 미확인, https://robotics.hyundai.com/projects/research/view.do?seq=102, 접근일 2026-09-30
[^ref-1102]: 네이버클라우드, ARC brain 개요 - 사용 가이드, 미확인, https://guide.ncloud-docs.com/docs/arc-brain-overview, 접근일 2026-09-30
[^ref-1103]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-09-30
[^ref-253]: MassRobotics (MassRobotics-AMR/AMR_Interop_Standard), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09
[^ref-863]: European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 12: Record-keeping, 2024-07-12, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-10-09
[^ref-1341]: European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 19: Automatically generated logs, 2024-07-12, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19, 접근일 2026-10-09
[^ref-1342]: European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 26: Obligations of deployers of high-risk AI systems, 2024-07-12, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26, 접근일 2026-10-09
[^ref-1343]: LG CNS (LG 미디어 보도자료), ‘로봇 통합운영 플랫폼’ 개발, 2023-07-06, https://lg.co.kr/media/release/26480, 접근일 2026-10-09
[^ref-1344]: 코메디닷컴, [메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠, 2024-04-20, https://kormedi.com/1682189/, 접근일 2026-10-09
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)
[^ref-1345]: 바이라인네트워크 (이진호), 뉴빌리티, 실외이동 로봇 운행안전 인증 획득, 2024-01-31, https://byline.network/2024/01/240131_00004/, 접근일 2026-10-09
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)
[^ref-1007]: 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동, 2025-04-23, https://www.newstomato.com/ReadNews.aspx?no=1259970, 접근일 2026-10-09 (원문 미열람)
[^ref-976]: 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’, 2024-07-18, https://www.koit.co.kr/news/articleView.html?idxno=123976, 접근일 2026-10-09 (원문 미열람)
```

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md

```markdown
---
title: "37. 관제 화면·실행 기록"
type: area
category: "J. 현장 운영·관제"
area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [관제 화면, 실행 기록, 작업 상태, 로그 재생, 설명 가능한 표시, Open-RMF]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1093, ref-302, ref-111, ref-1094, ref-1095, ref-031, ref-1096, ref-1097, ref-1098, ref-477, ref-1099, ref-1100, ref-1101, ref-1102, ref-1103]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 37. 관제 화면·실행 기록

# 37. 관제 화면·실행 기록

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]

## 3. 왜 중요한가

관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.

이 영역이 중요한 까닭은 세 가지로 정리된다. 다중 로봇 인터페이스 연구(Roldán 외)는 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었고, 공정 산업의 인간–기계 인터페이스(Human-Machine Interface, HMI) 표준은 화면을 설계·구현·운영·지속 개선의 수명주기 전체에 걸쳐 관리할 대상으로 보며, 병원처럼 배송 이력을 남기려는 현장에서는 실행 기록이 인계 확인의 근거가 된다. [추정][^ref-1099][^ref-1100][^ref-1103]

핵심 질문에 비추면, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만, '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이다. 실제 다중 제조사 플릿 관제 화면에서 그 효과를 측정한 공개 자료는 이번 조사 범위(2026-09-30 기준)에서 찾지 못했다. [추정][^ref-1093][^ref-111][^ref-1094][^ref-031][^ref-1098][^ref-477][^ref-1099]

## 4. 핵심 개념과 용어

관제 화면과 실행 기록에 관련된 개념을 정리한다.

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area37-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 관제 화면·실행 기록의 현장 근거를 찾은 것은 병원 한 건이며, 그것도 협약·개발 계획 단계 보도다. [사실][^ref-1103]

**현장 유형:** 병원

**사례:** 병원에서 특수 물품을 로봇으로 배송하고 수령 인증과 배송 이력을 남기는 계획(한림대학교의료원 협약, 2025-04-07 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 특수 물품(품목 범위는 미확인) [사실][^ref-1103] |
| 수행 자원 | 병원 맞춤형 배송 로봇과 관제 시스템(공동 개발 계획) [사실][^ref-1103] |
| 제약 | 미확인 |
| 완료·인계 | 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템(개발 계획) [사실][^ref-1103] |
| 예외·성과 | 미확인(운영 결과 보도 없음) |

아주경제 2025-04-07 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다. [사실][^ref-1103] 이 보도는 협약·개발 계획 단계이며, 실제 운영 여부와 처리량·시간 같은 결과는 확인되지 않았다.

이 사례에서 37. 관제 화면·실행 기록은 완료·인계 칸에 관여한다. 배송 이력을 남겨야 하는 현장에서는 실행 기록이 '누구에게 넘겨졌는가'를 나중에 확인하는 근거가 된다. [추정][^ref-1103]

물류창고·제조 공장·상업 시설·가정·실외·기타 현장의 관제 화면·실행 기록 사례는 이번 조사(2026-09-30)에서 찾지 못했다.

## 6. 대표 접근법과 기술

접근법은 지도 위 통합 상태 표시, 실행 기록 저장과 시간축 재생, 설명 가능한 표시의 세 갈래로 나뉜다. 앞의 두 갈래는 공개 구현이 있고, 셋째는 연구 단계다. [추정][^ref-1093][^ref-302][^ref-1098]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area37-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

관제 화면·실행 기록에 쓸 수 있는 공개 구현과 명세는 다음과 같다(확인일 2026-09-30). [사실][^ref-1093][^ref-031][^ref-1096]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Open-RMF rmf_visualization | 오픈소스 | 층 평면도 위에 로봇 위치·문·승강기·주행 그래프·예측 궤적 표시 | [사실][^ref-1093] |
| Open-RMF rmf-web | 오픈소스 | 웹 대시보드·API 서버. 기본은 비영속 저장 | [사실][^ref-302] |
| Open-RMF rmf_api_msgs 작업 상태·작업 로그 스키마 | 오픈소스 | 상태 값 12개, 작업·단계·사건 3계층 로그 | [사실][^ref-111][^ref-1094][^ref-1095] |
| VDA 5050 3.0.0 visualization·state 토픽 | 표준 | 차량 위치·계획 경로를 시각화 시스템에 보내는 토픽을 상태 토픽과 분리 | [사실][^ref-031] |
| MCAP | 오픈소스 | 시각 색인을 둔 기록 컨테이너 형식 | [사실][^ref-1096] |
| ISA-101.01-2015, ISA-TR101.01-2022(HMI 철학), ISA-TR101.02-2019(HMI 사용성과 성능) | 표준 | HMI 수명주기(설계·구현·운영·지속 개선)를 다루며 연속·배치·이산 산업에 적용된다고 밝힌다. 표준 본문은 유료라 발행 기관 소개 페이지 기준 | [사실][^ref-1100] |
| Foxglove 재생 기능 | 벤더 도구 | 시간축 탐색·사건 주석·lookback 재생 | [추정] 벤더 주장[^ref-1097] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

설명 가능한 표시와 다중 로봇 관제 인터페이스에 관한 연구는 다음 세 건이 대표적이며, 모두 실험실·알고리즘 수준이다. [추정][^ref-1098][^ref-477][^ref-1099]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 연구와 자료](../../topics/2026/2026-09-30-area37-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 제조사 플릿과 설비가 내보내는 상태를 받아 하나의 화면과 기록으로 묶는 쪽을 맡고, 로봇 내부 기록과 설비 자체 관제 화면은 연계 대상으로 둘 것으로 보인다. [추정][^ref-1093][^ref-031]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 제조사 플릿이 보고한 위치·계획 경로·작업 상태를 하나의 층별 지도에 표시하고, 공통 작업 상태 값·단계·수준별 로그로 정규화해 기록 [추정][^ref-1093][^ref-111][^ref-1094] | 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록), 로컬 회피 시각화 — 로봇 제조사 [추정][^ref-1096][^ref-031] |
| 시설·설비 제어 | 승강기·문 상태를 같은 지도에 겹쳐 표시하고 기록 [추정][^ref-1093] | 승강기·자동문·CCTV 같은 설비의 자체 관제 화면 — 시설·설비 쪽 [추정][^ref-1093] |

이번 자료를 종합하면 ROP가 직접 맡을 범위는 통합 화면, 정규화한 실행 기록, 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색, 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시다. [추정][^ref-1093][^ref-302][^ref-111][^ref-1094][^ref-1096][^ref-1098][^ref-477] 6절에서 예로 든 나콘·ARC brain·Foxglove도 같은 범위의 기능을 내세우지만 독립 확인이 없다. [추정] 벤더 주장[^ref-1101][^ref-1102][^ref-1097] ROP는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태를 받는 인터페이스를 맡는다. [추정][^ref-031]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 화면과 기록은 운영·지도·연동·재현 영역과 두루 이어진다. 아래 연결은 이번 조사 자료를 바탕으로 한 판단이다. [추정][^ref-1093][^ref-111][^ref-1094][^ref-031][^ref-1099][^ref-1103]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area37-s10.md)에 있다.

## 11. 열린 질문

실행 기록을 시뮬레이션으로 바꾸는 형식, 공통 상태·로그 규약, 설명 표시의 현장 효과는 아직 확인되지 않았다(2026-09-30 기준). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-131** (상태: 열림) 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? 이번 실행(2026-09-30-13)에서도 공개 형식을 찾지 못했다.
- (새 질문, 상태: 열림) 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가?
- (새 질문, 상태: 열림) 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가?
- (새 질문, 상태: 열림) 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가?
- (새 질문, 상태: 열림) 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) — 영역 심화: 3~11절 신규 작성, 13절 각주 정의 15건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 15건 반영). 2차: 3절 첫 문장을 태그 없는 연결 문장으로, 4절 도입 문장의 [사실] 태그 제거, 9절 '상용 예로'를 '6절에서 예로'로 고침 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area37-s6.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로 고침 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 대표 연구와 자료](../../topics/2026/2026-09-30-area37-s8.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "8. 대표 연구와 자료" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area37-s4.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차: 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 뗀 연결 문장으로 바꿈 (실행 2026-09-30-13)
- 2026-09-30 · 생성 · [37. 관제 화면·실행 기록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area37-s10.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차: 짝 엔진을 번호와 이름으로 표기, 39. 운영 성과 측정·개선 항목의 '실제 소요 시간' 드리프트 수정 (실행 2026-09-30-13)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-302]: Open Robotics (open-rmf/rmf-web), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-09-30
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-30
[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-1095]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — log_entry.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json, 접근일 2026-09-30
[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-09-30
[^ref-1097]: Foxglove, Playback — Foxglove Documentation, 미확인, https://docs.foxglove.dev/docs/visualization/playback, 접근일 2026-09-30
[^ref-1098]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30
[^ref-1100]: ISA (International Society of Automation), ISA-101 Series of Standards, 미확인, https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards, 접근일 2026-09-30
[^ref-1101]: 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON), 미확인, https://robotics.hyundai.com/projects/research/view.do?seq=102, 접근일 2026-09-30
[^ref-1102]: 네이버클라우드, ARC brain 개요 - 사용 가이드, 미확인, https://guide.ncloud-docs.com/docs/arc-brain-overview, 접근일 2026-09-30
[^ref-1103]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-09-30
```

### runs/2026-10-09-15/pages/topics/2026/2026-10-09-area37-s7.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-1093, ref-1094, ref-1095, ref-1096, ref-1097, ref-1100, ref-111, ref-253, ref-1338, ref-1120, ref-762, ref-1349, ref-302]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#7
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 관련 표준·프레임워크·오픈소스

# 37. 관제 화면·실행 기록 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 관제 화면·실행 기록에 쓸 수 있는 공개 구현과 명세는 다음과 같다(확인일 2026-09-30, 상태 값 규약·관제실·투명성·기록 장치 행은 2026-10-09 추가). [사실][^ref-1093][^ref-031][^ref-1096]
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

관제 화면·실행 기록에 쓸 수 있는 공개 구현과 명세는 다음과 같다(확인일 2026-09-30, 상태 값 규약·관제실·투명성·기록 장치 행은 2026-10-09 추가). [사실][^ref-1093][^ref-031][^ref-1096]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Open-RMF rmf_visualization | 오픈소스 | 층 평면도 위에 로봇 위치·문·승강기·주행 그래프·예측 궤적 표시 | [사실][^ref-1093] |
| Open-RMF rmf-web | 오픈소스 | 웹 대시보드·API 서버. 기본 설정은 메모리 안의 SQLite(비영속 내부 데이터베이스)를 쓰며, 설정의 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 지정해 영속 저장할 수 있다(확인일 2026-10-09, 두 문서는 같은 저장소라 독립 출처가 아니다) | [사실][^ref-762][^ref-302] |
| Open-RMF rmf_api_msgs 작업 상태·작업 로그 스키마 | 오픈소스 | 상태 값 12개, 작업·단계·사건 3계층 로그. 로그 항목은 순번(seq)·수준(tier)·밀리초 유닉스 시각·본문이 필수이고 수준 값은 uninitialized·info·warning·error 다(2026-10-09 재확인) | [사실][^ref-111][^ref-1094][^ref-1095] |
| Open-RMF 작업 상태 스키마의 배차 상태·개입 기록 | 오픈소스 | 작업 상태 값과 별도로 배차 상태를 queued·selected·dispatched·failed_to_assign·canceled_in_flight 로 기록한다. 작업 요청자(booking.requester)와, 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다의 요청 시각·라벨(예: dashboard)로 어떤 창구에서 개입했는지를 담으며, 개입 요청 자체에는 요청자 필드가 없다(확인일 2026-10-09) | [사실][^ref-111] |
| VDA 5050 3.0.0 visualization·state 토픽 | 표준 | 차량 위치·계획 경로를 시각화 시스템에 보내는 토픽을 상태 토픽과 분리. 기준 3.0.0(main), 발행일 미확인, 확인일 2026-10-09 | [사실][^ref-031] |
| VDA 5050 3.0.0 동작 상태·오류 수준 | 표준 | 로봇이 보고하는 동작 상태 값 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE, 오류 수준 WARNING·URGENT·CRITICAL·FATAL 네 단계, 오류마다 사람이 읽는 설명(errorDescription)·조치 힌트(errorHint)와 ISO 639-1 언어 코드별 번역. 기준 3.0.0(main), 발행일 미확인, 확인일 2026-10-09 | [사실][^ref-031] |
| VDA 5050 3.0.0 information 배열·logReport | 표준 | 로봇이 state 메시지의 information 배열로 보내는 부가 정보는 플릿 관제가 로직에 쓰지 않고 시각화·디버깅에만 쓴다. logReport 즉시 동작으로 로봇에 로그 보고서 생성·저장을 요청하고 저장된 로그 이름을 동작 상태로 보고받는다. 기준 3.0.0(main), 발행일 미확인, 확인일 2026-10-09 | [사실][^ref-031] |
| MassRobotics AMR 상호운용 표준 statusReport | 표준 | uuid·timestamp·operationalState·location 이 필수이고, 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 정한다. 오류 코드 배열, 약 10초의 단기 경로(예측 위치 최대 10개), 목적지, 배터리 잔량은 선택 항목이다. 공식 저장소 JSON 스키마 기준, 발행일 미확인, 확인일 2026-10-09 | [사실][^ref-253] |
| MCAP | 오픈소스 | 시각 색인을 둔 기록 컨테이너 형식 | [사실][^ref-1096] |
| ISA-101.01-2015, ISA-TR101.01-2022(HMI 철학), ISA-TR101.02-2019(HMI 사용성과 성능) | 표준 | HMI 수명주기(설계·구현·운영·지속 개선)를 다루며 연속·배치·이산 산업에 적용된다고 밝힌다. 표준 본문은 유료라 발행 기관 소개 페이지 기준 | [사실][^ref-1100] |
| ISO 11064 관제 센터 인간공학 설계 계열 | 표준 | 설계 원칙, 관제 공간 배치, 관제실 배치, 작업대 배치·치수, 표시 장치와 조작기, 환경 요건, 관제 센터 평가 원칙, 특정 적용의 인간공학 요건의 여러 부로 나뉜다. ISO 11064-1:2000 미리보기 머리말 기준(확인일 2026-10-09)이며, 각 부의 이후 개정 여부와 적용 범위는 미확인 | [사실][^ref-1349] |
| IEEE 7001-2021 자율 시스템 투명성 표준 | 표준 | 사용자, 검증·인증 담당자, 고장·사고 조사자, 소송·행정 절차의 전문 자문가, 일반 대중의 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 객관적으로 평가할 수 있는 다섯 단계의 투명성 수준을 정한다. IEEE 로봇·자동화 학회가 공동 후원 학회 가운데 하나다. 표준 본문이 아니라 IEEE SA 소개 글(2022-05-11) 기준 | [사실][^ref-1338] |
| [윤리적 블랙박스](../../glossary/ethical-black-box.md) 공개 표준 초안 | 프레임워크 | 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 같은 운용 데이터를 안전하게 기록하는 장치 또는 소프트웨어 모듈의 첫 초안(Winfield 외, 2022-05-13, ICRES 2022 제출). 부록의 기록 항목·보관 기간은 미확인 | [사실][^ref-1120] |
| Foxglove 재생 기능 | 벤더 도구 | 시간축 탐색·사건 주석·lookback 재생 | [추정] 벤더 주장[^ref-1097] |

VDA 5050 logReport 로 생성되는 로그 자체는 로봇 쪽 기록이어서 연계 대상이고, ROP 는 생성 요청과 로그 이름(동작 상태) 수신만 맡는 것으로 본다. [추정][^ref-031] 세 상태 값 규약(VDA 5050, MassRobotics, Open-RMF)은 값 집합과 단위가 서로 달라 9절과 11절에서 정규화 문제로 다룬다.

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-1095]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — log_entry.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json, 접근일 2026-10-09
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-09-30
[^ref-1097]: Foxglove, Playback — Foxglove Documentation, 미확인, https://docs.foxglove.dev/docs/visualization/playback, 접근일 2026-09-30
[^ref-1100]: ISA (International Society of Automation), ISA-101 Series of Standards, 미확인, https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards, 접근일 2026-09-30
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-253]: MassRobotics (MassRobotics-AMR/AMR_Interop_Standard), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-10-09 (원문 미열람)
[^ref-1338]: IEEE Standards Association, How To Make Autonomous Systems More Transparent and Trustworthy, 2022-05-11, https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy, 접근일 2026-10-09
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09
[^ref-762]: Open Robotics (open-rmf/rmf-web), rmf-web packages/api-server — README, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-1349]: ISO (ANSI Webstore 미리보기), ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview), 2000, https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf, 접근일 2026-10-09
[^ref-302]: Open Robotics (open-rmf/rmf-web), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-15 | 37. 관제 화면·실행 기록 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-15/pages/topics/2026/2026-10-09-area37-s11.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 열린 질문"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-1099, ref-111, ref-253, ref-1338, ref-1120, ref-1341, ref-1342, ref-1347, ref-1348, ref-1349]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#11
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 열린 질문

# 37. 관제 화면·실행 기록 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공통 상태 값 규약을 묻던 oq-237 은 해결로 보고, 나머지 질문에는 부분 근거만 더했다(2026-10-09 기준). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공통 상태 값 규약을 묻던 oq-237 은 해결로 보고, 나머지 질문에는 부분 근거만 더했다(2026-10-09 기준). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-131** (상태: 열림) 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? 이번 실행(2026-09-30-13)에서도 공개 형식을 찾지 못했다. 부분 근거로, Rohrer 외(2022)는 공장 물류를 모사한 RoboCup Logistics League 시뮬레이션의 사건을 데이터베이스에서 꺼내 로봇·주문·부품(제품) 객체와 11개 활동을 담은 [객체 중심 이벤트 로그](../../glossary/ocel.md)(OCEL JSON)로 만들고, 이후 사건과 그 시각(남은 사건 순서 포함)을 예측하는 데 썼다. [사실][^ref-1348] 그 로그를 시뮬레이션 시나리오 사양으로 되돌리는 변환 규칙은 이번(2026-10-09-15)에도 확인하지 못해, 기록 쪽 형식만 부분 근거가 된 것으로 보인다. [추정][^ref-1348]
- **oq-237** (상태: 해결 · 실행 2026-10-09-15) 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? 답: VDA 5050 3.0.0 은 동작 상태 값과 오류 수준 네 단계를 정한다. [사실][^ref-031] MassRobotics AMR 상호운용 표준은 로봇 운용 상태 아홉 값을 정한다. [사실][^ref-253] 다만 세 규약의 값 집합과 단위(동작·로봇·작업)가 달라 ROP 가 대응표로 정규화해야 할 것으로 보이며, 대응표 문제는 아래 새 질문으로 잇는다. [추정][^ref-031][^ref-253][^ref-111] 근거는 7절 표에 있다.
- **oq-238** (상태: 열림) 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? Patel 외(2021)는 여러 운영자가 다중 로봇을 함께 감독할 때의 투명성을 다루며, 자기 작업 정보만 보이는 방식·다른 운영자 작업 정보를 공유하는 방식·둘을 섞은 방식·없음의 네 모드를 참가자 18명의 사용자 연구로 비교해 인식·신뢰·작업 부하를 쟀다. [사실][^ref-1347] 이처럼 이번에 확인한 연구도 실험실 사용자 연구 수준이어서, 현장 측정 연구는 여전히 확인하지 못한 것으로 보인다. [추정][^ref-1347][^ref-1099]
- **oq-239** (상태: 열림) 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? 이번 실행(2026-10-09-15)에서도 법령 원문으로 로봇 배송 이력의 보관 요건을 확인하지 못했다.
- **oq-240** (상태: 열림) 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? ISO 11064 계열은 관제 센터 인간공학 설계를 표시 장치와 조작기, 관제 센터 평가 원칙 등 여러 부로 다룬다(ISO 11064-1:2000 머리말 기준). [사실][^ref-1349] IEEE 7001-2021 은 이해관계자 범주마다 다섯 단계의 투명성 수준을 정한다(IEEE SA 소개 글 기준). [사실][^ref-1338] IEEE 7001-2021 이 운영자(사용자)와 사고 조사자를 별도 이해관계자로 두므로 설명 가능한 표시는 운영자용, 실행 기록은 조사자용 투명성으로 나눠 평가하는 근거가 될 수 있어 보이나, 표준이 화면 설계나 기록 항목을 정하는지는 확인하지 못했다. [추정][^ref-1338] 두 표준 모두 다중 로봇 관제 화면에 특화된 것인지는 확인하지 못해 질문을 열어 둔다.
- **oq-252** (상태: 열림) 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? [윤리적 블랙박스](../../glossary/ethical-black-box.md) 초안(2022-05-13)은 소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록해 사고·아차 사고 조사를 돕는 첫 초안이다. [사실][^ref-1120] 이 초안은 로봇 한 대의 내부 기록을 대상으로 하고 VDA 5050 logReport 도 로봇 쪽 로그 생성을 요청할 뿐 기록 항목을 정하지 않아, 플랫폼 수준의 명령·정지·재가동 기록 항목을 정한 공개 규약은 이번에도 확인하지 못한 것으로 보인다. [추정][^ref-1120][^ref-031]
- **oq-316** (상태: 열림) 로봇 플랫폼의 AI 구성요소가 EU AI Act 고위험 AI 로 분류되면 제12조 자동 사건 기록 요건을 플랫폼 실행 기록이 충족해야 하는가, 그 기록의 보관 주체는 플랫폼 사업자와 배포자 가운데 누구인가? 9절의 제12조·제19조·제26조가 부분 근거다. 제19조와 제26조가 모두 공급자·배포자가 통제하는 범위에서 로그를 보관하게 하므로 보관 주체는 로그를 계약상 누가 통제하는지에 따라 나뉠 것으로 보이며, 로봇 플랫폼에 대한 적용 해석 자료는 찾지 못했다. [추정][^ref-1341][^ref-1342]
- (새 질문, 상태: 열림) VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가?
- (새 질문, 상태: 열림) 국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? 평가 항목 수가 바이라인네트워크 보도(16개 항목)와 한국로봇산업진흥원 안내(관제장치를 포함한 8개 심사 항목)에서 다르게 표현되므로 현행 기준도 함께 확인해야 한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-10-09 (원문 미열람)
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-253]: MassRobotics (MassRobotics-AMR/AMR_Interop_Standard), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-10-09 (원문 미열람)
[^ref-1338]: IEEE Standards Association, How To Make Autonomous Systems More Transparent and Trustworthy, 2022-05-11, https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy, 접근일 2026-10-09
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09
[^ref-1341]: European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 19: Automatically generated logs, 2024-07-12, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19, 접근일 2026-10-09
[^ref-1342]: European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 26: Obligations of deployers of high-risk AI systems, 2024-07-12, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26, 접근일 2026-10-09
[^ref-1347]: Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv), Transparency in Multi-Human Multi-Robot Interaction, 2021-05-14, https://arxiv.org/abs/2101.10495, 접근일 2026-10-09
[^ref-1348]: Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv), Predictive Object-Centric Process Monitoring, 2022-07-20, https://arxiv.org/abs/2207.10017, 접근일 2026-10-09
[^ref-1349]: ISO (ANSI Webstore 미리보기), ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview), 2000, https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-15 | 37. 관제 화면·실행 기록 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-15/pages/topics/2026/2026-10-09-area37-s3.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 왜 중요한가"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-1093, ref-1094, ref-1098, ref-1099, ref-1100, ref-1103, ref-111, ref-477]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#3
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 왜 중요한가

# 37. 관제 화면·실행 기록 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.

이 영역이 중요한 까닭은 세 가지로 정리된다. 다중 로봇 인터페이스 연구(Roldán 외)는 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었고, 공정 산업의 인간–기계 인터페이스(Human-Machine Interface, HMI) 표준은 화면을 설계·구현·운영·지속 개선의 수명주기 전체에 걸쳐 관리할 대상으로 보며, 병원처럼 배송 이력을 남기려는 현장에서는 실행 기록이 인계 확인의 근거가 된다. [추정][^ref-1099][^ref-1100][^ref-1103]

핵심 질문에 비추면, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만, '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이다. 실제 다중 제조사 플릿 관제 화면에서 그 효과를 측정한 공개 자료는 이번 조사 범위(2026-09-30 기준)에서 찾지 못했다. [추정][^ref-1093][^ref-111][^ref-1094][^ref-031][^ref-1098][^ref-477][^ref-1099]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-1098]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-10-09 (원문 미열람)
[^ref-1100]: ISA (International Society of Automation), ISA-101 Series of Standards, 미확인, https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards, 접근일 2026-09-30
[^ref-1103]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-09-30
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-15 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-15 | 37. 관제 화면·실행 기록 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1315건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 2026-09-25 | 예 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | https://github.com/open-rmf/rmf-web | 2026-09-25 | 예 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 미확인 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 2026-09-25 | 아니오 |
| ref-1093 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 미확인 | https://github.com/open-rmf/rmf_visualization | 2026-09-30 | 예 |
| ref-1094 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json | 2026-09-30 | 예 |
| ref-1095 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 2026-09-30 | 예 |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | https://mcap.dev/spec | 2026-09-30 | 예 |
| ref-1097 | Foxglove | Playback — Foxglove Documentation | 미확인 | https://docs.foxglove.dev/docs/visualization/playback | 2026-09-30 | 예 |
| ref-1098 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 2022-02 | https://arxiv.org/abs/2202.09930 | 2026-09-30 | 예 |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 2026-09-30 | 예 |
| ref-1100 | ISA (International Society of Automation) | ISA-101 Series of Standards | 미확인 | https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards | 2026-09-30 | 예 |
| ref-1101 | 현대자동차그룹 로보틱스랩 | PROJECTS — Robot Fleet Management (NARCHON) | 미확인 | https://robotics.hyundai.com/projects/research/view.do?seq=102 | 2026-09-30 | 예 |
| ref-1102 | 네이버클라우드 | ARC brain 개요 - 사용 가이드 | 미확인 | https://guide.ncloud-docs.com/docs/arc-brain-overview | 2026-09-30 | 예 |
| ref-1103 | 아주경제 | 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 | 2025-04-07 | https://www.ajunews.com/view/20250407084333272 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 374개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
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
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
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
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
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
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
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
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
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
- integrity-risk: 무결성 위험 (Integrity Risk)
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
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
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
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
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
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
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
- remote-attestation: 원격 증명 (Remote Attestation)
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
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
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
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
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
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
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
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
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
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [37] 에 걸린 9건 / 전체 331건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-237 [열림] 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? (영역 37, 21)
- oq-238 [열림] 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? (영역 37, 31)
- oq-239 [열림] 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? (영역 37, 59)
- oq-240 [열림] 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? (영역 37, 38)
- oq-248 [열림] 명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가? (영역 52, 37)
- oq-252 [열림] 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? (영역 50, 37, 38)
- oq-263 [열림] 여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가? (영역 40, 37)
- oq-316 [열림] 로봇 플랫폼의 AI 구성요소가 EU AI Act 고위험 AI 로 분류되면 제12조 자동 사건 기록 요건을 플랫폼 실행 기록이 충족해야 하는가, 그 기록의 보관 주체는 플랫폼 사업자와 배포자 가운데 누구인가? (영역 47, 37, 43)
```
