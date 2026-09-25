---
title: "멱등성 키 (Idempotency Key)"
type: glossary
term_ko: 멱등성 키
term_en: Idempotency Key
definition: 클라이언트가 요청마다 만든 고유 값으로, 서버가 같은 요청의 재시도를 알아보고 한 번만 처리하게 하는 데 쓰인다.
related_areas: [12, 1]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-367]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 멱등성 키

# 멱등성 키 (Idempotency Key)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 멱등성 키 | Idempotency Key | 없음 |

## 한 줄 정의

클라이언트가 요청마다 만든 고유 값으로, 서버가 같은 요청의 재시도를 알아보고 한 번만 처리하게 하는 데 쓰인다. [추정][^ref-367]

## 설명

IETF HTTPAPI 작업반의 Idempotency-Key 헤더 초안(RFC 아님)은 키를 다른 내용의 요청에 재사용하지 않게 하고, 서버가 키 만료 정책을 공개하며, 처리 중 재요청에는 409, 다른 내용으로 재사용한 요청에는 422 를 돌려주도록 제안한다.

## 관련 영역

- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)
- [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)

## 출처

[^ref-367]: IETF HTTPAPI Working Group (Jena, J., & Dalal, S.), The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header), 미확인, https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md, 접근일 2026-09-25

- 참고문헌 페이지: [ref-367](../references/ref-367.md)
