(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-01
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 21. 상호운용 표준·적합성 (F. 연동)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 1건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- next_ref_id: ref-1423
- 새 출처 id 구간: ref-1423 ~ ref-1452 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1423 부터 순서대로 쓰고 ref-1452 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-11-01/target.json

```json
{
  "run_id": "2026-10-11-01",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 167,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 21,
    "area_name": "21. 상호운용 표준·적합성",
    "category": "F. 연동",
    "category_letter": "F"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=update, area=21"
}
```

### docs/categories/integration/interoperability-standards-and-conformance.md

```markdown
---
title: "21. 상호운용 표준·적합성"
type: area
category: "F. 연동"
area_no: 21
related_areas: [20, 22, 48, 51, 54, 57]
tags: [VDA 5050, 의미적 버전 관리, 적합성 시험, 감사 추적, 데이터 권리]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-407, ref-408, ref-608, ref-634, ref-253, ref-635, ref-636, ref-637, ref-638, ref-639, ref-704, ref-705, ref-706, ref-560, ref-707, ref-708, ref-709, ref-710]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 연동](index.md) › 21. 상호운용 표준·적합성

# 21. 상호운용 표준·적합성

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]

## 3. 왜 중요한가

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 왜 중요한가](../../topics/2026/2026-09-25-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 입고 → 출하

**시나리오:** 새 제조사 로봇 등록(입고)과 펌웨어 갱신 뒤 출하 마감 작업 유지(출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | (입고) 입고 물량에 대응하려고 새 제조사 로봇을 현장 관제에 등록한다(설명용 가상 설정). (출하) 출하 마감 전에 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀐다(설명용 가상 설정). [추정][^ref-031][^ref-051] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | (출하) VDA 5050 3.0.0 에서 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송은 이동로봇 쪽 책임이다. [사실][^ref-031] (입고) MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. [추정][^ref-253][^ref-051] |
| 제약 | (출하) 변경 승인 전에 판 호환 시험과 수정 책임을 계약으로 정해 두어야 할 것으로 보인다. [추정][^ref-031][^ref-051] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | (출하) 관제가 헤더 version 으로 판 차이를 감지하고, 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 사전 시험이 없으면 출하 마감 전 작업 실패로 이어질 수 있을 것으로 보인다. [추정][^ref-031][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 입고 물량이 늘어 새 제조사 로봇을 들이는 날, 등록 단계에서 어떤 식별자로 제조사를 구분할지 정해 두면 뒤에 생기는 연동 오류를 누구의 것인지 가릴 수 있다. [추정][^ref-253][^ref-051]

며칠 뒤 한 제조사가 펌웨어를 올려 프로토콜 판이 바뀌면, 출하 마감 직전에 관제가 보낸 주문의 일부 필드가 거부될 수 있다. 이때 규격 불일치를 누가 고치고 판 변경을 누가 승인하는지가 미리 정해져 있어야 복구가 빨라지지만, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634]

## 6. 대표 접근법과 기술

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

- VDA / VDMA / KIT IFL, VDA 5050 공식 저장소 README(발행일 미확인) — 변경 제안 절차, 계획 판, 지원 의무 부인 문구를 담아 규격 거버넌스를 읽는 기본 자료다. [사실][^ref-634]
- MassRobotics, AMR_Interop_Standard 저장소(발행일 미확인) — 신원·상태 보고 스키마만 두는 보고 중심 규격이다. [사실][^ref-253]
- gpue, vda5050-sim / ekusiadadus, vda5050-lab(발행일 미확인) — VDA 5050 시뮬레이션·적합성 시험 묶음과 MQTT 기록 진단 도구로, 개인 프로젝트이며 VDA·VDMA 공식 시험이 아닌 것으로 보인다. [추정][^ref-407][^ref-408]
- OSRA, Open-RMF 프로젝트 헌장(2024-03)과 정책·절차 저장소 — 오픈소스 관제 프레임워크의 운영·개정 권한 구조를 보여 준다. [추정][^ref-704][^ref-639]
- 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점(발행일 미확인) — 산업데이터 권리 규정을 해설한 국내 자료다. [사실][^ref-638]
- 국가기술표준원, 로봇 엘리베이터 탑승 KS 제정 보도자료(2021-11-11) — 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준을 다룬다. KS 번호는 미확인이다. [사실][^ref-709]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 인터페이스 판·적합성·책임 경계를 정하고 확인한다. [추정][^ref-031] | 연계 대상: 로봇의 위치 추정·주행 실행, 기능·시스템 안전(제조사 쪽). [추정][^ref-031] |
| 시설·설비 제어 | 승강기 연동 표준의 요구를 작업·경로 제약으로 반영한다. [의견] | 연계 대상: 승강기 안전기준·제어. [추정][^ref-709] |
| 상위 업무 시스템 | 상위 시스템에 여는 API 의 판 번호·폐기 예고 정책. [추정][^ref-635][^ref-706] | 연계 대상: 데이터 권리의 법률 해석과 계약 조건. [의견] |

VDA 5050 3.0.0 에서 교착 탐지·해소는 관제 쪽 기능이다. [사실][^ref-031] 그러나 교통 조율 알고리즘 자체와 기능·운영·시스템 안전 요구는 명세 범위 밖이다. [사실][^ref-031] 그래서 21. 상호운용 표준·적합성에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. [추정][^ref-031]

분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634] ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. [사실][^ref-560] 물류 이동로봇 플릿에 적용되는지는 미확인이다. 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

21. 상호운용 표준·적합성는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-705][^ref-707][^ref-560][^ref-709]

- [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) — 규격 판과 관제–로봇 책임 분리가 연동 구현의 전제다.
- [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) — 로봇 승강기 탑승 KS 같은 설비 연동 표준을 공유한다.
- [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 적합성 시험·인증을 새 로봇 연동 승인에 쓰는 방법을 다룬다.
- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 펌웨어·프로토콜 판 이행과 폐기 예고가 수명주기 관리와 겹친다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) — 통합자의 시스템 수준 위험성평가를 누가 맡는지가 책임 경계의 핵심이다.
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) — 감사 추적 요구가 보안 표준에서 온다.

## 11. 열린 질문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-634]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-635]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-638]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-704]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-707]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
```

### data/area_reflection_proposals.json (대상 영역 21. 상호운용 표준·적합성 에 대한 트랙 반영 제안 1건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-10-09-26",
      "date": "2026-10-09",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 21,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "IDS 1.0 의 적용 대상·요구 구조, 엔터티·속성 패싯, 값 제한·기수와 IFC 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례를 BIM 데이터 교환 요구·적합성 검사 수단으로(f17, f18, f19, f20, f21, f22).",
      "status": "제안"
    }
  ]
}
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/safety/safety-and-risk-management.md (요약)

```markdown
# 48. 안전·위험 관리

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
```

### docs/categories/security-and-privacy/authentication-authorization-and-isolation.md (요약)

