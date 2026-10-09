---
title: "18. 실시간 세계 상태·데이터 일관성"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 18
related_areas: [5, 15, 17, 20, 22, 27, 34, 38, 42]
tags: [세계 상태, 정보 나이, 발생 시각과 기록 시각, 상태 품질, 정정 이벤트, 시계 동기화]
status: draft
confidence: low
created: 2026-09-24
updated: 2026-10-09
sources: [ref-004, ref-030, ref-031, ref-044, ref-045, ref-051, ref-148, ref-282, ref-283, ref-284, ref-285, ref-286, ref-287, ref-288, ref-289, ref-290, ref-291, ref-292, ref-293, ref-294, ref-295, ref-296, ref-1275, ref-1276, ref-569, ref-1277, ref-1278, ref-1279, ref-1280, ref-1281, ref-1282, ref-1283, ref-1284, ref-575, ref-1285, ref-1286, ref-1287]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 18. 실시간 세계 상태·데이터 일관성

# 18. 실시간 세계 상태·데이터 일관성

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 3. 왜 중요한가

이번에 확인한 표준·프레임워크는 시각 필드·주기 발행·메시지 수명·생존성·STALE 표시 같은 장치만 주고 대상별 허용 경과 시간은 정하지 않으므로, 30초 전 '문 열림' 정보로 지금 통과를 확정할지는 ROP가 문·승강기 같은 대상마다 허용 경과 시간을 정하고 이를 넘으면 설비 어댑터에 다시 확인하는 규칙으로 답해야 할 것으로 보인다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 왜 중요한가](../../topics/2026/2026-09-25-area08-s3.md)에 있다.

## 4. 핵심 개념과 용어

- **정보 나이(Age of Information, AoI)** — 시각 표시된 상태 갱신을 받는 쪽의 정보가 얼마나 최신인지를 재는 지표로, 저지연 사이버물리 시스템의 설계·최적화 연구에서 평가 방법이 정리되어 있다(2021-05 서베이 기준). [사실][^ref-289]
- **발생 시각과 기록 시각** — GS1 EPCIS 2.0 온톨로지는 캡처 애플리케이션이 이벤트가 일어났다고 주장하는 시각(eventTime), 저장소가 이벤트를 기록한 시각(recordTime), 발생 장소의 UTC 차이(eventTimeZoneOffset)를 구분한다. [사실][^ref-045]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area08-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 절의 사례는 현장 유형별로 나뉜다. 2026-09-25 에 쓴 물류창고 시나리오 2건(설명용 가상 사례) 뒤에, 2026-10-09 실행에서 병원 사례 2건, 기타 현장 사례 1건, 제조 공장 사례 1건을 더했다.

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 이 영역은 두 시나리오 모두에서 상태가 언제의 것이고 얼마나 믿을 만한지를 판단하는 제약과 완료·인계 칸에 주로 관여한다.

### 시나리오 1. 입고한 팔레트를 문과 승강기를 지나 적치

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 입고한 팔레트를 방화문과 화물 승강기를 지나 보관 구역으로 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 확정된 팔레트에 대해 WMS가 적치 작업을 내린다(설명용 가정). |
| 작업 대상 | 팔레트 1개. VDA 5050 상태 스키마는 로봇이 취급 중인 적재물(loads)을 담으므로 로봇이 실제로 무엇을 싣고 있는지 보고받을 수 있다(3.0.0 판, 공식 저장소 main 기준, 확인일 2026-09-25). [사실][^ref-051] |
| 수행 자원 | 운반 로봇, 문·승강기 어댑터, 연계 대상인 설비 제어. Open-RMF 로봇 상태는 밀리초 단위 시각, 위치, 상태 7종, 문제 목록, 배터리 충전 상태를 한 메시지에 담는다. [사실][^ref-148] |
| 제약 | 이번에 연 Open-RMF 문·승강기 연동 문서 범위에서는 상태 발행 주기나 오래된 상태를 판정하는 규칙을 찾지 못했고, 메시지 정의에는 시각 필드만 있다. [추정][^ref-283][^ref-284] 승강기 상태에는 운영 모드(사람·AGV·화재·오프라인·비상)와 세션 id 가 있다. [사실][^ref-286] |
| 완료·인계 | 입고 단계의 RFID 판독 스트림은 누락·오판독이 섞여 미들웨어 정제가 필요하다. [사실][^ref-293] EPCIS 2.0 온톨로지는 발생 시각(eventTime)과 기록 시각(recordTime)을 구분한다. [사실][^ref-045] |
| 예외·성과 | 로봇 연결이 예기치 않게 끊기면 로봇이 연결 때 등록한 MQTT 유언으로 브로커가 CONNECTION_BROKEN 을 대신 알린다(VDA 5050 3.0.0 판, 공식 저장소 main 기준, 확인일 2026-09-25). [사실][^ref-031] 처리량·시간·비용에 주는 영향 수치는 미확인이다. |

