---
title: "환경 조건을 반영한 로봇 능력"
type: field-research
research: field-readiness-rop
related_areas: [4, 5, 6, 7, 18, 25]
tags: [능력 모델, 환경 조건, 조건부 능력, 검증 증거, 임시 제한, 온톨로지]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-030, ref-1577, ref-1578, ref-1579, ref-1590]
---

[홈](../../index.md) › [현장 적용·운영 검증](index.md) › 환경 조건을 반영한 로봇 능력

# 환경 조건을 반영한 로봇 능력

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

"이 로봇은 계단을 오른다"는 한 줄은 현장에서 충분하지 않다. 어느 계단을, 어떤 설정과 적재로, 어느 방향으로, 언제 확인했는지가 빠져 있기 때문이다. 이 페이지는 로봇 능력을 "가능 / 불가능" 하나로 두지 않고, 누가 무엇을 근거로 말했는지에 따라 나눠 기록하고 배정에 쓰는 방법을 제안한다.

## 1. 현장 문제

발표 관찰: 같은 로봇이 어떤 구간에서는 문제없이 다니고 다른 구간에서는 바닥 상태·조명·주변 물체 때문에 실패한 사례가 소개됐다. 계단에서는 이동 방향과 주변 물체가, 좁은 통로에서는 경로를 얼마나 엄격히 따를지가 언급됐다.

기존 위키의 [능력 온톨로지 초안](../../tracks/manual-capability-ontology/ontology-draft.md)은 6절에서 "로봇의 하드웨어·소프트웨어 구성 버전"과 "운용 구역·환경 조건"을 아직 반영하지 않은 질문으로 남겨 두었다. 아이디어가 없는 것이 아니라 상세 모델과 승인이 끝나지 않은 상태다. 열린 질문 oq-024는 제조사가 선언한 능력과 현장에서 관측한 능력이 다를 때 배정 기준을 묻는다([열린 질문](../../open-questions.md)).

## 2. 근거·적용 조건

**조건 아래의 운용 특성.** [사실] W3C SSN 온톨로지의 OperatingRange는 지정된 조건 아래에서 시스템의 정상 운용 특성을 표현한다("under some specified Conditions"). 이 개념은 SOSA 핵심이 아니라 ssn-system 모듈에 있다.[^ref-030] 센서 조건 어휘를 로봇 배정의 증거 모델로 잇는 것은 아래 3절의 제안이며, 표준이 이미 그런 배정 모델을 완성했다는 뜻이 아니다.

**제조사 SDK의 조건 관련 설정.** [추정] 벤더 주장: Spot SDK의 이동 명령에는 사용자가 주는 지면 마찰계수 힌트(ground_mu_hint)가 있다. 양수여야 하고 로봇이 범위를 제한할 수 있으며 주석상 권장 범위는 0.4~0.8, 기본값은 0.8이다. 계단 모드(StairsMode)는 trot 보행에서만 지원되고, 계단 오류 시 자동 하강을 끄는 필드가 따로 있다.[^ref-1577] [추정] 벤더 주장: 같은 SDK의 지도 정의에는 경로를 엄격히 따르는 모드(PATH_MODE_STRICT), 계단 하강 방향 선호(뒤로 선호·항상 뒤로·제약 없음, 값이 없으면 항상 뒤로 처리하고 제약 없음에는 전진 하강 시 넘어질 수 있다는 경고), 회피 시 허용 통로 폭의 절반을 뜻하는 필드(max_corridor_distance, 단위는 주석에 없음)가 있다.[^ref-1590]

**위치 상실 상태.** [추정] 벤더 주장: 같은 SDK 문서는 대부분 비어 있는 공간처럼 특징이 적은 곳에서 위치 추정이 어렵다고 설명하고[^ref-1578], 경로 실행 중 위치 상실(STATUS_LOST)과 막힘(STUCK) 같은 상태를 구분해 보고한다.[^ref-1579]

