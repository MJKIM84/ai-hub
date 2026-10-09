---
title: "I. 설계·시뮬레이션"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-079, ref-098, ref-101, ref-102, ref-103, ref-104, ref-105, ref-106, ref-109, ref-116, ref-241, ref-267, ref-291, ref-381, ref-398, ref-406, ref-407, ref-409, ref-516, ref-518, ref-521, ref-526, ref-527, ref-528, ref-741, ref-815, ref-831, ref-832, ref-833, ref-943, ref-971, ref-1086, ref-1087, ref-1088, ref-1089, ref-1090, ref-1091, ref-1092, ref-1096, ref-1126, ref-1127, ref-1128, ref-1129, ref-1130, ref-1131, ref-1133, ref-1134, ref-1165, ref-1231, ref-1241, ref-1242, ref-416, ref-1243, ref-1244, ref-1245, ref-1246, ref-1247, ref-1248, ref-1249, ref-1250, ref-1251, ref-822, ref-1252]
---

[홈](../../index.md) › I. 설계·시뮬레이션

# I. 설계·시뮬레이션

## 핵심 질문

현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

## 개요

시나리오를 모델링하고, 시뮬레이션으로 처리능력·배치·정책을 미리 보고, 가상 시운전과 실제 상황 재현을 하는 설계 사용자의 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **33. 시나리오 모델·편집** | 시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 | 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? | [33. 시나리오 모델·편집](scenario-model-and-editing.md) | published |
| **34. 시뮬레이션·예측용 디지털 트윈** | 물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 | 현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? | [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md) | published |
| **35. 처리능력·규모·배치 설계** | 필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 | 로봇을 늘려야 할까, 공간이나 설비가 병목일까? | [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md) | published |
| **36. 가상 시운전·실제 상황 재현** | 설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 | 설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? | [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 다른 대분류와의 연결

I. 설계·시뮬레이션의 네 세부영역 — [33. 시나리오 모델·편집](scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md), [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) — 이 다른 대분류의 세부영역에서 무엇을 받고 무엇을 넘기는지 대분류 문자 순으로 적는다. 연결을 해석한 문장은 대부분 추정이고, 근거 가운데 일부는 로봇 플릿이 아닌 대상(자율주행·제약 공정·단일 로봇)에서 나왔으므로 문장마다 그 대상을 밝힌다. 승강기·문·PLC 제어, 로봇 자체 주행·인식, 안전 인증, 수요예측은 연계 대상으로만 다룬다.

- [A. 기획·사업](../planning-and-business/index.md)
    - 35. 처리능력·규모·배치 설계 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md): Howard(Cal Poly 석사논문, 2026-06)는 처리량 최대화 기준의 자율이동로봇(Autonomous Mobile Robot, AMR) 대수 산정이 서비스형 로봇(Robot-as-a-Service, RaaS) 구독 과금에서 플릿을 과대 산정한다고 보고, 대수 산정을 주문 라인당 비용 최소화 문제로 바꿔 피킹 구역제 물류창고를 이산 사건 시뮬레이션 27,000회로 분석했다. [사실][^ref-822] 그 조건에서 라인당 비용은 AMR:피커 비율에 대해 U자형이었고, 비용이 가장 낮은 비율은 저수요 1에서 고수요 2.5로 옮겨 갔다(저자 보고값). [사실][^ref-822]
    - 36. 가상 시운전·실제 상황 재현 ↔ 3. 경제성·조달·사업 모델: Rockwell Automation 사례 소개(2024-08-28)는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18%, 현장 시운전을 5주 줄였다고 밝히지만, 이는 벤더 주장이며 18%·5주의 기준선과 측정 방법은 공개되지 않았다(컨베이어 제어 에뮬레이션은 설비 업체·통합자 쪽 연계 대상, 독립 측정은 [oq-257](../../open-questions.md)). [추정][^ref-1165]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md): NVIDIA 는 2025-01-06 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 배치 전에 센서 시뮬레이션·합성 데이터로 로봇 플릿을 시험·최적화할 수 있다고 내세우지만, 이는 독립 확인되지 않은 벤더 주장이다(센서 시뮬레이션은 시뮬레이터 제공자 쪽 연계 대상). [추정][^ref-527]
- [B. 로봇 온톨로지](../robot-ontology/index.md)
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md): 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로 기종 제원 기술(형상·질량·센서)이 시뮬레이션 자산의 원천으로 이어질 것으로 보이나, 등록 정보와 시뮬레이션 모델을 잇는 사례는 확인하지 못했다. [추정][^ref-1092]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 4. 이기종 로봇 등록: IDTA 서브모델 템플릿 'Provision of Simulation Models'(1.0, IDTA 02005)는 자산관리셸(Asset Administration Shell, AAS)을 통해 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하고, 현재 단계 사용 사례로 시뮬레이션 모델 검색과 제조사·유통사에 대한 모델 파일 요청을 둔다. [사실][^ref-1251]
    - 36. 가상 시운전·실제 상황 재현 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md): 7. 온톨로지 검증·변경 관리가 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정하려면 모델·시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다([oq-156](../../open-questions.md)). [추정][^ref-1133][^ref-1127]
