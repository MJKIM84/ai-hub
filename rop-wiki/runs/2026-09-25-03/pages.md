# 스토리텔러 산출 2026-09-25-03

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| create | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md | draft | 신규 작성: 로봇 적재·하역 완료 신호를 EPCIS 이벤트 필드(readPoint·bizLocation·source/destination)로 나누는 방법과 CBV 정의 한계, 식별 수준 비교, 매핑 부재. 2차 수정: 4절 끝 문장 태그·각주, 약어 첫 등장 풀어 쓰기 |
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | draft | 4절 인계 맥락 유형에 ref-044 각주 추가, 6절 이벤트 기반 추적에 readPoint·bizLocation 구분과 CBV loading 정의 한계·새 주제 페이지 링크 추가(분량 초과 시 요약은 절 내용 요약 2문장), 7절 EPCIS·CBV 열람 표시 분리와 Oliot EPCIS 행 추가, 11절 새 질문 2건 |
| create | docs/topics/2026/2026-09-25-area07-s6.md | draft | 자동 분리: 7. 화물·재고·자산 식별과 추적 의 "6. 대표 접근법과 기술" 절(775자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 7. 화물·재고·자산 식별과 추적 | 주제 페이지 '로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가' 신규 작성, 영역 페이지 4·6·7·11절 갱신(Oliot EPCIS 행, 새 열린 질문 2건) | run 2026-09-25-03
- 홈 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 주제 '로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가' 신규 작성(readPoint·bizLocation·source/destination 구분, CBV loading 정의 한계, 매핑 미확인)
- 대분류 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: EPCIS 인계 이벤트 설계 주제 페이지 신규, 6·7·11절 갱신(국내 오픈소스 Oliot EPCIS, 새 열린 질문 2건)
- 세부영역 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 6절 이벤트 기반 추적에 readPoint·bizLocation 구분과 주제 페이지 '로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가' 링크, 7절 Oliot EPCIS 행, 11절 새 질문 2건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 판독 지점 | Read Point (EPCIS readPoint) | EPCIS 이벤트가 일어난 지점을 나타내는 선택 필드이다. | 7, 17 | ref-045, ref-015 |
| new | 업무 위치 | Business Location (EPCIS bizLocation) | EPCIS 이벤트 뒤 다른 이벤트가 반박할 때까지 객체가 있다고 보는 업무상 위치를 나타내는 선택 필드이다. | 7, 6 | ref-045 |
| new | 연결 이벤트 | AssociationEvent | 물리 객체를 상위 객체나 특정 물리 위치와 연결하거나 연결을 해제한 사실을 기록하는 EPCIS 2.0 이벤트 유형이다. | 7 | ref-045 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg |
| ref-048 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-050 | Auto-ID Labs Korea(세종대학교), Byun, J. | Oliot EPCIS for GS1 EPCIS/CBV 2.0.0 (GitHub JaewookByun/epcis README) | 오픈소스 문서 | high | https://github.com/JaewookByun/epcis |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 표준 | medium | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 표준 | medium | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | CBV의 loading·unloading이 운송 수단 적재로 정의되어 있을 때 시설 안 로봇의 적재·운반·하역은 어떤 업무 단계(bizStep) 값이나 사용자 정의 어휘로 기록해야 하는가? | 7, 17 | 열림 | — |
| new | — | VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? | 7, 9 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오 | 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가 |
| 출하 | 작업 대상 | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오 | 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가 |
| 출하 | 수행 자원 | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오 | 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가 |
| 출하 | 완료·인계 | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오 | 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가 |
| 출하 | 예외·성과 | docs/topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md#4-현장-시나리오 | 로봇 적재·하역 완료를 EPCIS 인계 이벤트로 어떻게 기록할 것인가 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) | 오픈소스 | Auto-ID Labs Korea(세종대학교) | 7 | ref-050 | https://github.com/JaewookByun/epcis |

## 추가 조사 요청

- 주제 페이지 3절·7. 화물·재고·자산 식별과 추적 6절: CBV 2.0 업무 단계(bizStep) 전체 목록과 GS1의 시설 내 운반 표현 권고 — 시설 안 로봇 운반에 쓸 표준 값이 있는지 확인이 필요하다.
- 주제 페이지 3절: VDA 5050 3.0.0 state 메시지 load 절(loadId 설정 주체, loads 빈 배열·생략 규정)의 원문 글자 단위 확인 — f12가 추정으로 강등되었다.
- EPCIS 2.0 JSON 스키마의 이벤트 유형별 하위 스키마 필수 항목 — f9 삭제로 이벤트 필수 필드를 본문에 쓰지 못했다.
- GS1 EPCIS and CBV Implementation Guideline 원문 — 출하 이벤트에서 bizLocation 처리 안내를 확인해야 f6을 사실로 쓸 수 있다.
- oq-002: 국내 물류센터에서 로봇 작업 결과와 EPCIS 이벤트를 연결한 운영 사례.
- GS1 온톨로지 파일(ref-044·ref-045)과 ref.gs1.org 비준판 문구의 일치 여부 확인.
- 7. 화물·재고·자산 식별과 추적 페이지 다음 갱신: ref-023 각주와 7절 표의 '원문 미열람' 표기를 이번 실행의 원문 열람(inbox) 기록과 맞출지 확인(2차 검증 참고 사항).

## 이행한 수정 지시

- f9 제외 — 주제 페이지·7. 화물·재고·자산 식별과 추적 페이지 어디에도 EPCIS 공통 필수 항목 주장을 넣지 않았다.
- ref-046 제외 — 주제 페이지 각주·프런트매터 sources와 reference_updates에서 뺐다.
- f6 강등 — 주제 페이지 3절과 영역 페이지 6절에서 [추정]으로 쓰고 출입구 = readPoint, 그 너머 방 = bizLocation 비유만 남겼으며 출하 이벤트 bizLocation 생략 안내는 삭제했다.
- f12 강등 — 주제 페이지 3절에서 [추정]으로 쓰고 문장에 '3.0.0 원문의 해당 절 글자 단위 대조 미확인'을 병기했다.
- f20 — 주제 페이지 3절에서 [추정]을 유지하고 같은 문장에 전제 문구가 원문 대조 미확인임을 밝혔으며 SSCC를 loadId로 내려보내는 설계는 '가능성으로 생각할 수 있다'로만 썼다.
- f11 — 파라미터 구절을 '2.0.0(공식 저장소 태그)에서는 lhd·loadId·height가 선택 파라미터이고 stationType·loadType은 선택 표시가 없으며, 3.0.0에서는 모두 선택이다'로 고치고 FINISHED 정의는 [사실]로 두었다.
- ref-022 각주 — 기존 각주 정의를 그대로 쓰고 접근일 뒤 ' (원문 미열람)'을 유지했으며 reference_updates에서 source_unopened: true로 두었다.
- ref-015 각주 — 두 페이지 모두 ' (원문 미열람)'을 유지하고 reference_updates에서 source_unopened: true로 두었다.
- ref-044·ref-045 — 각주 제목 괄호와 reference_updates 요약에 초안 저장소 파일·비준판 문구 일치 미확인·발행일은 온톨로지 수정일임을 적고, 주제 페이지 3절과 영역 페이지 7절 본문에도 밝혔다.
- 영역 페이지 7절 — EPCIS·CBV 행의 출처 칸을 'GS1 공식 저장소 온톨로지 파일 확인(ref-044·ref-045), ISO/IEC 판(ref-011·ref-012)은 원문 미열람'으로 나눠 표시했다.
- 주제 페이지 — f10·f11·f13·f14·f15는 3절 '로봇·설비 신호의 식별 수준'의 짧은 두 단락으로 줄이고 2절에서 기존 주제 페이지 '로봇 관제 인터페이스의 적재·하역 보고와 화물 인계 확인'으로 링크했다.
- 직접 인용 — 두 페이지 모두 출처 원문을 직접 인용하지 않고 ref-045 발췌(f5·f7·f8)를 포함해 전부 재서술했다.
- oq-001 — 영역 페이지 11절과 주제 페이지 7절 모두 '열림'으로 두고 open_question_updates에 상태 변경을 내지 않아 두 곳이 같다.
- oq-002 — 해결로 바꾸지 않고 영역 페이지 11절과 주제 페이지 7절에서 Oliot EPCIS를 관련 자료로만 연결하며 로봇 작업 결과 연결 사례가 아님을 적었다.
- f16 — 주제 페이지 3절과 영역 페이지 6절에서 staging_outbound가 운송 픽업 대기 구역으로의 이동(출하 준비)이라 시설 안 일반 운반에 쓰기 어렵다는 점을 함께 적고 시설 내 운반 표현은 [추정]으로만 두었다.
- 2차: 7. 화물·재고·자산 식별과 추적 6절 요약 — outline 의 6절 summary 를 편집 지시문에서 절 내용 요약 2문장으로 바꿨다: readPoint·bizLocation 정의 문장은 [사실][^ref-045], CBV loading·staging_outbound 정의 한계 문장은 [추정][^ref-044][^ref-045]로 문장마다 태그 하나씩 붙였다. 분량 초과 시 코드가 이 summary 를 6절 요약과 분리 주제 페이지 '7. 화물·재고·자산 식별과 추적 — 대표 접근법과 기술' 1절에 쓴다.
- 2차: 새 주제 페이지 4절 — 표 아래 마지막 문장 끝에 [추정][^ref-048][^ref-049][^ref-022]를 붙였다.
- 2차: 새 주제 페이지 약어 — 1절에서 EPCIS(Electronic Product Code Information Services), CBV(Core Business Vocabulary, 핵심 업무 어휘), WMS(Warehouse Management System, 창고 관리 시스템)를, 3절 첫 등장 위치에서 Open-RMF(Open Robotics Middleware Framework), SSCC(Serial Shipping Container Code, 물류 단위 일련 코드)를 7. 화물·재고·자산 식별과 추적 페이지·용어집 표기대로 풀어 썼다.
- 분량 초과 자동 분리: 7. 화물·재고·자산 식별과 추적 본문 4,602자 > 기준 4,000자 → 1개 절을 주제 페이지로 옮김, 남은 본문 3,983자
