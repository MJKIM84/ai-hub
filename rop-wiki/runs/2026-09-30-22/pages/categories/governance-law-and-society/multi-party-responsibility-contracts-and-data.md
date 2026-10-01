---
title: "58. 다사업자 책임·계약·데이터"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 58
related_areas: [2, 3, 13, 20, 21, 22, 37, 47, 52, 53, 57, 59, 63, 65]
tags: [데이터 접근 계약, 실질적 변경, API 폐기 정책, 서비스 수준 협약, 감사 추적]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-872, ref-1191, ref-1192, ref-1193, ref-1194, ref-1204, ref-555, ref-1205, ref-1206, ref-1207, ref-317, ref-1208, ref-1209, ref-1210, ref-1211, ref-1212]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 58. 다사업자 책임·계약·데이터

# 58. 다사업자 책임·계약·데이터

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

책임과 변경 승인, 데이터 소유권, API 변경 정책, 서비스 수준·감사 이력 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다사업자 책임·변경 승인**: 연동 오류를 누가 고치고 변경을 누가 승인할지 정한다
- **데이터 소유권**: 운영 데이터를 누가 갖고 어디까지 쓸 수 있는지 정한다
- **API 변경 정책**: 제조사와 플랫폼의 API가 바뀔 때 호환성과 공지 방식을 정한다
- **서비스 수준·감사 이력**: 서비스 수준 약속과 감사 이력을 정하고 지킨다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’에서 왔다. 그 본문은 [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]

## 3. 왜 중요한가

여러 사업자가 함께 운영하는 현장에서 연동 오류를 누가 고치고 변경을 누가 승인하는지를 한 번에 정한 공개 표준이나 책임 분담표는 이번 조사(2026-09-30 기준)에서 찾지 못했고, 실제 규칙은 변경한 주체에게 제조자·제공자 의무를 지우는 법 규정, 인터페이스 표준의 버전·폐기 규칙, 서비스 수준 협약·표준 계약 조항과 통합자 사전 자격 같은 계약·조달 장치가 겹쳐 정해지는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-031][^ref-1204][^ref-1205][^ref-1192][^ref-1206][^ref-872]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 왜 중요한가](../../topics/2026/2026-09-30-area58-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 책임이 넘어가는 조건, 데이터 권리, 인터페이스 변경 예고, 서비스 약속과 기록의 네 묶음으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area58-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 싱가포르 공공 의료기관의 로봇·소프트웨어·IoT 연동을 등재 통합자에게 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 공공 의료기관이 로봇·소프트웨어·IoT를 연동하려 할 때 [사실][^ref-872] |
| 작업 대상 | 로봇·소프트웨어·IoT와 의료 로봇 미들웨어 RoMi-H 사이의 통합 [사실][^ref-872] |
| 수행 자원 | 창이종합병원 CHART가 연 2회 평가·인증해 등재한 시스템 통합자 [사실][^ref-872] |
| 제약 | 공공 의료기관은 등재된 통합자를 써야 한다 [사실][^ref-872] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

창이종합병원 CHART는 의료 로봇 미들웨어 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md) 통합을 맡을 시스템 통합자를 연 2회 [등재 프로그램](../../glossary/empanelment-programme.md)으로 평가·인증하고, 공공 의료기관이 로봇·소프트웨어·IoT 연동에 등재된 통합자를 쓰게 해 다사업자 연동의 책임 주체를 사전 자격으로 정한다(2025-05 기준). [사실][^ref-872] 연동 완료를 인정하는 기준과 장애 때 누가 복구하는지는 확인하지 못했다. 국내에서 비슷한 관문을 운용한 사례는 [oq-149](../../open-questions.md)에서 열려 있다.

**현장 유형:** 가정

