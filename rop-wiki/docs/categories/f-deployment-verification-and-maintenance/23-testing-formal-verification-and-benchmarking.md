---
title: "23. 시험·형식 검증·벤치마크"
type: area
category: "F. 도입·검증·유지관리"
area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [장애 주입, 회귀 시험, 형식 검증, 런타임 검증, 벤치마크]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-008, ref-528, ref-529, ref-599, ref-600, ref-601, ref-602, ref-186, ref-603, ref-604, ref-470, ref-605, ref-606, ref-607, ref-608, ref-609, ref-406]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 23. 시험·형식 검증·벤치마크

# 23. 시험·형식 검증·벤치마크

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [분류원문]

## 2. SCM 관점의 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]

## 3. 왜 중요한가

로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며, 로봇 실무자 면담 연구는 시험 실무 12가지와 어려움 9가지를 도출해 실세계 복잡성, 커뮤니티와 표준, 구성요소 통합의 세 주제로 묶었다. [사실][^ref-600] 저자들은 이 연구를 로봇 시스템 시험에 초점을 둔 첫 연구로 소개했다. [사실][^ref-600]

자율 로봇 시스템은 복잡하고 혼성적이며 안전이 중요한 경우가 많아, 시험과 시뮬레이션에만 기대서는 정확성을 보장하거나 인증 근거를 대기에 부족하다는 지적이 있다. [사실][^ref-599] 이 때문에 형식 명세·검증의 과제와 접근법을 정리한 조사 연구가 나왔다. [사실][^ref-599]

물류 현장의 다중 로봇 계획도 같은 문제를 안고 있다. 기존 [다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)](../../glossary/mapf.md) 연구는 단순화한 운동 모델과 완전한 실행·통신을 가정한다는 한계가 지적되어, [플릿 관리 시스템(Fleet Management System, FMS)](../../glossary/fleet-management-system.md) 안에서 알고리즘을 평가하는 시험대가 제안됐다. [사실][^ref-604] Open-RMF 시뮬레이션 문서는 드물지만 심각한 예외 상황과 장시간 운전을 배치 전에 시뮬레이션으로 시험할 수 있다고 설명한다(2026-09-25 확인). [사실][^ref-406]

## 4. 핵심 개념과 용어

이 영역은 장애를 계획적으로 넣어 보는 시험, 변경 뒤 다시 돌리는 시험, 수학적 모델로 성질을 확인하는 검증, 운영 중 감시, 공통 기준으로 비교하는 벤치마크를 함께 다룬다. [사실][^ref-528][^ref-601]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area23-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹

**시나리오:** 플릿 어댑터 업데이트 뒤 피킹 운반 중 로봇 정지 장애를 넣는 회귀 시험

| 항목 | 내용 |
|---|---|
| 시작 조건 | [플릿 어댑터](../../glossary/fleet-adapter.md) 업데이트가 반영되어 회귀 시험을 시작한다(가상 시나리오). |
| 작업 대상 | 피킹한 화물을 실은 운반구와 그 운반 작업(시뮬레이션 안). |
| 수행 자원 | 시뮬레이션 속 로봇, 장애를 넣는 주입 도구, 합격·불합격을 내는 단정. ROP 는 재배정·복구 동작을 시험하는 몫을 맡는 것으로 보인다. [추정][^ref-601][^ref-406] |
| 제약 | 재배정 과정에서 교착·제약 위반이 없어야 한다는 조건을 판정에 넣는 예시다. 교착 검증의 근거 자료는 원문 미열람 사례 연구다. [추정][^ref-609] |
| 완료·인계 | 작업이 다른 로봇에 재배정되는지, 완료 확인 전에는 재고 변경이 확정되지 않는지를 단정으로 확인한다. [추정][^ref-528][^ref-601] |
| 예외·성과 | 장애 시나리오의 합격 여부와 함께 완료·시간·비용 지표를 판정 기준으로 둘 수 있을 것으로 보인다. [추정][^ref-528][^ref-529] |