- [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md) — 분류 원문의 C. 채팅 기반 구성·운영 주석에 따라 대화 기능은 엔진과 짝으로 읽는다. 시나리오 구성과 실제 상황 재현의 엔진은 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현, 맵 작성의 엔진은 [14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md)·[15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md), 업무 지시의 엔진은 [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)·[26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)이다. 아래 근거는 로봇 플릿이 아닌 대상에서 나온 것이 많다.
    - 33. 시나리오 모델·편집 ↔ [9. 채팅으로 시나리오 구성](../chat-based-configuration-and-operation/chat-scenario-composition.md): Chat2Scenic(2026-07)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다(자율주행 시나리오 대상이며 로봇 플릿이 아니다). [사실][^ref-833]
    - 33. 시나리오 모델·편집 ↔ 9. 채팅으로 시나리오 구성·[13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md): 대화로 만든 시나리오의 출력 형식은 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식이 되고, 생성 스크립트가 컴파일되지 않는 경우가 남으므로 승인 전 형식 검사가 두 대분류의 인계 지점이 될 것으로 보인다(사용자 의도와의 일치를 검사하는 방법은 미확인). [추정][^ref-833][^ref-1088][^ref-528]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md): Xia 외(2026-08, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다(로봇 플릿 대상이 아니다). [사실][^ref-832]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 11. 채팅으로 실제 상황 시뮬레이션 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34. 시뮬레이션·예측용 디지털 트윈의 시뮬레이션 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36. 가상 시운전·실제 상황 재현의 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-832][^ref-1127]
    - 36. 가상 시운전·실제 상황 재현 ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md): SayPlan(Rana 외, CoRL 2023)은 언어 모델이 3차원 장면 그래프로 세운 초기 계획을 실행 전에 장면 그래프 시뮬레이터로 확인하고 그 피드백으로 실행 불가능한 동작을 고치는 반복 재계획을 두며, 최대 3개 층·36개 방·140개 자산·물체의 두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연했다(단일 로봇 대상). [사실][^ref-416] 대화로 만든 계획을 사람이 승인하기 전에 36. 가상 시운전·실제 상황 재현의 실행 전 계획 검증으로 실행 가능성을 먼저 걸러 내는 구조가 두 영역의 접점이 될 것으로 보이나, 다중 로봇 플릿 계획에 적용한 사례는 확인하지 못했다. [추정][^ref-416]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [8. 채팅으로 맵 작성](../chat-based-configuration-and-operation/chat-map-authoring.md): Open-RMF 에서 같은 건물 파일(`.building.yaml`)이 주행 그래프와 시뮬레이션 월드를 모두 만들므로, 대화로 작성·수정한 지도가 같은 형식으로 저장되면 시뮬레이션 월드도 다시 생성할 수 있을 것으로 보이나 대화형 지도 작성과 연결한 사례는 확인하지 못했다. [추정][^ref-406][^ref-079]
- [D. 공간·지도 모델](../space-and-map-model/index.md)
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md): Open-RMF 의 `building_map_generator` 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽과 문·승강기를 담은 시뮬레이션 월드와 주행 그래프를 만들고, 환경을 바꿀 때는 주석을 고쳐 다시 생성한다(두 출처는 같은 기관 자료). [사실][^ref-406][^ref-079]
    - 33. 시나리오 모델·편집 ↔ 14. 도면·BIM에서 지도 만들기, L. AI·학습 기술의 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md): 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33. 시나리오 모델·편집의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다. [추정][^ref-815][^ref-1089]
- [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): 제조 분야 분류 자료가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현장 상태를 가상 모델에 반영하는 현재 상태 표현을, 34. 시뮬레이션·예측용 디지털 트윈은 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). [추정][^ref-291]
    - 36. 가상 시운전·실제 상황 재현 ↔ [19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md): Waymax(2023)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다(자율주행 대상이며 로봇 현장 사례가 아니다. 관련 열린 질문 [oq-256](../../open-questions.md)). [사실][^ref-1128]
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 19. 사람·보행자 모델, M. 안전의 [49. 사람 근접 안전](../safety/human-proximity-safety.md): Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드(현장 유형: 상업 시설)가 이를 군중 시뮬레이션으로 쓴다(예제 월드이며 실제 시설 배치가 아니다. 두 출처는 같은 기관 자료). [사실][^ref-406][^ref-104]
    - 33. 시나리오 모델·편집 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md): NIST ARIAC 시나리오는 작업 대상인 배터리 셀의 종류(Li-Ion·Ni-MH)·전압 허용 범위·결함(찌그러짐·부풂·긁힘)과 4셀 키트를 정의하고, 키트는 출하 지점에서 제출 서비스가 셀 결함·전압·종류·총전압 조건을 모두 만족할 때만 받아들인다(현장 유형: 제조 공장, 경진대회 시뮬레이션이며 실제 공장이 아니다). [사실][^ref-1087] 이처럼 시나리오가 작업 대상의 속성과 완료 판정 조건을 함께 담으면 시나리오 형식이 17. 작업 대상·자산 식별과 인계 추적의 작업 대상 식별자와 G. 계획·최적화의 [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)의 완료 조건 어휘를 공유해야 할 것으로 보이나, 이를 정한 공통 형식은 확인하지 못했다. [추정][^ref-1087]
