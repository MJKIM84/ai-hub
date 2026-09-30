---
title: "운영 지표"
type: metrics
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](index.md) › 운영 지표

# 운영 지표

영역별 페이지 상태 분포, 검증 통과율, 반려·보류 건수, 출처 유형 분포, 현장 유형 매트릭스 채움률, 마지막 갱신이 오래된 영역을 퍼블리셔가 계산한다. 원천은 페이지 프런트매터(status, updated), `data/changelog.json`, `data/flow_matrix.json`, `runs/<run_id>/summary.json`, 참고문헌 페이지의 `source_type` 이다.

## 지표

<!-- auto:metrics:start -->
기준일: 2026-09-30

### 영역별 페이지 상태 분포

| 대분류 | seed | draft | verified | published | needs_update | deprecated | 합계 |
|---|---|---|---|---|---|---|---|
| [A. 기획·사업](categories/planning-and-business/index.md) | 1 | 0 | 0 | 16 | 0 | 0 | 17 |
| [B. 로봇 온톨로지](categories/robot-ontology/index.md) | 0 | 0 | 0 | 29 | 0 | 0 | 29 |
| [C. 채팅 기반 구성·운영](categories/chat-based-configuration-and-operation/index.md) | 0 | 0 | 0 | 48 | 0 | 0 | 48 |
| [D. 공간·지도 모델](categories/space-and-map-model/index.md) | 0 | 0 | 0 | 21 | 0 | 0 | 21 |
| [E. 사물·사람·실시간 상태](categories/objects-people-and-live-state/index.md) | 1 | 0 | 0 | 13 | 0 | 0 | 14 |
| [F. 연동](categories/integration/index.md) | 0 | 0 | 0 | 26 | 0 | 0 | 26 |
| [G. 계획·최적화](categories/planning-and-optimization/index.md) | 0 | 0 | 0 | 30 | 0 | 0 | 30 |
| [H. 실행·협업·예외 복구](categories/execution-collaboration-and-recovery/index.md) | 0 | 0 | 0 | 24 | 0 | 0 | 24 |
| [I. 설계·시뮬레이션](categories/design-and-simulation/index.md) | 0 | 0 | 0 | 27 | 0 | 0 | 27 |
| [J. 현장 운영·관제](categories/field-operations-and-monitoring/index.md) | 0 | 0 | 0 | 26 | 0 | 0 | 26 |
| [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md) | 0 | 0 | 0 | 21 | 0 | 0 | 21 |
| [L. AI·학습 기술](categories/ai-and-learning/index.md) | 0 | 0 | 0 | 30 | 0 | 0 | 30 |
| [M. 안전](categories/safety/index.md) | 0 | 0 | 0 | 23 | 0 | 0 | 23 |
| [N. 보안·개인정보](categories/security-and-privacy/index.md) | 0 | 0 | 0 | 23 | 0 | 0 | 23 |
| [O. 검증·도입·수명주기](categories/verification-deployment-and-lifecycle/index.md) | 1 | 0 | 0 | 17 | 0 | 0 | 18 |
| [P. 거버넌스·법규·사회](categories/governance-law-and-society/index.md) | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| [Q. 현장 유형별 적용](categories/site-type-applications/index.md) | 0 | 0 | 0 | 56 | 0 | 0 | 56 |

세부영역 페이지와 그 영역을 주 영역으로 하는 주제 페이지를 함께 센다.

**A. 기획·사업**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [1. 기술·시장·업체 동향](categories/planning-and-business/technology-market-and-vendor-trends.md) | published | medium | 2026-09-29 | 2 |
| [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md) | published | medium | 2026-09-30 | 2 |
| [3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md) | seed | — | 2026-09-28 | 1 |

**B. 로봇 온톨로지**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [4. 이기종 로봇 등록](categories/robot-ontology/heterogeneous-robot-registration.md) | published | medium | 2026-09-29 | 2 |
| [5. 로봇 능력·작업 표현](categories/robot-ontology/robot-capability-and-task-representation.md) | published | medium | 2026-09-25 | 2 |
| [6. 온톨로지 기반 시스템·로봇 연동](categories/robot-ontology/ontology-based-system-and-robot-integration.md) | published | medium | 2026-09-29 | 2 |
| [7. 온톨로지 검증·변경 관리](categories/robot-ontology/ontology-verification-and-change-management.md) | published | medium | 2026-09-29 | 2 |

