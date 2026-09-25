---
title: "F. 도입·검증·유지관리"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
---

[홈](../../index.md) › F. 도입·검증·유지관리

# F. 도입·검증·유지관리

## 핵심 질문

새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

## 개요

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? | [21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md) | published |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? | [22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) | published |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? | [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) | published |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? | [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8] [분류원문]

## 다른 대분류와의 연결

이 절은 게시된 세부영역 페이지와 다른 대분류 페이지의 검증된 근거로, 이 대분류의 네 세부영역이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지를 정리한다. 이번 정리의 연결 근거는 모두 단일 출처이거나 같은 발행 주체(VDA 명세와 스키마)의 출처이며, 교차 확인된 것은 없다.

### A. 업무·공급망 설계

[A. 업무·공급망 설계](../a-business-supply-chain-design/index.md)와는 처리능력·성과 결정을 시뮬레이션으로 실험하고, 도입 기간과 공정 모델 점검으로 이어진다.

- **[22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) ↔ [3. 처리능력·거점·설비 계획](../a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)·[4. 성과·경제성·프로세스 개선](../a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)**: RAWSim-O 는 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS) 운영의 여러 결정 문제가 미치는 효과를 연구하는 이산 사건 시뮬레이션 프레임워크다(확인일 2026-09-25). [사실][^ref-101] Merschformann 외(2019)가 보고한 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다(모델·시뮬레이션 조건에서의 저자 보고). [사실][^ref-398]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md)**: 연계 대상: 성수기 시나리오 입력(주문·물동량 전망)은 1. 주문·업무 시스템 연계를 거쳐 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 수요예측 자체는 분류 원문 9장의 상위 업무 시스템 경계에 속한다. [추정][^ref-521]
- **[21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md) ↔ 3. 처리능력·거점·설비 계획**: 다중 AGV 도입이 정밀 지도 작성·좌표 지정·수작업 경로망 설계로 오래 걸린다는 연구(2017)와, 설치 기간을 6개월에서 2개월로 줄일 수 있다는 과제 측 보고(비교 조건 미확인)가 있어, 온보딩 기간이 증차한 로봇이 처리능력으로 바뀌는 시점을 좌우하는 것으로 보인다. [추정][^ref-217][^ref-265]
- **[23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) ↔ [2. 공정·워크플로 모델링](../a-business-supply-chain-design/02-process-and-workflow-modeling.md)**: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있어 공정 모델의 형식적 점검이 형식 검증과 이어질 것으로 보이나, 물류 로봇 공정 적용 사례는 확인되지 않았다. [추정][^ref-121]

