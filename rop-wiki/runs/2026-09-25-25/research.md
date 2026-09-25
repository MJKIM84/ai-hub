# 리서치 브리프 2026-09-25-25

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-25 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 10. 설비·건물 시스템 연동 |
| 대분류 | C. 연결·실행 기반 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 문·승강기·작업대(워크셀) 어댑터, 승강기 모드·세션, 해제 구역 개념 없음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 설비 인터페이스, VDA 5050 의 주변 설비 범위, 국내 KS·단체표준 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-010 연결 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [분류원문]
2. 로봇 관제가 문·승강기·작업대(컨베이어 등)와 요청·상태·완료를 주고받는 공개 인터페이스(Open-RMF 설비 메시지 등)는 어떤 구조인가? (섹션 4·6·7 겨냥)
3. VDA 5050 같은 로봇–관제 표준은 주변 설비 연동을 어디까지 다루며, 설비 연동 책임은 누구에게 두는가? (섹션 7·9 겨냥)
4. 국내에서 로봇의 승강기 탑승·연동을 다루는 국가표준·단체표준·제조사 API 는 무엇이 있는가? (섹션 7·8, 한국 자료 우선)
5. 승강기 같은 공용 설비가 다층 운반의 대기 시간·처리량에 주는 영향을 다룬 연구는 무엇인가? (섹션 3·8, oq-010 관련)
6. 설비 연동에서 ROP 가 맡는 요청·예약·상태 확인과 외부 설비 제어·안전 제어의 경계는 어디인가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 는 문 제어기와 통신하는 문 노드(door node) 앞에 문 어댑터를 두어, 플릿 어댑터·RMF 핵심 시스템의 문 요청을 받아 로봇 운영을 방해하지 않는다고 판단될 때만 문 노드에 전달하는 상태 감독자 역할을 맡긴다. | ref-408 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | Open-RMF 의 문 상태 메시지(DoorMode)는 자동문 제어기의 상태를 닫힘·움직이는 중·열림·오프라인·알 수 없음의 다섯 값으로 보고한다. | ref-412 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f3 | [사실] | Open-RMF 의 승강기 어댑터는 플릿 어댑터·RMF 핵심 시스템의 승강기 요청을 받아 적절하다고 판단될 때만 승강기 노드에 전달하고, 어댑터를 거치지 않고 승강기 노드에 직접 보낸 요청은 무효로 만든다. | ref-409 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f4 | [사실] | Open-RMF 승강기 요청 메시지(LiftRequest)는 승강기 이름, 요청자별 세션 id, 요청 유형(세션 종료·AGV 모드·사람 모드), 목적 층, 문 상태(닫힘·열림)를 담으며, AGV 모드에서는 정지 시 문이 항상 열려 있고 사람 모드에서는 문이 시간 초과로 자동으로 닫힐 수 있다. | ref-411 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | Open-RMF 승강기 상태 메시지(LiftState)는 이용 가능한 층·현재 층·목적 층, 문 상태(닫힘·움직임·열림), 운행 상태(정지·상승·하강·알 수 없음), 모드(설정 가능한 사람·AGV, 읽기만 가능한 화재·오프라인·비상)와 승강기를 점유한 세션 id 를 보고한다. | ref-410 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | Open-RMF 는 작업대(workcell)를 물건을 내주는 디스펜서와 받아들이는 인제스터 두 유형으로 두고 각각 요청·결과·상태 메시지를 쓰며, 배송 작업에서 로봇은 픽업 위치에서 디스펜서 서비스를 요청해 확인을 기다린 뒤 하역 위치에서 인제스터 서비스를 요청해 확인을 기다린다. | ref-023, ref-047, ref-049 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f7 | [사실] | VDA 5050 3.0.0 은 관제와 이동로봇 사이 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f8 | [사실] | VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 가운데 하나로 들어, 설비 연동 책임을 로봇이 아니라 관제 쪽에 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f9 | [사실] | VDA 5050 3.0.0 의 해제 구역(RELEASE zone)은 관제의 진입 허가를 받아야 들어갈 수 있는 구역으로, 로봇이 상태 메시지의 zoneRequests 로 진입을 요청하면 관제가 responses 토픽으로 허가·대기·철회·거절을 답하고, 허가가 철회·만료될 때의 행동은 releaseLossBehavior(정지·계속·대피)로 정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f10 | [사실] | VDA 5050 3.0.0 의 동작 구역(ACTION zone)은 로봇이 구역에 들어갈 때·지나는 동안·나올 때 미리 정한 action(entryActions·duringActions·exitActions)을 수행하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f11 | [사실] | 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했으며, 행정안전부(승강기 안전기준 소관)와 협력해 추진했다. | ref-413, ref-414 | 아니오 | medium | 2021-11 | 제약 | 원문 미열람 |
| f12 | [사실] | 국가기술표준원 보도자료는 로봇이 건물 안을 이동하고 엘리베이터에 타려면 속도 제어, 위험 상황에서의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지 기준이 필요하다고 설명한다. | ref-414 | 아니오 | medium | 2021-11 | 제약 | 원문 미열람 |
| f13 | [사실] | 대한승강기협회는 엘리베이터에 로봇이 탑승할 수 있도록 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준을 제정했다고 보도됐다. | ref-415 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | 대한승강기협회는 산업통상자원부 과제 '디지털 기반 차세대 개방형 승강기 운영시스템 개발'을 수행하며 승강기·로봇 분야 23개 단체 24명의 협의체를 꾸려 API 로 실시간 정보를 주고받는 승강기–로봇 연동 프로토콜(안)과 시나리오(안)를 협의했다고 보도됐다. | ref-416 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | KONE 은 청소·배송·보안용 자율 로봇을 자사 승강기와 연동하는 Service Robot API 를 엘리베이터 호출 API·설비 상태 API 와 함께 제공한다고 밝힌다. | ref-417 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f16 | [추정] | 현대엘리베이터는 2022년 3월 로봇이 엘리베이터를 호출해 탑승하는 '로봇 연동' 등을 제공하는 클라우드 기반 오픈 API 를 공개하고 추가 장비 없이 연동할 수 있다고 밝혔다. | ref-418 | 아니오 | low | 2022-03 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f17 | [추정] | 현대엘리베이터는 오픈 API 참여 주체가 1년여 만에 60여 곳으로 늘었고 병원·호텔·은행 등에서 배송로봇 40여 대가 자사 엘리베이터를 이용해 운행 중이라고 밝혔다. | ref-419 | 아니오 | low | 2023-02 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f18 | [사실] | Electronics(2025) 게재 연구는 실내 배송 로봇의 다층 경로계획에서 승강기 선택을 최적화하는 그래프 기반 방법을 제안해 층간 이동과 승강기 대기 시간을 경로계획에 함께 넣었다. | ref-420 | 아니오 | medium | 2025 | 예외·성과 | 원문 미열람 |
| f19 | [사실] | Digital Health(2026) 게재 연구는 이용이 많은 병원 환경에서 승강기 이용을 고려해 자율 약품 배송 로봇의 실현 가능성을 평가했다. | ref-060 | 아니오 | medium | 2026 | 예외·성과 | 원문 미열람 |
| f20 | [사실] | 다층 호텔 환경의 로봇 배송 경로계획 연구는 승강기를 포함한 층간 이동을 다중 로봇 경로계획 문제에 넣어 다룬다. | ref-103 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f21 | [사실] | 국내 연구(로봇학회 논문지 2026)는 탐사와 엘리베이터 연계를 이용해 다층 실내 지도를 자율로 구축하는 시스템을 보고했다. | ref-163 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f22 | [사실] | 국토교통부는 로봇이 승강기 등을 이용해 건물 안을 이동할 수 있게 하는 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'에 착수한다고 발표했다. | ref-421 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f23 | [추정] | 분류 원문의 질문(컨베이어 준비와 로봇 도착을 어떻게 맞출까)에 대해, Open-RMF 의 디스펜서·인제스터처럼 로봇 도착 후 설비에 요청을 보내고 결과를 받아야 다음 단계로 넘어가는 요청–결과 방식과, VDA 5050 해제 구역처럼 설비 앞 구역 진입을 관제가 허가하는 방식을 조합하면 ROP 가 설비 준비 신호와 로봇 도착을 한 작업 흐름 안에서 맞출 수 있을 것으로 보인다. | ref-023, ref-031 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f24 | [추정] | 입고·적치에서 로봇이 층간 운반에 승강기를 쓰면 한 세션이 승강기를 점유하는 동안 다른 로봇이 기다려야 하므로(Open-RMF 세션 방식), 승강기 대기가 처리량과 운반 시간에 영향을 줄 것으로 보인다. | ref-411, ref-410, ref-060, ref-103 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f25 | [추정] | 승강기가 화재·비상·오프라인 모드로 바뀌거나 문 상태가 오프라인·알 수 없음으로 보고되면 ROP 는 해당 설비를 쓰는 작업을 멈추거나 다른 경로·사람 확인으로 넘기는 예외로 다뤄야 할 것으로 보인다. | ref-410, ref-412 | 아니오 | low | 2026-09-25 | 적치 / 예외·성과 | — |
| f26 | [추정] | 연계 대상: 승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어는 설비 제조사·설비 제어기 쪽에 남고, ROP 는 어댑터를 통해 작업 요청·점유 예약·상태 확인·완료 확인을 맡는 것으로 보인다. | ref-408, ref-409, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |

### 근거 발췌

- **f1**: 원문(github_raw): 'The door adapter stands in between the rest of the RMF core systems, fleet adapters, and the door node, and acts like a state supervisor'. 문 요청은 adapter_door_requests 토픽으로 들어온다. (발행일 미확인, 확인일 기준)
- **f2**: DoorMode.msg: MODE_CLOSED=0, MODE_MOVING=1, MODE_OPEN=2, MODE_OFFLINE=3, MODE_UNKNOWN=4. (발행일 미확인, 확인일 기준)
- **f3**: 원문(github_raw): 어댑터는 'receiving lift requests from the fleet adapters and the RMF core systems and only relaying the instructions to the lift node if it is deemed appropriate'. 승강기 노드는 OPC 등으로 승강기 제어기와 통신. (발행일 미확인, 확인일 기준)
- **f4**: LiftRequest.msg: session_id, REQUEST_END_SESSION=0, REQUEST_AGV_MODE=1, REQUEST_HUMAN_MODE=2, destination_floor, DOOR_CLOSED=0, DOOR_OPEN=2. 주석: AGV 모드는 정지 시 문 상시 개방. (발행일 미확인, 확인일 기준)
- **f5**: LiftState.msg: available_floors, current_floor, destination_floor, door_state, motion_state, available_modes(HUMAN=1, AGV=2), current_mode 에 FIRE=3, OFFLINE=4, EMERGENCY=5, session_id 는 REQUEST_END_SESSION 까지 제어 보유. (발행일 미확인, 확인일 기준)
- **f6**: 워크셀 문서(github_raw): Request/Result/State 세 메시지, perform_deliveries 가 true 여야 배송 작업 수락. DispenserRequest·IngestorResult 메시지 정의(재사용 출처). 모두 Open Robotics 발행이라 독립 교차 아님.
- **f7**: 명세 원문(github_raw) 범위 절: 'interfaces to peripheral equipment, infrastructure components, or external IT systems' 제외. (발행일 미확인, 확인일 기준)
- **f8**: 명세 원문의 관제 기능 목록: 'Communication with peripheral systems such as doors, gates, elevators, etc.' (발행일 미확인, 확인일 기준)
- **f9**: 명세 원문: RELEASE 는 'only allowed entering this zone once they have been granted access through fleet control'; responseType GRANTED·QUEUED·REVOKED·REJECTED; releaseLossBehavior STOP·CONTINUE·EVACUATE. (발행일 미확인, 확인일 기준)
- **f10**: 명세 원문: ACTION 구역에서 로봇은 'shall perform predefined actions when entering, traversing, or exiting the zone'. 문·승강기 연동에 쓰라는 규정은 확인하지 못함. (발행일 미확인, 확인일 기준)
- **f11**: 검색 요약: KSSN 표준 상세의 표제 'KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법', 정책브리핑 보도자료(2021-11) 제정 발표. 두 출처 모두 국가기술표준원 계열이라 독립 교차로 보지 않음. 원문 미열람.
- **f12**: 검색 요약: '속도제어, 위험상황에서의 보호정지, 높낮이차·틈새극복, 추락·넘어짐 방지 등에 대한 기준이 필요'. KS B 7317 본문의 조항 구성은 미확인. 원문 미열람.
- **f13**: 기사 검색 요약: 배송 로봇 확산에도 통일된 기준이 없어 단체표준 제정. 표준 번호·제정일·세부 내용은 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f14**: 기사 검색 요약: 한국로봇산업진흥원·ETRI·한국승강기안전공단 등 참여, '승강기-로봇 연동 관련 프로토콜(안) 및 시나리오(안)' 협의. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f15**: 벤더 주장: 검색 요약 'Service Robot API lets you integrate autonomous robots … with KONE elevators'. 메시지 구조·인증 방식은 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f16**: 벤더 주장: 기사 검색 요약 — 클라우드 기반이라 연동용 추가 장비 불필요, 로봇 연동·원격 콜 서비스. 원문 미열람.
- **f17**: 벤더 주장: 기사 검색 요약 — 참여 주체 60여 개(로봇 기업·통신사·연구기관 등), 배송로봇 40여 대 운행. 독립 확인 없음. 원문 미열람.
- **f18**: 검색 요약: 'elevator function for effective vertical navigation optimizes floor transitions and reduces waiting times'. 실험 조건·수치는 미확인. 원문 미열람.
- **f19**: 논문 표제 'Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments'(재사용 출처). 결과 수치는 이번에 확인하지 않음. 원문 미열람.
- **f20**: 검색 요약: 승강기 노드를 암묵적 경유점으로 모델링하고 적응형 대근방 탐색(ALNS)으로 배송 경로를 최적화. 재사용 출처, 원문 미열람.
- **f21**: 논문 표제 '탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템'(재사용 출처). 승강기 연동 방식 세부는 미확인. 원문 미열람.
- **f22**: 검색 요약: 보도자료 제목 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발부터 착수', 이후 UAM·자율주행차 친화형 건축 기술개발 순차 추진. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f23**: f6(요청·결과 대기), f9(진입 허가)를 출하 흐름의 완료·인계에 대응시킨 추론. 컨베이어 준비 시각과 로봇 도착을 함께 최적화한 공개 연구는 이번 검색에서 찾지 못함.
- **f24**: f4·f5(세션 점유)와 f19·f20(승강기 이용을 다룬 병원·호텔 연구)에서 도출. 물류센터 화물용 승강기의 정량 자료는 없음(oq-010).
- **f25**: f2·f5 의 상태 값을 예외 처리에 대응시킨 추론. 복구 규칙 자체는 20. 예외 복구·재계획·업무 연속성의 과제.
- **f26**: f1·f3(어댑터가 요청을 걸러 설비 노드에 전달), f7·f8(VDA 5050 은 설비 인터페이스 제외, 관제가 담당)과 분류 원문 9장 '시설·설비 제어' 경계를 대응시킨 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 예 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.1177/20552076261437181 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |
| ref-408 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-409 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 아니오 |
| ref-410 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-411 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-412 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-413 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-414 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 예 |
| ref-415 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 미확인 | 기사 | low | 2026-09-25 | https://www.ctman.kr/35296 | 예 |
| ref-416 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | 기사 | low | 2026-09-25 | https://www.electimes.com/news/articleView.html?idxno=320147 | 예 |
| ref-417 | KONE | KONE Service Robot API | 미확인 | 벤더 문서 | low | 2026-09-25 | https://dev.kone.com/api-portal/service-robot-api/ | 예 |
| ref-418 | 한국경제 | 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 | 2022-03 | 기사 | low | 2026-09-25 | https://www.hankyung.com/economy/article/202203314153Y | 예 |
| ref-419 | 파이낸셜뉴스 | 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" | 2023-02 | 기사 | low | 2026-09-25 | https://www.fnnews.com/news/202302140913318867 | 예 |
| ref-420 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics14050982 | 예 |
| ref-421 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 예 |

