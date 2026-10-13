---
title: "면접 준비"
type: field-research
research: pm-interview-prep
level: study
hide: [toc]
search: {exclude: true}
related_areas: [1, 2, 3, 20, 22, 25, 29, 32, 38, 39, 41, 48, 51, 55, 56, 64]
tags: [면접 준비, PM, 로봇 서비스, 순찰, 배송, 안내, 사업 모델, 현장 구축]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-031, ref-251, ref-1580, ref-1589, ref-1591, ref-1592, ref-1595, ref-1596, ref-1597, ref-1599, ref-1600]
---

[홈](../../index.md) › [확장 아이디어](../../ideas/index.md) › [스터디](../index.md) › 면접 준비

# 면접 준비

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

이 스터디는 **순찰·배송·안내 로봇 서비스**를 맡는 PM(제품 관리자)이 면접이나 발표 과제를 준비할 때 무엇을 알고 무엇을 결정해야 하는지를 정리한다. 로봇 두 종류를 소개하는 것이 목적이 아니다. PM은 **고객에게 어떤 완료 결과를 약속하고, 어떤 현장·기체·시설 조건에서 그 약속을 지키며, 실패했을 때 누가 업무를 이어갈지**를 결정해야 한다. 제품 사양, 사용자 흐름, ROP 계약, 현장 인수를 그 결정에 연결해 공부한다.

과제는 세 항목으로 나눈다. **① 서비스·사업 모델**, **② ROP·연동 아키텍처**, **③ 현장 구축·운영**이다. 각 페이지는 이 번호로 어느 과제에 쓰이는지 표시한다.

**조사용 가정:** 대한민국의 다층 복합 업무빌딩에 로비·사무 공간·공용 복도·공용 승강기·출입통제 구역이 있고, 사람과 로봇이 함께 다닌다. 특정 건물의 실측 결과가 아니다. 공장 사례는 비교에 쓰고, 호텔은 야간 소음·객실 사생활·수령 부재의 비교 가설로 다룬다. 실제 기체·현장·예산·수요는 미정이다.

## 결론 먼저

[의견] 과제에서 두 항목을 고른다면 **① 서비스·사업 모델 + ③ 현장 구축·운영**을 추천한다. 고객 가치와 운영 가능성을 한 흐름으로 입증하기 좋다. ② ROP는 그 약속을 구현하는 책임 경계와 시퀀스 한 장으로 뒷받침한다. 플랫폼·기술 PM 면접이라면 ②+③을 주축으로 바꾸고 ①의 완료 정의와 비용을 도입부에 둔다. 어느 조합이든 세 항목의 조사 근거는 이 스터디에 모두 있다.

[의견] 제안의 범위는 다음과 같다. 평탄한 구역의 배송·안내는 4휠 로봇 중심으로 검토하고, 계단이나 비정형 접근 구역에 중요한 점검점이 있어 점검 공백이 확인될 때만 4족 로봇을 추가로 비교한다. 한 종류의 로봇이나 사람·고정 센서만으로 충분하면 이종 로봇을 도입하지 않는다. 근거는 제품의 조건부 기능, 빌딩 통합 사례, 점검 운영 사례이며, ROI와 안전성은 시범 운영으로 검증할 가설이다.

## 먼저 이해할 일곱 가지

1. **4휠은 하나의 운동학이 아니다.** [추정] 벤더 주장: Robotnik RB-SUMMIT의 2024 데이터시트에도 skid-steering과 mecanum(전방향) 구성이 나뉜다.[^ref-1592] 현재 제품·공개 시뮬레이션 구성과 실제 구매품이 같은지는 따로 확인해야 한다.
2. **4족의 이동과 물체 조작은 다른 능력이다.** [추정] 벤더 주장: Spot의 Arm은 추가 장비이며 합산 페이로드와 다리 간섭에 영향을 준다.[^ref-1597] 계단은 형상·적재·조명·마찰·상하행까지 검증해야 한다.
3. **제품 자료도 판을 맞춰 읽어야 한다.** [추정] 벤더 주장: Spot의 현재 제품 페이지와 SDK 문서의 Gamma 기체 설명은 배터리·충전 값이 다르고,[^ref-1595][^ref-1596] RB-SUMMIT의 현재 페이지와 2024 데이터시트도 속도·통신 구성이 다르다.[^ref-1591][^ref-1592] 최신 페이지의 숫자와 예전 문서의 조건을 섞어 하나의 사양을 만들지 않는다.
4. **빌딩 서비스에는 시설과 기존 업무가 들어간다.** [추정] 운영기관 보고: NAVER 1784는 직원 앱·로봇 배송·로봇 전용 승강기·ARC 시스템을 함께 소개한다.[^ref-1599] 기존 공용 승강기 빌딩에 같은 경제성과 운영 결과가 재현된다는 증거는 아니다.
5. **점검 데이터의 품질이 이동 완료보다 중요할 수 있다.** [추정] 운영기관 보고: BMW는 시각·열·음향 데이터를 보전에 활용한다고 보고한다.[^ref-1600] [추정] 벤더 주장: 열화상 측정은 방사율·반사 온도·거리 같은 매개변수가 결과를 좌우한다.[^ref-1589] 둘 다 특정 건물의 탐지 정확도나 절감액을 보장하지 않는다.
6. **ROP는 모든 것을 직접 제어하는 계층이 아니다.** [사실] Open-RMF의 조율은 어댑터가 제공하는 제어·상태 수준에 의존하고,[^ref-251] VDA 5050은 로봇–관제 통신을 다루지만 시설·외부 IT·책임·안전·보안 구현은 범위 밖으로 둔다.[^ref-031]
7. **안전성과 경제성은 현장 조건별 증거가 필요하다.** [사실] NIST의 시험 방법은 변수를 통제한 뒤 단계적으로 조건을 바꾸는 반복 시험을 설명한다.[^ref-1580] 국내 영상·시설·업무 안전 법령과 고객이 합의한 목표는 각각 구분한다. 이 스터디는 특정 기체가 특정 빌딩에서 안전하거나 수익성이 있다는 실증이 아니다.

