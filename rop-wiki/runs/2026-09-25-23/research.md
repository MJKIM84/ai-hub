# 리서치 브리프 2026-09-25-23

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-23 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 온톨로지 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 1 · 답한 질문 q1-03, q1-06, q1-07

## 갭(비어 있거나 약한 섹션)

- 단계 1 질문 q1-03(조사 중, 2026-09-25-02·16 부분 답), q1-06, q1-07 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 6건 중 오래된 순)
- 완료 조건: 모델·표준 비교표의 IEEE 1872 CORA·IEEE 1872.2·KnowRob·SOMA·SSN/SOSA 행의 다섯 정보 항목 열 미조사
- 완료 조건: ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 미반영(q1-06 미조사)
- 단계 1 페이지 3절 q1-02 소제목의 VDA 5050 팩트시트 블록 서술이 2.0.0 기준 [추정](판 미확인)으로 남아 있고, 2.x 대비 3.0.0 필드 변화 미확인(q1-07)
- 5. 로봇 능력·작업 온톨로지 페이지 섹션 11. 열린 질문의 적재물 유형 공통 어휘(oq-023)와 선언 능력·운용 능력 배정 기준(oq-024) 미해결

## 조사 질문

1. 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]
2. q1-03 이 모델들은 ROP가 배정·실행·검증에 필요로 하는 정보 — 전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미 — 를 얼마나 담는가? 빠진 것은 무엇인가? (이번 실행은 남은 학술 온톨로지 행 IEEE 1872 CORA·IEEE 1872.2·KnowRob·SOMA·SSN/SOSA 를 공식·공개 저장소 원문으로 대조)
3. q1-06 부록 A 5번 정의의 요소(제조사별 기능·제약·장착 장비·실행 조건, 작업 요구)를 기준으로 ROP용 능력 개념에 무엇을 더 추가해야 하는가?
4. q1-07 VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가?
5. 요구 능력과 제공 능력을 속성 단위로 비교(능력 매칭)하는 기존 연구는 ROP용 능력 개념 요구 목록에 무엇을 더하는가? (단계 1 완료 조건 둘째 항목, 온톨로지 초안 2절 겨냥)
6. 국내 자료에 로봇 능력 온톨로지나 능력 기반 작업 할당을 다룬 연구가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소 2.1.0 태그의 팩트시트 JSON 스키마(제목 'AGV Factsheet')는 version·manufacturer·serialNumber 와 typeSpecification·physicalParameters·protocolLimits·protocolFeatures·agvGeometry·loadSpecification 블록을 필수로 두고, 버전·네트워크 정보를 담는 vehicleConfig 블록을 둔다. | ref-348 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 공식 저장소 main(3.0.0 판)의 팩트시트 JSON 스키마는 headerId·timestamp·version·manufacturer·serialNumber 와 typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 블록을 필수로, mobileRobotConfiguration 블록을 선택으로 둔다. | ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | 2.1.0 태그와 main(3.0.0) 팩트시트 스키마를 대조하면 agvGeometry→mobileRobotGeometry, vehicleConfig→mobileRobotConfiguration, agvActions→mobileRobotActions, resultDescription→actionResult, agvKinematic·agvClass·maxLoadMass→mobileRobotKinematics·mobileRobotClass·maximumLoadMass, speedMin·speedMax·accelerationMax·decelerationMax·heightMin·heightMax→minimumSpeed·maximumSpeed·maximumAcceleration·maximumDeceleration·minimumHeight·maximumHeight 로 이름이 바뀌었다. | ref-348, ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | main(3.0.0) 팩트시트 스키마는 2.1.0 태그 스키마에 없던 action 적용 범위 ZONE, action 필수 필드 pauseAllowed·cancelAllowed, 유형 명세의 supportedZones, 구성 블록의 batteryCharging(임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간)을 더했고, 지원·필수 선택 파라미터 목록(optionalParameters: parameter·support SUPPORTED/REQUIRED·description)은 두 판 모두 둔다. | ref-348, ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | 적재 제약은 두 판 모두 적재 명세(loadSpecification)의 적재 세트(loadSets)에 기술되며, 2.1.0 태그는 maxWeight, min/maxLoadhandlingHeight·Depth·Tilt, agvSpeedLimit·agvAccelerationLimit·agvDecelerationLimit, pickTime·dropTime 을, main(3.0.0)은 maximumWeight, minimum/maximumLoadhandlingHeight·Depth·Tilt, maximumSpeed·maximumAcceleration·maximumDeceleration, pickTime·dropTime 을 두고, 로봇 전체 최대 적재 질량은 유형 명세(maxLoadMass→maximumLoadMass)에 둔다. | ref-348, ref-228 | 아니오 | medium | 2026-09-25 | 적치 / 제약 | — |
| f6 | [추정] | 2.x 와 3.0.0 팩트시트의 적재 제약은 적재 세트 단위(치수·최대 중량·취급 높이·깊이·기울기·적재 시 속도 한계·적재·하역 시간)라는 구조가 같고 필드 이름만 바뀐 것으로 보여, ROP 가 두 판을 함께 받으려면 필드 이름 대응표로 판 무관 속성에 정규화할 수 있을 것으로 보인다. | ref-348, ref-228 | 아니오 | low | 2026-09-25 | — | — |
| f7 | [추정] | VDA 5050 공식 저장소 2.0.0 태그의 명세 마크다운(머리말 'RELEASE CANDIDATE' 표기)은 팩트시트 블록으로 localizationParameters 를 적지만, 2.1.0 태그와 main 스키마에서는 이 블록이 확인되지 않아 2.0.0 게시판의 블록 구성은 확정할 수 없는 것으로 보인다. | ref-354, ref-348, ref-228 | 아니오 | low | 2026-09-25 | — | — |
| f8 | [사실] | W3C SSN 의 System Capabilities 모듈(ssn-system.ttl)은 조건 아래 시스템 성질을 기술하는 SystemCapability·OperatingRange·SurvivalRange·Condition 클래스와, 하위 성질 MeasurementRange·ActuationRange·Accuracy·Latency·ResponseTime 등, 운용 성질 MaintenanceSchedule·OperatingPowerRange, 생존 성질 SystemLifetime·BatteryLifetime 을 두고 hasSystemCapability·hasOperatingRange·inCondition 속성으로 잇는다. | ref-235 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [추정] | SSN System Capabilities 모듈은 다섯 정보 항목 가운데 파라미터 범위(ActuationRange·조건 아래 성능)와 환경 제약(Condition·OperatingRange·SurvivalRange)을 담지만, 이번 열람 범위에서 전제조건·완료 확인 방법·오류 의미·적재 제약을 기술하는 클래스는 확인되지 않았다. | ref-235 | 아니오 | low | 2026-09-25 | — | — |
| f10 | [사실] | SOMA 공식 저장소의 SOMA-ACT 온톨로지는 작업 실행 상태 영역(ExecutionStateRegion)에 Active·Cancelled·Failed·Paused·Pending·Succeeded 여섯 상태를 두고, 전제 상황(hasRequiredInitialSituation)과 기대 종료 상황(hasExpectedTerminalSituation) 관계, 충족되지 않은 사후조건 같은 기대 불일치를 나타내는 NonmanifestedSituation 클래스를 둔다. | ref-349 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f11 | [추정] | SOMA 는 다섯 정보 항목 가운데 전제조건(요구 초기 상황), 완료 확인(기대 종료 상황과 Succeeded 상태), 오류 의미(Failed 상태와 기대 불일치 상황)를 담지만, 이번에 연 SOMA-ACT 파일에서 파라미터 허용 범위와 적재 제약은 확인되지 않았다. | ref-349 | 아니오 | low | 2026-09-25 | — | — |
| f12 | [사실] | 헬무트 슈미트 대학이 공개한 IEEE 1872.2 AuR 온톨로지 OWL 구현은 기능(Function)·기능 실행(FunctionExecution), 행동 분류(ArchitecturalBehavior·ManifestedBehavior·EmergentBehavior 등), 물리·정보 상호작용, 객체 중심 환경 기술 클래스를 두고 기능을 행동에 잇는 isPlayedBy 속성을 둔다. | ref-350 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [추정] | 이 IEEE 1872.2 OWL 구현에서는 능력·전제조건·사후조건·파라미터 범위·실패·작업 완료 상태를 명시하는 클래스·속성이 확인되지 않아, 다섯 정보 항목을 구조로 담지 않는 것으로 보인다. | ref-350 | 아니오 | low | 2026-09-25 | — | — |
| f14 | [사실] | IEEE 1872-2015 CORA 의 공개 OWL 번역(cora-bare.owl)은 Robot·RobotGroup·RobotInterface·RoboticEnvironment·RoboticSystem·SingleRoboticSystem·CollectiveRoboticSystem 클래스와 equippedWith·robotPart 및 자율성 수준(자율·반자율·원격 조종·원격 조작) 속성을 둔다. | ref-355 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f15 | [추정] | CORA 는 로봇·로봇 시스템의 분류와 부품·장착 관계를 표현할 뿐 다섯 정보 항목(전제조건·파라미터 범위·적재·환경 제약·완료 확인·오류 의미)과 능력·작업 개념은 담지 않는 것으로 보인다. | ref-355 | 아니오 | low | 2026-09-25 | — | — |
| f16 | [사실] | KnowRob 공식 저장소 README 는 KnowRob 을 RDF·RDFS·OWL 어휘의 맥락화된 트리플로 지식을 표현하고 여러 추론기의 결과를 결합하는 하이브리드 지식 베이스로 설명하며, 저장 백엔드로 Prolog 기반 저장소·MongoDB·Redland 를 들고, 로봇 제어 구조에 묻힌 암묵 지식을 온톨로지 기반 데이터 접근으로 명시화한다고 적는다. | ref-351 | 아니오 | medium | 2026-09-25 | — | — |
| f17 | [추정] | KnowRob README 는 전제조건·파라미터 범위·실패 같은 항목을 직접 다루지 않아, KnowRob 행의 다섯 정보 항목은 README 만으로 판정할 수 없고 KnowRob 이 쓰는 도메인 온톨로지(SOMA 등) 쪽 판정에 기대야 할 것으로 보인다. | ref-351, ref-349 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | 원문을 연 학술 온톨로지 기준으로 전제조건·완료 확인·오류 의미는 SOMA 가, 파라미터 범위·환경 제약은 SSN System Capabilities 가 일부 담고, CORA·IEEE 1872.2 구현은 다섯 항목을 담지 않으며, 적재 제약은 어떤 학술 온톨로지에서도 확인되지 않고 VDA 5050 적재 세트 같은 산업 규격에만 있어, ROP 는 적재 제약과 오류의 조치 의미(등급·재시도)를 산업 규격 쪽에서 가져와야 할 것으로 보인다. | ref-349, ref-235, ref-355, ref-350, ref-228 | 아니오 | low | 2026-09-25 | 제약 | — |
| f19 | [사실] | IDTA 02020 능력 기술 1.0 README 는 이 서브모델이 공정·제품 쪽 요구 능력과 자원 쪽 제공 능력을 비교해 생산 계획·오케스트레이션을 돕는다고 설명한다. | ref-229 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | Järvenpää 외(IJCIM 36(1), 2023)는 제품과 자원의 온톨로지 기술과 SPIN 규칙으로 결합 자원의 결합 능력 파라미터를 추론하고 제품 특성을 자원(조합)의 능력 파라미터와 비교해 가능한 자원 조합을 찾는 능력 매칭 소프트웨어를 제시했다. | ref-352 | 아니오 | medium | 2023 | 수행 자원 | 원문 미열람 |
| f21 | [사실] | Köcher·Vieira da Silva·Fay(arXiv 2312.08801, AAAI 2024 CAIPI 워크숍)는 의미 능력 모델과 SMT 로 제품 생산이나 자율 로봇 임무 수행에 필요한 개별 능력의 순서를 자동으로 찾는 공정 계획 방법을 제안했다. | ref-353 | 아니오 | medium | 2023-12 | — | 원문 미열람 |
| f22 | [사실] | VDA 5050 main(3.0.0) 팩트시트는 적재 취급 장치 식별자 목록(loadPositions), 위치추정·주행 방식(localizationTypes·navigationTypes), 지원 구역 유형(supportedZones), 하드웨어·소프트웨어 버전 키-값(mobileRobotConfiguration.versions), 충전 설정(batteryCharging)을 기술하게 해, 장착 장비·운용 구역·버전·충전 조건을 로봇 선언의 일부로 둔다. | ref-228 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f23 | [사실] | IDTA 02047 무인운반차 기술 데이터 1.0 템플릿은 부착 장비 인터페이스(InterfacesForAttachments)와 속도·가동 시간의 명세값(AsSpecified)·운용값(AsOperated) 쌍을 속성으로 둔다. | ref-245 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f24 | [추정] | 분류 원문 5. 로봇 능력·작업 온톨로지 정의 요소를 기준으로 온톨로지 초안 v0.2 에 더할 ROP용 능력 개념 요구 후보는 (1) 기능의 요구·제공 구분과 속성 단위 비교, (2) 기능 속성의 값·범위, (3) 전제·사후조건, (4) 실행 상태, (5) 로봇의 하드웨어·소프트웨어 구성 버전, (6) 장착 장비의 부착 인터페이스·적재 취급 장치 위치, (7) 운용 구역·환경 조건, (8) 충전 조건, (9) 결합 자원의 결합 능력인 것으로 보인다. | ref-229, ref-352, ref-349, ref-235, ref-228, ref-245, ref-355 | 아니오 | low | 2026-09-25 | — | — |
| f25 | [추정] | 분류 원문의 질문(같은 운반 로봇 중 누가 이 화물을 실제로 취급할 수 있는가)에 답하려면 작업 요구를 화물 치수·중량 같은 요구 능력 속성으로 표현하고 로봇의 적재 세트 같은 제공 능력 속성과 비교하는 규칙이 필요할 것으로 보이며, 제조 분야의 능력 매칭 연구가 이 비교를 의미 규칙으로 구현한 선례가 된다. | ref-229, ref-352, ref-228, ref-236 | 아니오 | low | 2026-09-25 | 적치 / 수행 자원 | — |