다음은 설명을 위한 가상의 시나리오이다. 피킹 단계에서 플릿 어댑터를 업데이트한 뒤, 운반 중인 로봇이 멈추는 장애를 주입하고 작업 재배정과 재고 변경 확정 시점(완료·인계)을 단정으로 확인하는 회귀 시험을 구성할 수 있을 것으로 보인다. [추정][^ref-528][^ref-601] 실제 사례가 아니며 현장 수치는 넣지 않는다.

2절의 질문에 대해서는, 반복 가능한 시뮬레이션 시나리오에 장애 주입과 합격 판정 단정을 붙여 지속적 통합에서 변경마다 다시 돌리는 방식이 답이 될 것으로 보인다. [추정][^ref-528][^ref-601][^ref-406] 다만 물류 오케스트레이션 소프트웨어에 이를 적용해 결과를 공개한 현장 사례는 찾지 못했다. [추정][^ref-406]

## 6. 대표 접근법과 기술

대표 접근법은 장애 주입형 시험과 채점, 시뮬레이션 기반 회귀 시험, 형식 검증, 런타임 검증, 현실 조건을 넣은 벤치마크다. [사실][^ref-528][^ref-602]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area23-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 자료는 평가 프로그램, 차량·로봇 단위의 안전·성능 표준과 국내 시험기관, 오픈소스 시험 도구로 나뉜다. [사실][^ref-008][^ref-470][^ref-601]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area23-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 형식 검증 조사, 로봇 시험 실무 연구, MAPF 벤치마크 정의, 대회와 현실적 시험대, 창고 AGV 교착 사례 연구다. [사실][^ref-599][^ref-609]

- Luckcuck 외, 자율 로봇 시스템의 형식 명세와 검증 조사(2019) — 시험·시뮬레이션만으로는 부족하다는 문제의식에서 형식 방법의 과제·형식체계·접근법을 분류했다. [사실][^ref-599]
- Afzal 외, 로봇 시스템 시험의 어려움 연구(ICST 2020) — 면담으로 시험 실무 12가지와 어려움 9가지를 도출했다. [사실][^ref-600]
- Stern 외, MAPF 정의·변형·벤치마크(2019) — 가정과 목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했다. [사실][^ref-186]
- League of Robot Runners 대회 목표·설계 소개(ICAPS 2024 시스템 시연) — 벤치마크 인스턴스 개발과 최신 성과 추적을 목표로 한다. [사실][^ref-603]
- Yan 외, LSMART와 지속형 AGV 플릿 관리 설계 선택 연구(2026) — 단순 운동 모델·완전 실행 가정을 넘어 FMS 안에서 계획 시점·방법·복구를 비교했다. [사실][^ref-604]
- von Berg·Aichernig·Wedenik, 창고 AGV 의 BDD 기반 교착 회피(FM 2026 사례 연구) — 전이 시스템 인코딩 세 가지를 BDD 로 분석했다. [사실][^ref-609]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP 가 직접 맡을 시험 몫은 오케스트레이션 논리와 인터페이스, 장애 대응이고, 로봇 자체의 안전·주행 성능 시험은 제조사와 시험기관 쪽 연계 대상으로 보인다. [추정][^ref-601][^ref-470]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 작업 배정·교통 관리 논리의 교착·제약 위반 검증, 관제 인터페이스 적합성, 장애 주입 시 재배정·복구 동작의 회귀 시험, 운영 중 런타임 감시로 보인다. [추정][^ref-609][^ref-601][^ref-602][^ref-406] | 연계 대상: 사람 감지·안정성 같은 로봇 자체 안전 검증과 주행·도킹·이동 성능 시험은 제조사와 시험기관 영역이고, ROP 는 그 결과를 로봇 등록·배정 조건의 입력으로 받는 쪽으로 보인다. [추정][^ref-470][^ref-605][^ref-606][^ref-607] |

