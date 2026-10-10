---
area: 28
title: "28. 공용 자원·충전·에너지 최적화"
researched: 2026-10-10
researcher: "Codex (GPT-6)"
---

# 28. 공용 자원·충전·에너지 최적화 — 보완 조사

## 요약
- VDA 5050 충전 하한의 권고 표현과 Open-RMF 운영 임계값의 단위를 구분한다.
- `is_parking_spot`과 `is_charger` 충돌은 그래프 API와 파서 원문으로 해소한다.
- 승강기 세션 메시지가 제공하는 기능과 배분 알고리즘을 구분한다.
- 호텔 배송 연구와 2026년 배터리 열화 연구의 모델·실험 범위를 원문으로 보강한다.
- 전기 요금 연계 연구는 원문을 열지 못해 후보 근거로만 남기고, Open-RMF 수정 이력은 확정 근거로 추가한다.

## 보완 항목

### 5. 적용 사례 (현장 유형 명시) — 수정
- 대상 문장(수정·교차 확인일 때): "팩트시트의 임계 저충전 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 한다."
- 새 내용: VDA 5050 3.0.0의 `criticalLowChargingLevel`은 충전 상태(State of Charge, SOC)의 백분율로 표현된다. [사실][^n1] 설명은 그 값 이하에서 관제가 충전소로 가는 주문만 보내는 것이 좋다고 `should`로 기술한다. [사실][^n1] 따라서 이를 `shall` 수준의 의무 문구로 옮기거나, 모든 로봇에 공통으로 정해진 충전 시작 비율이라고 설명해서는 안 된다. [의견][^n1]
- 근거 메모: 공식 3.0.0 태그 명세의 factsheet `batteryCharging/criticalLowChargingLevel` 행. 기존 문장의 “해야 한다”를 원문의 권고 강도에 맞춘다. 제조사 선언값 자체는 유지한다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: VDA 5050의 충전 선언값은 백분율이며, Open-RMF 템플릿의 `recharge_threshold: 0.10`과 `recharge_soc: 1.0`은 각각 운행 하한과 충전 목표를 나타내는 비율 예시다. [사실][^n1][^n2] 이 둘을 대조할 때는 단위를 먼저 맞추고, 운행 하한·충전 시작 판단·충전 목표를 별도 정책으로 기록하는 편이 좋다. [의견][^n1][^n2] 어느 값을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 원문에 없었다. [추정][^n1][^n2]
- 근거 메모: VDA factsheet의 네 충전 필드와 Open-RMF config.yaml의 해당 주석. 0.10은 10%에 해당하지만 현장 권장값은 아니다. 두 표준·구현이 서로 값을 자동 동기화한다는 근거는 확인 못 함이다.

### 6. 대표 접근법과 기술 — 수정
- 대상 문장(수정·교차 확인일 때): "한편 Open-RMF 지원 작업 문서는 충전소를 is_parking_spot 으로 설정한다고 적어 is_charger 로 적는 문서와 어긋난다."
- 새 내용: Open-RMF 그래프는 충전 경유점과 주차 경유점을 별도 속성으로 정의한다. [사실][^n3] `rmf_fleet_adapter` 2.14.0 파서는 `is_charger`를 `set_charger(true)`로, `is_parking_spot`을 `set_parking_spot(true)`로 각각 변환한다. [사실][^n4] 따라서 이 구현에서 충전소 표시는 `is_charger`로 확인되며, 주차 속성만 지정한 것을 충전소 지정과 같은 뜻으로 취급하면 안 된다. [의견][^n3][^n4]
- 근거 메모: 6절 분리 페이지의 충돌 문장. Graph.hpp의 `is_charger()/set_charger()`·`is_parking_spot()/set_parking_spot()`와 태그 고정 parse_graph.cpp의 두 YAML 분기를 대조했다. 문서와 코드 사이의 충돌을 구현 판별로 해소한 것이며, 같은 프로젝트 자료 두 개를 독립 출처로 세지 않는다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가
- 새 내용: Open-RMF 승강기 요청(LiftRequest)은 요청 시각, 세션 ID, 요청 모드, 목적층, 문 상태를 담고, 승강기 상태(LiftState)는 현재 제어 세션을 보고한다. [사실][^n5][^n6] 이 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 직접 지정하는 필드가 없다. [사실][^n5][^n6] 따라서 세션 인터페이스가 있다는 사실과 공정한 대기열·묶음 운행 정책이 정의되어 있다는 주장은 구별해야 한다. [의견][^n5][^n6]
- 근거 메모: 두 메시지 전체 필드와 REQUEST_END_SESSION 주석. 세션 종료 전 제어권 유지의 기존 설명을 확인했다. 메시지 정의만 조사한 결론이므로 다른 감독 구성요소에 타임아웃이나 대기열 구현이 전혀 없다는 뜻으로 확대하지 않는다.

