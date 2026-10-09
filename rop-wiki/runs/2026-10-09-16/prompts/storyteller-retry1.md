(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-16
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 38. 모니터링·이상 탐지·원인 분석 (J. 현장 운영·관제)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-09-16/target.json

```json
{
  "run_id": "2026-10-09-16",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 149,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 38,
    "area_name": "38. 모니터링·이상 탐지·원인 분석",
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
  "selection_rationale": "CLI 지정 run_type=update, area=38"
}
```

### runs/2026-10-09-16/research.json

```json
{
  "run_id": "2026-10-09-16",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 38,
    "area_name": "38. 모니터링·이상 탐지·원인 분석",
    "category": "J. 현장 운영·관제"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — 보고 어휘를 '같은 시간축에 맞춘다'고만 적었고, 표준마다 시각 형식·심각도 등급·연결 상태 표현이 어떻게 다른지에 대한 근거가 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) — 개정 전에 쓴 물류창고 가상 시나리오 1건뿐이고 병원·상업 시설·실외·기타 현장 사례가 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 운용 모드·information 사용 제한·연결 상태(HIBERNATING), MassRobotics 오류 코드 형식, Open-RMF 배차 오류·개입 기록이 정리되지 않음(주제 페이지로 분리된 절)",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 로봇 내부 진단(ROS 2 diagnostics)과 플랫폼 수준 원인 판정의 경계 근거가 README 수준 한 줄뿐",
    "섹션 11. 열린 질문 — oq-033·oq-073·oq-074·oq-075·oq-210 에 대한 부분 근거 미정리",
    "정정 요청 없음. 바뀐 출처 확인 대상은 입력으로 들어온 원문 텍스트(ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447)"
  ],
  "research_questions": [
    "지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]",
    "oq-033·oq-073 VDA 5050·MassRobotics·Open-RMF 는 오류 심각도·작업 상태·운용 상태를 각각 어떤 값과 형식으로 보고하며, 공통 어휘로 옮길 때 무엇이 어긋나는가? (섹션 3·7·11 겨냥)",
    "통신 원인을 로봇·설비 원인과 구분하는 데 쓸 수 있는 표준 신호(연결 상태, 메시지 순번, 마지막 유언 메시지)는 무엇인가? (섹션 3·7 겨냥)",
    "oq-210 플랫폼 서비스의 분산 추적과 로봇 상태 메시지를 하나의 작업 식별자로 이을 수 있는 표준 필드는 무엇인가? (섹션 6·7·11 겨냥)",
    "로봇 내부 진단(센서·드라이버)과 플랫폼 수준 원인 판정의 경계는 어디인가? (섹션 9 겨냥)",
    "oq-074·oq-075 병원·상업 시설·실외·기타 현장에서 로봇 정지·지연·실패의 원인이나 이상 감시 방식이 공개된 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 state 스키마는 로봇의 활성 오류 전체를 담는 errors 배열, 운용 모드(operatingMode), 안전 상태(safetyState)를 필수 항목으로 두고, 운용 모드 값을 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 가지로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema required 목록에 errors·operatingMode·safetyState 포함. errors 설명: 모든 활성 오류를 목록에 넣고 빈 배열은 활성 오류 없음. operatingMode enum 7개. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 state 스키마는 로봇이 보내는 부가 정보 배열(information)을 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정하므로, 원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "information 설명: \"This should only be used for visualization or debugging – it must not be used for logic in fleet control.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 은 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고 오류마다 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 담을 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 명세의 오류 객체: errorLevel 네 단계, errorDescription·errorHint, 언어 코드별 번역 가능. 이번 실행에서 원문을 다시 열지 않음 (재인용: 2026-10-09-15)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f4",
      "claim": "VDA 5050 connection 스키마는 연결 상태를 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 으로 나누어, 로봇이 질서 있게 끊으면 OFFLINE 을, 예기치 않게 끊기면 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리고, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-449"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "connection.schema: 유언 메시지는 retain 플래그로 보내고 CONNECTION_BROKEN 으로 설정. 정상 종료·수면 시 OFFLINE 발행. HIBERNATING 은 연결은 활성이나 state 메시지를 보내지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "MassRobotics AMR 상호운용 표준의 statusReport 는 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 두고, 오류는 심각도 필드 없이 문자열 목록(errorCodes)으로만 보고하며 정상 운용 때는 생략하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "statusReport.operationalState enum 9개. errorCodes: type array, items string, uniqueItems, 설명 'should be omitted for normal operation'. 심각도 필드는 스키마에 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f6",
      "claim": "Open-RMF 작업 상태 스키마는 작업 상태 12개(blocked·error·failed·delayed 등)와 별도로 배차 상태(failed_to_assign 포함)와 배차 오류 배열을 두고, 일시정지(interruptions)·재개(resumed_by)·취소·강제 종료 요청마다 요청 시각과 라벨을 남겨, 지연이 배정 실패인지 실행 중 차단인지 사람 개입인지를 기록에서 나눠 볼 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_state.json: status enum 12개, dispatch.status 에 failed_to_assign·canceled_in_flight, dispatch.errors 배열, interruption 의 unix_millis_request_time·labels·resumed_by. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 경보 메시지(Alert)는 심각도를 INFO·WARNING·ERROR 세 등급으로 두고 운영자 응답 목록(responses_available), 관련 작업 id, 화면 표시 여부를 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-448"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Alert.msg: tier TIER_INFO=0·TIER_WARNING=1·TIER_ERROR=2, responses_available, alert_parameters, task_id(작업이 없으면 비움), display 기본 true. 페이지 5절 서술이 오늘 기준 원문과 같다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "오늘 기준 Open-RMF 문 모드 메시지는 여전히 closed·moving·open·offline·unknown 다섯 값이고, 문 어댑터는 문 노드에 직접 보낸 요청을 무효로 돌려 진행 중 로봇 작업을 방해하지 않게 하는 상태 감독자 역할을 하므로, 페이지 5절의 문 관련 서술은 그대로 유효하다.",
      "tag": "사실",
      "source_ids": [
        "ref-313",
        "ref-283"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DoorMode.msg: MODE_CLOSED~MODE_UNKNOWN 5개. Doors 장: 문 노드는 /door_states 발행, 어댑터를 거치지 않은 직접 요청은 어댑터가 이전 상태로 되돌린다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "오류 심각도 표현이 VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록으로 서로 달라, 38. 모니터링·이상 탐지·원인 분석에서 이종 플릿의 이상을 한 경보 체계로 모으려면 ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다(oq-033·oq-073 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-448",
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세 원문의 심각도 필드를 대조한 도출. 세 규약 어디에도 다른 규약과의 대응표는 없음.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f10",
      "claim": "연계 대상: ROS 2 diagnostics 는 하드웨어 드라이버·로봇 하드웨어의 진단 정보를 /diagnostics 토픽으로 모아 aggregator 로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘기는 로봇 내부 진단 체계이므로, ROP 는 이 결과를 원인 범주 판정의 입력으로 받는 쪽에 선다.",
      "tag": "사실",
      "source_ids": [
        "ref-445"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 진단 시스템은 하드웨어 드라이버·로봇 하드웨어 정보를 사용자·운영자에게 제공. diagnostic_aggregator, diagnostic_remote_logging(예: influxdb 전달) 패키지. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "OpenTelemetry 명세는 분산 추적을 하나의 논리적 동작에서 비롯된 사건들을 프로세스·네트워크 경계를 넘어 모은 것으로 정의하고, 16바이트 TraceId 로 여러 프로세스의 span 을 묶으며, 일괄 처리처럼 여러 요청에서 시작된 작업은 span 간 링크(Links)로 잇게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-447"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Overview: TraceId 는 16 무작위 바이트로 모든 프로세스의 span 을 묶음. Links 는 단일 Trace 안이나 서로 다른 Trace 사이의 인과 관련 span 을 가리킴. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Open-RMF 작업 예약 id(booking.id)와 VDA 5050 state 의 orderId 가 각각 작업·주문을 식별하므로, ROP 서비스의 추적 TraceId 와 이 식별자들을 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이어 원인 분석에 쓸 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다(oq-210 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-447",
        "ref-111",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "task_state.json booking.id(작업 고유 식별자), state.schema orderId(현재 또는 직전 주문 식별), OpenTelemetry TraceId 를 대조한 도출.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "VDA 5050 의 headerId 는 토픽마다 보낸 메시지마다 1씩 늘어나므로 수신 쪽에서 번호가 건너뛰면 메시지 유실을 의심할 수 있고, 연결 상태(CONNECTION_BROKEN·HIBERNATING)와 함께 보면 상태 보고가 끊긴 원인이 통신인지 로봇 쪽 의도된 감축인지 가르는 근거가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-051",
        "ref-449"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "headerId 설명: 토픽마다 정의되고 보낸(반드시 수신되지는 않은) 메시지마다 1 증가. connection.schema 의 연결 상태 4값과 결합한 도출. 결번 판정 기준은 명세에 없음.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "세 규약의 시각 표현은 VDA 5050 이 ISO 8601 문자열(밀리초까지), MassRobotics 가 date-time 문자열, Open-RMF 작업 상태가 밀리초 유닉스 시각 정수로 서로 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-051",
        "ref-230",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema timestamp: ISO8601(YYYY-MM-DDTHH:mm:ss.fffZ). statusReport timestamp: format date-time. task_state.json: unix_millis_start_time 등 integer. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "VDA 5050 운용 모드의 INTERVENED·MANUAL, MassRobotics 의 manualOverride·waitingHumanEvent, Open-RMF 작업의 일시정지 라벨이 모두 사람 개입을 표시하므로, 지연 원인 범주에 로봇·설비·통신·앞 작업 외에 사람 개입·대기를 따로 두는 편이 판정에 유리할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-051",
        "ref-230",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "operatingMode enum 의 INTERVENED·MANUAL, operationalState 의 manualOverride·waitingHumanEvent, task_state interruptions.labels(예: dashboard)를 대조한 도출.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "고려대학교 구로병원 연구에서 의약품 배송 로봇의 승강기 호출·탑승은 승강기 가동률 59% 미만 구간에서 성공률 95.52% 였고 실패가 가동률 90% 초과 구간에 몰려, 병원 현장의 로봇 지연·실패 원인으로 설비(승강기) 혼잡이 드러났다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Digital Health 게재 연구: 제어반 전용 통신 모듈로 호출·탑승 자동화, 가동률 구간별 성공률 보고. 전체 성공률 분모는 미확인 (재인용: 2026-10-09-14)",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "한림대학교성심병원은 2024-04 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하지만, 이상 탐지·원인 분석 방식이나 원인별 장애 통계는 공개되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-944"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "로봇신문 보도: 커맨드센터 통합관제로 7종 73대 운영. 관제 화면 항목·장애 통계 언급 없음 (재인용: 2026-10-09-14)",
      "as_of": "2024-04-15",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "Equinor 의 이산화탄소 포집·저장 시설에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지로 설비 이상을 찾고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-995"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Offshore Technology 기사: 점검 로봇의 계기 판독·밸브 확인·누출 탐지, 운영자의 임무 직접 생성 (재인용: 2026-10-09-14)",
      "as_of": "2025-11-21",
      "site_type": "기타",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "국내 실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 하므로, 실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국로봇산업진흥원 운행안전인증 안내: 인증 대상이 로봇과 관제장치 조합. 관제장치 항목의 세부 요건은 미확인 (재인용: 2026-10-09-14)",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했고, 호텔은 로봇 일부를 철수했다.",
      "tag": "사실",
      "source_ids": [
        "ref-961",
        "ref-962"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "AI Incident Database 346 과 Hotel Technology News: 로봇이 단순 업무를 처리하지 못해 직원 개입, 로봇 인력 절반 철수 (재인용: 2026-10-09-14)",
      "as_of": "2019-01",
      "site_type": "상업 시설",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "이번에 확인한 병원·상업 시설·기타 현장 사례는 실패·지연 현상이나 통합관제 운영만 보고하고 원인을 로봇·설비·통신·앞 작업으로 나눈 분류나 원인별 발생 비율은 공개하지 않아, oq-074·oq-075 는 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-943",
        "ref-944",
        "ref-961"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f16·f17·f20 의 출처를 대조한 도출. 원인별 통계는 어느 출처에도 없음.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 로봇 상태 메시지 스키마. 필수 항목(errors·operatingMode·safetyState), 운용 모드 값, information 사용 제한, headerId 규칙을 확인했다(입력 원문 텍스트는 앞 13,220자 발췌).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-449",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/connection.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 연결 상태 메시지 스키마. ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 과 유언 메시지 규칙.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. VDA 5050 3.0.0 명세 본문. 오류 수준 네 단계와 오류 설명·조치 힌트 항목(이전 실행 2026-10-09-15 확인 내용 재인용).",
      "source_unopened": false,
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마. identityReport·statusReport, 운용 상태 9값, 문자열 오류 코드 목록.",
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
      "summary": "Open-RMF 작업 상태 스키마. 작업 상태 12값, 배차 상태·오류, 일시정지·재개·취소 기록, 예약 식별자.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-448",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_task_msgs/msg/Alert.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 경보 메시지 정의. 심각도 세 등급, 응답 목록, 관련 작업 id.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-313",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 자동문 모드 메시지. closed·moving·open·offline·unknown 다섯 값.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 문 연동 장. 문 노드·문 어댑터(상태 감독자)의 역할과 토픽.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-445",
      "org": "ROS (ros/diagnostics GitHub)",
      "title": "diagnostics — README (ros2 branch)",
      "published": null,
      "url": "https://github.com/ros/diagnostics/blob/ros2/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ROS 2 진단 시스템 README. /diagnostics 토픽, aggregator, 원격 기록 패키지 구성.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-447",
      "org": "OpenTelemetry (CNCF)",
      "title": "OpenTelemetry Specification — Overview",
      "published": null,
      "url": "https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenTelemetry 명세 개요. 추적·지표·로그 신호, TraceId·SpanId, span 간 링크 정의(입력 원문 텍스트는 앞 13,834자 발췌).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원 의약품 배송 로봇의 승강기 연동과 승강기 가동률 구간별 성공률을 보고한 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 한림대학교성심병원의 서비스 로봇 7종 73대와 커맨드센터 통합관제 운영 보도.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-995",
      "org": "Offshore Technology (Eve Thomas)",
      "title": "Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones",
      "published": "2025-11-21",
      "url": "https://www.offshore-technology.com/features/equinor-autonomous-robotics/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Equinor 시설의 4족 점검 로봇 운영(계기 판독·누출 탐지)과 운영자 임무 생성 보도.",
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
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 제도 안내. 인증 대상은 로봇과 관제장치의 조합.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-961",
      "org": "Responsible AI Collaborative (AI Incident Database)",
      "title": "Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks",
      "published": null,
      "url": "https://incidentdatabase.ai/cite/346/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔 로봇이 단순 업무를 처리하지 못한 사건 기록.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-962",
      "org": "Hotel Technology News",
      "title": "Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce",
      "published": "2019-01",
      "url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔의 로봇 절반 철수와 직원 개입 부담 보도.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "sections": [
        "3",
        "5",
        "7",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3 — '같은 시간축·같은 어휘' 근거로 f14(시각 형식 차이)·f9(심각도 표현 차이)·f13(통신 원인 신호)·f15(사람 개입 범주) 추가 / 섹션 5 — 물류창고 가상 시나리오의 문·작업 상태·경보 서술을 오늘 원문으로 재확인(f6·f7·f8), 현장 유형별 사례를 나눠 추가: 병원 f16(승강기 혼잡 원인)·f17(통합관제, 원인 분석 비공개), 상업 시설 f20, 실외 f19, 기타 f18 / 섹션 7(주제 페이지로 분리된 절의 요약) — VDA 5050 필수 오류·운용 모드·information 제한(f1·f2), 오류 수준(f3), 연결 상태(f4), MassRobotics 오류 코드 형식(f5), Open-RMF 배차 오류·개입 기록(f6), OpenTelemetry 추적·링크(f11) / 섹션 9 — 로봇 내부 진단은 연계 대상(f10), 심각도 대응 규칙과 작업 식별자 연결은 직접 범위 후보(f9·f12) / 섹션 11 — oq-033·oq-073 부분 근거(f9), oq-210 부분 근거(f12), oq-074·oq-075 미해결(f21), 새 질문 2건. 다음 실행 후보: 37. 관제 화면·실행 기록(f7 경보), 22. 설비·건물 시스템 연동(f16)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "연결 상태",
      "term_en": "Connection State (VDA 5050 connectionState)",
      "definition": "VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다."
    },
    {
      "term_ko": "경보 등급",
      "term_en": "Alert Tier (Open-RMF Alert)",
      "definition": "Open-RMF 경보 메시지가 운영자에게 보내는 경보의 심각도를 INFO·WARNING·ERROR 세 단계로 나타내는 필드다."
    }
  ],
  "open_questions_new": [
    "MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 21. 상호운용 표준·적합성 | 근거: f9 | 종류: 일반",
    "VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f13 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "oq-033·oq-073 미해결: 세 규약 사이의 공식 대응표는 원문 어디에도 없음(f9 는 도출)",
      "oq-210 부분 근거만: 작업 식별자와 추적 TraceId 를 잇는 표준 미확인(f12)",
      "oq-074·oq-075 미해결: 원인별 발생 비율 공개 자료 미확인(f21)",
      "ref-051 원문 텍스트가 앞 13,220자 발췌라 오류 객체 정의(errorLevel enum)는 이 원문에서 확인하지 못했고 f3 은 ref-031 재인용에 기댐",
      "f16 구로병원 전체 성공률 분모 미확인",
      "f19 운행안전인증 관제장치 항목의 세부 요건 미확인",
      "제조 공장 현장의 이상 탐지·원인 분석 사례는 이번 브리프에 없음"
    ],
    "scope_violations": [
      "f10: 센서·드라이버 수준 진단은 로봇 자체 지능·제어 경계라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 결과 수신으로 한정",
      "f8·f16: 문 개폐 제어와 승강기 운행 제어는 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 상태 확인·원인 범주 반영",
      "f18: 계기 판독·누출 탐지 자체는 로봇 인식 기능(연계 대상)이며 ROP 쪽은 점검 결과를 이상 판정·업무 시스템으로 넘기는 부분만 다뤄야 함",
      "f19: 인증 판단은 인증 기관·운영자 쪽이며 실외 현장 제약으로만 반영"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 0
    },
    "limits": "재실행 1회차(실행 컨텍스트에 retry_count 가 없어 1회차로 적음). 반려 사유 1(스키마 불일치: f9 가 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts 의 ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447, fetched_via inbox)와 이전 브리프(2026-10-09-14, 2026-10-09-15)의 기존 참고문헌만으로 브리프를 다시 구성했다. 새 f9 는 심각도 표현 비교로 [추정]이며 벤더 문서를 근거로 한 finding 은 하나도 없다(vendor_claim 대상 없음). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1367~ref-1396 은 쓰지 않았다. 재인용한 ref-031·ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 는 이번에 열지 않아 fetched false·source_unopened true 이고 신뢰도는 medium 이하다. 교차 확인 0건. 정정 요청 없음, 우선 지정 질문 없음, 입력 누락 없음. 현장 유형: 병원(f16·f17), 상업 시설(f20), 실외(f19), 기타(f18); 물류창고는 기존 5절 시나리오의 재확인(f6·f7·f8)만, 제조 공장 사례는 없음. L. AI·학습 기술 관련 새 finding 은 없어 47. AI·학습·적응과 모델 운영 연결(oq-315)은 그대로다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈을 섞지 않았다. 해결 제안한 열린 질문 없음."
  }
}
```

### runs/2026-10-09-16/verification.json

```json
{
  "run_id": "2026-10-09-16",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-051(state.schema)에서 required 목록에 errors·operatingMode·safetyState가 있고 operatingMode enum이 7개임을 대조했다. 단일 1차 출처(표준 원문)다. 발행일은 미확인이고 main 브랜치 기준이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(부분). 앞 절(information은 시각화·디버깅 전용이며 플릿 관제 로직에 쓰지 않음)은 ref-051 원문과 글자 단위로 일치한다. 뒤 절 '원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다'는 출처에 없는 도출이다. 직접 인용은 ref-051에서 1회로 허용 범위다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력의 ref-031 발췌(앞 59,038자)에는 오류 객체 절이 없다. 그래서 검증에서 raw.githubusercontent.com의 VDA5050 main state.schema(ref-051과 같은 문서)를 열어 확인했다. errorLevel은 WARNING·URGENT·CRITICAL·FATAL 네 값이고, errorDescription·errorHint와 각각의 Translations(ISO 639-1 키)가 있다. 같은 발행 주체의 두 문서라 독립 교차 확인은 아니다. ref-031 출처 summary가 '원문 미열람.'으로 시작하는데 fetched true·source_unopened false로 적혀 있어 서로 맞지 않는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-449(connection.schema)와 대조했다. 연결 상태 4값, 질서 있는 종료 시 OFFLINE, 유언 메시지 CONNECTION_BROKEN(retain), HIBERNATING(연결 유지·state 미발행·절전/통신 감축)이 모두 원문에 있다. ref-031 4.1절도 같은 내용을 담고 있으나 같은 발행 주체다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-230과 대조했다. operationalState enum은 9개다. errorCodes는 string 배열이고 uniqueItems이며 'should be omitted for normal operation'이다. statusReport에는 심각도 필드가 없다(additionalProperties false). 발행일 미확인."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(부분). 다음 사항은 입력 원문 ref-111과 일치한다: status enum 12개, dispatch.status의 failed_to_assign·canceled_in_flight, dispatch.errors, interruptions의 요청 시각·labels·resumed_by, cancellation·killed의 요청 시각·labels. 그러나 '지연이 배정 실패인지 실행 중 차단인지 사람 개입인지를 나눠 볼 수 있다'는 도출이다. labels는 요청 출처 설명(예: dashboard)일 뿐 사람 개입 여부를 정의하지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-448(Alert.msg)과 대조했다. tier 0~2(INFO·WARNING·ERROR), responses_available, alert_parameters, task_id(작업이 없으면 비움), display 기본 true가 원문에 있다. 기존 5절 서술과 일치한다(재확인)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-313 DoorMode 5값과 ref-283 Doors 장(어댑터를 거치지 않은 직접 요청은 어댑터가 이전 상태로 되돌림, 상태 감독자)이 원문과 일치한다. 두 출처 모두 Open Robotics 발행이라 독립 교차 확인은 아니다. 기존 5절 문 서술은 유효하다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 전제가 되는 세 심각도 표현(VDA 5050 네 단계, Open-RMF 세 등급, MassRobotics 등급 없는 문자열)은 각 원문에서 확인했다. 대응 규칙이 필요하다는 결론은 도출이며 oq-033·oq-073의 부분 근거다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(부분). 앞 절은 입력 원문 ref-445 README와 일치한다(하드웨어 드라이버·로봇 하드웨어 진단, /diagnostics, diagnostic_aggregator, diagnostic_remote_logging의 influxdb 전달). 'ROP는 이 결과를 원인 범주 판정의 입력으로 받는 쪽에 선다'는 출처에 없는 경계 판단이다. 기존 9절도 이 내용을 [추정]으로 두고 있다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-447 Overview와 대조했다. 분산 추적 정의(프로세스·네트워크·보안 경계를 넘는 사건), TraceId 16 무작위 바이트로 모든 프로세스의 span을 묶음, Links의 일괄 처리·Trace 간 인과 연결이 원문에 있다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. booking.id('The unique identifier for this task')와 orderId(현재 또는 직전 완료 주문 식별)의 정의는 원문과 일치한다. 추적 TraceId와의 대응은 도출이며, 이를 정한 표준이 없다는 한계를 brief가 명시했다(oq-210 부분 근거)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. headerId의 '보낸(반드시 수신되지는 않은) 메시지마다 1 증가'는 ref-051·ref-449 원문과 일치한다. 결번 판정 기준은 명세에 없다. 참고로 ref-031 표 2는 connection 토픽이 MQTT 수준의 연결 확인용이며 로봇 건강 상태 판단용이 아니라고 적고 있다. 이 finding은 통신 원인 판단에만 쓰므로 그 기술과 충돌하지 않는다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 timestamp ISO8601(YYYY-MM-DDTHH:mm:ss.fffZ)(ref-051), MassRobotics timestamp format date-time(ref-230), Open-RMF unix_millis_* integer(ref-111)를 각 원문에서 확인했다. 세 표준마다 자기 원문이 1차 근거다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 다만 표현을 고쳐야 한다. INTERVENED·MANUAL(ref-051)과 manualOverride·waitingHumanEvent(ref-230)는 원문에 있다. 그러나 Open-RMF interruptions.labels는 요청 출처를 설명하는 값(예: dashboard)이고 사람 개입을 표시한다고 정의되지 않았다. waitingHumanEvent는 개입이 아니라 사람 사건 대기다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 브리프는 원문 미열람이었고, 검증에서 PMC13039597을 열어 확인했다(Digital Health 2026-03-31, 고려대 구로병원·도구공간). 일치: 승강기 가동률 59.01% 미만 구간의 성공률 95.52%, 제어반 전용 통신 모듈. 불일치: '실패가 가동률 90% 초과 구간에 몰려'는 원문과 다르다. 원문은 실패 사례의 승강기 가동률이 높은 쪽에 몰렸다(중앙값 약 90%)고 적고, 90% 초과 수치는 탑승 인원 관련이다. '설비 혼잡이 원인으로 드러났다'는 해석이다. R-1에 따라 브리프의 source_unopened 표시와 신뢰도 상한은 유지한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증에서 로봇신문(2024-04-15)을 열어 확인했다. 7종 73대, 커맨드센터 통합관제시스템, 서로 다른 제조사 로봇의 중앙 관리가 보도에 있고, 이상 탐지·원인 분석·장애 통계·관제 화면 항목은 언급이 없다. 주의: 같은 기사의 세부 분류 합계(8종 76대)가 7종 73대와 맞지 않는다. '공개되지 않았다'는 이 보도 기준의 부재 진술로 한정해야 한다. 브리프의 원문 미열람 표시는 유지한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증에서 Offshore Technology(Eve Thomas, 2025-11-21)를 열어 확인했다. 계기·밸브 위치 판독(줌 카메라), CO₂ 등 가스 탐지·위치 파악, 운영자가 R&D 팀 없이 임무를 직접 생성하는 내용이 기사에 있다. 다만 기사는 시설을 노르웨이 Northern Lights 시설로 적고 '이산화탄소 포집·저장 시설'이라는 표현은 쓰지 않는다. 계기 판독·가스 탐지는 로봇 인식 기능으로 연계 대상이다. 단일 기사이며 원문 미열람 표시는 유지한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(부분). 검증에서 한국로봇산업진흥원 페이지를 열어 확인했다. 인증 대상은 '실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체'이고, 관제장치가 심사 항목에 포함된다. 그러나 '관제장치의 감시 기능이 운행 조건의 하나가 된다'의 '감시 기능'은 출처에 없는 도출이다. 참고로 이 페이지는 심사 항목을 8개로 적고 있어, 실행 2026-10-09-15 브리프의 '16개 항목'(기사 근거)과 다르다. 이번 브리프 범위 밖이므로 열린 질문 후보로만 남긴다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(표현 수정 필요): AI Incident Database 346은 일정 질문·여권 복사 같은 업무를 사람 개입 없이는 처리하지 못했다고 적는다. Hotel Technology News는 객실 비서·짐 운반 로봇의 실패, 프런트 공룡 로봇의 여권 스캔 실패, 243대 중 절반 이상 철수를 보도한다. '직원이 계속 넘겨받아야 했다'는 원문의 '사람의 일을 늘렸다' 수준보다 강하다. AIID는 같은 보도들을 모은 데이터베이스라 독립 교차 확인으로 보지 않는다. 사건일은 2016-06-15(AIID)이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "삭제",
      "note": "근거 출처 ref-943과 충돌한다. 검증에서 연 구로병원 논문은 실패 14건을 복도 자율주행 오류 4·통신 오류 2·승강기 막힘 8로 나누고, 실패 유형별 승강기 가동률 중앙값도 보고한다. 따라서 '병원 사례가 원인별 분류를 공개하지 않는다'는 주장은 성립하지 않는다. oq-074·oq-075는 물류창고 대상이므로 미해결로 두되, 이 finding은 본문에 쓰지 않는다."
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
      "f7·f8은 기존 5절 물류창고 시나리오의 문 모드·문 어댑터·경보 서술과 같은 주장이다. 기존 각주 ref-313·ref-283·ref-448을 재사용하고 접근일만 2026-10-09로 갱신한다.",
      "f9는 기존 3절 첫 두 문단의 [추정](서로 다른 어휘, 공통 매핑 표준 없음, oq-033)과 겹친다. 새 문단을 만들지 말고 기존 문장을 보강한다.",
      "f10은 기존 9절 표·본문의 ROS 2 diagnostics 연계 대상 [추정][^ref-445]과 같은 주장이다.",
      "f16·f17·f18·f19·f20은 실행 2026-10-09-14(Q. 현장 유형별 적용 대분류 연결)·2026-10-09-15(37. 관제 화면·실행 기록)의 finding과 같은 출처·주장이다. 같은 ref id(ref-943·ref-944·ref-995·ref-980·ref-961·ref-962)를 재사용한다.",
      "open_questions_new 1번(MassRobotics 오류 코드의 심각도 부여)은 oq-033·oq-073과, 실행 2026-10-09-15의 새 질문(세 규약 상태 값 대응표)과 주제가 가깝다. 심각도 부여 기준이라는 하위 질문으로는 구분되므로 관련 질문을 표시해 등록한다."
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
    "f2: 앞 절 'VDA 5050 state 스키마는 information 배열을 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정한다'만 [사실][^ref-051]로 쓴다. 뒤 절 '원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다'는 별도 문장 [추정][^ref-051]으로 쓴다 — 뒤 절은 출처에 없는 도출이다.",
    "f3: [사실]을 유지하고 각주를 [^ref-031][^ref-051] 두 개로 단다 — 오류 수준 4단계와 errorDescription·errorHint(번역 필드 포함)를 검증에서 ref-051 state.schema 원문의 error 정의로 확인했고, 입력의 ref-031 발췌에는 해당 절이 없다.",
    "f6: 상태 12값·배차 상태(failed_to_assign)·배차 오류 배열·일시정지/재개/취소/강제 종료 요청의 시각·라벨 기록까지만 [사실][^ref-111]로 쓴다. '지연이 배정 실패인지 실행 중 차단인지 사람 개입인지를 기록에서 나눠 볼 수 있다'는 [추정][^ref-111]으로 쓰고, '사람 개입' 대신 '개입 요청(라벨로 출처 표시)'으로 쓴다 — labels는 요청 출처 설명이며 사람 개입을 정의하지 않는다.",
    "f10: 9절에서 'ROS 2 diagnostics는 하드웨어 드라이버·로봇 하드웨어 진단을 /diagnostics로 모아 aggregator로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘긴다'만 [사실][^ref-445]로 쓴다. 'ROP는 그 결과를 원인 범주 판정의 입력으로 받는다'는 기존 9절처럼 [추정][^ref-445]으로 쓰고 '연계 대상:' 표시를 유지한다 — 경계 판단은 출처에 없다.",
    "f15: 'Open-RMF 작업의 일시정지 라벨이 사람 개입을 표시'라는 표현을 'Open-RMF 작업 기록이 일시정지·재개 요청과 그 요청 출처 라벨을 남긴다'로 바꾸고, waitingHumanEvent는 '사람 사건 대기'로 쓴다. [추정] 태그는 유지한다 — 원문은 라벨을 사람 개입 표지로 정의하지 않는다.",
    "f16: [사실] → [추정]으로 강등한다. 문장을 '승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다'로 고친다. '가동률 90% 초과 구간'이라는 표현은 쓰지 않는다. '설비(승강기) 혼잡이 원인으로 드러났다'는 해석임을 밝힌다. 승강기 운행 제어 자체는 연계 대상(시설·설비 제어)이며 ROP 몫은 승강기 상태를 원인 범주에 반영하는 데까지라고 쓴다 — 검증에서 연 원문과 '90% 초과' 수치가 일치하지 않는다(90% 초과는 탑승 인원 관련).",
    "f17: 문장을 '이 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다'로 한정한다. '7종 73대'는 '보도 기준'으로 쓴다 — 부재 진술은 이 기사 하나에 기댄 것이고, 같은 기사의 세부 분류 합계가 7종 73대와 맞지 않는다.",
    "f18: 시설을 '이산화탄소 포집·저장 시설' 대신 '노르웨이 Northern Lights 시설'로 쓴다. 계기 판독·가스(누출) 탐지는 로봇 인식 기능인 연계 대상으로 짧게 두고, ROP 쪽은 점검 결과를 이상 판정으로 받는 부분만 서술한다 — 기사는 '포집·저장'이라는 표현을 쓰지 않는다.",
    "f19: '실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 한다'만 [사실][^ref-980]로 쓴다. '실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 된다'는 [추정][^ref-980]으로 쓰고, 운행 안전 인증 판단은 인증 기관·운영자 쪽 연계 대상이라고 밝힌다 — '감시 기능'은 출처에 없는 도출이다.",
    "f20: '직원이 계속 넘겨받아야 했고'를 '사람 개입 없이는 처리하지 못해 사람의 일을 늘렸고'로 고친다. 철수 규모는 '로봇 일부(보도 기준 절반가량)'로 쓴다. 기준일은 보도 시점 2019-01을 유지한다 — 원문 표현보다 강한 단정을 피한다.",
    "f21: 본문에 쓰지 않는다. 그 대신 additional_research_requests에 '구로병원 논문(ref-943)의 실패 유형별 분류(복도 자율주행·통신·승강기 막힘)와 전체 성공률·분모를 원문 기준으로 재조사해 38. 모니터링·이상 탐지·원인 분석 5절 병원 사례와 oq-074에 반영'을 넣는다 — f21은 근거 출처 ref-943과 충돌한다.",
    "5절: 새 현장 유형 사례(병원 f16·f17, 상업 시설 f20, 실외 f19, 기타 f18)를 현장 유형마다 나눠 쓰고, 여섯 항목 가운데 브리프 finding이 없는 칸은 '미확인'으로 둔다. site_matrix_updates에는 실제로 채운 칸만 넣는다. 제조 공장 사례는 '이번 조사에서 찾지 못함'으로 둔다 — 단일 finding으로 여섯 항목을 채울 근거가 없다.",
    "3절: 기존 둘째 문단의 '2절의 질문, 곧 지연 원인이 로봇 고장인지 문인지 앞 공정인지'를 현재 2절 원문 질문('로봇인지, 설비인지, 통신인지, 앞 작업인지')에 맞게 고친다. 원문 문장은 [분류원문] 태그 없이 풀어 쓴다 — 개정 전 옛 질문 표현이 남아 있다.",
    "open_questions_new 1번(MassRobotics 오류 코드 심각도 부여 기준)은 질문 끝에 '(관련: oq-033, oq-073)'를 붙여 등록한다. 근거 f9, 관련 영역 38. 모니터링·이상 탐지·원인 분석·21. 상호운용 표준·적합성, 종류 일반은 그대로 둔다 — 기존 질문과 주제가 가깝다.",
    "각주·참고문헌: 재확인한 ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447·ref-031은 접근일을 2026-10-09로 갱신한다. 기관·제목은 docs/references 색인의 줄을 그대로 쓴다(기존 각주의 ref-111·ref-283·ref-230 기관 표기가 색인과 다르다).",
    "각주·참고문헌: ref-943·ref-944·ref-995·ref-980·ref-961·ref-962는 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates에 source_unopened: true를 넣는다 — 브리프가 이번 실행에서 원문을 열지 않았다고 기록했다(R-1에 따라 검증 열람으로 표시를 올리지 않는다)."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 15건, 미확인 6건, 교차 확인 0건. 강등: f2·f6·f10·f19(사실 → 추정, 출처에 없는 도출 절 분리), f16(사실 → 추정, '가동률 90% 초과에 실패 집중'이 원문과 다름). 삭제: f21(근거 출처 ref-943이 실패 유형을 복도 자율주행·통신·승강기 막힘으로 나눠 보고하므로 주장과 충돌). 원문 미열람 출처: ref-943, ref-944, ref-995, ref-980, ref-961, ref-962(브리프 기준. 검증에서 열어 f16 수치 불일치와 f17·f18·f19·f20 표현 과장을 찾았다). 주의: 3절 새 주장과 9절 경계는 대부분 표준 필드를 대조한 [추정]이다. 세 규약(VDA 5050·MassRobotics·Open-RMF) 사이의 공식 대응표나 작업 식별자–추적 연결 표준은 확인되지 않았다(oq-033·oq-073·oq-210 부분 근거, oq-074·oq-075 미해결). f3 오류 수준 4단계는 입력 ref-031 발췌에 없어 검증에서 VDA 5050 state.schema 원문으로 확인했다. 브리프 표기 문제: ref-031 summary는 '원문 미열람.'으로 시작하는데 fetched true·source_unopened false로 적혀 있다. github 출처의 fetched_via는 github_raw이지만 한계 항목은 inbox로 적었고 fetch_url이 비어 있다. 검색 0회로 신규 조사가 없는 재실행 브리프다. 한림대성심병원 보도는 세부 분류 합계(8종 76대)가 7종 73대와 맞지 않는다. 실외이동로봇 운행안전인증 심사 항목 수는 진흥원 페이지(8개)와 이전 브리프의 기사(16개)가 다르다. 정정 요청 없음. 기존 10절의 '분류 개정 전 원문 8장의 교차 규칙' 표현은 이번 갱신 절 밖이며 다음 갱신에서 원문 13장(L. AI·학습 기술 주석) 기준으로 확인할 대상이다.",
  "retry_reason": null
}
```

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석"
type: area
category: "J. 현장 운영·관제"
area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [이상 탐지, 근본 원인 분석, VDA 5050, Open-RMF, 분산 추적]
status: published
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-051, ref-445, ref-447, ref-448, ref-313, ref-111, ref-449, ref-230, ref-283, ref-451]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 38. 모니터링·이상 탐지·원인 분석

