# 리서치 브리프 2026-09-30-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-04 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 16. 장소 의미·지도 관리 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 지도 버전(mapId·mapVersion), 구역 집합(zoneSet), 대체 이름(alt_name), 의미 지도, 3차원 장면 그래프 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(청소 로봇 의미 지도 갱신), 병원(평면도 주요 위치 주석), 기타(로봇 친화형 건축물 정밀지도) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 장소 이름 레지스트리, 지도·구역 집합 버전 배포·활성화, 차선 폐쇄, 지도 변경 감지·갱신, 계층형 의미 지도 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 지도·구역, LIF, IMDF, IEEE 1873, Open-RMF 교통 편집기·LaneRequest, osmAG 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]
2. 장소의 이름·별칭·용도·접근 제한을 표현하는 표준·오픈소스 모델(IMDF, Open-RMF 교통 편집기, LIF, IEEE 1873, 계층형 의미 지도)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)
3. 지도 버전과 임시 통제 구역은 로봇–관제 인터페이스(VDA 5050, Open-RMF)에서 어떻게 배포·활성화·폐기되며 누가 책임지는가? (섹션 6·7·9 겨냥)
4. 공간이 바뀔 때 지도와 장소 의미를 갱신하는 연구와 운영 사례(가정·물류창고·병원 등)는 무엇이며 어떤 결과를 보고하는가? (섹션 5·8 겨냥)
5. 국내 공간정보·건축물 인증 체계는 로봇용 지도·장소 정보를 어떻게 다루는가? (섹션 3·5 겨냥, 한국 자료 우선)
6. 장소 의미·지도 관리에서 ROP가 직접 맡을 것과 로봇 자체 지도 작성·갱신, 건물 데이터 소유자, 설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)
7. oq-193 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추는가? (섹션 5·11 겨냥; oq-188·oq-190 은 11절 반영 대상으로만 확인)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세에서 지도는 작업 공간 구역을 가리키는 mapId 와 갱신을 나타내는 mapVersion 의 조합으로 식별되고 상태는 ENABLED·DISABLED 이며, 관제(fleet control)가 downloadMap·enableMap·deleteMap 즉시 동작으로 지도 서버의 지도를 로봇에 내려받게 하고 활성화하되 같은 mapId 에서는 한 버전만 활성화된다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f2 | [사실] | VDA 5050 3.0.0 명세는 올바른 지도가 활성화되도록 보장하는 책임을 관제에 두고, 로봇이 스스로 지도를 지우지 못하게 하며 사용 중인 지도의 삭제 요청은 로봇이 거부하게 한다. | ref-031 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f3 | [사실] | VDA 5050 3.0.0 명세는 진입 금지(BLOCKED)·유도선 주행(LINE_GUIDED)·해제(RELEASE)·재계획 조율·속도 제한·동작 구역과 우선·벌점·방향 구역을 구역 유형으로 두고, 구역 묶음(zoneSet)은 전역 고유 zoneSetId 를 가지며 mapVersion 이 아니라 mapId 에 묶이고 mapId 당 하나만 활성화되며 내용이 바뀌면 새 zoneSetId 가 필요하다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f4 | [사실] | VDA 5050 3.0.0 명세는 경로·경로망·스테이션 정의 같은 설정을 구현 단계의 일로 보고 명세 범위 밖에 두며, 구현 단계에서 LIF(Layout Interchange Format)로 경로를 관제에 가져올 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDMA 의 LIF 는 무인운반차 통합사업자가 궤도 레이아웃(에지·노드·스테이션의 모음)을 제3자 상위 관제 시스템으로 넘기기 위한 교환 형식이며, 공식 저장소 README 기준 1.0.0 판은 2023-09 에 나왔다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f6 | [사실] | IMDF 의 Unit(실내의 구별되는 공간)은 기능 분류(category)·접근 제한(restriction)·접근성(accessibility)·이름(name)·대체 이름(alt_name)·표시 지점(display_point)·소속 층(level_id)을 속성으로 가지며, 분류에는 승강기·에스컬레이터·계단·경사로·방·화장실·비공개 구역 등이 있다. | ref-1026 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f7 | [사실] | IMDF 용어집에서 이름(name)은 현실에 물리적으로 있고 보행자에게 표시되어야 할 기준 레이블이고, 대체 이름(alt_name)은 공간·물체·서비스를 가리키는 동의어로 색인·질의·검색에 쓰이며, 접근 제한(restriction)은 직원 전용처럼 일반 대중의 일부에게만 허용된 공간을 나타낸다. | ref-1027 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f8 | [사실] | OGC 는 IMDF 1.0.0 을 커뮤니티 표준 20-094 로 2021-02-02 승인하고 2021-02-18 게시했으며, 이 표준은 venue·building·level·unit·opening·fixture·anchor·occupant·geofence 등 16개 지형지물 유형을 정의한다. | ref-1028 | 아니오 | medium | 2021-02-18 | — | — |
| f9 | [사실] | Open-RMF 교통 편집기에서 로봇이 어떤 경유점에서 끝나는 작업을 주려면 그 경유점에 이름을 붙여야 하며, 경유점에는 주차(is_parking_spot)·대기(is_holding_point)·충전(is_charger)·디스펜서·인제스터 같은 속성을 달고, 층별 경유점(좌표·높이·이름)·벽·문·차선을 담은 .building.yaml 을 building_map_generator 로 항법 그래프로 내보내 플릿 어댑터가 쓴다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | Open-RMF 의 차선 요청 메시지(LaneRequest)는 플릿 이름과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어져, 지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 열게 한다. | ref-569 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f11 | [사실] | 에스토니아 타르투 대학병원 현장 시험에서는 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소와 함께 주요 위치를 주석해 로봇 운반 작업의 목적지를 정했고, 이 지도로 중환자실에서 검사실까지 혈액 검체를 운반했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 작업 대상 | 원문 미열람 |
| f12 | [사실] | Narayana 외(IROS 2020)는 실제 가정의 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도(lifelong semantic map)에서, 로봇 원시 지도가 주행마다 달라져도 사용자와 공유하는 의미 정보를 새 지도로 옮기고(공간 의미 전이), 메타 의미 계층으로 동적 물체 때문에 생긴 의미 충돌을 찾아 해소하며, 새로 탐색한 공간의 의미를 찾아 더하는 방법을 제시했다. | ref-1036 | 아니오 | medium | 2020-10 | 가정 / 작업 대상 | — |
| f13 | [사실] | 연계 대상: Stefanini 외(Sensors, 2023)의 LiDAR 점유 격자 지도 갱신 알고리즘은 격자 변화가 여러 스캔에서 반복될 때만(버퍼 10회 중 7회 이상) 지도에 반영하고, 감지된 변화량이 위치 추정 오류가 의심되는 범위이면 갱신을 멈춰 지도 오염을 막으며, 모의 창고 100개 시나리오와 80 m² 실험실에서 갱신 지도로 평균 위치 오차를 10 cm 아래(정적 지도는 50 cm 초과)로 유지했다고 보고했다. | ref-1037 | 아니오 | medium | 2023-07 | 예외·성과 | — |
| f14 | [사실] | Hughes 외(IJRR)는 3차원 장면 그래프를 물체·장소·방·건물 같은 추상화 층으로 환경을 묶는 계층형 공간 표현으로 제시하고, 시각·관성 데이터로 이를 실시간 구축하는 공개 소스 시스템 Hydra 를 Clearpath Jackal·Unitree A1 로봇으로 시험했다. | ref-347 | 아니오 | medium | 2023-05 | — | — |
| f15 | [사실] | Feng 외의 osmAG 는 OpenStreetMap XML 형식 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담는 파일 형식으로, 기존 OSM 도구로 사람이 읽고 고칠 수 있으며 로봇의 이동 방식과 속성을 고려한 전역 경로 계획을 지원하는 ROS 연동 C++ 라이브러리를 함께 제공한다. | ref-1031 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Xie·Schwertfeger·Blum 의 osmAG-LLM(RA-L 2026 채택)은 금방 낡는 고정밀 물체 지도 대신 osmAG 의미 지도를 환경 맥락으로 쓰고 대규모 언어 모델(LLM)이 방 속성 같은 지도 단서로 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 해, 동적·미기록 대상에서 기존 방법보다 나은 탐색 성공을 보고했다. | ref-1032 | 아니오 | medium | 2025-07 | — | — |
| f17 | [사실] | IEEE 1873-2015(Robot Map Data Representation for Navigation)는 항법하는 이동 로봇의 2차원 메트릭·위상 지도에 대한 데이터 모델과 데이터 형식을 정한 IEEE 로봇자동화학회(RAS) 표준으로 2015-09-03 승인·2015-10-26 발행됐으며, 10년 안에 개정되지 않아 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다. | ref-1033 | 아니오 | medium | 2026-03-26 | — | — |
| f18 | [사실] | 지디넷코리아(2022-04-11)에 따르면 네이버 제2사옥 1784 는 스마트도시협회가 처음 실시한 로봇 친화형 건축물 인증(4개 부문·25개 평가 범주)을 받았고, 평가위원은 이 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공하며 이동형 서비스 로봇의 승강기 이동을 지원한다고 평가했다. | ref-956 | 아니오 | low | 2022-04-11 | 기타 / 수행 자원 | — |
| f19 | [사실] | 국토지리정보원은 지하철·철도역사와 평창동계올림픽 관련 시설 등을 대상으로 LoD2 수준의 실내공간정보(2차원 도면·3차원 성과, shp·3ds·max 형식)를 구축해 공간정보 오픈 플랫폼(브이월드)으로 제공하며, 활용처로 길안내·시설물관리·안전·소방을 들고 로봇 활용은 언급하지 않는다. | ref-1035 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에 대해, 같은 이름은 장소마다 고유 식별자·기준 이름·별칭·용도 분류·접근 제한을 둔 장소 목록을 지도 요소(경유점·공간·스테이션)에 묶는 방식으로 표현되고(f6·f7·f9), 공간 변경은 지도 자체의 버전 교체(mapId·mapVersion)와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 나뉘어 관리되는 것으로 보인다(f1·f3·f10). | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇이 만든 원시 지도는 주행과 환경 변화에 따라 계속 달라지는데(f12·f13) 작업 목적지와 사용자 대화는 장소 이름으로 이루어지므로 이름과 지도 요소의 연결을 버전이 바뀌어도 유지해야 하고, VDA 5050 이 올바른 지도 활성화 책임을 관제에 두므로(f2) 여러 제조사 로봇을 묶는 ROP 가 그 책임을 이어받게 되기 때문이다. | ref-1036, ref-1037, ref-031, ref-079 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 16. 장소 의미·지도 관리에서 ROP 가 직접 맡을 범위는 장소 목록(식별자·이름·별칭·용도·접근 제한)의 관리와 제조사별 지도 요소와의 연결(f6·f7·f9), 제조사별 지도·구역 집합의 버전 기록과 배포·활성화 지시(f1·f2·f3), 공사·청소 같은 임시 통제 구역과 차선 폐쇄의 선언·해제(f3·f10), 사람이 층·공간·장소를 고치는 편집 화면과 변경 이력이다. | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM 지도 작성·점유 격자 갱신·장면 그래프 구축 같은 센서 기반 지도 생성(f13·f14)은 로봇 자체 지능·제어에, 공공 실내공간정보·BIM 같은 건물 공간 데이터의 구축·갱신(f19)은 건물·공공 데이터 소유자에, 승강기 운행은 시설·설비 제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 만든 지도·데이터를 받아 장소 의미를 붙이고 버전을 관리하는 인터페이스를 맡을 것으로 보인다. | ref-1037, ref-347, ref-1035, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 기준 평면도를 주는 14. 도면·BIM에서 지도 만들기(f11), 좌표 정렬·공간 그래프를 다루는 15. 지도·공간·위치 모델(f9·f15), 대화로 지도를 고치고 장소 이름을 찾는 8. 채팅으로 맵 작성과 12. 채팅으로 업무 지시·오케스트레이션(f7·f16), 현재 활성 지도 버전·폐쇄 구역을 알아야 하는 18. 실시간 세계 상태·데이터 일관성(f1·f10), 차선 폐쇄를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f10), 지도 교환 표준을 다루는 21. 상호운용 표준·적합성(f5·f8·f17), 버전 이력을 다루는 57. 자산·소프트웨어 수명주기 관리(f1), 접근 제한 공간을 다루는 51. 인증·권한·격리(f7), 장면 이해를 다루는 45. 문서·도면·장면 이해(f14·f16), 적용 현장인 63. 병원·의료(f11)·65. 가정·공동주택(f12)·67. 기타 현장(f18)과 이어진다. | ref-869, ref-079, ref-1031, ref-1027, ref-1032, ref-031, ref-569, ref-046, ref-1028, ref-1033, ref-347, ref-1036, ref-956 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

