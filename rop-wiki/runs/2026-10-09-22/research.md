# 리서치 브리프 2026-10-09-22

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-22 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 표현 |
| 대분류 | B. 로봇 온톨로지 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 2 · 답한 질문 q2-04

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-02·q2-03 조사 중(실행 2026-09-25-57 부분 답), q2-04 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 6건 중 오래된 순)
- q2-02 남은 부분: 기계가독 스키마·설정 파일 안에서도 자유 텍스트로 남는 항목과 단위 표기 방식이 정리되지 않음, 형태별 추출 난이도 측정 자료 없음
- q2-03 남은 부분: AMR 제조사 공개 매뉴얼 샘플과 포털 매뉴얼 문서의 이용 조건 미확인
- q2-04 미조사: 문서에 없지만 실행에 필요한 정보(암묵지)와 보완 경로
- 완료 조건: 문서 유형 매트릭스 64칸 가운데 9칸만 채움, 5절 '문서에 없는 정보' 비어 있음
- 완료 조건: 공개 문서 샘플 목록에 AMR 샘플 없음

## 조사 질문

1. 로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]
2. q2-02 기능 정보는 어떤 형태(문장, 표, 그림·다이어그램, 코드 예제, 파라미터 표)로 존재하며 형태별 추출 난이도는 어떠한가?
3. q2-03 공개적으로 접근할 수 있는 대표 문서 샘플(AMR, 협동로봇, 로봇팔 등)은 무엇이고 이용 조건은 어떠한가?
4. q2-04 문서에 없지만 실행에 필요한 정보(암묵지)는 무엇이고 어디서 보완하는가(제조사 문의, 시험, 커뮤니티)?
5. 기계가독 스키마(VDA 5050 팩트시트, MassRobotics 스키마)와 플릿 어댑터 설정 파일 안에서 단위·값 형식과 자유 텍스트 항목은 어떻게 나뉘는가? (단계 2 페이지 3절 q2-02 겨냥)
6. 통합·시운전 때 사람이 채워야 하는 설정·코드 항목은 무엇이며 55. 현장 조사·설치·시운전과 어떻게 이어지는가? (단계 2 페이지 3절 q2-04, 문서 유형 매트릭스 5절 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 팩트시트 JSON 스키마(main, 3.0.0)는 수치 필드마다 단위(maximumLoadMass 는 kg, 속도는 m/s, 각속도는 rad/s)와 최솟값 제약을 스키마 속성으로 달아, 파라미터 표 정보를 단위가 명시된 기계가독 형식으로 담는다. | ref-228 | 아니오 | medium | 2026-10-09 | — | — |
| f2 | [사실] | 같은 팩트시트 스키마도 시리즈 설명(seriesDescription), 동작 설명(actionDescription), 동작 결과(actionResult), 바퀴 제약(constraints)을 자유 텍스트로 두고 기구학 유형·로봇 분류를 확장 가능한 열거값으로 두어, 능력 관련 정보 일부가 기계가독 스키마 안에서도 문장으로 남는다. | ref-228 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [추정] | 팩트시트의 동작 결과·제약 같은 자유 텍스트 필드와 확장 열거값은 제조사마다 다른 문장·값을 담을 수 있으므로, 기계가독 스키마를 받아도 동작의 완료 의미와 제약은 문장 해석을 거쳐야 능력 모델로 옮길 수 있을 것으로 보인다. | ref-228 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [사실] | MassRobotics AMR 상호운용 표준 스키마의 식별 보고는 화물 최대 중량(cargoMaxWeight)을 설명에는 kg 단위로 적되 문자열형으로 정의하고, 화물 설명(cargoType)은 자유 문자열로, 제품 문서(productDocumentation)는 문서 내용이 아니라 URI 링크로 둔다. | ref-230 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | Open-RMF 플릿 어댑터 템플릿의 config.yaml 은 수행 가능한 작업 유형(task_capabilities 의 loop·delivery 참거짓값), 동작 목록(actions), 배터리 전압·용량·충전 전류, 질량, 외형 반경을 YAML 값으로 선언하되 단위는 V·Ahr·A·kg·m 같은 줄 끝 주석으로만 적는다. | ref-105 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [추정] | 확인한 기계가독 형식 안에서도 단위가 스키마 속성으로 명시된 값(VDA 5050 팩트시트), 단위가 주석에만 있는 설정값(Open-RMF config.yaml), 수치를 문자열로 담은 값(MassRobotics 화물 최대 중량), 자유 텍스트(동작 결과·제약·화물 설명) 순으로 정규화에 드는 추가 해석이 늘 것으로 보이나, 형태별 추출 난이도를 측정한 자료는 여전히 확인되지 않았다. | ref-228, ref-105, ref-230, ref-513 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [사실] | OmniDocBench 공식 저장소 README 는 PDF 문서 파싱을 텍스트 문단·표·수식·읽기 순서로 나눠 평가하며 문서 유형으로 논문·재무 보고서·신문·교과서·손글씨 노트 등을 들고 매뉴얼은 명시하지 않는다. | ref-513 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f8 | [추정] | Boston Dynamics Spot SDK 는 GitHub 에 공개되어 있으나 사용·복제·배포가 Boston Dynamics SDK 라이선스(20191101-BDSDK-SL) 조건을 따른다고 저장소 README 가 적는다. | ref-505 | 아니오 | medium | 2026-10-09 | — | 원문 미열람, 벤더 주장 |
| f9 | [추정] | Kinova Kortex API 저장소는 BSD 3-Clause 라이선스로 공개되어 있다고 저장소가 표기한다. | ref-506 | 아니오 | medium | 2026-10-09 | — | 원문 미열람, 벤더 주장 |
| f10 | [추정] | 국내 협동로봇 제조사의 공개 저장소(두산 doosan-robot2: Apache 2.0·BSD 3-Clause, 레인보우 rbpodo: Apache 2.0)는 코드에 개방 라이선스를 달지만, 두산로보틱스 로봇랩 포털에서 내려받는 매뉴얼 문서 자체의 이용 조건은 확인되지 않았다. | ref-507, ref-508, ref-511 | 아니오 | low | 2026-10-09 | — | 원문 미열람, 벤더 주장 |
| f11 | [추정] | 이번 재실행 입력에서 AMR 쪽 공개 문서는 VDA 5050 팩트시트·MassRobotics 표준 스키마뿐이고, MassRobotics 식별 보고는 제품 문서 링크 필드만 두어 AMR 제조사 매뉴얼 샘플을 대신하지 못하는 것으로 보인다(부재 확정 아님). | ref-228, ref-230 | 아니오 | low | 2026-10-09 | — | — |
| f12 | [사실] | Open-RMF PerformAction 튜토리얼에서 사용자 정의 동작은 config.yaml 의 actions 로 이름만 선언되고, 그 동작을 로봇 API 호출로 옮기는 start_activity 는 로봇과 사용 사례에 특화된 것으로서 통합자가 RobotClientAPI 에 직접 구현해야 한다. | ref-040 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f13 | [사실] | 같은 튜토리얼에서 RMF 는 사용자 정의 동작 동안 로봇 제어권을 내려놓고, 어댑터의 갱신 루프가 is_command_completed 로 로봇 API 의 완료를 확인한 뒤 execution.finished() 를 호출해야 완료로 처리한다. | ref-040 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f14 | [사실] | Open-RMF 플릿 어댑터 템플릿의 config.yaml 은 층별 RMF 좌표와 로봇 좌표 대응점 네 쌍(reference_coordinates), 로봇별 충전기 이름, 운용 하한·충전 목표 배터리 수준(recharge_threshold·recharge_soc), 질량·관성 모멘트·마찰 계수, 대기·도구 소비 전력, 제조사 관제 접속 주소·계정을 채우게 한다. | ref-105 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f15 | [추정] | 좌표 대응점·충전기 배정·배터리 하한 같은 현장 설정과 동작–로봇 API 매핑·완료 확인 코드는 현장과 통합 방식에 따라 정해지므로 제조사 문서에서 가져올 수 없고, 통합자가 55. 현장 조사·설치·시운전 단계의 측정·시험과 어댑터 구현으로 보완해야 하는 암묵지에 해당하는 것으로 보인다. | ref-105, ref-040 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | VDA 5050 팩트시트 스키마는 팩트시트를 특정 이동로봇 유형 시리즈의 기본 정보로 규정하고, 그 쓰임을 유형 비교, 시스템 계획·규모 산정·시뮬레이션, VDA 5050 플릿 관제 통합으로 든다. | ref-228 | 아니오 | medium | 2026-10-09 | — | — |
| f17 | [사실] | MassRobotics 스키마의 상태 보고는 배터리 비율, 남은 가동 시간, 남은 적재 여유 비율, 오류 코드(자유 문자열 배열)를 실행 중 값으로 보고하게 한다. | ref-230 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f18 | [사실] | Naqvi 외(2025)는 제조사가 광고한 능력과 운용 중 관측된 능력을 온톨로지로 구분해 통합하는 방법을 제시했다. | ref-041 | 아니오 | medium | 2025-10-02 | — | 원문 미열람 |
| f19 | [추정] | 팩트시트가 유형 시리즈 수준의 선언이고(f16) 남은 가동 시간·적재 여유·오류 코드 같은 값은 상태 보고로만 드러나므로(f17), 개체별 실제 성능 저하나 오류 코드의 뜻 같은 암묵지는 문서보다 운용 중 상태 보고와 관측 능력 기록(f18)으로 보완하는 것으로 보이며, 제조사 문의·커뮤니티 경로는 이번에 확인하지 못했다. | ref-228, ref-230, ref-041 | 아니오 | low | 2026-10-09 | 예외·성과 | — |

### 근거 발췌

- **f1**: maximumLoadMass: type number, "unit": "kg", minimum 0; maximumSpeed: unit m/s; maximumAngularSpeed: unit rad/s (발행일 미확인, 확인일 기준)
- **f2**: actionResult "Free text: description of the result"; wheel constraints "Free text: can be used by the manufacturer to define constraints"; mobileRobotClass "Extensible enum: FORKLIFT, CONVEYOR, TUGGER, CARRIER" (발행일 미확인, 확인일 기준)
- **f3**: f2 의 자유 텍스트 필드(actionResult·constraints·actionDescription)와 확장 열거값에서 도출한 이 위키의 추론이며 측정 근거는 없다 (발행일 미확인, 확인일 기준)
- **f4**: cargoMaxWeight: "Max weight of cargo in kg", type string; cargoType: type string; productDocumentation: "Link to product documenation", format uri (발행일 미확인, 확인일 기준)
- **f5**: task_capabilities: loop: True, delivery: True; actions: ["some_action_here"]; battery_system: voltage: 12.0 # V, capacity: 24.0 # Ahr; footprint: 0.3 # radius in m (발행일 미확인, 확인일 기준)
- **f6**: f1·f2·f4·f5 의 값 형식을 대응시킨 이 위키의 추론. 범용 파싱 벤치마크는 매뉴얼을 문서 유형에 두지 않아 측정 근거가 없다 (발행일 미확인, 확인일 기준)
- **f7**: 요소 형태별(문단·표·수식·읽기 순서) 평가, 문서 유형 목록에 매뉴얼 없음 (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-57)
- **f8**: 벤더 주장: 저장소 README 의 라이선스 표기(20191101-BDSDK-SL) (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-57)
- **f9**: 벤더 주장: kortex 저장소 라이선스 표기 BSD 3-Clause (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-57)
- **f10**: 벤더 주장: 저장소 라이선스 표기(Apache 2.0·BSD 3-Clause / Apache 2.0), 포털 매뉴얼 이용 약관 미확인 (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-57)
- **f11**: 표준 스키마는 공식 저장소에 공개, productDocumentation 은 URI 링크 필드. 이번 재실행은 새 검색을 하지 않아 AMR 매뉴얼 샘플을 찾지 않았다 (발행일 미확인, 확인일 기준)
- **f12**: start_activity docstring: "This is specific to the robot and the use case"; fleet manager 가 동작을 모르면 execution.finished() 로 활동을 끝낸다 (발행일 미확인, 확인일 기준)
- **f13**: RMF would relinquish control of the robot until it is signalled that the robot has completed the custom action; update 루프의 is_command_completed → execution.finished() (발행일 미확인, 확인일 기준)
- **f14**: reference_coordinates: L1: rmf/robot 4점; charger: "tinyRobot1_charger"; recharge_threshold: 0.10; moment_of_inertia, friction_coefficient; fleet_manager: prefix, user, password (발행일 미확인, 확인일 기준)
- **f15**: f12·f13·f14 의 설정·코드 항목에서 도출한 이 위키의 추론이며, 제조사 문의·커뮤니티 경로를 다룬 출처는 이번에 없다 (발행일 미확인, 확인일 기준)
- **f16**: "The factsheet provides basic information about a specific mobile robot type series" — planning, dimensioning and simulation, integration into fleet control (발행일 미확인, 확인일 기준)
- **f17**: statusReport: batteryPercentage, remainingRunTime, loadPercentageStillAvailable, errorCodes(items type string) (발행일 미확인, 확인일 기준)
- **f18**: advertised capabilities 와 operational capabilities 를 온톨로지로 구분·통합 (재인용: 2026-09-25-15)
- **f19**: f16·f17·f18 을 대응시킨 이 위키의 추론 (발행일 미확인, 확인일 기준)

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | 논문 | medium | 2026-10-09 | https://www.nature.com/articles/s41598-025-16649-3 | 예 |
| ref-505 | Boston Dynamics (boston-dynamics/spot-sdk GitHub) | spot-sdk — README | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://github.com/boston-dynamics/spot-sdk | 예 |
| ref-506 | Kinova (Kinovarobotics/kortex GitHub) | kortex — readme | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://github.com/Kinovarobotics/kortex | 예 |
| ref-507 | Doosan Robotics (doosan-robotics/doosan-robot2 GitHub) | doosan-robot2 — README (humble) | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://github.com/doosan-robotics/doosan-robot2 | 예 |
| ref-508 | Rainbow Robotics (RainbowRobotics/rbpodo GitHub) | rbpodo — README | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://github.com/RainbowRobotics/rbpodo | 예 |
| ref-511 | 두산로보틱스 | 매뉴얼 : Doosan Robotics Training & Service | 미확인 | 벤더 문서 | low | 2026-10-09 | https://robotlab.doosanrobotics.com/ko/board/Resources/Manual | 예 |
| ref-513 | OpenDataLab (opendatalab/OmniDocBench GitHub) | OmniDocBench — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/opendatalab/OmniDocBench | 예 |

### 출처 요약

- **ref-040**: Open-RMF 플릿 어댑터에서 사용자 정의 동작을 config.yaml 로 선언하고 로봇 API 호출과 완료 확인을 구현하는 튜토리얼.
- **ref-105**: Open-RMF 플릿 어댑터 템플릿 설정 파일. 작업 능력·동작·배터리·기계 특성·좌표 변환·관제 접속 정보를 선언한다.
- **ref-228**: VDA 5050 main(3.0.0) 팩트시트 JSON 스키마. 유형 명세·물리 파라미터·프로토콜 한계·지원 기능·기하·적재 명세를 단위와 함께 정의한다(입력 원문은 앞 37,286자 발췌).
- **ref-230**: MassRobotics AMR 상호운용 표준의 식별 보고·상태 보고 JSON 스키마.
- **ref-041**: 원문 미열람. 제조사 광고 능력과 운용 중 관측 능력을 온톨로지로 구분해 통합하는 방법을 제시한 논문.
- **ref-505**: 원문 미열람. Spot SDK 공식 저장소 README. 문서 구성과 SDK 라이선스를 안내한다(이번 재실행에서는 다시 열지 않음).
- **ref-506**: 원문 미열람. Kinova Kortex API 공식 저장소 README. API 문서·예제와 라이선스를 안내한다(이번 재실행에서는 다시 열지 않음).
- **ref-507**: 원문 미열람. 두산로보틱스 ROS2 패키지 저장소 README(이번 재실행에서는 다시 열지 않음).
- **ref-508**: 원문 미열람. 레인보우로보틱스 협동로봇 클라이언트 라이브러리 README(이번 재실행에서는 다시 열지 않음).
- **ref-511**: 원문 미열람. 두산로보틱스 로봇랩 포털의 매뉴얼 게시판.
- **ref-513**: 원문 미열람. 범용 PDF 문서 파싱 벤치마크 README(이번 재실행에서는 다시 열지 않음).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-2-document-types.md | 2, 3, 4, 5, 6, 8, 9 | q2-04 답: f12·f13·f14·f15·f16·f17·f18·f19 (신뢰도 low) / q2-02 부분 답: f1·f2·f3·f4·f5·f6·f7 / q2-03 부분 답: f8·f9·f10·f11 — 2절 q2-04 답함, q2-02·q2-03 조사 중 유지, 3절 q2-04 소제목 신설({#q2-04}, 통합 설정·어댑터 코드·상태 보고로 보완되는 정보), q2-02 에 기계가독 스키마 안의 단위 표기·자유 텍스트 구분 보강, q2-03 은 재인용 확인만, 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/tracks/manual-capability-ontology/document-type-matrix.md | 3, 5, 8 | 트랙 산출물 갱신: 사양서·데이터시트 행 파라미터 범위 칸에 단위가 스키마 속성으로 명시됨(f1), 동작 결과·제약 자유 텍스트(f2) 메모. 5절 '문서에 없는 정보'에 통합 설정(좌표 대응점·충전기 배정·배터리 하한)·동작–API 매핑·완료 확인 코드(f12~f15)와 운용 중 값(f16~f19)을 정보 항목별로 요약(보완 경로: 통합·시운전, 상태 보고, 운용 관측. 제조사 문의·커뮤니티는 미확인) |
| update | docs/categories/robot-ontology/robot-capability-and-task-representation.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f2, f16, f18, f19): 팩트시트가 유형 시리즈 수준 선언이고 동작 결과·제약이 자유 텍스트로 남아, 능력 모델은 문서 선언과 운용 관측을 함께 담아야 한다는 점 |
| update | docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f12, f14, f15): 플릿 어댑터 통합 때 사람이 채우는 현장 설정(층별 좌표 대응점·충전기 배정·배터리 하한)과 동작–로봇 API 매핑 코드가 제조사 문서 밖의 암묵지라는 점 |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 11 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - q2-02 부분 답: 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 정확도를 측정한 자료 미확인
    - q2-03 부분 답: AMR 제조사 공개 매뉴얼 샘플과 포털 매뉴얼 문서의 이용 약관 미확인(이번 재실행에서 새 검색 없음)
    - q2-04: 보완 경로 가운데 제조사 문의·커뮤니티는 근거 출처 없음
    - ref-228 원문 텍스트가 앞 37,286자 발췌라 적재 명세 뒷부분·구성 블록 미확인
    - ref-041·ref-505·ref-506·ref-507·ref-508·ref-511·ref-513 은 이번 재실행에서 다시 열지 않음
    - 모든 finding 교차 확인 없음
- 범위 경계 위반 의심:
    - 없음
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f10·f11·f16 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환 JSON 이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts 의 ref-040·ref-105·ref-228·ref-230, fetched_via inbox)와 기존 참고문헌 재인용만으로 같은 질문(q2-02·q2-03·q2-04)의 브리프를 다시 구성했다. 벤더 문서만 근거로 한 finding(f8·f9·f10)은 모두 태그 추정, vendor_claim true, evidence_excerpt 첫머리 '벤더 주장: '으로 냈고, 사실 태그는 표준·오픈소스 문서·논문 출처 finding 에만 두었다(새 f11·f16 은 표준 출처 근거). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1397~ref-1426 은 쓰지 않았다. 재사용 11건 가운데 4건은 inbox 원문, 7건은 원문 미열람 표시. 답한 질문: q2-04(통합 설정·어댑터 코드·상태 보고로 보완되는 정보, 신뢰도 low). q2-02·q2-03 은 부분 답. 후속 질문 2건. 온톨로지 변경 없음: 이번 근거(f2·f16·f18)는 초안 6절 '근거 문서의 단위와 버전' 질문과 기능의 능력 출처 구분 속성(광고 / 운용)과 겹쳐 새 개념·관계 근거가 되지 않는다. 용어 후보 없음: 트랙 glossary_targets 가운데 미등록 용어(로봇 능력 온톨로지, SPARQL, 온톨로지 학습)에 대한 이번 근거 없음. 현장 유형 사례 finding 없음(site_type 모두 null). 47. AI·학습·적응과 모델 운영 관련 finding(f6·f7)은 적용 대상 5. 로봇 능력·작업 표현·55. 현장 조사·설치·시운전과 함께 반영 제안. 18. 실시간 세계 상태·데이터 일관성 관련 f17·f19 는 현재 상태 보고로만 다뤘고 34. 시뮬레이션·예측용 디지털 트윈과 섞지 않았다. 새 일반 열린 질문 없음. 정정 요청 없음. 입력 누락 없음.

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 2
- 답한 질문 id: q2-04

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | VDA 5050 팩트시트의 동작 결과(actionResult)·제약(constraints)·동작 설명처럼 기계가독 스키마 안에 남은 자유 텍스트 필드를 능력 온톨로지의 완료 확인·제약으로 옮길 때 어떤 추출·검토 방법을 쓰는가? (q2-02 에서 파생) | 3 | f2 |
| — | 통합자가 플릿 어댑터에 구현한 동작–로봇 API 매핑과 완료 확인 코드를 능력 온톨로지의 근거 문서로 기록하고, 제조사 문서 선언과 어떻게 구분해 관리하는가? (q2-04 에서 파생) | 4 | f12 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 문서 유형 매트릭스: 사용자 매뉴얼·오류 코드표·치수도·도면 행 미조사, 64칸 가운데 대부분 미조사
    - 공개 문서 샘플 목록: AMR 샘플 없음, 포털 매뉴얼 이용 조건 미확인
    - q2-02·q2-03 부분 답, q2-05·q2-06·q2-07 열림