- [F. 연동](../integration/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 시뮬레이션의 문·승강기 플러그인은 실제와 같은 문·승강기 요청 메시지에 응답하고, `door_supervisor` 는 한 로봇이 다른 로봇 앞에서 문을 닫는 것 같은 충돌을 막으며 `lift_supervisor` 는 여러 플릿의 승강기 요청을 관리한다(실제 승강기·문 제어는 연계 대상이며 ROP 는 요청·상태 확인만 맡는다). [사실][^ref-406]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): Open-RMF 의 slotcar(슬롯카) 플러그인은 플릿 어댑터의 경로·모드 요청(`PathRequest`·`ModeRequest`)을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물을 감지하면 멈추는 단순화 로봇 모델로, 센서 기반 주행 스택을 돌리는 계산 부담을 피한다(로봇 자체 주행·인식 거동의 충실도는 제조사·물리 시뮬레이터 쪽 연계 대상). [사실][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 20. 로봇·제조사 관제 연동: 공개 오픈소스 vda5050-sim 은 VDA 5050 3.0.0 을 주 대상으로 2.1.0·2.0.0·1.1.0 구형 판도 흉내 내고, 공식 3.0.0 JSON 스키마 위에 세운 메시지 스키마와 적합성 시험 묶음을 둔다고 README 에 적는다(개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아니다). [사실][^ref-407]
    - 36. 가상 시운전·실제 상황 재현 ↔ 20. 로봇·제조사 관제 연동, O. 검증·도입·수명주기의 [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md): 2025-07 보도에 따르면 클로봇은 산업통상자원부 국가로봇테스트필드 기술개발 과제(54억원) 주관기관으로 KETI 와 함께 다종·다수 로봇 제어 플릿 관리 시스템(Fleet Management System, FMS) 요소기술, 로봇과 디지털 트윈·시뮬레이터 간 인터페이스, 실환경 연동 디지털 트윈 증강 시뮬레이션을 2028년까지 개발해 국가로봇테스트필드에 적용하는 것을 목표로 한다(기사 1건 기준이며 과제 공고·성과는 미확인). [사실][^ref-1247]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): 제조용 디지털 트윈 프레임워크 ISO 23247 은 제1부가 국내에 KS X ISO 23247-1 로 들어와 있다. [사실][^ref-516] 디지털 트윈 결합을 다루는 ISO 23247 제6부는 2026년에 발행되었으나, 이 프레임워크를 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다([oq-085](../../open-questions.md)). [사실][^ref-518]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): 연계 대상: 성수기 주문·물동량 전망 같은 시나리오 입력은 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토(Le·Fan, 2024)는 실제 데이터로 검증한 연구가 소수라고 보고한다. [추정][^ref-521]
    - 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 63. 병원·의료: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸다(현장 유형: 병원, 승강기 제어 자체는 연계 대상). [사실][^ref-943]
    - 35. 처리능력·규모·배치 설계 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 64. 상업 시설: 다층 호텔의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다(현장 유형: 상업 시설, 승강기 제어 자체는 연계 대상). [사실][^ref-103]
    - 35. 처리능력·규모·배치 설계 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 65. 가정·공동주택: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다(현장 유형: 가정, 공동주택 대상). [사실][^ref-409]
- [G. 계획·최적화](../planning-and-optimization/index.md)
    - 35. 처리능력·규모·배치 설계 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): 한 유통사 물류센터 팔레트 이동 데이터로 한 AMR 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)의 충전·배터리 교환 전략을 반개방형 대기행렬 네트워크로 비교한 연구(Zou 외, 2018)가 있다. [사실][^ref-098] 창고 충전소 배치를 페이지랭크 유사 방법으로 최적화하는 연구(Stark 외, 2024-06)도 있다. [사실][^ref-109]
    - 35. 처리능력·규모·배치 설계 ↔ 25. 작업 배정 — MRTA: Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 `recharge_threshold`(예시값 0.10) 아래인 로봇은 작동하지 않으며, 충전 작업의 목표 충전 수준은 `recharge_soc`(예시값 1.0)로 둔다. [사실][^ref-105] 그래서 충전기 수·위치 같은 충전 설비 계획의 결과가 운영 중 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보이나, 공개 사례는 확인하지 못했다. [추정][^ref-105][^ref-102]
    - 35. 처리능력·규모·배치 설계 ↔ 26. 작업 순서·스케줄링: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다(저자 계산 실험 조건, 독립 재현 미확인). [사실][^ref-381]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ 25. 작업 배정 — MRTA: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이다. [사실][^ref-101] Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다(시뮬레이션 결과이며 현장 실측이 아니다). [사실][^ref-398]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다. [사실][^ref-267] 경로망 배치를 시뮬레이션으로 평가하는 일은 현재 상태 표현이 아니라 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽에 걸치는 것으로 보인다. [추정][^ref-267]
    - 33. 시나리오 모델·편집 ↔ 27. 다중 로봇 경로·교통 관리 — MAPF: Moving AI Lab 의 다중 에이전트 경로 찾기(MAPF) 벤치마크는 지도마다 시나리오 파일(even·random 각 25개)을 묶어 공개한다. [사실][^ref-1091] 지도와 시나리오 파일을 묶어 공개하는 방식은 경로 계획기를 같은 조건에서 비교하게 하는 시나리오 라이브러리 구성의 예로 쓰일 수 있을 것으로 보인다. [추정][^ref-1091]
    - 33. 시나리오 모델·편집 ↔ 24. 작업·워크플로 모델링: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33. 시나리오 모델·편집의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24. 작업·워크플로 모델링의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다. [추정][^ref-116][^ref-1090]
    - 36. 가상 시운전·실제 상황 재현 ↔ 25. 작업 배정 — MRTA: VirTooS(2026-08)는 ROS 2와 Unity 를 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다. [사실][^ref-1129] Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다(현장 유형: 병원). [의견][^ref-943]
