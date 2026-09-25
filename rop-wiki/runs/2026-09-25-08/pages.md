# 스토리텔러 산출 2026-09-25-08

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md | draft | 영역 심화: 3~11절 신규 작성(상위 지시의 변경·취소를 로봇 작업으로 옮기는 ISA-95·B2MML·OPC UA Job Control·VDA 5050·Open-RMF 정리), 13절 각주 11건, 페이지 상태 자동 영역 추가. 2차 수정: 5절 시작 조건·9절 마지막 문장을 사실/추정으로 나눔 |
| create | docs/topics/2026/2026-09-25-area01-s6.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "6. 대표 접근법과 기술" 절을 옮겼다(2차 수정 대상 아님, 변경 없음) |
| create | docs/topics/2026/2026-09-25-area01-s4.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 수정 대상 아님, 변경 없음) |
| create | docs/topics/2026/2026-09-25-area01-s3.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "3. 왜 중요한가" 절을 옮겼다. 2차 수정: [의견]에 '구축자 의견' 병기 |
| create | docs/topics/2026/2026-09-25-area01-s8.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: [의견]에 '구축자 의견' 병기 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 1. 주문·업무 시스템 연계 | 영역 심화: 3~11절 초안 작성(ISA-95·B2MML·OPC UA Job Control·VDA 5050·Open-RMF의 변경·취소 처리와 번역 경계), 2차 수정 반영 | run 2026-09-25-08
- 홈 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 영역 심화 초안 작성(상위 지시의 변경·취소를 로봇 작업으로 옮기는 표준·인터페이스 정리)
- 대분류 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 3~11절 초안 작성(작업 지시·작업 응답, VDA 5050 주문 갱신·취소, Open-RMF 작업 API)
- 세부영역 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 3~11절 신규 작성, 피킹 → 출하 우선순위 변경 시나리오

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 작업 지시 | Job Order (ISA-95) | ISA-95 운영 관리 활동 모델에서 실행할 작업 단위의 요청으로, 작업 요청(work request)을 이루는 구성 요소이다. | 1, 2 | ref-116 |
| new | 작업 응답 | Job Response (ISA-95) | ISA-95 에서 작업 지시에 대해 수행된 작업을 보고하는 정보이다. | 1, 2 | ref-116 |
| new | B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International 이 공개한 ISA-95(IEC/ISO 62264) 데이터 모델의 XML 스키마 구현이다. | 1, 28 | ref-114, ref-115 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-110 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json |
| ref-112 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-113 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-114 | MESA International | MESAInternational/B2MML-BatchML — README | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML |
| ref-115 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd |
| ref-116 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control (OPC 10031-4) | 표준 | medium | https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/ |
| ref-117 | Merschformann, M. 외 | Decision Rules for Robotic Mobile Fulfillment Systems | 논문 | medium | https://arxiv.org/abs/1801.06703 |
| ref-118 | 씨메스(CMES Robotics) | 물류 자동화 시스템을 이해하는 첫 걸음 : WES · WCS · WMS, 무엇이 다를까요? | 벤더 문서 | low | https://blog.cmesrobotics.ai/wes-wcs-wms |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | 1, 9, 28 | 열림 | — |
| new | — | 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | 1, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 출하 | 예외·성과 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 작업 대상 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 수행 자원 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 제약 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 완료·인계 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 예외·성과 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| B2MML (Business To Manufacturing Markup Language, 거래 프로파일 Version 0701) | 표준 | MESA International | 1, 28 | ref-114 | https://github.com/MESAInternational/B2MML-BatchML |
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4) | 표준 | OPC Foundation / ISA | 1, 2 | ref-116 | https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/ |

## 추가 조사 요청

- 3·8절: ERP·TMS·MES 와 로봇 작업을 연계한 실제 사례와 SCOR 관점 자료가 없어 '왜 중요한가'와 '대표 연구와 자료'의 근거가 얇다 — 학술·표준·정부 자료 조사 필요.
- 6절: VDA 5050 3.0.0 주문 메시지에 우선순위 필드가 있는지 미확인 — 명세·json_schemas 확인 필요.
- 5절 예외·성과: 진행 중 작업 취소·재지시가 처리량·시간·비용에 주는 영향의 출처 있는 수치가 없다.
- 3·9절: 국내 물류센터의 WMS·WES·WCS 와 로봇 연동 역할 분담에 대한 공공기관·학술 자료(현재 벤더 블로그 1건뿐) 조사 필요.
- 7절: OPC 10031-4 원문 열람과 v1.00/v2.00 판별 차이 확인 필요(현재 검색 요약 기준).
- 참고문헌 id ref-110~ref-118 은 이전 브리프가 다른 출처에 쓴 적이 있어 퍼블리셔의 등록 시 충돌 확인 필요(1차 검증 지적).
- 퍼블리셔 담당: 자동 분리 주제 페이지의 9. 검증 노트가 1차 판정·건수 형식이 아닌 한 줄 문구로 생성된다(2차 검증 지적).

