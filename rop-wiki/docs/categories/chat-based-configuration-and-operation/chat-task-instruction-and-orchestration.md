---
title: "12. 채팅으로 업무 지시·오케스트레이션"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 12
related_areas: [5, 9, 10, 13, 20, 24, 25, 26, 32, 37, 44, 47, 63, 66]
tags: [언어 모델 작업 분해, 실행 전 승인, 사전 실행 계획 검증, 작업 상태 질의, 모델 컨텍스트 프로토콜, 이기종 로봇 배정]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-165, ref-090, ref-059, ref-242, ref-753, ref-777, ref-849, ref-677, ref-850, ref-851, ref-852, ref-453, ref-853, ref-854, ref-847, ref-110, ref-111, ref-125]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 12. 채팅으로 업무 지시·오케스트레이션

# 12. 채팅으로 업무 지시·오케스트레이션

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

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]

## 3. 왜 중요한가

대화로 받은 지시가 로봇 동작으로 이어지려면 지시를 계획으로 바꾸는 일, 그 계획을 사람이 확인·승인하는 일, 실행 뒤 진행을 설명하는 일이 한 흐름으로 이어져야 하며, 이 영역은 C. 채팅 기반 구성·운영 가운데 로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 왜 중요한가](../../topics/2026/2026-09-29-area12-s3.md)에 있다.

## 4. 핵심 개념과 용어

**[작업 분해](../../glossary/task-decomposition.md)·[연합 형성](../../glossary/coalition-formation.md)·작업 배정(Task Decomposition, Coalition Formation, Task Allocation)** — SMART-LLM은 상위 작업 지시를 이 세 단계로 나누어 다중 로봇 작업 계획으로 바꾸고, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시킨다. [사실][^ref-090]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area12-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 현장 유형은 병원과 실외(정밀 농업)뿐이며, 물류창고·제조 공장·상업 시설에서 대화로 로봇 업무를 지시한 사례는 확인되지 않았다. 병원 사례는 원문을 열지 못해 검색 결과 요약 범위만 옮겼고, 실외 사례는 논문 초록만 확인했으므로 출처로 확인되지 않은 항목은 "미확인"으로 남긴다.

**현장 유형:** 병원

**사례:** 병원에서 간호 인력이 보조 로봇에게 자연어로 업무를 지시하고 실행 중 추가 요청을 반영

| 항목 | 내용 |
|---|---|
| 시작 조건 | 간호 인력의 자연어 지시가 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바뀌고, 실행 중 들어오는 추가 요청이 재스케줄링을 촉발한다. [사실][^ref-847] |
| 작업 대상 | 미확인(원문 미열람) |
| 수행 자원 | Temi 로봇과 맞춤 안드로이드 앱, 지시를 내리는 간호 인력. [사실][^ref-847] |
| 제약 | 미확인(원문 미열람) |
| 완료·인계 | 미확인(원문 미열람) |
| 예외·성과 | 실행 실패는 시각-언어 추론과 AI 제안으로 복구하며, 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다(정량 결과 미확인). [사실][^ref-847] |

Autonomous Robots(Springer, 2026, 발행월 미확인) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패를 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치했다고 보고했다(병원 이름 미확인, 원문 미열람). [사실][^ref-847] 이 사례에서 이 영역이 관여하는 항목은 시작 조건(대화 지시→작업 순서열)과 예외·성과(실패 복구와 재스케줄링)이며, 실행 전 사람 승인 절차가 있었는지는 확인되지 않았다.

**현장 유형:** 실외

**사례:** 실외 정밀 농업 현장에서 자연어로 활동을 지정하고 로봇에 질의해 실행 진행을 확인

| 항목 | 내용 |
|---|---|
| 시작 조건 | 사람이 자연어로 상위 활동을 지정하면 언어 모델과 자동 계획이 결합된 구조가 이를 실행 가능한 형태로 만든다. [사실][^ref-850] |
| 작업 대상 | 미확인(초록에 없음) |
| 수행 자원 | 미확인(로봇 종류·대수는 초록에 없음) |
| 제약 | 미확인(초록에 없음) |
| 완료·인계 | 사람이 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있다. [사실][^ref-850] |
| 예외·성과 | 미확인(초록에 없음) |

Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다. [사실][^ref-850] 이 사례는 이 영역의 "채팅으로 진행 상황 질의·결과 설명"에 해당하며, 답의 근거가 되는 기록이 어떤 형식인지는 초록에서 확인되지 않았다.

## 6. 대표 접근법과 기술

대화 지시를 다중 로봇 계획으로 바꾸는 연구는 지시를 하위 작업으로 분해하고 의존 관계와 능력에 맞춰 로봇에 배정하는 공통 틀을 갖는다. SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. [사실][^ref-090]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area12-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

