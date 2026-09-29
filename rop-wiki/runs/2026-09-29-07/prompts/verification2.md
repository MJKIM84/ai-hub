(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-07
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 4. 이기종 로봇 등록 (B. 로봇 온톨로지)
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

### runs/2026-09-29-07/target.json

```json
{
  "run_id": "2026-09-29-07",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 99,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 4,
    "area_name": "4. 이기종 로봇 등록",
    "category": "B. 로봇 온톨로지",
    "category_letter": "B"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=4"
}
```

### runs/2026-09-29-07/research.json

```json
{
  "run_id": "2026-09-29-07",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 4,
    "area_name": "4. 이기종 로봇 등록",
    "category": "B. 로봇 온톨로지"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 디지털 명판·URDF·AGV 기술 데이터 서브모델·자산관리셸 레지스트리·온톨로지 채우기 용어 없음(VDA 5050 팩트시트·신원 보고·자산관리셸·소프트웨어 명판·능력 기술 서브모델·의미 식별자는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 등록 데이터 수집(팩트시트 요청·자산관리셸), 문서·URDF에서 능력 추출, 검토·승인 흐름, 어댑터 설정 생성 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 팩트시트, IDTA 02047·02006, MassRobotics 신원 보고, OPC UA Robotics, 자산관리셸 API, Open-RMF 플릿 어댑터 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 열린 질문 oq-128 미반영, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]",
    "등록 시 받아야 할 식별·제원 데이터를 정한 기계가독 형식(VDA 5050 팩트시트, 자산관리셸 서브모델·디지털 명판, MassRobotics 신원 보고, OPC UA Robotics)은 각각 무엇을 필수로 요구하는가? (섹션 4·7 겨냥)",
    "플릿 관리 프레임워크(Open-RMF)는 새 로봇을 등록·연동할 때 어떤 설정과 구현을 요구하며, 병원 현장에서 실제로 어떻게 등록했는가? (섹션 5·6 겨냥)",
    "매뉴얼·URDF·자연어 설명에서 능력·제약을 자동으로 추출하고 검증과 사람 검토를 두는 방법은 무엇이 보고되었는가? (섹션 6·8 겨냥, 교차 규칙에 따라 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 연결)",
    "제조사가 능력·제원 정보를 제공·갱신하는 경로(자산관리셸 레지스트리·디스커버리, 팩트시트 요청)와 벤더·통합사를 사전 평가하는 등록 승인 관문의 사례는 무엇인가? (섹션 6·9 겨냥)",
    "oq-128 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있는가? (섹션 5·11 겨냥, 한국 자료 우선)",
    "이기종 로봇 등록에서 ROP가 직접 맡을 것(등록부·데이터 수집·추출 초안·검토 승인)과 로봇 내부 주행 기술·제조사 책임에 맡길 것의 경계는 어디이며, 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 공식 저장소(main, 3.0.0 판)의 팩트시트 JSON 스키마는 headerId·timestamp·version·manufacturer·serialNumber·typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 을 필수 속성으로, 하드웨어·소프트웨어 버전과 네트워크·배터리 매개변수를 담는 mobileRobotConfiguration 을 선택 속성으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "factsheet.schema 의 required 목록에 위 11개 속성이 있고 mobileRobotConfiguration 은 선택이다. headerId 는 \"defined per topic and incremented by 1 with each sent message\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f2",
      "claim": "같은 팩트시트 스키마에서 typeSpecification 은 시리즈 이름, 구동 방식(DIFFERENTIAL·OMNIDIRECTIONAL·THREE_WHEEL), 로봇 종류(FORKLIFT·CONVEYOR·TUGGER·CARRIER), 최대 적재 질량, 위치추정 방식, 주행 방식(물리 라인·가상 라인·자유 주행), 지원 구역 유형을, physicalParameters 는 최소·최대 속도, 각속도, 최대 가감속, 높이·폭·길이를 기종 단위로 기술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "typeSpecification: seriesName, mobileRobotKinematics, mobileRobotClass, maximumLoadMass, localizationTypes, navigationTypes, supportedZones / physicalParameters: minimumSpeed·maximumSpeed, 각속도, maximumAcceleration·Deceleration(최대 적재 기준), height·width·length. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다고 적어 등록 데이터를 로봇에서 직접 받는 경로를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 판 명세: 팩트시트는 \"Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control\"을 담고, 관제가 factsheetRequest 즉시 동작으로 요청하면 로봇이 factsheet 토픽에 게시한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f4",
      "claim": "IDTA 02047-1-0(2025-03) '실내 물류용 AGV 기술 데이터' 자산관리셸 서브모델은 TypeAndApplicationInformation·TechnicalParameters·VDA5050Factsheet·EnergyAndCommunication·Battery·Safety·TemporaryTechnicalData 컬렉션으로 구성되며, 혼합 플릿을 중앙 관제에 통합하고 시운전·운영·유지보수에 걸쳐 쓰는 것을 목표로 디지털 명판·기술 데이터 서브모델과 연계된다.",
      "tag": "사실",
      "source_ids": [
        "ref-198"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 본문의 컬렉션 목록과 VDA 5050 팩트시트 연계, 관련 서브모델(Digital Nameplate, Technical Data) 확인. 공식 저장소 README 는 대상이 \"driverless vehicles and robots in intralogistics\"이고 요구가 \"commissioning, operation and maintenance\"에 걸친다고 적는다.",
      "as_of": "2025-03",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f5",
      "claim": "IDTA 02006 디지털 명판 서브모델 3.0 판은 URIOfTheProduct·ManufacturerName·ManufacturerProductDesignation·SerialNumber·YearOfConstruction·DateOfManufacture 를 필수로, HardwareVersion·FirmwareVersion·SoftwareVersion·ContactInformation·Markings 를 선택으로 두어 로봇을 포함한 산업 장비의 식별자와 버전을 기계가독 명판으로 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-876"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IDTA 02006-3-0 PDF 의 속성표: 필수 6개(제품 URI·제조사·제품명·일련번호·제조 연도·제조일), 선택 5개(하드웨어·펌웨어·소프트웨어 버전, 연락처, 마킹). 발행일은 도구가 2024-11 로 읽었으나 파일명은 3-0-1 판(2025-10 게시)이라 확정하지 못함. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "MassRobotics AMR 상호운용 표준의 JSON 스키마는 로봇이 접속 시 보내는 identityReport 에 uuid(RFC 4122)·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope 를 필수로, maxSpeed·maxRunTime·chargerType·supportVendorName·productDocumentation·cargoType·cargoMaxVolume·cargoMaxWeight 등을 선택으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AMR_Interop_Standard.json: identityReport 필수 6개, 선택에 productDocumentation(문서 URL)·cargoMaxWeight 등. robotSerialNumber 는 \"Unique robot identifier that ideally can be physically linked to the AMR\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f7",
      "claim": "서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하고, 셋 모두 제조사명·기종(시리즈)·일련번호·치수(외곽)·최대 적재·최대 속도 항목을 공통으로 담아 '제조사 제공 식별·제원 기록'이 이기종 로봇 등록의 표준 관행으로 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-228",
        "ref-230",
        "ref-876"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "VDA 5050 팩트시트(manufacturer·serialNumber·typeSpecification·physicalParameters·mobileRobotGeometry), MassRobotics identityReport(manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope·maxSpeed), IDTA 02006(ManufacturerName·SerialNumber·버전) 세 원문을 대조. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "OPC UA for Robotics 1부(OPC 40010-1) 1.02 판(2025-09-08)은 수직 통합·자산 관리·상태 감시를 범위로 MotionDeviceSystem 정보 모델을 정의하고, MotionDevice 와 Controller 에 Manufacturer·Model·SerialNumber·ProductCode·SoftwareRevision 식별 속성을 두어 산업용 로봇(매니퓰레이터) 등록에 쓸 식별 정보를 표준화한다.",
      "tag": "사실",
      "source_ids": [
        "ref-881"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OPC Foundation 참조 사이트: Version 1.02, 2025-09-08 게시, 범위 'Vertical Integration'(자산 관리·상태 감시), MotionDevice·Controller 식별 속성 Manufacturer·Model·SerialNumber·ProductCode·SoftwareRevision.",
      "as_of": "2025-09-08",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f9",
      "claim": "OPC Foundation 은 OPC UA for Robotics 명세를 STS XML 외에 'AI 응용용 마크다운'과 'RAG 청크' 형식으로도 제공해, 표준 문서 자체를 언어 모델이 읽어 처리하기 쉬운 형식으로 배포하기 시작했다.",
      "tag": "사실",
      "source_ids": [
        "ref-881"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "참조 페이지의 제공 형식: STS XML, \"Markdown for AI applications\", RAG Chunks(로컬 모델 통합용), 네임스페이스 http://opcfoundation.org/UA/Robotics/ 와 노드셋 다운로드.",
      "as_of": "2025-09-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "자산관리셸 API 명세(IDTA-01002) 공식 저장소는 최신 3.2.0 판에서 AAS 저장소·서브모델 저장소·AAS 레지스트리·서브모델 레지스트리·디스커버리·개념 설명 저장소·AASX 파일 서버 등 아홉 가지 서비스 명세를 두어, 제조사가 낸 자산관리셸을 등록하고 찾는 인터페이스를 표준으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-880"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "aas-specs-api README: 최신 릴리스 3.2.0, 서비스 명세 9종(AAS Service, AAS Repository, AAS Registry, Submodel Service·Repository·Registry, Discovery, Concept Description Repository, AASX File Server). 레지스트리·디스커버리의 결합 목적 문장은 README 에 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "디지털 명판(f5)·AGV 기술 데이터 서브모델(f4)·레지스트리·디스커버리 API(f10)를 함께 보면, 이 영역의 '제조사 능력 정보 제공 경로'는 제조사가 명판과 기술 데이터 서브모델을 자산관리셸로 내고 레지스트리에 등록해 ROP 가 자산 식별자로 찾아 읽는 방식으로 구성할 수 있을 것으로 보이나, 로봇 관제가 이 경로로 실제 등록한 운영 사례는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-876",
        "ref-198",
        "ref-880"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세 표준 산출물의 역할(식별·제원·등록/발견)을 조합한 리서치 에이전트의 추론. 자산 ID→AAS ID(디스커버리)→엔드포인트(레지스트리) 순서는 IDTA Part 2 PDF 검색 결과 요약에서만 보였고 원문은 열지 않았다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f12",
      "claim": "Open-RMF 플릿 어댑터 튜토리얼은 새 플릿을 등록하는 config.yaml 에 플릿 이름, 선속도·각속도 한계, 발자국·근접 반경(profile), 후진 가능 여부, 배터리·기계·주변·도구 시스템 매개변수, 재충전 임계값, 작업 능력(loop·delivery·clean), 로봇별 충전기를 적고, 로봇 측 RobotAPI 가 navigate·position·battery_soc·stop·start_activity·is_command_completed 를 구현해야 한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "integration_fleets_adapter_tutorial.md: \"limits: [linear: [0.5, 0.75], angular: [0.6, 2.0]]\", profile footprint/vicinity, battery_system(voltage·capacity·charging_current), task_capabilities, robots 별 charger; RobotAPI 필수 메서드 6종. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f13",
      "claim": "Valner 외(2022)의 타르투대학교병원 현장 시험은 자체 관제가 없는 PAL Robotics TIAGo 를 로봇 탑재 컴퓨터의 FreeFleet 클라이언트, 플릿 이름·DDS 설정의 FreeFleet 서버, 배터리·속도·발자국을 적은 RMF 어댑터 파일로 Open-RMF 에 등록했고, 프로그램 제어가 없는 병원 문은 카드 인식·근접 센서를 대신 작동시키는 서보 장치를 만들어 지나며 중환자실에서 검사실로 혈액 검체를 운반했다.",
      "tag": "사실",
      "source_ids": [
        "ref-874"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Frontiers in Robotics and AI 2022-08-23 전문: TIAGo 주 배치, Clearpath Jackal 시험 환경, MiR100+UR5e 예정; 등록은 FreeFleet 클라이언트·서버 설정과 어댑터 파일의 로봇 특성; 문은 \"swipe the key card or trigger the proximity sensor\" 장치로 통과.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "서로 다른 두 발행 주체(Open Robotics 튜토리얼, 타르투대학교 연구진의 병원 현장 시험)가 플릿 관리 프레임워크에 로봇을 등록하는 일이 '기종 제원·배터리 매개변수를 적은 어댑터 설정 파일'과 '로봇별 API 구현'의 두 부분으로 이루어진다고 각각 보고해, 등록 작업의 구성이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-153",
        "ref-874"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "튜토리얼의 config.yaml(제원·배터리·작업 능력)+RobotAPI 와 병원 시험의 어댑터 파일(배터리·속도·발자국)+FreeFleet 클라이언트가 같은 구조. 발행 기관이 다르고 한쪽이 다른 쪽을 옮긴 것이 아님.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "싱가포르 창이종합병원 CHART 의 RoMi-H 등재 프로그램(2025-05-01 시행)은 보건부가 Open-RMF 기반 RoMi-H 를 공공 의료기관의 자동화 통합 플랫폼으로 지정한 뒤 시스템 통합사가 기술·배치 역량 평가를 거쳐 2년 유효 등재를 받아야 병원 제안 요청에 참여하게 하며, 2026-08-24 기준 등재 업체는 5곳이다.",
      "tag": "사실",
      "source_ids": [
        "ref-878"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CGH 공지: 통합사는 \"a series of evaluations, encompassing both technical expertise and deployment knowledge\"를 거침, 등재 5곳(HOPE Technik·Medisys·Panasonic Asia Pacific·QuikBot·Techfox), 2년 유효, 반기 평가.",
      "as_of": "2026-08-24",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "벤더 주장(기사 경유): 클로봇의 크롬스는 '국내 첫 이기종 로봇 통합관제 솔루션'으로 50대 이상 로봇 동시 제어와 엘리베이터 탑승을 지원한다고 소개되며, 기사는 LG CNS 와 함께 인천공항 다기종 로봇 제작·5G 디지털 트윈 관제 구축 사업을 계약했다고 전하나 VDA 5050 지원 여부·연동 제조사 수·등록 방식은 기사에 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-875"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 로봇신문 2025-11-09 기사에서 \"다양한 제조사의 로봇을 하나의 시스템에서 제어할 수 있는 국내 첫 이기종 로봇 통합관제 솔루션\", 50대 이상 동시 제어, 인천공항 사업 계약. VDA 5050 기반이라는 문구는 검색 결과 요약에서만 보였고 공식 페이지는 403 으로 열지 못함.",
      "as_of": "2025-11-09",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "신민종·한영석·정재윤(한국디지털산업학회지 29권 4호, 2024)은 자율이동로봇(AMR)의 하드웨어·소프트웨어 정보를 자산관리셸(AAS)로 기록해 JSON 으로 저장·송수신하고 OPC UA 로 실시간 감시하는 모니터링 시스템 설계를 제안했으나, 초록은 실제 현장 적용 결과를 적지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-043"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록: \"AMR의 정보를 AAS로 기록하고 JSON 형식으로 저장하고 송수신하여\" 정보를 공유, OPC UA 활용; 기대 효과만 서술. 세부 서브모델(명판·기술 데이터) 명칭은 초록에 없음.",
      "as_of": "2024",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "oq-128 관련: 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구(f17)와 벤더의 이기종 관제 소개(f16)뿐이며, VDA 5050 팩트시트나 자산관리셸 능력 기술을 실제 로봇 등록 데이터로 운영에 쓴 국내 사례는 이번 조사에서 확인되지 않아 oq-128 은 미해결로 남는다.",
      "tag": "추정",
      "source_ids": [
        "ref-043",
        "ref-875"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국어 검색 2회(관제 플랫폼·팩트시트·자산관리셸, 자산관리쉘 스마트공장·로봇)에서 국내 운영 사례를 찾지 못함. 중기부 스마트공장 고도화 사업의 AAS 적용 의무화는 검색 결과 요약에서만 보여 finding 으로 내지 않음.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Dussard·Sarthou(2026)는 URDF 가 로봇의 구조·운동학은 기술하지만 식별자에 의미가 없다는 점을 들어, 기존 온톨로지의 개념을 프롬프트에 넣어 언어 모델이 URDF 요소의 의미 관계를 추론하게 하고 여러 번 질의한 다수결과 구문·스키마 검증으로 출력을 제약해 로봇 온톨로지를 자동으로 채우는 방법을 여러 로봇 기술로 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2606.17073 초록(2026-06-10): 언어 모델에 \"concepts from an existing ontology\"를 프롬프트로 주어 정렬, \"majority voting across multiple LLM queries\"와 구문·스키마 검증; 정확도 수치·사람 검증 언급은 초록에 없음.",
      "as_of": "2026-06-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "Vieira da Silva·Köcher·Gehlhoff·Fay(2024)는 능력의 자연어 설명을 정해진 프롬프트에 넣어 언어 모델이 능력 온톨로지를 생성하고, 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행한 뒤 사람이 최종 검토·수정만 하게 하는 방법을 제안해 수작업 모델링 부담을 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-465"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2406.07962 초록: 모델링은 \"manual and error-prone task\"; 자동 검증 루프(구문·모순·환각/누락) 뒤 \"a final human review and possible correction\"만 필요. 정량 결과는 초록에 없음.",
      "as_of": "2024-10-18",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f21",
      "claim": "Abolhasani·Pan(2024)의 OntoKGen 은 신뢰성·유지보수성 분야 기술 문서에서 언어 모델로 온톨로지와 지식 그래프를 뽑되, 대화형 인터페이스에서 시스템이 모범 사례 기반 온톨로지를 추천하고 사용자가 최종 결정을 갖게 하는 방식으로 '보편적으로 옳은 온톨로지는 없다'는 전제를 두고 사용자 검토를 설계의 중심에 두었다.",
      "tag": "사실",
      "source_ids": [
        "ref-883"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2412.00608 초록: 적응형 반복 사고 연쇄로 사용자 요구에 맞추고, 사용자가 \"complete control over final decisions\"; 결과는 Neo4j 저장·RAG 기반으로 활용. 로봇 문서가 아닌 신뢰성·유지보수성 문서가 대상.",
      "as_of": "2024-12-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f22",
      "claim": "서로 다른 세 연구 그룹(LAAS 의 URDF 온톨로지 채우기, 헬무트 슈미트 대학 계열의 자연어 능력 온톨로지 생성, Abolhasani·Pan 의 기술 문서 온톨로지 추출)이 언어 모델 추출에 자동 검증이나 사용자 최종 검토를 결합한 방법을 각각 보고해, '자동 추출 + 자동 검증 + 사람 최종 검토' 구성이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-239",
        "ref-465",
        "ref-883"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "f19(다수결·스키마 검증), f20(검증 루프+사람 최종 검토), f21(사용자 최종 결정) 대조. 세 출처 모두 프리프린트(초록 확인)라 medium.",
      "as_of": "2026-06-10",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f23",
      "claim": "이 영역이 요구하는 '원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만들고 사람이 대조해 확정·반려'하는 흐름은 f20·f21 의 사람 최종 검토와 방향이 같지만, 확인한 세 연구 어느 것도 추출 항목마다 매뉴얼의 절·줄 위치를 붙여 검토자가 대조하게 하는 근거 연결을 초록에서 밝히지 않아 근거 연결형 검토·승인은 아직 확인되지 않은 요구로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-465",
        "ref-883",
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세 초록의 검증·검토 서술에 원문 위치 인용 항목이 없음. 원문 위치 강조를 갖춘 검토 작업대(HERMES 등)는 지질 분야라 출처 상한 때문에 넣지 않음.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f24",
      "claim": "확인한 자료를 종합하면 4. 이기종 로봇 등록에서 ROP가 직접 맡을 범위는 제조사·기종·일련번호·펌웨어·SDK 버전·장착 장비를 담는 등록부, 팩트시트·자산관리셸·신원 보고를 받아 저장·대조하는 수집 경로, 문서·URDF에서 뽑은 능력 초안의 검토·승인 기록, 어댑터 설정 초안 생성이며, 등록 승인 관문에 벤더·통합사 사전 평가(f15)를 둘 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-198",
        "ref-153",
        "ref-878"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "팩트시트 요청 경로(f3), 자산관리셸 서브모델(f4), 어댑터 설정 구성(f12·f14), 등재 프로그램(f15)을 분류 원문 19장의 경계에 맞춰 조합한 추론.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "연계 대상: 팩트시트의 위치추정 방식·주행 방식(localizationTypes·navigationTypes)과 mobileRobotConfiguration 의 펌웨어·소프트웨어 버전은 제조사가 소유·갱신하는 로봇 자체 지능·제어 정보이므로, 이종 제조사를 잇는 ROP 는 등록 시 이를 받아 저장·대조하고 버전 변경을 추적하는 데 그치고 위치추정·회피 성능 자체는 제조사에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-228",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "스키마 필드(f2)와 명세의 벤더 정보 문구(f3)를 분류 원문 19장 '로봇 자체 지능·제어' 경계에 대응시킨 추론.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f26",
      "claim": "언어 모델로 URDF·자연어·기술 문서에서 온톨로지를 추출하는 연구(f19~f22)는 L. AI·학습 기술의 45. 문서·도면·장면 이해와 47. AI·학습·적응과 모델 운영에 속하는 방법이며 원문 교차 규칙(매뉴얼 해석은 4·55번)에 따라 이 영역과 55. 현장 조사·설치·시운전에 연결해야 하고, 등록 데이터는 5. 로봇 능력·작업 표현(능력 표현), 6. 온톨로지 기반 시스템·로봇 연동(어댑터 설정), 7. 온톨로지 검증·변경 관리와 57. 자산·소프트웨어 수명주기 관리(펌웨어·문서 개정), 20. 로봇·제조사 관제 연동과 21. 상호운용 표준·적합성(팩트시트·자산관리셸 규격)에 연결된다.",
      "tag": "추정",
      "source_ids": [
        "ref-239",
        "ref-198",
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 13장 교차 규칙과 4장 주석, 그리고 이번 finding 의 내용 분포에 따른 연결 제안.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-228",
      "org": "VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소",
      "title": "VDA5050/json_schemas/factsheet.schema (main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDA 5050 팩트시트 메시지의 JSON 스키마 원본. 필수·선택 속성과 typeSpecification·physicalParameters 필드 정의를 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-198",
      "org": "Industrial Digital Twin Association (IDTA)",
      "title": "IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics",
      "published": "2025-03",
      "url": "https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "실내 물류 AGV·AMR 의 기술 데이터를 자산관리셸 서브모델로 표준화한 명세. VDA 5050 팩트시트 컬렉션을 포함하고 혼합 플릿의 중앙 관제 통합을 목표로 한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics (AMR Interoperability Working Group)",
      "title": "AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. identityReport·statusReport 메시지와 필수·선택 필드를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06-10",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "URDF 모델을 언어 모델로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 방법. 다수결과 구문·스키마 검증으로 출력을 제약한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-153",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 플릿 어댑터를 만드는 튜토리얼. 플릿·로봇 설정 파일(config.yaml)의 항목과 로봇 측 RobotAPI 가 구현할 메서드를 적는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets_adapter_tutorial.md",
      "source_unopened": false
    },
    {
      "id": "ref-874",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "타르투대학교병원에서 Open-RMF 와 FreeFleet 으로 이기종 로봇을 등록·운용해 혈액 검체를 운반한 현장 시험. 등록 설정과 문 통과용 보조 장치를 기술한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-875",
      "org": "로봇신문",
      "title": "[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막",
      "published": "2025-11-09",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=43274",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "클로봇의 이기종 로봇 통합관제 솔루션 크롬스를 소개한 기사. 50대 이상 동시 제어·엘리베이터 탑승과 인천공항 다기종 로봇 사업 계약을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-876",
      "org": "Industrial Digital Twin Association (IDTA)",
      "title": "IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment",
      "published": null,
      "url": "https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "산업 장비의 디지털 명판 서브모델 3.0 판 명세. 제품 URI·제조사·제품명·일련번호·제조 연도·제조일을 필수로, 하드웨어·펌웨어·소프트웨어 버전 등을 선택으로 둔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-043",
      "org": "신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4))",
      "title": "자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AMR 의 하드웨어·소프트웨어 정보를 자산관리셸로 기록해 JSON 으로 교환하고 OPC UA 로 감시하는 시스템 설계를 제안한 국내 논문. KCI 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-878",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "싱가포르 공공 의료기관의 로봇 통합 플랫폼 RoMi-H 에 시스템 통합사를 평가·등재하는 프로그램 공지. 등재 요건·유효 기간·등재 업체 5곳을 적는다(2026-08-24 갱신).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소",
      "title": "VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDA 5050 명세 3.0.0 판 원문(마크다운). 팩트시트의 목적과 factsheetRequest 즉시 동작·factsheet 토픽을 통한 요청·게시 방식을 적는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-880",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README)",
      "published": null,
      "url": "https://github.com/admin-shell-io/aas-specs-api",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 API 명세(IDTA-01002)의 공식 OpenAPI 저장소 README. 최신 3.2.0 판과 레지스트리·디스커버리를 포함한 서비스 명세 9종을 나열한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/aas-specs-api/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-881",
      "org": "OPC Foundation",
      "title": "OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02)",
      "published": "2025-09-08",
      "url": "https://reference.opcfoundation.org/Robotics/v100/docs/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "산업용 로봇의 수직 통합·자산 관리·상태 감시를 위한 OPC UA 정보 모델(MotionDeviceSystem). 제조사·모델·일련번호 등 식별 속성을 정의하고 AI 응용용 마크다운·RAG 청크 형식도 제공한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-10-18",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 능력 설명을 소수 예시 프롬프트로 언어 모델에 넣어 능력 온톨로지를 생성하고 자동 검증 루프 뒤 사람이 최종 검토하는 방법. 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-883",
      "org": "Abolhasani, M. S., & Pan, R.",
      "title": "Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation",
      "published": "2024-12-10",
      "url": "https://arxiv.org/abs/2412.00608",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "기술 문서에서 언어 모델로 온톨로지·지식 그래프를 추출하되 대화형 인터페이스에서 사용자가 최종 결정을 갖게 하는 OntoKGen 파이프라인. 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
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
      "rationale": "섹션 3: f7(세 표준 기관이 제조사 제공 등록 기록을 공통으로 요구), f14(등록 작업이 설정 파일+API 구현으로 이루어짐), f15(공공 의료의 벤더 사전 평가 관문) / 섹션 4: f1·f2(팩트시트 필수 속성·기종 제원 항목), f5(디지털 명판 필수 식별자·버전), f6(신원 보고), f19(URDF 는 구조·운동학 기술, 온톨로지 채우기), f10(자산관리셸 레지스트리·디스커버리) / 섹션 5: 병원 — f13(타르투대학교병원, FreeFleet·어댑터 파일 등록, 문 통과 보조 장치, 검체 운반), f15(싱가포르 공공 의료기관의 RoMi-H 등재 프로그램), 기타 — f16(인천공항 다기종 로봇 사업, 벤더 주장 병기), 제조 공장·물류창고 사례는 이번 조사에서 확인되지 않음을 서술 / 섹션 6: 등록 데이터 수집 f3(팩트시트 요청·게시)·f11(자산관리셸 경로, 추정), 어댑터 설정 등록 f12·f14, 문서·URDF·자연어에서 능력 추출 f19·f20·f21·f22, 검토·승인 f20·f21·f23(근거 연결형 검토는 미확인), 표준 문서의 AI 가독 형식 f9 / 섹션 7: f1·f2·f3(VDA 5050 팩트시트 스키마·명세), f4(IDTA 02047), f5(IDTA 02006), f6(MassRobotics), f8·f9(OPC UA Robotics), f10(자산관리셸 API), f12(Open-RMF 플릿 어댑터) / 섹션 8: f13, f19, f20, f21, 국내 f17 / 섹션 9: f24(직접 범위: 등록부, 수집 경로, 검토·승인 기록, 어댑터 설정 초안, 승인 관문), f25(연계 대상: 위치추정·주행 방식·펌웨어는 제조사 소유) / 섹션 10: f26 — 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 63. 병원·의료(f13·f15) / 섹션 11: 기존 oq-128(f17·f18 로 부분 진전, 미해결)과 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지에 f13·f15 반영, 21. 상호운용 표준·적합성 페이지에 f7·f8 반영, 45. 문서·도면·장면 이해 페이지에 f19·f22 반영, 트랙 manual-capability-ontology 단계 2(문서 유형)에 f9·f19·f20 참고."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "디지털 명판",
      "term_en": "Digital Nameplate (IDTA 02006)",
      "definition": "제품 URI·제조사·제품명·일련번호·제조 연도·제조일을 필수로 담고 하드웨어·펌웨어·소프트웨어 버전을 선택으로 두는 자산관리셸 서브모델로, 산업 장비의 명판 정보를 기계가독 형식으로 교환하게 한다."
    },
    {
      "term_ko": "AGV 기술 데이터 서브모델",
      "term_en": "Technical Data for AGV in Intralogistics (IDTA 02047)",
      "definition": "실내 물류용 AGV·AMR 의 유형·기술 매개변수·VDA 5050 팩트시트·에너지·통신·배터리·안전·임시 기술 데이터를 컬렉션으로 나눠 담는 자산관리셸 서브모델 템플릿이다."
    },
    {
      "term_ko": "통합 로봇 기술 형식",
      "term_en": "Unified Robot Description Format (URDF)",
      "definition": "로봇의 링크와 관절로 구조·운동학·물리 속성을 기술하는 ROS 계열의 XML 형식으로, 식별자 자체에는 의미가 없어 온톨로지로 옮기려면 해석이 필요하다."
    },
    {
      "term_ko": "자산관리셸 레지스트리·디스커버리",
      "term_en": "AAS Registry / Discovery",
      "definition": "자산관리셸 API 명세(IDTA-01002)가 정한 서비스로, 등록된 자산관리셸과 서브모델의 서술자를 관리하고 자산 식별자로 해당 자산관리셸을 찾게 한다."
    },
    {
      "term_ko": "온톨로지 채우기",
      "term_en": "Ontology Population",
      "definition": "이미 정해진 온톨로지의 개념·관계에 맞춰 문서·모델 파일 같은 원천에서 개체와 관계 인스턴스를 뽑아 채우는 작업으로, 언어 모델을 쓸 때는 검증과 사람 검토를 함께 둔다."
    }
  ],
  "open_questions_new": [
    "문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 45. 문서·도면·장면 이해, 7. 온톨로지 검증·변경 관리 | 근거: f23 | 종류: 일반",
    "VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? | 관련 영역: 4. 이기종 로봇 등록, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현 | 근거: f7 | 종류: 일반",
    "싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 63. 병원·의료, 58. 다사업자 책임·계약·데이터 | 근거: f15 | 종류: 일반",
    "팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? | 관련 영역: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 3,
    "unverified": [
      "MDPI Applied Sciences 자동차 공장 다중 브랜드 플릿 통합 사례(제조 공장 사례 후보)는 두 경로 모두 403 으로 열지 못해 넣지 않음 — 제조 공장 현장 유형 사례 미확보",
      "f16 클로봇 크롬스 공식 페이지(clobot.co.kr/croms) 403 — 'VDA 5050 기반 FMS' 문구는 검색 결과 요약에서만 보여 claim 에 넣지 않음, 벤더 주장 미교차",
      "URDF 공식 문서(wiki.ros.org 는 Anubis 차단, docs.ros.org 차단, ros2_documentation raw 경로 404) 미열람 — URDF 서술은 ref-239 초록의 '구조·운동학 기술' 문구에만 기댐",
      "Springer 'Conversational Knowledge Extraction from Technical Manuals'(ECML PKDD 2025)는 인증 리다이렉트로 열지 못해 넣지 않음",
      "f4 IDTA 02047 PDF 는 컬렉션 이름과 관련 서브모델까지만 확인했고 개별 속성명·VDA 5050 팩트시트 대응 세부는 추출 응답이 얇아 미확인",
      "f5 IDTA 02006 3.0 발행일 불확실(도구 응답 2024-11, 파일명 3-0-1 판 2025-10 게시) — published null",
      "f11 자산 ID→AAS ID→엔드포인트 흐름은 IDTA Part 2 PDF 검색 결과 요약에서만 확인, 원문 미열람",
      "f15 RoMi-H 등재 평가의 기술 항목(어댑터 시험·적합성 검사 등)은 공지에 없어 미확인",
      "f17 KCI 논문 초록만 확인 — 서브모델 구성(명판·기술 데이터 등)과 현장 적용 결과 미확인",
      "f19·f20·f21 정량 결과는 초록에 없어 미확인",
      "f1·f2·f3·f6·f10·f12 출처 발행일 미확인(저장소 원문)",
      "oq-128 미해결(f18)",
      "f7·f14·f22 외 모든 finding 교차 확인 실패(표준·연구마다 발행 주체 한 곳)"
    ],
    "scope_violations": [
      "f25: 팩트시트의 위치추정·주행 방식과 펌웨어 버전은 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함",
      "f15: 벤더 등재 제도는 58. 다사업자 책임·계약·데이터와 겹치므로 이 영역에서는 등록 승인 관문 사례로만 제안함",
      "f8·f9: OPC UA Robotics 는 산업용 매니퓰레이터의 수직 통합 규격이므로 등록 식별 속성과 문서 형식 근거로만 제안하고 제어 연동은 다루지 않음",
      "f19~f22: 언어 모델 추출 연구는 L. AI·학습 기술의 방법이므로 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안함(f26)"
    ],
    "budget_used": {
      "queries": 14,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 14회/30, 신규 출처 15건/15(ref-228~ref-883, 예약 구간 안) 상한 도달로 URDF 공식 문서, IDTA Part 2 API PDF, HERMES 검토 작업대, OntoKGen 외 매뉴얼 추출 논문, IFR 의 VDA 5050 해설을 넣지 못했다. 원문 열람 15건(github_raw 5: 팩트시트 스키마·VDA5050_EN.md·MassRobotics JSON·Open-RMF 튜토리얼·aas-specs-api README, webfetch 10: IDTA 02047·02006 PDF, arXiv 초록 3건, Frontiers 전문, KCI 초록, CGH 공지, OPC Foundation 참조 페이지, 로봇신문 기사). 재사용 출처 없음(참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 전체 868건과의 URL 중복을 대조하지 못했으므로 Open-RMF 튜토리얼·VDA 5050 저장소·MassRobotics 저장소는 퍼블리셔가 기존 id 로 합칠 수 있다). 교차 확인 3건(f7: VDA·MassRobotics·IDTA, f14: Open Robotics·타르투대학교, f22: LAAS·헬무트 슈미트 대학 계열·Abolhasani·Pan — 모두 발행 주체가 다름). 신뢰도 high 는 f7·f14 두 건(각각 원문을 연 high 신뢰도 출처 포함), 나머지 medium 이하. 분류 원문 핵심 질문(제조사도 형식도 다른 로봇을 빠르고 믿을 수 있게 등록)에는 f3·f7(제조사가 기계가독 기록을 제공하고 로봇이 요청에 게시), f12·f14(등록은 설정 파일+API 구현), f19·f20·f21·f22(문서·URDF 에서 자동 추출 후 검증·사람 검토), f15(벤더 사전 평가 관문)로 답했으며 결론은 '식별·제원은 세 표준이 겹치게 정해 두었지만 능력 추출의 근거 연결형 검토와 형식 간 대응은 확인되지 않았다'는 추정(f11·f23·f24)이다. 현장 유형: 병원(f13 타르투대학교병원, f15 싱가포르 공공 의료기관), 기타(f16 인천공항, 벤더 주장)만 확인했고 제조 공장·물류창고·상업 시설·가정·실외 사례는 없다(제조 공장 후보 MDPI 논문은 403). 국내 자료는 KCI 논문(f17)과 로봇신문 기사(f16) 두 건이며 국내 운영 사례는 찾지 못해 oq-128 은 미해결이다. L. AI·학습 기술 관련 finding(f19~f23)은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 이 영역·55. 현장 조사·설치·시운전 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(IDTA 02047 의 TemporaryTechnicalData 는 f4 에 이름만 적음). 벤더 문서 출처는 없고 벤더 주장은 기사 경유 f16 한 건(vendor_claim). 용어집에 이미 있는 VDA 5050 팩트시트·신원 보고·자산관리셸·소프트웨어 명판·능력 기술 서브모델·의미 식별자·플릿 어댑터·플러그 앤 프로듀스는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-07/verification.json

```json
{
  "run_id": "2026-09-29-07",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. raw factsheet.schema(main) 열람: required 11개 속성 일치, mobileRobotConfiguration 선택이며 versions·network·batteryCharging 포함, headerId 설명 문구 일치. 발행일 없음(저장소 원문, 확인일 기준)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. typeSpecification 의 mobileRobotKinematics·mobileRobotClass·navigationTypes 열거값, localizationTypes·supportedZones, physicalParameters 의 속도·각속도·가감속·높이·폭·길이 항목 일치. 발췌의 '최대 적재 기준' 문구는 열람 응답에서 확인하지 못함(본문에 쓰지 않는다)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. VDA5050_EN.md(main) Version 3.0.0, 표 2 팩트시트 목적 문구 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control' 및 표 4 factsheetRequest 즉시 동작·factsheet 토픽(로봇 게시, 관제 구독) 일치."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인. PDF 는 도구가 본문을 추출하지 못했고, 공식 저장소 README(raw)에서 대상(intralogistics 무인 차량·로봇), commissioning·operation·maintenance, 전체 시스템 통합을 확인했으며 7개 컬렉션 이름은 공식 PDF 의 검색 결과 요약에서 확인. '디지털 명판·기술 데이터 서브모델과 연계' 구절은 어디서도 확인하지 못함 → 제외 또는 미확인 표시 지시. 발행 2025-03."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: PDF 본문은 도구가 추출하지 못했고, IDTA 02006 3.0 변경 이력(검색 결과)에 따르면 YearOfConstruction 이 [1]→[0..1] 로, OrderCodeOfManufacturer 가 [0..1]→[1] 로 바뀌어 브리프의 '필수 6개' 목록과 어긋난다. 필수·선택 구분은 미확인으로 두고 추가 조사 대상. 판 표기: 3.0 은 2024-11 게시(/en/ 경로 파일), 인용 URL 은 3.0.1(2025-10) 파일."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. AMR_Interop_Standard.json(raw) identityReport 필수 6개(uuid·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope), 선택 항목(maxSpeed·maxRunTime·chargerType·supportVendorName·productDocumentation·cargoType·cargoMaxVolume·cargoMaxWeight 등) 및 robotSerialNumber 설명 문구 일치. 파일에 판·날짜 없음."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": true,
      "tag_decision": "강등",
      "note": "사실 → 추정(high → medium): 세 출처(VDA·MassRobotics·IDTA) 모두 열어 대조했고 제조사명·기종·일련번호가 공통임은 맞지만, 디지털 명판(IDTA 02006)에는 치수·최대 적재·최대 속도 항목이 없어 '셋 모두 … 치수·최대 적재·최대 속도를 공통으로 담는다'는 서술은 과장이다. 공통 항목을 제조사명·기종(시리즈)·일련번호로 좁히고 치수·적재·속도는 VDA 5050·MassRobotics 두 형식의 공통 항목으로 서술하도록 지시."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인. OPC Foundation 참조 사이트: Version 1.02, 2025-09-08, 5장 사용 사례(감독·상태 감시·자산 관리·원격 운영), 7.2.2 표 13 MotionDeviceType 필수 속성 Manufacturer·Model·SerialNumber·ProductCode 확인. SoftwareRevision 은 MotionDeviceType 표에 없고 ControllerType 절은 열람 상한(출처당 2회)으로 확인하지 못함 → SoftwareRevision·Controller 부분은 제외 또는 미확인 표시 지시."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 제공 형식 STS XML, 'Markdown (AI Friendly, Low Token Count)', 'RAG Chunks (JSONL for Ollama/local models)' 일치. '배포하기 시작했다'는 시점 표현은 근거가 없어 '제공한다'로 쓰도록 지시."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. aas-specs-api README(raw): 최신 릴리스 3.2.0, 서비스 명세 9종 이름 일치. 레지스트리·디스커버리의 목적 문장은 README 에 없음(브리프도 그렇게 적음)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지, low). 세 표준 산출물의 역할을 조합한 추론이며 운영 사례 미확인을 스스로 밝힘. 자산 ID→AAS ID→엔드포인트 순서는 원문 미열람이므로 본문에 단정하지 않는다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 튜토리얼 원문(raw): config.yaml 의 limits [0.5, 0.75]/[0.6, 2.0], profile footprint·vicinity, reversible, battery·mechanical·ambient·tool system, recharge_threshold·recharge_soc, task_capabilities(loop·delivery·clean), robots 별 charger, RobotAPI 6개 메서드 일치. 발행일 없음."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Frontiers 전문(2022-08-23): 타르투대학교병원, TIAGo 주 배치(Jackal 은 시뮬레이션 이기종 시험, MiR100+UR5e 향후), FreeFleet 클라이언트(탑재 컴퓨터)+서버, 어댑터 설정 파일의 배터리·속도·발자국, 서보 장치로 카드 인식·근접 센서 작동, 중환자실→검사실 혈액 검체 운반 일치. 현장 유형 병원."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-153·ref-874 원문을 각각 열어 '설정 파일(제원·배터리) + 로봇 측 API·클라이언트' 구조를 대조. 발행 주체가 다르고 인용 관계 아님 → high 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CGH CHART 공지: 시행 2025-05-01, 갱신 2026-08-24, MOH 가 모든 PHI 의 자동화 통합 플랫폼으로 RoMi-H 인정, 기술·배치 역량 평가, 2년 유효, bi-annual 프로그램, 등재 5곳 이름 일치. 등재 평가의 기술 항목은 공지에 없음."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정·벤더 주장 유지). 로봇신문 2025-11-09(수정 2025-12-01): '국내 첫 이기종 로봇 통합관제 솔루션', 50대 이상 동시 제어, 엘리베이터 탑승, 2024-10 LG CNS 와 인천공항 사업 계약 문구 일치. VDA 5050·연동 제조사 수·등록 방식 언급 없음 확인 → 본문에 VDA 5050 을 쓰지 않는다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI: 한국디지털산업학회지 29(4) 203-213, 2024, 저자 일치, 초록에 AAS 기록·JSON 송수신·OPC UA 실시간 모니터링 있음, 현장 적용 결과 없음. 초록만 확인."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지). f16·f17 확인 결과와 부합. oq-128 미해결 판정 인정."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2606.17073(2026-06-10, Dussard·Sarthou, LAAS) 초록: 식별자의 의미 부족, 기존 온톨로지 개념 프롬프트, 다수결, 구문·스키마 검증, 여러 로봇 기술 평가 일치. 정확도 수치·사람 검증 없음 → 본문에 수치 쓰지 않는다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2406.07962(v2 2024-10-18) 초록: manual and error-prone, 소수 예시 프롬프트, 구문→모순→환각·누락 검증 루프, 최종 사람 검토만 필요 문구 일치. 정량 결과 없음."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2412.00608(v2 2024-12-10) 초록: OntoKGen, 신뢰성·유지보수성 도메인, 적응형 반복 사고 연쇄, 사용자가 최종 온톨로지 완전 통제, '보편적으로 옳은 온톨로지 없음', Neo4j·RAG 일치."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-239·ref-465·ref-883 초록을 각각 열어 자동 검증·사용자 최종 검토 결합을 대조. 세 연구 그룹이 독립. 프리프린트 초록 확인이므로 medium 유지."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지, low). 세 초록에 원문 절·줄 위치 인용 항목이 없음을 확인. 미확인 요구로 서술하고 열린 질문과 연결."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지, low). 인용 finding(f3·f4·f12·f14·f15)이 검증을 통과했고 분류 원문 19장 경계에 맞는 조합. 9절에 [추정]으로만 쓴다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지, low). '연계 대상: ' 표시가 있고 로봇 자체 지능·제어 경계에 맞음. 위치추정·주행 방식 필드는 f2 로 확인."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지). 연결 대상 영역의 번호·이름이 부록 A 와 일치하고 교차 규칙(매뉴얼 해석은 4·55번) 적용이 맞음. 10절에서 번호+이름으로 쓴다."
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
      "출처 id ref-228 가 직전 실행 2026-09-29-06 의 ref-228(Nandkumar·Peternel, Frontiers 2025)와 충돌한다 — 이번 브리프의 ref-228 는 VDA 5050 factsheet.schema 이므로 퍼블리셔가 참고문헌 등록 시 번호 충돌을 확인해 새 id 를 부여해야 한다(내용 중복 아님)",
      "ref-153(Open-RMF 플릿 어댑터 튜토리얼)·ref-031(VDA5050_EN.md)·ref-230(MassRobotics 저장소)는 전체 참고문헌 868건 안에 같은 URL 이 이미 있을 수 있다 — 입력 목록이 0건 요약이라 대조하지 못했으며 퍼블리셔가 URL 로 합친다",
      "5. 로봇 능력·작업 표현 페이지의 '표현 표준 정렬'(VDA 5050 팩트시트·자산 관리 셸 대응)과 이 페이지 7절이 주제상 겹치나 모순은 없음 — 10절에서 연결하고 팩트시트 필드 설명은 이 페이지에 둔다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f5: [사실] → [추정]으로 강등하고 '필수 6개(제품 URI·제조사·제품명·일련번호·제조 연도·제조일)·선택 5개' 구분을 본문에서 뺀다. 디지털 명판이 제조사명·제품명·일련번호·제조일·하드웨어·펌웨어·소프트웨어 버전 같은 식별·버전 항목을 담는다는 수준으로만 쓰고 필수·선택 구분은 '미확인'으로 남긴다 — IDTA 02006 3.0 변경 이력에 따르면 YearOfConstruction 은 [0..1]로 바뀌었고 OrderCodeOfManufacturer 가 [1]로 바뀌어 브리프 목록과 어긋나며, PDF 본문은 검증 도구가 추출하지 못했다. 정확한 필수·선택 목록은 additional_research_requests 로 넘긴다.",
    "glossary_candidates '디지털 명판' 정의에서 '제품 URI·제조사·제품명·일련번호·제조 연도·제조일을 필수로 담고 … 선택으로 두는' 구절을 지우고 필수·선택 구분 없이 식별·버전 항목을 담는 서브모델로 고친다 — f5 강등과 같은 이유.",
    "f7: [사실] → [추정]으로 강등하고(신뢰도 high → medium) 세 형식의 공통 항목을 '제조사명·기종(시리즈)·일련번호'로 좁힌다. 치수(외곽)·최대 적재·최대 속도는 VDA 5050 팩트시트와 MassRobotics identityReport 두 형식의 공통 항목으로만 쓴다 — 디지털 명판(IDTA 02006)에는 치수·적재·속도 항목이 없다.",
    "f8: OPC UA for Robotics 의 식별 속성은 MotionDevice 의 Manufacturer·Model·SerialNumber·ProductCode 네 가지만 [사실]로 쓰고, SoftwareRevision 과 Controller 의 식별 속성은 본문에서 빼거나 '미확인'으로 표시한다 — 7.2.2 MotionDeviceType 표에 SoftwareRevision 이 없고 ControllerType 절은 열람 상한으로 확인하지 못했다.",
    "f4: 'IDTA 02047 이 디지털 명판·기술 데이터 서브모델과 연계된다'는 구절을 빼거나 '미확인'으로 표시한다 — 공식 README 와 PDF 검색 요약 어디에도 없다. 7개 컬렉션 이름과 혼합 플릿 통합·시운전·운영·유지보수 목표는 확인됐으므로 그대로 쓴다.",
    "f9: 'AI 응용용 마크다운·RAG 청크 형식으로 배포하기 시작했다'의 '시작했다'를 '제공한다'로 바꾼다 — 제공 형식(STS XML·Markdown(AI Friendly)·RAG Chunks(JSONL))은 확인됐으나 제공 시작 시점은 근거가 없다.",
    "f19·f20·f21: 정확도·정량 결과를 본문에 쓰지 않는다 — 세 초록 모두 수치가 없다. f22 는 [사실] medium 유지.",
    "f16: [추정]에 '벤더 주장'을 병기하고 '국내 첫'·'50대 이상'을 기사 인용임을 밝혀 쓴다. VDA 5050 지원·연동 제조사 수·등록 방식은 기사에 없으므로 본문에 쓰지 않는다(확인).",
    "5. 적용 사례 (현장 유형 명시): 사례마다 현장 유형을 이름으로 밝히고 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과)에 놓는다 — 병원(f13 타르투대학교병원 검체 운반, f15 싱가포르 공공 의료기관 RoMi-H 등재), 기타(f16 인천공항, 벤더 주장 병기). 물류창고·제조 공장·상업 시설·가정·실외 사례는 이번 조사에서 확인되지 않았음을 서술하고 물류창고를 기본값으로 쓰지 않는다. site_matrix_updates 의 site_type 은 이 현장 유형과 같아야 한다.",
    "9. ROP가 직접 맡는 것과 외부와 연계하는 것: f24·f25 는 [추정]으로만 쓰고, f25 의 위치추정·주행 방식·펌웨어 버전은 분류 원문 19장 '로봇 자체 지능·제어'의 연계 대상으로 짧게 다룬다.",
    "11. 열린 질문: oq-128 은 해결로 바꾸지 않고 f17·f18 로 부분 진전(국내 설계 연구·벤더 소개만 확인, 운영 사례 미확인)임을 적는다. open_questions_new 4건은 브리프 형식대로 등록한다(근거 f23·f7·f15·f12).",
    "f11·f23: [추정] low 로 유지하고 '확인되지 않았다'는 서술을 남긴다. f11 의 자산 ID→AAS ID→엔드포인트 순서는 원문 미열람이므로 본문에 단정하지 않는다.",
    "각주: ref-239·ref-465·ref-883 은 arXiv 초록 확인, ref-043 은 KCI 초록 확인임을 8절 서술에 밝힌다. ref-198·ref-876 PDF 는 접근일 뒤 ' (원문 미열람)' 표기를 붙이지 않는다(리서치가 열람했고 검증은 README·검색 요약으로 대신 확인)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 2건(f5·f7), 교차 확인 3건(f7·f14·f22). 강등: f5 사실 → 추정(IDTA 02006 3.0 변경 이력과 필수 목록 불일치), f7 사실 → 추정(디지털 명판에 치수·적재·속도 항목 없음, high → medium). 원문 미열람 출처: 없음 — 다만 ref-198·ref-876 PDF 는 검증 도구가 본문을 추출하지 못해 공식 저장소 README(raw)와 검색 결과 요약으로 대신 확인했고, ref-881 은 5장·7.2.2 절까지만 열어 ControllerType 의 SoftwareRevision 은 확인하지 못했다. 주의: 출처 id ref-228 가 직전 실행 2026-09-29-06 의 ref-228 와 충돌하므로 퍼블리셔가 새 id 를 부여해야 한다. 국내 운영 사례는 확인되지 않아 oq-128 은 미해결이며, 병원 외 현장 유형 사례가 없다. 9절의 직접 범위·연계 경계는 모두 [추정]이다. 미사용 출처 없음. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-29-07/pages.json

