# 스토리텔러 산출 2026-09-25-72

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | draft | q4-01 답함(보정 여섯 묶음·용도별 지도·ROP 경계, 추정), 후속 질문 2건(q4-09·q4-10), 완료 조건 첫 행 충족(2차 확인)·둘째 행 미충족, 상태 줄 진행 중; 2차: 시나리오 제약 칸 비용 지도 필터 문장을 Nav2 로 한정 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v0.9 → v1.0: 층별 지도 교환 형식(후보)의 Nav2 격자 지도 값에 딸린 속성 '내비게이션 지도 메타데이터' 추가(f1); 거부된 '로봇 지도 좌표계 변환'은 6절 정렬 정보 질문 근거 보강(f5); 6절에 보정 항목·용도별 지도·운영 규칙 마스크 질문 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 상태 줄 갱신(현재 단계 단계 4, 마지막 트랙 실행 2026-09-25), 6절 산출물 링크에 스키마 초안 v1.0·q4-01 답·후속 질문 2건 반영 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절 끝에 '내비게이션 지도 변환 보정' 소절 추가(q4-01, 추정), 도면–현장 정합 절차 미조사 명시, 새 각주 5건 정의 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 4 | q4-01 답함(내비게이션 지도 변환 보정 여섯 묶음·용도별 지도·ROP 경계, 추정), 공간 그래프 스키마 초안 v1.0, 후속 질문 2건 | run 2026-09-25-72
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 4: q4-01(도면 인식 결과를 로봇 내비게이션 지도로 바꿀 때의 보정) 답함, 공간 그래프 스키마 초안 v1.0 (실행 2026-09-25-72)
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 4에서 내비게이션 지도 변환 보정 여섯 묶음과 ROP·로봇 쪽 경계를 추정으로 정리, 세부영역 반영 제안 3건 (실행 2026-09-25-72)
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 4 q4-01 답(내비게이션 지도 변환 보정), 6절·9절 반영 제안 (실행 2026-09-25-72)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 비용 지도 | Costmap | 로봇 경로 계획을 위해 점유 격자 지도 위에 장애물, 로봇 외형에 따른 여유(인플레이션), 필터 마스크로 적용한 금지 구역·속도 제한 같은 비용을 칸마다 매긴 격자 지도다. | 6, 15 | ref-644 |
| new | 필터 마스크 | Filter Mask (Nav2 costmap filter) | Nav2 에서 금지 구역·속도 제한처럼 공간별 동작 규칙을 표시하는 별도 래스터 지도로, 일반 지도와 같은 이미지+YAML 형식으로 배포되어 비용 지도 필터로 비용 지도에 적용된다. | 6, 15, 16 | ref-644, ref-645 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-440 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_map_server — README | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-082 | Vega-Torres, M. A. (MigVega GitHub) | Ogm2Pgbm — README (Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments) | 오픈소스 문서 | medium | https://github.com/MigVega/Ogm2Pgbm |
| ref-081 | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2308.05443 |
| ref-628 | Lee, H.-C., Woo, H.-M., & Shin, S. (International Journal of Precision Engineering and Manufacturing) | Digital Twin-based Sensor-Free Virtual Mapping for Autonomous Mobile Robot Localization | 논문 | medium | https://link.springer.com/article/10.1007/s12541-026-01598-2 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 논문 | medium | https://arxiv.org/abs/2408.01737 |
| ref-270 | Macenski, S. (SteveMacenski GitHub) | slam_toolbox — README (Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS) | 오픈소스 문서 | medium | https://github.com/SteveMacenski/slam_toolbox |
| ref-644 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_costmap_2d — README | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md |
| ref-645 | Open Navigation (Nav2 documentation) | Navigating with Keepout Zones — Nav2 documentation | 오픈소스 문서 | medium | https://docs.nav2.org/tutorials/docs/navigation2_with_keepout_filter.html |
| ref-646 | IEEE 학술대회 논문 저자(미확인) | BIM-to-Robot Mapping: Constructing IFC-Referenced Occupancy Grids and Semantic Metadata for Rule-Based Navigation | 논문 | medium | https://ieeexplore.ieee.org/document/11019519/ |
| ref-647 | Construction Robotics(Springer) 게재 논문 저자(미확인) | Improving autonomous robotic navigation using IFC files | 논문 | medium | https://link.springer.com/article/10.1007/s41693-023-00112-8 |
| ref-648 | Tibebu, H., Roche, J., De Silva, V., & Kondoz, A. (Loughborough University London, Sensors 21(7), 2263) | LiDAR-Based Glass Detection for Improved Occupancy Grid Mapping | 논문 | medium | https://www.mdpi.com/1424-8220/21/7/2263 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 수행 자원 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 제약 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 완료·인계 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 예외·성과 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01 | 단계 4. 지도 변환 보정과 현장 정합 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) | 오픈소스 | ROS Navigation (ros-navigation/navigation2) | 6, 15 | ref-644 | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md |