ROSA는 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트이므로 분류 원문 19장의 "로봇 자체 지능·제어"에 해당하는 연계 대상이며, CoMuRoS의 로봇별 지역 언어 모델 코드 생성과 마찬가지로 ROP가 직접 맡는 기능이 아니라는 것이 구축자 추정이다. [추정][^ref-852][^ref-677][^ref-110] Open-RMF 관련 항목은 [표준·프레임워크 목록](../../standards/index.md)의 기존 항목이며, 이번 실행에서 새로 든 것은 VerifyLLM이다.

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area12-s7.md)에 있다.

## 8. 대표 연구와 자료

Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey(2025, v5 2026-05-03) — 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정·중간 수준 동작 계획·하위 수준 행동 생성·사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. [사실][^ref-165]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료](../../topics/2026/2026-09-29-area12-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 대화로 받은 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보낸다 | 요청·기한·자원 제약을 내는 업무 시스템 자체(수요예측·구매·재무·전사 자원 계획) |
| 로봇 자체 지능·제어 | 플릿 작업 API 수준의 요청과 상태·실패·완료 확인, 관제의 작업 상태·단계 사건 기록을 근거로 한 진행·실패 설명, 실행 중 재계획을 승인된 계획과의 차이로 표시하는 일 | 로봇별 언어 모델의 실행 코드 생성·스킬 실행(CoMuRoS), ROS 토픽·서비스 직접 조작(ROSA), 센서 인식·SLAM·로컬 회피·모터 제어 |

확인한 자료를 종합하면 이 영역에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것이라는 것이 구축자 추정이다. [추정][^ref-242][^ref-753][^ref-677][^ref-111][^ref-110] 연계 대상인 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 "로봇 자체 지능·제어" 쪽이며, 이종 제조사를 연결하는 ROP는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 한다는 것이 구축자 추정이다. [추정][^ref-677][^ref-852][^ref-110] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) · [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md) — 원문 주석대로 업무 지시가 대화로 부르는 짝 엔진이다. 언어 모델은 작업 그래프·능력 요구를 만들고 실제 배정·일정은 이 두 영역의 엔진이 계산한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area12-s10.md)에 있다.

## 11. 열린 질문

**신규(id 부여 예정)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-05) 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? 서베이는 운영자 인지 부담이 정량화되지 않았다고 지적했다. [사실][^ref-165]

자세한 내용은 주제 페이지 [12. 채팅으로 업무 지시·오케스트레이션 — 열린 질문](../../topics/2026/2026-09-29-area12-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-29 · 갱신 · [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md) — 3~11절 신규 작성(seed → draft), 출처 18건(ref-165~ref-847, ref-110·ref-111·ref-125 재사용), 병원·실외 사례 2건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 10건과 2차 수정 지시 8건(10절 연결 다섯 항목·8절 FLEET·3절 의견 주체·11절 보조 문장의 태그·문구 수정) 이행 (실행 2026-09-29-05)
- 2026-09-29 · 생성 · [12. 채팅으로 업무 지시·오케스트레이션 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area12-s6.md) — 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "6. 대표 접근법과 기술" 절(3,807자)을 옮겼다 (실행 2026-09-29-05)
- 2026-09-29 · 생성 · [12. 채팅으로 업무 지시·오케스트레이션 — 대표 연구와 자료](../../topics/2026/2026-09-29-area12-s8.md) — 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "8. 대표 연구와 자료" 절(1,970자)을 옮겼다 (실행 2026-09-29-05)
- 2026-09-29 · 생성 · [12. 채팅으로 업무 지시·오케스트레이션 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area12-s7.md) — 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,291자)을 옮겼다 (실행 2026-09-29-05)
- 2026-09-29 · 생성 · [12. 채팅으로 업무 지시·오케스트레이션 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area12-s10.md) — 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,270자)을 옮겼다 (실행 2026-09-29-05)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-165]: Li, P., An, Z., Abrar, S., & Zhou, L., Large Language Models for Multi-Robot Systems: A Survey, 2025-02-06 (열람 판 v5 2026-05-03), https://arxiv.org/abs/2502.03814, 접근일 2026-09-29
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-29
[^ref-059]: Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H., DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11-13, https://arxiv.org/abs/2411.09022, 접근일 2026-09-29
[^ref-242]: Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D., FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams, 2025-10-08, https://arxiv.org/abs/2510.07417, 접근일 2026-09-29
[^ref-753]: Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025), VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots, 2025-07-07, https://arxiv.org/abs/2507.05118, 접근일 2026-09-29
[^ref-677]: Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning, 2025-11-27, https://arxiv.org/abs/2511.22354, 접근일 2026-09-29
[^ref-850]: Argenziano, F., Umili, E., Leotta, F., & Nardi, D., Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning, 2025-09-19, https://arxiv.org/abs/2509.16006, 접근일 2026-09-29
[^ref-852]: Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025), Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent, 2024-10-09, https://arxiv.org/abs/2410.06472, 접근일 2026-09-29
[^ref-847]: Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer), Agile assistive hospital robot for suboptimal Task execution in dynamic environments, 2026, https://link.springer.com/article/10.1007/s10514-026-10255-6, 접근일 2026-09-29 (원문 미열람)
[^ref-110]: Open Robotics, Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_new.html, 접근일 2026-09-29
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-29