# 38. 모니터링·이상 탐지·원인 분석

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

이종 로봇이 섞인 현장에서는 로봇 오류 수준·연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 작업 지연·차단과 문 모드(Open-RMF)가 서로 다른 어휘로 보고되므로, 지연 원인을 가리려면 이들을 같은 시간축에 맞추고 ROP 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111]

2절의 질문, 곧 지연 원인이 로봇 고장인지 문인지 앞 공정인지를 가리는 일은 복구 담당과 조치를 정하는 출발점이다. 그런데 각 표준은 자기 필드만 정의하고 서로 간 대응표는 두지 않으며, 이번 조사에서는 공통 매핑 표준을 찾지 못했다(열린 질문 oq-033). [추정][^ref-051][^ref-230][^ref-111]

원인 구분은 처리량 관리와도 이어진다. 무인운반차(Automated Guided Vehicle, AGV) 시스템을 다룬 2003년 연구는 기존 두 방법(가동률·대기 시간 기반)에는 이동 병목 탐지와 비교해 여러 한계가 있다고 보고한다. [사실][^ref-451] 어느 설비·로봇이 흐름을 막는지 판정하는 방식에 따라 개선 대상이 달라질 수 있다는 뜻이다.

## 4. 핵심 개념과 용어

아래 용어는 3절에서 말한 서로 다른 보고 어휘와 원인 분석 기법을 읽기 위한 기본 개념이다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area19-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 보충

