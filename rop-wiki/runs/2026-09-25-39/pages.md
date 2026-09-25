# 스토리텔러 산출 2026-09-25-39

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md | draft | 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 트랙 반영 제안 2건(경로망 자동 설계)을 6·8절에 반영 |
| create | docs/topics/2026/2026-09-25-area15-s6.md | draft | 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "6. 대표 접근법과 기술" 절(2,051자)을 옮겼다. 2차 수정: SIPP 가정 한계 문장을 [추정]으로 고쳐 썼다 |
| create | docs/topics/2026/2026-09-25-area15-s8.md | draft | 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "8. 대표 연구와 자료" 절(1,679자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area15-s7.md | draft | 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,155자)을 옮겼다. 형식 수정: 아직 참고문헌 페이지가 없는 ref-839·ref-833 링크를 텍스트 id 로 바꿨다 |
| create | docs/topics/2026/2026-09-25-area15-s4.md | draft | 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "4. 핵심 개념과 용어" 절(969자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area15-s3.md | draft | 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 의 "3. 왜 중요한가" 절(742자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 15. 다중 로봇 경로·교통 관리 — MAPF | 영역 심화: 3~11절 신규 작성, 트랙 반영 제안 2건(경로망 자동 설계)을 6·8절에 반영, 열린 질문 3건 추가 | run 2026-09-25-39
- 홈 최근 업데이트: 2026-09-25 — 15. 다중 로봇 경로·교통 관리 — MAPF: 영역 심화로 3~11절 신규 작성(MAPF 해법, Open-RMF·VDA 5050 교통 규칙, 교착 대응, 경로망 자동 설계)
- 대분류 최근 업데이트: 2026-09-25 — 15. 다중 로봇 경로·교통 관리 — MAPF: 영역 심화로 3~11절 신규 작성, 건축 도면 자동 인식 트랙의 경로망 자동 설계 반영 제안 2건 반영
- 세부영역 최근 업데이트: 2026-09-25 — 15. 다중 로봇 경로·교통 관리 — MAPF: 섹션 3~11 신규 작성(실행 2026-09-25-39)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 충돌 기반 탐색 | Conflict-Based Search (CBS) | 에이전트 쌍의 충돌로 이루어진 충돌 트리를 상위 단계에서 탐색하고 하위 단계에서는 에이전트 하나씩 경로를 다시 찾는 2단계 최적 MAPF 알고리즘이다. | 15 | ref-829 |
| new | 안전 구간 경로 계획 | Safe Interval Path Planning (SIPP) | 위치마다 충돌 없는 연속 시간 구간(안전 구간)을 두고 위치와 안전 구간의 쌍을 상태로 삼아 움직이는 장애물 사이 경로를 찾는 방법이다. | 15 | ref-837 |
| new | 우선순위 상속·되돌림 | Priority Inheritance with Backtracking (PIBT) | 매 시간 단계마다 에이전트에 우선순위를 주고 우선순위 상속과 되돌림으로 한 걸음씩 이동을 정하는 반복형 MAPF 방법이다. | 15 | ref-831 |
| new | 행동 의존 그래프 | Action Dependency Graph (ADG) | MAPF 계획에서 로봇들 사이 통과 순서를 의존 관계로 기록해, 실행 중 지연이 생겨도 그 순서를 지키며 충돌 없이 계획을 실행하게 하는 그래프이다. | 15 | ref-830 |
| new | 교착 | Deadlock | 여러 로봇이 서로 상대가 비켜 주기를 기다리며 아무도 진행하지 못하는 상태로, 좁은 통로·공유 구간에서 교통 관리가 탐지·예방·해소해야 한다. | 15, 9 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 논문 | medium | https://arxiv.org/abs/2005.07371 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 논문 | medium | https://arxiv.org/abs/1705.10868 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 논문 | medium | https://arxiv.org/abs/2511.07175 |
| ref-828 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 논문 | medium | https://arxiv.org/abs/1906.08291 |
| ref-829 | Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R. | Conflict-based search for optimal multi-agent pathfinding | 논문 | medium | https://dl.acm.org/doi/10.1016/j.artint.2014.11.006 |
| ref-830 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 논문 | medium | https://ieeexplore.ieee.org/abstract/document/8620328/ |
| ref-831 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 논문 | medium | https://arxiv.org/abs/1901.11282 |
| ref-832 | Yu, J., & LaValle, S. M. | Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity | 논문 | medium | https://arxiv.org/abs/1507.03289 |
| ref-833 | DiligentPanda (Team Pikachu, GitHub) | MAPF-LRR2023 — README (Team Pikachu's solution in the League of Robot Runners Competition 2023) | 오픈소스 문서 | medium | https://github.com/DiligentPanda/MAPF-LRR2023 |
| ref-834 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 논문 | medium | https://arxiv.org/abs/2609.10400 |
| ref-835 | IEEE 게재 논문 저자(미확인) | Hierarchical Traffic Management of Multi-AGV Systems With Deadlock Prevention Applied to Industrial Environments | 논문 | medium | https://ieeexplore.ieee.org/document/10132864/ |
| ref-836 | 전진표, 강재호, 류광렬, 김갑환, 윤항묵(한국항해항만학회지) | 자동화 컨테이너 터미널에서 AGV 교착 방지와 회귀 분석을 이용한 경로 선정 방안 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001130155 |
| ref-837 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 논문 | medium | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments |
| ref-838 | Ma, H., Koenig, S. 외 | Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios | 논문 | medium | https://arxiv.org/abs/1702.05515 |
| ref-839 | Open Robotics (open-rmf) | rmf_traffic — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic |
| ref-841 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2410.21415 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가? | 15, 9 | 열림 | — |
| new | — | 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? | 15, 23 | 열림 | — |
| new | — | 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? | 15, 14 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 15. 다중 로봇 경로·교통 관리 — MAPF |
| 피킹 | 수행 자원 | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 15. 다중 로봇 경로·교통 관리 — MAPF |
| 피킹 | 제약 | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 15. 다중 로봇 경로·교통 관리 — MAPF |
| 피킹 | 예외·성과 | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 15. 다중 로봇 경로·교통 관리 — MAPF |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) | 오픈소스 | Open Robotics (open-rmf) | 15, 9 | ref-839 | https://github.com/open-rmf/rmf_traffic |
| Open-RMF Traffic Editor | 오픈소스 | Open Robotics | 15, 6, 21 | ref-079 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) | 오픈소스 | DiligentPanda (Team Pikachu, GitHub) | 15, 23 | ref-833 | https://github.com/DiligentPanda/MAPF-LRR2023 |

## 추가 조사 요청

- 5절 완료·인계 칸: 교통 구간 통과의 완료를 무엇으로 확인하고 경로 해제·반납하는지(예: VDA 5050 베이스 해제 반납, Open-RMF 예정 경로 갱신) 근거가 필요하다 — 이번 브리프에 없어 '해당 없음'으로 두었다.
- 8절 국내 자료: ref-840(물류과학기술연구 MARL 트랜스포터 경로 계획)의 실재를 확인하지 못해 뺐다. 국내 물류센터 다중 AGV·AMR 교착·혼잡 경로 계획 연구를 추가 조사해야 한다.
- 9절: 승강기·문 같은 시설·설비 제어 경계에서 교통 관리(통과 예약·대기)가 어떻게 나뉘는지 근거가 있으면 경계 표에 행을 더할 수 있다.
- 11절 oq-032: 플릿 제어 수준(Full Control·신호등·읽기 전용)별 교통 성능·교착 발생을 측정한 연구 조사가 필요하다.
- 6절: 트랙 반영 제안의 '경로망은 보통 전문가가 수작업으로 설계한다'(ref-267) 서술은 출처 확인이 안 돼 싣지 않았다. 원문 확인 시 재검토한다.
- 6절(분리 페이지 s6): SIPP 의 즉시 출발·정지 가정이 실제 로봇 운동 제약과 어떻게 다른지 명시한 출처(SIPP 확장 연구 등)가 있으면 [사실]로 다시 쓸 수 있다.

## 이행한 수정 지시

- f24 삭제 — 본문 어디에도 싣지 않았고 ref-840 을 reference_updates·13절 각주·프런트매터 sources 에서 뺐으며, 8절 국내 자료는 f21(ref-836)만 썼다.
- 원문 미열람 표시 — ref-005·ref-006·ref-253·ref-267·ref-268·ref-828·ref-829·ref-830·ref-831·ref-832·ref-834·ref-835·ref-836·ref-837·ref-838·ref-841 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다(ref-253 summary 도 '원문 미열람'으로 시작하게 고침).
- 성능·순위 저자 보고 명시 — 6·8절에서 PIBT 속도(f4), Bonetti 처리량 우위(f19), GSRM 대비 1.2~23.4%(f23), SILLM 의 대회 우승 해법 추월(f25), WPPL 의 Overall Best 우승(f8)을 각각 '저자 보고'·'팀 자기 보고'로 적고 8절 머리에 이 위키가 확인한 성능이 아님을 밝혔다.
- f2 — '3-SAT 환원' 표현을 빼고 3·8절에서 '각 목적의 최적해 계산이 NP-hard 임을 보였다'까지만 썼다.
- f22 — 6·8절에 방법 서술만 반영하고 '경로망은 보통 전문가가 수작업으로 설계' 서술은 싣지 않았으며, 트랙 반영 제안 2건은 f22·f23 으로 6. 대표 접근법과 기술·8. 대표 연구와 자료에 반영한 것으로 처리했다.
- f20 — ref-835 각주의 저자를 '미확인'으로, 발행일을 '2023(검색 결과 기준)'으로 적고 reference_updates summary 에도 검색 결과 기준임을 밝혔다.
- f19·f21 — 6·8절에서 각각 대형·이종 AGV 공장 조건, 실외 자동화 컨테이너 터미널 조건임을 밝히고 물류센터 직접 적용 근거로 보지 않는다고 적었다.
- f18·f26·f27·f28·f29·f30 — [추정] 태그를 유지하고 문장에 '이 위키는 추정한다/추론한다'를 밝혔다. f28 시나리오는 5절에 확인된 현장 사례가 아닌 설명용 가상 시나리오임을 적었고, f27 은 9절에서 '연계 대상'으로 짧게 다루며 로컬 회피 책임을 명시한 문구를 찾지 못했음을 적었다.
- f16 — 4·7절에서 RELEASE·COORDINATED_REPLANNING·BLOCKED·SPEED_LIMIT 는 윤곽 기반 구역, DIRECTED/BIDIRECTED 는 운동 중심 기반 구역으로 구분해 썼다.
- f25 — 10절에서 27. AI·학습·적응과 모델 운영을 연결하고 학습 기반 경로 계획을 이 영역과 양쪽에 연결한다고 적었다.
- f30 — 10절에서 경로망 설계 평가용 MAPF 시뮬레이션을 22. 시뮬레이션·예측용 디지털 트윈으로만 연결하고 8. 실시간 세계 상태·데이터 일관성과 구분한다고 명시했다.
- 11절 — oq-032 를 열림으로 두고 f11 을 부분 근거로 연결했으며, 새 열린 질문 3건을 11절과 open_question_updates(new, 열림)에 등록했다.
- 직접 인용 제한 — VDA 5050(ref-031)·Open-RMF(ref-004·ref-079) 내용은 모두 재서술했고 출처 원문 직접 인용은 쓰지 않았다.
- 용어 후보 5건 — 충돌 기반 탐색·안전 구간 경로 계획·우선순위 상속·되돌림·행동 의존 그래프·교착을 glossary_updates 에 신규로 내고, PIBT 정의에서 '빠르게' 같은 성능 표현을 뺐다.
- 분량 초과 자동 분리: 15. 다중 로봇 경로·교통 관리 — MAPF 본문 9,348자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,617자
- 형식 검증 수정 — docs/topics/2026/2026-09-25-area15-s7.md 표의 출처 칸에서 아직 참고문헌 페이지가 없는 ref-839·ref-833 링크(../../references/ref-839.md, ../../references/ref-833.md)를 링크 없는 텍스트 id 로 바꿨다. 각주 정의·주장·태그는 바꾸지 않았다.
- 2차: SIPP 가정 한계 문장 드리프트 — docs/topics/2026/2026-09-25-area15-s6.md 3절 '최적 탐색: CBS와 SIPP' 소제목 아래 '이 가정은 실제 로봇의 가감속과 다르다는 점이 한계다. [사실][^ref-838]'를 '이 위키는 즉시 출발·정지 가정이 실제 로봇의 운동 제약과 다르다고 본다. [추정][^ref-837][^ref-838]'로 고쳐 썼다. 그 밖의 부분은 바꾸지 않았다.