### 근거 발췌

- **f1**: 2.1.0 태그 factsheet.schema(github_raw 열람): 필수 블록 목록과 vehicleConfig(versions 키-값, network). 스키마 예시 판 표기 2.0.0. (발행일 미확인, 확인일 기준)
- **f2**: main factsheet.schema(github_raw 열람): 최상위 required 11개와 선택 mobileRobotConfiguration(versions, network, batteryCharging). (발행일 미확인, 확인일 기준)
- **f3**: 두 스키마 필드 목록을 열람 도구로 대조한 결과. 두 파일 모두 VDA5050 공식 저장소라 독립 교차 아님. 클래스 열거값(FORKLIFT·CONVEYOR·TUGGER·CARRIER)은 두 판이 같다. (발행일 미확인, 확인일 기준)
- **f4**: 2.1.0 태그: actionScopes INSTANT·NODE·EDGE, pauseAllowed·cancelAllowed·supportedZones·배터리 충전 필드 없음. main: actionScopes에 ZONE, supportedZones 열거(BLOCKED, LINE_GUIDED, RELEASE 등 10종), batteryCharging 4필드. (발행일 미확인, 확인일 기준)
- **f5**: 두 스키마의 loadSets 하위 필드(setName·loadType·loadPositions·boundingBoxReference·loadDimensions 는 공통, main 은 setName·loadType 만 필수). (발행일 미확인, 확인일 기준)
- **f6**: f3·f5 의 대조에서 도출. 2.1.0 태그가 2.0.0 게시판과 필드 단위로 같은지는 확인하지 않음(2.0.0 태그에는 json_schemas/factsheet.schema 경로가 404).
- **f7**: 2.0.0 태그 VDA5050_EN_V1.md(github_raw 열람): 팩트시트 7개 객체 중 7번째로 localizationParameters 기술. main 스키마 열람 응답: 해당 블록 없음. 열람 도구 요약 기준.
- **f8**: SystemCapability 주석: "Describes normal measurement, actuation, sampling properties such as accuracy, range, precision, etc. of a System under some specified Conditions." (W3C sdw 저장소 편집본, /TR 판과 문구 차이 가능) (발행일 미확인, 확인일 기준)
- **f9**: f8 클래스 목록에서 도출. SOSA 핵심 모듈(Actuation·Procedure)은 이번에 열지 않아 부재 확정 아님.
- **f10**: ExecutionStateRegion 주석: 'A region containing labels that describe different states in the evolution/completion of a task execution.' PhysicalTask·GetTaskParameter 등 작업 클래스도 정의. (발행일 미확인, 확인일 기준)
- **f11**: f10 에서 도출. SOMA 의 다른 모듈(SOMA-OBJ 등)은 열지 않아 부재 확정 아님.
- **f12**: AuR_IEEE1872-2.ttl(github_raw 열람) 클래스 목록. 제3자 OWL 구현이며 IEEE 표준 문서 본문이 아님. (발행일 미확인, 확인일 기준)
- **f13**: 열람 도구 응답 기준의 부재 관찰(파일 전체를 글자 단위로 대조하지 않음). 표준 원문(유료)과 구현의 차이는 미확인.
- **f14**: cora-bare.owl(github_raw 열람)은 스스로를 CORA 개념·관계만 분리한 'bare implementation'이라 설명. 저장소 README 기준 IEEE 1872 명세를 수작업으로 OWL 번역(제3자). (발행일 미확인, 확인일 기준)
- **f15**: f14 의 클래스·속성 목록에서 도출. POS·CORAX·RPARTS 파일은 열지 않음.
- **f16**: README(dev 브랜치, github_raw 열람): 'ensemble of reasoners approach where inferences of different reasoners are combined'. 현재 C++ 구현, Prolog 선택 지원. (발행일 미확인, 확인일 기준)
- **f17**: README 에 SOMA·DUL 명칭은 이번 열람 응답에 없었음. KnowRob–SOMA 관계는 이전 실행의 논문 요약(ref-027·ref-028) 수준.
- **f18**: f8~f15 와 f5 를 다섯 항목에 대응시킨 이 위키의 종합. 산업 규격 행 판정은 2026-09-25-16 실행 결과(재인용: 2026-09-25-16).
- **f19**: README(github_raw 열람): "This enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes." (발행일 미확인, 확인일 기준)
- **f20**: 검색 요약: 규칙은 1) 결합 자원의 결합 능력 파라미터 추론·단언, 2) 제품 특성과 자원 능력 파라미터 비교. 제조 시스템 설계·재구성 대상. 원문 미열람.
- **f21**: 검색 요약: 'finding a sequence of individual capabilities required to manufacture a certain product or to accomplish a mission using autonomous robots'. v2 2024-02. 원문 미열람.
- **f22**: main factsheet.schema 열람: loadPositions 는 유효한 적재 취급 장치 식별자 배열, localizationTypes 열거 NATURAL·REFLECTOR·RFID·DMC·SPOT·GRID. (발행일 미확인, 확인일 기준)
- **f23**: 템플릿 속성 InterfacesForAttachments, SpeedMaxWithMaxLoadAsSpecified/AsOperated, MaxRunTimeAsSpecified/AsOperated. 이번 실행 재열람 안 함 (재인용: 2026-09-25-16)
- **f24**: f19~f23 과 f8·f10·f14 를 원문 정의 요소(기능·제약·장착 장비·실행 조건·작업 요구)에 대응시킨 이 위키의 요구 목록 초안. 이 목록을 제시한 단일 출처는 없음.
- **f25**: f5·f19·f20 과 적재 상태별 도달 가능성 판정 연구(ref-236, 재인용: 2026-09-25-16)에서 도출. 물류 이동로봇 대상의 능력 매칭 규칙은 찾지 못함.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-348 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.1.0) — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema | 아니오 |
| ref-354 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.0.0) — VDA5050_EN_V1.md | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md | 아니오 |
| ref-235 | W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub) | ssn/integrated/ssn-system.ttl (SSN System Capabilities module) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl | 아니오 |
| ref-349 | EASE CRC (ease-crc/soma) | SOMA — owl/SOMA-ACT.owl | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl | 아니오 |
| ref-350 | Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub) | IndustrialStandard-ODP-IEEE1872-2 — AuR_IEEE1872-2.ttl | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2/blob/main/AuR_IEEE1872-2.ttl | 아니오 |
| ref-355 | srfiorini (IEEE1872-owl GitHub) | IEEE1872-owl — cora-bare.owl (OWL specification of CORA) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl | 아니오 |
| ref-351 | KnowRob (knowrob GitHub) | knowrob — README (dev branch) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/knowrob/knowrob | 아니오 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-245 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-352 | Järvenpää, E., Siltala, N., Hylli, O., Nylund, H., & Lanz, M. | Semantic rules for capability matchmaking in the context of manufacturing system design and reconfiguration | 2023 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/0951192X.2022.2081361 | 예 |
| ref-353 | Köcher, A., Vieira da Silva, L. M., & Fay, A. | Automated Process Planning Based on a Semantic Capability Model and SMT | 2023-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2312.08801 | 예 |

