# 리서치 브리프 2026-09-25-65

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-65 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 3 · 답한 질문 q3-03

## 갭(비어 있거나 약한 섹션)

- 단계 3 질문 q3-03 열림(target.json 지정, CLI 지정 질문 id). 단계 3 페이지 3절에 q3-03 소제목 없음
- 완료 조건: 아이디어 3. 건축 도면 자동 인식 5절 '핵심 구성 요소' 가운데 능력 대조가 '아직 조사되지 않은 구성 요소'로 남아 있음
- 완료 조건: 아이디어 3. 건축 도면 자동 인식 5절 '다른 아이디어와의 연결'이 '아직 조사되지 않음'(아이디어 1. 로봇 기능 온톨로지와의 연결 근거 없음)
- 공간 그래프 스키마 초안 v0.7: 문·계단·주행 차선에 로봇 능력과 대조할 통과 요구 조건 속성이 없고, 6절 질문 '공간 그래프를 로봇 기능 온톨로지와 어떤 관계로 잇는가'(q3-03) 미해결
- 5. 로봇 능력·작업 온톨로지 쪽에 공간 요소(문·계단·승강기)와 로봇 능력의 대응 근거 없음
- 10. 설비·건물 시스템 연동 쪽에 문·승강기 통과를 로봇 능력과 설비 연동 가운데 무엇으로 충족하는지에 대한 근거 없음

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q3-03 인식한 공간·시설을 로봇 기능 온톨로지의 능력(계단·도어 조작·충전)과 어떻게 이어 "이 로봇이 이 경로를 갈 수 있는가"를 판단하게 하는가?
3. 로봇 상호운용 규격과 오픈소스 관제(VDA 5050 팩트시트·주문, Open-RMF 플릿 설정·차선 폐쇄, Nav2 경로 서버)는 로봇별 통행 가능 여부를 어떤 필드와 구조로 표현하는가? (단계 3 페이지 3절, 스키마 초안 2·6절 겨냥)
4. BIM(IFC 4.3)과 실내 공간 표준 확장은 문·계단·승강기의 통과 조건(폭, 자동 구동, 단 높이)을 어떤 속성으로 담고, 이동 주체의 능력과 어떻게 대조하는가? (스키마 초안 2절 겨냥)
5. BIM·건물 디지털 트윈에서 로봇 능력별 지도·경로를 만드는 연구와 능력 모델(AAS 능력 기술, 이종 로봇 능력·스킬 모델)은 요구 능력과 제공 능력을 어떻게 맞추는가? (아이디어 페이지 5절, 5. 로봇 능력·작업 온톨로지 연결)
6. 국내에는 로봇의 승강기 탑승·건물 이동을 위한 표준이나 인증 기준(KS, 로봇 친화형 건축물 인증)이 있고, 무엇을 요구하는가? (한국 자료 우선 규칙, 10. 설비·건물 시스템 연동 연결)
7. 능력별로 걸러 낸 경로를 작업 배정에 어떻게 쓰는가, 그리고 문 닫힘 같은 현재 상태는 정적 능력 대조와 어떻게 구분하는가? (13. 작업 배정 — MRTA, 8. 실시간 세계 상태·데이터 일관성 연결)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소의 팩트시트 JSON 스키마는 로봇 유형 사양(기구학·등급·최대 적재 질량·위치추정 방식·주행 방식·지원 구역 유형), 물리 파라미터(최소·최대 속도, 최소·최대 높이, 폭, 길이), 지원 동작과 동작 범위(즉시·노드·엣지·구역)를 두지만 계단·문·승강기 이용 능력을 뜻하는 전용 필드는 두지 않는다. | ref-228 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | VDA 5050 3.0.0 명세는 도입 단계에서 경로를 로봇 크기 비율에 따라 특정 로봇 그룹으로 제한할 수 있다고 적고, 관제의 경로 계산이 로봇마다 크기·기동성 같은 물리적 특성의 한계를 고려하며, 관제가 보유한 전체 그래프의 로봇별 통행 제한은 로봇에 전달하지 않고 허용 엣지만 주문에 넣는다고 규정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f3 | [추정] | VDA 5050 주문 스키마의 엣지 통과 조건(로봇 최대 높이·적재장치 최소 높이·최대 속도 등)과 팩트시트의 로봇 물리 파라미터(높이·폭·길이·속도)는 같은 단위의 값이어서, 관제 쪽에서 둘을 비교해 로봇별 통행 가능 엣지를 거를 수 있을 것으로 보인다. | ref-413, ref-228 | 아니오 | low | 2026-09-25 | 제약 | — |
| f4 | [사실] | Open-RMF 는 플릿마다 자기 주행 그래프(traffic-editor 의 그래프 번호)로 허용 동작을 전달하고, 플릿 어댑터 설정은 속도·가속 한계, 차체 반경(footprint)·근접 반경(vicinity), 후진 가능 여부, 배터리, 수행 가능 작업 유형, 동작 목록을 두지만 문·승강기 이용 능력 필드는 두지 않는다. | ref-079, ref-105 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f5 | [사실] | Open-RMF rmf_traffic 의 그래프 정의에는 로봇별·플릿별 차선 필터나 차선 폐쇄 상태가 없고, 실행 중 차선 폐쇄·개방은 플릿 이름과 열 차선·닫을 차선 번호 목록을 담는 별도 메시지(LaneRequest)로 요청한다. | ref-536, ref-645 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f6 | [사실] | Open-RMF 에서 문은 traffic-editor 로 주행 그래프에 이름과 함께 그려야 하고, 문 여닫기는 로봇이 아니라 문 어댑터가 DoorRequest 를 받아 진행 중인 로봇 작업을 방해하지 않을 때만 문 노드에 지시하며 문 노드는 DoorState 를 낸다. | ref-283 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f7 | [사실] | Nav2 경로 서버(Route Server)는 GeoJSON 경로 그래프의 노드·방향 엣지에 임의 메타데이터를 달고, 벌점·의미 분류·동적 엣지(로봇이 막힌 엣지를 보고해 닫음) 같은 채점 플러그인으로 엣지 비용을 계산하며, 엣지 진입·이탈이나 노드 도달 때 문 열기 같은 동작(operation)을 실행하게 한다. | ref-646 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f8 | [사실] | IFC 4.3 의 문 공통 속성 세트(Pset_DoorCommon)는 자동 구동 장치가 있는지(HasDrive)와 지역 건축 기준상 장애인 접근 가능 여부(HandicapAccessible)를 속성으로 두며, IfcDoor 자체는 전체 폭(OverallWidth)을 갖는다. | ref-649, ref-419 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f9 | [사실] | IFC 4.3 의 계단 공통 속성 세트(Pset_StairCommon)는 단 높이(RiserHeight), 디딤판 길이(TreadLength), 단 수(NumberOfRiser)를 속성으로 두어, 계단의 통과 난이도를 수치로 담을 수 있다. | ref-650 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f10 | [사실] | BIM 기반 로봇 주행·점검 온톨로지 OBRNIT 는 로봇 개념에 유형·크기, 이동 방식·자유도, 안전 거리 같은 제약, 센서를 두고, 지상 로봇에는 오를 수 있는 계단 단의 최대 높이 같은 이동 제약이 있다고 본다. | ref-461 | 아니오 | medium | 2024 | 수행 자원 | 원문 미열람 |
| f11 | [사실] | 교통약자 실내 길찾기를 위한 IndoorGML 확장 연구는 경사로에 경사, 엘리베이터에 면적·통과 폭 속성을 두고 이 값을 사전 정한 임계값으로 통과 가능·어려움·불가의 세 단계로 나눠 경로 계획에 써, 이동 주체에 따라 경로가 크게 달라짐을 보였다. | ref-348 | 아니오 | medium | 2020 | 제약 | 원문 미열람 |
| f12 | [사실] | de Vos 외(2024)는 BIM 에서 건물 요소의 3D 형상과 의미(재질·요소 유형 등)를 뽑아 RDF 그래프 세계 모델에 저장하고, 요청한 로봇의 스킬에 맞춘 지도를 SPARQL 질의로 생성하는 방법을 제안했다(예: 유리가 아닌 요소만 골라 지도 생성). | ref-647 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f13 | [사실] | Omer 외(RoboCup 2024 심포지엄, 2025)는 건물 디지털 트윈의 의미·거리 정보로 연결 그래프에 가중치를 주고 A* 로 경로를 구해, 주행 능력이 서로 다른 로봇마다 로봇별 지도·경로를 만드는 의미 기반 경로 계획을 제안했다. | ref-648 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f14 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 은 공정·제품의 요구 능력과 자원의 제공 능력을 모델링해 비교하게 하며, 능력을 속성(최대 속도·허용 공차 등)으로 상세화하고 속성 제약을 전제조건으로 쓸 수 있게 한다. | ref-229 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f15 | [사실] | Vieira da Silva 외는 이종 자율 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 보고, 제조 분야의 능력·스킬 모델을 자율 로봇·다중 로봇 시스템으로 확장하는 온톨로지 기반 능력 모델을 제안했다. | ref-038 | 아니오 | medium | 2022-09 | — | 원문 미열람 |
| f16 | [사실] | 연계 대상: Schulze 외(2025)는 7자유도 팔을 단 이동 로봇이 닫힌 문을 스스로 열고 사람용 인터페이스로 승강기를 조작해 층을 옮기는 운반 서비스를 요양 시설과 대학 건물에서 현장 시험했다. | ref-653 | 아니오 | medium | 2025-02-25 | 수행 자원 | 원문 미열람 |
| f17 | [사실] | 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항과 실내 배송 로봇에 관한 KS 제정을 알리며, 로봇이 건물 안을 이동하려면 속도 제어, 위험 상황의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지 기준이 필요하다고 밝혔고, 관련 표준으로 KS B 7317(이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법)이 등재되어 있다. | ref-315, ref-314 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f18 | [사실] | 국내 연구(지적과 국토정보, 2022)는 업무 시설을 대상으로 초점집단면접과 계층화 분석으로 로봇 친화형 건축물 인증 지표 23개 평가 항목의 상대 중요도를 정했으며, 요구사항을 운영 시설·시스템의 적정성과 건축·로봇 운영 시스템·네트워크의 적정성으로 나눴다. | ref-658 | 아니오 | medium | 2022 | 제약 | 원문 미열람 |
| f19 | [사실] | 연계 대상: CHORAL(arXiv 2601.10340)은 의미 지도에서 플랫폼마다 통과 능력을 반영한 경로를 먼저 구하고 이를 이종 차량 경로 문제에 넣어 점검 작업 배정과 경로를 함께 계산하는 틀을 제안했다(실외 점검 임무 대상). | ref-654 | 아니오 | medium | 2026-01 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | Halilovic 외(arXiv 2606.00117)는 주변 개체의 어포던스(affordance)와 그 상태, 정성적 공간 관계를 지역 어포던스 온톨로지로 표현하고 가상의 상태 변화를 평가해, 경로가 막힌 이유와 무엇이 바뀌면 계속 갈 수 있는지를 설명하는 방법을 제안했다. | ref-655 | 아니오 | medium | 2026-05 | 예외·성과 | 원문 미열람 |
| f21 | [추정] | q3-03 에 대해 확인한 자료를 이 위키가 묶으면, '이 로봇이 이 경로를 갈 수 있는가'는 공간 요소가 요구하는 통과 조건(문 폭·자동 구동 여부, 계단 단 높이, 승강기 칸 면적·통과 폭, 차선 높이 제한)을 로봇의 제공 능력 속성(폭·높이, 오를 수 있는 최대 단 높이, 문 조작·승강기 이용 가능 여부)과 비교하는 요구 능력–제공 능력 매칭으로 판단할 수 있을 것으로 보인다. | ref-649, ref-650, ref-461, ref-348, ref-229, ref-228, ref-413 | 아니오 | low | 2026-09-25 | 제약 | — |
| f22 | [추정] | 문·승강기 통과는 로봇 쪽 능력(팔로 문 열기·버튼 조작)으로도, 건물 쪽 연동(문 어댑터·자동 구동 문, 승강기 연동)으로도 충족될 수 있으므로, 능력 대조 규칙은 '로봇 능력 또는 설비 연동 가능' 같은 선택 조건으로 두어야 할 것으로 보이며, 로봇 쪽 조작 기술 자체는 연계 대상이다. | ref-283, ref-649, ref-653, ref-315 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f23 | [추정] | 확인한 관제 인터페이스(VDA 5050 팩트시트, Open-RMF 플릿 설정)에는 계단·문·승강기 능력 필드가 없고 통행 제한은 관제가 보유한 플릿·로봇별 그래프로 처리되므로, ROP 는 매뉴얼 등에서 얻은 로봇별 능력 속성을 따로 두고 플릿 중립 공간 그래프에서 로봇별 통행 가능 부분 그래프를 파생해야 하며, 차선 폐쇄·문 상태 같은 현재 상태는 이와 분리한 별도 층으로 두어야 할 것으로 보인다. | ref-228, ref-105, ref-031, ref-079, ref-645, ref-646 | 아니오 | low | 2026-09-25 | 제약 | — |
| f24 | [추정] | 분류 원문 질문의 ‘3층 출하 대기장’에 어느 로봇을 보낼 수 있는지는 그 구역 노드까지 승강기 엣지를 포함한 경로가 그 로봇의 통행 가능 부분 그래프 안에 있는지로 걸러 낸 뒤 작업 배정 후보로 넘기는 방식이 될 것으로 보이며, 능력별 경로를 먼저 구해 배정 문제에 넣는 연구가 이 구조의 예다. | ref-654, ref-648, ref-031 | 아니오 | low | 2026-09-25 | 출하 / 수행 자원 | — |