```json
{
  "run_id": "2026-09-29-07",
  "outline": [
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "세 발행 기관이 제조사 제공 기계가독 등록 기록을 정하며 제조사명·기종·일련번호가 공통으로 보인다. [추정][^ref-228][^ref-230][^ref-876] 플릿 등록은 어댑터 설정 파일과 로봇 API 구현의 두 부분으로 이루어진다. [사실][^ref-153][^ref-874]",
      "planned_findings": [
        "f7",
        "f14",
        "f15",
        "f3"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1100,
      "summary": "팩트시트·디지털 명판·AGV 기술 데이터 서브모델·신원 보고·레지스트리·URDF·온톨로지 채우기·어댑터 설정을 정의한다. [사실][^ref-228] [추정][^ref-876]",
      "planned_findings": [
        "f1",
        "f2",
        "f5",
        "f4",
        "f6",
        "f10",
        "f19",
        "f12"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1300,
      "summary": "병원 사례 2건(타르투대학교병원 검체 운반, 싱가포르 RoMi-H 등재)과 기타(인천공항, 벤더 주장). [사실][^ref-874][^ref-878] [추정] 벤더 주장[^ref-875]",
      "planned_findings": [
        "f13",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "팩트시트 요청·신원 보고, 자산관리셸 경로(추정), 어댑터 설정+API, 문서·URDF 추출과 사람 검토, 표준 문서의 AI 가독 형식. [사실][^ref-031][^ref-153][^ref-239][^ref-465][^ref-883][^ref-881] [추정][^ref-880]",
      "planned_findings": [
        "f3",
        "f6",
        "f11",
        "f10",
        "f12",
        "f14",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f9"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "VDA 5050 팩트시트, IDTA 02047, IDTA 02006, MassRobotics, OPC UA Robotics, 자산관리셸 API, Open-RMF 플릿 어댑터, RoMi-H 등재 프로그램 표. [사실][^ref-228][^ref-198][^ref-230][^ref-881][^ref-880][^ref-153][^ref-878]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f8",
        "f10",
        "f12",
        "f15"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 750,
      "summary": "병원 현장 시험 전문, 언어 모델 추출 연구 3건(arXiv 초록), 국내 자산관리셸 설계 연구(KCI 초록). [사실][^ref-874][^ref-239][^ref-465][^ref-883][^ref-043]",
      "planned_findings": [
        "f13",
        "f19",
        "f20",
        "f21",
        "f17"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 700,
      "summary": "등록부·수집 경로·검토 승인 기록·어댑터 설정 초안·승인 관문은 직접 범위로 보이고, 위치추정·주행 방식·펌웨어 성능은 제조사 소유 연계 대상이다. [추정][^ref-031][^ref-198][^ref-153][^ref-878] [추정][^ref-228][^ref-031]",
      "planned_findings": [
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "5·6·7·20·21·45·47·55·57·63 영역과 매뉴얼 기반 로봇 기능 온톨로지 트랙에 연결한다. [추정][^ref-239][^ref-198][^ref-153]",
      "planned_findings": [
        "f26",
        "f13",
        "f15"
      ]
    },
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "oq-128 은 국내 설계 연구·벤더 소개만 확인되어 미해결이며 새 질문 4건을 올린다. [추정][^ref-043][^ref-875]",
      "planned_findings": [
        "f18",
        "f23",
        "f7",
        "f15",
        "f12"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/robot-ontology/heterogeneous-robot-registration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 섹션 3~11 신규 작성(finding 26건 반영, 1차 조건부 승인 수정 13건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2. 출처 id ref-228 는 직전 실행과 충돌하므로 퍼블리셔가 새 id 를 부여해야 한다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"4. 핵심 개념과 용어\" 절(2,184자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"6. 대표 접근법과 기술\" 절(1,749자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"8. 대표 연구와 자료\" 절(1,238자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,149자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"11. 열린 질문\" 절(1,109자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(805자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area04-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 4. 이기종 로봇 등록 의 \"3. 왜 중요한가\" 절(734자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 4. 이기종 로봇 등록 | 영역 심화: 섹션 3~11 신규 작성(병원 사례 2건·기타 1건, 표준 8종, 언어 모델 추출 연구 3건), 1차 조건부 승인 수정 13건 이행 | run 2026-09-29-07",
  "index_updates": {
    "home_recent": "2026-09-29 — 4. 이기종 로봇 등록: 영역 심화로 3~11절 신규 작성. VDA 5050 팩트시트·자산관리셸 서브모델·MassRobotics 신원 보고의 등록 항목, Open-RMF 어댑터 설정과 병원 현장 등록 사례, 문서·URDF 능력 추출과 사람 검토 연구를 정리했다",
    "category_recent": "2026-09-29 — 4. 이기종 로봇 등록: 영역 심화, 3~11절 신규 작성(신뢰도 medium, 새 출처 15건, 새 열린 질문 4건, oq-128 은 미해결)",
    "area_recent": "2026-09-29 — 실행 2026-09-29-07: 3~11절 신규 작성. 1차 조건부 승인 수정 13건 이행(디지털 명판·세 형식 공통 항목 강등, OPC UA 식별 속성 축소, 벤더 주장 병기)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "digital-nameplate",
      "term_ko": "디지털 명판",
      "term_en": "Digital Nameplate (IDTA 02006)",
      "definition": "제조사명·제품명·일련번호·제조일과 하드웨어·펌웨어·소프트웨어 버전 같은 식별·버전 항목을 담는 자산관리셸 서브모델로, 산업 장비의 명판 정보를 기계가독 형식으로 교환하게 한다.",
      "description": "IDTA 02006 3.0 판의 필수·선택 항목 구분은 이번 실행에서 확인하지 못했다(미확인). 로봇 등록 시 제조사 제공 식별 기록의 한 형식이다.",
      "related_areas": [
        4,
        21,
        57
      ],
      "sources": [
        "ref-876"
      ]
    },
    {
      "action": "new",
      "slug": "agv-technical-data-submodel",
      "term_ko": "AGV 기술 데이터 서브모델",
      "term_en": "Technical Data for AGV in Intralogistics (IDTA 02047)",
      "definition": "실내 물류용 AGV·AMR 의 유형·기술 매개변수·VDA 5050 팩트시트·에너지·통신·배터리·안전·임시 기술 데이터를 컬렉션으로 나눠 담는 자산관리셸 서브모델 템플릿이다.",
      "description": "IDTA 02047-1-0(2025-03). 혼합 플릿을 중앙 관제에 통합하고 시운전·운영·유지보수에 걸쳐 쓰는 것을 목표로 한다.",
      "related_areas": [
        4,
        5,
        21
      ],
      "sources": [
        "ref-198"
      ]
    },
    {
      "action": "new",
      "slug": "urdf",
      "term_ko": "통합 로봇 기술 형식",
      "term_en": "Unified Robot Description Format (URDF)",
      "definition": "로봇의 링크와 관절로 구조·운동학·물리 속성을 기술하는 ROS 계열의 XML 형식으로, 식별자 자체에는 의미가 없어 온톨로지로 옮기려면 해석이 필요하다.",
      "description": "URDF 공식 문서는 이번 실행에서 열지 못했고, 정의는 URDF 온톨로지 채우기 연구의 초록에 기댄다.",
      "related_areas": [
        4,
        5,
        45
      ],
      "sources": [
        "ref-239"
      ]
    },
    {
      "action": "new",
      "slug": "aas-registry-and-discovery",
      "term_ko": "자산관리셸 레지스트리·디스커버리",
      "term_en": "AAS Registry / Discovery",
      "definition": "자산관리셸 API 명세(IDTA-01002)가 정한 서비스로, 등록된 자산관리셸과 서브모델의 서술자를 관리하고 자산 식별자로 해당 자산관리셸을 찾게 한다.",
      "description": "IDTA-01002 3.2.0 판은 AAS·서브모델 저장소, AAS·서브모델 레지스트리, 디스커버리, 개념 설명 저장소, AASX 파일 서버 등 서비스 명세 9종을 둔다. 디스커버리와 레지스트리를 부르는 순서는 원문 미열람으로 미확인.",
      "related_areas": [
        4,
        6,
        21
      ],
      "sources": [
        "ref-880"
      ]
    },
    {
      "action": "new",
      "slug": "ontology-population",
      "term_ko": "온톨로지 채우기",
      "term_en": "Ontology Population",
      "definition": "이미 정해진 온톨로지의 개념·관계에 맞춰 문서·모델 파일 같은 원천에서 개체와 관계 인스턴스를 뽑아 채우는 작업으로, 언어 모델을 쓸 때는 검증과 사람 검토를 함께 둔다.",
      "description": "URDF 를 언어 모델로 해석해 로봇 온톨로지를 채우는 연구는 여러 번 질의한 다수결과 구문·스키마 검증으로 출력을 제약한다.",
      "related_areas": [
        4,
        45,
        47
      ],
      "sources": [
        "ref-239"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-228",
      "org": "VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소",
      "title": "VDA5050/json_schemas/factsheet.schema (main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDA 5050 팩트시트 메시지의 JSON 스키마 원본. 필수·선택 속성과 typeSpecification·physicalParameters 필드 정의를 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-198",
      "org": "Industrial Digital Twin Association (IDTA)",
      "title": "IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics",
      "published": "2025-03",
      "url": "https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "실내 물류 AGV·AMR 의 기술 데이터를 자산관리셸 서브모델로 표준화한 명세. VDA 5050 팩트시트 컬렉션을 포함하고 혼합 플릿의 중앙 관제 통합을 목표로 한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics (AMR Interoperability Working Group)",
      "title": "AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. identityReport·statusReport 메시지와 필수·선택 필드를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06-10",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "URDF 모델을 언어 모델로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 방법. 다수결과 구문·스키마 검증으로 출력을 제약한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-153",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 플릿 어댑터를 만드는 튜토리얼. 플릿·로봇 설정 파일(config.yaml)의 항목과 로봇 측 RobotAPI 가 구현할 메서드를 적는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-874",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "타르투대학교병원에서 Open-RMF 와 FreeFleet 으로 이기종 로봇을 등록·운용해 혈액 검체를 운반한 현장 시험. 등록 설정과 문 통과용 보조 장치를 기술한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-875",
      "org": "로봇신문",
      "title": "[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막",
      "published": "2025-11-09",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=43274",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "클로봇의 이기종 로봇 통합관제 솔루션 크롬스를 소개한 기사. 50대 이상 동시 제어·엘리베이터 탑승과 인천공항 다기종 로봇 사업 계약을 전한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-876",
      "org": "Industrial Digital Twin Association (IDTA)",
      "title": "IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment",
      "published": null,
      "url": "https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "산업 장비의 디지털 명판 서브모델 3.0 판 명세. 제조사·제품명·일련번호·제조일과 하드웨어·펌웨어·소프트웨어 버전 같은 식별·버전 항목을 둔다. 필수·선택 구분은 검증에서 미확인으로 남았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-043",
      "org": "신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4))",
      "title": "자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계",
      "published": "2024",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "AMR 의 하드웨어·소프트웨어 정보를 자산관리셸로 기록해 JSON 으로 교환하고 OPC UA 로 감시하는 시스템 설계를 제안한 국내 논문. KCI 초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-878",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "RoMi-H Empanelment Programme 2025",
      "published": "2025-05-01",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "싱가포르 공공 의료기관의 로봇 통합 플랫폼 RoMi-H 에 시스템 통합사를 평가·등재하는 프로그램 공지. 등재 요건·유효 기간·등재 업체 5곳을 적는다(2026-08-24 갱신).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소",
      "title": "VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDA 5050 명세 3.0.0 판 원문(마크다운). 팩트시트의 목적과 factsheetRequest 즉시 동작·factsheet 토픽을 통한 요청·게시 방식을 적는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-880",
      "org": "Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소",
      "title": "aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README)",
      "published": null,
      "url": "https://github.com/admin-shell-io/aas-specs-api",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "자산관리셸 API 명세(IDTA-01002)의 공식 OpenAPI 저장소 README. 최신 3.2.0 판과 레지스트리·디스커버리를 포함한 서비스 명세 9종을 나열한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-881",
      "org": "OPC Foundation",
      "title": "OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02)",
      "published": "2025-09-08",
      "url": "https://reference.opcfoundation.org/Robotics/v100/docs/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "산업용 로봇의 수직 통합·자산 관리·상태 감시를 위한 OPC UA 정보 모델(MotionDeviceSystem). MotionDevice 의 Manufacturer·Model·SerialNumber·ProductCode 식별 속성을 정의하고 AI 응용용 마크다운·RAG 청크 형식도 제공한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-10-18",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 능력 설명을 소수 예시 프롬프트로 언어 모델에 넣어 능력 온톨로지를 생성하고 자동 검증 루프 뒤 사람이 최종 검토하는 방법. 초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    },
    {
      "id": "ref-883",
      "org": "Abolhasani, M. S., & Pan, R.",
      "title": "Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation",
      "published": "2024-12-10",
      "url": "https://arxiv.org/abs/2412.00608",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "기술 문서에서 언어 모델로 온톨로지·지식 그래프를 추출하되 대화형 인터페이스에서 사용자가 최종 결정을 갖게 하는 OntoKGen 파이프라인. 초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/robot-ontology/heterogeneous-robot-registration.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-128",
      "question": "국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가?",
      "areas": [
        10,
        4,
        21
      ],
      "status": "열림",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#11-열린-질문"
    },
    {
      "action": "new",
      "question": "문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가?",
      "areas": [
        4,
        45,
        7
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가?",
      "areas": [
        4,
        21,
        5
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가?",
      "areas": [
        4,
        63,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가?",
      "areas": [
        4,
        5,
        6
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시",
      "title": "4. 이기종 로봇 등록"
    }
  ],
  "standards_updates": [
    {
      "name": "IDTA 02006 Digital Nameplate for Industrial Equipment (3.0)",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf",
      "related_areas": [
        4,
        21,
        57
      ],
      "summary": "산업 장비의 식별·버전 항목을 담는 자산관리셸 디지털 명판 서브모델. 필수·선택 항목 구분은 이번 실행에서 미확인.",
      "ref_id": "ref-876"
    },
    {
      "name": "IDTA-01002 Asset Administration Shell Specification — API (3.2.0)",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/aas-specs-api",
      "related_areas": [
        4,
        6,
        21
      ],
      "summary": "자산관리셸 API 명세. AAS·서브모델 저장소, AAS·서브모델 레지스트리, 디스커버리, 개념 설명 저장소, AASX 파일 서버 등 서비스 명세 9종을 둔다.",
      "ref_id": "ref-880"
    },
    {
      "name": "RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재)",
      "kind": "평가 프로그램",
      "org": "Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology)",
      "url": "https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste",
      "related_areas": [
        4,
        63,
        58
      ],
      "summary": "Open-RMF 기반 RoMi-H 에 로봇을 연동할 시스템 통합사를 기술·배치 역량 평가로 등재하는 프로그램(2025-05-01 시행, 등재 2년 유효, 2026-08-24 기준 5곳).",
      "ref_id": "ref-878"
    }
  ],
  "additional_research_requests": [
    "4절·7절 디지털 명판(IDTA 02006 3.0)의 정확한 필수·선택 속성 목록 — PDF 본문을 열어 YearOfConstruction·OrderCodeOfManufacturer 의 카디널리티 변경까지 확인해야 f5 를 [사실]로 되돌릴 수 있다",
    "7절 OPC UA for Robotics(OPC 40010-1 1.02) ControllerType 의 식별 속성과 SoftwareRevision 유무 — 이번 검증이 열람 상한으로 확인하지 못해 본문에서 뺐다",
    "4절·6절 IDTA 02047 서브모델의 개별 속성명과 VDA 5050 팩트시트 필드 대응 세부, 그리고 디지털 명판·기술 데이터 서브모델과의 연계 여부 — 검색 요약과 README 에서 확인하지 못해 서술을 컬렉션 이름 수준으로 제한했다",
    "6절 자산관리셸 디스커버리·레지스트리 호출 순서(자산 ID→AAS ID→엔드포인트) — IDTA Part 2 원문 미열람으로 본문에 단정하지 않았다",
    "5절 제조 공장·물류창고·상업 시설·가정·실외 현장의 이기종 로봇 등록 사례 — 제조 공장 후보(MDPI Applied Sciences 다중 브랜드 플릿 통합)는 403 으로 열지 못했다",
    "5절 RoMi-H 등재 평가의 기술 항목(어댑터 시험·적합성 검사 등) — 공지에 없어 미확인",
    "4절 URDF 공식 문서 — wiki.ros.org·docs.ros.org 를 열지 못해 URDF 정의를 arXiv 초록에 기댔다",
    "11절 oq-128 국내 운영 사례 — 중기부 스마트공장 고도화 사업의 AAS 적용 의무화 문구가 검색 요약에만 보여 확인이 필요하다"
  ],
  "fixes_applied": [
    "f5 강등 — 4절 디지털 명판 항목과 7절 표를 [추정][^ref-876]으로 쓰고 '필수 6개·선택 5개' 구분을 뺐으며 식별·버전 항목을 담는다는 수준으로만 서술하고 필수·선택 구분은 '미확인'으로 남겼다. 정확한 목록은 additional_research_requests 1번으로 넘겼다",
    "용어집 '디지털 명판' 정의 수정 — glossary_updates 에서 필수·선택 구절을 지우고 식별·버전 항목을 담는 서브모델로 고쳤으며 description 에 필수·선택 미확인을 적었다",
    "f7 강등 — 3절에서 세 형식의 공통 항목을 제조사명·기종(시리즈)·일련번호로 좁혀 [추정][^ref-228][^ref-230][^ref-876]으로 쓰고, 치수·최대 적재·최대 속도는 VDA 5050 팩트시트와 MassRobotics identityReport 두 형식의 공통 항목으로만 별도 문장([추정][^ref-228][^ref-230])에 썼다",
    "f8 축소 — 7절 표의 OPC UA for Robotics 행에 MotionDevice 의 Manufacturer·Model·SerialNumber·ProductCode 네 가지만 [사실]로 쓰고 Controller 의 식별 속성과 SoftwareRevision 은 '미확인'으로 표시했다. reference_updates 의 ref-881 요약도 같은 범위로 고쳤다",
    "f4 구절 제거 — 4절 AGV 기술 데이터 서브모델 항목과 7절 표에서 '디지털 명판·기술 데이터 서브모델과 연계' 구절을 빼고 7개 컬렉션 이름과 혼합 플릿 통합·시운전·운영·유지보수 목표만 [사실][^ref-198]으로 썼다",
    "f9 표현 수정 — 6절 '표준 문서 자체의 기계가독 형식'에서 '배포하기 시작했다'를 '제공한다'로 썼다",
    "f19·f20·f21 정량 결과 제외 — 6절·8절에 정확도 수치를 쓰지 않았고 6절에 '정량 결과는 초록에 없어 적지 않는다'고 밝혔으며 f22 는 [사실][^ref-239][^ref-465][^ref-883]으로 유지했다",
    "f16 벤더 주장 병기 — 5절 기타 사례와 8절에서 [추정] 벤더 주장[^ref-875]으로 쓰고 '국내 첫 이기종 로봇 통합관제 솔루션'과 '50대 이상'을 기사 인용임을 밝혀 썼으며 VDA 5050 지원·연동 제조사 수·등록 방식은 쓰지 않았다",
    "5절 현장 유형 명시 — 병원 2건(타르투대학교병원 검체 운반 f13, RoMi-H 등재 f15)과 기타 1건(인천공항 f16)을 각각 현장 유형·사례·여섯 항목 표·서술로 썼고, 물류창고·제조 공장·상업 시설·가정·실외 사례는 확인되지 않았음을 절 첫 문장에 적었으며, site_matrix_updates 의 site_type 을 병원·기타로만 냈다",
    "9절 경계 — f24·f25 를 [추정]으로만 쓰고 f25 의 위치추정·주행 방식·펌웨어 버전은 '연계 대상:' 단락에서 분류 원문 19장 '로봇 자체 지능·제어' 행의 연계 대상으로 짧게 다뤘다",
    "11절 열린 질문 — oq-128 을 해결로 바꾸지 않고 f17·f18 로 부분 진전(국내 설계 연구·벤더 소개만 확인, 운영 사례 미확인)임을 적었으며 open_questions_new 4건을 브리프 형식대로 open_question_updates 에 new 로 등록했다(근거 f23·f7·f15·f12)",
    "f11·f23 유지 — 6절에서 둘 다 [추정]으로 쓰고 '확인되지 않았다'는 서술을 남겼으며, f11 의 자산 ID→AAS ID→엔드포인트 순서는 '원문을 열지 못해 단정하지 않는다'고 적었다",
    "각주 표기 — 8절에서 ref-239·ref-465·ref-883 은 arXiv 초록으로, ref-043 은 KCI 초록만 확인했음을 밝혔고, ref-198·ref-876 의 각주 정의에 ' (원문 미열람)'을 붙이지 않았다",
    "분량 초과 자동 분리: 4. 이기종 로봇 등록 본문 11,446자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,109자"
  ]
}
```

