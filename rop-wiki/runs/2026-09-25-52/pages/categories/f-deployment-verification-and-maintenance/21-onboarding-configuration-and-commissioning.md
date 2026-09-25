---
title: "21. 온보딩·설정·현장 시운전"
type: area
category: "F. 도입·검증·유지관리"
area_no: 21
related_areas: [5, 6, 9, 10, 22, 23, 24, 25, 27]
tags: [VDA 5050 팩트시트, 레이아웃 교환 형식, 플릿 어댑터, 지도 정합, 가상 시운전]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-251, ref-230, ref-228, ref-079, ref-153, ref-229, ref-046, ref-217, ref-269, ref-037, ref-465, ref-470, ref-466, ref-481, ref-265]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 21. 온보딩·설정·현장 시운전

# 21. 온보딩·설정·현장 시운전

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
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [분류원문]

## 2. SCM 관점의 질문

새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

다중 무인운반차(Automated Guided Vehicle, AGV) 도입이 오래 걸리는 원인으로 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문가의 수작업 경로망 설계가 꼽힌다(Beinschob 외, 2017). [사실][^ref-217] 지도 작성은 새 환경에 로봇을 배치할 때 시간이 많이 드는 과정으로 지목된다(Heselden·Das, 2024). [사실][^ref-269]

이 작업이 새 제조사·새 물류센터마다 반복되면, 늘린 로봇 대수가 실제 처리능력으로 바뀌는 시점이 늦어진다. [의견] 유럽연합 PAN-Robots 과제는 설치 기간을 6개월에서 2개월로 줄일 수 있다고 소개했으나, 이는 과제 측 보고값이며 비교 조건은 확인되지 않았다. [추정][^ref-265]

반복 작업은 로봇 신원·기능·제약 등록, 지도·레이아웃·경로망 작성과 가져오기, 제조사 지도와 공통 지도의 정합, 연동 수준 선택으로 나눌 수 있다. 등록 정보는 표준 메시지로 받을 수 있지만 경로망 설계와 지도 정합은 여전히 사람의 설정 작업으로 남는 것으로 보인다. [추정][^ref-031][^ref-230][^ref-153][^ref-079][^ref-217]

## 4. 핵심 개념과 용어

온보딩(onboarding)은 새 로봇·새 현장을 관제에 등록하고 설정해 운용에 넣는 과정이며, 아래 용어가 그 단계를 이룬다.

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area21-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 적치

**시나리오:** 새 제조사 AMR 을 적치 운반에 추가하고 현장 시운전하기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 물동량이 늘어 적치 운반 능력을 키우기로 하고, 기존 관제에 다른 제조사의 자율이동로봇(Autonomous Mobile Robot, AMR)을 더하기로 결정한다. [의견] |
| 작업 대상 | 입고 검수를 마친 팔레트·토트를 보관 위치까지 옮기는 적치 운반. [의견] |
| 수행 자원 | 새 AMR 은 신원 보고로 제조사·모델·일련번호·외곽 치수를 알린다. [사실][^ref-230] 통합 담당자는 플릿 어댑터 설정에 속도 한계·작업 유형·좌표 대응점·제조사 관제 연결 정보를 채운다. [사실][^ref-153] 경로망 설계와 지도 정합은 사람의 설정 작업으로 남는 것으로 보인다. [추정][^ref-217] |
| 제약 | 이번에 확인한 팩트시트의 필수·선택 최상위 절과 신원 보고 필드에는 지도 정합을 담는 항목이 보이지 않아, 정합은 현장별 설정·검증 항목으로 남는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-153] 연계 대상: 운행 구역 준비는 ISO 3691-4:2023 부속서 A 가 요구한다. [사실][^ref-470] |
| 완료·인계 | 관제가 지도 내려받기를 지시하고 로봇이 특정 지도 버전을 활성화한다. [사실][^ref-031] 이어 시운전 적치에서 도착 위치와 재고 위치 변경이 일치해야 운용 투입을 인정한다. [의견] 합격 기준은 미확인이다(11절). |
| 예외·성과 | 설치 기간 6개월→2개월(PAN-Robots)은 과제 측 보고값이며 비교 조건 미확인이다. [추정][^ref-265] 가상 시운전으로 시운전 기간을 3주 줄였다는 사례도 벤더 주장이다. [추정] 벤더 주장[^ref-481] |

다음은 설명을 위한 가상의 시나리오이다. 이 영역이 관여하는 칸은 주로 수행 자원·제약·완료·인계다. 로봇이 스스로 알리는 등록 정보와, 현장마다 사람이 정해야 하는 경로망·지도 정합이 갈리는 지점이 시운전 기간을 좌우한다. [의견]

시운전 중 정합 오차로 로봇이 엉뚱한 보관 위치에 도착하면 적치 완료와 재고 위치가 어긋난다. 그래서 어떤 시험으로 정합을 합격 판정할지가 열린 질문으로 남는다. [의견] 흐름 전체는 [흐름 매트릭스](../../flow-matrix.md)에서 본다.

## 6. 대표 접근법과 기술

반복 작업을 줄이는 접근은 등록 정보의 표준화, 설정의 구조화, 지도 작성의 반자동화, 능력 기술의 기계 판독화로 나뉜다. [추정][^ref-031][^ref-153][^ref-217][^ref-229]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area21-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

