---
title: "K. 플랫폼 아키텍처·인프라"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-004, ref-009, ref-031, ref-045, ref-051, ref-105, ref-148, ref-251, ref-282, ref-287, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-405, ref-493, ref-762, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120]
---

[홈](../../index.md) › K. 플랫폼 아키텍처·인프라

# K. 플랫폼 아키텍처·인프라

## 핵심 질문

플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

## 개요

플랫폼의 구조, 클라우드·현장 서버·로봇의 역할 분담, 네트워크·가용성·다현장, 데이터·관측성·배포·비용. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **41. 플랫폼 아키텍처·외부 API** | 기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK | 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? | [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) | published |
| **42. 분산 시스템·통신·컴퓨팅 구조** | 현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? | [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) | published |
| **43. 데이터·관측성·배포** | 데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 | 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? | [43. 데이터·관측성·배포](data-observability-and-deployment.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

플랫폼 구조는 현장의 네트워크 조건을 전제로 정해야 한다. **연결이 끊겼을 때 현장에서 계속할 수 있는 범위**가 구조 선택의 기준이 된다. [분류원문]

## 다른 대분류와의 연결

K. 플랫폼 아키텍처·인프라의 세 세부영역, 곧 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)는 다른 대분류의 기능이 어디에서 돌고, 연결이 끊겼을 때 무엇을 이어 가며, 무엇을 기록으로 남기는지를 정한다. 아래 연결은 게시된 세부영역 페이지와 다른 대분류 페이지에 실린 검증된 주장을 대분류별로 묶은 것이다. 근거는 모두 단일 출처이거나 기존 페이지의 재인용이며, 교차 확인된 것은 없다. 두 영역을 잇는 해석은 추정 태그로 표시했고, 제조사·판매사 자료에 기댄 내용에는 벤더 주장을 함께 적었다.

### A. 기획·사업

[A. 기획·사업](../planning-and-business/index.md)과는 비용과 업체 전략에서 만난다.

- **43. 데이터·관측성·배포 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)**: FinOps Foundation 은 클라우드 비용 관리를 알리기(Inform)·최적화(Optimize)·운영(Operate) 단계가 되풀이되는 주기로 설명한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1041] 같은 재단은 2025-06-03 클라우드 청구 데이터 명세 FOCUS 1.2 를 발표하면서 서비스형 소프트웨어(Software as a Service, SaaS)·서비스형 플랫폼(Platform as a Service, PaaS) 청구 데이터 지원과 청구서 대사(invoice reconciliation)를 더했다고 밝혔다(발표 글 기준이며 명세 본문은 미열람). [사실][^ref-1042] 43. 데이터·관측성·배포가 계측·배분하는 클라우드·언어 모델 호출 비용은 3. 경제성·조달·사업 모델의 총소유비용 산정과 과금 단위 결정의 입력이 될 것으로 보이나, 다중 제조사 오케스트레이션 플랫폼의 과금 단위를 공개한 자료는 확인되지 않았다(oq-267). [추정][^ref-1041][^ref-1042][^ref-1037]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 3. 경제성·조달·사업 모델**: FreightWaves 기사는 하이브리드 창고 관리 시스템(Warehouse Management System, WMS) 판매사의 조사를 인용해 창고 운영 중단 비용이 시간당 최대 10만 달러라고 전하며, 이는 연결 단절이 물류창고 투자 효과 판단에 들어갈 위험 비용이 될 수 있음을 보여 준다(기사 발행일·조사 방법·표본·하한 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-309]
- **41. 플랫폼 아키텍처·외부 API ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md)**: 업체 사례로, 네이버는 제2사옥 1784(기타 현장, 기업 사옥)에서 로봇 100여 대를 클라우드로 제어하고 로봇에는 연산·판단을 싣지 않는 구조를 쓴다고 밝힌다(발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1023]

### B. 로봇 온톨로지

