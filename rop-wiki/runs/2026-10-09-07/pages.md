# 스토리텔러 산출 2026-10-09-07

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/index.md | draft | '다른 대분류와의 연결' 절 작성: 다른 대분류 16곳과의 연결(finding 84건, 각주 63건), 아직 다루지 않은 연결 6개 영역 명시, 1차 조건부 승인 수정 16건 반영 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | I. 설계·시뮬레이션 | '다른 대분류와의 연결' 절 작성(다른 대분류 16곳, 각주 63건, 1차 조건부 승인 수정 16건 반영, 보류 실행 2026-10-09-04 대체) | run 2026-10-09-07
- 홈 최근 업데이트: 2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 작성(다른 대분류 16곳과의 연결, 연결 해석은 대부분 추정·단일 출처, 벤더 주장 4건 병기)
- 대분류 최근 업데이트: 2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 작성(33. 시나리오 모델·편집~36. 가상 시운전·실제 상황 재현과 다른 대분류 16곳의 연결, 아직 다루지 않은 연결 6개 영역 명시)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 슬롯카 모델 | Slotcar (Open-RMF simulated robot plugin) | Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물이 있으면 멈추는 단순화 로봇 모델로, 로봇마다 주행 스택을 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다. | 34, 20 | ref-406 |
| new | 대리 모델 | Surrogate Model | 시뮬레이션처럼 계산 비용이 큰 모델의 입력–출력 관계를 학습한 근사 모델로, 추가 시뮬레이션 없이 설계 공간의 성능·비용을 빠르게 예측하는 데 쓴다. | 35, 46 | ref-822 |
| new | 동기화 손실 | Synchronization Loss | 사람 작업자와 로봇이 함께 일하는 공정에서 한쪽이 다른 쪽을 기다리며 생기는 유휴 시간과 그 비용을 가리킨다. | 31, 35 | ref-822 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-833 | Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. | Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving | 논문 | medium | https://arxiv.org/abs/2607.14387 |
| ref-832 | Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P. | LLM Agents Perform Controlled Experiments Using Simulation Models | 논문 | medium | https://arxiv.org/abs/2608.23622 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 표준 | medium | https://www.asam.net/standards/detail/openscenario-xml/ |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 정부·연구기관 | medium | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html |
| ref-1127 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 논문 | medium | https://arxiv.org/abs/1912.06321 |
| ref-416 | Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv) | SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | 논문 | medium | https://arxiv.org/abs/2307.06135 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 오픈소스 문서 | medium | http://sdformat.org/ |
| ref-1314 | IDTA (Industrial Digital Twin Association, admin-shell-io/submodel-templates) | Provision of Simulation Models (IDTA 02005) 1.0 — README | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models |
| ref-1133 | NASA | NASA-STD-7009B Standard for Models and Simulations | 표준 | medium | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 논문 | medium | https://arxiv.org/abs/2312.09067 |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 논문 | medium | https://arxiv.org/abs/2409.12471 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2405896318316021 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 논문 | medium | https://arxiv.org/abs/2310.08710 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-1087 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 표준 | medium | https://www.iso.org/standard/87426.html |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-409 | 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인) | 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381 |
| ref-1310 | 파이낸스스코프 (윤영훈) | 클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정 | 기사 | low | https://www.finance-scope.com/article/view/scp202507110007 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 오픈소스 문서 | medium | https://github.com/gpue/vda5050-sim |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 오픈소스 문서 | medium | https://github.com/merschformann/RAWSim-O |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2214716019300946 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 오픈소스 문서 | medium | https://movingai.com/benchmarks/mapf/index.html |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 벤더 문서 | medium | https://www.behaviortree.dev/groot/ |
| ref-1129 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2608.26066 |
| ref-1306 | Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11)) | Optimising human-robot collaboration for efficiency in retail warehousing | 논문 | medium | https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for |
| ref-822 | Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문) | A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities | 논문 | medium | https://digitalcommons.calpoly.edu/theses/3387 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 오픈소스 문서 | high | https://github.com/ros2/rosbag2 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 정부·연구기관 | medium | https://cslc.koti.re.kr/ |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 오픈소스 문서 | high | https://mcap.dev/spec |
| ref-741 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 논문 | medium | https://arxiv.org/abs/2510.20808 |
| ref-1308 | Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv) | Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking | 논문 | medium | https://arxiv.org/abs/2404.08006 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 |
| ref-1303 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 논문 | medium | https://arxiv.org/abs/2011.10294 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 논문 | medium | https://arxiv.org/abs/2307.03325 |
| ref-1312 | Wind River (Engblom, J. 인터뷰, Buchwieser, A.) | Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser | 벤더 문서 | low | https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 논문 | medium | https://arxiv.org/abs/2211.09507 |
| ref-1309 | Autoware Foundation (autowarefoundation GitHub) | autoware_rosbag2_anonymizer — README | 오픈소스 문서 | high | https://github.com/autowarefoundation/autoware_rosbag2_anonymizer |
| ref-1126 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 표준 | medium | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions |
| ref-1130 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ |
| ref-1313 | Open Robotics (gazebosim/gz-fuel-tools GitHub) | Gazebo Fuel Tools — README | 오픈소스 문서 | high | https://github.com/gazebosim/gz-fuel-tools |
| ref-1231 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 오픈소스 문서 | medium | https://classic.gazebosim.org/tutorials?tut=model_structure |
| ref-1311 | Kassem, K., & Michahelles, F. (Mensch und Computer 2022 Workshop Proceedings, Gesellschaft für Informatik) | Exploring Human-robot Interaction by Simulating Robots | 논문 | medium | https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full |
| ref-1307 | Stączek, P., Pizoń, J., Danilczuk, W., & Gola, A. (Sensors 21(23):7830) | A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR's) Operating Environment—A Case Study | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/ |
| ref-1131 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 |
| ref-1316 | 파이낸스스코프 | 아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속 | 기사 | low | https://www.finance-scope.com/article/view/scp202608140009 |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 벤더 문서 | low | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 논문 | medium | https://arxiv.org/abs/2403.09227 |
| ref-1134 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI) | Composable and executable scenarios for simulation-based testing of mobile robots | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full |
| ref-1165 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 벤더 문서 | low | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 벤더 문서 | low | https://blogs.nvidia.com/blog/mega-omniverse-blueprint |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? | 9, 33, 13 | 열림 | — |
| new | — | 대화로 만든 다중 로봇 작업 계획을 사람이 승인하기 전에 시뮬레이션으로 실행 가능성을 미리 확인하는 절차를 플릿 오케스트레이션에 적용한 공개 사례가 있는가? | 12, 36, 44 | 열림 | — |
| new | — | 실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? | 36, 52, 51 | 열림 | — |
| new | — | 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? | 48, 34, 19 | 열림 | — |
| new | — | 운영 기록으로 상황을 재현하기 전에 영상 기록을 익명화하면 재현 충실도가 얼마나 떨어지며, 국내 개인정보 처리 기준에서 재현용 기록을 어떻게 보관·공유해야 하는가? | 53, 36 | 열림 | — |
| new | — | 이동로봇 안전 표준(ISO 3691-4 등)이나 국내 인증 기관이 시뮬레이션·가상 시운전 결과를 안전 확인 근거로 인정하는 조건과 절차가 있는가? | 50, 36, 54 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 수행 자원 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 물류창고 | 제약 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 물류창고 | 예외·성과 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 제조 공장 | 작업 대상 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 제조 공장 | 제약 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 제조 공장 | 예외·성과 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 병원 | 제약 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 병원 | 예외·성과 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 상업 시설 | 제약 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 상업 시설 | 수행 자원 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 가정 | 제약 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 가정 | 작업 대상 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 실외 | 작업 대상 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |
| 기타 | 완료·인계 | docs/categories/design-and-simulation/index.md#다른-대분류와의-연결 | I. 설계·시뮬레이션 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02005 Provision of Simulation Models (1.0) | 표준 | IDTA(Industrial Digital Twin Association) | 34, 36, 4, 58 | ref-1314 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models |
| autoware_rosbag2_anonymizer | 오픈소스 | Autoware Foundation | 53, 36 | ref-1309 | https://github.com/autowarefoundation/autoware_rosbag2_anonymizer |
| Gazebo Fuel Tools (gz-fuel-tools) | 오픈소스 | Open Robotics | 34, 57 | ref-1313 | https://github.com/gazebosim/gz-fuel-tools |

