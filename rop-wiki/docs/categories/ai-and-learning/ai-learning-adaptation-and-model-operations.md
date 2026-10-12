---
title: "47. AI·학습·적응과 모델 운영"
type: area
category: "L. AI·학습 기술"
area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [LLM 계획 접지, 등각 예측, 학습 기반 배차, 모델 레지스트리, 단계적 배포, AI 위험관리]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-12
sources: [ref-617, ref-618, ref-619, ref-620, ref-621, ref-088, ref-092, ref-351, ref-622, ref-623, ref-624, ref-625, ref-626, ref-627, ref-354, ref-359, ref-056, ref-541, ref-417, ref-1512, ref-1513, ref-1514, ref-1515, ref-1516, ref-1547, ref-1548, ref-1549, ref-1550, ref-1551, ref-1552, ref-1553]
last_run: 2026-10-12
version: 3
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 47. AI·학습·적응과 모델 운영

# 47. AI·학습·적응과 모델 운영

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-10-12 · 마지막 실행: 2026-10-12
<!-- auto:page-status:end -->

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

## 3. 왜 중요한가

AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-625][^ref-626][^ref-618] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 왜 중요한가](../../topics/2026/2026-10-12-area47-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area47-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹, 출하

**시나리오:** 자연어 피킹 지시의 해석 검증과 출하 마감 시간대의 학습 배차 모델 교체

다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았고, 근거 출처의 실험 환경(가정·주방·벤치마크, 시뮬레이션 창고)은 물류 현장과 다르다.

### 가. 피킹 — 자연어 지시 해석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관리자가 “오늘 마감 주문을 B구역부터 피킹”처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. [추정][^ref-092][^ref-351][^ref-354] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | LLM은 지시를 해석하고, ROP는 해석 결과의 채택·거부와 사람 확인 요청, 채택·거부 기록을 맡는 구조로 보인다. [추정][^ref-351] |
| 제약 | 이런 AI 활용이 인공지능 기본법의 고영향 인공지능에 해당하는지는 미확인이다(11절 열린 질문). |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해석 후보가 불확실하면 사람에게 묻는다. KnowNo는 필요할 때 사람에게 도움을 요청하게 하며 사람 도움을 줄이는 것을 목표로 한다(저자 보고). [사실][^ref-351] |

### 나. 출하 — 학습 배차 모델 교체

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려는 변경 요청(설명용 가정) |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 창고 다중 로봇 작업 배정을 강화학습 정책으로 수행하는 방법이 연구되어 있다(RTAW, 시뮬레이션 창고 조건). [사실][^ref-623] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고 교체 전 시험·감시 기준을 통과시켜야, 데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험에서 오는 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. [추정][^ref-626][^ref-625][^ref-623][^ref-624] MLflow v3.1.0 문서 기준으로 별칭 재지정은 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 반영된다. [사실][^ref-1512] ML Test Score는 오프라인 시험만으로는 운영 성능을 보장할 수 없다며 소수 트래픽에 먼저 내보내는 카나리를 완화책으로 들고, 롤백을 비상 절차로 두되 평상시에 연습하라고 권고한다(일반 ML 서비스 지침). [사실][^ref-625] |

피킹 시나리오에서 이 영역이 관여하는 칸은 시작 조건(지시가 작업으로 바뀌는 순간)과 예외·성과(되묻기)다. 출하 시나리오에서는 모델 교체가 예외·성과 칸의 위험이 된다.

국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. [추정] 벤더 주장[^ref-627] 이런 예측을 ROP 관점에서 쓴다면 ROP의 몫은 입출고 시간·접안·현장 상·하차 작업의 동기화까지이고, 간선 배차·운송계획은 분류 원문 19장 “거점 간 운송”의 연계 대상이다([범위 경계](../../about/scope-boundary.md)).

**현장 유형:** 기타

**사례:** 부산 스마트시티 국가 시범도시의 서비스 로봇 4종 통합 관제(회사 발표)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | LG CNS 발표에 따르면 로봇 학습·운영 플랫폼 ‘피지컬웍스’의 운영·관제 도구 바통(Baton)이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다. [추정] 벤더 주장[^ref-1549] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

LG CNS 발표(2026-05-07)에 따르면 피지컬웍스의 포지(Forge)에서 학습·검증한 로봇을 바통으로 운영·관제하고, 이 과정에서 쌓인 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 한다. [추정] 벤더 주장[^ref-1549] 같은 발표에 따르면 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 기대된다고 하나, 이는 회사가 기대치로 제시한 값(실측 아님)이다. [추정] 벤더 주장[^ref-1549] 같은 발표에 따르면 포지는 20곳 이상 고객사와 개념검증(Proof of Concept, PoC)을 진행 중이며, 이 주장은 독립적으로 확인되지 않았다. [추정] 벤더 주장[^ref-1549]

이 사례에서 이 영역이 관여하는 부분은 학습과 운영 사이의 모델 갱신이지만, 공개 자료로 채울 수 있는 칸은 수행 자원뿐이었다. 이 위키는 학습·운영 연계 플랫폼을 도입 검토할 때 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청하는 편이 좋다고 본다. [의견][^ref-1549]

## 6. 대표 접근법과 기술

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-626] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area47-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area47-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 연구와 자료](../../topics/2026/2026-10-12-area47-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리로 보인다. [추정][^ref-618][^ref-617][^ref-619][^ref-351][^ref-626]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | AI가 낸 계획의 실행 가능 여부 확인, 채택·거부와 기록 | 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(연계 대상) |
| 상위 업무 시스템 | 주문·납기 제약을 받은 배정·계획 모델의 버전·변경 승인 | 수요예측 모델(연계 대상) |
| 거점 간 운송 | 입출고 시간·접안·현장 상·하차 작업 동기화 | 간선 배차·운송계획(연계 대상) |

연계 대상: Code as Policies의 저수준 정책 코드, SayCan의 사전 학습 기술 같은 저수준 정책·파지 학습과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. [추정][^ref-622][^ref-088] 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 ROP의 채택 기준을 둘러싼 운영 틀로 보인다. [추정][^ref-618][^ref-617][^ref-619] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

### 배포 후 감시·변경관리·복구 실패 처리

NIST AI RMF 1.0의 MANAGE 4.1은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화, 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 하는 항목이며, 법적 의무가 아닌 자율 적용 프레임워크다. [사실][^ref-1551] 이 위키는 모델 공급자의 학습·검증 책임, ROP의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할을 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다고 본다. [의견][^ref-1551] 같은 맥락에서 이 위키는 ROP가 배포 중단·이전 모델 복원 시도·복원 확인을 서로 다른 상태로 기록하고, 복구하지 못한 로봇을 새 작업 배정에서 빼는 정책을 맡는 편이 맞다고 본다. [의견][^ref-1514][^ref-1515][^ref-1516] 장치 업데이트 실행 수단은 [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md), 법 해석과 의무 발생 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 법무·운영 사업자 쪽 연계 대상이며, 이 페이지는 개별 ROP의 의무 발생 여부를 판단하지 않는다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류 개정 전 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area27-s10.md)에 있다.

