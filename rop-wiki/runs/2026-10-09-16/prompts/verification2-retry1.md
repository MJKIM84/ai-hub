(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
      "budget_chars": 1800,
      "summary": "VDA 5050 state·connection 스키마, MassRobotics 상태 보고, Open-RMF 작업 상태·경보, OpenTelemetry 가 원인 분석에 쓰는 필드를 2026-10-09 원문으로 정리했고, 2026-09-25 목록으로 가는 링크를 유지했다. [사실][^ref-051][^ref-449][^ref-230][^ref-111][^ref-448][^ref-447]",
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
      "budget_chars": 1000,
      "summary": "2026-09-25 열린 질문 목록 링크를 유지하고, oq-033·oq-073·oq-210 에 부분 근거를 더하며 oq-074·oq-075 는 열린 채로 두고, 심각도 부여 기준과 headerId 결번 판정 기준을 새 질문으로 올렸다. [추정][^ref-031][^ref-448][^ref-230]",
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
      "diff_summary": "3절 둘째 문단을 현재 원문 질문에 맞추고 심각도·시각 형식·통신 신호·사람 개입 근거 보강, 5절 현장 유형별 사례(병원·상업 시설·실외·기타) 추가와 물류창고 사례 재확인, 7절 표준 필드 표 추가와 2026-09-25 목록 링크 유지, 9절 내부 진단·승강기·실외 인증 경계와 직접 범위 후보 추가, 11절 2026-09-25 목록 링크 유지·부분 근거·새 질문 2건, 13절 각주 접근일·기관 표기 갱신(2차 수정 3건 반영)",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
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
          "content": "(절 본문 생략 — runs/2026-10-09-16/pages/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,049자)을 옮겼다"
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
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"11. 열린 질문\" 절(1,010자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area38-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(648자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 38. 모니터링·이상 탐지·원인 분석 | 3절 심각도·시각 형식·통신 신호·사람 개입 근거 보강과 원문 질문 표현 정정, 5절 병원·상업 시설·실외·기타 사례 추가, 7절 VDA 5050·MassRobotics·Open-RMF·OpenTelemetry 필드 표, 9절 내부 진단·승강기·실외 인증 경계, 11절 부분 근거·새 질문 2건, 각주 갱신(1차 조건부 승인 수정 16건·2차 수정 3건 반영) | run 2026-10-09-16",
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
    "5절 제조 공장 현장의 이상 탐지·원인 분석 적용 사례 — 이번 브리프에 근거가 없어 '이번 조사에서 찾지 못했다'로 두었다",
    "한림대학교성심병원 보도(ref-944)의 세부 분류 합계(8종 76대)와 7종 73대가 맞지 않는 점을 다른 출처로 확인 — 5절 병원 사례의 '보도 기준' 표기를 해소하기 위해",
    "실외이동로봇 운행안전인증 심사 항목 수가 한국로봇산업진흥원 안내 페이지(8개)와 이전 실행 2026-10-09-15 의 기사(16개)에서 다른 점과 관제장치 항목의 세부 요건 — 5절 실외 사례와 9절 업종별 조건 행의 근거 보강 및 출처 충돌 여부 판단을 위해",
    "ref-031 출처 항목의 표기 불일치(summary 는 '원문 미열람.'으로 시작하나 fetched true·source_unopened false) 정리 — 참고문헌 페이지 표기를 바로잡기 위해",
    "10절(분리 주제 페이지)의 '분류 개정 전 원문 8장의 교차 규칙' 표현을 원문 13장(L. AI·학습 기술 주석) 기준으로 다시 확인 — 이번 갱신 절 밖이라 고치지 않았다",
    "파이프라인 담당: 자동 분리가 기존 '자세한 내용은 주제 페이지 …' 줄을 지우는 문제와, 3절 분리 뒤 세부영역 페이지 프런트매터 sources 에 본문 인용이 없는 ref-451 이 남는 문제 확인 — 2차 검증 노트의 지적"
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
    "5절 현장 유형별 분리 — 병원(f16·f17)·상업 시설(f20)·실외(f19)·기타(f18) 사례를 현장 유형마다 나누고 finding 이 없는 칸은 '미확인'으로 두었으며, site_matrix_updates 에는 실제로 채운 칸만 넣었다. 제조 공장은 이번 조사에서 찾지 못했다고 두었다.",
    "3절 원문 질문 표현 — 둘째 문단을 '지연의 원인이 로봇인지 설비인지 통신인지 앞 작업인지'로 고쳐 [분류원문] 태그 없이 풀어 썼다.",
    "열린 질문 1번 — 질문 끝에 '(관련: oq-033, oq-073)'를 붙여 open_question_updates 와 11절에 등록했고, 관련 영역 38·21 과 종류 일반(접두어 없음)을 유지했다.",
    "각주 접근일·표기 — ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447·ref-031 의 접근일을 2026-10-09 로 갱신하고, ref-111·ref-283·ref-230·ref-313 의 기관·제목을 참고문헌 색인 줄과 같게 고쳤다.",
    "원문 미열람 표시 — ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "2차: 7절·11절 기존 목록 링크 복원 — 7절 replace 본문의 첫 문단 뒤에 '2026-09-25에 정리한 표준·오픈소스 목록은 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스(2026-09-25)](../../topics/2026/2026-09-25-area19-s7.md)에 있다.'를, 11절 append 본문의 '### 2026-10-09 갱신' 소제목 앞에 '2026-09-25에 정리한 열린 질문은 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문(2026-09-25)](../../topics/2026/2026-09-25-area19-s11.md)에 있다.'를 지시된 형식 그대로 넣었다.",
    "2차: 5절 병원 사례 표 정리 — 수행 자원 칸에서 한림대학교성심병원 문장을 빼고 의약품 배송 로봇의 승강기 호출·탑승 문장과 승강기 운행 제어 연계 대상 문장만 남겼으며, 한림대학교성심병원 문장('다른 병원 사례로, … [사실][^ref-944]')은 표 아래 '한림대학교성심병원 보도에는 …' 문장 앞에 별도 언급으로 옮겼다. site_matrix_updates 의 병원 3칸은 그대로 두었다.",
    "2차: 5절 문체 — 도입 문단 끝과 '### 제조 공장' 아래의 '찾지 못함.'을 '…이번 조사에서 찾지 못했다.'로 고쳤고 표 칸의 '미확인'은 그대로 두었다.",
    "분량 초과 자동 분리: 38. 모니터링·이상 탐지·원인 분석 본문 9,770자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 5,370자"
  ]
}
```

### runs/2026-10-09-16/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (6개 절)
- 분량 초과 자동 분리:
    - docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area38-s7.md (2,049자)
    - docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md "3. 왜 중요한가" → docs/topics/2026/2026-10-09-area38-s3.md (1,297자)
    - docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area38-s11.md (1,010자)
    - docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-09-area38-s10.md (648자)
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

이 절은 지연·정지의 원인을 가리는 일이 현장 유형마다 어떻게 드러나는지를 사례로 보인다. 물류창고 사례는 설명용 가상 사례이고, 병원·상업 시설·실외·기타 현장 사례는 공개 연구·보도에 기댄 것이다. 사례마다 이번 근거로 채우지 못한 항목은 '미확인'으로 두었고, 제조 공장의 이상 탐지·원인 분석 사례는 이번 조사에서 찾지 못했다.

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
| 수행 자원 | 의약품 배송 로봇이 승강기를 호출해 탑승한다. [추정][^ref-943] 승강기 운행 제어 자체는 연계 대상(시설·설비 제어)이다. |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 고려대학교 구로병원 연구(2026-03-31 게재)에서 승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다. [추정][^ref-943] |

이 결과를 설비(승강기) 혼잡이 지연·실패의 원인으로 드러난 것으로 읽는 것은 해석이며, 전체 성공률의 분모는 미확인이다. [추정][^ref-943] 승강기 운행 제어는 연계 대상이고, ROP 몫은 승강기 상태를 원인 범주(설비)에 반영하는 데까지로 보인다. [추정][^ref-943]

다른 병원 사례로, 한림대학교성심병원은 보도 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리한다(2024-04-15 보도). [사실][^ref-944] 한림대학교성심병원 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다. [사실][^ref-944] 이 부재 진술은 보도 한 건에 기댄 것이다.

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

제조 공장의 이상 탐지·원인 분석 적용 사례는 이번 조사에서 찾지 못했다.

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

2026-09-25에 정리한 표준·오픈소스 목록은 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스(2026-09-25)](2026-09-25-area19-s7.md)에 있다.

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


2026-09-25에 정리한 열린 질문은 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문(2026-09-25)](2026-09-25-area19-s11.md)에 있다.

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