## 추가 조사 요청

- 단계 4 페이지 3절 q4-01: 보정 여섯 묶음(추정)을 교차 확인할 독립 출처 — 도면·BIM 에서 로봇 내비게이션 지도로 가는 변환 절차를 정리한 문헌이나 제조사 중립 가이드가 필요하다(현재 교차 확인 0건).
- 단계 4 페이지 3절: ref-081(arXiv 2308.05443) 원문에서 창문·문·가구를 요소 유형 의미로 지도에서 제외했는지 확인 — 현재 검색 요약 기준이라 [추정]으로 강등됐다.
- 단계 4 페이지 3절: 거울·광택 금속 면 같은 유리 외 반사면이 라이다 점유 격자 지도에 주는 영향을 다룬 출처 — ref-648 스니펫은 유리만 뒷받침한다.
- 단계 4 페이지 3절: ref-647 원문에서 진입 불가 공간을 장애물로 칠한 흑백 점유 지도 로드 방식을 확인 — 검색 요약에 없어 본문에서 뺐다.
- 단계 4 페이지 3절 시나리오 제약 칸: VDA 5050 로봇·Open-RMF 플릿 어댑터 로봇이 금지 구역·속도 제한을 어떤 방식(VDA 5050 구역 집합, 제조사 내비게이션 스택 등)으로 적용하는지에 대한 근거 — 현재는 Nav2 로 한정해 적었다.
- 단계 4 q4-02·q4-03: 도면–현장 정합 절차 초안(차이 탐지, 좌표 정렬 합격 기준, 층·목적지 이름 대응)의 근거 — 완료 조건을 채우는 데 필요하다. 국내 물류센터 사례(oq-022) 우선.

## 이행한 수정 지시

