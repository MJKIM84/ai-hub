# 리서치 브리프 2026-10-10-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-05 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 28. 공용 자원·충전·에너지 최적화 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 호텔 연구 수치(ref-103)가 원문 미열람·저자 미확인 상태로 '거의 두 배'로 요약돼 있음
- 섹션 5. 적용 사례 (현장 유형 명시) — 제약 행의 '임계 저충전 수준 이하에서는 충전소로 가는 주문만 보내야 한다'가 원문 권고(should)보다 강함. 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 분리 페이지 53행의 is_parking_spot/is_charger 출처 충돌 미해소(oq-069), VDA 선언값과 Open-RMF 설정의 단위·의미 구분 없음(oq-068)
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — 승강기 메시지의 필드 범위와 배분 정책 부재 구분 없음(oq-067), Open-RMF 충전·뮤텍스 관련 2026년 수정 이력과 적용 버전 미기재
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 배터리 열화·공용 충전기 비중첩 제약을 함께 푸는 최신 연구, 에너지 공급과 결합한 충전 연구 없음(oq-066)
- 섹션 11. 열린 질문 — oq-066·oq-067·oq-068 부분 근거, oq-069 해소 근거 미반영
- 정정 요청 없음(target.json corrections 비어 있음). 외부 조사 메모의 '수정' 항목 두 건(5절 제약 행, 6절 분리 페이지 충돌 문장)을 정정 근거로 다룸

## 조사 질문

