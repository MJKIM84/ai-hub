# 스토리텔러 산출 2026-09-30-20

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md | draft | 영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주, 1차 조건부 승인 수정 16건 이행, 2차 수정: 5절 기타 사례 제약 칸을 비교 지표로 바로잡음·완료·인계 칸 두 곳 미확인·병원 서술의 검증 상태 문장 태그 제거, 7절 요약 문장을 사실·추정으로 분리 |
| create | docs/topics/2026/2026-09-30-area19-s6.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 장기 시공간 흐름 지도 첫 문장을 ref-1204 확인 범위(전형적 움직임 패턴 지도)로 고침 |
| create | docs/topics/2026/2026-09-30-area19-s4.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area19-s7.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약·첫 문장을 REP-155 사실 문장과 종합 판단 추정 문장으로 나눔 |
| create | docs/topics/2026/2026-09-30-area19-s8.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Helbing·Molnár 항목에서 '보행자 시뮬레이션에 널리 쓰이는' 삭제 |
| create | docs/topics/2026/2026-09-30-area19-s10.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area19-s11.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "11. 열린 질문" 절을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area19-s3.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "3. 왜 중요한가" 절을 옮겼다(2차 재실행에서 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 19. 사람·보행자 모델 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건), 1차 조건부 승인 수정 16건·2차 수정 7건 이행 | run 2026-09-30-20
- 홈 최근 업데이트: 2026-09-30 — 19. 사람·보행자 모델: 영역 심화로 3~11절 신규 작성(움직임 지도·궤적 예측·보행자 시뮬레이션, 물류창고·병원·상업 시설·기타 사례)
- 대분류 최근 업데이트: 2026-09-30 — 19. 사람·보행자 모델: 영역 심화로 3~11절 신규 작성, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈을 나눠 연결
- 세부영역 최근 업데이트: 2026-09-30 — 19. 사람·보행자 모델: 3~11절 신규 작성(신뢰도 low, 출처 15건, 열린 질문 신규 3건)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사회적 힘 모델 | Social Force Model | 보행자 움직임을 원하는 속도로의 가속, 다른 보행자·벽과의 거리 유지(반발), 끌림을 나타내는 가상의 힘의 합으로 계산하는 보행자 행동 모델이다. | 19, 34 | ref-1207 |
| new | 사람 움직임 궤적 예측 | Human Motion Trajectory Prediction | 관측된 과거 위치와 주변 맥락(다른 사람·장애물·목적지)을 바탕으로 사람의 가까운 미래 이동 경로를 추정하는 기법이다. | 19, 46 | ref-1205 |
| new | 사회적 내비게이션 | Social Robot Navigation (Human-aware Navigation) | 로봇이 사람 사이를 이동할 때 안전뿐 아니라 쾌적성·가독성·예의 같은 사회적 원칙을 지키도록 경로와 행동을 정하는 주행 방식이다. | 19, 49, 54 | ref-1079 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1204 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 논문 | medium | https://journals.sagepub.com/doi/10.1177/02783649231190428 |
| ref-1205 | Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020) | Human Motion Trajectory Prediction: A Survey | 논문 | medium | https://arxiv.org/abs/1905.06113 |
| ref-1206 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 오픈소스 문서 | high | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst |
| ref-1207 | Helbing, D., & Molnár, P. (Physical Review E 51(5)) | Social force model for pedestrian dynamics | 논문 | medium | https://link.aps.org/doi/10.1103/PhysRevE.51.4282 |
| ref-1208 | Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020) | THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset | 논문 | medium | https://arxiv.org/abs/1909.04403 |
| ref-1209 | ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외 | ATC shopping center tracking dataset | 정부·연구기관 | high | https://dil.atr.jp/crest2010_HRI/ATC_dataset/ |
| ref-1210 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 | 정부·연구기관 | medium | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 |
| ref-1211 | Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI) | Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 논문 | medium | https://arxiv.org/abs/2306.16740 |
| ref-1213 | Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023) | HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation | 논문 | medium | https://arxiv.org/abs/2305.01303 |
| ref-406 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Simulation | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-1215 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 정부·연구기관 | medium | https://iliad-project.eu/concluding-iliad/ |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 논문 | medium | https://arxiv.org/abs/2310.08710 |
| ref-1217 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 기사 | low | https://v.daum.net/v/bc4riunbUE |
| ref-1218 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 논문 | medium | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? | 19, 18, 53 | 열림 | — |
| new | — | 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? | 19, 26, 63 | 열림 | — |
| new | — | 기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? | 19, 66 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 물류창고 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 물류창고 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 물류창고 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 기타 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 기타 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 기타 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 기타 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) | 프레임워크 | ROS (ros-infrastructure/rep) | 19, 18, 53 | ref-1206 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst |
| HuNavSim (ROS 2 사람 보행 시뮬레이터) | 오픈소스 | Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. | 19, 34, 54 | ref-1213 | https://arxiv.org/abs/2305.01303 |
| Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) | 오픈소스 | Open Robotics | 19, 34 | ref-406 | https://osrf.github.io/ros2multirobotbook/simulation.html |
| 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) | 프레임워크 | Francis, A. 외 | 19, 54 | ref-1079 | https://arxiv.org/abs/2306.16740 |