### 2026-10-12 갱신으로 더한 연결

- [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 장치 업데이트 도구의 단계적 배포·배포 중단·롤백 상태가 모델 교체·되돌림의 실행 수단이 된다.
- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 가중치·전처리기·데이터 형식·보정판을 묶은 배포 묶음의 판 관리와 이전 묶음 보존이 이어진다.
- [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) — 한국 인공지능기본법 제34조의 문서 책무와 EU AI Act 개정(부속서 I Section B, 제2조 2항)의 해석이 이어진다.

## 11. 열린 질문

아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 열린 질문](../../topics/2026/2026-10-12-area47-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-12 · 갱신 · [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md) — 차등 갱신: 3절 법·규제 문단 정정(인공지능기본법 개정 법률 2026-07-21 시행·제34조, EU AI Act 2026/1744 개정의 기계류 Section B 이동·제2조 2항), 4·6·7·8절에 기존 분리 주제 페이지(2026-09-25-area27-s4·s6·s7·s8) 링크를 단 갱신 소절 추가(별칭 반영 시점, 배포 묶음 호환성, ML Test Score Infra4·6·7, 배포 중단·롤백 상태, KnowNo·ACI 보장 조건, LWD, AI-Hub 71825, NIST MANAGE 4.1, 제43·72조 조문 소개), 5절 출하 예외·성과 보강과 기타 현장 사례 추가, 9절 배포 후 감시 책임 경계, 10절 연결 3건, 11절 oq id 부여·부분 근거·새 질문 4건, 13절 각주 갱신(신규 12건). 2차: 기존 주제 페이지 링크 복구, oq-213 항목 삭제, 7절 법 문단 첫 문장 태그·각주 추가 (실행 2026-10-12-04)
- 2026-10-12 · 생성 · [47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area47-s6.md) — 자동 분리: 47. AI·학습·적응과 모델 운영 의 "6. 대표 접근법과 기술" 절(3,448자)을 옮겼다 (실행 2026-10-12-04)
- 2026-10-12 · 생성 · [47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area47-s7.md) — 자동 분리: 47. AI·학습·적응과 모델 운영 의 "7. 관련 표준·프레임워크·오픈소스" 절(2,884자)을 옮겼다 (실행 2026-10-12-04)
- 2026-10-12 · 생성 · [47. AI·학습·적응과 모델 운영 — 열린 질문](../../topics/2026/2026-10-12-area47-s11.md) — 자동 분리: 47. AI·학습·적응과 모델 운영 의 "11. 열린 질문" 절(1,912자)을 옮겼다 (실행 2026-10-12-04)
- 2026-10-12 · 생성 · [47. AI·학습·적응과 모델 운영 — 왜 중요한가](../../topics/2026/2026-10-12-area47-s3.md) — 자동 분리: 47. AI·학습·적응과 모델 운영 의 "3. 왜 중요한가" 절(1,551자)을 옮겼다 (실행 2026-10-12-04)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-617]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-09-25 (원문 미열람)
[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-619]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-622]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)
[^ref-627]: 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI', 2026-09-19, https://www.mt.co.kr/industry/2026/09/19/2026091818023697394, 접근일 2026-09-25 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-1512]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12
[^ref-1514]: Northern.tech (Mender documentation), Create a custom Update Module, 미확인, https://docs.mender.io/artifact-creation/create-a-custom-update-module, 접근일 2026-10-12
[^ref-1515]: Amazon Web Services (AWS IoT Greengrass V2 Developer Guide), Check deployment status, 미확인, https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html, 접근일 2026-10-12
[^ref-1516]: Amazon Web Services (AWS IoT Core Developer Guide), How job configurations work, 미확인, https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html, 접근일 2026-10-12
[^ref-1549]: LG CNS, LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개, 2026-05-07, https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1, 접근일 2026-10-12
[^ref-1551]: NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023-01, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 접근일 2026-10-12
