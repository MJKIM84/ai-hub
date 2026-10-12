---
title: "22. 설비·건물 시스템 연동"
type: area
category: "F. 연동"
area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [승강기 연동, Open-RMF, VDA 5050, 작업대 인계, KS B 7317, 단체표준]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-023, ref-031, ref-047, ref-049, ref-060, ref-103, ref-163, ref-202, ref-283, ref-284, ref-286, ref-312, ref-313, ref-314, ref-315, ref-316, ref-317, ref-318, ref-319, ref-320, ref-321, ref-322, ref-943, ref-1398, ref-1431, ref-1432, ref-1433, ref-1434, ref-1435, ref-1436, ref-1437, ref-1438, ref-1439, ref-1440, ref-1442, ref-1443, ref-1444]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 22. 설비·건물 시스템 연동

# 22. 설비·건물 시스템 연동

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
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 3 · 마지막 갱신: 2026-10-11 · 마지막 실행: 2026-10-11
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇–관제 인터페이스 표준인 VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 목록에 넣는다. [사실][^ref-031] 그러나 같은 명세는 관제–이동로봇 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. [사실][^ref-031]

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area22-s3.md)에 있다.

## 4. 핵심 개념과 용어

아래 개념은 대부분 [Open-RMF](../../glossary/open-rmf.md)와 [VDA 5050](../../glossary/vda-5050.md)의 공개 문서에서 왔으며, 각각 발행 주체 한 곳의 문서에 기댄다(확인일 2026-09-25).

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area10-s4.md)에 있다.

### 2026-10-11 보강

- **AGV 모드 전환과 세션 수락** — Open-RMF 개발자는 2024-08-21 토론 답변에서, 세션을 안전하게 수행하려면 승강기가 별도 AGV 모드여야 하는 경우 모드 전환을 마칠 때까지 승강기 상태에 세션 식별자(session_id)를 내보내지 말아야 한다고 권고했다. [사실][^ref-1435] 같은 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다. [사실][^ref-1435] 이 권고는 설계 의도의 설명이며 현장 안전 동작을 재현한 결과가 아니다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 수치는 쓰지 않는다.

**물류 흐름 단계:** 출하 (같은 층간 운반 구조가 입고·적치에도 나타난다)

**시나리오:** 위층 보관 구역의 출하 화물을 승강기로 내려 1층 출하 작업대(컨베이어 입구)에 인계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템의 출하 지시로 운반 작업이 생기고, 출하 작업대가 화물을 받을 준비가 됐는지가 인계 단계의 진행 조건이 된다. 작업대 앞 구역을 VDA 5050 해제 구역으로 두면 로봇이 진입을 요청하고 관제가 허가·대기·철회·거절로 답한다. [사실][^ref-031] |
| 작업 대상 | 출하용 박스·토트(가상) |
| 수행 자원 | 이동로봇은 운반, 승강기·자동문은 각 설비 제어기가 제어하고, Open-RMF 구조에서는 문·승강기 어댑터가 요청을 걸러 설비 노드에 전달한다. [사실][^ref-283][^ref-284] |
| 제약 | 승강기는 요청한 세션이 점유하며 AGV 모드에서는 정지 시 문이 열려 있다. [사실][^ref-312] KS B 7317 은 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한다. [사실][^ref-314] |
| 완료·인계 | 로봇은 하역 위치에서 인제스터 서비스를 요청하고 확인을 받아야 다음 단계로 넘어간다. [사실][^ref-023] 이 요청–결과 방식과 구역 진입 허가를 조합하면 설비 준비 신호와 로봇 도착을 한 작업 흐름 안에서 맞출 수 있을 것으로 보인다. [추정][^ref-023][^ref-031] |
| 예외·성과 | 승강기가 화재·비상·오프라인 모드로 바뀌거나 문 상태가 오프라인·알 수 없음이면 해당 설비를 쓰는 작업을 멈추거나 다른 경로·사람 확인으로 넘기는 예외로 다뤄야 할 것으로 보인다. [추정][^ref-286][^ref-313] 승강기 세션 대기는 출하뿐 아니라 입고·적치의 층간 운반에서도 처리량과 운반 시간에 영향을 줄 것으로 보인다. [추정][^ref-312][^ref-286][^ref-060][^ref-103] |

