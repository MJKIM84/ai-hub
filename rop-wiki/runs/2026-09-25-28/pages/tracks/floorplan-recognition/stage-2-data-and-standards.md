---
title: "단계 2. 필요한 데이터와 표준 조사"
type: track-stage
track: floorplan-recognition
stage: 2
related_areas: [28, 6, 10]
tags: [BIM, IFC, IndoorGML, 실내 공간 표준, 지도 형식]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-156, ref-157, ref-158, ref-214, ref-331, ref-332, ref-333, ref-334, ref-335, ref-336, ref-337, ref-338, ref-339, ref-340, ref-341, ref-342, ref-343, ref-344, ref-345, ref-346, ref-347, ref-348, ref-349]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › 중점 연구 트랙 › [건축 도면 자동 인식](index.md) › 단계 2. 필요한 데이터와 표준 조사

# 단계 2. 필요한 데이터와 표준 조사

> 단계 상태: 진행 중 · 열린 질문: 5건 · 답한 질문: 1건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 도면 입력 형식마다 어떤 공간 정보가 들어 있고, 공간 그래프·층별 지도·공용 자원 목록을 어떤 표준·형식으로 표현하고 교환하는가.

위 문장은 트랙 정의의 "밝힐 것"이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 조사 결과는 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)과 [공간 그래프 스키마 초안](space-graph-schema-draft.md)으로 이어진다.

## 2. 질문 목록