같은 연결의 반대편은 [A. 업무·공급망 설계 페이지의 다른 대분류와의 연결](../a-business-supply-chain-design/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### B. 공통 정보·환경 모델

[B. 공통 정보·환경 모델](../b-common-information-and-environment-model/index.md)과는 등록·설정 때 넘어가는 능력·지도 정보, 버전 관리, 현재 상태와 가정한 미래의 구분으로 이어진다.

- **21. 온보딩·설정·현장 시운전 ↔ [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)**: IDTA 02020 능력 기술(Capability Description) 서브모델 README 는 능력을 속성·제약(전제조건·순서)·스킬로 구조화해 공정이 요구하는 능력과 자원이 제공하는 능력을 비교하고, 자원 매칭·계획·오케스트레이션을 지원한다고 설명한다(확인일 2026-09-25). [추정][^ref-229] Vieira da Silva 외(2024-06)는 자연어 능력 설명에서 대규모 언어 모델(Large Language Model, LLM)을 이용해 능력 온톨로지를 생성하는 방법을 제안했다. [사실][^ref-465]
- **21. 온보딩·설정·현장 시운전 ↔ [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md)**: Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 RMF 좌표계 사이 변환을 위한 기준 좌표(대응 경유점)를 설정에 두고, 대응 경유점을 최소 4개 둘 것을 권한다(확인일 2026-09-25). [사실][^ref-153] Open-RMF traffic-editor 는 차선·경유점·충전소·주차 지점·문·승강기·층과 기준점(fiducial)을 이용한 층간 정렬을 주석하게 하고, 주석한 그래프는 building_map_generator 로 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- **[24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) ↔ 6. 지도·공간·위치 모델**: VDA 5050 3.0.0 은 지도 내려받기·활성화·삭제 즉시 동작(downloadMap·enableMap·deleteMap)을 두고, 같은 mapId 에 대해 "only be one version of maps with the same mapId enabled at a time" 라고 정한다. [사실][^ref-031] 상태 스키마는 로봇이 mapId·mapVersion·mapStatus(ENABLED·DISABLED)를 보고하게 한다(확인일 2026-09-25). [사실][^ref-051] 분류 원문이 6. 지도·공간·위치 모델에 '지도 버전 관리'를, 24. 자산·소프트웨어 수명주기 관리의 정의에 '지도 버전'을 함께 넣고 VDA 5050 이 지도 배포·활성화를 관제의 지시로 두므로, 지도 버전의 내용 정의는 B. 공통 정보·환경 모델 쪽, 배포·활성화 시점 조율과 이력 관리는 F. 도입·검증·유지관리 쪽이 맡는 분담이 될 것으로 보인다. [추정][^ref-031]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [8. 실시간 세계 상태·데이터 일관성](../b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)**: Kritzinger 외(2018)는 제조 분야 문헌을 검토해 물리 객체와 디지털 객체 사이 데이터 흐름의 자동화 정도에 따라 디지털 모델·디지털 섀도·디지털 트윈을 구분했다(제조 대상 분류). [사실][^ref-291] 8. 실시간 세계 상태·데이터 일관성은 현재 상태를 표현하고 22. 시뮬레이션·예측용 디지털 트윈은 그 모델을 이용해 가정한 미래를 실험한다는 분류 원문의 구분에 따라, 22. 시뮬레이션·예측용 디지털 트윈은 8. 실시간 세계 상태·데이터 일관성의 현재 상태(로봇·설비·배터리 상태)를 시나리오 초기값으로 받는 쪽이 될 것으로 보이며, 근거 분류 자료가 물류가 아닌 제조 대상이라는 한계가 있다. [추정][^ref-291][^ref-406]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 8. 실시간 세계 상태·데이터 일관성**: VDA 5050 상태 스키마(3.0.0 판)는 powerSupply 아래 충전 상태(stateOfCharge), 배터리 건강 상태(batteryHealth, 0~100%), 현재 충전량으로 추정한 도달 거리(range), 충전 여부(charging)를 로봇이 보고하게 한다(확인일 2026-09-25). [사실][^ref-051]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ 6. 지도·공간·위치 모델**: Sommer 외(2023)는 건물 환경 스캔과 객체 검출을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 제시했다(생산 계획 대상 연구). [사실][^ref-241]

[B. 공통 정보·환경 모델 페이지의 다른 대분류와의 연결](../b-common-information-and-environment-model/index.md#다른-대분류와의-연결)은 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리와의 연결을 아직 다루지 않은 연결로 두고 있으며, 위 24. 자산·소프트웨어 수명주기 관리 두 항목이 그 절을 보강할 근거 후보다.

### C. 연결·실행 기반

[C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md)과는 등록 정보·어댑터 설정, 설비 연동의 시뮬레이션, 판 차이 오류와 적합성 시험으로 이어진다.

- **21. 온보딩·설정·현장 시운전 ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)**: VDA 5050 은 팩트시트를 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보로 두며, 초기 설정 뒤 관제–로봇 능력의 지속적인 호환성 평가에도 쓰도록 하는지는 미확인이다. [추정][^ref-031] 팩트시트 스키마는 적재 명세(loadSpecification.loadSets), 로봇 구성의 버전 목록(mobileRobotConfiguration.versions, 예: softwareVersion), 충전 설정(batteryCharging 의 criticalLowChargingLevel·minimumDesiredChargingLevel·maximumDesiredChargingLevel·minimumChargingTime)을 담는다(확인일 2026-09-25). [사실][^ref-228] 그래서 한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화에 함께 쓰이는 것으로 보인다. [추정][^ref-228] Open-RMF 플릿 어댑터 설정은 최대 선·각속도와 가속도, 수행 가능한 작업 유형(loop·delivery·clean), 로봇 외곽 반경, 배터리·재충전 임계값, 제조사 관제 API 연결 정보(주소·계정)를 요구한다. [사실][^ref-153]
- **21. 온보딩·설정·현장 시운전·22. 시뮬레이션·예측용 디지털 트윈·23. 시험·형식 검증·벤치마크 ↔ [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)**: 앞의 traffic-editor 주석 대상에는 문·승강기가 들어간다. [사실][^ref-079] Open-RMF 시뮬레이션 문서에 따르면 building_map_generator 는 traffic-editor 로 주석한 건물 지도에서 Gazebo 시뮬레이션 세계와 주행 그래프를 만들고, 문·승강기 플러그인, 워크셀을 흉내 내는 TeleportDispenser·TeleportIngestor, 여러 플릿 어댑터의 승강기 요청을 조율하는 lift_supervisor 를 둔다. [사실][^ref-406] 같은 문서는 시뮬레이션 속 로봇이 배터리 소모나 충돌 비용 없이 장시간·가속 조건으로 드문 예외 상황을 시험할 수 있고, 장시간 시뮬레이션이 배치 전 시설 소유자의 확신을 높인다고 설명한다. [사실][^ref-406]
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ 9. 로봇·제조사 관제 연동**: Open-RMF 시뮬레이션의 slotcar 플러그인은 경로·모드 요청을 받아 레일식으로 움직이고 센서 기반 주행 스택 없이 로봇 상태를 발행하는 전체 제어(full control) 로봇 모델이다. [사실][^ref-406] 이런 단순화 모델은 제조사 관제·로봇 고유 거동을 재현하지 않으므로, 관제 연동 방식(전체 제어·신호등·읽기 전용)과 제조사별 거동 차이가 처리량 예측 오차의 원인이 될 것으로 보인다(오차 크기 미확인, [열린 질문](../../open-questions.md) oq-086). [추정][^ref-406]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 9. 로봇·제조사 관제 연동**: VDA 5050 3.0.0 에서는 로봇이 자신이 쓸 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 유형의 오류를 CRITICAL 수준으로, 문제가 된 필드의 참조와 함께 보고해야 한다. [사실][^ref-031]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)**: ROS 2 관리형 노드는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate 같은 전이를 두어, 감독 도구가 구성요소 준비를 확인한 뒤 실행을 허용하게 한다. [사실][^ref-364]
- **23. 시험·형식 검증·벤치마크 ↔ 9. 로봇·제조사 관제 연동·12. 명령·작업 실행의 신뢰성**: 공개 개인 프로젝트 vda5050-sim 은 VDA 5050 3.0.0 주문 수명주기·동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을, vda5050-lab 은 메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT) 기록에서 반복 주문 id·재연결·취소 불일치를 진단한다고 README 에 적으며, 둘 다 VDA·VDMA 공식 적합성 시험이 아니다. [사실][^ref-407][^ref-408] OTTO by Rockwell Automation 은 자사 AMR 이 여러 관제 업체와 VDA 5050 인증을 마쳤다고 2026-04 발표했으나, 인증의 시험 항목은 확인되지 않았다. [추정] 벤더 주장[^ref-608] 연계 대상: ros2_fault_injection 은 오도메트리·레이저 스캔·관성 측정 장치(Inertial Measurement Unit, IMU)·점군 같은 센서 신호와 속도 명령을 조작하는 로봇 수준 장애 주입 도구이며, 23. 시험·형식 검증·벤치마크에서 ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. [추정][^ref-601]

