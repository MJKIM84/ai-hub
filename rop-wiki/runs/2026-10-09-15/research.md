# 리서치 브리프 2026-10-09-15

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-15 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 37. 관제 화면·실행 기록 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 병원 협약 단계 보도 1건뿐이고 물류창고·제조 공장·상업 시설·가정·실외·기타 사례가 '찾지 못했다'로 남아 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — 공통 상태 값 표준이 Open-RMF 작업 상태 스키마뿐이고(oq-237) MassRobotics·VDA 5050 의 상태·오류 수준 정의, 관제실 설계 표준(ISO 11064), 투명성 표준(IEEE 7001)이 없음. rmf-web 저장 설정(바뀐 출처) 확인 필요
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 실행 기록 보관 주체·기간 근거(oq-316, oq-239)와 사고 조사용 최소 기록 항목(oq-252) 없음
- 섹션 11. 열린 질문 — oq-131·oq-237·oq-238·oq-239·oq-240·oq-252·oq-316 해결 근거 미조사
- 정정 요청 없음, 발행 2년이 지난 표준 수치 재확인 대상은 ISA-101 계열(본문 유료, 이번에 재열람하지 않음)

## 조사 질문

1. 운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
2. oq-237 여러 제조사 로봇의 작업 상태·실행 로그를 한 화면·한 기록으로 모을 때 Open-RMF 작업 상태 스키마 말고 공통 상태 값과 로그·오류 수준을 정한 공개 규약이 있는가? (섹션 7·9 겨냥)
3. oq-238·oq-240 설명 가능한 표시를 실제 플릿 관제 화면에서 측정한 연구가 있는가, 다중 로봇 관제 화면에 쓸 수 있는 화면·관제실 설계 표준이나 투명성 표준은 무엇인가? (섹션 7·11 겨냥)
4. oq-252·oq-316·oq-239 사고 조사용 최소 기록 항목, 고위험 AI 자동 사건 기록의 보관 기간·주체, 병원 특수 물품 배송 기록의 국내 보관 요건은 무엇인가? (섹션 9·11 겨냥)
5. 물류창고·실외·가정·기타 현장과 국내 병원에서 여러 로봇을 하나의 관제 화면으로 운영한 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)
6. 바뀐 출처와 oq-131: Open-RMF rmf-web 의 실행 기록 저장 설정은 바뀌었는가, 로봇 물류 실행 기록을 객체 중심 이벤트 로그로 만든 공개 사례가 있는가? (섹션 7·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 로봇이 보고하는 동작 상태 값을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 로, 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고, 오류마다 사람이 읽는 설명(errorDescription)·조치 힌트(errorHint)와 ISO 639-1 언어 코드별 번역을 담을 수 있게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 로봇이 state 메시지의 information 배열로 보내는 부가 정보를 플릿 관제가 로직에 쓰지 말고 시각화·디버깅에만 쓰게 하며, logReport 즉시 동작으로 로봇에 로그 보고서 생성·저장을 요청하고 저장된 로그 이름을 동작 상태로 보고받게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | MassRobotics AMR 상호운용 표준의 statusReport 는 uuid·timestamp·operationalState·location 을 필수로 하고, operationalState 를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 정하며, 오류 코드 배열, 약 10초의 단기 경로(예측 위치 최대 10개), 목적지, 배터리 잔량을 선택 항목으로 둔다. | ref-253 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f4 | [사실] | Open-RMF 작업 상태 스키마는 작업 상태 값 12개와 별도로 배차 상태를 queued·selected·dispatched·failed_to_assign·canceled_in_flight 로 기록하고, 요청자(requester)·예약 라벨과 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다 요청 시각과 라벨(예: dashboard)을 남기게 해, 누가 어떤 창구로 작업에 개입했는지를 실행 기록에 담을 수 있다. | ref-111 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f5 | [추정] | Open-RMF 작업 상태 스키마 말고도 VDA 5050(동작 상태·오류 수준)과 MassRobotics 상호운용 표준(운용 상태)이 공개된 상태 값 집합을 정하지만 세 규약의 값 집합과 단위(작업·동작·로봇)가 서로 달라, 37. 관제 화면·실행 기록에서 여러 제조사 상태를 한 기록으로 모으려면 ROP 가 대응표를 만들어 정규화해야 할 것으로 보인다. | ref-031, ref-253, ref-111 | 아니오 | low | 2026-10-09 | — | — |
| f6 | [사실] | Open-RMF rmf-web 의 API 서버는 기본으로 메모리 안의 SQLite 를 써서 실행 기록이 남지 않지만, 설정의 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 지정해 영속 저장할 수 있다. | ref-762, ref-302 | 아니오 | medium | 2026-10-09 | — | — |
| f7 | [사실] | Open-RMF 로그 항목(log_entry) 스키마는 오늘 기준으로도 순번(seq)·수준(tier)·밀리초 유닉스 시각·본문을 필수로 하고 수준 값을 uninitialized·info·warning·error 로 두어, 페이지 7절의 로그 수준 서술이 그대로 유효하다. | ref-1095 | 아니오 | medium | 2026-10-09 | — | — |
| f8 | [사실] | IEEE 7001-2021(자율 시스템 투명성 표준)은 사용자, 검증·인증 담당자, 고장·사고 조사자, 소송·행정 절차의 전문 자문가, 일반 대중의 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 객관적으로 평가할 수 있는 다섯 단계의 투명성 수준을 정하며, IEEE 로봇·자동화 학회가 공동 후원했다. | ref-1338 | 아니오 | medium | 2022-05-11 | — | — |
| f9 | [추정] | IEEE 7001-2021 이 운영자(사용자)와 사고 조사자를 별도 이해관계자로 두므로, 37. 관제 화면·실행 기록의 설명 가능한 표시는 운영자용 투명성으로, 실행 기록은 조사자용 투명성으로 나눠 평가하는 근거가 될 수 있을 것으로 보이나, 표준이 화면 설계나 기록 항목을 정하는지는 확인하지 못했다. | ref-1338 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | ISO 11064(관제 센터 인간공학 설계) 계열은 설계 원칙, 관제 공간 배치, 관제실 배치, 작업대 배치·치수, 표시 장치와 조작기, 환경 요건, 관제 센터 평가 원칙, 특정 적용의 인간공학 요건의 여러 부로 나뉜다. | ref-1349 | 아니오 | medium | 2000 | — | — |
| f11 | [사실] | Winfield 외(2022-05, ICRES 2022 제출)는 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 같은 운용 데이터를 안전하게 기록하는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스의 공개 표준 초안을 첫 초안으로 내놓았다. | ref-1120 | 아니오 | medium | 2022-05-13 | 예외·성과 | — |
| f12 | [추정] | 윤리적 블랙박스 초안은 로봇 한 대의 내부 기록을 대상으로 하므로, 여러 제조사 로봇을 지휘하는 플랫폼 수준의 명령·정지·재가동 기록 항목을 정한 공개 규약은 이번 조사에서도 확인하지 못해 oq-252 는 열린 채로 남는 것으로 보인다. | ref-1120, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f13 | [사실] | EU AI Act 제12조는 고위험 AI 시스템이 수명 동안 사건을 자동 기록(로그)할 수 있게 기술적으로 갖추고, 그 기록이 위험 상황·실질적 변경의 식별, 출시 후 모니터링, 배포자의 운용 모니터링(제26조 제5항)을 뒷받침하게 한다. | ref-863 | 아니오 | medium | 2024-07-12 | — | — |
| f14 | [사실] | EU AI Act 는 고위험 AI 의 자동 생성 로그를 공급자(제19조 제1항)와 배포자(제26조 제6항)가 각자 통제하는 범위에서 목적에 맞는 기간, 최소 6개월 보관하게 하고, 다른 EU·회원국 법(특히 개인정보 보호법)이 다르게 정하면 그에 따르게 한다. | ref-1341, ref-1342 | 아니오 | medium | 2024-07-12 | — | — |
| f15 | [추정] | 연계 대상: 로봇 플랫폼의 AI 구성요소가 고위험 AI 인지의 판단은 법무·규제 영역이며, 해당한다면 플랫폼 실행 기록의 보관 의무는 그 로그를 공급자와 배포자 중 누가 통제하는지에 따라 나뉘므로 ROP 는 보관 기간 설정과 통제 주체 표시를 기록 기능으로 갖추는 쪽을 맡을 것으로 보인다(oq-316 부분 근거). | ref-863, ref-1341, ref-1342 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | 한림대학교성심병원은 2024-04 기준 안내·배송·방역 로봇 등 7종 73대의 서비스 로봇을 커맨드센터의 통합관제시스템으로 운영하며, 커맨드센터 담당자는 서로 다른 제조사 로봇을 하나의 관제시스템으로 연결하는 일이 중요하다고 밝혔다. | ref-1344, ref-944 | 예 | medium | 2024-04-20 | 병원 / 수행 자원 | — |
| f17 | [사실] | 같은 보도에 따르면 한림대학교성심병원의 로봇 서비스는 2022-08 부터 2024-03 까지 3만 1607건 시행되었으나, 관제 화면 항목이나 배송 이력 조회 방식은 공개되지 않았다. | ref-1344 | 아니오 | low | 2024-04-20 | 병원 / 예외·성과 | — |
| f18 | [추정] | LG CNS 는 Open-RMF 를 바탕으로 한 로봇 통합운영 플랫폼에서 고객이 로봇의 이동 동선과 작업 처리 결과를 실시간으로 한눈에 확인할 수 있고 AGV·AMR·오토스토어·소팅로봇이 연계되어 있으며, G마켓 동탄 물류센터에서 기술검증에 착수했다고 밝혔다. | ref-1343 | 아니오 | low | 2023-07-06 | 물류창고 / 수행 자원 | 벤더 주장 |
| f19 | [사실] | 국내 실외이동로봇 운행안전인증은 속도 제어·비상정지·장애물 감지·횡단보도 통행·운행구역 준수·관제 장치 등 16개 항목을 평가하고 로봇과 관제장치의 조합에 인증을 주므로, 실외 현장에서는 관제 장치가 운행 제약의 하나가 된다. | ref-1345, ref-980 | 아니오 | low | 2024-01-31 | 실외 / 제약 | — |
| f20 | [사실] | 농촌진흥청의 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다. | ref-1007 | 아니오 | low | 2025-04-23 | 기타 / 수행 자원 | 원문 미열람 |
| f21 | [사실] | LH토지주택연구원 자료를 인용한 보도는 공동주택 단지 로봇 택배에서 택배 차량이 단지 집하처에 송장번호를 인식시키면 물품 정보가 관제실로 전달된다고 전한다. | ref-976 | 아니오 | low | 2024-07-18 | 가정 / 시작 조건 | 원문 미열람 |
| f22 | [사실] | Patel 외(2021)는 여러 운영자가 다중 로봇을 함께 감독할 때의 투명성을 다루며, 자기 작업 정보만 보이는 방식·다른 운영자 작업 정보를 공유하는 방식·둘을 섞은 방식·없음의 네 모드를 참가자 18명의 사용자 연구로 비교해 인식·신뢰·작업 부하를 쟀다. | ref-1347 | 아니오 | medium | 2021-05-14 | — | — |
| f23 | [추정] | 이번에 확인한 설명 가능한 표시·투명성 연구도 실험실 사용자 연구 수준이어서, 실제 운영 중인 로봇 플릿 관제 화면에서 운영자의 상황 인식과 대응 시간을 측정한 공개 연구는 여전히 확인하지 못해 oq-238 은 열린 채로 남는 것으로 보인다. | ref-1347, ref-1099 | 아니오 | low | 2026-10-09 | — | — |
| f24 | [사실] | Rohrer 외(2022)는 공장 물류를 모사한 RoboCup Logistics League 시뮬레이션의 사건을 데이터베이스에서 꺼내 로봇·주문·부품 객체와 11개 활동을 담은 객체 중심 이벤트 로그(OCEL JSON)로 만들고, 다음 사건과 그 시각을 예측하는 데 썼다. | ref-1348 | 아니오 | medium | 2022-07-20 | — | — |
| f25 | [추정] | 로봇 물류 실행 기록을 로봇·주문·부품 객체 중심 이벤트 로그로 만든 공개 사례는 있으나 그 로그를 시뮬레이션 시나리오 사양으로 되돌리는 변환 규칙은 이번에도 확인하지 못해, oq-131 에는 기록 쪽 형식만 부분 근거가 된 것으로 보인다. | ref-1348 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

- **f1**: 6.6.5.1 오류 수준 4단계(WARNING 은 즉시 조치 불필요, FATAL 은 사용자 개입 필요), 표 5 동작 상태 열, 6.6.5.3 errorDescriptionTranslations·errorHintTranslations (발행일 미확인, 확인일 기준)
- **f2**: 6.6.4: fleet control shall not use the information for logic; only for visualization and debugging. 표 4·5 logReport(reason) — 보고서 저장 시 FINISHED, 로그 이름을 동작 상태에 포함 (발행일 미확인, 확인일 기준)
- **f3**: AMR_Interop_Standard.json statusReport: required uuid, timestamp, operationalState, location; errorCodes 는 정상 운행 중 생략; path 는 short-term path of about 10 seconds (발행일 미확인, 확인일 기준)
- **f4**: task_state.json $defs.dispatch.status enum, booking.requester, interruptions·cancellation·killed·skip_requests 의 unix_millis_request_time 과 labels(`dashboard` 또는 `app=dashboard`) (발행일 미확인, 확인일 기준)
- **f5**: VDA 5050 은 동작 단위 상태와 오류 수준, MassRobotics 는 로봇 단위 운용 상태, Open-RMF 는 작업·단계·사건 단위 상태를 정한다. 세 규약 사이의 공식 대응표는 이번 조사에서 확인하지 못했다
- **f6**: api-server README: "by default it uses a in-memory sqlite instance"; db_url 형식 DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME, PostgreSQL 은 rmf-server[postgres] 설치. 상위 README 도 기본은 internal non-persistent database (발행일 미확인, 확인일 기준)
- **f7**: log_entry.json required: seq, tier, unix_millis_time, text; tier enum uninitialized, info, warning, error (발행일 미확인, 확인일 기준)
- **f8**: IEEE SA 기사(2022-05-11): "specific, measurable levels of transparency that can be assessed objectively". 표준 본문은 열지 않았고 기사 기준
- **f9**: 기사는 사용자에게 시스템이 무엇을 왜 하는지 이해할 간단한 방법이 필요하다고 쓰지만 이벤트 기록 장치나 화면 요건을 표준이 정한다고는 쓰지 않는다
- **f10**: ISO 11064-1:2000 미리보기의 머리말: Part 5 "Displays and controls", Part 7 "Principles for the evaluation of control centres" 등 8개 부. 적용 범위 절은 미리보기에 없어 확인하지 못함
- **f11**: 초록: securely recording operational data (sensor, actuator and control decisions) for a social robot, 사고 조사를 위한 비행 기록 장치에 상응. 부록의 기록 항목·보관 기간은 PDF 를 읽지 못해 미확인
- **f12**: 초안은 단일 소셜 로봇 기준. VDA 5050 의 logReport 는 로봇 쪽 로그 생성을 요청할 뿐 기록 항목을 정하지 않는다
- **f13**: Article 12(1): "automatic recording of events (logs) over the lifetime of the system"; 12(2) 세 목적(제79조 제1항 위험·실질적 변경, 제72조 출시 후 모니터링, 제26조 제5항 운용 모니터링)
- **f14**: Art.19(1) logs kept for a period appropriate to the intended purpose, of at least six months, 공급자가 계약·법에 따라 통제하는 범위. Art.26(6) 배포자도 to the extent such logs are under their control
- **f15**: 제19조·제26조가 모두 '통제하는 범위에서' 보관하게 하므로 계약상 통제 주체가 보관 주체를 가른다. 로봇 플랫폼에 대한 적용 해석 자료는 찾지 못함
- **f16**: 코메디닷컴(2024-04-20): "각기 다른 제조사의 로봇들을 하나의 관제시스템으로 연결하는 일이 중요하다", 7종 73대. 로봇신문(2024-04-15)도 7종 73대·통합관제 보도(재인용: 2026-10-09-14)
- **f17**: 2022년 8월~2024년 3월 3만 1607건 서비스 시행. 실시간 모니터링·문제 대응 업무 서술이나 화면 구성은 기사에 없음
- **f18**: 벤더 주장: 2023-07-06 보도자료. 로봇 이동 동선·작업 처리 결과 실시간 확인, G마켓과 동탄 물류센터 PoC 착수, 로보셔틀·소형 피킹로봇 연동 검증 예정. 운영 결과는 미공개
- **f19**: 바이라인네트워크(2024-01-31): 16개 항목 평가, 모든 기준을 만족해야 인증. 로봇·관제장치 조합 인증은 한국로봇산업진흥원 안내(재인용: 2026-10-09-14). 관제 장치 항목의 세부 요건은 미확인
- **f20**: 뉴스토마토(2025-04-23) 보도 기준 (재인용: 2026-10-09-14)
- **f21**: 정보통신신문(2024-07-18) 보도 기준, 시나리오 단계 서술 (재인용: 2026-10-09-14)
- **f22**: arXiv 2101.10495 초록: transparency modes none, central, peripheral, mixed; user study with 18 participants on a complex multi-robot task. 현장 평가는 없음
- **f23**: Patel 외 18명 사용자 연구, Roldán 외 24명 실험실 비교(재인용: 2026-09-30-13). 현장 측정 자료는 검색 2회(영어)로 찾지 못함
- **f24**: 본문: RCLL 은 "a simulation of factory logistics", 활동 예 deliver·mount-first-ring·fill-cap, 이벤트 id·활동·시각·객체 유형을 OCEL JSON 으로 저장. 로그 규모는 표가 깨져 미확인
- **f25**: Rohrer 외는 예측 모니터링 목적이며 시나리오 생성은 다루지 않음

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-1095 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 아니오 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 | 2025-04-23 | 기사 | low | 2026-10-09 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 예 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 2024-07-18 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=123976 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 예 |
| ref-253 | MassRobotics (MassRobotics-AMR/AMR_Interop_Standard) | AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-1338 | IEEE Standards Association | How To Make Autonomous Systems More Transparent and Trustworthy | 2022-05-11 | 표준 | medium | 2026-10-09 | https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy | 아니오 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 아니오 |
| ref-863 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 12: Record-keeping | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 아니오 |
| ref-1341 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 19: Automatically generated logs | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19 | 아니오 |
| ref-1342 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 26: Obligations of deployers of high-risk AI systems | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 | 아니오 |
| ref-1343 | LG CNS (LG 미디어 보도자료) | ‘로봇 통합운영 플랫폼’ 개발 | 2023-07-06 | 벤더 문서 | low | 2026-10-09 | https://lg.co.kr/media/release/26480 | 아니오 |
| ref-1344 | 코메디닷컴 | [메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠 | 2024-04-20 | 기사 | low | 2026-10-09 | https://kormedi.com/1682189/ | 아니오 |
| ref-1345 | 바이라인네트워크 (이진호) | 뉴빌리티, 실외이동 로봇 운행안전 인증 획득 | 2024-01-31 | 기사 | low | 2026-10-09 | https://byline.network/2024/01/240131_00004/ | 아니오 |
| ref-762 | Open Robotics (open-rmf/rmf-web) | rmf-web packages/api-server — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-1347 | Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv) | Transparency in Multi-Human Multi-Robot Interaction | 2021-05-14 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2101.10495 | 아니오 |
| ref-1348 | Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv) | Predictive Object-Centric Process Monitoring | 2022-07-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2207.10017 | 아니오 |
| ref-1349 | ISO (ANSI Webstore 미리보기) | ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview) | 2000 | 표준 | medium | 2026-10-09 | https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문(입력의 원문 텍스트). 동작 상태 값, 오류 수준 4단계와 번역, information 배열의 시각화·디버깅 전용 규칙, logReport 즉시 동작을 확인했다.
- **ref-111**: Open-RMF 작업 상태 JSON 스키마(입력의 원문 텍스트). 배차 상태 값, 요청자·라벨, 일시정지·취소·강제 종료·건너뛰기 요청 기록 구조를 확인했다.
- **ref-302**: rmf-web 저장소 README. API 서버·API 클라이언트·대시보드 프레임워크 구성과 기본 비영속 내부 데이터베이스 사용을 다시 확인했다.
- **ref-1095**: Open-RMF 로그 항목 스키마. 필수 필드 seq·tier·unix_millis_time·text 와 수준 값 네 개를 다시 확인했다.
- **ref-944**: 원문 미열람. 한림대성심병원의 7종 73대 서비스 로봇 통합관제 운영 보도(이전 실행 2026-10-09-14 확인 내용 재인용).
- **ref-1007**: 원문 미열람. 농촌진흥청이 자체 개발 농업 로봇 3종을 하나의 화면으로 관리하는 통합 관리 프로그램 보도(재인용).
- **ref-976**: 원문 미열람. LH토지주택연구원 자료를 인용한 공동주택 로봇 택배 관제실 연동 시나리오 보도(재인용).
- **ref-980**: 원문 미열람. 실외이동로봇 운행안전인증 안내. 인증이 로봇과 관제장치의 조합에 주어진다(재인용).
- **ref-1099**: 원문 미열람. 운영자 24명이 다중 로봇 임무를 감독한 실험실 인터페이스 비교 연구(이전 실행 2026-09-30-13 확인 내용 재인용).
- **ref-253**: MassRobotics 공식 저장소의 상호운용 표준 JSON 스키마. identityReport·statusReport 필드와 operationalState 아홉 값을 정한다.
- **ref-1338**: IEEE 7001-2021(자율 시스템 투명성 표준)을 소개하는 IEEE SA 공식 글. 이해관계자 범주 다섯과 범주별 다섯 단계 투명성 수준을 설명한다. 표준 본문은 열지 않았다.
- **ref-1120**: 소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록해 사고·아차 사고 조사를 돕는 윤리적 블랙박스의 공개 표준 초안. 초록만 확인했고 부록(표준 본문)은 PDF 추출 실패로 읽지 못했다.
- **ref-863**: EU AI Act 제12조. 고위험 AI 의 수명 동안 자동 사건 기록 기능과 기록이 뒷받침해야 할 세 목적을 정한다.
- **ref-1341**: EU AI Act 제19조. 공급자가 통제하는 자동 생성 로그를 목적에 맞는 기간, 최소 6개월 보관하게 한다.
- **ref-1342**: EU AI Act 제26조. 제6항이 배포자가 통제하는 자동 생성 로그를 최소 6개월 보관하게 한다.
- **ref-1343**: LG CNS 의 Open-RMF 기반 로봇 통합운영 플랫폼 발표와 G마켓 동탄 물류센터 기술검증 착수 보도자료. 기능 서술은 벤더 주장이다.
- **ref-1344**: 한림대의료원 커맨드센터 파트장 인터뷰. 7종 73대 서비스 로봇, 통합관제시스템, 2022-08~2024-03 누적 3만 1607건 서비스.
- **ref-1345**: 실외이동로봇 운행안전인증이 관제 장치를 포함한 16개 항목을 평가한다는 보도. 관제 장치 항목의 세부는 없다.
- **ref-762**: rmf-web API 서버 README. 기본은 메모리 내 SQLite 이고 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 설정한다.
- **ref-1347**: 여러 운영자–다중 로봇 상호작용에서 네 가지 투명성 모드를 참가자 18명 사용자 연구로 비교한 프리프린트(초록 확인).
- **ref-1348**: RoboCup Logistics League 시뮬레이션 사건을 객체 중심 이벤트 로그(OCEL)로 만들어 다음 사건·시각을 예측한 프리프린트. 본문은 ar5iv 로 열었다.
- **ref-1349**: ISO 11064-1:2000 미리보기(표지·목차·머리말·서론). 계열의 8개 부 제목을 확인했고 적용 범위 절과 본문은 미리보기에 없다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md | 5, 7, 9, 11 | 갱신(차등): 섹션 5 — 병원 사례에 f16(7종 73대 통합관제, 교차 확인)·f17(누적 3만 1607건) 추가, 물류창고 f18('벤더 주장' 병기, 흐름 단계는 서술하지 않음), 실외 f19(관제 장치가 인증 항목·제약), 기타 f20, 가정 f21 을 현장 유형마다 나눠 '찾지 못했다' 문장 교체. 제조 공장·상업 시설은 이번에도 찾지 못함 / 섹션 7 — 표에 MassRobotics statusReport(f3), VDA 5050 동작 상태·오류 수준·information·logReport(f1·f2), Open-RMF 배차 상태·개입 기록(f4), IEEE 7001-2021(f8), ISO 11064(f10), 윤리적 블랙박스 초안(f11) 행 추가, rmf-web 행을 '기본은 메모리 내 SQLite, db_url 로 영속 DB 설정'으로 갱신(f6, 바뀐 출처), 로그 수준 재확인(f7) / 섹션 9 — 상태 값 정규화를 직접 범위에(f5), EU AI Act 로그 보관 기간·주체를 연계 대상으로(f13·f14·f15) / 섹션 11 — oq-237 해결 제안(f1·f3·f4·f5), oq-238 미해결(f22·f23), oq-240 부분 근거(f8·f9·f10), oq-252 부분 근거(f11·f12), oq-316 부분 근거(f13·f14·f15), oq-131 부분 근거(f24·f25), oq-239 미해결, 새 질문 2건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석(f1 오류 수준·f10 ISO 11064), 59. 법·규제·보험·라이선스(f13·f14), 50. 안전 표준·인증·사고 조사(f11), 66. 실외(f19) 페이지 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 운용 상태 | Operational State (MassRobotics statusReport operationalState) | MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다. |
| 동작 상태 | Action Status (VDA 5050 actionStatus) | VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다. |
| 자율 시스템 투명성 수준 | Transparency Level (IEEE 7001-2021) | IEEE 7001-2021 이 사용자·인증 담당자·사고 조사자 등 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 다섯 단계로 정한, 객관적으로 평가할 수 있는 투명성 등급이다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? | 관련 영역: 37. 관제 화면·실행 기록, 21. 상호운용 표준·적합성 | 근거: f5 | 종류: 일반
- 국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? | 관련 영역: 37. 관제 화면·실행 기록, 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-237

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 14회 · 신규 출처 13건
- 미확인 항목:
    - oq-239 미해결: 마약류 관리에 관한 법률 시행규칙의 장부·기록 2년 보존 조문을 국가법령정보센터에서 열지 못했고(본문 미표시) 검색 결과는 기사·비공식 법령 사이트뿐이라 근거로 쓰지 않음. 로봇 배송 이력 자체의 보관 요건은 확인하지 못함
    - f11 윤리적 블랙박스 초안 부록(기록 항목·보관 시간 창·보안 요건): PDF 텍스트 추출 실패로 미확인
    - f8 IEEE 7001-2021 본문 미열람(IEEE SA 소개 글 기준), 화면·기록 요건 포함 여부 미확인
    - f10 ISO 11064-1 적용 범위 절 미확인(미리보기에 없음). 검색 요약에 나온 '교통·물류 관제 시스템 포함' 범위 문구는 원문으로 확인하지 못해 넣지 않음
    - f19 운행안전인증 16개 항목 중 관제 장치 항목의 세부 요건 미확인, ref-980 이번 실행에서 다시 열지 않음
    - f16 의 ref-944 와 f20·f21 출처는 이전 실행 확인 내용 재인용이며 이번에 다시 열지 않음
    - f18 LG CNS 플랫폼 기능과 G마켓 동탄 기술검증 결과는 벤더 보도자료뿐이며 독립 확인하지 못함
    - 제조 공장·상업 시설의 관제 화면·실행 기록 사례는 이번에도 찾지 못함
    - f24 RCLL 로그 규모는 표가 깨져 미확인