이 단계의 시작 질문 3개(q2-01~q2-03)와 앞선 트랙 실행·이번 실행에서 이 단계로 들어온 후속 질문 3개(q2-04·q2-06·q2-07)다. q2-01은 사용자 요청의 시작 질문 문구 그대로이고, q2-02·q2-03은 구축자가 이 단계의 밝힐 것에서 정한 시작 질문이다. [가정] 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"(q2-05)는 표에서 빼고 백로그에만 남긴다. 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커를 적는다. 제기 근거 칸에는 finding id(실행 id 병기) 또는 "사용자"만 쓴다.

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q2-01 | 공간 그래프를 표현하는 기존 표준(예: BIM·IFC, 실내 공간 표준)은 무엇이 있는가? | 답함 | 사용자 | 2026-09-25-28 | [답](#q2-01) |
| q2-02 | 도면 입력 형식(벡터 CAD, BIM 모델, 래스터 스캔)마다 벽·문·엘리베이터·계단·충전 위치 정보가 어떻게 들어 있고 무엇이 빠지는가? | 열림 | 사용자 | | |
| q2-03 | 층별 지도와 공용 자원 목록을 로봇 관제와 ROP가 받아들이는 형식(제조사 지도 형식, 지도 교환 형식)은 무엇이 있는가? | 열림 | 사용자 | | |
| q2-04 | AI Hub 건축 도면 데이터와 CubiCasa5K 의 클래스 목록에 계단·엘리베이터가 포함되는지, 그리고 상업적 이용 조건은 무엇인가? | 열림 | f17, 실행 2026-09-25-05 | | |
| q2-06 | 로봇 충전소·작업 스테이션처럼 IFC 4.3 표준 유형 값에 없는 운영 시설을 BIM 에 담으려면 사용자 정의 유형·속성 세트로 표현해야 하는가, 이를 정한 IDS·속성 세트 관례나 사례가 있는가? (q1-03 에서 파생) | 열림 | f10, 실행 2026-09-25-19 | | |
| q2-07 | IndoorGML 2.0 Part 1 발행판은 문·엘리베이터·계단 같은 연결과 수직 이동을 NavigableBoundary·TransferSpace 등 어떤 클래스로 표현하며, 1.x 의 ConnectionSpace·TransitionSpace 구성과 무엇이 달라졌는가? (q2-01 에서 파생) | 열림 | f4, 실행 2026-09-25-28 | | |

## 3. 조사 결과

이번 실행은 일반 웹 페이지 열람이 막힌 환경에서 이뤄졌다. 공식 GitHub 저장소 원문(IFC 4.3 개발 브랜치, IndoorGML 표준 작업반 저장소, BOT, ifcOWL, Open-RMF 메시지 정의)만 열었고, 나머지 출처는 검색 결과 요약 기준이며 각주에 "원문 미열람"을 표시했다. 표준마다 근거가 발행 기관 한 곳(또는 같은 계열)에만 있어 교차 확인된 주장은 없다.

### q2-01 공간 그래프를 표현하는 기존 표준은 무엇이 있는가 {#q2-01}

이 위키의 정리로는, 확인한 표준을 공간 연결을 노드–엣지 쌍대 그래프로 명시하는 실내 공간 표준(IndoorGML), 공간·층·경계를 담는 건물·도시 모델(IFC 4.3, CityGML 3.0), 의미 분류와 표준 간 대응을 주는 ISO 19164, 포함·인접 위상을 RDF로 담는 링크드 데이터 온톨로지(BOT·ifcOWL·Brick), 사람 길안내 지도 형식(IMDF)의 다섯 갈래로 나눌 수 있고, 공간 그래프 교환에 가장 가까운 것은 IndoorGML이지만 2.0 인코딩은 아직 초안인 것으로 보인다. 이 5분류를 제시한 단일 출처는 확인하지 못했다. [추정][^ref-331][^ref-333][^ref-156][^ref-334][^ref-339][^ref-158][^ref-336][^ref-342][^ref-341][^ref-338]

#### 실내 공간 표준: OGC IndoorGML 2.0

OGC는 2025-08-28 IndoorGML 2.0 Part 1(개념 모델, 문서 번호 22-045r5)을 발행했으며, 이 개념 모델은 실내 공간의 위상 연결과 여러 맥락을 기술하는 핵심(core) 데이터 모델과 실내 길찾기(navigation) 데이터 모델 두 부분으로 이루어진다. [사실][^ref-331][^ref-332][^ref-157]

IndoorGML은 방 같은 3차원 공간(셀)을 쌍대 공간(dual space)의 노드로, 두 공간이 공유하는 경계면을 두 노드를 잇는 엣지로 바꾸어 공간 연결 그래프를 만들고, 같은 실내를 지형(방·복도·계단) 레이어와 Wi-Fi·RFID 커버리지 레이어처럼 여러 주제 레이어로 나누어 표현한다. [사실][^ref-331][^ref-332]

IndoorGML 2.0 Part 2의 인코딩(XML 26-042, JSON 26-043, SQL 26-044)은 아직 초안이다. JSON 인코딩 초안(v0.5.0, 2026-02-28 제출, 승인·발행일 미정)은 IndoorFeatures·ThematicLayer·PrimalSpaceLayer·CellSpace·CellBoundary·DualSpaceLayer·Node·Edge와 길찾기 클래스(NavigableSpace·GeneralSpace·TransferSpace·NonNavigableSpace·ObjectSpace·NavigableBoundary·Route), 그리고 외부 모델을 가리키는 외부 참조 형식(ExternalReferenceType)을 둔다. 이 외부 참조가 IFC를 예로 드는지는 미확인이다. [사실][^ref-333][^ref-157]

IndoorGML 1.x 기반 확장 연구는 길찾기 모듈이 일반 방(GeneralSpace), 복도·계단 같은 전이 공간(TransitionSpace), 출입구(AnchorSpace), 문에 대응하는 연결 공간(ConnectionSpace)과 경로(RouteNode·RouteSegment·Route)를 두며, 교통약자 길찾기를 위해 엘리베이터·에스컬레이터·경사로를 TransitionSpace의 하위 클래스로 더했다고 설명한다(2020, 1.x 기준이며 2.0에서 같은 구성이 유지되는지는 미확인). [사실][^ref-348]

국내에서는 이기준·이지영(한국공간정보학회지 21(3), 2013)이 OGC가 IndoorGML 표준화 작업반을 꾸려 2013년 9월 발행을 목표로 했고 IndoorGML의 주된 목적이 실내 위치 기반 서비스의 기반인 실내 공간의 네트워크 위상 표현이라고 소개했다. [사실][^ref-344]

#### 건물 정보 모델: IFC 4.3

IFC 4.3은 ISO 16739-1:2024로 국제표준화되었고 교량·도로·철도·항만 같은 기반시설 정보를 더했으며, 앞선 ISO 16739-1:2018은 IFC4 ADD2 TC1에 해당한다. [사실][^ref-335]

IFC 4.3 문서(개발 브랜치 원본, 2026-09-25 확인)는 IfcSpace를 실제 또는 이론적으로 경계 지어진 면적·체적으로 건물 안에서 특정 기능을 제공하는 공간으로 정의하고, IfcRelAggregates로 건물 층(IfcBuildingStorey, 외부 공간은 IfcSite)에 묶으며, 공간 경계는 IfcRelSpaceBoundary로 정의한다. [사실][^ref-156]

IfcRelSpaceBoundary는 공간을 둘러싼 물리 요소(벽 등)·가상 요소·개구부와 공간을 잇는 객체화된 관계이며, 2차 수준 경계는 반대편에 다른 공간이 있는 A 유형과 건물 요소가 있는 B 유형으로 나뉜다(개발 브랜치 원본, 2026-09-25 확인). [사실][^ref-334]

IfcSpace·IfcRelSpaceBoundary 문서에는 공간과 공간을 직접 잇는 연결(인접·통행) 관계가 정의되어 있지 않아, IFC에서 공간 그래프를 얻으려면 공간 경계(2차 A 유형)·문·층 소속 관계로부터 연결을 도출해야 할 것으로 보인다. IFC 전체 관계 엔터티를 대조한 것은 아니므로 부재 확정은 아니다. [추정][^ref-156][^ref-334]

Zhu 외(Automation in Construction 171, 2025)는 IFC를 그래프로 바꾼 IFC-Graph의 의미 정보로 실내 길찾기용 연결 그래프를 만들면서, 층 사이 수직 연결을 위해 사용자 정의 엔터티 IfcRelConnectsSpace를 IFC에 더해 공간–공간·공간–출구·공간–설비 경로 탐색을 보였다. [사실][^ref-343] 수평 연결을 어떤 기존 관계에서 도출했는지와 시험 모델의 세부는 원문 미열람으로 미확인이다.

buildingSMART의 ifcOWL 저장소는 IFC 스키마를 RDF·TTL 형식의 온톨로지로 제공하며, README의 대상 판 목록은 IFC2X3_Final·IFC2X3_TC1·IFC4·IFC4_ADD1·IFC4_ADD2까지이고 IFC 4.3은 목록에 없다(다른 경로의 4.3 판 존재 여부는 미확인, 2026-09-25 확인). [사실][^ref-342]

#### 도시·건물 모델: CityGML 3.0

CityGML 3.0 Part 1 개념 모델(OGC 20-010, 2021 승인)은 공간(AbstractSpace)과 공간 경계(AbstractSpaceBoundary) 개념을 새로 두고, 건물 방을 비점유 공간의 하위 클래스인 BuildingRoom으로, 문·창문을 DoorSurface·WindowSurface 같은 채움 면으로, 가상 경계를 ClosureSurface로 표현하며 건물 층(Storey) 표현을 더했다. [사실][^ref-339][^ref-340]

CityGML 3.0에서 공간 사이 연결 그래프를 얻으려면 IFC처럼 경계·문 표현에서 연결을 도출해야 할 것으로 보이나, 이 부분은 확인된 발견 사항이 없는 이 위키의 추론이다. [추정][^ref-339]

#### 표준 간 대응: ISO 19164:2024

ISO 19164:2024는 건물 실내 위치 기반 응용에 공통으로 필요한 실내 지물(indoor feature)의 핵심 의미 분류와 속성·지물 사이 연관을 정하고 기하·위상보다 의미에 초점을 둔다. 정보성 부속서가 CityGML 3.0 건물 모델·IFC(ISO 16739-1)·IndoorGML과의 클래스 수준 대응을 제시한다는 부분은 검색 요약 기준(원문 미열람)이다. [사실][^ref-158]

#### 링크드 데이터 온톨로지: BOT·Brick

W3C 링크드 빌딩 데이터 커뮤니티 그룹의 건물 위상 온톨로지(Building Topology Ontology, BOT, v0.3.2, 2020-07-31 수정)는 Zone·Site·Building·Storey·Space·Element·Interface 클래스와 containsZone·hasStorey·hasSpace·adjacentZone·intersectsZone·adjacentElement·interfaceOf 같은 관계로 건물의 층·공간·요소 위상을 기술하는 최소 온톨로지다. W3C 권고안이 아닌 커뮤니티 그룹 사양이다. [사실][^ref-336][^ref-337]

BOT에는 문·개구부 전용 클래스가 없고 공간 사이 연결은 adjacentZone·adjacentElement 관계와 일반 개념인 Interface로만 표현되는 것으로 보여, 통행 가능 연결을 담으려면 다른 온톨로지와 결합해야 할 것으로 보인다. [추정][^ref-336]

Brick 온톨로지는 자동화에 관련된 건물 안 위치(건물·층·방)를 brick:Location으로 두고 hasPart·isPartOf 관계로 계층을 짓되, 벽 위치 같은 정확한 기하는 담지 않는 위상 중심 표현을 쓴다(발행일 미확인, 2026-09-25 확인). [사실][^ref-341]

#### 사람 길안내 지도 형식: IMDF

실내 지도 데이터 형식(Indoor Mapping Data Format, IMDF) 1.0.0은 2021-02-23 OGC 커뮤니티 표준이 되었으며, 층(level)을 방·통로·계단실·엘리베이터 같은 공간 단위(unit)로 채우고 문 같은 출입구를 접근성·출입통제 속성을 가진 opening으로, 설비·편의시설을 fixture·kiosk·amenity로, 표시 위치를 anchor로 모델링한다. [사실][^ref-338]

#### 국내 규정

국토교통부 고시 '실내공간정보 구축 작업규정'(2018-03-05 제정판 기준)은 철도역·공항처럼 유동 인구가 많은 시설의 길찾기·시설관리·안전에 쓰는 실내공간정보를 정의하고, 실내공간정보를 원칙적으로 CityGML 2.0 데이터 형식과 IndoorGML 공간 개념으로 제작하도록 한다. [사실][^ref-345] 이후 개정판(2021-12-24 판 링크 확인)의 현행 조문이 같은 원칙을 유지하는지는 미확인이다.

#### 대조 사례: 로봇 쪽 그래프 표현

Open-RMF 건물 지도 메시지는 층(Level)마다 이름·고도·배경 이미지·장소(Place)·문(Door)·주행 그래프 목록(nav_graphs)·벽 그래프를 두고, 그래프(Graph)는 이름·꼭짓점(GraphNode)·간선(GraphEdge)·파라미터로 이루어진다(발행일 미확인, 2026-09-25 확인). [사실][^ref-346][^ref-349]

연계 대상: 로봇 인식 연구의 3D 장면 그래프(Hydra 계열)는 건물·방·장소(주행 가능 자유 공간)·객체·메트릭 메시를 층으로 쌓고 포함·인접 관계를 엣지로 두는 계층 그래프이며, 표준이 아니라 로봇이 센서로 온라인 생성하는 표현이다. [사실][^ref-347] 이 표현은 로봇 자체 지능·제어 쪽 연계 대상이므로 표준 비교의 대조 사례로만 둔다.

#### 공간 그래프 스키마 초안과의 대응

이 위키의 정리로는, 확인한 표준 클래스를 스키마 초안에 대응시키면 공간 노드는 IndoorGML CellSpace·IFC IfcSpace·CityGML BuildingRoom·BOT Space·IMDF unit, 문은 IndoorGML 경계(NavigableBoundary, 1.x의 ConnectionSpace)·IFC 문과 공간 경계 관계·CityGML DoorSurface·IMDF opening, 층은 IfcBuildingStorey·BOT Storey·IMDF level에 대응할 수 있으나, 로봇 충전 위치·작업 스테이션에 대응하는 전용 클래스는 이번에 확인한 표준들에서 찾지 못한 것으로 보인다. [추정][^ref-333][^ref-348][^ref-156][^ref-334][^ref-339][^ref-336][^ref-338][^ref-214] 검증이 승인한 공간 노드·층의 대응 후보와 주제 레이어 개념은 [공간 그래프 스키마 초안](space-graph-schema-draft.md) v0.4에 반영했고, 문의 대응은 IndoorGML 2.0에서 문을 어느 클래스로 표현하는지 확인되지 않아 미해결 질문으로 두었다.

#### 분류 원문 질문과의 관계

> 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]

