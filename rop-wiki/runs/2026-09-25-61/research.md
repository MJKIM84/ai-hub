# 리서치 브리프 2026-09-25-61

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-61 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 24. 자산·소프트웨어 수명주기 관리 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(예지보전·상태 기반 정비, 배터리 건강 상태, 소프트웨어 명판, 패치 관리, 지도 버전)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(상태 감시·고장 예측, 배터리 열화 인지 배정, OTA 배포·롤백, 관리형 노드)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건, 정정 요청 0건)

## 조사 질문

1. 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
2. 로봇 상호운용 규격(VDA 5050, MassRobotics AMR 상호운용 표준)은 펌웨어·소프트웨어·지도 버전과 배터리 건강 상태를 어떤 필드로 보고하며, 버전 호환성 규칙은 무엇인가? (섹션 4·6·7 겨냥)
3. 고장 예측·정비(상태 감시, 예지보전)와 자산 관리의 표준·대표 연구는 무엇인가(ISO 17359, ISO 55000, 산업용 로봇 상태 감시 검토 논문)? (섹션 3·7·8 겨냥)
4. 배터리 열화를 플릿 운영(작업 배정·충전)에 반영하는 접근은 무엇인가? (섹션 5·6 겨냥)
5. 로봇 소프트웨어 배포·복구(무선 업데이트, 롤백, 관리형 노드, 배포판 지원 종료)와 패치 관리 표준은 무엇인가? (섹션 6·7 겨냥)
6. 펌웨어·설정 변경이 안전 재평가·규제상 '실질적 변경'에 해당하는 조건은 무엇이며 한국 인증 제도는 어떻게 다루는가? (섹션 3·9·11 겨냥, 한국 자료 우선)
7. ROP 가 직접 맡을 수명주기 관리 범위와 제조사·설비에 맡길 범위는 어떻게 나뉘는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 지도를 지도 식별자(mapId)와 지도 버전(mapVersion)의 조합으로 식별하고, 즉시 동작 downloadMap·enableMap·deleteMap 으로 지도 내려받기·활성화·삭제를 지시하며, 같은 mapId 에서는 한 번에 한 버전만 활성화되게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 은 의미적 버전 체계를 써서 주 버전 변경은 새 필수 필드 도입 같은 호환성을 깨는 변경, 부 버전은 기능 추가, 수 버전은 작은 수정으로 규정하고, MQTT 토픽 경로에 주 버전(v3 등)을 넣는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 오류 유형 UNSUPPORTED_PARAMETER 를 수준 CRITICAL 로 보고하도록 되어 있어, 판 차이로 생긴 미지원 기능이 실행 시점 오류로 드러난다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 팩트시트 스키마는 mobileRobotConfiguration.versions 배열에 로봇에서 도는 하드웨어·소프트웨어 버전(예: softwareVersion)을 키–값으로 담고, batteryCharging 블록에 임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간을 담는다. | ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 상태(state) 스키마는 전원 정보로 충전 상태(stateOfCharge), 원래 용량 대비 배터리 상태(batteryHealth), 충전 중 여부, 현재 충전 상태로 갈 수 있는 추정 거리(range)를, 지도 정보로 mapId·mapVersion·mapStatus 를 로봇이 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f6 | [추정] | MassRobotics AMR 상호운용 표준 JSON 스키마는 제조사명·모델·일련번호, 배터리 잔량 비율, 남은 가동 시간, 오류 코드 목록을 담지만 소프트웨어·펌웨어 버전 필드는 명시적으로 두지 않은 것으로 보인다. | ref-230 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [추정] | VDA 5050 은 소프트웨어 버전을 팩트시트에, 지도 버전을 상태 메시지에 두지만 MassRobotics 스키마는 버전 필드가 없어, 여러 규격이 섞인 플릿에서는 ROP 가 로봇별 버전 목록을 별도로 유지해야 할 것으로 보인다. | ref-228, ref-051, ref-230 | 아니오 | low | 2026-09-25 | — | — |
| f8 | [사실] | ROS 2 관리형 노드 설계는 미구성·비활성·활성·종료의 네 주 상태와 구성·활성화·비활성화·정리·종료 전이를 두어, 실행 전에 구성 요소가 올바로 초기화됐는지 확인하고 실행 중 노드를 교체·재시작할 수 있게 한다. | ref-364 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | ROS 2 배포판 지원 정책(REP 2000)에 따르면 장기 지원판은 5년, 비장기 지원판은 1.5년 지원되며, Humble 은 2022-05~2027-05, Jazzy 는 2024-05~2029-05, Kilted 는 2025-05~2026-11 이 지원 기간이다. | ref-752 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | rmf_simulation 저장소는 지원 대상으로 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 적어, 오케스트레이션 검증용 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리 대상이다. | ref-523 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | IDTA 02007 소프트웨어 명판(Nameplate for Software in Manufacturing) 서브모델은 업데이트·패치 관리·라이선스 관리·감사를 위해 소프트웨어 제품과 설치 인스턴스 정보를 통일된 형태로 표현하며, 버전(주·부·개정·빌드), 배포일·빌드일·설치일, 설치 경로·체크섬, 설치된 버전과 구성 경로 같은 속성을 둔다. | ref-753 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | ISO 17359:2018 은 기계의 상태 감시 프로그램을 세울 때의 일반 절차 지침을 주며, 진동·온도·유량·오염·전력·속도 같은 변수를 쓰고 상태 감시·진단 표준군의 상위 문서 역할을 한다. | ref-754 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f13 | [사실] | ISO 55000:2024(제2판, 2024년 7월, ISO/TC 251)는 자산 관리의 개요·원칙·용어를 정하고 ISO 55000:2014 를 대체하며, 자산에 하드웨어·소프트웨어·설비를 포함하고 수명주기 단계별로 자산의 필요와 성능을 평가하게 한다. | ref-755 | 아니오 | medium | 2024-07 | — | 원문 미열람 |
| f14 | [사실] | Lei 외(2025)의 검토 논문은 산업용 로봇의 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 상태 감시·고장 진단 기술을 상태 기반 정비 구현 관점에서 정리했다. | ref-757 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f15 | [사실] | 2026년 3월 arXiv 프리프린트 'Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots'는 작업 배정·서비스 순서·충전 여부·충전 모드·충전기 접근을 함께 최적화해 플릿 전체의 배터리 열화를 균형 있게 나누는 정식화를 제안했고, 급속 충전에 따른 사이클 열화와 높은 충전 상태로 대기할 때의 달력 열화를 근사 열화 지표로 반영했다. | ref-403 | 아니오 | medium | 2026-03 | 수행 자원 | 원문 미열람 |
| f16 | [사실] | IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템의 패치 관리 프로그램을 운영하는 자산 소유자와 제품 공급자에 대한 요구를 기술하고, 공급자–소유자 간 패치 정보 교환 형식과 패치 개발·배포·설치 활동을 정의하며, 보안 외 패치·업데이트에도 적용될 수 있다고 적는다. | ref-758 | 아니오 | medium | 2015-06 | — | 원문 미열람 |
| f17 | [사실] | EU 기계 규정 (EU) 2023/1230 은 2027-01-20 부터 적용되며, 시장에 나온 기계에 대한 물리적 또는 디지털 변경이 새 위험을 만들거나 기존 위험을 키워 새 보호 조치가 필요하면 '실질적 변경'으로 정의해, 동작을 바꾸는 소프트웨어 업데이트가 이 판단 대상이 될 수 있다. | ref-759 | 아니오 | medium | 2023-06 | — | 원문 미열람 |
| f18 | [추정] | AWS 샘플 저장소의 ROS 2 플릿 무선 펌웨어 업데이트 참조 구현은 IoT Jobs·Greengrass v2·Docker 로 배포를 지시·추적하고 플릿 색인으로 기기별 펌웨어 버전을 조회하며, 실패한 업데이트를 이전의 검증된 버전으로 자동 복귀시킨다고 밝히지만 운영용이 아닌 참조 구현이다. | ref-760 | 아니오 | low | 2026-09-25 | — | 벤더 주장 |
| f19 | [사실] | 2026-07-22 판교에서 열린 SDR(Software Defined Robot) 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍에서 KIST 휴머노이드연구센터가 클라우드 기반 SDR 공통 서비스 프레임워크를 소개했고, 이 플랫폼은 무선 업데이트(OTA)로 로봇 소프트웨어를 갱신하고 기능을 추가하는 것을 목표로 한다고 보도됐다. | ref-761 | 아니오 | low | 2026-07-23 | — | 원문 미열람 |
| f20 | [의견] | 국내 로봇 안전 컨설팅 업체의 위험성평가 가이드는 같은 모델로 교체해도 제어기 펌웨어 버전·안전 기능 파라미터·엔드이펙터 재장착에 따른 정밀도가 달라질 수 있어 기존 위험성평가의 조건 변경에 해당하므로 변경 범위 재평가와 검증 문서 갱신이 필요하다고 권고한다. | ref-763 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f21 | [사실] | 한국로봇사용자협회의 협동로봇 설치 작업장 안전인증은 협동운전 산업용 로봇 시스템이 ISO 10218-2 를 준수하는지 심사하며, 인증서 발급일로부터 2년 주기로 정기 심사한다. | ref-762 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f22 | [추정] | 분류 원문 질문 '제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까?'에 대해, 확인한 자료로는 로봇별 소프트웨어 버전(VDA 5050 팩트시트 versions, 소프트웨어 명판)을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전 변경·팩트시트 기능 선언 변화·안전 파라미터 변화·지도 버전 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 찾지 못했다. | ref-031, ref-228, ref-753, ref-763 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f23 | [추정] | ROP 가 직접 맡을 수명주기 관리 몫은 로봇·어댑터·지도·모델의 버전 목록 유지, 로봇이 보고하는 배터리 상태·오류를 배정·충전 계획에 반영, 업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포하고 실패 시 복구를 조율, 지도 버전 활성화 시점 동기화로 보인다. | ref-031, ref-051, ref-364, ref-760 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f24 | [추정] | 연계 대상: 펌웨어 내용 자체, 관절·감속기 같은 기계 부품의 고장 진단·잔여 수명 예측, 배터리 관리 시스템(BMS) 내부의 열화 추정은 로봇 제조사·설비 쪽 영역이고, ROP 는 그 결과(배터리 상태 값·오류 코드·정비 필요 신호)를 받는 쪽으로 보인다. | ref-757, ref-051, ref-230 | 아니오 | low | 2026-09-25 | — | — |
| f25 | [추정] | 출하 마감 전 집중 시간대에 배터리 상태(batteryHealth)가 낮아진 로봇은 같은 충전 상태에서도 추정 도달 거리(range)가 짧아질 수 있어, 배터리 열화가 작업 배정·충전 계획의 제약으로 작용하는 것으로 보인다. | ref-051, ref-403 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f26 | [추정] | 적치 구역의 랙 배치가 바뀌면 플릿 제어가 새 mapVersion 을 로봇에 내려받게 한 뒤 enableMap 으로 전환해야 하고, 같은 mapId 에 한 버전만 활성화되므로 전환 시점과 진행 중 주문의 정리가 적치 작업 재개의 시작 조건이 되는 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 적치 / 시작 조건 | — |
| f27 | [의견] | 24. 자산·소프트웨어 수명주기 관리는 업데이트 뒤 회귀·장애 시험(23. 시험·형식 검증·벤치마크), 시뮬레이션 환경의 판 관리(22. 시뮬레이션·예측용 디지털 트윈), 보안 패치(26. 사이버보안·접근권한·개인정보), 변경 후 안전 재평가(25. 안전·위험 관리), 배터리 열화를 반영한 충전(16. 공용 자원·충전·에너지 최적화)과 맞물리는 것으로 보인다. | ref-523, ref-758, ref-403, ref-763 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: 6.3.1 지도 배포: 지도는 mapId 와 mapVersion 조합으로 식별, 지도 서버→로봇 전송은 플릿 제어가 시작하는 pull 방식. 6.3.2: "There shall only be one version of maps with the same mapId enabled at a time." (VDA 5050 3.0.0, 공식 저장소 main)
- **f2**: 1절: 주 버전(x.0.0)은 breaking changes(새 비선택 필드 도입 등), 부 버전은 새 기능, 수 버전은 오탈자 등 수정. 4.2절 토픽 예: vda5050/v3/KIT/0001/order (3.0.0 판)
- **f3**: 6.1.4.2: 로봇이 쓸 수 없는 선택 필드가 있는 주문을 받으면 'UNSUPPORTED_PARAMETER' 오류를 'CRITICAL' 수준으로 보고. 판 불일치 처리 절차 자체는 명세에 명시되지 않음
- **f4**: versions: "various hardware and software versions running on the mobile robot"(예 softwareVersion, cameraVersion, plcSoftChecksum). batteryCharging: criticalLowChargingLevel, minimumDesiredChargingLevel, maximumDesiredChargingLevel, minimumChargingTime
- **f5**: powerSupply: stateOfCharge(0~100%), batteryVoltage, batteryCurrent, batteryHealth(0~100%), charging, range("Estimated reach with current State of Charge in meter"). maps: mapId, mapVersion, mapDescriptor, mapStatus(ENABLED/DISABLED) (발행일 미확인, 확인일 기준)
- **f6**: identityReport/statusReport: manufacturerName, robotModel, robotSerialNumber, batteryPercentage, remainingRunTime, maxRunTime, errorCodes("omitted for normal operation"), supportVendorName. 버전 필드는 스키마 요약에서 찾지 못함(부재는 요약 판독 기준)
- **f7**: f4·f5·f6 의 스키마 비교에서 도출한 추정. 실제 다규격 플릿에서 버전 목록을 관리하는 공개 사례는 확인하지 못함
- **f8**: "A managed life cycle for nodes allows greater control over the state of ROS system." 주 상태 Unconfigured·Inactive·Active·Finalized, 전이 상태 Configuring·CleaningUp·Activating·Deactivating·ShuttingDown·ErrorProcessing (발행일 미확인, 확인일 기준)
- **f9**: "LTS releases come with 5 years of standard support", 비LTS 1.5년(다음 LTS 와 6개월 겹침). Humble EOL 2027-05, Jazzy EOL 2029-05, Kilted EOL 2026-11 (발행일 미확인, 확인일 기준)
- **f10**: Gazebo Classic 11(2025년 1월 지원 종료)과 Gazebo Fortress 지원 명시 (재인용: 2026-09-25-56)
- **f11**: 목적: "a uniform representation" 으로 updates, patch management, license management, audits 지원. 제품 정의와 설치 인스턴스 상태를 함께 기술 (IDTA 02007-1-0, 발행일 미확인, 확인일 기준)
- **f12**: ISO 17359:2018 gives guidelines for the general procedures ... setting up a condition monitoring programme for machines (검색 요약 범위)
- **f13**: ISO 55000:2024 Asset management — Vocabulary, overview and principles. 제2판 2024-07, 2014 판 대체. 원칙: 가치, 정렬, 리더십 등 (검색 요약 범위)
- **f14**: Science China Technological Sciences 68, 1110301 (2025). 고장 모드·원인 분석, 데이터 수집·센서, 모델 기반·데이터 기반 방법 검토 (검색 요약 범위)
- **f15**: fast charging intensifies cycling-related wear, and prolonged idling at elevated SOC accelerates calendar aging. 비교 기준: 최근접 가용 규칙, 열화 무시 에너지 인지 정식화, 충전기 용량 무시 정식화 (프리프린트, 검색 요약 범위)
- **f16**: defined format for the distribution of information about security patches ... may also be applicable for non-security related patches or updates. 취약점 발견~패치 사이 완화는 다루지 않음 (제1판 2015-06, 검색 요약 범위)
- **f17**: 적용일 2027-01-20. 제3조(16) substantial modification: physical or digital change ... introduces a new hazard or increases an existing risk (검색 요약 범위, 원문 조문 미열람)
- **f18**: 벤더 주장: "Automatically roll back failed firmware updates to previously running (known good) versions". 참조·시연용 구현으로 명시(발행일 미확인, 확인일 기준)
- **f19**: 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장(2026-07-23 보도). 원 매체·과제 공식 자료 미확인(검색 요약 범위)
- **f20**: 동일 모델 교체 시에도 펌웨어 버전·안전 기능 파라미터·엔드이펙터 정밀도 변화 → 위험성평가 조건 변경 → 변경 범위 재평가와 검증 문서 갱신 필요(검색 요약 범위, 요약 문장의 출처 귀속은 검색 결과 기준으로만 확인)
- **f21**: 협동 로봇 설치 작업장 안전인증 심사규정: 영리 생산 목적 상시 작업장 대상, 발급일로부터 2년 주기 정기 심사(검색 요약 범위, 펌웨어 변경 시 재심사 여부는 미확인)
- **f22**: f2(주 버전=호환성 깨짐), f4(팩트시트 versions), f11(소프트웨어 명판의 설치 인스턴스), f20(펌웨어·안전 파라미터 변경→재평가)에서 도출한 추정
- **f23**: 플릿 제어가 지도 pull·enableMap 을 지시(f1), 로봇이 batteryHealth·range 보고(f5), 관리형 노드의 교체·재시작(f8), 버전 조회·복귀(f18, 벤더 주장)에서 도출
- **f24**: 산업용 로봇 상태 감시는 센서·모델 기반 부품 진단(f14), 규격은 batteryHealth·errorCodes 같은 결과 값만 교환(f5·f6). 분류 원문 9장 '로봇 자체 지능·제어' 경계
- **f25**: state 스키마의 batteryHealth·range(f5)와 열화 인지 플릿 스케줄링 연구(f15)에서 도출한 시나리오 추정. 물류센터 실측 자료는 확인하지 못함
- **f26**: downloadMap·enableMap 동작과 '한 mapId 한 활성 버전' 규칙(f1)에서 도출한 시나리오 추정
- **f27**: f10(시뮬레이터 지원 종료), f16(패치 관리), f15(열화 인지 충전), f20(변경 후 재평가)을 영역 연결로 정리한 의견

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-364 | Open Robotics (ROS 2 Design) | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 아니오 |
| ref-752 | Open Robotics (ROS REP) | REP 2000 -- ROS 2 Releases and Target Platforms | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://www.ros.org/reps/rep-2000.html | 아니오 |
| ref-753 | IDTA (admin-shell-io/id GitHub) | IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md | 아니오 |
| ref-754 | ISO | ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines | 2018 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/71194.html | 예 |
| ref-755 | ISO | ISO 55000:2024 - Asset management — Vocabulary, overview and principles | 2024-07 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83053.html | 예 |
| ref-403 | arXiv (저자 미확인) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-757 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 예 |
| ref-758 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | 표준 | medium | 2026-09-25 | https://webstore.iec.ch/en/publication/22811 | 예 |
| ref-759 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | medium | 2026-09-25 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-760 | Amazon Web Services (aws-samples GitHub) | ros2-ota-firmware-updates — README | 미확인 | 벤더 문서 | low | 2026-09-25 | https://github.com/aws-samples/ros2-ota-firmware-updates | 아니오 |
| ref-761 | 네이트 뉴스(원 매체 미확인) | 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장 | 2026-07-23 | 기사 | low | 2026-09-25 | https://m.news.nate.com/view/20260723n24828 | 예 |
| ref-762 | 한국로봇사용자협회 | 협동로봇 설치 작업장 안전인증 안내 | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.korua.or.kr/inspect/inspectInfo.do | 예 |
| ref-763 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | 벤더 문서 | low | 2026-09-25 | https://doc.safetics.io/insight-risk-assessment/ | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-523 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_simulation | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 의미적 버전 규칙, 토픽의 주 버전, 지도 배포·버전(downloadMap·enableMap·deleteMap), 미지원 파라미터 오류 규정 확인.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마. powerSupply(stateOfCharge·batteryHealth·charging·range)와 maps(mapId·mapVersion·mapStatus) 필드 확인.
- **ref-364**: ROS 2 관리형 노드의 주 상태·전이 상태·전이와 목적(초기화 확인, 실행 중 교체·재시작) 설계 문서.
- **ref-752**: ROS 2 배포판별 출시·지원 종료 일정과 LTS 5년·비LTS 1.5년 지원 정책.
- **ref-753**: 자산관리셸 소프트웨어 명판 서브모델의 목적(업데이트·패치·라이선스·감사)과 버전·설치 인스턴스 속성.
- **ref-754**: 원문 미열람. 기계 상태 감시 프로그램 수립 일반 지침, 상태 감시·진단 표준군의 상위 문서.
- **ref-755**: 원문 미열람. 자산 관리 개요·원칙·용어 제2판(2014 판 대체), 수명주기 단계별 자산 평가.
- **ref-403**: 원문 미열람. AMR 플릿의 작업 배정·충전을 배터리 열화 균형과 함께 최적화하는 프리프린트.
- **ref-757**: 원문 미열람. 산업용 로봇 고장 모드, 데이터 수집, 모델·데이터 기반 상태 감시·고장 진단 검토.
- **ref-758**: 원문 미열람. 산업 제어 시스템 패치 관리 프로그램의 소유자·공급자 요구와 패치 정보 교환 형식.
- **ref-759**: 원문 미열람. EU 기계 규정. 2027-01-20 적용, 디지털 변경을 포함한 실질적 변경 정의.
- **ref-760**: ROS 2 플릿 무선 펌웨어 업데이트 참조 구현(IoT Jobs·Greengrass·Docker, 버전 추적, 롤백 주장). 운영용 아님.
- **ref-761**: 원문 미열람. SDR 차세대 로봇 공통 플랫폼 기술개발 3차년도 착수 워크숍과 클라우드 기반 OTA 목표 보도.
- **ref-762**: 원문 미열람. 협동로봇 설치 작업장 안전인증(ISO 10218-2 준수 심사, 2년 주기 정기 심사) 안내.
- **ref-763**: 원문 미열람. 로봇 시스템 위험성평가 가이드. 동일 모델 교체 시 펌웨어·안전 파라미터 변경에 따른 재평가 권고.
- **ref-228**: VDA 5050 팩트시트 JSON 스키마. 이번 실행에서 versions 배열과 batteryCharging 블록 확인.
- **ref-230**: MassRobotics AMR 상호운용 표준 JSON 스키마. 이번 실행에서 식별·배터리·오류 필드 확인.
- **ref-523**: 원문 미열람. Open-RMF 시뮬레이션 플러그인 저장소 README(이번 실행에서 다시 열지 않음, 2026-09-25-56 확인 내용 재사용).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f17(디지털 변경도 실질적 변경 판단 대상), f9(배포판 지원 종료), f22(분류 원문 질문 — 추정) / 4절 핵심 개념: f13(자산·수명주기), f12(상태 감시), f5(배터리 상태), f11(소프트웨어 명판), f16(패치 관리), f1(지도 버전) / 5절 현장 시나리오: f26(적치·시작 조건), f25(출하·제약), f20·f21(교체 후 재평가, 의견·국내 제도) / 6절 대표 접근법: f14(상태 감시·고장 진단), f15(열화 인지 스케줄링), f8(관리형 노드), f18(OTA·롤백, 벤더 주장 병기), f19(국내 SDR 과제) / 7절 표준·오픈소스: f1~f5(VDA 5050), f6(MassRobotics), f11(IDTA 02007), f12·f13·f16·f17, f9·f10 / 8절 대표 연구: f14·f15 / 9절 경계: f23(ROP 직접), f24('연계 대상') / 10절 연결: f27(23. 시험·형식 검증·벤치마크, 22. 시뮬레이션·예측용 디지털 트윈, 26. 사이버보안·접근권한·개인정보, 25. 안전·위험 관리, 16. 공용 자원·충전·에너지 최적화), f7·f4(21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스), f26(6. 지도·공간·위치 모델) / 11절: open_questions_new 4건. 벤더 주장 f18 은 [추정]+'벤더 주장', f20 은 [의견]. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 예지보전 | Predictive Maintenance (PdM) | 설비의 상태 데이터로 고장 시점을 예측해 고장 전에 정비를 계획하는 정비 방식이다. |
| 상태 기반 정비 | Condition-Based Maintenance (CBM) | 정해진 주기 대신 상태 감시로 확인한 설비 상태에 따라 정비 여부와 시점을 정하는 정비 방식이다. |
| 배터리 건강 상태 | State of Health (SOH) | 배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다. |
| 소프트웨어 명판 | Software Nameplate (IDTA 02007) | 자산관리셸에서 소프트웨어 제품과 설치 인스턴스의 식별·버전·설치 정보를 통일된 형태로 기술하는 서브모델이다. |
| 무선 업데이트 | Over-the-Air Update (OTA) | 기기를 회수하지 않고 네트워크로 소프트웨어·펌웨어를 내려받아 갱신하는 방식이다. |

