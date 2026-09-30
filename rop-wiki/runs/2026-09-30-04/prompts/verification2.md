(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-04
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 16. 장소 의미·지도 관리 (D. 공간·지도 모델)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-30-04/target.json

```json
{
  "run_id": "2026-09-30-04",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 113,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 16,
    "area_name": "16. 장소 의미·지도 관리",
    "category": "D. 공간·지도 모델",
    "category_letter": "D"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=16"
}
```

### runs/2026-09-30-04/research.json

```json
{
  "run_id": "2026-09-30-04",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 16,
    "area_name": "16. 장소 의미·지도 관리",
    "category": "D. 공간·지도 모델"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 지도 버전(mapId·mapVersion), 구역 집합(zoneSet), 대체 이름(alt_name), 의미 지도, 3차원 장면 그래프 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(청소 로봇 의미 지도 갱신), 병원(평면도 주요 위치 주석), 기타(로봇 친화형 건축물 정밀지도) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 장소 이름 레지스트리, 지도·구역 집합 버전 배포·활성화, 차선 폐쇄, 지도 변경 감지·갱신, 계층형 의미 지도 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 지도·구역, LIF, IMDF, IEEE 1873, Open-RMF 교통 편집기·LaneRequest, osmAG 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 반영 안 됨",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]",
    "장소의 이름·별칭·용도·접근 제한을 표현하는 표준·오픈소스 모델(IMDF, Open-RMF 교통 편집기, LIF, IEEE 1873, 계층형 의미 지도)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)",
    "지도 버전과 임시 통제 구역은 로봇–관제 인터페이스(VDA 5050, Open-RMF)에서 어떻게 배포·활성화·폐기되며 누가 책임지는가? (섹션 6·7·9 겨냥)",
    "공간이 바뀔 때 지도와 장소 의미를 갱신하는 연구와 운영 사례(가정·물류창고·병원 등)는 무엇이며 어떤 결과를 보고하는가? (섹션 5·8 겨냥)",
    "국내 공간정보·건축물 인증 체계는 로봇용 지도·장소 정보를 어떻게 다루는가? (섹션 3·5 겨냥, 한국 자료 우선)",
    "장소 의미·지도 관리에서 ROP가 직접 맡을 것과 로봇 자체 지도 작성·갱신, 건물 데이터 소유자, 설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)",
    "oq-193 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추는가? (섹션 5·11 겨냥; oq-188·oq-190 은 11절 반영 대상으로만 확인)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 명세에서 지도는 작업 공간 구역을 가리키는 mapId 와 갱신을 나타내는 mapVersion 의 조합으로 식별되고 상태는 ENABLED·DISABLED 이며, 관제(fleet control)가 downloadMap·enableMap·deleteMap 즉시 동작으로 지도 서버의 지도를 로봇에 내려받게 하고 활성화하되 같은 mapId 에서는 한 버전만 활성화된다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.3절: 지도 파일은 로봇이 접근하는 전용 지도 서버에 두고, 내려받은 지도는 DISABLED 로 상태에 추가되며 enableMap 이 같은 mapId 의 다른 버전을 비활성화한다. 모르는 mapId 를 참조한 주문은 UNKNOWN_MAP_ID 로 거부된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 명세는 올바른 지도가 활성화되도록 보장하는 책임을 관제에 두고, 로봇이 스스로 지도를 지우지 못하게 하며 사용 중인 지도의 삭제 요청은 로봇이 거부하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.3.1절: \"It is the responsibility of the fleet control to ensure that the correct maps are enabled\". 6.3.5절: 로봇 자신은 지도를 삭제하지 않고, 사용 중인 지도의 deleteMap 은 거부한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 명세는 진입 금지(BLOCKED)·유도선 주행(LINE_GUIDED)·해제(RELEASE)·재계획 조율·속도 제한·동작 구역과 우선·벌점·방향 구역을 구역 유형으로 두고, 구역 묶음(zoneSet)은 전역 고유 zoneSetId 를 가지며 mapVersion 이 아니라 mapId 에 묶이고 mapId 당 하나만 활성화되며 내용이 바뀌면 새 zoneSetId 가 필요하다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.4절: 구역 집합은 MQTT zoneSet 토픽 또는 downloadZoneSet 으로 배포하고 enableZoneSet·deleteZoneSet 으로 관리한다. 같은 zoneSetId 를 다시 받으면 DUPLICATE_ZONE_SET 경고로 거부한다. BLOCKED 구역 침범은 치명 오류다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 명세는 경로·경로망·스테이션 정의 같은 설정을 구현 단계의 일로 보고 명세 범위 밖에 두며, 구현 단계에서 LIF(Layout Interchange Format)로 경로를 관제에 가져올 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.2절: LIF 로 경로를 관제에 가져올 수 있고, 경로·경로망 구성은 이 문서의 일부가 아니며 관제 주문 논리의 기반이 된다. 운영 단계의 변경은 MQTT 통신으로 다룬다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDMA 의 LIF 는 무인운반차 통합사업자가 궤도 레이아웃(에지·노드·스테이션의 모음)을 제3자 상위 관제 시스템으로 넘기기 위한 교환 형식이며, 공식 저장소 README 기준 1.0.0 판은 2023-09 에 나왔다.",
      "tag": "사실",
      "source_ids": [
        "ref-046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"An interchange format for a track layout (e.g.: collection of edges, nodes and stations)\". 발행 주체 VDMA, Version 1.0.0(2023-09). 필드 목록(layoutVersion·stationName 등)은 README 에 없어 확인하지 못함.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "IMDF 의 Unit(실내의 구별되는 공간)은 기능 분류(category)·접근 제한(restriction)·접근성(accessibility)·이름(name)·대체 이름(alt_name)·표시 지점(display_point)·소속 층(level_id)을 속성으로 가지며, 분류에는 승강기·에스컬레이터·계단·경사로·방·화장실·비공개 구역 등이 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1026"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Unit 속성 7개(category, restriction, accessibility, name, alt_name, display_point, level_id). name·alt_name 은 다국어 레이블이며 예시는 {\"en\": \"Ball Room\"}. 분류 예: elevator, escalator, stairs, ramp, room, restroom, nonpublic. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f7",
      "claim": "IMDF 용어집에서 이름(name)은 현실에 물리적으로 있고 보행자에게 표시되어야 할 기준 레이블이고, 대체 이름(alt_name)은 공간·물체·서비스를 가리키는 동의어로 색인·질의·검색에 쓰이며, 접근 제한(restriction)은 직원 전용처럼 일반 대중의 일부에게만 허용된 공간을 나타낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1027"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "alt_name 은 \"intended to be indexed, enable queries, and support the retrieval of a predetermined label\" 이고, name 은 현실에 있는 것을 반영하는 기준값(ground truth)이다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f8",
      "claim": "OGC 는 IMDF 1.0.0 을 커뮤니티 표준 20-094 로 2021-02-02 승인하고 2021-02-18 게시했으며, 이 표준은 venue·building·level·unit·opening·fixture·anchor·occupant·geofence 등 16개 지형지물 유형을 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1028"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OGC Community Standard 20-094, IMDF 1.0.0. 16개 유형: venue, building, footprint, level, unit, fixture, section, geofence, kiosk, detail, opening, amenity, anchor, occupant, address, relationship.",
      "as_of": "2021-02-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF 교통 편집기에서 로봇이 어떤 경유점에서 끝나는 작업을 주려면 그 경유점에 이름을 붙여야 하며, 경유점에는 주차(is_parking_spot)·대기(is_holding_point)·충전(is_charger)·디스펜서·인제스터 같은 속성을 달고, 층별 경유점(좌표·높이·이름)·벽·문·차선을 담은 .building.yaml 을 building_map_generator 로 항법 그래프로 내보내 플릿 어댑터가 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"to issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint\". 경유점은 x, y, 높이, 이름, 추가 매개변수 목록으로 저장된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f10",
      "claim": "Open-RMF 의 차선 요청 메시지(LaneRequest)는 플릿 이름과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어져, 지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 열게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-569"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LaneRequest.msg: string fleet_name, uint64[] open_lanes, uint64[] close_lanes. 메시지 정의에 설명 주석은 없다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "에스토니아 타르투 대학병원 현장 시험에서는 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소와 함께 주요 위치를 주석해 로봇 운반 작업의 목적지를 정했고, 이 지도로 중환자실에서 검사실까지 혈액 검체를 운반했다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TIAGo 로 만든 격자 지도를 평면도에 정합하고 평면도에 벽·문·차선·충전소·주요 위치를 주석했다. (재인용: 2026-09-30-03)",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "Narayana 외(IROS 2020)는 실제 가정의 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도(lifelong semantic map)에서, 로봇 원시 지도가 주행마다 달라져도 사용자와 공유하는 의미 정보를 새 지도로 옮기고(공간 의미 전이), 메타 의미 계층으로 동적 물체 때문에 생긴 의미 충돌을 찾아 해소하며, 새로 탐색한 공간의 의미를 찾아 더하는 방법을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1036"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "의미 지도를 로봇과 사용자의 공유 표현으로 보고, 지도 흔들림·동적 물체·새 공간 편입 문제를 다룬다. 배포 규모는 \"thousands of floor-cleaning robots in real homes\". 초록 기준.",
      "as_of": "2020-10",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f13",
      "claim": "연계 대상: Stefanini 외(Sensors, 2023)의 LiDAR 점유 격자 지도 갱신 알고리즘은 격자 변화가 여러 스캔에서 반복될 때만(버퍼 10회 중 7회 이상) 지도에 반영하고, 감지된 변화량이 위치 추정 오류가 의심되는 범위이면 갱신을 멈춰 지도 오염을 막으며, 모의 창고 100개 시나리오와 80 m² 실험실에서 갱신 지도로 평균 위치 오차를 10 cm 아래(정적 지도는 50 cm 초과)로 유지했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Gazebo 모의 창고(Robotnik XL-Steel, SICK LiDAR) 100개 단계 시나리오와 실험실 4개 구성에서 평가. 지도 품질 지표 약 20~40% 개선, CPU 10~13%, 메모리 약 57.5 MB. 저자 보고 수치.",
      "as_of": "2023-07",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "Hughes 외(IJRR)는 3차원 장면 그래프를 물체·장소·방·건물 같은 추상화 층으로 환경을 묶는 계층형 공간 표현으로 제시하고, 시각·관성 데이터로 이를 실시간 구축하는 공개 소스 시스템 Hydra 를 Clearpath Jackal·Unitree A1 로봇으로 시험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-347"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "평면적인 메트릭-의미 지도는 넓은 환경과 큰 의미 레이블 사전으로 확장되지 않는다는 문제에서 출발해, 층 구조 그래프로 저장·추론 비용을 관리한다. 초록 기준.",
      "as_of": "2023-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Feng 외의 osmAG 는 OpenStreetMap XML 형식 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담는 파일 형식으로, 기존 OSM 도구로 사람이 읽고 고칠 수 있으며 로봇의 이동 방식과 속성을 고려한 전역 경로 계획을 지원하는 ROS 연동 C++ 라이브러리를 함께 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"hierarchical, topometric semantic multi-floor maps of indoor and outdoor environments\"를 저장하는 형식. 독점 소프트웨어 없이 편집 가능. 초록 기준.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Xie·Schwertfeger·Blum 의 osmAG-LLM(RA-L 2026 채택)은 금방 낡는 고정밀 물체 지도 대신 osmAG 의미 지도를 환경 맥락으로 쓰고 대규모 언어 모델(LLM)이 방 속성 같은 지도 단서로 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 해, 동적·미기록 대상에서 기존 방법보다 나은 탐색 성공을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기하 지도를 시각-언어 특징으로 보강하고 LLM 이 이를 환경 단서로 삼는다. 코드·데이터 공개. 초록 기준, 수치는 확인하지 않음.",
      "as_of": "2025-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "IEEE 1873-2015(Robot Map Data Representation for Navigation)는 항법하는 이동 로봇의 2차원 메트릭·위상 지도에 대한 데이터 모델과 데이터 형식을 정한 IEEE 로봇자동화학회(RAS) 표준으로 2015-09-03 승인·2015-10-26 발행됐으며, 10년 안에 개정되지 않아 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1033"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "범위: \"data models and data formats for two-dimensional (2D) metric and topological maps\". 상태: Inactive-Reserved Standard(2026-03-26 행정 처리).",
      "as_of": "2026-03-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "지디넷코리아(2022-04-11)에 따르면 네이버 제2사옥 1784 는 스마트도시협회가 처음 실시한 로봇 친화형 건축물 인증(4개 부문·25개 평가 범주)을 받았고, 평가위원은 이 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공하며 이동형 서비스 로봇의 승강기 이동을 지원한다고 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-956"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "인증지표 4개 부문: 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스. 평가위원 언급: 로봇이 인식하는 정밀지도와 측위 인프라 제공.",
      "as_of": "2022-04-11",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f19",
      "claim": "국토지리정보원은 지하철·철도역사와 평창동계올림픽 관련 시설 등을 대상으로 LoD2 수준의 실내공간정보(2차원 도면·3차원 성과, shp·3ds·max 형식)를 구축해 공간정보 오픈 플랫폼(브이월드)으로 제공하며, 활용처로 길안내·시설물관리·안전·소방을 들고 로봇 활용은 언급하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1035"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실내공간정보: \"지상 또는 지하에 존재하는 건물 등 인공구조물의 내부에 관한 공간정보\". 브이월드에 탑재해 공공·민간에 제공. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에 대해, 같은 이름은 장소마다 고유 식별자·기준 이름·별칭·용도 분류·접근 제한을 둔 장소 목록을 지도 요소(경유점·공간·스테이션)에 묶는 방식으로 표현되고(f6·f7·f9), 공간 변경은 지도 자체의 버전 교체(mapId·mapVersion)와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 나뉘어 관리되는 것으로 보인다(f1·f3·f10).",
      "tag": "추정",
      "source_ids": [
        "ref-1026",
        "ref-1027",
        "ref-079",
        "ref-031",
        "ref-569"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "IMDF name·alt_name·category·restriction, Open-RMF 이름 붙은 경유점, VDA 5050 지도 버전과 mapId 에 묶인 zoneSet, Open-RMF LaneRequest 를 종합한 해석.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇이 만든 원시 지도는 주행과 환경 변화에 따라 계속 달라지는데(f12·f13) 작업 목적지와 사용자 대화는 장소 이름으로 이루어지므로 이름과 지도 요소의 연결을 버전이 바뀌어도 유지해야 하고, VDA 5050 이 올바른 지도 활성화 책임을 관제에 두므로(f2) 여러 제조사 로봇을 묶는 ROP 가 그 책임을 이어받게 되기 때문이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1036",
        "ref-1037",
        "ref-031",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "가정용 청소 로봇의 의미 전이 문제(f12), 산업 현장 정적 지도 노후화(f13), 관제의 지도 활성화 책임(f2), 이름 붙은 경유점만 작업 목적지가 되는 구조(f9)를 종합한 해석.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 16. 장소 의미·지도 관리에서 ROP 가 직접 맡을 범위는 장소 목록(식별자·이름·별칭·용도·접근 제한)의 관리와 제조사별 지도 요소와의 연결(f6·f7·f9), 제조사별 지도·구역 집합의 버전 기록과 배포·활성화 지시(f1·f2·f3), 공사·청소 같은 임시 통제 구역과 차선 폐쇄의 선언·해제(f3·f10), 사람이 층·공간·장소를 고치는 편집 화면과 변경 이력이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1026",
        "ref-1027",
        "ref-079",
        "ref-031",
        "ref-569"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 이 관제에 둔 지도·구역 배포 책임과 Open-RMF 교통 편집기·LaneRequest, IMDF 장소 속성을 ROP 역할로 옮겨 본 해석.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM 지도 작성·점유 격자 갱신·장면 그래프 구축 같은 센서 기반 지도 생성(f13·f14)은 로봇 자체 지능·제어에, 공공 실내공간정보·BIM 같은 건물 공간 데이터의 구축·갱신(f19)은 건물·공공 데이터 소유자에, 승강기 운행은 시설·설비 제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 만든 지도·데이터를 받아 장소 의미를 붙이고 버전을 관리하는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1037",
        "ref-347",
        "ref-1035",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 에서 지도 파일 자체는 지도 서버에 두고 관제는 배포·활성화만 지시하는 구조(f1)와 로봇 측 지도 갱신 연구(f13)를 대비한 해석.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "이 영역은 기준 평면도를 주는 14. 도면·BIM에서 지도 만들기(f11), 좌표 정렬·공간 그래프를 다루는 15. 지도·공간·위치 모델(f9·f15), 대화로 지도를 고치고 장소 이름을 찾는 8. 채팅으로 맵 작성과 12. 채팅으로 업무 지시·오케스트레이션(f7·f16), 현재 활성 지도 버전·폐쇄 구역을 알아야 하는 18. 실시간 세계 상태·데이터 일관성(f1·f10), 차선 폐쇄를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f10), 지도 교환 표준을 다루는 21. 상호운용 표준·적합성(f5·f8·f17), 버전 이력을 다루는 57. 자산·소프트웨어 수명주기 관리(f1), 접근 제한 공간을 다루는 51. 인증·권한·격리(f7), 장면 이해를 다루는 45. 문서·도면·장면 이해(f14·f16), 적용 현장인 63. 병원·의료(f11)·65. 가정·공동주택(f12)·67. 기타 현장(f18)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-869",
        "ref-079",
        "ref-1031",
        "ref-1027",
        "ref-1032",
        "ref-031",
        "ref-569",
        "ref-046",
        "ref-1028",
        "ref-1033",
        "ref-347",
        "ref-1036",
        "ref-956"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 의 대상 기능을 세부영역 정의에 대응시킨 해석. L. AI·학습 기술 관련(f14·f16)은 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성 양쪽에 연결.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 저장소 main 브랜치의 명세 원문(3.0.0). 이번 실행에서 지도(mapId·mapVersion·downloadMap·enableMap·deleteMap), 구역 집합(zoneSet), LIF 언급 절을 다시 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 교통 편집기 문서. 이번 실행에서 경유점 이름 규칙, 경유점 속성, .building.yaml 구조와 항법 그래프 내보내기를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R. 외 (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원 이기종 로봇 플릿 현장 시험. 평면도 주석과 격자 지도 정합, 검체 운반 사례. 이번 실행에서는 다시 열지 않고 2026-09-30-03 브리프를 재인용했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF)",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDMA 의 궤도 레이아웃 교환 형식 LIF 공식 저장소 README. 목적(통합사업자→제3자 상위 관제로 에지·노드·스테이션 전달)과 1.0.0 판(2023-09)을 확인했다. 스키마 필드는 README 에 없어 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Intralogistics-2X-LIF/Layout-Interchange-Format/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1026",
      "org": "Apple (Apple Business Register)",
      "title": "Unit - Indoor Mapping Data Format",
      "published": null,
      "url": "https://register.apple.com/resources/imdf/types/unit",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "IMDF Unit 유형 참조 문서. 속성(category, restriction, accessibility, name, alt_name, display_point, level_id)과 분류값을 규정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1027",
      "org": "Apple (Apple Business Register)",
      "title": "Glossary - Indoor Mapping Data Format",
      "published": null,
      "url": "https://register.apple.com/resources/imdf/glossary",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "IMDF 용어집. name(기준 레이블), alt_name(색인·검색용 동의어), Unit, Level, Anchor, Venue, Restriction 을 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1028",
      "org": "Open Geospatial Consortium (OGC)",
      "title": "Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094",
      "published": "2021-02-18",
      "url": "https://docs.ogc.org/cs/20-094/index.html",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "OGC 가 커뮤니티 표준으로 승인(2021-02-02)·게시(2021-02-18)한 IMDF 1.0.0. 16개 지형지물 유형을 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-569",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 차선 열기·닫기 요청 메시지 정의(fleet_name, open_lanes, close_lanes).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "source_unopened": false
    },
    {
      "id": "ref-347",
      "org": "Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (IJRR)",
      "title": "Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems",
      "published": "2023-05",
      "url": "https://arxiv.org/abs/2305.07154",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "계층형 3차원 장면 그래프(물체·장소·방·건물)와 실시간 구축 시스템 Hydra 를 제시한 논문의 arXiv 초록. 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1031",
      "org": "Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv)",
      "title": "osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.04791",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OpenStreetMap XML 기반 계층형 위상·거리 의미 지도 형식 osmAG 와 ROS 연동 라이브러리. 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1032",
      "org": "Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv)",
      "title": "osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning",
      "published": "2025-07",
      "url": "https://arxiv.org/abs/2507.12753",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "osmAG 의미 지도를 환경 맥락으로 삼아 LLM 이 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 한 방법. 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1033",
      "org": "IEEE Standards Association (IEEE RAS)",
      "title": "IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation",
      "published": "2015-10-26",
      "url": "https://standards.ieee.org/standard/1873-2015.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IEEE SA 표준 소개 페이지. 2D 메트릭·위상 지도 데이터 모델·형식 범위, 승인·발행일, 2026-03-26 비활성 보류 상태를 확인했다. 유료 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-956",
      "org": "지디넷코리아",
      "title": "네이버 제2사옥, 로봇 친화형 건축물 인증 획득",
      "published": "2022-04-11",
      "url": "https://zdnet.co.kr/view/?no=20220411142336",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "네이버 1784 의 로봇 친화형 건축물 인증 획득 보도. 인증지표 구성과 정밀지도·측위 인프라에 대한 평가위원 언급.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1035",
      "org": "국토지리정보원",
      "title": "실내공간정보",
      "published": null,
      "url": "https://www.ngii.go.kr/kor/content.do?sq=324",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "국토지리정보원의 실내공간정보 소개. 정의, 구축 대상(지하철·철도역사 등), LoD2, 자료 형식, 브이월드 제공.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020)",
      "title": "Lifelong update of semantic maps in dynamic environments",
      "published": "2020-10",
      "url": "https://arxiv.org/abs/2010.08846",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "가정용 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도의 의미 전이·충돌 감지·새 의미 발견 방법. 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066)",
      "title": "Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments",
      "published": "2023-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업 물류 환경용 LiDAR 점유 격자 지도 안전 갱신 알고리즘. 반복 확인·위치 추정 의심 시 갱신 중지, 모의 창고·실험실 평가. PMC 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "섹션 3: f21(원시 지도 변화와 이름 기반 작업·관제 책임), f20(핵심 질문 답, 추정) / 섹션 4: 지도 버전 f1, 구역 집합 f3, 이름·대체 이름·접근 제한 f6·f7, 의미 지도 f12, 3차원 장면 그래프 f14 / 섹션 5: 병원 — f11(타르투 대학병원 평면도 주요 위치 주석, 재인용), 가정 — f12(청소 로봇 의미 지도 갱신), 기타 — f18(네이버 1784 정밀지도·측위 인프라, 기사 기준 신뢰도 low). 여섯 항목 중 시작 조건·완료·인계 근거는 부족함을 명시. 물류창고 사례는 모의 실험(f13)뿐이라 현장 사례로 쓰지 않음 / 섹션 6: 장소 목록과 지도 요소 연결 f6·f7·f9, 지도 버전 배포·활성화 f1·f2, 임시 통제 구역 f3·차선 폐쇄 f10, 지도 변경 감지·갱신 f13(연계 대상), 평생 의미 지도 f12, 계층형 의미 지도 f14·f15, LLM 과 의미 지도 f16 / 섹션 7: VDA 5050 f1~f4, LIF f5, IMDF f6~f8, Open-RMF f9·f10, IEEE 1873 f17(비활성 보류 명시), osmAG f15 / 섹션 8: f12~f16, f19(국내 공공 실내공간정보) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 8, 12, 14, 15, 18, 21, 27, 45, 51, 57, 63, 65, 67 / 섹션 11: 기존 oq-188·oq-190·oq-193 과 open_questions_new 5건. 다음 실행 후보: 21. 상호운용 표준·적합성 페이지에 f5·f8·f17 반영, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f10 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "지도 버전",
      "term_en": "Map Version (VDA 5050 mapId / mapVersion)",
      "definition": "같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 에서는 관제가 내려받게 한 여러 버전 가운데 한 버전만 활성화해 로봇이 쓰게 한다."
    },
    {
      "term_ko": "대체 이름",
      "term_en": "Alternative Name (IMDF alt_name)",
      "definition": "IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다."
    },
    {
      "term_ko": "의미 지도",
      "term_en": "Semantic Map",
      "definition": "기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다."
    },
    {
      "term_ko": "3차원 장면 그래프",
      "term_en": "3D Scene Graph",
      "definition": "물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다."
    }
  ],
  "open_questions_new": [
    "제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 15. 지도·공간·위치 모델 | 근거: f1 | 종류: 일반",
    "IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성 | 근거: f17 | 종류: 일반",
    "공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 40. 운영 절차·요청 창구, 63. 병원·의료 | 근거: f3 | 종류: 일반",
    "IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 12. 채팅으로 업무 지시·오케스트레이션 | 근거: f7 | 종류: 일반",
    "국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 67. 기타 현장 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "f5 LIF 스키마의 layoutVersion·stationName 등 필드는 검색 요약에만 나와 README·스키마 원문으로 확인하지 못함(GitHub 저장소 페이지 403, VDMA 가이드라인 PDF 본문 추출 실패)",
      "f13 수치는 저자 보고이며 교차 확인 실패",
      "f14·f15·f16·f12 는 초록 기준이며 본문 실험 조건 미확인",
      "f17 IEEE 1873 표준 본문(유료) 미열람, Amigoni 외 해설 논문(oru.diva-portal.org)은 ECONNRESET 으로 열지 못함",
      "f18 기사 기준이며 스마트도시협회 인증 원자료 미확인",
      "Nav2 금지 구역·속도 필터(costmap filter) 문서는 docs.nav2.org·raw 경로 404, navigation.ros.org 연결 거부로 열지 못해 넣지 않음",
      "MiR 지도 편집기(바닥 계층과 구역·위치 구성 요소, 로봇 수 제한 구역)는 PDF 본문 추출 실패로 넣지 않음",
      "oq-193 건설 현장 지도–BIM 동기화 주기는 이번 조사에서도 확인되지 않음",
      "oq-188·oq-190 은 조사하지 않음(11절 반영 대상으로만 둠)",
      "물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례는 확인하지 못함"
    ],
    "scope_violations": [
      "f13: 로봇 점유 격자 지도 갱신은 분류 원문 19장의 로봇 자체 지능·제어(SLAM)이므로 claim 을 '연계 대상: '으로 시작함",
      "f14: 장면 그래프를 센서로 구축하는 부분은 로봇 인식(연계 대상)이며 계층형 표현 구조만 이 영역 근거로 쓰도록 제안함(f23 에서 구분)",
      "f19: 공공 실내공간정보 구축은 공공 데이터 소유자의 일이므로 입력 데이터 가용성 근거로만 제안함",
      "f23: SLAM·건물 데이터 구축·승강기 운행을 '연계 대상: '으로 표시함"
    ],
    "budget_used": {
      "queries": 18,
      "sources": 13
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 18회/30, 신규 출처 13건/15, 재사용 3건(ref-031·ref-079 는 github_raw 로 다시 열었고 ref-869 는 2026-09-30-03 브리프 재인용으로 이번에 열지 않음). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1014 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-03)가 ref-1015·ref-1017·ref-1019·ref-1024 를 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-046~ref-1037 을 순서대로 썼다. 원문 열람: 신규 13건 모두 열었다(webfetch 11건, github_raw 2건). 논문은 대부분 초록 페이지이고 Stefanini 외(ref-1037)만 PMC 본문을 열었다. 열지 못해 쓰지 않은 것: Nav2 문서(404·연결 거부), MiR Fleet 참조 안내서 PDF(본문 추출 실패), VDMA LIF 가이드라인 PDF(본문 추출 실패), LIF GitHub 저장소 페이지(403), MDPI·preprints.org(403), IEEE 1873 해설 논문(ECONNRESET). 교차 확인 0건, 신뢰도 high finding 없음(사실 finding 은 모두 단일 출처; IMDF 는 Apple 문서와 OGC 게시본이 같은 원천이라 독립 출처로 보지 않음). 분류 원문 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에는 f20 으로 답했고, 결론은 '장소 목록을 지도 요소에 묶고, 지도 버전 교체와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 변경을 나눠 관리한다'는 추정이다. 현장 유형 사례는 병원(f11, 재인용)·가정(f12)·기타(f18)이며, 물류창고 근거는 모의 실험(f13)뿐이라 site_type 을 null 로 두었다. 국내 자료는 국토지리정보원(ref-1035)·지디넷코리아(ref-956) 두 건이며 국내 로봇 지도 표준(KS)은 검색 2회에서 찾지 못했다. L. AI·학습 기술 관련(f14 장면 그래프, f16 LLM 추론)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 활성 지도 버전·폐쇄 구역으로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 IMDF·IndoorGML·LIF·구역 집합·차선 폐쇄·필터 마스크·위상 지도·반정적 객체·공간 그래프는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다."
  }
}
```

### runs/2026-09-30-04/verification.json

```json
{
  "run_id": "2026-09-30-04",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. raw.githubusercontent 원문(VDA5050_EN.md main, 3.0.0) 6.3절: mapId+mapVersion 식별, mapStatus ENABLED/DISABLED, 같은 mapId 는 한 버전만 활성, 지도 파일은 전용 지도 서버(6.3.1), 6.1.4.10 UNKNOWN_MAP_ID. 발행일 미확인 — 판 번호(3.0.0, main)를 기준으로 명시할 것. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분 수정). 6.3.1 'It is the responsibility of the fleet control to ensure that the correct maps are enabled' 와 6.3.5 'The mobile robot itself shall not delete maps' 는 원문과 일치. 다만 '사용 중인 지도의 deleteMap 은 로봇이 거부하게 한다'는 규범 문장이 아니며, 원문은 deleteMap 이 실패(FAILED)하는 예로 '지도가 사용 중인 경우'를 든다 — 문구 수정 지시."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 6.4절: 구역 유형(BLOCKED, LINE_GUIDED, RELEASE, COORDINATED_REPLANNING, SPEED_LIMIT, ACTION / PRIORITY, PENALTY, DIRECTED, BIDIRECTED), 전역 고유 zoneSetId, mapId 에만 묶이고 mapVersion 은 참조하지 않음, mapId 당 활성 구역 집합 하나, 내용 변경 시 새 zoneSetId, DUPLICATE_ZONE_SET(WARNING), BLOCKED_ZONE_VIOLATION(CRITICAL) 모두 원문 일치. 나열에서 BIDIRECTED 가 빠졌고 '구역 묶음'은 용어집 '구역 집합'과 충돌 — 수정 지시."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력 원문 5.2절: LIF 로 경로를 관제에 가져올 수 있고, 경로·경로망 구성은 이 문서의 일부가 아니다. 원문은 LIF 를 'VDMA 2024-03'으로 인용해 f5 의 README 날짜(2023-09)와 다르다 — 둘 다 제시 지시."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. LIF 저장소 README(raw): 발행 주체 VDMA, 'an interchange format for a track layout (e.g.: collection of edges, nodes and stations)', 'Version 1.0.0 - September 2023'. VDA 5050 3.0.0 은 같은 LIF 를 'VDMA 2024-03'으로 인용한다(f4) — 날짜 차이를 둘 다 제시."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분 수정). Apple IMDF Unit 페이지: 선택 속성 category·restriction·accessibility·name·alt_name·level_id·display_point, 예시 {\"en\": \"Ball Room\"}, 분류에 elevator·escalator·stairs·ramp·room·nonpublic 확인. '화장실(restroom)'은 이 페이지에서 확인하지 못함(분류 목록 페이지 404) — 나열에서 뺀다. Apple 문서와 OGC 게시본(ref-1028)은 같은 원천이라 독립 출처가 아니다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IMDF 용어집: name 은 ground truth·현실에 있는 것을 반영, alt_name 은 'intended to be indexed, enable queries, and support the retrieval of a predetermined label', Restriction 은 일반 대중의 일부로 제한된 공간(employeesonly·restricted). 원문과 일치."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. OGC 20-094, IMDF 1.0.0, 승인 2021-02-02, 게시 2021-02-18, 16개 지형지물 유형 목록 일치."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 입력 원문(traffic-editor.md): 'To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint', 경유점 속성 is_holding_point·is_parking_spot·is_charger·pickup_dispenser·dropoff_ingestor, 경유점 저장 형식(x, y, 높이, 이름, 매개변수), building_map_generator 로 항법 그래프 내보내기 후 rmf_fleet_adapters 가 사용. 기존 각주 ref-079 재사용."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 부분 추정. LaneRequest.msg 원문은 'string fleet_name / uint64[] open_lanes / uint64[] close_lanes' 세 줄뿐이며 설명 주석이 없다. 필드 구성은 [사실]로 남기되, '지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 연다'는 원문에 없는 해석이므로 [추정]으로 분리한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 리서치는 재인용(원문 미열람)이었으나 검증에서 Frontiers 원문을 열어 확인함: 'The floorplan is annotated in the Traffic Editor by adding walls, traffic lanes, chargers, locations, doors', 격자 지도를 평면도에 정합, ICU→검사실 혈액 검체 운반, 발행 2022-08-23. 브리프의 fetched: false 표시는 코드 상한(medium)에 따르며 검증이 올리지 않는다. 기존 각주 ref-869 재사용."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2010.08846 초록(IROS 2020 게재 예정, 2020-10-17 제출): 공간 의미 전이, 메타 의미 계층으로 불일치 처리, 새 공간 의미 편입, 수천 대 바닥 청소 로봇 배포. 초록 기준. 청소 로봇 제품 자체의 기능이므로 ROP 직접 기능처럼 쓰지 않도록 지시."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. PMC 본문: 버퍼 Nb=10·임계 7, 변화 수가 임계를 넘으면 위치 추정 회복까지 갱신 중지, Gazebo 290 m² 모의 창고 100개 시나리오·약 80 m² 실험실 4구성, 갱신 지도 오차 10 cm 미만 대 초기 지도 50 cm 초과, 지표 약 20~40% 개선, CPU 10~13%, 메모리 약 57.5 MB. 발행일은 2023-06-30 — as_of·발행일 정정. 저자 보고 수치. '연계 대상:' 표시 적절."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2305.07154(2023-05-11 제출) 초록: 계층형 3차원 장면 그래프, 실시간 시스템 Hydra, Clearpath Jackal·Unitree A1. arXiv 표기는 IJRR 투고본이므로 출처 표기를 'arXiv 2023-05(IJRR 투고본, 초록 기준)'로 맞춘다. 센서 기반 구축은 연계 대상."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2309.04791(2023-09-09 제출) 초록: OSM XML 기반 계층형 위상·거리 의미 지도, 로봇 이동 방식·속성을 고려한 계획, ROS 연동 C++ 라이브러리. 초록 기준."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2507.12753(v1 2025-07-17, v2 2026-03-03), RA-L 2026 채택 표기 확인, 동적·미기록 물체에서 기존 방법보다 우수 보고. 초록 기준, 수치 미확인. 언어 모델 추론이므로 교차 규칙상 44. 로봇 기반 모델·언어 모델 계획에도 연결."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IEEE SA 페이지: IEEE 1873-2015, 승인 2015-09-03, 발행 2015-10-26, IEEE RAS, 2D 메트릭·위상 지도 데이터 모델·형식, 2026-03-26 Inactive-Reserved. 유료 본문 미열람(소개 페이지로 실재 확인)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 지디넷코리아 2022-04-11: 스마트도시협회가 올해 처음 시작한 로봇 친화형 건축물 인증, 4개 부문·25개 평가 범주, 평가위원 발언(로봇이 인식하는 정밀지도와 측위 인프라, 승강기 이동 지원) 일치. 기사 단일 출처(신뢰도 low) — '지디넷코리아에 따르면' 형식 유지. 67. 기타 현장 페이지의 네이버 1784 사례(ref-997)·용어집 '로봇 친화형 건축물 인증'과 겹친다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분 수정). 국토지리정보원 페이지: 정의, 구축 대상(지하철·철도역사, 평창동계올림픽 관련 시설), LoD2, shp·3ds·max, 브이월드 제공, 로봇 언급 없음은 일치. 활용처는 원문상 공공분야(철도보안시스템, 시설물관리)·민간분야(실내 내비게이션, 메타버스, 좌석안내서비스)이며 '안전·소방'은 확인되지 않음 — 원문대로 고친다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. f6·f7·f9·f1·f3 의 확인된 내용에 기댄 종합 해석이다. f10 은 강등 뒤 필드 구성 부분만 근거로 쓴다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 근거 f12·f13·f2·f9 는 모두 확인됨. 3절 핵심 주장으로 쓸 때 [추정]을 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ROP 직접 범위 해석. '편집 화면과 변경 이력'은 교통 편집기(f9) 외에 직접 근거가 없으므로 [추정] 표기와 근거 범위를 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. '연계 대상:' 표시가 적절하며, 분류 원문 19장 경계와 맞다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 연결 영역의 번호와 이름이 정확하다. 교차 규칙상 f16 은 44. 로봇 기반 모델·언어 모델 계획에도 연결하도록 수정 지시."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f11 은 2026-09-30-03 브리프 f7(14. 도면·BIM에서 지도 만들기, ref-869)과 같은 타르투 대학병원 사례 — 기존 각주 ref-869 재사용, 충돌 없음",
      "f1~f4 는 기존 각주 ref-031, f9 는 ref-079 를 재사용(2026-09-25-40·2026-09-30-03 에서도 인용)",
      "f18 은 67. 기타 현장 페이지의 네이버 1784 사례(2026-09-30-02 f7·f8, ref-997)와 같은 건물을 다룸 — 충돌 없음, 용어집 '로봇 친화형 건축물 인증' 재사용",
      "VDA 5050 구역 집합·LIF·IMDF·차선 폐쇄는 용어집 기존 항목과 겹침 — 신규 등록하지 않음(브리프도 후보로 내지 않음)"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f3 의 '구역 묶음(zoneSet)'은 용어집 zone-set '구역 집합 (Zone Set (VDA 5050 zoneSet))'과 다르다 — '구역 집합'으로 통일"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f1: 기준일 표기에 'VDA 5050 3.0.0(공식 저장소 main)' 판을 명시한다 — 출처 발행일이 미확인이어서 판 번호로 기준을 고정해야 한다.",
    "f2: '사용 중인 지도의 deleteMap 은 로봇이 거부하게 한다'를 '지도가 사용 중이면 deleteMap 이 실패(FAILED)할 수 있다는 예를 든다'로 고친다 — 원문은 이를 규범 문장이 아니라 동작 상태의 실패 예로 적는다.",
    "f3: '구역 묶음'을 용어집의 '구역 집합'으로 바꾸고, 구역 유형 나열에 양방향(BIDIRECTED)을 더하거나 끝에 '등'을 붙인다 — 용어집과의 충돌, 나열 누락.",
    "f4·f5: 7절에서 LIF 판·날짜를 한쪽만 고르지 말고 'LIF 저장소 README 기준 1.0.0(2023-09)'과 'VDA 5050 3.0.0 이 인용한 VDMA 2024-03'을 함께 제시하고, 11절에 '종류: 출처 충돌' 열린 질문으로 올린다(관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성; 근거: f4, f5).",
    "f6: Unit 분류 나열에서 '화장실'을 뺀다 — ref-1026 Unit 페이지에서 확인되지 않았다(확인된 값: elevator·escalator·stairs·ramp·room·nonpublic 등).",
    "f10: 메시지 필드 구성(fleet_name·open_lanes·close_lanes)만 [사실]로 쓰고, '지도 파일을 다시 만들지 않고 운영 중에 차선을 닫거나 연다'는 [추정]으로 분리한다 — 메시지 정의에 설명 주석이 없어 원문이 이 해석을 뒷받침하지 않는다.",
    "f13: ref-1037 발행일과 기준일을 2023-06-30 으로 정정하고, 본문에서 '연계 대상'으로 짧게 다룬다(로봇 자체 지도 갱신) — PMC 원문 발행일.",
    "f14: ref-347 출처 표기를 'arXiv 2305.07154, 2023-05(IJRR 투고본, 초록 기준)'로 맞추고 센서 기반 구축 부분은 연계 대상으로 쓴다 — arXiv 페이지는 IJRR 투고 상태로 표기한다.",
    "f19: 활용처를 원문대로 '공공분야(철도보안시스템, 시설물관리)·민간분야(실내 내비게이션, 메타버스, 좌석안내서비스)'로 바꾼다 — '안전·소방'은 원문에서 확인되지 않았다.",
    "f12: 5절 가정 사례와 6절에서 청소 로봇의 평생 의미 지도는 로봇 제품 쪽 기능으로 서술하고, ROP 쪽 역할은 9절의 [추정](f22·f23) 범위로만 쓴다 — 분류 원문 19장 로봇 자체 지능·제어 경계.",
    "f16·f24: 10절에 44. 로봇 기반 모델·언어 모델 계획 연결을 더한다(45. 문서·도면·장면 이해, 8. 채팅으로 맵 작성, 12. 채팅으로 업무 지시·오케스트레이션 연결은 유지) — 언어 모델 추론은 L. AI·학습 기술의 44번 영역이 다루므로 교차 규칙상 양쪽 연결이 필요하다.",
    "5절: 사례는 브리프 근거대로 병원(f11)·가정(f12)·기타(f18) 세 현장 유형만 쓰고 물류창고 사례를 만들지 않으며(f13 은 모의 실험, site_type null), 여섯 항목 가운데 근거가 없는 칸(특히 시작 조건·완료·인계)은 '미확인'으로 둔다.",
    "f18: '지디넷코리아(2022-04-11)에 따르면' 기사 기준 표기를 유지하고, 용어는 용어집의 '로봇 친화형 건축물 인증'을 링크해 재사용한다 — 기사 단일 출처(신뢰도 low).",
    "각주: ref-031·ref-079·ref-869 는 참고문헌 페이지의 기존 각주 줄을 그대로 재사용하고, 신규 ref-046~ref-1037 만 reference_updates 에 넣는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 23건, 미확인 1건, 교차 확인 0건. 강등: f10 사실 → 일부 추정(운영 중 차선 폐쇄 해석 부분). 원문 미열람 출처: ref-869(리서치 재인용이나 검증에서 원문을 열어 내용 확인, 신뢰도 상한 medium 유지). 주의: 모든 사실 주장은 단일 출처이며(IMDF 의 Apple 문서와 OGC 게시본은 같은 원천), 논문 f12·f14·f15·f16 은 초록 기준이고 f13 수치는 저자 보고, f18 은 기사 기준이다. 3절(왜 중요한가)과 9절(책임 경계)의 결론은 [추정]이다. LIF 날짜가 출처마다 다르다(README 2023-09, VDA 5050 인용 2024-03). IEEE 1873-2015 는 2026-03-26 부터 비활성 보류 상태다. 정정 요청 없음. 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다. 검증은 추가 검색 없이 원문 열람으로만 확인했다.",
  "retry_reason": null
}
```

### runs/2026-09-30-04/pages.json

```json
{
  "run_id": "2026-09-30-04",
  "outline": [
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 800,
      "summary": "로봇 원시 지도는 계속 달라지지만 작업 목적지와 대화는 장소 이름으로 이루어지므로 지도 버전이 바뀌어도 이름과 지도 요소의 연결을 유지해야 한다. [추정][^ref-1036]",
      "planned_findings": [
        "f21",
        "f12",
        "f9",
        "f2",
        "f20"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 650,
      "summary": "지도 버전(mapId·mapVersion), 구역 집합, 이름·대체 이름, 접근 제한, 의미 지도, 3차원 장면 그래프가 이 영역의 기본 용어다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f3",
        "f7",
        "f12",
        "f14"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 900,
      "summary": "병원(평면도 주요 위치 주석), 가정(청소 로봇 의미 지도 갱신), 기타(로봇 친화형 건축물의 정밀지도) 세 현장 유형 사례를 여섯 항목으로 정리하고 근거 없는 칸은 미확인으로 둔다. [사실][^ref-869]",
      "planned_findings": [
        "f11",
        "f12",
        "f18"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "장소 목록을 지도 요소에 묶는 방식, 지도 버전 배포·활성화, 구역 집합과 차선 폐쇄 같은 임시 통제, 연계 대상인 지도 갱신, 계층형 의미 지도가 대표 접근법이다. [사실][^ref-031]",
      "planned_findings": [
        "f6",
        "f9",
        "f1",
        "f2",
        "f4",
        "f3",
        "f10",
        "f13",
        "f12",
        "f14",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "VDA 5050 3.0.0, LIF, IMDF 1.0.0, Open-RMF 교통 편집기와 LaneRequest, IEEE 1873-2015(비활성 보류), osmAG 가 관련된다. LIF 날짜는 출처마다 다르다. [사실][^ref-046]",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f5",
        "f8",
        "f9",
        "f10",
        "f15",
        "f17"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "평생 의미 지도, 지도 안전 갱신(연계 대상), 3차원 장면 그래프, osmAG·osmAG-LLM, 국토지리정보원 실내공간정보가 대표 자료다. [사실][^ref-1036]",
      "planned_findings": [
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f19"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 650,
      "summary": "ROP 는 장소 목록·지도와 구역 집합의 버전·임시 통제 선언을 맡고, 센서 기반 지도 생성·건물 데이터 구축·승강기 운행은 연계 대상으로 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "8·12·14·15·18·21·27·44·45·51·57·63·65·67번 영역과 이어진다. [추정][^ref-031]",
      "planned_findings": [
        "f24",
        "f16"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "기존 oq-188·oq-190·oq-193 과 새 질문 6건(LIF 날짜 출처 충돌 포함)을 둔다.",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f5",
        "f7",
        "f17",
        "f19"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/space-and-map-model/place-semantics-and-map-management.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 장소 목록·지도 버전·구역 집합·차선 폐쇄, 책임 경계, 연결 14개 영역, 열린 질문 9건), 13절 각주 16건, 프런트매터 갱신"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"6. 대표 접근법과 기술\" 절(2,190자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"11. 열린 질문\" 절(1,766자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,125자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"8. 대표 연구와 자료\" 절(960자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"4. 핵심 개념과 용어\" 절(866자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area16-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 16. 장소 의미·지도 관리 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(732자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 16. 장소 의미·지도 관리 | 영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 지도 버전·구역 집합·차선 폐쇄·장소 이름 모델, 책임 경계, 연결 14개 영역, 새 열린 질문 6건), 각주 16건 | run 2026-09-30-04",
  "index_updates": {
    "home_recent": "2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성(병원·가정·기타 적용 사례, VDA 5050 지도 버전·구역 집합, IMDF 장소 이름·대체 이름, Open-RMF 차선 요청, 책임 경계, 새 열린 질문 6건)",
    "category_recent": "2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성(적용 사례 3건, 대표 접근법·표준 7종, 책임 경계, 연결 14개 영역, 열린 질문 9건)",
    "area_recent": "2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성, 13절 각주 16건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "map-version",
      "term_ko": "지도 버전",
      "term_en": "Map Version (VDA 5050 mapId / mapVersion)",
      "definition": "같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 3.0.0 에서는 관제가 내려받게 한 여러 버전 가운데 같은 mapId 에서 한 버전만 활성화해 로봇이 쓰게 한다.",
      "description": "VDA 5050 3.0.0(공식 저장소 main, 확인일 2026-09-30)에서 지도 상태는 ENABLED·DISABLED 이며 관제가 downloadMap·enableMap·deleteMap 즉시 동작으로 관리한다.",
      "related_areas": [
        16,
        15,
        57
      ],
      "sources": [
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "alternative-name",
      "term_ko": "대체 이름",
      "term_en": "Alternative Name (IMDF alt_name)",
      "definition": "IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다.",
      "related_areas": [
        16,
        12
      ],
      "sources": [
        "ref-1027",
        "ref-1026"
      ]
    },
    {
      "action": "new",
      "slug": "semantic-map",
      "term_ko": "의미 지도",
      "term_en": "Semantic Map",
      "definition": "기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다.",
      "related_areas": [
        16,
        45,
        65
      ],
      "sources": [
        "ref-1036"
      ]
    },
    {
      "action": "new",
      "slug": "3d-scene-graph",
      "term_ko": "3차원 장면 그래프",
      "term_en": "3D Scene Graph",
      "definition": "물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다.",
      "related_areas": [
        16,
        45
      ],
      "sources": [
        "ref-347"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF)",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDMA 의 궤도 레이아웃 교환 형식 LIF 공식 저장소 README. 목적(통합사업자→제3자 상위 관제로 에지·노드·스테이션 전달)과 1.0.0 판(2023-09)을 확인했다. VDA 5050 3.0.0 은 같은 LIF 를 VDMA 2024-03 으로 인용한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1026",
      "org": "Apple (Apple Business Register)",
      "title": "Unit - Indoor Mapping Data Format",
      "published": null,
      "url": "https://register.apple.com/resources/imdf/types/unit",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "IMDF Unit 유형 참조 문서. 속성(category, restriction, accessibility, name, alt_name, display_point, level_id)과 분류값을 규정한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1027",
      "org": "Apple (Apple Business Register)",
      "title": "Glossary - Indoor Mapping Data Format",
      "published": null,
      "url": "https://register.apple.com/resources/imdf/glossary",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "IMDF 용어집. name(기준 레이블), alt_name(색인·검색용 동의어), Unit, Level, Anchor, Venue, Restriction 을 정의한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1028",
      "org": "Open Geospatial Consortium (OGC)",
      "title": "Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094",
      "published": "2021-02-18",
      "url": "https://docs.ogc.org/cs/20-094/index.html",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "OGC 가 커뮤니티 표준으로 승인(2021-02-02)·게시(2021-02-18)한 IMDF 1.0.0. 16개 지형지물 유형을 정의한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-569",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 차선 열기·닫기 요청 메시지 정의(fleet_name, open_lanes, close_lanes). 설명 주석은 없다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-347",
      "org": "Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본)",
      "title": "Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems",
      "published": "2023-05",
      "url": "https://arxiv.org/abs/2305.07154",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "계층형 3차원 장면 그래프(물체·장소·방·건물)와 실시간 구축 시스템 Hydra 를 제시한 논문의 arXiv 초록(IJRR 투고본, 초록 기준). 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1031",
      "org": "Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv)",
      "title": "osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.04791",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OpenStreetMap XML 기반 계층형 위상·거리 의미 지도 형식 osmAG 와 ROS 연동 라이브러리. 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1032",
      "org": "Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv)",
      "title": "osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning",
      "published": "2025-07",
      "url": "https://arxiv.org/abs/2507.12753",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "osmAG 의미 지도를 환경 맥락으로 삼아 LLM 이 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 한 방법. 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1033",
      "org": "IEEE Standards Association (IEEE RAS)",
      "title": "IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation",
      "published": "2015-10-26",
      "url": "https://standards.ieee.org/standard/1873-2015.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IEEE SA 표준 소개 페이지. 2D 메트릭·위상 지도 데이터 모델·형식 범위, 승인(2015-09-03)·발행일, 2026-03-26 비활성 보류 상태를 확인했다. 유료 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-956",
      "org": "지디넷코리아",
      "title": "네이버 제2사옥, 로봇 친화형 건축물 인증 획득",
      "published": "2022-04-11",
      "url": "https://zdnet.co.kr/view/?no=20220411142336",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "네이버 1784 의 로봇 친화형 건축물 인증 획득 보도. 인증지표 구성과 정밀지도·측위 인프라에 대한 평가위원 언급.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1035",
      "org": "국토지리정보원",
      "title": "실내공간정보",
      "published": null,
      "url": "https://www.ngii.go.kr/kor/content.do?sq=324",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "국토지리정보원의 실내공간정보 소개. 정의, 구축 대상(지하철·철도역사 등), LoD2, 자료 형식, 브이월드 제공, 공공·민간 활용처.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020)",
      "title": "Lifelong update of semantic maps in dynamic environments",
      "published": "2020-10",
      "url": "https://arxiv.org/abs/2010.08846",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "가정용 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도의 의미 전이·충돌 감지·새 의미 발견 방법. 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066)",
      "title": "Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments",
      "published": "2023-06-30",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업 물류 환경용 LiDAR 점유 격자 지도 안전 갱신 알고리즘. 반복 확인·위치 추정 의심 시 갱신 중지, 모의 창고·실험실 평가. PMC 본문 열람, 발행일 2023-06-30.",
      "cited_by": [
        "docs/categories/space-and-map-model/place-semantics-and-map-management.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "출처 충돌: LIF 의 판·날짜가 저장소 README 기준 1.0.0(2023-09)과 VDA 5050 3.0.0 이 인용한 VDMA 2024-03 으로 다르다. 어느 쪽이 현행이며 두 날짜는 같은 판을 가리키는가?",
      "areas": [
        16,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가?",
      "areas": [
        16,
        15
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가?",
      "areas": [
        16,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가?",
      "areas": [
        16,
        40,
        63
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가?",
      "areas": [
        16,
        12
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가?",
      "areas": [
        16,
        67
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시",
      "title": "16. 장소 의미·지도 관리"
    }
  ],
  "standards_updates": [
    {
      "name": "IEEE 1873-2015 Robot Map Data Representation for Navigation",
      "kind": "표준",
      "org": "IEEE Standards Association (IEEE RAS)",
      "url": "https://standards.ieee.org/standard/1873-2015.html",
      "related_areas": [
        16,
        15,
        21
      ],
      "summary": "항법하는 이동 로봇의 2차원 메트릭·위상 지도 데이터 모델·형식을 정한 표준(2015-10-26 발행). 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다.",
      "ref_id": "ref-1033"
    },
    {
      "name": "osmAG (OSM 형식 계층형 위상·거리 의미 지도)",
      "kind": "프레임워크",
      "org": "Feng, D. 외 (ShanghaiTech, arXiv)",
      "url": "https://arxiv.org/abs/2309.04791",
      "related_areas": [
        16,
        15
      ],
      "summary": "OpenStreetMap XML 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담는 파일 형식과 ROS 연동 C++ 라이브러리. 초록 기준.",
      "ref_id": "ref-1031"
    },
    {
      "name": "Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "related_areas": [
        16,
        27
      ],
      "summary": "플릿 이름(fleet_name)과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어진 메시지 정의.",
      "ref_id": "ref-569"
    }
  ],
  "additional_research_requests": [
    "6·7절: LIF 스키마 필드(layoutVersion·stationName 등)를 스키마 원문으로 확인해야 LIF 가 장소 이름·버전을 어떻게 표현하는지 쓸 수 있다(README 에 필드 없음).",
    "5절: 물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례가 필요하다(이번 브리프에는 물류창고 근거가 모의 실험뿐).",
    "5절: 병원·가정·기타 사례의 시작 조건·완료·인계·제약·예외·성과 근거가 없어 '미확인'으로 두었다. 타르투 대학병원 논문 본문과 청소 로봇 의미 지도 논문 본문에서 해당 항목을 확인해야 한다.",
    "6절: Nav2 금지 구역·속도 필터(costmap filter)와 MiR 지도 편집기(구역·위치 구성 요소)의 공식 문서를 열어 제조사·오픈소스 쪽 임시 통제 구역 방식을 보강해야 한다(이번 실행에서 열지 못함).",
    "11절 oq-193: 건설 현장 점검 로봇 지도–BIM 동기화 주기의 근거가 여전히 없다.",
    "13절: ref-031·ref-079·ref-869 의 참고문헌 페이지 '각주 형식' 줄이 입력에 없어 브리프 출처 필드로 각주를 만들었다. 기존 줄과 다르면 퍼블리셔가 맞춰 주어야 한다. 또 ref-046 는 기존 ref-046(LIF README)과 URL 이 같으므로 병합 여부 확인이 필요하다."
  ],
  "fixes_applied": [
    "f1 기준일 명시 — 3·4·6·7절에서 VDA 5050 을 'VDA 5050 3.0.0(공식 저장소 main)'으로 적고 확인일 2026-09-30 을 함께 두었다.",
    "f2 문구 수정 — 6절 '지도 버전의 배포와 활성화'에서 '명세는 지도가 사용 중이면 deleteMap 이 실패(FAILED)할 수 있다는 예를 든다'로 고쳤다.",
    "f3 용어·나열 수정 — 4·6절에서 '구역 집합'(용어집 zone-set 링크)으로 통일하고 구역 유형 나열에 양방향(BIDIRECTED)을 더했다.",
    "f4·f5 LIF 날짜 — 7절 LIF 행에 'README 기준 1.0.0(2023-09)'과 'VDA 5050 3.0.0 이 인용한 VDMA 2024-03'을 함께 제시하고, 11절에 '출처 충돌' 새 질문(관련 영역 16·21, 각주 ref-046·ref-031)을 두고 open_question_updates 에 냈다.",
    "f6 화장실 제외 — 6절 IMDF Unit 분류 나열을 '승강기·에스컬레이터·계단·경사로·방·비공개 구역 등'으로 쓰고 화장실을 뺐다.",
    "f10 분리 — 6절에서 LaneRequest 필드 구성(fleet_name·open_lanes·close_lanes)만 [사실]로 쓰고, 운영 중 차선을 닫거나 여는 쓰임은 설명 주석이 없다는 점을 밝혀 [추정]으로 분리했다(7절 표도 필드 구성만 [사실]).",
    "f13 발행일·범위 — ref-1037 각주·reference_updates 발행일을 2023-06-30 으로 고치고, 6·8절에서 '연계 대상:'으로 시작하는 짧은 서술로 다뤘다.",
    "f14 출처 표기 — ref-347 각주·8절·4절 표기를 'arXiv 2305.07154, 2023-05(IJRR 투고본, 초록 기준)'로 맞추고, Hydra 센서 기반 구축 부분은 6·8절에서 연계 대상으로 표시했다.",
    "f19 활용처 — 8절 국토지리정보원 항목의 활용처를 '공공분야(철도보안시스템, 시설물관리)·민간분야(실내 내비게이션, 메타버스, 좌석안내서비스)'로 바꾸고 안전·소방을 뺐다.",
    "f12 경계 — 5절 가정 사례 표와 서술, 6절에서 평생 의미 지도를 '로봇 제품 쪽 기능'으로 서술하고, ROP 역할은 9절의 [추정](f22·f23) 범위로만 다룬다고 밝혔다.",
    "f16·f24 연결 — 10절에 44. 로봇 기반 모델·언어 모델 계획(ref-1032)을 더하고 45·8·12번 연결을 유지했으며 프런트매터 related_areas 에 44 를 넣었다.",
    "5절 사례 범위 — 병원(f11)·가정(f12)·기타(f18) 세 현장 유형만 쓰고 물류창고 사례를 만들지 않았으며, 근거 없는 칸(시작 조건·완료·인계 등)은 '미확인'으로 두었다.",
    "f18 표기 — 5절 기타 사례를 '지디넷코리아(2022-04-11)에 따르면' 형식으로 쓰고 용어집 '로봇 친화형 건축물 인증'을 링크했다.",
    "각주 — ref-031·ref-079·ref-869 는 기존 id 를 재사용하고(참고문헌 페이지 줄은 입력에 없어 브리프 출처 필드로 같은 형식을 구성, additional_research_requests 에 확인 요청), reference_updates 에는 신규 ref-046~ref-1037 만 넣었다.",
    "분량 초과 자동 분리: 16. 장소 의미·지도 관리 본문 10,449자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,485자"
  ]
}
```

### runs/2026-09-30-04/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area16-s6.md (2,190자)
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area16-s11.md (1,766자)
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area16-s7.md (1,125자)
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area16-s8.md (960자)
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area16-s4.md (866자)
    - docs/categories/space-and-map-model/place-semantics-and-map-management.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area16-s10.md (732자)
```

### runs/2026-09-30-04/pages/categories/space-and-map-model/place-semantics-and-map-management.md

```markdown
---
title: "16. 장소 의미·지도 관리"
type: area
category: "D. 공간·지도 모델"
area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [장소 이름, 지도 버전, 구역 집합, IMDF, 의미 지도, VDA 5050]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-079, ref-869, ref-046, ref-1026, ref-1027, ref-1028, ref-569, ref-347, ref-1031, ref-1032, ref-1033, ref-956, ref-1035, ref-1036, ref-1037]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 16. 장소 의미·지도 관리

