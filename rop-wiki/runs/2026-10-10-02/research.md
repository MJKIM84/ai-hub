# 리서치 브리프 2026-10-10-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-02 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 25. 작업 배정 — MRTA |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 가상 시나리오뿐이고, 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인'(oq-054)이 남아 있음. 운영 중 도착하는 작업과 용량·마감을 함께 다룬 다른 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 문헌 검토(ref-152)의 계열 구분·실험 플릿 규모가 '미확인'으로 남아 있고, LTAA(ref-168) 비교 결과가 출처 충돌(oq-030)로 11절에 미뤄져 있음. rmf_task TaskPlanner 최적 배정의 적용 범위(한 플릿)가 명시되지 않음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — Open-RMF 입찰(BidProposal)이 담는 필드가 구체적으로 적혀 있지 않고, 2026-09-26 rmf_fleet_adapter 2.14.0 의 플릿 이름 필터 수정이 반영되지 않음(바뀐 출처)
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 2024~2026 연구(마감 제약 SMT 배정, 혼잡 환경 재분배 배정 MRTA-RM, 최소 비용 흐름 기반 대규모 배정) 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 두 수준 배정에서 제조사 관제가 내야 할 비용·상태 정보(oq-053)가 미확인으로 남아 있음
- 섹션 11. 열린 질문(주제 페이지로 분리) — oq-030·oq-053·oq-054 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. oq-030 LTAA(arXiv 2512.02810) 원문은 LLM 배정과 동적 계획법·강화학습의 성공률을 어떤 조건에서 비교했고, 초록의 '전통 기법을 모두 앞섰다'는 표현은 본문 수치와 맞는가? (섹션 6·11 겨냥)
3. oq-053 ROP 가 플릿 단위로 배정하고 제조사 관제가 플릿 안에서 로봇을 고르는 두 수준 배정에서 제조사 관제는 어떤 비용·상태 정보를 내며, 한 플릿 안의 최적 배정은 어디까지 보장되는가? (섹션 6·7·9·11 겨냥)
4. oq-054 출하 마감·납기 같은 상위 업무 제약을 배정과 결합하는 공개 설계가 있는가? (섹션 5·6·11 겨냥)
5. 이동로봇 플릿 작업 배정 문헌 검토(2025-01)는 방법을 어떤 계열로 나누고 실험 플릿 규모를 어떻게 보고하는가? (섹션 6 겨냥)
6. 배정 비용에 환경 구조·혼잡을 반영해 대규모로 배정하는 최근(2024~2026) 연구와 공개 구현은 무엇이며, 그 결과는 어떤 조건의 실험인가? (섹션 6·8 겨냥)
7. 바뀐 출처: Open-RMF rmf_fleet_adapter 의 입찰 동작은 최근 판에서 어떻게 바뀌었는가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Meseguer Valenzuela·Blanes Noguera 의 2025 년 문헌 검토는 이동로봇 플릿의 다중 로봇 작업 배정(Multi-Robot Task Allocation, MRTA) 방법을 휴리스틱, 메타휴리스틱, 정확·수리 휴리스틱(matheuristic), 시장 기반, 인공지능 기반의 다섯 계열로 정리한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f2 | [사실] | 같은 문헌 검토의 표 I~V 는 계열별로 각 연구의 방법, 중앙·분산 구조, 구현 환경(프레임워크), 플릿 규모, 주요 결과를 함께 제시한다. | ref-152 | 아니오 | medium | 2025-01 | — | — |
| f3 | [의견] | 문헌 검토의 본문 설명과 표의 플릿 규모 값이 서로 달라, 검토된 연구의 최대 플릿 규모나 계열 간 우열을 하나의 수치로 요약하지 않는 편이 좋다. | ref-152 | 아니오 | low | 2025-01 | — | — |
| f4 | [사실] | LTAA 원문(Kaitha·Yu, 2025-12 프리프린트)의 그림 15 비교는 TEACh 데이터셋의 건설 작업에서 전체 성공률을 LTAA 75.97%, Q-learning 73%, DQN 77% 로 보고하며, 초록은 LTAA 값을 76% 로 반올림해 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f5 | [사실] | 같은 원문 p.61 은 결정적 비교군의 성공률을 brute force 0.77, greedy 0.81, 동적 계획법(Dynamic Programming, DP) 0.95 로 적고, 이 결정적 알고리즘들은 불확실성 모델이 없어 비교 그림에서 제외했으며 확률적 조건의 직접 비교 기준은 강화학습이라고 설명한다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f6 | [사실] | LTAA 원문 초록은 로봇 전문화가 뚜렷한 Heavy Excels 설정에서 LTAA 가 77% 완료율과 더 나은 작업 부하 균형으로 전통 기법을 모두 앞섰다고 쓰고, 결론(p.62)은 이 설정의 성공률을 77.1% 로 적는다. | ref-168 | 아니오 | medium | 2025-12-02 | — | — |
| f7 | [의견] | f4~f6 을 함께 보면 원문에는 LTAA 전체 75.97%, Heavy Excels 77.1%, DP 95% 가 모두 있으나 DP 는 불확실성 모델 차이로 비교에서 빠졌으므로, 'LTAA 가 전통 배정법 전체보다 우수하다'는 결론은 지지되지 않으며 같은 조건의 LLM 대 DP 우열은 확정할 수 없고, Heavy Excels 결과와 전체 비교 결과는 분리해 적어야 한다(oq-030 부분 해소). | ref-168 | 아니오 | low | 2025-12-02 | — | — |
| f8 | [사실] | Open-RMF 의 입찰 제안 메시지 BidProposal.msg 는 입찰 공고(BidNotice)에 답해 플릿 어댑터가 내는 것으로, 플릿 이름(fleet_name), 작업을 수행할 것으로 예상되는 로봇 이름(expected_robot_name), 새 작업 수용 전·후의 전체 배정 비용(prev_cost·new_cost), 새 작업의 예상 완료 시각(finish_time) 다섯 필드를 담는다. | ref-1453 | 아니오 | medium | 2026-10-10 | — | — |
| f9 | [추정] | BidProposal 의 필드(f8)는 두 수준 배정에서 제조사 관제(플릿)가 공개하는 비용·상태 정보의 구체적인 예이지만, 이 메시지는 각 플릿이 자기 안에서 계산한 비용만 전하므로 이것만으로 모든 플릿을 합친 최적 배정이 보장되지는 않으며, 이종 플릿의 최적성 손실을 수치로 제한하는 근거는 확인하지 못했다(oq-053 부분 근거). | ref-1453, ref-404 | 아니오 | low | 2026-10-10 | — | — |
| f10 | [사실] | Open-RMF rmf_task README 는 작업 계획기(TaskPlanner)의 최적 배정을 물리·운동 특성을 공유하는 한 플릿에 속한 로봇과 주어진 작업 집합에 대해, 요청된 시작 시각을 고려해 작업이 가장 짧은 시간에 끝나도록 순서를 정하는 문제로 설명한다. | ref-404 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | TaskPlanner 의 '최적 배정'(f10)은 한 플릿의 주어진 작업 집합에 한정되므로, 앞으로 들어올 작업, 다른 제조사 관제의 내부 결정, 실제 혼잡까지 포함한 운영 전체의 전역 최적성으로 넓혀 해석해서는 안 된다. | ref-404, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [사실] | Tuck 외(2024, NFM 2024 게재 예정 프리프린트)는 이론 모듈로 만족 가능성(Satisfiability Modulo Theories, SMT) 풀이를 써서, 온라인으로 도착하는 픽업·배송 작업의 배정, 로봇의 동시 적재 용량, 엄격한 마감 준수를 함께 제약식으로 표현하고 점진(incremental) 풀이로 새 작업을 배정한다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f13 | [사실] | Tuck 외 방법의 목표는 주어진 모델에서 제약을 모두 만족하는 계획을 찾는 것이고 최소 이동 비용의 전역 최적해를 찾는 것과는 구별되며, 저자들은 알고리즘이 건전·완전하다고 증명하지만 이는 논문의 모델·인코딩 조건 안의 결과이고 국소 경로 계획·충돌 회피는 하위 계획기에 맡긴다. | ref-1454 | 아니오 | medium | 2024-03-18 | — | — |
| f14 | [의견] | 납기·마감 준수가 필수인 작업은 높은 우선순위 점수만 주는 방식과 별도로, 마감을 필수 제약으로 두는 정식화(f12)를 검토할 필요가 있으나, 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못했다(oq-054 부분 근거). | ref-1454 | 아니오 | low | 2024-03-18 | 제약 | — |
| f15 | [사실] | Tuck 외는 병원과 유사한 공간을 그래프(노드=구역, 가중치=최악 이동 시간)로 추상화한 다중 로봇 배송 벤치마크 200개(작업 10~30개, 로봇 5~20대, 최대 용량 2 또는 3, 마감 균등 분포)에서 용량 제한 로봇의 동적 작업 배정을 평가했다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 수행 자원 | — |
| f16 | [사실] | Tuck 외의 병원 모사 배송 문제에서 각 요청은 출발·도착 위치와 발생·마감 시각을 가지며, 새 요청이 들어오면 이미 실행한 동작과 현재 동작은 유지한 채 계획을 갱신한다. | ref-1454 | 아니오 | medium | 2024-03-18 | 병원 / 시작 조건 | — |
| f17 | [의견] | Tuck 외 연구는 병원 배송의 계산 실험 사례이며 병원 현장 실증으로 분류해서는 안 된다. | ref-1454 | 아니오 | low | 2024-03-18 | 병원 / 예외·성과 | — |
| f18 | [사실] | Lee·Sim·Nam 의 MRTA-RM 은 장애물이 밀집하고 통로가 좁은 환경에서 일반화 보로노이 다이어그램(GVD)으로 로드맵을 만들고 이를 여러 구역으로 나눈 뒤 구역 사이에 로봇을 재분배하고 작업을 배정해, 충돌·교착을 줄이면서 전체 완료 시간(makespan)을 줄이려 한다. | ref-1455 | 아니오 | medium | 2025-06-08 | — | — |
| f19 | [사실] | MRTA-RM 저자들은 수백 대 규모 로봇의 동적 시뮬레이션 결과(무작위 시나리오 성공률 96% 초과, 분리 시나리오 58~100%)를 보고하고 Python 구현을 공개했으며, 결론에서 성공률 100% 달성(경로 추종 제어기)과 이종 로봇 팀 확장을 후속 과제로 남겼다. | ref-1455, ref-1456 | 아니오 | medium | 2025-06-08 | — | — |
| f20 | [의견] | MRTA-RM 은 혼잡을 줄이는 배정의 재현 후보로 볼 수 있지만, 임의 환경에서 교착이 없다는 보장으로 소개해서는 안 된다. | ref-1455 | 아니오 | low | 2025-06-08 | — | — |
| f21 | [사실] | Zhang 외의 AAMAS 2026 연구는 온라인 다중 에이전트 픽업·배송의 작업 배정을 환경 그래프 위의 최소 비용 흐름(Minimum-Cost Flow) 문제로 풀어, 선형 배정 방식이 요구하는 로봇·작업 사이 모든 쌍의 거리 행렬 계산을 피한다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f22 | [사실] | Zhang 외는 격자 지도 벤치마크(창고형 Sortation Large 포함)에서 1초 계획 예산으로 최대 20,000 에이전트와 30,000 작업까지 다뤘다고 보고하며, 이는 실제 로봇 배치가 아니라 계산 실험이다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f23 | [사실] | Zhang 외의 흐름 정식화는 기본 간선 비용으로 단위 비용을 쓰고, 선택할 수 있는 대체 비용 모델로 경로 계획기의 혼잡 추정치나 실행 중 평균 대기 시간을 배정 비용에 반영할 수 있으며, 계획기와의 결합은 6절에서 다룬다. | ref-1457 | 아니오 | medium | 2026-05 | — | — |
| f24 | [추정] | MRTA-RM(f18)과 Zhang 외(f21~f23)를 함께 보면 배정 비용에 환경 구조와 혼잡을 반영하는 연구 흐름은 확인되지만, 두 방법은 환경·규모·지표가 달라 성능 수치를 같은 조건의 순위로 비교할 수 없는 것으로 보인다. | ref-1455, ref-1457 | 아니오 | low | 2026-10-10 | — | — |
| f25 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 작업 요청에 지정된 플릿 이름이 문자열 또는 배열에 포함되기만 하면 입찰하도록 한 수정(#534)을 기록한다. | ref-1398 | 아니오 | medium | 2026-09-26 | — | — |
| f26 | [의견] | 요청에 후보 플릿을 제한하는 배정 사례를 적을 때는 #534 수정이 포함된 rmf_fleet_adapter 패키지 버전(2.14.0 이상)을 함께 적는 편이 좋으며, 이 변경이 모든 배포판에 자동 반영되었다는 뜻은 아니다. | ref-1398 | 아니오 | low | 2026-09-26 | — | — |

### 근거 발췌

- **f1**: PDF §II Algorithms 의 소절 A. Heuristics, B. Meta-heuristics, C. Exact and matheuristic Methods, D. Market-based Approach (MBA), E. Artificial Intelligence (AI). 기존 6절 문장의 '계열 구분 미확인'을 채운다
- **f2**: §III Simulations 표 I~V 의 열: Method / Centralized / Decentralized / Framework / Fleet Size / Remarkable results. 총 검토 편수는 선정·제외 절차가 원문에 없어 새 수치로 내지 않음
- **f3**: §III 본문: 휴리스틱 연구의 시뮬레이션은 'up to 25 robots'(예외 Shi 외 2024 는 이동 랙 1,923개로 로봇 수가 아님). 그러나 표 I 의 L. Li 외 행은 최대 45 AMR, 표 IV(시장 기반)의 Teck 외 2023 행은 3~48 AMR 을 적는다. 표 I 페이지 렌더 확인
- **f4**: pp.57–58 그림 15 'Task Allocation Methods Comparison' 본문: "overall success rate of 75.97%, positioning it between Q-learning (73%) and DQN (77%)". 초록: 76% task completion rate. 논문의 실험·모델 보고값이며 건설 현장 실측 완료율이 아님
- **f5**: p.61(이미지 렌더 확인): 'Brute force, greedy, and DP obtained success rates of 0.77, 0.81, and 0.95. However, they are omitted from the comparison plots because these deterministic algorithms lack uncertainty modeling.' oq-030 관련
- **f6**: 초록: 'In the Heavy Excels configuration ... reaches 77% completion with superior workload balance, exceeding all traditional methods.' p.62 결론: Heavy Excels setting (77.1% success with balanced workloads). 초록의 포괄적 우위 표현과 p.61 의 DP 제외 설명이 함께 있음
- **f7**: f4·f5·f6 에서 도출. 기존 oq-030 의 두 요약은 각각 초록(Heavy Excels 우위)과 본문 p.61(DP 0.95)을 전한 것으로 보임. 결정적·확률적 비교군을 같은 조건으로 재평가한 자료는 원문에 없음
- **f8**: rmf_task_msgs/msg/BidProposal.msg 전체 필드 5개: string fleet_name, string expected_robot_name, float64 prev_cost, float64 new_cost, builtin_interfaces/Time finish_time. 검증 시 BidResponse.msg 안에 담겨 쓰이는 것을 확인 (발행일 미확인, 확인일 기준)
- **f9**: f8 의 prev_cost·new_cost 는 '플릿의 전체 배정 비용'이고 rmf_task README 는 계획기 대상을 한 플릿으로 둠(f10). BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님
- **f10**: README: "For a given collection of tasks and robots belonging to a fleet (ie, they share physical and kinematic traits), the planner determines the best ordering of tasks across robots". 배터리 제약과 충전 작업 삽입도 포함 (발행일 미확인, 확인일 기준)
- **f11**: f10 과 Zhang 외 AAMAS 2026 §5 에서 도출: 선형 배정은 '최적 단발(one-shot) 배정'을 주지만 단위 이동 비용과 혼잡(traffic) 비용이 다르고(§5, §5.3), 장기 처리량은 §7.2 에서 따로 평가. 서로 다른 연구팀 자료를 대조한 범위 한정
- **f12**: §1: 작업은 온라인 생성·엄격한 마감·로봇 1대 필요, 로봇 동시 작업 수 제한. §3.2 과업 튜플(출발·도착 위치 id, 도착 시각, 마감), 용량 K_n. Definition 6: 하차가 마감 전이어야 완료. §4.3 점진 풀이. arXiv comment: NFM 2024 게재 예정
- **f13**: §1: 'even satisfying solutions without guaranteed optimality are relevant for this application', 국소 운동 계획·충돌 회피는 downstream planners 몫. §5 건전성(Thm 5.1)·완전성(D=D_max 가정, 사용 솔버의 건전·완전 가정)
- **f14**: f12·f13 에서 도출. 원문은 마감을 Definition 6 의 완료 조건으로 강제하고 2절에서 휴리스틱 방법이 엄격한 마감의 완전성 보장을 못 한다고 지적. 병원 모사 환경 연구이며 창고 출하 마감 사례는 아님
- **f15**: 초록: 'benchmarks encoding multi-robot delivery created from a graph abstraction of a hospital-like environment'. §1 그래프 추상화, §6 실험: 200 benchmarks, tasks 10–30, agents 5–20, capacity c=2·3. 병원 모사 계산 실험
- **f16**: §3.2 과업 m=(id, 시작 위치, 종료 위치, 도착 시각 t_m, 마감 T_m). Definition 9 갱신 계획: 'past actions and the current action are unchanged', 계획 갱신은 시스템 위치에서만
- **f17**: f15·f16 에서 도출. 원문은 그래프 추상화 벤치마크의 솔버 성능(풀이 수·시간)을 보고하고 실제 병원·로봇 운행 결과는 없음
- **f18**: 초록: 'considers the paths of the robots to avoid collisions and deadlocks ... constructs a roadmap using a Generalized Voronoi Diagram ... partitions the roadmap into several components'. 충돌 없는 경로를 직접 찾지 않고 충돌 가능성이 낮은 배정을 찾음
- **f19**: 본문 실험 절: 'high success rates exceeding 96% in the random scenario', 'separated scenario ... 58 to 100%'. §6 Conclusion: 'we will achieve 100% of the success rate by implementing a controller', 이종 로봇 확장 계획. README: Python 3.9+, MIT, RAS 2025-12 표기. 논문과 코드는 같은 팀 산출물
- **f20**: 본문: 'our method cannot achieve deadlock-free as our research aims to find a task allocation that is likely to prevent deadlocks'. 분리 시나리오 성공률 58% 사례 존재(f19)
- **f21**: §2 문제 정의, §5 흐름 정식화(격자 각 칸을 노드로, 더미 source·sink), §5.3.2 Network Flow: 명시적 에이전트–작업 쌍 거리 계산 회피. 초록: 'eliminates the need for pairwise distance' 행렬. DOI 10.65109/MQIK8423
- **f22**: 초록: 'scales to 20,000 agents and 30,000 tasks within 1-second planning' 시간. §7(§7.1 실행 시간, §7.2 처리량)·표 1: Sortation Large 20,000 에이전트 행. 단일 시점 배정 최적성과 장기 처리량은 §7.2 에서 따로 평가
- **f23**: §5: 기본은 지도 간선 비용(격자는 unit cost), 대체로 Traffic(계획기 혼잡 추정)·Avg Waiting Time 비용 모델. §6: 계획기의 FCost 로 간선 비용 설정(Algorithm 2). 표 1 열 Flow-Unit Cost / Flow-Traffic / Flow-Avg Waiting
- **f24**: MRTA-RM: 연속 공간 GVD 로드맵·동적 시뮬레이션 성공률·makespan. Zhang 외: 격자 MAPD 벤치마크·처리량·1초 예산. 공통 벤치마크 비교 없음
- **f25**: rmf_ros2 2.14.0 태그 rmf_fleet_adapter/CHANGELOG.rst '2.14.0 (2026-09-26)': 'Submit bid as long as fleet name exists (in string or array) (#534)'. FleetUpdateHandle.cpp 의 fleet_name 문자열·배열 검사 코드와 일치
- **f26**: f25 에서 도출. 변경 이력은 패키지 태그 기준이며 ROS 배포판별 반영 시점은 확인하지 않음

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2501.08726 | 아니오 |
| ref-168 | Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12-02 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2512.02810 | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_task | 아니오 |
| ref-1453 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg | 아니오 |
| ref-1454 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정) | SMT-Based Dynamic Multi-Robot Task Allocation | 2024-03-18 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2403.11737v1 | 아니오 |
| ref-1455 | Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293) | Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution | 2025-06-08 | 논문 | medium | 2026-10-10 | https://arxiv.org/html/2506.07293 | 아니오 |
| ref-1456 | Lee, S. 외 (SeBin-Lee-SG GitHub) | MRTA-RM_public — README | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/SeBin-Lee-SG/MRTA-RM_public | 아니오 |
| ref-1457 | Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS) | Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery | 2026-05 | 논문 | high | 2026-10-10 | https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf | 아니오 |
| ref-1398 | Open Robotics (open-rmf/rmf_ros2) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |

### 출처 요약

- **ref-152**: 이동로봇 플릿 작업 배정 방법을 휴리스틱·메타휴리스틱·정확·수리 휴리스틱·시장 기반·인공지능 기반의 다섯 계열로 나누고 표 I~V 로 각 연구의 구조·구현 환경·플릿 규모·결과를 정리한 리뷰 프리프린트(arXiv 2025-01-15). 이번에 PDF 원문을 열어 확인했다.
- **ref-168**: LangGraph 기반 LLM 작업 배정 에이전트(LTAA)를 건설 작업(TEACh)에서 DP·Q-learning·DQN 과 비교한 프리프린트. 이번에 v1 PDF 원문을 열어 그림 15·p.61·결론을 확인했다. 기존 ref-168 의 저자 표기 'Yu, S.' 정정: Hongrui Yu(저자: Shyam prasad reddy Kaitha, Hongrui Yu). 발행일은 arXiv 2025-12-02(PDF 하단의 2025-12-01 표기와 다름).
- **ref-404**: 로봇 간 최적 작업 배정·순서를 푸는 TaskPlanner API 와 배터리 제약에 따른 충전 작업 자동 삽입을 설명한 README. 이번에 계획기 대상이 한 플릿의 로봇·작업 집합임을 원문으로 다시 확인했다.
- **ref-1453**: 플릿 어댑터가 입찰 공고(BidNotice)에 답해 내는 입찰 제안 메시지 정의. 플릿 이름·예상 수행 로봇·수용 전후 전체 배정 비용·예상 완료 시각 다섯 필드를 담는다.
- **ref-1454**: 온라인으로 도착하는 마감 있는 픽업·배송 작업을 용량 제한 로봇에 배정하는 문제를 SMT 로 인코딩하고 건전성·완전성을 증명한 뒤 병원 모사 그래프 벤치마크로 평가한 논문(arXiv comment: NFM 2024 게재 예정).
- **ref-1455**: GVD 로드맵을 구역으로 나누고 구역 사이 로봇 재분배 후 작업을 배정해 밀집 환경의 충돌·교착을 줄이는 대규모 배정 방법(MRTA-RM)과 수백 대 동적 시뮬레이션 결과. arXiv 초판 2025-06-08, 저자 README 는 RAS 2025-12 게재를 표기.
- **ref-1456**: MRTA-RM 저자 공개 구현의 README. 로드맵·구역 단위 배정 구조와 Python 실행 안내, RAS 2025-12 게재 표기를 담는다. 논문과 같은 팀 산출물이다.
- **ref-1457**: 온라인 MAPD 의 작업 배정을 환경 그래프 위 최소 비용 흐름으로 풀어 모든 쌍 거리 행렬을 피하고, 선택적으로 계획기 혼잡 비용을 반영해 최대 20,000 에이전트·30,000 작업을 1초 예산으로 다룬 AAMAS 2026(2026-05-25~29, Paphos) 논문. DOI 10.65109/MQIK8423.
- **ref-1398**: rmf_fleet_adapter 패키지의 판별 변경 이력. 2.14.0(2026-09-26)에 요청의 플릿 이름이 문자열 또는 배열에 있으면 입찰하도록 한 수정 #534 가 기록되어 있다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-allocation-mrta.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 병원 모사 환경의 동적 배정 계산 실험 사례 추가(f15 수행 자원·f16 시작 조건·f17 현장 실증 아님 표시), 물류창고 표 제약 행의 '출하 마감 결합 미확인'에 마감 필수 제약 정식화 근거 보충(f12·f14) / 섹션 6(주제 페이지 2026-09-25-area13-s6 반영) — 문헌 검토 문장의 '미확인'을 계열 구분·표 구성으로 교체(f1·f2)하고 최대 규모를 한 수치로 요약하지 않음(f3), LTAA 문장을 원문 수치로 교체(f4·f5·f6·f7: 전체 75.97%·Heavy Excels 77.1%·결정적 비교군 brute force 0.77·greedy 0.81·DP 0.95 의 비교 제외), TaskPlanner 최적 배정의 범위 한정(f10·f11), SMT 기반 마감·용량 배정(f12·f13) / 섹션 7(주제 페이지 s7 반영) — BidProposal 다섯 필드(f8), 메시지만으로 전 플릿 최적이 보장되지 않음(f9), rmf_fleet_adapter 2.14.0 #534(f25·f26) / 섹션 8(주제 페이지 s8 반영) — Tuck 외 2024(f12·f13), MRTA-RM(f18·f19·f20), Zhang 외 AAMAS 2026(f21·f22·f23), 두 연구 비교 한계(f24) / 섹션 9 — 두 수준 배정에서 제조사 관제가 내는 정보의 예와 한계(f8·f9·f10·f11) / 섹션 11(주제 페이지 s11 반영) — oq-030 부분 해소(f4~f7, 출처 충돌의 원인: 초록과 본문 p.61 의 서로 다른 비교 조건), oq-053 부분 근거(f8·f9·f11), oq-054 부분 근거(f12·f14), 새 질문 4건. 참고문헌 ref-168 저자 표기 정정(Yu, S. → Yu, H.; Hongrui Yu)과 ref-152·ref-168 원문 열람 반영. 기존 내용 확인: Open-RMF 입찰이 비용을 담는다는 문장(s7, ref-376)과 TaskPlanner 의 배정·충전 삽입 문장(s6, ref-404)은 이미 있으므로 중복하지 않고 세부(필드·범위)만 더한다. 다음 실행 후보: 20. 로봇·제조사 관제 연동(f8·f9·f25), 27. 다중 로봇 경로·교통 관리 — MAPF(f18·f21~f24), 47. AI·학습·적응과 모델 운영(f4~f7). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 최소 비용 흐름 | Minimum-Cost Flow | 간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다. |
| 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? | 관련 영역: 25. 작업 배정 — MRTA, 20. 로봇·제조사 관제 연동 | 근거: f8 | 종류: 일반
- LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? | 관련 영역: 25. 작업 배정 — MRTA, 47. AI·학습·적응과 모델 운영 | 근거: f5 | 종류: 일반
- 최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가? | 관련 영역: 25. 작업 배정 — MRTA, 28. 공용 자원·충전·에너지 최적화 | 근거: f21 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 9 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-02/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - f1~f3: 문헌 검토의 총 검토 편수는 선정·제외 절차가 원문에 없어 확인하지 못함
    - f4~f7: LTAA 결정적·확률적 비교군을 같은 조건으로 비교한 결과는 원문에 없음(oq-030 은 부분 해소에 그침). 초록의 '전통 기법 모두 우위' 표현과 p.61 의 DP 제외 설명의 불일치는 저자 설명이 없음
    - f8·f9: BidProposal 과 rmf_task README 는 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님. 이종 플릿 두 수준 배정의 최적성 손실을 수치로 제한하는 근거는 찾지 못함(oq-053 미해결)
    - f12: NFM 2024 게재 예정 표기는 arXiv comment 기준이며 게재본(쪽·DOI)은 확인하지 않음
    - f14: 출하 마감을 배정에 연동한 창고 현장 사례는 확인하지 못함(oq-054 미해결)
    - f19: MRTA-RM 논문과 공개 구현은 같은 팀 산출물이라 독립 재현 근거가 아님. RAS 게재본은 README 표기로만 확인
    - f25·f26: #534 수정이 ROS 배포판별 바이너리에 언제 반영되었는지는 확인하지 않음
    - 모든 사실 finding 은 단일 출처라 교차 확인 0건
