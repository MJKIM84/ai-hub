# 리서치 브리프 2026-09-25-50

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-50 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 20. 예외 복구·재계획·업무 연속성 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 운반 중 고장 난 로봇의 화물·남은 주문 처리 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-003, oq-021, oq-038, oq-048 이 이 영역과 관련

## 조사 질문

1. 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문]
2. 로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 고장·통신 단절·작업 취소·일시정지·재계획을 어떤 메시지·기능으로 다루는가? (섹션 6·7 겨냥)
3. 지연·고장이 생겼을 때 다중 로봇 경로와 작업 배정을 실시간으로 재계획하는 연구는 무엇이 있는가? (섹션 6·8 겨냥)
4. 업무 연속성 관리 표준과 국내 제도는 무엇이며 로봇 현장의 제한 운영·수동 전환 계획과 어떻게 연결되는가? (섹션 3·7 겨냥, 한국 자료 우선)
5. 이미 수행한 물리 작업을 취소·되돌릴 때 이벤트 기록과 재고를 어떻게 바로잡는가? (oq-021, oq-003 관련, 섹션 4·6 겨냥)
6. 통신 단절이나 관제 어댑터 재시작 동안 작업을 어디까지 계속하고 재연결 뒤 어떻게 맞추는가? (oq-038, oq-048 관련, 섹션 6·11 겨냥)
7. 예외 복구에서 ROP 직접 범위와 연계 대상(로봇 자체 복구·안전 제어, 상위 WMS)의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세에서 이동로봇은 즉시 동작 cancelOrder 를 받으면 가능한 한 빨리 정지하고, 예정된 동작은 FAILED 로 보고하며, 정지 뒤 cancelOrder 상태를 FINISHED 로 보고하고 유휴 상태가 된다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 MQTT 라스트 윌 메시지로 관제가 로봇의 연결 끊김을 감지하게 하고(connectionState ONLINE·OFFLINE·CONNECTION_BROKEN), 브로커와 연결이 끊긴 로봇은 주문 정보를 유지한 채 마지막으로 해제된(released) 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 최신판 state 스키마는 오류 수준(errorLevel)을 WARNING·URGENT·CRITICAL·FATAL 로, 동작 상태(actionStatus)에 RETRIABLE 을 두며, 명세는 RETRIABLE 상태의 로봇이 관제나 운영자의 개입을 기다린다고 설명한다. | ref-051, ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 state 스키마의 loads 배열은 로봇에 실린 적재물의 식별번호(loadId), 종류, 적재 위치(loadPosition), 치수, 무게를 보고하게 하므로 고장 로봇에 어떤 화물이 실려 있는지 관제가 알 수 있는 근거가 된다. | ref-051 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f5 | [사실] | VDA 5050 의 startPause 즉시 동작은 자동 주행을 멈추고 일시정지 가능한 동작(pauseAllowed=true)만 멈추며, stopPause 로 주문 실행을 재개한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | VDA 5050 은 교착(deadlock) 탐지·해소와 통신 오류 탐지·해소를 관제(fleet control)의 역할로 두고, 구역 충돌 같은 상황에서 사용자 개입이 필요한지, 현재 주문을 취소하고 새 주문을 보낼지를 관제가 결정한다고 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 플릿 어댑터의 RobotUpdateHandle 은 작업 중단(interrupt)과 재개(resume), 작업 취소(cancel_task)·강제 종료(kill_task), 마지막 보고 위치에서의 재계획 요청(replan), 작업 수락 중지(set_commission), 이슈 생성(create_issue) 기능을 제공한다. | ref-570 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [사실] | Open-RMF 의 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자 사이의 협상이 시작되며, 긴급 참여자는 의도적으로 충돌을 게시해 협상을 강제할 수 있다. | ref-004 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 중단하고 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 RMF 에 제어권 없이 상태만 보고한다. | ref-569, ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f10 | [사실] | Open-RMF rmf_ros2 이슈 224 는 플릿 어댑터가 재시작되면 배정된 작업이 유실되는 문제를 제기하고, 작업 로그·백업을 SQLite 로 저장하는 PR 161 과 rmf-web 영속 데이터베이스를 조회하는 대안을 제안하지만, 배포판 반영 여부는 이번에 확인되지 않았다. | ref-582 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f11 | [사실] | Hönig 외(IEEE RA-L, 2019)는 MAPF 계획을 후처리해 로봇 간 순서와 운동 제약을 행동 의존 그래프(ADG)로 인코딩함으로써 예기치 않은 감속·장애물·지연에도 계획을 충돌 없이 실행하고 재계획과 실행을 겹치게 하는 창고용 실행 틀을 제시한다. | ref-571 | 아니오 | medium | 2019-04 | 예외·성과 | 원문 미열람 |
| f12 | [사실] | Feng 외(ICAPS 2024)는 실행 중 로봇이 지연될 때 경로는 유지하고 통과 순서만 다시 정하는 전환 가능 간선 탐색(Switchable-Edge Search, SES)을 제안하며, 최선 변형이 중소 규모 문제에서 1초 미만, 대규모 문제에서 기준선보다 최대 4배 빠르다고 보고한다. | ref-572 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Kalempa 외(Sensors, 2021)의 MRPF 는 작업 간 의존성, 우선순위 기반 선점(preemption) 스케줄링, 고장 복구를 함께 다루는 다중 로봇 작업 배정 방법이며, 소규모 창고 물류 실험 환경(ARENA)에서 평가되었다. | ref-573 | 아니오 | medium | 2021-09-30 | 수행 자원 | 원문 미열람 |
| f14 | [사실] | 창고 로봇 경로 계획용 다중 에이전트 롤아웃·재배열(multiagent rollout with reshuffling) 방법은 온라인 재계획으로 환경 변화에 적응하며, 일부 로봇이 고장 나는 예제로 이를 보여 준다. | ref-574 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | ISO 22301:2019(Security and resilience — Business continuity management systems — Requirements)는 교란 사건으로부터 보호하고 발생 가능성을 줄이며 복구를 보장하기 위한 업무연속성 관리 시스템(BCMS)의 수립·운영·점검·개선 요구사항을 정한다. | ref-575 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f16 | [사실] | 국내에서는 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」에 따라 행정안전부가 기업재난관리표준을 고시하고, 재해경감활동관리체계를 갖춘 기업을 문서평가·현장평가를 거쳐 재해경감 우수기업으로 인증한다. | ref-576 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [사실] | 고용노동부는 2022년 오미크론 확산기에 '중소규모 사업장 기능연속성계획(BCP) 수립 가이드'를 안내했으며, 가이드는 사업 우선순위 파악부터 위험성 분석, 피해 최소화 조치, 분야별 대응, 계획 수립·시행, 공유, 점검까지 7단계로 구성된다. | ref-577 | 아니오 | medium | 2022-03 | — | 원문 미열람 |
| f18 | [사실] | Microsoft 아키텍처 센터의 보상 트랜잭션 패턴은 실패한 여러 단계 작업에서 완료된 단계의 효과를 되돌리되 원래 상태를 그대로 복원하는 것이 아니라 업무 규칙에 맞춰 보정하며, 보상 자체가 실패할 수 있으므로 단계를 멱등 명령으로 정의하고 진행 상황을 기록해 실패 지점부터 재개하고, 영향이 큰 결정에는 사람을 참여시키라고 권한다. | ref-578 | 아니오 | medium | 2026-04-16 | 예외·성과 | — |
| f19 | [추정] | Element Logic 은 AutoStore 의 XHandler 소프트웨어 모듈이 고장 난 로봇을 넘겨받아 시스템을 멈추지 않고 오류를 처리하며, 자동 처리가 불가능하거나 로봇 충돌 위험이 있을 때만 시스템이 정지한다고 설명한다. | ref-579 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | Swisslog 은 AutoStore 그리드에서 로봇이 멈추면 자사 SynQ 소프트웨어가 멈춘 로봇 아래 보관함의 재고를 다른 보관함으로 재할당해, 멈춘 로봇을 정기 휴식이나 저수요 시간에 꺼낼 때까지 주문 처리를 계속한다고 설명한다. | ref-580 | 아니오 | low | 2025-07 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f21 | [사실] | GS1 EPCIS 저장소는 기존 이벤트를 수정·삭제하지 않는 일지(journal) 방식이며, 잘못 기록된 이벤트는 같은 eventID 에 오류 선언(errorDeclaration: 선언 시각, 사유, 정정 이벤트 id 목록)을 붙인 이벤트로 정정한다. | ref-581 | 아니오 | medium | 2016-09-29 | 완료·인계 | 원문 미열람 |
| f22 | [추정] | f1~f4·f13·f18·f21 을 종합하면 운반 중 고장 로봇의 화물과 남은 주문 처리는 고장·연결 끊김 감지(오류·연결 상태), 주문 일시정지·취소, 실린 화물 식별(loads), 남은 작업의 재배정, 화물의 물리적 회수, 재고·이벤트 기록의 보상·정정으로 이어지는 결정 흐름으로 볼 수 있을 것으로 보인다. | ref-031, ref-051, ref-573, ref-578, ref-581 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f23 | [추정] | 연계 대상: 장애물 회피·재위치 추정·비상정지 회로 같은 로봇 자체 복구·안전 제어는 제조사 몫이고, VDA 5050·Open-RMF 가 관제에 주는 기능(주문 취소·일시정지·재계획 요청·작업 수락 중지·이슈 보고)을 보면 이종 로봇을 연결하는 ROP 는 주문 취소·재배정·수동 전환 결정과 기록 정정을 맡는 경계가 될 것으로 보인다. | ref-031, ref-570 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | VDA 5050 에서 연결이 끊긴 로봇이 마지막 해제 노드까지만 주행한다는 규칙(f2)을 보면, 관제가 한 번에 해제하는 주문 범위(base)의 길이가 통신 단절 동안 현장 작업이 얼마나 계속되는지를 정하는 설계 변수가 될 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |

### 근거 발췌

- **f1**: "After receiving the instantAction cancelOrder, the mobile robot shall attempt to stop as soon as possible." 명세는 취소 시 적재물 처리는 따로 정하지 않는다(VDA5050_EN.md main, 3.0.0).
- **f2**: 연결 시 last will 토픽·메시지를 설정해 끊김 시 브로커가 게시하고, 끊긴 로봇은 주문을 last released node 까지 수행한다고 적는다(VDA5050_EN.md main, 3.0.0).
- **f3**: state.schema 의 errorLevel 열거값 4개와 actionStatus 의 RETRIABLE. 명세: 실패한 집기 등 RETRIABLE 상태에서 로봇은 fleet control 또는 operator 의 개입을 기다린다.
- **f4**: loads: loadId "Unique identification number of the load", loadType, loadPosition, loadDimensions, weight(kg).
- **f5**: startPause: 자동 주행 중지, pauseAllowed 동작만 일시정지하고 다른 동작은 계속, stopPause 뒤 재개. state 의 paused 값으로 확인.
- **f6**: 관제 역할 목록에 blockages(deadlocks)와 communication errors 의 탐지·해소가 있고, 관제가 user interaction 필요 여부 또는 cancel 후 new order 를 결정한다.
- **f7**: replan(): "Tell the RMF schedule that the robot needs a new plan." 새 계획은 update_position() 으로 준 마지막 위치에서 시작한다(rmf_ros2 main 헤더 주석).
- **f8**: 스케줄은 "a living database"로 지연·취소·경로 변경을 반영하고, 충돌 시 conflict notice 후 협상과 제3자 판정으로 선택한다(rmf-core.md).
- **f9**: Full Control: path can be interrupted at any time and replaced; Traffic Light: pause/resume 만; Read Only: RMF 에 제어권 없음, 한 공간에 하나만(rmf-core.md, integration_fleets.md).
- **f10**: 재시작 뒤 assigned tasks 가 lost 되며, 작업은 어댑터 내부 큐에만 저장된다고 적는다. 반영 여부 미확인(oq-048 관련, 발행일 미확인, 확인일 기준)
- **f11**: ADG 로 순서·운동 제약을 인코딩해 unforeseen delays 에도 실행하며, overlap of re-planning and execution 을 가능하게 한다(검색 요약 기준).
- **f12**: delayed agents 에 대해 passing order 를 재스케줄하는 A* 계열 SES, 최적성 증명, 소·중 규모 1초 미만·대규모 최대 4배 빠름(ICAPS 34(1) 201–209, 검색 요약 기준).
- **f13**: priority policies on preemptive task scheduling, dependencies between tasks, tolerates faults; small-scale warehouse logistics(ARENA)에서 평가(검색 요약 기준).
- **f14**: generic rollout 의 online replanning 능력을 물려받아 some robots malfunction 예제로 시연(arXiv 2211.08201 v2, IFAC, 검색 요약 기준).
- **f15**: BCMS 를 plan, establish, implement, operate, monitor, review, maintain, continually improve 하여 disruptive incidents 에 대비·복구(검색 요약 기준, 유료 원문 미열람).
- **f16**: 기업재난관리표준(행정안전부 고시)에 따라 재해경감활동계획을 수립·이행하고 인증대행기관의 1차 문서평가, 2차 현장평가 후 인증 신청(검색 요약 기준, 발행일 미확인, 확인일 기준)
- **f17**: ① 사업의 우선순위 파악 ② 위험성 분석 ③ 피해 최소화 조치 ④ 분야별 대응 ⑤ 수립·시행 ⑥ 공유 ⑦ 점검(검색 요약 기준).
- **f18**: "define each step as an idempotent command"; 진행 기록 후 실패 지점부터 재개, 자동화가 어려운 고영향 결정은 사람 포함(compensating-transaction.md, 2026-04-16).
- **f19**: 벤더 주장: XHandler 가 failed robot 을 넘겨받아 시스템 정지 없이 복구 시도, 자동 처리 불가·충돌 위험 시에만 정지(FAQ 검색 요약 기준, 발행일 미확인, 확인일 기준)
- **f20**: 벤더 주장: SynQ 가 stalled robot 아래 재고를 다른 bin 으로 re-allocate 하고 로봇 제거 전까지 주문 처리 지속(블로그 검색 요약 기준).
- **f21**: no mechanism for modification or deletion; 정정 시 원 eventID 와 같은 near-duplicate 이벤트가 ErrorDeclaration 과 correctiveEventIDs 를 가리킨다(EPCIS 1.2, 검색 요약 기준).
- **f22**: 개별 출처는 각 단계의 메커니즘만 다루며, 이 흐름을 한 절차로 정한 출처는 이번 조사에서 찾지 못했다(종합 추정).
- **f23**: VDA 5050 은 로봇이 오류를 보고하고 관제가 취소·새 주문·사용자 개입을 결정하는 구조이고, RobotUpdateHandle 은 interrupt·replan·set_commission 을 관제 쪽에 준다(경계 추정).
- **f24**: 끊긴 로봇은 order 를 last released node 까지 수행하고, newBaseRequest 가 없으면 속도를 줄인다(state.schema 설명과 명세의 종합, oq-038 관련 추정).

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-569 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-570 | Open Robotics (open-rmf/rmf_ros2) | rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 아니오 |
| ref-571 | Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N. | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019-04 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-572 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.18145 | 예 |
| ref-573 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 2021-09-30 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/1424-8220/21/19/6536 | 예 |
| ref-574 | KTH 연구진 (arXiv:2211.08201) | Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning | 2023 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2211.08201 | 예 |
| ref-575 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/75106.html | 예 |
| ref-576 | 행정안전부 | 재해경감 우수기업 인증제도 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do | 예 |
| ref-577 | 고용노동부 | 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내 | 2022-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591 | 예 |
| ref-578 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 2026-04-16 | 오픈소스 문서 | medium | 2026-09-25 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction | 아니오 |
| ref-579 | Element Logic | FAQ - Element Logic (AutoStore) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.elementlogic.net/solutions-and-services/autostore/faq/ | 예 |
| ref-580 | Swisslog | The benefits of using AutoStore for high-throughput retail fulfillment | 2025-07 | 벤더 문서 | low | 2026-09-25 | https://www.swisslog.com/en-us/case-studies-and-resources/blog/2025/07/benefits-of-autostore-htp | 예 |
| ref-581 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 예 |
| ref-582 | Open Robotics (open-rmf/rmf_ros2) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/issues/224 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 최신판(3.0.0) 명세 원문. cancelOrder·startPause·연결 끊김·오류 처리와 관제 역할을 규정한다.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마. errorLevel, actionStatus, loads, paused, newBaseRequest 필드를 정의한다.
- **ref-004**: 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
- **ref-569**: Open-RMF 플릿 어댑터 연동 수준(Full Control, Easy Full Control, Traffic Light)과 경로 중단·교체 방식을 설명하는 장.
- **ref-570**: 플릿 어댑터의 로봇 갱신 핸들 API 헤더. interrupt·resume·cancel_task·kill_task·replan·set_commission·create_issue·responsive wait 등의 문서 주석을 담는다.
- **ref-571**: 원문 미열람. 행동 의존 그래프로 창고 MAPF 계획을 지연·감속에 강건하게 실행하고 재계획과 실행을 겹치게 하는 틀(IEEE RA-L).
- **ref-572**: 원문 미열람. 실행 중 지연된 로봇의 통과 순서를 전환 가능 간선 탐색(SES)으로 실시간 재스케줄하는 알고리즘(ICAPS 2024).
- **ref-573**: 원문 미열람. 우선순위 선점 스케줄링·작업 의존성·고장 복구를 결합한 다중 로봇 작업 배정 방법 MRPF(Sensors 21(19)).
- **ref-574**: 원문 미열람. 창고 로봇 경로 계획용 다중 에이전트 롤아웃 방법으로, 온라인 재계획으로 로봇 고장에 적응하는 예제를 보인다(IFAC 게재, 프리프린트).
- **ref-575**: 원문 미열람. 업무연속성 관리 시스템(BCMS)의 요구사항 국제표준. 유료 원문은 열지 못하고 발행 기관 소개 페이지 검색 결과로 확인.
- **ref-576**: 원문 미열람. 재해경감을 위한 기업의 자율활동 지원에 관한 법률에 따른 기업재난관리표준과 재해경감 우수기업 인증 절차 안내.
- **ref-577**: 원문 미열람. 오미크론 확산기 사회 필수 기능 유지를 위한 중소규모 사업장 BCP 수립 7단계 가이드 안내.
- **ref-578**: 여러 단계 작업이 실패할 때 완료된 단계를 되돌리는 보상 트랜잭션 패턴 설명. 멱등 단계, 진행 기록, 사람 개입을 권한다.
- **ref-579**: 원문 미열람. AutoStore 통합 업체의 FAQ. 로봇 고장 시 XHandler 모듈의 처리와 시스템 지속 운영을 설명한다.
- **ref-580**: 원문 미열람. Swisslog 블로그. 멈춘 로봇 아래 재고를 SynQ 가 재할당해 주문 처리를 계속한다고 설명한다.
- **ref-581**: 원문 미열람. EPCIS 1.2 표준. 저장소를 일지 방식으로 두고 오류 선언(errorDeclaration)으로 이벤트를 정정하는 방법을 정한다.
- **ref-582**: 원문 미열람. 플릿 어댑터 재시작 시 작업 유실 문제와 SQLite 백업(PR 161)·rmf-web 영속 DB 조회 제안을 다룬 이슈.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f19·f20(벤더 주장 병기, 고장 로봇 하나가 전체를 멈추지 않게 하는 설계), f15·f17(업무 연속성) / 4절 용어: f1(cancelOrder), f2(연결 상태), f3(오류 수준·RETRIABLE), f18(보상 트랜잭션), f21(오류 선언), f11(ADG, 기존 용어 재사용) / 5절 시나리오: 피킹 단계 운반 중 고장 f22(시작 조건·작업 대상 f4·수행 자원 f13·완료·인계 f21·예외·성과 f1·f19·f20), 통신 단절 f2·f24 / 6절 접근법: 관제 인터페이스의 중단·취소·재계획 f1~f10, 실행 중 재계획 f11·f12·f14, 고장 허용 재배정 f13, 보상·정정 f18·f21 / 7절 표준·오픈소스: VDA 5050(f1~f6), Open-RMF(f7~f10), ISO 22301(f15), 국내 제도(f16·f17), EPCIS(f21) / 8절 연구: f11~f14 / 9절 범위: f23(로봇 자체 복구·안전 제어는 연계 대상) / 10절 연결: 12. 명령·작업 실행의 신뢰성(f1·f2·f10), 13. 작업 배정 — MRTA(f13), 15. 다중 로봇 경로·교통 관리 — MAPF(f8·f11·f12·f14), 19. 모니터링·이상 탐지·원인 분석(f3·f7 이슈 보고), 18. 사람–로봇 협업·운영 인터페이스(f5·f18 사람 개입), 7. 화물·재고·자산 식별과 추적(f4·f21, oq-003), 1. 주문·업무 시스템 연계(f18, oq-021), 11. 분산 시스템·통신·컴퓨팅 구조(f2·f24, oq-038), 22. 시뮬레이션·예측용 디지털 트윈(제한 운영 처리량 추정 질문) / 11절 열린 질문: oq-003·oq-021·oq-038·oq-048(f10 은 부분 근거일 뿐 해결 아님)과 새 질문 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 보상 트랜잭션 | Compensating Transaction | 여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다. |
| 업무연속성 관리 시스템 | Business Continuity Management System (BCMS) | 교란 사건에 대비하고 핵심 업무를 지속·복구하기 위한 조직의 관리 체계로, ISO 22301 이 요구사항을 정한다. |
| 주문 취소 즉시 동작 | cancelOrder (VDA 5050 instant action) | VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다. |

