# 스토리텔러 산출 2026-10-09-04

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/index.md | draft | '다른 대분류와의 연결' 절 신규 작성: 대분류 16곳과의 연결(근거 각주 46건, 각주 정의는 절 끝), 아직 다루지 않은 세부영역 23곳 명시, 1차 조건부 승인 수정 16건 반영. 형식 검증 재작성: 현재 페이지에 없는 '참고 자료' 절 패치를 뺐다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | I. 설계·시뮬레이션 | '다른 대분류와의 연결' 절 신규 작성(대분류 16곳과의 연결, 각주 46건, 1차 조건부 승인 수정 16건 반영) | run 2026-10-09-04
- 홈 최근 업데이트: 2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 신규 작성(C. 채팅 기반 구성·운영, F. 연동, G. 계획·최적화, O. 검증·도입·수명주기 등 대분류 16곳, 아직 다루지 않은 세부영역 23곳 명시)
- 대분류 최근 업데이트: 2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 신규 작성(대분류 16곳과의 연결 근거 정리, 연결 해석은 추정으로 표시, 각주 46건)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 슬롯카 모델 | Slotcar (Open-RMF simulated robot plugin) | Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이는 단순화 로봇 모델로, 로봇마다 주행 스택 전체를 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다. | 20, 34 | ref-406 |
| new | 혼합 현실 시험 | Mixed-Reality Testing | 실제 로봇·센서와 가상 로봇·센서를 한 환경에 함께 두고 플릿 관리 같은 기능을 시험하는 방식으로, 모든 로봇을 실물로 갖추기 전에 작업 배정 등을 검증할 수 있게 한다. | 36, 25 | ref-1129 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-833 | Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. (TUM 외, arXiv; IROS 2026 채택) | Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving | 논문 | medium | https://arxiv.org/abs/2607.14387 |
| ref-832 | Xia, Y., Weyrich, M., Jazdi, N. 외 (University of Stuttgart·AstraZeneca, arXiv; ETFA 2026 채택) | LLM Agents Perform Controlled Experiments Using Simulation Models | 논문 | medium | https://arxiv.org/abs/2608.23622 |
| ref-1331 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 논문 | medium | https://arxiv.org/abs/2011.10294 |
| ref-1332 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 논문 | medium | https://arxiv.org/abs/2211.09507 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 오픈소스 문서 | high | https://github.com/ros2/rosbag2 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 논문 | medium | https://arxiv.org/abs/2310.08710 |
| ref-1129 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2608.26066 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 논문 | medium | https://arxiv.org/abs/2312.09067 |
| ref-1127 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 논문 | medium | https://arxiv.org/abs/1912.06321 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 정부·연구기관 | medium | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_demos |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 오픈소스 문서 | medium | https://github.com/merschformann/RAWSim-O |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2214716019300946 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 표준 | medium | https://www.asam.net/standards/detail/openscenario-xml/ |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 논문 | medium | https://arxiv.org/abs/2409.12471 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 벤더 문서 | medium | https://www.behaviortree.dev/groot/ |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 오픈소스 문서 | medium | https://movingai.com/benchmarks/mapf/index.html |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 오픈소스 문서 | medium | http://sdformat.org/ |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 논문 | medium | https://arxiv.org/abs/2307.03325 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 논문 | medium | https://arxiv.org/abs/2403.09227 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2405896318316021 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 표준 | medium | https://www.iso.org/standard/87426.html |
| ref-1126 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 표준 | medium | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions |
| ref-1130 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ |
| ref-1131 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 |
| ref-1133 | NASA | NASA-STD-7009B Standard for Models and Simulations | 표준 | medium | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 |
| ref-741 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 논문 | medium | https://arxiv.org/abs/2510.20808 |
| ref-1239 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 오픈소스 문서 | medium | https://classic.gazebosim.org/tutorials?tut=model_structure |
| ref-409 | 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인) | 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 정부·연구기관 | medium | https://cslc.koti.re.kr/ |
| ref-1165 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 벤더 문서 | low | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 벤더 문서 | low | https://blogs.nvidia.com/blog/mega-omniverse-blueprint |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 벤더 문서 | low | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? | 9, 33, 13 | 열림 | — |
| new | — | 실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해, 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? | 36, 52, 51 | 열림 | — |
| new | — | 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? | 48, 34, 19 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 다른 대분류와의 연결 절의 '아직 다루지 않은 연결'에 적은 세부영역(예: 2. 사용 사례·요구·책임 범위, 29. 명령·작업 실행의 신뢰성, 41. 플랫폼 아키텍처·외부 API, 53. 개인정보·영상 데이터, 66. 실외, 67. 기타 현장)과 I. 설계·시뮬레이션의 연결 근거 — 이번 브리프에 finding 이 없어 절 보강을 미뤘다
- 34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계 페이지(이전 분류 기준)의 10. 다른 연구영역과의 연결 절에 C. 채팅 기반 구성·운영, L. AI·학습 기술, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회 연결(Xia 외, Holodeck, Huck 외, Carr 외, Gazebo 모델 라이선스 근거)을 반영할 갱신 실행 — 대분류 연결 실행은 대분류 절만 고친다
- 참고문헌 정리 요청: ref-943(PMC 링크)과 ref-060(doi 링크)이 같은 Lee 외 Digital Health 논문으로 이중 등록되어 있다 — 이번 절은 ref-943 하나로만 인용했다
- 벤더 주장 확인: Rockwell Automation 물류센터 에뮬레이션 사례(프로젝트 기간 18%·현장 시운전 5주 단축), NVIDIA Mega 블루프린트, CJ대한통운 디지털 트윈 계획의 독립 출처 확인 또는 이후 적용 결과
- pipeline 담당 확인 요청: 시드 대분류 페이지(I. 설계·시뮬레이션)에는 템플릿의 번호 없는 '참고 자료' 절이 없어, 이번 재작성에서는 그 절에 대한 패치를 빼고 각주 정의를 부록 R-4 대로 '다른 대분류와의 연결' 절 끝에 두었다. 시드 대분류 페이지에 '참고 자료' 절을 추가할지 정해 달라