1. 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
2. oq-069 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? (섹션 6·11 겨냥)
3. oq-068 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? (섹션 5·6·11 겨냥)
4. oq-067 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? (섹션 7·11 겨냥)
5. oq-066 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? (섹션 8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 팩트시트의 batteryCharging.criticalLowChargingLevel 은 임계 충전 수준을 백분율(percent)로 선언하는 float64 필드다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [사실] | 같은 필드 설명은 그 충전 수준 이하에서 관제가 충전소로 가도록 지시하는 주문만 보내는 것이 좋다고 권고 표현(should)으로 기술한다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f3 | [의견] | 따라서 criticalLowChargingLevel 을 shall 수준의 의무 문구로 옮기거나 모든 로봇에 공통으로 정해진 충전 시작 비율로 설명해서는 안 되며, 제조사가 로봇별로 선언하는 값으로 다뤄야 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 팩트시트의 batteryCharging 객체는 criticalLowChargingLevel·maximumDesiredChargingLevel·minimumDesiredChargingLevel(모두 백분율)과 minimumChargingTime(초) 네 필드로 이루어진다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f5 | [사실] | Open-RMF fleet_adapter_template 의 config.yaml 은 recharge_threshold: 0.10 을 그 아래로는 로봇이 운행하지 않는 배터리 수준으로, recharge_soc: 1.0 을 충전 작업에서 채울 목표 배터리 수준으로 두며, 두 값은 0~1 비율로 적힌 템플릿 예시값이다. | ref-105 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [의견] | VDA 5050 의 백분율 선언값과 Open-RMF 의 비율 설정을 대조할 때는 단위를 먼저 맞추고, 운행 하한·충전 시작 판단·충전 목표를 별도 정책 항목으로 기록하는 편이 좋다. | ref-031, ref-105 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [추정] | 제조사가 팩트시트로 선언한 임계 충전 수준과 ROP 운영 설정(recharge_threshold) 가운데 어느 값을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 두 원문에 없었다. | ref-031, ref-105 | 아니오 | low | 2026-10-10 | — | — |
| f8 | [사실] | Open-RMF rmf_traffic 의 그래프 API(Graph.hpp)는 경유점에 주차 지점(is_parking_spot/set_parking_spot)과 충전 지점(is_charger/set_charger)을 서로 다른 속성으로 정의하며, 충전 지점은 배터리 충전 수준이 임계값 아래로 떨어진 로봇이 보내지는 곳으로 설명된다. | ref-536 | 아니오 | medium | 2026-10-10 | — | — |
| f9 | [사실] | rmf_fleet_adapter 2.14.0 의 그래프 파서(parse_graph.cpp)는 경유점 옵션 is_parking_spot 을 set_parking_spot(true)로, is_charger 를 set_charger(true)로 각각 따로 변환한다. | ref-1543 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [의견] | 따라서 이 구현에서 충전소 경유점 지정은 is_charger 로 확인되며, is_parking_spot 만 지정한 경유점을 충전소 지정과 같은 뜻으로 취급하면 안 된다. 지원 작업 문서의 is_parking_spot 서술과 생긴 출처 충돌(6절 분리 페이지)은 구현 기준으로 해소된다. | ref-536, ref-1543 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [사실] | Open-RMF LiftRequest 메시지는 lift_name·request_time·session_id·request_type(세션 종료·AGV 모드·사람 모드)·destination_floor·door_state 필드로 이루어지고, LiftState 메시지는 세션 종료 요청을 보낼 때까지 승강기 제어권을 받은 session_id 를 보고한다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | — | — |
| f12 | [사실] | LiftRequest·LiftState 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 직접 지정하는 필드가 없다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f13 | [의견] | 따라서 승강기 세션 점유·종료 인터페이스가 공개되어 있다는 사실과 공정한 대기열·묶음 운행 같은 배분 정책이 정의되어 있다는 주장은 구별해야 하며, 메시지 정의만 본 결론이므로 다른 감독 구성요소에 타임아웃이나 대기열 구현이 없다는 뜻으로 넓히지 않는다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | — | — |
| f14 | [사실] | Han 외(2025, Sensors)는 다층 호텔 배송 로봇의 경로 계획에서 승강기 노드를 암묵적 경유점으로 두고 문제를 다회 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)로 정식화해 적응형 대규모 이웃 탐색으로 푼다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f15 | [사실] | 이 논문은 고객 노드 60개 사례에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다고 보고한다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 / 제약 | — |
| f16 | [의견] | 이 수치는 승강기 운행 시간에 대한 모델 민감도이며 실제 물류센터에서 측정한 승강기 대기열 손실값이 아니다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f17 | [사실] | 논문은 무작위·동적 승강기 운행 시간, 동적 수요 변동, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링 알고리즘을 후속 연구 과제로 남긴다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f18 | [사실] | Li 외(2026, arXiv 2603.22731 프리프린트)는 작업 배정·서비스 순서·선택적 충전 결정·충전 방식 선택·공용 충전기 접근을 하나의 혼합 정수 선형 계획(Mixed-Integer Linear Programming, MILP)으로 함께 표현한다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f19 | [사실] | 이 모델의 목적함수는 총 배터리 열화, 충전기 대기, 납기 지연, 로봇 사이 열화 불균형을 함께 최소화한다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [사실] | 같은 논문 §2.6 의 식 (33)–(34)는 같은 충전기에서 일어날 수 있는 서로 다른 충전 세션 쌍(같은 로봇의 세션 쌍 포함)마다 순서 변수를 두어 충전 구간이 겹치지 않게 하는 비중첩 순서 제약이다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f21 | [사실] | 실험은 100×50 m 가상 창고, 동종 로봇, 표준·고속 두 충전 방식을 가정하며, §4.4 표 2 는 대표 사례(로봇 4·작업 40·충전기 2)의 '예시적 기대 평균(illustrative expected averages)'으로 총 열화가 규칙 기반 0.214 에서 0.098 로 준다고 보고하고, 기여 요약은 규칙 기반 대비 최대 54% 열화 감소를 적는다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [의견] | §4.4 가 비교표를 예시적 기대 평균으로 설명하고 열화를 축약 대리 모형으로 표현하므로, 최대 54% 열화 감소를 현장 배터리 수명 개선의 검증값으로 인용하지 않는 편이 좋다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [추정] | Yang 외(2026, Processes)는 냉동 컨테이너 온도 제약 아래 항만 무인운반차(Automated Guided Vehicle, AGV)의 작업 스케줄링과 충전을, 태양광·풍력·에너지 저장 장치(Energy Storage System, ESS)를 갖춘 항만 마이크로그리드 운영과 결합해 운영비를 최소화하는 2단계 물류–에너지 협조 최적화 프레임워크를 제시한 것으로 소개된다. | ref-1544 | 아니오 | low | 2026-10-10 | 실외 | 원문 미열람 |
| f24 | [의견] | 이 항만 연구는 물류 작업과 에너지 공급을 함께 계획하는 충전 연구의 후보 자료일 뿐이며, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 채택하지 않는다. | ref-1544 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f25 | [사실] | rmf_fleet_adapter 변경 이력의 2.12.0(2026-02-23) 판에는 충전 대기(WaitForCharge) 단계 완료 발행(#502)과 다음 작업에 충전량이 모자라면 충전기로 복귀하는 변경(#423)이 기록되어 있다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [사실] | 같은 변경 이력의 2.13.0(2026-06-15) 판에는 뮤텍스(Mutex) 잠금·해제 실행에서 생길 수 있는 교착을 고친 수정(#490)이 기록되어 있다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |
| f27 | [의견] | 따라서 Open-RMF 의 충전 작업 삽입·뮤텍스 그룹 기능을 인용할 때는 기능의 존재뿐 아니라 적용 버전과 이 수정들의 포함 여부를 함께 기록해야 하며, 이전 판이 모든 조건에서 교착 없이 동작했다는 근거로 쓰지 않는다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

- **f1**: 3.0.0 명세 factsheet 표 2148행: "criticalLowChargingLevel | float64 | Specifies the critical charging level in percent at or below which the fleet control should only send orders that command the mobile robot to a charging station." (발행일 미확인, 확인일 기준)
- **f2**: 3.0.0 명세 2148행 같은 행의 "should only send orders" 구절. 위키 5절 제약 행의 '보내야 한다'(근거 ref-228)는 원문의 권고 강도보다 강하다. 정정 대상 문장: "팩트시트의 임계 저충전 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다." (발행일 미확인, 확인일 기준)
- **f3**: 근거: 2148행이 should 를 쓰고 값은 팩트시트(로봇별 선언)에 들어간다. 5절 제약 행의 '보내야 한다'를 '보내는 것이 좋다(권고)'로 고치는 정정 근거.
- **f4**: 3.0.0 명세 2147~2151행: maximumDesiredChargingLevel "maximum desired charging level in percent", minimumDesiredChargingLevel "minimum desired charging level in percent", minimumChargingTime uint32 "desired minimum charging time in seconds". (발행일 미확인, 확인일 기준)
- **f5**: config.yaml 25~26행: "recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate", "recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks". 0.10 은 10% 에 해당하나 현장 권장값이 아니다. (발행일 미확인, 확인일 기준)
- **f6**: 근거: VDA 는 percent(2148~2150행), Open-RMF 템플릿은 0.10·1.0 비율(25~26행). VDA 의 임계 수준은 관제의 주문 제한 기준, Open-RMF 의 recharge_threshold 는 운행 하한으로 서로 의미가 다르다.
- **f7**: VDA 5050 3.0.0 명세 batteryCharging 행과 Open-RMF config.yaml 주석에 두 값의 동기화·우선순위 규정이 없음(확인한 범위 안의 부재). 다른 Open-RMF 구성요소에 그런 규칙이 있는지는 조사하지 않았다.
- **f8**: Graph.hpp 146~160행: "Returns true if this Waypoint is a charger spot. Robots are routed to these spots when their batteries charge levels drop below the threshold value." 주차 지점은 비상 경보 때 로봇이 스스로 주차하는 곳. 참고: set_charger 위 주석이 "Set this Waypoint to be a parking spot."으로 잘못 복사돼 있으나 함수 이름·인자(_is_charger)로 별도 속성임이 확인된다. (발행일 미확인, 확인일 기준)
- **f9**: 2.14.0 태그 parse_graph.cpp 170~176행: options["is_parking_spot"] → wp.set_parking_spot(true); 194~200행: options["is_charger"] → wp.set_charger(true). 두 분기는 독립적이다.
- **f10**: 정정 대상: 6절 분리 페이지(2026-09-25-area16-s6.md 53행) "한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다." Graph.hpp 와 parse_graph.cpp 는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않는다.
- **f11**: LiftRequest.msg: REQUEST_END_SESSION=0, REQUEST_AGV_MODE=1, REQUEST_HUMAN_MODE=2; "session_id should be unique at least between different requesters". LiftState.msg: "this field records the session_id that has been granted control of the lift until it sends a request with a request_type of REQUEST_END_SESSION". (발행일 미확인, 확인일 기준)
- **f12**: 두 메시지 전체 필드 대조: LiftRequest(lift_name, request_time, session_id, request_type, destination_floor, door_state), LiftState(lift_time, lift_name, available_floors, current_floor, destination_floor, door_state, motion_state, available_modes, current_mode, session_id). 시간 한도·시간창·다중 목적층 필드 없음. (발행일 미확인, 확인일 기준)
- **f13**: 근거: f11·f12 의 메시지 정의. 승강기 감독(lift supervisor) 등 다른 구성요소의 소스는 이번에 조사하지 않았다.
- **f14**: 초록·§2: "... nodes are modeled as implicit waypoints, and the routing problem is formulated as a Multi-Trip Vehicle Routing Problem (MTVRP). To solve this NP-hard problem, an Adaptive Large ..." Sensors 25(6) 1783, doi:10.3390/s25061783, 2025-03-13.
- **f15**: §4.4 Discussion(p.16): "in the scenario with 60 customer nodes, increasing elevator operation time from 40 s to 100 s nearly doubles the total travel time (from 225 s to 500 s)." 호텔 사례의 수치 실험이며 물류센터 적용은 미확인.
- **f16**: 근거: §4 는 가정한 승강기 운행 시간(40·50·60·70·80·100 s)을 바꾸는 수치 실험이다. 기존 3절의 '거의 두 배' 표현 대신 원 수치(225→500 s)를 쓰는 정정 근거.
- **f17**: §5: "Future research will explore ... random or dynamic elevator operation times, dynamic demand fluctuations ... multi-robot collaboration mechanisms, collision avoidance mechanisms (e.g., velocity obstacles), intelligent elevator scheduling algorithms". 여러 제조사 승강기 배분의 완성 사례로 쓰지 않는다.
- **f18**: 초록: "jointly optimizing task assignment, service sequencing, optional charging decisions, charging-mode selection, and charger access while balancing degradation across the fleet." v1, 2026-03-24.
- **f19**: §2.2 Objective function: "The objective minimizes total degradation, charger waiting, tardiness, and degradation imbalance"; 가중치 λ·µ·ρ 는 충전기 대기·납기 지연·불균형용.
- **f20**: §2.6 Shared-charger capacity constraints: 충전기 m 의 세션 집합 Ωm 은 모든 로봇 r 의 세션을 포함하고, "For each unordered pair of distinct sessions σ, σ′ ∈ Ωm, let uσ,σ′,m ∈ {0,1} enforce temporal ordering. Non-overlap is imposed by (33)–(34)".
- **f21**: §4.1: "100 × 50 m rectangular warehouse ... Robots are homogeneous with a two-mode charging set Lr = {standard, fast}". §4.4: "Table 2 reports illustrative expected averages for a representative instance with |R| = 4, |K| = 40, and |M| = 2". §1 기여 (3): "reduces total degradation by up to 54% over rule-based dispatch".
- **f22**: 근거: 초록 "reduced-form degradation proxies grounded in the empirical battery-aging literature", §4.4 "illustrative expected averages". 실물 배터리 노화 실험·공개 재현 데이터는 확인 못 함.
- **f23**: 원문 미열람. Crossref 초록 기준: 냉동 컨테이너 온도 제약, 항만 마이크로그리드(태양광·풍력·ESS), 운영비 최소화를 다루는 2단계 프레임워크. 초록에 '시간대별 전기 요금'·'충전소 용량' 표현은 직접 나오지 않는다. 출판사 본문 열기 실패.
- **f24**: 원문 미열람. 항만(냉동 컨테이너·마이크로그리드)과 실내 물류센터의 적용 조건이 다르다. oq-066(시간대별 요금·최대 수요 전력 기준 충전 계획)에는 후보 자료 수준의 부분 근거만 된다.
- **f25**: 2.14.0 태그 CHANGELOG.rst 57~77행, 2.12.0 (2026-02-23): "Publish WaitForCharge phase completed (#502)", "Retreat to charger if there will not be enough charge for the next task (#423)".
- **f26**: CHANGELOG.rst 28~46행, 2.13.0 (2026-06-15): "Fix potential deadlocks from execution of mutex lock and release (#490)". 최신 판 2.14.0 은 2026-09-26.
- **f27**: 근거: f25·f26 의 2026년 수정 이력. 위키 6절 분리 페이지의 충전 작업 삽입·뮤텍스 그룹 서술은 판을 적지 않았다.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-1543 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-103 | Linghui Han, Junzhe Ding, Songtao Liu, Meng Meng (Sensors) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 2025-03-13 | 논문 | medium | 2026-10-10 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03-24 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2603.22731 | 아니오 |
| ref-1544 | Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI) | A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints | 2026-07-27 | 논문 | medium | 2026-10-10 | https://www.mdpi.com/2227-9717/14/15/2424 | 예 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 이번에는 3.0.0 태그판의 팩트시트 batteryCharging 표(임계·최대·최소 희망 충전 수준 백분율, 최소 충전 시간)를 대조했다.
- **ref-105**: Open-RMF 플릿 어댑터 설정 템플릿. recharge_threshold(운행 하한 비율 0.10)와 recharge_soc(충전 목표 비율 1.0) 등 배터리·충전 설정 예시값을 담는다.
- **ref-536**: Open-RMF 교통 그래프 API 헤더. 경유점의 주차 지점·충전 지점·대기 지점 속성과 뮤텍스 그룹 등을 정의한다(set_charger 위 주석은 주차 지점 문구가 잘못 복사돼 있음).
- **ref-1543**: rmf_fleet_adapter 2.14.0 태그의 탐색 그래프 YAML 파서. 경유점 옵션 is_parking_spot·is_holding_point·is_passthrough_point·is_charger 를 각각 별도 속성으로 변환한다(발행일은 2.14.0 패키지판 날짜).
- **ref-312**: Open-RMF 승강기 요청 메시지. 승강기 이름·요청 시각·세션 id·요청 유형(세션 종료·AGV 모드·사람 모드)·목적층·문 상태 필드를 정의한다.
- **ref-286**: Open-RMF 승강기 상태 메시지. 층·문·운행·모드 상태와 세션 종료 요청 때까지 제어권을 가진 session_id 를 보고한다.
- **ref-103**: Sensors 25(6) 1783, doi:10.3390/s25061783. 다층 호텔 배송 로봇 경로 계획을 승강기 노드를 암묵적 경유점으로 둔 MTVRP 로 정식화하고 승강기 운행 시간 민감도를 수치 실험한다. 이번 실행이 출판 PDF 첫 원문 열람이다(PMC·출판사 HTML 접근 실패).
- **ref-403**: arXiv 프리프린트 v1. 작업 배정·순서·충전 방식·공용 충전기 비중첩 제약을 MILP 로 함께 풀어 열화·충전기 대기·납기 지연·열화 불균형을 줄이는 계층형 해법을 제시한다(가상 창고 수치 실험).
- **ref-1544**: 원문 미열람. Crossref 초록 기준으로 냉동 컨테이너 온도 제약 아래 항만 AGV 작업·충전을 태양광·풍력·ESS 를 갖춘 항만 마이크로그리드와 결합해 운영비를 최소화하는 2단계 프레임워크다.
- **ref-1398**: rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.12.0(2026-02-23)의 충전 대기 단계 완료 발행·충전기 복귀 변경과 2.13.0(2026-06-15)의 뮤텍스 잠금·해제 교착 수정을 기록한다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md | 3, 5, 6, 7, 8, 11 | 갱신(차등): 섹션 3 — 호텔 연구 수치를 원문(§4.4 p.16) 기준 225→500 s 로 적고 저자·발행일 보강(f15), 모델 민감도임을 명시(f16) / 섹션 5 — 정정: 제약 행 '보내야 한다'를 권고(should)로 고치고 단위를 충전 수준(백분율)로 명시(f1·f2·f3); 상업 시설(호텔) 사례 추가(f14·f15·f16·f17) / 섹션 6(주제 페이지 요약) — 정정: 분리 페이지 53행 is_parking_spot/is_charger 충돌 문장을 구현 기준 해소로 교체(f8·f9·f10); VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분(f4·f5·f6·f7) / 섹션 7(주제 페이지 요약) — 승강기 메시지 전체 필드와 배분 정책 필드 부재(f11·f12·f13; 세션 종료 전 제어권 유지는 기존 내용 확인), rmf_fleet_adapter 2026년 수정 이력과 버전 기록(f25·f26·f27) / 섹션 8(주제 페이지 요약) — Li 외 열화·공용 충전기 MILP(f18~f22), Yang 외 항만 물류–에너지 협조 연구는 원문 미열람 후보(f23·f24) / 섹션 11 — oq-069 해소 제안(f8·f9·f10), oq-068 부분 근거(f4~f7), oq-067 부분 근거(f11~f13), oq-066 후보 자료(f23·f24), 새 질문 4건. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f20 | 종류: 일반
- 충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 표현 | 근거: f5·f6 | 종류: 일반
- 배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21·f22 | 종류: 일반
- 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 22. 설비·건물 시스템 연동 | 근거: f15·f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-069