### 5. 적용 사례 (현장 유형 명시) — 추가
- 새 내용: 현장 유형은 다층 호텔 배송의 수리·수치 실험이며, Han 외의 2025년 연구는 승강기를 암묵적 경유점으로 다루는 다회 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)를 제시한다. [사실][^n7] 논문은 60개 고객 노드 사례에서 승강기 운행 시간을 40초에서 100초로 바꾸면 총 이동 시간이 약 225초에서 500초로 늘었다고 보고한다. [사실][^n7] 이는 승강기 시간에 대한 모델 민감도이며 실제 물류센터의 대기열 손실을 측정한 값은 아니다. [사실][^n7]
- 근거 메모: 출판 PDF §2 모델, §4 수치 실험, §4.4 Discussion(p.16), §5의 후속 연구. 기존 3절의 근거를 원문으로 확인하고 5절에 비창고 사례로 추가한다. 기존 “거의 두 배” 대신 원 수치를 그대로 적었다. 논문은 동적 수요·동적 승강기 시간·충돌 회피 등을 후속 과제로 남기므로 여러 제조사 승강기 배분의 완성 사례로 쓰지 않는다.

### 8. 대표 연구와 자료 — 추가
- 새 내용: Li 외의 2026년 프리프린트는 작업 배정·순서·충전 방식·공용 충전기 점유를 혼합 정수 선형 계획(Mixed-Integer Linear Programming, MILP)으로 함께 표현한다. [사실][^n8] 목적에는 배터리 열화와 납기 지연 등이 들어가고, 같은 충전기의 충전 구간이 겹치지 않도록 로봇 사이 순서 제약을 둔다. [사실][^n8] 다만 §4.4는 비교표를 예시적 기대 평균으로 설명하므로, 보고된 최대 54% 열화 감소를 현장 배터리 수명 개선의 검증값으로 인용하지 않는 편이 좋다. [의견][^n8]
- 근거 메모: §2.2 목적, §2.5 SOC 제약, §2.6 공용 충전기 용량 제약 식 (33)–(34), §4.1 가상 창고·동종 로봇 설정, §4.4 표 2. 원문에 “illustrative expected averages”라고 적혀 있다. 실물 배터리 노화 실험·공개 재현 데이터는 확인 못 함이다. 현재 페이지의 단순 충전 임계값 설명에 모델링 대안을 보태는 용도다.

### 8. 대표 연구와 자료 — 추가
- 새 내용: Yang 외의 2026년 항만 연구는 무인운반차(Automated Guided Vehicle, AGV)의 작업·충전 계획을 시간대별 전기 요금과 충전소 용량에 결합한 것으로 소개된다. [추정][^n9] 이 자료는 요금 연계 충전 연구의 후보이지만, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 채택하지 않는다. [의견][^n9]
- 근거 메모: 출판사 검색 색인에 노출된 제목·초록·§4·§5.3 설명까지만 확인했다. 출판사 본문 직접 열기와 HTML 내려받기가 실패했다. 본문 열람으로 세지 않았으며 태그도 [추정]으로 제한했다. 항만과 창고의 적용 조건은 다르다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가
- 새 내용: `rmf_fleet_adapter`의 2026년 변경 이력에는 충전 완료 단계 발행 수정, 다음 작업에 필요한 충전량이 부족할 때 충전소로 복귀하는 변경, 뮤텍스(Mutex) 잠금·해제 과정의 잠재적 교착 수정이 기록되어 있다. [사실][^n10] 따라서 충전·상호 배제 기능의 존재뿐 아니라 적용 버전과 수정 포함 여부를 함께 기록해야 한다. [의견][^n10]
- 근거 메모: 2.14.0 태그에 포함된 변경 이력 중 2.12.0(2026-02-23)의 #502·#423, 2.13.0(2026-06-15)의 #490. 2.14.0은 2026-09-26 판이지만 여기 인용한 세 변경은 그보다 앞선 2026년 수정이다. 과거 기능이 모든 조건에서 교착 없이 동작했다는 근거로 사용하지 않는다.

