---
title: "현장 유형 × 대분류 적용 사례 매트릭스"
type: matrix
status: published
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](index.md) › 현장 유형 × 대분류 적용 사례 매트릭스

# 현장 유형 × 대분류 적용 사례 매트릭스

행은 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타), 열은 대분류다. 각 칸의 숫자는 그 현장 유형의 적용 사례를 다룬 페이지 수이고, 아래 현장 유형별 목록에 링크가 있다. 스토리텔러 에이전트가 적용 사례를 쓸 때 현장 유형과 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과) 가운데 다룬 칸을 출력하고, 퍼블리셔가 `data/site_matrix.json` 에 반영해 이 표를 다시 그린다.

비어 있는 칸이 많은 현장 유형은 대상 선정에서 가산점을 받아 먼저 조사된다. 2026-09-28 개정 전 현장 유형 매트릭스의 칸은 모두 ‘물류창고’ 행으로 옮겼다. 방법 설명은 [연구 방법](about/research-method.md)에 있다.

## 매트릭스

<!-- auto:site-matrix:start -->
| 현장 유형 / 대분류 | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **물류창고** | 3 | 9 | 12 | 1 | 5 | 4 | 5 | 4 | 3 | 2 | 4 | 4 | 3 | 1 | 4 | 1 | 1 |
| **제조 공장** | 3 | 비어 있음 | 3 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 2 | 비어 있음 | 2 | 3 | 1 | 1 | 1 | 비어 있음 | 1 |
| **병원** | 2 | 3 | 5 | 2 | 2 | 비어 있음 | 비어 있음 | 비어 있음 | 2 | 2 | 3 | 1 | 1 | 2 | 1 | 2 | 1 |
| **상업 시설** | 2 | 비어 있음 | 1 | 비어 있음 | 1 | 비어 있음 | 비어 있음 | 비어 있음 | 1 | 1 | 비어 있음 | 1 | 비어 있음 | 비어 있음 | 1 | 비어 있음 | 1 |
| **가정** | 비어 있음 | 1 | 비어 있음 | 1 | 1 | 비어 있음 | 비어 있음 | 비어 있음 | 1 | 비어 있음 | 비어 있음 | 1 | 1 | 2 | 비어 있음 | 1 | 1 |
| **실외** | 1 | 비어 있음 | 2 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 1 | 비어 있음 | 비어 있음 | 1 | 2 | 1 | 비어 있음 | 2 | 1 |
| **기타** | 1 | 2 | 비어 있음 | 2 | 2 | 비어 있음 | 비어 있음 | 비어 있음 | 1 | 비어 있음 | 2 | 1 | 1 | 비어 있음 | 1 | 비어 있음 | 1 |

열 머리의 문자는 대분류다(A. 기획·사업, B. 로봇 온톨로지, C. 채팅 기반 구성·운영, D. 공간·지도 모델, E. 사물·사람·실시간 상태, F. 연동, G. 계획·최적화, H. 실행·협업·예외 복구, I. 설계·시뮬레이션, J. 현장 운영·관제, K. 플랫폼 아키텍처·인프라, L. AI·학습 기술, M. 안전, N. 보안·개인정보, O. 검증·도입·수명주기, P. 거버넌스·법규·사회, Q. 현장 유형별 적용). 아직 사례가 없는 칸은 "비어 있음"으로 표시한다. 채움률: 75/119 칸.

### 물류창고

