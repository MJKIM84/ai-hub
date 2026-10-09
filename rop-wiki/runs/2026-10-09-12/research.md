# 리서치 브리프 2026-10-09-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-12 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 19. 사람·보행자 모델 |
| 대분류 | E. 사물·사람·실시간 상태 |

## 갭(비어 있거나 약한 섹션)

- 정정 요청 없음(inbox/corrections.md 에 대상 페이지 요청 없음). 갱신 실행이므로 원문 미열람·검색 결과 기준 주장의 재확인과 약한 절만 다룬다
- 섹션 5. 적용 사례 (현장 유형 명시) — 상업 시설 사례(Kidokoro 외, HRI 2013)의 '실제 쇼핑몰 시험'이 원문 미열람·검색 결과 기준이고, 병원 사례는 기사 1건, 실외·제조 공장·가정 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 2023 년 이후 움직임 지도 기반 장기 예측·배정 연구와 시설 센서 사람 검출을 교통 제약으로 바꾸는 방식이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — REP-155 의 현재 상태(Draft 여부) 재확인 필요, Open-RMF 의 사람 장애물 메시지·검출 패키지 미기재
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 움직임 지도 서베이(ref-1171)·Kidokoro 외(ref-1182) 원문 미열람
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 직접 범위 서술이 추정뿐이고 오케스트레이션 계층의 구현 사례가 없음
- 섹션 11. 열린 질문 — oq-272·oq-273·oq-274·oq-298·oq-303 에 근거가 없음

## 조사 질문

