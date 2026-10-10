---
title: "28. 공용 자원·충전·에너지 최적화"
type: area
category: "G. 계획·최적화"
area_no: 28
related_areas: [5, 18, 22, 25, 27, 34, 35, 47]
tags: [충전 상태, 충전 임계값, 뮤텍스 그룹, 승강기 세션, VDA 5050, Open-RMF]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-031, ref-039, ref-051, ref-060, ref-079, ref-098, ref-103, ref-104, ref-105, ref-109, ref-146, ref-216, ref-219, ref-228, ref-284, ref-286, ref-312, ref-321, ref-377, ref-403, ref-530, ref-531, ref-532, ref-533, ref-534, ref-535, ref-536, ref-537, ref-538, ref-1410, ref-1411, ref-1398]
last_run: 2026-10-10
version: 3
---

[홈](../../index.md) › [G. 계획·최적화](index.md) › 28. 공용 자원·충전·에너지 최적화

# 28. 공용 자원·충전·에너지 최적화

!!! info "소속 대분류"
    [G. 계획·최적화](index.md) — 핵심 질문:
    누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-10-10 · 마지막 실행: 2026-10-10
<!-- auto:page-status:end -->

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]

## 3. 왜 중요한가

로봇마다 정해 둔 충전 하한 — VDA 5050 의 임계 충전 수준(criticalLowChargingLevel, 관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율) — 에만 맞춰 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. [추정][^ref-228][^ref-031][^ref-105][^ref-530][^ref-531][^ref-533][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 왜 중요한가](../../topics/2026/2026-10-10-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

앞 절의 문제를 다루려면 배터리 상태와 공용 자원 점유를 표현하는 용어가 먼저 필요하다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area16-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 첫 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 2026-10-10 갱신에서 상업 시설 사례(다층 호텔 배송을 모델링한 수치 실험)를 더했고, 그 밖의 현장 유형 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹 → 출하

**시나리오:** 피킹 성수기에 충전 요청과 층간 출하 운반이 겹칠 때

다음은 설명을 위한 가상의 시나리오이다. 여러 제조사 로봇이 한 다층 물류센터에서 피킹 화물을 다른 층 출하 구역으로 옮기는 중에 충전 수요와 승강기 호출이 몰리는 상황을 가정한다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇이 일련의 작업을 마칠 충전량이 부족하면 Open-RMF 작업 계획기가 충전 작업을 일정에 끼워 넣는다. [사실][^ref-104] 같은 시간대에 피킹을 마친 화물의 층간 운반 요청이 이어진다(가정). |
| 작업 대상 | 피킹을 마친 출하 대상 화물과 이를 실은 로봇이며, 충전기·승강기·대기 위치는 여러 로봇이 나눠 쓰는 공용 자원이다(가정). |
| 수행 자원 | 과충전 보호, 충전기와의 통신·정밀 도킹, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다. [추정][^ref-031][^ref-216][^ref-284] |
| 제약 | VDA 5050 은 팩트시트의 임계 충전 수준(백분율, 로봇 유형별 선언값) 이하에서는 관제가 충전소로 가는 주문만 보내는 것이 좋다고 권고(should)한다(3.0.0 판 기준, 발행일 미확인). [사실][^ref-031][^ref-228] 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 호출을 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다. [추정][^ref-312][^ref-286][^ref-103] |
| 완료·인계 | 로봇 쪽 도킹 프레임워크(연계 대상)는 도킹 뒤 충전 시작 여부(isCharging)를 확인하는 함수를 둔다. [사실][^ref-216] 승강기 이용이 끝나면 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남는다. [사실][^ref-286] |
| 예외·성과 | VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. [사실][^ref-031] 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기면 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대의 기회 충전이나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. [추정][^ref-534][^ref-531][^ref-031] |

이 시나리오에서 이 영역이 관여하는 곳은 시작 조건(충전 작업을 언제 넣을지), 제약(충전 하한과 승강기 점유), 예외·성과(충전으로 빠지는 가용 로봇과 층간 대기)다. 화물의 인계 확인 자체는 다른 영역이 다룬다(가정).

실제 물류센터에서 충전 대기와 승강기 대기가 처리량을 얼마나 줄이는지는 이번 조사에서 확인되지 않았으며, [열린 질문](../../open-questions.md)의 oq-010 으로 남겨 둔다.

**현장 유형:** 상업 시설

**사례:** 다층 호텔에서 승강기를 거쳐 여러 층의 고객에게 배송(다층 호텔 배송을 모델링한 수치 실험이며 실제 배치 아님)

다음은 Han 외(2025)가 다층 호텔 배송을 모델링한 수치 실험을 여섯 항목으로 옮긴 것이며, 실제 현장 배치 사례가 아니다.

| 항목 | 내용 |
|---|---|
| 시작 조건 | 여러 층에 흩어진 고객 노드로 가는 배송 로봇의 경로 계획 문제가 주어지며, 논문은 이를 [다중 운행 차량 경로 문제](../../glossary/multi-trip-vehicle-routing-problem.md)(Multi-Trip Vehicle Routing Problem, MTVRP)로 정식화하고 적응형 대규모 이웃 탐색으로 푼다. [사실][^ref-103] |
| 작업 대상 | 층마다 흩어진 고객 노드와, 경로 안에서 암묵적 경유점으로 모델링한 승강기 노드다. [사실][^ref-103] |
| 수행 자원 | 배송 로봇이 승강기 노드를 거쳐 층을 옮기는 것으로 모델링된다. [사실][^ref-103] 승강기 설비 쪽의 호출·배분 분담은 미확인이다. |
| 제약 | 승강기 운행 시간이 모델의 입력이며, 고객 노드 60개 사례에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다. [사실][^ref-103] |
| 완료·인계 | 미확인 |
| 예외·성과 | 논문은 무작위·동적 승강기 운행 시간, 동적 수요 변동, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링을 후속 연구 과제로 남긴다. [사실][^ref-103] 실패 시 누가 복구하는지는 미확인이다. |

이 사례에서 이 영역이 관여하는 곳은 제약(승강기라는 공용 자원의 운행 시간)과 예외·성과(그에 따른 총 이동 시간)다. 이 위키는 위 수치를 가정한 승강기 운행 시간을 바꾼 모델 민감도로 보며, 실제 승강기 대기열 손실값이나 여러 로봇이 승강기를 나눠 쓰는 배분 규칙의 근거로 쓰지 않는다. [의견][^ref-103]

## 6. 대표 접근법과 기술

Open-RMF 는 충전량이 부족한 로봇의 일정에 충전 작업을 끼워 넣고, 통로 구간은 뮤텍스 그룹으로, 승강기는 세션으로 점유를 제한한다. [사실][^ref-104][^ref-536][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 은 충전을 동작과 배터리 선언·상태 필드로 표현하고, Open-RMF 는 충전 설정·작업 계획기·교통 그래프·승강기 메시지로 공용 자원을 다룬다. [사실][^ref-031][^ref-105] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절은 충전 방식·정책의 처리량·비용 효과를 대기행렬로 분석한 창고 연구, 충전을 작업 배정·순서와 함께 푸는 최적화 연구, 승강기를 층간 병목으로 다룬 배송 로봇 연구로 나누어 정리한다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-10-10-area28-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력인 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 충전 시점·충전 목표 결정, 충전 시작·중지 요청, 배터리 상태 확인과 작업 배정 반영 | 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치 |
| 시설·설비 제어 | 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 승강기 세션 요청과 모드 확인 | 승강기 운행·설비 안전 제어 |

이 직접 범위는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. [추정][^ref-031][^ref-104][^ref-536][^ref-312] 과충전 보호는 VDA 5050 이 이동로봇의 책임으로 명시한다. [사실][^ref-031] 정밀 도킹·충전 확인은 로봇 쪽 프레임워크가, 승강기 동작을 방해하는 요청의 차단은 승강기 어댑터가 맡으므로, ROP 는 요청과 상태 확인까지를 담당하는 연계 구조로 보인다. [추정][^ref-216][^ref-284] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 충전과 공용 자원 점유를 매개로 배정·교통·설비 연동·설비 계획·능력 모델·상태 모델·시뮬레이션·학습 영역과 이어지는 것으로 보인다. [추정][^ref-534][^ref-536][^ref-312]

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area28-s10.md)에 있다.

## 11. 열린 질문

충전·대기 시간을 성과 지표에서 어떻게 분류할지, 물류센터에서 충전·승강기 병목이 얼마나 되는지, 제조사가 다른 로봇이 충전기·승강기를 어떤 규칙으로 나눠 쓸지가 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-10-10-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-10 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 3절 충전 값 의미·단위 구분과 호텔 연구 수치(Han 외 2025) 보강, 5절 제약 행 권고 표현 정정·상업 시설(호텔 수치 실험) 사례 추가, 6·7·8·11절 갱신 요약과 새 주제 페이지·2026-09-25 분리 페이지 링크(문단 안 문장으로 둠), 13절 각주 갱신(ref-031·ref-103 등) (실행 2026-10-10-05)
- 2026-10-10 · 생성 · [충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가](../../topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md) — 신규 작성: 충전 하한 값 구분, 충전소 is_charger 지정(oq-069 해결), 승강기 메시지 범위, Open-RMF 판 기록, 공용 충전기·열화 MILP, 항만 물류–에너지 후보 자료(2차 수정: 세 줄 요약 둘째 줄 범위 조정, 연계 범위 의견 주체 명시) (실행 2026-10-10-05)
- 2026-10-10 · 갱신 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 3. 본문 끝에 충전소 속성 충돌 문장 정정 소제목 추가(문서 is_parking_spot·구현 is_charger 병기, 구현 기준 판단은 의견), 8. 출처에 ref-1410 정의 추가, 10. 이력에 2026-10-10 행 추가, 프런트매터 sources·last_run 갱신 (실행 2026-10-10-05)
- 2026-10-10 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 열린 질문](../../topics/2026/2026-10-10-area28-s11.md) — 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "11. 열린 질문" 절(1,185자)을 옮겼다 (실행 2026-10-10-05)
- 2026-10-10 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 왜 중요한가](../../topics/2026/2026-10-10-area28-s3.md) — 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "3. 왜 중요한가" 절(770자)을 옮겼다 (실행 2026-10-10-05)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-10
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-10
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-10
[^ref-216]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_docking — README (Open Navigation's Nav2 Docking Framework), 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-10
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-10-10
[^ref-530]: Computers & Industrial Engineering 게재 논문(저자 미확인), Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach, 2024-08, https://www.sciencedirect.com/science/article/pii/S0360835224006314, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-534]: Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D., Scheduling heterogeneous multi-load AGVs with battery constraints, 2021-12, https://www.sciencedirect.com/science/article/pii/S0305054821002586, 접근일 2026-09-25 (원문 미열람)
[^ref-536]: Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 미확인, https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp, 접근일 2026-10-10
