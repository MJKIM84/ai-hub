# 스토리텔러 산출 2026-09-25-43

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | draft | q2-02 답함(3절 소제목 신설), 상태 줄 수치·4~6·7~9절 갱신, 후속 질문 q3-08·q3-09 추가. 2차: 형식–작업 모델 대응 표 머리 문장 각주에 ref-125·ref-413 추가 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | v0.4 → v0.5: 진행 상태에 외부 표현 원천 후보 추가(초안 → 확정), 배정에 외부 표현 메모 추가(확정 유지), 6절 질문 추가(H1 버전 표기 변경 때문에 전체 content 로 보냄). 2차 변경 없음 |
| update | docs/ideas/nl-task-chatbot.md | draft | 4절에 '작업·배정 결과를 표현하는 표준·형식' 소절 신설(q2-02, 이 위키 구성 비교표 [추정]), 안내 문장 갱신, q2-03 미조사 명시. 2차: 아직 없는 용어 페이지(계층적 작업 네트워크) 링크를 글자로 바꿈 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 살아있는 산출물 링크: 초안 v0.5 반영, 아이디어 4절 q2-02 작성 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 2 | q2-02 답함(작업·배정 결과 표현 형식 비교), 업무 분해·배정 설계 초안 v0.4 → v0.5, 후속 질문 q3-08·q3-09 | run 2026-09-25-43
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: q2-02 답함 — Open-RMF·VDA 5050·ISA-95·BPMN·Serverless Workflow·HDDL·행동 트리의 작업·배정 표현을 비교했고, 배정 근거·확인 여부를 담는 형식은 찾지 못했다(추정). 업무 분해·배정 설계 초안 v0.5
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2(중심 영역 13. 작업 배정 — MRTA): 표준 형식의 배정 결과는 누가 맡았는지만 남긴다는 관찰과 배정 근거 기록 필요(추정)를 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: 7. 관련 표준·프레임워크·오픈소스 절에 Open-RMF 작업 상태의 assigned_to·디스패치 상태와 배정 근거 기록 필요(추정) 반영 제안(다음 영역 실행에서 반영)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 계층적 작업 네트워크 | Hierarchical Task Network (HTN) | 복합 작업을 미리 정한 분해 방법으로 하위 작업 네트워크로 나누어 결국 실행 가능한 기본 작업의 순서에 이르게 하는 자동 계획 방식이다. | 14, 2, 13 | ref-951, ref-116 |
| new | 계층 도메인 정의 언어 | Hierarchical Domain Definition Language (HDDL) | PDDL 을 확장해 기본 작업·복합 작업·분해 방법과 하위 작업의 순서를 기술하는 계층적 작업 네트워크 계획 문제의 공통 기술 언어이다. | 14, 2, 13 | ref-951 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | medium | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-114 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-948 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json |
| ref-949 | CNCF Serverless Workflow (serverlessworkflow/specification GitHub) | Serverless Workflow Specification — dsl.md (DSL 1.0) | 오픈소스 문서 | high | https://github.com/serverlessworkflow/specification/blob/main/dsl.md |
| ref-950 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — README | 오픈소스 문서 | high | https://github.com/BehaviorTree/BehaviorTree.CPP |
| ref-951 | Höller, D., Behnke, G., Bercher, P., Biundo, S., Fiorino, H., Pellier, D., & Alford, R. | HDDL – A Language to Describe Hierarchical Planning Problems | 논문 | medium | https://arxiv.org/abs/1911.05499 |
| ref-952 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 표준 | medium | https://www.omg.org/spec/BPMN/2.0.2/PDF |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Serverless Workflow (Open Workflow Specification) DSL 1.0 | 오픈소스 | CNCF Serverless Workflow | 2, 14 | ref-949 | https://github.com/serverlessworkflow/specification/blob/main/dsl.md |
| HDDL (Hierarchical Domain Definition Language) | 프레임워크 | Höller, D. 외 | 14, 2 | ref-951 | https://arxiv.org/abs/1911.05499 |

## 추가 조사 요청