### 출처 요약

- **ref-023**: Open-RMF 작업대(디스펜서·인제스터)의 요청·결과·상태 메시지와 배송 작업 연동을 설명하는 공식 문서(mdBook 원본).
- **ref-031**: VDA 5050 공식 명세 본문(main 은 3.0.0 판). 이번 실행은 범위 제외(주변 설비), 관제 기능 목록, 해제·동작 구역을 확인했다.
- **ref-047**: 원문 미열람. Open-RMF 디스펜서 요청 메시지 정의(재사용, 이번 실행 재열람 안 함).
- **ref-049**: 원문 미열람. Open-RMF 인제스터 결과 메시지 정의(재사용, 이번 실행 재열람 안 함).
- **ref-060**: 원문 미열람. 이용이 많은 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇의 실현 가능성을 다룬 논문(재사용).
- **ref-103**: 원문 미열람. 승강기를 포함한 다층 호텔 환경의 다중 로봇 배송 경로계획 논문(재사용).
- **ref-163**: 원문 미열람. 탐사와 엘리베이터 연계로 다층 실내 지도를 자율 구축하는 국내 논문(재사용).
- **ref-408**: Open-RMF 의 문 연동 구조(문 노드, DoorState·DoorRequest, 상태 감독자 역할의 문 어댑터)를 설명하는 공식 문서(mdBook 원본).
- **ref-409**: Open-RMF 의 승강기 연동 구조(승강기 노드, LiftState·LiftRequest, 요청을 걸러 전달하는 승강기 어댑터)를 설명하는 공식 문서(mdBook 원본).
- **ref-410**: 승강기 층·문·운행 상태, 모드(사람·AGV·화재·오프라인·비상), 점유 세션을 보고하는 Open-RMF 승강기 상태 메시지 정의.
- **ref-411**: 세션 id, 요청 유형(세션 종료·AGV 모드·사람 모드), 목적 층, 문 상태를 담는 Open-RMF 승강기 요청 메시지 정의.
- **ref-412**: 자동문 제어기 상태를 닫힘·움직임·열림·오프라인·알 수 없음으로 나타내는 Open-RMF 문 모드 메시지 정의.
- **ref-413**: 원문 미열람. 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한 국가표준의 KSSN 상세 페이지.
- **ref-414**: 원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항 등 KS 제정과 필요한 안전 기준을 알린 정부 보도자료.
- **ref-415**: 원문 미열람. 대한승강기협회의 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준 제정을 전한 기사.
- **ref-416**: 원문 미열람. 대한승강기협회 주도 승강기·로봇 협의체의 연동 프로토콜(안)·시나리오(안) 협의를 전한 기사.
- **ref-417**: 원문 미열람. 자율 로봇을 KONE 승강기와 연동하는 API 를 소개하는 제조사 개발자 포털 페이지.
- **ref-418**: 원문 미열람. 현대엘리베이터의 클라우드 기반 오픈 API(로봇 연동·원격 콜) 공개를 전한 기사.
- **ref-419**: 원문 미열람. 현대엘리베이터 오픈 API 참여 주체 확대와 배송로봇 운행 현황을 전한 기사.
- **ref-420**: 원문 미열람. 실내 배송 로봇의 다층 경로계획에 승강기 선택 최적화를 넣은 그래프 기반 방법 논문.
- **ref-421**: 원문 미열람. 로봇 친화형 건축물 설계·시공·운영 핵심기술 개발 착수를 알린 국토교통부 보도자료.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f7·f8(로봇–관제 표준이 설비 연동을 관제에 맡김), f24(승강기 대기가 처리량에 영향), f22 / 섹션 4: f1·f3(문·승강기 어댑터), f4·f5(승강기 모드·세션), f6(디스펜서·인제스터), f9·f10(해제·동작 구역) / 섹션 5: 출하 완료·인계 f6·f23, 적치 예외·성과 f24·f25 / 섹션 6: f1~f6(어댑터 경유 요청·상태 감독), f9·f10(구역 기반 진입 허가), f23 / 섹션 7: Open-RMF 설비 메시지 f1~f6, VDA 5050 범위 f7~f10, 국내 KS B 7317 f11·f12, 대한승강기협회 단체표준·프로토콜 f13·f14, 제조사 API f15~f17(모두 [추정] 벤더 주장) / 섹션 8: f18~f22 / 섹션 9: f26(연계 대상: 설비 제어·안전은 외부), f7·f8 / 섹션 10: 9. 로봇·제조사 관제 연동(f8), 15. 다중 로봇 경로·교통 관리 — MAPF(f18·f20), 16. 공용 자원·충전·에너지 최적화(f24 승강기 점유), 3. 처리능력·거점·설비 계획(f24, oq-010), 6. 지도·공간·위치 모델(f21), 17. 로봇 간 협업·물리적 인계(f6), 20. 예외 복구·재계획·업무 연속성(f25), 25. 안전·위험 관리(f11·f12), 12. 명령·작업 실행의 신뢰성(f4 세션) / 섹션 11: 기존 oq-010 연결, open_questions_new 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 승강기 어댑터 | Lift Adapter | Open-RMF 에서 플릿 어댑터·핵심 시스템의 승강기 요청을 받아 적절할 때만 승강기 노드에 전달하는 감독 구성요소이다. |
| 디스펜서·인제스터 | Dispenser / Ingestor | Open-RMF 에서 로봇에 물건을 내주는 작업대(디스펜서)와 로봇에서 물건을 받아들이는 작업대(인제스터)로, 각각 요청·결과·상태 메시지로 배송 작업과 연동된다. |
| 해제 구역 | Release Zone | VDA 5050 3.0.0 에서 관제의 진입 허가를 받아야 이동로봇이 들어갈 수 있는 구역이다. |