### runs/2026-09-29-07/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area04-s4.md (2,184자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area04-s6.md (1,749자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area04-s8.md (1,238자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area04-s7.md (1,149자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area04-s11.md (1,109자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area04-s10.md (805자)
    - docs/categories/robot-ontology/heterogeneous-robot-registration.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area04-s3.md (734자)
```

### runs/2026-09-29-07/pages/categories/robot-ontology/heterogeneous-robot-registration.md

```markdown
---
title: "4. 이기종 로봇 등록"
type: area
category: "B. 로봇 온톨로지"
area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [VDA 5050 팩트시트, 자산관리셸, 디지털 명판, 신원 보고, 플릿 어댑터, 온톨로지 채우기]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-228, ref-198, ref-230, ref-239, ref-153, ref-874, ref-875, ref-876, ref-043, ref-878, ref-031, ref-880, ref-881, ref-465, ref-883]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 4. 이기종 로봇 등록

# 4. 이기종 로봇 등록

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

제조사마다 식별·제원 정보의 이름과 형식이 다르므로, 등록을 빠르고 믿을 수 있게 하려면 제조사가 기계가독 형식으로 내는 기록과 그것을 받는 경로가 먼저 정해져야 한다. 서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하며, 제조사명·기종(시리즈)·일련번호는 세 형식에 공통으로 들어 있는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-876]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 왜 중요한가](../../topics/2026/2026-09-29-area04-s3.md)에 있다.

