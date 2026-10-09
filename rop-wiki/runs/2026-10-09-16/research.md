# 리서치 브리프 2026-10-09-16

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-16 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 38. 모니터링·이상 탐지·원인 분석 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 보고 어휘를 '같은 시간축에 맞춘다'고만 적었고, 표준마다 시각 형식·심각도 등급·연결 상태 표현이 어떻게 다른지에 대한 근거가 없음
- 섹션 5. 적용 사례 (현장 유형 명시) — 개정 전에 쓴 물류창고 가상 시나리오 1건뿐이고 병원·상업 시설·실외·기타 현장 사례가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 운용 모드·information 사용 제한·연결 상태(HIBERNATING), MassRobotics 오류 코드 형식, Open-RMF 배차 오류·개입 기록이 정리되지 않음(주제 페이지로 분리된 절)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 로봇 내부 진단(ROS 2 diagnostics)과 플랫폼 수준 원인 판정의 경계 근거가 README 수준 한 줄뿐
- 섹션 11. 열린 질문 — oq-033·oq-073·oq-074·oq-075·oq-210 에 대한 부분 근거 미정리
- 정정 요청 없음. 바뀐 출처 확인 대상은 입력으로 들어온 원문 텍스트(ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447)

## 조사 질문

1. 지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]
2. oq-033·oq-073 VDA 5050·MassRobotics·Open-RMF 는 오류 심각도·작업 상태·운용 상태를 각각 어떤 값과 형식으로 보고하며, 공통 어휘로 옮길 때 무엇이 어긋나는가? (섹션 3·7·11 겨냥)
3. 통신 원인을 로봇·설비 원인과 구분하는 데 쓸 수 있는 표준 신호(연결 상태, 메시지 순번, 마지막 유언 메시지)는 무엇인가? (섹션 3·7 겨냥)
4. oq-210 플랫폼 서비스의 분산 추적과 로봇 상태 메시지를 하나의 작업 식별자로 이을 수 있는 표준 필드는 무엇인가? (섹션 6·7·11 겨냥)
5. 로봇 내부 진단(센서·드라이버)과 플랫폼 수준 원인 판정의 경계는 어디인가? (섹션 9 겨냥)
6. oq-074·oq-075 병원·상업 시설·실외·기타 현장에서 로봇 정지·지연·실패의 원인이나 이상 감시 방식이 공개된 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 state 스키마는 로봇의 활성 오류 전체를 담는 errors 배열, 운용 모드(operatingMode), 안전 상태(safetyState)를 필수 항목으로 두고, 운용 모드 값을 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 가지로 정한다. | ref-051 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 state 스키마는 로봇이 보내는 부가 정보 배열(information)을 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정하므로, 원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다. | ref-051 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 은 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고 오류마다 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 담을 수 있게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 connection 스키마는 연결 상태를 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 으로 나누어, 로봇이 질서 있게 끊으면 OFFLINE 을, 예기치 않게 끊기면 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리고, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드로 정한다. | ref-449 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | MassRobotics AMR 상호운용 표준의 statusReport 는 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 두고, 오류는 심각도 필드 없이 문자열 목록(errorCodes)으로만 보고하며 정상 운용 때는 생략하게 한다. | ref-230 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f6 | [사실] | Open-RMF 작업 상태 스키마는 작업 상태 12개(blocked·error·failed·delayed 등)와 별도로 배차 상태(failed_to_assign 포함)와 배차 오류 배열을 두고, 일시정지(interruptions)·재개(resumed_by)·취소·강제 종료 요청마다 요청 시각과 라벨을 남겨, 지연이 배정 실패인지 실행 중 차단인지 사람 개입인지를 기록에서 나눠 볼 수 있다. | ref-111 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 경보 메시지(Alert)는 심각도를 INFO·WARNING·ERROR 세 등급으로 두고 운영자 응답 목록(responses_available), 관련 작업 id, 화면 표시 여부를 담는다. | ref-448 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f8 | [사실] | 오늘 기준 Open-RMF 문 모드 메시지는 여전히 closed·moving·open·offline·unknown 다섯 값이고, 문 어댑터는 문 노드에 직접 보낸 요청을 무효로 돌려 진행 중 로봇 작업을 방해하지 않게 하는 상태 감독자 역할을 하므로, 페이지 5절의 문 관련 서술은 그대로 유효하다. | ref-313, ref-283 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f9 | [추정] | 오류 심각도 표현이 VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록으로 서로 달라, 38. 모니터링·이상 탐지·원인 분석에서 이종 플릿의 이상을 한 경보 체계로 모으려면 ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다(oq-033·oq-073 부분 근거). | ref-031, ref-448, ref-230 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: ROS 2 diagnostics 는 하드웨어 드라이버·로봇 하드웨어의 진단 정보를 /diagnostics 토픽으로 모아 aggregator 로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘기는 로봇 내부 진단 체계이므로, ROP 는 이 결과를 원인 범주 판정의 입력으로 받는 쪽에 선다. | ref-445 | 아니오 | medium | 2026-10-09 | 수행 자원 | — |
| f11 | [사실] | OpenTelemetry 명세는 분산 추적을 하나의 논리적 동작에서 비롯된 사건들을 프로세스·네트워크 경계를 넘어 모은 것으로 정의하고, 16바이트 TraceId 로 여러 프로세스의 span 을 묶으며, 일괄 처리처럼 여러 요청에서 시작된 작업은 span 간 링크(Links)로 잇게 한다. | ref-447 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [추정] | Open-RMF 작업 예약 id(booking.id)와 VDA 5050 state 의 orderId 가 각각 작업·주문을 식별하므로, ROP 서비스의 추적 TraceId 와 이 식별자들을 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이어 원인 분석에 쓸 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다(oq-210 부분 근거). | ref-447, ref-111, ref-051 | 아니오 | low | 2026-10-09 | — | — |
| f13 | [추정] | VDA 5050 의 headerId 는 토픽마다 보낸 메시지마다 1씩 늘어나므로 수신 쪽에서 번호가 건너뛰면 메시지 유실을 의심할 수 있고, 연결 상태(CONNECTION_BROKEN·HIBERNATING)와 함께 보면 상태 보고가 끊긴 원인이 통신인지 로봇 쪽 의도된 감축인지 가르는 근거가 될 것으로 보인다. | ref-051, ref-449 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f14 | [사실] | 세 규약의 시각 표현은 VDA 5050 이 ISO 8601 문자열(밀리초까지), MassRobotics 가 date-time 문자열, Open-RMF 작업 상태가 밀리초 유닉스 시각 정수로 서로 다르다. | ref-051, ref-230, ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [추정] | VDA 5050 운용 모드의 INTERVENED·MANUAL, MassRobotics 의 manualOverride·waitingHumanEvent, Open-RMF 작업의 일시정지 라벨이 모두 사람 개입을 표시하므로, 지연 원인 범주에 로봇·설비·통신·앞 작업 외에 사람 개입·대기를 따로 두는 편이 판정에 유리할 것으로 보인다. | ref-051, ref-230, ref-111 | 아니오 | low | 2026-10-09 | 수행 자원 | — |
| f16 | [사실] | 고려대학교 구로병원 연구에서 의약품 배송 로봇의 승강기 호출·탑승은 승강기 가동률 59% 미만 구간에서 성공률 95.52% 였고 실패가 가동률 90% 초과 구간에 몰려, 병원 현장의 로봇 지연·실패 원인으로 설비(승강기) 혼잡이 드러났다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | 원문 미열람 |
| f17 | [사실] | 한림대학교성심병원은 2024-04 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하지만, 이상 탐지·원인 분석 방식이나 원인별 장애 통계는 공개되지 않았다. | ref-944 | 아니오 | low | 2024-04-15 | 병원 / 수행 자원 | 원문 미열람 |
| f18 | [사실] | Equinor 의 이산화탄소 포집·저장 시설에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지로 설비 이상을 찾고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다. | ref-995 | 아니오 | low | 2025-11-21 | 기타 / 작업 대상 | 원문 미열람 |
| f19 | [사실] | 국내 실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 하므로, 실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 된다. | ref-980 | 아니오 | low | 2026-10-09 | 실외 / 제약 | 원문 미열람 |
| f20 | [사실] | 일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했고, 호텔은 로봇 일부를 철수했다. | ref-961, ref-962 | 아니오 | low | 2019-01 | 상업 시설 / 예외·성과 | 원문 미열람 |
| f21 | [추정] | 이번에 확인한 병원·상업 시설·기타 현장 사례는 실패·지연 현상이나 통합관제 운영만 보고하고 원인을 로봇·설비·통신·앞 작업으로 나눈 분류나 원인별 발생 비율은 공개하지 않아, oq-074·oq-075 는 열린 채로 남는 것으로 보인다. | ref-943, ref-944, ref-961 | 아니오 | low | 2026-10-09 | 예외·성과 | 원문 미열람 |

