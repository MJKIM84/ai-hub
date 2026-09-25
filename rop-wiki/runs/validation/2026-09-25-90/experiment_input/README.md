# VDA 5050 팩트시트 스키마 필드 비교(2.1.0 → 3.0.0) — 검증용 예시 실험

- 트랙: manual-capability-ontology
- 단계: 1
- 답하려는 질문: q1-07
- 실험 계획: 자체 설계
- 수행일: 2026-09-25
- 수행자: 구축자(운영 전환 1-7 사용자 입력 반영 흐름 검증용 예시)
- 이전 실험: 없음

## 목적

VDA 5050 팩트시트(factsheet) JSON 스키마가 2.1.0 에서 3.0.0 으로 바뀌면서 로봇 능력·적재 제약을 기술하는 필드가 어떻게 달라졌는지 기계적으로 비교한다.

## 방법

- 대상: VDA5050/VDA5050 공식 GitHub 저장소의 `json_schemas/factsheet.schema` 두 판. 태그 2.1.0(https://raw.githubusercontent.com/VDA5050/VDA5050/2.1.0/json_schemas/factsheet.schema)과 태그 3.0.0(https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/json_schemas/factsheet.schema). 태그 2.0.0 에는 이 파일이 없었다(404).
- 도구: Python 3.11 표준 json 모듈. 2.1.0 파일에 끝 쉼표(trailing comma)가 있어 정규식으로 끝 쉼표를 지운 뒤 읽었다.
- 절차: 두 스키마의 `properties` 를 재귀로 따라가며(객체는 하위 properties, 배열은 items 의 properties) 필드 경로를 모았고, 경로 집합의 차이를 셌다.

## 결과 요약

- 최상위 필드: 2.1.0 은 12개, 3.0.0 도 12개다. `agvGeometry`·`vehicleConfig` 가 빠지고 `mobileRobotGeometry`·`mobileRobotConfiguration` 이 들어왔다.
- 필드 경로 수: 2.1.0 132개, 3.0.0 144개. 경로 문자열 기준으로 3.0.0 에만 있는 경로 104개, 2.1.0 에만 있는 경로 92개다(대부분 이름 변경: `agv*` → `mobileRobot*`, `max*`/`*Max` → `maximum*`, `maxArrayLens` → `maximumArrayLengths`).
- 이름 변경이 아닌 새 필드(경로 비교로 확인): `protocolFeatures.mobileRobotActions[].actionResult`·`cancelAllowed`·`pauseAllowed`, `typeSpecification.supportedZones`, `mobileRobotConfiguration.batteryCharging`(최저·최고 희망 충전량, 임계 저충전량, 최소 충전 시간), `protocolLimits.maximumArrayLengths.state.zoneActionStates`·`zoneSet.zones`.
- 적재 제약은 두 판 모두 `loadSpecification.loadSets[]` 에 있다. 3.0.0 필드: 적재 유형(loadType), 적재 치수(loadDimensions), 최대 중량(maximumWeight), 적재 취급 높이·깊이·기울기 최소·최대, 적재 시 최대 속도·가감속, 적재·하역 시간(pickTime·dropTime), 기준 경계 상자(boundingBoxReference).

## 한계

- 필드 경로의 문자열 비교이므로 이름만 바뀐 필드와 의미가 바뀐 필드를 구분하지 않았다. 설명(description) 문장 비교는 하지 않았다.
- 2.0.0 스키마 파일이 태그에 없어 질문의 "2.0 대비"는 2.1.0 대비로 대신했다.
- 3.0.0 경로 가운데 `mobileRobotConfiguration.batteryCharging ` 은 원 스키마의 키 이름 끝에 공백이 있다(원문 그대로).

## 데이터 파일

- field-diff.txt: 비교 스크립트 출력 전체(최상위 필드, 추가·삭제 경로 목록, 적재 관련 경로 목록)