## 이행한 수정 지시

- f1·f2·ref-1329 — Chat2Scenic 문장 두 개의 각주를 ref-833 으로 썼고 reference_updates 에 ref-1329 를 넣지 않았다(ref-833 을 cited_by 갱신용으로 넣음).
- f3·f4·ref-1330 — Xia 외 문장 두 개의 각주를 ref-832 로 썼고 ref-1330 을 등록하지 않았다.
- f15 — G. 계획·최적화 항목에서 'recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않는다'를 [사실][^ref-105] 문장으로, '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보인다'를 별도 [추정] 문장으로 나눴다.
- f18 — '경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다'를 [사실][^ref-267], '가정한 미래를 실험하는 쪽에 걸친다'를 별도 [추정] 문장으로 나눴다.
- f19 — 'MAPF 벤치마크는 지도마다 시나리오 파일을 묶어 공개한다'만 [사실][^ref-1091]로, 같은 조건 비교와 시나리오 형식·라이브러리와 맞닿는다는 부분은 별도 [추정] 문장으로 강등했다.
- f2 — C. 채팅 기반 구성·운영 항목에서 '생성 스크립트의 약 4분의 1은 컴파일에 실패했으므로'로 써서 '실행 불가' 표현을 쓰지 않았다.
- f31 — O. 검증·도입·수명주기 항목에 'CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18'로 썼다.
- f44·f48·f49 — 세 문장 모두 '[추정] 벤더 주장' 을 병기했고, ref-527 각주와 reference_updates 의 발행일을 2025-01-06 으로 고쳤다(본문에도 2025-01-06 발표로 기준일 명시).
- 각주 원문 미열람 표기 — 지시 목록의 33개 출처 각주 정의 끝에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-079·ref-105·ref-528 은 표기하지 않고 source_unopened: false 와 원문 텍스트 확인 요약으로 고쳤다.
- 범위 경계 문구 — f8·f20·f21·f42 쪽 승강기·문 제어(f8·f20·f21 문장 안에 '연계 대상' 명시, f42 는 인증 모델 사실만 서술해 제어를 다루지 않음), f11·f44·f45 의 PLC·컨베이어 제어 가상 시운전, f9·f32·f48 의 로봇 자체 주행·현실 격차 보정·센서 시뮬레이션, f36 의 안전 인증·설비 안전 제어를 각 문장 괄호에 '연계 대상'으로 밝혔고, f41 은 '연계 대상:'으로 시작하는 문장으로 두었다.
- 18·34 구분 — E. 사물·사람·실시간 상태 항목에서 f7 로 '18. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험'을 밝혔고, N. 보안·개인정보 항목의 디지털 트윈 동기화는 36. 가상 시운전·실제 상황 재현이 18의 현재 상태를 34의 실험으로 옮기고 결과를 되돌리는 경로로만 서술했다.
- f14 — 세 출처를 세 문장으로 나눠 ref-102(충전기 부족·과잉), ref-098(충전·배터리 교환 전략 비교), ref-109(충전소 배치 최적화) 각주를 따로 붙였다.
- f20·f22 — 병원 문장 두 개를 ref-943 하나로만 인용했고 ref-060 을 쓰지 않았다.
- '아직 다루지 않은 연결' — 지시한 22개 세부영역(5·6·8·10·12·17·29·30·31·40·41·43·45·46·50·53·56·57·58·60·66·67)을 번호와 이름으로 적었고, 브리프 finding 이 다루지 않은 2. 사용 사례·요구·책임 범위도 함께 적어 실제 미연결 영역과 맞췄다. 완전성 표현은 쓰지 않았다.
- 새 분류 명칭 — 다른 대분류는 17개 대분류 기준 문자+이름(예: 'F. 연동', 'O. 검증·도입·수명주기'), 세부영역은 번호+이름(예: '25. 작업 배정 — MRTA')으로 썼고 옛 대분류 이름을 옮기지 않았다.
- L. AI·학습 기술 연결 — L 항목 머리에 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영 링크와 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 링크를 함께 두고 f5·f6·f32 를 그 아래에 썼다.
- 형식 검증 재작성 — 현재 페이지에 없는 '참고 자료' 절에 대한 패치를 빼고 '다른 대분류와의 연결' 절 패치 하나만 보냈다(각주 정의는 부록 R-4 대로 그 절 끝에 둠). 주장·태그·각주 내용은 바꾸지 않았다.