**사례:** 한국 공동주택의 주차·순찰·운반 로봇 도입과 관리 책임

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 차량 주차, 단지 순찰, 물품 운반 [사실][^ref-1211] |
| 수행 자원 | 시흥 힐스테이트더웨이브시티 주차로봇 2세트(실증), 서울 송파구 아파트 자율주행 순찰로봇 2대, 강남 타워팰리스 사족보행로봇(기술검증), 부산 강서구 아파트 운반로봇 서비스 [사실][^ref-1211] |
| 제약 | 발의된 이동로봇 특별법안이 개인정보 처리·책임 분담·책임보험 가입 같은 안전관리 체계를 담는다고 전해졌다(법안 원문 미확인) [사실][^ref-1211] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 사설(한국아파트신문, 2026-09-14)의 의견으로는 이런 로봇이 들어오면 관리주체의 관리 영역과 책임이 넓어질 수 있어, 도입 전에 책임 범위를 명확히 해야 한다. [의견][^ref-1211] 사례마다 제조사·관제 사업자·관리주체가 장애를 어떻게 나눠 맡는지는 확인하지 못했다. 가정 로봇의 원격 조작자 책임은 [oq-185](../../open-questions.md)에서 열려 있다.

물류창고·제조 공장·상업 시설·실외 현장의 다사업자 책임·계약 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

다사업자 책임·계약·데이터를 다루는 접근은 변경한 주체에게 책임을 지우는 규정과 사전 자격, 데이터 접근·공유 계약, 인터페이스 버전·폐기 규칙, 서비스 수준 약속과 감사 이력의 네 갈래로 모이는 것으로 보인다. [추정][^ref-555][^ref-1192][^ref-031][^ref-1205]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 걸리는 규칙은 데이터 권리(EU 데이터법·국내 산업 디지털 전환 촉진법), 인터페이스 변경(VDA 5050·Kubernetes 폐기 정책), 서비스 수준·보안·기록(ISO/IEC 19086-1·IEC 62443-2-4·21 CFR Part 11), 변경 주체 책임(EU 기계류 규정·EU AI법)으로 나뉜다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md)에 있다.

## 8. 대표 연구와 자료

- 유럽연합 집행위원회, 데이터 접근·이용 모델 계약 조항과 클라우드 표준 계약 조항 권고 초안(2025) — 데이터법 이행용 계약 문안 네 벌과 클라우드 계약 조항 여섯 개를 담은 구속력 없는 초안이며, 의무적 기업 간 데이터 공유의 합리적 보상 지침은 추후 발표 예정으로 되어 있다. [사실][^ref-1192]
- 산업통상부, 산업데이터 계약 가이드라인(2023) — 국내 산업데이터 거래 당사자를 위한 유의사항·표준계약서·업종별 사례를 담은 432쪽 자료다. [사실][^ref-1194]
- Shaik, A. S., Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?(SSRN, 2026, 동료심사 전 원고) — Shaik의 제안은 로봇 제조사(OEM)·시스템 통합자·AI 공급자·운영자 사이의 책임을 통제력(피해를 막을 수 있었는가)·예견 가능성·정보 비대칭의 세 원칙으로 배분하는 위험 비례 책임 프레임워크(RPLF)이며, 저자는 이를 상업 계약과 기존 보험으로 구현할 수 있다고 주장한다. [의견][^ref-1208]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록 [추정][^ref-031][^ref-1204] | 로봇 펌웨어와 제조사 API의 수명주기(로봇 제조사) [추정][^ref-555][^ref-1209] |
| 시설·설비 제어 | 설비 어댑터의 인터페이스 버전 관리와 연동 변경 기록 [추정][^ref-031][^ref-1204] | 승강기·출입문 쪽 연동 인터페이스와 설비 안전(설비 제조사·관리주체) [추정][^ref-317][^ref-1211] |
| 원문 19장 다섯 경계 밖(계약·법무·데이터 권리·서비스 수준) | 누가 언제 어떤 명령·변경을 했는지 남기는 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고 [추정][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205] | 계약 체결, 법적 책임 판정·보험·규제 적합성 평가(계약 당사자·법무, [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md)) [추정][^ref-555][^ref-1209][^ref-1208] |

이 영역에서 ROP가 직접 맡을 범위는 제조사·설비 어댑터별 인터페이스 버전과 폐기 일정 관리, 연동·설정 변경의 요청·승인·적용 기록, 타임스탬프 감사 이력과 보관, 데이터 항목별 소유·접근·반출 조건 표시, 계약한 서비스 수준 지표의 측정·보고로 보인다. [추정][^ref-031][^ref-1204][^ref-1207][^ref-1210][^ref-1191][^ref-1192][^ref-1205]

