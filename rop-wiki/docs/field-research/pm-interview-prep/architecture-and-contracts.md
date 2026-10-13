---
title: "ROP 책임 경계와 연동 계약"
type: field-research
research: pm-interview-prep
related_areas: [10, 12, 18, 20, 21, 22, 23, 29, 41, 42, 51]
tags: [면접 준비, ROP, 책임 경계, 연동 계약, API, 이벤트, 시퀀스, 승강기 세션, LLM]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-031, ref-251, ref-282, ref-283, ref-284, ref-306, ref-1579, ref-1593, ref-1598]
---

[홈](../../index.md) › [스터디](../index.md) › [면접 준비](index.md) › ROP 책임 경계와 연동 계약

# ROP 책임 경계와 연동 계약

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

업무빌딩의 순찰·배송·안내 서비스에서 ROP가 무엇을 결정하고 무엇을 제조사·설비·서비스 계층에 맡기는지, 식별자와 상태를 어떻게 나눠 두는지, 배송 하나가 어떤 순서로 흐르는지, API와 이벤트 계약은 어떻게 생겼는지를 정리한다. 이 페이지의 구성도·시퀀스·식별자·상태·JSON·정책은 모두 **[의견]인 설계 예시**다. 실제 Open-RMF·VDA 5050·Spot의 메시지 형식이나 이미 구현된 제품 API가 아니다. 사실로 인용하는 기능 범위에는 각주를 붙였고, 자료 번호는 [핵심 학습 자료](core-materials.md)의 카드다.

## 공식 자료가 해결하는 범위

| 수단 | 원문에서 확인한 기능 | 별도 구현·합의가 필요한 것 | 적용 결정 [의견] |
|---|---|---|---|
| Open-RMF 플릿 어댑터 | [사실] Full Control은 경로 지정·중단과 교체·현재 위치 제공을 전제로 하고, Traffic Light는 일시정지·재개 중심이다[^ref-251] | 제조사 API 연결, 좌표 정합, 실제 취소·정지 확인, 운영·보안·사용자 서비스 | 제조사가 제공하는 제어 수준을 먼저 확인한 뒤 어댑터 범위를 고른다 |
| Open-RMF 문·승강기 어댑터 | [사실] 지도의 설비 이름·층과 제어 가능한 설비를 연결한다. 자동문만 연동할 수 있고 승강기 제어기가 명령을 받아들여야 한다[^ref-283][^ref-284] | 현장 설비 API, 전기·통신 공사, 소유자 승인, 화재·수동 모드, 점유 관측 | 승강기 모델·제어반·라이선스와 업체별 지원 표를 확보한다 |
| VDA 5050 3.0.0 | [사실] 관제와 이동 로봇 사이의 order·state·action·map 등 통신 의미. 안전·교통 논리·주변 설비와 외부 IT·프로젝트 절차·운영 책임·사이버보안은 범위 밖[^ref-031] | 시설·고객 서비스 API, 교통 알고리즘, 안전 구현, 보안, 책임·인수 절차 | 두 제조사 모두 해당 판·행동을 지원할 때의 옵션. 제품 지원은 미확인 |
| Spot SDK 5.2.0 | [추정] 벤더 주장: GraphNav 명령과 피드백, 상태·영상·로그 서비스, 시간 동기·lease·비상 정지[^ref-1579][^ref-1598] | 상위 요청 id 대응, 업무 완료, 물품 인계, 출입 권한, 빌딩 시스템 연결 | 직접 어댑터 또는 지원되는 제조사 관제 API 가운데 한 제어 경로를 고른다 |
| Robotnik 소프트웨어 | [추정] 벤더 주장: ROS 2 기반 구조, RLC·Command Manager의 외부 연계 설명[^ref-1593] | 최신 실기 API 상세, 취소·실패 의미, 권한, 지원 SLA는 계약으로 확인 | 공개 시뮬레이터를 실기 SDK의 완전한 사양으로 쓰지 않는다 |
| ROS 2 QoS·MQTT | [사실] 상태 신선도·생존 확인 정책과 메시지 전달 등급[^ref-282][^ref-306] | 업무 중복 방지, 증거 보관, 재연결 뒤 실물 대조 | 역할이 다른 도구이며 완제품 ROP의 대체재가 아니다 |