### 근거 발췌

- **f1**: factsheet.schema(main): typeSpecification(mobileRobotKinematics, mobileRobotClass, maximumLoadMass, localizationTypes, navigationTypes, supportedZones), physicalParameters(minimumHeight, maximumHeight, width, length 등, 미터), protocolFeatures.mobileRobotActions(actionScopes INSTANT·NODE·EDGE·ZONE). 계단·문·승강기 전용 필드는 열람 범위에서 확인되지 않음(발행일 미확인, 확인일 기준)
- **f2**: 5.2: routes "restricted for certain mobile robot groups (based on the size ratios)"; 5.3: route calculation taking into account limitations of physical properties (size, maneuverability); 6.1.1: fleet control only includes edges the robot is allowed to traverse. 6.1.4.3: 수행할 수 없는 동작(최대 들어올림 높이 초과 등)이 든 주문은 INVALID_ORDER_ACTION 으로 거부
- **f3**: order.schema 엣지: maxSpeed, maxRobotHeight, minLoadHandlingDeviceHeight, corridor 등. factsheet.schema physicalParameters: maximumHeight, width, length, maximumSpeed(미터·m/s). 두 값을 비교하는 규칙은 명세에 없고 이 위키의 추론이다(발행일 미확인, 확인일 기준)
- **f4**: fleet_adapter_template config.yaml rmf_fleet: limits, profile(footprint 0.3, vicinity 0.5), reversible, battery_system, task_capabilities(loop, delivery), actions, robots(charger). 문·승강기 관련 필드 없음. traffic-editor: 차선의 graph_idx 로 플릿별 그래프(발행일 미확인, 확인일 기준)
- **f5**: Graph.hpp: Lane 속성은 속도 제한·상호 배제 그룹, 폐쇄·로봇별 필터 없음. rmf_fleet_msgs/LaneRequest.msg: string fleet_name, uint64[] open_lanes, uint64[] close_lanes. 두 파일은 같은 발행 주체(Open Robotics)라 독립 교차 확인 아님(발행일 미확인, 확인일 기준)
- **f6**: integration_doors.md: doors must be drawn on the navigation graph using traffic_editor; 문 어댑터는 "acts like a state supervisor" 로서 로봇 작업을 방해할 요청을 막는다; DoorRequest·DoorState 메시지(발행일 미확인, 확인일 기준)
- **f7**: nav2_route README: nodes·edges(startid, endid) + metadata; Penalty·Semantic·DynamicEdges scorer("robots report an edge to be blocked"); operations triggered on entering/exiting edge or achieving node, 예: opening doors(발행일 미확인, 확인일 기준)
- **f8**: IFC 4.3.2 Pset_DoorCommon: HasDrive = 객체에 자동 구동 장치가 있으면 TRUE; HandicapAccessible = 지역 건축 기준에 따라 장애인 접근 가능하면 TRUE. IfcDoor: OverallWidth·OperationType(개발 브랜치 원본). Pset 정의는 검색 요약 기준(발행일 미확인, 확인일 기준)
- **f9**: IFC4.3.2 Pset_StairCommon: RiserHeight(계단의 모든 단에 같다고 가정), TreadLength(보행선에서 디딤판 앞끝 사이 수평 거리), NumberOfRiser. 공식 문서 검색 요약 기준, 개발 저장소 Pset 파일은 속성 정의를 담지 않아 확인 못함(발행일 미확인, 확인일 기준)
- **f10**: OBRNIT(Buildings 14(8), 2024): robot concepts cover basic attributes(type, size), performance(movements, DOF), constraints(safety distance), sensors; UGV 에는 "maximum height of a stair step that they can climb" 같은 제약(검색 요약 기준)
- **f11**: PWDRamp: slope; PWDElevator: area, passing width. 속성값을 임계 등급에 따라 0(통과 가능)·1(어려움)·2(불가)로 부여; 쇼핑몰 두 사례에서 교통약자 경로가 일반 보행자와 크게 다름(검색 요약 기준)
- **f12**: arXiv 2402.18174: RDF graph world model 을 질의해 "maps tailored to the skill of the robot requesting them"; SPARQL 로 유리가 아닌 특정 의미 유형 요소의 메시만 조회; 세계 모델은 로봇과 양방향 연결(검색 요약 기준)
- **f13**: Semantic and metric information extracted from the digital twin is used to assign weights to a connectivity graph, A*; robot-specific maps; accommodates robots with varying navigation abilities(초록 검색 요약 기준)
- **f14**: README: "process or product requirements (required capabilities) and resource capabilities (provided capabilities)"; properties 예 maximum speed, allowed tolerances; property constraints 는 precondition 으로 사용 가능; 요구·제공 능력 매칭의 기반(발행일 미확인, 확인일 기준)
- **f15**: arXiv 2209.10900(at - Automatisierungstechnik 게재): "For heterogeneous robots, there is currently no consistent way of describing the functions that each robot provides"; keywords Capabilities, Skills, AMR, Multi-Robot Systems, Ontologies(검색 요약 기준)
- **f16**: Frontiers in Robotics and AI(2025-02-25): SCITOS G5 + Kinova Gen II 7-DOF arm, autonomous door manipulation and floor switching through elevator operation, field tests in elderly care facility and university office building(검색 요약 기준)
- **f17**: 보도자료: 실내 주행, 엘리베이터 탑승 등 건물 내 이동에 속도제어, 보호정지, 높낮이차·틈새극복, 추락·넘어짐 방지 기준 필요. KSSN: KS B 7317 표준명. 단차·틈새의 수치 기준은 미확인(두 출처 모두 원문 미열람)
- **f18**: 업무시설로 범위 한정, FGI·AHP 로 23개 평가 항목 상대 중요도 산출; 요구사항을 (1) 운영 시설·시스템 적정성 (2) 건축·로봇 운영 시스템·네트워크 적정성으로 분류(검색 요약 기준, 세부 수치 기준 미확인)
- **f19**: capability-aware paths for each platform ... incorporated into a heterogeneous vehicle routing formulation that jointly assigns inspection tasks and computes robot trajectories; 지상 로봇은 통과성이 나쁜 영역 회피; 시뮬레이션과 3개 플랫폼 실제 임무로 평가(저자 보고, 검색 요약 기준)
- **f20**: local affordance ontology: nearby entities, affordances, affordance states, qualitative spatial relations; hypothetical object–affordance state changes 를 설명 요인으로 평가; 로봇 사서 시나리오 벤치마크(2026-05 제출, 검색 요약 기준)
- **f21**: IFC Pset(HasDrive, RiserHeight), OBRNIT(최대 단 높이), IndoorGML 교통약자 확장(임계값 3단계 판정), IDTA 02020(요구·제공 능력 매칭, 속성 제약)을 이 위키가 종합한 것이며 로봇 경로 통과성을 이렇게 정의한 단일 출처는 확인하지 못함
- **f22**: Open-RMF 문 어댑터가 문을 여는 구조, IFC HasDrive(자동 구동), Schulze 외의 팔 기반 문·승강기 조작, KS 승강기 탑승 기준을 이 위키가 종합(추정)
- **f23**: 팩트시트·플릿 설정의 필드 부재(f1·f4), VDA 5050 관제 보유 통행 제한(f2), Open-RMF graph_idx·LaneRequest(f4·f5), Nav2 동적 엣지(f7)를 이 위키가 종합(추정). 현재 상태 층은 8. 실시간 세계 상태·데이터 일관성 쪽
- **f24**: CHORAL(능력별 경로 → 이종 차량 경로·배정), Omer 외(로봇별 지도·경로), VDA 5050 허용 엣지만 주문에 포함을 이 위키가 종합(추정). 13. 작업 배정 — MRTA 와 연결

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-348 | ISPRS International Journal of Geo-Information(MDPI) 게재 논문 저자(미확인) | Data Model for IndoorGML Extension to Support Indoor Navigation of People with Mobility Disabilities | 2020 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2220-9964/9/2/66 | 예 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 예 |
| ref-419 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcDoor (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcDoor.md | 예 |
| ref-461 | Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인) | Ontology for BIM-Based Robotic Navigation and Inspection Tasks | 2024 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2075-5309/14/8/2274 | 예 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-645 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-646 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_route — README (Nav2 Route Server) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ros-navigation/navigation2/blob/main/nav2_route/README.md | 아니오 |
| ref-647 | de Vos, K., van den Brandt, G., Senden, J., Pauwels, P., van de Molengraft, R., & Torta, E. | Generation of skill-specific maps from graph world models for robotic systems | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.18174 | 예 |
| ref-648 | Omer 외(Omer, de Vos, Pauwels, Torta, Monteriù; RoboCup 2024 심포지엄 논문집) | Semantic Path Planning for Heterogeneous Robots from Building Digital Twin Data | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-031-85859-8_5 | 예 |
| ref-649 | buildingSMART International | Pset_DoorCommon - IFC 4.3.2 Documentation | 미확인 | 표준 | medium | 2026-09-25 | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm | 예 |
| ref-650 | buildingSMART International | Pset_StairCommon - IFC4.3.2.0 Documentation | 미확인 | 표준 | medium | 2026-09-25 | https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_StairCommon.htm | 예 |
| ref-229 | IDTA (admin-shell-io/submodel-templates GitHub) | IDTA 02020 Capability Description — README (Submodel Template, Version 1.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-038 | Vieira da Silva, L. M. 외 | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.10900 | 예 |
| ref-653 | Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau) | On realizing autonomous transport services in multi story buildings with doors and elevators | 2025-02-25 | 논문 | medium | 2026-09-25 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full | 예 |
| ref-654 | arXiv 2601.10340 저자(미확인) | CHORAL: Traversal-Aware Planning for Safe and Efficient Heterogeneous Multi-Robot Routing | 2026-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2601.10340 | 예 |
| ref-655 | Halilovic, A., Hasic, V., & Krivic, S. | Ontology-Guided Reasoning for Affordance-Based Explanations of Robot Navigation | 2026-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.00117 | 예 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-658 | 지적과 국토정보(한국국토정보공사 공간정보연구원) 게재 논문 저자(미확인) | 로봇 친화형 건축물 인증 지표 개발: 초점집단면접(FGI)과 분석적 계층화 과정(AHP)의 활용 | 2022 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002903574 | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세. 도입 단계의 로봇 그룹별 경로 제한, 관제의 경로 계산과 로봇별 통행 제한 보유, 주문 거부 규칙을 확인했다.
- **ref-079**: 원문 미열람. traffic-editor 의 차선 속성(양방향·graph_idx)과 플릿별 그래프, 경유점 속성 참고(이전 실행에서 확인).
- **ref-105**: Open-RMF 플릿 어댑터 설정 템플릿. 속도 한계·차체 반경·후진·배터리·작업 유형·동작·좌표 대응점을 두고 문·승강기 필드는 없다.
- **ref-348**: 원문 미열람. IndoorGML 교통약자 확장: 경사로 경사·엘리베이터 면적·통과 폭 속성과 임계값 기반 3단계 통과 판정.
- **ref-413**: 원문 미열람. VDA 5050 주문 스키마의 엣지 통과 조건(최대 속도·로봇 최대 높이·적재장치 최소 높이 등) 참고(이전 실행에서 확인, 이번에 다시 열지 않음).
- **ref-419**: 원문 미열람. IfcDoor 의 전체 폭(OverallWidth)·여닫는 방식(OperationType) 참고(이전 실행에서 확인).
- **ref-461**: 원문 미열람. OBRNIT 의 로봇 개념(크기·이동·자유도·제약·센서)과 지상 로봇의 최대 계단 단 높이 제약.
- **ref-536**: rmf_traffic 그래프 정의. 차선 속성은 속도 제한·상호 배제 그룹이며 로봇별 필터·폐쇄 상태는 없다.
- **ref-228**: VDA 5050 팩트시트 JSON 스키마(main 브랜치). 유형 사양·물리 파라미터·지원 동작·적재 사양을 두며 계단·문·승강기 전용 필드는 없다.
- **ref-645**: Open-RMF 차선 폐쇄·개방 요청 메시지. 플릿 이름과 열 차선·닫을 차선 번호 목록을 담는다.
- **ref-646**: Nav2 경로 서버. GeoJSON 경로 그래프의 노드·엣지 메타데이터, 엣지 채점 플러그인(벌점·의미·동적 엣지 폐쇄), 노드·엣지에서 실행하는 동작(문 열기 등).
- **ref-647**: 원문 미열람. BIM 에서 만든 RDF 그래프 세계 모델을 SPARQL 로 질의해 로봇 스킬별 지도를 생성하는 방법.
- **ref-648**: 원문 미열람. 건물 디지털 트윈의 의미·거리 정보로 연결 그래프에 가중치를 주고 A* 로 로봇별 경로를 구하는 의미 기반 경로 계획.
- **ref-649**: 원문 미열람. IFC 4.3.2 문 공통 속성 세트. 자동 구동 여부(HasDrive), 장애인 접근 가능(HandicapAccessible) 등.
- **ref-650**: 원문 미열람. IFC 4.3.2 계단 공통 속성 세트. 단 높이(RiserHeight)·디딤판 길이(TreadLength)·단 수(NumberOfRiser) 등.
- **ref-229**: 자산관리셸 능력 기술 서브모델 1.0. 요구 능력과 제공 능력, 속성, 속성·전이 제약, 스킬과 능력 매칭의 기반을 정의한다.
- **ref-038**: 원문 미열람. 제조 분야 능력·스킬 모델을 이종 자율 로봇으로 확장하는 온톨로지 기반 능력 모델(at - Automatisierungstechnik 게재).
- **ref-653**: 원문 미열람. 팔을 단 이동 로봇이 문을 열고 사람용 인터페이스로 승강기를 조작하는 다층 건물 운반 서비스와 현장 시험.
- **ref-654**: 원문 미열람. 의미 지도에서 플랫폼별 통과 능력 반영 경로를 구해 이종 차량 경로·작업 배정 문제에 넣는 틀(실외 점검).
- **ref-655**: 원문 미열람. 주변 개체의 어포던스와 상태를 지역 온톨로지로 표현해 막힌 경로의 이유와 해소 조건을 설명하는 방법.
- **ref-315**: 원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료. 속도제어·보호정지·높낮이차·틈새극복·추락 방지 기준 언급.
- **ref-314**: 원문 미열람. 이동 로봇의 엘리베이터 탑승 안전 요구사항·평가 방법 KS 표준의 등재 정보. 수치 기준은 미확인.
- **ref-658**: 원문 미열람. 업무 시설 대상 로봇 친화형 건축물 인증 지표 23개 평가 항목과 상대 중요도.
- **ref-283**: Open-RMF 문 연동. 문을 주행 그래프에 이름과 함께 그리고, 문 어댑터가 DoorRequest·DoorState 로 문 여닫기를 감독한다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | 2, 3, 4, 5, 6, 8, 9 | q3-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24 (신뢰도 low) — 2절 q3-03 상태 답함, 3절 q3-03 소제목 신설({#q3-03}): 관제 인터페이스의 능력·통행 제한 표현(VDA 5050 팩트시트 f1, 관제 보유 통행 제한 f2, 엣지 조건–물리 파라미터 비교 f3 추정, Open-RMF 플릿 설정·플릿별 그래프 f4, 차선 폐쇄 메시지 f5, 문 어댑터 f6, Nav2 경로 서버 f7), 공간 요소의 통과 조건 속성(IFC Pset_DoorCommon f8, Pset_StairCommon f9, IndoorGML 교통약자 확장 f11), 로봇 능력 표현(OBRNIT f10, IDTA 02020 f14, 이종 로봇 능력 모델 f15), 능력별 지도·경로 연구(f12·f13·f19 연계 대상), 문·승강기 통과 방식(f16 연계 대상, 국내 KS f17, 로봇 친화형 건축물 인증 f18), 현재 상태와의 구분(f20), 종합: 요구–제공 능력 매칭(f21), 로봇 능력 또는 설비 연동(f22), 로봇별 통행 가능 부분 그래프와 현재 상태 층 분리(f23), 분류 원문 질문(f24) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 5 | 아이디어 페이지 5절(트랙 산출물): '핵심 구성 요소'에 '능력 대조' 소절 신설 — 공간 요소 통과 조건(f8·f9·f11)과 로봇 제공 능력(f1·f4·f10·f14)의 매칭(f21 추정), 설비 연동 선택 조건(f22), 로봇별 부분 그래프와 현재 상태 분리(f23). '다른 아이디어와의 연결'에 아이디어 1(로봇 기능 온톨로지)의 능력 속성이 공간 그래프 통과 조건과 대조되는 지점(f14·f15·f21·f23, 추정), 13. 작업 배정 — MRTA 로 넘어가는 지점(f19·f24) |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes 가 검증 승인되면 문에 '자동 구동 여부(HasDrive)·장애인 접근 가능' 속성(f8), 계단에 '단 높이·디딤판 길이·단 수' 속성(f9), 개념 '통과 요구 조건' 추가(f8·f9·f11·f14). 미승인 제안과 f21~f23(매칭 규칙·설비 연동 선택 조건·부분 그래프 파생)은 6절 질문(q3-03 항목 근거 보강)으로 |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f1, f10, f14, f15, f21, f23): 로봇 능력 속성(최대 단 높이·폭·높이·문 조작·승강기 이용)을 공간 요소의 통과 조건과 요구–제공 능력으로 대조하는 접근(추정)과 관제 인터페이스에 해당 필드가 없다는 점 |
| update | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f6, f8, f17, f22): 문·승강기 통과를 설비 연동(Open-RMF 문 어댑터, IFC 자동 구동 문)으로 충족하는 방식, 국내 KS B 7317 승강기 탑승 기준(단차·틈새), 로봇 조작과 설비 연동의 선택 조건(추정) |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f19, f24): 능력별 통행 가능 경로를 먼저 구해 배정 후보를 거르거나 이종 차량 경로·배정 문제에 넣는 접근(CHORAL, 연계 대상 사례) |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f7, f12, f13, f23): BIM·건물 디지털 트윈에서 로봇 스킬별 지도·경로를 생성하는 연구, 경로 그래프 엣지 메타데이터·동적 폐쇄, 플릿 중립 공간 그래프에서 로봇별 통행 가능 부분 그래프 파생(추정) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 통과 가능성 | Traversability | 특정 로봇이 공간 그래프의 구역·차선·문·계단·승강기를 자신의 능력과 현재 상태로 지나갈 수 있는지의 여부나 정도를 말한다. |
| 차선 폐쇄 | Lane Closure | 관제가 실행 중에 주행 그래프의 특정 차선을 일시적으로 쓰지 못하게 닫는 조치로, Open-RMF 에서는 플릿 이름과 닫을 차선 번호 목록을 담은 요청 메시지로 한다. |

