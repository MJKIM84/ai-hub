# 스토리텔러 산출 2026-09-25-51

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | draft | q2-02 답함(3절 소제목 신설), 새 질문 q2-07·q3-08·q3-09, 4·6·7·8·9절과 상태 줄 갱신. 2차: q2-07 행 제기 근거 칸을 'f15' 로 정정 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.4 → v0.5: 진행 상태 외부 표현 원천 메모(초안 → 확정), 배정 외부 표현 대응 메모(확정 유지), 6절 질문 2건 추가·선행 의존 질문 보강(2차 변경 없음) |
| update | docs/ideas/nl-task-chatbot.md | draft | 4절에 '작업·배정 결과를 표현하는 표준·형식' 소절 신설(이 위키 구성 비교표, 초안 대비 빠진 항목, 임무 기술 형식 비교 연구), 평가 데이터(q2-03) 미조사 명시. 2차: ref-608 각주 발행일을 2024-06-18 로 정정(각주를 직접 넣으려 전체 content 로 보냄) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6. 살아있는 산출물 링크: 초안 v0.5 와 아이디어 2 4절(q2-02 표준·형식 비교) 진행 상황 갱신(2차 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 2 | q2-02 답함(실행 2026-09-25-43 이 다룬 같은 질문의 반영 재시도), 업무 분해·배정 설계 초안 v0.4→v0.5(진행 상태·배정 외부 표현 메모), 새 질문 q2-07·q3-08·q3-09; 같은 URL 이 이전 실행에서 ref-111·ref-505(task_state.json), ref-569(compose), ref-230·ref-507(MassRobotics JSON), ref-570(dsl.md), ref-571(BehaviorTree.CPP), ref-572(HDDL), ref-116(Filippone 외)로 쓰였을 수 있어 퍼블리셔 URL 병합 확인이 필요하다 | run 2026-09-25-51
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: q2-02(작업·배정 결과를 표현하는 표준·형식과 빠진 것) 답함, 업무 분해·배정 설계 초안 v0.5, 후속 질문 3건
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2(중심 영역 13. 작업 배정 — MRTA): Open-RMF 작업 상태의 배정 결과·배정 과정 표현과 배정 근거 기록 공백을 정리했다(세부영역 반영 제안 4건)
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: Open-RMF assigned_to·dispatch 상태, VDA 5050 배정 기능·주문 단위, 배정 근거 기록 필요를 7. 관련 표준·프레임워크·오픈소스 반영 제안으로 냈다

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 계층적 작업 네트워크 | Hierarchical Task Network (HTN) | 복합 작업을 미리 정한 분해 방법으로 하위 작업 네트워크로 나누어 결국 실행 가능한 기본 동작의 순서에 이르게 하는 자동 계획 방식이다. | 14, 13, 2 | ref-604 |
| new | 계층 도메인 정의 언어 | Hierarchical Domain Definition Language (HDDL) | PDDL 을 확장해 작업·분해 방법과 하위 작업의 부분 또는 전체 순서를 기술하는 계층적 작업 네트워크 계획 문제의 공통 기술 언어이다. | 14, 13 | ref-604 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | medium | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-600 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-602 | CNCF Serverless Workflow (serverlessworkflow/specification GitHub) | Serverless Workflow Specification — dsl.md | 오픈소스 문서 | high | https://github.com/serverlessworkflow/specification/blob/main/dsl.md |
| ref-603 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — README | 오픈소스 문서 | high | https://github.com/BehaviorTree/BehaviorTree.CPP |
| ref-604 | Höller, D., Behnke, G., Bercher, P., Biundo, S., Fiorino, H., Pellier, D., & Alford, R. | HDDL – A Language to Describe Hierarchical Planning Problems | 논문 | medium | https://arxiv.org/abs/1911.05499 |
| ref-605 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 표준 | medium | https://www.omg.org/spec/BPMN/2.0.2/ |
| ref-606 | Pettinari, S. (FaMe 공식 저장소, UNICAM PROS) | FaMe — a BPMN-driven framework for Multi-Robot System development (GitHub README) | 오픈소스 문서 | high | https://github.com/SaraPettinari/fame |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P.(GSSI) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-608 | IEEE Standards Association | IEEE 1872.1-2024 — IEEE Standard for Robot Task Representation | 표준 | medium | https://standards.ieee.org/ieee/1872.1/6993/ |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IEEE 1872.1-2024 Standard for Robot Task Representation | 표준 | IEEE Standards Association | 5, 28, 14 | ref-608 | https://standards.ieee.org/ieee/1872.1/6993/ |
| Serverless Workflow (Open Workflow Specification) DSL | 오픈소스 | CNCF Serverless Workflow | 2, 14 | ref-602 | https://github.com/serverlessworkflow/specification/blob/main/dsl.md |
| HDDL (Hierarchical Domain Definition Language) | 프레임워크 | Höller 외(IPC 2020 계층 계획 부문) | 14, 13 | ref-604 | https://arxiv.org/abs/1911.05499 |
| FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) | 오픈소스 | Pettinari, S. (UNICAM PROS) | 2, 13 | ref-606 | https://github.com/SaraPettinari/fame |