1. 현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
2. 게시 페이지가 원문 미열람·검색 결과 기준으로 둔 주장(Kidokoro 외 쇼핑몰 시험, 움직임 지도 서베이의 정의, REP-155 의 상태, ATC 데이터셋의 추적 방식)은 원문·초록 기준으로 여전히 맞는가? (섹션 5·7·8 재확인)
3. oq-272 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (섹션 7·9)
4. oq-273 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (섹션 5·6)
5. oq-274 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? (섹션 5·9)
6. oq-298 시간대별 사람 흐름을 담은 움직임 지도를 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? (섹션 6·7)
7. 제조 공장·가정·실외 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 있는가? (섹션 5)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ROS 규약 제안 REP-155(ROS4HRI)는 2026-10-09 확인 기준으로도 상태가 Draft, 유형이 Informational 이며, 식별되지 않은 사람을 익명 사람으로 표시하되 그 ID 는 영속을 보장하지 않고, 개인정보·동의는 다루지 않는다. | ref-1173 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f2 | [사실] | Kucner 외 서베이(IJRR 42(11), 2023-09)의 초록은 움직임 지도를 환경의 전형적 움직임 패턴을 기록한 지도로 정의하고, 궤적이나 짧고 끊긴 움직임 관측으로 만들며 전역 경로 계획·위치추정 개선·사람 움직임 예측에 쓰인다고 하고, 새 분류 체계를 제안하며 이 분야가 실제 적용에 이를 만큼 성숙했지만 빠르게 발전 중이라고 결론짓는다. | ref-1171 | 아니오 | medium | 2023-09 | — | — |
| f3 | [사실] | Kidokoro 외(HRI 2013)의 초록은 보행자 흐름·보행자 상호작용·보행 쾌적성의 세 모델로 로봇이 사람 사이를 다니는 가상 상황을 시뮬레이션하는 방법을 친근한 순찰(friendly-patrolling) 시나리오에 구현했고, 현장 실험에서 노출만 최대화한 로봇보다 주변 보행자가 보행 쾌적성을 더 좋게 인식했다고 적지만, 실험 장소가 쇼핑몰이라고는 밝히지 않는다. | ref-1182 | 아니오 | medium | 2013-03 | 제약 | — |
| f4 | [사실] | 같은 연구의 확장판(Kidokoro 외, IEEE Transactions on Robotics 31(6), 2015)은 로봇 주변 군중 형성 예측·보행 쾌적성 추정·혼잡 사전 회피 계획을 결합해 다음 이동 단계를 고르는 방법을 실제 쇼핑몰에서 시험해, 혼잡으로 인한 로봇의 보행 쾌적성 영향을 줄였다고 초록에 적는다. | ref-1479 | 아니오 | medium | 2015-11-11 | 상업 시설 / 제약 | — |
| f5 | [사실] | ATC 데이터셋을 공개한 ATR 연구진(Brščić 외, IEEE THMS 43(6), 2013)은 사람 키보다 높게 단 여러 3차원 거리 센서로 넓은 공공 공간에서 사람의 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현했다고 보고했다. | ref-1480, ref-1176 | 아니오 | medium | 2013-10-17 | 상업 시설 / 작업 대상 | — |
| f6 | [사실] | Open-RMF 의 장애물 메시지(rmf_obstacle_msgs/Obstacle)는 헤더의 좌표 프레임·시각, 발행 주체(source), 층 이름(level_name), 분류 라벨(예: human), 3차원 경계 상자, 예상 수명(lifetime), 추가·삭제 동작을 담으며, 확인한 정의에는 검출 신뢰도나 익명화를 위한 필드가 없다. | ref-1484 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f7 | [사실] | Open-RMF 의 rmf_obstacle 저장소는 기존 CCTV·영상 센서로 군중을 검출하는 용도의 사람 검출 노드(단안 카메라 YOLO-V4, OAK-D 카메라)를 두고, lane_blocker 노드가 /rmf_obstacles 의 장애물이 플릿 주행 차선과 겹치면 차선을 닫았다가 비면 다시 열거나 속도 제한(기본 0.5 m/s)을 건다. | ref-1485 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f8 | [추정] | f6·f7 에 따르면 시설 카메라의 사람 검출 결과를 층·발행 주체·수명과 함께 모아 여러 플릿의 차선 폐쇄·속도 제한으로 바꾸는 경로가 오케스트레이션 계층(Open-RMF)에 이미 있어 19. 사람·보행자 모델의 ROP 직접 범위 예시가 될 수 있으나, 신뢰도·익명화 형식은 정해져 있지 않아 oq-272 는 부분적으로만 답해진 것으로 보인다. | ref-1484, ref-1485, ref-1173 | 아니오 | low | 2026-10-09 | 제약 | — |
| f9 | [사실] | Kazemi Eskeri 외(IROS 2025)는 시간대별 사람 존재 확률을 담은 이산 격자형 움직임 지도를 다중 로봇 작업 배정의 확률적 비용에 넣어, ATC 쇼핑몰 데이터의 기록 궤적을 재생한 시뮬레이션에서 임무 완료 시간을 움직임 무시 방법 대비 최대 26%, 기준 방법 대비 최대 19% 줄였다고 보고했으며 실제 로봇 실험은 없다. | ref-1083 | 아니오 | medium | 2025-08-27 | 예외·성과 | — |
| f10 | [사실] | 고려대학교 구로병원 연구(Lee 외, Digital Health 12, 2026)는 약제부→응급실 직원 전용 승강기 경로에서 의약품 배송로봇(DOGU IROI)의 비긴급 임무 122건(2025-06-18~29)을 분석해 전체 성공률 87.03%, 승강기 가동률 59.01% 미만에서 95.52% 였고, 실패 14건 가운데 8건이 승강기 탑승·하차 중 막힘이었으며 탑승 인원이 1명 늘 때 실패 오즈비가 1.73 이었다고 보고했다. | ref-1487 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f11 | [사실] | 같은 연구는 혼잡이 임계값 아래일 때 로봇 배송을 배정하고, 승강기가 운행 중이며 가동률이 60% 이상이면 출발을 미루도록 권고하며, 59.01% 임계값은 현장 고유값이라 다른 곳에서는 다시 보정해야 한다고 적는다. | ref-1487 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | — |
| f12 | [추정] | oq-273 에 대해 f9(쇼핑몰 데이터 기반 시뮬레이션)와 f10·f11(병원 승강기 혼잡의 현장 측정)은 사람 혼잡이 로봇 작업 시간·실패에 주는 영향을 재고 배정 시점에 반영하는 근거가 되지만, 복도·구역 단위의 시간대별 사람 흐름을 작업 시간 추정과 스케줄링에 넣어 현장에서 효과를 잰 연구는 이번에도 찾지 못했다. | ref-1083, ref-1487 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f13 | [사실] | Gehrke 외(Transportation Research Interdisciplinary Perspectives 18, 2023)는 미국 노던애리조나대학교 캠퍼스 10곳에서 일주일간 녹화한 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(PET)으로 재고, 중간·위험 충돌의 예측 요인을 모델링했다. | ref-990 | 아니오 | medium | 2023-03-01 | 실외 / 제약 | — |
| f14 | [사실] | 노던애리조나대학교 보도(2023-05-16)에 따르면 이 연구에서 충돌(0초)이 12건 관찰됐고, 보도가 좁고 교차가 많은 지점일수록 위험 상호작용이 많았으며, 연구진은 넓은 보도에서 나란히 주행하도록 경로를 정하고 사람이 많은 지점의 횡단을 줄이며 덜 붐비는 표시된 지점으로 배송하도록 권고했다. | ref-1482 | 아니오 | medium | 2023-05-16 | 실외 / 제약 | — |
| f15 | [추정] | f13·f14 에 따르면 실외 보도 로봇의 보행자 충돌 위험은 보도 폭·교차 수·사람 활동량 같은 지점 특성과 이어지므로, ROP 가 실외 경로망에 지점별 보행자 활동·폭 속성을 두고 경로·배송 지점 선택의 비용으로 쓰는 방식이 19. 사람·보행자 모델과 27. 다중 로봇 경로·교통 관리 — MAPF 를 잇는 것으로 보인다. | ref-990, ref-1482 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f16 | [사실] | 연계 대상: 2024-08 경기 의왕시 부곡파출소 앞 횡단보도에서 경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제 시스템과 연동해, 실외 이동로봇이 카메라 신호 인식과 별도로 신호 상태를 실시간으로 받아 횡단보도를 건너는 시연이 열렸다. | ref-1483 | 아니오 | low | 2024-08-10 | 실외 / 시작 조건 | — |
| f17 | [추정] | oq-274 에 대해 국내에서는 공공 교통신호 데이터를 실외 로봇 관제 시스템에 연동한 시연(f16)은 확인되지만, 인파관리지원시스템 같은 공공 인파 밀집 데이터를 로봇 경로·운행 제한에 연동한 사례나 데이터 제공 조건은 이번에도 찾지 못했다. | ref-1483, ref-1177 | 아니오 | low | 2026-10-09 | 실외 / 시작 조건 | — |
| f18 | [사실] | 현대자동차·기아와 한림대학교의료원은 2025-04-07 한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇과 관제 시스템을 함께 개발·실증하는 협약을 맺으면서 병원을 환자·의료진·휠체어·이동식 침대가 섞인 고밀도 환경으로 규정했으나, 이 발표는 조선비즈 기사(2024-07)의 로봇 대수나 사람·휠체어 앞 대기 규칙을 확인해 주지 않는다. | ref-1488, ref-1181 | 아니오 | medium | 2025-04-07 | 병원 / 제약 | — |
| f19 | [사실] | Kairos(Catalano 외, arXiv 프리프린트 2026-09-23)는 3차원 장면 그래프의 복셀마다 사람 존재율과 이동 방향 분포를 두고 임의의 미래 시각을 스펙트럼 예측기로 예측해 주행 노드 단위로 모으는 4차원 장면 그래프를 제안했고, 로봇이 모은 캠퍼스·쇼핑몰·11개월 역 구내 데이터로 평가해 사람을 만나는 계획 과제에서 시간 불변 지도보다 같은 성공률로 더 많은 사람을 만났다고 보고했다. | ref-1486 | 아니오 | medium | 2026-09-23 | — | — |
| f20 | [추정] | oq-298 에 대해 f19 처럼 사람 존재·흐름 예측을 장면 그래프의 장소·주행 노드에 붙이는 연구 구현은 있으나, 움직임 지도를 장소 목록·지도 판과 함께 관리하는 공통 형식이나 현장 운영 사례는 이번에도 찾지 못했다. | ref-1486, ref-1171 | 아니오 | low | 2026-10-09 | — | — |
| f21 | [사실] | Zhu 외(arXiv 2025-10-03, IEEE RA-L 표기)는 시간대별 움직임 패턴을 담는 시간 조건부 움직임 지도를 써서 최대 60초 앞의 사람 움직임을 예측해, 실제 데이터셋 두 개에서 학습 기반 방법보다 평균 변위 오차를 최대 50% 줄였다고 보고했다. | ref-1489 | 아니오 | medium | 2025-10-03 | — | — |
| f22 | [사실] | Open-RMF 시뮬레이션 문서는 하드웨어 시험에서 기록한 데이터로 시뮬레이션 상황을 다시 만들 수 있다고 적고, menge 를 엔진으로 쓰는 선택 기능 crowdsim 을 traffic_editor 에서 켜 airport_terminal 예제에서 가상 사람을 움직이게 하지만, 기록된 사람 흐름을 crowdsim 입력으로 옮기는 방법은 설명하지 않는다. | ref-406 | 아니오 | medium | 2026-10-09 | — | — |