이 시나리오에서 이 영역이 맡는 칸은 수행 자원(설비와의 요청 경로), 제약(승강기 점유와 탑승 조건), 완료·인계(작업대의 결과 확인)다. 분류 원문의 질문인 컨베이어 준비와 로봇 도착 맞추기에는 현재 추정 수준의 답만 있다. 두 시점을 함께 최적화한 공개 연구는 이번 조사에서 찾지 못했다.

복구 규칙 자체는 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)에서 다룬다. 흐름 전체의 칸은 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

**현장 유형:** 기타

**사례:** 도서관에서 기존 승강기를 로봇의 층간 이동에 연동 (도서관 현장 설계 문서)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 연계 대상: 현장에 새로 설치한 승강기 제어함 안의 PLC(Beckhoff CX9020)가 서버의 ADS 명령을 받아 드라이 접점으로 승강기 신호를 조작하고, 승강기 업체가 기존 승강기를 AGV 모드로 개조했다. [추정] 벤더 주장[^ref-1440] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 연계 대상: 화재 경보가 울리면 승강기가 수동 모드로 돌아가고 PLC 는 재시작할 때까지 오류 상태에 머물러, 다시 시작하려면 사람의 개입이 필요하다. [추정] 벤더 주장[^ref-1440] |

이 사례는 한 도서관 현장의 벤더 설계 문서(발행일 미확인, 확인일 2026-10-11)에 기대며, 승강기 자체 제어반이 아니라 새로 단 제어함을 거쳐 신호를 조작하는 방식이다. 같은 문서는 승강기 상태 전송 주기를 개요에서는 1 Hz 로, 서버 절에서는 2초마다로 서로 다르게 적고 승강기 요청은 1초마다 보낸다고 적는다. [추정] 벤더 주장[^ref-1440] 차이를 설명하는 근거가 없어 실제 주기는 결론을 내리지 않는다.

이 사례에서 이 영역이 맡는 칸은 수행 자원(설비 쪽 연결 경로)과 예외·성과(비상 뒤 설비 복귀)다. 한 현장의 설계이므로 다른 건물의 화재 복구 조건으로 일반화하지 않는다.

**현장 유형:** 병원

**사례:** 혼잡한 병원에서 승강기를 함께 쓰며 약품 배송 (고려대 구로병원 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 약품 [사실][^ref-943] |
| 수행 자원 | 미확인 |
| 제약 | 승강기 가동률이 높을수록 배송 시간이 길어졌다. [사실][^ref-943] 논문은 ROC 분석으로 찾은 [승강기 가동률](../../glossary/elevator-operating-rate.md)(EOR) 임계값 59.01% 를 현장 특정값으로 해석해야 하며 다른 병원에 적용하려면 재보정이 필요하다고 명시한다(2026-03-31 발표). [사실][^ref-943] |
| 완료·인계 | 미확인 |
| 예외·성과 | 2026-10-11 재확인에서도 논문에는 전체 성공률 87.03% 의 분모를 설명하는 구절이 없고, 분석 대상 122건에서 실패 14건을 뺀 108건의 비율(약 88.52%)과 보고값이 다르다. [사실][^ref-943] |

병원 쪽 요구와 다른 칸은 [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md)에서 다룬다. 이 사례에서 이 영역이 보는 것은 공유 승강기라는 설비 자원이 로봇 배송에 거는 제약이다. 병원·호텔·그래프·지도 연구의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 승강기 가동률·통신 상태·카 내부 점유를 나눠 수집해 현장별 임계값을 새로 검증해야 한다는 것이 이 위키 구축자의 의견이다(oq-010). [의견][^ref-943]

**현장 유형:** 상업 시설

**사례:** 상업 건물(Tokyo Midtown Yaesu)의 기존 화물 승강기·자동문을 로봇 배송에 연결 (NAVER LABS 발표)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | NAVER LABS 는 2026-07-23 블로그에서 다중 로봇 플랫폼 ARC 가 이 건물의 기존 화물 승강기·자동문과 출입 경로를 중앙에서 연결한다고 설명했다. [추정] 벤더 주장[^ref-1444] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 블로그는 연말까지 전 층 로봇 배송으로 넓힐 계획이라고 밝혔으며, 이는 계획이지 운영 결과가 아니다. [추정] 벤더 주장[^ref-1444] 공급자 밖의 독립 운영 평가는 확인하지 못했다. 기존 건물 도입 사례는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 따로 확인하기 전에는 운영 실증으로 세지 않는 것이 맞다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1444]

