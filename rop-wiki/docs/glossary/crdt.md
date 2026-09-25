---
title: "무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))"
type: glossary
term_ko: 무충돌 복제 데이터 타입
term_en: Conflict-free Replicated Data Type (CRDT)
definition: 여러 복제본을 조율 없이 수정해도 같은 갱신을 받으면 정해진 규칙으로 같은 상태에 수렴하도록 설계된 데이터 타입이다.
related_areas: [8, 11]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-295]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 무충돌 복제 데이터 타입

# 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 무충돌 복제 데이터 타입 | Conflict-free Replicated Data Type (CRDT) | CRDT — Conflict-free Replicated Data Type |

## 한 줄 정의

여러 복제본을 조율 없이 수정해도 같은 갱신을 받으면 정해진 규칙으로 같은 상태에 수렴하도록 설계된 데이터 타입이다. [추정][^ref-295]

## 설명

관측 기록 모음처럼 순서와 무관하게 합칠 수 있는 상태에 맞고, 한 시점에 한 주체만 가져야 하는 자원에는 단일 감독자 판정이 필요할 것으로 보인다(추정).

## 관련 영역

- [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)
- [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)

## 출처

[^ref-295]: Preguiça, N., Baquero, C., & Shapiro, M., Conflict-free Replicated Data Types (CRDTs), 2018-05, https://arxiv.org/abs/1805.06358, 접근일 2026-09-25 (원문 미열람)

- 참고문헌 페이지: [ref-295](../references/ref-295.md)
