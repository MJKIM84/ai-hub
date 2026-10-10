---
title: "Open-RMF 이진 우선순위 비용과 마감·재계획 표현"
type: topic
category: "G. 계획·최적화"
primary_area_no: 26
related_areas: [25, 28, 23, 20, 39]
tags: [이진 우선순위, 비용 벌점, 누적 용량 제약, 마감, 온라인 재계획]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-125, ref-377, ref-379, ref-1407, ref-1408, ref-1403, ref-1409]
last_run: 2026-10-10
version: 1
---

[홈](../../index.md) › [주제](../index.md) › Open-RMF 이진 우선순위 비용과 마감·재계획 표현

# Open-RMF 이진 우선순위 비용과 마감·재계획 표현

**주 연구영역:** [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) · **관련 영역:** [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) · **실행:** 2026-10-10-03

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF rmf_task 의 이진 우선순위 비용 계산기는 마감을 검사하지 않고, 우선순위 검사가 켜져 있으면 우선순위 배분을 어긴 배정의 비용에 벌점 계수를 곱한다. [사실][^ref-1407]
- 이 위키의 판단(외부 조사 메모 기반)으로는 ROP 가 출하 마감이나 작업 간 선후를 지키려면 그 조건의 확장 계약과 집행 주체를 공통 요청 스키마 밖에서 따로 정해야 한다. [의견][^ref-125]
- 유형별 description 확장으로 마감·선후를 실제로 집행하는 구현과, 진행 중 작업을 재정렬하는 현장 설계는 확인하지 못했다. [추정][^ref-125]

## 2. 배경

이 글은 26. 작업 순서·스케줄링의 핵심 질문에서 출발했다.

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

세부영역 페이지 7절은 Open-RMF 이진 우선순위의 비용 반영 방식을 미확인으로 남겨 두었고, [열린 질문](../../open-questions.md) oq-019(출고 우선순위로 진행 중 작업 재정렬)와 oq-049(제조사가 다른 플릿 사이 작업 선후)가 답을 기다린다. 실행 2026-10-10-03 은 외부 조사 메모를 원문과 대조해 이 빈칸을 다시 확인했다.

## 3. 본문

### 이진 우선순위는 비용 벌점이다

rmf_task 의 이진 우선순위 체계는 낮은 우선순위를 nullptr, 높은 우선순위를 BinaryPriority(1) 로 만들고 BinaryPriorityCostCalculator 를 비용 계산기로 돌려준다. [사실][^ref-1408] 이 계산기는 두 경우를 위반으로 본다. 같은 계획 노드에서 한 로봇이 높은 작업을 2개 이상 받았는데 높은 작업이 없는 로봇이 있는 경우, 그리고 같은 로봇의 순서에서 충전 작업을 건너뛰고 보았을 때 낮은 작업 뒤에 높은 작업이 오는 경우다. [사실][^ref-1407] 우선순위 검사가 켜져 있고 배정이 위반이면 비용은 벌점 계수 × (g + h), 아니면 g + h 다. [사실][^ref-1407]

이 위키의 판단(외부 조사 메모 기반)으로는 이 처리가 납기를 직접 검사하는 코드가 아니므로 높은 우선순위를 마감 보장으로 해석하면 안 되고, 로봇 사이 배분 조건이 있어 단순한 선입선출 정렬로 설명해서도 안 된다. [의견][^ref-1407][^ref-125]

### 비용 계산기가 더하는 값

BinaryPriorityCostCalculator(작업 계획기 헤더 주석상 비용 계산기를 지정하지 않으면 쓰는 계산기[^ref-377])의 실비용 g 는 각 일반 작업의 (완료 시각 − 그 요청의 가장 이른 시작 시각)을 모든 로봇·모든 배정에 걸쳐 더한 값이다. [사실][^ref-1407] 충전 작업 배정 자체의 비용은 0 이다. [사실][^ref-1407] 다만 충전 때문에 같은 로봇의 뒤 작업 완료가 늦어지면 그 작업의 비용은 커질 수 있을 것으로 보인다. [추정][^ref-1407] 이 계산기가 Open-RMF 계획기의 목적 전체를 대표하는지는 확인하지 못했다. 이 위키의 판단(외부 조사 메모 기반)으로는 이 비용을 Dai 외가 최소화하는 메이크스팬(Makespan)이나 납기 지연 합과 같은 지표라고 부르면 안 된다. [의견][^ref-1407][^ref-1409]

### 마감과 용량을 제약으로 표현하기