## 6. 대표 접근법과 기술

공개 자료에서 확인한 접근법은 어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계, 관제의 구역 진입 허가 세 가지다. [사실][^ref-283][^ref-023][^ref-031]

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area22-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 공개 규격은 오픈소스 메시지 정의와 로봇 탑승 안전 표준이 중심이다. [사실][^ref-286][^ref-314] 설비–로봇 연동 자체를 정한 국제 표준은 이번 조사에서 확인하지 못했다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area22-s7.md)에 있다.

## 8. 대표 연구와 자료

승강기를 포함한 다층 이동은 경로계획·병원 배송·지도 구축 연구에서 다뤄지며, 연구마다 실물 실증·수치 실험·시뮬레이션으로 조건이 다르다. [사실][^ref-943][^ref-103][^ref-321][^ref-163] 2026-09-25 에는 원문을 열지 못해 결과 수치를 쓰지 않았고, 2026-10-11 재확인에서 아래 실험 조건과 일부 결과를 확인했다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area22-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 시설·설비 제어 | 어댑터를 통한 작업 요청·점유 예약(승강기 세션 등)·상태 확인·완료 확인 [추정][^ref-283][^ref-284] | 연계 대상: 승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어(설비 제조사·설비 제어기) [추정][^ref-283][^ref-284][^ref-031] |
| 로봇 자체 지능·제어 | 로봇이 탑승 조건을 갖췄는지를 실행 조건으로 확인해 작업·경로 제약에 반영하는 것이 적절하다는 구축자 의견 [의견] | 연계 대상: 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법(KS B 7317) [사실][^ref-314] |

승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어는 설비 제조사·설비 제어기 쪽에 남고, ROP 는 어댑터를 통해 작업 요청·점유 예약·상태 확인·완료 확인을 맡는 것으로 보인다. [추정][^ref-283][^ref-284][^ref-031] VDA 5050 3.0.0 은 주변 시스템과의 통신을 관제 최소 기능 목록에 넣지만 주변 설비 인터페이스 자체는 범위에서 제외한다. [사실][^ref-031]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 위의 어댑터 구조와 VDA 5050 범위 규정에 비추어, 이종 제조사를 연결하는 ROP 라면 설비 쪽 제어를 직접 만들기보다 설비별 어댑터의 요청·상태 형식과 실행 확인을 담당하는 쪽이 원문의 경계와 맞는다는 것이 이 위키 구축자의 의견이다. [의견]

건물 설비의 비상 복귀도 같은 경계로 나뉜다. 5절 기타 현장 사례처럼 화재 경보 뒤 승강기의 수동 모드 복귀와 PLC 재시작에는 사람의 개입이 필요할 수 있으며, 이는 연계 대상인 설비 쪽 조치다. [추정] 벤더 주장[^ref-1440] 그래서 ROP 장애 복구와 건물 설비의 비상 복귀를 따로 시험하고, 화재 뒤 설비 재시작 같은 수동 복귀의 책임자를 정해 두는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1440]

출입통제에서는 문 열기 요청과 통행 권한 승인을 나눠 본다. Dormakaba 문 어댑터 README 는 문 클라우드 API 접근 자격증명을 Dormakaba 가 제공한다고 안내한다. [사실][^ref-1439] BACnet 출입통제 백서가 인증과 권한 검사를 구분한다는 내용은 검증에서 재현하지 못한 추정 근거다. [추정][^ref-1443] 이에 비추어 자동문 연동에서는 문 열기 API 자격증명과 별도로 로봇의 공간별 출입 권한과 비상 우선권을 누가 정하는지 확인해야 한다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1439]

