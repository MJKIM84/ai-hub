# 스토리텔러 산출 2026-09-25-34

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md | draft | 영역 심화: 섹션 3~11 신규 작성(4·6·8·11절은 주제 페이지로 분리), 2차 수정 지시 4건 반영(9절 경계 칸, 10절 태그, 5절 시작 조건·제약 칸) |
| create | docs/topics/2026/2026-09-25-area14-s6.md | draft | 자동 분리: 14. 작업 순서·스케줄링 의 "6. 대표 접근법과 기술" 절(1,504자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area14-s4.md | draft | 자동 분리: 14. 작업 순서·스케줄링 의 "4. 핵심 개념과 용어" 절(985자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area14-s8.md | draft | 자동 분리: 14. 작업 순서·스케줄링 의 "8. 대표 연구와 자료" 절(904자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area14-s11.md | draft | 자동 분리: 14. 작업 순서·스케줄링 의 "11. 열린 질문" 절(865자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 14. 작업 순서·스케줄링 | 영역 심화로 3~11절 초안 작성(신규 출처 15건, 재사용 6건). ref-678 은 2026-09-25-33 브리프의 ref-656 과 같은 URL(task.html)이라 중복 등록 가능성 있음 | run 2026-09-25-34
- 홈 최근 업데이트: 2026-09-25 — 14. 작업 순서·스케줄링: 주문 배치·선후 제약·피킹–포장 동기화·Open-RMF 일정 계획을 정리한 3~11절 초안 작성
- 대분류 최근 업데이트: 2026-09-25 — 14. 작업 순서·스케줄링: 3~11절 초안 작성(작업대 순서 최적화, 뒤 공정 기준 순서, 제약 프로그래밍, ROP 경계)
- 세부영역 최근 업데이트: 2026-09-25 — 14. 작업 순서·스케줄링: 영역 심화로 3~11절 신규 작성, 새 열린 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 주문 배치 | Order Batching | 여러 고객 주문을 한 번의 피킹 작업으로 묶어 이동·방문 횟수를 줄이는 창고 운영 결정이다. | 14 | ref-682 |
| new | 선후 제약 | Precedence Constraint | 한 작업이 끝나야 다른 작업을 시작할 수 있는 것처럼 두 작업의 실행 순서를 제한하는 조건이다. | 14, 15 | ref-691 |
| new | 시간창 | Time Window | 작업이 시작되거나 실행되어야 하는 가장 이른 시각과 가장 늦은 시각 사이의 허용 구간이다. | 14, 13 | ref-685 |
| new | 풋월 | Put Wall | 앞뒤로 열린 칸막이 선반으로, 한쪽에서 묶음 피킹한 물품을 주문별 칸에 넣고 반대쪽에서 완성된 주문을 꺼내 포장하는 주문 통합 설비이다. | 14 | ref-687 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-678 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-679 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |
| ref-680 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp |
| ref-681 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 오픈소스 문서 | high | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md |
| ref-682 | de Koster, R., Le-Duc, T., & Roodbergen, K. J. | Design and control of warehouse order picking: A literature review | 논문 | medium | https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/ |
| ref-683 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 |
| ref-684 | Boysen, N., de Koster, R., & Weidinger, F. | Warehousing in the e-commerce era: A survey | 논문 | medium | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ |
| ref-685 | Nunes, E., Manner, M., Mitiche, H., & Gini, M. | A taxonomy for task allocation problems with temporal and ordering constraints | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157 |
| ref-686 | Yang, X., Hua, G., Zhang, L., Cheng, T. C. E., & Choi, T. M. | Joint order assignment and picking station scheduling in KIVA warehouses with multiple stations | 논문 | medium | https://arxiv.org/abs/2108.09056 |
| ref-687 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2192437620300315 |
| ref-688 | Jiang, M., & Huang, G. Q. | Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175 |
| ref-689 | 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지) | 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116 |
| ref-690 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 |
| ref-691 | Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P. | Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks | 논문 | medium | https://arxiv.org/abs/2202.10449 |
| ref-692 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 논문 | medium | https://arxiv.org/abs/1705.10868 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 논문 | medium | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 논문 | medium | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? | 14, 13, 9 | 열림 | — |
| new | — | 로봇 작업대의 주문·랙 순서 최적화 연구가 보고한 로봇 대수·랙 방문 절감 효과를 이종 로봇과 사람 포장대가 섞인 국내 물류센터에서 검증한 자료가 있는가? | 14, 3 | 열림 | — |
| new | — | 피킹–포장 동기화의 성과를 포장 작업자 대기시간이나 주문 완료 시간 분산 같은 지표로 재는 합의된 정의가 있는가, ROP 가 순서 결정의 목적함수로 쓸 수 있는가? | 14, 4 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 피킹 | 작업 대상 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 피킹 | 수행 자원 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 피킹 | 제약 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 피킹 | 완료·인계 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 포장 | 수행 자원 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 포장 | 제약 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 포장 | 완료·인계 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 포장 | 예외·성과 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 출하 | 시작 조건 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |
| 출하 | 제약 | docs/categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 14. 작업 순서·스케줄링 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OR-Tools CP-SAT (스케줄링 레시피) | 오픈소스 | Google | 14 | ref-681 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md |
| Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) | 오픈소스 | Open Robotics (open-rmf) | 14, 13, 16 | ref-679 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp |

## 추가 조사 요청

- 6·8절: ref-686(Yang 외) 의 저널 게재판 게재지·판과 수치가 프리프린트와 같은지 확인이 필요하다(현재 기준일 arXiv 2021-08).
- 5절: ref-690(작업자 스케줄링, 2025)의 결과 수치가 미확인이라 포장 수행 자원 칸에 정책 효과를 쓰지 못했다.
- 9·11절: Open-RMF 가 우선순위(BinaryPriorityScheme)로 기존 배정을 재계획·재정렬하는지 소스 코드 확인이 필요하다(oq-019 관련).
- 9절: 플릿 안 일정 계획(제조사 관제·플릿 어댑터의 작업 순서 결정)을 ROP 직접 범위로 볼지 연계 대상으로 볼지 판단할 근거가 브리프에 없어 경계 표에 넣지 못했다.
- 3·8절: 긴급 주문 삽입·재스케줄링을 다룬 국내 학술 자료를 찾지 못했다. 한국어 검색 보강이 필요하다.
- 8절: 기계·AGV 동시 스케줄링 고전 연구(Ulusoy·Bilge)와 주문 배치 분류 검토(EJOR 2023)는 신규 출처 예산으로 넣지 못했다.
- 2026-09-25-33 의 ref-656 이 참고문헌에 등록되면 ref-678 과의 중복 정리가 필요하다(같은 task.html).

## 이행한 수정 지시

- f1 55% 출처·기준일 명시 — 3절 첫 문장에서 '2007년 문헌 검토가 추정한 값'이며 단일 출처 추정치·독립 교차 확인 없음을 밝혔다.
- f3·f4·f6 저자 실험 조건 — 3·6·8절의 로봇 대수·랙 방문·makespan·면적 감소 문장마다 '저자 (계산) 실험(원문 미열람, 독립 재현 미확인)'을 붙이고 일반화하지 않았다.
- f4 기준일 — 6·8절에서 'arXiv 프리프린트(2021-08) 기준'으로 적고 저널 게재판은 미확인이라고 밝혔다.
- f7 맥락 — 3·5·8절에서 편의점 물류센터 레이아웃 기준이었다는 점과 총 주문 처리 시간은 피킹 시간이 결정했다는 보고를 함께 적었다.
- f9 표현 — 6절에서 '잡숍 스케줄링'을 '스케줄링 문제'로 썼다.
- f11 인용 금지 — 6절에서 영문 구절 인용 없이 '이 위키의 추론'으로 [추정] 표기했다.
- ref-691 기관 — 각주와 reference_updates 의 기관을 Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P. 로 고쳤다.
- ref-678 중복 — 참고문헌 색인에 ref-656 이 없어 ref-678 로 등록하고 changelog_entry 에 같은 URL 중복 가능성을 적었다.
- f14·f15 중복 — 6절 Open-RMF 소절을 TaskPlanner 의 일정·시작 시각·충전 삽입 중심으로 쓰고 입찰 배정은 한 문장으로 줄여 13. 작업 배정 — MRTA 로 연결했다(10절 포함).
- f8 — 5절 수행 자원 칸 사례로만 짧게 쓰고 결과 수치는 '미확인'으로 두었다(8절 목록에는 넣지 않음).
- 원문 미열람 표시 — ref-006·ref-133·ref-134·ref-682~ref-691 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- 기존 각주 재사용 — f12·f13·f17·f20·f21·f22 에 ref-117·ref-125·ref-110·ref-134·ref-133·ref-006 을 그대로 썼다.
- oq-013·oq-019 — 11절에서 상태 '열림'을 유지하고 open_question_updates 로 해결 처리하지 않았다.
- 신뢰도 — 프런트매터 confidence 를 medium 으로 두었다.
- 분량 초과 자동 분리: 14. 작업 순서·스케줄링 본문 7,811자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,958자
- 2차: 9절 경계 칸 — '로봇 자체 지능·제어' 행 외부 연계 칸에서 '플릿 안 일정 계획과'와 [^ref-679]를 지우고 '연계 대상: 로봇의 주행·로컬 회피(분류 원문 9장 기준)'로만 두었다.
- 2차: 10절 태그 — '1. 주문·업무 시스템 연계' 항목을 '출고 우선순위·시작 시각을 상위 시스템에서 받는 쪽에 가까울 것으로 보인다(oq-019). [추정][^ref-125][^ref-688]'로 고쳤다.
- 2차: 5절 시작 조건 칸 — '표현할 수 있는 것은 …뿐이고 마감 시각 필드는 없다'를 '시각·순서 관련 필드로는 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후 필드는 없다'로 고치고 [사실][^ref-125]를 유지했다.
- 2차: 5절 제약 칸 — 첫 문장 각주를 [사실][^ref-683][^ref-687]로 바꿨다.