```markdown
# 51. 인증·권한·격리

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장비·사용자 인증**: 로봇·설비·사용자를 인증한다
- **명령 권한 관리**: 누가 어느 로봇에 어떤 명령까지 내릴 수 있는지 정하고 강제한다
- **원격 접속·유지보수 계정**: 외부 유지보수 계정이 접속할 수 있는 범위와 기록을 관리한다
- **고객·현장 격리**: 고객·현장·방문자별로 데이터와 제어를 분리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 26번 영역 ‘사이버보안·접근권한·개인정보’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [옛 분류원문]

> 옛 질문: 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [옛 분류원문]

## 2. 핵심 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1419건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 2026-09-25 | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | https://github.com/gpue/vda5050-sim | 2026-09-25 | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | https://github.com/ekusiadadus/vda5050-lab | 2026-09-25 | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 2026-09-25 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 2026-09-25 | 아니오 |
| ref-634 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 미확인 | https://github.com/VDA5050/VDA5050 | 2026-09-25 | 예 |
| ref-635 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | https://semver.org/spec/v2.0.0.html | 2026-09-25 | 예 |
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 2026-09-25 | 아니오 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 2026-09-25 | 아니오 |
| ref-638 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 미확인 | https://spri.kr/posts/view/23480?code=industry_trend | 2026-09-25 | 아니오 |
| ref-639 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 미확인 | https://github.com/openrobotics/osra-policies-and-procedures | 2026-09-25 | 예 |
| ref-704 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 2024-03 | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf | 2026-09-25 | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | https://opcfoundation.org/certification/how-to-certify/ | 2026-09-25 | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | https://www.rfc-editor.org/info/rfc9745/ | 2026-09-25 | 아니오 |
| ref-707 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 2026-09-25 | 아니오 |
| ref-708 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 2018 | https://www.iso.org/standard/70636.html | 2026-09-25 | 아니오 |
| ref-709 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 2026-09-25 | 아니오 |
| ref-710 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025-06-04 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-element-proxy: 건물 요소 프록시 (Building Element Proxy (IfcBuildingElementProxy))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- buildingsmart-data-dictionary: buildingSMART 데이터 사전 (buildingSMART Data Dictionary (bSDD))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- domain-shift: 도메인 이동 (Domain Shift)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
- failure-explanation: 실패 설명 (Failure Explanation)
- falsification: 반증 기반 시험 (Falsification)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- finops: 핀옵스 (FinOps)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- generalized-voronoi-graph: 일반화 보로노이 그래프 (Generalized Voronoi Graph (GVG))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- gln-extension-component: GLN 확장 성분 (GLN Extension Component)
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- guidance-graph: 안내 그래프 (Guidance Graph)
- hallucination: 환각 (Hallucination)
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indirect-prompt-injection: 간접 프롬프트 주입 (Indirect Prompt Injection)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
- integrity-risk: 무결성 위험 (Integrity Risk)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic-on-finite-traces: 유한 트레이스 선형 시간 논리 (Linear Temporal Logic on Finite Traces (LTLf))
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- makespan: 메이크스팬 (Makespan)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- original-instructions: 원본 설명서 (Original Instructions)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- phased-rollout: 단계적 배포 (Phased Rollout (Staged Rollout))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-attestation: 원격 증명 (Remote Attestation)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- security-level-iec-62443: 보안 수준 (Security Level (SL, IEC 62443))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shift-handover: 교대 인수인계 (Shift Handover)
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- skos: 단순 지식 조직 체계 (Simple Knowledge Organization System (SKOS))
- slot-filling: 슬롯 채우기 (Slot Filling)
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
- software-in-the-loop: 소프트웨어 인 더 루프 (Software-in-the-Loop (SiL))
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- stakeholder-requirements-specification: 이해관계자 요구사항 명세 (Stakeholder Requirements Specification (StRS))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- state-script: 상태 스크립트 (State Script (Mender))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- task-dependency-graph: 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- trace-context: 추적 문맥 (Trace Context (W3C traceparent / tracestate))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-defined-property-set: 사용자 정의 속성 세트 (User-defined Property Set)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050-hibernation: 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-diagram: 워크플로 다이어그램 (Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안))
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [21] 에 걸린 48건 / 전체 369건)

```markdown
- oq-004 [열림] IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? (영역 5, 21)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 20, 21)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 21, 23)
- oq-025 [열림] 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? (영역 15, 21)
- oq-026 [열림] KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) (영역 5, 21)
- oq-027 [열림] ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? (영역 15, 21)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 21, 22)
- oq-044 [열림] 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? (영역 15, 21)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 20, 21, 54)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 21, 28)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 21, 34)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 21, 54)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 20, 21, 57)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 21, 48)
- oq-101 [열림] 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? (영역 21, 51)
- oq-105 [열림] 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? (영역 21, 47)
- oq-108 [열림] 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? (영역 21, 34)
- oq-109 [열림] ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? (영역 21)
- oq-110 [열림] EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? (영역 20, 21)
- oq-111 [열림] KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? (영역 21, 54)
- oq-112 [열림] 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? (영역 21, 32)
- oq-115 [열림] 제조사가 자사 로봇 지도(SLAM 지도)의 판을 바꿀 때 변경 내용과 판 식별자를 ROP 나 상위 관제에 알리는 계약·인터페이스 관행이나 공개 사례가 있는가? (영역 21, 57)
- oq-122 [열림] 산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? (관련 기존 질문: oq-109) (영역 21)
- oq-124 [열림] 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? (영역 8, 15, 21)
- oq-128 [열림] 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? (영역 10, 4, 21)
- oq-148 [열림] VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? (영역 4, 21, 5)
- oq-154 [열림] 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? (영역 6, 21, 5)
- oq-158 [열림] IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? (영역 7, 21, 4)
- oq-159 [열림] 국내 이기종 로봇 통합 관제 제품(크롬스 등)이 VDA 5050 이나 MassRobotics AMR 상호운용 표준을 지원하는지 공개 자료로 확인되는가? (영역 1, 21)
- oq-167 [열림] 국내 제조 공장에서 서로 다른 제조사의 AGV·AMR·모바일 매니퓰레이터를 VDA 5050 같은 표준 인터페이스로 하나의 관제 계층 아래 운영한 공개 사례가 있는가(확인된 국내 사례는 자체 로봇 도입과 정부 시범사업뿐이다)? (영역 62, 21)
- oq-182 [열림] 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? (영역 65, 22, 21)
- oq-190 [열림] 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? (영역 66, 21, 16)
- oq-191 [열림] 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? (영역 67, 22, 21)
- oq-195 [열림] SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? (영역 67, 21, 5)
- oq-200 [열림] 출처 충돌: LIF 의 판·날짜가 저장소 README 기준 1.0.0(2023-09)과 VDA 5050 3.0.0 이 인용한 VDMA 2024-03 으로 다르다. 어느 쪽이 현행이며 두 날짜는 같은 판을 가리키는가? (영역 16, 21)
- oq-202 [열림] IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? (영역 16, 21)
- oq-209 [열림] 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? (영역 41, 21)
- oq-232 [열림] 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (영역 49, 21)
- oq-237 [해결] 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? (영역 37, 21)
- oq-244 [열림] 싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가? (영역 2, 21)
- oq-246 [열림] 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? (영역 52, 20, 21)
- oq-270 [열림] 국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가? (영역 3, 21)
- oq-301 [열림] 로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가? (영역 41, 21)
- oq-332 [열림] VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? (영역 37, 21)
- oq-334 [열림] MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073) (영역 38, 21)
- oq-339 [열림] W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가? (영역 43, 21)
- oq-345 [열림] 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) (영역 20, 21, 24)
- oq-348 [열림] 국내 공공건축 BIM 납품 기준(건설산업 BIM 시행지침 등)이나 로봇 친화형 건축물 인증이 로봇 충전 공간·작업 스테이션을 BIM 객체·속성으로 납품하도록 요구하거나 그 IDS·속성 세트를 정한 사례가 있는가? (관련 기존 질문: oq-199) (영역 14, 21)
```

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### runs/2026-10-10-06/research.md

```markdown
# 리서치 브리프 2026-10-10-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-06 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 20. 로봇·제조사 관제 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — IO-AMRs 과제 문장(ref-258)이 원문 미열람이고 주관 기관·과제 단계(계획인지 완료인지)가 없음
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 출하 시나리오 하나뿐이고 '수행 자원' 행이 추정이며 직접 제어·위임 비교 자료 없음(oq-031). 연동 위치와 제어 수준을 나눠 보는 기준, 상업 시설·전시 시연 사례 없음
- 섹션 6. 대표 접근법과 기술 — 연결 단절 시 실행 의미와 상태 분리, 신호등 수준 연동의 정지 시간 전제·교착 시 사람 개입(oq-032), 상태·오류 변환의 실제 필드 매핑 사례(oq-033) 근거가 약함
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 발행일 미확인(oq-005), 공개 구현(free_fleet·ros_amr_interop·vda-5050-lib.js)의 판별 지원 범위와 Open-RMF 구역 기능의 개발 상태 미반영
- 섹션 8. 대표 연구와 자료 — Lopes 외 논문(ref-136) 저자 미확인·120 ms 지표 명칭과 측정 조건 미확인, Franke 외(ref-1429) 원문 미열람·워크숍 구성 미기재
- 섹션 10. 다른 연구영역과의 연결 — 21. 상호운용 표준·적합성(ISO 21423 단계), 47. AI·학습·적응과 모델 운영(MCP 연동)과의 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-031·oq-032·oq-033 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 발행일은 공식 자료에서 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-032 제조사 관제가 일시정지·재개만 허용하는 신호등 수준 연동에서 정지·교착 처리의 전제는 무엇인가? (섹션 6·11 겨냥)
4. oq-033 공개 구현은 로봇 상태·오류를 표준 필드로 어떻게 옮기는가? (섹션 6·11 겨냥)
5. oq-031 직접 제어와 제조사 관제 위임을 고르는 기준이나 비교 자료가 있는가? (섹션 5·11 겨냥)
6. 기존 8절·3절 연구 자료(Lopes 외, Franke 외, IO-AMRs)의 서지·측정 조건·단계는 원문에서 무엇으로 확인되는가? (섹션 3·8 겨냥)
7. VDA 5050·Open-RMF 공개 구현의 판별 지원 범위와 개발 중 기능은 무엇인가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 보도자료 'Version 3.0 of VDA 5050 released'의 본문 날짜는 2026-04-20(Berlin, April 20, 2026)이며, 보도자료 URL 은 260421 계열이다. | ref-032 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [사실] | VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목은 날짜를 2026-03-17(March 17, 2026)로 표시한다. | ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f3 | [사실] | VDA 가 배포하는 VDA 5050 3.0.0 공식 PDF 의 표지는 판 표기를 'Version 3.0.0, March 2026'으로 적어 월 단위(2026-03)까지만 밝힌다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [사실] | VDA 의 공식 자료 세 가지가 VDA 5050 3.0.0 의 날짜를 서로 다르게 표시한다: 카탈로그 2026-03-17, 보도자료 본문 2026-04-20, 명세 표지 2026-03. | ref-1423, ref-032, ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f5 | [의견] | VDA 5050 3.0.0 의 발행일은 하나로 확정하지 않고 서지에는 판 표기의 월(2026-03)을 적으며, 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)는 주석으로 함께 남기는 것이 맞아 보인다(oq-005 부분 답변). | ref-031, ref-032, ref-1423 | 아니오 | low | 2026-10-10 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §4.1 은 로봇이 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다고 정한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 주문에 딸린 동작·즉시 동작·구역 동작의 상태를 상태 메시지의 actionStates·instantActionStates·zoneActionStates 세 배열로 나눠 보고하게 하며, 구역 동작의 예정 상태 보고는 선택 사항이다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f8 | [의견] | 로봇이 단절 중에도 해제된 노드까지 주행을 이어 가므로(f6) ROP 어댑터는 연결 단절(connection 상태)을 곧 정지로 해석하지 말고, 연결 상태와 동작 실패(동작 상태 배열의 FAILED)를 별도 상태로 보존해 단절 시 실행 의미와 상태를 분리하는 것이 좋아 보인다. | ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f9 | [사실] | Open-RMF EasyTrafficLight API(rmf_fleet_adapter 2.14.0)의 moving_from() 경고는 로봇이 다음 체크포인트에서 멈출 시간이 있을 때만, 곧 정지 명령의 통신 지연과 로봇 최대 감속을 감안해 호출하라고 하며, 이를 어기면 MovingError·WaitingError 가 나고 교통 흐름이 끊기거나 교착될 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [사실] | 같은 헤더의 Blocker 설명은 해결할 수 없는 충돌로 교착이 생기면 RMF 교통 협상 시스템이 충돌 참여자를 충분히 제어하지 못하므로 사람 개입이 필요할 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | 신호등 수준으로 붙는 제조사 플릿의 연동 계약에는 정지 명령의 유무만이 아니라 정지 가능 시간(통신 지연·최대 감속)과 정지 확인 응답, 교착 시 사람 개입 경로를 함께 적는 것이 좋아 보이며, 제어 수준별 교통 성능을 같은 조건에서 비교한 자료는 여전히 찾지 못했다(oq-032 부분 근거). | ref-1424 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [의견] | 신호등 연동을 평가·재현할 때는 쓰는 rmf_fleet_adapter 패키지 판을 함께 기록하는 것이 좋아 보인다. 2.14.0(2026-09-26) 변경 이력에 EasyTrafficLight 의 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 들어 있기 때문이다. | ref-1398 | 아니오 | low | 2026-10-10 | — | — |
| f13 | [추정] | InOrbit 개발자 문서는 InOrbit 이 제어하는 로봇 플릿을 RMF core 에 잇는 오픈소스 전체 제어(full control) 플릿 어댑터를 제공해 여러 제조사 로봇의 중앙 교통 조정을 가능하게 한다고 밝힌다. | ref-1029 | 아니오 | low | 2026-10-10 | — | 벤더 주장 |
| f14 | [의견] | 연동 위치(제조사 관제 API 를 거치는지, 로봇에 직접 붙는지)와 제어 수준(전체 제어인지)은 따로 판단해 별도 항목으로 기록하고, 제어 권한은 경로 지정·교체, 정지, 진행 상태 반환으로 나눠 적는 것이 좋아 보인다(oq-031 판단 기준 보강). | ref-251, ref-1029 | 아니오 | low | 2026-10-10 | — | — |
| f15 | [사실] | Lopes 외(Applied Sciences 2025, 15(13), 7235, 2025-06-27) 논문은 본문 §6.2 에서 로봇 상태의 평균 갱신 간격(average update interval)을 약 120 ms, 사용자 화면 지연을 1초 미만으로 보고하며, 초록은 같은 값을 'average latency'로 표현한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f16 | [사실] | 같은 논문은 실험 시험 중 AMR·AGV 를 포함해 최대 20대를 화면·서버 성능의 큰 저하 없이 동시에 감시할 수 있었고 시험 기간 서버 가동률이 99.5% 이상이었다고 보고한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f17 | [사실] | 같은 논문의 §5.3(로봇 지도 작성·연결) 시험은 코임브라 공학연구소 기계공학과의 약 500 m² 실험실에서 수행됐으며, 120 ms·20대 결과를 어디서 측정했는지는 논문에 명시돼 있지 않다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f18 | [의견] | Lopes 외의 결과는 자동차 공장 적용을 목표로 한 실험실 연구의 감시 성능이므로, 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않고, 기존 '작업 상태 갱신 평균 지연 120 ms' 표현은 '로봇 상태 평균 갱신 간격 약 120 ms'로 고치는 것이 맞아 보인다. | ref-136 | 아니오 | low | 2026-10-10 | — | — |
| f19 | [사실] | Franke 외(Logistics Journal: Proceedings No.19, 2023-10-11) 연구는 2023년 봄 소프트웨어 기업 2곳·하드웨어 제조사 3곳·창고 사용자 1곳 등 여섯 회사가 참여한 워크숍으로 VDA 5050 개념에 기반한 새 표준 인터페이스 요구를 수집했다. | ref-1429 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | Franke 외 연구는 연동 요구 분석 자료로 분류하고, 실물 플릿을 비교한 실험이 아니므로 직접 제어와 제조사 관제 위임의 처리량 비교 근거로 쓰지 않는 것이 맞아 보인다. | ref-1429 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | ARM Institute 의 IO-AMRs 과제 소개는 주관 기관을 Siemens Technology 로, 협력 기관을 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 로 적는다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [사실] | IO-AMRs 과제 소개는 다중 지도 관리자·연결 계층·전역 플릿 관리자를 이전 ARM 지원 과제의 산출물을 활용해 만들 '계획'으로 서술해, 이 과제가 소개 시점에 계획 단계였음을 보여 준다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [의견] | IO-AMRs 소개는 과제 목표의 근거로만 쓰고 달성한 운영 성과의 근거로 쓰지 않으며, 3절의 목표 문장에는 주관 기관과 계획 단계라는 범위만 보태는 것이 맞아 보인다. | ref-258 | 아니오 | low | 2026-10-10 | — | — |
| f24 | [추정] | Open-RMF rmf_ros2 PR #516 'Add GoToZone feature'는 구역 이름을 받아 구역 안 경유점을 예약하는 기능을 제안하며 2026-10-10 기준 미병합 상태인 것으로 보이나, 이번 환경에서 PR 원문과 상태를 직접 확인하지 못했다. | ref-1425 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f25 | [사실] | Open Robotics Discourse 의 2026-05-04 Interop SIG 공지는 CHART 가 RMF-2.0 프로젝트로 개발한 새 기능을 단계적으로 공개하며 첫 단계가 시설 '구역(zones)' 관리 기능이고, 공지 시점에 이 기능이 검토 중(currently undergoing review)이라고 밝힌다. | ref-1426 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [의견] | 어댑터 기능 목록을 정리할 때는 배포판(태그)에 든 기능과 검토 중인 기능(예: Open-RMF 구역 기능)을 구분해 적는 것이 좋아 보인다. | ref-1426, ref-1425 | 아니오 | low | 2026-10-10 | — | — |
| f27 | [사실] | ros_amr_interop 1.1.1 의 MassRobotics 송신 예제 설정은 ROS 토픽 /we_b_robots/mode(std_msgs/String)를 operationalState 에, /troubleshooting/errorcodes 를 errorCodes 에 연결하고, 오류 코드는 쉼표로 구분한 문자열로 받아 MassRobotics 표준이 요구하는 배열로 바꾼다고 주석에 적는다. | ref-255 | 아니오 | medium | 2026-10-10 | — | — |
| f28 | [사실] | MassRobotics AMR 상호운용 표준 1.0 태그의 JSON 스키마는 상태 보고(statusReport)의 필수 필드를 uuid·timestamp·operationalState·location 넷으로 둔다. | ref-230 | 아니오 | medium | 2026-10-10 | — | — |
| f29 | [의견] | ros_amr_interop 예제는 ROS→MassRobotics 한 방향의 운용 상태·오류 매핑 사례일 뿐이므로 Open-RMF·VDA 5050·MassRobotics 세 체계의 공통 상태·오류 어휘 표준으로 일반화하지 않는 것이 맞아 보이며, 세 체계를 함께 다루는 표준 매핑은 이번에도 확인하지 못했다(oq-033 부분 근거). | ref-255, ref-230 | 아니오 | low | 2026-10-10 | — | — |
| f30 | [사실] | free_fleet 1.3.0 태그의 README 는 메시지를 CycloneDDS 의 dds_idlc 로 FleetMessages.idl 에서 생성한다고 설명하고, ROS 1·ROS 2 양쪽의 cyclonedds 판을 같게 맞춰야 한다고 권고하며, DDS 를 쓰지 않는 새 판을 준비 중이라고 적는다. | ref-256 | 아니오 | medium | 2026-10-10 | — | — |
| f31 | [의견] | 위키의 free_fleet 설명(현재 기본 브랜치의 zenoh 기반 Nav2·Nav1 어댑터)과 과거 태그 1.3.0 의 CycloneDDS 기반 설치 절차는 섞지 않고 판을 밝혀 적는 것이 좋아 보인다. | ref-256 | 아니오 | low | 2026-10-10 | — | — |
| f32 | [사실] | vda-5050-lib.js 의 v1.7.0(2026-04-29) 변경 이력은 VDA 5050 3.0 지원을 추가하며 새 Topic.ZoneSet·Topic.Responses 토픽, VdaVersion 의 '3.0.0', 3.0 용 사전 컴파일 검증기와 타입을 넣었다고 적는다. | ref-742 | 아니오 | medium | 2026-10-10 | — | — |
| f33 | [의견] | 어댑터에 VDA 5050 라이브러리를 쓸 때는 라이브러리 판과 지원 규격 판을 함께 고정하는 것이 좋아 보이며, 라이브러리가 선언한 3.0 지원은 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않는 것이 맞아 보인다. | ref-742 | 아니오 | low | 2026-10-10 | — | — |
| f34 | [추정] | InOrbit 은 Automate 2026 시연에서 Ati Robotics·Kärcher·Neura Robotics·Omron·Peer Robotics·Quasi Robotics·Unitree 7개사 로봇이 공유 공간에서 함께 임무를 수행하고, Slamcore·Guide Robotics 의 실시간 위치 추적(RTLS)으로 수동 차량까지 묶어 InOrbit 을 포함해 10개사가 협업했다고 밝힌다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | 벤더 주장 |
| f35 | [의견] | Automate 2026 시연의 '10개사'는 참여 기업 수(로봇 7·위치 추적 2·InOrbit 1)이지 로봇 대수나 AMR 제조사 수가 아니므로, 상용 운영 사례가 아닌 전시 시연으로 분류하는 것이 맞아 보인다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | — |
| f36 | [추정] | 카카오모빌리티는 2024년 로보티즈와 업무협약을 맺고 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용해 왔다고 발표했다(2026-03-16). | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | 벤더 주장 |
| f37 | [의견] | 카카오모빌리티–로보티즈 호텔 사례는 국내 플랫폼–로봇 제조사 연동 사례로 분류하되, 제어 위임 방식·API·로봇 대수가 공개되지 않아 한 현장에서 여러 제조사 플릿을 함께 운영한 증거나 직접 제어·위임 비교 근거(oq-031)로는 쓰지 않는 것이 맞아 보인다. | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | — |
| f38 | [추정] | 연계 대상: ISO 21423(산업용 이동로봇 통신·상호운용) 공식 카탈로그가 2026-10-10 기준 '60.00 Under publication' 단계를 표시한다는 외부 메모의 기록이 있으나, iso.org 가 403 으로 막혀 이번에 직접 확인하지 못했다. | ref-159 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f39 | [사실] | Open Robotics Discourse 의 Interop SIG 2026-07-02 세션 공지는 Open-RMF REST API 를 언어 모델이 호출할 수 있는 MCP 도구로 노출하는 서버와, 영어 명령을 다단계 RMF 임무로 바꿔 NVIDIA Isaac Sim 창고의 로봇이 Nav2 로 실행하는 에이전트(Nayantra)를 발표한다고 알린다. | ref-854 | 아니오 | medium | 2026-10-10 | — | — |
| f40 | [의견] | MCP 로 Open-RMF REST API 를 노출하는 시연은 47. AI·학습·적응과 모델 운영(및 12. 채팅으로 업무 지시·오케스트레이션)과의 연결 지점으로 제안할 만하나, 시뮬레이션 창고 시연이므로 실물 다사업자 플릿의 안정성 근거로 쓰지 않는 것이 맞아 보인다. | ref-854 | 아니오 | low | 2026-10-10 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1423 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | 벤더 문서 | medium | 2026-10-10 | https://developer.inorbit.ai/docs | 아니오 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp | 아니오 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외 17명 (Polytechnic University of Coimbra 등; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025-06-27 | 논문 | medium | 2026-10-10 | https://www.mdpi.com/2076-3417/15/13/7235 | 아니오 |
| ref-1429 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023-10-11 | 논문 | medium | 2026-10-10 | https://proc.logistics-journal.de/article/download/1067/1036/8465 | 아니오 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | 정부·연구기관 | medium | 2026-10-10 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 아니오 |
| ref-1425 | chart-singapore / CHART (open-rmf/rmf_ros2 GitHub) | Add GoToZone feature (rmf_ros2 pull request #516) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/pull/516 | 예 |
| ref-1426 | Open Robotics Discourse (OSRA Interop SIG) | Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature | 2026-05-04 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490 | 아니오 |
| ref-255 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/inorbit-ai/ros_amr_interop | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-10 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/free_fleet | 아니오 |
| ref-742 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/coatyio/vda-5050-lib.js | 아니오 |
| ref-1427 | InOrbit.AI | 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026 | 미확인 | 벤더 문서 | low | 2026-10-10 | https://www.inorbit.ai/automate-2026 | 아니오 |
| ref-1428 | 카카오모빌리티 | 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속 | 2026-03-16 | 벤더 문서 | low | 2026-10-10 | https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361 | 아니오 |
| ref-1200 | 아시아경제 | 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) | 2026-03-16 | 기사 | low | 2026-10-10 | https://view.asiae.co.kr/article/2026031610244491183 | 아니오 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-10 | https://www.iso.org/standard/86749.html | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md | 3, 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 3 — IO-AMRs 목표 문장(기존 내용 확인)에 주관 기관 Siemens Technology·협력 기관과 '계획 단계' 범위만 보탬(f21·f22·f23). / 섹션 5 — 연동 위치와 제어 수준을 따로 기록하는 기준(f14, InOrbit 문서 f13 은 벤더 주장 보강 근거로만; 제조사 관제 API 경유 전체 제어 조건은 '제약' 행 ref-251 에 이미 있어 중복 추가 안 함), 새 사례 두 개: 전시 시연(현장 유형 기타, f34·f35, 벤더 주장), 국내 호텔(현장 유형 상업 시설, f36·f37, 벤더 주장; 2. 사용 사례·요구·책임 범위의 ref-1200 사례와 같은 건이므로 '플랫폼–제조사 연동 사례' 분류 관점만 짧게). / 섹션 6(주제 페이지 2026-09-25-area09-s6 요약) — VDA 연결 단절 시 실행 의미와 상태 분리(f6~f8; '마지막으로 해제된 노드' 번역어는 대분류 개요와 같게, f6 사실은 개요에 이미 있으므로 영역 20 에는 상태 분리 관점으로), 신호등 연동의 정지 시간 전제·교착 시 사람 개입(f9~f11), 상태·오류 변환표 절에 ros_amr_interop→MassRobotics 필드 매핑 사례(f27~f29). / 섹션 7(주제 페이지 2026-09-25-area09-s7 표) — VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 공식 자료 세 날짜 표시로 교체(f1~f5), Open-RMF 신호등 연동 평가 시 패키지 판 기록(f12; 2.14.0 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 에 이미 있음), Open-RMF 구역 기능 개발 상태(f24 추정·f25·f26), free_fleet 1.3.0 판 구분(f30·f31), vda-5050-lib.js v1.7.0 3.0 지원(f32·f33). / 섹션 8(주제 페이지 2026-09-25-area09-s8) — Lopes 외 항목의 저자 '미확인'을 17명 저자·DOI 로, '작업 상태 갱신 평균 지연 120 ms'를 '로봇 상태 평균 갱신 간격 약 120 ms'로 정정하고 20대 감시·§5.3 실험실 범위 추가(f15~f18), Franke 외 항목에 워크숍 구성과 서지 보강(f19·f20). / 섹션 10(주제 페이지 2026-09-25-area09-s10) — 21. 상호운용 표준·적합성: ISO 21423 단계 기록은 추정으로 연결 제안 수준(f38, oq-027 과 겹치므로 링크만), 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션: MCP 로 Open-RMF REST API 노출 시연(f39·f40, oq-141 관련). / 섹션 11(주제 페이지 2026-09-25-area09-s11) — 분리 페이지의 '신규' 세 질문을 실제 id 로 표기(oq-031·oq-032·oq-033), 부분 근거: oq-005 ← f1~f5, oq-032 ← f9~f11, oq-033 ← f27~f29, oq-031 ← f14·f20·f37(답 아님, 판단 기준만). 모두 열림 유지. 새 질문 5건. 다음 실행 후보: 21. 상호운용 표준·적합성(ISO 21423 발행 확인, f38), 27. 다중 로봇 경로·교통 관리 — MAPF(신호등 연동 교착, f9~f11). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- Lopes 외 논문이 보고한 로봇 상태 평균 갱신 간격 약 120 ms 와 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 37. 관제 화면·실행 기록 | 근거: f15 | 종류: 일반
- ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반
- zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가? | 관련 영역: 20. 로봇·제조사 관제 연동, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f30 | 종류: 일반
- InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f34 | 종류: 일반
- 카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 64. 상업 시설 | 근거: f36 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-06/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 GitHub 릴리스 설명의 'March 19th, 2026'과 게시 시각(published_at)은 이 환경에서 확인하지 못해 출처로 넣지 않았다(발행일 null 유지).
    - f24: GoToZone PR #516(ref-1425)의 설명·미병합 상태는 GitHub 접근 차단으로 원문 대조 실패. 간접 근거로 2026-05-04 SIG 공지(ref-1426, f25)만 사실로 둠
    - f38: ISO 21423 카탈로그의 '60.00 Under publication' 단계는 iso.org 403 으로 확인 실패(ref-159 원문 미열람)
    - f15~f17: Lopes 외 120 ms·20대 결과의 측정 장소·로봇 구성·시험 기간은 논문에 명시돼 있지 않음
    - f30: free_fleet 1.3.0 태그 커밋일 미확인(published null)
    - f34·f36: Automate 2026 시연과 카카오모빌리티 호텔 사례는 벤더 발표만 있고 독립 확인 없음(ref-1200 은 보도자료를 옮긴 기사)
    - oq-031: 국내 물류센터의 직접 제어·위임 비중·비용·처리량 비교 자료는 이번에도 찾지 못함
