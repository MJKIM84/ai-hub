# 리서치 브리프 2026-09-25-39

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-39 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 15. 다중 로봇 경로·교통 관리 — MAPF |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 floorplan-recognition 단계 1 반영 제안(경로망 자동 설계, ref-267·ref-268) 검토 대상
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안(ref-267·ref-268) 검토 대상
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(기존 oq-032 가 이 영역에 걸림)

## 조사 질문

1. 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
2. MAPF 는 어떻게 정의되고 어떤 목적함수·충돌 가정이 쓰이며, 최적해 계산은 얼마나 어려운가? (섹션 3·4 겨냥)
3. 대표 해법(CBS, SIPP, PIBT, 지속형 MAPF 대회 해법)은 무엇이고 물류 창고 규모에서 어떤 절충을 하는가? (섹션 6·8 겨냥)
4. 실제 로봇의 지연·운동 제약 아래 MAPF 계획을 실행하고 교착을 막는 방법은 무엇인가? (섹션 5·6 겨냥)
5. Open-RMF, VDA 5050, MassRobotics 는 다른 제조사 플릿 사이 교통 조율을 어떻게 나누어 맡는가 — oq-032(제어 수준이 낮은 플릿의 교착 방지)와 연결 (섹션 7·9 겨냥)
6. 경로망(roadmap)을 자동 설계·생성하는 연구는 MAPF 평가와 어떻게 연결되는가 — 트랙 floorplan-recognition 반영 제안 2건 검증 (섹션 6·8 겨냥)
7. 국내에서 다중 AGV 교착·혼잡 경로 계획을 다룬 연구는 무엇이 있는가? (한국 자료 우선, 섹션 8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Stern 외(2019)는 MAPF 를 여러 에이전트가 서로 충돌하지 않고 동시에 따라갈 수 있는 경로를 계획하는 문제로 두고, 연구마다 같은 길을 동시에 지날 수 있는지 같은 가정과 목적함수(마지막 도착 시각인 makespan, 행동 비용 합인 sum of costs)가 달라 공통 용어를 제안했으며 격자 벤치마크를 공개했다. | ref-828 | 아니오 | medium | 2019-06 | — | 원문 미열람 |
| f2 | [사실] | Yu·LaValle 은 그래프 위 다중 로봇 경로 계획의 네 목적(총 도착 시간, makespan, 총 이동 거리, 최대 개별 이동 거리)이 서로 동시에 최적화될 수 없는 파레토 관계이며, 각 목적의 최적해 계산이 NP-hard 임을 3-SAT 환원으로 보였다. | ref-832 | 아니오 | medium | 2015-07 | — | 원문 미열람 |
| f3 | [사실] | 충돌 기반 탐색(Conflict-Based Search, CBS)은 상위 단계에서 에이전트 쌍의 충돌로 이루어진 충돌 트리를 탐색하고 하위 단계에서는 한 번에 에이전트 하나의 경로만 탐색하는 2단계 최적 MAPF 알고리즘이다. | ref-829 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f4 | [사실] | PIBT(Priority Inheritance with Backtracking)는 매 시간 단계마다 에이전트에 고유 우선순위를 주고 우선순위 상속과 되돌림으로 한 걸음씩 이동을 정하는 반복형 MAPF 방법으로, 저자들은 수백 대 규모에서도 거의 즉시 해를 내고 인접 노드 쌍이 모두 단순 순환에 속하는 그래프(예: 이중 연결)에서는 모든 에이전트가 유한 시간 안에 목적지에 도달함을 보였다. | ref-831 | 아니오 | medium | 2019-01 | — | 원문 미열람 |
| f5 | [사실] | 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 연속된 시간 단계를 충돌 없는 안전 구간으로 묶어 상태를 '위치 + 안전 구간'으로 두는 방법으로, 로봇이 즉시 출발·정지할 수 있다는 가정 등 아래에서 완전하고 최적이다. | ref-837 | 아니오 | medium | 2011 | — | 원문 미열람 |
| f6 | [사실] | Ma 외는 표준 MAPF 해법이 최대 속도 같은 로봇의 운동 제약과 불완전한 실행을 무시한다고 지적하고, MAPF 해를 단순 시간 네트워크(simple temporal network)로 후처리해 속도 한계·안전 거리·여유 시간(slack)을 반영한 실행 일정을 만드는 MAPF-POST 를 제시했다. | ref-838 | 아니오 | medium | 2017-02 | — | 원문 미열람 |
| f7 | [사실] | Hönig 외(2019)는 MAPF 해를 풀고 난 뒤 AGV 사이 통과 순서와 운동 제약을 행동 의존 그래프(Action Dependency Graph)로 인코딩해, 예상 못한 감속·장애물 출현 같은 지연이 있어도 창고 AGV 가 계획을 충돌 없이 실행하게 하고 지연이 쌓이면 재계획 여부를 판단하는 실행 체계를 제시했다. | ref-830 | 아니오 | medium | 2019 | 예외·성과 | 원문 미열람 |
| f8 | [사실] | League of Robot Runners 2023 대회에서 Overall Best 트랙을 우승한 팀 저장소는 해법을 PIBT·대규모 이웃 탐색(LNS)·창(window) 단위 계획을 결합한 WPPL 로 설명하고, 특정 위치에서 특정 행동을 유도하는 안내 그래프(guidance graph)를 쓰며 대회의 실행 단계당 계획 시간 한도를 1초로 적는다. | ref-833 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | 시드 참고문헌 가운데 Li 외(2020)는 대규모 창고의 지속형 MAPF(Lifelong MAPF)를, Ma 외(2017)는 픽업·배송 작업이 온라인으로 들어오는 다중 에이전트 픽업·배송(MAPD)의 지속형 경로 계획을 다룬다. | ref-005, ref-006 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f10 | [사실] | Open-RMF 는 시설 안 로봇들의 예정 주행 궤적을 모은 중앙 교통 스케줄 데이터베이스를 두고 각 플릿 관리자가 예정 경로(itinerary)를 보고·갱신하게 하며, 충돌이 감지되면 관련 참여자에게 충돌 통지를 보내 각 플릿이 선호 경로와 상대를 수용하는 경로를 내고 제3자 판정자가 제안 조합을 고르는 협상을 한다. | ref-004 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | Open-RMF 문서는 플릿의 제어 수준을 완전 제어(Full Control), 일시정지·재개만 가능한 신호등(Traffic Light), 상태만 보고하는 읽기 전용(Read Only), 연동 불가(No Interface)로 나누고, 읽기 전용 플릿이 여럿이면 교착 위험이 있어 공유 공간마다 읽기 전용 플릿은 하나만 허용한다고 적는다. | ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f12 | [사실] | Open-RMF 의 rmf_traffic 패키지는 여러 에이전트 사이 이동로봇 교통을 스케줄링하고 협상하는 알고리즘과 자료구조를 제공한다. | ref-839 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | Open-RMF Traffic Editor 는 주행 차선(lane)마다 양방향 여부, 소속 플릿 그래프 번호(graph_idx), 전진·후진 방향 제약을 두고, 경유점에 대기 지점(holding point: 무기한 대기 허용)·주차 지점·충전소 표시를 두며, 기본으로 플릿 9개를 위한 그래프 9개를 제공한다. | ref-079 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f14 | [사실] | VDA 5050(최신 main, 3.0.0)은 관제가 이미 해제한 노드·간선인 베이스(base)와 계획만 된 호라이즌(horizon)을 구분하고, 해제되지 않은 노드·간선은 로봇이 지나면 안 되며, 관제는 교통 상황이 허락하면 로봇이 결정 지점에 닿기 전에 베이스를 늘려야 한다고 정한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f15 | [사실] | VDA 5050 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 규격 범위에서 제외하면서, 관제의 기능으로 교착(deadlock) 탐지·해소와 버퍼 경로·대기 위치를 포함한 교통 제어를 든다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f16 | [사실] | VDA 5050 3.0.0 은 로봇이 진입을 요청하고 관제가 응답하는 해제 구역(RELEASE), 진입 전에 계획 경로 승인을 받는 협조 재계획 구역(COORDINATED_REPLANNING), 진입 금지(BLOCKED)·속도 제한(SPEED_LIMIT)·선호 주행 방향(DIRECTED/BIDIRECTED) 구역을 정의한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f17 | [사실] | MassRobotics AMR 상호운용 표준은 제조사가 다른 로봇이 같은 공간에서 공존하도록 위치·속도·방향·상태·작업 가용성 정보를 공유하게 하는 규격이며, README 에는 경로 조율이나 우선권 결정 절차가 적혀 있지 않다. | ref-253 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f18 | [추정] | 분류 원문 질문(서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까)에 대해, VDA 5050 은 우선순위·교착 해소를 관제에 맡기고 MassRobotics 는 상태 공유만 정하므로 양보 규칙은 표준이 아니라 여러 플릿 위의 조율 계층(ROP 또는 Open-RMF 식 협상 판정자)이 정해야 하며, 한쪽 플릿이 읽기 전용 수준이면 그 플릿은 양보시킬 수 없어 다른 플릿이 양보하는 구조가 될 것으로 보인다. | ref-031, ref-253, ref-004 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f19 | [사실] | Bonetti 외(2026)는 좁은 양방향 통로와 높은 교통 밀도의 비격자형 산업 현장에서 크기와 능력이 다른 대형 AGV 를 위해, NURBS 곡선으로 만든 경로망 위의 지속형 MAPF 와 시간 지평을 조정하는 애니타임 충돌 해소, 실제 AGV 와의 실행 계층, 교착 탐지·해소 장치를 갖춘 교통 관리 시스템을 제안했다. | ref-834 | 아니오 | medium | 2026-09 | 예외·성과 | 원문 미열람 |
| f20 | [사실] | 다중 AGV 계층형 교통 관리 연구(IEEE, Hierarchical Traffic Management of Multi-AGV Systems With Deadlock Prevention)는 구역 간 교통을 모델링하는 위상 계층, 교통을 고려한 경로를 계산하는 중간 계층, 경로망에서 시간에 따라 AGV 를 조율하는 하위 계층의 3계층 구조와 시간 확장 그래프 기반 교착 예방을 제안했다. | ref-835 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f21 | [사실] | 전진표 외(2005, 한국항해항만학회지 29(8))는 주행 영역을 그리드로 관리하는 자동화 컨테이너 터미널에서 AGV 의 그리드 점유 순서 그래프의 강결합 요소를 찾아 그 그리드들로의 진입을 통제해 교착을 막고, AGV 간 간섭 지연을 반영한 회귀식으로 소요 시간이 짧은 경로를 실시간 선정하는 방안을 제시했다. | ref-836 | 아니오 | medium | 2005 | 예외·성과 | 원문 미열람 |
| f22 | [사실] | 경로망 자동 설계 연구(IEEE Transactions on Automation Science and Engineering 21(4), ref-267)는 공장 배치·차량 대수·작업 분포·배차 규칙에 맞춘 경로망을 개미 군집 영감 최적화와 사건 기반 시뮬레이터로 생성하고, SIPP 를 쓰는 MAPF 시뮬레이터로 처리량을 평가해 적정 차량 대수를 제시한다. | ref-267 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f23 | [사실] | Rüdt·Enke·Furmans(KIT)는 자유 공간의 볼록 모서리와 스테이션 상호작용 지점에 노드를 두고 로봇 치수에서 나온 최소 거리 제약과 운송 수요 기반 K-최단 경로 가지치기로 연속 공간 경로망을 만드는 방법을 제안했고, 세 인트라로지스틱스 환경에서 MAPD 해법 두 개로 평가해 PIBT 에서 최대 차량 수일 때 GSRM 대비 1.2~23.4% 앞섰다고 보고했다. | ref-268 | 아니오 | medium | 2025-11 | — | 원문 미열람 |
| f24 | [사실] | 물류과학기술연구(JLST) 게재 논문은 혼잡을 고려한 트랜스포터 경로 계획을 다중 에이전트 강화학습으로 최적화해 메가 물류센터(DC)에서 다수 트랜스포터를 제어하는 방법을 다룬다. | ref-840 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f25 | [사실] | 지속형 MAPF 에 모방 학습을 적용한 연구(arXiv 2410.21415)는 제안 방법이 League of Robot Runners 2023 우승 해법을 앞섰다고 보고했다. | ref-841 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f26 | [추정] | ROP 가 직접 맡을 교통 관리 범위는 여러 제조사 플릿에 걸친 공유 공간의 경로 예약·해제(베이스 확장), 구역 진입 허가, 우선권과 교착 탐지·해소처럼 경로망·구역 단위의 조율이며, 이는 VDA 5050 이 관제에 맡기고 Open-RMF 가 교통 스케줄·협상으로 다루는 층위에 해당하는 것으로 보인다. | ref-031, ref-004 | 아니오 | low | 2026-09-25 | — | — |
| f27 | [추정] | 연계 대상: 개별 로봇의 로컬 장애물 회피·주행 제어와 제조사 플릿 내부의 경로 계획은 로봇·제조사 관제가 맡고, ROP 는 제어 수준(완전 제어·신호등·읽기 전용)에 따라 경로 지시·일시정지·상태 수신만 할 수 있는 것으로 보인다. | ref-004, ref-031 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f28 | [추정] | 피킹 단계에서 보충 로봇과 피킹 운반 로봇(서로 다른 제조사)이 좁은 통로에서 마주치는 상황은, 대기 지점·차선 방향 같은 경로망 제약과 구역 진입 허가로 사전에 막고, 그래도 생기면 협상·일시정지로 한쪽을 대기시키는 순서로 다룰 수 있을 것으로 보인다. | ref-079, ref-031, ref-004 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f29 | [추정] | 교통 지연과 교착은 처리량 손실로 이어지므로, 실행 중 지연이 쌓일 때 계획을 유지할지 재계획할지(행동 의존 그래프 기반 판단)와 교착 발생 시 누가 해소하는지가 예외·성과 항목의 핵심이 될 것으로 보인다. | ref-830, ref-031, ref-834 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f30 | [추정] | 이 영역은 MAPD 를 통해 13. 작업 배정 — MRTA 와, 충전소·대기 지점·승강기 같은 공유 자원을 통해 16. 공용 자원·충전·에너지 최적화와, 경로망·차선 그래프를 통해 6. 지도·공간·위치 모델·21. 온보딩·설정·현장 시운전과, 플릿 제어 수준을 통해 9. 로봇·제조사 관제 연동과 이어지며, 경로망 설계 평가에 쓰는 MAPF 시뮬레이션은 가정한 미래를 실험하므로 22. 시뮬레이션·예측용 디지털 트윈에 속하는 것으로 보인다. | ref-006, ref-079, ref-267, ref-004 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 검색 요약: different MAPF papers make different assumptions (e.g., whether agents can traverse the same road at the same time) and objective functions (makespan or sum of costs); 새 격자 기반 벤치마크 소개. SoCS 2019. 원문 미열람.
- **f2**: 검색 요약: each pair of these four objectives induces a Pareto front; computation over each objective is NP-hard; 로봇 그룹이 둘뿐이어도 NP-hard. 원문 미열람.
- **f3**: 검색 요약: two-level algorithm not converting the problem into a single 'joint agent' model; high-level search on a Conflict Tree; low level for a single agent at a time. Artificial Intelligence 219:40–66. 원문 미열람.
- **f4**: 검색 요약: gives a unique priority to each agent every timestep; backtracking prevents agents from being stuck; 자동 창고 소포 운반 반복 시나리오에서 기존 방법보다 우수(저자 보고). IJCAI 2019, AIJ 2022. 원문 미열람.
- **f5**: 검색 요약: group consecutive time moments into time intervals; number of safe intervals per configuration is finite and small; provably complete and optimal under assumptions incl. instantaneous start/stop. ICRA 2011, 5628–5635. 원문 미열람.
- **f6**: 검색 요약: standard MAPF solvers ignore kinematic constraints and imperfect plan-execution; MAPF-POST postprocesses in polynomial time, guaranteed safety distance, exploits slack to avoid time-intensive replanning. IJCAI-16 워크숍. 원문 미열람.
- **f7**: 검색 요약: Action Dependency Graph encodes the ordering between AGVs as well as their kinematic constraints in a post-processing step; robust to unforeseen slow-downs; deciding when to search for an alternate plan is costly. IEEE RA-L 2019. 원문 미열람.
- **f8**: README 원본(github_raw): 'Windowed Parallel PIBT-LNS (WPPL). Essentially, it is a combination of PIBT, LNS and RHCR'; 'won the Overall Best and Fast Mover tracks'; planTimeLimit 'In the competition, it is 1'. 대회 결과는 팀 자기 보고. (발행일 미확인, 확인일 기준)
- **f9**: 참고문헌 목록의 제목 기준: 'Lifelong Multi-Agent Path Finding in Large-Scale Warehouses'(2020), 'Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks'(2017). 이번 실행에서 원문 미열람.
- **f10**: rmf-core.md 원본(github_raw): 'centralized database of all the intended robot traffic trajectories in a facility'; 예방(교통 스케줄 기반 경로 계획)과 협상 두 단계; 'each fleet manager will submit its preferred itineraries'. 고우선 작업은 협상을 강제할 수 있음. (발행일 미확인, 확인일 기준)
- **f11**: rmf-core.md 원본(github_raw): 'any shared space is allowed to have a maximum of just one "Read Only" fleet in operation'. 네 제어 수준 서술. (발행일 미확인, 확인일 기준)
- **f12**: README 원본(github_raw): 'algorithms and data structures that are used for scheduling and negotiating mobile robot traffic between multiple agents'. (발행일 미확인, 확인일 기준)
- **f13**: traffic-editor.md 원본(github_raw): bidirectional 이면 'plan routes ... assuming the lanes can be traversed in both directions'; holding point 는 'allowed to wait at this waypoint for an indefinite period of time'; 'a default of nine Graphs for nine different fleets'. 차선 속도 제한 항목은 문서에 없음. (발행일 미확인, 확인일 기준)
- **f14**: VDA5050_EN.md 원본(github_raw) 6.1.1·6.1.2: 'If a node or edge is not released, the mobile robot shall not traverse it'; 'extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it'. (발행일 미확인, 확인일 기준)
- **f15**: VDA5050_EN.md 원본 2절 범위: traffic coordination strategies '(e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included'; 5.3 관제 기능에 'Detection and resolution of blockages ("deadlocks")'. (발행일 미확인, 확인일 기준)
- **f16**: VDA5050_EN.md 원본 6.4.3 상호작용 구역, 6.4.1.1 윤곽 기반 구역: BLOCKED 'Mobile robots shall not enter this zone'; RELEASE 요청은 responses 토픽으로 응답. (발행일 미확인, 확인일 기준)
- **f17**: README 원본(github_raw): 'share information about their robot(s) location, speed, direction, health, tasking / availability'; 목적은 'coexist effectively'. 세부 필드는 JSON 스키마·PDF 에 있음(이번에 미열람). (발행일 미확인, 확인일 기준)
- **f18**: f10·f11·f15·f17 을 SCM 질문에 대응시킨 이 위키의 추론. 양보 규칙을 명시한 공통 표준은 이번 검색에서 찾지 못함(oq-032 관련).
- **f19**: 검색 요약: L-MAPF on roadmaps generated with NURBS curves; anytime conflict resolution with adaptive time horizon; execution layer for safe and standard-compliant interaction with real AGVs; deadlock detection and resolution. 처리량 우위는 저자 보고. 원문 미열람.
- **f20**: 검색 요약: three-layer control architecture (Topological, Middle, Roadmap Layer); deadlock prevention approach based on time-expanded graphs; 자동 창고 교통 처리량 최대화 목표. 저자·발행연도 원문 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f21**: 검색 요약: 그리드를 노드로 하여 점유 순서의 선후를 연결한 그래프에서 교착 발생 가능성이 있는 강결합 요소를 파악하고 진입을 통제. 회귀 분석으로 주행 소요 시간 추정. 721–731쪽. 원문 미열람.
- **f22**: 검색 요약: event-based simulator uses ant-colony inspired optimization to generate roadmaps; evaluated with a MAPF simulator that uses SIPP; optimal fleet size proposed by analysing throughput. '전문가 수작업 설계' 서술은 이번 요약에서 확인 못함. 원문 미열람.
- **f23**: 검색 요약: nodes at convex corner points and station interaction points; minimum inter-node and node-edge distance constraints derived from robot dimensions; transport demand-driven K-shortest path pruning; 'outperformed GSRM by 1.2-23.4%'. 저자 보고 수치. 원문 미열람.
- **f24**: 검색 요약(국문): MARL 과 학습 기법을 통합한 모델로 메가 DC 환경의 다수 트랜스포터 제어. 저자·권호·결과 수치 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f25**: 검색 요약: 'SILLM ... beats the winning solution of the 2023 League of Robot Runners, an international LMAPF competition'. 저자 보고. 원문 미열람.
- **f26**: f10·f14·f15·f16 을 분류 원문 9장 경계(로봇 자체 지능·제어 대 ROP)에 대응시킨 추론.
- **f27**: f11 의 제어 수준 구분과 f14 의 해제 규칙(로봇은 해제된 노드·간선만 주행)에서 도출. 로컬 회피 책임을 명시한 문구는 이번 열람 범위에서 확인하지 못함.
- **f28**: f13(대기 지점·양방향 차선), f16(RELEASE·DIRECTED 구역), f10·f11(협상·신호등 수준 일시정지)을 현장 시나리오에 조합한 추론. 실제 현장 사례는 확인하지 못함.
- **f29**: f7(재계획 시점 판단의 비용), f15(교착 해소는 관제 기능), f19(교착 탐지·해소 장치)를 물류 흐름 여섯 항목의 예외·성과에 대응시킨 추론.
- **f30**: f9(MAPD), f13(충전소·대기 지점·플릿별 그래프), f22(시뮬레이터로 경로망·차량 대수 평가), f11(제어 수준)을 영역 연결로 정리한 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2005.07371 | 예 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1705.10868 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.07175 | 예 |
| ref-828 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-829 | Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R. | Conflict-based search for optimal multi-agent pathfinding | 2015 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1016/j.artint.2014.11.006 | 예 |
| ref-830 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-831 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 2019-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1901.11282 | 예 |
| ref-832 | Yu, J., & LaValle, S. M. | Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity | 2015-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1507.03289 | 예 |
| ref-833 | DiligentPanda (Team Pikachu, GitHub) | MAPF-LRR2023 — README (Team Pikachu's solution in the League of Robot Runners Competition 2023) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/DiligentPanda/MAPF-LRR2023 | 아니오 |
| ref-834 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 2026-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2609.10400 | 예 |
| ref-835 | IEEE 게재 논문 저자(미확인) | Hierarchical Traffic Management of Multi-AGV Systems With Deadlock Prevention Applied to Industrial Environments | 미확인 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10132864/ | 예 |
| ref-836 | 전진표, 강재호, 류광렬, 김갑환, 윤항묵(한국항해항만학회지) | 자동화 컨테이너 터미널에서 AGV 교착 방지와 회귀 분석을 이용한 경로 선정 방안 | 2005 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001130155 | 예 |
| ref-837 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 2011 | 논문 | medium | 2026-09-25 | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments | 예 |
| ref-838 | Ma, H., Koenig, S. 외 | Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios | 2017-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1702.05515 | 예 |
| ref-839 | Open Robotics (open-rmf) | rmf_traffic — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_traffic | 아니오 |
| ref-840 | 물류과학기술연구(Journal of Logistics Science & Technology) 게재 논문 저자(미확인) | Multi-Agent Reinforcement Learning for Optimizing Path Planning of Transporters Considering the Congestion | 미확인 | 논문 | medium | 2026-09-25 | https://koreascience.kr/article/JAKO202426164834912.page | 예 |
| ref-841 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21415 | 예 |

### 출처 요약

- **ref-004**: Open-RMF 핵심 구조 문서. 이번 실행은 교통 스케줄 데이터베이스, 충돌 통지·협상, 플릿 제어 수준 4종과 읽기 전용 플릿 제한을 원문으로 확인했다.
- **ref-079**: Open-RMF 교통 편집기 문서. 이번 실행은 차선의 양방향·그래프 번호·방향 제약과 경유점의 대기 지점·주차·충전소 속성, 플릿별 그래프를 원문으로 확인했다.
- **ref-031**: VDA 5050 최신판(main, 3.0.0) 명세 원문. 이번 실행은 베이스·호라이즌과 해제 규칙, 교통 조율 전략의 범위 제외, 관제의 교착 해소 기능, 구역 유형을 확인했다.
- **ref-253**: MassRobotics AMR 상호운용 표준 저장소 README. 제조사가 다른 로봇의 공존을 위해 위치·속도·방향·상태·작업 가용성을 공유한다는 목적을 원문으로 확인했다.
- **ref-005**: 원문 미열람. 대규모 창고에서 에이전트가 계속 새 목적지를 받는 지속형 MAPF 를 다룬 논문(분류 원문 참고 자료).
- **ref-006**: 원문 미열람. 온라인으로 들어오는 픽업·배송 작업의 배정과 충돌 없는 경로 계획을 함께 다룬 MAPD 논문(분류 원문 참고 자료).
- **ref-267**: 원문 미열람. 개미 군집 영감 최적화와 사건 기반 시뮬레이터로 경로망을 생성하고 SIPP 기반 MAPF 시뮬레이터로 처리량·차량 대수를 평가한 논문.
- **ref-268**: 원문 미열람. 스테이션 상호작용 지점·거리 제약·운송 수요 기반 가지치기로 연속 공간 경로망을 생성하고 MAPD 해법으로 평가한 프리프린트.
- **ref-828**: 원문 미열람. MAPF 의 가정·목적함수 용어를 통일하고 격자 기반 벤치마크를 제시한 SoCS 2019 논문.
- **ref-829**: 원문 미열람. 충돌 트리 상위 탐색과 단일 에이전트 하위 탐색으로 된 최적 MAPF 알고리즘 CBS 를 제시한 Artificial Intelligence 219 논문.
- **ref-830**: 원문 미열람. 행동 의존 그래프로 창고 AGV 의 MAPF 계획을 지연에 강건하게 실행하고 재계획 시점을 판단하는 IEEE RA-L 논문.
- **ref-831**: 원문 미열람. 매 단계 우선순위·우선순위 상속·되돌림으로 대규모 반복형 MAPF 를 빠르게 푸는 PIBT 를 제시한 논문(IJCAI 2019, AIJ 2022).
- **ref-832**: 원문 미열람. 그래프 위 다중 로봇 경로 계획의 네 목적 사이 파레토 관계와 각 목적의 NP-hard 성을 보인 논문.
- **ref-833**: League of Robot Runners 2023 우승 팀의 해법 저장소 README. PIBT·LNS·창 단위 계획을 결합한 WPPL, 안내 그래프, 대회 계획 시간 한도(1초)를 설명한다.
- **ref-834**: 원문 미열람. NURBS 경로망 위 지속형 MAPF 와 교착 탐지·해소로 좁은 통로의 크기가 다른 AGV 를 조율하는 교통 관리 시스템 프리프린트.
- **ref-835**: 원문 미열람. 위상·중간·경로망 3계층 구조와 시간 확장 그래프 기반 교착 예방으로 다중 AGV 교통을 관리하는 논문.
- **ref-836**: 원문 미열람. 그리드 점유 순서 그래프의 강결합 요소 진입 통제로 AGV 교착을 막고 회귀식으로 경로를 선정하는 국내 논문(29권 8호).
- **ref-837**: 원문 미열람. 시간 단계를 안전 구간으로 묶어 동적 장애물 사이 경로를 찾는 SIPP 를 제시한 ICRA 2011 논문.
- **ref-838**: 원문 미열람. MAPF 를 실제 로봇에 옮길 때의 운동 제약·실행 불완전성 문제와 MAPF-POST 후처리를 다룬 IJCAI-16 워크숍 개관.
- **ref-839**: Open-RMF 교통 패키지 README. 여러 에이전트 사이 이동로봇 교통의 스케줄링·협상 알고리즘과 자료구조를 제공한다고 밝힌다.
- **ref-840**: 원문 미열람. 혼잡을 고려해 메가 물류센터의 다수 트랜스포터 경로 계획을 다중 에이전트 강화학습으로 최적화하는 국내 학술지 논문.
- **ref-841**: 원문 미열람. 지속형 MAPF 에 확장형 모방 학습(SILLM)을 적용해 대규모 로봇 수를 다룬 프리프린트.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절: f1·f2(문제 정의와 NP-hard 성), f18(SCM 질문과 다제조사 양보 문제) / 4절: f1(makespan·sum of costs, 정점·간선 충돌), f3·f5·f7·f9(CBS·SIPP·행동 의존 그래프·Lifelong MAPF·MAPD), f14(베이스·호라이즌) / 5절: f28(피킹, 제약), f29(예외·성과), f11(수행 자원) / 6절: f3·f4·f5·f6·f7·f8·f19·f20·f21과 트랙 floorplan-recognition 반영 제안 2건 검토 결과로 f22·f23(경로망 자동 설계·생성 — 반영 제안의 '[추정] 수작업 설계' 서술은 이번 요약에서 확인 못해 f22 는 방법 서술만 [사실]) / 7절: f10·f11·f12·f13(Open-RMF 교통 스케줄·협상·rmf_traffic·Traffic Editor), f14·f15·f16(VDA 5050 해제·범위 제외·구역), f17(MassRobotics) / 8절: f1·f2·f3·f4·f5·f6·f7·f8·f9·f19·f20·f21·f22·f23·f24·f25(국내 자료 f21·f24 포함, 트랙 반영 제안의 ref-267·ref-268 포함) / 9절: f26(직접 범위), f27(연계 대상: 로컬 회피·제조사 내부 경로 계획) / 10절: f30(13. 작업 배정 — MRTA, 16. 공용 자원·충전·에너지 최적화, 6. 지도·공간·위치 모델, 21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동, 22. 시뮬레이션·예측용 디지털 트윈), f25 는 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 11절: 기존 oq-032 와 새 열린 질문 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 충돌 기반 탐색 | Conflict-Based Search (CBS) | 에이전트 쌍의 충돌로 이루어진 충돌 트리를 상위 단계에서 탐색하고 하위 단계에서는 에이전트 하나씩 경로를 다시 찾는 2단계 최적 MAPF 알고리즘이다. |
| 안전 구간 경로 계획 | Safe Interval Path Planning (SIPP) | 위치마다 충돌 없는 연속 시간 구간(안전 구간)을 두고 '위치 + 안전 구간'을 상태로 삼아 움직이는 장애물 사이 경로를 찾는 방법이다. |
| 우선순위 상속·되돌림 | Priority Inheritance with Backtracking (PIBT) | 매 시간 단계마다 에이전트에 우선순위를 주고 우선순위 상속과 되돌림으로 한 걸음씩 이동을 정해 대규모 반복형 MAPF 를 빠르게 푸는 방법이다. |
| 행동 의존 그래프 | Action Dependency Graph (ADG) | MAPF 계획에서 로봇들 사이 통과 순서를 의존 관계로 기록해, 실행 중 지연이 생겨도 그 순서를 지키며 충돌 없이 계획을 실행하게 하는 그래프이다. |
| 교착 | Deadlock | 여러 로봇이 서로 상대가 비켜 주기를 기다리며 아무도 진행하지 못하는 상태로, 좁은 통로·공유 구간에서 교통 관리가 탐지·예방·해소해야 한다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가? | 관련 영역: 15. 다중 로봇 경로·교통 관리 — MAPF, 9. 로봇·제조사 관제 연동 | 근거: f10 | 종류: 일반
- 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? | 관련 영역: 15. 다중 로봇 경로·교통 관리 — MAPF, 23. 시험·형식 검증·벤치마크 | 근거: f8 | 종류: 일반
- 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? | 관련 영역: 15. 다중 로봇 경로·교통 관리 — MAPF, 14. 작업 순서·스케줄링 | 근거: f18 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 23회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 알고리즘·표준 내용은 각각 단일 발행 주체 자료
    - f2·f3·f4·f5·f6·f7·f19·f20·f21·f22·f23·f24·f25 근거 원문 미열람(검색 요약 범위)
    - f20 ref-835 저자·발행연도 미확인
    - f24 ref-840 저자·권호·발행연도·결과 미확인
    - f8·f23·f25 성능·순위는 저자·팀 자기 보고
    - 트랙 반영 제안의 '경로망은 보통 전문가가 수작업으로 설계해 시간이 많이 들고 최적이 아닐 수 있다'(ref-267) 서술은 이번 검색 요약에서 확인하지 못함
    - MassRobotics 스키마의 경로·목적지 필드 세부는 미열람
    - Open-RMF Traffic Editor 차선 속도 제한 항목은 문서에서 확인되지 않음
- 범위 경계 위반 의심:
    - f27: 로봇 로컬 회피·주행 제어는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이라 claim 을 '연계 대상: '으로 표시함
    - f19·f21: 대형 AGV·컨테이너 터미널 사례는 업종·실외 조건이 섞여 물류센터 직접 적용 근거로는 제한적임
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-004(rmf-core)·ref-079(traffic-editor)·ref-031(VDA 5050 main)·ref-253(MassRobotics README), 신규 ref-833(MAPF-LRR2023 README)·ref-839(rmf_traffic README). PIBT 저장소 README(pibt2)는 main·master 모두 404 로 열지 못함. 그 밖의 신규 12건과 재사용 ref-005·ref-006·ref-267·ref-268 은 원문 미열람(신뢰도 상한 medium). finding 신뢰도 모두 medium 이하, 교차 확인 0건. 검색 23회/30, 신규 출처 14건/15(ref-828~ref-841, 예약 구간 안), 재사용 8건. 세부영역 반영 제안 2건(트랙 floorplan-recognition 2026-09-25-22)을 검토해 f22·f23 으로 6·8절 반영을 제안했다. 한국 자료: 전진표 외 2005(ref-836), 물류과학기술연구 게재 논문(ref-840). 교차 규칙: 학습 기반 MAPF(f25)는 27. AI·학습·적응과 모델 운영과 이 영역 양쪽 연결을 제안했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다(경로망 평가용 MAPF 시뮬레이션은 22 쪽으로만 연결). 정정 요청 없음. oq-032 는 f11(읽기 전용 플릿은 공유 공간당 하나, 신호등 수준은 일시정지·재개)로 일부 답했으나 제어 수준별 교통 성능을 측정한 연구를 찾지 못해 해결 제안하지 않았다.