## 추가 조사 요청

- 단계 2 페이지 3절 q2-02·초안 6절: IEEE 1872.1-2024 본문(또는 공식 OWL·구현 지침 P1872.1.1 자료)에서 작업 분해·선후 의존·배정 대상을 표현하는 개념 이름 — q2-07 에 답하고 업무·작업·배정 개념과 대조하기 위해 필요하다.
- 초안 6절 진행 상태 대응 질문: OPC UA for ISA-95 작업 제어의 작업 상태 기계(JobState) 상태 이름 목록 — 초안의 네 값과 Open-RMF status·dispatch 값과의 대응 규칙을 정하기 위해 필요하다.
- 단계 2 페이지 3절 플릿 사이 선후(q3-09·oq-049): VDA 5050 waitForTrigger–trigger 를 다른 플릿·설비 과정과의 선후 동기화에 쓴 공개 구현·사례 — 현재 사례 미확인이다.
- 단계 2 페이지 3절 BPMN 행: BPMN 2.0.2 명세 원문의 수행자·자원 배정 절 번호와 순서 흐름 정의 — 현재 검색 요약 범위이며 원문 미열람이다.
- 단계 2 페이지 4절 한국 자료: 로봇 작업·임무 기술 형식이나 작업 지시 표현을 다룬 KS 표준·국내 연구(한국어 검색 확대) — 한국 자료 우선 규칙에 따라 필요하다.
- 아이디어 2 4절·단계 2 완료 조건: 해석·분해 정확도 평가용 지시–정답 작업 쌍 데이터셋(q2-03) — 단계 2 완료 조건의 남은 항목이다.
- 퍼블리셔 확인 요청: 아이디어 페이지는 2차 수정(ref-608 각주 발행일)을 반영하려고 각주 정의까지 포함한 전체 content 로 보냈다. 퍼블리셔가 참고문헌에서 각주 정의를 다시 만들어 덧붙이면 ref-608 발행일이 '2024' 로 되돌아가거나 정의가 중복될 수 있으므로, 이미 정의된 각주는 다시 만들지 않도록 확인해 달라. URL 병합으로 ref-600·ref-602·ref-603·ref-604 를 이전 id 로 합칠 때 참고문헌 페이지·일일 로그 링크가 깨지지 않는지도 확인해 달라.

## 이행한 수정 지시

