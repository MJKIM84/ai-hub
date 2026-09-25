# 스토리텔러 산출 2026-09-25-74

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | draft | q3-03 답함(3절 소제목 신설 #q3-03), 새 질문 q3-14·q4-11·q5-08, 4·6·7·8·9절과 상태 줄 갱신(답한 질문 3건·열린 질문 10건), 단계 전환 아니오 |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '온톨로지 질의 결과에 따른 되묻기' 소절 신설(q3-03), 다른 아이디어와의 연결은 구조 언급 수준으로 명시, 절 머리 문장 갱신 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 6절에 개념 '배정 실패' 제안(검증 미반영)을 미해결 모델링 질문으로 추가, 초안 버전 v0.7 유지 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 상태 줄의 현재 단계를 '단계 3. 구현 가설 설계'로 갱신, 6절 산출물 링크에 실행 2026-09-25-74(q3-03, 초안 변경 없음) 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 3 | q3-03 답함(후보 없음·후보 여럿일 때 되묻기 범위, 신뢰도 low), 새 질문 3건, 초안 v0.7 유지 | run 2026-09-25-74
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 3: q3-03(온톨로지 질의가 후보를 찾지 못하거나 여럿 낼 때 챗봇이 되묻는 것과 스스로 정하는 것) 답함, 신뢰도 low
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 3: 배정 실패(무입찰) 기록과 후보 여럿일 때 평가기·되묻기 경계를 정리하고 13. 작업 배정 — MRTA 에 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 3(q3-03)에서 Open-RMF 무입찰 배정 실패 기록, 평가기 기본값 병기, 후보 여럿일 때 되묻기 경계를 6. 대표 접근법과 기술에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 대조적 설명 | Contrastive Explanation | 시스템이 왜 다른 선택(예: 다른 로봇·다른 일정)이 아니라 이 선택을 했는지를 대안과 비교해 설명하는 방식으로, 사용자가 명세 오류를 찾는 데 쓰인다. | 13, 18, 27 | ref-720 |
| new | 기약 불능 제약 집합 | Irreducible Infeasible Subset (IIS) | 최적화 모델을 실행 불가능하게 만드는 제약 가운데, 어느 하나라도 빼면 실행 가능해지는 최소 제약 묶음으로, 불능 원인을 사람에게 보여 주는 데 쓰인다. | 13, 14, 27 | ref-719 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-713 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp |
| ref-714 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp |
| ref-039 | Open Robotics | Currently supported Tasks (task_types) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task_types.html |
| ref-716 | Rasa Technologies (RasaHQ/rasa GitHub) | Fallback and Human Handoff — Rasa documentation (docs/docs/fallback-handoff.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/fallback-handoff.mdx |
| ref-717 | Göbelbecker, M., Keller, T., Eyerich, P., Brenner, M., & Nebel, B. | Coming Up With Good Excuses: What to do When no Plan Can be Found | 논문 | medium | https://ojs.aaai.org/index.php/ICAPS/article/view/13421 |
| ref-718 | Sreedharan, S., Srivastava, S., Smith, D., & Kambhampati, S. | Why Couldn't You do that? Explaining Unsolvability of Classical Planning Problems in the Presence of Plan Advice | 논문 | medium | https://arxiv.org/abs/1903.08218 |
| ref-719 | Chen, H. 외(OptiChat 저자) | Diagnosing Infeasible Optimization Problems Using Large Language Models | 논문 | medium | https://arxiv.org/abs/2308.12923 |
| ref-720 | Schneider, E. 외(CE-MRS 저자) | CE-MRS: Contrastive Explanations for Multi-Robot Systems | 논문 | medium | https://arxiv.org/abs/2410.08408 |
| ref-721 | Liang, K. 외(Introspective Planning 저자) | Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity | 논문 | medium | https://arxiv.org/abs/2402.06529 |
| ref-722 | Suri, M. 외(University of Maryland·Adobe Research) | Structured Uncertainty guided Clarification for LLM Agents | 논문 | medium | https://arxiv.org/abs/2511.08798 |
| ref-723 | Shida, Y. 외 | Reinforcement Learning of Multi-robot Task Allocation for Multi-object Transportation with Infeasible Tasks | 논문 | medium | https://arxiv.org/abs/2404.11817 |
| ref-724 | Kazmi, M. (plan-failure-bench GitHub) | plan-failure-bench — README (Benchmark measuring how LLM planners fail at robot tasks) | 오픈소스 문서 | low | https://github.com/munawarkazmi/plan-failure-bench |
| ref-459 | W3C | Shapes Constraint Language (SHACL) | 표준 | medium | https://www.w3.org/TR/shacl/ |
| ref-041 | Scientific Reports 게재 논문(저자 미확인) | Ontology-driven integration of advertised and operational capabilities in robots | 논문 | medium | https://www.nature.com/articles/s41598-025-16649-3 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 오픈소스 문서 | medium | https://robot-help.github.io/ |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-352 | Park, J. 외(고려대학교·연세대학교·Google Research, CLARA 프로젝트) | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents — project page (clararobot.github.io) | 오픈소스 문서 | medium | https://clararobot.github.io/ |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 논문 | medium | https://arxiv.org/abs/2306.10376 |
| ref-598 | Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026) | LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation | 논문 | medium | https://arxiv.org/abs/2512.14138 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 관제가 배정 실패(수행 가능한 로봇·플릿 없음)를 WMS 등 상위 업무 시스템에 어떤 필드로 되돌리고, 상위 시스템이 이를 사람 작업 지시로 전환하는 표준이나 국내 물류센터 사례가 있는가? | 13, 1 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | 단계 3. 구현 가설 설계 — q3-03 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | 단계 3. 구현 가설 설계 — q3-03 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | 단계 3. 구현 가설 설계 — q3-03 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | 단계 3. 구현 가설 설계 — q3-03 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | 단계 3. 구현 가설 설계 — q3-03 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) | 오픈소스 | Open Robotics (open-rmf) | 13, 9 | ref-713 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp |
| Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) | 오픈소스 | Rasa Technologies | 18, 27 | ref-716 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/fallback-handoff.mdx |