- **f1**: 6.3절: 지도 파일은 로봇이 접근하는 전용 지도 서버에 두고, 내려받은 지도는 DISABLED 로 상태에 추가되며 enableMap 이 같은 mapId 의 다른 버전을 비활성화한다. 모르는 mapId 를 참조한 주문은 UNKNOWN_MAP_ID 로 거부된다. (발행일 미확인, 확인일 기준)
- **f2**: 6.3.1절: "It is the responsibility of the fleet control to ensure that the correct maps are enabled". 6.3.5절: 로봇 자신은 지도를 삭제하지 않고, 사용 중인 지도의 deleteMap 은 거부한다. (발행일 미확인, 확인일 기준)
- **f3**: 6.4절: 구역 집합은 MQTT zoneSet 토픽 또는 downloadZoneSet 으로 배포하고 enableZoneSet·deleteZoneSet 으로 관리한다. 같은 zoneSetId 를 다시 받으면 DUPLICATE_ZONE_SET 경고로 거부한다. BLOCKED 구역 침범은 치명 오류다. (발행일 미확인, 확인일 기준)
- **f4**: 5.2절: LIF 로 경로를 관제에 가져올 수 있고, 경로·경로망 구성은 이 문서의 일부가 아니며 관제 주문 논리의 기반이 된다. 운영 단계의 변경은 MQTT 통신으로 다룬다. (발행일 미확인, 확인일 기준)
- **f5**: README: "An interchange format for a track layout (e.g.: collection of edges, nodes and stations)". 발행 주체 VDMA, Version 1.0.0(2023-09). 필드 목록(layoutVersion·stationName 등)은 README 에 없어 확인하지 못함.
- **f6**: Unit 속성 7개(category, restriction, accessibility, name, alt_name, display_point, level_id). name·alt_name 은 다국어 레이블이며 예시는 {"en": "Ball Room"}. 분류 예: elevator, escalator, stairs, ramp, room, restroom, nonpublic. (발행일 미확인, 확인일 기준)
- **f7**: alt_name 은 "intended to be indexed, enable queries, and support the retrieval of a predetermined label" 이고, name 은 현실에 있는 것을 반영하는 기준값(ground truth)이다. (발행일 미확인, 확인일 기준)
- **f8**: OGC Community Standard 20-094, IMDF 1.0.0. 16개 유형: venue, building, footprint, level, unit, fixture, section, geofence, kiosk, detail, opening, amenity, anchor, occupant, address, relationship.
- **f9**: "to issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint". 경유점은 x, y, 높이, 이름, 추가 매개변수 목록으로 저장된다. (발행일 미확인, 확인일 기준)
- **f10**: LaneRequest.msg: string fleet_name, uint64[] open_lanes, uint64[] close_lanes. 메시지 정의에 설명 주석은 없다. (발행일 미확인, 확인일 기준)
- **f11**: TIAGo 로 만든 격자 지도를 평면도에 정합하고 평면도에 벽·문·차선·충전소·주요 위치를 주석했다. (재인용: 2026-09-30-03)
- **f12**: 의미 지도를 로봇과 사용자의 공유 표현으로 보고, 지도 흔들림·동적 물체·새 공간 편입 문제를 다룬다. 배포 규모는 "thousands of floor-cleaning robots in real homes". 초록 기준.
- **f13**: Gazebo 모의 창고(Robotnik XL-Steel, SICK LiDAR) 100개 단계 시나리오와 실험실 4개 구성에서 평가. 지도 품질 지표 약 20~40% 개선, CPU 10~13%, 메모리 약 57.5 MB. 저자 보고 수치.
- **f14**: 평면적인 메트릭-의미 지도는 넓은 환경과 큰 의미 레이블 사전으로 확장되지 않는다는 문제에서 출발해, 층 구조 그래프로 저장·추론 비용을 관리한다. 초록 기준.
- **f15**: "hierarchical, topometric semantic multi-floor maps of indoor and outdoor environments"를 저장하는 형식. 독점 소프트웨어 없이 편집 가능. 초록 기준.
- **f16**: 기하 지도를 시각-언어 특징으로 보강하고 LLM 이 이를 환경 단서로 삼는다. 코드·데이터 공개. 초록 기준, 수치는 확인하지 않음.
- **f17**: 범위: "data models and data formats for two-dimensional (2D) metric and topological maps". 상태: Inactive-Reserved Standard(2026-03-26 행정 처리).
- **f18**: 인증지표 4개 부문: 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스. 평가위원 언급: 로봇이 인식하는 정밀지도와 측위 인프라 제공.
- **f19**: 실내공간정보: "지상 또는 지하에 존재하는 건물 등 인공구조물의 내부에 관한 공간정보". 브이월드에 탑재해 공공·민간에 제공. (발행일 미확인, 확인일 기준)
- **f20**: IMDF name·alt_name·category·restriction, Open-RMF 이름 붙은 경유점, VDA 5050 지도 버전과 mapId 에 묶인 zoneSet, Open-RMF LaneRequest 를 종합한 해석.
- **f21**: 가정용 청소 로봇의 의미 전이 문제(f12), 산업 현장 정적 지도 노후화(f13), 관제의 지도 활성화 책임(f2), 이름 붙은 경유점만 작업 목적지가 되는 구조(f9)를 종합한 해석.
- **f22**: VDA 5050 이 관제에 둔 지도·구역 배포 책임과 Open-RMF 교통 편집기·LaneRequest, IMDF 장소 속성을 ROP 역할로 옮겨 본 해석.
- **f23**: VDA 5050 에서 지도 파일 자체는 지도 서버에 두고 관제는 배포·활성화만 지시하는 구조(f1)와 로봇 측 지도 갱신 연구(f13)를 대비한 해석.
- **f24**: 각 finding 의 대상 기능을 세부영역 정의에 대응시킨 해석. L. AI·학습 기술 관련(f14·f16)은 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성 양쪽에 연결.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-1026 | Apple (Apple Business Register) | Unit - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/types/unit | 아니오 |
| ref-1027 | Apple (Apple Business Register) | Glossary - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/glossary | 아니오 |
| ref-1028 | Open Geospatial Consortium (OGC) | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 2021-02-18 | 표준 | high | 2026-09-30 | https://docs.ogc.org/cs/20-094/index.html | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (IJRR) | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 2023-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2305.07154 | 아니오 |
| ref-1031 | Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv) | osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics | 2023-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2309.04791 | 아니오 |
| ref-1032 | Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv) | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.12753 | 아니오 |
| ref-1033 | IEEE Standards Association (IEEE RAS) | IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation | 2015-10-26 | 표준 | medium | 2026-09-30 | https://standards.ieee.org/standard/1873-2015.html | 아니오 |
| ref-956 | 지디넷코리아 | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 2022-04-11 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20220411142336 | 아니오 |
| ref-1035 | 국토지리정보원 | 실내공간정보 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.ngii.go.kr/kor/content.do?sq=324 | 아니오 |
| ref-1036 | Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020) | Lifelong update of semantic maps in dynamic environments | 2020-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2010.08846 | 아니오 |
| ref-1037 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066) | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 2023-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/ | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 공식 저장소 main 브랜치의 명세 원문(3.0.0). 이번 실행에서 지도(mapId·mapVersion·downloadMap·enableMap·deleteMap), 구역 집합(zoneSet), LIF 언급 절을 다시 확인했다.
- **ref-079**: Open-RMF 교통 편집기 문서. 이번 실행에서 경유점 이름 규칙, 경유점 속성, .building.yaml 구조와 항법 그래프 내보내기를 확인했다.
- **ref-869**: 타르투 대학병원 이기종 로봇 플릿 현장 시험. 평면도 주석과 격자 지도 정합, 검체 운반 사례. 이번 실행에서는 다시 열지 않고 2026-09-30-03 브리프를 재인용했다.
- **ref-046**: VDMA 의 궤도 레이아웃 교환 형식 LIF 공식 저장소 README. 목적(통합사업자→제3자 상위 관제로 에지·노드·스테이션 전달)과 1.0.0 판(2023-09)을 확인했다. 스키마 필드는 README 에 없어 확인하지 못했다.
- **ref-1026**: IMDF Unit 유형 참조 문서. 속성(category, restriction, accessibility, name, alt_name, display_point, level_id)과 분류값을 규정한다.
- **ref-1027**: IMDF 용어집. name(기준 레이블), alt_name(색인·검색용 동의어), Unit, Level, Anchor, Venue, Restriction 을 정의한다.
- **ref-1028**: OGC 가 커뮤니티 표준으로 승인(2021-02-02)·게시(2021-02-18)한 IMDF 1.0.0. 16개 지형지물 유형을 정의한다.
- **ref-569**: Open-RMF 차선 열기·닫기 요청 메시지 정의(fleet_name, open_lanes, close_lanes).
- **ref-347**: 계층형 3차원 장면 그래프(물체·장소·방·건물)와 실시간 구축 시스템 Hydra 를 제시한 논문의 arXiv 초록. 본문은 열지 않았다.
- **ref-1031**: OpenStreetMap XML 기반 계층형 위상·거리 의미 지도 형식 osmAG 와 ROS 연동 라이브러리. 초록 기준.
- **ref-1032**: osmAG 의미 지도를 환경 맥락으로 삼아 LLM 이 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 한 방법. 초록 기준.
- **ref-1033**: IEEE SA 표준 소개 페이지. 2D 메트릭·위상 지도 데이터 모델·형식 범위, 승인·발행일, 2026-03-26 비활성 보류 상태를 확인했다. 유료 표준 본문은 열지 않았다.
- **ref-956**: 네이버 1784 의 로봇 친화형 건축물 인증 획득 보도. 인증지표 구성과 정밀지도·측위 인프라에 대한 평가위원 언급.
- **ref-1035**: 국토지리정보원의 실내공간정보 소개. 정의, 구축 대상(지하철·철도역사 등), LoD2, 자료 형식, 브이월드 제공.
- **ref-1036**: 가정용 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도의 의미 전이·충돌 감지·새 의미 발견 방법. 초록 기준.
- **ref-1037**: 산업 물류 환경용 LiDAR 점유 격자 지도 안전 갱신 알고리즘. 반복 확인·위치 추정 의심 시 갱신 중지, 모의 창고·실험실 평가. PMC 본문 열람.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(원시 지도 변화와 이름 기반 작업·관제 책임), f20(핵심 질문 답, 추정) / 섹션 4: 지도 버전 f1, 구역 집합 f3, 이름·대체 이름·접근 제한 f6·f7, 의미 지도 f12, 3차원 장면 그래프 f14 / 섹션 5: 병원 — f11(타르투 대학병원 평면도 주요 위치 주석, 재인용), 가정 — f12(청소 로봇 의미 지도 갱신), 기타 — f18(네이버 1784 정밀지도·측위 인프라, 기사 기준 신뢰도 low). 여섯 항목 중 시작 조건·완료·인계 근거는 부족함을 명시. 물류창고 사례는 모의 실험(f13)뿐이라 현장 사례로 쓰지 않음 / 섹션 6: 장소 목록과 지도 요소 연결 f6·f7·f9, 지도 버전 배포·활성화 f1·f2, 임시 통제 구역 f3·차선 폐쇄 f10, 지도 변경 감지·갱신 f13(연계 대상), 평생 의미 지도 f12, 계층형 의미 지도 f14·f15, LLM 과 의미 지도 f16 / 섹션 7: VDA 5050 f1~f4, LIF f5, IMDF f6~f8, Open-RMF f9·f10, IEEE 1873 f17(비활성 보류 명시), osmAG f15 / 섹션 8: f12~f16, f19(국내 공공 실내공간정보) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 8, 12, 14, 15, 18, 21, 27, 45, 51, 57, 63, 65, 67 / 섹션 11: 기존 oq-188·oq-190·oq-193 과 open_questions_new 5건. 다음 실행 후보: 21. 상호운용 표준·적합성 페이지에 f5·f8·f17 반영, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 지도 버전 | Map Version (VDA 5050 mapId / mapVersion) | 같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 에서는 관제가 내려받게 한 여러 버전 가운데 한 버전만 활성화해 로봇이 쓰게 한다. |
| 대체 이름 | Alternative Name (IMDF alt_name) | IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다. |
| 의미 지도 | Semantic Map | 기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다. |
| 3차원 장면 그래프 | 3D Scene Graph | 물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다. |

