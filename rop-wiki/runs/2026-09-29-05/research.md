# 리서치 브리프 2026-09-29-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-29-05 |
| 날짜 | 2026-09-29 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 사전 실행 계획 검증·감독 제어·실패 설명·로봇–작업 적합도 행렬 용어 없음(작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시는 용어집에 이미 있음)
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청·작업 상태 스키마, MCP 기반 관제 연결, ROSA·RobotFleet 같은 오픈소스 에이전트 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 짝 연결 필요, 13. 대화형 기능의 신뢰·기반·32. 예외 복구·재계획·업무 연속성·37. 관제 화면·실행 기록 연결 필요
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. 언어 모델이 자연어 업무 지시를 여러 이기종 로봇의 하위 작업으로 분해하고 의존 관계·능력에 맞춰 배정·일정을 제안하는 연구는 무엇이 있고 결과는 어떻게 보고되는가? (섹션 4·6·8 겨냥)
3. 언어 모델이 만든 계획을 실행 전에 자동 검증하고 사람이 승인하게 하는 설계(사전 실행 검증, 감독 제어)는 어떤 것이 있으며 승인 부담은 어떻게 다뤄지는가? (섹션 3·6·11 겨냥)
4. 어디까지 했는지·왜 멈췄는지를 대화로 묻고 실행 기록을 근거로 답하는 연구와, 관제가 제공하는 작업 상태·단계·사건 기록은 무엇인가? (섹션 4·6·7 겨냥)
5. 관제·플랫폼의 작업 요청 API 와 언어 모델 도구 호출(MCP)을 잇는 오픈소스·프레임워크는 무엇이고 승인 단계를 두는가? (섹션 7 겨냥)
6. 병원·제조 공장·물류창고·실외 등 현장 유형별로 대화로 로봇 업무를 지시한 사례와 국내 자료는 무엇인가? (섹션 5·8 겨냥)
7. 채팅 업무 지시에서 ROP가 직접 맡을 것(대화→계획, 검증, 승인, 관제 작업 요청, 진행 설명)과 로봇 수준 코드 생성·스킬 실행·형식 최적화기에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Li 외(2025)의 서베이는 다중 로봇 시스템에 언어 모델을 쓰는 연구를 상위 수준 작업 배정, 중간 수준 동작 계획, 하위 수준 행동 생성, 사람 개입의 네 층으로 나누어 정리한 최초의 전용 서베이라고 밝히며, 조정·확장성·실세계 적응이 단일 로봇·다중 에이전트 시스템과 다른 과제라고 적었다. | ref-165 | 아니오 | medium | 2025-02-06 | — | — |
| f2 | [사실] | Li 외(2025) 서베이의 사람 개입 절은 실행 전에 사람이 계획을 승인하는 방식(Hunt 외), 로봇이 막히면 도움을 요청하는 방식(VADER), 환각을 줄이는 사람 검증 방식(Li 외)을 예로 들고, 사람이 계획을 함께 만드는 파트너가 아니라 오류를 잡는 반응적 역할에 머문다는 점과 로봇 수가 늘 때 운영자 인지 부담이 정량화되지 않았다는 점을 빈틈으로 지적했다. | ref-165 | 아니오 | medium | 2026-05-03 | 제약 | — |
| f3 | [사실] | SMART-LLM(Kannan·Venkatesh·Min, 2023)은 상위 작업 지시를 작업 분해→연합 형성→작업 배정의 세 단계로 다중 로봇 작업 계획으로 바꾸며, 각 단계를 소수 예시(few-shot) 프로그램형 프롬프트로 언어 모델에 수행시키고 네 가지 복잡도의 벤치마크 데이터셋·시뮬레이션·실제 로봇으로 평가했다. | ref-090 | 아니오 | medium | 2023-09-18 | — | — |
| f4 | [사실] | DART-LLM(Wang 외, 2024)은 자연어 지시를 방향 비순환 그래프(DAG)로 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀로, 질의응답형 분해 모듈·로봇 배정 함수·구동 모듈·시각-언어 물체 탐지 모듈로 구성되며 세 복잡도 수준에서 DeepSeek-r1-671B 가 최고 성공률을, Llama-3.1-8B 가 응답 시간 안정성을 보였고 명시적 의존 모델링이 작은 모델의 성능을 눈에 띄게 높였다고 보고했다. | ref-059 | 아니오 | medium | 2024-11-13 | — | — |
| f5 | [사실] | FLEET(Rivera 외, 2025)은 언어 모델 전단이 소요 시간·선후 관계가 붙은 작업 그래프와 능력을 반영한 로봇–작업 적합도 행렬을 만들고, 형식 최적화기가 완료 시간(makespan) 최소화 문제를 풀어 배정하는 2단계 혼합 방식으로, 절제 실험에서 혼합 정수 계획은 시간 구조를, 언어 모델의 능력 매칭은 특수 능력이 필요한 작업을 각각 뒷받침했으며 능력이 다른 사족 로봇 실기로 검증했다. | ref-242 | 아니오 | medium | 2025-10-08 | 수행 자원 | — |
| f6 | [사실] | 서로 다른 세 연구 그룹(SMART-LLM, DART-LLM, FLEET)이 자연어 업무 지시를 언어 모델로 하위 작업으로 분해하고 이기종 로봇에 배정하는 방법을 각각 보고해, '대화 지시→분해→배정' 접근이 한 곳 이상에서 확인된다. | ref-090, ref-059, ref-242 | 예 | medium | 2025-10-08 | — | — |
| f7 | [추정] | FLEET 가 배정·일정은 형식 최적화기에 맡기고 언어 모델은 작업 그래프·능력 매칭에만 쓴 점(f5)과 DART-LLM 이 의존 관계를 DAG 로 명시한 점(f4)을 함께 보면, 이 영역의 '업무 파악·분해·배정·일정 제안'은 언어 모델이 대화를 의존 관계 있는 작업 그래프와 능력 요구로 바꾸고, 실제 배정·일정은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 엔진에 넘겨 계산한 결과를 계획으로 제안하는 혼합 구조가 원문 주석의 짝 연결과 맞을 것으로 보인다. | ref-242, ref-059 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f8 | [사실] | VerifyLLM(Grigorev·Kovalev·Panov, IROS 2025)은 자연어 지시를 선형 시간 논리(LTL)로 옮긴 뒤 언어 모델 추론으로 행동 순서열의 논리적 일관성과 빠진 단계를 실행 전에 찾는 2단계 검증 모듈로, 복잡도가 다른 가정 작업 데이터셋에서 시험했으며 코드를 공개했다. | ref-753 | 아니오 | medium | 2025-07-07 | 가정 / 제약 | — |
| f9 | [사실] | HMCF(Li 외, 2025)는 로봇마다 자기 능력을 이해하고 작업을 실행 가능한 지시로 바꾸는 언어 모델 에이전트를 두고, 작업 검증과 사람 감독으로 환각을 줄이며 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀로, 시뮬레이션에서 기존 계획 방법보다 작업 성공률을 4.76% 높이고 실제 환경에서 최소한의 사람 개입으로 제로샷 일반화를 보였다고 보고했다. | ref-855 | 아니오 | medium | 2025-05-01 | 예외·성과 | — |
| f10 | [사실] | 서로 다른 세 연구 그룹(Li 외 서베이가 정리한 Hunt 외의 실행 전 승인, HMCF 의 작업 검증·사람 감독, VerifyLLM 의 자동 사전 검증)이 언어 모델이 만든 로봇 계획을 실행 전에 검증하거나 사람이 승인하게 하는 설계를 각각 보고해, '실행 전 검증·승인' 접근이 한 곳 이상에서 확인된다. | ref-165, ref-855, ref-753 | 예 | medium | 2026-05-03 | 시작 조건 | — |
| f11 | [추정] | 자동 사전 검증(f8)과 사람 승인(f2·f9·f10)을 함께 보면, 분류 원문의 '사람이 확인·승인한 계획만 실행'은 언어 모델이 낸 계획을 먼저 자동 검증(의존 관계·능력·논리 일관성)으로 걸러 승인자에게는 검토 가능한 구조(작업 그래프·배정·일정)로 보여 주는 방식으로 구현해야 서베이가 지적한 운영자 인지 부담을 줄일 수 있을 것으로 보인다. | ref-165, ref-753, ref-855 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f12 | [사실] | CoMuRoS(Borate 외, 2025)는 중앙 작업 관리자 언어 모델이 자연어 목표를 해석해 정적 규칙과 작업 이력·로봇 상태 같은 동적 정보로 일을 배정하고, 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 만들며, 실패나 사용자 의도 변경이 생기면 사건 기반으로 재계획해 로봇이 동료를 돕거나 중단된 작업을 재개하거나 사람 도움을 요청하게 하는 중앙 숙고·분산 실행 구조로, 실기에서 협업 복구 9/10·협동 운반 8/8·사람 보조 복구 5/5, 22개 시나리오 벤치마크에서 정확도 최대 0.91 을 보고했다. | ref-677 | 아니오 | medium | 2025-11-27 | 예외·성과 | — |
| f13 | [사실] | Argenziano·Umili·Leotta·Nardi(2025)는 언어 모델과 자동 계획을 결합해 사람이 자연어로 상위 활동을 지정하고 로봇에게 질문해 과거·현재·미래 행동에 걸친 실행 진행 상황을 확인할 수 있게 하는 구조를 제안하고, 실제 정밀 농업 시나리오에서 최신 구성요소로 구현해 시험했다. | ref-857 | 아니오 | medium | 2025-09-19 | 실외 / 완료·인계 | — |
| f14 | [사실] | REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 만든 로봇 경험의 계층적 요약을 근거로 언어 모델에 실패 원인을 묻고 그 설명으로 언어 기반 계획기가 실패를 바로잡게 하는 틀로, 다양한 작업·실패 시나리오를 담은 RoboFail 데이터셋에서 정보성 있는 실패 설명이 교정 계획을 돕는다고 보고했다. | ref-453 | 아니오 | medium | 2023-06-27 | 예외·성과 | — |
| f15 | [사실] | 서로 다른 두 연구 그룹(REFLECT, Argenziano 외)이 로봇의 실행 기록·경험 요약을 근거로 언어 모델이 무엇을 했고 왜 실패했는지를 자연어로 설명하거나 질의에 답하게 하는 방법을 각각 보고해, '실행 기록 근거의 진행·실패 설명' 접근이 한 곳 이상에서 확인된다. | ref-453, ref-857 | 예 | medium | 2025-09-19 | 완료·인계 | — |
| f16 | [추정] | 실행 기록 근거의 설명 연구(f14·f15)와 Open-RMF 작업 상태 스키마가 단계·사건·추정 시간·배정 로봇을 담는 점(f17)을 함께 보면, 이 영역의 '채팅으로 진행 상황 질의·결과 설명'은 언어 모델의 대화 기억이 아니라 관제의 작업 상태·단계 사건 기록(37. 관제 화면·실행 기록)을 조회해 시각과 함께 답하는 방식으로 구현해야 하며, 답에 근거 기록의 식별자·시각을 붙이는 것이 13. 대화형 기능의 신뢰·기반의 근거 표시 요구와 맞을 것으로 보인다. | ref-453, ref-857, ref-111 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f17 | [사실] | Open-RMF 작업 상태 스키마(rmf_api_msgs task_state.json)는 작업 상태 값으로 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 를 두고, 활성 단계 id(active), 완료까지 남은 추정 시간(estimate_millis), 배정 로봇(assigned_to 의 group·name), 단계마다 시작·종료 시각·추정·사건(events)·건너뛰기 요청, 그리고 중단(interruptions)·취소(cancellation) 요청 기록을 담는다. | ref-111 | 아니오 | medium | 2026-09-29 | 완료·인계 | — |
| f18 | [사실] | Open-RMF 는 작업을 단계(phase)로 구성하고 Clean·Delivery·Patrol·Compose 범주의 작업 요청을 특정 로봇 지정(robot_task_request) 또는 최적 플릿 위임(dispatch_task_request)으로 보내며, 요청은 범주(category)와 플릿 지원 스키마를 따르는 설명(description)을 필수로, 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·수행 플릿 이름을 선택으로 두고, 이후 작업 취소나 단계 건너뛰기 요청으로 추가 제어를 할 수 있다. | ref-110, ref-125 | 아니오 | medium | 2026-09-29 | 시작 조건 | — |
| f19 | [사실] | Open Source Robotics Alliance(OSRA) 상호운용 SIG 는 2026-07-02 세션에서 Open-RMF REST API 를 언어 모델이 부를 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(MCP) 서버와 평이한 영어 명령을 여러 단계의 RMF 임무로 바꾸는 에이전트(Nayantra)를 다뤘으며, 공지 본문에는 실행 전 사람 확인·승인이나 작업 상태 질의에 관한 언급이 없다. | ref-862 | 아니오 | medium | 2026-07-02 | 시작 조건 | — |
| f20 | [추정] | MCP 도구 호출로 언어 모델이 관제 API 를 직접 부르는 구현(f19)에는 승인 단계가 드러나지 않으므로, 분류 원문의 '대화 결과는 실행 명령이 아니라 계획'이라는 요구를 지키려면 ROP 는 언어 모델의 도구 호출 제안(작업 요청 초안)과 실제 dispatch_task_request 발행 사이에 계획 미리보기·승인 관문을 두고, 승인된 계획만 한 번 관제 작업 요청으로 변환해야 할 것으로 보인다. | ref-862, ref-110, ref-125 | 아니오 | low | 2026-09-29 | 시작 조건 | — |
| f21 | [사실] | ROSA(Royce 외, NASA JPL, IEEE Aerospace 2025)는 ROS 1·ROS 2 로봇 시스템을 자연어로 점검·진단·조작하게 하는 오픈소스 언어 모델 에이전트로, 명령을 잘 정의된 도구로 ROS 에 연결하고 매개변수 검증과 제약 강제 같은 안전 장치를 두며 JPL 화성 실험장·실험실·시뮬레이션의 세 로봇으로 모의 운용을 시연했다. | ref-859 | 아니오 | medium | 2024-10-09 | — | — |
| f22 | [사실] | RobotFleet(Gupta 외, 2025)은 이기종 로봇 플릿을 컨테이너 서비스로 배치하고 언어 모델로 중앙 집중식 다중 로봇 작업 계획·스케줄링을 하며, 공유 선언형 세계 상태와 실행·재계획을 위한 양방향 통신, 모듈형 자율 스택 층을 갖춘 오픈소스 프레임워크다. | ref-777 | 아니오 | medium | 2025-10-12 | — | — |
| f23 | [사실] | Henkel 외(2026)의 체계적 문헌 고찰(88편)은 산업 자동화의 기반 모델 에이전트가 사용자 지원·모니터링 용도에 강하고 사람 상호작용(+37%)·불확실성 처리(+35%)에서 기존 산업 에이전트보다 나으나, 보고된 시스템의 75.0% 가 기술 성숙도 4~6 의 프로토타입·초기 검증 단계이고 배포 지향 근거는 9.1% 에 그치며, 일반화 부족·환각과 출력 불안정·데이터 부족·추론 지연이 지속적 장애물이라고 보고했다. | ref-861 | 아니오 | medium | 2026-05-04 | 예외·성과 | — |
| f24 | [사실] | ETRI 전자통신동향분석 39권 1호(2024-02)의 '거대언어모델 기반 로봇 인공지능 기술 동향'(이준기 외)은 언어 모델의 상식·추론 능력으로 명령을 이해하고 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획과 요소 기술을 수행하는 제어 코드 생성을 자동화하는 흐름을 정리했으며, 다중 로봇 조율이나 사람 승인 절차는 다루지 않고 대규모 계산 자원·데이터·시뮬레이션·물리 테스트베드가 소수 기업에 집중된 점을 한계로 적었다. | ref-858 | 아니오 | medium | 2024-02 | — | — |
| f25 | [사실] | Autonomous Robots(Springer, 2026) 게재 연구는 병원 보조 로봇이 간호 인력의 자연어 지시를 AI 기반 작업 계획기와 키워드 검색으로 실행 가능한 작업 순서열로 바꾸고, 실행 중 추가 요청에 실시간으로 대응해 유전 알고리즘 기반 준최적 방식으로 작업을 다시 일정 잡으며, 실행 실패는 시각-언어 추론과 AI 제안으로 복구하는 시스템을 Temi 로봇과 맞춤 안드로이드 앱에 배치해 국립대만대학병원 간호 인력에게서 긍정적 피드백을 얻었다고 보고했다. | ref-847 | 아니오 | medium | 2026 | 병원 / 시작 조건 | 원문 미열람 |
| f26 | [추정] | 확인한 자료를 종합하면 12. 채팅으로 업무 지시·오케스트레이션에서 ROP가 직접 맡을 범위는 대화 지시를 의존 관계·능력 요구가 붙은 작업 그래프로 바꾸고, 배정·일정 엔진의 결과를 계획으로 제안하며, 자동 검증을 거쳐 사람 승인을 받은 계획만 관제 작업 요청으로 한 번 변환해 보내고, 관제의 작업 상태·단계 사건 기록을 근거로 진행 상황과 실패를 대화로 설명하는 일이며, 실행 중 재계획은 승인된 계획과의 차이로 표시해 32. 예외 복구·재계획·업무 연속성과 함께 다루는 것이 맞을 것으로 보인다. | ref-242, ref-753, ref-677, ref-111, ref-110 | 아니오 | low | 2026-09-29 | 완료·인계 | — |
| f27 | [추정] | 연계 대상: 로봇별 지역 언어 모델이 보유 스킬로 실행 코드를 생성하는 일(CoMuRoS)과 ROS 토픽·서비스·매개변수를 직접 다루는 에이전트(ROSA)는 분류 원문 19장의 로봇 자체 지능·제어 쪽이며, 이종 제조사를 연결하는 ROP 는 로봇 내부 코드 생성·스킬 실행을 제조사·로봇 소프트웨어에 맡기고 플릿 작업 API 수준의 요청·상태 확인에 그쳐야 할 것으로 보인다. | ref-677, ref-859, ref-110 | 아니오 | low | 2026-09-29 | 수행 자원 | — |
| f28 | [추정] | 언어 모델 기반 다중 로봇 작업 분해·배정(SMART-LLM, DART-LLM, FLEET), 사전 계획 검증(VerifyLLM), 실패 설명(REFLECT)은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 연구 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 이 영역 양쪽에 연결하고, 승인·근거 표시·환각 관련 내용은 13. 대화형 기능의 신뢰·기반에도 연결해야 한다. | ref-165, ref-861, ref-753 | 아니오 | low | 2026-09-29 | — | — |

