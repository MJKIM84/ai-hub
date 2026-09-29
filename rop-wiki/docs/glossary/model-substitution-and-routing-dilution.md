---
title: "모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)"
type: glossary
term_ko: 모델 대체·라우팅 희석
term_en: Model Substitution / Routing Dilution
definition: 언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다.
related_areas: [13, 47, 57]
tags: []
status: published
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-865]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 모델 대체·라우팅 희석

# 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 모델 대체·라우팅 희석 | Model Substitution / Routing Dilution | 없음 |

## 한 줄 정의

언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다. [추정][^ref-865]

## 설명

Zhang·Zhang·Qin(2026)의 IRIS 는 응답 텍스트만으로 이를 감사해 상용 라이브러리에서 희석을 탐지력 0.85·오탐률 0.017 로 잡았다.

## 관련 영역

- [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md)
- [47. AI·학습·적응과 모델 운영](../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- [57. 자산·소프트웨어 수명주기 관리](../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 출처

[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29

- 참고문헌 페이지: [ref-865](../references/ref-865.md)
