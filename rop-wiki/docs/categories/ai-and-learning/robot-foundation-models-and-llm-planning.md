---
title: "44. 로봇 기반 모델·언어 모델 계획"
type: area
category: "L. AI·학습 기술"
area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [VLA, 로봇 기반 모델, 언어 모델 계획, 교차 형태 학습, 불확실도 정렬, 다중 로봇 계획]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1045, ref-1046, ref-1047, ref-1048, ref-088, ref-092, ref-586, ref-090, ref-351, ref-1049, ref-170, ref-171, ref-1050, ref-1051, ref-1052]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 44. 로봇 기반 모델·언어 모델 계획

# 44. 로봇 기반 모델·언어 모델 계획

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]

## 3. 왜 중요한가

로봇 기반 모델과 대규모 언어 모델(Large Language Model, LLM) 기반 계획은 ROP가 로봇의 능력을 받아들이는 방식과 대화로 받은 지시를 실행으로 옮기는 방식을 함께 바꾸고 있어, 무엇을 받아들이고 무엇을 검증할지 정해야 하는 영역이다. [추정][^ref-1048][^ref-351]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 왜 중요한가](../../topics/2026/2026-09-30-area44-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 개념은 로봇 쪽의 학습된 범용 정책과 계획 쪽의 접지·검증 장치로 나뉜다. [추정][^ref-1045][^ref-586]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area44-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 가정 사례는 처음 보는 가정집에서의 연구 평가다. [사실][^ref-1047] 제조 공장 사례는 도입 기업의 발표이고, 물류창고 사례는 국내 실증 계획이다. [추정] 벤더 주장[^ref-1051][^ref-1052] 병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 적용 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 가정

**사례:** 처음 보는 가정집에서 부엌·침실 정리(연구 평가)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(초록에 작업을 일으키는 요청 방식이 없다) |
| 작업 대상 | 처음 보는 가정집의 부엌·침실 공간과 그 안의 물건 [사실][^ref-1047] |
| 수행 자원 | 미확인(초록에 로봇 기종과 사람의 역할이 없다) |
| 제약 | 학습 때 보지 못한 가정집에서 장기·정교한 조작 작업을 해야 한다 [사실][^ref-1047] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

Physical Intelligence의 π0.5는 여러 로봇의 데이터, 고수준 의미 예측, 웹 데이터 같은 이질적 과제를 함께 학습(co-training)해 “cleaning a kitchen or bedroom, in entirely new homes” 같은 장기 작업을 수행했다고 보고했다(2025-04). [사실][^ref-1047] 이것은 연구 평가(처음 보는 가정집에서의 실험)이며 상용 배치가 아니다. [사실][^ref-1047] 이 사례에서 로봇 기반 모델이 관여하는 부분은 작업 대상을 미리 정한 스킬 목록 없이 다루는 방식이다. [추정][^ref-1045][^ref-1047]

**현장 유형:** 제조 공장

**사례:** 자동차 공장에서 휴머노이드의 부품 투입과 순서 공급(BMW 그룹 스파턴버그 공장)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(자료에 작업을 일으키는 요청 방식이 없다) |
| 작업 대상 | 용접 공정용 판금 부품(Figure 02), 대용량 용기에 섞여 들어온 부품(Figure 03, 착수 발표) [추정] 벤더 주장[^ref-1051] |
| 수행 자원 | Figure AI의 휴머노이드 Figure 02·Figure 03, 순서 대차를 조립 공정으로 옮기는 자동화 시스템 [추정] 벤더 주장[^ref-1051] |
| 제약 | 미확인 |
| 완료·인계 | 계획 내용(착수 발표): Figure 03이 부품을 순서 대차(sequencing trolley)에 정리하면 대차가 자동화 시스템으로 조립 공정에 운반된다. 수행 결과가 아니다 [추정] 벤더 주장[^ref-1051] |
| 예외·성과 | Figure 02가 BMW X3 3만 대 이상의 생산을 도왔다고 밝히나, 같은 자료 안에서 기간이 10개월과 11개월로 엇갈린다. 복구 주체는 미확인 [추정] 벤더 주장[^ref-1051] |

BMW 그룹은 2025년 스파턴버그 공장에 Figure AI의 휴머노이드 Figure 02를 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다. [추정] 벤더 주장[^ref-1051] 같은 보도자료(2026-06-25) 안에는 10개월 동안 3만 대 이상 생산을 지원했다는 문장과 11개월 배치라는 문장이 함께 있어 기간을 하나로 정하지 않는다(11절 열린 질문). [추정] 벤더 주장[^ref-1051]

BMW 그룹은 또 후속 Figure 03이 스파턴버그에서 순서 공급(just in sequence) 물류 작업을 시작한다고 밝혔고(착수 발표), 이 로봇이 음성 대화 기능과 무선 충전을 갖췄다고 설명한다. [추정] 벤더 주장[^ref-1051] Figure AI 자체 발표로는 교차 확인하지 못했다.

**현장 유형:** 물류창고

**사례:** 물류센터에서 시각–언어–행동(Vision-Language-Action, VLA) 모델([비전 언어 행동 모델](../../glossary/vision-language-action-model.md))을 넣은 휴머노이드의 실증(개념 검증, Proof of Concept, PoC) 계획 — 입고·출고·피킹·반품 단계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 입·출고·오발주 등 고난도 작업과 분류·피킹·반품 등 수작업 공정(비정형 작업) [추정] 벤더 주장[^ref-1052] |
| 수행 자원 | VLA 모델을 넣은 로보티즈의 상체형 휴머노이드 AI 워커, 협력사 BGF로지스 [추정] 벤더 주장[^ref-1052] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 목표치(실측 아님): 핵심 공정 자동화율 80% 이상, 오발주 재분류·피킹 작업 성공률 90% 이상 [추정] 벤더 주장[^ref-1052] |

헬로티 보도(2025-11-26)에 따르면 로보티즈는 정부 과제 'AI 파운데이션 모델 기반 유통 공정 특화 휴머노이드 로봇 개발'(정부 출연금 약 60억 원)로, VLA 모델을 넣은 상체형 휴머노이드 AI 워커가 BGF로지스 물류센터 실증(PoC)을 수행할 계획이다. [추정] 벤더 주장[^ref-1052] 기사가 전한 성과 수치는 목표치(실측 아님)이며, 공개된 측정 결과는 확인하지 못했다(11절 열린 질문). [추정] 벤더 주장[^ref-1052]

## 6. 대표 접근법과 기술

대표 접근법은 여러 로봇 데이터로 범용 정책을 학습하는 로봇 기반 모델과, 언어 모델 계획을 로봇 능력·기호 계획기·사람 확인에 묶어 믿을 수 있게 하는 방법으로 나뉜다. [추정][^ref-1048][^ref-092][^ref-351]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area44-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 자원은 공개 데이터셋(Open X-Embodiment), 공개 VLA 모델(OpenVLA, GR00T N1), ROS용 언어 모델 에이전트(ROSA), 계획 표현 언어인 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)다. [사실][^ref-1048][^ref-1046][^ref-1049][^ref-171][^ref-092]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area44-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 로봇 기반 모델 계열과 언어 모델 계획 계열의 논문, 그리고 국내 협력 동향 기사다. [사실][^ref-1045][^ref-088][^ref-1050]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료](../../topics/2026/2026-09-30-area44-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 언어 모델 계획을 검증하고 사람 확인을 거쳐 이종 로봇에 내리는 계층을 맡고, VLA의 저수준 조작 정책은 로봇 제조사·모델 제공자에게 연계하는 것으로 보인다. [추정][^ref-092][^ref-351][^ref-1045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받고, 검증된 계획을 내리는 인터페이스 [추정][^ref-088][^ref-090][^ref-171] | 연계 대상: VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(로봇 제조사·모델 제공자) [추정][^ref-1045][^ref-1046][^ref-1047][^ref-1049] |

ROP가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층, 불확실할 때 사람에게 확인을 요청하는 절차, 이종 로봇에 계획을 내리는 인터페이스이며, 이는 분류 원문 C. 채팅 기반 구성·운영 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 같은 방향이다. [추정][^ref-092][^ref-586][^ref-351]

IMR-LLM처럼 공정 트리를 따라 실행 가능한 저수준 로봇 프로그램까지 생성하는 연구도 있으나, 그 부분은 로봇 자체 제어에 닿으므로 ROP에서는 연계 대상 문맥으로 본다. [추정][^ref-170] 이 경계는 제품 전략에 따라 이동할 수 있으며, 분류 원문은 '이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다'고 적는다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 로봇 능력 표현, 대화형 지시, 계획·배정, 계획 검증, 현장 유형 영역과 이어진다. [추정][^ref-1046][^ref-090]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area44-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-07) 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가?

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 열린 질문](../../topics/2026/2026-09-30-area44-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md) — 영역 심화: seed → draft, 3~11절 신규 작성(자동 분리 후 요약·링크), 각주 15건, 1차 수정 지시 10건 이행. 2차: 5절 도입 문장을 가정 [사실]과 제조 공장·물류창고 [추정] 벤더 주장으로 분리, 5절에 VLA(용어집 링크)·PoC, 7절에 PDDL 풀어쓰기 (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area44-s6.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "6. 대표 접근법과 기술" 절(1,491자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area44-s4.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "4. 핵심 개념과 용어" 절(1,296자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료](../../topics/2026/2026-09-30-area44-s8.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차: RT-2 '출발점' 평가 삭제·f1·f3 범위로 재서술, LLM+P 문장을 분리해 [사실]`[^ref-092]` 부여(각주 정의·sources 추가), [의견]은 Kambhampati 외 주장에만 (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area44-s10.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(953자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1045]: Brohan, A., Brown, N. 외 (Google DeepMind, arXiv), RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control, 2023-07-28, https://arxiv.org/abs/2307.15818, 접근일 2026-09-30
[^ref-1046]: Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv), OpenVLA: An Open-Source Vision-Language-Action Model, 2024-06-13, https://arxiv.org/abs/2406.09246, 접근일 2026-09-30
[^ref-1047]: Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv), π0.5: a Vision-Language-Action Model with Open-World Generalization, 2025-04-22, https://arxiv.org/abs/2504.16054, 접근일 2026-09-30
[^ref-1048]: Open X-Embodiment Collaboration (arXiv), Open X-Embodiment: Robotic Learning Datasets and RT-X Models, 2023-10-13, https://arxiv.org/abs/2310.08864, 접근일 2026-09-30
[^ref-088]: Ahn, M., Brohan, A., Brown, N. 외 (arXiv), Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-30
[^ref-092]: Liu, B., Jiang, Y., Zhang, X. 외 (arXiv), LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04-22, https://arxiv.org/abs/2304.11477, 접근일 2026-09-30
[^ref-586]: Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv), LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks, 2024-02-02, https://arxiv.org/abs/2402.01817, 접근일 2026-09-30
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-30
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-30
[^ref-1049]: NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv), GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, 2025-03-18, https://arxiv.org/abs/2503.14734, 접근일 2026-09-30
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv), IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03-03, https://arxiv.org/abs/2603.02669, 접근일 2026-09-30
[^ref-171]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — README, 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-09-30
[^ref-1050]: 지디넷코리아, K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과, 2025-05-01, https://zdnet.co.kr/view/?no=20250501140356, 접근일 2026-09-30
[^ref-1051]: BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg, 2026-06-25, https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en, 접근일 2026-09-30
[^ref-1052]: 헬로티, VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입, 2025-11-26, https://www.hellot.net/news/article.html?no=107567, 접근일 2026-09-30