### 근거 발췌

- **f1**: 초록: "systematically categorizes their applications across high-level task allocation, mid-level motion planning, low-level action generation, and human intervention." v1 2025-02-06, v5 2026-05-03.
- **f2**: HTML 본문 요약: Hunt 외는 실행 전 승인(pre-execution approval)을 두고, 운영자 한 사람이 여러 로봇을 감독할 수 있는지에 관한 인지 부담은 정량화되지 않았다고 정리(재서술).
- **f3**: 초록: "task decomposition, coalition formation, and task allocation, all guided by programmatic LLM prompts within the few-shot prompting paradigm." 벤치마크는 네 복잡도 범주.
- **f4**: 초록: DAG 로 작업 의존을 모델링해 자연어 지시를 조율된 하위 작업으로 분해; "explicit dependency modeling notably enhances the performance of smaller models"(절제 실험).
- **f5**: 초록: "An LLM front-end produces (i) a task graph with durations and precedence and (ii) a capability-aware robot–task fitness matrix." 이후 형식 최적화가 makespan 최소화.
- **f6**: 세 논문 모두 자연어 지시의 분해와 이기종 로봇 배정을 초록에서 명시(SMART-LLM: 분해·연합·배정, DART-LLM: DAG 분해·배정, FLEET: 작업 그래프·적합도 행렬).
- **f7**: FLEET 절제 실험에서 MILP 는 시간 구조, LLM 은 능력 매칭을 각각 담당; DART-LLM 은 의존 모델링이 작은 모델의 성능을 높임. 이를 원문 주석(업무 지시는 25·26번 기능을 대화로 쓰게 함)과 대조한 추정.
- **f8**: 초록: 자연어 지시→LTL 변환 후 행동 순서열 분석으로 논리 불일치·누락 단계를 실행 전에 식별; 가정 작업 데이터셋으로 평가(재서술).
- **f9**: 초록: "reducing hallucinations through task verification and human supervision"; 시뮬레이션 성공률 +4.76%, 실세계 제로샷 일반화(저자 실험 조건).
- **f10**: 서베이 사람 개입 절(실행 전 승인·사람 검증), HMCF 초록(작업 검증·사람 감독), VerifyLLM 초록(실행 전 검증)이 같은 설계 방향을 독립적으로 보고.
- **f11**: 서베이는 운영자 인지 부담 미정량화를 빈틈으로, VerifyLLM 은 자동 검증으로 실행 전 오류 감소를, HMCF 는 필요할 때만 개입을 보고. 이를 원문 '승인된 계획만 실행'과 결합한 추정.
- **f12**: 초록: "centralized deliberation with decentralized execution"; 사건 기반 재계획은 실패·사용자 의도 변경이 촉발; 실기 9/10, 8/8, 5/5(저자 실험 조건). v1 2025-11-27, v2 2026-06-18.
- **f13**: 초록: "specify high-level activities...using natural language, and to monitor their execution by querying a robot." 실제 정밀 농업 시나리오에서 시험.
- **f14**: 초록: "queries LLM for failure reasoning based on a hierarchical summary of robot past experiences generated from multisensory observations." RoboFail 데이터셋.
- **f15**: REFLECT 는 계층적 경험 요약→실패 설명, Argenziano 외는 로봇 질의로 과거·현재·미래 행동 진행 확인을 각각 초록에서 명시.
- **f16**: REFLECT·Argenziano 외는 기록 요약을 설명 근거로 씀; task_state 스키마는 phases 아래 events 와 estimate_millis·assigned_to 를 둠. 이를 결합한 추정.
- **f17**: 원문(raw JSON) status enum: "uninitialized", "blocked", "error", "failed", "queued", "standby", "underway", "delayed", "skipped", "canceled", "killed", "completed"; estimate_millis 는 완료까지 걸릴 시간 추정 (발행일 미확인, 확인일 기준)
- **f18**: task_new.md 원문: "take additional control over your tasks by sending requests to RMF to cancel a task or skip a phase." task_request.json 원문: category·description 필수, 나머지 선택 (재인용: 2026-09-29-04) (발행일 미확인, 확인일 기준)
- **f19**: 공지 원문: "I'll present an MCP server that exposes the Open-RMF REST API as LLM-callable tools, and an agent that turns plain-English commands into multi-step RMF missions"
- **f20**: OSRA 공지에 승인 언급 없음; Open-RMF 작업 요청은 category·description 만 필수라 언어 모델 출력으로 바로 만들 수 있음. 이를 원문 '승인된 계획만 실행'과 대조한 추정.
- **f21**: 초록: ROS 와 자연어 인터페이스의 간극을 잇고 매개변수 검증·제약 강제로 안전한 운용을 보장; Mars Yard·실험실·시뮬레이션에서 세 로봇으로 시연(재서술).
- **f22**: 초록: 언어 모델 기반 "centralized multi-robot task planning and scheduling"; 공유 선언형 세계 상태, 실행·재계획용 양방향 통신, 컨테이너화된 로봇(재서술).
- **f23**: 초록: "predominantly at prototype and early validation stages (75.0% at TRL 4-6), with deployment-oriented evidence remaining rare (9.1%)."
- **f24**: 본문: "거대언어모델의 추론 능력을 활용하여 로봇이 수행할 명령을 요소 기술로 나누는 작업 계획"; 다중 로봇·사람 확인은 다루지 않음(열람 확인).
- **f25**: 검색 결과 초록 범위: 간호 인력의 자연어 지시→실행 가능한 작업 순서열, 실행 중 추가 요청에 대한 유전 알고리즘 재스케줄링, 실패 복구는 시각-언어 추론·AI 제안 (재인용: 2026-09-29-04)
- **f26**: FLEET(작업 그래프+최적화), VerifyLLM(사전 검증), CoMuRoS(사건 기반 재계획·사람 도움 요청), Open-RMF 작업 요청·상태 스키마를 원문 정의 세 항목(지시·승인·진행 설명)에 대응시킨 추정.
- **f27**: CoMuRoS 는 로봇별 지역 LLM 이 Python 실행 코드를 생성; ROSA 는 ROS 1·2 와 직접 연결. 원문 19장 경계표(로봇 자체 지능·제어는 연계)와 대조한 추정.
- **f28**: 서베이의 네 층 분류(상위 배정~사람 개입)와 Henkel 외의 환각·출력 불안정 과제를 원문 교차 규칙(학습 기반 배정은 25번, 업무 지시는 25·26번)에 대응시킨 추정.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 2025-02-06 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2502.03814 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-059 | Wang, Y., Xiao, R., Kasahara, J. Y. L., Yajima, R., Nagatani, K., Yamashita, A., & Asama, H. | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11-13 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D. | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10-08 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.07417 | 아니오 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07-07 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2507.05118 | 아니오 |
| ref-777 | Gupta, R., Asbery, T., Merchant, Z., Anwar, A., & Thomason, J. | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10-12 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2510.10379 | 아니오 |
| ref-855 | Li, Z., Wu, W., Wang, Y., Xu, Y., Hunt, W., & Stein, S. | HMCF: A Human-in-the-loop Multi-Robot Collaboration Framework Based on Large Language Models | 2025-05-01 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2505.00820 | 아니오 |
| ref-677 | Borate, S., Rai B, B., Pardeshi, V., & Vadali, M. (Frontiers in Robotics and AI 게재 예정) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2511.22354 | 아니오 |
| ref-857 | Argenziano, F., Umili, E., Leotta, F., & Nardi, D. | Defining and Monitoring Complex Robot Activities via LLMs and Symbolic Reasoning | 2025-09-19 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2509.16006 | 아니오 |
| ref-858 | 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)) | 거대언어모델 기반 로봇 인공지능 기술 동향 | 2024-02 | 정부·연구기관 | high | 2026-09-29 | https://ettrends.etri.re.kr/ettrends/206/0905206009/0905206009.html | 아니오 |
| ref-859 | Royce, R., Kaufmann, M., Becktor, J., Moon, S., Carpenter, K., Pak, K., Towler, A., Thakker, R., & Khattak, S. (NASA JPL, IEEE Aerospace 2025) | Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent | 2024-10-09 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2410.06472 | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. (CoRL 2023) | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023-06-27 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2306.15724 | 아니오 |
| ref-861 | Henkel, V., Gehlhoff, F., Kube, D., Almutareb, A., Cruz, L., Hellingrath, B., Koch, P., Legat, C., Mohr, F., Oberle, M., Ocker, F., Schoeler, T., Thron, M., Töpfer, N. A., Vogt, L., & Xia, Y. | Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges | 2026-05-04 | 논문 | medium | 2026-09-29 | https://arxiv.org/abs/2605.02592 | 아니오 |
| ref-862 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-07-02 | 오픈소스 문서 | medium | 2026-09-29 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |
| ref-847 | Autonomous Robots(Springer) 게재 논문 저자(미확인), 국립대만대학병원 협력 | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 2026 | 논문 | medium | 2026-09-29 | https://link.springer.com/article/10.1007/s10514-026-10255-6 | 예 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-29 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |

### 출처 요약

- **ref-165**: 언어 모델을 다중 로봇 시스템에 쓰는 연구를 상위 작업 배정·중간 동작 계획·하위 행동 생성·사람 개입의 네 층으로 정리한 서베이. v5(2026-05-03)의 HTML 본문에서 사람 개입 절과 배정 프레임워크 비교를 확인했다.
- **ref-090**: 상위 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸는 소수 예시 프롬프트 틀. 네 복잡도의 벤치마크·시뮬레이션·실기로 평가.
- **ref-059**: 자연어 지시를 DAG 의존 관계를 가진 하위 작업으로 분해해 다중 로봇이 병렬 실행하게 하는 틀. 모델별 성공률·응답 시간과 의존 모델링 절제 실험을 보고.
- **ref-242**: 언어 모델이 작업 그래프와 로봇–작업 적합도 행렬을 만들고 형식 최적화기가 완료 시간 최소화로 배정하는 2단계 혼합 방식. 사족 로봇 실기 검증.
- **ref-753**: 자연어 지시를 LTL 로 옮긴 뒤 행동 순서열의 논리 일관성과 누락 단계를 실행 전에 찾는 검증 모듈. 가정 작업 데이터셋으로 평가, 코드 공개.
- **ref-777**: 언어 모델 기반 중앙 집중식 다중 로봇 작업 계획·스케줄링 오픈소스 프레임워크. 컨테이너화된 로봇, 공유 선언형 세계 상태, 실행·재계획용 양방향 통신.
- **ref-855**: 로봇별 언어 모델 에이전트가 작업 검증으로 환각을 줄이고 사람은 필요할 때만 개입하는 사람 참여 루프 다중 로봇 협업 틀. 시뮬레이션 성공률 +4.76%, 실세계 제로샷.
- **ref-677**: CoMuRoS: 중앙 작업 관리자 언어 모델이 자연어 목표를 배정하고 로봇별 지역 언어 모델이 실행 코드를 만들며 실패·의도 변경 시 사건 기반으로 재계획하는 구조. 실기 복구·운반 결과와 22개 시나리오 벤치마크.
- **ref-857**: 언어 모델과 자동 계획을 결합해 자연어로 활동을 지정하고 로봇에 질문해 실행 진행을 확인하는 구조. 실제 정밀 농업 시나리오에서 시험.
- **ref-858**: 언어 모델로 로봇 명령 이해·요소 기술 분해 작업 계획·제어 코드 생성을 자동화하는 흐름(SayCan, PaLM-E, Code as Policies 등)을 정리한 ETRI 동향 논문. 다중 로봇·사람 승인은 다루지 않음.
- **ref-859**: ROS 1·2 로봇을 자연어로 점검·진단·조작하는 오픈소스 언어 모델 에이전트. 매개변수 검증·제약 강제 안전 장치, 화성 실험장·실험실·시뮬레이션 시연.
- **ref-453**: 다중 감각 관측의 계층적 경험 요약을 근거로 언어 모델이 실패를 설명하고 교정 계획을 돕게 하는 틀. RoboFail 데이터셋.
- **ref-861**: 산업 자동화의 기반 모델 에이전트 88편 체계적 문헌 고찰. 75.0% 가 TRL 4~6, 배포 근거 9.1%, 환각·출력 불안정·지연이 과제.
- **ref-862**: OSRA 상호운용 SIG 공식 세션 공지. Open-RMF REST API 를 MCP 도구로 노출하고 영어 명령을 다단계 RMF 임무로 바꾸는 에이전트(Nayantra)를 다룬다. 승인·상태 질의 언급 없음.
- **ref-847**: 원문 미열람. 병원 보조 로봇이 간호 인력의 자연어 지시를 작업 순서열로 바꾸고 실행 중 추가 요청에 유전 알고리즘으로 재스케줄링하며 실패를 시각-언어 추론으로 복구하는 시스템(이전 실행 2026-09-29-04 의 ref-242 와 같은 URL, 퍼블리셔가 기존 id 로 합칠 수 있음).
- **ref-110**: Open-RMF 작업 구성(단계·범주·compose)과 robot_task_request·dispatch_task_request, 취소·단계 건너뛰기 설명.
- **ref-125**: Open-RMF 작업 요청 JSON 스키마: category·description 필수, 시작 시각·우선순위·라벨·요청자·플릿 이름 선택.
- **ref-111**: Open-RMF 작업 상태 JSON 스키마: 상태 값, 활성 단계, 추정 시간, 배정 로봇, 단계별 사건, 중단·취소 요청 기록.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f2(사람 개입이 반응적이고 승인 부담 미정량화), f23(산업 배포 근거 9.1%, 환각·출력 불안정), f19·f20(도구 호출 직결 구현에 승인 단계 부재) / 섹션 4: f3(작업 분해·연합 형성·배정), f4(의존 관계 DAG), f5(작업 그래프·로봇–작업 적합도 행렬), f8(사전 실행 계획 검증), f2(감독 제어·실행 전 승인), f14(실패 설명), f17(작업 상태·단계·사건) / 섹션 5: 병원 — f25(간호 인력 자연어 지시→작업 순서열·실행 중 재스케줄링, 원문 미열람 명시), 실외 — f13(정밀 농업에서 질의로 진행 확인), 가정 — f8(가정 작업 데이터셋 검증, 실제 현장이 아닌 데이터셋임을 명시) / 섹션 6: f3·f4·f5·f6·f7(대화 지시→분해·의존·능력 매칭→형식 배정), f8·f9·f10·f11(자동 검증 후 사람 승인), f12(사건 기반 재계획·사람 도움 요청), f13·f14·f15·f16(기록 근거의 진행·실패 설명), f20(승인 관문 위치) / 섹션 7: f17·f18(Open-RMF 작업 요청·상태 스키마), f19(OSRA Interop SIG, MCP 서버), f21(ROSA), f22(RobotFleet), f8(VerifyLLM 코드 공개) / 섹션 8: f1, f2, f3, f4, f5, f8, f9, f12, f13, f14, f23, 국내 f24 / 섹션 9: f26(직접 범위: 대화→작업 그래프, 엔진 결과의 계획 제안, 검증·승인, 관제 작업 요청 변환, 기록 근거 설명), f27(연계 대상: 로봇 내부 코드 생성·스킬 실행·ROS 직접 제어) / 섹션 10: 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링(f7·f28, 원문 주석의 짝), 13. 대화형 기능의 신뢰·기반(f11·f16·f28), 32. 예외 복구·재계획·업무 연속성(f12·f26), 37. 관제 화면·실행 기록(f16·f17), 20. 로봇·제조사 관제 연동(f18·f19·f20), 9. 채팅으로 시나리오 구성(f18 작업 요청에 없는 기한·반복은 시나리오 모델에), 10. 채팅으로 로봇 구성(f5 능력 매칭), 5. 로봇 능력·작업 표현(f5·f9 능력 이해), 24. 작업·워크플로 모델링(f4 DAG), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f28, 교차 규칙), 63. 병원·의료(f25) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 f5·f6·f7 반영, 13. 대화형 기능의 신뢰·기반 페이지에 f2·f10·f11·f23 반영, 37. 관제 화면·실행 기록 페이지에 f17 반영, 32. 예외 복구·재계획·업무 연속성 페이지에 f12 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사전 실행 계획 검증 | Pre-execution Plan Verification | 언어 모델이나 계획기가 만든 로봇 작업 계획을 실행하기 전에 논리 일관성·누락 단계·제약 위반을 자동으로 검사해 잘못된 계획이 로봇 동작으로 이어지지 않게 하는 절차다. |
| 감독 제어 | Supervisory Control | 사람이 개별 동작을 조작하지 않고 시스템이 제안한 계획을 검토·승인하거나 필요할 때만 개입하는 방식으로 여러 로봇의 실행을 감독하는 제어 형태다. |
| 실패 설명 | Failure Explanation | 로봇의 실행 기록·관측을 요약해 무엇이 왜 실패했는지를 자연어로 설명하고, 그 설명을 사람의 문제 파악이나 교정 계획의 입력으로 쓰는 기법이다. |
| 로봇–작업 적합도 행렬 | Robot–Task Fitness Matrix | 로봇마다 각 하위 작업을 얼마나 잘 수행할 수 있는지를 능력 기준으로 점수화한 행렬로, 언어 모델이 추정한 값을 형식 최적화기가 배정 계산에 입력으로 쓴다. |