**C. 채팅 기반 구성·운영**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [8. 채팅으로 맵 작성](categories/chat-based-configuration-and-operation/chat-map-authoring.md) | published | medium | 2026-09-29 | 2 |
| [9. 채팅으로 시나리오 구성](categories/chat-based-configuration-and-operation/chat-scenario-composition.md) | published | medium | 2026-09-29 | 2 |
| [10. 채팅으로 로봇 구성](categories/chat-based-configuration-and-operation/chat-robot-configuration.md) | published | medium | 2026-09-29 | 2 |
| [11. 채팅으로 실제 상황 시뮬레이션 재현](categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) | published | medium | 2026-09-29 | 2 |
| [12. 채팅으로 업무 지시·오케스트레이션](categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) | published | medium | 2026-09-29 | 2 |
| [13. 대화형 기능의 신뢰·기반](categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) | published | medium | 2026-09-29 | 2 |

**D. 공간·지도 모델**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [14. 도면·BIM에서 지도 만들기](categories/space-and-map-model/maps-from-floor-plans-and-bim.md) | published | medium | 2026-09-30 | 2 |
| [15. 지도·공간·위치 모델](categories/space-and-map-model/map-space-and-location-model.md) | published | medium | 2026-09-25 | 2 |
| [16. 장소 의미·지도 관리](categories/space-and-map-model/place-semantics-and-map-management.md) | published | medium | 2026-09-30 | 2 |

**E. 사물·사람·실시간 상태**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [17. 작업 대상·자산 식별과 인계 추적](categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) | published | medium | 2026-09-25 | 4 |
| [18. 실시간 세계 상태·데이터 일관성](categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) | published | low | 2026-09-25 | 2 |
| [19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md) | seed | — | 2026-09-28 | 1 |

**F. 연동**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [20. 로봇·제조사 관제 연동](categories/integration/robot-and-vendor-fleet-manager-integration.md) | published | medium | 2026-09-25 | 2 |
| [21. 상호운용 표준·적합성](categories/integration/interoperability-standards-and-conformance.md) | published | medium | 2026-09-25 | 2 |
| [22. 설비·건물 시스템 연동](categories/integration/facility-and-building-system-integration.md) | published | medium | 2026-09-25 | 2 |
| [23. 업무 시스템 연동](categories/integration/business-system-integration.md) | published | medium | 2026-09-25 | 2 |

**G. 계획·최적화**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [24. 작업·워크플로 모델링](categories/planning-and-optimization/task-and-workflow-modeling.md) | published | medium | 2026-09-25 | 2 |
| [25. 작업 배정 — MRTA](categories/planning-and-optimization/task-allocation-mrta.md) | published | medium | 2026-09-25 | 2 |
| [26. 작업 순서·스케줄링](categories/planning-and-optimization/task-sequencing-and-scheduling.md) | published | medium | 2026-09-25 | 2 |
| [27. 다중 로봇 경로·교통 관리 — MAPF](categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) | published | medium | 2026-09-25 | 2 |
| [28. 공용 자원·충전·에너지 최적화](categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) | published | medium | 2026-09-25 | 2 |

**H. 실행·협업·예외 복구**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [29. 명령·작업 실행의 신뢰성](categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) | published | medium | 2026-09-25 | 2 |
| [30. 로봇 간 협업·물리적 인계](categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md) | published | medium | 2026-09-25 | 2 |
| [31. 사람–로봇 협업](categories/execution-collaboration-and-recovery/human-robot-collaboration.md) | published | medium | 2026-09-25 | 2 |
| [32. 예외 복구·재계획·업무 연속성](categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) | published | medium | 2026-09-25 | 2 |

**I. 설계·시뮬레이션**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md) | published | low | 2026-09-30 | 2 |
| [34. 시뮬레이션·예측용 디지털 트윈](categories/design-and-simulation/simulation-and-predictive-digital-twin.md) | published | medium | 2026-09-25 | 2 |
| [35. 처리능력·규모·배치 설계](categories/design-and-simulation/capacity-sizing-and-layout-design.md) | published | medium | 2026-09-25 | 2 |
| [36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) | published | medium | 2026-09-30 | 2 |

**J. 현장 운영·관제**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [37. 관제 화면·실행 기록](categories/field-operations-and-monitoring/control-screen-and-execution-records.md) | published | low | 2026-09-30 | 2 |
| [38. 모니터링·이상 탐지·원인 분석](categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) | published | low | 2026-09-25 | 2 |
| [39. 운영 성과 측정·개선](categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) | published | medium | 2026-09-26 | 3 |
| [40. 운영 절차·요청 창구](categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) | published | medium | 2026-09-30 | 2 |

**K. 플랫폼 아키텍처·인프라**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) | published | low | 2026-09-30 | 2 |
| [42. 분산 시스템·통신·컴퓨팅 구조](categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) | published | low | 2026-09-25 | 2 |
| [43. 데이터·관측성·배포](categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) | published | low | 2026-09-30 | 2 |

