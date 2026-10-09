---
title: "채팅 기반 구성·운영"
type: track
track: chat-based-configuration-and-operation
related_areas: [5, 8, 9, 10, 11, 12, 13, 15, 18, 23, 24, 25, 26, 28, 29, 31, 32, 38, 47, 48, 51, 54]
tags: [자연어 지시, 챗봇, 채팅 기반 구성, 맵 작성, 시나리오 구성, 로봇 구성, 상황 재현, LLM, 작업 분해, 작업 배정, 스케줄링, 중점 연구 트랙, 확장 아이디어]
status: draft
created: 2026-09-25
updated: 2026-10-09
last_run: 2026-10-09
version: 20
confidence: low
sources: [ref-807, ref-809, ref-166, ref-779, ref-674, ref-677, ref-168, ref-236, ref-746, ref-041, ref-592, ref-594, ref-611, ref-612]
---

[홈](../../index.md) › 중점 연구 트랙 › 채팅 기반 구성·운영

# 채팅 기반 구성·운영

> 트랙 상태: active · 현재 단계: 단계 3. 업무 지시 구현 가설 설계 · 마지막 트랙 실행: 2026-09-25

이 페이지는 중점 연구 트랙 "채팅 기반 구성·운영"의 개요다. 이 트랙은 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)(확장 아이디어 2)의 연구를 위해 2026-09-25에 추가되었다. 트랙(track)은 분류 원문의 17개 대분류·67개 세부 연구영역을 바꾸지 않고, 여러 세부영역을 가로지르는 하나의 연구 주제를 단계적으로 파고드는 집중 연구 프로그램이다. 페이지 구성·백로그 형식·단계 전환 규칙은 첫 트랙 [매뉴얼 기반 로봇 기능 온톨로지](../manual-capability-ontology/index.md)와 같고, 단계는 열 개다. 2026-09-28 분류 개정에서 이 트랙은 "자연어 업무 지시 챗봇"에서 "채팅 기반 구성·운영"으로 범위를 넓혔다. 기존 단계 1~5(업무 지시)는 그대로 이어 가고, 채팅으로 맵 작성·시나리오 구성·로봇 구성·실제 상황 재현을 다루는 단계 6~9와 통합 검증 단계 10을 더했다. 이 트랙의 중심 영역은 새 대분류 [C. 채팅 기반 구성·운영](../../categories/chat-based-configuration-and-operation/index.md)의 8~13번이다.

트랙 정의 파일은 `config/tracks/chat-based-configuration-and-operation.yaml`이다. 트랙 공통 운영 규칙(트랙 실행 1회가 반드시 내는 결과, 단계 전환, 트랙 조사 비중 설정)은 [에이전트 소개](../../about/agents.md)의 "트랙 실행이 일반 실행과 다른 점" 절에 있다. 세 확장 아이디어가 이어지는 구조와 공통 데이터 모델은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다. 첫 트랙 실행(2026-09-25-04)의 조사 결과는 [단계 1. 선행 연구·제품 사례 조사](stage-1-prior-work-and-products.md)에 있으며, 모든 조사 내용은 트랙 실행이 출처와 함께 채운다.

## 1. 컨셉

> 사용자가 채팅으로 상황과 처리할 일을 입력하면 AI가 업무를 파악·분해하고, 온톨로지로 적합한 로봇을 찾아 배정·배치한 뒤 작업 진행과 스케줄링을 자동으로 관리

위 문장은 사용자가 2026-09-25에 정의한 확장 아이디어 2의 문구를 그대로 옮긴 것이다. 2026-09-28에 사용자가 범위를 다음과 같이 넓혔다.

> 채팅 기능으로 쉽게 맵을 그리고, 상황을 구성하고, 로봇을 오케스트레이션 하는 기능 등. 맵 그리기뿐만 아니라 시나리오 구성, 로봇 구성, 실제 상황 시뮬레이션 재현까지 가는 것

