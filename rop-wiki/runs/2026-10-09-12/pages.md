# 스토리텔러 산출 2026-10-09-12

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md | draft | 차등 갱신: 5절 상업 시설 사례 근거를 ref-1182→ref-1479 로 정정하고 병원(고려대 구로병원)·실외(대학 캠퍼스 보도) 사례 추가, 4절 덧붙임, 6·7·8·10·11절 기존 요약·2026-09-30 주제 페이지 링크 유지와 새 내용 추가, 9절 경계 표 보강, 13절 각주 정리, 프런트매터 sources 에 기존 ref-1175·ref-1079 유지(2차 수정 반영) |
| create | docs/topics/2026/2026-10-09-area19-s6.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절(1,552자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area19-s8.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "8. 대표 연구와 자료" 절(1,472자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area19-s11.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "11. 열린 질문" 절(1,150자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area19-s7.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절(925자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area19-s10.md | draft | 자동 분리: 19. 사람·보행자 모델 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(733자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 19. 사람·보행자 모델 | 갱신: 상업 시설 사례의 쇼핑몰 시험 근거를 HRI 2013(ref-1182)에서 TRO 2015 확장판(ref-1479)으로 정정, 병원(고려대 구로병원 승강기 혼잡)·실외(대학 캠퍼스 보도 배송로봇) 사례 추가, Open-RMF 사람 장애물·차선 차단과 움직임 지도 기반 배정·예측 보강, 열린 질문 부분 근거·새 질문 2건 | run 2026-10-09-12
- 홈 최근 업데이트: 2026-10-09 — 19. 사람·보행자 모델: 상업 시설 사례 근거 정정(TRO 2015 확장판), 병원(고려대 구로병원 승강기 혼잡)·실외(대학 캠퍼스 보도 배송로봇) 사례 추가, Open-RMF 사람 장애물·차선 차단과 움직임 지도 기반 배정·예측 보강
- 대분류 최근 업데이트: 2026-10-09 — 19. 사람·보행자 모델: 5절 사례 정정·추가(병원·실외), 6~11절 보강(시설 카메라 사람 검출→차선 폐쇄, 움직임 지도 배정·예측, 열린 질문 부분 근거)
- 세부영역 최근 업데이트: 2026-10-09 — 19. 사람·보행자 모델: 갱신 — 5절 상업 시설 사례 근거를 ref-1479 로 정정, 병원·실외 사례 추가, 4·6·7·8·10·11절 보강(2026-09-30 주제 페이지 링크 유지), 9절 경계 표 보강, 13절 각주 정리

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 평균 변위 오차 | Average Displacement Error (ADE) | 궤적 예측에서 예측 구간의 모든 시점에 대해 예측 위치와 실제 위치 사이 거리를 평균한 오차 지표이다. | 19, 46 | ref-1489 |
| new | 4차원 장면 그래프 | 4D Scene Graph | 3차원 장면 그래프(3D Scene Graph)의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다. | 19, 16, 46 | ref-1486 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1171 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 논문 | medium | https://journals.sagepub.com/doi/10.1177/02783649231190428 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 오픈소스 문서 | medium | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst |
| ref-1182 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 논문 | medium | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 논문 | medium | https://arxiv.org/abs/2508.19731 |
| ref-1479 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6)) | Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot | 논문 | medium | https://doi.org/10.1109/TRO.2015.2492862 |
| ref-1480 | Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6)) | Person Tracking in Large Public Spaces Using 3-D Range Sensors | 논문 | medium | https://doi.org/10.1109/THMS.2013.2283945 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 논문 | medium | https://doi.org/10.1016/j.trip.2023.100789 |
| ref-1482 | Northern Arizona University (NAU Review) | Got robot delivery? New research demonstrates need for robot-friendly infrastructure | 정부·연구기관 | medium | https://in.nau.edu/news/delivery-robot-research/ |
| ref-1483 | 보안뉴스 (박미영) | 경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다 | 기사 | low | https://www.boannews.com/news/articleView.html?idxno=131956 |
| ref-1484 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_obstacle_msgs/msg/Obstacle.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg |
| ref-1485 | Open Robotics (open-rmf/rmf_obstacle) | rmf_obstacle — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_obstacle |
| ref-1486 | Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv) | Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs | 논문 | medium | https://arxiv.org/abs/2609.27467 |
| ref-1487 | Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | high | https://journals.sagepub.com/doi/10.1177/20552076261437181 |
| ref-1488 | 현대자동차그룹 | 현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결 | 벤더 문서 | medium | https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736 |
| ref-1489 | Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기) | Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics | 논문 | medium | https://arxiv.org/abs/2510.03031 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가? | 19, 27, 18 | 열림 | — |
| new | — | 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? | 19, 26, 22 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 병원 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 상업 시설 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 실외 | 작업 대상 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 실외 | 수행 자원 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 실외 | 제약 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |
| 실외 | 예외·성과 | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시 | 19. 사람·보행자 모델 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) | 오픈소스 | Open Robotics (open-rmf) | 19, 18, 27 | ref-1484 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg |
| Open-RMF rmf_obstacle (사람 검출·lane_blocker) | 오픈소스 | Open Robotics (open-rmf) | 19, 27, 18 | ref-1485 | https://github.com/open-rmf/rmf_obstacle |

