---
area: 26
title: "26. 작업 순서·스케줄링"
researched: 2026-10-10
researcher: "Codex (GPT-6)"
---

# 26. 작업 순서·스케줄링 — 보완 조사

## 요약
- Open-RMF에 마감·선후 필드가 없다는 주장을 공통 최상위 스키마 범위로 한정한다.
- 이진 우선순위가 비용에 반영되는 코드와 완료 시각 합·전체 종료 시각의 차이를 보충한다.
- 마감·공용 자원 용량·선택 작업을 표현하는 제약 모델과 진행 중 동작을 고정하는 재계획 연구를 추가한다.
- 2025년 이종 로봇 협업 일정 연구와 2026-09-26 수정 이력을 반영한다.

## 보완 항목

### 5. 적용 사례 (현장 유형 명시) — 수정
- 대상 문장(수정·교차 확인일 때): "긴급 주문을 Open-RMF 요청으로 보낼 때 시각·순서 관련 필드로는 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후 필드는 없다."
- 새 내용: Open-RMF `task_request.json`의 공통 최상위 필드에는 가장 이른 시작 시각과 우선순위가 있지만, 마감 시각이나 다른 작업 ID를 가리키는 선후 필드는 정의되어 있지 않다. [사실][^n1] 다만 `description`은 작업 유형별 스키마를 따르고 `priority`도 플릿이 지원하는 스키마를 따르므로, 공통 필드의 부재가 확장 구현의 불가능을 뜻하지는 않는다. [사실][^n1] 출하 마감·다른 작업 완료를 조건으로 쓰려면 그 확장 계약과 집행 주체를 별도로 명시해야 한다. [의견][^n1]
- 근거 메모: task_request.json 전체 `properties`와 `required`. `description`에 고정된 구조를 강제하지 않으며 최상위 `additionalProperties: false`도 없다. 단, 문법상 추가 필드를 넣을 수 있다는 것과 계획기가 실제로 그 필드를 집행한다는 것은 다르다.

