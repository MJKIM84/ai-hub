---
title: "현장 실패 사례"
type: field-research
research: field-readiness-rop
related_areas: [18, 22, 30, 36, 38, 55, 62]
tags: [실패 사례, 미끄럼, 투명 재질, 반사, 위치 상실, 계단, 파지, 승강기, 재현 패키지]
status: published
confidence: low
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-031, ref-1577, ref-1578, ref-1579, ref-1580, ref-1585, ref-1588, ref-1589, ref-1590]
---

[홈](../../index.md) › [스터디](../index.md) › [현장 적용·운영 검증](index.md) › 현장 실패 사례

# 현장 실패 사례

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

발표에서 소개된 현장 실패를 열 가지 유형으로 일반화하고, 유형마다 원인을 가르는 질문과 기록해야 할 관측값을 붙였다. 사례의 현장명·세부 수치·발표자는 싣지 않았다. 이 페이지는 "이렇게 하면 해결된다"는 처방집이 아니라 "이 실패를 다시 볼 때 무엇을 확인해야 하는가"의 목록이다.

## 1. 현장 문제

발표 관찰: 아래 C01~C10의 "발표 관찰" 열은 모두 발표에서 그런 일이 있었다고 소개된 내용이다. 원본 로그를 받거나 원인을 검증한 것이 아니다. 발표에서 했다고 설명한 조치도 검증된 일반 처방으로 취급하지 않는다.

| id | 유형 | 발표 관찰 |
|---|---|---|
| C01 | 바닥 오염·마찰 | 기름이 묻은 바닥에서 미끄러짐. 설정 조정과 청소를 함께 했다 |
| C02 | 투명·반사 재질 | 투명 패널을 장애물로 인식해 멈춤. 인식 옵션을 조정했다 |
| C03 | 매달린 물체·통로 침범 | 장애물을 피하다 공정 구역 쪽으로 벗어남. 경로 추종을 엄격하게 제한했다 |
| C04 | 덮개 홈·문턱 | 회전할 때 발·구동부가 홈에 걸림. 진입 방향을 바꿨다 |
| C05 | 계단·주변 물체 | 계단 주변 물체와 인식·이동 방향 문제가 언급됐다 |
| C06 | 어둠·조명·그림자 | 어두운 구간과 명암 변화에서 잘못 인식. 조명·옵션을 바꿨다 |
| C07 | 광택 바닥·특징 부족 | 반사와 위치 상실. 경로·바닥을 조정했다 |
| C08 | 측정 대상 가림 | 로봇은 접근했지만 주변 설비가 측정할 부위를 가렸다 |
| C09 | 파지 공간 | 정격 무게보다 손잡이와 접근 공간이 제약이었다 |
| C10 | 승강기 통신·층 불확실 | 승강기 안 통신 음영과 층 상태 혼동. 위치 표지를 활용했다 |

## 2. 근거·적용 조건

공개 자료는 개별 사례의 원인이 아니라 관련 일반 사실만 알려 준다.

- C01: [추정] 벤더 주장: 제조사 SDK에 지면 마찰계수 힌트 설정이 있다(양수, 로봇이 범위를 제한할 수 있음, 권장 0.4~0.8, 기본 0.8).[^ref-1577] 해당 기름·발 패드·효과는 확인하지 못했고, 이 값은 실측 마찰계수와 같은 것이 아니다.
- C02: [사실] 투명 물체의 3D 형상 추정 연구의 저자 초록은 일반 깊이 센서가 투명 물체의 정확한 깊이를 얻기 어렵다는 문제를 다룬다.[^ref-1588] 초록만 읽었으며, 발표 사례의 센서·알고리즘은 확인하지 못했다.
- C03: [추정] 벤더 주장: 경로를 엄격히 따르는 모드와, 회피 시 허용 통로 폭의 절반을 정하는 별도 필드가 SDK에 있다.[^ref-1590] 발표에서 쓴 폭 값·단위·기준(로봇 중심인지 외곽인지)은 확인하지 못했고 재게시하지 않는다.
- C05: [추정] 벤더 주장: SDK는 계단 하강 방향 선호(뒤로 선호·항상 뒤로·제약 없음)를 구분하고, 값이 없으면 항상 뒤로 처리하며, 제약 없음에는 전진 하강 시 넘어질 수 있다는 경고가 있다. 계단은 trot 보행에서만 지원된다.[^ref-1590][^ref-1577] 이 설명을 모든 계단·모든 기종·상승 방향으로 넓힐 수 없다.
- C06: [사실] 시험 방법 측면에서는 조명 같은 조건을 통제된 기준에서 단계적으로 바꾸는 반복 시험이 공개돼 있다.[^ref-1580] [사실] 작업장 조도 규정은 사람이 상시 작업하는 작업면의 밝기 기준이며 센서 성능 기준이 아니다.[^ref-1585]
- C07: [추정] 벤더 주장: 특징이 적은 공간에서 위치 추정이 어렵고 로봇이 위치를 잃을 수 있다는 설명[^ref-1578]과, 위치 상실·막힘을 구분해 보고하는 상태가 있다.[^ref-1579] 바닥 반사가 원인이라는 인과는 따로 확인해야 한다.
- C08: [추정] 벤더 주장: 열화상 측정은 방사율·반사 겉보기 온도·물체 거리 등을 측정 매개변수로 구분하고 방사율을 가장 중요한 매개변수로 든다.[^ref-1589] 가림 해소나 대상 보정의 성공을 입증하지 않는다.
- C10: [사실] VDA 5050은 통신이 끊겨도 로봇이 마지막으로 확정된(released) 노드까지 주문을 수행한다고 정한다.[^ref-031] 이는 통신 규약의 의미이지, 특정 승강기·표지 방식의 신뢰성을 실증한 것이 아니다.
- C04, C09: 현장 자료나 공개 근거를 확보하지 못했다.

