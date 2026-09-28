# spot: platform research execution contract v1

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
    "기존 plan_validation이 장비·관측·경로·에너지 조건을 재검증함",
    "Spot 순찰은 제조사 GraphNav 호출이 아니라 프로젝트 연구 제어기임"
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