IndoorGML의 외부 참조 형식으로 공간 셀을 IFC 같은 외부 모델 요소에 이을 수 있을 것으로 보이고 ISO 19164가 IFC·CityGML·IndoorGML 사이 클래스 대응을 주므로 건물 표준 쪽 장소 식별자는 공통 기준이 될 수 있으나, 제조사 로봇 지도 좌표·지도 식별자와의 대응은 이들 표준이 다루지 않아 ROP 쪽 대응 계층이 여전히 필요할 것으로 보인다. [추정][^ref-333][^ref-158][^ref-346] 제조사 지도와 IndoorGML 셀을 대응시킨 공개 사례는 이번 조사에서 찾지 못했다.

## 4. 결론과 남은 불확실성

**결론**
- 공간 연결을 노드–엣지 그래프로 명시하는 실내 공간 표준은 IndoorGML이며, 2.0 Part 1(개념 모델)은 2025-08 발행됐고 Part 2 인코딩은 아직 초안이다. [사실][^ref-331][^ref-333][^ref-157]
- IFC 4.3은 공간·층·공간 경계를 담지만 공간 사이 직접 연결 관계는 확인되지 않아 연결을 도출하거나 확장해야 할 것으로 보인다. [추정][^ref-156][^ref-334][^ref-343]
- 확인한 표준들에는 로봇 충전 위치·작업 스테이션 전용 클래스가 없는 것으로 보여, 운영 시설은 표준 밖 정보로 보완해야 할 것으로 보인다. [추정][^ref-333][^ref-156][^ref-338][^ref-214]
- 건물 표준의 장소 식별자와 제조사 로봇 지도 사이 대응은 표준이 다루지 않아 ROP 쪽 대응 계층이 필요할 것으로 보인다. [추정][^ref-333][^ref-158][^ref-346]
- 공간 그래프 스키마 초안은 v0.3 → v0.4로 올렸다(공간 노드·층의 표준 대응 클래스(후보), 층 확정, 주제 레이어 추가). 문의 표준 대응 클래스와 주제 레이어의 로봇·사람 레이어 구분은 근거가 부족해 반영하지 않았다.

