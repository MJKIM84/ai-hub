---
title: "62. 제조 공장"
type: area
category: "Q. 현장 유형별 적용"
area_no: 62
related_areas: [1, 12, 21, 23, 25, 26, 30, 31, 32, 34, 35, 44, 49, 50]
tags: [VDA 5050, 조립라인 공급, 협동로봇, ISA-95, 셀 생산 방식, 이기종 플릿 관제]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-257, ref-922, ref-923, ref-924, ref-925, ref-926, ref-927, ref-928, ref-930, ref-931, ref-932, ref-933, ref-934, ref-935, ref-936, ref-938]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 62. 제조 공장

# 62. 제조 공장

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]

## 3. 왜 중요한가

제조 공장은 생산 계획이 정한 순서와 시각에 맞춰 여러 로봇이 부품을 나르고 조립해야 하는 현장이며, 대량 맞춤화와 제품 다양성이 커지면서 조립라인에 부품을 어떤 방식으로 공급할지 정하는 문제가 약 25년 전부터 별도 연구 분야로 자리 잡았다(2019년 서베이 기준). [사실][^ref-922] 이 문제는 로봇 한 대의 주행 성능이 아니라 어느 부품을 어떤 정책(라인 적재·상자 공급·순서 공급·키팅)으로 어느 스테이션에 보내는가 하는 전술적 결정이므로, 플랫폼이 생산 관리와 어긋나면 로봇이 많아도 결품과 막힘으로 라인이 멈춘다는 점에서 이 영역의 핵심 질문과 직결된다. [추정][^ref-922][^ref-936]

자세한 내용은 주제 페이지 [62. 제조 공장 — 왜 중요한가](../../topics/2026/2026-09-29-area62-s3.md)에 있다.

## 4. 핵심 개념과 용어

**조립라인 공급 문제(Assembly Line Feeding Problem, ALFP)** — 조립라인의 각 부품을 라인 적재·상자 공급·순서 공급·정치식 키팅·이동식 키팅 같은 공급 정책 가운데 어디에 배정할지 정하는 전술적 의사결정 문제로, 대량 맞춤화와 제품 다양성이 커지면서 연구가 늘었다(2019년 기준). [사실][^ref-922]
- **라인 공급 정책(line feeding policy)** — 라인 적재(line stocking)·상자 공급(boxed-supply)·순서 공급(sequencing)·키팅(kitting)처럼 부품이 스테이션에 놓이는 방식을 뜻한다. [사실][^ref-922]