[B. 로봇 온톨로지](../robot-ontology/index.md)와는 어댑터 설정과 버전 기록에서 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md)**: Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-105] 41. 플랫폼 아키텍처·외부 API가 ROP 직접 범위로 두는 제조사 어댑터 계층은 6. 온톨로지 기반 시스템·로봇 연동이 능력 모델에서 만드는 어댑터 설정·명령 매핑 초안이 반영되는 자리가 될 것으로 보이나, 그렇게 초안을 만든 공개 사례는 확인되지 않았다. [추정][^ref-004][^ref-105]
- **43. 데이터·관측성·배포 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md)**: 43. 데이터·관측성·배포가 남기는 소프트웨어·펌웨어 배포 버전 기록은 7. 온톨로지 검증·변경 관리가 능력 정의를 다시 검증할 계기를 알려 주는 입력이 될 것으로 보이나, 두 기록을 잇는 공개 사례는 확인하지 못했다. [추정][^ref-1040]

### C. 채팅 기반 구성·운영

[C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)과는 대화가 부르는 외부 API 와 언어 모델 호출 계측에서 만난다. 분류 원문 4장 주석은 업무 지시를 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링의 기능을 대화로 쓰게 하는 것으로 보므로, 아래 12. 채팅으로 업무 지시·오케스트레이션 연결은 G. 계획·최적화 항목과 함께 읽는다.

- **41. 플랫폼 아키텍처·외부 API ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)**: Open Robotics 상호운용 SIG 의 2026-07-02 발표 안내문(2026-06-25 게시)은 Nayantra 를 소개했다. Nayantra 는 Open-RMF REST 응용 프로그래밍 인터페이스(Application Programming Interface, API)를 언어 모델이 호출하는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와, 평이한 영어 지시를 RMF 임무로 바꾸는 에이전트로 이루어진다(안내문 기준이며 발표 내용 자체는 미열람, 시연은 Isaac Sim 창고 시뮬레이션). [사실][^ref-854]
- **41. 플랫폼 아키텍처·외부 API ↔ [13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md)**: 대화형 기능이 플랫폼 외부 API 를 도구로 부르면, API 의 인증·권한 범위가 13. 대화형 기능의 신뢰·기반이 다루는 사용자별 대화 권한의 실제 집행 지점이 될 것으로 보인다(아래 N. 보안·개인정보 항목과 함께 읽는다). [추정][^ref-854][^ref-762]
- **43. 데이터·관측성·배포 ↔ 13. 대화형 기능의 신뢰·기반**: OpenTelemetry 생성형 AI 의미 규약 저장소는 언어 모델 클라이언트 호출의 토큰 사용량 지표를 정의하며, 이 규약은 아직 개발(Development) 단계다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1037] 13. 대화형 기능의 신뢰·기반이 언어 모델 공급자를 고르고 바꾸려면 43. 데이터·관측성·배포가 호출별 토큰·비용·지연을 계측해야 할 것으로 보이나, 계측 지표 이름은 안정 판이 나오지 않아 고정되지 않았다(oq-212). [추정][^ref-1037][^ref-1043]

### D. 공간·지도 모델

- **41. 플랫폼 아키텍처·외부 API ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)** ([D. 공간·지도 모델](../space-and-map-model/index.md)): 네이버는 ARC eye 가 클라우드에서 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정한다고 밝히지만, 위치 모델을 클라우드에 둔 이 설계에서 연결이 끊기면 로봇이 어디까지 동작하는지는 공개되지 않았다(기타 현장, 기업 사옥, oq-206). [추정] 벤더 주장[^ref-1023] 위치 추정 자체는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 사례는 제품 전략 사례로만 읽고 ROP 직접 범위의 근거로 쓰지 않는다.

### E. 사물·사람·실시간 상태