## 추가 조사 요청

- 5절 제조 공장·가정: 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 브리프에 없어 쓰지 못했다. 두 현장 유형의 사례 조사가 필요하다.
- 5절 실외: 이 영역의 로봇 적용 사례(예: 실외 배송로봇이 보행자 흐름을 경로에 반영한 사례)가 없어 사례 묶음을 쓰지 못했다.
- 5절 모든 사례: 시작 조건·완료·인계 칸이 미확인이다. 물류창고(ILIAD)·병원(한림대학교성심병원)의 사람 흐름 반영이 처리 시간·지연에 준 정량 효과도 미확인이다.
- 6·8절: Kidokoro 외(HRI 2013) 원문을 열어 보행 쾌적성 효과 수치를 확인하고, Rudenko 외 서베이의 세부 분류 명칭과 Vintr 외의 최우수 방법 이름을 확인할 필요가 있다.
- 7절: REP-155(ROS4HRI)의 최종 채택 상태(Draft 여부)와 ILIAD 프로젝트 시작 연도를 확인할 필요가 있다.
- 5·8절: 병원 로봇의 대기 규칙(환자·휠체어를 만나면 무조건 대기)을 독립 출처로 교차 확인할 필요가 있다.
- 브리프 self_check 에서 예산으로 빠진 Mavrogiannis 외 사회적 내비게이션 서베이, ILIAD Safety Stack 논문, 병원 군중 동행 리뷰, Kairos(4D 장면 그래프 기반 존재·흐름 예측)를 다음 실행에서 조사하면 6·8절을 보강할 수 있다.
- 파이프라인 참고(2차 검증 노트): 자동 분리 뒤 세부영역 페이지 프런트매터 sources 에 본문에서 더는 인용하지 않는 ref-1208·ref-1079·ref-406 이 남아 있고, reference_updates 의 cited_by 가 분리 주제 페이지를 반영하지 않는다. 퍼블리셔 쪽 정리가 필요하다.

## 이행한 수정 지시