## 4. 핵심 개념과 용어

**VDA 5050 팩트시트(factsheet)** — 독일자동차산업협회(Verband der Automobilindustrie, VDA)와 독일기계설비제조업협회(VDMA)의 VDA 5050 에서 로봇이 자신의 제원을 관제에 알리는 메시지다.

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area04-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 병원 2건과 기타(공항) 1건이다. 물류창고·제조 공장·상업 시설·가정·실외의 등록 사례는 이번 조사에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 타르투대학교병원에서 자체 관제가 없는 로봇을 Open-RMF 에 등록해 혈액 검체 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 중환자실에서 검사실로 혈액 검체를 운반하는 작업. 요청이 발생하는 방식은 이번 브리프에 없어 미확인 |
| 작업 대상 | 혈액 검체와, 로봇이 지나야 하는 프로그램 제어가 없는 병원 문. [사실][^ref-874] |
| 수행 자원 | PAL Robotics TIAGo(로봇 탑재 컴퓨터의 FreeFleet 클라이언트), 플릿 이름·DDS 설정을 적은 FreeFleet 서버, 배터리·속도·발자국을 적은 RMF 어댑터 파일, 문의 카드 인식·근접 센서를 대신 작동시키는 서보 장치. [사실][^ref-874] |
| 제약 | 병원 문에 프로그램 제어가 없어 서보 장치를 만들어 카드 인식·근접 센서를 대신 작동시켜야 했다. [사실][^ref-874] |
| 완료·인계 | 미확인(브리프에 없음) |
| 예외·성과 | 미확인(브리프에 없음) |

