# 스토리텔러 산출 2026-10-09-06

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/index.md | draft | '다른 대분류와의 연결' 절 신규 작성: 16개 대분류별 세부영역 연결(추정 연결 표시, 벤더 주장 6건 병기), 현장 유형별 사례, 아직 다루지 않은 세부영역 목록, 절 끝 각주 정의 44건. 2차 수정: L. AI·학습 기술 항목에 적용 대상 세부영역 링크, 약어 첫 등장 풀어 쓰기 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | K. 플랫폼 아키텍처·인프라 | '다른 대분류와의 연결' 절 신규 작성(16개 대분류의 세부영역 연결, 조건부 승인 수정 18건과 2차 수정 5건 반영: f21 1 Hz 귀속 정정, f30 추정 강등) | run 2026-10-09-06
- 홈 최근 업데이트: 2026-10-09 — K. 플랫폼 아키텍처·인프라: '다른 대분류와의 연결' 절을 처음 작성했다. 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포 세부영역이 다른 대분류의 세부영역과 만나는 지점, 현장 유형별 사례, 아직 다루지 않은 세부영역 목록을 담았다
- 대분류 최근 업데이트: 2026-10-09 — K. 플랫폼 아키텍처·인프라: '다른 대분류와의 연결' 절 작성(비용·어댑터·대화 API·통신 단절·기록·보안·배포 연결, 추정 연결과 벤더 주장 표시)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | MQTT 유언 메시지 | MQTT Last Will (Will Message) | MQTT 클라이언트가 접속할 때 브로커에 맡겨 두고, 연결이 예기치 않게 끊기면 브로커가 대신 발행하는 메시지다. VDA 5050 은 이를 써서 로봇의 연결 끊김(CONNECTION_BROKEN)을 알린다. | 42, 20, 18 | ref-031 |
| new | A/B 업데이트 | A/B Update (Dual Partition Update with Rollback) | 장치에 두 개의 시스템 영역을 두고 쓰지 않는 쪽에 새 이미지를 설치한 뒤 전환하며, 실패하면 이전 영역으로 되돌리는 소프트웨어 업데이트 방식이다. | 43, 57 | ref-1040 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_dds_security.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 표준 | medium | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 오픈소스 문서 | medium | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 표준 | medium | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 오픈소스 문서 | medium | https://github.com/kubeedge/kubeedge |
| ref-304 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 논문 | medium | https://arxiv.org/abs/2205.09778 |
| ref-306 | OASIS | MQTT Version 5.0 | 표준 | medium | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html |
| ref-307 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 벤더 문서 | low | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 논문 | medium | https://arxiv.org/abs/2512.15215 |
| ref-309 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 기사 | low | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms |
| ref-310 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 논문 | medium | https://dl.acm.org/doi/10.1145/564585.564601 |
| ref-374 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/issues/224 |
| ref-401 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 정부·연구기관 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-493 | Lott, J., & Honary, V.(University of San Diego) | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 논문 | medium | https://arxiv.org/abs/2609.13711 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호) | 정부·연구기관 | medium | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 오픈소스 문서 | medium | https://github.com/ros2/rosbag2 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG | Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 |
| ref-937 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | ROMI-H \| Changi General Hospital | 정부·연구기관 | medium | https://www.cgh.com.sg/chart/projects/romi-h |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-1023 | NAVER Corp. | 로보틱스 l NAVER Corp. | 벤더 문서 | low | https://www.navercorp.com/tech/robotics |
| ref-1024 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 표준 | medium | https://www.asyncapi.com/docs/reference/specification/v3.1.0 |
| ref-1025 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 표준 | medium | https://spec.openapis.org/oas/v3.1.0 |
| ref-1030 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 벤더 문서 | low | https://locusrobotics.com/locusone/automated-warehouse-software/integrations |
| ref-1031 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 논문 | medium | https://arxiv.org/abs/2412.05408 |
| ref-1032 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 논문 | medium | https://arxiv.org/abs/2201.00393 |
| ref-1033 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 논문 | medium | https://arxiv.org/abs/2606.10746 |
| ref-1034 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 오픈소스 문서 | medium | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html |
| ref-1036 | OpenTelemetry (CNCF) | Specification Status Summary | 오픈소스 문서 | medium | https://opentelemetry.io/docs/specs/status/ |
| ref-1037 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 오픈소스 문서 | medium | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md |
| ref-1039 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ |
| ref-1040 | Northern.tech (mendersoftware) | mender — README | 오픈소스 문서 | medium | https://github.com/mendersoftware/mender |
| ref-1041 | FinOps Foundation | FinOps Phases | 업계 보고서 | medium | https://www.finops.org/framework/phases/ |
| ref-1042 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 표준 | medium | https://www.finops.org/insights/focus-1-2-available/ |
| ref-1043 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 논문 | medium | https://arxiv.org/abs/2609.29043 |
| ref-1044 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies and innovation at scale | 벤더 문서 | low | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 논문 | medium | https://arxiv.org/abs/2205.06564 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가? | 43, 41, 32 | 열림 | — |
| new | — | 로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가? | 41, 21 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 물류창고 | 완료·인계 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 물류창고 | 시작 조건 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 물류창고 | 제약 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 병원 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 병원 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 제조 공장 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |
| 기타 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결 | K. 플랫폼 아키텍처·인프라 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 43. 데이터·관측성·배포 5절 병원 사례의 '로봇 시스템 로그는 … 1 Hz 로 남겼고' 문장은 1차 검증에서 귀속 오류로 확인됐다(1 Hz 는 승강기–로봇 통신 로그의 주기). 다음 갱신 실행에서 ref-943 원문(SAGE 전문)으로 정정이 필요하다.
- ref-374(Open-RMF rmf_ros2 이슈 #224)를 다시 열어 SQLite 작업 로그·백업 복구 풀 리퀘스트 제안과 현재 배포판 반영 여부를 확인해야 한다(H. 실행·협업·예외 복구 항목을 [사실]로 되돌릴 근거, oq-048).
- K. 플랫폼 아키텍처·인프라와 P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터(API 변경 정책·데이터 접근 책임 등), 60. 노동·수용성·접근성을 잇는 검증된 근거가 없다. 대분류 연결 절의 P 항목이 연계 대상 추정 하나뿐이다.
- Q. 현장 유형별 적용의 64. 상업 시설, 65. 가정·공동주택, 66. 실외 현장에서 플랫폼 배치(클라우드·현장 서버·로봇 분담)나 통신 단절 대응을 다룬 사례가 필요하다.
- K. 플랫폼 아키텍처·인프라 대분류 페이지 '다른 대분류와의 연결' 절의 '아직 다루지 않은 연결' 목록에 있는 세부영역과 K. 플랫폼 아키텍처·인프라를 잇는 근거 조사가 필요하다. 특히 C. 채팅 기반 구성·운영의 8. 채팅으로 맵 작성 ~ 11. 채팅으로 실제 상황 시뮬레이션 재현과 그 짝 엔진 영역, 55. 현장 조사·설치·시운전의 현장 네트워크 조사가 우선 후보다.
- 참고문헌 중복 등록 정리 요청: ros2_tracing 논문이 ref-1032·ref-1361 로, 구로병원 논문이 ref-943·ref-060 으로 이중 등록돼 있다(이번 절은 ref-1032·ref-943 만 인용).

## 이행한 수정 지시

- patches 절 제목 — 번호 없는 '다른 대분류와의 연결'로 보냈다.
- f21 — F. 연동의 22. 설비·건물 시스템 연동 항목을 '승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지'로 정정해 [사실][^ref-943]으로 두고, 승강기 통신 로그 생성은 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 수집·결합이라는 문장을 유지했다.
- f30 — H. 실행·협업·예외 복구 항목을 [추정][^ref-374]로 강등하고 SQLite 백업 풀 리퀘스트 내용은 쓰지 않았으며, 복구 제안 내용과 배포판 반영 여부를 이번 확인에서 재확인하지 못했음을 밝히고 oq-048 연결을 유지했다.
- f31 — FogROS2-FT 를 '독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다'로 고치고, 진행 중 작업 상태 보존의 근거로 읽지 않는다는 문장을 덧붙였다.
- f52 — Q. 현장 유형별 적용의 제조 공장 항목을 '기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 기준 아키텍처', '대형 차량(heavy-vehicle) 제조 현장'으로 고쳤다.
- f40 — L. AI·학습 기술 항목에 '실험은 계획 성공률만 측정했고 비용·지연 자체는 측정하지 않았다'는 단서를 붙였다.
- f22 — 본문에서 기준일 2021-02-15 를 OpenAPI 3.1.0 에만 붙이고 AsyncAPI 3.1.0 은 '발행일 미확인'으로 썼으며, ref-1024 각주 발행일을 '미확인'으로 두었다.
- f37·f38·f21·f54 — ros2_tracing 은 ref-1032 하나로만, 구로병원 논문은 ref-943 하나로만 인용하고 ref-1361·ref-060 은 절에 쓰지 않았다.
- f4·f5·f13·f20·f33·f53 — 여섯 문장 모두 '[추정] 벤더 주장[^ref-…]' 형식으로 병기했다(f4 는 판매사 조사를 인용한 기사임을 밝혔다).
- 범위 경계 문구 — f13(위치 추정)·f41(로봇 내부 계산 배치)은 로봇 자체 지능·제어 경계, f21 은 시설·설비 제어 경계, f19·f20 은 상위 업무 시스템 경계, f48 은 로봇 운영체제·펌웨어 무선 업데이트 연계 대상, f53 은 무선망 구축 연계 대상임을 각 항목에 밝히고, f50 은 '연계 대상:'으로 시작하는 문장으로 두었다.
- 18·34·36 구분 — f14·f15·f16 은 E. 사물·사람·실시간 상태 항목에서 현재 상태(18. 실시간 세계 상태·데이터 일관성)로, f33 은 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래)으로, f34·f35 는 36. 가상 시운전·실제 상황 재현(지난 기록)으로 나눠 쓰고, 셋을 디지털 트윈이라는 한 이름으로 묶지 않는다는 문장을 I 항목 머리에 두었다.
- 교차 규칙 — C. 채팅 기반 구성·운영 항목 머리에 12. 채팅으로 업무 지시·오케스트레이션의 엔진이 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링임을 밝히고 G. 계획·최적화 항목과 함께 읽도록 양쪽에 연결했다. L. AI·학습 기술 항목에는 44. 로봇 기반 모델·언어 모델 계획 링크와 적용 대상인 41·42·43 세부영역을 함께 적었다.
- '아직 다루지 않은 연결' 목록 — 지시된 31개 세부영역을 대분류별로 번호와 이름으로 적고, P. 거버넌스·법규·사회 연결은 f50 하나(연계 대상 추정)뿐임을 밝혔으며, 완전성 표현은 쓰지 않았다.
- Q. 현장 유형별 적용 — f51·f54(및 F 항목의 f21)는 병원(63. 병원·의료), f52 는 제조 공장(62. 제조 공장), f4·f19·f20·f33·f53 은 물류창고(61. 물류창고), f5·f13 은 기타(67. 기타 현장, 기업 사옥)로 현장 유형을 밝히고, f51 은 특정 병원 배치 결과가 아니라 미들웨어 구조라는 단서를 유지했다.
- 원문 미열람 표기 — 지시된 33개 출처 각주에 접근일 2026-10-09 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 원문 텍스트가 입력된 11개 출처(ref-004·009·031·045·051·105·148·251·287·405·762)에는 표기하지 않고 source_unopened: false 로 두었다.
- 각주 발행일 — ref-1042 2025-06-03, ref-1025 2021-02-15, ref-1034 2023-05-23, ref-943 2026-03-31, ref-1039 2025-08-14, ref-1120 2022-05-13, ref-045 2021-09-30 을 채우고, ref-766 은 제목에 '개인정보보호위원회고시 제2023-6호', 발행일 2023-09-22 로 맞췄다.
- f47·f50 — 접속기록 조항은 '2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인(oq-214)'으로만 쓰고 보관 기간 수치는 넣지 않았다.
- open_question_updates — 새 질문 1은 areas [43, 41, 32] 로 두고 H. 실행·협업·예외 복구 항목에서 oq-048·oq-213 과 함께 연결했고, 새 질문 2는 areas [41, 21] 로 두고 F. 연동 항목에서 oq-209 와 함께 연결했으며, question 문자열에 필드 구분 문자열을 남기지 않았다.
- 2차: index_updates.home_recent — '41·42·43 세부영역이'를 '41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포 세부영역이'로 고쳤다.
- 2차: additional_research_requests 다섯째 항목 — 번호만 나열한 목록을 빼고 'K. 플랫폼 아키텍처·인프라 대분류 페이지 '다른 대분류와의 연결' 절의 '아직 다루지 않은 연결' 목록'을 가리키게 했으며, '8~11'을 '8. 채팅으로 맵 작성 ~ 11. 채팅으로 실제 상황 시뮬레이션 재현'으로 이름과 함께 썼다.
- 2차: L. AI·학습 기술 항목 머리 문장의 적용 대상 세 세부영역 이름을 같은 폴더 상대 경로 링크(platform-architecture-and-external-api.md, distributed-systems-communication-and-computing.md, data-observability-and-deployment.md)로 바꿨다.
- 2차: 약어 첫 등장 풀어 쓰기 — E 항목 f14 문장의 MQTT 를 '메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)'으로(유언 표기는 용어집과 같게 '유언 메시지(Last Will)'), A 항목 f2 문장의 SaaS·PaaS 를 '서비스형 소프트웨어(Software as a Service, SaaS)·서비스형 플랫폼(Platform as a Service, PaaS)'으로, H 항목 f29 문장의 UWB 를 '초광대역(Ultra-Wideband, UWB)'으로, N 항목 f46 문장의 DDS 를 '데이터 분산 서비스(Data Distribution Service, DDS)'로 풀어 썼다. 주장·태그·각주는 바꾸지 않았다.
- 2차: reference_updates 의 ref-766 title 을 각주와 같은 '개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호)'로 맞췄다.
