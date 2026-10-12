---
title: "48. 안전·위험 관리"
type: area
category: "M. 안전"
area_no: 48
related_areas: [27, 29, 31, 47, 51, 57]
tags: [위험성평가, STPA, 운용 구역, 비상정지, VDA 5050, 안전 책임 경계]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-004, ref-031, ref-417, ref-470, ref-472, ref-555, ref-560, ref-561, ref-563, ref-564, ref-566, ref-567, ref-789, ref-1077, ref-1255, ref-1398, ref-1455, ref-1456, ref-1457, ref-1458, ref-1459, ref-1460, ref-1461, ref-1462, ref-1463, ref-1464, ref-1465]
last_run: 2026-10-11
version: 4
---

[홈](../../index.md) › [M. 안전](index.md) › 48. 안전·위험 관리

# 48. 안전·위험 관리

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 4 · 마지막 갱신: 2026-10-11 · 마지막 실행: 2026-10-11
<!-- auto:page-status:end -->

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]

## 3. 왜 중요한가

확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08 Part 1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025)을 나누어 다루고, STPA 연구는 개별적으로 정상인 구성요소 사이의 상호작용에서 위험을 찾는다. 그래서 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. [추정][^ref-470][^ref-472][^ref-560][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 왜 중요한가](../../topics/2026/2026-10-11-area48-s3.md)에 있다.

## 4. 핵심 개념과 용어

**위험성평가(Risk Assessment)** — ISO 12100:2010 이 기계 설계의 일반 원칙으로 정하는, 위험원을 찾고 위험을 평가해 위험 감소 필요성을 판단하는 절차다. [사실][^ref-566]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area48-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 두 장면 모두 ROP 가 안전 기능을 직접 수행하지 않고, 로봇·설비가 보고한 안전 상태를 받아 작업을 보류·재배정·재개하는 장면이다.

### 피킹 중 작업자 진입

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 구역에 작업자가 들어와 로봇이 멈춘 뒤 작업을 이어가기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업자가 피킹 구역에 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고한다. [추정][^ref-031] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 로봇은 안전 상태를 보고하고, ROP 는 진행 중 피킹 작업의 보류·재배정과 재개 지시를 맡는다. [추정][^ref-031] |
| 제약 | 안전 상태가 해제되고 운용 모드가 자동(AUTOMATIC)으로 돌아오기 전에는 재개하지 않는다. [추정][^ref-031] |
| 완료·인계 | 재개 조건을 확인한 뒤 즉시 동작 stopPause 등으로 재개를 지시한다. [추정][^ref-031] |
| 예외·성과 | 멈춘 로봇의 피킹 작업을 보류하거나 다른 로봇에 재배정해야 할 것으로 보인다. [추정][^ref-031] |

여기서 ROP 의 몫은 정지 자체가 아니라 정지 뒤의 업무 처리다. 어떤 주문을 기다리게 하고 어떤 주문을 다른 로봇에 넘길지가 이 영역과 [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)이 만나는 지점이다.

구축자 의견: VDA 5050 의 업무 일시정지·재개 명령(startPause·stopPause)이 비상정지 회로 리셋과 같다는 근거는 없으므로, ROP 는 업무 일시정지 해제와 현장 안전정지 해제 승인을 별도 상태로 관리하고 제조사·설비의 해제 조건 충족을 확인하기 전에는 재개를 지시하지 않는 정책을 두는 것이 바람직하다. [의견][^ref-031]

### 출하 마감 전 화재경보

**물류 흐름 단계:** 출하

**시나리오:** 출하 준비 중 비상 신호로 로봇이 주차한 뒤 작업 재개

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 전에 화재경보 같은 비상 신호가 온다. [추정][^ref-567] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | Open-RMF 기능 요청에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동한다. [사실][^ref-567] |
| 제약 | 이슈 #658 작성 시점(2025-04-04) 기준으로 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다. [사실][^ref-567] 이슈 작성자는 두 건물에 로봇을 둔 상황에서 한 건물의 화재경보가 모든 로봇을 주차시킨다고 보고한 것으로 보이나, 세부 상황은 확인하지 못했다. [추정][^ref-567] rmf_fleet_adapter 변경 이력은 2.10.0(2025-05-09) 절에 플릿 이름으로 화재경보를 분리하는 선택지(#413)를 싣는다. [사실][^ref-1398] 2.14.0 코드에서 플릿 어댑터는 대상 비상 신호의 플릿 이름 목록(fleet_names)이 비어 있거나 자기 플릿 이름을 포함할 때만 비상 처리를 하므로, 빈 목록은 모든 플릿에 적용된다. [사실][^ref-1464] 같은 2.14.0 코드에는 플릿을 가리지 않는 기존 불리언 비상 알림(EmergencyNotice) 구독 경로도 함께 남아 있다. [사실][^ref-1464] 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 마감 준수에 영향을 주는 것으로 보인다. [추정][^ref-567][^ref-004] |