**시나리오:** 보충용 박스를 운반하던 AMR 이 문 앞에서 멈춰 보충이 늦어진 원인 가리기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 피킹 구역 재고가 보충 기준 아래로 내려가 보충 작업이 생성된다(가상 설정). |
| 작업 대상 | 예비 보관 구역에서 피킹 구역으로 옮길 보충용 박스와 이를 실은 자율이동로봇(AMR). |
| 수행 자원 | AMR 은 운반, 문 설비는 개폐, ROP 는 상태 수집과 원인 구분, 운영자는 경보 응답을 맡는다. 문 개폐 제어 자체는 연계 대상(시설·설비 제어)이며 ROP 는 문 상태 확인과 문 요청만 다룬다. |
| 제약 | 경로가 문을 지나야 한다. Open-RMF 에서 문 노드는 문 상태를 /door_states 로 발행하고 문 모드는 closed·moving·open·offline·unknown 다섯 값이다. [사실][^ref-313][^ref-283] 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다. [사실][^ref-283] |
| 완료·인계 | 작업 상태가 completed 로 바뀌고 보충 위치 도착이 확인되면 보충 완료로 본다. 작업 상태 토큰 completed 는 Open-RMF 작업 상태 스키마에 있다. [사실][^ref-111] |
| 예외·성과 | 작업 상태가 delayed 또는 blocked 로 바뀌고 [사실][^ref-111], MassRobotics 운용 상태가 waitingExternalEvent 를 보고하며 [사실][^ref-230], 경보는 심각도 등급(INFO·WARNING·ERROR)·응답 목록·관련 작업 id 를 담아 운영자에게 간다. [사실][^ref-448] 이 신호들을 맞춰 원인을 문·로봇·통신 중 하나로 판정하는 절차는 추정이다. [추정][^ref-313][^ref-111][^ref-230] |

다음은 설명을 위한 가상의 시나리오이다. 보충 작업을 받은 AMR 이 문 앞에서 멈추고, ROP 에는 작업 지연과 외부 사건 대기가 함께 들어온다. 수치는 쓰지 않는다.

ROP 는 같은 시각의 문 모드를 확인한다. 문 모드가 offline 이나 unknown 이면 설비 쪽 원인일 가능성을, 문이 open 인데도 로봇이 대기 중이면 로봇 쪽 원인일 가능성을 먼저 살피는 식으로 판정 순서를 세울 수 있어 보인다. [추정][^ref-313][^ref-230] 로봇 연결이 CONNECTION_BROKEN 으로 끊겼다면 통신 원인을 따로 볼 수 있다. [추정][^ref-449]

원인 범주가 정해지면 경보의 응답 목록으로 운영자가 조치를 고르고, 복구 방식은 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)으로 넘어간다. 현장 유형 매트릭스 전체는 [현장 유형 매트릭스](../../site-matrix.md)에 있다.

## 6. 대표 접근법과 기술

5절의 판정 절차를 일반화하면 다음 접근들로 정리된다. 대부분 표준 필드는 확인됐지만 물류 로봇 관제에 적용한 공개 사례는 확인되지 않았다. [추정][^ref-051][^ref-447]

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area19-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

6절의 접근은 아래 표준·오픈소스가 정의한 필드와 신호를 재료로 쓴다. VDA 5050 은 3.0.0 판(GitHub main 브랜치, 접근일 2026-09-25) 기준이며 main 브랜치는 판이 바뀔 수 있다. [사실][^ref-051]

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area19-s7.md)에 있다.

## 8. 대표 연구와 자료

7절의 표준이 무엇을 보고하는지를 정한다면, 아래 연구는 그 보고로 원인과 병목을 찾는 방법을 다룬다. 논문은 모두 원문 미열람이며 검색 요약 기준이다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 대표 연구와 자료](../../topics/2026/2026-09-25-area19-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 표준 인터페이스가 보고하는 오류 수준·연결 상태·작업 상태를 모아 원인 범주(로봇·설비·통신·공정)로 구분하고 업무 영향과 연결 [추정][^ref-051][^ref-449][^ref-111] | 연계 대상: 센서·모터·드라이버 수준의 진단(ROS 2 diagnostics 같은 로봇 내부 진단)과 개별 부품 고장 진단 [추정][^ref-445] |
| 시설·설비 제어 | 문 상태(DoorMode) 확인과 문 요청, 문 대기를 원인 범주에 반영 [추정][^ref-313][^ref-283] | 연계 대상: 문 개폐 제어 자체 |

센서·모터·드라이버 수준의 진단과 개별 부품 고장 진단은 로봇 제조사 영역이며, 이종 로봇을 연결하는 ROP 는 표준 인터페이스가 보고하는 오류 수준·연결 상태·설비 상태·작업 상태를 모아 원인 범주로 구분하고 업무 영향과 연결하는 부분을 맡는 경계가 될 것으로 보인다. [추정][^ref-445][^ref-051][^ref-449][^ref-111] 경계의 원문 정의는 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

원인 구분은 상태를 모으는 영역, 결과를 쓰는 영역과 양쪽으로 이어진다.

- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) — 병목 탐지 연구와 SCM 프로세스 마이닝 리뷰가 처리량 개선과 이어지며 oq-018 을 함께 다룬다.
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 원인 구분은 현재 상태를 표현하는 오류·연결·문·작업 상태를 같은 시간축에 맞춘 데이터를 쓴다.
- [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) — VDA 5050·MassRobotics 가 보고하는 오류 수준·연결 상태·운용 상태가 여기서 들어온다.
- [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md) — 문 상태 발행과 문 어댑터가 설비 원인 판정의 근거가 된다.
- [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 동작 실패와 오류 보고의 대응, 작업 상태 토큰이 실행 결과 확인과 겹친다.
- [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md) — 경보의 응답 목록과 관제 인터페이스 연구가 운영자 대응으로 이어진다.
- [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 오류 수준이 주문 계속 가능 여부를 가르고, 판정된 원인이 복구 방식 선택으로 넘어간다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 분류 개정 전 원문 8장의 교차 규칙에 따라 장애 분석은 이 영역에 적용되는 AI 연구 방법이며, LLM 실패 설명(REFLECT)이 그 예다.

## 11. 열린 질문

위 내용 가운데 확인되지 않은 부분을 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문](../../topics/2026/2026-09-25-area19-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) — 영역 심화: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 13절 각주 정의(1차 조건부 승인 수정 14건 반영). 형식 재작성: 프런트매터 sources 를 이 페이지 각주 정의와 일치시킴 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area19-s4.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "4. 핵심 개념과 용어" 절(1,482자)을 옮겼다 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area19-s7.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,413자)을 옮겼다 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 대표 연구와 자료](../../topics/2026/2026-09-25-area19-s8.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "8. 대표 연구와 자료" 절(1,396자)을 옮겼다. 형식 재작성: 8. 실시간 세계 상태·데이터 일관성 링크를 주제 페이지 기준 경로로 고침 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area19-s6.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "6. 대표 접근법과 기술" 절(861자)을 옮겼다. 형식 재작성: 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침 (실행 2026-09-25-48)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-445]: ROS (ros/diagnostics GitHub), diagnostics — README (ros2 branch), 미확인, https://github.com/ros/diagnostics/blob/ros2/README.md, 접근일 2026-09-25
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-09-25
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-09-25
[^ref-313]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics (MassRobotics-AMR/AMR_Interop_Standard), AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-283]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Doors, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-451]: Roser, C., Nakano, M., & Tanaka, M., Comparison of bottleneck detection methods for AGV systems (WSC 2003 Proceedings, 1192–1198쪽), 2003, https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/field-operations-and-monitoring/index.md

