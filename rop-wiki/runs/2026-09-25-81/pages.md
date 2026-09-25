# 스토리텔러 산출 2026-09-25-81

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | draft | q4-02 답함(검증 방법별 포착·놓침 오류, 모의 실행의 8·22 구분, 피킹 시나리오), 후속 질문 3건(q4-15·q4-16·q5-16), 완료 조건 미충족 유지(열린 질문 q4-03~q4-16), 관련 세부영역 22·23·8 추가, 8. 출처에 새 각주 정의(ref-782 발행일 2026-04), 이력 행 추가 |
| update | docs/ideas/nl-task-chatbot.md | draft | 게시본(v15)의 5절 끝에 '검증 방법별로 잡는 오류' 소절 추가(q4-02, 실행 2026-09-25-81), 6절·auto 영역은 게시본 유지, 프런트매터 sources 에 새 인용 id 추가, version 16 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 6절 '검증 기록' 질문에 q4-02 답 연결과 재제안 미반영 사유 추가(초안 v0.8 유지), 프런트매터 sources 에 새 인용 id 추가 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 게시본(v14) 6절을 유지한 채 실행 2026-09-25-81(q4-02 답, 초안 변경 없음)만 덧붙임, version 15 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 4 | q4-02 답함: 실행 전 검증 방법(스키마·온톨로지 제약·계획 검증·모의 실행·사람 확인)별 포착·놓침 오류 정리(신뢰도 low), 후속 질문 3건, 초안 v0.8 유지 | run 2026-09-25-81
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4: q4-02 답함, 실행 전 검증 방법별로 잡는 오류와 놓치는 오류 정리(신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 자연어 업무 지시 챗봇 트랙 단계 4 에서 배정 결과의 실행 전 검증(제약 대조·모의 실행) 근거 정리, 세부영역 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 q4-02 답(배정 결과의 실행 전 검증 방법), 6. 대표 접근법과 기술 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 제약 디코딩 | Constrained Decoding | 언어 모델이 토큰을 생성할 때 스키마·문법·오토마톤에 맞지 않는 토큰을 가려, 출력이 정해진 형식이나 명세를 벗어나지 않게 하는 생성 방식이다. | 27, 23 | ref-774, ref-786 |
| new | JSON 스키마 | JSON Schema | JSON 데이터의 자료형·허용 값·필수 속성·수치 범위 같은 구조 제약을 기술하고 인스턴스가 이를 따르는지 검증하는 명세다. | 27, 12 | ref-773 |
| new | 잠재 실패 | Latent Failure | 계획 실행을 즉시 멈추지는 않지만 목표 달성을 조용히 해치고 때로 되돌릴 수 없는 결과로 이어지는 계획 오류다. | 23, 22, 27 | ref-781 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-773 | JSON Schema (json-schema-org/json-schema-spec GitHub) | json-schema-spec — specs/jsonschema-validation.md (JSON Schema Validation: A Vocabulary for Structural Validation of JSON) | 표준 | medium | https://github.com/json-schema-org/json-schema-spec/blob/main/specs/jsonschema-validation.md |
| ref-774 | guidance-ai (JSONSchemaBench GitHub) | jsonschemabench — README (JSONSchemaBench) | 오픈소스 문서 | medium | https://github.com/guidance-ai/jsonschemabench |
| ref-775 | Geng, S. 외(JSONSchemaBench 저자, arXiv 2501.10868) | JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | 논문 | medium | https://arxiv.org/abs/2501.10868 |
| ref-776 | KCL-Planning (VAL GitHub) | VAL — The plan validation system (README) | 오픈소스 문서 | medium | https://github.com/KCL-Planning/VAL |
| ref-777 | Guan, L., Valmeekam, K., Sreedharan, S., & Kambhampati, S. | Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning | 논문 | medium | https://arxiv.org/abs/2305.14909 |
| ref-778 | VerifyLLM 저자(arXiv 2507.05118) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 논문 | medium | https://arxiv.org/abs/2507.05118 |
| ref-779 | Hariharan, A., Dongre, V., Hakkani-Tür, D., & Tur, G. | Plan Verification for LLM-Based Embodied Task Completion Agents | 논문 | medium | https://arxiv.org/abs/2509.02761 |
| ref-780 | Raman, S. S., Cohen, V., Idrees, I., Rosen, E., Mooney, R., Tellex, S., & Paulius, D. | CAPE: Corrective Actions from Precondition Errors using Large Language Models | 논문 | medium | https://arxiv.org/abs/2211.09935 |
| ref-781 | Lu, X., Zhang, R. H., & Zhang, R.(Pennsylvania State University) | SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model | 논문 | medium | https://arxiv.org/abs/2606.14574 |
| ref-782 | Lee, Y.-H., Nam, T., Cho, D.-S., & Kim, W.-T. | LLM-Based Adaptive Control Code Generation Framework with Digital Twin-Integrated Verification for Heterogeneous Robot Systems | 논문 | medium | https://doi.org/10.3390/app16083883 |
| ref-783 | Deng, M., Fu, B., Li, L., & Wang, X. | Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction | 논문 | medium | https://arxiv.org/abs/2506.18178 |
| ref-784 | Ko, T.-H., & Lin, C.-T.(National Central University) | Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin | 논문 | medium | https://arxiv.org/abs/2609.29061 |
| ref-785 | Köcher, A., da Silva, L. M. V., & Fay, A.(Helmut Schmidt University) | Constraint Checking of Skills using SHACL | 논문 | medium | https://ieeexplore.ieee.org/abstract/document/9557549/ |
| ref-786 | SELP 저자(arXiv 2409.19471) | SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models | 논문 | medium | https://arxiv.org/abs/2409.19471 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-362 | OpenAI | Introducing Structured Outputs in the API | 벤더 문서 | low | https://openai.com/index/introducing-structured-outputs-in-the-api/ |
| ref-416 | Rana, K. 외 | SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | 논문 | medium | https://arxiv.org/abs/2307.06135 |
| ref-459 | W3C RDF Data Shapes Working Group | Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) | 표준 | medium | https://www.w3.org/TR/shacl/ |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-702 | SafePlan 저자(arXiv 2503.06892, 저자 미확인) | SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning | 논문 | medium | https://arxiv.org/abs/2503.06892 |
| ref-697 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 오픈소스 문서 | medium | https://docs.langchain.com/oss/python/langchain/human-in-the-loop |
| ref-713 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 논문 | medium | https://dl.acm.org/doi/10.1145/3706598.3713218 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터 로봇 관제에서 작업 지시나 배정 결과를 배치 전에 시뮬레이션(디지털 트윈)으로 모의 실행해 확인하는 운영 사례나 연구가 있는가? | 22, 13 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | 단계 4. 오해석 방지와 확인 절차 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) | 표준 | JSON Schema (json-schema-org) | 27, 12 | ref-773 | https://github.com/json-schema-org/json-schema-spec/blob/main/specs/jsonschema-validation.md |
| VAL (PDDL 계획 검증 도구) | 오픈소스 | KCL-Planning | 23, 27 | ref-776 | https://github.com/KCL-Planning/VAL |
| JSONSchemaBench | 오픈소스 | guidance-ai | 27, 23 | ref-774 | https://github.com/guidance-ai/jsonschemabench |

