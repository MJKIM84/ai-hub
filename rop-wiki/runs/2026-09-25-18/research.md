# 리서치 브리프 2026-09-25-18

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-18 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 8. 실시간 세계 상태·데이터 일관성 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 시각 개념(발생 시각·기록 시각·허용 경과 시간), 상태 품질, 정정 이벤트 용어 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 22. 시뮬레이션·예측용 디지털 트윈과의 구분 근거 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [분류원문]
2. 로봇 관제 인터페이스(VDA 5050, Open-RMF)와 설비 인터페이스(문·승강기)는 상태를 얼마나 자주, 어떤 시각·품질 정보와 함께 보고하며, 연결이 끊기거나 상태가 오래되면 무엇을 규정하는가? (섹션 5·7 겨냥)
3. 메시지 계층(ROS 2 QoS, MQTT Sparkplug, OPC UA)은 정보의 오래됨(staleness)·순서 뒤바뀜·품질을 어떤 장치로 표현하는가? (섹션 4·6·7 겨냥)
4. 사건 기록 표준(GS1 EPCIS, W3C SOSA)은 발생 시각과 기록 시각, 잘못된 기록의 정정을 어떻게 다루는가? (섹션 4·6, 7. 화물·재고·자산 식별과 추적 연결)
5. 정보 신선도(Age of Information), 대상 지속성 모델, 복제 데이터 수렴(CRDT), 판독 데이터 정제 같은 연구는 세계 상태의 지연·누락·충돌·불확실성 관리에 어떤 방법을 주는가? (섹션 6·8 겨냥)
6. 재고 기록과 실물의 불일치는 얼마나 흔하며, 디지털 트윈 분류(디지털 모델·섀도·트윈, ISO 23247)는 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 경계에 어떤 기준을 주는가? (섹션 3·10 겨냥, 국내 연구 포함)
7. 세계 상태 관리에서 ROP가 직접 맡을 부분과 로봇 자체 위치추정·설비 제어에 맡길 부분의 경계는 어디인가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 이동로봇의 상태(state) 메시지를 주문 수신·적재 변화·오류·운전 상태 변화 같은 관련 사건이 생길 때, 그리고 적어도 30초마다 발행하도록 정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 연결 상태를 connection 토픽의 ONLINE·OFFLINE·CONNECTION_BROKEN 으로 알리며, 예기치 않게 끊기면 MQTT 브로커가 미리 등록된 유언(last will) 메시지로 CONNECTION_BROKEN 을 대신 발행하고, connection 토픽만 QoS 1 이고 order·state·visualization 등은 QoS 0(최선 노력)이다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [추정] | 이번에 연 VDA 5050 3.0.0 명세에서는 관제가 오래된 상태 메시지나 연결 끊김에 어떻게 대응해야 하는지, 시각 동기화 방식을 무엇으로 할지에 대한 규정을 찾지 못했다. | ref-031 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 공식 저장소 main 의 상태 스키마는 ISO 8601 시각(timestamp), 마지막 도달 노드(lastNodeId·lastNodeSequenceId), 새 base 요청(newBaseRequest), 지도별 위치와 위치추정 여부(localized)·위치추정 품질(localizationScore, 0~1)·위치 편차 범위(deviationRange)·지도 id(mapId), 취급 중인 적재물(loads), 일시정지·운전 모드·안전 상태를 담는다. | ref-051 | 아니오 | medium | 2026-09-25 | 피킹 / 작업 대상 | — |
| f5 | [사실] | Open-RMF API 로봇 상태 스키마는 밀리초 단위 시각(unix_millis_time), 지도 이름과 x·y·yaw 위치, 상태 7종(uninitialized·offline·shutdown·idle·charging·working·error), 운영자가 조치할 문제(issues), 배터리 충전 상태를 한 메시지에 담는다. | ref-148 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f6 | [사실] | Open-RMF 에서 문 장치 노드는 문 상태(DoorState: 시각 door_time, 문 이름, 현재 모드)를 /door_states 토픽으로 발행하고, 문 어댑터가 진행 중인 로봇 작업을 방해할 수 있는 요청을 막는 상태 감독자 역할을 하며, 어댑터를 거치지 않은 직접 요청은 어댑터가 이전 상태로 되돌린다. | ref-184, ref-186 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f7 | [사실] | Open-RMF 승강기 상태(LiftState)는 시각(lift_time), 현재·목적 층, 승강기 문 상태, 운행 상태, 운영 모드(사람·AGV·화재·오프라인·비상), 제어권을 받은 세션 id 를 담고, 승강기 어댑터는 승강기의 내부 상태와 목표 상태를 추적하다가 적절할 때만 요청을 승강기 노드로 넘긴다. | ref-185, ref-187 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f8 | [추정] | 이번에 연 Open-RMF 문·승강기 연동 문서에는 상태 발행 주기나 오래된 상태를 판정·처리하는 규칙이 적혀 있지 않았다. | ref-184, ref-185 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | ROS 2 QoS 는 연속 발행 사이의 최대 간격(Deadline), 발행에서 수신까지 이 시간을 넘으면 오래되었거나 만료된 것으로 보는 수명(Lifespan), 발행자가 살아 있음을 알려야 하는 최대 기간(Liveliness·Lease Duration)을 정책으로 두고, 기한 초과·생존성 상실을 이벤트 콜백으로 알린다. | ref-183 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f10 | [사실] | Eclipse Sparkplug 사양은 에지 노드의 NDEATH 를 받거나 호스트 애플리케이션이 MQTT 서버와 연결을 잃으면 관련 측정값을 모두 STALE 품질로 표시하게 하고, 0~255 순번(seq)으로 순서 뒤바뀜을 감지해 재정렬 대기 시간이 지나도 빠진 메시지가 오지 않으면 재탄생(Rebirth) 요청으로 전체 상태를 다시 받게 한다. | ref-188 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f11 | [사실] | OPC UA 의 DataValue 는 값과 함께 데이터 원천이 값에 붙인 시각(SourceTimestamp), 서버가 값을 받았거나 정확하다고 안 시각(ServerTimestamp), 값의 사용 가능성을 Good·Uncertain·Bad 로 나타내는 상태 코드(StatusCode)를 담는다. | ref-182 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f12 | [사실] | 정보 나이(Age of Information, AoI)는 수신 측이 가진 최신 갱신이 생성된 뒤 흐른 시간으로 정의되어, 개별 메시지의 지연이 아니라 수신 측 정보가 얼마나 최신인지를 재는 지표로 연구되어 왔다. | ref-189 | 아니오 | medium | 2021-05 | — | 원문 미열람 |
| f13 | [추정] | 분류 원문의 질문(30초 전 '문 열림' 정보로 지금 통과할 수 있는가)에 대해, 확인한 표준·프레임워크는 시각 필드·주기 발행·수명·생존성·STALE 표시 같은 장치만 주고 대상별 허용 경과 시간은 정하지 않으므로, ROP가 문·승강기 같은 대상마다 허용 경과 시간을 정하고 넘으면 통과를 확정하기 전에 설비 어댑터에 다시 요청·확인하는 규칙을 가져야 할 것으로 보인다. | ref-031, ref-183, ref-188, ref-184, ref-189 | 아니오 | low | 2026-09-25 | 적치 / 제약 | — |
| f14 | [사실] | GS1 EPCIS 온톨로지는 이벤트가 일어났다고 캡처 애플리케이션이 주장하는 시각(eventTime)과 저장소가 기록한 시각(recordTime)을 구분하고, 발생 장소의 시간대 차이(eventTimeZoneOffset)를 함께 둔다. | ref-045 | 아니오 | medium | 2021-09-30 | 완료·인계 | — |
| f15 | [사실] | EPCIS 는 앞선 이벤트가 틀렸다고 선언하는 오류 선언(errorDeclaration)에 선언 시각(declarationTime), 사유(CBV 의 did_not_occur·incorrect_data), 정정 이벤트 id 목록(correctiveEventIDs)을 두어, 원 기록을 지우지 않고 뒤 이벤트로 바로잡게 한다. | ref-045, ref-044 | 아니오 | medium | 2021-09-30 | 완료·인계 | — |
| f16 | [추정] | EPCIS 의 오류 선언 방식을 참고하면, ROP 의 세계 상태 이력도 잘못 들어온 상태(예: 인계 완료로 잘못 보고된 적재)를 덮어쓰지 않고 정정 기록을 덧붙이는 방식으로 두어야 인계 분쟁 때 원 기록과 정정 근거를 함께 추적할 수 있을 것으로 보인다. | ref-045, ref-044 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f17 | [사실] | W3C/OGC SOSA 는 관측 결과가 대상에 적용되는 시각(phenomenonTime)과 관측 활동이 끝난 시각(resultTime)을 구분해 정의한다. | ref-030 | 아니오 | medium | 2017-10-19 | — | 원문 미열람 |
| f18 | [추정] | SOSA(phenomenonTime·resultTime), EPCIS(eventTime·recordTime), OPC UA(SourceTimestamp·ServerTimestamp)가 모두 '사실이 성립한 시각'과 '시스템이 받거나 기록한 시각'을 나누므로, ROP 세계 상태의 각 값에도 최소한 이 두 시각과 품질 표시를 함께 두어야 오래됨·순서 역전을 판단할 수 있을 것으로 보인다. | ref-030, ref-045, ref-182 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [사실] | Open-RMF 의 교통 일정(traffic schedule) 데이터베이스는 각 플릿이 보고한 로봇 예정 경로를 모아 지연·취소·경로 변경을 계속 반영하는 살아 있는 데이터베이스로, 충돌이 예상되면 관련 플릿 관리자에게 알려 협상을 시작하게 한다. | ref-004 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f20 | [사실] | DeHoratius·Raman(2008)은 한 소매업체 37개 매장의 재고 기록 약 37만 건을 조사해 65%가 실물과 맞지 않았고, 실사(audit)는 부정확성을 줄이며 매장 환경의 복잡성과 유통 구조는 늘린다고 보고했다. | ref-192 | 아니오 | medium | 2008 | 보충 / 예외·성과 | 원문 미열람 |
| f21 | [추정] | 재고 기록이 실물과 자주 어긋난다는 연구 결과로 볼 때, ROP의 화물 상태는 WMS 기록을 그대로 참값으로 두지 말고 로봇이 보고한 적재물 식별(VDA 5050 loads)이나 판독 결과를 대조 근거로 함께 보관해 불일치를 드러내야 할 것으로 보인다. | ref-192, ref-051 | 아니오 | low | 2026-09-25 | 피킹 / 작업 대상 | — |
| f22 | [사실] | RFID 판독 스트림에는 놓친 판독(false negative)과 잘못된 판독(false positive)이 섞이며, 판독 데이터 정제 연구는 창 크기를 적응적으로 바꾸는 슬라이딩 윈도(SMURF 등)로 이를 줄이고, 이동 태그 환경을 겨냥한 WSTD 는 SMURF 보다 전체 오류가 약 30% 적었다고 보고했다. | ref-194 | 아니오 | medium | 2012 | 입고 / 완료·인계 | 원문 미열람 |
| f23 | [사실] | Perpetua(IROS 2025)는 반정적 환경에서 관측 사이에 사라지거나 다시 나타나는 요소를 지속(persistence)·출현(emergence) 필터의 혼합으로 베이즈 방식으로 모델링해, 마지막 관측 뒤 요소의 현재·미래 상태를 확률로 예측한다. | ref-193 | 아니오 | medium | 2025-07 | — | 원문 미열람 |
| f24 | [사실] | 무충돌 복제 데이터 타입(CRDT)은 각 복제본을 다른 복제본과 조율하지 않고 수정할 수 있고, 같은 갱신 집합을 받은 복제본들이 수학적으로 정해진 규칙에 따라 결정적으로 같은 상태에 수렴하도록 설계된 데이터 타입이다. | ref-196 | 아니오 | medium | 2018-05 | — | 원문 미열람 |
| f25 | [추정] | CRDT 식 수렴은 관측 기록 모음처럼 순서와 무관하게 합칠 수 있는 상태에는 맞지만, 문·승강기 사용권처럼 한 시점에 하나의 주체만 가져야 하는 자원은 Open-RMF 문·승강기 어댑터나 승강기 세션처럼 단일 감독자가 판정하는 구조가 필요할 것으로 보인다. | ref-196, ref-184, ref-185 | 아니오 | low | 2026-09-25 | 제약 | — |
| f26 | [사실] | ISO 23247 은 제조 디지털 트윈을 관측 가능한 제조 요소(인력·장비·자재·공정·시설·환경·제품·지원 문서)의 목적에 맞는 디지털 표현으로서 요소와 표현 사이에 동기화가 있는 것으로 정의하고, 장비 상태 변화를 모으는 장치 통신 계층과 모델을 갱신하는 디지털 트윈 계층을 나눈다. | ref-190 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f27 | [사실] | Kritzinger 외(2018)는 제조 디지털 트윈 문헌을 통합 수준으로 분류해, 물리 대상과 자동 데이터 교환이 없는 디지털 모델, 물리→디지털 한 방향 자동 흐름이 있는 디지털 섀도(digital shadow), 양방향 자동 흐름이 있는 디지털 트윈을 구분했다. | ref-191 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f28 | [추정] | 8. 실시간 세계 상태·데이터 일관성이 다루는 현재 상태 표현은 현장에서 자동으로 갱신되는 표현(디지털 섀도, ISO 23247 의 동기화된 표현)에 가깝고, 그 표현을 복제해 가정한 미래를 실험하는 쪽은 22. 시뮬레이션·예측용 디지털 트윈의 몫으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다. | ref-191, ref-190 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f29 | [사실] | 김지형(2023)은 국내 학술지 게재 논문에서 OPC UA 와 상용 연결 솔루션(FLEXING CPS·FLEXING EDGE)으로 이기종 로봇과 PLC 의 데이터를 수집해 실시간 3D 디지털 트윈을 구축하는 설계·구현을 제시했다. | ref-195 | 아니오 | medium | 2023 | 수행 자원 | 원문 미열람 |
| f30 | [추정] | 연계 대상: 로봇의 위치추정과 그 품질 계산은 분류 원문 9장의 로봇 자체 지능·제어 쪽이며, ROP 는 로봇이 보고한 위치추정 여부·품질 점수·편차 범위와 보고 시각을 받아 그 위치를 얼마나 믿을지 판단하는 쪽을 맡는 것으로 보인다. | ref-051 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f31 | [추정] | ROP 의 직접 범위는 로봇 관제 인터페이스(VDA 5050·Open-RMF)의 로봇 상태, 설비 어댑터의 문·승강기 상태, EPCIS 같은 업무 이벤트를 시각·품질 정보와 함께 하나의 세계 상태로 모으고 불일치를 드러내는 것이며, 설비 자체 제어와 센서 융합은 외부에 맡기는 경계가 될 것으로 보인다. | ref-031, ref-184, ref-045 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 6.6 State: 'published when relevant events occur or at least every 30 seconds'. 사건 예: 주문 수신, 적재 변화, 오류, 운전 모드·주행 상태·안전 상태·동작 상태 변화. (발행일 미확인, 확인일 기준)
- **f2**: 6.5 Connection: 연결이 예기치 않게 끊기면 브로커가 last will 을 connectionState 'CONNECTION_BROKEN' 으로 발행. 4.1: connection 은 QoS 1, 나머지 토픽은 QoS 0. (발행일 미확인, 확인일 기준)
- **f3**: 열람 도구 응답: 관제의 오래된 상태·연결 끊김 대응과 NTP 등 시각 동기화는 명세에 정의되지 않음. 전문을 글자 단위로 대조하지 않아 부재의 확정은 아님. (발행일 미확인, 확인일 기준)
- **f4**: state.schema: timestamp 'ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ)'; localized 'True: ... x, y, and theta can be trusted'; localizationScore 0.0 unknown~1.0 known; 'Each floor has its own map'. (발행일 미확인, 확인일 기준)
- **f5**: robot_state.json: unix_millis_time, location(map·x·y·yaw), status 'A simple token representing the status of the robot', issues 'operators need to address'. (발행일 미확인, 확인일 기준)
- **f6**: 문서: door adapter 는 'state supervisor ensuring that the doors are not acting on requests that might obstruct an ongoing mobile robot task'. DoorState.msg 필드: door_time, door_name, current_mode. (발행일 미확인, 확인일 기준)
- **f7**: LiftState.msg: lift_time, current_floor, destination_floor, door_state, motion_state, mode(fire·emergency 등은 읽기만), session_id. 문서: adapter 'keeping track of the internal and desired state of the lift'. (발행일 미확인, 확인일 기준)
- **f8**: 두 문서 열람 응답: 발행 빈도·staleness 언급 없음. 메시지 정의는 시각 필드만 둔다. 다른 구현 코드는 보지 않아 부재의 확정은 아님. (발행일 미확인, 확인일 기준)
- **f9**: Lifespan: 'the maximum amount of time between the publishing and the reception of a message without the message being considered stale or expired'. 이벤트: offered/requested deadline missed, liveliness lost/changed. (Jazzy 판 문서 원본)
- **f10**: 'Host Applications MUST mark all metrics that were included in the previous NBIRTH as STALE'; reorder timeout 만료 시 'Node Control/Rebirth' NCMD 전송. (발행일 미확인, 확인일 기준)
- **f11**: 검색 요약(OPC 10000-4 7.11): StatusCode 'can be used as an indicator of the usability of the value'; Uncertain·Bad 는 SubCode 로 이유 표시. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f12**: 검색 요약: AoI 는 'time elapsed since the latest received update was generated'; 시각 표시된 상태 갱신을 보내는 저지연 사이버물리 시스템 설계·최적화 서베이(IEEE JSAC 39(5), 2021). 원문 미열람.
- **f13**: f1(30초 주기), f9(Lifespan·Deadline), f10(STALE), f6·f8(문 상태에 시각만 있고 오래됨 규칙 없음), f12(AoI)를 분류 원문 SCM 질문에 대응시킨 추론. 허용 경과 시간 값을 정한 출처는 찾지 못함.
- **f14**: EPCIS.ttl: eventTime 'The date and time at which the EPCIS Capturing Applications asserts the event occurred'; recordTime 은 저장소 기록 시각으로 캡처 시 무시되고 조회 결과에 나타남.
- **f15**: EPCIS.ttl: errorDeclaration 'indicates that this event serves to assert that the assertions made by a prior event are in error'. CBV.ttl: did_not_occur 는 정정 이벤트 없음, incorrect_data 는 뒤 이벤트가 바로잡을 수 있음. 두 파일 같은 발행 주체.
- **f16**: f15 의 오류 선언·정정 이벤트 구조를 로봇 상태 이력에 옮긴 추론. 로봇 관제 표준에서 같은 정정 구조를 둔 예는 이번 열람 범위에서 확인하지 못함.
- **f17**: sosa.ttl: phenomenonTime 'The time that the Result of an Observation ... applies to the FeatureOfInterest'; resultTime 'the instant of time when the Observation ... was completed'. 작업반 저장소 편집본이라 /TR 권고안과 문구가 다를 수 있음.
- **f18**: f11·f14·f17 의 시각 구분을 대응시킨 추론. 세 표준이 서로를 참조한다는 근거는 확인하지 못했고 이름·정의가 조금씩 다름.
- **f19**: rmf-core 원본: 'a living database whose contents will change over time to reflect delays, cancellations, or route changes'; 충돌 감지 시 conflict notice 와 협상, 제3자 판정. (발행일 미확인, 확인일 기준)
- **f20**: 검색 요약: 'nearly 370,000 inventory records from 37 stores of one retailer and found 65% to be inaccurate'. Management Science 54(4) 627-641. 소매 매장 조건이며 물류센터 값이 아님. 원문 미열람.
- **f21**: f20(기록 부정확성)과 f4(상태에 적재물 식별 포함)를 대응시킨 추론. 로봇 관측으로 WMS 재고를 정정한 공개 사례는 찾지 못함.
- **f22**: 검색 요약: 'In mobile environments, WSTD performs better than SMURF, producing approximately 30% less overall errors'. Sensors 12(4) 4187. 실험 조건 원문 미열람.
- **f23**: 검색 요약: 'chains together mixtures of "persistence" and "emergence" filters to model the probability that features will disappear or reappear in a formal Bayesian framework'. 원문 미열람.
- **f24**: 검색 요약: '(1) any replica can be modified without coordinating ... (2) when any two replicas have received the same set of updates, they reach the same state deterministically'. 원문 미열람.
- **f25**: f24(조율 없는 수렴)와 f6·f7(어댑터가 요청을 감독, session_id 로 제어권 부여)을 대조한 추론. 로봇 세계 상태에 CRDT 를 적용한 사례는 이번 검색에서 확인하지 못함.
- **f26**: 검색 요약(NIST 해설): 'fit for purpose digital representation of an observable manufacturing element with synchronization between the element and its digital representation'. Part 4 는 동기화용 기술 식별. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f27**: 검색 요약: Digital Model 은 'does not use any form of automated data exchange', Digital Shadow 는 'automated one-way data flow'. IFAC-PapersOnLine 51(11), 2018. 원문 미열람.
- **f28**: f26·f27 의 분류를 분류 원문 7장 주석(현재 상태 표현 대 가정한 미래 실험)에 대응시킨 추론. 두 출처는 제조 대상이며 로봇 오케스트레이션에 이 구분을 적용한 문헌은 찾지 못함.
- **f29**: 검색 요약: 이기종 로봇·PLC 대응을 위해 연결 솔루션과 OPC UA 활용, 데이터 수집·전달과 3D 디지털 트윈 시뮬레이션 담당. 게재지 이름은 검색 요약마다 다름(열린 질문). 제조 대상, 원문 미열람.
- **f30**: f4 의 localized·localizationScore·deviationRange 필드를 분류 원문 9장 경계(로봇 자체 지능·제어는 연계 영역)와 대응시킨 추론.
- **f31**: f1·f6·f14 와 분류 원문 9장('시설·설비 제어'는 작업 요청·예약·인계·상태 확인만 ROP)을 대응시킨 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-09-25 | https://www.w3.org/TR/vocab-ssn/ | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-182 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 | 예 |
| ref-183 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 아니오 |
| ref-184 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-185 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 아니오 |
| ref-186 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg | 아니오 |
| ref-187 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-188 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 미확인 | 표준 | high | 2026-09-25 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc | 아니오 |
| ref-189 | Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. | Age of Information: An Introduction and Survey | 2021-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2007.08564 | 예 |
| ref-190 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 | 예 |
| ref-191 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-192 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 2008 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 | 예 |
| ref-193 | Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. | Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments | 2025-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2507.18808 | 예 |
| ref-194 | Massawe, L. V. 외(Sensors) | Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach | 2012 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/s120404187 | 예 |
| ref-195 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 2023 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 | 예 |
| ref-196 | Preguiça, N., Baquero, C., & Shapiro, M. | Conflict-free Replicated Data Types (CRDTs) | 2018-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1805.06358 | 예 |

