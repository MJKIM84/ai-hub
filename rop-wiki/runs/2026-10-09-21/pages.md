# 스토리텔러 산출 2026-10-09-21

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | 되돌아온 질문 q1-05·q1-06 답함(3절 {#q1-05}·{#q1-06}), q1-08 부분 답, 2절 질문 목록 표 재작성, 4절 결론·불확실성 추가, 5절 후속 질문 q2-10·q3-12와 q1-05·q1-06 행 상태 답함, 6절 전환 줄, 7절 반영 제안, 8절 새 각주, 9절 이력 행, 상태 줄(재개)·프런트매터(sources·related_areas·last_run) 갱신, ArchCAD-400K 엘리베이터 근거 충돌 연결 문장 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 '물류 시설 도면 인식과 도면 자동 가져오기의 근거 보강' 소절 추가(비주거 데이터셋 구성·FloorPlanCAD 범주 수 출처 충돌·AI Hub 주거 한정·전이 근거, 제품·로봇 밖 도구 근거, 도입 기간 사례), 프런트매터 sources 에 새 출처 13건 추가, last_run 2026-10-09 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 상태 줄을 현재 단계 2·마지막 트랙 실행 2026-10-09로 고치고 프런트매터 last_run 2026-10-09, 6절에 실행 2026-10-09-21(되돌아온 단계 1 질문 q1-05·q1-06 답함, q1-08 부분 답, 초안 v1.2 유지, 단계 전환 미승인) 단락 추가 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 건축 도면 자동 인식 단계 2 | 되돌아온 단계 1 질문 q1-05·q1-06 답함(종합 신뢰도 low), q1-08 부분 답, 후속 질문 q2-10·q3-12, 공간 그래프 스키마 초안 v1.2 유지, 아이디어 3 페이지 3절 근거 보강, 출처 충돌 열린 질문 2건(FloorPlanCAD 범주 수, ArchCAD-400K 엘리베이터 범주). 신규 참고문헌 ref-1367~ref-1376 이 실행 2026-10-09-19 브리프의 같은 id(다른 URL)와 충돌하므로 게시 전 id 충돌 검사와 재번호 확인 필요 | run 2026-10-09-21
- 홈 최근 업데이트: 2026-10-09 — 건축 도면 자동 인식 단계 2: 되돌아온 단계 1 질문 q1-05(물류 시설 도면 인식 데이터셋과 전이)·q1-06(관제 제품의 도면 자동 가져오기) 답함, q1-08 부분 답, 후속 질문 2건
- 대분류 최근 업데이트: 2026-10-09 — 건축 도면 자동 인식 트랙: 14. 도면·BIM에서 지도 만들기와 관련된 비주거 도면 데이터셋 구성과 도면 자동 가져오기 근거를 단계 1 페이지에 싣고 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해, 55. 현장 조사·설치·시운전 세부영역 반영을 제안
- 세부영역 최근 업데이트: 2026-10-09 — 14. 도면·BIM에서 지도 만들기: 건축 도면 자동 인식 트랙이 8. 대표 연구와 자료·11. 열린 질문 반영을 제안(비주거 도면 데이터셋, 산업용 건물 도면 전이 한계, 도면 자동 가져오기 근거)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 도메인 이동 | Domain Shift | 학습에 쓴 데이터와 실제로 적용하는 데이터의 분포가 달라(예: 주거 평면도로 학습한 모델을 산업용 건물 도면에 적용) 모델 성능이 떨어지는 현상이다. | 14, 45, 47 | ref-1369 |
| new | 일반화 보로노이 그래프 | Generalized Voronoi Graph (GVG) | 격자 지도를 세선화해 얻는 골격 그래프로, 로봇 주행용 초기 노드를 만들고 방 분할에 쓰인다. | 14, 15 | ref-1370 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2503.22346 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2105.07147 |
| ref-1012 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 정부·연구기관 | high | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 논문 | medium | https://arxiv.org/abs/2409.12842 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 벤더 문서 | low | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 |
| ref-1367 | Pizarro, P. N., Hitschfeld, N., Sipiran, I., & Saavedra, J. M. (Automation in Construction) | Automatic floor plan analysis and recognition | 논문 | medium | https://meshinglab.dcc.uchile.cl/publication/pizarro-2022104348/ |
| ref-1368 | Aalto University School of Science 석사 논문(저자 미확인) | A deep learning approach to wall recognition in industrial architectural floor plan images | 논문 | medium | https://aaltodoc.aalto.fi/items/69293ef2-19d9-4081-99c8-b30af833da8a |
| ref-1369 | Ospici, M., Gueze, A., Bourrat, L., & Bernhardt, A. | Mitigating Domain Shift in Conditioned Floor Plan Generation: Synthetic Pre-training for Data-Efficient Adaptation | 논문 | medium | https://arxiv.org/abs/2607.06483 |
| ref-1370 | Lee, W.-J., & Yun, S.-S. (KIST, Applied Sciences 14(13), 5671) | Automated Destination Renewal Process for Location-Based Robot Errands | 논문 | medium | https://www.mdpi.com/2076-3417/14/13/5671 |
| ref-1371 | Esri (ArcGIS Pro documentation) | Import BIM To Indoor Dataset (Indoors) | 벤더 문서 | medium | https://doc.esri.com/en/arcgis-pro/latest/tool-reference/indoors/import-bim-to-indoor-dataset.html |
| ref-1372 | Thunderhead Engineering (Pathfinder documentation 2026-1) | IFC Import (Pathfinder How-To) | 벤더 문서 | medium | https://www.thunderheadeng.com/docs/2026-1/pathfinder/examples/how-to/ifc-import |
| ref-1373 | ti-insight (Transport Intelligence) | CEVA deploys Automated Mobile Robots at its Melbourne site | 기사 | low | https://ti-insight.com/?p=113161 |
| ref-1374 | ABB Robotics | AMR Studio — A simple and intuitive way to set up AMRs | 벤더 문서 | low | https://www.abb.com/gb/en/areas/robotics/products/software/amr-studio-suite/amr-studio |
| ref-1375 | Kollmorgen | Kollmorgen launches NDC Layout Assistant | 벤더 문서 | medium | https://www.kollmorgen.com/en-us/company/press-releases/2026/kollmorgen-launches-ndc-layout-assistant-your-simple-solution-smart |
| ref-1376 | BlueBotics | ANT lab configuration software | 벤더 문서 | low | https://bluebotics.com/autonomous-navigation-technology/ant-lab-configuration-software |
| ref-1377 | Logistics Matters | Fulfillment centre deploys AMRs in 12 days | 기사 | low | https://www.logisticsmatters.co.uk/?p=1091 |
| ref-1378 | Ganon, K., Alper, M., Mikulinsky, R., & Averbuch-Elor, H. (WACV 2025) | WAFFLE: Multimodal Floorplan Understanding in the Wild | 논문 | medium | https://arxiv.org/abs/2412.00955 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 공공 AI 학습 데이터(AI Hub 등)나 연구 과제에 물류센터·공장·병원 같은 비주거 건축 도면을 랙·도크·승강기·충전 구역 라벨과 함께 담은 데이터셋이 있거나 구축 계획이 있는가? (관련 기존 질문: oq-197, 트랙 질문 q2-04) | 14, 45 | 열림 | — |
| new | — | 출처 충돌: FloorPlanCAD 의 범주 수는 30개(arXiv 초록)인가 35개(프로젝트 페이지)인가? | 14, 45 | 열림 | — |
| new | — | 출처 충돌: ArchCAD-400K 의 의미 범주에 엘리베이터가 있는가(앞선 실행의 검색 요약과 v3 본문 열람 결과가 다르다)? | 14, 45 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 트랙 현재 단계 표기 정리: config/tracks/floorplan-recognition.yaml 의 current_stage 는 1, target.json 은 2, 트랙 개요 자동 진행 현황 표는 단계 1 이다. 이번 재실행에서 개요 상태 줄은 2차 검증 지시대로 '단계 2. 필요한 데이터와 표준 조사'로 고쳤으나 자동 표(auto:track-progress)와 트랙 정의 값은 pipeline 담당이 함께 맞춰 주기 바란다.
- 아이디어 페이지(docs/ideas/floorplan-recognition.md)의 last_run 은 3절 패치의 frontmatter 로 보냈다. 패치 적용 코드가 frontmatter 필드를 반영하는지 확인이 필요하다.
- 단계 1 페이지·아이디어 페이지의 기존 각주 ref-067·ref-073·ref-076·ref-163 정의는 앞선 실행의 '접근일 2026-09-25 (원문 미열람)'으로 남아 있다. 이번 실행에서 이 출처들을 열람했으므로 참고문헌 색인 갱신 뒤 각주 정의를 맞출지 퍼블리셔·참고문헌 담당이 정해 주기 바란다.
- q1-08 나머지: 국내 물류센터에서 지도 작성·공용 자원 등록·제조사별 좌표 정렬에 든 시간을 단계별로 공개한 공공·학술 자료(한국로봇산업진흥원 실증사업 보고서, 스마트물류센터 인증 자료 등)가 단계 1 페이지 q1-08 부분 답을 채우는 데 필요하다.
- 단계 1 페이지 q1-05 소절의 불확실성 해소: ArchCAD-400K 의 엘리베이터 범주(앞선 검색 요약과 v3 본문 결과 충돌), FloorPlanCAD 개정판(v2)이 학교·병원·쇼핑몰을 포함하는지, Aalto 석사 논문의 저자·연도·성능 수치 확인이 필요하다.
- AI Hub 건축 도면 데이터의 이용정책 별도 페이지(상업적 이용 조건)와 구조 8개 클래스 전체 목록이 q2-04·oq-197 답에 필요하다.
- 단계 1 페이지 q1-06 소절 보강: KIST Lee·Yun 논문의 건물 유형·단계별 수치, ABB AMR Studio 원문, MiR Fleet Enterprise 문서(파일 크기 초과로 이번에 열지 못함)의 재열람이 필요하다.
- 참고문헌 id 충돌: ref-1367~ref-1376 이 실행 2026-10-09-19 의 다른 출처 id 와 겹친다는 1차 검증 지적에 따라 퍼블리셔가 게시 전 id 충돌을 검사하고 필요하면 재번호한 뒤 이번 페이지 각주를 함께 바꿔야 한다.

## 이행한 수정 지시

- f2 — 단계 1 페이지 q1-05 소절과 아이디어 페이지 3절의 새 소절에 FloorPlanCAD 를 '초록 기준 1만 장 이상·30개 범주(ref-067)'로 적고 프로젝트 페이지 기준 '15,663장·35개 범주(ref-066)'를 함께 제시했으며 기존 3절 표는 그대로 두었고, open_question_updates 에 '출처 충돌: FloorPlanCAD 의 범주 수는 30개(arXiv 초록)인가 35개(프로젝트 페이지)인가?'(areas 14·45)를 new 로 냈다.
- f9 — 단계 1 페이지와 아이디어 페이지의 '둘 다 비상업 이용 제한' 종합 문장에 FloorPlanCAD 라이선스 근거로 [^ref-066] 각주를 더했다.
- f20·ref-1377 — reference_updates 의 published 를 2022-10-26 으로 고치고 각주 발행일과 본문 기준일을 '업체 제공 기사(2022-10-26)'로 적었으며, 12일 수치는 Geek+ 측 발언으로 밝히고 [추정]·'벤더 주장' 병기를 유지했다.
- ref-1378 — reference_updates 의 org 와 두 페이지의 각주 기관 표기를 'Ganon, K., Alper, M., Mikulinsky, R., & Averbuch-Elor, H. (WACV 2025)'로 고쳤다.
- ref-1012 — 각주 발행일을 2023-07-26 으로 두고, 단계 1 페이지와 아이디어 페이지 본문에 '1.1 판 2023-12-15, 최종 변경 2025-05-08, 확인일 2026-10-09'를 병기했으며 ref-074 는 새로 인용하지 않았다.
- f16 — '실제 다층 건물의 CAD 도면'을 '다층 건물의 CAD 도면'으로 고쳐 썼고 ref-1370 각주 접근일 뒤에 ' (원문 미열람)'을 붙였다.
- f4·f14·f16·ref-227 — ref-1368·ref-1374·ref-1370 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 네 항목에 source_unopened: true 를 넣었으며(ref-227 은 기존 페이지 각주 정의에 이미 표시가 있어 새 정의를 추가하지 않음), f4 의 저자·연도는 '미확인'으로 남겼다.
- f7 — Ospici 외 문장 안에 '인식이 아닌 생성 과제에서 주거 데이터셋 사이로 옮긴 결과'이며 '인식 과제에 대한 유추 근거로만 쓴다'를 함께 밝히고 '최대 한 자릿수 배'를 유지했다.
- 직접 인용 — ref-073·ref-079 를 포함해 모든 출처를 재서술로만 쓰고 직접 인용을 넣지 않았으며 ref-079 원문의 'backgroud' 구절은 인용하지 않았다.
- q1-05·q1-06 답 — 단계 1 페이지 3절 {#q1-05}·{#q1-06} 첫 문장에 '이번 검색 범위에서 찾지 못함(부재 확인 아님)'과 종합 신뢰도 low 를 밝히고 종합 문장(f9·f17)을 [추정]으로 두었으며, 백로그는 q1-05·q1-06 답함, q1-08 조사 중(answer_link null), 2절 표는 q1-05·q1-06 답함, q1-08 열림으로 적었다.
- 질문–finding 대응 — 단계 1 페이지 갱신 제안의 rationale 을 규약 1항으로 읽어 단계 1 페이지에 답을 실었고, 단계 2 페이지는 pages 에 넣지 않아 6절 전환 줄과 상태 줄 '진행 중'을 바꾸지 않았으며 track_updates.stage_transition 을 넣지 않았다.
- 새 트랙 질문 — 단계 2 질문을 q2-10(origin f9), 단계 3 질문을 q3-12(origin f17)로 backlog_updates 에 등록하고 단계 1 페이지 5절 표에 실었다.
- open_questions_new — 질문 문장 끝에 '(관련 기존 질문: oq-197, 트랙 질문 q2-04)'를 덧붙여 areas [14, 45]로 open_question_updates 에 new 로 냈다.
- 용어 후보 — '일반화 보로노이 그래프' 정의를 f16 범위('격자 지도를 세선화해 얻는 골격 그래프로, 로봇 주행용 초기 노드를 만들고 방 분할에 쓰인다')로 줄여 sources 에 ref-1370 을 달았고, '도메인 이동'에는 sources ref-1369 를 달았다.
- 참고문헌 id — reference_updates 에 브리프 id 를 그대로 쓰고 URL·제목을 브리프 sources 와 같게 적었으며, ref-1367~ref-1376 이 실행 2026-10-09-19 의 같은 id(다른 URL)와 충돌한다는 사실을 changelog_entry 에 적었다.
- 세부영역 반영 — 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해, 55. 현장 조사·설치·시운전 반영은 area_reflection_proposals 로만 냈고 세부영역 페이지는 고치지 않았으며, 55 의 5절 제안에서 f19 는 '물류창고', f18 은 '기타'(대학 건물, 연계 대상)로 현장 유형을 밝혔다.
- 범위 — f13·f18 문장에 '연계 대상:' 표시를 유지했고, f11·f12 문장은 각각 '로봇 관제 제품이 아닌 실내 GIS 도구의 비교 사례', '로봇 관제 제품이 아닌 피난 시뮬레이터의 비교 사례'임을 같은 문장에 밝혔다.
- 2차: index_updates.category_recent — '14·45·55 세부영역'을 '14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해, 55. 현장 조사·설치·시운전 세부영역'으로 고쳐 번호와 이름을 함께 썼다.
- 2차: 단계 1 페이지 프런트매터 — sources 에 ref-1012·ref-1367~ref-1378 13건을 더하고 related_areas 에 14·45 를 더했으며 last_run 을 2026-10-09 로 고쳤다(페이지 전체 content 로 보냄).
- 2차: 단계 1 페이지 상태 줄 — '> 단계 상태: 재개 · 열린 질문: 1건 · 답한 질문: 6건 · 완료 조건: 충족 · 마지막 실행: 2026-10-09' 로 고쳤고, 이 줄이 절 밖이라 페이지 전체 content 로 보냈다.
- 2차: 단계 1 페이지 5절 — 첫 표의 q1-05·q1-06 행 상태를 '열림'에서 '답함'으로 고쳤다.
- 2차: 단계 1 페이지 6절 — 표 아래 줄을 '다음 단계로 전환: 아니오(막힌 질문 q1-08)'로 고쳤다.
- 2차: 단계 1 페이지 9절 — 실행 2026-10-09-21 이력 행의 버전 칸을 '6'으로 고쳤다.
- 2차: 단계 1 페이지 q1-05 소절 — ArchCAD-400K 항목 바로 뒤에 'q1-01 소절은 검색 요약을 근거로 ArchCAD-400K 에 엘리베이터 범주가 있다고 보았으나 이번 v3 본문 열람 범위에서는 확인되지 않아 두 근거가 다르다. [추정][^ref-073]' 연결 문장과 열린 질문 링크를 두었고, 4절 남은 불확실성에도 한 줄을 더했으며, open_question_updates 에 '출처 충돌: ArchCAD-400K 의 의미 범주에 엘리베이터가 있는가(앞선 실행의 검색 요약과 v3 본문 열람 결과가 다르다)?'(areas 14·45, 열림)를 new 로 냈다.
- 2차: 트랙 개요(docs/tracks/floorplan-recognition/index.md) — 상태 줄을 '> 트랙 상태: active · 현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-10-09' 로, 프런트매터 last_run 을 2026-10-09 로 고쳐 페이지 전체 content 로 보냈다.
- 2차: 아이디어 페이지(docs/ideas/floorplan-recognition.md) — 3절 패치의 frontmatter 에 last_run: 2026-10-09 를 더했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 1.2
- 트랙 로그 항목: 답한 질문: q1-05(f1·f2·f3·f4·f5·f6·f7·f8·f9), q1-06(f10·f11·f12·f13·f14·f15·f16·f17) — 단계 2 진행 중에 되돌아온 단계 1 질문, 종합 신뢰도 low; 부분 답 q1-08(f18·f19·f20·f21, 국내 단계별 소요 시간 자료 없음) / 새 질문: q2-10(단계 2. 필요한 데이터와 표준 조사, f9), q3-12(단계 3. 구현 가설 설계, f17) / 온톨로지 변경: 없음(공간 그래프 스키마 초안 v1.2 유지 — 이번 finding 은 데이터셋·제품·도입 기간에 관한 것으로 개념·관계를 뒷받침하지 않음) / 완료 조건 평가: 미충족(부족: 관계(엣지) 쪽 표준 대응이 공간 그래프 스키마 초안에 없음; 단계 2 열린 질문 q2-04·q2-06·q2-07·q2-08·q2-09·q2-10; 되돌아온 질문 q1-08 부분 답), 단계 전환 미승인 / 세부영역 반영 제안: 14. 도면·BIM에서 지도 만들기(8·11절), 45. 문서·도면·장면 이해(8절), 55. 현장 조사·설치·시운전(5·11절) — 3개 영역 5건 / 다음 실행 제안: q2-04(이번 AI Hub 확인으로 부분 근거 확보), q2-07, q2-10
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 6, 답함 3, 완료 조건 미충족. 되돌아온 단계 1 질문 q1-05·q1-06 답함, q1-08 조사 중(부분 답)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-05 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-05 | — | — | — |
| q1-06 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-06 | — | — | — |
| q1-08 | 조사 중 | — | — | — | — |
| q2-10 | 열림 | — | 물류센터·창고 평면도 인식에 필요한 학습 데이터(랙·도크·충전 구역·작업 스테이션·엘리베이터 라벨, 규모)를 어떻게 마련하는가 — 소량 직접 주석으로 미세조정, 절차적 합성 평면도 사전학습, 산업단지를 포함한 비주거 CAD 데이터셋(ArchCAD-400K 등) 활용 가운데 무엇이 가능하며 각각의 이용 조건(비상업 제한)은 어떤가? (q1-05 에서 파생) | 2 | f9 |
| q3-12 | 열림 | — | BIM 에서 층·문·계단을 자동 추출하는 로봇 밖 도구(실내 GIS 가져오기, 피난 시뮬레이터)의 출력을 ROP 공간 그래프의 입력 초안으로 그대로 쓸 수 있는가, 쓴다면 엘리베이터·충전 위치·작업 스테이션은 어떤 정보로 보완하는가? (q1-06 에서 파생) | 3 | f17 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 14 | 8. 대표 연구와 자료 | 비주거 도면 데이터셋 구성: ArchCAD-400K(v3, 2025-03)는 주거 14%이고 사무 단지·산업단지를 포함하며 27개 범주에 엘리베이터 범주가 확인되지 않음(앞선 검색 요약과 충돌, 열린 질문), FloorPlanCAD 는 초록 기준 1만 장 이상·30개 범주(프로젝트 페이지 기준 15,663장·35개 범주와 출처 충돌), AI Hub 건축 도면 데이터는 48,033장이 모두 주거 유형(1.1 판 2023-12-15, 확인일 2026-10-09). 산업용 건물 평면도 500장 전이 실패와 소량 재학습 효과(Aalto 석사 논문, 원문 미열람), KIST Lee·Yun(2024-07)의 CAD 평면도→격자 지도·GVG 세선화·목적지 자동 갱신(원문 미열람), 물류 로봇 관제 제품의 도면 자동 가져오기는 이번 검색 범위에서 확인하지 못함([추정], 부재 확인 아님). 근거 f1·f2·f3·f4·f16·f17, 실행 2026-10-09-21. |
| 14 | 11. 열린 질문 | oq-196(비주거 도면 인식 성능)에 산업용 건물 도면 전이 실패 부분 근거(f4), oq-197(AI Hub 라벨·비주거 비율)에 '주거 3유형뿐' 부분 근거(f3), oq-299(VLM 개방 구역 저하)에 f6·f9 부분 근거를 덧붙이고(해결 아님), 새 열린 질문(국내 공공 데이터의 비주거 도면 라벨)과 FloorPlanCAD 범주 수·ArchCAD-400K 엘리베이터 범주 출처 충돌 질문을 연결한다. 실행 2026-10-09-21. |
| 45 | 8. 대표 연구와 자료 | 분류 원문 13장 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 모델의 도메인 이동 근거를 싣는다: 산업용 건물 도면 전이 실패와 수작업 주석 32장 재학습 효과(f4, 원문 미열람), 평면도 분석 연구의 도면 양식 의존·표준 지표 부재·공개 데이터셋 부족(f5, Pizarro 외 2022-01), VLM 평면도 해석의 큰 개방 구역 성능 저하(f6), 생성 과제의 교차 데이터셋 저하와 합성 사전학습(f7, 인식 과제에는 유추 근거), 물류 도면 대상 성능 측정값 부재 종합(f9, [추정]). 실행 2026-10-09-21. |
| 55 | 5. 적용 사례 (현장 유형 명시) | 현장 유형 물류창고: CEVA 멜버른 시설(약 25만㎡)의 400㎡ 시범 구역에 Geek+ 로봇 8대를 3주 만에 구현했으나 단계별 기간 미분해(f19, 2020-04-28 기사), 홍콩 풀필먼트 센터 Geek+ 하드웨어 구현 12일([추정] 벤더 주장, f20, 2022-10-26). 현장 유형 기타(대학 건물, 연계 대상): KAIST N1 5개 층 자율 다층 지도 작성 27분·기준 대비 탐사 시간 약 33% 단축, 수작업 비교 없음(f18). 실행 2026-10-09-21. |
| 55 | 11. 열린 질문 | 국내 물류센터의 지도 작성·공용 자원 등록·제조사별 좌표 정렬 단계별 소요 시간을 공개한 공공·학술 자료는 이번 검색 범위(한국어 검색 6회)에서 찾지 못했다([추정], 부재 확인 아님, f21). oq-119(설정 공수 산정 기준)의 부분 근거로 연결한다. 실행 2026-10-09-21. |