## 열린 질문

새로 생긴 질문:

- 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? | 관련 영역: 10. 설비·건물 시스템 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f13 | 종류: 일반
- 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? | 관련 영역: 10. 설비·건물 시스템 연동, 17. 로봇 간 협업·물리적 인계 | 근거: f7 | 종류: 일반
- 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? | 관련 영역: 10. 설비·건물 시스템 연동, 26. 사이버보안·접근권한·개인정보 | 근거: f1 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 11회 · 신규 출처 14건
- 미확인 항목:
    - f11 KS B 7317 두 출처가 국가기술표준원 계열이라 독립 교차 아님, 표준 본문 조항 미확인
    - f13 단체표준 번호·제정일·내용 미확인
    - f15~f17 제조사 API·운행 대수는 벤더 주장이며 독립 확인 없음
    - f18·f19·f20 결과 수치·실험 조건 미확인
    - f22 국토교통부 보도자료 발행일 미확인
    - 컨베이어–로봇 인계 핸드셰이크의 공식 표준 출처를 찾지 못함(블로그·제품 페이지만 확인되어 넣지 않음)
    - VDMA 40001(OPC UA for Machinery)의 물류 설비 적용 범위는 검색 요약만으로 확정하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f26: 승강기·자동문·컨베이어·PLC 제어와 설비 안전 제어는 분류 원문 9장 '시설·설비 제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f11·f12: KS B 7317 은 로봇 자체의 탑승 안전 요구사항이므로 ROP 직접 범위가 아니라 25. 안전·위험 관리 연결과 제약 조건으로만 제안