### 출처 요약

- **ref-004**: 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. 이번 실행은 교통 일정 데이터베이스(지연·취소·경로 변경 반영, 충돌 감지와 협상)를 확인했다.
- **ref-030**: 관측·센서·액추에이션을 기술하는 W3C/OGC 온톨로지. 이번 실행은 작업반 저장소의 sosa.ttl(편집본)로 phenomenonTime·resultTime 정의를 확인했다.
- **ref-031**: VDA 5050 공식 명세의 GitHub 저장소 본문(main 은 3.0.0 판). 이번 실행은 상태 발행 조건(사건 발생 시와 최소 30초마다), connection 토픽과 last will, 토픽별 MQTT QoS 를 확인했다.
- **ref-044**: CBV 2.0 어휘의 온톨로지 원본. 이번 실행은 오류 사유 어휘 did_not_occur·incorrect_data 를 확인했다.
- **ref-045**: EPCIS 2.0 온톨로지 원본. 이번 실행은 eventTime·recordTime·eventTimeZoneOffset 과 오류 선언(declarationTime·reason·correctiveEventIDs) 정의를 확인했다.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마(main). 이번 실행은 시각 형식, 마지막 노드, 위치추정 여부·품질·편차 범위, 지도 id, 적재물, 운전·안전 상태 필드를 확인했다.
- **ref-148**: Open-RMF API 로봇 상태 JSON 스키마. 시각(unix_millis_time), 위치, 상태 7종, 문제 목록, 배터리 충전 상태를 정의한다.
- **ref-182**: 원문 미열람. OPC UA 데이터 값 구조(값, SourceTimestamp, ServerTimestamp, StatusCode)와 시각·품질의 의미를 정의한 공식 온라인 참조.
- **ref-183**: ROS 2 QoS 정책(History·Reliability·Durability·Deadline·Lifespan·Liveliness·Lease Duration)과 QoS 이벤트를 설명하는 공식 문서(ros2_documentation 저장소 jazzy 브랜치 원본).
- **ref-184**: Open-RMF 문 연동 문서(mdBook 원본). 문 노드의 상태 발행, 문 어댑터의 요청 감독과 직접 요청 되돌림을 설명한다.
- **ref-185**: Open-RMF 승강기 연동 문서(mdBook 원본). 승강기 노드의 상태 발행과 승강기 어댑터의 내부·목표 상태 추적, 요청 중계를 설명한다.
- **ref-186**: Open-RMF 문 상태 메시지 정의. 시각(door_time), 문 이름, 현재 모드 세 필드를 둔다.
- **ref-187**: Open-RMF 승강기 상태 메시지 정의. 시각, 이용 가능·현재·목적 층, 문·운행 상태, 운영 모드, 세션 id 를 둔다.
- **ref-188**: MQTT 기반 산업 데이터 사양 Sparkplug 의 운영 동작 장. 연결 끊김·NDEATH 시 STALE 표시, 순번으로 순서 역전 감지, 재정렬 대기와 재탄생 요청, 호스트 STATE 메시지를 규정한다.
- **ref-189**: 원문 미열람. 시각 표시된 상태 갱신의 신선도 지표인 정보 나이(AoI)의 정의와 설계·최적화 연구를 정리한 서베이(IEEE JSAC 39(5), arXiv 2020 게재).
- **ref-190**: 원문 미열람. ISO 23247 제조 디지털 트윈 프레임워크의 정의(동기화된 디지털 표현), 관측 가능한 제조 요소, 계층 구조를 해설한 NIST 발표 자료.
- **ref-191**: 원문 미열람. 제조 디지털 트윈 문헌을 데이터 통합 수준에 따라 디지털 모델·디지털 섀도·디지털 트윈으로 분류한 IFAC-PapersOnLine 논문.
- **ref-192**: 원문 미열람. 한 소매업체 37개 매장의 재고 기록 약 37만 건을 분석해 기록 부정확성의 정도와 요인을 밝힌 Management Science 54(4) 논문.
- **ref-193**: 원문 미열람. 반정적 환경 요소의 사라짐·재출현을 지속·출현 필터 혼합으로 모델링해 미래 상태를 예측하는 방법(IROS 2025).
- **ref-194**: 원문 미열람. RFID 판독 스트림의 누락 판독을 적응형 슬라이딩 윈도(WSTD)로 줄이고 SMURF 와 비교한 논문(Sensors 12(4)). 저자 목록 일부 미확인.
- **ref-195**: 원문 미열람. OPC UA 와 연결 솔루션으로 이기종 로봇·PLC 데이터를 모아 실시간 3D 디지털 트윈을 구축한 국내 논문. 게재지 이름은 검색 요약마다 달라 미확인.
- **ref-196**: 원문 미열람. 조율 없이 수정하고 같은 갱신을 받으면 같은 상태로 수렴하는 복제 데이터 타입(CRDT)의 정의와 설계를 정리한 해설 프리프린트.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f13(30초 전 문 상태 판단은 표준이 정하지 않아 ROP 규칙 필요), f20·f21(기록–실물 불일치) / 섹션 4: f12(정보 나이), f14·f17·f11·f18(발생 시각·기록 시각·품질), f9(Deadline·Lifespan·Liveliness), f15(오류 선언·정정 이벤트), f24(CRDT), f27(디지털 섀도) / 섹션 5: 적치·이동 중 문 통과 제약 f6·f13, 승강기 층간 이동 제약 f7, 입고 판독 누락 f22(완료·인계), 피킹 적재물 식별 f4·f21(작업 대상), 출하 인계 정정 f16(완료·인계), 보충 재고 기록 오류 f20(예외·성과) — 흐름 단계와 여섯 항목 명시 / 섹션 6: f10(STALE·순번·재탄생), f9, f19(교통 일정 DB), f16, f18, f22(판독 정제), f23(지속성 모델), f25(단일 감독자 대 수렴) / 섹션 7: f1·f2·f3·f4(VDA 5050 3.0.0), f5·f6·f7·f8·f19(Open-RMF 로봇·문·승강기·교통 일정), f9(ROS 2 QoS), f10(Sparkplug), f11(OPC UA DataValue), f14·f15(EPCIS·CBV), f17(SOSA), f26(ISO 23247) / 섹션 8: f12, f20, f22, f23, f24, f27, 국내 f29 / 섹션 9: f30(연계 대상: 위치추정), f31(직접 범위) / 섹션 10: 22. 시뮬레이션·예측용 디지털 트윈(f28, 현재 상태 표현과 가정한 미래 실험 구분), 7. 화물·재고·자산 식별과 추적(f14·f15·f21), 10. 설비·건물 시스템 연동(f6·f7), 9. 로봇·제조사 관제 연동(f1·f2·f4), 11. 분산 시스템·통신·컴퓨팅 구조(f9·f10·f24), 15. 다중 로봇 경로·교통 관리 — MAPF(f19), 6. 지도·공간·위치 모델(f4 mapId·위치 품질), 19. 모니터링·이상 탐지·원인 분석(f10 STALE·f2 연결 끊김) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 10. 설비·건물 시스템 연동 페이지에 f6·f7·f8 반영 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 정보 나이 | Age of Information (AoI) | 수신 측이 가진 최신 상태 갱신이 생성된 뒤 흐른 시간으로, 정보가 얼마나 최신인지를 재는 지표이다. |
| 디지털 섀도 | Digital Shadow | 물리 대상의 상태가 디지털 표현으로 한 방향 자동 흐름으로만 반영되는 단계의 디지털 표현으로, 디지털 모델·디지털 트윈과 구분된다. |
| 무충돌 복제 데이터 타입 | Conflict-free Replicated Data Type (CRDT) | 여러 복제본을 조율 없이 수정해도 같은 갱신을 받으면 정해진 규칙으로 같은 상태에 수렴하도록 설계된 데이터 타입이다. |

