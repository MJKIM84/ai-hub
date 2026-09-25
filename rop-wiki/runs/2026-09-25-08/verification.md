# 1차 검증(브리프) 2026-09-25-08

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 텍스트(data/source_texts/ref-031.txt, 3.0.0 main) 6.1.2절에 'The orderId stays the same and the orderUpdateId is incremented', base 변경 불가, 결정 지점 내용 불변, 공개된 노드의 sequenceId 불변 문구가 있다. 단일 발행 주체(VDA/VDMA)라 교차 확인 아님. 발행일 미확인(확인일 2026-09-25). |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: 원문 6.1.3절. 가능한 한 빨리 정지(선로 유도형은 다음 가능한 노드, 자유 주행형은 즉시), 예정 동작 FAILED, 취소 불가 동작은 완료 후 최종 상태 보고, 모든 이동·동작 정지 뒤 cancelOrder FINISHED, 유휴 상태로 새 주문 수신 가능. 원문 텍스트로 확인했으므로 '요약 도구 경유' 단서는 필요 없다. 원문은 취소 자체도 통신 한계로 신뢰할 수 없다고 적는다(6.1.2). |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: OUTDATED_ORDER_UPDATE·OTHER_ORDER_ACTIVE·INVALID_ORDER_ACTION·VALIDATION_FAILURE·SAME_ORDER_UPDATE_ID·NO_ROUTE_TO_TARGET·MOBILE_ROBOT_NOT_AVAILABLE 는 6.1.4절, ORDER_UPDATE_FOLLOWING_CANCEL 은 6.1.3.1절과 표 9 에 글자 단위로 있다. 브리프의 '글자 단위 일치 미확인'은 원문 텍스트로 해소됐다. 모두 등급 WARNING(UNSUPPORTED_PARAMETER 만 CRITICAL). |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: 원문 2절 범위 밖 목록에 'Other Communication Interfaces … such as interfaces to peripheral equipment, infrastructure components, or external IT systems'와 교통 관리 로직이 있다. 원문은 WMS·ERP 를 직접 거명하지 않으므로 'WMS·ERP 같은'은 외부 IT 시스템의 예시로 표현해야 한다(수정 지시). |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: raw.githubusercontent.com 으로 task_request.json 열람. required [category, description], 선택 priority·unix_millis_earliest_start_time·unix_millis_request_time·requester·fleet_name·labels. fleet_name 은 지정 시 그 플릿만 입찰. 주장 문구의 '최早'는 오기(용어 수정 지시). |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: cancel_task_request.json 열람. required [type, task_id], type 값은 'cancel_task_request', labels 선택. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: task_state.json 열람. status enum 12종이 주장과 같고, 최상위에 assigned_to·original_estimate_millis·estimate_millis·interruptions·cancellation·killed 등이 있다. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: task_new.md 원본 열람. /task_api_requests 토픽 ApiRequest 발행, dispatch_task_request 는 'the best available fleet', robot_task_request 는 특정 로봇. 취소 스키마는 rmf_api_msgs schemas 목록 링크로만 안내된다. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: README 원문 'B2MML is an XML implementation of the ANSI/ISA-95, Enterprise-Control System Integration, family of standards (ISA-95), known internationally as IEC/ISO 62264.' 저장소 소유자와 스키마 저작권 표기가 MESA International. README 에 B2MML 판 번호는 없다. |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: B2MML-TransactionProfile.xsd 열람. TransactionVerb1Type 열거값이 NOTIFY, GET, PROCESS, CHANGE, CANCEL, CONFIRM, SYNC ADD, SYNC CHANGE, SYNC DELETE, Other 로 주장과 같다. 파일 머리에 'Copyright 2023 MESA International, Version 0701'과 ANSI/ISA-95.00.05-2018 Part 5 참조가 있어 기준 판으로 적을 수 있다. |
| f11 | 예 | 예 | 아니오 | 유지 | 원문 미열람(fetch_mode mirror_only, 검색 결과 일치). OPC Foundation 온라인 참조 v200 '4 ISA-95 Overview' 스니펫: Work Schedule 은 하나 이상의 Work Request, 각 Work Request 는 하나 이상의 Job Order, Job Response 는 Job Order 에 대한 수행 보고. 신뢰도 medium 상한. |
| f12 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). 스니펫: ISA95JobOrderReceiverObjectType 메서드는 Store, StoreAndStart, Start, RevokeStart, Pause, Resume, Update, Abort, Stop, Cancel, Clear 이며, Abort 는 실행 중·중단·시작 전(AllowedToStart·NotAllowedToStart) 모두에서 상태를 Aborted 로 바꾼다. 주장의 메서드 목록은 일부이므로 전체 목록처럼 쓰지 않게 한다. v1.00/v2.00 판별 차이는 미확인. |
| f13 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). arXiv 1801.06703(Merschformann, Lamballais, de Koster, Suhl) 검색 스니펫에 운영 의사결정을 (1) Order Assignment (2) Task Creation (3) Task Allocation (4) Path Planning 네 단계로 나눈다는 문장이 있다. 같은 논문은 2019년 ScienceDirect(Operations Research Perspectives 계열) 게재본이 있어 최신 판 표기를 확인할 여지가 있다(발행일 note 로만 남김). |
| f14 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). 씨메스 블로그 글이 실재하며(같은 글이 모비인사이드에 2025-09-10 재게재), 스니펫은 WMS=창고 전체 관리, WES=WMS 작업 지시를 바탕으로 장비·작업자 작업을 순서화·배분, WCS=컨베이어·AGV·로봇 실시간 제어라는 역할 구분까지만 담는다. '출고 시간·SKU 수·주문 난이도에 따른 자동 재정렬' 세부는 검증 검색 스니펫에서 확인되지 않아 빼게 한다. 벤더 주장·추정 유지. |
| f15 | 예 | 예 | 아니오 | 유지 | 추론 finding. 근거 f1·f5·f7·f11 은 확인됐고, 매핑 부재는 검색 범위 기준이며 부재의 확인이 아님을 유지해야 한다. ref-116 는 원문 미열람인데 브리프가 source_unopened false 로 적었다(브리프 기록 누락). |
| f16 | 예 | 예 | 아니오 | 유지 | 추론 finding. 근거 f1·f2·f3·f5·f6 확인. 원문 2절이 우선순위 부여(prioritization)를 포함한 교통 관리 로직을 범위 밖으로 둔다는 점과도 어긋나지 않는다. VDA 5050 주문 메시지의 우선순위 필드 유무는 미확인으로 남긴다. |
| f17 | 예 | 예 | 아니오 | 유지 | 추론 finding. 근거 f10·f12(원문 미열람)·f1·f2·f6 확인. cancelOrder 가 정지와 동작 상태만 규정하고 화물 원위치 복귀를 규정하지 않는다는 점은 원문 6.1.3절과 맞다. ref-116 원문 미열람 표기 누락(브리프). |
| f18 | 예 | 예 | 아니오 | 유지 | 추론 finding. 분류 원문 9장 '상위 업무 시스템'의 외부 연계 열은 수요예측·구매·재무·전사 재고정책이며 '주문을 작업대에 배정'은 거기 없다. 원문 2장은 WES·WCS·FMS·ROP 의 책임이 제품별로 겹칠 수 있다고 적는다. 따라서 추정으로만 두고 경계가 제품 전략에 따라 이동할 수 있음을 함께 적게 한다(수정 지시). |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 예 | ref-031 은 기존 참고문헌 재사용(정상). 새 id ref-110~ref-118 은 참고문헌 목록(ref-052 까지, ref-046 결번)과는 겹치지 않으나, 이전 브리프 2026-09-25-04·05·06 이 같은 id 를 다른 출처에 부여했으므로 퍼블리셔가 등록 시 충돌 여부를 확인해야 한다., f11 의 ISA-95 개념은 용어집 '기업–제어 시스템 통합 표준(ISA-95)'과 이어지므로 새 용어 '작업 지시·작업 응답'은 그 항목에 연결한다., f14 의 WMS·WES·WCS 역할은 용어집 'WES/WCS/WMS/MES/TMS' 항목 정의(ROP는 작업 요청을 받아 로봇 작업으로 바꾸고 결과를 되돌려 줌)와 충돌하지 않는다. |
| 용어 일관성 | 아니오 | f5 주장의 '최早 시작 시각'은 오기다 — '가장 이른 시작 시각(unix_millis_earliest_start_time)'으로 쓴다., 관제는 용어집 VDA 5050 항목과 같이 '상위 관제(fleet control)'로 통일한다. |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f5: '최早 시작 시각'을 '가장 이른 시작 시각(unix_millis_earliest_start_time)'으로 고친다 — 문자 오기.
- f4: 'WMS·ERP 같은 상위 시스템에서 주문을 받는 인터페이스는 규정하지 않는다'를 '외부 IT 시스템(예: WMS·ERP)과의 인터페이스는 범위 밖으로 둔다'로 고쳐 쓴다 — 원문 2절은 WMS·ERP 를 직접 거명하지 않고 'external IT systems'로만 적는다.
- f2·f3: 페이지에 '요약 도구 경유'·'오류 유형 문자열 글자 단위 일치 미확인' 단서를 옮기지 않는다 — 입력 원문 텍스트(ref-031) 6.1.3·6.1.4·6.6.5.4절에서 글자 단위로 확인됐다. 단 ORDER_UPDATE_FOLLOWING_CANCEL 은 '취소 뒤 갱신 거부' 오류로, 나머지와 함께 '주문 거부·취소 관련 오류 유형'으로 묶어 쓴다.
- f12: 메서드 목록을 전체처럼 쓰지 말고 '…등의 메서드'로 쓰고, 기준 판을 '온라인 참조 v2.00 기준, 판별 차이 미확인'으로 명시한다 — 검증 검색 결과상 Start·Stop·Cancel·Clear 도 있다.
- f10: 기준일·판을 스키마 머리 표기 'Version 0701(저작권 표기 2023)' 기준으로 적는다 — 발행일 null 을 보완하는 버전 정정.
- f14: [추정]에 '벤더 주장'을 병기하고, '출고 시간·SKU 수·주문 난이도에 따른 우선순위 자동 재정렬' 세부를 빼고 WMS(창고 업무 관리)–WES(WMS 작업 지시를 바탕으로 장비·작업 순서 조정)–WCS(장비 실시간 제어) 역할 구분까지만 쓴다 — 출처가 벤더 블로그이고 재정렬 기준은 검증 검색 요약에서 확인되지 않았다.
- f18: 9절에서 [추정]으로만 쓰고, '주문의 작업대 배정·재고 할당'을 분류 원문 9장 표의 외부 연계 열 항목처럼 쓰지 않는다. 원문 2장의 'WES·WCS·FMS·ROP의 책임은 겹칠 수 있다'와 9장의 '경계는 제품 전략에 따라 이동할 수 있다'를 함께 제시한다 — 9장 표의 상위 업무 시스템 외부 연계 열은 수요예측·구매·재무·전사 재고정책뿐이다.
- f15·f16·f17: [추정] 유지, '표준 매핑이 없다'처럼 단정하지 말고 '이번 검색 범위에서 확인되지 않았다'로 쓴다 — 부재의 확인이 아니다.
- 각주: ref-116·ref-117·ref-118 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 세 항목에 source_unopened: true 를 넣는다. ref-031·ref-110~ref-115 은 공식 저장소 원문(github_raw·inbox)을 열었으므로 붙이지 않는다.
- 5절 현장 시나리오: 출하 우선순위 변경(f14·f16)과 피킹 중 취소(f17)를 흐름 단계와 여섯 항목(시작 조건·예외·성과 등) 문자열로 명시하고, 수치 없는 설명용 가상 시나리오임을 밝힌다.
- 용어집: '작업 지시(Job Order)'·'작업 응답(Job Response)' 정의는 ISA-95 용어집 항목과 연결하고 근거 각주를 ref-116(원문 미열람)로 둔다.

