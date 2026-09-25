# 스토리텔러 산출 2026-09-25-55

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/index.md | draft | '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 아직 다루지 않은 연결에 7. 화물·재고·자산 식별과 추적 명시), '참고 자료' 끝에 새 각주 정의 38건 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | D. 계획·최적화 | '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 1차 수정 지시 14건 이행) | run 2026-09-25-55
- 홈 최근 업데이트: 2026-09-25 — D. 계획·최적화: '다른 대분류와의 연결' 절 신규 작성(여섯 대분류와의 연결, 7. 화물·재고·자산 식별과 추적은 근거 미확보로 표기)
- 대분류 최근 업데이트: 2026-09-25 — D. 계획·최적화: '다른 대분류와의 연결' 절 신규 작성(A. 업무·공급망 설계~G. 안전·보안·지능·거버넌스 연결, 새 각주 38건)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 플릿 제어 수준 | Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only) | Open-RMF 가 제조사 플릿과 연동하는 정도를 경로 지시까지 하는 전체 제어, 일시정지·재개만 하는 신호등, 상태만 받는 읽기 전용으로 나눈 구분이다. | 9, 15 | ref-004 |
| new | 기반·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 로봇이 주행하도록 해제되어 바꿀 수 없는 경로 구간(기반)과 아직 해제되지 않아 주문 갱신으로 바꿀 수 있는 예정 구간(호라이즌)을 가리킨다. | 9, 12, 14 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 논문 | medium | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 논문 | medium | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2192437620300315 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 표준 | medium | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 논문 | medium | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 논문 | medium | https://ieeexplore.ieee.org/abstract/document/8620328/ |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2214716019300946 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 논문 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 |
| ref-401 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 정부·연구기관 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 논문 | medium | https://arxiv.org/abs/1906.08291 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2603.22731 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 논문 | medium | https://link.springer.com/article/10.1007/s10514-021-09997-2 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2410.21415 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 논문 | medium | https://arxiv.org/abs/2607.05683 |
| ref-539 | Lott, J., & Honary, V.(University of San Diego) | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 논문 | medium | https://arxiv.org/abs/2609.13711 |
| ref-540 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 논문 | medium | https://arxiv.org/abs/2608.25690 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? | 13, 26, 19 | 열림 | — |
| new | — | 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? | 13, 11 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- '다른 대분류와의 연결' 절: 7. 화물·재고·자산 식별과 추적과 D. 계획·최적화(배정·순서 결정이 화물·운반구 식별과 재고 이벤트를 입력으로 쓰는지)를 잇는 근거가 브리프에 없어 '아직 다루지 않은 연결'로만 두었다
- 11. 분산 시스템·통신·컴퓨팅 구조 연결: ref-539(arXiv 2609.13711) 원문을 열어 통신 저하 조건별 배정기 안정성 결과를 확인해야 결과 문장을 쓸 수 있다(1차 검증에서 'ACBBA·PI·DGA 안정성 상실' 문구가 확인되지 않아 뺐다)
- 26. 사이버보안·접근권한·개인정보, 19. 모니터링·이상 탐지·원인 분석 연결: 물류센터 조건의 배정 보안·이상 로봇 제외 사례나 연구가 있으면 단일 프리프린트(ref-540) 의존을 줄일 수 있다
- 8. 실시간 세계 상태·데이터 일관성 연결: ref-051(VDA 5050 state.schema)의 배터리 상태 필드를 원문으로 다시 확인해야 f13 추정을 보강할 수 있다

## 이행한 수정 지시

- patches 절 이름 — section 을 대분류 정본 H2 '다른 대분류와의 연결'(번호 없음)로 썼고, 새 각주 정의 38건은 '참고 자료' 절에 append 로 덧붙여 기존 ref-005·ref-006 정의와 auto 마커(category-area-table·category-recent) 및 다른 절은 건드리지 않았다
- f21 강등 — 6종 분산 배정기를 통신 저하 조건에서 비교했다는 설계만 [사실]로 남기고 'ACBBA·PI·DGA 가 안정성이나 실행 가능성을 잃었다'는 문구는 삭제했다
- ref-031 직접 인용 — 이 절에서 VDA 5050 원문을 직접 인용하지 않고 범위 제외(f1)와 연결 끊김 규칙(f27)을 모두 재서술했으며, ref-004·ref-079·ref-376·ref-405·ref-104 도 직접 인용 없이 재서술했다
- ref-540·ref-539 서지 — ref-540 의 기관을 'Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)', 발행 2026-08 로 reference_updates 와 각주 정의에 같게 썼고, ref-539 는 'Lott, J., & Honary, V.(University of San Diego)', 2026-09 로 썼다
- 원문 미열람 표기 — fetched:false 인 27건의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, raw.githubusercontent.com 으로 연 11건에는 붙이지 않았다
- f28·f29·f31 — ref-540 이 GPS 스푸핑 데이터·택시 수요로 실험한 프리프린트이며 물류센터 적용이 확인되지 않았다는 점을 19. 모니터링·이상 탐지·원인 분석, 26. 사이버보안·접근권한·개인정보 항목 본문에 적고 f29·f31 은 [추정]을 유지했다
- f18·f38·f19 범위 — 승강기 운행·설비 안전 제어는 시설·설비 제어 경계, 과충전 보호는 로봇 자체 지능·제어 경계의 연계 대상으로 쓰고, ROP 는 승강기 세션 요청·운영 모드 확인, 충전 시작·중지 요청과 상태 확인만 맡는다고 서술했다
- f39 — VDA 5050 구역 유형을 교통 관리 수단으로만 쓰고 명세가 스스로 안전 표준이 아니라고 밝힌 점을 함께 적어, 25. 안전·위험 관리 연결을 교통 관리 수단과 안전 기능의 구분으로만 다뤘다
- f13·f32·f33 — 8. 실시간 세계 상태·데이터 일관성(현재 배터리 상태 표현)은 B. 공통 정보·환경 모델 항목에, 22. 시뮬레이션·예측용 디지털 트윈(배정 규칙·경로망을 가정한 미래에서 실험)은 F. 도입·검증·유지관리 항목에 서로 다른 문장으로 나누고 구분 문장을 덧붙였다
- f40·f41·f42 — 27. AI·학습·적응과 모델 운영 연결이 분류 원문 8장 교차 규칙(학습 기반 배차는 13. 작업 배정 — MRTA)에 따른 것임을 밝히고, LLM 배정 결과 수치는 출처 충돌(oq-030)로 쓰지 않는다고 적었다
- f5·f9·f36 — f5 에 저자 계산 실험·독립 재현 미확인, f9 에 모델·시뮬레이션 저자 보고값·현장 실측 아님·독립 재현 미확인을 병기했고, f36 의 계산 시간 수치는 넣지 않았다
- 중복 연결 — f4·f9·f10·f12·f11·f16·f18·f20 은 새 각주 없이 A·B·C 대분류 페이지와 같은 ref id(ref-134·ref-133·ref-146·ref-236·ref-079·ref-105·ref-004·ref-312·ref-031)와 같은 태그로 썼다
- '아직 다루지 않은 연결' 소제목에 7. 화물·재고·자산 식별과 추적을 번호와 이름, 링크로 명시했다
- 호칭 — 본문·도식·링크 텍스트에서 대분류는 문자와 이름('E. 협업·현장 운영'), 세부영역은 번호와 이름('19. 모니터링·이상 탐지·원인 분석')을 함께 쓰고 번호만의 호칭을 쓰지 않았다
