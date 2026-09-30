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
- verification_stage: first
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
        "ref-1025"
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
        "ref-1029"
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
        "ref-1030"
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
        "ref-1034"
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
        "ref-1029"
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
        "ref-1029"
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
        "ref-1030",
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
        "ref-1029",
        "ref-1025",
        "ref-1028",
        "ref-1033",
        "ref-1030",
        "ref-1036",
        "ref-1034"
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
      "id": "ref-1025",
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
      "id": "ref-1029",
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
      "id": "ref-1030",
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
      "id": "ref-1034",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 18회/30, 신규 출처 13건/15, 재사용 3건(ref-031·ref-079 는 github_raw 로 다시 열었고 ref-869 는 2026-09-30-03 브리프 재인용으로 이번에 열지 않음). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1014 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-03)가 ref-1015·ref-1017·ref-1019·ref-1024 를 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1025~ref-1037 을 순서대로 썼다. 원문 열람: 신규 13건 모두 열었다(webfetch 11건, github_raw 2건). 논문은 대부분 초록 페이지이고 Stefanini 외(ref-1037)만 PMC 본문을 열었다. 열지 못해 쓰지 않은 것: Nav2 문서(404·연결 거부), MiR Fleet 참조 안내서 PDF(본문 추출 실패), VDMA LIF 가이드라인 PDF(본문 추출 실패), LIF GitHub 저장소 페이지(403), MDPI·preprints.org(403), IEEE 1873 해설 논문(ECONNRESET). 교차 확인 0건, 신뢰도 high finding 없음(사실 finding 은 모두 단일 출처; IMDF 는 Apple 문서와 OGC 게시본이 같은 원천이라 독립 출처로 보지 않음). 분류 원문 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에는 f20 으로 답했고, 결론은 '장소 목록을 지도 요소에 묶고, 지도 버전 교체와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 변경을 나눠 관리한다'는 추정이다. 현장 유형 사례는 병원(f11, 재인용)·가정(f12)·기타(f18)이며, 물류창고 근거는 모의 실험(f13)뿐이라 site_type 을 null 로 두었다. 국내 자료는 국토지리정보원(ref-1035)·지디넷코리아(ref-1034) 두 건이며 국내 로봇 지도 표준(KS)은 검색 2회에서 찾지 못했다. L. AI·학습 기술 관련(f14 장면 그래프, f16 LLM 추론)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 활성 지도 버전·폐쇄 구역으로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 IMDF·IndoorGML·LIF·구역 집합·차선 폐쇄·필터 마스크·위상 지도·반정적 객체·공간 그래프는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다."
  }
}
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

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md (요약)

```markdown
# 14. 도면·BIM에서 지도 만들기

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
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

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-09-30-03/research.md

```markdown
# 리서치 브리프 2026-09-30-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-03 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 14. 도면·BIM에서 지도 만들기 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 기준점(fiducial), 공간 경계, 설계–준공 편차, 포즈 그래프 지도 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(도면 주석·로봇 지도 정합), 기타(대학 건물 BIM 기반 위치 추정) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 래스터 평면도 벡터화, CAD 기호 인식, BIM→점유 격자·위상 지도 변환, 축척 보정·좌표 변환 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IFC 4.3(IfcSpace·IfcTransportElement), Open-RMF 교통 편집기·플릿 어댑터 좌표 변환 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — CubiCasa5K, Raster-to-Vector, FloorPlanCAD, AI Hub 건축 도면 데이터, BIM 기반 위치 추정 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]
2. 평면도(이미지·CAD)에서 벽·문·공간·기호를 인식하는 대표 방법과 공개 데이터셋(국내 데이터 포함)은 무엇이며 보고된 성능은 어느 수준인가? (섹션 4·6·8 겨냥)
3. IFC 같은 BIM(Building Information Modeling)에서 공간·문·승강기를 가져와 로봇 지도(점유 격자·위상 지도)를 만드는 표준 요소·연구·도구는 무엇인가? (섹션 6·7·8 겨냥)
4. 도면 픽셀을 미터로 보정하고 제조사별 로봇 지도를 도면 좌표에 맞추는 절차는 오픈소스 관제(Open-RMF)와 제품에서 어떻게 이루어지며, 누가 확인하는가? (섹션 5·6·7 겨냥, oq-126 관련)
5. 도면·BIM 과 실제 현장이 다를 때(설계–준공 편차, 가구·배치 변경) 어떻게 확인하고 반영하는가? (섹션 3·6·11 겨냥, oq-193 관련)
6. 병원·건설 현장 등 실제 현장에서 도면 기반 지도를 쓴 사례는 무엇이며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥)
7. 도면·BIM 지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 위치 추정·BIM 저작·설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 교통 편집기(traffic-editor)는 건축 도면 같은 기존 평면도 이미지를 배경으로 불러와 그 위에 교통 기반 시설을 그리게 하며, 주석은 기준 평면도 이미지의 왼쪽 위를 원점으로 하는 픽셀 좌표로 만들어지고 평면도가 제조사별 로봇 지도의 기준 좌표계 역할을 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | Open-RMF 교통 편집기에서 도면 축척은 도면의 축척 막대처럼 실제 거리를 아는 두 점 사이에 측정선을 긋고 실제 길이를 미터로 입력해 층별 픽셀–미터 비율을 정하는 방식으로 설정한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f3 | [사실] | Open-RMF 교통 편집기는 여러 층을 맞출 때 기둥처럼 층 사이에 수직으로 같은 위치에 있을 것으로 기대되는 기준점(fiducial)을 층마다 찍고, 이를 대응시켜 층 사이의 이동·회전·축척 변환을 자동으로 계산한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f4 | [사실] | Open-RMF 교통 편집기에서 도면 위에 주석으로 표현하는 요소는 벽, 문(여닫이·미닫이 등 유형 지정), 여러 층에 걸친 승강기(층별 카 문 위치 포함), 이동 그래프를 이루는 차선(lane), 충전 위치(is_charger 속성의 지점)다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f5 | [사실] | Open-RMF 교통 편집기는 로봇이 만든 지도를 레이어로 불러와 축척·이동·회전 변환을 주어 기준 평면도와 겹치도록 맞추게 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 교통 편집기 좌표계가 다르면 두 좌표계에서 서로 대응하는 지점 쌍(reference_coordinates)을 설정 파일에 적게 하고 최소 4개 대응 지점을 권장하며, nudged 라이브러리로 회전·축척·이동 변환을 추정해 명령 좌표를 자동으로 바꾼다. | ref-153 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | Valner 외(Frontiers in Robotics and AI, 2022-08)에 따르면 에스토니아 타르투 대학병원 현장 시험에서는 PAL Robotics TIAGo 를 원격 조작해 SLAM 으로 격자 지도를 만들고, 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합해 두 좌표 표현 사이 변환을 정했으며, 이 지도로 중환자실에서 검사실까지 시간이 중요한 혈액 검체를 운반하고 RFID·근접 센서로 여는 반자동 문 두 곳을 통과했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 수행 자원 | — |
| f8 | [사실] | 같은 타르투 대학병원 시험의 저자들은 넓은 구역을 한 번에 매핑하면 누적 불확실성 때문에 지도가 비틀리기 쉬우므로 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확하다고 보고했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 예외·성과 | — |
| f9 | [사실] | IFC 4.3 문서에서 IfcSpace 는 건물 안에서 특정 기능을 제공하는 실제 또는 이론상 경계로 둘러싸인 면적·부피이며, IfcRelAggregates 로 층(building storey, 외부 공간은 site)에 속해 공간 계층을 이루고 IfcRelSpaceBoundary 로 물리적·가상 경계가 정의된다. | ref-156 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | IFC 4.3 문서에서 IfcTransportElement 는 시설 안에서 사람·동물·물품을 옮기는 운송 요소 전체를 일반화한 요소로, 승강기(lift)·에스컬레이터·무빙워크를 포함하며 PredefinedType 이나 IfcTransportElementType 으로 구분한다. | ref-213 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f11 | [사실] | Kalervo 외(2019)의 CubiCasa5K 는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 주석한 데이터셋이며, 저자들은 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 합성곱 신경망으로 평면도를 자동 해석하는 방법을 함께 제시했다. | ref-063 | 아니오 | medium | 2019-04 | — | — |
| f12 | [사실] | Liu·Wu·Kohli·Furukawa(ICCV 2017)의 Raster-to-Vector 는 신경망으로 벽 모서리·문 끝점 같은 접합점을 찾고 정수 계획법으로 이를 벽선·문선·아이콘 상자로 묶어 위상·기하가 일관된 벡터 평면도를 만들며, 저자 평가에서 정밀도·재현율 약 90%를 얻고 실제 서비스용 평면도 이미지 수십만 장을 벡터로 변환했다고 보고했다. | ref-1015 | 아니오 | medium | 2017 | — | — |
| f13 | [사실] | Fan 외(ICCV 2021)의 FloorPlanCAD 는 주거·상업 건물의 벡터 CAD 평면도 1만 장 이상을 30개 객체 범주로 선 단위 주석한 데이터셋으로, 셀 수 있는 사물 인스턴스와 셀 수 없는 영역의 의미를 함께 찾는 파놉틱 심볼 스포팅 과제와 CNN–GCN 결합 방법을 제시했다. | ref-067 | 아니오 | medium | 2021-05 | — | — |
| f14 | [사실] | AI Hub 의 '건축 도면 데이터'(2022년 구축, 주관기관 에이치씨아이플러스)는 평면도 41,556장을 포함한 건축 도면 48,033장으로 이루어지며, 출입문·창호·벽체 등 구조 8종, 거실·침실·주방·현관·화장실 등 공간 12종, 객체 5종 라벨과 문자 인식(OCR) 304,462건을 담은 인공지능 학습용 데이터다. | ref-1019 | 아니오 | medium | 2026-09-30 | — | — |
| f15 | [사실] | 연계 대상: Hendrikx 외(ICRA 2021)는 IFC 형식 BIM 의 의미 요소를 로봇용 세계 모델 표현으로 바꿔 공간 데이터베이스에 저장하고, 로봇 주변의 구조 요소를 질의해 특징 검출기를 설정한 뒤 그래프 기반 방법으로 위치를 추정해, 2D LiDAR 와 주행거리계만 가진 로봇이 BIM 이 있는 대형 대학 건물에서 자세를 추적할 수 있음을 보였다. | ref-1017 | 아니오 | medium | 2021 | 기타 | — |
| f16 | [사실] | Vega Torres·Braun·Borrmann(ECPPM 2022)은 복잡한 BIM 에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 방법을 제안했으며, BIM 과 현실의 차이(Scan-BIM 편차)가 가구·잡동사니뿐 아니라 설계 모델과 준공 상태의 차이에서도 생긴다고 지적하고, 제안 방법이 변화·동적 환경에서 일반 AMCL 보다 강건하게 위치를 추정했다고 보고했다. | ref-081 | 아니오 | medium | 2022-09 | 제약 | — |
| f17 | [사실] | 연계 대상: 같은 연구진의 BIM-SLAM(ISARC 2023, arXiv 2024-08)은 BIM 에서 포즈 그래프 지도·기술자 같은 세션 데이터를 먼저 만들고 다중 세션 앵커링으로 실제 LiDAR 측정과 맞추며, BIM 에 없는 요소를 찾아 묶고 표면으로 재구성해 설계 모델과 실제 실내 상태의 차이를 드러내고, 로봇의 초기 자세를 몰라도 BIM 에 정렬된 지도를 만든다. | ref-221 | 아니오 | medium | 2024-08 | 제약 | — |
| f18 | [사실] | Zhang·Wu·Ma·Schwertfeger(arXiv 2507.00552, 2025-07; 2026-03 개정)는 SLAM 매핑의 시간·노력·강건성 한계를 피하려고 건축 CAD 파일에서 구조 요소를 추출하고 AreaGraph 기반 위상 분할로 이동 가능한 공간을 나누며 CAD 의 문자 라벨을 넣고 여러 층을 합쳐 로봇 항법용 계층형 위상·거리 OpenStreetMap 실내 지도를 자동 생성하는 파이프라인과 GUI 를 공개했다. | ref-083 | 아니오 | medium | 2025-07 | — | — |
| f19 | [추정] | 모빌리오(Mobilio Robotics)는 자사 산업용 순찰 로봇 관제 솔루션이 사용자가 기둥·모서리 같은 기준점 3개 이상을 지정하면 2D LiDAR 지도를 CAD·BIM 도면에 정합하고 회전각·크기를 미세 조정해 로봇 위치를 실제 도면 위에 보여 주며, 공장·플랜트를 대상으로 한다고 주장한다. | ref-817 | 아니오 | low | 2026-08-24 | — | 벤더 주장 |
| f20 | [사실] | 엔지니어링데일리 보도에 따르면 국토교통부의 건설산업 BIM 활성화 로드맵은 설계 단계부터 BIM 100% 도입을 핵심 목표로 삼고 측량·설계·시공·감리·유지관리까지 전 단계에 BIM 을 쓰게 하며, LH 공공주택부터 BIM 적용을 의무화해 단계적으로 넓히는 계획을 담았다. | ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에 대해, 평면도의 벽·문·공간·기호 인식과 BIM·CAD 에서 점유 격자·위상 지도를 만드는 일은 연구 수준에서 자동화가 진행됐지만(f12·f13·f16·f18), 축척 설정·로봇 지도와의 좌표 정합·설계–준공 편차 확인은 측정선·기준점 입력과 사람의 확인에 기대고 있어(f2·f3·f6·f7·f16), 현재 형태는 '자동 초안 + 사람 확인·보정'에 가깝다. | ref-1015, ref-067, ref-081, ref-083, ref-079, ref-153, ref-869 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 도면·BIM 지도가 중요한 까닭은, 넓은 공간을 로봇으로 매핑하면 지도가 비틀리기 쉽고 제조사마다 지도 좌표가 다른 반면 평면도는 여러 제조사 로봇 지도를 묶는 공통 기준 좌표와 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점을 주기 때문이다(f1·f4·f8·f10). | ref-079, ref-869, ref-213 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 14. 도면·BIM에서 지도 만들기에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고(f4·f9·f10), 층별 축척과 층 간 기준점을 설정하며(f2·f3), 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고(f5·f6), 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일이다(f16, oq-126 과 연결). | ref-079, ref-153, ref-156, ref-213, ref-081 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정 포함)은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속하므로, 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다. | ref-1017, ref-081, ref-221, ref-213, ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 좌표 정렬·다층 모델을 다루는 15. 지도·공간·위치 모델(f3·f5·f6), 지도 편집·버전을 다루는 16. 장소 의미·지도 관리(f1·f16), 대화로 맵을 만드는 8. 채팅으로 맵 작성(f2·f6), 도면 해석 AI 를 다루는 45. 문서·도면·장면 이해(f11~f14), 승강기·문 연동을 다루는 22. 설비·건물 시스템 연동(f4·f10), 충전 위치를 다루는 28. 공용 자원·충전·에너지 최적화(f4), 차선 그래프를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f4), 설치 때 매핑·정합을 하는 55. 현장 조사·설치·시운전(f7·f8), 현재 상태의 차이를 다루는 18. 실시간 세계 상태·데이터 일관성(f17), 병원 적용을 다루는 63. 병원·의료(f7)와 이어진다. | ref-079, ref-153, ref-081, ref-063, ref-1015, ref-067, ref-1019, ref-213, ref-869, ref-221 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-156 | buildingSMART International | IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md | 아니오 |
| ref-213 | buildingSMART International | IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-1015 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017) | Raster-to-Vector: Revisiting Floorplan Transformation | 2017 | 논문 | medium | 2026-09-30 | https://art-programmer.github.io/floorplan-transformation.html | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-1017 | Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021) | Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization | 2021 | 논문 | medium | 2026-09-30 | https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/ | 아니오 |
| ref-081 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022) | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2022-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2308.05443 | 아니오 |
| ref-1019 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-817 | 모빌리오(Mobilio Robotics) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션) | 2026-08-24 | 벤더 문서 | low | 2026-09-30 | https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98 | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv) | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.00552 | 아니오 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023) | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 2024-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2408.15870 | 아니오 |
| ref-1024 | 엔지니어링데일리 | "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 … (제목 일부만 확인) | 미확인 | 기사 | low | 2026-09-30 | https://www.engdaily.com/news/articleView.html?idxno=12613 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(공통 기준 좌표·공용 자원 목록의 출발점), f8(넓은 구역 매핑의 누적 오차), f20(국내 BIM 전 단계 적용 정책, 기사 기준 신뢰도 low) / 섹션 4: 기준점(fiducial) f3, 공간·공간 경계 f9, 운송 요소 f10, 설계–준공 편차 f16, 포즈 그래프 지도 f16 / 섹션 5: 병원 — f7(타르투 대학병원 평면도 주석·격자 지도 정합·검체 운반), f8(예외·성과); 기타 — f15(대학 건물 BIM 기반 위치 추정, 연계 대상 표시). 여섯 항목 가운데 시작 조건·완료·인계 근거는 부족함을 명시 / 섹션 6: 래스터 평면도 벡터화 f12, CAD 기호 인식 f13, 평면도 해석 데이터셋 f11·f14, BIM→점유 격자·포즈 그래프 f16, CAD→위상 OSM f18, 축척 보정 f2, 층 정렬 f3, 로봇 지도 정합 f5·f6, 편차 검출 f17, 제품 사례 f19(벤더 주장 병기 필수), 자동화 수준 종합 f21 / 섹션 7: IFC 4.3 f9·f10, Open-RMF 교통 편집기 f1~f5, 플릿 어댑터 좌표 변환 f6 / 섹션 8: f11~f18, f7 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 8, 15, 16, 18, 22, 27, 28, 45, 55, 63 / 섹션 11: 기존 oq-126·oq-193 과 open_questions_new 4건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 f6(대응점 기반 좌표 변환) 반영, 45. 문서·도면·장면 이해 페이지에 f11~f14 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 층 정렬 기준점 | Fiducial (Level Alignment Fiducial) | 기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다. |
| 공간 경계 | Space Boundary (IfcRelSpaceBoundary) | IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다. |
| 설계–준공 편차 | As-planned vs As-built Deviation | 설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다. |

