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
| **물류창고** | 비어 있음 | 9 | 11 | 1 | 4 | 4 | 5 | 4 | 2 | 2 | 1 | 1 | 1 | 1 | 3 | 비어 있음 | 비어 있음 |
| **제조 공장** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |
| **병원** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |
| **상업 시설** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |
| **가정** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |
| **실외** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |
| **기타** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |

열 머리의 문자는 대분류다(A. 기획·사업, B. 로봇 온톨로지, C. 채팅 기반 구성·운영, D. 공간·지도 모델, E. 사물·사람·실시간 상태, F. 연동, G. 계획·최적화, H. 실행·협업·예외 복구, I. 설계·시뮬레이션, J. 현장 운영·관제, K. 플랫폼 아키텍처·인프라, L. AI·학습 기술, M. 안전, N. 보안·개인정보, O. 검증·도입·수명주기, P. 거버넌스·법규·사회, Q. 현장 유형별 적용). 아직 사례가 없는 칸은 "비어 있음"으로 표시한다. 채움률: 14/119 칸.

### 물류창고

- **B. 로봇 온톨로지**: [단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값](tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-02), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-01), [단계 4. 지도 변환 보정과 현장 정합](tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-04), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-02), [단계 5. 검증 방법과 가설 판정](tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-03), [5. 로봇 능력·작업 표현](categories/robot-ontology/robot-capability-and-task-representation.md#5-적용-사례-현장-유형-명시)
- **C. 채팅 기반 구성·운영**: [단계 3. 업무 지시 구현 가설 설계](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-01), [단계 3. 업무 지시 구현 가설 설계 — q3-04 지시 변경 반영](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-04), [단계 3. 업무 지시 구현 가설 설계](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-02), [단계 3. 업무 지시 구현 가설 설계 — q3-03](tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md#q3-03), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-01), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-01), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-02), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-02), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-03), [단계 4. 오해석 방지와 확인 절차](tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md#q4-04), [단계 5. 업무 지시 검증과 가설 판정](tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md#q5-03)
- **D. 공간·지도 모델**: [15. 지도·공간·위치 모델](categories/space-and-map-model/map-space-and-location-model.md#5-적용-사례-현장-유형-명시)
- **E. 사물·사람·실시간 상태**: [17. 작업 대상·자산 식별과 인계 추적](categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md#5-적용-사례-현장-유형-명시), [로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오), [로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인](topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md#4-현장-시나리오), [18. 실시간 세계 상태·데이터 일관성](categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시)
- **F. 연동**: [23. 업무 시스템 연동](categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시), [20. 로봇·제조사 관제 연동](categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시), [22. 설비·건물 시스템 연동](categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시), [21. 상호운용 표준·적합성](categories/integration/interoperability-standards-and-conformance.md#5-적용-사례-현장-유형-명시)
- **G. 계획·최적화**: [26. 작업 순서·스케줄링](categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시), [28. 공용 자원·충전·에너지 최적화](categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시), [24. 작업·워크플로 모델링](categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시), [25. 작업 배정 — MRTA](categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시), [27. 다중 로봇 경로·교통 관리 — MAPF](categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md#5-적용-사례-현장-유형-명시)
- **H. 실행·협업·예외 복구**: [30. 로봇 간 협업·물리적 인계](categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md#5-적용-사례-현장-유형-명시), [31. 사람–로봇 협업](categories/execution-collaboration-and-recovery/human-robot-collaboration.md#5-적용-사례-현장-유형-명시), [32. 예외 복구·재계획·업무 연속성](categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md#5-적용-사례-현장-유형-명시), [29. 명령·작업 실행의 신뢰성](categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md#5-적용-사례-현장-유형-명시)
- **I. 설계·시뮬레이션**: [35. 처리능력·규모·배치 설계](categories/design-and-simulation/capacity-sizing-and-layout-design.md#5-적용-사례-현장-유형-명시), [34. 시뮬레이션·예측용 디지털 트윈](categories/design-and-simulation/simulation-and-predictive-digital-twin.md#5-적용-사례-현장-유형-명시)
- **J. 현장 운영·관제**: [39. 운영 성과 측정·개선](categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md#5-적용-사례-현장-유형-명시), [38. 모니터링·이상 탐지·원인 분석](categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시)
- **K. 플랫폼 아키텍처·인프라**: [42. 분산 시스템·통신·컴퓨팅 구조](categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시)
- **L. AI·학습 기술**: [47. AI·학습·적응과 모델 운영](categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- **M. 안전**: [48. 안전·위험 관리](categories/safety/safety-and-risk-management.md#5-적용-사례-현장-유형-명시)
- **N. 보안·개인정보**: [51. 인증·권한·격리](categories/security-and-privacy/authentication-authorization-and-isolation.md#5-적용-사례-현장-유형-명시)
- **O. 검증·도입·수명주기**: [57. 자산·소프트웨어 수명주기 관리](categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [54. 시험·형식 검증·벤치마크](categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md#5-적용-사례-현장-유형-명시)

### 제조 공장

아직 이 현장 유형의 적용 사례가 없다.

### 병원

아직 이 현장 유형의 적용 사례가 없다.

### 상업 시설

아직 이 현장 유형의 적용 사례가 없다.

### 가정

아직 이 현장 유형의 적용 사례가 없다.

### 실외

아직 이 현장 유형의 적용 사례가 없다.

### 기타

아직 이 현장 유형의 적용 사례가 없다.
<!-- auto:site-matrix:end -->