## 열린 질문

새로 생긴 질문:

- 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반
- VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f2 | 종류: 일반
- 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f21 | 종류: 일반
- EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - f6: MassRobotics 스키마의 버전 필드 부재는 요약 판독 기준이라 추정으로 둠
    - f17: EU 2023/1230 조문 원문 미열람, 제조사가 예정한 업데이트의 취급은 2차 해설에만 있어 finding 에서 제외
    - f19: 원 매체와 SDR 과제 공식 자료 미확인
    - f20·f21: 검색 요약 문장의 출처 귀속(세이프틱스/한국로봇사용자협회)을 원문으로 확인하지 못함
    - ref-403 저자, ref-031·ref-051·ref-753 발행일 미확인
    - f22: 펌웨어 변경 영향 범위 산정 공개 절차 찾지 못함
- 범위 경계 위반 의심:
    - f24: 감속기·관절 진단, BMS 내부 열화 추정은 분류 원문 9장 '로봇 자체 지능·제어' 쪽이므로 '연계 대상:'으로 표시
    - f14·f15: 부품 진단·열화 모델 연구는 ROP 가 결과를 받아 쓰는 근거로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-051·ref-364·ref-752·ref-753·ref-760 과 재사용 ref-228·ref-230. 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 17회/30, 신규 출처 15건/15(ref-031~ref-763, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 13374, ISO 10218-1:2025(사이버보안 요구 추가), CISA SBOM, ICAN-Deploy(카나리 배포 프리프린트)는 출처로 넣지 않음. 재사용 3건: ref-228·ref-230(2026-09-25-57 브리프 값), ref-523(2026-09-25-56 브리프 값, 이번에 다시 열지 않음). 교차 확인 0건. 한국 자료: 한국로봇사용자협회 안전인증(ref-762), 세이프틱스 가이드(ref-763, 의견), SDR 과제 보도(ref-761). 27. AI·학습·적응과 모델 운영 관련 finding 없음(모델 버전 관리는 일반 수명주기 관점으로만 다룸). 8·22 구분: f10 은 시뮬레이션 환경의 판 관리로만 서술. 정정 요청 없음, 대상 영역 열린 질문 0건.