## 열린 질문

새로 생긴 질문:

- 제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 15. 지도·공간·위치 모델 | 근거: f1 | 종류: 일반
- IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성 | 근거: f17 | 종류: 일반
- 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 40. 운영 절차·요청 창구, 63. 병원·의료 | 근거: f3 | 종류: 일반
- IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 12. 채팅으로 업무 지시·오케스트레이션 | 근거: f7 | 종류: 일반
- 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 67. 기타 현장 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 13건
- 미확인 항목:
    - f5 LIF 스키마의 layoutVersion·stationName 등 필드는 검색 요약에만 나와 README·스키마 원문으로 확인하지 못함(GitHub 저장소 페이지 403, VDMA 가이드라인 PDF 본문 추출 실패)
    - f13 수치는 저자 보고이며 교차 확인 실패
    - f14·f15·f16·f12 는 초록 기준이며 본문 실험 조건 미확인
    - f17 IEEE 1873 표준 본문(유료) 미열람, Amigoni 외 해설 논문(oru.diva-portal.org)은 ECONNRESET 으로 열지 못함
    - f18 기사 기준이며 스마트도시협회 인증 원자료 미확인
    - Nav2 금지 구역·속도 필터(costmap filter) 문서는 docs.nav2.org·raw 경로 404, navigation.ros.org 연결 거부로 열지 못해 넣지 않음
    - MiR 지도 편집기(바닥 계층과 구역·위치 구성 요소, 로봇 수 제한 구역)는 PDF 본문 추출 실패로 넣지 않음
    - oq-193 건설 현장 지도–BIM 동기화 주기는 이번 조사에서도 확인되지 않음
    - oq-188·oq-190 은 조사하지 않음(11절 반영 대상으로만 둠)
    - 물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례는 확인하지 못함