OR-Tools CP-SAT 스케줄링 문서는 구간 변수, 선택 구간, 구간 사이 시간 관계, 겹침 금지에 더해 구간별 수요의 합이 용량 프로필을 넘지 않게 하는 누적 용량(Cumulative) 제약을 다룬다. [사실][^ref-379] 이 표현으로 ‘이전 작업 종료 뒤 시작’, ‘도크는 한 번에 한 작업’, ‘작업대 동시 사용량은 용량 이하’를 서로 다른 제약으로 쓸 수 있을 것으로 보이나, 문서의 예제는 로봇·도크 사례가 아닌 일반 스케줄링 예제다. [추정][^ref-379] Tuck 외(2024)의 동적 작업 배정 정식화는 내려놓기 동작이 마감 전에 일어나야 작업을 완료한 것으로 보아 마감을 필수 조건으로 둔다. [사실][^ref-1403] 이 위키의 판단(외부 조사 메모 기반)으로는 마감을 반드시 지킬 조건으로 둘지 어겼을 때 비용을 주는 조건으로 둘지를 목적함수와 제약식으로 나눠 설계해야 한다. [의견][^ref-379][^ref-1403]

### 진행 중 동작을 고정하는 재계획

Tuck 외는 새 작업이 들어올 때 각 로봇의 과거 동작과 현재 동작을 바꾸지 않은 채 계획을 갱신하도록 정의한다. [사실][^ref-1403] 이를 참고하면 긴급 작업 삽입 정책을 ‘현재 동작 고정’과 ‘아직 실행하지 않은 구간의 재배열’로 나눠 기술할 수 있을 것으로 보이나, 이동 시간이 불확실한 조건의 실행 성능 보장으로 넓히지는 않는다. [추정][^ref-1403]

## 4. 현장 시나리오

**현장 유형:** 물류창고

**사례:** 출하 마감이 임박한 주문을 이진 우선순위 요청으로 끼워 넣기(피킹 → 출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 출하 마감이 임박한 주문을 내린다. Open-RMF 공통 요청 스키마로는 가장 이른 시작 시각과 우선순위를 줄 수 있지만 마감 시각 필드는 없다. [사실][^ref-125] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 한 플릿의 로봇들. 우선순위 검사가 켜져 있으면, 높은 작업이 한 로봇에 2개 이상 몰리고 높은 작업이 없는 로봇이 있을 때 배정 비용에 벌점이 붙는다. [사실][^ref-1407] |
| 제약 | 도크·작업대 동시 사용량은 누적 용량 제약으로 쓸 수 있을 것으로 보인다. [추정][^ref-379] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 긴급 주문이 들어오면 현재 동작은 고정하고 아직 실행하지 않은 구간만 재배열하는 정책으로 나눠 기술할 수 있을 것으로 보인다. [추정][^ref-1403] |

다음은 설명을 위한 가상의 사례이다. 이 영역이 관여하는 칸은 제약과 예외·성과다. 이 위키의 판단(외부 조사 메모 기반)으로는 마감이 실제로 지켜지는지는 우선순위 값이 아니라, 마감을 제약으로 표현하고 집행하는 주체가 있는지에 달려 있다. [의견][^ref-125][^ref-1407]

## 5. ROP 관점의 시사점

**직접 범위:**
- 상위 시스템에서 받은 출하 마감·작업 선후를 Open-RMF 공통 요청 스키마 밖의 확장 계약으로 정의하고 집행 주체를 명시하는 일이 ROP 쪽에 남는다는 것이 이 위키의 판단(외부 조사 메모 기반)이다. [의견][^ref-125]
- 긴급 작업 삽입 규칙은 ‘현재 동작 고정’과 ‘미실행 구간 재배열’로 나눠 정할 수 있을 것으로 보인다. [추정][^ref-1403]

**연계 범위:**
- 연계 대상: 출하 마감 시각 자체의 결정은 분류 원문 19장의 상위 업무 시스템 경계(WMS 등)에 속한다. [추정][^ref-125]

## 6. 연결되는 연구영역

- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 이 글의 출발 영역이며, 7절 BinaryPriorityScheme 행과 11절 열린 질문을 보강한다.
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 이진 우선순위 벌점이 로봇 사이 높은 작업 배분을 조건으로 삼는다.
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 충전 작업의 비용과 뒤 작업 지연을 다룬다.
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 출하 마감을 상위 시스템에서 받는 쪽이다(oq-019).
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플릿별 우선순위 스키마와 플릿 사이 선후(oq-049)를 다룬다.
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 완료 시각 합·납기 지연 합·메이크스팬 같은 지표를 구분한다.

## 7. 열린 질문

- **oq-019** (상태: 열림) 출고 우선순위로 진행 중 작업을 재정렬하는 공개 설계나 사례 — 3절의 이진 우선순위 표현·벌점은 부분 근거일 뿐이며 재정렬 현장 설계는 찾지 못했다는 것이 이 위키의 판단(외부 조사 메모 기반)이다. [의견][^ref-1407][^ref-1408]
- **oq-049** (상태: 열림) 제조사가 다른 플릿 사이 작업 선후의 표준 필드나 공개 구현 — 공통 요청 스키마에는 선행 작업 ID 가 없고 유형별 description 확장 경로만 있어, 이 경로만으로 선후 집행이 구현되었다고 볼 수 없다. [추정][^ref-125]
- 새 질문 3건(상태: 열림): 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책, 제조사별 완료 시간 오차를 고려한 출하 마감 여유 시간, 작업 완료 시각 합·납기 지연 합·계획 변경량의 현장별 가중치 검증(관련 기존 질문: oq-054, oq-051). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 8. 출처

[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-10
[^ref-377]: Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp, 접근일 2026-10-10
[^ref-379]: Google (google/or-tools GitHub), OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver), 미확인, https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md, 접근일 2026-10-10
[^ref-1407]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp, 접근일 2026-10-10
[^ref-1408]: Open Robotics (open-rmf), rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 미확인, https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp, 접근일 2026-10-10
[^ref-1403]: Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America), SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, https://arxiv.org/html/2403.11737v1, 접근일 2026-10-10
[^ref-1409]: Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682), Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025-01-27, https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf, 접근일 2026-10-10 (원문 미열람)