표의 교착 검증 부분 근거인 창고 무인운반차(Automated Guided Vehicle, AGV) 사례 연구는 원문 미열람 자료다. [사실][^ref-609] ISO 3691-4:2023 은 AGV·자율이동로봇(Autonomous Mobile Robot, AMR)을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정하며(세부 시험 항목 미확인), 로봇 쪽 안전 검증의 연계 대상이다. [사실][^ref-470]

연계 대상: ros2_fault_injection 은 README 기준으로 오도메트리·레이저 스캔·관성 측정 장치(Inertial Measurement Unit, IMU)·점군 같은 센서 신호를 장애 주입 대상으로 다루고, 속도 명령(Twist)은 센서가 아니라 명령 조작 대상으로 둔다. [사실][^ref-601] 이런 센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하는 것으로 보인다. [추정][^ref-601] ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. [추정][^ref-601]

OTTO by Rockwell Automation 은 자사 AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 와 VDA 5050 인증을 마쳤다고 2026년 4월 발표했으며, 인증의 시험 항목은 미확인이다. [추정] 벤더 주장[^ref-608] 이번 조사에서 공식 적합성 시험 절차를 찾지 못했으므로(부재가 확인된 것은 아니다), ROP 는 새 로봇 연동마다 자체 인수 시험을 둘 필요가 있는 것으로 보인다. [추정][^ref-608]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계의 전체 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시뮬레이션 환경을 22. 시뮬레이션·예측용 디지털 트윈과 공유하고, 시험 대상 논리와 표준을 여러 영역에서 받는다는 것이 구축자 의견이다. [의견][^ref-406]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area23-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 부분 근거만 얻었거나 새로 제기된 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 열린 질문](../../topics/2026/2026-09-25-area23-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [23. 시험·형식 검증·벤치마크](23-testing-formal-verification-and-benchmarking.md) — 영역 심화: 3~11절 신규 작성(4·6·7·10·11절은 주제 페이지로 분리), 2차 수정: 9절 f8 태그 분리, 3절 첫 문장 범위 정정, 10절 요약 의견 주체 표시, 3·9절 약어 풀이 (실행 2026-09-25-59)
- 2026-09-25 · 생성 · [23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area23-s6.md) — 자동 분리: 23. 시험·형식 검증·벤치마크 의 "6. 대표 접근법과 기술" 절을 옮겼다(2차 수정 없음) (실행 2026-09-25-59)
- 2026-09-25 · 생성 · [23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area23-s7.md) — 자동 분리: 23. 시험·형식 검증·벤치마크 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 없음) (실행 2026-09-25-59)
- 2026-09-25 · 생성 · [23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area23-s4.md) — 자동 분리: 23. 시험·형식 검증·벤치마크 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차 수정: 적합성 시험 항목에 '벤더 주장' 병기 (실행 2026-09-25-59)
- 2026-09-25 · 생성 · [23. 시험·형식 검증·벤치마크 — 열린 질문](../../topics/2026/2026-09-25-area23-s11.md) — 자동 분리: 23. 시험·형식 검증·벤치마크 의 "11. 열린 질문" 절을 옮겼다(2차 수정 없음) (실행 2026-09-25-59)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-529]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Scoring, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html, 접근일 2026-09-25
[^ref-599]: Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M., Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019-09, https://arxiv.org/abs/1807.00048, 접근일 2026-09-25 (원문 미열람)
[^ref-600]: Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S., A Study on Challenges of Testing Robotic Systems, 2020, https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc, 접근일 2026-09-25 (원문 미열람)
[^ref-601]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-602]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-603]: IDM Lab (USC) 게재 초록, 저자 미확인, The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration], 2024, https://idm-lab.org/bib/abstracts/Koen24p.html, 접근일 2026-09-25 (원문 미열람)
[^ref-604]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-605]: NIST, ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles, 미확인, https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-606]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-607]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-609]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