온보딩에 쓰이는 정보는 관제 인터페이스 표준, 레이아웃 교환 형식, 오픈소스 설정 도구, 능력 기술 서브모델로 흩어져 있다. [추정][^ref-031][^ref-046][^ref-153][^ref-229]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area21-s7.md)에 있다.

## 8. 대표 연구와 자료

연구는 지도 작성 부담을 줄이는 쪽과 능력 정보를 기계가 읽게 하는 쪽으로 나뉜다. [추정][^ref-217][^ref-037]

자세한 내용은 주제 페이지 [21. 온보딩·설정·현장 시운전 — 대표 연구와 자료](../../topics/2026/2026-09-25-area21-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

로봇 자체의 SLAM 지도 작성·위치 추정·센서 교정은 제조사 몫이고, 이종 로봇을 잇는 ROP 는 등록 정보의 수집·검증, 레이아웃·지도 정합 설정, 연동 수준 결정과 그 설정의 버전 관리를 맡는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-153][^ref-251]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트·신원 보고 수집과 검증, 어댑터 설정, 지도 배포 지시와 버전 관리, 연동 수준 결정 | SLAM 지도 작성, 위치 추정, 센서 교정, 로컬 주행 |
| 시설·설비 제어 | 평면도 위 문·승강기·충전기 위치 주석, 레이아웃·지도 정합 설정 | 승강기 제어, 운행 구역 안전 준비(ISO 3691-4:2023 부속서 A) |

이 표는 관제 인터페이스 자료에서 끌어낸 이 위키의 추론을 정리한 것이다. [추정][^ref-031][^ref-153][^ref-251]

VDA 5050 은 지도 배포 동작과 팩트시트를 정하지만 경로 설정은 범위 밖으로 둔다. [사실][^ref-031] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

온보딩은 등록할 정보(능력·지도)를 정의하는 영역과, 그 정보를 쓰고 검증하는 영역 사이에 놓인다.

- [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 요구·제공 능력 비교(IDTA 02020)와 자연어 능력 설명에서 능력 온톨로지를 생성하는 방법이 로봇 등록 작업을 줄이는 데 쓰일 수 있다. [추정][^ref-229][^ref-465]
- [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md) — 평면도 주석, 층 정렬, 지도 정합이 공통 공간 모델을 만든다. [사실][^ref-079]
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 팩트시트·신원 보고·어댑터 설정이 관제 연동의 첫 단계가 되는 것으로 보인다. [추정][^ref-031][^ref-230][^ref-153]
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 평면도 위 승강기·문 주석이 설비 연동과 맞물리는 것으로 보인다. [추정][^ref-079]
- [22. 시뮬레이션·예측용 디지털 트윈](22-simulation-and-predictive-digital-twin.md) — 가상 시운전과 팩트시트의 시뮬레이션 용도로만 이어진다. [추정][^ref-481][^ref-228]
- [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) — 시운전 합격 판정 기준은 아직 열린 질문(11절)이며, 국내 물류로봇 시험·실증 체계가 이 판정과 이어질 수 있다. [추정][^ref-466]
- [24. 자산·소프트웨어 수명주기 관리](24-asset-and-software-lifecycle-management.md) — 지도 id·버전 배포와 활성화가 버전 관리 대상이다. [사실][^ref-031]
- [25. 안전·위험 관리](../g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — 운행 구역 준비 요구가 시운전 제약이 된다. [사실][^ref-470]
- [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 자연어 능력 설명에서 LLM 으로 능력 온톨로지를 생성하는 방법은 27. AI·학습·적응과 모델 운영의 문서 해석을 이 영역과 5. 로봇 능력·작업 온톨로지에 적용하는 연구 방법이다. [추정][^ref-465]

관련 트랙: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md).

## 11. 열린 질문

국내 적용 사례와 시운전 합격 기준이 아직 확인되지 않았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-022** (열림) 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? 이번 실행의 한국어 검색에서는 사례를 찾지 못했다.
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가?
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가?
- (새 질문 · 열림 · 제기 2026-09-25 · 실행 2026-09-25-52) 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? [^ref-031][^ref-046]

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-251]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration), 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-079]: Open Robotics, Programming Multiple Robots with ROS 2 — traffic-editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-229]: IDTA (admin-shell-io/submodel-templates), IDTA 02020 Submodel Capability Description 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25 (원문 미열람)
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-25
[^ref-217]: Beinschob, P. 외, Semi-automated map creation for fast deployment of AGV fleets in modern logistics, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724, 접근일 2026-09-25 (원문 미열람)
[^ref-269]: Heselden, J. R., & Das, G. P., Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments, 2024-04, https://arxiv.org/abs/2404.13499, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-466]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-481]: Siemens Digital Industries Software, Virtual commissioning with Siemens solutions reduces launch time by three weeks, 미확인, https://resources.sw.siemens.com/en-US/case-study-idc/, 접근일 2026-09-25 (원문 미열람)
[^ref-265]: European Commission CORDIS, PAN-ROBOTS: Automating logistics for the factory of the future, 미확인, https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future, 접근일 2026-09-25 (원문 미열람)