## 열린 질문

새로 생긴 질문:

- 대화로 제안된 다중 로봇 계획을 사람이 승인할 때 로봇 대수·계획 크기에 따라 검토 부담이 얼마나 커지며, 승인 단위(전체 계획 1회·단계별·변경분만)를 정한 공개 연구나 지침이 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 13. 대화형 기능의 신뢰·기반 | 근거: f2 | 종류: 일반
- 사람이 승인한 계획이 실행 중 실패나 의도 변경으로 재계획될 때 어느 범위의 변경까지 자동 재계획을 허용하고 어디부터 다시 승인받아야 하는지 정한 기준이나 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 20. 로봇·제조사 관제 연동, 13. 대화형 기능의 신뢰·기반 | 근거: f19 | 종류: 일반
- 국내 물류창고·병원·제조 공장에서 대화로 여러 로봇에 업무를 지시하고 승인·실행한 실제 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 ETRI 동향 논문뿐이다)? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 61. 물류창고, 63. 병원·의료, 62. 제조 공장 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 3
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f25 병원 논문 원문 미열람(이전 실행에서 Springer 인증 리다이렉트) — 저자·정량 결과·승인 절차 미확인, 검색 결과 초록 범위만 재인용
    - f12 CoMuRoS 의 채팅 인터페이스 중단·재지시 기능과 작업 상태 값(COMPLETED·IN PROGRESS·INTERRUPTED)은 검색 결과 요약에서만 보여 claim 에 넣지 않음
    - f2 서베이가 인용한 Hunt 외·VADER·Li 외 원 논문은 직접 열지 않아 서베이 본문 요약에만 기댐
    - f4 DART-LLM 의 로봇 종류·성공률 수치는 초록에 없어 미확인
    - f9 HMCF 의 사람 개입 횟수 등 정량값은 초록에 없어 미확인
    - f6·f10·f15 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)
    - f17·f18 Open-RMF 문서·스키마 발행일 미확인
    - MDPI Applied Sciences 'LLM-Enhanced Control of a Mobile Robotic Platform for Smart Industry'(제조 공장 사례 후보)는 403 으로 열지 못해 넣지 않음
    - Eluna(arXiv 2607.08960, 창고 SOP 에이전트)는 로봇 지시가 아닌 업무 시스템 자동화라 적용 사례로 넣지 않음
    - 국내 산업 사례: 한국어 검색 3회에서 LG CNS 물류 로봇 관제 플랫폼·한림대성심병원 통합 관제 기사는 찾았으나 대화형 업무 지시가 아니어서 출처로 넣지 않음
    - hellot SCM FAIR 2026 기사의 자연어 프롬프트는 영상 분석 조건 설정이라 이 영역과 무관해 제외