[사실] VDA 5050에서 취소는 즉시 물리 정지와 같지 않다. 명세는 로봇의 이동 방식에 따른 정지 처리와 그 뒤의 상태, 같은 orderId와 orderUpdateId를 받았을 때의 처리를 §6에서 따로 정의한다.[^ref-031] [의견] 이 규칙을 상위 API의 재시도와 함께 확인하되, 아래 예시 API를 VDA 메시지라고 부르지 않는다.

## 시스템 구성도

[의견] ROP는 여러 기종·시설·업무의 운영 조율을 맡는 논리적 계층이다. 특정 표준이 보장하는 제품명이 아니다.

```mermaid
flowchart TB
    U[이용자 앱 · 키오스크 · 직원 화면] --> S[서비스 플랫폼]
    S --- B[사용자 권한 · 요청 · 결제 · 알림 · 인계 원장]
    S --> G[실행 검증 게이트]
    L[선택 기능: 채팅 LLM] -->|구조화된 요청 후보| G
    G --> R[ROP: 작업 상태 · 배정 · 정책]
    R --- D[능력 · 구성 · 지도 · 상태 이력 · 감사]
    R --> E[현장 엣지 조율기]
    E --- Q[교통 · 공용 자원 예약 · 작업 기록]
    E --> A[기종별 어댑터]
    A --> F[제조사 RCS · FMS]
    A --> X[직접 SDK 경로]
    F --> W[4휠 로봇]
    X --> P[4족 로봇]
    E --> I[시설 어댑터]
    I --> C[승강기 · 자동문 · 출입 제어기]
    W --- WL[기체: 위치 추정 · 주행 · 회피 · 안전 제어]
    P --- PL[기체: 위치 추정 · 보행 · 안전 제어]
```

도식의 제조사 관제 경로와 직접 SDK 경로는 기종별 선택 예다. 같은 로봇에 독립된 두 명령 발행자를 동시에 두지 않는다. 제조사 관제와 직접 API를 함께 쓰려면 소유권 전환·우선권·회수 절차를 명시한다. Spot SDK의 lease 개념은 참고하지만 다른 로봇이 같은 기능을 제공한다고 가정하지 않는다.[^ref-1598]

## 책임 경계

[의견] 기능마다 결정·기록의 주체와 다른 계층이 맡는 부분을 나눈다.

| 기능 | 결정·기록의 주체 | 다른 계층이 맡는 부분 | PM 산출물 |
|---|---|---|---|
| 사용자·결제·알림·약관 | 서비스 플랫폼 | ROP는 요청·완료 근거·예외를 전달 | 사용자 여정, 권한표, 과금 기준, 취소·환불 정책 |
| 능력·구성·가용성 | ROP 등록부 + 제조사 제공 상태 + 현장 승인 | 로봇이 보고한 상태와 현장 검증 범위를 분리 | 기종·펌웨어·센서·적재·구역별 승인표 |
| 작업 분해·배정 | ROP | 제조사 관제는 자기 플릿 안의 배정·명령 변환 가능 | 한 작업의 소유자와 하위 작업 id 대응 |
| 경로·교통·공용 자원 | ROP·현장 조율기가 플릿 사이의 자원 충돌·시간 예약 | 제조사 planner가 허용 경로 안에서 주행, 로봇이 즉시 회피·정지 | 누가 길을 바꿀 수 있는지와 경로·점유 데이터 계약 |
| 명령·실행 추적·취소·복구 | ROP가 업무 상태, 어댑터·관제가 제조사 명령·피드백 대응 | 로봇의 안전 판단을 ROP가 우회하지 않는다 | 접수·실행·물리 종료·업무 종료를 구분한 상태표 |
| 위치 추정·바퀴/보행 제어·회피 | 로봇과 제조사 제어 SW | ROP는 부정확·상실 상태를 받아 배정·구역 진입 제한 | 진단 정보, 한계, 복구 요청과 승인 절차 |
| 승강기·문·출입 설비 | 설비 제어기가 물리 운전·인터록. 시설 관리자에게 최종 현장 권한 | ROP는 승인된 요청·세션·예약·상태를 관리 | 사용 권한, 수동·화재 우선, 변경 검토·점검 책임 |
| 점검 데이터·물품 인계 | 서비스 도메인·운영자가 증거와 품질 확인 | 로봇의 "도착"은 한 단계의 결과 | 검사 품질, 수령 증거, 분쟁, 재측정 절차 |

