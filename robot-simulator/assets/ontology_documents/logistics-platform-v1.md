# logistics: platform research execution contract v1

프로젝트 작성 기술문서. 기존 구현을 설명하기 위해 사람이 검토 가능한 형태로 명시적으로 작성한 계약이며, 카탈로그를 자동 추출한 결과나 제조사 매뉴얼이 아니다. 제조사 근거가 없는 연구 모델의 실물 성능을 주장하지 않는다.

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