## 추가 조사 요청

- 단계 4 페이지 H1 아래 상태 줄('열린 질문: 13건 · 답한 질문: 1건')은 H2 절 밖이라 patches 로 바꿀 수 없다. 이번 실행 뒤 값은 열린 질문 14건·답한 질문 2건이므로 퍼블리셔(또는 pipeline 담당)가 상태 줄을 갱신하도록 요청한다.
- 패치 적용 기준판 확인 요청: 이전 초안에서 트랙 개요·아이디어 페이지 패치가 실행 2026-09-25-98·99 반영 전 판(개요 v13, 아이디어 v13)에 적용되었다. 이번 패치는 게시본(개요 v14, 아이디어 v15)에 적용되어야 하며 프런트매터 version 을 각각 15·16 으로 명시했다.
- 트랙 개요 상태 줄(현재 단계: 단계 3)과 자동 진행 표(단계 1)의 현재 단계 표기가 서로 달라 config/tracks/nl-task-chatbot.yaml 의 current_stage 확인이 필요하다(1차 검증 노트). 개요 상태 줄은 값이 바뀌지 않아 이번 실행에서 고치지 않았다.
- q4-02 3절 '모의 실행': SIMMER 가 평가한 모델 수와 '오류 없는 계획' 비율의 정확한 값을 원문으로 확인해야 한다(검증에서 '최대 17%'·'여섯 LLM' 미확인).
- q4-02 3절 '계획 검증기': VAL 이 검증 실패 때 내는 보고 형식(위반 위치·수리 조언)을 원문으로 확인하면 초안 6절 '검증 기록'의 위반 위치·사유 속성 근거가 된다.
- q4-02 3절 '스키마 검증': 게시된 JSON Schema 2020-12 판과 main 브랜치 초안의 검증 키워드 문구 차이를 확인해야 한다.
- 백로그 중복 정리 필요: q4-09·q4-10, q3-12·q3-13, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06.