- 범위 경계 위반 의심:
    - f27: 로봇별 지역 언어 모델의 실행 코드 생성(CoMuRoS)과 ROS 직접 제어 에이전트(ROSA)는 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함
    - f7·f26: 배정·일정 계산 자체는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 범위이므로 이 영역에서는 대화→작업 그래프 변환과 계획 제안·승인의 근거로만 제안함
    - f12·f26: 실행 중 재계획·복구는 32. 예외 복구·재계획·업무 연속성의 범위이므로 이 영역에서는 승인된 계획과의 차이 표시·재승인 근거로만 제안함
    - f8: VerifyLLM 의 가정 작업 데이터셋은 실제 가정 현장이 아니므로 site_type 가정 은 데이터셋 기준임을 서술에 밝혀야 함
    - f23: 산업 자동화 일반(비로봇 포함) 문헌 고찰은 성숙도·과제 근거로만 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-165~ref-847, 예약 구간 안) 상한 도달로 'Prompting Robot Teams with Natural Language'(arXiv 2509.24575), COHERENT, Hierarchical LLM multi-agent prompt optimization(arXiv 2602.21670), 'Large language model-based task planning for service robots: A review'(arXiv 2510.23357)는 확인했으나 넣지 못했다. 원문 열람 17건(webfetch 14, github_raw 3: task_new.md·task_request.json·task_state.json), 미열람 1건(ref-847, 이전 실행의 검색 결과 초록 재인용). ref-847 은 이전 실행 2026-09-29-04 가 ref-242 로 낸 병원 논문과 같은 URL 이나 참고문헌 목록 입력에 없어 새 id 로 냈으며 퍼블리셔가 기존 id 로 합칠 수 있다(이번 실행의 ref-242 는 FLEET 논문이다). 교차 확인 3건(f6: SMART-LLM·DART-LLM·FLEET, f10: Li 외 서베이·HMCF·VerifyLLM, f15: REFLECT·Argenziano 외 — 모두 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv 초록·HTML 본문 확인, high 신뢰도 출처는 ETRI 동향 1건이며 단일 출처). 분류 원문 핵심 질문(대화 지시→확인 가능한 계획→승인→실행·진행 설명)에는 f3·f4·f5·f6(분해·배정 가능), f8·f9·f10(실행 전 검증·승인 설계 존재), f13·f14·f15·f17(기록 근거 진행·실패 설명과 관제 상태 기록), f19·f20(도구 호출 직결 구현의 승인 부재)로 답했으며 결론은 '세 단계 각각의 연구·오픈소스는 있으나 셋을 하나의 승인 관문이 있는 흐름으로 이은 운영 사례는 확인되지 않았고 산업 배포 근거는 드물다'는 추정(f7·f11·f16·f20·f26)이다. 현장 유형: 병원(f25, 원문 미열람 명시), 실외(f13, 정밀 농업), 가정(f8, 데이터셋 기준)만 확인했고 물류창고·제조 공장·상업 시설 사례는 없다. L. AI·학습 기술 관련 finding(f1~f6·f8·f9·f12·f14·f28)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링·13. 대화형 기능의 신뢰·기반 양쪽에 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 848건과의 URL 중복을 대조하지 못했으므로 서베이·SMART-LLM·ROSA 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 작업 분해·연합 형성·사람 참여 루프·LLM 에이전트·모델 컨텍스트 프로토콜·과도한 에이전시·구조화 출력·팬아웃·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