연계 대상: 계약 체결과 법적 책임 판정·보험·규제 적합성 평가는 계약 당사자와 법무에, 로봇 펌웨어와 제조사 API의 수명주기는 로봇 제조사에, 승강기·출입문 쪽 연동 인터페이스와 설비 안전은 설비 제조사·관리주체에 속하므로, ROP는 그들이 정한 조건을 운영 제약으로 받고 판단 근거가 되는 기록과 데이터를 제공하는 쪽을 맡는 것으로 보인다. [추정][^ref-555][^ref-1209][^ref-317][^ref-1211][^ref-1208] EU 기계류 규정과 EU AI법이 정하는 제조자·제공자·배포자 의무를 누가 지는지 판정하고 이행하는 일도 이 연계 대상에 들며, 이 페이지는 그 의무를 ROP가 직접 지는 것으로 서술하지 않는다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 인터페이스 버전 규칙, 설비 연동, 감사 이력, 데이터 권리, 규제 책임, 조달, AI 가치사슬 책임, 적용 현장을 통해 열네 개 세부영역과 이어지는 것으로 보인다. [추정][^ref-031][^ref-1210][^ref-1191][^ref-1209]

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 8건은 모두 열려 있고, 이번 실행에서 새 질문 5건을 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-872]: Changi General Hospital — Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025, 2025-05-01, https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste, 접근일 2026-09-30 (원문 미열람)
[^ref-1191]: European Commission (Shaping Europe's digital future), Data Act explained, 2025-12-15, https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained, 접근일 2026-09-30
[^ref-1192]: European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts, 2025-11-19, https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding, 접근일 2026-09-30
[^ref-1194]: 산업통상부 (공공데이터포털), 산업통상부_산업데이터 계약 가이드라인_20230109, 2023-04-05, https://www.data.go.kr/data/15113186/fileData.do, 접근일 2026-09-30
[^ref-1204]: The Kubernetes Authors, Kubernetes Deprecation Policy, 미확인, https://kubernetes.io/docs/reference/using-api/deprecation-policy/, 접근일 2026-09-30
[^ref-555]: European Parliament and Council of the European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery, 2023-06-14, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-09-30 (원문 미열람)
[^ref-1205]: IEC / ISO (ISO/IEC JTC 1), ISO/IEC 19086-1:2016 Information technology - Cloud computing - Service level agreement (SLA) framework - Part 1: Overview and concepts, 2016-09-21, https://webstore.iec.ch/en/publication/25920, 접근일 2026-09-30 (원문 미열람)
[^ref-1206]: IEC (BSI Knowledge 게재), IEC 62443-2-4:2023 Security for industrial automation and control systems - Security program requirements for IACS service providers, 2023-12-15, https://knowledge.bsigroup.com/products/security-for-industrial-automation-and-control-systems-security-program-requirements-for-iacs-service-providers-1, 접근일 2026-09-30 (원문 미열람)
[^ref-1207]: U.S. Food and Drug Administration 규정 (Cornell Law School LII 게재), 21 CFR § 11.10 - Controls for closed systems, 미확인, https://www.law.cornell.edu/cfr/text/21/11.10, 접근일 2026-09-30
[^ref-317]: 전기신문 (안상민), 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 2023-05-17, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-30
[^ref-1208]: Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong?, 2026-05-01, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6737139, 접근일 2026-09-30 (원문 미열람)
[^ref-1209]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 25: Responsibilities Along the AI Value Chain | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/25/, 접근일 2026-09-30
[^ref-1210]: Future of Life Institute (EU AI법 조문 비공식 게재본), Article 26: Obligations of Deployers of High-Risk AI Systems | EU Artificial Intelligence Act, 미확인, https://artificialintelligenceact.eu/article/26/, 접근일 2026-09-30
[^ref-1211]: 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까, 2026-09-14, https://www.hapt.co.kr/news/articleView.html?idxno=169488, 접근일 2026-09-30