- f18 범위 축소 — 단계 2 페이지 3절 '제조사가 다른 플릿 사이 작업 선후' 첫 항목과 초안 6절 선행 의존 질문을 '로봇 관제·보고 형식(Open-RMF 복합 작업·작업 상태, VDA 5050, MassRobotics)과 ISA-95 작업 제어 노드셋에서 찾지 못했다'로 고치고 BPMN 순서 흐름·Serverless Workflow do·fork·HDDL 하위 작업 순서는 순서를 표현하나 수행 플릿에 묶는 필드는 확인되지 않았다고 병기했다. B2MML 의존 유형은 용어집 링크와 oq-013 으로 연결했고 [추정] 유지, oq-049 는 해결로 바꾸지 않았다.
- f4 — VDA 5050 항목의 앞부분(관제의 주문 배정 기능, 노드–간선 그래프 구간·하위 주문, 외부 IT 시스템 인터페이스 제외)은 [사실]로, '업무·작업 수준 구조나 배정 근거를 담는 메시지'는 '이번에 읽은 3.0.0 명세 범위에서 확인되지 않았다'는 별도 문장 [추정]으로 썼다.
- f5·f18 — VDA 5050 의 관제를 곧바로 ROP 로 쓰지 않고 'ROP 가 VDA 5050 관제 역할을 맡는 구성에서는 ROP 몫, 제조사 관제에 맡기는 구성(9. 로봇·제조사 관제 연동)에서는 제조사 관제 몫'으로 조건을 붙이고 범위 경계 페이지를 링크했다. q3-09 질문 문장에도 같은 조건을 넣었다.
- f9 — 본문 표기를 'OMG BPMN 2.0.2 명세(2014-01)'로 맞추고 ref-605 각주 접근일 뒤에 ' (원문 미열람)'을 붙였다.
- f10 — FaMe 기준일을 '2023, Robotics and Autonomous Systems 160권 104322; README 표기 2022'로 적고 협업 다이어그램·실행 환경 세부는 미확인으로 두었다.
- f14 — ref-604 각주는 arXiv 판 제목을 그대로 쓰고 본문에 AAAI 2020 게재판 제목을 병기했으며 원문 미열람을 표시했다.
- f15 — IEEE 1872.1-2024 발행일을 2024-06-18(IEEE SA 발행 기관 소개 기준)로 적고 바로 뒤 문장에 '표준 본문(유료)은 열람하지 못해 작업 분해·배정·의존 표현 방식은 미확인'을 두었다. 5. 로봇 능력·작업 온톨로지 반영 제안에도 같은 단서를 달았다.
- f16 — 판 표기를 'v1 2026-03, v2 2026-08-17'로 적었다. 저자의 '표준·합의된 형식이 없다'는 평가 문장은 브리프 finding 에 없어 본문에 쓰지 않았다.
- f7 — 설비 ID 구절을 '설비·물리 자산 데이터형의 ID 는 클래스 또는 개별 대상을 가리킬 수 있다' 수준으로 썼다.
- 인용 — ref-031·ref-111·ref-600 을 포함해 모든 출처의 영어 원문 구절을 직접 인용하지 않고 한국어로 재서술했다(필드 이름·값 이름만 그대로 표기).
- 원문 미열람 표시 — ref-604·ref-605·ref-116·ref-608 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-031·ref-130·ref-111·ref-600·ref-230·ref-602·ref-603·ref-606 은 원문을 연 출처로 두었다.
- 참고문헌 id — reference_updates 에 브리프 id(ref-111~ref-608)를 쓰고, changelog_entry 에 이전 실행 id(ref-111·ref-505, ref-569, ref-230·ref-507, ref-570, ref-571, ref-572, ref-116)와의 퍼블리셔 URL 병합 확인 필요 문구를 남겼다.
- 온톨로지 초안 — 두 변경을 반영해 v0.4 → v0.5 로 올리고 H1 '(v0.5)', 프런트매터 ontology_version '0.5', track_updates.ontology_draft_version '0.5' 를 맞췄다(상태 줄은 auto:page-status 마커이므로 퍼블리셔가 프런트매터 값으로 채운다). 진행 상태는 Open-RMF status 대표 값·12개 표기, dispatch 5개 값(canceled_in_flight 포함), ISA-95 JobState·실제 시작·종료 시각 메모를 더하고 초안 → 확정, 배정은 Open-RMF assigned_to·dispatch 상태와 VDA 5050 주문 수신 로봇 대응 메모를 더하고 확정 유지했으며, 필드 부재 부분(f3·f19)은 속성 정의가 아닌 [추정] 문장으로만 적었다.
- 초안 6절 — 진행 상태 네 값과 외부 값의 대응 규칙 질문을 새로 두고, 플릿 사이 작업 선행 의존(f18, oq-049)은 기존 '작업 / 선행 의존한다 / 작업' 질문에 합쳤으며, IEEE 1872.1-2024 작업 개념과의 대응(f15, 본문 미열람) 질문을 더했다.
- 단계 2 페이지 — 2절 q2-02 를 답함·2026-09-25-51·#q2-02 로 바꾸고 3절에 '### q2-02 … {#q2-02}' 소제목을 두었다. 6절 두 행을 미충족, 검증 판정 '미충족 · 미승인'으로, 아래 줄을 지시 문구 그대로 썼고, 상태 줄을 열린 질문 5건·답한 질문 2건으로 맞췄다.
- 새 질문 — backlog_updates 에 q3-08(단계 3, origin f17), q3-09(단계 3, origin f18, 'ROP 가 VDA 5050 관제 역할을 맡는 구성' 조건 포함), q2-07(단계 2, origin f15)을 등록하고 단계 페이지 2·5절에도 실었다.
- 아이디어 2 4절 — '작업·배정 결과를 표현하는 표준·형식' 소절의 비교표가 이 위키가 구성한 표이며 출처 표·그림을 옮긴 것이 아님을 [추정]과 함께 밝히고, 평가 데이터(q2-03) 미조사를 절 머리와 소절 끝에 적었다.
- 세부영역 — 13. 작업 배정 — MRTA, 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링, 5. 로봇 능력·작업 온톨로지 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, 14. 작업 순서·스케줄링 제안의 f18 은 범위를 좁힌 판으로 썼다.
- 2차: ref-608 각주 발행일 — docs/ideas/nl-task-chatbot.md 끝의 [^ref-608] 정의 발행일을 '2024' 에서 '2024-06-18' 로 고쳐 reference_updates·단계 2 페이지·초안 페이지와 맞췄다(자동 각주 재생성으로 되돌아가지 않도록 이 페이지를 전체 content 로 보냈다).
- 2차: q2-07 제기 근거 — docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md 2절 질문 목록 표 q2-07 행의 제기 근거 칸을 'f15, 실행 2026-09-25-51' 에서 'f15' 로 고쳤다(실행 id 는 5절 표에 그대로 둠).

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.5
- 트랙 로그 항목: 답한 질문: q2-02(작업·배정 결과를 표현하는 표준·형식과 빠진 것, 근거 f1~f19; 같은 질문을 다뤘으나 반영되지 않은 실행 2026-09-25-43 의 반영 재시도) / 새 질문: q2-07(f15), q3-08(f17), q3-09(f18) / 온톨로지 변경: v0.4 → v0.5: 개념 '진행 상태 (Progress)' 외부 표현 원천 메모(Open-RMF status·dispatch 값, ISA-95 JobState·실제 시작·종료 시각) 추가·초안 → 확정(f2·f7), 개념 '배정 (Assignment)' 외부 표현 대응 메모(Open-RMF assigned_to·dispatch 상태, VDA 5050 주문 수신 로봇) 추가·확정 유지(f2·f4; 필드 부재는 추정 메모 f3·f19), 근거 실행 2026-09-25-51 / 완료 조건 평가: 미충족(부족: 아이디어 2 4절 평가 데이터(q2-03) 미조사, 작업 모델 정보 항목 일부만 반영(작업 요구 적재물 속성·완료 조건 미확정)) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링, 5. 로봇 능력·작업 온톨로지 4건 / 다음 실행 제안: q2-03, q2-07, q2-04 / 비고: ref-111~ref-116 일부가 이전 실행 id 와 같은 URL 이라 퍼블리셔 URL 병합 확인 필요, 트랙 개요 상태 줄의 현재 단계 표기(단계 1)와 진행 현황은 트랙 정의 current_stage 와 함께 사용자 확인 필요(2차 검증 지적). 2차 수정: 아이디어 페이지 ref-608 각주 발행일, 단계 2 페이지 q2-07 제기 근거 칸 정정
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 5, 답함 2, 완료 조건 미충족 (q2-02 답함, 업무 분해·배정 설계 초안 v0.5)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-02 | 답함 | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md#q2-02 | — | — | — |
| q2-07 | 열림 | — | IEEE 1872.1-2024 로봇 작업 표현 온톨로지는 작업 분해·선후 의존·배정 대상을 어떤 개념으로 표현하며, 업무 분해·배정 설계 초안의 업무·작업·배정 개념과 어떻게 대응하는가? (q2-02 에서 파생) | 2 | f15 |
| q3-08 | 열림 | — | ROP 가 업무→작업 분해 구조를 내부에 둘 때 BPMN·Serverless Workflow·HDDL 같은 기존 형식을 표준 표현으로 채택할지, 자체 작업 모델 스키마를 두고 Open-RMF 복합 작업·VDA 5050 주문으로 변환할지, 변환 때 배정 근거·확인 여부는 어디에 남기는가? (q2-02 에서 파생) | 3 | f17 |
| q3-09 | 열림 | — | ROP 가 VDA 5050 관제 역할을 맡는 구성에서 Open-RMF 복합 작업의 단계와 VDA 5050 waitForTrigger–trigger 를 조합해 제조사가 다른 플릿 사이 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 집행할 수 있는가, 트리거 누락·시간 초과 때 누가 복구하는가? (q2-02 에서 파생) | 3 | f18 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 작업 상태 스키마는 배정 결과를 assigned_to(그룹·이름)로, 배정 과정을 queued·selected·dispatched·failed_to_assign·canceled_in_flight 의 dispatch 상태로 표현한다(f2). VDA 5050 3.0.0 은 주문 배정을 관제 최소 기능으로 두되 주문 단위는 로봇 한 대의 노드–간선 그래프 구간이다(f4). 표준 형식의 배정 결과는 누가 맡았는지만 남겨, 최근접 배정과 다른 기준의 전체 효과를 비교하려면 ROP 가 배정 근거·목적함수 값을 따로 기록해야 할 것으로 보인다(f19, 추정, oq-052 연결). |
| 2 | 7. 관련 표준·프레임워크·오픈소스 | OPC UA for ISA-95 작업 응답의 실제 시작·종료 시각·작업 상태·실적 필드(f7), BPMN 2.0.2 의 사람 수행자·잠재 담당자·자원 배정 식(f9, 원문 미열람), BPMN 기반 다중 로봇 개발 틀 FaMe(f10), Serverless Workflow DSL 의 순차·병렬 작업·시간 초과·일정(f11), 임무 기술 형식 네 가지 비교 연구(f16, 원문 미열람). |
| 14 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 복합 작업의 순서 있는 단계(f1), HDDL 의 하위 작업 부분·전체 순서(f14, 원문 미열람), VDA 5050 waitForTrigger–trigger 동작(f5). 확인한 로봇 관제·보고 형식과 ISA-95 작업 제어 노드셋에서는 제조사가 다른 플릿 작업 사이 선행 의존 필드를 찾지 못했고, 워크플로·계획 형식은 순서를 표현하나 수행 플릿에 묶는 필드는 확인되지 않았다(f18 범위 축소판, 추정, oq-049·oq-013 연결). |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | 로봇 작업 지식의 표현·추론·교환을 위한 온톨로지 표준 IEEE 1872.1-2024(2024-06-18 발행)와 구현 지침 P1872.1.1(f15). 표준 본문(유료)은 열람하지 못해 작업 분해·배정·의존 표현 방식은 미확인이라는 단서를 함께 싣는다. |