## 3. ROP 판단

[의견] 발표 관찰과 SDK 기능 설명은 "그 설정을 쓸 수 있다는 개연성"만 이어 준다. 실제 문제의 재현·개선·안전성을 서로 독립적으로 확인한 쌍으로 세지 않는다. 이번 열 가지 사례의 **현장 인과와 개선 효과를 독립 검증한 공개 증거는 확보하지 못했다.**

[의견] ROP에서 이 사례들은 두 곳에 쓰인다. 하나는 [환경 조건을 반영한 로봇 능력](context-aware-capabilities.md)의 실패 유형 기록이고, 다른 하나는 [제조사 피드백 패키지](manufacturer-feedback.md)의 재현 요청이다. 원인이 확정되기 전까지 해당 조건의 구간은 임시 제한이나 "확인 필요"로 둔다.

## 4. 제조사·설비·운영자 역할

[의견] 원인이 어디 있느냐에 따라 고칠 쪽이 다르다. 로봇 쪽(센서 옵션·제어 설정·인식 알고리즘)은 제조사, 환경 쪽(누유·바닥 덮개·조명·통신 음영)은 시설·네트워크 담당, 업무 쪽(경로·시간대·작업 순서)은 현장 운영과 통합자다. 같은 실패를 여러 쪽이 동시에 고치면 무엇이 효과였는지 알 수 없으므로, 변경은 한 번에 하나씩 기록하고 전후를 비교한다.

## 5. 대응·판단 기준

[의견] 사례마다 원인을 가르는 질문과 기록할 관측값이다.

| id | 원인을 가르는 질문 | 기록할 관측값과 수용 조건 |
|---|---|---|
| C01 | 오염의 분포·점도, 패드 마모, 적재 중심, 속도, 선회 중 무엇이 영향을 주는가? 반복 누유라면 시설·공정 원인을 제거해야 하는가? | 청결·허용 오염 조건을 나눠 미끄럼·자세·발 접촉·정지 거리·복구를 기록. 사람 보호를 갖춘 별도 승인 시험 |
| C02 | 반사로 생긴 가짜 물체인가, 깊이 결손인가, 실제 사람·장애물인가? 오검출을 줄이면 실제 장애물 미검출이 늘지 않는가? | 원시 영상·깊이, 재질·입사각·배경·조명, 실제 물체 위치. 정상 장애물 대조군 포함 |
| C03 | 경로 이탈 여유와 회피 공간이 함께 성립하는가? 피할 수 없을 때 정지하고 사람을 부르는가? | 로봇 중심이 아니라 적재물을 포함한 점유 궤적, 최대 횡오차, 정지 위치·대기 시간, 작업 구역 침범 |
| C04 | 진입·회전·이탈 중 어느 순간의 접촉인가? 덮개를 바꾸면 점검 접근성이 유지되는가? | 홈 폭·깊이, 단차, 유효 통로, 적재별 회전 궤적. 직진 통과와 선회 시험을 분리 |
| C05 | 오르기·내리기, 난간, 참, 주변 물체, 센서 시야를 나눠 봤는가? | 계단 기하, 이동 방향, 센서 시야, 적재 중심, 지원 설정. 기종 한계 밖이면 후보에서 빼거나 다른 동선 검토 |
| C06 | 조도 부족, 포화, 역광, 노출 전환, 그림자 경계 중 무엇인가? | 작업면·센서 시야 조도, 시간대·노출·영상, 오검출과 미검출. 조명 변경이 사람 작업·법규에 주는 영향은 별도 |
| C07 | 시각 특징 부족과 깊이 오인식은 같은 원인인가? 지도가 낡거나 가려진 것은 아닌가? | 기준 위치 대비 자세 오차, 재위치 추정 시간, 실패 위치. 반사 조건과 특징 밀도를 독립 변수로 기록 |
| C08 | 측정할 표면이 실제로 보이는가? 앞쪽 설비의 온도를 대상 온도로 잘못 읽지 않는가? | 자산·부위 id, 관심 영역, 가림 비율, 측정 각도, 기준 계측기 대조, 방사율 근거. 접근 성공과 측정 적합을 따로 판정 |
| C09 | 그리퍼 삽입·닫기·들기·회수 공간과 하중 중심, 물체 변형·표면 상태가 모두 맞는가? | 물체·손잡이 치수, 접근 자세, 힘·미끄럼, 안착 품질. 정격 가반하중만으로 배정하지 않는다 |
| C10 | 로봇 위치, 승강기 제어기의 층, 문·카 점유 중 무엇을 잃었나? 하나의 표지만으로 진입을 허락하는가? | 메시지 나이·순서, 문·카 상태, 로봇 관측, 세션 소유자. 서로 맞지 않으면 "알 수 없음"으로 두고 진입 보류 |