## 열린 질문

새로 생긴 질문:

- 운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 7. 화물·재고·자산 식별과 추적 | 근거: f22 | 종류: 일반
- 국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f16 | 종류: 일반
- 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? | 관련 영역: 20. 예외 복구·재계획·업무 연속성, 22. 시뮬레이션·예측용 디지털 트윈 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 14건
- 미확인 항목:
    - f3: 명세 본문 요약은 오류 수준을 WARNING·CRITICAL 위주로 설명하고 state 스키마는 네 값을 두어, 본문 문구와 스키마를 글자 단위로 대조하지 못함
    - f10: PR 161(SQLite 작업 백업)이 현재 배포판에 반영됐는지 미확인 — oq-048 해결 제안하지 않음
    - f11~f17·f21: 원문 미열람, 검색 요약 기준
    - ISO 22301 의 업무 영향 분석·목표 복구 시간(RTO) 요구는 제3자 해설에서만 확인되어 finding 으로 내지 않음
    - KS A ISO 22301 부합화 연도는 출처를 특정하지 못해 finding 으로 내지 않음
    - ref-574 저자 이름 미확인(KTH 연구진으로 표기)
    - f19·f20 벤더 주장, 독립 확인 없음
    - 모든 finding 교차 확인 없음
- 범위 경계 위반 의심:
    - f23: 장애물 회피·재위치 추정·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 취소·재배정·기록 정정만 맡는다고 구분
    - f16·f17: 기업 BCP 체계 전반은 전사 관리 영역이라 ROP 직접 범위가 아니며 현장 로봇 운영 계획의 참조 틀로만 제안