## 열린 질문

새로 생긴 질문:

- Raster-to-Vector 의 약 90% 정밀도·재현율처럼 보고된 평면도 인식 성능은 주로 주거용 도면 기준인데, 병원·공장·물류창고 같은 비주거 시설 도면에서 벽·문·승강기·충전 위치 인식 정확도를 보고한 자료가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f12 | 종류: 일반
- AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 승강기·계단·충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f14 | 종류: 일반
- 도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 제품 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 55. 현장 조사·설치·시운전 | 근거: f6 | 종류: 일반
- 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 22. 설비·건물 시스템 연동 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f20 국토교통부 원문 보도자료(molit.go.kr)는 ECONNRESET 으로 열지 못해 기사 기준이며, 공공공사 금액별 BIM 의무화 연도(검색 요약에만 나옴)는 넣지 않음
    - ref-1024 기사 발행일과 제목 전체 미확인
    - ref-817 모빌리오 글의 제목 전체 미확인, 정합 기능·성능은 벤더 주장이며 독립 확인 없음
    - ref-1019 AI Hub 데이터 공개일 미확인(구축 연도 2022 만 확인)
    - f11~f13·f15~f18 은 논문 초록·프로젝트 페이지 기준이며 본문의 실험 조건 미확인(Raster-to-Vector CVF 본문 403)
    - f12 의 약 90% 수치는 저자 평가이며 교차 확인 실패
    - f9·f10 은 IFC 4.3 개발 브랜치 문서 기준으로 게시판(ADD2)과의 문구 일치 미확인
    - 도면 인식 결과를 로봇 지도로 확정하는 승인 주체·시점(oq-126)은 어느 자료에서도 확인되지 않음
    - 건설 현장 지도–BIM 동기화 주기와 국내 사례(oq-193)는 이번 조사에서 확인되지 않음
    - 병원 외 현장 유형(물류창고·제조 공장·상업 시설)의 도면 기반 지도 사례는 벤더 주장(f19) 외에 확인되지 않음
