(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-12
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 33. 시나리오 모델·편집 (I. 설계·시뮬레이션)
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

### runs/2026-09-30-12/target.json

```json
{
  "run_id": "2026-09-30-12",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 121,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 33,
    "area_name": "33. 시나리오 모델·편집",
    "category": "I. 설계·시뮬레이션",
    "category_letter": "I"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=33"
}
```

### runs/2026-09-30-12/research.json

```json
{
  "run_id": "2026-09-30-12",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 33,
    "area_name": "33. 시나리오 모델·편집",
    "category": "I. 설계·시뮬레이션"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 시나리오 기술 언어, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 장애 주입 선언, 반증 기반 시험 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(호텔·공항)·병원(클리닉)·실외(캠퍼스)·가정(가정 활동)·제조 공장(배터리 생산) 시나리오 예제와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 확률적 시나리오 언어, 건물 주석 편집기, 행동 트리·BPMN 같은 미션 형식, LLM 기반 환경·시나리오 생성 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ASAM OpenSCENARIO, SDFormat, VDMA LIF, Open-RMF rmf_demos·traffic-editor, BEHAVIOR-1K·BDDL, NIST ARIAC, MovingAI MAPF 벤치마크, Groot2 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131·oq-135 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]",
    "로봇 시뮬레이션·자율 시스템 시험에서 쓰는 시나리오 기술 형식·언어는 무엇이며 환경·개체·작업·사건·장애를 어떻게 나누어 담고 판(버전)을 어떻게 관리하는가? (섹션 4·6·7 겨냥)",
    "현장 유형별(호텔·병원·공장·가정·실외·물류창고) 시나리오 예제·템플릿 라이브러리로 공개된 것은 무엇이고 각각 무엇을 담는가? (섹션 5·7 겨냥, 한국 자료 우선)",
    "사람이 화면에서 시나리오·워크플로·미션을 그리고 고치는 편집기와 미션 기술 형식(행동 트리·상태 기계·BPMN 등)은 무엇이며 비교 연구는 무엇을 말하는가? (섹션 6·7·8 겨냥)",
    "언어 모델로 시뮬레이션 환경·시나리오를 자동 생성하는 연구는 무엇을 입력으로 받아 무엇을 만들고 어떻게 평가했는가? (섹션 6·8 겨냥, 9. 채팅으로 시나리오 구성과의 연결)",
    "oq-131 플릿 관제 실행 기록을 시나리오 사양으로 바꾸는 공개 형식·변환 규칙, oq-135 시나리오 구성 시 되물어야 할 항목의 표준 목록이 있는가? (섹션 11 겨냥)",
    "33. 시나리오 모델·편집에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·로봇 제조사·설비 쪽에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Vin 외의 Scenic 3.0(CAV 2023)은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어 Scenic 에 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, 선형 시간 논리(LTL)로 쓰는 시간 요구사항을 더해 반증(falsification) 기반 시험에 쓸 수 있게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1135"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: Scenic 3.0 은 3D 기하 지원, 박스 대신 복잡한 형상의 정밀 모델과 가림을 반영한 광선 추적 가시성, LTL 로 표현한 임의의 시간 요구를 추가했고, Scenic 2 로는 정확히 모델링할 수 없던 사례를 보였다.",
      "as_of": "2023-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "ASAM OpenSCENARIO XML 은 주행·교통 시뮬레이터의 동적 내용(차량·보행자 등 여러 개체의 동기화된 기동)을 계층 구조의 XML 파일(.xosc)로 기술하는 표준으로, 2026-05-19 에 1.4.0 판이 나왔고, 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1141"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 소개: 1.4.0 판(2026-05-19), 파일 형식 xosc. \"complete scenario descriptions support parameterization, which allows test automation without the need to create a large amount of scenario files\"",
      "as_of": "2026-05-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "ASAM 은 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO XML 은 그 위의 동적 내용만 담게 나누며, 병행 표준 OpenSCENARIO DSL 은 대규모 검증용, XML 은 예측 가능한 정밀 시나리오용으로 역할을 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1141"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 소개: OpenSCENARIO XML 은 도로망용 OpenDRIVE, 노면용 OpenCRG 와 함께 쓰이며, DSL 은 대규모 자율주행 검증을, XML 은 V&V 용 정밀 시나리오를 겨냥한다.",
      "as_of": "2026-05-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Open-RMF 의 rmf_demos 는 호텔 월드로 로비와 객실 2개 층, 승강기 2대, 여러 문, 로봇 플릿 3개(로봇 4대)가 층을 오가며 순찰(loop)·청소 작업을 하는 다중 플릿 시나리오를 예제로 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: Hotel World — 로비와 객실 2개 층, 승강기 2대, 문 여러 개, 플릿 3개(로봇 4대). 작업: Loop, Clean. 실행 예: dispatch_clean -cs clean_lobby (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f5",
      "claim": "rmf_demos 의 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 여러 플릿과 설비·이용자의 상호작용을 보이며, 선택적으로 군중 시뮬레이션을 켜고 사람이 직접 모는 읽기 전용(read_only) 카트를 함께 두고 순찰·배송·청소 작업을 실행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: Airport Terminal World — 대규모 환경, 여러 플릿, use_crowdsim:=1 로 군중 시뮬레이션 추가, 수동 조작 read_only 카트. 작업: Loop, Delivery, Clean (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "rmf_demos 의 클리닉 월드는 승강기 2대가 있는 2개 층 시설에서 역할이 다른 로봇 플릿 2개가 층을 오가며 간호 스테이션 사이를 순찰하는 병원형 시나리오 예제다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: Clinic World — 2개 층, 승강기 2대, 역할이 다른 플릿 2개. 예: dispatch_patrol -p L1_left_nurse_center L2_right_nurse_center -n 5 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "rmf_demos 의 캠퍼스 월드는 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스에서 여러 배송 로봇이 장거리 순찰을 하는 실외 시나리오 예제이고, 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: Campus World — WGS84 좌표의 행성 규모 데모, 배송 로봇 여러 대. Manufacturing & Logistics World — 작업셀(컨베이어, 고정 매니퓰레이터)과 AMR 플릿, 영상 기반 데모 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "작업 대상"
    },
    {
      "id": "f8",
      "claim": "rmf_demos 에서 시나리오는 월드(건물 구성·차선·승강기·문·충전 위치)를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣는 구조이며, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 월드는 traffic editor 로 차선·웨이포인트를 정의하고 승강기·문·충전소를 건물 구성에 주석하며, 작업은 dispatch_* 명령으로 넣고 dispatcher 노드가 플릿 어댑터 간 입찰을 조율한다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f9",
      "claim": "Open-RMF 의 traffic-editor 는 시설 지도 위에 벽·문(여닫이·미닫이·양문)·층·승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, 층 정렬용 기준점을 그려 넣는 GUI 편집기로, 결과를 .building.yaml 파일로 저장하고 building_map_generator 가 이를 물리 시뮬레이션 월드로 자동 생성한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "책 traffic-editor 장: 층별 정점·벽·차선·문·승강기·모델 배치를 담은 .building.yaml 로 저장하며 GUI 편집과 프로그램 접근을 모두 지원하고, 2D 주석에서 3D 시뮬레이션 월드를 만든다. \"Traffic conventions for multi-robot systems do not exist\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Stanford 등의 BEHAVIOR-1K(arXiv 2403.09227, 예비판 CoRL 2022)는 '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(BDDL)로 형식 명세하고, 주택·정원·식당·사무실 등 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상, 강체·변형체·액체를 다루는 OmniGibson 시뮬레이터 위에 구현한 활동 라이브러리다.",
      "tag": "사실",
      "source_ids": [
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 1,000개 일상 활동, 장면 50개(주택·정원·식당·사무실 등), 객체 9,000개 이상, BDDL 로 활동 명세, OmniGibson 에서 강체·변형체·액체 시뮬레이션. 활동은 장기 과제이고 복잡한 조작 기술에 의존한다.",
      "as_of": "2024-03",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f11",
      "claim": "NIST ARIAC 문서의 시나리오는 전기차 배터리 생산 시설로, 배터리 셀 4개를 트레이에 담는 키팅과 셀 4개와 상하 케이스로 모듈을 조립하는 두 작업을 주문으로 받고, 우선순위가 높은 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않게 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1140"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ARIAC 문서 scenario: EV 배터리 생산 시설, 키트는 셀 4개를 트레이에 담은 묶음, 모듈은 셀 4개와 상하 케이스를 용접 연결한 단위. 셀 전압 허용치 ±0.2 V (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "제조 공장",
      "flow_item": "작업 대상"
    },
    {
      "id": "f12",
      "claim": "NIST ARIAC 는 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(시작·지속·대상 TESTER), 진공 그리퍼 파지 실패(TOOL·몇 번째 파지인지 GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID) 네 가지 민첩성 과제를 매개변수로 선언해, 장애와 긴급 요청을 시각 또는 발생 횟수 조건으로 시나리오에 주입한다.",
      "tag": "사실",
      "source_ids": [
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ARIAC 문서 challenges: Conveyor Malfunction, Voltage Tester Malfunction, Vacuum Tool Malfunction, High Priority Order 네 과제. 컨베이어·시험기 고장은 경과 초로, 진공 그리퍼는 \"which grasp attempt will fail\" 로 발동 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Kästner 외의 Arena-Bench(RA-L 2022)는 동적 환경의 시나리오·월드 생성 도구와 평가 지표를 갖춘 벤치마크 모음으로, 3차원 환경에서 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오로 비교하고 실물 로봇 배치까지 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-726"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"a benchmark suite to train, test, and evaluate navigation planners on different robotic platforms within 3D environments\" — 동적 평가 시나리오 설계 도구와 평가 지표 포함.",
      "as_of": "2022-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Shcherbyna 외의 Arena 4.0(arXiv 2409.12471)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1143"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: LLM 과 확산 모델로 텍스트나 2D 평면 배치에서 사람 중심 환경을 동적으로 생성, 의미 주석 3D 자산 DB, ROS 2 이전, 사용자 연구로 사용성·효율 개선 확인, CC BY 4.0 공개.",
      "as_of": "2024-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Yang 외의 Holodeck(CVPR 2024)은 GPT-4 가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하는 방식으로 오락실·스파·박물관 같은 상호작용 가능한 환경을 자동 생성하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했고 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-815"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: AI2-THOR 기반, GPT-4 로 장면 의미와 공간 관계 제약 생성 후 최적화 배치, 주거 장면 인간 평가에서 절차적 기준선보다 선호, 음악실·어린이집 제로샷 주행.",
      "as_of": "2023-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "행동 트리 편집기 Groot2 는 끌어놓기로 트리를 만들며 XML 을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1145"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 무료판은 편집·모니터링을 노드 20개까지, PRO(연 590유로 유동 라이선스)는 블랙보드 시각화, 대화형 중단점, 장애 주입, 대형 트리 노드 검색 제공. 로그를 열어 여러 속도로 재생 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "Filippone·Pettinari·Pelliccione(IEEE TSE, arXiv 2603.15427)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·표현력·도구 지원 측면에서 비교하며, 미션을 명세하는 표준이나 널리 받아들여진 형식이 없고 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다고 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"there is no standard or widely accepted formalism for specifying missions in single- or multi-robot systems\" — 네 형식의 장단점을 비교해 탄력적인 미션 설계 형식 선택을 돕는다.",
      "as_of": "2026-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "Moving AI 연구실의 MAPF 벤치마크는 도시·게임·창고형·무작위·미로·방 등 격자 지도 36개마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 모두 1,800개의 시나리오 파일을 공개한 재사용 가능한 시나리오 라이브러리다.",
      "tag": "사실",
      "source_ids": [
        "ref-1147"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤치마크 페이지: 지도 36개, 지도마다 random 25·even 25 시나리오(.scen), 총 1,800개 파일. 창고 지도는 통로 배치를 격자로 추상화한 것이다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "SDFormat(Simulation Description Format)은 로봇 시뮬레이터·시각화·제어용으로 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo 에서 시작했고 Open Source Robotics Foundation 이 Apache 2.0 으로 관리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1148"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 사이트: \"an XML format that describes objects and environments for robot simulators, visualization, and control\" — 라이브러리 libsdformat 16.0.0 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰는 비구속적 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받아 만들어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 판 1.0.0(2023-09), 목적은 \"initial transfer of a track layout to a central (third-party) master control system\", VDA5050 의 영향, 비구속적 접근이라는 면책 문구.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 형식들은 공통으로 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃, OpenDRIVE 도로망)과 동적 내용(작업 명령, OpenSCENARIO 스토리보드, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하며, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 두지만 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1148",
        "ref-079",
        "ref-046",
        "ref-1141",
        "ref-104",
        "ref-528",
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3·f8·f9·f10·f12·f19·f20 의 종합. 시나리오 인스턴스 버전 관리 규칙은 어느 출처에도 없었다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 공개 형식은 분야별로 나뉘어(자율주행 OpenSCENARIO, 가정 활동 BDDL, 시설 다중 로봇 Open-RMF 건물 파일과 작업 명령, 제조 ARIAC 과제 설정, MAPF .scen) 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 찾지 못했고 미션 기술에도 표준이 없으며(f17), 재사용은 매개변수화·카탈로그(f2), 확률 분포 표본 추출(f1), 현장 유형별 예제 월드(f4~f7), 대규모 활동·시나리오 라이브러리(f10·f18), 언어 모델 생성(f14·f15)으로 이루어지는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1141",
        "ref-971",
        "ref-104",
        "ref-528",
        "ref-1147",
        "ref-116",
        "ref-1135",
        "ref-1143",
        "ref-815"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f4~f10·f12·f14·f15·f17·f18 의 종합 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 계획기·정책을 같은 조건에서 비교하려면 고정된 시나리오 파일이 있어야 하고(f13·f18), 장애·긴급 요청을 시나리오에 선언해야 예외 대응 시험을 반복할 수 있으며(f12), 매개변수화가 없으면 조건별 시나리오 파일이 불어나고(f2), 비전문가가 미션과 환경을 정의해야 하는데 공통 형식이 없기 때문이다(f17).",
      "tag": "추정",
      "source_ids": [
        "ref-726",
        "ref-1147",
        "ref-528",
        "ref-1141",
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f12·f13·f17·f18 의 종합 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "확인한 자료를 종합하면 33. 시나리오 모델·편집에서 ROP가 직접 맡을 범위는 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 버전 있는 시나리오 모델(f8·f12·f21), 현장 유형별 예제 라이브러리(f4~f7), 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택(f9·f16·f17), 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환(f9·f19)으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-104",
        "ref-528",
        "ref-079",
        "ref-1145",
        "ref-116",
        "ref-1148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4~f9·f12·f16·f17·f19·f21 의 종합 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 로봇 기구학·센서 모델(SDFormat 로봇 기술, f19)은 시뮬레이터·로봇 제조사 쪽에, 컨베이어·작업셀 같은 설비 제어(f7·f12)는 설비 쪽에, 도로 교통 시나리오 표준(f2·f3)은 자율주행 분야에 속하므로, ROP 는 이들을 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1148",
        "ref-104",
        "ref-528",
        "ref-1141"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3·f7·f12·f19 와 분류 원문 19장 경계의 종합 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "이 영역은 시나리오를 대화로 만드는 9. 채팅으로 시나리오 구성(f14·f15)과 11. 채팅으로 실제 상황 시뮬레이션 재현, 시나리오를 실행하는 34. 시뮬레이션·예측용 디지털 트윈(f19), 기록 재생·재현의 36. 가상 시운전·실제 상황 재현(f16), 규모 산정의 35. 처리능력·규모·배치 설계, 건물·레이아웃 주석의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f9·f20), 군중·보행자의 19. 사람·보행자 모델(f5·f14), 승강기 연동의 22. 설비·건물 시스템 연동(f4·f6), 미션 형식의 24. 작업·워크플로 모델링(f17), 장애 주입의 32. 예외 복구·재계획·업무 연속성(f12), 경로 시나리오의 27. 다중 로봇 경로·교통 관리 — MAPF(f18), 언어 모델 생성의 44. 로봇 기반 모델·언어 모델 계획(f15), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f13·f18), 적용 현장인 62. 제조 공장(f11·f12)·63. 병원·의료(f6)·64. 상업 시설(f4·f5)·65. 가정·공동주택(f10)·66. 실외(f7)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1143",
        "ref-815",
        "ref-1148",
        "ref-1145",
        "ref-079",
        "ref-046",
        "ref-104",
        "ref-116",
        "ref-528",
        "ref-1147",
        "ref-1135",
        "ref-726",
        "ref-1140",
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f20 의 연결 판단.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1135",
      "org": "Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv)",
      "title": "3D Environment Modeling for Falsification and Beyond with Scenic 3.0",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.03325",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "확률적 시나리오 언어 Scenic 의 3.0 판. 3D 기하, 가림 고려 가시성, LTL 시간 요구를 더해 반증 기반 시험에 쓴다(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open-RMF (open-rmf/rmf_demos)",
      "title": "rmf_demos — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "호텔·사무실·공항 터미널·클리닉·캠퍼스·제조·물류 데모 월드와 작업 명령(dispatch_*)으로 구성된 Open-RMF 예제 시나리오 모음.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_demos/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics (osrf/ros2multirobotbook)",
      "title": "Programming Multiple Robots with ROS 2 — Traffic Editor",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "시설 지도에 벽·문·승강기·차선·웨이포인트 속성을 주석해 .building.yaml 로 저장하고 시뮬레이션 월드를 생성하는 GUI 편집기 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-971",
      "org": "Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv)",
      "title": "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09227",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BDDL 로 명세한 일상 가정 활동 1,000개, 장면 50개, 객체 9,000개 이상을 OmniGibson 에 구현한 벤치마크(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "컨베이어·전압 시험기·진공 그리퍼 고장과 긴급 주문의 네 민첩성 과제와 발동 매개변수 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/challenges.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1140",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Scenario",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립 작업, 주문과 우선순위, 품질 허용치 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/scenario.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1141",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO® XML",
      "published": null,
      "url": "https://www.asam.net/standards/detail/openscenario-xml/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "주행·교통 시뮬레이터의 동적 내용을 기술하는 XML 표준의 공식 소개. 1.4.0 판(2026-05-19), 카탈로그·매개변수화, OpenDRIVE·DSL 과의 관계.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-726",
      "org": "Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv)",
      "title": "Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments",
      "published": "2022-06",
      "url": "https://arxiv.org/abs/2206.05728",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "동적 환경 시나리오·월드 생성 도구와 평가 지표로 주행 계획기를 비교하는 벤치마크 모음(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1143",
      "org": "Shcherbyna, V. 외 (arXiv)",
      "title": "Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.12471",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM·확산 모델로 텍스트·2D 평면 배치에서 사람 중심 주행 환경을 생성하는 ROS 2 플랫폼(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-815",
      "org": "Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv)",
      "title": "Holodeck: Language Guided Generation of 3D Embodied AI Environments",
      "published": "2023-12",
      "url": "https://arxiv.org/abs/2312.09067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GPT-4 와 공간 관계 제약 최적화로 텍스트에서 상호작용 가능한 3D 환경을 생성(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1145",
      "org": "BehaviorTree.CPP 프로젝트 (behaviortree.dev)",
      "title": "Groot2",
      "published": null,
      "url": "https://www.behaviortree.dev/groot/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "행동 트리 편집·모니터링·로그 재생 도구 Groot2 의 기능과 무료·PRO 판 차이를 소개하는 제품 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv)",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "행동 트리·상태 기계·HTN·BPMN 을 미션 기술 형식으로 비교한 연구(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1147",
      "org": "Moving AI Lab (Sturtevant 외)",
      "title": "MAPF Benchmarks",
      "published": null,
      "url": "https://movingai.com/benchmarks/mapf/index.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "격자 지도 36개와 지도당 .scen 시나리오 50개를 공개한 다중 에이전트 경로 찾기 벤치마크.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1148",
      "org": "Open Source Robotics Foundation",
      "title": "SDFormat (Simulation Description Format)",
      "published": null,
      "url": "http://sdformat.org/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "로봇 시뮬레이터·시각화·제어용으로 로봇과 환경을 기술하는 XML 형식의 공식 사이트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF)",
      "title": "Layout Interchange Format (LIF) — README",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "무인운반차 통합업체가 주행 레이아웃을 제3자 상위 관제에 넘기는 VDMA 교환 형식 1.0.0 저장소 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Intralogistics-2X-LIF/Layout-Interchange-Format/main/README.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
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
      "rationale": "섹션 3: f23(왜 중요한가), f22(핵심 질문 답, 추정) / 섹션 4: 확률적 시나리오 언어·반증 f1, 매개변수화·카탈로그 f2, 정적 환경과 동적 내용 분리 f3·f21, 장애 주입 선언 f12, 미션 기술 형식 f17 / 섹션 5: 상업 시설 — f4(호텔, 수행 자원)·f5(공항 터미널, 제약: 군중·수동 카트), 병원 — f6(클리닉, 제약: 층간 승강기), 실외 — f7(캠퍼스, 작업 대상: WGS84 공간), 가정 — f10(일상 활동 라이브러리), 제조 공장 — f11(배터리 생산 작업 대상)·f12(장애 주입 예외·성과). 물류창고는 f18 격자 지도와 f20 레이아웃 형식뿐이고 실제 현장 사례는 찾지 못함을 명시 / 섹션 6: 확률적 언어 f1, 건물 주석 편집 f9, 월드+작업 명령 구조 f8, 미션 형식 비교 f17, 행동 트리 편집·재생 f16(벤더 주장 병기), 언어 모델 기반 환경 생성 f14·f15 / 섹션 7: ASAM OpenSCENARIO f2·f3, SDFormat f19, VDMA LIF f20, Open-RMF rmf_demos·traffic-editor f4~f9, BEHAVIOR-1K·BDDL f10, NIST ARIAC f11·f12, MovingAI MAPF f18, Arena f13·f14, Groot2 f16 / 섹션 8: f1·f10·f13·f14·f15·f17 / 섹션 9: f24(직접 범위), f25(연계 대상) / 섹션 10: f26 — 9, 11, 14, 15, 19, 22, 24, 27, 32, 34, 35, 36, 44, 54, 62, 63, 64, 65, 66 / 섹션 11: 기존 oq-131·oq-135(미해결)와 open_questions_new 4건. 다음 실행 후보: 9. 채팅으로 시나리오 구성 페이지에 f14·f15, 36. 가상 시운전·실제 상황 재현 페이지에 f12·f16 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "오픈시나리오",
      "term_en": "ASAM OpenSCENARIO",
      "definition": "ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다."
    },
    {
      "term_ko": "행동 영역 정의 언어",
      "term_en": "Behavior Domain Definition Language (BDDL)",
      "definition": "BEHAVIOR 벤치마크가 가정 활동을 시뮬레이션된 물리 상태와 연결된 논리 술어로 형식 명세하는 데 쓰는 도메인 특화 언어다."
    },
    {
      "term_ko": "시뮬레이션 기술 형식",
      "term_en": "Simulation Description Format (SDFormat)",
      "definition": "Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다."
    },
    {
      "term_ko": "반증 기반 시험",
      "term_en": "Falsification",
      "definition": "시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다."
    }
  ],
  "open_questions_new": [
    "환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 관련 영역: 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f21 | 종류: 일반",
    "형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반",
    "ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반",
    "국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 65. 가정·공동주택 | 근거: f4 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f10 BDDL 이 활동을 초기 조건·목표 조건 쌍으로 정의한다는 세부 구조는 검색 요약에만 있어 claim 에 넣지 않음",
      "f1 Scenic 이 한 프로그램에서 표본 추출로 여러 장면을 만든다는 설명과 로봇 적용 사례(암석 지대)는 검색 요약에만 있어 넣지 않음",
      "f15 Holodeck 3D 자산 수(약 5만 개)는 검색 요약에만 있어 넣지 않음",
      "f13 Arena 시나리오 편집기의 끌어놓기 배치·보행자 웨이포인트 기능은 검색 요약에만 있어 넣지 않음",
      "f16 Groot2 기능은 제품 페이지뿐이며 독립 출처로 교차 확인하지 못함",
      "f2 OpenSCENARIO XML 1.4.0 명세 본문은 열지 않았고 공식 소개 페이지 기준",
      "oq-131 미해결: 플릿 실행 기록을 시나리오로 바꾸는 공개 형식은 찾지 못함(찾은 JoyAI-Sim arXiv 2606.16776 은 탁상 조작 과제 재구성이라 제외)",
      "oq-135 미해결: 시나리오 구성 시 되물을 항목의 표준 목록은 이번 조사에서 찾지 못함(검색하지 못함)",
      "물류창고 실제 현장의 시나리오 예제·템플릿 사례와 국내 자료는 찾지 못함",
      "Bourr·Tiezzi 의 BPMN→X-Klaim 변환(arXiv 2311.04126)은 철회된 논문이라 제외",
      "Moskovskaya 외 안내 로봇 LLM 시나리오 생성(arXiv 2509.10317)은 대화 행동 대본 의미의 시나리오라 제외"
    ],
    "scope_violations": [
      "f19: SDFormat 의 로봇 기구학·센서 기술은 로봇 제조사·시뮬레이터 쪽 내용이므로 형식 참조 근거로만 쓰고 f25 에서 연계 대상으로 구분함",
      "f2·f3: OpenSCENARIO 는 자율주행 도로 시나리오 표준이므로 ROP 직접 범위가 아니라 참조 설계 사례로만 제안함",
      "f7·f12: 컨베이어·작업셀 설비 제어는 설비 쪽 연계 대상이며 시나리오에 장애를 선언하는 방식만 근거로 씀",
      "f8·f21: 시나리오는 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 섞지 않음",
      "f14·f15: 언어 모델 기반 생성은 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획)과 9. 채팅으로 시나리오 구성에도 연결하도록 제안함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1135~ref-046, 예약 구간 안)로 출처 상한에 도달해 물류창고 실제 현장 시나리오와 국내 자료, oq-135 조사를 더 하지 못했다. 재사용 출처 없음: NIST ARIAC 는 공통 규칙상 ref-008 이지만 입력 참고문헌 요약에 ref-008 의 등록 URL·제목이 없어 이번에 연 개별 문서 페이지(challenges·scenario)를 새 id(ref-528·ref-1140)로 적었다. 같은 URL 이면 퍼블리셔가 합치고, 다르면 ref-008 과의 관계를 검증에서 확인해 주기 바란다. 원문 열람: 15건 모두 열었다(webfetch 10건, github_raw 5건). 논문은 모두 초록 페이지 기준이다. VDMA LIF 지침 PDF 는 본문 추출에 실패해 공식 저장소 README 로 대신했다. 교차 확인 0건: 각 형식·사례가 한 출처에만 기술되어 있어 finding 신뢰도는 medium 이하로 두었다. Groot2 기능(f16)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에는 f22 로 답했고 결론은 '공개 형식은 분야별로 나뉘고 공통 표준은 없으며, 재사용은 매개변수화·표본 추출·예제 라이브러리·언어 모델 생성으로 이루어진다'는 추정이다. 현장 유형 사례는 상업 시설(f4·f5)·병원(f6)·실외(f7)·가정(f10)·제조 공장(f11·f12)이며 물류창고는 격자 지도 벤치마크(f18)와 레이아웃 교환 형식(f20)만 있고 현장 사례는 찾지 못했다. 국내 자료는 한국어 검색 2회에서 이 영역에 맞는 것을 찾지 못했다(찾은 한국지능시스템학회 시뮬레이터 리뷰는 시나리오 정의를 다루지 않아 제외). 기존 열린 질문 oq-131·oq-135 는 해결 근거가 없어 해결 제안하지 않았다. 용어집에 이미 있는 행동 트리·BPMN·HTN·레이아웃 교환 형식·가상 시운전·시나리오 재구성·미션 명세 패턴은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-12/verification.json

```json
{
  "run_id": "2026-09-30-12",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2307.03325 초록(2023-07-06 제출, CAV 2023)에 3D 기하, 광선 추적 기반 가림 고려 가시성, LTL 시간 요구, Scenic 2로는 정확히 모델링할 수 없던 사례가 모두 있다. 제목에 'Falsification'이 있다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ASAM 공식 소개 페이지에 1.4.0(2026-05-19), .xosc, 여러 개체의 동기화된 기동, 기동·동작·궤적 카탈로그와 매개변수화, '대량의 시나리오 파일 없이 시험 자동화' 구절이 있다. 명세 본문은 열지 않았으며 공식 소개 페이지 기준이다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 공식 소개 페이지가 OpenDRIVE(도로망)·OpenCRG(노면)와 함께 정적·동적 내용을 나눠 맡는다고 적고, XML은 V&V용 정밀 시나리오, DSL은 AV·ADAS 대규모 V&V용이라고 구분한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_demos README에 호텔 월드(로비+객실 2개 층, 승강기 2대, 문 여러 개, 플릿 3개·로봇 4대, Loop·Clean 작업)가 있다. 실제 현장이 아니라 시뮬레이션 예제 월드다. 발행일 미확인(확인일 2026-09-30)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README에 공항 터미널 월드의 대규모 환경, 군중 시뮬레이션 선택 기능, 키보드·조이스틱으로 원격 조작하는 read_only 카트, dispatch_patrol·dispatch_delivery·dispatch_clean 예시 명령이 있다. 시뮬레이션 예제 월드다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 클리닉 월드(2개 층, 승강기 2대, 역할이 다른 플릿 2개)와 dispatch_patrol -p L1_left_nurse_center L2_right_nurse_center -n 5 명령이 있다. 시뮬레이션 예제 월드다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README에 캠퍼스 월드(행성 규모, GPS WGS84 좌표, 순찰 명령)와 영상으로만 보이는 제조·물류 월드(작업셀=컨베이어·고정 매니퓰레이터, AMR 플릿 여러 개)가 있다. 한 finding에 실외 사례(캠퍼스)와 영상 데모(제조·물류)가 섞여 있어 5절에서 나눠야 한다(required_fixes)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README에 traffic_editor로 월드를 설계한다는 설명, dispatch_* 작업 명령, 디스패처가 BidNotice를 모든 플릿 어댑터에 보내 비용 제안을 받아 낙찰하는 입찰 모델이 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ros2multirobotbook traffic-editor 장(github_raw 원본)에 벽, 문 네 종류(hinged·double_hinged·sliding·double_sliding), 승강기, 기본 그래프 9개, 충전·주차·대기·도킹·로봇 생성 웨이포인트, 층 정렬 기준점, .building.yaml, building_map_generator가 있고 'Traffic conventions for multi-robot systems do not exist' 구절도 있다. 발행일 미확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2403.09227 초록(2024-03-14 제출)에 활동 1,000개, 장면 50개(주택·정원·식당·사무실 등), 객체 9,000개 이상, OmniGibson의 강체·변형체·액체 시뮬레이션, CoRL 2022 예비판, 'what do you want robots to do for you' 설문이 있다. 장면에 식당·사무실이 들어 있어 '가정' 현장 유형은 활동의 성격(일상 가정 활동) 기준임을 밝혀야 한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ARIAC scenario.rst에 EV 배터리 생산 시설, 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 된 모듈, 셀 전압 허용치 ±0.2 V가 있다. 다만 원문은 '아직 발표될(to be announced) 긴급 주문이 남아 있으면 ORDERS_COMPLETE로 바뀌지 않는다'고 적으므로 '남아 있으면'을 '아직 발표되지 않은 긴급 주문이 남아 있으면'으로 좁혀야 한다(required_fixes). 경진대회 시뮬레이션 시나리오이며 실제 공장 사례가 아니다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ARIAC challenges.rst에 네 과제와 매개변수(START_TIME·DURATION, TESTER, TOOL·GRASP_OCCURRENCE, START_TIME·ID)가 있고 'which grasp attempt will fail' 구절이 있다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2206.05728(2022-06-12 제출, RA-L 2022) 초록에 동적 평가 월드·시나리오·과제 설계·생성 도구, 여러 지표, 모델 기반·학습 기반 비교, 여러 로봇 플랫폼, 3D 환경, 실물 로봇 배치가 있다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2409.12471(2024-09-19 제출) 초록에 LLM·확산 모델로 텍스트 프롬프트나 2D 평면도에서 사람 중심 환경 생성, 의미 주석 3D 모델 DB, ROS 2 이전, 사용자 연구에서 이전 판 대비 사용성·효율 개선이 있다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록에 GPT-4, 공간 관계 제약과 배치 최적화, Objaverse, 오락실·스파·박물관, 주거 장면 인간 평가에서 절차적 기준선보다 선호, 음악실·어린이집 주행 학습이 있다. 평면 배치·재질·문과 창은 초록에 없지만 검증자가 연 arXiv HTML 본문에 있다(GPT-4가 방 좌표·치수·연결, 바닥·벽 재질, 문·창 사양을 정함). 근거 발췌의 '초록' 표기는 본문 내용을 포함한 것이다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: behaviortree.dev/groot 제품 페이지에 끌어놓기 편집, XML 실시간 미리보기, 실행 중인 BT.CPP 실행기 연결·모니터링, 여러 속도의 로그 재생, 무료판 20노드 제한, PRO(연 590유로)의 블랙보드 시각화·대화형 중단점·장애 주입·노드 검색이 있다. vendor_claim: true, 태그 추정, '벤더 주장' 첫머리 표시가 맞다. 독립 확인은 없다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2603.15427(2026-03-16 제출, 2026-08-17 개정, IEEE TSE 2026) 초록에 행동 트리·상태 기계·HTN·BPMN 비교, 제어 구조·표현력·도구 지원 기준, 'no standard or widely accepted formalism' 구절, 현장에서 도메인 전문가가 미션을 정의하는 경우가 많다는 지적이 있다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. Moving AI MAPF 벤치마크 페이지에는 지도마다 무작위형 25개·균등형 25개의 시나리오(.scen)가 있다는 것은 있지만, 지도 수나 총 파일 수를 적은 문장은 없다. 검증자가 연 목록에는 지도 33개(도시 3, 게임 10, 창고 4, 무작위 4, 미로 5, 방 3, 빈 지도 4)가 있어 브리프의 '36개·1,800개'와 맞지 않는다. '창고 지도는 통로 배치를 격자로 추상화한 것' 문장도 페이지에서 찾지 못했다. 지도 수·총수·창고 추상화 서술은 빼고 구조(지도별 random 25·even 25의 .scen)만 남긴다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: sdformat.org에 'an XML format that describes objects and environments for robot simulators, visualization, and control', 로봇의 기구학·동역학·센서, 조명·지형·OpenStreetMap 도로·모델, 물리, Gazebo 기원, Apache 2.0, libsdformat 16.0.0이 있다. OSRF 관리 여부는 페이지 하단 저작권 표기(©2020 OSRF) 기준이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LIF 저장소 README에 1.0.0(2023-09), VDMA, 'initial transfer of a track layout to a central (third-party) master control system', VDA5050의 영향, 비구속적 접근이라는 면책, 간선·노드·스테이션이 있다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(종합 추정): 근거 finding f2·f3·f8·f9·f10·f12·f19·f20이 모두 유지됐다. 시나리오 인스턴스 버전 관리 규칙이 없다는 것은 부재 진술이므로 '확인한 자료에서 찾지 못했다'는 표현을 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(종합 추정): 핵심 질문에 대한 답이다. 인용한 f18은 강등됐지만 f22는 .scen 라이브러리의 존재만 쓰고 수치는 쓰지 않으므로 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(종합 추정): 3절 근거이며, 근거 finding f2·f12·f13·f17·f18의 강등 뒤에도 논지가 선다. f18의 수치는 쓰지 않는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(종합 추정): 9절 직접 범위다. '버전 있는 시나리오 모델'은 출처가 아니라 대상 페이지 1절 리스트업 문장에 기댄다. f21이 인스턴스 버전 관리 근거를 찾지 못했다고 했으므로 이 부분은 목표로 서술해야 한다(required_fixes)."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(종합 추정): 분류 원문 19장 기준의 연계 대상 구분(물리·센서 엔진과 로봇 기구학은 시뮬레이터·제조사, 컨베이어·작업셀 제어는 설비, 도로 교통 표준은 자율주행 분야)이 맞다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(연결 판단): 9. 채팅으로 시나리오 구성과 11. 채팅으로 실제 상황 시뮬레이션 재현의 연결은 분류 원문 C 주석('시나리오 구성과 실제 상황 재현은 33·36번')이 뒷받침한다. 35. 처리능력·규모·배치 설계는 근거 finding이 없다(required_fixes)."
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
      "ref-528·ref-1140(NIST ARIAC 문서 challenges·scenario)은 공통 규칙의 ref-008(NIST ARIAC)과 같은 대상이다. 개별 문서 페이지라 URL이 다를 수 있으므로 새 id를 유지하되 참고 자료에서 ref-008과의 관계를 밝히고, 같은 URL이면 퍼블리셔가 합친다",
      "용어집의 기존 항목 ariac, open-rmf, layout-interchange-format, fault-injection, linear-temporal-logic, behavior-tree, bpmn, hierarchical-task-network, mapf, level-alignment-fiducial, fleet-adapter, fleet-control-level과 겹치므로 4절은 새로 정의하지 않고 이 용어들에 연결한다",
      "f16 Groot2의 로그 재생과 f12 장애 주입은 36. 가상 시운전·실제 상황 재현, 54. 시험·형식 검증·벤치마크의 범위와 겹친다. 이 페이지에서는 시나리오 표현 측면만 다루고 해당 영역에는 연결만 한다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f18: [사실] → [추정]으로 강등한다. 지도 수 '36개'·총 '1,800개'와 '창고 지도는 통로 배치를 격자로 추상화' 서술은 빼고, 지도 수·총 파일 수는 '미확인'으로 둔다. 이유: ref-1147 페이지에 합계 문장이 없고, 검증자가 연 목록(33개)과도 맞지 않는다.",
    "f11: '우선순위가 높은 주문이 남아 있으면'을 '아직 발표되지 않은 긴급 주문이 남아 있으면'으로 고쳐 쓴다. 이유: ref-1140 원문은 발표 예정(to be announced) 긴급 주문을 조건으로 한다.",
    "5절: f4~f7(rmf_demos), f10(BEHAVIOR-1K), f11·f12(ARIAC)는 실제 현장 배치가 아니라 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오임을 각 사례에 밝힌다. 이유: 출처가 모두 시뮬레이션 자료다.",
    "5절: f7은 캠퍼스 월드(현장 유형 '실외')만 실외 사례로 쓴다. 제조·물류 월드는 영상 데모라 사례의 여섯 항목을 채울 근거가 없으므로 사례로 세우지 않고 6절·7절에서 언급만 한다. 이유: 한 finding에 두 현장 유형이 섞여 있다.",
    "5절: f10(가정)은 활동이 일상 가정 활동이라서 '가정'으로 분류했고, 장면에는 정원·식당·사무실도 들어 있음을 밝힌다. 이유: ref-971 초록의 장면 구성.",
    "5절: 물류창고는 현장 사례를 찾지 못했음을 밝힌다. f18(격자 창고 지도, 강등)과 f20(레이아웃 교환 형식)은 물류창고 적용 사례로 쓰지 말고 7절에서 다룬다. 이유: 현장 유형을 밝힌 적용 사례가 아니다.",
    "f16: 본문에서 [추정]에 '벤더 주장'을 병기하고, 출처가 제품 페이지(ref-1145)뿐임을 유지한다. 이유: 독립 확인이 없는 벤더 기능 주장이다.",
    "9절(f24): '버전 있는 시나리오 모델'은 ROP가 맡을 목표로 서술하고, 인스턴스 버전 관리 방식을 공개 자료에서 찾지 못했다는 f21을 함께 밝힌다. 이유: 근거는 페이지 1절 리스트업뿐이고 출처 근거가 없다.",
    "10절(f26): 35. 처리능력·규모·배치 설계 연결은 근거 finding이 없으므로 넣지 않는다. 9. 채팅으로 시나리오 구성·11. 채팅으로 실제 상황 시뮬레이션 재현 연결은 분류 원문 C 주석(2절 원문 주석)을 근거로 든다. 이유: 브리프 밖 연결을 막는다.",
    "10절: 언어 모델 기반 생성(f14·f15)은 L. AI·학습 기술 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 9. 채팅으로 시나리오 구성 양쪽에 연결하고, 시나리오가 34. 시뮬레이션·예측용 디지털 트윈이 실행할 '가정한 미래'의 입력임을 18. 실시간 세계 상태·데이터 일관성과 구분해 쓴다. 이유: 공통 규칙 5·6.",
    "4절: 장애 주입·선형 시간 논리·행동 트리·BPMN·계층적 작업 네트워크·레이아웃 교환 형식·Open-RMF·ARIAC는 기존 용어집 항목에 연결하고, 새 용어 등록은 glossary_candidates 4건(오픈시나리오, 행동 영역 정의 언어, 시뮬레이션 기술 형식, 반증 기반 시험)으로 한정한다. 이유: 용어집 중복 방지.",
    "참고 자료: ref-528·ref-1140 각주는 새 id를 쓰되 NIST ARIAC 참고문헌 ref-008과 같은 경진대회의 개별 문서 페이지임을 밝힌다. 이유: 공통 규칙 6절 참고문헌 id 대응.",
    "11절: 기존 oq-131·oq-135는 해결로 바꾸지 않고 열림으로 둔다. open_questions_new 4건을 싣는다. 이유: 해결 근거 finding이 없다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 25건, 미확인 1건, 교차 확인 0건. 강등: f18 사실 → 추정(MAPF 벤치마크 지도 수·총 시나리오 수가 출처 페이지에 없고, 검증자가 연 목록 33개와 맞지 않음). 원문 미열람 출처: 없음(15건 모두 검증자가 다시 열어 확인했다. 논문 6건은 초록 페이지 기준이고, Holodeck은 HTML 본문도 확인했다). 주의: 적용 사례(상업 시설·병원·실외·가정·제조 공장)는 모두 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오이며 실제 현장 배치 사례가 아니다. 물류창고 현장 사례와 국내 자료는 찾지 못했다. 3절(왜 중요한가)과 9절(책임 경계)은 종합 추정(f23·f24·f25)이고 모든 사실 주장이 단일 출처여서 신뢰도는 low다. Groot2 기능(f16)은 벤더 주장이다. oq-131·oq-135는 해결되지 않았다. 검증 검색 0회(열람만 사용).",
  "retry_reason": null
}
```

### runs/2026-09-30-12/pages.json

```json
{
  "run_id": "2026-09-30-12",
  "outline": [
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1000,
      "summary": "고정된 시나리오 형식이 없으면 계획기 비교·예외 대응 시험 반복이 어렵고 시나리오 파일이 불어나며 도메인 전문가가 쓸 공통 형식도 없다. [추정][^ref-726][^ref-528][^ref-1141][^ref-116]",
      "planned_findings": [
        "f23",
        "f13",
        "f12",
        "f2",
        "f17",
        "f22"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "시나리오 기술 형식, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 확률적 언어와 반증 기반 시험, 장애 주입 선언, 미션 기술 형식, 활동 명세 언어를 정리한다. [사실][^ref-1141][^ref-1135][^ref-528][^ref-116]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f10",
        "f12",
        "f17",
        "f21"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2400,
      "summary": "상업 시설·병원·실외·가정·제조 공장 다섯 사례를 공개 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오로 정리하고, 물류창고 현장 사례는 찾지 못했음을 밝힌다. [사실][^ref-104][^ref-971][^ref-1140]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f10",
        "f11",
        "f12"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1400,
      "summary": "확률적 시나리오 언어, 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 편집기, 언어 모델 기반 환경 생성의 다섯 접근을 정리한다. [의견]",
      "planned_findings": [
        "f1",
        "f3",
        "f8",
        "f9",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f21"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1400,
      "summary": "OpenSCENARIO XML·SDFormat·Open-RMF rmf_demos·traffic-editor·LIF·BEHAVIOR-1K·ARIAC·MAPF 벤치마크·Arena·Groot2를 이 영역과의 관계로 표에 정리한다. [추정][^ref-1141][^ref-104][^ref-1147]",
      "planned_findings": [
        "f2",
        "f3",
        "f4",
        "f7",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f16",
        "f18",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "Scenic 3.0, BEHAVIOR-1K, Arena-Bench, Arena 4.0, Holodeck, 미션 기술 형식 비교 연구 6건을 요약한다. [사실][^ref-1135][^ref-971][^ref-116]",
      "planned_findings": [
        "f1",
        "f10",
        "f13",
        "f14",
        "f15",
        "f17"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1000,
      "summary": "ROP는 시나리오 모델·예제 라이브러리·편집기·형식 변환을 맡고, 물리 엔진·로봇 모델·설비 제어·도로 교통 표준은 연계 대상으로 둔다. 시나리오 판 관리는 목표다. [추정][^ref-104][^ref-1148][^ref-528]",
      "planned_findings": [
        "f21",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1500,
      "summary": "9. 채팅으로 시나리오 구성·11. 채팅으로 실제 상황 시뮬레이션 재현, 34·36 설계·시뮬레이션 영역, 공간·사람·설비·작업 영역, 44 언어 모델 계획, 54 벤치마크, 62~66 현장 유형 영역과 연결한다. [추정][^ref-104][^ref-1143]",
      "planned_findings": [
        "f26"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "기존 oq-131·oq-135는 열림으로 두고 시나리오 형식 조합, 인스턴스 버전 관리, 설비 장애 일반화, 국내 예제 라이브러리 질문 4건을 새로 올린다.",
      "planned_findings": [
        "f4",
        "f12",
        "f21"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,795자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,571자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"6. 대표 접근법과 기술\" 절(1,360자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"4. 핵심 개념과 용어\" 절(1,249자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"8. 대표 연구와 자료\" 절(951자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"11. 열린 질문\" 절(919자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area33-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"3. 왜 중요한가\" 절(886자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 33. 시나리오 모델·편집 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건), 1차 조건부 승인 수정 13건 반영(MAPF 벤치마크 수치 주장 강등 등) | run 2026-09-30-12",
  "index_updates": {
    "home_recent": "2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성(시나리오 형식·예제 라이브러리·편집기, 상업 시설·병원·실외·가정·제조 공장 시뮬레이션 사례)",
    "category_recent": "2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성(OpenSCENARIO·Open-RMF rmf_demos·ARIAC·BEHAVIOR-1K 등 15개 출처, 신뢰도 low)",
    "area_recent": "2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성, 열린 질문 4건 추가(실행 2026-09-30-12)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "asam-openscenario",
      "term_ko": "오픈시나리오",
      "term_en": "ASAM OpenSCENARIO",
      "definition": "ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다.",
      "description": "XML 판(2026-05-19 기준 1.4.0)은 예측 가능한 정밀 시나리오를, DSL 은 대규모 검증을 겨냥한다. 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO 에는 동적 내용만 담는다.",
      "related_areas": [
        33,
        34,
        54
      ],
      "sources": [
        "ref-1141"
      ]
    },
    {
      "action": "new",
      "slug": "behavior-domain-definition-language",
      "term_ko": "행동 영역 정의 언어",
      "term_en": "Behavior Domain Definition Language (BDDL)",
      "definition": "BEHAVIOR 벤치마크가 일상 가정 활동을 형식 명세하는 데 쓰는 도메인 특화 언어다.",
      "description": "BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 OmniGibson 시뮬레이터에 구현했다.",
      "related_areas": [
        33,
        65
      ],
      "sources": [
        "ref-971"
      ]
    },
    {
      "action": "new",
      "slug": "simulation-description-format",
      "term_ko": "시뮬레이션 기술 형식",
      "term_en": "Simulation Description Format (SDFormat)",
      "definition": "Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다.",
      "description": "로봇의 기구학·동역학·센서와 조명·지형·OpenStreetMap 도로·3D 모델 같은 환경을 기술하며 Apache 2.0 으로 공개된다.",
      "related_areas": [
        33,
        34
      ],
      "sources": [
        "ref-1148"
      ]
    },
    {
      "action": "new",
      "slug": "falsification",
      "term_ko": "반증 기반 시험",
      "term_en": "Falsification",
      "definition": "시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다.",
      "description": "확률적 시나리오 언어 Scenic 3.0 은 3차원 기하·가시성 판정·LTL 시간 요구를 더해 반증 기반 시험에 쓸 수 있게 했다.",
      "related_areas": [
        33,
        54
      ],
      "sources": [
        "ref-1135"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1135",
      "org": "Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv)",
      "title": "3D Environment Modeling for Falsification and Beyond with Scenic 3.0",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.03325",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "확률적 시나리오 언어 Scenic 의 3.0 판. 3D 기하, 가림 고려 가시성, LTL 시간 요구를 더해 반증 기반 시험에 쓴다(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open-RMF (open-rmf/rmf_demos)",
      "title": "rmf_demos — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "호텔·사무실·공항 터미널·클리닉·캠퍼스·제조·물류 데모 월드와 작업 명령(dispatch_*)으로 구성된 Open-RMF 예제 시나리오 모음.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics (osrf/ros2multirobotbook)",
      "title": "Programming Multiple Robots with ROS 2 — Traffic Editor",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "시설 지도에 벽·문·승강기·차선·웨이포인트 속성을 주석해 .building.yaml 로 저장하고 시뮬레이션 월드를 생성하는 GUI 편집기 설명.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-971",
      "org": "Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv)",
      "title": "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09227",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BDDL 로 명세한 일상 가정 활동 1,000개, 장면 50개, 객체 9,000개 이상을 OmniGibson 에 구현한 벤치마크(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "컨베이어·전압 시험기·진공 그리퍼 고장과 긴급 주문의 네 민첩성 과제와 발동 매개변수 설명. 참고문헌 ref-008(NIST ARIAC)과 같은 경진대회의 개별 문서 페이지다.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1140",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Scenario",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립 작업, 주문과 우선순위, 품질 허용치 설명. 참고문헌 ref-008(NIST ARIAC)과 같은 경진대회의 개별 문서 페이지다.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1141",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO® XML",
      "published": null,
      "url": "https://www.asam.net/standards/detail/openscenario-xml/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "주행·교통 시뮬레이터의 동적 내용을 기술하는 XML 표준의 공식 소개. 1.4.0 판(2026-05-19), 카탈로그·매개변수화, OpenDRIVE·DSL 과의 관계.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-726",
      "org": "Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv)",
      "title": "Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments",
      "published": "2022-06",
      "url": "https://arxiv.org/abs/2206.05728",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "동적 환경 시나리오·월드 생성 도구와 평가 지표로 주행 계획기를 비교하는 벤치마크 모음(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1143",
      "org": "Shcherbyna, V. 외 (arXiv)",
      "title": "Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.12471",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM·확산 모델로 텍스트·2D 평면 배치에서 사람 중심 주행 환경을 생성하는 ROS 2 플랫폼(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-815",
      "org": "Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv)",
      "title": "Holodeck: Language Guided Generation of 3D Embodied AI Environments",
      "published": "2023-12",
      "url": "https://arxiv.org/abs/2312.09067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GPT-4 와 공간 관계 제약 최적화로 텍스트에서 상호작용 가능한 3D 환경을 생성(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1145",
      "org": "BehaviorTree.CPP 프로젝트 (behaviortree.dev)",
      "title": "Groot2",
      "published": null,
      "url": "https://www.behaviortree.dev/groot/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "행동 트리 편집·모니터링·로그 재생 도구 Groot2 의 기능과 무료·PRO 판 차이를 소개하는 제품 페이지.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv)",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "행동 트리·상태 기계·HTN·BPMN 을 미션 기술 형식으로 비교한 연구(초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1147",
      "org": "Moving AI Lab (Sturtevant 외)",
      "title": "MAPF Benchmarks",
      "published": null,
      "url": "https://movingai.com/benchmarks/mapf/index.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "격자 지도마다 무작위형 25개·균등형 25개의 .scen 시나리오 파일을 공개한 다중 에이전트 경로 찾기 벤치마크. 지도 수·총 파일 수는 미확인.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1148",
      "org": "Open Source Robotics Foundation",
      "title": "SDFormat (Simulation Description Format)",
      "published": null,
      "url": "http://sdformat.org/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "로봇 시뮬레이터·시각화·제어용으로 로봇과 환경을 기술하는 XML 형식의 공식 사이트.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF)",
      "title": "Layout Interchange Format (LIF) — README",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "무인운반차 통합업체가 주행 레이아웃을 제3자 상위 관제에 넘기는 VDMA 교환 형식 1.0.0 저장소 README.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가?",
      "areas": [
        33,
        34
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가?",
      "areas": [
        33,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가?",
      "areas": [
        33,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가?",
      "areas": [
        33,
        65
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "제조 공장",
      "item": "완료·인계",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    }
  ],
  "standards_updates": [
    {
      "name": "ASAM OpenSCENARIO XML (1.4.0)",
      "kind": "표준",
      "org": "ASAM e.V.",
      "url": "https://www.asam.net/standards/detail/openscenario-xml/",
      "related_areas": [
        33,
        34,
        54
      ],
      "summary": "주행·교통 시뮬레이터의 동적 내용(여러 개체의 동기화된 기동)을 .xosc XML 로 기술하고 카탈로그·매개변수화로 재사용하는 표준. 2026-05-19 에 1.4.0 판이 나왔고 도로망은 OpenDRIVE 에 맡긴다.",
      "ref_id": "ref-1141"
    },
    {
      "name": "SDFormat (Simulation Description Format)",
      "kind": "오픈소스",
      "org": "Open Source Robotics Foundation",
      "url": "http://sdformat.org/",
      "related_areas": [
        33,
        34
      ],
      "summary": "로봇(기구학·동역학·센서)과 환경(조명·지형·도로·3D 모델), 물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식. Gazebo 에서 시작했고 Apache 2.0 으로 공개된다.",
      "ref_id": "ref-1148"
    },
    {
      "name": "BEHAVIOR-1K (BDDL 활동 명세·OmniGibson)",
      "kind": "평가 프로그램",
      "org": "Stanford 등 (Li, C. 외)",
      "url": "https://arxiv.org/abs/2403.09227",
      "related_areas": [
        33,
        54,
        65
      ],
      "summary": "설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 장면 50개·객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크.",
      "ref_id": "ref-971"
    },
    {
      "name": "Moving AI MAPF 벤치마크",
      "kind": "평가 프로그램",
      "org": "Moving AI Lab (Sturtevant 외)",
      "url": "https://movingai.com/benchmarks/mapf/index.html",
      "related_areas": [
        27,
        33,
        54
      ],
      "summary": "격자 지도마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 공개한 다중 에이전트 경로 찾기 벤치마크. 지도 수·총 파일 수는 미확인.",
      "ref_id": "ref-1147"
    },
    {
      "name": "Arena-Bench",
      "kind": "평가 프로그램",
      "org": "Kästner, L. 외 (RA-L 2022)",
      "url": "https://arxiv.org/abs/2206.05728",
      "related_areas": [
        33,
        54
      ],
      "summary": "동적 환경의 시나리오·월드 생성 도구와 평가 지표로 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오에서 비교하는 벤치마크 모음.",
      "ref_id": "ref-726"
    }
  ],
  "additional_research_requests": [
    "5절 물류창고 사례: 물류창고 현장(입고~반품 흐름 가운데 어느 단계든)의 시나리오 예제·템플릿을 공개한 자료와 국내 자료가 필요하다. 이번 브리프에는 현장 사례가 없어 물류창고 사례를 세우지 못했다.",
    "7절 Moving AI MAPF 벤치마크: 지도 수와 총 시나리오 파일 수를 출처 페이지에서 직접 확인해야 한다. 브리프(36개·1,800개)와 검증자가 연 목록(33개)이 맞지 않아 '미확인'으로 두었다.",
    "5절 상업 시설·병원·실외 사례의 완료·인계·예외·성과 칸: Open-RMF 작업이 완료로 인정되는 조건과 실패 처리를 rmf_demos 시나리오 단위로 기술한 자료가 있으면 칸을 채울 수 있다.",
    "5절 제조 공장 사례 제약 칸: ARIAC 셀 전압 허용치(±0.2 V) 같은 품질 제약은 발견 사항 본문에 없어 쓰지 않았다. 다음 조사에서 claim 으로 확인하면 제약 칸에 넣을 수 있다.",
    "4절 BDDL: 활동을 초기 조건·목표 조건 쌍으로 정의한다는 구조와 Scenic 의 표본 추출 방식은 검색 요약에만 있어 쓰지 않았다. 원문 확인이 필요하다.",
    "11절 oq-135: 시나리오 구성 시 되물을 항목의 표준 질문 목록은 이번 조사에서 검색하지 못했다. oq-131 도 공개 변환 형식을 찾지 못했다.",
    "다음 실행 반영 후보(브리프 제안): 9. 채팅으로 시나리오 구성 페이지에 Arena 4.0·Holodeck(ref-1143·ref-815), 36. 가상 시운전·실제 상황 재현 페이지에 ARIAC 장애 주입·Groot2 로그 재생(ref-528·ref-1145, 벤더 주장)을 반영한다."
  ],
  "fixes_applied": [
    "f18 강등 — 7절 MAPF 벤치마크 행을 [추정]으로 쓰고 지도 수·총 파일 수를 '미확인'으로 두었으며 '36개·1,800개'와 창고 지도 추상화 서술을 넣지 않았다(reference_updates 의 ref-1147 요약에서도 '36개' 표현을 뺐다).",
    "f11 문구 수정 — 5절 제조 공장 사례의 완료·인계 칸을 '아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 주문 완료로 바뀌지 않는다'로 고쳐 썼다.",
    "5절 시뮬레이션 명시 — 도입 문장과 각 사례 제목·서술에 시뮬레이션 예제 월드(rmf_demos)·벤치마크(BEHAVIOR-1K)·경진대회 시나리오(ARIAC)이며 실제 현장 배치가 아님을 밝혔다.",
    "f7 분리 — 캠퍼스 월드만 '실외' 사례로 세우고, 제조·물류 월드는 사례로 쓰지 않고 7절 rmf_demos 행에서 영상 데모로만 언급했다.",
    "f10 가정 분류 — 가정 사례 서술에 활동이 일상 가정 활동이라 '가정'으로 분류했고 장면에 정원·식당·사무실도 들어 있음을 밝혔다.",
    "물류창고 — 5절 끝에 물류창고 현장 사례를 찾지 못했다고 밝히고, MAPF 시나리오 파일(f18)과 LIF(f20)는 적용 사례로 쓰지 않고 7절에서만 다뤘다.",
    "f16 — 6절·7절·10절에서 Groot2 기능을 '[추정] 벤더 주장' 으로 병기하고 6절에 출처가 제품 페이지(ref-1145)뿐임을 적었다.",
    "9절 f24 — '버전 있는 시나리오 모델'을 1절 리스트업이 정한 목표로 서술하고, 개별 시나리오 인스턴스 버전 관리 방식을 공개 자료에서 찾지 못했다는 f21 을 함께 밝혔다.",
    "10절 f26 — 35. 처리능력·규모·배치 설계 연결은 넣지 않았고(related_areas 에서도 제외), 9. 채팅으로 시나리오 구성·11. 채팅으로 실제 상황 시뮬레이션 재현 연결은 2절 원문 주석을 근거로 들었다.",
    "10절 교차 규칙 — 언어 모델 기반 생성(f14·f15)을 44. 로봇 기반 모델·언어 모델 계획과 9. 채팅으로 시나리오 구성 양쪽에 연결했고, 시나리오가 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력임을 18. 실시간 세계 상태·데이터 일관성과 구분하는 항목을 두었다.",
    "4절 용어 — 장애 주입·선형 시간 논리·행동 트리·BPMN·계층적 작업 네트워크·ARIAC 는 4절에서, 레이아웃 교환 형식·Open-RMF 는 7절에서 기존 용어집 항목에 링크했고, glossary_updates 는 오픈시나리오·행동 영역 정의 언어·시뮬레이션 기술 형식·반증 기반 시험 4건으로 한정했다.",
    "참고 자료 ref-528·ref-1140 — 새 id 를 그대로 쓰고, 7절 ARIAC 행과 reference_updates 요약에 NIST ARIAC 참고문헌 ref-008 과 같은 경진대회의 개별 문서 페이지임을 밝혔다(ref-008 링크 포함).",
    "11절 — oq-131·oq-135 는 '열림' 그대로 두고, open_questions_new 4건을 11절에 싣고 open_question_updates 에 new 4건으로 냈다.",
    "분량 초과 자동 분리: 33. 시나리오 모델·편집 본문 12,268자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,610자"
  ]
}
```

### runs/2026-09-30-12/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area33-s7.md (1,795자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area33-s10.md (1,571자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area33-s6.md (1,360자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area33-s4.md (1,249자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area33-s8.md (951자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area33-s11.md (919자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area33-s3.md (886자)
```

### runs/2026-09-30-12/pages/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [시나리오 형식, OpenSCENARIO, Open-RMF, 장애 주입, 시나리오 라이브러리, 미션 기술 형식]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1135, ref-104, ref-079, ref-971, ref-528, ref-1140, ref-1141, ref-726, ref-1143, ref-815, ref-1145, ref-116, ref-1147, ref-1148, ref-046]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1147][^ref-528][^ref-1141][^ref-116]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 왜 중요한가](../../topics/2026/2026-09-30-area33-s3.md)에 있다.

## 4. 핵심 개념과 용어

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [사실][^ref-1141][^ref-1135][^ref-528]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 다섯 사례는 모두 실제 현장 배치가 아니라 공개된 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오를 여섯 항목으로 정리한 것이며, 이 영역에서는 각 시나리오가 무엇을 어떤 단위로 담았는지를 본다. [사실][^ref-104][^ref-971][^ref-1140]

**현장 유형:** 상업 시설

**사례:** Open-RMF 예제 호텔·공항 터미널 월드의 다중 플릿 순찰·청소 시나리오(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 월드를 띄운 뒤 dispatch_clean·dispatch_patrol 같은 작업 명령을 따로 넣으면 작업이 생긴다. [사실][^ref-104] |
| 작업 대상 | 호텔 월드의 로비와 객실 2개 층 공간을 순찰(loop)·청소한다(예제 명령은 로비 청소). [사실][^ref-104] |
| 수행 자원 | 호텔 월드에는 로봇 플릿 3개(로봇 4대), 승강기 2대, 여러 문이 있고, 디스패처가 [플릿 어댑터](../../glossary/fleet-adapter.md)들 사이의 작업 입찰을 조율한다. [사실][^ref-104] |
| 제약 | 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에 선택적으로 군중 시뮬레이션과 사람이 모는 읽기 전용(read_only) 카트를 더해 순찰·배송·청소를 실행한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

rmf_demos의 시나리오는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 작업을 명령으로 따로 넣는 구조다(2026-09-30 확인). [사실][^ref-104] 호텔·공항 터미널 모두 시뮬레이션 예제 월드이며 실제 시설의 도입 사례가 아니다.

**현장 유형:** 병원

**사례:** Open-RMF 예제 클리닉 월드에서 두 층의 간호 스테이션 사이 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 순찰 명령(dispatch_patrol)으로 작업을 넣는다. 예제 명령은 1층과 2층의 간호 스테이션을 순찰 지점으로 지정한다. [사실][^ref-104] |
| 작업 대상 | 두 층에 걸친 간호 스테이션 사이의 순찰 경로(공간) [사실][^ref-104] |
| 수행 자원 | 역할이 다른 로봇 플릿 2개와 승강기 2대 [사실][^ref-104] |
| 제약 | 로봇이 승강기 2대가 있는 2개 층 시설에서 층을 오가며 순찰해야 한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

클리닉 월드는 병원형 시나리오 예제이며 실제 병원 배치 사례가 아니다. 층간 이동이 승강기를 거친다는 점에서 설비를 시나리오 요소로 담는 예가 된다. [사실][^ref-104]

**현장 유형:** 실외

**사례:** Open-RMF 예제 캠퍼스 월드의 배송 로봇 장거리 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 명령으로 장거리 순찰을 넣는다. [사실][^ref-104] |
| 작업 대상 | 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스 공간 [사실][^ref-104] |
| 수행 자원 | 여러 대의 배송 로봇 [사실][^ref-104] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

캠퍼스 월드는 실내 층 좌표 대신 지구 좌표로 공간을 주석한 실외 시나리오 예제다. [사실][^ref-104] 같은 예제 모음의 제조·물류 월드는 영상 데모뿐이라 사례로 세우지 않고 7절에서만 다룬다.

**현장 유형:** 가정

**사례:** BEHAVIOR-1K의 일상 가정 활동 라이브러리(벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고, 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상(강체·변형체·액체)을 OmniGibson 시뮬레이터에 구현했다. [사실][^ref-971] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 활동이 일상 가정 활동이라서 현장 유형을 '가정'으로 분류했으며, 장면에는 주택뿐 아니라 정원·식당·사무실도 들어 있다. [사실][^ref-971] 실제 가정 배치가 아니라 시뮬레이션 벤치마크다.

**현장 유형:** 제조 공장

**사례:** NIST ARIAC 전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립과 장애 주입(경진대회 시나리오)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 키팅과 모듈 조립 두 작업을 주문으로 받는다. [사실][^ref-1140] |
| 작업 대상 | 배터리 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 조립하는 모듈 [사실][^ref-1140] |
| 수행 자원 | 시나리오에 컨베이어·전압 시험기·진공 그리퍼가 들어 있고, 각각을 고장 대상으로 선언할 수 있다. [사실][^ref-528] |
| 제약 | 해당 없음 |
| 완료·인계 | 아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않는다. [사실][^ref-1140] |
| 예외·성과 | 컨베이어 고장(시작 시각·지속 시간), 전압 시험기 고장(시작·지속·대상 시험기), 진공 그리퍼 파지 실패(도구·몇 번째 파지인지), 긴급 주문(시작 시각·주문 id) 네 과제를 매개변수로 선언해 시각이나 발생 횟수 조건으로 주입한다. [사실][^ref-528] |

ARIAC는 경진대회용 시뮬레이션 시나리오이며 실제 공장 사례가 아니다. 장애와 긴급 요청을 시나리오 파일 안의 선언으로 다룬다는 점이 이 영역의 참고점이다. [사실][^ref-528]

물류창고 현장의 시나리오 예제·템플릿 사례는 이번 조사에서 찾지 못했다. 경로 찾기 벤치마크의 시나리오 파일과 VDMA 레이아웃 교환 형식은 현장 사례가 아니므로 7절에서 다룬다. 국내 자료도 찾지 못했다.

## 6. 대표 접근법과 기술

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1141][^ref-104][^ref-971][^ref-528][^ref-1147]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md)에 있다.

## 8. 대표 연구와 자료

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-09-30-area33-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP는 시나리오 모델·현장 유형별 예제 라이브러리·편집기·형식 변환을 맡고, 물리·센서 시뮬레이션 엔진과 로봇 모델, 설비 제어, 도로 교통 시나리오 표준은 참조·변환해 묶는 연계 대상으로 두는 것으로 보인다. [추정][^ref-104][^ref-528][^ref-1148][^ref-1141]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 시나리오에 어떤 로봇을 어디에 둘지(로봇 구성)를 정하고 로봇 모델을 참조로 묶는다. [추정][^ref-104][^ref-1148] | 물리·센서 시뮬레이션 엔진과 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 시뮬레이터·로봇 제조사 쪽 연계 대상이다. [추정][^ref-1148] |
| 시설·설비 제어 | 승강기·문·컨베이어 같은 설비를 시나리오 요소로 선언하고 설비 장애를 시각·발생 조건으로 주입한다. [추정][^ref-104][^ref-528] | 컨베이어·작업셀 같은 설비 제어 자체는 설비 쪽 연계 대상이다. [추정][^ref-104][^ref-528] |
| 업종별 조건 | 도로 교통 시나리오 표준의 구조(정적·동적 분리, 매개변수화)를 참조 설계로 삼는다. [추정][^ref-1141] | 도로 교통 시나리오 표준(OpenSCENARIO·OpenDRIVE)은 자율주행 분야의 연계 대상이다. [추정][^ref-1141] |

ROP가 직접 맡을 범위는 네 가지로 보인다: 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 시나리오 모델, 현장 유형별 예제 라이브러리, 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택, 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환이다. [추정][^ref-104][^ref-528][^ref-079][^ref-1145][^ref-116][^ref-1148]

시나리오 모델에 판(버전)을 두는 것은 1절 리스트업이 정한 목표다. 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 공개 자료에서 찾지 못했으므로, 판 관리 규칙은 아직 근거 없이 설계해야 하는 부분이다. [추정][^ref-1141][^ref-046][^ref-104][^ref-079]

경계는 제품 전략에 따라 이동할 수 있다. 이종 제조사를 연결하는 ROP는 시뮬레이터·제조사·설비 쪽 기능을 직접 만들기보다 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. [추정][^ref-1148][^ref-104][^ref-528][^ref-1141] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1143]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-09-30-area33-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1140]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1141]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1145]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1147]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1148]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
```

### docs/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

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

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s7.md

```markdown
---
title: "33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-104, ref-079, ref-971, ref-528, ref-1140, ref-1141, ref-726, ref-1143, ref-1145, ref-1147, ref-1148, ref-046]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#7
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스

# 33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1141][^ref-104][^ref-971][^ref-528][^ref-1147]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1141][^ref-104][^ref-971][^ref-528][^ref-1147]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ASAM OpenSCENARIO XML 1.4.0 | 표준 | 주행·교통 시뮬레이터의 동적 내용을 .xosc 파일로 기술하고 카탈로그·매개변수화로 재사용하며, 도로망은 OpenDRIVE, 노면은 OpenCRG에 맡긴다. [사실][^ref-1141] | ASAM 공식 소개(1.4.0 판 2026-05-19) |
| SDFormat(Simulation Description Format) | 오픈소스 | 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo에서 시작했고 Open Source Robotics Foundation이 Apache 2.0으로 관리한다. [사실][^ref-1148] | 공식 사이트(2026-09-30 확인) |
| [Open-RMF](../../glossary/open-rmf.md) rmf_demos | 오픈소스 | 호텔·공항 터미널·클리닉·캠퍼스 예제 월드와 작업 명령으로 된 다중 플릿 시나리오 모음이다(5절). [사실][^ref-104] 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다. [사실][^ref-104] | README(2026-09-30 확인) |
| Open-RMF traffic-editor | 오픈소스 | 시설 지도에 벽·문·층·승강기·차선·웨이포인트를 주석해 .building.yaml로 저장하고 시뮬레이션 월드를 생성하는 편집기다. [사실][^ref-079] | ROS 2 다중 로봇 책(2026-09-30 확인) |
| [레이아웃 교환 형식](../../glossary/layout-interchange-format.md)(Layout Interchange Format, LIF) 1.0.0 | 표준 | VDMA가 정한 비구속적 교환 형식으로, 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰며 VDA 5050의 영향을 받았다. [사실][^ref-046] | VDMA 저장소 README(2023-09) |
| BEHAVIOR-1K·BDDL | 평가 프로그램 | 일상 가정 활동 1,000개를 BDDL로 명세하고 OmniGibson에 구현한 활동 라이브러리다(5절). [사실][^ref-971] | arXiv 2403.09227(2024-03) |
| [ARIAC](../../glossary/ariac.md) 시나리오·과제 문서 | 평가 프로그램 | 전기차 배터리 생산 시설 시나리오와 네 가지 민첩성 과제의 매개변수 선언을 담는다(5절). [사실][^ref-1140][^ref-528] 두 문서는 참고문헌 [ref-008](../../references/ref-008.md)(NIST ARIAC)과 같은 경진대회의 개별 문서 페이지다. | NIST ARIAC 문서(2026-09-30 확인) |
| Moving AI 연구실 [MAPF](../../glossary/mapf.md) 벤치마크 | 평가 프로그램 | 격자 지도마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 재사용 가능한 시나리오 라이브러리로 공개한다. 지도 수와 총 파일 수는 미확인이다. [추정][^ref-1147] | 벤치마크 페이지(2026-09-30 확인) |
| Arena-Bench·Arena 4.0 | 평가 프로그램 | 동적 환경의 시나리오·월드 생성 도구와 평가 지표로 주행 계획기를 비교하고(Arena-Bench, 2022), Arena 4.0(2024)은 언어 모델·확산 모델로 사람이 있는 주행 환경을 생성한다. [사실][^ref-726][^ref-1143] | arXiv 2206.05728, 2409.12471 |
| Groot2 | 벤더 도구 | 행동 트리를 끌어놓기로 편집하고 실행 로그를 재생하며 유료판에서 장애 주입을 제공한다고 밝힌다. [추정] 벤더 주장[^ref-1145] | 제품 페이지(2026-09-30 확인) |

표준·오픈소스 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1140]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1141]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1145]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-1147]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1148]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s10.md

```markdown
---
title: "33. 시나리오 모델·편집 — 다른 연구영역과의 연결"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-104, ref-079, ref-971, ref-528, ref-1140, ref-726, ref-1143, ref-815, ref-1145, ref-116, ref-1147, ref-1148, ref-046]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#10
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 다른 연구영역과의 연결

# 33. 시나리오 모델·편집 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1143]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1143]

- [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) — 2절 원문 주석대로 시나리오 구성 대화는 이 영역의 기능을 부르는 짝이며, 텍스트에서 환경을 생성하는 Arena 4.0·Holodeck 같은 언어 모델 기반 생성이 그 방법 후보다. [추정][^ref-1143][^ref-815]
- [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 2절 원문 주석대로 실제 상황 재현 대화는 이 영역과 36. 가상 시운전·실제 상황 재현의 기능을 부른다.
- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 시설 지도에 건물 요소를 주석해 시뮬레이션 월드로 바꾸는 편집기가 도면·지도와 시나리오의 접점이다. [추정][^ref-079]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 차선·웨이포인트·층 정렬과 LIF 레이아웃이 시나리오의 정적 환경을 이룬다. [추정][^ref-079][^ref-046]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 이 페이지의 시나리오는 가정한 미래를 실험하는 입력이며, 현재 상태를 표현하는 실시간 모델과 섞지 않는다(분류 원문 I. 설계·시뮬레이션 주석의 구분). [의견]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 공항 터미널 월드의 군중 시뮬레이션과 Arena 4.0의 사람이 있는 환경 생성이 사람 흐름을 시나리오에 넣는 예다. [추정][^ref-104][^ref-1143]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 호텔·클리닉 예제 월드는 승강기·문을 시나리오 요소로 담는다. [추정][^ref-104]
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — 행동 트리·상태 기계·HTN·BPMN 같은 미션 기술 형식 선택을 공유한다. [추정][^ref-116]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — .scen 시나리오 파일 라이브러리가 경로 찾기 알고리즘의 공통 시험 입력이다. [추정][^ref-1147]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 장애·긴급 주문을 시나리오에 선언하는 방식이 예외 복구 시험의 입력이 된다. [추정][^ref-528]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 시나리오는 이 영역이 실행할 가정한 미래의 입력이며, SDFormat 같은 시뮬레이터 형식으로 내보내진다. [추정][^ref-1148]
- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 2절 원문 주석의 짝이며, 실행 로그를 재생하는 편집기 기능(Groot2)은 재현 기능과 겹친다. 이 페이지는 시나리오 표현 측면만 다룬다. [추정] 벤더 주장[^ref-1145]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — L. AI·학습 기술 교차 규칙에 따라 언어 모델로 환경·시나리오를 생성하는 연구(Holodeck·Arena 4.0)를 양쪽에 연결한다. [추정][^ref-815][^ref-1143]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 반증 기반 시험(Scenic), 주행 벤치마크(Arena-Bench), 경로 찾기 벤치마크가 시나리오를 시험 입력으로 쓴다. [추정][^ref-1135][^ref-726][^ref-1147]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — ARIAC 배터리 생산 시설 시나리오(5절). [추정][^ref-1140][^ref-528]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — rmf_demos 클리닉 월드(5절). [추정][^ref-104]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — rmf_demos 호텔·공항 터미널 월드(5절). [추정][^ref-104]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — BEHAVIOR-1K 일상 가정 활동(5절). [추정][^ref-971]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — rmf_demos 캠퍼스 월드(5절). [추정][^ref-104]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1140]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12, https://arxiv.org/abs/2312.09067, 접근일 2026-09-30
[^ref-1145]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1147]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1148]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s6.md

```markdown
---
title: "33. 시나리오 모델·편집 — 대표 접근법과 기술"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-104, ref-079, ref-1141, ref-1143, ref-815, ref-1145, ref-116, ref-046]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#6
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 대표 접근법과 기술

# 33. 시나리오 모델·편집 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

### 확률적 시나리오 언어

Scenic은 자율 시스템·로봇의 환경을 확률적 프로그램으로 모델링하는 언어이며, 3.0 판(CAV 2023)은 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, LTL로 쓰는 시간 요구사항을 더해 반증 기반 시험에 쓸 수 있게 했다. [사실][^ref-1135]

### 정적 월드와 작업 명령의 분리

Open-RMF의 rmf_demos는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣고, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다. [사실][^ref-104] 자율주행 분야의 ASAM도 정적 도로망·노면과 동적 내용을 나누며, 대규모 검증용 OpenSCENARIO DSL과 예측 가능한 정밀 시나리오용 XML로 역할을 구분한다. [사실][^ref-1141] 한계로, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 있으나 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다. [추정][^ref-1141][^ref-046][^ref-104][^ref-079]

### 건물 주석 편집기

Open-RMF의 traffic-editor는 시설 지도 위에 벽, 문(여닫이·미닫이·양문), 층, 승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, [층 정렬 기준점](../../glossary/level-alignment-fiducial.md)을 그려 넣는 GUI 편집기다. [사실][^ref-079] 결과는 .building.yaml 파일로 저장되고 building_map_generator가 이를 물리 시뮬레이션 월드로 자동 생성한다. [사실][^ref-079]

### 미션 기술 형식과 편집기

Filippone 외(2026)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·HTN·BPMN을 제어 구조·표현력·도구 지원 측면에서 비교했다. [사실][^ref-116] 행동 트리 편집기 Groot2는 끌어놓기로 트리를 만들며 XML을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다. 출처는 제품 페이지뿐이다. [추정] 벤더 주장[^ref-1145]

### 언어 모델 기반 환경 생성

Arena 4.0(2024)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다. [사실][^ref-1143] Holodeck(CVPR 2024)은 GPT-4가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했다. [사실][^ref-815]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-1141]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12, https://arxiv.org/abs/2312.09067, 접근일 2026-09-30
[^ref-1145]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s4.md

```markdown
---
title: "33. 시나리오 모델·편집 — 핵심 개념과 용어"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-104, ref-079, ref-971, ref-528, ref-1141, ref-116, ref-1148, ref-046]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#4
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 핵심 개념과 용어

# 33. 시나리오 모델·편집 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [사실][^ref-1141][^ref-1135][^ref-528]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [사실][^ref-1141][^ref-1135][^ref-528]

- **시나리오 기술 형식(scenario description format)** — 시뮬레이터에 넣을 시나리오를 파일로 기술하는 형식이다. ASAM OpenSCENARIO XML은 주행·교통 시뮬레이터에서 차량·보행자 등 여러 개체의 동기화된 기동을 계층 구조의 XML 파일(.xosc)로 기술한다. [사실][^ref-1141]
- **정적 환경과 동적 내용의 분리** — ASAM은 도로망을 OpenDRIVE, 노면 형상을 OpenCRG로 따로 기술하고 OpenSCENARIO XML에는 그 위의 동적 내용만 담는다. [사실][^ref-1141] 확인한 다른 형식들도 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃)과 동적 내용(작업 명령, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하는 것으로 보인다. [추정][^ref-1148][^ref-079][^ref-046][^ref-104][^ref-528][^ref-971]
- **매개변수화·카탈로그(parameterization, catalog)** — 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수로 바꿔, 조건마다 시나리오 파일을 새로 만들지 않게 하는 방식이다. [사실][^ref-1141]
- **확률적 시나리오 언어와 반증 기반 시험(falsification)** — Scenic은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어이며, 3.0 판은 3차원 기하, 가림을 고려한 가시성 판정, [선형 시간 논리](../../glossary/linear-temporal-logic.md)(Linear Temporal Logic, LTL)로 쓰는 시간 요구사항을 더해 반증 기반 시험에 쓸 수 있게 했다. [사실][^ref-1135]
- **[장애 주입](../../glossary/fault-injection.md)(fault injection) 선언** — [ARIAC](../../glossary/ariac.md)는 컨베이어·전압 시험기·진공 그리퍼 고장과 긴급 주문을 시작 시각·지속 시간·몇 번째 파지인지 같은 매개변수로 시나리오에 선언한다. [사실][^ref-528]
- **미션 기술 형식(mission specification formalism)** — [행동 트리](../../glossary/behavior-tree.md)(Behavior Tree), 상태 기계, [계층적 작업 네트워크](../../glossary/hierarchical-task-network.md)(Hierarchical Task Network, HTN), [BPMN](../../glossary/bpmn.md)(Business Process Model and Notation)이 미션 기술 형식으로 비교되며, 단일·다중 로봇 미션을 명세하는 표준은 없다. [사실][^ref-116]
- **행동 영역 정의 언어(Behavior Domain Definition Language, BDDL)** — BEHAVIOR-1K가 일상 가정 활동 1,000개를 형식 명세하는 데 쓰는 언어다. [사실][^ref-971]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1141]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1148]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s8.md

```markdown
---
title: "33. 시나리오 모델·편집 — 대표 연구와 자료"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-971, ref-726, ref-1143, ref-815, ref-116]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#8
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 대표 연구와 자료

# 33. 시나리오 모델·편집 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

- Vin, E. 외, 3D Environment Modeling for Falsification and Beyond with Scenic 3.0(CAV 2023) — 확률적 시나리오 언어에 3차원 기하·가시성 판정·LTL 시간 요구를 더해 반증 기반 시험에 쓰게 했다. [사실][^ref-1135] 시나리오를 프로그램과 분포로 표현하는 접근의 예다. [의견]
- Li, C. 외, BEHAVIOR-1K(arXiv 2024, 예비판 CoRL 2022) — 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고 장면 50개·객체 9,000개 이상을 구현했다. [사실][^ref-971] 대규모 시나리오 라이브러리의 예다. [의견]
- Kästner, L. 외, Arena-Bench(RA-L 2022) — 동적 환경의 시나리오·월드 생성 도구와 평가 지표로 여러 로봇 플랫폼의 주행 계획기를 비교하고 실물 로봇 배치까지 보였다. [사실][^ref-726]
- Shcherbyna, V. 외, Arena 4.0(arXiv 2024) — 언어 모델과 확산 모델로 텍스트나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 사용자 연구에서 사용성·효율 개선을 보고했다. [사실][^ref-1143]
- Yang, Y. 외, Holodeck(CVPR 2024) — GPT-4와 공간 관계 제약 최적화로 텍스트에서 상호작용 가능한 3D 환경을 만들고, 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다. [사실][^ref-815]
- Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution(IEEE TSE, 2026) — 행동 트리·상태 기계·HTN·BPMN을 비교하고 미션 명세 표준이 없다고 지적했다. [사실][^ref-116]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12, https://arxiv.org/abs/2312.09067, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s11.md

```markdown
---
title: "33. 시나리오 모델·편집 — 열린 질문"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#11
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 열린 질문

# 33. 시나리오 모델·편집 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-131** (상태: 열림) 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가?
- **oq-135** (상태: 열림) 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가?
- (신규 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-12) 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가?
- (신규 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-12) 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가?
- (신규 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-12) ARIAC처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가?
- (신규 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-12) 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-12/pages/topics/2026/2026-09-30-area33-s3.md

```markdown
---
title: "33. 시나리오 모델·편집 — 왜 중요한가"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-104, ref-971, ref-528, ref-1141, ref-726, ref-1143, ref-815, ref-116, ref-1147]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#3
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 왜 중요한가