**판단 배치:** 클라우드에는 고객·과금·전사 분석·장기 기록, 엣지에는 현장 작업 원장·시설 세션·조율·오프라인 허용 정책, 로봇에는 위치 추정·즉각 반응·보행과 주행·안전 기능을 둔다. 실제 제품이 이 구성을 지원하는지는 따로 검증한다. 클라우드 단절과 로봇 무선 단절을 같은 상태로 처리하지 않는다. 계층별 결정 주체의 일반 논의는 [현장 적용·운영 검증 — 엣지·클라우드와 연동 계약](../field-readiness-rop/edge-cloud-and-integration.md)에 있다.

## 식별자와 상태를 섞지 않기

| 대상 | 예시 식별·버전 | 반드시 함께 보관할 정보 |
|---|---|---|
| 업무 요청 | tenant_id, site_id, request_id, idempotency_key | 요청 본문 해시, 요청자 권한, 생성·마감·접수 시각 |
| 실행 | task_id, attempt_id, vendor_command_id | 현재 제어 소유자, command_seq, 재시도·취소 이유 |
| 로봇·능력 | robot_id, vendor_serial, config_version | 펌웨어·SDK·센서·적재·현장 승인·제한의 유효기간 |
| 지도 | map_id, map_version, floor_id, coordinate_frame | 단위·축·기준점·좌표변환 버전·현장 승인자 |
| 시설 | facility_id, vendor_device_id, resource_session_id | 요청자, 허용 목적, lease·fencing 값, 예약, 물리 점유, 상태 관찰 시각 |
| 점검·물품 | asset_id 또는 parcel_id, evidence_id | 교정·측정 품질 또는 보관 책임·인계 상태 |
| 이벤트 | event_id, task_seq, schema_version | 발생 시각, 수신 시각, 출처, trace_id, 이전 상태·버전 |

**서비스 작업 상태 예시:** REQUESTED → ACCEPTED → QUEUED → ASSIGNED → EXECUTING → AWAITING_VERIFICATION → SUCCEEDED. 예외 분기는 BLOCKED, RECOVERY_REQUIRED, FAILED, CANCEL_REQUESTED → CANCELLED이며, 실제 실행 결과를 아직 확인하지 못했으면 RECONCILIATION_REQUIRED로 둔다. **통신 단절은 그 자체로 FAILED·CANCELLED·물리 정지가 아니다.**

**관측 차원은 따로 둔다:** 연결(CONNECTED / STALE / DISCONNECTED), 위치(LOCALIZED / UNCERTAIN / LOST), 모드(AUTONOMOUS / TELEOP / MAINTENANCE), 화물(EMPTY / LOADED / RECIPIENT_PENDING / HANDED_OVER), 시설(AVAILABLE / RESERVED / OCCUPIED / UNKNOWN / OUT_OF_SERVICE). 위치가 오래된 로봇을 "현 위치에서 정지"로 그리지 않는다.

**상태 신선도:** observed_at, received_at, 시간 동기 품질을 모두 보관한다. 화면은 마지막 확정 위치와 경과 시간을 보여 준다. 배터리 값이 오래되면 계획상 잔량과 실측 잔량을 구별하고 신규 배정을 막거나 확인 절차를 거친다. 허용 나이와 경고 주기는 로봇·설비·서비스별 시험으로 정한다. ROS 2의 lifespan·deadline은 이를 구현하는 수단의 일부이며 업무 정책 자체는 아니다.[^ref-282]