## 이행한 수정 지시

- f15 강등 — 단계 4 페이지 q4-02 '모의 실행'의 SIMMER 문장을 [추정]으로 쓰고 수치를 '오류 없는 계획 20% 미만, 잠재 실패 포함 계획 29~56%, 최대 72% 감소, 동작 77개·객체 262개'로 고쳤으며 '최대 17%'·'여섯 LLM'은 쓰지 않고 모델 수는 미확인으로, '동료심사 전 프리프린트의 저자 보고'를 병기했다(아이디어 페이지도 [추정]).
- f17 — Ko·Lin 문장의 '올바른 거부 7/8, 자율 전략 성공 3/10' 뒤에 '(저자 보고값, 검증 미재확인, 가상 분류 라인 30개 고정 시험 기록)'을 붙였다.
- f13 — SayPlan 문장을 '저자들은 거의 완전한 실행 가능성(near-perfect executability)을 보고했다(사무실·가정 3D 장면 그래프 조건)'로 저자 보고임을 밝혀 썼다.
- f16 — 발행일을 2026-04 로 적고(본문·reference_updates published), 실행 전 동역학 검증·동작 스케일링은 분류 원문 9장 로봇 자체 지능·제어 경계의 연계 대상이며 ROP 쪽은 로봇 선택·공간 접지 수준의 검증으로 본다는 [추정] 문장을 더했다.
- f4 — 로봇의 주문 거절은 연계 대상이고 ROP 는 오류 유형을 받아 확인 절차의 마지막 결과로 처리하는 쪽만 맡는다고 [추정]으로 서술하고, 오류 수준을 원문 Table 9 대로 'UNSUPPORTED_PARAMETER 만 CRITICAL, 나머지 WARNING'으로 적었다.
- f21·f24 — 방법별 표의 '로봇 관제 쪽 거절' 행에 '연계 대상(로봇 쪽 기능)'을 표시하고 표 아래에 '출처별 보고를 이 위키가 대응시킨 종합이며 같은 조건에서 비교한 출처는 없다'를 적었으며(아이디어 페이지 표도 같음), f24 시나리오는 '설명용 가정 사례, 현장 수치 없음'으로 밝혔다.
- f3 — 여섯 프레임워크 목록이 원문 미열람 논문(ref-775) 요약 기준이고 README(ref-774)와 논문은 같은 저자 그룹이라 독립 교차가 아님을 본문과 4절 불확실성에 적었다.
- f12·f14·f9·f11·f19 — 각 수치·결과 뒤에 '(저자 보고, 원문 미열람)'과 평가 조건(드론 항법·로봇 조작 / VirtualHome·Spot / 48개 과제 / 가정 환경 / TEACh)을 유지했다.
- f20 — 새로 서술하지 않고 '사람 확인과 LLM 판정자' 소절에서 [q4-01 답](#q4-01)의 사람 승인 한계 서술로 연결하는 한 문장과 기존 각주 ref-713·ref-697 만 두었다.
- 온톨로지 변경 '검증 기록' 미반영 — 초안 2절은 고치지 않고 6절에 q4-02 답(f21·f22) 연결과 미반영 사유(추정·원문 미열람 근거, '사용자 확인' 경계 미결정, 로봇 관제 거절의 연계 대상 경계)를 질문으로 덧붙였으며 초안 v0.8 과 ontology_draft_version '0.8'을 유지했다.
- reference_updates — 원문 미열람 출처(ref-775, ref-777~ref-786, ref-362, ref-416, ref-459, ref-236, ref-702, ref-697, ref-713)에 source_unopened: true 를 두었고, ref-773·ref-774·ref-776 은 github_raw 로 연 원문이라 false 로 두었으며 각주 정의 줄의 접근일 뒤에 ' (원문 미열람)'을 붙였다.
- ref-031 — 단계 4 페이지의 기존 각주 정의 줄을 그대로 재사용하고 새로 정의하지 않았으며 reference_updates 에서 입력 원문 텍스트 열람으로 표시했다.
- 6절·2절 — 완료 조건 세 행을 모두 '미충족 · 미승인'으로 두고 '다음 단계로 전환: 아니오(…)'로 적었으며, 2절 q4-02 를 '답함', 답 위치 [q4-02 답](#q4-02), 3절 소제목을 '### q4-02 … {#q4-02}' 형식으로 두었다.
- 세부영역 반영 제안 — 13·23·22·27 세부영역 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그로만 남겼으며, 22. 시뮬레이션·예측용 디지털 트윈 제안에 초기 상태는 8. 실시간 세계 상태·데이터 일관성에서 받는다는 f23 구분을 함께 적었다.
- 2차: 트랙 개요 6절 — 게시본(v14) 6절을 기준으로 다시 써 실행 2026-09-25-98·99 서술(초안 변경 없음 목록, 6절 평가 지표·검증 절차 소절, 뒤 단계를 다뤘다는 문장)을 유지하고 실행 2026-09-25-81(q4-02 답, '검증 방법별로 잡는 오류' 소절, '검증 기록' 재제안의 초안 6절 질문)만 덧붙였으며 프런트매터 version 을 15 로 명시했다.
- 2차: 아이디어 2 페이지 — 5절 append 패치를 게시본(v15)에 적용하도록 하고 6절·auto 영역은 보내지 않아 게시본 그대로 두었으며 프런트매터 version 을 16 으로 명시했다.
- 2차: 아이디어 2 페이지 프런트매터 sources — 게시본 목록(ref-730~ref-746 포함)을 유지하고 없던 ref-416, ref-459, ref-773, ref-777, ref-778, ref-781, ref-782, ref-784, ref-785, ref-786 을 더했다(ref-362·ref-713·ref-031·ref-697 은 이미 있음).
- 2차: 업무 분해·배정 설계 초안 프런트매터 sources 에 ref-773, ref-785, ref-777, ref-416, ref-781, ref-713, ref-459 를 더했다.
- 2차: 새 단계 5 질문 id 를 q5-11 에서 q5-16 으로 고쳤다(backlog_updates, 단계 4 페이지 5절 표, 9절 이력 행, log_entry).
- 2차: 단계 4 페이지 8절(append 로 각주 정의를 직접 넣음)과 아이디어 2 페이지(5절 소절 끝 각주 정의)의 [^ref-782] 발행일을 2026-04 로 고쳤다.
- 2차: 단계 4 페이지 6절 아래 줄을 '다음 단계로 전환: 아니오(명령 권한 q4-03·제한 운영 기준 q4-04 미조사, 열린 질문 q4-03~q4-16)'로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q4-02(실행 전 검증 방법별 포착·놓침 오류, 신뢰도 low; 근거 f1~f26) / 새 질문: q4-15(f22), q4-16(f23), q5-16(f21) / 온톨로지 변경: 없음(v0.8 유지; 개념 '검증 기록' 재제안(f4·f5·f17·f21)은 검증 거부 — 근거에 추정·원문 미열람이 섞였고 '사용자 확인'·배정 '확인 여부'와의 경계 미결정, 로봇 관제 거절의 연계 대상 경계 불일치 — 초안 6절 질문으로 둠) / 완료 조건 평가: 미충족(부족: 확인 절차 초안의 검증 승인 반영, 명령 권한 q4-03, 제한 운영 기준 q4-04; 열린 질문 q4-03~q4-16) / 세부영역 반영 제안: 4건 — 13. 작업 배정 — MRTA(6. 대표 접근법과 기술: 실행 가능성 판정·불변 조건 추론·정수계획 배정과 배치 전 모의 실행, f7·f8·f18·f21·f25), 23. 시험·형식 검증·벤치마크(6절: PDDL 계획 검증기·LTL 검증·제약 디코딩 벤치마크·잠재 실패 벤치마크·LLM 판정자, f3·f10·f11·f12·f15·f19), 22. 시뮬레이션·예측용 디지털 트윈(6절: 개별 지시의 실행 전 모의 실행과 8. 실시간 세계 상태·데이터 일관성에서 초기 상태를 받는 구분, f13·f16·f17·f23), 27. AI·학습·적응과 모델 운영(6절: 구조화 출력·제약 디코딩의 범위와 한계, LTL 제약 디코딩, 판정자 LLM, 방법별로 놓치는 오류, f2·f3·f12·f19·f22) / 다음 실행 제안: q4-03(명령 권한·감사 기록), q4-04(제한 운영 기준); 백로그 중복(q4-09·q4-10 등) 정리
- 개요 진행 현황: 단계 4 질문 q4-02 답함(단계 3 완료·전환 미승인 상태에서 지정 질문으로 다룸, 현재 단계 표기는 단계 3 유지) — 단계 4 열린 질문 14, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-02 | 답함 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-02 | — | — | — |
| q4-15 | 열림 | — | 해석 결과가 스키마·온톨로지 제약·모의 실행을 모두 통과했지만 사용자 의도와 다른 경우(예: 존재하는 다른 도크를 가리킨 해석)를 사람 확인 외에 해석 되말하기나 SELP 식 동치 투표 같은 방법으로 얼마나 잡을 수 있으며, 그 결과를 사람 확인 대상 선정(q4-13)에 어떻게 쓰는가? (q4-02 에서 파생) | 4 | f22 |
| q4-16 | 열림 | — | 배치 전 모의 실행에 허용할 시간 예산(배치 지연 한계) 안에서 무엇을 모의할지(경로 점유, 도크·승강기 예약, 충전 여유), 모의 실행의 초기 상태를 8. 실시간 세계 상태·데이터 일관성의 어느 시점 상태로 잡는지는 어떻게 정하는가? (q4-02 에서 파생) (관련: oq-104) | 4 | f23 |
| q5-16 | 열림 | — | 물류 지시에 오류(기한 누락, 없는 도크, 운반 불가 화물, 뜻과 다른 도크, 점유된 경로)를 주입한 시험 세트로 스키마 검증·온톨로지 제약 대조·계획 검증·모의 실행·사람 확인 각각의 오류 포착률과 확인 비용을 어떻게 재는가? (q4-02 에서 파생) | 5 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 배정 결과의 실행 전 검사: 온톨로지 기반 실행 가능성 판정(ref-236), 불변·전제·사후 조건 추론기(SafePlan, ref-702), 정수계획 배정과 LLM 의 자연어 기반 제약 갱신(건설 사례, ref-783), 배치 전 모의 실행·제약 검사로 최근접 배정의 대기·충돌 영향을 드러낼 가능성([추정], 물류 실측 없음, oq-052). 27. AI·학습·적응과 모델 운영과 양쪽 연결. 근거 f7·f8·f18·f21·f25(실행 2026-09-25-81). |
| 23 | 6. 대표 접근법과 기술 | LLM 계획의 실행 전 검증 방법: PDDL 계획 검증기(VAL, ref-776), LTL 기반 실행 전 검증(VerifyLLM, ref-778), LTL 동치 투표·제약 디코딩(SELP, ref-786), 제약 디코딩 벤치마크(JSONSchemaBench, ref-774·ref-775), 잠재 실패 벤치마크(SIMMER, 프리프린트 [추정], ref-781), 판정자 LLM 반복 검증(ref-779). 수치는 원문 미열람 저자 보고. 근거 f3·f10·f11·f12·f15·f19(실행 2026-09-25-81). |
| 22 | 6. 대표 접근법과 기술 | 개별 지시·계획의 실행 전 모의 실행: 장면 그래프 시뮬레이터 피드백(SayPlan, ref-416), 디지털 트윈 통합 검증(ref-782, 동역학 검증은 연계 대상), 제안–검증–결정 흐름의 시뮬레이션 실행 검사(ref-784). 모의 실행은 가정한 미래를 실험하는 22. 시뮬레이션·예측용 디지털 트윈의 기능이고 초기 상태는 8. 실시간 세계 상태·데이터 일관성의 현재 상태에서 받되 결과를 현재 상태처럼 반영하지 않는다는 구분([추정])을 함께 적는다. 근거 f13·f16·f17·f23(실행 2026-09-25-81). |
| 27 | 6. 대표 접근법과 기술 | LLM 출력 검증 방법: 구조화 출력의 스키마 준수와 값 오류 한계([추정] 벤더 주장, ref-362), 제약 디코딩 벤치마크(ref-774·ref-775), LTL 제약 디코딩(ref-786), 판정자 LLM(ref-779), 방법별로 놓치는 오류([추정] 이 위키의 종합). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결. 근거 f2·f3·f12·f19·f22(실행 2026-09-25-81). |