- 단계 2 페이지 3절 q2-02 표의 VDA 5050 진행 상태 칸: VDA 5050 3.0.0 상태 메시지(state)가 주문·동작 진행을 어떤 필드로 표현하는지 이번 브리프에 없어 '이번 실행에서 보지 않음'으로 두었다. 초안 진행 상태의 외부 원천 후보를 보완하려면 필요하다.
- 업무 분해·배정 설계 초안 6절 진행 상태 대응 질문: ISA-95 작업 지시 상태 기계(OPC 10031-4)의 상태 이름을 원문으로 확인해야 초안 네 값과의 대응 규칙을 정할 수 있다.
- BPMN 2.0.2 수행자(Performer, 10.3.2절) 정의를 OMG 발행 원문으로 확인해 f9 를 [사실]로 되돌릴 수 있는지 재확인이 필요하다(1차 검증 요청).
- q2-03(해석·분해 평가용 지시–정답 작업 쌍 데이터와 공개 데이터셋)이 미조사라 단계 2 완료 조건과 아이디어 2 4절이 채워지지 않았다.
- Open-RMF rmf_task 내부 구현에 서로 다른 작업 요청 사이의 선행 의존이나 배정 근거를 보관하는 구조가 있는지 확인이 필요하다(q3-09, oq-049 관련).
- 업무 완료 조건의 표현 원천(EPCIS 이벤트 등) 확인이 필요하다(초안 6절 완료 조건 질문).
- 용어집 계층적 작업 네트워크 페이지가 게시된 뒤, 아이디어 2 4절과 HDDL 용어 설명에서 해당 용어를 링크로 되살리는 후속 갱신이 필요하다(2차 수정으로 링크를 글자로 바꿈).

## 이행한 수정 지시

