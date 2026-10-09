---
title: "클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))"
type: glossary
term_ko: 클라이언트 자격 증명 흐름
term_en: OAuth 2.0 Client Credentials Grant (Machine-to-Machine)
definition: 사람 사용자 없이 서비스나 기계가 자기 자격 증명으로 접근 토큰을 받아 API 를 부르는 OAuth 2.0 인가 방식이다.
related_areas: [41, 51]
tags: []
status: published
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-762]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 클라이언트 자격 증명 흐름

# 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 클라이언트 자격 증명 흐름 | OAuth 2.0 Client Credentials Grant (Machine-to-Machine) | Machine-to-Machine — OAuth 2.0 Client Credentials Grant |

## 한 줄 정의

사람 사용자 없이 서비스나 기계가 자기 자격 증명으로 접근 토큰을 받아 API 를 부르는 OAuth 2.0 인가 방식이다. [추정][^ref-762]

## 설명

Open-RMF rmf-web API 서버 README 는 이 흐름(M2M)에서 신원 제공자가 표준 클레임 대신 네임스페이스 붙은 클레임만 주는 경우를 위한 선택 설정 preferred_username_claim_namespace 를 둔다(2026-10-09 확인).

## 관련 영역

- [41. 플랫폼 아키텍처·외부 API](../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- [51. 인증·권한·격리](../categories/security-and-privacy/authentication-authorization-and-isolation.md)

## 출처

[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09

- 참고문헌 페이지: [ref-762](../references/ref-762.md)