- 범위 경계 위반 의심:
    - f15·f17: BIM 을 사전 지도로 쓰는 로봇 위치 추정·SLAM 은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f16: BIM→점유 격자 지도 생성은 직접 범위 후보이나 AMCL 비교 등 위치 추정 성능 부분은 로봇 자체 지능·제어 쪽 근거로만 쓰도록 제안함
    - f24: 승강기 제어(시설·설비 제어), BIM 저작·갱신(건물 측 체계)을 '연계 대상: '으로 표시함
    - f20: BIM 정책은 이 영역의 입력 데이터 가용성 근거로만 쓰고 ROP 직접 범위로 서술하지 않음
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: finding f7 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음): 직전 반환값(runs/2026-09-30-03/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. finding·출처 번호는 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-817)만 근거로 한 finding 은 f19 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 이번 f7 은 동료심사 논문(ref-869, Frontiers)에 근거한 병원 사례이며 벤더 문서를 근거로 하지 않는다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f7, f19). web_fetch_available: true · fetch_mode full. 사용량은 검색 13회/30, 신규 출처 15건/15(ref-079~ref-1024, 예약 구간 안)로 출처 상한에 도달했다. 그래서 BIM2RDT(건설 현장 BIM–로봇 디지털 트윈, arXiv 2509.20705, 열었음), 평면도 사전지식 기반 장기 위치 추정(arXiv 2303.10959), IFC→ROS 지도 도구 BIRS, Nav2 지도 YAML 형식(해상도·원점; 문서 URL 404)은 넣지 못했다. 원문 열람: 15건 모두 열었다(github_raw 4건, webfetch 11건). 논문은 대부분 초록 페이지다. 열지 못해 쓰지 않은 것: 국토교통부 보도자료·ancnews(ECONNRESET), 한국경제(403), Springer 'Improving autonomous robotic navigation using IFC files'(인증 리디렉션), CVF 논문 페이지(403). 교차 확인 0건, 신뢰도 high finding 없음(모든 사실 finding 이 단일 출처). 분류 원문 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에는 f21 로 답했고 결론은 '인식·변환은 연구 수준에서 자동화됐으나 축척·정합·편차 확인은 사람 입력·확인에 기대는 자동 초안 + 사람 확인 형태'라는 추정이다. 현장 유형 사례는 병원(f7·f8)과 기타(f15, 대학 건물)이며, 물류창고·제조 공장·상업 시설 사례는 벤더 주장(f19, 현장 유형 미특정) 외에 찾지 못했다. 국내 자료는 AI Hub(ref-1019)·엔지니어링데일리(ref-1024)·모빌리오(ref-817) 세 건이다. L. AI·학습 기술 관련(평면도 인식 f11~f14)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 상태와 BIM 차이(f17)로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 평면도 인식·래스터–벡터 변환·파놉틱 심볼 스포팅·스캔 대 BIM 비교·지도 정합·유사 변환·IFC·점유 격자 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 은 관련 근거(f6·f7, f16·f17)가 늘었으나 해결되지 않았다.
```

### runs/2026-09-30-02/research.md

```markdown
# 리서치 브리프 2026-09-30-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-02 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 67. 기타 현장 |
| 대분류 | Q. 현장 유형별 적용 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — SiLA 2·자율 실험실·브레인리스 로봇·정상 무인 시설 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 플랜트·변전소 점검, 건설 현장, 농업, 공항, 오피스 빌딩, 데이터센터, 연구실 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 점검 데이터 수집·AI 분석, BIM 비교, 작업자 추종·유도선 주행, 클라우드 두뇌 로봇 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 이동 로봇 화학자(Nature 2020) 등 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
2. 플랜트·변전소·데이터센터의 점검·순찰 로봇은 무엇을 점검하고 어떤 설비·통신 조건에서 운영되는가? (섹션 3·5·6 겨냥)
3. 건설 현장에서 로봇은 매일 바뀌는 현장 상태를 BIM(Building Information Modeling)과 어떻게 대조하고 무엇을 기록하는가? (섹션 5·6 겨냥, 한국 자료 우선)
4. 농업 현장에서 여러 로봇을 함께 운영하는 국내 사례와 관리 방식(통합 관리 프로그램, 수확·운반 분업, 작업자 추종)은 무엇인가? (섹션 5·6·8 겨냥)
5. 공항·오피스 빌딩·연구실 같은 공공시설·업무 공간에서 로봇은 무엇을 하고 승강기·출입문·실험 장비와 어떻게 연동되는가? (섹션 5·6 겨냥)
6. 기타 현장에 적용되는 표준·프레임워크(ISO 18497, SiLA 2, 싱가포르 SS 713·TR 130, Open-RMF)는 무엇을 다루는가? (섹션 7 겨냥)
7. 기타 현장에서 ROP 가 직접 맡을 것과 로봇 자체 기능·설비·업무 시스템·업종별 규정에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Offshore Technology(2025-11-21)에 따르면 Equinor 는 2024-11부터 평소 사람이 상주하지 않도록 설계된 노르웨이 Northern Lights 이산화탄소 포집·저장(CCS) 시설에 ANYbotics 의 4족 로봇 ANYmal('Roberta')을 배치해 계기 판독·밸브 위치 확인·CO2 농도 감시·누출 탐지를 맡겼으며, 현장 운영자가 연구개발 부서 지원 없이 직접 임무를 만들기 시작했다. | ref-995 | 아니오 | medium | 2025-11-21 | 기타 / 작업 대상 | — |
| f2 | [추정] | Equinor 는 로봇을 폭넓게 도입하면 연간 10억 노르웨이 크로네(약 9,910만 달러)를 넘는 비용을 절감할 것으로 추산한다. | ref-995 | 아니오 | low | 2025-11-21 | 기타 / 예외·성과 | — |
| f3 | [사실] | 넷매니아즈(2023-09-30)가 정리한 한국전력공사 실증 자료에 따르면 한전은 2022-12 신중부 변전소에 5G 특화망을 구축하고 4족 로봇이 아날로그·디지털 계기와 LED·밸브·램프 상태를 촬영하고 열화상 영상을 모아 AI 서버로 스트리밍하게 했으며, 무선 IoT 센서와 무선 CCTV(추락·쓰러짐·위험지역 접근·화재·침입 감지)를 함께 운영했다. | ref-1008 | 아니오 | medium | 2023-09-30 | 기타 / 작업 대상 | — |
| f4 | [추정] | Energy Robotics(2026-05 Korial 로 사명 변경)는 하드웨어에 독립적인 로봇 운영 소프트웨어와 클라우드 기반 플릿 관리, AI 데이터 분석을 결합한 산업 점검 플랫폼을 내세우며, Boston Dynamics Spot·ExRobotics ExR-1 을 포함해 20개가 넘는 하드웨어 플랫폼을 제어하도록 소프트웨어를 맞춰 왔다고 주장한다. | ref-1003 | 아니오 | low | 2021-01-15 | 수행 자원 | 벤더 주장 |
| f5 | [사실] | 서울신문(2022-11-15)에 따르면 현대건설은 건설 현장의 안전·품질 관리에 4족 보행 로봇 스팟을 투입해 현장 사진 촬영·기록 자동화, 영상·환경 센서 실시간 모니터링, 레이저 스캐닝 3D 데이터 수집, QR 코드 기반 자재 추적, 출입 제한 구역 위험 경보를 하게 하고, 사무실에서 현장을 실시간으로 확인하게 했으며, 2023년 김포–파주 고속도로 현장에서 시범 운영할 계획이었다. | ref-999 | 아니오 | medium | 2022-11-15 | 기타 / 작업 대상 | — |
| f6 | [사실] | 인더스트리뉴스에 따르면 GS건설은 2020-07 큐픽스와 함께 스팟을 국내 건설 현장에 처음 도입해 성남 아파트 현장(지하주차장 골조·세대 내부 마감)과 서울 공연장 신축 현장에서 실증했고, 로봇에 단 LiDAR·360도 카메라·IoT 센서로 모은 데이터를 기존 3차원 BIM 데이터와 통합해 전기·설비 공사 간섭 확인과 안전관리계획 수립에 썼다. | ref-1000 | 아니오 | medium | 2026-09-30 | 기타 / 완료·인계 | — |
| f7 | [사실] | 이코노미스트(2023-01-11)에 따르면 네이버 제2사옥 1784 에서는 로봇이 초기 40대에서 약 100대로 늘었고, 두뇌를 클라우드에 둔 '브레인리스' 배달 로봇 루키를 네이버 클라우드와 5G 특화망 기반의 멀티 로봇 시스템 ARC(AI·Robot·Cloud)가 제어하며, 루키는 로봇 전용 엘리베이터 로보포트로 층을 오가며 커피·택배를 자리까지 배달하고 충전소로 돌아간다. | ref-997 | 아니오 | medium | 2023-01-11 | 기타 / 수행 자원 | — |
| f8 | [추정] | 네이버는 1784 사옥 로봇 배달 시간이 초기 15~17분에서 5~10분으로 줄었다고 밝혔다. | ref-997 | 아니오 | low | 2023-01-11 | 기타 / 예외·성과 | 벤더 주장 |
| f9 | [사실] | 아주경제(2023-11-08)에 따르면 네이버 데이터센터 각 세종에서는 네이버랩스가 개발한 서버 관리 로봇 '세로'와 서버실·창고를 오가며 고중량 자산을 나르는 운반 로봇 '가로'가 협력해 자산 흐름을 실시간으로 추적·관리하고, 두 로봇은 ARC 와 ARM 시스템을 통해 공간·서비스 인프라와 실시간으로 연동된다. | ref-1002 | 아니오 | medium | 2023-11-08 | 기타 / 작업 대상 | — |
| f10 | [사실] | 로봇신문(2018-07-11)에 따르면 인천국제공항공사는 2018-07-21부터 푸른기술·LG CNS 컨소시엄이 만든 안내 로봇 에어스타를 제1여객터미널 8대·제2여객터미널 6대로 운영해 출국장·면세지역·입국장 수하물 수취 지역에서 항공편·체크인 카운터 안내, 목적지 에스코트, 4개 국어 음성 안내, 기내 반입 금지 물품 회수를 하게 했다. | ref-998 | 아니오 | medium | 2018-07-11 | 기타 / 작업 대상 | — |
| f11 | [사실] | The Robot Report(2025-10-29)에 따르면 싱가포르 국가 로봇 프로그램이 2018년 ROS 기반으로 함께 출범시킨 로봇 미들웨어 프레임워크(RMF, 현 Open-RMF)는 제조사가 다른 로봇과 시스템이 함께 일하게 하는 것으로, 창이 공항 같은 대형 시설에서 이미 운영되고 있다. | ref-1004 | 아니오 | medium | 2025-10-29 | 기타 / 수행 자원 | — |
| f12 | [사실] | 같은 기사에 따르면 싱가포르는 로봇·승강기·자동문 사이 데이터 교환 표준 SS 713 과 로봇·중앙 관제 시스템 상호운용 기술 참조 TR 130 을 두고 SS 713 을 ISO 국제표준으로 올리려 하며, BCA Braddell 캠퍼스의 ELEVATE 시험장에서 로봇·승강기·건물 시스템의 상호작용을 시험한다. | ref-1004 | 아니오 | medium | 2025-10-29 | 기타 / 제약 | — |
| f13 | [사실] | Burger 외(Nature 583, 2020)는 사람과 비슷한 크기·팔 길이의 이동 매니퓰레이터가 개조하지 않은 일반 습식 화학 실험실에서 8일 동안 자율로 움직이며 분석 장비를 다뤄 10개 변수 공간에서 688회 실험을 수행하고, 배치 베이지안 탐색으로 초기보다 6배 활성이 높은 광촉매 조합을 찾았다고 보고했다. | ref-996 | 아니오 | medium | 2020-07 | 기타 / 수행 자원 | 원문 미열람 |
| f14 | [사실] | SiLA 컨소시엄의 SiLA 2 는 실험실 장비를 'SiLA 서버'로 보고 서버의 능력을 Command(매개변수를 받는 동작)와 Property(읽거나 구독하는 데이터)를 담은 Feature 로 기술하며, 서버·Feature 자동 탐색과 gRPC(HTTP/2·Protocol Buffers) 통신을 규정하고, 1.1 판은 클라우드 연결용 서버 주도 연결 방식을 더했으나 워크플로 오케스트레이션은 표준 범위 밖이다. | ref-1001 | 아니오 | medium | 2026-09-30 | — | — |
| f15 | [사실] | 뉴스토마토(2025-04-23)에 따르면 농촌진흥청은 자체 개발한 방제 로봇(2022)·운반 로봇(2023)·모니터링 로봇(2024)을 개인용 컴퓨터나 휴대전화 하나로 함께 관리하는 통합 관리 프로그램을 개발했으며, 이 프로그램은 로봇의 위치·속도·이동 거리와 운영 통계를 보여 주고 작업 순서를 설정하며, 모니터링 로봇 영상으로 수확 가능한 열매 수·위치·익은 정도를 알려 주고 작업·작물 정보로 방제 횟수와 수확 시기를 조절하게 한다. | ref-1007 | 아니오 | medium | 2025-04-23 | 기타 / 수행 자원 | — |
| f16 | [사실] | 농민신문(2024-03-25)에 따르면 농촌진흥청이 스마트팜에 시범 보급한 작업자 추종 운반 로봇은 3D 카메라로 작업자와 10cm~1m 간격을 유지하며 따라가고, 최대 300kg 을 싣고 한 번 충전으로 10시간 운행하며, 바닥의 바코드 유도선을 따라 재배 현장과 집하장 사이를 자율로 오간다. 2024년에는 8개 지역 10개 농가를 대상으로 시범사업을 진행했고, 로봇 속도와 유도선 내구성이 개선 과제로 꼽혔다. | ref-1006 | 아니오 | medium | 2024-03-25 | 기타 / 예외·성과 | — |
| f17 | [추정] | 헬로디디 보도에 따르면 한국기계연구원은 온실에서 작물을 수확하는 수확 로봇과 수확물을 하역장까지 자율로 나르는 이송 로봇으로 수확부터 운반까지 나눠 맡는 원예작물 수확 다수 로봇 시스템을 개발했으며, 연구진은 작물 인식률 90% 이상, 24시간 운영을 가정하면 사람의 80% 효율로 수확할 수 있다고 밝혔다. | ref-1005 | 아니오 | low | 2026-09-30 | 기타 / 수행 자원 | — |
| f18 | [사실] | ISO 18497 은 2024년 판에서 부분 자동·반자율·자율 농업기계·트랙터의 안전을 설계 원칙·용어(1부), 장애물 보호 시스템(2부), 자율 운용 구역(3부), 검증 방법·타당성 확인 원칙(4부)의 네 부분으로 나눠 다룬다. | ref-1009 | 아니오 | medium | 2024 | 기타 / 제약 | 원문 미열람 |
| f19 | [추정] | 확인한 자료를 종합하면 67. 기타 현장의 로봇 작업은 (1) 플랜트·변전소 점검·순찰(f1·f3), (2) 건설 현장 공정·품질·안전 점검(f5·f6), (3) 농업의 방제·운반·모니터링·수확(f15~f17), (4) 공항 같은 공공시설의 안내·청소(f10·f11), (5) 오피스 빌딩 사내 배달(f7), (6) 데이터센터 서버 자산 운반·관리(f9), (7) 연구실 실험 수행(f13)의 일곱 형태로 나타난다. | ref-995, ref-1008, ref-999, ref-1000, ref-1007, ref-1006, ref-1005, ref-998, ref-1004, ref-997, ref-1002, ref-996 | 아니오 | low | 2026-09-30 | 기타 / 작업 대상 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(다른 현장은 무엇이 다른가)에는 다음과 같이 답할 수 있다. 점검·순찰 현장은 사람이 상주하지 않거나 위험한 설비에서 계기값·열화상·가스 농도 같은 '정보'를 작업 대상으로 삼는다(f1·f3). 건설 현장은 공간이 날마다 바뀌어 수집 데이터를 BIM 과 대조한다(f5·f6). 농업은 비정형 지면과 계절성 때문에 작업자 추종·유도선 주행과 작물 상태 판단이 함께 들어간다(f15·f16). 공항은 다국어 안내·에스코트처럼 사람을 대상으로 한다(f10). 오피스·데이터센터는 전용 승강기·클라우드·5G 같은 건물 인프라에 기댄다(f7·f9). 연구실은 분석 장비 조작과 실험 계획이 한 루프로 묶인다(f13·f14). | ref-995, ref-1008, ref-999, ref-1000, ref-1007, ref-1006, ref-998, ref-997, ref-1002, ref-996, ref-1001 | 아니오 | low | 2026-09-30 | 기타 | — |
| f21 | [추정] | 확인한 자료를 종합하면 기타 현장 로봇 작업의 여섯 항목은 다음처럼 채울 수 있다. 시작 조건은 점검 일정·현장 운영자가 만든 임무, 사내 배달 주문, 여객 질의, 실험 계획 알고리즘의 다음 실험 선택이다(f1·f7·f10·f13). 작업 대상은 계기·밸브·열화상 같은 설비 정보, 공사 공간과 자재, 작물·수확물, 서버 자산, 여객, 시료다(f3·f5·f9·f10·f15). 수행 자원은 4족 점검 로봇·클라우드 제어 배달 로봇·전용 승강기·농업 로봇과 작업자·실험 장비다(f1·f7·f13·f16). 제약은 위험 구역·방폭·통신망·유도선·자율 운용 구역이다(f3·f5·f16·f18). 완료·인계는 점검 영상의 AI 서버 전송과 BIM 대조 결과, 자리까지의 배달, 집하장 하역이다(f3·f6·f7·f16). 예외·성과는 출동 감소·비용 절감 추산·배달 시간 단축 같은 주장과 속도·유도선 내구성 문제다(f2·f8·f16). | ref-995, ref-997, ref-998, ref-996, ref-1008, ref-999, ref-1002, ref-1007, ref-1006, ref-1000, ref-1009 | 아니오 | low | 2026-09-30 | 기타 | — |
| f22 | [추정] | 확인한 자료를 종합하면 67. 기타 현장에서 ROP 가 직접 맡을 범위는 다음과 같다. 점검 일정·배달 주문·운반 요청을 받아 로봇에 배정하고 작업 순서를 정하며(f1·f7·f15), 승강기·자동문 연동을 요청·확인하고(f7·f12), 점검 영상·계기값·BIM 대조 결과 같은 작업 결과를 모아 요청한 시스템에 돌려주고(f3·f6), 위험 구역·자율 운용 구역을 운행 제약으로 반영한다(f5·f18). 확인한 국내 사례(네이버 ARC, 농촌진흥청 통합 관리 프로그램)는 한 기관이 만든 로봇을 자체 계층으로 묶은 것이고, 제조사가 다른 로봇을 한 계층에서 묶은 공개 사례는 창이 공항의 Open-RMF(f11)와 벤더 주장(f4) 수준에서만 확인됐다. | ref-995, ref-997, ref-1007, ref-1004, ref-1008, ref-1000, ref-999, ref-1009, ref-1003 | 아니오 | low | 2026-09-30 | 기타 | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 다음은 외부에 맡길 영역으로 보인다. 로봇의 SLAM·가스·음향 감지·계단 보행·파지는 로봇 자체 지능·제어에 속한다(f1·f5·f13). 승강기·자동문·5G 특화망·실험 분석 장비(SiLA 서버)는 시설·설비 제어에 속한다(f7·f12·f14). 설비 보전·공정 관리 시스템과 BIM 저작 도구는 상위 업무 시스템에 속한다(f6). 농업기계 안전(ISO 18497)·위험 시설 요건은 업종별 조건에 속한다(f18). 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·상태 확인만 걸고 주행·계측 성능과 설비 제어는 해당 제조사·설비 주체에 맡겨야 할 것으로 보인다. | ref-995, ref-999, ref-996, ref-997, ref-1004, ref-1001, ref-1000, ref-1009 | 아니오 | low | 2026-09-30 | 기타 | — |
| f24 | [추정] | 이 영역은 다음 영역들과 이어진다. 승강기·자동문 연동은 22. 설비·건물 시스템 연동(f7·f12)과 연결된다. 이기종 로봇 관제는 20. 로봇·제조사 관제 연동(f4·f11), 표준은 21. 상호운용 표준·적합성(f12·f14·f18)과 연결된다. BIM 대조는 14. 도면·BIM에서 지도 만들기·16. 장소 의미·지도 관리(f6), 자산·자재 추적은 17. 작업 대상·자산 식별과 인계 추적(f5·f9), 점검 이상 감지는 38. 모니터링·이상 탐지·원인 분석(f1·f3)과 연결되며, 계기 판독·열화상 분석은 45. 문서·도면·장면 이해(f3)와도 이어진다. 작업 순서 설정은 26. 작업 순서·스케줄링(f15), 수확·이송 분업은 25. 작업 배정 — MRTA(f17), 작업자 추종은 31. 사람–로봇 협업(f16), 5G·클라우드 두뇌는 42. 분산 시스템·통신·컴퓨팅 구조(f3·f7), 실험 계획 루프는 46. 예측·학습 기반 최적화(f13), 농업기계 안전은 50. 안전 표준·인증·사고 조사(f18)와 연결된다. 공항 안내는 64. 상업 시설(f10), 실외 농지·건설은 66. 실외(f16·f5), 벤더 동향은 1. 기술·시장·업체 동향(f4)과 이어진다. | ref-997, ref-1004, ref-1003, ref-1001, ref-1009, ref-1000, ref-999, ref-1002, ref-995, ref-1008, ref-1007, ref-1005, ref-1006, ref-996, ref-998 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and subsea drones | 2025-11-21 | 기사 | medium | 2026-09-30 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 아니오 |
| ref-996 | Burger, B., Maffettone, P. M., Gusev, V. V. 외 (Nature 583) | A mobile robotic chemist | 2020-07 | 논문 | medium | 2026-09-30 | https://www.nature.com/articles/s41586-020-2442-2 | 예 |
| ref-997 | 이코노미스트 (송재민) | 로봇이 로봇들을 움직이는, 네이버 1784 | 2023-01-11 | 기사 | medium | 2026-09-30 | https://economist.co.kr/article/view/ecn202301110006 | 아니오 |
| ref-998 | 로봇신문 (정원영) | 인천국제공항, 안내 로봇 '에어스타' 본격 운영 | 2018-07-11 | 기사 | medium | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=14422 | 아니오 |
| ref-999 | 서울신문 | 로봇 '스팟' 건설현장 누빈다…현대건설 품질·안전 관리 | 2022-11-15 | 기사 | medium | 2026-09-30 | https://www.seoul.co.kr/news/economy/2022/11/15/20221115500118 | 아니오 |
| ref-1000 | 인더스트리뉴스 | GS건설, 4족보행 로봇 '스팟(SPOT)' 국내 최초 건설현장 도입 | 미확인 | 기사 | medium | 2026-09-30 | https://www.industrynews.co.kr/news/articleView.html?idxno=38911 | 아니오 |
| ref-1001 | SiLA Consortium | SiLA Standards | 미확인 | 표준 | high | 2026-09-30 | https://sila-standard.com/standards/ | 아니오 |
| ref-1002 | 아주경제 (윤선훈) | 아시아 최대 규모 데이터센터…네이버 '각 세종' | 2023-11-08 | 기사 | medium | 2026-09-30 | https://www.ajunews.com/view/20231107091520837 | 아니오 |
| ref-1003 | Korial (구 Energy Robotics) — Andre Retterath, Earlybird Venture Capital 기고 | Game-changer: The rationale behind the investment in Energy Robotics | 2021-01-15 | 벤더 문서 | low | 2026-09-30 | https://www.energy-robotics.com/post/revolutionizing-industrial-inspection-the-rationale-behind-the-investment-in-energy-robotics | 아니오 |
| ref-1004 | The Robot Report | Singapore's National Robotics Programme reveals initiatives to advance robot adoption | 2025-10-29 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/singapores-national-robotics-programme-reveals-initiatives-advance-robot-adoption/ | 아니오 |
| ref-1005 | 헬로디디 | 스스로 수확하고 운반···'로봇농부' 나왔다 | 미확인 | 기사 | medium | 2026-09-30 | https://www.hellodd.com/news/articleView.html?idxno=99827 | 아니오 |
| ref-1006 | 농민신문 (조영창) | 농민 뒤 졸졸 '운반로봇'…무거운 수확물 옮기고 | 2024-03-25 | 기사 | medium | 2026-09-30 | https://www.nongmin.com/article/20240322500556 | 아니오 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합 관리 기술 개발 | 2025-04-23 | 기사 | medium | 2026-09-30 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 아니오 |
| ref-1008 | 넷매니아즈 (손장우) | 한전의 5G 특화망 기반 응용: IoT 예방진단, 로봇기반 순시점검 및 안전관리 | 2023-09-30 | 업계 보고서 | medium | 2026-09-30 | https://www.netmanias.com/ko/post/blog/15878/5g-5g-private-5g-5g/applications-based-on-kepco-s-private-5g-network-iot-preventive-diagnosis-robot-based-inspection-and-safety-management | 아니오 |
| ref-1009 | ISO | ISO 18497-3:2024 Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 3: Autonomous operating zones | 2024 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/82687.html | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/site-type-applications/other-sites.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1(정상 무인 시설 점검), f3(노후 변전소 점검), f20(현장별 차이) / 섹션 4: SiLA 2(f14), 브레인리스 로봇(f7), 정상 무인 시설(f1), 자율 운용 구역(f18), 자율 실험실(f13) / 섹션 5(현장 유형 모두 기타): 점검·순찰 — f1·f2(Equinor, f2 는 운영사 추산), f3(한전 변전소); 건설 — f5(현대건설), f6(GS건설 BIM 통합); 농업 — f15(농촌진흥청 통합 관리), f16(작업자 추종 운반), f17(한국기계연구원, 연구기관 발표 수치); 공공시설 — f10(인천공항 에어스타), f11(창이 공항 Open-RMF); 오피스 — f7·f8(네이버 1784, f8 벤더 주장); 데이터센터 — f9(각 세종); 연구실 — f13; 작업 형태 f19, 여섯 항목 f21(완료·인계 확인 기준 근거 부족 명시) / 섹션 6: 점검 데이터 수집·AI 분석 f1·f3, BIM 대조 f6, 작업자 추종·유도선 f16, 클라우드 두뇌·5G f7, 통합 관리 프로그램 f15, 이기종 플랫폼 f4(벤더 주장) / 섹션 7: ISO 18497 f18(원문 미열람), SiLA 2 f14, SS 713·TR 130 f12, Open-RMF f11 / 섹션 8: f13(Nature 2020) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 1, 14, 16, 17, 20, 21, 22, 25, 26, 31, 38, 42, 45, 46, 50, 64, 66 / 섹션 11: open_questions_new 5건. f4·f8 은 벤더 주장 병기 필수. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f7·f12 반영, 21. 상호운용 표준·적합성 페이지에 f12·f14 반영, 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| SiLA 2 | Standardization in Lab Automation 2 (SiLA 2) | SiLA 컨소시엄이 관리하는 실험실 장비 통신 표준으로, 장비를 서버로 보고 그 능력을 Command·Property 를 담은 Feature 로 기술하며 자동 탐색과 gRPC 통신을 규정한다. |
| 브레인리스 로봇 | Brainless Robot | 인식·판단 같은 연산을 로봇 본체가 아닌 클라우드에 두고 저지연 네트워크(5G 등)로 제어받는 로봇으로, 네이버 1784 의 배달 로봇 루키가 예다. |
| 정상 무인 시설 | Not Normally Manned (NNM) Facility | 평소 사람이 상주하지 않도록 설계한 플랜트·해상 설비로, 원격 감시와 점검 로봇으로 불필요한 현장 출동을 줄이는 운영 방식을 전제로 한다. |
| 자율 실험실 | Self-driving Laboratory (Autonomous Laboratory) | 로봇이 실험을 수행하고 알고리즘이 결과를 보고 다음 실험을 고르는 과정을 사람 개입 없이 반복하는 실험실로, 이동 로봇이 일반 실험실 장비를 다루는 형태도 포함한다. |