로봇이 방화문 앞에 도착했을 때 ROP가 가진 문 상태가 오래전에 받은 '열림'이라면, 허용 경과 시간을 넘긴 값으로 통과를 확정하지 말고 문 어댑터에 다시 확인해야 할 것으로 보인다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] 승강기도 같은 방식으로 운영 모드가 화재·비상으로 바뀌지 않았는지 최신 상태로 확인한 뒤 탑승을 확정하는 흐름이 될 것으로 보인다. [추정][^ref-286]

### 시나리오 2. 보충 중 재고 기록과 실물의 불일치

**물류 흐름 단계:** 보충

**시나리오:** 피킹 위치를 보충하러 간 로봇이 WMS 기록과 다른 적재물을 보고

| 항목 | 내용 |
|---|---|
| 시작 조건 | WMS 재고 기록상 피킹 위치 수량이 기준 아래로 내려가 보충 작업이 생긴다(설명용 가정). |
| 작업 대상 | 보충용 케이스·팔레트. 로봇이 보고한 적재물과 WMS 기록을 함께 보관해 불일치를 드러내야 할 것으로 보인다. [추정][^ref-292][^ref-051] |
| 수행 자원 | 보충 로봇과 불일치를 확인하는 재고 담당자(설명용 가정). |
| 제약 | 해당 없음 |
| 완료·인계 | 잘못 들어온 완료 보고는 덮어쓰지 않고 정정 기록을 덧붙여야 원 기록과 정정 근거를 함께 추적할 수 있을 것으로 보인다. [추정][^ref-045][^ref-044] |
| 예외·성과 | 소매 자료에서 유추한 것이다: 한 소매업체 37개 매장 재고 기록의 65%가 실물과 맞지 않았다는 보고가 있으나, 이는 소매 매장 조건이며 물류센터 값이 아니다. [사실][^ref-292] 물류센터 재고 기록 정확도는 미확인이다. |

이 시나리오의 불일치 빈도는 소매 연구에서 유추한 것일 뿐이다. 물류센터에서 로봇 관측으로 WMS 재고를 정정한 공개 사례는 이번 조사에서 확인하지 못했다.

### 사례 3. 병원 혈액 이송 로봇의 승강기·자동문 연동

**현장 유형:** 병원

**사례:** 용인세브란스병원에서 혈액 이송 로봇이 승강기·스피드게이트·자동문을 지나 통제 구역과 층 사이를 이동

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 혈액. 혈액 이송 로봇이 통제 구역과 층 사이를 이동한다고 보도되었다(2022-11-18 기사 기준). [사실][^ref-1285] |
| 수행 자원 | 한국로봇산업진흥원 AI·5G 기반 서비스로봇 융합모델 실증사업으로 들인 로봇 5종 10대이며, LG전자·리드앤·트위니 등이 참여했다. [사실][^ref-1285] 통합반응상황실에 5G 기반 통합 관제 플랫폼을 더해 여러 로봇의 상태·위치를 실시간으로 모니터링하도록 구축을 진행 중이라고 보도되었다(2022-11-18 기준). [사실][^ref-1285] |
| 제약 | 로봇은 승강기·스피드게이트·자동문과 연동해 통제 구역과 층 사이를 지난다. [사실][^ref-1285] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 기사 1건에 기댄 것이며 교차 확인하지 못했다. 관제 플랫폼은 기사 시점에 구축 중이었으므로, 설비·로봇 상태를 실제로 어떻게 모으고 몇 초까지 믿는지는 이 자료로 알 수 없다.