### 7. 관련 표준·프레임워크·오픈소스 — 수정
- 대상 문장(수정·교차 확인일 때): "높음·낮음 두 단계 우선순위, 낮음은 현재 nullptr 반환. 비용 반영 방식은 미확인"
- 새 내용: `BinaryPriorityScheme`은 낮은 우선순위를 `nullptr`, 높은 우선순위를 우선순위 객체로 표현한다. [사실][^n3] `BinaryPriorityCostCalculator`는 우선순위 검사가 켜진 평가에서 낮은 작업 뒤에 높은 작업이 배치되는 경우 등을 조건 위반으로 보고 비용에 벌점 계수를 곱한다. [사실][^n2] 이는 납기 제약을 직접 검사하는 코드가 아니므로 높은 우선순위를 마감 보장으로 해석해서는 안 된다. [의견][^n1][^n2]
- 근거 메모: 7절 표의 BinaryPriorityScheme 설명을 대상으로 한다. BinaryPriorityScheme.cpp의 `make_low_priority()`·`make_high_priority()`; BinaryPriorityCostCalculator.cpp의 `valid_assignment_priority()`·`compute_cost(Node, time, check_priority)`. 플릿 사이 높은 작업 배분 조건도 있으므로 단순한 FIFO 정렬로 설명하지 않는다. 같은 프로젝트의 선언·구현 대조이며 독립 교차 검증은 아니다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: 이진 우선순위 비용 계산기의 기본 실비용은 각 일반 작업의 완료 시각에서 가장 이른 시작 시각을 뺀 값을 합산한다. [사실][^n2] 충전 작업 자체의 직접 비용은 0으로 계산하지만, 충전 때문에 다른 작업 완료가 늦어지면 그 작업의 비용은 커질 수 있다. [추정][^n2] 따라서 이 비용을 모든 작업 중 마지막 종료 시각인 메이크스팬(Makespan)이나 납기 지연 합과 같은 지표라고 부르면 안 된다. [의견][^n2][^n6]
- 근거 메모: `compute_g_assignment()`의 `finish_state.time - booking.earliest_start_time`, 충전 작업 분기, `compute_g()`의 합산. Dai 외 연구는 목적을 makespan으로 명시하므로 서로 다른 목적함수의 구체적인 대비가 된다. 사용자 지정 계산기를 선택한 경우까지 이 설명을 일반화하지 않는다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: OR-Tools의 제약 프로그래밍 기반 해법기(CP-SAT)는 구간 변수, 선택 구간, 선후 부등식, 겹침 금지(NoOverlap), 누적 용량(Cumulative) 제약을 제공한다. [사실][^n4] 이 표현을 이용하면 “이전 작업 종료 뒤 시작”, “도크는 한 번에 한 작업”, “작업대 동시 사용량은 용량 이하”를 서로 다른 제약으로 작성할 수 있다. [추정][^n4] 마감을 반드시 지킬 조건으로 둘지, 어겼을 때 비용을 주는 조건으로 둘지는 목적함수와 제약식을 나눠 설계해야 한다. [의견][^n4][^n5]
- 근거 메모: 공식 Scheduling recipes의 Interval variables, Optional intervals, Time relations between intervals, NoOverlap, Cumulative 절. Tuck 외 논문 Definition 6은 마감을 필수 완료 조건으로 둔다. 두 독립 자료는 시간 제약을 명시적으로 모델링하는 근거이며, OR-Tools가 즉시 사용할 수 있는 로봇 스케줄러라는 뜻은 아니다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: Tuck 외의 2024년 동적 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 연구는 새 작업이 도착했을 때 과거 동작과 현재 동작을 보존하는 갱신 계획을 정의한다. [사실][^n5] 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT)의 증분 풀이를 이용해 앞선 탐색 정보를 재사용하지만, 증분 방식의 시간 이득은 해법기와 인코딩에 따라 달랐다. [사실][^n5] 이를 참고하면 긴급 삽입 정책을 “현재 동작 고정”과 “미실행 구간 재배열”로 나눠 기술할 수 있다. [추정][^n5]
- 근거 메모: §3 Definition 9 Updated plan, §4.3 Incremental Solving, §6.2 RQ2. 새 작업마다 진행 중 물리 동작을 즉시 중단하는 방식이 아니다. 불확실한 현장 이동 시간을 포함한 실행 성능 보장으로 확대하지 않는다.

### 5. 적용 사례 (현장 유형 명시) — 추가
- 새 내용: 현장 유형은 탐색·구조를 모사한 협업 과제이며, Dai 외의 2025년 연구는 필요한 능력을 가진 모든 로봇이 도착해야 시작하는 작업을 모델링한다. [사실][^n6] 먼저 도착한 로봇은 나머지 팀원을 기다리고, 작업 동안 팀이 함께 머물러야 하므로 개별 로봇의 빠른 도착만으로 전체 종료 시간이 줄지는 않는다. [사실][^n6] 이 사례를 이용하면 도착 동기화, 공동 작업 시간, 다음 작업으로의 이동을 구분한 일정 설명을 추가할 수 있다. [의견][^n6]
- 근거 메모: 논문 §III 문제 정의의 능력 벡터·작업 시작 조건과 §IV 방법. 협업 조립도 동기 설명으로 등장하지만 상용 조립 현장의 검증 결과로 제시하지 않았다. 실제 창고의 피킹–포장 인계 구현과 동일하다고 주장하지 않는다.