## 열린 질문

새로 생긴 질문:

- 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? | 관련 영역: 8. 실시간 세계 상태·데이터 일관성, 10. 설비·건물 시스템 연동 | 근거: f13 | 종류: 일반
- 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? | 관련 영역: 8. 실시간 세계 상태·데이터 일관성, 9. 로봇·제조사 관제 연동, 11. 분산 시스템·통신·컴퓨팅 구조 | 근거: f3 | 종류: 일반
- 로봇이 보고한 적재물 식별·판독 결과와 WMS 재고 기록이 어긋날 때 어느 쪽을 기준으로 삼고 정정 기록을 누가 발행하는가(국내 물류센터 사례 포함)? | 관련 영역: 8. 실시간 세계 상태·데이터 일관성, 7. 화물·재고·자산 식별과 추적 | 근거: f21 | 종류: 일반
- 출처 충돌: 김지형(2023) 'OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현'의 게재 학술지가 검색 요약에 따라 지능정보논문지와 한국인터넷방송통신학회논문지로 다르게 나온다. 어느 쪽이 맞는가? | 관련 영역: 8. 실시간 세계 상태·데이터 일관성 | 근거: ref-195 | 종류: 출처 충돌

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·프레임워크마다 발행 주체 한 곳의 자료만 있음(f6·f7 은 같은 Open-RMF 저장소 계열, f15 의 EPCIS·CBV 는 같은 GS1 저장소)
    - f3·f8 은 열람 도구 응답 기준의 부재 관찰이며 문서 전체를 글자 단위로 대조하지 않음
    - f11·f12·f20·f22·f23·f24·f26·f27·f29 원문 미열람(검색 요약 범위)
    - f20 65% 수치는 소매 매장 조건이며 물류센터 재고 기록 정확도 자료는 찾지 못함
    - f26 ISO 23247 표준 원문 미열람(NIST 해설 자료 경유)
    - ref-194 저자 목록 일부, ref-195 게재지 이름 미확인(출처 충돌로 열린 질문)
    - ref-182·ref-183·ref-184·ref-185·ref-186·ref-187·ref-188·ref-190 발행일 미확인
    - ROS 2 설계 문서 qos.md(2019)에는 Deadline·Lifespan·Liveliness 가 없어 ros2_documentation 원본으로 확인함
    - Toris·Chernova(ICRA 2017) 시간 지속성 모델은 서지만 확인되고 URL 을 확인하지 못해 넣지 않음
    - 국내 물류센터에서 설비 상태 신선도나 로봇–WMS 재고 불일치를 다룬 자료는 찾지 못함
