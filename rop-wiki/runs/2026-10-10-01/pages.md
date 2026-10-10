# 스토리텔러 산출 2026-10-10-01

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-and-workflow-modeling.md | draft | 3절 첫 문단을 원문 정의(CBV 세 단계·VDA 5050 3.0.0 drop FINISHED·IngestorResult 기본 필드)와 [의견]으로 나눠 다시 씀, 5절 시나리오 1 문장 수정·IngestorResult 범위 한정과 사례 3(현장 유형 기타, FaMe, 작업 대상 미확인) 추가, 6·7·8·11절 보강(각 보강 소절 첫 줄에 2026-09-25 분리 주제 페이지 링크 유지)과 10절 연결 덧붙임, 13절 각주 갱신(ref-031·ref-044·ref-049 접근일, ref-116 발행일·접근일·열람)과 새 각주 1건(ref-1423). ref-366·ref-404·ref-502·ref-1424·ref-1425 는 자동 분리 뒤 분리 주제 페이지의 출처 절에만 남는다 |
| create | docs/topics/2026/2026-10-10-area24-s11.md | draft | 자동 분리: 24. 작업·워크플로 모델링 의 "11. 열린 질문" 절(1,498자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area24-s6.md | draft | 자동 분리: 24. 작업·워크플로 모델링 의 "6. 대표 접근법과 기술" 절(1,442자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area24-s3.md | draft | 자동 분리: 24. 작업·워크플로 모델링 의 "3. 왜 중요한가" 절(1,339자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area24-s7.md | draft | 자동 분리: 24. 작업·워크플로 모델링 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,291자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area24-s8.md | draft | 자동 분리: 24. 작업·워크플로 모델링 의 "8. 대표 연구와 자료" 절(886자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-10 | 24. 작업·워크플로 모델링 | 3절 하역 완료와 인수·재고 반영을 원문 정의별로 분리, 5절 시나리오 1 문장 수정과 사례 3(현장 유형 기타) 추가, 6·7·8·10·11절 보강(BPMN 2.0.2·취소 후 정리·rmf_task_sequence·VDA 5050 blockingType·rmf_fleet_adapter 2.14.0·Filippone 외 v2·FaMe, 2026-09-25 분리 주제 페이지 링크 유지), 13절 각주 갱신. 비고: ref-1423~ref-1425 는 실행 2026-10-09-26 브리프의 다른 출처 id 와 같아 id 충돌 여부 퍼블리셔 확인 필요 | run 2026-10-10-01
- 홈 최근 업데이트: 2026-10-10 — 24. 작업·워크플로 모델링: 로봇 하역 완료와 업무상 인수·재고 반영의 원문 정의를 나누고, 기타 현장(농업·지상 로봇 협업 시뮬레이션) 사례와 BPMN 2.0.2·rmf_task_sequence·VDA 5050 3.0.0 blockingType 근거를 보강
- 대분류 최근 업데이트: 2026-10-10 — 24. 작업·워크플로 모델링: 3절 완료 신호 정의 분리, 5절 기타 현장 사례 추가, 6·7·8·10·11절 보강과 각주 갱신
- 세부영역 최근 업데이트: 2026-10-10 — 24. 작업·워크플로 모델링: 3절 첫 문단을 CBV·VDA 5050 3.0.0·IngestorResult 원문 정의와 [의견]으로 다시 쓰고, 5절 사례 3(현장 유형 기타, FaMe)과 6·7·8·10·11절 보강을 더함(2026-09-25 분리 주제 페이지 링크 유지)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 수신 작업 | Receive Task (BPMN) | 외부 참여자가 보낸 메시지가 도착할 때까지 기다리다가 메시지를 받으면 완료되는 BPMN 작업 유형이다. | 24 | ref-502 |
| new | BPMN 보상 | Compensation (BPMN) | 이미 성공적으로 끝난 단계의 결과가 더는 필요 없을 때 그 효과를 되돌리는 처리를 별도 활동으로 표현하는 BPMN 개념이다. | 24, 32 | ref-502 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 표준 | high | https://www.omg.org/spec/BPMN/2.0.2/ |
| ref-1423 | University of Camerino PROS Lab | FaMe — A BPMN-driven Framework for Multi-Robot System Development (공식 페이지·사용 지침) | 정부·연구기관 | medium | https://pros.unicam.it/fame/ |
| ref-366 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 (tag 2.14.0) — rmf_fleet_adapter/CHANGELOG.rst | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst |
| ref-1425 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.1.0) — VDA5050_EN.md | 표준 | high | https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇이 이미 하역한 뒤 작업이 취소되면, 로봇 쪽 정리 단계 완료와 업무상 인수 취소(재고 반영 취소)를 어떤 완료 조건으로 나눠야 하는가? | 24, 32 | 열림 | — |
| new | — | Open-RMF rmf_task_sequence 의 Bundle 이벤트와 BPMN 병렬 게이트웨이 합류의 의미 차이를 자동으로 검사하거나 변환하는 공개 도구가 있는가? | 24, 54 | 열림 | — |
| new | — | 운영 정책 버전이 바뀔 때 이미 시작한 워크플로 인스턴스가 이전 정책을 유지하는지 새 정책으로 옮기는지에 대한 공개 운영 기준이 있는가? | 24, 57 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 기타 | 수행 자원 | docs/categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시 | 24. 작업·워크플로 모델링 |
| 물류창고 | 완료·인계 | docs/categories/planning-and-optimization/task-and-workflow-modeling.md#5-적용-사례-현장-유형-명시 | 24. 작업·워크플로 모델링 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| BPMN 2.0.2 (OMG formal/13-12-09) | 표준 | OMG(Object Management Group) | 24 | ref-502 | https://www.omg.org/spec/BPMN/2.0.2/ |

## 추가 조사 요청

- 분리 주제 페이지(2026-09-25-area02-s6·s7·s8·s11) 본문이 입력에 없고 하루 갱신 상한(2)도 있어 직접 고치지 못했다(예산으로 미룸). 다음 갱신 실행에서 이 페이지들을 입력으로 넣어 s8 의 ref-116 각주(발행일 2026-03 → 2026-03-16, 접근일 2026-10-10, '원문 미열람' 삭제)와 s7 표의 BPMN 행(ref-502 추가)을 고쳐야 한다. 이번 보강은 세부영역 6·7·8·11절에 더했고, 각 보강 소절 첫 줄에 이 페이지들로 가는 링크를 두었다.
- 3·5절: 한국어 검색과 국내 자료(국내 물류센터·제조 현장의 운반 완료와 인수 확정 분리, 작업 모델링 사례)가 없다. 공통 규칙 8 충족을 위해 다음 갱신에서 보강이 필요하다.
- 5절: 병원·제조 공장·상업 시설 등 다른 현장 유형의 실제 작업 모델링 사례가 없다. 시작 조건·제약·완료·인계·예외·성과를 채울 공개 사례가 필요하다.
- 5절 사례 3: FaMe 농업·지상 로봇 협업 시나리오의 작업 대상(물건·공간·정보·사람), 시작 조건·제약·완료 조건·예외 처리, 실외 현장 여부, 실물 로봇 실험 규모를 확인할 원문(시나리오 패키지·논문)이 필요하다.
- 6절: rmf_task_sequence Bundle 이벤트의 병렬·합류 의미를 API 문서 원문으로 확인해야 한다(f15 한정 해소).
- 7절: rmf_fleet_adapter #543 에서 고친 단계 건너뛰기 요청 키의 실제 이름을 풀 리퀘스트 원문으로 확인해야 한다.
- 11절 oq-001: 로봇 하역 완료를 EPCIS 인계 이벤트로 옮기는 공개 구현 사례를 실제로 검색해야 한다(이번 브리프는 검색하지 않아 '확인 못 함').
- 트랙 반영 제안 2건 가운데 이번 브리프로 뒷받침되지 않은 항목(OPC UA for ISA-95 작업 응답, BPMN 2.0.2 사람 수행자·자원 배정, Serverless Workflow DSL, Isaac Mission Dispatch, PlanSys2, DART-LLM, LTLf→행동 트리, Open-RMF 워크플로 다이어그램, crossflow)은 다음 실행에서 검증한 뒤 반영해야 한다.

## 이행한 수정 지시

- 3절 첫 문단 — 기존 [추정] 문장('arriving 수준의 물리적 인도')을 지우고 f1 [사실][^ref-044]·f2 [사실][^ref-031](3.0.0 §6.2.3.2 표 5)·f3 [사실][^ref-049](기본 정의 필드 한정)로 나눠 적은 뒤 f4 를 [의견](이 위키의 판단)으로 덧붙이고 '이 구성을 적용한 표준·사례는 확인하지 못했다' 한정을 유지했다.
- 5절 시나리오 1 — 'CBV로 보면 arriving에 가깝다' 문장을 f27 [의견]으로 바꿔 drop 완료를 arriving·receiving 으로 단정하지 않고 업무 측(WMS) 확인으로 단계를 정한다고 썼다(완료·인계 칸의 IngestorResult 문장도 f3 대로 기본 정의 필드로 한정했다).
- 5절 — 사례 3(현장 유형 기타, 농업·지상 로봇 협업 시뮬레이션, 67. 기타 현장 링크)을 새로 두고 f7·f8·f24 를 작업 대상·수행 자원·서술에 놓았으며, 시작 조건·제약·완료·인계·예외·성과는 '미확인'으로 두고 f9 를 [의견](이 위키의 판단)으로 적었다. site_matrix_updates 의 site_type 은 '기타'로 냈다.
- f17 — 7절 보강에서 'SINGLE 은 2.1.0 명세에는 없고 3.0.0 명세에는 있다'로 쓰고, 두 판 사이 다른 판 미확인과 같은 발행 계열 두 판의 대조라 교차 확인이 아님을 밝혔다.
- 의견 주체 — f4·f9·f12·f18·f20·f23·f25·f27 을 쓴 [의견] 문장마다 '이 위키의 판단이다'를 넣었다(3·5·6·7·8·11절).
- ref-116 — 세부영역 13절 각주를 발행일 2026-03-16·접근일 2026-10-10 으로 고치고 '(원문 미열람)'을 뺐으며, 8절 보강에 v2(2026-08-17)·IEEE Transactions on Software Engineering (2026) 게재 정보와 f22 연구 방법(83명 요청·29개 응답, 인터뷰 3명·서면 1명, 처리량 측정 아님)을 적었다. 8절 분리 주제 페이지(2026-09-25-area02-s8)는 본문이 입력에 없고 갱신 상한이 있어 직접 고치지 못해 reference_updates 로 참고문헌 ref-116 을 갱신하고 additional_research_requests 에 남겼다.
- ref-031 — 새 문장(3절 f2, 7절 f16)에 '3.0.0 태그판(main 브랜치 판과 다를 수 있다)'을 밝히고 발표일은 쓰지 않았으며, 13절 각주 접근일을 2026-10-10 으로 고쳤다.
- f19·f20 — 7절 보강에 '개별 패키지 rmf_fleet_adapter 2.14.0(2026-09-26)'으로 적고 Open-RMF 배포판 버전이 아니라고 밝혔으며, 고친 키의 이름은 '미확인'으로 두었다.
- f15·f26 — 6절에 'Bundle 이벤트의 병렬·합류 의미는 원문 미확인', 11절 oq-001 에 '공개 구현 사례는 검색하지 않아 확인 못 함' 한정을 남기고 '없다'로 단정하지 않았다.
- 범위 경계 — 3절과 11절에 수령자 재고 편입(CBV receiving)·EPCIS 이벤트 생성·재고 확정을 '연계 대상: 상위 업무 시스템(WMS 등)'으로 표시하고 ROP 몫을 완료 조건 구분과 대기·분기로 한정했다.
- 연결 — f16~f18 은 7절에서 20. 로봇·제조사 관제 연동, f10~f12 는 6절에서 32. 예외 복구·재계획·업무 연속성, f1~f4 는 3절에서 17. 작업 대상·자산 식별과 인계 추적과 번호·이름으로 연결하고 10절에 덧붙였으며 프런트매터 related_areas 에 32·67 을 더했다.
- 6절 분리 주제 페이지 — 본문이 입력에 없어 해당 페이지는 고치지 않고(기존 Camunda 문장 ref-113 과 ref-112 각주는 그 페이지와 5절에 그대로 남음) 세부영역 6절에 f5(ref-502)·f6 을 덧붙였으며, Camunda 고유의 메시지 보존 시간·중복 거부 동작을 BPMN 표준 보장으로 넓히지 않는다고 적었다.
- 7절 분리 주제 페이지 — 그 페이지 표는 입력에 없어 고치지 못하고, 세부영역 7절에 BPMN 2.0.2(ref-502, formal/13-12-09, 2014-01) 행을 포함한 보강 표를 더했으며 VDA 5050 blockingType(f16·f17)과 rmf_fleet_adapter 2.14.0(f19)을 기준일과 함께 적었다.
- 트랙 반영 제안 2건 — 이번 브리프로 뒷받침되는 FaMe(f7·f8·f24, 5·8·11절)와 임무 기술 형식 비교 연구(f21~f23, 8절)만 반영하고, 나머지 항목은 본문에 넣지 않고 '제안'으로 남겼다(additional_research_requests 에 기록).
- 11절과 open_question_updates — oq-001(f26·f27)·oq-014(f24·f25)는 '열림'을 유지한 채 11절에 부분 근거만 달았고(상태가 바뀌지 않아 update 는 내지 않음), 새 질문 3건을 관련 영역 24·32 / 24·54 / 24·57 로 등록했다.
- glossary_updates — '수신 작업 (Receive Task (BPMN))'을 신규로, 보상 후보는 'BPMN 보상 (Compensation (BPMN))'으로 표기하고 설명에 기존 '보상 트랜잭션 (Compensating Transaction)'과 다른 개념임과 연결을 적었다.
- 인용 — 페이지 본문에 출처 원문의 직접 인용을 넣지 않고 모두 재서술했다(ref-044·ref-031·ref-502 포함).
- reference_updates 의 ref-1423·ref-1424·ref-1425 — 브리프 id 를 그대로 쓰고 changelog_entry 비고에 'id 충돌 여부 퍼블리셔 확인 필요'를 남겼다.
- 2차: 기존 분리 주제 페이지 링크 복원 — 6·7·8·11절 패치를 append 에서 replace 로 바꿔 각 절의 기존 첫 문장을 유지하고, '### 2026-10-10 보강' 소절 첫 줄에 '이전 정리(2026-09-25)는 [24. 작업·워크플로 모델링 — 대표 접근법과 기술 / 관련 표준·프레임워크·오픈소스 / 대표 연구와 자료 / 열린 질문](../../topics/2026/2026-09-25-area02-s6·s7·s8·s11.md)에 있다.' 줄을 두어 자동 분리 뒤에도 링크가 남게 했다.
- 2차: 5절 사례 3 작업 대상 칸 — '미확인'으로 바꾸고 f24 문장(FaMe 의 모델링·구성·실행과 ROS 2 위 직접 실행, [사실][^ref-1423])을 표 아래 서술 문단으로 옮겼으며, 서술의 미확인 목록에 작업 대상을 더했다. site_matrix_updates 에서 {기타, 작업 대상}을 빼고 {기타, 수행 자원}은 유지했다.
- 2차: 6절 보강 첫 문단의 Camunda 구절 — 구체 동작 이름(메시지 보존 시간·중복 거부)을 빼고 '이전 정리의 기존 Camunda 근거 문장이 서술한 엔진 고유 동작'으로만 가리켰다.
- 2차: pages[0].diff_summary — '새 각주 6건'을 '새 각주 1건(ref-1423)'으로 고치고 ref-366·ref-404·ref-502·ref-1424·ref-1425 는 자동 분리 뒤 분리 주제 페이지의 출처 절에만 남는다고 적었다.
- 분량 초과 자동 분리: 24. 작업·워크플로 모델링 본문 10,315자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,459자