[E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)와의 연결은 지금의 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이며, I. 설계·시뮬레이션 항목의 미래 실험·지난 기록 재현과 구분한다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: 통신 계층에는 상태가 오래되었음을 알리는 장치가 있으며, ROS 2 서비스 품질(Quality of Service, QoS)의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 이 메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)의 유언 메시지(Last Will)로 보내는 연결 끊김 통지가 그 예다(세 출처는 각각 한 장치만 다루므로 서로 교차 확인한 것이 아니다, 2026-10-09 확인). [사실][^ref-282][^ref-287][^ref-031] Open-RMF 로봇 상태는 밀리초 단위 유닉스 시각(unix_millis_time)을, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담아 시각 표현이 서로 다르며, 공통 시간축 변환과 허용 시계 오차를 정한 자료는 확인되지 않았다(oq-035). [사실][^ref-148][^ref-051]
- **43. 데이터·관측성·배포 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)·18. 실시간 세계 상태·데이터 일관성**: EPCIS 2.0 온톨로지(2021-09-30)는 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분하므로, 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-045]

### F. 연동

[F. 연동](../integration/index.md)과는 통신 전제, 어댑터 구조, API 명세, 설비·업무 시스템 기록에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제해 주문·상태 토픽에 재전송 없는 MQTT QoS 0 을 쓴다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- **41. 플랫폼 아키텍처·외부 API ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고하고, 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004][^ref-251] 두 자료는 같은 기관 문서라 교차 확인은 아니며, 제어 수준별 교통 성능 차이는 미확인이다(oq-032).
- **41. 플랫폼 아키텍처·외부 API ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: OpenAPI 명세 3.1.0(2021-02-15)은 HTTP API 를 언어와 무관하게 기술하는 표준 인터페이스 기술 형식이고, AsyncAPI 명세 3.1.0(발행일 미확인)은 메시지 기반 API 를 기술하는 형식이다. [사실][^ref-1025][^ref-1024] 플랫폼 외부 API 를 두 형식으로 기계가 읽게 기술하면 21. 상호운용 표준·적합성이 다루는 연동 규격 적합성 시험의 기준 문서가 될 수 있을 것으로 보이나, 국내에 통합관제 플랫폼 외부 API 를 정한 TTA·KS 표준이 있는지는 확인되지 않았다(oq-209). [추정][^ref-1025][^ref-1024] 이런 기술 문서를 실제 적합성 시험에 쓴 공개 도구·절차가 있는지는 oq-209 와 함께 새 열린 질문으로 올렸다.
- **43. 데이터·관측성·배포 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: 고려대학교 구로병원 약품 배송 로봇 실증(병원)은 승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지를 함께 모아 실패 원인을 분석했다(2026-03-31 게재). [사실][^ref-943] 승강기 통신 로그를 만드는 일은 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이고, ROP 몫은 그 기록의 수집·결합이다.
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: 물류창고에서 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있을 것으로 보이나, 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다(물류센터 운영 기준 미확인, oq-038). [추정][^ref-031][^ref-300][^ref-310] 새 주문과 재고 확정은 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이고, ROP 는 받은 요청을 실행하고 결과를 반영하는 쪽을 맡는다.
- **41. 플랫폼 아키텍처·외부 API ↔ 23. 업무 시스템 연동**: Locus Robotics 는 LocusONE 이 WMS 주문을 API 로 받아 로봇 작업으로 내리고 피킹 완료 확인을 WMS 로 즉시 회신한다고 밝힌다(물류창고, 흐름 단계 피킹, 발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1030] 주문 최적화 판단은 상위 업무 시스템 경계의 WMS·로봇 공급사 몫이고, ROP 는 연동 인터페이스만 다룬다.

### G. 계획·최적화

