# 리서치 브리프 2026-09-25-74

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-74 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 3 · 답한 질문 q3-03

## 갭(비어 있거나 약한 섹션)

- 단계 3 질문 q3-03 열림(target.json 지정, CLI 지정 질문 id). 단계 3 페이지 3절에 q3-03 소제목 없음
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 5절에 다른 아이디어와의 연결 없음, 온톨로지 질의 결과(후보 없음·후보 여럿)에 따른 되묻기 흐름 없음
- 완료 조건: 실험 페이지에 사용자에게 제안하는 실험 계획 없음(스토리텔러 몫)
- 업무 분해·배정 설계 초안: 배정이 실패했을 때(수행 가능한 로봇 없음)의 사유와 사용자에게 제시한 대안을 담는 개념·속성 없음
- 13. 작업 배정 — MRTA 섹션 6에 배정 실패 처리와 후보가 여럿일 때의 결정 규칙(평가기) 근거 없음
- 18. 사람–로봇 협업·운영 인터페이스 섹션 6에 되묻기·폴백·사람 인계 기준 근거 약함

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q3-03 온톨로지 질의가 수행 가능한 로봇을 찾지 못하거나 후보를 여럿 낼 때, 챗봇은 무엇을 사용자에게 되묻고 무엇을 스스로 정하는가?
3. 오케스트레이션 도구(Open-RMF 디스패처·입찰 평가기, VDA 5050 주문 거절)는 수행 가능한 플릿·로봇이 없거나 여럿일 때 무엇을 기록하고 무엇을 자동으로 결정하는가? (단계 3 페이지 3절, 13. 작업 배정 — MRTA 섹션 6 겨냥)
4. 계획기·최적화 해법·온톨로지 검증은 '왜 실행할 수 없는지'를 사람이 고칠 수 있는 형태(해결 불가 설명, 불능 제약 집합, 검증 보고, 대조적 설명)로 돌려줄 수 있는가? (5. 로봇 능력·작업 온톨로지, 27. AI·학습·적응과 모델 운영 연결)
5. 후보가 여럿이거나 해석이 모호할 때 되묻기 여부를 정하는 기준(등각 예측, 내성적 계획, 정보 가치 기반 질문 선택, 폴백·사람 인계)은 무엇이며 되묻기 부담을 어떻게 줄이는가? (18. 사람–로봇 협업·운영 인터페이스 겨냥)
6. 실행 불가 작업을 배정에서 빼거나 사람 처리로 넘기는 방식과, 이를 다룬 국내 물류 관제 사례가 있는가? (20. 예외 복구·재계획·업무 연속성 연결, 한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 디스패처는 입찰 기간에 어떤 플릿 어댑터도 입찰하지 않으면 작업의 배정 상태를 FailedToAssign 으로 두고 'No fleet adapters offered a bid' 오류(코드 10)를 기록하며, 그 작업은 수행되지 않는다. | ref-713 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | Open-RMF 에서 플릿 어댑터는 설정에서 해당 작업 유형(청소·배송·순회)을 받도록 구성되어 있지 않으면 그 작업에 입찰하지 않으며, 공식 플릿 어댑터 템플릿 설정은 task_capabilities 로 loop·delivery 를 켜 둔다. | ref-039, ref-105 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [사실] | Open-RMF 작업 상태 스키마의 dispatch 필드는 상태(queued·selected·dispatched·failed_to_assign·canceled_in_flight)와 함께 배정 대상(fleet_name, expected_robot_name)과 오류 배열(errors)을 두어, 배정 실패의 사유를 기록할 자리를 제공한다. | ref-111 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | Open-RMF 디스패처는 여러 플릿이 입찰하면 평가기(evaluator)로 하나를 고르며, 기본 평가기는 가장 빨리 끝나는 입찰을 고르는 QuickestFinishEvaluator 이고 LeastFleetCostEvaluator·LeastFleetDiffCostEvaluator 로 바꾸거나 사용자 정의 평가기를 넣을 수 있다. | ref-713, ref-714 | 아니오 | medium | 2026-09-25 | 피킹 / 수행 자원 | — |
| f5 | [사실] | Open-RMF 작업 요청 스키마의 선택 필드 fleet_name 은 이 작업을 수행하도록 허용된 플릿(하나 또는 여러 개)을 지정하며, 지정하면 그 플릿만 입찰한다. | ref-125 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f6 | [사실] | VDA 5050 3.0.0 에서 이동로봇은 수행할 수 없는 동작이 담긴 주문(예: 최대 인상 높이를 넘는 인상)을 INVALID_ORDER_ACTION 오류로, 쓸 수 없는 선택 필드는 UNSUPPORTED_PARAMETER 로, 새 주문을 받을 수 없는 운용 모드에서는 MOBILE_ROBOT_NOT_AVAILABLE 로 거절해, 능력 부족과 일시적 가용 불가를 서로 다른 오류로 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f7 | [사실] | Electronics(2026) 논문은 이종 로봇 배정에서 플릿 구성과 대상 물품의 적재 상태가 모두 배정 실행 가능성에 영향을 준다고 보고, 온톨로지 기반 판정 결과(ReasonerOutput)가 세 가지 플릿 구성과 네 가지 배정기에서 공통 실행 가능성 제약으로 작동했다고 보고했다. | ref-236 | 아니오 | medium | 2026-08-11 | 수행 자원 | 원문 미열람 |
| f8 | [사실] | W3C SHACL 은 검증 결과를 sh:conforms(적합 여부)와 결과 목록(sh:result)으로 된 검증 보고로 내고, 각 결과에 원인이 된 초점 노드(sh:focusNode)·속성 경로(sh:resultPath)·문제 값(sh:value)·제약 구성요소·사람이 읽는 메시지(sh:resultMessage)·심각도를 담을 수 있다. | ref-459 | 아니오 | medium | 2017-07 | — | — |
| f9 | [사실] | Göbelbecker 외(ICAPS 2010)는 계획을 찾지 못할 때 그 이유로 '변명(excuse)', 곧 계획 과제를 풀 수 있게 만드는 초기 상태의 반사실적 변경을 찾는 형식화와 알고리즘을 제안했다. | ref-717 | 아니오 | medium | 2010 | — | 원문 미열람 |
| f10 | [사실] | Sreedharan 외는 사용자가 준 제약(plan advice, 예: 주 엘리베이터를 쓰지 말라)이 계획을 풀 수 없게 만드는 원인일 수 있다고 보고, 계층적 추상화와 계획 랜드마크로 사람이 이해할 수 있는 해결 불가 사유를 만드는 방법을 제안했다. | ref-718 | 아니오 | medium | 2019-03 | — | 원문 미열람 |
| f11 | [사실] | OptiChat(Chen 외)은 GPT-4 가 최적화 해법기와 함수 호출로 연결되어 모델을 실행 불가능하게 만드는 최소 제약 집합(IIS)을 찾고, 불능 원인을 자연어로 설명하며 실행 가능하게 고칠 제안을 내는 대화형 시스템이다. | ref-719 | 아니오 | medium | 2023-08 | — | 원문 미열람 |
| f12 | [사실] | CE-MRS(Schneider 외, 2024)는 작업 배정·스케줄링·경로 계획 정보를 골라 써서 다중 로봇 시스템의 해를 사람에게 대조적으로 설명하는 방법이며, 운영자 사용자 연구에서 시스템 명세의 오류를 찾아 고치는 능력이 유의하게 좋아졌다고 저자들이 보고했다. | ref-720 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f13 | [사실] | Shida 외는 무게를 모르는 물체의 다중 로봇 운반 배정에서 운반 불가 작업이 로봇 정지(교착)를 부를 수 있다고 보고, 작업 경험을 공유해 로봇마다 작업별 배제 수준을 학습하고 실행 불가로 보이는 작업을 일시적으로 배제하는 방법을 제안했다. | ref-723 | 아니오 | medium | 2024-04 | 예외·성과 | 원문 미열람 |
| f14 | [사실] | CLARA 는 LLM 불확실성과 상황 맥락으로 불확실한 명령을 모호한 명령과 수행 불가능한 명령으로 나누어, 모호한 명령은 질문을 만들어 사용자와 대화로 풀고 수행 불가능한 명령은 거절한다. | ref-352, ref-353 | 아니오 | medium | 2024 | 시작 조건 | 원문 미열람 |
| f15 | [사실] | KnowNo 는 LLM 계획기가 낸 선택지 가운데 등각 예측으로 정한 문턱을 넘는 것이 둘 이상이면 사람에게 도움을 요청하고, 하나면 스스로 실행한다. | ref-350, ref-351 | 아니오 | medium | 2023-07 | — | 원문 미열람 |
| f16 | [사실] | 내성적 계획(Introspective Planning, NeurIPS 2024)은 사람이 고른 안전한 계획의 사후 추론 예시를 지식 기반으로 검색해 LLM 불확실성을 과업 모호성에 맞추며, 등각 예측과 결합해 성공 보장을 유지하면서 불필요한 되묻기를 줄였다고 저자들이 보고했다. | ref-721 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f17 | [사실] | SAGE-Agent(Suri 외, ACL 2026 Findings)는 도구 인자와 그 값 영역 위에서 사용자가 원하는 것에 대한 명세 불확실성과 모델 예측 불확실성을 나누고, 질문마다 완전 정보의 기대 가치(EVPI)와 질문 비용을 따져 되물을 질문을 고르며, 기준선 대비 모호 과제 달성 범위를 7~39% 늘리고 질문 수를 1.5~2.7배 줄였다고 보고했다. | ref-722 | 아니오 | medium | 2025-11 | — | 원문 미열람 |
| f18 | [사실] | Rasa 는 의도 분류 신뢰도가 문턱(기본 0.7) 아래면 폴백으로 넘어가 다시 말해 달라고 요청하고, 두 단계 폴백에서는 추정한 의도를 사용자에게 확인받고 부정하면 재진술을 요청한 뒤, 끝까지 실패하면 최종 폴백으로 보통 사람 상담원에게 대화를 넘긴다. | ref-716 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f19 | [사실] | 개인 연구자가 공개한 Plan-Failure-Bench 는 LLM 계획기가 실행 가능한 계획, 사유를 단 infeasible, 후보 지시 대상을 단 clarify 가운데 하나로 답하게 하고 도달 불가 목표·능력 부족·모호한 지칭 등 여섯 함정 유형을 기계 검증 정답으로 평가하며, 시험한 어떤 모델도 능력 부족과 도달 불가 목표를 구분하지 못했다고 보고한다. | ref-724 | 아니오 | low | 2026-09-25 | — | — |
| f20 | [사실] | LAPPI 는 LLM 이 대화로 사용자의 모호한 선호를 후보 항목·선호 점수·제약으로 바꿔 최적화 문제를 인스턴스화하고, 풀이는 기존 해법기에 맡기는 대화형 최적화 방식이다. | ref-598 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f21 | [사실] | 로봇 능력 온톨로지(RCO) 연구(Scientific Reports, 2025)는 제조사가 광고한 능력과 경험적으로 측정한 운용 능력을 함께 표현하고 SPARQL 질의로 둘을 비교해, 선언 능력과 실제 성능이 다를 수 있음을 온톨로지 안에서 다룬다. | ref-041 | 아니오 | medium | 2025 | 수행 자원 | 원문 미열람 |
| f22 | [추정] | q3-03 의 '후보 없음'에 대해 확인한 자료를 이 위키가 묶으면, 원인은 (1) 능력 부재(어느 플릿도 그 작업 유형·능력을 선언하지 않음), (2) 일시적 가용 불가(운용 모드·배터리 임계값·점유), (3) 제약 조합의 불능(적재 상태 도달 가능성·기한), (4) 해석 오류(잘못 채운 슬롯)로 나뉘며, 챗봇은 원인과 함께 사용자가 바꿀 수 있는 항목(기한 완화, 장소·대상 변경, 사람 처리 전환)만 되묻고 재질의·대기·재입찰은 시스템이 정하는 분담이 근거가 가장 많은 것으로 보인다. | ref-713, ref-039, ref-031, ref-236, ref-105, ref-717, ref-718, ref-719, ref-714 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f23 | [추정] | q3-03 의 '후보 여럿'에 대해서는, 후보 사이 차이가 완료 시각·비용처럼 시스템이 계산할 수 있는 목적 기준뿐이면 미리 정한 평가기·최적화로 스스로 정하고 결과를 설명하며, 차이가 사용자만 아는 정보나 선호(어느 화물·장소인지, 기한과 비용의 교환)에 걸리거나 해석 자체가 여러 갈래일 때만 되묻는 분담이 근거가 가장 많은 것으로 보인다. | ref-713, ref-376, ref-350, ref-722, ref-721, ref-598, ref-720 | 아니오 | low | 2026-09-25 | 피킹 / 수행 자원 | — |
| f24 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 후보가 여럿일 때 '가장 가까운 로봇'은 평가기 선택지의 하나일 뿐이므로 챗봇이 채팅마다 사용자에게 고르게 하기보다 운영 조직이 평가 기준을 미리 정해 두고 채팅에서는 그 기준에 따른 선택 이유를 설명하는 편이 전체 기준의 일관성에 맞는 것으로 보인다. | ref-713, ref-714, ref-720 | 아니오 | low | 2026-09-25 | 피킹 / 수행 자원 | — |
| f25 | [추정] | 피킹 단계에서 관리자가 채팅으로 토트 운반을 지시했는데 어떤 플릿도 입찰하지 않으면, 챗봇은 배정 실패 기록(failed_to_assign·오류)을 근거로 원인을 설명하고 기한 완화·다른 장소·사람 작업자 처리 같은 선택지를 되묻는 흐름이 가능해 보인다(설명용 가정 사례). | ref-713, ref-111, ref-716, ref-719 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f26 | [추정] | 이번에 확인한 배정 실패 설명·되묻기 근거의 평가 환경은 고전 계획 벤치마크, 운영과학 최적화 모델, 실험실 다중 로봇, 도구 호출 대화, 가정·사무실 시뮬레이션이었고, 물류 창고 로봇 관제에서 배정 실패를 사용자와 대화로 처리한 연구와 국내 사례는 한국어 검색 포함 검색 범위에서 찾지 못했다(부재의 확인은 아님). | ref-717, ref-719, ref-720, ref-722, ref-724, ref-723 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: Dispatcher.cpp: 입찰 제출이 없으면 dispatch_state->status = FailedToAssign, 오류 메시지 "No fleet adapters offered a bid for task", 경고 로그 'Dispatching failed, and the task will not be performed'.
- **f2**: task_types.md: fleet adapter needs to be configured to accept Clean type of task. Else, it will not submit a bid; 로그 예 'Fleet [tinyRobot] is configured to not accept task'. 템플릿 config.yaml: task_capabilities loop True, delivery True (두 출처 모두 Open Robotics 계열로 독립 교차 아님).
- **f3**: task_state.json dispatch: status enum queued/selected/dispatched/failed_to_assign/canceled_in_flight, assignment{fleet_name, expected_robot_name}, errors(array, 외부 error 스키마 참조).
- **f4**: Dispatcher.cpp: Auctioneer::make(..., std::make_shared<bidding::QuickestFinishEvaluator>()); 공개 메서드 evaluator(...)로 교체. Auctioneer.hpp: 세 평가기 클래스 정의, 각 순위 기준 문서화는 없음.
- **f5**: task_request.json fleet_name(string 또는 array): "If specified, only the named fleet(s) will bid for this task." 필수는 category·description 뿐.
- **f6**: 6.1.4.2~6.1.4.9: order with actions it cannot perform (lifting height higher than maximum) → 'INVALID_ORDER_ACTION' WARNING; unsupported optional fields → 'UNSUPPORTED_PARAMETER' CRITICAL; operating mode not allowing orders → 'MOBILE_ROBOT_NOT_AVAILABLE'. (3.0.0, 공식 저장소 main)
- **f7**: 검색 요약: four scenarios over three fleet configurations and four allocators; ReasonerOutput consistently functioned as a shared semantic feasibility constraint; fleet composition and loaded state affect assignment feasibility. (원문 미열람)
- **f8**: W3C data-shapes 저장소 편집자 초안: "The value of sh:conforms is true if and only if the validation did not produce any validation results"; focusNode·sourceConstraintComponent·resultSeverity 필수, resultPath·value·sourceShape·resultMessage 선택. 권고안 본문과 문구 차이 가능.
- **f9**: 검색 요약: excuses are counterfactual alterations to the planning task such that the new task will be solvable; 계획 실패는 원리적 불가능이거나 과제 기술이 불완전·부정확해서 생길 수 있다. (ICAPS 2010 pp.81–88, 원문 미열람)
- **f10**: 검색 요약: users often provide advice or constraints that might be the very reason a goal becomes unreachable; hierarchical abstractions generate compact, human-understandable reasons for unsolvability. (arXiv 1903.08218, 원문 미열람)
- **f11**: 검색 요약: interfaces with an optimization solver to identify the Irreducible Infeasible Subset (IIS); identify potential sources of infeasibility, offer suggestions to make the model feasible. (arXiv 2308.12923, INFOR 2024 게재, 원문 미열람)
- **f12**: 검색 요약: contrastive explanations incorporating data from multi-robot task allocation, scheduling, and motion-planning; user studies show significant improvements in ability to identify and solve errors in specifications. (arXiv 2410.08408, IEEE 저널 게재, 원문 미열람)
- **f13**: 초록 요약: presence of infeasible tasks (untransportable objects) can lead to robot stoppage (deadlock); robots learn exclusion levels to exclude infeasible tasks; temporary exclusion of tasks considered infeasible. (arXiv 2404.11817, 원문 미열람)
- **f14**: 프로젝트 페이지·논문(IEEE RA-L 2024)이 명확/모호/수행 불가 3분류와 모호한 명령의 질문 생성, 수행 불가 명령 거절을 설명. 같은 저자 계열이라 독립 교차 아님. (재인용: 2026-09-25-30)
- **f15**: 등각 예측으로 만든 예측 집합이 단일 선택지가 아니면 도움 요청, 사용자가 정한 성공 수준을 통계적으로 보장. 같은 저자 계열(프로젝트 페이지·논문). (재인용: 2026-09-25-30)
- **f16**: 검색 요약: combination with conformal prediction achieves tighter confidence bounds, maintaining statistical success guarantees while minimizing unnecessary user clarification requests; avoids over-asking, lowest unsafe rate. (arXiv 2402.06529, 원문 미열람)
- **f17**: 검색 요약: separating specification uncertainty from model uncertainty; EVPI balanced against aspect-based cost; coverage +7–39%, clarification questions reduced 1.5–2.7× (ClarifyBench: 문서 편집·차량 제어·여행 예약, 저자 보고, 원문 미열람).
- **f18**: fallback-handoff.mdx: FallbackClassifier threshold(기본 0.7) → nlu_fallback; action_two_stage_fallback: 의도 확인 → 거부 시 재진술 → 'ultimate fallback action'(typically handoff to human), 대화 기록 전달.
- **f19**: README: answer in JSON — a plan, infeasible with a reason, or clarify with candidate referents; traps: unreachable goals, missing robot capabilities, ambiguous object references 등; "No model separates a missing capability from an unreachable goal." (동료심사 전, Zenodo 프리프린트)
- **f20**: LLM-assisted preference-based problem instantiation, 해법은 기존 최적화 해법기; 여행 계획 사용자 연구에서 실행 가능 계획 개선(저자 보고, 원문 미열람). (재인용: 2026-09-25-66)
- **f21**: 검색 요약: Robot Capability Ontology bridging manufacturer specifications and empirical performance data; SPARQL queries retrieve and compare advertised and operational repeatability capabilities. (원문 미열람)
- **f22**: 이 위키의 종합: 원인 구분은 Open-RMF 무입찰·task_capabilities, VDA 5050 오류 유형(능력 대 가용), 적재 상태 판정에서, '바꿀 수 있는 항목' 제시는 excuse·plan advice·IIS 연구에서 도출. 이 분류를 제시한 단일 출처 없음.
- **f23**: 이 위키의 종합: 자동 결정은 Open-RMF 평가기(f4), 되묻기 조건은 KnowNo 예측 집합(f15)·EVPI 질문 선택(f17)·불필요한 되묻기 감소(f16), 선호 반영은 LAPPI(f20), 설명은 CE-MRS(f12). 물류 조건 평가 없음.
- **f24**: Open-RMF 기본 평가기는 QuickestFinish, 교체 가능(f4). 평가 기준을 누가 정하는지는 출처에 없음 — 이 위키의 추론.
- **f25**: 설명용 가정 사례. 근거: 무입찰 시 FailedToAssign(f1), dispatch errors 배열(f3), 최종 폴백의 사람 인계(f18), 불능 원인 설명과 수정 제안(f11).
- **f26**: 한국어 검색 2회는 해외 논문 번역 페이지와 통합관제 제품 소개만 나와 배정 실패 처리 절차를 담은 국내 자료를 찾지 못함.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://robot-help.github.io/ | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-352 | Park, J. 외(고려대학교·연세대학교·Google Research, CLARA 프로젝트) | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents — project page (clararobot.github.io) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://clararobot.github.io/ | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 아니오 |
| ref-598 | Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026) | LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.14138 | 예 |
| ref-713 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 아니오 |
| ref-714 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp | 아니오 |
| ref-039 | Open Robotics | Currently supported Tasks (task_types) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task_types.html | 아니오 |
| ref-716 | Rasa Technologies (RasaHQ/rasa GitHub) | Fallback and Human Handoff — Rasa documentation (docs/docs/fallback-handoff.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/fallback-handoff.mdx | 아니오 |
| ref-717 | Göbelbecker, M., Keller, T., Eyerich, P., Brenner, M., & Nebel, B. | Coming Up With Good Excuses: What to do When no Plan Can be Found | 2010 | 논문 | medium | 2026-09-25 | https://ojs.aaai.org/index.php/ICAPS/article/view/13421 | 예 |
| ref-718 | Sreedharan, S., Srivastava, S., Smith, D., & Kambhampati, S. | Why Couldn't You do that? Explaining Unsolvability of Classical Planning Problems in the Presence of Plan Advice | 2019-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1903.08218 | 예 |
| ref-719 | Chen, H. 외(OptiChat 저자) | Diagnosing Infeasible Optimization Problems Using Large Language Models | 2023-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2308.12923 | 예 |
| ref-720 | Schneider, E. 외(CE-MRS 저자) | CE-MRS: Contrastive Explanations for Multi-Robot Systems | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.08408 | 예 |
| ref-721 | Liang, K. 외(Introspective Planning 저자) | Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.06529 | 예 |
| ref-722 | Suri, M. 외(SAGE-Agent 저자) | Structured Uncertainty guided Clarification for LLM Agents | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.08798 | 예 |
| ref-723 | Shida, Y. 외 | Reinforcement Learning of Multi-robot Task Allocation for Multi-object Transportation with Infeasible Tasks | 2024-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2404.11817 | 예 |
| ref-724 | Kazmi, M. (plan-failure-bench GitHub) | plan-failure-bench — README (Benchmark measuring how LLM planners fail at robot tasks) | 미확인 | 오픈소스 문서 | low | 2026-09-25 | https://github.com/munawarkazmi/plan-failure-bench | 아니오 |
| ref-459 | W3C | Shapes Constraint Language (SHACL) | 2017-07 | 표준 | medium | 2026-09-25 | https://www.w3.org/TR/shacl/ | 아니오 |
| ref-041 | Scientific Reports 게재 논문(저자 미확인) | Ontology-driven integration of advertised and operational capabilities in robots | 2025 | 논문 | medium | 2026-09-25 | https://www.nature.com/articles/s41598-025-16649-3 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세. 주문 거절 오류 유형(INVALID_ORDER_ACTION, UNSUPPORTED_PARAMETER, MOBILE_ROBOT_NOT_AVAILABLE)과 관제 기능 범위를 확인.
- **ref-105**: 플릿 어댑터 템플릿 설정. task_capabilities(loop·delivery), recharge_threshold 0.10.
- **ref-111**: 작업 상태 스키마. dispatch 필드의 상태 값·배정 대상·오류 배열.
- **ref-125**: 작업 요청 스키마. 필수 category·description, 선택 fleet_name(허용 플릿 지정) 등.
- **ref-236**: 원문 미열람. 온톨로지 기반 실행 가능성 판정을 배정기 독립 ReasonerOutput 으로 정형화, 적재 상태·플릿 구성이 실행 가능성에 영향.
- **ref-350**: 원문 미열람. KnowNo 프로젝트 페이지. 등각 예측 기반 도움 요청.
- **ref-351**: 원문 미열람. KnowNo 논문(CoRL 2023).
- **ref-352**: 원문 미열람. CLARA 프로젝트 페이지. 명확·모호·수행 불가 명령 구분.
- **ref-353**: 원문 미열람. CLARA 논문(IEEE RA-L 2024).
- **ref-376**: Open-RMF 입찰 흐름(BidNotice·BidProposal·설정 기준 비교). 무입찰·실패 처리는 이 문서에 없음을 확인.
- **ref-598**: 원문 미열람. LLM 이 대화로 선호를 최적화 문제로 인스턴스화하고 해법기가 푸는 방식.
- **ref-713**: Open-RMF 디스패처 소스. 무입찰 시 FailedToAssign·오류 기록, 기본 평가기 QuickestFinishEvaluator 와 교체 메서드.
- **ref-714**: 입찰 경매자 헤더. 평가기 LeastFleetDiffCost·LeastFleetCost·QuickestFinish 정의(각 기준 문서화 없음).
- **ref-039**: 지원 작업 유형 문서. 플릿 어댑터가 해당 작업 유형을 받도록 설정되지 않으면 입찰하지 않는다고 설명.
- **ref-716**: NLU 폴백 문턱, 두 단계 폴백(의도 확인·재진술), 최종 폴백의 사람 인계 설명.
- **ref-717**: 원문 미열람. 계획을 찾지 못할 때 과제를 풀 수 있게 만드는 초기 상태의 반사실적 변경(excuse)을 찾는 형식화와 알고리즘(ICAPS 2010).
- **ref-718**: 원문 미열람. 사용자 제약이 원인이 되는 해결 불가를 계층적 추상화·랜드마크로 설명하는 방법.
- **ref-719**: 원문 미열람. GPT-4 와 해법기를 연결해 IIS 로 불능 원인을 찾고 수정 제안을 하는 대화형 시스템 OptiChat(INFOR 2024 게재).
- **ref-720**: 원문 미열람. 작업 배정·스케줄링·경로 계획 정보를 쓰는 다중 로봇 대조적 설명과 운영자 사용자 연구(IEEE 저널 게재).
- **ref-721**: 원문 미열람. 내성적 추론 예시 검색과 등각 예측 결합으로 불필요한 되묻기를 줄이는 LLM 계획(NeurIPS 2024).
- **ref-722**: 원문 미열람. 도구 인자 위의 구조화 불확실성과 EVPI 로 되물을 질문을 고르는 방법과 ClarifyBench(ACL 2026 Findings).
- **ref-723**: 원문 미열람. 운반 불가 작업이 교착을 부르는 문제와 작업별 배제 수준 학습으로 일시 배제하는 동적 배정(IEEE 학술대회 게재).
- **ref-724**: 개인 연구자 벤치마크 README. plan/infeasible/clarify 세 응답과 여섯 함정 유형, 기계 검증 정답. 동료심사 전 프리프린트.
- **ref-459**: SHACL 명세. 검증 보고(sh:conforms, sh:result)와 결과 속성 구조. 연 것은 W3C data-shapes 저장소의 편집자 초안이라 권고안과 문구가 다를 수 있음.
- **ref-041**: 원문 미열람. 제조사 광고 능력과 측정 운용 능력을 함께 표현하는 로봇 능력 온톨로지(RCO)와 SPARQL 비교 질의.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md | 2, 3, 4, 5, 6, 8, 9 | q3-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26 (신뢰도 low) — 2절 q3-03 상태 답함, 3절 q3-03 소제목 신설({#q3-03}): 오케스트레이션 도구의 무입찰·배정 실패 기록(f1·f2·f3), 후보 여럿일 때 평가기(f4)와 허용 플릿 지정(f5), 로봇 쪽 거절 오류의 능력 대 가용 구분(f6), 온톨로지 판정과 검증 보고(f7·f8·f21), 해결 불가 설명 연구(f9·f10·f11·f12), 실행 불가 작업 일시 배제(f13), 되묻기 기준(f14·f15·f16·f17·f18·f20), 세 응답 벤치마크(f19, 신뢰도 low), 종합: 후보 없음 원인 네 갈래와 되묻기 범위(f22)·후보 여럿일 때 자동 결정과 되묻기의 경계(f23, mermaid 판정 흐름 권장)·SCM 질문 연결(f24)·피킹 시나리오(f25)·근거 공백(f26) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 5 | 아이디어 페이지 5절(트랙 산출물): '온톨로지 질의 결과에 따른 되묻기' 소절 신설 — 후보 없음 원인 구분과 되묻기 범위 f22(추정), 후보 여럿일 때 자동 결정·되묻기 경계 f23(추정), 근거 f1·f3·f4·f6·f11·f15·f17·f18. 다른 아이디어와의 연결: 능력 판정 불일치의 원인(아이디어 1, 선언 대 운용 능력 f21), 장소 슬롯 변경 제안(아이디어 3)은 구조만 언급 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(개념 '배정 실패' 추가)가 승인되면 2절 반영과 초안 버전 인상(f1·f3·f6·f22). 미승인 시 6절 질문으로 두고, 배정 실패와 진행 상태의 dispatch 값 failed_to_assign 메모, 사용자 확인 개념(q4-01·q4-04)과의 관계를 질문으로 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f1, f4, f5, f13, f23, f24): Open-RMF 무입찰 시 배정 실패 처리, 입찰 평가기(가장 빨리 끝남 기본·교체 가능)와 분류 원문 질문 연결, 실행 불가 작업의 일시 배제. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md | 6 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f12, f16, f17, f18, f22): 배정 실패·후보 여럿일 때의 되묻기 범위, 폴백과 사람 인계, 불필요한 되묻기를 줄이는 방법, 다중 로봇 대조적 설명의 운영자 연구 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6, 8 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f11, f16, f17, f19): LLM 과 해법기 결합의 불능 원인 진단(OptiChat), 내성적 계획·EVPI 기반 되묻기, 계획 실패 유형 벤치마크(신뢰도 low). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결 |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 10 | 트랙 nl-task-chatbot 단계 3 반영 제안 (f7, f8, f21): 온톨로지 판정이 '후보 없음'의 원인을 제약 단위(SHACL 검증 보고 같은 형식)로 13. 작업 배정 — MRTA 에 돌려주는 연결과 선언·운용 능력 차이(oq-024 관련) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 대조적 설명 | Contrastive Explanation | 시스템이 왜 다른 선택(예: 다른 로봇·다른 일정)이 아니라 이 선택을 했는지를 대안과 비교해 설명하는 방식으로, 사용자가 명세 오류를 찾는 데 쓰인다. |
| 기약 불능 제약 집합 | Irreducible Infeasible Subset (IIS) | 최적화 모델을 실행 불가능하게 만드는 제약 가운데, 어느 하나라도 빼면 실행 가능해지는 최소 제약 묶음으로, 불능 원인을 사람에게 보여 주는 데 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 로봇 관제가 배정 실패(수행 가능한 로봇·플릿 없음)를 WMS 등 상위 업무 시스템에 어떤 필드로 되돌리고, 상위 시스템이 이를 사람 작업 지시로 전환하는 표준이나 국내 물류센터 사례가 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 1. 주문·업무 시스템 연계 | 근거: f1 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 25 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 도구 동작은 단일 공식 저장소(Open Robotics 계열 파일끼리는 독립 아님), 연구는 단일 논문 검색 요약
    - f9~f13·f16·f17·f21 원문 미열람(검색 요약 범위), f17 수치는 저자 보고값
    - f4 평가기 LeastFleetCost·LeastFleetDiffCost 의 순위 기준은 헤더에 문서화가 없어 미확인
    - f7 ReasonerOutput 이 불가 사유를 필드로 담는지 미확인
    - f8 은 W3C data-shapes 저장소의 편집자 초안을 열어 확인했으며 2017-07 권고안 문구와의 일치는 미확인
    - f19 Plan-Failure-Bench 는 개인 연구자·동료심사 전 자료이고 평가 모델명 등 수치는 넣지 않음
    - ref-719·ref-720·ref-721·ref-722·ref-041 저자 목록 전체 미확인
    - f22~f25 는 이 위키의 종합이며 후보 없음·후보 여럿 처리를 한 번에 제시한 단일 출처는 찾지 못함
    - f26 물류 관제 배정 실패 대화 처리 연구·국내 사례의 부재는 검색 범위 관찰이며 부재 확인 아님
- 범위 경계 위반 의심:
    - f6: VDA 5050 주문 거절은 로봇 쪽 기능이며, ROP 는 거절 오류를 받아 원인을 구분·설명하는 관제 쪽 역할만 판단하도록 서술
    - f13: 무게를 모르는 물체 운반의 학습 배정은 로봇 파지·운반 능력(로봇 자체 지능·제어)과 맞닿아 배제 규칙 사례로만 씀
    - f25: 사람 작업자 처리 전환은 18. 사람–로봇 협업·운영 인터페이스의 운영 선택지로만 다루고 작업자 관리 정책은 서술하지 않음
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 신규 ref-713(Dispatcher.cpp)·ref-714(Auctioneer.hpp)·ref-039(task_types.md)·ref-716(Rasa 폴백 문서)·ref-724(Plan-Failure-Bench README)·ref-459(SHACL 편집자 초안), 재사용 ref-376(task.md)·ref-111·ref-125·ref-105. ref-031 은 입력 원문 텍스트(inbox). introplan.github.io 는 프록시가 거부. 나머지 신규 8건과 재사용 6건은 원문 미열람이라 신뢰도 상한 medium. 원문을 연 출처도 공통 규칙 0절 6항에 따라 high 를 주지 않음. 검색 17회/40, 신규 출처 14건/20(ref-713~ref-041, 예약 구간 안), 재사용 11건. 질문 선택: target.json 지정 q3-03 1건. q3-03 은 도구 동작(사실)과 해결 불가 설명·되묻기 연구(사실)로 답했으나, 후보 없음 원인 네 갈래와 되묻기 범위(f22)·후보 여럿일 때 자동 결정 경계(f23)는 이 위키의 종합이고 근거가 물류 플릿 조건이 아니라 질문 종합 신뢰도를 low 로 둠. 한국 자료: 한국어 검색 2회는 해외 논문 번역 페이지와 통합관제 제품 소개만 나와 finding 으로 쓰지 않음(국내 CLARA 는 재사용 ref-352·ref-353). 교차 규칙: LLM 되묻기·불능 진단 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스 양쪽에 반영 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 새 일반 열린 질문 1건(배정 실패의 상위 시스템 반환). 용어 후보: 트랙 glossary_targets 는 모두 용어집에 있어 finding 근거 용어 2건을 냄. 후속 질문 3건, 온톨로지 변경 제안 1건. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 4건(갱신 상한과 별도). 백로그 참고: q3-12·q3-13, q4-09·q4-10, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06 이 중복 등록되어 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 3
- 답한 질문 id: q3-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 배정 실패 원인(능력 부재·일시적 가용 불가·제약 조합 불능·해석 오류)마다 챗봇이 사용자에게 제시할 완화 선택지(기한 완화, 장소·대상 변경, 사람 작업자 처리 전환, 대기)를 어떤 목록으로 두고, 사람 처리 전환이나 기한 완화는 누가 승인하는가? (q3-03 에서 파생) | 4 | f22 |
| — | 온톨로지 기반 실행 가능성 판정이 후보를 하나도 내지 않을 때, 어느 능력·제약 때문인지를 SHACL 검증 보고처럼 제약 단위로 돌려주는 형식을 배정기 독립 출력(ReasonerOutput)에 둘 수 있는가, 그 형식에서 챗봇이 사용자에게 보여 줄 설명을 만들 수 있는가? (q3-03 에서 파생) | 3 | f8 |
| — | 후보가 여럿일 때 '시스템이 계산할 수 있는 차이는 자동 결정, 사용자만 아는 정보에 걸린 차이만 되묻기' 규칙을 물류 지시 시나리오에 적용하면 되묻기 횟수와 오배정은 모든 경우를 묻거나 묻지 않는 방식에 비해 어떻게 달라지는가? (q3-03 에서 파생) | 5 | f23 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| add | concept | 배정 실패 (Assignment Failure) | f1, f3, f6, f22 | 작업에 수행 가능한 로봇·플릿을 찾지 못한 결과. 주요 속성: 사유 유형(값 후보: 능력 부재 / 일시적 가용 불가 / 제약 조합 불능 / 해석 오류 — 분류는 f22 추정), 오류 기록 원천(Open-RMF dispatch 의 failed_to_assign·errors, VDA 5050 INVALID_ORDER_ACTION·MOBILE_ROBOT_NOT_AVAILABLE 등), 사용자에게 제시한 대안과 응답. 진행 상태 개념의 외부 표현 메모(dispatch 값 failed_to_assign)와 겹칠 수 있어, 별도 개념으로 둘지 진행 상태·배정의 속성으로 둘지는 검증이 판단한다. 사유 유형 값은 추정 근거라 확정 전에는 후보로만 둔다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 아이디어 2. 자연어 업무 지시 챗봇 5절에 다른 아이디어와의 연결이 아직 없음(이번 제안은 구조 언급 수준)
    - 사용자에게 제안하는 실험 계획이 실험 페이지에 없음
    - 열린 질문 q3-04~q3-13(q3-09·q3-10, q3-12·q3-13 중복 정리 필요)
