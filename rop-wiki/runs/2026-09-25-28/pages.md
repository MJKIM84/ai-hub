# 스토리텔러 산출 2026-09-25-28

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | draft | q2-01 답함(공간 그래프 표준 조사), 3절 조사 결과·4절 결론 신규 작성, 후속 질문 2건(q2-07·q3-05), 완료 조건 미충족·전환 미승인, 단계 상태 진행 중. 상태 줄 갱신이 필요해 patches 대신 전체 content로 보냄 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.3 → v0.4: 공간 노드·층에 표준 대응 클래스(후보) 속성, 층 확정, 주제 레이어 추가·확정. 문 대응·레이어 구분·IFC 수직 연결은 6절 질문. H1 버전 표기 변경이 필요해 전체 content로 보냄 |
| update | docs/ideas/floorplan-recognition.md | draft | 4절에 '공간 그래프를 표현하는 표준' 소절 덧붙임(q2-01 요약 비교표, 국내 규정, 종합). 입력 형식별 정보 항목(q2-02)·관제 수용 형식(q2-03)은 아직 없음을 명시 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 스키마 초안 v0.4, 아이디어 페이지 4절 표준 소절, 백로그 q2-01 답함·후속 질문 2건 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 2 | q2-01 답함(IndoorGML 2.0·IFC 4.3·CityGML 3.0·ISO 19164·BOT·ifcOWL·Brick·IMDF 공간 그래프 표준 정리), 공간 그래프 스키마 초안 v0.3 → v0.4, 후속 질문 2건 | run 2026-09-25-28
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: q2-01 답함(공간 그래프를 표현하는 표준 비교), 공간 그래프 스키마 초안 v0.4
- 대분류 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2(중심 영역 6. 지도·공간·위치 모델): 실내 공간 표준(IndoorGML 2.0·IFC 4.3·CityGML 3.0·ISO 19164·IMDF)의 공간 연결 표현 비교, 공간 그래프 스키마 초안 v0.4
- 세부영역 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: 공간 그래프 표준 비교(q2-01)를 7. 관련 표준·프레임워크·오픈소스 절 반영 제안으로 남김

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 건물 정보 모델링 | Building Information Modeling (BIM) | 건물의 공간·요소·속성을 객체 단위의 디지털 모델로 만들고 설계·시공·운영 단계에서 공유하는 방식으로, IFC 가 그 개방형 교환 스키마다. | 6, 28 | ref-502, ref-156 |
| new | 공간 그래프 | Space Graph | 방·복도 같은 공간을 노드로, 문·공유 경계·계단·엘리베이터 같은 연결을 엣지로 두어 건물 실내의 연결 관계를 나타내는 그래프로, IndoorGML 의 쌍대 그래프가 대표적 표준 표현이다. | 6, 15, 28 | ref-498, ref-499 |
| new | 건물 위상 온톨로지 | Building Topology Ontology (BOT) | W3C 링크드 빌딩 데이터 커뮤니티 그룹이 만든, 건물의 대지·건물·층·공간·요소와 그 포함·인접 관계를 RDF 로 기술하는 최소 온톨로지이다. | 6, 28 | ref-503, ref-504 |
| new | 실내 지도 데이터 형식 | Indoor Mapping Data Format (IMDF) | Apple 이 개발해 OGC 커뮤니티 표준이 된 실내 지도 형식으로, 층·공간 단위·출입구·편의시설 등을 사람 길안내용으로 모델링한다. | 6, 28 | ref-505 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-156 | buildingSMART International | IFC 4.3 documentation — IfcSpace (IFC4.3.x-development) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md |
| ref-157 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | IndoorGML-SWG — README and OGC IndoorGML 2.0 Part 2a – XML Encoding (26-042, Candidate SWG Draft) | 표준 | medium | https://github.com/opengeospatial/IndoorGML-SWG |
| ref-158 | ISO | ISO 19164:2024 - Geographic information — Indoor feature model | 표준 | medium | https://www.iso.org/standard/83153.html |
| ref-214 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md |
| ref-498 | OGC (Open Geospatial Consortium) | OGC IndoorGML 2.0 Part 1 – Conceptual Model (22-045r5) | 표준 | medium | https://docs.ogc.org/is/22-045r5/22-045r5.html |
| ref-499 | OGC (Open Geospatial Consortium) | OGC Publishes IndoorGML 2.0 Part 1 Conceptual Model Standard | 표준 | medium | https://www.ogc.org/announcement/ogc-publishes-indoorgml-2-0-part-1-conceptual-model-standard/ |
| ref-500 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | OGC IndoorGML 2.0 Part 2b – JSON Encoding (26-043, Candidate SWG Draft v0.5.0) | 표준 | high | https://github.com/opengeospatial/IndoorGML-SWG/blob/master/26-043.html |
| ref-501 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcRelSpaceBoundary (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcRelSpaceBoundary.md |
| ref-502 | ISO | ISO 16739-1:2024 - Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema | 표준 | medium | https://www.iso.org/standard/84123.html |
| ref-503 | W3C Linked Building Data Community Group (w3c-lbd-cg GitHub) | Building Topology Ontology (BOT) — bot.ttl (version 0.3.2) | 표준 | high | https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl |
| ref-504 | Rasmussen, M. H., Lefrançois, M., Schneider, G. F., & Pauwels, P. | BOT: The building topology ontology of the W3C linked building data group | 논문 | medium | https://journals.sagepub.com/doi/10.3233/SW-200385 |
| ref-505 | OGC (Open Geospatial Consortium) / Apple | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 표준 | medium | https://docs.ogc.org/cs/20-094/ |
| ref-506 | OGC (Open Geospatial Consortium) | OGC City Geography Markup Language (CityGML) Part 1: Conceptual Model Standard (20-010) | 표준 | medium | https://docs.ogc.org/is/20-010/20-010.html |
| ref-507 | PFG(Journal of Photogrammetry, Remote Sensing and Geoinformation Science) 게재 논문 저자(미확인) | CityGML 3.0: New Functions Open Up New Applications | 논문 | medium | https://link.springer.com/article/10.1007/s41064-020-00095-z |
| ref-508 | Brick Consortium (Brick Schema) | Relationships — Brick Ontology Documentation | 오픈소스 문서 | medium | https://docs.brickschema.org/brick/relationships.html |
| ref-509 | buildingSMART (buildingsmart-community GitHub) | ifcOWL — README (ifcOWL standard) | 표준 | high | https://github.com/buildingsmart-community/ifcOWL |
| ref-510 | Zhu, J., Wong, M. O., Nisbet, N., Xu, J., Kelly, T., Zlatanova, S., & Brilakis, I. | Semantics-based connectivity graph for indoor pathfinding powered by IFC-Graph | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S0926580525000597 |
| ref-511 | 이기준, 이지영(한국공간정보학회지) | 실내공간 표준안 IndoorGML의 개념 및 활용 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001786322 |
| ref-512 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 정부·연구기관 | medium | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 |
| ref-513 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg |
| ref-514 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 논문 | medium | https://arxiv.org/abs/2305.07154 |
| ref-515 | ISPRS International Journal of Geo-Information(MDPI) 게재 논문 저자(미확인) | Data Model for IndoorGML Extension to Support Indoor Navigation of People with Mobility Disabilities | 논문 | medium | https://www.mdpi.com/2220-9964/9/2/66 |
| ref-516 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Graph.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Graph.msg |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? | 6, 28 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) | 표준 | OGC | 6, 28 | ref-506 | https://docs.ogc.org/is/20-010/20-010.html |
| IMDF (Indoor Mapping Data Format) 1.0.0 | 표준 | OGC / Apple | 6, 28 | ref-505 | https://docs.ogc.org/cs/20-094/ |
| BOT (Building Topology Ontology) 0.3.2 | 프레임워크 | W3C Linked Building Data Community Group | 6, 28 | ref-503 | https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl |
| ifcOWL | 표준 | buildingSMART | 6, 28 | ref-509 | https://github.com/buildingsmart-community/ifcOWL |
| Brick Schema | 오픈소스 | Brick Consortium | 6, 10 | ref-508 | https://docs.brickschema.org/brick/relationships.html |
| ISO 16739-1:2024 (IFC 4.3) | 표준 | ISO | 6, 28 | ref-502 | https://www.iso.org/standard/84123.html |