- [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)
    - 33. 시나리오 모델·편집 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): NIST ARIAC 는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다(현장 유형: 제조 공장, 경진대회 시나리오이며 실제 공장이 아니다). [사실][^ref-528]
    - 36. 가상 시운전·실제 상황 재현 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)·32. 예외 복구·재계획·업무 연속성: vda5050-sim 은 로봇별 고장 프로필로 연결 끊김·오류 주입·필드 위반·서비스 모드·비상 정지의 확률을 정하고, 명세의 재시도 가능 동작 흐름(`RETRIABLE`·`retry`·`skipRetry`)을 구현한다고 README 에 적는다(개인 프로젝트의 자기 기술이며 공식 적합성 시험이 아니다). [사실][^ref-407]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): Open-RMF 시뮬레이션의 `TeleportDispenser` 는 `DispenserRequest` 에 응답해 적재물을 가장 가까운 로봇 위로 순간 이동시키고, `TeleportIngestor` 는 `IngestorRequest` 에 응답해 로봇의 적재물을 월드로 옮겨 배송 작업의 적재·하역을 흉내 낸다. [사실][^ref-406] 적재·하역을 순간 이동으로 대신하므로 이 시뮬레이션은 물리적 인계 동작이 아니라 인계 요청–응답 흐름과 그 순서를 시험하는 데 쓰이며, 인계 실패 같은 물리 거동은 별도 모델이 필요할 것으로 보인다(파지·적재 물리는 로봇 자체 제어 쪽 연계 대상). [추정][^ref-406]
    - 35. 처리능력·규모·배치 설계 ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): Garg·Maywald·Naman(IJRDM, 2025)은 AMR 과 피킹 작업자 수를 바꾼 창고 구성 48가지의 이산 사건 시뮬레이션에서 처리량·효율이 AMR:작업자 약 2:1 에서 가장 높았고, 교차 통로 배치의 처리량 효과는 통계적으로 유의하지 않았다고 보고했다(저자 시뮬레이션 조건). [사실][^ref-1243] Howard(2026)의 시뮬레이션(3구역 순차 구역제·연속 도착 조건)에서는 피커(작업자) 유휴 시간이 교대당 AMR 유휴 시간보다 약 2.5배 비싸 피커와 로봇이 서로 기다리는 동기화 손실의 비용이 주로 노동 쪽에 떨어졌고, 세 배차 휴리스틱은 라인당 비용에 유의한 차이를 내지 않았다(교대조 단위 계획은 [oq-009](../../open-questions.md)로 남아 있다). [사실][^ref-822]
- [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)
    - 36. 가상 시운전·실제 상황 재현 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)·[38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): rosbag2 는 ROS 2 통신을 백 파일(기본 저장 형식 MCAP)로 기록하고, 재생 속도 조절(`~/set_rate`)·`/clock` 발행(`--clock`)·토픽 선택(`--topics`)·여러 백 파일의 수신 시각순 동시 재생(`-i`)을 지원하며, 시작 시각 지정은 `~/play` 서비스로 제공한다. [사실][^ref-831]
    - 36. 가상 시운전·실제 상황 재현 ↔ 37. 관제 화면·실행 기록: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37. 관제 화면·실행 기록이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다([oq-131](../../open-questions.md)). [추정][^ref-831][^ref-1128]
    - 35. 처리능력·규모·배치 설계 ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md): 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다([oq-011](../../open-questions.md)). [추정][^ref-098][^ref-106]