- 범위 경계 위반 의심:
    - f38: ISO 21423 은 21. 상호운용 표준·적합성 쪽 내용이므로 claim 을 '연계 대상: '으로 시작하고 10절 연결 제안 수준으로만 씀
    - f9~f11: 신호등 연동의 교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 영역 20 에는 연동 계약 관점으로 한정
    - f39·f40: MCP·언어 모델 연동은 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션 쪽 내용이라 연결 제안으로만 씀
    - f36·f37: 호텔 사례의 업무 범위는 2. 사용 사례·요구·책임 범위·64. 상업 시설에 이미 있으므로 영역 20 에는 연동 사례 분류만
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 6건(ref-1423, ref-1424, ref-1425, ref-1426, ref-1427, ref-1428, 예약 구간 ref-1423~ref-1452 안), 재사용 15건. 메모 출처 매핑: n1·VDA 공식 PDF→ref-031, n3→ref-032, n4→ref-1423(신규), n5→ref-251, n6→ref-1424(신규, 위키에 EasyTrafficLight.hpp 출처 없음), n7→ref-136, n8→ref-1429, n9→ref-258, n10→ref-1398, n11→ref-1425(신규, 미열람), n12→ref-742, n13→ref-255, n14→ref-230, n15→ref-256, n16→ref-1427(신규; 기존 ref-177 은 RoboticsTomorrow 게재 보도자료라 다른 문서), n17→ref-1428(신규, 카카오모빌리티 보도자료 원문)+ref-1200(같은 내용을 옮긴 아시아경제 기사, 이번에 재열람해 호텔 이름 확인), n18→ref-854, n19→ref-159, n20→ref-1029. n2(GitHub 릴리스)는 넣지 않음. 간접 근거로 SIG 공지 ref-1426(신규) 추가. 검증 수정 반영: VDA 날짜는 세 공식 표시가 다르다는 것을 사실로, 하나로 확정하지 않는 것은 의견으로(f4·f5); 상태 배열 근거를 §6.6.9·§7.8 로(§7.7 아님, f7); '마지막으로 해제된 노드' 번역어를 대분류 개요와 맞춤(f6); Lopes 120 ms 를 '평균 갱신 간격'으로, 실험실 범위를 §5.3 지도 작성·연결 작업으로 좁힘(f15~f17); Franke 근거 쪽수 p.5(f19); IO-AMRs 는 주관 기관·계획 단계만 새로(f21·f22); 제조사 관제 API 경유 전체 제어는 5절 '제약' 행 기존 내용이라 중복 추가 안 함(f13 은 보강); EasyTrafficLight 2.14.0 수정은 의견으로만(f12); GoToZone PR·ISO 21423 단계는 추정·미열람(f24·f38); Automate·호텔은 벤더 주장·추정 유지. 교차 확인 0건: VDA 날짜 세 자료는 모두 VDA 계열, Open-RMF 헤더·변경 이력은 같은 프로젝트, ref-1200 은 ref-1428 을 옮긴 기사라 독립 출처가 아니다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-005 근거 f1~f5, oq-032 근거 f9~f11, oq-033 근거 f27~f29, oq-031 판단 기준 f14·f20·f37. 분리 페이지 11절의 '신규' 세 질문은 oq-031·oq-032·oq-033 이다. 메모의 새 질문 U1~U11 가운데 기존 질문과 겹치는 U1(oq-005)·U2(oq-031)·U3(oq-032)·U4(oq-033)·U11(oq-141 과 겹침)과 본문 근거가 없는 U6 은 빼고 U5·U7·U8·U9·U10 을 다듬어 5건을 올렸다. 현장 유형 사례 finding: 상업 시설(호텔, f36·f37), 기타(전시 시연, f34·f35). 용어 후보 없음(플릿 어댑터·VDA 5050·오픈 RMF 는 용어집에 있음). 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-10-10-05/research.md

```markdown
# 리서치 브리프 2026-10-10-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-05 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 28. 공용 자원·충전·에너지 최적화 |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 호텔 연구 수치(ref-103)가 원문 미열람·저자 미확인 상태로 '거의 두 배'로 요약돼 있음
- 섹션 5. 적용 사례 (현장 유형 명시) — 제약 행의 '임계 저충전 수준 이하에서는 충전소로 가는 주문만 보내야 한다'가 원문 권고(should)보다 강함. 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 분리 페이지 53행의 is_parking_spot/is_charger 출처 충돌 미해소(oq-069), VDA 선언값과 Open-RMF 설정의 단위·의미 구분 없음(oq-068)
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — 승강기 메시지의 필드 범위와 배분 정책 부재 구분 없음(oq-067), Open-RMF 충전·뮤텍스 관련 2026년 수정 이력과 적용 버전 미기재
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 배터리 열화·공용 충전기 비중첩 제약을 함께 푸는 최신 연구, 에너지 공급과 결합한 충전 연구 없음(oq-066)
- 섹션 11. 열린 질문 — oq-066·oq-067·oq-068 부분 근거, oq-069 해소 근거 미반영
- 정정 요청 없음(target.json corrections 비어 있음). 외부 조사 메모의 '수정' 항목 두 건(5절 제약 행, 6절 분리 페이지 충돌 문장)을 정정 근거로 다룸

## 조사 질문

1. 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
2. oq-069 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? (섹션 6·11 겨냥)
3. oq-068 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? (섹션 5·6·11 겨냥)
4. oq-067 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? (섹션 7·11 겨냥)
5. oq-066 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? (섹션 8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 팩트시트의 batteryCharging.criticalLowChargingLevel 은 임계 충전 수준을 백분율(percent)로 선언하는 float64 필드다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [사실] | 같은 필드 설명은 그 충전 수준 이하에서 관제가 충전소로 가도록 지시하는 주문만 보내는 것이 좋다고 권고 표현(should)으로 기술한다. | ref-031 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f3 | [의견] | 따라서 criticalLowChargingLevel 을 shall 수준의 의무 문구로 옮기거나 모든 로봇에 공통으로 정해진 충전 시작 비율로 설명해서는 안 되며, 제조사가 로봇별로 선언하는 값으로 다뤄야 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 팩트시트의 batteryCharging 객체는 criticalLowChargingLevel·maximumDesiredChargingLevel·minimumDesiredChargingLevel(모두 백분율)과 minimumChargingTime(초) 네 필드로 이루어진다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f5 | [사실] | Open-RMF fleet_adapter_template 의 config.yaml 은 recharge_threshold: 0.10 을 그 아래로는 로봇이 운행하지 않는 배터리 수준으로, recharge_soc: 1.0 을 충전 작업에서 채울 목표 배터리 수준으로 두며, 두 값은 0~1 비율로 적힌 템플릿 예시값이다. | ref-105 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [의견] | VDA 5050 의 백분율 선언값과 Open-RMF 의 비율 설정을 대조할 때는 단위를 먼저 맞추고, 운행 하한·충전 시작 판단·충전 목표를 별도 정책 항목으로 기록하는 편이 좋다. | ref-031, ref-105 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [추정] | 제조사가 팩트시트로 선언한 임계 충전 수준과 ROP 운영 설정(recharge_threshold) 가운데 어느 값을 자동으로 우선하는지에 관한 공통 조정 규칙은 확인한 두 원문에 없었다. | ref-031, ref-105 | 아니오 | low | 2026-10-10 | — | — |
| f8 | [사실] | Open-RMF rmf_traffic 의 그래프 API(Graph.hpp)는 경유점에 주차 지점(is_parking_spot/set_parking_spot)과 충전 지점(is_charger/set_charger)을 서로 다른 속성으로 정의하며, 충전 지점은 배터리 충전 수준이 임계값 아래로 떨어진 로봇이 보내지는 곳으로 설명된다. | ref-536 | 아니오 | medium | 2026-10-10 | — | — |
| f9 | [사실] | rmf_fleet_adapter 2.14.0 의 그래프 파서(parse_graph.cpp)는 경유점 옵션 is_parking_spot 을 set_parking_spot(true)로, is_charger 를 set_charger(true)로 각각 따로 변환한다. | ref-1543 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [의견] | 따라서 이 구현에서 충전소 경유점 지정은 is_charger 로 확인되며, is_parking_spot 만 지정한 경유점을 충전소 지정과 같은 뜻으로 취급하면 안 된다. 지원 작업 문서의 is_parking_spot 서술과 생긴 출처 충돌(6절 분리 페이지)은 구현 기준으로 해소된다. | ref-536, ref-1543 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [사실] | Open-RMF LiftRequest 메시지는 lift_name·request_time·session_id·request_type(세션 종료·AGV 모드·사람 모드)·destination_floor·door_state 필드로 이루어지고, LiftState 메시지는 세션 종료 요청을 보낼 때까지 승강기 제어권을 받은 session_id 를 보고한다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | — | — |
| f12 | [사실] | LiftRequest·LiftState 두 메시지에는 최대 점유 시간, 예약 시간창, 여러 요청의 목적층 묶음을 직접 지정하는 필드가 없다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | 제약 | — |
| f13 | [의견] | 따라서 승강기 세션 점유·종료 인터페이스가 공개되어 있다는 사실과 공정한 대기열·묶음 운행 같은 배분 정책이 정의되어 있다는 주장은 구별해야 하며, 메시지 정의만 본 결론이므로 다른 감독 구성요소에 타임아웃이나 대기열 구현이 없다는 뜻으로 넓히지 않는다. | ref-312, ref-286 | 아니오 | medium | 2026-10-10 | — | — |
| f14 | [사실] | Han 외(2025, Sensors)는 다층 호텔 배송 로봇의 경로 계획에서 승강기 노드를 암묵적 경유점으로 두고 문제를 다회 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)로 정식화해 적응형 대규모 이웃 탐색으로 푼다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f15 | [사실] | 이 논문은 고객 노드 60개 사례에서 승강기 운행 시간을 40초에서 100초로 늘리면 총 이동 시간이 약 225초에서 500초로 늘었다고 보고한다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 / 제약 | — |
| f16 | [의견] | 이 수치는 승강기 운행 시간에 대한 모델 민감도이며 실제 물류센터에서 측정한 승강기 대기열 손실값이 아니다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f17 | [사실] | 논문은 무작위·동적 승강기 운행 시간, 동적 수요 변동, 다중 로봇 협업·충돌 회피, 지능형 승강기 스케줄링 알고리즘을 후속 연구 과제로 남긴다. | ref-103 | 아니오 | medium | 2026-10-10 | 상업 시설 | — |
| f18 | [사실] | Li 외(2026, arXiv 2603.22731 프리프린트)는 작업 배정·서비스 순서·선택적 충전 결정·충전 방식 선택·공용 충전기 접근을 하나의 혼합 정수 선형 계획(Mixed-Integer Linear Programming, MILP)으로 함께 표현한다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f19 | [사실] | 이 모델의 목적함수는 총 배터리 열화, 충전기 대기, 납기 지연, 로봇 사이 열화 불균형을 함께 최소화한다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [사실] | 같은 논문 §2.6 의 식 (33)–(34)는 같은 충전기에서 일어날 수 있는 서로 다른 충전 세션 쌍(같은 로봇의 세션 쌍 포함)마다 순서 변수를 두어 충전 구간이 겹치지 않게 하는 비중첩 순서 제약이다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f21 | [사실] | 실험은 100×50 m 가상 창고, 동종 로봇, 표준·고속 두 충전 방식을 가정하며, §4.4 표 2 는 대표 사례(로봇 4·작업 40·충전기 2)의 '예시적 기대 평균(illustrative expected averages)'으로 총 열화가 규칙 기반 0.214 에서 0.098 로 준다고 보고하고, 기여 요약은 규칙 기반 대비 최대 54% 열화 감소를 적는다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [의견] | §4.4 가 비교표를 예시적 기대 평균으로 설명하고 열화를 축약 대리 모형으로 표현하므로, 최대 54% 열화 감소를 현장 배터리 수명 개선의 검증값으로 인용하지 않는 편이 좋다. | ref-403 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [추정] | Yang 외(2026, Processes)는 냉동 컨테이너 온도 제약 아래 항만 무인운반차(Automated Guided Vehicle, AGV)의 작업 스케줄링과 충전을, 태양광·풍력·에너지 저장 장치(Energy Storage System, ESS)를 갖춘 항만 마이크로그리드 운영과 결합해 운영비를 최소화하는 2단계 물류–에너지 협조 최적화 프레임워크를 제시한 것으로 소개된다. | ref-1544 | 아니오 | low | 2026-10-10 | 실외 | 원문 미열람 |
| f24 | [의견] | 이 항만 연구는 물류 작업과 에너지 공급을 함께 계획하는 충전 연구의 후보 자료일 뿐이며, 원문을 열지 못했으므로 비용 절감 수치나 국내 물류센터 적용 근거로 채택하지 않는다. | ref-1544 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f25 | [사실] | rmf_fleet_adapter 변경 이력의 2.12.0(2026-02-23) 판에는 충전 대기(WaitForCharge) 단계 완료 발행(#502)과 다음 작업에 충전량이 모자라면 충전기로 복귀하는 변경(#423)이 기록되어 있다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [사실] | 같은 변경 이력의 2.13.0(2026-06-15) 판에는 뮤텍스(Mutex) 잠금·해제 실행에서 생길 수 있는 교착을 고친 수정(#490)이 기록되어 있다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |
| f27 | [의견] | 따라서 Open-RMF 의 충전 작업 삽입·뮤텍스 그룹 기능을 인용할 때는 기능의 존재뿐 아니라 적용 버전과 이 수정들의 포함 여부를 함께 기록해야 하며, 이전 판이 모든 조건에서 교착 없이 동작했다는 근거로 쓰지 않는다. | ref-1398 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-1543 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-103 | Linghui Han, Junzhe Ding, Songtao Liu, Meng Meng (Sensors) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 2025-03-13 | 논문 | medium | 2026-10-10 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03-24 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2603.22731 | 아니오 |
| ref-1544 | Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI) | A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints | 2026-07-27 | 논문 | medium | 2026-10-10 | https://www.mdpi.com/2227-9717/14/15/2424 | 예 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md | 3, 5, 6, 7, 8, 11 | 갱신(차등): 섹션 3 — 호텔 연구 수치를 원문(§4.4 p.16) 기준 225→500 s 로 적고 저자·발행일 보강(f15), 모델 민감도임을 명시(f16) / 섹션 5 — 정정: 제약 행 '보내야 한다'를 권고(should)로 고치고 단위를 충전 수준(백분율)로 명시(f1·f2·f3); 상업 시설(호텔) 사례 추가(f14·f15·f16·f17) / 섹션 6(주제 페이지 요약) — 정정: 분리 페이지 53행 is_parking_spot/is_charger 충돌 문장을 구현 기준 해소로 교체(f8·f9·f10); VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분(f4·f5·f6·f7) / 섹션 7(주제 페이지 요약) — 승강기 메시지 전체 필드와 배분 정책 필드 부재(f11·f12·f13; 세션 종료 전 제어권 유지는 기존 내용 확인), rmf_fleet_adapter 2026년 수정 이력과 버전 기록(f25·f26·f27) / 섹션 8(주제 페이지 요약) — Li 외 열화·공용 충전기 MILP(f18~f22), Yang 외 항만 물류–에너지 협조 연구는 원문 미열람 후보(f23·f24) / 섹션 11 — oq-069 해소 제안(f8·f9·f10), oq-068 부분 근거(f4~f7), oq-067 부분 근거(f11~f13), oq-066 후보 자료(f23·f24), 새 질문 4건. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f20 | 종류: 일반
- 충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 5. 로봇 능력·작업 표현 | 근거: f5·f6 | 종류: 일반
- 배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21·f22 | 종류: 일반
- 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가? | 관련 영역: 28. 공용 자원·충전·에너지 최적화, 22. 설비·건물 시스템 연동 | 근거: f15·f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-069

## 자체 점검

- 출처 수: 10 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 3건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-05/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - f23·f24: Yang 외(ref-1544) 원문 미열람. Crossref 초록만 확인했고 비용 절감 수치·요금제·충전소 용량 모델은 미확인
    - f7: 임계 충전 수준과 recharge_threshold 의 우선순위 규칙 부재는 두 원문 범위 안의 확인이며, Open-RMF 다른 구성요소·VDA 5050 다른 절 전체를 뒤지지는 않음
    - f13: 승강기 감독(lift supervisor) 등 메시지 밖 구성요소의 타임아웃·대기열 구현은 조사하지 않음
    - f22: Li 외 결과를 실물 배터리 노화 실험·공개 재현 데이터로 확인하지 못함
    - VDA 5050 3.0.0 발표일은 근거 미확인이라 적지 않음(published null)
    - oq-066: 물류센터 로봇의 시간대별 전기 요금·최대 수요 전력 기준 충전 계획 연구와 국내 사례는 찾지 못함(항만 후보 자료만)
    - 섹션 5 의 물류창고 외 현장 유형 사례는 호텔(상업 시설)·항만(실외, 미열람) 외에는 찾지 못함
- 범위 경계 위반 의심:
    - f8·f9: 경유점 속성 정의는 15. 지도·공간·위치 모델과 겹치므로 이 영역에서는 충전소 지정 판별 근거로만 씀
    - f11~f13: 승강기 메시지 인터페이스는 22. 설비·건물 시스템 연동 소관이며 이 영역에는 공용 자원 배분 정책의 유무 근거로만 씀
    - f23·f24: 항만 마이크로그리드 운영은 ROP 직접 범위 밖(시설·에너지 설비 쪽 연계 대상)이며 충전 계획 연구 후보로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 3건(ref-1543~ref-1398, 예약 구간 ref-1543~ref-1572 안), 재사용 7건(ref-031·ref-105·ref-536·ref-312·ref-286 github_raw, ref-103·ref-403 webfetch). ref-103 은 기존 위키 출처(원문 미열람·저자 미확인)와 같은 논문으로, 이번이 첫 원문 열람이며 저자·발행일·doi 를 보강했다(메모의 '재열람' 표현은 틀림). ref-403 은 영역 24 등에서 쓰인 기존 id 를 재사용했다. 검증 수정 반영: criticalLowChargingLevel 을 '충전 수준(백분율)'로 표기(f1), 호텔 논문 셋째 문장을 의견으로 강등(f16), Li 외 식 (33)–(34)를 같은 충전기의 세션 쌍 비중첩 제약으로 정정하고 목적에 충전기 대기·불균형 포함(f19·f20), 변경 이력 원문 문구 정정(f25·f26), Yang 외 서술을 Crossref 초록 내용으로 교체(f23), Graph.hpp 주석 복사 오류 기록(f8), LiftRequest 에 lift_name 포함(f11), VDA 5050 발표일 null. VDA 5050 3.0.0 release notes 출처는 넣지 않았다. 교차 확인 0건: Graph.hpp 와 parse_graph.cpp, 두 승강기 메시지는 같은 프로젝트 자료라 독립 출처가 아니다. 현장 유형: 상업 시설(호텔, f14~f17), 실외(항만, f23, 미열람). 열린 질문: oq-069 해소 제안(f8~f10), oq-066·oq-067·oq-068 은 부분 근거만. 정정 요청 없음, 우선 지정 질문 없음.
```

### runs/2026-09-25-52/research.md