## 추가 조사 요청

- 단계 3 페이지 3절 q3-03: Open-RMF 평가기 LeastFleetCostEvaluator·LeastFleetDiffCostEvaluator·QuickestFinishEvaluator 의 순위 기준(구현 코드)과 디스패처 코드·헤더 문서의 기본 평가기 표현 차이를 확인할 자료가 필요하다 — 두 출처의 기본값 표현이 달라 병기만 했다.
- 단계 3 페이지 3절 q3-03·q3-14: Electronics(2026) ReasonerOutput 이 불가 사유를 필드로 담는지 원문 확인이 필요하다 — 후보 없음의 원인 설명 형식 판단에 필요하다.
- 단계 3 페이지 3절 q3-03: SHACL 2017-07 권고안 원문으로 검증 보고 구조(sh:conforms, sh:result 속성)를 재확인할 필요가 있다 — 이번에는 편집자 초안만 열람했다.
- 단계 3 완료 조건: 다른 아이디어와의 연결(아이디어 1 의 선언·운용 능력, 아이디어 3 의 공간 그래프 장소 슬롯)을 뒷받침할 근거 finding 이 필요하다 — 이번 반영은 구조 언급 수준이다.
- 단계 3 완료 조건: 실험 페이지에 실을 사용자 실험 계획(예: 후보 없음·후보 여럿 되묻기 규칙의 물류 지시 시나리오 시험)은 다음 트랙 실행에서 제안이 필요하다 — 이번 1차 판정은 실험 계획 없음을 미충족으로 두었다.
- 물류 창고 관제에서 배정 실패를 사용자와 대화로 처리한 연구·국내 사례(한국어 자료 포함)가 필요하다 — q3-03 결론의 근거가 물류 조건이 아니다.
- 백로그 정리: q3-12·q3-13, q4-09·q4-10, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06 이 중복 등록되어 있어 담당자의 정리(폐기 처리)가 필요하다.
- 트랙 개요·단계 페이지의 머리 상태 줄은 patches 로 갱신할 수 없어 이번에 두 페이지를 전체 content 로 냈다 — 머리 상태 줄 갱신 방식(patches 대상 확장)을 pipeline 담당에게 요청한다.

## 이행한 수정 지시