```markdown
---
title: "J. 현장 운영·관제"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-031, ref-051, ref-096, ref-102, ref-111, ref-125, ref-139, ref-140, ref-145, ref-146, ref-148, ref-230, ref-283, ref-302, ref-313, ref-447, ref-448, ref-449, ref-453, ref-494, ref-569, ref-762, ref-781, ref-782, ref-944, ref-1093, ref-1094, ref-1096, ref-1098, ref-1099, ref-1103, ref-1150, ref-1151, ref-1152, ref-1153, ref-1154, ref-1157, ref-1199, ref-1228, ref-1220, ref-1226, ref-1333, ref-1120, ref-1032, ref-1334, ref-1335, ref-1336]
---

[홈](../../index.md) › J. 현장 운영·관제

# J. 현장 운영·관제

## 핵심 질문

운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

## 개요

운영 사용자가 상태를 보고, 이상을 알아차리고, 원인을 찾고, 성과를 측정하고, 운영 절차를 돌리는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **37. 관제 화면·실행 기록** | 지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 | 운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? | [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) | published |
| **38. 모니터링·이상 탐지·원인 분석** | 감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 | 지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? | [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) | published |
| **39. 운영 성과 측정·개선** | 지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 | 로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? | [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) | published |
| **40. 운영 절차·요청 창구** | 운영 절차·교대, 현장 사용자의 요청 창구 | 현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? | [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

운영 화면은 로봇 상태를 보여 주는 데서 끝나지 않는다. **왜 그런 상태인지와 사람이 무엇을 해야 하는지**까지 보여 줘야 운영자가 개입할 수 있다. [분류원문]

## 다른 대분류와의 연결

J. 현장 운영·관제의 네 세부영역은 다른 대분류가 만든 지도·상태·계획·기록을 받아 운영자에게 보여 주고, 판정·경보·지표를 다시 다른 대분류로 넘긴다. 아래 연결은 게시된 세부영역 페이지(37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구)와 2026-10-09 조사·검증을 거친 주장에 기댄다. 대부분 단일 출처이거나 세부영역 페이지의 판단을 다시 인용한 것이므로, 두 영역이 이어진다고 해석한 문장은 추정 표기로 남겼다.

### 한눈에 보기

| 다른 대분류 | J. 현장 운영·관제 쪽 세부영역 | 상대 세부영역 |
|---|---|---|
| A. 기획·사업 | 39. 운영 성과 측정·개선 | 3. 경제성·조달·사업 모델 |
| B. 로봇 온톨로지 | 근거 없음 | 아래 '아직 다루지 않은 연결' |
| C. 채팅 기반 구성·운영 | 37. 관제 화면·실행 기록 | 11. 채팅으로 실제 상황 시뮬레이션 재현, 12. 채팅으로 업무 지시·오케스트레이션 |
| D. 공간·지도 모델 | 37. 관제 화면·실행 기록, 40. 운영 절차·요청 창구 | 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리 |
| E. 사물·사람·실시간 상태 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선 | 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성 |
| F. 연동 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동 |
| G. 계획·최적화 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 27. 다중 로봇 경로·교통 관리 — MAPF, 28. 공용 자원·충전·에너지 최적화 |
| H. 실행·협업·예외 복구 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 29. 명령·작업 실행의 신뢰성, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성 |
| I. 설계·시뮬레이션 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선 | 35. 처리능력·규모·배치 설계, 36. 가상 시운전·실제 상황 재현 |
| K. 플랫폼 아키텍처·인프라 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 43. 데이터·관측성·배포 |
| L. AI·학습 기술 | 38. 모니터링·이상 탐지·원인 분석 | 47. AI·학습·적응과 모델 운영 |
| M. 안전 | 37. 관제 화면·실행 기록, 40. 운영 절차·요청 창구 | 50. 안전 표준·인증·사고 조사 |
| N. 보안·개인정보 | 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터 |
| O. 검증·도입·수명주기 | 40. 운영 절차·요청 창구 | 56. 운영 이관·확대·교육 |
| P. 거버넌스·법규·사회 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 59. 법·규제·보험·라이선스, 60. 노동·수용성·접근성 |
| Q. 현장 유형별 적용 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 61. 물류창고, 62. 제조 공장, 63. 병원·의료, 64. 상업 시설 |

### [A. 기획·사업](../planning-and-business/index.md)

- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md): 39. 운영 성과 측정·개선 페이지는 투자 수익률·순현재가치·회수 기간 같은 재무 평가를 연계 대상으로 두고 ROP는 그 입력인 처리량·가동률·충전·예외 실행 데이터를 제공한다고 보므로, 운영 지표가 투자 효과 판단으로 넘어가는 지점에서 두 영역이 이어지는 것으로 보인다. [추정][^ref-148] 그 계량 데이터를 누가 재고 어떻게 합의하는지는 열린 질문 oq-268 로 남아 있다.

### [B. 로봇 온톨로지](../robot-ontology/index.md)

게시된 페이지에서 B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 검증된 근거를 찾지 못했다. 아래 '아직 다루지 않은 연결'에 적었다.

### [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md): 11. 채팅으로 실제 상황 시뮬레이션 재현은 재현 결과를 실제 기록의 시각·위치·사건 순서와 비교해야 하며, 그 실제 기록은 37. 관제 화면·실행 기록이 정규화해 저장하는 실행 기록에서 나올 것으로 보인다. [추정][^ref-1094][^ref-1096] 이 대화 기능이 부르는 엔진은 36. 가상 시운전·실제 상황 재현이므로 아래 I. 설계·시뮬레이션 항목과 함께 읽는다.
- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md): 12. 채팅으로 업무 지시·오케스트레이션이 진행 상황 질의에 실행 기록과 시각을 근거로 답할 때, Open-RMF 작업 상태 스키마의 상태 값, 시작·종료 시각, 단계 목록, 취소·강제 종료 기록이 그 답의 근거 자료가 될 것으로 보인다. [추정][^ref-111] 업무 지시가 부르는 엔진은 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링이다.

### [D. 공간·지도 모델](../space-and-map-model/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md): Open-RMF rmf_visualization 은 층 평면도 위에 로봇 위치, 문·승강기, 주행 그래프, 예측 궤적을 겹쳐 표시한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1093]
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md): Open-RMF 차선 요청(LaneRequest)이 플릿 이름과 열고 닫을 차선 목록 세 필드만 두므로, 임시 통제 구역을 누가 왜 언제까지 닫았는지는 40. 운영 절차·요청 창구의 운영 기록이, 차선·구역 반영은 16. 장소 의미·지도 관리가 맡는 접점이 될 것으로 보인다. [추정][^ref-569] 통제 구역의 선언·해제 절차를 공개한 현장 사례는 열린 질문 oq-203 으로 남아 있다([차선 폐쇄](../../glossary/lane-closure.md) 참고).

### [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)

이 대분류와의 연결은 지금의 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이다. 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 연결은 섞지 않고 아래 I. 설계·시뮬레이션 항목에 따로 둔다.

- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): Open-RMF 로봇 상태가 상태 값·문제 목록과 함께 기록 시각을 담으므로, 지연 원인 구분은 18. 실시간 세계 상태·데이터 일관성이 시각과 함께 유지하는 로봇·문·작업의 현재 상태를 같은 시간축에 맞춘 데이터를 쓸 것으로 보인다. [추정][^ref-148][^ref-051][^ref-313]
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): Open-RMF 로봇 상태 스키마는 상태 값 7개(uninitialized·offline·shutdown·idle·charging·working·error), 0~1 범위의 배터리, 현재 작업 id, 문제 목록, 기록 시각을 담는다(2026-10-09 확인). [사실][^ref-148] 이 값이 가동률·충전·오류 시간 지표의 원천이 될 것으로 보인다. [추정][^ref-148] 같은 해석이 [A. 기획·사업의 '다른 대분류와의 연결'](../planning-and-business/index.md#다른-대분류와의-연결)에도 같은 각주로 실려 있다.
- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)(병원): 현대차·기아와 한림대학교의료원이 안면 인식 기반 수령 인증과 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 한 협약 보도(2025-04-07, 운영 결과 미확인)를 보면, 병원의 완료·인계 단계에서 수령인 확인과 배송 이력 기록이 한 기록으로 묶일 것으로 보인다. [추정][^ref-1103]

### [F. 연동](../integration/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0 은 차량 위치·계획 경로를 시각화 시스템에 보내는 visualization 토픽을 상태(state) 토픽과 따로 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 의 오류 수준과 연결 상태(CONNECTION_BROKEN), MassRobotics 의 외부 사건 대기(waitingExternalEvent), Open-RMF 의 작업 지연·차단은 서로 다른 어휘로 보고되므로, 20. 로봇·제조사 관제 연동에서 들어온 신호를 ROP 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-111] 공통 매핑 표준은 확인되지 않았고 열린 질문 oq-033·oq-073 으로 남아 있다.
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 문 모드는 closed·moving·open·offline·unknown 다섯 값이고, 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다(2026-10-09 확인). [사실][^ref-313][^ref-283] 문 개폐 제어 자체는 시설·설비 제어 경계의 연계 대상이며, 이 연결에서 ROP 몫은 문 상태 확인과 작업 요청으로 한정된다.
- 연계 대상: [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)(병원): 미국 MultiCare 계열 두 병원의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기 버튼을 스스로 누르지 못해 사람이 계속 따라다녀야 했다고 2026-06-09 보도되었다. [사실][^ref-1154] 승강기 조작은 시설·설비 제어 경계의 연계 대상이며, 40. 운영 절차·요청 창구 페이지도 승강기 연동을 이 영역 밖의 설비 연계로 둔다.
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)(물류창고): 로봇·작업 상태 기록만으로는 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표를 계산할 수 없으므로, 이 지표는 23. 업무 시스템 연동을 거쳐 WMS·ERP 주문 데이터와 이어야 계산될 것으로 보인다. [추정][^ref-140][^ref-148][^ref-111] 이를 실제로 검증한 공개 사례는 열린 질문 oq-015 로 남아 있다.
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)(병원): 미국 ChristianaCare 는 간호사가 키오스크에서 Moxi 로봇을 호출하던 방식에 더해, 로봇을 Cerner 전자의무기록과 연동해 주문이 들어오면 로봇이 물품을 가지러 가게 하는 계획을 밝혔다(2022-08-11 보도, 계획 단계이며 운영 결과 미확인). [사실][^ref-1334] 주문 취소·변경을 진행 중인 로봇 작업에 반영한 공개 사례가 있는지는 [열린 질문](../../open-questions.md)에 새로 올렸다.

### [G. 계획·최적화](../planning-and-optimization/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): [설명 가능한 다중 에이전트 경로 찾기](../../glossary/explainable-mapf.md) 연구(Kottinger·Almagor·Lahijanian, ICAPS 2022)는 경로 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 문제를 다루지만 알고리즘 수준의 연구다. [사실][^ref-1098]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터가 위치 신뢰도와 실행 행동 증거를 결합해 에이전트를 분류하는 것으로 미루어, 실행 기록으로 이상 로봇을 가려 배정 후보에서 빼는 일이 두 영역의 접점이 될 것으로 보이며 물류센터 적용은 확인되지 않았다. [추정][^ref-494] 같은 연결이 [G. 계획·최적화의 '다른 대분류와의 연결'](../planning-and-optimization/index.md#다른-대분류와의-연결)에도 같은 각주로 실려 있고, 배정 전 검증 기준은 열린 질문 oq-082 로 남아 있다.
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)(물류창고): Omega(2024) 게재 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했으며, 이는 모델·시뮬레이션 조건의 저자 보고값이고 현장 실측이 아니다. [사실][^ref-146] A. 기획·사업 페이지의 연결 절에도 같은 값과 단서가 실려 있다.
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md): Open-RMF 작업 요청 스키마가 가장 이른 시작 시각과 우선순위만 두고 마감 시각 필드는 두지 않으므로, 요청 창구에서 받은 긴급도·기한을 순서 결정 입력으로 옮기는 규칙이 두 영역의 접점이 될 것으로 보인다. [추정][^ref-125]

### [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 다중 로봇 인터페이스 연구(Roldán 외, Sensors 2017-07-27)는 운영자 [상황 인식](../../glossary/situation-awareness.md)을 위한 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었으며, 이 연구의 몰입·예측 실험은 실험실 조건이다. [사실][^ref-1099]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): Open-RMF 작업 상태 스키마는 blocked·error·failed·delayed·canceled·killed 를 포함한 12개 상태 값과 작업에 걸린 중단(interruptions)·취소·강제 종료 요청 기록, 시작·종료 시각을 담는다(2026-10-09 확인). [사실][^ref-111] 그래서 실행 결과 확인과 이상 탐지가 같은 기록을 쓰는 것으로 보인다. [추정][^ref-111]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): Open-RMF 경보(Alert) 메시지는 심각도 등급(info 0·warning 1·error 2), 운영자가 고를 수 있는 응답 목록(responses_available), 관련 작업 id 를 담는다(2026-10-09 확인). [사실][^ref-448] 원인 판정 뒤의 운영자 선택이 이 메시지를 거쳐 복구 조치로 넘어가는 것으로 보인다. [추정][^ref-448]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 다중 로봇 수색·구조 과제 실험(Mehrotra·Sycara·Lewis·Chien·Wang, HFES 2011)은 경보 없음, 경보 자유 표시, 최상위 경보만 보이는 의사결정 보조의 세 조건을 비교했고, 자유 표시 조건의 운영자가 고장과 피해자를 더 빨리 탐지했으며 탐색 면적과 발견한 피해자 수에는 차이가 없었다(실험실 시뮬레이션 조건). [사실][^ref-1335] 경보 관리 표준으로는 ANSI/ISA 18.2-2016 이 공정 산업 시설에서 제어 시스템을 거쳐 운영자에게 표시되는 경보 전체의 수명주기 관리 원칙과 절차를 정하지만 이는 공정 산업 표준이며, 다중 로봇 플릿에 특화된 경보 관리 표준은 2026-10-09 조사에서 찾지 못했다. [사실][^ref-1333] 로봇 운영용 경보 관리 표준이나 지침이 있는지는 [열린 질문](../../open-questions.md)에 새로 올렸다.

### [I. 설계·시뮬레이션](../design-and-simulation/index.md)

이 대분류와의 연결은 현재 상태 표현이 아니라 기록 재현과 가정한 미래의 설계 쪽이다.

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md): Open-RMF 작업 이벤트 로그는 작업·단계·사건의 3계층으로 나뉘고 [MCAP](../../glossary/mcap.md) 은 시각 색인을 둔 기록 형식이어서 37. 관제 화면·실행 기록이 남긴 기록은 시간축 재현의 입력이 될 수 있어 보이지만, 이 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식은 확인되지 않았다. [추정][^ref-1094][^ref-1096] 변환 규칙은 열린 질문 oq-131 로 남아 있다.
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)(물류창고): AMR 물류센터 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼으며, 이는 시뮬레이션 결과다. [사실][^ref-102]

### [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하므로, 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다(2026-10-09 확인, 두 문서는 같은 프로젝트라 독립 출처가 아니다). [사실][^ref-762][^ref-302]
- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): ros2_tracing(Bédard·Lütkebohle·Dagenais, IEEE RA-L 2022)은 저부하 LTTng 추적기로 ROS 2 실행 정보를 모으며 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가가 평균 0.0033 ms 였다고 보고했는데, 이는 저자 실험값이고 독립 재현은 미확인이다. [사실][^ref-1032] 플랫폼 서비스 쪽 [분산 추적](../../glossary/distributed-tracing.md)(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모으므로, 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다. [추정][^ref-447][^ref-1032] 두 계층을 이은 공개 사례는 열린 질문 oq-210 으로 남아 있다.

### [L. AI·학습 기술](../ai-and-learning/index.md)

분류 원문의 교차 규칙은 장애 분석을 38. 모니터링·이상 탐지·원인 분석에 적용되는 AI 연구 방법으로 둔다.

- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 대규모 언어 모델로 로봇 실패를 설명하고 수정하는 REFLECT(2023) 같은 [실패 설명](../../glossary/failure-explanation.md) 연구가 두 영역을 잇는 예가 될 것으로 보인다. [추정][^ref-453]

### [M. 안전](../safety/index.md)

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): Winfield 외(2022-05-13)의 [윤리적 블랙박스](../../glossary/ethical-black-box.md) 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록하는 장치나 소프트웨어 모듈을 제안하며, 초안 표준은 논문 부속서에 토론용 초안으로 실렸다. [사실][^ref-1120] 초록에는 플릿·플랫폼 수준 기록에 대한 언급이 없다(부속서 본문은 열람하지 않음). [사실][^ref-1120] 플랫폼 수준의 최소 기록 항목은 열린 질문 oq-252 로 남아 있다.
- 연계 대상: [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): 40. 운영 절차·요청 창구 페이지는 로봇 교시·정비 작업 지침(산업안전보건기준에 관한 규칙 제222조)과 ANSI/A3 R15.08-3-2026 이 사용자에게 두는 운영 요구를 사업주·제조사 책임의 연계 대상으로 두므로, ROP는 요청·권한·기록 층으로 그 이행을 받쳐 주는 쪽인 것으로 보인다. [추정][^ref-1157][^ref-1153] 누가 이를 이행하는지는 열린 질문 oq-265 로 남아 있다.

### [N. 보안·개인정보](../security-and-privacy/index.md)

- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md): [사이버복원력법](../../glossary/cyber-resilience-act.md)은 2026-09-11부터 디지털 요소 제품의 제조자에게 실제 악용되는 취약점과 중대 보안 사고를 24시간 안에 조기 경보하게 하므로, 이상 탐지가 보안 사고를 가려내는 시점이 보고 의무와 맞물릴 가능성이 있으며 오케스트레이션 플랫폼의 제조자 해당 여부는 미확인이다. [추정][^ref-1228]
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)(물류창고): 창고 작업자 12명을 반구조화 면담한 연구(Malik·Brandão·Coopamootoo, 2026)는 로봇 운영에 따르는 데이터 감시에 대한 작업자 우려를 확인하고, 감시 활동 알림·개인정보 통제 같은 작업자 중심 요구를 제시했다. [사실][^ref-1226]
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md): Open-RMF API 서버(rmf-server)는 OpenID Connect 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정하며, 관리자는 모든 그룹에서 모든 동작을 할 수 있고 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다(2026-10-09 확인). [사실][^ref-762]

### [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)

- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [56. 운영 이관·확대·교육](../verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)(상업 시설): 중국 고급 호텔 직원 19명 면담 연구(Fu·Zheng·Wong, 2022)에서는 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육·동료 교육·고장 처리·고객 안내 같은 추가 업무가 직원의 사용 저항으로 이어졌다. [사실][^ref-1150] 운영 책임 조직과 교육의 연결은 열린 질문 oq-266·oq-278 로 남아 있다([역할 모호성](../../glossary/role-ambiguity.md) 참고).

### [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)

- 연계 대상: [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md): 국내 병원·약국은 2018-05-18 입고 내역부터 마약류 취급 내역을 마약류통합관리시스템에 전산 보고하고 종전 마약류 관리대장은 2년간 보관한다고 2018-07-13 보도되었으며, 법령 원문과 현행 여부는 미확인이다. [사실][^ref-1336] 로봇 배송 이력이 이 보고·보관 대상에 드는지는 열린 질문 oq-239 로 남아 있다.
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md): 한국 근로자참여법 제20조가 신기계·기술 도입과 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 두므로, 성과 측정이 개별 작업자의 처리량·위치까지 기록하면 도입 전 노동자 참여 절차가 필요할 가능성이 있으며 법적 해당 여부는 미확인이다. [추정][^ref-1220][^ref-1226]
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md)(병원): 병원 자율 배송 로봇(TUG) 민족지 연구(Mutlu·Forlizzi, HRI 2008)에서 내과 병동은 업무 중단에 대한 낮은 허용도, 비용과 이익의 불일치, 통행이 많은 곳의 주행 중단 때문에 직원 저항을 보였고, 산후 병동은 로봇을 업무 흐름에 통합했다. [사실][^ref-1151]

### [Q. 현장 유형별 적용](../site-type-applications/index.md)

Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고, 모든 현장에 공통인 운영·관제 기능은 J. 현장 운영·관제에 둔다. 이번 근거는 물류창고·제조 공장·병원·상업 시설에 한정되며 가정·실외·기타 현장의 근거는 없다.

- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): 국내 병원 현장에서 관제 시스템과 특수 물품 배송 이력 관리를 함께 개발하기로 한 협약이 2025-04-07 보도되었고, 37. 관제 화면·실행 기록 페이지가 찾은 현장 근거는 이 병원 사례 한 건뿐이다. [사실][^ref-1103]
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [61. 물류창고](../site-type-applications/warehouse.md): 로봇 이동형 풀필먼트 시스템 대기행렬 모델(Lamballais 외, 2017)에서는 처리량이 보관 구역 둘레의 작업대 위치에 영향을 받았으며, 이는 모델 연구로 현장 실측이 아니다. [사실][^ref-096] 협업형 AMR 피킹 해석 모델(Ghelichi·Kilaru, 2021)에서는 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우했으며, 이 역시 모델 연구로 현장 실측이 아니다. [사실][^ref-145]
- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [62. 제조 공장](../site-type-applications/manufacturing-plant.md): ISO 22400-2:2014 는 제조 운영 관리의 핵심성과지표 정의를 다루는 현행판이다. [사실][^ref-139] 에너지 관리 KPI 를 더한 개정 1(ISO 22400-2:2014/Amd 1:2017, 2017-04)이 있다. [사실][^ref-782] 개정판 ISO/DIS 22400-2 의 발행은 2026-09-26 확인 기준으로 확인되지 않았다. [사실][^ref-781] 이동로봇 플릿에 OEE 를 적용하는 합의된 정의는 열린 질문 oq-016 으로 남아 있다.
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다고 보도되었으며, 이는 2024년 보도 기준이고 두 보도가 병원 발표에서 나왔을 수 있어 독립 확인으로 보지 않는다. [사실][^ref-1199][^ref-944]
- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [64. 상업 시설](../site-type-applications/commercial-facilities.md): 미국 뉴욕 알로프트 호텔에서는 투숙객이 전화로 프런트에 요청하면 사람이 주문 물건과 객실 번호를 확인해 처리했고, 배송 로봇(Savioke Relay)은 객실 앞에 도착하면 객실 전화로 자동 알림을 보냈다(2017-04-18 보도). [사실][^ref-1152]

### 아직 다루지 않은 연결

- [B. 로봇 온톨로지](../robot-ontology/index.md) 전체(4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리): 게시된 페이지에 J. 현장 운영·관제와 잇는 근거가 없다.
- 이번 근거가 없는 세부영역: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터.
- Q. 현장 유형별 적용 가운데 65. 가정·공동주택, 66. 실외, 67. 기타 현장과의 연결 근거는 없다.

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System, 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-10-09 (원문 미열람)
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-10-09 (원문 미열람)
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-09
[^ref-139]: ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 2014, https://www.iso.org/standard/54497.html, 접근일 2026-10-09 (원문 미열람)
[^ref-140]: ASCM, SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment, 미확인, https://scor.ascm.org/performance/reliability/RL.1.1, 접근일 2026-10-09 (원문 미열람)
[^ref-145]: Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers, 2021, https://www.sciencedirect.com/science/article/pii/S0307904X20305801, 접근일 2026-10-09 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-10-09 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-09
[^ref-302]: Open Robotics (open-rmf), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-10-09 (원문 미열람)
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-10-09
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09
[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09
[^ref-453]: Liu, Z., Bahety, A., & Song, S., REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023, https://arxiv.org/abs/2306.15724, 접근일 2026-10-09 (원문 미열람)
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-10-09 (원문 미열람)
[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-10-09
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-781]: ISO, ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 미확인, https://www.iso.org/standard/87563.html, 접근일 2026-09-26 (원문 미열람)
[^ref-782]: ISO, ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management, 2017-04, https://www.iso.org/standard/68295.html, 접근일 2026-09-26 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)
[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-10-09 (원문 미열람)
[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-10-09
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-09 (원문 미열람)
[^ref-1098]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-10-09 (원문 미열람)
[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-10-09 (원문 미열람)
[^ref-1103]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-10-09 (원문 미열람)
[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-10-09 (원문 미열람)
[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-10-09 (원문 미열람)
[^ref-1152]: 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인), 2017-04-18, https://www.hankookilbo.com/news/article/201704180418820469, 접근일 2026-10-09 (원문 미열람)
[^ref-1153]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-10-09 (원문 미열람)
[^ref-1154]: Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged, 2026-06-09, https://www.proofnews.org/moxi/, 접근일 2026-10-09 (원문 미열람)
[^ref-1157]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-10-09 (원문 미열람)
[^ref-1199]: ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-10-09 (원문 미열람)
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-10-09 (원문 미열람)
[^ref-1220]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-10-09 (원문 미열람)
[^ref-1226]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-10-09 (원문 미열람)
[^ref-1333]: ISA (ANSI Webstore 게재), ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries, 2016, https://webstore.ansi.org/standards/isa/ansiisa182016, 접근일 2026-10-09
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09
[^ref-1334]: TechTarget (Hannah Nelson, Xtelligent Healthcare Media), Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout, 2022-08-11, https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout, 접근일 2026-10-09
[^ref-1335]: Mehrotra, S., Sycara, K., Lewis, M., Chien, S.-Y., & Wang, H. (Proceedings of the Human Factors and Ergonomics Society), Effects of alarms on control of robot teams, 2011, https://d-scholarship.pitt.edu/12400/, 접근일 2026-10-09
[^ref-1336]: 데일리팜 (김지은), 마약통합시스템 시행 2개월…병원·약국 다빈도 질문은, 2018-07-13, https://dailypharm.com/user/news/85066, 접근일 2026-10-09

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 91건이다(논문 31건 · 기사·보고서 14건 · 업체 발표 5건 · 표준·오픈소스·기관 자료 41건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-455](../../references/ref-455.md) — DBpia 게재 논문(저자 미확인), 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 (발행 2026-07)
- [ref-1226](../../references/ref-1226.md) — Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety (발행 2026)
- [ref-102](../../references/ref-102.md) — Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics (발행 2025)
- [ref-454](../../references/ref-454.md) — International Journal of Production Research(Taylor & Francis), 저자 미확인, Process mining in supply chain management: state-of-the-art, use cases and research outlook (발행 2024)
- [ref-146](../../references/ref-146.md) — Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority (발행 2024)
- [ref-453](../../references/ref-453.md) — Liu, Z., Bahety, A., & Song, S., REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction (발행 2023)
- [ref-115](../../references/ref-115.md) — Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes (발행 2023)
- [ref-1319](../../references/ref-1319.md) — Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv), Predictive Object-Centric Process Monitoring (발행 2022-07-20)
- [ref-1032](../../references/ref-1032.md) — Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 (발행 2022-07)
- 그 밖에 21건

**기사·보고서**

- [ref-1154](../../references/ref-1154.md) — Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged (발행 2026-06-09)
- [ref-1007](../../references/ref-1007.md) — 뉴스토마토 (이규하), 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 (발행 2025-04-23)
- [ref-1103](../../references/ref-1103.md) — 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 (발행 2025-04-07)
- [ref-141](../../references/ref-141.md) — WERC(Warehousing Education and Research Council), WERC DC Measures Survey - 2025 (발행 2025)
- [ref-1199](../../references/ref-1199.md) — ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인) (발행 2024-09-19)
- [ref-976](../../references/ref-976.md) — 정보통신신문 (김연균), 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ (발행 2024-07-18)
- [ref-1316](../../references/ref-1316.md) — 코메디닷컴, [메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠 (발행 2024-04-20)
- [ref-944](../../references/ref-944.md) — 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (발행 2024-04-15)
- [ref-1317](../../references/ref-1317.md) — 바이라인네트워크 (이진호), 뉴빌리티, 실외이동 로봇 운행안전 인증 획득 (발행 2024-01-31)
- [ref-1334](../../references/ref-1334.md) — TechTarget (Hannah Nelson, Xtelligent Healthcare Media), Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout (발행 2022-08-11)
- 그 밖에 4건

**업체 발표**

- [ref-1315](../../references/ref-1315.md) — LG CNS (LG 미디어 보도자료), ‘로봇 통합운영 플랫폼’ 개발 (발행 2023-07-06)
- [ref-1156](../../references/ref-1156.md) — OMRON Industrial Automation Europe, Autonomous Mobile Robots (AMR) (발행 미확인)
- [ref-1102](../../references/ref-1102.md) — 네이버클라우드, ARC brain 개요 - 사용 가이드 (발행 미확인)
- [ref-1101](../../references/ref-1101.md) — 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON) (발행 미확인)
- [ref-1097](../../references/ref-1097.md) — Foxglove, Playback — Foxglove Documentation (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-1228](../../references/ref-1228.md) — European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations (발행 2026-09-11)
- [ref-1157](../../references/ref-1157.md) — 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등) (발행 2025-09-01)
- [ref-1314](../../references/ref-1314.md) — European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 26: Obligations of deployers of high-risk AI systems (발행 2024-07-12)
- [ref-1313](../../references/ref-1313.md) — European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 19: Automatically generated logs (발행 2024-07-12)
- [ref-863](../../references/ref-863.md) — European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) (발행 2024-06-13)
- [ref-1312](../../references/ref-1312.md) — IEEE Standards Association, How To Make Autonomous Systems More Transparent and Trustworthy (발행 2022-05-11)
- [ref-1220](../../references/ref-1220.md) — 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) (발행 2019-04-16)
- [ref-782](../../references/ref-782.md) — ISO, ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management (발행 2017-04)
- [ref-1333](../../references/ref-1333.md) — ISA (ANSI Webstore 게재), ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries (발행 2016)
- [ref-139](../../references/ref-139.md) — ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions (발행 2014)
- 그 밖에 31건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) — 5절 현장 사례를 6건(병원 2·물류창고·실외·가정·기타)으로 늘리고 '찾지 못했다' 문장 교체, 7절에 VDA 5050 동작 상태·오류 수준·logReport, MassRobotics 운용 상태, Open-RMF 배차·개입 기록, ISO 11064, IEEE 7001-2021, 윤리적 블랙박스 초안 행 추가와 rmf-web 행 갱신, 9절에 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계 추가, 11절 oq-237 해결·부분 근거·새 질문 2건, 13절 각주 갱신 (실행 2026-10-09-15)
- 2026-10-09 · 생성 · [37. 관제 화면·실행 기록 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area37-s7.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "7. 관련 표준·프레임워크·오픈소스" 절(2,936자)을 옮겼다 (실행 2026-10-09-15)
- 2026-10-09 · 생성 · [37. 관제 화면·실행 기록 — 열린 질문](../../topics/2026/2026-10-09-area37-s11.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "11. 열린 질문" 절(2,787자)을 옮겼다 (실행 2026-10-09-15)
- 2026-10-09 · 생성 · [37. 관제 화면·실행 기록 — 왜 중요한가](../../topics/2026/2026-10-09-area37-s3.md) — 자동 분리: 37. 관제 화면·실행 기록 의 "3. 왜 중요한가" 절(485자)을 옮겼다 (실행 2026-10-09-15)
- 2026-10-09 · 요약 · [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) — 37. 관제 화면·실행 기록: 갱신: 5절 현장 사례 6건(병원 2·물류창고·실외·가정·기타), 7절 VDA 5050·MassRobotics 상태 값 규약·ISO 11064·IEEE 7001-2021·윤리적 블랙박스 초안 추가와 rmf-web 저장 설정 갱신, 9절 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계, 11절 oq-237 해결·새 질문 2건 (실행 2026-10-09-15)
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

### templates/topic.md

```markdown
---
title: "{{title}}"                          # 주제 제목. 질문형 또는 명사구. 예: "로봇 도착과 작업 대상 인계 확인은 어떻게 다른가"
type: topic
category: "{{category}}"                    # 주 연구영역이 속한 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
primary_area_no: {{primary_area_no}}        # 주 연구영역 번호(1~67). 반드시 하나
track: {{track_slug}}                       # 트랙 실행에서 나온 주제 페이지만. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition. 아니면 이 줄을 뺀다
related_areas: [{{related_areas}}]          # 관련 영역 번호 0개 이상. 예: [18, 29]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개
status: {{status}}                          # draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜
version: {{version}}                        # 정수. 신규 1, 갱신마다 +1
---
<!--
[템플릿] 주제 페이지 (type: topic)
경로: docs/topics/YYYY/YYYY-MM-DD-slug.md  (YYYY-MM-DD 는 생성한 실행 날짜, slug 는 영문 소문자·하이픈)
쓰임: 파이프라인 2주기부터의 주제 조사 실행, 세부영역 페이지가 4,000자를 넘어 분리한 글, 트랙 실행에서 하나의 질문을 깊게 다룬 글. 하루 신규 주제 페이지 상한은 daily_budget.new_topic_pages 를 따른다.
필수: 주 연구영역 하나(primary_area_no)와 0개 이상의 관련 영역. 트랙 실행에서 나온 페이지는 프런트매터에 track 을 넣고, 해당 트랙 단계 페이지의 3절(조사 결과)에서 이 페이지를 링크한다.
분량: 1~7절 텍스트 합계(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 1,500~2,500자.
서사 골격: 왜 중요한가 → 현장에서 무슨 일이 벌어지는가(현장 유형을 밝힌 적용 사례) → 무엇이 알려져 있는가(검증된 사실) → ROP는 무엇을 맡고 무엇을 연계하는가 → 다른 영역과 어떻게 이어지는가 → 아직 모르는 것.
브리프의 발견 사항(finding)만 쓴다. 새 사실을 더하지 않는다. 필요한 사실이 브리프에 없으면 본문에 넣지 않고 pages.json 의 additional_research_requests 에 기록한다.

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

[경로 규약] 이 페이지에서 홈은 ../../index.md, 주제 목록은 ../index.md, 세부영역 페이지는 ../../categories/<대분류 slug>/<파일>, 대분류 페이지는 ../../categories/<대분류 slug>/index.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 트랙은 ../../tracks/<트랙 slug>/<파일>.md 이다.
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
[홈](../../index.md) › [주제](../index.md) › {{title}}

# {{title}}

**주 연구영역:** [{{primary_area_no}}. {{primary_area_name}}](../../categories/{{category_slug}}/{{area_file}}.md) · **관련 영역:** {{related_area_links_or_없음}} · **실행:** {{run_id}}
<!-- 관련 영역 링크는 "[18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)" 형식으로 쉼표 구분. 트랙 페이지면 "· **트랙:** [트랙 이름](../../tracks/<트랙 slug>/index.md) 단계 n" 을 덧붙인다(예: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)). -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 새 페이지에는 빈 마커 두 줄만 둔다. -->

