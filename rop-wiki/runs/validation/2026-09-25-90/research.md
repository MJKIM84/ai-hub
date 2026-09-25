# 리서치 브리프 2026-09-25-90

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-90 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 온톨로지 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 1 · 답한 질문 q1-07

## 갭(비어 있거나 약한 섹션)

- 단계 1 질문 q1-07 열림(target.json 지정: CLI 지정 질문 id)
- 모델·표준 비교표 VDA 5050 행: 파라미터 범위·적재·환경 제약 칸이 판 미확인 [추정](GitHub main 브랜치·구현 라이브러리 문서 혼재)으로만 채워져 있음
- 단계 1 페이지 3절 q1-02 답의 팩트시트 블록 서술이 원문 미열람 추정(이전 실행 f11)
- 완료 조건: 모델·표준 비교표의 다섯 정보 항목 열 대부분 미조사, ROP용 능력 개념 요구 목록 초안 미반영(q1-06 미조사)
- 아이디어 1 페이지 4절(필요한 데이터와 표준) 비어 있음

## 조사 질문

1. 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]
2. q1-07 VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가?
3. VDA 5050 공식 저장소에서 2.0.0·2.1.0·3.0.0 태그별 팩트시트 기계가독 스키마(json_schemas/factsheet.schema)와 명세 본문은 어느 판에 있고, 팩트시트는 필수 토픽인가? (q1-07 전제, 비교표 VDA 5050 행의 '판 미확인' 해소 겨냥)
4. 3.0.0 팩트시트의 지원 action 기술(mobileRobotActions)에는 완료·결과, 일시정지·취소 가능 여부 같은 실행 관련 정보가 있는가? (q1-03 다섯 정보 항목 중 완료 확인 방법·오류의 의미 보강)
5. 3.0.0 팩트시트의 충전 관련 설정(범위 능력 '충전')과 구역(zone) 지원 선언은 어떤 필드로 기술되는가? (아이디어 1 페이지 4절, 16. 공용 자원·충전·에너지 최적화 겨냥)
6. 사용자 실험 experiments/2026-09-25-vda5050-factsheet-field-diff/ 의 필드 비교 결과가 공식 스키마 원문과 일치하는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소의 팩트시트 JSON 스키마는 최상위 필드가 2.1.0과 3.0.0 모두 12개이며, 2.1.0의 agvGeometry·vehicleConfig가 3.0.0에서 mobileRobotGeometry·mobileRobotConfiguration으로 바뀌었고 나머지(headerId, timestamp, version, manufacturer, serialNumber, typeSpecification, physicalParameters, protocolLimits, protocolFeatures, loadSpecification)는 이름이 같다. | ref-044, ref-045 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 팩트시트는 적재 제약을 loadSpecification.loadSets[] 의 적재 세트마다 기술하며, 세트별로 setName, loadType(예: EPAL), 적용 적재 장치(loadPositions), 기준 경계 상자(boundingBoxReference), 적재 치수(loadDimensions: 길이·폭 필수, 높이 선택), 최대 중량 maximumWeight(kg), 취급 높이·깊이의 최소·최대(m), 취급 기울기 최소·최대(rad), 적재 시 maximumSpeed(m/s)·maximumAcceleration·maximumDeceleration(m/s²), 적재·하역 소요 시간 pickTime·dropTime(s), 설명을 둔다. | ref-044 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f3 | [사실] | VDA 5050 2.1.0 팩트시트 스키마의 loadSets[] 도 같은 구조로 setName, loadType, loadPositions, boundingBoxReference, loadDimensions, maxWeight(kg), min/maxLoadhandlingHeight·Depth(m), min/maxLoadhandlingTilt(rad), agvSpeedLimit, agvAccelerationLimit, agvDecelerationLimit, pickTime, dropTime, description 을 둔다. | ref-045 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [추정] | 2.1.0에서 3.0.0으로 오면서 적재 제약 필드는 구조가 유지된 채 이름만 바뀐 것으로 보인다(max* → maximum*/minimum*, agvSpeedLimit·agvAccelerationLimit·agvDecelerationLimit → maximumSpeed·maximumAcceleration·maximumDeceleration, maxLoadMass → maximumLoadMass), 적재 세트에 새 종류의 제약 필드가 더해진 것은 경로 비교 범위에서 확인되지 않았다. | ref-044, ref-045 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f5 | [사실] | VDA 5050 3.0.0 팩트시트의 유형 명세(typeSpecification)는 seriesName, seriesDescription, mobileRobotKinematics(DIFFERENTIAL·OMNIDIRECTIONAL·THREE_WHEEL), mobileRobotClass(FORKLIFT·CONVEYOR·TUGGER·CARRIER), maximumLoadMass(kg), localizationTypes, navigationTypes, supportedZones 를 두며, 2.1.0에서는 같은 자리에 agvKinematic(DIFF·OMNI·THREEWHEEL), agvClass, maxLoadMass 가 있었고 supportedZones 는 없었다. | ref-044, ref-045 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f6 | [사실] | VDA 5050 3.0.0 팩트시트는 typeSpecification.supportedZones 로 로봇이 처리할 수 있는 구역 유형(BLOCKED, LINE_GUIDED, RELEASE, COORDINATED_REPLANNING, SPEED_LIMIT, ACTION, PRIORITY, PENALTY, DIRECTED, BIDIRECTED)을 선언하게 한다. | ref-044 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f7 | [사실] | VDA 5050 3.0.0 팩트시트의 지원 action 목록(protocolFeatures.mobileRobotActions)은 action 마다 actionType, actionDescription, actionScopes(INSTANT·NODE·EDGE·ZONE), actionParameters(key·valueDataType·description·isOptional), actionResult, blockingTypes(NONE·SOFT·SINGLE·HARD), pauseAllowed, cancelAllowed 를 두며, 2.1.0의 agvActions 는 resultDescription 과 actionScopes(INSTANT·NODE·EDGE)·blockingTypes(NONE·SOFT·HARD)만 있었고 pauseAllowed·cancelAllowed 는 없었다. | ref-044, ref-045 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f8 | [사실] | VDA 5050 3.0.0 팩트시트는 mobileRobotConfiguration 아래 충전 설정(batteryCharging)으로 임계 저충전량(criticalLowChargingLevel, 이하이면 관제가 충전으로 보냄), 최저·최고 희망 충전량(%), 최소 충전 시간(s)을 기술하게 하며, 2.1.0의 vehicleConfig 에는 이 항목이 없었다. | ref-044, ref-045 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | VDA 5050 3.0.0 명세는 AGV 대신 이동로봇(mobile robot) 용어를 쓰고, factsheet 를 관제–로봇 사이 필수(mandatory) 토픽으로 두며 그 구현을 7.10절에서 정한다. | ref-046 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f10 | [사실] | VDA 5050 2.1.0 명세는 팩트시트를 6.15절 Topic "factsheet"에서 정의하고, 2.0.0 태그의 명세 마크다운은 7장 AGV Factsheet 에서 팩트시트를 AGV 유형 시리즈의 기본 정보로 정의하며 AGV 가 factsheet 하위 토픽으로 이를 알려야 한다고 적는다. | ref-047, ref-048 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [추정] | VDA 5050 2.0.0 태그 명세의 팩트시트 블록은 typeSpecification, physicalParameters, protocolLimits, protocolFeatures, agvGeometry, loadSpecification(적재 능력의 추상 명세)으로 설명되고 vehicleConfig 블록은 보이지 않아, 2.0.0 대비 비교에서 vehicleConfig 는 2.1.0 이후 항목일 가능성이 있다. | ref-048 | 아니오 | low | 2026-09-25 | — | — |
| f12 | [추정] | VDA 5050 3.0.0 팩트시트의 적재 세트 필드는 '같은 운반 로봇 중 누가 이 화물을 취급할 수 있는가'를 판정할 재료(적재 유형별 중량·치수·취급 높이·기울기 범위, 적재 시 속도 한계, 적재·하역 시간)를 제조사 선언값으로 제공하므로, ROP 능력 온톨로지에서 적재 유형에 묶인 제약(최소·최대 범위와 단위)으로 옮길 수 있을 것으로 보인다. | ref-044 | 아니오 | low | 2026-09-25 | 제약 | — |
| f13 | [추정] | 사용자 실험은 VDA 5050 팩트시트 스키마 2.1.0과 3.0.0의 필드 경로를 재귀 비교해 경로 수 132개 대 144개, 3.0.0에만 있는 경로 104개·2.1.0에만 있는 경로 92개를 보고했고, 공식 저장소 2.0.0 태그에는 팩트시트 스키마 파일이 없어(404) 2.0 대비 비교를 2.1.0 대비로 대신했다. | — | 아니오 | medium | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 3.0.0 스키마(title 'Mobile Robot Factsheet') 최상위 properties 12개와 2.1.0 스키마 최상위 properties 12개를 원문에서 직접 대조. 사용자 실험의 최상위 필드 목록과도 일치. (발행일 미확인, 확인일 기준)
- **f2**: 3.0.0 factsheet.schema loadSets items: maximumWeight "Maximum weight of loadtype"(kg), minimum/maximumLoadhandlingHeight·Depth(m), Tilt(rad), maximumSpeed(m/s), pickTime·dropTime(s). loadPositions 가 비면 모든 적재 장치에 적용. (발행일 미확인, 확인일 기준)
- **f3**: 2.1.0 factsheet.schema loadSets items 필드 목록을 원문에서 확인. typeSpecification 에는 maxLoadMass(kg). 2.1.0 명세 본문도 6.15절 Topic "factsheet" 에 maxWeight·agvSpeedLimit·pickTime 을 싣는다. (발행일 미확인, 확인일 기준)
- **f4**: 두 판 스키마의 loadSets 필드를 대조한 추론. 설명문·단위의 의미 동일성은 확인하지 않았다. 사용자 실험(경로 문자열 비교)도 '대부분 이름 변경'으로 같은 결론. (발행일 미확인, 확인일 기준)
- **f5**: 3.0.0 typeSpecification: maximumLoadMass "Maximum loadable mass"(kg). 2.1.0 typeSpecification: agvKinematic DIFF/OMNI/THREEWHEEL, maxLoadMass(kg). 열거값 표기도 바뀜. (발행일 미확인, 확인일 기준)
- **f6**: 3.0.0 factsheet.schema typeSpecification.supportedZones 열거값 10개를 원문에서 확인. 2.1.0 스키마에는 이 필드가 없다. (발행일 미확인, 확인일 기준)
- **f7**: 3.0.0: pauseAllowed "Action can be paused via startPause", cancelAllowed 는 cancelOrder 로 취소 가능 여부, actionResult "Description of the result". 3.0.0 명세 본문은 pauseAllowed=true 인 action 만 일시정지된다고 적는다. (발행일 미확인, 확인일 기준)
- **f8**: 3.0.0 batteryCharging: criticalLowChargingLevel "Critical charging level in percent"(0–100), minimumChargingTime(s). 원 스키마 키 이름 끝에 공백이 있다는 점은 사용자 실험이 보고. (발행일 미확인, 확인일 기준)
- **f9**: 3.0.0 명세: "The mobile robot shall communicate this information via the topic factsheet in a specific way that is defined in Section 7.10." 토픽 표에서 factsheet 는 mandatory. 문서에 3.0.0 발행일 표기는 없음. (발행일 미확인, 확인일 기준)
- **f10**: 2.0.0 태그 명세: "The AGV must communicate this information via the subtopic factsheet". 단, 2.0.0 태그 문서 머리에 'RELEASE CANDIDATE, FOR REVIEW' 표기가 있어 VDA 게시 PDF 와 동일성 미확인. (발행일 미확인, 확인일 기준)
- **f11**: 2.0.0 태그 명세 7장: loadSpecification "Abstract specification of load capabilities". 열람한 본문이 loadSets 세부 필드 앞에서 잘려 2.0.0 의 적재 세트 필드는 확인하지 못함. vehicleConfig 부재도 잘린 본문 기준. (발행일 미확인, 확인일 기준)
- **f12**: f2 필드를 분류 원문 5. 로봇 능력·작업 온톨로지의 SCM 질문과 온톨로지 초안 '제약' 개념에 대응시킨 추론. 값은 제조사가 채우는 광고 능력이며 현장 검증 여부는 별개. (발행일 미확인, 확인일 기준)
- **f13**: 사용자 실험 (experiments/2026-09-25-vda5050-factsheet-field-diff/): field paths 2.1.0 132, 3.0.0 144, added 104, removed 92. 이번 실행에서도 2.0.0 태그 json_schemas/factsheet.schema 가 404 임을 재확인했다. 경로 수 자체는 재계산하지 않음.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-044 | VDA / VDMA (VDA5050 GitHub) | VDA5050/json_schemas/factsheet.schema (tag 3.0.0) — Mobile Robot Factsheet | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema | 아니오 |
| ref-045 | VDA / VDMA (VDA5050 GitHub) | VDA5050/json_schemas/factsheet.schema (tag 2.1.0) — AGV Factsheet | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema | 아니오 |
| ref-046 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md (tag 3.0.0) — VDA 5050 Version 3.0.0 specification | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md | 아니오 |
| ref-047 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md (tag 2.1.0) — VDA 5050 Version 2.1.0 specification | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md | 아니오 |
| ref-048 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN_V1.md (tag 2.0.0) — VDA 5050 Version 2.0.0 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md | 아니오 |

