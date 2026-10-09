---
title: "원격 증명 (Remote Attestation)"
type: glossary
term_ko: 원격 증명
term_en: Remote Attestation
definition: 원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다.
related_areas: [52, 18]
tags: []
status: published
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1272]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 원격 증명

# 원격 증명 (Remote Attestation)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 원격 증명 | Remote Attestation | 없음 |

## 한 줄 정의

원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다. [추정][^ref-1272]

## 설명

Shen 외(2026-09, 프리프린트)는 ROS 2 에서 발행 전 훅으로 텔레메트리를 위조해 이 신뢰 경계가 깨질 수 있음을 보고했다(저자 보고값, 독립 재현 미확인).

## 관련 영역

- [52. 통신 보호·위협 관리·감사](../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)

## 출처

[^ref-1272]: Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv), Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics, 2026-09-08, https://arxiv.org/abs/2609.08280, 접근일 2026-10-09

- 참고문헌 페이지: [ref-1272](../references/ref-1272.md)