# 16. 장소 의미·지도 관리

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

## 3. 왜 중요한가

로봇이 만든 원시 지도는 주행과 환경 변화에 따라 계속 달라지는데 작업 목적지와 사용자 대화는 장소 이름으로 이루어지므로, 지도 버전이 바뀌어도 이름과 지도 요소의 연결을 유지해야 한다는 점에서 이 영역이 중요한 것으로 보인다. [추정][^ref-1036][^ref-1037]

근거는 두 갈래다. 가정용 바닥 청소 로봇 연구에서는 로봇 원시 지도가 주행마다 달라져도 사용자와 공유하는 의미 정보를 새 지도로 옮겨야 하는 문제가 다뤄졌다(2020-10 발표, 초록 기준). [사실][^ref-1036] Open-RMF 교통 편집기에서는 로봇이 어떤 경유점에서 끝나는 작업을 주려면 그 경유점에 이름을 붙여야 한다(확인일 2026-09-30). [사실][^ref-079]

책임의 문제도 있다. VDA 5050 3.0.0(공식 저장소 main, 확인일 2026-09-30)은 올바른 지도가 활성화되도록 보장하는 책임을 관제에 둔다. [사실][^ref-031] 여러 제조사 로봇을 묶는 ROP 는 이 관제 책임을 이어받게 될 것으로 보인다. [추정][^ref-031]

