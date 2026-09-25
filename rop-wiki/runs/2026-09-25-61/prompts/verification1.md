(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-61
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 24. 자산·소프트웨어 수명주기 관리 (F. 도입·검증·유지관리)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-25-61/target.json

```json
{
  "run_id": "2026-09-25-61",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 61,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 24,
    "area_name": "24. 자산·소프트웨어 수명주기 관리",
    "category": "F. 도입·검증·유지관리",
    "category_letter": "F"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=24"
}
```

### runs/2026-09-25-61/research.json

```json
{
  "run_id": "2026-09-25-61",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 24,
    "area_name": "24. 자산·소프트웨어 수명주기 관리",
    "category": "F. 도입·검증·유지관리"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(예지보전·상태 기반 정비, 배터리 건강 상태, 소프트웨어 명판, 패치 관리, 지도 버전)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음(상태 감시·고장 예측, 배터리 열화 인지 배정, OTA 배포·롤백, 관리형 노드)",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건, 정정 요청 0건)"
  ],
  "research_questions": [
    "제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]",
    "로봇 상호운용 규격(VDA 5050, MassRobotics AMR 상호운용 표준)은 펌웨어·소프트웨어·지도 버전과 배터리 건강 상태를 어떤 필드로 보고하며, 버전 호환성 규칙은 무엇인가? (섹션 4·6·7 겨냥)",
    "고장 예측·정비(상태 감시, 예지보전)와 자산 관리의 표준·대표 연구는 무엇인가(ISO 17359, ISO 55000, 산업용 로봇 상태 감시 검토 논문)? (섹션 3·7·8 겨냥)",
    "배터리 열화를 플릿 운영(작업 배정·충전)에 반영하는 접근은 무엇인가? (섹션 5·6 겨냥)",
    "로봇 소프트웨어 배포·복구(무선 업데이트, 롤백, 관리형 노드, 배포판 지원 종료)와 패치 관리 표준은 무엇인가? (섹션 6·7 겨냥)",
    "펌웨어·설정 변경이 안전 재평가·규제상 '실질적 변경'에 해당하는 조건은 무엇이며 한국 인증 제도는 어떻게 다루는가? (섹션 3·9·11 겨냥, 한국 자료 우선)",
    "ROP 가 직접 맡을 수명주기 관리 범위와 제조사·설비에 맡길 범위는 어떻게 나뉘는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 은 지도를 지도 식별자(mapId)와 지도 버전(mapVersion)의 조합으로 식별하고, 즉시 동작 downloadMap·enableMap·deleteMap 으로 지도 내려받기·활성화·삭제를 지시하며, 같은 mapId 에서는 한 번에 한 버전만 활성화되게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-749"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.3.1 지도 배포: 지도는 mapId 와 mapVersion 조합으로 식별, 지도 서버→로봇 전송은 플릿 제어가 시작하는 pull 방식. 6.3.2: \"There shall only be one version of maps with the same mapId enabled at a time.\" (VDA 5050 3.0.0, 공식 저장소 main)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "VDA 5050 은 의미적 버전 체계를 써서 주 버전 변경은 새 필수 필드 도입 같은 호환성을 깨는 변경, 부 버전은 기능 추가, 수 버전은 작은 수정으로 규정하고, MQTT 토픽 경로에 주 버전(v3 등)을 넣는다.",
      "tag": "사실",
      "source_ids": [
        "ref-749"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1절: 주 버전(x.0.0)은 breaking changes(새 비선택 필드 도입 등), 부 버전은 새 기능, 수 버전은 오탈자 등 수정. 4.2절 토픽 예: vda5050/v3/KIT/0001/order (3.0.0 판)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 에서 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 오류 유형 UNSUPPORTED_PARAMETER 를 수준 CRITICAL 로 보고하도록 되어 있어, 판 차이로 생긴 미지원 기능이 실행 시점 오류로 드러난다.",
      "tag": "사실",
      "source_ids": [
        "ref-749"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.1.4.2: 로봇이 쓸 수 없는 선택 필드가 있는 주문을 받으면 'UNSUPPORTED_PARAMETER' 오류를 'CRITICAL' 수준으로 보고. 판 불일치 처리 절차 자체는 명세에 명시되지 않음",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 팩트시트 스키마는 mobileRobotConfiguration.versions 배열에 로봇에서 도는 하드웨어·소프트웨어 버전(예: softwareVersion)을 키–값으로 담고, batteryCharging 블록에 임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간을 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "versions: \"various hardware and software versions running on the mobile robot\"(예 softwareVersion, cameraVersion, plcSoftChecksum). batteryCharging: criticalLowChargingLevel, minimumDesiredChargingLevel, maximumDesiredChargingLevel, minimumChargingTime",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 상태(state) 스키마는 전원 정보로 충전 상태(stateOfCharge), 원래 용량 대비 배터리 상태(batteryHealth), 충전 중 여부, 현재 충전 상태로 갈 수 있는 추정 거리(range)를, 지도 정보로 mapId·mapVersion·mapStatus 를 로봇이 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-750"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "powerSupply: stateOfCharge(0~100%), batteryVoltage, batteryCurrent, batteryHealth(0~100%), charging, range(\"Estimated reach with current State of Charge in meter\"). maps: mapId, mapVersion, mapDescriptor, mapStatus(ENABLED/DISABLED) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "MassRobotics AMR 상호운용 표준 JSON 스키마는 제조사명·모델·일련번호, 배터리 잔량 비율, 남은 가동 시간, 오류 코드 목록을 담지만 소프트웨어·펌웨어 버전 필드는 명시적으로 두지 않은 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "identityReport/statusReport: manufacturerName, robotModel, robotSerialNumber, batteryPercentage, remainingRunTime, maxRunTime, errorCodes(\"omitted for normal operation\"), supportVendorName. 버전 필드는 스키마 요약에서 찾지 못함(부재는 요약 판독 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 은 소프트웨어 버전을 팩트시트에, 지도 버전을 상태 메시지에 두지만 MassRobotics 스키마는 버전 필드가 없어, 여러 규격이 섞인 플릿에서는 ROP 가 로봇별 버전 목록을 별도로 유지해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-750",
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f5·f6 의 스키마 비교에서 도출한 추정. 실제 다규격 플릿에서 버전 목록을 관리하는 공개 사례는 확인하지 못함",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "ROS 2 관리형 노드 설계는 미구성·비활성·활성·종료의 네 주 상태와 구성·활성화·비활성화·정리·종료 전이를 두어, 실행 전에 구성 요소가 올바로 초기화됐는지 확인하고 실행 중 노드를 교체·재시작할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-751"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A managed life cycle for nodes allows greater control over the state of ROS system.\" 주 상태 Unconfigured·Inactive·Active·Finalized, 전이 상태 Configuring·CleaningUp·Activating·Deactivating·ShuttingDown·ErrorProcessing (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "ROS 2 배포판 지원 정책(REP 2000)에 따르면 장기 지원판은 5년, 비장기 지원판은 1.5년 지원되며, Humble 은 2022-05~2027-05, Jazzy 는 2024-05~2029-05, Kilted 는 2025-05~2026-11 이 지원 기간이다.",
      "tag": "사실",
      "source_ids": [
        "ref-752"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"LTS releases come with 5 years of standard support\", 비LTS 1.5년(다음 LTS 와 6개월 겹침). Humble EOL 2027-05, Jazzy EOL 2029-05, Kilted EOL 2026-11 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "rmf_simulation 저장소는 지원 대상으로 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 적어, 오케스트레이션 검증용 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리 대상이다.",
      "tag": "사실",
      "source_ids": [
        "ref-668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Gazebo Classic 11(2025년 1월 지원 종료)과 Gazebo Fortress 지원 명시 (재인용: 2026-09-25-56)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "IDTA 02007 소프트웨어 명판(Nameplate for Software in Manufacturing) 서브모델은 업데이트·패치 관리·라이선스 관리·감사를 위해 소프트웨어 제품과 설치 인스턴스 정보를 통일된 형태로 표현하며, 버전(주·부·개정·빌드), 배포일·빌드일·설치일, 설치 경로·체크섬, 설치된 버전과 구성 경로 같은 속성을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-753"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목적: \"a uniform representation\" 으로 updates, patch management, license management, audits 지원. 제품 정의와 설치 인스턴스 상태를 함께 기술 (IDTA 02007-1-0, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "ISO 17359:2018 은 기계의 상태 감시 프로그램을 세울 때의 일반 절차 지침을 주며, 진동·온도·유량·오염·전력·속도 같은 변수를 쓰고 상태 감시·진단 표준군의 상위 문서 역할을 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-754"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 17359:2018 gives guidelines for the general procedures ... setting up a condition monitoring programme for machines (검색 요약 범위)",
      "as_of": "2018",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "ISO 55000:2024(제2판, 2024년 7월, ISO/TC 251)는 자산 관리의 개요·원칙·용어를 정하고 ISO 55000:2014 를 대체하며, 자산에 하드웨어·소프트웨어·설비를 포함하고 수명주기 단계별로 자산의 필요와 성능을 평가하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-755"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 55000:2024 Asset management — Vocabulary, overview and principles. 제2판 2024-07, 2014 판 대체. 원칙: 가치, 정렬, 리더십 등 (검색 요약 범위)",
      "as_of": "2024-07",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "Lei 외(2025)의 검토 논문은 산업용 로봇의 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 상태 감시·고장 진단 기술을 상태 기반 정비 구현 관점에서 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-757"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Science China Technological Sciences 68, 1110301 (2025). 고장 모드·원인 분석, 데이터 수집·센서, 모델 기반·데이터 기반 방법 검토 (검색 요약 범위)",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "2026년 3월 arXiv 프리프린트 'Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots'는 작업 배정·서비스 순서·충전 여부·충전 모드·충전기 접근을 함께 최적화해 플릿 전체의 배터리 열화를 균형 있게 나누는 정식화를 제안했고, 급속 충전에 따른 사이클 열화와 높은 충전 상태로 대기할 때의 달력 열화를 근사 열화 지표로 반영했다.",
      "tag": "사실",
      "source_ids": [
        "ref-756"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "fast charging intensifies cycling-related wear, and prolonged idling at elevated SOC accelerates calendar aging. 비교 기준: 최근접 가용 규칙, 열화 무시 에너지 인지 정식화, 충전기 용량 무시 정식화 (프리프린트, 검색 요약 범위)",
      "as_of": "2026-03",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템의 패치 관리 프로그램을 운영하는 자산 소유자와 제품 공급자에 대한 요구를 기술하고, 공급자–소유자 간 패치 정보 교환 형식과 패치 개발·배포·설치 활동을 정의하며, 보안 외 패치·업데이트에도 적용될 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-758"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "defined format for the distribution of information about security patches ... may also be applicable for non-security related patches or updates. 취약점 발견~패치 사이 완화는 다루지 않음 (제1판 2015-06, 검색 요약 범위)",
      "as_of": "2015-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "EU 기계 규정 (EU) 2023/1230 은 2027-01-20 부터 적용되며, 시장에 나온 기계에 대한 물리적 또는 디지털 변경이 새 위험을 만들거나 기존 위험을 키워 새 보호 조치가 필요하면 '실질적 변경'으로 정의해, 동작을 바꾸는 소프트웨어 업데이트가 이 판단 대상이 될 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-759"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "적용일 2027-01-20. 제3조(16) substantial modification: physical or digital change ... introduces a new hazard or increases an existing risk (검색 요약 범위, 원문 조문 미열람)",
      "as_of": "2023-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "AWS 샘플 저장소의 ROS 2 플릿 무선 펌웨어 업데이트 참조 구현은 IoT Jobs·Greengrass v2·Docker 로 배포를 지시·추적하고 플릿 색인으로 기기별 펌웨어 버전을 조회하며, 실패한 업데이트를 이전의 검증된 버전으로 자동 복귀시킨다고 밝히지만 운영용이 아닌 참조 구현이다.",
      "tag": "추정",
      "source_ids": [
        "ref-760"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"Automatically roll back failed firmware updates to previously running (known good) versions\". 참조·시연용 구현으로 명시(발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "2026-07-22 판교에서 열린 SDR(Software Defined Robot) 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍에서 KIST 휴머노이드연구센터가 클라우드 기반 SDR 공통 서비스 프레임워크를 소개했고, 이 플랫폼은 무선 업데이트(OTA)로 로봇 소프트웨어를 갱신하고 기능을 추가하는 것을 목표로 한다고 보도됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-761"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장(2026-07-23 보도). 원 매체·과제 공식 자료 미확인(검색 요약 범위)",
      "as_of": "2026-07-23",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "국내 로봇 안전 컨설팅 업체의 위험성평가 가이드는 같은 모델로 교체해도 제어기 펌웨어 버전·안전 기능 파라미터·엔드이펙터 재장착에 따른 정밀도가 달라질 수 있어 기존 위험성평가의 조건 변경에 해당하므로 변경 범위 재평가와 검증 문서 갱신이 필요하다고 권고한다.",
      "tag": "의견",
      "source_ids": [
        "ref-763"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "동일 모델 교체 시에도 펌웨어 버전·안전 기능 파라미터·엔드이펙터 정밀도 변화 → 위험성평가 조건 변경 → 변경 범위 재평가와 검증 문서 갱신 필요(검색 요약 범위, 요약 문장의 출처 귀속은 검색 결과 기준으로만 확인)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "한국로봇사용자협회의 협동로봇 설치 작업장 안전인증은 협동운전 산업용 로봇 시스템이 ISO 10218-2 를 준수하는지 심사하며, 인증서 발급일로부터 2년 주기로 정기 심사한다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "협동 로봇 설치 작업장 안전인증 심사규정: 영리 생산 목적 상시 작업장 대상, 발급일로부터 2년 주기 정기 심사(검색 요약 범위, 펌웨어 변경 시 재심사 여부는 미확인)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "분류 원문 질문 '제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까?'에 대해, 확인한 자료로는 로봇별 소프트웨어 버전(VDA 5050 팩트시트 versions, 소프트웨어 명판)을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전 변경·팩트시트 기능 선언 변화·안전 파라미터 변화·지도 버전 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-749",
        "ref-228",
        "ref-753",
        "ref-763"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(주 버전=호환성 깨짐), f4(팩트시트 versions), f11(소프트웨어 명판의 설치 인스턴스), f20(펌웨어·안전 파라미터 변경→재평가)에서 도출한 추정",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f23",
      "claim": "ROP 가 직접 맡을 수명주기 관리 몫은 로봇·어댑터·지도·모델의 버전 목록 유지, 로봇이 보고하는 배터리 상태·오류를 배정·충전 계획에 반영, 업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포하고 실패 시 복구를 조율, 지도 버전 활성화 시점 동기화로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-749",
        "ref-750",
        "ref-751",
        "ref-760"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "플릿 제어가 지도 pull·enableMap 을 지시(f1), 로봇이 batteryHealth·range 보고(f5), 관리형 노드의 교체·재시작(f8), 버전 조회·복귀(f18, 벤더 주장)에서 도출",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "연계 대상: 펌웨어 내용 자체, 관절·감속기 같은 기계 부품의 고장 진단·잔여 수명 예측, 배터리 관리 시스템(BMS) 내부의 열화 추정은 로봇 제조사·설비 쪽 영역이고, ROP 는 그 결과(배터리 상태 값·오류 코드·정비 필요 신호)를 받는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-757",
        "ref-750",
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "산업용 로봇 상태 감시는 센서·모델 기반 부품 진단(f14), 규격은 batteryHealth·errorCodes 같은 결과 값만 교환(f5·f6). 분류 원문 9장 '로봇 자체 지능·제어' 경계",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f25",
      "claim": "출하 마감 전 집중 시간대에 배터리 상태(batteryHealth)가 낮아진 로봇은 같은 충전 상태에서도 추정 도달 거리(range)가 짧아질 수 있어, 배터리 열화가 작업 배정·충전 계획의 제약으로 작용하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-750",
        "ref-756"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "state 스키마의 batteryHealth·range(f5)와 열화 인지 플릿 스케줄링 연구(f15)에서 도출한 시나리오 추정. 물류센터 실측 자료는 확인하지 못함",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "적치 구역의 랙 배치가 바뀌면 플릿 제어가 새 mapVersion 을 로봇에 내려받게 한 뒤 enableMap 으로 전환해야 하고, 같은 mapId 에 한 버전만 활성화되므로 전환 시점과 진행 중 주문의 정리가 적치 작업 재개의 시작 조건이 되는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-749"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "downloadMap·enableMap 동작과 '한 mapId 한 활성 버전' 규칙(f1)에서 도출한 시나리오 추정",
      "as_of": "2026-09-25",
      "flow_step": "적치",
      "flow_item": "시작 조건"
    },
    {
      "id": "f27",
      "claim": "24. 자산·소프트웨어 수명주기 관리는 업데이트 뒤 회귀·장애 시험(23. 시험·형식 검증·벤치마크), 시뮬레이션 환경의 판 관리(22. 시뮬레이션·예측용 디지털 트윈), 보안 패치(26. 사이버보안·접근권한·개인정보), 변경 후 안전 재평가(25. 안전·위험 관리), 배터리 열화를 반영한 충전(16. 공용 자원·충전·에너지 최적화)과 맞물리는 것으로 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-668",
        "ref-758",
        "ref-756",
        "ref-763"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10(시뮬레이터 지원 종료), f16(패치 관리), f15(열화 인지 충전), f20(변경 후 재평가)을 영역 연결로 정리한 의견",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-749",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 의미적 버전 규칙, 토픽의 주 버전, 지도 배포·버전(downloadMap·enableMap·deleteMap), 미지원 파라미터 오류 규정 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-750",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. powerSupply(stateOfCharge·batteryHealth·charging·range)와 maps(mapId·mapVersion·mapStatus) 필드 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
      "source_unopened": false
    },
    {
      "id": "ref-751",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "Managed nodes (ROS 2 Design: node_lifecycle)",
      "published": null,
      "url": "https://design.ros2.org/articles/node_lifecycle.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 관리형 노드의 주 상태·전이 상태·전이와 목적(초기화 확인, 실행 중 교체·재시작) 설계 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/node_lifecycle.md",
      "source_unopened": false
    },
    {
      "id": "ref-752",
      "org": "Open Robotics (ROS REP)",
      "title": "REP 2000 -- ROS 2 Releases and Target Platforms",
      "published": null,
      "url": "https://www.ros.org/reps/rep-2000.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 배포판별 출시·지원 종료 일정과 LTS 5년·비LTS 1.5년 지원 정책.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-2000.rst",
      "source_unopened": false
    },
    {
      "id": "ref-753",
      "org": "IDTA (admin-shell-io/id GitHub)",
      "title": "IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing)",
      "published": null,
      "url": "https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "자산관리셸 소프트웨어 명판 서브모델의 목적(업데이트·패치·라이선스·감사)과 버전·설치 인스턴스 속성.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/id/master/idta/SoftwareNameplate/1/0/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-754",
      "org": "ISO",
      "title": "ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines",
      "published": "2018",
      "url": "https://www.iso.org/standard/71194.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 기계 상태 감시 프로그램 수립 일반 지침, 상태 감시·진단 표준군의 상위 문서.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-755",
      "org": "ISO",
      "title": "ISO 55000:2024 - Asset management — Vocabulary, overview and principles",
      "published": "2024-07",
      "url": "https://www.iso.org/standard/83053.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자산 관리 개요·원칙·용어 제2판(2014 판 대체), 수명주기 단계별 자산 평가.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-756",
      "org": "arXiv (저자 미확인)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AMR 플릿의 작업 배정·충전을 배터리 열화 균형과 함께 최적화하는 프리프린트.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-757",
      "org": "Lei, Y., Liu, H., Li, N. 외",
      "title": "Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301)",
      "published": "2025",
      "url": "https://link.springer.com/article/10.1007/s11431-024-2810-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 고장 모드, 데이터 수집, 모델·데이터 기반 상태 감시·고장 진단 검토.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-758",
      "org": "IEC",
      "title": "IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment",
      "published": "2015-06",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 제어 시스템 패치 관리 프로그램의 소유자·공급자 요구와 패치 정보 교환 형식.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-759",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 기계 규정. 2027-01-20 적용, 디지털 변경을 포함한 실질적 변경 정의.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-760",
      "org": "Amazon Web Services (aws-samples GitHub)",
      "title": "ros2-ota-firmware-updates — README",
      "published": null,
      "url": "https://github.com/aws-samples/ros2-ota-firmware-updates",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "ROS 2 플릿 무선 펌웨어 업데이트 참조 구현(IoT Jobs·Greengrass·Docker, 버전 추적, 롤백 주장). 운영용 아님.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/aws-samples/ros2-ota-firmware-updates/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-761",
      "org": "네이트 뉴스(원 매체 미확인)",
      "title": "클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장",
      "published": "2026-07-23",
      "url": "https://m.news.nate.com/view/20260723n24828",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SDR 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍과 클라우드 기반 OTA 목표 보도.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-762",
      "org": "한국로봇사용자협회",
      "title": "협동로봇 설치 작업장 안전인증 안내",
      "published": null,
      "url": "https://www.korua.or.kr/inspect/inspectInfo.do",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 협동로봇 설치 작업장 안전인증(ISO 10218-2 준수 심사, 2년 주기 정기 심사) 안내.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-763",
      "org": "세이프틱스(Safetics)",
      "title": "로봇 시스템 위험성평가 가이드",
      "published": null,
      "url": "https://doc.safetics.io/insight-risk-assessment/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 시스템 위험성평가 가이드. 동일 모델 교체 시 펌웨어·안전 파라미터 변경에 따른 재평가 권고.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-228",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 팩트시트 JSON 스키마. 이번 실행에서 versions 배열과 batteryCharging 블록 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마. 이번 실행에서 식별·배터리·오류 필드 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-668",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_simulation — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_simulation",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 시뮬레이션 플러그인 저장소 README(이번 실행에서 다시 열지 않음, 2026-09-25-56 확인 내용 재사용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f17(디지털 변경도 실질적 변경 판단 대상), f9(배포판 지원 종료), f22(분류 원문 질문 — 추정) / 4절 핵심 개념: f13(자산·수명주기), f12(상태 감시), f5(배터리 상태), f11(소프트웨어 명판), f16(패치 관리), f1(지도 버전) / 5절 현장 시나리오: f26(적치·시작 조건), f25(출하·제약), f20·f21(교체 후 재평가, 의견·국내 제도) / 6절 대표 접근법: f14(상태 감시·고장 진단), f15(열화 인지 스케줄링), f8(관리형 노드), f18(OTA·롤백, 벤더 주장 병기), f19(국내 SDR 과제) / 7절 표준·오픈소스: f1~f5(VDA 5050), f6(MassRobotics), f11(IDTA 02007), f12·f13·f16·f17, f9·f10 / 8절 대표 연구: f14·f15 / 9절 경계: f23(ROP 직접), f24('연계 대상') / 10절 연결: f27(23. 시험·형식 검증·벤치마크, 22. 시뮬레이션·예측용 디지털 트윈, 26. 사이버보안·접근권한·개인정보, 25. 안전·위험 관리, 16. 공용 자원·충전·에너지 최적화), f7·f4(21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스), f26(6. 지도·공간·위치 모델) / 11절: open_questions_new 4건. 벤더 주장 f18 은 [추정]+'벤더 주장', f20 은 [의견]."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "예지보전",
      "term_en": "Predictive Maintenance (PdM)",
      "definition": "설비의 상태 데이터로 고장 시점을 예측해 고장 전에 정비를 계획하는 정비 방식이다."
    },
    {
      "term_ko": "상태 기반 정비",
      "term_en": "Condition-Based Maintenance (CBM)",
      "definition": "정해진 주기 대신 상태 감시로 확인한 설비 상태에 따라 정비 여부와 시점을 정하는 정비 방식이다."
    },
    {
      "term_ko": "배터리 건강 상태",
      "term_en": "State of Health (SOH)",
      "definition": "배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다."
    },
    {
      "term_ko": "소프트웨어 명판",
      "term_en": "Software Nameplate (IDTA 02007)",
      "definition": "자산관리셸에서 소프트웨어 제품과 설치 인스턴스의 식별·버전·설치 정보를 통일된 형태로 기술하는 서브모델이다."
    },
    {
      "term_ko": "무선 업데이트",
      "term_en": "Over-the-Air Update (OTA)",
      "definition": "기기를 회수하지 않고 네트워크로 소프트웨어·펌웨어를 내려받아 갱신하는 방식이다."
    }
  ],
  "open_questions_new": [
    "제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반",
    "VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f2 | 종류: 일반",
    "국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f21 | 종류: 일반",
    "EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f17 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처)",
      "f6: MassRobotics 스키마의 버전 필드 부재는 요약 판독 기준이라 추정으로 둠",
      "f17: EU 2023/1230 조문 원문 미열람, 제조사가 예정한 업데이트의 취급은 2차 해설에만 있어 finding 에서 제외",
      "f19: 원 매체와 SDR 과제 공식 자료 미확인",
      "f20·f21: 검색 요약 문장의 출처 귀속(세이프틱스/한국로봇사용자협회)을 원문으로 확인하지 못함",
      "ref-756 저자, ref-749·ref-750·ref-753 발행일 미확인",
      "f22: 펌웨어 변경 영향 범위 산정 공개 절차 찾지 못함"
    ],
    "scope_violations": [
      "f24: 감속기·관절 진단, BMS 내부 열화 추정은 분류 원문 9장 '로봇 자체 지능·제어' 쪽이므로 '연계 대상:'으로 표시",
      "f14·f15: 부품 진단·열화 모델 연구는 ROP 가 결과를 받아 쓰는 근거로만 제안"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-749·ref-750·ref-751·ref-752·ref-753·ref-760 과 재사용 ref-228·ref-230. 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 17회/30, 신규 출처 15건/15(ref-749~ref-763, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 13374, ISO 10218-1:2025(사이버보안 요구 추가), CISA SBOM, ICAN-Deploy(카나리 배포 프리프린트)는 출처로 넣지 않음. 재사용 3건: ref-228·ref-230(2026-09-25-57 브리프 값), ref-668(2026-09-25-56 브리프 값, 이번에 다시 열지 않음). 교차 확인 0건. 한국 자료: 한국로봇사용자협회 안전인증(ref-762), 세이프틱스 가이드(ref-763, 의견), SDR 과제 보도(ref-761). 27. AI·학습·적응과 모델 운영 관련 finding 없음(모델 버전 관리는 일반 수명주기 관점으로만 다룸). 8·22 구분: f10 은 시뮬레이션 환경의 판 관리로만 서술. 정정 요청 없음, 대상 영역 열린 질문 0건."
  }
}
```

### docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리"
type: area
category: "F. 도입·검증·유지관리"
area_no: 24
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 24. 자산·소프트웨어 수명주기 관리

# 24. 자산·소프트웨어 수명주기 관리

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [분류원문]

## 2. SCM 관점의 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

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

### docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md (요약)

```markdown
# 21. 온보딩·설정·현장 시운전

소속 대분류: F. 도입·검증·유지관리 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [분류원문]

## 2. SCM 관점의 질문

새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md (요약)

```markdown
# 22. 시뮬레이션·예측용 디지털 트윈

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 23. 시험·형식 검증·벤치마크

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [분류원문]

## 2. SCM 관점의 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 513건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 133개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- order-batching: 주문 배치 (Order Batching)
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [24] 에 걸린 0건 / 전체 83건)