이 SDK 자료는 "그런 설정·상태가 정의돼 있다"는 데까지만 말한다. 마찰 힌트는 바닥을 실측한 마찰계수가 아니고, 설정이 미끄럼을 없앤다는 보장도 아니다. 모두 master 판 기준이며 특정 현장의 펌웨어·SDK 판에 같은 필드와 기본값이 있는지는 확인하지 못했다. 다른 제조사가 같은 개념을 어떻게 노출하는지도 이 자료로는 알 수 없다.

## 3. ROP 판단

[의견] 능력 하나를 세 종류의 주장으로 나눠 기록한다.

| 종류 | 기록할 것 | 효력 | 배정에서의 의미 |
|---|---|---|---|
| 제조사 선언 | 매뉴얼·SDK 판과 구절, 기종·옵션, 공식 한계, 지원 명령 | 제조사 새 문서가 나오면 새 버전으로 보존 | 후보 자격의 상한. 현장 성공의 증거가 아니다 |
| 현장 검증 | 기체·센서·도구·펌웨어·설정·지도 버전, 장소·시간·적재·환경, 성공·실패와 반복 횟수, 판정 기준, 로그 위치, 검토자 | 시험한 범위와 기간에 한정. 구성이 바뀌면 영향 검토 | 조건이 일치하는 승인 범위 안에서만 쓴다 |
| 임시 제한 | 금지 또는 조건부 허용, 이유, 발효·만료, 승인자, 구역·작업 범위 | 만료돼도 자동으로 성공 승인이 되지 않는다 | 허용 범위를 줄이는 운영 정책. 물리 능력 자체와 구별 |

[의견] 연결 모델의 최소 단위는 다음과 같다.

- **로봇 구성**: 기체·센서·도구·펌웨어·설정·적재 인터페이스의 식별자와 버전.
- **능력 주장**: 기능, 파라미터 범위, 전제·유지·사후 조건, 주장 종류(선언·검증·제한).
- **환경 조건**: 바닥·조명·재질·기하·무선·사람 밀도와 그 측정 방법·불확실성·측정 시각.
- **검증 증거**: 시험 절차 판, 실측·시뮬레이션·문서의 구분, 성공·실패 표본, 원문·로그 위치, 적용 구성, 검토 결과.
- **실패 유형**: 조건, 관측 증상, 원인 가설과 확정 수준, 복구 방법과 남은 제한.
- **배정 결정**: 작업 요구와 현재 조건의 대조, 근거 증거 id, 제외 사유, 승인자·시각.

[의견] 배정은 **선언 범위 ∩ 검증된 현장 범위 ∩ 현재 조건 ∩ 운영 허용 범위** 안에서만 제안한다. 측정하지 않았거나, 관측이 오래됐거나, 구성이 일치하지 않으면 "가능"도 "불가능"도 아닌 **확인 필요**로 남긴다.

## 4. 제조사·설비·운영자 역할

[의견] 제조사는 선언과 공식 한계, 설정의 의미(단위·기본값·부작용)를 문서로 제공한다. 현장 통합자는 현장 검증을 설계·수행하고 증거를 남긴다. 시설 담당은 환경 조건(바닥 상태, 조명, 공사)의 변화를 알린다. 운영자는 임시 제한을 걸고 해제한다. ROP는 이 네 출처를 섞지 않고 각각의 근거 id로 보관하며, 배정 근거를 사람이 읽을 수 있게 돌려준다.

## 5. 대응·판단 기준

[의견] 질의는 "후보 검색"과 "지금 실행 허용"을 나눠 답한다.