- [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [41. 플랫폼 아키텍처·외부 API](../platform-architecture-and-infrastructure/platform-architecture-and-external-api.md): rmf_demos 는 시뮬레이션 데모에서 플릿 어댑터의 `server_uri` 를 rmf-web API 서버(`ws://localhost:8000/_internal`)로 지정하면 어댑터가 최신 작업·로봇 상태를 API 서버에 보내고 대시보드로 볼 수 있게 하며, Docker 대시보드는 빠른 연동·시험용이라고 적는다. [사실][^ref-104] 시뮬레이션 플릿과 실제 플릿이 같은 플랫폼 API·대시보드에 붙으므로 외부 시스템 연동과 운영자 화면을 설치 전에 가상 플릿으로 시험할 수 있을 것으로 보이나, 이를 시운전 절차로 정리한 공개 사례는 확인하지 못했다([oq-255](../../open-questions.md)). [추정][^ref-104][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다([oq-040](../../open-questions.md)). [추정][^ref-1129][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): MCAP 은 시각이 찍힌 발행·구독 메시지를 담는 컨테이너 형식으로, 메시지마다 기록 시각(`log_time`)과 발행 시각(`publish_time`)을 따로 두고 청크 색인에 청크별 최초·최종 기록 시각을 담아 시각·토픽으로 메시지를 찾게 한다. [사실][^ref-1096] rosbag2 의 기본 저장 형식이 MCAP 이다. [사실][^ref-831]
- [L. AI·학습 기술](../ai-and-learning/index.md) — 교차 규칙에 따라 L. AI·학습 기술의 영역과 적용 대상인 이 대분류의 영역을 함께 적는다. D. 공간·지도 모델 항목의 생성 환경 구분도 44. 로봇 기반 모델·언어 모델 계획과 33. 시나리오 모델·편집을 잇는다.
    - [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md) ↔ 33. 시나리오 모델·편집: Holodeck(CVPR 2024)은 GPT-4 가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다. [사실][^ref-815]
    - [45. 문서·도면·장면 이해](../ai-and-learning/document-drawing-and-scene-understanding.md) ↔ 34. 시뮬레이션·예측용 디지털 트윈: Sommer 외(2023)는 기존 건물 환경의 스캔과 객체 인식을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 다룬다(로봇 플릿 시뮬레이션에 쓴 사례는 미확인). [사실][^ref-241]
    - [46. 예측·학습 기반 최적화](../ai-and-learning/prediction-and-learning-based-optimization.md) ↔ 34. 시뮬레이션·예측용 디지털 트윈: Smit 외(2024-04, arXiv)는 작업자와 AMR 이 피킹 위치에서 만나는 창고에서 작업자–AMR 배정을 다목적 심층 강화학습으로 정하고, 이를 학습·평가하려고 이산 사건 시뮬레이션 모델을 만들었으며, 학습 정책이 효율과 작업자 부하 공정성 모두에서 비교 방법을 앞섰다고 보고했다(프리프린트, 학습 기반 배정이므로 25. 작업 배정 — MRTA 와도 이어진다). [사실][^ref-1245]
    - 46. 예측·학습 기반 최적화 ↔ 35. 처리능력·규모·배치 설계: Howard(2026)는 반개방형 대기행렬 모델로 설계안을 걸러 내고 XGBoost 대리 모델과 등각 예측 구간으로 추가 시뮬레이션 없이 연속 설계 공간의 비용을 예측했으며, 대기행렬 모델은 시뮬레이션 라인당 비용과 약 5%, 대리 모델은 교차 검증에서 3% 안에서 맞았다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-822]
    - [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ 36. 가상 시운전·실제 상황 재현: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47. AI·학습·적응과 모델 운영(및 로봇 제조사·시뮬레이션 도구 쪽 연계 대상)의 일이고 36. 가상 시운전·실제 상황 재현은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다. [추정][^ref-741][^ref-1127]
- [M. 안전](../safety/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md): Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다(협동 로봇 셀 대상이며 이동로봇 플릿이 아니다. 안전 인증·설비 안전 제어는 연계 대상). [사실][^ref-1241]
    - 33. 시나리오 모델·편집 ↔ 48. 안전·위험 관리: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로 33. 시나리오 모델·편집에서 선언한 장애·사람 흐름 시나리오가 48. 안전·위험 관리의 위험 식별 입력이 될 수 있을 것으로 보이나, 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-1241][^ref-1086]
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 49. 사람 근접 안전: E. 사물·사람·실시간 상태 항목의 Open-RMF 군중 시뮬레이션(crowdsim)이 이 연결의 예다.
    - 36. 가상 시운전·실제 상황 재현 ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): 연계 대상: Wind River 블로그 인터뷰(2014)는 IEC 61508-7 C.5.19 가 시뮬레이션을 시험 목적으로만 피제어 설비(Equipment Under Control, EUC)의 거동을 흉내 내는 시스템으로 정의한다고 인용하고 기능안전 표준들이 안전 확인에 시뮬레이션·장애 주입을 강하게 권고한다고 해석하지만, 이는 업체 직원의 인용·해석이고 표준 원문은 확인하지 않았으며, 이동로봇 안전 표준이 시뮬레이션 결과를 인증 근거로 받아들이는 절차는 이번 조사에서 찾지 못했다. [추정][^ref-1249]
- [N. 보안·개인정보](../security-and-privacy/index.md)
    - 36. 가상 시운전·실제 상황 재현 ↔ [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md): Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고하고 완화 방안을 논의했다(프리프린트). [사실][^ref-1242]
    - 36. 가상 시운전·실제 상황 재현 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)·52. 통신 보호·위협 관리·감사: 36. 가상 시운전·실제 상황 재현이 다루는 디지털 트윈 동기화(실시간 상태를 가상 모델에 반영하고 결과를 되돌리는 경로)는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다(로봇 플릿 플랫폼 적용 사례는 확인하지 못했다). [추정][^ref-1242]
    - 36. 가상 시운전·실제 상황 재현 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md): Autoware 재단의 `autoware_rosbag2_anonymizer` 는 ROS 2 백 파일(sqlite3·mcap)의 이미지에서 사람 얼굴·번호판 같은 대상을 GroundingDINO·OpenCLIP·SegmentAnything2·YOLO 로 찾아 가우시안 블러로 가린 익명화 백 파일을 만든다(자율주행 생태계 도구이며 ROP 직접 범위가 아니다). [사실][^ref-1246] 운영 기록으로 상황을 재현하거나 기록을 외부와 공유하기 전에 영상 기록의 얼굴 등을 가리는 익명화 단계가 두 영역의 경계가 될 것으로 보이나, 로봇 플릿 재현에서 익명화가 재현 충실도에 주는 영향을 다룬 자료는 확인하지 못했다. [추정][^ref-1246][^ref-831]