```markdown
# 리서치 브리프 2026-09-25-52

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-52 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 21. 온보딩·설정·현장 시운전 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음 (트랙 반영 제안: 도입 설치 시간의 원인)
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 새 제조사 로봇을 적치 운반에 추가하는 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음 (트랙 반영 제안 3건 대상)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 (트랙 반영 제안 2건 대상)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-022 관련

## 조사 질문

1. 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]
2. 새 로봇을 관제에 등록할 때 로봇 신원·기능·제약을 어떤 표준 메시지나 설정으로 받는가(VDA 5050 팩트시트, MassRobotics 신원 보고, Open-RMF 플릿 어댑터 설정)? (섹션 4·6·7 겨냥)
3. 지도·레이아웃·경로망은 새 현장에서 어떻게 만들고 관제에 넘기며, 이를 자동화·반자동화하는 연구는 무엇인가? (섹션 3·6·8 겨냥, 트랙 반영 제안 검토)
4. 제조사별 로봇 지도와 공통 지도 사이의 좌표 대응과 다층 정렬은 어떻게 설정하는가? (섹션 6 겨냥, 6. 지도·공간·위치 모델 연결)
5. 능력 기술 표준과 문서(매뉴얼) 해석 AI 는 로봇 등록·능력 매칭 작업을 어떻게 줄이려 하는가? (섹션 6·8 겨냥, 교차 규칙: 27. AI·학습·적응과 모델 운영 → 5·21)
6. 현장 시운전 전 안전 준비·가상 시운전·국내 시험·실증 체계는 무엇이 있는가? (섹션 7·9·10 겨냥, 한국 자료 우선)
7. oq-022 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 활용한 사례가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 팩트시트(factsheet) 토픽을 관제(fleet control)에서 이동로봇 설정을 돕는 파라미터·제조사 정보 전달 수단으로 두고, 관제가 즉시 동작 factsheetRequest 로 로봇에 팩트시트 전송을 요청할 수 있게 한다. | ref-031, ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 팩트시트 스키마는 유형 사양(typeSpecification), 물리 파라미터, 프로토콜 한계, 지원 프로토콜 기능·동작(protocolFeatures), 로봇 기하, 적재 사양(loadSpecification), 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)의 일곱 절을 필수로 두며, 스키마 설명은 이 정보가 관제 통합에 필요하고 시스템 계획·규모 산정·시뮬레이션에도 쓸 수 있다고 적는다. | ref-228 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 3.0.0 은 지도 배포를 위해 즉시 동작 downloadMap(지도 id·버전·내려받기 링크)·enableMap·deleteMap 을 두고, 관제가 내려받기를 지시하면 로봇이 지도 서버에서 지도를 받아 특정 버전을 활성화하는 흐름을 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 은 도입(implementation) 단계에서 경로 정의·스테이션 설정·로봇 속성 저장이 이루어진다고 설명하되 경로 설정 자체는 명세 범위 밖으로 두며, 경로망은 레이아웃 교환 형식(LIF)으로 관제에 가져올 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합사업자가 간선·노드·스테이션으로 이루어진 주행 레이아웃을 제3자 중앙 관제 시스템에 처음 넘겨주기 위한 비구속적 교환 형식이다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f6 | [사실] | MassRobotics AMR 상호운용 표준의 신원 보고(identityReport)는 uuid·시각·제조사명·모델·일련번호·기본 외곽 치수를 필수로, 최고 속도·예상 가동 시간·충전기 형식·지원 업체·제품 문서 URI·화물 종류·최대 화물 부피·최대 화물 무게를 선택으로 둔다. | ref-230 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f7 | [사실] | Open-RMF 플릿 어댑터 설정 파일은 새 플릿마다 속도·가속 한계, 외곽 반경, 배터리·기계 파라미터, 후진 가능 여부, 수행 가능한 작업 유형(순회·배송·청소), 작업 종료 후 동작, 로봇 좌표계와 RMF 좌표계를 대응점 쌍으로 변환하는 reference_coordinates, 제조사 관제 API 연결 정보를 채우게 한다. | ref-153 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF traffic-editor 는 기존 건축 도면·평면도를 배경 이미지로 불러오고, 알려진 두 점 사이 거리 측정으로 축척을 맞춘 뒤 정점·벽·문·승강기·주행 차선·충전기를 사람이 주석하게 하며, 층 사이 정렬은 수직으로 맞춘 기준점(fiducial) 쌍으로 변환을 계산한다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 는 대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor(rmf_site)를 공개하며, 이 도구의 프로젝트에서 시뮬레이션과 주행 그래프를 생성할 수 있다고 설명한다. | ref-643 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 제어권 없이 상태만 보고하므로, 새 플릿 온보딩 때 어느 수준으로 연동할지가 선택 사항이 된다. | ref-251 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f11 | [사실] | Beinschob 외(Robotics and Autonomous Systems 87권, 2017)는 다중 AGV 도입의 긴 설치 시간 원인으로 공장의 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문가의 수작업 경로망 설계를 들고, 레이저 스캐너 시스템으로 3D 의미 지도를 얻어 이를 반자동화하는 통합 시스템을 제안한다. | ref-217 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f12 | [추정] | EU CORDIS 의 PAN-Robots 과제 소개는 기존 표지를 활용한 위치 추정과 반자동 공장 탐사로 시스템 설치 기간을 6개월에서 2개월로 줄일 수 있다고 적지만, 이는 과제 측 보고값이며 비교 조건은 확인되지 않았다. | ref-265 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Heselden·Das(arXiv 2404.13499, 2024)는 지도 작성이 새 환경에 로봇을 배치할 때 시간이 많이 드는 과정이라고 보고, 전역 위치·물체 위치·위상·점유 정보 중심의 표준화된 지도 처리 방식과 빠진 데이터를 틀·절차적으로 생성하는 관리 스크립트를 제안한다. | ref-269 | 아니오 | medium | 2024-04 | — | 원문 미열람 |
| f14 | [사실] | 노주형 외(한국로봇학회 논문지 21권 1호, 2026)는 3D 라이다–관성 센서 기반 SLAM 탐사와 로봇팔로 승강기 버튼을 누르는 기능을 결합해 사물인터넷 장치 개조나 외부 시스템 연동 없이 다층 실내 지도를 처음부터 끝까지 자율로 구축하는 시스템을 제안한다. | ref-163 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f15 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 은 공정·제품 요구와 자원 능력을 함께 모델링해 요구 능력과 제공 능력을 비교하고 생산 공정의 계획·오케스트레이션을 지원하도록 만든 자산관리셸 서브모델 명세다. | ref-229 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | Vieira da Silva 외(arXiv 2307.00827, ETFA 2023)는 새 자원과 기능의 통합 공수를 줄이려는 플러그 앤 프로듀스(Plug and Produce)를 위해 능력·스킬을 기술하는 두 접근(온톨로지 기반 형식 기술, 자산관리셸 서브모델 표준화)이 서로 호환되지 않는다고 보고 둘 사이의 대응을 제안한다. | ref-037 | 아니오 | medium | 2023-07 | — | 원문 미열람 |
| f17 | [사실] | Vieira da Silva 외(arXiv 2406.07962, 2024)는 능력의 자연어 설명을 소수 예시 프롬프트에 넣어 LLM(Large Language Model, 대규모 언어 모델)으로 능력 온톨로지를 생성하고, 구문 검사·모순 검사·환각과 누락 요소 검사를 LLM 과 반복하는 방식으로 결과를 자동 검증하는 방법을 제안한다. | ref-637 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f18 | [사실] | 연계 대상: ISO 3691-4:2023 은 무인 산업용 트럭과 그 시스템의 안전 요구사항과 검증 수단을 정하고, 트럭이 안전하게 운행하도록 운행 구역을 준비하는 요구를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f19 | [사실] | 한국산업기술시험원(KTL)과 한국통합물류협회(KILA)는 2026-07-23 물류로봇·자동화 설비의 시험·인증과 표준화 협력 업무협약을 맺고, AMR·AGV·팔레타이징 로봇·모바일 매니퓰레이터·자율주행 지게차의 성능·안전성 검증을 KTL 테스트베드와 회원사 물류센터를 잇는 연구개발–시험평가–현장 실증 체계로 지원하겠다고 밝혔다. | ref-639 | 아니오 | low | 2026-07-24 | — | 원문 미열람 |
| f20 | [추정] | Siemens 는 고객사례에서 IDC 가 가상 시운전(virtual commissioning)으로 코드를 시스템 설계와 대조 검증해 현장에서 큰 변경이 필요 없었고 가동 개시를 3주 앞당겼다고 설명한다. | ref-640 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f21 | [추정] | f1~f8·f11·f13 을 종합하면 새 제조사 로봇이나 새 현장을 추가할 때 반복되는 작업은 로봇 신원·기능·제약 등록(팩트시트·신원 보고·어댑터 설정), 지도·레이아웃·경로망 작성과 가져오기, 제조사 지도와 공통 지도의 좌표 대응, 연동 수준 선택으로 나눌 수 있고, 앞의 등록 항목은 표준 메시지로 받을 수 있으나 경로망 설계와 좌표 대응은 여전히 사람의 설정 작업으로 남는 것으로 보인다. | ref-031, ref-228, ref-230, ref-153, ref-079, ref-217, ref-269 | 아니오 | low | 2026-09-25 | 적치 / 수행 자원 | — |
| f22 | [추정] | 이번에 확인한 범위의 팩트시트 스키마 최상위 절과 신원 보고 필드에는 제조사 지도와 공통(관제) 지도 사이의 좌표 대응을 담는 항목이 보이지 않고, Open-RMF 는 이를 현장별 어댑터 설정(reference_coordinates)으로 두므로, 좌표 정합은 현장 시운전의 설정·검증 항목으로 남는 것으로 보인다. | ref-228, ref-230, ref-153 | 아니오 | low | 2026-09-25 | 적치 / 제약 | — |
| f23 | [추정] | 연계 대상: 로봇 자체의 SLAM 지도 작성·위치 추정·센서 교정은 제조사 몫이고, 관제 인터페이스가 제공하는 것(팩트시트 요청, 지도 배포 지시, 레이아웃 가져오기, 어댑터 설정)을 보면 이종 로봇을 연결하는 ROP 는 로봇 등록 정보의 수집·검증, 레이아웃·좌표 대응 설정, 연동 수준 결정과 그 설정의 버전 관리를 맡는 경계가 될 것으로 보인다. | ref-031, ref-153, ref-251 | 아니오 | low | 2026-09-25 | 수행 자원 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-251 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-079 | Open Robotics | Programming Multiple Robots with ROS 2 — traffic-editor | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-153 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-229 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020 Submodel Capability Description 1.0 — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA | 2023-09 | 표준 | medium | 2026-09-25 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-217 | Beinschob, P. 외 | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |
| ref-269 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 2024-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2404.13499 | 예 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.00827 | 예 |
| ref-637 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-639 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | 기사 | low | 2026-09-25 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 예 |
| ref-640 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 미확인 | 벤더 문서 | low | 2026-09-25 | https://resources.sw.siemens.com/en-US/case-study-idc/ | 예 |
| ref-265 | European Commission CORDIS | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철 (한국로봇학회) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |
| ref-643 | Open Robotics (open-rmf/rmf_site) | rmf_site — README (RMF Site Editor) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_site | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f11·f13(설치 시간 원인, 트랙 반영 제안 2026-09-25-22 재확인), f12(PAN-Robots 6→2개월, 추정), f21(SCM 질문 연결) / 4절 용어: 팩트시트(f1·f2, 기존 용어), 신원 보고(f6), LIF(f5, 기존 용어), 기준점(f8), 가상 시운전(f20), 플러그 앤 프로듀스(f16) / 5절 시나리오: 적치 단계에 새 제조사 AMR 추가 — 수행 자원 f6·f7·f21, 제약 f22·f18, 예외·성과 f12·f20 / 6절 접근법: 표준 등록 메시지 f1·f2·f6, 어댑터 설정 f7, 평면도 주석·측정 축척 f8·f9(트랙 반영 제안 2026-09-25-11 재확인), 연동 수준 선택 f10, 반자동·자율 지도 작성 f11·f13·f14(트랙 반영 제안 2026-09-25-19 재확인), 능력 기술·매칭 f15·f16, 문서 해석 AI f17 / 7절 표준·오픈소스: VDA 5050(f1~f4), LIF(f5), MassRobotics(f6), Open-RMF(f7~f10), IDTA 02020(f15), ISO 3691-4(f18, 연계 대상), 국내 KTL–KILA 체계(f19) / 8절 연구: f11·f13·f14·f16·f17 / 9절 범위: f23(로봇 자체 SLAM·교정은 연계 대상), f18 / 10절 연결: 5. 로봇 능력·작업 온톨로지(f15~f17), 6. 지도·공간·위치 모델(f8·f13·f22), 9. 로봇·제조사 관제 연동(f1·f6·f7·f10), 10. 설비·건물 시스템 연동(f14 승강기), 22. 시뮬레이션·예측용 디지털 트윈(f2·f20), 23. 시험·형식 검증·벤치마크(f19), 24. 자산·소프트웨어 수명주기 관리(f3 지도 버전), 25. 안전·위험 관리(f18), 27. AI·학습·적응과 모델 운영(f17, 교차 규칙) / 11절 열린 질문: oq-022(미해결)와 새 질문 2건. 트랙 반영 제안 가운데 MiR·OTTO 벤더 주장(ref-271 등), Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 이번에 다시 확인하지 않아 다음 실행 후보로 남긴다 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 가상 시운전 | Virtual Commissioning | 제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다. |
| 플러그 앤 프로듀스 | Plug and Produce | 새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다. |
| 신원 보고 | Identity Report (MassRobotics identityReport) | MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동 | 근거: f21 | 종류: 일반
- 제조사 로봇 지도와 공통 관제 지도 사이 좌표 대응(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 항목마다 단일 출처(f1 의 두 출처는 같은 저장소라 독립 아님)
    - f11·f13·f14·f16·f17·f18: 원문 미열람, 검색 요약 범위
    - f12 PAN-Robots 6→2개월: 과제 측 보고값, 비교 조건 미확인
    - f19 KTL–KILA 협약: 기사만 확인, 기관 보도자료 원문 미확인
    - f20 Siemens 가상 시운전 3주 단축: 벤더 주장, 독립 확인 없음
    - f22: 팩트시트 최상위 절과 신원 보고 필드 범위의 부재 관찰이며 하위 필드 전체 확인 아님
    - ISO 3691-4 의 시운전 절차·통합사업자 책임 구분은 제3자 해설에서만 보여 finding 으로 내지 않음
    - oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 한국어 검색 2회에서 찾지 못함
- 범위 경계 위반 의심:
    - f18: ISO 3691-4 는 설비·차량 안전 영역(25. 안전·위험 관리, 분류 원문 9장 연계)이라 '연계 대상: '으로 표시하고 운행 구역 준비 요구만 시운전 제약으로 연결
    - f23: 로봇 자체 SLAM·위치 추정·센서 교정은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역으로 구분
    - f14: 로봇팔 승강기 조작 자율 지도 작성은 로봇 자체 기능 연구이므로 8절 연구 사례로만 두고 ROP 직접 범위로 서술하지 않도록 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-230(재사용), ref-228·ref-079·ref-153·ref-229·ref-046·ref-643(신규). 그 밖의 신규 출처(ref-217~ref-163)와 재사용 ref-251 는 원문 미열람(신뢰도 상한 medium, 모든 finding medium 이하). 검색 18회/30, 신규 출처 15건/15(ref-228~ref-643, 예약 구간 안) — 신규 출처 상한 도달로 MiR·OTTO 벤더 문서, Boniardi 외 2019, 다중 AGV 경로망 자동 설계(IEEE T-ASE 2024), Rüdt 외 2025, 문서 해석 LLM(기술 매뉴얼 지식 추출) 논문은 추가하지 않았다. 입력의 참고문헌 목록이 요약본(0건 표시)이라 트랙 반영 제안이 인용한 ref-217·ref-265·ref-269 등의 서지 정보를 몰라 재사용하지 못하고, 같은 문헌(Beinschob 외 2017, PAN-Robots CORDIS, Heselden·Das 2024)을 새 id(ref-217·ref-265·ref-269)로 다시 적었다 — 같은 URL 이면 퍼블리셔가 기존 id 로 합쳐야 한다. ref-251 는 이전 브리프(2026-09-25-50) 값을 재인용. 트랙 반영 제안 6건 가운데 traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)는 이번 finding 으로 재확인했고, 나머지는 페이지 제안 rationale 에 다음 실행 후보로 적었다. 한국 자료: KTL–KILA 협약(f19, 기사), 한국로봇학회 논문(f14). 한국어 검색에서 나온 블로그·업체 홍보 글은 쓰지 않았다. 교차 규칙: 문서 해석 AI(f17)는 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 연구 방법으로 27. AI·학습·적응과 모델 운영 연결을 제안. 8. 실시간 세계 상태·데이터 일관성 관련 주장 없음, 22. 시뮬레이션·예측용 디지털 트윈은 가상 시운전(f20)·팩트시트의 시뮬레이션 용도(f2) 연결로만 제안. 정정 요청 없음. oq-022 는 해결하지 못함.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.
…(발췌: 전체 207,642자 중 앞 36,974자)
````

### data/source_texts/ref-051.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "state",
    "description": "State of the mobile robot.",
    "subtopic": "/state",
    "type": "object",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "orderId",
        "orderUpdateId",
        "lastNodeId",
        "lastNodeSequenceId",
        "nodeStates",
        "edgeStates",
        "driving",
        "actionStates",
        "instantActionStates",
        "powerSupply",
        "operatingMode",
        "errors",
        "safetyState"
    ],
    "properties": {
        "headerId": {
            "type": "integer",
            "description": "headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message."
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot."
        },
        "maps":{
            "type": "array",
            "description": "Array of map-objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/map"
			}
        },
        "zoneSets":{
            "type": "array",
            "description": "Array of zoneSet objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/zoneSet"
			}
        },
        "orderId": {
            "type": "string",
            "description": "Unique order identification of the current order or the previous finished order. The orderId is kept until a new order is received. Empty string (\"\") if no previous orderId is available."
        },
        "orderUpdateId": {
            "type": "integer",
            "description": "Order Update Identification to identify that an order update has been accepted by the mobile robot. 0 if no previous orderUpdateId is available."
        },
        "lastNodeId": {
            "type": "string",
            "description": "Node ID of last reached node or, if mobile robot is currently on a node, current node (e.g., \"node7\"). Empty string (\"\") if no lastNodeId is available."
        },
        "lastNodeSequenceId": {
            "type": "integer",
            "description": "sequenceId of the last reached node or, if the mobile robot is currently on a node, sequenceId of current node. 0 if no lastNodeSequenceId is available."
        },
		"nodeStates": {
            "type": "array",
            "description": "Array of nodeState-Objects, that need to be traversed for fulfilling the order. Empty list if idle.",
            "items": {
                "$ref": "#/definitions/nodeState"
            }
        },
        "edgeStates": {
            "type": "array",
            "description": "Array of edgeState-Objects, that need to be traversed for fulfilling the order, empty list if idle.",
            "items": {
				"$ref": "#/definitions/edgeState"
			}
        },
        "plannedPath": {
            "$ref": "#/definitions/plannedPath"
        },
        "intermediatePath": {
            "$ref": "#/definitions/intermediatePath"
        },
        "mobileRobotPosition": {
            "$ref": "#/definitions/mobileRobotPosition"
        },
        "velocity": {
            "type": "object",
            "description": "The mobile robot's velocity in mobile robot coordinates",
            "properties": {
                "vx": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its x direction",
                    "unit": "m/s"
                },
                "vy": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its y direction",
                    "unit": "m/s"
                },
                "omega": {
                    "type": "number",
                    "description":"The mobile robot's turning speed around its z axis.",
                    "unit": "rad/s"
                }
            }
        },
        "loads": {
            "type": "array",
            "description": "Loads, that are currently handled by the mobile robot. Optional: If mobile robot cannot determine load state, leave the array out of the state. If the mobile robot can determine the load state, but the array is empty, the mobile robot is considered unloaded.",
            "items": {
                "$ref": "#/definitions/load"
            }
        },
        "driving": {
            "type": "boolean",
            "description": "True: indicates that the mobile robot is driving and/or rotating. Other movements of the mobile robot (e.g., lift movements) are not included here.\nFalse: indicates that the mobile robot is neither driving nor rotating."
        },
        "paused": {
            "type": "boolean",
            "description": "True: mobile robot is currently in a paused state, either because of the push of a physical button on the mobile robot or because of an instantAction. The mobile robot can resume the order.\nFalse: The mobile robot is currently not in a paused state."
        },
        "newBaseRequest": {
            "type": "boolean",
            "description": "True: mobile robot is almost at the end of the base and will reduce speed if no new base is transmitted. Trigger for fleet control to send new base\nFalse: no base update required."
        },
		"zoneRequests": {
            "description": "Array of zoneRequest objects that are currently active on the mobile robot. Empty array if no zone requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/zoneRequest"
            }
        },
        "edgeRequests": {
            "description": "Array of edgeRequest objects that are currently active on the mobile robot. Empty array if no edge requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/edgeRequest"
            }
        },
        "distanceSinceLastNode": {
            "type": "number",
            "description": "Used by line guided vehicles to indicate the distance it has been driving past the lastNodeId. Distance is in meters."
        },
        "actionStates": {
            "type": "array",
            "description": "Array of the current actions and the actions which are yet to be finished. This may include actions from previous nodes that are still in progress\nWhen an action is completed, an updated state message is published with actionStatus set to finished and if applicable with the corresponding resultDescriptor. The actionStates are kept until a new order is received.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "instantActionStates": {
            "type": "array",
            "description": "Array of all instant action states that the mobile robot received. Empty array if the mobile robot has not received any instant actions. Instant actions are kept in the state until restart or action clearInstantActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "zoneActionStates": {
            "type": "array",
            "description": "Array of all zone actions that are in an end state or are currently running; sharing upcoming actions is optional. Zone action states are kept in the state message until restart or action clearZoneActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "powerSupply": {
            "$ref": "#/definitions/powerSupply"
        },
        "operatingMode": {
            "type": "string",
            "description": "Current operating mode of the mobile robot.",
            "enum": [
                "STARTUP",
                "AUTOMATIC",
                "SEMIAUTOMATIC",
                "INTERVENED",
                "MANUAL",
                "SERVICE",
                "TEACH_IN"
            ]
        },
        "errors": {
            "type": "array",
            "description": "Array of error-objects. All active errors of the mobile robot should be in the list. An empty array indicates that the mobile robot has no active errors.",
            "items": {
				"$ref": "#/definitions/error"
            }
        },
        "information": {
            "type": "array",
            "description": "Array of info-objects. An empty array indicates, that the mobile robot has no information. This should only be used for visualization or debugging – it must not be used for logic in fleet control.",
            "items": {
				"$ref": "#/definitions/info"
            }
        },
        "safetyState": {
            "$ref": "#/definitions/safetyState"
        }
    },
    "definitions": {
		"map": {
			"type": "object",
			"title": "map",
			"required": [
				"mapId",
				"mapVersion",
				"mapStatus"
			],
			"properties": {
				"mapId": {
					"type": "string",
					"description": "ID of the map describing a defined area of the mobile robot's workspace."
				},
				"mapVersion": {
					"type": "string",
					"description": "Version of the map."
				},
				"mapDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor"
				},
				"mapStatus": {
					"type": "string",
					"description": "Information on the status of the map indicating, if a map version is currently used on the mobile robot. ENABLED: Indicates this map is currently active / used on the mobile robot. At most one map with the same mapId can have its status set to ENABLED.<br>DISABLED: Indicates this map version is currently not enabled on the mobile robot and thus could be enabled or deleted by request.",
					"enum": [
						"ENABLED",
						"DISABLED"
					]
				}
			}
		},
		"zoneSet": {
			"type": "object",
			"title": "zoneSet",
			"required": [
				"zoneSetId",
				"mapId",
				"zoneSetStatus"
			],
			"properties": {
				"zoneSetId": {
					"type": "string",
					"description": "Unique identifier of the zone set that is currently enabled for the map.<br> This field shall be left empty only if the mobile robot has no zones defined for the corresponding map."
				},
				"mapId": {
					"type": "string",
					"description": "Identifier of the corresponding map."
				},
				"zoneSetStatus": {
					"type": "string",
					"description": "ENABLED: Indicates this zone set is currently active / used on the mobile robot. At most one zone set for each map can have its status set to ENABLED. DISABLED: Indicates this zone set is currently not enabled on the mobile robot and thus could be enabled or deleted by fleet control.",
					"enum": [
						"ENABLED",
						"DISABLED"
					]
				}
			}
		},
		"nodeState": {
			"type": "object",
			"title": "nodeState",
			"required": [
				"nodeId",
				"sequenceId",
				"released"
			],
			"properties": {
				"nodeId": {
					"type": "string",
					"description": "Unique node identification"
				},
				"sequenceId": {
					"type": "integer",
					"description": "Sequence ID to discern multiple nodes with same nodeId."
				},
				"nodeDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor."
				},
				"released": {
					"type": "boolean",
					"description": "True: indicates that the node is part of the base. False: indicates that the node is part of the horizon."
				},
				"nodePosition": {
					"type": "object",
					"description": "Node position. Optional: Fleet control has this information. Can be sent additionally, e.g., for debugging purposes.",
					"required": [
						"x",
						"y",
						"mapId"
					],
					"properties": {
						"x": {
							"type": "number"
						},
						"y": {
							"type": "number"
						},
						"theta": {
							"type": "number",
							"unit": "rad",
							"minimum": -3.14159265359,
							"maximum": 3.14159265359
						},
						"mapId": {
							"type": "string"
						}
					}
				}
			}
		},
		"edgeState": {
			"type": "object",
			"required": [
				"edgeId",
				"sequenceId",
				"released"
			],
			"properties": {
				"edgeId": {
					"type": "string",
					"description": "Unique edge identification"
				},
				"sequenceId": {
					"type": "integer",
					"description": "Sequence ID to differentiate between multiple edges with the same edgeId"
				},
				"edgeDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor."
				},
				"released": {
					"type": "boolean",
					"description": "True indicates that the edge is part of the base. False indicates that the edge is part of the horizon."
				},
				"trajectory": {
					"$ref": "#/definitions/trajectory",
					"description": "Reports the trajectory that has been defined a priori within a layout or was sent for this edge as part of the order."
				}
			}
		},
		"trajectory": {
            "type": "object",
            "description": "The trajectory is to be communicated as a NURBS and is defined in chapter 6.7 Implementation of the Order message. Trajectory segments reach from the point, where the mobile robot starts to enter the edge to the point where it reports that the next node was traversed.",
            "required": [
                "controlPoints"
            ],
            "properties": {
                "degree": {
                    "type": "integer",
                    "description": "Defines the number of control points that influence any given point on the curve. Increasing the degree increases differentiability. If not defined, the default value is 1.",
                    "minimum": 1
                },
                "knotVector": {
                    "type": "array",
                    "description": "Sequence of parameter values that determine where and how the control points affect the NURBS curve. knotVector has size of number of control points + degree + 1.",
                    "items": {
                        "type": "number",
                        "maximum": 1.0,
                        "minimum": 0.0
                    }
                },
                "controlPoints": {
                    "type": "array",
                    "description": "List of JSON controlPoint objects defining the control points of the NURBS, which includes the beginning and end point.",
                    "items": {
                        "type": "object",
                        "required": [
                            "x",
                            "y"
                        ],
                        "properties": {
                            "x": {
                                "type": "number"
                            },
                            "y": {
                                "type": "number"
                            },
                            "weight": {
                                "type": "number",
                                "description": "The weight, with which this control point pulls on the curve. When not defined, the default will be 1.0."
                            }
                        }
                    }
                }
            }
        },
		"plannedPath": {
			"type": "object",
            "description": "Represents a path within the robot's currently active order as NURBS.",
            "required": [
                "trajectory"
            ],
            "properties": {
                "trajectory": {
                    "$ref": "#/definitions/trajectory"
                },
                "traversedNodes": {
                    "type": "array",
                    "description": "Array of nodeIds as communicated in the currently executed order that are traversed within the shared planned path.",
                    "items": {
                        "type": "string"
                    }
                }
            }
		},
		"intermediatePath": {
			"type": "object",
            "description": "Represents the estimated time of arrival at closer waypoints that the mobile robot is able to perceive with its sensors.",
            "required": [
                "polyline"
            ],
            "properties": {
                "polyline": {
                    "type": "array",
                    "description": "Array of end points of segments of a polyline.",
                    "items": {
                        "type": "object",
                        "description": "Endpoint of a segment within a defined polyline.",
                        "required": [
                            "x",
                            "y",
                            "eta"
                        ],
                        "properties": {
                            "x": {
                                "type": "number",
                                "description": "X-coordinate described in the project-specific coordinate system.",
                                "unit": "m"
                            },
                            "y": {
                                "type": "number",
                                "description": "Y-coordinate described in the project-specific coordinate system.",
                                "unit": "m"
                            },
                            "theta": {
                                "type": "number",
                                "description": "Absolute orientation of the mobile robot in the project-specific coordinate system.",
                                "unit": "rad",
                                "minimum": -3.14159265359,
                                "maximum": 3.14159265359
                            },
                            "eta": {
                                "type": "string",
                                "description": "Estimated time of arrival/traversal. Formatted as a timestamp (ISO 8601, UTC); YYYY-MM-DDTHH:mm:ss.fffZ (e.g., '2017-04-15T11:40:03.123Z')."
                            }
                        }
                    }
                }
            }
		},
		"mobileRobotPosition": {
			"type": "object",
            "description": "Defines the position on a map in world coordinates. Each floor has its own map.",
            "required": [
                "x",
                "y",
                "theta",
                "mapId",
                "localized"
            ],
            "properties": {
                "x": {
                    "type": "number",
                    "unit": "m"
                },
                "y": {
                    "type": "number",
                    "unit": "m"
                },
                "theta": {
                    "type": "number",
                    "unit": "rad",
                    "minimum": -3.14159265359,
                    "maximum": 3.14159265359
                },
                "mapId": {
                    "type": "string",
					"description": "Unique identification of the map."
                },
                "localized": {
                    "type": "boolean",
                    "description": "True: mobile robot is localized. x, y, and theta can be trusted. False: mobile robot is not localized. x, y, and theta cannot be trusted."
                },
                "localizationScore": {
                    "type": "number",
                    "description": "Describes the quality of the localization and therefore, can be used, e.g., by SLAM mobile robot to describe how accurate the current position information is.\n0.0: position unknown\n1.0: position known\nOptional for vehicles that cannot estimate their localization score.\nOnly for logging and visualization purposes",
                    "minimum": 0.0,
                    "maximum": 1.0
                },
                "deviationRange": {
                    "type": "number",
                    "description": "Value for position deviation range in meters. Optional for vehicles that cannot estimate their deviation, e.g., grid-based localization. Only for logging and visualization purposes.",
                    "unit": "m",
                    "minimum": 0.0
                }
            }
		},
		"load": {
			"type": "object",
			"required": [],
			"description": "Load object that describes the load if the mobile robot has information about it.",
			"title": "load",
			"properties": {
				"loadId": {
					"type": "string",
					"description": "Unique identification number of the load (e.g., barcode or RFID). Empty field, if the mobile robot can identify the load, but did not identify the load yet. Optional, if the mobile robot cannot identify the load."
				},
				"loadType": {
					"type": "string",
					"description":"Type of load."
				},
				"loadPosition": {
					"type": "string",
					"description": "Indicates, which load handling/carrying unit of the mobile robot is used, e.g., in case the mobile robot has multiple spots/positions to carry loads. Optional for vehicles with only one loadPosition.",
					"examples":[
						"front", "back", "positionC1"
					]
				},
				"boundingBoxReference": {
					"type": "object",
					"required": [
						"x",
						"y",
						"z"
					],
					"description": "Point of reference for the location of the bounding box. The point of reference is always the center of the bounding box bottom surface (at height = 0) and is described in coordinates of the mobile robot coordinate system.",
					"properties": {
						"x": {
							"type": "number"
						},
						"y": {
							"type": "number"
						},
						"z": {
							"type": "number"
						},
						"theta": {
							"type": "number",
							"description":"Orientation of the loads bounding box. Important for tugger, trains, etc."
						}
					}
				},
				"loadDimensions": {
					"type": "object",
					"required": [
						"length",
						"width"
					],
					"description": "Dimensions of the loads bounding box in meters.",
					"properties": {
						"length": {
							"type": "number",
							"description": "Absolute length (along the mobile robot’s coordinate system's x-axis) of the load's bounding box in meters.",
							"unit": "m",
							"minimum": 0.0
						},
						"width": {
							"type": "number",
							"description": "Absolute width (along the mobile robot’s coordinate system's y-axis) of the load's bounding box in meters.",
							"unit": "m",
							"minimum": 0.0
						},
						"height": {
							"type": "number",
							"description": "Absolute height of the loads bounding box in meter.\nOptional:\nset value only if known.",
							"unit": "m",
							"minimum": 0.0
						}
					}
				},
				"weight": {
					"type": "number",
					"description": "Absolute weight of the load measured in kg.",
					"unit": "kg",
					"minimum": 0.0
				}
			}
		},
		"zoneRequest": {
			"type": "object",
			"description": "Zone information sent by the mobile robot to fleet control.",
			"required": [
				"requestId",
				"requestType",
				"zoneId",
				"zoneSetId",
				"requestStatus"
			],
			"properties": {
				"requestId": {
					"type": "string",
					"description": "Unique per mobile robot identifier within all active requests."
				},
				"requestType": {
					"type": "string",
					"enum": ["ACCESS", "REPLANNING"],
					"description": "Enum specifying the type of zone the request relates to. Feasible values are ACCESS or REPLANNING."
				},
				"zoneId": {
					"type": "string",
					"description": "Locally (within the zone set) unique identifier referencing the zone the request is related to."
				},
				"zoneSetId": {
					"type": "string",
					"description": "Due to the zoneId only being unique to a zoneSet, the zoneSetId is part of the request."
				},
				"requestStatus": {
					"type": "string",
					"enum": ["REQUESTED", "GRANTED", "REVOKED", "EXPIRED"],
					"description": "When stating a request, this is set to REQUESTED. After response or update from fleet control set to GRANTED or REVOKED. If lease time expires, shall be to EXPIRED."
				},
				"trajectory": {
					"$ref": "#/definitions/trajectory"
				}
			}
		},
		"edgeRequest": {
			"type": "object",
			"description": "Edge request information sent by the mobile robot to fleet control.",
			"required": [
				"requestId",
				"requestType",
				"edgeId",
				"sequenceId",
				"requestStatus"
			],
			"properties": {
				"requestId": {
					"type": "string",
					"description": "Unique per mobile robot identifier across all active requests."
				},
				"requestType": {
					"type": "string",
					"enum": ["CORRIDOR"],
					"description": "Enum specifying the type of edge the request relates to."
				},
				"edgeId": {
					"type": "string",
					"description": "Globally unique identifier referencing the edge the request is related to."
				},
				"sequenceId": {
					"type": "integer",
					"description": "Tracking number for sequence of edge within order. Required to uniquely identify the referenced edge within the order."
				},
				"requestStatus": {
					"type": "string",
					"enum": ["REQUESTED", "GRANTED", "REVOKED", "EXPIRED"],
					"description": "When stating a request, this is set to REQUESTED. After response or update from fleet control set to GRANTED or REVOKED. If lease time expires set to EXPIRED."
				}
			}
		},
        "actionState": {
            "type": "object",
            "required": [
                "actionId",
                "actionStatus"
            ],
            "title": "actionState",
            "properties": {
                "actionId": {
                    "type": "string",
                    "description": "Unique actionId",
                    "examples": [
                        "blink_123jdaimoim234"
                    ]
                },
                "actionType": {
                    "type": "string",
                    "description": "actionType of the action. Optional: Only for informational or visualization purposes. Order knows the type."
                },
                "actionDescriptor": {
                    "type": "string",
                    "description": "A user-defined, human-readable name or descriptor."
                },
                "actionStatus": {
                    "type": "string",
                    "description": "WAITING: waiting for the trigger (passing the mode, entering the edge); INITIALIZING: Action was triggered, preparatory measures are initiated; RUNNING: The action is running; RETRIABLE: Actions that failed, but can be retried; PAUSED: paused by instantAction or external trigger; FINISHED: The action is finished; FAILED: action could not be performed.",
                    "enum": [
                        "WAITING",
                        "INITIALIZING",
                        "RUNNING",
                        "PAUSED",
                        "RETRIABLE",
                        "FINISHED",
                        "FAILED"
                    ]
                },
                "actionResult": {
                    "type": "string",
                    "description": "Description of the result, e.g., the result of a RFID-read. Errors will be transmitted in errors."
                }
            }
        },
		"powerSupply": {
			"type": "object",
            "required": [
                "stateOfCharge",
                "charging"
            ],
            "description": "Contains all battery-related information.",
            "properties": {
                "stateOfCharge": {
                    "type": "number",
                    "description": "State of Charge in %: If mobile robot only provides values for good or bad battery levels, these will be indicated as 20% (bad) and 80% (good).",
                    "minimum":0,
                    "maximum":100
                },
                "batteryVoltage": {
                    "type": "number",
                    "description": "Battery voltage"
                },
                "batteryCurrent": {
                    "type": "number",
                    "description": "Battery current in Ampere (A)"
                },
                "batteryHealth": {
                    "type": "number",
                    "description": "State of health in percent.",
                    "minimum":0,
                    "maximum":100
                },
                "charging": {
                    "type": "boolean",
                    "description": "True: charging in progress. False: mobile robot is currently not charging."
                },
                "range": {
                    "type": "number",
                    "description": "Estimated reach with current State of Charge in meter.",
                    "minimum": 0
                }
            }
		},
		"error": {
			"type": "object",
			"required": [
				"errorType",
				"errorLevel"
			],
			"title": "Error",
			"properties": {
				"errorType": {
					"type": "string",
					"description": "Error type, extensible enumeration including the following predefined values."
				},
				"errorReferences": {
					"type": "array",
					"items": {
						"type": "object",
						"title": "errorReference",
						"description": "Array of references (e.g. nodeId, edgeId, orderId, actionId, etc.) to provide more information related to the error.",
						"properties": {
							"referenceKey": {
								"type": "string",
								"description":"Specifies the type of reference used (e.g. nodeId, edgeId, orderId, actionId, etc.)."
							},
							"referenceValue": {
								"type": "string",
								"description":"The value that belongs to the reference key. For example, the id of the node where the error occurred."
							}
						},
						"required": [
							"referenceKey",
							"referenceValue"
						]
					}
				},
				"errorDescription": {
					"type": "string",
					"description": "Verbose description providing details and possible causes of the error."
				},
				"errorDescriptionTranslations": {
					"type": "array",
					"description": "Array of translations of the error description.",
					"items": {
						"$ref": "#/definitions/translation"
					}
				},
				"errorHint": {
					"type": "string",
					"description": "Hint on how to approach or solve the reported error."
				},
				"errorHintTranslations": {
					"type": "array",
					"description": "Array of translations of the error hint.",
					"items": {
						"$ref": "#/definitions/translation"
					}
				},
				"errorLevel": {
					"type": "string",
					"description": "WARNING: No immediate attention required, mobile robot is able to continue active and accept new order. URGENT: Immediate attention required, mobile robot is able to continue active and accept new order. CRITICAL: Immediate attention required, mobile robot is unable to continue active order, but can accept new order. FATAL: User intervention is required, mobile robot is unable to continue active or accept new order.",
					"enum": [
						"WARNING",
						"URGENT",
						"CRITICAL",
						"FATAL"
					]
				}
			}
		},
        "translation": {
            "type": "object",
            "title": "translation",
            "description": "Translation of a text for a given language code.",
            "required": [
                "translationKey",
                "translationValue"
            ],
            "properties": {
                "translationKey": {
                    "type": "string",
                    "description": "Specifies the language of the translation according to ISO 639-1."
                },
                "translationValue": {
                    "type": "string",
                    "description": "Translation in language of translation key."
                }
            }
        },
		"info": {
			"type": "object",
			"required": [
				"infoType",
				"infoLevel"
			],
			"properties": {
				"infoType": {
					"type": "string",
					"description": "Type/name of information."
				},
				"infoReferences": {
					"type": "array",
					"items": {
						"type": "object",
						"required": [
							"referenceKey",
							"referenceValue"
						],
						"title": "infoReference",
						"description": "Array of references.",
						"properties": {
							"referenceKey": {
								"type": "string",
								"description":"References the type of reference (e.g., headerId, orderId, actionId, etc.)."
							},
							"referenceValue": {
								"type": "string",
								"description":"References the value, which belongs to the reference key."
							}
						}
					}
				},
				"infoDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor."
				},
				"infoLevel": {
					"type": "string",
					"description": "DEBUG: used for debugging. INFO: used for visualization.",
					"enum": [
						"INFO",
						"DEBUG"
					]
				}
			}
		},
		"safetyState": {
			"type": "object",
            "required": [
                "activeEmergencyStop",
                "fieldViolation"
            ],
            "description": "Contains all safety-related information.",
            "properties": {
                "activeEmergencyStop": {
                    "type": "string",
                    "description": "EmergencyStop-Types:  MANUAL: e-stop shall be acknowledged manually at the mobile robot. REMOTE: facility e-stop shall be acknowledged remotely. NONE: no e-stop activated.",
                    "enum": [
                        "MANUAL",
                        "REMOTE",
                        "NONE"
                    ]
                },
                "fieldViolation": {
                    "type": "boolean",
                    "description": "Protective field violation. True: field is violated. False: field is not violated."
                }
            }
		}
    }
}
```

