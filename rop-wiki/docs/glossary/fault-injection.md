---
title: "장애 주입 (Fault Injection)"
type: glossary
term_ko: 장애 주입
term_en: Fault Injection
definition: 시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다.
related_areas: [23, 12, 20]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-528, ref-601]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 장애 주입

# 장애 주입 (Fault Injection)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 장애 주입 | Fault Injection | 없음 |

## 한 줄 정의

시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다. [추정][^ref-528][^ref-601]

## 설명

NIST ARIAC 는 경진 중 컨베이어 정지·공구 파지 실패 등을 주입하고, ros2_fault_injection 은 ROS 2 토픽·서비스에 장애를 넣는다(README 기준).

## 관련 영역

- [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)
- [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)

## 출처

[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-601]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25

- 참고문헌 페이지: [ref-528](../references/ref-528.md), [ref-601](../references/ref-601.md)
