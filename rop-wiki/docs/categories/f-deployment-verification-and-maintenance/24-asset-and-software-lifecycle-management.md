---
title: "24. 자산·소프트웨어 수명주기 관리"
type: area
category: "F. 도입·검증·유지관리"
area_no: 24
related_areas: [6, 9, 13, 16, 19, 21, 22, 23, 25, 26, 28]
tags: [펌웨어 버전 관리, 지도 버전, 배터리 건강 상태, 상태 감시, 패치 관리, 무선 업데이트]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-051, ref-228, ref-230, ref-523, ref-364, ref-550, ref-403, ref-553, ref-554, ref-556, ref-557, ref-559]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 24. 자산·소프트웨어 수명주기 관리

# 24. 자산·소프트웨어 수명주기 관리

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [분류원문]

## 2. SCM 관점의 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]

## 3. 왜 중요한가

펌웨어가 바뀔 때 다시 검증할 범위를 정하려면 로봇별 소프트웨어 버전을 그 로봇이 쓰이는 현장·기능과 연결해 두고, 규격 주 버전·기능 선언·안전 파라미터·지도 버전의 변화를 재검증 촉발 조건으로 삼는 방식이 가능해 보이지만, 이 영향 범위 산정을 규정한 공개 절차는 이번 조사(2026-09-25 기준)에서 찾지 못했다. [추정][^ref-031][^ref-228][^ref-550][^ref-559]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area24-s3.md)에 있다.

## 4. 핵심 개념과 용어

수명주기 관리를 이야기하려면 먼저 무엇을 자산으로 보고, 그 상태와 버전을 어떤 이름으로 부르는지 정해야 한다.

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

다음은 설명을 위한 가상의 시나리오 두 개이다. 지도 버전 전환 규칙과 배터리 상태 보고 필드가 적치의 시작 조건과 출하의 제약으로 어떻게 작용하는지를 보인다. [추정][^ref-031][^ref-051]

### 적치: 랙 배치 변경 뒤 새 지도 버전으로 작업 재개

**물류 흐름 단계:** 적치

**시나리오:** 랙 배치 변경 뒤 새 지도 버전으로 적치 작업 재개

| 항목 | 내용 |
|---|---|
| 시작 조건 | 랙 배치가 바뀌어 새 지도 버전이 나오면, 진행 중 적치 주문을 정리하고 지도 전환 시점을 정하는 일이 적치 재개의 시작 조건이 되는 것으로 보인다. [추정][^ref-031] |
| 작업 대상 | 입고 뒤 적치할 팔레트·박스(가상) |
| 수행 자원 | 플릿 제어가 즉시 동작 downloadMap·enableMap 으로 지도 내려받기·활성화를 지시하고 [사실][^ref-031], 로봇은 상태 메시지로 mapId·mapVersion·mapStatus 를 보고한다. [사실][^ref-051] |
| 제약 | 같은 mapId 에서는 한 번에 한 버전만 활성화된다. [사실][^ref-031] |
| 완료·인계 | 로봇이 보고한 새 mapVersion 의 mapStatus 가 ENABLED 인지 확인한 뒤 적치 주문을 재개한다(이 시나리오의 가정). mapStatus 는 ENABLED 또는 DISABLED 값을 가진다. [사실][^ref-051] |
| 예외·성과 | 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 오류를 CRITICAL 수준으로 보고하도록 규정돼 있다. [사실][^ref-031] 이 규정 때문에 판 차이로 생긴 미지원 기능이 실행 시점 오류로 드러난다고 해석할 수 있다. [추정][^ref-031] |

### 출하: 마감 전 배터리 열화 로봇의 배정

**물류 흐름 단계:** 출하

**시나리오:** 출하 마감 전 집중 시간대에 배터리 상태가 낮아진 로봇 배정

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 전 집중 시간대에 출하 주문이 몰린다(가상). |
| 작업 대상 | 출하 대기 구역으로 옮길 화물(가상) |
| 수행 자원 | 로봇은 stateOfCharge·batteryHealth·range 를 보고하고 [사실][^ref-051], ROP 는 이 값을 작업 배정·충전 계획에 반영하는 쪽으로 보인다. [추정][^ref-051] |
| 제약 | batteryHealth 가 낮아진 로봇은 같은 충전 상태에서도 추정 도달 거리(range)가 짧아질 수 있어, 배터리 열화가 작업 배정·충전 계획의 제약으로 작용하는 것으로 보인다(물류센터 실측 자료는 미확인). [추정][^ref-051][^ref-403] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

두 시나리오에서 이 영역이 관여하는 칸은 적치의 시작 조건·수행 자원·제약·완료·인계·예외·성과와 출하의 수행 자원·제약이다. 전체 흐름은 [흐름 매트릭스](../../flow-matrix.md)에서 본다.

## 6. 대표 접근법과 기술

산업용 로봇의 상태 감시·고장 진단은 고장 모드와 근본 원인, 데이터 수집 전략과 센서, 모델 기반·데이터 기반 기법으로 정리돼 있다. [사실][^ref-553]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 버전·상태 정보는 로봇 상호운용 규격의 필드와 자산·패치 관리 표준에서 출발한다. [추정][^ref-031][^ref-550][^ref-554] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area24-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 대표 연구를 부품 상태 감시 검토와 배터리 열화 인지 스케줄링으로 나누는 것은 구축자 의견이다. [의견][^ref-553][^ref-403]

- Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review(2025) — 산업용 로봇의 고장 모드·데이터 수집·모델 기반·데이터 기반 진단을 상태 기반 정비 관점에서 정리했다. [사실][^ref-553] 이 논문이 ROP 가 받을 정비 신호의 출처를 이해하는 배경 자료라는 것은 구축자 의견이다. [의견]
- 저자 미확인, Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots(2026-03, arXiv 프리프린트, 동료 심사 전) — 작업 배정·충전을 플릿 전체 배터리 열화 균형과 함께 최적화한다. [사실][^ref-403]
- Amazon Web Services, ros2-ota-firmware-updates README — aws-samples 저장소의 시연용 샘플로 플릿 OTA 배포·버전 조회를 보이며, 자동 롤백은 README가 이점으로 나열할 뿐 구현 절차는 보이지 않는다. [추정] 벤더 주장[^ref-556]
- SDR 과제 킥오프 워크숍 보도(2026-07-23) — 국내 클라우드 기반 OTA 목표 사례다. [추정][^ref-557]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP 는 버전 목록·배터리 상태·배포 복구·지도 전환을 조율하고, 펌웨어 내용과 부품·배터리 내부 진단은 제조사 쪽에 두는 것으로 보인다. [추정][^ref-051][^ref-553]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇·어댑터·지도·모델의 버전 목록 유지, 로봇이 보고하는 배터리 상태·오류를 배정·충전 계획에 반영, 업데이트 배포와 실패 시 복구 조율, 지도 버전 활성화 시점 동기화 [추정][^ref-031][^ref-051][^ref-364][^ref-556] | 연계 대상: 펌웨어 내용 자체, 관절·감속기 같은 기계 부품의 고장 진단·잔여 수명 예측, 배터리 관리 시스템(Battery Management System, BMS) 내부의 열화 추정. ROP 는 그 결과(배터리 상태 값·오류 코드·정비 필요 신호)를 받는 쪽으로 보인다. [추정][^ref-553][^ref-051][^ref-230] |

업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포하는 방식도 ROP 가 조율할 후보로 보이지만, 이 부분은 확인한 출처에 직접 근거가 없는 구축자 추론이다. [추정]

분류 원문 9장은 이 경계가 제품 전략에 따라 이동할 수 있고, 이종 제조사를 연결하는 ROP 는 "인터페이스와 실행 보장"을 맡을 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 규격마다 버전 필드의 위치가 달라(VDA 5050 은 팩트시트에 소프트웨어 버전, 상태 메시지에 지도 버전을 두고 MassRobotics 스키마는 버전 필드가 없다) 여러 규격이 섞인 플릿에서는 ROP 가 로봇별 버전 목록을 별도로 유지해야 할 것으로 보인다. [추정][^ref-228][^ref-051][^ref-230]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아래 연결은 이번 조사 결과를 바탕으로 한 구축자 의견이다. [의견][^ref-523][^ref-554][^ref-403][^ref-559]

자세한 내용은 주제 페이지 [24. 자산·소프트웨어 수명주기 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area24-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 새로 올린 질문이며 id 는 퍼블리셔가 부여한다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-61) EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가. 2차 수정: 7절 첫 문장 [추정]·각주 보강, 8절 대표 연구 분류·평가 [의견]화, 8절 ref-556 항목 롤백 문구 정정 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area24-s4.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "4. 핵심 개념과 용어" 절(1,365자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area24-s6.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "6. 대표 접근법과 기술" 절(1,327자)을 옮겼다. 2차 수정: 부품 진단 연계 대상 문장을 [추정]과 각주로 고치고, 5·9절 참조를 원 세부영역 페이지 절 링크로 바꿈 (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 왜 중요한가](../../topics/2026/2026-09-25-area24-s3.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "3. 왜 중요한가" 절(1,019자)을 옮겼다(2차 수정 없음) (실행 2026-09-25-61)
- 2026-09-25 · 생성 · [24. 자산·소프트웨어 수명주기 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area24-s7.md) — 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(982자)을 옮겼다. 2차 수정: 1절 요약과 3절 첫 문장의 태그를 [추정]으로 낮추고 각주를 ref-031·ref-550·ref-554 로 바꿈 (실행 2026-09-25-61)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: Open Robotics (ROS 2 Design), Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-550]: IDTA (admin-shell-io/id GitHub), IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing), 미확인, https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md, 접근일 2026-09-25
[^ref-403]: arXiv (저자 미확인), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-553]: Lei, Y., Liu, H., Li, N. 외, Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301), 2025, https://link.springer.com/article/10.1007/s11431-024-2810-2, 접근일 2026-09-25 (원문 미열람)
[^ref-554]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-556]: Amazon Web Services (aws-samples GitHub), ros2-ota-firmware-updates — README, 미확인, https://github.com/aws-samples/ros2-ota-firmware-updates, 접근일 2026-09-25
[^ref-557]: 네이트 뉴스(원 매체 미확인), 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장, 2026-07-23, https://m.news.nate.com/view/20260723n24828, 접근일 2026-09-25 (원문 미열람)
[^ref-559]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)