[G. 계획·최적화](../planning-and-optimization/index.md)와는 배정·교통 계산을 어디에 두는지에서 만난다. 위 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션이 부르는 엔진도 여기의 25. 작업 배정 — MRTA와 [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)이다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: Lott·Honary(2026-09 프리프린트, 초록 기준)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 같은 통신 저하 조건에서 비교했다. [사실][^ref-493] 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보이나, 통신이 나빠질 때 중앙 방식과 분산 방식 사이를 언제 바꿀지 정한 물류센터 기준은 확인되지 않았다(oq-083). [추정][^ref-493][^ref-401]
- **41. 플랫폼 아키텍처·외부 API·42. 분산 시스템·통신·컴퓨팅 구조 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: Open-RMF 교통 관리는 플릿 어댑터가 예상 경로를 중앙 교통 스케줄에 보고하는 구조이므로, 중앙 스케줄을 현장 서버와 클라우드 가운데 어디에 두는지가 단절 때 교통 조율을 계속할 수 있는지를 좌우할 것으로 보인다(실측 자료 없음). [추정][^ref-004]

### H. 실행·협업·예외 복구

[H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)와는 단절·재시작 뒤 일을 어떻게 이어 가는지에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-300]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 은 주문·상태를 QoS 0 으로 보내고 상태를 사건 발생 시와 최대 30초 간격으로 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 오기를 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신해야 할 것으로 보인다(VDA 5050 이 MQTT 5.0 세션 만료를 어떻게 쓰는지는 미확인). [추정][^ref-031][^ref-306]
- **43. 데이터·관측성·배포 ↔ 32. 예외 복구·재계획·업무 연속성**: Zhang·Yu·Westerlund(Sensors, 2025-08-14)는 Kubernetes 컨테이너 자동 재시작으로 ROS 2 다중 로봇 시스템이 장애 중에도 초광대역(Ultra-Wideband, UWB) 기반 상대 위치 정확도를 유지했다고 보고했으며, 이는 현장 적용 사례가 아니라 실험실 결과다. [사실][^ref-1039] Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하지만, 이번 확인에서는 이슈 원문을 다시 열지 못해 이슈가 언급한 복구 기능 제안의 내용과 현재 배포판 반영 여부를 재확인하지 못했다(oq-048). [추정][^ref-374]
- **41. 플랫폼 아키텍처·외부 API ↔ 32. 예외 복구·재계획·업무 연속성**: FogROS2-FT(IROS 2024, 초록 기준)는 클라우드 로보틱스의 장애 허용을 다루며, 독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다. [사실][^ref-1031] 대상이 상태 비저장 서비스이므로, 이 방식을 진행 중인 작업 상태를 보존하는 근거로 읽지 않는다. 플랫폼 서비스를 복제하거나 자동 재시작하면서 진행 중인 작업 상태를 잃지 않은 공개 사례가 있는지는 새 열린 질문으로 올렸고, 어댑터 복구의 배포판 반영(oq-048)·무중단 순차 배포(oq-213)와 함께 본다.

### I. 설계·시뮬레이션

[I. 설계·시뮬레이션](../design-and-simulation/index.md)과의 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 지난 기록을 재현하는 36. 가상 시운전·실제 상황 재현으로 나뉜다. 위 E. 사물·사람·실시간 상태의 현재 상태 표현과 함께 셋을 디지털 트윈이라는 한 이름으로 묶지 않는다.

- **43. 데이터·관측성·배포 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Ocado 는 교통 관리·오케스트레이션 알고리즘 변경을 실제 창고(물류창고)에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 43. 데이터·관측성·배포 쪽에서는 배포 전 검증의 근거로만 쓰고, 시뮬레이션 자체는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용으로 둔다.
- **43. 데이터·관측성·배포 ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md)**: ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 의 기본 저장 형식은 MCAP 이고, rosbag2 는 재생 속도 조절, /clock 발행, 여러 백 파일을 기록 시각순으로 동시에 재생하는 기능을 지원한다(두 출처는 서로 다른 내용을 말하므로 교차 확인이 아니다). [사실][^ref-1034][^ref-831] 43. 데이터·관측성·배포가 정하는 기록 형식과 보존 기간이 36. 가상 시운전·실제 상황 재현이 재현에 쓸 수 있는 실제 기록의 범위를 정할 것으로 보이며, 이 연결은 지난 기록을 다루는 것이라 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과는 구분된다(oq-211). [추정][^ref-1034][^ref-831]