2절의 핵심 질문에 대해 확인한 자료가 가리키는 답은 두 부분이다. 같은 이름은 장소마다 고유 식별자·기준 이름·별칭·용도 분류·접근 제한을 둔 장소 목록을 지도 요소(경유점·공간·스테이션)에 묶는 방식으로 표현되고, 공간 변경은 지도 자체의 버전 교체(mapId·mapVersion)와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 나뉘어 관리되는 것으로 보인다. [추정][^ref-1026][^ref-1027][^ref-079][^ref-031][^ref-569]

## 4. 핵심 개념과 용어

이 영역의 용어는 지도 자체를 가리키는 말과 지도 위 장소를 가리키는 말로 나뉜다. 아래 정의의 확인일은 따로 적지 않으면 2026-09-30 이다.

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area16-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

확인한 자료에서 장소 의미·지도 관리의 현장 근거는 병원·가정·기타 세 현장 유형에서 나왔다. 물류창고 근거는 모의 실험뿐이어서 현장 사례로 쓰지 않았고, 각 사례에서 자료로 확인하지 못한 항목은 "미확인"으로 두었다.

**현장 유형:** 병원

**사례:** 병원 평면도에 주요 위치를 주석해 검체 운반 목적지 정하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 평면도 위에 주석한 주요 위치(운반 목적지)와, 중환자실에서 검사실까지 운반한 혈액 검체 [사실][^ref-869] |
| 수행 자원 | 평면도 주석은 Open-RMF 교통 편집기로 했고, TIAGo 로봇으로 만든 격자 지도를 평면도에 정합했다 [사실][^ref-869] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

