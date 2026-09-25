# 스토리텔러 산출 2026-09-25-49

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/index.md | draft | '다른 대분류와의 연결' 절 신규 작성: A·B·C·E·F·G 대분류와의 연결 34건(태그·각주), 근거 없는 연결 4건 명시, 절 끝 각주 정의. 2차 수정: 번호만 쓴 세부영역 호칭 2곳을 번호+이름으로 고침 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | D. 계획·최적화 | 다른 대분류와의 연결 절 신규 작성(A·B·C·E·F·G 대분류 연결, 근거 없는 연결 4건 명시, 1차 수정 지시 15건·2차 수정 지시 2건 이행) | run 2026-09-25-49
- 홈 최근 업데이트: 2026-09-25 — D. 계획·최적화: 다른 대분류와의 연결 절 신규 작성(A. 업무·공급망 설계~G. 안전·보안·지능·거버넌스와의 연결, 근거 없는 연결 4건 명시)
- 대분류 최근 업데이트: 2026-09-25 — D. 계획·최적화: 다른 대분류와의 연결 절 신규 작성(13. 작업 배정 — MRTA~16. 공용 자원·충전·에너지 최적화와 다른 대분류 세부영역의 연결, 27. AI·학습·적응과 모델 운영 교차 규칙 반영)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 플릿 제어 수준 | Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read-Only / No Interface) | Open-RMF 가 제조사 플릿과 연동하는 정도를 경로 지시까지 하는 전체 제어, 일시정지·재개만 하는 신호등, 상태만 받는 읽기 전용으로 나누고, 이 셋과 달리 연동할 수 없는 범주(No Interface)를 따로 구분한 것이다. | 9, 15 | ref-004 |
| new | 기반·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 로봇이 주행하도록 해제된 경로 구간(기반, 변경 불가)과 아직 해제되지 않아 주문 갱신으로 바꿀 수 있는 예정 구간(호라이즌)을 가리킨다. | 9, 12, 14 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 논문 | medium | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 논문 | medium | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2192437620300315 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 표준 | medium | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 논문 | medium | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 논문 | medium | https://ieeexplore.ieee.org/abstract/document/8620328/ |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2214716019300946 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 논문 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 논문 | medium | https://arxiv.org/abs/1906.08291 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2603.22731 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 논문 | medium | https://link.springer.com/article/10.1007/s10514-021-09997-2 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2410.21415 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 논문 | medium | https://arxiv.org/abs/2607.05683 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 의 우선(PRIORITY)·벌점(PENALTY) 구역 가중치를 출하 마감 같은 업무 우선순위와 연결해 ROP 가 설정하는 공개 설계나 사례가 있는가? (관련 기존 질문: oq-059) | 15, 1 | 열림 | — |
| new | — | 제조사가 다른 이동로봇이 배터리 건강(열화) 상태를 관제에 보고하는 표준 필드가 있어, 충전·배정 계획이 이를 공통으로 쓸 수 있는가? | 16, 24 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 다른 대분류와의 연결 절: 19. 모니터링·이상 탐지·원인 분석과 D. 계획·최적화 세부영역(예: 교착·지연 탐지가 재배정·재계획으로 이어지는 지점)을 잇는 검증된 근거가 없어 '아직 다루지 않은 연결'로 두었다.
- 다른 대분류와의 연결 절: 26. 사이버보안·접근권한·개인정보와 D. 계획·최적화(예: 배정·교통 협상 메시지의 인증·권한)를 잇는 근거가 없다.
- 다른 대분류와의 연결 절: 11. 분산 시스템·통신·컴퓨팅 구조(계획 계산 위치·지연)와 7. 화물·재고·자산 식별과 추적(배정 입력으로서의 화물 식별)과의 직접 연결 근거가 필요하다.
- 연결 전반: 모든 연결이 단일 출처·같은 발행 주체 근거라 교차 확인이 0건이다. 18. 사람–로봇 협업·운영 인터페이스, 20. 예외 복구·재계획·업무 연속성, 22. 시뮬레이션·예측용 디지털 트윈, 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스 페이지가 작성되면 상대편 근거로 교차 확인이 필요하다.