## 추가 조사 요청

- 단계 2 페이지 3절·스키마 초안 6절: IndoorGML 2.0 Part 1 본문(22-045r5)을 열어 문·엘리베이터·계단을 어느 클래스(NavigableBoundary·TransferSpace 등)로 표현하는지 확인해야 문의 표준 대응 클래스를 정할 수 있다(q2-07).
- 단계 2 완료 조건: 입력 형식별 정보 항목(q2-02)과 층별 지도·공용 자원 목록의 관제 수용 형식(q2-03)을 조사해야 아이디어 페이지 4절이 채워진다.
- 스키마 초안 3절: 표준에 대응시킨 관계(엣지) 유형(IndoorGML Edge·InterLayerConnection, BOT adjacentZone, IfcRelSpaceBoundary 2차 A 유형 등)과 스키마 관계의 대응 근거가 필요하다.
- 교차 확인: IndoorGML·IFC·CityGML·IMDF 주장이 모두 발행 기관 한 곳의 자료에 기대므로 독립 출처(논문·구현 문서)로 교차 확인이 필요하다.
- 단계 2 3절 국내 규정: 실내공간정보 구축 작업규정 현행판(2021-12-24 개정판)의 조문과 ISO 19164·IndoorGML 2.0 KS 부합화 여부 확인이 필요하다.