Valner 외(2022)의 현장 시험은 자체 관제가 없는 로봇을 FreeFleet 클라이언트·서버와 어댑터 파일로 등록했다. [사실][^ref-874] 이 영역이 관여하는 칸은 수행 자원이다. 등록 때 적은 배터리·속도·발자국이 곧 기종 제원 기술이며, 문 통과용 보조 장치는 등록된 로봇 능력만으로 부족한 현장 조건을 설비 쪽에서 메운 예다.

**현장 유형:** 병원

**사례:** 싱가포르 공공 의료기관의 RoMi-H 등재 프로그램으로 시스템 통합사를 사전 평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 시스템 통합사가 공공 의료기관의 병원 제안 요청에 참여하려면 등재가 필요하다(2025-05-01 시행). [사실][^ref-878] |
| 작업 대상 | 통합사의 기술·배치 역량(평가 대상 정보). [사실][^ref-878] |
| 수행 자원 | 보건부(RoMi-H 를 공공 의료기관의 자동화 통합 플랫폼으로 지정), 창이종합병원 CHART(등재 운영), 시스템 통합사(2026-08-24 기준 등재 5곳). [사실][^ref-878] |
| 제약 | 기술·배치 역량 평가 통과, 등재 유효 기간 2년. [사실][^ref-878] |
| 완료·인계 | 등재가 확정되어야 병원 제안 요청 참여 자격이 생긴다. [사실][^ref-878] |
| 예외·성과 | 미확인(브리프에 없음) |

