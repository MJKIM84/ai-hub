# 스토리텔러 산출 2026-09-29-05

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | draft | 3~11절 신규 작성(seed → draft), 출처 18건(ref-165~ref-847, ref-110·ref-111·ref-125 재사용), 병원·실외 사례 2건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 10건과 2차 수정 지시 8건(10절 연결 다섯 항목·8절 FLEET·3절 의견 주체·11절 보조 문장의 태그·문구 수정) 이행 |
| create | docs/topics/2026/2026-09-29-area12-s6.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "6. 대표 접근법과 기술" 절(3,807자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s8.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "8. 대표 연구와 자료" 절(1,970자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s7.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,291자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s10.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,270자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s4.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "4. 핵심 개념과 용어" 절(1,255자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s3.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "3. 왜 중요한가" 절(1,149자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area12-s11.md | draft | 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 의 "11. 열린 질문" 절(852자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 12. 채팅으로 업무 지시·오케스트레이션 | 3~11절 신규 작성(seed → draft), 출처 18건, 병원·실외 사례 2건, 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 10건과 2차 수정 지시 8건 이행 | run 2026-09-29-05
- 홈 최근 업데이트: 2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft). 언어 모델 작업 분해·배정(SMART-LLM·DART-LLM·FLEET), 실행 전 검증·승인(VerifyLLM·HMCF), 기록 근거의 진행·실패 설명, Open-RMF 작업 요청·상태 스키마와 MCP 서버 공지를 정리. 출처 18건, 병원·실외 사례 2건, 열린 질문 4건
- 대분류 최근 업데이트: 2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft), 출처 18건(ref-165~ref-847, ref-110·ref-111·ref-125 재사용), 병원·실외 사례 2건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 10건과 2차 수정 지시 8건 이행 (실행 2026-09-29-05)
- 세부영역 최근 업데이트: 2026-09-29 — 12. 채팅으로 업무 지시·오케스트레이션: 3~11절 신규 작성(seed → draft). 대화 지시→작업 그래프→배정 엔진→사전 검증→사람 승인→관제 작업 요청→상태 기록 근거 설명의 흐름을 구축자 추정으로 정리하고, 승인 단위·재승인 범위·MCP 승인 관문·국내 사례의 열린 질문 4건을 올림 (실행 2026-09-29-05)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사전 실행 계획 검증 | Pre-execution Plan Verification | 언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다. | 12, 13, 44, 54 | ref-753 |
| new | 감독 제어 | Supervisory Control | 사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다. | 12, 13, 31 | ref-165, ref-855 |
| new | 실패 설명 | Failure Explanation | 로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다. | 12, 32, 38 | ref-453 |
| new | 로봇–작업 적합도 행렬 | Robot–Task Fitness Matrix | 로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다. | 12, 25, 5 | ref-242 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 논문 | medium | https://arxiv.org/abs/2502.03814 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-059 | Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H. | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D. | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 논문 | medium | https://arxiv.org/abs/2510.07417 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 논문 | medium | https://arxiv.org/abs/2507.05118 |
| ref-777 | Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J. | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 논문 | medium | https://arxiv.org/abs/2510.10379 |
| ref-855 | Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S. | HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2505.00820 |
| ref-677 | Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 논문 | medium | https://arxiv.org/abs/2511.22354 |
| ref-857 | Argenziano, F., Umili, E., Leotta, F., & Nardi, D. | Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning | 논문 | medium | https://arxiv.org/abs/2509.16006 |
| ref-858 | 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)) | 거대언어모델 기반 로봇 인공지능 기술 동향 | 정부·연구기관 | high | https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html |
| ref-859 | Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025) | Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent | 논문 | medium | https://arxiv.org/abs/2410.06472 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. (CoRL 2023) | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 논문 | medium | https://arxiv.org/abs/2306.15724 |
| ref-861 | Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y. | Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges | 논문 | medium | https://arxiv.org/abs/2605.02592 |
| ref-862 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 |
| ref-847 | Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer) | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 논문 | medium | https://link.springer.com/article/10.1007/s10514-026-10255-6 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? | 12, 13 | 열림 | — |
| new | — | 사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? | 12, 32 | 열림 | — |
| new | — | 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? | 12, 20, 13 | 열림 | — |
| new | — | 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? | 12, 61, 63, 62 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 병원 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 병원 | 예외·성과 | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 실외 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 실외 | 완료·인계 | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md#5-적용-사례-현장-유형-명시 | 12. 채팅으로 업무 지시·오케스트레이션 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) | 오픈소스 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | 12, 13, 44, 54 | ref-753 | https://arxiv.org/abs/2507.05118 |

## 추가 조사 요청