## 열린 질문

새로 생긴 질문:

- KS B 7317 이 정한 이동 로봇의 승강기 탑승 단차·틈새 기준값은 무엇이며, 국내 물류센터의 화물용 승강기와 이종 제조사 로봇에 그대로 적용되는가? | 관련 영역: 10. 설비·건물 시스템 연동, 6. 지도·공간·위치 모델 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 24 · 교차 확인: 0
- 예산 사용량: 검색 22회 · 신규 출처 16건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 자료마다 발행 주체 한 곳의 근거만 있음(f5 의 두 출처는 같은 Open Robotics, f17 의 두 출처는 보도자료와 표준 등재 정보로 내용 확인은 보도자료뿐)
    - f8·f9 IFC 4.3 Pset 속성 정의는 공식 문서 검색 요약 기준. 개발 저장소의 Pset_DoorCommon.md·Pset_StairCommon.md 는 열었으나 속성 정의를 담지 않아 확인하지 못함
    - f10·f11·f12·f13·f15·f16·f19·f20 논문 원문 미열람(검색 요약 범위), ref-648·ref-654 세부 방법·평가 조건 미확인
    - f17 KS B 7317 의 단차·틈새 수치 기준 미확인(표준 원문 유료·미열람)
    - f18 로봇 친화형 건축물 인증 지표의 세부 항목(출입문 폭·단차 등) 미확인
    - f21~f24 는 이 위키의 종합이며 로봇 경로 통과성을 요구–제공 능력 매칭으로 정의한 단일 출처는 찾지 못함
    - 매뉴얼 기반 로봇 기능 온톨로지 트랙의 능력 개념(계단·도어 조작·충전)과의 이름 대응은 그 트랙 온톨로지 초안이 입력에 없어 확인하지 못함