## 열린 질문

새로 생긴 질문:

- 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? | 관련 영역: 67. 기타 현장, 22. 설비·건물 시스템 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반
- 농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? | 관련 영역: 67. 기타 현장, 20. 로봇·제조사 관제 연동 | 근거: f15 | 종류: 일반
- 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? | 관련 영역: 67. 기타 현장, 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리 | 근거: f6 | 종류: 일반
- 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? | 관련 영역: 67. 기타 현장, 23. 업무 시스템 연동, 38. 모니터링·이상 탐지·원인 분석 | 근거: f3 | 종류: 일반
- SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? | 관련 영역: 67. 기타 현장, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f2 Equinor 비용 절감 추산은 운영사 추산이며 산정 근거 미확인
    - f3 한전 변전소 실증은 넷매니아즈 정리본 기준, 한전 원자료 미열람
    - f4 Korial(구 Energy Robotics)의 20개 이상 플랫폼 제어는 벤더 주장이며 독립 확인 없음
    - f6 인더스트리뉴스 기사 발행일 미확인
    - f8 네이버 배달 시간 단축은 벤더 주장이며 측정 조건 미확인
    - f11 창이 공항 Open-RMF 운영 규모(로봇 대수·제조사 수)는 미확인 — 창이 공항 매거진 페이지는 본문이 렌더링되지 않아 열지 못함
    - f12 SS 713·TR 130 표준 원문 미열람
    - f13 Nature 논문은 저장소 PDF 본문 추출 실패로 검색 결과 요약 범위만 사용(원문 미열람)
    - f15 농촌진흥청 보도자료 원문(korea.kr·rda.go.kr)은 연결 재설정으로 열지 못해 뉴스토마토 기사 기준
    - f17 한국기계연구원 성능 수치의 시험 조건과 기사 발행일 미확인
    - f18 ISO 18497-3 원문 미열람(ISO 페이지 403)
    - Ju 외(2022) 농업 다중 로봇 리뷰는 ScienceDirect·ADS 접근 실패로 넣지 않음
    - 완료·인계 확인 기준(점검 결과 승인 주체 등)은 어느 사례에서도 확인되지 않음