**남은 불확실성**
- 모든 주장이 발행 기관 한 곳(또는 같은 계열)의 자료에 기대며 교차 확인은 0건이다.
- IndoorGML 2.0 Part 1 본문은 원문을 열지 못해 발표문·검색 요약 기준이다. 1.x의 ConnectionSpace·TransitionSpace 구성이 2.0에서 유지되는지는 미확인이다(q2-07).
- IFC 4.3 근거는 개발 브랜치 원본이며 게시판 IFC 4.3 ADD2와 문구가 다를 수 있다. IFC·BOT의 연결 관계·문 클래스 부재는 열람 범위 기준의 관찰이다.
- ISO 19164의 부속서 대응, CityGML 3.0, IMDF, Brick은 원문 미열람이다. IMDF의 amenity·fixture가 충전소를 담을 수 있는지는 미확인이다.
- 실내공간정보 구축 작업규정은 2018 제정판 기준이며, ISO 19164·IndoorGML 2.0의 KS 부합화 여부는 미확인이다([열린 질문](../../open-questions.md)).
- 입력 형식별 정보 항목(q2-02)과 관제 수용 형식(q2-03)은 아직 조사하지 않았고, 표준에 대응시킨 관계(엣지) 유형도 아직 없다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q2-07 | IndoorGML 2.0 Part 1 발행판은 문·엘리베이터·계단 같은 연결과 수직 이동을 NavigableBoundary·TransferSpace 등 어떤 클래스로 표현하며, 1.x 의 ConnectionSpace·TransitionSpace 구성과 무엇이 달라졌는가? (q2-01 에서 파생) | 단계 2. 필요한 데이터와 표준 조사 | f4 (실행 2026-09-25-28) | 열림 |
| q3-05 | IFC 에 공간 사이 수직 연결 관계가 없을 때, IfcRelConnectsSpace 같은 사용자 확장 없이 IfcStair·IfcTransportElement 와 층 소속·공간 경계 관계만으로 층간 연결 엣지를 도출하려면 어떤 규칙이 필요한가? (q2-01 에서 파생) | 단계 3. 구현 가설 설계 | f9 (실행 2026-09-25-28) | 열림 |