### J. 현장 운영·관제

[J. 현장 운영·관제](../field-operations-and-monitoring/index.md)와는 실행 기록 저장과 원인 분석용 추적에서 만난다.

- **43. 데이터·관측성·배포 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)**: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하므로, 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **43. 데이터·관측성·배포 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: ros2_tracing(IEEE RA-L, 2022-07)은 LTTng 기반 저부하 추적기로 ROS 2 실행 정보를 모으며, 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가가 평균 0.0033 ms 였다고 보고했다(저자 실험값, 독립 재현 미확인). [사실][^ref-1032] ros2probe(2026-06 프리프린트)는 관찰 도구가 관찰 대상을 교란하는 문제를 커널 선택 관찰로 줄여, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033] 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모으므로, 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(공개 사례 미확인, oq-210). [추정][^ref-1036][^ref-1032]

### L. AI·학습 기술

[L. AI·학습 기술](../ai-and-learning/index.md)과는 언어 모델·계산을 어디에서 돌리는지에서 만난다. 적용 대상은 이 대분류의 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)다.

- **42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포 ↔ [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md)**: Bruno·Sim·Hagiwara(2026-09 프리프린트)는 범용 서비스 로봇의 대규모 언어 모델(Large Language Model, LLM) 연쇄 기반 작업 계획에서 로컬 모델과 클라우드 모델을 비교했고 비교의 동기는 클라우드 API 비용과 지연이었으나, 실험은 계획 성공률만 측정했고 비용·지연 자체는 측정하지 않았다. [사실][^ref-1043]
- **41. 플랫폼 아키텍처·외부 API ↔ 44. 로봇 기반 모델·언어 모델 계획**: FogROS2(2022-05)는 ROS 2 로봇의 계산 부담이 큰 작업을 클라우드·포그로 옮겨 실행하는 플랫폼이다. [사실][^ref-304] 로봇 내부 기능의 실행 위치 선택은 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 연구는 계산 배치 선택지의 연구 근거로만 쓴다.

### M. 안전

[M. 안전](../safety/index.md)은 통신 계층과 안전 기능의 구분, 사고 조사용 기록에서 이 대분류와 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: VDA 5050 은 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 그래서 관제 통신 계층과 48. 안전·위험 관리가 다루는 안전 기능은 구분해 다룬다.
- **43. 데이터·관측성·배포 ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)**: Winfield 외(2022-05-13)의 윤리적 블랙박스 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 기록하는 모듈을 제안하며, 단일 로봇을 대상으로 하고 플릿·플랫폼 수준 기록은 다루지 않는다. [사실][^ref-1120] 사고 조사에 쓸 플랫폼 수준 실행 기록에는 43. 데이터·관측성·배포 쪽의 보존 기간·무결성 관리가 필요할 것으로 보이나, 로봇 플랫폼 기록의 보존 기간을 정한 기준은 개인정보 접속기록 규정 밖에서는 확인되지 않았다(oq-211). [추정][^ref-1120][^ref-766]

### N. 보안·개인정보

[N. 보안·개인정보](../security-and-privacy/index.md)는 외부 API 인증·통신 보호·접속기록에서 이 대분류와 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: Open-RMF API 서버(rmf-server)는 OpenID Connect(OIDC) 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정하며, 관리자는 모든 그룹에서 모든 동작을 할 수 있고 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 51. 인증·권한·격리·[52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)**: ROS 2 는 데이터 분산 서비스(Data Distribution Service, DDS) 보안 규격의 인증(공개 키 기반 구조, PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓰고, Open-RMF 문서는 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고 웹 대시보드에는 전송 계층 보안(Transport Layer Security, TLS)·OIDC 인증을 더한다고 설명한다(두 자료는 서로 다른 계층을 설명하므로 교차 확인이 아니다). [사실][^ref-009][^ref-405]
- **43. 데이터·관측성·배포 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)**: 개인정보보호위원회 고시 「개인정보의 안전성 확보조치 기준」은 접속기록의 보관과 점검에 관한 조항을 둔다(2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인, oq-214). [사실][^ref-766]