- f7 분리 — 단계 4 페이지 3절에서 BIM 추출 점유 격자 지도·AMCL 연구의 가정과 가구·설계–시공 편차 영향은 [사실]로, 창문·문·가구 제외 부분은 '검색 요약 기준'을 밝힌 [추정] 문장으로 따로 썼다.
- f10 흑백 점유 지도 부분 — 단계 4 페이지에서 흑백 점유 지도로 불러온다는 부분을 빼고, IFC→의미별 장애물 지도·시뮬레이션 환경·JSON·경유점 생성과 사전 지도 작성 주행 불필요만 [사실]로 썼다.
- f14 축소와 ref-648 정정 — 유리가 라이다에 잘 보이지 않아 점유 격자 지도 작성을 어렵게 한다는 주장만 [사실]로 쓰고 거울·금속·반사 잡음은 뺐으며, ref-648 기관을 Tibebu 외(Loughborough University London, Sensors 21(7), 2263), 발행일을 2021-04 로 각주와 reference_updates 에 반영했다.
- f7·f8·f16 연계 대상 — 세 문장 앞에 '연계 대상:'을 붙이고, 3절 머리에 위치추정·SLAM 은 분류 원문 9장 '로봇 자체 지능·제어' 쪽이며 지도 형식·좌표·판 관리 관점으로만 다룬다고 밝혔다.
- f8 의 78% 개선 — 본문 어디에도 쓰지 않았다.
- f12 연계 대상과 f19 경계 — 비용 지도 인플레이션·필터 적용이 로봇 쪽 내비게이션 스택 기능(연계 대상)임을 밝히고, ROP 쪽을 규칙의 공통 정의와 판 관리로 한정한 f19 문장은 [추정]으로 유지했다.
- f17·f18 근거 요약 — 강등된 창문 제외·흑백 지도·거울 세부를 사실처럼 인용하지 않고 '유리처럼 센서가 잘 못 보는 요소', '의미 정보로 요소를 거른 연구가 있다는 검색 요약' 수준으로 낮췄으며, 두 종합에 [추정]과 '이 위키의 종합, 단일 출처 없음'을 유지했다.
- 온톨로지 승인 — 공간 그래프 스키마 초안 층별 지도 행의 '교환 형식(후보)' Nav2 격자 지도 값에 딸린 속성 '내비게이션 지도 메타데이터(해상도·원점·점유/빈 공간 임계값)'를 더하고 근거 칸에 'finding f1 (실행 2026-09-25-72)[^ref-440]'을 적었으며 상태는 확정을 유지했다.
- 온톨로지 거부 — '로봇 지도 좌표계 변환' 속성은 표에 넣지 않고 6절의 정렬 정보 항목에 근거 보강으로 f5 문장을 [사실][^ref-153]으로 적었다.
- 버전 1.0 — ontology_version 을 '1.0'으로 하고 H1 (v1.0), 프런트매터, track_updates.ontology_draft_version 을 같게 맞췄으며(auto 상태 줄은 퍼블리셔가 채운다), 2절 변경 설명 문단에 v1.0 의 승인·거부 내용을 한 문장씩 더했다.
- 단계 4 페이지 6절 — 두 행 모두 충족 여부 '미충족', 검증 판정 '미충족 · 미승인'으로 쓰고 표 아래 줄을 '다음 단계로 전환: 아니오(도면–현장 정합 절차 초안 없음; 막힌 질문 q4-02·q4-03·q4-04·q4-05·q4-07·q4-08)'로, 상태 줄 단계 상태를 '진행 중'으로 두었다.
- 단계 4 페이지 2절·3절·4절 — q4-01 을 답함(2026-09-25-72, #q4-01)으로 바꾸고 3절에 '### q4-01 … {#q4-01}' 소제목을 두었으며 4절에 핵심 결론이 [추정]이고 종합 신뢰도 low 임을 밝혔다.
- 각주 원문 미열람 — ref-081·ref-628·ref-224·ref-645·ref-646·ref-647·ref-648 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 원문을 연 ref-440·ref-079·ref-153·ref-080·ref-082·ref-270·ref-644·ref-031 에는 붙이지 않았다.
- ref-646·ref-647 — 기관 칸을 저자 미확인으로 두고 ref-646 발행일을 각주 '미확인', JSON null 로 두었다.
- 세부영역 반영 제안 — 6. 지도·공간·위치 모델과 21. 온보딩·설정·현장 시운전 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그 '세부영역 반영 제안'으로만 냈으며, 6절 제안에서 f5 는 기존 6절 문장의 ref-153 각주 재사용으로 적었다.
- 용어집 — '필터 마스크' 정의에 sources ref-644·ref-645 를 달고, '비용 지도'는 점유 격자 지도 위에 비용을 매긴 격자로 설명하며 금지 구역은 필터 마스크 적용으로 표현했다.
- 새 질문 — q4-09(origin f18)·q4-10(origin f12)을 stage 4 로 backlog_updates 에 등록하고 단계 페이지 2절·5절에도 같은 근거로 적었다.
- 2차: 시나리오 제약 칸 드리프트 — 단계 4 페이지 3절 '현장 시나리오: 3층 출하 대기장 도착 판정' 표의 제약 칸 문장을 'Nav2 를 쓰는 로봇에서는 금지 구역·속도 제한이 로봇 쪽 비용 지도 필터로 적용된다. [사실][^ref-644]'로 Nav2 에 한정했다.
- 2차: 완료 조건 첫 행 — 단계 4 페이지 6절 표 첫 행(보정 항목 목록의 반영)의 충족 여부를 '충족', 근거를 '두 페이지에 반영됨(q4-01 답, 종합은 추정)', 검증 판정을 '충족(2차 확인)'으로 고쳤고, 둘째 행 '미충족 · 미승인', 표 아래 '다음 단계로 전환: 아니오(…)' 줄, 상태 줄의 '완료 조건: 미충족'·'진행 중'은 그대로 두었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
- 온톨로지 초안 버전: 1.0
- 트랙 로그 항목: 답한 질문: q4-01(보정 여섯 묶음·용도별 지도·ROP 경계, 핵심 종합은 추정, 신뢰도 low) / 새 질문: q4-09(f18), q4-10(f12) / 온톨로지 변경: v0.9 → v1.0: 층별 지도 교환 형식(후보)의 Nav2 격자 지도 값에 딸린 속성 '내비게이션 지도 메타데이터(해상도·원점·점유/빈 공간 임계값)' 추가(f1); 거부: 층별 지도 속성 '로봇 지도 좌표계 변환'(f5 → 6절 정렬 정보 질문 근거 보강, q4-03). 버전 이력 행: 1.0 / 2026-09-25 / v0.9 → v1.0: 층별 지도 '내비게이션 지도 메타데이터' 추가(f1); 거부: '로봇 지도 좌표계 변환'(f5 → 6절 질문); H1 버전 표기 v1.0 / 2026-09-25-72 / 완료 조건 평가: 미충족(보정 항목 목록의 스키마 초안 6절·아이디어 5절 반영은 충족(2차 확인); 부족: 도면–현장 정합 절차 초안 없음; 막힌 질문 q4-02·q4-03·q4-04·q4-05·q4-07·q4-08) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건(6. 대표 접근법과 기술, 9. ROP가 직접 맡는 것과 외부와 연계하는 것), 21. 온보딩·설정·현장 시운전 1건(6. 대표 접근법과 기술) / 다음 실행 제안: q4-03, q4-02
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 8, 답함 1, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-01 | 답함 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-01 | — | — | — |
| q4-09 | 열림 | — | 도면 한 장에서 경로 계획용 지도, 위치추정용 지도, 운영 규칙 마스크를 따로 만들 때 유리벽·창문·문·가구 같은 요소를 어느 지도에 어떻게 넣을지 정하는 규칙은 무엇이며, 그 규칙이 맞는지 시운전에서 어떻게 확인하는가? (q4-01 에서 파생) | 4 | f18 |
| q4-10 | 열림 | — | 금지 구역·속도 제한 같은 운영 규칙을 도면 기반 공간 그래프에서 한 벌로 정의해 Nav2 필터 마스크와 VDA 5050 구역 집합처럼 형식이 다른 대상으로 내보낼 수 있는가, 내보낼 때 무엇이 빠지는가? (q4-01 에서 파생) | 4 | f12 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 도면 기반 지도를 로봇 내비게이션 지도로 쓰기 전 보정 여섯 묶음(좌표·축척, 층 정렬, 제조사 좌표계 변환과 오차, 표현 보정, 도면–현장 편차, 운영 규칙 층, [추정], f17)과 traffic-editor 의 측정선 축척·세로축 반전·층 기준점 정렬([사실], f2·f3, ref-079). 대응점 기반 좌표 변환·오차 확인(f5)은 기존 6절 문장과 같으므로 새 문장 없이 기존 ref-153 각주를 재사용한다. |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 보정 가운데 도면 좌표·축척·층 정렬, 제조사 지도 좌표계 변환과 오차 확인, 금지 구역·속도 제한 규칙의 공통 정의와 판 관리는 ROP 쪽, 장애물 채움·비용 지도 인플레이션·SLAM 재정합·위치추정 지도 갱신은 로봇·제조사 쪽 연계 대상이라는 경계([추정], f19, ref-153·ref-031·ref-644·ref-270·ref-082). |
| 21 | 6. 대표 접근법과 기술 | 시운전에서 도면 기반 지도의 좌표 변환 오차를 대응 경유점(최소 4쌍 권장)으로 확인하는 절차([사실], f5, ref-153)와 이를 노드 허용 편차와 비교해 도착 판정 전에 확인하는 단계([추정], f20), 사전 지도 작성 주행을 줄인 연구(IFC 기반 지도 생성 [사실] f10 ref-647, 연계 대상: CAD 기반 가상 지도 위치추정 f9 ref-628). |