### 사례 4. 병원에서 제조사가 다른 로봇의 승강기·자동문 공용

**현장 유형:** 병원

**사례:** 싱가포르 창이종합병원(Changi General Hospital, CGH)에서 제조사가 다른 로봇들이 기존 승강기·자동문을 함께 사용

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 제조사가 다른 로봇들이 공통 미들웨어 [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)(Robotic Middleware for Healthcare)로 병원의 기존 승강기·자동문을 함께 쓰며, 새로 들인 로봇도 기존 승강기·자동문과 연동하도록 설정할 수 있다고 보도되었다(2022-05-28 기준). [사실][^ref-1284] |
| 제약 | 승강기·자동문을 함께 쓸 때 긴급한 작업을 하는 로봇에 우선권을 준다. [사실][^ref-1284] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

CGH 보도자료에 따르면 싱가포르 국가 표준 Technical Reference 93(TR 93)은 자율 로봇과 승강기·자동문 같은 건물 설비 사이의 데이터 교환 지침을 정하고, KONE 의 차세대 승강기는 TR 93 에 맞춘 클라우드 연결·개방 API 로 RoMi-H 로봇과 시험 연동되었다(2022-05-28 기준). [사실][^ref-1283] 위 기사와 이 보도자료는 같은 기관 발표에서 나온 것이므로 서로를 교차 확인하는 독립 출처로 보지 않는다. TR 93 본문의 상태 갱신 주기·유효 시간 조항은 확인하지 못했다.

### 사례 5. 요양 시설·대학 건물에서 문·승강기를 지나는 자율 운반

**현장 유형:** 기타