## 답한 열린 질문
- 질문: "출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot 과 is_charger 가운데 어느 속성으로 하는가?" → 구현 기준으로 해소: 2.14.0 파서는 `is_charger`와 `is_parking_spot`을 별도 속성으로 처리하며 충전 경유점에는 `is_charger`를 사용한다. [사실][^n3][^n4]
- 질문: "충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가?" → 부분 답변: 제조사 선언은 백분율, Open-RMF 설정은 비율 예시이며 서로 다른 계약이다. [사실][^n1][^n2] 단위 변환은 필요하지만 어느 값을 우선하는 공통 규칙은 확인 못 했으므로, 양쪽 조건을 함께 검토하는 현장 정책이 필요하다는 수준으로 남긴다. [의견][^n1][^n2]
- 질문: "여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가?" → 부분 답변: 세션 점유·종료 메시지는 공개되어 있지만, 메시지 자체는 최대 점유 시간이나 목적층 묶음 정책을 정의하지 않는다. [사실][^n5][^n6] 해당 배분 알고리즘을 확인한 것으로 질문을 닫지는 않는다. [의견][^n5][^n6]
- 질문: "물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가?" → 후보 자료까지만 확인: 2026년 항만 AGV의 요금 연계 연구가 검색되었지만 원문·물류센터 적용·국내 사례는 확인 못 함이다. [추정][^n9]

## 새로 생긴 열린 질문
- 공용 충전기 예약이 끝났지만 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가?
- SOC 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가?
- 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가?
- 호텔의 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가?

## 출처
집계: 총 10개, 기존 영역·분리 주제 페이지 대비 새 출처 4개(n4·n8·n9·n10), 원문 열람 9/10(90%). 호텔 논문의 출판 PDF 사본은 기존 논문의 재열람으로 셌다. 다른 G 영역에 이미 있던 자료라도 이 영역에 없던 출처는 이 영역의 새 출처로 셌다.

[^n1]: VDA / VDMA, VDA 5050 Version 3.0.0, 2026-03-19, [태그 고정 명세](https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md), 접근일 2026-10-10, 원문 열람.
[^n2]: Open-RMF, fleet_adapter_template/config.yaml, 발행일 미확인, [공식 설정 템플릿](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml), 접근일 2026-10-10, 원문 열람.
[^n3]: Open-RMF, rmf_traffic — Graph.hpp, 발행일 미확인, [공식 그래프 API](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp), 접근일 2026-10-10, 원문 열람.
[^n4]: Open-RMF, rmf_fleet_adapter — parse_graph.cpp, 2026-09-26(2.14.0 패키지판), [태그 고정 파서](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp), 접근일 2026-10-10, 원문 열람.
[^n5]: Open-RMF, LiftRequest.msg, 발행일 미확인, [공식 요청 메시지](https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg), 접근일 2026-10-10, 원문 열람.
[^n6]: Open-RMF, LiftState.msg, 발행일 미확인, [공식 상태 메시지](https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg), 접근일 2026-10-10, 원문 열람.
[^n7]: Linghui Han, Junzhe Ding, Songtao Liu, Meng Meng, The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, [출판사 페이지](https://www.mdpi.com/1424-8220/25/6/1783), [직접 열람한 출판 PDF 사본](https://pdfs.semanticscholar.org/428c/ef353aae52dbdc80767ccbe405597b13c4a4.pdf), 접근일 2026-10-10, 원문 열람(출판 PDF 19쪽; PMC·출판사 HTML 접근 실패 후 PDF 열람).
[^n8]: Jiachen Li, Shihao Li, Jian Chu, Wei Li, Dongmei Chen, Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03-24, [v1 프리프린트 본문](https://arxiv.org/html/2603.22731v1), 접근일 2026-10-10, 원문 열람.
[^n9]: Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang, A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints, 2026-07-27, [출판사 원문 위치](https://www.mdpi.com/2227-9717/14/15/2424), 접근일 2026-10-10, 원문 미열람(출판사 검색 색인의 초록·본문 일부만 확인; 직접 접근 실패).
[^n10]: Open-RMF, rmf_fleet_adapter Changelog — 2.14.0 및 수록 이전 이력, 2026-09-26, [태그 고정 변경 이력](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst), 접근일 2026-10-10, 원문 열람.
