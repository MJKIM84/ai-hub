---
title: "단계 2. 필요한 데이터와 표준 조사"
type: track-stage
track: floorplan-recognition
stage: 2
related_areas: [28, 6, 10, 27]
tags: [BIM, IFC, IndoorGML, 실내 공간 표준, 지도 형식, CAD 레이어, DXF, VDA 5050, LIF]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-156, ref-157, ref-158, ref-214, ref-331, ref-332, ref-333, ref-334, ref-335, ref-336, ref-337, ref-338, ref-339, ref-340, ref-341, ref-342, ref-343, ref-344, ref-345, ref-346, ref-347, ref-348, ref-349, ref-419, ref-420, ref-421, ref-422, ref-423, ref-424, ref-425, ref-426, ref-427, ref-428, ref-429, ref-430, ref-431, ref-432, ref-433, ref-434, ref-435, ref-436, ref-213, ref-215, ref-063, ref-066, ref-067, ref-069, ref-070, ref-073, ref-074, ref-078, ref-081, ref-084, ref-031, ref-046, ref-079, ref-105, ref-212, ref-227, ref-440, ref-441, ref-442]
last_run: 2026-09-25
version: 4
---

[홈](../../index.md) › 중점 연구 트랙 › [건축 도면 자동 인식](index.md) › 단계 2. 필요한 데이터와 표준 조사

# 단계 2. 필요한 데이터와 표준 조사

> 단계 상태: 진행 중 · 열린 질문: 5건 · 답한 질문: 3건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 도면 입력 형식마다 어떤 공간 정보가 들어 있고, 공간 그래프·층별 지도·공용 자원 목록을 어떤 표준·형식으로 표현하고 교환하는가.

위 문장은 트랙 정의의 "밝힐 것"이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 조사 결과는 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)과 [공간 그래프 스키마 초안](space-graph-schema-draft.md)으로 이어진다.

## 2. 질문 목록

