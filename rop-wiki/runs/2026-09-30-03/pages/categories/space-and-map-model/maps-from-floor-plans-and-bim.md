---
title: "14. 도면·BIM에서 지도 만들기"
type: area
category: "D. 공간·지도 모델"
area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [평면도 인식, BIM, IFC, 지도 정합, 층 정렬 기준점, 설계–준공 편차]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-079, ref-153, ref-156, ref-213, ref-063, ref-1010, ref-067, ref-1011, ref-081, ref-1012, ref-817, ref-869, ref-083, ref-221, ref-1013]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 14. 도면·BIM에서 지도 만들기

# 14. 도면·BIM에서 지도 만들기

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

건물 도면과 건물 정보 모델링(Building Information Modeling, BIM) 모델은 여러 제조사의 로봇 지도를 묶는 공통 기준 좌표이자, 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점이 될 수 있다. [추정][^ref-079][^ref-213]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 왜 중요한가](../../topics/2026/2026-09-30-area14-s3.md)에 있다.

## 4. 핵심 개념과 용어

도면·BIM 과 로봇 지도를 잇는 데는 층을 맞추는 기준점, 건물 모델의 공간·운송 요소, 로봇용 지도 형식, 모델과 현실의 차이라는 개념이 쓰인다. [사실][^ref-079][^ref-156][^ref-081]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area14-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

확인한 자료에서 도면 기반 지도를 현장에 쓴 사례는 병원 현장 시험 1건이며, 대학 건물의 BIM 기반 위치 추정 연구 시험 1건을 연계 대상 사례로 함께 싣는다. [사실][^ref-869][^ref-1011] 물류창고·제조 공장·상업 시설 사례는 이번 자료에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 병원 평면도 주석과 로봇 격자 지도 정합으로 검체 운반 준비

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병원 건축 평면도(공간), 로봇이 만든 격자 지도(정보), 중환자실에서 검사실로 옮기는 시간이 중요한 혈액 검체(물건) [사실][^ref-869] |
| 수행 자원 | 원격 조작한 PAL Robotics TIAGo 로봇이 동시적 위치 추정 및 지도 작성(Simultaneous Localization and Mapping, SLAM)으로 격자 지도를 만들고, Open-RMF 교통 편집기로 평면도에 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합했다 [사실][^ref-869] |
| 제약 | 무선 주파수 식별(Radio-Frequency Identification, RFID)·근접 센서로 여는 반자동 문 두 곳을 통과해야 했다 [사실][^ref-869] |
| 완료·인계 | 미확인 |
| 예외·성과 | 넓은 구역을 한 번에 매핑하면 누적 불확실성으로 지도가 비틀리기 쉬워, 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확했다. 처리량·시간·비용 영향은 미확인 [사실][^ref-869] |

Valner 외(2022-08)가 보고한 에스토니아 타르투 대학병원 현장 시험에서는 평면도와 격자 지도 두 좌표 표현 사이의 변환을 정한 뒤 그 지도로 검체 운반을 수행했다. [사실][^ref-869] 이 영역은 여섯 항목 가운데 작업 대상(평면도·격자 지도)과 수행 자원(주석·정합 작업), 예외·성과(매핑 오차 대처)에 주로 관여한다. [추정][^ref-869] 시작 조건과 완료·인계를 적은 근거는 이번 자료에 없어 미확인으로 둔다.

**현장 유형:** 기타

**사례:** 대학 건물에서 BIM 을 사전 지도로 쓰는 로봇 위치 추정 연구 시험(연계 대상)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | IFC 형식 BIM 의 의미 요소를 바꾼 로봇용 세계 모델과 이를 저장한 공간 데이터베이스(정보) [사실][^ref-1011] |
| 수행 자원 | 2D 라이다(Light Detection and Ranging, LiDAR)와 주행거리계만 가진 로봇이 주변 구조 요소를 질의해 특징 검출기를 설정하고 그래프 기반 방법으로 위치를 추정했다 [사실][^ref-1011] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | BIM 이 있는 대형 대학 건물에서 로봇이 자세를 추적할 수 있음을 보였다. 실패 시 복구 주체와 처리량·시간·비용 영향은 미확인 [사실][^ref-1011] |

이 사례는 상용 운영이 아니라 Hendrikx 외(ICRA 2021)가 대형 대학 건물에서 한 위치 추정 연구 시험이다. [사실][^ref-1011] BIM 을 사전 지도로 쓰는 위치 추정은 로봇 자체 지능·제어에 속하는 연계 대상이며, 이 영역과 맞닿는 부분은 같은 BIM 에서 구조 요소·공간 정보를 가져오는 단계다. [추정][^ref-1011]