이 사례는 로봇이 아니라 로봇을 등록·연동할 주체를 사전 평가하는 관문이다. 평가의 기술 항목(어댑터 시험·적합성 검사 등)은 공지에 없어 미확인이다.

**현장 유형:** 기타

**사례:** 인천공항 다기종 로봇 제작·관제 구축 사업(기사가 전한 벤더 주장)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(기사에 없음) |
| 작업 대상 | 미확인(기사에 없음) |
| 수행 자원 | 여러 제조사의 로봇을 하나의 시스템에서 제어한다는 클로봇의 통합관제 솔루션 크롬스(기사 인용 "국내 첫 이기종 로봇 통합관제 솔루션", 50대 이상 동시 제어). [추정] 벤더 주장[^ref-875] |
| 제약 | 엘리베이터 탑승을 지원한다고 소개된다. [추정] 벤더 주장[^ref-875] |
| 완료·인계 | 미확인(기사에 없음) |
| 예외·성과 | 미확인(기사에 없음) |

로봇신문 기사(2025-11-09)는 클로봇이 LG CNS 와 함께 인천공항 다기종 로봇 제작·5G 디지털 트윈 관제 구축 사업을 계약했다고 전하지만, 연동 제조사 수와 등록 방식은 기사에 없다. [추정] 벤더 주장[^ref-875] 이 사례는 국내에 이기종 관제 사업이 있음을 보여 줄 뿐 등록 데이터 형식의 근거는 되지 않는다.

## 6. 대표 접근법과 기술

등록 데이터를 로봇에서 직접 받는 경로가 두 표준에 있다. VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에는 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다. [사실][^ref-031]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area04-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

전체 목록은 [표준 목록](../../standards/index.md)에 있다. 용어집의 [능력 기술 서브모델](../../glossary/capability-description-submodel.md)과 [소프트웨어 명판](../../glossary/software-nameplate.md)은 같은 자산관리셸 계열이지만 이번 브리프가 다루지 않아 표에 넣지 않았다.

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area04-s7.md)에 있다.

## 8. 대표 연구와 자료