## 자체 점검

- 출처 수: 10 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 3건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-05/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - f23·f24: Yang 외(ref-1544) 원문 미열람. Crossref 초록만 확인했고 비용 절감 수치·요금제·충전소 용량 모델은 미확인
    - f7: 임계 충전 수준과 recharge_threshold 의 우선순위 규칙 부재는 두 원문 범위 안의 확인이며, Open-RMF 다른 구성요소·VDA 5050 다른 절 전체를 뒤지지는 않음
    - f13: 승강기 감독(lift supervisor) 등 메시지 밖 구성요소의 타임아웃·대기열 구현은 조사하지 않음
    - f22: Li 외 결과를 실물 배터리 노화 실험·공개 재현 데이터로 확인하지 못함
    - VDA 5050 3.0.0 발표일은 근거 미확인이라 적지 않음(published null)
    - oq-066: 물류센터 로봇의 시간대별 전기 요금·최대 수요 전력 기준 충전 계획 연구와 국내 사례는 찾지 못함(항만 후보 자료만)
    - 섹션 5 의 물류창고 외 현장 유형 사례는 호텔(상업 시설)·항만(실외, 미열람) 외에는 찾지 못함
- 범위 경계 위반 의심:
    - f8·f9: 경유점 속성 정의는 15. 지도·공간·위치 모델과 겹치므로 이 영역에서는 충전소 지정 판별 근거로만 씀
    - f11~f13: 승강기 메시지 인터페이스는 22. 설비·건물 시스템 연동 소관이며 이 영역에는 공용 자원 배분 정책의 유무 근거로만 씀
    - f23·f24: 항만 마이크로그리드 운영은 ROP 직접 범위 밖(시설·에너지 설비 쪽 연계 대상)이며 충전 계획 연구 후보로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 3건(ref-1543~ref-1398, 예약 구간 ref-1543~ref-1572 안), 재사용 7건(ref-031·ref-105·ref-536·ref-312·ref-286 github_raw, ref-103·ref-403 webfetch). ref-103 은 기존 위키 출처(원문 미열람·저자 미확인)와 같은 논문으로, 이번이 첫 원문 열람이며 저자·발행일·doi 를 보강했다(메모의 '재열람' 표현은 틀림). ref-403 은 영역 24 등에서 쓰인 기존 id 를 재사용했다. 검증 수정 반영: criticalLowChargingLevel 을 '충전 수준(백분율)'로 표기(f1), 호텔 논문 셋째 문장을 의견으로 강등(f16), Li 외 식 (33)–(34)를 같은 충전기의 세션 쌍 비중첩 제약으로 정정하고 목적에 충전기 대기·불균형 포함(f19·f20), 변경 이력 원문 문구 정정(f25·f26), Yang 외 서술을 Crossref 초록 내용으로 교체(f23), Graph.hpp 주석 복사 오류 기록(f8), LiftRequest 에 lift_name 포함(f11), VDA 5050 발표일 null. VDA 5050 3.0.0 release notes 출처는 넣지 않았다. 교차 확인 0건: Graph.hpp 와 parse_graph.cpp, 두 승강기 메시지는 같은 프로젝트 자료라 독립 출처가 아니다. 현장 유형: 상업 시설(호텔, f14~f17), 실외(항만, f23, 미열람). 열린 질문: oq-069 해소 제안(f8~f10), oq-066·oq-067·oq-068 은 부분 근거만. 정정 요청 없음, 우선 지정 질문 없음.