### 출처 요약

- **ref-228**: VDA 5050 팩트시트 JSON 스키마(main, 3.0.0 판). 이번 실행은 최상위 블록, 적재 세트 필드, action 정의, 선택 파라미터, 구성 블록(versions·batteryCharging), supportedZones 를 확인했다.
- **ref-348**: VDA 5050 공식 저장소 2.1.0 태그의 팩트시트 JSON 스키마('AGV Factsheet'). agvGeometry·agvActions·vehicleConfig 등 2.x 필드 이름과 적재 세트 필드를 정의한다.
- **ref-354**: 공식 저장소 2.0.0 태그의 명세 마크다운. 머리말에 RELEASE CANDIDATE 표기가 있어 VDA 게시 PDF 와 같다고 확인하지 못했다. 팩트시트 블록 구성 설명을 확인했다.
- **ref-235**: SSN 시스템 능력 모듈의 온톨로지 파일(작업반 편집본). SystemCapability·OperatingRange·SurvivalRange·Condition 과 하위 성질 클래스를 정의한다.
- **ref-349**: SOMA 공식 저장소의 활동 모듈 OWL 파일. 작업·행동 클래스, 실행 상태 영역 6상태, 요구 초기 상황·기대 종료 상황 관계, 기대 불일치 상황 클래스를 정의한다.
- **ref-350**: IEEE 1872.2 AuR 온톨로지의 제3자 OWL 구현 파일. 기능·기능 실행·행동·상호작용·환경 기술 클래스를 둔다. IEEE 표준 본문이 아니다.
- **ref-355**: IEEE 1872-2015 CORA 의 개념·관계만 분리한 수작업 OWL 번역(제3자). 로봇·로봇 시스템 분류와 equippedWith·robotPart·자율성 수준 속성을 둔다. IEEE 표준 본문이 아니다.
- **ref-351**: KnowRob 공식 저장소 README. RDF·OWL 기반 하이브리드 지식 베이스, 추론기 앙상블, 저장 백엔드, 온톨로지 기반 데이터 접근을 설명한다.
- **ref-229**: IDTA 능력 기술 서브모델 1.0 README. 요구 능력과 제공 능력의 비교, 속성, 속성 제약·전이 제약, 스킬에 의한 구현을 설명한다.
- **ref-245**: 원문 미열람. 이번 실행에서는 다시 열지 않았다(2026-09-25-16 실행에서 원문 확인). 무인운반차 기술 데이터 서브모델 템플릿으로 적재 질량·명세값·운용값·부착 인터페이스 속성을 정의한다.
- **ref-236**: 원문 미열람. 로봇·작업·장소의 의미 모델과 혼합 추론으로 이종 로봇의 수행 가능성과 적재 상태별 장소 도달 가능성을 판정하는 방법을 제안한 논문.
- **ref-352**: 원문 미열람. 제품·자원 온톨로지와 SPIN 규칙으로 결합 능력 파라미터를 추론하고 제품 요구와 자원 능력을 비교하는 능력 매칭 방법(IJCIM 36(1) 128-154).
- **ref-353**: 원문 미열람. 의미 능력 모델과 SMT 로 제품 생산·자율 로봇 임무에 필요한 능력 순서를 찾는 공정 계획 프리프린트(AAAI 2024 CAIPI 워크숍).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q1-03 답: f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 medium) / q1-06 답: f19·f20·f21·f22·f23·f24·f25 (신뢰도 low) / q1-07 답: f1·f2·f3·f4·f5·f6·f7 (신뢰도 medium) — 2절 q1-03·q1-06·q1-07 상태 답함, 3절 q1-03 소제목을 '(부분 답)'에서 학술 온톨로지 행 원문 대조(f8~f18)를 더한 답으로 갱신하고 {#q1-03} 앵커 부여, q1-06·q1-07 소제목 신설(q1-07 은 2.1.0 태그 대 main 필드 대조 f3~f5, q1-02 절의 2.0.0 기준 [추정] 팩트시트 블록 문장은 f1·f3 근거로 판 표기를 붙여 정리), 4절 결론·불확실성(2.0.0 게시판 블록 구성 f7, KnowRob 판정 한계 f17), 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | 4, 5, 8 | 트랙 산출물 갱신: IEEE 1872 CORA 행(f14·f15, 제3자 OWL 번역 원문), IEEE 1872.2 행(f12·f13, 제3자 OWL 구현), KnowRob·SOMA 행(f10·f11·f16·f17), W3C SSN/SOSA 행(f8·f9)의 다섯 정보 항목 열 채움. VDA 5050 행 종류 칸에 2.x→3.0.0 필드 이름 변화와 추가 필드(f3·f4·f5) 반영. 5절 빠진 정보 요약을 f18 로 갱신(적재 제약은 산업 규격에만 있음) |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | 2, 3, 4, 6 | 트랙 산출물 갱신: track.ontology_changes 가 검증 승인되면 ROP용 능력 개념 요구 목록 초안(f24)을 반영 — 기능 한정자(요구·제공, f19·f20), 개념 실행 상태(f10), 로봇 구성 버전(f22), 장착 장비 부착 인터페이스·적재 취급 장치 위치(f14·f22·f23), 제약 종류 값(운용 구역·환경 조건·충전 조건, f8·f22). 제약 값 추가는 6절 '실행 조건과 제약의 경계' 질문과 충돌할 수 있어 미승인 시 6절 질문으로 |
| update | docs/ideas/robot-capability-ontology.md | 3, 4 | 아이디어 페이지 3절: 능력 매칭 선행 연구(f20·f21)와 요구·제공 능력 비교(f19), 분류 원문 질문 연결(f25) / 아이디어 페이지 4절: 범위 능력 '충전'에 팩트시트 batteryCharging(f4·f22), '적재'에 적재 세트 판별 필드 이름(f5), 장착 장비 표현(f14·f22·f23) |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 4, 7, 8 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f14, f18, f19, f20, f24, f25): 섹션 4 요구 능력·제공 능력, 섹션 7 CORA·SSN·SOMA 가 다섯 정보 항목을 담는 정도, 섹션 8 능력 매칭 연구(Järvenpää 외, Köcher 외). 분류 원문 SCM 질문과 요구–제공 능력 비교 규칙 연결 |
| update | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f3, f4, f5, f6): VDA 5050 2.x 와 3.0.0 팩트시트의 필드 이름 변화와 추가 필드(ZONE 범위, pauseAllowed·cancelAllowed, supportedZones, batteryCharging) — 어댑터가 두 판을 함께 받을 때의 정규화 필요 |
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f4, f22): VDA 5050 3.0.0 팩트시트의 충전 설정(임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간)이 충전 시점 계획의 입력이 될 수 있음 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 능력 매칭 | Capability Matchmaking | 제품·작업이 요구하는 특성을 자원(로봇·설비)이 제공하는 능력의 파라미터와 비교해 수행 가능한 자원이나 자원 조합을 찾는 일이다. |
| 요구 능력·제공 능력 | Required Capability / Provided (Offered) Capability | 공정·작업 쪽이 필요로 하는 능력과 자원 쪽이 내놓는 능력을 구분한 표현으로, 둘을 비교해 작업을 맡을 자원을 정한다. |
| 능력 기반 작업 배정 | Capability-based Task Allocation | 로봇이 선언하거나 관측된 능력·제약과 작업의 요구 조건을 대조해 수행 가능한 로봇에게 작업을 배정하는 방식이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 13 · 교차 확인: 0
- 예산 사용량: 검색 6회 · 신규 출처 8건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·모델마다 발행 주체 한 곳의 자료이거나 같은 저장소의 서로 다른 판
    - f6: 2.1.0 태그가 2.0.0 게시판(PDF)과 필드 단위로 같은지 미확인(2.0.0 태그의 json_schemas/factsheet.schema 경로는 404)
    - f7: 2.0.0 태그 명세의 localizationParameters 블록이 2.0.0 게시판에 있는지 미확인(RC 표기 문서)
    - f9·f11·f13·f15: 열람 도구 응답 기준의 부재 관찰이며 부재 확정 아님
    - f12·f14: IEEE 1872.2·1872-2015 는 제3자 OWL 구현·번역만 열었고 IEEE 표준 원문(유료)은 미열람
    - f17: KnowRob 자체의 다섯 정보 항목은 README 범위에서 판정 불가
    - f20·f21: 논문 원문 미열람(검색 요약 범위)
    - f24: 요구 목록 초안은 이 위키의 종합이며 단일 출처 없음
    - ref-348·ref-349·ref-350·ref-351·ref-354·ref-355 발행일 미확인
