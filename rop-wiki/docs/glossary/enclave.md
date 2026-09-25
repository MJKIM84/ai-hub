---
title: "인클레이브 (Enclave (SROS 2))"
type: glossary
term_ko: 인클레이브
term_en: Enclave (SROS 2)
definition: SROS 2 에서 같은 신원과 접근통제 규칙을 공유하는 프로세스 또는 프로세스 묶음으로, 보안 인증서·권한 파일을 이 단위로 발급·적용한다.
related_areas: [26, 11, 10]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-405, ref-009]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 인클레이브

# 인클레이브 (Enclave (SROS 2))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 인클레이브 | Enclave (SROS 2) | SROS 2 — Enclave |

## 한 줄 정의

SROS 2 에서 같은 신원과 접근통제 규칙을 공유하는 프로세스 또는 프로세스 묶음으로, 보안 인증서·권한 파일을 이 단위로 발급·적용한다. [추정][^ref-405][^ref-009]

## 설명

Open-RMF 문서는 SROS 2 키스토어의 인클레이브로 RMF 구성요소의 권한을 나눈다고 설명한다. 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서 설비 명령 권한을 제한하는 단위로 논의된다.

## 관련 영역

- [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)
- [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)
- [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)

## 출처

[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-25

- 참고문헌 페이지: [ref-405](../references/ref-405.md), [ref-009](../references/ref-009.md)
