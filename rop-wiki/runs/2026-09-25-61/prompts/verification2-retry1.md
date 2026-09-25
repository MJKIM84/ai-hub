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
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- retry_count: 1
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
        "ref-031"
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
        "ref-031"
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
        "ref-031"
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
        "ref-051"
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
        "ref-051",
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
        "ref-364"
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
        "ref-523"
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
        "ref-403"
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
        "ref-031",
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
        "ref-031",
        "ref-051",
        "ref-364",
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
        "ref-051",
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
        "ref-051",
        "ref-403"
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
        "ref-031"
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
        "ref-523",
        "ref-758",
        "ref-403",
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
      "id": "ref-031",
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
      "id": "ref-051",
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
      "id": "ref-364",
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
      "id": "ref-403",
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
      "id": "ref-523",
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
      "ref-403 저자, ref-031·ref-051·ref-753 발행일 미확인",
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
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-051·ref-364·ref-752·ref-753·ref-760 과 재사용 ref-228·ref-230. 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 17회/30, 신규 출처 15건/15(ref-031~ref-763, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 13374, ISO 10218-1:2025(사이버보안 요구 추가), CISA SBOM, ICAN-Deploy(카나리 배포 프리프린트)는 출처로 넣지 않음. 재사용 3건: ref-228·ref-230(2026-09-25-57 브리프 값), ref-523(2026-09-25-56 브리프 값, 이번에 다시 열지 않음). 교차 확인 0건. 한국 자료: 한국로봇사용자협회 안전인증(ref-762), 세이프틱스 가이드(ref-763, 의견), SDR 과제 보도(ref-761). 27. AI·학습·적응과 모델 운영 관련 finding 없음(모델 버전 관리는 일반 수명주기 관점으로만 다룸). 8·22 구분: f10 은 시뮬레이션 환경의 판 관리로만 서술. 정정 요청 없음, 대상 영역 열린 질문 0건."
  }
}
```

### runs/2026-09-25-61/verification.json

```json
{
  "run_id": "2026-09-25-61",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw VDA5050_EN.md(3.0.0)에서 mapId·mapVersion, downloadMap·enableMap·deleteMap, '한 mapId 한 활성 버전' 문장 확인. 단일 출처. ref-031 는 기존 ref-031 과 같은 URL."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 주 버전=호환성 깨짐(새 비선택 필드), 부=기능, 수=작은 수정, 토픽 예 vda5050/v3/KIT/0001/order 를 원문에서 확인."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 쓸 수 없는 선택 필드가 있는 주문에 UNSUPPORTED_PARAMETER·CRITICAL 보고 규정을 원문에서 확인. '판 차이로 생긴 미지원 기능이 드러난다'는 해석 부분은 본문에서 해석임을 밝힌다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw factsheet.schema 에서 mobileRobotConfiguration.versions(key–value, softwareVersion 등 예)와 batteryCharging 네 필드 확인."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw state.schema 에서 powerSupply(stateOfCharge·batteryHealth·charging·range)와 maps(mapId·mapVersion·mapStatus ENABLED/DISABLED) 확인. ref-051 은 기존 ref-051 과 같은 URL."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw AMR_Interop_Standard.json 의 identityReport·statusReport 속성 목록을 직접 대조했고 소프트웨어·펌웨어 버전 필드가 없음을 확인. [추정] 유지(태그를 올리지 않음)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f4·f5·f6 스키마 비교에서 나온 추론으로 [추정] 적정."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw node_lifecycle.md 에서 주 상태 4개·전이 상태 6개와 '실행 전 올바른 초기화 확인, 온라인 재시작·교체' 문장 확인. 용어집 managed-node 기존 항목 재사용."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw rep-2000.rst 에서 LTS 5년·비LTS 1.5년, Humble 2022-05~2027-05, Jazzy 2024-05~2029-05, Kilted 2025-05~2026-11 확인. Kilted 는 실행일 기준 약 2개월 뒤 지원 종료이므로 기준일을 명시."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): rmf_simulation 이 Gazebo Classic 11·Fortress 를 지원한다는 문구가 있음. Gazebo Classic 지원 종료(2025-01-31)는 Open Robotics Discourse 검색 결과에서도 보였으나 같은 기관 계열이라 독립 교차 확인으로 보지 않음."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README(IDTA 2007-1-0)에서 목적(updates, patch management, license management, audits)과 Version(주·부·개정·빌드), ReleaseDate·BuildDate·InstallationDate, InstallationPath·InstallationChecksum·InstalledVersion·ConfigurationPaths 속성 확인."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): 상태 감시 프로그램 수립의 일반 절차 지침, 진동·온도·트라이볼로지·유량·오염·전력·속도, 관련 표준 참조. 제3판 2018-01(2011판 대체)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검색 결과로 일부 확인(원문 미열람): 제2판 2024-07, ISO/TC 251, 2014판 대체, 용어·개요·원칙, 모든 유형의 자산에 적용. '하드웨어·소프트웨어·설비를 포함'과 '수명주기 단계별로 자산의 필요와 성능을 평가'는 검색 결과에서 확인되지 않음 → 확인한 부분만 [사실]로 두고 나머지 구절은 삭제."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): Lei Yaguo·Liu Huan·Li Naipeng 외, Sci China Tech Sci 68권 1호(2025), 고장 모드·근본 원인, 데이터 수집·센서, 모델 기반·데이터 기반 방법, 상태 기반 정비."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): arXiv 2603.22731(2026-03-24), 작업 배정·순서·충전 모드·공용 충전기 조율을 함께 다루는 MILP와 열화 균형 페널티. 사이클 열화·달력 열화 문장은 브리프 발췌 기준. 저자 미확인. 프리프린트(동료 심사 전)임을 밝힌다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): 패치 관리 프로그램을 운영하는 자산 소유자와 공급자에 대한 요구, 패치 정보 형식, 개발·배포·설치 활동, 보안 외 패치에도 적용될 수 있음. 제1판 2015-06, 발행 2년 경과로 월간 재검증 대상."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검색 결과로 확인(원문 미열람): 적용일 2027-01-20, 물리적·디지털 변경 정의는 확인. 그러나 정의에는 '제조사가 예견·계획하지 않은' 변경이라는 조건이 있고, 여러 해설은 제조사가 예견한 업데이트는 원칙적으로 실질적 변경이 아니라고 적는다. 브리프는 이 조건을 빼고 일반화함 → 정의 문장은 조건을 넣어 [사실]로 두고, '소프트웨어 업데이트가 판단 대상' 부분은 [추정]으로 분리."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README 에서 IoT Jobs·Greengrass v2·Docker, 플릿 색인의 firmwareVersion 조회, 자동 롤백 문구(이점으로 나열됨) 확인. 다만 '운영용이 아닌 참조 구현'이라는 명시는 README 에 없고, 자동 롤백의 구현 절차도 나와 있지 않음 → 문구 수정. [추정]+벤더 주장 유지."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검색 결과로 확인(원문 미열람): 2026-07-22 판교(경기스타트업캠퍼스) 3차년도 킥오프, KIST 주관, 클라우드 기반 SDR 공통 서비스 프레임워크. 검색 결과상 주관 조직명은 '휴머노이드연구단'이며 브리프의 '휴머노이드연구센터'와 다름. OTA 목표는 기사 제목 수준에서만 확인됨. 원 매체를 모르는 기사 단일 출처 → 사실에서 추정으로."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): doc.safetics.io '로봇 시스템 위험성평가 가이드' 실재, 같은 모델로 교체해도 펌웨어·안전 파라미터·엔드이펙터 정밀도가 바뀌면 재평가·문서 갱신이 필요하다는 문장 확인. 벤더(세이프틱스) 권고로서 [의견] 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): korua.or.kr 안내에 (KS B) ISO 10218-2 적합성 심사와 발급일로부터 2년 주기 정기 심사가 있음. 펌웨어 변경 시 재심사 여부는 미확인(열린 질문으로 처리)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f2·f4·f11·f20 을 근거로 한 추론이며 '공개 절차를 찾지 못했다'는 한계를 밝혀 [추정] 적정. 원문 SCM 질문을 다룬다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: [추정]으로 적정. 단 '운영 시간대·일부 로봇 단위 분할 배포'는 어느 출처에도 직접 근거가 없는 구축자 추론이므로 본문에서 그렇게 밝힌다. ref-760 은 벤더 주장."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '연계 대상:'으로 표시했고 분류 원문 9장 '로봇 자체 지능·제어' 경계와 맞다. [추정] 적정."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: batteryHealth·range 필드(f5)와 f15 에서 나온 시나리오 추정. 실측 자료가 없다는 점을 [추정]으로 밝힘. 출하/제약."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f1 규칙에서 나온 시나리오 추정. 적치/시작 조건."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 영역 연결에 관한 [의견]. 누구의 의견인지(구축자 의견) 밝혀야 함."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f14·f15·f24: 부품 고장 진단·BMS 내부 열화 추정은 '로봇 자체 지능·제어' 쪽 연계 대상이다. 브리프가 이미 이렇게 표시했으므로 9절에서 연계 대상으로 짧게 유지한다(위반 아님, 주의 사항)"
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "ref-031(VDA5050_EN.md)의 URL이 기존 ref-031(2026-09-25-60 브리프)과 같다",
      "ref-051(json_schemas/state.schema)의 URL이 기존 ref-051 과 같다",
      "새 열린 질문 '펌웨어 변경 영향 범위 산정 절차'(f22)가 2026-09-25-59 브리프의 새 질문 '업데이트 후 회귀 시험 최소 장애 시나리오 집합'(관련 영역: 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리)과 인접한다. 뜻은 다르다(영향 범위와 시험 집합)"
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
    "ref-031·ref-051: 각주와 reference_updates 에서 새 id 대신 URL이 같은 기존 ref-031(VDA5050_EN.md)과 ref-051(state.schema)을 재사용한다 — 같은 출처가 이미 등록돼 있다(ref-031·ref-051 은 참고문헌에 새로 등록하지 않는다).",
    "f13: 확인된 부분(ISO 55000:2024 제2판, 2024-07, ISO/TC 251, 2014판 대체, 자산 관리의 용어·개요·원칙, 모든 유형의 자산에 적용)만 [사실]로 쓰고, '하드웨어·소프트웨어·설비를 포함'과 '수명주기 단계별로 자산의 필요와 성능을 평가' 구절은 삭제한다 — 검색 결과에서 확인되지 않았다.",
    "f17: 실질적 변경 정의 문장에 '제조사가 예견·계획하지 않은' 변경이라는 조건을 넣어 [사실]로 쓰고, '동작을 바꾸는 소프트웨어 업데이트가 판단 대상이 될 수 있다'는 부분은 [추정]으로 떼어 쓴다 — 브리프가 정의의 조건을 빼고 일반화했다.",
    "f18: '운영용이 아닌 참조 구현' 대신 'aws-samples 저장소의 시연용 샘플'로 고쳐 쓰고, 자동 롤백은 README가 이점으로 나열한 것일 뿐 구현 절차는 보이지 않는다고 밝힌다. [추정]과 '벤더 주장' 병기는 유지한다 — README에 운영용 여부가 명시돼 있지 않다.",
    "f19: [사실]을 [추정]으로 강등하고 주관 조직명을 'KIST 휴머노이드연구단'으로 고친다 — 원 매체를 모르는 기사 단일 출처이고, 검색 결과의 조직명이 브리프와 다르다.",
    "f27: [의견]에 '구축자 의견'임을 밝힌다 — 누구의 의견인지 표시해야 한다.",
    "f23: '업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포' 부분이 출처에 직접 근거가 없는 추론임을 본문에서 밝힌다(태그 [추정] 유지).",
    "f15: 본문에서 프리프린트(동료 심사 전)이고 저자가 미확인임을 밝힌다.",
    "f9: Kilted 지원 종료(2026-11)가 실행일 기준 약 2개월 뒤임을 기준일 2026-09-25 와 함께 적는다 — 곧 바뀌는 사실이다.",
    "원문 미열람 출처 ref-754·ref-755·ref-403·ref-757·ref-758·ref-759·ref-761·ref-762·ref-763·ref-523: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다(web_fetch_available: false).",
    "페이지 confidence 는 medium 을 넘기지 않는다. 각 finding 의 태그는 이번 판정의 태그 처분을 그대로 따른다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다(raw.githubusercontent.com 미러만 열 수 있음). 확인 25건, 미확인 2건(f13·f17, 출처가 주장의 일부만 뒷받침), 교차 확인 0건. 강등: f13 사실 → 확인된 부분만 사실로 두고 나머지 구절 삭제, f17 사실 → 정의는 조건을 넣어 사실로 두고 적용 해석은 추정으로 분리, f19 사실 → 추정. 원문 미열람 출처: ref-754, ref-755, ref-403, ref-757, ref-758, ref-759, ref-761, ref-762, ref-763, ref-523. 원문을 연 출처: ref-031(=ref-031), ref-051(=ref-051), ref-228, ref-230, ref-364, ref-752, ref-753, ref-760(GitHub 원문). 주의: 모든 핵심 주장이 단일 출처이고, 펌웨어 변경의 영향 범위를 산정하는 공개 절차는 확인되지 않았다(f22 추정). EU 기계 규정의 실질적 변경은 제조사가 예견하지 않은 변경에 한정된다. f18 은 벤더 주장이다. 국내 인증에서 펌웨어 변경이 재심사 대상인지는 미확인이다. 정정 요청 없음. 검증 검색은 10회 썼다(리서치 17회와 합쳐 27/30).",
  "retry_reason": null
}
```

### runs/2026-09-25-61/pages.json

```json
{
  "run_id": "2026-09-25-61",
  "outline": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "펌웨어 변경의 재검증 범위를 산정하는 공개 절차는 찾지 못했고, 배포판 지원 종료·시뮬레이터 교체·EU 기계 규정의 실질적 변경·국내 재평가 권고가 수명주기 관리를 강제한다. [추정][^ref-031]",
      "planned_findings": [
        "f22",
        "f9",
        "f10",
        "f17",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 650,
      "summary": "자산 관리(ISO 55000:2024), 상태 감시(ISO 17359), 배터리 건강 상태(batteryHealth), 소프트웨어 명판, 패치 관리, 의미적 버전·지도 버전, 관리형 노드가 핵심 용어다. [사실][^ref-755]",
      "planned_findings": [
        "f13",
        "f12",
        "f14",
        "f5",
        "f11",
        "f16",
        "f2",
        "f1",
        "f8"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 700,
      "summary": "적치 구역 지도 버전 전환과 출하 마감 전 배터리 열화 로봇 배정의 두 가상 시나리오로, 지도 활성화 규칙과 batteryHealth·range 가 시작 조건·제약이 되는 모습을 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f26",
        "f1",
        "f5",
        "f3",
        "f25",
        "f23"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 800,
      "summary": "부품 상태 감시·고장 진단, 배터리 열화를 반영한 배정·충전, 버전 필드 관리, 관리형 노드와 OTA 배포·복구가 대표 접근법이다. [사실][^ref-757]",
      "planned_findings": [
        "f14",
        "f15",
        "f4",
        "f6",
        "f8",
        "f18",
        "f19",
        "f1",
        "f24"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 500,
      "summary": "이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [추정][^ref-031][^ref-753][^ref-758]",
      "planned_findings": [
        "f1",
        "f4",
        "f5",
        "f6",
        "f11",
        "f12",
        "f13",
        "f16",
        "f8",
        "f9",
        "f10",
        "f21"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 450,
      "summary": "대표 연구를 부품 상태 감시 검토와 배터리 열화 인지 스케줄링으로 나누는 것은 구축자 의견이다. [의견][^ref-757][^ref-403]",
      "planned_findings": [
        "f14",
        "f15",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 500,
      "summary": "ROP 는 버전 목록 유지·배터리 상태 반영·배포 복구 조율·지도 전환 동기화를 맡고, 펌웨어 내용·부품 진단·BMS 열화 추정은 제조사 쪽 연계 대상으로 보인다. [추정][^ref-051]",
      "planned_findings": [
        "f23",
        "f24",
        "f7"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 450,
      "summary": "시험·시뮬레이션·보안·안전·충전·배정·모니터링·온보딩·관제 연동·표준·지도 영역과 이어진다는 것이 구축자 의견이다. [의견][^ref-403]",
      "planned_findings": [
        "f27",
        "f7",
        "f4",
        "f26",
        "f15",
        "f14"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "section": "11. 열린 질문",
      "budget_chars": 300,
      "summary": "영향 범위 산정 절차, VDA 5050 판 혼재 운영, 국내 인증의 펌웨어 변경 재심사, EU 실질적 변경의 오케스트레이션 적용 여부가 열린 질문이다.",
      "planned_findings": [
        "f22",
        "f2",
        "f21",
        "f17"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가. 2차 수정: 7절 첫 문장 [추정]·각주 보강, 8절 대표 연구 분류·평가 [의견]화, 8절 ref-760 항목 롤백 문구 정정"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area24-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 \"4. 핵심 개념과 용어\" 절(1,365자)을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area24-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 \"6. 대표 접근법과 기술\" 절(1,327자)을 옮겼다. 2차 수정: 부품 진단 연계 대상 문장을 [추정]과 각주로 고치고, 5·9절 참조를 원 세부영역 페이지 절 링크로 바꿈"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area24-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 \"3. 왜 중요한가\" 절(1,019자)을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area24-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(982자)을 옮겼다. 2차 수정: 1절 요약과 3절 첫 문장의 태그를 [추정]으로 낮추고 각주를 ref-031·ref-753·ref-758 로 바꿈"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area24-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 \"10. 다른 연구영역과의 연결\" 절(731자)을 옮겼다. 형식 수정: 본문 링크 11건을 주제 페이지 위치 기준 경로로 고침(2차 수정 없음)"
    }
  ],
  "changelog_entry": "2026-09-25 | 24. 자산·소프트웨어 수명주기 관리 | 영역 심화: 3~11절 신규 작성(버전·지도·배터리 열화·배포 복구·변경 후 재평가, 적치·출하 가상 시나리오) | run 2026-09-25-61",
  "index_updates": {
    "home_recent": "2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 영역 심화로 3~11절 첫 작성(펌웨어·지도 버전, 배터리 건강 상태, 배포·복구, 변경 후 재평가)",
    "category_recent": "2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 영역 심화로 3~11절 첫 작성, 열린 질문 4건 등록",
    "area_recent": "2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 3~11절 신규 작성(실행 2026-09-25-61)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "condition-based-maintenance",
      "term_ko": "상태 기반 정비",
      "term_en": "Condition-Based Maintenance (CBM)",
      "definition": "정해진 주기 대신 상태 감시로 확인한 설비 상태에 따라 정비 여부와 시점을 정하는 정비 방식이다.",
      "description": "산업용 로봇 분야에서는 고장 모드 분석, 데이터 수집·센서, 모델 기반·데이터 기반 상태 감시·고장 진단 기법이 상태 기반 정비 구현 관점에서 정리돼 있다.",
      "related_areas": [
        24,
        19
      ],
      "sources": [
        "ref-757",
        "ref-754"
      ]
    },
    {
      "action": "new",
      "slug": "state-of-health",
      "term_ko": "배터리 건강 상태",
      "term_en": "State of Health (SOH)",
      "definition": "배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다.",
      "description": "VDA 5050 상태 스키마는 충전 상태(stateOfCharge)와 별도로 batteryHealth 와 추정 도달 거리(range)를 로봇이 보고하게 한다.",
      "related_areas": [
        24,
        16
      ],
      "sources": [
        "ref-051"
      ]
    },
    {
      "action": "new",
      "slug": "software-nameplate",
      "term_ko": "소프트웨어 명판",
      "term_en": "Software Nameplate (IDTA 02007)",
      "definition": "자산관리셸에서 소프트웨어 제품과 설치 인스턴스의 식별·버전·설치 정보를 통일된 형태로 기술하는 서브모델이다.",
      "description": "업데이트·패치 관리·라이선스 관리·감사를 목적으로 하며 버전(주·부·개정·빌드), 배포일·빌드일·설치일, 설치 경로·체크섬 같은 속성을 둔다.",
      "related_areas": [
        24,
        28
      ],
      "sources": [
        "ref-753"
      ]
    },
    {
      "action": "new",
      "slug": "over-the-air-update",
      "term_ko": "무선 업데이트",
      "term_en": "Over-the-Air Update (OTA)",
      "definition": "기기를 회수하지 않고 네트워크로 소프트웨어·펌웨어를 내려받아 갱신하는 방식이다.",
      "description": "로봇 플릿용 시연 샘플과 국내 SDR 과제 보도에서 다뤄졌다. 롤백 등 기능 주장은 벤더 주장 수준이다.",
      "related_areas": [
        24
      ],
      "sources": [
        "ref-760",
        "ref-761"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 의미적 버전 규칙, 토픽의 주 버전, 지도 배포·버전(downloadMap·enableMap·deleteMap), 미지원 파라미터 오류 규정 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. powerSupply(stateOfCharge·batteryHealth·charging·range)와 maps(mapId·mapVersion·mapStatus) 필드 확인.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
    },
    {
      "id": "ref-523",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_simulation — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_simulation",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 시뮬레이션 플러그인 저장소 README(이번 실행에서 다시 열지 않음, 2026-09-25-56 확인 내용 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
    },
    {
      "id": "ref-364",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "Managed nodes (ROS 2 Design: node_lifecycle)",
      "published": null,
      "url": "https://design.ros2.org/articles/node_lifecycle.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 관리형 노드의 주 상태·전이 상태·전이와 목적(초기화 확인, 실행 중 교체·재시작) 설계 문서.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "cited_by": [
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "summary": "원문 미열람. 자산 관리 용어·개요·원칙 제2판(ISO/TC 251, 2014 판 대체), 모든 유형의 자산에 적용.",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
    },
    {
      "id": "ref-403",
      "org": "arXiv (저자 미확인)",
      "title": "Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.22731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AMR 플릿의 작업 배정·충전을 배터리 열화 균형과 함께 최적화하는 프리프린트(동료 심사 전).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
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
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s6.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
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
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s4.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
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
      "summary": "원문 미열람. EU 기계 규정. 2027-01-20 적용, 제조사가 예견·계획하지 않은 물리적·디지털 변경을 포함한 실질적 변경 정의.",
      "source_unopened": true,
      "cited_by": [
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s7.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
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
      "summary": "aws-samples 저장소의 ROS 2 플릿 무선 펌웨어 업데이트 시연용 샘플(IoT Jobs·Greengrass·Docker, 버전 조회, 자동 롤백을 이점으로 나열).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s6.md"
      ]
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
      "summary": "원문 미열람. SDR 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍(KIST 휴머노이드연구단)과 클라우드 기반 OTA 목표 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s6.md"
      ]
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
      "cited_by": [
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s7.md"
      ]
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
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
        "docs/topics/2026/2026-09-25-area24-s3.md",
        "docs/topics/2026/2026-09-25-area24-s10.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가?",
      "areas": [
        24,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가?",
      "areas": [
        24,
        9,
        28
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가?",
      "areas": [
        24,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가?",
      "areas": [
        24,
        25
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "적치",
      "item": "시작 조건",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "적치",
      "item": "수행 자원",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "적치",
      "item": "제약",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "적치",
      "item": "완료·인계",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "적치",
      "item": "예외·성과",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "출하",
      "item": "수행 자원",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    },
    {
      "step": "출하",
      "item": "제약",
      "link": "docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md",
      "title": "24. 자산·소프트웨어 수명주기 관리"
    }
  ],
  "standards_updates": [
    {
      "name": "IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0)",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md",
      "related_areas": [
        24,
        28
      ],
      "summary": "자산관리셸 서브모델로 소프트웨어 제품과 설치 인스턴스의 버전·설치 정보를 업데이트·패치·라이선스·감사 목적으로 통일해 표현한다.",
      "ref_id": "ref-753"
    },
    {
      "name": "ISO 17359:2018 기계 상태 감시·진단 일반 지침",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/71194.html",
      "related_areas": [
        24,
        19
      ],
      "summary": "기계의 상태 감시 프로그램 수립 일반 절차 지침이며 상태 감시·진단 표준군의 상위 문서다(원문 미열람).",
      "ref_id": "ref-754"
    },
    {
      "name": "ISO 55000:2024 자산 관리 — 용어·개요·원칙",
      "kind": "표준",
      "org": "ISO (ISO/TC 251)",
      "url": "https://www.iso.org/standard/83053.html",
      "related_areas": [
        24
      ],
      "summary": "자산 관리의 용어·개요·원칙을 정한 제2판(2024-07)으로 2014판을 대체하며 모든 유형의 자산에 적용된다(원문 미열람).",
      "ref_id": "ref-755"
    },
    {
      "name": "IEC TR 62443-2-3:2015 IACS 환경의 패치 관리",
      "kind": "표준",
      "org": "IEC",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "related_areas": [
        24,
        26
      ],
      "summary": "산업 제어 시스템 패치 관리 프로그램의 자산 소유자·공급자 요구와 패치 정보 교환 형식을 정의한다(원문 미열람).",
      "ref_id": "ref-758"
    },
    {
      "name": "REP 2000 ROS 2 Releases and Target Platforms",
      "kind": "프레임워크",
      "org": "Open Robotics (ROS REP)",
      "url": "https://www.ros.org/reps/rep-2000.html",
      "related_areas": [
        24
      ],
      "summary": "ROS 2 배포판별 출시·지원 종료 일정과 장기 지원판 5년·비장기 지원판 1.5년 지원 정책을 정한다.",
      "ref_id": "ref-752"
    },
    {
      "name": "rmf_simulation (Open-RMF 시뮬레이션 플러그인)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_simulation",
      "related_areas": [
        22,
        24
      ],
      "summary": "Open-RMF 시뮬레이션 플러그인 저장소로 Gazebo Classic 11과 Gazebo Fortress 를 지원 대상으로 적는다(원문 미열람).",
      "ref_id": "ref-523"
    },
    {
      "name": "협동로봇 설치 작업장 안전인증",
      "kind": "평가 프로그램",
      "org": "한국로봇사용자협회",
      "url": "https://www.korua.or.kr/inspect/inspectInfo.do",
      "related_areas": [
        25,
        24
      ],
      "summary": "협동운전 산업용 로봇 시스템의 ISO 10218-2 준수를 심사하고 발급일로부터 2년 주기로 정기 심사한다(원문 미열람).",
      "ref_id": "ref-762"
    }
  ],
  "additional_research_requests": [
    "4절: 예지보전(Predictive Maintenance) 정의를 뒷받침할 출처가 브리프에 없어 본문·용어집에 넣지 못했다 — 표준·검토 논문 출처로 정의를 확인해 달라.",
    "전 절: 모든 핵심 주장이 단일 출처이므로 교차 확인이 필요하다(특히 REP 2000 지원 기간, VDA 5050 버전·지도 규칙, IDTA 02007 속성). 페이지 신뢰도를 높이려면 독립 출처가 필요하다.",
    "3절·11절: EU 기계 규정에서 제조사가 예견한 소프트웨어 업데이트의 취급(실질적 변경 제외 여부)을 조문 원문이나 EU 공식 지침으로 확인해 달라 — 브리프에는 정의 조건만 있다.",
    "3절·11절: 국내 협동로봇 설치 작업장 안전인증에서 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정 원문 확인이 필요하다.",
    "6절·7절: 신규 출처 예산 도달로 빠진 ISO 13374, ISO 10218-1:2025 사이버보안 요구, CISA SBOM, 카나리 배포 연구를 다음 실행에서 조사해 달라.",
    "9절: '업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포'하는 방식의 근거(단계적 배포·카나리 배포의 로봇 플릿 적용 사례)가 없어 구축자 추론으로만 남겼다.",
    "5절: 적치·출하 시나리오의 작업 대상과 출하 시작 조건을 뒷받침할 물류 현장 자료가 없어 흐름 매트릭스 연결에서 뺐다 — 지도 전환·배터리 열화가 실제 물류센터 작업에 미친 사례를 조사해 달라.",
    "운영: 자동 분리 주제 페이지 9절의 '1차·2차 검증을 거쳤다'는 고정 문구는 2차 통과 전에는 사실이 아니므로 퍼블리셔 담당이 문구 생성 시점을 확인해 달라."
  ],
  "fixes_applied": [
    "ref-031·ref-051 재사용 지시 — 본문 각주와 13절 정의, sources, reference_updates 에서 URL 이 같은 기존 ref-031(VDA5050_EN.md)과 ref-051(state.schema)을 그대로 쓰고 새 id 로 등록하지 않았다.",
    "f13 축소 지시 — 4절 '자산 관리' 항목에 제2판·2024-07·ISO/TC 251·2014판 대체·용어·개요·원칙·모든 유형의 자산 적용만 [사실]로 쓰고 '하드웨어·소프트웨어·설비 포함'과 '수명주기 단계별 평가' 구절은 넣지 않았다.",
    "f17 분리 지시 — 3절에 '제조사가 예견·계획하지 않은' 조건을 넣은 실질적 변경 정의를 [사실]로, 소프트웨어 업데이트가 판단 대상이 될 수 있다는 부분을 별도 문장 [추정]으로 썼다.",
    "f18 문구 수정 지시 — 6절·8절에서 'aws-samples 저장소의 시연용 샘플'로 쓰고 자동 롤백은 README 가 이점으로 나열할 뿐 구현 절차는 보이지 않는다고 밝혔으며 [추정]과 '벤더 주장'을 유지했다.",
    "f19 강등 지시 — 6절·8절에서 [추정]으로 쓰고 주관 조직명을 'KIST 휴머노이드연구단'으로 고쳤으며 원 매체 미확인을 병기했다.",
    "f27 의견 주체 표시 지시 — 10절 첫 문장에 '구축자 의견'임을 밝히고 각 연결 항목을 [의견]으로 두었다.",
    "f23 추론 표시 지시 — 9절 표 아래에 '운영 시간대·일부 로봇 단위 분할 배포'가 확인한 출처에 직접 근거가 없는 구축자 추론이라고 밝히고 [추정]을 유지했다.",
    "f15 프리프린트 표시 지시 — 6절과 8절에 arXiv 프리프린트(동료 심사 전)이며 저자 미확인임을 적었다.",
    "f9 기준일 지시 — 3절에 Kilted 지원 종료(2026-11)가 기준일 2026-09-25 에서 약 2개월 뒤라는 문장을 더했다.",
    "원문 미열람 표시 지시 — ref-754·ref-755·ref-403·ref-757·ref-758·ref-759·ref-761·ref-762·ref-763·ref-523 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.",
    "신뢰도·태그 지시 — 프런트매터 confidence 를 medium 으로 두고 각 finding 의 태그를 1차 판정 처분(f13·f17 부분 강등, f19 강등, 나머지 유지)대로 썼다.",
    "분량 초과 자동 분리: 24. 자산·소프트웨어 수명주기 관리 본문 8,444자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,733자",
    "형식 검증 수정: 주제 페이지 2026-09-25-area24-s10.md 3절의 세부영역 링크 11건이 원 세부영역 페이지 기준 상대 경로로 남아 깨졌으므로 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤다. 원 세부영역 페이지 프런트매터 sources 를 13절 각주 정의 목록과 일치시켰다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: 8절 ref-760 항목 롤백 문구 — 세부영역 8절 항목을 'aws-samples 저장소의 시연용 샘플로 플릿 OTA 배포·버전 조회를 보이며, 자동 롤백은 README가 이점으로 나열할 뿐 구현 절차는 보이지 않는다'로 고치고 [추정]과 '벤더 주장' 병기를 유지했다.",
    "2차: 7절 첫 문장 태그·각주 — 세부영역 7절과 주제 페이지 2026-09-25-area24-s7.md 1절·3절의 같은 문장을 [추정][^ref-031][^ref-753][^ref-758]로 바꿨다(두 페이지 모두 sources·각주 정의에 ref-753·ref-758 이 이미 있다).",
    "2차: 8절 대표 연구 분류·평가 — 8절 첫 문장을 '대표 연구를 … 나누는 것은 구축자 의견이다. [의견][^ref-757][^ref-403]'로, Lei 외 항목의 '배경 자료' 문장을 '구축자 의견이다. [의견]'인 별도 문장으로 바꾸고 논문 내용 문장만 [사실][^ref-757]로 남겼다.",
    "2차: 6절 분리 페이지 연계 대상 문장과 절 참조 — 2026-09-25-area24-s6.md 3절 '부품 상태 감시와 고장 진단' 소절을 '부품 진단 자체는 로봇 제조사 쪽 연계 대상으로 보인다. [추정][^ref-757]'로 고치고, '9절에서 다룬다'와 '5절의 적치 시나리오'를 원 세부영역 페이지의 9절·5절 링크로 바꿨다. 같은 원칙으로 s7 페이지의 '(3절)' 참조도 3절 분리 주제 페이지 링크로 바꿨다.",
    "2차: flow_matrix_updates 정리 — 적치/작업 대상, 출하/시작 조건, 출하/작업 대상 세 항목을 뺐다(남은 7칸은 5절 끝 문장의 관여 칸 목록과 같다)."
  ]
}
```

### runs/2026-09-25-61/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-61/pages/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리"
type: area
category: "F. 도입·검증·유지관리"
area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [펌웨어 버전 관리, 지도 버전, 배터리 건강 상태, 상태 감시, 패치 관리, 무선 업데이트]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-051, ref-228, ref-230, ref-523, ref-364, ref-753, ref-403, ref-757, ref-758, ref-760, ref-761, ref-763]
last_run: 2026-09-25
version: 2
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

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [분류원문]

## 2. SCM 관점의 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]

## 3. 왜 중요한가

펌웨어가 바뀔 때 다시 검증할 범위를 정하려면 로봇별 소프트웨어 버전을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전·기능 선언·안전 파라미터·지도 버전의 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 이번 조사(2026-09-25 기준)에서 찾지 못했다. [추정][^ref-031][^ref-228][^ref-753][^ref-763]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area24-s3.md)에 있다.

## 4. 핵심 개념과 용어

수명주기 관리를 이야기하려면 먼저 무엇을 자산으로 보고, 그 상태와 버전을 어떤 이름으로 부르는지 정해야 한다.

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

다음은 설명을 위한 가상의 시나리오 두 개이다. 지도 버전 전환 규칙과 배터리 상태 보고 필드가 적치의 시작 조건과 출하의 제약으로 어떻게 작용하는지를 보인다. [추정][^ref-031][^ref-051]

### 적치: 랙 배치 변경 뒤 새 지도 버전으로 작업 재개

**물류 흐름 단계:** 적치

**시나리오:** 랙 배치 변경 뒤 새 지도 버전으로 적치 작업 재개

| 항목 | 내용 |
|---|---|
| 시작 조건 | 랙 배치가 바뀌어 새 지도 버전이 나오면, 진행 중 적치 주문을 정리하고 지도 전환 시점을 정하는 일이 적치 재개의 시작 조건이 되는 것으로 보인다. [추정][^ref-031] |
| 작업 대상 | 입고 뒤 적치할 팔레트·박스(가상) |
| 수행 자원 | 플릿 제어가 즉시 동작 downloadMap·enableMap 으로 지도 내려받기·활성화를 지시하고 [사실][^ref-031], 로봇은 상태 메시지로 mapId·mapVersion·mapStatus 를 보고한다. [사실][^ref-051] |
| 제약 | 같은 mapId 에서는 한 번에 한 버전만 활성화된다. [사실][^ref-031] |
| 완료·인계 | 로봇이 보고한 새 mapVersion 의 mapStatus 가 ENABLED 인지 확인한 뒤 적치 주문을 재개한다(이 시나리오의 가정). mapStatus 는 ENABLED 또는 DISABLED 값을 가진다. [사실][^ref-051] |
| 예외·성과 | 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 오류를 CRITICAL 수준으로 보고하도록 규정돼 있다. [사실][^ref-031] 이 규정 때문에 판 차이로 생긴 미지원 기능이 실행 시점 오류로 드러난다고 해석할 수 있다. [추정][^ref-031] |

### 출하: 마감 전 배터리 열화 로봇의 배정

**물류 흐름 단계:** 출하

**시나리오:** 출하 마감 전 집중 시간대에 배터리 상태가 낮아진 로봇 배정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 전 집중 시간대에 출하 주문이 몰린다(가상). |
| 작업 대상 | 출하 대기 구역으로 옮길 화물(가상) |
| 수행 자원 | 로봇은 stateOfCharge·batteryHealth·range 를 보고하고 [사실][^ref-051], ROP 는 이 값을 작업 배정·충전 계획에 반영하는 쪽으로 보인다. [추정][^ref-051] |
| 제약 | batteryHealth 가 낮아진 로봇은 같은 충전 상태에서도 추정 도달 거리(range)가 짧아질 수 있어, 배터리 열화가 작업 배정·충전 계획의 제약으로 작용하는 것으로 보인다(물류센터 실측 자료는 미확인). [추정][^ref-051][^ref-403] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

두 시나리오에서 이 영역이 관여하는 칸은 적치의 시작 조건·수행 자원·제약·완료·인계·예외·성과와 출하의 수행 자원·제약이다. 전체 흐름은 [흐름 매트릭스](../../flow-matrix.md)에서 본다.

## 6. 대표 접근법과 기술

산업용 로봇의 상태 감시·고장 진단은 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 기법으로 정리돼 있다. [사실][^ref-757]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [추정][^ref-031][^ref-753][^ref-758] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area24-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 대표 연구를 부품 상태 감시 검토와 배터리 열화 인지 스케줄링으로 나누는 것은 구축자 의견이다. [의견][^ref-757][^ref-403]

- Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review(2025) — 산업용 로봇의 고장 모드·데이터 수집·모델 기반·데이터 기반 진단을 상태 기반 정비 관점에서 정리했다. [사실][^ref-757] 이 논문이 ROP 가 받을 정비 신호의 출처를 이해하는 배경 자료라는 것은 구축자 의견이다. [의견]
- 저자 미확인, Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots(2026-03, arXiv 프리프린트, 동료 심사 전) — 작업 배정·충전을 플릿 전체 배터리 열화 균형과 함께 최적화한다. [사실][^ref-403]
- Amazon Web Services, ros2-ota-firmware-updates README — aws-samples 저장소의 시연용 샘플로 플릿 OTA 배포·버전 조회를 보이며, 자동 롤백은 README가 이점으로 나열할 뿐 구현 절차는 보이지 않는다. [추정] 벤더 주장[^ref-760]
- SDR 과제 킥오프 워크숍 보도(2026-07-23) — 국내 클라우드 기반 OTA 목표 사례다. [추정][^ref-761]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP 는 버전 목록·배터리 상태·배포 복구·지도 전환을 조율하고, 펌웨어 내용과 부품·배터리 내부 진단은 제조사 쪽에 두는 것으로 보인다. [추정][^ref-051][^ref-757]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇·어댑터·지도·모델의 버전 목록 유지, 로봇이 보고하는 배터리 상태·오류를 배정·충전 계획에 반영, 업데이트 배포와 실패 시 복구 조율, 지도 버전 활성화 시점 동기화 [추정][^ref-031][^ref-051][^ref-364][^ref-760] | 연계 대상: 펌웨어 내용 자체, 관절·감속기 같은 기계 부품의 고장 진단·잔여 수명 예측, 배터리 관리 시스템(Battery Management System, BMS) 내부의 열화 추정. ROP 는 그 결과(배터리 상태 값·오류 코드·정비 필요 신호)를 받는 쪽으로 보인다. [추정][^ref-757][^ref-051][^ref-230] |

업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포하는 방식도 ROP 가 조율할 후보로 보이지만, 이 부분은 확인한 출처에 직접 근거가 없는 구축자 추론이다. [추정]

분류 원문 9장은 이 경계가 제품 전략에 따라 이동할 수 있고, 이종 제조사를 연결하는 ROP 는 "인터페이스와 실행 보장"을 맡을 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 규격마다 버전 필드의 위치가 달라(VDA 5050 은 팩트시트에 소프트웨어 버전, 상태 메시지에 지도 버전을 두고 MassRobotics 스키마는 버전 필드가 없다) 여러 규격이 섞인 플릿에서는 ROP 가 로봇별 버전 목록을 별도로 유지해야 할 것으로 보인다. [추정][^ref-228][^ref-051][^ref-230]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아래 연결은 이번 조사 결과를 바탕으로 한 구축자 의견이다. [의견][^ref-523][^ref-758][^ref-403][^ref-763]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area24-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 새로 올린 질문이며 id 는 퍼블리셔가 부여한다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: Open Robotics (ROS 2 Design), Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-753]: IDTA (admin-shell-io/id GitHub), IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing), 미확인, https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md, 접근일 2026-09-25
[^ref-403]: arXiv (저자 미확인), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-757]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-758]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-760]: Amazon Web Services (aws-samples GitHub), ros2-ota-firmware-updates — README, 미확인, https://github.com/aws-samples/ros2-ota-firmware-updates, 접근일 2026-09-25
[^ref-761]: 네이트 뉴스(원 매체 미확인), 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장, 2026-07-23, https://m.news.nate.com/view/20260723n24828, 접근일 2026-09-25 (원문 미열람)
[^ref-763]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)
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

### runs/2026-09-25-61/pages/topics/2026/2026-09-25-area24-s4.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-364, ref-753, ref-754, ref-755, ref-757, ref-758]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md#4
---

[홈](../../index.md) › [주제](../index.md) › 24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어

# 24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 수명주기 관리를 이야기하려면 먼저 무엇을 자산으로 보고, 그 상태와 버전을 어떤 이름으로 부르는지 정해야 한다.
- 이 페이지는 [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

수명주기 관리를 이야기하려면 먼저 무엇을 자산으로 보고, 그 상태와 버전을 어떤 이름으로 부르는지 정해야 한다.

- **자산 관리(Asset Management)** — ISO 55000:2024(제2판, 2024-07, ISO/TC 251)는 자산 관리의 용어·개요·원칙을 정하고 ISO 55000:2014 를 대체하며, 모든 유형의 자산에 적용된다. [사실][^ref-755]
- **상태 감시(Condition Monitoring)** — ISO 17359:2018 은 기계의 상태 감시 프로그램을 세울 때의 일반 절차 지침으로, 진동·온도·유량·오염·전력·속도 같은 변수를 쓰며 상태 감시·진단 표준군의 상위 문서 역할을 한다. [사실][^ref-754] 산업용 로봇 분야의 검토 논문은 상태 감시·고장 진단을 상태 기반 정비(Condition-Based Maintenance, CBM) 구현 관점에서 정리한다. [사실][^ref-757]
- **배터리 건강 상태(State of Health, SOH)** — VDA 5050 상태 메시지는 [충전 상태(State of Charge, SOC)](../../glossary/state-of-charge.md)(stateOfCharge)와 별도로 원래 용량 대비 배터리 상태(batteryHealth), 충전 중 여부, 현재 충전 상태로 갈 수 있는 추정 거리(range)를 로봇이 보고하게 한다. [사실][^ref-051]
- **소프트웨어 명판(Software Nameplate)** — [자산관리셸(Asset Administration Shell, AAS)](../../glossary/asset-administration-shell.md)의 IDTA 02007 서브모델은 업데이트·패치 관리·라이선스 관리·감사를 위해 소프트웨어 제품과 설치 인스턴스 정보를 통일된 형태로 표현하며, 버전(주·부·개정·빌드), 배포일·빌드일·설치일, 설치 경로·체크섬, 설치된 버전과 구성 경로 같은 속성을 둔다. [사실][^ref-753]
- **패치 관리(Patch Management)** — IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템의 패치 관리 프로그램을 운영하는 자산 소유자와 제품 공급자에 대한 요구, 공급자–소유자 간 패치 정보 교환 형식, 패치 개발·배포·설치 활동을 정의하며, 보안 외 패치·업데이트에도 적용될 수 있다고 적는다. [사실][^ref-758]
- **의미적 버전과 지도 버전** — [VDA 5050](../../glossary/vda-5050.md)은 주 버전 변경을 새 필수 필드 도입 같은 호환성을 깨는 변경, 부 버전을 기능 추가, 수 버전을 작은 수정으로 규정하고 MQTT 토픽 경로에 주 버전(v3 등)을 넣는다. [사실][^ref-031] 지도는 지도 식별자(mapId)와 지도 버전(mapVersion)의 조합으로 식별한다. [사실][^ref-031]
- **[관리형 노드(Managed Node)](../../glossary/managed-node.md)** — ROS 2 관리형 노드 설계는 미구성·비활성·활성·종료의 네 주 상태와 구성·활성화·비활성화·정리·종료 전이를 두어, 실행 전에 구성 요소가 올바로 초기화됐는지 확인하고 실행 중 노드를 교체·재시작할 수 있게 한다. [사실][^ref-364]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- 관련 영역: [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-364]: Open Robotics (ROS 2 Design), Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-753]: IDTA (admin-shell-io/id GitHub), IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing), 미확인, https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md, 접근일 2026-09-25
[^ref-754]: ISO, ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines, 2018, https://www.iso.org/standard/71194.html, 접근일 2026-09-25 (원문 미열람)
[^ref-755]: ISO, ISO 55000:2024 - Asset management — Vocabulary, overview and principles, 2024-07, https://www.iso.org/standard/83053.html, 접근일 2026-09-25 (원문 미열람)
[^ref-757]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-758]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-61 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-61 | 24. 자산·소프트웨어 수명주기 관리 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-61/pages/topics/2026/2026-09-25-area24-s6.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-228, ref-230, ref-364, ref-403, ref-757, ref-760, ref-761]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md#6
---

[홈](../../index.md) › [주제](../index.md) › 24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술

# 24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 산업용 로봇의 상태 감시·고장 진단은 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 기법으로 정리돼 있다. [사실][^ref-757]
- 이 페이지는 [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

산업용 로봇의 상태 감시·고장 진단은 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 기법으로 정리돼 있다. [사실][^ref-757]

### 부품 상태 감시와 고장 진단

Lei 외(2025)의 검토 논문은 산업용 로봇의 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 상태 감시·고장 진단 기술을 상태 기반 정비 구현 관점에서 정리했다. [사실][^ref-757] 부품 진단 자체는 로봇 제조사 쪽 연계 대상으로 보인다. [추정][^ref-757] ROP 가 그 결과를 받는 방식은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에서 다룬다.

### 배터리 열화를 반영한 배정·충전

2026년 3월 arXiv 프리프린트(동료 심사 전, 저자 미확인)는 작업 배정·서비스 순서·충전 여부·충전 모드·충전기 접근을 함께 최적화해 플릿 전체의 배터리 열화를 균형 있게 나누는 정식화를 제안했고, 급속 충전에 따른 사이클 열화와 높은 충전 상태로 대기할 때의 달력 열화를 근사 열화 지표로 반영했다. [사실][^ref-403] 규격 쪽에서는 VDA 5050 팩트시트의 batteryCharging 블록이 임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간을 담는다. [사실][^ref-228]

### 버전 정보 수집

VDA 5050 팩트시트 스키마는 mobileRobotConfiguration.versions 배열에 로봇에서 도는 하드웨어·소프트웨어 버전(예: softwareVersion)을 키–값으로 담는다. [사실][^ref-228] MassRobotics AMR 상호운용 표준 JSON 스키마는 제조사명·모델·일련번호, 배터리 잔량 비율, 남은 가동 시간, 오류 코드 목록을 담지만 소프트웨어·펌웨어 버전 필드는 명시적으로 두지 않은 것으로 보인다. [추정][^ref-230]

### 배포·교체·복구

ROS 2 관리형 노드는 실행 전 초기화 확인과 실행 중 노드 교체·재시작을 위한 상태 전이를 제공한다. [사실][^ref-364] aws-samples 저장소의 시연용 샘플인 ROS 2 플릿 무선 업데이트(Over-the-Air, OTA) 구현은 IoT Jobs·Greengrass v2·Docker 로 배포를 지시·추적하고 플릿 색인으로 기기별 펌웨어 버전을 조회한다. [추정] 벤더 주장[^ref-760] README 는 실패한 업데이트를 이전의 검증된 버전으로 자동 복귀시키는 것을 이점으로 나열할 뿐, 자동 롤백의 구현 절차는 보이지 않는다. [추정] 벤더 주장[^ref-760]

국내에서는 2026-07-22 판교에서 열린 SDR(Software Defined Robot) 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍에서 KIST 휴머노이드연구단이 클라우드 기반 SDR 공통 서비스 프레임워크를 소개했고, 이 플랫폼이 무선 업데이트로 로봇 소프트웨어를 갱신하고 기능을 추가하는 것을 목표로 한다고 보도됐다(원 매체 미확인). [추정][^ref-761]

### 지도 버전 배포

VDA 5050 3.0.0 은 즉시 동작 downloadMap·enableMap·deleteMap 으로 지도 내려받기·활성화·삭제를 지시한다. [사실][^ref-031] 지도 전환 절차는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절의 적치 시나리오에서 보였다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- 관련 영역: [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-364]: Open Robotics (ROS 2 Design), Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-403]: arXiv (저자 미확인), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-757]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-760]: Amazon Web Services (aws-samples GitHub), ros2-ota-firmware-updates — README, 미확인, https://github.com/aws-samples/ros2-ota-firmware-updates, 접근일 2026-09-25
[^ref-761]: 네이트 뉴스(원 매체 미확인), 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장, 2026-07-23, https://m.news.nate.com/view/20260723n24828, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-61 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-61 | 24. 자산·소프트웨어 수명주기 관리 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-61/pages/topics/2026/2026-09-25-area24-s3.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-228, ref-523, ref-752, ref-753, ref-759, ref-762, ref-763]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md#3
---

[홈](../../index.md) › [주제](../index.md) › 24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가

# 24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 펌웨어가 바뀔 때 다시 검증할 범위를 정하려면 로봇별 소프트웨어 버전을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전·기능 선언·안전 파라미터·지도 버전의 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 이번 조사(2026-09-25 기준)에서 찾지 못했다. [추정][^ref-031][^ref-228][^ref-753][^ref-763]
- 이 페이지는 [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

펌웨어가 바뀔 때 다시 검증할 범위를 정하려면 로봇별 소프트웨어 버전을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전·기능 선언·안전 파라미터·지도 버전의 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 이번 조사(2026-09-25 기준)에서 찾지 못했다. [추정][^ref-031][^ref-228][^ref-753][^ref-763]

바뀌는 것은 제조사 펌웨어만이 아니다. ROS 2 배포판 지원 정책(REP 2000)에 따르면 장기 지원판은 5년, 비장기 지원판은 1.5년 지원되며, Humble 은 2022-05~2027-05, Jazzy 는 2024-05~2029-05, Kilted 는 2025-05~2026-11 이 지원 기간이다. [사실][^ref-752] Kilted 의 지원 종료는 기준일 2026-09-25 에서 약 2개월 뒤로, 곧 바뀌는 사실이다. [사실][^ref-752] 오케스트레이션 검증에 쓰는 시뮬레이션 환경도 같아서, rmf_simulation 저장소는 지원 대상으로 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 적고 있다. [사실][^ref-523]

변경은 안전·규제 문제로도 이어진다. EU 기계 규정 (EU) 2023/1230 은 2027-01-20 부터 적용되며, 시장에 나온 기계에 대해 제조사가 예견·계획하지 않은 물리적 또는 디지털 변경이 새 위험을 만들거나 기존 위험을 키워 새 보호 조치가 필요해지면 이를 '실질적 변경'으로 정의한다. [사실][^ref-759] 이 정의에 따르면 로봇 동작을 바꾸는 소프트웨어 업데이트도 실질적 변경 여부를 따져야 하는 대상이 될 수 있다. [추정][^ref-759]

국내에서는 로봇 안전 컨설팅 업체 세이프틱스의 가이드가, 같은 모델로 교체해도 제어기 펌웨어 버전·안전 기능 파라미터·엔드이펙터 재장착 정밀도가 달라지면 위험성평가 조건이 바뀐 것이므로 변경 범위 재평가와 검증 문서 갱신이 필요하다고 권고한다. [의견][^ref-763] 한국로봇사용자협회의 협동로봇 설치 작업장 안전인증은 협동운전 산업용 로봇 시스템의 ISO 10218-2 준수 여부를 심사하고 인증서 발급일로부터 2년 주기로 정기 심사한다. [사실][^ref-762] 펌웨어 변경이 재심사 대상인지는 미확인이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- 관련 영역: [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25 (원문 미열람)
[^ref-752]: Open Robotics (ROS REP), REP 2000 -- ROS 2 Releases and Target Platforms, 미확인, https://www.ros.org/reps/rep-2000.html, 접근일 2026-09-25
[^ref-753]: IDTA (admin-shell-io/id GitHub), IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing), 미확인, https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md, 접근일 2026-09-25
[^ref-759]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-25 (원문 미열람)
[^ref-762]: 한국로봇사용자협회, 협동로봇 설치 작업장 안전인증 안내, 미확인, https://www.korua.or.kr/inspect/inspectInfo.do, 접근일 2026-09-25 (원문 미열람)
[^ref-763]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-61 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-61 | 24. 자산·소프트웨어 수명주기 관리 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-25-61/pages/topics/2026/2026-09-25-area24-s7.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-228, ref-230, ref-523, ref-364, ref-752, ref-753, ref-754, ref-755, ref-758, ref-759, ref-762]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md#7
---

[홈](../../index.md) › [주제](../index.md) › 24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스

# 24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [추정][^ref-031][^ref-753][^ref-758] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [추정][^ref-031][^ref-753][^ref-758] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 3.0.0 명세 | 표준 | 의미적 버전 규칙, 지도 배포·버전 관리, 미지원 파라미터 오류 규정 [사실] | [^ref-031] |
| VDA 5050 팩트시트 스키마 | 표준 | versions 배열(하드웨어·소프트웨어 버전), batteryCharging 블록 [사실] | [^ref-228] |
| VDA 5050 상태 스키마 | 표준 | batteryHealth·range 와 mapId·mapVersion·mapStatus 보고 [사실] | [^ref-051] |
| MassRobotics AMR 상호운용 표준 | 표준 | 배터리 잔량·남은 가동 시간·오류 코드. 버전 필드는 없는 것으로 보임 [추정] | [^ref-230] |
| IDTA 02007 소프트웨어 명판 | 표준 | 소프트웨어 제품·설치 인스턴스의 버전·설치 정보 [사실] | [^ref-753] |
| ISO 17359:2018 | 표준 | 기계 상태 감시 프로그램 수립 일반 지침(원문 미열람) [사실] | [^ref-754] |
| ISO 55000:2024 | 표준 | 자산 관리 용어·개요·원칙(원문 미열람) [사실] | [^ref-755] |
| IEC TR 62443-2-3:2015 | 표준 | 산업 제어 시스템 패치 관리(원문 미열람) [사실] | [^ref-758] |
| ROS 2 관리형 노드 | 프레임워크 | 노드 초기화 확인과 실행 중 교체·재시작 [사실] | [^ref-364] |
| REP 2000 | 프레임워크 | ROS 2 배포판 지원 기간 정책 [사실] | [^ref-752] |
| rmf_simulation | 오픈소스 | 시뮬레이터 판(Gazebo Classic 11·Fortress) 지원 범위(원문 미열람) [사실] | [^ref-523] |
| 한국로봇사용자협회 협동로봇 설치 작업장 안전인증 | 평가 프로그램 | ISO 10218-2 준수 심사, 2년 주기 정기 심사(원문 미열람) [사실] | [^ref-762] |

규정으로는 EU 기계 규정 (EU) 2023/1230 이 디지털 변경을 포함한 실질적 변경을 정의한다(원 페이지 3절의 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](2026-09-25-area24-s3.md)). [사실][^ref-759]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- 관련 영역: [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: Open Robotics (ROS 2 Design), Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-752]: Open Robotics (ROS REP), REP 2000 -- ROS 2 Releases and Target Platforms, 미확인, https://www.ros.org/reps/rep-2000.html, 접근일 2026-09-25
[^ref-753]: IDTA (admin-shell-io/id GitHub), IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing), 미확인, https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md, 접근일 2026-09-25
[^ref-754]: ISO, ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines, 2018, https://www.iso.org/standard/71194.html, 접근일 2026-09-25 (원문 미열람)
[^ref-755]: ISO, ISO 55000:2024 - Asset management — Vocabulary, overview and principles, 2024-07, https://www.iso.org/standard/83053.html, 접근일 2026-09-25 (원문 미열람)
[^ref-758]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-759]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-25 (원문 미열람)
[^ref-762]: 한국로봇사용자협회, 협동로봇 설치 작업장 안전인증 안내, 미확인, https://www.korua.or.kr/inspect/inspectInfo.do, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-61 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-61 | 24. 자산·소프트웨어 수명주기 관리 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-61/pages/topics/2026/2026-09-25-area24-s10.md

```markdown
---
title: "24. 자산·소프트웨어 수명주기 관리 — 다른 연구영역과의 연결"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-228, ref-230, ref-523, ref-403, ref-757, ref-758, ref-759, ref-763]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md#10
---

[홈](../../index.md) › [주제](../index.md) › 24. 자산·소프트웨어 수명주기 관리 — 다른 연구영역과의 연결

# 24. 자산·소프트웨어 수명주기 관리 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 연결은 이번 조사 결과를 바탕으로 한 구축자 의견이다. [의견][^ref-523][^ref-758][^ref-403][^ref-763]
- 이 페이지는 [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 연결은 이번 조사 결과를 바탕으로 한 구축자 의견이다. [의견][^ref-523][^ref-758][^ref-403][^ref-763]

- [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 업데이트 뒤 정상·장애 상황의 회귀 시험이 재검증 범위 산정의 결과를 받는다. [의견][^ref-763]
- [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 가정한 미래를 실험하는 시뮬레이션 환경 자체도 시뮬레이터 판 교체에 따른 수명주기 관리 대상이다. [의견][^ref-523]
- [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) — 보안 패치의 배포·설치가 이 영역의 배포 절차와 겹친다. [의견][^ref-758]
- [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — 펌웨어·안전 파라미터 변경 뒤 위험성 재평가와 실질적 변경 판단이 필요하다. [의견][^ref-763][^ref-759]
- [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 배터리 열화를 반영한 충전 모드·충전기 접근 계획과 이어진다. [의견][^ref-403]
- [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 배터리 열화 균형을 작업 배정과 함께 최적화하는 연구가 있다. [의견][^ref-403]
- [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 상태 감시·고장 진단 결과와 오류 코드가 정비 판단의 입력이 된다. [의견][^ref-757]
- [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 로봇 등록 때 팩트시트의 버전 정보를 수집해 버전 목록의 출발점으로 삼는다. [의견][^ref-228]
- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 규격별 버전·배터리 필드 차이를 어댑터가 메워야 한다. [의견][^ref-228][^ref-230]
- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 규격 주 버전 이행이 여러 사업자의 합의 문제다. [의견][^ref-031]
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 지도 버전의 배포·활성화 시점이 지도 모델 변경과 맞물린다. [의견][^ref-031]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)
- 관련 영역: [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: arXiv (저자 미확인), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-757]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-758]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-759]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-25 (원문 미열람)
[^ref-763]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-61 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-61 | 24. 자산·소프트웨어 수명주기 관리 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-25-61/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/action-dependency-graph.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/b2mml.md
glossary/battery-swapping.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/compensating-transaction.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fleet-adapter.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/grai.md
glossary/hallucination.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoorgml.md
glossary/information-delivery-specification.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/isa-95.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mobile-manipulator.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/order-batching.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/plug-and-produce.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/root-cause-analysis-rca.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/virtual-commissioning.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
glossary/zone-set.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/index.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 553건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 142개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
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
- fault-injection: 장애 주입 (Fault Injection)
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
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
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
- model-checking: 모델 검사 (Model Checking)
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
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
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
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [24] 에 걸린 1건 / 전체 89건)

```markdown
- oq-087 [열림] 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? (영역 23, 24)
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

### runs/2026-09-25-61/verification2.json

```json
{
  "run_id": "2026-09-25-61",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
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
    "overlaps": []
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
    "세부영역 8절 ref-760 항목: '플릿 OTA 배포·버전 조회·롤백을 시연하는 샘플이다'를 'aws-samples 저장소의 시연용 샘플로 플릿 OTA 배포·버전 조회를 보이며, 자동 롤백은 README가 이점으로 나열할 뿐 구현 절차는 보이지 않는다'로 고친다([추정]과 '벤더 주장' 병기는 유지한다). 이유: 1차 f18 지시가 6절(분리 페이지 2026-09-25-area24-s6.md)에서만 이행됐고, 8절은 여전히 롤백을 시연한다고 적고 있다.",
    "세부영역 7절 첫 문장 '이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [사실][^ref-031]'(자동 분리된 주제 페이지 2026-09-25-area24-s7.md 1절·3절의 같은 문장 포함): 태그를 [추정]으로 낮추고 각주를 [^ref-031][^ref-753][^ref-758]로 바꾼다. 이유: ref-031(VDA 5050 명세)은 '자산·패치 관리 표준'을 뒷받침하지 않고, '출발한다'는 여러 finding을 묶은 해석이다.",
    "세부영역 8절 첫 문장 '이 영역의 대표 연구는 부품 상태 감시 검토와 배터리 열화 인지 스케줄링으로 나뉜다. [사실]'과 Lei 외 항목의 'ROP 가 받을 정비 신호의 출처를 이해하는 배경 자료다': 두 문장을 [의견](구축자 의견)으로 표시한다. Lei 외 항목에서는 논문 내용 문장만 [사실][^ref-757]로 남긴다. 이유: 대표 연구를 어떻게 나누고 평가할지는 브리프의 어느 finding에도 없는 편집 판단이다.",
    "6절(자동 분리 페이지 2026-09-25-area24-s6.md 3절 '부품 상태 감시와 고장 진단' 소절)의 '부품 진단 자체는 로봇 제조사 쪽 연계 대상이며' 문장: 태그·각주 없는 단정을 '연계 대상으로 보인다. [추정][^ref-757]'로 고친다(f24 처분과 같게 한다). 같은 페이지의 '9절에서 다룬다'와 '5절의 적치 시나리오'는 원 세부영역 페이지의 해당 절 링크로 바꾼다. 이유: 주장에 태그가 없고, 분리 페이지의 5·9절은 다른 절을 가리킨다.",
    "flow_matrix_updates: 적치/작업 대상, 출하/시작 조건, 출하/작업 대상 세 항목을 뺀다. 이유: 5절 끝 문장은 이 영역이 관여하는 칸을 적치의 시작 조건·수행 자원·제약·완료·인계·예외·성과와 출하의 수행 자원·제약으로 한정한다. 세 칸은 finding 없이 '(가상)' 자리 표시만 있어 흐름 매트릭스 연결 근거가 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다(raw.githubusercontent.com 미러만 열 수 있음). 확인 25건, 미확인 2건(f13·f17: 출처가 주장의 일부만 뒷받침함), 교차 확인 0건. 강등: f13은 확인된 부분만 사실로 두고 나머지 구절을 삭제했다. f17은 정의를 조건과 함께 사실로 두고 적용 해석을 추정으로 분리했다. f19는 사실 → 추정. 원문 미열람 출처: ref-754, ref-755, ref-403, ref-757, ref-758, ref-759, ref-761, ref-762, ref-763, ref-523. 주의: 모든 핵심 주장이 단일 출처이고, 펌웨어 변경의 영향 범위를 산정하는 공개 절차는 확인되지 않았다(f22 추정). EU 기계 규정의 실질적 변경은 제조사가 예견하지 않은 변경에 한정된다. f18은 벤더 주장이다. 국내 인증에서 펌웨어 변경이 재심사 대상인지는 미확인이다. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 3건: 7절 첫 문장의 사실 태그가 근거보다 넓고, 8절 대표 연구 분류가 편집 판단인데 사실로 표시됐으며, 6절 분리 페이지에 태그 없는 연계 대상 단정이 있다. 1차 f18 지시가 8절에서 이행되지 않았다. flow_matrix_updates 3칸이 본문과 맞지 않는다. [분류원문] 보존, 섹션 순서 준수, 링크 유효. 참고: 자동 분리 주제 페이지 9절의 '1차·2차 검증을 거쳤다'는 고정 문구이며 2차 통과 전에는 사실이 아니다. 퍼블리셔 담당이 확인해야 한다. reference_updates의 cited_by는 분리 페이지 인용을 일부 빠뜨렸다(퍼블리셔 자동 영역이 재계산하는지 확인).",
  "retry_reason": null
}
```
