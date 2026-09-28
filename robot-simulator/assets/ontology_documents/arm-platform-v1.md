# arm: platform research execution contract v1

프로젝트 작성 기술문서. 기존 구현을 설명하기 위해 사람이 검토 가능한 형태로 명시적으로 작성한 계약이며, 카탈로그를 자동 추출한 결과나 제조사 매뉴얼이 아니다. 제조사 근거가 없는 연구 모델의 실물 성능을 주장하지 않는다.

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