이 표의 제약 칸은 2026-10-11 갱신에서 고쳤다. 이전 판은 이슈 작성 뒤의 구현 여부를 미확인으로 두었으나, 변경 이력과 코드로 보면 2.10.0 부터 플릿 이름으로 대상을 고르는 비상 신호가 있고 2.14.0 에는 기존 불리언 경로와 대상 지정 경로가 함께 있다고 쓰는 것이 맞아 보인다. 다만 세 출처가 모두 Open-RMF 계열이라 독립 교차 확인이 아니고, 코드 열람이므로 대피 안전성을 검증한 것도 아니며, 건물·구역 단위 구분은 플릿 이름 매핑 설계에 달려 있다. [추정][^ref-1398][^ref-1464][^ref-567]

구축자 의견: 빈 플릿 이름 목록이 전체 플릿을 뜻하므로 운영 화면은 빈 목록을 '전체 플릿'으로 분명히 표시하고, 잘못된 플릿 선택·신호 지연·중복 신호·재개 전 승인 조건을 시험 항목으로 두며, 화재 때 로봇의 이동·정지 정책은 시설·설비 경계의 연계 대상인 현장 대피 계획과 함께 정해야 한다. [의견][^ref-1464]

## 6. 대표 접근법과 기술

안전을 다루는 접근은 위험을 찾는 방법, 운영 중 안전 상태를 주고받는 방법, 실행 전에 명령을 거르는 방법으로 나뉜다. [추정][^ref-566][^ref-031][^ref-417]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area48-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준은 대부분 발행 기관 소개·발표 자료 기준이며 본문은 열람하지 않았다(각주의 원문 미열람 표시). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area48-s7.md)에 있다.

## 8. 대표 연구와 자료

Bensaci, C.·Zennir, Y.·Pomorski, D., A Comparative Study of STPA Hierarchical Structures in Risk Analysis(2018) — 다중 이동 로봇 시스템의 제어 구조별 위험 시나리오를 STPA 로 비교했다. 대상은 화학 분석 실험실의 다중 로봇이며 물류 현장이 아니다. [사실][^ref-564]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 대표 연구와 자료](../../topics/2026/2026-10-11-area48-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집과 일시정지·재개 지시 [추정][^ref-031] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증(로봇 제조사) [추정][^ref-470][^ref-560] OMRON LD Safety Guide Rev H(2019-10)는 플릿 안의 로봇들이 위치·크기·경로 계획 정보를 주고받아 장애물 회피에 쓰는 것을 충돌을 막는 인터록 방식으로 보지 않고, 필요한 인터록은 사용자·통합자가 따로 갖춰야 한다고 설명한다(이 제품 매뉴얼 기준, 타사 플릿이나 현행 모델로 일반화하지 않음). [추정] 벤더 주장[^ref-1463] 같은 매뉴얼은 외부 비상정지 회로에 사용자 부품이 들어가면 그 부품을 포함한 성능 수준(Performance Level, PL)·시간당 위험 고장 확률(PFH) 계산과 최종 위험성평가를 사용자 책임으로 둔다(OMRON LD Safety Guide Rev H 기준 벤더 주장, 법적 의무 판단 아님). [추정] 벤더 주장[^ref-1463] |
| 시설·설비 제어 | 비상 신호에 따른 플릿별 대피·주차 조율 [추정][^ref-567][^ref-004] | 연계 대상: 현장 방호 설비와 설비 안전 제어 [추정][^ref-560] |
| 업종별 조건 | 구역·권한 제약을 경로·배정에 반영하는 운영 조율 [추정][^ref-004] | 연계 대상: 업종별 전문 안전 요구 [추정][^ref-563] 현장 사업주의 법적 의무로, 국내 지침은 도급사업주와 수급사업주가 각각 위험성평가를 하게 한다. [사실][^ref-1460] 이를 제조사 매뉴얼의 사용자 책임 구분과 함께 보면 혼합 플릿 현장의 위험성평가는 현장 사업주(도급 구조이면 각각)가 주체가 되고 ROP 사업자·제조사·설비업체는 계약에 따라 자료와 분석을 제공하는 구조로 보이나, ROP 사업자를 지칭하는 규정은 확인한 자료에 없어 실제 배분은 현장의 법적 주체·계약에 따라 달라 확정되지 않는다(oq-096). [추정][^ref-1460][^ref-1463] |

ROP 가 맡는 것은 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-567] 이 경계는 제품 전략에 따라 이동할 수 있으며, 이종 제조사를 연결하는 ROP 는 안전 기능을 제조사에 맡기고 그 상태와 결과를 받는 쪽에 설 수 있는 것으로 보인다([범위 경계](../../about/scope-boundary.md)). [추정][^ref-031][^ref-470][^ref-560] 국내 지침의 해석과 다사업자 책임 배분은 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)와 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)의 연계 범위다.