## 이행한 수정 지시

- f3 외부 참조 문구 — 단계 2 페이지 3절 IndoorGML 소절에서 '외부 모델을 가리키는 외부 참조 형식(ExternalReferenceType)'으로 쓰고 IFC 를 예로 드는지는 미확인이라고 적었다.
- f23 문구 — 단계 2 페이지 3절 '분류 원문 질문과의 관계'와 4절 결론에서 '외부 참조 형식으로 공간 셀을 IFC 같은 외부 모델 요소에 이을 수 있을 것으로 보이고'로 고치고 [추정]을 유지했다.
- f9 세부 — 수평 연결 도출 관계와 '계단 4개'는 본문에 쓰지 않고 '원문 미열람으로 미확인'을 병기했으며, IfcRelConnectsSpace 부분은 [사실]로 유지했다(단계 2 페이지 3절, 스키마 초안 6절).
- f5 부속서 대응 — 단계 2 페이지 3절과 아이디어 페이지 4절에 '검색 요약 기준(원문 미열람)'을 병기했다.
- f17 기준일 — 단계 2 페이지 3절·아이디어 페이지 4절에 '2018-03-05 제정판 기준'을 명시하고 현행 조문의 원칙 유지 여부는 미확인으로 적었다.
- f20 — 단계 2 페이지 3절 '대조 사례'에서 '연계 대상:' 표시를 유지하고 대조 사례로만 두었으며, 28. 표준·상호운용성·다사업자 거버넌스 반영 제안에서 뺐다.
- f21·f22 — 5분류와 클래스 대응을 '이 위키의 정리'로 밝히고 [추정]을 유지했으며, CityGML 3.0 연결 도출 부분은 '확인된 발견 사항이 없는 이 위키의 추론'이라고 별도 문장으로 드러냈다.
- 온톨로지 승인 변경 — 공간 노드·층에 '표준 대응 클래스(후보)' 속성(공간 노드는 1:1 대응 여부 미확정 병기)을 더하고 층을 확정, 주제 레이어를 정의를 한정해 추가·확정했다. H1 (v0.4), 프런트매터 ontology_version '0.4', track_updates.ontology_draft_version '0.4' 를 맞췄고, auto 상태 줄은 마커 안이라 퍼블리셔가 프런트매터 값으로 v0.4 를 채우도록 두었다.
- 문 표준 대응 클래스 — 개념 표에 반영하지 않고 스키마 초안 6절 미해결 질문으로 두었으며 q2-07·q2-01 을 관련 id 로 적었다.
- 주제 레이어의 로봇·사람 레이어 구분 — 개념 정의에 넣지 않고 6절 질문으로 두었으며 아이디어 정의 밖 개념의 1절 범위 관계도 함께 적었다.
- f8·f9 — 스키마 초안 6절의 IFC 수직 연결 도출·확장 질문 근거로만 두고 개념·관계 표에는 넣지 않았다.
- ref-514 — reference_updates 의 기관과 단계 2 페이지 각주를 'Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L.'로 고쳤다.
- 원문 미열람 표시 — 지정한 15개 출처의 각주 정의(단계 2 페이지·스키마 초안·아이디어 페이지)에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- ref-225 — 어느 페이지에서도 새 각주로 인용하지 않았고 reference_updates 에 넣지 않았다.
- 단계 2 페이지 — 2절 q2-01 답함·2026-09-25-28·#q2-01, 3절 '### q2-01 … {#q2-01}', 6절 두 항목 미충족·지시된 전환 불가 문구, 상태 줄 '진행 중 · 완료 조건: 미충족'으로 썼다(상태 줄은 H2 밖이라 전체 content 로 보냄). 트랙 개요 상태 줄은 이미 '단계 1 … · 마지막 트랙 실행: 2026-09-25'라 바꾸지 않았다.
- 아이디어 페이지 4절 — '공간 그래프를 표현하는 표준' 소절을 덧붙이고 q2-02·q2-03 이 아직 없음과 표가 검증된 finding 으로 직접 만든 것임을 밝혔다.
- 세부영역 반영 — 6. 지도·공간·위치 모델과 28. 표준·상호운용성·다사업자 거버넌스 페이지는 고치지 않고 area_reflection_proposals 로만 냈다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.4
- 트랙 로그 항목: 답한 질문: q2-01(공간 그래프를 표현하는 표준: IndoorGML 2.0·IFC 4.3·CityGML 3.0·ISO 19164·BOT·ifcOWL·Brick·IMDF, 국내 실내공간정보 구축 작업규정, 대조 사례 Open-RMF 건물 지도·3D 장면 그래프(연계 대상); 근거 f1~f23) / 새 질문: q2-07(단계 2. 필요한 데이터와 표준 조사, f4), q3-05(단계 3. 구현 가설 설계, f9) / 온톨로지 변경: v0.3 → v0.4: 공간 노드 속성 '표준 대응 클래스(후보)' 추가(f3·f6·f12·f14·f15), 층 속성 '표준 대응 클래스(후보)' 추가와 층 확정(f6·f12·f15), 개념 '주제 레이어' 추가·확정(f2·f3). 거부: 문 '표준 대응 클래스' 속성(IndoorGML 2.0 의 문 표현 미확인 → 6절 질문, q2-07·q2-01), 주제 레이어의 로봇·사람 레이어 구분(근거 없음 → 6절 질문). 근거 실행 2026-09-25-28 / 완료 조건 평가: 미충족(부족: 입력 형식별 정보 항목 q2-02·관제 수용 형식 q2-03 미작성, 엣지 쪽 표준 대응 없음; 막힌 질문 q2-02·q2-03·q2-04·q2-06; 단계 전환 미승인) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건(7. 관련 표준·프레임워크·오픈소스, 11. 열린 질문), 28. 표준·상호운용성·다사업자 거버넌스 1건(7. 관련 표준·프레임워크·오픈소스) / 다음 실행 제안: q2-02, q2-03(이어서 q2-07, q2-06)
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 5, 답함 1, 완료 조건 미충족(트랙 개요의 현재 단계 표기는 단계 1. 선행 연구·제품 사례 조사 유지, 단계 전환 미승인)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-01 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-01 | — | — | — |
| q2-07 | 열림 | — | IndoorGML 2.0 Part 1 발행판은 문·엘리베이터·계단 같은 연결과 수직 이동을 NavigableBoundary·TransferSpace 등 어떤 클래스로 표현하며, 1.x 의 ConnectionSpace·TransitionSpace 구성과 무엇이 달라졌는가? (q2-01 에서 파생) | 2 | f4 |
| q3-05 | 열림 | — | IFC 에 공간 사이 수직 연결 관계가 없을 때, IfcRelConnectsSpace 같은 사용자 확장 없이 IfcStair·IfcTransportElement 와 층 소속·공간 경계 관계만으로 층간 연결 엣지를 도출하려면 어떤 규칙이 필요한가? (q2-01 에서 파생) | 3 | f9 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 7. 관련 표준·프레임워크·오픈소스 | 표준마다 공간 연결을 표현하는 방식을 더한다: IndoorGML 2.0(Part 1 개념 모델 2025-08 발행, 쌍대 그래프·주제 레이어, Part 2 인코딩 초안), IFC 4.3(IfcSpace·IfcBuildingStorey·IfcRelSpaceBoundary, 공간 사이 직접 연결 관계는 도출 필요 추정), CityGML 3.0(BuildingRoom·Storey·DoorSurface), ISO 19164:2024(의미 분류, 부속서 대응은 원문 미열람), IMDF(사람 길안내 형식), 국내 실내공간정보 구축 작업규정(2018-03-05 제정판 기준 CityGML 2.0·IndoorGML 공간 개념 원칙). 근거 f1·f2·f3·f5·f6·f8·f14·f15·f17·f21(실행 2026-09-25-28). |
| 6 | 11. 열린 질문 | 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가(근거 f17, 실행 2026-09-25-28). |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | 실내 공간 표준의 발행 상태를 더한다: IndoorGML 2.0 Part 1 발행·Part 2 인코딩 초안(JSON v0.5.0), ISO 19164:2024(표준 간 클래스 대응 부속서, 원문 미열람), ISO 16739-1:2024(IFC 4.3), ifcOWL(IFC4_ADD2까지, 4.3 목록 없음), BOT v0.3.2(커뮤니티 그룹 사양), IMDF 1.0.0(OGC 커뮤니티 표준). 근거 f1·f3·f5·f10·f11·f12·f15(실행 2026-09-25-28). 3D 장면 그래프(f20)는 로봇 자체 지능·제어 연계 대상이라 제외. |