- f4 기본 평가기 표현 — 단계 3 페이지 q3-03 '후보가 여럿일 때' 소절과 아이디어 페이지 5절에서 '디스패처는 경매자를 만들 때 QuickestFinishEvaluator 를 지정하며(Dispatcher.cpp), Auctioneer.hpp 문서 주석은 미지정 시 기본을 LeastFleetDiffCostEvaluator 로 적는다'로 두 출처를 병기하고, 사용자 정의 평가기 추상 인터페이스와 세 평가기 순위 기준 미확인을 남겼으며, 종합 문장도 '디스패처 코드가 지정한 평가기'로 맞췄다.
- f18 강등 — Rasa 문장을 [추정]으로 바꾸고 '문턱(설정 예 0.7), 두 단계 폴백의 의도 확인·재진술, 최종 폴백의 기본은 기본 응답 발화와 대화 상태 초기화이고 사람 인계는 사용자 정의 동작으로 구성하는 예'로 고쳤으며, f22 종합과 f25 시나리오의 사람 인계 서술을 '선택 구성'으로 맞췄다.
- f12 연구 조건 — CE-MRS 를 '22명 참가 대면 사용자 연구(수색·구조 영역, IEEE RA-L 9권 2024)'로 바꾸고 명세 오류 식별·해결 향상을 저자 보고로 병기했으며, 참고문헌 요약도 같게 고쳤다.
- f17 게재처 — 'ACL 2026 Findings' 를 지우고 'arXiv 2511.08798, 게재처 미확인', 저자 표기 'Suri, M. 외(University of Maryland·Adobe Research)'로 본문·각주·참고문헌 항목을 고쳤다.
- f19 — 본문에 '개인 연구자가 공개한 동료심사 전 벤치마크(Zenodo 프리프린트)'임을 밝히고 종합(f22·f23) 문장의 각주에서 ref-724 를 뺐으며 '종합의 근거로 쓰지 않는다'를 적고 평가 모델명·수치는 쓰지 않았다.
- f6 — VDA 5050 문장을 세 오류 유형(INVALID_ORDER_ACTION WARNING, UNSUPPORTED_PARAMETER CRITICAL, MOBILE_ROBOT_NOT_AVAILABLE WARNING)을 서로 다른 오류 유형으로 정의한다는 명세 기준 서술로 고치고, 주문 거절은 로봇 쪽 기능(연계 대상)이며 ROP 는 오류를 받아 원인을 구분·설명하는 쪽임을 단계 페이지와 아이디어 페이지에 밝혔다.
- f13 — Shida 외 문장에 IEEE/SICE SII 2025 게재를 병기하고, 운반 불가 판정·학습은 로봇 쪽 운반 능력과 맞닿은 연계 대상이며 배정에서 실행 불가 작업을 일시 배제하는 규칙 사례로만 다룬다고 적었다.
- ref-459 각주 — 단계 페이지 각주 제목 뒤에 '발행일은 권고안 기준이며 열람본은 W3C data-shapes 저장소 편집자 초안으로 권고안 문구와의 일치는 미확인'을 병기하고 본문에도 같은 사실을 적었다.
- 원문 미열람 표시 — ref-236·350·351·352·353·598·717·718·719·720·721·722·723·726 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- 온톨로지 변경 거부 — 개념 '배정 실패'를 초안 2절에 넣지 않고 업무 분해·배정 설계 초안 6절에 근거 f1·f3·f6·f22, dispatch 값 failed_to_assign·errors 및 배정 개념과의 경계, 사유 유형 값이 추정 근거라는 점을 적은 질문으로 추가했으며 초안 버전은 v0.7 로 두고 6절만 갱신했다.
- 아이디어 2 5절 — '온톨로지 질의 결과에 따른 되묻기' 소절에서 아이디어 1(선언·운용 능력)·아이디어 3(장소 슬롯) 연결을 구조 언급 수준이라고 밝히고 완료 조건이 아직 충족되지 않았다고 적었다.
- 세부영역 페이지 비수정 — 13·18·27·5 세부영역 페이지는 pages 에 넣지 않고 area_reflection_proposals 로만 냈으며, 27. AI·학습·적응과 모델 운영 8절 제안에 Plan-Failure-Bench 를 신뢰도 low 참고 사례로 표시했다.
- 단계 3 페이지 — q3-03 을 답함(답한 실행 2026-09-25-74, 답 위치 #q3-03)으로 바꾸고 3절 소제목 '### q3-03 … {#q3-03}'을 두었으며, 6절을 '다음 단계로 전환: 아니오(아이디어 2 5절 다른 아이디어와의 연결 미완, 실험 계획 없음, 열린 질문 q3-04~q3-13)'로 쓰고 상태 줄을 2절 표와 같은 열린 질문 10건·답한 질문 3건으로 맞췄다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.7
- 트랙 로그 항목: 답한 질문: q3-03(후보 없음은 원인 설명과 사용자가 바꿀 수 있는 항목만 되묻기, 후보 여럿은 계산 가능한 목적 기준이면 평가기로 자동 결정; 근거 f1~f18·f20~f26, 종합 f22·f23 은 추정, f19 는 신뢰도 low 참고 사례, 페이지 신뢰도 low) / 새 질문: q3-14(f8), q4-11(f22), q5-08(f23); 일반 열린 질문 1건(배정 실패의 상위 업무 시스템 반환, 영역 13. 작업 배정 — MRTA·1. 주문·업무 시스템 연계) / 온톨로지 변경: 없음(v0.7 유지; 개념 '배정 실패'(f1·f3·f6·f22)는 진행 상태·배정 개념과 경계 중복, 사유 유형 추정으로 검증 거부 → 초안 6절 질문) / 완료 조건 평가: 미충족(부족: 아이디어 2 5절의 다른 아이디어와의 연결(구조 언급 수준), 실험 페이지의 실험 계획; 열린 질문 q3-04~q3-13) / 세부영역 반영 제안: 13. 작업 배정 — MRTA(6절), 18. 사람–로봇 협업·운영 인터페이스(6절), 27. AI·학습·적응과 모델 운영(6절·8절), 5. 로봇 능력·작업 온톨로지(10절) 5건 / 다음 실행 제안: q3-04, q3-12(q3-13 중복 정리), 단계 3 실험 계획 제안과 다른 아이디어 연결 근거 조사
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 10(단계 페이지 표 기준, 백로그에는 중복 q3-13 포함 11), 답함 3, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-03 | 답함 | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md#q3-03 | — | — | — |
| q4-11 | 열림 | — | 배정 실패 원인(능력 부재·일시적 가용 불가·제약 조합 불능·해석 오류)마다 챗봇이 사용자에게 제시할 완화 선택지(기한 완화, 장소·대상 변경, 사람 작업자 처리 전환, 대기)를 어떤 목록으로 두고, 사람 처리 전환이나 기한 완화는 누가 승인하는가? (q3-03 에서 파생) | 4 | f22 |
| q3-14 | 열림 | — | 온톨로지 기반 실행 가능성 판정이 후보를 하나도 내지 않을 때, 어느 능력·제약 때문인지를 SHACL 검증 보고처럼 제약 단위로 돌려주는 형식을 배정기 독립 출력(ReasonerOutput)에 둘 수 있는가, 그 형식에서 챗봇이 사용자에게 보여 줄 설명을 만들 수 있는가? (q3-03 에서 파생) | 3 | f8 |
| q5-08 | 열림 | — | 후보가 여럿일 때 '시스템이 계산할 수 있는 차이는 자동 결정, 사용자만 아는 정보에 걸린 차이만 되묻기' 규칙을 물류 지시 시나리오에 적용하면 되묻기 횟수와 오배정은 모든 경우를 묻거나 묻지 않는 방식에 비해 어떻게 달라지는가? (q3-03 에서 파생) | 5 | f23 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | Open-RMF 디스패처는 무입찰 시 FailedToAssign·오류(코드 10)를 기록하고 작업을 수행하지 않는다(f1). 여러 입찰은 평가기로 고르며 기본값은 디스패처 코드(QuickestFinishEvaluator 지정)와 Auctioneer.hpp 문서(미지정 시 LeastFleetDiffCostEvaluator)를 병기, 순위 기준 미확인(f4). 작업 요청 fleet_name 으로 허용 플릿 지정(f5). 실행 불가 작업의 일시 배제 학습(f13, 운반 능력은 연계 대상). 후보 여럿일 때 계산 가능한 목적 기준은 평가기로 자동 결정하고 사용자만 아는 정보에 걸릴 때만 되묻는 경계와 분류 원문 질문과의 연결(f23·f24, 추정). 27. AI·학습·적응과 모델 운영과 양쪽 연결. |
| 18 | 6. 대표 접근법과 기술 | 배정 실패 시 원인 설명과 사용자가 바꿀 수 있는 항목만 되묻는 범위(f22, 추정). Rasa 폴백(문턱 설정 예 0.7, 두 단계 폴백, 최종 폴백 기본은 기본 응답·대화 초기화이고 사람 인계는 선택 구성, f18 추정). 불필요한 되묻기를 줄이는 내성적 계획(f16)과 EVPI 기반 질문 선택(f17, 게재처 미확인, 저자 보고). CE-MRS 대조적 설명의 22명 참가 대면 사용자 연구(수색·구조 영역, f12). |
| 27 | 6. 대표 접근법과 기술 | LLM 과 해법기를 함수 호출로 결합해 IIS 로 불능 원인을 찾고 설명·수정 제안을 내는 OptiChat(f11), 내성적 계획과 등각 예측 결합(f16), 명세·모델 불확실성을 나눈 EVPI 기반 되묻기(f17). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결. |
| 27 | 8. 대표 연구와 자료 | 해결 불가 설명 연구: Göbelbecker 외 excuse(ICAPS 2010, f9), Sreedharan 외 plan advice 해결 불가 설명(f10), CE-MRS(IEEE RA-L 9권 2024, f12). 계획 실패 유형 벤치마크 Plan-Failure-Bench(f19)는 개인 연구자의 동료심사 전 자료로 신뢰도 low 참고 사례로만 표시. |
| 5 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 온톨로지 기반 실행 가능성 판정(ReasonerOutput, f7)이 후보 없음의 원인을 SHACL 검증 보고 같은 제약 단위 형식(f8, 편집자 초안 기준)으로 13. 작업 배정 — MRTA 에 돌려주는 연결과, 제조사 광고 능력과 측정 운용 능력을 함께 표현하는 RCO(f21, oq-024 관련). |