## 1. 세 줄 요약

- {{summary_line_1}}
- {{summary_line_2}}
- {{summary_line_3}}
<!-- 정확히 세 줄. 각 줄은 한 문장. 첫 줄은 무엇을 밝혔는가, 둘째 줄은 ROP 운영에 무엇을 뜻하는가, 셋째 줄은 무엇이 아직 확인되지 않았는가. 요약에도 핵심 주장에는 태그를 붙인다. -->

## 2. 배경

{{background}}
<!--
어느 연구영역의 어떤 질문에서 출발했는지 쓴다. 주 연구영역의 원문 "핵심 질문"을 인용하면 그대로 옮기고 [분류원문] 을 붙인다. 출발점이 열린 질문(oq-NNN)이나 트랙 백로그 질문(q1-01), 정정 요청, priority.yaml 의 우선 주제이면 그 id 와 링크를 적는다. 1~2단락.
-->

## 3. 본문

### {{subheading_1}}

{{body_1}}

### {{subheading_2}}

{{body_2}}
<!--
소제목은 자유(2~5개). 주장마다 태그·각주. 검증된 발견 사항만 쓰고 순서는 서사 골격을 따른다. 출처가 충돌하면 둘 다 제시하고 7절 열린 질문에 올린다.
표·그림 복제 금지. 도식이 필요하면 mermaid 로 그리고 도식 안에서도 이름을 쓴다. 벤더 주장은 [추정]에 "벤더 주장" 병기. 조건부 승인의 수정 목록을 모두 반영하고 pages.json 의 fixes_applied 에 표시한다.
-->

## 4. 현장 시나리오

**현장 유형:** {{site_types}}