- 범위 경계 위반 의심:
    - f30: 위치추정·품질 계산은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f6·f7: 문·승강기 제어 자체는 '시설·설비 제어' 연계 영역이며, 상태 확인·요청 감독 관점으로만 제안함
    - f23: 대상 지속성 모델은 로봇 지도 연구이며 ROP 세계 상태에 적용하는 방법 참고로만 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. GitHub 공식 저장소 원문 13건을 raw.githubusercontent.com 으로 열었다(재사용 ref-004 rmf-core, ref-030 SOSA 편집본, ref-031 VDA 5050 명세, ref-044 CBV.ttl, ref-045 EPCIS.ttl, ref-051 state.schema, ref-148 robot_state.json / 신규 ref-183 ROS 2 QoS 문서, ref-184·ref-185 Open-RMF 문·승강기 문서, ref-186·ref-187 DoorState·LiftState 메시지, ref-188 Sparkplug 5장). OPC UA 온라인 참조·NIST 해설·논문 7건은 검색 요약만 봐서 원문 미열람(신뢰도 상한 medium). 교차 확인 0건. 검색 18회/30, 신규 출처 15건/15(ref-182~ref-196)로 출처 상한에 도달해 KIIT 2023 MQTT 이기종 로봇 디지털 트윈 논문, Toris·Chernova(2017), 자동물류시스템 디지털트윈 국내 논문은 넣지 못했다. 재사용 7건. 한국 자료: KCI 논문 1건(ref-195, 제조 대상)뿐이며 물류센터 세계 상태·재고 불일치 국내 자료는 찾지 못해 열린 질문으로 올렸다. 분류 원문 SCM 질문(30초 전 문 상태)은 f13 으로 답했으나 허용 경과 시간 값을 정한 출처가 없어 추정이다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f26·f27·f28 로 구분 근거만 두고 섞지 않았다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 새 id 는 이 실행에 예약된 ref-182~ref-211 구간을 썼으나 이전 브리프 2026-09-25-13 이 같은 번호대(ref-182~ref-192)를 다른 출처에 제안한 이력이 있어 퍼블리셔의 충돌 확인이 필요하다.
