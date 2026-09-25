---
title: "28. 표준·상호운용성·다사업자 거버넌스"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [VDA 5050, 의미적 버전 관리, 적합성 시험, 감사 추적, 데이터 권리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-407, ref-408, ref-608, ref-704, ref-253, ref-706, ref-707, ref-708, ref-709, ref-710, ref-711, ref-712, ref-713, ref-560, ref-715, ref-716, ref-717, ref-718]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 28. 표준·상호운용성·다사업자 거버넌스

# 28. 표준·상호운용성·다사업자 거버넌스

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]

## 3. 왜 중요한가

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가](../../topics/2026/2026-09-25-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 입고 → 출하

**시나리오:** 새 제조사 로봇 등록(입고)과 펌웨어 갱신 뒤 출하 마감 작업 유지(출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | (입고) 입고 물량에 대응하려고 새 제조사 로봇을 현장 관제에 등록한다. (출하) 출하 마감 전에 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀐다. |
| 작업 대상 | 해당 없음 |
| 수행 자원 | (출하) VDA 5050 3.0.0 에서 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송은 이동로봇 쪽 책임이다. [사실][^ref-031] (입고) MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. [추정][^ref-253][^ref-051] |
| 제약 | (출하) 변경 승인 전에 판 호환 시험과 수정 책임을 계약으로 정해 두어야 할 것으로 보인다. [추정][^ref-031][^ref-051] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | (출하) 관제가 헤더 version 으로 판 차이를 감지하고, 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 사전 시험이 없으면 출하 마감 전 작업 실패로 이어질 수 있을 것으로 보인다. [추정][^ref-031][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 입고 물량이 늘어 새 제조사 로봇을 들이는 날, 등록 단계에서 어떤 식별자로 제조사를 구분할지 정해 두면 뒤에 생기는 연동 오류를 누구의 것인지 가릴 수 있다. [추정][^ref-253][^ref-051]

며칠 뒤 한 제조사가 펌웨어를 올려 프로토콜 판이 바뀌면, 출하 마감 직전에 관제가 보낸 주문의 일부 필드가 거부될 수 있다. 이때 규격 불일치를 누가 고치고 판 변경을 누가 승인하는지가 미리 정해져 있어야 복구가 빨라지지만, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-704]

## 6. 대표 접근법과 기술

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

- VDA / VDMA / KIT IFL, VDA 5050 공식 저장소 README(발행일 미확인) — 변경 제안 절차, 계획 판, 지원 의무 부인 문구를 담아 규격 거버넌스를 읽는 기본 자료다. [사실][^ref-704]
- MassRobotics, AMR_Interop_Standard 저장소(발행일 미확인) — 신원·상태 보고 스키마만 두는 보고 중심 규격이다. [사실][^ref-253]
- gpue, vda5050-sim / ekusiadadus, vda5050-lab(발행일 미확인) — VDA 5050 시뮬레이션·적합성 시험 묶음과 MQTT 기록 진단 도구로, 개인 프로젝트이며 VDA·VDMA 공식 시험이 아닌 것으로 보인다. [추정][^ref-407][^ref-408]
- OSRA, Open-RMF 프로젝트 헌장(2024-03)과 정책·절차 저장소 — 오픈소스 관제 프레임워크의 운영·개정 권한 구조를 보여 준다. [추정][^ref-711][^ref-710]
- 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점(발행일 미확인) — 산업데이터 권리 규정을 해설한 국내 자료다. [사실][^ref-709]
- 국가기술표준원, 로봇 엘리베이터 탑승 KS 제정 보도자료(2021-11-11) — 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준을 다룬다. KS 번호는 미확인이다. [사실][^ref-717]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 인터페이스 판·적합성·책임 경계를 정하고 확인한다. [추정][^ref-031] | 연계 대상: 로봇의 위치 추정·주행 실행, 기능·시스템 안전(제조사 쪽). [추정][^ref-031] |
| 시설·설비 제어 | 승강기 연동 표준의 요구를 작업·경로 제약으로 반영한다. [의견] | 연계 대상: 승강기 안전기준·제어. [사실][^ref-717] |
| 상위 업무 시스템 | 상위 시스템에 여는 API 의 판 번호·폐기 예고 정책. [추정][^ref-706][^ref-713] | 연계 대상: 데이터 권리의 법률 해석과 계약 조건. [의견] |

VDA 5050 3.0.0 에서 교착 탐지·해소는 관제 쪽 기능이다. [사실][^ref-031] 그러나 교통 조율 알고리즘 자체와 기능·운영·시스템 안전 요구는 명세 범위 밖이다. [사실][^ref-031] 그래서 28. 표준·상호운용성·다사업자 거버넌스에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. [추정][^ref-031]

분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-704] ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. [사실][^ref-560] 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

28. 표준·상호운용성·다사업자 거버넌스는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-712][^ref-715][^ref-560][^ref-717]

- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 규격 판과 관제–로봇 책임 분리가 연동 구현의 전제다.
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 로봇 승강기 탑승 KS 같은 설비 연동 표준을 공유한다.
- [23. 시험·형식 검증·벤치마크](../f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 적합성 시험·인증을 새 로봇 연동 승인에 쓰는 방법을 다룬다.
- [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) — 펌웨어·프로토콜 판 이행과 폐기 예고가 수명주기 관리와 겹친다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) — 통합자의 시스템 수준 위험성평가를 누가 맡는지가 책임 경계의 핵심이다.
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) — 감사 추적 요구가 보안 표준에서 온다.

## 11. 열린 질문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-704]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-706]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-709]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)
[^ref-710]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-711]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-712]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-713]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-715]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-717]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