- 5절 적용 사례에 물류창고·제조 공장·상업 시설에서 대화로 여러 로봇에 업무를 지시한 실제 사례가 필요하다 — 이번 브리프는 병원(원문 미열람)·실외(초록만) 두 사례뿐이다. MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(403 으로 미열람)를 다시 열어 제조 공장 사례로 쓸 수 있는지 확인이 필요하다.
- 5절 병원 사례(ref-847)의 작업 대상·제약·완료·인계 항목과 정량 결과, 실행 전 사람 승인 절차 유무가 필요하다 — Springer 원문을 열지 못해 검색 결과 요약 범위만 옮겼다. 원문 열람(또는 저자 공개 판) 뒤 여섯 항목을 채워야 한다.
- 6절 실행 중 재계획 절에 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)이 필요하다 — 검색 결과 요약에서만 보여 finding 에 넣지 못했다. 논문 본문에서 확인이 필요하다.
- 3절·11절의 승인 부담 논의에 승인 단위(전체 계획 1회·단계별·변경분만)와 로봇 수에 따른 검토 부담을 다룬 연구가 필요하다 — 서베이는 미정량화만 지적했다. 예산 상한으로 넣지 못한 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)를 다음 실행에서 확인하면 6·8절을 보강할 수 있다.
- 7절에 OSRA 세션의 실제 발표 자료·MCP 서버 저장소 URL 이 필요하다 — 이번에는 세션 공지(2026-06-25 게시)만 확인했고 세션 진행 내용과 승인 관문 유무는 미확인이다.
- 8절·11절의 국내 자료에 ETRI 동향 논문 외의 국내 대화형 업무 지시 사례가 필요하다 — 한국어 검색에서 찾은 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 대화형 지시가 아니어서 제외됐다.
- 10절 연결 항목 가운데 '9. 채팅으로 시나리오 구성이 기한·반복·실패 처리 조건을 정해 이 영역의 지시에 넣는다'와 '로봇–작업 적합도 행렬(FLEET)·로봇별 능력 이해(HMCF)가 능력 표현을 전제한다'는 연결은 브리프에 finding 이 없어 [추정]으로 남겼다 — 두 연결을 뒷받침하는 출처(FLEET·HMCF 본문의 능력 표현 형식, 시나리오 모델과 작업 요청의 필드 대응)를 다음 실행에서 확인하면 [사실]로 올릴 수 있다.

## 이행한 수정 지시