- 한계: 재실행(스키마 불일치) 1회차. 반려 사유 1·2(f19·f20 이 벤더 문서만 근거로 한 [사실]이고 vendor_claim 표시 없음): 직전 research.json 이 이번 입력에 포함되지 않아 형식만 고칠 원본이 없었으므로, 같은 대상에 대해 예산 안에서 브리프 전체를 다시 작성했다. 벤더 문서만 근거로 한 f19(Element Logic·AutoStore XHandler)·f20(Swisslog SynQ 재고 재할당)은 vendor_claim: true, 태그 추정, 신뢰도 low, evidence_excerpt 첫머리 '벤더 주장: '으로 냈다(관련 finding: f19, f20). 직전 브리프와 finding 번호·내용이 다를 수 있다. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031·ref-051(VDA 5050)·ref-004(rmf-core), 신규 ref-569(integration_fleets)·ref-570(RobotUpdateHandle.hpp)·ref-578(보상 트랜잭션 패턴). 그 밖의 신규 출처는 원문 미열람(신뢰도 상한 medium). web_fetch_available: false 에 따라 재사용 출처의 신뢰도도 medium 으로 적었다. 검색 20회/30, 신규 출처 14건/15(ref-569~ref-582, 예약 구간 안). 한국 자료: 행정안전부 재해경감 인증(f16), 고용노동부 BCP 가이드(f17). 국내 물류센터의 로봇 장애 수동 전환 사례는 한국어 검색 3회에서 찾지 못함(열린 질문으로 올림). 입력의 참고문헌 목록은 요약본(0건 표시)이라 기존 id 는 이전 브리프에 나온 ref-031·ref-051 과 공통 규칙의 ref-004 만 재사용했다 — 같은 URL 이 이미 있으면 퍼블리셔가 합쳐야 한다. 기존 열린 질문 oq-003·oq-021·oq-038·oq-048 은 관련 근거(f21·f18·f2·f24·f10)만 내고 해결 제안하지 않음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 열린 질문 1건으로만 연결했고 섞지 않았다. 정정 요청 없음.