자세한 내용은 주제 페이지 [62. 제조 공장 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area62-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 세 사례는 모두 현장 유형이 제조 공장이며, 실제 도입·연구 사례를 출처와 함께 정리한 것이다. 성과 수치는 모두 회사 설명이라 독립 확인이 없고, 완료·인계 항목은 ISA-95 기반 모델의 계획 재통합 연구와 자재 관리 시스템의 운송 주문 생성 설명에서 도출한 추정이다. [추정][^ref-925][^ref-926]

**현장 유형:** 제조 공장

**사례:** 자동차 조립 공장에서 트럭 하역장의 부품 랙을 조립라인으로 공급 (폭스바겐 하노버, BMW 그룹)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 자재 관리 시스템이 생산 계획과 칸반에 따라 운송 주문을 자동 생성해 플릿에 보낸다. [추정] 벤더 주장[^ref-926] 하노버 공장에서는 적시(Just-in-Time, JIT)·순서 맞춤(Just-in-Sequence, JIS) 공급 호출이 운반을 일으킨다. [추정] 벤더 주장[^ref-924] |
| 작업 대상 | 부품 랙과 상자. [추정] 벤더 주장[^ref-924] 어느 부품을 어떤 공급 정책으로 보낼지는 조립라인 공급 문제로 정한다. [사실][^ref-922] |
| 수행 자원 | SYNAOS 는 MLR 언더라이드 로봇 약 100대와 괴팅·린데 자율 견인차 40대 등 135대 이상을 제조사 독립 플랫폼이 VDA 5050 으로 관제한다고 설명한다(회사 설명). [추정] 벤더 주장[^ref-924] BMW 그룹 물류기획 책임자(Head of Logistics Planning) Peter Kiermaier 는 스마트 운반 로봇·자율 견인차·자율 지게차 프로젝트에 VDA 5050 을 적용하고 신규 무인 운반차(Automated Guided Vehicle, AGV) 시스템 입찰의 표준으로 삼았다고 밝혔다. [추정] 벤더 주장[^ref-923] |
| 제약 | 무인 산업 차량의 사람 감지·제동·속도 제어·안정성·운용 구역 분류 요구(ISO 3691-4:2023, 인증 기관 안내 기준이며 표준 원문은 미열람). [추정] 벤더 주장[^ref-938] |
| 완료·인계 | 스테이션 도착·하역 확인과 생산 시스템으로의 상태 보고(도출 추정). [추정][^ref-925][^ref-926] |
| 예외·성과 | 하루 9,000개 랙 운반과 연 약 30만 km 주행은 회사 설명이다. [추정] 벤더 주장[^ref-924] 실패 시 복구 주체는 출처에 없어 미확인이다. |

이 사례에서 이 영역이 관여하는 자리는 시작 조건과 수행 자원이다. 운송 주문은 생산 관리 쪽에서 오고 로봇은 제조사가 여럿이므로, 표준 인터페이스로 배정·관제하는 계층이 두 항목 사이에 놓인다. 다만 SYNAOS 글에는 제조 실행 시스템 연동의 세부가 없고 수치는 모두 업체 설명이다. [추정] 벤더 주장[^ref-924]

**현장 유형:** 제조 공장

**사례:** 자동차 공장에서 차체·조립체를 라인과 버퍼 창고 사이로 운반 (국내 시뮬레이션 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 생산라인 사이의 도어·후드·트렁크 조립체 공급 요구와, 도장 라인 정지 같은 라인 사건. [사실][^ref-935][^ref-936] |
| 작업 대상 | 도어·후드·트렁크 조립체와 차체. [사실][^ref-935][^ref-936] |
| 수행 자원 | 유인 견인차를 대체하는 AGV, 통합창고의 스태커 크레인과 AGV. [사실][^ref-935][^ref-936] |
| 제약 | 단일 차선 양방향 AGV 도로의 타당성, 적정 AGV 대수, 투자 타당성(2014-04). [사실][^ref-935] |
| 완료·인계 | 초록에서 확인되지 않음(미확인). |
| 예외·성과 | 차체 버퍼 창고(WBS·PBS)가 따로 운영되면 결품(starvation)과 막힘(blocking)이 생기며, 통합창고 모형이 도장 라인 정지 상황에서 기존 창고보다 효율적이었다(2012). [사실][^ref-936] |

두 연구는 로봇을 투입하기 전에 시뮬레이션으로 대수·도로·운영 방식을 정한 사례로, 가정한 미래를 실험한다는 점에서 34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계의 방법을 제조 공장에 적용한 것이다. [추정][^ref-935][^ref-936]

**현장 유형:** 제조 공장

**사례:** 셀과 라인에서 작업자·협동로봇·모바일 매니퓰레이터가 함께 하는 조립 공정 (LG전자 창원, 현대자동차그룹 싱가포르 글로벌 혁신센터(HMGICS), 유럽 전문가 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출처에 작업 발생 조건이 없어 미확인이다. |
| 작업 대상 | 차량 지붕 같은 무거운 부품과 작업자에게 전달할 공구·부품. [사실][^ref-928] 타원형 셀에서 동시에 생산하는 여러 차종. [추정] 벤더 주장[^ref-930] |
| 수행 자원 | 협동로봇이 무거운 부품을 받쳐 주고 공구·부품을 골라 가져다준다. [사실][^ref-928] HMGICS 는 셀에서 작업자와 로봇이 함께 일한다. [추정] 벤더 주장[^ref-930] LG전자는 자체 자율이동로봇(Autonomous Mobile Robot, AMR)과 AMR 에 로봇팔을 결합한 자율주행 수직다관절로봇(MM)으로 부품·자재 공급을 맡기고, MM 이 조립·불량 검사와 다른 AMR 의 배터리 교체까지 할 수 있다고 설명한다. [추정] 벤더 주장[^ref-927] |
| 제약 | 좁은 조립 공간에서 협동로봇끼리, 그리고 외골격과의 충돌을 예측·회피하는 것이 핵심 안전·기술 과제다(유럽 전문가 31명 조사, 2024-12-02). [사실][^ref-928] 작업자 안전과 일자리 대체 우려가 함께 다뤄져야 한다. [사실][^ref-933] |
| 완료·인계 | 도출 추정(첫 사례와 같음). [추정][^ref-925][^ref-926] |
| 예외·성과 | LG전자는 창원 공장에서 생산성 17% 향상, 에너지 효율 30% 개선, 품질 비용 70% 절감을 냈다고 밝혔다(회사 설명). [추정] 벤더 주장[^ref-927] HMGICS 는 연 3만 대 이상의 전기차를 생산할 수 있다고 밝혔다(회사 설명). [추정] 벤더 주장[^ref-930] |

LG전자는 이 솔루션이 그룹 40여 지역 60여 곳 생산기지에 적용됐고 사업 첫해인 2024년 외부 업체 공급 규모가 2,000억 원 수준이라고 밝혔으나, 기사에 제조 실행 시스템 같은 생산 관리 시스템 이름은 없다. [추정] 벤더 주장[^ref-927] HMGICS 는 디지털 트윈 메타 팩토리를 갖췄다고 소개되는데, 이는 회사 발행 자료의 설명이며 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽으로만 읽는다. [추정] 벤더 주장[^ref-930] 국내 중소 제조 현장에서는 정부의 'AI 공장장' 사업이 2026년 개별 물류 작업에서 2027년 물류공정 확대, 2028년 생산 전 공정, 2029년 '다크팩토리 OS'로 범위를 넓힐 계획이며, 기사에 자연어·언어 모델 지시는 언급되지 않는다. [사실][^ref-931]

## 6. 대표 접근법과 기술

확인한 자료를 종합하면 제조 공장의 로봇 작업은 (1) 창고·슈퍼마켓에서 조립 스테이션으로 부품을 옮기는 라인 공급, (2) 차체·조립체를 라인과 버퍼 사이에서 옮기는 공정 간 운반, (3) 셀 안에서 작업자와 로봇이 함께 조립하거나 두 대 이상의 로봇(로봇팔·이동 플랫폼)이 치구 없이 조립하거나 협동로봇이 부품 지지·공구 전달을 맡는 여러 로봇 공정 작업의 세 형태로 들어간다. [추정][^ref-922][^ref-935][^ref-924][^ref-936][^ref-930][^ref-934][^ref-928][^ref-927]

자세한 내용은 주제 페이지 [62. 제조 공장 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area62-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준 목록 전체는 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [62. 제조 공장 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area62-s7.md)에 있다.

## 8. 대표 연구와 자료

Schmid, N. A., & Limère, V., A classification of tactical assembly line feeding problems(2019) — 조립라인 공급 문제를 여러 차원으로 분류해 실무 문제와 학술 해법을 잇는 틀. [사실][^ref-922] 이 영역에서 라인 공급 작업을 나누는 기준으로 참고할 수 있다는 것은 추론이다. [추정][^ref-922]

자세한 내용은 주제 페이지 [62. 제조 공장 — 대표 연구와 자료](../../topics/2026/2026-09-29-area62-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 제조 실행 시스템(Manufacturing Execution System, MES) 같은 생산 관리·자재 관리 시스템(ISA-95 의 3계층)이 내는 운송·공정 작업 요청을 받아 실행하고, 도착·하역·조립 완료를 확인해 결과를 돌려준다. [추정][^ref-925][^ref-926] | 생산 계획·재고·칸반 규칙의 판단은 MES·전사 자원 계획(Enterprise Resource Planning, ERP)이 맡는다(연계 대상). [추정][^ref-926] |
| 로봇 자체 지능·제어 | 제조사가 다른 AGV·견인차·AMR·모바일 매니퓰레이터에 VDA 5050 같은 표준 인터페이스로 작업을 배정하고 상태·실패·완료를 확인한다. [추정][^ref-923][^ref-924] | 무인 운반차의 사람 감지·제동 같은 안전 기능, 협동로봇의 힘 제한·충돌 회피, 로봇팔의 조립 동작·동기화는 로봇 제조사가 맡는다(연계 대상). [추정][^ref-938][^ref-928][^ref-934] |
| 시설·설비 제어 | 컨베이어·스태커 크레인·버퍼 창고에 작업 요청·예약·인계·상태 확인을 건다. [추정][^ref-936] | 컨베이어·스태커 크레인·프로그래머블 로직 컨트롤러(Programmable Logic Controller, PLC) 설비 제어 자체는 설비 업체가 맡는다(연계 대상). [추정][^ref-936] |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 생산 관리 요청 수신, 표준 인터페이스로 이기종 로봇 배정, 셀·라인 사이의 교통과 순서 조율, 완료 확인과 결과 반환, 그리고 라인 정지·결품 같은 예외를 받아 재계획하는 것까지이며, 이를 하나의 계층에서 묶은 국내 공개 사례는 확인되지 않았다. [추정][^ref-923][^ref-924][^ref-925][^ref-926][^ref-936] 이 경계는 제품 전략에 따라 이동할 수 있으나, 이종 제조사를 연결하는 ROP 는 생산 계획 판단·설비 제어·안전 기능 성능을 MES 업체·설비 업체·로봇 제조사에 맡기고 인터페이스와 실행 보장을 담당하는 것이 [범위 경계](../../about/scope-boundary.md)의 취지에 맞는다. [추정][^ref-926][^ref-938][^ref-928]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md) — 독일 자동차 산업이 VDA 5050 을 개발하고 완성차 업체가 마스터 컨트롤 업체를 지원·분사시켜 채택을 이끈 시장 동향. [사실][^ref-257]

자세한 내용은 주제 페이지 [62. 제조 공장 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area62-s10.md)에 있다.

## 11. 열린 질문

**oq-142** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-12) 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가? — 이번 조사에서도 제조 공장의 운영 사례는 확인되지 않았으며, 확인된 국내 자료는 자연어 입력으로 로봇을 제어하는 한국전자기술연구원(KETI)의 전시 시연과 자연어 지시가 언급되지 않은 정부 'AI 공장장' 시범사업뿐이다. [추정][^ref-932][^ref-931]

자세한 내용은 주제 페이지 [62. 제조 공장 — 열린 질문](../../topics/2026/2026-09-29-area62-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-257]: Interact Analysis (Rueben Scriven), AMR Multi-Fleet Orchestration Software Explained, 2023-01, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-29 (원문 미열람)
[^ref-922]: Schmid, N. A., & Limère, V. (International Journal of Production Research 57(24)), A classification of tactical assembly line feeding problems, 2019-02-23, https://www.tandfonline.com/doi/full/10.1080/00207543.2019.1581957, 접근일 2026-09-29
[^ref-923]: Verband der Automobilindustrie (VDA), VDA 5050: Managing Transport in Manufacturing Plants, 미확인, https://www.vda.de/en/news/articles/vda-5050, 접근일 2026-09-29
[^ref-924]: SYNAOS (IoT Use Case), VDA 5050: unified AGV fleet control in real time at VW, 2025-10-16, https://www.iotusecase.com/en/solution-examples/vda-5050-agv-fleet-control, 접근일 2026-09-29
[^ref-925]: Wally, B., Vyskočil, J., Novák, P., Huemer, C., Šindelář, R., Kadera, P., Mazak, A., & Wimmer, M., Flexible Production Systems: Automated Generation of Operations Plans Based on ISA-95 and PDDL, 2019-11-13, https://arxiv.org/abs/1911.05481, 접근일 2026-09-29
[^ref-926]: Siemens, AGV fleet management integration with intralogistics, 미확인, https://resources.sw.siemens.com/en-US/white-paper-integrating-agv-automated-guided-vehicle-system-with-intralogistics/, 접근일 2026-09-29
[^ref-927]: 물류신문 (이경성), LG전자, 스마트팩토리 솔루션 확대에 AMR 등 물류로봇 적극 활용한다, 2024-07-18, https://www.klnews.co.kr/news/articleView.html?idxno=313143, 접근일 2026-09-29
[^ref-928]: Pietrantoni, L., Favilla, M., Fraboni, F., Mazzoni, E., Morandini, S., Benvenuti, M., & De Angelis, M. (Frontiers in Robotics and AI), Integrating collaborative robots in manufacturing, logistics, and agriculture: Expert perspectives on technical, safety, and human factors, 2024-12-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1342130/full, 접근일 2026-09-29
[^ref-930]: 현대자동차그룹, ‘혁신의 장場’ HMGICS, 인간 중심 모빌리티 솔루션의 새 시대 열다, 2023-11-21, https://www.hyundaimotorgroup.com/ko/news/hmgics-human-centric-mobility-solutions-new-era, 접근일 2026-09-29
[^ref-931]: 뉴시스, "로봇 몇 대, 어디로 움직일까"…중소 제조현장에 'AI 공장장' 뜬다, 2026-09-07, https://www.newsis.com/view/NISX20260907_0003779780, 접근일 2026-09-29
[^ref-932]: 테크데일리, KETI, LLM 모델 및 모방학습, 조립공정 자동화 기술 공개, 2025-03-12, https://www.techdaily.co.kr/news/articleView.html?idxno=25352, 접근일 2026-09-29
[^ref-933]: Keshvarparast, A., Battini, D., Battaia, O., & Pirayesh, A. (Journal of Intelligent Manufacturing 35), Collaborative robots in manufacturing and assembly systems: literature review and future research agenda, 2023-05-30, https://link.springer.com/article/10.1007/s10845-023-02137-w, 접근일 2026-09-29
[^ref-934]: Marvel, J. A., Bostelman, R., & Falco, J. (NIST; ACM Computing Surveys 51), Multi-Robot Assembly Strategies and Metrics, 2018-01-01, https://dl.acm.org/doi/10.1145/3150225, 접근일 2026-09-29
[^ref-935]: 강명훈, 곽춘종 (부산대학교; Asia-Pacific Journal of Business & Commerce), 시뮬레이션을 이용한 자동차 부품 공급 시스템 도입 방안 분석: R자동차 사례, 2014-04, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02448280, 접근일 2026-09-29
[^ref-936]: 옥창훈, 김득수, 공정수, 서윤호 (고려대학교, 현대자동차; 한국시뮬레이션학회 논문지 21(2)), 자동차 생산을 위한 통합창고 연구, 2012, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001671601, 접근일 2026-09-29
[^ref-938]: Applus+ Laboratories, ISO 3691-4:2023: Compliance Testing for Automated Guided Vehicles (AGVs), 미확인, https://www.appluslaboratories.com/global/en/what-we-do/service-sheet/iso-3691-4-2023-compliance-testing-for-automated-guided-vehicles-agvs, 접근일 2026-09-29
