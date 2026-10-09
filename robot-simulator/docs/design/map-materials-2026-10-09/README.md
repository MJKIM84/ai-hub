# 3D 지도 재질 이미지 적용 — 2026-10-09

## 범위와 결과

기존 물류 지도의 벽·바닥·승강기·계단·사람을 구분할 수 있도록 이미지 5종을 기획하고, 내장 `image_gen`으로 생성해 실제 Three.js 장면에 적용했다. 현재 로컬 앱은 <http://127.0.0.1:5187/>이다. 실시간 관제 → 3D 물리에서 확인하고, 상단 **재질** 버튼으로 단색 표현과 비교할 수 있다. 전체 화면과 객체 선택·카메라 추적을 그대로 사용할 수 있다.

이 작업은 시각 재질 적용이다. 물리 형상, 위치, 마찰계수, 충돌체, 로봇 제어, 보행 경로와 안전거리 설정을 변경하지 않았다. 실제 건물 재질을 측정한 데이터나 실물 검증을 뜻하지 않는다. 라이브 사이트에는 배포하지 않았다.

## 이미지 기획과 저장 위치

로봇과 경로 표시를 가리지 않도록 밝고 낮은 대비의 산업 시설 재질을 사용했다. 계단은 어두운 미끄럼 방지 무늬, 사람은 청록색 작업복으로 구분한다. 사람 이미지는 입간판이나 배경 그림이 아니라 기존 사람 모델에 입히는 옷감이다.

| 대상 | 생성 이미지 | 적용 대상 |
|---|---|---|
| 바닥 | `floor-epoxy` | 기존 층 바닥의 밝은 에폭시 표면 |
| 벽 | `wall-panel` | 벽·기둥의 도장 패널 |
| 승강기 | `elevator-steel` | 승강기 구조·문 및 문턱의 브러시 금속 |
| 계단 | `stair-grip` | 계단·경사로·승강기 플랫폼의 금속 논슬립 표면 |
| 사람 | `worker-jacket` | 기존 관절형 사람 모델의 상의·소매 |

- 생성 도구: 내장 `image_gen`. 별도 API 또는 대체 모형을 사용하지 않았다.
- 최종 프롬프트 전체와 생성 원본 파일명: [prompts.json](prompts.json).
- 생성 원본: [originals/](originals/)의 동일 이름 PNG 5개.
- 실제 앱이 읽는 자산: [web/public/materials/industrial-v1/](../../../web/public/materials/industrial-v1/)의 동일 이름 JPEG 5개. 웹용 1024px JPEG로 인코딩했으며 총 1,498,308바이트다.
- 파일 해시와 크기: [validation.json](validation.json).

## 구현

- [MapMaterials.ts](../../../web/src/MapMaterials.ts): 기존 객체 종류를 기준으로 재질을 선택하고 실제 미터 단위에 맞춰 UV를 부여한다. 바닥 조각은 공통 좌표를 사용하며, 움직이는 시설은 로컬 표면 좌표를 사용한다. 정점 위치와 법선은 수정하지 않는다.
- [PhysicsView.tsx](../../../web/src/PhysicsView.tsx): 기존 물리 장면의 메시 위에 이미지를 표시한다. 물리 진단 중에는 기본 색으로 전환하며, 이미지 로딩 실패 시 기존 단색을 유지하고 재시도 버튼을 제공한다.
- [HumanVisual.ts](../../../web/src/HumanVisual.ts): 상의 재질만 바꾸고 기존 관절·보행 애니메이션을 유지한다.
- 구역 표시, 물품과 로봇, 종류를 식별할 수 없는 객체는 기존 표현을 유지한다. 2D 지도 데이터에는 장식 이미지를 넣지 않는다.

## 확인한 화면

2026-10-09 내장 브라우저에서 기존 **물류 시설 · 혼합 로봇 실험**을 열고 재질 표시, 전체 화면, 객체 선택을 직접 확인했다. 실행을 시작하거나 이 지도의 구성을 변경하지 않았다. 재개 후 최종 코드에서 다시 촬영한 비교는 같은 카메라 위치다.

