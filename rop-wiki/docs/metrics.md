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

영역별 페이지 상태 분포, 검증 통과율, 반려·보류 건수, 출처 유형 분포, 물류 흐름 매트릭스 채움률, 마지막 갱신이 오래된 영역을 퍼블리셔가 계산한다. 원천은 페이지 프런트매터(status, updated), `data/changelog.json`, `data/flow_matrix.json`, `runs/<run_id>/summary.json`, 참고문헌 페이지의 `source_type` 이다.

## 지표

<!-- auto:metrics:start -->
기준일: 2026-09-25

### 영역별 페이지 상태 분포

| 대분류 | seed | draft | verified | published | needs_update | deprecated | 합계 |
|---|---|---|---|---|---|---|---|
| [A. 업무·공급망 설계](categories/a-business-supply-chain-design/index.md) | 0 | 0 | 0 | 25 | 0 | 0 | 25 |
| [B. 공통 정보·환경 모델](categories/b-common-information-and-environment-model/index.md) | 0 | 0 | 0 | 25 | 0 | 0 | 25 |
| [C. 연결·실행 기반](categories/c-connectivity-and-execution-foundation/index.md) | 0 | 0 | 0 | 25 | 0 | 0 | 25 |
| [D. 계획·최적화](categories/d-planning-and-optimization/index.md) | 0 | 0 | 0 | 23 | 0 | 0 | 23 |
| [E. 협업·현장 운영](categories/e-collaboration-and-field-operations/index.md) | 0 | 0 | 0 | 24 | 0 | 0 | 24 |
| [F. 도입·검증·유지관리](categories/f-deployment-verification-and-maintenance/index.md) | 0 | 0 | 0 | 23 | 0 | 0 | 23 |
| [G. 안전·보안·지능·거버넌스](categories/g-safety-security-intelligence-and-governance/index.md) | 0 | 0 | 0 | 26 | 0 | 0 | 26 |

세부영역 페이지와 그 영역을 주 영역으로 하는 주제 페이지를 함께 센다.

**A. 업무·공급망 설계**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | published | medium | 2026-09-25 | 2 |
| [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) | published | medium | 2026-09-25 | 2 |
| [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | published | medium | 2026-09-25 | 2 |
| [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | published | medium | 2026-09-25 | 2 |

**B. 공통 정보·환경 모델**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | published | medium | 2026-09-25 | 2 |
| [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | published | medium | 2026-09-25 | 2 |
| [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | published | medium | 2026-09-25 | 4 |
| [8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) | published | low | 2026-09-25 | 2 |

**C. 연결·실행 기반**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | published | medium | 2026-09-25 | 2 |
| [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | published | medium | 2026-09-25 | 2 |
| [11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | published | low | 2026-09-25 | 2 |
| [12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | published | medium | 2026-09-25 | 2 |

**D. 계획·최적화**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md) | published | medium | 2026-09-25 | 2 |
| [14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | published | medium | 2026-09-25 | 2 |
| [15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | published | medium | 2026-09-25 | 2 |
| [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | published | medium | 2026-09-25 | 2 |

**E. 협업·현장 운영**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | published | medium | 2026-09-25 | 2 |
| [18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | published | medium | 2026-09-25 | 2 |
| [19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | published | low | 2026-09-25 | 2 |
| [20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | published | medium | 2026-09-25 | 2 |

**F. 도입·검증·유지관리**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | published | medium | 2026-09-25 | 2 |
| [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | published | medium | 2026-09-25 | 2 |
| [23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | published | medium | 2026-09-25 | 2 |
| [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | published | medium | 2026-09-25 | 2 |

**G. 안전·보안·지능·거버넌스**

| 세부영역 | 상태 | 신뢰도 | 마지막 갱신 | 버전 |
|---|---|---|---|---|
| [25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | published | medium | 2026-09-25 | 2 |
| [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) | published | medium | 2026-09-25 | 2 |
| [27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | published | medium | 2026-09-25 | 2 |
| [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | published | medium | 2026-09-25 | 2 |

### 검증 통과율

- 실행 78회 중 최종 통과 78회 (통과율 100%)
- 1차 검증 판정: 조건부 승인 78
- 2차 검증 판정: 통과 78

### 반려·보류 건수

- 1차 반려 0건, 2차 불통과·재검증 0건
- 보류(runs/parked) 14건

### 출처 유형 분포

| 유형 | 건수 |
|---|---|
| 논문 | 297 |
| 오픈소스 문서 | 176 |
| 표준 | 139 |
| 정부·연구기관 | 51 |
| 벤더 문서 | 39 |
| 기사 | 21 |
| 업계 보고서 | 6 |

신뢰도: medium 549건, high 125건, low 55건

### 물류 흐름 매트릭스 채움률

- 36/42 칸 (86%) — [흐름 매트릭스](flow-matrix.md)

### 마지막 갱신이 오래된 영역 상위 5

| 세부영역 | 마지막 갱신 | 경과일 | 상태 |
|---|---|---|---|
| [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 0 | published |
| [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) | 2026-09-25 | 0 | published |
| [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 0 | published |
| [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 0 | published |
| [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 0 | published |
<!-- auto:metrics:end -->