두 문장을 합친 이 트랙의 범위는 채팅 하나로 맵 작성 → 시나리오 구성 → 로봇 구성 → 실제 상황 시뮬레이션 재현 → 업무 지시·오케스트레이션까지 이어 가는 대화형 기능 전체다. 첫 문장(업무 지시)은 단계 1~5가, 둘째 문장(맵·시나리오·로봇 구성·재현)은 단계 6~9가 다루고, 단계 10이 둘을 한 흐름으로 이어 검증한다. 문장의 "온톨로지"는 [매뉴얼 기반 로봇 기능 온톨로지](../manual-capability-ontology/index.md) 트랙(확장 아이디어 1)이 만드는 로봇 기능 온톨로지이며, [건축 도면 자동 인식](../floorplan-recognition/index.md) 트랙(확장 아이디어 3)이 공간 그래프로 적재하는 공간·시설도 함께 담는 것으로 본다. [가정] 이 트랙은 그 온톨로지를 만드는 쪽이 아니라 질의해 쓰는 쪽이다. 지시의 해석과 분해, 로봇 배정과 배치, 진행 관리와 스케줄링을 어디까지 자동화할 수 있는지, 그리고 대규모 언어 모델(Large Language Model, LLM)의 잘못된 해석이 로봇 배정으로 이어지지 않게 하려면 무엇이 필요한지를 묻는다.

## 2. 연구 목표

1. 자연어 지시(상황과 처리할 일)를 ROP가 실행할 수 있는 작업 단위로 파악·분해하는 방법을 밝힌다.
2. 분해한 작업을 로봇 기능 온톨로지 질의로 적합한 로봇에 배정·배치하는 연결 방법을 밝힌다.
3. LLM의 잘못된 해석이 로봇 배정과 실행으로 이어지지 않게 하는 확인 절차와 권한 경계를 정한다.
4. 작업 진행 관리와 스케줄링 결정을 LLM과 최적화 엔진 사이에 어떻게 나눌지 정한다.
5. 해석·분해 정확도와 배정 적합성을 검증하는 지표와 절차를 정한다.
6. 채팅으로 맵을 작성하는 방법(말·글 설명, 도면·사진 입력, 대화 중 확인 질문)과 한계를 밝힌다.
7. 채팅으로 시나리오(할 일·물품·사람·순서·기한·실패 처리)와 로봇 구성(종류·대수·장비·위치·역할)을 정하고 온톨로지로 가능 여부를 확인하는 방법을 밝힌다.
8. 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현 충실도를 확인하며, 조건을 바꿔 비교하는 방법을 밝힌다.

목표 1은 단계 1·2·3, 목표 2는 단계 2·3, 목표 3은 단계 4, 목표 4는 단계 3, 목표 5는 단계 5, 목표 6은 단계 6, 목표 7은 단계 7·8, 목표 8은 단계 9에 주로 대응하고, 단계 10은 목표 전체를 한 흐름으로 검증한다. [가정] 목표 6~8은 2026-09-28 범위 확장으로 더했다.

## 3. 가설과 판정 상태

