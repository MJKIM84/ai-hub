# 리서치 브리프 2026-09-25-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-09 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 2. 공정·워크플로 모델링 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 페이지 각주 0건(용어집의 SCOR·ISA-95·EPCIS 항목만 이 영역에 연결됨)
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음

## 조사 질문

1. ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [분류원문]
2. 업무 흐름을 작업 단계·선후관계·완료 조건으로 표현하는 표준 모델(BPMN, ISA-95/IEC 62264와 그 XML 구현 B2MML, SCOR)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)
3. 선후관계·병렬·대기 같은 제어 흐름을 교착 없이 설계했는지 형식적으로 점검하는 방법(워크플로 넷의 건전성 등)은 무엇인가? (섹션 6·8 겨냥)
4. 로봇 오케스트레이션 쪽 도구(Open-RMF 작업·단계, VDA 5050 동작 상태, BPMN 엔진 기반 다중 로봇 연구)는 작업 단계와 완료·실패를 어떻게 표현하는가? (섹션 5·6·7·8 겨냥)
5. 실행된 공정을 주문·화물·로봇 여러 객체에 걸친 이벤트 로그로 남겨 분석하는 표준(OCEL 2.0)은 무엇을 담는가? (섹션 8·10 겨냥)
6. 공정·워크플로 모델링에서 ROP가 직접 맡을 부분과 WMS·ERP·로봇 내부 제어에 맡길 부분의 경계는 어디인가? (섹션 9 겨냥)
7. 국내 제도·자료는 물류센터 처리 과정을 어떤 단계로 나누어 평가하는가? (한국 자료 우선 규칙, 섹션 3·5 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO/IEC 19510은 OMG의 BPMN(Business Process Model and Notation, 비즈니스 프로세스 모델 및 표기법) 2.0.x를 공개 규격(PAS) 절차로 국제표준화한 것이며, BPMN은 업무 분석가부터 구현 개발자·운영 관리자까지 이해할 수 있는 프로세스 표기법을 목표로 한다. | ref-055 | 아니오 | medium | 2013 | — | 원문 미열람 |
| f2 | [추정] | Camunda 8 문서는 BPMN 메시지 대기 지점(수신 작업·메시지 중간 이벤트)이 활성화되면 메시지 이름과 상관 키(correlation key)로 구독을 만들고, 들어온 메시지를 이 구독에 맞춰 공정 인스턴스에 연결하며, 유지 시간(TTL) 동안 메시지를 보관하고 같은 이름·키·메시지 ID의 중복 메시지는 거부한다고 설명한다. | ref-056 | 아니오 | medium | 2026-09-25 | 완료·인계 | 벤더 주장 |
| f3 | [추정] | BPMN 모델에서 로봇 운반을 하나의 작업 단계로 두고 그 뒤에 WMS의 인수 확인 메시지를 기다리는 수신 단계를 두어 작업 id나 화물 식별자로 상관시키면, ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 완료 조건을 가진 연속 단계로 표현할 수 있을 것으로 보인다. | ref-055, ref-056, ref-044 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |
| f4 | [사실] | IEC 62264-3:2016(ISA-95 Part 3)은 수준 4(업무 계획·물류)와 수준 2(공정 제어) 사이의 제조 운영 관리 활동을 생산·유지보수·품질·재고 운영 관리의 네 활동 모델로 정의하며, 재고 운영 관리는 수준 3에서 재고와 자재 이동을 조정·지시·관리·추적하는 활동이다. | ref-062 | 아니오 | medium | 2016 | — | 원문 미열람 |
| f5 | [사실] | B2MML은 MESA International이 ISA-95(IEC/ISO 62264)의 데이터 모델을 XML 스키마(XSD)로 구현한 것이며, 공식 저장소의 공통 스키마 머리말은 판 0701(2023)이고 ANSI/ISA-95.00.02-2018과 ANSI/ISA-95.00.05-2018을 기반으로 한다. | ref-060 | 아니오 | medium | 2023 | — | — |
| f6 | [사실] | B2MML의 운영 정의 스키마는 운영 세그먼트 사이 선후관계를 SegmentDependency 요소(의존 대상 DependentOperationsSegmentID)로 두고, 공통 스키마의 의존 유형은 NotFollow, PossibleParallel, NotInParallel, AtStart, AfterStart, AfterEnd, NoLaterAfterStart, NoEarlierAfterStart, NoLaterAfterEnd, NoEarlierAfterEnd, Other 값을 둔다. | ref-060, ref-061 | 아니오 | medium | 2023 | 제약 | — |
| f7 | [사실] | B2MML 공통 스키마의 자재 사용 유형(MaterialUse)에는 Consumed, Produced, Consumable, By-product Produced, Co-product Produced, Inventoried 등이 있어 공정 세그먼트가 자재를 소비하는지 생산하는지 재고로 두는지를 구분한다. | ref-060 | 아니오 | medium | 2023 | 작업 대상 | — |
| f8 | [추정] | ISA-95 세그먼트 의존 유형(예: AfterEnd, NotInParallel, NoLaterAfterEnd)을 창고 작업에 쓰면 ‘검수 종료 후 적치 시작’, ‘같은 도크의 상차와 하차 병행 금지’, ‘하역 종료 후 일정 시간 안에 입고 확정’ 같은 선후·병행·시간 제약을 단순 순서보다 세밀하게 표현할 수 있을 것으로 보인다. | ref-060, ref-061 | 아니오 | low | 2026-09-25 | 적치 / 제약 | — |
| f9 | [사실] | Open-RMF 문서는 작업(task)을 단계(phase)를 만들어 내는 객체로 보고, 배송 작업을 픽업 지점 이동·화물 수령·하역 지점 이동·화물 인도·복귀 단계로 나누며, Compose 유형으로 단계·활동의 순서를 직접 조합하게 하고, 여러 층 배송의 승강기 요청 같은 필수 단계는 필요할 때 자동으로 더한다. | ref-053 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f10 | [사실] | Open-RMF API의 작업 상태 스키마는 작업 상태를 uninitialized, blocked, error, failed, queued, standby, underway, delayed, skipped, canceled, killed, completed 12개 값으로 두고, 작업의 단계를 완료(completed)·진행(active)·대기(pending)로 나눠 보고하며 단계마다 이벤트 목록과 소요 시간 추정값을 담는다. | ref-054 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f11 | [사실] | VDA 5050 3.0.0 명세는 drop 동작의 완료(FINISHED)를 적재물이 이동로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의해, 로봇 쪽 완료가 화물의 물리적 인도까지만 가리킨다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f12 | [사실] | Open-RMF 배송 작업에서 로봇은 하역 지점에서 IngestorResult를 받을 때까지 IngestorRequest를 보내며, IngestorResult는 요청 id·결과를 보낸 워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)만 담는다. | ref-023, ref-049 | 아니오 | medium | 2026-09-25 | 입고 / 완료·인계 | — |
| f13 | [사실] | GS1 CBV 2.0 온톨로지는 업무 단계 arriving을 ‘객체가 위치에 도착함’, receiving을 ‘객체를 위치에서 받아 수령자의 재고에 더함’, accepting을 ‘객체의 점유 또는 소유가 바뀜’, storing을 ‘위치 안에서 보관 구역으로 넣고 빼는 이동’으로 서로 다르게 정의한다. | ref-044 | 아니오 | medium | 2021-09-30 | 입고 / 완료·인계 | — |
| f14 | [추정] | 로봇 관제 규격의 완료 신호(VDA 5050 drop FINISHED, Open-RMF IngestorResult SUCCESS)는 CBV의 arriving 수준의 물리적 인도만 나타내고, 수령자 재고 반영(receiving)과 점유·소유 변경(accepting)은 다른 규격이 정의하므로, 공정 모델은 ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 단계와 완료 조건으로 두고 둘을 잇는 식별 키를 명시해야 할 것으로 보인다. | ref-031, ref-049, ref-044 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |
| f15 | [사실] | ASCM의 SCOR 모델 Fulfill 프로세스는 B2C 이행(F1)을 Pick Product(F1.3), Pack Product(F1.4), Stage Product(F1.5) 등을 거쳐 Obtain Proof of Delivery or Customer Acceptance(F1.11)로 끝나는 단계로 나누고, B2B 이행(F2)에도 같은 계열의 단계(F2.3 피킹, F2.12 배송 증빙·고객 인수)를 둔다. | ref-066 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | 원문 미열람 |
| f16 | [사실] | 워크플로 넷(workflow net)은 워크플로의 제어 흐름을 모델링·분석하는 표준적 방법으로 쓰이는 페트리 넷의 한 부류이며, 그 건전성(soundness) 속성은 도메인 지식 없이 찾을 수 있는 교착(deadlock)·라이브락(livelock) 같은 이상이 없음을 보장한다. | ref-063, ref-064 | 아니오 | medium | 2022 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | OCEL(Object-Centric Event Log) 2.0은 이벤트와 여러 객체(주문·품목·출하 등) 사이 관계를 명시적으로 기록하는 이벤트 로그 교환 표준으로, 객체 간 관계, 관계의 한정자(qualifier), 시간에 따라 바뀌는 객체 속성을 담고 SQLite·XML·JSON 세 교환 형식을 둔다. | ref-065 | 아니오 | medium | 2024-03 | 예외·성과 | 원문 미열람 |
| f18 | [추정] | 로봇 하역 한 건이 작업·로봇·팔레트·주문 여러 객체에 동시에 걸리는 ROP 실행 기록은 단일 사례 중심 로그보다 OCEL 2.0 같은 객체 중심 로그 구조에 맞아, 설계한 공정 모델과 실제 실행 흐름의 차이를 분석하는 근거가 될 수 있을 것으로 보인다. | ref-065, ref-054 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f19 | [사실] | Corradini 외(2023)의 FaMe는 BPMN 요소 일부와 모델링 지침으로 다중 로봇 임무를 기술하고, 그 협업 모델을 로봇별 실행 프로세스로 자동 분할해 각 로봇에 내장한 ROS 2 연동 BPMN 엔진이 분산 실행하게 하는 프레임워크이다. | ref-057 | 아니오 | medium | 2023 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 스위스 장크트갈렌 대학 저장소의 경험 보고는 BPMN 2.0을 지원하는 Camunda Platform 7로 자율이동로봇 TurtleBot 4 Pro 두 대를 조율하면서, 업무 프로세스 관리 시스템(BPMS)을 로봇 안에서 돌리는 구성과 외부 노트북에서 돌리는 구성을 비교했다. | ref-058 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f21 | [사실] | arXiv 2603.15427 비교 연구는 로봇 임무 기술 형식으로 행동 트리(Behavior Tree), 상태 기계, 계층적 작업 네트워크(HTN), BPMN 네 가지를 임무 수준에서 제어 구조·표현력·한계·도구 지원 기준으로 비교하고 전문가 검증으로 결과를 확인했다. | ref-059 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f22 | [추정] | 연계 대상: 로봇 내부의 동작 실행 흐름(행동 트리·상태 기계로 구현되는 주행·파지 등)은 제조사 쪽 영역이고, ROP의 공정·워크플로 모델은 업무 단계(BPMN·ISA-95·SCOR 수준)와 로봇 작업 단위(Open-RMF 단계, VDA 5050 동작) 사이의 순서·대기·완료 조건을 맡는 층으로 나누는 것이 분류 원문 9장 경계와 맞아 보인다. | ref-059, ref-053, ref-055 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f23 | [사실] | 국토교통부 스마트물류센터 인증은 입고·보관·피킹·출고 등 물류처리 과정별 첨단·자동화 정도를 보는 기능영역과 시설 구조 성능·성과관리 체계·정보시스템 도입 수준을 보는 기반영역으로 평가해 1~5등급을 부여한다. | ref-067 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 연계 대상: 수령자 재고에 더하는 재고 반영(CBV receiving)과 재고·자재 이동을 추적하는 재고 운영 관리(IEC 62264-3)는 WMS·MES 같은 상위 업무 시스템의 책임이며, ROP는 운반 완료 이벤트를 전달하고 인수 확인을 기다리거나 예외로 분기하는 공정 단계까지만 맡는 구조가 될 것으로 보인다. | ref-044, ref-062 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |

