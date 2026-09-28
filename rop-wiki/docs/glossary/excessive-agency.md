---
title: "과도한 에이전시 (Excessive Agency)"
type: glossary
term_ko: 과도한 에이전시
term_en: Excessive Agency
definition: LLM 기반 시스템이 필요 이상의 기능·권한·자율성을 가져 잘못되거나 조작된 출력이 해로운 행동으로 이어지는 위험으로, OWASP LLM Top 10(2025)의 한 항목이다.
related_areas: [31, 47, 51]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-695]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 과도한 에이전시

# 과도한 에이전시 (Excessive Agency)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 과도한 에이전시 | Excessive Agency | 없음 |

## 한 줄 정의

LLM 기반 시스템이 필요 이상의 기능·권한·자율성을 가져 잘못되거나 조작된 출력이 해로운 행동으로 이어지는 위험으로, OWASP LLM Top 10(2025)의 한 항목이다. [추정][^ref-695]

## 설명

OWASP 문서는 원인을 과도한 기능·과도한 권한·과도한 자율성으로 나누고, 영향이 큰 행동 전 사람 승인, 최소 권한, 완전한 중재를 대응으로 든다.

## 관련 영역

- [47. AI·학습·적응과 모델 운영](../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- [51. 인증·권한·격리](../categories/security-and-privacy/authentication-authorization-and-isolation.md)
- [31. 사람–로봇 협업](../categories/execution-collaboration-and-recovery/human-robot-collaboration.md)

## 출처

[^ref-695]: OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub), LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md), 2024-11, https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-695](../references/ref-695.md)
