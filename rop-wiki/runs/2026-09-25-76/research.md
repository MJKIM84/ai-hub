# 리서치 브리프 2026-09-25-76

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-76 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 4 · 답한 질문 q4-03

## 갭(비어 있거나 약한 섹션)

- 단계 4 질문 q4-03 열림(target.json 지정, CLI 지정 질문 id). 단계 4 페이지 3절에 q4-03 소제목 없음
- 완료 조건: 도면–현장 정합 절차 초안이 공간 그래프 스키마 초안 6절과 아이디어 3. 건축 도면 자동 인식 5절에 없음 — q4-02(차이 탐지·반영)는 실행 2026-09-25-75 에서 답했고 좌표 정렬과 층·목적지 이름 맞춤(q4-03)만 남음
- 공간 그래프 스키마 초안 6절: 정렬 정보(제조사·플릿별 좌표 변환)를 층별 지도 속성으로 둘지 별도 개념으로 둘지 미해결(실행 2026-09-25-72 에서 '로봇 지도 좌표계 변환' 속성 제안 거부)
- 공간 그래프 스키마 초안 6절: 형식별 층·장소 식별자(VDA 5050 mapId, Open-RMF 층 이름, MassRobotics planarDatum, LIF layoutLevelId) 대응 규칙 미해결(q4-03·q4-07 관련)
- 6. 지도·공간·위치 모델 11절 열린 질문 oq-027(ISO 21423 공통 좌표계 정의와 대응)·oq-045(지도 층 이름과 승강기 층 이름 대응)·oq-029(GLN 하위 위치·WMS 로케이션 코드와 경유점 대응) 미해결

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q4-03 도면 좌표계와 로봇별 지도 좌표계를 정렬하고 층·목적지 이름을 맞추는 방법은 무엇인가?
3. 관제·상호운용 규격(Open-RMF 플릿 어댑터·traffic-editor, VDA 5050 3.0.0, MassRobotics AMR 상호운용 표준, ISO 21423)은 공통 좌표계의 원점·층 구분과 제조사 지도 좌표 변환을 무엇으로 정하는가? (단계 4 페이지 3절, oq-027 겨냥)
4. 대응점으로 두 좌표계의 변환을 추정하는 방법(유사 변환 최소제곱)과 도면–격자 지도 자동 정합 연구는 무엇을 가정하고 어떤 오차 지표를 주는가? (단계 4 페이지 3절, 21. 온보딩·설정·현장 시운전 oq-077 연결)
5. 층 이름(지도 층, 승강기 층, 실내 지도 표준의 층 순번·약칭)과 목적지 이름(경유점 이름, 스테이션 이름, GLN 하위 위치)은 형식마다 어떻게 표현되며 공통 키가 있는가? (oq-045·oq-029, 10. 설비·건물 시스템 연동·7. 화물·재고·자산 식별과 추적 연결)
6. 국내 실내공간정보 규정은 기준점 선정과 좌표 부여를 어떻게 정하는가? (한국 자료 우선 규칙, oq-044 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇 지도와 RMF 좌표의 변환을 층(지도)마다 따로 구하며, 대응 경유점을 최소 4쌍 권장하고 nudged 라이브러리로 회전·축척·이동을 추정한 뒤 층별 평균제곱오차(MSE)를 기록하게 한다. | ref-153 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | Open-RMF 공식 플릿 어댑터 템플릿 설정은 reference_coordinates 를 층 이름(예: L1)을 키로 하고 그 아래 RMF 좌표 목록과 로봇 좌표 목록을 같은 순서의 대응점 4쌍으로 적게 한다. | ref-105 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | nudged 라이브러리 README 는 이 라이브러리를 반사 없는 유사 변환(이동·축척·회전)에 대한 최소제곱 추정기로 설명하고, 점 집합 크기에 선형인 시간으로 계산하며 평균제곱오차로 적합도를 분석하는 기능을 둔다. | ref-744 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | Umeyama(IEEE TPAMI 13(4), 1991)는 두 점 패턴 사이의 평균제곱오차를 최소화하는 유사 변환(회전·이동·축척)의 해를 제시했으며, 데이터가 크게 오염돼도 회전 대신 반사를 내는 기존 해의 문제를 피한다고 보고했다. | ref-745 | 아니오 | medium | 1991 | — | 원문 미열람 |
| f5 | [사실] | Open-RMF traffic-editor 는 층마다 이름과 고도(미터)를 두고, 실제 거리를 넣은 측정선으로 도면 축척을 정하며, 층 사이 수직으로 겹칠 기준점 2쌍 이상으로 이동·회전·축척 변환을 구하고, 로봇이 작업 목적지로 끝낼 경유점에는 이름을 붙여야 한다고 적는다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 은 위치를 관제와 로봇 사이에 정한 프로젝트 고유 좌표계로 주고 층·구역 구분에 고유 mapId 를 쓰며, initializePosition 동작은 x·y·theta·mapId·lastNodeId 로 자세를 재설정해 승강기 노드에서도 쓸 수 있고, pick·drop 동작은 선택 파라미터 stationName 으로 스테이션을 가리킨다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | ISO/FDIS 21423 소개 자료는 공통 좌표계(CCS)의 원점을 시설 안에서 임의로 고른 한 점(벽·기둥·바닥 위의 점 등)으로 두고 이를 시설의 속성으로 보며, 공유되는 모든 위치 데이터를 그 원점에 대한 미터 단위 위치로 정한다고 전한다. | ref-746 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [사실] | MassRobotics AMR 상호운용 표준 JSON 스키마의 location 은 x·y·angle(쿼터니언)·planarDatum 을 필수로 두고 planarDatum 을 '로봇이 참조하는 planarDatum 의 id'(UUID)로 설명하며, 건물·층을 나타내는 별도 필드는 두지 않는다. | ref-230 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 건물 지도 메시지에서 층(Level)은 이름·고도·이미지·장소·문·주행 그래프를 갖고, 승강기(Lift)는 운행 층을 '층 이름' 문자열 목록(levels)으로 두며 층 사이 정렬에 쓸 수 있는 칸 기준 방향(ref_x·ref_y·ref_yaw)을 둔다. | ref-346, ref-743 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 승강기 상태 메시지(LiftState)는 현재 층·목적 층·운행 가능 층을 주석 없는 문자열(current_floor, destination_floor, available_floors)로만 나타낸다. | ref-286 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | IMDF 1.0.0 의 층(Level)은 지상 출입이 가능한 가장 낮은 층을 순번(ordinal) 0, 지하층을 음수로 두는 물리적 층 순번과 사람이 보는 약칭(short_name, 예: P1)을 따로 가지며, 층 표기 관례가 다른 층을 같은 순번의 여러 Level 로 모델링할 수 있다. | ref-338 | 아니오 | medium | 2021-02 | — | 원문 미열람 |
| f12 | [사실] | GS1 GLN 은 확장 요소로 도크 문·보관 칸·판독 지점 같은 하위 위치를 식별할 수 있으나, 확장 요소는 조직 내부나 거래 당사자 간 합의로만 쓴다. | ref-162 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f13 | [사실] | Carpin(Autonomous Robots, 2008)은 여러 로봇의 점유 격자 지도를 합치기 위해 허프 스펙트럼의 순환 상호상관으로 회전 후보를, 축별 투영 스펙트럼으로 이동을 구해 가중치가 붙은 변환 후보 여러 개를 결정적·비반복적으로 내는 방법을 제안했다. | ref-747 | 아니오 | medium | 2008 | — | 원문 미열람 |
| f14 | [사실] | Kakuma 외(2017)는 SLAM 으로 만든 점유 격자 지도와 건물 평면도를 그래프 매칭으로 대응시키고 정렬해, 로봇이 평면도가 가진 의미 정보(방 이름 등)에 접근하게 하는 방법을 제안했다. | ref-748 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f15 | [사실] | Hou·Kuang·Schwertfeger(ROBIO 2019)는 2D 점유 격자 지도를 방 분할 기반 영역 그래프(Area Graph)로 바꾼 뒤 그 공간에서 투표로 두 지도를 맞추는 방법을 제안하고, 대규모 지도에서 기존 방법보다 성능과 계산 속도가 낫다고 보고했다. | ref-749 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f16 | [사실] | 국토교통부 고시 '실내공간정보 구축 작업규정'은 기준점을 바닥 중심의 고정 시설물이나 선의 교차점에 두고 가상 표시는 피하게 하며, 절대좌표는 지상기준점 측량 성과나 수치지형도 가운데 활용 목적에 맞게 골라 부여하게 한다. | ref-345 | 아니오 | low | 2018-03-05 | — | 원문 미열람 |
| f17 | [사실] | 국가법령정보센터에는 '실내공간정보구축작업규정'의 2021-12-24 판(고시 제2021-1445호) 항목이 있어, 2018-03-05 제정 이후 개정판이 있는 것으로 확인된다. | ref-750 | 아니오 | low | 2021-12-24 | — | 원문 미열람 |
| f18 | [추정] | 확인한 도구·규격을 이 위키가 묶으면 도면–로봇 지도 좌표 정렬 절차 초안은 (1) 시설 공통 좌표계의 원점과 층별 기준점을 도면 위 고정 지점에 정하고, (2) 측정선으로 도면 축척을, 층간 기준점으로 층 사이 변환을 정하며, (3) 제조사·플릿·층마다 대응점(최소 4쌍 권장)으로 유사 변환을 최소제곱 추정하고, (4) 잔차(MSE)를 확인한 뒤, (5) 층·장소 식별자 대응표를 등록하는 순서가 될 것으로 보인다. | ref-746, ref-345, ref-079, ref-153, ref-105, ref-744, ref-745, ref-031, ref-230 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [추정] | 층은 형식마다 Open-RMF 층 이름·승강기 층 이름 문자열, VDA 5050 mapId, MassRobotics planarDatum UUID, IMDF 순번·약칭으로 따로 표현되고 공통 키가 없으므로, ROP 는 물리적 층 순번 같은 한 키에 시스템별 층 식별자를 별칭으로 매다는 층 대응표를 따로 두어야 할 것으로 보인다. | ref-346, ref-743, ref-286, ref-031, ref-230, ref-338 | 아니오 | low | 2026-09-25 | — | — |
| f20 | [추정] | 확인한 추정 방법은 층마다 균일 축척·반사 없는 유사 변환 하나를 가정하므로, 제조사 SLAM 지도에 국소 왜곡이 있으면 층 전체 잔차가 작아도 특정 목적지의 오차가 노드 허용 편차를 넘을 수 있어, 합격 판정은 층 평균 잔차가 아니라 목적지 대응점별 잔차로 해야 할 것으로 보인다. | ref-153, ref-744, ref-745, ref-031, ref-224 | 아니오 | low | 2026-09-25 | — | — |
| f21 | [추정] | 목적지 이름은 공간 그래프의 구역 노드 이름을 기준 키로 두고, 그 아래에 제조사별 경유점 이름(Open-RMF)·노드 id 와 스테이션 이름(VDA 5050)·업무 위치 식별자(GLN 하위 위치 또는 WMS 로케이션 코드)를 대응시키는 대응표로 맞추는 방식이 될 것으로 보인다. | ref-079, ref-031, ref-162, ref-338 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f22 | [추정] | ‘3층 출하 대기장’의 경우, 국내 층 표기상 ‘3층’이 지상 1층을 순번 0 으로 두는 IMDF 식 순번에서는 2 가 될 수 있으므로, 사람이 쓰는 층 이름과 순번·제조사 mapId 를 대응표로 명시하지 않으면 같은 이름이 다른 층으로 해석될 위험이 있어 보인다(설명용 가정 사례). | ref-338, ref-031, ref-743 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f23 | [추정] | 이종 제조사를 연결하는 ROP 는 공통 좌표계 원점·층 대응표·목적지 대응표·제조사별 변환과 그 잔차 확인을 직접 맡고, 제조사 지도 작성과 위치추정은 로봇 쪽 연계 대상으로 두며, 격자 지도–도면 자동 정합 알고리즘은 대응점 입력을 줄이는 시운전 보조 도구 후보로 보는 경계가 될 것으로 보인다. | ref-153, ref-031, ref-746, ref-747, ref-748, ref-749 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: "A minimum of 4 matching waypoints is recommended." nudged.estimate() 로 rotation·scale·translation 을 구하고 nudged.estimate_error() 로 층별 MSE 를 로그에 남긴다(raw 원문 확인, 발행일 미확인, 확인일 기준)
- **f2**: reference_coordinates: L1: rmf: [[20.33, -3.156], …] robot: [[59, 399], …] — 층 키 외에 별도 map_name 필드는 없음(raw 원문 확인, 발행일 미확인, 확인일 기준)
- **f3**: "optimal least squares estimators for the group of nonreflective similarity transformation matrices" — O(n), nudged.analysis.mse 제공. README 는 JavaScript 판(2.x) 기준이며 Open-RMF 가 쓰는 Python 판과의 동일성은 미확인(발행일 미확인, 확인일 기준)
- **f4**: similarity transformation parameters (rotation, translation, and scaling) that give the least mean squared error between two point patterns; 기존 해는 심하게 오염된 데이터에서 반사를 내기도 했다(검색 요약 기준)
- **f5**: "With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived." 목적지 경유점에는 name 이 필요(raw 원문 확인, 발행일 미확인, 확인일 기준)
- **f6**: position is always specified in reference to the project-specific coordinate system; unique mapId for levels; initializePosition 은 node 범위 yes(Elevator); pick 파라미터 stationName(string, optional)(명세 3.0.0, 발행일 미확인, 확인일 기준)
- **f7**: CCS origin point is an arbitrarily selected point within a facility … designated as the (0,0,0) … property of the facility; locational data … relative to the CCS origin point, stated in meters(FDIS 미리보기 검색 요약 기준, 발행판 문구는 미확인)
- **f8**: location required: x, y, angle, planarDatum; planarDatum "Id of planarDatum AMR is referencing"(uuid), z 는 선택. 건물·층 필드 없음(raw 원문 확인, 발행일 미확인, 확인일 기준)
- **f9**: Lift.msg: string[] levels — floor names; ref_x, ref_y, ref_yaw — reference orientation of the lift cabin which can be used to align floors. Level.msg: name, elevation, images, places, doors, nav_graphs(raw 원문 확인, 같은 저장소라 독립 출처 아님)
- **f10**: string current_floor / string destination_floor / string[] available_floors — 추가 주석 없음(raw 원문 확인, 발행일 미확인, 확인일 기준)
- **f11**: the Level that models the lowest floor which supports ground-floor access … MUST have an ordinal equal to 0; short_name 은 물리적 층의 라벨; 표기 관례가 다르면 같은 ordinal 의 Level 여러 개 가능(검색 요약 기준)
- **f12**: extension component may identify sub-locations such as storage bins, dock doors … SHALL only be used internally by an organisation or through mutual agreement between partners(검색 요약 기준, 재인용: 2026-09-25-17)
- **f13**: Hough spectra … circular cross-correlation … multiple local maxima, each associated with a possible rotation; returns n transformations, 가중치로 모호한 경우를 추적(검색 요약 기준)
- **f14**: graph matching to align a floor map with an occupancy grid map generated by SLAM; floor map includes semantic information(검색 요약 기준, 학회명 표기는 요약마다 다름)
- **f15**: general 2D occupancy grid maps are transferred to an area graph representation, then computed through voting; better performance on large-scale maps and faster(검색 요약 기준, 저자 보고)
- **f16**: 기준점(선점)은 공간상의 고정되어 있는 바닥 중심의 시설물을 이용 … 가상적인 표시는 피하여야; 절대좌표 부여는 지상기준점 측량 성과물 또는 수치지형도 중 선택(검색 요약 기준, 해당 조문의 판 미확인)
- **f17**: 행정규칙 실내공간정보구축작업규정 (2021-1445, 20211224) 항목 URL — 개정 내용은 미확인(검색 결과 제목·URL 기준)
- **f18**: 이 위키의 종합. 원점(ISO 21423 FDIS 요약)·기준점 선정(국내 작업규정)·측정선·층간 기준점(traffic-editor)·층별 대응점 4쌍과 MSE(플릿 어댑터)를 한 절차로 묶은 단일 출처는 찾지 못함
- **f19**: 이 위키의 종합. Lift.msg levels·LiftState 층은 주석 없는 문자열, MassRobotics 는 층 필드 없이 planarDatum 만, IMDF 는 ordinal 과 short_name 을 분리
- **f20**: 이 위키의 추론. 플릿 어댑터는 층별 MSE 만 기록하고, VDA 5050 은 노드마다 allowedDeviationXY 를 둔다. 도면–현장 편차 연구(ref-224)는 도면이 부정확할 수 있음을 전제로 함
- **f21**: 이 위키의 종합. traffic-editor 는 목적지 경유점에 이름이 필요하고, VDA 5050 은 stationName, GLN 확장 요소는 조직 내부 합의로만 쓴다. WMS 로케이션 코드와의 대응 사례는 찾지 못함
- **f22**: 이 위키의 추론. IMDF 는 지상 출입 최저층을 ordinal 0 으로 강제하고 short_name 을 따로 둔다. 국내 층 표기 관례와의 대응은 출처로 확인하지 않은 가정
- **f23**: 이 위키의 종합. 플릿 어댑터·VDA 5050 은 관제 쪽에서 좌표 변환을 맡기고, 자동 정합 연구는 SLAM 격자 지도와 평면도 정렬을 다룸. 자동 정합을 물류 관제 시운전에 쓴 사례는 찾지 못함

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-346 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-338 | OGC (Open Geospatial Consortium) / Apple | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 2021-02 | 표준 | medium | 2026-09-25 | https://docs.ogc.org/cs/20-094/ | 예 |
| ref-162 | GS1 | Identifying a physical location - GLN | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/standards/id-keys/gln/physical-location | 예 |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 2018-03-05 | 정부·연구기관 | medium | 2026-09-25 | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 | 예 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 2024-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2408.01737 | 예 |
| ref-743 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Lift.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Lift.msg | 아니오 |
| ref-744 | Palonen, A. (axelpale/nudged GitHub) | nudged — README (Affine transformation estimator e.g. for multi-touch gestures and calibration) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/axelpale/nudged | 아니오 |
| ref-745 | Umeyama, S. (IEEE Transactions on Pattern Analysis and Machine Intelligence 13(4), 376-380) | Least-Squares Estimation of Transformation Parameters Between Two Point Patterns | 1991 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/88573/ | 예 |
| ref-746 | ISO (iTeh Standards 미리보기) | ISO/FDIS 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-09-25 | https://standards.iteh.ai/catalog/standards/iso/f772b16e-582a-4ed4-9f79-0a80ad376f40/iso-fdis-21423 | 예 |
| ref-747 | Carpin, S. (Autonomous Robots) | Fast and accurate map merging for multi-robot systems | 2008 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10514-008-9097-4 | 예 |
| ref-748 | Kakuma, D., Tsuichihara, S., Garcia Ricardez, G. A., Takamatsu, J., & Ogasawara, T. | Alignment of Occupancy Grid and Floor Maps Using Graph Matching | 2017 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/7889504/ | 예 |
| ref-749 | Hou, J., Kuang, H., & Schwertfeger, S. (ROBIO 2019) | Fast 2D Map Matching Based on Area Graphs | 2019 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1911.07432 | 예 |
| ref-750 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 2021-12-24 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) | 예 |