에스토니아 타르투 대학병원 현장 시험(2022-08-23 발행)에서는 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소와 함께 주요 위치를 주석해 로봇 운반 작업의 목적지를 정했고, 이 지도로 중환자실에서 검사실까지 혈액 검체를 운반했다. [사실][^ref-869] 이 사례에서 장소 의미는 "어디로 가라"는 작업 목적지를 정하는 데 쓰였다.

**현장 유형:** 가정

**사례:** 가정용 바닥 청소 로봇의 의미 지도 갱신

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 사용자와 공유하는 공간 의미 정보와 새로 탐색한 공간 [사실][^ref-1036] |
| 수행 자원 | 실제 가정에 배포된 바닥 청소 로봇 수천 대(로봇 제품 쪽 기능) [사실][^ref-1036] |
| 제약 | 로봇 원시 지도가 주행마다 달라진다 [사실][^ref-1036] |
| 완료·인계 | 미확인 |
| 예외·성과 | 동적 물체 때문에 생긴 의미 충돌을 메타 의미 계층으로 찾아 해소한다 [사실][^ref-1036]. 처리량·시간·비용 영향은 미확인 |

Narayana 외(IROS 2020, 초록 기준)는 실제 가정의 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도(lifelong semantic map)에서 공간 의미를 새 지도로 옮기고, 의미 충돌을 해소하며, 새로 탐색한 공간의 의미를 찾아 더하는 방법을 제시했다. [사실][^ref-1036] 이것은 청소 로봇 제품 쪽 기능이며, ROP 가 이런 로봇과 역할을 어떻게 나눌지는 9절의 추정 범위로만 다룬다.

