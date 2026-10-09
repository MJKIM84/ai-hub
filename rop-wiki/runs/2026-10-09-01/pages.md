# 스토리텔러 산출 2026-10-09-01

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/index.md | draft | '다른 대분류와의 연결' 절 신규 작성(16개 대분류와의 연결, 각주 66건, 1차 조건부 승인 수정 14건 이행). 2차 수정: 원문 미열람 표시 정정, 번호·문자만 쓴 호칭 수정, 벤더 주장 표기 위치 수정, 긴 글머리표를 세부영역별 하위 글머리표로 나눔 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | C. 채팅 기반 구성·운영 | '다른 대분류와의 연결' 절 신규 작성(16개 대분류와의 연결, 각주 66건, 1차 조건부 승인 수정 14건·2차 수정 7건 이행) | run 2026-10-09-01
- 홈 최근 업데이트: 2026-10-09 — C. 채팅 기반 구성·운영: '다른 대분류와의 연결' 절을 처음 작성했다(원문 주석의 짝 엔진 대분류와 승인 구조가 만나는 대분류 등 16개 대분류, 새 출처 4건)
- 대분류 최근 업데이트: 2026-10-09 — C. 채팅 기반 구성·운영: '다른 대분류와의 연결' 절 신규 작성(16개 대분류와의 연결, 각주 66건, 근거 없는 연결 9개 영역 명시)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 안전 가드레일 | Safety Guardrail (LLM-enabled robots) | 언어 모델이 제안한 로봇 계획을 실행 전에 안전 규칙에 비추어 검사하고 위험한 부분을 막거나 고치는 별도의 감독 계층으로, RoboGuard 는 안전 규칙을 시간 논리 제약으로 바꿔 제어 합성으로 계획을 수정한다. | 13, 12, 48 | ref-700 |
| new | 생성형 AI 의미 규약 | OpenTelemetry GenAI Semantic Conventions | 생성형 AI 클라이언트·에이전트·도구 호출·MCP 의 스팬·지표·이벤트 이름과 속성을 정한 OpenTelemetry 규약으로, 2026-10 확인 시점에 지표는 개발(Development) 단계다. | 43, 13 | ref-1240, ref-1241 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-083 | Zhang, J. 외 | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 논문 | medium | https://arxiv.org/abs/2507.00552 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_demos |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-165 | Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자 | Large Language Models for Multi-Robot Systems: A Survey | 논문 | medium | https://arxiv.org/abs/2502.03814 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 논문 | medium | https://arxiv.org/abs/2606.02167 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 논문 | medium | https://arxiv.org/abs/2510.07417 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 논문 | medium | https://arxiv.org/abs/2306.15724 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 논문 | medium | https://arxiv.org/abs/2606.08214 |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 논문 | medium | https://arxiv.org/abs/2511.22354 |
| ref-738 | Yao, S. 외(Sierra, τ-bench 저자) | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 논문 | medium | https://arxiv.org/abs/2406.12045 |
| ref-753 | VerifyLLM 저자(arXiv 2507.05118) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 논문 | medium | https://arxiv.org/abs/2507.05118 |
| ref-759 | Ko, T.-H., & Lin, C.-T.(National Central University) | Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin | 논문 | medium | https://arxiv.org/abs/2609.29061 |
| ref-786 | Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K. | SENT Map -- Semantically Enhanced Topological Maps with Foundation Models | 논문 | medium | https://arxiv.org/abs/2511.03165 |
| ref-787 | Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W. | Tell2Design: A Dataset for Language-Guided Floor Plan Generation | 논문 | medium | https://arxiv.org/abs/2311.15941 |
| ref-811 | 김영재, 김세윤, 김홍준 (대한공간정보학회지) | 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654 |
| ref-812 | Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P. | FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations | 논문 | medium | https://arxiv.org/abs/2507.07644 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 논문 | medium | https://arxiv.org/abs/2312.09067 |
| ref-817 | 모빌리오(Mobilio) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 | 벤더 문서 | low | https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/ |
| ref-818 | Nakajima, H., & Miura, J. (IROS 2024) | Combining Ontological Knowledge and Large Language Model for User-Friendly Service Robots | 논문 | medium | https://arxiv.org/abs/2410.16804 |
| ref-822 | Howard, T. L. (California Polytechnic State University, 석사논문) | A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities | 논문 | medium | https://digitalcommons.calpoly.edu/theses/3387/ |
| ref-823 | 폴라리스3D(Polaris3D) | AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기 | 벤더 문서 | low | https://polaris3d.com/blog/trends/amr-roi-calculator/ |
| ref-824 | Kleiman, J., Frank, K., Voyles, J., & Campagna, S. | Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making | 논문 | medium | https://arxiv.org/abs/2505.13761 |
| ref-825 | Chen, Z., Zhuang, H., Li, Z., & Li, C. | Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism | 논문 | medium | https://arxiv.org/abs/2603.03784 |
| ref-826 | Ghasemloo, M., Eckman, D. J., & Li, Y. | Subtrace-Conditional Validation of Simulation Models and Digital Twins | 논문 | medium | https://arxiv.org/abs/2607.17088 |
| ref-827 | Yang, L., Luo, S., Cheng, X., & Yu, L. | Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges | 논문 | medium | https://arxiv.org/abs/2503.02167 |
| ref-828 | Camargo, M., Dumas, M., & González-Rojas, O. | Automated Discovery of Business Process Simulation Models from Event Logs | 논문 | medium | https://arxiv.org/abs/1910.05404 |
| ref-830 | 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)) | 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 오픈소스 문서 | medium | https://github.com/ros2/rosbag2 |
| ref-832 | Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P. | LLM Agents Perform Controlled Experiments Using Simulation Models | 논문 | medium | https://arxiv.org/abs/2608.23622 |
| ref-837 | Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)) | Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins | 논문 | medium | https://www.mdpi.com/2079-9292/14/24/4954 |
| ref-838 | Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports) | Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts | 논문 | medium | https://www.nature.com/articles/s41598-026-57316-5 |
| ref-843 | Kourani, H., Berti, A., Schuster, D., & van der Aalst, W. M. P. | Process Modeling With Large Language Models | 논문 | medium | https://arxiv.org/abs/2403.07541 |
| ref-844 | Matei, I., Zhenirovskyy, M., Menaka Sekar, P. K., & Wong, H. Y. | Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach | 논문 | medium | https://arxiv.org/abs/2604.12105 |
| ref-847 | Chiang, Y.-C., Lee, I.-P., Fu, L.-C. 외 (Autonomous Robots 50, Article 28, 2026) | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 논문 | medium | https://link.springer.com/article/10.1007/s10514-026-10255-6 |
| ref-848 | 손승아, 강태민, 하동수 (한국과학기술원), 정보과학회지 42(10) | 자연어 로봇 제어 기술 동향: 분류, 기술, 응용 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11940459 |
| ref-849 | Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S. | HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2505.00820 |
| ref-850 | Argenziano, F., Umili, E., Leotta, F., & Nardi, D. | Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning | 논문 | medium | https://arxiv.org/abs/2509.16006 |
| ref-851 | 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)) | 거대언어모델 기반 로봇 인공지능 기술 동향 | 정부·연구기관 | medium | https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 |
| ref-855 | OWASP GenAI Security Project | OWASP Top 10 for LLM Applications 2025 | 업계 보고서 | medium | https://genai.owasp.org/llm-top-10/ |
| ref-856 | Model Context Protocol (Anthropic 주도 오픈소스 프로젝트) | Specification — Model Context Protocol (2025-06-18) | 오픈소스 문서 | medium | https://modelcontextprotocol.io/specification/2025-06-18 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 논문 | medium | https://arxiv.org/abs/2410.13691 |
| ref-858 | Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks) | Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making | 논문 | medium | https://arxiv.org/abs/2410.07166 |
| ref-859 | Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R. | Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges | 논문 | medium | https://arxiv.org/abs/2601.02377 |
| ref-862 | 개인정보보호위원회 | 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) | 정부·연구기관 | medium | https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 정부·연구기관 | medium | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 |
| ref-864 | Mullen, J. F., Jr., & Manocha, D. | Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2403.13198 |
| ref-865 | Zhang, Y., Zhang, Z.-H., & Qin, H. | Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways | 논문 | medium | https://arxiv.org/abs/2607.20860 |
| ref-866 | Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E. | Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems | 논문 | medium | https://arxiv.org/abs/2607.11792 |
| ref-867 | Michael, A. E., & Roesner, F. | How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement | 논문 | medium | https://arxiv.org/abs/2607.13718 |
| ref-868 | Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI | Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/ |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. | Safety Guardrails for LLM-Enabled Robots | 논문 | medium | https://arxiv.org/abs/2503.07885 |
| ref-1240 | OpenTelemetry (open-telemetry/semantic-conventions-genai GitHub) | semantic-conventions-genai — README | 오픈소스 문서 | high | https://github.com/open-telemetry/semantic-conventions-genai |
| ref-1241 | OpenTelemetry (open-telemetry/semantic-conventions-genai GitHub) | Semantic conventions for generative AI metrics (docs/gen-ai/gen-ai-metrics.md) | 오픈소스 문서 | high | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-metrics.md |
| ref-1217 | 대한민국 정책브리핑 (보건복지부) | 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행 | 정부·연구기관 | medium | https://www.korea.kr/news/policyNewsView.do?newsId=148958690 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | RoboGuard 처럼 안전 규칙을 시간 논리 제약으로 바꿔 언어 모델 계획을 고치는 안전 가드레일을 다중 로봇 오케스트레이션의 승인 전 검사에 두면 사람 승인 부담을 얼마나 줄일 수 있으며, 가드레일이 계획을 수정했을 때 무엇을 사람에게 다시 승인받아야 하는가? | 12, 48, 13 | 열림 | — |
| new | — | 대화로 실제 상황을 재현할 때 운영 기록에 남은 사람 흐름·혼잡을 시뮬레이션의 보행자 모델 입력으로 옮긴 연구나 사례가 있는가? | 11, 19, 36 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- E. 사물·사람·실시간 상태의 19. 사람·보행자 모델과 11. 채팅으로 실제 상황 시뮬레이션 재현을 잇는 근거(운영 기록의 사람 흐름·혼잡을 보행자 모델 입력으로 쓰는 연구·사례)가 없어 '아직 근거가 없는 연결'에만 적었다. 다음 대분류 연결 또는 11번 영역 갱신에서 조사가 필요하다.
- D. 공간·지도 모델의 16. 장소 의미·지도 관리와 12. 채팅으로 업무 지시·오케스트레이션 사이의 장소 이름 해석 연결은 oq-204 로만 남아 있어 근거 출처가 필요하다.
- F. 연동의 23. 업무 시스템 연동, H. 실행·협업·예외 복구의 30. 로봇 간 협업·물리적 인계, J. 현장 운영·관제의 39. 운영 성과 측정·개선·40. 운영 절차·요청 창구, M. 안전의 49. 사람 근접 안전·50. 안전 표준·인증·사고 조사, O. 검증·도입·수명주기의 56. 운영 이관·확대·교육과 C. 채팅 기반 구성·운영 세부영역을 잇는 검증된 근거가 없어 연결 서술을 하지 못했다.
- ref-847(병원 보조 로봇) 재확인 필요: 이번 1차 검증에서 Springer 열람이 막혀 [추정]으로 강등했고, 게시 페이지끼리 태그가 다르다(9. 채팅으로 시나리오 구성 5절은 [추정], 12. 채팅으로 업무 지시·오케스트레이션 5절은 [사실]). 원문 확인 후 12번 페이지 태그 정합 여부를 판단해야 한다.
- 퍼블리셔 확인 요청: 새 참고문헌 id ref-700·ref-1217·ref-1240·ref-1241 이 브리프 2026-09-30-23·24 가 다른 출처에 준 번호와 겹칠 수 있다(색인 전체 1246건). 충돌하면 새 번호를 다시 매기고 이 페이지 각주와 프런트매터 sources 도 함께 바꿔야 한다. ref-1217 는 브리프 2026-09-30-24 의 ref-1268 과 URL 이 같으므로 기존 id 가 있으면 그 id 로 합친다.
- ref-049·ref-228 의 각주 접근일은 참고문헌 페이지의 '각주 형식' 줄을 입력에서 확인할 수 없어 이번 브리프 값(2026-10-09)으로 적었다. 기존 참고문헌 페이지 값과 다르면 그 값으로 맞춰야 한다.
- 구축자 확인 요청: 입력 대분류 페이지에는 템플릿의 '참고 자료' 절이 없어(정본 뒤 선택 절) 이번 patches 에서 다루지 않았다. 부록 R-4 에 따라 연결 절의 각주 정의는 그 절 끝에 두었다. 시드 대분류 페이지에 '참고 자료' 절을 둘지는 시드 담당이 정해야 한다.
- 다음 실행 후보: 13. 대화형 기능의 신뢰·기반 페이지 8절에 RoboGuard(ref-700)·OpenTelemetry 생성형 AI 지표(ref-1240·ref-1241), 12. 채팅으로 업무 지시·오케스트레이션 페이지 7절에 Nayantra(ref-854)·HMCF(ref-849) 반영(예산으로 이번 실행에서 다루지 않음).
- 상대편 대분류 페이지(A. 기획·사업·B. 로봇 온톨로지·F. 연동·G. 계획·최적화의 이전 분류 기준 연결 절, seed 상태인 D. 공간·지도 모델·E. 사물·사람·실시간 상태 페이지)에 C. 채팅 기반 구성·운영과의 연결이 아직 없다. 해당 대분류 연결 실행에서 반영이 필요하다.