### 출처 요약

- **ref-153**: 플릿 어댑터 통합 튜토리얼. 층별 대응 경유점으로 로봇–RMF 좌표 변환을 추정하고 오차를 확인하는 절차를 설명한다.
- **ref-105**: 플릿 어댑터 템플릿 설정 파일. 층 이름을 키로 한 reference_coordinates(RMF·로봇 대응점)를 둔다.
- **ref-079**: traffic-editor 문서. 층 이름·고도, 측정선 축척, 층간 기준점 변환, 경유점 이름을 설명한다.
- **ref-031**: VDA 5050 3.0.0 명세. 프로젝트 고유 좌표계, 층별 mapId, initializePosition, pick·drop 의 stationName 을 정한다.
- **ref-230**: MassRobotics AMR 상호운용 표준 JSON 스키마. location 은 x·y·angle·planarDatum(UUID)을 필수로 두고 층 필드는 없다.
- **ref-346**: Open-RMF 건물 지도 층 메시지. 이름·고도·이미지·장소·문·주행 그래프를 가진다.
- **ref-286**: Open-RMF 승강기 상태 메시지. 현재·목적·운행 가능 층을 문자열로 둔다.
- **ref-338**: 원문 미열람. 사람 길안내용 실내 지도 형식. Level 에 물리적 층 순번(ordinal)과 약칭(short_name)을 둔다.
- **ref-162**: 원문 미열람. GLN 으로 물리적 위치와 하위 위치를 식별하는 방법. 확장 요소는 내부·합의 사용.
- **ref-345**: 원문 미열람. 실내공간정보 제작 기준 고시. 기준점 선정과 절대좌표 부여 방법을 정한다.
- **ref-224**: 원문 미열람. 부정확한 건축 도면과 라이다 상황 그래프를 결합해 도면–현장 정렬과 편차를 추정한다.
- **ref-743**: Open-RMF 건물 지도 승강기 메시지. 운행 층을 층 이름 문자열 목록으로, 층 정렬용 칸 기준 방향을 둔다.
- **ref-744**: 2D 점 집합에서 이동·축척·회전(유사 변환)을 최소제곱으로 추정하는 라이브러리 README(JavaScript 판). Open-RMF 튜토리얼이 쓰는 Python 판과 같은 방법 계열이다.
- **ref-745**: 원문 미열람. 두 점 패턴 사이 평균제곱오차를 최소화하는 유사 변환의 해를 제시한 논문.
- **ref-746**: 원문 미열람. ISO 21423 최종 국제표준안 미리보기. 공통 좌표계(CCS) 원점을 시설의 속성으로 정의한다고 검색 요약이 전한다.
- **ref-747**: 원문 미열람. 허프 스펙트럼으로 점유 격자 지도 사이 변환 후보를 구하는 지도 병합 방법.
- **ref-748**: 원문 미열람. SLAM 점유 격자 지도와 건물 평면도를 그래프 매칭으로 대응·정렬하는 방법.
- **ref-749**: 원문 미열람. 점유 격자 지도를 영역 그래프로 바꿔 투표로 두 지도를 맞추는 방법.
- **ref-750**: 원문 미열람. 실내공간정보 구축 작업규정의 2021-12-24 판 항목. 개정 내용은 확인하지 못했다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | 2, 3, 4, 5, 6, 8, 9 | q4-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23 (신뢰도 low) — 2절 q4-03 상태 답함, 3절 q4-03 소제목 신설({#q4-03}): 공통 좌표계 원점(ISO 21423 FDIS f7, 국내 작업규정 기준점 f16·f17), 도면 축척·층간 기준점(f5), 제조사별 대응점 유사 변환과 잔차(f1·f2·f3·f4), 관제 규격의 좌표·층 표현(f6·f8·f9·f10), 자동 정합 연구(f13·f14·f15), 층 이름(f11·f19)·목적지 이름(f12·f21), 종합: 정합 절차 초안(f18, mermaid 절차도 권장)·잔차 합격 기준(f20)·‘3층 출하 대기장’ 층 표기 시나리오(f22)·ROP 경계(f23) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건(정합 절차 초안 생성, 검증 승인 전) / 8절 출처 / 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 5 | 아이디어 페이지 5절(트랙 산출물): '좌표 정렬과 층·목적지 이름 맞춤' 소절 신설 — 근거 f1·f5·f6·f7·f8·f9·f11·f12, 구현 가설 f18(정합 절차 초안)·f19·f21·f23(추정). q4-02 소절과 합쳐 도면–현장 정합 절차 초안이 됨을 명시 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(개념 '좌표계 정렬' 추가, 층 '시스템별 층 식별자' 속성)가 승인되면 2절 반영과 v1.1 인상(f1·f2·f5·f6·f8·f9·f10·f11). 미승인 시 6절 '정렬 정보를 층별 지도 속성으로 둘지 별도 개념으로 둘지' 항목과 '형식별 층·장소 식별자 대응 규칙' 항목의 근거 보강(f18·f19·f21) |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 6, 7, 9 | 트랙 floorplan-recognition 단계 4 반영 제안 (f1, f7, f8, f11, f18, f19, f21, f23): 6절(주제 페이지 area06-s6)에 대응점 유사 변환과 잔차 확인·층/목적지 대응표(추정), 7절(주제 페이지 area06-s7)에 ISO 21423 CCS 원점 정의(FDIS 요약)·MassRobotics planarDatum·IMDF 층 순번, 9절에 대응표·변환은 ROP, 지도 작성·위치추정은 연계 대상이라는 경계(추정). oq-027·oq-045 근거 보강 |
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 6 | 트랙 floorplan-recognition 단계 4 반영 제안 (f1, f16, f20, f14, f15): 시운전에서 층별 대응점 4쌍 이상과 목적지별 잔차로 정렬을 합격 판정하는 방법(추정)과 도면–격자 지도 자동 정합 연구, 국내 작업규정의 기준점 선정. oq-077 근거 보강 |
| update | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md | 6 | 트랙 floorplan-recognition 단계 4 반영 제안 (f9, f10, f19): 승강기 층 이름이 주석 없는 문자열이라 지도 층 이름과의 대응표가 필요하다는 점(oq-045 근거 보강) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 유사 변환 | Similarity Transformation | 회전·이동·균일 축척만으로 한 좌표계의 점을 다른 좌표계로 옮기는 변환으로, 대응점 쌍에서 최소제곱으로 추정해 도면·관제 지도와 제조사 로봇 지도를 맞추는 데 쓴다. |
| 공통 좌표계 | Common Coordinate System (CCS, ISO 21423) | ISO 21423 이 시설 안의 한 점을 원점으로 정해 여러 제조사 이동로봇이 위치를 미터 단위로 함께 표현하게 하는 시설 공통 좌표계다(최종안 요약 기준). |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 8건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 도구·규격마다 발행 주체 한 곳(f9 의 두 출처는 같은 Open-RMF 저장소)
    - f3 nudged README 는 JavaScript 판 기준이며 Open-RMF 가 쓰는 Python 판과의 구현 동일성 미확인
    - f7 ISO 21423 CCS 정의는 FDIS 미리보기 검색 요약 기준, 발행판 문구·층별 원점 여부·기준점 개수 미확인(oq-027 미해결)
    - f11 IMDF 층 규칙, f12 GLN, f13~f15 논문은 원문 미열람(검색 요약 범위)
    - f16 작업규정 조문의 판(2018 제정판 또는 2021 개정판) 미확인, f17 개정 내용 미확인
    - f18~f23 은 이 위키의 종합이며 정합 절차·층/목적지 대응표를 제시한 단일 출처는 찾지 못함
    - Open-RMF 승강기 층 이름과 건물 지도 층 이름이 같아야 하는지의 명시 규정은 찾지 못함(oq-045 미해결)
    - 국내 물류센터에서 WMS 로케이션 코드·GLN 하위 위치를 로봇 경유점과 대응시킨 사례는 한국어 검색 2회에서 찾지 못함(oq-029 미해결)
- 범위 경계 위반 의심:
    - f13·f14·f15: 점유 격자 지도 병합·정합 알고리즘은 로봇 쪽 SLAM 과 맞닿지만, 제조사 지도와 도면을 시운전 때 오프라인으로 맞추는 도구 후보로만 제안하고 로봇의 위치추정 자체는 f23 에서 연계 대상으로 명시
    - f12·f21: GLN·WMS 로케이션 코드의 부여·관리 자체는 상위 업무 시스템 경계의 연계 대상이며, ROP 는 대응표만 둔다고 서술
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-153(fleet adapter tutorial)·ref-105(config.yaml)·ref-079(traffic-editor)·ref-230(MassRobotics JSON)·ref-346(Level.msg)·ref-286(LiftState.msg), 신규 ref-743(Lift.msg)·ref-744(nudged README). ref-031 은 입력 원문 텍스트(inbox). MassRobotics README 는 열었으나 좌표 관련 내용이 없어 출처로 쓰지 않음. 나머지 신규 6건(ref-745~ref-750)과 재사용 ref-338·ref-162·ref-345·ref-224 는 원문 미열람이라 신뢰도 상한 medium. 원문을 연 출처도 공통 규칙 0절 6항에 따라 high 를 주지 않음. 검색 16회/40(한국어 3회), 신규 출처 8건/20(ref-743~ref-750, 예약 구간 안), 재사용 11건. 질문 선택: target.json 지정 q4-03 1건. q4-03 은 좌표 정렬(공통 원점 → 도면 축척·층간 기준점 → 제조사·층별 대응점 유사 변환 → 잔차 확인)과 층·목적지 대응표로 답했으나 핵심 종합(f18~f23)이 추정이라 종합 신뢰도 low. 이번 답과 q4-02 답을 합치면 도면–현장 정합 절차 초안이 되지만 반영은 검증 승인 뒤다. 한국 자료: 실내공간정보 구축 작업규정의 기준점 선정(ref-345)과 2021 개정판 존재(ref-750); 국내 물류센터 사례는 찾지 못함. oq-027·oq-045·oq-029 는 근거 보강만 되고 해결로 올리지 않음. 교차 규칙: 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 일반 열린 질문 신규 없음(새 질문은 트랙 전용). 후속 질문 2건. 온톨로지 변경 제안 2건. 정정 요청 없음. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 3건(갱신 상한과 별도).

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 4
- 답한 질문 id: q4-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 제조사 SLAM 지도에 국소 왜곡이 있어 층당 유사 변환 하나의 목적지별 잔차가 노드 허용 편차(VDA 5050 allowedDeviationXY 등)를 넘을 때, 구역별 분할 변환이나 목적지별 보정점을 어떻게 두고 시운전 합격 기준을 무엇으로 정하는가? (q4-03 에서 파생) | 4 | f20 |
| — | 메자닌·중층·지하층·다른 건물 동이 섞인 물류센터에서 물리적 층 순번(IMDF ordinal 등)을 층 대응표의 기준 키로 쓰고 Open-RMF 층·승강기 층 이름, VDA 5050 mapId, MassRobotics planarDatum 을 별칭으로 매달 때, 같은 순번에 여러 표기가 있거나 층이 부분적으로 겹치는 경우를 어떻게 표현하는가? (q4-03 에서 파생) | 4 | f19 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| add | concept | 좌표계 정렬 (Coordinate Alignment) | f1, f2, f5, f6, f8 | 한 층에서 공통(도면·관제) 좌표계와 특정 제조사·플릿 로봇 지도 좌표계 사이의 변환 기록. 속성 후보: 대상 층, 대상 좌표계 식별자(Open-RMF 층 키, VDA 5050 mapId, MassRobotics planarDatum), 대응점 쌍 목록(최소 4쌍 권장), 변환(회전·축척·이동), 잔차(MSE), 작성 시각. 한 층별 지도에 제조사 수만큼 생기므로 층별 지도 속성보다 별도 개념이 맞다는 근거는 f1·f2(층 키 아래 플릿별 설정)이며, 실행 2026-09-25-72 에서 거부된 층별 지도 속성 '로봇 지도 좌표계 변환' 제안과 같은 대상을 다르게 모델링한 것이라 6절 정렬 정보 질문의 결정이 필요하다. 목적지별 잔차 합격 규칙(f20)은 추정이라 정의에 넣지 않는다. |
| modify | concept | 층 (Floor) | f6, f8, f9, f10, f11 | 속성 '시스템별 층 식별자(별칭)'를 더한다: Open-RMF 건물 지도 층 이름·승강기 층 이름 문자열, VDA 5050 mapId, MassRobotics planarDatum UUID, IMDF 순번(ordinal)·약칭(short_name). 기존 속성 '층 이름'·'표준 대응 클래스(후보)'와 충돌하지 않으며, 기준 키를 무엇으로 둘지(f19 추정)는 정의에 넣지 않고 6절 질문으로 둔다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 도면–현장 정합 절차 초안(q4-02 답 + 이번 q4-03 답 f18)은 검증 승인 전이며 공간 그래프 스키마 초안 6절과 아이디어 3. 건축 도면 자동 인식 5절에 아직 반영되지 않음
    - 열린 질문 q4-04·q4-05·q4-07·q4-08·q4-09·q4-10·q4-11