## 6. 대표 접근법과 기술

도면·BIM 에서 로봇 지도를 만드는 기술은 평면도 인식, BIM·CAD 변환, 축척 보정과 도면 기준 정합, 설계–준공 편차 확인으로 나뉘며, 앞의 둘은 연구 수준에서 자동화가 진행됐고 뒤의 둘은 사람 입력과 확인에 기대는 부분이 크다. [추정][^ref-1010][^ref-081][^ref-079][^ref-153]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area14-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 직접 닿는 표준·오픈소스는 공간·운송 요소를 정의한 IFC 4.3 과, 도면 주석·좌표 변환을 다루는 [Open-RMF](../../glossary/open-rmf.md) 도구다. [사실][^ref-156][^ref-079]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| IFC 4.3 IfcSpace·IfcRelSpaceBoundary | 표준 | 공간과 그 경계를 가져와 층별 공간 목록을 만드는 입력 요소 [사실][^ref-156] | buildingSMART 개발 저장소 문서 |
| IFC 4.3 IfcTransportElement | 표준 | 승강기·에스컬레이터·무빙워크를 공용 자원 후보로 가져오는 입력 요소 [사실][^ref-213] | buildingSMART 개발 저장소 문서 |
| Open-RMF 교통 편집기(traffic-editor) | 오픈소스 | 평면도 위 벽·문·승강기·차선·충전 위치 주석, 측정선 축척, 층 정렬 기준점, 로봇 지도 레이어 정합 [사실][^ref-079] | Open Robotics 문서 |
| Open-RMF 플릿 어댑터 reference_coordinates 와 nudged | 오픈소스 | 로봇 좌표계와 도면 기준 좌표계 사이 대응점 기반 변환 추정 [사실][^ref-153] | Open Robotics 튜토리얼 |

IFC 4.3 두 행은 buildingSMART 개발 저장소(ifc4.3-main) 문서를 기준으로 했으며, 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있다. [사실][^ref-156] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 대표 자료는 평면도 인식 데이터셋·방법, BIM 기반 지도·위치 추정 연구, 병원 현장 시험이다. [사실][^ref-063][^ref-081][^ref-869]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 대표 연구와 자료](../../topics/2026/2026-09-30-area14-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사별 로봇 지도와 도면 기준 공통 좌표 사이 변환을 등록·관리하고, 도면과 현장의 차이를 표시해 사람이 확인·승인하게 한다 [추정][^ref-153][^ref-081] | 연계 대상: 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정과 그 성능 포함) [추정][^ref-1011][^ref-221] |
| 시설·설비 제어 | 도면·IFC 에서 문·승강기·충전 위치 초안을 만들어 공용 자원 목록에 올린다 [추정][^ref-079][^ref-213] | 연계 대상: 승강기 운행 제어 [추정][^ref-213] |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고, 층별 축척과 층 간 기준점을 설정하며, 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고, 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일로 보인다. [추정][^ref-079][^ref-153][^ref-156][^ref-213][^ref-081] 정합 결과를 누가 언제 확정하는지는 아직 확인되지 않았다(열린 질문 oq-126).

로봇의 SLAM·LiDAR 위치 추정은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속한다. [추정][^ref-1011][^ref-081][^ref-221][^ref-213][^ref-1013] 따라서 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다. [추정][^ref-1011][^ref-081][^ref-221][^ref-213][^ref-1013]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계 기준 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 좌표 정렬·지도 관리·도면 해석 AI·설비 연동·설치 과정과 이어진다. [추정][^ref-079]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area14-s10.md)에 있다.

## 11. 열린 질문

이 영역에는 정합 결과의 승인 주체와 변하는 현장의 BIM 동기화라는 기존 질문 두 건이 열려 있고, 이번 조사에서 새 질문 네 건이 생겼다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 열린 질문](../../topics/2026/2026-09-30-area14-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-30
[^ref-156]: buildingSMART International, IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md, 접근일 2026-09-30
[^ref-213]: buildingSMART International, IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-30
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-1010]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017), Raster-to-Vector: Revisiting Floorplan Transformation, 2017, https://art-programmer.github.io/floorplan-transformation.html, 접근일 2026-09-30
[^ref-1011]: Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021), Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization, 2021, https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30
[^ref-221]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023), BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR, 2024-08, https://arxiv.org/abs/2408.15870, 접근일 2026-09-30
[^ref-1013]: 엔지니어링데일리, "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개, 2020-12-28, https://www.engdaily.com/news/articleView.html?idxno=12613, 접근일 2026-09-30