- 한계: 재실행 1회차. 반려 사유 1(f17 벤더 문서 근거 [사실]에 vendor_claim 누락): 직전 반환값이 이 프롬프트에 포함되지 않아 같은 범위로 브리프를 다시 구성했고, 벤더·제조사 발표에 기댄 기능·실적 주장 f15·f16·f17 을 모두 vendor_claim: true, 태그 [추정], evidence_excerpt 첫머리 '벤더 주장: '으로 냈다 (관련 finding: f15, f16, f17). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처는 ref-023·ref-031(재사용)과 ref-408~ref-412(신규) 7건이고, 나머지 14건(신규 9, 재사용 5)은 원문 미열람이라 신뢰도 상한 medium(기사·벤더는 low). 검색 11회/30, 신규 출처 14건/15(ref-408~ref-421, 예약 구간 안). 교차 확인 0건: 대부분 단일 출처이거나 같은 발행 주체의 문서다. 한국 자료: KS B 7317, 국가기술표준원·국토교통부 보도자료, 대한승강기협회 단체표준·협의체 기사, 현대엘리베이터 오픈 API 기사, 국내 논문(ref-163). 분류원문 질문(컨베이어 준비와 로봇 도착 맞추기)은 f23 으로 추정 수준 답만 냈고 정량 연구는 찾지 못했다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 이전 실행 2026-09-25-20 의 신규 출처(ref-258~ref-272, 예: Franke 외 VDA 5050 주변 설비 논문)는 참고문헌 목록에 없어 재사용하지 않았다.
