# 리서치 브리프 2026-09-25-81

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-81 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 4 · 답한 질문 q4-02

## 갭(비어 있거나 약한 섹션)

- 단계 4 질문 q4-02 열림(target.json 지정, CLI 지정 질문 id). 단계 4 페이지 3절에 q4-02 소제목 없음
- 단계 4 페이지 3절 q4-01 답은 다섯 겹 확인 절차의 배치만 다루고, 검증 방법(스키마 검증·온톨로지 제약 대조·계획 검증·모의 실행·사람 확인)별로 어떤 오류를 잡고 무엇을 놓치는지는 비어 있음
- 완료 조건: 실행 전 검증 단계를 담은 확인 절차 초안이 업무 분해·배정 설계 초안 6절과 아이디어 2. 자연어 업무 지시 챗봇 5절에 검증 승인 상태로 반영되지 않음(명령 권한 q4-03·제한 운영 기준 q4-04 미조사)
- 업무 분해·배정 설계 초안 6절: 개념 '검증 기록'(실행 2026-09-25-71 미반영)과 '사용자 확인'(실행 2026-09-25-79 미반영)의 경계 미해결 — 검증 방법별 기록 항목 근거 없음
- 13. 작업 배정 — MRTA 섹션 6에 배정 결과를 실행 전에 모의 실행·제약 대조로 검사하는 방법 근거 없음
- 23. 시험·형식 검증·벤치마크 섹션 6에 LLM 계획의 실행 전 검증(계획 검증기, LTL 검증, 잠재 실패 벤치마크) 근거 없음
- 22. 시뮬레이션·예측용 디지털 트윈 섹션 6에 개별 지시의 실행 전 모의 실행(dry run) 용도 근거 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q4-02 해석 결과를 실행 전에 검증하는 방법(스키마 검증, 온톨로지 제약 대조, 사람 확인, 모의 실행)에는 무엇이 있고 각각 어떤 오류를 잡는가?
3. 스키마 검증(JSON Schema, 구조화 출력·제약 디코딩)은 해석 결과의 어떤 오류(형식·필수 항목·허용 값)를 잡고, 어떤 오류(형식은 맞지만 값이 틀린 경우)를 놓치는가? (단계 4 페이지 3절, 27. AI·학습·적응과 모델 운영 겨냥)
4. 온톨로지·제약 대조(SHACL 검증 보고, 스킬 제약 검사, 실행 가능성 판정)와 계획 검증기·형식 논리 검증(VAL, LTL 기반 검증)은 능력 불일치·전제 조건 위반·순서 오류 가운데 무엇을 잡는가? (5. 로봇 능력·작업 온톨로지, 13. 작업 배정 — MRTA 섹션 6 겨냥)
5. 모의 실행(장면 그래프 시뮬레이터, 디지털 트윈, 기호 세계 모델)은 실행 불가 동작·잠재 실패·물리적 불가능을 어디까지 잡으며, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 가운데 어디에 속하는가? (22. 시뮬레이션·예측용 디지털 트윈, 23. 시험·형식 검증·벤치마크 연결)
6. 사람 확인과 LLM 판정자(judge)는 결정적 검사가 놓치는 오류(형식·제약은 맞지만 사용자 의도와 다른 해석)를 잡는가, 로봇 관제 쪽(VDA 5050)의 마지막 거절은 어떤 오류 유형을 구분하는가? (18. 사람–로봇 협업·운영 인터페이스, 12. 명령·작업 실행의 신뢰성 연결)
7. 국내에 LLM 로봇 지시·배정 결과를 실행 전에 검증하는 방법을 비교한 연구·사례가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | JSON Schema 검증 어휘(json-schema-spec 저장소 main 브랜치 판)는 인스턴스의 자료형(type), 허용 값(enum·const), 수치 범위(minimum·maximum), 문자열 패턴(pattern), 필수 속성(required), 조건부 필수 속성(dependentRequired), 배열·객체 크기 제한을 검사한다. | ref-773 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [추정] | OpenAI 는 구조화 출력(Structured Outputs)이 모델 출력을 개발자가 준 JSON 스키마에 맞추도록 보장한다고 설명하면서도, 모델이 JSON 객체의 값 안에서는 여전히 실수할 수 있다고 밝힌다. | ref-362 | 아니오 | low | 2024-08 | — | 원문 미열람, 벤더 주장 |
| f3 | [사실] | JSONSchemaBench 는 실제 JSON 스키마 약 1만 개로 제약 디코딩(constrained decoding) 프레임워크를 효율(생성 속도)·범위(지원하는 스키마 기능)·품질(과제 정확도에 주는 영향) 세 측면에서 평가하는 벤치마크이며, 논문은 Guidance·Outlines·Llamacpp·XGrammar·OpenAI·Gemini 여섯 프레임워크를 평가했다. | ref-774, ref-775 | 아니오 | medium | 2025-01 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 은 로봇이 주문을 받기 전 형식 오류(VALIDATION_FAILURE), 쓸 수 없는 선택 필드(UNSUPPORTED_PARAMETER), 수행할 수 없는 동작(INVALID_ORDER_ACTION), 도달할 수 없는 노드(NO_ROUTE_TO_TARGET), 모르는 지도(UNKNOWN_MAP_ID), 범위 밖 시작 노드(START_NODE_OUT_OF_RANGE), 주문을 받지 않는 운용 모드(MOBILE_ROBOT_NOT_AVAILABLE)를 서로 다른 오류 유형으로 보고하고 주문을 내부 버퍼에 받지 않게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f5 | [사실] | W3C SHACL 은 검증 결과를 적합 여부(sh:conforms)와 결과 목록으로 된 검증 보고로 내고, 각 결과에 원인이 된 초점 노드·속성 경로·문제 값·사람이 읽는 메시지·심각도를 담을 수 있다. | ref-459 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f6 | [사실] | Köcher·da Silva·Fay(IEEE INDIN 2021)는 온톨로지로 기술한 기계 스킬에 SHACL 제약을 걸어, 새 스킬을 생산 시스템에 추가할 때 실행에 필요한 필수 정보가 빠진 잘못 모델링된 스킬을 가려내 수정 대상으로 표시하는 방법을 제시했다. | ref-785 | 아니오 | medium | 2021-07 | — | 원문 미열람 |
| f7 | [사실] | Electronics(2026) 논문은 이종 로봇 배정에서 플릿 구성과 대상 물품의 적재 상태가 배정 실행 가능성에 영향을 준다고 보고, 온톨로지 기반 판정 결과(ReasonerOutput)가 여러 배정기에서 공통 실행 가능성 제약으로 작동했다고 보고했다. | ref-236 | 아니오 | medium | 2026-08-11 | 수행 자원 | 원문 미열람 |
| f8 | [사실] | SafePlan 은 LLM 이 만든 자연어 지시·작업 계획·작업 배정 결과를 프롬프트 건전성 추론기와 불변·전제·사후 조건 추론기로 각각 검사한다. | ref-702 | 아니오 | medium | 2025-03 | — | 원문 미열람 |
| f9 | [사실] | Guan 외(NeurIPS 2023)는 LLM 이 PDDL 도메인 모델을 만들고 건전한 도메인 독립 계획기로 계획하되, LLM 이 처음부터 완전한 모델을 만들지 못하는 문제를 PDDL 검증기와 사람의 교정 피드백을 LLM 이 모델에 반영하는 방식으로 다뤘으며, 교정한 모델로 48개 계획 과제를 풀었다고 보고했다. | ref-777 | 아니오 | medium | 2023-05 | — | 원문 미열람 |
| f10 | [사실] | KCL-Planning 의 VAL 저장소는 AI 계획의 계획과 계획 모델(PDDL, 연속 효과·파생 술어·시간 지정 초기 리터럴 포함)을 다루는 계획 검증 도구를 공개한다. | ref-776 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | VerifyLLM 은 과제 기술을 선형 시간 논리(LTL) 식으로 옮긴 뒤 LLM 이 행동 순서를 슬라이딩 윈도(최적 크기 5개 행동)로 분석해, 실행 전에 위치 오류·빠진 전제 행동·중복 행동의 세 가지 계획 불일치를 찾고 재정렬·추가·삭제로 고치는 틀이다. | ref-778 | 아니오 | medium | 2025-07 | — | 원문 미열람 |
| f12 | [사실] | SELP 는 자연어 명령에서 여러 LTL 식을 뽑아 동치인 식끼리 묶어 다수 묶음을 고르는 동치 투표와, LTL 식을 뷔히 오토마톤으로 바꿔 명세와 어긋나는 토큰을 가려 계획을 다시 뽑게 하는 제약 디코딩을 쓰며, 저자들은 드론 항법에서 안전율 10.8%, 로봇 조작에서 20.4% 개선을 보고했다. | ref-786 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f13 | [사실] | SayPlan 은 LLM 이 만든 초기 계획을 장면 그래프 시뮬레이터의 피드백으로 반복 검증·수정해 환경이 부과하는 술어·제약과 맞지 않는 실행 불가 동작을 고치며, 이 반복 재계획으로 실행 가능성이 거의 완전해졌다고 저자들이 보고했다. | ref-416 | 아니오 | medium | 2023-07 | — | 원문 미열람 |
| f14 | [사실] | CAPE 는 동작을 실행할 수 없을 때 전제 조건 오류 정보를 LLM 에 다시 주어 교정 동작을 얻는 방식으로, VirtualHome 에서 사람 주석 계획 정확도를 SayCan 대비 28.89% 에서 49.63% 로 높였다고 저자들이 보고했다. | ref-780 | 아니오 | medium | 2022-11 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | SIMMER 는 실행을 즉시 멈추지 않지만 목표 달성을 조용히 해치는 잠재 실패(latent failure)를 주방 기호 세계 모델(동작 77개, 객체 262개)로 평가하며, 저자들은 여섯 LLM 가운데 오류 없는 계획이 최대 17%, 잠재 실패를 포함한 계획이 최대 56%였고 반사실적 예견 시뮬레이션으로 잠재 실패를 최대 72% 줄였다고 보고했다. | ref-781 | 아니오 | medium | 2026-06 | 예외·성과 | 원문 미열람 |
| f16 | [사실] | Lee 외(Applied Sciences 16(8), 2026)는 LLM 이 만든 로봇 프로그램이 공간적으로 일관되지 않은 명령과 동역학적으로 불가능한 동작 같은 물리적 환각에 취약하다고 보고, 구조화된 중간 작업 표현으로 공간 접지·로봇 선택·실행 전 동역학 검증을 거친 뒤 제조사별 코드를 생성하는 디지털 트윈 통합 검증 틀을 제안했다. | ref-782 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f17 | [사실] | Ko·Lin(arXiv 2609.29061)의 제안–검증–결정(Propose-Verify-Decide) 흐름은 로컬 LLM 이 운영자 의도를 구조화 요구로 바꾸고 후보 전략을 낸 뒤 의미 검사·시뮬레이션 실행·운영 제약 검사를 거쳐 사람이 결정하게 하며, 가상 분류 라인 시험 기록에서 잘못된 입력의 올바른 거부 7/8, 자율 전략 성공 3/10 을 보고했다. | ref-784 | 아니오 | medium | 2026-09 | — | 원문 미열람 |
| f18 | [사실] | Deng 외(arXiv 2506.18178)는 건설 현장 다중 로봇 배정을 정수계획으로 풀고 LLM 이 자연어 상황 서술에서 최적화 제약·파라미터를 갱신하며 디지털 트윈이 현장과 동기화되는 틀을 제안했고, 상위 LLM 들이 제약·파라미터 추출에서 97% 넘는 정확도를 보였다고 보고했다. | ref-783 | 아니오 | medium | 2025-06 | — | 원문 미열람 |
| f19 | [사실] | Hariharan 외(NeurIPS 2025 워크숍)는 판정자 LLM 이 행동 순서를 비평하고 계획자 LLM 이 고치는 반복 검증으로 불필요한 행동·모순·빠진 단계를 찾아, TEACh 수동 주석 행동에서 재현율 최대 90%, 정밀도 100% 를 보고했다. | ref-779 | 아니오 | medium | 2025-09 | — | 원문 미열람 |
| f20 | [사실] | He·Demartini·Gadiraju(CHI 2025)는 계획 후 실행 방식의 LLM 에이전트에서 사용자가 그럴듯해 보이는 계획을 쉽게 잘못 신뢰했다고 보고했고, LangChain 사람 참여 미들웨어는 도구 호출 전에 사람이 승인·인자 수정·거부를 고르게 한다. | ref-713, ref-697 | 아니오 | medium | 2025-04 | — | 원문 미열람 |
| f21 | [추정] | q4-02 에 대해 확인한 자료를 이 위키가 묶으면, 스키마 검증은 형식·필수 항목 누락·허용 값 밖 오류를, 온톨로지·제약 대조는 능력 불일치·필수 정보 누락·안전 불변 조건 위반을, 계획 검증기·형식 논리 검증은 전제 조건 위반·순서 오류·빠진 단계·중복 행동을, 모의 실행은 실행 불가 동작·잠재 실패·물리적 불가능을, 사람 확인은 형식·제약은 맞지만 사용자 의도와 다른 해석을 주로 잡고, 로봇 관제 쪽 거절은 형식·능력·경로·지도·운용 모드 오류를 마지막으로 잡는 분담으로 정리되는 것으로 보인다. | ref-773, ref-362, ref-459, ref-785, ref-702, ref-777, ref-778, ref-416, ref-781, ref-782, ref-713, ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f22 | [추정] | 확인한 자료로는 각 방법이 놓치는 오류도 나뉘는 것으로 보인다: 스키마 검증은 형식은 맞지만 값이 틀린 해석(존재하는 다른 도크 번호 등)을, 제약 대조와 계획 검증은 온톨로지·명세 자체가 틀리거나 LLM 이 명세를 잘못 옮긴 경우를, 모의 실행은 모델 충실도 밖의 상황을, 사람 확인은 그럴듯한 계획에 대한 잘못된 신뢰를 놓칠 수 있어, 한 방법만으로는 해석 오류를 걸러내기 어렵다. | ref-362, ref-777, ref-786, ref-781, ref-713 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f23 | [추정] | 개별 지시의 실행 전 모의 실행은 가정한 미래를 실험하는 기능이므로 22. 시뮬레이션·예측용 디지털 트윈에 속하고, 그 초기 상태는 8. 실시간 세계 상태·데이터 일관성이 표현하는 현재 상태에서 가져와야 하며, 모의 실행 결과를 현재 상태처럼 반영하지 않도록 구분해야 할 것으로 보인다. | ref-416, ref-782, ref-784, ref-783 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 피킹 구역 관리자가 '피킹 끝난 토트를 10시 전까지 2번 도크로'라고 지시하면, 스키마 검증은 기한 슬롯 누락을, 온톨로지 제약 대조는 토트를 운반할 수 없는 로봇 후보를, 모의 실행은 도착 예정 시각의 도크 점유·경로 차단을, 사람 확인은 관리자가 실제로 뜻한 도크가 3번인 경우를, 로봇 관제 쪽 거절은 모르는 지도·도달 불가 노드를 잡는 식으로 나뉠 수 있어 보인다(설명용 가정 사례). | ref-773, ref-785, ref-416, ref-713, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f25 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 배정 결과를 배치 전에 모의 실행이나 최적화 모델의 제약 검사로 확인하면 최근접 배정이 뒤이은 요청의 대기·충돌을 키우는지 실행 전에 드러낼 수 있어 보이나, 이를 물류 플릿에서 잰 자료는 찾지 못했다. | ref-783, ref-784, ref-416 | 아니오 | low | 2026-09-25 | 피킹 / 수행 자원 | 원문 미열람 |
| f26 | [추정] | 이번에 확인한 실행 전 검증 근거의 평가 환경은 가정·주방 시뮬레이터, 도구 호출 JSON 스키마, 건설 현장, 다품종 소량 생산 셀, 가상 분류 라인이었고, 물류 창고 로봇에 채팅으로 준 지시의 검증 방법을 비교한 연구와 국내 연구·사례는 한국어 검색 2회를 포함한 검색 범위에서 찾지 못했다(부재의 확인은 아님). | ref-778, ref-781, ref-782, ref-783, ref-784 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: required 정의: "An object instance is valid against this keyword if every item in the array is the name of a property in the instance." (main 브랜치 초안, 메타스키마 https://json-schema.org/v1/2026, 발행일 미확인, 확인일 기준)
- **f2**: 벤더 주장: 스키마 준수 보장은 제공자 설명. 같은 발표문은 값 안의 실수(예: 수학 풀이 단계 오류)는 막지 못한다고 적는다(검색 요약 기준, 2024-08 발표).
- **f3**: README: 약 10,000개 실제 스키마, efficiency·coverage·quality 평가. 여섯 프레임워크 목록은 논문 초록 요약 기준(원문 미열람). README 와 논문은 같은 저자 그룹이라 독립 교차 아님.
- **f4**: 6.1.4 Order rejection 각 항: "The mobile robot shall not take over the new order in its internal buffer." 오류 유형 표(Table 9) 기준, 공식 저장소 main 브랜치 3.0.0(확인일 2026-09-25)
- **f5**: 검증 보고의 sh:focusNode·sh:resultPath·sh:value·sh:resultMessage·심각도 (재인용: 2026-09-25-74)
- **f6**: 온톨로지 추론에는 스킬 실행에 필요한 정보의 존재를 시험하는 내장 장치가 없어 SHACL 로 필수 정보 제약을 표현(검색 요약 기준, 원문 미열람)
- **f7**: 세 플릿 구성·네 배정기에서 공통 실행 가능성 제약으로 작동(저자 보고, 원문 미열람) (재인용: 2026-09-25-74)
- **f8**: 지시·계획·배정 세 층을 따로 검사하는 구조(원문 미열람) (재인용: 2026-09-25-79)
- **f9**: PDDL validators and humans 를 교정 피드백 원천으로 사용, GPT-4 로 40개 넘는 동작 모델, 48개 과제 해결(저자 보고, 검색 요약 기준)
- **f10**: README: "tools for AI Planning plans and planning models". 검증 실패 시 보고 형식은 README 에 없어 미확인(발행일 미확인, 확인일 기준)
- **f11**: three critical plan inconsistencies: position errors, missing prerequisites, redundant actions(검색 요약 기준, 원문 미열람, 가정 환경 평가)
- **f12**: equivalence voting, constrained decoding(Büchi automaton), domain-specific fine-tuning. 수치는 저자 보고, 검색 요약 기준(원문 미열람)
- **f13**: iterative replanning via scene graph simulator: 비일관성·환각·물리 제약 위반으로 인한 실행 불가 동작 수정(검색 요약 기준, 원문 미열람, 사무실·가정 3D 장면 그래프 조건)
- **f14**: precondition error 를 재프롬프트에 사용, VirtualHome 28.89%→49.63%, Spot 로봇에서도 개선(저자 보고, ICRA 2024, 검색 요약 기준)
- **f15**: latent failures do not immediately halt plan execution; 다수가 되돌릴 수 없는 결과로 이어짐(저자 보고, 동료심사 전 프리프린트, 검색 요약 기준)
- **f16**: physical hallucination, including spatially inconsistent commands and dynamically infeasible motions; 다품종 소량 생산의 이종 로봇 조건(검색 요약 기준, 원문 미열람)
- **f17**: checks semantics, simulation execution, and operational constraints; 요청–검증 근거–결정을 잇는 기록으로 추적성 유지. 30개 고정 시험 기록, 가상 수술기구 분류 라인 4개(저자 보고, 원문 미열람)
- **f18**: narrative-driven schedule adaptation; top-performing models over 97% accuracy in constraint and parameter extraction(건설 사례 연구, 저자 보고, 검색 요약 기준)
- **f19**: Judge LLM critiques, Planner LLM revises; 96.5% 의 순서가 3회 이하 반복으로 수렴(가정 환경 데이터셋, 저자 보고, 검색 요약 기준)
- **f20**: 일상 비서 6개 과제·248명 조건의 신뢰 보정 문제, HITL approve/edit/reject (재인용: 2026-09-25-79)
- **f21**: 방법별 포착 오류는 각 출처의 보고를 이 위키가 대응시킨 종합이며, 다섯 방법을 같은 조건에서 비교한 단일 출처는 찾지 못함
- **f22**: OpenAI 의 값 오류 언급, Guan 외의 불완전 모델 교정 필요, SELP 의 명세 번역 일관성 문제, SIMMER 의 세계 모델 한정 조건, CHI 2025 의 신뢰 보정 문제를 이 위키가 묶은 추론
- **f23**: SayPlan 장면 그래프 시뮬레이터, 디지털 트윈 검증 틀, 제안–검증–결정 흐름의 시뮬레이션 단계, 현장 동기화 디지털 트윈을 분류 원문 7장 구분에 대응시킨 이 위키의 추론
- **f24**: f21 의 분담을 피킹 운반 지시에 적용한 설명용 가정 사례이며 현장 수치는 없음
- **f25**: 정수계획·디지털 트윈 결합(건설), 시뮬레이션 실행 검사(가상 분류 라인), 장면 그래프 모의 실행을 배정 검증에 옮긴 이 위키의 추론
- **f26**: 한국어 검색 2회는 해외 논문 번역 페이지만 반환. 검색 범위 관찰이며 부재 확인 아님

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-773 | JSON Schema (json-schema-org/json-schema-spec GitHub) | json-schema-spec — specs/jsonschema-validation.md (JSON Schema Validation: A Vocabulary for Structural Validation of JSON) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/json-schema-org/json-schema-spec/blob/main/specs/jsonschema-validation.md | 아니오 |
| ref-774 | guidance-ai (JSONSchemaBench GitHub) | jsonschemabench — README (JSONSchemaBench) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/guidance-ai/jsonschemabench | 아니오 |
| ref-775 | Geng, S. 외(JSONSchemaBench 저자, arXiv 2501.10868) | JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | 2025-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2501.10868 | 예 |
| ref-776 | KCL-Planning (VAL GitHub) | VAL — The plan validation system (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/KCL-Planning/VAL | 아니오 |
| ref-777 | Guan, L., Valmeekam, K., Sreedharan, S., & Kambhampati, S. | Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning | 2023-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2305.14909 | 예 |
| ref-778 | VerifyLLM 저자(arXiv 2507.05118) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2507.05118 | 예 |
| ref-779 | Hariharan, A., Dongre, V., Hakkani-Tür, D., & Tur, G. | Plan Verification for LLM-Based Embodied Task Completion Agents | 2025-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2509.02761 | 예 |
| ref-780 | Raman, S. S., Cohen, V., Idrees, I., Rosen, E., Mooney, R., Tellex, S., & Paulius, D. | CAPE: Corrective Actions from Precondition Errors using Large Language Models | 2022-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2211.09935 | 예 |
| ref-781 | Lu, X., Zhang, R. H., & Zhang, R.(Pennsylvania State University) | SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.14574 | 예 |
| ref-782 | Lee, Y.-H., Nam, T., Cho, D.-S., & Kim, W.-T. | LLM-Based Adaptive Control Code Generation Framework with Digital Twin-Integrated Verification for Heterogeneous Robot Systems | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/app16083883 | 예 |
| ref-783 | Deng, M., Fu, B., Li, L., & Wang, X. | Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction | 2025-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2506.18178 | 예 |
| ref-784 | Ko, T.-H., & Lin, C.-T.(National Central University) | Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin | 2026-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2609.29061 | 예 |
| ref-785 | Köcher, A., da Silva, L. M. V., & Fay, A.(Helmut Schmidt University) | Constraint Checking of Skills using SHACL | 2021-07 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/9557549/ | 예 |
| ref-786 | SELP 저자(arXiv 2409.19471) | SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.19471 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-362 | OpenAI | Introducing Structured Outputs in the API | 2024-08 | 벤더 문서 | low | 2026-09-25 | https://openai.com/index/introducing-structured-outputs-in-the-api/ | 예 |
| ref-416 | Rana, K. 외 | SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.06135 | 예 |
| ref-459 | W3C RDF Data Shapes Working Group | Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) | 2017 | 표준 | medium | 2026-09-25 | https://www.w3.org/TR/shacl/ | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-702 | SafePlan 저자(arXiv 2503.06892, 저자 미확인) | SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.06892 | 예 |
| ref-697 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://docs.langchain.com/oss/python/langchain/human-in-the-loop | 예 |
| ref-713 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 2025-04 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/3706598.3713218 | 예 |

### 출처 요약

- **ref-773**: JSON Schema 검증 어휘의 원본(main 브랜치, 차기판 초안). type·enum·const·수치 범위·pattern·required·dependentRequired 등 구조 검증 키워드를 정의한다. 게시된 2020-12 판과 문구가 다를 수 있다.
- **ref-774**: 실제 JSON 스키마 약 1만 개로 구조화 출력 엔진의 효율·범위·품질을 재는 벤치마크의 공식 README.
- **ref-775**: 원문 미열람. 제약 디코딩 프레임워크 여섯 개(Guidance, Outlines, Llamacpp, XGrammar, OpenAI, Gemini)를 1만 개 스키마로 효율·범위·품질 측면에서 평가한 논문.
- **ref-776**: PDDL 계획과 계획 모델을 검증하는 도구 모음의 공식 저장소 README. 연속 효과·파생 술어 등 지원 기능을 언급하며 실패 보고 형식은 README 에 없다.
- **ref-777**: 원문 미열람. LLM 이 PDDL 도메인 모델을 만들고 PDDL 검증기·사람의 교정 피드백으로 고친 뒤 도메인 독립 계획기로 계획하는 방법(NeurIPS 2023).
- **ref-778**: 원문 미열람. 과제 기술을 LTL 로 옮기고 LLM 이 행동 순서를 분석해 위치 오류·빠진 전제 행동·중복 행동을 실행 전에 찾아 고치는 틀.
- **ref-779**: 원문 미열람. 판정자 LLM 과 계획자 LLM 의 반복 검증으로 불필요한 행동·모순·빠진 단계를 고치는 틀, TEACh 에서 평가(NeurIPS 2025 워크숍).
- **ref-780**: 원문 미열람. 전제 조건 오류 정보를 LLM 에 재프롬프트해 교정 동작을 얻는 방법, VirtualHome 과 Spot 로봇에서 평가(ICRA 2024).
- **ref-781**: 원문 미열람. 주방 기호 세계 모델로 LLM 계획의 잠재 실패를 평가하는 벤치마크와 반사실적 예견 시뮬레이션의 효과(동료심사 전 프리프린트).
- **ref-782**: 원문 미열람. 이종 로봇 제어 코드 생성에서 물리적 환각을 막으려 중간 작업 표현·로봇 선택·실행 전 동역학 검증을 디지털 트윈으로 수행하는 틀(Applied Sciences 16(8), 3883).
- **ref-783**: 원문 미열람. 정수계획 배정, LLM 의 자연어 기반 제약 갱신, 디지털 트윈 동기화를 결합한 건설 다중 로봇 배정 틀.
- **ref-784**: 원문 미열람. 로컬 LLM·디지털 트윈·사람 결정을 잇는 제안–검증–결정 흐름으로 의미·시뮬레이션 실행·운영 제약을 검사하고 추적 기록을 남기는 다중 라인 작업 조정 시스템.
- **ref-785**: 원문 미열람. 온톨로지로 기술한 기계 스킬에 SHACL 제약을 걸어 실행에 필요한 필수 정보 누락을 검사하는 방법(IEEE INDIN 2021).
- **ref-786**: 원문 미열람. LTL 동치 투표, 뷔히 오토마톤 기반 제약 디코딩, 도메인 미세 조정으로 안전한 로봇 계획을 생성하는 방법.
- **ref-031**: VDA 5050 3.0.0 명세 원문(공식 저장소 main 브랜치). 주문 거절 사유와 오류 유형 표를 정의한다.
- **ref-362**: 원문 미열람. 모델 출력을 JSON 스키마에 맞추는 구조화 출력 기능 발표. 값 안의 실수는 막지 못한다고 언급.
- **ref-416**: 원문 미열람. 3D 장면 그래프 기반 LLM 계획과 장면 그래프 시뮬레이터 피드백을 이용한 반복 재계획.
- **ref-459**: 원문 미열람. RDF 그래프를 형상 제약으로 검증하고 검증 보고를 내는 W3C 표준(이번 실행에서는 다시 열지 않음).
- **ref-236**: 원문 미열람. 온톨로지 기반 실행 가능성 판정 결과를 배정기 독립 출력(ReasonerOutput)으로 정형화한 연구.
- **ref-702**: 원문 미열람. 지시·계획·배정 결과를 건전성·불변·전제·사후 조건 추론기로 검사하는 LLM 로봇 계획 안전 틀.
- **ref-697**: 원문 미열람. 도구 호출 전 에이전트를 멈추고 사람이 승인·수정·거부·직접 응답을 고르게 하는 미들웨어(이번 실행에서는 다시 열지 않음).
- **ref-713**: 원문 미열람. 계획 후 실행 LLM 에이전트에서 사용자 신뢰와 팀 성과를 조사한 CHI 2025 사용자 연구.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | 2, 3, 4, 5, 6, 8, 9 | q4-02 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26 (신뢰도 low) — 2절 q4-02 상태 답함, 3절 q4-02 소제목 신설({#q4-02}): 스키마 검증(JSON Schema 어휘 f1, 구조화 출력의 한계 f2 벤더 주장, 제약 디코딩 벤치마크 f3), 온톨로지·제약 대조(SHACL 검증 보고 f5, 스킬 제약 검사 f6, 실행 가능성 판정 f7, 불변·전제·사후 조건 f8), 계획 검증기·형식 논리(PDDL 검증기 교정 f9·f10, LTL 기반 VerifyLLM f11, SELP 동치 투표·제약 디코딩 f12), 모의 실행(장면 그래프 시뮬레이터 f13, 전제 조건 오류 피드백 f14, 잠재 실패 f15, 디지털 트윈 검증 f16·f17·f18), LLM 판정자 f19, 사람 확인 f20, 로봇 관제 쪽 거절 오류 유형 f4, 종합: 방법별 포착 오류 표(f21, 표 권장)·방법별 놓치는 오류(f22)·8. 실시간 세계 상태·데이터 일관성 대 22. 시뮬레이션·예측용 디지털 트윈 구분(f23)·피킹 시나리오(f24)·SCM 질문 연결(f25)·근거 공백(f26) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 5 | 아이디어 페이지 5절(트랙 산출물): '오해석 방지 확인 절차' 소절에 '검증 방법별로 잡는 오류' 하위 내용 추가 — 방법별 포착·놓침 표(f21·f22, 추정), 근거 f1·f4·f5·f9·f11·f13·f15·f17·f20. 모의 실행은 22. 시뮬레이션·예측용 디지털 트윈 기능이며 초기 상태는 8. 실시간 세계 상태·데이터 일관성에서 가져온다는 구분(f23) 명시. 명령 권한(q4-03)·제한 운영 기준(q4-04)은 미조사로 유지 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(개념 '검증 기록' 재제안, 속성 '검증 방법'·'검출 오류 유형')가 승인되면 2절 반영과 초안 버전 인상(f4·f5·f17·f21). 미승인 시 6절 '검증 기록' 질문에 q4-02 답(f21·f22) 연결하고, 사람 확인은 '사용자 확인' 질문과 따로 두는 경계 메모 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f7, f8, f18, f21, f25): 배정 결과의 실행 전 검사(실행 가능성 판정, 불변 조건 추론, 정수계획 배정과 LLM 제약 갱신), 배치 전 모의 실행으로 최근접 배정의 영향을 드러내는 가능성과 분류 원문 질문 연결. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f3, f10, f11, f12, f15, f19): LLM 계획의 실행 전 검증 방법(PDDL 계획 검증기, LTL 기반 검증, 제약 디코딩 벤치마크, 잠재 실패 벤치마크, LLM 판정자) |
| update | docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f13, f16, f17, f23): 개별 지시·계획의 실행 전 모의 실행(장면 그래프 시뮬레이터, 디지털 트윈 검증)과 8. 실시간 세계 상태·데이터 일관성에서 초기 상태를 받는 구분 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f2, f3, f12, f19, f22): LLM 출력 검증 방법(구조화 출력·제약 디코딩의 범위와 한계, LTL 제약 디코딩, 판정자 LLM)과 방법별로 놓치는 오류. 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 제약 디코딩 | Constrained Decoding | 언어 모델이 토큰을 생성할 때 스키마·문법·오토마톤에 맞지 않는 토큰을 가려, 출력이 정해진 형식이나 명세를 벗어나지 않게 하는 생성 방식이다. |
| JSON 스키마 | JSON Schema | JSON 데이터의 자료형·허용 값·필수 속성·수치 범위 같은 구조 제약을 기술하고 인스턴스가 이를 따르는지 검증하는 명세다. |
| 잠재 실패 | Latent Failure | 계획 실행을 즉시 멈추지는 않지만 목표 달성을 조용히 해치고 때로 되돌릴 수 없는 결과로 이어지는 계획 오류다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터 로봇 관제에서 작업 지시나 배정 결과를 배치 전에 시뮬레이션(디지털 트윈)으로 모의 실행해 확인하는 운영 사례나 연구가 있는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 13. 작업 배정 — MRTA | 근거: f26 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 25회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 방법마다 단일 논문·단일 문서이며 f3 의 README 와 논문은 같은 저자 그룹
    - f2 OpenAI 구조화 출력의 보장·한계 문구는 검색 요약 기준(원문 미열람, 벤더 주장)
    - f6·f9·f11~f19 는 검색 요약 기준 원문 미열람, 수치는 저자 보고값
    - f10 VAL 의 검증 실패 보고 형식(수리 조언 등) 미확인
    - f1 JSON Schema 는 main 브랜치 차기판 초안 기준이며 게시된 2020-12 판과의 문구 차이 미확인
    - ref-778·ref-786 저자 목록 미확인
    - f21~f26 은 이 위키의 종합이며 다섯 검증 방법을 같은 조건에서 비교한 단일 출처는 찾지 못함
    - 물류 창고 로봇 채팅 지시의 검증 방법 비교 연구·국내 사례 부재는 검색 범위 관찰
- 범위 경계 위반 의심:
    - f16: 동역학 검증·동작 스케일링은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이며, ROP 쪽은 로봇 선택·공간 접지 수준의 검증만 서술하도록 제안
    - f4: 로봇의 주문 거절은 로봇 쪽 기능(연계 대상)이며 ROP 는 거절 오류를 받아 확인 절차의 마지막 결과로 다루는 쪽만 서술
    - f18: 건설 현장 사례는 업종별 조건이라 방법 근거로만 제안
    - f23: 모의 실행을 22. 시뮬레이션·예측용 디지털 트윈으로, 초기 상태를 8. 실시간 세계 상태·데이터 일관성으로 구분해 두 영역을 섞지 않도록 명시
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 신규 출처: ref-773(JSON Schema 검증 어휘)·ref-774(JSONSchemaBench README)·ref-776(VAL README). ref-031 은 입력 원문 텍스트(inbox). 나머지 신규 11건과 재사용 ref-362·ref-416·ref-459·ref-236·ref-702·ref-697·ref-713 은 이번 실행에서 원문을 열지 않아 신뢰도 상한 medium, 원문을 연 출처도 공통 규칙 0절 6항에 따라 high 를 주지 않음. 검색 25회/40(한국어 2회), 신규 출처 14건/20(ref-773~ref-786, 예약 구간 안), 재사용 8건. 질문 선택: target.json 지정 q4-02 1건. q4-02 는 방법별 근거(사실)로 답했으나 방법별 포착·놓침 분담(f21·f22)과 시나리오(f24)는 이 위키의 종합이고 근거가 물류 플릿 조건이 아니라 질문 종합 신뢰도 low. 이 실행도 단계 3 완료가 승인되지 않은 상태에서 지정된 질문으로 단계 4 를 다룸. 한국 자료: 한국어 검색 2회는 해외 논문 번역 페이지만 나와 국내 연구·사례를 찾지 못함(일반 열린 질문 1건). 교차 규칙: LLM 출력 검증 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA 양쪽에 반영 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈: 모의 실행은 22, 초기 상태는 8 로 구분(f23). 정정 요청 없음. 후속 질문 3건. 온톨로지 변경 제안 1건('검증 기록' 재제안, 이전 미반영 사유와 경계를 description 에 명시). 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 4건(갱신 상한과 별도). 백로그 참고: q4-09·q4-10, q3-12·q3-13, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06 중복 등록 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 4
- 답한 질문 id: q4-02

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 해석 결과가 스키마·온톨로지 제약·모의 실행을 모두 통과했지만 사용자 의도와 다른 경우(예: 존재하는 다른 도크를 가리킨 해석)를 사람 확인 외에 해석 되말하기나 SELP 식 동치 투표 같은 방법으로 얼마나 잡을 수 있으며, 그 결과를 사람 확인 대상 선정(q4-13)에 어떻게 쓰는가? (q4-02 에서 파생) | 4 | f22 |
| — | 배치 전 모의 실행에 허용할 시간 예산(배치 지연 한계) 안에서 무엇을 모의할지(경로 점유, 도크·승강기 예약, 충전 여유), 모의 실행의 초기 상태를 8. 실시간 세계 상태·데이터 일관성의 어느 시점 상태로 잡는지는 어떻게 정하는가? (q4-02 에서 파생) (관련: oq-104) | 4 | f23 |
| — | 물류 지시에 오류(기한 누락, 없는 도크, 운반 불가 화물, 뜻과 다른 도크, 점유된 경로)를 주입한 시험 세트로 스키마 검증·온톨로지 제약 대조·계획 검증·모의 실행·사람 확인 각각의 오류 포착률과 확인 비용을 어떻게 재는가? (q4-02 에서 파생) | 5 | f21 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| add | concept | 검증 기록 (Verification Record) | f4, f5, f17, f21 | 해석 결과·계획·배정이 실행 전 결정적 검사를 거친 결과의 기록. 속성 후보: 검증 방법(값 후보: 스키마 검증 / 온톨로지·제약 대조 / 계획 검증 / 모의 실행 / 로봇 관제 거절), 결과(적합 / 위반), 위반 위치·사유(SHACL 검증 보고의 초점 노드·속성 경로·메시지 f5, VDA 5050 오류 유형 f4), 검사 시각. 실행 2026-09-25-71 에서 같은 이름의 제안이 배정 속성 '확인 여부'·'사용자 확인' 질문과 겹쳐 반영되지 않았으므로, 이번 제안은 사람 확인을 담지 않고 결정적 검사만 담는 것으로 경계를 좁혔다(사람 확인은 초안 6절의 '사용자 확인' 질문으로 남김). 요청–검증 근거–결정을 잇는 추적 기록의 사례는 f17. 검증 방법 값의 분담(f21)은 추정이라 값 목록은 후보로만 둔다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 실행 전 검증 단계 초안(q4-01 다섯 겹 절차, 이번 q4-02 방법별 포착 오류)이 검증 승인 전이며 업무 분해·배정 설계 초안 6절·아이디어 2. 자연어 업무 지시 챗봇 5절에 확정 반영되지 않음
    - 명령 권한(q4-03) 미조사
    - 제한 운영 기준(q4-04) 미조사
    - 열린 질문 q4-03~q4-14(q4-09·q4-10 중복 정리 필요)