**사례:** 요양 시설과 대학 사무 건물에서 자율 운반 로봇이 문·승강기를 지나 층 사이를 운반(실증 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 연계 대상: 로봇이 승강기 문 상태를 자기 라이다로 직접 판단했다(Frontiers in Robotics and AI, 2025-02-25). [사실][^ref-575] |
| 제약 | 승강기 문은 6초만 열려 있었다. [사실][^ref-575] 이처럼 열림 상태가 수 초만 유지되는 설비에서는 '열림' 정보의 허용 경과 시간을 그 설비의 유지 시간보다 짧게 잡아야 할 것으로 보인다. [추정][^ref-575][^ref-286] |
| 완료·인계 | 미확인 |
| 예외·성과 | 연계 대상: 로봇은 승강기가 의도하지 않은 층에서 멈춘 이유를 구분하지 못했고, 119건 작업에서 문·승강기가 얽힌 작업의 약 14%가 실패했으며(이 14%는 전체 작업 기준), 주된 실패 원인은 위치추정·검출 오류였다. [사실][^ref-575] 두 현장의 승강기 탑승 성공률은 93.2%·88.0%, 문 통과 성공률은 94.8%·88.1%로 보고되었다(문 수치는 시도 단위일 수 있다). [사실][^ref-575] |

이 사례의 문 상태 검출과 위치추정은 로봇 자체 지능·제어 경계의 연계 대상이다. ROP 쪽에서는 설비가 보고한 상태(승강기 상태의 문 상태·운영 모드·생성 시각)와 로봇이 직접 관측한 상태를 함께 확인하는 규칙이 필요할 것으로 보인다. [추정][^ref-575][^ref-286]

### 사례 6. 이기종 로봇팔 상태를 OPC UA 로 모은 실시간 디지털 트윈

**현장 유형:** 제조 공장

**사례:** 제조사가 다른 로봇팔 두 대의 상태를 OPC UA Pub/Sub 서버에 모아 3D 실시간 디지털 트윈으로 연결(연구 사례)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 두산 로봇팔과 KUKA 로봇팔의 상태 데이터(정보). [사실][^ref-296] |
| 수행 자원 | 스마트 커넥터가 각 로봇팔 데이터를 OPC UA Pub/Sub 서버에 모으고 3D 실시간 디지털 트윈이 이를 보여 준다. 구조는 공장 현장 설비를 대상으로 했으나 실험은 엣지 장치 1대·서버 1대의 실험실 구성이었다(2023년 논문 기준). [사실][^ref-296] |
| 제약 | 두 로봇팔의 통신 방식이 다르다(두산은 Modbus, KUKA 는 UDP 소켓). [사실][^ref-296] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 초당 50개 이상 노드 수집과 약 70 fps 렌더링을 보고했으나 종단 간 지연·동기화 오차 수치는 제시하지 않았다. [사실][^ref-296] |

이 연구는 이기종 로봇의 상태를 한곳에 모으는 구조를 보이지만 지연 수치가 없어, 모은 상태가 얼마나 오래된 것인지는 이 자료로 알 수 없다. 이 논문의 게재지 표기 차이는 11절의 oq-037 에 적었다.

## 6. 대표 접근법과 기술

상태의 오래됨을 판정하는 기본 장치는 발행 주기·기한·수명·생존성이며, ROS 2 QoS 는 이를 정책으로 두고 기한 초과·생존성 상실·변경을 이벤트 콜백으로 알린다(Jazzy 판 문서 기준). [사실][^ref-282]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area18-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

아래 표준·프레임워크는 상태에 시각·품질·연결 정보를 붙이는 장치를 제공하지만, 대상별 허용 경과 시간은 어느 것도 정하지 않는다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area18-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 연구 자료는 정보의 신선도 지표, 기록과 실물의 불일치, 판독 정제, 복제 상태의 수렴, 디지털 표현의 분류로 나뉜다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 대표 연구와 자료](../../topics/2026/2026-10-09-area18-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP의 직접 범위는 로봇 관제 인터페이스(VDA 5050·Open-RMF)의 로봇 상태, 설비 어댑터의 문·승강기 상태, EPCIS 같은 업무 이벤트를 시각·품질 정보와 함께 하나의 세계 상태로 모으고 불일치를 드러내는 것이며, 설비 자체 제어와 센서 융합은 외부에 맡기는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-283][^ref-045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | VDA 5050 3.0.0 은 위치추정 품질 점수(localizationScore)·편차 범위(deviationRange)를 로그·시각화 용도로만 쓰라고 정하고, 판단 신호로 위치추정 여부(localized: 참이면 x·y·theta 를 믿을 수 있음)를 둔다. [사실][^ref-031][^ref-051] 그래서 ROP 는 위치추정 여부·지도 id·보고 시각을 받아 그 위치를 믿을지 판단하고 품질 점수·편차 범위는 기록·표시에만 쓰며, 설비·다른 로봇 관측과의 대조를 판단 근거에 더하는 것으로 보인다(이 대조는 규격이 정한 것이 아닌 ROP 설계 제안이다). [추정][^ref-031][^ref-051] | 연계 대상: 로봇의 위치추정과 그 품질 계산, 센서 융합 |
| 시설·설비 제어 | 문·승강기 상태를 시각과 함께 받아 오래됨을 판정하고, 허용 경과 시간을 넘으면 통과 확정 전에 재확인을 요청한다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] | 연계 대상: 문·승강기 자체 제어와 설비 안전 제어. Open-RMF 에서는 문·승강기 어댑터가 로봇 작업을 방해할 요청을 막는다. [사실][^ref-283][^ref-284] |
| 상위 업무 시스템 | 업무 이벤트를 발생·기록 시각과 함께 세계 상태에 모으고 로봇 관측과의 불일치를 드러낸다. [추정][^ref-031][^ref-283][^ref-045] | 연계 대상: 전사 재고정책 |

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 이종 제조사를 연결하는 ROP라면 위치추정·설비 제어는 제조사와 설비에 맡기고, 받은 상태를 얼마나 믿을지 판단하는 규칙과 재확인 절차를 인터페이스로 맡는 구성이 된다.

