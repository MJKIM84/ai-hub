# 리서치 브리프 2026-09-25-13

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-13 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 1. 주문·업무 시스템 연계 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문은 oq-002 1건, 정정 요청 없음
- 이전 실행 2026-09-25-08 이 같은 영역을 조사했으나 그 출처(ref-138~ref-187 제안분)가 참고문헌 목록에 없어 게시되지 않은 것으로 보여, 원문을 다시 열어 새 id 로 재조사함

## 조사 질문

1. 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [분류원문]
2. 로봇 관제 인터페이스(VDA 5050, Open-RMF)는 진행 중인 작업의 갱신·일시정지·취소·되감기를 어떤 메시지와 상태로 처리하며, 무엇이 바뀌지 않는가? (섹션 5·6·7 겨냥)
3. 상위 업무·실행 시스템과 하위 실행 계층 사이의 작업 요청·변경·취소는 ISA-95 계열 표준(B2MML 거래 동사, OPC UA for ISA-95 Job Control 메서드)에서 어떻게 표현되는가? (섹션 4·7 겨냥)
4. SCOR 같은 공급망 참조 모델은 주문(Order)과 이행(Fulfill)을 어떻게 나누며, 이는 ERP·WMS·TMS 와 ROP 사이 경계에 어떤 기준을 주는가? (섹션 3·9 겨냥)
5. 동적으로 도착하는 주문·긴급 주문을 진행 중인 피킹 사이클에 끼워 넣는 개입형(interventionist) 전략과 웨이브·웨이브리스 출고 지시 연구는 무엇을 보여 주는가? (섹션 6·8 겨냥)
6. 상위 시스템(WMS·MES·ERP)과 다제조사 로봇 관제를 연동한 연구·국내 실증 사례가 있는가? (섹션 5·8, 한국 자료 우선, oq-002 관련)
7. 주문·업무 시스템 연계에서 ROP가 직접 맡을 부분과 상위 업무 시스템·로봇 제조사에 맡길 부분의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 관제(fleet control)와 이동로봇 사이의 통신만 다루며, 주변 설비·외부 IT 시스템 같은 다른 통신 인터페이스와 교통 관리 로직은 범위 밖으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 에서 관제는 진행 중인 주문을 같은 orderId 에 orderUpdateId 를 올린 주문 갱신으로 바꿀 수 있지만, 이미 공개된 base 는 바꿀 수 없고(로봇이 이미 실행했다고 가정) 공개되지 않은 horizon 만 수정·삭제하거나 base 를 다르게 연장할 수 있다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 제약 | — |
| f3 | [추정] | 이번에 연 VDA 5050 3.0.0 명세에서는 주문(order) 메시지의 우선순위 필드를 찾지 못해, 로봇 인터페이스 수준에서 주문 간 우선순위를 표현하는 수단은 확인되지 않았다. | ref-031 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f4 | [사실] | VDA 5050 3.0.0 에서 이동로봇은 이전 주문의 마지막 노드와 모든 동작을 마쳤거나 cancelOrder 를 끝내 유휴 상태일 때만 다른 orderId 의 새 주문을 받으며, 진행 중에 다른 orderId 가 오면 OTHER_ORDER_ACTIVE 로 거부한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f5 | [사실] | VDA 5050 3.0.0 의 즉시 동작 cancelOrder 를 받으면 이동로봇은 가능한 한 빨리 멈추고 예정·실행 중 동작을 FAILED 로 보고하되, 취소할 수 없는 동작(cancelAllowed=false)은 끝날 때까지 RUNNING 으로 계속하며 그 뒤에 cancelOrder 가 FINISHED 가 된다. | ref-031 | 아니오 | medium | 2026-09-25 | 피킹 / 예외·성과 | — |
| f6 | [사실] | VDA 5050 3.0.0 의 즉시 동작 startPause 는 다음 노드 도달을 기다리지 않고 자동 주행을 멈추고 일시정지 가능한 동작만 멈추며, stopPause 는 주행과 동작을 재개한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 작업 요청 스키마(task_request)는 category·description 을 필수로 두고, 플릿이 지원하는 우선순위 스키마에 맞춰야 하는 priority, 최早 시작 시각, 요청 시각, 요청자, 라벨, 입찰할 수 있는 플릿 이름을 선택 필드로 둔다. | ref-138 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [사실] | Open-RMF API 는 이미 요청한 작업에 대해 task_id 로 지정하는 취소 요청(cancel_task_request), 중단 요청(interrupt_task_request), 지정한 단계의 처음부터 다시 시작시키는 되감기 요청(rewind_task_request, phase_id 필수)을 별도 스키마로 둔다. | ref-182, ref-183, ref-184 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF 작업 상태 스키마(task_state)는 상태 값 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 와 함께 배정 로봇, 최초·현재 예상 소요 시간, 완료·진행·대기 단계, 중단(interruptions)·취소(cancellation)·강제 종료(killed) 요청 정보를 담는다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f10 | [사실] | Open-RMF 공식 문서는 작업을 /task_api_requests 토픽의 ApiRequest 로 보내며, dispatch_task_request 는 가장 적합한 플릿에, robot_task_request 는 특정 로봇에 작업을 맡기고, 별도 요청으로 작업 취소나 단계 건너뛰기를 할 수 있다고 안내한다. | ref-110 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f11 | [사실] | MESA International 의 B2MML 거래 프로파일 스키마(판 0701, 2023, ANSI/ISA-95.00.02-2018·95.00.05-2018 기반)는 거래 동사로 NOTIFY, GET, PROCESS, CHANGE, CANCEL, CONFIRM, SYNC ADD, SYNC CHANGE, SYNC DELETE 와 확장용 Other 를 정의한다. | ref-185 | 아니오 | medium | 2023 | 시작 조건 | — |
| f12 | [사실] | OPC Foundation 공식 노드셋의 OPC UA for ISA-95 Job Control(판 2.0.0, 2024-01-31)은 작업 지시 처리에 Store, StoreAndStart, Start, RevokeStart, Pause, Resume, Stop, Update, Abort, Cancel, Clear 메서드와 작업 응답 조회 메서드를 두고, 작업 지시 데이터형과 작업 응답 데이터형을 함께 정의한다. | ref-186 | 아니오 | medium | 2024-01-31 | 시작 조건 | — |
| f13 | [사실] | OPC UA for ISA-95 Job Control 명세는 Pause 로 시작된 작업 지시를 Interrupted 로, Resume 으로 다시 Running 으로 바꾸고, Abort 는 실행 중·중단·시작 전(AllowedToStart, NotAllowedToStart) 작업 지시 모두에 쓸 수 있어 Aborted 로 바꾸며, Aborted·Ended 가 된 작업 지시는 Clear 로 지운다. | ref-187 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | ISA 는 2025년 ISA-95 Part 1(ANSI/ISA-95.00.01-2025, IEC 62264-1 Mod)을 개정 발행하며, 이 표준 계열이 물류 시스템과 제조 제어 시스템의 통합을 기술하고 개정판이 기업 영역과 제조·제어 영역의 경계를 더 분명히 한다고 밝혔다. | ref-002 | 아니오 | medium | 2025-04 | — | 원문 미열람 |
| f15 | [사실] | ASCM 의 SCOR Digital Standard 는 공급망을 Orchestrate, Plan, Order, Source, Transform, Fulfill, Return 프로세스로 나누고, Order 를 위치·결제·가격·이행 상태 등 주문 데이터를 포함한 고객 구매 활동으로, Fulfill 을 배송 일정·피킹·포장·출하 등 주문 이행 활동으로 정의한다. | ref-190 | 아니오 | medium | 2025 | 출하 / 시작 조건 | 원문 미열람 |
| f16 | [사실] | Yu·Srinivas(2025)는 작업자가 피킹하고 AMR 이 운반하는 협업 동적 주문 피킹 문제(CHR-DOPP)에서 새 주문을 진행 중인 AMR·작업자 피킹 사이클에 반영하는 개입형 전략 두 가지(AMR 가용성·근접도 기반 반응형, 진행 중 사이클 교란을 줄이는 조건부형)를 제안하고, 개입 없는 협업 시스템보다 평균 주문 완료 시간과 평균 총 지연이 크게 좋았다고 보고했다. | ref-188 | 아니오 | medium | 2025 | 피킹 / 예외·성과 | 원문 미열람 |
| f17 | [사실] | Lorenz 외(2025)는 주문이 동적으로 도착하는 온라인 주문 묶음·순서·경로 문제에서 새 주문이 올 때마다 현재 해를 다시 최적화하는 재최적화(Reopt)를 수동 카트와 로봇 카트 조건에서 분석하고, 확률적 가정 아래 거의 확실하게 점근적 최적임을 보였으며 개입형·비개입형 재최적화를 구분했다. | ref-120 | 아니오 | medium | 2025 | 피킹 / 시작 조건 | 원문 미열람 |
| f18 | [사실] | Gallien·Weber(2010)는 미국 온라인 소매업체 자료로 자동 분류기가 있는 창고의 웨이브리스(연속) 출고 지시 모델을 검증하고, 제안한 웨이브리스 정책이 모든 시나리오에서 가장 좋은 웨이브 정책 이상의 처리량을 더 낮은 교착(gridlock) 확률로 냈다고 보고했다. | ref-189 | 아니오 | medium | 2010 | 포장 / 시작 조건 | 원문 미열람 |
| f19 | [사실] | Applied Sciences(2025) 게재 사례 연구는 자동차 부문 GreenAuto 프로젝트에서 여러 제조사의 AGV·AMR 을 한 지도에서 감시·관리하는 플릿 관리 소프트웨어를 만들고, MES·ERP 에는 REST API 로 정형 데이터를, 로봇 이벤트는 MQTT 로 발행하는 구조를 두며 VDA 5050 연동은 향후 과제로 설계했다. | ref-191 | 아니오 | medium | 2025 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 2025년 1월 기사에 따르면 통합 물류 플랫폼 운영사 테크타카는 자사 WMS 와 플로틱의 오더 피킹용 자율주행로봇 30대를 연동하는 자동화 모델을 남이천 물류센터에서 실증하는 협력을 발표했다. | ref-192 | 아니오 | low | 2025-01 | 피킹 / 수행 자원 | 원문 미열람 |
| f21 | [추정] | 확인한 로봇 인터페이스에서 진행 중 작업의 우선순위를 바꾸는 수단은 요청 시점 우선순위 지정(Open-RMF), 공개되지 않은 경로의 주문 갱신(VDA 5050), 일시정지·중단, 취소 후 재지시, 단계 되감기 정도로 보여, 출고 우선순위가 바뀔 때 어떤 작업을 끊고 무엇을 먼저 할지 정하는 규칙은 ROP 쪽 작업 대기열·재계획 로직이 맡아야 할 것으로 보인다. | ref-031, ref-138, ref-182, ref-183, ref-184 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f22 | [추정] | 상위 시스템의 변경·취소 지시(B2MML CHANGE·CANCEL, OPC UA Job Control Update·Pause·Abort)는 로봇 쪽 주문 갱신·일시정지·취소·재지시로 옮겨야 하지만, 취소할 수 없는 동작은 끝까지 수행되고 base 는 바뀌지 않으므로 번역이 일대일이 아니며, 이미 화물을 실은 뒤라면 되돌림 작업이 추가로 필요할 것으로 보인다. | ref-185, ref-186, ref-187, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f23 | [추정] | ISA-95 계열의 작업 지시–작업 응답(B2MML, OPC UA Job Control)과 VDA 5050 주문–상태, Open-RMF 작업 요청–작업 상태는 모두 요청–응답 구조이지만 이번 검색 범위에서 이들을 서로 옮기는 표준 매핑은 확인되지 않았고, 확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다. | ref-031, ref-186, ref-138, ref-111, ref-191 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f24 | [추정] | 연계 대상: 주문 접수·출고 지시 방식(웨이브·웨이브리스)과 출고 우선순위 결정은 ERP·WMS·WES 같은 상위 업무 시스템의 몫이고, ROP 는 그 결과를 작업 요청의 우선순위·시작 시각·마감 제약으로 받아 로봇 작업으로 바꾸고 진행·완료·취소 결과를 되돌리는 경계에 서는 것으로 보인다. | ref-190, ref-189, ref-002, ref-138 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | — |
| f25 | [추정] | 동적 피킹 연구(개입형 전략, 재최적화)가 진행 중 사이클에 새 주문을 반영할 때 완료 시간·지연이 개선됨을 보이므로, ROP 는 대기열 수준 재정렬만이 아니라 실행 중 작업의 수정도 지원하되 교란 비용을 조건으로 판단하는 구조가 필요할 것으로 보인다. | ref-188, ref-120 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |

### 근거 발췌

- **f1**: 공식 저장소 main 명세 범위 절: 'standardized communication interface between a fleet control system and mobile robots'. 범위 밖으로 Traffic Management Logic, Other Communication Interfaces 등 열거. (발행일 미확인, 확인일 기준)
- **f2**: 명세: 'the base cannot be changed'; 'The horizon may be modified or deleted entirely with any order update'. 갱신의 첫 노드는 이전 주문의 마지막 공개 노드와 같아야 함. (발행일 미확인, 확인일 기준)
- **f3**: 열람 도구가 명세 원문에서 order 메시지의 priority 필드가 없다고 답함. order.schema 를 직접 대조하지 않아 부재의 확정은 아님. (발행일 미확인, 확인일 기준)
- **f4**: 주문 수락 흐름: 로봇이 'idle and not waiting for an update' 여야 새 orderId 수락. 거부 오류 유형 OTHER_ORDER_ACTIVE, OUTDATED_ORDER_UPDATE, SAME_ORDER_UPDATE_ID, INVALID_ORDER_ACTION 등. (발행일 미확인, 확인일 기준)
- **f5**: 명세: 'If the action cannot be cancelled, the actionState of that action should reflect that by reporting RUNNING while it is running.' 선로 유도형은 다음 가능한 노드에서, 자유 주행형은 즉시 정지. (발행일 미확인, 확인일 기준)
- **f6**: 명세 사전 정의 동작 표: startPause 'No more automatic driving - reaching next node is not necessary. Actions that can be paused (pauseAllowed=true), shall be paused, other actions continue.' (발행일 미확인, 확인일 기준)
- **f7**: task_request.json: priority 'This must match a priority schema supported by a fleet.'; fleet_name 을 지정하면 'only the named fleet(s) will bid for this task'. (발행일 미확인, 확인일 기준)
- **f8**: rewind_task_request.json: phase_id 'The task will restart at the beginning of this phase.' 취소·중단 요청은 type·task_id 필수, 목적을 적는 labels 선택. 세 파일 모두 같은 저장소. (발행일 미확인, 확인일 기준)
- **f9**: task_state.json 최상위 필드 booking, assigned_to, original_estimate_millis, estimate_millis, phases, completed, active, pending, interruptions, cancellation, killed. (발행일 미확인, 확인일 기준)
- **f10**: task_new 원본: dispatch_task_request 는 'the best available fleet', 'send requests to RMF to cancel a task or skip a phase'. (발행일 미확인, 확인일 기준)
- **f11**: B2MML-TransactionProfile.xsd 머리말 'Copyright 2023 MESA International, Version 0701'. 동사별 의미 설명과 응답 코드 열거는 이 파일에 없음.
- **f12**: 노드셋 문서화 CSV 메서드 목록과 nodeset2.xml 머리의 Version 2.0.0, 2024-01-31. ISA95JobOrderDataType·ISA95JobResponseDataType 정의. 메서드별 상태 전이는 이 파일로 확인 못 함.
- **f13**: 검색 요약(OPC 10031-4 6.2 절): Abort 는 'while the job order is running, interrupted or not even started'; Clear 는 클라이언트가 최종 결과를 받은 뒤 호출. 원문 미열람.
- **f14**: 검색 요약(ISA 보도자료): 'describe the integration of logistics systems with manufacturing control systems'; 2010판 Part 1 대비 'highlight the boundary between enterprise and manufacturing and control domains'. 원문 미열람.
- **f15**: 검색 요약(SCOR DS 소개 문서): Order 'activities associated with the customer purchase of products and services, including ... fulfillment status'; 기존 Deliver 를 Order 와 Fulfill 로 나눔. 원문 미열람. (발행일 2025판 기준)
- **f16**: 검색 요약: 'allowing ongoing AMR and worker pick cycles to be updated with new requests'; 지표 AOCT·AWTD·ATT. Transportation Research Part E 197, 104082. 원문 미열람.
- **f17**: 검색 요약: 비개입형은 피커가 거점으로 돌아올 때 새 주문을 반영, Reopt 'almost surely asymptotically optimal'. Networks(Wiley) 2025, arXiv 2409.12619. 원문 미열람.
- **f18**: 검색 요약: waveless policy 'yielded larger or equal throughput than the best performing wave-based policy with a lower gridlock probability'. MSOM 12(4) 642-662. 원문 미열람.
- **f19**: 검색 요약: 'REST API for exposing structured data to systems like MES and ERP, and an MQTT broker for real-time event publishing'; 'designed to support future integration with the VDA 5050 protocol'. 원문 미열람.
- **f20**: 검색 요약(머니투데이): 아르고 WMS 와 자율주행로봇 연동으로 동선·작업 속도 개선 모델 설계, 남이천 물류센터 실증, 로봇 30대 지원. 발표 단계이며 결과는 미확인. 원문 미열람.
- **f21**: f2·f3·f4·f5·f6(VDA 5050)과 f7·f8(Open-RMF)에서 도출한 추론. 로봇 인터페이스 표준 가운데 우선순위 재정렬 규칙을 정한 것은 확인하지 못함.
- **f22**: f11·f12·f13 의 상위 동사·메서드와 f2·f5 의 로봇 쪽 제약을 대응시킨 추론. cancelOrder 는 정지만 규정하고 화물 원위치 복귀는 규정하지 않음(열람 범위 기준).
- **f23**: f1(VDA 5050 은 외부 IT 인터페이스를 범위 밖에 둠), f9·f12 의 상태·응답 구조, f19 의 자체 API 사례에서 도출. 부재의 확인은 아님.
- **f24**: f15(SCOR Order·Fulfill), f18(출고 지시 정책 연구), f14(기업–제어 경계), f7(요청 필드)과 분류 원문 9장 '상위 업무 시스템' 경계를 대응시킨 추론.
- **f25**: f16(조건부 전략이 교란 최소화), f17(Reopt 의 개입형·비개입형 구분)에서 도출. 두 연구 모두 로봇 관제 인터페이스 제약(f2·f5)은 다루지 않은 것으로 보임.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-002 | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | 기사 | medium | 2026-09-25 | https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of | 예 |
| ref-138 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-182 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-183 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 아니오 |
| ref-184 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-185 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 아니오 |
| ref-186 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | high | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-187 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 미확인 | 표준 | medium | 2026-09-25 | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 | 예 |
| ref-188 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-120 | Lorenz 외 (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-189 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-190 | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 2025 | 표준 | medium | 2026-09-25 | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf | 예 |
| ref-191 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/2076-3417/15/13/7235 | 예 |
| ref-192 | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 2025-01 | 기사 | low | 2026-09-25 | https://news.mt.co.kr/mtview.php?no=2025012116183583251 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 공식 명세의 GitHub 저장소 본문(현재 main 은 3.0.0 판). 이번 실행은 범위, 주문 갱신, cancelOrder·startPause, 주문 수락·거부 규칙을 확인했다.
- **ref-002**: 원문 미열람. ANSI/ISA-95.00.01-2025(Part 1) 개정 발행을 알리는 ISA 보도자료. 기업 영역과 제조·제어 영역의 경계를 강조한다.
- **ref-138**: Open-RMF 작업 요청 JSON 스키마. category·description 필수, 우선순위·시작 시각·요청자·라벨·허용 플릿 선택 필드.
- **ref-182**: Open-RMF 작업 취소 요청 JSON 스키마. type·task_id 필수, labels 선택.
- **ref-183**: Open-RMF 작업 중단 요청 JSON 스키마. type·task_id 필수, 중단 목적 labels 선택.
- **ref-184**: Open-RMF 작업 되감기 요청 JSON 스키마. type·task_id·phase_id 필수, 지정 단계의 처음부터 재시작.
- **ref-111**: Open-RMF 작업 상태 JSON 스키마. 상태 값 12종과 배정 로봇·예상 시간·단계·중단·취소·강제 종료 필드를 정의한다.
- **ref-110**: Open-RMF 에 작업을 보내는 방법(dispatch_task_request, robot_task_request)과 취소·단계 건너뛰기 요청을 안내하는 공식 문서(mdBook 원본).
- **ref-185**: ISA-95 의 XML 구현 B2MML(판 0701)의 거래 프로파일 스키마. 거래 동사(NOTIFY·GET·PROCESS·CHANGE·CANCEL·CONFIRM·SYNC 계열)를 정의한다.
- **ref-186**: OPC UA for ISA-95 Part 4: Job Control 의 공식 노드셋(판 2.0.0). 작업 지시 수신 메서드와 작업 지시·응답 데이터형을 정의한다. 명세 본문은 아니다.
- **ref-187**: 원문 미열람. 작업 지시 수신 객체의 Pause·Resume·Abort·Clear 등 메서드와 작업 지시 상태 전이를 정의한 OPC UA 동반 규격의 공식 온라인 참조.
- **ref-188**: 원문 미열람. 작업자–AMR 협업 동적 주문 피킹에서 새 주문을 진행 중 사이클에 반영하는 개입형 전략을 제안한 Transportation Research Part E 197 논문.
- **ref-120**: 원문 미열람. 동적 도착 주문의 온라인 묶음·순서·경로 문제에서 재최적화의 성능을 수동·로봇 카트 조건으로 분석한 논문(arXiv 2409.12619).
- **ref-189**: 원문 미열람. 자동 분류기 창고의 웨이브·웨이브리스 출고 지시 정책을 실제 소매업체 자료로 비교한 MSOM 12(4) 논문.
- **ref-190**: 원문 미열람. SCOR DS 의 7개 프로세스(Orchestrate·Plan·Order·Source·Transform·Fulfill·Return)와 정의를 소개하는 ASCM 공식 소개 문서.
- **ref-191**: 원문 미열람. 다제조사 AGV·AMR 통합 플릿 관리 소프트웨어를 GreenAuto 프로젝트 사례로 제시하고 MES·ERP REST 연동과 MQTT 이벤트 구조를 설명한 논문(Applied Sciences 15(13) 7235).
- **ref-192**: 원문 미열람. 테크타카 WMS 와 플로틱 자율주행로봇 연동 실증(남이천 물류센터) 협력 발표를 전한 기사.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f1·f23(로봇 인터페이스는 상위 연계를 규정하지 않아 번역 계층 필요), f15(SCOR 의 Order·Fulfill 구분) / 섹션 4: f2(주문 갱신·base·horizon), f11(B2MML 거래 동사), f12·f13(작업 지시·작업 응답과 상태), f9(작업 상태), f18(웨이브·웨이브리스 출고 지시) / 섹션 5: 출하 우선순위 변경 f21(시작 조건·예외·성과)·f2·f3, 피킹 중 취소 f5·f22(예외·성과), 피킹 수행 자원 f16·f20, 포장·출고 지시 f18 — 흐름 단계와 여섯 항목 명시 / 섹션 6: f2·f4·f5·f6·f7·f8·f10·f21·f22·f25 / 섹션 7: f1~f6(VDA 5050 3.0.0), f7~f10(Open-RMF 작업 API), f11(B2MML), f12·f13(OPC UA for ISA-95 Job Control), f14(ISA-95 Part 1 2025), f15(SCOR DS) / 섹션 8: f16·f17·f18·f19, 국내 사례 f20(기사, 발표 단계임을 명시) / 섹션 9: f24(연계 대상: 출고 지시·우선순위 결정), f1, f23 / 섹션 10: 2. 공정·워크플로 모델링(f12), 9. 로봇·제조사 관제 연동(f1·f2·f10), 12. 명령·작업 실행의 신뢰성(f4·f8), 13. 작업 배정 — MRTA(f10·f16), 14. 작업 순서·스케줄링(f17·f21), 20. 예외 복구·재계획·업무 연속성(f5·f22), 28. 표준·상호운용성·다사업자 거버넌스(f23) / 섹션 11: open_questions_new 3건과 기존 oq-002 연결(f20) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 작업 지시 | Job Order (ISA-95) | ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다. |
| B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International 이 ISA-95(IEC 62264)의 데이터 모델과 거래를 XML 스키마로 구현한 교환 형식이다. |
| 웨이브리스 출고 지시 | Waveless Order Release | 주문을 큰 묶음(웨이브)으로 모아 내리지 않고 도착·여유 용량에 따라 연속으로 현장에 내려보내는 출고 지시 방식이다. |

## 열린 질문

새로 생긴 질문:

- 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | 관련 영역: 1. 주문·업무 시스템 연계, 14. 작업 순서·스케줄링 | 근거: f21 | 종류: 일반
- ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 1. 주문·업무 시스템 연계, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f23 | 종류: 일반
- 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | 관련 영역: 1. 주문·업무 시스템 연계, 20. 예외 복구·재계획·업무 연속성 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 규격마다 발행 기관 한 곳의 원문만 있고(Open-RMF 스키마 4건은 같은 저장소), 논문은 단일 출처
    - f3 VDA 5050 order 메시지 우선순위 필드 부재는 열람 도구 응답 기준이며 order.schema 직접 대조 안 함
    - f13 OPC 10031-4 상태 전이는 검색 요약만 확인(ref-187 원문 미열람), 노드셋 CSV 로는 메서드 이름만 확인
    - f14·f15·f16·f17·f18·f19 원문 미열람(검색 요약 범위만 사용)
    - f20 국내 실증은 발표 기사뿐이며 결과 미확인
    - ref-120 제1저자 이름 전체와 ref-191 저자 미확인
    - ref-031·ref-138~ref-110 발행일 미확인
    - TMS 연계(운송 마감·도크 배정)와 MES 생산 지시 연계는 1차 자료를 충분히 찾지 못함
- 범위 경계 위반 의심:
    - f24: 출고 지시 정책·우선순위 결정은 분류 원문 9장 '상위 업무 시스템' 쪽이므로 '연계 대상: '으로 표시함
    - f18: 웨이브·웨이브리스 출고 지시는 WMS·WES 정책이므로 ROP 직접 범위가 아니라 입력 조건으로만 쓰도록 제안
- 한계: fetch_mode mirror_only(web_fetch_available: false): raw.githubusercontent.com 공식 저장소 원문(VDA 5050 main 명세, Open-RMF rmf_api_msgs 스키마 5건과 task_new 원본, B2MML 거래 프로파일 스키마, OPC UA ISA-95 Job Control 노드셋)은 열어 fetched=true 로 표시했다. ISA 보도자료·OPC 온라인 참조·ASCM 문서·논문 4건·기사는 원문 미열람(신뢰도 상한 medium, 기사 low). 교차 확인 0건. 검색 20회/30, 신규 출처 15건/15(ref-138~ref-192, next_ref_id 기준)로 출처 상한에 도달해 Ceven·Gue(2017) 웨이브 출고 시각 연구, Open-RMF 입찰(task.md) 문서, SYNAOS 벤더 글(WMS/ERP–VDA 5050 번역 주장), 씨메스 벤더 블로그(WES 우선순위 재정렬 주장)는 넣지 못했다. 재사용 출처 2건(ref-031, ref-002). 이전 실행 2026-09-25-08 이 같은 영역을 조사했으나 그 출처 id 가 참고문헌 목록에 없어 게시되지 않은 것으로 보고 원문을 다시 열어 새 id 로 기록했다(같은 URL 이 이전 브리프의 ref-138~ref-187 제안과 겹치므로 퍼블리셔 확인 필요). 한국 자료는 기사 1건(발표 단계)뿐이며 학술·공공 자료는 한국어 검색 4회에서 찾지 못했다. oq-002 는 해결하지 못했다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다.