### 근거 발췌

- **f1**: 원문 머리 필드: Status Draft, Type Informational, Created 11-Jan-2022. 익명 사람은 /anonymous 에 true 를 발행하고 ID 가 영속하지 않을 수 있다. location_confidence 1·0~1·0 규칙. 개인정보·동의 언급 없음(확인일 기준 상태).
- **f2**: Aalto 연구 포털의 초록(IJRR 42(11) pp. 977–1006, 2023-08-03 온라인): MoD 는 typical motion patterns 를 기록하며, 궤적 또는 끊긴 관측으로 구축, 전역 계획·위치추정·사람 움직임 예측에 사용. 본문 PDF 는 추출 실패로 초록만 확인.
- **f3**: OpenAlex 초록 복원(HRI 2013, pp. 259-266): three underlying models — pedestrian flow, pedestrian interaction, walking comfort; 'friendly-patrolling scenario'; field experiment 결과 보행 쾌적성 개선. 초록에 shopping mall 언급 없음.
- **f4**: OpenAlex 초록(TRO 31(6) pp. 1419–1431, 2015-11-11): 여러 기본 보행자 행동 모델을 결합해 가상 주행 상황을 시뮬레이션하고 결과로 다음 이동 단계를 선택. 'real shopping mall' 시험에서 쾌적성 영향 감소. 효과 수치는 초록에 없음.
- **f5**: OpenAlex 초록 복원(THMS 43(6) pp. 522–534, 2013-10-17): 'sensors, which are mounted above human height to have less occlusion'; 단일 센서 추적을 결합해 넓은 구역을 최소 센서로 덮음; 쇼핑센터 환경 구현. 센서 수·면적은 초록에 없음. 데이터셋 페이지와 같은 저자군이라 독립 교차 확인 아님.
- **f6**: Obstacle.msg 필드: header(frame_id 기준 측정), id, source, level_name, classification(human, chair 등), bbox, data_resolution, data(옥트리), lifetime, action(ADD·DELETE·DELETEALL). 신뢰도·익명화 필드 없음. (발행일 미확인, 확인일 기준)
- **f7**: README: rmf_human_detector 는 sensor_msgs::Image 에 YOLO-V4 로 사람 검출, 용도는 기존 CCTV 로 군중 검출. lane_blocker_node 파라미터 lane_closure_threshold 1, speed_limit_threshold 3, speed_limit 0.5. 개인정보 언급 없음. (발행일 미확인, 확인일 기준)
- **f8**: Open-RMF 장애물 메시지에는 source·level_name·classification·lifetime 이 있고 REP-155 에는 location_confidence 가 있으나, 두 형식 모두 익명화·집계 규칙을 두지 않음(f1·f6·f7 종합).
- **f9**: arXiv 초록·HTML: 'time-dependent discrete probabilistic model'; ATC 데이터셋(오사카 쇼핑몰) 궤적을 재생한 'simulated environment'; 로봇은 시뮬레이션 차량. 완료 시간 최대 26%·19% 감소.
- **f10**: 단일 병원·단일 로봇. 실패 원인: 승강기 막힘 8, 복도 자율주행 오류 4, 호출 통신 오류 2. 가동률은 승강기 대기 시간(r=0.458)·이동 시간(r=0.224)과 상관. 임계값 AUC 0.779.
- **f11**: 결론: 'robotic medication delivery should be scheduled when congestion is below critical thresholds'. 실무 경계 약 60%, 한계로 단일 병원·단일 기종과 임계값 재보정 필요를 명시.
- **f12**: f9 는 시뮬레이션뿐이고 f10 의 혼잡 지표는 승강기 가동률·탑승 인원이며 복도 보행자 흐름이 아님.
- **f13**: 초록: 'one week of field-recorded video from ten locations'; PET 를 충돌·지점 특성의 함수로 모델링; 공유 통로 시설 관리 전략 수립에 쓰려는 목적.
- **f14**: 위험 기준: 공유 지점을 1.5초 안에 지남. 심각한 충돌은 로봇이 보행자 앞을 가로지르거나 추월할 때 대부분 발생. 권고: 'parallel travel' along 'wide sidewalks'. 논문과 같은 기관 보도라 독립 출처 아님.
- **f15**: 연구진 권고(경로·배송 지점 선택)를 플랫폼 경로 비용으로 옮긴 해석이며 오케스트레이션 플랫폼 적용 사례는 미확인.
- **f16**: 보안뉴스(2024-08-10): 경찰청 '실시간 교통신호정보 수집·제공 시스템'을 관제와 연동, 자체 카메라 인식의 이중화. 참여: 의왕시·도로교통공단·현대차·기아. 인파·보행자 수 데이터 언급 없음.
- **f17**: 한국어 검색 2회(실외 배송로봇 유동인구·인파 밀집 데이터 연동)에서 사례 없음. 연동 경로(공공 데이터→로봇 관제)의 선례로만 볼 수 있음.
- **f18**: 현대자동차그룹 보도자료: 고밀도 병원 환경에서 주행 성능·안전성이 핵심, 병원 데이터로 제품 기획·고도화, 로봇 친화 병원 표준·인증체계 공동 수립 계획. 기간은 명시 없음.
- **f19**: 초록·HTML: voxel 별 'directional mixture and a presence rate', 주행 노드로 집계·흐름 정렬 점수, 코드 공개(github.com/IacopomC/kairos). 계획 과제 목적은 만남 확률(최대화로 읽힘), 동료심사 전.
- **f20**: Kairos 는 연구 코드이며 지도 판 관리·교환 형식을 다루지 않음. 움직임 지도 ROS 2 패키지 검색 1회에서도 계획기 통합 패키지는 확인하지 못함.
- **f21**: 초록: MoD 세 유형 평가, time-conditioned MoD 가 가장 정확, 예측 구간 최대 60초, ADE 최대 50% 개선. 데이터셋 이름은 초록에 없음.
- **f22**: 원문: 'Data logged from hardware trials can be used to recreate the scenario in simulation'. crowdsim 실행 예: airport_terminal.launch.xml use_crowdsim:=1. 기록→보행자 모델 변환 언급 없음.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1171 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 2023 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649231190428 | 아니오 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 아니오 |
| ref-1176 | ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외 | ATC shopping center tracking dataset | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://dil.atr.jp/crest2010_HRI/ATC_dataset/ | 예 |
| ref-1177 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 | 2023-12-27 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1182 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 2013-03 | 논문 | medium | 2026-10-09 | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-1479 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6)) | Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot | 2015-11-11 | 논문 | medium | 2026-10-09 | https://doi.org/10.1109/TRO.2015.2492862 | 아니오 |
| ref-1480 | Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6)) | Person Tracking in Large Public Spaces Using 3-D Range Sensors | 2013-10-17 | 논문 | medium | 2026-10-09 | https://doi.org/10.1109/THMS.2013.2283945 | 아니오 |
| ref-990 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03-01 | 논문 | medium | 2026-10-09 | https://doi.org/10.1016/j.trip.2023.100789 | 아니오 |
| ref-1482 | Northern Arizona University (NAU Review) | Got robot delivery? New research demonstrates need for robot-friendly infrastructure | 2023-05-16 | 정부·연구기관 | medium | 2026-10-09 | https://in.nau.edu/news/delivery-robot-research/ | 아니오 |
| ref-1483 | 보안뉴스 (박미영) | 경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다 | 2024-08-10 | 기사 | low | 2026-10-09 | https://www.boannews.com/news/articleView.html?idxno=131956 | 아니오 |
| ref-1484 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_obstacle_msgs/msg/Obstacle.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg | 아니오 |
| ref-1485 | Open Robotics (open-rmf/rmf_obstacle) | rmf_obstacle — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_obstacle | 아니오 |
| ref-1486 | Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv) | Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs | 2026-09-23 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.27467 | 아니오 |
| ref-1487 | Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/20552076261437181 | 아니오 |
| ref-1488 | 현대자동차그룹 | 현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결 | 2025-04-07 | 벤더 문서 | medium | 2026-10-09 | https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736 | 아니오 |
| ref-1489 | Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기) | Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics | 2025-10-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.03031 | 아니오 |