| 가설 | 내용 | 판정 | 근거(단계·실행 id) |
|---|---|---|---|
| 가설 1 | 자연어 지시를 정해진 작업 모델([업무 분해·배정 설계 초안](task-model-draft.md))로 먼저 구조화하면, LLM이 로봇 명령을 직접 만드는 방식보다 잘못된 배정이 줄어든다. [가설] | 부분 지지(잠정) | 단계 5 · 실행 2026-09-25-86 · 확실성 낮음 ([단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md#q5-03)) |
| 가설 2 | 적합한 로봇의 선택을 LLM의 판단 대신 온톨로지 질의(능력·제약 대조)에 맡기면 배정 근거를 설명하고 재현할 수 있다. [가설] | 부분 지지(잠정) | 단계 5 · 실행 2026-09-25-86 · 확실성 매우 낮음~낮음 ([단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md#q5-03)) |
| 가설 3 | 스케줄링 결정은 최적화 엔진이 맡고 LLM은 지시 해석·확인 대화·진행 설명을 맡는 분담이 운영을 더 안정적으로 만든다. [가설] | 부분 지지(잠정) | 단계 5 · 실행 2026-09-25-86 · 확실성 낮음 ([단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md#q5-03)) |

판정 값은 지지 / 부분 지지 / 기각 / 미판정 네 가지다. 구축 시점에는 모두 미판정이었으며, 판정은 [단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md)에서 내용 검증 에이전트의 승인을 받은 결과만 적는다. 가설은 `[사실]`로 승격되기 전까지 `[가설]` 태그를 유지한다. 가설 문장은 아이디어 정의에서 구축자가 도출한 것이다. [가정]

위 판정은 이 위키의 판정 규칙을 적용한 잠정 결과다. 판정 규칙은 가설을 하위 주장으로 나누고 GRADE 식으로 근거 확실성을 낮춰 매긴 뒤, 핵심 하위 주장 모두에 물류 조건의 직접 근거가 있고 확실성이 중간 이상이면 지지, 일부 하위 주장만 근거가 있거나 가설이 성립하지 않는 조건이 확인되면 부분 지지, 핵심 하위 주장에 직접 반대 근거가 있으면 기각, 직접 근거가 없으면 미판정으로 가르는 것이다(이 위키의 종합, 판정 규칙을 직접 정한 출처는 없음). [추정][^ref-807][^ref-809]

- 가설 1: 구조화·분해 뒤 결정적 해법·검사를 거친 방식이 LLM 직접 배정·직접 코드 생성보다 실패가 적었다는 비교가 있으나, 비교 형태가 작업 모델 구조화와 같지 않고 LLM 직접 배정이 높은 정답률을 보인 반례가 있으며 물류 조건 근거가 없다(이 위키의 종합). [추정][^ref-166][^ref-779][^ref-674][^ref-677][^ref-168]
- 가설 2: 설명 가능성 하위 주장은 직접 근거가 없어 미판정이고, 부분 지지는 재현성 쪽 간접 근거(온톨로지 판정을 배정기 독립 제약으로 쓰는 구조, LLM 반복 출력 불일치 보고)에만 기댄다. 선언 능력과 운용 능력이 다를 수 있다는 반대 방향 근거도 있다(이 위키의 종합). [추정][^ref-236][^ref-746][^ref-041]
- 가설 3: LLM 직접 스케줄링의 실행 가능성·일관성 한계와 LLM 지연 근거가 있으나, LLM 이 루프 밖에서 설계한 규칙이 롤링 MILP 를 앞선 반례(제조·AGV 시뮬레이션 조건, 저자 보고, 롤링 MILP 는 AGV 운송 하위 문제의 추상화, 물류 창고 적용 미확인)가 있어 '최적화 엔진'의 해석에 따라 판정 방향이 갈린다(이 위키의 종합). [추정][^ref-592][^ref-594][^ref-611][^ref-612]

판정 변경 기록

- 2026-09-25 · 실행 2026-09-25-86: 가설 1~3 미판정 → 부분 지지(잠정). 이 위키의 판정 규칙(추정)을 비물류 조건의 단일 출처 저자 보고 근거에 적용한 잠정 결과이며, 가설 2 의 설명 가능성 하위 주장은 미판정이다.

## 4. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 아래 목록은 [확장 아이디어 연결 구조](../../ideas/index.md)의 매핑표(● 중심 영역, ○ 함께 필요한 영역)에서 자동으로 만들며, 원천은 트랙 정의의 `idea_areas`와 `idea_area_notes`다. 프런트매터 `related_areas`는 이 목록과 같다. 매핑은 구축자 제안이며 근거는 결정 기록에 남겼다. [가정]

<!-- auto:idea-areas:start -->
**중심 영역(●)**

- [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) — 사용자 정의(2026-09-28)의 '채팅 기능으로 쉽게 맵을 그리고'가 이 영역의 일 자체다
- [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) — 사용자 정의의 '상황을 구성하고'와 '시나리오 구성'이 이 영역의 일 자체다
- [10. 채팅으로 로봇 구성](../../categories/chat-based-configuration-and-operation/chat-robot-configuration.md) — 사용자 정의의 '로봇 구성'이 이 영역의 일 자체다
- [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 사용자 정의의 '실제 상황 시뮬레이션 재현'이 이 영역의 일 자체다
- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 옛 아이디어 정의(채팅으로 업무를 파악·분해하고 배정·배치·스케줄링)와 사용자 정의의 '로봇을 오케스트레이션 하는 기능'이 이 영역이다
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 대화 결과를 계획으로 확인·승인하고 오해석·권한을 관리하는 기반이다(기존 단계 4 오해석 방지의 대상)

**함께 필요한 영역(○)**

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — '온톨로지로 적합한 로봇을 찾는' 질의의 대상이다(아이디어 1의 산출물)
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 지시 속 장소 표현(예: 층·구역 이름)을 공간 노드로 해석한다(아이디어 3의 산출물)
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 배정 시점의 로봇 위치·배터리·가용 상태를 현재 상태로 확인한다
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 채팅 지시는 업무 시스템의 주문·요청과 나란히 들어오는 업무 요청이므로 변경·취소·완료 반영 규칙을 함께 본다
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — 분해 결과가 들어갈 작업 단계·선후관계·완료 조건의 틀을 이 영역이 정의한다
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — '온톨로지로 적합한 로봇을 찾아 배정'하는 일이 이 영역의 배정 문제다
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — '작업 진행과 스케줄링을 자동으로 관리'하는 일이 이 영역의 순서·시간 제약·긴급 작업 삽입 문제다
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 배치할 때 승강기·충전기 같은 공용 자원 예약을 함께 정한다
- [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) — 배정 뒤 명령의 접수·실행·완료·취소 상태와 같은 지시의 중복 처리 방지가 필요하다
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 채팅은 작업자·관리자가 일을 지시하고 확인·승인하는 운영 인터페이스다
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 진행 중 고장·지시 변경 때 재배정·재계획을 한다
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — '작업 진행 관리'에서 지연·이상을 탐지하고 원인을 설명한다
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 이 영역 정의의 LLM 에이전트와, AI가 만든 작업 계획을 실행에 쓰는 기준을 묻는 이 영역의 질문이 해석과 오해석 방지 단계에 그대로 걸린다
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 오해석이 위험한 동작으로 이어지지 않게 안전 조건을 확인 절차에 넣는다
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 채팅 사용자가 어느 로봇·구역에 어떤 작업까지 지시할 수 있는지(명령 권한)와 대화 기록 보호를 정한다
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 해석·배정 결과를 지시 시나리오 시험과 모델·프롬프트 변경 뒤 회귀시험으로 검증한다

매핑 전체와 다른 아이디어와의 비교는 [확장 아이디어 연결 구조](../../ideas/index.md)의 매핑표에 있다.
<!-- auto:idea-areas:end -->

## 5. 단계 진행 현황 표

열 단계는 각각 시작 질문에 답하고, 답하는 과정에서 생긴 후속 질문을 [질문 백로그](question-backlog.md)에 쌓고, 완료 조건을 채우면 다음 단계로 넘어간다. 뒤 단계에서 생긴 질문이 앞 단계를 다시 열 수 있다. 단계별로 밝힐 것과 완료 조건은 다음과 같다.

| 단계 | 밝힐 것 | 완료 조건 | 시작 질문 수 |
|---|---|---|---|
| [단계 1. 선행 연구·제품 사례 조사](stage-1-prior-work-and-products.md) | 자연어 지시를 작업으로 바꾸고 로봇에 배정하는 기존 연구와 제품은 무엇을 자동화하고 무엇을 사람에게 남기는가. | 선행 연구·제품 사례 비교가 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "3. 선행 연구·제품 사례" 절에 실림; 지시 분해 접근의 유형 목록이 [업무 분해·배정 설계 초안](task-model-draft.md)에 반영됨 | 4 |
| [단계 2. 필요한 데이터와 표준 조사](stage-2-data-and-standards.md) | 지시를 작업으로 바꾸고 배정·스케줄링하는 데 필요한 정보 항목과, 그 정보를 표현·교환하는 기존 표준·형식은 무엇인가. | 필요한 데이터 항목과 표준·형식 목록이 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "4. 필요한 데이터와 표준" 절에 실림; 작업 모델의 정보 항목이 [업무 분해·배정 설계 초안](task-model-draft.md)의 개념 목록 표에 반영됨 | 3 |
| [단계 3. 업무 지시 구현 가설 설계](stage-3-implementation-hypothesis.md) | 지시 해석부터 진행 관리까지의 처리 흐름에서 어느 부분을 LLM이 맡고 어느 부분을 온톨로지 질의와 최적화 엔진이 맡는가. | 처리 흐름·핵심 구성 요소·다른 아이디어와의 연결이 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "5. 구현 가설" 절에 실림; [업무 분해·배정 설계 초안](task-model-draft.md)이 근거 finding과 함께 v0.1 이상으로 갱신됨; 사용자에게 제안하는 실험 계획이 [실험](experiments.md)에 실림 | 4 |
| [단계 4. 오해석 방지와 확인 절차](stage-4-misinterpretation-safeguards.md) | LLM의 잘못된 해석이 배정·실행으로 이어지기 전에 어디서, 어떤 방법으로 멈추는가. | 실행 전 검증 단계, 명령 권한, 제한 운영 기준을 담은 확인 절차 초안이 [업무 분해·배정 설계 초안](task-model-draft.md)의 미해결 모델링 질문과 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "5. 구현 가설" 절에 반영됨 | 4 |
| [단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md) | 챗봇이 지시를 맞게 해석하고 적합한 로봇을 배정했는지를 어떻게 측정하고, 가설 1~3을 어떻게 판정하는가. | 평가 지표와 검증 절차가 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "6. 검증 방법" 절에 실림; 가설 판정표가 [트랙 개요](index.md)의 "3. 가설과 판정 상태"에 실림; 사용자에게 제안하는 실험 계획이 [실험](experiments.md)에 실림 | 3 |
| [단계 6. 채팅으로 맵 작성](stage-6-chat-map-authoring.md) | 공간을 말·글로 설명하거나 도면·사진을 올려 대화로 지도를 만들고 고치는 방법은 무엇이며 어디까지 되는가. | 채팅 맵 작성 방법 비교표와 구현 가설이 단계 페이지와 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "5. 구현 가설" 절에 실림 | 4 |
| [단계 7. 채팅으로 시나리오 구성](stage-7-chat-scenario-composition.md) | 할 일·물품·사람·순서·기한·실패 처리 조건을 대화로 정하는 방법은 무엇인가. | 대화형 시나리오 구성 절차 초안과 시나리오 형식 비교가 단계 페이지에 실림 | 4 |
| [단계 8. 채팅으로 로봇 구성](stage-8-chat-robot-configuration.md) | 투입할 로봇의 종류·대수·장비·위치·역할을 대화로 정하고 온톨로지로 수행 가능 여부를 어떻게 확인하는가. | 대화형 로봇 구성 절차 초안과 온톨로지 질의 연결 방식이 단계 페이지에 실림 | 3 |
| [단계 9. 채팅으로 실제 상황 시뮬레이션 재현](stage-9-chat-real-situation-replay.md) | 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현 충실도를 확인하며, 조건을 바꿔 비교하는 방법은 무엇인가. | 실제 상황 재현 방법 비교표와 재현 충실도 지표 초안이 단계 페이지에 실림 | 4 |
| [단계 10. 대화형 구성·운영 통합 검증과 가설 판정](stage-10-integrated-verification.md) | 맵 작성부터 업무 지시까지를 하나의 대화 흐름으로 이었을 때 무엇을 어떻게 검증하고, 트랙 가설을 어떻게 판정하는가. | 통합 검증 절차와 트랙 가설 판정이 [트랙 개요](index.md)의 "3. 가설과 판정 상태"와 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)의 "6. 검증 방법" 절에 실림 | 3 |

아래 표는 퍼블리셔가 트랙 정의와 질문 백로그에서 자동으로 만든다(단계 / 상태 / 열린 질문 수 / 완료 조건 충족 여부).

<!-- auto:track-progress:start -->
| 단계 | 상태 | 열린 질문 수 | 완료 조건 충족 여부 |
|---|---|---|---|
| [단계 1. 선행 연구·제품 사례 조사](stage-1-prior-work-and-products.md) | 진행 중 | 2 | 미충족 |
| [단계 2. 필요한 데이터와 표준 조사](stage-2-data-and-standards.md) | 대기 | 4 | 미충족 |
| [단계 3. 업무 지시 구현 가설 설계](stage-3-implementation-hypothesis.md) | 대기 | 12 | 미충족 |
| [단계 4. 오해석 방지와 확인 절차](stage-4-misinterpretation-safeguards.md) | 대기 | 15 | 미충족 |
| [단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md) | 대기 | 15 | 미충족 |
| [단계 6. 채팅으로 맵 작성](stage-6-chat-map-authoring.md) | 대기 | 4 | 미충족 |
| [단계 7. 채팅으로 시나리오 구성](stage-7-chat-scenario-composition.md) | 대기 | 4 | 미충족 |
| [단계 8. 채팅으로 로봇 구성](stage-8-chat-robot-configuration.md) | 대기 | 3 | 미충족 |
| [단계 9. 채팅으로 실제 상황 시뮬레이션 재현](stage-9-chat-real-situation-replay.md) | 대기 | 4 | 미충족 |
| [단계 10. 대화형 구성·운영 통합 검증과 가설 판정](stage-10-integrated-verification.md) | 대기 | 3 | 미충족 |

현재 단계: 단계 1. 선행 연구·제품 사례 조사 (1 / 10) · 트랙 상태: active
<!-- auto:track-progress:end -->

## 6. 살아있는 산출물 링크

- [업무 분해·배정 설계 초안](task-model-draft.md) — 현재 버전 v0.9. 아이디어 정의에서 도출한 v0 개념 10개·관계 9개에 검증을 거친 개념 로봇 팀을 더했고(v0.1, 실행 2026-09-25-04), 배정 개념에 속성 '배정 산출 방식'을 더해 확정했으며(v0.2, 실행 2026-09-25-21), 상황 개념에 속성 '값 출처'를 더해 확정했고(v0.3, 실행 2026-09-25-30), 상황의 장소 표현에 해석 결과 '공간 노드 참조'를 짝으로 더하고 업무 개념의 기한·우선순위 값 원천을 정리해 확정했으며(v0.4, 실행 2026-09-25-37), 진행 상태 개념에 외부 표현 원천 메모를 더해 확정하고 배정 개념에 외부 표현 대응 메모를 더했다(v0.5, 실행 2026-09-25-51). 일정 개념에 속성 '일정 산출 방식'을 더해 확정했고(v0.6, 실행 2026-09-25-66), 배정 개념의 배정 산출 방식에 값 후보 '입찰 비교'를 더했으며(v0.7, 실행 2026-09-25-71), 지시 개념에 속성 '변경 유형'·'원 지시 참조'를, 작업 개념에 속성 '변경 허용 상태'·'취소 시 보상 활동'을 더해 두 개념을 확정했다(v0.8, 실행 2026-09-25-77). 개념 '명령 권한'을 더해 확정하고(속성 구성·기본 거부는 후보) 지시 개념의 속성 '입력자'를 인증된 사용자 식별로 정리했다(v0.9, 실행 2026-09-25-83). 실행 2026-09-25-26, 2026-09-25-62, 2026-09-25-74, 2026-09-25-79, 2026-09-25-81, 2026-09-25-98, 2026-09-25-99 에서는 변경이 없었다(2026-09-25-74 에서 제안된 개념 '배정 실패'와 2026-09-25-79 에서 제안된 개념 '사용자 확인', 2026-09-25-81 에서 다시 제안된 개념 '검증 기록'은 초안 6절의 질문으로 남았고, 2026-09-25-98 의 평가 지표는 작업 모델의 개념이 아니라 검증 방법이라 초안에 넣지 않았다). 트랙 실행이 근거 finding과 함께 갱신한다.
- [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md) — 확장 아이디어 페이지. 3~6절(선행 연구·제품 사례, 필요한 데이터와 표준, 구현 가설, 검증 방법)을 이 트랙의 단계 1·2·3·4·5 실행이 채운다. 3절은 선행 연구와 제품 사례(벤더 주장 수준), 채팅·음성 지시 제품의 확인·승인 방식 비교(q1-03, 실행 2026-09-25-26)에 더해 상황 정보 추출과 되묻기(q1-04, 실행 2026-09-25-30)가 작성되었다. 로봇에 자연어로 일을 지시하는 제품의 해석 결과 확인·승인 절차와 물류 지시를 대상으로 한 추출·되묻기 연구는 공개 자료·검색 범위에서 확인되지 않았다(부재의 확인은 아님). 4절은 필요한 데이터 항목과 원천(q2-01, 실행 2026-09-25-37), 작업·배정 결과를 표현하는 표준·형식 비교(q2-02, 실행 2026-09-25-51), 해석·분해 평가 데이터(q2-03, 실행 2026-09-25-62)가 작성되었다. 물류 창고 지시를 정답과 짝지은 공개 데이터셋은 검색 범위에서 찾지 못했다(부재의 확인은 아님). 5절은 스케줄링 결정의 분담(q3-01, 실행 2026-09-25-66), 처리 흐름·핵심 구성 요소(q3-02, 실행 2026-09-25-71), 온톨로지 질의 결과에 따른 되묻기(q3-03, 실행 2026-09-25-74), 지시 변경 반영(q3-04, 실행 2026-09-25-77)이 작성되어 단계 3 시작 질문 4개가 모두 답해졌고, 다른 아이디어와의 연결은 구조 언급 수준이다. 실행 2026-09-25-79 에서는 단계 4 의 q4-01 에 답해 5절에 '오해석 방지 확인 절차' 소절(다섯 겹 확인 절차 가설, 신뢰도 low)을 더했고, 실행 2026-09-25-81 에서는 q4-02 에 답해 '검증 방법별로 잡는 오류' 소절(신뢰도 low)을 더했다. 실행 2026-09-25-83 에서는 CLI 로 지정된 질문으로 q4-03 에 답해 5절에 '명령 권한과 감사 추적' 소절(신뢰도 low)을 더했다. 제한 운영 기준(q4-04)은 아직 조사하지 않았다. 실행 2026-09-25-98 에서는 CLI 로 지정된 질문으로 단계 5 의 q5-01 에 답해 6절에 '평가 지표' 소절(해석·분해·배정 적합성·일정 품질 네 층 지표 구성, 신뢰도 low)을 더했다. 실행 2026-09-25-99 에서 CLI 로 지정된 질문으로 q5-02 에 답해 6절에 검증 절차 소절(지시·실행·교란·반복 네 층 가상 시험 구성, 신뢰도 low)을 더했다. 가설 판정(q5-03)은 아직 조사하지 않았다. 실행 2026-09-25-79, 2026-09-25-81, 2026-09-25-83, 2026-09-25-98, 2026-09-25-99 는 단계 3·4 완료와 단계 전환이 승인되지 않은 상태에서 지정된 질문으로 뒤 단계를 다뤘으므로, 현재 단계는 단계 3 으로 둔다.
- [질문 백로그](question-backlog.md) — 최신 수치는 백로그 페이지의 자동 표를 따른다.
- [트랙 로그](log.md) — 실행별 기록
- [실험](experiments.md) — 제안된 실험 계획과 사용자 실험 결과 요약(선택). 현재 제안된 실험은 없다.

- 실행 2026-09-25-85 에서 CLI 로 지정된 질문으로 단계 4 의 q4-04 에 답해 [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md) 5절에 '제한 운영으로 넘기는 기준' 소절(되묻기·사람 승인·실행 보류 세 경로, 신뢰도 low)을 더했다. [업무 분해·배정 설계 초안](task-model-draft.md)은 변경 없이 v0.9 를 유지했다. 단계 3·4 완료와 단계 전환이 승인되지 않아 현재 단계는 단계 3 으로 둔다.

- 실행 2026-09-25-86 에서 CLI 로 지정된 질문으로 단계 5 의 q5-03 에 답해 3절에 잠정 가설 판정(가설 1~3 모두 부분 지지(잠정), 이 위키의 종합, 신뢰도 low)을 싣고, [실험](experiments.md)에 제안 실험 E5-01~E5-03(사용자 수행 대기)을, [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md) 6절에 '가설 판정 절차' 소절을 더했다. [업무 분해·배정 설계 초안](task-model-draft.md)은 변경 없이 v0.9 를 유지했다. 단계 3·4 완료와 단계 전환이 승인되지 않아 현재 단계는 단계 3 으로 둔다.

- 실행 2026-10-09-20 에서 앞 단계로 되돌아온 [단계 1. 선행 연구·제품 사례 조사](stage-1-prior-work-and-products.md)의 q1-05·q1-06 과 [단계 2. 필요한 데이터와 표준 조사](stage-2-data-and-standards.md)의 q2-04 에 답했다(신뢰도 low). [업무 분해·배정 설계 초안](task-model-draft.md)은 작업 개념의 선후관계를 작업 사이 선행 의존으로 정리해 v0.9 → v1.0 으로 올렸다(1.0 은 0.1 증가 규칙에 따른 번호이며 완성판을 뜻하지 않는다). [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md) 3절에 물류 지향 LLM 작업 분해 연구를, 4절에 중간 표현과 로봇 관제 인터페이스 대응 소절을 더했다. 위에서 '현재 단계는 단계 3 으로 둔다'고 적은 서술은 실행 2026-09-25-79~99 시점 기준이며, 이번 실행 대상은 단계 2. 필요한 데이터와 표준 조사이고 단계 2 완료와 단계 전환은 승인되지 않았다.

## 7. 최근 실행

<!-- auto:track-recent-runs:start -->
아직 트랙 실행 기록이 없다.
<!-- auto:track-recent-runs:end -->

## 8. 참고 자료

아래는 3. 가설과 판정 상태의 잠정 판정 근거 각주다. 트랙 실행의 나머지 출처는 각 단계 페이지의 출처 절에 있으며, 판정의 자세한 근거는 [단계 5. 업무 지시 검증과 가설 판정](stage-5-verification-and-hypotheses.md#q5-03)에 있다.

[^ref-807]: Cochrane, Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence, 미확인, https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14, 접근일 2026-09-25 (원문 미열람)
[^ref-809]: NASA ESTO, Definition Of Technology Readiness Levels, 미확인, https://esto.nasa.gov/files/trl_definitions.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-166]: Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T., LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning, 2024-10, https://arxiv.org/abs/2410.21040, 접근일 2026-09-25 (원문 미열람)
[^ref-779]: Garrabé, É., Teixeira, P., Khoramshahi, M., & Doncieux, S., Enhancing Robustness in Language-Driven Robotics: A Modular Approach to Failure Reduction, 2024-11, https://arxiv.org/abs/2411.05474, 접근일 2026-09-25 (원문 미열람)
[^ref-674]: Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH), Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins, 2026-06, https://arxiv.org/abs/2606.08214, 접근일 2026-09-25 (원문 미열람)
[^ref-677]: CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11, https://arxiv.org/abs/2511.22354, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: Atil, B. 외, Non-Determinism of "Deterministic" LLM Settings, 2024-08, https://arxiv.org/abs/2408.04667, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-592]: ConstraintBench 저자(arXiv 2602.22465, 저자 미확인), ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization, 2026-02, https://arxiv.org/abs/2602.22465, 접근일 2026-09-25 (원문 미열람)
[^ref-594]: SCHEDBench 저자(arXiv 2608.00991, 저자 미확인), SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling, 2026-08, https://arxiv.org/abs/2608.00991, 접근일 2026-09-25 (원문 미열람)
[^ref-611]: RACE-Sched 저자(arXiv 2605.29262, 저자 미확인), Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling, 2026-05, https://arxiv.org/abs/2605.29262, 접근일 2026-09-25 (원문 미열람)
[^ref-612]: Li, J., & Li, C.(소속 미확인), LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling, 2026-08, https://arxiv.org/abs/2608.09343, 접근일 2026-09-25 (원문 미열람)
