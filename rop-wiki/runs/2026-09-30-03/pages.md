# 스토리텔러 산출 2026-09-30-03

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | draft | 영역 심화: 3~11절 신규 작성(병원·기타 적용 사례, 평면도 인식·BIM 변환·도면 기준 정합, 책임 경계, 연결 10개 영역, 열린 질문 6건), 13절 각주 15건. 2차 수정: 3절 f20·f21 문장과 9절 f24 문장에 태그·각주 추가, 4절 설계–준공 편차 설명의 [의견] 각주를 떼고 용어 사용 설명으로 바꿈, 8절 BIM-SLAM 항목에 '연계 대상' 표시 |
| create | docs/topics/2026/2026-09-30-area14-s6.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "6. 대표 접근법과 기술" 절(1,924자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area14-s4.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "4. 핵심 개념과 용어" 절(1,101자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area14-s8.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "8. 대표 연구와 자료" 절(1,017자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area14-s11.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "11. 열린 질문" 절(880자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area14-s10.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(825자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area14-s3.md | draft | 자동 분리: 14. 도면·BIM에서 지도 만들기 의 "3. 왜 중요한가" 절(748자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 14. 도면·BIM에서 지도 만들기 | 영역 심화: 3~11절 신규 작성(병원·기타 적용 사례, 평면도 인식·BIM 변환·도면 기준 정합), 1차 조건부 승인 수정 13건과 2차 수정 4건 이행 | run 2026-09-30-03
- 홈 최근 업데이트: 2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화로 3~11절 작성(평면도 인식·BIM→지도 변환·도면 기준 정합, 병원 적용 사례)
- 대분류 최근 업데이트: 2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화로 3~11절 작성, 15. 지도·공간·위치 모델과 좌표 정합 역할을 나눔
- 세부영역 최근 업데이트: 2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화 3~11절 신규 작성, 각주 15건, 새 열린 질문 4건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 층 정렬 기준점 | Fiducial (Level Alignment Fiducial) | 기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다. | 14, 15 | ref-079 |
| new | 공간 경계 | Space Boundary (IfcRelSpaceBoundary) | IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다. | 14, 16 | ref-156 |
| new | 설계–준공 편차 | As-planned vs As-built Deviation | 설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이 자체로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다. | 14, 16, 18 | ref-081 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-153 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-156 | buildingSMART International | IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md |
| ref-213 | buildingSMART International | IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 논문 | medium | https://arxiv.org/abs/1904.01920 |
| ref-1015 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017) | Raster-to-Vector: Revisiting Floorplan Transformation | 논문 | medium | https://art-programmer.github.io/floorplan-transformation.html |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2105.07147 |
| ref-1017 | Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021) | Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization | 논문 | medium | https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/ |
| ref-081 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022) | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2308.05443 |
| ref-1019 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 정부·연구기관 | high | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 |
| ref-817 | 모빌리오(Mobilio Robotics) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션) | 벤더 문서 | low | https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv) | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 논문 | medium | https://arxiv.org/abs/2507.00552 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023) | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 논문 | medium | https://arxiv.org/abs/2408.15870 |
| ref-1024 | 엔지니어링데일리 | "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개 | 기사 | low | https://www.engdaily.com/news/articleView.html?idxno=12613 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가? | 14, 45 | 열림 | — |
| new | — | AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 14, 45 | 열림 | — |
| new | — | 도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 벤더 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가? | 14, 15, 55 | 열림 | — |
| new | — | 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? | 14, 22 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 작업 대상 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 병원 | 수행 자원 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 병원 | 제약 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 병원 | 예외·성과 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 기타 | 작업 대상 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 기타 | 수행 자원 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |
| 기타 | 예외·성과 | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시 | 14. 도면·BIM에서 지도 만들기 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 5절 적용 사례: 물류창고·제조 공장·상업 시설에서 도면·BIM 기반 로봇 지도를 실제로 쓴 독립 출처 사례(벤더 주장 외)가 필요하다 — 현재 병원 1건과 기타(연구 시험) 1건뿐이다.
- 5절 병원 사례: 타르투 대학병원 시험의 시작 조건(검체 운반 요청 방식)과 완료·인계(수령 확인) 근거가 필요하다 — 두 칸을 미확인으로 두었다.
- 9·11절: 도면–로봇 지도 정합 결과를 누가 언제 승인·확정하는지(oq-126) 다룬 제품 문서·현장 절차 자료가 필요하다.
- 3절: 국토교통부 BIM 활성화 로드맵 원문 보도자료(2020-12-29)와 이후 이행 상황 자료가 필요하다 — 현재 기사 단독 출처라 [추정]으로 강등했다.
- 7절: IFC 4.3 ADD2 게시판(또는 ISO 16739-1:2024)의 IfcSpace·IfcTransportElement 문구 확인이 필요하다 — 현재 개발 저장소 문서 기준이다.
- 11절: 건설 현장 등 변하는 공간에서 로봇 지도와 BIM 의 동기화 주기·국내 사례(oq-193) 자료가 필요하다.
- 다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 대응점 기반 좌표 변환(reference_coordinates, nudged) 반영, 45. 문서·도면·장면 이해 페이지에 CubiCasa5K·Raster-to-Vector·FloorPlanCAD·AI Hub 건축 도면 데이터 반영.
- 분리 코드 담당 요청(2차 검증 참고 사항): 자동 분리 뒤 세부영역 페이지의 프런트매터 sources 와 reference_updates 의 cited_by 를 분리된 주제 페이지 인용 결과에 맞춰 갱신해야 한다.

## 이행한 수정 지시

- f20 강등 — 3절의 국토교통부 BIM 로드맵 문장을 [추정]으로 쓰고 '조사·설계·발주·조달·시공·감리·유지관리 등 전 생애주기', 'LH 공동주택'으로 고쳤으며 '2020-12 발표 기준이며 이후 이행 상황은 미확인'을 덧붙였다.
- ref-1024 정정 — 13절 각주의 발행일을 2020-12-28, 제목을 '"설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개'로 고치고 reference_updates 의 published 를 2020-12-28 로 넣었으며, 3절 문장에 기사 날짜(2020-12-28)와 2020-12 기준을 적었다.
- ref-1019·f14 정정 — 13절 각주 발행일을 2023-07-26 으로, reference_updates 의 published 를 2023-07-26 으로 넣고, 8절 AI Hub 문장의 기준일을 '2023-12-15 최종개방 기준'으로 적었다.
- f16 경계 — 6절에서 BIM→점유 격자·포즈 그래프 지도 생성은 접근법으로 쓰고, AMCL 대비 강건성은 별도 문장으로 로봇 자체 지능·제어 쪽 연구 결과이자 연계 대상이라고 밝혔으며, 9절 직접 범위에는 넣지 않고 연계 열에 '위치 추정과 그 성능'으로만 두었다.
- Scan-BIM 편차 용어 — 4절에서 'Scan-BIM 편차'를 처음 쓰는 자리에 용어집 스캔 대 BIM 비교(Scan-vs-BIM) 링크를 달고, 설계–준공 편차가 비교 방법이 아니라 모델과 실제의 차이 자체임을 본문과 glossary_updates 정의·설명에서 구분했다.
- f5·f6 중복 방지 — 6절 '축척 보정과 도면 기준 정합' 소절 첫머리에 도면을 기준 좌표로 쓰는 정합 절차로 한정한다고 밝히고 7절 표도 '도면 기준 좌표계 사이 변환'으로 적었으며, 좌표계 통합 일반론은 10절에서 15. 지도·공간·위치 모델로 연결만 했다.
- 5절 사례 칸 — 병원 사례의 시작 조건·완료·인계를 '미확인'으로 두고, 기타 사례는 상용 운영이 아닌 대학 건물 위치 추정 연구 시험이자 연계 대상임을 제목·서술에 밝히고 근거 없는 시작 조건·제약·완료·인계를 '미확인'으로 두었으며, site_matrix_updates 는 실제로 채운 칸(병원 4칸, 기타 3칸)만 냈다.
- f19 — 6절 제품 사례로만 쓰고 '[추정] 벤더 주장'을 병기했으며, 5절 사례와 site_matrix_updates 근거로 쓰지 않았다.
- f9·f10 — 7절 표 아래에 IFC 4.3 두 행이 buildingSMART 개발 저장소(ifc4.3-main) 문서 기준이며 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있음을 밝혔다.
- f12 — 6절에서 약 90% 정밀도·재현율과 수십만 장 변환을 '저자들이 보고했으며 교차 확인되지 않은 저자 보고'로만 서술하고 일반화하지 않았다.
- open_questions_new 1번 — '주로 주거용 도면 기준인데' 전제를 빼고 '보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가?' 형식으로 11절과 open_question_updates 에 옮겼다.
- open_questions_new 2번 — '승강기·계단'을 빼고 '충전 위치처럼 로봇 운영에 필요한 클래스'로 좁혀 11절과 open_question_updates 에 옮겼다.
- oq-126·oq-193 — 해결로 바꾸지 않고 11절에 '상태: 열림'으로 싣고 확인된 근거와 아직 답하지 못한 부분을 한 문장씩 덧붙였으며, open_question_updates 에 상태 변경을 내지 않았다.
- 2차: f20 — 3절 마지막 문단에서 '국내에서도 BIM 적용을 넓히려는 정책이 발표됐는데'를 보도 내용 문장과 한 문장으로 합치고, 그 문장 끝에 [추정][^ref-1024]를 붙였다(단서 문장의 태그도 유지).
- 2차: f21 — 3절 셋째 문단의 '… 연구 수준에서 자동화가 진행됐다.' 문장 끝에 [추정][^ref-1015][^ref-067][^ref-081][^ref-083]을 붙였다.
- 2차: f24 — 9절의 '로봇의 SLAM·LiDAR 위치 추정은 … 건물 소유자·설계·시공 측 체계에 속한다.' 문장 끝에 [추정][^ref-1017][^ref-081][^ref-221][^ref-213][^ref-1024]를 붙였다.
- 2차: 설계–준공 편차 — 4절 해당 항목의 '[의견][^ref-081]' 문장에서 태그와 각주를 떼고, '이 위키에서 설계–준공 편차는 … 차이 자체를 가리키는 용어로 쓴다.'라는 태그 없는 용어 사용 설명으로 바꿨다(glossary_updates 설명도 '이 위키는 … 말로 쓴다'로 맞춤).
- 분량 초과 자동 분리: 14. 도면·BIM에서 지도 만들기 본문 9,510자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,887자
