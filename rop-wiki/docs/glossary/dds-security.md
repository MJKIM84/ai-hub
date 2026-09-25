---
title: "DDS 보안 규격 (DDS-Security)"
type: glossary
term_ko: DDS 보안 규격
term_en: DDS Security (DDS-Security)
definition: DDS 참여자의 권한을 담은 서명된 XML 문서로, ROS 2 보안에서 참여자마다 도메인 보호 방식을 정한 거버넌스 파일과 함께 둔다.
related_areas: [11, 26, 28]
tags: [보안, OMG, ROS 2, 접근 제어]
status: published
created: 2026-09-24
updated: 2026-09-25
sources: [ref-009, ref-010]
version: 4
confidence: medium
---

[홈](../index.md) › [용어집](index.md) › DDS 보안 규격

# DDS 보안 규격 (DDS-Security)

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| DDS 보안 규격 | DDS Security | DDS — Data Distribution Service(데이터 분산 서비스). ROS 2 — Robot Operating System 2. 통용되는 한글 명칭이 없어 "DDS 보안 규격"으로 옮겼다 |

## 한 줄 정의

DDS 참여자의 권한을 담은 서명된 XML 문서로, ROS 2 보안에서 참여자마다 도메인 보호 방식을 정한 거버넌스 파일과 함께 둔다. [추정][^ref-009]

## 설명

분류 원문은 G. 안전·보안·지능·거버넌스의 설명에서 ROS 2의 보안 설계를 인용한다.

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문][^ref-009][^ref-010]

원문 12장은 ROS 2 설계 문서 "ROS 2 DDS-Security Integration"을 인증·암호화·접근통제 구조의 참고 자료로, "ROS 2 Robotic Systems Threat Model"을 로봇 시스템의 보안 위협과 대응 설계의 참고 자료로 든다. [사실][^ref-009][^ref-010] 규격 자체의 제정 기관은 객체 관리 그룹(OMG, Object Management Group)으로 검색 결과에 나타나고, 규격이 인증·접근 제어·암호화 등을 플러그인 구조로 정의한다는 설명도 검색 결과에 있으나 규격 본문은 열지 못했다. [추정][^cand-09] 규격의 현행 판 번호와 발행일은 미확인이다.

ROP 맥락에서 DDS-Security는 26. 사이버보안·접근권한·개인정보의 SCM 관점의 질문에 대한 통신 계층의 답 가운데 하나다.

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]

다만 이것은 ROS 2 위에서 동작하는 구성 요소 사이의 보안이며, 제조사 관제 API(Application Programming Interface)·클라우드 연동·업무 시스템 연계처럼 ROS 2 밖을 지나는 경로에는 별도의 인증·권한 설계가 필요하다. [추정] 원문이 기능 연동과 보안 연동을 함께 설계해야 한다고 한 것은, 9. 로봇·제조사 관제 연동의 어댑터를 만들 때 명령 권한의 범위를 같이 정한다는 뜻으로 읽을 수 있다. [의견]

## 관련 영역

- [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) — 장비 인증·통신 보호·명령 권한의 참조 규격이다.
- [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) — DDS가 담당하는 분산 통신 계층의 보안이 여기에 얹힌다.
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 규격 준수 구현 간 상호운용과 제조사 간 권한 정책을 다룬다.

관련 용어: [오픈 RMF (Open-RMF)](open-rmf.md)

## 출처

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24 (원문 미열람)
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24 (원문 미열람)
[^cand-09]: OMG, About the DDS Security Specification Version 1.2, 미확인, https://www.omg.org/spec/DDS-SECURITY/1.2/About-DDS-SECURITY, 접근일 2026-09-24 (원문 미열람)

- [ref-009](../references/ref-009.md), [ref-010](../references/ref-010.md)
- cand-09 는 검색 결과의 기관·제목·URL 로 실재만 확인한 후보 출처다. 정식 참고문헌 id 는 첫 검증 실행에서 부여하며, 그 전까지 이 출처에 기댄 주장은 [추정]으로 둔다.
- [표준·프레임워크 목록](../standards/index.md)
