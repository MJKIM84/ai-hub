---
title: "실험"
type: track
subtype: experiments
track: nl-task-chatbot
status: draft
created: 2026-09-25
updated: 2026-09-25
version: 2
sources: [ref-746, ref-592, ref-734, ref-400]
last_run: 2026-09-25
---

[홈](../../index.md) › 중점 연구 트랙 › [자연어 업무 지시 챗봇](index.md) › 실험

# 실험

이 페이지는 중점 연구 트랙 [자연어 업무 지시 챗봇](index.md)에서 스토리텔러 에이전트가 제안한 실험 계획과, 사용자가 직접 수행해 저장소의 `experiments/` 폴더에 넣은 실험 결과의 요약을 모은다. 선택 페이지이며, 실험이 없어도 트랙은 진행된다.

## 실험 규칙

- 실험은 사용자가 직접 수행한다. 에이전트는 계획을 제안하고, 사용자가 넣은 결과를 읽어 반영한다.
- 이 트랙에서 계획은 단계 3·5에서 제안한다(트랙 정의의 `stage_artifacts`). [가정]
- 결과는 `experiments/<날짜>-<이름>/`에 넣고 `README.md` 머리에 트랙(`nl-task-chatbot`), 단계, 답하려는 질문 id를 적는다. 다음 트랙 실행에서 `[사용자 실험]` 태그로 반영되며, `[사실]`로 올라가려면 내용 검증 에이전트의 판정이 필요하다.
- 계획 형식(계획 번호 `E<단계>-<두 자리>`, 목적, 방법, 측정 지표와 조건, 필요한 자료, 제안한 실행 id, 상태)과 결과 입력 형식은 첫 트랙의 [실험](../manual-capability-ontology/experiments.md) 페이지와 [기여·정정 방법](../../about/how-to-contribute.md)을 따른다.

## 제안된 실험 계획

아래 계획은 [단계 5. 검증 방법과 가설 판정](stage-5-verification-and-hypotheses.md#q5-03)의 잠정 가설 판정(가설 1~3 모두 부분 지지(잠정))을 옮기는 데 필요한 사용자 실험 후보다. 결과나 수치가 아니라 제안이며, 계획의 근거는 이 위키의 종합이다. [추정][^ref-746][^ref-592][^ref-734] 측정 지표는 [q5-01 답](stage-5-verification-and-hypotheses.md#q5-01)의 네 층 지표를, 시험 구성은 [q5-02 답](stage-5-verification-and-hypotheses.md#q5-02)의 가상 현장 네 층(지시·실행·교란·반복)을 쓰는 안이다.

### E5-01 작업 모델 경유 대 LLM 직접 명령 생성의 오배정률 (가설 1)

- 목적: 자연어 지시를 작업 모델로 먼저 구조화하면 LLM 이 로봇 명령을 직접 만드는 방식보다 잘못된 배정이 줄어드는지 본다.
- 방법: 같은 물류 지시 세트를 (가) 작업 모델([업무 분해·배정 설계 초안](task-model-draft.md))로 구조화한 뒤 결정적 능력 질의·배정기에 넘기는 경로와 (나) LLM 이 로봇 명령을 직접 만드는 경로에 똑같이 준다.
- 측정 지표와 조건: 오배정률(능력·제약 위반 배정, 정답 배정과 다른 배정)을 같은 지시로 여러 번 반복해 분포로 보고한다. [추정][^ref-746][^ref-592]
- 필요한 자료: 화물·로케이션·기한·배정 로봇을 정답에 담은 물류 지시–정답 쌍(q5-04), 가상 현장·가상 로봇
- 제안한 실행 id: 2026-09-25-86
- 상태: 제안(사용자 수행 대기)

### E5-02 온톨로지 질의 대 LLM 로봇 선택의 반복 일치율·근거 추적 (가설 2)

- 목적: 로봇 선택을 온톨로지 질의(능력·제약 대조)에 맡기면 LLM 선택보다 배정 근거를 설명·재현할 수 있는지 본다.
- 방법: 같은 작업 요구로 온톨로지 질의와 LLM 선택을 각각 반복 시행한다.
- 측정 지표와 조건: 반복 시행 사이 선택 결과의 일치율, 선택 근거를 능력·제약 항목으로 되짚을 수 있는 비율. 결정적으로 설정한 LLM 도 반복 실행에서 결과가 달라질 수 있다는 보고가 있어 반복 횟수를 함께 적는다. [추정][^ref-746]
- 필요한 자료: 로봇 능력 정보(선언 능력과 측정한 운용 능력을 구분), 작업 요구 세트
- 제안한 실행 id: 2026-09-25-86
- 상태: 제안(사용자 수행 대기)

### E5-03 해법기·검증된 규칙 대 LLM 직접 스케줄 (가설 3, 최근접 기준선 포함)

- 목적: 스케줄링을 결정적 구성 요소(해법기 또는 검증을 거친 규칙 실행기)에 두는 분담이 LLM 직접 스케줄보다 운영을 안정적으로 만드는지 본다.
- 방법: 같은 피킹 운반 지시 흐름과 교란을 최근접 배정 기준선, 해법기·검증된 규칙, LLM 직접 스케줄 세 방식에 똑같이 재생한다. [추정][^ref-400][^ref-592]
- 측정 지표와 조건: 실행 가능 비율, 납기 지연, 재스케줄 뒤 작업 시작 시각 편차. [추정][^ref-592][^ref-734] 최근접 기준선 대비 대기·지연 차이로 분류 원문 13. 작업 배정 — MRTA 의 SCM 관점 질문도 함께 본다. [추정][^ref-400]
- 필요한 자료: 창고 레이아웃(피킹 구역·도크)과 지시 흐름(자체 구축), 교란 시나리오
- 제안한 실행 id: 2026-09-25-86
- 상태: 제안(사용자 수행 대기)

결과는 `experiments/<날짜>-<이름>/`에 넣고 `README.md` 머리에 트랙(`nl-task-chatbot`), 단계(5), 답하려는 질문 id(q5-03)와 계획 번호를 적는다.

[^ref-746]: Atil, B. 외, Non-Determinism of "Deterministic" LLM Settings, 2024-08, https://arxiv.org/abs/2408.04667, 접근일 2026-09-25 (원문 미열람)
[^ref-592]: ConstraintBench 저자(arXiv 2602.22465, 저자 미확인), ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization, 2026-02, https://arxiv.org/abs/2602.22465, 접근일 2026-09-25 (원문 미열람)
[^ref-734]: Rangsaritratsamee, R., Ferrell Jr., W. G., & Kurz, M. B.(Computers & Industrial Engineering 46), Dynamic rescheduling that simultaneously considers efficiency and stability, 2004, https://www.sciencedirect.com/science/article/abs/pii/S0360835203000950, 접근일 2026-09-25 (원문 미열람)
[^ref-400]: International Journal of Planning and Scheduling 게재 논문(저자 미확인), Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors, 2019, https://www.inderscience.com/info/inarticle.php?artid=103016, 접근일 2026-09-25 (원문 미열람)

## 사용자 실험 결과 요약

아직 없음.