**현장 유형:** 기타

**사례:** 로봇 친화형 건축물 인증을 받은 사옥의 정밀지도·측위 인프라

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공하고 이동형 서비스 로봇의 승강기 이동을 지원한다는 평가위원 평가(지디넷코리아 보도 기준) [사실][^ref-956] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

지디넷코리아(2022-04-11)에 따르면 네이버 제2사옥 1784 는 스마트도시협회가 처음 실시한 [로봇 친화형 건축물 인증](../../glossary/robot-friendly-building-certification.md)(4개 부문·25개 평가 범주)을 받았고, 평가위원은 이 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공한다고 평가했다. [사실][^ref-956] 기사 단일 출처이며 인증 원자료는 확인하지 못했다.

## 6. 대표 접근법과 기술

장소 의미·지도 관리의 접근법은 장소 목록을 지도 요소에 묶는 방식, 지도 버전을 배포·활성화하는 방식, 지도와 따로 두는 임시 통제로 나뉜다. [추정][^ref-031][^ref-1026]

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area16-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

6절의 접근법은 아래 표준과 오픈소스로 구체화돼 있다. 확인일은 따로 적지 않으면 2026-09-30 이다.

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area16-s7.md)에 있다.

## 8. 대표 연구와 자료

장소 의미를 지도 변화에 맞춰 유지하는 연구는 주로 로봇 쪽 의미 지도와 계층형 표현에서 나왔다. [추정][^ref-1036][^ref-347]

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 대표 연구와 자료](../../topics/2026/2026-09-30-area16-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

[범위 경계](../../about/scope-boundary.md) 기준으로 보면, 이 영역에서 ROP 는 여러 제조사의 지도를 받아 장소 의미를 붙이고 버전을 관리하는 쪽을 맡는 것으로 보인다. [추정][^ref-031][^ref-1026]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 장소 목록(식별자·이름·별칭·용도·접근 제한)을 관리해 제조사별 지도 요소와 연결하고, 제조사별 지도·구역 집합의 버전을 기록하며 배포·활성화를 지시한다 [추정][^ref-031][^ref-079][^ref-1027] | 연계 대상: SLAM 지도 작성·점유 격자 갱신·장면 그래프 구축 같은 센서 기반 지도 생성 [추정][^ref-1037][^ref-347] |
| 시설·설비 제어 | 공사·청소 같은 임시 통제 구역과 차선 폐쇄의 선언·해제 [추정][^ref-031][^ref-569] | 연계 대상: 승강기 운행 [추정][^ref-031] |

사람이 층·공간·장소를 고치는 편집 화면과 변경 이력도 ROP 가 맡을 범위로 보이지만, 교통 편집기 외에 직접 근거는 없다. [추정][^ref-079] 공공 실내공간정보·BIM 같은 건물 공간 데이터의 구축·갱신은 건물·공공 데이터 소유자의 일이며, ROP 는 이를 받아 장소 의미를 붙이는 인터페이스를 맡을 것으로 보인다. [추정][^ref-1035][^ref-031]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

장소 이름과 지도 버전은 도면·좌표·대화·경로·표준 영역에 두루 쓰인다. [추정][^ref-031][^ref-079]

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area16-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이 영역에서 아직 답하지 못한 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [16. 장소 의미·지도 관리 — 열린 질문](../../topics/2026/2026-09-30-area16-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30 (원문 미열람)
[^ref-1026]: Apple (Apple Business Register), Unit - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/types/unit, 접근일 2026-09-30
[^ref-1027]: Apple (Apple Business Register), Glossary - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/glossary, 접근일 2026-09-30
[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본, 초록 기준), Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-30
[^ref-956]: 지디넷코리아, 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-30
[^ref-1035]: 국토지리정보원, 실내공간정보, 미확인, https://www.ngii.go.kr/kor/content.do?sq=324, 접근일 2026-09-30
[^ref-1036]: Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020), Lifelong update of semantic maps in dynamic environments, 2020-10, https://arxiv.org/abs/2010.08846, 접근일 2026-09-30
[^ref-1037]: Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066), Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments, 2023-06-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/, 접근일 2026-09-30
```

### docs/categories/space-and-map-model/place-semantics-and-map-management.md

```markdown
---
title: "16. 장소 의미·지도 관리"
type: area
category: "D. 공간·지도 모델"
area_no: 16
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 16. 장소 의미·지도 관리

