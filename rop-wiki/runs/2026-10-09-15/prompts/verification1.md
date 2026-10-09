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
- verification_stage: first
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
        "ref-1337"
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
        "ref-1337",
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
        "ref-1346",
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
        "ref-1339"
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
        "ref-1339",
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
        "ref-1340"
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
        "ref-1340",
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
      "id": "ref-1337",
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
      "id": "ref-1339",
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
      "id": "ref-1340",
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
      "id": "ref-1346",
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
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청이 없어 빈·약한 절(5절 현장 사례, 7절 표준, 9절 기록 보관 경계, 11절 열린 질문)과 바뀐 출처(rmf-web 저장 설정)만 조사했다. 검색 14회/30, 신규 출처 13건/15(ref-1337~ref-1349, 예약 구간 안), 재사용 9건. 신규 출처는 모두 원문 또는 공식 페이지를 열었다(webfetch 10, github_raw 2, 미리보기 1). 재사용 가운데 ref-031·ref-111 은 입력의 원문 텍스트(inbox), ref-302·ref-1095 는 github_raw 로 다시 열었고, ref-944·ref-1007·ref-976·ref-980·ref-1099 는 다시 열지 않아 source_unopened 로 표시했다. 교차 확인 1건(f16, 7종 73대 통합관제: 코메디닷컴·로봇신문). oq-237 해결 근거: f1·f3·f4·f5(Open-RMF 외에 VDA 5050 과 MassRobotics 가 공개 상태 값을 정함, 대응표는 없음 — 새 질문으로 올림). oq-238·oq-239 는 미해결, oq-131·oq-240·oq-252·oq-316 은 부분 근거만. 현장 유형: 병원(f16·f17), 물류창고(f18, 벤더 주장), 실외(f19), 기타(f20), 가정(f21). 제조 공장·상업 시설 사례는 검색 1회로 찾지 못했다. 벤더 주장 1건(f18). 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 섞지 않았고 f24·f25 는 기록 형식으로만 다뤘다. 핵심 질문에 대한 새 결론은 없으며 '무엇'의 표시 근거(상태 값 규약)만 보강되었다. 용어집에 이미 있는 윤리적 블랙박스·자동 사건 기록·HMI 철학·객체 중심 이벤트 로그는 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
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

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
```

### docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md (요약)

```markdown
# 40. 운영 절차·요청 창구

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

운영 절차·교대, 현장 사용자의 요청 창구 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 절차·교대**: 운영 표준 절차, 교대 인수인계, 역할을 정한다
- **현장 사용자 요청 창구**: 간호사·객실 직원·거주자처럼 비전문 사용자가 호출 버튼·앱·단말로 일을 요청한다

## 2. 핵심 질문

현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
```

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md (요약)

```markdown
# 17. 작업 대상·자산 식별과 인계 추적

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 4

## 1. 한 줄 정의

물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 대상 식별·추적**: 물품·자산·도구·운반구·검체·세탁물처럼 작업 대상의 식별자·위치·적재 관계를 추적한다
- **인계·책임 기록**: 누가 언제 무엇을 넘겨받았는지 관측 근거와 함께 기록한다
- **이벤트 공통 형식**: 상태·위치·이동·인계 이벤트를 공통 형식으로 주고받는다(GS1 EPCIS 등)
- **수령인 확인**: 물건을 사람에게 넘길 때 받는 사람을 PIN·카드·앱으로 확인하고 인계 기록을 남긴다

이전 분류(2026-09-24)에서 이 페이지는 옛 7번 영역 ‘화물·재고·자산 식별과 추적’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [옛 분류원문]

> 옛 질문: 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [옛 분류원문]

> 옛 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [옛 분류원문]

이전 분류 기준: 원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 2. 핵심 질문

로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]

> 원문 주석: **17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md (요약)

```markdown
# 31. 사람–로봇 협업

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

사람과의 작업 분담, 수동 개입·원격 조작, 주변 사람과의 소통 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람–로봇 작업 분담**: 사람과 로봇이 서로 기다리지 않도록 일을 나누고 작업자의 부담(인체공학)을 고려한다
- **수동 개입·원격 조작**: 운영자가 승인·수동 전환·원격 조작으로 로봇 작업에 개입한다
- **주변 사람과의 소통**: 로봇이 빛·소리·화면으로 의도를 알리고 주변 사람을 안내한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [옛 분류원문]

> 옛 질문: 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [옛 분류원문]

## 2. 핵심 질문

사람과 로봇이 같은 공간에서 서로 기다리거나 방해하지 않게 하려면? [분류원문]
```

### docs/categories/design-and-simulation/scenario-model-and-editing.md (요약)

```markdown
# 33. 시나리오 모델·편집

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md (요약)

```markdown
# 36. 가상 시운전·실제 상황 재현

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실행 전 계획 검증**: 선언한 초기 조건에서 경로·자원·능력을 실제로 실행하지 않고 정적으로 검사한다
- **가상 시운전**: 실제 설치 전에 연동과 운영 정책을 가상 환경에서 시험한다
- **운영 기록 기반 재현**: 실제 운영 기록으로 시뮬레이션의 초기 상태와 사건을 다시 구성한다
- **시뮬레이션–현실 차이 관리**: 시뮬레이션 결과를 현실에 적용할 때 생기는 차이를 측정하고 보정한다
- **디지털 트윈 동기화**: 실시간 상태를 가상 모델에 계속 반영해 현재 상태 표현과 미래 실험을 잇는다

## 2. 핵심 질문

설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md (요약)

```markdown
# 43. 데이터·관측성·배포

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
```

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
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

### runs/2026-10-09-14/research.md