- [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 54. 시험·형식 검증·벤치마크·[55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): Open-RMF 문서는 시뮬레이션 로봇이 배터리 소모·충돌 비용이 없어 시나리오를 반복해 수정을 확인하고 드문 예외를 살필 수 있으며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높일 수 있다고 설명한다. [사실][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 55. 현장 조사·설치·시운전: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구가 있어 36. 가상 시운전·실제 상황 재현의 결과가 55. 현장 조사·설치·시운전의 현장 시운전 준비로 넘어갈 것으로 보이나, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(PLC·설비 제어 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상, [oq-255](../../open-questions.md)). [추정][^ref-1126][^ref-1130][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 54. 시험·형식 검증·벤치마크: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(Sim-vs-Real Correlation Coefficient, SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다(단일 로봇 주행 대상). [사실][^ref-1127] NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다. [사실][^ref-1133] F. 연동 항목의 국가로봇테스트필드 과제 보도도 이 연결에 해당한다.
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): Gazebo Fuel 서버의 모델·월드를 내려받고 올리는 gz-fuel-tools 의 README 로드맵은 원격 모델의 새 버전이 올라왔을 때 이를 감지하는 방법을 아직 정해야 할 과제로 적고 해시 기반 방식을 아이디어로 든다. [사실][^ref-1250]
- [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md): IDTA 'Provision of Simulation Models' 서브모델이 제조사·유통사에 시뮬레이션 모델 파일을 요청하는 사용 사례를 두므로, 로봇·설비 제조사가 가상 시운전용 모델을 어떤 형식·충실도로 제공할지가 다사업자 계약·데이터 제공 항목이 될 것으로 보인다(로봇 플릿 조달 계약에 넣은 사례는 미확인). [추정][^ref-1251]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md): Gazebo(클래식) 모델 데이터베이스 규칙은 `database.config` 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며(요구가 아니라 권장), 각 모델의 `model.config` 에 작성자 이름·이메일을 필수로 적게 한다([oq-292](../../open-questions.md)). [사실][^ref-1231]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md): Kassem·Michahelles(Mensch und Computer 2022 워크숍)는 협동 로봇이 공장·물류·제조 현장에 들어오면서 사람–기계 상호작용을 빠르게 평가할 필요가 커졌다고 보고, 소비자용 VR·AR 헤드셋으로 로봇을 가상으로 흉내 내 사용자 연구에 쓰는 방법과 방향을 제시했다(이동로봇 플릿 도입 전 작업자 수용성을 가상 환경으로 측정한 사례는 찾지 못했다). [사실][^ref-1248]
    - 35. 처리능력·규모·배치 설계 ↔ 60. 노동·수용성·접근성: H. 실행·협업·예외 복구 항목의 Howard(2026) 결과에서 동기화 손실의 비용이 주로 노동 쪽에 떨어진 것은 노동 비용 측면의 근거이며, 수용성·노동 영향의 직접 근거는 아니다(논문은 비용 분석이다). [사실][^ref-822]
- [Q. 현장 유형별 적용](../site-type-applications/index.md) — 현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고, 현장 유형에 공통인 시뮬레이션 기능은 이 대분류에 둔다. 아래의 예제 월드·벤치마크·경진대회 시나리오는 실제 현장 배치가 아니다.
    - 현장 유형 물류창고 — [61. 물류창고](../site-type-applications/warehouse.md): CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표하고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나(벤더 주장), 이후 적용 결과는 확인하지 못했다([oq-084](../../open-questions.md)). [추정][^ref-526] 위 A. 기획·사업, G. 계획·최적화, H. 실행·협업·예외 복구, L. AI·학습 기술 항목의 Howard·FAIM 2025·Garg 외·Smit 외 연구도 물류창고 조건이다.
    - 현장 유형 제조 공장 — [62. 제조 공장](../site-type-applications/manufacturing-plant.md): Stączek 외(Sensors, 2021-11)는 통로가 좁은 생산 홀의 AMR 운영 환경을 ROS 와 연결한 Gazebo 디지털 트윈으로 만들어 현장 시험 전에 위치 추정·주행·작업 시간을 확인했고, 통로에 회전용 홈을 내는 배치 변경안에서 도킹 복귀 시간이 평균 44초에서 22.5~23.3초로 줄었다고 보고했다(34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계와 연결. 수치는 저자 사례 연구의 보고값이며 검증 단계에서 다시 대조하지 못했다). [사실][^ref-1244] 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다(PLC 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상이며 방법 근거로만 쓴다). [사실][^ref-1131] 2026-08 보도에 따르면 아바코는 산업통상자원부 산업 AI 솔루션 실증확산 지원사업(이차전지 분야, 한국생산기술연구원 주관)에서 AMR 스마트 물류 시스템을 개발·실증하며 실물 설비 구축 전에 디지털 트윈 가상 환경에서 물류 동선과 장비 운용을 검증했고 공정물류 다운타임 20% 절감·물류 자동화율 90% 이상을 달성했다고 밝혔으나, 이는 벤더 주장이며 수치의 기준선·측정 방법은 공개되지 않았다. [추정][^ref-1252] E. 사물·사람·실시간 상태와 H. 실행·협업·예외 복구 항목의 ARIAC 시나리오도 제조 공장을 본뜬 경진대회 시뮬레이션이다.
    - 현장 유형 병원 — [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): F. 연동 항목의 고려대학교 구로병원 약품 배송 로봇 재현과 G. 계획·최적화 항목의 Lee 외 저자 의견이 해당한다.
    - 현장 유형 상업 시설 — [64. 상업 시설](../site-type-applications/commercial-facilities.md): Open-RMF 예제 호텔 월드는 로비와 객실 2개 층에 승강기 2대·여러 문·로봇 플릿 3개(로봇 4대)를 담고, 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 플릿·설비·사람의 상호작용과 청소 작업을 보이는 시뮬레이션 예제다(실제 시설 사례가 아니다). [사실][^ref-104] F. 연동 항목의 다층 호텔 경로 계획 연구와 E. 사물·사람·실시간 상태 항목의 군중 시뮬레이션도 상업 시설 조건이다.
    - 현장 유형 가정 — [65. 가정·공동주택](../site-type-applications/home-and-apartment.md): BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(Behavior Domain Definition Language, BDDL)로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다(33. 시나리오 모델·편집과 연결, 실제 가정 배치가 아니다). [사실][^ref-971] F. 연동 항목의 아파트 단지 로봇 친화형 환경 인증 모델도 이 현장 유형에 해당한다.
    - 현장 유형 실외 — [66. 실외](../site-type-applications/outdoor.md): Open-RMF 예제 캠퍼스 월드는 GPS(WGS84) 좌표를 쓰는 넓은 실외 지도에서 여러 배송 로봇이 위치를 플릿 어댑터에 보내는 시뮬레이션 예제다(33. 시나리오 모델·편집과 연결, 실제 캠퍼스 배치가 아니다). [사실][^ref-104]
    - 현장 유형 기타 — [67. 기타 현장](../site-type-applications/other-sites.md): Ortega 외(Frontiers in Robotics and AI, 2024)는 실측 점유 격자로 모델링한 대학 건물 1층을 대상으로 동적 요소와 수용 기준(위치 추정 오차·충돌 회피)을 명시한 실행 가능한 이동로봇 시뮬레이션 시험 시나리오를 구성했다(36. 가상 시운전·실제 상황 재현과 연결, 시뮬레이션 시험 사례이며 현장 기록 재생은 다루지 않는다). [사실][^ref-1134]

**아직 다루지 않은 연결:** [2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md), [10. 채팅으로 로봇 구성](../chat-based-configuration-and-operation/chat-robot-configuration.md)(oq-129 관련 부분 근거만 있음), [40. 운영 절차·요청 창구](../field-operations-and-monitoring/operating-procedures-and-request-channels.md), [56. 운영 이관·확대·교육](../verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)과 이 대분류의 세부영역을 잇는 근거는 이번 조사에서 찾지 못했다.

[^ref-822]: Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities, 2026-06, https://digitalcommons.calpoly.edu/theses/3387, 접근일 2026-10-09
[^ref-1165]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-10-09 (원문 미열람)
[^ref-527]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 2025-01-06, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-10-09
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-10-09 (원문 미열람)
[^ref-1251]: IDTA (Industrial Digital Twin Association, admin-shell-io/submodel-templates), Provision of Simulation Models (IDTA 02005) 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models, 접근일 2026-10-09
[^ref-1133]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-10-09 (원문 미열람)
[^ref-1127]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-10-09 (원문 미열람)
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-10-09 (원문 미열람)
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-10-09 (원문 미열람)
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-10-09
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-10-09 (원문 미열람)
[^ref-416]: Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv), SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning, 2023-07-12, https://arxiv.org/abs/2307.06135, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-10-09
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-10-09 (원문 미열람)
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-10-09 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-10-09 (원문 미열람)
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-10-09 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-10-09
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-10-09
[^ref-1247]: 파이낸스스코프 (윤영훈), 클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정, 2025-07-11, https://www.finance-scope.com/article/view/scp202507110007, 접근일 2026-10-09
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-10-09 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-10-09 (원문 미열람)
[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-09 (원문 미열람)
[^ref-409]: 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105), 2023, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381, 접근일 2026-10-09 (원문 미열람)
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-10-09 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-10-09 (원문 미열람)
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-10-09 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-10-09 (원문 미열람)
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-10-09 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-10-09 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-10-09 (원문 미열람)
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-10-09 (원문 미열람)
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-10-09 (원문 미열람)
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-10-09 (원문 미열람)
[^ref-1129]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-10-09 (원문 미열람)
[^ref-1243]: Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11)), Optimising human-robot collaboration for efficiency in retail warehousing, 2025-10-14, https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for, 접근일 2026-10-09
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09
[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-10-09 (원문 미열람)
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-09
[^ref-741]: Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10, https://arxiv.org/abs/2510.20808, 접근일 2026-10-09 (원문 미열람)
[^ref-1245]: Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv), Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking, 2024-04-09, https://arxiv.org/abs/2404.08006, 접근일 2026-10-09
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-10-09 (원문 미열람)
[^ref-1241]: Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020), Simulation-based Testing for Early Safety-Validation of Robot Systems, 2020-11-20, https://arxiv.org/abs/2011.10294, 접근일 2026-10-09
[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-10-09 (원문 미열람)
[^ref-1249]: Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser, 2014-11-20, https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser, 접근일 2026-10-09
[^ref-1242]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09
[^ref-1246]: Autoware Foundation (autowarefoundation GitHub), autoware_rosbag2_anonymizer — README, 미확인, https://github.com/autowarefoundation/autoware_rosbag2_anonymizer, 접근일 2026-10-09
[^ref-1126]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-10-09 (원문 미열람)
[^ref-1130]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-10-09 (원문 미열람)
[^ref-1250]: Open Robotics (gazebosim/gz-fuel-tools GitHub), Gazebo Fuel Tools — README, 미확인, https://github.com/gazebosim/gz-fuel-tools, 접근일 2026-10-09
[^ref-1231]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-10-09 (원문 미열람)
[^ref-1248]: Kassem, K., & Michahelles, F. (Mensch und Computer 2022 Workshop Proceedings, Gesellschaft für Informatik), Exploring Human-robot Interaction by Simulating Robots, 2022-09, https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full, 접근일 2026-10-09
[^ref-1244]: Stączek, P., Pizoń, J., Danilczuk, W., & Gola, A. (Sensors 21(23):7830), A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR's) Operating Environment—A Case Study, 2021-11-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/, 접근일 2026-10-09
[^ref-1131]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-10-09 (원문 미열람)
[^ref-1252]: 파이낸스스코프, 아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속, 2026-08-14, https://www.finance-scope.com/article/view/scp202608140009, 접근일 2026-10-09
[^ref-526]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-10-09 (원문 미열람)
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-10-09 (원문 미열람)
[^ref-1134]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-10-09 (원문 미열람)

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 95건이다(논문 52건 · 기사·보고서 3건 · 업체 발표 7건 · 표준·오픈소스·기관 자료 33건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1129](../../references/ref-1129.md) — Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots (발행 2026-08-26)
- [ref-832](../../references/ref-832.md) — Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models (발행 2026-08-22)
- [ref-833](../../references/ref-833.md) — Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving (발행 2026-07-15)
- [ref-822](../../references/ref-822.md) — Howard, T. L. (California Polytechnic State University, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities (발행 2026-06)
- [ref-1307](../../references/ref-1307.md) — Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance (발행 2026-05-28)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-116](../../references/ref-116.md) — Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis (발행 2026-03)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-1243](../../references/ref-1243.md) — Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11)), Optimising human-robot collaboration for efficiency in retail warehousing (발행 2025-10-14)
- [ref-741](../../references/ref-741.md) — Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices (발행 2025-10)
- 그 밖에 42건

