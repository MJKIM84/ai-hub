---
title: "9. 채팅으로 시나리오 구성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 9
related_areas: [10, 12, 13, 20, 24, 26, 32, 33, 36, 44, 47, 63]
tags: [명확화 질문, 불확실도 정렬, 과소명세, 상황 상태 추적, 미션 명세 패턴, 작업 요청 스키마]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-351, ref-839, ref-840, ref-841, ref-842, ref-843, ref-844, ref-061, ref-845, ref-846, ref-110, ref-125, ref-548, ref-847, ref-848]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 9. 채팅으로 시나리오 구성

# 9. 채팅으로 시나리오 구성

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-29 · 마지막 실행: 2026-09-29
<!-- auto:page-status:end -->

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]

## 3. 왜 중요한가

이 영역의 핵심 위험은 언어 모델(Large Language Model, LLM)이 여러 턴에 걸친 대화에서 이미 합의한 내용을 잃거나 초기 가정에 묶여 잘못된 시나리오를 만드는 것이며, 최근의 다중 턴 대화 연구가 이 위험을 수치로 보여 준다. [추정][^ref-840][^ref-841]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 왜 중요한가](../../topics/2026/2026-09-29-area09-s3.md)에 있다.

## 4. 핵심 개념과 용어

**과소명세(Underspecification)** — 사용자 지시에 실행에 필요한 조건(대상·장소·수량·기한 등)이 빠져 여러 해석이 가능한 상태다. Deng 외(2026)는 과소명세된 지시의 의도 불확실성이 잘못된 도구 호출로 이어진다고 보고, [명확화 질문](../../glossary/clarification-question.md)으로 이를 줄이는 모델을 학습했다. [사실][^ref-839]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area09-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 간호 인력의 자연어 지시를 병원 보조 로봇의 작업 순서열로 바꾸고 실행 중 추가 요청을 반영

| 항목 | 내용 |
|---|---|
| 시작 조건 | 간호 인력이 보조 로봇에 자연어로 내리는 지시가 작업을 발생시키고, 실행 중 들어오는 추가 요청이 재스케줄링을 일으킨다(원문 미열람). [추정][^ref-847] |
| 작업 대상 | 지시 문장에서 만들어 낸 실행 가능한 작업 순서열(정보)이며, 지시가 다루는 물품·장소의 종류는 원문 미열람으로 확인하지 못했다. [추정][^ref-847] |
| 수행 자원 | Temi 로봇과 맞춤 안드로이드 앱, AI 기반 작업 계획기와 키워드 검색, 지시를 내리는 간호 인력이 맡는다(원문 미열람). [추정][^ref-847] |
| 제약 | 이 영역의 관점에서는 사람이 승인한 시나리오만 실행 단계로 넘기고, 실행 중 대화로 들어온 변경은 확정본에 대한 차이로 표시해 다시 승인받아야 한다. 사례 논문이 승인 절차를 두었는지는 밝히지 않았다. [추정][^ref-847][^ref-840][^ref-841] |
| 완료·인계 | 미확인 — 원문 미열람으로 완료 확인 절차를 확인하지 못했다. |
| 예외·성과 | 실행 실패는 시각-언어 추론과 AI 제안으로 복구하며, 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. 처리량·시간·비용에 대한 정량 성과는 미확인이다(원문 미열람). [추정][^ref-847] |

이 사례는 Autonomous Robots(Springer, 2026)에 실린 연구를 검색 결과 요약으로 확인한 것이며, 원문을 열지 못해 정량 결과와 확인 절차는 미확인이다. 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. [추정][^ref-847]

이 영역이 관여하는 항목은 시작 조건과 제약이다. 실행 중 들어온 추가 요청이 곧바로 재스케줄링으로 이어진 점과 다중 턴에서 합의가 흔들리는 문제를 함께 보면, 채팅 시나리오 구성은 실행 전 합의된 시나리오를 확정본으로 잠그고 실행 중 대화로 들어온 변경은 확정본에 대한 차이로 표시해 다시 승인받는 절차를 두어야 하며, 그 실행·재계획 자체는 [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md)과 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)이 맡는 것이 원문 구분에 맞을 것으로 보인다. [추정][^ref-847][^ref-840][^ref-841]