[의견] 반증 시험은 필수다. 반사 구간 정지가 줄었더라도 사람이나 투명한 실물 장애물 미검출이 늘면 통과로 보지 않는다. 엄격한 경로 추종으로 공정 침범이 줄었더라도 피할 수 없는 장애물 앞에서 통로를 오래 막으면 업무 수용 기준을 다시 본다. 바닥 개선으로 미끄럼이 줄었어도 청소·유지 뒤 효과가 지속되는지 따로 본다.

## 6. 검증·한계

- 사례는 발표 정리에서 일반화한 것이다. 원본 로그·영상·현장 측정은 받지 않았다.
- 공개 자료(SDK, 논문 초록, 시험 방법, 법령)는 같은 현장 성과를 측정한 자료가 아니다. 사례의 원인을 확증하는 데 쓰지 않는다.
- 공개 근거를 찾지 못했다는 것이 그런 현장이 없다는 뜻은 아니다.

## 7. 연결 영역

- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md): 실패 유형별 모델·관측·보정. 시뮬레이션으로 무엇까지 재현할 수 있는지는 [시뮬레이션 검증 범위](simulation-validation.md).
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): 상태·오류·작업을 시간축으로 잇는 원인 분석.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md): 승강기 층·문·점유 상태와 세션.
- [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): 파지·안착·인계 품질.
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md).

## 8. 남은 질문

- 실패마다 재현에 필요한 기록을 빠짐없이 모으려면 어떤 필드가 필요한가? 공통 재현 패키지는 [제조사 피드백 패키지](manufacturer-feedback.md)에 있다.
- 파지 가능성과 실제 인계 품질을 접근 → 파지 → 이동 → 안착 → 검사 전 구간에서 어떻게 대조하는가? (FR08, 관련 oq-063)
- 승강기 층·문·점유 상태가 오래됐거나 서로 맞지 않을 때 진입을 어떻게 막는가? (FR05, 관련 oq-034, oq-067)

[^ref-1577]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/spot/robot_command.proto (master, blob 183f8fa), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/spot/robot_command.proto, 접근일 2026-10-12
[^ref-1588]: Shreeyak S. Sajjan 외 (arXiv), ClearGrasp: 3D Shape Estimation of Transparent Objects for Manipulation, 2019-10-06, https://arxiv.org/abs/1910.02550, 접근일 2026-10-12
[^ref-1590]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/graph_nav/map.proto (master, blob f37e496), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/graph_nav/map.proto, 접근일 2026-10-12
[^ref-1580]: NIST, Performance of Emergency Response Robots, 2014-04-28, https://www.nist.gov/programs-projects/performance-emergency-response-robots, 접근일 2026-10-12
[^ref-1585]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제8조(조도), 2025-09-01, https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0008&lsiSeq=273603&urlMode=lsScJoRltInfoR, 접근일 2026-10-12
[^ref-1578]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_tech_summary.md (master, blob b92aad6), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_tech_summary.md, 접근일 2026-10-12
[^ref-1579]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_and_robot_locomotion.md (master, blob 1362051), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_and_robot_locomotion.md, 접근일 2026-10-12
[^ref-1589]: Teledyne FLIR, Measuring temperatures (FLIR 사용 설명서 T810605, latest), 미확인, https://docs.flir.com/T810605/en-US/latest/s10.html, 접근일 2026-10-12
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-12
