# 리서치 브리프 2026-09-25-40

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-40 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 16. 공용 자원·충전·에너지 최적화 |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 floorplan-recognition 단계 1 반영 제안(충전소 위치 정보 출처: ref-079·ref-216·ref-219) 검토 대상
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안 2건(VDA 5050 startCharging·stopCharging과 구역 유형, Nav2 도킹 / VDA 5050 팩트시트 batteryCharging) 검토 대상
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음 — 트랙 반영 제안(Stark 외 2024 충전소 배치 → 3. 처리능력·거점·설비 계획) 검토 대상
- 섹션 11. 열린 질문 비어 있음(기존 oq-016 이 이 영역에 걸림)

## 조사 질문

1. 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
2. VDA 5050·Open-RMF 같은 표준·오픈소스는 충전 명령, 배터리 상태, 충전 임계값, 충전기 위치를 어떤 필드와 동작으로 표현하는가? (섹션 4·7 겨냥, 트랙 반영 제안 2건 검증)
3. 충전기·승강기·통로 구간 같은 공용 자원을 한 번에 한 로봇에 배분하거나 예약하는 오픈소스 장치(뮤텍스 그룹, 승강기 세션, 예약 시스템)는 무엇인가? (섹션 6·7 겨냥)
4. 충전 시점·충전기 선택·충전 방식(플러그인·교환·유도)과 충전기 대수를 정하는 대표 연구는 무엇이고 어떤 결과를 보고하는가? (섹션 6·8 겨냥, 트랙 반영 제안 ref-109 검토)
5. 다층 시설에서 승강기가 로봇 배송의 병목이 되는 근거와 승강기 선택·층간 이동을 다룬 연구(국내 포함)는 무엇인가? (섹션 3·5·8 겨냥)
6. 충전 대기·배터리 제약을 작업 배정과 함께 푸는 연구와 학습 기반 충전 결정은 13. 작업 배정 — MRTA·27. AI·학습·적응과 모델 운영과 어떻게 연결되는가? (섹션 6·10 겨냥)
7. ROP가 직접 맡을 충전·공용 자원 계획과 로봇 자체 제어(과충전 보호·정밀 도킹)·설비 안전 제어 사이 경계는 어디인가? — oq-016(충전·대기 시간의 OEE 손실 분류)과 연결 (섹션 9·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0(main)은 충전을 즉시 동작 또는 노드 동작인 startCharging·stopCharging 으로 표현하며, 충전은 정지한 충전 지점이나 주행 중 충전 차선에서 할 수 있고 과충전 보호는 이동로봇의 책임이다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 관제(fleet control)의 기능으로 에너지 관리를 들며, 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 최신 팩트시트 스키마의 batteryCharging 은 criticalLowChargingLevel(이 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 함), minimumDesiredChargingLevel, maximumDesiredChargingLevel, minimumChargingTime 네 항목을 로봇 선언으로 둔다. | ref-228 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | VDA 5050 최신 상태 스키마의 powerSupply 는 충전 상태(stateOfCharge, %), 충전 중 여부(charging), 배터리 전압·전류, 건강 상태(batteryHealth), 현재 충전량으로 갈 수 있는 거리(range, m)를 담으며, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다. | ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 명세는 충전소를 별도 구역 유형으로 두지 않고 충전을 주문의 노드 동작과 즉시 동작으로 다룬다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 템플릿 설정은 로봇이 운행하지 않는 배터리 하한(recharge_threshold), 충전 목표(recharge_soc), 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다. | ref-105 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f7 | [사실] | Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다. | ref-039, ref-104 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [사실] | Open-RMF 작업 계획기(rmf_task TaskPlanner)는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다. | ref-377 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓰고, 주차 예약 시스템 사용은 기본값 꺼짐이지만 켜기를 권장한다. | ref-079, ref-864, ref-865 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹(mutex group)에 넣을 수 있고, 같은 뮤텍스 그룹에 속한 경유점이나 차선은 한 번에 한 로봇만 점유할 수 있다. | ref-864 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f11 | [사실] | Open-RMF 승강기 요청은 요청자별 고유 세션 id 로 승강기를 점유하며, 승강기 상태는 세션 종료 요청(REQUEST_END_SESSION)을 보낼 때까지 제어권을 받은 세션 id 를 기록하고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다. | ref-312, ref-286 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f12 | [사실] | Open-RMF 의 실험적 예약 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개된다. | ref-866 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [사실] | 연계 대상: Nav2 도킹 프레임워크는 환경 안 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며, 센서로 도크 자세를 보정하고 도킹 뒤 충전 시작 여부(isCharging)를 확인한다. | ref-216 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f14 | [추정] | MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다. | ref-219 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f15 | [사실] | Zou·Gong·de Koster·Xu(2018)는 로봇 이동형 풀필먼트 시스템(RMFS)에서 플러그인 충전·배터리 교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교해, 유도 충전이 회수 처리 시간에서 가장 좋고 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다. | ref-098 | 아니오 | medium | 2018 | 피킹 / 예외·성과 | 원문 미열람 |
| f16 | [사실] | Chen·Gong·Chen·Wang(2024)은 자가 등반 로봇(SCR) 창고의 배터리 관리를 반개방형 대기행렬 네트워크로 모델링해, 배터리 열화를 반영하면 느린 충전이 빠른 충전보다 나은 조건이 있고, 우선 충전 정책이 전용 충전 정책보다 비용 효율적이며, 충전기 대수 결정 도구를 제시했다. | ref-861 | 아니오 | medium | 2024-01 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | 다중 AGV 충전 순서 최적화 연구(Computers & Industrial Engineering, 2024)는 도착 시 충전소가 사용 중일 확률과 충전 전 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적임을 보였다. | ref-858 | 아니오 | medium | 2024-08 | 제약 | 원문 미열람 |
| f18 | [사실] | Dang·Singh·Adan·Martagan·van de Sande(2021)는 다중 적재·다능력 AGV 에 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 혼합 정수 선형 계획과 적응형 대규모 이웃 탐색을 제시해, 현행 방식 대비 비용을 약 20~50% 줄였다고 보고했다. | ref-862 | 아니오 | medium | 2021-12 | 수행 자원 | 원문 미열람 |
| f19 | [사실] | 근접 정책 최적화(PPO) 기반 심층 강화학습 연구(arXiv 2607.05683)는 고정 충전소가 있는 다중 블록 창고에서 주문이 확률적으로 도착할 때 충전소 선택과 충전 시간을 충전소 대기 예상 시간을 반영해 학습하며, 고정 규칙 휴리스틱은 동적 환경과 다중 로봇 조율에서 비효율적이라고 지적한다. | ref-859 | 아니오 | medium | 2026-07 | 피킹 / 예외·성과 | 원문 미열람 |
| f20 | [사실] | Ma·Zhou·Stephen(2020)은 자동화 컨테이너 터미널의 배터리 AGV 시스템을 시뮬레이션해 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다. | ref-860 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f21 | [사실] | Stark 외(2024)는 창고 안 충전소의 최적 배치를 PageRank 와 비슷한 방법으로 다룬 연구를 발표했다. | ref-109 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f22 | [사실] | Omega 게재 논문(2024)은 로봇 이동형 풀필먼트 시스템의 성능 평가에 로봇 에너지 소비를 넣고 동적 우선순위를 쓰는 운영 정책을 다룬다. | ref-146 | 아니오 | low | 2024 | — | 원문 미열람 |
| f23 | [사실] | 고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다. | ref-060 | 아니오 | medium | 2026 | 제약 | 원문 미열람 |
| f24 | [사실] | 다층 호텔 배송 경로 계획 연구는 승강기를 층간 이동의 대기·운행 시간으로 모델링했고, 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 거의 두 배가 된다고 보고했다. | ref-103 | 아니오 | medium | 2025 | 예외·성과 | 원문 미열람 |
| f25 | [사실] | Electronics(2025) 게재 논문은 실내 배송 로봇의 그래프 기반 다층 경로 계획에서 승강기 선택을 최적화하는 방법을 제시한다. | ref-321 | 아니오 | low | 2025 | — | 원문 미열람 |
| f26 | [사실] | 박재범·조성준·김준식·유범재(2024)는 서버를 통해 엘리베이터를 신속하게 제어하는 모듈과 작업 구조로 층간 이동을 처리하고, 노드 그래프 기반으로 한 번의 주행에서 여러 목적지를 고려하는 다층 경로 계획 알고리즘을 제안해 실증 시험과 주행 시간 비교로 검증했다. | ref-863 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f27 | [추정] | 분류 원문 질문(로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까)에 대해, 로봇마다 같은 충전 임계값(criticalLowChargingLevel, recharge_threshold)으로만 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. | ref-228, ref-105, ref-858, ref-859, ref-861, ref-312 | 아니오 | low | 2026-09-25 | 제약 | — |
| f28 | [추정] | 피킹 성수기에는 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기고 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대에 기회 충전을 넣거나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. | ref-862, ref-859, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f29 | [추정] | 다층 시설의 출하 단계에서는 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 승강기 호출을 조율 계층이 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다. | ref-312, ref-286, ref-103 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f30 | [추정] | ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력이며, 이는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. | ref-031, ref-104, ref-864, ref-312 | 아니오 | low | 2026-09-25 | — | — |
| f31 | [추정] | 연계 대상: 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다. | ref-031, ref-216, ref-284 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f32 | [추정] | 충전소 정보는 시설 안 설비 위치(도크 인스턴스 자세)와 로봇이 경로 그래프에서 접근하는 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다. | ref-216, ref-079, ref-865 | 아니오 | low | 2026-09-25 | — | — |
| f33 | [추정] | 이 영역은 충전 요청을 작업 배정과 함께 푸는 연구로 13. 작업 배정 — MRTA 와, 뮤텍스 그룹·대기 지점으로 15. 다중 로봇 경로·교통 관리 — MAPF 와, 승강기 세션으로 10. 설비·건물 시스템 연동과, 충전기 대수·배치로 3. 처리능력·거점·설비 계획과, 팩트시트 충전 설정으로 5. 로봇 능력·작업 온톨로지와, 현재 배터리 상태로 8. 실시간 세계 상태·데이터 일관성과, 충전 정책 시뮬레이션으로 22. 시뮬레이션·예측용 디지털 트윈과, 학습 기반 충전 결정으로 27. AI·학습·적응과 모델 운영과 이어지는 것으로 보인다. | ref-862, ref-864, ref-312, ref-861, ref-109, ref-228, ref-051, ref-860, ref-859 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: VDA5050_EN.md 원본(github_raw) 동작 표: startCharging 'Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). Protection against overcharging is the responsibility of the mobile robot.' (발행일 미확인, 확인일 기준)
- **f2**: VDA5050_EN.md 원본 5.3 관제 기능: 에너지 관리 — 충전 주문이 운반 주문을 중단할 수 있음. 충전 순서·시점 결정 알고리즘은 규정하지 않음. (발행일 미확인, 확인일 기준)
- **f3**: factsheet.schema 원본(github_raw): criticalLowChargingLevel 'at or below which the fleet control should only send orders that command the mobile robot to a charging station'; minimumChargingTime 'desired minimum charging time in seconds'. (발행일 미확인, 확인일 기준)
- **f4**: state.schema 원본(github_raw): stateOfCharge 'If mobile robot only provides values for good or bad battery levels, these will be indicated as 20% (bad) and 80% (good).' range 'Estimated reach with current State of Charge in meter.' (발행일 미확인, 확인일 기준)
- **f5**: VDA5050_EN.md 원본: 구역 유형(BLOCKED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT 등)에 충전 구역 없음, 충전은 startCharging 동작으로 표현(트랙 실행 2026-09-25-19 반영 제안을 이번에 원문으로 재확인). (발행일 미확인, 확인일 기준)
- **f6**: config.yaml 원본(github_raw): 'recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate', 'recharge_soc: 1.0', 'charging_current: 5.0 # A', 'account_for_battery_drain: True', 로봇마다 charger 지정. 예시값. (발행일 미확인, 확인일 기준)
- **f7**: task_types.md 원본: 'This is a self-generated task, self generated by RMF fleet adapter.' rmf_demos README 원본: 'ChargeBattery tasks are optimally injected into a robot's schedule when the robot has insufficient charge'; 'we assume each robot in the map has a dedicated charging location'. 같은 발행 주체. (발행일 미확인, 확인일 기준)
- **f8**: TaskPlanner.hpp 원본(github_raw): 'sufficient initial charge to even head back to their charging stations'; 해결책으로 배터리 용량 증대 또는 threshold_soc 낮추기 제시; BatteryAware 설정 'strongly penalize low SOC with a quadratic term'. (발행일 미확인, 확인일 기준)
- **f9**: traffic-editor.md 원본: is_charger 이면 'rmf_fleet_adapter will treat this as a charging station'. Graph.hpp: 'Robots are routed to these spots when their batteries charge levels drop below the threshold value.' RobotUpdateHandle.hpp: 지정 없으면 가장 가까운 is_charger 경유점. (발행일 미확인, 확인일 기준)
- **f10**: Graph.hpp 원본(github_raw) in_mutex_group(): 'Only one robot at a time is allowed to occupy any waypoint or lane associated with a particular mutex group.' 저장소 이슈에 동시 진입 버그 보고가 있어 동작 신뢰성은 미확인. (발행일 미확인, 확인일 기준)
- **f11**: LiftRequest.msg 원본: 'session_id should be unique at least between different requesters'; 'AGV mode means that the doors are always open when the lift is stopped'. LiftState.msg 원본: session_id 'has been granted control of the lift until it sends a request with a request_type of REQUEST_END_SESSION'. (발행일 미확인, 확인일 기준)
- **f12**: 검색 요약: 'Experimental reservation library in rust'; 'A robot may request the use of a resource like a charger for a fixed duration of time within a given time range'. README 원본은 main·master 경로 모두 404로 열지 못함.
- **f13**: nav2_docking README 원본(github_raw): 'dock with charging stations, as well as non-charging infrastructure such as static locations (ex. conveyers) or dynamic locations (ex. pallets)'; getRefinedPose 로 센서 보정; isCharging·hasStoppedCharging. (발행일 미확인, 확인일 기준)
- **f14**: 벤더 주장: 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본의 충전 마커 설정 절. 이번 실행에서 원문 미열람. (재인용: 2026-09-25-19)
- **f15**: 검색 요약: 'Inductive charging performs the best in terms of retrieval throughput time'; 배터리 비용이 낮을 때 교환이 플러그인보다 저렴. EJOR 267(2), 733–753. 원문 미열람.
- **f16**: 검색 요약: 'slow charging outperforms fast charging' 조건 도출, 'The priority charging policy is more cost-effective than the dedicated charging policy', 충전기 대수 결정 도구. EJOR 312(1), 164–181. 원문 미열람.
- **f17**: 검색 요약: 'two random variables for each charging station—one modeling the probability of finding the station busy upon arrival, and another modeling the probability of having to wait'; 'fully recharging to the maximum allowed is optimal'. 저자 미확인. 원문 미열람.
- **f18**: 검색 요약: 'assigning transport and charging requests to AGVs, sequencing these requests, and determining the arrival times and charging duration'; 'about 20%–50% cost reduction with respect to current practice'(저자 보고). 원문 미열람.
- **f19**: 검색 요약: 'charging station selection and optimal charging duration, explicitly accounting for anticipated queuing times at the stations'; 'fixed-rule heuristics often prove suboptimal'. 프리프린트, 성능 비교는 저자 보고. 원문 미열람.
- **f20**: 검색 요약: 'a decentralized charging station layout and a progressive recharging policy lead to excellent performance'. Simulation Modelling Practice and Theory 106. 항만 사례라 물류센터 적용은 미확인. 원문 미열람.
- **f21**: 참고문헌 목록 제목 기준: 'A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse'(arXiv 2406.17003). 이번 실행에서 원문 미열람. (재인용: 2026-09-25-19)
- **f22**: 참고문헌 목록 제목 기준: 'The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority'. 결과 수치 미확인.
- **f23**: Digital Health 2026 논문. 병원 사례이며 물류센터 적용은 미확인(oq-010). 결과 수치는 원문 미열람으로 쓰지 않음. (재인용: 2026-09-25-38)
- **f24**: 검색 요약: 'increasing elevator operation time from 40 s to 100 s nearly doubles the total travel time (from 225 s to 500 s)'. Sensors 게재(doi 10.3390/s25061783). 호텔 사례. 원문 미열람.
- **f25**: 검색 결과 제목 기준: 'Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots'. 결과 수치 미확인. 원문 미열람.
- **f26**: 검색 요약(국문): 서버를 통한 엘리베이터 제어 모듈과 task 구조, 노드 그래프 기반 다층 경로 계획, 다수 실증 테스트. 배송 로봇 대상(물류센터 아님). 원문 미열람.
- **f27**: f3·f6(임계값 기반 충전 시작), f17·f19(대기 반영 충전 결정), f16(우선 충전 정책), f11·f12(세션·예약)를 SCM 질문에 대응시킨 이 위키의 추론. 물류센터 실측 자료는 확인 못함.
- **f28**: f18(운반·충전 요청 동시 배정과 부분 충전), f19(확률적 주문 도착 하의 충전 결정), f2(충전 주문이 운반 주문을 중단 가능)를 현장 시나리오로 조합한 추론. 실제 현장 사례는 확인 못함.
- **f29**: f11(세션 점유), f24(승강기 운행 시간에 따른 총 이동 시간 증가)를 출하 단계에 적용한 추론. 물류센터 정량 자료는 oq-010 미해결.
- **f30**: f2·f7·f10·f11 을 분류 원문 9장 경계에 대응시킨 추론.
- **f31**: f1('Protection against overcharging is the responsibility of the mobile robot'), f13(도크 자세 보정·충전 확인은 로봇 쪽 프레임워크), Lifts 문서의 승강기 어댑터가 승강기 동작을 방해하는 요청을 막는 역할에서 도출.
- **f32**: f9(경유점 주석·가장 가까운 충전 경유점)와 f13(도크 위치 데이터베이스·센서 보정)을 결합한 추론(트랙 실행 2026-09-25-19 f19 의 추정을 이번 원문으로 뒷받침).
- **f33**: f18·f10·f11·f16·f21·f3·f4·f20·f19 를 영역 연결로 정리한 추론. 8번(현재 배터리 상태)과 22번(충전 정책을 가정해 실험하는 시뮬레이션)은 구분.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_types.html | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 아니오 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md | 아니오 |
| ref-219 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.17003 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.1177/20552076261437181 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics14050982 | 예 |
| ref-858 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach | 2024-08 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0360835224006314 | 예 |
| ref-859 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.05683 | 예 |
| ref-860 | Ma, N., Zhou, C., & Stephen, A. | Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals | 2020 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X | 예 |
| ref-861 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 예 |
| ref-862 | Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D. | Scheduling heterogeneous multi-load AGVs with battery constraints | 2021-12 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0305054821002586 | 예 |
| ref-863 | 박재범, 조성준, 김준식, 유범재 | 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템 | 2024 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904 | 예 |
| ref-864 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-865 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 아니오 |
| ref-866 | Open Robotics (open-rmf) | rmf_reservation — Experimental reservation library in rust (GitHub) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_reservation | 예 |

### 출처 요약

- **ref-031**: VDA 5050 최신판(main, 3.0.0) 명세 원문. 이번 실행은 startCharging·stopCharging 동작, 관제의 에너지 관리 기능, 구역 유형을 원문으로 확인했다.
- **ref-228**: VDA 5050 팩트시트 JSON 스키마. 이번 실행은 batteryCharging 네 항목을 원문으로 확인했다.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마. 이번 실행은 powerSupply 항목을 원문으로 확인했다.
- **ref-105**: 플릿 어댑터 설정 템플릿. 이번 실행은 충전 임계값·충전 목표·배터리·전력 소비·작업 종료 동작·로봇별 충전기 항목을 원문으로 확인했다.
- **ref-079**: Open-RMF 교통 편집기 문서. 이번 실행은 is_charger·dock_name·대기 지점 속성과 승강기를 공유 자원으로 보는 서술을 원문으로 확인했다.
- **ref-039**: Open-RMF 지원 작업 유형 문서. 이번 실행은 충전 작업이 플릿 어댑터가 스스로 만드는 작업이라는 서술을 원문으로 확인했다.
- **ref-104**: Open-RMF 데모 README. 이번 실행은 충전 작업의 일정 삽입과 로봇별 전용 충전 위치 가정을 원문으로 확인했다.
- **ref-377**: Open-RMF 작업 계획기 헤더. 이번 실행은 충전량 부족 오류 구분과 배터리 우선 비용 설정을 원문으로 확인했다.
- **ref-312**: 승강기 요청 메시지. 이번 실행은 세션 id, 요청 유형, AGV 모드의 문 동작을 원문으로 확인했다.
- **ref-286**: 승강기 상태 메시지. 이번 실행은 제어권을 받은 세션 id 기록과 운영 모드를 원문으로 확인했다.
- **ref-284**: Open-RMF 승강기 연동 문서. 이번 실행은 승강기 어댑터의 역할을 원문으로 확인했다(여러 플릿 사이 배분 규칙은 문서에 없음).
- **ref-216**: Nav2 도킹 프레임워크 README. 이번 실행은 도크 데이터베이스, 충전·비충전 도크 플러그인, 센서 보정, 충전 확인 함수를 원문으로 확인했다.
- **ref-219**: 원문 미열람. 이번 실행에서 다시 열지 않았다. 지도에 충전 스테이션 마커를 설정하는 매뉴얼 절.
- **ref-098**: 원문 미열람. RMFS 에서 플러그인·교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교한 EJOR 논문.
- **ref-109**: 원문 미열람. 창고 충전소 배치를 PageRank 와 비슷한 방법으로 최적화한 프리프린트.
- **ref-146**: 원문 미열람. RMFS 성능 평가에 에너지 소비를 넣고 동적 우선순위 운영 정책을 다룬 논문(제목 기준).
- **ref-060**: 원문 미열람. 병원 약품 배송 로봇의 승강기 이용과 배송 실패·시간의 관계를 다룬 논문.
- **ref-103**: 원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링한 논문.
- **ref-321**: 원문 미열람. 실내 배송 로봇의 다층 경로 계획에서 승강기 선택을 최적화한 논문.
- **ref-858**: 원문 미열람. 충전소 사용 중·대기 확률을 확률 변수로 둔 다중 AGV 충전 순서 최적화(혼합 정수 선형 계획) 논문.
- **ref-859**: 원문 미열람. 다중 블록 창고에서 PPO 기반 강화학습으로 충전소 선택과 충전 시간을 학습하는 프리프린트.
- **ref-860**: 원문 미열람. 자동화 컨테이너 터미널의 충전소 배치와 배터리 AGV 충전 정책을 시뮬레이션으로 평가한 논문(Simulation Modelling Practice and Theory 106).
- **ref-861**: 원문 미열람. 자가 등반 로봇 창고에서 충전 기술·충전 정책·충전기 대수를 반개방형 대기행렬 네트워크로 분석한 EJOR 312(1) 논문.
- **ref-862**: 원문 미열람. 운반·충전 요청을 함께 배정·순서화하고 부분 충전 시간을 정하는 MILP·적응형 대규모 이웃 탐색 논문(Computers & Operations Research).
- **ref-863**: 원문 미열람. 서버 기반 엘리베이터 제어 모듈과 노드 그래프 기반 다층·다중 목적지 경로 계획을 제안하고 실증 시험한 국내 논문.
- **ref-864**: Open-RMF 교통 그래프 헤더. 경유점·차선의 뮤텍스 그룹(한 번에 한 로봇만 점유), 충전 경유점·주차 지점·대기 지점, 문·승강기 문 차선 조건을 정의한다. 이번 실행에서 원본을 열었다.
- **ref-865**: 플릿 어댑터 로봇 갱신 인터페이스 헤더. 로봇별 충전 경유점 지정, 주차 예약 시스템 사용 설정, 배터리 충전 상태 갱신, 승강기 세션 정보를 다룬다. 이번 실행에서 원본을 열었다.
- **ref-866**: 원문 미열람. 충전기 같은 자원을 시간 범위 안에서 정해진 시간 동안 로봇에 배정하는 실험적 제약 자원 스케줄링 라이브러리(검색 요약 기준). README raw 경로는 404.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절: f27(SCM 질문 — 같은 임계값에 따른 충전 수요 겹침), f23·f24(승강기 병목 근거), f15·f16(충전 정책이 처리량·비용에 미치는 영향) / 4절: f3·f4(충전 상태·임계 저충전 수준), f6(recharge_threshold·recharge_soc), f10(뮤텍스 그룹), f11(승강기 세션), f15(플러그인·교환·유도 충전) / 5절: f28(피킹, 예외·성과), f29(출하, 제약), f7(시작 조건) / 6절: f7·f8·f9·f10·f11·f12, f17·f18·f19·f20, f32 — 트랙 floorplan-recognition 반영 제안(충전소 위치 정보 출처) 검토 결과: f9(ref-079 is_charger, 원문 확인)·f13(Nav2 도크 데이터베이스, 연계 대상)·f14(MiR, 벤더 주장 유지)·f32(시설 위치와 접근 지점 분리 [추정]) 반영 / 7절: f1·f2·f3·f4·f5(VDA 5050 — 트랙 반영 제안 2건을 원문으로 재확인, 필드 이름은 스키마 기준 minimumDesiredChargingLevel·maximumDesiredChargingLevel), f6~f12(Open-RMF), f13(Nav2 도킹) / 8절: f15~f26(국내 f26) / 9절: f30(직접 범위), f31(연계 대상) / 10절: f33 — 트랙 반영 제안(Stark 외 2024 → 3. 처리능력·거점·설비 계획) 반영(f21), f19 는 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 11절: 기존 oq-016 과 새 열린 질문 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 충전 상태 | State of Charge (SOC) | 배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다. |
| 뮤텍스 그룹 | Mutex Group (Open-RMF) | Open-RMF 교통 그래프에서 같은 그룹에 묶인 경유점·차선을 한 번에 한 로봇만 점유하도록 하는 상호 배제 단위이다. |
| 승강기 세션 | Lift Session (Open-RMF) | Open-RMF 에서 한 요청자가 세션 id 로 승강기 제어권을 받아 세션 종료 요청을 보낼 때까지 점유하는 단위이다. |
| 배터리 교환 | Battery Swapping | 방전된 로봇 배터리를 충전기에 꽂아 기다리는 대신 충전된 배터리로 바꿔 끼워 로봇을 곧바로 다시 운행하게 하는 충전 방식이다. |

## 열린 질문

새로 생긴 질문:

- 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f1 | 종류: 일반
- 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 4. 성과·경제성·프로세스 개선 | 근거: f17 | 종류: 일반
- 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 10. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반
- 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 온톨로지 | 근거: f3 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 28 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 9건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 표준·오픈소스 내용은 단일 발행 주체, 연구 결과는 각 논문 단일 출처
    - f12 rmf_reservation README 원문 열지 못함(main·master 404), 배포판 사용 여부 미확인
    - f10 뮤텍스 그룹 동시 진입 버그 보고(open-rmf 이슈)가 있어 실제 동작 신뢰성 미확인
    - f15~f26 근거 논문 원문 미열람(검색 요약·제목 범위)
    - f17 ref-858 저자 미확인
    - f18·f19 성능 수치는 저자 보고
    - f22·f25 는 제목 수준만 확인
    - f14 MiR 충전 마커는 벤더 주장이며 이번에 다시 열지 않음
    - 국내 물류센터 충전·승강기 병목 정량 자료 미확인(oq-010 관련)
    - 시간대별 전기 요금 기반 로봇 충전 계획의 학술 출처 미확보
- 범위 경계 위반 의심:
    - f13·f31: 정밀 도킹·과충전 보호·승강기 안전 제어는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 대상이라 claim 을 '연계 대상: '으로 표시하고 ROP 역할을 요청·상태 확인으로 한정함
    - f20·f23·f24·f26: 컨테이너 터미널·병원·호텔·배송 로봇 사례라 물류센터 직접 적용 근거로는 제한적임
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-031·ref-228·ref-051·ref-105·ref-079·ref-039·ref-104·ref-377·ref-312·ref-286·ref-284·ref-216, 신규 ref-864·ref-865. rmf_reservation README 는 404, task_new.md 에는 충전 내용 없음. 그 밖의 신규 7건(ref-858~ref-863, ref-866)과 재사용 ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321 은 원문 미열람(신뢰도 상한 medium). finding 신뢰도 모두 medium 이하, 교차 확인 0건. 검색 19회/30, 신규 출처 9건/15(ref-858~ref-866, 예약 구간 안), 재사용 19건. 세부영역 반영 제안 4건(트랙 floorplan-recognition 2026-09-25-19 3건, manual-capability-ontology 2026-09-25-23 1건)을 모두 검토해 f1·f3·f5·f9·f13·f14·f21·f32 로 6·7·10절 반영을 제안했다(batteryCharging 필드 이름은 스키마 원문 기준으로 정정). 한국 자료: 박재범 외 2024(ref-863). 한국 물류센터 충전 연구는 검색 2회에서 찾지 못함. 교차 규칙: 학습 기반 충전 결정(f19)은 27. AI·학습·적응과 모델 운영과 이 영역 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성(현재 배터리 상태)과 22. 시뮬레이션·예측용 디지털 트윈(충전 정책 실험)은 섞지 않았다. 정정 요청 없음. oq-016(충전·대기 시간의 OEE 손실 분류)은 관련 근거를 찾지 못해 해결 제안하지 않았다.