**기사·보고서**

- [ref-1252](../../references/ref-1252.md) — 파이낸스스코프, 아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속 (발행 2026-08-14)
- [ref-519](../../references/ref-519.md) — 머니투데이, 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 (발행 2026-07-28)
- [ref-1247](../../references/ref-1247.md) — 파이낸스스코프 (윤영훈), 클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정 (발행 2025-07-11)

**업체 발표**

- [ref-1165](../../references/ref-1165.md) — Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation (발행 2024-08-28)
- [ref-1132](../../references/ref-1132.md) — 현대자동차그룹, 가상의 디지털 공간에 세운 쌍둥이 공장 (발행 2023-11-21)
- [ref-526](../../references/ref-526.md) — CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) (발행 2021-11)
- [ref-1249](../../references/ref-1249.md) — Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser (발행 2014-11-20)
- [ref-527](../../references/ref-527.md) — NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins (발행 미확인)
- [ref-1309](../../references/ref-1309.md) — NVIDIA, Isaac Sim Documentation — Warehouse Creator Extension (발행 미확인)
- [ref-1090](../../references/ref-1090.md) — BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2 (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-518](../../references/ref-518.md) — ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition (발행 2026)
- [ref-1126](../../references/ref-1126.md) — VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions (발행 2025-05)
- [ref-1298](../../references/ref-1298.md) — Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey), Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor (발행 2024-06-05)
- [ref-1133](../../references/ref-1133.md) — NASA, NASA-STD-7009B Standard for Models and Simulations (발행 2024-03-05)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-831](../../references/ref-831.md) — ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications) (발행 미확인)
- [ref-528](../../references/ref-528.md) — NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges (발행 미확인)
- [ref-524](../../references/ref-524.md) — OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund), ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) (발행 미확인)
- [ref-523](../../references/ref-523.md) — Open Robotics (open-rmf), rmf_simulation — README (발행 미확인)
- [ref-517](../../references/ref-517.md) — NIST, Digital Twins for Advanced Manufacturing (발행 미확인)
- 그 밖에 23건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [33. 시나리오 모델·편집](scenario-model-and-editing.md) — 차등 갱신: 3절 면담 근거 추가, 5절 물류창고 경진대회 사례 추가·문장 교체, 6·7·8·10절 요약 덧붙임과 2026-09-30 주제 페이지 링크 복원, 9절 판 관리 문장 정정, 11절 첫 문장 건수 정정·진행 현황, 13절 각주 11건 추가, related_areas 에 57·61 추가, last_run 2026-10-09 (2차 수정 5건 반영) (실행 2026-10-09-13)
- 2026-10-09 · 생성 · [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area33-s6.md) — 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(2,409자)을 옮겼다 (실행 2026-10-09-13)
- 2026-10-09 · 생성 · [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-10-09-area33-s8.md) — 자동 분리: 33. 시나리오 모델·편집 의 "8. 대표 연구와 자료" 절(1,827자)을 옮겼다 (실행 2026-10-09-13)
- 2026-10-09 · 생성 · [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area33-s10.md) — 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,294자)을 옮겼다 (실행 2026-10-09-13)
- 2026-10-09 · 생성 · [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-10-09-area33-s11.md) — 자동 분리: 33. 시나리오 모델·편집 의 "11. 열린 질문" 절(1,273자)을 옮겼다 (실행 2026-10-09-13)
<!-- auto:category-recent:end -->