- 범위 경계 위반 의심:
    - f15: 고위험 AI 해당 여부와 로그 보관 의무 해석은 법무·규제 쪽 연계 대상이라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 보관 기간 설정·통제 주체 표시로 한정
    - f19: 운행안전인증 판단은 인증 기관·운영자 쪽이며 ROP 에는 실외 현장 제약으로만 반영 제안
    - f11·f12: 윤리적 블랙박스의 센서·구동기 기록은 로봇 자체 지능·제어 쪽 기록이므로 ROP 직접 범위가 아니라 플랫폼 수준 기록 항목의 비교 대상으로만 씀
    - f2: VDA 5050 logReport 로 만드는 로그는 로봇 쪽 기록(연계 대상)이며 ROP 는 요청과 결과 이름 수신만 맡는다고 서술해야 함
- 한계: web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청이 없어 빈·약한 절(5절 현장 사례, 7절 표준, 9절 기록 보관 경계, 11절 열린 질문)과 바뀐 출처(rmf-web 저장 설정)만 조사했다. 검색 14회/30, 신규 출처 13건/15(ref-253~ref-1349, 예약 구간 안), 재사용 9건. 신규 출처는 모두 원문 또는 공식 페이지를 열었다(webfetch 10, github_raw 2, 미리보기 1). 재사용 가운데 ref-031·ref-111 은 입력의 원문 텍스트(inbox), ref-302·ref-1095 는 github_raw 로 다시 열었고, ref-944·ref-1007·ref-976·ref-980·ref-1099 는 다시 열지 않아 source_unopened 로 표시했다. 교차 확인 1건(f16, 7종 73대 통합관제: 코메디닷컴·로봇신문). oq-237 해결 근거: f1·f3·f4·f5(Open-RMF 외에 VDA 5050 과 MassRobotics 가 공개 상태 값을 정함, 대응표는 없음 — 새 질문으로 올림). oq-238·oq-239 는 미해결, oq-131·oq-240·oq-252·oq-316 은 부분 근거만. 현장 유형: 병원(f16·f17), 물류창고(f18, 벤더 주장), 실외(f19), 기타(f20), 가정(f21). 제조 공장·상업 시설 사례는 검색 1회로 찾지 못했다. 벤더 주장 1건(f18). 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 섞지 않았고 f24·f25 는 기록 형식으로만 다뤘다. 핵심 질문에 대한 새 결론은 없으며 '무엇'의 표시 근거(상태 값 규약)만 보강되었다. 용어집에 이미 있는 윤리적 블랙박스·자동 사건 기록·HMI 철학·객체 중심 이벤트 로그는 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