Valner, R. 외(타르투대학교), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — 자체 관제가 없는 TIAGo 를 FreeFleet 과 어댑터 파일로 Open-RMF 에 등록하고, 프로그램 제어가 없는 병원 문을 서보 장치로 지나며 혈액 검체를 운반한 현장 시험. 등록 작업의 실제 구성을 보여 준다. [사실][^ref-874]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 대표 연구와 자료](../../topics/2026/2026-09-29-area04-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트·명판·신원 보고에 담긴 식별·제원·버전을 받아 등록부에 저장·대조하고 버전 변경을 추적한다 | 위치추정 방식·주행 방식·펌웨어·소프트웨어 버전이 가리키는 위치추정·회피 성능 자체는 제조사가 소유·갱신한다 |
| 업종별 조건 | 현장이 요구하는 벤더·통합사 사전 평가 결과를 등록 승인 관문의 제약으로 반영한다 | 의료 현장의 등재 제도 자체(평가 기준·운영)는 보건당국·병원의 몫이다 |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 제조사·기종·일련번호·펌웨어·SDK 버전·장착 장비를 담는 등록부, 팩트시트·자산관리셸·신원 보고를 받아 저장·대조하는 수집 경로, 문서·URDF 에서 뽑은 능력 초안의 검토·승인 기록, 어댑터 설정 초안 생성이며, 등록 승인 관문에 벤더·통합사 사전 평가를 둘 수 있을 것으로 보인다. [추정][^ref-031][^ref-198][^ref-153][^ref-878]

연계 대상: 팩트시트의 위치추정 방식·주행 방식과 mobileRobotConfiguration 의 펌웨어·소프트웨어 버전은 제조사가 소유·갱신하는 로봇 자체 지능·제어 정보이므로, 이종 제조사를 잇는 ROP 는 등록 시 이를 받아 저장·대조하고 버전 변경을 추적하는 데 그치고 위치추정·회피 성능 자체는 제조사에 맡겨야 할 것으로 보인다. [추정][^ref-228][^ref-031] 이 경계는 분류 원문 19장의 "로봇 자체 지능·제어" 행에 해당하며([범위 경계](../../about/scope-boundary.md)), 자사 로봇까지 만드는 회사라면 경계가 이동할 수 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) — 등록 때 받은 팩트시트·서브모델·신원 보고의 제원과 문서에서 뽑은 능력 초안이 능력 표현의 입력이 된다. 팩트시트 필드 설명은 이 페이지에 두고, 표현 표준 정렬은 저 페이지가 맡는다. [추정][^ref-198][^ref-153]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area04-s10.md)에 있다.

## 11. 열린 질문

**oq-128** (상태: 열림 · 실행 2026-09-29-07 에서 부분 진전) 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? — 이번 조사에서 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구와 벤더의 이기종 관제 소개뿐이며, 실제 등록 데이터로 운영에 쓴 국내 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-043][^ref-875]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 열린 질문](../../topics/2026/2026-09-29-area04-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-874]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-875]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-29
[^ref-876]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-043]: 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)), 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-29
[^ref-878]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29
```

### docs/categories/robot-ontology/heterogeneous-robot-registration.md

```markdown
---
title: "4. 이기종 로봇 등록"
type: area
category: "B. 로봇 온톨로지"
area_no: 4
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 4. 이기종 로봇 등록

# 4. 이기종 로봇 등록

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

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

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s4.md

```markdown
---
title: "4. 이기종 로봇 등록 — 핵심 개념과 용어"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-198, ref-230, ref-239, ref-153, ref-876, ref-880]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#4
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 핵심 개념과 용어

# 4. 이기종 로봇 등록 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **VDA 5050 팩트시트(factsheet)** — 독일자동차산업협회(Verband der Automobilindustrie, VDA)와 독일기계설비제조업협회(VDMA)의 VDA 5050 에서 로봇이 자신의 제원을 관제에 알리는 메시지다.
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **VDA 5050 팩트시트(factsheet)** — 독일자동차산업협회(Verband der Automobilindustrie, VDA)와 독일기계설비제조업협회(VDMA)의 VDA 5050 에서 로봇이 자신의 제원을 관제에 알리는 메시지다. 공식 저장소(main, 3.0.0 판)의 JSON 스키마는 headerId·timestamp·version·manufacturer·serialNumber·typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 을 필수 속성으로, 하드웨어·소프트웨어 버전과 네트워크·배터리 매개변수를 담는 mobileRobotConfiguration 을 선택 속성으로 둔다. [사실][^ref-228] typeSpecification 은 시리즈 이름, 구동 방식(DIFFERENTIAL·OMNIDIRECTIONAL·THREE_WHEEL), 로봇 종류(FORKLIFT·CONVEYOR·TUGGER·CARRIER), 최대 적재 질량, 위치추정 방식, 주행 방식(물리 라인·가상 라인·자유 주행), 지원 구역 유형을, physicalParameters 는 최소·최대 속도, 각속도, 최대 가감속, 높이·폭·길이를 기종 단위로 기술한다. [사실][^ref-228] 용어집: [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md).
- **디지털 명판(Digital Nameplate, IDTA 02006)** — [자산관리셸](../../glossary/asset-administration-shell.md)(Asset Administration Shell, AAS)의 서브모델로, 제조사명·제품명·일련번호·제조일과 하드웨어·펌웨어·소프트웨어 버전 같은 식별·버전 항목을 기계가독 명판으로 담는 것으로 보인다. [추정][^ref-876] 어느 항목이 필수이고 어느 항목이 선택인지는 이번 실행에서 확인하지 못했다(미확인).
- **AGV 기술 데이터 서브모델(Technical Data for AGV in Intralogistics, IDTA 02047-1-0)** — 실내 물류용 AGV·AMR 의 기술 데이터를 TypeAndApplicationInformation·TechnicalParameters·VDA5050Factsheet·EnergyAndCommunication·Battery·Safety·TemporaryTechnicalData 컬렉션으로 나눠 담는 자산관리셸 서브모델 템플릿이며, 혼합 플릿을 중앙 관제에 통합하고 시운전·운영·유지보수에 걸쳐 쓰는 것을 목표로 한다(2025-03). [사실][^ref-198]
- **신원 보고(identityReport)** — MassRobotics AMR 상호운용 표준에서 로봇이 접속 시 보내는 메시지로, uuid(RFC 4122)·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope 를 필수로, maxSpeed·maxRunTime·chargerType·supportVendorName·productDocumentation·cargoType·cargoMaxVolume·cargoMaxWeight 등을 선택으로 둔다. [사실][^ref-230] 용어집: [신원 보고](../../glossary/identity-report.md).
- **자산관리셸 레지스트리·디스커버리(AAS Registry / Discovery)** — 자산관리셸 API 명세(IDTA-01002)의 공식 저장소는 최신 3.2.0 판에서 AAS 저장소·서브모델 저장소·AAS 레지스트리·서브모델 레지스트리·디스커버리·개념 설명 저장소·AASX 파일 서버 등 아홉 가지 서비스 명세를 둔다. [사실][^ref-880]
- **통합 로봇 기술 형식(Unified Robot Description Format, URDF)** — 로봇의 구조·운동학을 기술하는 형식이지만 식별자 자체에는 의미가 없어, 온톨로지로 옮기려면 해석이 필요하다는 점이 지적된다. [사실][^ref-239]
- **온톨로지 채우기(ontology population)** — 이미 정해진 온톨로지의 개념에 맞춰 URDF 같은 원천에서 개체와 관계를 뽑아 채우는 작업이다. 언어 모델로 이를 자동화한 연구는 여러 번 질의한 다수결과 구문·스키마 검증으로 출력을 제약한다. [사실][^ref-239]
- **플릿 어댑터 설정(config.yaml)** — Open-RMF 에서 새 플릿을 등록하는 파일로, 플릿 이름, 선속도·각속도 한계, 발자국·근접 반경(profile), 후진 가능 여부, 배터리·기계·주변·도구 시스템 매개변수, 재충전 임계값, 작업 능력(loop·delivery·clean), 로봇별 충전기를 적는다. [사실][^ref-153] 용어집: [플릿 어댑터](../../glossary/fleet-adapter.md).

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-876]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-880]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README), 미확인, https://github.com/admin-shell-io/aas-specs-api, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s6.md

```markdown
---
title: "4. 이기종 로봇 등록 — 대표 접근법과 기술"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-198, ref-230, ref-239, ref-153, ref-874, ref-876, ref-031, ref-880, ref-881, ref-465, ref-883]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 대표 접근법과 기술

# 4. 이기종 로봇 등록 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 등록 데이터를 로봇에서 직접 받는 경로가 두 표준에 있다. VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에는 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다. [사실][^ref-031]
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 로봇에서 직접 받기: 팩트시트 요청과 신원 보고

등록 데이터를 로봇에서 직접 받는 경로가 두 표준에 있다. VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에는 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다. [사실][^ref-031] MassRobotics 표준에서는 로봇이 접속할 때 신원 보고를 보내며, 일련번호는 로봇에 물리적으로 연결될 수 있는 고유 식별자로 설명된다. [사실][^ref-230]

### 제조사가 낸 자산관리셸을 찾아 읽기

디지털 명판, AGV 기술 데이터 서브모델, 레지스트리·디스커버리 API 를 함께 보면, 제조사가 명판과 기술 데이터 서브모델을 자산관리셸로 내고 레지스트리에 등록해 ROP 가 자산 식별자로 찾아 읽는 경로를 구성할 수 있을 것으로 보이나, 로봇 관제가 이 경로로 실제 등록한 운영 사례는 확인되지 않았다. [추정][^ref-876][^ref-198][^ref-880] 디스커버리와 레지스트리를 어떤 순서로 부르는지는 원문을 열지 못해 이 페이지에서 단정하지 않는다.

### 어댑터 설정 파일과 로봇 API 구현

Open-RMF 플릿 어댑터 튜토리얼은 config.yaml 에 플릿·로봇 제원을 적는 것과 별도로, 로봇 측 RobotAPI 가 navigate·position·battery_soc·stop·start_activity·is_command_completed 를 구현해야 한다고 정한다. [사실][^ref-153] 타르투대학교병원 현장 시험도 FreeFleet 클라이언트·서버 설정과 배터리·속도·발자국을 적은 어댑터 파일로 로봇을 등록했다. [사실][^ref-874] 발행 주체가 다른 두 보고가 같은 구조를 보인다. [사실][^ref-153][^ref-874] 이 구조에서 ROP 가 줄일 수 있는 것은 설정 파일 작성이며, 로봇별 API 구현은 제조사나 통합사의 몫으로 남는다.

### 문서·URDF·자연어에서 능력 추출과 사람 검토

세 연구 그룹이 언어 모델 추출에 자동 검증이나 사용자 최종 검토를 결합한 방법을 각각 보고해, 자동 추출과 자동 검증, 사람 최종 검토를 잇는 구성이 한 곳 이상에서 확인된다. [사실][^ref-239][^ref-465][^ref-883] Dussard·Sarthou(2026)는 기존 온톨로지의 개념을 프롬프트에 넣어 언어 모델이 URDF 요소의 의미 관계를 추론하게 하고, 여러 번 질의한 다수결과 구문·스키마 검증으로 출력을 제약해 여러 로봇 기술로 평가했다. [사실][^ref-239] Vieira da Silva 외(2024)는 능력의 자연어 설명을 정해진 프롬프트에 넣어 언어 모델이 능력 온톨로지를 생성하고, 구문 검증·모순 탐지·환각과 누락 점검을 언어 모델과의 반복 루프로 자동 수행한 뒤 사람이 최종 검토·수정만 하게 했다. [사실][^ref-465] Abolhasani·Pan(2024)의 OntoKGen 은 기술 문서에서 온톨로지를 뽑되 시스템이 모범 사례 기반 온톨로지를 추천하고 사용자가 최종 결정을 갖게 하는 대화형 방식을 택했다. [사실][^ref-883] 세 연구의 정확도 같은 정량 결과는 초록에 없어 이 페이지에 적지 않는다.

이 영역이 요구하는, 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만들고 사람이 대조해 확정·반려하는 흐름은 위 연구들의 사람 최종 검토와 방향이 같다. 그러나 세 연구 어느 것도 추출 항목마다 매뉴얼의 절·줄 위치를 붙여 검토자가 대조하게 하는 근거 연결을 초록에서 밝히지 않아, 근거 연결형 검토·승인은 아직 확인되지 않은 요구로 보인다. [추정][^ref-465][^ref-883][^ref-239] 이 방법들은 L. AI·학습 기술의 연구 방법이므로 10절에서 45. 문서·도면·장면 이해와 47. AI·학습·적응과 모델 운영에 함께 연결한다.

### 표준 문서 자체의 기계가독 형식

OPC Foundation 은 OPC UA for Robotics 명세를 STS XML 외에 AI 응용용 마크다운과 RAG 청크 형식으로도 제공한다. [사실][^ref-881] 표준 문서를 언어 모델이 읽어 등록 항목을 뽑는 입력으로 쓸 수 있는지는 이번 조사에서 확인하지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-874]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-876]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29
[^ref-880]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README), 미확인, https://github.com/admin-shell-io/aas-specs-api, 접근일 2026-09-29
[^ref-881]: OPC Foundation, OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02), 2025-09-08, https://reference.opcfoundation.org/Robotics/v100/docs/, 접근일 2026-09-29
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-883]: Abolhasani, M. S., & Pan, R., Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation, 2024-12-10, https://arxiv.org/abs/2412.00608, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s8.md

