# 주행 속도와 화면 연속성 검증 — 2026-10-09

대상: `feat/map-material-images`, 기준 커밋 `0f28b47` 이후 이 문서와 함께 커밋된 수정. 로컬 macOS 26.5.1 arm64, Python 3.14, MuJoCo, 내장 브라우저. 실물 로봇과 배포 사이트는 변경하지 않았다. 이전 로봇 외장과 캐스터 디자인은 유지했다.

## 바뀐 동작

- Spot 관절 제어기의 평지 연구 상한을 0.4 → 1.0m/s로 변경했다. 걸음 주기·보폭 피드백·가감속과 목적지 감속을 조정했다. 몸체 좌표를 쓰거나 접촉을 생략하지 않는다.
- 모델 조회에서 매번 전체 카탈로그를 복사하던 처리를 제거했다. 경로 탐색의 점유 검사 캐시는 단일 탐색 안에서만 유지한다. 물리 모델의 관절 주소·형상 소유자 조회를 재사용한다.
- 실행 스레드가 상태 잠금을 길게 점유하지 않도록 작은 계산 묶음으로 양보한다. 물리 시간 간격 0.002초와 제어·관측 설정은 유지한다.
- 3D는 마지막으로 수신한 두 물리 자세를 화면 프레임 사이에서 연결한다. 로봇 외장·캐스터·사람·추적 카메라가 같은 화면 자세를 따른다. 앞으로의 움직임을 예측하지 않는다. 보간은 최대 120ms이며 정지·연결 단절·초기화·물리 진단에서는 수신 위치를 즉시 표시한다. 측정·충돌 판정은 원래 물리 상태를 사용한다.
- 상단의 **실제 n×**는 실제 경과 시간 대비 시뮬레이션 진행률이다. 선택 객체의 **현재 이동 속도 · 물리**는 실제 m/s이다.
- 새 일반 예제와 새 로봇은 모델별 연구 속도를 사용한다. 기존 저장 구성은 자동 변경하지 않는다. **정책과 물리 설정 → 모델 기준 주행 속도 적용 → 적용**으로 초안을 반영할 수 있다. 실행에 영향을 주는 변경은 기존 승인 검증을 따른다.

## 최종 결과

최종 물리 측정은 [after.json](after.json), 설정은 [baseline-project.json](baseline-project.json)과 [crossing-project.json](crossing-project.json), 요약은 [measurements.log](measurements.log)에 저장했다. 아래 시간을 서로 다른 검사끼리 합산하지 않는다.

| 확인 내용 | 조건과 결과 |
|---|---|
| 계산 처리량 전후 | 동일 저장된 창고 구성, 로봇 8대·사람 1명, seed 42, 1000 물리 단계=시뮬레이션 2초. 이전 실제 계산 7.267초 → 최종 1.300초. 단일 로컬 비교 약 5.6배. 프레임 속도나 모든 환경의 성능을 뜻하지 않는다. |
| 실제 1배속 화면 | 내장 브라우저, 로봇 8대. 실제 31.982초 동안 화면 시뮬레이션 21.562→53.524초, 진행률 약 1.00배. `browser-timing.json` 및 `browser-final-running.png`. |
| Spot 속도 | 평탄한 열린 바닥, 직진 요청 0.4 / 0.8 / 1.0m/s. 8–14 시뮬레이션 초 평균 실제 전진 속도 0.398 / 0.781 / 0.991m/s. 모든 검사에서 upright >0.996, 이후 정지 확인. |
| Spot 경로 | (3,10)→(10,10), 15.402 시뮬레이션 초에 종료. (3,10)→(9,14) 및 최종 방향 1.57rad, 24.402초 종료. 관측 도착·방향·정지 기준 유지. 충돌·근접·전도 0. |
| 이동 보행자 | Spot 1.0m/s 상한, 사람 0.6m/s로 x=7에서 교차. 1.4초 대기 후 재개, 23.202초 작업 완료. 목표 표면 간격 0.5m, 실제 최소 0.615m. 충돌·근접·전도 0. 사람의 실제 위치 변화도 저장. |
| 다중 로봇 도착 | 창고 예제의 Spot 01은 로봇 간 경로 조정 후 36.2초에 완료. 마지막 경유점 소비 허용치가 실제 도착 허용치보다 커서 반복 접근하던 결함을 수정했다. 기존 0.06m 도착 기준을 유지했다. |
| 브라우저 정지/추적 | 최종 코드 실행 e375195c에서 Spot 선택·따라가기·1배속·일시정지 직접 조작. 최종 Spot 작업 완료 표시 확인. 보간 상태와 매 프레임 갱신을 DOM 진단 속성으로 확인. 정지 시 보간 해제·시간 고정 확인. 렌더 횟수를 디스플레이 FPS로 주장하지 않는다. |

48개 표적 검사 통과: [tests.log](tests.log). 화면 보간·외장 검사 통과, TypeScript/Vite 빌드 통과: [web-build.log](web-build.log). Starlette/httpx 사용에 관한 기존 의존성 경고 1개가 있다.

## 재확인

`robot-simulator`에서 가상 환경 Python을 사용한다.

```sh
PYTHONPATH=src python -m pytest -q tests/test_motion_performance.py tests/test_api_speed.py tests/test_guided_observation_safety.py
PYTHONPATH=src python scripts/verify_motion_performance.py
```

`robot-simulator/web`에서:

```sh
node scripts/check-scene-motion.mjs
node scripts/check-robot-design.mjs
npm run build
```

이번 로컬 화면은 http://127.0.0.1:5188/ (API 8005)이다. **정책과 물리 설정**에서 모델 속도를 초안에 적용하고, **실시간 관제 → 3D 물리 → 로봇 선택 → 따라가기 → 시작**으로 확인한다. 이전 승인된 시나리오의 저속 설정은 자동으로 바뀌지 않는다. 좁은 통로·사람·도킹·정확한 도착에는 기존 제한이 적용된다.

## 실패 기록과 범위

- 제조사 Spot 최대 속도 1.6m/s는 [Boston Dynamics 공식 문서](https://dev.bostondynamics.com/docs/concepts/about_spot)에 명시돼 있다. 현재 연구 제어기는 제조사 펌웨어가 아니다. 1.6m/s 후보에서 전도가 발생해 배포 코드의 상한을 1.0m/s로 정했다. `gait-candidates.json`의 실패를 보존했다. 새 보행 제어기의 계단·경사·적재 상태를 이 평지 검사로 검증했다고 표시하지 않는다.
- 전체 창고 업무 완료를 주장하지 않는다. 최종 37초 표적 관찰에서 AMR/AGV 작업은 진행 중, 물류 운반 모델의 기존 순찰 과제는 능력 불일치로 대기 중이다. `after.json`의 모든 작업 상태를 보존했다. 이번 검증은 Spot 속도·주행과 계산/표시 지연에 한정한다.
- `spot-route-first.json`, `spot-route-verified.json`, `spot-stop.json`, `before-peer-arrival-fix.json`, `crossing-and-short-turn.json`, `warehouse-speed-run-*.json` 등은 수정 도중 결과다. 최종 수치로 인용하지 않는다. 최종 결과는 **after.json**이다.
- 첫 브라우저 실행의 `browser-running.png`, `browser-paused-state.json`은 목적지 판정 수정 전 기록이다. 최종 화면은 **browser-final-running.png**, **browser-final-paused.png**이다.
- 충전 정책·기존 실패 검사의 기준을 변경하지 않았다. 고속 주행과 시각 보간을 실물 안전성이나 전체 플랫폼 완료로 일반화하지 않는다.