- 범위 경계 위반 의심:
    - f14: CORA 의 자율성 수준·부품 관계는 로봇 분류 설명이며 로봇 제어를 ROP 직접 범위로 서술하지 않음
    - f20·f21: 제조 공정 계획 연구이므로 물류 현장 적용 사례처럼 서술하지 않도록 방법 선례로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 열었다: 신규 ref-348(VDA 5050 2.1.0 태그 팩트시트 스키마)·ref-354(2.0.0 태그 명세 마크다운)·ref-349(SOMA-ACT.owl)·ref-350(IEEE 1872.2 제3자 OWL)·ref-351(KnowRob README)·ref-355(CORA 제3자 OWL 번역), 재사용 ref-228(main 팩트시트 스키마)·ref-235(SSN 시스템 능력 모듈)·ref-229(IDTA 02020 README). 논문 2건(ref-352·ref-353)과 재사용 ref-245·ref-236 은 원문 미열람(신뢰도 상한 medium). finding 신뢰도는 모두 medium 이하. 검색 6회/40, 신규 출처 8건/20(ref-348~ref-355, 예약 구간 안), 재사용 5건. 교차 확인 0건. 질문 선택: target.json 지정 q1-03·q1-06·q1-07 세 건 모두 답했다. q1-03 은 앞 실행들의 산업 규격 대조에 이번 학술 온톨로지 행 대조를 더해 답으로 올리되, KnowRob 은 README 만 열어 SOMA 판정에 기댄다는 한계가 있어 신뢰도 medium 으로 본다. q1-06 은 여러 출처를 대응시킨 추정 목록(f24)이라 신뢰도 low. q1-07 의 2.x 기준은 2.0.0 태그 스키마 경로가 404 라 2.1.0 태그 스키마로 대신했다. 한국 자료: 로봇 능력 온톨로지·능력 기반 할당 한국어 검색 결과는 해외 논문 번역 페이지뿐이라 넣지 않았다. 참고: 2026-09-25-16 의 f8(MassRobotics 식별 보고 필드)은 q1-08 의 답 근거가 되므로 다음 실행에서 q1-08 을 처리하면 된다. 백로그 정리 필요: q1-10·q4-11·q5-08 은 q1-09·q4-09·q5-07 과 같은 질문이 중복 등록된 것으로 보인다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 새 일반 열린 질문 없음. 후속 질문 2건, 온톨로지 변경 제안 5건.

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 1
- 답한 질문 id: q1-03, q1-06, q1-07

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | VDA 5050 2.x 와 3.0.0 팩트시트를 함께 받는 현장에서 판마다 다른 필드 이름(maxWeight→maximumWeight 등)을 능력 온톨로지의 판 무관 속성으로 정규화하고, 판이 바뀔 때 능력 정의를 어떻게 재검증하는가? (q1-07 에서 파생) | 6 | f6 |
| — | 작업 요구를 화물 치수·중량 같은 요구 능력 속성으로 표현하고 로봇 적재 세트(제공 능력)와 비교하는 규칙을 어떤 질의·규칙 형식(SPARQL·SHACL·SPIN 등)으로 표현할 수 있는가, 결합 자원(로봇+장착 장비)의 결합 능력은 어떻게 추론하는가? (q1-06 에서 파생) | 4 | f25 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 기능 (Capability) | f19, f20 | 속성 '한정자(요구 능력 / 제공 능력)'를 더한다(IDTA 02020 의 요구·제공 비교, 능력 매칭 연구의 제품 요구 대 자원 능력 비교). 작업 요구는 요구 능력 속성 값으로 표현되어 제공 능력 속성과 비교된다는 메모를 둔다. 기존 관계 '작업 요구 / 기능과 대응된다 / 기능'과 충돌하지 않고 그 판정 방식을 구체화한다. |
| add | concept | 실행 상태 (Execution State) | f10 | 기능·스킬 실행의 진행 단계(대기·진행·일시정지·취소·실패·성공 등). SOMA 실행 상태 영역 6상태에 대응하며 완료 확인 방법의 판정 대상이다. 스킬 인터페이스·오류와의 관계는 근거가 더 필요해 이번에는 개념만 제안한다. |
| modify | concept | 로봇 (Robot) | f22 | v0 의 '펌웨어 버전(단계 6에서 확정)' 속성을 '구성 버전(하드웨어·소프트웨어 버전 키-값)'으로 구체화한다(VDA 5050 3.0.0 mobileRobotConfiguration.versions). |
| modify | concept | 장착 장비 (Mounted Equipment) | f14, f22, f23 | 속성 '부착 인터페이스'(IDTA 02047 InterfacesForAttachments)와 '적재 취급 장치 위치'(VDA 5050 loadPositions)를 더한다. 관계 '로봇 / 장착 장비를 갖춘다'는 CORA equippedWith 속성과 대응한다는 근거 메모를 붙인다. |
| modify | concept | 제약 (Constraint) | f8, f22 | 속성 '종류'의 값 후보에 '운용 구역(VDA 5050 supportedZones)', '환경 조건(SSN Condition·OperatingRange)', '충전 조건(VDA 5050 batteryCharging)'을 더한다. 충전 수준은 실행 시점에 확인하는 실행 조건일 수도 있어 초안 6절 '실행 조건과 제약의 경계' 질문과 충돌할 수 있다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 모델·표준 비교표: 모든 후보 행을 채울 근거는 모였으나 스토리텔러 반영과 검증 판정 전이며, KnowRob 행은 README 범위의 판정 한계가 남음
    - ROP용 능력 개념 요구 목록 초안(f24)이 온톨로지 초안에 반영되려면 검증 승인이 필요함
    - 열린 질문 q1-08, q1-09, q1-10(q1-09 중복 등록)
