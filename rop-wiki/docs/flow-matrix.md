---
title: "물류 흐름 매트릭스"
type: matrix
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](index.md) › 물류 흐름 매트릭스

# 물류 흐름 매트릭스

행은 원문 11장의 물류 흐름 7단계(입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품), 열은 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과)이다. 각 칸에는 그 단계·항목을 다룬 페이지의 링크를 두고, 아직 다룬 페이지가 없으면 "비어 있음"으로 표시한다. 스토리텔러 에이전트가 현장 시나리오를 쓸 때 다룬 칸을 출력하고, 퍼블리셔가 `data/flow_matrix.json` 에 반영해 이 표를 다시 그린다.

이 매트릭스는 기술 목록에 실제 물류 흐름을 교차해 보는 도구다. 채움률이 낮은 단계·항목은 대상 선정에서 가산점을 받아 먼저 조사된다. 방법 설명은 [SCM 관점의 연구 시작 방법](about/research-method.md)에 있다.

## 매트릭스

<!-- auto:flow-matrix:start -->
| 물류 단계 / 항목 | 시작 조건 | 작업 대상 | 수행 자원 | 제약 | 완료·인계 | 예외·성과 |
|---|---|---|---|---|---|---|
| **입고** | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) |
| **적치** | 비어 있음 | 비어 있음 | 비어 있음 | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | 비어 있음 | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) |
| **보충** | 비어 있음 | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | 비어 있음 | 비어 있음 | 비어 있음 |
| **피킹** | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | 비어 있음 | 비어 있음 |
| **포장** | 비어 있음 | 비어 있음 | 비어 있음 | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | 비어 있음 | 비어 있음 |
| **출하** | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시)<br>[로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오) | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시)<br>[로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인](topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md#4-현장-시나리오)<br>[로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오)<br>[2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시)<br>[로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인](topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md#4-현장-시나리오)<br>[로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오) | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시)<br>[로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인](topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md#4-현장-시나리오)<br>[로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오)<br>[2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시) | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시)<br>[로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가](topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오) |
| **반품** | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 | 비어 있음 |

아직 채워지지 않은 칸은 "비어 있음"으로 표시한다. 채움률: 21/42 칸.
<!-- auto:flow-matrix:end -->
