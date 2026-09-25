# 스토리텔러 산출 2026-09-25-13

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md | draft | 섹션 3~11 신규 작성(로봇 인터페이스의 주문 갱신·취소·일시정지·되감기, ISA-95 작업 지시·B2MML 거래 동사, 동적 주문 피킹 연구, 피킹 → 출하 시나리오, ROP 경계, 열린 질문 3건), 페이지 상태 표식 추가 |
| create | docs/topics/2026/2026-09-25-area01-s4.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "4. 핵심 개념과 용어" 절(1,341자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area01-s8.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "8. 대표 연구와 자료" 절(1,257자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area01-s6.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "6. 대표 접근법과 기술" 절(1,257자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area01-s11.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "11. 열린 질문" 절(988자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area01-s7.md | draft | 자동 분리: 1. 주문·업무 시스템 연계 의 "7. 관련 표준·프레임워크·오픈소스" 절(831자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 1. 주문·업무 시스템 연계 | 3~11절 신규 작성: 로봇 인터페이스의 주문 갱신·취소·일시정지·되감기, ISA-95 작업 지시·B2MML 거래 동사, 동적 주문 피킹 연구, 피킹 → 출하 시나리오, ROP 경계, 새 열린 질문 3건 | run 2026-09-25-13
- 홈 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 3~11절 신규 작성(출고 우선순위 변경 시 VDA 5050·Open-RMF 의 변경 수단, ISA-95 작업 지시, 동적 주문 피킹 연구, 열린 질문 3건)
- 대분류 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 3~11절 신규 작성(진행 중 로봇 작업의 갱신·취소 수단과 상위 지시 번역, ROP 경계, 열린 질문 3건)
- 세부영역 최근 업데이트: 2026-09-25 — 1. 주문·업무 시스템 연계: 영역 심화로 3~11절 신규 작성(참고문헌 ref-125~ref-137 신규, ref-002·ref-031·ref-110·ref-111 재사용)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 작업 지시 | Job Order (ISA-95) | ISA-95 계열에서 하위 실행 계층이 수행할 작업 단위의 요청으로, OPC UA for ISA-95 Job Control 은 이를 저장·시작·갱신·일시정지·중단하는 메서드를 둔다. | 1, 2, 28 | ref-130, ref-131 |
| new | 웨이브리스 출고 지시 | Waveless Order Release | 주문을 큰 묶음(웨이브)으로 모아 내리지 않고 도착·여유 용량에 따라 연속으로 현장에 내려보내는 출고 지시 방식이다. | 1, 14 | ref-134 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-002 | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 기사 | medium | https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json |
| ref-128 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | high | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-131 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 표준 | medium | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 논문 | medium | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 논문 | medium | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 |
| ref-135 | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 표준 | medium | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf |
| ref-136 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 논문 | medium | https://www.mdpi.com/2076-3417/15/13/7235 |
| ref-137 | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 기사 | low | https://news.mt.co.kr/mtview.php?no=2025012116183583251 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | 1, 14 | 열림 | — |
| new | — | ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | 1, 9, 28 | 열림 | — |
| new | — | 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | 1, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 작업 대상 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 수행 자원 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 제약 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 완료·인계 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 피킹 | 예외·성과 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 출하 | 시작 조건 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |
| 출하 | 제약 | docs/categories/a-business-supply-chain-design/01-order-and-business-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 1. 주문·업무 시스템 연계 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) | 표준 | OPC Foundation / ISA | 1, 2, 28 | ref-130 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |

## 추가 조사 요청

- 5·9절: TMS 연계(운송 마감·도크 배정)와 MES 생산 지시가 로봇 작업 우선순위로 내려오는 방식에 관한 1차 자료 — 브리프가 찾지 못해 출하 시작 조건을 상위 시스템 일반으로만 썼다.
- 4·5절: VDA 5050 주문 메시지의 우선순위 필드 부재(f3)를 [사실]로 쓰려면 json_schemas/order.schema 를 브리프 출처로 등록해야 한다 — 검증자가 확인했으나 브리프 출처가 아니어서 [추정]으로 두었다.
- 6절: B2MML 거래 동사(CHANGE·CANCEL·CONFIRM 등)의 의미 정의를 담은 1차 자료(ISA-95 Part 5 또는 B2MML 문서) — 스키마에는 의미 설명이 없어 번역 규칙 근거가 부족하다.
- 8·11절: 테크타카–플로틱 남이천 실증의 결과 자료와 그 밖의 국내 WMS·WES–다제조사 로봇 연동 학술·공공 자료 — 현재는 발표 기사뿐이며 oq-002 도 해결되지 않았다.
- 8절: Yu·Srinivas(2025) 두 개입형 전략의 정식 이름과 AWTD 지표의 뜻, Lorenz·Otto·Gendreau(2025)의 개입형·비개입형 구분을 원문으로 확인 — 원문 미열람이다.

## 이행한 수정 지시

- 참고문헌 id 재부여 — 브리프 id 를 ref-125~ref-137 로 바꾸고 task_state.json 은 기존 ref-111, task_new 는 기존 ref-110 을 재사용해 본문 각주·프런트매터 sources·reference_updates 에 일관되게 썼으며, ref-110·ref-111 은 reference_updates 에 넣지 않았다.
- 각주 원문 미열람 표기 — ref-002, ref-131~ref-137 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true 로 두었으며, ref-031·ref-110·ref-111·ref-125~ref-130 에는 붙이지 않았다.
- f7 오기 — 6절에서 '가장 이른 시작 시각'으로 썼다.
- f16 — 8절에서 개입 없는 협업 시스템보다 AOCT·ATT 가 좋았고 같은 비교에서 AWTD 지표는 늘었다고 쓰고 '크게'를 뺐으며, 두 전략은 '저자들은 … 제안했다고 밝혔다'로 저자 제안임을 밝혔다.
- f17 — 8절 본문과 각주, reference_updates org 를 'Lorenz, Otto, & Gendreau'(Networks, 2025)로 썼다.
- ref-002 — reference_updates 로 발행일을 2025-04-10 으로 갱신하고 13절 각주 발행일도 2025-04-10 으로 썼다.
- 인용 — ref-031 직접 인용은 4절의 'the base cannot be changed' 한 번만 두고 f1·f5·f6 은 재서술했으며, ref-125 는 직접 인용하지 않았다.
- f9·f10 — 새 각주 없이 ref-111·ref-110 을 달았고 10절에서 2. 공정·워크플로 모델링과 연결했다.
- f19 — 8절에서 REST·MQTT·VDA 5050 향후 과제를 '저자들은 … 설계했다고 기술한다'로 쓰고 성과 수치를 붙이지 않았다.
- f20 — 5·8절에서 '2025년 1월 보도된 협력 발표이며 실증 결과는 미확인'을 명시하고 5절에서는 가상 시나리오와 분리한 발표 사례로만 두었으며, oq-002 는 열림으로 두고 해결 처리하지 않았다.
- f21 — 3·5·6절 서술에서 VDA 5050 PRIORITY 구역을 언급하지 않았다.
- 용어집 — B2MML 은 신규 등록하지 않고 '작업 지시(Job Order)'·'웨이브리스 출고 지시(Waveless Order Release)'만 glossary_updates 에 냈다.
- 열린 질문 — 3건을 open_question_updates 에 new 로 등록하고, 2번 질문과 oq-014·oq-001 의 관계는 11절에서 열린 질문 페이지 링크로만 밝혔다.
- 분량 초과 자동 분리: 1. 주문·업무 시스템 연계 본문 8,847자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,985자