- f9 강등 — 단계 2 페이지 3절 q2-02 와 아이디어 2 4절에서 BPMN 문장을 지시 문구대로 [추정]으로 고쳐 쓰고 'Performer 를 활동을 수행하거나 책임지는 자원으로 정의' 문구는 넣지 않았다.
- f3·f16·f17 선행 의존 한정 — 단계 2 페이지·아이디어 2 4절·초안 6절에서 선행 의존 부재 서술을 모두 '서로 다른 작업(작업 요청) 사이'로 한정했고, 작업 내부 사건 의존(deps)은 새 [사실] 문장으로 넣지 않았다.
- f16 BPMN 분류 — 단계 2 페이지와 아이디어 2 4절의 대응 서술·표에서 BPMN 을 '배정 대상 지정' 칸에 수행자·자원 배정 식(원문 미열람)으로 함께 적고 표 전체에 [추정] 태그와 근거 각주를 붙였다.
- f2 용어 — Open-RMF dispatch 를 모든 페이지에서 '디스패치 상태(dispatch)'로 원어 병기했고, 초안의 배치(Dispatch)·배정(Assignment) 개념과 같은 것으로 보지 않는다는 문장을 단계 2 페이지·초안 2절 아래 설명·아이디어 2 4절에 두었다.
- f15 — [의견] 문장을 'Filippone 외(2026-03, 프리프린트)의 평가에 따르면'으로 시작해 평가 주체를 문장 안에 밝혔다(단계 2 페이지, 아이디어 2 4절).
- f14 — HDDL 날짜를 'arXiv 2019-11 공개, AAAI 2020 발표'로 쓰고, IPC 2020 계층 계획 부문 공통 언어 부분은 원문 미열람 검색 요약 기준임을 별도 문장으로 병기했다(단계 2 페이지, 용어집 설명).
- 원문 미열람 표시 — ref-114·ref-116·ref-253·ref-951·ref-952 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에서 ref-951·ref-952(와 ref-114·ref-116·ref-253)에 source_unopened: true 를 넣었다. 열람 출처 7건에는 표시하지 않았다.
- 진행 상태 수정 승인 — 초안 2절 진행 상태 행의 속성 '상태 값'에 외부 표현 원천 후보(Open-RMF status 값, 디스패치 상태 값, ISA-95 JobState·실제 시작·종료 시각)를 근거 f2·f7 각주와 함께 적고 상태를 초안 → 확정으로 바꿨으며, 네 값과의 대응 규칙을 6절 새 질문으로 두었다.
- 배정 메모 승인 — 초안 2절 배정 행 정의에 지시 문구대로 외부 표현 메모([추정][^ref-111]; [사실][^ref-031])를 넣고 '로봇 토픽' 표현은 쓰지 않았으며 상태는 확정을 유지했다.
- 초안 버전 — 프런트매터 ontology_version '0.5', H1 '(v0.5)', track_updates.ontology_draft_version '0.5' 로 맞추고(page-status 표기는 자동 영역이라 퍼블리셔가 프런트매터 값으로 갱신), 1절 버전 설명에 v0.5 문장을 더했다.
- 단계 2 페이지 — 2절 q2-02 를 답함(2026-09-25-43, #q2-02)으로, 3절에 '### q2-02 … {#q2-02}' 소제목을 두고, 6절 두 조건을 미충족·'미충족 · 미승인'으로, 전환 줄을 지시 문구대로 썼으며 상태 줄을 열린 질문 4건·답한 질문 2건으로 맞췄다(상태 줄·H1 은 H2 밖이라 전체 content 로 보냄).
- 새 질문 — q3-08(origin f16)·q3-09(origin f17)를 단계 3 으로 backlog_updates 에 등록하고, q3-09 질문 문장에 oq-049 관련을 병기했으며, 단계 2 페이지 5절에 q3-08 과 q2-04 의 관계를 한 줄로 적었다.
- 세부영역 반영 — 13. 작업 배정 — MRTA, 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, 13 제안에서 VDA 5050 배정 기능은 기존 7·9절 문장과 ref-031 재사용을 명시하고 f9 는 [추정]으로 제안했다.
- 아이디어 2 4절 — '작업·배정 결과를 표현하는 표준·형식' 소절의 비교표를 이 위키가 구성한 것이라고 밝히고 [추정] 태그와 근거 각주를 붙였으며, 원 명세 표를 복제하지 않았고 q2-03 미조사를 절 머리에 명시했다.
- 용어집 — '계층적 작업 네트워크(HTN)'와 '계층 도메인 정의 언어(HDDL)'를 근거 ref-951(f14)로 glossary_updates 에 냈고, HDDL 설명에서 기존 PDDL 페이지에 연결했으며 BPMN 은 새로 등록하지 않았다.
- 2차: 아이디어 2 4절 HDDL 항목의 용어 링크 — ../glossary/hierarchical-task-network.md 링크를 링크 없는 글자 '계층적 작업 네트워크(Hierarchical Task Network, HTN)'로 바꿨고 glossary_updates 의 용어 등록은 유지했다.
- 2차: hddl 용어 description — '관련 용어: 계층적 작업 네트워크(Hierarchical Task Network, HTN)'로 링크 없는 글자로 바꾸고 기존 PDDL 페이지 링크는 유지했다.
- 2차: hierarchical-task-network 용어 — Filippone 외 문장을 유지하고 sources 에 ref-116 을 더했다(원문 미열람 병기).
- 2차: area_reflection_proposals 세 항목 — 태그 바로 뒤 괄호를 모두 없애고 '[사실] 근거 ref-111·f2' 처럼 태그 뒤에 공백과 '근거'를 두는 형식으로 고쳤다.
- 2차: area_reflection_proposals 의 2. 공정·워크플로 모델링 항목 Corradini 외(ref-114)와 14. 작업 순서·스케줄링 항목 HDDL(ref-951)에 '원문 미열람'을 병기했다(2. 공정·워크플로 모델링 항목의 BPMN·Filippone 외에도 병기).
- 2차: 단계 2 페이지 3절 '형식–작업 모델 대응' 표 머리 문장의 [추정] 태그 각주에 [^ref-125][^ref-413] 을 더했다(두 각주 정의는 8절에 이미 있음).

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.5
- 트랙 로그 항목: 답한 질문: q2-02(작업·배정 결과를 표현하는 표준·형식 비교, f1~f18) / 새 질문: q3-08(f16), q3-09(f17, oq-049 관련) / 온톨로지 변경: v0.4 → v0.5: 개념 '진행 상태 (Progress)' 속성 '상태 값'에 외부 표현 원천 후보(Open-RMF 작업 상태 status 값, 디스패치 상태 값, ISA-95 작업 응답 JobState·실제 시작·종료 시각) 추가, 초안 → 확정(f2·f7) / 개념 '배정 (Assignment)'에 외부 표현이 배정 대상만 담는다는 메모 추가, 확정 유지(f2·f3·f4·f18); 거부 없음; 근거 실행 2026-09-25-43 / 완료 조건 평가: 미충족(부족: 평가 데이터 q2-03 미조사, 작업 요구의 적재물 속성·업무 완료 조건 미확정; 막힌 질문 q2-03·q2-04·q2-05·q2-06) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 2. 공정·워크플로 모델링, 14. 작업 순서·스케줄링 3건 / 다음 실행 제안: q2-03(평가 데이터), q2-04(중간 표현 변환 손실)
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 4, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-02 | 답함 | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md#q2-02 | — | — | — |
| q3-08 | 열림 | — | ROP 가 업무→작업 분해 구조를 내부에 둘 때 BPMN·Serverless Workflow·HDDL 같은 기존 형식을 표준 표현으로 채택할지, 자체 작업 모델 스키마를 두고 Open-RMF 복합 작업·VDA 5050 주문으로 변환할지, 변환 때 배정 근거·확인 여부는 어디에 남기는가? (q2-02 에서 파생) | 3 | f16 |
| q3-09 | 열림 | — | Open-RMF 복합 작업의 단계와 VDA 5050 waitForTrigger–trigger 를 조합해 제조사가 다른 플릿 사이 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 집행할 수 있는가, 트리거 누락·시간 초과 때 누가 복구하는가? (q2-02 에서 파생, 열린 질문 oq-049 관련) | 3 | f17 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 작업 상태 스키마는 배정 결과를 assigned_to(플릿 그룹·로봇 이름)로, 배정·발송 과정을 디스패치 상태(dispatch)로 표현한다 [사실] 근거 ref-111·f2. VDA 5050 배정 기능은 기존 7·9절 문장과 각주 ref-031 을 재사용하고 새로 반복하지 않는다. 표준 형식의 배정 결과는 누가 맡았는지만 남기므로 최근접 배정과 다른 기준의 전체 효과를 사후 비교하려면 ROP 가 배정 근거·목적함수 값을 별도로 기록해야 할 것으로 보인다 [추정] 근거 ref-111·ref-130·f18 — 2절 원문 질문과 oq-052 에 연결. |
| 2 | 7. 관련 표준·프레임워크·오픈소스 | OPC UA for ISA-95 작업 응답의 실제 시작·종료 시각·작업 상태·인원·설비·자재 실적 필드 [사실] 근거 ref-130·f7; BPMN 2.0.2 의 사람 수행자·잠재 담당자·자원 배정 식 [추정] 근거 ref-952·f9, 원문 미열람; Corradini 외(2023)의 BPMN 기반 다중 로봇 틀 [사실] 근거 ref-114·f10, 원문 미열람; Serverless Workflow DSL 1.0.x [사실] 근거 ref-949·f11; Filippone 외(2026-03, 프리프린트)의 '로봇 임무 기술에 합의된 표준 형식이 없다'는 평가 [의견] 근거 ref-116·f15, 원문 미열람. |
| 14 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 복합 작업의 순서가 있는 단계(phases) 표현 [사실] 근거 ref-948·f1; HDDL 의 하위 작업 부분·전체 순서 표현(arXiv 2019-11 공개, AAAI 2020 발표) [사실] 근거 ref-951·f14, 원문 미열람; VDA 5050 3.0.0 waitForTrigger–trigger 동작 [사실] 근거 ref-031·f5; 이를 서로 다른 플릿의 작업(작업 요청) 사이 동기화에 쓸 가능성 [추정] 근거 f17, oq-049 관련. |
