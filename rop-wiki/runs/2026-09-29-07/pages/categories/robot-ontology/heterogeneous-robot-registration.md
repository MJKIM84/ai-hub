---
title: "4. 이기종 로봇 등록"
type: area
category: "B. 로봇 온톨로지"
area_no: 4
related_areas: [5, 6, 7, 20, 21, 45, 47, 55, 57, 63]
tags: [VDA 5050 팩트시트, 자산관리셸, 디지털 명판, 신원 보고, 플릿 어댑터, 온톨로지 채우기]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-228, ref-198, ref-230, ref-239, ref-153, ref-869, ref-870, ref-871, ref-043, ref-872, ref-031, ref-873, ref-874, ref-465, ref-875]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 4. 이기종 로봇 등록

# 4. 이기종 로봇 등록

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

제조사마다 식별·제원 정보의 이름과 형식이 다르므로, 등록을 빠르고 믿을 수 있게 하려면 제조사가 기계가독 형식으로 내는 기록과 그것을 받는 경로가 먼저 정해져야 한다. 서로 다른 세 발행 기관(VDA, IDTA, MassRobotics)이 각각 제조사가 제공하는 기계가독 등록 기록을 정의하며, 제조사명·기종(시리즈)·일련번호는 세 형식에 공통으로 들어 있는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-871]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 왜 중요한가](../../topics/2026/2026-09-29-area04-s3.md)에 있다.

## 4. 핵심 개념과 용어

**VDA 5050 팩트시트(factsheet)** — 독일자동차산업협회(Verband der Automobilindustrie, VDA)와 독일기계설비제조업협회(VDMA)의 VDA 5050 에서 로봇이 자신의 제원을 관제에 알리는 메시지다.

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area04-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 병원 2건과 기타(공항) 1건이다. 물류창고·제조 공장·상업 시설·가정·실외의 등록 사례는 이번 조사에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 타르투대학교병원에서 자체 관제가 없는 로봇을 Open-RMF 에 등록해 혈액 검체 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 중환자실에서 검사실로 혈액 검체를 운반하는 작업. 요청이 발생하는 방식은 이번 브리프에 없어 미확인 |
| 작업 대상 | 혈액 검체와, 로봇이 지나야 하는 프로그램 제어가 없는 병원 문. [사실][^ref-869] |
| 수행 자원 | PAL Robotics TIAGo(로봇 탑재 컴퓨터의 FreeFleet 클라이언트), 플릿 이름·DDS 설정을 적은 FreeFleet 서버, 배터리·속도·발자국을 적은 RMF 어댑터 파일, 문의 카드 인식·근접 센서를 대신 작동시키는 서보 장치. [사실][^ref-869] |
| 제약 | 병원 문에 프로그램 제어가 없어 서보 장치를 만들어 카드 인식·근접 센서를 대신 작동시켜야 했다. [사실][^ref-869] |
| 완료·인계 | 미확인(브리프에 없음) |
| 예외·성과 | 미확인(브리프에 없음) |

Valner 외(2022)의 현장 시험은 자체 관제가 없는 로봇을 FreeFleet 클라이언트·서버와 어댑터 파일로 등록했다. [사실][^ref-869] 이 영역이 관여하는 칸은 수행 자원이다. 등록 때 적은 배터리·속도·발자국이 곧 기종 제원 기술이며, 문 통과용 보조 장치는 등록된 로봇 능력만으로 부족한 현장 조건을 설비 쪽에서 메운 예다.

**현장 유형:** 병원

**사례:** 싱가포르 공공 의료기관의 RoMi-H 등재 프로그램으로 시스템 통합사를 사전 평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 시스템 통합사가 공공 의료기관의 병원 제안 요청에 참여하려면 등재가 필요하다(2025-05-01 시행). [사실][^ref-872] |
| 작업 대상 | 통합사의 기술·배치 역량(평가 대상 정보). [사실][^ref-872] |
| 수행 자원 | 보건부(RoMi-H 를 공공 의료기관의 자동화 통합 플랫폼으로 지정), 창이종합병원 CHART(등재 운영), 시스템 통합사(2026-08-24 기준 등재 5곳). [사실][^ref-872] |
| 제약 | 기술·배치 역량 평가 통과, 등재 유효 기간 2년. [사실][^ref-872] |
| 완료·인계 | 등재가 확정되어야 병원 제안 요청 참여 자격이 생긴다. [사실][^ref-872] |
| 예외·성과 | 미확인(브리프에 없음) |

이 사례는 로봇이 아니라 로봇을 등록·연동할 주체를 사전 평가하는 관문이다. 평가의 기술 항목(어댑터 시험·적합성 검사 등)은 공지에 없어 미확인이다.

**현장 유형:** 기타

**사례:** 인천공항 다기종 로봇 제작·관제 구축 사업(기사가 전한 벤더 주장)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(기사에 없음) |
| 작업 대상 | 미확인(기사에 없음) |
| 수행 자원 | 여러 제조사의 로봇을 하나의 시스템에서 제어한다는 클로봇의 통합관제 솔루션 크롬스(기사 인용 "국내 첫 이기종 로봇 통합관제 솔루션", 50대 이상 동시 제어). [추정] 벤더 주장[^ref-870] |
| 제약 | 엘리베이터 탑승을 지원한다고 소개된다. [추정] 벤더 주장[^ref-870] |
| 완료·인계 | 미확인(기사에 없음) |
| 예외·성과 | 미확인(기사에 없음) |