- f2 '보행자 중심의 지상 2차원' 한정구 삭제 — 4절 궤적 예측 항목과 6절·8절에서 한정구 없이 '여러 연구 공동체의 궤적 예측 방법'으로 썼다.
- f9 비교 방법 수와 방법 이름 — 6절 장기 흐름 지도에 '26개 방법'으로 쓰고 HyT×GMM 등 구체 방법 이름을 빼고 '공간과 시간을 독립적으로 모델링한 연속 시공간 방법이 우수했다'로 썼으며, 8절도 '26개 흐름 지도 방법'으로 맞췄다.
- f10 표본 한계 — 5절 기타 사례의 예외·성과 칸과 서술 문장에 '40분 세션 네 번, 방법당 두 세션'과 로봇 없는 대조 측정(211명 중 불만 0명)을 같은 문장에 밝히고 Toyota HSR 기종은 쓰지 않았다(수행 자원 칸은 '기종 미확인').
- f8 효과 서술 — 5절 상업 시설 사례의 예외·성과 칸을 '노출만 최대화한 로봇에 비해 주변 보행자가 보행 쾌적성을 더 좋게 인식, 효과 수치는 미확인'으로 쓰고 원문 미열람을 밝혔다.
- f15 대기 대상과 출처 한계 — 5절 병원 사례·6절 운영 규칙에서 '환자나 휠체어와 마주치면'으로 고치고 기사 1건(조선비즈, 2024-07-12) 기준임을 밝혔으며, 직접 인용은 '무조건 기다리도록 설계됐다' 짧은 구절 1회로 제한했다.
- f5 person ID 부여 노드 — 7절 표 아래 문장에서 얼굴 인식·음성 인식 노드로만 예시하고 '옷 색 같은 신체 특징'은 쓰지 않았다.
- f4 REP-155 지위 — 4절과 7절 표에서 '표준'이 아니라 '원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안'으로 쓰고 최종 채택 여부를 미확인으로 두었다. standards_updates 도 종류를 프레임워크로 두고 요약에 Draft를 밝혔다.
- f11 '논문 177편 검토' — 본문 어디에도 쓰지 않았다.
- f14 프로젝트 기간 — 5절 물류창고 서술에 '2021-06 종료'로만 쓰고 '2017~2021'은 쓰지 않았다.
- f21 범위 수정 — 9절 표에서 CCTV를 빼고 기지국 접속정보 기반 공공 시스템만 연계 대상으로 두었으며, 로봇 탑재 안전 기능(안전 센서 기반 감속·정지, 국소 회피)은 연계 대상으로, 구역별 속도·진입 제한은 49. 사람 근접 안전과 연결되는 운영 제약으로 나눠 썼다.
- 5절 실외 — 실외에서는 이 영역의 로봇 적용 사례를 찾지 못했음을 밝히고 f16은 9절 연계 대상, f17은 6절 방법 참고로만 두었으며 site_matrix_updates 에 실외 칸을 넣지 않았다.
- 5절 상업 시설 — 로봇 적용 사례를 f8(Kidokoro 외)로 세우고 f7(ATC 데이터셋)은 서술에서 '로봇 적용 사례가 아니라 보행자 관측 데이터셋'으로 밝혔으며, 제조 공장·가정 사례를 찾지 못했음을 절 끝에 명시했다.
- 11절 — 기존 oq-261을 열림으로 싣고 새 근거가 없음을 밝혔으며, oq-256은 f17·f18을 부분 근거로 싣되 열림을 유지했다(open_question_updates 에 상태 변경을 내지 않음).
- 용어집 — '로그 재생 에이전트·반응형 에이전트'는 신규 등록하지 않고 4절에서 기존 용어 log-playback(로그 재생)으로 링크했으며, 사회적 힘 모델·사람 움직임 궤적 예측·사회적 내비게이션 세 용어만 glossary_updates 로 냈다.
- 원문 미열람 표시 — ref-1204, ref-1207, ref-1218 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 세 항목에 source_unopened: true 를 넣었다.
- ref-1210 제목 — 각주 정의와 reference_updates 의 제목을 '29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방'으로 적었다.
- 2차: HuNavSim 소속 기관 드리프트 — standards_updates 의 HuNavSim 항목 org 를 'Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L.'로 고치고 '(Universidad Pablo de Olavide)'를 지웠다.
- 2차: 사회적 힘 모델의 순위 표현 — 분리 페이지 2026-09-30-area19-s8.md 의 Helbing·Molnár 항목에서 '보행자 시뮬레이션에 널리 쓰이는'을 지워 '사회적 힘 모델의 원 논문이며 기준일은 1995-05다(원문 미열람)'로 썼다.
- 2차: 기타 사례 제약 칸 — 세부영역 페이지 5절 기타 사례 표의 제약 칸을 '시공간 흐름 지도를 쓴 경로 계획. 경로 계획 시뮬레이션에서 예상 조우(Expected Encounters)와 예상 경로 길이로 방법을 비교'로 고쳐 두 값을 비교 지표로 적었다.
- 2차: 완료·인계 칸 — 세부영역 페이지 5절 상업 시설 사례와 기타 사례 표의 완료·인계 칸을 '해당 없음'에서 '미확인'으로 바꿨다(site_matrix_updates 에는 넣지 않았다).
- 2차: 검증 상태 문장 태그 — 5절 병원 사례 서술의 '이 대기 규칙은 기사 1건 기준이며 독립 출처로 확인되지 않았다. [사실][^ref-1217]' 문장을 지우고, 앞 문장의 인용 뒤에 '(기사 1건 기준, 독립 확인 없음)'을 합쳤다.
- 2차: 7절 종합 문장 태그 — 세부영역 페이지 7절과 분리 페이지 s7 의 세 줄 요약·본문 첫 문장을 'REP-155(ROS4HRI)는 원문 상태 Draft(2022-01-11 작성)인 ROS 규약 제안' 문장 [사실][^ref-1206]과 '보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다' 문장 [추정][^ref-1213]으로 나눴다.
- 2차: 6절 '시간대·구역별' 드리프트 — 분리 페이지 s6 의 '장기 시공간 흐름 지도' 첫 문장을 '궤적이나 짧고 끊긴 관측으로 환경의 전형적인 움직임 패턴을 지도로 만들어 전역 경로 계획에 쓴다. [사실][^ref-1204]'로 고쳤고, 시간대 표현은 ref-1211 문장에만 남겼다.