## 추가 조사 요청

- E. 사물·사람·실시간 상태 대분류 페이지 '다른 대분류와의 연결' 절의 G. 계획·최적화(26. 작업 순서·스케줄링), I. 설계·시뮬레이션(34. 시뮬레이션·예측용 디지털 트윈), Q. 현장 유형별 적용 항목이 Kidokoro 외 HRI 2013(ref-1182)을 쇼핑몰 사례 근거로 인용한다. 이번 갱신으로 쇼핑몰 시험의 근거가 TRO 2015 확장판(ref-1479)으로 정정됐으므로 다음 대분류 연결(category_link) 실행에서 해당 문장의 각주를 정정해야 한다. 실외 사례도 이제 있으므로 같은 절의 '아직 다루지 않은 연결'의 'Q. 현장 유형별 적용' 문장도 고쳐야 한다(예산·실행 유형으로 이번에 미룸)
- pipeline 담당 확인 요청: 자동 분리 코드가 절 안의 기존 '자세한 내용은 주제 페이지 …' 링크 줄을 새 분리 주제 페이지로 옮기지 않고 버렸다(2차 검증 지적). 이번 재실행에서는 6·7·8·10·11절 첫 문단의 요약 문장 바로 뒤에 2026-09-30 주제 페이지 링크 문장을 넣어 원 절과 분리 주제 페이지 양쪽에 남도록 했다. 또 새 분리 주제 페이지(2026-10-09-area19-s6·s7·s8·s10·s11)의 H1 이 기존 2026-09-30 분리 주제 페이지와 같아지는 문제의 처리 방안(제목에 날짜를 붙이거나 기존 주제 페이지에 합치는 방식)이 필요하다
- 다음 실행 후보: 63. 병원·의료 5절에 고려대 구로병원 승강기 혼잡 사례(ref-1487), 66. 실외에 캠퍼스 보도 배송로봇 관측(ref-990·ref-1482)과 의왕시 교통신호 연동 시연(ref-1483), 27. 다중 로봇 경로·교통 관리 — MAPF 에 Open-RMF lane_blocker(ref-1485) 반영
- 5절 병원 사례: 고려대 구로병원 연구(ref-1487)의 성공률 87.03% 산출 분모를 확인할 수 있는 정오표·추가 자료와, 다른 병원에서 승강기 혼잡을 독립적으로 측정한 자료가 필요하다(단일 출처·내부 불일치)
- 5절 상업 시설 사례: Kidokoro 외 TRO 2015(ref-1479) 본문의 쇼핑몰 시험 효과 수치, ATC 데이터셋 센서 49대·약 900㎡ 수치의 재확인이 필요하다
- 5절: 제조 공장·가정 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 여전히 없다
- 5절 병원 사례: 한림대학교성심병원 로봇 대수(73대)·사람·휠체어 앞 대기 규칙을 기사(ref-1181) 외 독립 출처로 확인하지 못했다

## 이행한 수정 지시