### O. 검증·도입·수명주기

- **43. 데이터·관측성·배포 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)** ([O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)): Mender 는 임베디드 리눅스 장치용 오픈소스 무선(Over-the-Air, OTA) 업데이트 도구로, 이미지 기반 A/B 업데이트와 실패 시 롤백을 지원한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1040] 로봇 운영체제·펌웨어의 무선 업데이트 자체는 연계 대상이다. 43. 데이터·관측성·배포의 배포·롤백 자동화가 57. 자산·소프트웨어 수명주기 관리의 버전 관리와 맞물릴 것으로 보이나, 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구는 확인되지 않았다(oq-213). [추정][^ref-1040][^ref-1039]

### P. 거버넌스·법규·사회

- **43. 데이터·관측성·배포 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)** ([P. 거버넌스·법규·사회](../governance-law-and-society/index.md)): 연계 대상: 접속기록 보관 같은 법적 의무의 해석과 적용 판단은 59. 법·규제·보험·라이선스와 운영 사업자의 몫으로 보이고, ROP 는 그 기준에 맞춰 기록을 수집·보존·점검하는 기능을 제공하는 쪽으로 보인다(근거 고시는 2023-09-22 시행 판 제8조 기준, 현행 조문 미확인, oq-214). [추정][^ref-766]

P. 거버넌스·법규·사회와의 연결은 현재 위의 연계 대상 추정 하나뿐이다.

### Q. 현장 유형별 적용

[Q. 현장 유형별 적용](../site-type-applications/index.md)에는 현장마다 다른 요구를 모으고, 모든 현장에 공통인 구조 선택은 이 대분류에 둔다. 아래는 위 연결의 근거가 된 사례를 현장 유형별로 다시 묶은 것이다.

