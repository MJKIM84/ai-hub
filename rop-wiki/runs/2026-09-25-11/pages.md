# 스토리텔러 산출 2026-09-25-11

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | q1-02 답함(3절 {#q1-02} 소제목 추가), 새 질문 q1-06, 4·5·6·7·8·9절 갱신, 완료 조건 충족(1차 예비)·전환 미승인. H1 아래 단계 상태 줄은 H2 밖이라 패치로 못 바꿈 — '> 단계 상태: 진행 중 · 열린 질문: 4건 · 답한 질문: 2건 · 완료 조건: 충족 · 마지막 실행: 2026-09-25' 로 교체 필요 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절: 입력 형식별 도면→로봇 지도 연구·오픈소스 도구 비교표 추가, '제품 사례' 소절을 벤더 주장 병기로 채움, 한계에 남는 수작업·제품 근거 한계·국내 문헌고찰 추가 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.1 → v0.2: 개념 '층간 정렬 기준점' 추가(f1·f3), '층별 지도'(f1·f2·f3)·'평면도'(f1·f8·f11) 확정, 문 속성 제안과 f17·f20 은 6절 질문으로. H1 '(v0.1)' 은 H2 밖이라 패치 불가 — '(v0.2)' 로 교체 필요 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 초안 v0.2, 아이디어 3절 제품 사례 반영, 백로그 수치(후속 질문 4건, q1-01·q1-02 답함) 갱신. 상태 줄은 변경 없음(현재 단계·마지막 트랙 실행 동일) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 1 | q1-02 답함(래스터·벡터 CAD·BIM/IFC 입력별 도면→로봇 지도 연구·도구·제품 사례), 공간 그래프 스키마 초안 v0.1 → v0.2, 새 질문 q1-06, 참고문헌 id 재부여 | run 2026-09-25-11
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: q1-02 답함(래스터·벡터 CAD·BIM/IFC 입력별 도면→로봇 지도 생성 연구·오픈소스 도구·제품 사례, 제품은 벤더 주장), 공간 그래프 스키마 초안 v0.2
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 건축 도면 자동 인식 트랙 단계 1에서 도면→로봇 지도 생성 사례를 조사하고 6~9절 반영을 제안(실행 2026-09-25-11)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 점유 격자 지도 | Occupancy Grid Map (OGM) | 공간을 일정 크기 칸으로 나누고 칸마다 점유·빈 공간·미지 여부를 적어 로봇 위치추정과 경로계획에 쓰는 지도 표현이다. | 6 | ref-081, ref-082 |
| new | 산업 기초 클래스 | Industry Foundation Classes (IFC) | IfcSpace·IfcDoor 같은 클래스로 건물 요소를 담는 BIM 교환 형식이다. | 6, 28 | ref-085, ref-086 |
| new | IndoorGML | IndoorGML | IFC 데이터에서 자동 생성하는 도구(ifc2indoorgml)의 대상이 되는 실내 공간 정보 표준이다. | 6, 28 | ref-130 |
| new | 위상 지도 | Topological Map | 정확한 좌표 대신 방·구역 같은 장소를 노드로, 통로·문 같은 연결을 엣지로 두어 공간의 연결 관계를 표현하는 지도이다. | 6, 15 | ref-083, ref-084, ref-085 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html |
| ref-081 | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2308.05443 |
| ref-082 | Vega-Torres, M. A. (MigVega GitHub) | Ogm2Pgbm — README (Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments) | 오픈소스 문서 | high | https://github.com/MigVega/Ogm2Pgbm |
| ref-083 | Zhang, J. 외 | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 논문 | medium | https://arxiv.org/abs/2507.00552 |
| ref-084 | Zhang, J. (jiajiezhang7 GitHub) | osmAG-from-cad — README (CAD-to-osmAG pipeline) | 오픈소스 문서 | high | https://github.com/jiajiezhang7/osmAG-from-cad |
| ref-085 | Braga, R. G., Tahir, M. O., Karimi, S., Dah-Achinanon, U., Iordanova, I., & St-Onge, D. | Intuitive BIM-aided robotic navigation and assets localization with semantic user interfaces | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1548684/full |
| ref-086 | Palacz, W., Ślusarczyk, G., Strug, B., & Grabska, E. | Indoor Robot Navigation Using Graph Models Based on BIM/IFC | 논문 | medium | https://www.researchgate.net/publication/333410520_Indoor_Robot_Navigation_Using_Graph_Models_Based_on_BIMIFC |
| ref-120 | Boniardi, F., Valada, A., Mohan, R., Caselitz, T., & Burgard, W. | Robot Localization in Floor Plans Using a Room Layout Edge Extraction Network | 논문 | medium | https://arxiv.org/abs/1903.01804 |
| ref-125 | Pointr | IMDF from Floor Plan & CAD Conversion Services | 벤더 문서 | low | https://www.pointr.tech/technology/imdf |
| ref-126 | Vega Torres, M. A., Braun, A., & Borrmann, A. | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 논문 | medium | https://arxiv.org/abs/2408.15870 |
| ref-127 | Navitec Systems | Universal Fleet Control Software for AGVs & AMRs | 벤더 문서 | low | https://navitecsystems.com/universal-fleet-control/ |
| ref-128 | Boniardi, F., Caselitz, T., Kümmerle, R., & Burgard, W. | Robust LiDAR-based localization in architectural floor plans | 논문 | medium | http://ais.informatik.uni-freiburg.de/publications/papers/boniardi17iros.pdf |
| ref-129 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 논문 | medium | https://arxiv.org/abs/2408.01737 |
| ref-130 | Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S. | IFC2INDOORGML: An Open-Source Tool for Generating IndoorGML from IFC | 논문 | medium | https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/ |
| ref-131 | 박근홍, 박병준, 이슬기(한국산학기술학회논문지) | BIM-건설로봇 통합 연구의 체계적 문헌고찰 (한국산학기술학회논문지 26(11), 218-225, DOI 10.5762/KAIS.2025.26.11.218) | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003269295 |
| ref-132 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 벤더 문서 | low | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? | 6, 21 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| osmAG-from-cad (CAD-to-osmAG 파이프라인) | 오픈소스 | Zhang, J. (jiajiezhang7 GitHub) | 6 | ref-084 | https://github.com/jiajiezhang7/osmAG-from-cad |
| Ogm2Pgbm | 오픈소스 | Vega-Torres, M. A. (MigVega GitHub) | 6 | ref-082 | https://github.com/MigVega/Ogm2Pgbm |
| ifc2indoorgml | 오픈소스 | Diakité, A. A. 외 | 6, 28 | ref-130 | https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/ |

## 추가 조사 요청

- IFC·IndoorGML 표준 구조(IFC의 스키마 성격, IndoorGML의 셀 공간·연결 그래프 구조와 발행 기관 OGC 여부)를 buildingSMART·OGC 공식 저장소 미러로 확인해 용어집 정의와 28. 표준·상호운용성·다사업자 거버넌스 반영 근거로 쓸 수 있게 해 달라(1차 검증 지시로 이번 정의에서 뺐다).
- 참고문헌 id 충돌: 1차 검증이 지시한 매핑 ref-087→ref-119, ref-089→ref-121, ref-090→ref-122, ref-091→ref-123, ref-092→ref-124 는 입력 docs/references/index.md 에 이미 있는 ref-119(IEC 62264-3)·ref-121(Blondin 외)·ref-122(OCEL 2.0)·ref-123(SCOR F1.3)·ref-124(스마트물류센터 인증제 안내)와 겹친다. 그래서 충돌하지 않는 지시값(ref-088→ref-120, ref-093→ref-125, ref-094→ref-126, ref-095→ref-127)은 그대로 쓰고, 충돌하는 다섯 건은 ref-087→ref-128, ref-089→ref-129, ref-090→ref-130, ref-091→ref-131, ref-092→ref-132 로 바꿨다. 퍼블리셔는 ref-120·ref-125~ref-132 가 다른 실행에서 이미 쓰였는지 다시 확인해 달라(pipeline/publish 담당).
- patches 로는 H2 밖의 줄을 바꿀 수 없다. (1) 단계 1 페이지 H1 아래 상태 줄을 '> 단계 상태: 진행 중 · 열린 질문: 4건 · 답한 질문: 2건 · 완료 조건: 충족 · 마지막 실행: 2026-09-25' 로, (2) 공간 그래프 스키마 초안 H1 을 '# 공간 그래프 스키마 초안 (v0.2)' 로 바꾸는 처리를 퍼블리셔 패치 적용 단계에 넣어 달라(pipeline 담당). 넣지 못하면 두 줄이 이전 값으로 남는다.
- q1-06: 물류 로봇 관제 제품(OTTO, ABB, SEER, Kollmorgen NDC8 등)의 공개 매뉴얼·API 문서에서 CAD·BIM 가져오기와 문·승강기·충전 위치 자동 추출 기능 여부를 확인해 아이디어 3. 건축 도면 자동 인식 3절 제품 사례의 벤더 주장 편중을 보강해야 한다.
- q1-02 연구 근거의 독립 교차 확인: 같은 저자 계열이 아닌 출처(예: 다른 그룹의 BIM→점유 격자 지도 연구)로 입력 형식별 자동화 범위(f19)를 확인해야 [추정]을 올릴 수 있다.

## 이행한 수정 지시

- 참고문헌 id 재부여 — 지시 매핑 가운데 ref-120·ref-125·ref-126·ref-127 은 그대로 쓰고, 지시값 ref-119·ref-121·ref-122·ref-123·ref-124 는 입력 참고문헌 색인에 이미 다른 출처가 있어(지시의 전제 '최대 ref-109, ref-110~118' 과 다름) 기존 각주가 덮어써지지 않도록 ref-128·ref-129·ref-130·ref-131·ref-132 로 바꿨다. 단계 1 페이지·아이디어 페이지·초안의 본문 각주, 프런트매터 sources, reference_updates 를 모두 같은 매핑으로 맞췄고 ref-087~ref-095 는 어디에도 쓰지 않았으며, 퍼블리셔 재확인 요청을 additional_research_requests 에 적었다.
- 원문 미열람 표시 — ref-079·ref-080·ref-082·ref-084 를 뺀 ref-081·ref-083·ref-085·ref-086·ref-120·ref-125~ref-132 의 모든 각주 접근일 뒤에 ' (원문 미열람)' 을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- ref-090(재부여 ref-130) 기관 표기를 'Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S.' 로 고쳤다(각주·reference_updates).
- ref-089(재부여 ref-129) 기관 표기를 Shaheer 외 7인으로 고치고, 각주 제목과 본문에 'arXiv 2024-08 제출, 2025-06 개정' 을 적었다.
- ref-094(재부여 ref-126) 기관 표기를 'Vega Torres, M. A., Braun, A., & Borrmann, A.' 로 고치고, 단계 1 페이지 3절·4절과 아이디어 페이지 비교표 설명에 Vega-Torres 외·Ogm2Pgbm·BIM-SLAM 이 같은 TUM 저자 그룹 근거임을 적었다.
- ref-091(재부여 ref-131) 기관 표기를 '박근홍, 박병준, 이슬기(한국산학기술학회논문지)' 로, 서지에 26(11), 218-225, DOI 10.5762/KAIS.2025.26.11.218 을 넣고 URL 을 KCI 논문 페이지(ART003269295)로 바꿨다.
- f16 — 단계 1 페이지 3절에서 [사실] 문장을 'BIM 에서 세션 데이터(포즈 그래프 지도·기술자) 생성, 다중 세션 앵커링 정렬, BIM 에 없는 새 요소 재구성' 범위로 줄이고, URDF 건물 월드·점유 격자 지도 생성은 '검색 요약 기준이며 미확인' 을 붙인 [추정] 문장으로 분리했다. 아이디어 비교표에도 확인 범위만 넣었다.
- f2 — [사실] 문장에는 레이어 축척·이동·회전 변환과 is_charger 정점 동작만 두고, '충전 위치는 사람이 주석하는 항목' 이라는 해석은 f20 문단의 [추정] 문장으로 옮겼다.
- f19 — 'IfcSpace·IfcDoor 같은 의미 클래스 덕분에' 구절 바로 뒤에 [^ref-086] 을 달고 문장 전체는 [추정]을 유지했다.
- f5·f6·f11·f12·f16·f17 — 단계 1 페이지와 아이디어 페이지에서 도면을 기준으로 한 지도 정합·도면 해석 방법으로만 소개하고, 위치추정·SLAM 자체는 분류 원문 9장의 로봇 자체 지능·제어 연계 대상이라고 짧게 적었다(f22 문단은 '연계 대상:' 으로 시작). 세부영역 반영 제안의 요약도 같은 표현으로 썼다.
- f4·f9·f10 — 단계 1 페이지 3절과 아이디어 페이지 '제품 사례' 소절에서 모두 '[추정] 벤더 주장' 으로 쓰고, ref-132 는 본문과 각주 제목에 '유통사(jk.de) 게재본' 임을 밝혔으며, Pointr 는 사람용 실내 지도이고 로봇 지도 사례가 아님을 유지했다.
- f17 — 35cm·15도 수치를 '시뮬레이션·실제 데이터셋 실험 조건의 단일 출처 수치' 로 조건과 함께 적었다(단계 1 페이지 3절, 4절 불확실성).
- f1 — 시뮬레이션 월드 생성은 22. 시뮬레이션·예측용 디지털 트윈 링크로만 연결하고 8. 실시간 세계 상태·데이터 일관성과 구분한다고 적었다.
- 용어 IFC·IndoorGML — 정의를 'IfcSpace·IfcDoor 같은 클래스로 건물 요소를 담는 BIM 교환 형식', 'IFC 데이터에서 자동 생성하는 도구의 대상이 되는 실내 공간 정보 표준' 으로 줄이고 OGC·스키마 구조 서술을 뺐으며, 표준 구조 확인을 additional_research_requests 로 넘겼다.
- 용어 점유 격자 지도·위상 지도 — sources 에 점유 격자 지도는 ref-081·ref-082(f11·f12), 위상 지도는 ref-083·ref-084·ref-085(f7·f13)를 달았다.
- 온톨로지 반영 — 초안을 v0.2 로 올렸다(프런트매터 ontology_version 패치, track_updates.ontology_draft_version "0.2"). (1) '층간 정렬 기준점' 개념 추가(근거 f1·f3, 확정), (2) '층별 지도' 속성에 축척(미터당 픽셀)·도면 대비 변환(이동·회전) 추가, 근거 f1·f2·f3, 초안 → 확정, f4 제외, 층 이름은 추가하지 않고 기존 관계로 대신함을 적음, (3) '평면도' 형식 값 후보를 근거 f1·f8·f11 로 적고 '단계 2에서 확정' 유지, 초안 → 확정, f19 제외. H1 '(v0.2)' 는 H2 밖이라 패치로 못 바꿔 퍼블리셔 처리를 요청했다.
- 문 속성 추가 제안 — 초안 2절에 반영하지 않고 6절 미해결 질문에 f13·f14 근거([^ref-085][^ref-086])와 q3-02 를 달아 두었다.
- f17·f20 — 초안 6절에 q4-02·q4-03 항목의 근거 보강 항목으로 연결했고 새 개념은 넣지 않았다.
- 공간 그래프 교환 형식 질문(단계 2) — backlog_updates 에 넣지 않고, 단계 1 페이지 5절 아래 문장으로 IndoorGML·osmAG(OSM XML)·'Open-RMF traffic-editor 주석 결과' 가 q2-01·q2-03 의 조사 후보임을 적었다(building.yaml 표기는 쓰지 않음).
- as-planned/as-built 편차 질문(단계 4) — backlog_updates 에 넣지 않고 단계 1 페이지 5절 아래에 f17 을 q4-02 관련 근거로 연결만 했다.
- 물류 로봇 관제 제품 질문 — q1-06(단계 1, origin 'f21')으로 등록하고 단계 1 페이지 2절·5절 표에 넣었다.
- q1-02 — 3절에 '### q1-02 … {#q1-02}' 소제목으로 답을 쓰고, 2절 표를 답함·2026-09-25-11·#q1-02 로 바꿨으며 backlog_updates 에 답함과 answer_link 를 냈다. 4절 남은 불확실성에 제품 근거가 벤더 주장 3건뿐이고 공개 근거 부재는 검색 범위 기준임을 적었다.
- 아이디어 3절 — '아직 조사되지 않음(q1-02)' 을 제품 사례(MiR Fleet·Navitec·Pointr, 벤더 주장 병기)로 바꾸고, 오픈소스 도구(traffic-editor·osmAG-from-cad·Ogm2Pgbm·ifc2indoorgml)는 비교표의 '구분' 열에 도구로 구분했으며, 표는 검증된 finding 으로 직접 만들었다.
- 세부영역 반영 — 6. 지도·공간·위치 모델, 21. 온보딩·설정·현장 시운전, 28. 표준·상호운용성·다사업자 거버넌스 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, 28. 표준·상호운용성·다사업자 거버넌스 제안에 'IFC·IndoorGML 을 발행 기관 자료로 확인하지 않음' 을 병기했다.
- 단계 1 페이지 6절 — 완료 조건 1·2 를 충족(1차 예비 판정, 2차에서 확정)·미승인으로, 표 아래를 '다음 단계로 전환: 아니오(막힌 질문 q1-03·q1-04·q1-05·q1-06)' 로 썼고 단계 상태는 진행 중이며 stage_transition 은 넣지 않았다. H1 아래 상태 줄은 H2 밖이라 패치로 못 바꿔 값('진행 중 · 열린 질문 4건 · 답한 질문 2건 · 완료 조건 충족')을 diff_summary 와 additional_research_requests 에 적어 퍼블리셔 처리를 요청했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-02(f1~f22; 입력 형식별 도면→로봇 지도 연구·오픈소스 도구·제품 사례, 제품은 벤더 주장 3건) / 새 질문: q1-06(단계 1, 근거 f21). 중복으로 등록하지 않은 2건은 q2-01·q2-03(f19), q4-02(f17)에 연결 / 온톨로지 변경: v0.1 → v0.2(2026-09-25, 근거 실행 2026-09-25-11): 개념 '층간 정렬 기준점' 추가(f1·f3), '층별 지도' 속성 축척·도면 대비 변환 추가·확정(f1·f2·f3), '평면도' 형식 값 후보 추가·확정(f1·f8·f11). 거부: 문 속성 추가(f13·f14 → 6절 질문, q3-02) / 완료 조건 평가: 충족(1차 예비 판정, 2차에서 확정), 단계 전환 미승인(막힌 질문 q1-03·q1-04·q1-05·q1-06) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 4건, 21. 온보딩·설정·현장 시운전 2건, 28. 표준·상호운용성·다사업자 거버넌스 1건 / 다음 실행 제안: q1-03(충전 위치·작업대 인식·보완 사례), q1-06, q1-04. 참고: 참고문헌 id 는 ref-120·ref-125~ref-132 로 재부여(검증 지시 매핑 중 5건이 기존 id 와 충돌)
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 4, 답함 2, 완료 조건 충족(1차 예비 판정, 2차에서 확정), 단계 전환 미승인(막힌 질문 q1-03·q1-04·q1-05·q1-06)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-02 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-02 | — | — | — |
| q1-06 | 열림 | — | 물류 로봇 관제 제품 가운데 CAD·BIM 도면에서 문·승강기·충전 위치를 자동으로 가져와 지도와 공용 자원 목록을 만드는 기능을 공개 매뉴얼·API 문서로 확인할 수 있는 것이 있는가? | 1 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 입력 형식별 도면→로봇 지도 생성 접근: 래스터 평면도는 사람이 축척·요소를 주석하는 배경(Open-RMF traffic-editor, f1), 벡터 CAD는 구조 레이어 분리·AreaGraph 위상 분할로 계층형 지도 생성(osmAG, f7), BIM/IFC는 점유 격자 지도(f11)·위상·거리 지도와 하이퍼그래프(f13·f14) 생성. 형식별 자동화 수준 종합(f19)은 [추정]. |
| 6 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF traffic-editor(평면도 배경 주석, 측정 축척, 층 기준점 정렬, is_charger, f1·f2), osmAG-from-cad(DXF→osmAG, f8), ifc2indoorgml(IFC→IndoorGML, f15), Ogm2Pgbm(격자 지도→포즈 그래프 지도, f12). 관제 연동의 층 이름·미터 좌표 요건(f3). |
| 6 | 8. 대표 연구와 자료 | 도면 기준 지도 정합·도면 해석 연구로 Boniardi 외 2017·2019(f5·f6), Vega-Torres 외(f11, BIM 과 현실의 편차 지적), Shaheer 외 A-Graph·S-Graph 도면–현장 편차 추정(f17, 35cm·15도는 단일 출처 실험 조건), BIRS(f13), Palacz 외(f14), 국내 BIM–건설로봇 문헌고찰(f18). 위치추정·SLAM 자체는 로봇 자체 지능·제어 연계 대상으로만 적는다. |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 연계 대상: 도면·BIM 기준 위치추정과 SLAM 은 로봇 자체 지능·제어 쪽. 이종 제조사를 연결하는 ROP는 도면에서 만든 층별 지도·공간 그래프의 좌표·층 이름 정렬과 버전 관리를 맡는 경계가 될 것으로 보인다([추정], f22). |
| 21 | 6. 대표 접근법과 기술 | 현장 시운전에서 평면도를 배경으로 벽·문·승강기·차선·충전 정점을 사람이 주석하고 측정으로 축척을 맞추는 방식(Open-RMF traffic-editor, f1·f2). 제품 쪽 평면도 PNG 업로드·축척 요건은 [추정] 벤더 주장(MiR Fleet, 유통사 게재본, f4). 운영 요소가 사람 주석으로 남는 점(f20, [추정]). |
| 21 | 8. 대표 연구와 자료 | 전문가의 지도 작성 노동을 줄이려는 평면도 기반 위치추정 동기(Boniardi 외 2019, f6)와 국내 문헌고찰의 현장 검증·지표 보고 부족(f18, 건설로봇 대상). |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | 공간 정보 교환 형식 후보로 IFC(BIRS 가 BIM–ROS 교환 형식으로 사용, f13), IndoorGML(IFC 에서 자동 생성 도구 존재, f15), OSM 형식 osmAG(f7). IFC·IndoorGML 은 발행 기관 자료로 확인하지 않음. |