### 근거 발췌

- **f1**: state.schema required 목록에 errors·operatingMode·safetyState 포함. errors 설명: 모든 활성 오류를 목록에 넣고 빈 배열은 활성 오류 없음. operatingMode enum 7개. (발행일 미확인, 확인일 기준)
- **f2**: information 설명: "This should only be used for visualization or debugging – it must not be used for logic in fleet control." (발행일 미확인, 확인일 기준)
- **f3**: 3.0.0 명세의 오류 객체: errorLevel 네 단계, errorDescription·errorHint, 언어 코드별 번역 가능. 이번 실행에서 원문을 다시 열지 않음 (재인용: 2026-10-09-15)
- **f4**: connection.schema: 유언 메시지는 retain 플래그로 보내고 CONNECTION_BROKEN 으로 설정. 정상 종료·수면 시 OFFLINE 발행. HIBERNATING 은 연결은 활성이나 state 메시지를 보내지 않음. (발행일 미확인, 확인일 기준)
- **f5**: statusReport.operationalState enum 9개. errorCodes: type array, items string, uniqueItems, 설명 'should be omitted for normal operation'. 심각도 필드는 스키마에 없음. (발행일 미확인, 확인일 기준)
- **f6**: task_state.json: status enum 12개, dispatch.status 에 failed_to_assign·canceled_in_flight, dispatch.errors 배열, interruption 의 unix_millis_request_time·labels·resumed_by. (발행일 미확인, 확인일 기준)
- **f7**: Alert.msg: tier TIER_INFO=0·TIER_WARNING=1·TIER_ERROR=2, responses_available, alert_parameters, task_id(작업이 없으면 비움), display 기본 true. 페이지 5절 서술이 오늘 기준 원문과 같다. (발행일 미확인, 확인일 기준)
- **f8**: DoorMode.msg: MODE_CLOSED~MODE_UNKNOWN 5개. Doors 장: 문 노드는 /door_states 발행, 어댑터를 거치지 않은 직접 요청은 어댑터가 이전 상태로 되돌린다. (발행일 미확인, 확인일 기준)
- **f9**: 세 원문의 심각도 필드를 대조한 도출. 세 규약 어디에도 다른 규약과의 대응표는 없음.
- **f10**: README: 진단 시스템은 하드웨어 드라이버·로봇 하드웨어 정보를 사용자·운영자에게 제공. diagnostic_aggregator, diagnostic_remote_logging(예: influxdb 전달) 패키지. (발행일 미확인, 확인일 기준)
- **f11**: Overview: TraceId 는 16 무작위 바이트로 모든 프로세스의 span 을 묶음. Links 는 단일 Trace 안이나 서로 다른 Trace 사이의 인과 관련 span 을 가리킴. (발행일 미확인, 확인일 기준)
- **f12**: task_state.json booking.id(작업 고유 식별자), state.schema orderId(현재 또는 직전 주문 식별), OpenTelemetry TraceId 를 대조한 도출.
- **f13**: headerId 설명: 토픽마다 정의되고 보낸(반드시 수신되지는 않은) 메시지마다 1 증가. connection.schema 의 연결 상태 4값과 결합한 도출. 결번 판정 기준은 명세에 없음.
- **f14**: state.schema timestamp: ISO8601(YYYY-MM-DDTHH:mm:ss.fffZ). statusReport timestamp: format date-time. task_state.json: unix_millis_start_time 등 integer. (발행일 미확인, 확인일 기준)
- **f15**: operatingMode enum 의 INTERVENED·MANUAL, operationalState 의 manualOverride·waitingHumanEvent, task_state interruptions.labels(예: dashboard)를 대조한 도출.
- **f16**: Digital Health 게재 연구: 제어반 전용 통신 모듈로 호출·탑승 자동화, 가동률 구간별 성공률 보고. 전체 성공률 분모는 미확인 (재인용: 2026-10-09-14)
- **f17**: 로봇신문 보도: 커맨드센터 통합관제로 7종 73대 운영. 관제 화면 항목·장애 통계 언급 없음 (재인용: 2026-10-09-14)
- **f18**: Offshore Technology 기사: 점검 로봇의 계기 판독·밸브 확인·누출 탐지, 운영자의 임무 직접 생성 (재인용: 2026-10-09-14)
- **f19**: 한국로봇산업진흥원 운행안전인증 안내: 인증 대상이 로봇과 관제장치 조합. 관제장치 항목의 세부 요건은 미확인 (재인용: 2026-10-09-14)
- **f20**: AI Incident Database 346 과 Hotel Technology News: 로봇이 단순 업무를 처리하지 못해 직원 개입, 로봇 인력 절반 철수 (재인용: 2026-10-09-14)
- **f21**: f16·f17·f20 의 출처를 대조한 도출. 원인별 통계는 어느 출처에도 없음.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 아니오 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/ros/diagnostics/blob/ros2/README.md | 아니오 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 아니오 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 예 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones | 2025-11-21 | 기사 | low | 2026-10-09 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-961 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 미확인 | 기사 | low | 2026-10-09 | https://incidentdatabase.ai/cite/346/ | 예 |
| ref-962 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 2019-01 | 기사 | low | 2026-10-09 | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ | 예 |