**사례:** {{case_title}}

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
절 제목 "4. 현장 시나리오"는 파이프라인(pipeline/lib/validate.py)이 쓰는 고정 문자열이므로 바꾸지 않는다. 내용은 분류 원문 21장의 방법대로 쓴다: 현장 유형(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 하나를 명시하고, 여섯 항목(시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가 / 수행 자원 / 제약 / 완료·인계 / 예외·성과)을 채운다. 물류창고는 일곱 현장 유형 가운데 하나이므로 기본값으로 쓰지 않는다. 이 주제와 직접 관련 없는 항목은 "해당 없음"으로 둔다. 실제 사례는 출처 각주와 함께, 설명용 가상 사례이면 첫 문장에 밝히고 지어낸 수치는 쓰지 않는다. 다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 낸다.
-->

## 5. ROP 관점의 시사점

**직접 범위:**
{{direct_scope_implications}}

**연계 범위:**
{{external_scope_implications}}
<!-- 분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 경계를 기준으로 ROP가 직접 맡는 것과 외부와 연계하는 것을 나누어 쓴다. 각 항목은 목록으로, 주장마다 태그·각주. 외부 연계 영역을 ROP 직접 범위처럼 쓰지 않는다. -->

## 6. 연결되는 연구영역

{{connected_areas}}
<!-- 목록 형식: "- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 연결 이유 한 문장". 주 연구영역을 첫 줄에, 관련 영역을 그 아래에. 번호와 이름을 함께 쓴다. 여기 적은 번호는 프런트매터 primary_area_no·related_areas 와 일치시킨다. AI를 다루면 27. AI·학습·적응과 모델 운영을 함께 연결한다. -->

## 7. 열린 질문

{{open_questions}}
<!-- 목록 형식: "- **oq-012** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 이 글에서 새로 생긴 질문과 답한(해결한) 질문을 나누어 적고, 해결한 질문에는 답이 있는 절을 표시한다. 트랙 질문(q1-01)은 트랙 백로그 링크만 둔다. pages.json 의 open_question_updates 로도 낸다. 없으면 "없음"과 이유. -->

## 8. 출처

{{footnotes}}
<!-- 각주 정의만 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". 본문의 각주와 프런트매터 sources 를 일치시킨다. 새 출처는 pages.json 의 reference_updates 로도 낸다. -->

## 9. 검증 노트

- 판정: 1차 {{first_verdict}} / 2차 {{second_verdict}}
- 확인·미확인: 확인 {{confirmed_count}}건 · 미확인 {{unconfirmed_count}}건 · 교차 확인 {{cross_checked_count}}건
- 강등된 주장: {{downgraded_claims_or_없음}}
- 검증자 주의: {{verification_note}}
- 신뢰도: {{confidence}}
<!-- 내용 검증 에이전트의 verification.json 에서 옮긴다. 판정 값: 1차 = 승인 | 조건부 승인 | 반려, 2차 = 통과 | 수정 후 재검증 | 불통과. 강등된 주장은 finding id 와 "사실 → 추정" 같은 변경을 적는다. "검증자 주의"는 verification_note 문구를 그대로 쓴다. 스토리텔러는 여기에 자기 의견을 넣지 않는다. -->

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| {{date}} | {{run_id}} | {{change_summary}} | {{version}} |
<!-- 신규 작성은 "신규 작성". 갱신마다 한 행을 위에 추가하고 프런트매터 version 을 올린다. 정정 요청을 반영했으면 corr-NNN id 를 적는다. -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 10건 / 전체 1324건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 2026-09-25 | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 2026-09-25 | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 2026-09-25 | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 2026-09-25 | 예 |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | https://github.com/ros/diagnostics/blob/ros2/README.md | 2026-09-25 | 예 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 2026-09-25 | 예 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 2026-09-25 | 예 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 2026-09-25 | 예 |
| ref-451 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 377개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
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
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
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
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
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

### docs/open-questions.md (요약: 대상 영역 [38] 에 걸린 16건 / 전체 333건)

```markdown
- oq-018 [열림] 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? (영역 38, 39)
- oq-033 [열림] Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 29, 38)
- oq-072 [열림] 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? (영역 31, 38)
- oq-073 [열림] VDA 5050 3.0.0 판의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 이전 판(2.x)의 오류 수준이 다를 때, 두 판이 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? (영역 20, 38)
- oq-074 [열림] 물류 로봇 작업 지연을 로봇·설비·통신·공정 원인으로 나누는 공개 원인 분류 체계나 현장 데이터셋이 있는가? (영역 38, 39)
- oq-075 [열림] 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? (영역 32, 38)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 25, 38, 51)
- oq-194 [열림] 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? (영역 67, 23, 38)
- oq-210 [열림] 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? (영역 43, 38)
- oq-221 [열림] 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? (영역 46, 38)
- oq-240 [열림] 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? (영역 37, 38)
- oq-252 [열림] 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? (영역 50, 37, 38)
- oq-295 [열림] 다중 로봇 플릿 관제에서 경보 우선순위, 경보 홍수 기준, 경보 합리화 절차를 ANSI/ISA 18.2 처럼 정한 로봇 운영용 경보 관리 표준이나 공개 지침이 있는가? (영역 38, 31)
- oq-312 [열림] 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? (영역 48, 38, 54)
- oq-315 [열림] 언어 모델 기반 고장 진단(REFLECT, SYSDIAGBENCH)을 제조사가 다른 이동로봇 플릿의 실행 기록·오류 코드에 적용해 원인 분석 정확도를 측정한 사례가 있는가? (영역 47, 38, 44)
- oq-319 [열림] 로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? (관련: oq-082) (영역 52, 18, 38)
```

### docs/standards/index.md (요약: 331개 — 이름 · 종류 · 발행 기관)

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
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
- ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) · ISO (ISO/TC 299 Robotics) · 표준
- ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) · ISO (ISO/TC 178 Lifts, escalators and moving walks) · 표준
- 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 · 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) · 표준
- Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_obstacle (사람 검출·lane_blocker) · Open Robotics (open-rmf) · 오픈소스
- Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) · Pasch, F. 외 (Intel Labs 외) · 오픈소스
- RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) · Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. · 프레임워크
- ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 · ISO · 표준
- IEEE 7001-2021 자율 시스템 투명성 표준 · IEEE Standards Association · 표준
```

### runs/2026-10-09-16/docs_tree.txt

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
glossary/3d-scene-graph.md
glossary/4d-scene-graph.md
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/actively-exploited-vulnerability.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-recording-of-events.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/average-displacement-error.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
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
glossary/cloud-robotics.md
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
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/door-to-door-robot-delivery.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
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
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/integrity-risk.md
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
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lease-expiry.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/management-of-change.md
glossary/map-alignment.md
glossary/map-distribution.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/online-simulation.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry-genai-semantic-conventions.md
glossary/opentelemetry.md
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
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/persistence-filter.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/precision-time-protocol.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-attestation.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-tracing.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/safety-guardrail.md
glossary/safety-state-report.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/slotcar.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/surrogate-model.md
glossary/synchronization-loss.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/wireless-safety-rated-emergency-stop.md
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
logs/daily/2026-10-09.md
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
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-1239.md
references/ref-124.md
references/ref-1240.md
references/ref-1241.md
references/ref-1242.md
references/ref-1243.md
references/ref-1244.md
references/ref-1245.md
references/ref-1246.md
references/ref-1247.md
references/ref-1248.md
references/ref-1249.md
references/ref-125.md
references/ref-1250.md
references/ref-1251.md
references/ref-1252.md
references/ref-1253.md
references/ref-1254.md
references/ref-1255.md
references/ref-1256.md
references/ref-1257.md
references/ref-1258.md
references/ref-1259.md
references/ref-126.md
references/ref-1260.md
references/ref-1261.md
references/ref-1262.md
references/ref-1263.md
references/ref-1264.md
references/ref-1265.md
references/ref-1266.md
references/ref-1267.md
references/ref-1268.md
references/ref-1269.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-1272.md
references/ref-1273.md
references/ref-1274.md
references/ref-1275.md
references/ref-1276.md
references/ref-1277.md
references/ref-1278.md
references/ref-1279.md
references/ref-128.md
references/ref-1280.md
references/ref-1281.md
references/ref-1282.md
references/ref-1283.md
references/ref-1284.md
references/ref-1285.md
references/ref-1286.md
references/ref-1287.md
references/ref-1288.md
references/ref-1289.md
references/ref-129.md
references/ref-1290.md
references/ref-1291.md
references/ref-1292.md
references/ref-1293.md
references/ref-1294.md
references/ref-1295.md
references/ref-1296.md
references/ref-1297.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
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
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
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
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
topics/2026/2026-10-09-area18-s10.md
topics/2026/2026-10-09-area18-s11.md
topics/2026/2026-10-09-area18-s6.md
topics/2026/2026-10-09-area18-s7.md
topics/2026/2026-10-09-area18-s8.md
topics/2026/2026-10-09-area19-s10.md
topics/2026/2026-10-09-area19-s11.md
topics/2026/2026-10-09-area19-s6.md
topics/2026/2026-10-09-area19-s7.md
topics/2026/2026-10-09-area19-s8.md
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

### runs/2026-10-09-16/pages.json

```json
{
  "run_id": "2026-10-09-16",
  "outline": [
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1500,
      "summary": "이종 로봇의 보고 어휘·심각도·시각 형식이 표준마다 달라 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111] 통신 단절 신호와 사람 개입·대기 표시도 원인 구분의 재료가 될 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-111]",
      "planned_findings": [
        "f9",
        "f13",
        "f14",
        "f15"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3200,
      "summary": "물류창고 가상 사례(2026-10-09 원문 재확인)에 병원·상업 시설·실외·기타 현장 사례를 더했다. 병원 의약품 배송 로봇은 승강기 가동률이 높은 구간에 실패가 몰렸다. [추정][^ref-943]",
      "planned_findings": [
        "f7",
        "f8",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1700,
      "summary": "VDA 5050 state·connection 스키마, MassRobotics 상태 보고, Open-RMF 작업 상태·경보, OpenTelemetry 가 원인 분석에 쓰는 필드를 2026-10-09 원문으로 정리했다. [사실][^ref-051][^ref-449][^ref-230][^ref-111][^ref-448][^ref-447]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f11",
        "f12"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1300,
      "summary": "ROS 2 diagnostics 같은 로봇 내부 진단과 문·승강기 제어, 실외 인증 판단은 연계 대상이고, ROP 는 표준 보고를 원인 범주로 구분하고 심각도 대응·작업 식별자 연결을 맡을 후보로 보인다. [추정][^ref-445][^ref-031][^ref-447]",
      "planned_findings": [
        "f10",
        "f9",
        "f12",
        "f16",
        "f19"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "section": "11. 열린 질문",
      "budget_chars": 900,
      "summary": "oq-033·oq-073·oq-210 에 부분 근거를 더하고 oq-074·oq-075 는 열린 채로 두며, 심각도 부여 기준과 headerId 결번 판정 기준을 새 질문으로 올렸다. [추정][^ref-031][^ref-448][^ref-230]",
      "planned_findings": [
        "f9",
        "f12",
        "f13"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3절 둘째 문단을 현재 원문 질문에 맞추고 심각도·시각 형식·통신 신호·사람 개입 근거 보강, 5절 현장 유형별 사례(병원·상업 시설·실외·기타) 추가와 물류창고 사례 재확인, 7절 표준 필드 표 추가, 9절 내부 진단·승강기·실외 인증 경계와 직접 범위 후보 추가, 11절 부분 근거·새 질문 2건, 13절 각주 접근일·기관 표기 갱신",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "content": "이종 로봇이 섞인 현장에서는 로봇 오류 수준·연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 작업 지연·차단과 문 모드(Open-RMF)가 서로 다른 어휘로 보고되므로, 지연 원인을 가리려면 이들을 같은 시간축에 맞추고 ROP 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111]\n\n2절의 질문, 곧 지연의 원인이 로봇인지 설비인지 통신인지 앞 작업인지를 가리는 일은 복구 담당과 조치를 정하는 출발점이다. 그런데 각 표준은 자기 필드만 정의하고 서로 간 대응표는 두지 않으며, 이번 조사에서는 공통 매핑 표준을 찾지 못했다(열린 질문 oq-033). [추정][^ref-051][^ref-230][^ref-111] 심각도 표현만 보아도 VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록이어서, 이종 플릿의 이상을 한 경보 체계로 모으려면 ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다(oq-033·oq-073 부분 근거). [추정][^ref-031][^ref-448][^ref-230]\n\n같은 시간축에 맞추는 일도 간단하지 않다. 시각 표현이 VDA 5050 은 밀리초까지의 ISO 8601 문자열, MassRobotics 는 date-time 문자열, Open-RMF 작업 상태는 밀리초 유닉스 시각 정수로 서로 다르다(2026-10-09 확인). [사실][^ref-051][^ref-230][^ref-111]\n\n통신 원인을 따로 가리는 신호도 표준 안에 있다. VDA 5050 의 headerId 는 토픽마다 보낸 메시지마다 1씩 늘어나므로 수신 쪽에서 번호가 건너뛰면 메시지 유실을 의심할 수 있고, 연결 상태(CONNECTION_BROKEN·HIBERNATING)와 함께 보면 상태 보고가 끊긴 원인이 통신인지 로봇 쪽의 의도된 통신 감축인지 가르는 근거가 될 것으로 보이나, 결번 판정 기준은 명세에 없다. [추정][^ref-051][^ref-449]\n\n사람이 관여한 지연도 따로 볼 만하다. VDA 5050 운용 모드의 INTERVENED·MANUAL, MassRobotics 운용 상태의 manualOverride(수동 조작)와 waitingHumanEvent(사람 사건 대기)가 있고, Open-RMF 작업 기록이 일시정지·재개 요청과 그 요청 출처 라벨을 남기므로, 지연 원인 범주에 로봇·설비·통신·앞 작업 외에 사람 개입·대기를 따로 두는 편이 판정에 유리할 것으로 보인다. [추정][^ref-051][^ref-230][^ref-111]\n\n원인 구분은 처리량 관리와도 이어진다. 무인운반차(Automated Guided Vehicle, AGV) 시스템을 다룬 2003년 연구는 기존 두 방법(가동률·대기 시간 기반)에는 이동 병목 탐지와 비교해 여러 한계가 있다고 보고한다. [사실][^ref-451] 어느 설비·로봇이 흐름을 막는지 판정하는 방식에 따라 개선 대상이 달라질 수 있다는 뜻이다."
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "이 절은 지연·정지의 원인을 가리는 일이 현장 유형마다 어떻게 드러나는지를 사례로 보인다. 물류창고 사례는 설명용 가상 사례이고, 병원·상업 시설·실외·기타 현장 사례는 공개 연구·보도에 기댄 것이다. 사례마다 이번 근거로 채우지 못한 항목은 '미확인'으로 두었고, 제조 공장의 이상 탐지·원인 분석 사례는 이번 조사에서 찾지 못함.\n\n### 물류창고\n\n**현장 유형:** 물류창고\n\n**사례:** 보충 단계 — 보충용 박스를 운반하던 AMR 이 문 앞에서 멈춰 보충이 늦어진 원인 가리기\n\n이 사례는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 가상 사례이며, 문 모드·문 어댑터·작업 상태·경보 서술은 2026-10-09 원문으로 다시 확인했다.\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 피킹 구역 재고가 보충 기준 아래로 내려가 보충 작업이 생성된다(가상 설정). |\n| 작업 대상 | 예비 보관 구역에서 피킹 구역으로 옮길 보충용 박스와 이를 실은 자율이동로봇(AMR). |\n| 수행 자원 | AMR 은 운반, 문 설비는 개폐, ROP 는 상태 수집과 원인 구분, 운영자는 경보 응답을 맡는다. 문 개폐 제어 자체는 연계 대상(시설·설비 제어)이며 ROP 는 문 상태 확인과 문 요청만 다룬다. |\n| 제약 | 경로가 문을 지나야 한다. Open-RMF 에서 문 노드는 문 상태를 /door_states 로 발행하고 문 모드는 closed·moving·open·offline·unknown 다섯 값이다(2026-10-09 재확인). [사실][^ref-313][^ref-283] 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다. [사실][^ref-283] |\n| 완료·인계 | 작업 상태가 completed 로 바뀌고 보충 위치 도착이 확인되면 보충 완료로 본다. 작업 상태 토큰 completed 는 Open-RMF 작업 상태 스키마에 있다. [사실][^ref-111] |\n| 예외·성과 | 작업 상태가 delayed 또는 blocked 로 바뀌고 [사실][^ref-111], MassRobotics 운용 상태가 waitingExternalEvent 를 보고하며 [사실][^ref-230], 경보는 심각도 등급(INFO·WARNING·ERROR)·응답 목록·관련 작업 id 를 담아 운영자에게 간다(2026-10-09 재확인). [사실][^ref-448] 이 신호들을 맞춰 원인을 문·로봇·통신 중 하나로 판정하는 절차는 추정이다. [추정][^ref-313][^ref-111][^ref-230] |\n\n다음은 설명을 위한 가상의 시나리오이다. 보충 작업을 받은 AMR 이 문 앞에서 멈추고, ROP 에는 작업 지연과 외부 사건 대기가 함께 들어온다. 수치는 쓰지 않는다.\n\nROP 는 같은 시각의 문 모드를 확인한다. 문 모드가 offline 이나 unknown 이면 설비 쪽 원인일 가능성을, 문이 open 인데도 로봇이 대기 중이면 로봇 쪽 원인일 가능성을 먼저 살피는 식으로 판정 순서를 세울 수 있어 보인다. [추정][^ref-313][^ref-230] 로봇 연결이 CONNECTION_BROKEN 으로 끊겼다면 통신 원인을 따로 볼 수 있다. [추정][^ref-449]\n\n원인 범주가 정해지면 경보의 응답 목록으로 운영자가 조치를 고르고, 복구 방식은 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)으로 넘어간다. 현장 유형 매트릭스 전체는 [현장 유형 매트릭스](../../site-matrix.md)에 있다.\n\n### 병원\n\n**현장 유형:** 병원\n\n**사례:** 의약품 배송 로봇의 승강기 호출·탑승과 승강기 혼잡\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 미확인 |\n| 작업 대상 | 로봇이 배송하는 의약품. [추정][^ref-943] |\n| 수행 자원 | 의약품 배송 로봇이 승강기를 호출해 탑승한다. [추정][^ref-943] 승강기 운행 제어 자체는 연계 대상(시설·설비 제어)이다. 다른 병원 사례로, 한림대학교성심병원은 보도 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리한다(2024-04-15 보도). [사실][^ref-944] |\n| 제약 | 미확인 |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 고려대학교 구로병원 연구(2026-03-31 게재)에서 승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다. [추정][^ref-943] |\n\n이 결과를 설비(승강기) 혼잡이 지연·실패의 원인으로 드러난 것으로 읽는 것은 해석이며, 전체 성공률의 분모는 미확인이다. [추정][^ref-943] 승강기 운행 제어는 연계 대상이고, ROP 몫은 승강기 상태를 원인 범주(설비)에 반영하는 데까지로 보인다. [추정][^ref-943]\n\n한림대학교성심병원 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다. [사실][^ref-944] 이 부재 진술은 보도 한 건에 기댄 것이다.\n\n### 상업 시설\n\n**현장 유형:** 상업 시설\n\n**사례:** 호텔 로봇이 단순 업무를 처리하지 못해 사람 일이 늘어난 사례(일본 헨나 호텔)\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 미확인 |\n| 작업 대상 | 투숙객의 기본 질문, 여권 복사 같은 업무. [사실][^ref-961][^ref-962] |\n| 수행 자원 | 객실 음성 비서 로봇, 짐 운반 로봇, 프런트 로봇과 호텔 직원. [사실][^ref-961][^ref-962] |\n| 제약 | 미확인 |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 로봇이 이런 업무를 사람 개입 없이는 처리하지 못해 사람의 일을 늘렸고, 호텔은 로봇 일부(보도 기준 절반가량)를 철수했다(2019-01 보도 기준). [사실][^ref-961][^ref-962] |\n\n공개 기록은 실패 현상과 철수만 전하며, 시작 조건·제약·완료·인계는 이번 근거로 확인하지 못했다.\n\n### 실외\n\n**현장 유형:** 실외\n\n**사례:** 실외이동로봇 운행안전인증과 관제장치\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 미확인 |\n| 작업 대상 | 미확인 |\n| 수행 자원 | 미확인 |\n| 제약 | 실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 한다(2026-10-09 확인). [사실][^ref-980] 그래서 실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 될 것으로 보인다. [추정][^ref-980] |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 미확인 |\n\n운행 안전 인증 판단은 인증 기관·운영자 쪽 연계 대상이며, ROP 는 이 조건을 실외 현장의 감시·운영 제약으로 반영하는 쪽에 설 것으로 보인다. [추정][^ref-980] 관제장치 항목의 세부 요건은 미확인이다.\n\n### 기타\n\n**현장 유형:** 기타\n\n**사례:** 노르웨이 Northern Lights 시설의 4족 점검 로봇 운영(Equinor)\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다(2025-11-21 보도). [사실][^ref-995] |\n| 작업 대상 | 계기 값, 밸브 위치, 가스 누출 같은 설비 상태. [사실][^ref-995] |\n| 수행 자원 | 4족 점검 로봇과 현장 운영자가 맡는다. [사실][^ref-995] 계기 판독·가스(누출) 탐지는 로봇 인식 기능이라 연계 대상이다. |\n| 제약 | 미확인 |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 미확인 |\n\nROP 쪽 몫은 이 점검 결과를 설비 이상 판정의 입력으로 받는 부분으로 보인다. [추정][^ref-995] 점검 결과가 설비 보전 시스템의 작업 지시·점검 기록으로 돌아가는 형식은 열린 질문 oq-194 로 남아 있다.\n\n### 제조 공장\n\n제조 공장의 이상 탐지·원인 분석 적용 사례는 이번 조사에서 찾지 못함."
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "6절의 접근은 아래 표준·오픈소스가 정의한 필드와 신호를 재료로 쓴다. VDA 5050 은 3.0.0 판(GitHub main 브랜치, 접근일 2026-10-09) 기준이며 main 브랜치는 판이 바뀔 수 있다. [사실][^ref-051]\n\n자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area19-s7.md)에 있다.\n\n### 2026-10-09 원문 재확인으로 더한 필드\n\n| 이름 | 유형 | 이 영역과의 관계 | 출처 |\n|---|---|---|---|\n| VDA 5050 state 스키마 | 표준 | 로봇의 활성 오류 전체를 담는 errors 배열, 운용 모드(operatingMode), 안전 상태(safetyState)를 필수 항목으로 두고, 운용 모드 값을 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 가지로 정한다. [사실][^ref-051] 로봇이 보내는 부가 정보 배열(information)은 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정한다. [사실][^ref-051] 그래서 원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 할 것으로 보인다. [추정][^ref-051] | [ref-051](../../references/ref-051.md) |\n| VDA 5050 3.0.0 명세(오류 객체) | 표준 | 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고, 오류마다 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 언어별 번역과 함께 담을 수 있게 한다. [사실][^ref-031][^ref-051] | [ref-031](../../references/ref-031.md), [ref-051](../../references/ref-051.md) |\n| VDA 5050 connection 스키마 | 표준 | 연결 상태를 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 으로 나눈다. 로봇이 질서 있게 끊으면 OFFLINE 을, 예기치 않게 끊기면 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리며, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드다. [사실][^ref-449] | [ref-449](../../references/ref-449.md) |\n| MassRobotics AMR 상호운용 표준 statusReport | 표준 | 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 두고, 오류는 심각도 필드 없이 문자열 목록(errorCodes)으로만 보고하며 정상 운용 때는 생략하게 한다. [사실][^ref-230] | [ref-230](../../references/ref-230.md) |\n| Open-RMF 작업 상태 스키마 | 오픈소스 | 작업 상태 12개(blocked·error·failed·delayed 등)와 별도로 배차 상태(failed_to_assign 포함)와 배차 오류 배열을 두고, 일시정지·재개·취소·강제 종료 요청마다 요청 시각과 라벨을 남긴다. [사실][^ref-111] 이 기록으로 지연이 배정 실패인지, 실행 중 차단인지, 개입 요청(라벨로 출처 표시)인지 나눠 볼 수 있을 것으로 보인다. [추정][^ref-111] | [ref-111](../../references/ref-111.md) |\n| Open-RMF 경보 메시지(Alert) | 오픈소스 | 심각도를 INFO·WARNING·ERROR 세 등급으로 두고 운영자 응답 목록(responses_available), 관련 작업 id, 화면 표시 여부를 담는다. [사실][^ref-448] | [ref-448](../../references/ref-448.md) |\n| OpenTelemetry 명세 | 오픈소스 | 분산 추적을 하나의 논리적 동작에서 비롯된 사건들을 프로세스·네트워크 경계를 넘어 모은 것으로 정의하고, 16바이트 TraceId 로 여러 프로세스의 span 을 묶으며, 일괄 처리처럼 여러 요청에서 시작된 작업은 span 간 링크(Links)로 잇게 한다. [사실][^ref-447] | [ref-447](../../references/ref-447.md) |\n\nOpen-RMF 작업 예약 id(booking.id)와 VDA 5050 state 의 orderId 가 각각 작업·주문을 식별하므로, ROP 서비스의 추적 TraceId 와 이 식별자들을 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이어 원인 분석에 쓸 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다. [추정][^ref-447][^ref-111][^ref-051] 표준 전체 목록은 [표준·프레임워크](../../standards/index.md)에 있다."
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |\n|---|---|---|\n| 로봇 자체 지능·제어 | 표준 인터페이스가 보고하는 오류 수준·연결 상태·작업 상태를 모아 원인 범주(로봇·설비·통신·앞 작업)로 구분하고 업무 영향과 연결 [추정][^ref-051][^ref-449][^ref-111] | 연계 대상: 센서·모터·드라이버 수준의 진단(ROS 2 diagnostics 같은 로봇 내부 진단)과 개별 부품 고장 진단 [추정][^ref-445] |\n| 시설·설비 제어 | 문 상태(DoorMode) 확인과 문 요청, 문 대기와 승강기 상태를 원인 범주에 반영 [추정][^ref-313][^ref-283][^ref-943] | 연계 대상: 문 개폐 제어와 승강기 운행 제어 자체 |\n| 업종별 조건 | 실외 현장의 인증 조건을 감시·운영 제약으로 반영 [추정][^ref-980] | 연계 대상: 실외이동로봇 운행안전인증 판단(인증 기관·운영자) |\n\nROS 2 diagnostics 는 하드웨어 드라이버·로봇 하드웨어의 진단 정보를 /diagnostics 토픽으로 모아 aggregator 로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘긴다(2026-10-09 확인). [사실][^ref-445] 연계 대상: 이 로봇 내부 진단은 로봇·제조사 쪽 몫이며, ROP 는 그 결과를 원인 범주 판정의 입력으로 받는 쪽에 설 것으로 보인다. [추정][^ref-445]\n\n센서·모터·드라이버 수준의 진단과 개별 부품 고장 진단은 로봇 제조사 영역이며, 이종 로봇을 연결하는 ROP 는 표준 인터페이스가 보고하는 오류 수준·연결 상태·설비 상태·작업 상태를 모아 원인 범주로 구분하고 업무 영향과 연결하는 부분을 맡는 경계가 될 것으로 보인다. [추정][^ref-445][^ref-051][^ref-449][^ref-111] 반대로 규약마다 다른 심각도 표현을 한 경보 체계로 맞추는 대응 규칙과, 플랫폼 처리 추적(TraceId)과 로봇 보고의 작업·주문 식별자(booking.id, orderId)를 잇는 대응은 어느 표준도 정하지 않아 ROP 가 직접 맡을 후보로 보인다. [추정][^ref-031][^ref-448][^ref-230][^ref-447][^ref-111][^ref-051] 경계의 원문 정의는 [범위 경계](../../about/scope-boundary.md)에 있다.\n\n이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "\n### 2026-10-09 갱신(실행 2026-10-09-16)\n\n- **oq-033**·**oq-073** (상태: 열림) 공통 상태·오류 어휘와 오류 수준 대응 — 부분 근거: VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록으로 심각도를 나타내고 세 규약 어디에도 서로 간 대응표가 없어, ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다. [추정][^ref-031][^ref-448][^ref-230]\n- **oq-210** (상태: 열림) 작업 식별자와 분산 추적 연결 — 부분 근거: Open-RMF booking.id 와 VDA 5050 orderId 를 OpenTelemetry TraceId 와 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이을 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다. [추정][^ref-447][^ref-111][^ref-051]\n- **oq-074**·**oq-075** (상태: 열림) 물류창고 대상 원인 분류 체계와 원인별 발생 비율 자료는 이번 갱신에서도 찾지 못했다. 5절 병원 사례 연구는 원문 기준 재조사를 요청했다.\n- 새 질문 (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-16) MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073)\n- 새 질문 (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-16) VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가?"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-051",
              "ref-031",
              "ref-449",
              "ref-230",
              "ref-111",
              "ref-448",
              "ref-313",
              "ref-283",
              "ref-445",
              "ref-447",
              "ref-451",
              "ref-943",
              "ref-944",
              "ref-995",
              "ref-980",
              "ref-961",
              "ref-962"
            ],
            "last_run": "2026-10-09"
          },
          "content": "[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09\n[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09\n[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09\n[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09\n[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09\n[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09\n[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-10-09\n[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-09\n[^ref-445]: ROS (ros/diagnostics GitHub), diagnostics — README (ros2 branch), 미확인, https://github.com/ros/diagnostics/blob/ros2/README.md, 접근일 2026-10-09\n[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09\n[^ref-451]: Roser, C., Nakano, M., & Tanaka, M., Comparison of bottleneck detection methods for AGV systems (WSC 2003 Proceedings, 1192–1198쪽), 2003, https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/, 접근일 2026-09-25 (원문 미열람)\n[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)\n[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)\n[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-10-09 (원문 미열람)\n[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)\n[^ref-961]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-10-09 (원문 미열람)\n[^ref-962]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-10-09 (원문 미열람)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,024자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"3. 왜 중요한가\" 절(1,297자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"11. 열린 질문\" 절(939자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(648자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 38. 모니터링·이상 탐지·원인 분석 | 3절 심각도·시각 형식·통신 신호·사람 개입 근거 보강과 원문 질문 표현 정정, 5절 병원·상업 시설·실외·기타 사례 추가, 7절 VDA 5050·MassRobotics·Open-RMF·OpenTelemetry 필드 표, 9절 내부 진단·승강기·실외 인증 경계, 11절 부분 근거·새 질문 2건, 각주 갱신(1차 조건부 승인 수정 16건 반영) | run 2026-10-09-16",
  "index_updates": {
    "home_recent": "2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 표준별 심각도·시각 형식·연결 상태 차이와 병원·상업 시설·실외·기타 현장 사례를 더하고 책임 경계를 보강했다",
    "category_recent": "2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 3·5·7·9·11절 갱신(현장 유형별 사례 4건 추가, VDA 5050·MassRobotics·Open-RMF 필드 정리, 새 열린 질문 2건)",
    "area_recent": "2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 3절 원문 질문 표현 정정과 근거 보강, 5절 병원·상업 시설·실외·기타 사례, 7절 표준 필드 표, 9절 경계 보강, 11절 부분 근거·새 질문 2건, 13절 각주 접근일 갱신"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "connection-state",
      "term_ko": "연결 상태",
      "term_en": "Connection State (VDA 5050 connectionState)",
      "definition": "VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다.",
      "description": "질서 있는 종료 때는 OFFLINE, 예기치 않은 끊김은 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리고, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드다.",
      "related_areas": [
        38,
        20
      ],
      "sources": [
        "ref-449"
      ]
    },
    {
      "action": "new",
      "slug": "alert-tier",
      "term_ko": "경보 등급",
      "term_en": "Alert Tier (Open-RMF Alert)",
      "definition": "Open-RMF 경보 메시지가 운영자에게 보내는 경보의 심각도를 INFO·WARNING·ERROR 세 단계로 나타내는 필드다.",
      "description": "경보 메시지는 등급과 함께 운영자 응답 목록, 관련 작업 id, 화면 표시 여부를 담는다.",
      "related_areas": [
        38,
        32
      ],
      "sources": [
        "ref-448"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 로봇 상태 메시지 스키마. 필수 항목(errors·operatingMode·safetyState), 운용 모드 값, information 사용 제한, headerId 규칙, 시각 형식을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 본문. 오류 수준 네 단계와 오류 설명·조치 힌트 항목(이전 실행 2026-10-09-15 확인 내용 재인용, 검증에서 state.schema 원문으로 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-449",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/connection.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 연결 상태 메시지 스키마. ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 과 유언 메시지 규칙.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마. identityReport·statusReport, 운용 상태 9값, 문자열 오류 코드 목록.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
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
      "summary": "Open-RMF 작업 상태 스키마. 작업 상태 12값, 배차 상태·오류, 일시정지·재개·취소 기록, 예약 식별자.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-448",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_task_msgs/msg/Alert.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 경보 메시지 정의. 심각도 세 등급, 응답 목록, 관련 작업 id.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-313",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 자동문 모드 메시지. closed·moving·open·offline·unknown 다섯 값.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 문 연동 장. 문 노드·문 어댑터(상태 감독자)의 역할과 토픽.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-445",
      "org": "ROS (ros/diagnostics GitHub)",
      "title": "diagnostics — README (ros2 branch)",
      "published": null,
      "url": "https://github.com/ros/diagnostics/blob/ros2/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ROS 2 진단 시스템 README. /diagnostics 토픽, aggregator, 원격 기록 패키지 구성.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-447",
      "org": "OpenTelemetry (CNCF)",
      "title": "OpenTelemetry Specification — Overview",
      "published": null,
      "url": "https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenTelemetry 명세 개요. 추적·지표·로그 신호, TraceId·SpanId, span 간 링크 정의.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원 의약품 배송 로봇의 승강기 연동과 승강기 가동률 구간별 성공률을 보고한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
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
      "summary": "원문 미열람. 한림대학교성심병원의 서비스 로봇 7종 73대와 커맨드센터 통합관제 운영 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-995",
      "org": "Offshore Technology (Eve Thomas)",
      "title": "Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones",
      "published": "2025-11-21",
      "url": "https://www.offshore-technology.com/features/equinor-autonomous-robotics/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Equinor 시설의 4족 점검 로봇 운영(계기 판독·누출 탐지)과 운영자 임무 생성 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
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
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 제도 안내. 인증 대상은 로봇과 관제장치의 조합.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-961",
      "org": "Responsible AI Collaborative (AI Incident Database)",
      "title": "Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks",
      "published": null,
      "url": "https://incidentdatabase.ai/cite/346/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔 로봇이 단순 업무를 처리하지 못한 사건 기록.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    },
    {
      "id": "ref-962",
      "org": "Hotel Technology News",
      "title": "Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce",
      "published": "2019-01",
      "url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 헨나 호텔의 로봇 절반 철수와 직원 개입 부담 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073)",
      "areas": [
        38,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가?",
      "areas": [
        38,
        42
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시",
      "title": "38. 모니터링·이상 탐지·원인 분석"
    }
  ],
  "additional_research_requests": [
    "구로병원 논문(ref-943)의 실패 유형별 분류(복도 자율주행·통신·승강기 막힘)와 전체 성공률·분모를 원문 기준으로 재조사해 38. 모니터링·이상 탐지·원인 분석 5절 병원 사례와 oq-074에 반영",
    "5절 병원·상업 시설·실외·기타 사례의 '미확인' 칸(시작 조건·제약·완료·인계 등)을 채울 근거 — 이번 브리프의 finding 이 한두 항목에만 걸려 있어 여섯 항목을 채우지 못했다",
    "5절 제조 공장 현장의 이상 탐지·원인 분석 적용 사례 — 이번 브리프에 근거가 없어 '이번 조사에서 찾지 못함'으로 두었다",
    "한림대학교성심병원 보도(ref-944)의 세부 분류 합계(8종 76대)와 7종 73대가 맞지 않는 점을 다른 출처로 확인 — 5절 병원 사례의 '보도 기준' 표기를 해소하기 위해",
    "실외이동로봇 운행안전인증 심사 항목 수가 한국로봇산업진흥원 안내 페이지(8개)와 이전 실행 2026-10-09-15 의 기사(16개)에서 다른 점과 관제장치 항목의 세부 요건 — 5절 실외 사례와 9절 업종별 조건 행의 근거 보강 및 출처 충돌 여부 판단을 위해",
    "ref-031 출처 항목의 표기 불일치(summary 는 '원문 미열람.'으로 시작하나 fetched true·source_unopened false) 정리 — 참고문헌 페이지 표기를 바로잡기 위해",
    "10절의 '분류 개정 전 원문 8장의 교차 규칙' 표현을 원문 13장(L. AI·학습 기술 주석) 기준으로 다시 확인 — 이번 갱신 절 밖이라 고치지 않았다"
  ],
  "fixes_applied": [
    "f2 분리 — 7절 VDA 5050 state 스키마 행에서 information 배열의 시각화·디버깅 전용 규정만 [사실][^ref-051]로 쓰고, '원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다'는 별도 문장 [추정][^ref-051]으로 썼다.",
    "f3 각주 — 7절 VDA 5050 3.0.0 명세 행의 오류 수준 4단계와 errorDescription·errorHint(번역 포함) 문장에 [사실][^ref-031][^ref-051] 두 각주를 달았다.",
    "f6 분리·표현 — 7절 Open-RMF 작업 상태 행에서 상태 12값·배차 상태(failed_to_assign)·배차 오류 배열·일시정지/재개/취소/강제 종료 요청의 시각·라벨 기록까지 [사실][^ref-111]로, 지연 구분 가능성은 [추정][^ref-111]으로 쓰고 '사람 개입' 대신 '개입 요청(라벨로 출처 표시)'으로 썼다.",
    "f10 분리 — 9절 본문에서 ROS 2 diagnostics 의 /diagnostics·aggregator·원격 기록(InfluxDB) 설명만 [사실][^ref-445]로, 'ROP 는 결과를 원인 범주 판정의 입력으로 받는다'는 '연계 대상:' 표시와 함께 [추정][^ref-445]로 썼고 표의 연계 대상 칸도 유지했다.",
    "f15 표현 — 3절에서 'Open-RMF 작업 기록이 일시정지·재개 요청과 그 요청 출처 라벨을 남긴다'로 바꾸고 waitingHumanEvent 를 '사람 사건 대기'로 썼으며 [추정] 태그를 유지했다.",
    "f16 강등 — 5절 병원 사례를 [추정][^ref-943]으로 쓰고 '승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다'로 고쳤으며 '90% 초과' 표현을 쓰지 않았다. 설비(승강기) 혼잡 원인은 해석이라고 밝히고, 승강기 운행 제어는 연계 대상이며 ROP 몫은 승강기 상태를 원인 범주에 반영하는 데까지라고 5절 서술과 9절 표에 썼다.",
    "f17 한정 — 5절 병원 사례에서 '7종 73대'를 '보도 기준'으로 쓰고 '이 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다'로 한정했다.",
    "f18 표현 — 5절 기타 사례의 시설을 '노르웨이 Northern Lights 시설'로 쓰고, 계기 판독·가스(누출) 탐지는 로봇 인식 기능인 연계 대상으로 짧게 두었으며 ROP 쪽은 점검 결과를 설비 이상 판정의 입력으로 받는 부분만 [추정]으로 서술했다.",
    "f19 분리 — 5절 실외 사례에서 '운행안전인증은 로봇과 관제장치의 조합을 대상으로 한다'만 [사실][^ref-980]로, '관제장치의 감시 기능이 운행 조건의 하나가 된다'는 [추정][^ref-980]으로 쓰고 인증 판단은 인증 기관·운영자 쪽 연계 대상이라고 5절 서술과 9절 표에 밝혔다.",
    "f20 표현 — 5절 상업 시설 사례에서 '사람 개입 없이는 처리하지 못해 사람의 일을 늘렸고', 철수 규모를 '로봇 일부(보도 기준 절반가량)'로 쓰고 기준일 2019-01 보도를 유지했다.",
    "f21 제외 — 본문에 쓰지 않고 additional_research_requests 에 구로병원 논문의 실패 유형별 분류와 전체 성공률·분모 재조사 요청을 넣었다.",
    "5절 현장 유형별 분리 — 병원(f16·f17)·상업 시설(f20)·실외(f19)·기타(f18) 사례를 현장 유형마다 나누고 finding 이 없는 칸은 '미확인'으로 두었으며, site_matrix_updates 에는 실제로 채운 칸만 넣었다. 제조 공장은 '이번 조사에서 찾지 못함'으로 두었다.",
    "3절 원문 질문 표현 — 둘째 문단을 '지연의 원인이 로봇인지 설비인지 통신인지 앞 작업인지'로 고쳐 [분류원문] 태그 없이 풀어 썼다.",
    "열린 질문 1번 — 질문 끝에 '(관련: oq-033, oq-073)'를 붙여 open_question_updates 와 11절에 등록했고, 관련 영역 38·21 과 종류 일반(접두어 없음)을 유지했다.",
    "각주 접근일·표기 — ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447·ref-031 의 접근일을 2026-10-09 로 갱신하고, ref-111·ref-283·ref-230·ref-313 의 기관·제목을 참고문헌 색인 줄과 같게 고쳤다.",
    "원문 미열람 표시 — ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "분량 초과 자동 분리: 38. 모니터링·이상 탐지·원인 분석 본문 9,672자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 5,368자"
  ]
}
```

### runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석"
type: area
category: "J. 현장 운영·관제"
area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [이상 탐지, 근본 원인 분석, VDA 5050, Open-RMF, 분산 추적]
status: draft
confidence: low
created: 2026-09-24
updated: 2026-10-09
sources: [ref-051, ref-031, ref-449, ref-230, ref-111, ref-448, ref-313, ref-283, ref-445, ref-447, ref-451, ref-943, ref-944, ref-995, ref-980, ref-961, ref-962]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 38. 모니터링·이상 탐지·원인 분석

# 38. 모니터링·이상 탐지·원인 분석

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

이종 로봇이 섞인 현장에서는 로봇 오류 수준·연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 작업 지연·차단과 문 모드(Open-RMF)가 서로 다른 어휘로 보고되므로, 지연 원인을 가리려면 이들을 같은 시간축에 맞추고 ROP 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111]

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 왜 중요한가](../../topics/2026/2026-10-09-area38-s3.md)에 있다.

## 4. 핵심 개념과 용어

아래 용어는 3절에서 말한 서로 다른 보고 어휘와 원인 분석 기법을 읽기 위한 기본 개념이다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area19-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 절은 지연·정지의 원인을 가리는 일이 현장 유형마다 어떻게 드러나는지를 사례로 보인다. 물류창고 사례는 설명용 가상 사례이고, 병원·상업 시설·실외·기타 현장 사례는 공개 연구·보도에 기댄 것이다. 사례마다 이번 근거로 채우지 못한 항목은 '미확인'으로 두었고, 제조 공장의 이상 탐지·원인 분석 사례는 이번 조사에서 찾지 못함.

### 물류창고

**현장 유형:** 물류창고

**사례:** 보충 단계 — 보충용 박스를 운반하던 AMR 이 문 앞에서 멈춰 보충이 늦어진 원인 가리기

이 사례는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 가상 사례이며, 문 모드·문 어댑터·작업 상태·경보 서술은 2026-10-09 원문으로 다시 확인했다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 피킹 구역 재고가 보충 기준 아래로 내려가 보충 작업이 생성된다(가상 설정). |
| 작업 대상 | 예비 보관 구역에서 피킹 구역으로 옮길 보충용 박스와 이를 실은 자율이동로봇(AMR). |
| 수행 자원 | AMR 은 운반, 문 설비는 개폐, ROP 는 상태 수집과 원인 구분, 운영자는 경보 응답을 맡는다. 문 개폐 제어 자체는 연계 대상(시설·설비 제어)이며 ROP 는 문 상태 확인과 문 요청만 다룬다. |
| 제약 | 경로가 문을 지나야 한다. Open-RMF 에서 문 노드는 문 상태를 /door_states 로 발행하고 문 모드는 closed·moving·open·offline·unknown 다섯 값이다(2026-10-09 재확인). [사실][^ref-313][^ref-283] 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다. [사실][^ref-283] |
| 완료·인계 | 작업 상태가 completed 로 바뀌고 보충 위치 도착이 확인되면 보충 완료로 본다. 작업 상태 토큰 completed 는 Open-RMF 작업 상태 스키마에 있다. [사실][^ref-111] |
| 예외·성과 | 작업 상태가 delayed 또는 blocked 로 바뀌고 [사실][^ref-111], MassRobotics 운용 상태가 waitingExternalEvent 를 보고하며 [사실][^ref-230], 경보는 심각도 등급(INFO·WARNING·ERROR)·응답 목록·관련 작업 id 를 담아 운영자에게 간다(2026-10-09 재확인). [사실][^ref-448] 이 신호들을 맞춰 원인을 문·로봇·통신 중 하나로 판정하는 절차는 추정이다. [추정][^ref-313][^ref-111][^ref-230] |

다음은 설명을 위한 가상의 시나리오이다. 보충 작업을 받은 AMR 이 문 앞에서 멈추고, ROP 에는 작업 지연과 외부 사건 대기가 함께 들어온다. 수치는 쓰지 않는다.

ROP 는 같은 시각의 문 모드를 확인한다. 문 모드가 offline 이나 unknown 이면 설비 쪽 원인일 가능성을, 문이 open 인데도 로봇이 대기 중이면 로봇 쪽 원인일 가능성을 먼저 살피는 식으로 판정 순서를 세울 수 있어 보인다. [추정][^ref-313][^ref-230] 로봇 연결이 CONNECTION_BROKEN 으로 끊겼다면 통신 원인을 따로 볼 수 있다. [추정][^ref-449]

원인 범주가 정해지면 경보의 응답 목록으로 운영자가 조치를 고르고, 복구 방식은 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)으로 넘어간다. 현장 유형 매트릭스 전체는 [현장 유형 매트릭스](../../site-matrix.md)에 있다.

### 병원

**현장 유형:** 병원

**사례:** 의약품 배송 로봇의 승강기 호출·탑승과 승강기 혼잡

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 로봇이 배송하는 의약품. [추정][^ref-943] |
| 수행 자원 | 의약품 배송 로봇이 승강기를 호출해 탑승한다. [추정][^ref-943] 승강기 운행 제어 자체는 연계 대상(시설·설비 제어)이다. 다른 병원 사례로, 한림대학교성심병원은 보도 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리한다(2024-04-15 보도). [사실][^ref-944] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 고려대학교 구로병원 연구(2026-03-31 게재)에서 승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다. [추정][^ref-943] |

이 결과를 설비(승강기) 혼잡이 지연·실패의 원인으로 드러난 것으로 읽는 것은 해석이며, 전체 성공률의 분모는 미확인이다. [추정][^ref-943] 승강기 운행 제어는 연계 대상이고, ROP 몫은 승강기 상태를 원인 범주(설비)에 반영하는 데까지로 보인다. [추정][^ref-943]

한림대학교성심병원 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다. [사실][^ref-944] 이 부재 진술은 보도 한 건에 기댄 것이다.

### 상업 시설

**현장 유형:** 상업 시설

**사례:** 호텔 로봇이 단순 업무를 처리하지 못해 사람 일이 늘어난 사례(일본 헨나 호텔)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 투숙객의 기본 질문, 여권 복사 같은 업무. [사실][^ref-961][^ref-962] |
| 수행 자원 | 객실 음성 비서 로봇, 짐 운반 로봇, 프런트 로봇과 호텔 직원. [사실][^ref-961][^ref-962] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 로봇이 이런 업무를 사람 개입 없이는 처리하지 못해 사람의 일을 늘렸고, 호텔은 로봇 일부(보도 기준 절반가량)를 철수했다(2019-01 보도 기준). [사실][^ref-961][^ref-962] |

공개 기록은 실패 현상과 철수만 전하며, 시작 조건·제약·완료·인계는 이번 근거로 확인하지 못했다.

### 실외

**현장 유형:** 실외

**사례:** 실외이동로봇 운행안전인증과 관제장치

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 미확인 |
| 제약 | 실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 한다(2026-10-09 확인). [사실][^ref-980] 그래서 실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 될 것으로 보인다. [추정][^ref-980] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

운행 안전 인증 판단은 인증 기관·운영자 쪽 연계 대상이며, ROP 는 이 조건을 실외 현장의 감시·운영 제약으로 반영하는 쪽에 설 것으로 보인다. [추정][^ref-980] 관제장치 항목의 세부 요건은 미확인이다.

### 기타

**현장 유형:** 기타

**사례:** 노르웨이 Northern Lights 시설의 4족 점검 로봇 운영(Equinor)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다(2025-11-21 보도). [사실][^ref-995] |
| 작업 대상 | 계기 값, 밸브 위치, 가스 누출 같은 설비 상태. [사실][^ref-995] |
| 수행 자원 | 4족 점검 로봇과 현장 운영자가 맡는다. [사실][^ref-995] 계기 판독·가스(누출) 탐지는 로봇 인식 기능이라 연계 대상이다. |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

ROP 쪽 몫은 이 점검 결과를 설비 이상 판정의 입력으로 받는 부분으로 보인다. [추정][^ref-995] 점검 결과가 설비 보전 시스템의 작업 지시·점검 기록으로 돌아가는 형식은 열린 질문 oq-194 로 남아 있다.

### 제조 공장

제조 공장의 이상 탐지·원인 분석 적용 사례는 이번 조사에서 찾지 못함.

## 6. 대표 접근법과 기술

5절의 판정 절차를 일반화하면 다음 접근들로 정리된다. 대부분 표준 필드는 확인됐지만 물류 로봇 관제에 적용한 공개 사례는 확인되지 않았다. [추정][^ref-051][^ref-447]

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area19-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

6절의 접근은 아래 표준·오픈소스가 정의한 필드와 신호를 재료로 쓴다. VDA 5050 은 3.0.0 판(GitHub main 브랜치, 접근일 2026-10-09) 기준이며 main 브랜치는 판이 바뀔 수 있다. [사실][^ref-051]

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area38-s7.md)에 있다.

## 8. 대표 연구와 자료

7절의 표준이 무엇을 보고하는지를 정한다면, 아래 연구는 그 보고로 원인과 병목을 찾는 방법을 다룬다. 논문은 모두 원문 미열람이며 검색 요약 기준이다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 대표 연구와 자료](../../topics/2026/2026-09-25-area19-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 표준 인터페이스가 보고하는 오류 수준·연결 상태·작업 상태를 모아 원인 범주(로봇·설비·통신·앞 작업)로 구분하고 업무 영향과 연결 [추정][^ref-051][^ref-449][^ref-111] | 연계 대상: 센서·모터·드라이버 수준의 진단(ROS 2 diagnostics 같은 로봇 내부 진단)과 개별 부품 고장 진단 [추정][^ref-445] |
| 시설·설비 제어 | 문 상태(DoorMode) 확인과 문 요청, 문 대기와 승강기 상태를 원인 범주에 반영 [추정][^ref-313][^ref-283][^ref-943] | 연계 대상: 문 개폐 제어와 승강기 운행 제어 자체 |
| 업종별 조건 | 실외 현장의 인증 조건을 감시·운영 제약으로 반영 [추정][^ref-980] | 연계 대상: 실외이동로봇 운행안전인증 판단(인증 기관·운영자) |

ROS 2 diagnostics 는 하드웨어 드라이버·로봇 하드웨어의 진단 정보를 /diagnostics 토픽으로 모아 aggregator 로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘긴다(2026-10-09 확인). [사실][^ref-445] 연계 대상: 이 로봇 내부 진단은 로봇·제조사 쪽 몫이며, ROP 는 그 결과를 원인 범주 판정의 입력으로 받는 쪽에 설 것으로 보인다. [추정][^ref-445]

센서·모터·드라이버 수준의 진단과 개별 부품 고장 진단은 로봇 제조사 영역이며, 이종 로봇을 연결하는 ROP 는 표준 인터페이스가 보고하는 오류 수준·연결 상태·설비 상태·작업 상태를 모아 원인 범주로 구분하고 업무 영향과 연결하는 부분을 맡는 경계가 될 것으로 보인다. [추정][^ref-445][^ref-051][^ref-449][^ref-111] 반대로 규약마다 다른 심각도 표현을 한 경보 체계로 맞추는 대응 규칙과, 플랫폼 처리 추적(TraceId)과 로봇 보고의 작업·주문 식별자(booking.id, orderId)를 잇는 대응은 어느 표준도 정하지 않아 ROP 가 직접 맡을 후보로 보인다. [추정][^ref-031][^ref-448][^ref-230][^ref-447][^ref-111][^ref-051] 경계의 원문 정의는 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

원인 구분은 상태를 모으는 영역, 결과를 쓰는 영역과 양쪽으로 이어진다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area38-s10.md)에 있다.

## 11. 열린 질문

위 내용 가운데 확인되지 않은 부분을 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문](../../topics/2026/2026-10-09-area38-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) — 영역 심화: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 13절 각주 정의(1차 조건부 승인 수정 14건 반영). 형식 재작성: 프런트매터 sources 를 이 페이지 각주 정의와 일치시킴 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area19-s4.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "4. 핵심 개념과 용어" 절(1,482자)을 옮겼다 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area19-s7.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,413자)을 옮겼다 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 대표 연구와 자료](../../topics/2026/2026-09-25-area19-s8.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "8. 대표 연구와 자료" 절(1,396자)을 옮겼다. 형식 재작성: 8. 실시간 세계 상태·데이터 일관성 링크를 주제 페이지 기준 경로로 고침 (실행 2026-09-25-48)
- 2026-09-25 · 생성 · [38. 모니터링·이상 탐지·원인 분석 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area19-s6.md) — 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "6. 대표 접근법과 기술" 절(861자)을 옮겼다. 형식 재작성: 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침 (실행 2026-09-25-48)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-10-09
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-09
[^ref-445]: ROS (ros/diagnostics GitHub), diagnostics — README (ros2 branch), 미확인, https://github.com/ros/diagnostics/blob/ros2/README.md, 접근일 2026-10-09
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)
[^ref-995]: Offshore Technology (Eve Thomas), Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones, 2025-11-21, https://www.offshore-technology.com/features/equinor-autonomous-robotics/, 접근일 2026-10-09 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)
[^ref-961]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-10-09 (원문 미열람)
[^ref-962]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-10-09 (원문 미열람)
```

### runs/2026-10-09-16/pages/topics/2026/2026-10-09-area38-s7.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-051, ref-111, ref-230, ref-447, ref-448, ref-449]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#7
---

[홈](../../index.md) › [주제](../index.md) › 38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스

# 38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 6절의 접근은 아래 표준·오픈소스가 정의한 필드와 신호를 재료로 쓴다. VDA 5050 은 3.0.0 판(GitHub main 브랜치, 접근일 2026-10-09) 기준이며 main 브랜치는 판이 바뀔 수 있다. [사실][^ref-051]
- 이 페이지는 [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

6절의 접근은 아래 표준·오픈소스가 정의한 필드와 신호를 재료로 쓴다. VDA 5050 은 3.0.0 판(GitHub main 브랜치, 접근일 2026-10-09) 기준이며 main 브랜치는 판이 바뀔 수 있다. [사실][^ref-051]


### 2026-10-09 원문 재확인으로 더한 필드

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 state 스키마 | 표준 | 로봇의 활성 오류 전체를 담는 errors 배열, 운용 모드(operatingMode), 안전 상태(safetyState)를 필수 항목으로 두고, 운용 모드 값을 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 가지로 정한다. [사실][^ref-051] 로봇이 보내는 부가 정보 배열(information)은 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정한다. [사실][^ref-051] 그래서 원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 할 것으로 보인다. [추정][^ref-051] | [ref-051](../../references/ref-051.md) |
| VDA 5050 3.0.0 명세(오류 객체) | 표준 | 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고, 오류마다 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 언어별 번역과 함께 담을 수 있게 한다. [사실][^ref-031][^ref-051] | [ref-031](../../references/ref-031.md), [ref-051](../../references/ref-051.md) |
| VDA 5050 connection 스키마 | 표준 | 연결 상태를 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 으로 나눈다. 로봇이 질서 있게 끊으면 OFFLINE 을, 예기치 않게 끊기면 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리며, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드다. [사실][^ref-449] | [ref-449](../../references/ref-449.md) |
| MassRobotics AMR 상호운용 표준 statusReport | 표준 | 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 두고, 오류는 심각도 필드 없이 문자열 목록(errorCodes)으로만 보고하며 정상 운용 때는 생략하게 한다. [사실][^ref-230] | [ref-230](../../references/ref-230.md) |
| Open-RMF 작업 상태 스키마 | 오픈소스 | 작업 상태 12개(blocked·error·failed·delayed 등)와 별도로 배차 상태(failed_to_assign 포함)와 배차 오류 배열을 두고, 일시정지·재개·취소·강제 종료 요청마다 요청 시각과 라벨을 남긴다. [사실][^ref-111] 이 기록으로 지연이 배정 실패인지, 실행 중 차단인지, 개입 요청(라벨로 출처 표시)인지 나눠 볼 수 있을 것으로 보인다. [추정][^ref-111] | [ref-111](../../references/ref-111.md) |
| Open-RMF 경보 메시지(Alert) | 오픈소스 | 심각도를 INFO·WARNING·ERROR 세 등급으로 두고 운영자 응답 목록(responses_available), 관련 작업 id, 화면 표시 여부를 담는다. [사실][^ref-448] | [ref-448](../../references/ref-448.md) |
| OpenTelemetry 명세 | 오픈소스 | 분산 추적을 하나의 논리적 동작에서 비롯된 사건들을 프로세스·네트워크 경계를 넘어 모은 것으로 정의하고, 16바이트 TraceId 로 여러 프로세스의 span 을 묶으며, 일괄 처리처럼 여러 요청에서 시작된 작업은 span 간 링크(Links)로 잇게 한다. [사실][^ref-447] | [ref-447](../../references/ref-447.md) |

Open-RMF 작업 예약 id(booking.id)와 VDA 5050 state 의 orderId 가 각각 작업·주문을 식별하므로, ROP 서비스의 추적 TraceId 와 이 식별자들을 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이어 원인 분석에 쓸 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다. [추정][^ref-447][^ref-111][^ref-051] 표준 전체 목록은 [표준·프레임워크](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- 관련 영역: [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09
[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-16 | 38. 모니터링·이상 탐지·원인 분석 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-16/pages/topics/2026/2026-10-09-area38-s3.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석 — 왜 중요한가"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-051, ref-111, ref-230, ref-313, ref-448, ref-449, ref-451]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#3
---

[홈](../../index.md) › [주제](../index.md) › 38. 모니터링·이상 탐지·원인 분석 — 왜 중요한가

# 38. 모니터링·이상 탐지·원인 분석 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이종 로봇이 섞인 현장에서는 로봇 오류 수준·연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 작업 지연·차단과 문 모드(Open-RMF)가 서로 다른 어휘로 보고되므로, 지연 원인을 가리려면 이들을 같은 시간축에 맞추고 ROP 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111]
- 이 페이지는 [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이종 로봇이 섞인 현장에서는 로봇 오류 수준·연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 작업 지연·차단과 문 모드(Open-RMF)가 서로 다른 어휘로 보고되므로, 지연 원인을 가리려면 이들을 같은 시간축에 맞추고 ROP 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-313][^ref-111]

2절의 질문, 곧 지연의 원인이 로봇인지 설비인지 통신인지 앞 작업인지를 가리는 일은 복구 담당과 조치를 정하는 출발점이다. 그런데 각 표준은 자기 필드만 정의하고 서로 간 대응표는 두지 않으며, 이번 조사에서는 공통 매핑 표준을 찾지 못했다(열린 질문 oq-033). [추정][^ref-051][^ref-230][^ref-111] 심각도 표현만 보아도 VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록이어서, 이종 플릿의 이상을 한 경보 체계로 모으려면 ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다(oq-033·oq-073 부분 근거). [추정][^ref-031][^ref-448][^ref-230]

같은 시간축에 맞추는 일도 간단하지 않다. 시각 표현이 VDA 5050 은 밀리초까지의 ISO 8601 문자열, MassRobotics 는 date-time 문자열, Open-RMF 작업 상태는 밀리초 유닉스 시각 정수로 서로 다르다(2026-10-09 확인). [사실][^ref-051][^ref-230][^ref-111]

통신 원인을 따로 가리는 신호도 표준 안에 있다. VDA 5050 의 headerId 는 토픽마다 보낸 메시지마다 1씩 늘어나므로 수신 쪽에서 번호가 건너뛰면 메시지 유실을 의심할 수 있고, 연결 상태(CONNECTION_BROKEN·HIBERNATING)와 함께 보면 상태 보고가 끊긴 원인이 통신인지 로봇 쪽의 의도된 통신 감축인지 가르는 근거가 될 것으로 보이나, 결번 판정 기준은 명세에 없다. [추정][^ref-051][^ref-449]

사람이 관여한 지연도 따로 볼 만하다. VDA 5050 운용 모드의 INTERVENED·MANUAL, MassRobotics 운용 상태의 manualOverride(수동 조작)와 waitingHumanEvent(사람 사건 대기)가 있고, Open-RMF 작업 기록이 일시정지·재개 요청과 그 요청 출처 라벨을 남기므로, 지연 원인 범주에 로봇·설비·통신·앞 작업 외에 사람 개입·대기를 따로 두는 편이 판정에 유리할 것으로 보인다. [추정][^ref-051][^ref-230][^ref-111]

원인 구분은 처리량 관리와도 이어진다. 무인운반차(Automated Guided Vehicle, AGV) 시스템을 다룬 2003년 연구는 기존 두 방법(가동률·대기 시간 기반)에는 이동 병목 탐지와 비교해 여러 한계가 있다고 보고한다. [사실][^ref-451] 어느 설비·로봇이 흐름을 막는지 판정하는 방식에 따라 개선 대상이 달라질 수 있다는 뜻이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- 관련 영역: [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-10-09
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09
[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09
[^ref-451]: Roser, C., Nakano, M., & Tanaka, M., Comparison of bottleneck detection methods for AGV systems (WSC 2003 Proceedings, 1192–1198쪽), 2003, https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-16 | 38. 모니터링·이상 탐지·원인 분석 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-09-16/pages/topics/2026/2026-10-09-area38-s11.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석 — 열린 질문"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-051, ref-111, ref-230, ref-447, ref-448]
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#11
---

[홈](../../index.md) › [주제](../index.md) › 38. 모니터링·이상 탐지·원인 분석 — 열린 질문

# 38. 모니터링·이상 탐지·원인 분석 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 위 내용 가운데 확인되지 않은 부분을 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

위 내용 가운데 확인되지 않은 부분을 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.


### 2026-10-09 갱신(실행 2026-10-09-16)

- **oq-033**·**oq-073** (상태: 열림) 공통 상태·오류 어휘와 오류 수준 대응 — 부분 근거: VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록으로 심각도를 나타내고 세 규약 어디에도 서로 간 대응표가 없어, ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다. [추정][^ref-031][^ref-448][^ref-230]
- **oq-210** (상태: 열림) 작업 식별자와 분산 추적 연결 — 부분 근거: Open-RMF booking.id 와 VDA 5050 orderId 를 OpenTelemetry TraceId 와 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이을 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다. [추정][^ref-447][^ref-111][^ref-051]
- **oq-074**·**oq-075** (상태: 열림) 물류창고 대상 원인 분류 체계와 원인별 발생 비율 자료는 이번 갱신에서도 찾지 못했다. 5절 병원 사례 연구는 원문 기준 재조사를 요청했다.
- 새 질문 (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-16) MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073)
- 새 질문 (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-16) VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- 관련 영역: [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09
[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-16 | 38. 모니터링·이상 탐지·원인 분석 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-16/pages/topics/2026/2026-10-09-area38-s10.md

```markdown
---
title: "38. 모니터링·이상 탐지·원인 분석 — 다른 연구영역과의 연결"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 38
related_areas: [18, 20, 22, 29, 31, 32, 39, 47]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: []
last_run: 2026-10-09
version: 1
split_from: docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#10
---

[홈](../../index.md) › [주제](../index.md) › 38. 모니터링·이상 탐지·원인 분석 — 다른 연구영역과의 연결

# 38. 모니터링·이상 탐지·원인 분석 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 원인 구분은 상태를 모으는 영역, 결과를 쓰는 영역과 양쪽으로 이어진다.
- 이 페이지는 [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

원인 구분은 상태를 모으는 영역, 결과를 쓰는 영역과 양쪽으로 이어진다.

- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 병목 탐지 연구와 SCM 프로세스 마이닝 리뷰가 처리량 개선과 이어지며 oq-018 을 함께 다룬다.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 원인 구분은 현재 상태를 표현하는 오류·연결·문·작업 상태를 같은 시간축에 맞춘 데이터를 쓴다.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — VDA 5050·MassRobotics 가 보고하는 오류 수준·연결 상태·운용 상태가 여기서 들어온다.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 문 상태 발행과 문 어댑터가 설비 원인 판정의 근거가 된다.
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 동작 실패와 오류 보고의 대응, 작업 상태 토큰이 실행 결과 확인과 겹친다.
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 경보의 응답 목록과 관제 인터페이스 연구가 운영자 대응으로 이어진다.
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 오류 수준이 주문 계속 가능 여부를 가르고, 판정된 원인이 복구 방식 선택으로 넘어간다.
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 분류 개정 전 원문 8장의 교차 규칙에 따라 장애 분석은 이 영역에 적용되는 AI 연구 방법이며, LLM 실패 설명(REFLECT)이 그 예다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)
- 관련 영역: [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-16 | 38. 모니터링·이상 탐지·원인 분석 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-09-16/verification2.json

```json
{
  "run_id": "2026-10-09-16",
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
      "f9는 기존 3절 둘째 문단을 보강하는 방식으로 들어갔다(새 문단 없음). 1차 지시대로 이행됐다.",
      "f7·f8은 기존 5절 물류창고 사례의 서술을 유지하고 '2026-10-09 재확인'만 덧붙였으며, 기존 각주 ref-313·ref-283·ref-448을 재사용했다."
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
    "7절·11절(분리 주제 페이지 docs/topics/2026/2026-10-09-area38-s7.md·2026-10-09-area38-s11.md): 이번 갱신 뒤 세부영역 페이지의 7절과 11절은 새 주제 페이지만 가리킨다. 그런데 새 주제 페이지에는 2026-10-09에 더한 표와 질문만 있다. 그래서 이전에 검증·게시된 7절 표준 목록(docs/topics/2026/2026-09-25-area19-s7.md)과 11절 열린 질문 목록(docs/topics/2026/2026-09-25-area19-s11.md)으로 가는 링크가 페이지에서 사라졌다. area19-s11은 어디에서도 링크되지 않는다. 다음 두 문장을 원래 자리에 다시 넣는다. 7절 replace 본문의 첫 문장 뒤에는 '2026-09-25에 정리한 표준·오픈소스 목록은 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스(2026-09-25)](../../topics/2026/2026-09-25-area19-s7.md)에 있다.'를 넣는다. 11절 append 본문의 '### 2026-10-09 갱신' 소제목 앞에는 '2026-09-25에 정리한 열린 질문은 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문(2026-09-25)](../../topics/2026/2026-09-25-area19-s11.md)에 있다.'를 넣는다. 두 문장은 '자세한 내용은 주제 페이지 …에 있다' 형식이 아닌 위 형식 그대로 쓴다. 근거: 분량 분리는 내용을 줄이지 않는 것이 원칙이다(공통 규칙 부록 R-6). 새 페이지의 '2026-10-09 원문 재확인으로 더한 필드'라는 제목도 기존 표가 따로 있다는 전제로 쓰였다.",
    "5절 병원 사례 표의 수행 자원 칸: '다른 병원 사례로, 한림대학교성심병원은 보도 기준 7종 73대 … [사실][^ref-944]' 문장을 구로병원 의약품 배송 사례 표에서 뺀다. 이 문장은 표 아래 문단('한림대학교성심병원 보도에는 …')의 앞에 붙여 별도 언급으로 둔다. 수행 자원 칸에는 의약품 배송 로봇의 승강기 호출·탑승 문장과 '승강기 운행 제어 자체는 연계 대상' 문장만 남긴다. 근거: 여섯 항목 표는 사례 하나를 기술한다(원문 21장). 서로 다른 두 병원 사례를 한 칸에 섞으면 병원|수행 자원 매트릭스 칸의 근거가 모호해진다. site_matrix_updates의 병원 항목 3칸은 그대로 둔다.",
    "5절 문체: 도입 문단 끝의 '제조 공장의 이상 탐지·원인 분석 사례는 이번 조사에서 찾지 못함.'과 '### 제조 공장' 아래의 같은 문장을 평서체 '…이번 조사에서 찾지 못했다.'로 고친다. 근거: 본문은 '~이다/~한다' 평서체로 쓴다(공통 규칙 6절). 표 칸의 '미확인'은 그대로 둔다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 15건, 미확인 6건, 교차 확인 0건. 강등: f2·f6·f10·f19(사실 → 추정, 출처에 없는 도출 절을 분리), f16(사실 → 추정, '가동률 90% 초과에 실패 집중'이 원문과 다름). 삭제: f21(근거 출처 ref-943이 실패 유형을 복도 자율주행·통신·승강기 막힘으로 나눠 보고하므로 주장과 충돌). 원문 미열람 출처: ref-943, ref-944, ref-995, ref-980, ref-961, ref-962(브리프 기준. 검증에서 열어 f16 수치 불일치와 f17·f18·f19·f20 표현 과장을 찾았다). 주의: 3절 새 주장과 9절 경계는 대부분 표준 필드를 대조한 [추정]이다. 세 규약(VDA 5050·MassRobotics·Open-RMF) 사이의 공식 대응표나 작업 식별자–추적 연결 표준은 확인되지 않았다(oq-033·oq-073·oq-210 부분 근거, oq-074·oq-075 미해결). 한림대성심병원 보도는 세부 분류 합계(8종 76대)가 7종 73대와 맞지 않는다. 실외이동로봇 운행안전인증 심사 항목 수는 진흥원 페이지(8개)와 이전 브리프의 기사(16개)가 다르다. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 16건은 모두 페이지에 반영됐다(태그 분리·강등, 표현 한정, 원문 미열람 표기, f21 제외, 현장 유형별 사례 분리와 site_matrix_updates 일치, 열린 질문 2건). [분류원문] 보존, 섹션 순서 준수. 남은 문제는 세 가지다. 첫째, 분량 분리 뒤 7절·11절이 새 주제 페이지만 가리켜, 이전에 게시된 표준 목록(2026-09-25-area19-s7)과 열린 질문 목록(2026-09-25-area19-s11)으로 가는 링크가 끊겼다. 둘째, 병원 사례 표 한 칸에 다른 병원 사례가 섞였다. 셋째, 5절 문장 두 곳이 평서체가 아니다. 파이프라인 담당 참고: 자동 분리가 기존 '자세한 내용은 주제 페이지 …' 줄을 지우는 것으로 보인다(새 주제 페이지 본문에 빈 줄이 겹쳐 남음). 또 3절 분리 뒤 세부영역 페이지 프런트매터 sources에 본문 인용이 없는 ref-451이 남았다(인용은 주제 페이지 2026-10-09-area38-s3에만 있다). 10절 분리 페이지의 '분류 개정 전 원문 8장의 교차 규칙' 표현은 이번 갱신 절 밖이다. 다음 갱신에서 원문 13장(L. AI·학습 기술 주석) 기준으로 확인한다.",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 7절·11절(분리 주제 페이지 docs/topics/2026/2026-10-09-area38-s7.md·2026-10-09-area38-s11.md): 이번 갱신 뒤 세부영역 페이지의 7절과 11절은 새 주제 페이지만 가리킨다. 그런데 새 주제 페이지에는 2026-10-09에 더한 표와 질문만 있다. 그래서 이전에 검증·게시된 7절 표준 목록(docs/topics/2026/2026-09-25-area19-s7.md)과 11절 열린 질문 목록(docs/topics/2026/2026-09-25-area19-s11.md)으로 가는 링크가 페이지에서 사라졌다. area19-s11은 어디에서도 링크되지 않는다. 다음 두 문장을 원래 자리에 다시 넣는다. 7절 replace 본문의 첫 문장 뒤에는 '2026-09-25에 정리한 표준·오픈소스 목록은 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스(2026-09-25)](../../topics/2026/2026-09-25-area19-s7.md)에 있다.'를 넣는다. 11절 append 본문의 '### 2026-10-09 갱신' 소제목 앞에는 '2026-09-25에 정리한 열린 질문은 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문(2026-09-25)](../../topics/2026/2026-09-25-area19-s11.md)에 있다.'를 넣는다. 두 문장은 '자세한 내용은 주제 페이지 …에 있다' 형식이 아닌 위 형식 그대로 쓴다. 근거: 분량 분리는 내용을 줄이지 않는 것이 원칙이다(공통 규칙 부록 R-6). 새 페이지의 '2026-10-09 원문 재확인으로 더한 필드'라는 제목도 기존 표가 따로 있다는 전제로 쓰였다.
    - 5절 병원 사례 표의 수행 자원 칸: '다른 병원 사례로, 한림대학교성심병원은 보도 기준 7종 73대 … [사실][^ref-944]' 문장을 구로병원 의약품 배송 사례 표에서 뺀다. 이 문장은 표 아래 문단('한림대학교성심병원 보도에는 …')의 앞에 붙여 별도 언급으로 둔다. 수행 자원 칸에는 의약품 배송 로봇의 승강기 호출·탑승 문장과 '승강기 운행 제어 자체는 연계 대상' 문장만 남긴다. 근거: 여섯 항목 표는 사례 하나를 기술한다(원문 21장). 서로 다른 두 병원 사례를 한 칸에 섞으면 병원|수행 자원 매트릭스 칸의 근거가 모호해진다. site_matrix_updates의 병원 항목 3칸은 그대로 둔다.
    - 5절 문체: 도입 문단 끝의 '제조 공장의 이상 탐지·원인 분석 사례는 이번 조사에서 찾지 못함.'과 '### 제조 공장' 아래의 같은 문장을 평서체 '…이번 조사에서 찾지 못했다.'로 고친다. 근거: 본문은 '~이다/~한다' 평서체로 쓴다(공통 규칙 6절). 표 칸의 '미확인'은 그대로 둔다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 15건, 미확인 6건, 교차 확인 0건. 강등: f2·f6·f10·f19(사실 → 추정, 출처에 없는 도출 절을 분리), f16(사실 → 추정, '가동률 90% 초과에 실패 집중'이 원문과 다름). 삭제: f21(근거 출처 ref-943이 실패 유형을 복도 자율주행·통신·승강기 막힘으로 나눠 보고하므로 주장과 충돌). 원문 미열람 출처: ref-943, ref-944, ref-995, ref-980, ref-961, ref-962(브리프 기준. 검증에서 열어 f16 수치 불일치와 f17·f18·f19·f20 표현 과장을 찾았다). 주의: 3절 새 주장과 9절 경계는 대부분 표준 필드를 대조한 [추정]이다. 세 규약(VDA 5050·MassRobotics·Open-RMF) 사이의 공식 대응표나 작업 식별자–추적 연결 표준은 확인되지 않았다(oq-033·oq-073·oq-210 부분 근거, oq-074·oq-075 미해결). 한림대성심병원 보도는 세부 분류 합계(8종 76대)가 7종 73대와 맞지 않는다. 실외이동로봇 운행안전인증 심사 항목 수는 진흥원 페이지(8개)와 이전 브리프의 기사(16개)가 다르다. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 없음. 1차 수정 지시 16건은 모두 페이지에 반영됐다(태그 분리·강등, 표현 한정, 원문 미열람 표기, f21 제외, 현장 유형별 사례 분리와 site_matrix_updates 일치, 열린 질문 2건). [분류원문] 보존, 섹션 순서 준수. 남은 문제는 세 가지다. 첫째, 분량 분리 뒤 7절·11절이 새 주제 페이지만 가리켜, 이전에 게시된 표준 목록(2026-09-25-area19-s7)과 열린 질문 목록(2026-09-25-area19-s11)으로 가는 링크가 끊겼다. 둘째, 병원 사례 표 한 칸에 다른 병원 사례가 섞였다. 셋째, 5절 문장 두 곳이 평서체가 아니다. 파이프라인 담당 참고: 자동 분리가 기존 '자세한 내용은 주제 페이지 …' 줄을 지우는 것으로 보인다(새 주제 페이지 본문에 빈 줄이 겹쳐 남음). 또 3절 분리 뒤 세부영역 페이지 프런트매터 sources에 본문 인용이 없는 ref-451이 남았다(인용은 주제 페이지 2026-10-09-area38-s3에만 있다). 10절 분리 페이지의 '분류 개정 전 원문 8장의 교차 규칙' 표현은 이번 갱신 절 밖이다. 다음 갱신에서 원문 13장(L. AI·학습 기술 주석) 기준으로 확인한다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