```markdown
# 리서치 브리프 2026-10-09-14

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-14 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- Q. 현장 유형별 적용 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다
- 61. 물류창고 ~ 67. 기타 현장 일곱 세부영역의 게시 사례가 A~P 대분류의 어느 세부영역과 무엇을 주고받는지 대분류 단위로 정리되어 있지 않다
- 현장 유형마다 승강기·문 연동 방식, 수령 확인 방식, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례 유무가 대분류 연결 관점에서 비교되어 있지 않다
- C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, L. AI·학습 기술과 Q. 현장 유형별 적용을 잇는 현장 사례 근거가 약하다

## 조사 질문

1. 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]
2. 61. 물류창고·62. 제조 공장의 게시 사례는 F. 연동(업무 시스템·관제 연동)과 G. 계획·최적화(배정·경로)에 어떤 입력과 제약을 넘기는가?
3. 63. 병원·의료·64. 상업 시설·65. 가정·공동주택의 승강기·문 연동과 수령 확인 사례는 F. 연동의 22. 설비·건물 시스템 연동, E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적, N. 보안·개인정보와 어떻게 이어지는가?
4. 66. 실외의 인증·보도 규정·접근성 사례는 P. 거버넌스·법규·사회와 M. 안전, D. 공간·지도 모델에 어떤 요구를 넘기는가?
5. 67. 기타 현장(점검·건설·농업·오피스·데이터센터)의 사례는 J. 현장 운영·관제, D. 공간·지도 모델, K. 플랫폼 아키텍처·인프라와 어떻게 이어지는가?
6. 현장 유형 전반에서 제조사가 다른 로봇을 하나의 오케스트레이션 계층으로 묶은 공개 사례가 있는가(oq-163, oq-174, oq-176, oq-183)? A. 기획·사업의 2. 사용 사례·요구·책임 범위와 어떻게 이어지는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ F. 연동의 23. 업무 시스템 연동: 국내 스마트물류센터 인증 심사기준은 하차·입고를 입고예정정보 확인·하역작업·상품검수·제품정보 인식·등록으로, 상차·출고를 발주처별 분류·차량입차·상차순서관리·출고정보전달로 나누어, 물류창고 로봇 작업의 시작 조건과 완료 정보가 업무 시스템 단계에 묶여 있다. | ref-919 | 아니오 | medium | 2026-10-09 | 물류창고 / 시작 조건 | 원문 미열람 |
| f2 | [추정] | Q. 현장 유형별 적용의 61. 물류창고 ↔ F. 연동의 20. 로봇·제조사 관제 연동·A. 기획·사업의 1. 기술·시장·업체 동향: 쿠팡 대구 풀필먼트센터가 AGV·소팅봇·무인지게차를 층별로 나눠 투입했고 다중 플릿 오케스트레이션 소프트웨어가 창고 제어 시스템에 비견된다는 시장 정의가 있어, ROP 가 WMS 와 WCS 사이에서 제조사가 다른 로봇에 작업을 배정하는 자리가 이 연결의 중심이 될 것으로 보인다. | ref-257, ref-917, ref-918, ref-919 | 아니오 | low | 2026-10-09 | 물류창고 / 수행 자원 | 원문 미열람 |
| f3 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF·M. 안전의 49. 사람 근접 안전: 쿠팡 대구 풀필먼트센터의 AGV 는 바닥 QR 코드 경로를 따르고 무인지게차는 사람 출입을 막은 구역에서만 주행하며 경계 침범 시 안전 센서로 정지한다. | ref-917, ref-918 | 아니오 | low | 2023-02-07 | 물류창고 / 제약 | 원문 미열람 |
| f4 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Li 외(2020)는 대규모 물류창고의 지속형 다중 에이전트 경로 찾기를, Ma 외(2017)는 온라인 픽업·배송 작업의 지속형 경로 찾기를 다루어, 작업이 계속 들어오는 물류창고 운영이 경로 계획 연구의 대표 적용 대상이다. | ref-005, ref-006 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f5 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 쿠팡 대구 풀필먼트센터의 소팅봇은 포장 라벨 바코드를 읽어 목적지별로 분류·이송하므로, 물류창고 출하 단계의 완료 확인이 작업 대상 식별에 기댄다. | ref-917 | 아니오 | low | 2023-02-07 | 물류창고 / 완료·인계 | 원문 미열람 |
| f6 | [추정] | 연계 대상: Q. 현장 유형별 적용의 61. 물류창고 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: DHL 의 트레일러 하역 로봇은 떨어진 상자의 자동 복구 개선이 향후 목표로 보도되었을 뿐이며, 로봇 자체 복구와 ROP 재계획의 분담은 공개 자료에서 확인되지 않아 두 영역의 경계 과제로 남는 것으로 보인다(oq-166). | ref-921 | 아니오 | low | 2023-02-01 | 물류창고 / 예외·성과 | 원문 미열람 |
| f7 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링: Schrotenboer 외(2019)는 반품 재적치를 고객 주문 피킹 경로에 통합하는 최적화를 다루었으나 피커 기반 창고 연구이며 로봇 피킹 적용은 아니다(oq-165). | ref-912 | 아니오 | medium | 2019-09-01 | 물류창고 / 작업 대상 | 원문 미열람 |
| f8 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ G. 계획·최적화의 24. 작업·워크플로 모델링: Schmid·Limère(2019)는 조립라인 부품을 라인 적재·상자 공급·순서 공급·키팅 같은 공급 정책에 배정하는 조립라인 공급 문제를 분류해, 제조 공장 라인 공급 작업을 나누는 기준을 제공한다. | ref-922 | 아니오 | medium | 2019-02-23 | 제조 공장 / 작업 대상 | 원문 미열람 |
| f9 | [추정] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 21. 상호운용 표준·적합성·20. 로봇·제조사 관제 연동: SYNAOS 는 폭스바겐 하노버 공장에서 MLR 언더라이드 로봇 약 100대와 자율 견인차 40대 등 135대 이상을 제조사 독립 플랫폼이 VDA 5050 으로 관제한다고 설명한다. | ref-924 | 아니오 | low | 2025-10-16 | 제조 공장 / 수행 자원 | 원문 미열람, 벤더 주장 |
| f10 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 23. 업무 시스템 연동: Wally 외(2019)는 ISA-95 모델과 PDDL 로 유연 생산 시스템의 운영 계획을 자동 생성하는 방법을 제안해, 생산 관리 쪽 요청을 실행 계획으로 옮기는 연결의 연구 근거가 된다. | ref-925 | 아니오 | medium | 2019-11-13 | — | 원문 미열람 |
| f11 | [추정] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ F. 연동의 23. 업무 시스템 연동: Siemens 는 자재 관리 시스템이 생산 계획과 칸반에 따라 운송 주문을 자동 생성해 AGV 플릿에 보낸다고 설명한다. | ref-926 | 아니오 | low | 2026-10-09 | 제조 공장 / 시작 조건 | 원문 미열람, 벤더 주장 |
| f12 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계·34. 시뮬레이션·예측용 디지털 트윈: 국내 자동차 공장 연구는 시뮬레이션으로 AGV 대수·단일 차선 양방향 도로의 타당성을 따졌고(2014), 차체 버퍼 창고가 따로 운영될 때의 결품·막힘을 통합창고 모형으로 비교했다(2012). | ref-935, ref-936 | 아니오 | medium | 2014-04 | 제조 공장 / 예외·성과 | 원문 미열람 |
| f13 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업·M. 안전의 49. 사람 근접 안전: 유럽 전문가 31명 조사(2024-12-02)는 좁은 조립 공간에서 협동로봇끼리, 그리고 외골격과의 충돌을 예측·회피하는 것을 핵심 안전·기술 과제로 꼽았다. | ref-928 | 아니오 | medium | 2024-12-02 | 제조 공장 / 제약 | 원문 미열람 |
| f14 | [추정] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 인증 기관 Applus+ 는 ISO 3691-4:2023 이 무인 산업 차량의 사람 감지·제동·속도 제어·운용 구역 분류를 요구한다고 안내하며, 표준 원문은 확인되지 않았다(oq-170). | ref-938 | 아니오 | low | 2026-10-09 | 제조 공장 / 제약 | 원문 미열람, 벤더 주장 |
| f15 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: 국내 제조 현장에서 확인된 자료는 한국전자기술연구원(KETI)의 언어 모델·모방학습 조립공정 자동화 기술 공개(2025-03)와 자연어 지시가 언급되지 않은 정부 'AI 공장장' 사업(2026-09 보도)뿐이다(oq-142). | ref-931, ref-932 | 아니오 | low | 2026-09-07 | 제조 공장 | 원문 미열람 |
| f16 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 22. 설비·건물 시스템 연동·G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: 고려대학교 구로병원 연구는 승강기 제어반에 단 전용 통신 모듈로 로봇의 승강기 호출·탑승을 자동화했고, 승강기 가동률 59% 미만 구간의 성공률이 95.52% 이며 실패가 가동률 90% 초과 구간에 몰렸다고 보고했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | 원문 미열람 |
| f17 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성: 싱가포르 창이종합병원 CHART 의 RoMi-H 는 ROS 2·DDS 기반 오픈소스 미들웨어로 여러 제조사 로봇·센서·병원 정보 시스템을 잇고, 2025-05-01 부터 2년 유효한 등재 프로그램으로 시스템 통합사 5곳이 배치를 맡으며, 로봇들이 승강기를 공유하고 출입 금지 구역으로 충돌을 피한다. | ref-937, ref-872, ref-942 | 아니오 | medium | 2025-05-01 | 병원 / 수행 자원 | 원문 미열람 |
| f18 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·N. 보안·개인정보의 51. 인증·권한·격리: 중국 산시성 인민병원 연구에서 AMR 10대의 약품·검체 이송은 픽업·배송 지점의 RFID 신원 확인으로 완료·인계를 확인했고, 약국·병동·시스템 관리자·장비 관리자의 역할을 정한 협력 책임 체계를 두었다. | ref-929 | 아니오 | medium | 2026-04-24 | 병원 / 완료·인계 | 원문 미열람 |
| f19 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ F. 연동의 20. 로봇·제조사 관제 연동·J. 현장 운영·관제의 37. 관제 화면·실행 기록·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 한림대성심병원은 2024-04 기준 7종 73대 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하고 LG전자와 빅웨이브로보틱스가 배송로봇을 공급하며, 시스템 정착에 약 3년이 걸렸으나 통합관제의 인터페이스·표준은 공개되지 않았다(oq-174). | ref-944, ref-941 | 아니오 | low | 2024-07-15 | 병원 / 수행 자원 | 원문 미열람 |
| f20 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료·64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동·M. 안전의 50. 안전 표준·인증·사고 조사: 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항 KS 제정을 발표했으며, 병원 이송과 호텔 배송 사례가 모두 이 요구 아래 승강기를 쓴다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f21 | [추정] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ M. 안전의 48. 안전·위험 관리·N. 보안·개인정보의 53. 개인정보·영상 데이터: 병원에서 감염 관리 구역·야간 시간대·권한은 ROP 의 경로·배정 제약이 되고, 감염 관리 기준 설정과 이동형 영상정보처리기기 운영 제한 같은 법 판단은 병원 감염관리 조직·법령 쪽 연계 대상으로 남는 것으로 보인다(oq-171, oq-172). | ref-950, ref-929, ref-978 | 아니오 | low | 2026-10-09 | 병원 / 제약 | 원문 미열람 |
| f22 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 국내 병원 로봇 도입의 장애 요인으로 속도·안전성 부족, 대당 억 단위 비용, 경사 구간·문 호환·건물마다 다른 회사의 승강기가 보도되었고, 확인된 국내 지원 제도는 과제 단위의 서비스로봇 실증사업이다. | ref-948, ref-947 | 아니오 | medium | 2025-04-10 | 병원 / 제약 | 원문 미열람 |
| f23 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: 분당서울대병원은 KT 5G 특화망 위의 AMR 6대가 다중 연동된 승강기·자동문을 거쳐 약 300m 연결 터널로 진료재료·약품·린넨 카트를 야간에 옮기게 했다. | ref-939 | 아니오 | low | 2023-07-06 | 병원 / 수행 자원 | 원문 미열람 |
| f24 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화·26. 작업 순서·스케줄링: 다층 호텔 배치 자료(3개 층 67실) 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 총 이동 시간이 거의 두 배가 되었고, 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄었다. | ref-103 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | 원문 미열람 |
| f25 | [추정] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동: 오티스는 자사 클라우드 API(Otis Integrated Dispatch)로 로봇이 승강기를 스스로 호출·탑승·층 선택하며, 오사카 호텔에서 2022-12 부터 24시간 객실 배송을 한다고 설명한다. | ref-957 | 아니오 | low | 2026-10-09 | 상업 시설 / 수행 자원 | 원문 미열람, 벤더 주장 |
| f26 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 22. 설비·건물 시스템 연동: 화성 동탄 상업시설 레이크 꼬모에서는 라이노스의 청소로봇 휠리 J40 이 클라우드 승강기 관리 솔루션 rEMS 로 전 층을 오간다고 보도되었다. | ref-963 | 아니오 | low | 2025-04-02 | 상업 시설 / 수행 자원 | 원문 미열람 |
| f27 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업·32. 예외 복구·재계획·업무 연속성: 일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했다. | ref-961, ref-962 | 아니오 | low | 2019-01 | 상업 시설 / 예외·성과 | 원문 미열람 |
| f28 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ F. 연동의 23. 업무 시스템 연동: Sam's Club 은 약 600개 매장의 자율 바닥 청소기에 재고 스캔 타워를 달아, 로봇이 모은 가격 정확도·재고 수준·진열 위치 정보를 매장 관리자에게 전달하게 했다. | ref-952 | 아니오 | low | 2022-02-01 | 상업 시설 / 완료·인계 | 원문 미열람 |
| f29 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업: 쇼핑몰 안내 로봇 연구(2010)는 소음 속 음성 인식과 예상치 못한 지식 요구 때문에 일부 기능을 원격 조작자가 맡는 반자율 방식을 택했다. | ref-953 | 아니오 | medium | 2010-10 | 상업 시설 / 제약 | 원문 미열람 |
| f30 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 네덜란드 슈퍼마켓 로봇 연구는 영어·네덜란드어와 성별 집단으로 음성 인식 기술을 비교해 Whisper 가 가장 낮은 단어 오류율을 보였다고 보고했다. | ref-868 | 아니오 | medium | 2025-04-29 | 상업 시설 | 원문 미열람 |
| f31 | [사실] | Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 22. 설비·건물 시스템 연동·E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 서울 래미안 리더스원에서는 공동현관 자동문 개폐와 엘리베이터 호출을 연동해 배송로봇이 세대 현관까지 가고, 주문자만 음식을 꺼낼 수 있는 방식으로 넘기며 인증 수단은 공개되지 않았다(oq-184). | ref-966, ref-965, ref-979 | 아니오 | low | 2026-09-20 | 가정 / 완료·인계 | 원문 미열람 |
| f32 | [사실] | Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: 개인정보 보호법 제25조의2 는 이동형 영상정보처리기기의 운영을 제한하며, 개발용 Roomba 가 집 안에서 찍은 이미지가 라벨링 외주를 거쳐 외부에 게시된 사례가 보도되었다(세대 안 적용 여부는 oq-181). | ref-978, ref-968 | 아니오 | medium | 2023-03-14 | 가정 / 제약 | 원문 미열람 |
| f33 | [사실] | Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 21. 상호운용 표준·적합성: Matter 1.2 는 로봇청소기를 기기 유형으로 더해 원격 시작과 진행 알림, 브러시·오류·충전 상태 보고를 가전 연동 표준으로 다룬다. | ref-977 | 아니오 | medium | 2023-10-23 | 가정 / 완료·인계 | 원문 미열람 |
| f34 | [사실] | Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ F. 연동의 23. 업무 시스템 연동·J. 현장 운영·관제의 37. 관제 화면·실행 기록: LH토지주택연구원 자료를 인용한 보도는 택배 차량이 단지 집하처에서 송장번호를 인식시키면 물품 정보가 관제실로 가고, 단지 로봇 택배를 단지 중앙집하·동 단위·구역 단위 분산집하의 세 시나리오로 나눈다고 전한다. | ref-976 | 아니오 | low | 2024-07-18 | 가정 / 시작 조건 | 원문 미열람 |
| f35 | [사실] | Q. 현장 유형별 적용의 66. 실외 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스·M. 안전의 50. 안전 표준·인증·사고 조사: 2023-11-17 개정 지능형로봇법·도로교통법 시행으로 운행안전인증을 받은 실외이동로봇이 보행자 지위를 얻고 운영자의 보험 가입 의무가 생겼으며, 인증은 로봇과 관제장치의 조합에 주어진다. | ref-991, ref-980 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | 원문 미열람 |
| f36 | [추정] | Q. 현장 유형별 적용의 66. 실외 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 운행안전인증이 로봇과 관제장치의 조합을 대상으로 하므로, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지가 연동 설계의 쟁점이 될 것으로 보인다(oq-187). | ref-980 | 아니오 | low | 2026-10-09 | 실외 / 수행 자원 | 원문 미열람 |
| f37 | [사실] | Q. 현장 유형별 적용의 66. 실외 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 피츠버그 대학 캠퍼스에서 Starship 배송로봇이 연석 경사로를 막아 휠체어 이용자가 차도에 갇힌 뒤 대학이 시험 운행을 멈췄고, 회사는 해당 교차로의 지도 오류를 원인으로 들었다. | ref-987 | 아니오 | low | 2019-10-21 | 실외 / 예외·성과 | 원문 미열람 |
| f38 | [사실] | Q. 현장 유형별 적용의 66. 실외 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델·G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Gehrke 외(2023)는 대학 캠퍼스 녹화 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(PET)으로 쟀다. | ref-990 | 아니오 | medium | 2023-03 | 실외 / 제약 | 원문 미열람 |
| f39 | [사실] | Q. 현장 유형별 적용의 66. 실외 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·31. 사람–로봇 협업: Dobrosovestnova 외(RO-MAN 2022)는 눈 속에 갇힌 배송로봇을 행인이 도운 사례를 탐색적으로 연구했다. | ref-993 | 아니오 | medium | 2022 | 실외 / 예외·성과 | 원문 미열람 |
| f40 | [사실] | 연계 대상: Q. 현장 유형별 적용의 66. 실외 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Nav2 문서는 GPS 위치추정으로 실외에서 주행하는 방법을 튜토리얼로 제공하며, 위성 위치 기반 위치추정은 로봇 자체 지능·제어 쪽 기능이다. | ref-988 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f41 | [추정] | Q. 현장 유형별 적용의 66. 실외 ↔ F. 연동의 21. 상호운용 표준·적합성·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 일본(2022년 공포 개정 도로교통법)과 미국 주별 개인 배송 장치(PDD) 법처럼 관할마다 보도 로봇의 크기·속도·신고 기준이 달라, ROP 가 관할 조건을 경로·속도 제약으로 바꿔 담는 공통 표현이 필요할 것으로 보인다(oq-190). | ref-985, ref-986 | 아니오 | low | 2026-10-09 | 실외 / 제약 | 원문 미열람 |
| f42 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·F. 연동의 23. 업무 시스템 연동: Equinor 의 이산화탄소 포집·저장 시설에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지를 하고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다. | ref-995 | 아니오 | low | 2025-11-21 | 기타 / 시작 조건 | 원문 미열람 |
| f43 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기: GS건설은 4족 로봇 스팟이 모은 건설 현장 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다고 밝혔다. | ref-1000 | 아니오 | low | 2020-07-13 | 기타 / 완료·인계 | 원문 미열람 |
| f44 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조·F. 연동의 22. 설비·건물 시스템 연동: 네이버 제2사옥 1784 의 배달 로봇 루키는 클라우드 기반 멀티 로봇 시스템 ARC 가 5G 특화망으로 제어하고 로봇 전용 엘리베이터 로보포트로 층을 오간다. | ref-997 | 아니오 | low | 2023-01-11 | 기타 / 수행 자원 | 원문 미열람 |
| f45 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 농촌진흥청 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다(oq-192). | ref-1007 | 아니오 | low | 2025-04-23 | 기타 / 수행 자원 | 원문 미열람 |
| f46 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 네이버 데이터센터 각 세종에서는 서버 관리 로봇과 운반 로봇이 협력해 서버 자산 흐름을 실시간으로 추적·관리한다고 보도되었다. | ref-1002 | 아니오 | low | 2023-11-08 | 기타 / 작업 대상 | 원문 미열람 |
| f47 | [사실] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ M. 안전의 48. 안전·위험 관리: ISO 18497-3:2024 는 부분 자동·반자율·자율 농업기계의 자율 운용 구역을 다루어, 농업 현장 로봇의 운용 구역이 ROP 의 운행 제약 입력이 된다. | ref-1009 | 아니오 | medium | 2024 | 기타 / 제약 | 원문 미열람 |
| f48 | [추정] | Q. 현장 유형별 적용의 67. 기타 현장 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 싱가포르 창이 공항에서 Open-RMF 가 청소 로봇 운영에 쓰인다는 기사가 있으나, 제조사가 다른 로봇을 한 계층에서 묶은 기타 현장의 공개 사례로 확인할 수준은 아닌 것으로 보인다. | ref-1004 | 아니오 | low | 2025-10-29 | 기타 | 원문 미열람 |
| f49 | [사실] | Q. 현장 유형별 적용의 63. 병원·의료 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: 에스토니아 타르투 대학병원 현장 시험은 Open-RMF 교통 편집기로 평면도를 주석하고 로봇 격자 지도를 정합해 중환자실에서 검사실로 혈액 검체를 운반했으며, 작은 구역으로 나눠 매핑한 뒤 합치는 편이 더 정확했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 작업 대상 | 원문 미열람 |
| f50 | [사실] | Q. 현장 유형별 적용의 61. 물류창고 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: EU ILIAD 프로젝트는 학습한 사람 흐름에 맞춰 물류창고 자율 지게차의 경로를 계획했다. | ref-1180 | 아니오 | medium | 2021-06 | 물류창고 / 제약 | 원문 미열람 |
| f51 | [추정] | Q. 현장 유형별 적용 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 게시된 61. 물류창고 ~ 67. 기타 현장 페이지가 확인한 국내 사례는 한 운영사가 설비별로 로봇을 들이거나 건설사·물류사 한 곳과 로봇 업체 한 곳이 짝을 이루거나 한 기관이 만든 로봇을 자체 계층으로 묶은 형태이며, 제조사가 다른 로봇을 하나의 오케스트레이션 계층으로 묶은 국내 공개 사례는 지금까지 확인되지 않은 것으로 보인다. | ref-917, ref-944, ref-966, ref-997, ref-1007 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2005.07371 | 예 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/1705.10868 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-257 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 미확인 | 업계 보고서 | medium | 2026-10-09 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 예 |
| ref-868 | Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI | Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents | 2025-04-29 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/ | 예 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | 정부·연구기관 | medium | 2026-10-09 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 예 |
| ref-912 | Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J. | Integration of returns and decomposition of customer orders in e-commerce warehouses | 2019-09-01 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/1909.01794 | 예 |
| ref-917 | 로봇신문 (장길수) | 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이... | 2023-02-07 | 기사 | low | 2026-10-09 | https://www.irobotnews.com/news/articleView.html?idxno=30736 | 예 |
| ref-918 | 물류신문 (석한글) | ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니 | 2023-02-07 | 기사 | low | 2026-10-09 | https://www.klnews.co.kr/news/articleView.html?idxno=306994 | 예 |
| ref-919 | 스마트물류시설인증센터 (한국교통연구원) | 인증스마트물류센터 : 인증심사 > 심사기준 > 일반 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://cslc.koti.re.kr/new_sub2/new_sub2_2_1 | 예 |
| ref-921 | Robotics 24/7 (Eugene Demaitre) | DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers | 2023-02-01 | 기사 | low | 2026-10-09 | https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers | 예 |
| ref-922 | Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)) | A classification of tactical assembly line feeding problems | 2019-02-23 | 논문 | medium | 2026-10-09 | https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957 | 예 |
| ref-924 | SYNAOS (IoT Use Case) | VDA 5050: unified AGV fleet control in real time at VW | 2025-10-16 | 벤더 문서 | low | 2026-10-09 | https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control | 예 |
| ref-925 | Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M. | Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL | 2019-11-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/1911.05481 | 예 |
| ref-926 | Siemens | AGV fleet management integration with intralogistics | 미확인 | 벤더 문서 | low | 2026-10-09 | https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/ | 예 |
| ref-928 | Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI) | Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors | 2024-12-02 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full | 예 |
| ref-929 | Li, M. 외 (Scientific Reports) | Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios | 2026-04-24 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13276296/ | 예 |
| ref-931 | 뉴시스 | "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다 | 2026-09-07 | 기사 | low | 2026-10-09 | https://www.newsis.com/view/NISX20260907_0003779780 | 예 |
| ref-932 | 테크데일리 | KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개 | 2025-03-12 | 기사 | low | 2026-10-09 | https://www.techdaily.co.kr/news/articleView.html?idxno=25352 | 예 |
| ref-935 | 강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce) | 시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례 | 2014-04 | 논문 | medium | 2026-10-09 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280 | 예 |
| ref-936 | 옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2)) | 자동차 생산을 위한 통합창고 연구 | 2012 | 논문 | medium | 2026-10-09 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601 | 예 |
| ref-937 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | ROMI-H \| Changi General Hospital | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.cgh.com.sg/chart/projects/romi-h | 예 |
| ref-938 | Applus+ Laboratories | ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs) | 미확인 | 벤더 문서 | low | 2026-10-09 | https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs | 예 |
| ref-939 | 이데일리 | 분당서울대병원, 무거운 이송카트 로봇자율배송, 무안경 3D 의료실습에 도입 | 2023-07-06 | 기사 | low | 2026-10-09 | https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01403846635671896 | 예 |
| ref-941 | 데일리팜 | 원내 약 배송로봇 도입 확대...정부 지원에 변화 바람 | 2024-07-15 | 기사 | low | 2026-10-09 | https://m.dailypharm.com/user/news/15128 | 예 |
| ref-942 | Open Robotics | ROMI-H: Bringing Robot Traffic Control to Healthcare | 2021-02-10 | 오픈소스 문서 | medium | 2026-10-09 | https://www.openrobotics.org/blog/2021/2/10/romi-h-bringing-robot-traffic-control-to-healthcare | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 예 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-10-09 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 예 |
| ref-947 | 한국로봇산업진흥원 | 서비스로봇 실증사업 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/bizsupt/portalBsuptRoCreIntro.do | 예 |
| ref-948 | 비즈한국 | 병원에 늘어나는 '로봇', 의사·간호사도 편해졌을까 | 2025-04-10 | 기사 | low | 2026-10-09 | https://bizhankook.com/articles/29394.html | 예 |
| ref-950 | 한국보건산업진흥원 스마트병원 확산지원센터 | 선도모델 및 모듈 소개 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.khidi.or.kr/board?menuId=MENU03336&siteId=SITE00040 | 예 |
| ref-952 | Retail Dive (Sam Silverstein) | Sam's Club rolls out inventory-checking robots chainwide | 2022-02-01 | 기사 | low | 2026-10-09 | https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/ | 예 |
| ref-953 | Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)) | A Communication Robot in a Shopping Mall | 2010-10 | 논문 | medium | 2026-10-09 | https://ieeexplore.ieee.org/abstract/document/5557825 | 예 |
| ref-957 | Otis Elevator Company | Elevators and service robots | 미확인 | 벤더 문서 | low | 2026-10-09 | https://www.otis.com/en/us/innovation/elevators-and-service-robots | 예 |
| ref-961 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 미확인 | 기사 | low | 2026-10-09 | https://incidentdatabase.ai/cite/346/ | 예 |
| ref-962 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 2019-01 | 기사 | low | 2026-10-09 | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ | 예 |
| ref-963 | 서울경제 (백주연) | 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장 | 2025-04-02 | 기사 | low | 2026-10-09 | https://www.sedaily.com/article/14048085 | 예 |
| ref-965 | 삼성물산 뉴스룸 | 삼성물산, 아파트 세대 현관까지 음식배달로봇 확장 운영 | 2026-01-15 | 벤더 문서 | low | 2026-10-09 | https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EA%B1%B4%EC%84%A4%EB%B6%80%EB%AC%B8/2026-01-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%84%B8%EB%8C%80-%ED%98%84%EA%B4%80%EA%B9%8C%EC%A7%80-%EC%9D%8C%EC%8B%9D%EB%B0%B0%EB%8B%AC%EB%A1%9C%EB%B4%87-%ED%99%95%EC%9E%A5/ | 예 |
| ref-966 | 지디넷코리아 (신영빈) | 로봇이 문앞까지 택배 가져다 주는 미래 곧 온다 | 2025-01-19 | 기사 | low | 2026-10-09 | https://zdnet.co.kr/view/?no=20250119062609 | 예 |
| ref-968 | MIT Technology Review (Eileen Guo) | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 2022-12-19 | 기사 | low | 2026-10-09 | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ | 예 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 2024-07-18 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=123976 | 예 |
| ref-977 | Connectivity Standards Alliance (CSA) | Matter 1.2 Arrives with Nine New Device Types & Improvements Across the Board | 2023-10-23 | 표준 | medium | 2026-10-09 | https://csa-iot.org/newsroom/matter-1-2-arrives-with-nine-new-device-types-improvements-across-the-board/ | 예 |
| ref-978 | CaseNote (법령 게재; 원 제정 국회·개인정보보호위원회 소관) | 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) | 2023-03-14 | 정부·연구기관 | medium | 2026-10-09 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C25%EC%A1%B0%EC%9D%982 | 예 |
| ref-979 | 미디어펜 (조태민) | 로봇이 다닐 길부터 짓는다…건설사, ‘로봇 친화 설계’ 속도 | 2026-09-20 | 기사 | low | 2026-10-09 | https://www.mediapen.com/news/view/1124680 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-985 | 内閣府 (일본 내각부) | 令和5年版交通安全白書 トピック 改正道路交通法（令和4年公布）について | 2023 | 정부·연구기관 | medium | 2026-10-09 | https://www8.cao.go.jp/koutu//taisaku/r05kou_haku/zenbun/genkyo/topics/topic_1.html | 예 |
| ref-986 | Supply Chain Dive | Why delivery robots face a regulatory ‘nightmare’ | 2023-04-26 | 기사 | low | 2026-10-09 | https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/ | 예 |
| ref-987 | The Pitt News | Pitt pauses testing of Starship robots due to safety concerns | 2019-10-21 | 기사 | low | 2026-10-09 | https://pittnews.com/article/151679/news/pitt-pauses-testing-of-starship-robots-due-to-safety-concerns/ | 예 |
| ref-988 | Open Navigation (Nav2) | Navigating Using GPS Localization — Nav2 documentation | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://docs.nav2.org/jazzy/tutorials/general_tutorials/navigation2_with_gps/navigation2_with_gps/ | 예 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03 | 논문 | medium | 2026-10-09 | https://doi.org/10.1016/j.trip.2023.100789 | 예 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 예 |
| ref-993 | Dobrosovestnova, A., Schwaninger, I., & Weiss, A. (IEEE RO-MAN 2022) | With a Little Help of Humans. An Exploratory Study of Delivery Robots Stuck in Snow | 2022 | 논문 | medium | 2026-10-09 | https://ieeexplore.ieee.org/abstract/document/9900588/ | 예 |
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones | 2025-11-21 | 기사 | low | 2026-10-09 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 예 |
| ref-997 | 이코노미스트 (송재민) | 로봇이 로봇들을 움직이는, 네이버 1784 | 2023-01-11 | 기사 | low | 2026-10-09 | https://economist.co.kr/article/view/ecn202301110006 | 예 |
| ref-1000 | 인더스트리뉴스 (정형우) | GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입하기로 | 2020-07-13 | 기사 | low | 2026-10-09 | https://www.industrynews.co.kr/news/articleView.html?idxno=38911 | 예 |
| ref-1002 | 아주경제 (윤선훈) | 아시아 최대 규모 데이터센터…네이버 '각 세종' 본격 가동 | 2023-11-08 | 기사 | low | 2026-10-09 | https://www.ajunews.com/view/20231107091520837 | 예 |
| ref-1004 | The Robot Report | Singapore's National Robotics Programme reveals initiatives to advance robot adoption | 2025-10-29 | 기사 | low | 2026-10-09 | https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/ | 예 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 | 2025-04-23 | 기사 | low | 2026-10-09 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 예 |
| ref-1009 | ISO | ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones | 2024 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/82687.html | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-10-09 | https://iliad-project.eu/concluding-iliad/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/index.md | 5. 다른 대분류와의 연결 | 대분류 연결(category_link): '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 묶음 제안 — A. 기획·사업: f2·f22·f51 / C. 채팅 기반 구성·운영: f15·f30 / D. 공간·지도 모델: f37·f40·f43·f49 / E. 사물·사람·실시간 상태: f5·f18·f31·f38·f46·f50 / F. 연동: f1·f9·f10·f11·f16·f17·f19·f20·f25·f26·f28·f33·f34·f36·f41·f45·f48 / G. 계획·최적화: f3·f4·f7·f8·f24 / H. 실행·협업·예외 복구: f6·f13·f27·f29·f39 / I. 설계·시뮬레이션: f12 / J. 현장 운영·관제: f19·f34·f42 / K. 플랫폼 아키텍처·인프라: f23·f44 / L. AI·학습 기술: f15 / M. 안전: f3·f14·f21·f35·f47 / N. 보안·개인정보: f18·f21·f32 / O. 검증·도입·수명주기: f19·f49 / P. 거버넌스·법규·사회: f35·f37·f41. 벤더 주장(f9·f11·f14·f25)은 '벤더 주장' 병기, 연계 대상(f6·f40)은 짧게. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않는다(f12 는 가정한 미래 실험 쪽). 모든 현장에 공통인 기능은 A~P 에 두고 이 절은 현장 사례가 넘기는 요구만 적는다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사람-대-상품 | Person-to-Goods (PTG) | 작업자가 선반·보관 위치까지 걸어가 물품을 집는 피킹 방식으로, 설비·로봇이 선반을 작업자에게 가져오는 상품-대-사람 방식과 대비된다. |
| 도어 투 도어 로봇 배송 | Door-to-Door Robot Delivery | 공동주택 단지 입구에서 공동현관·승강기 연동을 거쳐 세대 현관 앞까지 로봇이 물품을 나르는 배송 방식이다. |

## 열린 질문

새로 생긴 질문:

- 병원·호텔·쇼핑몰·공동주택에서 로봇의 승강기 연동이 승강기 제조사 API, 승강기 관리 솔루션, 로봇팔 버튼 조작, 제어반 전용 통신 모듈로 갈리는데, 이 방식들을 한 현장에서 같은 승강기 인터페이스로 묶어 제조사가 다른 로봇이 함께 쓰게 한 사례나 방식별 비교 자료가 있는가? | 관련 영역: 22. 설비·건물 시스템 연동, 63. 병원·의료, 64. 상업 시설, 65. 가정·공동주택 | 근거: f16 | 종류: 일반
- 병원·오피스처럼 5G 특화망으로 로봇을 연결하거나 클라우드에서 제어하는 현장에서 통신이 끊길 때 로봇의 현장 동작과 진행 중 작업의 재배정 기준을 공개한 사례가 있는가? | 관련 영역: 42. 분산 시스템·통신·컴퓨팅 구조, 63. 병원·의료, 67. 기타 현장 | 근거: f44 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 62 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - 직전 반환값(1회차 브리프)이 입력에 포함되지 않아 그 브리프의 신규 출처(예약 구간 ref-1539~)와 finding 을 확인할 수 없었다
    - f3·f5 쿠팡 사례 두 보도는 같은 현장 공개 행사 기반이라 독립 교차 확인 아님
    - f16 구로병원 전체 성공률 분모(oq-215) 미확인
    - f19 한림대성심병원 통합관제의 인터페이스·표준(oq-174) 미확인
    - f21 병원 감염 관리 구역 규칙(oq-172)과 영상 촬영 법 적용(oq-171) 미확인
    - f31 공동주택 배송로봇 수령 인증 수단(oq-184) 미확인
    - f36 이종 제조사 계층의 운행안전인증상 관제장치 해당 여부(oq-187) 미확인
    - f9·f11·f14·f25 벤더 주장은 독립 확인 없음
- 범위 경계 위반 의심:
    - f6: 떨어진 상자 복구는 로봇 자체 지능·제어 경계라 claim 을 '연계 대상: '으로 시작하고 ROP 쪽은 재계획 분담만 다룸
    - f40: GPS 위치추정은 로봇 자체 지능·제어 경계라 '연계 대상: '으로 표시
    - f16·f20·f25·f26: 승강기 운행·호출 제어 자체는 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 예약·상태 확인·제약 반영으로 한정해야 함
    - f21·f32·f35·f41: 법 적용·인증 판단은 운영자·법무·인증 기관 쪽 연계 대상
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f17 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고쳤다. 다만 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었으므로, 입력으로 받은 게시 페이지(61. 물류창고 ~ 67. 기타 현장, A~G 대분류 연결 절)의 검증된 주장과 각주(기존 참고문헌 재사용)만으로 브리프를 다시 구성했다. 새 f17 은 RoMi-H 연결로 근거가 정부·연구기관·오픈소스 출처뿐이다. 벤더 문서만 근거로 한 finding(f9·f11·f14·f25)은 모두 tag 추정·vendor_claim true·evidence_excerpt 첫머리 '벤더 주장: '으로 냈고, [사실] finding 가운데 벤더 문서만 근거로 한 것은 없다(f31 은 기사 2건과 함께 인용). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1539~ref-1568 은 쓰지 않았다. 이번 실행에서 원문을 열지 않았으므로 모든 출처를 fetched false·source_unopened true 로 표시했고 신뢰도는 medium 이하다. 교차 확인 0건. 현장 유형: 물류창고(f1~f7·f50), 제조 공장(f8~f15), 병원(f16~f23·f49), 상업 시설(f24~f30), 가정(f31~f34), 실외(f35~f41), 기타(f42~f48)를 고르게 다뤘다. 34. 시뮬레이션·예측용 디지털 트윈(f12, 가정한 미래 실험)과 18. 실시간 세계 상태·데이터 일관성을 섞지 않았다. L. AI·학습 기술 연결 근거는 f15 하나뿐이다. 해결 제안한 열린 질문 없음. 입력 누락 없음. 우선 지정 질문·정정 요청 없음.
```