### 출처 요약

- **ref-044**: VDA 5050 공식 저장소 3.0.0 태그의 팩트시트 JSON 스키마. typeSpecification(supportedZones 포함), loadSpecification.loadSets, protocolFeatures.mobileRobotActions(actionResult·pauseAllowed·cancelAllowed), mobileRobotConfiguration.batteryCharging 필드를 정의한다.
- **ref-045**: VDA 5050 공식 저장소 2.1.0 태그의 팩트시트 JSON 스키마. agvGeometry·vehicleConfig, loadSets(maxWeight·agvSpeedLimit 등), agvActions(resultDescription) 필드를 정의한다.
- **ref-046**: VDA 5050 3.0.0 명세 본문(공식 저장소 3.0.0 태그). 이동로봇 용어, factsheet 필수 토픽과 7.10절 구현 규정, action 일시정지 규칙을 담는다. 문서에 발행일 표기 없음.
- **ref-047**: VDA 5050 2.1.0 명세 본문(공식 저장소 2.1.0 태그). 6.15절 Topic "factsheet"에서 팩트시트를 정의한다. 열람 본문이 팩트시트 표 중간에서 잘렸다.
- **ref-048**: 공식 저장소 2.0.0 태그의 명세 마크다운. 7장 AGV Factsheet 를 담으나 머리말에 'RELEASE CANDIDATE, FOR REVIEW' 표기가 있어 VDA 게시 PDF(ref-022)와 동일성 미확인. 열람 본문이 loadSets 앞에서 잘렸다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q1-07 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13 (신뢰도 medium) — 단계 1 질문 목록 q1-07 상태 '답함', 3절에 q1-07 소제목 신설(적재 제약은 loadSets 적재 세트별 필드, 2.1.0→3.0.0 이름 변경, 3.0.0 신규 supportedZones·actionResult·pauseAllowed·cancelAllowed·batteryCharging, 2.0.0 스키마 부재로 2.1.0 대비 비교), q1-02 답의 팩트시트 블록 서술(이전 f11 추정)을 원문 열람 근거로 보강하되 판(2.1.0/3.0.0) 명시, 4절 남은 불확실성에서 '팩트시트 판 미확인' 항목 갱신, 후속 질문 1건, 사용자 실험 반영([사용자 실험] 태그), 출처 ref-044~ref-048 추가 |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | 4, 5, 7, 8 | 트랙 산출물 갱신: VDA 5050의 팩트시트 행을 원문 열람 근거로 고침 — 파라미터 범위(f2: 적재 세트별 최소·최대와 단위), 적재·환경 제약(f2·f6: 적재 세트, supportedZones), 완료 확인 방법(f7: actionResult 는 결과 설명 자유 문장), 오류의 의미는 기존 유지, 종류 칸 판 명시(2.1.0/3.0.0 스키마), 상태 '확인(3.0.0 스키마 원문 열람)'. 5절 빠진 정보 요약의 VDA 5050 '판 미확인' 문구 갱신 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | 2, 6, 7 | 트랙 산출물 갱신: track.ontology_changes 가 승인되면 제약·기능·실행 조건의 속성 후보 수정 반영(f2·f7·f8·f12). 미승인 제안은 6절 질문으로 |
| update | docs/ideas/robot-capability-ontology.md | 4 | 아이디어 페이지 4절: 필요한 데이터와 표준 — VDA 5050 3.0.0 팩트시트가 범위 능력 '적재'(f2·f5), '충전'(f8), 이동 구역 제약(f6)을 기술하는 필드를 제공한다는 근거 |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f2, f5, f7, f9, f12): VDA 5050 3.0.0 팩트시트의 적재 세트·지원 action 기술을 능력 기술 표준 사례로 |
| update | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f1, f7, f9, f10): VDA 5050 팩트시트 필수 토픽, 2.1.0→3.0.0 필드 이름 변경(어댑터 판별 영향), pauseAllowed·cancelAllowed |
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f8): VDA 5050 3.0.0 팩트시트 batteryCharging(임계 저충전량, 희망 충전량 범위, 최소 충전 시간) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| VDA 5050 팩트시트 | VDA 5050 Factsheet | VDA 5050에서 이동로봇이 유형 명세·물리 파라미터·프로토콜 한계·지원 action·기하·적재 명세·설정을 상위 관제에 알리는 필수 토픽 메시지이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 5 · 교차 확인: 0
- 예산 사용량: 검색 2회 · 신규 출처 5건
- 미확인 항목:
    - f4 이름이 바뀐 적재 필드의 의미·단위 동일성(설명문 비교) 미확인
    - f11 2.0.0 태그 명세 본문이 잘려 2.0.0 loadSets 필드와 vehicleConfig 유무를 확인하지 못함, 2.0.0 태그 문서와 VDA 게시 PDF(ref-022)의 동일성 미확인
    - ref-044~ref-048 발행일 미확인(3.0.0 명세·README 에 발행일 표기 없음) — oq-005(VDA 5050 3.0.0 발행일 출처 충돌)는 해소하지 못함
    - 3.0.0 명세 7.10절 팩트시트 본문은 열람 본문이 잘려 스키마로만 필드를 확인
    - 모든 finding 교차 확인 없음: 같은 기관의 판별 산출물이라 독립 출처가 아님