### 출처 요약

- **ref-1171**: 움직임 지도(MoD)의 정의·분류 체계·응용·열린 문제를 정리한 서베이. 이번 실행에서는 Aalto 연구 포털의 초록을 열어 확인했다(본문 PDF 는 추출 실패).
- **ref-1173**: 사람 인지 정보를 ROS 에서 주고받는 규약 제안. 2026-10-09 확인 기준 상태 Draft, 유형 Informational.
- **ref-1176**: 원문 미열람. 오사카 ATC 쇼핑센터 천장 3차원 거리 센서 보행자 추적 데이터셋(이번 실행에서 다시 열지 않음).
- **ref-1177**: 원문 미열람. 기지국 접속정보 기반 인파 밀집도·위험도 산출과 지자체 경보 체계(이번 실행에서 다시 열지 않음).
- **ref-1181**: 원문 미열람. 한림대학교성심병원 로봇 운영(통행 경로 표시, 사람·휠체어 앞 대기) 보도(이번 실행에서 다시 열지 않음).
- **ref-1182**: 보행자 흐름·상호작용·쾌적성 모델로 로봇이 혼잡 영향을 예상하는 방법(HRI 2013, pp. 259-266). 이번 실행에서 OpenAlex 초록을 열어 확인했으며 초록에는 쇼핑몰 언급이 없다.
- **ref-406**: Open-RMF 시뮬레이션 장. 건물 지도 생성, 로봇·문·승강기 플러그인, menge 기반 crowdsim, 하드웨어 기록으로 상황 재현 언급.
- **ref-1083**: 움직임 지도를 다중 로봇 작업 배정 비용에 넣은 방법. ATC 데이터 재생 시뮬레이션에서 임무 완료 시간 단축 보고.
- **ref-1479**: HRI 2013 연구의 저널 확장판. 군중 형성 예측·보행 쾌적성·혼잡 사전 회피 계획을 실제 쇼핑몰에서 시험(OpenAlex 초록 열람, 본문 미열람).
- **ref-1480**: 사람 키보다 높게 단 3차원 거리 센서 여러 대로 넓은 공공 공간의 사람 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현(OpenAlex 초록 열람).
- **ref-990**: 대학 캠퍼스 10곳 일주일 영상으로 보도 배송로봇–보행자·자전거 상호작용을 PET 로 분석한 현장 관측 연구(초록 열람).
- **ref-1482**: ref-990 연구의 대학 보도. 충돌 12건, 좁은 보도·많은 교차의 위험, 경로·배송 지점 권고를 소개.
- **ref-1483**: 경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제와 연동해 실외 로봇이 횡단보도를 건너는 의왕시 시연 보도.
- **ref-1484**: Open-RMF 장애물 메시지 정의. 프레임·시각, 발행 주체, 층, 분류 라벨(human 등), 경계 상자, 수명, 추가·삭제 동작.
- **ref-1485**: CCTV·카메라 사람 검출 노드와 장애물이 주행 차선과 겹치면 차선을 닫거나 속도를 제한하는 lane_blocker 노드를 제공.
- **ref-1486**: 4차원 장면 그래프에 사람 존재율·이동 방향 분포를 두고 미래 시각을 예측하는 프리프린트. 캠퍼스·쇼핑몰·역 구내 데이터 평가, 코드 공개.
- **ref-1487**: 고려대 구로병원 의약품 배송로봇 122개 임무의 승강기 혼잡(가동률·탑승 인원)과 성공률·지연을 분석한 전향적 타당성 연구.
- **ref-1488**: 한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇·관제 시스템 공동 개발·실증 협약. 병원을 고밀도 혼재 환경으로 규정.
- **ref-1489**: 시간 조건부 움직임 지도로 최대 60초 사람 움직임을 예측해 학습 기반 방법보다 ADE 최대 50% 개선을 보고(초록 열람).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 상업 시설 사례의 쇼핑몰 시험 근거를 바로잡음: HRI 2013 초록(f3, ref-1182)은 친근한 순찰 시나리오의 현장 실험만 적고 쇼핑몰을 밝히지 않으며, 쇼핑몰 시험은 TRO 2015 확장판(f4, ref-1479)의 초록에 있으므로 사례 제목·각주를 ref-1479 중심으로 고치고 '원문 미열람, 검색 결과 기준' 문구를 정리. ATC 데이터셋 추적 방식은 f5 로 보강(같은 저자군이라 교차 확인 아님). 병원 — 고려대학교 구로병원 승강기 혼잡 사례(f10·f11, 한국, 여섯 항목: 수행 자원·제약·예외·성과) 추가, 한림대 사례는 f18 로 맥락만 보강하고 기사 1건 기준임을 유지. 실외 — 대학 캠퍼스 보도 배송로봇 관측 사례(f13·f14, f15) 추가로 '실외 사례 없음' 문장 수정, 의왕시 교통신호 연동 시연(f16)은 연계 대상으로 짧게. 제조 공장·가정은 여전히 사례 없음. 섹션 6(주제 페이지) — 시설 카메라 사람 검출→차선 폐쇄·속도 제한(f7), 움직임 지도 기반 배정(f9)·장기 예측(f21)·4D 장면 그래프 예측(f19). 섹션 7(주제 페이지) — REP-155 상태 Draft 재확인(f1), Open-RMF 장애물 메시지·rmf_obstacle(f6·f7). 섹션 8(주제 페이지) — 움직임 지도 서베이 초록 확인(f2), f9·f10·f13·f19·f21 추가. 섹션 9 — 직접 범위 예시로 f8(Open-RMF 장애물·lane_blocker), 외부 검출 모델 실행·카메라는 연계 대상. 섹션 11 — oq-272 부분 근거 f6·f8, oq-273 부분 근거 f9·f10·f11·f12, oq-274 부분 근거 f16·f17, oq-298 부분 근거 f19·f20, oq-303·oq-256 부분 근거 f22(모두 미해결 유지), 새 열린 질문 2건. 교차 규칙: 학습 기반 예측·배정(f9·f21)은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽 연결, 현재 관측(f6·f7)은 18. 실시간 세계 상태·데이터 일관성, crowdsim(f22)은 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10·f11, 66. 실외 페이지에 f13·f14·f16, 27. 다중 로봇 경로·교통 관리 — MAPF 에 f7. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 평균 변위 오차 | Average Displacement Error (ADE) | 궤적 예측에서 예측 구간의 모든 시점에 대해 예측 위치와 실제 위치 사이 거리를 평균한 오차 지표이다. |
| 4차원 장면 그래프 | 4D Scene Graph | 3차원 장면 그래프의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다. |