### 근거 발췌

- **f1**: 검색 요약: ISO/IEC 19510 은 OMG BPMN 2.0.1 을 PAS 로 제출·처리해 ISO/IEC JTC1 이 준비했고, 2.0.2 가 2013년판으로 발행됨. 주 목표는 'readily understandable by all business users' 인 표기법. OMG 원문 미열람.
- **f2**: 벤더 주장: 공식 문서 원본 "A message is not sent to a process instance directly. Instead, the message correlation is based on subscriptions that contain the message name and the correlation key." TTL 버퍼링, 메시지 ID 로 중복 거부. (발행일 미확인, 확인일 기준)
- **f3**: f1(BPMN 표기)·f2(메시지 상관 구조)·f13(CBV receiving·accepting 정의)에서 도출한 추론. 이 구성을 물류 로봇에 적용한 표준·사례는 확인하지 못함.
- **f4**: ISO 소개 요약: four formal models — production, maintenance, quality and inventory operations management. 재고 운영 관리는 'coordinate, direct, manage and track inventory and material movement'. 원문 미열람.
- **f5**: B2MML-Common.xsd 머리말: 'Copyright 2023 MESA International, Version 0701'. ISA-95 Part 2(객체 모델 속성)·Part 5(업무–제조 트랜잭션) 2018판 기반. 저장소 README 는 ERP·SCM 과 MES·제어 시스템 통합용이라 밝힘.
- **f6**: B2MML-OperationsDefinition.xsd: SegmentDependency(SegmentDependencyType), DependentOperationsSegmentID. B2MML-Common.xsd DependencyType 열거값 11개. 두 파일 모두 MESA 저장소라 독립 교차 아님.
- **f7**: B2MML-Common.xsd MaterialUseType 열거: Consumable, Consumed, Produced, By-product Produced, Co-product Produced, Yield Produced, Material Consumed, Material Produced, 샘플 3종, Inventoried, Other.
- **f8**: f6 의 열거값을 물류 흐름 단계에 대응시킨 추론. ISA-95 는 제조 운영 관리 표준이며, 창고 물류 작업에 이 의존 유형을 적용한 사례는 확인하지 못함.
- **f9**: task_new 원본: task 는 'an object that generates phases'. 공개 API 단계 GoToPlace, PickUp, DropOff, PerformAction. Compose 는 'a sequence of phases'. RequestLift 같은 단계는 'automatically added to a task when necessary'. (발행일 미확인, 확인일 기준)
- **f10**: task_state.json: status 열거 12개, completed 'An array of the IDs of completed phases', active 'The ID of the active phase', pending 배열, 단계별 events·estimate_millis·시작·종료 시각. (발행일 미확인, 확인일 기준)
- **f11**: 3.0.0 main 사전 정의 action 표: drop "Load has left the mobile robot and mobile robot reports new load state." 이번 실행에서 다시 열지 않음. (재인용: 2026-09-25-07)
- **f12**: IngestorResult.msg 원본(이번 실행 재열람): request_guid, source_guid, uint8 status ACKNOWLEDGED=0·SUCCESS=1·FAILED=2. 요청 반복 흐름은 ref-023. 두 출처 모두 Open-RMF 라 독립 교차 아님. (재인용: 2026-09-25-03)
- **f13**: CBV.ttl 원문 receiving: "an object is being received at a location and is added to the receiver's inventory." accepting 은 possession and/or ownership 변경, arriving 은 위치 도착, storing 은 moved into and out of storage.
- **f14**: f11·f12(로봇·워크셀 완료 신호에 재고·당사자 정보 없음)와 f13(CBV 단계 정의)을 대응시킨 추론. 두 계층을 잇는 표준 매핑은 oq-001 로 여전히 미확인.
- **f15**: scor.ascm.org 검색 요약: F1.3 Pick Product, F1.4 Pack Product, F1.5 Stage Product, F1.11 Obtain Proof of Delivery or Customer Acceptance; F2.4 Pack and/or Kit Product, F2.12. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f16**: 검색 요약: LICS 2022 논문은 workflow nets 가 'one of the standard ways to model and analyze workflows' 이고 soundness 검사에 쓰인다고 적음. FAC 논문 요약은 soundness 가 livelocks·deadlocks 부재를 보장한다고 적음. 둘 다 원문 미열람.
- **f17**: arXiv 2403.01975 검색 요약: OCEL 2.0 은 changes in objects, object relationships, qualifiers 를 표현하며 relational database(SQLite), XML, JSON 형식 제공. OCEL 1.0(2020) 확장. 원문 미열람.
- **f18**: f17(객체 간 관계를 담는 로그)과 f10(작업·단계 단위 상태 보고)에서 도출한 추론. 로봇 오케스트레이션 로그를 OCEL 로 분석한 사례는 확인하지 못함.
- **f19**: 검색 요약: collaboration 은 ROS2 에 맞게 설정되고 'automatically split into single executable processes, one for each robot'; 각 로봇이 BPMN 엔진 내장. Robotics and Autonomous Systems 160, 104322. 공식 저장소 README 로 서지만 확인.
- **f20**: 검색 요약: 두 로봇이 각자 로컬 BPMS 인스턴스로 서로 상호작용, ROS2 내비게이션과 공유 지도로 사전 좌표 간 이동. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f21**: 검색 요약: 'focusing on mission-level descriptions rather than robot software development', 사람 업무 흐름·외부 장치 통합 지원 정도가 형식마다 다름. 원문 미열람.
- **f22**: f1·f9·f21 과 분류 원문 9장('로봇 자체 지능·제어'는 외부 연계)을 대응시킨 추론. 두 층의 상태를 잇는 표준 매핑은 확인하지 못함.
- **f23**: 국가물류통합정보센터 인증제 안내 검색 요약: 기능영역(물류처리 과정별 자동화)·기반영역(구조적 성능, 성과관리, 정보시스템) 구분, 1등급~5등급. 세부 배점 미확인. (발행일 미확인, 확인일 기준)
- **f24**: f4·f13 정의와 분류 원문 9장 '상위 업무 시스템'(ROP 는 주문·재고 제약을 받아 실행하고 결과 반영, 전사 재고정책은 외부) 경계를 대응시킨 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-053 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-054 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-055 | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | 표준 | medium | 2026-09-25 | https://www.omg.org/spec/BPMN/2.0/About-BPMN | 예 |
| ref-056 | Camunda | Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://docs.camunda.io/docs/components/concepts/messages/ | 아니오 |
| ref-057 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 | 예 |
| ref-058 | University of St. Gallen (Alexandria 저장소), 저자 미확인 | Autonomous Mobile Robots with Business Process Management Systems at the Edge | 미확인 | 논문 | medium | 2026-09-25 | https://alexandria.unisg.ch/server/api/core/bitstreams/3b1a80df-f89a-46d2-bbf3-118aac764282/content | 예 |
| ref-059 | arXiv:2603.15427 저자(미확인) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-060 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 아니오 |
| ref-061 | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd | 아니오 |
| ref-062 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/67480.html | 예 |
| ref-063 | Formal Aspects of Computing 게재 논문(저자 미확인) | Soundness of workflow nets: classification, decidability, and analysis | 2011 | 논문 | medium | 2026-09-25 | https://doi.org/10.1007/S00165-010-0161-4 | 예 |
| ref-064 | LICS 2022 논문(arXiv:2201.05588) 저자 미확인 | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2201.05588 | 예 |
| ref-065 | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 2024-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.01975 | 예 |
| ref-066 | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | 표준 | medium | 2026-09-25 | https://scor.ascm.org/processes/fulfill/F1.3 | 예 |
| ref-067 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 예 |