### data/source_texts/ref-634.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# VDA5050 - Version 3.0.0

An open standard for communication between mobile robot fleets and a central fleet control. Developed jointly by the German Association of the Automotive Industry (www.vda.de) and the VDMA (www.vdma.org), as well as the Institute for Material Handling and Logistics (IFL) at the Karlsruhe Institute of Technology (www.ifl.kit.edu) and many contributors from the mobile robot industry.

**Note**: We are constantly working to improve the VDA 5050. If there are any differences between the markdown document/JSON schemas on GitHub and the published document by the VDA, the PDF on the VDA website is valid. The current version of the official VDA 5050 document can be found ([here](https://www.vda.de/vda-5050)).

## How to contribute
If you work for a VDA / VDMA member, ask your contact person if you can join the working group.
Everyone is free to raise issues or suggest new improvements to the protocol.

Anyone is free to raise issues or suggest new improvements to the protocol using the Github issues. Github issues will be marked by the VDA/VDMA team as **VD(M)A in progress** if the issue is discussed in the monthly VDA 5050 meetings. If the issue has been accepted by the team, it will receive a milestone tag indicating when the change will be added to the document, according to

- V3.0.1: Minor changes such as typos and fixes,
- V3.1.0: Non-breaking, backward-compatible changes,
- V4.0.0 (Currently not planned): Breaking changes, which would mean reworking structures or variable names.

When creating pull requests, please create them against the *development* branch. The *main* branch contains the latest published version of VDA 5050 (currently version 3.0.0).

## Legal notice regarding the scope of support for VDA 5050 on GitHub
Use of this GitHub repository and all content, information, and support services offered therein is at your own risk.
With the release of a new version of VDA 5050, the core team may provide support for this version at its own discretion. There is no legal entitlement to support, maintenance, troubleshooting, further development, or timely response at any time. In particular, there is no legal obligation to process issues or to review or accept pull requests.
No support is provided for any previously published versions of VDA 5050. Any responses to issues or other feedback are provided on a voluntary basis, are non-binding, and do not constitute recognition of any legal obligation.

## Disclaimer
Use of this GitHub repository and all content, information, and support services contained therein is at your own risk. No guarantee is given for the accuracy, completeness, timeliness, suitability for a particular purpose, or availability of the content.
All information, advice, and support services are provided voluntarily, without obligation, and without legal claim. No contractual relationship, in particular a support, service, or consulting contract, is established.
Liability for damages arising from the use or non-use of the information provided, from incorrect or incomplete content, or from failure to provide support is excluded. This also applies to indirect damages, consequential damages, and lost profits. Liability for intent, gross negligence, and injury to life, limb, or health remains unaffected.
```

### runs/2026-10-11-01/research.json

```json
{
  "run_id": "2026-10-11-01",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 21,
    "area_name": "21. 상호운용 표준·적합성",
    "category": "F. 연동"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 수행 자원 칸이 'VDA 5050 3.0.0 에서 주문 배정·경로 계산…은 관제 쪽'으로 경로 계산을 모든 로봇에 일반화함(원문은 선 유도 로봇). 물류창고 외 현장 유형 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 'OPC 는 제조사가 자체 인증하거나' 문장의 근거 없음(정정 필요). 선택 필드·재전송을 확인하는 동작 시험 방법 없음. OTTO 인증 발표 각주가 원문 미열람",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 행 '발행일은 명세 머리에 없어 미확인', MassRobotics 행 '원문 미열람', OPC 행 '자체·독립 시험소 인증' 표현. 3.0.0 태그 스키마 구문 오류, OPC UA Robotics Facet, KS B ISO 22166-202·TTA 표준 미반영",
    "섹션 8. 대표 연구와 자료 — vda5050-lab 원문 미열람 표시, VDA 5050 통신 평가 논문 없음",
    "섹션 11. 열린 질문 — oq-005·oq-055·oq-091·oq-026·oq-111 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]",
    "oq-005 VDA 5050 3.0.0 의 정확한 발행일은 언제인가? 배포 PDF 표지·카탈로그·보도자료의 날짜 표시는 각각 무엇인가? (섹션 7·11 겨냥)",
    "oq-055 VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (섹션 6·8·11 겨냥)",
    "oq-091 VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? — 3.0.0 시험 입력(스키마)의 신뢰성 (섹션 7·11 겨냥)",
    "oq-026 KS B 7321-2 가 ISO 22166-202 와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (섹션 7·11 겨냥, 한국 자료 우선)",
    "oq-111 KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? (섹션 7·11 겨냥)",
    "기존 문장 점검: VDA 5050 3.0.0 은 경로 계산을 어느 로봇에 대해 관제 책임으로 두는가, OPC Foundation 은 제조사 자체 인증을 허용하는가? (섹션 5·6·7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 공식 배포 PDF(103쪽)의 표지는 판을 'VDA 5050 Version 3.0.0, March 2026'으로 표기한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF 표지 \"VDA 5050 Version 3.0.0, March 2026\", 전체 103쪽. PDF 메타데이터 생성일은 2026-04-17. 파일명의 '2025-03'은 발행일 근거로 쓰지 않음. 20번 주제 페이지(2026-10-10-area20-s7)에서 [추정]으로 남았던 표지 문구를 원문으로 확인한 것",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "21번 7절 표 VDA 5050 행의 '발행일은 명세 머리에 없어 미확인'은 PDF 표지 판 표기(2026년 3월)로 고치고, 카탈로그 표시일(2026-03-17)·보도자료 날짜(2026-04-20)와의 비교는 20번 주제 페이지의 날짜 절로 연결하며 단일 공식 채택일은 확인 못 함으로 남기는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1423",
        "ref-1412",
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "카탈로그 표시 2026-03-17(ref-1412), 보도자료 머리 'Berlin, April 20, 2026'(ref-032)은 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」에 이미 있음. 세 자료 모두 VDA 계열이라 독립 교차 확인 아님. GitHub 릴리스 설명의 날짜는 원문 확인 불가(403)라 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 §5.3 의 관제 기능 목록은 경로 계산을 일반 기능이 아니라 '선 유도(line-guided) 이동로봇의 경로 계산·안내'로 적고, §5.4 는 이동로봇을 선 유도형과 자유 주행형(freely navigating)으로 나눠 서술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF §5.3 p.11 \"Route calculation and guidance of line-guided mobile robots\"; §5.4 'line-guided or freely navigating'. 원문에 '한정'이라는 표현은 없어 직역함. 같은 직역은 2026-10-09-area41-s6 46행에 이미 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 의 3.0 발표 보도자료는 자율도가 높은 이동로봇이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 관제와 공유(path sharing)하는 구성을 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료 New features 문단: robots independently plan their own routes, \"detailed route planning takes place on the vehicle itself\", 'path sharing'. 대상은 high degree of autonomy 로봇. 명세 §6.8 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행에 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "21번 본문 5절 수행 자원 칸과 분리 7절 본문의 '주문 배정·경로 계산·…은 관제 쪽' 문장은 '선 유도 로봇의 경로 계산·안내'로 고치고, 자유 주행 로봇은 상세 경로를 스스로 계획해 공유할 수 있음을 병기해 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1423",
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정정 대상: 본문 5절 수행 자원 칸 '(출하) … 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽', 2026-09-25-area28-s7 본문 첫 문단. 같은 일반화가 categories/governance-law-and-society/index.md 70행에도 있으나 다른 영역 페이지라 후속 정리 대상",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 §7.1.1 은 선택(optional) 필드에 대해 로봇이 필드를 무시해서는 안 된다고 정하고, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF §7.1.1 p.67 로봇 쪽 'shall not ignore the field'; 같은 절 관제 쪽 \"Fleet control shall only send optional fields that the mobile robot supports\". 관제 쪽 의무는 외부 조사 메모가 빠뜨린 것을 검증에서 보탰다",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 은 연동 시험의 기대값으로 쓸 응답을 조항으로 정한다: 지원하지 않는 선택 파라미터가 든 주문은 UNSUPPORTED_PARAMETER(CRITICAL)로 거절, 같은 orderUpdateId 재전송은 내용이 같으면 무시하고 다르면 SAME_ORDER_UPDATE_ID(WARNING)를 보고하며 이전 주문을 계속, 취소된 주문의 후속 갱신은 ORDER_UPDATE_FOLLOWING_CANCEL(WARNING).",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PDF §6.1.4.2 p.20·§6.1.3.1 p.20(UNSUPPORTED_PARAMETER·CRITICAL, ORDER_UPDATE_FOLLOWING_CANCEL·WARNING), §6.1.4.5 p.21(같으면 무시, 다르면 'SAME_ORDER_UPDATE_ID' WARNING), §7.10 p.92~(p.96 optionalParameters). 재전송 규칙 자체는 2026-10-09-area41-s6 56행, command-and-task-execution-reliability.md 90행에 이미 있음 — 새로운 것은 시험 기대값과 쪽 위치",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "로봇 연동 승인에는 버전 문자열 확인에 더해 (1) 미지원 선택 필드 주문 거절, (2) 같은 번호·같은 내용 재전송 무시, (3) 같은 번호·다른 내용 재전송 경고, (4) 취소 후 갱신 경고, (5) 관제가 로봇 factsheet 가 지원한다고 밝힌 선택 필드만 보내는지를 확인하는 동작 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f6·f7 조항을 시험 행으로 옮긴 제안이며 공식 인증 항목 목록이 아님. (5)행은 §7.1.1 관제 의무에서 나옴",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "VDA5050 공식 저장소 3.0.0 태그의 order.schema·factsheet.schema·visualization.schema 세 파일은 끝 쉼표(trailing comma) 때문에 JSON 으로 파싱되지 않고, 같은 태그의 state·instantActions·connection 스키마와 main 브랜치의 세 파일은 파싱된다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검증 단계에서 태그 파일을 내려받아 재현. SHA-256 order f7e2d3b5…986d12, factsheet d2fd651d…7991ec, visualization 858eeab4…fafc92 가 조사 메모 값과 일치. JSON 구문 검사이며 JSON Schema 의미 검증이나 로봇 적합성 시험이 아님(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "세 스키마의 구문 오류 위치는 파서에 따라 다르게 진단된다: Python 3.11 json 은 315행 8열·174행 17열·55행 5열을, Python 3.13 이후는 'Illegal trailing comma' 로 314행 130열·173행 32열·54행 10열을 가리킨다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검증 단계 직접 재현(order/factsheet/visualization 순). 이슈 제보의 315·174·55행과 메모 재현의 314·173·54행 차이는 파서 진단 방식 차이로 설명됨",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "VDA5050 공식 저장소 이슈 #660 은 3.0.0 태그의 order·factsheet·visualization 스키마가 유효한 JSON 이 아니며 main 에서는 고쳐졌으나 새 릴리스는 없다고 보고한 것으로 외부 조사 메모가 전한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 인용 제목 '3.0.0 tag ships invalid JSON … (fixed on main, not released)'. 검증에서 이슈 페이지·API 가 403 이라 원문 미열람 — 메모가 적은 날짜(2026-09-13)와 제보자 계정은 미확인. 제보이며 표준기관 정오표가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "VDA 5050 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며 main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-051",
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f9·f10 재현 결과에서 나온 운영 제안. 공식 PDF·태그 스키마·검사 도구 판을 각각 고정",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "vda5050-lab README(커밋 4a1a812)는 v0.2.0 을 합성 데모 개발자 프리뷰로 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 로그·외부 시험 대상(DUT)·실물 하드웨어 실행 검증이 없다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README Status: \"Synthetic Demo Preview\", 'not a public-alpha or certification claim', no real customer trace, external DUT·hardware execution 없음. 문서의 자기 기술만 확인했고 프로그램은 실행하지 않음(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "vda5050-lab 은 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 합격 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "21번 8절의 vda5050-lab 항목과 각주 '(원문 미열람)' 표시를 f13 으로 보강하는 제안. 개인 프로젝트의 한계 선언과 공식 시험기관 인증은 별개",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "OPC Foundation 'How to Certify' 는 제조사가 인증 시험소(Certification Lab)에 가기 전에 적합성 시험 도구(CTT)로 준비하도록 권고하며, CTT 는 시험소가 쓰는 도구라고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-705"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Preparing for Testing: \"It is suggested that vendors prepare … before attending the … Certification Lab\"(권고 표현), CTT 'used by the lab'(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "OPC Foundation 'Overview & Benefits' 는 인증 제품이 OPC Foundation 이 인정한 인증 시험소에서 시험을 거쳤다고 설명하고, 인증된 SDK 를 쓴 응용도 각자 인증 시험을 받아야 한다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Certified products have been tested in an OPC Foundation accredited Certification Lab\"; SDK 기반 응용은 'require their own certification testing'. ref-705 와 같은 기관이라 독립 교차 확인 아님(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "확인한 OPC Foundation 인증 안내 두 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없으므로, 21번 분리 6절의 '제조사가 자체 인증하거나'와 분리 7절 표 OPC 행의 '자체·독립 시험소 인증'은 근거가 없는 표현이다.",
      "tag": "사실",
      "source_ids": [
        "ref-705",
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 페이지 어디에도 self-certification 표현 없음(검증 확인). 정정 대상: 2026-09-25-area28-s6「적합성 시험과 인증」첫 문단, 2026-09-25-area28-s7 표 OPC Foundation 인증 프로그램 행. 같은 표현이 ref-705 요약에도 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "OPC 적합성 체계는 '제조사의 CTT 사전 점검(권고)'과 '인정 시험소 인증'을 구분하는 문장으로 고치고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-705",
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f15~f17 정정 제안. 시험 항목은 지원 프로파일에 따라 달라짐",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "MassRobotics AMR_Interop_Standard.json(커밋 f9357a4)의 최상위 oneOf 는 identityReport 와 statusReport 두 정의를 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "JSON 최상위 oneOf: identityReport·statusReport; definitions.location.required = [x, y, angle, planarDatum]. planarDatum 만 필수인 것처럼 쓰지 않음. statusReport 필수 필드는 2026-10-10-area20-s7 52행에 이미 있음. 별도 표준 PDF 판·발행일은 미확인(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "MassRobotics 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f19 스키마에 명령·작업 배정 메시지가 없음. 21번 분리 7절 표 MassRobotics 행의 '(원문 미열람)'은 스키마 원문 확인으로 해소",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "OPC 40010-1(OPC UA for Robotics Part 1) 1.02판 §11 은 서버 기능 묶음(Facet)을 기본·운전·자산관리 확장·상태감시 확장 등으로 나누고 각 기능 단위를 필수(Mandatory)·선택(Optional)으로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-034"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§11 Facet 표 123~127 'Mandatory / Optional'. 1.02판·2025-09-08·§1 범위('higher-level control and evaluation systems')는 2026-09-29-area04-s7 43행(ref-874)에 이미 있음 — 새로운 것은 Facet 구조",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-034"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f21 에서 나온 제안. 발행일이 최근 1년 창보다 앞서 2026년 신규 표준으로 세지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "외부 조사 메모는 2026-10-11 ISO 공식 목록이 ISO 21423 을 단계 60.00(발행 준비 중)으로 표시하고 범위에서 안전 관련 요구와 공도 운행 이동기계를 제외한다고 전하지만, 이번 검증에서는 iso.org 가 403 이라 원문을 대조하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 인용 'International Standard under publication', 'Safety-related requirements', 'public roads'. 같은 내용이 categories/space-and-map-model/index.md 106행, categories/safety/index.md 93행, 2026-10-10-area20-s10 44행에 있음 — 21번엔 ref-159 와 확인일만",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "KSSN 목록에서 KS B 7321-2 는 2024-01-05 제정으로 표시되고 국제표준 부합화 칸은 비어 있으며, 고시사유는 '수요조사 반영에 의한 제정'(제2024-1003호), 47쪽이다.",
      "tag": "사실",
      "source_ids": [
        "ref-138"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세: 제정 2024-01-05, 부합화 칸 공란, 고시사유 '수요조사 반영에 의한 제정', 47쪽. 표준 본문은 유료라 미열람. 공란을 비부합·폐지의 증거로 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "KS B ISO 22166-202(로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델)는 2026-09-11 제정된 별도 KS 로, ISO 22166-202:2025 와 IDT(일치) 부합화이며 국가기술표준원 고시 제2026-0279호, '국제표준 부합화에 의한 제정', 70쪽이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1426"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세: 2026-09-11, 'ISO 22166-202:2025(IDT)', 고시 제2026-0279호, 고시사유 '국제표준 부합화에 의한 제정', 70쪽. ISO 원표준 발행은 2025(월은 ISO 원문 확인 불가). 표준 본문 미열람",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "oq-026 에는 KS B 7321-2 와 별도로 ISO 22166-202 와 IDT 인 KS B ISO 22166-202(2026-09-11)가 있다는 사실을 더하고, 두 KS 의 대체 관계와 국내 적용 사례는 미확인으로 남기는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-138",
        "ref-1426"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f24·f25 기반 부분 답변. KS B 7321-2 의 부합화 칸 공란만으로 부합 여부를 판정하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "외부 조사 메모는 KOROS 1148-8:2025 게시물이 표준 제정일을 2025-05-28 로, 게시일을 2025-06-04 로 구분하고 이 단체표준을 바탕으로 TTA 표준이 만들어졌다고 안내한다고 전하지만, 검증에서 KOROS 사이트가 봇 접근을 막아 원문을 대조하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-710"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 인용 '표준 제정일 2025.05.28.', 게시 정보 2025-06-04. 첨부 본문은 성명·소속·이메일 입력과 동의를 요구해 미확보. 제정일과 'TTA 표준의 기반' 관계는 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "TTA TC4 공식 표준 목록에는 TTAK.KO-10.1295-Part8 '서비스 로봇 정보 모듈 — 제8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차'가 제·개정일 2026-06-26 으로 실려 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TC4 목록 해당 행 'TTAK.KO-10.1295-Part8', '2026-06-26'(목록 1597행 부근). 상세 페이지는 열람 실패, 표준 본문 미열람(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "KOROS 1148-8·TTAK.KO-10.1295-Part8 은 국내 후보 표준으로 번호와 날짜만 보강하고, 본문의 시험 항목을 확인하기 전에는 플릿 메시지 적합성 시험 절차로 채택하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-710",
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "oq-111 부분 근거. 두 표준의 시험 항목 동등성과 VDA 5050 적합성 검사 대체 가능성은 확인 못 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f30",
      "claim": "벤더 주장: OTTO by Rockwell Automation 은 2026-04-09 발표에서 OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝혔으나, 시험한 프로토콜 판·시험 항목·시험 기관은 원문에 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-608"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 첫 문단 'certified with leading VDA 5050-compliant intralogistics software providers', 업체 열거는 'including Idealworks, NAiSE and SYNAOS'. 인증 발표 자체는 2026-09-25-area28-s6 에 이미 있음 — 새로운 것은 날짜·기종과 각주 '(원문 미열람)' 해소",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f31",
      "claim": "VDMA 의 Mesh-Up 2025 안내는 automatica 2025(2025-06-24~27) 전시에서 총 9개 기업이 참여하고 MHP 가 관제를 맡은 생산 공급용 이동로봇 혼합 플릿 시연 구성을 설명한다(전시장 시연이며 실제 공장 배치가 아님).",
      "tag": "사실",
      "source_ids": [
        "ref-1428"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "행사 안내 본문 'a total of nine companies', Software 절 MHP 관제. 기업 수를 로봇 대수로 바꾸지 않음. 최근 1년 창 밖의 보완 사례(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f32",
      "claim": "같은 Mesh-Up 2025 안내는 관제 소프트웨어 공급자를 바꿔 고를 수 있는 유연성을 automatica 현장에서 실시간으로 시연하지는 않는다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1428"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Software 절 'not demonstrated live at automatica'(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f33",
      "claim": "Mesh-Up 같은 전시 시연은 제조 현장 유형의 혼합 플릿 구성 사례로만 쓰고, 실제 배치나 현장 무중단 관제 교체가 검증된 근거로 세지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1428"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f31·f32 기반. 21번 5절에 물류창고 외 현장 유형(제조 공장, 전시 시연) 보완 사례로 제안",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "Wagner 외(IEEE WFCS 2026)는 VDA 5050 에 원격조작(teleoperation) 확장과 VDA 5050 트래픽 생성기를 제안하고 개방형 산업 네트워크에서 미들웨어를 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저자 공개본 초록·§III: 'proposing' 원격조작 확장, 'traffic generator'. 제22회 WFCS(오펜부르크), pp.1–8. 논문 제안 확장이며 표준 채택 기능 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "이 논문의 평가 시나리오는 단일 모의 이동로봇의 60초 주문 실행이고, 원격조작 시나리오는 그중 20~40초 구간에 원격조작을 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§IV p.4 'a single mobile robot', '60 s', '20 s to 40 s'; 표 III·IV p.6. 여러 실물 제조사 로봇의 적합성 시험이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "이 논문은 가상 무선(virtual-radio) Open RAN 시험과 실제 무선 링크(real-world) 검증을 구분해 보고하고, 대규모 다중 로봇 시나리오 검증은 향후 과제로 남긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "그림 7 p.6, 그림 10 p.7 'virtual-radio' / 'real-world', §V 'larger-scale multi-robot scenarios'",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "21번에서는 Wagner 외 연구를 VDA 5050 통신 부하·지연 평가로 소개하되 적합성 시험과 구별하고, 상세 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 연결로만 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f34~f36 기반 8절·10절 제안",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "VDA 5050 연동 승인의 근거는 제3자 도구의 자체 진단, 벤더 간 인증 발표, 전시 시연, 인정 시험소 인증을 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-408",
        "ref-608",
        "ref-1428",
        "ref-705",
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f13·f30·f32·f15~f17 종합. oq-055 부분 근거: VDA·VDMA 공인 인증 제도의 존재·부재는 확정 못 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1423",
      "org": "VDA / VDMA",
      "title": "VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control, Version 3.0.0 (PDF)",
      "published": "2026-03",
      "url": "https://www.vda.de/dam/jcr%3A09f03b91-13e2-4db3-bf30-4f221710071b/VDA5050-V3.0.0-2025-03.pdf",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 가 배포하는 VDA 5050 3.0.0 공식 PDF(103쪽). 표지 판 표기 'March 2026'과 §5.3·§6.1·§7.1.1·§7.10 등 관제–로봇 기능 분담·오류 응답 조항을 쪽 번호로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1412",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "VDA 5050",
      "published": "2026-03-17",
      "url": "https://www.vda.de/en/news/publications/publication/vda-5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목. 표시 날짜 2026-03-17 을 다시 확인했고, 내려받는 PDF 표지의 판 표기(2026년 3월)는 이번에 ref-1423 으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-032",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "Version 3.0 of VDA 5050 released",
      "published": "2026-04",
      "url": "https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0 발행 보도자료. 본문 머리 'Berlin, April 20, 2026'과 자율도 높은 로봇의 경로 자체 계획·경로 공유 설명을 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 공식 JSON 스키마 묶음. 이번에는 3.0.0 태그의 order·factsheet·visualization 스키마를 내려받아 끝 쉼표 구문 오류와 해시를 재현했고 main 의 같은 파일은 파싱됨을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/json_schemas/order.schema",
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "VDA5050 GitHub 이슈 제보자(미확인)",
      "title": "3.0.0 tag ships invalid JSON in order/factsheet/visualization schemas (fixed on main, not released) — VDA5050 issue #660",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/issues/660",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 3.0.0 태그의 세 스키마가 유효한 JSON 이 아니라는 공식 저장소 이슈 제보로 외부 조사 메모가 전한다. 검증에서 403 으로 날짜·제보자를 확인하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "MQTT 기록에서 VDA 5050 주문·재연결·취소 실패를 진단하는 개인 프로젝트 README. 커밋 4a1a812 고정본에서 v0.2.0 이 합성 데모 프리뷰이며 인증 주장이 아니라는 한계 선언을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ekusiadadus/vda5050-lab/4a1a812f9418084f658b65856cf3e1a5bbc2cf51/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-705",
      "org": "OPC Foundation",
      "title": "How to Certify - OPC Foundation",
      "published": null,
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC 제품 인증 절차 안내. 제조사가 인증 시험소에 가기 전에 CTT 로 준비하도록 권고하고 CTT 는 시험소가 쓰는 도구라고 설명한다. 제조사 자체 인증 경로는 없다(기존 요약의 '자체 인증' 표현은 정정 필요).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1427",
      "org": "OPC Foundation",
      "title": "Overview & Benefits — OPC Foundation Certification",
      "published": null,
      "url": "https://opcfoundation.org/certification/overview-benefits/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC Foundation 인증 프로그램 개요. 인증 제품은 재단이 인정한 인증 시험소에서 시험을 거치며, 인증 SDK 를 쓴 응용도 각자 인증 시험이 필요하다고 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 커밋 f9357a4 고정본에서 최상위 oneOf(identityReport·statusReport)와 location 필수 필드 [x, y, angle, planarDatum]을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/f9357a423ecabc3f7112e6d10025a5231943ec50/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-034",
      "org": "OPC Foundation / VDMA",
      "title": "OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration",
      "published": "2025-09-08",
      "url": "https://reference.opcfoundation.org/specs/OPC-40010-1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC UA for Robotics 1부 공식 온라인 참조(1.02판, 2025-09-08). 이번에 §1 범위와 §11 서버 Facet 표(표 123~127)의 필수·선택 구분을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://reference.opcfoundation.org/specs/OPC-40010-1/full",
      "source_unopened": false
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 서로 다른 공급사의 산업용 이동로봇·플릿 관리자 사이 통신·상호운용을 다루는 ISO 규격 페이지. 2026-10-11 검증에서도 403 으로 단계·범위를 대조하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": "2024-01-05",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B 7321-2 의 KSSN 상세 목록. 2024-01-05 제정, 국제표준 부합화 칸 공란, 고시사유 '수요조사 반영에 의한 제정'을 확인했다(본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1426",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델",
      "published": "2026-09-11",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158171",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 22166-202:2025 와 IDT 인 KS 의 KSSN 상세 목록. 2026-09-11 제정, 국가기술표준원 고시 제2026-0279호, 국제표준 부합화에 의한 제정을 확인했다(본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-710",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "title": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": "2025-06-04",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차 단체표준 제·개정 게시물(게시일 2025-06-04). 2026-10-11 검증에서도 봇 차단으로 제정일을 대조하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1425",
      "org": "한국정보통신기술협회(TTA)",
      "title": "TTA 표준화위원회 TC4 표준 목록 — TTAK.KO-10.1295-Part8 서비스 로봇 정보 모듈 — 제8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": null,
      "url": "https://committee.tta.or.kr/standard/standard.jsp?commit_code=TC4",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "TTA TC4 공식 표준 목록. TTAK.KO-10.1295-Part8 의 제·개정일 2026-06-26 을 목록에서 확인했다(상세 페이지·본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04-09",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "OTTO AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 등과 VDA 5050 인증을 마쳤다는 2026-04-09 보도자료(벤더 주장). 시험 판·항목·기관은 밝히지 않는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1428",
      "org": "VDMA",
      "title": "Mobile Robots in Production: Mesh-Up 2025",
      "published": null,
      "url": "https://www.vdma.eu/en/mesh-up",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDMA 의 automatica 2025(2025-06-24~27) 이동로봇 혼합 플릿 공동 시연 안내. 9개 기업 참여, MHP 관제 구성과 관제 공급자 교체 유연성은 현장 실시간 시연이 아니라는 점을 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1429",
      "org": "Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P.",
      "title": "Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks",
      "published": "2026-04-21",
      "url": "https://doi.org/10.1109/WFCS67029.2026.11511549",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "제22회 IEEE WFCS(2026, 오펜부르크) 논문. VDA 5050 원격조작 확장과 트래픽 생성기를 제안하고 단일 모의 로봇·가상 무선 Open RAN·실제 무선 링크 조건에서 통신을 평가했다(저자 공개본 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://comnets.etit.tu-dortmund.de/storages/cni-etit/r/Research/Publications/2026/Wagner_2026_WFCS/Wagner_WFCS_AuthorsVersion.pdf",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 본문 5절 수행 자원 칸의 '경로 계산'을 '선 유도 로봇의 경로 계산·안내'로 정정(f3·f5, §5.4 선 유도/자유 주행 구분 함께), 자유 주행 로봇의 경로 자체 계획·공유 병기(f4; 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행 연결). 물류창고 외 현장 유형 보완: 제조 공장 전시 시연 Mesh-Up 2025(f31·f32, 전시 시연이며 실제 배치 아님, f33) / 섹션 6(분리 2026-09-25-area28-s6) — 「적합성 시험과 인증」첫 문단 '제조사가 자체 인증하거나'를 정정(f15·f16·f17·f18: CTT 사전 준비는 권고, 인증은 인정 시험소, SDK 응용도 개별 시험). OTTO 문단에 날짜 2026-04-09·기종 4개·'등' 표기 보강, 각주 원문 미열람 해소(f30, 벤더 주장 유지). 선택 필드·재전송·취소 후 갱신 동작 시험표 추가(f6·f7·f8, §7.1.1 관제 의무 행 포함; 재전송 규칙 자체는 2026-10-09-area41-s6 56행·command-and-task-execution-reliability.md 90행 연결). 근거 수준 구분(f38) / 섹션 7(분리 2026-09-25-area28-s7) — 표 VDA 5050 행 '발행일은 명세 머리에 없어 미확인'을 PDF 표지 판 표기 'March 2026'(f1)로 고치고 날짜 비교는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」로 연결(f2, 그 페이지의 표지 [추정]은 f1 로 확인됨). 본문 첫 문단 '주문 배정·경로 계산…' 정정(f3·f5). 표 OPC 행 '자체·독립 시험소 인증'을 '인정 시험소 인증(CTT 는 사전 점검 도구)'으로 정정(f17). 표 MassRobotics 행 '(원문 미열람)' 해소와 location 필수 필드(f19·f20; statusReport 필수 필드는 2026-10-10-area20-s7 52행 연결). 3.0.0 태그 스키마 구문 오류 주의사항 추가(f9·f10 사실, f11 이슈 제보는 추정, f12). OPC UA Robotics Facet 구조(f21·f22; 판·발행일·범위는 2026-09-29-area04-s7 43행 연결). ISO 21423 은 ref-159 와 확인일만(f23 추정; 같은 내용은 categories/space-and-map-model/index.md 106행 등). KS B 7321-2 제정일·부합화 칸 공란(f24), KS B ISO 22166-202 IDT 신규(f25·f26), KOROS 1148-8 제정일(f27 추정)과 TTAK.KO-10.1295-Part8(f28·f29) / 섹션 8 — vda5050-lab 항목에 v0.2.0 합성 데모 프리뷰·인증 주장 아님 반영, 각주 '(원문 미열람)' 해소(f13·f14). Wagner 외 WFCS 2026 통신 평가 논문 추가(f34~f36, 적합성 시험과 구별 f37) / 섹션 10 — 42. 분산 시스템·통신·컴퓨팅 구조 연결 추가(f37) / 섹션 11 — oq-005(f1·f2), oq-055(f13~f18·f30·f38), oq-091(f9~f12), oq-026(f24~f26), oq-111(f27~f29) 부분 근거. 해결 제안 없음. 새 질문 3건. 기존 내용 확인(새 finding 없음): VDA 5050 날짜 비교(2026-10-10-area20-s7), vda-5050-lib.js v1.7.0 의 3.0 지원(2026-10-10-area20-s7 56행, ref-742) — 21번에는 요약과 연결만. 후속 정리 필요(이번 대상 아님): categories/governance-law-and-society/index.md 70행의 '경로 계산' 일반화, ref-705 참고문헌 요약의 '자체 인증' 표현."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "VDA 5050 3.0.0 태그 스키마 수정본과 공식 PDF·태그가 서로 다를 때, 연동 시험에 쓸 수정 단위·승인 책임자·회귀 시험을 어떻게 정하는가? | 관련 영역: 21. 상호운용 표준·적합성, 57. 자산·소프트웨어 수명주기 관리 | 근거: f9 | 종류: 일반",
    "TTAK.KO-10.1295-Part8 과 KOROS 1148-8:2025 의 시험 항목·판정 기준은 얼마나 같은가? (관련 기존 질문: oq-111) | 관련 영역: 21. 상호운용 표준·적합성, 54. 시험·형식 검증·벤치마크 | 근거: f28 | 종류: 일반",
    "VDA 5050 2.x·3.x 혼합 플릿을 실제 현장에서 전환할 때 관제 교체와 로봇 교체를 각각 검증한 공개 기록이 있는가? (관련 기존 질문: oq-091) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f32 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-01/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f11: 이슈 #660 원문(GitHub 403) 미확인 — 날짜 2026-09-13·제보자 계정 미확인이라 추정",
      "GitHub 릴리스 3.0.0 설명의 발행일(2026-03-19)과 published_at: 403 으로 확인 불가 — 출처·finding 에 넣지 않음",
      "f23: ISO 21423 단계 60.00·제외 범위는 iso.org 403 으로 대조 못 함(추정)",
      "f27: KOROS 1148-8 제정일 2025-05-28 과 'KOROS 표준을 바탕으로 TTA 표준' 안내는 봇 차단으로 대조 못 함(추정)",
      "ISO 22166-202 원표준의 발행 월(메모 2025-03): ISO 원문 확인 불가 — 연도 2025 만 KS B ISO 22166-202 목록(f25)의 'ISO 22166-202:2025(IDT)'로 확인",
      "f28·f29: TTA 상세 페이지와 KOROS·TTA·KS 표준 본문(유료·동의 절차) 미열람 — 시험 항목·대체 관계 미확인",
      "f30: OTTO 인증의 시험 판·항목·기관, f31·f32: Mesh-Up 2025 사후 성과 자료는 이번 변환에서 따로 확인하지 않음",
      "VDA·VDMA 공인 적합성 인증 제도의 존재·부재(oq-055)는 확정 못 함"
    ],
    "scope_violations": [
      "f31~f33: Mesh-Up 2025 는 제조 생산 공급 전시 시연으로, 실제 공장 배치가 아니며 site_type '제조 공장'은 시연이 겨냥한 현장 유형을 뜻함",
      "f34~f37: 무선망·Open RAN 통신 평가는 42. 분산 시스템·통신·컴퓨팅 구조 쪽 내용이므로 21번에는 적합성 시험과 구별되는 통신 평가 연구로만 씀",
      "f21·f22: OPC UA Robotics 정보모델은 4. 이기종 로봇 등록에서 이미 다루므로 21번에는 Facet·인증 범위 요구만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 7
    },
    "limits": "외부 조사 변환이라 검색 횟수 집계 없음(queries 0 으로 기록). 신규 출처 7건/15(ref-1423~ref-1429, 예약 구간 ref-1423~ref-1452 안), 재사용 11건(ref-1412·ref-032·ref-051·ref-408·ref-705·ref-230·ref-034·ref-138·ref-608 는 검증 단계 원문 대조, ref-159·ref-710 은 미열람). 미열람 신규 출처는 ref-1424(이슈 #660) 1건. 메모 출처와의 대응: n1→ref-1423(공식 PDF; 태그 스키마는 ref-051), n2→ref-1412, n4→ref-032, n6→ref-1424, n7→ref-408, n8→ref-705, n9→ref-230, n10→ref-034, n11→ref-159, n12→ref-138, n14→ref-710, n15→ref-1425(URL 을 ?commit_code=TC4 로 교체), n16→ref-1426, n17→ref-608, n18→ref-1428, n19→ref-1429, n20→ref-1427. 넣지 않은 출처: n3(GitHub 릴리스, 403 확인 불가이고 날짜 비교는 20번 페이지에 있음), n5(ref-742, vda-5050-lib.js 3.0 지원은 2026-10-10-area20-s7 에 이미 있어 새 finding 없음), n13(ref-248, 발행 연도는 f25 로 충분). 검증에서 나온 수정: B02 '한정' 표현을 §5.3 직역으로, B04 시험표에 §7.1.1 관제 의무 추가, B05 파서별 진단 행 차이를 [사실]로 상향하고 이슈 날짜·제보자는 추정으로 강등, B07 자체 인증 근거 없음 정정, B08 location 필수 4필드, B09 Facet 만 새로, B11 ISO 발행을 2025 로, B12 KOROS 제정일·TTA 기반 관계를 추정으로 강등, B13 '등' 표기, B14 '사후 자료 미확보' 서술 제외. 중복 제거: B01 날짜 비교·B03·B04 재전송 규칙·B08 statusReport·B09 판·범위·B10 은 다른 영역 페이지에 이미 있어 새 finding 으로 늘리지 않고 rationale 에 연결 위치를 적음. 열린 질문: 해결 제안 없음(모두 부분 답변). oq-005 근거 f1·f2, oq-055 근거 f13~f18·f30·f38, oq-091 근거 f9~f12, oq-026 근거 f24~f26, oq-111 근거 f27~f29. 메모의 새 질문 1(발행일 차이 설명)·2(시험기관 인증의 판·기능)·4(KS 대체 관계)는 기존 열린 질문과 겹쳐 새로 만들지 않음. 교차 확인 0건(VDA·VDMA 계열, OPC 두 페이지는 같은 기관). 정정 요청 없음. 용어 후보 없음."
  }
}
```


## 반려 사유

- 판정(verdict): 반려
- 재조사 사유(retry_reason): (a) 재조사 사유: ① 신규 참고문헌 id 가 이미 게시된 출처와 충돌한다. 직전 실행 2026-10-10-06 이 같은 예약 구간(ref-1423~ref-1452)을 써서 ref-1424 EasyTrafficLight.hpp, ref-1425 GoToZone PR #516, ref-1426 Interop SIG 구역 기능 공지, ref-1427 InOrbit Automate 2026, ref-1428 카카오모빌리티 보도자료를 등록했고, ref-1429 는 기존 출처 Franke 외(2023)다. 이번 브리프는 같은 id 를 다른 문서(PDF·이슈 #660·TTA 목록·KSSN·OPC Overview·Mesh-Up·Wagner 외)에 붙였고 URL 이 달라 퍼블리셔 병합으로 풀리지 않는다. 스토리텔러는 브리프 id 를 바꿀 수 없으므로 리서치 단계에서 고쳐야 한다. 실행 컨텍스트의 next_ref_id(없으면 pipeline/agent_runner.py 담당에게 기존 최대 id 이후의 예약 구간을 요청)로 신규 출처 id 를 다시 매긴다. ② 원문을 열었다고 적은 출처 가운데 검증에서 재현되지 않은 것이 있다. 근거(fetch_url 또는 data/source_texts 원문)를 대거나 fetched: false 와 태그 강등으로 고친다. ref-1423 PDF 표지(f1), ref-138·ref-1426 KSSN 세부 칸(f24·f25), ref-1425 TTA 목록(f28, HTTP 400), Wagner 외 저자 공개본 본문 수치(f35·f36)가 해당한다. ③ ref-1424(이슈 #660)는 실재를 확인하지 못했으므로 출처에서 빼고, f11·f23·f27 같은 '외부 메모가 전한다'식 전언 finding 은 넣지 않는다. f29 의 source_unopened 표시는 근거 출처 상태와 맞춘다. ④ 트랙 반영 제안 2026-10-09-26(IDS 1.0 을 7절 BIM 데이터 교환 요구·적합성 검사 수단으로)을 다루지 않았다. (b) 보강할 질문: VDA 5050 3.0.0 공식 PDF 표지의 판 표기는 무엇인가? PDF 텍스트를 data/source_texts 로 넣거나 쪽 이미지를 확인한 경로를 남긴다. KS B 7321-2 와 KS B ISO 22166-202 의 제정일·부합화 표시·고시번호를 KSSN 이나 국가기술표준원 고시로 확인할 수 있는가? TTAK.KO-10.1295-Part8 은 TTA 정보통신표준(standard.tta.or.kr)에 실재하며 제정일은 언제인가? Wagner 외(WFCS 2026)의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 virtual-radio / real-world 구분은 본문 어디에 있는가? IDS 1.0(buildingSMART)의 적용 대상·요구 구조·패싯은 발행 기관 자료로 무엇이며, 21. 상호운용 표준·적합성의 적합성 검사 수단으로 볼 수 있는가? 우선 출처는 VDA·KIT IFL 공식 PDF, KSSN·국가기술표준원 고시, TTA 표준 검색, IEEE Xplore 또는 저자 공개본, buildingSMART IDS 공식 문서다. (c) 살려도 되는 finding: f2(f1 처분에 맞춰 문구 수정), f3·f4·f5·f6·f7·f8·f9(출처 서지 보완)·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f30·f31·f32·f33·f34·f37·f38. 이 finding 들은 이번 검증에서 원문과 대조됐다.
- 보강할 질문·수정 목록(required_fixes):
    - 재조사 브리프에서 지킬 사항 — f2·f5·f8·f12·f14·f18·f20·f22·f33·f37·f38: [의견]마다 누구의 의견인지(구축자 의견 등) 밝힌다 — 공통 규칙 2절·검증 항목 5.
    - f9: 각주 ref-051 의 서지('json_schemas/state.schema', main URL)는 확인 대상(3.0.0 태그의 order·factsheet·visualization.schema)과 다르다. 본문에 확인한 파일 경로·태그·확인일을 밝히거나, 태그 파일을 가리키는 출처 항목을 따로 둔다.
    - f13: README 문구는 'Developer Preview'(합성 데모 포함, 인증 주장 아님)로 재서술하고 'Synthetic Demo Preview'를 인용하지 않는다 — 원문 문구가 아니다.
    - f21: Facet 표 번호를 124~127 로 적는다(검증에서 확인한 Server Facet 표 번호).
    - f30: ref-608 발행일을 참고문헌 목록의 '2026-04'에서 '2026-04-09'로 고친다 — 원문 확인.
    - f31~f33: Mesh-Up 사례를 5절 '제조 공장'에 둘 때는 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히고, site_matrix_updates 를 도입 사례로 세지 않는다.
    - 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2, IDS 1.0 → 7절)은 이번 브리프에 근거 finding 이 없다. 7절에 반영하지 않고 다음 21. 상호운용 표준·적합성 실행으로 넘기거나, 재조사에서 근거 finding 을 낸다.
    - open_questions_new 둘째(TTAK.KO-10.1295-Part8 대 KOROS 1148-8)는 근거 f28 의 출처 실재를 확인하지 못했으므로 등록하지 않는다. 셋째(2.x·3.x 혼합 플릿 전환 기록)의 근거 f32 는 관제 공급자 교체 시연이 없었다는 내용이라 판 전환과 직접 관계가 약하다. 근거를 f9·f12 또는 oq-091 로 고친다.
- 문제 삼은 주장(claim_checks):
    - f1: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. ref-1423 PDF(3.4MB, A4)는 내려받혔지만 검증에서 텍스트를 추출하지 못해 표지 문구 'Version 3.0.0, March 2026'을 대조하지 못했다. 같은 판의 3.0.0 태그 마크다운 표지에는 날짜 없이 'Version 3.0.0'만 있다. 리서치 출처 항목도 fetched: true 인데 fetch_url 이 null 이다. 20번 주제 페이지가 같은 문구를 [추정]으로 둔 상태도 그대로다.
    - f10: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. 끝 쉼표가 있다는 것은 확인했으나, 파서별 행·열 번호(315/174/55, 314/173/54)는 이번 검증에서 재현하지 못했다. 재현 환경이 리서치 측 실행이라 출처로 확인할 수 없다. 본문에 행·열 번호를 싣지 않기를 권한다.
    - f11: 출처 실재 False · 뒷받침 False · 교차 False · 처분 삭제 — 이슈 #660(ref-1424)은 검증에서도 403 이 나서 실재·제목·날짜·제보자를 확인하지 못했다. 근거는 외부 메모의 전언뿐이다. 존재를 확인하지 않은 출처이므로 본문과 참고문헌에서 뺀다. f9 는 이것 없이도 성립한다.
    - f23: 출처 실재 True · 뒷받침 False · 교차 False · 처분 삭제 — ref-159 는 기존 참고문헌이지만 이번에도 원문을 열지 못했다. 주장 내용(단계 60.00·제외 범위)은 외부 메모의 전언일 뿐 출처가 아니다. 21번 본문에 단계·범위를 새로 쓰지 않는다. 같은 내용은 다른 페이지에 이미 [추정]으로 있으므로 연결만 한다.
    - f24: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. KSSN 상세 페이지를 재열람했으나 표준 번호와 제목만 보였다. 제정일(2024-01-05), 부합화 칸 공란, 고시사유, 쪽수는 대조하지 못했다. 리서치 출처도 fetch_url 이 null 이다.
    - f25: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. KSSN 상세 페이지를 재열람했으나 번호와 제목만 보였다. 제정일(2026-09-11), IDT, 고시 제2026-0279호, 쪽수는 대조하지 못했다. 웹 검색에서도 KS 제정 기록은 나오지 않았다. ISO 22166-202:2025 발행(2025-03)은 검색 결과로 확인된다.
    - f26: 출처 실재 True · 뒷받침 False · 교차 False · 처분 열린 질문 이동 — 근거인 f24·f25 가 미대조(추정)라서, 'KS B ISO 22166-202 가 있다는 사실을 더한다'를 본문 사실로 반영하지 않는다. 기존 oq-026 은 열림을 유지하고, 확인할 거리로만 남긴다.
    - f27: 출처 실재 True · 뒷받침 False · 교차 False · 처분 삭제 — ref-710 은 기존 참고문헌이지만 이번에도 봇 차단으로 원문을 열지 못했다. 제정일(2025-05-28)과 'TTA 표준의 기반' 관계는 외부 메모의 전언이다. 본문에 새로 쓰지 않는다.
    - f28: 출처 실재 False · 뒷받침 False · 교차 False · 처분 열린 질문 이동 — 검증에서 ref-1425 URL(committee.tta.or.kr …?commit_code=TC4)이 HTTP 400 을 냈다. 웹 검색에서도 TTAK.KO-10.1295-Part8 이 나오지 않아 목록 행과 날짜(2026-06-26)를 확인하지 못했다. 리서치 출처도 fetch_url 이 null 이다. 본문 사실로 쓰지 않는다.
    - f29: 출처 실재 False · 뒷받침 False · 교차 False · 처분 열린 질문 이동 — 근거 출처 둘이 모두 미확인이다(ref-710 원문 미열람, ref-1425 실재 미확인). 그런데 브리프는 source_unopened: false 로 적었다. oq-111 은 열림을 유지한다.
    - f35: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. 저자 공개본 PDF 를 내려받았지만 검증에서 텍스트를 추출하지 못했다. 단일 로봇·60초·20~40초 원격 조작 구간은 대조하지 못했고, 초록에는 이 수치가 없다.
    - f36: 출처 실재 True · 뒷받침 False · 교차 False · 처분 강등 — 사실 → 추정. PDF 텍스트 추출에 실패해 virtual-radio / real-world 구분과 향후 과제 문구를 대조하지 못했다. 초록에는 Open RAN 무선 링크를 쓴 지연·오버헤드 평가만 있다.
- 중복·모순: {"ok": false, "overlaps": ["참고문헌 id 충돌: 직전 실행 2026-10-10-06 브리프(게시됨, 20. 로봇·제조사 관제 연동 버전 3)가 같은 예약 구간 ref-1423~ref-1452 를 썼다. 그때 신규 출처는 ref-1424 EasyTrafficLight.hpp, ref-1425 GoToZone PR #516, ref-1426 Interop SIG 구역 기능 공지, ref-1427 InOrbit Automate 2026, ref-1428 카카오모빌리티 보도자료였고, ref-1429 는 기존 출처 Franke 외(2023)였다. 이번 브리프는 같은 id 를 다른 문서에 붙였다(ref-1424 이슈 #660, ref-1425 TTA 목록, ref-1426 KSSN KS B ISO 22166-202, ref-1427 OPC Overview, ref-1428 VDMA Mesh-Up, ref-1429 Wagner 외). URL 이 달라 퍼블리셔의 같은 URL 병합으로도 해소되지 않는다.", "ref-1423 도 직전 실행에서 VDA 카탈로그(https://www.vda.de/en/news/publications/publication/vda-5050)에 쓰인 id 다. 이번 브리프는 카탈로그를 ref-1412 로, ref-1423 을 PDF 로 바꿔 붙였다.", "f3(선 유도 경로 계산 직역)은 2026-10-09-area41-s6 과 겹친다. f7 재전송 규칙은 2026-10-09-area41-s6·29. 명령·작업 실행의 신뢰성 페이지와, f4 경로 공유는 2026-10-10-area27-s7 과, f19 statusReport 는 2026-10-10-area20-s7 과, f21 판·범위는 2026-09-29-area04-s7 과, f23 ISO 21423 은 공간·지도 모델·안전 대분류 페이지와 겹친다. 모두 새로 쓰지 않고 연결해야 한다."]}
- 용어 일관성: {"ok": false, "conflicts": ["f34·f37 의 '원격조작'은 용어집 '원격 조작 (Teleoperation)'과 표기가 다르다. 용어집 표기로 맞춘다.", "f15 의 'CTT' 약어는 출처 페이지에 없다. 첫 등장에서 '적합성 시험 도구(compliance test tools)'로 풀어 쓴다. 용어집 '적합성 시험 (Conformance Test)'과 같은 개념으로 등록하지 않는다."]}
- 검증 노트: 판정: 반려. 확인 26건, 미확인 12건, 교차 확인 0건. 강등: f1·f10·f24·f25·f35·f36 사실 → 추정. 삭제: f11·f23·f27. 열린 질문 이동: f26·f28·f29. 원문 미열람 출처: ref-1424(검증에서도 403, 실재 미확인), ref-159, ref-710. 출처 문제: ref-1425(TTA 목록)는 검증 재열람이 HTTP 400 이었고, ref-1423(VDA 5050 3.0.0 PDF)과 Wagner 외 저자 공개본은 텍스트 추출에 실패해 표지·본문 수치를 대조하지 못했다. KSSN 두 상세 페이지는 번호·제목만 보였다. 조항 내용(§5.3·§5.4·§6.1.3.1·§6.1.4.2·§6.1.4.5·§7.1.1)은 공식 저장소 3.0.0 태그 마크다운으로 확인했다. 3.0.0 태그 스키마 세 파일의 끝 쉼표와 main 의 수정 상태는 raw 파일을 직접 열어 확인했다. OPC Foundation 인증 안내 두 페이지에 제조사 자체 인증 경로가 없음도 확인했다. 주의: 이 브리프의 신규 참고문헌 id(ref-1423~ref-1429)는 게시된 직전 실행 2026-10-10-06 의 id 와 겹치며 문서가 서로 다르다. 그대로 게시하면 각주가 다른 문서를 가리키게 되어 반려했다. VDA 5050 3.0.0 날짜는 VDA 계열 자료끼리도 표시가 다르므로 단일 발행일을 확정하지 않는 현재 방침이 맞다. 트랙 반영 제안(IDS 1.0)은 이번 브리프에서 다루지 않았다. 브리프는 외부 조사 메모를 변환한 것이라 검색 0회로 기록됐다. 정정 요청 없음.

직전 브리프(runs/<run_id>/research.json)는 입력에 있다. 위 사유에 답하는 보강 조사를 하고 전체 브리프를 다시 반환한다(researcher.md 12절).