(이번 실행의 브리프에는 제조 공장·물류창고 등 다른 현장 유형에서 대화로 시나리오를 구성한 사례가 없다. 물류 자율이동로봇 임무 명세를 다룬 학위논문은 현장 유형을 특정하지 않아 3절과 6절에서만 다룬다.)

## 6. 대표 접근법과 기술

되묻기 시점을 불확실도로 정하고 질문 내용을 정보 이득으로 고르는 두 계열의 연구가 이 영역의 '모자란 조건은 선택지와 이유를 붙인 질문으로 채운다'는 기능의 근거가 된다. [추정][^ref-351][^ref-839]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area09-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역이 대화로 정하려는 값 가운데 할 일·순서(compose 활동 순서열)·물품 인계(PickUp·DropOff)·시작 조건(가장 이른 시작 시각)·우선순위·요청자·수행 플릿은 Open-RMF 작업 구성과 작업 요청에 이미 자리가 있으나, 완료 기한·반복·실패 처리 조건은 작업 요청 스키마에 자리가 없으므로 채팅 시나리오 구성의 결과물은 관제 작업 요청보다 넓은 시나리오 모델([33. 시나리오 모델·편집](../design-and-simulation/scenario-model-and-editing.md), [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md))에 담고 실행 시점에 작업 요청으로 변환해야 할 것으로 보인다. [추정][^ref-110][^ref-125]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area09-s7.md)에 있다.

## 8. 대표 연구와 자료

Ren 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners(CoRL 2023) — 등각 예측으로 예측 집합을 만들어 여럿이 남을 때만 되묻는 KnowNo 틀. 이 영역에서 되묻기 시점을 정하는 기준의 출발점이다. [사실][^ref-351]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area09-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 대화를 값마다 출처가 붙은 구조화 시나리오(할 일·물품·사람·순서·반복·기한·실패 처리 조건)로 바꾸고, 불확실한 항목만 선택지와 이유를 붙여 되묻고, 워크플로 모델과 실행 지향 검사로 시나리오의 유효성을 확인하며, 합의본을 보존·차이 표시하고 사람이 승인한 시나리오만 실행 단계로 넘긴다. [추정][^ref-351][^ref-842][^ref-844][^ref-110] | 연계 대상: 자연어에서 로봇 수준 행동 트리를 생성해 로봇에서 실행하는 일과, 자연어를 LTL·STL 공식으로 옮겨 형식 계획기·모델 검사기로 계획을 만드는 일. ROP는 시나리오의 순서·기한·실패 처리 조건을 이들 도구가 읽을 수 있는 인터페이스로 넘기고 결과(실행 가능 여부·검증 결과)를 받아 대화로 설명하는 데 그친다. [추정][^ref-061][^ref-845][^ref-548] |
| 시설·설비 제어 | 승강기 이동이 필요한 시나리오임을 작업 구성에 남기고 그 단계의 완료를 확인한다. [추정][^ref-110] | 연계 대상: 승강기 호출 자체. Open-RMF 는 필요할 때 RequestLift 단계를 내부에서 자동으로 넣는다. [사실][^ref-110] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역에서 ROP가 맡는 네 기능(구조화 시나리오, 되묻기, 유효성 검사, 승인 게이트)을 하나로 묶은 시스템 사례는 확인하지 못했으며, 위 표의 직접 범위는 되묻기 기준·구조화 상태·실행 지향 검사·관제 작업 형식의 개별 연구에서 도출한 추정이다. [추정][^ref-351][^ref-842][^ref-844][^ref-110] 범위 경계의 원문 표는 [ROP 범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[33. 시나리오 모델·편집](../design-and-simulation/scenario-model-and-editing.md) — 원문 주석대로 시나리오 구성 대화가 부르는 엔진 영역이며, 기한·반복·실패 처리처럼 관제 작업 요청에 자리가 없는 항목을 담는 시나리오 모델이 여기에 속한다. [추정][^ref-110][^ref-125]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area09-s10.md)에 있다.

## 11. 열린 질문

(id 미부여 · 상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-04) 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가?[^ref-846]

