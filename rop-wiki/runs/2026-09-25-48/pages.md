# 스토리텔러 산출 2026-09-25-48

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md | draft | 영역 심화: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 13절 각주 정의(1차 조건부 승인 수정 14건 반영). 형식 재작성: 프런트매터 sources 를 이 페이지 각주 정의와 일치시킴 |
| create | docs/topics/2026/2026-09-25-area19-s4.md | draft | 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "4. 핵심 개념과 용어" 절(1,482자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area19-s7.md | draft | 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,413자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area19-s8.md | draft | 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "8. 대표 연구와 자료" 절(1,396자)을 옮겼다. 형식 재작성: 8. 실시간 세계 상태·데이터 일관성 링크를 주제 페이지 기준 경로로 고침 |
| create | docs/topics/2026/2026-09-25-area19-s6.md | draft | 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "6. 대표 접근법과 기술" 절(861자)을 옮겼다. 형식 재작성: 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침 |
| create | docs/topics/2026/2026-09-25-area19-s11.md | draft | 자동 분리: 19. 모니터링·이상 탐지·원인 분석 의 "11. 열린 질문" 절(767자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 19. 모니터링·이상 탐지·원인 분석 | 영역 심화: 3~11절 신규 작성(표준 상태·오류 어휘, 원인 구분 접근, ROP 경계), 1차 조건부 승인 수정 14건 반영 | run 2026-09-25-48
- 홈 최근 업데이트: 2026-09-25 — 19. 모니터링·이상 탐지·원인 분석: 영역 심화로 3~11절 작성(VDA 5050·MassRobotics·Open-RMF 상태·오류 어휘와 지연 원인 구분 접근, 신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 19. 모니터링·이상 탐지·원인 분석: 영역 심화 3~11절 작성, 보충 단계 문 대기 시나리오와 ROP 경계 정리
- 세부영역 최근 업데이트: 2026-09-25 — 19. 모니터링·이상 탐지·원인 분석: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 새 열린 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 근본 원인 분석 | Root Cause Analysis (RCA) | 관측된 이상이나 실패를 일으킨 가장 근원적인 원인(구성 요소·사건)을 찾아내는 분석이다. | 19, 20 | ref-511 |
| new | 고장 탐지·진단 | Fault Detection and Diagnosis (FDD) | 시스템에 고장이 생겼음을 알아내고(탐지) 그 종류와 위치·원인을 밝히는(진단) 기법의 총칭이다. | 19 | ref-509 |
| new | 이동 병목 탐지 | Shifting Bottleneck Detection (Active Period Method) | 각 설비·차량이 끊김 없이 활성 상태로 있는 구간의 길이로 시점마다 병목을 판정하고 병목의 이동을 추적하는 방법이다. | 19, 4 | ref-510 |
| new | 분산 추적 | Distributed Tracing | 하나의 요청이 여러 구성 요소를 거치는 과정을 공통 추적 id 로 묶은 스팬들의 그래프로 기록하는 관측 기법이다. | 19, 11 | ref-502 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-500 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 오픈소스 문서 | high | https://github.com/ros/diagnostics/blob/ros2/README.md |
| ref-501 | ROS 2 (ros2/ros2_tracing GitHub) | ros2_tracing — README | 오픈소스 문서 | high | https://github.com/ros2/ros2_tracing |
| ref-502 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 오픈소스 문서 | high | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md |
| ref-503 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg |
| ref-313 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_door_msgs/msg/DoorMode.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg |
| ref-111 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-506 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema |
| ref-230 | MassRobotics (MassRobotics-AMR/AMR_Interop_Standard) | AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-283 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Doors | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-509 | Khalastchi, E., & Kalech, M. | Fault Detection and Diagnosis in Multi-Robot Systems: A Survey | 논문 | medium | https://doi.org/10.3390/s19184019 |
| ref-510 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 논문 | medium | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ |
| ref-511 | Soldani, J., & Brogi, A. | Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey | 논문 | medium | https://dl.acm.org/doi/full/10.1145/3501297 |
| ref-512 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 논문 | medium | https://arxiv.org/abs/2306.15724 |
| ref-513 | International Journal of Production Research(Taylor & Francis), 저자 미확인 | Process mining in supply chain management: state-of-the-art, use cases and research outlook | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2412285 |
| ref-514 | DBpia 게재 논문(저자 미확인) | 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12892366 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 3.0.0 판의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 이전 판(2.x)의 오류 수준이 다를 때, 두 판이 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? | 19, 9 | 열림 | — |
| new | — | 물류 로봇 작업 지연을 로봇·설비·통신·공정 원인으로 나누는 공개 원인 분류 체계나 현장 데이터셋이 있는가? | 19, 4 | 열림 | — |
| new | — | 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? | 19, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 보충 | 시작 조건 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |
| 보충 | 작업 대상 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |
| 보충 | 수행 자원 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |
| 보충 | 제약 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |
| 보충 | 완료·인계 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |
| 보충 | 예외·성과 | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 19. 모니터링·이상 탐지·원인 분석 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROS 2 diagnostics | 오픈소스 | ROS (ros/diagnostics GitHub) | 19 | ref-500 | https://github.com/ros/diagnostics/blob/ros2/README.md |
| ros2_tracing | 오픈소스 | ROS 2 (ros2/ros2_tracing GitHub) | 19, 11 | ref-501 | https://github.com/ros2/ros2_tracing |
| OpenTelemetry Specification | 오픈소스 | OpenTelemetry (CNCF) | 19, 11 | ref-502 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md |
| Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) | 오픈소스 | Open Robotics (open-rmf) | 19, 12, 20 | ref-111 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| Open-RMF 경보 메시지(rmf_task_msgs Alert) | 오픈소스 | Open Robotics (open-rmf) | 19, 18, 20 | ref-503 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg |

## 추가 조사 요청

- 27. AI·학습·적응과 모델 운영 페이지의 10. 다른 연구영역과의 연결에 19. 모니터링·이상 탐지·원인 분석(장애 분석, REFLECT 예)으로 가는 연결을 다음 해당 영역 실행에서 추가하도록 제안한다 — 분류 원문 8장 교차 규칙의 양쪽 연결.
- 11. 열린 질문(oq-033): Open-RMF·VDA 5050·MassRobotics 상태·오류 어휘 공통 매핑 — 이번 실행 후보였던 inorbit-ai ros_amr_interop README 와 Spatial Process Mining(arXiv 2506.06081)을 출처로 열어 매핑·혼합 흐름 적용 여부 확인 필요(예산 상한으로 미룸).
- 8. 대표 연구와 자료: Khalastchi·Kalech(2019) 원문에서 1차·2차 계획 진단 구분이 실제로 있는지, Soldani·Brogi(2022) 원문에서 로그 기반 인과 그래프 접근이 있는지 확인 필요 — 현재 [추정]으로 강등됨.
- 11. 열린 질문(신규 1): VDA 5050 2.x 판의 오류 수준 값 확인 필요 — 3.0.0 판과의 차이를 사실로 쓰려면 2.x 판 원문 근거가 필요하다.
- 3. 왜 중요한가·8. 대표 연구와 자료: 국내 물류센터의 로봇 정지·지연 원인 비율이나 이상 대응 시간 실측 자료, 국내 논문(ref-514) 저자·피험자 조건 재확인 필요 — 현재 국내 자료는 단일 예비 연구뿐이다.
- ref-500~ref-514 가 기존 참고문헌 448건과 같은 URL 인지 퍼블리셔 병합 확인 필요(입력 요약본으로는 확인 불가).
- 형식 재작성 관련(pipeline 담당): 퍼블리셔 4단계가 logs/daily/2026-09-25.md 의 깨진 링크로 실패했으나 오류 메시지가 잘려 대상 링크를 알 수 없다. 페이지 본문 링크는 docs_tree.txt 와 이번 실행이 만드는 페이지만 가리키도록 확인했고, 용어집 slug 는 퍼블리셔가 term_en 에서 만들도록 비웠다. 일일 로그가 아직 만들어지지 않은 참고문헌(ref-500~ref-514)·용어집 페이지를 먼저 링크하는지 확인이 필요하다.

## 이행한 수정 지시

- f15 — 4절 FDD 항목과 8절에서 '다중 로봇 속성이 FDD 에 서로 다른 어려움을 주며 적용 가능한 FDD 접근을 정리한다'만 [사실]로 쓰고, 1차·2차 계획 진단 구분은 8절에 [추정]과 '검색 요약 기준이며 원문 미확인'을 병기했다.
- f17 — 4절·6절·8절에서 '다중 서비스 클라우드 응용의 이상 탐지·근본 원인 분석 기법을 개관한 설문'까지만 [사실]로 쓰고, 로그 기반 인과 그래프 접근은 [추정]으로 강등하고 '로봇 분야 적용은 아니다'를 유지했다.
- f20 — 8절에서 [추정]으로 강등하고 수치 네 가지를 피험자 10명·가상 테스트베드 조건과 같은 문장에 '단일 예비 연구의 보고'로 적었으며, 3절에서는 이 수치를 쓰지 않았다.
- f20 디지털 트윈 — 8절에서 논문의 디지털 트윈을 현재 상태를 보여 주는 실시간 관제 화면으로 적고 8. 실시간 세계 상태·데이터 일관성에만 연결했으며 22. 시뮬레이션·예측용 디지털 트윈과는 연결하지 않았다.
- f16 — 3절·8절 문구를 '기존 두 방법(가동률·대기 시간 기반)에는 이동 병목 탐지와 비교해 여러 한계가 있다고 보고한다'로 바꾸고, 각주 ref-510 에 발행일 2003과 WSC 2003 Proceedings 1192–1198쪽을 적었다.
- f1·f2·f4 — 4절과 7절 서두에 기준을 'VDA 5050 3.0.0 판(GitHub main 브랜치, 접근일 2026-09-25)'으로 명시하고 main 브랜치는 판이 바뀔 수 있다고 적었다.
- f7 — 5절 수행 자원 칸과 7절 Open-RMF 문 행, 9절 표에서 문 개폐 제어 자체를 연계 대상(시설·설비 제어)으로 표시하고 ROP 는 문 상태(DoorMode) 확인과 요청만 다룬다고 썼다.
- f11·f12 — 7절 ROS 2 diagnostics·ros2_tracing 행을 로봇 내부 진단·계측 도구로서 연계 대상으로 짧게 다루고 9절 f21 경계와 같은 표현(센서·모터·드라이버 수준의 로봇 내부 진단)을 썼다.
- f18 — 6절과 10절에 27. AI·학습·적응과 모델 운영을 번호와 이름으로 연결하고, 27. AI·학습·적응과 모델 운영 페이지에서 오는 연결은 additional_research_requests 에 다음 실행 제안으로 남겼다.
- ref-513 — 각주와 reference_updates 의 기관 표기를 'International Journal of Production Research(Taylor & Francis), 저자 미확인'으로 바꾸고 'Leopold, H. 외'를 쓰지 않았다(8절 본문도 저자명 없이 기재).
- 원문 미열람 표시 — ref-509~ref-514 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 여섯 항목에 source_unopened: true 를 넣었으며, ref-031·ref-051·ref-500~ref-283 에는 붙이지 않았다.
- 열린 질문 신규 1번 — 질문 문장을 'VDA 5050 3.0.0 판의 네 단계 오류 수준과 이전 판(2.x)의 오류 수준이 다를 때'로 고쳐 2.x 두 단계를 사실 전제로 두지 않았다(11절과 open_question_updates 모두).
- 5절 시나리오 — 첫 문장에 가상 시나리오임을 밝히고 수치를 쓰지 않았으며, 필드·값은 f5·f6·f8·f9(와 문 어댑터 역할 f7)가 확인한 것만 쓰고 원인 판정 절차는 [추정]으로 두었다.
- oq-018·oq-033 — 11절에 열림 상태로 두고 해결로 바꾸지 않았으며, f16·f19 는 oq-018 의 부분 자료로만 8절·11절에 연결했다(open_question_updates 에 상태 변경 없음).
- 분량 초과 자동 분리: 19. 모니터링·이상 탐지·원인 분석 본문 8,856자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,601자
- 형식 재작성 — 내용(주장·태그·각주·판정)은 바꾸지 않고, 세부영역 페이지 프런트매터 sources 를 13절 각주 정의(10건)와 일치시켰으며, reference_updates 의 cited_by 를 실제로 각주를 둔 페이지(세부영역·분리 주제 페이지)로 맞추고, glossary_updates 의 slug 를 비워 퍼블리셔가 term_en 에서 만든 경로와 일일 로그 링크가 어긋나지 않게 했다.