같은 연결의 반대편은 [C. 연결·실행 기반 페이지의 다른 대분류와의 연결](../c-connectivity-and-execution-foundation/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### D. 계획·최적화

[D. 계획·최적화](../d-planning-and-optimization/index.md)와는 배정·경로 알고리즘을 시뮬레이션·벤치마크·형식 검증으로 시험하고, 배터리 열화 정보를 제약으로 넘기는 데서 이어진다.

- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md)·[15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)**: 앞의 A. 업무·공급망 설계 항목에서 본 피킹 주문 배정 규칙 비교는 시뮬레이션 조건에서 나온 결과다. [사실][^ref-398] 다중 AGV 시스템의 경로망(roadmap)을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있다. [사실][^ref-267]
- **21. 온보딩·설정·현장 시운전 ↔ 15. 다중 로봇 경로·교통 관리 — MAPF**: 시운전 때 traffic-editor 로 주석한 그래프가 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- **23. 시험·형식 검증·벤치마크 ↔ 15. 다중 로봇 경로·교통 관리 — MAPF**: Stern 외(2019)는 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)의 가정·목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했으나, 그 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). [사실][^ref-186] Yan 외(2026-02, 프리프린트)는 기존 MAPF 연구가 단순한 운동 모델과 완전한 실행·통신을 가정한다고 지적하고, 플릿 관리 시스템 안에서 계획 시점·방법·복구 설계 선택을 비교하는 시험대(LSMART)를 제안했다. [사실][^ref-604] 이 시험대는 D. 계획·최적화의 경로 알고리즘을 23. 시험·형식 검증·벤치마크의 시험 환경으로 잇는 사례로 보인다. [추정][^ref-604] von Berg 외(2026-05)는 창고 물류 AGV 의 교착 회피를 전이 시스템 인코딩과 BDD 로 분석한 사례 연구를 발표했다(계산 규모 한계는 oq-088). [사실][^ref-609]
- **23. 시험·형식 검증·벤치마크 ↔ 13. 작업 배정 — MRTA**: Lott·Honary(2026-09, 프리프린트)는 분산 작업 배정기 6종을 패킷 손실·페이딩 같은 통신 저하 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크를 제시했다. [사실][^ref-493]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 13. 작업 배정 — MRTA·[16. 공용 자원·충전·에너지 최적화](../d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)**: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 작업 배정·충전 일정을 정하는 연구(2026-03, 프리프린트)가 있다. [사실][^ref-403] 로봇이 보고하는 batteryHealth 가 낮아지면 같은 충전 상태에서도 도달 거리(range)가 짧아질 수 있어, 배터리 열화 정보가 13. 작업 배정 — MRTA·16. 공용 자원·충전·에너지 최적화의 제약 입력이 되는 것으로 보인다(물류센터 실측 자료 미확인). [추정][^ref-051][^ref-403]

