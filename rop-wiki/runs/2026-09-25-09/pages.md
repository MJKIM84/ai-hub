# 스토리텔러 산출 2026-09-25-09

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md | draft | 섹션 3~11 신규 작성(BPMN·ISA-95/B2MML·Open-RMF 작업 단계·CBV 업무 단계·워크플로 넷·OCEL 2.0, 입고 → 적치·출하 시나리오), 페이지 상태 자동 영역 추가. 2차 수정: 5절 태그 강등 2건·예외 칸 태그 추가, 6절 요약 [의견], 프런트매터 sources 정리 |
| create | docs/topics/2026/2026-09-25-area02-s4.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차 수정: ref-120 각주와 건전성의 교착·라이브락 문장을 빼고 ref-121 근거 문장으로 줄였다 |
| create | docs/topics/2026/2026-09-25-area02-s6.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 첫 문장을 [의견] 정리로 바꾸고 ref-120 문장을 ref-121 근거 문장으로 줄였다 |
| create | docs/topics/2026/2026-09-25-area02-s7.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,105자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area02-s8.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "8. 대표 연구와 자료" 절(870자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area02-s11.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "11. 열린 질문" 절(815자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area02-s10.md | draft | 자동 분리: 2. 공정·워크플로 모델링 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다(링크는 주제 페이지 위치 기준). 2차 수정: 7번 항목 [추정] 강등, 12번 항목 두 주장 분리, 1번 항목 ref-119 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 2. 공정·워크플로 모델링 | 영역 심화 3~11절 초안 작성(BPMN·ISA-95/B2MML·Open-RMF 작업 단계·CBV 업무 단계·워크플로 넷·OCEL 2.0, 입고 → 적치·출하 시나리오, 1차 조건부 승인 수정 13건과 2차 수정 지시 9건 반영) | run 2026-09-25-09
- 홈 최근 업데이트: 2026-09-25 — 2. 공정·워크플로 모델링: 영역 심화 초안 작성. 로봇의 운반 완료와 인수 확인·재고 반영 완료를 서로 다른 단계로 표현하는 표준(BPMN, ISA-95/B2MML, Open-RMF, GS1 CBV)을 정리했다
- 대분류 최근 업데이트: 2026-09-25 — 2. 공정·워크플로 모델링: 3~11절 초안 작성(작업 단계·선후관계·완료 조건 표현 표준, 입고 → 적치·출하 시나리오)
- 세부영역 최근 업데이트: 2026-09-25 — 2. 공정·워크플로 모델링: 영역 심화 초안(3~11절) 작성, 새 열린 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 비즈니스 프로세스 모델 및 표기법 | Business Process Model and Notation (BPMN) | OMG가 정한 업무 프로세스 표기법으로, ISO/IEC 19510:2013은 OMG BPMN 2.0.1을 PAS 절차로 국제표준화한 것이다. | 2, 12 | ref-112 |
| new | 워크플로 넷 | Workflow Net (WF-net) | 워크플로를 모델링·분석하는 표준적 방법 가운데 하나로 쓰이는 페트리 넷의 한 부류이다. | 2, 23 | ref-121 |
| new | 객체 중심 이벤트 로그 | Object-Centric Event Log (OCEL) | 이벤트와 여러 객체 사이 관계, 관계의 한정자, 시간에 따라 바뀌는 객체 속성을 기록하는 이벤트 로그 교환 표준이며, 2.0판은 SQLite·XML·JSON 형식을 둔다. | 2, 4, 19 | ref-122 |
| new | B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International이 ISA-95(IEC 62264)의 데이터 모델을 XML 스키마로 구현한 교환 형식이다. | 1, 2, 14 | ref-117, ref-118 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-112 | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 표준 | medium | https://www.omg.org/spec/BPMN/2.0/About-BPMN |
| ref-113 | Camunda | Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 벤더 문서 | medium | https://docs.camunda.io/docs/components/concepts/messages/ |
| ref-114 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd |
| ref-118 | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 표준 | high | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 표준 | medium | https://www.iso.org/standard/67480.html |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 논문 | medium | https://arxiv.org/abs/2201.05588 |
| ref-122 | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 논문 | medium | https://arxiv.org/abs/2403.01975 |
| ref-123 | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 표준 | medium | https://scor.ascm.org/processes/fulfill/F1.3 |
| ref-124 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 정부·연구기관 | medium | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | 2, 1 | 열림 | — |
| new | — | ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | 2, 14 | 열림 | — |
| new | — | 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | 2, 9, 12 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 입고 | 시작 조건 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 입고 | 작업 대상 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 입고 | 수행 자원 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 입고 | 제약 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 입고 | 완료·인계 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 입고 | 예외·성과 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 적치 | 제약 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 출하 | 작업 대상 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |
| 출하 | 완료·인계 | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 2. 공정·워크플로 모델링 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| BPMN 2.0 (ISO/IEC 19510:2013) | 표준 | OMG(Object Management Group) · ISO/IEC | 2, 12 | ref-112 | https://www.omg.org/spec/BPMN/2.0/About-BPMN |
| IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 | 표준 | IEC / ISO | 1, 2 | ref-119 | https://www.iso.org/standard/67480.html |
| B2MML (Business To Manufacturing Markup Language, 판 0701) | 표준 | MESA International | 1, 2, 14 | ref-117 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd |
| OCEL 2.0 (Object-Centric Event Log) | 표준 | arXiv:2403.01975 저자(미확인) | 2, 4, 19 | ref-122 | https://arxiv.org/abs/2403.01975 |

## 추가 조사 요청

- 6·8절: 장크트갈렌 대학 Alexandria 저장소의 경험 보고(Autonomous Mobile Robots with Business Process Management Systems at the Edge, 원래 ref-115)의 실재·저자·발행일 확인 — 1차 검증에서 실재 미확인으로 삭제(f20)되어 BPMS 를 로봇 안·밖에 두는 구성 비교를 싣지 못했다.
- 3·5·7절: SCOR Fulfill 의 F1.4 Pack Product, F1.5 Stage Product, F2.3·F2.4·F2.12 단계 번호와 명칭을 scor.ascm.org 원문 또는 독립 출처로 확인 — 1차 검증에서 미확인이라 F1.3·F1.11 만 실었다.
- 4·6절: ref-120(Soundness of workflow nets, Formal Aspects of Computing 2011)의 실재와 저자 확인, 워크플로 넷 건전성이 교착·라이브락 부재를 보장한다는 정의의 확인 — 2차 검증 지시로 ref-120 과 교착·라이브락 서술을 모든 출력에서 뺐다.
- 6절: BPMN 2.0.x 명세 원문(OMG formal)에서 수신 작업·메시지 이벤트·게이트웨이의 실행 의미 확인 — 현재 메시지 대기 동작은 벤더 문서(Camunda)에만 기대고 있다.
- 6·7절: ISA-88 절차 모델(절차·단위 절차·운영·단계)과 PackML 의 공식 원문 출처 — 이번 실행은 신규 출처 상한으로 넣지 못했다.
- 3·5절: 국내 물류센터에서 로봇 운반 완료와 WMS 입고·인수 확정을 분리해 운영하는 사례, 국내 BPMN·물류 로봇 공정 모델링 학술 자료 — 한국 자료는 스마트물류센터 인증 안내 1건뿐이다.
- 5절 예외·성과: 인수 확인 지연·하역 실패가 처리량·시간·비용에 주는 영향의 출처 있는 수치 — 현재 미확인으로 두었다.
- 퍼블리셔 확인: 이전 브리프(2026-09-25-04·05·06)가 ref-110~ref-118 을 다른 출처에 부여했을 수 있어 참고문헌 id 충돌 여부 점검이 필요하다.
- 파이프라인 담당 요청: 분량 자동 분리 코드가 세부영역 절을 주제 페이지로 옮길 때 상대 링크를 새 위치 기준으로 다시 쓰지 않아 10절 분리 페이지에서 링크가 깨졌다. 분리 시 링크 경로 재작성이 필요하다.

## 이행한 수정 지시

- f1: ISO/IEC 19510:2013 표기 — 4절과 7절 표, 각주에서 'ISO/IEC 19510:2013은 OMG BPMN 2.0.1을 공개 규격(PAS) 절차로 국제표준화(채택)한 것'으로 적고 '2.0.2가 2013년판'이라는 표현은 쓰지 않았다(2.0.2 발행일은 싣지 않음).
- f2: 6절 BPMN 메시지 대기 문단과 10절 12. 명령·작업 실행의 신뢰성 항목에서 [추정]과 '벤더 주장'을 유지하고, 중복 거부를 '같은 이름·상관 키·메시지 ID의 메시지가 아직 버퍼에 있는 동안'으로 조건을 붙여 썼다.
- f6: 4절 운영 세그먼트 의존 항목과 6절 ISA-95·B2MML 소절에서 '운영 세그먼트가 SegmentDependency 요소와 DependentOperationsSegmentID 요소를 둔다'로 고쳐 부모-자식 관계를 단정하지 않았다.
- f15: 3절·5절(출하 시나리오 완료·인계)·7절 SCOR 행에서 F1.3 Pick Product와 F1.11 Obtain Proof of Delivery or Customer Acceptance(B2C 이행의 마지막 단계)만 [사실]로 쓰고 F1.4·F1.5·F2.3·F2.4·F2.12는 본문에서 뺐다.
- f16: 4절·6절·8절·10절에서 '워크플로 넷은 워크플로를 모델링·분석하는 표준적 방법 가운데 하나'를 [사실]로 두고 ref-064만 각주로 달았으며, '건전성이 교착·라이브락 부재를 보장한다'는 [추정]으로 강등하고 ref-120 각주에 '(원문 미열람)'을 유지했다.
- f20: 6·8절에 넣지 않았고 ref-058은 본문 각주와 reference_updates에서 뺐으며, 장크트갈렌 경험 보고의 실재·서지 확인을 additional_research_requests에 넘겼다.
- f21: 8절에서 '전문가 검증' 부분을 빼고 네 형식을 임무 수준에서 비교했다는 내용만 썼으며, ref-116 기관 칸을 각주와 reference_updates 모두 'Filippone, G., Pettinari, S., & Pelliccione, P.'로 등록했다.
- ref-121: reference_updates와 13절 각주의 기관 칸을 'Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022)'로 등록했다.
- f23: 3절에서 '성과관리 체계'를 빼고 기반영역을 '시설의 구조적 성능·정보시스템 도입 수준 등'으로 썼으며 reference_updates 요약도 같게 고쳤다.
- f3·f8·f14·f18·f22·f24: 모두 [추정]을 유지하고 3·5·6·8·9절의 해당 문장 안에 '이 구성을 적용한 표준·사례는 확인하지 못했다'(또는 같은 뜻의 한계)를 붙였으며, f22·f24는 9절 표의 '연계 대상:' 칸에 WMS·MES 재고 확정과 로봇 내부 행동 트리·상태 기계로만 짧게 썼다.
- 각주: ref-112·ref-114·ref-116·ref-119·ref-120·ref-121·ref-122·ref-123·ref-124 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates에 source_unopened: true를 넣었으며, ref-023·ref-031에는 붙이지 않고 요약의 '원문 미열람.' 머리말도 지웠다.
- 5절 현장 시나리오: 입고 → 적치 시나리오의 완료·인계(f11·f12·f13·f14·f3)와 제약(f8), 출하 시나리오의 완료·인계(f15의 F1.11만)를 흐름 단계명과 여섯 항목 문자열 그대로 표기하고, 설명용 가상 시나리오임을 밝히고 수치는 넣지 않았다(처리량 영향은 미확인으로 둠).
- 10절: 1. 주문·업무 시스템 연계, 4. 성과·경제성·프로세스 개선, 7. 화물·재고·자산 식별과 추적, 9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성, 14. 작업 순서·스케줄링, 23. 시험·형식 검증·벤치마크를 번호와 이름으로 연결하고, f18에 따라 19. 모니터링·이상 탐지·원인 분석도 연결했으며 프런트매터 related_areas를 [1, 4, 7, 9, 12, 14, 19, 23]으로 맞췄다.
- 분량 초과 자동 분리: 2. 공정·워크플로 모델링 본문 8,781자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,565자
- 형식 검증 재작성: docs/topics/2026/2026-09-25-area02-s10.md 본문의 세부영역 링크 8개(세부영역 폴더 기준 상대 경로라 깨짐)를 주제 페이지 위치 기준 '../../categories/<대분류 slug>/<파일>.md' 경로로 고쳤다. 내용·태그·각주는 바꾸지 않았고, 이미 분리된 결과(세부영역 본문 3,565자)를 그대로 보내 재분리가 일어나지 않게 했다.
- 2차: 세부영역 페이지 5절 시나리오 1 표 아래 'CBV로 보면 arriving에 가깝다' 문장을 [추정]으로 바꾸고 각주를 [^ref-031][^ref-049][^ref-044]로 달았다.
- 2차: 분리 페이지 2026-09-25-area02-s10.md 의 7. 화물·재고·자산 식별과 추적 항목 'CBV의 arriving·receiving·accepting 구분이 두 완료를 잇는 기준이 된다'를 [추정]으로 바꿨다.
- 2차: 세부영역 페이지 6절 요약 문장과 분리 페이지 2026-09-25-area02-s6.md 의 1. 세 줄 요약 첫 줄·3. 본문 첫 문장을 '이 위키는 이 영역의 관련 접근법을 … 네 갈래로 정리한다'로 다시 쓰고 '두 완료를 나눠 표현하는 방법' 표현을 없앴으며 태그를 [의견]으로 바꿨다(태그 뒤 괄호 없음).
- 2차: 세부영역 페이지 5절 시나리오 2 아래 '출하에서도 로봇 작업 완료와 고객 인수 사이에 업무 단계가 남는다'를 [추정]으로 바꾸고 각주를 [^ref-031][^ref-123]으로 달았다.
- 2차: ref-120 을 모든 출력에서 뺐다 — s4·s6 의 [^ref-120] 각주·각주 정의·프런트매터 sources, reference_updates 의 ref-120 항목을 지우고, s4·s6 의 교착·라이브락 문장을 ref-121 근거의 '워크플로 넷의 건전성(soundness) 판정은 그 계산 복잡도까지 다뤄지는 연구 대상이다. [사실]'로 줄였으며, 용어집 workflow-net description 에서도 교착·라이브락 문구를 뺐다.
- 2차: 세부영역 페이지 프런트매터 sources 에서 ref-114·ref-120·ref-122 를 뺐다(본문·13절 각주와 일치).
- 2차: 분리 페이지 2026-09-25-area02-s10.md 의 12. 명령·작업 실행의 신뢰성 항목을 '메시지 상관·버퍼 보관 중 중복 거부 … [추정] 벤더 주장[^ref-113]'과 'Open-RMF 작업 상태 12개 값 … [사실][^ref-111]' 두 주장으로 나눴다.
- 2차: 분리 페이지 2026-09-25-area02-s10.md 의 1. 주문·업무 시스템 연계 항목 각주에 [^ref-119]를 더하고 프런트매터 sources 와 8. 출처에 ref-119 를 넣었으며 reference_updates 의 ref-119 cited_by 에 이 페이지를 더했다.
- 2차: 세부영역 페이지 5절 시나리오 1 예외·성과 칸의 '인수 확인이 오지 않거나 하역이 실패하면 공정은 대기하거나 예외로 분기해야 한다.' 뒤에 [추정][^ref-044][^ref-119]를 붙였다.