## PM의 핵심 의사결정

[의견] 아래 결정마다 먼저 알아야 할 것과 이 스터디가 제안하는 산출물이다.

| 결정 | 먼저 알아야 할 것 | 제안하는 산출물 |
|---|---|---|
| 누구의 문제를 풀 것인가 | 비용 지불자·이용자·현장 운영자가 다른지, 현재 업무와 수요 | 서비스별 고객 가치·이해관계자·업무 기준선 |
| 무엇을 성공으로 팔 것인가 | 배송 수령, 순찰 데이터, 안내 방문객 도착·인계의 차이 | 완료 증거·실패·부분 완료·환불/재수행 기준 |
| 기종을 한 종류로 할지 두 종류로 할지 | 접근 경로·센서·하중·사람 경험·가격/운영 제약 | 기종 후보별 "필수 기능·조건·증거·제외 이유" 표 |
| 구매·구축·개발 중 무엇을 선택할지 | 완제품 서비스와 개발형 차체의 차이, API·지원 계약 | 본체·옵션·서비스 앱·시설 연동·시험·운영의 조달 범위 |
| ROP가 어디까지 조율할지 | 제조사 중단·재개·상태 API, 지도·시설 제어 권한 | 책임 경계, 제어 소유권, 상태·취소 계약 |
| 어떤 현장에서 시작할지 | 통로 폭·회전·승강기·무선·충전·점검 품질·영상 문제 | 시범 구역·시간·적재·이용자·제외 구역 |
| 실패 시 서비스를 어떻게 이어갈지 | 물품의 실제 위치, 직원 대체·원격/현장 대응 시간 | RACI, 당직·출동, 인계 원장, 재개 승인 |
| 확대와 중단을 언제 결정할지 | 기준선·성과·개입·전체 비용·잔여 위험 | 인수 기준, 확대/축소 관문, 계약 종료·데이터 반출 조건 |

## PM이 이해할 것과 전문 검토에 넘길 것

[의견] PM이 직접 설명하고 요구할 수준과, 전문 담당자가 검토할 범위를 나눈다.

| 주제 | PM이 설명하고 요구할 수준 | 전문 담당자 검토 범위 |
|---|---|---|
| 이동·인지 | 운동학과 회전 외곽, 센서 한계, 위치 상실이 업무에 주는 영향 | 구동·보행 제어, 추정 알고리즘, 제동·안정성, 센서 융합 |
| ROP·API | 상태·id·중복·기한·권한·소유권·물리 완료 증거 | 분산 일관성, 구체 어댑터, 성능, 보안 구현 |
| 안전 | 위험, 금지 조건, 운영 중지·재개, 증거의 부족 | 제품·시스템 안전 설계, 적용 표준, 시험 수치, 인증 |
| 시설·통신 | 승강기·문 모델, 권한, 장애 모드, 무선 음영, 비용 | 제어반·전기 공사, 인터록, 검사, RF·보안 구성 |
| 사업·법 | TCO, 분모, 현금화, SLA, 책임, 영상 목적·접근 | 견적, 보험 조건, 계약·법률, 개인정보, 노무 적용 판단 |

## 근거 표기

이 스터디도 [스터디](../index.md) 공통 표기를 따른다. 제품 사양·기능은 "[추정] 벤더 주장:", NAVER·BMW처럼 운영 주체가 낸 소개·보도자료는 "[추정] 운영기관 보고:"로 쓴다. 둘 다 독립 검증이나 감사 결과가 아니다. 표준·법령·공식 문서·연구는 원문을 열어 확인한 범위에서 [사실]과 각주를 붙인다. 서비스 설계·적합성·권한·계약·경제성 계산·시험 항목은 모두 [의견]이다. 설계 예시와 가상 계산은 표준 명세·제품 구현·측정 성과가 아니다. 자료 번호 S01~S18은 이 스터디 안에서만 쓰는 번호이며, 현장 적용·운영 검증 스터디의 S번호와 다르다.

## 페이지 구성