- **A. 기획·사업**: [1. 기술·시장·업체 동향](categories/planning-and-business/technology-market-and-vendor-trends.md#5-적용-사례-현장-유형-명시), [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시), [3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시)
- **B. 로봇 온톨로지**: [단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값](tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-02), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-01), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-04), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-02), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-03), [5. 로봇 능력·작업 온톨로지](categories/robot-ontology/robot-capability-and-task-representation.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [단계 3. 업무 지시 구현 가설 설계](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-01), [단계 3. 업무 지시 구현 가설 설계 — q3-04 지시 변경 반영](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-04), [단계 3. 업무 지시 구현 가설 설계](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-02), [단계 3. 업무 지시 구현 가설 설계 — q3-03](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-03), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-01), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-01), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-02), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-02), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-03), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-04), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-03), [10. 채팅으로 로봇 구성](categories/chat-based-configuration-and-operation/chat-robot-configuration.md#5-적용-사례-현장-유형-명시)
- **D. 공간·지도 모델**: [6. 지도·공간·위치 모델](categories/space-and-map-model/map-space-and-location-model.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [7. 화물·재고·자산 식별과 추적](categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md#5-적용-사례-현장-유형-명시), [로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오), [로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인](topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md#4-현장-시나리오), [8. 실시간 세계 상태·데이터 일관성](categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시), [19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시)
- **F. 연동**: [1. 주문·업무 시스템 연계](categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시), [9. 로봇·제조사 관제 연동](categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시), [10. 설비·건물 시스템 연동](categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시), [28. 표준·상호운용성·다사업자 거버넌스](categories/integration/interoperability-standards-and-conformance.md#5-적용-사례-현장-유형-명시)
- **G. 계획·최적화**: [14. 작업 순서·스케줄링](categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시), [16. 공용 자원·충전·에너지 최적화](categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시), [2. 공정·워크플로 모델링](categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시), [13. 작업 배정 — MRTA](categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시), [15. 다중 로봇 경로·교통 관리 — MAPF](categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시)
- **H. 실행·협업·예외 복구**: [17. 로봇 간 협업·물리적 인계](categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md#5-적용-사례-현장-유형-명시), [18. 사람–로봇 협업·운영 인터페이스](categories/execution-collaboration-and-recovery/human-robot-collaboration.md#5-적용-사례-현장-유형-명시), [20. 예외 복구·재계획·업무 연속성](categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md#5-적용-사례-현장-유형-명시), [12. 명령·작업 실행의 신뢰성](categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md#5-적용-사례-현장-유형-명시)
- **I. 설계·시뮬레이션**: [3. 처리능력·거점·설비 계획](categories/design-and-simulation/capacity-sizing-and-layout-design.md#5-적용-사례-현장-유형-명시), [22. 시뮬레이션·예측용 디지털 트윈](categories/design-and-simulation/simulation-and-predictive-digital-twin.md#5-적용-사례-현장-유형-명시), [36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시)
- **J. 현장 운영·관제**: [4. 성과·경제성·프로세스 개선](categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md#5-적용-사례-현장-유형-명시), [19. 모니터링·이상 탐지·원인 분석](categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시)
- **K. 플랫폼 아키텍처·인프라**: [11. 분산 시스템·통신·컴퓨팅 구조](categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시), [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시), [43. 데이터·관측성·배포](categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시), [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결)
- **L. AI·학습 기술**: [27. AI·학습·적응과 모델 운영](categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [44. 로봇 기반 모델·언어 모델 계획](categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시), [46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시), [45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [25. 안전·위험 관리](categories/safety/safety-and-risk-management.md#5-적용-사례-현장-유형-명시), [49. 사람 근접 안전](categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시), [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [26. 사이버보안·접근권한·개인정보](categories/security-and-privacy/authentication-authorization-and-isolation.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [24. 자산·소프트웨어 수명주기 관리](categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [23. 시험·형식 검증·벤치마크](categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [21. 온보딩·설정·현장 시운전](categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md#5-적용-사례-현장-유형-명시), [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시)
- **P. 거버넌스·법규·사회**: [60. 노동·수용성·접근성](categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [61. 물류창고](categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시)

### 제조 공장

- **A. 기획·사업**: [1. 기술·시장·업체 동향](categories/planning-and-business/technology-market-and-vendor-trends.md#5-적용-사례-현장-유형-명시), [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시), [3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [8. 채팅으로 맵 작성](categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시), [10. 채팅으로 로봇 구성](categories/chat-based-configuration-and-operation/chat-robot-configuration.md#5-적용-사례-현장-유형-명시), [11. 채팅으로 실제 상황 시뮬레이션 재현](categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시)
- **I. 설계·시뮬레이션**: [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시), [36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시)
- **K. 플랫폼 아키텍처·인프라**: [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시), [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결)
- **L. AI·학습 기술**: [44. 로봇 기반 모델·언어 모델 계획](categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시), [46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시), [45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [52. 통신 보호·위협 관리·감사](categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [62. 제조 공장](categories/site-type-applications/manufacturing-plant.md#5-적용-사례-현장-유형-명시)

### 병원

- **A. 기획·사업**: [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시), [3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시)
- **B. 로봇 온톨로지**: [4. 이기종 로봇 등록](categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시), [6. 온톨로지 기반 시스템·로봇 연동](categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시), [7. 온톨로지 검증·변경 관리](categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [8. 채팅으로 맵 작성](categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시), [10. 채팅으로 로봇 구성](categories/chat-based-configuration-and-operation/chat-robot-configuration.md#5-적용-사례-현장-유형-명시), [11. 채팅으로 실제 상황 시뮬레이션 재현](categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시), [9. 채팅으로 시나리오 구성](categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시), [12. 채팅으로 업무 지시·오케스트레이션](categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시)
- **D. 공간·지도 모델**: [14. 도면·BIM에서 지도 만들기](categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시), [16. 장소 의미·지도 관리](categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시), [E. 사물·사람·실시간 상태](categories/objects-people-and-live-state/index.md#다른-대분류와의-연결)
- **I. 설계·시뮬레이션**: [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시), [36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시)
- **J. 현장 운영·관제**: [37. 관제 화면·실행 기록](categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시), [40. 운영 절차·요청 창구](categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시)
- **K. 플랫폼 아키텍처·인프라**: [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시), [43. 데이터·관측성·배포](categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시), [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결)
- **L. AI·학습 기술**: [46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [49. 사람 근접 안전](categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [52. 통신 보호·위협 관리·감사](categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시), [53. 개인정보·영상 데이터](categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시)
- **P. 거버넌스·법규·사회**: [58. 다사업자 책임·계약·데이터](categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시), [60. 노동·수용성·접근성](categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [63. 병원·의료](categories/site-type-applications/hospital-and-healthcare.md#5-적용-사례-현장-유형-명시)

### 상업 시설

- **A. 기획·사업**: [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시), [3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [13. 대화형 기능의 신뢰·기반](categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시)
- **I. 설계·시뮬레이션**: [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시)
- **J. 현장 운영·관제**: [40. 운영 절차·요청 창구](categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시)
- **L. AI·학습 기술**: [45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [64. 상업 시설](categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시)

### 가정

- **B. 로봇 온톨로지**: [7. 온톨로지 검증·변경 관리](categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시)
- **D. 공간·지도 모델**: [16. 장소 의미·지도 관리](categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [E. 사물·사람·실시간 상태](categories/objects-people-and-live-state/index.md#다른-대분류와의-연결)
- **I. 설계·시뮬레이션**: [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시)
- **L. AI·학습 기술**: [44. 로봇 기반 모델·언어 모델 계획](categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [52. 통신 보호·위협 관리·감사](categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시), [53. 개인정보·영상 데이터](categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시)
- **P. 거버넌스·법규·사회**: [58. 다사업자 책임·계약·데이터](categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [65. 가정·공동주택](categories/site-type-applications/home-and-apartment.md#5-적용-사례-현장-유형-명시)

### 실외

- **A. 기획·사업**: [2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [8. 채팅으로 맵 작성](categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시), [12. 채팅으로 업무 지시·오케스트레이션](categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시)
- **I. 설계·시뮬레이션**: [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시)
- **L. AI·학습 기술**: [45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [49. 사람 근접 안전](categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시), [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [53. 개인정보·영상 데이터](categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시)
- **P. 거버넌스·법규·사회**: [60. 노동·수용성·접근성](categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시), [59. 법·규제·보험·라이선스](categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [66. 실외](categories/site-type-applications/outdoor.md#5-적용-사례-현장-유형-명시)

### 기타

- **A. 기획·사업**: [1. 기술·시장·업체 동향](categories/planning-and-business/technology-market-and-vendor-trends.md#5-적용-사례-현장-유형-명시)
- **B. 로봇 온톨로지**: [4. 이기종 로봇 등록](categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시), [6. 온톨로지 기반 시스템·로봇 연동](categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시)
- **D. 공간·지도 모델**: [14. 도면·BIM에서 지도 만들기](categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시), [16. 장소 의미·지도 관리](categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시), [E. 사물·사람·실시간 상태](categories/objects-people-and-live-state/index.md#다른-대분류와의-연결)
- **I. 설계·시뮬레이션**: [36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시)
- **K. 플랫폼 아키텍처·인프라**: [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시), [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결)
- **L. AI·학습 기술**: [46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시)
- **M. 안전**: [50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md#5-적용-사례-현장-유형-명시)
- **Q. 현장 유형별 적용**: [67. 기타 현장](categories/site-type-applications/other-sites.md#5-적용-사례-현장-유형-명시)
<!-- auto:site-matrix:end -->
