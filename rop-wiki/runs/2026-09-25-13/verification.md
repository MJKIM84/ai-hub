# 1차 검증(브리프) 2026-09-25-13

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문(data/source_texts/ref-031, 3.0.0 main) 2장 Scope 에서 'Traffic Management Logic', 'Other Communication Interfaces … external IT systems' 제외를 확인했다. 단일 발행 기관(VDA/VDMA). 발행일 미확인, 확인일 2026-09-25. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: 원문 6.1.2 'the base cannot be changed', 'fleet control shall therefore assume that the base has already been executed', 'The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon', 갱신의 첫 노드 = 이전 마지막 base 노드를 확인했다. |
| f3 | 예 | 예 | 아니오 | 유지 | [추정] low 유지. 검증자가 raw 경로로 main json_schemas/order.schema 를 열어 order·node·edge·action 어느 수준에도 우선순위 필드가 없음을 확인했다(브리프 미열람분 보완). 이 스키마는 브리프 출처가 아니므로 본문 태그를 올리지 않는다. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: 원문 6.1.2 수락 흐름 3항 'idle and not waiting for an update', 6.6.8 유휴 정의, 6.1.4.6 OTHER_ORDER_ACTIVE(level WARNING)를 확인했다. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: 원문 6.1.3 에서 예정 동작 FAILED, 실행 중 동작 취소 시 FAILED, 취소 불가 동작은 RUNNING 후 결과 상태, 모든 이동·동작 정지 후 cancelOrder FINISHED, 선로 유도형·자유 주행형 정지 차이를 확인했다. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: 원문 표 4 startPause·stopPause 정의가 주장과 일치한다. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw task_request.json 을 열어 필수 category·description, 선택 unix_millis_earliest_start_time·unix_millis_request_time·priority('must match a priority schema supported by a fleet')·requester·labels·fleet_name 을 확인했다. 주장 문장의 '최早'는 오기(한자 혼입)이다(required_fixes). |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: raw rewind_task_request.json(type·task_id·phase_id 필수, 'The task will restart at the beginning of this phase'), interrupt_task_request.json(type·task_id 필수, labels 선택)을 열어 확인했다. cancel 스키마는 게시된 2. 공정·워크플로 모델링 실행 계열에서 같은 구조로 확인된 바 있다. 세 파일은 같은 저장소라 독립 교차 아님. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: 같은 파일(task_state.json)이 이미 참고문헌 ref-111 로 게시돼 2. 공정·워크플로 모델링 페이지에서 같은 12개 상태 값으로 검증됐다. 새 id 대신 기존 ref-111 을 재사용한다(required_fixes). |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: raw task_new.md 에서 /task_api_requests·ApiRequest, dispatch_task_request 'to the best available fleet', robot_task_request 'to a specific robot', 'cancel a task or skip a phase' 문장을 확인했다. 같은 문서가 이미 ref-110 으로 게시돼 있으므로 기존 id 를 재사용한다. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: raw B2MML-TransactionProfile.xsd 머리말 'Copyright 2023 MESA International, Version 0701', ANSI/ISA-95.00.02-2018·95.00.05-2018 기반, 동사 열거 NOTIFY·GET·PROCESS·CHANGE·CANCEL·CONFIRM·SYNC ADD·SYNC CHANGE·SYNC DELETE·Other 를 확인했다. 동사별 의미 설명은 파일에 없다. |
| f12 | 예 | 예 | 아니오 | 유지 | 확인: raw documentation.csv 에서 Store·StoreAndStart·Start·RevokeStart·Pause·Resume·Stop·Update·Abort·Cancel·Clear 와 RequestJobResponseByJobOrderID·RequestJobResponseByJobOrderState·ReceiveJobResponse, ISA95JobOrderDataType·ISA95JobResponseDataType 를 확인했고, nodeset2.xml Models 요소에서 Version 2.0.0, PublicationDate 2024-01-31 을 확인했다. |
| f13 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과(reference.opcfoundation.org/specs/OPC-10031-4/6.2)에서 Pause→Interrupted, Resume→Running, Abort 는 running·interrupted·not even started(AllowedToStart·NotAllowedToStart)에서 Aborted, Aborted·Ended 후 Clear 를 확인했다. 스니펫 범위 안의 주장이다. 판(v200)·발행일 미확인. |
| f14 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과에서 ANSI/ISA-95.00.01-2025(IEC 62264-1 Mod) 발행, 'integration of logistics systems with manufacturing control systems', 2010판 대비 'highlight the boundary between enterprise and manufacturing and control domains' 를 확인했다. 보도자료 게시일은 2025-04-10(PR Newswire·automation.com 재게재는 같은 보도자료라 독립 교차 아님). |
| f15 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과(ASCM intro-and-front-matter-scor-digital-standard-2025.pdf)에서 7개 프로세스와 Order('customer purchase … fulfillment status'), Fulfill('scheduling order delivery, picking, packing, shipping …') 정의를 확인했다. 게시된 ref-001(SCOR DS 페이지)과 같은 발행 기관이라 독립 교차 아님. |
| f16 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과로 저자 S. Yu·S. Srinivas, TR Part E 197(2025), CHR-DOPP, 진행 중 사이클을 새 요청으로 갱신하는 개입형 전략, 개입 없는 협업 시스템 대비 AOCT·ATT 개선을 확인했다. 같은 요약은 AWTD 가 늘었다고 적어, 개선만 적으면 맥락이 빠진다(required_fixes). 두 전략의 세부 이름은 검증 검색에서 재확인하지 못했다. |
| f17 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과(Wiley net.22281, arXiv 2409.12619)에서 OOBSRP, 수동·로봇 카트, Reopt 의 almost surely asymptotically optimal 를 확인했다. 저자는 Lorenz·Otto·Gendreau(2025, Networks)로 확인됐다(required_fixes). 개입형·비개입형 구분은 브리프 스니펫 기준. |
| f18 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과(MSOM 10.1287/msom.1100.0291)에서 웨이브리스 정책이 'in all scenarios considered' 가장 좋은 웨이브 정책 이상의 처리량을 더 낮은 gridlock 확률로 냈다는 결론을 확인했다. 기준일 2010. |
| f19 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과로 Applied Sciences 15(13) 7235(2025-06-27 게재), GreenAuto 프로젝트, 다제조사 AGV·AMR 을 한 지도에서 통합 감시하는 웹 플랫폼을 확인했다. REST·MQTT 구조와 VDA 5050 향후 연동 문구는 브리프 스니펫 기준이며 검증 검색에서 재확인하지 못했다. 저자 미확인. |
| f20 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색에서 머니투데이 기사 URL 실재와 함께 테크M·물류신문·AI타임스·한국경제가 같은 내용(아르고 WMS–플로틱 자율주행로봇 연동, 남이천 물류센터 실증, 오더 피킹 특화 로봇 30대)을 보도했음을 확인했다. 같은 보도자료 계열이라 독립 교차로 보지 않는다. 발표 단계이며 결과 미확인. |
| f21 | 예 | 예 | 아니오 | 유지 | f2~f8 에서 도출한 추론으로 근거 finding 이 모두 확인돼 [추정] low 를 유지한다. VDA 5050 3.0.0 의 PRIORITY 구역은 경로 계획 선호도이지 주문 우선순위가 아니므로 섞어 쓰지 않는다. |
| f22 | 예 | 예 | 아니오 | 유지 | f11~f13 과 f2·f5 를 대응시킨 추론. B2MML 동사의 의미 정의는 스키마에 없다는 한계를 함께 둔다. [추정] low 유지. |
| f23 | 예 | 예 | 아니오 | 유지 | f1·f9·f12·f19 에서 도출한 추론, 부재의 확인 아님. [추정] low 유지. 기존 oq-014(업무 프로세스 단계 상태와 로봇 작업 상태 동기화)와 관련된다. |
| f24 | 예 | 예 | 아니오 | 유지 | '연계 대상:' 표시가 있고 분류 원문 9장 '상위 업무 시스템' 경계와 맞다. 근거 ref-122·ref-121·ref-002 가 원문 미열람인데 finding 의 source_unopened 가 false 로 적혀 있다(verification_note 기록). [추정] low 유지. |
| f25 | 예 | 예 | 아니오 | 유지 | f16·f17 에서 도출한 추론. [추정] low 유지. 두 연구가 로봇 관제 인터페이스 제약을 다루지 않았다는 부분은 브리프 판단이며 원문 미열람. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | 참고문헌 id 충돌: 브리프의 ref-110·ref-111·ref-112·ref-113·ref-114·ref-116·ref-117·ref-118·ref-119·ref-121·ref-122·ref-123·ref-124 가 이미 게시된 다른 출처(task_new, task_state.json, OMG BPMN, Camunda, Corradini 외, Filippone 외, B2MML-Common.xsd, B2MML-OperationsDefinition.xsd, IEC 62264-3, Blondin 외, OCEL 2.0, SCOR F1.3, 스마트물류센터 인증제 안내)의 id 와 같다, 브리프 ref-115(task_new)는 게시된 ref-110 과, 브리프 ref-114(task_state.json)는 게시된 ref-111 과 같은 문서다 — 기존 id 재사용 대상, f9(Open-RMF 작업 상태 12개 값)·f10(task_new 작업 요청 방식)은 게시된 2. 공정·워크플로 모델링 페이지의 같은 주장과 겹친다 — 기존 각주 ref-111·ref-110 재사용, f11(B2MML 판 0701·ISA-95 2018 기반)은 게시된 2. 공정·워크플로 모델링의 B2MML-Common.xsd(ref-117) 서술과 겹치며 용어집 B2MML 항목이 이미 있다, f15(SCOR DS 프로세스)는 시드 ref-001(ASCM SCOR DS)과 용어집 SCOR 정의와 겹친다(모순 없음), 새 열린 질문 2(ISA-95 작업 지시↔VDA 5050·Open-RMF 매핑)는 기존 oq-014(BPMN 단계 상태↔로봇 작업 상태 동기화)·oq-001 과 관련되나 대상이 달라 중복은 아니다, 이전 미게시 브리프 2026-09-25-08 과 같은 URL·주장을 다시 조사했다(같은 영역 재실행) |
| 용어 일관성 | 아니오 | 용어 후보 'B2MML' 은 용어집에 이미 있다(b2mml.md) — 신규 등록하지 않는다, f7 주장 문장의 '최早 시작 시각'은 한자 혼입 오기다 — '가장 이른 시작 시각'으로 쓴다 |
| 인용 길이·저작권 | 아니오 | ref-031 에서 직접 인용이 여러 번 계획돼 있다(f1 범위 문구, f2 'the base cannot be changed'·'The horizon may be modified…', f5·f6 문구), ref-110(새 id ref-125, task_request.json)에서 f7 직접 인용이 두 번 계획돼 있다 |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- 참고문헌 id 재부여: 브리프의 출처 id 를 다음처럼 한 번에 바꿔 본문 각주·프런트매터 sources·reference_updates 에 일관되게 쓴다 — ref-110(task_request.json)→ref-125, ref-111(cancel_task_request.json)→ref-126, ref-112(interrupt_task_request.json)→ref-127, ref-113(rewind_task_request.json)→ref-128, ref-114(task_state.json)→기존 ref-111 재사용, ref-115(task_new)→기존 ref-110 재사용, ref-116(B2MML-TransactionProfile.xsd)→ref-129, ref-117(ISA95-JOBCONTROL 노드셋)→ref-130, ref-118(OPC 10031-4 6.2)→ref-131, ref-119(Yu·Srinivas)→ref-132, ref-120(Lorenz 외)→ref-133, ref-121(Gallien·Weber)→ref-134, ref-122(SCOR DS 소개 문서)→ref-135, ref-123(Applied Sciences 사례)→ref-136, ref-124(머니투데이)→ref-137. 재사용 ref-002·ref-031 은 그대로 쓴다 — 이유: 브리프 id 가 게시된 참고문헌 ref-110~ref-124 와 충돌하며, 기존 ref-110·ref-111 페이지를 덮어쓰지 않는다. 기존 ref-110·ref-111 은 reference_updates 로 새로 등록하지 않는다.
- 각주 원문 미열람 표기: 원문을 열지 않은 출처 ref-002, ref-131, ref-132, ref-133, ref-134, ref-135, ref-136, ref-137(새 id 기준)의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates[].source_unopened: true 로 둔다. raw 원문을 연 ref-031, ref-110, ref-111, ref-125~ref-130 에는 붙이지 않는다.
- f7: '최早 시작 시각'을 '가장 이른 시작 시각'으로 고쳐 쓴다 — 한자 혼입 오기다.
- f16: 결과를 '개입 없는 협업 시스템보다 평균 주문 완료 시간(AOCT)과 평균 총 지연(ATT)이 좋았다'로 한정하고, 같은 비교에서 AWTD 지표는 늘었다는 점을 함께 적는다 — 검증 검색 요약이 AWTD 증가를 명시해 개선만 쓰면 맥락이 빠진다. '두 가지 전략'의 세부 이름을 쓸 때는 [사실] 문장 안에서 저자 제안임을 밝힌다.
- f17: 저자 표기를 'Lorenz, Otto, & Gendreau'(Networks, 2025)로 적고 reference_updates 의 org 도 같게 한다 — 검증 검색으로 확인했다.
- ref-002: reference_updates 로 발행일을 '2025-04-10'으로 갱신할 수 있다(ISA 보도자료 게시일, 검증 검색 확인). 갱신하지 않으면 기존 '2025'를 유지한다.
- 인용: ref-031 의 직접 인용은 페이지 전체에서 한 번만(예: f2 의 'the base cannot be changed') 쓰고 f1·f5·f6 은 재서술한다. ref-125(task_request.json)도 직접 인용은 한 번만 쓴다 — 5.3 출처당 1회 규칙.
- f9·f10: 2. 공정·워크플로 모델링 페이지에 이미 있는 같은 주장이므로 새 각주를 만들지 않고 ref-111·ref-110 을 달며, 10절에서 2. 공정·워크플로 모델링과 연결한다.
- f19: 'MES·ERP 에 REST API, 로봇 이벤트 MQTT, VDA 5050 향후 과제' 부분은 저자 설계 기술로 쓰고 성과 수치는 붙이지 않는다 — 검증 검색은 다제조사 통합 감시 플랫폼까지만 재확인했다.
- f20: 본문에서 '2025년 1월 보도된 협력 발표이며 실증 결과는 미확인'임을 문장에 명시하고 5절에는 가상 예시가 아니라 발표 사례로만 둔다. oq-002 는 f20 이 SSCC·EPCIS 연결을 다루지 않으므로 해결로 바꾸지 않는다.
- f21 서술 시 VDA 5050 3.0.0 의 PRIORITY 구역(경로 선호도)을 주문 우선순위 수단처럼 쓰지 않는다 — 브리프에 없는 내용이며 의미가 다르다.
- 용어집: 'B2MML' 은 이미 있으므로 glossary_updates 에 신규 등록하지 않는다. '작업 지시(Job Order)'·'웨이브리스 출고 지시(Waveless Order Release)'만 신규로 등록한다.
- open_questions_new 3건은 형식이 맞으므로 등록하되, 2번 질문의 open_question_updates 에는 관련 기존 질문 oq-014·oq-001 과의 관계를 페이지 11절에서 링크로만 밝힌다.