자세한 내용은 주제 페이지 [9. 채팅으로 시나리오 구성 — 열린 질문](../../topics/2026/2026-09-29-area09-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-29 · 갱신 · [9. 채팅으로 시나리오 구성](chat-scenario-composition.md) — 3~11절 신규 작성(seed → draft), 출처 15건(ref-351~ref-848), 병원 사례 1건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-04)
- 2026-09-29 · 생성 · [9. 채팅으로 시나리오 구성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area09-s6.md) — 자동 분리: 9. 채팅으로 시나리오 구성 의 "6. 대표 접근법과 기술" 절(2,863자)을 옮겼다 (실행 2026-09-29-04)
- 2026-09-29 · 생성 · [9. 채팅으로 시나리오 구성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area09-s8.md) — 자동 분리: 9. 채팅으로 시나리오 구성 의 "8. 대표 연구와 자료" 절(1,570자)을 옮겼다 (실행 2026-09-29-04)
- 2026-09-29 · 생성 · [9. 채팅으로 시나리오 구성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area09-s4.md) — 자동 분리: 9. 채팅으로 시나리오 구성 의 "4. 핵심 개념과 용어" 절(1,364자)을 옮겼다 (실행 2026-09-29-04)
- 2026-09-29 · 생성 · [9. 채팅으로 시나리오 구성 — 왜 중요한가](../../topics/2026/2026-09-29-area09-s3.md) — 자동 분리: 9. 채팅으로 시나리오 구성 의 "3. 왜 중요한가" 절(1,211자)을 옮겼다 (실행 2026-09-29-04)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29
[^ref-839]: Deng, M., Li, Z., Li, X., Zhu, T., Zhao, Y., Guo, Z., & Wang, W., Uncertainty-Aware Clarification in LLM Agents with Information Gain, 2026-06-02, https://arxiv.org/abs/2606.03135, 접근일 2026-09-29
[^ref-840]: Laban, P., Hayashi, H., Zhou, Y., & Neville, J., LLMs Get Lost In Multi-Turn Conversation, 2025-05-09, https://arxiv.org/abs/2505.06120, 접근일 2026-09-29
[^ref-841]: Tack, J., Laban, P., & Neville, J., LLMs Get Lost in Evolving User Intent, 2026-07-22, https://arxiv.org/abs/2607.20734, 접근일 2026-09-29
[^ref-842]: Tao, M., Tao, Y., & Wang, P., Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents, 2026-08-16, https://arxiv.org/abs/2608.15755, 접근일 2026-09-29
[^ref-844]: Matei, I., Zhenirovskyy, M., Menaka Sekar, P. K., & Wong, H. Y., Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach, 2026-04-13, https://arxiv.org/abs/2604.12105, 접근일 2026-09-29
[^ref-061]: Izzo, R. A., Bardaro, G., & Matteucci, M., BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs, 2024-03-19, https://arxiv.org/abs/2403.12761, 접근일 2026-09-29
[^ref-845]: Sundarsingh, D. S., Wang, J., Deshmukh, J. V., & Kantaros, Y., ConformalNL2LTL: Translating Natural Language Instructions into Temporal Logic Formulas with Conformal Correctness Guarantees, 2026-02-20, https://arxiv.org/abs/2504.21022, 접근일 2026-09-29
[^ref-846]: Menghi, C., Tsigkanos, C., Pelliccione, P., Ghezzi, C., & Berger, T., Specification Patterns for Robotic Missions, 2019-01-07, https://arxiv.org/abs/1901.02077, 접근일 2026-09-29
[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-29
[^ref-548]: University West (Högskolan Väst, DiVA) 학위논문 저자(미확인), An LLM- Interface for Robot Mission Specification in Logistics, 미확인, https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf, 접근일 2026-09-29 (원문 미열람)
[^ref-847]: Chiang, Y.-C., Lee, I.-P., Fu, L.-C. 외 (Autonomous Robots 50, Article 28, 2026), Agile assistive hospital robot for suboptimal Task execution in dynamic environments, 2026, https://link.springer.com/article/10.1007/s10514-026-10255-6, 접근일 2026-09-29 (원문 미열람)