### runs/2026-10-09-13/research.md

```markdown
# 리서치 브리프 2026-10-09-13

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-13 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 33. 시나리오 모델·편집 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 사례 없음('찾지 못했다'로 남음), 국내 자료 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다'는 문장이 근거 없이 남아 있음(oq-234)
- 섹션 6·7. 대표 접근법·관련 오픈소스 — 시설 주석 편집기를 traffic-editor 로만 서술. Open-RMF 의 후속 편집기(Site Editor) 전환이 반영되지 않음(바뀐 출처)
- 섹션 6·8 — 로봇 쪽 시나리오 기술 언어(OpenSCENARIO 2 DSL 재사용), 시나리오 변형·인스턴스 해석·출처 추적 연구 없음
- 섹션 11. 열린 질문 — oq-131·oq-233·oq-234·oq-235·oq-236 해결 근거 미조사
- 섹션 3. 왜 중요한가 — 실무자 면담 같은 직접 근거 없이 종합 추정만 있음
- 정정 요청 없음, 발행 2년이 지난 표준·수치 없음(Arena-Bench 2022 는 논문이라 재확인 대상 아님)

## 조사 질문

1. 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]
2. oq-234 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? (섹션 9 문장 정정 겨냥)
3. oq-235 장애·긴급 요청을 시각·발생 조건으로 선언하는 방식을 여러 제조사 로봇과 설비 장애까지 일반화한 시나리오 형식이 있는가? (섹션 6·11 겨냥)
4. oq-131 실행 기록이나 사고 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식·방법이 있는가? (섹션 6·11 겨냥)
5. 물류창고 현장의 시나리오 예제·벤치마크·편집 도구는 무엇이 있으며(oq-236 국내 예제 라이브러리 포함) 무엇을 담는가? (섹션 5 겨냥)
6. oq-233 시설 주석 편집기와 건물 형식(Open-RMF traffic-editor·.building.yaml)은 이후 어떻게 바뀌었고, 로봇 쪽에서 기존 시나리오 형식(OpenSCENARIO 등)을 조합해 쓰는 사례가 있는가? (섹션 6·7·9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ASAM OpenSCENARIO XML 1.4.0 문서의 하위 호환성 절은 판 사이 호환 여부를 판마다 선언한다: 1.4.0 은 1.3.1 과, 1.3.1 은 1.3.0 과 완전히 호환되고, 1.2.0 은 1.1.1·1.0.0 과 호환되지만, 1.3.0 은 의미상 잘못된 시나리오를 허용하던 스키마 오류를 고쳐 1.2.0 과 완전히 호환되지 않는다. | ref-1511 | 아니오 | medium | 2026-10-09 | — | — |
| f2 | [사실] | ASAM OpenSCENARIO XML 은 1.2.0 시나리오 파일을 1.3.0 으로 옮기는 XSLT 이전 스크립트를 제공하고 스크립트가 경고를 내면 원래부터 잘못된 시나리오이므로 사람이 고치게 하며, 모든 판에 폐기 요소를 뺀 엄격 스키마를 두어 폐기 요소를 찾아 바꾸게 한다. | ref-1511 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [추정] | 확인한 도로 교통 시나리오 표준에는 개별 시나리오 파일을 형식 판 사이에서 옮기는 규칙(판별 호환 선언, 이전 스크립트, 엄격 스키마 검사)이 공개되어 있으므로, 33. 시나리오 모델·편집 페이지 9절의 '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다'는 서술은 도로 교통 분야에 한해 고쳐야 하며 로봇 시뮬레이션 형식의 같은 규칙은 여전히 확인하지 못했다. | ref-1511, ref-1088 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [사실] | Ortega·Wiest·Pasch·Hochgeschwender(arXiv 2605.29973, ERAS 2026 채택)가 확장한 시험 틀 RoboVAST 는 환경을 FloorPlan 모델(.fpm), 과제를 OpenSCENARIO DSL 의 추상 시나리오, 시작·목표 자세·장애물 수·센서 잡음·설정 파일을 변형 파일(.vast)로 나누고, 각 인스턴스를 모든 값이 정해진 구체 시험 구성(scenario.config)으로 해석한 뒤 실행마다 해석된 매개변수·rosbag·시각·합격 여부·결정적 실행 식별자를 남긴다. | ref-1515 | 아니오 | medium | 2026-05-29 | — | — |
| f5 | [사실] | 같은 연구는 시험 산출물 사이의 관계를 W3C PROV(PROV-O)를 핵심 메타모델로 DCAT·Dublin Core·QUDT 와 함께 JSON-LD 로 기록해 SPARQL 로 질의하게 했으며, 저자들은 이 메타모델이 일반화하기 어려울 수 있고 로봇 분야 공동 어휘가 없다고 한계를 밝혔다. | ref-1515 | 아니오 | medium | 2026-05-29 | — | — |
| f6 | [추정] | RoboVAST 처럼 환경 모델·추상 시나리오·변형을 나누고 인스턴스를 구체 구성으로 해석해 출처 기록과 함께 남기는 방식은, 형식 판 이전 규칙과 별개로 개별 시나리오 인스턴스를 식별·재현하는 근거가 되어 oq-234 에 부분 답이 될 것으로 보이나, 단일 로봇 주행 시험 기준이라 다중 플릿·설비 시나리오에 맞는지는 확인하지 못했다. | ref-1515 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [사실] | Pasch·Mirus·Zhang·Scholl(Intel Labs, arXiv 2409.07080)의 Scenario Execution for Robotics 는 ASAM OpenSCENARIO 2 로 쓴 로봇 시나리오를 구문 분석해 행동 트리(PyTrees)로 바꿔 실행하는 백엔드·미들웨어 독립 파이썬 라이브러리이며, Gazebo·Nav2·PyBullet 라이브러리를 두고 매개변수 값 목록을 조합마다 하나의 실행 시나리오로 펼친다. | ref-1512 | 아니오 | medium | 2024-09-11 | — | — |
| f8 | [사실] | Scenario Execution for Robotics 의 저자들은 시뮬레이션과 실물 실험에서 위치 데이터만 바꾼 같은 시나리오 파일을 썼다고 보고했다. | ref-1512 | 아니오 | medium | 2024-09-11 | — | — |
| f9 | [사실] | 같은 연구는 2D 라이다 스캔에 가우시안 잡음을 더하거나 검출을 무작위로 빼는 ROS 2 노드로 장애를 주입하고 잡음 크기와 누락 비율을 시나리오 매개변수로 두었으며, 장애 수준이 높아질수록 AMCL 위치추정 오차가 커지는 것을 기능 시연으로 보였다. | ref-1512 | 아니오 | medium | 2024-09-11 | — | — |
| f10 | [추정] | 자율주행 분야의 시나리오 기술 언어 OpenSCENARIO 2 가 이동로봇 주행 시나리오 기술(Scenario Execution for Robotics, RoboVAST)에 다시 쓰이고 있으므로, 이 영역 9절에서 연계 대상으로만 둔 도로 교통 시나리오 표준이 로봇 시나리오의 과제·사건 기술 언어 후보가 될 수 있어 oq-233 의 '기존 형식 조합' 쪽에 부분 근거가 될 것으로 보인다. | ref-1512, ref-1515, ref-1088 | 아니오 | low | 2026-10-09 | — | — |
| f11 | [사실] | ros2_fault_injection 은 ROS 2 의 토픽·변환(TF)·서비스에 장애를 주입하는 프레임워크로, 오도메트리·LaserScan·관절 상태·IMU·TF·속도 명령·트리거 서비스·점군 장애 유형과 시나리오 실행 중 기대 결과를 확인하는 단언(assertion)을 두고 pluginlib 로 새 주입기를 더하게 한다. | ref-1518 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [추정] | 확인한 장애 주입 선언은 ARIAC 의 설비·도구 장애(시작 시각·지속 시간·발생 횟수 매개변수), Scenario Execution 의 센서 잡음 매개변수, ros2_fault_injection 의 메시지 단위 장애로 나뉘며, 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애를 한 형식으로 선언하는 사례는 이번에도 찾지 못해 oq-235 는 열린 채로 남는 것으로 보인다. | ref-528, ref-1512, ref-1518 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f13 | [사실] | Ortega·Parra·Schneider·Hochgeschwender(Frontiers in Robotics and AI, 2024-08)는 도메인 전문가 14명 면담에서 환경 모델과 로봇 과제를 묶은 시험 시나리오의 변형 관리가 이동로봇 시뮬레이션 시험을 꺼리는 주요 장벽으로 나타났다고 보고했다. | ref-1516 | 아니오 | medium | 2024-08-02 | — | — |
| f14 | [사실] | 같은 연구는 기존 모델을 고치지 않고 동적 문·다른 과제 명세 같은 의미를 덧붙이는 조합형 실행 시나리오를 제안해 점유 격자 지도·3D 메시·Gazebo 월드·주행 경유점을 생성했고, 정적 시험·무작위로 움직이는 문·로봇이 다가오면 닫히는 문의 세 시나리오로 공개 주행 스택에서 1년 넘게 드러나지 않은 설정 오류를 찾았다. | ref-1516 | 아니오 | medium | 2024-08-02 | 예외·성과 | — |
| f15 | [사실] | Open-RMF 의 Site Editor(rmf_site)는 Rust 와 Bevy 게임 엔진으로 만든 대규모 RMF 배치 현장 시각화·편집 도구로 데스크톱과 웹(WebAssembly)에서 돌며, rmf_site_ros2 의 rmf_site_cmake 가 Site Editor 프로젝트에서 시뮬레이션과 주행 그래프를 생성한다. | ref-482 | 아니오 | medium | 2026-10-09 | — | — |
| f16 | [사실] | Open-RMF 상호운용 그룹 공지(2024-06-05)는 Site Editor 를 예전 traffic-editor 를 대체하는 도구로 소개하고, 시각화·시뮬레이션용 3D 환경, 환경 안의 로봇, 로봇 교통 규칙, 승강기와 문을 편집 대상으로 들었다. | ref-1510 | 아니오 | medium | 2024-06-05 | — | — |
| f17 | [사실] | traffic-editor 문서는 편집기의 목표를 여러 플릿의 의도를 제조사 중립 방식으로 표현하고 실제 환경을 반영한 3D 시뮬레이션 월드를 생성하는 것으로 밝히면서, 다음 판은 영상 좌표 대신 데카르트 좌표나 위경도 좌표를 기본으로 하려 하나 일정은 정해지지 않았다고 적는다. | ref-079 | 아니오 | medium | 2026-10-09 | — | — |
| f18 | [추정] | Open-RMF 의 시설 주석 편집기가 traffic-editor(.building.yaml)에서 Site Editor 로 넘어가고 있으므로, ROP 시나리오 모델이 건물 파일을 환경 참조로 묶는다면 편집기·건물 형식 전환에 따른 참조 이전 규칙이 함께 필요할 것으로 보이며, 기존 .building.yaml 을 Site Editor 형식으로 옮기는 공식 방법은 이번에 확인하지 못했다. | ref-482, ref-1510, ref-079 | 아니오 | low | 2026-10-09 | — | — |
| f19 | [사실] | Jiang·Zhang·Veerapaneni·Li(SoCS 2024)에 따르면 Amazon Robotics 가 후원한 2023 League of Robot Runners 지속형 다중 에이전트 경로 찾기 경진대회는 Warehouse(140×500, 정점 38,586개, 에이전트 8,000)와 Sortation(140×500, 정점 54,320개, 에이전트 10,000) 지도를 포함한 시나리오로 단계당 1초 계획 제한 아래 처리량을 겨뤘으며, 이는 실제 물류창고 배치가 아니라 경진대회 벤치마크다. | ref-1514 | 아니오 | medium | 2024-04-24 | 물류창고 / 작업 대상 | — |
| f20 | [사실] | 같은 경진대회에서는 외부 작업 배정기가 에이전트가 현재 목표에 도달할 때마다 새 목표를 정확히 하나씩 주는 방식으로 작업이 생긴다. | ref-1514 | 아니오 | medium | 2024-04-24 | 물류창고 / 시작 조건 | — |
| f21 | [추정] | NVIDIA 는 Isaac Sim 의 Warehouse Creator 확장이 2D 격자 배치를 Modular Warehouse 자산 묶음의 USD 창고로 바꾸는 대화형 배치 편집기이며 바닥·벽·기둥 같은 건물 구조만 생성한다고 설명한다. | ref-1517 | 아니오 | low | 2026-09-18 | 물류창고 | 벤더 주장 |
| f22 | [사실] | Elmaaroufi 외의 ScenicNL(COLM 2024)은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮어, 세부가 불확실한 경찰 사고 보고서(최근 5년 캘리포니아 자율주행차 사고 보고)를 불확실성을 확률 분포로 담은 Scenic 시나리오 프로그램으로 바꿔 '만약 ~였다면' 시나리오를 탐색하게 했다. | ref-1513 | 아니오 | medium | 2024-10-02 | — | — |
| f23 | [추정] | 사고 기록 같은 서술형 기록을 확률적 시나리오 프로그램으로 바꾸는 방법은 도로 교통 분야에 있으나, 로봇 플릿의 실행 기록(작업·배정·위치·사건 시각)을 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙은 이번 조사에서도 찾지 못해 oq-131 은 열린 채로 남는 것으로 보인다. | ref-1513, ref-1086 | 아니오 | low | 2026-10-09 | — | — |
| f24 | [사실] | 레온 대학교 연구진(WAF 2025)은 공개 지리공간 데이터로 3D 시나리오를 만들어 주요 로봇 플랫폼에서 쓸 수 있는 시뮬레이션 모델을 생성하고 Gazebo·Unity 의 ROS 2 시스템과 연동하는 방법을 제안했다. | ref-1519 | 아니오 | medium | 2025 | — | — |
| f25 | [추정] | 이번에 확인한 자료를 더하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 로봇 쪽에서도 환경 모델·추상 시나리오·변형을 나누고 구체 인스턴스를 해석·기록하는 도구와 자율주행 시나리오 언어의 재사용이 나타나지만, 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 여전히 확인하지 못한 것으로 보인다. | ref-1515, ref-1512, ref-1516, ref-116 | 아니오 | low | 2026-10-09 | — | — |
| f26 | [추정] | 연계 대상: OpenSCENARIO XML 의 판 이전 스크립트나 Open-RMF 편집기 전환 같은 외부 시나리오·건물 형식의 판 규칙은 각 형식 관리 주체의 몫이며, ROP 는 자기 시나리오 모델의 판 규칙과 참조하는 외부 형식 판의 대응을 맡을 것으로 보인다. | ref-1511, ref-482 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | medium | 2026-10-09 | https://www.asam.net/standards/detail/openscenario-xml/ | 예 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2307.03325 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-482 | Open-RMF (open-rmf/rmf_site) | rmf_site — RMF Site Editor (README) | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_site | 아니오 |
| ref-1510 | Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey) | Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor | 2024-06-05 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070 | 아니오 |
| ref-1511 | ASAM e.V. | ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility | 미확인 | 표준 | high | 2026-10-09 | https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html | 아니오 |
| ref-1512 | Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs, arXiv) | Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests | 2024-09-11 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2409.07080 | 아니오 |
| ref-1513 | Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv) | ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports | 2024-05-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2405.03709 | 아니오 |
| ref-1514 | Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv) | Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities | 2024-04-24 | 논문 | high | 2026-10-09 | https://arxiv.org/abs/2404.16162 | 아니오 |
| ref-1515 | Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택) | Replicable Simulation-Based Robot Validation through Provenance | 2026-05-28 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2605.29973 | 아니오 |
| ref-1516 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11) | Composable and executable scenarios for simulation-based testing of mobile robots | 2024-08-02 | 논문 | high | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/ | 아니오 |
| ref-1517 | NVIDIA | Isaac Sim Documentation — Warehouse Creator Extension | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://docs.isaacsim.omniverse.nvidia.com/latest/assets/asset_utilities/ext_omni_warehouse_creator.html | 아니오 |
| ref-1518 | ros2_fault_injection 프로젝트 (Read the Docs) | ros2_fault_injection documentation | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://ros2-fault-injection.readthedocs.io/ | 아니오 |
| ref-1519 | Sánchez de la Fuente, S., Prieto López, L., González Santamarta, M. Á., Matellán Olivera, V. 외 (Universidad de León, WAF 2025) | Scenario Generation for Robot Simulation from Public Data | 2025 | 논문 | medium | 2026-10-09 | https://portalcientifico.unileon.es/documentos/6972798ce66b2902147b1aeb | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | 3, 5, 6, 7, 8, 9, 10, 11 | 갱신(차등): 섹션 3 — f13(전문가 면담 근거)으로 종합 추정 보강 / 섹션 5 — 물류창고 사례 추가: f19(Warehouse·Sortation 지도, 작업 대상)·f20(목표 배정, 시작 조건), 경진대회 벤치마크이지 실제 현장이 아님을 밝힘. f21 은 편집 도구로 [추정]+'벤더 주장' 병기. '물류창고 사례를 찾지 못했다' 문장 교체, 국내 자료는 여전히 없음 / 섹션 6·7 — f15·f16·f17·f18(traffic-editor→Site Editor 전환, 바뀐 출처), f7·f8·f9(OpenSCENARIO 2 를 쓰는 로봇 시나리오 실행 라이브러리), f11(ros2_fault_injection), f4·f5(RoboVAST), f24(공개 데이터 기반 생성). 6·7절 본문은 주제 페이지로 분리되어 있으므로 요약 문장과 주제 페이지 갱신을 함께 제안 / 섹션 8 — f13·f14·f22·f4 대표 연구 추가 / 섹션 9 — '개별 시나리오 인스턴스 버전 관리 방식을 찾지 못했다' 문장을 f1·f2·f3(도로 교통 표준의 판 이전 규칙)·f6(인스턴스 해석·출처 기록)로 정정하고 f26(연계 대상: 외부 형식 판 규칙) 추가, f10 으로 OpenSCENARIO 를 '참조 설계'만이 아니라 로봇 시나리오 기술 후보로도 서술 / 섹션 10 — 54. 시험·형식 검증·벤치마크(f4·f9·f14), 57. 자산·소프트웨어 수명주기 관리(f1·f2·f6), 61. 물류창고(f19·f20), 27. 다중 로봇 경로·교통 관리 — MAPF(f19), 11. 채팅으로 실제 상황 시뮬레이션 재현·36. 가상 시운전·실제 상황 재현(f22·f23) 연결 추가, related_areas 에 57·61 추가 제안 / 섹션 11 — oq-234 부분 근거(f3·f6), oq-235 미해결(f12), oq-131 미해결(f23), oq-233 부분 근거(f10·f18), oq-236 미해결(국내 자료 없음), 새 질문 3건. 다음 실행 후보: docs/topics/2026/2026-09-30-area33-s7.md 표에 Site Editor·Scenario Execution·RoboVAST·ros2_fault_injection·League of Robot Runners 행 추가. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 데이터 출처 추적 | Data Provenance (W3C PROV) | 어떤 산출물이 어떤 입력·설정·실행·주체로부터 만들어졌는지를 기계가 읽을 수 있는 관계로 기록하는 일로, W3C PROV 가 그 표준 데이터 모델이며 시뮬레이션 시험의 재현성 확보에 쓰인다. |
| 추상 시나리오·구체 시나리오 | Abstract Scenario / Concrete Scenario | 매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다. |
| 엄격 스키마 | Strict Schema (deprecated elements removed) | 형식의 판에서 폐기 예정 요소를 뺀 검증용 스키마로, 기존 시나리오 파일을 이 스키마로 검사해 다음 판에서 사라질 요소를 찾아 바꾸게 한다(ASAM OpenSCENARIO XML). |

## 열린 질문

새로 생긴 질문:

- RoboVAST 처럼 추상 시나리오를 구체 인스턴스로 해석하고 실행마다 출처를 기록하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비가 함께 있는 다중 로봇 시나리오에 적용한 사례가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 54. 시험·형식 검증·벤치마크 | 근거: f6 | 종류: 일반
- Open-RMF Site Editor 의 현장 형식이 기존 traffic-editor 의 .building.yaml 을 대체하는가, 그리고 기존 건물 파일을 옮기는 공식 변환 도구나 판 이전 규칙이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 15. 지도·공간·위치 모델 | 근거: f18 | 종류: 일반
- OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가? | 관련 영역: 33. 시나리오 모델·편집, 22. 설비·건물 시스템 연동 | 근거: f10 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 11건
- 미확인 항목:
    - oq-234 부분 답: 도로 교통 표준(OpenSCENARIO XML)의 판 이전 규칙과 RoboVAST 인스턴스 해석은 확인했으나, 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 시나리오 판 이전 규칙은 확인하지 못함. SDFormat 변환 규칙 파일(1_10.convert)은 열었으나 내용이 비어 근거로 쓰지 않음
    - oq-235 미해결: 여러 제조사 플릿과 설비 장애를 함께 선언하는 형식 없음
    - oq-131 미해결: 로봇 플릿 실행 기록을 시나리오로 바꾸는 공개 형식 없음(자율주행 쪽 MathWorks Scenario Builder·특허는 벤더·특허 자료라 근거로 쓰지 않음)
    - oq-236 미해결: 국내 다중 로봇 시나리오 예제 라이브러리를 찾지 못함(한국어 검색 4회)
    - oq-135 이번 실행에서 조사하지 못함
    - f19·f20 League of Robot Runners 공식 사이트·2024 대회 자료는 열지 않고 우승 팀 논문 기준
    - ref-1518 관리 주체·판·발행일 미확인
    - ref-1511 문서 절의 발행일 미확인(1.4.0 판 공개일은 이전 실행에서 2026-05-19 로 확인됨)
    - f21 Isaac Sim Warehouse Creator 기능은 벤더 문서뿐이며 독립 확인하지 못함
    - Scenario Execution 공식 저장소 README 는 403/404 로 열지 못해 논문 본문으로 대신함
    - f10 의 두 출처는 공동 저자가 겹쳐 독립 출처가 아님
- 범위 경계 위반 의심:
    - f9·f11·f12: 센서·메시지 장애 주입과 위치추정 성능은 로봇 자체 지능·제어 경계의 내용이라, 시나리오에 장애를 선언하는 방식의 근거로만 씀
    - f21: 3D 창고 건물 자산 생성은 시뮬레이터·벤더 쪽 연계 대상이며 시나리오 환경 참조의 사례로만 제안
    - f22·f23: 도로 교통 사고 보고 기반 생성은 자율주행 분야 내용이라 로봇 플릿 재현의 참고 사례로만 씀
    - f26: 외부 형식 판 규칙은 형식 관리 주체 몫이므로 claim 을 '연계 대상: '으로 시작
- 한계: web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청·발행 2년 지난 표준이 없어 빈·약한 절(5절 물류창고·국내 사례, 9절 판 관리 문장, 6·7절 편집기 전환)과 열린 질문 oq-131·oq-233·oq-234·oq-235·oq-236 만 조사했다. 검색 19회/30, 신규 출처 11건/15(ref-482~ref-1519, 예약 구간 안), 모두 원문 페이지를 열었다(webfetch 10, github_raw 1). 재사용 5건 가운데 ref-079·ref-528 은 입력의 원문 텍스트(inbox)로 확인했고 ref-1088·ref-1086·ref-116 은 다시 열지 않았다(source_unopened). 교차 확인 0건: 새 근거가 모두 단일 출처라 신뢰도는 medium 이하다. 벤더 주장 1건(f21). 핵심 질문 답은 f25(추정)로 갱신했다. 현장 유형: 이번 새 사례는 물류창고(f19·f20 경진대회 벤치마크, f21 편집 도구)뿐이며 실제 물류창고 배치 사례와 국내 자료는 여전히 찾지 못했다. 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 18. 실시간 세계 상태·데이터 일관성(현재 상태)을 섞지 않았고, 시나리오는 가정한 미래 실험의 입력으로만 다뤘다. 해결 제안한 열린 질문 없음(oq-234 는 부분 근거). 답한 트랙 질문 없음(트랙 실행 아님). 입력 누락 없음. 우선 지정 질문 없음.
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
| f2 | [사실] | Open-RMF 의 rmf-web 은 사용자가 Open-RMF 배치 전체를 시각화하고 제어하는 웹 인터페이스 묶음으로 API 서버·API 클라이언트·대시보드 프레임워크로 이루어지며, 기본 설정의 API 서버는 비영속 내부 데이터베이스를 쓰므로 실행 기록을 남기려면 영속 저장소를 따로 설정해야 한다. | ref-302 | 아니오 | medium | 2026-09-30 | — | — |
| f3 | [사실] | Open-RMF API 메시지의 작업 상태(task_state) 스키마는 작업 상태를 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 12개 값으로 표현하고, 처음 추정 소요 시간과 현재 추정 소요 시간, 배정 로봇, 완료·진행·대기 단계 목록, 일시정지(interruptions)·취소·강제 종료 요청 정보를 함께 담는다. | ref-111 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f4 | [사실] | Open-RMF API 메시지의 작업 로그(task_log) 스키마는 로그를 작업 수준·단계(phase) 수준·사건(event) 수준으로 계층화하고, 각 로그 항목(log_entry)은 단조 증가하는 순번(seq), 중요도 tier(uninitialized·info·warning·error), 밀리초 단위 유닉스 시각, 본문 텍스트를 필수로 가진다. | ref-1168, ref-1169 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 명세는 차량의 위치와 계획 경로를 시각화 시스템에 높은 빈도로 보내는 visualization 토픽을 주문 확인·오류·운용 상태를 담는 state 토픽과 분리해 두며, state 메시지는 사건이 생길 때 또는 최소 30초 간격으로 보내게 한다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | MCAP 은 임의 직렬화 형식의 타임스탬프 발행·구독 메시지를 기록하는 모듈형 컨테이너 형식으로, 스키마·채널·메시지·청크 레코드와 메시지 색인·청크 색인·요약 레코드를 두어 시각 기준 임의 접근(탐색)을 지원하고 첨부·메타데이터 레코드를 함께 담을 수 있다. | ref-1171 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [추정] | Foxglove 문서는 기록 재생 기능으로 시간축 막대 탐색, 재생 속도 조절, 재생 구간 자르기, 사건(event) 주석의 생성·검색, 반복 재생을 제공하고, 임의 시점으로 이동할 때 구독 토픽마다 가장 최근 메시지를 불러와(lookback) 모든 패널이 같은 시점 상태를 보이게 한다고 설명한다. | ref-1172 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f8 | [사실] | Kottinger·Almagor·Lahijanian(ICAPS 2022)은 다중 에이전트 경로 계획을 사람이 눈으로 검증할 수 있도록 에이전트 궤적이 서로 겹치지 않는 시간 구간별 이미지 몇 장으로 설명하는 방식을 채택하고, 이 설명 가능한 MAPF 가 환경 크기에 대해 NP-난해임을 보인 뒤 CBS 에 설명 가능성 제약을 더한 XG-CBS 를 제안해 계획 시간과 설명 가능성의 절충을 분석했다. | ref-1173 | 아니오 | medium | 2022-02 | — | — |
| f9 | [사실] | Chen 외(Theoretical Issues in Ergonomics Science, 2018)는 지능형 에이전트와 함께 일하는 운영자의 임무 환경 상황 인식을 돕기 위한 상황 인식 기반 에이전트 투명성(SAT) 모델을 Autonomous Squad Member·IMPACT 두 시스템의 사람 참여 시뮬레이션 실험에 적용했고, 에이전트가 더 투명해질수록 운영자의 작업 수행이 일관되게 나아졌다고 보고했다. | ref-477 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f10 | [사실] | Roldán 외(Sensors, 2017-07)는 드론 2대·지상 로봇 1대의 화재 감시·진압 임무 8개를 운영자 24명이 감독하는 실험에서 기존·예측형 기존·가상현실·예측형 가상현실 인터페이스를 비교해, 가상현실 인터페이스가 상황 인식(SAGAT)을 높이고 작업 부하(NASA-TLX)를 낮췄으나 예측 요소의 효과는 유의하지 않았고 오히려 부하를 늘렸다고 보고했으며, 다중 로봇 인터페이스 요건으로 정보량 줄이기, 관련 정보로 주의 유도, 로봇 위치·건강·상태·측정값을 같은 화면에 통합하기, 지도 활용을 들었다. | ref-1175 | 아니오 | medium | 2017-07-27 | — | — |
| f11 | [사실] | ISA 는 공정 자동화 시스템의 인간–기계 인터페이스(HMI) 표준으로 ISA-101.01-2015 와 기술 보고서 TR101.01-2022(HMI 철학)·TR101.02-2019(HMI 사용성과 성능)를 두며, ISA-101.01 은 설계·구현·운영·지속 개선에 이르는 HMI 수명주기를 다루고 연속·배치·이산 산업 모두에 적용된다고 밝힌다. | ref-1176 | 아니오 | medium | 2026-09-30 | — | — |
| f12 | [추정] | 현대자동차그룹 로보틱스랩은 통합 관제 시스템 나콘(NARCHON)을 다수 이기종 로봇의 실시간 모니터링, BPMN 2.0 기반 워크플로·시나리오 관리, 이상 탐지·보고가 있는 실시간 대시보드, 승강기·자동문·보안 게이트 연동과 층간 이동을 지원하는 시스템으로 소개하며 적용처로 건물·상업 시설을 든다. | ref-1177 | 아니오 | low | 2026-09-30 | 상업 시설 / 수행 자원 | 벤더 주장 |
| f13 | [추정] | 네이버클라우드의 ARC brain 사용 가이드는 서비스 기능으로 여러 제조사 로봇의 제어와 충돌 방지, 로봇 실시간 상태 모니터링과 알림, 실시간 태스크와 운영 이력 조회, 제3자 로봇 등록, 승강기·자동문 연동, 맵 에디터 기반 동선 설정, 로봇 상태 기반 알림 설정을 든다. | ref-1178 | 아니오 | low | 2026-09-17 | — | 벤더 주장 |
| f14 | [사실] | 아주경제(2025-04-07) 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다. | ref-1179 | 아니오 | low | 2025-04-07 | 병원 / 완료·인계 | — |
| f15 | [추정] | 확인한 자료를 종합하면 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에 대해, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만(f1·f3·f4·f5), '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이고(f8·f9·f10) 실제 다중 제조사 플릿 관제 화면에서 효과를 측정한 공개 자료는 찾지 못했다. | ref-1165, ref-111, ref-1168, ref-031, ref-1173, ref-477, ref-1175 | 아니오 | low | 2026-09-30 | — | — |
| f16 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇을 감독하는 운영자는 정보량이 많을수록 상황 인식과 작업 부하가 나빠지고(f10), 에이전트의 판단이 투명할수록 운영자 수행이 나아지며(f9), 공정 산업 HMI 표준이 화면을 수명주기 전체에 걸쳐 관리할 대상으로 보고(f11), 병원처럼 배송 이력을 남겨야 하는 현장에서는 실행 기록이 인계 확인의 근거가 되기 때문이다(f14). | ref-1175, ref-477, ref-1176, ref-1179 | 아니오 | low | 2026-09-30 | — | — |
| f17 | [추정] | 확인한 자료를 종합하면 37. 관제 화면·실행 기록에서 ROP가 직접 맡을 범위는 여러 제조사 플릿과 승강기·문 같은 설비 상태를 하나의 층별 지도에 겹쳐 보여 주는 통합 화면(f1·f12·f13), 제조사마다 다른 상태를 공통 작업 상태 값·단계·수준별 로그로 정규화한 실행 기록(f3·f4), 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색(f2·f6·f7), 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시(f8·f9)다. | ref-1165, ref-1177, ref-1178, ref-111, ref-1168, ref-302, ref-1171, ref-1172, ref-1173, ref-477 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록)과 로컬 회피 시각화는 로봇 제조사에, 승강기·자동문·CCTV 같은 시설 설비의 자체 관제 화면은 시설·설비 쪽에 속하므로, ROP 는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태와 설비 상태를 받아 통합 표시·기록하는 인터페이스를 맡을 것으로 보인다. | ref-031, ref-1171, ref-1165 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 이 영역은 알림·이상 탐지의 38. 모니터링·이상 탐지·원인 분석(f4·f12·f13), 작업 시각 기록을 지표로 쓰는 39. 운영 성과 측정·개선(f3), 층별 지도의 15. 지도·공간·위치 모델(f1), 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f5), 기록 재생의 36. 가상 시운전·실제 상황 재현과 11. 채팅으로 실제 상황 시뮬레이션 재현(f6·f7, oq-131), 경로 설명의 27. 다중 로봇 경로·교통 관리 — MAPF(f8), 투명성의 13. 대화형 기능의 신뢰·기반·31. 사람–로봇 협업(f9·f10), 상태 메시지의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f5), 문·승강기 표시의 22. 설비·건물 시스템 연동(f1), 기록 저장의 43. 데이터·관측성·배포(f2·f6), 배송 이력의 17. 작업 대상·자산 식별과 인계 추적(f14), 적용 현장인 63. 병원·의료(f14)·64. 상업 시설(f12)과 이어진다. | ref-1165, ref-302, ref-111, ref-1168, ref-031, ref-1171, ref-1172, ref-1173, ref-477, ref-1175, ref-1177, ref-1178, ref-1179 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1165 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_visualization | 아니오 |
| ref-302 | Open Robotics (open-rmf/rmf-web) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-111 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-1168 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json | 아니오 |
| ref-1169 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 아니오 |
| ref-031 | VDA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0) | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1171 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://mcap.dev/spec | 아니오 |
| ref-1172 | Foxglove | Playback — Foxglove Documentation | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://docs.foxglove.dev/docs/visualization/playback | 아니오 |
| ref-1173 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 2022-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2202.09930 | 아니오 |
| ref-477 | Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 2018 | 논문 | medium | 2026-09-30 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 예 |
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
    - f9 SAT 모델 논문(ref-477): 출판사·DTIC·ADS 페이지가 403/405 로 열리지 않아 검색 결과 요약 범위로만 서술했고, SAT 세 수준의 정의는 출처 귀속이 불분명해 넣지 않음(용어집의 기존 SAT 항목 참조)
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
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 출처 상한에 도달해 ISO 11064, RCLL 객체 중심 이벤트 로그, 물류창고·제조 공장 관제 화면 사례를 더 넣지 못했다. 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건이고 전체 목록 id 를 받지 못함. VDA 5050·MCAP 이 기존 목록에 같은 URL 로 있으면 퍼블리셔가 합친다). 원문 열람: 14건 열었고(github_raw 6건, webfetch 8건) SAT 논문(ref-477)만 열지 못해 source_unopened 로 표시했다. 논문은 Roldán 외(PMC 본문) 외에 Kottinger 외는 초록만 봤다. 교차 확인 0건: 핵심 내용이 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더 문서 기능 주장(f7·f12·f13)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에는 f15 로 답했고 결론은 '무엇을 보여 주는 요소는 공개 구현·표준에 있으나 왜를 보여 주는 설명 표시는 실험실 연구 수준이며 현장 평가 자료를 찾지 못했다'는 추정이다. 현장 유형 사례는 병원(f14, 협약 단계)·상업 시설(f12, 벤더 주장)뿐이며 물류창고·제조 공장·가정·실외는 찾지 못했다. 국내 자료는 현대차 로보틱스랩(ref-1177)·네이버클라우드(ref-1178)·아주경제(ref-1179) 3건이다. oq-131 은 근거를 찾지 못해 해결 제안하지 않았다. 용어집에 이미 있는 백 파일·MCAP·상황 인식 기반 에이전트 투명성·감사 추적·관측성·오픈 RMF·VDA 5050 은 후보로 내지 않았다. 페이지 제안은 대상 영역 갱신 1건이고 36·38번 반영은 다음 실행 후보로 적었다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### data/source_texts/ref-111.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
  "title": "Task State",
  "description": "The state of a task",
  "type": "object",
  "properties": {
    "booking": { "$ref": "#/$defs/booking" },
    "category": { "$ref": "#/$defs/category" },
    "detail": { "$ref": "#/$defs/detail" },
    "unix_millis_start_time": { "type": "integer" },
    "unix_millis_finish_time": { "type": "integer" },
    "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "assigned_to": {
      "description": "Which agent (robot) is the task assigned to",
      "type": "object",
      "properties": {
        "group": { "type": "string" },
        "name": { "type": "string" }
      },
      "required": ["group", "name"]
    },
    "status": { "$ref": "#/$defs/status" },
    "dispatch": { "$ref": "#/$defs/dispatch" },
    "phases": {
      "description": "A dictionary of the states of the phases of the task. The keys (property names) are phase IDs, which are integers.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/phase" }
    },
    "completed": {
      "description": "An array of the IDs of completed phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "active": {
      "description": "The ID of the active phase for this task",
      "$ref": "#/$defs/id"
    },
    "pending": {
      "description": "An array of the pending phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "interruptions": {
      "description": "A dictionary of interruptions that have been applied to this task. The keys (property names) are the unique token of the interruption request.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/interruption" }
    },
    "cancellation": {
      "description": "If the task was cancelled, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the cancel request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "killed": {
      "description": "If the task was killed, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the kill request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  },
  "required": ["booking"],
  "$defs": {
    "phase": {
      "description": "Information about a phase",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "category": { "$ref": "#/$defs/category" },
        "detail": { "$ref": "#/$defs/detail" },
        "unix_millis_start_time": { "type": "integer" },
        "unix_millis_finish_time": { "type": "integer" },
        "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "final_event_id": { "$ref": "#/$defs/id" },
        "events": {
          "description": "A dictionary of events for this phase. The keys (property names) are the event IDs, which are integers.",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/event_state" }
        },
        "skip_requests": {
          "description": "Information about any skip requests that have been received",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/skip_phase_request" }
        }
      },
      "required": ["id"]
    },
    "booking": {
      "description": "Information about how a task was booked",
      "type": "object",
      "properties": {
        "id": {
          "description": "The unique identifier for this task",
          "type": "string"
        },
        "unix_millis_earliest_start_time": { "type": "integer" },
        "unix_millis_request_time": { "type": "integer" },
        "priority": {
          "description": "Priority information about this task",
          "anyOf": [
            { "type": "object" },
            { "type": "string" }
          ]
        },
        "labels": {
          "description": "Information about how and why this task was booked, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "requester": {
          "description": "(Optional) An identifier for the entity that requested this task",
          "type": "string"
        }
      },
      "required": ["id"]
    },
    "id": {
      "type": "integer",
      "minimum": 0
    },
    "category": {
      "description": "The category of this task or phase",
      "type": "string"
    },
    "detail": {
      "description": "Detailed information about a task, phase, or event",
      "anyOf": [
        { "type": "object" },
        { "type": "array" },
        { "type": "string" }
      ]
    },
    "estimate_millis": {
      "description": "An estimate, in milliseconds, of how long the subject will take to complete",
      "type": "integer",
      "minimum": 0
    },
    "event_state": {
      "description": "The current state of an event",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "status": { "$ref": "#/$defs/status"},
        "name": {
          "description": "The brief name of the event",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the event",
          "$ref": "#/$defs/detail"
        },
        "deps": {
          "description": "This event may depend on other events. This array contains the IDs of those other event dependencies.",
          "type": "array",
          "items": {
            "description": "The IDs of events that this event depends on. Event IDs are isolated within the scope of this task phase.",
            "type": "integer",
            "minimum": 0
          }
        }
      },
      "required": ["id"]
    },
    "status": {
      "description": "A simple token representing how the task is proceeding",
      "type": "string",
      "enum": ["uninitialized", "blocked", "error", "failed", "queued", "standby", "underway", "delayed", "skipped", "canceled", "killed", "completed"]
    },
    "dispatch": {
      "description": "Information about how this task is being dispatched",
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": ["queued", "selected", "dispatched", "failed_to_assign", "canceled_in_flight"]
        },
        "assignment": {
          "type": "object",
          "properties": {
            "fleet_name": { "type": "string" },
            "expected_robot_name": { "type": "string" }
          }
        },
        "errors": {
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["status"]
    },
    "interruption": {
      "description": "Task interruption information",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the interruption request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the interruption, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "resumed_by": {
          "description": "Information about the resume request that ended this interruption. This field will be missing if the interruption is still active.",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the resume request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the resume request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_resume_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "skip_phase_request": {
      "description": "Information about a request to skip a phase",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the skip request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the skip request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
          "type": "array",
          "items": { "type": "string" }
        },
        "undo": {
          "description": "Information about an undo skip request that applied to this request",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the undo skip request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the undo skip request, items can be a single value like `dashboard` or a key-value pair like `app=dashboard`, in the case of a single value, it will be interpreted as a key-value pair with an empty string value.",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_request_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  }
}
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
…(발췌: 전체 207,642자 중 앞 106,899자)
````