- 범위 경계 위반 의심:
    - f16: 팔로 문을 열고 승강기 버튼을 누르는 조작은 분류 원문 9장 '로봇 자체 지능·제어'(파지·관절 제어) 연계 영역이라 '연계 대상: '으로 표시하고 문·승강기 통과 방식의 한 갈래로만 씀
    - f19: CHORAL 은 실외 점검 임무의 인식 기반 통과성 연구(업종별 조건·센서 인식 연계)라 '연계 대상: '으로 표시하고 능력별 경로를 배정에 넣는 구조의 사례로만 씀
    - f17·f22: 승강기 안전 제어 자체는 분류 원문 9장 '시설·설비 제어' 연계 영역이며, ROP 쪽은 통과 조건 대조와 연동 요청까지로 한정해 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 신규 ref-228(VDA 5050 factsheet.schema)·ref-645(LaneRequest.msg)·ref-646(nav2_route README)·ref-229(IDTA 02020 README)·ref-283(integration_doors), 재사용 ref-105(플릿 어댑터 config.yaml)·ref-536(Graph.hpp). ref-031 은 입력 원문 텍스트(inbox). 나머지 신규 10건과 재사용 ref-079·ref-348·ref-413·ref-419·ref-461 은 원문 미열람이라 신뢰도 상한 medium. IFC Pset 파일 2건(raw)은 열었으나 속성 정의가 없어 출처로 쓰지 않았다. 검색 22회/40, 신규 출처 16건/20(ref-228~ref-283, 예약 구간 안), 재사용 8건. 질문 선택: target.json 지정 q3-03 1건. q3-03 은 공간 요소의 통과 조건 속성과 로봇 능력 속성의 요구–제공 능력 매칭, 설비 연동 선택 조건, 로봇별 통행 가능 부분 그래프 파생으로 답했으나 핵심 종합(f21~f24)이 추정이라 종합 신뢰도 low. 충전 능력은 이전 실행의 충전 동작(startCharging)·충전소 속성 외에 새 근거를 찾지 못해 이번 답은 계단·문·승강기 중심이다. 한국 자료: 국가기술표준원 보도자료(ref-315), KS B 7317(ref-314), 로봇 친화형 건축물 인증 지표 연구(ref-658). 교차 규칙: 27. AI·학습·적응과 모델 운영 관련 finding 없음(f20 온톨로지 추론은 설명 방법이며 학습 모델이 아님). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈: 문 상태·차선 폐쇄는 현재 상태로 8 쪽에 두도록(f20·f23) 구분했고 22 관련 주장 없음. 정정 요청 없음. 후속 질문 2건, 온톨로지 변경 제안 3건. 일반 열린 질문 1건. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 4건(갱신 상한과 별도).

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 3
- 답한 질문 id: q3-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | VDA 5050 팩트시트·Open-RMF 플릿 설정에 계단·문·승강기 능력 필드가 없을 때, 로봇별 최대 단 높이·문 조작·승강기 이용 가능 여부 같은 능력 속성 값을 매뉴얼이나 현장 시험에서 어떻게 얻어 공간 그래프의 통과 요구 조건과 같은 단위로 맞추는가? (q3-03 에서 파생, 매뉴얼 기반 로봇 기능 온톨로지 트랙과 연결) | 3 | f23 |
| — | 요구–제공 능력 매칭으로 만든 로봇별 통행 가능 판정이 실제 주행에서 틀리는 경우(통과 가능 판정 후 실패, 불가 판정의 과잉 제한)를 시뮬레이션·실기체 시험으로 어떻게 측정하고 임계값을 보정하는가? (q3-03 에서 파생) | 5 | f21 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 문 (Door) | f8 | 속성에 '자동 구동 여부(IFC 4.3.2 Pset_DoorCommon.HasDrive)'와 '장애인 접근 가능(HandicapAccessible)'을 더한다. 로봇 능력(문 조작)과 대조할 때 자동 구동 문이면 설비 연동으로 통과할 수 있는 근거가 된다. Pset 정의는 공식 문서 검색 요약 기준(원문 미열람). |
| modify | concept | 계단 (Stairs) | f9, f10 | 속성에 '단 높이·디딤판 길이·단 수(IFC 4.3.2 Pset_StairCommon 의 RiserHeight·TreadLength·NumberOfRiser)'를 더한다. OBRNIT 가 지상 로봇의 제약으로 둔 '오를 수 있는 최대 단 높이'와 대조하는 값이다. 기존 속성 '잇는 층'과 충돌하지 않는다. |
| add | concept | 통과 요구 조건 (Traversal Requirement) | f8, f9, f11, f14 | 문·계단·승강기·주행 차선을 지나기 위해 이동 주체가 갖춰야 하는 조건(최소 통과 폭, 최대 단 높이, 문 조작 또는 자동 구동, 승강기 칸 면적·통과 폭, 높이 제한)과 그 임계값. IndoorGML 교통약자 확장의 임계 등급 판정과 IDTA 02020 의 요구 능력·속성 제약이 근거다. 로봇 능력과의 매칭 규칙(f21)과 설비 연동 선택 조건(f22)은 추정이라 정의에 넣지 않고 6절 질문으로 둔다. 아이디어 정의 문구에 없는 개념이어서 1절 범위와의 관계, 아이디어 1 온톨로지의 '제약'·'실행 조건' 개념과의 중복 여부를 검토해야 한다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 아이디어 3. 건축 도면 자동 인식 5절 핵심 구성 요소 가운데 능력 대조는 이번 제안(q3-03)의 검증 승인 전이며 시뮬레이션 초기값(q3-04) 미답
    - 다른 아이디어와의 연결은 이번 제안(f21·f23 추정)의 검증 승인 전
    - 공간 그래프 스키마 초안의 이번 온톨로지 변경 제안은 검증 승인 전
    - 실험 페이지에 사용자에게 제안하는 실험 계획 없음
    - 열린 질문 q3-04·q3-05·q3-06·q3-07·q3-08·q3-09