## 추가 조사 요청

- '다른 대분류와의 연결' 절의 '아직 다루지 않은 연결': 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육(운영자 교육용 다중 로봇 플릿 시뮬레이터 등)과 I. 설계·시뮬레이션 영역을 잇는 근거 — 연결 공백을 줄이기 위해 필요하다.
- M. 안전 연결: IEC 61508-7 C.5.19 원문과 ISO 3691-4 의 시뮬레이션·가상 검증 관련 조항 — 현재 업체 블로그 인용(ref-1312)에만 기대므로 표준 원문 근거가 필요하다.
- Stączek 외(ref-1307)의 도킹 복귀 시간 수치(44초 → 22.5~23.3초)를 원문으로 다시 대조 — 1차 검증 단계에서 원문을 열지 못했다.
- IDTA 02005 'Provision of Simulation Models' 1.0 의 공식 발행일과 번호를 IDTA 공식 목록에서 확인 — 각주 발행일이 미확인이다.
- 벤더 주장(Rockwell Automation 18%·5주, 아바코 다운타임 20%·자동화율 90%, NVIDIA Mega, CJ대한통운 디지털 트윈 계획)의 독립 확인 또는 같은 기준선의 독립 측정 연구(oq-257·oq-084).
- 34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계 페이지(이전 분류 기준)의 10절 갱신: Xia 외·Holodeck·Smit 외·Howard·Huck 외·Carr 외·Gazebo 라이선스 규칙·Stączek 외 연결 반영 — 이번 실행 유형(대분류 연결)은 대분류 페이지 한 절만 고치므로 다음 해당 영역 실행으로 미룬다.