## 열린 질문

새로 생긴 질문:

- 시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가? | 관련 영역: 19. 사람·보행자 모델, 27. 다중 로봇 경로·교통 관리 — MAPF, 18. 실시간 세계 상태·데이터 일관성 | 근거: f7 | 종류: 일반
- 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? | 관련 영역: 19. 사람·보행자 모델, 26. 작업 순서·스케줄링, 22. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 11건
- 미확인 항목:
    - Kidokoro 외 HRI 2013 과 TRO 2015 는 OpenAlex 초록만 열었고 본문 미열람(IEEE Xplore 빈 응답, CroRIS 대기 페이지). 쇼핑몰 효과 수치 미확인
    - ref-1171 움직임 지도 서베이는 Aalto 포털 초록만 열었고 본문 PDF 는 추출 실패
    - f5 는 ATC 데이터셋(ref-1176)과 같은 저자군의 논문이라 독립 교차 확인 아님. ATC 센서 49대·약 900㎡ 수치는 이번에 다시 확인하지 않음
    - f14 는 ref-990 과 같은 대학의 보도라 독립 출처 아님. 논문 본문(충돌 수·예측 요인 계수) 미열람
    - f10·f11 고려대 구로병원 연구는 단일 출처, 교차 확인 실패
    - f18 은 조선비즈 기사(ref-1181)의 로봇 73대·대기 규칙을 확인해 주지 않음. 한림대 사례의 독립 확인은 여전히 실패
    - f19 Kairos 는 동료심사 전 프리프린트, 계획 과제의 목적(만남 최대화)은 본문 앞부분 기준 해석이며 데이터셋 이름(ATC·HB 표기)과의 대응 미확인
    - f21 의 데이터셋 이름 미확인(초록에 없음)
    - Open-RMF rmf_obstacle 의 이슈 #22(장애물 서버 통합 계획)는 403 으로 열지 못함
    - STRANDS 요양시설 배치에서 FreMEn 으로 상호작용 확률을 예측해 일정을 짠 내용은 PDF 추출 실패로 출처로 넣지 않음
    - 제조 공장·가정 현장의 사람 흐름 반영 사례는 이번에도 찾지 못함
    - 공공 인파 밀집 데이터의 실외 로봇 연동 국내 사례 미발견(oq-274)