로봇신문 기사(2025-11-09)는 클로봇이 LG CNS 와 함께 인천공항 다기종 로봇 제작·5G 디지털 트윈 관제 구축 사업을 계약했다고 전하지만, 연동 제조사 수와 등록 방식은 기사에 없다. [추정] 벤더 주장[^ref-870] 이 사례는 국내에 이기종 관제 사업이 있음을 보여 줄 뿐 등록 데이터 형식의 근거는 되지 않는다.

## 6. 대표 접근법과 기술

등록 데이터를 로봇에서 직접 받는 경로가 두 표준에 있다. VDA 5050 명세 3.0.0 판은 플릿 관제가 factsheetRequest 즉시 동작을 보내면 로봇이 factsheet 토픽에 팩트시트를 게시하는 요청·응답 방식을 정하고, 팩트시트에는 플릿 관제에서 로봇 설정을 돕는 매개변수와 벤더 특정 정보가 들어간다. [사실][^ref-031]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area04-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

전체 목록은 [표준 목록](../../standards/index.md)에 있다. 용어집의 [능력 기술 서브모델](../../glossary/capability-description-submodel.md)과 [소프트웨어 명판](../../glossary/software-nameplate.md)은 같은 자산관리셸 계열이지만 이번 브리프가 다루지 않아 표에 넣지 않았다.

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area04-s7.md)에 있다.

## 8. 대표 연구와 자료

Valner, R. 외(타르투대학교), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — 자체 관제가 없는 TIAGo 를 FreeFleet 과 어댑터 파일로 Open-RMF 에 등록하고, 프로그램 제어가 없는 병원 문을 서보 장치로 지나며 혈액 검체를 운반한 현장 시험. 등록 작업의 실제 구성을 보여 준다. [사실][^ref-869]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 대표 연구와 자료](../../topics/2026/2026-09-29-area04-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트·명판·신원 보고에 담긴 식별·제원·버전을 받아 등록부에 저장·대조하고 버전 변경을 추적한다 | 위치추정 방식·주행 방식·펌웨어·소프트웨어 버전이 가리키는 위치추정·회피 성능 자체는 제조사가 소유·갱신한다 |
| 업종별 조건 | 현장이 요구하는 벤더·통합사 사전 평가 결과를 등록 승인 관문의 제약으로 반영한다 | 의료 현장의 등재 제도 자체(평가 기준·운영)는 보건당국·병원의 몫이다 |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 제조사·기종·일련번호·펌웨어·SDK 버전·장착 장비를 담는 등록부, 팩트시트·자산관리셸·신원 보고를 받아 저장·대조하는 수집 경로, 문서·URDF 에서 뽑은 능력 초안의 검토·승인 기록, 어댑터 설정 초안 생성이며, 등록 승인 관문에 벤더·통합사 사전 평가를 둘 수 있을 것으로 보인다. [추정][^ref-031][^ref-198][^ref-153][^ref-872]

연계 대상: 팩트시트의 위치추정 방식·주행 방식과 mobileRobotConfiguration 의 펌웨어·소프트웨어 버전은 제조사가 소유·갱신하는 로봇 자체 지능·제어 정보이므로, 이종 제조사를 잇는 ROP 는 등록 시 이를 받아 저장·대조하고 버전 변경을 추적하는 데 그치고 위치추정·회피 성능 자체는 제조사에 맡겨야 할 것으로 보인다. [추정][^ref-228][^ref-031] 이 경계는 분류 원문 19장의 "로봇 자체 지능·제어" 행에 해당하며([범위 경계](../../about/scope-boundary.md)), 자사 로봇까지 만드는 회사라면 경계가 이동할 수 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) — 등록 때 받은 팩트시트·서브모델·신원 보고의 제원과 문서에서 뽑은 능력 초안이 능력 표현의 입력이 된다. 팩트시트 필드 설명은 이 페이지에 두고, 표현 표준 정렬은 저 페이지가 맡는다. [추정][^ref-198][^ref-153]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area04-s10.md)에 있다.

## 11. 열린 질문

**oq-128** (상태: 열림 · 실행 2026-09-29-07 에서 부분 진전) 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? — 이번 조사에서 국내 자료로 확인된 것은 자산관리셸로 AMR 정보를 기록하는 설계 연구와 벤더의 이기종 관제 소개뿐이며, 실제 등록 데이터로 운영에 쓴 국내 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-043][^ref-870]

자세한 내용은 주제 페이지 [4. 이기종 로봇 등록 — 열린 질문](../../topics/2026/2026-09-29-area04-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-228]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050/json_schemas/factsheet.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-29
[^ref-198]: Industrial Digital Twin Association (IDTA), IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-29
[^ref-230]: MassRobotics (AMR Interoperability Working Group), AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-29
[^ref-153]: Open Robotics (Programming Multiple Robots with ROS 2), Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-29
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29
[^ref-870]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-29
[^ref-871]: Industrial Digital Twin Association (IDTA), IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf, 접근일 2026-09-29
[^ref-043]: 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)), 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-29
[^ref-872]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-29
[^ref-031]: VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소, VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-29