## 이행한 수정 지시

- 패치 대상 절 제목 — patches[].section 을 번호 없는 정본 H2 '다른 대분류와의 연결'로 썼다.
- f7·f29 조사 현황 분리 — B2MML Dependency1Type 정의와 MAPF 벤치마크 틀은 [사실] 문장으로, '창고 물류 적용 사례 미확인'·'현장 처리량으로 이어지는지 미확인'은 태그·각주 없는 별도 문장으로 쓰고 각각 oq-013·oq-058 에 연결했다.
- f20 분리 — E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 연결에서 연구 존재는 [사실][^ref-132], 로봇 배정이 작업자 배치와 맞물린다는 해석은 [추정][^ref-132]로 나눴다.
- f17·f24 범위 — 승강기 운행 제어·설비 안전 제어를 분류 원문 9장 시설·설비 제어 경계의 연계 대상으로 표기하고 ROP 는 세션 요청·운영 모드 확인과 작업·경로 제약 반영만 맡는다고 썼다.
- f18 범위 — 과충전 보호를 로봇 자체 지능·제어 경계의 연계 대상(로봇 책임)으로 쓰고 ROP 는 충전 주문과 충전 상태 확인만 맡는다고 썼다.
- f5·f9 한정 문구 — '저자 계산 실험(독립 재현 미확인)'과 '모델·시뮬레이션 조건의 저자 보고값이며 현장 실측이 아니다'를 수치와 같은 문장에 넣었다.
- ref-031 인용 — 페이지에 ref-031 원문 직접 인용을 두지 않고 f16·f18·f19·f25 내용을 모두 한국어로 재서술했다(다른 출처의 영어 발췌도 재서술).
- 원문 미열람 표시 — 지시된 26개 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- 27. AI·학습·적응과 모델 운영 교차 규칙 — f31~f33 항목에서 27. AI·학습·적응과 모델 운영 페이지와 13. 작업 배정 — MRTA, 15. 다중 로봇 경로·교통 관리 — MAPF, 16. 공용 자원·충전·에너지 최적화 페이지를 모두 링크했다.
- 8·22 구분 — f13 은 B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 연결(현재 상태 표현)로, f26·f27 은 F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈 연결(가정한 미래 실험)로 따로 쓰고 양쪽에 구분 문장을 두었다.
- 아직 다루지 않은 연결 — 7. 화물·재고·자산 식별과 추적, 11. 분산 시스템·통신·컴퓨팅 구조, 19. 모니터링·이상 탐지·원인 분석, 26. 사이버보안·접근권한·개인정보를 '근거 없음'으로만 나열하고 연결 문장을 쓰지 않았다.
- seed 안내 — 절 첫머리에 연결 상대 세부영역 페이지(18. 사람–로봇 협업·운영 인터페이스 등 아홉 곳)가 아직 작성되지 않아 E·F·G 대분류와의 연결이 D. 계획·최적화 쪽 근거에 기댄다는 문장을 두었다.
- A·B·C 겹침 — f1·f2·f4·f9·f10·f12·f14~f17·f19 를 해당 페이지와 같은 태그·같은 각주 id 로 쓰고, A·B·C 소제목마다 그 대분류 페이지의 '다른 대분류와의 연결' 절을 링크했다.
- 열린 질문 — PRIORITY·PENALTY 구역 가중치 질문 끝에 '(관련 기존 질문: oq-059)'를 덧붙여 open_question_updates 에 등록했다.
- 용어집 — '플릿 제어 수준' 정의에 Open-RMF 가 연동 불가 범주(No Interface)도 따로 구분한다는 점을 더했다.
- 2차: G. 안전·보안·지능·거버넌스 셋째 항목 굵은 머리 — '13·15·16 세부영역'을 '13. 작업 배정 — MRTA·15. 다중 로봇 경로·교통 관리 — MAPF·16. 공용 자원·충전·에너지 최적화'로 고쳤다.
- 2차: 첫 단락 둘째 문장 — '근거는 게시된 13~16 세부영역 페이지와'를 '근거는 게시된 위 네 세부영역 페이지와'로 고쳤고 나머지는 그대로 두었다.
