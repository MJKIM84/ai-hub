# 리서치 브리프 2026-09-25-54

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-54 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 3 · 답한 질문 q3-01

## 갭(비어 있거나 약한 섹션)

- 단계 3 질문 q3-01 열림(target.json 지정, CLI 지정 질문 id). 단계 3 페이지는 seed 상태로 3절 조사 결과·4절 결론·5절 후속 질문이 비어 있음
- 완료 조건: 아이디어 3. 건축 도면 자동 인식 5절(구현 가설)이 '아직 조사되지 않음' — 처리 흐름·핵심 구성 요소 근거 없음
- 완료 조건: 공간 그래프 스키마 초안(v0.6)의 단계 3 근거 갱신 없음, 실험 페이지에 제안된 실험 계획 없음
- 이전 실행들은 입력 형식·표준·수용 형식(단계 2)을 다뤘지만 인식 → 벡터화 → 공간 그래프 생성 → 온톨로지 적재의 단계별 입출력과 사람 검토 지점을 묶어 본 근거가 없음
- 6. 지도·공간·위치 모델 6절(주제 페이지 분리)에 도면 처리 흐름의 단계 구분과 사람 검토 지점이 없음

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q3-01 인식 → 벡터화 → 공간 그래프 생성 → 온톨로지 적재의 흐름에서 단계마다 입력·출력은 무엇이고 사람 검토는 어디에 두는가?
3. 공개 도구·연구(osmAG-from-cad, Raster-to-Graph, FloorplanVLM, Open-RMF traffic-editor, ifc2indoorgml)는 도면 처리 흐름을 어떤 단계와 중간 산출물 형식으로 나누는가? (단계 3 페이지 3절, 아이디어 페이지 5절 겨냥)
4. 평면도 인식·주석 흐름에서 사람 검토는 어디에 두는가(불확실성 기반 검토, 벡터 공간 전문가 보정, 반복 피드백)? (단계 3 페이지 3절 겨냥)
5. BIM·공간 그래프를 RDF 온톨로지로 적재하는 도구와 적재 전 검증 수단(IFCtoLBD, SHACL, IDS)은 무엇인가? (공간 그래프 스키마 초안 6절, 28. 표준·상호운용성·다사업자 거버넌스 연결)
6. 로봇 쪽 온톨로지·지식 그래프에 건물·장면 정보를 적재한 연구(OBRNIT, 장면 그래프–로봇 온톨로지 결합)는 어떤 단계와 사람 주석을 두는가? (5. 로봇 능력·작업 온톨로지 연결)
7. 국내에 평면도를 벡터화해 BIM·3D 모델로 바꾸는 처리 흐름을 다룬 연구가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | osmAG-from-cad 공식 저장소 README 는 처리 흐름을 DXF → SVG·bounds.json → PNG → AreaGraph 분할 → osmAG.osm(OSM XML) → 선택적 문자 기반 방 이름 붙이기로 나누고, 사용자가 해상도(미터/픽셀)·문 폭·복도 폭·좌표 기준점(위도·경도·픽셀 좌표) 같은 파라미터를 설정하게 하며, 실행 입력·명령을 적은 실행 기록(manifest)을 함께 남긴다. | ref-084 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | Raster-to-Graph 공식 README 는 입력을 가운데 정렬한 512×512 래스터 평면도로, 출력을 벽 교차점(노드)과 벽 선분(엣지)에 평면도 의미를 붙인 구조 그래프로 두며, 다른 이미지 전처리를 쓰면 모델을 다시 학습해야 할 수 있다고 적는다. | ref-070 | 아니오 | medium | 2024 | — | — |
| f3 | [사실] | FloorplanVLM(arXiv 2602.06507)은 래스터 평면도에서 벽·문·창문·방을 구조화된 JSON 시퀀스로 바로 출력하는 시각-언어 모델 방식의 벡터화를 제안하고, 외벽 IoU 92.52% 를 보고했다(저자 보고 단일 출처). | ref-696 | 아니오 | medium | 2026-02 | — | 원문 미열람 |
| f4 | [사실] | ArchCAD-400K 프로젝트 페이지는 주석 과정을 레이어·블록 구조가 일관된 도면 선별, 레이어·블록 계층을 이용한 자동 라벨링, 전문가가 래스터로 바꾸지 않고 벡터 공간에서 직접 보정하는 단계로 나누고, 자동 라벨링으로 비용을 50배 넘게 줄였다고 적는다(저자 측 수치). | ref-434 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | Jakubik 외(AAAI 2022)는 평면도 기호 검출 시스템이 검출한 기호마다 불확실성 척도를 계산해 분류하기 어려운 기호에만 전문가 판단을 받는 사람 참여 루프(human-in-the-loop) 설계를 제안했다. | ref-691 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f6 | [사실] | Sketch2BIM(arXiv 2510.20838)은 손으로 그린 축척 없는 평면도를 다중 모달 LLM 다중 에이전트가 사람 피드백과 스키마 검증을 거쳐 벽·문·창문의 구조화 JSON 레이아웃으로 반복 보정한 뒤 BIM 생성 스크립트로 바꾸는 흐름을 제안했고, 평면도 10장 실험에서 벽 검출은 첫 회 약 83% 에서 몇 번의 피드백 뒤 거의 완전히 맞았다고 보고했다. | ref-690 | 아니오 | medium | 2025-10 | — | 원문 미열람 |
| f7 | [사실] | DoorDet(2025)은 객체 검출기로 문을 찾고 대규모 언어 모델(LLM)이 문 유형을 분류한 뒤 사람이 검수하는 반자동 데이터 구축 절차를 제안했다. | ref-077 | 아니오 | medium | 2025-08 | — | 원문 미열람 |
| f8 | [사실] | Open-RMF rmf_traffic_editor README 는 사람이 평면도 위에 주석한 결과를 .building.yaml 로 저장하고, building_map_generator 가 이 파일에서 nav 인자로 주행 그래프를, gazebo·ignition 인자로 시뮬레이터 월드(.world)를 만든다고 적어, 하나의 주석 파일에서 경로용 그래프와 시뮬레이션 초기값이 함께 나온다. | ref-441, ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | ifc2indoorgml(ISPRS Archives 2022)은 IFC 데이터에서 IndoorGML 모델을 자동 생성하는 오픈소스 도구로, BIM 입력은 이미지 인식·벡터화 단계를 거치지 않고 공간 그래프 표현으로 바로 변환하는 경로가 있다. | ref-225 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f10 | [사실] | IFCtoLBD 공식 저장소 README 는 IFC STEP·IFC/XML·IFC/JSON 을 입력으로 받아 건물 위상 온톨로지(BOT) 등 링크드 빌딩 데이터 RDF 로 바꾸고 Turtle·JSON-LD·ICDD 패키지로 저장하며, 변환 결과를 SHACL 로 검증할 수 있다고 적는다(판 2.54.0, Apache 2.0). | ref-689 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | W3C SHACL 은 RDF 데이터 그래프를 형상(shapes) 그래프의 조건에 대해 검증하는 언어이며, 검증 결과로 sh:conforms(참·거짓)와 위반별 결과를 담은 검증 보고서를 낸다(2017 W3C 권고안). | ref-692 | 아니오 | medium | 2017 | — | — |
| f12 | [사실] | buildingSMART 의 IDS(Information Delivery Specification)는 IFC 기반 정보 요구사항을 컴퓨터가 해석할 수 있게 정의하는 XML 기반 표준으로, XSD 스키마와 XML 예시로 제공된다. | ref-697 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | arXiv 2507.11770(IROS 2025)은 서로 다른 장면 기술 형식(MJCF·URDF·SDF)을 USD 장면 그래프로 통일하고, 웹 기반 도구에서 사람이 온톨로지 개념 클래스로 의미 라벨을 붙인 뒤 지식 그래프로 옮겨 역량 질문(competency question)에 답하게 하는 흐름을 제안했다. | ref-695 | 아니오 | medium | 2025-07 | — | 원문 미열람 |
| f14 | [사실] | OBRNIT(Buildings 14(8), 2024)은 BIM 기반 로봇 주행·점검 작업을 위해 로봇, 건물, 주행 작업, 점검 작업의 네 개념 묶음을 두고 가구·HVAC 같은 건물 개념을 ifcOWL 에서 가져온 온톨로지다. | ref-694 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f15 | [사실] | 대한건축학회 논문집 40(1)(2024)의 국내 연구는 기존 주택 평면도를 BIM 기반 3D 모델로 바꾸기 위해 인스턴스 정규화·화이트닝 기반 딥러닝 분할 뒤 경로 계획 기반 벡터 생성 알고리즘으로 벽선을 만드는 2단계 방법을 제안했다. | ref-693 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f16 | [추정] | q3-01 에 대해 확인한 도구·연구를 이 위키가 묶으면 흐름은 (1) 입력 정리(래스터는 크기·여백 정규화와 축척, CAD 는 DXF 와 레이어, BIM 은 IFC) → (2) 인식·벡터화(요소 목록 JSON 이나 벽 구조 그래프) → (3) 공간 그래프 생성(방·구역 분할과 연결: osmAG, IndoorGML, building.yaml) → (4) 온톨로지 적재(BOT 등 RDF 와 SHACL 검증)로 나뉘고, BIM 입력은 (2)를 건너뛸 수 있으며, 충전소·스테이션 같은 운영 요소는 확인한 흐름 어디에서도 자동으로 채워지지 않는 것으로 보인다. | ref-084, ref-070, ref-696, ref-441, ref-225, ref-689, ref-692, ref-079 | 아니오 | low | 2026-09-25 | — | — |
| f17 | [추정] | 확인한 사례를 종합하면 사람 검토는 (a) 처리 전 입력 파라미터 확정(축척·좌표 기준점·레이어 대응), (b) 인식 뒤 불확실한 요소만 골라 벡터 공간에서 보정, (c) 공간 그래프에 운영 요소(충전소·스테이션·대기 지점)와 장소 이름을 주석, (d) 온톨로지 적재 전 검증 보고서 위반 확인의 네 지점에 둘 수 있을 것으로 보인다. | ref-084, ref-691, ref-434, ref-690, ref-077, ref-079, ref-692, ref-695 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | 분류 원문 질문(‘3층 출하 대기장’을 같은 장소로 인식)과 관련해, 확인한 흐름에서 방 이름은 CAD 문자 추출이 기본으로 꺼져 있거나 래스터 문자 인식에 기대므로 업무 장소 이름과 공간 노드를 잇는 일은 공간 그래프 생성 뒤 사람 확인 단계에 두어야 할 것으로 보인다. | ref-084, ref-079, ref-695 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |

### 근거 발췌

- **f1**: README 원문: "DXF -> SVG + bounds.json -> PNG -> AreaGraph segmentation -> osmAG.osm -> optional text naming". 문자 기반 이름 붙이기는 기본 꺼짐(--with-text), 최소 면적(min_area)·분할 파라미터 조정 가능.
- **f2**: README: 출력은 "structural graphs embedded with floorplan semantics", 벽 교차점·선분을 그래프 순회 순서로 반복 예측. 전처리가 다르면 "you might need to retrain the model".
- **f3**: 검색 요약: Qwen2.5-VL-3B 를 SFT·GRPO 로 미세조정해 raster → JSON(walls, doors, windows, rooms), Floorplan-2M·HQ-300K 데이터, external-wall IoU 92.52%. (원문 미열람)
- **f4**: 프로젝트 페이지: 11,917건 중 5,538건 선별, 자동 라벨링 "cost reduction by over 50x using CAD layers and blocks", 전문가 보정은 벡터 공간에서 직접 수행. (재인용: 2026-09-25-36)
- **f5**: 검색 요약: 건설 분야 평면도 물량 산출 사례에서 각 검출 기호의 불확실성을 계산해 어려운 기호에 대해 전문가 지식을 획득. AAAI 36(11), 12524–12530. (원문 미열람)
- **f6**: 검색 요약: perceptual extraction → human feedback → schema validation → automated BIM scripting. 정밀도·재현율·F1 모두 0.83 이상, RMSE·MAE 는 피드백으로 0까지 감소(저자 보고). (원문 미열람)
- **f7**: 검출기 → LLM 유형 분류 → 사람 검수의 반자동 절차. (재인용: 2026-09-25-05) (원문 미열람)
- **f8**: README: traffic-editor 가 ".building.yaml" 파일 생성, building_map_generator gazebo/ignition 은 .world, nav 는 주행 그래프 출력. 충전소 등 경유점 속성은 사람이 입력(ref-079, 같은 발행 주체라 독립 확인 아님).
- **f9**: IFC → IndoorGML 자동 생성 오픈소스 도구, IndoorGML 실용 도구 부족이 개발 동기. (재인용: 2026-09-25-11) (원문 미열람)
- **f10**: README: 출력은 "Turtle, JSON-LD, or an ICDD package", 변환 뒤 "validate it with SHACL". Building Topology Ontology 를 공유 어휘로 언급.
- **f11**: 편집자 초안 원본: "a language for validating RDF graphs against a set of conditions". 검증 보고서에 sh:conforms 와 sh:result. 열람한 것은 w3c/data-shapes 저장소의 편집자 초안이며 권고안 본문과 문구가 다를 수 있음.
- **f12**: README: "computer interpretable XML based standard from buildingSMART to define IFC based Information Delivery Specifications". 판 번호·검사 범위는 README 에 없어 미확인. (발행일 미확인, 확인일 기준)
- **f13**: 검색 요약: unified scene graph in USD, web-based visualization tool for annotating semantic labels with ontology concept classes, translated into a knowledge graph. (원문 미열람)
- **f14**: 검색 요약: four main groups of concepts (robot, building, navigation task, inspection task), ifcOWL 개념 재사용, 천장 누수 점검 사례로 평가. (원문 미열람)
- **f15**: 검색 요약: 정보 분할(IN·IW 로 일반화 성능 개선) → 경로계획 기반 벡터 생성으로 벽선 신속 생성, 레거시 2D 도면의 BIM 3D 변환 목적. (원문 미열람)
- **f16**: f1(osmAG 단계), f2·f3(벡터화 출력), f8(building.yaml→주행 그래프·월드), f9(IFC→IndoorGML), f10·f11(RDF 적재·SHACL)을 이 위키가 대응시킨 종합. 이 네 단계 구분을 제시한 단일 출처는 확인하지 못함.
- **f17**: 근거: 입력 파라미터 설정(f1), 불확실성 기반 전문가 검토(f5), 벡터 공간 전문가 보정(f4), 반복 피드백·스키마 검증(f6), LLM 뒤 사람 검수(f7), 경유점 속성 수동 주석(f8), SHACL 보고서(f11), 온톨로지 라벨 사람 주석(f13). 검토 지점의 효과를 비교 측정한 자료는 찾지 못함.
- **f18**: osmAG 의 문자 기반 이름 붙이기는 선택 기능·기본 꺼짐(f1), Open-RMF 장소·경유점 이름은 사람 입력(f8), 장면 그래프 의미 라벨도 사람 주석(f13).

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-689 | Oraskari, J. (jyrkioraskari GitHub) | IFCtoLBD — README (IFCtoLBD converts IFC (Industry Foundation Classes STEP formatted files into the Linked Building Data ontologies) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/jyrkioraskari/IFCtoLBD | 아니오 |
| ref-690 | Ratul, A. K., Acharjee, S., Park, S., & Sakib, M. N. | Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.20838 | 예 |
| ref-691 | Jakubik, J., Hemmer, P., Vössing, M., Blumenstiel, B., Bartos, A., & Mohr, K. | Designing a Human-in-the-Loop System for Object Detection in Floor Plans | 2022 | 논문 | medium | 2026-09-25 | https://ojs.aaai.org/index.php/AAAI/article/view/21522 | 예 |
| ref-692 | W3C RDF Data Shapes Working Group | Shapes Constraint Language (SHACL) | 2017 | 표준 | high | 2026-09-25 | https://www.w3.org/TR/shacl/ | 아니오 |
| ref-693 | 대한건축학회 논문집 게재 논문 저자(미확인) | 딥러닝과 경로계획 기반의 주택 평면도 3D 모델링 방법 | 2024 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003047128 | 예 |
| ref-694 | Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인) | Ontology for BIM-Based Robotic Navigation and Inspection Tasks | 2024 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2075-5309/14/8/2274 | 예 |
| ref-695 | arXiv 2507.11770 저자(미확인) | Generating Actionable Robot Knowledge Bases by Combining 3D Scene Graphs with Robot Ontologies | 2025-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2507.11770 | 예 |
| ref-696 | arXiv 2602.06507 저자(미확인) | FloorplanVLM: A Vision-Language Model for Floorplan Vectorization | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.06507 | 예 |
| ref-697 | buildingSMART (buildingSMART/IDS GitHub) | IDS — README (Information Delivery Specification) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IDS | 아니오 |
| ref-084 | Zhang, J. (jiajiezhang7 GitHub) | osmAG-from-cad — README (CAD-to-osmAG pipeline) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/jiajiezhang7/osmAG-from-cad | 아니오 |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 2024 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/SizheHu/Raster-to-Graph | 아니오 |
| ref-434 | ArchiAI Lab (ArchCAD-400K 프로젝트) | ArchCAD-400k: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting — project page | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://archiai-lab.github.io/ArchCAD.github.io/ | 아니오 |
| ref-441 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_traffic_editor | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 예 |
| ref-225 | Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S. | IFC2INDOORGML: An Open-Source Tool for Generating IndoorGML from IFC | 2022 | 논문 | medium | 2026-09-25 | https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/ | 예 |
| ref-077 | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 2025-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2508.07714 | 예 |