로봇 자체 지능·제어 행은 2026-10-09 실행에서 고쳤다. 2026-09-25 판은 품질 점수·편차 범위로 위치를 얼마나 믿을지 판단한다고 적었으나, VDA 5050 3.0.0 7.8절은 이 두 값을 로그·시각화 용도로만 둔다. [사실][^ref-031] 다른 제조사의 신뢰도 필드를 같은 기준으로 다루는 방법은 열린 질문 oq-028 로 남아 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 현재 상태 표현은 현장과 자동으로 동기화되는 표현(디지털 섀도, ISO 23247 의 동기화된 표현)에 가깝고, 그 표현을 복제해 가정한 미래를 실험하는 쪽은 34. 시뮬레이션·예측용 디지털 트윈의 몫으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). [추정][^ref-291][^ref-290]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area18-s10.md)에 있다.

## 11. 열린 질문

이 영역의 가장 큰 공백은 대상별 허용 경과 시간의 근거이며, 아래 질문은 [열린 질문](../../open-questions.md) 목록에도 있다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 열린 질문](../../topics/2026/2026-10-09-area18-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 1차 조건부 승인 수정 14건 이행, 2차 수정: 5절 승강기 추론 문장에 [추정] 태그·각주 추가, 완료·인계 칸 EPCIS 문장을 사실 부분만 남김 (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area08-s7.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,454자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area08-s4.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "4. 핵심 개념과 용어" 절(1,436자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area08-s6.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "6. 대표 접근법과 기술" 절(1,386자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 대표 연구와 자료](../../topics/2026/2026-09-25-area08-s8.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "8. 대표 연구와 자료" 절(1,250자)을 옮겼다. 2차 수정: Yates 외 항목에서 브리프에 없는 평가 문장을 뺐다 (실행 2026-09-25-24)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-09
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-10-09
[^ref-289]: Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S., Age of Information: An Introduction and Survey, 2021-05, https://arxiv.org/abs/2007.08564, 접근일 2026-09-25 (원문 미열람)
[^ref-290]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-292]: DeHoratius, N., & Raman, A., Inventory Record Inaccuracy: An Empirical Analysis, 2008, https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789, 접근일 2026-09-25 (원문 미열람)
[^ref-293]: Massawe, L. V. 외(Sensors), Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach, 2012-03-28, https://doi.org/10.3390/s120404187, 접근일 2026-09-25 (원문 미열람)
[^ref-296]: 김지형, OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454, 접근일 2026-10-09
[^ref-1283]: Changi General Hospital (CGH), Changi General Hospital, CapitaLand Investment and KONE collaborate to advance the integration of robotics in buildings, 2022-05-28, https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings, 접근일 2026-10-09
[^ref-1284]: The Straits Times (SingHealth 게재, Wong Shiying), New software enables different robots to communicate with each other and building infrastructure, 2022-05-28, https://www.singhealth.com.sg/news/tomorrows-medicine/new-software-enables-different-robots-to-communicate-with-each-other-and-building-infrastructure, 접근일 2026-10-09
[^ref-575]: Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau; Frontiers in Robotics and AI), On realizing autonomous transport services in multi story buildings with doors and elevators, 2025-02-25, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full, 접근일 2026-10-09
[^ref-1285]: 메디포뉴스 (이형규), 용인세브란스병원, 지능형 의료서비스로봇 생태계 구축, 2022-11-18, https://medifonews.com/news/article.html?no=172554, 접근일 2026-10-09