### 8. 대표 연구와 자료 — 추가
- 새 내용: Dai 외는 강화학습(Reinforcement Learning, RL)으로 이종 로봇의 협업 일정을 정하고, 계산 실험에서 최대 150 에이전트·500 작업·5종 능력 조건을 다룬다. [사실][^n6] Open-RMF TaskPlanner API는 탐욕 방식은 최적성을 보장하지 않고 A* 방식은 더 긴 풀이 시간이 들 수 있다고 설명한다. [사실][^n8] 두 접근법은 목적·모델·평가 환경이 달라, 규모나 풀이 시간만으로 우열을 정하기보다 실행 가능한 일정 비율과 목적값을 같은 조건에서 비교하는 편이 좋다. [의견][^n6][^n8]
- 근거 메모: Dai 외 논문 실험 표 IV 및 대규모 실험 설명; TaskPlanner.hpp의 `Options(greedy, interrupter, finishing_request)` 주석. RL의 보고 성능은 해당 논문의 결과이며 Open-RMF와 직접 비교한 실험은 확인 못 함이다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가
- 새 내용: `rmf_fleet_adapter` 2.14.0의 2026-09-26 변경 이력은 단계 건너뛰기 요청 키 수정과 EasyTrafficLight의 누적 지연 계산 수정을 포함한다. [사실][^n7] 일정의 예외 조정과 지연 기반 추정에 의존하는 구현은 사용 패키지 버전을 함께 기록하는 편이 좋다. [의견][^n7]
- 근거 메모: 2.14.0 변경 이력 #543·#524. 2026-09-25 이후 변경이며, 이 수정이 새 납기 최적화 알고리즘이나 모든 진행 중 작업의 선점 기능을 제공한다는 뜻은 아니다.

## 답한 열린 질문
- 질문: "상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가?" → 부분 답변: 이진 우선순위의 표현과 비용 벌점 구현은 공개되어 있다. [사실][^n2][^n3] 납기·운송 마감을 이진 값으로 변환하고 진행 중 작업을 재정렬하는 현장 설계까지는 확인 못 했으므로 질문을 닫을 수 없다. [의견][^n1][^n2]
- 질문: "제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가?" → 부분 답변: 공통 task_request 스키마에는 선행 작업 ID가 없지만 유형별 `description` 확장 경로는 있다. [사실][^n1] 이 경로만으로 제조사 간 선후 집행이 구현되었다고 볼 수 없으며, 확인한 자료에서 범용 표준 필드와 완성된 공개 구현은 확인 못 함이다. [추정][^n1]

## 새로 생긴 열린 질문
- 이진 우선순위가 계속 높은 작업을 받는 상황에서 낮은 작업의 무한 대기를 막는 공개 정책이 있는가?
- 제조사별 예상 완료 시간의 오차를 고려해 마감 여유를 얼마나 두는가?
- 작업 완료 시간 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가?

## 출처
집계: 총 8개, 기존 영역·분리 주제 페이지 대비 새 출처 5개(n2·n3·n5·n6·n7), 원문 열람 8/8. 같은 프로젝트의 헤더와 구현 대조는 독립 교차 검증으로 세지 않았다.

[^n1]: Open-RMF, task_request.json, 발행일 미확인, [공식 스키마](https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json), 접근일 2026-10-10, 원문 열람.
[^n2]: Open-RMF, BinaryPriorityCostCalculator.cpp, 발행일 미확인, [비용·우선순위 구현](https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp), 접근일 2026-10-10, 원문 열람.
[^n3]: Open-RMF, BinaryPriorityScheme.cpp, 발행일 미확인, [우선순위 생성 구현](https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp), 접근일 2026-10-10, 원문 열람.
[^n4]: Google OR-Tools, Scheduling recipes for the CP-SAT solver, 발행일 미확인, [공식 스케줄링 문서](https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md), 접근일 2026-10-10, 원문 열람.
[^n5]: Victoria Marie Tuck 외, SMT-Based Dynamic Multi-Robot Task Allocation, 2024-03-18, [v1 논문 본문](https://arxiv.org/html/2403.11737v1), 접근일 2026-10-10, 원문 열람.
[^n6]: Weiheng Dai, Utkarsh Rai, Jimmy Chiun, Yuhong Cao, Guillaume Sartoretti, Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning, 2025(IEEE Robotics and Automation Letters), [저자 연구실 PDF](https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf), 접근일 2026-10-10, 원문 열람.
[^n7]: Open-RMF, rmf_fleet_adapter Changelog — 2.14.0, 2026-09-26, [태그 고정 변경 이력](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst), 접근일 2026-10-10, 원문 열람.
[^n8]: Open-RMF, TaskPlanner.hpp, 발행일 미확인, [공식 API 원문](https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp), 접근일 2026-10-10, 원문 열람.
