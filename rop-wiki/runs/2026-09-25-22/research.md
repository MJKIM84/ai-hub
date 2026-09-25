# 리서치 브리프 2026-09-25-22

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-22 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 1 · 답한 질문 q1-04

## 갭(비어 있거나 약한 섹션)

- 단계 1 질문 q1-04 열림(target.json 지정: 사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 3건 중 오래된 순)
- 단계 1 페이지 3절에 q1-04 소제목 없음. q1-02·q1-03 답은 수작업이 남는다는 것만 보이고, 그 수작업에 드는 시간·반복 횟수를 확인할 자료는 다루지 않음
- 아이디어 3. 건축 도면 자동 인식 6절(검증 방법) 비어 있음 — 가설 3(현장 모델링 시간 단축)을 판정할 기준 시간 자료 없음
- 21. 온보딩·설정·현장 시운전 페이지 섹션 3. 왜 중요한가, 섹션 6. 대표 접근법과 기술 비어 있음(지도 작성·경로망 설계·자원 등록 부담의 근거 없음)
- 완료 조건: 두 조건 모두 자체 평가 충족이나 검증 승인 전, 막힌 질문 q1-05·q1-06 열림

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q1-04 로봇을 새 현장에 들일 때 지도 작성과 공용 자원 등록에 드는 시간과 반복 작업은 어떤 자료로 확인할 수 있는가?
3. AGV·AMR 도입의 지도 작성·경로망(roadmap) 설계·픽업/하역 위치 지정 부담을 정량 또는 정성으로 다룬 학술·공공 과제 자료는 무엇이 있는가? (단계 페이지 3절, 21. 온보딩·설정·현장 시운전 섹션 3·6 겨냥)
4. 제조사·오픈소스 도구 문서는 지도 작성과 충전소·스테이션 등록을 어떤 절차로 두며, 그 절차 가운데 현장·제조사마다 반복되는 작업은 무엇인가? (공간 그래프 스키마 초안, 아이디어 페이지 3절 겨냥)
5. 다중 제조사 현장에서 같은 레이아웃을 제조사·관제 형식별로 다시 입력하는 부담을 다룬 자료가 있는가? (28. 표준·상호운용성·다사업자 거버넌스, VDMA LIF 겨냥)
6. 국내 물류·서비스 현장에서 지도 작성·시운전 소요 시간을 공개한 연구·공공 자료가 있는가? (한국 자료 우선 규칙, oq-022 관련)
7. 가설 3(도면 기반 자동 생성이 현장 모델링 시간을 줄인다)을 판정하려면 어떤 기준 시간 자료를 비교 대상으로 쓸 수 있는가? (아이디어 페이지 6절, 단계 5 q5-02 선행 근거)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Beinschob 외(2017)는 다중 AGV 도입의 긴 설치 시간 원인으로 공장의 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문 기술자의 수작업 경로망 설계를 들고, 지도 작성에 숙련 인력이 필요하며 하역 지점 위치 정보가 없거나 부정확해 현장에서 고쳐야 하는 경우가 많다고 지적했다. | ref-217 | 아니오 | medium | 2017 | 시작 조건 | 원문 미열람 |
| f2 | [사실] | 유럽연합 CORDIS 기사는 FP7 과제 PAN-Robots의 반자동 3D 지도 작성·경로망 자동 설계 시스템이 AGV 시스템 설치 기간을 6개월에서 2개월로 줄여 공장 가동 중단 시간을 아낄 수 있다고 전한다(과제 측 보고값, 비교 조건 미확인). | ref-318 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f3 | [사실] | Beinschob·Reinke(2015)는 반사판 기반 AGV가 위치추정을 위해 수백에서 수천 개의 반사판 설치를 요구하는 등 도입에 큰 노력과 투자가 들며, PAN-Robots가 자연 지형지물 기반의 반자동 공장 탐사로 설치 시간과 비용을 줄이려 한다고 밝혔다. | ref-319 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f4 | [사실] | 다중 AGV 경로망 자동 설계 연구(IEEE, 2023)는 경로망이 보통 전문가가 설계하며 시간이 많이 들고 문제의 복잡도 때문에 최적이 아닐 수 있다고 보고, 시뮬레이션 기반 자동 설계 경로망이 연결성·중복성에서 수작업 경로망보다 낫다고 보고했다. | ref-320 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f5 | [사실] | arXiv 2511.07175(2025)는 산업 현장의 수작업 경로망 생성이 시간·비용이 많이 들고 최적이 아니라고 지적하며, 자유 공간의 볼록 모서리와 스테이션 상호작용 지점에 노드를 두고 운송 수요를 반영해 경로망을 자동 생성하는 방법을 제안했다. | ref-321 | 아니오 | medium | 2025-11 | — | 원문 미열람 |
| f6 | [사실] | Heselden·Das(ICRA 2024 Field Robotics 워크숍)는 새 환경에 로봇을 배치할 때 지도 작성이 시간이 많이 드는 과정이고 지도 관리가 체계적이지 않으면 위험하다고 보고, 위치·객체·위상·점유 정보를 표준화한 지도 처리 방식과 템플릿·절차적 생성으로 빠진 데이터를 채우는 관리 스크립트를 제안했다. | ref-322 | 아니오 | medium | 2024-04 | — | 원문 미열람 |
| f7 | [사실] | 오픈소스 SLAM Toolbox의 README는 약 30,000 제곱피트까지 실시간의 5배 이상, 약 60,000 제곱피트까지 3배 속도로 지도를 처리하고 200,000 제곱피트 시설에서 쓰였다고 적으며, 저장한 포즈 그래프에서 이어서 지도를 작성하는 기능·지도 병합·수동 그래프 편집을 제공한다. | ref-323 | 아니오 | medium | 2026-09-25 | — | — |
| f8 | [추정] | SLAM 계산 자체가 실시간보다 빠르게 처리된다는 보고(f7)와 설치 병목으로 지도 작성·위치 지정·경로망 설계를 든 연구(f1, f4, f5)를 함께 보면, 현장 모델링 시간의 큰 부분은 계산보다 데이터 수집 주행과 사람의 후처리·주석·설계에서 나오는 것으로 보인다. | ref-323, ref-217, ref-320, ref-321 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [추정] | MiR250 사용자 매뉴얼(매뉴얼 게재 사이트 사본)은 지도를 만들 때 로봇을 수동 모드로 두고 사람이 현장 전체를 몰고 다니며 레이저 스캔으로 지도를 기록한 뒤 지도를 설정하도록 안내한다. | ref-326 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f10 | [추정] | BlueBotics는 AGV 시운전을 지도 작성·설정·시험·직원 교육 단계로 설명하며, 나중에 차량을 추가할 때는 현장 지도가 이미 있어 지도 작성 단계를 빼고, 시운전 기간을 가르는 주요 요인은 내비게이션 방식이라고 밝힌다. | ref-325 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f11 | [추정] | OTTO Motors는 소프트웨어 개정으로 자사 내부 시험에서 시설 지도와 새 작업 흐름을 설정하는 시간이 이전 판보다 50% 줄었고, 충전기·팔레트 같은 여러 끝점의 설정을 한 번에 복제·변경하며 시설 일부만 다시 지도화해 시운전 시간을 줄일 수 있다고 밝힌다. | ref-324 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람, 벤더 주장 |
| f12 | [사실] | Open-RMF traffic-editor 문서는 충전소·주차 위치·대기 지점·도킹 이름·픽업 디스펜서·하역 인제스터를 주행 차선 경유점마다 사람이 편집기에서 입력하게 해, 현장마다 공용 자원 등록이 수작업 주석으로 반복된다. | ref-079 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f13 | [사실] | Open-RMF 플릿 어댑터 템플릿 설정은 플릿마다 RMF 지도 좌표와 로봇 지도 좌표의 대응점(reference_coordinates), 속도·차체·배터리 사양, 수행 가능 작업 유형을 적게 해, 제조사 플릿을 하나 더할 때마다 좌표 정렬과 설정이 반복된다. | ref-105 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f14 | [사실] | VDMA 레이아웃 교환 형식(LIF) 공식 저장소 README는 무인운반 차량 통합사업자가 엣지·노드·스테이션으로 된 주행 레이아웃을 제3자 중앙 관제에 처음 넘겨 쓰고 통합하게 하는 것을 목적으로 적는다(1.0.0 판, 2023-09). | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f15 | [추정] | LIF 해설을 낸 업체 ScaliRo는 다중 제조사 프로젝트에서 레이아웃을 중복 작성하는 비용이 프로젝트당 수 인일(person-day)에 이르고, 형식 사이 수작업 전달이 좌표 오기·스테이션 누락 같은 오류를 낳아 시운전 때 충돌·교통 막힘으로 드러난다고 주장한다. | ref-327 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f16 | [사실] | 노주형 외(로봇학회 논문지 21(1), 2026)는 3D 라이다–IMU SLAM 기반 탐사와 RGB-D 카메라·4자유도 매니퓰레이터로 엘리베이터 버튼을 누르는 층간 이동을 결합해, 다층 실내 지도를 사람 개입 없이 처음부터 끝까지 자율로 구축하는 시스템을 제안했다. | ref-163 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f17 | [추정] | 이번 검색 범위에서 현장 모델링 시간과 반복 작업을 확인할 수 있는 자료는 (1) 설치 병목을 정성적으로 기술한 연구(Beinschob 외, 경로망 자동 설계 연구, Heselden·Das), (2) 과제 측 설치 기간 비교(PAN-Robots 6개월→2개월), (3) 벤더의 내부 시험·주장(OTTO 50%, ScaliRo 수 인일), (4) 반복 작업 항목을 드러내는 도구·형식 문서(traffic-editor 주석, 플릿 어댑터 좌표 대응점, LIF 전달, MiR 수동 주행 지도 작성)로 나뉘고, 단계별 소요 시간을 독립적으로 측정한 시간 연구는 찾지 못한 것으로 보인다. | ref-217, ref-320, ref-322, ref-318, ref-324, ref-327, ref-079, ref-105, ref-046, ref-326 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | 확인한 자료에서 새 현장·새 제조사마다 반복되는 작업은 지도 작성 주행(층마다), 픽업·하역·충전 위치 지정, 경로망 설계, 제조사 지도와 공통 지도의 좌표 대응, 제조사·관제 형식별 레이아웃 재입력으로 정리되며, 이 가운데 위치 지정·경로망 초안·좌표 대응이 도면 기반 자동 생성이 줄일 후보로 보인다. | ref-217, ref-079, ref-105, ref-046, ref-327, ref-321, ref-163 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f19 | [추정] | 연계 대상: SLAM 지도 작성 주행과 로봇 쪽 위치추정 지도의 생성은 분류 원문 9장의 로봇 자체 지능·제어 쪽이므로, 이종 제조사를 연결하는 ROP가 시간 단축을 측정·책임질 대상은 공용 자원 등록, 좌표·층 이름 정렬, 레이아웃 전달·버전 관리 같은 ROP 쪽 설정 작업이 될 것으로 보인다. | ref-323, ref-326, ref-105, ref-046 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 검색 요약: 'precise 2D mapping of the plant, 3D geo-referencing of pick-up/drop positions and the manual design of the roadmap'; 경로망은 전문 기술자가 'tedious process'로 수작업 최적화. 소요 시간 수치 없음. 원문 미열람. (재인용: 2026-09-25-19)
- **f2**: 검색 요약: 'The PAN-ROBOTS system can be installed in two instead of six months, saving on factory outage time.' 대상 공장 규모·비교 기준·측정 방법은 요약에 없음. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f3**: 검색 요약: AGV 는 'designated infrastructure and readily available maps' 가 필요해 'high effort and investment'; 반사판 'hundreds or even thousands'. 원문 미열람.
- **f4**: 검색 요약: 'roadmaps are designed by experts, which is time consuming and may lead to suboptimal solutions'; 개미 군집 최적화와 SIPP 기반 MAPF 시뮬레이터로 평가. 저자 목록 미확인, 원문 미열람.
- **f5**: 검색 요약: 'Manual roadmap generation in industrial practice is time-consuming, costly, and often suboptimal.' 노드는 'convex corner points of the free space and at station interaction points'. 원문 미열람.
- **f6**: 검색 요약: 'mapping is a time-consuming process for deploying robotic systems to new environments, and map handling is risk-prone when not managed effectively'. 농업·도로·실내 사례 데이터셋 포함. 원문 미열람.
- **f7**: README 원문: 'mapping building at 5x+ real-time up to about 30,000 sq. ft. and 3x real-time up to about 60,000 sq. ft.' 프로젝트 문서의 보고값이며 데이터 수집을 위한 주행 시간은 포함하지 않음. (발행일 미확인, 확인일 기준)
- **f8**: f1·f4·f5·f7 에서 도출한 추론. 단계별 소요 시간을 나눠 측정한 자료는 이번 검색 범위에서 찾지 못함.
- **f9**: 벤더 주장: 검색 요약 — Manual Mode 에서 'drive the robot around manually, capturing the layout', 전 구역을 돈 뒤 'Finish Mapping'. 매뉴얼 104쪽. 소요 시간 수치 없음. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f10**: 벤더 주장: 검색 요약 'if adding vehicles later, your integrator will probably exclude the mapping step since your site map will already exist'; 'The main factor determining commissioning times is the type of navigation technology'. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f11**: 벤더 주장: 검색 요약 'Internal testing has shown that it takes a user 50% less time to set-up facility maps and new workflows'; 'replicate configurations ... multiple endpoints—such as chargers and pallets'. 측정 조건 미공개. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f12**: 경유점 속성 is_charger·is_parking_spot·is_holding_point·dock_name·pickup_dispenser·dropoff_ingestor 가 편집기 입력 항목. 소요 시간 기록은 없음. (재인용: 2026-09-25-19)
- **f13**: config.yaml: reference_coordinates 에 층별 rmf·robot 좌표 쌍, linear·footprint·battery·task_capabilities 항목. (재인용: 2026-09-25-20)
- **f14**: README 원문: 'The integrator of the driverless transport vehicles will be able to initially transfer a track layout to a central (third-party) master control system'. 작업량·시간 절감 수치는 README 에 없음.
- **f15**: 벤더 주장: 검색 요약 'the cost of redundant layout creation quickly adds up to several person-days per project'. 근거 자료·측정 방법 미공개. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f16**: 검색 요약: 3D LiDAR–IMU SLAM 기반 효율적 프런티어 생성, 다중 센서 융합 코스트맵, 버튼 누르기로 엘리베이터 연계, 'completely autonomously'. pp. 48-57. 소요 시간 수치는 요약에 없음. 원문 미열람.
- **f17**: f1~f6·f9~f15 를 자료 유형별로 묶은 이 위키의 분류. 한·영 검색 25회 범위의 부재이며 부재 확인은 아님.
- **f18**: f1·f5·f12·f13·f14·f15·f16 에서 도출한 설계 추론. 자동화로 실제로 줄어드는 시간은 측정 자료가 없어 가설 3 판정(단계 5, q5-02)으로 넘김.
- **f19**: f7·f9(로봇 쪽 SLAM 지도 작성)와 f13·f14(관제·ROP 쪽 설정·전달)를 분류 원문 9장 경계에 대응시킨 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 예 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | 표준 | medium | 2026-09-25 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-318 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-319 | Beinschob, P., & Reinke, C. | Graph SLAM based mapping for AGV localization in large-scale warehouses | 2015 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/7312637/ | 예 |
| ref-320 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems | 2023 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-321 | arXiv 2511.07175 저자(미확인) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.07175 | 예 |
| ref-322 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 2024-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2404.13499 | 예 |
| ref-323 | Macenski, S. (SteveMacenski GitHub) | slam_toolbox — README (Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/SteveMacenski/slam_toolbox | 아니오 |
| ref-324 | OTTO Motors (Rockwell Automation) | Maximize AMR productivity and simplify commissioning with our latest software release | 미확인 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/blog/amr-productivity-software-release/ | 예 |
| ref-325 | BlueBotics | 7 Tips to Ensure AGV Commissioning Success | 미확인 | 벤더 문서 | low | 2026-09-25 | https://bluebotics.com/7-tips-to-ensure-agv-commissioning-success/ | 예 |
| ref-326 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR250 User Manual — Creating and configuring a map (page 104, 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.manualslib.com/manual/1941073/Mir-Mir250.html?page=104 | 예 |
| ref-327 | ScaliRo | LIF – Layout Interchange Format Explained | 미확인 | 벤더 문서 | low | 2026-09-25 | https://scaliro.de/en/lif/ | 예 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (로봇학회 논문지 21(1), 48-57) | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |

### 출처 요약

- **ref-079**: 원문 미열람. 이번 실행에서는 다시 열지 않았다(2026-09-25-11·19 실행에서 원문 확인). 평면도 배경 위에 벽·문·차선·충전소·작업셀을 사람이 주석하는 Open-RMF 편집기 설명.
- **ref-105**: 원문 미열람. 이번 실행에서는 다시 열지 않았다(2026-09-25-20 실행에서 원문 확인). 플릿별 관제 접속 정보·지도 좌표 대응점·속도·배터리·작업 능력을 적는 Open-RMF 어댑터 설정 파일.
- **ref-217**: 원문 미열람. 3D 레이저 스캐너 의미 지도로 경로망을 자동 설계해 다중 AGV 도입 시간을 줄이는 방법과 설치 병목(지도 작성·위치 지정·경로망 설계)을 다룬 논문(PAN-Robots).
- **ref-046**: VDMA 레이아웃 교환 형식 공식 저장소 README. 통합사업자가 엣지·노드·스테이션 주행 레이아웃을 제3자 관제에 넘기는 목적과 1.0.0 판(2023-09)을 적는다.
- **ref-318**: 원문 미열람. FP7 과제 PAN-Robots의 반자동 3D 지도 작성·AGV 시스템 성과를 소개하며 설치 기간을 6개월에서 2개월로 줄일 수 있다고 전하는 EU 연구 성과 기사.
- **ref-319**: 원문 미열람. 반사판 기반 AGV의 설치 부담을 지적하고 그래프 SLAM으로 대형 창고 지도를 만들어 AGV 위치추정에 쓰는 방법을 다룬 PAN-Robots 계열 학회 논문.
- **ref-320**: 원문 미열람. 개미 군집 최적화와 MAPF 시뮬레이터로 다중 AGV 경로망을 자동 설계하고 전문가 수작업 경로망과 비교한 논문.
- **ref-321**: 원문 미열람. 수작업 경로망 생성의 시간·비용 문제를 지적하고 스테이션 상호작용 지점과 운송 수요를 반영한 연속 공간 경로망 자동 생성 방법을 제안한 프리프린트.
- **ref-322**: 원문 미열람. 새 환경 배치에서 지도 작성이 시간이 많이 든다는 문제를 들고 표준화한 지도 처리 방식과 생성 보조 스크립트를 제안한 ICRA 2024 워크숍 논문.
- **ref-323**: ROS 2 SLAM Toolbox 공식 README. 처리 속도·적용 시설 규모, 저장한 포즈 그래프에서 이어 작성·병합·수동 편집 기능을 설명한다.
- **ref-324**: 원문 미열람. 시설 지도·작업 흐름 설정 시간 단축(내부 시험 50%), 충전기 등 끝점 설정 일괄 복제, 부분 재지도화 기능을 소개한 제조사 블로그.
- **ref-325**: 원문 미열람. AGV 시운전 단계(지도 작성·설정·시험·교육)와 시운전 기간을 좌우하는 요인을 설명한 내비게이션 기술 업체 글.
- **ref-326**: 원문 미열람. 로봇을 수동 모드로 몰아 지도를 기록하고 설정하는 MiR250 지도 작성 절차를 설명한 사용자 매뉴얼 사본.
- **ref-327**: 원문 미열람. VDMA LIF의 구조와 도입 동기(다중 제조사 레이아웃 중복 작성 비용, 수작업 전달 오류)를 설명한 관제 소프트웨어 업체 해설.
- **ref-163**: 원문 미열람. 자율 탐사 SLAM과 매니퓰레이터의 엘리베이터 버튼 조작을 결합해 다층 실내 지도를 자율 구축하는 국내 연구.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | 2, 3, 4, 5, 6, 8, 9 | q1-04 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19 (신뢰도 medium) — 2절 q1-04 상태 답함, 3절 q1-04 소제목 신설(설치 병목 연구 f1·f3·f4·f5·f6, 과제 측 설치 기간 비교 f2, SLAM 처리 속도와 병목 위치 f7·f8, 제조사·도구 문서의 반복 작업 f9·f10·f11·f12·f13, 다중 제조사 레이아웃 전달 f14·f15, 국내 다층 자율 지도 연구 f16, 자료 유형 종합 f17, 반복 작업 목록 f18, 범위 경계 f19; f9·f10·f11·f15 벤더 주장 병기), 4절 결론·불확실성(독립 시간 측정 자료 부재는 검색 범위 기준), 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 3, 6 | 아이디어 페이지 3절: 현장 모델링 부담 근거 소절 — f1·f2·f4·f5(설치 병목·경로망 수작업), f11·f15(벤더 주장), f17 / 아이디어 페이지 6절: 가설 3 판정의 비교 기준 후보로 PAN-Robots 설치 기간 비교(f2, 과제 보고값), 반복 작업 항목 목록(f18)을 단계 5 조사 전 선행 근거로 명시. 6절 본격 작성은 단계 5(q5-02) |
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 3, 6, 8 | 트랙 floorplan-recognition 단계 1 반영 제안 (f1, f2, f4, f6, f10, f11, f13, f18): 섹션 3 새 현장 도입의 지도 작성·위치 지정·경로망 설계 병목, 섹션 6 반복 작업 항목과 기존 지도 재사용·설정 복제, 섹션 8 Beinschob 외·PAN-Robots·경로망 자동 설계 연구. 벤더 주장(f10, f11)은 [추정] 병기 |
| update | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md | 6, 8 | 트랙 floorplan-recognition 단계 1 반영 제안 (f4, f5): 경로망 수작업 설계의 한계와 자동 경로망 생성(시뮬레이션·MAPF 평가, 스테이션 상호작용 지점 반영) |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 3, 9 | 트랙 floorplan-recognition 단계 1 반영 제안 (f6, f7, f13, f14, f19): 섹션 3 지도 작성이 새 환경 배치의 시간 병목이라는 근거, 섹션 9 SLAM 지도 작성은 연계 대상이고 좌표 정렬·레이아웃 전달은 ROP 쪽이라는 경계 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 경로망 | Roadmap | 다중 AGV·이동로봇이 따라 달릴 수 있는 노드와 엣지의 주행 경로 그래프로, 현장 도입 때 전문가가 설계하거나 자동 생성한다. |
| 지도 정합 | Map Alignment | 도면·공통 지도와 제조사별 로봇 지도를 축척·이동·회전 변환이나 좌표 대응점으로 맞춰 같은 위치를 같은 좌표로 가리키게 하는 작업이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 25회 · 신규 출처 11건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 자료마다 발행 주체 한 곳의 근거만 있음
    - f2 PAN-Robots 6개월→2개월은 CORDIS 기사 검색 요약의 과제 측 보고값이며 대상 공장·비교 기준·측정 방법 미확인
    - f7 SLAM Toolbox 처리 속도는 프로젝트 문서의 보고값이며 독립 측정 아님
    - f9·f10·f11·f15 벤더 주장이며 독립 확인 없음, OTTO 50% 는 내부 시험 조건 미공개
    - ref-320·ref-321 저자 목록 미확인, ref-318·ref-323~ref-327 발행일 미확인
    - f16 국내 연구의 소요 시간 수치는 요약에 없어 미확인
    - 단계별(지도 작성 주행·위치 지정·경로망 설계·자원 등록) 소요 시간을 독립적으로 측정한 시간 연구는 찾지 못함
    - 국내 물류센터의 지도 작성·시운전 소요 시간 공개 자료는 찾지 못함(기사·벤더 소개 글만 나와 넣지 않음, oq-022 미해결)
- 범위 경계 위반 의심:
    - f7·f9·f16: SLAM 지도 작성·자율 탐사는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 지도 작성 시간·부담의 근거로만 쓰고 f19 에 '연계 대상: '으로 경계를 표시함
    - f15: 관제 업체의 비용 주장은 vendor_claim 으로 표시하고 ROP 직접 범위 근거로 쓰지 않음
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문 2건을 열었다(재사용 ref-046 LIF README, 신규 ref-323 SLAM Toolbox README). 신규 논문·EU 기사·벤더 글 9건과 재사용 3건(ref-079, ref-105, ref-217; 이번에 다시 열지 않음)은 원문 미열람이라 신뢰도 상한 medium(벤더 low). 검색 25회/40, 신규 출처 11건/20(ref-318~ref-163, 예약 구간 안). 교차 확인 0건. 질문 선택: target.json 지정 q1-04 1건. q1-04 는 '어떤 자료로 확인할 수 있는가'에 자료 유형 네 가지(f17)와 반복 작업 목록(f18)으로 답했으나, 단계별 소요 시간을 독립 측정한 자료는 찾지 못해 수치 근거는 과제 보고값(f2)과 벤더 주장(f11·f15)뿐이다. 한국 자료: KCI 다층 자율 지도 구축 연구 1건(ref-163). 로봇 친화형 건축물 인증 지표(KCI) 자료도 찾았으나 지도 작성 시간과 직접 관련이 확인되지 않아 넣지 않았다. 교차 규칙: 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(가상 시운전 기간 단축 주장은 출처가 벤더·2차 요약뿐이라 넣지 않음). 일반 열린 질문 신규 없음(새 질문은 트랙 전용). 온톨로지 변경 없음: q1-04 는 시간·작업 부담 자료에 관한 질문이며 공간 그래프 개념·관계의 새 근거를 주지 않는다. 후속 질문 2건.

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 1
- 답한 질문 id: q1-04

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | PAN-Robots 과제가 보고한 설치 기간 6개월→2개월의 비교 조건(대상 공장 규모, 기준 시스템, 단계별 소요 시간)을 과제 결과 보고서·산출물로 확인해, 도면 기반 자동 생성의 시간 단축 효과를 판정할 기준 자료로 쓸 수 있는가? (q1-04 에서 파생) | 5 | f2 |
| — | 국내 물류센터에서 로봇 도입 시 지도 작성·충전소 등 공용 자원 등록·제조사별 좌표 정렬에 든 시간을 단계별로 공개한 공공·학술 자료나 사례가 있는가? (q1-04 에서 파생) | 1 | f17 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 막힌 질문 q1-05·q1-06 열림
    - 완료 조건 두 항목(아이디어 3절 비교, 공간 그래프 스키마 초안의 인식 대상 요소 반영)은 자체 평가 충족이나 검증 승인 전