| 페이지 | 과제 | 다루는 것 |
|---|---|---|
| [핵심 학습 자료](core-materials.md) | ①②③ | 학습 단위 18개의 기관·판·일자·읽을 절·한계와 열람 실패 기록, 보조 연습 |
| [로봇 선택과 서비스 설계](robots-and-services.md) | ①③ | 4휠·4족 제품 비교, 서비스별 적합성과 이종 도입 조건, 역할별 권한, 순찰·배송·안내의 6단계 흐름 |
| [사업 모델과 경제성](business-model-and-roi.md) | ① | 계약 모델, TCO 항목, KPI 정의, 가상 ROI 계산 템플릿 |
| [ROP 책임 경계와 연동 계약](architecture-and-contracts.md) | ② | 공식 자료가 해결하는 범위, 구성도, 책임 경계, 식별자·상태, 배송 시퀀스, API·이벤트 예시, 시설·통신·보안·LLM |
| [현장 구축과 인수시험](deployment-and-acceptance.md) | ③ | 구축 8단계, 현장 조사표, RACI, 수치 기준의 출처 구분, 시험 14개, 장애 대응, 국내 법령 적용 범위 |
| [학습 순서](learning-plan.md) | — | 2시간·1일·1주 계획과 근거 카드 |
| [발표 구성과 예상 질문](presentation-and-questions.md) | — | 두 항목 조합, 15분 9장 구성, 예상 질문 10개, 추가 확인 과제 |

## 기존 분류와의 관계

이 스터디는 [스터디](../index.md) 섹션 안의 한 묶음이며 67개 세부 연구영역을 바꾸지 않는다. 현장 조건·실패 사례·제조사 피드백·시뮬레이션 검증은 같은 섹션의 [현장 적용·운영 검증](../field-readiness-rop/index.md) 스터디가 더 깊게 다루므로 그 페이지로 연결하고 다시 쓰지 않는다. 세부 영역과의 연결은 각 페이지 끝의 "연결 영역"에 있다.

## 공개 범위와 싣지 않은 것

- 면접 대상 회사·직무, 개인의 이력, 특정 고객 현장은 다루지 않는다. 빌딩은 조사용 가정이다.
- 제품 가격·견적은 공개 페이지에 없어 싣지 않았다. 과거 기사의 가격을 현재 국내 도입가로 쓰지 않는다.
- ISO 13482·ISO 3691-4는 공개 초록만 읽었다. 유료 전문의 수치·절차·인증 판정을 쓰지 않는다.
- 가상 ROI 계산의 금액은 학습 예시이며 어떤 제품의 견적도 아니다.
- 법령은 열람한 판의 현행 조문이다. 개별 건물·사업·제품에 대한 적용 판정은 하지 않았다.

## 조사 이력

| 날짜 | 내용 |
|---|---|
| 2026-10-12 | 외부 조사(PM 학습 가이드, 문서 6개)를 공개 출처 원문·위키 내부 연결과 대조한 뒤 8개 페이지로 게시 |

[^ref-1592]: Robotnik Automation, Robotnik Datasheet RB-SUMMIT 2024 EN (CF 06.24, Standard version), 2024-06, https://robotnik.eu/wp-content/uploads/2024/05/Robotnik_Datasheet_RB-SUMMIT_2024_EN.pdf, 접근일 2026-10-12
[^ref-1597]: Boston Dynamics (Spot SDK docs), Payload Configuration Requirements (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/payload/payload_configuration_requirements.html, 접근일 2026-10-12
[^ref-1595]: Boston Dynamics, Spot — The Agile Mobile Robot (제품 페이지), 2024-06-24, https://bostondynamics.com/products/spot/, 접근일 2026-10-12
[^ref-1596]: Boston Dynamics (Spot SDK docs), About Spot — Robot specifications (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/concepts/about_spot.html, 접근일 2026-10-12
[^ref-1591]: Robotnik Automation, RB-SUMMIT — Mobile Robot ideal for R&D applications (제품 페이지), 2020-05-29, https://robotnik.eu/products/mobile-robots/rb-summit/, 접근일 2026-10-12
[^ref-1599]: NAVER Corp., 1784 — Service (Rookie, ROBOPORT, ARC System, Works assistant), 미확인, https://www.navercorp.com/en/service/1784, 접근일 2026-10-12
[^ref-1600]: BMW Group PressClub (UK), "Good boy SpOTTO": robot dog scans and monitors manufacturing equipment at BMW Group Plant Hams Hall, 2024-05-07, https://www.press.bmwgroup.com/united-kingdom/article/detail/T0441735EN_GB/%E2%80%9Cgood-boy-spotto%E2%80%9D%3A-robot-dog-scans-and-monitors-manufacturing-equipment-at-bmw-group-plant-hams-hall?language=en_GB, 접근일 2026-10-12
[^ref-1589]: Teledyne FLIR, Measuring temperatures (FLIR 사용 설명서 T810605, latest), 미확인, https://docs.flir.com/T810605/en-US/latest/s10.html, 접근일 2026-10-12
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-12
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-12
[^ref-1580]: NIST, Performance of Emergency Response Robots, 2014-04-28, https://www.nist.gov/programs-projects/performance-emergency-response-robots, 접근일 2026-10-12