**L. AI·학습 기술**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [44. 로봇 기반 모델·언어 모델 계획](categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) | published | medium | 2026-09-30 | 2 |
| [45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md) | published | medium | 2026-09-30 | 2 |
| [46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md) | published | medium | 2026-09-30 | 2 |
| [47. AI·학습·적응과 모델 운영](categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) | published | medium | 2026-09-25 | 2 |

**M. 안전**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [48. 안전·위험 관리](categories/safety/safety-and-risk-management.md) | published | medium | 2026-09-26 | 3 |
| [49. 사람 근접 안전](categories/safety/human-proximity-safety.md) | published | medium | 2026-09-30 | 2 |
| [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md) | published | medium | 2026-09-30 | 2 |

**N. 보안·개인정보**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [51. 인증·권한·격리](categories/security-and-privacy/authentication-authorization-and-isolation.md) | published | medium | 2026-09-25 | 2 |
| [52. 통신 보호·위협 관리·감사](categories/security-and-privacy/communication-protection-threat-management-and-audit.md) | published | medium | 2026-09-30 | 2 |
| [53. 개인정보·영상 데이터](categories/security-and-privacy/privacy-and-video-data.md) | published | medium | 2026-09-30 | 2 |

**O. 검증·도입·수명주기**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [54. 시험·형식 검증·벤치마크](categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) | published | medium | 2026-09-25 | 2 |
| [55. 현장 조사·설치·시운전](categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) | published | medium | 2026-09-25 | 2 |
| [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) | seed | — | 2026-09-28 | 1 |
| [57. 자산·소프트웨어 수명주기 관리](categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) | published | medium | 2026-09-25 | 2 |

**P. 거버넌스·법규·사회**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [58. 다사업자 책임·계약·데이터](categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) | seed | — | 2026-09-28 | 1 |
| [59. 법·규제·보험·라이선스](categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) | seed | — | 2026-09-28 | 1 |
| [60. 노동·수용성·접근성](categories/governance-law-and-society/labor-acceptance-and-accessibility.md) | seed | — | 2026-09-28 | 1 |

**Q. 현장 유형별 적용**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [61. 물류창고](categories/site-type-applications/warehouse.md) | published | medium | 2026-09-29 | 2 |
| [62. 제조 공장](categories/site-type-applications/manufacturing-plant.md) | published | medium | 2026-09-29 | 2 |
| [63. 병원·의료](categories/site-type-applications/hospital-and-healthcare.md) | published | medium | 2026-09-29 | 2 |
| [64. 상업 시설](categories/site-type-applications/commercial-facilities.md) | published | medium | 2026-09-29 | 2 |
| [65. 가정·공동주택](categories/site-type-applications/home-and-apartment.md) | published | medium | 2026-09-29 | 2 |
| [66. 실외](categories/site-type-applications/outdoor.md) | published | medium | 2026-09-30 | 2 |
| [67. 기타 현장](categories/site-type-applications/other-sites.md) | published | medium | 2026-09-30 | 2 |

### 검증 통과율

- 실행 123회 중 최종 통과 121회 (통과율 98%)
- 1차 검증 판정: 조건부 승인 121, None 2
- 2차 검증 판정: 통과 121, None 2

### 반려·보류 건수

- 1차 반려 0건, 2차 불통과·재검증 0건
- 보류(runs/parked) 4건

### 출처 유형 분포

| 유형 | 건수 |
|---|---|
| 논문 | 513 |
| 오픈소스 문서 | 208 |
| 표준 | 175 |
| 기사 | 95 |
| 정부·연구기관 | 86 |
| 벤더 문서 | 69 |
| 업계 보고서 | 21 |

신뢰도: medium 857건, high 215건, low 95건

### 현장 유형 매트릭스 채움률

- 63/119 칸 (53%) — [현장 유형 × 대분류 적용 사례 매트릭스](site-matrix.md)

### 마지막 갱신이 오래된 영역 상위 5

| 세부영역 | 마지막 갱신 | 경과일 | 상태 |
|---|---|---|---|
| [5. 로봇 능력·작업 표현](categories/robot-ontology/robot-capability-and-task-representation.md) | 2026-09-25 | 5 | published |
| [15. 지도·공간·위치 모델](categories/space-and-map-model/map-space-and-location-model.md) | 2026-09-25 | 5 | published |
| [17. 작업 대상·자산 식별과 인계 추적](categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) | 2026-09-25 | 5 | published |
| [18. 실시간 세계 상태·데이터 일관성](categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) | 2026-09-25 | 5 | published |
| [20. 로봇·제조사 관제 연동](categories/integration/robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 5 | published |
<!-- auto:metrics:end -->
