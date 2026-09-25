# 스토리텔러 산출 2026-09-25-40

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | draft | 섹션 3~11 신규 작성(트랙 반영 제안 4건을 6·7·10절에 반영, 1차 수정 지시 13건 이행), 상태 자동 영역 마커 추가 |
| create | docs/topics/2026/2026-09-25-area16-s6.md | draft | 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절(1,873자)을 옮겼다(형식 수정: 27. AI·학습·적응과 모델 운영 링크 경로를 ../../categories/ 기준으로 고침) |
| create | docs/topics/2026/2026-09-25-area16-s8.md | draft | 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절(1,578자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area16-s7.md | draft | 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,278자)을 옮겼다(형식 수정: 아직 페이지가 없는 ref-864·ref-866 참고문헌 링크를 id 표기로 바꿈) |
| create | docs/topics/2026/2026-09-25-area16-s11.md | draft | 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "11. 열린 질문" 절(1,189자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area16-s4.md | draft | 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "4. 핵심 개념과 용어" 절(988자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 16. 공용 자원·충전·에너지 최적화 | 영역 심화: 3~11절 신규 작성, 트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행 | run 2026-09-25-40
- 홈 최근 업데이트: 2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 영역 심화로 3~11절 신규 작성(충전 임계값·충전 작업 삽입·뮤텍스 그룹·승강기 세션, 충전 정책 연구, 트랙 반영 제안 4건 반영)
- 대분류 최근 업데이트: 2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 영역 심화로 3~11절 신규 작성, 새 열린 질문 5건
- 세부영역 최근 업데이트: 2026-09-25 — 16. 공용 자원·충전·에너지 최적화: 3~11절 신규 작성(VDA 5050 충전 동작·batteryCharging, Open-RMF 충전 작업 삽입·뮤텍스 그룹·승강기 세션, 충전 정책 연구), 트랙 반영 제안 4건 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 충전 상태 | State of Charge (SOC) | 배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다. | 16, 8, 9 | ref-051, ref-865 |
| new | 뮤텍스 그룹 | Mutex Group (Open-RMF) | Open-RMF 교통 그래프에서 같은 그룹에 묶인 경유점·차선을 한 번에 한 로봇만 점유하도록 하는 상호 배제 단위이다. | 16, 15 | ref-864 |
| new | 승강기 세션 | Lift Session (Open-RMF) | Open-RMF 에서 한 요청자가 세션 id 로 승강기 제어권을 받아 세션 종료 요청을 보낼 때까지 점유하는 단위이다. | 16, 10 | ref-312, ref-286 |
| new | 배터리 교환 | Battery Swapping | 방전된 로봇 배터리를 충전기에 꽂아 기다리는 대신 충전된 배터리로 바꿔 끼워 로봇을 곧바로 다시 운행하게 하는 충전 방식이다. | 16, 3 | ref-098 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_types.html |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://doi.org/10.1177/20552076261437181 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md |
| ref-219 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 벤더 문서 | low | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_lifts.html |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 논문 | medium | https://doi.org/10.3390/electronics14050982 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-858 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S0360835224006314 |
| ref-859 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 논문 | medium | https://arxiv.org/abs/2607.05683 |
| ref-860 | Ma, N., Zhou, C., & Stephen, A. | Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X |
| ref-861 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 |
| ref-862 | Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D. | Scheduling heterogeneous multi-load AGVs with battery constraints | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S0305054821002586 |
| ref-863 | 박재범, 조성준, 김준식, 유범재(전자공학회논문지 61(8)) | 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904 |
| ref-864 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp |
| ref-865 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp |
| ref-866 | Open Robotics (open-rmf) | rmf_reservation — Experimental reservation library in rust (GitHub) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_reservation |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? | 16, 28 | 열림 | — |
| new | — | 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? | 16, 4 | 열림 | — |
| new | — | 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? | 16, 10 | 열림 | — |
| new | — | 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? | 16, 5 | 열림 | — |
| new | — | 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? | 16, 6 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 피킹 | 작업 대상 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 피킹 | 수행 자원 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 피킹 | 제약 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 피킹 | 완료·인계 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 피킹 | 예외·성과 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 시작 조건 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 작업 대상 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 수행 자원 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 제약 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 완료·인계 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |
| 출하 | 예외·성과 | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 16. 공용 자원·충전·에너지 최적화 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) | 오픈소스 | Open Robotics (open-rmf) | 16, 15 | ref-864 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp |
| Open-RMF rmf_reservation (실험적 예약 라이브러리) | 오픈소스 | Open Robotics (open-rmf) | 16 | ref-866 | https://github.com/open-rmf/rmf_reservation |

## 추가 조사 요청

- 11절 oq-016: 이동로봇 플릿의 충전·대기·교통 정체 시간을 OEE 손실로 분류한 정의나 사례가 필요하다 — 이번 브리프에 근거가 없어 해결하지 못했다.
- 3·5절: 국내 물류센터의 충전 대기·승강기 대기가 처리량에 주는 영향을 정량화한 자료가 필요하다 — 현재 근거는 병원·호텔·항만·배송 로봇 사례뿐이다(oq-010).
- 6·7절: rmf_reservation README 원문과 배포판 포함 여부 확인이 필요하다 — 원문 미열람(404)이라 실험적 라이브러리로만 적었다.
- 6절: 뮤텍스 그룹의 실제 동작 신뢰성(동시 진입 문제 보고)의 출처 확인이 필요하다 — 브리프에 출처가 없어 '실제 동작 검증은 미확인'으로만 적었다.
- 8절: ref-858 저자, ref-146·ref-321 의 결과 수치, 논문 원문 대조가 필요하다 — 모두 검색 요약·제목 수준이다.
- 11절: 시간대별 전기 요금·최대 수요 전력 기반 로봇 충전 계획의 학술·국내 출처가 필요하다.
- 4·6절: 배터리 교환 방식을 쓰는 국내 물류 로봇 사례가 있으면 현장 시나리오 보강에 필요하다.

## 이행한 수정 지시

- 원문 미열람 표시 — ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321·ref-858·ref-859·ref-860·ref-861·ref-862·ref-863·ref-866 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-039 는 브리프가 github_raw 로 열었다고 기록했고 지시가 제외를 허용하므로 표시하지 않았다.
- f7 is_parking_spot 충돌 — 6절 '충전소 위치 정보의 출처'에 ref-039(is_parking_spot)와 ref-079·ref-104(is_charger)를 모두 [사실]로 제시하고, 11절과 open_question_updates 에 '출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot 과 is_charger 가운데 어느 속성으로 하는가?'(관련 영역 16·6)를 올렸다.
- f10 — 동시 진입 버그 보고는 쓰지 않고 6절 뮤텍스 그룹 문장에 '실제 동작 검증은 미확인'만 적었다.
- f2 — 7절 VDA 5050 관제 기능 행에 '충전 순서·시점 결정 방법은 명세에서 확인되지 않는다'로 적고 명세 문구처럼 쓰지 않았다.
- f6 — 4절과 6절·7절에서 0.10·1.0·5.0 A 등 수치를 템플릿 예시값이며 운영 권장값이 아니라고 밝혔다.
- f12 — 6·7절에 '실험적 라이브러리'와 '배포판 포함 여부는 미확인'을 함께 적고 ref-866 각주에 원문 미열람을 표시했다.
- f15~f26 — 연구 결과 문장을 '보고했다'·'저자 보고' 형식으로 쓰고, f19 에 프리프린트, f20(항만)·f23(병원)·f24(호텔)·f26(배송 로봇)에 물류센터 적용 미확인을 병기했다(3·6·8절).
- ref-103 — 각주 발행일을 2025-03 으로 쓰고 reference_updates 의 published 도 2025-03 으로 고쳤다.
- ref-863 — 각주 기관 표기에 '전자공학회논문지 61(8)'을 넣고 reference_updates 의 org·summary 에도 반영했다.
- 새 열린 질문 2번(전기 요금·최대 수요 전력) — 근거를 f2 로 바꿔 11절에서 ref-031(관제의 에너지 관리) 각주를 달았다.
- f14 — 6절에서 [추정] 벤더 주장 병기를 유지하고 ref-219 각주 제목에 제조사 공식 사이트가 아닌 게재본임을 남겼다.
- f19·f18 — 10절에서 f19 를 27. AI·학습·적응과 모델 운영 연결에, f18 을 13. 작업 배정 — MRTA 연결에 쓰고, 6절에도 27. AI·학습·적응과 모델 운영 링크를 두었다.
- 트랙 반영 제안 4건 — 6절(충전소 위치 정보 출처: ref-079·ref-216·ref-219), 7절(VDA 5050 startCharging·stopCharging·구역 유형 ref-031, batteryCharging ref-228, Nav2 도킹 ref-216), 10절(Stark 외 2024 ref-109 → 3. 처리능력·거점·설비 계획)에 반영했고, 트랙 실행 2026-09-25-19 f19 의 [추정] 대신 이번 f32 를 썼다.
- 분량 초과 자동 분리: 16. 공용 자원·충전·에너지 최적화 본문 9,913자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,779자