같은 연결의 반대편은 [D. 계획·최적화 페이지의 다른 대분류와의 연결](../d-planning-and-optimization/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### E. 협업·현장 운영

[E. 협업·현장 운영](../e-collaboration-and-field-operations/index.md)과는 장애 대응·인계·감시를 시험하고, 고장 진단을 정비로 넘기는 데서 이어진다.

- **23. 시험·형식 검증·벤치마크 ↔ [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)**: NIST ARIAC 2025 문서는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급(고우선) 주문을 과제로 두어 설비·로봇 장애와 긴급 주문 대응을 평가한다(확인일 2026-09-25). [사실][^ref-528] 이런 장애 과제 정의와 장애 주입 도구를 결합하면 20. 예외 복구·재계획·업무 연속성의 재배정·수동 전환·제한 운영 동작을 업데이트마다 다시 돌리는 회귀 시험 시나리오로 만들 수 있을 것으로 보이나, 물류 오케스트레이션에 적용해 공개한 사례는 확인되지 않았다(oq-087). [추정][^ref-528][^ref-601]
- **23. 시험·형식 검증·벤치마크 ↔ [17. 로봇 간 협업·물리적 인계](../e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)**: ASTM F3499-21 은 자율 무인 지상 차량(A-UGV)의 도킹 성능을 확인하는 시험 방법이며, 그 결과를 로봇팔 파지 허용 오차와 잇는 기준은 확인되지 않았다(oq-063). [사실][^ref-204]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)**: Lei 외(2025)는 산업용 로봇의 고장 모드·데이터 수집·모델 기반과 데이터 기반 진단을 상태 기반 정비 관점에서 정리한 검토를 발표했다. [사실][^ref-553]
- **23. 시험·형식 검증·벤치마크 ↔ 19. 모니터링·이상 탐지·원인 분석**: ROSMonitoring 은 ROS 시스템의 런타임 검증 프레임워크다. [사실][^ref-602] 이런 운영 중 감시는 배치 전 시험을 보완하는 연결 지점이 될 것으로 보인다. [추정][^ref-602]