## 이행한 수정 지시

- 절 이름 — patches 의 section 을 번호 없는 정본 H2 문자열 '다른 대분류와의 연결'로 썼다.
- f16 강등 — 현장 유형별 사례의 병원 항목에서 병원 보조 로봇 문장을 [추정]으로 쓰고 '원문 미열람(검색 결과 요약 기준)'과 '실행 전 사람 승인 절차 유무는 미확인'을 괄호로 함께 적었다.
- f6·f22 벤더 주장 — O. 검증·도입·수명주기 항목의 모빌리오 문장과 A. 기획·사업 항목의 폴라리스3D 문장을 각각 '[추정] 벤더 주장' 으로 표기하고, 뒤따르는 연결 추정 문장도 [추정]으로 두었다.
- f4·f14 범위 경계 — F. 연동 항목에서 RequestLift 자동 삽입(f14)과 승강기·문 연결 추정(f4) 뒤에 분류 원문 19장의 시설·설비 제어 경계에 따라 승강기·문 제어는 연계 대상이고 ROP 몫은 지도 요소 등록·통과 제약 반영·단계 완료 확인이라고 적었다.
- f46·f47·f53 법 적용 판단 — N. 보안·개인정보 항목에서 EU AI Act 해당 여부와 개인정보 처리 적법성 판단을 운영자·법무가 맡을 연계 대상으로 적고, P. 거버넌스·법규·사회 항목에서 f53 에 '로봇 현장 단말·채팅 화면이 무인정보단말기에 해당하는지는 이 출처에 없다'는 단서를 붙여 60. 노동·수용성·접근성 연결 근거로만 썼다.
- f53 표현·병합 메모 — 기존 기기 적용을 '단계적 의무화를 거쳐 기존 기기까지 전면 적용'으로 썼고, reference_updates 의 ref-1217 요약에 브리프 2026-09-30-24 의 ref-1268 과 URL 이 같으면 그 id 로 합치라는 메모를 남겼다(additional_research_requests 에도 적음).
- f44 단서 — M. 안전 항목에 RoboGuard 수치가 arXiv v2(2026-03-03 개정판) 초록 기준이고 v1 수치(92.3%→2.5% 미만)와 다르며 프리프린트 단일 출처의 저자 보고값(시뮬레이션·실세계 실험)임을 병기했고, ref-700 각주 발행일을 '2025-03-10(v2 개정 2026-03-03)'으로 썼다.
- f48 단서 — K. 플랫폼 아키텍처·인프라 항목에 지표가 모두 개발(Development) 단계라 이름·정의가 바뀔 수 있다는 점과 확인일 2026-10-09 를 적고 토큰 지표 이름 차이를 oq-212 로 연결했다.
- f34 범위 — F. 연동 항목에서 Nayantra 내용을 발표 예고 게시글(2026-06-25 작성) 기준으로 쓰고, 승인·접근통제 미언급을 '이 게시글 범위에서는'으로 한정했으며 발표 영상 내용은 확인하지 않았다고 적었다.
- f24·f28 — I. 설계·시뮬레이션 항목에서 Ko·Lin 결과를 '출처가 현장 유형을 밝히지 않은 가상 라인의 결과이므로 특정 현장 사례로 보지 않는다'고 적고, 제조 공장 항목에서 '최대 3.5배'가 저자 보고값이며 실제 운영 기록 재현이 아니라고 병기했다.
- f26 구분 — I. 설계·시뮬레이션과 E. 사물·사람·실시간 상태 항목에서 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)의 구분을 유지했고, 19. 사람·보행자 모델은 f26 으로 연결하지 않고 '아직 근거가 없는 연결'에 두었다.
- 각주 — 재사용 출처는 참고문헌 색인의 기관·제목·발행일·URL·접근일로 각주를 만들고 ref-674 는 2026-06-06, ref-090 은 2023-09-18 을 썼다. 지시 목록의 원문 미열람 출처 50건(ref-104 포함)은 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-079·125·110·049·228·105·111 에는 표시를 붙이지 않고 요약의 '원문 미열람' 문구도 뺐다.
- RoboGuard 열린 질문 — '이 연결에서 남은 질문'의 첫 항목에 이 질문이 oq-139(승인 단위)·oq-144(탈옥 방어 효과)와 이어진다고 적고, RoboGuard 결과는 oq-144 의 부분 진전일 뿐 해결이 아니라고 밝혔다. open_question_updates 에서도 oq-144 상태를 바꾸지 않았다.
- 호칭·구성 — 모든 연결과 mermaid 도식에서 대분류는 문자와 이름, 세부영역은 번호와 이름으로 썼고, 원문 주석의 짝 엔진(D. 공간·지도 모델·B. 로봇 온톨로지·I. 설계·시뮬레이션·G. 계획·최적화)을 먼저 서술한 뒤 '사람이 확인·승인한 계획만 실행' 축으로 F·H·J·K·M 대분류를 묶었다. A·B·F·G 대분류 페이지는 이번 patches 에 넣지 않았다.
- 2차: 각주 원문 미열람 표시 정정 — 참고문헌 색인에 '원문 열람: 예'인 ref-104·786·787·811·812·815·817·822·823·824·825·826·827·828·830·831·832·843·844·850·851·855·856·857·858·859·862·863·864·865·866·867·868 의 각주에서 ' (원문 미열람)'을 지워 색인 줄(접근일 포함)과 같게 했고, reference_updates 에서 source_unopened 를 false 로 바꾸고 summary 첫머리의 '원문 미열람. '을 지웠다. 색인 '아니오'인 ref-046·059·083·090·165·201·229·242·351·677·738·753·759·837·838·847·848 은 표시를 유지했다.
- 2차: ref-453·ref-674 접근일 — 두 각주의 접근일과 reference_updates 의 accessed 를 2026-10-09 로 고치고 source_unopened 는 false 로 두었다.
- 2차: 번호만 쓴 호칭 — L. AI·학습 기술 항목의 '14번 영역과'를 '14. 도면·BIM에서 지도 만들기와'로 고쳤다.
- 2차: 'A~P' 표기 — 현장 유형별 사례 첫 단락의 '위의 A~P 대분류 연결로'를 '위의 A. 기획·사업 ~ P. 거버넌스·법규·사회 대분류 연결로'로 고쳤다.
- 2차: index_updates.home_recent — 문자만 쓴 대분류 나열을 빼고 '원문 주석의 짝 엔진 대분류와 승인 구조가 만나는 대분류 등 16개 대분류'로 줄였다.
- 2차: 벤더 주장 표기 위치 — 모빌리오 문장을 '…관제 지도로 쓴다고 설명한다(벤더 주장, 2026-08-24). [추정][^ref-817]', 폴라리스3D 문장을 '…계산한다고 설명한다(벤더 주장, 2026-06-12, 제조 공장). [추정][^ref-823]'으로 고쳐 태그 바로 뒤에 각주만 오게 했다.
- 2차: 단락 길이 — I. 설계·시뮬레이션(33·36·34·35)·G. 계획·최적화(25·26, 24, 27·28)·F. 연동(20·22·21)·H. 실행·협업·예외 복구(29·32·31)·J. 현장 운영·관제(37·38)·K. 플랫폼 아키텍처·인프라(41·43·42)·N. 보안·개인정보(52·51·대화 기록 의무·53)·L. AI·학습 기술(45·44·47)·O. 검증·도입·수명주기(54·55·57)·P. 거버넌스·법규·사회(60) 항목을 연결 세부영역별 하위 글머리표로 나눴다. 문장·태그·각주는 바꾸지 않았다.