- ref-862 발행일·f19 문구 — 13절 각주와 reference_updates 의 ref-862 발행일을 2026-06-25 로 고치고 제목은 그대로 두었으며, 3절·4절·7절에서 f19 를 쓰는 문장을 '2026-07-02 세션 공지(2026-06-25 게시)에서 … 다룬다고 밝혔으며' 형식으로 썼다. 7절 표에도 '공지에서 밝힘' 으로 적었다.
- f25/ref-847 병원 이름·저자·미열람 표시 — 5절 병원 사례 표와 서술, 10절 63. 병원·의료 연결에서 '국립대만대학병원' 을 빼고 '(병원 이름 미확인)' 으로 썼으며, 각주 저자를 'Chiang, Y.-C., Lee, I.-P., & Fu, L.-C. (Autonomous Robots, Springer)' 로 적고 접근일 뒤에 ' (원문 미열람)' 을 붙였고, reference_updates 의 ref-847 에 source_unopened: true 를 넣었다. 기준일은 '2026(발행월 미확인)' 으로 남겼다.
- f10 연구 그룹 수 — 6절 '실행 전 자동 검증과 사람 승인' 의 교차 확인 문장을 '서로 다른 두 연구 그룹 이상(Hunt 외의 실행 전 승인과 HMCF 는 저자가 겹치는 같은 그룹, VerifyLLM 은 독립 그룹)' 으로 고쳤다. [사실] 태그와 세 각주(ref-165·ref-855·ref-753)는 유지했다.
- f8 가정 현장 유형 제외 — 5절에 '가정' 사례를 세우지 않았고 site_matrix_updates 에 가정 칸을 넣지 않았다. VerifyLLM 은 4절 용어와 6절·7절·8절에서만 다루고 '가정 작업 데이터셋으로 평가(실제 현장 아님)' 을 명시했다.
- 5절 사례 범위·미확인 처리 — 병원(f25)·실외(f13) 두 사례만 세우고, 병원 사례는 작업 대상·제약·완료·인계를, 실외 사례는 작업 대상·수행 자원·제약·예외·성과를 '미확인' 으로 남겼으며, 절 첫머리에 물류창고·제조 공장·상업 시설 사례가 없다고 밝혔다. site_matrix_updates 는 채운 칸(병원 3칸, 실외 2칸)만 냈다.
- f12·f21 연계 대상 표시 — 6절 '실행 중 재계획과 사람 도움 요청' 에서 CoMuRoS 의 로봇별 지역 언어 모델 코드 생성을 같은 문단에서 '로봇 자체 지능·제어 연계 대상' 으로 밝혔고, 7절 표 아래 문단에서 ROSA 를 같은 이유로 연계 대상이라고 적었으며 9절 표의 '외부와 연계하는 것' 열에도 두 항목을 두었다. ROP 가 직접 맡는 기능처럼 쓰지 않았다.
- f23 문헌 고찰 범위 — 3절과 8절에서 '산업 자동화 일반(로봇 한정 아님)의 기반 모델 에이전트 문헌 고찰(88편)' 임을 명시하고, 75.0%·9.1% 수치가 '그 문헌 집합에서 보고된 시스템' 에 대한 값임을 밝혔다.
- [추정] 문장의 구축자 추정 표시·각주 — f7(6절·10절), f11(6절), f16(6절), f20(3절·6절), f26(9절), f27(6절·7절·9절), f28(10절)을 쓴 모든 문장을 '…라는 것이 구축자 추정이다' 형식으로 쓰고 근거 finding 의 출처 각주(f7: ref-242·ref-059, f11: ref-165·ref-753·ref-855, f16: ref-453·ref-857·ref-111, f20: ref-862·ref-110·ref-125, f26: ref-242·ref-753·ref-677·ref-111·ref-110, f27: ref-677·ref-859·ref-110, f28: ref-165·ref-861·ref-753)를 붙였다.
- f4·f9·f12 수치의 저자 실험 조건 병기 — 6절과 8절에서 DART-LLM 의 모델별 성공률·응답 시간, HMCF 의 +4.76%, CoMuRoS 의 9/10·8/8·5/5·0.91 을 쓴 문장마다 '(저자 실험 조건)' 을 병기했다.
- ref-165 열람 판 표시 — 13절 각주를 '2025-02-06 (열람 판 v5 2026-05-03)' 으로 쓰고, 3절과 8절의 f2 서술에 '2026-05-03 판 기준' 을 밝혔다.
- 2차: 10절 37. 관제 화면·실행 기록 항목 — 세부영역 페이지 10절 원문에서 '…작업 상태·단계·사건 기록(Open-RMF task_state)을 이 영역이 조회한다는 것이 구축자 추정이다. [추정][^ref-111]' 로 고쳤다(f16 태그 복원). 분리 페이지는 코드가 다시 만들도록 출력에 넣지 않았다.
- 2차: 10절 20. 로봇·제조사 관제 연동 항목 — '…MCP 서버로 관제 API를 노출하는 구현이 이 연동을 통과한다는 것이 구축자 추정이다. [추정][^ref-110][^ref-125][^ref-862]' 로 고쳤다(f20 태그 복원, 각주 세 개 유지).
- 2차: 10절 32. 예외 복구·재계획·업무 연속성 항목 — 두 문장으로 나눠 'CoMuRoS는 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획하고 필요하면 로봇이 사람 도움을 요청하게 한다고 보고했다. [사실][^ref-677]' 와 '이 재계획이 승인된 계획과의 차이 표시·재승인 문제로 이 영역과 이어진다는 것이 구축자 추정이다. [추정][^ref-677]' 로 썼다(f12 사실·f26 추정 분리).
- 2차: 10절 9. 채팅으로 시나리오 구성 항목 — '…시나리오 모델에서 정해져 이 영역의 지시에 들어온다는 것이 구축자 추정이다. [추정][^ref-125]' 로 고쳤다(finding 없는 연결 해석을 추정으로 강등). 근거 확인 요청을 additional_research_requests 에 더했다.
- 2차: 10절 10. 채팅으로 로봇 구성 · 5. 로봇 능력·작업 표현 항목 — '…능력 표현이 있어야 성립한다는 것이 구축자 추정이다. [추정][^ref-242][^ref-855]' 로 고쳤다(초록에 없는 해석을 추정으로 강등).
- 2차: 8절 FLEET 항목 — [사실] 문장을 '…2단계 혼합 방식. [사실][^ref-242]' 에서 끝내고, 역할 분담 구절을 '이 방식을 이 영역과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 역할 분담 근거로 삼는다는 것이 구축자 추정이다. [추정][^ref-242][^ref-059]' 로 따로 썼다(f7 추정 분리).
- 2차: 3절 첫 문장 — 세부영역 페이지 3절 원문을 '…로봇 동작과 가장 가까운 자리에 있다는 것이 구축자 의견이다. [의견]' 으로 고쳤다. 코드가 다시 분리하는 주제 페이지의 1절·3절에도 같은 문장이 옮겨진다.
- 2차: 11절 두 번째 열린 질문 보조 문장 — 'CoMuRoS는 사건 기반 재계획을 보고했지만 재승인 기준은 초록에서 확인되지 않았다. [사실][^ref-677]' 로 고쳤다(초록 범위를 넘는 부재 진술 제거).
- 분량 초과 자동 분리: 12. 채팅으로 업무 지시·오케스트레이션 본문 13,989자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,201자