- 범위 경계 위반 의심:
    - f7·f8: 카메라 영상의 사람 검출 모델 실행은 원문 19장 '로봇 자체 지능·제어'·센서 인식 쪽에 가까워 연계 대상으로 두고, ROP 직접 범위는 검출 결과(장애물 메시지)를 모아 차선 폐쇄·속도 제한 같은 교통 제약으로 쓰는 부분으로 한정해야 함
    - f16: 교통신호 시스템은 시설·공공 시스템 경계의 연계 대상이므로 claim 을 '연계 대상: '으로 시작
    - f10·f11: 승강기 운행·호출 제어는 시설·설비 제어 경계의 연계 대상이며, ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 서술해야 함
    - f13·f14: 보도 위 국소 회피·양보 동작은 로봇 제조사 몫이며, ROP 쪽은 경로·배송 지점 선택 비용(f15, 추정)으로만 연결
- 한계: web_fetch_available: true · fetch_mode full. 갱신(update) 실행으로, 정정 요청이 없어 원문 미열람·검색 결과 기준이던 주장의 재확인과 약한 절(5·7·9·11)과 열린 질문(oq-272·oq-273·oq-274·oq-298·oq-303)만 조사했다. 검색 15회/30, 신규 출처 11건/15(ref-1479~ref-1489, 예약 구간 안). 재사용 8건 가운데 ref-1171(Aalto 초록)·ref-1173(github_raw)·ref-1182(OpenAlex 초록)·ref-1083(arXiv)·ref-406(inbox 원문)은 이번에 열었고, ref-1176·ref-1177·ref-1181 은 열지 않았다(fetched false). 신규 11건은 모두 원문 또는 공식 초록을 열었다. 다만 ref-1479·ref-1480·ref-990 은 OpenAlex 초록만 열었다. 교차 확인 0건이다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-990)은 독립 출처로 보지 않았다. 주요 정정 근거: 5절 상업 시설 사례의 '실제 쇼핑몰 시험'은 HRI 2013 초록에 없고 TRO 2015 확장판 초록에 있다(f3·f4). 7절 REP-155 는 2026-10-09 원문 기준으로 여전히 Draft 이며(f1), 지난 실행의 '공식 채택' 검색 요약과의 차이는 원문 기준으로 정리된다. 한국 자료: 신규 ref-1483(보안뉴스)·ref-1487(고려대 구로병원)·ref-1488(현대자동차그룹), 재사용 ref-1177·ref-1181. 현장 유형: 병원(f10·f11·f18)·상업 시설(f4·f5)·실외(f13·f14·f15·f16·f17)이며 물류창고는 기존 ILIAD 사례를 유지하고 새 근거는 찾지 않았다. 제조 공장·가정 사례는 없다. 18. 실시간 세계 상태·데이터 일관성(현재 관측: f6·f7)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험: f22)을 구분했다. L. AI·학습 기술 관련 f9·f21 은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 에 함께 연결하자고 제안했다. 열린 질문에 대한 부분 근거: oq-272(f6·f8), oq-273(f9·f10·f11·f12), oq-274(f16·f17), oq-298(f19·f20), oq-303·oq-256(f22). 해결 제안은 없다. 벤더 기능·성능 주장은 없다(f18 은 협약 내용 진술이다). 페이지 갱신 제안은 1건(대상 영역 페이지)이며 63. 병원·의료, 66. 실외, 27. 다중 로봇 경로·교통 관리 — MAPF 반영은 다음 실행 후보로 남겼다. 입력 누락 없음, 우선 지정 질문 없음.