### 출처 요약

- **ref-023**: 원문 미열람. Open-RMF 의 적재(dispenser)·하역(ingestor) 워크셀 연동과 요청·결과 메시지 흐름을 설명하는 공식 문서(이번 실행은 재인용).
- **ref-031**: 원문 미열람. VDA 5050 공식 명세의 GitHub 저장소 본문(현재 main 은 3.0.0 판). pick·drop 동작 정의와 파라미터(이번 실행은 2026-09-25-07 재인용).
- **ref-044**: GS1 공식 EPCIS 저장소의 CBV 2.0 온톨로지(Turtle). 업무 단계(arriving·receiving·accepting·storing 등)·처분 상태의 정의 문구를 담는다. 초안 저장소라 ref.gs1.org 게시판과 판이 다를 수 있다.
- **ref-049**: Open-RMF 하역 워크셀 결과 메시지 정의. 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다.
- **ref-053**: Open-RMF 작업을 단계(phase)로 구성하는 방식, 배송·청소·순회·Compose 작업 유형, 자동으로 더해지는 필수 단계, 작업 요청 API 를 설명하는 공식 문서(mdBook 원본).
- **ref-054**: Open-RMF API 의 작업 상태 JSON 스키마. 작업 상태 12개 값, 완료·진행·대기 단계, 단계별 이벤트와 소요 시간 추정을 정의한다.
- **ref-055**: 원문 미열람. BPMN 2.0 명세의 OMG 공식 소개 페이지. ISO/IEC 19510 으로도 발행된 업무 프로세스 표기법과 실행 의미를 정의한다.
- **ref-056**: BPMN 엔진 Camunda 8 의 메시지 상관(메시지 이름·상관 키 구독, TTL 버퍼링, 메시지 ID 중복 거부) 동작을 설명하는 공식 문서의 저장소 원본.
- **ref-057**: 원문 미열람. BPMN 모델링 지침으로 다중 로봇 임무를 기술하고 로봇별 실행 프로세스로 분할해 ROS 2 연동 BPMN 엔진으로 분산 실행하는 FaMe 프레임워크 논문(Robotics and Autonomous Systems 160).
- **ref-058**: 원문 미열람. Camunda Platform 7 BPMS 로 TurtleBot 4 Pro 두 대를 조율하고 BPMS 를 로봇 안·밖에 두는 구성을 비교한 경험 보고.
- **ref-059**: 원문 미열람. 행동 트리·상태 기계·HTN·BPMN 을 로봇 임무 기술 형식으로 비교하고 전문가 검증을 거친 프리프린트.
- **ref-060**: ISA-95 의 XML 구현 B2MML(판 0701) 공통 스키마. 세그먼트 의존 유형·자재 사용 유형 등 열거값을 정의한다.
- **ref-061**: B2MML 운영 정의 스키마. 운영 세그먼트, 세그먼트 의존(SegmentDependency), 자재 명세·사용 유형 요소를 정의한다.
- **ref-062**: 원문 미열람. 수준 3 제조 운영 관리를 생산·유지보수·품질·재고 운영 관리 네 활동 모델로 정의한 ISA-95 Part 3 국제판의 ISO 소개 페이지.
- **ref-063**: 원문 미열람. 워크플로 넷 건전성 개념의 여러 변형을 분류하고 결정 가능성과 분석 방법을 정리한 논문.
- **ref-064**: 원문 미열람. 워크플로 넷이 워크플로 모델링·분석의 표준적 방법임을 전제로 건전성 판정의 계산 복잡도를 다룬 논문(ACM/IEEE LICS 2022).
- **ref-065**: 원문 미열람. 이벤트–객체·객체–객체 관계와 한정자, 변하는 객체 속성을 담는 객체 중심 이벤트 로그 표준 OCEL 2.0 명세.
- **ref-066**: 원문 미열람. SCOR Digital Standard 의 Fulfill 프로세스 단계(피킹·포장·대기·배송 증빙 또는 고객 인수 등) 정의 페이지.
- **ref-067**: 원문 미열람. 물류처리 과정별 자동화 수준(기능영역)과 시설·성과관리·정보시스템(기반영역)으로 물류센터를 평가해 등급을 주는 국내 인증제 안내.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f14·f15·f23(로봇 완료와 업무 완료의 차이, SCOR 이행 단계가 인수로 끝남, 국내 인증이 처리 과정별로 평가) / 섹션 4: f1(BPMN)·f6(세그먼트 의존)·f9(작업·단계)·f13(arriving·receiving·accepting)·f16(워크플로 넷·건전성)·f17(OCEL) / 섹션 5: 입고 완료·인계 f11·f12·f13·f14·f3, 적치 제약 f8, 출하 완료·인계 f15 — 흐름 단계와 여섯 항목 명시 / 섹션 6: f1·f2·f3·f6·f8·f9·f16·f19·f20·f21 / 섹션 7: f1(BPMN·ISO/IEC 19510), f4·f5·f6·f7(IEC 62264-3·B2MML), f9·f10(Open-RMF 작업·상태 스키마), f15(SCOR), f17(OCEL 2.0), f2(Camunda, 벤더 주장 병기) / 섹션 8: f16·f17·f19·f20·f21 / 섹션 9: f22·f24(로봇 내부 동작 흐름과 재고 확정은 연계 대상, ROP는 단계 순서·대기·완료 조건) / 섹션 10: 1. 주문·업무 시스템 연계(f4·f5·f24), 7. 화물·재고·자산 식별과 추적(f13·f14), 9. 로봇·제조사 관제 연동(f11·f12), 12. 명령·작업 실행의 신뢰성(f2·f10), 14. 작업 순서·스케줄링(f6·f8), 4. 성과·경제성·프로세스 개선(f17·f18), 23. 시험·형식 검증·벤치마크(f16) / 섹션 11: open_questions_new 3건과 기존 oq-001 연결(f14). 다음 실행 후보: 1. 주문·업무 시스템 연계 페이지 7절에 B2MML(f5) 반영 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 비즈니스 프로세스 모델 및 표기법 | Business Process Model and Notation (BPMN) | OMG가 정하고 ISO/IEC 19510으로도 발행된 업무 프로세스 표기법으로, 작업·이벤트·게이트웨이·흐름으로 업무 단계와 순서를 그리고 실행 의미를 정의한다. |
| 워크플로 넷 | Workflow Net (WF-net) | 시작·끝 장소를 하나씩 가진 페트리 넷으로 워크플로의 제어 흐름을 표현하며, 건전성 검사로 교착·라이브락 같은 설계 이상을 찾는 데 쓰인다. |
| 객체 중심 이벤트 로그 | Object-Centric Event Log (OCEL) | 하나의 이벤트를 주문·품목·출하 같은 여러 객체와 관계로 함께 기록하는 프로세스 마이닝용 이벤트 로그 표준 형식이다. |
| B2MML | Business To Manufacturing Markup Language (B2MML) | MESA International이 ISA-95(IEC 62264)의 데이터 모델을 XML 스키마로 구현한 교환 형식이다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | 관련 영역: 2. 공정·워크플로 모델링, 1. 주문·업무 시스템 연계 | 근거: f14 | 종류: 일반
- ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | 관련 영역: 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링 | 근거: f8 | 종류: 일반
- 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | 관련 영역: 2. 공정·워크플로 모델링, 9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 실패: 표준·규격별로 발행 기관 한 곳의 자료만 확인(B2MML 두 파일, Open-RMF 두 출처는 같은 발행 주체)
    - f1 BPMN 명세 본문(OMG formal PDF) 원문 미열람 — 게이트웨이·수신 작업의 토큰 의미는 제3자 설명만 봐서 finding 으로 내지 않음
    - f4 IEC 62264-3 의 활동 세부 목록(정의 관리·배차·실행·추적 등)은 제3자 논문 요약에만 있어 finding 으로 내지 않음
    - ISA-88 절차 모델(절차·단위 절차·운영·단계)은 위키·블로그 요약만 확인되어 finding 으로 내지 않음
    - f15 SCOR Fulfill 단계 번호는 scor.ascm.org 검색 요약만 확인
    - f16 ref-063·ref-064 저자 목록 미확인, 워크플로 넷 정의 세부는 강의 슬라이드 요약이라 인용하지 않음
    - f17 ref-065 저자 목록 미확인
    - f19 FaMe 는 공식 저장소 README 로 서지(RAS 160, 104322)만 원문 확인, 기능 설명은 검색 요약
    - f20 ref-058 저자·발행일 미확인
    - f23 스마트물류센터 인증 세부 평가 항목·배점 미확인
    - ref-031·ref-023 은 이번 실행에서 다시 열지 않아 재인용