- 범위 경계 위반 의심:
    - f13: 로봇 점유 격자 지도 갱신은 분류 원문 19장의 로봇 자체 지능·제어(SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 장면 그래프를 센서로 구축하는 부분은 로봇 인식(연계 대상)이며 계층형 표현 구조만 이 영역 근거로 쓰도록 제안함(f23 에서 구분)
    - f19: 공공 실내공간정보 구축은 공공 데이터 소유자의 일이므로 입력 데이터 가용성 근거로만 제안함
    - f23: SLAM·건물 데이터 구축·승강기 운행을 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 18회/30, 신규 출처 13건/15, 재사용 3건(ref-031·ref-079 는 github_raw 로 다시 열었고 ref-869 는 2026-09-30-03 브리프 재인용으로 이번에 열지 않음). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1014 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-03)가 ref-1015·ref-1017·ref-1019·ref-1024 를 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-046~ref-1037 을 순서대로 썼다. 원문 열람: 신규 13건 모두 열었다(webfetch 11건, github_raw 2건). 논문은 대부분 초록 페이지이고 Stefanini 외(ref-1037)만 PMC 본문을 열었다. 열지 못해 쓰지 않은 것: Nav2 문서(404·연결 거부), MiR Fleet 참조 안내서 PDF(본문 추출 실패), VDMA LIF 가이드라인 PDF(본문 추출 실패), LIF GitHub 저장소 페이지(403), MDPI·preprints.org(403), IEEE 1873 해설 논문(ECONNRESET). 교차 확인 0건, 신뢰도 high finding 없음(사실 finding 은 모두 단일 출처; IMDF 는 Apple 문서와 OGC 게시본이 같은 원천이라 독립 출처로 보지 않음). 분류 원문 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에는 f20 으로 답했고, 결론은 '장소 목록을 지도 요소에 묶고, 지도 버전 교체와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 변경을 나눠 관리한다'는 추정이다. 현장 유형 사례는 병원(f11, 재인용)·가정(f12)·기타(f18)이며, 물류창고 근거는 모의 실험(f13)뿐이라 site_type 을 null 로 두었다. 국내 자료는 국토지리정보원(ref-1035)·지디넷코리아(ref-956) 두 건이며 국내 로봇 지도 표준(KS)은 검색 2회에서 찾지 못했다. L. AI·학습 기술 관련(f14 장면 그래프, f16 LLM 추론)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 활성 지도 버전·폐쇄 구역으로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 IMDF·IndoorGML·LIF·구역 집합·차선 폐쇄·필터 마스크·위상 지도·반정적 객체·공간 그래프는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다.