| 질의 | 돌려줄 것 |
|---|---|
| 계단 이동을 지원한다고 선언된 로봇은? | 기종, 매뉴얼 판, 계단 기능 종류, 공식 한계. 현장 허용 여부는 따로 표시 |
| 이 장소의 계단을 이 설정·적재로 지금 내려갈 수 있는가? | 그 장소·기하·방향·적재·펌웨어·설정과 일치하는 현장 시험, 현재 상태의 신선도, 임시 제한, 승인 유효기간 |
| 센서를 바꾼 뒤 기존 승인을 그대로 쓸 수 있는가? | 영향받는 검증 증거 목록과 재시험이 필요한 이유. 근거가 부족하면 "확인 필요" |
| 실패 기록이 없는 후보는 안전한가? | 관찰 횟수, 시험한 조건 범위, 시험하지 않은 영역. 실패가 없다는 것과 안전이 입증된 것을 구분 |

[의견] 구성이 바뀌면(센서 교체, 펌웨어 갱신, 그리퍼 변경) 그 구성을 쓴 현장 검증 증거의 효력을 자동으로 "검토 필요"로 바꾼다. 어떤 증거가 영향을 받는지는 구성과 증거를 잇는 기록이 있어야 계산할 수 있다.

## 6. 검증·한계

- 이 모델과 질의는 제안이다. 구현하거나 실행해 성능을 측정하지 않았고, 기존 능력 온톨로지 초안과 스키마를 바꾸지 않았다.
- 온톨로지가 논리적으로 정합해도 현장에서 성공한다는 뜻은 아니다. 형식 검증과 현장 실측은 서로 다른 증거다.
- SDK 필드의 존재는 확인했지만 발표 현장에서 실제로 쓴 판·값·효과는 확인하지 못했다.

## 7. 연결 영역

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md): 선언 능력과 운용 능력의 차이, 환경 조건.
- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md): 등록 관문과 구성별 증거, 버전이 바뀔 때 현장 승인에 미치는 영향.
- [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md): 능력 → 스킬 → 인터페이스. 측정하지 않았거나 만료된 조건에 "확인 필요"를 돌려주는 방식.
- [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md): 구성·환경 변경의 영향 분석과 재검증.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md): 현재 조건 관측의 신선도.
- 트랙: [능력 온톨로지 초안](../../tracks/manual-capability-ontology/ontology-draft.md) 6절, [평가 지표와 검증 절차](../../tracks/manual-capability-ontology/evaluation-and-verification.md), [질문 백로그](../../tracks/manual-capability-ontology/question-backlog.md)의 q4-04(실행 조건을 실행 시점 판단으로 넘기기), q5-05(광고 능력과 운용 능력의 차이 측정), q6-02(온톨로지 버전과 기종·펌웨어·어댑터 버전의 대응).

## 8. 남은 질문

- 이 장소·기체·설정·적재에서 이 작업이 가능한가를, 선언·검증·임시 제한을 나눠 근거와 함께 답할 수 있는가? (FR01, 관련 oq-024)
- 위치 상실을 어떤 상태로 알리고, 실제 위치를 확인하기 전에 위험 구역 진입을 어떻게 막는가? 제조사마다 다른 위치 신뢰도를 같은 기준으로 받는 방법은? (FR04, 관련 oq-028)
- 경로 엄격 추종·계단·마찰 설정이 현장에서 쓰는 SDK·펌웨어 판에서 정확히 어떤 단위·기본값·부작용을 갖는가? (FR15)

[^ref-030]: W3C / OGC, Semantic Sensor Network Ontology, 2017-10-19, https://www.w3.org/TR/vocab-ssn/, 접근일 2026-10-12
[^ref-1577]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/spot/robot_command.proto (master, blob 183f8fa), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/spot/robot_command.proto, 접근일 2026-10-12
[^ref-1590]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/graph_nav/map.proto (master, blob f37e496), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/graph_nav/map.proto, 접근일 2026-10-12
[^ref-1578]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_tech_summary.md (master, blob b92aad6), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_tech_summary.md, 접근일 2026-10-12
[^ref-1579]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_and_robot_locomotion.md (master, blob 1362051), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_and_robot_locomotion.md, 접근일 2026-10-12