물리 인계에서는 ROP 가 준비·허가·이송·완료의 의미를 현장 PLC·작업대와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 것이 좋다는 것이 이 위키 구축자의 의견이다. SEMI E84 같은 업종 규격은 인계 신호 구조의 참고일 뿐 다른 현장에 대한 적합성을 검증한 근거가 아니다. [의견][^ref-202]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

설비 연동은 로봇 연동, 공용 자원 계획, 안전 제약과 함께 움직인다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area22-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 [열린 질문](../../open-questions.md) 목록에 함께 오른다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area22-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-10-11 · 갱신 · [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) — 차등 갱신: 3절 공유 승강기 지연 교차 확인·KS B 7317 개정 이력·국토부 연구개발 2차 보도; 4절 AGV 모드와 세션 수락; 5절 기타(도서관)·병원·상업 시설 사례 추가; 6절 승강기 감독·작업대 완료 판정·제조사 어댑터; 7절 표준 보강 표; 8절 연구 실험 조건 갱신; 9절 비상 복귀·출입통제 경계; 10절 연결 8건; 11절 부분 근거·새 질문 6건; 13절 각주 갱신. 2차 수정: 10절 구축자 의견 3건 태그 분리, 3절 f38 근거 문구 정정, 7·8·10·11절에 2026-09-25 주제 페이지 링크 복원, 11절 새 질문 문구를 열린 질문 갱신과 일치 (실행 2026-10-11-03)
- 2026-10-11 · 생성 · [22. 설비·건물 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area22-s6.md) — 자동 분리: 22. 설비·건물 시스템 연동 의 "6. 대표 접근법과 기술" 절(2,450자)을 옮겼다 (실행 2026-10-11-03)
- 2026-10-11 · 생성 · [22. 설비·건물 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area22-s11.md) — 자동 분리: 22. 설비·건물 시스템 연동 의 "11. 열린 질문" 절(2,065자)을 옮겼다 (실행 2026-10-11-03)
- 2026-10-11 · 생성 · [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area22-s7.md) — 자동 분리: 22. 설비·건물 시스템 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,902자)을 옮겼다 (실행 2026-10-11-03)
- 2026-10-11 · 생성 · [22. 설비·건물 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area22-s3.md) — 자동 분리: 22. 설비·건물 시스템 연동 의 "3. 왜 중요한가" 절(1,323자)을 옮겼다 (실행 2026-10-11-03)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-11
[^ref-163]: 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026-02-28, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-10-11
[^ref-202]: SEMI, E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface, 미확인, https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface, 접근일 2026-10-11
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-09-25
[^ref-314]: 국가기술표준원(e-나라표준인증·KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2025-05-09, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-10-11
[^ref-321]: Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots, 2025-02-28, https://doi.org/10.3390/electronics14050982, 접근일 2026-10-11
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11
[^ref-1435]: cwrx777; mxgrey (Open Robotics Discourse 아카이브), Lift session issues - Robot enter lift while lift is still in human mode (#513), 2024-08-21, https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679, 접근일 2026-10-11
[^ref-1439]: Open-RMF (open-rmf/door_adapter_dormakaba 저장소), door_adapter_dormakaba — README (commit 2cf76a6), 미확인, https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 접근일 2026-10-11
[^ref-1440]: HopeTechnik (RMF Systems Engineering Handbook), Lift and Doors Integration, 미확인, https://trl-rmf.github.io/website/content/lift-door-integration.html, 접근일 2026-10-11
[^ref-1443]: SSPC 135 LSS-WG; Isler, B. 외 (BACnet International), Physical Access Control with BACnet (BAC-09-08 White Paper), 2008-09-27, https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf, 접근일 2026-10-11
[^ref-1444]: NAVER LABS, NAVER’s ARC Goes to Japan, 2026-07-23, https://naverlabs.com/en/blogDetail?seq=10034507, 접근일 2026-10-11