- 5절 상업 시설 사례 근거 정정 — 사례 제목을 'Kidokoro 외, IEEE Transactions on Robotics 2015'로 바꾸고 표의 모든 칸과 '실제 쇼핑몰에서 시험했다' 문장의 각주를 [^ref-1479]로 고쳤으며 '(원문 미열람, 검색 결과 기준)' 문구를 지웠다. ref-1182 는 세 모델·친근한 순찰 시나리오의 현장 실험·초록에 쇼핑몰 언급 없음 범위의 한 문장에만 인용했다.
- 13절 ref-1171·ref-1182 각주 — 접근일을 2026-10-09 로 바꾸고 ' (원문 미열람)'을 뺐으며 ref-1171 발행일을 2023-09 로 적었다. 본문에서는 4절 움직임 지도 항목·8절 서베이 항목에 '초록 기준(본문 미열람)'을, 5절 HRI 2013 문장에 '초록 기준'을 밝혔다.
- 13절 ref-1176·ref-1177·ref-1181 각주 — 기존 줄(접근일 2026-09-30)을 그대로 두었고 참고문헌 갱신에도 넣지 않았다.
- f5 — Brščić 외(ref-1480) 문장에 '데이터셋과 같은 저자군이라 독립 교차 확인이 아니다'를 밝히고 ref-1176 과 교차 확인으로 쓰지 않았다. ATC 센서 49대·약 900㎡ 수치는 기존 ref-1176 각주 문장에만 두었다.
- f7 — 6절에서 'CCTV 영상으로 군중 검출' 용도는 단안 카메라용 rmf_human_detector(YOLO-V4)에만 붙이고 OAK-D 노드는 칩 내 추론(MobileNet-SSD)으로 따로 적었다. 6절·9절에서 사람 검출 모델 실행·카메라를 연계 대상으로 두고, ROP 직접 범위는 /rmf_obstacles 장애물을 모아 차선 폐쇄·속도 제한으로 바꾸는 부분으로 한정했다.
- f8 — 9절 끝 문단과 11절 oq-272 항목에서 'Open-RMF 장애물 메시지에는 검출 신뢰도 필드가 없고, REP-155 는 location_confidence 를 두지만 두 형식 모두 익명화·집계 규칙이 없다'로 구분해 쓰고 [추정]을 유지했다.
- f10 — 5절 표와 서술에서 87.03% 를 '논문 보고 성공률'로 적고 '성공률 산출 기준 미확인'을 함께 적었으며, 다시 계산한 수치는 쓰지 않았다. '단일 병원·단일 기종' 한계를 서술과 6절에 남겼다.
- f10·f11 — 혼잡 지표를 용어집 '승강기 가동률'(elevator-operating-rate) 링크로 표기했다. 5절·6절·9절에서 승강기 운행·호출 제어를 연계 대상으로 두고, ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 썼다.
- f13·f14 — 지표를 용어집 '침범 후 시간'(post-encroachment-time) 링크로 적었다. f14(ref-1482)는 '논문과 같은 기관의 보도라 독립 교차 확인이 아니다'를 밝혔다. 보도 위 국소 회피·양보 동작을 제조사 연계 대상으로 5절·9절에 두고 f15 는 [추정]으로 썼다.
- 5절 '사례를 찾지 못한 현장 유형' 문장 — 실외 문장을 고치고 실외 사례(노던애리조나대학교 캠퍼스 보도, f13·f14)를 여섯 항목 표로 추가했다. 제조 공장·가정은 사례가 없다고 남겼고, 의왕시 교통신호 연동 시연(f16)은 9절 표에 '연계 대상:'으로 짧게 두었다.
- f9·f19·f21 — 6절과 8절에서 f9 에 '기록 궤적을 재생한 시뮬레이션 결과이며 실제 로봇 실험은 없다', f19 에 '동료심사 전 프리프린트(2026-09-23)', f21 에 '데이터셋 이름 미확인'을 함께 적었다. f9·f21 은 6절과 10절에서 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽에 연결했다(프런트매터 related_areas 에 25 추가).
- f6·f7 은 6절·7절·10절에서 현재 관측으로 18. 실시간 세계 상태·데이터 일관성 쪽에 두었다. f22(crowdsim, 기록 재현)는 7절·10절에서 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분해 연결했다.
- 11절 — oq-256·oq-272·oq-273·oq-274·oq-298·oq-303 에 부분 근거만 덧붙이고 상태를 모두 '열림'으로 두었다. open_question_updates 에 상태 변경을 내지 않았다.
- 용어집 — '평균 변위 오차'와 '4차원 장면 그래프'를 신규로 냈고, '4차원 장면 그래프' 정의와 설명에 기존 용어 '3차원 장면 그래프 (3D Scene Graph)'를 연결했다. 움직임 지도·차선 폐쇄·승강기 가동률·침범 후 시간은 신규로 내지 않고 본문에서 기존 용어집 페이지에 링크만 했다.
- 2차: 세부영역 페이지 6·7·8·10·11절의 2026-09-30 주제 페이지 링크 복구 — 다섯 절을 append 대신 replace 패치로 보내, 각 절 첫 문단의 기존 요약 문장 바로 뒤에 '2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — …](../../topics/2026/2026-09-30-area19-sN.md)에 있다.' 문장을 두었다. 자동 분리 뒤에도 세부영역 페이지 해당 절에 남는 앞 두 문장 안에 들어가 새 2026-10-09 분리 주제 페이지 링크와 함께 놓이고, 분리 주제 페이지 3. 본문 첫머리에도 그대로 옮겨진다. 7절은 REP-155 사실 문장 뒤에 링크를 두고 추정 문장을 다음 단락으로 나눴으며, 11절 링크 문장에는 oq-261·oq-294·oq-307 서술이 그 페이지에 있음을 밝혔다.
- 2차: 8절(분리 시 2026-10-09-area19-s8) Brščić 외 항목 — '천장 높이 3차원 거리 센서'를 '사람 키보다 높게 단 여러 3차원 거리 센서'로 고쳤다.
- 2차: 세부영역 페이지 프런트매터 sources — 근거 없이 빠졌던 ref-1175(THÖR)와 ref-1079(Francis 외 평가 지침)를 기존 순서 자리에 되살렸다(기존 페이지처럼 분리 주제 페이지의 출처를 함께 올리는 관행이며 13절 각주 정의는 기존과 같이 두지 않았다).
- 분량 초과 자동 분리: 19. 사람·보행자 모델 본문 12,913자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 8,122자