# 16. 장소 의미·지도 관리

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 적용 사례 (현장 유형 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

아직 작성되지 않음

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아직 작성되지 않음

## 11. 열린 질문

아직 작성되지 않음

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

(아직 각주가 없다. 본문이 작성되면 출처 각주를 여기에 둔다.)
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s6.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 대표 접근법과 기술"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-079, ref-1026, ref-569, ref-347, ref-1031, ref-1032, ref-1036, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#6
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 대표 접근법과 기술

# 16. 장소 의미·지도 관리 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 장소 의미·지도 관리의 접근법은 장소 목록을 지도 요소에 묶는 방식, 지도 버전을 배포·활성화하는 방식, 지도와 따로 두는 임시 통제로 나뉜다. [추정][^ref-031][^ref-1026]
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

장소 의미·지도 관리의 접근법은 장소 목록을 지도 요소에 묶는 방식, 지도 버전을 배포·활성화하는 방식, 지도와 따로 두는 임시 통제로 나뉜다. [추정][^ref-031][^ref-1026]

### 장소 목록을 지도 요소에 묶기

IMDF 의 Unit(실내의 구별되는 공간)은 기능 분류(category)·접근 제한(restriction)·접근성(accessibility)·이름(name)·대체 이름(alt_name)·표시 지점(display_point)·소속 층(level_id)을 속성으로 가지며, 분류에는 승강기·에스컬레이터·계단·경사로·방·비공개 구역 등이 있다(확인일 2026-09-30). [사실][^ref-1026] Open-RMF 교통 편집기는 경유점에 주차(is_parking_spot)·대기(is_holding_point)·충전(is_charger)·디스펜서·인제스터 같은 속성을 달고, 층별 경유점(좌표·높이·이름)·벽·문·차선을 담은 .building.yaml 을 building_map_generator 로 항법 그래프로 내보내 플릿 어댑터가 쓰게 한다(확인일 2026-09-30). [사실][^ref-079]

### 지도 버전의 배포와 활성화

VDA 5050 3.0.0(공식 저장소 main)에서 관제는 downloadMap·enableMap·deleteMap 즉시 동작으로 전용 지도 서버의 지도를 로봇에 내려받게 하고 활성화하며, 내려받은 지도는 DISABLED 로 추가되고 enableMap 은 같은 mapId 의 다른 버전을 비활성화한다. [사실][^ref-031] 모르는 mapId 를 참조한 주문은 UNKNOWN_MAP_ID 로 거부된다. [사실][^ref-031] 로봇은 스스로 지도를 지우지 않으며, 명세는 지도가 사용 중이면 deleteMap 이 실패(FAILED)할 수 있다는 예를 든다. [사실][^ref-031] 경로·경로망·스테이션 정의 같은 설정은 구현 단계의 일로 명세 범위 밖에 있고, 구현 단계에서 LIF 로 경로를 관제에 가져올 수 있다. [사실][^ref-031]

### 임시 통제: 구역 집합과 차선 폐쇄

VDA 5050 3.0.0 의 구역 유형에는 진입 금지(BLOCKED)·유도선 주행(LINE_GUIDED)·해제(RELEASE)·재계획 조율·속도 제한·동작 구역과 우선·벌점·방향·양방향(BIDIRECTED) 구역이 있다. [사실][^ref-031] 구역 집합은 MQTT zoneSet 토픽이나 downloadZoneSet 으로 배포하고 enableZoneSet·deleteZoneSet 으로 관리하며, 내용이 바뀌면 새 zoneSetId 가 필요하고 같은 zoneSetId 를 다시 받으면 DUPLICATE_ZONE_SET 경고로 거부한다. [사실][^ref-031] 진입 금지 구역 침범은 치명 오류다. [사실][^ref-031]

Open-RMF 의 차선 요청 메시지(LaneRequest)는 플릿 이름(fleet_name)과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어진다(확인일 2026-09-30). [사실][^ref-569] 이 메시지는 지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 여는 [차선 폐쇄](../../glossary/lane-closure.md)에 쓰이는 것으로 보이지만, 메시지 정의에 설명 주석이 없어 원문으로 확인하지는 못했다. [추정][^ref-569]

### 지도 변경 감지·갱신 (연계 대상)

연계 대상: Stefanini 외(Sensors, 2023-06-30)의 LiDAR 점유 격자 지도 갱신 알고리즘은 격자 변화가 여러 스캔에서 반복될 때만(버퍼 10회 중 7회 이상) 반영하고 위치 추정 오류가 의심되면 갱신을 멈추며, 모의 창고 100개 시나리오와 약 80 m² 실험실에서 갱신 지도로 평균 위치 오차를 10 cm 아래(정적 지도는 50 cm 초과)로 유지했다고 보고했다(저자 보고 수치). [사실][^ref-1037] 이런 센서 기반 지도 갱신은 로봇 자체 지능·제어에 속하는 일로 보인다. [추정][^ref-1037]

### 의미 지도와 계층형 표현

가정용 청소 로봇의 평생 의미 지도는 로봇 제품 쪽에서 공간 의미를 새 지도로 옮기고 의미 충돌을 해소하는 방법이다(5절 가정 사례). [사실][^ref-1036] Hughes 외는 3차원 장면 그래프를 물체·장소·방·건물 층으로 묶는 계층형 공간 표현으로 제시했다(초록 기준). [사실][^ref-347] 연계 대상: 시각·관성 데이터로 이를 실시간 구축하는 공개 소스 시스템 Hydra 는 Clearpath Jackal·Unitree A1 로봇으로 시험됐다. [사실][^ref-347] osmAG 는 OpenStreetMap XML 형식 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담아 기존 OSM 도구로 사람이 읽고 고칠 수 있게 한다(2023-09, 초록 기준). [사실][^ref-1031] osmAG-LLM(RA-L 2026 채택)은 osmAG 의미 지도를 환경 맥락으로 삼아 대규모 언어 모델(Large Language Model, LLM)이 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 해, 동적·미기록 대상에서 기존 방법보다 나은 탐색 성공을 보고했다(초록 기준, 수치 미확인). [사실][^ref-1032]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-1026]: Apple (Apple Business Register), Unit - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/types/unit, 접근일 2026-09-30
[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본, 초록 기준), Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-30
[^ref-1031]: Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv), osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics, 2023-09, https://arxiv.org/abs/2309.04791, 접근일 2026-09-30
[^ref-1032]: Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning, 2025-07, https://arxiv.org/abs/2507.12753, 접근일 2026-09-30
[^ref-1036]: Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020), Lifelong update of semantic maps in dynamic environments, 2020-10, https://arxiv.org/abs/2010.08846, 접근일 2026-09-30
[^ref-1037]: Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066), Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments, 2023-06-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s11.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 열린 질문"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-046]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#11
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 열린 질문