## 배송 연동 시퀀스

[의견] 정상 배송과 응답 유실의 처리 경로다. 물리 인계 증거는 적재함 센서·스캔·수령 확인을 실제 구성에 맞춰 정의한다.

```mermaid
sequenceDiagram
    actor U as 발송자 · 수령자
    participant S as 서비스 플랫폼
    participant R as ROP
    participant A as 기종 어댑터 · 제조사 관제
    participant B as 로봇
    participant F as 시설 어댑터 · 제어기
    U->>S: 물품 규격 · 목적지 · 수령 방식
    S->>R: 요청 id · 중복 키 · 권한 · 지도 판
    R->>R: 중복 · 능력 · 상태 신선도 검증
    R-->>S: 접수(task_id)
    U->>S: 직원 적재와 잠금 확인
    S->>R: 적재 증거와 운송 승인
    R->>F: 승인된 승강기 세션 예약
    F-->>R: 세션과 현재 층 · 문 · 모드 관측
    R->>A: 실행 id와 이동 작업
    A->>B: 제조사 명령과 기한
    B-->>A: 명령 수락 · 진행 · 실제 위치
    A-->>R: 실행 상태와 관찰 시각
    alt 응답 유실 또는 시설 상태 불명
        R->>A: 같은 실행 id의 현재 상태 조회
        R-->>S: 확인 중 또는 지연
        Note over R,F: 확인 전에는 새 중복 실행과 점유 자동 해제 금지
    else 도착 확인
        R->>F: 승강기 실제 퇴실 확인 뒤 세션 해제
        R-->>S: 수령 대기
        S-->>U: 일회용 수령 인증 안내
        U->>S: 인증과 인출 확인
        S->>R: 인계 증거
        R-->>S: 서비스 완료 이벤트
        S-->>U: 수령 완료 영수증
    end
```

승강기에서 내린 뒤의 세션 해제는 실제 퇴실이 확인되는 즉시 한다. 예약 승인만으로 진입하지 않는다. 현재 층·문·모드·진입 공간·로봇 위치 등 구성에 맞는 물리 조건을 확인한다.

## API와 이벤트 계약 예시

[의견] 아래의 `/v1`은 이 예제의 임의 판이다. 제조사 SDK나 VDA API의 이름이 아니며, 구현·부하·보안 시험을 거치지 않은 설계 템플릿이다.

```http
POST /v1/service-tasks
Authorization: Bearer <short-lived-scoped-token>
Idempotency-Key: delivery-req-001
Content-Type: application/json
```

```json
{
  "schema_version": "1.0",
  "request_id": "req-001",
  "tenant_id": "tenant-A",
  "site_id": "building-A",
  "service_type": "delivery",
  "origin": {"location_id": "mailroom", "floor_id": "L1"},
  "destination": {"location_id": "reception-3", "floor_id": "L3"},
  "parcel": {"parcel_id": "parcel-001", "mass_kg": 2.0},
  "requirements": ["locked_compartment", "recipient_confirmation"],
  "map": {"map_id": "building-A", "version": "2026-10-13.1"},
  "deadline_at": "2026-10-13T15:00:00+09:00",
  "handover_policy_id": "staff-load-recipient-unload-v1"
}
```