- 범위 경계 위반 의심:
    - f1·f5·f13: SLAM·가스 감지·계단 보행·장비 조작은 분류 원문 19장의 로봇 자체 지능·제어이므로 사례 설명으로만 쓰고 f23 에서 '연계 대상: '으로 구분함
    - f7·f12·f14: 승강기·자동문·5G 망·실험 장비는 시설·설비 제어이므로 ROP 는 요청·예약·상태 확인만 맡는 것으로 제안함
    - f18: 농업기계 안전 표준은 업종별 조건이므로 운행 제약 근거로만 제안함
    - f3·f1: 계기 판독·열화상 AI 분석을 로봇·플랫폼 어느 쪽이 맡는지는 사례마다 달라 직접 범위로 단정하지 않음
- 한계: 재실행 1회차. 반려 사유(스키마 불일치: f1·f6·f8·f15·f18 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음)에 대응함. 직전 반환값(runs/2026-09-30-02/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었다. 그래서 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었고, finding·출처 번호가 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-1003)만 근거로 한 finding 은 f4 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 회사 성능 주장 f8 도 같은 방식으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f4, f8). web_fetch_available: true · fetch_mode full. 사용량은 검색 16회/30, 신규 출처 15건/15(ref-995~ref-1009, 예약 구간 안)로, 출처 상한에 도달했다. 그래서 정책브리핑 농업로봇 기사(2025-03-10, 열었으나 통합 관리 프로그램 서술 없음), 한전KPS 정비 보조 로봇, LS일렉트릭 변압기 공장 순찰(제조 공장 사례), 역·지하철 사례, 해외 건설·농업 상용 사례는 넣지 못했다. 원문 열람은 13건이 webfetch 로 열렸고(ref-1003 은 korial.com 으로 리디렉션), 2건은 미열람(ref-996 PDF 추출 실패, ref-1009 ISO 403)이다. 교차 확인 0건, 신뢰도 high finding 없음. 분류 원문 핵심 질문(점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가)에는 작업 형태 f19, 현장별 차이 f20, 여섯 항목 f21, 직접 범위 f22, 연계 대상 f23 으로 답했다. 결론은 추정이다. 기타 현장은 점검 현장처럼 정보가 작업 대상이거나, 건설처럼 공간이 매일 바뀌거나, 농업처럼 비정형 지면·계절성이 있거나, 오피스·데이터센터처럼 건물 인프라에 기대는 점에서 다르다. 국내 사례는 대부분 한 기관이 자체 로봇을 자체 계층으로 묶은 형태다. 현장 유형은 f4·f14·f24 를 빼고 모두 기타다. 국내 자료는 이코노미스트·로봇신문·서울신문·인더스트리뉴스·아주경제·헬로디디·농민신문·뉴스토마토·넷매니아즈 아홉 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련(계기 판독·열화상 분석, 베이지안 실험 계획)은 45. 문서·도면·장면 이해·46. 예측·학습 기반 최적화와 적용 대상 38. 모니터링·이상 탐지·원인 분석에 함께 연결했다. 입력 누락은 없고 정정 요청·우선 지정 질문도 없다. 이 영역에 걸린 기존 열린 질문은 없으며 해결된 열린 질문도 없다.
```

### runs/2026-09-25-40/research.md

```markdown
# 리서치 브리프 2026-09-25-40

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-40 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 16. 공용 자원·충전·에너지 최적화 |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 floorplan-recognition 단계 1 반영 제안(충전소 위치 정보 출처: ref-079·ref-216·ref-219) 검토 대상
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 트랙 반영 제안 2건(VDA 5050 startCharging·stopCharging과 구역 유형, Nav2 도킹 / VDA 5050 팩트시트 batteryCharging) 검토 대상
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음 — 트랙 반영 제안(Stark 외 2024 충전소 배치 → 3. 처리능력·거점·설비 계획) 검토 대상
- 섹션 11. 열린 질문 비어 있음(기존 oq-016 이 이 영역에 걸림)

## 조사 질문