```markdown
---
title: "4. 이기종 로봇 등록 — 대표 연구와 자료"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-239, ref-874, ref-875, ref-043, ref-465, ref-883]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 대표 연구와 자료

# 4. 이기종 로봇 등록 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Valner, R. 외(타르투대학교), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — 자체 관제가 없는 TIAGo 를 FreeFleet 과 어댑터 파일로 Open-RMF 에 등록하고, 프로그램 제어가 없는 병원 문을 서보 장치로 지나며 혈액 검체를 운반한 현장 시험. 등록 작업의 실제 구성을 보여 준다. [사실][^ref-874]
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Valner, R. 외(타르투대학교), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — 자체 관제가 없는 TIAGo 를 FreeFleet 과 어댑터 파일로 Open-RMF 에 등록하고, 프로그램 제어가 없는 병원 문을 서보 장치로 지나며 혈액 검체를 운반한 현장 시험. 등록 작업의 실제 구성을 보여 준다. [사실][^ref-874] 전문을 열어 확인했다.
- Dussard, B., & Sarthou, G.(LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF(2026-06-10) — URDF 를 언어 모델로 해석해 기존 온톨로지에 맞춰 채우고 다수결·스키마 검증으로 제약한 연구. [사실][^ref-239] arXiv 초록으로 확인했다.
- Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions(2024-10-18) — 자연어 능력 설명에서 능력 온톨로지를 생성하고 자동 검증 루프 뒤 사람이 최종 검토하는 방법. [사실][^ref-465] arXiv 초록으로 확인했다.
- Abolhasani, M. S., & Pan, R., Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation(2024-12-10) — 기술 문서에서 온톨로지·지식 그래프를 뽑되 사용자가 최종 결정을 갖는 OntoKGen. 대상이 로봇 문서가 아닌 신뢰성·유지보수성 문서라는 한계가 있다. [사실][^ref-883] arXiv 초록으로 확인했다.
- 신민종·한영석·정재윤, 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계(한국디지털산업학회지 29권 4호, 2024) — AMR 의 하드웨어·소프트웨어 정보를 자산관리셸로 기록해 JSON 으로 교환하고 OPC UA 로 감시하는 설계 제안. 초록은 현장 적용 결과를 적지 않는다. [사실][^ref-043] KCI 초록만 확인했다.
- 로봇신문, 클로봇 기업 소개 기사(2025-11-09) — 이기종 통합관제 솔루션과 인천공항 사업을 소개한 보조 자료. [추정] 벤더 주장[^ref-875]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-29
[^ref-874]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-875]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-29
[^ref-043]: 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)), 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-29
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-883]: Abolhasani, M. S., & Pan, R., Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation, 2024-12-10, https://arxiv.org/abs/2412.00608, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s7.md

```markdown
---
title: "4. 이기종 로봇 등록 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-198, ref-230, ref-153, ref-876, ref-878, ref-031, ref-880, ref-881]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 관련 표준·프레임워크·오픈소스

# 4. 이기종 로봇 등록 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 전체 목록은 [표준 목록](../../standards/index.md)에 있다. 용어집의 [능력 기술 서브모델](../../glossary/capability-description-submodel.md)과 [소프트웨어 명판](../../glossary/software-nameplate.md)은 같은 자산관리셸 계열이지만 이번 브리프가 다루지 않아 표에 넣지 않았다.
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)(3.0.0, 공식 저장소 main) | 표준 | 로봇이 관제 요청에 따라 게시하는 식별·제원 기록. 필수 11개 속성과 기종 제원 필드를 정한다. [사실][^ref-228][^ref-031] | ref-228, ref-031 |
| IDTA 02047-1-0 AGV 기술 데이터 서브모델(2025-03) | 표준 | 실내 물류 AGV·AMR 의 기술 데이터를 7개 컬렉션으로 담고 VDA5050Factsheet 컬렉션을 포함한다. [사실][^ref-198] | ref-198 |
| IDTA 02006-3-0 디지털 명판 | 표준 | 산업 장비의 식별·버전 항목을 담는 자산관리셸 서브모델로 보인다. 필수·선택 구분은 미확인. [추정][^ref-876] | ref-876 |
| MassRobotics AMR 상호운용 표준 JSON 스키마 | 표준 | 접속 시 신원 보고(identityReport)의 필수·선택 필드를 정한다. [사실][^ref-230] | ref-230 |
| OPC 40010-1 OPC UA for Robotics 1부(1.02, 2025-09-08) | 표준 | 수직 통합·자산 관리·상태 감시를 범위로 MotionDeviceSystem 정보 모델을 정의하고 MotionDevice 에 Manufacturer·Model·SerialNumber·ProductCode 식별 속성을 둔다. [사실][^ref-881] Controller 의 식별 속성과 SoftwareRevision 은 미확인. | ref-881 |
| 자산관리셸 API 명세 IDTA-01002(3.2.0) | 표준 | 레지스트리·디스커버리를 포함한 서비스 명세 9종으로 제조사가 낸 자산관리셸을 등록하고 찾는 인터페이스를 정한다. [사실][^ref-880] | ref-880 |
| [Open-RMF](../../glossary/open-rmf.md) 플릿 어댑터 튜토리얼 | 오픈소스 | config.yaml 항목과 RobotAPI 필수 메서드 6종으로 새 플릿 등록 절차를 정한다. [사실][^ref-153] | ref-153 |
| RoMi-H 등재 프로그램(싱가포르 창이종합병원 CHART, 2025-05-01 시행) | 평가 프로그램 | 시스템 통합사를 기술·배치 역량 평가로 등재하는 등록 승인 관문 사례. [사실][^ref-878] | ref-878 |

전체 목록은 [표준 목록](../../standards/index.md)에 있다. 용어집의 [능력 기술 서브모델](../../glossary/capability-description-submodel.md)과 [소프트웨어 명판](../../glossary/software-nameplate.md)은 같은 자산관리셸 계열이지만 이번 브리프가 다루지 않아 표에 넣지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-876]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-878]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29
[^ref-880]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README), 미확인, https://github.com/admin-shell-io/aas-specs-api, 접근일 2026-09-29
[^ref-881]: OPC Foundation, OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02), 2025-09-08, https://reference.opcfoundation.org/Robotics/v100/docs/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s11.md

```markdown
---
title: "4. 이기종 로봇 등록 — 열린 질문"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-875, ref-043]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 열린 질문

# 4. 이기종 로봇 등록 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-128** (상태: 열림 · 실행 2026-09-29-07 에서 부분 진전) 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? — 이번 조사에서 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구와 벤더의 이기종 관제 소개뿐이며, 실제 등록 데이터로 운영에 쓴 국내 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-043][^ref-875]
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-128** (상태: 열림 · 실행 2026-09-29-07 에서 부분 진전) 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? — 이번 조사에서 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구와 벤더의 이기종 관제 소개뿐이며, 실제 등록 데이터로 운영에 쓴 국내 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-043][^ref-875]
- **신규(id 는 퍼블리셔가 부여)** 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (관련: 4. 이기종 로봇 등록, 45. 문서·도면·장면 이해, 7. 온톨로지 검증·변경 관리)
- **신규(id 는 퍼블리셔가 부여)** VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? (관련: 4. 이기종 로봇 등록, 21. 상호운용 표준·적합성, 5. 로봇 능력·작업 표현)
- **신규(id 는 퍼블리셔가 부여)** 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? (관련: 4. 이기종 로봇 등록, 63. 병원·의료, 58. 다사업자 책임·계약·데이터)
- **신규(id 는 퍼블리셔가 부여)** 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? (관련: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동)

전체 목록은 [열린 질문](../../open-questions.md)에 있다. 디지털 명판의 정확한 필수·선택 항목과 OPC UA for Robotics 의 Controller 식별 속성은 미확인으로 남겨 추가 조사로 넘긴다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-875]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-29
[^ref-043]: 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)), 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s10.md

```markdown
---
title: "4. 이기종 로봇 등록 — 다른 연구영역과의 연결"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-198, ref-239, ref-153, ref-874, ref-878, ref-031]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 다른 연구영역과의 연결

# 4. 이기종 로봇 등록 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 등록 때 받은 팩트시트·서브모델·신원 보고의 제원과 문서에서 뽑은 능력 초안이 능력 표현의 입력이 된다. 팩트시트 필드 설명은 이 페이지에 두고, 표현 표준 정렬은 저 페이지가 맡는다. [추정][^ref-198][^ref-153]
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 등록 때 받은 팩트시트·서브모델·신원 보고의 제원과 문서에서 뽑은 능력 초안이 능력 표현의 입력이 된다. 팩트시트 필드 설명은 이 페이지에 두고, 표현 표준 정렬은 저 페이지가 맡는다. [추정][^ref-198][^ref-153]
- [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md) — 등록 데이터에서 어댑터 설정을 자동으로 만드는 일이 이어진다. [추정][^ref-153]
- [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) — 펌웨어·문서 개정 때 등록 내용을 무엇부터 다시 확인할지가 이어진다. [추정][^ref-198]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 팩트시트 요청·게시 경로가 곧 관제 연동 인터페이스다. [사실][^ref-031]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 팩트시트·자산관리셸·신원 보고·OPC UA 규격 사이의 대응과 적합성. [추정][^ref-198]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — URDF·자연어·기술 문서에서 온톨로지를 추출하는 언어 모델 연구는 이 영역의 방법이다(원문 교차 규칙: 매뉴얼 해석). [추정][^ref-239]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 추출에 쓰는 언어 모델의 검증·운영. [추정][^ref-239]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 매뉴얼 해석 교차 규칙의 다른 한 축이며, 등록 뒤 시운전에서 등록 내용이 현장과 맞는지 확인한다. [추정][^ref-239][^ref-198]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 팩트시트 mobileRobotConfiguration 의 하드웨어·소프트웨어 버전 추적. [추정][^ref-228]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 5절의 병원 사례 2건(타르투대학교병원 등록, RoMi-H 등재)이 현장 유형별 요구로 이어진다. [사실][^ref-874][^ref-878]
- 트랙: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 문서에서 능력을 추출하는 방법과 문서 유형 조사가 이 영역과 겹친다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-874]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-878]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-07/pages/topics/2026/2026-09-29-area04-s3.md

```markdown
---
title: "4. 이기종 로봇 등록 — 왜 중요한가"
type: topic
category: "B. 로봇 온톨로지"
primary_area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-228, ref-230, ref-153, ref-874, ref-876, ref-878, ref-031]
last_run: 2026-09-29
version: 1
split_from: docs/categories/robot-ontology/heterogeneous-robot-registration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 4. 이기종 로봇 등록 — 왜 중요한가

# 4. 이기종 로봇 등록 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 제조사마다 식별·제원 정보의 이름과 형식이 다르므로, 등록을 빠르고 믿을 수 있게 하려면 제조사가 기계가독 형식으로 내는 기록과 그것을 받는 경로가 먼저 정해져야 한다. 서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하며, 제조사명·기종(시리즈)·일련번호는 세 형식에 공통으로 들어 있는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-876]
- 이 페이지는 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

제조사마다 식별·제원 정보의 이름과 형식이 다르므로, 등록을 빠르고 믿을 수 있게 하려면 제조사가 기계가독 형식으로 내는 기록과 그것을 받는 경로가 먼저 정해져야 한다. 서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하며, 제조사명·기종(시리즈)·일련번호는 세 형식에 공통으로 들어 있는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-876] 치수(외곽)·최대 적재·최대 속도는 VDA 5050 팩트시트와 MassRobotics identityReport 두 형식에 공통으로 들어 있는 것으로 보인다. [추정][^ref-228][^ref-230]

등록은 정보를 받는 일로 끝나지 않는다. Open Robotics 의 튜토리얼과 타르투대학교 연구진의 병원 현장 시험은 플릿 관리 프레임워크에 로봇을 등록하는 일이 기종 제원·배터리 매개변수를 적은 어댑터 설정 파일과 로봇별 API 구현의 두 부분으로 이루어진다고 각각 보고했다. [사실][^ref-153][^ref-874] 제조사가 낸 기록을 플랫폼의 설정과 연동 코드로 옮기는 작업이 등록의 실체다. VDA 5050 은 이 기록을 관제가 로봇에 요청해 받는 경로까지 정해 두었다. [사실][^ref-031]

믿을 수 있는 등록에는 누가 등록할 자격이 있는가도 포함된다. 싱가포르 공공 의료기관은 Open-RMF 기반 RoMi-H 를 자동화 통합 플랫폼으로 지정하고, 시스템 통합사가 기술·배치 역량 평가를 거쳐 2년 유효 등재를 받아야 병원 제안 요청에 참여하게 한다. [사실][^ref-878] 등록 데이터의 형식뿐 아니라 등록하는 주체의 검증도 이 영역의 일이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../../categories/robot-ontology/ontology-based-system-and-robot-integration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/robot-ontology/heterogeneous-robot-registration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-874]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-876]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-878]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-07 | 4. 이기종 로봇 등록 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 868건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 227개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
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
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
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
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
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
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
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
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
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
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
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
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [4] 에 걸린 1건 / 전체 146건)

```markdown
- oq-128 [열림] 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? (영역 10, 4, 21)
```