```markdown
없음
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
# area_no 는 1~28 의 세부영역 번호다. 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 7. 화물·재고·자산 식별과 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 7            # 7. 화물·재고·자산 식별과 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "팔레트 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 7            # 주 연구영역: 7. 화물·재고·자산 식별과 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 팔레트 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 7            # 7. 화물·재고·자산 식별과 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1~7). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-09-25-60/research.md

```markdown
# 리서치 브리프 2026-09-25-60

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-60 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- E. 협업·현장 운영 대분류 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음)
- 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(제한 운영 처리량 추정, oq-081): 22. 시뮬레이션·예측용 디지털 트윈 페이지가 seed 상태라 게시된 근거 없음
- 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스 ↔ 26. 사이버보안·접근권한·개인정보, 24. 자산·소프트웨어 수명주기 관리, 21. 온보딩·설정·현장 시운전: 게시된 E. 협업·현장 운영 세부영역 페이지에 검증된 근거 없음
- 5. 로봇 능력·작업 온톨로지·6. 지도·공간·위치 모델 ↔ E. 협업·현장 운영 세부영역: E 쪽 게시 페이지에 직접 근거 없음

## 조사 질문

1. 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]
2. 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문] — 20. 예외 복구·재계획·업무 연속성이 A. 업무·공급망 설계, B. 공통 정보·환경 모델, C. 연결·실행 기반, D. 계획·최적화와 넘겨받는 지점은 무엇인가? (oq-021, oq-038, oq-048, oq-079 관련)
3. 17. 로봇 간 협업·물리적 인계의 인계 확인 신호는 7. 화물·재고·자산 식별과 추적, 10. 설비·건물 시스템 연동, 14. 작업 순서·스케줄링, 23. 시험·형식 검증·벤치마크, 25. 안전·위험 관리와 어떻게 이어지는가? (oq-001, oq-006, oq-042, oq-062, oq-063, oq-064)
4. 18. 사람–로봇 협업·운영 인터페이스는 3. 처리능력·거점·설비 계획, 9. 로봇·제조사 관제 연동, 13. 작업 배정 — MRTA, 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영과 무엇을 주고받는가? (oq-009, oq-070, oq-072)
5. 19. 모니터링·이상 탐지·원인 분석은 4. 성과·경제성·프로세스 개선, 8. 실시간 세계 상태·데이터 일관성, 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스와 어떻게 연결되는가? (oq-018, oq-033, oq-073)
6. E. 협업·현장 운영과 다른 대분류의 연결 가운데 근거가 아직 없는 쌍은 무엇인가? (다루지 않은 연결 목록)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: VDA 5050 3.0.0 에서 관제가 주문 취소(cancelOrder)를 보내면 예정된 동작은 취소되어 동작 상태를 FAILED 로 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [추정] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 상위 시스템의 취소가 로봇이 화물을 실은 뒤에 오면 로봇 쪽 동작 실패 보고만으로는 화물 위치가 정해지지 않으므로, 되돌림 작업과 재고 반영 규칙을 정하는 일이 두 대분류가 넘겨받는 지점이 될 것으로 보이며 이를 정한 표준·사례는 확인되지 않았다(oq-021). | ref-031, ref-489 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f3 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: 시설 안 로봇 사이·로봇과 작업대 사이의 물리적 인계는 CBV 의 accepting·receiving 에 가깝고 운송 수단 기준의 loading·unloading 과 맞지 않아, 인계 이벤트의 업무 단계 값을 ROP 쪽에서 정해야 할 것으로 보인다(oq-006). | ref-044 | 아니오 | low | 2021-09-30 | 완료·인계 | 원문 미열람 |
| f4 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: VDA 5050 상태 스키마의 선택 필드 loads 의 loadId 는 바코드·RFID 같은 적재물 식별 번호로, 멈춘 로봇에 어떤 화물이 실렸는지 관제가 알 수 있게 하지만 적재물을 식별할 수 없는 로봇은 생략할 수 있다. | ref-051 | 아니오 | medium | 2026-09-25 | 피킹 / 작업 대상 | — |
| f5 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: EPCIS 1.2 는 이미 기록된 이벤트를 오류 선언(errorDeclaration)으로 정정하게 하므로, 회수한 화물의 재고·이벤트 기록 정정이 식별·추적 쪽 기록 규칙에 기대게 된다. | ref-492 | 아니오 | medium | 2016-09-29 | 완료·인계 | 원문 미열람 |
| f6 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: 지연 원인을 문·로봇·통신으로 가르려면 같은 시각의 문 모드(closed·moving·open·offline·unknown)와 작업 상태(delayed·blocked 등)를 한 시간축에 맞춘 현재 상태 기록이 필요할 것으로 보이며, 이는 현재 상태를 표현하는 쪽이지 가정한 미래를 실험하는 22. 시뮬레이션·예측용 디지털 트윈의 일이 아니다. | ref-313, ref-111 | 아니오 | low | 2026-09-25 | 보충 / 예외·성과 | 원문 미열람 |
| f7 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석·20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 상태 스키마의 오류 수준은 WARNING·URGENT·CRITICAL·FATAL 네 값이고, 연결 스키마는 연결 끊김을 CONNECTION_BROKEN 으로 보고한다. | ref-051, ref-449 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 작업 상태·VDA 5050 오류·MassRobotics 운용 상태(waitingExternalEvent 등)가 서로 다른 어휘로 보고되어, 이를 ROP 의 공통 원인 범주로 옮기는 매핑이 두 대분류 사이에 필요할 것으로 보이며 공통 매핑 표준은 확인되지 않았다(oq-033). | ref-051, ref-230, ref-111 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 문 노드는 문 상태를 /door_states 로 발행하고 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 해, 설비 원인 판정의 근거가 된다. | ref-313, ref-283 | 아니오 | medium | 2026-09-25 | 보충 / 제약 | 원문 미열람 |
| f10 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 배송 작업에서 로봇은 픽업 지점에서 DispenserResult 를, 하역 지점에서 IngestorResult 를 받을 때까지 요청을 반복해 보내고 워크셀은 /dispenser_states·/ingestor_states 로 상태를 주기적으로 발행하며, 이 흐름은 플릿 어댑터의 perform_deliveries 설정이 켜져야 동작한다. | ref-023 | 아니오 | medium | 2026-09-25 | 보충 / 완료·인계 | — |
| f11 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 반도체 업종 SEMI E84 처럼 준비–진행–완료를 양쪽이 단계별로 확인하는 인계 신호 구조는 이동로봇–작업대 인계 상태 모델의 참고가 될 수 있으나, VDA 5050 은 주변 설비 인터페이스를 범위에서 제외하고 물류 업종의 제조사 중립 인계 신호 규격은 확인되지 않았다(oq-042, oq-062). | ref-202, ref-203, ref-031 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f12 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f13 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 은 교착(deadlock)과 통신 오류의 탐지·해소를 관제(fleet control)의 기능으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f14 | [추정] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: 오류·연결 상태 수신, 주문 일시정지·취소, Open-RMF 로봇 갱신 핸들을 통한 재계획 요청·작업 수락 중지가 실행 신뢰성 계층과 복구 결정이 맞물리는 지점이 될 것으로 보인다. | ref-031, ref-537 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f15 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자가 서로를 수용하는 경로로 협상한다. | ref-004 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f16 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: 지연에 강건한 계획 실행(행동 의존 그래프, Hönig 외 2019)과 지연된 로봇의 통과 순서 재스케줄(Feng 외 2024)이 연구되어, 실행 중 지연 복구가 경로 계획 연구와 이어진다. | ref-188, ref-483 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 작업 의존성·우선순위 선점·고장 복구를 함께 다루는 다중 로봇 작업 배정 방법(Kalempa 외 2021)이 있어, 고장 로봇의 남은 작업 재배정이 배정 문제로 넘어간다. | ref-484 | 아니오 | medium | 2021-09-30 | 수행 자원 | 원문 미열람 |
| f18 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링: 사람 피커와 AMR 의 협동 피킹 연구는 두 자원의 조율을 배치 구성·배치 순서와 작업 완료 시각(makespan) 최소화 문제로 다룬다. | ref-467, ref-468 | 아니오 | medium | 2023 | 피킹 / 수행 자원 | 원문 미열람 |
| f19 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ D. 계획·최적화의 14. 작업 순서·스케줄링·16. 공용 자원·충전·에너지 최적화: 이동로봇 운반과 로봇팔 적치가 선후로 이어지면 스케줄 간 의존이 생기고 인계 스테이션의 도크·버퍼가 공용 자원 제약이 되어 인계 시점을 두 로봇 일정에 함께 맞춰야 할 것으로 보인다. | ref-394, ref-209 | 아니오 | low | 2026-07 | 보충 / 제약 | 원문 미열람 |
| f20 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 협동 피킹 시스템에서 피커와 로봇의 투입 수를 정하는 연구(Yang 외 2026-03)가 있어 인원·로봇 비율 결정이 처리능력 계획과 이어지나, 교대조 단위 결정 여부는 미확인이다(oq-009). | ref-469 | 아니오 | medium | 2026-03 | 피킹 / 수행 자원 | 원문 미열람 |
| f21 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: AGV 시스템 병목 탐지 방법 비교 연구(Roser 외 2003)는 가동률·대기 시간 기반 방법에 이동 병목 탐지 대비 한계가 있다고 보고해, 원인·병목 판정 방식이 개선 대상 선정과 이어진다(oq-018). | ref-451 | 아니오 | medium | 2003 | 예외·성과 | 원문 미열람 |
| f22 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 상태 메시지는 운용 모드(STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN)와 비상정지 종류(MANUAL·REMOTE·NONE)를 보고해, 사람 개입 상태가 관제 연동을 통해 운영 인터페이스로 들어온다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f23 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 데모는 시설 비상 경보 때 로봇을 가장 가까운 주차 위치로 보내는 흐름을 보인다. | ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f24 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 도킹 정지 위치의 반복성을 확인하는 시험 방법 ASTM F3499-21 이 있고, NIST ARIAC 2025 는 완성 키트를 실은 AGV 를 움직이기 전에 품질 확인 서비스를 호출하게 해 이동 전 인계 확인을 평가한다. | ref-204, ref-008 | 아니오 | medium | 2021 | 완료·인계 | — |
| f25 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: NIST 협업 로봇 시스템 성능 프로젝트는 사람–로봇·로봇–로봇 협업 팀의 안전성과 효과를 평가하는 방법·지표 개발을 목표로 한다. | ref-007 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f26 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: ANSI/A3 R15.08-2-2023 은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C 로 다루며 시스템·적용 단위 안전 요구를 정한다. | ref-210 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f27 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: 사람 감지·보호 필드·비상정지 같은 안전 기능은 로봇 제조사·현장 통합사가 갖추고, ROP 는 로봇이 보고한 안전 상태를 표시하고 재개·수동 전환 승인을 작업 흐름에 반영하는 경계가 될 것으로 보인다. | ref-470, ref-051, ref-210 | 아니오 | low | 2026-09-25 | 제약 | — |
| f28 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: 국내에서는 고용노동부가 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했고, 중소벤처기업부는 2024-11 대구 규제자유특구 실증을 거쳐 이동식 협동로봇 산업표준이 제정되었다고 발표했다. | ref-473, ref-475 | 아니오 | medium | 2024-11 | 제약 | 원문 미열람 |
| f29 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, Ren 외 2023)와 사용자 명령을 분류·모호성 해소하는 연구(CLARA, Park 외 2024), 실행 전 안전 게이트 연구(Obi 외 2026-04)가 있어 자연어 지시 인터페이스가 AI 연구 방법과 이어진다. | ref-351, ref-353, ref-417 | 아니오 | medium | 2026-04 | — | 원문 미열람 |
| f30 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석·18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 로봇 실패에 대한 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구(Das 외 2021)가 있어, 분류 원문 8장 교차 규칙의 장애 분석이 원인 분석 결과를 사람에게 전달하는 인터페이스까지 이어진다. | ref-476 | 아니오 | medium | 2021-01 | 예외·성과 | 원문 미열람 |
| f31 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스: 표준마다 상태·오류 어휘가 다르고 공통 매핑 표준이 확인되지 않으므로, 이종 플릿의 오류 수준·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-033, oq-073). | ref-051, ref-230, ref-111 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-007 | NIST | Performance of Collaborative Robot Systems | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/performance-collaborative-robot-systems | 예 |
| ref-008 | NIST | ARIAC Documentation | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/ | 아니오 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | medium | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-202 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | 표준 | medium | 2026-09-25 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 예 |
| ref-203 | PEER Group | SEMI E84: Carrier Handoff | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.peergroup.com/definition-of-standard/semi-e84/ | 예 |
| ref-204 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | 표준 | medium | 2026-09-25 | https://www.astm.org/f3499-21.html | 예 |
| ref-209 | Zang, C. 외 | Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.17724 | 예 |
| ref-210 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 2023 | 표준 | medium | 2026-09-25 | https://webstore.ansi.org/standards/ria/ansia3r15082023 | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 예 |
| ref-451 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | 논문 | medium | 2026-09-25 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 예 |
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 2022 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 | 예 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 2023 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 | 예 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 2026-03 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 예 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 예 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2101.01625 | 예 |
| ref-483 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.18145 | 예 |
| ref-484 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 2021-09-30 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/1424-8220/21/19/6536 | 예 |
| ref-489 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 2026-04-16 | 벤더 문서 | medium | 2026-09-25 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction | 예 |
| ref-492 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 예 |
| ref-537 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 실행: '다른 대분류와의 연결' 절만 patches 로 채움. A. 업무·공급망 설계: f1·f2(20↔1), f20(18↔3), f21(19↔4) / B. 공통 정보·환경 모델: f3(17↔7), f4·f5(20↔7), f6(19↔8, 8·22 구분 유지) / C. 연결·실행 기반: f7·f8(19·20↔9), f22(18↔9), f9(19↔10), f10·f11(17↔10), f23(18↔10), f12(20↔11), f13·f14(20↔12) / D. 계획·최적화: f15·f16(20↔15), f17(20↔13), f18(18↔13·14), f19(17↔14·16) / F. 도입·검증·유지관리: f24·f25(17↔23) / G. 안전·보안·지능·거버넌스: f26·f27·f28(17·18↔25), f29·f30(18·19↔27, 분류 원문 8장 교차 규칙), f31(19↔28). 아직 다루지 않은 연결: 20↔22(oq-081, 22 페이지 seed), 21·24·26 과의 연결, 5·6 과의 연결. 추정 태그 finding 은 추정 그대로, 관련 열린 질문 id 병기. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 35 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(연결 서술은 게시된 세부영역 페이지의 단일 출처 주장 재인용 중심)
    - 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거 미확보(oq-081)
    - f28: 2024-11 제정 KS 의 번호·내용 미확인(oq-070)
    - ref-007·ref-008·ref-104 등 재사용 출처 원문 이번 실행에서 재열람 안 함