# 33. 시나리오 모델·편집 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1147][^ref-528][^ref-1141][^ref-116]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1147][^ref-528][^ref-1141][^ref-116]

비교의 기준은 고정된 시나리오다. Arena-Bench(2022)는 시나리오·월드 생성 도구와 평가 지표를 갖춰 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오에서 비교했다. [사실][^ref-726]

예외 대응도 시나리오에 선언해야 반복해서 시험할 수 있다. NIST ARIAC는 설비 고장과 긴급 주문을 매개변수로 선언해 시나리오에 주입한다(2026-09-30 확인). [사실][^ref-528] 조건별 파일이 불어나는 문제에는 매개변수화가 쓰인다. ASAM OpenSCENARIO XML(1.4.0 판, 2026-05-19)은 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화하게 한다. [사실][^ref-1141]

누가 시나리오를 쓰는가도 문제다. 단일·다중 로봇 미션을 명세하는 표준이나 널리 받아들여진 형식은 없고, 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다(2026년 비교 연구). [사실][^ref-116]

2절 핵심 질문에 대한 현재 답은 추정 단계다. 공개 형식은 자율주행(OpenSCENARIO), 가정 활동(BDDL), 시설 다중 로봇(Open-RMF 건물 파일과 작업 명령), 제조(ARIAC 과제 설정), 경로 찾기(MAPF .scen)처럼 분야별로 나뉘어 있고, 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식에 담는 공통 표준은 확인한 자료에서 찾지 못했다. [추정][^ref-1141][^ref-971][^ref-104][^ref-528][^ref-1147][^ref-116] 재사용은 매개변수화·카탈로그, 확률 분포 표본 추출, 현장 유형별 예제 월드, 대규모 활동·시나리오 라이브러리, 언어 모델 생성으로 이루어지는 것으로 보인다. [추정][^ref-1141][^ref-1135][^ref-104][^ref-971][^ref-1143][^ref-815]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1141]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1143]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12, https://arxiv.org/abs/2312.09067, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1147]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-12 | 33. 시나리오 모델·편집 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1074건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 293개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
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
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
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
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
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
- finops: 핀옵스 (FinOps)
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
- guidance-graph: 안내 그래프 (Guidance Graph)
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
- imitation-learning: 모방 학습 (Imitation Learning)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
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
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
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
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
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
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
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
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
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
- semantic-map: 의미 지도 (Semantic Map)
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
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
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
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [33] 에 걸린 2건 / 전체 228건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-135 [열림] 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? (영역 9, 33)
```