1. 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
2. VDA 5050·Open-RMF 같은 표준·오픈소스는 충전 명령, 배터리 상태, 충전 임계값, 충전기 위치를 어떤 필드와 동작으로 표현하는가? (섹션 4·7 겨냥, 트랙 반영 제안 2건 검증)
3. 충전기·승강기·통로 구간 같은 공용 자원을 한 번에 한 로봇에 배분하거나 예약하는 오픈소스 장치(뮤텍스 그룹, 승강기 세션, 예약 시스템)는 무엇인가? (섹션 6·7 겨냥)
4. 충전 시점·충전기 선택·충전 방식(플러그인·교환·유도)과 충전기 대수를 정하는 대표 연구는 무엇이고 어떤 결과를 보고하는가? (섹션 6·8 겨냥, 트랙 반영 제안 ref-109 검토)
5. 다층 시설에서 승강기가 로봇 배송의 병목이 되는 근거와 승강기 선택·층간 이동을 다룬 연구(국내 포함)는 무엇인가? (섹션 3·5·8 겨냥)
6. 충전 대기·배터리 제약을 작업 배정과 함께 푸는 연구와 학습 기반 충전 결정은 13. 작업 배정 — MRTA·27. AI·학습·적응과 모델 운영과 어떻게 연결되는가? (섹션 6·10 겨냥)
7. ROP가 직접 맡을 충전·공용 자원 계획과 로봇 자체 제어(과충전 보호·정밀 도킹)·설비 안전 제어 사이 경계는 어디인가? — oq-016(충전·대기 시간의 OEE 손실 분류)과 연결 (섹션 9·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0(main)은 충전을 즉시 동작 또는 노드 동작인 startCharging·stopCharging 으로 표현하며, 충전은 정지한 충전 지점이나 주행 중 충전 차선에서 할 수 있고 과충전 보호는 이동로봇의 책임이다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 관제(fleet control)의 기능으로 에너지 관리를 들며, 충전 주문이 운반 주문을 중단시킬 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 최신 팩트시트 스키마의 batteryCharging 은 criticalLowChargingLevel(이 수준 이하에서는 관제가 충전소로 가는 주문만 보내야 함), minimumDesiredChargingLevel, maximumDesiredChargingLevel, minimumChargingTime 네 항목을 로봇 선언으로 둔다. | ref-228 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | VDA 5050 최신 상태 스키마의 powerSupply 는 충전 상태(stateOfCharge, %), 충전 중 여부(charging), 배터리 전압·전류, 건강 상태(batteryHealth), 현재 충전량으로 갈 수 있는 거리(range, m)를 담으며, 좋음·나쁨만 아는 로봇은 80%·20%로 보고한다. | ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 명세는 충전소를 별도 구역 유형으로 두지 않고 충전을 주문의 노드 동작과 즉시 동작으로 다룬다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 템플릿 설정은 로봇이 운행하지 않는 배터리 하한(recharge_threshold), 충전 목표(recharge_soc), 배터리 전압·용량·충전 전류, 주변·도구 장치 소비 전력, 배터리 소모 반영 여부, 작업 종료 후 동작(park·charge·nothing), 로봇별 전용 충전기를 둔다. | ref-105 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f7 | [사실] | Open-RMF 에서 충전 작업은 플릿 어댑터가 스스로 만드는 작업이며, 로봇이 일련의 작업을 마칠 충전량이 부족하면 작업 계획기가 충전(ChargeBattery) 작업을 일정에 끼워 넣고, 현재는 로봇마다 전용 충전 위치가 있다고 가정한다. | ref-039, ref-104 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [사실] | Open-RMF 작업 계획기(rmf_task TaskPlanner)는 충전소로 돌아갈 초기 충전량조차 없거나 요청을 감당할 배터리 용량이 없는 경우를 오류로 구분하고, 낮은 충전 상태를 이차항으로 강하게 벌점하는 배터리 우선 비용 설정을 둔다. | ref-377 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | Open-RMF 에서 충전기 위치는 Traffic Editor 경유점의 is_charger 수동 주석으로 들어가 배터리가 임계값 아래로 떨어진 로봇이 그곳으로 보내지며, 로봇별 충전 경유점을 지정하지 않으면 그래프에서 가장 가까운 충전 경유점을 쓰고, 주차 예약 시스템 사용은 기본값 꺼짐이지만 켜기를 권장한다. | ref-079, ref-864, ref-865 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 교통 그래프는 경유점·차선을 뮤텍스 그룹(mutex group)에 넣을 수 있고, 같은 뮤텍스 그룹에 속한 경유점이나 차선은 한 번에 한 로봇만 점유할 수 있다. | ref-864 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f11 | [사실] | Open-RMF 승강기 요청은 요청자별 고유 세션 id 로 승강기를 점유하며, 승강기 상태는 세션 종료 요청(REQUEST_END_SESSION)을 보낼 때까지 제어권을 받은 세션 id 를 기록하고, AGV 모드에서는 승강기가 멈추면 문이 계속 열려 있다. | ref-312, ref-286 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f12 | [사실] | Open-RMF 의 실험적 예약 라이브러리 rmf_reservation 은 로봇이 충전기 같은 자원을 주어진 시간 범위 안에서 정해진 시간 동안 쓰겠다고 요청하면 해법기가 로봇을 자원에 배정하는 제약 자원 스케줄링을 제공한다고 소개된다. | ref-866 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [사실] | 연계 대상: Nav2 도킹 프레임워크는 환경 안 도크 인스턴스(유형과 [x, y, θ] 위치)의 데이터베이스를 두고 충전 도크와 비충전 도크(컨베이어·팔레트 등)를 플러그인으로 구분하며, 센서로 도크 자세를 보정하고 도킹 뒤 충전 시작 여부(isCharging)를 확인한다. | ref-216 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f14 | [추정] | MiR 충전 스테이션 매뉴얼 게재본은 지도에 충전 스테이션 마커를 두고 로봇이 이를 감지해 도킹한다고 설명한다. | ref-219 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f15 | [사실] | Zou·Gong·de Koster·Xu(2018)는 로봇 이동형 풀필먼트 시스템(RMFS)에서 플러그인 충전·배터리 교환·유도 충전 전략을 반개방형 대기행렬 네트워크와 시뮬레이션으로 비교해, 유도 충전이 회수 처리 시간에서 가장 좋고 배터리 비용이 낮으면 배터리 교환이 플러그인 충전보다 싸다고 보고했다. | ref-098 | 아니오 | medium | 2018 | 피킹 / 예외·성과 | 원문 미열람 |
| f16 | [사실] | Chen·Gong·Chen·Wang(2024)은 자가 등반 로봇(SCR) 창고의 배터리 관리를 반개방형 대기행렬 네트워크로 모델링해, 배터리 열화를 반영하면 느린 충전이 빠른 충전보다 나은 조건이 있고, 우선 충전 정책이 전용 충전 정책보다 비용 효율적이며, 충전기 대수 결정 도구를 제시했다. | ref-861 | 아니오 | medium | 2024-01 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | 다중 AGV 충전 순서 최적화 연구(Computers & Industrial Engineering, 2024)는 도착 시 충전소가 사용 중일 확률과 충전 전 대기 확률을 충전소마다 확률 변수로 두고 총 주행 시간 기댓값을 최소화하는 혼합 정수 선형 계획을 세웠으며, 허용 최대치까지 완전 충전하는 것이 최적임을 보였다. | ref-858 | 아니오 | medium | 2024-08 | 제약 | 원문 미열람 |
| f18 | [사실] | Dang·Singh·Adan·Martagan·van de Sande(2021)는 다중 적재·다능력 AGV 에 운반 요청과 충전 요청을 함께 배정·순서화하고 임계 배터리 수준을 지키는 부분 충전 시간을 정하는 혼합 정수 선형 계획과 적응형 대규모 이웃 탐색을 제시해, 현행 방식 대비 비용을 약 20~50% 줄였다고 보고했다. | ref-862 | 아니오 | medium | 2021-12 | 수행 자원 | 원문 미열람 |
| f19 | [사실] | 근접 정책 최적화(PPO) 기반 심층 강화학습 연구(arXiv 2607.05683)는 고정 충전소가 있는 다중 블록 창고에서 주문이 확률적으로 도착할 때 충전소 선택과 충전 시간을 충전소 대기 예상 시간을 반영해 학습하며, 고정 규칙 휴리스틱은 동적 환경과 다중 로봇 조율에서 비효율적이라고 지적한다. | ref-859 | 아니오 | medium | 2026-07 | 피킹 / 예외·성과 | 원문 미열람 |
| f20 | [사실] | Ma·Zhou·Stephen(2020)은 자동화 컨테이너 터미널의 배터리 AGV 시스템을 시뮬레이션해 분산형 충전소 배치와 점진적 재충전 정책이 좋은 성능을 낸다고 보고했다. | ref-860 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f21 | [사실] | Stark 외(2024)는 창고 안 충전소의 최적 배치를 PageRank 와 비슷한 방법으로 다룬 연구를 발표했다. | ref-109 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f22 | [사실] | Omega 게재 논문(2024)은 로봇 이동형 풀필먼트 시스템의 성능 평가에 로봇 에너지 소비를 넣고 동적 우선순위를 쓰는 운영 정책을 다룬다. | ref-146 | 아니오 | low | 2024 | — | 원문 미열람 |
| f23 | [사실] | 고밀도 병원 환경의 약품 배송 로봇 연구는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다고 보고했다. | ref-060 | 아니오 | medium | 2026 | 제약 | 원문 미열람 |
| f24 | [사실] | 다층 호텔 배송 경로 계획 연구는 승강기를 층간 이동의 대기·운행 시간으로 모델링했고, 고객 노드 60개 시나리오에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 거의 두 배가 된다고 보고했다. | ref-103 | 아니오 | medium | 2025 | 예외·성과 | 원문 미열람 |
| f25 | [사실] | Electronics(2025) 게재 논문은 실내 배송 로봇의 그래프 기반 다층 경로 계획에서 승강기 선택을 최적화하는 방법을 제시한다. | ref-321 | 아니오 | low | 2025 | — | 원문 미열람 |
| f26 | [사실] | 박재범·조성준·김준식·유범재(2024)는 서버를 통해 엘리베이터를 신속하게 제어하는 모듈과 작업 구조로 층간 이동을 처리하고, 노드 그래프 기반으로 한 번의 주행에서 여러 목적지를 고려하는 다층 경로 계획 알고리즘을 제안해 실증 시험과 주행 시간 비교로 검증했다. | ref-863 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f27 | [추정] | 분류 원문 질문(로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까)에 대해, 로봇마다 같은 충전 임계값(criticalLowChargingLevel, recharge_threshold)으로만 충전을 시작하면 충전 수요가 겹칠 수 있으므로, 충전소 대기를 반영한 충전 시점·충전기 선택, 공유 충전기의 우선 충전 정책, 충전기·승강기 점유의 예약·세션 관리를 조율 계층이 함께 맡아야 할 것으로 보인다. | ref-228, ref-105, ref-858, ref-859, ref-861, ref-312 | 아니오 | low | 2026-09-25 | 제약 | — |
| f28 | [추정] | 피킹 성수기에는 여러 로봇이 비슷한 시각에 충전 하한에 닿아 충전기 대기열이 생기고 가용 로봇 수가 줄 수 있으므로, 주문이 적은 시간대에 기회 충전을 넣거나 충전 요청을 작업 배정과 함께 계획하는 방식이 처리량 손실을 줄이는 수단이 될 것으로 보인다. | ref-862, ref-859, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f29 | [추정] | 다층 시설의 출하 단계에서는 승강기가 세션 단위로 한 요청자에게 점유되므로, 여러 제조사 로봇의 승강기 호출을 조율 계층이 세션 순서·목적층 묶음으로 배분하지 않으면 층간 대기가 출하 마감을 위협할 수 있을 것으로 보인다. | ref-312, ref-286, ref-103 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f30 | [추정] | ROP 가 직접 맡을 범위는 여러 제조사 로봇에 걸친 충전기·승강기·통로 구간·대기 위치의 예약과 배분, 충전 시점과 충전 목표 결정, 배터리 상태를 반영한 작업 배정 입력이며, 이는 VDA 5050 이 관제의 에너지 관리로 두고 Open-RMF 가 충전 작업 삽입·뮤텍스 그룹·승강기 세션으로 다루는 층위에 해당하는 것으로 보인다. | ref-031, ref-104, ref-864, ref-312 | 아니오 | low | 2026-09-25 | — | — |
| f31 | [추정] | 연계 대상: 과충전 보호, 충전기와의 통신·정밀 도킹, 배터리 관리 장치, 승강기 운행·설비 안전 제어는 로봇·충전 설비·승강기 쪽이 맡고, ROP 는 충전 시작·중지 요청, 상태 확인, 승강기 세션 요청과 모드 확인을 담당하는 것으로 보인다. | ref-031, ref-216, ref-284 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f32 | [추정] | 충전소 정보는 시설 안 설비 위치(도크 인스턴스 자세)와 로봇이 경로 그래프에서 접근하는 지점(is_charger 경유점)으로 나뉘어 관리되므로, ROP 의 공용 자원 모델도 충전기 설비와 접근 경유점을 분리해 두어야 할 것으로 보인다. | ref-216, ref-079, ref-865 | 아니오 | low | 2026-09-25 | — | — |
| f33 | [추정] | 이 영역은 충전 요청을 작업 배정과 함께 푸는 연구로 13. 작업 배정 — MRTA 와, 뮤텍스 그룹·대기 지점으로 15. 다중 로봇 경로·교통 관리 — MAPF 와, 승강기 세션으로 10. 설비·건물 시스템 연동과, 충전기 대수·배치로 3. 처리능력·거점·설비 계획과, 팩트시트 충전 설정으로 5. 로봇 능력·작업 온톨로지와, 현재 배터리 상태로 8. 실시간 세계 상태·데이터 일관성과, 충전 정책 시뮬레이션으로 22. 시뮬레이션·예측용 디지털 트윈과, 학습 기반 충전 결정으로 27. AI·학습·적응과 모델 운영과 이어지는 것으로 보인다. | ref-862, ref-864, ref-312, ref-861, ref-109, ref-228, ref-051, ref-860, ref-859 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_types.html | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 아니오 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md | 아니오 |
| ref-219 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.17003 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.1177/20552076261437181 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics14050982 | 예 |
| ref-858 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach | 2024-08 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0360835224006314 | 예 |
| ref-859 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.05683 | 예 |
| ref-860 | Ma, N., Zhou, C., & Stephen, A. | Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals | 2020 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X | 예 |
| ref-861 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 예 |
| ref-862 | Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D. | Scheduling heterogeneous multi-load AGVs with battery constraints | 2021-12 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0305054821002586 | 예 |
| ref-863 | 박재범, 조성준, 김준식, 유범재 | 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템 | 2024 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904 | 예 |
| ref-864 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-865 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 아니오 |
| ref-866 | Open Robotics (open-rmf) | rmf_reservation — Experimental reservation library in rust (GitHub) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_reservation | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절: f27(SCM 질문 — 같은 임계값에 따른 충전 수요 겹침), f23·f24(승강기 병목 근거), f15·f16(충전 정책이 처리량·비용에 미치는 영향) / 4절: f3·f4(충전 상태·임계 저충전 수준), f6(recharge_threshold·recharge_soc), f10(뮤텍스 그룹), f11(승강기 세션), f15(플러그인·교환·유도 충전) / 5절: f28(피킹, 예외·성과), f29(출하, 제약), f7(시작 조건) / 6절: f7·f8·f9·f10·f11·f12, f17·f18·f19·f20, f32 — 트랙 floorplan-recognition 반영 제안(충전소 위치 정보 출처) 검토 결과: f9(ref-079 is_charger, 원문 확인)·f13(Nav2 도크 데이터베이스, 연계 대상)·f14(MiR, 벤더 주장 유지)·f32(시설 위치와 접근 지점 분리 [추정]) 반영 / 7절: f1·f2·f3·f4·f5(VDA 5050 — 트랙 반영 제안 2건을 원문으로 재확인, 필드 이름은 스키마 기준 minimumDesiredChargingLevel·maximumDesiredChargingLevel), f6~f12(Open-RMF), f13(Nav2 도킹) / 8절: f15~f26(국내 f26) / 9절: f30(직접 범위), f31(연계 대상) / 10절: f33 — 트랙 반영 제안(Stark 외 2024 → 3. 처리능력·거점·설비 계획) 반영(f21), f19 는 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 11절: 기존 oq-016 과 새 열린 질문 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 충전 상태 | State of Charge (SOC) | 배터리에 남은 충전량을 전체 용량 대비 비율(%)로 나타낸 값으로, VDA 5050 상태 메시지의 stateOfCharge 와 Open-RMF 배터리 갱신이 이 값을 쓴다. |
| 뮤텍스 그룹 | Mutex Group (Open-RMF) | Open-RMF 교통 그래프에서 같은 그룹에 묶인 경유점·차선을 한 번에 한 로봇만 점유하도록 하는 상호 배제 단위이다. |
| 승강기 세션 | Lift Session (Open-RMF) | Open-RMF 에서 한 요청자가 세션 id 로 승강기 제어권을 받아 세션 종료 요청을 보낼 때까지 점유하는 단위이다. |
| 배터리 교환 | Battery Swapping | 방전된 로봇 배터리를 충전기에 꽂아 기다리는 대신 충전된 배터리로 바꿔 끼워 로봇을 곧바로 다시 운행하게 하는 충전 방식이다. |

## 열린 질문

새로 생긴 질문:

- 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f1 | 종류: 일반
- 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 4. 성과·경제성·프로세스 개선 | 근거: f17 | 종류: 일반
- 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 10. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반
- 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 온톨로지 | 근거: f3 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 28 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 9건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 표준·오픈소스 내용은 단일 발행 주체, 연구 결과는 각 논문 단일 출처
    - f12 rmf_reservation README 원문 열지 못함(main·master 404), 배포판 사용 여부 미확인
    - f10 뮤텍스 그룹 동시 진입 버그 보고(open-rmf 이슈)가 있어 실제 동작 신뢰성 미확인
    - f15~f26 근거 논문 원문 미열람(검색 요약·제목 범위)
    - f17 ref-858 저자 미확인
    - f18·f19 성능 수치는 저자 보고
    - f22·f25 는 제목 수준만 확인
    - f14 MiR 충전 마커는 벤더 주장이며 이번에 다시 열지 않음
    - 국내 물류센터 충전·승강기 병목 정량 자료 미확인(oq-010 관련)
    - 시간대별 전기 요금 기반 로봇 충전 계획의 학술 출처 미확보
- 범위 경계 위반 의심:
    - f13·f31: 정밀 도킹·과충전 보호·승강기 안전 제어는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 대상이라 claim 을 '연계 대상: '으로 표시하고 ROP 역할을 요청·상태 확인으로 한정함
    - f20·f23·f24·f26: 컨테이너 터미널·병원·호텔·배송 로봇 사례라 물류센터 직접 적용 근거로는 제한적임
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-031·ref-228·ref-051·ref-105·ref-079·ref-039·ref-104·ref-377·ref-312·ref-286·ref-284·ref-216, 신규 ref-864·ref-865. rmf_reservation README 는 404, task_new.md 에는 충전 내용 없음. 그 밖의 신규 7건(ref-858~ref-863, ref-866)과 재사용 ref-219·ref-098·ref-109·ref-146·ref-060·ref-103·ref-321 은 원문 미열람(신뢰도 상한 medium). finding 신뢰도 모두 medium 이하, 교차 확인 0건. 검색 19회/30, 신규 출처 9건/15(ref-858~ref-866, 예약 구간 안), 재사용 19건. 세부영역 반영 제안 4건(트랙 floorplan-recognition 2026-09-25-19 3건, manual-capability-ontology 2026-09-25-23 1건)을 모두 검토해 f1·f3·f5·f9·f13·f14·f21·f32 로 6·7·10절 반영을 제안했다(batteryCharging 필드 이름은 스키마 원문 기준으로 정정). 한국 자료: 박재범 외 2024(ref-863). 한국 물류센터 충전 연구는 검색 2회에서 찾지 못함. 교차 규칙: 학습 기반 충전 결정(f19)은 27. AI·학습·적응과 모델 운영과 이 영역 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성(현재 배터리 상태)과 22. 시뮬레이션·예측용 디지털 트윈(충전 정책 실험)은 섞지 않았다. 정정 요청 없음. oq-016(충전·대기 시간의 OEE 손실 분류)은 관련 근거를 찾지 못해 해결 제안하지 않았다.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope

action type | counter action | description | idempotent | parameters | linked state | instant | node | edge | zone
---|---|---|---|---|---|---|---|---|---
startPause | stopPause | Activates the pause mode. <br>A linked state is required, because many mobile robots can be paused by using a hardware switch. <br>No more automatic driving - reaching next node is not necessary. Actions that can be paused (`pauseAllowed`=`true`), shall be paused, other actions continue. Order execution is resumed after stopPause. | yes | - | paused | yes | no | no | no
stopPause | startPause | Deactivates the pause mode. <br>Movement and all other actions will be resumed (if any). <br>A linked state is required because many mobile robots can be paused by using a hardware switch. <br>stopPause can also restart mobile robots that were stopped with a hardware button that triggered startPause (if configured). | yes | - | paused | yes | no | no | no
startHibernation | stopHibernation | Initiates hibernate mode, in which the mobile robot shall remain connected to the MQTT broker but no longer needs to send state messages. The mobile robot shall report this action as 'FINISHED' before discontinuing publishing state messages and publish a connection state of 'HIBERNATING'. If the mobile robot has an active order, it shall clear it. Reaching the next node is not required.<br>While in 'HIBERNATING' connection state, mobile robot shall not be moving. The mobile robot shall only receive and respond to the instant action 'stopHibernation' and shall not respond to any other commands, such as orders or additional instant actions. <br>If the mobile robot's battery becomes critically low while in this mode, the mobile robot may stop 'HIBERNATING' autonomously to report an error. In case a wake‑up time is set, the mobile robot is able to autonomously exit the 'HIBERNATING' connection state at the specified time and will publish the corresponding connection state transition before resuming normal operation. | yes | wakeUpTime (string, optional) | - | yes | no | no
stopHibernation | startHibernation | Ends hibernate mode. To initiate wake‑up while the mobile robot is in the 'HIBERNATING' state, a control device (onboard or external) shall subscribe to the `instantAction` topic and remain connected to the MQTT broker. Because the mobile robots standard control device may be partially shut down during hibernation, the wake‑up may be triggered by a distinct MQTT client (separate from the mobile robots usual communication client).<br>Upon success, the mobile robot shall publish the connection state ONLINE.| yes | - | - | yes | no | no
shutdown | - | Initiates a coordinated shutdown of the mobile robot, where it disconnects from the MQTT broker. The execution of the shutdown action requires the mobile robot to be in an idle state. There is no way using the VDA 5050 protocol to automatically restart due to the connection being terminated.<br>If a mobile robot is in hibernate mode but should be shut down, it shall first exit hibernation (via stopHibernation) before executing shutdown.| yes | - | - | yes | no | no | no
startCharging | stopCharging | Activates the charging process. <br>Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). <br>Protection against overcharging is the responsibility of the mobile robot. | yes | - | powerSupply.charging | yes | yes | no | no
stopCharging | startCharging | Discontinues the charging process. <br>The charging process can also be interrupted by the mobile robot or the charging station, e.g., if the battery is full. | yes | - | powerSupply.charging | yes | yes | no | no
initializePosition | - | Resets (overrides) the pose of the mobile robot with the given parameters. | yes | x (float64)<br>y (float64)<br>theta (float64)<br>mapId (string)<br>lastNodeId (string) | mobileRobotPosition.x<br>mobileRobotPosition.y<br>mobileRobotPosition.theta<br>mobileRobotPosition.mapId<br>lastNodeId<br> maps | yes | yes<br>(Elevator) | no | no
enableMap | - | Enable a previously downloaded map explicitly to be used in orders without initializing a new position. | yes | mapId (string)<br>mapVersion (string) | maps | yes | yes | no | no
downloadMap | - | Trigger the download of a new map. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the map for use and setting the map in the state. | yes | mapId (string)<br>mapVersion (string)<br>mapDownloadLink (string)<br>mapHash (string, optional) | maps | yes | no | no | no
deleteMap | - | Trigger the removal of a map from the mobile robot's memory. | yes | mapId (string)<br>mapVersion (string) | maps | yes | no | no | no
downloadZoneSet | - | Trigger the download of a zone set. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the zone set for use and setting the zone set in the state. | yes | zoneSetId (string)<br>zoneSetDownloadLink (string)<br>zoneSetHash (string, optional) | zoneSets | yes | no | no | no
enableZoneSet | - | Enable a previously downloaded zone set explicitly to be used in orders. | yes | zoneSetId (string)<br> | zoneSets | yes | yes | no | no
deleteZoneSet | - | Trigger the removal of a zone set from the mobile robot's memory. | yes | zoneSetId (string) | zoneSets | yes | no | no | no
clearInstantActions | - | Removes all finished or failed instant actions from the mobile robot state. | yes | - | instantActionStates | yes | yes | no | no
clearZoneActions | - | Removes all finished or failed zone actions from the mobile robot's state. | yes | - | zoneActionStates | yes | yes | no | no
stateRequest | - | Requests the mobile robot to send a new state message. | yes | - | - | yes | no | no | no
logReport | - | Requests the mobile robot to generate and store a log report. | yes | reason<br>(string) | - | yes | no | no | no
pick | drop<br><br>(if automated) | Request the mobile robot to pick a load. <br>Mobile robots with multiple load handling devices can process multiple pick operations in parallel. <br>In this case, the parameter lhd needs to be present (e.g., LHD1). <br>The parameter stationType informs how the pick operation is handled in detail (e.g., floor location, rack location, passive conveyor, active conveyor, etc.). <br>The load type informs about the load unit and can be used to switch field for example (e.g., EPAL, INDU, etc). <br>For preparing the load handling device (e.g., pre-lift operations based on the height parameter), the action could be announced in the horizon in advance. <br>But, pre-Lift operations, etc., are not reported as 'RUNNING' in the mobile robot state, because the associated node is not released yet.<br>If on an edge, the mobile robot can use its sensing device to detect the position for picking the node. | no |lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional) <br>loadId (string, optional)<br>height (float64, optional)<br>defines bottom of the load related to the floor<br>depth (float64, optional) for forklifts<br>side (string, optional) e.g., conveyor | .load | no | yes | yes | no
drop | pick<br><br>(if automated) | Request the mobile robot to drop a load. <br>See action pick for more details. | no | lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional)<br>loadId (string, optional)<br>height (float64, optional)<br>depth (float64, optional) <br>… | .load | no | yes | yes | no
detectObject | - | Mobile robot detects object (e.g., load, charging spot, free parking position). | yes | objectType (string, optional) | - | no | yes | yes | yes
finePositioning | - | On a node, mobile robot will position exactly on a target.<br>The mobile robot is allowed to deviate from its node position.<br>On an edge, the mobile robot will e.g., align on stationary equipment while traversing an edge. | yes | stationType (string, optional)<br>stationName (string, optional) | - | no | yes | yes | yes
waitForTrigger | - | Mobile robot shall wait for a trigger of the type defined specified in the triggerType parameter, which is an array of strings. Two predefined values shall be used when semantically appropriate: 'FLEET_CONTROL' if the trigger originates from the fleet control, and 'LOCAL' if the trigger comes from an input on the mobile robot (e.g., button press, manual loading). If none of the predefined values meet the specific requirements, custom values can be defined. <br>Fleet control is responsible for handling the timeout and shall cancel the order if necessary. | yes | triggerType [string] (array) | - | no | yes | no | yes
trigger | - | Fleet control system notifies the mobile robot that a waitForTrigger action has been released. Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed. | yes | - | - | yes | no | no | no
retry | - | Mobile robot retries action defined via actionId that is currently in state RETRIABLE. | yes | actionId (string) | - | yes | no | no | no
skipRetry | - | Mobile robot shall skip the action defined via actionId that is currently in state RETRIABLE, setting action to FAILED. | yes | actionId (string) | - | yes | no | no | no
cancelOrder | - | Mobile robot stops as soon as possible. This could be immediately or on the next node. See Chapter 6.1.3 Order cancellation. | yes | orderId (string, optional) | - | yes | no | no | no
factsheetRequest | - | Requests the mobile robot to send a factsheet | yes | - | - | yes | no | no | no
updateCertificate | - | Request the mobile robot to download and activate a new certificate set, the service parameter is an extensible enum with the predefined parameter 'MQTT' to be used for mqtt connection. | yes | service (string)<br>keyDownloadLink (string)<br>certificateDownloadLink (string)<br>certificateAuthorityDownloadLink (string, optional) | - | yes | no | no | no