### 출처 요약

- **ref-051**: VDA 5050 로봇 상태 메시지 스키마. 필수 항목(errors·operatingMode·safetyState), 운용 모드 값, information 사용 제한, headerId 규칙을 확인했다(입력 원문 텍스트는 앞 13,220자 발췌).
- **ref-449**: VDA 5050 연결 상태 메시지 스키마. ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 과 유언 메시지 규칙.
- **ref-031**: 원문 미열람. VDA 5050 3.0.0 명세 본문. 오류 수준 네 단계와 오류 설명·조치 힌트 항목(이전 실행 2026-10-09-15 확인 내용 재인용).
- **ref-230**: MassRobotics AMR 상호운용 표준 JSON 스키마. identityReport·statusReport, 운용 상태 9값, 문자열 오류 코드 목록.
- **ref-111**: Open-RMF 작업 상태 스키마. 작업 상태 12값, 배차 상태·오류, 일시정지·재개·취소 기록, 예약 식별자.
- **ref-448**: Open-RMF 경보 메시지 정의. 심각도 세 등급, 응답 목록, 관련 작업 id.
- **ref-313**: Open-RMF 자동문 모드 메시지. closed·moving·open·offline·unknown 다섯 값.
- **ref-283**: Open-RMF 문 연동 장. 문 노드·문 어댑터(상태 감독자)의 역할과 토픽.
- **ref-445**: ROS 2 진단 시스템 README. /diagnostics 토픽, aggregator, 원격 기록 패키지 구성.
- **ref-447**: OpenTelemetry 명세 개요. 추적·지표·로그 신호, TraceId·SpanId, span 간 링크 정의(입력 원문 텍스트는 앞 13,834자 발췌).
- **ref-943**: 원문 미열람. 병원 의약품 배송 로봇의 승강기 연동과 승강기 가동률 구간별 성공률을 보고한 연구.
- **ref-944**: 원문 미열람. 한림대학교성심병원의 서비스 로봇 7종 73대와 커맨드센터 통합관제 운영 보도.
- **ref-995**: 원문 미열람. Equinor 시설의 4족 점검 로봇 운영(계기 판독·누출 탐지)과 운영자 임무 생성 보도.
- **ref-980**: 원문 미열람. 실외이동로봇 운행안전인증 제도 안내. 인증 대상은 로봇과 관제장치의 조합.
- **ref-961**: 원문 미열람. 헨나 호텔 로봇이 단순 업무를 처리하지 못한 사건 기록.
- **ref-962**: 원문 미열람. 헨나 호텔의 로봇 절반 철수와 직원 개입 부담 보도.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md | 3, 5, 7, 9, 11 | 갱신(차등): 섹션 3 — '같은 시간축·같은 어휘' 근거로 f14(시각 형식 차이)·f9(심각도 표현 차이)·f13(통신 원인 신호)·f15(사람 개입 범주) 추가 / 섹션 5 — 물류창고 가상 시나리오의 문·작업 상태·경보 서술을 오늘 원문으로 재확인(f6·f7·f8), 현장 유형별 사례를 나눠 추가: 병원 f16(승강기 혼잡 원인)·f17(통합관제, 원인 분석 비공개), 상업 시설 f20, 실외 f19, 기타 f18 / 섹션 7(주제 페이지로 분리된 절의 요약) — VDA 5050 필수 오류·운용 모드·information 제한(f1·f2), 오류 수준(f3), 연결 상태(f4), MassRobotics 오류 코드 형식(f5), Open-RMF 배차 오류·개입 기록(f6), OpenTelemetry 추적·링크(f11) / 섹션 9 — 로봇 내부 진단은 연계 대상(f10), 심각도 대응 규칙과 작업 식별자 연결은 직접 범위 후보(f9·f12) / 섹션 11 — oq-033·oq-073 부분 근거(f9), oq-210 부분 근거(f12), oq-074·oq-075 미해결(f21), 새 질문 2건. 다음 실행 후보: 37. 관제 화면·실행 기록(f7 경보), 22. 설비·건물 시스템 연동(f16). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 연결 상태 | Connection State (VDA 5050 connectionState) | VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다. |
| 경보 등급 | Alert Tier (Open-RMF Alert) | Open-RMF 경보 메시지가 운영자에게 보내는 경보의 심각도를 INFO·WARNING·ERROR 세 단계로 나타내는 필드다. |

