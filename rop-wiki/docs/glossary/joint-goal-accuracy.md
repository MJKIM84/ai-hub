---
title: "결합 목표 정확도 (Joint Goal Accuracy (JGA))"
type: glossary
term_ko: 결합 목표 정확도
term_en: Joint Goal Accuracy (JGA)
definition: 대화 상태 추적에서 한 턴의 모든 슬롯 값을 정답과 똑같이 맞힌 턴의 비율로, 하나라도 틀리면 그 턴을 오답으로 세는 엄격한 지표다.
related_areas: [27, 18, 23]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-730]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 결합 목표 정확도

# 결합 목표 정확도 (Joint Goal Accuracy (JGA))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 결합 목표 정확도 | Joint Goal Accuracy (JGA) | JGA — Joint Goal Accuracy |

## 한 줄 정의

대화 상태 추적에서 한 턴의 모든 슬롯 값을 정답과 똑같이 맞힌 턴의 비율로, 하나라도 틀리면 그 턴을 오답으로 세는 엄격한 지표다. [추정][^ref-730]

## 설명

ACL 2022 연구는 이 지표가 초기 오류 누적으로 성능을 과소평가한다고 지적하고 상대 슬롯 정확도를 제안했다(MultiWOZ 조건, 원문 미열람). 관련 용어: 슬롯 채우기, 의도 인식.

## 관련 영역

- [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)
- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)

## 출처

[^ref-730]: Kim, T., Yoon, H., Lee, Y., Kang, P., Bang, J., & Kim, M.(ACL 2022 Short Papers, 소속 미확인), Mismatch between Multi-turn Dialogue and its Evaluation Metric in Dialogue State Tracking, 2022-05, https://aclanthology.org/2022.acl-short.33/, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-730](../references/ref-730.md)
