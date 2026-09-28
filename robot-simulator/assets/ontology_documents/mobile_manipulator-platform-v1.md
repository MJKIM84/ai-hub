# mobile_manipulator: platform research execution contract v1

프로젝트 작성 기술문서. 기존 구현을 설명하기 위해 사람이 검토 가능한 형태로 명시적으로 작성한 계약이며, 카탈로그를 자동 추출한 결과나 제조사 매뉴얼이 아니다. 제조사 근거가 없는 연구 모델의 실물 성능을 주장하지 않는다.

## 지정 지점 순찰

```capability
{
  "key": "patrol",
  "name": "지정 지점 순찰",
  "meaning": "기존 경로 계획과 관측 기반 이동 제어로 승인된 목적지에 도달하고 체류한다.",
  "parameters": [
    {
      "name": "timeout",
      "type": "number",
      "unit": "s",
      "minimum": 0.001,
      "maximum": 86400,
      "required": false
    },
    {
      "name": "dwell",
      "type": "number",
      "unit": "s",
      "minimum": 0,
      "maximum": 86400,
      "required": false
    }
  ],
  "inputs": [
    "지도상의 목적지",
    "로봇 초기 위치",
    "배터리"
  ],
  "outputs": [
    "도착 및 작업 상태",
    "실제 경로와 사건"
  ],
  "preconditions": [
    "정적 경로와 배터리 예산이 유효함",
    "최종 계획 승인"
  ],
  "constraints": [
    "제조사 제품이 아닌 파라미터 기반 연구 로봇"
  ],
  "dependencies": [
    "navigate"
  ],
  "sdk_mapping": null,
  "failures": [
    "경로 불가",
    "에너지 부족",
    "관측 만료",
    "작업 시간 초과"
  ],
  "recovery": [
    "명시적 재계획 또는 오류 원인 해소 후 복구"
  ]
}
```

## 협업 물품 운반

```capability
{
  "key": "transport",
  "name": "협업 물품 운반",
  "meaning": "적재 지지면의 물품을 운반하여 다른 조작 로봇에게 인계한다.",
  "parameters": [],
  "inputs": [
    "물품",
    "화물 적재 장비",
    "수신 로봇",
    "작업 공간",
    "인계 지점"
  ],
  "outputs": [
    "물품 소유권 전이",
    "협업 작업 결과"
  ],
  "preconditions": [
    "실제 cooperation 설정",
    "cargo_tray 지지면과 적재 중량 조건",
    "서로 다른 운반·인수 로봇"
  ],
  "dependencies": [
    "navigate",
    "manipulate"
  ],
  "constraints": [
    "운반 로봇 혼자서 자동 상하차하지 않음",
    "물품 관측·접촉·소유권 검증을 통과해야 완료"
  ],
  "sdk_mapping": null,
  "failures": [
    "인계 조건 불충족",
    "파지 실패",
    "자원 점유",
    "관측 만료"
  ],
  "recovery": [
    "기존 협업 상태기계의 제한된 재시도",
    "취소 시 자원 정리"
  ]
}
```

## 협업 물품 파지·놓기

```capability
{
  "key": "manipulate",
  "name": "협업 물품 파지·놓기",
  "meaning": "기존 협업 실행기의 인수 또는 상차 역할로 관절 팔과 그리퍼를 제어한다.",
  "parameters": [],
  "inputs": [
    "물품 관측",
    "인계 작업 공간",
    "그리퍼 장비"
  ],
  "outputs": [
    "파지 상태",
    "물품 인계 결과"
  ],
  "preconditions": [
    "실제 cooperation 역할 지정",
    "작업 반경과 중량 만족",
    "필요한 그리퍼 장비"
  ],
  "dependencies": [
    "item_observation"
  ],
  "constraints": [
    "기본 연구 모델의 조작 최대 중량 3 kg; 실제 기구학·현재 장비로 추가 제한",
    "이동형 팔도 파지 때 차체 정지 필요"
  ],
  "sdk_mapping": null,
  "failures": [
    "작업 반경 초과",
    "파지 실패",
    "물품 미관측"
  ],
  "recovery": [
    "상태기계의 제한된 재시도",
    "실패 시 자원 반환"
  ]
}
```