>Table 4 - Predefined actions and their scope (instant, node, edge, zone)

#### 6.2.3.2 Action states
…(발췌: 전체 207,642자 중 앞 59,038자)
````

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |

A vertex is a fundamental component of multiple annotations.
Walls, measurements, doors, floor polygons and traffic lanes are created from two or more vertices.
To create a vertex, click on the vertex icon in the `Toolbar` and then click anywhere on the canvas.
The default attributes of a vertex are its coordinates along with an empty name field.
Additional attributes may be added by first selecting the vertex (which will turn it red), and then clicking the `Add` button in the figure.
Short descriptions of these are presented below:
* **is_holding_point:** if true and if the waypoint is part of a traffic lane,
  the `rmf_fleet_adapter` will treat this as a _holding point_ during path
  planning, i.e., the robot is allowed to wait at this waypoint for an indefinite
  period of time.
* **is_parking_spot:** robot's parking spot. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L73-L76)
* **is_passthrough_point:** waypoint which the robot shouldnt stop. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L63-L68)
* **is_charger:** if true and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will treat this as a charging station.
* **is_cleaning_zone** indicate if current waypoint is a cleaning zone, specifically for `Clean` Task.
* **dock_name:** if specified and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will issue an `rmf_fleet_msgs::ModeRequest` message with
  `MODE_DOCKING` and `task_id` equal to the specified name to the robot as it approaches this waypoint. This is used when the robot is executing their custom docking sequence (or custom travel path).
* **spawn_robot_type:** the name of the robot model to spawn at this waypoint in
  simulation. The value must match the model's folder name in the assets
  repository. More details on the robot model and plugin required for simulation
  can be found in [Simulation](simulation.md)
* **spawn_robot_name:** a unique identifier for the robot spawned at this
  waypoint. The `rmf_fleet_msgs::RobotState` message published by this robot
  will have `name` field equal to this value.
* **pickup_dispenser** name of the dispenser workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **dropoff_ingestor** name of the ingestor workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **human_goal_set_name** The `goal_sets.set_area` name, used by crowd simulation. For more info about `crowd_sim`, please see the [Crowdsim section] (https://osrf.github.io/ros2multirobotbook/simulation.html#crowdsim) of the Simulation Chapter for more details.

![Vertex attributes](images/traffic_editor/add_vertex.png)

Each vertex is stored in the `tutorial.building.yaml` file as a list of x-coordinate, y-coordinate, elevation, vertex_name and a set of additional parameters.

```yaml
  vertices:
    - [1364.76, 1336.717, 0, magni1_charger, {is_charger: [4, true], is_parking_spot: [4, true], spawn_robot_name: [1, magni1], spawn_robot_type: [1, Magni]}]
```
### Adding a measurement
|                    Icon                    |
|:------------------------------------------:|
| ![Measurement icon](images/traffic_editor/icons/measurement.svg)|

Adding a measurement sets the scale of the imported 2D drawing, which is essential for planning and simulation accuracy.
Scalebars or reference dimensions in the floor plan aid with the process. Often, you can draw the measurement line directly on top of a reference scale bar in a drawing.
With the editor in _Building_ mode, select the _Add Measurement_ tool and click on two points with known dimensions.
A pink line is rendered on the map with two vertices at its ends at the selected points.

Note:
A measurement line may be drawn by clicking on existing vertices.
In this scenario, no additional vertices are created at its ends.

Selecting the line populates various parameters in the Properties window of the `Sidebar`.
Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.
Currently, you must save the project and restart `traffic-editor` to see the changes reflected (todo: fix this...).

![Measurement properties](images/traffic_editor/add_measurement.png)

The above process adds two `vertices` and a `measurement` field to the `tutorial.building.yaml` file as seen below.
For the measurement field, the first two elements represent the indices of vertices representing the ends of
the line.
The `distance` value is stored in a sub-list of parameters.

```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
    measurements:
      - [1, 0, {distance: [3, 8.409]}]
    vertices:
      - [2951.728, 368.353, 0, ""]
      - [2808.142, 1348.9, 0, ""]

lifts:
  {}
name: building
```

### Adding a wall
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Wall icon](images/traffic_editor/icons/wall.svg)| `w` |