## 6. 완료 조건 충족 현황

충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 입력 형식별 정보 항목과 표준·형식 목록이 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)의 "4. 필요한 데이터와 표준" 절에 실림 | 미충족 | 표준 목록(q2-01)은 이번 실행에서 4절의 "공간 그래프를 표현하는 표준" 소절로 실었으나, 입력 형식별 정보 항목(q2-02)과 관제 수용 형식(q2-03)이 없다 | 미충족 · 미승인 |
| 표준과 대응시킨 노드·엣지 유형이 [공간 그래프 스키마 초안](space-graph-schema-draft.md)의 개념·관계 목록 표에 반영됨 | 미충족 | 노드 쪽은 공간 노드·층의 표준 대응 클래스(후보)를 v0.4에 반영했으나 문의 대응은 미해결이고, 관계(엣지) 쪽 표준 대응은 없다 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(완료 조건 미충족 — 입력 형식별 정보 항목(q2-02)·관제 수용 형식(q2-03) 미작성, 엣지 표준 대응 없음; 열린 질문 q2-02·q2-03·q2-04·q2-06)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 확인된 사실은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안"으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 공간 그래프를 표현하는 표준(BIM·IFC, 실내 공간 표준)과 데이터 교환 형식을 본다. 이번 실행은 7. 관련 표준·프레임워크·오픈소스 절에 실내 공간 표준의 발행 상태와 표준 간 대응(ISO 19164 부속서)을 반영하도록 제안했다.
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 분류 원문 10장이 건축 도면 기반 이동 지도의 중심 연구영역으로 두며, BIM·CAD에서 이동 공간을 만들고 층·목적지를 정렬하는 일 자체다. 이번 실행은 7. 관련 표준·프레임워크·오픈소스 절(표준마다 공간 연결을 표현하는 방식, 국내 실내공간정보 구축 작업규정)과 11. 열린 질문 절(국내 표준 부합화)에 반영을 제안했다.
- [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 인식한 문·엘리베이터가 설비·건물 시스템 연동 지점이 된다. 이번 실행의 반영 제안은 없다.

## 8. 출처

[^ref-156]: buildingSMART International, IFC 4.3 documentation — IfcSpace (IFC4.3.x-development), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md, 접근일 2026-09-25
[^ref-157]: OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub), IndoorGML-SWG — README and OGC IndoorGML 2.0 Part 2a – XML Encoding (26-042, Candidate SWG Draft), 미확인, https://github.com/opengeospatial/IndoorGML-SWG, 접근일 2026-09-25
[^ref-158]: ISO, ISO 19164:2024 - Geographic information — Indoor feature model, 2024, https://www.iso.org/standard/83153.html, 접근일 2026-09-25 (원문 미열람)
[^ref-214]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md, 접근일 2026-09-25 (원문 미열람)
[^ref-331]: OGC (Open Geospatial Consortium), OGC IndoorGML 2.0 Part 1 – Conceptual Model (22-045r5), 2025-08, https://docs.ogc.org/is/22-045r5/22-045r5.html, 접근일 2026-09-25 (원문 미열람)
[^ref-332]: OGC (Open Geospatial Consortium), OGC Publishes IndoorGML 2.0 Part 1 Conceptual Model Standard, 2025-08-28, https://www.ogc.org/announcement/ogc-publishes-indoorgml-2-0-part-1-conceptual-model-standard/, 접근일 2026-09-25 (원문 미열람)
[^ref-333]: OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub), OGC IndoorGML 2.0 Part 2b – JSON Encoding (26-043, Candidate SWG Draft v0.5.0), 2026-02-28, https://github.com/opengeospatial/IndoorGML-SWG/blob/master/26-043.html, 접근일 2026-09-25
[^ref-334]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcRelSpaceBoundary (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcRelSpaceBoundary.md, 접근일 2026-09-25
[^ref-335]: ISO, ISO 16739-1:2024 - Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema, 2024, https://www.iso.org/standard/84123.html, 접근일 2026-09-25 (원문 미열람)
[^ref-336]: W3C Linked Building Data Community Group (w3c-lbd-cg GitHub), Building Topology Ontology (BOT) — bot.ttl (version 0.3.2), 2020-07-31, https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl, 접근일 2026-09-25
[^ref-337]: Rasmussen, M. H., Lefrançois, M., Schneider, G. F., & Pauwels, P., BOT: The building topology ontology of the W3C linked building data group, 2020, https://journals.sagepub.com/doi/10.3233/SW-200385, 접근일 2026-09-25 (원문 미열람)
[^ref-338]: OGC (Open Geospatial Consortium) / Apple, Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094, 2021-02, https://docs.ogc.org/cs/20-094/, 접근일 2026-09-25 (원문 미열람)
[^ref-339]: OGC (Open Geospatial Consortium), OGC City Geography Markup Language (CityGML) Part 1: Conceptual Model Standard (20-010), 2021, https://docs.ogc.org/is/20-010/20-010.html, 접근일 2026-09-25 (원문 미열람)
[^ref-340]: PFG(Journal of Photogrammetry, Remote Sensing and Geoinformation Science) 게재 논문 저자(미확인), CityGML 3.0: New Functions Open Up New Applications, 2020, https://link.springer.com/article/10.1007/s41064-020-00095-z, 접근일 2026-09-25 (원문 미열람)
[^ref-341]: Brick Consortium (Brick Schema), Relationships — Brick Ontology Documentation, 미확인, https://docs.brickschema.org/brick/relationships.html, 접근일 2026-09-25 (원문 미열람)
[^ref-342]: buildingSMART (buildingsmart-community GitHub), ifcOWL — README (ifcOWL standard), 미확인, https://github.com/buildingsmart-community/ifcOWL, 접근일 2026-09-25
[^ref-343]: Zhu, J., Wong, M. O., Nisbet, N., Xu, J., Kelly, T., Zlatanova, S., & Brilakis, I., Semantics-based connectivity graph for indoor pathfinding powered by IFC-Graph, 2025, https://www.sciencedirect.com/science/article/pii/S0926580525000597, 접근일 2026-09-25 (원문 미열람)
[^ref-344]: 이기준, 이지영(한국공간정보학회지), 실내공간 표준안 IndoorGML의 개념 및 활용, 2013, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001786322, 접근일 2026-09-25 (원문 미열람)
[^ref-345]: 국토교통부(법제처 국가법령정보센터), 실내공간정보 구축 작업규정, 2018-03-05, https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559, 접근일 2026-09-25 (원문 미열람)
[^ref-346]: Open Robotics (open-rmf), rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg, 미확인, https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg, 접근일 2026-09-25
[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L., Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-25 (원문 미열람)
[^ref-348]: ISPRS International Journal of Geo-Information(MDPI) 게재 논문 저자(미확인), Data Model for IndoorGML Extension to Support Indoor Navigation of People with Mobility Disabilities, 2020, https://www.mdpi.com/2220-9964/9/2/66, 접근일 2026-09-25 (원문 미열람)
[^ref-349]: Open Robotics (open-rmf), rmf_building_map_msgs — rmf_building_map_msgs/msg/Graph.msg, 미확인, https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Graph.msg, 접근일 2026-09-25

## 9. 이력

실행 id `build-2026-09-25`는 확장 아이디어 편입 때의 트랙 시드 생성을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 초안 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-28 | q2-01 | q2-07, q3-05 | v0.3 → v0.4 | 2 |
| 2026-09-25 | build-2026-09-25(트랙 시드, 파이프라인 실행 아님) | 없음 | 시드 q2-01~q2-03(3건, [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [공간 그래프 스키마 초안](space-graph-schema-draft.md)에서 생성) | 1 |