- 범위 경계 위반 의심:
    - f13: 국소 경로 계획·충돌 회피는 로봇 자체 지능·제어(연계 대상) 몫이며, 원문도 하위 계획기에 맡긴다고 밝혀 배정 범위만 다룸
    - f18~f24: 경로 충돌·교착·혼잡 비용은 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 배정 비용에 반영하는 부분만 이 영역에 쓰고 경로 계획 자체는 27 에 연결
    - f4~f7: LLM 기반 배정은 교차 규칙상 47. AI·학습·적응과 모델 운영의 연구 방법이 이 영역에 적용된 것으로 양쪽에 연결
    - f15~f17: 병원 모사 환경의 계산 실험이므로 site_type 병원은 '모사 환경'으로 명시하고 현장 실증으로 쓰지 않음
- 한계: 외부 조사 변환이라 검색 횟수 집계 없음(queries 0 은 미집계 표시). 신규 출처 6건(ref-1453~ref-1398, 예약 구간 ref-1453~ref-1482 안), 재사용 3건(ref-152 리뷰 논문·ref-168 LTAA·ref-404 rmf_task README, 모두 이번에 원문 열람). 원문 열람 9/9. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·6·7·8·9·11절)과 바뀐 출처(rmf_fleet_adapter 2.14.0)만 다뤘다. 검증 수정 반영: Zhang 외 절 번호(§2 문제 정의, §5 흐름 정식화·§5.3.2 거리 행렬 회피, §6 계획기 결합, §7·§7.2·표 1 실험)와 혼잡 비용을 '선택할 수 있는 대체 비용 모델'로 범위 한정(f21~f23), LTAA p.61 의 brute force 0.77·greedy 0.81·DP 0.95 병기와 초록 76% 반올림·arXiv 2025-12-02·저자 Hongrui Yu 정정(f4~f6, ref-168), 리뷰 본문 25대·표 I 45 AMR·표 IV 48 AMR 을 의견 근거에 병기(f3), Tuck 외 NFM 2024 게재 예정(f12, ref-1454), BidProposal 필드 5개와 같은 프로젝트 자료라 독립 확인 아님(f8·f9), #534 확인(f25). 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-030 근거 f4~f7, oq-053 근거 f8·f9·f11, oq-054 근거 f12·f14. 교차 확인 0건이라 사실 finding 신뢰도는 medium 이하. 현장 유형 사례 finding 은 병원 모사 환경(f15~f17)뿐이고 물류창고 실측 비교(2절 질문)는 이번에도 찾지 못함. 국내 자료 없음. L. AI·학습 기술 관련 f4~f7 은 47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안한다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