## 검증 노트

판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(fetch_mode mirror_only)에서 검증됐으며, 공식 GitHub 저장소 원문(VDA 5050 3.0.0 명세 입력 원문, Open-RMF rmf_api_msgs 스키마 3건·task_new 원본, B2MML README·거래 프로파일 스키마)은 직접 열어 대조했다. 확인 18건, 미확인 0건, 교차 확인 0건. 강등: 없음(f14 는 추정·벤더 주장 유지, 확인되지 않은 재정렬 기준 세부 삭제 지시). 원문 미열람 출처: ref-116, ref-117, ref-118. 브리프 출처 원문 미열람 표시 누락: f15·f17·f18 이 ref-116·ref-117 에 기대는데 source_unopened false 로 적힘. 주의: 모든 사실 주장이 규격별 발행 주체 한 곳의 자료라 독립 교차 확인이 없고, 섹션 3·8 근거가 얇으며(ERP·TMS·MES 연계 사례, SCOR 관점 미조사), 한국 자료는 벤더 블로그 1건이다. ISA-95 계열 작업 지시와 VDA 5050·Open-RMF 작업을 잇는 표준 매핑은 검색 범위에서 확인되지 않았을 뿐 부재가 확인된 것은 아니다. 참고문헌 id ref-110~ref-118 은 이전 트랙 브리프들이 같은 id 를 다른 출처에 쓴 적이 있어 퍼블리셔의 충돌 확인이 필요하다. 정정 요청 없음.