- **병원 — [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 창이종합병원 CHART 의 공공 의료기관용 로봇 미들웨어 RoMi-H 는 기계(하드웨어 추상화)·제어(항법·위치 추정)·중앙(플릿 관리, 로봇–기반 시설 통신)·통합(모바일·웹 앱·ICT 시스템용 API) 네 영역이 역할을 나누는 구조이며 OMG DDS 를 쓴다(2019-10-31 ROSCon 2019 에서 공식 출범). [사실][^ref-937] 이는 특정 병원의 배치 결과가 아니라 미들웨어 구조다.
- **병원 — 63. 병원·의료 ↔ 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포**: 고려대학교 구로병원 약품 배송 로봇 실증(2025-06, 비응급 임무 122건)의 실패 14건은 승강기 막힘 8건, 복도 주행 4건, 통신 오류 2건이었다(2026-03-31 게재). [사실][^ref-943] 논문이 밝힌 전체 성공률과 이 건수가 맞지 않는 문제는 oq-215 에 있고, 이 실증의 로그 결합은 위 F. 연동 항목에 있다.
- **제조 공장 — [62. 제조 공장](../site-type-applications/manufacturing-plant.md) ↔ 41. 플랫폼 아키텍처·외부 API**: Brorsson 외(2025-12, 초록 기준)는 기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 사내 물류 이동 로봇 기준 아키텍처를 제시하고, 대형 차량(heavy-vehicle) 제조 현장 실배치로 보였다. [사실][^ref-308] 처리량·시간·비용 수치는 확인하지 못했다.
- **물류창고 — [61. 물류창고](../site-type-applications/warehouse.md) ↔ 42. 분산 시스템·통신·컴퓨팅 구조**: CJ대한통운은 2023-04 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G 를 구축했다고 발표하며 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 발표 당시 로봇·설비 적용은 시범 뒤 확대 계획이었다. [추정] 벤더 주장[^ref-307] 무선망 구축은 ROP 가 소유하지 않는 통신 기반으로 연계 대상이다. 물류창고의 다른 근거는 위 A. 기획·사업(운영 중단 비용), F. 연동(단절 중 WMS 연동, 피킹 완료 회신), I. 설계·시뮬레이션(배포 전 시뮬레이션) 항목에 있다.
- **기타 — [67. 기타 현장](../site-type-applications/other-sites.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 기업 사옥 사례(네이버 1784)는 위 A. 기획·사업과 D. 공간·지도 모델 항목에 벤더 주장으로 있다.
- **상업 시설·가정·실외**: [64. 상업 시설](../site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../site-type-applications/home-and-apartment.md), [66. 실외](../site-type-applications/outdoor.md)와 이 대분류를 잇는 근거는 이번 정리에 없다.

### 아직 다루지 않은 연결

이번 정리의 근거가 다루지 않은 세부영역은 다음과 같다. 연결이 없다는 뜻이 아니라 아직 근거를 모으지 않았다는 뜻이다.

- A. 기획·사업: 2. 사용 사례·요구·책임 범위
- B. 로봇 온톨로지: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현
- C. 채팅 기반 구성·운영: 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현
- D. 공간·지도 모델: 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리
- E. 사물·사람·실시간 상태: 19. 사람·보행자 모델
- G. 계획·최적화: 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화
- H. 실행·협업·예외 복구: 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업
- I. 설계·시뮬레이션: 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계
- J. 현장 운영·관제: 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구
- L. AI·학습 기술: 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영
- M. 안전: 49. 사람 근접 안전
- O. 검증·도입·수명주기: 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 56. 운영 이관·확대·교육
- P. 거버넌스·법규·사회: 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성
- Q. 현장 유형별 적용: 64. 상업 시설, 65. 가정·공동주택, 66. 실외

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-09
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-09 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-10-09 (원문 미열람)
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-10-09 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-10-09 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-10-09 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-10-09 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-10-09 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-10-09 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-10-09 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-10-09 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-10-09
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-10-09 (원문 미열람)
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-766]: 국가법령정보센터(개인정보보호위원회 고시), 개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-10-09 (원문 미열람)
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-937]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-10-09 (원문 미열람)
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-10-09 (원문 미열람)
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-10-09 (원문 미열람)
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09 (원문 미열람)
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-10-09 (원문 미열람)
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-10-09 (원문 미열람)
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09 (원문 미열람)
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09 (원문 미열람)
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-10-09 (원문 미열람)
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-10-09 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-10-09 (원문 미열람)
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more, 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-10-09 (원문 미열람)
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-10-09 (원문 미열람)
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09 (원문 미열람)

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 72건이다(논문 16건 · 기사·보고서 6건 · 업체 발표 10건 · 표준·오픈소스·기관 자료 40건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-493](../../references/ref-493.md) — Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation (발행 2026-09)
- [ref-1043](../../references/ref-1043.md) — Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots (발행 2026-09)
- [ref-1033](../../references/ref-1033.md) — Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware (발행 2026-06)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-308](../../references/ref-308.md) — Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives (발행 2025-12)
- [ref-1039](../../references/ref-1039.md) — Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning (발행 2025-08-14)
- [ref-1031](../../references/ref-1031.md) — Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics (발행 2024-12)
- [ref-1328](../../references/ref-1328.md) — Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS), A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications (발행 2024)
- [ref-1327](../../references/ref-1327.md) — Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv), Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems (발행 2023-03)
- [ref-1032](../../references/ref-1032.md) — Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 (발행 2022-07)
- 그 밖에 6건

**기사·보고서**

- [ref-1026](../../references/ref-1026.md) — 뉴스핌, 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 (발행 2026-05-13)
- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)
- [ref-1321](../../references/ref-1321.md) — 바이라인네트워크 (곽중희), 개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환” (발행 2025-10-31)
- [ref-309](../../references/ref-309.md) — FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount (발행 미확인)
- [ref-1322](../../references/ref-1322.md) — Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog), EU Digital Omnibus on AI Enters into Force (발행 미확인)
- [ref-1041](../../references/ref-1041.md) — FinOps Foundation, FinOps Phases (발행 미확인)