| 화면 | 근거 |
|---|---|
| 같은 지도·시점의 단색 표현 | [plain-comparison.png](plain-comparison.png) |
| 벽·바닥·승강기·계단 적용 | [after-overview.png](after-overview.png) |
| 사람 모델의 작업복 | [worker.png](worker.png) |
| 승강기 이동 중 두 층과 로봇 추적 | [elevator-moving.png](elevator-moving.png) |
| 도착층 전환·하차 후 추적 | [elevator-arrival.png](elevator-arrival.png) |

`before.png`는 최초 적용 전 기록이다. `first-run-free-camera.png`는 첫 샘플 실행에서 추적이 꺼진 상태의 기록이며 카메라 추적 성공 근거로 사용하지 않는다. 최종 재질 적용 화면에서 브라우저 오류 로그는 0개였다.

## 검증 결과

현재 변경은 웹 재질 처리에 한정되므로 전체 플랫폼 회귀 검사를 반복하지 않았다. 실행기·물리 모델의 광범위한 정확성을 주장하지 않는다.

| 확인 | 결과·근거 |
|---|---|
| 표면 분류·미터 UV·정점/법선 보존·보행 자세 보존 | 표적 검사 통과, [material-checks.log](material-checks.log) |
| 로딩 실패 시 단색 유지·실패한 자산만 재시도·해제 후 콜백 처리 | 같은 표적 검사 통과. 이 항목은 모의 로더를 사용하는 단위 검사이며 실제 통신 장애 실험은 아니다. |
| TypeScript 및 웹 빌드 | `npm run build` 통과, [web-build.log](web-build.log) |
| 2D/3D 전환 | 실행 ID·시각·물리 형상·사람·물품·작업 데이터 동일, [validation.json](validation.json) |
| 기존 60초 승강기·이동 보행자 샘플 | 아래 두 실행을 각각 보존. 모두 시뮬레이션 51.302초에 작업 1/1 완료, 최소 분리거리 0.545408m, 목표 0.5m, 충돌 0, 근접 사건 0. |

샘플 입력은 [sample-project.json](sample-project.json)이다. 물리·보행자·시드 조건을 변경하지 않았으며 **51.302초는 실제 경과 시간이 아니라 시뮬레이션 시간**이다.

1. 실행 `8f3acb4f5c974818b5f0a6301ec4b087`: [sample-result.json](sample-result.json). 작업 완료와 움직이는 사람을 확인했다. 카메라가 자유 시점이 된 기록은 별도로 남겼다.
2. 실행 `05feeb0fc9274352947430c274b83ebb`: [sample-camera-result.json](sample-camera-result.json). 초기화 후 전체 화면에서 다시 로봇을 선택해 따라가기를 켰다. 승강기 상승 중 1·2층과 AMR을 함께 표시하고, 2층 하차 후에도 따라가기가 유지되는 것을 직접 확인했다.

두 결과는 같은 조건의 재실행이며 서로 다른 환경의 성공 사례로 합산하지 않는다. 이 기록은 해당 샘플에서 재질을 켠 상태로 기존 이동·추적이 유지됨을 확인한 것이다.

## 재확인

실행 중인 로컬 앱에서 **실시간 관제 → 3D 물리 → 재질**을 사용한다. 샘플은 **작업 기록 → 엘리베이터·보행자 회피 · 60초 → 실행 준비**에서 불러올 수 있다. 샘플을 실행할 때는 AMR 선택 후 따라가기를 켠다.

검사와 빌드는 `robot-simulator/web`에서 실행한다.

```sh
node scripts/check-map-materials.mjs
npm run build
```

로컬 서버를 다시 띄울 때는 `robot-simulator`에서 기존 Python 환경을 활성화한 뒤 별도 데이터 디렉터리를 사용한다.

```sh
PYTHONPATH=src python - <<'PY'
from pathlib import Path
import uvicorn
from robot_platform.api import create_app
uvicorn.run(create_app(Path('/tmp/robot-map-materials-2026-10-09'), initial_template='warehouse'), host='127.0.0.1', port=8004, access_log=False)
PY
```

다른 터미널의 `robot-simulator/web`에서:

```sh
ROBOT_API_URL=http://127.0.0.1:8004 npm run dev -- --port 5187
```

이 문서와 화면·생성 원본·샘플 설정·결과는 프로젝트에 보존한다. 서버의 임시 데이터 디렉터리는 산출물 보관 위치로 사용하지 않는다.