## 검증 노트

판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다; GitHub 공식 저장소 원문(VDA 5050 명세·order.schema, Open-RMF task_request·interrupt·rewind 스키마와 task_new 원본, B2MML 거래 프로파일 스키마, OPC UA ISA-95 Job Control 노드셋 CSV·XML)은 검증자가 직접 열어 대조했다. 확인 25건, 미확인 0건, 교차 확인 0건(모든 핵심 사실이 발행 기관 한 곳의 산출물이거나 단일 논문·기사). 강등: 없음. 원문 미열람 출처: ref-002, ref-131(OPC 10031-4), ref-132(Yu·Srinivas), ref-133(Lorenz·Otto·Gendreau), ref-134(Gallien·Weber), ref-135(SCOR DS 소개), ref-136(Applied Sciences 사례), ref-137(머니투데이) — 새 id 기준. 주의: 브리프의 새 출처 id 가 게시된 참고문헌 ref-110~ref-124 와 충돌해 ref-125~ref-137 로 재부여하고 같은 문서인 task_new·task_state.json 은 기존 ref-110·ref-111 을 재사용하도록 지시했다; pipeline 담당은 next_ref_id 산출(게시 목록의 빈 번호 ref-115·ref-120 을 재사용하지 않도록)을 점검해야 한다. f3 의 VDA 5050 주문 우선순위 필드 부재는 검증자가 main order.schema 로 재확인했으나 태그는 [추정]으로 둔다. f16 은 AWTD 증가를 함께 적도록 했다. f24 는 원문 미열람 출처에 기대면서 source_unopened 가 false 로 기록돼 있다(브리프 표시 불일치). 로봇 인터페이스 쪽 결론(f21~f25)은 모두 추론이며, 출고 우선순위 재정렬을 다룬 공개 설계는 확인하지 못했다. 한국 자료는 기업 협력 발표 기사 1건뿐이고 oq-002 는 해결되지 않았다. 정정 요청 없음. 미사용 출처: 없음. 검증 검색 8회 사용(리서치 20회와 합쳐 28/30).