| 계약 항목 | 예시 동작 | 인수시험 질문 |
|---|---|---|
| 권한·입력 | 서버가 토큰의 tenant·site·역할과 본문을 대조. 질량·규격·기한·목적지 확인 | 본문의 tenant만 바꾸면 다른 고객의 작업을 만들 수 있는가? |
| 접수 | 202 Accepted와 task_id·status_url 반환. 기체 출발을 뜻하지 않는다 | DB 기록은 성공했는데 응답이 유실됐을 때 같은 키의 재요청 결과는? |
| 중복 | 같은 범위의 키 + 같은 본문은 기존 task 반환. 본문이 다르면 409 Conflict | 브라우저 재전송·어댑터 재시작·다른 IP에서도 한 업무인가? |
| 기한 | 접수 RPC 타임아웃과 작업 마감 시간·제조사 명령 유효 시간을 분리 | HTTP 타임아웃 뒤에도 로봇이 실행 중일 수 있음을 처리하는가? |
| 취소 | POST /v1/service-tasks/{task_id}/cancel. 요청은 CANCEL_REQUESTED, 물리·업무 정리 뒤 CANCELLED | 인계 직후 취소와 완료가 경합할 때 최종 원장 하나를 유지하는가? |
| 재시도 | 조회로 실제 상태를 재조정한 뒤 재시도. 불가역 행동은 상태 확인 없이 재전송 금지 | 적재함 개방·상하차·시설 진입이 중복되지 않는가? |
| 부분 완료 | 물품이 운송 중이면 취소 뒤 반송·직원 회수 하위 작업 생성 | 원래 작업의 취소와 화물 처리의 종결을 구별하는가? |
| 보존 | 키·실행 id의 보존 기간은 최대 작업·재시도·감사 기간을 포함해 합의 | 키 만료 뒤의 지연 재전송이 새 배송을 만들지 않는가? |

```json
{
  "schema_version": "1.0",
  "event_id": "evt-023",
  "task_id": "task-001",
  "request_id": "req-001",
  "attempt_id": "attempt-1",
  "task_seq": 23,
  "type": "service.handover_verified",
  "occurred_at": "2026-10-13T14:36:00+09:00",
  "received_at": "2026-10-13T14:36:01+09:00",
  "state": "SUCCEEDED",
  "completion_mode": "AUTONOMOUS_TRANSPORT_STAFF_LOADED",
  "evidence": {"handover_receipt_id": "receipt-001"},
  "actor": {"kind": "recipient_token", "id": "receipt-subject-001"},
  "robot_id": "wheeled-01",
  "config_version": "cfg-17",
  "trace_id": "trace-001"
}
```

이벤트는 **최소 한 번 전달될 수 있다고 가정**한다. 소비자는 event_id로 중복을 제거하고 task_seq로 순서를 검증한다. 누락이나 역전이 보이면 현재 상태 API와 이벤트 이력으로 복구한다. 전송 시각보다 발생·관측 시각을 업무 판단에 쓴다. 로봇 도착, 점검 데이터 검증, 인계 확인은 서로 다른 사건이다. 원본 영상·이름·전화번호는 이벤트 본문에 기본으로 넣지 않는다.

## 시설의 예약과 물리 상태 불일치

[의견] 예약 없음 → 예약 → 진입 승인 → 점유 → 퇴실 확인 → 해제를 구분한다. 각 단계는 facility_id, session_id, 요청자·작업 id, 관찰 시각, 제어 소유권과 함께 기록한다.

- 예약 기한 만료는 물리 공간이 비었다는 증거가 아니다. 로봇이 승강기 안에서 단절되면 점유를 UNKNOWN으로 두고 현장 확인이나 설비 관측으로 복구한다.
- 지연된 이전 세션 명령이 새 세션을 닫지 못하도록 epoch·fencing 같은 소유권 검증을 설계한다. 설비가 지원하지 않으면 어댑터의 직렬화만으로 충분한지 실패 시험으로 확인한다.
- 문 열림 ACK, 현재 문 열림 센서, 로봇의 통과 완료를 분리한다. 출입 허가는 요청마다 유효 구역·시간·주체를 검증한다.
- 화재·정비·수동 운전은 로봇의 예약보다 우선하는 현장 규칙을 합의한다. ROP는 시설 인터록을 우회하거나 방화문을 고정 개방하지 않는다.
- 재연결 시 현재 층·문·모드·로봇 위치·작업과 화물 상태를 대조한 뒤 소유권을 다시 얻는다. 이전 큐 전체를 무조건 재생하지 않는다.

## 통신 계약과 보안