- 범위 경계 위반 의심:
    - f11: SEMI E84 는 업종별 인계 규격(분류 원문 9장 업종별 조건)이므로 참고 사례로만 서술
    - f26·f27·f28: 설비 안전 기능·안전 표준 이행은 로봇 제조사·현장 통합사 몫(연계 대상), ROP 는 상태 표시·승인 흐름만 맡는 것으로 서술
    - f23: 시설 비상정지·설비 안전 제어는 연계 대상, ROP 는 경보 상태 반영만
- 한계: 대분류 연결 실행으로 근거를 게시된 17. 로봇 간 협업·물리적 인계, 18. 사람–로봇 협업·운영 인터페이스, 19. 모니터링·이상 탐지·원인 분석, 20. 예외 복구·재계획·업무 연속성 페이지의 검증된 주장과 각주(기존 참고문헌 재사용)에서 찾았고, 새 출처는 필요하지 않아 WebSearch 0회·신규 출처 0건이다(한국어·영어 신규 검색 없음; 국내 자료는 ref-473·ref-475 재사용). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 다시 연 출처: ref-004(rmf-core), ref-023(workcells), ref-031(VDA 5050 3.0.0 명세), ref-051(state.schema). 나머지 재사용 출처는 원문 미열람 표시, 신뢰도 상한 medium. ref-031 원문 요약 도구는 본문에서 WARNING·CRITICAL 만 언급했으나 state.schema(ref-051) 원문의 errorLevel 열거값이 WARNING·URGENT·CRITICAL·FATAL 이므로 f7 은 ref-051 기준으로 적음. 22. 시뮬레이션·예측용 디지털 트윈·23·24·25·26·27·28 페이지는 seed 상태라 상대편 서술도 E. 협업·현장 운영 쪽 근거에 기댐. 27. AI·학습·적응과 모델 운영 연결(f29·f30)은 교차 규칙에 따라 18·19 적용 대상과 함께 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f6 에서 구분. 새 열린 질문 없음(관련 질문은 기존 oq-001·006·009·018·021·033·038·042·048·062~064·070·073·079·081 로 이미 등록됨). 정정 요청 없음.
```

### runs/2026-09-25-59/research.md

```markdown
# 리서치 브리프 2026-09-25-59

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-59 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 23. 시험·형식 검증·벤치마크 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크 구분 필요)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분 필요)
- 섹션 11. 열린 질문 비어 있음(대상 영역 열린 질문 oq-055·oq-058·oq-063·oq-077 반영 필요)

