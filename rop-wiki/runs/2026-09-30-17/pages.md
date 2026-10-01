# 스토리텔러 산출 2026-09-30-17

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md | draft | 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 13절 각주 16건, 1차 조건부 승인 수정 11건 반영 |
| create | docs/topics/2026/2026-09-30-area36-s6.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "6. 대표 접근법과 기술" 절(1,605자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s4.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "4. 핵심 개념과 용어" 절(1,262자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s8.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "8. 대표 연구와 자료" 절(1,238자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s11.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "11. 열린 질문" 절(1,205자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s10.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,078자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s7.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "7. 관련 표준·프레임워크·오픈소스" 절(836자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area36-s3.md | draft | 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "3. 왜 중요한가" 절(661자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 36. 가상 시운전·실제 상황 재현 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 각주 16건, 1차 조건부 승인 수정 11건 반영 | run 2026-09-30-17
- 홈 최근 업데이트: 2026-09-30 — 36. 가상 시운전·실제 상황 재현: 영역 심화 초안(VDI/VDE 3693·MiL·SiL·HiL, rosbag2 기록 재생, 현실 일치 판정 후보, 병원·제조 공장·물류창고·기타 사례)
- 대분류 최근 업데이트: 2026-09-30 — 36. 가상 시운전·실제 상황 재현: 3~11절 신규 작성, 현장 유형 사례 4건(병원 실제 기록 기반 승강기 실패 재현 포함), oq-132·oq-156 부분 근거 추가
- 세부영역 최근 업데이트: 2026-09-30 — 36. 가상 시운전·실제 상황 재현: 영역 심화로 3~11절을 처음 작성했다(신뢰도 medium, 벤더 주장 2건 표시)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 소프트웨어 인 더 루프 | Software-in-the-Loop (SiL) | 실제 제어 언어로 작성한 제어 코드를 대상 하드웨어와 분리해 돌리며 설비 시뮬레이션과 연결해 시험하는 가상 시운전 구성이다. | 36, 55 | ref-1172 |
| new | 하드웨어 인 더 루프 | Hardware-in-the-Loop (HiL) | 실제 대상 하드웨어(가상 머신·컨테이너로 가상화한 하드웨어 포함)를 설비 시뮬레이션과 연결해 제어 프로그램과 하드웨어를 함께 시험하는 가상 시운전 구성이다. | 36, 55 | ref-1172 |
| new | 시뮬레이션–현실 상관 계수 | Sim-vs-Real Correlation Coefficient (SRCC) | 여러 방법·설정을 비교할 때 시뮬레이션에서의 성능 차이가 실제 로봇에서의 성능 차이와 얼마나 같은 방향으로 나타나는지를 상관계수로 재는 시뮬레이션 예측력 지표다. | 36, 34, 54 | ref-1167 |
| new | 모델·시뮬레이션 신뢰도 평가 | Models and Simulations Credibility Assessment (NASA-STD-7009) | NASA-STD-7009B 가 모델·시뮬레이션의 개발·사용 단계에서 요구하는 신뢰도 평가로, 결과를 쓰기 위한 수용 기준을 프로젝트가 정하고 위임된 기술 권한자가 승인한다. | 36, 54 | ref-1177 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-1165 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 표준 | high | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions |
| ref-831 | ROS 2 (Open Robotics 외, ros2/rosbag2 저장소) | rosbag2 README | 오픈소스 문서 | high | https://github.com/ros2/rosbag2 |
| ref-1167 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 논문 | medium | https://arxiv.org/abs/1912.06321 |
| ref-1168 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 논문 | medium | https://arxiv.org/abs/2310.08710 |
| ref-406 | Open Robotics | Simulation — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-943 | Lee 외 (Digital Health, SAGE) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-1171 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2608.26066 |
| ref-1172 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ |
| ref-599 | Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)) | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 논문 | medium | https://arxiv.org/abs/1807.00048 |
| ref-741 | Aljalbout, E., Xing, J., Romero, A. 외 (arXiv) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 논문 | medium | https://arxiv.org/abs/2510.20808 |
| ref-1175 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 |
| ref-1176 | 현대자동차그룹 | 가상의 디지털 공간에 세운 쌍둥이 공장 | 벤더 문서 | low | https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330 |
| ref-1177 | NASA | NASA-STD-7009B Standard for Models and Simulations | 표준 | high | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 |
| ref-1178 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI) | Composable and executable scenarios for simulation-based testing of mobile robots | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full |
| ref-1179 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 벤더 문서 | low | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가? | 36, 20, 55 | 열림 | — |
| new | — | 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? | 36, 19, 33 | 열림 | — |
| new | — | 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가? | 36, 3 | 열림 | — |
| new | — | 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? | 36, 63, 22 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 병원 | 작업 대상 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 병원 | 수행 자원 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 병원 | 제약 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 병원 | 예외·성과 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 제조 공장 | 시작 조건 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 제조 공장 | 작업 대상 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 제조 공장 | 수행 자원 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 제조 공장 | 제약 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 제조 공장 | 예외·성과 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 물류창고 | 시작 조건 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 물류창고 | 작업 대상 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 물류창고 | 수행 자원 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 물류창고 | 예외·성과 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 기타 | 시작 조건 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 기타 | 작업 대상 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 기타 | 수행 자원 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 기타 | 완료·인계 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |
| 기타 | 예외·성과 | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시 | 36. 가상 시운전·실제 상황 재현 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) | 표준 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | 36, 55 | ref-1165 | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions |
| NASA-STD-7009B Standard for Models and Simulations | 표준 | NASA | 36, 54 | ref-1177 | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 |

## 추가 조사 요청

- 6절 '실행 전 계획 검증': 계획을 실행하지 않고 정적으로 검사하는 도구(VAL 등)의 검증 항목을 원문에서 확인한 근거가 없어 전용 서술을 넣지 못했다. 도구 문서·논문 원문 확인이 필요하다.
- 4·6절: NASA-STD-7009B 의 신뢰도 요소·점수 척도는 검색 요약에만 있어 넣지 못했다. 표준 본문 PDF 열람으로 확인이 필요하다.
- 5절: 상업 시설·가정·실외 로봇 현장의 가상 시운전·실제 상황 재현 사례를 찾지 못했다. 이 현장 유형의 사례 조사가 필요하다.
- 5·6절: 여러 제조사 로봇 플릿을 대상으로 한 가상 시운전 공개 사례(Kulkarni 창고 로봇 가상 시운전, Siemens·Wipro 사례)와 Striffler·Voigt(2023) 리뷰는 신규 출처 상한·접근 실패로 넣지 못했다. 다음 실행에서 확인이 필요하다.
- 3·4·6절: 이번 페이지의 모든 주장이 단일 출처이므로 핵심 주장(가상 시운전 정의·MiL·SiL·HiL 구분, SRCC 수치)의 교차 확인 출처가 필요하다.
- 7절: 국내 가상 시운전 표준(KS)이나 공공 지침이 있는지 확인이 필요하다.

## 이행한 수정 지시

- f12 문구 수정 — 4절 용어 목록, 6절 차이 관리, 7절 표, 11절 oq-132 설명에서 '수용 기준은 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자(Technical Authority)가 승인한다'로 쓰고 '결과를 쓰기 전에'를 뺐다.
- f15 — 5절 물류창고 사례 작업 대상을 'PLC·I/O 모듈과 제어 프로그램'으로 쓰고, 모든 칸과 서술에 '[추정] 벤더 주장'을 병기했으며, 18%·5주 수치에 기준선·측정 방법 미공개를 함께 적었다.
- f17 — 5절 제조 공장 서술의 현대자동차그룹 문장에 '[추정] 벤더 주장'을 병기하고 정량 수치를 밝히지 않았음을 적었다.
- f7 — 5절에 실외 사례로 넣지 않고 site_matrix_updates 에서도 뺐으며, 6절 운영 기록 기반 재현과 7절 표에서 '연계 대상'으로만 짧게 다뤘다.
- f3·f15·f16 — 5절 첫 단락에 설비 제어 코드(PLC·컨베이어) 가상 시운전이 분류 원문 19장 '시설·설비 제어' 연계 대상이며 ROP 에는 방법 근거로만 쓴다는 문장을 [추정] 태그와 각주로 두었다(f24).
- f18 — 5절 기타 사례 서술에 실측 지도로 만든 대학 건물의 시뮬레이션 시험 사례이며 현장 배치나 현장 기록 재생이 아님을 밝혔다.
- f11·f14 — [의견] 문장마다 주체를 문장 안에 밝혔다(3·6·8절 'Luckcuck 외', 5절 병원 사례 'Lee 외 저자들').
- ref-1167 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1167 에 source_unopened: true 를 넣었으며, 페이지 신뢰도는 medium 을 넘지 않는다.
- 용어집 '모델·시뮬레이션 신뢰도 평가' — 정의를 'NASA-STD-7009B 가 개발·사용 단계에서 요구하는 신뢰도 평가, 수용 기준은 프로젝트가 정하고 위임된 기술 권한자가 승인' 수준으로 줄이고 설명에 기존 용어 '시뮬레이션 모델 검증·타당성 확인'과의 연결을 적었다(4절 본문에도 링크).
- 5절 — 상업 시설·가정 사례를 찾지 못했고 실외는 자율주행 방법 참고(f7)뿐이라는 문장을 절 끝에 두었고, site_matrix_updates 는 물류창고·제조 공장·병원·기타 칸만 냈다.
- 3절·9절 — 핵심 질문의 답(f20)과 직접 범위·연계 대상(f23·f24)을 [추정] 태그와 '~로 보인다' 표현으로 서술했고, 11절에서 oq-132·oq-156 을 부분 근거(f21·f22)와 함께 '열림'으로 두었다(open_question_updates 에 해결 처리 없음).
- 분량 초과 자동 분리: 36. 가상 시운전·실제 상황 재현 본문 11,353자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,449자