이 단계의 시작 질문 3개(q2-01~q2-03)와 앞선 트랙 실행에서 이 단계로 들어온 후속 질문 5개(q2-04·q2-06·q2-07·q2-08·q2-09)다. q2-01은 사용자 요청의 시작 질문 문구 그대로이고, q2-02·q2-03은 구축자가 이 단계의 밝힐 것에서 정한 시작 질문이다. [가정] 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"(q2-05)는 표에서 빼고 백로그에만 남긴다. 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커를 적는다. 제기 근거 칸에는 finding id(실행 id 병기) 또는 "사용자"만 쓴다.

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q2-01 | 공간 그래프를 표현하는 기존 표준(예: BIM·IFC, 실내 공간 표준)은 무엇이 있는가? | 답함 | 사용자 | 2026-09-25-28 | [답](#q2-01) |
| q2-02 | 도면 입력 형식(벡터 CAD, BIM 모델, 래스터 스캔)마다 벽·문·엘리베이터·계단·충전 위치 정보가 어떻게 들어 있고 무엇이 빠지는가? | 답함 | 사용자 | 2026-09-25-36 | [답](#q2-02) |
| q2-03 | 층별 지도와 공용 자원 목록을 로봇 관제와 ROP가 받아들이는 형식(제조사 지도 형식, 지도 교환 형식)은 무엇이 있는가? | 답함 | 사용자 | 2026-09-25-44 | [답](#q2-03) |
| q2-04 | AI Hub 건축 도면 데이터와 CubiCasa5K 의 클래스 목록에 계단·엘리베이터가 포함되는지, 그리고 상업적 이용 조건은 무엇인가? | 열림 | f17, 실행 2026-09-25-05 | | |
| q2-06 | 로봇 충전소·작업 스테이션처럼 IFC 4.3 표준 유형 값에 없는 운영 시설을 BIM 에 담으려면 사용자 정의 유형·속성 세트로 표현해야 하는가, 이를 정한 IDS·속성 세트 관례나 사례가 있는가? (q1-03 에서 파생) | 열림 | f10, 실행 2026-09-25-19 | | |
| q2-07 | IndoorGML 2.0 Part 1 발행판은 문·엘리베이터·계단 같은 연결과 수직 이동을 NavigableBoundary·TransferSpace 등 어떤 클래스로 표현하며, 1.x 의 ConnectionSpace·TransitionSpace 구성과 무엇이 달라졌는가? (q2-01 에서 파생) | 열림 | f4, 실행 2026-09-25-28 | | |
| q2-08 | 국내 실무 건축 CAD 도면은 KS F 1542·건설CALS 전자도면 작성표준의 레이어 체계를 얼마나 따르며, 그 표준 레이어·심벌 코드에 문·계단·승강기·충전 위치를 구분하는 코드가 있는가? (q2-02 에서 파생) | 열림 | f15, 실행 2026-09-25-36 | | |
| q2-09 | 실무 IFC 모델에서 엘리베이터·문·계단이 IfcBuildingElementProxy 로 내보내지는 경우를 어떻게 찾아 보정하며(IDS 검사, 이름·형상 규칙 등), 그 빈도를 보고한 자료가 있는가? (q2-02 에서 파생) | 열림 | f7, 실행 2026-09-25-36 | | |

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

### q2-02 도면 입력 형식마다 벽·문·엘리베이터·계단·충전 위치 정보가 어떻게 들어 있고 무엇이 빠지는가 {#q2-02}

이 위키의 정리로는, BIM(IFC 4.3) 입력은 벽·문(폭·여닫는 방식)·계단·엘리베이터·층을 유형이 붙은 객체로 담아 세 입력 형식 가운데 정보가 가장 많지만 공간 사이 연결은 도출해야 하고 실무 모델에서는 요소가 범용 프록시로 잘못 분류될 수 있으며, 벡터 CAD는 기하는 담되 요소 의미와 길이 단위가 레이어·블록·텍스트 관례에 기대고, 래스터 스캔은 요소 의미와 축척을 인식으로 복원해야 하며, 충전 위치는 세 형식 모두에서 표준 표현이 확인되지 않은 것으로 보인다. 이 3분 비교를 제시한 단일 출처는 확인하지 못했다. [추정][^ref-419][^ref-420][^ref-421][^ref-432][^ref-425][^ref-426][^ref-433][^ref-435][^ref-214]

이번 실행도 일반 웹 페이지 열람이 막힌 환경에서 이뤄졌다. IFC 4.3 개발 브랜치 원본 5건, 오픈소스 DXF 라이브러리 ezdxf 문서 3건, ArchCAD-400K 프로젝트 페이지만 공식 GitHub 원문으로 열었고, 나머지는 검색 결과 요약 기준이며 각주에 원문 미열람을 표시했다. 교차 확인된 주장은 없다.

#### 입력 형식별 비교

아래 표는 검증된 발견 사항으로 직접 만든 이 위키의 정리이며 출처의 표를 옮긴 것이 아니다. BIM 열의 클래스·속성 이름과 데이터셋 라벨 유무는 출처에서 확인한 사실이고, '(추정)'을 붙인 칸은 이 위키의 추정이다. "미확인"은 이번 실행에서 확인하지 못했다는 뜻이다.

| 요소 | BIM(IFC 4.3) | 벡터 CAD(DXF·DWG) | 래스터 스캔 |
|---|---|---|---|
| 벽 | IfcWall, 개구부는 IfcRelVoidsElement 로 붙는 개구부 요소[^ref-422] | 선·폴리라인, 의미는 레이어 이름 관례에 기댐(추정)[^ref-425] | 기호 모양에서 인식(추정)[^ref-063] |
| 문 | IfcDoor(전체 높이·폭, 여닫는 방식), IfcRelFillsElement 로 벽 개구부를 채움[^ref-419] | 블록 참조·속성 텍스트, A-DOOR 같은 레이어 이름 관례(추정)[^ref-424][^ref-428] | 기호 모양에서 인식(추정), 공개 데이터셋에 출입문 라벨 있음[^ref-074] |
| 엘리베이터 | 운송 요소 유형 값 ELEVATOR[^ref-421][^ref-213] | 레이어 코드 미확인 | 공개 데이터셋 라벨 미확인(추정)[^ref-063][^ref-074] |
| 계단 | IfcStair(계단 구간·참 슬래브·난간으로 분해 가능), 잇는 층 전용 속성 미확인[^ref-420] | 레이어 코드 미확인 | CubiCasa5K·Kratochvila 외 라벨 있음[^ref-063][^ref-078] |
| 층·축척 | IfcBuildingStorey, 층 고도는 속성 세트 사용 권고[^ref-423] | 좌표 값에 단위 없음, 모델 공간 단위는 선택 헤더 $INSUNITS[^ref-426] | 별도 메타데이터나 축척 표기·치수 문자 인식(추정)[^ref-069][^ref-435] |
| 충전 위치 | 확인한 콘센트·전기기기 유형 열거에 충전 설비 값 없음[^ref-214][^ref-215] | 레이어 코드 찾지 못함(추정)[^ref-427][^ref-428] | 공개 데이터셋 라벨 없음(추정)[^ref-063][^ref-073] |
| 주의할 점 | 실무 모델의 프록시 오분류 가능성[^ref-432], 공간 연결은 도출 필요(추정) | 표준을 따르지 않은 도면은 의미·축척 복원 필요(추정)[^ref-433] | 의미·축척 모두 인식으로 복원(추정)[^ref-435] |

#### BIM 입력: IFC 4.3

IFC 4.3 문서(개발 브랜치 원본, 2026-09-25 확인)는 문(IfcDoor)을 사람·물품·차량의 통제된 출입에 주로 쓰는 건축 요소로 정의하고, 전체 높이·폭(OverallHeight·OverallWidth)과 여닫는 방식(OperationType) 속성을 두며, 문은 IfcRelFillsElement 관계로 벽의 개구부(IfcOpeningElement)를 채운다. 높이·폭을 생략하면 관련 개구부의 형상에서 값을 얻는다. [사실][^ref-419]

벽(IfcWall)은 공간을 둘러싸거나 나누는 수직 구조로 정의되고, 문·창문 같은 개구부는 IfcRelVoidsElement 로 벽에 붙는 개구부 요소로 표현되며, 벽은 층(기본)·건물·대지(외부)에 공간적으로 포함된다(개발 브랜치 원본, 2026-09-25 확인). [사실][^ref-422]

계단(IfcStair)은 다른 높이의 층 사이를 걸어서 오가게 하는 수직 통로로 정의되고, 계단 구간(IfcStairFlight)·참 슬래브(IfcSlab LANDING)·난간(IfcRailing)으로 분해할 수 있으며, 공간 컨테이너는 기본이 IfcBuildingStorey, 층에 할당할 수 없으면 IfcBuilding, 외부는 IfcSite 이다(개발 브랜치 원본, 2026-09-25 확인). [사실][^ref-420]

엘리베이터를 담는 운송 요소 클래스(IfcTransportElement)[^ref-213]의 유형 열거(IfcTransportElementTypeEnum)는 ELEVATOR(사람·물품을 수직으로 옮기는 승강기)와 ESCALATOR·MOVINGWALKWAY·CRANEWAY·HAULINGGEAR·LIFTINGGEAR, 그리고 USERDEFINED·NOTDEFINED 값을 둔다(개발 브랜치 원본, 2026-09-25 확인). [사실][^ref-421]

층(IfcBuildingStorey)은 수직으로 경계 지어진 공간들의 (거의) 수평 집합으로 정의되며, 층 기준 고도 속성 Elevation 은 IFC4.3.0.0 에서 폐기 예정(deprecated)으로 두고 속성 세트(Pset_BuildingStoreyCommon)의 ElevationOfSSLRelative 또는 ElevationOfFFLRelative 를 쓰도록 권한다. [사실][^ref-423]

이 위키의 정리로는, IFC 입력에는 벽·문·계단·엘리베이터·층이 유형 객체와 층 포함 관계로 들어 있지만, 문이 어느 두 공간을 잇는지는 문→개구부→벽의 채움·보이드 관계와 공간 경계(q2-01 에서 다룬 IfcRelSpaceBoundary)를 거쳐 도출해야 하고, 계단·엘리베이터가 잇는 층도 직접 속성이 아니라 포함 관계·형상에서 도출해야 할 것으로 보인다. 계단이 잇는 두 층을 가리키는 전용 속성은 이번 열람 범위에서 확인하지 못했고, IFC 전체 관계 엔터티를 대조한 것은 아니어서 부재 확정은 아니다. [추정][^ref-419][^ref-422][^ref-420][^ref-334][^ref-156]

Noardo 외(Applied Sciences 11(5), 2021)는 실무자가 만든 IFC 모델을 표준 정의와 대조해 점검하면서, IFC 가 예정하지 않은 요소를 담는 범용 요소 IfcBuildingElementProxy 가 유효한 IFC 엔터티가 있는 요소의 대체로 잘못 쓰일 수 있다고 보고 모델마다 그 사용을 점검했다. [사실][^ref-432] 대체 비율은 원문을 열지 못해 미확인이다.

따라서 엘리베이터·문·계단이 IfcTransportElement(ELEVATOR)·IfcDoor·IfcStair 로 담긴다는 것은 스키마가 허용하는 가능성이고, 실무 모델에서는 이들이 프록시로 내보내져 유형 정보가 빠질 수 있어 인식 전에 클래스 사용을 점검해야 할 것으로 보인다. 실제로 프록시로 내보낸 사례·비율은 확인하지 못했다. [추정][^ref-432][^ref-421][^ref-419]

연계 대상: Vega-Torres 외는 BIM(IFC)에서 자동 생성한 2D 점유 격자 지도가 구조 요소만 담고, 가구·잡동사니와 설계–시공 편차 때문에 BIM 이 현실을 정확히 나타낸다는 가정이 성립하지 않는다고 지적했다. [사실][^ref-081] BIM 기반 지도·위치추정은 분류 원문 9장의 로봇 자체 지능·제어 쪽 연계 대상이므로, 여기서는 BIM 입력이 담지 못하는 정보(가구·설계–시공 편차)의 근거로만 쓴다.

국내에서는 국토교통부가 2022-07 BIM 성과품의 작성·납품과 활용의 방법·절차를 제시하는 '건설산업 BIM 시행지침'을 발표했다. [사실][^ref-436]

#### 벡터 CAD 입력: DXF·DWG

아래 DXF 형식 설명은 Autodesk 의 공식 DXF 참조가 아니라 오픈소스 DXF 라이브러리 ezdxf 의 문서 기준이다(발행일 미확인, 2026-09-25 확인).

ezdxf 문서는 블록(block)을 여러 번 배치할 수 있는 엔터티 묶음으로, 각 배치를 위치·회전·축척을 가진 블록 참조(INSERT 엔터티)로 설명하며, 블록 참조에 태그가 붙은 속성 텍스트(ATTRIB)를 달아 메타데이터를 실을 수 있다고 설명한다. [사실][^ref-424]

같은 문서는 레이어를 객체를 논리적 묶음으로 나누고 보이기·색상·선 종류를 제어하는 수단으로 설명하며, 벽·가구·주석 같은 레이어 구분은 사용 예로만 들 뿐 레이어 이름의 의미를 형식이 정하지는 않는다(열람 범위 기준). [사실][^ref-425]

또 ezdxf 문서는 DXF 의 길이·좌표 값에 단위 정보가 붙지 않고, 모델 공간 단위는 선택 헤더 변수 $INSUNITS 로 주어지며, $MEASUREMENT 는 미터법·야드파운드법 선 종류·해치 패턴 선택에만 관계한다고 설명한다. [사실][^ref-426]

레이어 이름 표준으로, ISO 13567-1:2017 은 CAD 파일의 레이어 구조화 원칙을 정하고 레이어 이름을 책임 주체(설계 분야, 2자)·요소(분류 체계 코드, 6자)·표현 등 고정 길이 필드로 구성하게 한다. [사실][^ref-427]

미국 국가 CAD 표준(National CAD Standard, NCS)이 채택한 AIA CAD 레이어 형식은 하이픈으로 나눈 필드(분야 지정자·주 그룹 등)로 레이어 이름을 짓고, 건축 분야의 문 레이어를 A-DOOR, 벽 레이어를 A-WALL 같은 이름으로 둔다(NCS V5 문서 기준이며, 2026-09-25 확인 시점에 V6 판 문서 ncs6_clg_lnf.pdf 가 있다). [사실][^ref-428] 계단·승강기 레이어 코드는 확인하지 못했다.

국내에서는 건설CALS/EC 전자도면 작성표준이 전자도면의 도면분류·파일명·선·색상·레이어·심벌을 정하며, V1.0 은 2004-08, V1.1(KCCS-0001-2006)은 2006-12-26 한국건설기술연구원장 공고로 나왔다. [사실][^ref-430] 이와 별도로 국가표준 KS F 1542 'CAD 도면 작성을 위한 레이어 원칙과 기준'이 있다(2020-12-21 확인). [사실][^ref-429] 두 문서 사이의 관계와, 두 문서가 문·계단·승강기·충전 위치를 구분하는 레이어 코드를 두는지는 원문을 열지 못해 미확인이다.

신동철(대한건축학회 논문집 계획계 25(11), 2009-11)은 국내 건축 표준 CAD 레이어의 실무 적용 실태를 분석했으나, 분석 결과(표준 레이어 사용 비율 등)는 이번에 확인하지 못했다. [사실][^ref-431]

ArchCAD-400K 프로젝트 페이지는 체계적으로 보관된 CAD 도면의 레이어·블록 계층을 이용해 구조 인식형 자동 라벨링을 하고, 전문가 보정을 래스터가 아닌 벡터 공간에서 직접 한다고 설명한다(발행일 미확인, 2026-09-25 확인). [사실][^ref-434] 단계 1에서 다룬 FloorPlanCAD 는 CAD 선 요소에서 문·창문 같은 기호의 인스턴스와 벽 같은 영역의 의미를 함께 판별하는 파놉틱 심볼 스포팅 과제를 정의했다. [사실][^ref-067][^ref-066]

2026-07-14 공개된 프리프린트(arXiv 2607.12678)는 CAD 평면도의 텍스트 주석이 일반 자연어도 단순 보조 라벨도 아닌 복잡한 구문과 다층 의미를 가진다고 보고, 주석의 유형·속성을 함께 인코딩해 선 요소 단위 심볼 스포팅에 결합하는 다중 모달 방법을 제안했다. [사실][^ref-433] 단계 1에서 다룬 osmAG-from-cad 는 DXF 를 기본 입력으로 받고 DWG 는 외부 변환기를 거쳐야 하며, 문자 기반 방 이름 붙이기는 기본으로 꺼져 있다. [사실][^ref-084]

이 위키의 정리로는, 벡터 CAD 입력에서 벽·문·계단·엘리베이터는 선·폴리라인·블록 참조·텍스트로 들어 있고 그 의미는 형식이 아니라 프로젝트의 레이어·블록 이름 관례(ISO 13567, NCS, KS F 1542 같은 명명 표준을 따를 수도 있음)와 텍스트 주석에서 읽어야 하며, 길이 단위도 선택 헤더에 기대므로, 표준을 따르지 않은 도면에서는 요소 의미와 축척을 인식으로 복원해야 할 것으로 보인다. 국내 실무 도면이 표준 레이어를 얼마나 따르는지는 미확인이다. [추정][^ref-424][^ref-425][^ref-426][^ref-427][^ref-428][^ref-429][^ref-433][^ref-434]

#### 래스터 스캔 입력

MLSTRUCT-FP 는 이미지별 축척(px/m) 메타데이터를 주고, Raster-to-Graph 는 512×512 로 정규화한 이미지 좌표를 쓴다. [사실][^ref-069][^ref-070] 이 두 사례로 보면 래스터 입력에서는 축척을 별도 메타데이터나 도면 안 축척 표기·치수 문자 인식으로 얻어야 할 것으로 보인다. [추정][^ref-069][^ref-070]

래스터 주택 평면 인식·3D 재구성 연구(Buildings 15(7), 2025)는 YOLOv8 과 Shi–Tomasi 모서리 검출로 치수선 끝점을 찾고 사전학습 다중 모달 문자 인식(OFA-OCR)으로 치수 숫자를 읽어 축척을 계산했으며, 축척 계산 정확도가 95%를 넘었다고 보고했다(저자 보고 단일 출처, 데이터 조건 미확인). [사실][^ref-435]

단계 1에서 확인한 공개 래스터 평면도 자료의 라벨에는 CubiCasa5K 와 Kratochvila 외의 계단·난간, AI Hub 건축 도면 데이터의 출입문·창호·벽체·도면 문자가 있다. [사실][^ref-063][^ref-078][^ref-074] 엘리베이터 라벨은 이들 자료에서 확인되지 않았으나, 전체 클래스 목록을 열람하지 못해 부재 확정은 아니다(q2-04). [추정][^ref-063][^ref-078][^ref-074]

이 위키의 정리로는, 래스터 스캔 입력에는 레이어·객체·단위가 없어 벽·문·계단은 기호 모양에서, 축척은 축척 표기·치수 문자에서, 방·층 이름은 도면 문자 인식에서 복원해야 하고, 엘리베이터 라벨이 확인된 공개 래스터 데이터셋이 없어 엘리베이터 인식은 학습 자료부터 부족할 것으로 보인다. 스캔 품질(잡음·기울기)의 영향은 조사하지 않았다. [추정][^ref-063][^ref-069][^ref-070][^ref-074][^ref-435]

#### 충전 위치

BIM 쪽에서는 앞선 실행에서 확인한 대로 IFC 4.3 콘센트·전기기기 유형 열거(개발 브랜치 기준)에 차량·로봇 충전 설비를 뜻하는 값이 없다. [사실][^ref-214][^ref-215] 이 위키의 정리로는, 확인한 CAD 레이어 표준 자료에서도 충전 위치 레이어 코드를 찾지 못했고 공개 평면도 데이터셋에도 충전 위치 라벨이 없어, 세 입력 형식 모두에서 충전 위치는 도면 밖 정보로 보완해야 할 것으로 보인다. 레이어 표준 원문을 열지 못해 코드 부재는 확정이 아니다. [추정][^ref-214][^ref-215][^ref-427][^ref-428][^ref-063][^ref-073]

#### 분류 원문 질문과의 관계

이 위키의 정리로는, 앞 소제목에서 인용한 분류 원문 질문의 '3층 출하 대기장' 같은 장소 이름과 층을 도면에서 얻을 때, BIM 입력은 공간 이름과 층 소속을 객체 속성·관계로 주지만 벡터 CAD·래스터 입력에서는 장소 이름이 텍스트 주석으로만 있어 문자 인식·텍스트 해석으로 공간에 붙여야 하고, 어느 형식이든 제조사 로봇 지도 식별자와의 대응은 도면 밖의 ROP 쪽 대응 계층이 맡아야 할 것으로 보인다. 물류센터 도면에 구역 이름이 어떻게 적히는지는 확인하지 못했다. [추정][^ref-156][^ref-423][^ref-433][^ref-074]

레이어·블록 기반 자동 라벨링, 텍스트 결합 심볼 스포팅, 문자 인식 기반 축척 계산은 분류 원문 8장의 교차 규칙(도면 해석은 6. 지도·공간·위치 모델에 적용)에 해당하는 AI 방법이어서, [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)과 [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) 양쪽에 반영을 제안했다(7절).

### q2-03 층별 지도와 공용 자원 목록을 로봇 관제와 ROP가 받아들이는 형식은 무엇이 있는가 {#q2-03}

이 위키의 분류로는, 이번에 확인한 수용 형식은 (1) 이미지와 축척·원점 메타데이터로 된 격자 지도(Nav2 map_server YAML, 제조사 관제의 PNG 평면도), (2) 노드·엣지·스테이션으로 된 레이아웃 교환 형식(VDMA LIF, Open-RMF building.yaml과 주행 그래프 파일), (3) 지도에 붙는 다각형 구역 집합(VDA 5050 zoneSet)으로 나뉘는 것으로 보이고, 충전소·승강기·스테이션 같은 공용 자원은 별도 목록 형식 없이 경유점 속성·스테이션·경로망 설정 안에 흩어져 표현되는 것으로 보인다. 이 3분류를 제시한 단일 출처는 확인하지 못했고, 공용 자원 목록 전용 교환 형식은 이번 검색 범위(검색 2회)에서 찾지 못했다(부재 확인 아님). [추정][^ref-440][^ref-441][^ref-046][^ref-031][^ref-442][^ref-079][^ref-227] VDA 5050 주문은 지도·레이아웃 교환 형식이 아니라 주문마다 보내는 주행 구간 그래프이므로 레이아웃 교환 형식과 같은 칸에 두지 않았다. [추정][^ref-031]

실행 2026-09-25-44도 일반 웹 페이지 열람이 막힌 환경에서 이뤄졌다. VDA 5050 3.0.0 명세는 입력 원문 텍스트로, VDA 5050 구역 집합 스키마·Nav2 지도 서버 README·Open-RMF traffic-editor README 는 공식 GitHub 원문으로 읽었고, VDMA LIF 공식 README 는 검증 단계에서 원문을 열어 확인했다. Open-RMF 경유점 속성·플릿 어댑터 설정·건물 지도 메시지, 제3자 LIF 스키마, MiR 문서는 앞선 실행에서 검증을 통과한 주장을 다시 쓴 것이며 각주에 원문 미열람을 표시했다. 형식마다 발행 주체 한 곳(또는 같은 계열)의 자료에 기대며 교차 확인된 주장은 없다.

#### 수용 형식 비교

아래 표는 검증된 발견 사항으로 직접 만든 이 위키의 구성이며 출처의 표를 옮긴 것이 아니다. 갈래 구분은 이 위키의 분류([추정])이고, 각 칸의 필드·절차 이름은 근거 열 출처에서 확인한 것이다. "미확인"은 이번 실행에서 확인하지 못했다는 뜻이다.

| 갈래 | 형식 | 담는 것 | 층·판 식별 | 공용 자원 표현 | 근거 |
|---|---|---|---|---|---|
| 격자 지도 | Nav2 지도 서버(map_server) | YAML 메타데이터와 이미지 한 쌍의 점유 격자 지도, 로봇 쪽 내비게이션 스택의 입력 | 미확인 | 미확인 | [^ref-440] |
| 격자 지도 | MiR Fleet Enterprise | CAD 평면도를 PNG로 올린 지도(벤더 주장) | 미확인 | 미확인 | [^ref-227] |
| 레이아웃 교환 | Open-RMF traffic-editor .building.yaml | 편집 결과 파일, building_map_generator 로 주행 그래프 파일 생성 | 층 이름 | 경유점 속성(충전소·주차·대기·도킹·디스펜서·인제스터) | [^ref-441][^ref-346][^ref-079] |
| 레이아웃 교환 | VDMA LIF | 엣지·노드·스테이션 주행 레이아웃 | 층(layoutLevelId)·판(layoutVersion), 제3자 스키마 기준 | 스테이션(유형 필드 없음, 제3자 스키마 기준) | [^ref-046][^ref-212] |
| 구역 집합 | VDA 5050 zoneSet | 지도에 붙는 꼭짓점 3개 이상의 다각형 구역과 10종 유형 | mapId | 해당 없음 | [^ref-442][^ref-031] |
| 지도 배포 | VDA 5050 지도 배포 동작 | 식별·배포·활성화·삭제 절차, 파일 내용 형식은 6.3절 범위에서 정해지지 않은 것으로 보임(추정) | mapId·mapVersion | 경로망 설정(명세 범위 밖) | [^ref-031] |

#### VDA 5050 3.0.0: 지도 식별·배포와 구역 집합

[VDA 5050](../../glossary/vda-5050.md) 3.0.0 명세에서 지도는 지도 식별자(mapId)와 지도 판(mapVersion)의 조합으로 식별된다. 관제는 지도 서버에 둔 지도 파일을 즉시 동작 downloadMap(내려받을 주소 mapDownloadLink 포함)으로 로봇이 받아 가게 하고, enableMap·deleteMap 동작으로 활성화·삭제하며, 한 번의 전송은 파일 하나로 하도록 권한다(발행일 미확인, 2026-09-25 확인). [사실][^ref-031]

구역 집합(zoneSet)은 구역 집합 식별자(zoneSetId)·지도 식별자(mapId)·구역 목록(zones)을 갖고, 각 구역은 구역 식별자(zoneId), 10종 구역 유형(BLOCKED·LINE_GUIDED·RELEASE·COORDINATED_REPLANNING·SPEED_LIMIT·ACTION·PRIORITY·PENALTY·DIRECTED·BIDIRECTED), 3개 이상의 꼭짓점과 유형별 파라미터로 표현되며, zoneSet 토픽이나 downloadZoneSet 동작으로 전달된다. 한 지도에 활성 구역 집합은 하나다. 두 출처는 같은 발행 주체라 독립 교차 확인이 아니다. [사실][^ref-442][^ref-031] 구역 유형에는 통행 금지뿐 아니라 우선·벌점·방향 유형도 있고, RELEASE 유형은 용어집의 [해제 구역](../../glossary/release-zone.md)에 해당한다.

명세는 도입 단계에서 경로를 LIF 로 관제에 가져올 수 있다고 적는다. 또 경로망 설정에서 적재·하역 스테이션, 충전 스테이션, 주변 설비(게이트·승강기·차단기), 대기 위치, 버퍼 스테이션을 정의한다고 하면서, 이 경로·경로망 설정 자체는 명세의 범위가 아니라고 밝힌다. [사실][^ref-031]

LIF 의 판·발행일은 출처마다 다르다. VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용하고, LIF 공식 README 는 1.0.0 판을 2023-09 로 적는다. [사실][^ref-031][^ref-046] 한쪽을 고르지 않고 [열린 질문](../../open-questions.md) oq-025 에 둔다.

이번에 읽은 명세 범위(6.3절)에서는 지도 파일 자체의 내용 형식이 정해지지 않은 것으로 보여, 로봇이 내려받는 지도는 제조사별 형식일 수 있고 ROP 가 형식 변환을 따로 맡아야 할 것으로 보인다. 6.3절은 좌표계·식별·배포 절차만 다루며, 명세 전체를 대조하지 않았으므로 부재 확정은 아니다. [추정][^ref-031]

#### 레이아웃 교환 형식: VDMA LIF

[레이아웃 교환 형식](../../glossary/layout-interchange-format.md)(LIF)을 통합사업자가 엣지·노드·스테이션 레이아웃을 제3자 관제에 넘기는 교환 형식으로 정의한 공식 README 의 내용과, 제3자 JSON 스키마의 층·판·스테이션 필드(스테이션 유형 필드 없음)는 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)의 4절 '레이아웃 교환 형식(VDMA LIF)' 소절에 이미 실린 문장을 따른다. [사실][^ref-046][^ref-212]

#### Open-RMF: building.yaml·주행 그래프·경유점 속성

Open-RMF traffic-editor 는 편집 결과를 .building.yaml 파일로 저장하고, rmf_building_map_tools 의 building_map_generator 가 이 파일에서 nav 인자로 주행 경로 그래프 파일을, gazebo·ignition 인자로 시뮬레이션 월드를 생성한다(발행일 미확인, 2026-09-25 확인). [사실][^ref-441] 여기서 시뮬레이션 월드 생성은 형식 설명으로만 다루며, 시뮬레이션 활용은 [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)의 주제다.

건물 지도 메시지의 층·그래프 구성은 위 q2-01 의 '대조 사례: 로봇 쪽 그래프 표현'에 있다.[^ref-346][^ref-349] 충전소·주차 위치·대기 지점·도킹 이름·픽업 디스펜서·하역 인제스터를 traffic-editor 경유점 속성으로 사람이 입력하고, 플릿 어댑터 설정이 층별 RMF 지도 좌표와 로봇 지도 좌표의 대응점(reference_coordinates)을 적게 한다는 내용은 [단계 1의 q1-03 답](stage-1-prior-work-and-products.md#q1-03)과 아이디어 페이지에 이미 실린 문장을 따른다. [사실][^ref-079][^ref-105]

#### 격자 지도: Nav2 지도 서버와 제조사 관제

연계 대상: ROS 2 내비게이션 스택 Nav2 의 지도 서버(map_server)는 ROS 1 내비게이션과 같은 YAML 메타데이터(image, resolution, origin, negate, occupied_thresh, free_thresh)와 이미지 파일 한 쌍으로 된 [점유 격자 지도](../../glossary/occupancy-grid-map.md)(nav_msgs/msg/OccupancyGrid)를 읽는다(발행일 미확인, 2026-09-25 확인). [사실][^ref-440] 이는 로봇 쪽 내비게이션 스택의 입력 형식이며, 격자 지도 생성과 그 지도로 하는 위치추정은 분류 원문 9장의 로봇 자체 지능·제어 쪽 연계 대상이다.

MiR Fleet Enterprise 문서(1.2판, 2025-01, 유통사 게재본)가 CAD 평면도를 PNG 로 올려 지도로 쓰고 축척을 1m 당 20픽셀로 요구한다는 내용은 아이디어 페이지 3절 제품 사례에 이미 실린 문장을 따른다. [추정] 벤더 주장[^ref-227] 다른 관제 제품(ABB·KUKA·OTTO 등)의 지도 가져오기 형식과 국내 관제 제품의 지도 형식은 이번에 공개 자료로 확인하지 못했다.

#### 분류 원문 질문과의 관계

이 위키의 추론으로는, 확인한 형식들이 층을 VDA 5050 mapId·LIF layoutLevelId·Open-RMF 층 이름으로, 장소를 스테이션 이름·경유점 이름으로 각각 따로 표현하므로, 도면에서 만든 공간 그래프를 관제에 넘길 때 형식마다 층·장소 식별자를 대응시키는 변환 계층이 ROP 쪽에 필요할 것으로 보인다. 형식 사이 식별자 대응 규칙을 정한 출처는 찾지 못했다. [추정][^ref-031][^ref-212][^ref-346][^ref-079] 이 방향은 [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) 3절의 대응 계층 문장과 같고, [열린 질문](../../open-questions.md) oq-027(공통 좌표계와 mapId·Open-RMF 층 이름 대응)·oq-045(지도 층 이름과 승강기 층 이름 대응)와 이어진다.

연계 대상: 격자 지도 생성과 위치추정은 로봇 자체 지능·제어 쪽이고, 이종 제조사를 연결하는 ROP 는 도면 기반 결과를 레이아웃·구역·공용 자원 설정으로 변환·전달하고 지도 판을 관리하는 쪽을 맡는 경계가 될 것으로 보인다. 이는 [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) 9절의 경계 표와 같은 취지다. [추정][^ref-440][^ref-031][^ref-212]

## 4. 결론과 남은 불확실성

**결론**
- 공간 연결을 노드–엣지 그래프로 명시하는 실내 공간 표준은 IndoorGML이며, 2.0 Part 1(개념 모델)은 2025-08 발행됐고 Part 2 인코딩은 아직 초안이다. [사실][^ref-331][^ref-333][^ref-157]
- IFC 4.3은 공간·층·공간 경계를 담지만 공간 사이 직접 연결 관계는 확인되지 않아 연결을 도출하거나 확장해야 할 것으로 보인다. [추정][^ref-156][^ref-334][^ref-343]
- 확인한 표준들에는 로봇 충전 위치·작업 스테이션 전용 클래스가 없는 것으로 보여, 운영 시설은 표준 밖 정보로 보완해야 할 것으로 보인다. [추정][^ref-333][^ref-156][^ref-338][^ref-214]
- 건물 표준의 장소 식별자와 제조사 로봇 지도 사이 대응은 표준이 다루지 않아 ROP 쪽 대응 계층이 필요할 것으로 보인다. [추정][^ref-333][^ref-158][^ref-346]
- BIM(IFC 4.3) 입력은 벽·문·계단·엘리베이터·층을 유형 객체로 담아 세 입력 형식 가운데 정보가 가장 많지만, 공간 사이 연결은 도출해야 하고 실무 모델에서는 요소가 프록시로 잘못 분류될 수 있을 것으로 보인다. [추정][^ref-419][^ref-420][^ref-421][^ref-432]
- 벡터 CAD 입력의 요소 의미와 길이 단위는 형식이 아니라 레이어·블록·텍스트 관례와 선택 헤더에 기대고, 래스터 스캔 입력은 요소 의미와 축척을 인식으로 복원해야 할 것으로 보인다. [추정][^ref-425][^ref-426][^ref-433][^ref-435]
- 충전 위치는 세 입력 형식 모두에서 표준 표현이 확인되지 않아 도면 밖 정보로 보완해야 할 것으로 보인다. [추정][^ref-214][^ref-427][^ref-428][^ref-063]
- VDA 5050 3.0.0 은 지도를 mapId·mapVersion 으로 식별하고 관제가 downloadMap·enableMap·deleteMap 동작으로 배포·활성화·삭제하며, 지도에 붙는 구역 집합을 10종 유형의 다각형 구역으로 전달한다. [사실][^ref-031][^ref-442]
- 관제·ROP 수용 형식은 격자 지도, 레이아웃 교환 형식, 구역 집합의 세 갈래로 나뉘고 공용 자원은 전용 목록 형식 없이 경유점 속성·스테이션·경로망 설정에 흩어져 있는 것으로 보인다(이 위키의 분류). [추정][^ref-440][^ref-441][^ref-046][^ref-442][^ref-079]
- 공간 그래프 스키마 초안은 실행 2026-09-25-28에서 v0.3 → v0.4로 올렸다(공간 노드·층의 표준 대응 클래스(후보), 층 확정, 주제 레이어 추가). 문의 표준 대응 클래스와 주제 레이어의 로봇·사람 레이어 구분은 근거가 부족해 반영하지 않았다.
- 실행 2026-09-25-36에서 스키마 초안을 v0.4 → v0.5로 올렸다(문·계단의 BIM 대응 클래스, 엘리베이터 유형 값 ELEVATOR 확정, 평면도의 길이 단위·축척 정보 속성). 계단이 잇는 층의 도출 규칙과 래스터 평면도의 축척 복원 방식은 근거가 추정이어서 반영하지 않고 미해결 질문으로 두었다.
- 실행 2026-09-25-44에서 스키마 초안을 v0.5 → v0.6으로 올렸다(층별 지도의 교환 형식(후보) 속성). 지도 판(mapVersion·layoutVersion) 속성은 기존 지도 버전 질문을 근거 없이 결정하게 되어, VDA 5050 구역 집합을 공간 그래프 개념으로 두는 제안은 이름·범위가 정해지지 않아 반영하지 않고 미해결 질문으로 두었다.

**남은 불확실성**
- 모든 주장이 발행 기관 한 곳(또는 같은 계열)의 자료에 기대며 교차 확인은 0건이다.
- IndoorGML 2.0 Part 1 본문은 원문을 열지 못해 발표문·검색 요약 기준이다. 1.x의 ConnectionSpace·TransitionSpace 구성이 2.0에서 유지되는지는 미확인이다(q2-07).
- IFC 4.3 근거는 개발 브랜치 원본이며 게시판 IFC 4.3 ADD2와 문구가 다를 수 있다. IFC·BOT의 연결 관계·문 클래스 부재와 계단이 잇는 층 전용 속성 부재는 열람 범위 기준의 관찰이다.
- 실무 IFC 모델에서 요소가 IfcBuildingElementProxy 로 대체되는 비율과 엘리베이터가 프록시로 내보내진 사례는 원문 미열람으로 미확인이다(q2-09).
- DXF 형식 설명(블록·레이어·단위)은 Autodesk 공식 참조가 아닌 ezdxf 문서 기준이다.
- ISO 13567·NCS·KS F 1542·건설CALS 전자도면 작성표준은 원문 미열람이어서 문·계단·승강기·충전 위치 레이어 코드의 유무와 국내 실무 준수율을 확인하지 못했다(q2-08). NCS 근거는 V5 문서이며 V6 판이 있다.
- 래스터 축척 계산 정확도(95% 초과)는 저자 보고 단일 출처이고, 공개 래스터 데이터셋의 엘리베이터 라벨 부재는 확정이 아니다(q2-04).
- ISO 19164의 부속서 대응, CityGML 3.0, IMDF, Brick은 원문 미열람이다. IMDF의 amenity·fixture가 충전소를 담을 수 있는지는 미확인이다.
- 실내공간정보 구축 작업규정은 2018 제정판 기준이며, ISO 19164·IndoorGML 2.0의 KS 부합화 여부는 미확인이다([열린 질문](../../open-questions.md)).
- VDA 5050 이 지도 파일의 내용 형식을 정하지 않는다는 관찰은 명세 6.3절 범위 기준이고, 수용 형식 3분류와 공용 자원 목록 전용 형식 부재는 검색 2회 범위의 추론이다(부재 확인 아님).
- 제조사 관제 제품 쪽 근거는 MiR 문서(유통사 게재본, 원문 미열람)의 벤더 주장 1건뿐이며, 다른 관제 제품과 국내 관제 제품의 지도 가져오기 형식은 확인하지 못했다.
- LIF 판·발행일은 VDA 5050 의 인용(2024-03)과 LIF README(2023-09)가 달라 열린 질문 oq-025 로 남는다.
- Open-RMF 경유점 속성·플릿 어댑터 설정·건물 지도 메시지, 제3자 LIF 스키마는 이번 실행에서 다시 열지 않은 재인용이다.
- 표준에 대응시킨 관계(엣지) 유형은 아직 스키마 초안에 없다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q2-07 | IndoorGML 2.0 Part 1 발행판은 문·엘리베이터·계단 같은 연결과 수직 이동을 NavigableBoundary·TransferSpace 등 어떤 클래스로 표현하며, 1.x 의 ConnectionSpace·TransitionSpace 구성과 무엇이 달라졌는가? (q2-01 에서 파생) | 단계 2. 필요한 데이터와 표준 조사 | f4 (실행 2026-09-25-28) | 열림 |
| q3-05 | IFC 에 공간 사이 수직 연결 관계가 없을 때, IfcRelConnectsSpace 같은 사용자 확장 없이 IfcStair·IfcTransportElement 와 층 소속·공간 경계 관계만으로 층간 연결 엣지를 도출하려면 어떤 규칙이 필요한가? (q2-01 에서 파생) | 단계 3. 구현 가설 설계 | f9 (실행 2026-09-25-28) | 열림 |
| q2-08 | 국내 실무 건축 CAD 도면은 KS F 1542·건설CALS 전자도면 작성표준의 레이어 체계를 얼마나 따르며, 그 표준 레이어·심벌 코드에 문·계단·승강기·충전 위치를 구분하는 코드가 있는가? (q2-02 에서 파생) | 단계 2. 필요한 데이터와 표준 조사 | f15 (실행 2026-09-25-36) | 열림 |
| q2-09 | 실무 IFC 모델에서 엘리베이터·문·계단이 IfcBuildingElementProxy 로 내보내지는 경우를 어떻게 찾아 보정하며(IDS 검사, 이름·형상 규칙 등), 그 빈도를 보고한 자료가 있는가? (q2-02 에서 파생) | 단계 2. 필요한 데이터와 표준 조사 | f7 (실행 2026-09-25-36) | 열림 |
| q4-07 | VDA 5050 downloadMap 으로 배포하는 지도 파일의 내용 형식이 제조사마다 다를 때, 도면에서 만든 층별 지도를 제조사별 지도 파일로 변환·배포하고 mapVersion 을 맞추는 책임과 절차를 ROP 가 어떻게 둘 수 있는가? (q2-03 에서 파생) | 단계 4. 지도 변환 보정과 현장 정합 | f4 (실행 2026-09-25-44) | 열림 |
| q3-06 | 충전소·승강기·작업 스테이션 같은 공용 자원 목록을 관제 사이에 교환하는 전용 형식이 없을 때, LIF 스테이션·Open-RMF 경유점 속성·VDA 5050 경로망 설정 가운데 무엇을 기준으로 공용 자원 목록을 내보낼 수 있는가? (q2-03 에서 파생) | 단계 3. 구현 가설 설계 | f12 (실행 2026-09-25-44) | 열림 |

벡터 CAD 도면의 레이어·블록 이름과 텍스트 주석을 선 요소 인식과 결합해 공간 노드·문·구역 이름을 만드는 처리 흐름에서 사람 검토를 어디에 두는지는 q3-01(처리 흐름 단계별 입력·출력과 사람 검토 위치)과 중복이어서 새로 등록하지 않고 q3-01 로 흡수했다.

q4-07 은 q4-03(도면 좌표계와 로봇별 지도 좌표계 정렬)·q4-04(도면·지도 버전 관리와 재검증)와 관련되지만, 제조사 지도 파일로의 변환·배포 책임과 절차를 묻는 점이 다르다.

q3-06 은 q3-02(공간 그래프 노드·엣지 단위)와 관련되지만, 공용 자원 목록을 관제에 내보낼 기준 형식을 묻는 점이 다르다.

## 6. 완료 조건 충족 현황

충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 입력 형식별 정보 항목과 표준·형식 목록이 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)의 "4. 필요한 데이터와 표준" 절에 실림 | 충족 | 표준 목록(q2-01, 실행 2026-09-25-28), 입력 형식별 정보 항목(q2-02, 실행 2026-09-25-36), 관제·ROP 수용 형식(q2-03, 실행 2026-09-25-44)이 4절에 실렸다 | 미승인 |
| 표준과 대응시킨 노드·엣지 유형이 [공간 그래프 스키마 초안](space-graph-schema-draft.md)의 개념·관계 목록 표에 반영됨 | 미충족 | 노드 쪽은 v0.4(공간 노드·층의 표준 대응 클래스 후보), v0.5(문·계단의 BIM 대응 클래스, 엘리베이터 유형 값), v0.6(층별 지도의 교환 형식 후보)으로 반영했으나, 관계(엣지) 쪽 표준 대응은 없다 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(관계(엣지) 쪽 표준 대응 없음; 열린 질문 q2-04·q2-06·q2-07·q2-08·q2-09)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 확인된 사실은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안"으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 공간 그래프를 표현하는 표준(BIM·IFC, 실내 공간 표준)과 데이터 교환 형식을 본다. 실행 2026-09-25-28은 7. 관련 표준·프레임워크·오픈소스 절에 실내 공간 표준의 발행 상태와 표준 간 대응을, 실행 2026-09-25-36은 같은 절에 CAD 레이어 명명 표준(ISO 13567, 미국 NCS, KS F 1542, 건설CALS 전자도면 작성표준), 실무 IFC 모델의 프록시 오용 점검, 국토교통부 건설산업 BIM 시행지침을 반영하도록 제안했다. 실행 2026-09-25-44는 같은 절에 VDA 5050 의 지도 식별·배포와 구역 집합, 지도 파일 내용 형식 미규정([추정]), VDMA LIF 레이아웃 교환을 반영하도록 제안했다.
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 분류 원문 10장이 건축 도면 기반 이동 지도의 중심 연구영역으로 두며, BIM·CAD에서 이동 공간을 만들고 층·목적지를 정렬하는 일 자체다. 실행 2026-09-25-28은 7. 관련 표준·프레임워크·오픈소스 절과 11. 열린 질문 절에, 실행 2026-09-25-36은 7. 관련 표준·프레임워크·오픈소스 절(도면 입력 형식별로 담기는 공간 정보와 빠지는 정보)과 8. 대표 연구와 자료 절(도면 해석 AI 연구)에 반영을 제안했다. 실행 2026-09-25-44는 7. 관련 표준·프레임워크·오픈소스 절(로봇 관제가 받는 지도·구역·레이아웃 형식)과 9. ROP가 직접 맡는 것과 외부와 연계하는 것 절(형식 변환·지도 판 관리는 기존 경계 문장과 각주를 재사용)에 반영을 제안했다.
- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 분류 원문 8장의 교차 규칙에 따라 도면 해석은 이 영역의 방법이 6. 지도·공간·위치 모델에 적용되는 것이다. 실행 2026-09-25-36은 8. 대표 연구와 자료 절에 CAD 레이어·블록 기반 자동 라벨링, 텍스트 결합 심볼 스포팅, 래스터 축척 문자 인식 연구를 반영하도록 제안했다. 실행 2026-09-25-44의 반영 제안은 없다.
- [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 인식한 문·엘리베이터가 설비·건물 시스템 연동 지점이 된다. 실행 2026-09-25-44의 반영 제안은 없다.

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

[^ref-419]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcDoor (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcDoor.md, 접근일 2026-09-25
[^ref-420]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcStair (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcStair.md, 접근일 2026-09-25
[^ref-421]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcTransportElementTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Types/IfcTransportElementTypeEnum.md, 접근일 2026-09-25
[^ref-422]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcWall (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcWall.md, 접근일 2026-09-25
[^ref-423]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcBuildingStorey (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcBuildingStorey.md, 접근일 2026-09-25
[^ref-424]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: Blocks (docs/source/concepts/blocks.rst, Autodesk 공식 DXF 참조 아님), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst, 접근일 2026-09-25
[^ref-425]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: Layers (docs/source/concepts/layers.rst, Autodesk 공식 DXF 참조 아님), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/layers.rst, 접근일 2026-09-25
[^ref-426]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: DXF Units (docs/source/concepts/units.rst, Autodesk 공식 DXF 참조 아님), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/units.rst, 접근일 2026-09-25
[^ref-427]: ISO, ISO 13567-1:2017 - Technical product documentation — Organization and naming of layers for CAD — Part 1: Overview and principles, 2017, https://www.iso.org/standard/70181.html, 접근일 2026-09-25 (원문 미열람)
[^ref-428]: National Institute of Building Sciences (United States National CAD Standard), AIA CAD Layer Guidelines, Layer Name Format (NCS V5), 미확인, https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-429]: 국가표준인증통합정보시스템(KSSN), KS F 1542(2020 확인) CAD 도면 작성을 위한 레이어 원칙과 기준, 2020-12, https://www.kssn.net/search/stddetail.do?itemNo=K001010129900, 접근일 2026-09-25 (원문 미열람)
[^ref-430]: 국토교통부 건설사업정보시스템(CALS), 건설CALS 전자도면 작성표준, 미확인, https://www.calspia.go.kr/portal/intro/introStandard02.do, 접근일 2026-09-25 (원문 미열람)
[^ref-431]: 신동철(대한건축학회 논문집 계획계), 건축 표준 캐드 레이어의 실무적용 실태 분석 연구, 2009-11, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01288876, 접근일 2026-09-25 (원문 미열람)
[^ref-432]: Noardo, F., Arroyo Ohori, K., Krijnen, T., & Stoter, J. (Applied Sciences 11(5), 2232), An Inspection of IFC Models from Practice, 2021, https://www.mdpi.com/2076-3417/11/5/2232, 접근일 2026-09-25 (원문 미열람)
[^ref-433]: arXiv 2607.12678 저자(미확인), Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings, 2026-07-14, https://arxiv.org/abs/2607.12678, 접근일 2026-09-25 (원문 미열람)
[^ref-434]: ArchiAI Lab (ArchCAD-400K 프로젝트), ArchCAD-400k: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting — project page, 미확인, https://archiai-lab.github.io/ArchCAD.github.io/, 접근일 2026-09-25
[^ref-435]: Buildings(MDPI) 게재 논문 저자(미확인), Raster Image-Based House-Type Recognition and Three-Dimensional Reconstruction Technology, 2025, https://doi.org/10.3390/buildings15071178, 접근일 2026-09-25 (원문 미열람)
[^ref-436]: 국토교통부, 건설산업 BIM 시행지침 정책정보 상세보기, 2022-07, https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4634, 접근일 2026-09-25 (원문 미열람)
[^ref-213]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-25
[^ref-215]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md, 접근일 2026-09-25 (원문 미열람)
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-25 (원문 미열람)
[^ref-066]: FloorPlanCAD 프로젝트(Fan, Z. 외), FloorPlanCAD Dataset — project page (floorplancad.github.io index.md), 2021, https://floorplancad.github.io/, 접근일 2026-09-25 (원문 미열람)
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P., FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-25 (원문 미열람)
[^ref-069]: Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT), MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition), 2023, https://github.com/MLSTRUCT/MLStructFP, 접근일 2026-09-25 (원문 미열람)
[^ref-070]: Hu, S. 외, Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer), 2024, https://github.com/SizheHu/Raster-to-Graph, 접근일 2026-09-25 (원문 미열람)
[^ref-073]: Luo, R. 외, ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting, 2025-03, https://arxiv.org/abs/2503.22346, 접근일 2026-09-25 (원문 미열람)
[^ref-074]: 한국지능정보사회진흥원(AI Hub), 건축 도면 데이터, 미확인, https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465, 접근일 2026-09-25 (원문 미열람)
[^ref-078]: Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S., Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans, 2024-08, https://arxiv.org/abs/2408.01526, 접근일 2026-09-25 (원문 미열람)
[^ref-081]: Vega-Torres, M. A. 외, Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2023-08, https://arxiv.org/abs/2308.05443, 접근일 2026-09-25 (원문 미열람)
[^ref-084]: Zhang, J. (jiajiezhang7 GitHub), osmAG-from-cad — README (CAD-to-osmAG pipeline), 미확인, https://github.com/jiajiezhang7/osmAG-from-cad, 접근일 2026-09-25 (원문 미열람)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-212]: continua-systems (GitHub), vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마), 미확인, https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json, 접근일 2026-09-25 (원문 미열람)
[^ref-227]: Mobile Industrial Robots(MiR), MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본, 2025-01, https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330, 접근일 2026-09-25 (원문 미열람)
[^ref-440]: ROS Navigation (ros-navigation/navigation2 GitHub), nav2_map_server — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md, 접근일 2026-09-25
[^ref-441]: Open Robotics (open-rmf), rmf_traffic_editor — README, 미확인, https://github.com/open-rmf/rmf_traffic_editor, 접근일 2026-09-25
[^ref-442]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/zoneSet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/zoneSet.schema, 접근일 2026-09-25

## 9. 이력

실행 id `build-2026-09-25`는 확장 아이디어 편입 때의 트랙 시드 생성을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 초안 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-44 | q2-03 | q4-07, q3-06 | v0.5 → v0.6 | 4 |
| 2026-09-25 | 2026-09-25-36 | q2-02 | q2-08, q2-09 | v0.4 → v0.5 | 3 |
| 2026-09-25 | 2026-09-25-28 | q2-01 | q2-07, q3-05 | v0.3 → v0.4 | 2 |
| 2026-09-25 | build-2026-09-25(트랙 시드, 파이프라인 실행 아님) | 없음 | 시드 q2-01~q2-03(3건, [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [공간 그래프 스키마 초안](space-graph-schema-draft.md)에서 생성) | 1 |