- 범위 경계 위반 의심:
    - f22: 로봇 내부 행동 트리·상태 기계는 분류 원문 9장 '로봇 자체 지능·제어'의 외부 연계 영역이므로 '연계 대상: '으로 표시함
    - f24: 재고 확정·재고 운영 관리는 상위 업무 시스템(WMS·MES) 영역이므로 '연계 대상: '으로 표시함
- 한계: fetch_mode mirror_only(web_fetch_available: false): raw.githubusercontent.com 공식 저장소 원문(Open-RMF task_new 원본·task_state.json·IngestorResult.msg, B2MML 스키마 2건, GS1 CBV.ttl, Camunda 문서 원본, FaMe README)은 열어 fetched=true 로 표시했다. OMG·ISO·ASCM·arXiv·ScienceDirect·국가물류통합정보센터 페이지는 원문 미열람이라 신뢰도 상한 medium. 모든 finding 이 단일 발행 주체 근거여서 교차 확인 0건이다. 검색 22회/30, 신규 출처 15건/15(ref-053~ref-067, next_ref_id 기준; 신규 출처 상한 도달로 ISA-88/PackML 원문 출처와 FaMe README 를 출처로 넣지 못함). 재사용 출처 4건(ref-023, ref-031, ref-044, ref-049). 주의: 이전 브리프 2026-09-25-04·05·06 도 ref-053~ref-061 을 다른 출처에 부여했으나 참고문헌 목록에 없으므로 실행 컨텍스트 next_ref_id 를 따랐다 — id 충돌 여부는 퍼블리셔 확인 필요. 한국 자료는 국토교통부 스마트물류센터 인증 안내 1건뿐이며, 국내 BPMN·물류 로봇 공정 모델링 학술 자료는 한·영 검색에서 찾지 못했다(검색된 국내 WMS 자료는 벤더 블로그·개인 저장소라 제외). 정정 요청·이 영역 열린 질문·priority 지정 없음. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. Camunda 문서의 기능 설명(f2)은 벤더 주장으로 표시했다.