## 이행한 수정 지시

- f29 — vda5050-sim 문장(F. 연동 항목)에서 '기본 5종 AGV' 구절을 빼고, 'VDA 5050 3.0.0 을 주 대상으로 2.1.0·2.0.0·1.1.0 구형 판도 흉내 내고 공식 3.0.0 JSON 스키마 위에 세운 메시지 스키마와 적합성 시험 묶음을 둔다고 README 에 적는다'로 쓰고 개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아님을 밝혔다.
- f11 — SayPlan 문장(C. 채팅 기반 구성·운영 항목)을 '최대 3개 층·36개 방·140개 자산·물체의 두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연했다'로 고치고 '(단일 로봇 대상)'을 붙였다.
- f49 — H. 실행·협업·예외 복구 항목에서 '피커(작업자)'로 쓰고, P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결에서는 '노동 비용 측면의 근거이며 수용성·노동 영향의 직접 근거는 아니다(논문은 비용 분석이다)'를 밝혔다.
- f77 — Q. 현장 유형별 적용의 제조 공장 항목에서 도킹 복귀 시간 수치를 '보고했다'로 쓰고 '저자 사례 연구의 보고값이며 검증 단계에서 다시 대조하지 못했다'를 병기했다.
- f2·f3·f79·f80 — 각 문장에 벤더 주장을 밝히고 [추정] 태그를 붙였으며 18%·5주, 다운타임 20%·자동화율 90% 는 기준선·측정 방법 미공개임을 함께 썼다. f28 은 '2025-07 보도에 따르면'과 '목표' 표현을 유지했다.
- f64 — M. 안전 항목에 '연계 대상:'으로 시작하는 [추정] 문장 하나로만 두고, IEC 61508-7 C.5.19 는 Wind River 블로그 인터뷰(2014)의 인용으로, 시뮬레이션·장애 주입 권고는 업체 직원의 해석으로 밝히고 표준 원문 미확인을 적었다.
- 각주 원문 미열람 표기 — 지시된 39개 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-528·ref-079·ref-105·ref-406·ref-104·ref-407·ref-831·ref-1087·ref-1096·ref-527·ref-1303~ref-1316 은 표기하지 않았고, ref-528·ref-079 의 요약에서 '원문 미열람.' 접두어를 뺐다.
- ref-527 각주 발행일을 2025-01-06 으로 쓰고 reference_updates 의 published 도 정정했으며, ref-1314 의 발행일은 각주에 '미확인', JSON 에 null 로 두었다.
- 범위 경계 문구 — f21·f25·f26·f27 의 승강기·문 제어, f2·f70·f78 의 컨베이어·PLC 제어 코드 가상 시운전, f3·f22·f47·f61 의 센서 시뮬레이션·로봇 자체 주행·파지 물리·현실 격차 보정, f62·f63 의 안전 인증·설비 안전 제어를 각 문장 괄호 안에 '연계 대상'으로 짧게 밝혔고, f24·f64 는 '연계 대상:'으로 시작하는 문장으로 두었다.
- 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 — E. 사물·사람·실시간 상태 항목에 f16 으로 '18 은 현재 상태 표현, 34 는 가정한 미래 실험'을 밝히고, f65·f66 의 디지털 트윈 동기화는 N. 보안·개인정보 항목에서 36. 가상 시운전·실제 상황 재현의 경로로만 서술했다. 34 가 현재 상태를 표현한다고 쓰지 않았다.
- C. 채팅 기반 구성·운영 항목 머리에 분류 원문 주석의 엔진 짝(33·36, 14·15, 25·26 을 번호와 이름으로)을 링크와 함께 적고, f7(자율주행)·f9(제약 공정)·f11(단일 로봇) 문장에 대상을 밝혔다.
- L. AI·학습 기술 항목에 44·45·46·47 링크와 적용 대상 33·34·35·36 을 함께 적었고, f15 는 D. 공간·지도 모델 항목에서 44 와 33 을 함께 링크했다. f59 에는 25. 작업 배정 — MRTA 연결도 밝혔다.
- f43 은 [의견]으로 두고 'Lee 외 저자들은 … 제안했다'로 의견 주체를 밝혔다. f23 은 ref-516(제1부)·ref-518(제6부) 문장을 나눠 각자의 각주를 붙였고, f30·f31·f32 와 f36(ref-101·ref-398)도 출처별 문장과 각주로 나눴다.
- '아직 다루지 않은 연결'을 절 끝에 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129 관련 부분 근거만 있음), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육으로 적었고 완전성 표현은 쓰지 않았다.
- 다른 대분류·세부영역은 새 17개 대분류 기준의 문자+이름(예: 'F. 연동')과 번호+이름(예: '25. 작업 배정 — MRTA')으로 쓰고, 옛 대분류 이름을 옮겨 쓰지 않았다.
- Q. 현장 유형별 적용 항목에서 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타)을 이름으로 밝히고, f18·f19·f44·f81~f84 의 예제 월드·벤치마크·경진대회 시나리오는 각 문장에 실제 현장 배치가 아님을 밝혔다.