## 조사 질문

1. 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
2. 로봇 시스템 시험에서 장애 주입·시나리오 기반 시뮬레이션 시험·회귀 시험은 어떤 도구와 방식으로 이루어지며 실무의 어려움은 무엇인가? (섹션 3·4·6 겨냥)
3. 다중 로봇·AGV 시스템의 교착·제약 위반을 형식 검증(모델 검사, BDD 기반 분석)과 런타임 검증으로 확인하는 연구·도구는 무엇인가? (섹션 6·8 겨냥)
4. 다중 로봇 경로·작업 배정 알고리즘과 로봇 작업 능력을 비교하는 벤치마크·대회(MAPF 벤치마크, League of Robot Runners, NIST ARIAC)는 무엇을 어떻게 측정하며, 격자 가정 성과가 실제 처리량으로 이어지는가? (섹션 7·8 겨냥, oq-058)
5. 이동로봇·무인운반차의 안전·성능 시험을 정하는 표준(ISO 3691-4, ASTM F45, KS B ISO 18646)과 국내 시험기관(한국로봇산업진흥원)의 시험 항목은 무엇인가? (섹션 7·9 겨냥, 한국 자료 우선)
6. VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (oq-055, 섹션 9·11 겨냥)
7. ROP 가 직접 맡을 시험 범위(오케스트레이션 논리·인터페이스·장애 대응)와 제조사·시험기관에 맡길 범위(로봇 자체 안전·주행 성능)는 어떻게 나뉘는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST ARIAC 2025 문서는 경진 중 컨베이어 정지, 전압 시험기 데이터 중단, 진공 공구 파지 실패, 고우선 주문 투입을 '민첩성 도전 과제'로 주입해 시스템의 장애 감지·복구와 긴급 요청 대응을 시험한다. | ref-629 | 아니오 | medium | 2025 | 예외·성과 | — |
| f2 | [사실] | NIST ARIAC 2025 채점은 제출한 키트·모듈의 완료 비율로 기본 점수를 주고 시간 안 완료·고우선 주문 신속 처리·센서 예산 준수 등에 가점을, 충돌·정상 부품 낙하·잘못된 위치 배치 등에 감점을 준 뒤, 시행별 상위 2회 평균 실행 점수(80%)와 심사위원 평가(20%)를 합친다. | ref-630 | 아니오 | medium | 2025 | 예외·성과 | — |
| f3 | [추정] | ARIAC 가 장애를 시험 중에 계획적으로 주입하고 완료·시간·비용(센서 예산)·위반을 한 점수로 묶는 방식은, 물류 현장 오케스트레이션의 회귀 시험에서도 장애 시나리오와 처리량·시간·비용 지표를 함께 판정 기준으로 두는 틀로 옮겨 쓸 수 있을 것으로 보인다. | ref-629, ref-630 | 아니오 | low | 2025 | 예외·성과 | — |
| f4 | [사실] | Luckcuck 외(2019)의 자율 로봇 형식 명세·검증 조사 논문은 자율 로봇 시스템이 복잡하고 혼성적이며 안전 필수인 경우가 많아, 시험과 시뮬레이션만으로는 정확성 보장이나 인증 근거로 충분하지 않다고 보고 형식 방법의 과제·형식체계·접근법을 분류했다. | ref-631 | 아니오 | medium | 2019-09 | — | 원문 미열람 |
| f5 | [사실] | von Berg·Aichernig·Wedenik(FM 2026 사례 연구)은 정해진 경로망을 따라 움직이는 창고 AGV 시스템을 세 가지 방식으로 전이 시스템에 인코딩하고 이진 결정 다이어그램(BDD)으로 기호적 분석해, 합성 레이아웃과 실제 레이아웃 모두에서 교착 회피를 수행했다. | ref-643 | 아니오 | medium | 2026-05 | 제약 | 원문 미열람 |
| f6 | [사실] | Afzal 외(ICST 2020)는 로봇 실무자 면담으로 로봇 시스템 시험 실무 12가지와 어려움 9가지를 도출해 실세계 복잡성, 커뮤니티와 표준, 구성요소 통합의 세 주제로 묶었고, 이를 로봇 시스템 시험에 초점을 맞춘 첫 연구로 소개했다. | ref-632 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f7 | [사실] | ros2_fault_injection 은 ROS 2 토픽을 *_raw 로 돌려 받아 편향·잡음·지연·누락·명령 정지 같은 장애를 넣어 다시 발행하고, 서비스 강제 실패와 좌표 변환 손상도 지원하며, YAML 시나리오의 단정(assertion)으로 합격·불합격을 내고 헤드리스 실행기가 종료 코드로 지속적 통합(CI)에 결과를 넘긴다. | ref-633 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f8 | [추정] | 연계 대상: ros2_fault_injection 이 기본으로 다루는 오도메트리·레이저 스캔·IMU 등 센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하고, ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. | ref-633 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | ROSMonitoring 은 YAML 설정으로 ROS 토픽·서비스를 관찰하는 감시 노드를 생성하며, 온라인 모드에서는 외부 판정기(oracle)의 판정을 받아 위반 메시지를 기록하거나 걸러 내고 오프라인 모드에서는 사건만 기록하는 명세 형식 비종속 런타임 검증 틀로 ROS 1·ROS 2 를 모두 지원한다. | ref-634 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f10 | [사실] | Open-RMF 시뮬레이션 문서는 시뮬레이션에 쓴 코드를 실제 시스템에서 수정 없이 실행하므로 시뮬레이션의 반복 가능한 시나리오로 버그 수정을 확인하고, 드물지만 심각한 예외 상황과 장시간 운전을 배치 전에 시험할 수 있다고 설명한다. | ref-667 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | Stern 외(2019)는 다중 에이전트 경로 찾기(MAPF) 논문마다 가정과 목적함수가 달라 기준선 비교가 어렵다는 문제를 들어 공통 용어를 정리하고 새 격자 기반 벤치마크를 소개했다. | ref-635 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f12 | [사실] | League of Robot Runners 는 Amazon Robotics 가 후원하는 다중 로봇 조율 대회로, MAPF 의 핵심 과제를 찾고 벤치마크 인스턴스를 만들어 최신 성과를 추적하는 것을 목표로 하며 로봇 동역학·지속형 계획·작업 배정·실시간 실행을 창고 물류 같은 응용을 겨냥해 다룬다. | ref-636 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f13 | [사실] | LSMART(2026)는 기존 MAPF·지속형 MAPF 연구가 단순화한 운동 모델과 완전한 실행·통신을 가정한다는 한계를 들어, AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터를 내고 언제 계획할지·어떻게 계획할지·계획 실패 시 어떻게 복구할지를 비교했다. | ref-637 | 아니오 | medium | 2026-02 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | 연계 대상: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정하며, 사람 감지 시험·안정성 시험과 부속서의 검증 절차를 포함한다. | ref-638 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f15 | [사실] | 연계 대상: ASTM F45 위원회(무인 자동 유도 산업 차량)는 용어·권고 관행·시험 방법을 개발하며 환경 영향, 도킹·주행, 물체 감지·보호, 통신·통합 분과를 두고, NIST 가 이 표준 개발에 참여한다. | ref-639 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | 연계 대상: KS B ISO 18646 시리즈는 서비스 로봇의 성능 기준과 관련 시험 방법을 KS 로 부합화한 것으로, 제1부는 바퀴형 로봇의 이동 능력을 다루고 주행·조작 등을 다루는 다른 부가 함께 있다. | ref-640 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [사실] | 한국로봇산업진흥원은 로봇 시험평가에 KS·ISO·IEC·CISPR 등 표준 시험 방법을 적용하고, 경사 노면·특수 노면·계단·주행 내구 같은 로봇 주행 성능 시험을 수행한다. | ref-641 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f18 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 대응 인트라로지스틱스 소프트웨어 업체들과 인증을 마쳤다고 발표했다. | ref-642 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f19 | [추정] | oq-055 관련: 이번 조사에서 VDA 5050 공식 인증 기관이나 공식 적합성 시험 절차는 확인하지 못했고, 확인된 인증은 로봇 제조사와 관제 소프트웨어 업체 사이의 쌍별 연동 인증 형태여서, ROP 는 새 로봇 연동마다 자체 인수 시험을 두어야 할 것으로 보인다. | ref-642 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f20 | [의견] | Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색 환경은 22. 시뮬레이션·예측용 디지털 트윈과 공유되지만, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측을, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인을 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다. | ref-667 | 아니오 | low | 2026-09-25 | — | — |
| f21 | [추정] | 분류 원문 질문 '업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가?'에 대해, 확인한 자료로 보면 반복 가능한 시뮬레이션 시나리오에 장애 주입과 합격 판정 단정을 붙여 지속적 통합에서 매 변경마다 다시 돌리는 방식이 답이 될 것으로 보이나, 물류 오케스트레이션 소프트웨어에 이를 적용해 결과를 공개한 현장 사례는 찾지 못했다. | ref-629, ref-633, ref-667 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f22 | [추정] | 시나리오 예시(가상): 피킹 단계에서 플릿 어댑터를 업데이트한 뒤, 운반 중인 로봇이 멈추는 장애를 주입하고 작업이 재배정되는지와 완료 확인 전에는 재고 변경이 확정되지 않는지를 단정으로 확인하는 회귀 시험을 구성할 수 있을 것으로 보인다. | ref-629, ref-633 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f23 | [추정] | ROP 가 직접 맡을 시험 몫은 작업 배정·교통 관리 논리의 교착·제약 위반 검증, 관제 인터페이스 적합성, 장애 주입 시 재배정·복구 동작의 회귀 시험, 운영 중 런타임 감시로 보인다. | ref-643, ref-633, ref-634, ref-667 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | 연계 대상: 로봇 자체의 사람 감지·안정성 같은 안전 검증(ISO 3691-4)과 주행·도킹·이동 성능 시험(ASTM F45, KS B ISO 18646, 한국로봇산업진흥원 주행 성능 시험)은 제조사와 시험기관 영역이고, ROP 는 그 결과를 로봇 등록·배정 조건의 입력으로 받는 쪽으로 보인다. | ref-638, ref-639, ref-640, ref-641 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-629 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 2025 | 정부·연구기관 | high | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-630 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Scoring | 2025 | 정부·연구기관 | high | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html | 아니오 |
| ref-631 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1807.00048 | 예 |
| ref-632 | Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S. | A Study on Challenges of Testing Robotic Systems | 2020 | 논문 | medium | 2026-09-25 | https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc | 예 |
| ref-633 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/reeceholland/ros2_fault_injection | 아니오 |
| ref-634 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 아니오 |
| ref-635 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-636 | IDM Lab (USC) 게재 초록, 저자 미확인 | The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration] | 2024 | 논문 | medium | 2026-09-25 | https://idm-lab.org/bib/abstracts/Koen24p.html | 예 |
| ref-637 | arXiv 게재 논문(저자 미확인) | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.15721 | 예 |
| ref-638 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-639 | NIST | ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles | 예 |
| ref-640 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 예 |
| ref-641 | 한국로봇산업진흥원(KIRIA) | 시험평가 \| KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kiria.org/rp/kiria/tva/inr/page.dn | 예 |
| ref-642 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 미확인 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-643 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 예 |
| ref-667 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f4(시험·시뮬레이션만으로 불충분), f6(로봇 시험의 어려움), f10(배치 전 반복 시험), f13(격자 가정과 현실 실행의 차이) / 4절 핵심 개념: 장애 주입(f1·f7), 회귀 시험과 CI(f7·f21), 형식 검증·교착(f4·f5), 런타임 검증(f9), 벤치마크(f11·f12) / 5절 현장 시나리오: f22(피킹·완료·인계, 가상 구성안임을 명시), f21(분류 원문 질문, 추정) / 6절 대표 접근법: f1·f3(장애 주입형 시험), f5(BDD 교착 분석), f7·f8(장애 주입 도구), f9(런타임 검증), f10(시뮬레이션 회귀), f13(현실적 MAPF 평가) / 7절 표준·오픈소스: f14(ISO 3691-4), f15(ASTM F45), f16(KS B ISO 18646), f17(한국로봇산업진흥원), f7·f9·f10(오픈소스), f1·f2(NIST ARIAC) / 8절 대표 연구: f4·f5·f6·f11·f12·f13 / 9절 경계: f23(ROP 직접), f8·f14·f15·f16·f24('연계 대상') / 10절 연결: 22. 시뮬레이션·예측용 디지털 트윈(f20), 15. 다중 로봇 경로·교통 관리 — MAPF(f5·f11~f13), 12. 명령·작업 실행의 신뢰성과 19. 모니터링·이상 탐지·원인 분석(f9), 24. 자산·소프트웨어 수명주기 관리(f21, 업데이트 후 재검증), 25. 안전·위험 관리(f14), 9. 로봇·제조사 관제 연동과 28. 표준·상호운용성·다사업자 거버넌스(f18·f19), 20. 예외 복구·재계획·업무 연속성(f13 복구 설계) / 11절 열린 질문: oq-055(f18·f19 부분 근거), oq-058(f13 부분 근거), oq-063, oq-077, open_questions_new 3건. f18 은 [추정]+'벤더 주장' 병기. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 장애 주입 | Fault Injection | 시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다. |
| 회귀 시험 | Regression Testing | 소프트웨어나 설정을 바꾼 뒤 기존에 통과하던 정상·장애 시나리오를 다시 실행해 변경이 기존 동작을 깨뜨리지 않았는지 확인하는 시험이다. |
| 런타임 검증 | Runtime Verification | 실행 중인 시스템의 사건을 감시기로 관찰해 명세한 성질의 위반을 판정하고 기록하거나 차단하는 검증 기법이다. |
| 모델 검사 | Model Checking | 시스템을 상태 전이 모델로 표현하고 교착 부재 같은 성질이 도달 가능한 모든 상태에서 성립하는지 자동으로 확인하는 형식 검증 기법이다. |