# 16. 장소 의미·지도 관리 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 질문은 이 영역에서 아직 답하지 못한 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 질문은 이 영역에서 아직 답하지 못한 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-188** (상태: 열림) 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (관련 영역: 66. 실외, 60. 노동·수용성·접근성, 16. 장소 의미·지도 관리)
- **oq-190** (상태: 열림) 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? (관련 영역: 66. 실외, 21. 상호운용 표준·적합성, 16. 장소 의미·지도 관리)
- **oq-193** (상태: 열림) 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? 이번 조사에서도 확인되지 않았다. (관련 영역: 67. 기타 현장, 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리)
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) 출처 충돌: LIF 의 판·날짜가 저장소 README 기준 1.0.0(2023-09)과 VDA 5050 3.0.0 이 인용한 VDMA 2024-03 으로 다르다. 어느 쪽이 현행이며 두 날짜는 같은 판을 가리키는가? (관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성)[^ref-046][^ref-031]
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) 제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? (관련 영역: 16. 장소 의미·지도 관리, 15. 지도·공간·위치 모델)
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? (관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성)
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (관련 영역: 16. 장소 의미·지도 관리, 40. 운영 절차·요청 창구, 63. 병원·의료)
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? (관련 영역: 16. 장소 의미·지도 관리, 12. 채팅으로 업무 지시·오케스트레이션)
- **새 질문** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-04) 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? (관련 영역: 16. 장소 의미·지도 관리, 67. 기타 현장)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s7.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-079, ref-046, ref-1026, ref-1028, ref-569, ref-1031, ref-1033]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#7
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스

# 16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 6절의 접근법은 아래 표준과 오픈소스로 구체화돼 있다. 확인일은 따로 적지 않으면 2026-09-30 이다.
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