To annotate walls in the map, select the _Add Wall_ icon from the `Toolbar` and click on consecutive vertices that represent the corners of the wall.
The process of adding wall segments is continuous, and can be exited by pressing the `Esc` key.
Blue lines between vertices are rendered on the map which represent the drawn walls.
If the corner vertices are not present, they will automatically be created when using this tool.
Meshes of the annotated walls are automatically generated during 3D world generation using `building_map_generator`.
By default, the walls are of thickness of 10cm and height 2.5m.
The `wall_height` and `wall_thickness` attributes may be
modified [in the source code](https://github.com/open-rmf/rmf_traffic_editor/blob/main/rmf_building_map_tools/building_map/wall.py#L16-L17).

Wall texture options are available [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) in the source code.

![Annotating walls](images/traffic_editor/add_wall.png)

Walls are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices of the wall segment along with an empty parameter set.
```yaml
    walls:
      - [3, 4, {}]
      - [4, 5, {}]
      - [5, 6, {}]
      - [6, 7, {}]
      - [6, 8, {}]
      - [8, 9, {}]
```

### Adding a floor
|                    Icon                    |
|:------------------------------------------:|
| ![Floor icon](images/traffic_editor/icons/floor.svg)|

Flooring is essential for simulations as it provides a ground plane for the robots to travel over.
Floors are annotated using the _Add floor polygon_ tool from the `Main Toolbar` in _Building_ edit mode.
To define a floor, select consecutive vertices to create a polygon that accurately represents the flooring area as seen below.
These vertices will need to be added manually prior to this step.
Once created, save the project and reload.
Selecting the defined floor highlights its texture attributes. Similarly, [default list of available textures](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) is available in the source code.

![Highlighting floor's textures](images/traffic_editor/add_floor.png)

Certain scenarios may call for floors with cavities, for example, to represent elevator shafts.
The _Add hole polygon_ tool may be used for this purpose.
Additionally, the shape of a drawn polygon (floor or hole) may be modified using the _Edit polygon_ tool.
Clicking on the tool after selecting an existing polygon enables the user to modify vertices of the polygon.

Each polygon is stored in the `tutorial.building.yaml` file in the format below:
```yaml
    floors:
      - parameters: {texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [11, 10, 14, 15, 13, 12]
```

### Adding a door
|                    Icon                    |
|:------------------------------------------:|
| ![Door icon](images/traffic_editor/icons/door.svg)|

A door between two vertices can be added in _Building_ edit mode by selecting the _Add door_ tool from the `Main Toolbar`, and clicking on vertices representing the ends of the door.
Selecting an annotated door highlights its properties as seen in the figure below.
Presently, four door `types` are supported: "hinged", "double_hinged", "sliding" and "double_sliding".
The `motion_degrees` parameter specifies the range of motion in the case of hinged doors while the `motion_direction` dictates the direction of swing.
In order for the door to work in simulation, a `name` must be given to the door.

![Door type properties](images/traffic_editor/add_door.png)

Doors are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices along with the set of parameters that describes the door.

```yaml
 doors:
      - [24, 25, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, 1], name: [1, D001], type: [1, double_sliding]}]
```

### Adding a traffic lane
One of the most important tools in the `traffic_editor` GUI is the _Add lane_ tool.
The allowable motions of each fleet operating in the facility is conveyed through its respective Graph which consists of waypoints and connecting lanes.
In this approach, we assume that robots travel along effectively straight-line paths between waypoints.
While this may be perceived as an oversimplification of paths taken by robots that are capable of autonomous navigation, in practice the assumption holds fairly well given that these robots mostly travel along corridors or hallways and seldom in unconstrained open spaces.
For example, even in theoretically unconstrained spaces like building lobbies or shopping-mall atriums, it is likely that the site operator would prefer for the robots to operate in a "traffic lane" on the edge of the space, in order to not impede typical human traffic flows.

The `traffic` tab in the `Sidebar` has a default of nine Graphs for nine different fleets. To annotate lanes for a graph, say Graph 0, select the Graph from the `traffic` tab and click the _Add lane_ tool.
Lanes for this graph can be drawn by clicking vertices to be connected.
If a vertex is not present, it will automatically be added. Properties may be assigned to each vertex as described in the preceding section.
To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint.

![Graphs' lane colors](images/traffic_editor/add_lane.png)

Each Graph has a unique color for its lanes, and their visibility may be toggled using the checkbox in the `traffic` tab.
A lane that is defined between two waypoints may be configured with these additional properties:
* **bidirectional:** if `true`, the `rmf_fleet_adapter` will plan routes for its
  robot assuming the lanes can be traversed in both directions. Lanes that are
  not bidirectional have arrows indicating their directionality (indigo lanes in
  figure above). A handy shortcut is that when a lane segment is selected, you can
  press the `b` key to toggle between unidirectional and bidirectional motion along that lane.
* **graph_idx**: the Graph number a lane corresponds to
* **orientation**: constrain the lane to make the robot travel in `forward` or `backward` orientation. This can be useful for the final lane segment approaching a docking point or charger, for example.

While lifts that move between levels are now supported in the `traffic_editor`, the **demo_mock_floor_name** and **demo_mock_lift_name** properties were originally engineered to showcase shared lift access in a single floor demonstration environment with a "mock" lift that receives lift commands and transmits lift states but does not actually move between any different floors in a building.
However, as there may be interest in such functionality for testing single-floor hardware setups that seek to emulate multi-floor scenarios, these properties were retained.

* **demo_mock_floor_name**: name of the floor that the robot is on while
  traversing the lane
* **demo_mock_lift_name**: name of the lift that is being entered or exited
  while the robot traverses the lane

To further explain these properties, consider this representation of a
navigation graph where numbers are waypoints and letters are lanes:
```
1 <---a---> 2 <---b---> 3

Waypoint 1 is on floor L1
Waypoint 2 is inside the "lift" named LIFT001
Waypoint 3 is on floor L3
The properties of edge "a" are:
    bidirectional: true
    demo_mock_floor_name: L1
    demo_mock_lift_name: LIFT001
The properties of edge "b" are:
    bidirectional: true
    demo_mock_floor_name: L3
    demo_mock_lift_name: LIFT001
```

If the robot is to travel from waypoint 1 to waypoint 3, the `rmf_fleet_adapter` will request for the "mock lift" to arrive at L1 when the robot approaches waypoint 1.
With confirmation of the "lift" at L1 and its doors in "open" state, the robot will be instructed to move into the "lift" to waypoint 2.
Once the "lift" indicates that it has reached L3, the robot will exit along lane b toward waypoint 3.

Note: when annotating graphs, it is highly recommended to follow an ascending sequence of graph indices without skipping intermediate numbers. Drawn lanes can only be interacted with if their associated Graph is first selected in the `traffic` tab.

The annotated Graphs are eventually exported as `navigation graphs` using the `building_map_generator` which are then used by respective `rmf_fleet_adapters` for path planning.

Lanes are stored in the following format in `tutorial.building.yaml`.
The data structure is a list with the first two elements representing the indices of the two vertices of the lane and a set of parameters with configured properties.
```yaml
    lanes:
      - [32, 33, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 2], orientation: [1, forward]}]
```

### Deriving coordinate-space transforms

Coordinate spaces are confusing!
For historical reasons, the GUI internally creates traffic maps by annotating images, so the "raw" annotations are actually encoded in pixel coordinates of the "base" floorplan image, in pixel coordinates, with +X=right and +Y=down, with the origin in the upper-left of the base floorplan image.
However, during the building map generation step, the vertical axis is flipped to end up in a Cartesian plane, so the vast majority of RMF (that is, everything downstream of traffic-editor and the building map generators) uses a "normal" Cartesian coordinate system. (As an aside -- the next version of traffic-editor is intended to be more flexible in this respect, and will default to a normal Cartesian coordinate system (not an image-based coordinate system), or even global coordinates (lat/lon). Although preliminary work is underway, there is not a hard schedule for this next-gen editor at time of writing, so the rest of this chapter will describe the existing `traffic-editor`.)

Although `traffic-editor` currently uses the upper-left corner of the base floorplan image as the reference frame, maps generated by robots likely will have their origin elsewhere, and will likely be oriented and scaled differently.
It is critical to derive the correct transform between coordinate frames in `traffic_editor` maps and robot maps as
`rmf_fleet_adapters` expect all robots to publish their locations in the RMF coordinate system while the `rmf_fleet_adapters` also issue path requests in the same frame.

To derive such transforms, the `traffic_editor` GUI allows users to overlay robot maps on a floor plan and apply scale, translation and rotation transformations such that the two maps align correctly.
The user can then apply the same transformations to convert between robot map and RMF coordinates when programming interfaces for their robot.

The robot map can be imported by clicking the `Add` button from the `layers` tab in the `Sidebar`.
A dialog box will then prompt the user to upload the robot map image.
The same box contains fields for setting the scale for the image along with applying translations and rotation.
Through visual feedback, the user can determine appropriate values for these fields.
As seen in the image below, importing the robot-generated map into the GUI has it located and oriented
differently than the floor plan.
With the right transformation values, the two maps can be made to overlap.

![Overlap robot-generated map](images/traffic_editor/coordinate_transform.png)

### Adding fiducials
|                    Icon                    |
|:------------------------------------------:|
| ![Fiducial icon](images/traffic_editor/icons/fiducial.svg)|

For maps with multiple levels, fiducials provide a means to scale and align different levels with respect to a reference level.
This is crucial for ensuring dimensional accuracy of annotations across different levels and aligning the
same for simulation.
Fiducials are reference markers placed at locations which are expected to be vertically aligned between two or more levels.
For example, structural columns may run through multiple floors and their locations are often indicated on floor plans.
With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived between the two levels.
This transformation can then be applied to all the vertices and models in the newly defined level.

To begin, add two or more non-collinear fiducials to the reference level with unique `name` attributes using the _Add fiducial_ tool (left image in figure below).
In the newly created level, add the same number of fiducials at locations that are expected to be vertically aligned with matching names as the reference level (right image in figure below).
Saving and reloading the project computes the transformation between the levels which is evident from the Scale
and X-Y offsets for the new level as seen in the `levels` tab.
This level is now ready to be annotated.

![Adding fiducials](images/traffic_editor/add_fiducial.png)

For each level, fiducials are stored in a list of their X & Y coordinates along with their name.
```yaml
    fiducials:
      - [936.809, 1323.141, F1]
      - [1622.999, 1379.32, F2]
      - [2762.637, 346.69, F3]
```

### Adding a lift
Lifts are integral resources that are shared between humans and robot fleets in multi-level facilities.
To add a lift to a building, click the `Add` button in the `lifts` tab in the `Sidebar`.
A dialog box with various configurable properties will load.
It is essential to specify the Name, Reference level and the X&Y coordinates (pixel units) of its cabin center.
A yaw (radians) may further be added to orient the lift as desired.
The width and depth of the cabin (meters) can also be customized.
Lifts can be designed to have multiple cabin doors which may open at more than one level.
To add a cabin door, click the `Add` button in the box below the cabin image.
Each cabin door requires a name along with positional and orientational information.
Here, the X&Y coordinates are relative to the cabin center.

![Configuring lift properties](images/traffic_editor/add_lift.png)

The configured lift is stored in the `tutorial.building.yaml` file as described below:
```yaml
lifts:
  LF001:
    depth: 2
    doors:
      door1:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: 1
        y: 0
      door2:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: -1
        y: 0
    level_doors:
      L1: [door1]
      L2: [door2]
    reference_floor_name: L1
    width: 2
    x: 827
    y: 357.7
    yaw: 1.09
```

After adding the lift, we would also wish to let our robots to transverse through the lift.
To achieve that, the user needs to create vertices/waypoints which are located within the lift cabin on each floor.
Once done, connect the waypoint within the lift cabin to other vertices via __add_lane__.

### Adding environment assets
Levels may be annotated with thumbnails of models available for simulation using the __Add model__ tool in __Building__ edit mode.
Selecting this tool opens a dialog box with a list of model names and matching thumbnails which can be imported to the map.
Once on the map, their positions and orientations can be adjusted using the _Move_ and _Rotate_ tools. Sample models are provided [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor_assets/assets/thumbnails/images/cropped/OpenRobotics)

The [thumbnail_generator documentation](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor#generating-custom-thumbnails) contains instructions on expanding the list of thumbnails for other models.

> Note: If no models are shown on the __add models__ window, Go to "Edit -> Preference", then indicate the thumbnail path. (`e.g. $HOME/rmf_ws/src/rmf/rmf_traffic_editor/rmf_traffic_editor_assets/assets/thumbnails`)

![Model name and thumbnails dialog](images/traffic_editor/add_model.png)

## Conclusion
This chapter covered various capabilities of the `traffic_editor` which are useful for annotating maps of facilities while adhering to a standardized set of semantics.
Examples of other traffic editor projects can be found in the [rmf_demos](https://github.com/open-rmf/rmf_demos) repository.
Running physics based simulations with RMF in the annotated sites is described in the [Simulation](simulation.md) chapter.
````