## 이행한 수정 지시

- f5 '최早 시작 시각' 오기 — 6절에서 '가장 이른 시작 시각(unix_millis_earliest_start_time)'으로 썼다.
- f4 문구 — 3절과 7절에서 '외부 IT 시스템(예: WMS·ERP)과의 인터페이스는 범위 밖으로 둔다'로 고쳐 썼다.
- f2·f3 단서 — '요약 도구 경유'·'글자 단위 일치 미확인' 단서를 옮기지 않았고, 6절에서 ORDER_UPDATE_FOLLOWING_CANCEL 을 '취소 뒤 갱신을 거부하는' 오류로 설명하며 '주문 거부·취소 관련 오류 유형'으로 묶어 썼다.
- f12 메서드 목록 — 6·7절에서 'Store·StoreAndStart·Update·Abort·Pause·Resume 등의 메서드'로 쓰고 '온라인 참조 v2.00 기준, 판별 차이 미확인'을 명시했다.
- f10 기준 판 — 4·7절과 reference_updates 에 'Version 0701(저작권 표기 2023)' 기준을 적었다.
- f14 — 4·5절에서 '[추정] 벤더 주장' 을 병기하고 우선순위 자동 재정렬 세부를 빼고 WMS(창고 업무 관리)–WES(WMS 작업 지시를 바탕으로 장비·작업 순서 조정)–WCS(장비 실시간 제어) 역할 구분까지만 썼다.
- f18 — 9절에서 [추정]으로만 쓰고, 작업대 배정·재고 할당을 원문 9장 표의 외부 연계 열이 아닌 표 아래 추정 문장으로 분리했으며, 원문 2장 'WES·WCS·FMS·ROP의 책임은 겹칠 수 있다'와 9장 '경계는 제품 전략에 따라 이동할 수 있다' 문단을 [분류원문]으로 함께 제시했다.
- f15·f16·f17 — [추정]을 유지하고 3절에서 '이번 검색 범위에서 확인되지 않았고, 이는 부재가 확인된 것은 아니다'로 썼으며 단정 표현을 쓰지 않았다.
- 각주 — ref-116·ref-117·ref-118 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 세 항목에 source_unopened: true 를 넣었으며, ref-031·ref-110~ref-115 에는 붙이지 않았다.
- 5절 — 흐름 단계 '피킹 → 출하'를 명시하고 출하 우선순위 변경(f14·f16)과 피킹 중 취소(f17)를 시작 조건·제약·완료·인계·예외·성과 칸에 넣었으며, 첫 서술 문장에서 수치 없는 설명용 가상 시나리오임을 밝혔다.
- 용어집 — '작업 지시(Job Order)'·'작업 응답(Job Response)'을 glossary_updates 에 내며 설명에 ISA-95 용어집 항목과의 연결을 적고 sources 를 ref-116 로 두었다(원문 미열람 명시).
- 2차: 5절 시작 조건 칸 — 'B2MML로는 CHANGE·CANCEL 동사에 해당한다. [사실]'을 'B2MML 거래 동사에는 CHANGE·CANCEL이 있다. [사실][^ref-115] 이 변경·취소는 그 동사에 대응하는 것으로 보인다. [추정][^ref-115]'로 나눴다.
- 2차: 9절 — 마지막 문장을 'VDA 5050은 외부 IT 시스템 인터페이스를 범위 밖으로 둔다. [사실][^ref-031]'과 '따라서 상위 연계는 ROP 쪽에서 설계해야 할 것으로 보인다. [추정][^ref-031]'으로 나눴다.
- 2차: 주제 페이지 docs/topics/2026/2026-09-25-area01-s3.md 3. 본문 — '… 서로 다른 이야기를 하게 된다(구축자 의견). [의견]'으로 의견 주체를 병기했다.
- 2차: 주제 페이지 docs/topics/2026/2026-09-25-area01-s8.md 3. 본문 — '… 구분하는 출발점으로 쓸 수 있다(구축자 의견). [의견]'으로 의견 주체를 병기했다.