## 열린 질문

새로 생긴 질문:

- 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 15. 다중 로봇 경로·교통 관리 — MAPF | 근거: f5 | 종류: 일반
- 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - f5·f11·f12·f13: 논문 원문 미열람, 초록·검색 요약 범위
    - f14: ISO 3691-4 부속서 검증 절차 세부 미확인(유료 표준)
    - f15: F3244 등 개별 ASTM 시험 방법 내용 미확인
    - f16: KS B ISO 18646 각 부의 KS 제정일·판 미확인
    - f18: OTTO 인증의 시험 항목·주체 미확인(벤더 주장)
    - f19: VDA 5050 공식 적합성 시험 절차의 부재 여부 미확인(검색 요약에 VDMA 가 시험 환경을 계획한다는 언급이 있었으나 출처가 명확하지 않아 쓰지 않음)
    - ref-636·ref-637 저자 미확인
    - ref-633 라이선스 미확인
- 범위 경계 위반 의심:
    - f8·f14·f15·f16·f24: 로봇 자체 센서 인식·주행 성능·차량 안전 시험은 분류 원문 9장 '로봇 자체 지능·제어' 쪽 외부 연계 영역이므로 '연계 대상:'으로 표시
    - f22: 가상 시나리오 구성안이며 실제 사례로 서술하지 않도록 claim 에 '시나리오 예시(가상)' 표기
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-629·ref-630(NIST ARIAC 2025 challenges·scoring, 미러 목록 경로), ref-633(ros2_fault_injection), ref-634(ROSMonitoring), ref-667(재사용, Open-RMF 시뮬레이션 장). 나머지 11건은 검색 요약 기준(신뢰도 상한 medium). IntelLabs scenario_execution README raw 경로는 main·jazzy 모두 404 라 출처로 넣지 않았다. League of Robot Runners Start-Kit README 는 열었으나 평가 지표가 없어 쓰지 않았다. 검색 22회/30, 신규 출처 15건/15(ref-629~ref-643, 예약 구간 안)로 신규 출처 예산에 도달해 Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터, arculus VDA 5050 적합성 시험 도구는 출처로 넣지 않았다. 재사용 1건: ref-667(2026-09-25-56 브리프 값 사용). 참고문헌 목록 전체 값이 입력에 없어 ref-007(NIST 협업 로봇 성능)·ref-008(NIST ARIAC)의 기존 값을 재사용하지 못하고 ARIAC 는 개별 페이지 URL 로 새 id 를 붙였다(퍼블리셔 대조 필요). 열린 질문: oq-055 는 f18·f19, oq-058 은 f13 이 부분 근거일 뿐 해결로 보지 않았고, oq-063·oq-077 은 이번에 조사하지 못했다. 한국 자료: KS B ISO 18646(ref-640), 한국로봇산업진흥원(ref-641). 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 섞지 않았고, 22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분은 f20(의견)으로만 냈다. 정정 요청 없음.
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```
