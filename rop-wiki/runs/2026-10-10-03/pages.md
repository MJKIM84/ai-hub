# 스토리텔러 산출 2026-10-10-03

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md | draft | 5절 시작 조건·제약 칸을 공통 최상위 스키마 범위로 한정하고 ‘기타’(계산 실험) 사례 추가, 6절에 이진 우선순위 비용 요약(우선순위 검사 조건 명시)과 새 주제 페이지 링크, 7절 작업 요청 스키마·BinaryPriorityScheme·OR-Tools 행 갱신과 rmf_fleet_adapter 2.14.0 행 추가, 8절 머리 문장에 기존 주제 페이지 링크를 넣어 한정하고 Tuck 외·Dai 외 추가, 11절 머리 문장에 기존 열린 질문 페이지 링크를 넣고 oq-019·oq-049 부분 근거와 새 질문 3건, 13절 각주 갱신 |
| create | docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md | draft | 신규 작성: Open-RMF 이진 우선순위 비용 벌점(우선순위 검사가 켜져 있을 때)과 비용 계산기 정의, 마감·누적 용량 제약 표현, 진행 중 동작을 고정하는 재계획(26. 작업 순서·스케줄링 6절 보강) |
| create | docs/topics/2026/2026-10-10-area26-s7.md | draft | 자동 분리: 26. 작업 순서·스케줄링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,369자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area26-s8.md | draft | 자동 분리: 26. 작업 순서·스케줄링 의 "8. 대표 연구와 자료" 절(1,194자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area26-s11.md | draft | 자동 분리: 26. 작업 순서·스케줄링 의 "11. 열린 질문" 절(931자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area26-s3.md | draft | 자동 분리: 26. 작업 순서·스케줄링 의 "3. 왜 중요한가" 절(722자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area26-s10.md | draft | 자동 분리: 26. 작업 순서·스케줄링 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(616자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-10 | 26. 작업 순서·스케줄링 | 5·6·7·8·11·13절 차등 갱신(이진 우선순위 비용 벌점 확인, 작업 요청 스키마 범위 한정, 계산 실험 사례 ‘기타’ 추가, rmf_fleet_adapter 2.14.0, Tuck 외·Dai 외 추가, 기존 주제 페이지 링크 유지), 주제 페이지 1건 신규 | run 2026-10-10-03
- 홈 최근 업데이트: 2026-10-10 — 26. 작업 순서·스케줄링: Open-RMF 이진 우선순위가 마감 보장이 아닌 비용 벌점(우선순위 검사가 켜져 있을 때)임을 확인하고, 마감·재계획 표현을 다룬 주제 페이지를 더했다
- 대분류 최근 업데이트: 2026-10-10 — 26. 작업 순서·스케줄링: 7절 BinaryPriorityScheme·작업 요청 스키마 행 갱신, 5절에 계산 실험 사례(현장 유형: 기타) 추가, 8절에 Tuck 외·Dai 외 추가
- 세부영역 최근 업데이트: 2026-10-10 — 26. 작업 순서·스케줄링: 5·6·7·8·11절 갱신과 주제 페이지 ‘Open-RMF 이진 우선순위 비용과 마감·재계획 표현’ 신규(6절에서 연결)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 메이크스팬 | Makespan | 작업 집합 전체를 끝내는 데 걸린 시간으로, 일정 최적화에서는 가장 늦게 끝나는 작업(또는 로봇)의 종료 시각을 줄이는 목적으로 쓰인다. | 26, 25, 39 | ref-379, ref-1486 |
| new | 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 정수·비트벡터 산술 같은 배경 이론 위에서 논리식을 만족하는 값이 있는지 판정하는 문제와 그 해법기로, 일정·배정 제약을 논리식으로 풀 때 쓴다. | 26, 25 | ref-1485 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-379 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 오픈소스 문서 | high | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md |
| ref-1483 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityCostCalculator.cpp |
| ref-1484 | Open Robotics (open-rmf) | rmf_task — rmf_task/src/rmf_task/BinaryPriorityScheme.cpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/src/rmf_task/BinaryPriorityScheme.cpp |
| ref-1485 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (UC Berkeley, Toyota Motor North America) | SMT-Based Dynamic Multi-Robot Task Allocation | 논문 | medium | https://arxiv.org/html/2403.11737v1 |
| ref-1486 | Dai, W., Rai, U., Chiun, J., Cao, Y., & Sartoretti, G. (IEEE Robotics and Automation Letters) | Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning | 논문 | medium | https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 이진 우선순위에서 높은 작업이 계속 들어올 때 낮은 작업의 무한 대기를 막는 공개 정책이 있는가? | 26, 25 | 열림 | — |
| new | — | 제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? | 26, 20 | 열림 | — |
| new | — | 작업 완료 시각 합, 납기 지연 합, 계획 변경량을 함께 최적화할 때 현장별 가중치를 어떻게 검증하는가? (관련 기존 질문: oq-054, oq-051) | 26, 39 | 열림 | — |
| update | oq-019 | 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | 23, 26 | 열림 | — |
| update | oq-049 | 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? | 20, 25, 26 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 시작 조건 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 |
| 물류창고 | 제약 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 |
| 기타 | 시작 조건 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님) |
| 기타 | 수행 자원 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님) |
| 기타 | 제약 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님) |
| 기타 | 예외·성과 | docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md#5-적용-사례-현장-유형-명시 | 26. 작업 순서·스케줄링 — 협업 작업 일정 계산 실험(현장 적용 사례 아님) |
| 물류창고 | 시작 조건 | docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오 | Open-RMF 이진 우선순위 비용과 마감·재계획 표현 |
| 물류창고 | 수행 자원 | docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오 | Open-RMF 이진 우선순위 비용과 마감·재계획 표현 |
| 물류창고 | 제약 | docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오 | Open-RMF 이진 우선순위 비용과 마감·재계획 표현 |
| 물류창고 | 예외·성과 | docs/topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md#4-현장-시나리오 | Open-RMF 이진 우선순위 비용과 마감·재계획 표현 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 26. 작업 순서·스케줄링 6·7절과 주제 페이지 3절: rmf_task TaskPlanner.hpp 의 작업 배정 전략(TaskAssignmentStrategy: 완료 시각·배터리·바쁨 가중치)과 BinaryPriorityCostCalculator 의 관계를 확인해야 한다 — 이번에는 비용 설명을 이 계산기에 한정했고 계획기 목적 전체로 일반화하지 못했다(1차 검증 지시).
- 26. 작업 순서·스케줄링 7절: BinaryPriorityCostCalculator 의 벌점 계수(priority_penalty) 기본값과 우선순위 검사(check_priority)가 기본으로 켜지는지를 헤더·계획기 코드에서 확인해야 한다 — 구현 파일에는 기본값이 없다.
- 26. 작업 순서·스케줄링 5·8절: Dai 외(2025, ref-1486) 원문 대조가 필요하다 — 연합 능력 벡터 합 조건, 실행 기간 내내 함께 있어야 한다는 조건, 탐색·구조 모사 실험 틀, 최대 150 에이전트·500 작업·5종 능력 규모 수치를 원문으로 확인하지 못해 [추정]으로 두었다.
- 26. 작업 순서·스케줄링 11절(oq-049): Open-RMF 의 다른 작업 유형 description 스키마(compose 등)에 마감·선행 작업 필드나 이를 집행하는 계획기 구현이 있는지 대조가 필요하다 — 이번에는 task_request.json 한 파일만 확인했다.
- 26. 작업 순서·스케줄링 5절: 물류창고 외 현장 유형(제조 공장·병원·상업 시설 등)의 실제 작업 순서·스케줄링 적용 사례가 필요하다 — 이번에 더한 ‘기타’ 사례는 계산 실험이다.
- 트랙 반영 제안 4건(실행 2026-09-25-51·66·77·98: HDDL 하위 작업 순서·VDA 5050 waitForTrigger, rmf_task 순서 계획과 LLM 직접 스케줄 생성 벤치마크, 재스케줄링 정책·방법 분류와 동결 구간, 재스케줄링 효율·안정성 지표)은 이번 브리프에 조사·검증한 finding 이 없어 6·7절에 반영하지 않았다 — 다음 26. 작업 순서·스케줄링 실행에서 조사·검증이 필요하며, AI 관련 내용은 47. AI·학습·적응과 모델 운영과 양쪽에 연결한다.
- 리서치 기록 보완: ref-1485·ref-1486 은 fetched: true 인데 fetch_url 이 null 이다(1차 검증 지적).
- 참고문헌 id 정리(퍼블리셔 담당): ref-1485 는 실행 2026-10-10-02 의 ref-1454 와, ref-1398 은 실행 2026-10-10-01 의 ref-1424·실행 2026-10-10-02 의 ref-1458 과 URL 이 같다. 이번 입력 docs_tree 에는 세 id 가 아직 게시되지 않아 이번 실행에서는 각 URL 을 한 번만 등록했으며, 먼저 게시된 id 로 합쳐 각주를 통일해야 한다.
- pipeline 담당 요청: 분량 초과 자동 분리가 원 절의 '자세한 내용은 주제 페이지 …' 같은 기존 링크 줄을 지운다(2차 검증 지적). 이번에는 링크를 머리 문장 안에 넣어 우회했으며, 분리 처리에서 기존 링크 줄을 보존하는지 확인이 필요하다.

## 이행한 수정 지시

- f20 분리 — 5절 ‘기타’ 사례 시작 조건 칸에 ‘필요한 로봇이 모두 작업 위치에 와야 시작하고 먼저 온 로봇의 대기를 줄이는 것이 목표’를 [사실]로, 연합 능력 벡터 합 조건을 [추정]+‘검증 단계에서 원문을 대조하지 못했다’로, 실행 기간 내내 동석 조건을 제약 칸에 [추정]+같은 병기로, 탐색·구조 모사 틀을 서술 단락에 [추정]+같은 병기로 나눠 썼다.
- ‘기타’ 사례 표기 — 5절 사례 제목을 ‘현장을 특정하지 않은 협업 작업 일정 계산 실험(Dai 외, 2025) — 현장 적용 사례가 아니다’로 쓰고 서술에 ‘계산 실험이며 특정 현장의 적용 사례가 아니다’를 밝혔으며, 탐색·구조는 [추정] 범위로만 언급했고 site_matrix_updates 의 기타 칸 제목에 ‘협업 작업 일정 계산 실험(현장 적용 사례 아님)’을 넣었다.
- f23 강등 — 5절 수행 자원·예외·성과 칸과 8절 Dai 외 항목을 [추정]으로 쓰고, 150 에이전트·500 작업·5종 능력은 ‘저자 보고이며 검증 단계에서 원문을 대조하지 못했다’, 휴리스틱·MIP 대비 결과는 ‘저자 실험, 독립 재현 미확인’으로 병기했다.
- f12 괄호 정의 제거 — 주제 페이지 3절과 용어집 정의에서 ‘차고지 복귀를 포함한…’ 정의를 빼고 ‘Dai 외가 최소화하는 메이크스팬’까지만 썼다.
- f9·f11·f12·f25 주어 한정 — 주제 페이지 3절의 비용 정의 주어를 ‘BinaryPriorityCostCalculator(작업 계획기 헤더 주석상 비용 계산기를 지정하지 않으면 쓰는 계산기)’로, 8절 f25 문장도 같은 계산기로 한정했고 ‘이 계산기가 Open-RMF 계획기의 목적 전체를 대표하는지는 확인하지 못했다’를 적었으며 TaskAssignmentStrategy 관계 확인은 additional_research_requests 로 넘겼다.
- 의견 주체 표시 — f4(5절 제약 칸·주제 1·5절), f8(7절 BinaryPriorityScheme 행·주제 3절), f16(주제 3절), f22(5절 ‘기타’ 서술), f25(8절), f27(7절 rmf_fleet_adapter 행), f28(11절·주제 7절)의 [의견] 문장마다 ‘이 위키의 판단(외부 조사 메모 기반)’을 넣었다.
- 7절 BinaryPriorityScheme 행 — 새 행 없이 기존 행의 ‘비용 반영 방식은 미확인’을 높음 BinaryPriority(1)·낮음 nullptr, 로봇 사이 배분·로봇 안 순서 위반 시 비용에 벌점 계수를 곱한다는 [사실]로 바꾸고 f8 을 [의견]으로 덧붙였으며, 출처 칸에 ref-390 을 유지하고 ref-1484·ref-1483(f8 근거 ref-125 포함)을 더했다.
- 작업 요청 스키마 범위 한정 — 7절 Open-RMF 작업 요청 스키마 행과 5절 물류창고 시작 조건 칸을 ‘공통 최상위 스키마(8개 필드, 필수 category·description)에 마감·선후 필드 없음, description·priority 는 플릿 지원 스키마에 위임’으로 고쳤고, 13절 ref-125 각주 접근일을 2026-10-10 으로 고쳤다.
- 8절 머리 문장 — ‘성능 수치는 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다’를 2026-09-25 주제 페이지의 기존 항목에 한정하고, Tuck 외는 arXiv 원문을 열어 확인했고 Dai 외는 검증 단계에서 원문을 대조하지 못했다는 구분 문단을 더했다.
- ref-1486 서지 — reference_updates 의 published 를 2025-01-27 로 고치고, 각주·요약에 IEEE Robotics and Automation Letters 10(3), 2654–2661, DOI 10.1109/LRA.2025.3534682 를 적었으며 ‘게재지 미확인’ 문구를 지웠다(검증 단계 원문 미대조라 source_unopened: true, 각주에 ‘(원문 미열람)’ 표시).
- 참고문헌 중복 — ref-1454·ref-1424·ref-1458 은 입력 docs_tree 에 게시되지 않아 이번에는 ref-1485·ref-1398 을 각 URL 당 한 번만 reference_updates 에 넣었고, 퍼블리셔가 같은 URL 을 먼저 게시된 id 로 합치도록 additional_research_requests 에 정리 요청을 적었다.
- 새 열린 질문 3번 — 질문 끝에 ‘(관련 기존 질문: oq-054, oq-051)’을 붙여 open_question_updates 와 11절·주제 7절에 썼다.
- 용어집 — 입력 용어집 색인에 ‘이론 모듈로 만족 가능성(SMT)’이 없어 신규로 냈고(같은 slug 면 퍼블리셔가 기존 항목으로 합침), ‘메이크스팬’ 정의는 ref-379·f12 범위 안에서 쓰고 차고지 복귀 같은 세부는 넣지 않았다.
- oq-019·oq-049 — 11절과 주제 7절에 부분 근거(f28 [의견], f29 [추정])만 덧붙이고 open_question_updates 에서 상태를 ‘열림’, link 는 null 로 두었다.
- 트랙 반영 제안 4건 — HDDL·VDA 5050 waitForTrigger·LLM 스케줄 벤치마크·재스케줄링 분류·안정성 지표를 6·7절에 넣지 않고 다음 26. 작업 순서·스케줄링 실행으로 넘기도록 additional_research_requests 에 적었으며, ‘27. AI·학습·적응과 모델 운영’은 개정 분류의 ‘47. AI·학습·적응과 모델 운영’으로 표기했다.
- 직접 인용 — ref-1483(BinaryPriorityCostCalculator.cpp)의 코드·주석은 직접 인용하지 않았고(0회), 비용식·검사 조건은 모두 재서술했다.
- 2차: 8절 기존 주제 페이지 링크 복원 — ‘8. 대표 연구와 자료’ replace 패치의 머리 둘째 문장을 ‘[2026-09-25 에 정리한 기존 항목](../../topics/2026/2026-09-25-area14-s8.md)은 성능 수치가 모두 저자 실험 결과이며 이 위키가 원문을 열지 못했다.’로 바꿔 링크를 문장 안에 넣었고, 자동 분리에서 지워지는 별도 ‘자세한 내용은…’ 줄은 뺐다.
- 2차: 11절 기존 열린 질문 페이지 링크 복원 — ‘11. 열린 질문’ 패치를 append 에서 replace 로 바꾸고 머리 둘째 문장을 ‘2026-09-25 까지의 질문은 [기존 열린 질문 정리](../../topics/2026/2026-09-25-area14-s11.md)에 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.’로 써서 링크를 문장 안에 넣었다(그 아래 2026-10-10 갱신 목록은 그대로).
- 2차: f7 조건 보강 — (1) 세부영역 6절 append 패치, (2) 주제 페이지 1절 첫 항목, (3) 주제 페이지 4절 수행 자원 칸, (4) 7절 BinaryPriorityScheme 행에 ‘우선순위 검사가 켜져 있으면’ 조건을 넣어 벌점 계수를 곱하는 진술을 한정했다.
- 분량 초과 자동 분리: 26. 작업 순서·스케줄링 본문 8,224자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,108자