| 데이터 | 요구·설계 제안 | 장애 시 동작 |
|---|---|---|
| 업무 명령 | 인증, request·task·command id, 기한, 수락·진행·종결 구분, 중복 억제 | 응답 유실은 상태 조회·재조정. 실패로 즉시 재배정하지 않는다 |
| 위치·배터리·시설 상태 | 관찰 시각·신선도·품질, 상태별 최대 허용 나이 합의 | stale 표시, 신규 진입·배정 제한. 안전 제어는 로컬 정책 |
| 점검 원본·영상 | 센서 종류·시각·품질·접근권, 대역폭·보존 정책 | 영상 지연은 명령 성공·정지 판단과 분리. 전송 지연 중에도 데이터 유효기간 확인 |
| 감사 로그 | 수정 추적, 행위자·변경 전후·trace·시간 동기, 현장 버퍼 | 클라우드 복구 뒤 중복 없이 합치고 결손을 표시 |

**지연 예산은 서비스별로 합의한다.** 배송은 총 마감과 인계 대기, 안내는 일행 이탈을 감지하고 안전하게 대기하기까지의 시간, 순찰은 측정의 유효기간과 경보 대응 시간이 중요하다. 즉각적인 정지와 보행 균형은 인터넷 왕복 시간을 전제로 설계하지 않는다. 어떤 서비스에도 통하는 "100 ms면 안전" 같은 값을 근거 없이 제시하지 않는다.

인증·권한·감사 초기안: 기체·어댑터별 신원과 인증서, 역할·site·동작 범위 제한, 망 분리와 접근 허용 목록, 비밀 정보 회전, 원격 조작의 별도 승인과 기록 정책, 설정 변경의 승인·버전·롤백. 지도는 같은 map_id라도 version·층 좌표·출입 정책이 다르면 배정 전에 정합성을 확인한다. 암호·망 보안의 세부는 보안 담당자의 설계·검증 범위다.

## 채팅과 LLM의 위치

[의견] 선택 기능이다. 세 서비스의 실행은 폼·키오스크·일정·업무 시스템 이벤트만으로도 기획할 수 있다. LLM은 자연어 요청을 구조화하고 빠진 정보를 묻거나 계획 후보를 설명하는 역할에 둔다.

실행 게이트는 로그인 주체, 출입·물품 권한, 로봇 능력, 배터리 신선도, 시설 상태, 지도·설정 판, 마감, 중복을 결정적 규칙으로 검증한다. 문서나 채팅에 적힌 "관리자 승인" 문자열을 실제 권한으로 간주하지 않는다. 새 경로·새 동작·권한 확대·물리 인계 변경은 명시된 승인 절차를 거친다. LLM 출력은 바퀴 속도·보행·비상 정지·출입 해제 명령에 직접 연결하지 않는다. 고객과 합의한 저위험 반복 요청은 규칙 검증 뒤 자동 실행할 수 있으며, 모든 요청에 사람의 클릭을 강요할 필요는 없다.

## 연결 영역

- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md): 어댑터·표준·설비·업무 시스템.
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md): 명령 id·접수·완료·재시도.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md): 상태 신선도.
- [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): 판단 배치와 통신.
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md): 인증·권한.
- [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md): LLM의 위치.
- [현장 적용·운영 검증 — 엣지·클라우드와 연동 계약](../field-readiness-rop/edge-cloud-and-integration.md): 기술별 보장 경계와 작업별 단절 정책.

[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-12
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-12
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-10-12
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-12
[^ref-1579]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_and_robot_locomotion.md (master, blob 1362051), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_and_robot_locomotion.md, 접근일 2026-10-12
[^ref-1598]: Boston Dynamics (Spot SDK docs), Robot Services (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/concepts/robot_services.html, 접근일 2026-10-12
[^ref-1593]: Robotnik Automation, Software solutions — Open Architecture, RLC and Command Manager, Advanced Localization and Navigation, 2025-11-28, https://robotnik.eu/software-solutions/, 접근일 2026-10-12
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-12
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-10-12