**업체 발표**

- [ref-301](../../references/ref-301.md) — Microsoft, Operate Azure IoT Edge devices offline (발행 2026-03-02)
- [ref-1044](../../references/ref-1044.md) — Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale (발행 2025-06-04)
- [ref-227](../../references/ref-227.md) — Mobile Industrial Robots(MiR), MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 (발행 2025-01)
- [ref-307](../../references/ref-307.md) — CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 (발행 2023-04)
- [ref-1035](../../references/ref-1035.md) — Foxglove, MCAP as the ROS 2 Default Bag Format (발행 2022-12-22)
- [ref-1324](../../references/ref-1324.md) — Northern.tech (Mender blog, Farshad Tavakoli), Managing fleets of connected devices with Phased Rollout (발행 2020-01-28)
- [ref-774](../../references/ref-774.md) — Mobile Industrial Robots(MiR), MiR Fleet (발행 미확인)
- [ref-1030](../../references/ref-1030.md) — Locus Robotics, Seamless Integrations with LocusOne Robotics (발행 미확인)
- [ref-1029](../../references/ref-1029.md) — InOrbit, Contents — InOrbit Developer Portal (발행 미확인)
- [ref-1023](../../references/ref-1023.md) — NAVER Corp., 로보틱스 l NAVER Corp. (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-1042](../../references/ref-1042.md) — FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 2025-06-03)
- [ref-1314](../../references/ref-1314.md) — European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 26: Obligations of deployers of high-risk AI systems (발행 2024-07-12)
- [ref-1313](../../references/ref-1313.md) — European Commission, AI Act Service Desk (Regulation (EU) 2024/1689), Article 19: Automatically generated logs (발행 2024-07-12)
- [ref-1034](../../references/ref-1034.md) — Open Robotics (ROS 2 Documentation), Iron Irwini (iron) (발행 2023-05-23)
- [ref-1325](../../references/ref-1325.md) — W3C, Trace Context (발행 2021-11-23)
- [ref-045](../../references/ref-045.md) — GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) (발행 2021-09-30)
- [ref-1025](../../references/ref-1025.md) — OpenAPI Initiative, OpenAPI Specification v3.1.0 (발행 2021-02-15)
- [ref-306](../../references/ref-306.md) — OASIS, MQTT Version 5.0 (발행 2019-03)
- [ref-303](../../references/ref-303.md) — NIST, NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model (발행 2018-03)
- 그 밖에 30건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 5절 병원 사례 수행 자원·제약 행 채움과 성공률 분모 재확인, 6·7·8·9·10·11절에 2026-10-09 갱신 소절(Mender 상태 스크립트·단계적 배포(벤더 주장)·배포 시점 판단, W3C Trace Context·메시지 흐름 인과 분석, OpenTelemetry 상태·생성형 AI 토큰 지표 재확인, 개인정보 고시 개정 보도·EU AI Act 로그 보관 연계, 열린 질문 부분 근거와 새 질문 3건), 13절 각주 갱신. 2차 수정: 6·7·10·11절 갱신 소절에 2026-09-30 주제 페이지 링크 복원, 7절 기준일 문구 명확화 (실행 2026-10-09-19)
- 2026-10-09 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,358자)을 옮겼다 (실행 2026-10-09-19)
- 2026-10-09 · 생성 · [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area43-s7.md) — 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,654자)을 옮겼다 (실행 2026-10-09-19)
- 2026-10-09 · 생성 · [43. 데이터·관측성·배포 — 열린 질문](../../topics/2026/2026-10-09-area43-s11.md) — 자동 분리: 43. 데이터·관측성·배포 의 "11. 열린 질문" 절(1,457자)을 옮겼다 (실행 2026-10-09-19)
- 2026-10-09 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,426자)을 옮겼다 (실행 2026-10-09-19)
<!-- auto:category-recent:end -->