- 범위 경계 위반 의심:
    - 없음
- 한계: fetch_mode mirror_only: raw.githubusercontent.com 의 VDA 5050 공식 저장소 태그(2.0.0·2.1.0·3.0.0)만 열었고 원문 열람 출처는 모두 fetched=true 로 적었다. 검색 2회(40회 상한), 신규 출처 5건(ref-044~ref-048). 질문 선택: target.json 지정 q1-07(CLI 지정). 2.0.0 태그에는 팩트시트 스키마가 없어(404, 이번 실행에서 재확인) 질문의 '2.0 대비'는 2.1.0 대비로 답했고 2.0.0 은 명세 본문(잘림)으로만 보충했다. WebFetch 요약 모델이 긴 명세 본문을 잘라 읽어 3.0.0 7.10절·2.1.0 6.15절의 필드 표는 스키마로 대신했다. 사용자 실험 반영: experiments/2026-09-25-vda5050-factsheet-field-diff/ → f13(그리고 f1·f4·f8 근거 발췌에 일치 사실 언급). 사용자 실험의 최상위 필드·신규 필드·적재 필드 목록은 공식 스키마 원문과 일치했다. 신뢰도: 원문 출처는 high 지만 finding 은 단일 기관 출처라 medium 이하로 두었다. 용어 후보는 조사한 1건(VDA 5050 팩트시트)만 냈다. 기존 용어집 'VDA 5050' 항목의 정의가 표준 자체가 아니라 팩트시트 메시지를 설명하고 있어 정정이 필요해 보인다(스토리텔러·검증 확인 요망). 한국어 검색은 하지 않았다: 질문이 공식 스키마 원문 대조로 답해져 국내 자료가 필요한 범위가 아니었다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 후속 질문 1건, 온톨로지 변경 제안 3건(모두 modify, 속성 후보 수정).

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 1
- 답한 질문 id: q1-07

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | q1-07 후속: VDA 5050 2.1.0→3.0.0에서 이름이 바뀐 팩트시트 필드(예: agvSpeedLimit→maximumSpeed, maxWeight→maximumWeight)는 설명문·단위·필수 여부까지 같은가, 의미가 바뀐 필드가 있다면 기존 2.x 로봇의 팩트시트를 3.0 능력 모델로 옮길 때 무엇을 다시 확인해야 하는가? | 1 | f4 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 제약 (Constraint) | f2, f12 | 주요 속성 후보에 '적용 대상(적재 유형·적재 장치)', '최소값·최대값', '단위'를 더한다. VDA 5050 3.0.0 팩트시트가 적재 제약을 적재 세트(loadType, loadPositions)별 최소·최대 범위(kg, m, rad, m/s)로 기술하는 데 근거. 값의 출처는 제조사 선언(광고 능력)이다. |
| modify | concept | 기능 (Capability) | f7 | 주요 속성 후보에 '일시정지 가능 여부', '취소 가능 여부', '결과 설명'을 더한다(VDA 5050 3.0.0 mobileRobotActions 의 pauseAllowed·cancelAllowed·actionResult). 기능과 스킬 중 어디에 둘지는 6절 질문과 충돌할 수 있어 검증 판단 필요. |
| modify | concept | 실행 조건 (Execution Condition) | f8 | 조건 항목 예로 '임계 저충전량(이하이면 충전으로 보냄)'을 더한다(VDA 5050 3.0.0 batteryCharging.criticalLowChargingLevel). 범위 능력 '충전'과 연결. 제약과의 경계는 기존 6절 질문을 따른다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 모델·표준 비교표의 다섯 정보 항목 열이 VDA 5050 행 외에는 대부분 미조사
    - ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 미반영(q1-06 미조사)
    - 막힌 질문: q1-03 부분 답, q1-04·q1-05·q1-06·q1-08 열림