## 9. 검증 노트

- 판정: 1차 조건부 승인 / 2차 대기
- 확인·미확인: 확인 27건 · 미확인 2건 · 교차 확인 0건
- 강등된 주장: f20 사실 → 일부 추정, f23 사실 → 추정
- 검증자 주의: 판정: 조건부 승인. 확인 27건, 미확인 2건, 교차 확인 0건(rmf_task 헤더·구현·스키마는 같은 프로젝트 자료라 독립 교차 확인으로 세지 않았다). 강등: f20 사실 → 일부 추정(연합 능력 조건·탐색·구조 모사 틀을 원문으로 대조하지 못함), f23 사실 → 추정(150 에이전트·500 작업·5종 능력 규모 수치 미확인). 원문 미열람 출처: ref-1409(Dai 외) — 검증 단계에서 PDF 텍스트를 뽑지 못했다. 실재와 서지(IEEE RA-L 10(3), 2025-01-27, DOI 10.1109/LRA.2025.3534682, 저자 5명)는 OpenAlex 로, 핵심 설정(필요한 로봇이 모두 모여야 시작, 메이크스팬 최소화, 휴리스틱·MIP 대비 두 자릿수 이상 빠름)은 초록 요약으로만 확인했다. ref-125·ref-377·ref-379 는 입력 원문 텍스트로, ref-1407·ref-1408·ref-1398 은 GitHub raw 로, ref-1403 는 arXiv HTML 로 원문을 대조했다. 브리프의 ref-1403·ref-1409 은 fetched: true 인데 fetch_url 이 null 이다(리서치 기록 누락). 주의: Open-RMF 비용 설명은 비용 계산기를 지정하지 않았을 때 쓰는 BinaryPriorityCostCalculator 에 한정된다. 같은 헤더의 TaskAssignmentStrategy(완료 시각·배터리·바쁨 가중치)와의 관계는 미확인이다. 이진 우선순위는 비용 벌점이며 마감 보장이 아니다. Tuck 외와 Dai 외는 계산 실험이고, 5절 '기타' 사례는 현장 실증이 아니다. 같은 URL 의 출처가 이전 실행(ref-1454, ref-1424·ref-1458)과 겹쳐 id 통일이 필요하다. 트랙 반영 제안 4건은 이번 브리프가 다루지 않아 반영하지 않고 다음 실행으로 넘긴다. 정정 요청 없음. 열린 질문 oq-019·oq-049 는 부분 근거만 추가하고 해결로 인정하지 않는다. 검증 검색 6회를 썼다.
- 신뢰도: medium

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-10-10 | 2026-10-10-03 | 신규 작성 | 1 |