같은 연결의 반대편은 [E. 협업·현장 운영 페이지의 다른 대분류와의 연결](../e-collaboration-and-field-operations/index.md#다른-대분류와의-연결)에서 같은 각주로 다룬다.

### G. 안전·보안·지능·거버넌스

[G. 안전·보안·지능·거버넌스](../g-safety-security-intelligence-and-governance/index.md)의 세부영역 페이지는 아직 심화 전이라, 아래 연결은 이 대분류 쪽 근거에 기댄다.

- **21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 ↔ [25. 안전·위험 관리](../g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)**: 연계 대상: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하며, 운용 구역 준비를 부속서 A 에 둔다(세부 시험 항목 미확인). [사실][^ref-470]
- **24. 자산·소프트웨어 수명주기 관리 ↔ 25. 안전·위험 관리**: 업체(세이프틱스) 자료인 로봇 시스템 위험성평가 가이드(발행일 미확인)는 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로, 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 미확인이다(oq-092, oq-093). [추정][^ref-559]
- **24. 자산·소프트웨어 수명주기 관리 ↔ [26. 사이버보안·접근권한·개인정보](../g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)**: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템(Industrial Automation and Control Systems, IACS) 환경의 패치 관리를 다루는 기술 보고서다. [사실][^ref-554]
- **21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 ↔ [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)**: 분류 원문 8장 교차 규칙은 매뉴얼 해석을 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 AI 연구 방법으로 둔다. 이 규칙에 따르면 LLM 기반 능력 온톨로지 생성은 새 로봇 등록 작업을 줄이는 방법으로 두 대분류를 잇는 것으로 보이며, 온보딩 현장 적용 사례는 미확인이다. [추정][^ref-465][^ref-229] 같은 규칙대로 AI 내용을 적용 대상 영역과 양쪽으로 잇는다면, 23. 시험·형식 검증·벤치마크 쪽에는 AI 계획기의 평가 방법이 이어진다: ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과(목표 조건·성공률)로 자동 평가하는 공개 벤치마크이며, 물류 지시 데이터셋은 아니다. [사실][^ref-539][^ref-541] 관련 페이지는 [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md), [21. 온보딩·설정·현장 시운전](21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md)다.
- **22. 시뮬레이션·예측용 디지털 트윈 ↔ [28. 표준·상호운용성·다사업자 거버넌스](../g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)**: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고, 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나, 제조 대상 표준이라 물류센터 적용 여부는 미확인이다(oq-085). [사실][^ref-516][^ref-518]
- **23. 시험·형식 검증·벤치마크·24. 자산·소프트웨어 수명주기 관리 ↔ 28. 표준·상호운용성·다사업자 거버넌스**: 연계 대상: 국내에는 바퀴형 서비스 로봇의 이동 성능 시험방법 KS B ISO 18646-1 과 한국로봇산업진흥원의 시험평가 서비스가 있어, 로봇 자체 성능 시험은 시험기관 쪽이고 23. 시험·형식 검증·벤치마크의 ROP 몫은 그 결과를 등록·배정 조건으로 받는 쪽으로 보인다(oq-089). [추정][^ref-606][^ref-607] 한국산업기술시험원(KTL)과 통합물류협회가 물류로봇 시험인증 협력을 강화하기로 했다는 2026-07-24 기사가 있어(기사 기준, 1차 출처 미확인), 국내 물류로봇 시험·인증 체계가 두 세부영역을 잇는 후보가 될 것으로 보인다. [추정][^ref-466] 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 새 로봇 연동 승인 기준으로 쓰고 판 차이(2.x·3.0.0)로 생기는 UNSUPPORTED_PARAMETER 같은 미지원 오류를 누가 판정·수정할지가 28. 표준·상호운용성·다사업자 거버넌스로 넘어가는 과제가 될 것으로 보인다(공식 인증 절차 부재는 확정 사실 아님, oq-055·oq-091). [추정][^ref-407][^ref-408][^ref-608][^ref-031]

### 아직 다루지 않은 연결

다음 연결은 이번 실행에서 근거를 확보하지 못해 비워 둔다.

- [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) ↔ 22. 시뮬레이션·예측용 디지털 트윈: 제한 운영 상태의 처리량 저하를 미리 추정하는 근거 미확보(oq-081).
- [E. 협업·현장 운영](../e-collaboration-and-field-operations/index.md) ↔ 21. 온보딩·설정·현장 시운전: 근거 미확보.
- 22. 시뮬레이션·예측용 디지털 트윈 ↔ [26. 사이버보안·접근권한·개인정보](../g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md): 근거 미확보.
- [C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md)의 [11. 분산 시스템·통신·컴퓨팅 구조](../c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)와 이 대분류의 연결: 근거 미확보.
- [B. 공통 정보·환경 모델](../b-common-information-and-environment-model/index.md)의 [7. 화물·재고·자산 식별과 추적](../b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)과 이 대분류의 연결: 근거 미확보.

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-204]: ASTM International, Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21), 2021, https://www.astm.org/f3499-21.html, 접근일 2026-09-25 (원문 미열람)
[^ref-217]: Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L., Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission (CORDIS), PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: ROS 2 Design, Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-466]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-09-25 (원문 미열람)
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-539]: askforalfred (ALFRED 공식 저장소), ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README), 미확인, https://github.com/askforalfred/alfred, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-553]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-554]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-559]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)
[^ref-601]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25 (원문 미열람)
[^ref-602]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25 (원문 미열람)
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-606]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-607]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-609]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [F. 도입·검증·유지관리](index.md) — '다른 대분류와의 연결' 절 신규 작성(A·B·C·D·E·G 연결, 근거 미확보 연결 5건, 각주 41건) (실행 2026-09-25-67)
- 2026-09-25 · 요약 · [F. 도입·검증·유지관리](index.md) — F. 도입·검증·유지관리: 다른 대분류와의 연결 절 신규 작성(A·B·C·D·E·G 연결, f6·f18 강등 반영, 근거 미확보 연결 5건 명시) (실행 2026-09-25-67)
- 2026-09-25 · 갱신 · [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가. 2차 수정: 7절 첫 문장 [추정]·각주 보강, 8절 대표 연구 분류·평가 [의견]화, 8절 ref-556 항목 롤백 문구 정정 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "4. 핵심 개념과 용어" 절(1,365자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "6. 대표 접근법과 기술" 절(1,327자)을 옮겼다. 2차 수정: 부품 진단 연계 대상 문장을 [추정]과 각주로 고치고, 5·9절 참조를 원 세부영역 페이지 절 링크로 바꿈 (실행 2026-09-25-61)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [8]은 참고문헌 [ref-008](../../references/ref-008.md)에 해당한다.[^ref-008]

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24