## 열린 질문

새로 생긴 질문:

- MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 21. 상호운용 표준·적합성 | 근거: f9 | 종류: 일반
- VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f13 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - oq-033·oq-073 미해결: 세 규약 사이의 공식 대응표는 원문 어디에도 없음(f9 는 도출)
    - oq-210 부분 근거만: 작업 식별자와 추적 TraceId 를 잇는 표준 미확인(f12)
    - oq-074·oq-075 미해결: 원인별 발생 비율 공개 자료 미확인(f21)
    - ref-051 원문 텍스트가 앞 13,220자 발췌라 오류 객체 정의(errorLevel enum)는 이 원문에서 확인하지 못했고 f3 은 ref-031 재인용에 기댐
    - f16 구로병원 전체 성공률 분모 미확인
    - f19 운행안전인증 관제장치 항목의 세부 요건 미확인
    - 제조 공장 현장의 이상 탐지·원인 분석 사례는 이번 브리프에 없음
- 범위 경계 위반 의심:
    - f10: 센서·드라이버 수준 진단은 로봇 자체 지능·제어 경계라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 결과 수신으로 한정
    - f8·f16: 문 개폐 제어와 승강기 운행 제어는 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 상태 확인·원인 범주 반영
    - f18: 계기 판독·누출 탐지 자체는 로봇 인식 기능(연계 대상)이며 ROP 쪽은 점검 결과를 이상 판정·업무 시스템으로 넘기는 부분만 다뤄야 함
    - f19: 인증 판단은 인증 기관·운영자 쪽이며 실외 현장 제약으로만 반영
- 한계: 재실행 1회차(실행 컨텍스트에 retry_count 가 없어 1회차로 적음). 반려 사유 1(스키마 불일치: f9 가 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts 의 ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447, fetched_via inbox)와 이전 브리프(2026-10-09-14, 2026-10-09-15)의 기존 참고문헌만으로 브리프를 다시 구성했다. 새 f9 는 심각도 표현 비교로 [추정]이며 벤더 문서를 근거로 한 finding 은 하나도 없다(vendor_claim 대상 없음). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1367~ref-1396 은 쓰지 않았다. 재인용한 ref-031·ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 는 이번에 열지 않아 fetched false·source_unopened true 이고 신뢰도는 medium 이하다. 교차 확인 0건. 정정 요청 없음, 우선 지정 질문 없음, 입력 누락 없음. 현장 유형: 병원(f16·f17), 상업 시설(f20), 실외(f19), 기타(f18); 물류창고는 기존 5절 시나리오의 재확인(f6·f7·f8)만, 제조 공장 사례는 없음. L. AI·학습 기술 관련 새 finding 은 없어 47. AI·학습·적응과 모델 운영 연결(oq-315)은 그대로다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈을 섞지 않았다. 해결 제안한 열린 질문 없음.