### 출처 요약

- **ref-689**: IFC(STEP·XML·JSON)를 BOT 등 링크드 빌딩 데이터 RDF(Turtle·JSON-LD·ICDD)로 변환하고 SHACL 검증을 지원하는 오픈소스 변환기의 README. 판 2.54.0, Apache 2.0.
- **ref-690**: 원문 미열람. 다중 모달 LLM 다중 에이전트와 사람 피드백·스키마 검증으로 손그림 평면도를 JSON 레이아웃과 BIM 으로 바꾸는 흐름과 10장 실험 결과.
- **ref-691**: 원문 미열람. 평면도 기호 검출에서 기호별 불확실성으로 전문가 판단을 받을 대상을 고르는 사람 참여 루프 시스템(AAAI 36(11)).
- **ref-692**: RDF 데이터 그래프를 형상 그래프로 검증하고 sh:conforms 와 결과를 담은 검증 보고서를 내는 W3C 권고안. 열람은 w3c/data-shapes 저장소의 편집자 초안 원본(권고안 본문과 문구가 다를 수 있음).
- **ref-693**: 원문 미열람. 레거시 주택 평면도를 딥러닝 분할과 경로계획 기반 벡터 생성으로 벽선을 만들어 BIM 3D 모델로 바꾸는 국내 연구(대한건축학회 논문집 40(1)).
- **ref-694**: 원문 미열람. 로봇·건물·주행 작업·점검 작업 개념으로 된 BIM 기반 로봇 주행·점검 온톨로지 OBRNIT(ifcOWL 개념 재사용).
- **ref-695**: 원문 미열람. 장면 기술 형식을 USD 장면 그래프로 통일하고 사람이 온톨로지 개념으로 라벨을 붙여 지식 그래프로 옮기는 흐름(IROS 2025).
- **ref-696**: 원문 미열람. 래스터 평면도를 벽·문·창문·방의 구조화 JSON 으로 출력하는 시각-언어 모델 벡터화, 외벽 IoU 92.52% 보고.
- **ref-697**: IFC 기반 정보 요구사항을 정의하는 XML 기반 buildingSMART 표준 IDS 의 공식 저장소 README(XSD·XML 예시). 판·검사 범위는 README 에 없음.
- **ref-084**: DXF 를 SVG·PNG 로 바꿔 AreaGraph 로 분할하고 osmAG(OSM XML)로 내보내는 파이프라인 README. 단계별 파라미터와 실행 기록.
- **ref-070**: 512×512 래스터 평면도에서 벽 교차점·선분 구조 그래프를 자기회귀로 예측하는 모델과 데이터 README.
- **ref-434**: CAD 도면 선별, 레이어·블록 기반 자동 라벨링, 벡터 공간 전문가 보정의 주석 과정을 설명하는 프로젝트 페이지.
- **ref-441**: traffic-editor 가 .building.yaml 을 저장하고 building_map_generator 가 주행 그래프와 Gazebo·Ignition 월드를 만드는 도구 README.
- **ref-079**: 원문 미열람. 평면도 배경 위 벽·문·차선 주석과 충전소 등 경유점 속성을 사람이 입력하는 traffic-editor 문서(이번 실행에서 다시 열지 않음).
- **ref-225**: 원문 미열람. IFC 에서 IndoorGML 을 자동 생성하는 오픈소스 도구 논문.
- **ref-077**: 원문 미열람. 객체 검출·LLM 분류·사람 검수로 문 검출 데이터셋을 반자동 구축하는 절차.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | 2, 3, 4, 5, 6, 8, 9 | q3-01 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 low) — 2절 q3-01 상태 답함, 3절 q3-01 소제목 신설({#q3-01}): 입력 정리·인식·벡터화 도구의 입출력(f1 osmAG, f2 Raster-to-Graph, f3 FloorplanVLM, f15 국내 연구), 공간 그래프 생성(f8 building.yaml, f9 IFC→IndoorGML), 온톨로지 적재와 검증(f10 IFCtoLBD, f11 SHACL, f12 IDS, f13 장면 그래프–온톨로지, f14 OBRNIT), 사람 검토 사례(f4·f5·f6·f7), 단계 종합(f16)·검토 지점 종합(f17)·분류 원문 질문(f18)은 추정으로 / 4절 결론·불확실성(검토 지점 효과 측정 자료 없음, 운영 요소 자동화 근거 없음) / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 5 | 아이디어 페이지 5절(트랙 산출물): '처리 흐름과 사람 검토 지점' 소절 신설 — 단계별 입력·출력 표(f1·f2·f3·f8·f9·f10, 종합 f16 추정), 사람 검토 네 지점(f17 추정, 근거 f4·f5·f6·f7·f11), 장소 이름 확인(f18). 공간 그래프 단위(q3-02)·능력 대조(q3-03)·시뮬레이션 초기값(q3-04)은 아직 없음을 명시 |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f1, f8, f9, f16, f17, f18): 6절(주제 페이지 area06-s6)에 도면 처리 흐름의 단계 구분과 장소 이름·운영 요소를 사람이 확인하는 지점 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6, 8 | 트랙 floorplan-recognition 단계 3 반영 제안 (f3, f5, f6, f7): 교차 규칙(도면 해석은 6. 지도·공간·위치 모델에 적용)에 따라 시각-언어 모델 벡터화, 불확실성 기반 사람 참여 루프, LLM 다중 에이전트와 사람 피드백을 6. 지도·공간·위치 모델 페이지와 양쪽 연결 |
| update | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md | 7 | 트랙 floorplan-recognition 단계 3 반영 제안 (f10, f11, f12): IFC→링크드 빌딩 데이터 변환(IFCtoLBD), 적재 전 검증 표준 SHACL, IFC 정보 요구 명세 IDS |
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f1, f8, f17): 시운전 전 도면 처리에서 사람이 입력·확인하는 항목(축척·좌표 기준점, 운영 요소 주석, 검증 보고서 확인) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사람 참여 루프 | Human-in-the-Loop (HITL) | 자동 처리 결과 가운데 불확실하거나 중요한 부분을 사람이 확인·보정하고 그 판단을 다시 처리 흐름에 넣는 설계 방식이다. |
| 정보 전달 명세 | Information Delivery Specification (IDS) | buildingSMART 가 정한, IFC 모델이 갖춰야 할 정보 요구사항을 컴퓨터가 해석할 수 있게 적는 XML 기반 표준이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 9건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 도구·연구마다 발행 주체 한 곳의 자료만 있음(f8 의 두 출처는 같은 Open Robotics)
    - f3·f5·f6·f13·f14·f15 원문 미열람(검색 요약 범위), 성능 수치는 저자 보고 단일 출처
    - f11 은 SHACL 권고안이 아닌 w3c/data-shapes 편집자 초안 원본으로 확인
    - f12 IDS 의 판 번호·검사 범위(엔터티·속성·분류)는 README 에 없어 미확인
    - ref-693·ref-694·ref-695·ref-696 저자 목록 미확인, ref-689·ref-697 발행일 미확인
    - f16·f17 단계·검토 지점 구분은 이 위키의 종합이며 검토 지점별 효과를 측정한 자료는 찾지 못함
    - OBRNIT 공개 저장소와 ifc2indoorgml 저장소는 열지 못함
- 범위 경계 위반 의심:
    - 없음
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 신규 ref-689(IFCtoLBD README)·ref-692(SHACL 편집자 초안)·ref-697(IDS README), 재사용 ref-084·ref-070·ref-434·ref-441. arXiv·AAAI·MDPI·KCI 원문은 정책으로 열리지 않아(arXiv 열람 시도 거부) 검색 요약 기준이며 신뢰도 상한 medium. 검색 12회/40, 신규 출처 9건/20(ref-689~ref-697, 예약 구간 안), 재사용 7건. 질문 선택: target.json 지정 q3-01 1건. q3-01 은 단계별 입력·출력과 사람 검토 네 지점으로 답했으나 핵심 종합(f16·f17)이 이 위키의 추정이라 종합 신뢰도 low. 한국 자료: 대한건축학회 논문집 2024 연구 1건(ref-693), 물류 현장 도면 처리 흐름 사례는 찾지 못함(oq-022 미해결). 교차 규칙: 도면 인식 AI(f3·f5·f6·f7)는 27. AI·학습·적응과 모델 운영과 6. 지도·공간·위치 모델 양쪽 반영을 제안했다. 22. 시뮬레이션·예측용 디지털 트윈 연결은 f8 의 시뮬레이터 월드 생성을 형식 설명으로만 썼고 8. 실시간 세계 상태·데이터 일관성과 섞지 않았다. 온톨로지 변경 없음: q3-01 은 처리 흐름에 관한 질문이며 공간 그래프 개념·관계를 새로 뒷받침하는 finding 이 없다(공간 노드에 이름 출처·검토 상태 속성을 둘지는 근거 없는 설계 선택이라 후속 질문으로 올림). 일반 열린 질문 신규 없음(새 질문은 모두 트랙 전용). 후속 질문 3건. 정정 요청 없음. 페이지 제안: 트랙 산출물 2건, 세부영역 반영 제안 4건(갱신 상한과 별도).

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 3
- 답한 질문 id: q3-01

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 공간 그래프를 온톨로지에 적재하기 전 검증 관문으로 쓸 SHACL 형상(예: 모든 문은 두 공간 노드를 잇는다, 모든 공간 노드는 한 층에 속한다, 충전 위치는 접근 지점을 가진다)은 무엇이며, 위반 보고서를 누가 어떻게 처리하는가? (q3-01 에서 파생) | 3 | f11 |
| — | 여러 인식 방법(구조 그래프 예측, 시각-언어 모델 JSON 출력, CAD 레이어 기반 분할, IFC 직접 변환)을 바꿔 끼울 수 있게 하려면 인식·벡터화 단계의 중간 산출물 형식을 무엇으로 정해야 하는가? (q3-01 에서 파생) | 3 | f16 |
| — | 처리 단계마다 사람이 고친 요소 수와 검토 시간을 기록해 가설 1(인식만으로 대부분 추출)과 가설 3(현장 모델링 시간 단축)을 판정하는 지표로 쓸 수 있는가? (q3-01 에서 파생) | 5 | f17 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 처리 흐름·핵심 구성 요소·다른 아이디어와의 연결이 아이디어 3. 건축 도면 자동 인식 5절에 아직 실리지 않음(이번 제안 반영 전, 다른 아이디어와의 연결 근거 없음)
    - 공간 그래프 스키마 초안의 단계 3 근거 갱신 없음(이번 실행 온톨로지 변경 제안 없음)
    - 실험 페이지에 사용자에게 제안하는 실험 계획 없음
    - 열린 질문 q3-02·q3-03·q3-04·q3-05·q3-06
