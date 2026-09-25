# 스토리텔러 산출 2026-09-25-17

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | draft | 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 트랙 반영 제안 가운데 브리프 근거가 있는 것(평면도 인식·데이터셋·traffic-editor·경로 지도 요건·9절 경계)만 반영 |
| create | docs/topics/2026/2026-09-25-area06-s7.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: GS1 GLN 행을 [사실] 식별 문장과 [추정] 대응 문장으로 나눔 |
| create | docs/topics/2026/2026-09-25-area06-s6.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "6. 대표 접근법과 기술" 절(1,863자)을 옮겼다. 형식 수정: 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 위치 기준 경로로 고침 |
| create | docs/topics/2026/2026-09-25-area06-s8.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "8. 대표 연구와 자료" 절(1,701자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area06-s4.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "4. 핵심 개념과 용어" 절(1,382자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area06-s10.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,143자)을 옮겼다. 형식 수정: 세부영역 링크 11건을 주제 페이지 위치 기준 경로(../../categories/…)로 고침 |
| create | docs/topics/2026/2026-09-25-area06-s3.md | draft | 자동 분리: 6. 지도·공간·위치 모델 의 "3. 왜 중요한가" 절을 옮겼다. 2차 수정: MassRobotics 평면 기준 부재 문장에 '(스키마 파일 기준, 부재 확정 아님)' 한정 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 6. 지도·공간·위치 모델 | 영역 심화: 3~11절 신규 작성(좌표계 정렬·지도 판·위치 신뢰도·도면–현장 차이·평면도 인식), 트랙 반영 제안 가운데 브리프 근거가 있는 것만 반영 | run 2026-09-25-17
- 홈 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 영역 심화로 3~11절 작성(제조사 지도의 좌표계 정렬, 지도 판 관리, 위치추정 신뢰도, 도면–현장 차이, 평면도 인식)
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 영역 심화로 3~11절 작성, VDA 5050·MassRobotics·Open-RMF 위치 표현 비교와 ‘3층 출하 대기장’ 출하 시나리오 추가
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 3~11절 신규 작성, 열린 질문 3건 신규·oq-022 연결, 트랙 반영 제안 일부 반영(osmAG·BIM 지도 생성 연구는 근거 부족으로 보류)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| update | IndoorGML | IndoorGML | 실내 공간을 셀 공간(CellSpace)과 그 경계, 공간 연결을 나타내는 노드·엣지의 쌍대 그래프, 의미별 주제 레이어로 표현하는 OGC 실내 공간 정보 표준이다. | 6, 28 | ref-158 |
| update | 산업 기초 클래스 | Industry Foundation Classes (IFC) | buildingSMART 의 BIM 데이터 스키마로, IFC 4.3 은 건물 안에서 특정 기능을 제공하는 경계 지어진 면적·체적을 IfcSpace 로 정의하고 건물 층(IfcBuildingStorey)에 집합 관계로 연결한다. | 6, 28 | ref-157 |
| new | 레이아웃 교환 형식 | Layout Interchange Format (LIF) | 무인운반차 통합사가 노드·간선·스테이션으로 이루어진 주행 레이아웃을 제3자 중앙 관제 시스템에 넘기기 위해 VDMA 가 정한 교환 형식이다. | 6, 9, 28 | ref-046, ref-031 |
| new | 지도 정합 | Map Alignment | 서로 다른 로봇·도면의 지도 좌표계를 대응점으로 구한 회전·축척·이동 변환으로 공통 좌표계에 맞추는 일이다. | 6, 9, 21 | ref-154, ref-105, ref-079 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-155 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/location_2D.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/location_2D.json |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html |
| ref-154 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-156 | ROS (ros-infrastructure/rep) | REP 105 -- Coordinate Frames for Mobile Platforms | 오픈소스 문서 | high | https://www.ros.org/reps/rep-0105.html |
| ref-157 | buildingSMART International | IFC 4.3 documentation — IfcSpace (IFC4.3.x-development) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md |
| ref-158 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | IndoorGML-SWG — README and OGC IndoorGML 2.0 Part 2a – XML Encoding (26-042, Candidate SWG Draft) | 표준 | medium | https://github.com/opengeospatial/IndoorGML-SWG |
| ref-159 | ISO | ISO 19164:2024 - Geographic information — Indoor feature model | 표준 | medium | https://www.iso.org/standard/83153.html |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (LIF – Layout Interchange Format, Version 1.0.0) | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-161 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |
| ref-162 | Prakhya, S. M., Yang, L., & Liu, Z. | Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems | 논문 | medium | https://arxiv.org/abs/2501.18110 |
| ref-163 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 논문 | medium | https://journals.sagepub.com/doi/10.1177/02783649241287797 |
| ref-164 | GS1 | Identifying a physical location - GLN | 표준 | medium | https://www.gs1.org/standards/id-keys/gln/physical-location |
| ref-165 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 논문 | medium | https://arxiv.org/abs/2408.01737 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 논문 | medium | https://arxiv.org/abs/1904.01920 |
| ref-064 | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 오픈소스 문서 | medium | https://github.com/zlzeng/DeepFloorplan |
| ref-065 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 오픈소스 문서 | medium | https://github.com/art-programmer/FloorplanTransformation |
| ref-066 | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 오픈소스 문서 | medium | https://floorplancad.github.io/ |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2105.07147 |
| ref-069 | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 오픈소스 문서 | medium | https://github.com/MLSTRUCT/MLStructFP |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 오픈소스 문서 | medium | https://github.com/SizheHu/Raster-to-Graph |
| ref-071 | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 오픈소스 문서 | medium | https://github.com/m-agour/ResPlan |
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2503.22346 |
| ref-074 | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 정부·연구기관 | medium | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 논문 | medium | https://arxiv.org/abs/2409.12842 |
| ref-078 | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 논문 | medium | https://arxiv.org/abs/2408.01526 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? | 6, 28 | 열림 | — |
| new | — | 제조사마다 계산 방식이 다른 위치추정 신뢰도(VDA 5050 localizationScore 등)나 신뢰도 필드가 없는 로봇의 위치 보고를 ROP 가 같은 기준으로 수용·거부하는 방법이 있는가? | 6, 8 | 열림 | — |
| new | — | 국내 물류센터에서 GLN 하위 위치나 WMS 로케이션 코드를 로봇 지도 위 경유점·스테이션과 대응시켜 목적지로 쓰는 사례가 있는가? | 6, 7 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |
| 출하 | 작업 대상 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |
| 출하 | 수행 자원 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |
| 출하 | 제약 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |
| 출하 | 완료·인계 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |
| 출하 | 예외·성과 | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 6. 지도·공간·위치 모델 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| LIF (Layout Interchange Format) 1.0.0 | 표준 | VDMA | 6, 9, 28 | ref-046 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ISO 21423 Industrial mobile robots — Communications and interoperability | 표준 | ISO | 6, 9, 28 | ref-161 | https://www.iso.org/standard/86749.html |
| IFC 4.3 (IfcSpace) | 표준 | buildingSMART International | 6, 28 | ref-157 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md |
| OGC IndoorGML 2.0 | 표준 | OGC | 6, 28 | ref-158 | https://github.com/opengeospatial/IndoorGML-SWG |
| ISO 19164:2024 Indoor feature model | 표준 | ISO | 6, 28 | ref-159 | https://www.iso.org/standard/83153.html |
| GS1 GLN (Global Location Number) | 표준 | GS1 | 6, 7 | ref-164 | https://www.gs1.org/standards/id-keys/gln/physical-location |
| REP 105 Coordinate Frames for Mobile Platforms | 프레임워크 | ROS (ros-infrastructure/rep) | 6, 9 | ref-156 | https://www.ros.org/reps/rep-0105.html |

## 추가 조사 요청

- 7. 관련 표준·프레임워크·오픈소스 절: ISO 21423 발행판(또는 FDIS) 원문에서 공통 좌표계(CCS)의 정의와 기준점 개수를 확인해야 한다 — 현재는 출처가 불분명한 해설 요약뿐이다.
- 7. 관련 표준·프레임워크·오픈소스 절: LIF 최신판(VDMA 2024-03)의 레벨·좌표·스테이션 필드를 확인해야 한다 — README 1.0.0(2023-09) 범위만 확인했다.
- 6. 대표 접근법과 기술·8. 대표 연구와 자료 절: 트랙 반영 제안(2026-09-25-11)의 osmAG·osmAG-from-cad, ifc2indoorgml, Ogm2Pgbm, Boniardi 외, Vega-Torres 외, BIRS, Palacz 외, 국내 BIM–건설로봇 문헌고찰을 이 영역 브리프의 finding 으로 다시 확인해야 반영할 수 있다(이번 브리프에 근거가 없어 넣지 않았다).
- 6. 대표 접근법과 기술 절: 트랙 반영 제안(2026-09-25-05)의 '평면도 축척 복원은 별도 과제' 주장과 승강기·충전 위치 라벨 데이터셋 근거를 재확인해야 한다.
- 6. 대표 접근법과 기술 절: 제조사 사이 지도 판(mapVersion) 동기화나 변경 뒤 좌표 대응 재검증을 다룬 규격·사례 자료가 필요하다 — 현재 관련 문장은 추정이다.
- 6. 대표 접근법과 기술 절: VDA 5050 localizationScore 의 계산 방법이나 제조사 사이 비교 가능성을 다룬 자료가 필요하다.
- 10. 다른 연구영역과의 연결 절: 국가기술표준원 로봇 승강기 탑승 KS 등 층 이동 관련 국내 자료(리서치 출처 상한으로 제외)를 10. 설비·건물 시스템 연동 연결 근거로 조사해야 한다.
- 11. 열린 질문 절: 물류센터·창고 평면도나 충전 위치 라벨을 담은 공개 데이터셋 존재 여부를 이번 영역 조사로 재확인해야 한다(현재는 이전 트랙 실행 목록 기준).

## 이행한 수정 지시

- f1 필드명 정정 — 4절 위치 보고 항목과 7절 VDA 5050 행에서 positionInitialized 를 쓰지 않고 localized(필수, 위치를 신뢰할 수 있는지)로 적었으며, localizationScore(위치추정 품질 0~1)·deviationRange(미터 단위 위치 편차 범위)가 선택 필드임을 밝히고 ref-051 각주를 더했다.
- f22 문구 정정 — 3절·5절 예외·성과·6절 신뢰도 소절에서 'VDA 5050 은 선택 필드로 보고할 수 있게 한다'로 고쳐 쓰고 ref-051 각주를 함께 달았다.
- 출처 id 재매핑 — f6·f7·f8·f18·f31 문장의 각주를 ref-079(traffic-editor)·ref-080(경로 지도 요건)으로, f23·f31 을 ref-224(Shaheer 외)로 바꾸었고, reference_updates 에 ref-079·ref-080·ref-224 을 새 출처로 등록하지 않았다(기존 항목의 cited_by 갱신만).
- f4·f18·f22 근거 출처 변경 — MassRobotics 관련 문장의 각주를 모두 ref-230(AMR_Interop_Standard.json)으로 바꾸고 reference_updates 에 ref-033 을 넣지 않았다.
- f11 판·기준일 명시 — 7절 LIF 행에 'README 기준 판은 1.0.0(2023-09)'을 적고, VDA 5050 3.0.0 이 VDMA 2024-03 판을 인용해 더 새 판이 있을 수 있음을 [추정]으로 덧붙였다.
- f12·f13 처리 — 7절 ISO 21423 행에 발행 여부 미확인과 2026-09-25 검색 결과상 FDIS 단계를 적었고, 6절의 f13 문장은 [추정]을 유지하며 '초안 해설 요약 기준이며 기준점 개수는 미확인'을 병기해 11절 ISO 21423 열린 질문과 연결했다.
- f19·f30 기준일 — 6절·8절에서 Prakhya 외는 'arXiv 2025-01, IEEE 저널 게재본 있음', DeFazio 외는 'arXiv 2024-09, 2025 저널 게재본 있음'으로 적었다.
- f25~f30·f23 표기 — 6·7·8절의 해당 문장마다 '이전 실행 보고 기준, 원문 미열람'을 괄호로 밝히고 태그를 올리지 않았으며, f27 의 교차 확인 표시는 쓰지 않았다.
- 원문 미열람 표기 — 13절과 분리 주제 페이지 출처 절에서 ref-063·064·065·066·067·069·070·071·073·074·076·078·159·161·162·163·164·165·224 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- 용어집 — IndoorGML(f15 근거)·산업 기초 클래스(IFC, f14 근거)는 action update 로만 냈고, 레이아웃 교환 형식(LIF)·지도 정합은 new 로 냈다.
- 11절 — 기존 oq-022 를 id·상태·제기 실행과 함께 연결하고, open_questions_new 3건을 질문 문장 그대로 본문과 open_question_updates(new)에 등록했다.
- 트랙 반영 제안 처리 — 2026-09-25-11 제안 가운데 traffic-editor·층 이름·미터 좌표 요건(f6~f8)과 9절 경계(f32)만 반영하고 osmAG·osmAG-from-cad·ifc2indoorgml·Ogm2Pgbm·Boniardi 외·Vega-Torres 외·BIRS·Palacz 외·국내 BIM–건설로봇 문헌고찰, 2026-09-25-05 의 축척 복원·엘리베이터 라벨 문장은 넣지 않고 additional_research_requests 로 돌렸다.
- 10절 — 22. 시뮬레이션·예측용 디지털 트윈 연결은 traffic-editor 결과의 시뮬레이션 월드 생성(f7)으로만, 8. 실시간 세계 상태·데이터 일관성 연결은 현재 위치 보고와 신뢰도(f1·f5·f22)로만 썼고, 27. AI·학습·적응과 모델 운영은 도면 해석 AI 연구(f25~f30)로 양쪽 연결했다.
- 9절 — f10·f19·f21·f23·f24 의 SLAM·위치추정·지도 작성 기술은 '연계 대상:'으로 표 오른쪽 열과 표 아래 한 단락에만 짧게 두었고, ROP 쪽 경계(f32)는 모두 [추정]으로 표기했다.
- 분량 초과 자동 분리: 6. 지도·공간·위치 모델 본문 11,606자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,396자
- 형식 검증 재작성: 분리 주제 페이지 2026-09-25-area06-s10.md 의 세부영역 링크 11건과 2026-09-25-area06-s6.md 의 27. AI·학습·적응과 모델 운영 링크 1건이 세부영역 페이지 기준 상대 경로로 남아 깨졌으므로, 주제 페이지 위치(docs/topics/2026/) 기준 ../../categories/<대분류 slug>/<파일>.md 경로로 고쳤다. 주장·태그·각주는 바꾸지 않았다.
- 2차: GS1 GLN 행 분리 — docs/topics/2026/2026-09-25-area06-s7.md 3절 표의 GS1 GLN 행을 '물리적 위치와 하위 위치를 식별하는 업무 위치 식별자다. [사실][^ref-164]'와 '지도 위 장소와 대응시킬 업무 쪽 키가 될 것으로 보인다. [추정][^ref-164][^ref-031]' 두 문장으로 나눠 f18 추론을 [추정]으로 되돌렸다(ref-031 각주 정의는 이미 그 페이지에 있다).
- 2차: MassRobotics 부재 한정 통일 — docs/topics/2026/2026-09-25-area06-s3.md 3절의 '평면 기준의 원점·좌표계를 정의하는 메시지는 스키마에 없다' 뒤에 '(스키마 파일 기준, 부재 확정 아님)'을 붙여 7절 표의 표기와 맞췄다.