EU 기계 규정 2023/1230 제3조(16)의 [실질적 변경](../../glossary/substantial-modification.md)은 제조자가 예견·계획하지 않은 물리적·디지털 변경이 새 위험요인을 만들거나 기존 위험을 키워 안전에 영향을 주고, 그 결과 (a) 기존 안전 제어 시스템의 변경이 필요한 방호장치·보호장치 추가나 (b) 안정성·기계적 강도를 보장할 추가 보호조치가 필요한 경우로 한정된다(2026-07-27 통합본 기준). [사실][^ref-555] 같은 규정 제54조는 일반 적용일(2027-01-20)과 별도로 제26~42조는 2024-01-20, 제50조(1)은 2026-10-20, 제6조(7)·제48조·제52조는 2023-07-19, 제6조(2)~(6)·(8)·(11)·제47조·제53조(3)은 2024-07-20 부터 적용한다. [사실][^ref-555] 이 조건을 보면 ROP 정책·어댑터 업데이트가 실질적 변경인지는 업데이트마다 조건을 따져야 하며 디지털 변경이라는 이유만으로 모두 재인증 대상이라고 볼 수는 없어 보이나, 개별 업데이트의 법적 분류와 누가 제조자 의무를 지는지는 이번 자료로 판단하지 않았다(oq-093, oq-282). [추정][^ref-555] 이 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어지는 연계 범위다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) — ISO 10218-2:2025 에 사이버보안 요구가 들어오면서 안전과 보안이 맞물리는 것으로 보인다. [추정][^ref-560]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area48-s10.md)에 있다.

## 11. 열린 질문

**oq-064** (상태: 열림) 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 부분 근거: KS B 7327 이 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성과 인증 기준 대응은 확인되지 않는다(7절). [추정][^ref-1458]

자세한 내용은 주제 페이지 [48. 안전·위험 관리 — 열린 질문](../../topics/2026/2026-10-11-area48-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-11 · 갱신 · [48. 안전·위험 관리](safety-and-risk-management.md) — 3·5·6·7·8·9·11·13절 차등 갱신: 국내 위험성평가 지침(실시 주체·근로자 참여·수시평가), Open-RMF 대상 비상 신호로 화재경보 사례 제약 칸 정정, STPA 산출물·참여 기록·감시와 대응 구분, R15.08 Part 3·ISO 3691-4 판 번호·KS B 7327 정정·보강, Bensaci 2020·Belzile 사례 조건·SafeGate 분모, 책임 경계(벤더 주장·사업주 의무·EU 실질적 변경 조건), 열린 질문 부분 근거와 새 질문 4건. 2차: 3·6·7·8·11절에 이전 판 주제 페이지 링크 복원, 7절 정정 대상 페이지 명시. 후속 갱신 필요: docs/topics/2026/2026-09-25-area25-s7.md 43행, docs/topics/2026/2026-09-26-area25-s7.md 46행, docs/categories/safety/index.md 95행, docs/categories/governance-law-and-society/index.md 84행 (실행 2026-10-11-04)
- 2026-10-11 · 생성 · [48. 안전·위험 관리 — 열린 질문](../../topics/2026/2026-10-11-area48-s11.md) — 자동 분리: 48. 안전·위험 관리 의 "11. 열린 질문" 절(1,898자)을 옮겼다 (실행 2026-10-11-04)
- 2026-10-11 · 생성 · [48. 안전·위험 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area48-s7.md) — 자동 분리: 48. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,778자)을 옮겼다 (실행 2026-10-11-04)
- 2026-10-11 · 생성 · [48. 안전·위험 관리 — 대표 연구와 자료](../../topics/2026/2026-10-11-area48-s8.md) — 자동 분리: 48. 안전·위험 관리 의 "8. 대표 연구와 자료" 절(1,356자)을 옮겼다 (실행 2026-10-11-04)
- 2026-10-11 · 생성 · [48. 안전·위험 관리 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area48-s6.md) — 자동 분리: 48. 안전·위험 관리 의 "6. 대표 접근법과 기술" 절(1,151자)을 옮겼다 (실행 2026-10-11-04)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-10-11 (원문 미열람)
[^ref-472]: Association for Advancing Automation (A3), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I. 외(arXiv), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-11
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-10-11
[^ref-564]: Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore), A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회), 2018-12, https://ieeexplore.ieee.org/document/8910126/, 접근일 2026-09-25 (원문 미열람)
[^ref-566]: CEN (iTeh Standards 카탈로그), EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction, 2010, https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010, 접근일 2026-09-25 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-10-11 (원문 미열람)
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-1398]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-11
[^ref-1458]: 한국표준협회 KSSN(국가기술표준원 고시), KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항, 2024-11-01, https://www.kssn.net/search/stddetail.do?itemNo=K001010149365, 접근일 2026-10-11
[^ref-1460]: 고용노동부(국가법령정보센터), 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호), 2024-12-18, https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202, 접근일 2026-10-11
[^ref-1463]: OMRON (Omron Adept Technologies), Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H), 2019-10, https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1, 접근일 2026-10-11
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독), 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