6절의 접근법은 아래 표준과 오픈소스로 구체화돼 있다. 확인일은 따로 적지 않으면 2026-09-30 이다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0(공식 저장소 main) | 표준 | 지도 버전(mapId·mapVersion)의 배포·활성화·삭제와 구역 집합을 정하고, 경로·스테이션 정의는 명세 범위 밖에 둔다 [사실][^ref-031] | [^ref-031] |
| [레이아웃 교환 형식](../../glossary/layout-interchange-format.md)(Layout Interchange Format, LIF) | 표준 | 무인운반차 통합사업자가 궤도 레이아웃(에지·노드·스테이션의 모음)을 제3자 상위 관제 시스템으로 넘기는 교환 형식이다 [사실][^ref-046]. 판·날짜는 출처마다 다르다: 저장소 README 기준 1.0.0(2023-09) [사실][^ref-046], VDA 5050 3.0.0 이 인용한 VDMA 2024-03 [사실][^ref-031] | [^ref-046] |
| IMDF 1.0.0(OGC 커뮤니티 표준 20-094) | 표준 | OGC 가 2021-02-02 승인·2021-02-18 게시했으며 venue·building·level·unit·opening·fixture·anchor·occupant·geofence 등 16개 지형지물 유형을 정의한다 [사실][^ref-1028]. 장소의 이름·대체 이름·접근 제한을 표현한다(Apple 문서와 OGC 게시본은 같은 원천) [사실][^ref-1026] | [^ref-1028] |
| [Open-RMF](../../glossary/open-rmf.md) 교통 편집기 | 오픈소스 | 경유점 이름·속성과 층별 지도를 편집해 항법 그래프로 내보낸다 [사실][^ref-079] | [^ref-079] |
| Open-RMF 차선 요청 메시지(LaneRequest) | 오픈소스 | 플릿 이름과 열 차선·닫을 차선 번호 배열로 이루어진다 [사실][^ref-569] | [^ref-569] |
| IEEE 1873-2015 Robot Map Data Representation for Navigation | 표준 | 항법하는 이동 로봇의 2차원 메트릭·[위상 지도](../../glossary/topological-map.md) 데이터 모델·형식을 정한 IEEE 로봇자동화학회(RAS) 표준으로 2015-10-26 발행됐고, 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다 [사실][^ref-1033] | [^ref-1033] |
| osmAG | 프레임워크 | OSM 형식의 계층형 위상·거리 의미 지도 파일 형식과 ROS 연동 C++ 라이브러리다 [사실][^ref-1031] | [^ref-1031] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있고, 관련 용어로 [IndoorGML](../../glossary/indoorgml.md)·[공간 그래프](../../glossary/space-graph.md)가 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
[^ref-1026]: Apple (Apple Business Register), Unit - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/types/unit, 접근일 2026-09-30
[^ref-1028]: Open Geospatial Consortium (OGC), Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094, 2021-02-18, https://docs.ogc.org/cs/20-094/index.html, 접근일 2026-09-30
[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-1031]: Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv), osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics, 2023-09, https://arxiv.org/abs/2309.04791, 접근일 2026-09-30
[^ref-1033]: IEEE Standards Association (IEEE RAS), IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation, 2015-10-26, https://standards.ieee.org/standard/1873-2015.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s8.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 대표 연구와 자료"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-347, ref-1031, ref-1032, ref-1035, ref-1036, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#8
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 대표 연구와 자료

# 16. 장소 의미·지도 관리 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 장소 의미를 지도 변화에 맞춰 유지하는 연구는 주로 로봇 쪽 의미 지도와 계층형 표현에서 나왔다. [추정][^ref-1036][^ref-347]
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

장소 의미를 지도 변화에 맞춰 유지하는 연구는 주로 로봇 쪽 의미 지도와 계층형 표현에서 나왔다. [추정][^ref-1036][^ref-347]

- Narayana, Kolling, Nardelli, Fong, Lifelong update of semantic maps in dynamic environments(IROS 2020) — 가정용 바닥 청소 로봇 수천 대의 평생 의미 지도에서 의미 전이·충돌 해소·새 공간 의미 편입을 다룬다(초록 기준). [사실][^ref-1036]
- 연계 대상: Stefanini 외, Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments(Sensors, 2023-06-30) — 반복 확인과 위치 추정 의심 시 갱신 중지로 점유 격자 지도 오염을 막는 로봇 쪽 지도 갱신 알고리즘이다. [사실][^ref-1037]
- Hughes 외, Foundations of Spatial Perception for Robotics(arXiv 2305.07154, 2023-05, IJRR 투고본, 초록 기준) — 계층형 3차원 장면 그래프와 실시간 구축 시스템 Hydra 를 제시한다. 센서 기반 구축 부분은 연계 대상이다. [사실][^ref-347]
- Feng 외, osmAG(arXiv, 2023-09) — 사람이 기존 OSM 도구로 고칠 수 있는 계층형 의미 지도 형식이다(초록 기준). [사실][^ref-1031]
- Xie·Schwertfeger·Blum, osmAG-LLM(RA-L 2026 채택, arXiv 2025-07) — 의미 지도를 LLM 추론의 환경 맥락으로 쓴다(초록 기준). [사실][^ref-1032]
- 국토지리정보원, 실내공간정보(확인일 2026-09-30) — 지하철·철도역사와 평창동계올림픽 관련 시설 등의 LoD2 실내공간정보(2차원 도면·3차원 성과, shp·3ds·max 형식)를 브이월드로 제공하며, 활용처로 공공분야(철도보안시스템, 시설물관리)·민간분야(실내 내비게이션, 메타버스, 좌석안내서비스)를 들고 로봇 활용은 언급하지 않는다. [사실][^ref-1035]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본, 초록 기준), Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-30
[^ref-1031]: Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv), osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics, 2023-09, https://arxiv.org/abs/2309.04791, 접근일 2026-09-30
[^ref-1032]: Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning, 2025-07, https://arxiv.org/abs/2507.12753, 접근일 2026-09-30
[^ref-1035]: 국토지리정보원, 실내공간정보, 미확인, https://www.ngii.go.kr/kor/content.do?sq=324, 접근일 2026-09-30
[^ref-1036]: Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020), Lifelong update of semantic maps in dynamic environments, 2020-10, https://arxiv.org/abs/2010.08846, 접근일 2026-09-30
[^ref-1037]: Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066), Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments, 2023-06-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s4.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 핵심 개념과 용어"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1027, ref-347, ref-1036]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#4
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 핵심 개념과 용어

# 16. 장소 의미·지도 관리 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 지도 자체를 가리키는 말과 지도 위 장소를 가리키는 말로 나뉜다. 아래 정의의 확인일은 따로 적지 않으면 2026-09-30 이다.
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 지도 자체를 가리키는 말과 지도 위 장소를 가리키는 말로 나뉜다. 아래 정의의 확인일은 따로 적지 않으면 2026-09-30 이다.

- **지도 버전(Map Version, mapId·mapVersion)** — [VDA 5050](../../glossary/vda-5050.md) 3.0.0(공식 저장소 main)에서 지도는 작업 공간 구역을 가리키는 mapId 와 갱신을 나타내는 mapVersion 의 조합으로 식별되고, 상태는 ENABLED·DISABLED 이며, 같은 mapId 에서는 한 버전만 활성화된다. [사실][^ref-031]
- **[구역 집합](../../glossary/zone-set.md)(Zone Set, zoneSet)** — VDA 5050 3.0.0 에서 여러 구역을 담은 집합으로, 전역 고유 zoneSetId 를 가지며 mapVersion 이 아니라 mapId 에 묶이고 mapId 당 하나만 활성화된다. [사실][^ref-031]
- **이름·대체 이름(name·alt_name)** — [실내 지도 데이터 형식](../../glossary/indoor-mapping-data-format.md)(Indoor Mapping Data Format, IMDF) 용어집에서 이름은 현실에 물리적으로 있고 보행자에게 표시되어야 할 기준 레이블이고, 대체 이름은 공간·물체·서비스를 가리키는 동의어로 색인·질의·검색에 쓰인다. [사실][^ref-1027]
- **접근 제한(restriction)** — IMDF 에서 직원 전용처럼 일반 대중의 일부에게만 허용된 공간을 나타내는 속성이다. [사실][^ref-1027]
- **의미 지도(Semantic Map)** — Narayana 외(2020-10)는 의미 지도를 로봇과 사용자가 함께 쓰는 공유 표현으로 다뤘다. [사실][^ref-1036]
- **3차원 장면 그래프(3D Scene Graph)** — 물체·장소·방·건물 같은 추상화 층으로 환경을 묶는 계층형 공간 표현이다(arXiv 2305.07154, 2023-05, IJRR 투고본, 초록 기준). [사실][^ref-347]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1027]: Apple (Apple Business Register), Glossary - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/glossary, 접근일 2026-09-30
[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본, 초록 기준), Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-30
[^ref-1036]: Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020), Lifelong update of semantic maps in dynamic environments, 2020-10, https://arxiv.org/abs/2010.08846, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-04/pages/topics/2026/2026-09-30-area16-s10.md

```markdown
---
title: "16. 장소 의미·지도 관리 — 다른 연구영역과의 연결"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 16
related_areas: [8, 12, 14, 15, 18, 21, 27, 44, 45, 51, 57, 63, 65, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-079, ref-046, ref-1027, ref-1028, ref-569, ref-347, ref-1031, ref-1032, ref-1033, ref-956, ref-1036, ref-869]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/place-semantics-and-map-management.md#10
---

[홈](../../index.md) › [주제](../index.md) › 16. 장소 의미·지도 관리 — 다른 연구영역과의 연결

# 16. 장소 의미·지도 관리 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 장소 이름과 지도 버전은 도면·좌표·대화·경로·표준 영역에 두루 쓰인다. [추정][^ref-031][^ref-079]
- 이 페이지는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

장소 이름과 지도 버전은 도면·좌표·대화·경로·표준 영역에 두루 쓰인다. [추정][^ref-031][^ref-079]

- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 장소를 주석할 기준 평면도를 준다. [추정][^ref-869]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 장소 목록이 붙는 좌표 정렬·공간 그래프를 다룬다. [추정][^ref-079][^ref-1031]
- [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) — 대화로 지도를 고칠 때 장소 이름·대체 이름을 쓴다. [추정][^ref-1027][^ref-1032]
- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 지시 속 장소 이름을 지도 위 목적지로 바꾼다. [추정][^ref-1027]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 현재 활성 지도 버전과 폐쇄 구역을 알아야 한다. [추정][^ref-031][^ref-569]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 차선 폐쇄를 경로 계획에 쓴다. [추정][^ref-569]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — LIF·IMDF·IEEE 1873 같은 지도 교환 표준을 다룬다. [추정][^ref-046][^ref-1028][^ref-1033]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 지도 버전 이력을 관리한다. [추정][^ref-031]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 접근 제한 공간을 권한과 연결한다. [추정][^ref-1027]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 의미 지도를 맥락으로 쓰는 언어 모델 추론을 다룬다. [추정][^ref-1032]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 장면 그래프와 의미 지도 구축의 인식 방법을 다룬다. [추정][^ref-347][^ref-1032]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 평면도 주요 위치 주석 사례가 있다. [추정][^ref-869]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 청소 로봇 의미 지도 갱신 사례가 있다. [추정][^ref-1036]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 로봇 친화형 건축물의 정밀지도 사례가 있다. [추정][^ref-956]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/place-semantics-and-map-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
[^ref-1027]: Apple (Apple Business Register), Glossary - Indoor Mapping Data Format, 미확인, https://register.apple.com/resources/imdf/glossary, 접근일 2026-09-30
[^ref-1028]: Open Geospatial Consortium (OGC), Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094, 2021-02-18, https://docs.ogc.org/cs/20-094/index.html, 접근일 2026-09-30
[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-347]: Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본, 초록 기준), Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems, 2023-05, https://arxiv.org/abs/2305.07154, 접근일 2026-09-30
[^ref-1031]: Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv), osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics, 2023-09, https://arxiv.org/abs/2309.04791, 접근일 2026-09-30
[^ref-1032]: Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning, 2025-07, https://arxiv.org/abs/2507.12753, 접근일 2026-09-30
[^ref-1033]: IEEE Standards Association (IEEE RAS), IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation, 2015-10-26, https://standards.ieee.org/standard/1873-2015.html, 접근일 2026-09-30
[^ref-956]: 지디넷코리아, 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-30
[^ref-1036]: Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020), Lifelong update of semantic maps in dynamic environments, 2020-10, https://arxiv.org/abs/2010.08846, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-04 | 16. 장소 의미·지도 관리 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1013건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 270개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [16] 에 걸린 3건 / 전체 199건)

```markdown
- oq-188 [열림] 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (영역 66, 60, 16)
- oq-190 [열림] 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? (영역 66, 21, 16)
- oq-193 [열림] 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? (영역 67, 14, 16)
```
