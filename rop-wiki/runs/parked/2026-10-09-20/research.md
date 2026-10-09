# 리서치 브리프 2026-10-09-20

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-20 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

트랙 실행: 트랙 `chat-based-configuration-and-operation` · 단계 2 · 답한 질문 q1-05, q1-06, q2-04

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-04 열림(중간 표현 PDDL·LTL·행동 트리·의존 DAG 의 작업 모델·로봇 관제 인터페이스 대응) — 단계 2 페이지 3절에 답 소절 없음
- 앞 단계로 되돌아온 질문 q1-05·q1-06(물류·창고 지시 대상 LLM 작업 분해 연구와 지시–작업 데이터셋) 열림 — 단계 1 페이지 3절에 답 소절 없음, 두 질문은 뜻이 거의 같아 함께 다룸
- 단계 2 완료 조건: 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미반영(미충족), q2-05·q2-06·q2-07 열림
- 12. 채팅으로 업무 지시·오케스트레이션 페이지 5절: 물류창고·제조 공장 사례 없음(병원·실외만)

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. q1-05 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구가 있는가, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 무엇이 달라지는가?
3. q1-06 팔레트 이동·출하 준비 같은 물류·창고 현장 지시를 대상으로 한 LLM 작업 분해 연구나 지시–작업 데이터셋이 있는가, 가정용 시뮬레이터(VirtualHome, AI2-THOR) 결과를 물류 지시로 옮길 때 무엇이 달라지는가?
4. q2-04 분해 결과의 중간 표현(PDDL, LTL, 행동 트리, 의존 DAG) 가운데 업무 분해·배정 설계 초안의 작업 모델과 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업)로 옮기기 쉬운 것은 무엇이고 옮길 때 무엇이 빠지는가?
5. 국내(한국어) 자료 가운데 물류·제조 물류 현장의 자연어 로봇 지시를 다룬 연구가 있는가, 그 자료는 지시를 어떤 형식으로 바꾸는가? (12절 5. 적용 사례·oq-142 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Göbel·Lorang·Staderini·Zips(IFAC Symposium on Robotics 2025)는 공간 추론과 긴 계획이 필요한 팔레트 물류 PDDL 도메인에서 GPT-4o·GPT-o1 이 신뢰할 수 없고 자주 실행 불가능한 계획을 내며 실시간 로봇 계획에는 계산 비용이 크다고 보고하고, LLM 은 자연어 과제를 구조화된 목표로 옮겨 PDDL 문제 파일 일부를 만들고 고전 계획기가 최종 계획을 내는 하이브리드 구조를 제안했다. | ref-1337 | 아니오 | medium | 2025 | — | — |
| f2 | [사실] | Chen 외(ICRA 2024)는 창고에서 착안한 2D 다중 로봇 시나리오 네 개 가운데 이동 매니퓰레이터가 상자를 목표 구역으로 옮기는 Warehouse 시나리오(로봇 4·6·8·10대)에서 LLM 계획 구조별 평균 성공률을 분산형 0%, 혼합형 HMAS-1 5%, 중앙형 15%, 혼합형 HMAS-2 62.5%로 보고했다. | ref-1338 | 아니오 | medium | 2024-03 | — | — |
| f3 | [사실] | PIP-LLM 은 Gazebo 로 만든 창고 환경에서 로봇 12대가 선반 사이로 상품을 옮겨 목표 재고 수량을 맞추는 과제 10개를 평가했고, 저자들은 PIP-LLM 이 과제 7개에서 100%, 오탈자를 넣은 과제에서 70~90% 성공한 반면 비교 기준(CoT, SMART-LLM, LaMMA-P)은 과제 1에서만 성공했다고 보고했다. | ref-181 | 아니오 | medium | 2025-10 | — | — |
| f4 | [사실] | PIP-LLM 저자들은 미리 정의한 팀 수준 PDDL 도메인에 기대고 닫힌 정적 세계를 가정한다는 한계를 밝혔고, 'prodcut3'·'shelve4' 같은 오탈자가 새 품목·새 선반으로 해석되어 실패한 사례를 보고했다. | ref-181 | 아니오 | medium | 2025-10 | 작업 대상 | — |
| f5 | [사실] | Research Square 에 올라온 동료심사 전 프리프린트는 운영자의 자연어 명령을 LLM 이 창고 작업으로 바꾸고, SAP EWM 이 만든 창고 작업을 REST 로 자율이동로봇에 보내며, 로봇이 목적 저장 칸을 QR 코드로 확인한 뒤 EWM 에 작업을 확정하는 시제품 구조(Raspberry Pi 기반 로봇)를 기술한다. | ref-1339 | 아니오 | low | 2026-10-09 | 물류창고 / 완료·인계 | 원문 미열람 |
| f6 | [추정] | 국내 자료로 KAIST 연구진(강건·강서연·배정찬)이 2023년 대한산업공학회 추계학술대회에서 제조 물류 로봇에 LLM 을 쓴 로봇 협업 인터페이스를 발표했으며, 검색 요약에 따르면 자연어 명령을 정형화된 형태로 바꾸고 빠진 정보를 사용자에게 되묻는 구성이다. | ref-780 | 아니오 | low | 2023-11 | 제조 공장 / 시작 조건 | 원문 미열람 |
| f7 | [사실] | PlanBench(NeurIPS 2023 데이터셋·벤치마크 트랙)는 국제 계획 경진대회(IPC) 계열 도메인으로 LLM 의 계획 능력을 평가해, 계획 생성을 포함한 핵심 능력에서 최신 모델의 성능도 크게 못 미친다고 보고했다. | ref-1347 | 아니오 | medium | 2023-11 | — | — |
| f8 | [추정] | 확인한 물류 지향 연구(f1~f4)를 종합하면, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 (1) 대상이 상식 이름이 아니라 품목·선반 식별자와 수량이어서 정확 일치 접지가 필요하고 오탈자에 취약하며, (2) 같은 모양의 팔레트·상자가 많은 긴 공간 계획에서 LLM 직접 계획의 실행 가능성이 떨어지고 로봇 수가 늘면 성공률이 낮아지며, (3) 사람이 미리 설계한 닫힌 도메인 모델과 실시간 계산 비용 제약이 함께 걸리는 점이 달라지는 것으로 보인다. | ref-1337, ref-1338, ref-181, ref-1347 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [추정] | 이번 검색 범위(영어·한국어)에서 물류창고 지시를 정답 작업과 짝지어 공개한 지시–작업 데이터셋은 찾지 못했고, 가장 가까운 것은 논문 안의 시뮬레이션 과제 집합(Chen 외 Warehouse 시나리오, PIP-LLM 창고 과제 10개)과 EWM 연동 시제품 시연이어서 데이터셋으로 공개되었는지는 미확인이다. | ref-1338, ref-181, ref-1339 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | VDA 5050 공식 저장소의 주문 스키마(order.schema, main 브랜치)는 노드·간선을 sequenceId 순서의 한 줄 경로로 두고 동작에 blockingType(NONE·SOFT·SINGLE·HARD)을 붙이지만, 분기·대안 경로·주문 사이 의존·기한·우선순위를 담는 필드는 확인되지 않는다. | ref-413 | 아니오 | medium | 2026-10-09 | — | — |
| f11 | [사실] | Open-RMF 의 사용자 정의 작업(compose)은 GoToPlace·PickUp·DropOff·PerformAction 같은 공개 단계를 순서대로 이어 만들고, 활동 순서(sequence) 스키마는 플릿이 지원하는 범주·기술을 가진 활동의 배열로 정의되며, 승강기 요청 같은 단계는 RMF 가 필요할 때 자동으로 넣는다. | ref-110, ref-1340 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [사실] | Open-RMF 작업 상태 스키마에서 사건 사이 의존(deps)은 같은 작업 단계 안의 사건 id 로만 표현되므로, 작업과 작업 사이의 선행 의존을 담는 자리는 이 스키마에서 확인되지 않는다. | ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f13 | [사실] | Open-RMF 작업 요청 스키마는 가장 이른 시작 시각·우선순위·라벨·요청자·허용 플릿 이름을 선택 필드로 두고 범주·기술만 필수로 두며 마감 시각 필드는 없다. | ref-125 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | NVIDIA Isaac Mission Dispatch 는 임무를 sequence·selector·route·action·notify 노드로 된 행동 트리(암묵적 루트 sequence)로 받아, route·action 노드마다 별도의 VDA 5050 주문으로 옮기고 행동 트리 진행에 따라 주문을 차례로 보내며, action 노드의 동작은 로봇 현재 위치에 해당하는 주문 첫 노드에 붙인다. | ref-1341 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [사실] | Isaac Mission Dispatch README 는 작업 배정·충돌 해결을 다루지 않고 VDA 5050 만 지원하며, sequence·selector 구조를 바꾸려면 임무를 취소하고 다시 제출해야 하고 갱신은 아직 완료되지 않은 route 노드에만 허용한다고 밝힌다. | ref-1341 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f16 | [추정] | NVIDIA Isaac Mission Control README 는 제출된 임무로 작업 행동 트리를 조립해 Mission Dispatch 가 VDA 5050 으로 실행하게 하고, SAP EWM 창고 작업을 이동 임무로 바꾸는 기능과 VDA 5050 차량 유형에 MANIPULATOR·HUMANOID 를 더한 확장을 제공한다고 밝힌다. | ref-1342 | 아니오 | low | 2026-10-09 | — | 벤더 주장 |
| f17 | [사실] | ROS 2 계획 시스템 PlanSys2 의 실행기(Executor)는 PDDL 계획을 받아 행동의 효과와 뒤 행동의 요구를 짝지은 계획 그래프로 의존 관계를 만들고, 그 그래프의 실행 흐름들을 병렬로 돌리는 행동 트리로 변환해 실행한다. | ref-1343 | 아니오 | medium | 2026-10-09 | — | — |
| f18 | [사실] | DART-LLM 의 질의응답 LLM 은 하위 작업마다 실행 함수 이름·선행 의존 작업·대상 물체 키워드를 담은 구조화 JSON(의존 DAG)을 내고, 로봇 지정은 따로 파서가 맞는 스킬을 가진 가용 로봇을 고르며, 하위 작업은 위상 순서로 실행되고 의존이 없는 작업은 병렬로 실행된다. | ref-059 | 아니오 | medium | 2024-11 | — | — |
| f19 | [사실] | Nl2Hltl2Plan(arXiv 2024)은 LLM 이 계층 작업 트리를 만들고 미세 조정한 LLM 이 하위 작업을 평면 LTL 식으로 옮긴 뒤 이를 최하위가 순서 있는 로봇 행동인 계층 LTL 명세로 모아 기존 계획기로 풀며, 같은 지시가 여러 형식 명세로 번역될 수 있어 정확도와 다중 로봇 계획 효율이 떨어질 수 있다고 지적한다. | ref-1344 | 아니오 | medium | 2024-12 | — | — |
| f20 | [사실] | Luo·Liu(IEEE T-RO 2025 게재 표기)는 유한 트레이스 LTL 의 계층 확장 H-LTLf 를 정의하고, 명세별 하위 탐색 공간을 오토마타 분해로 오가며 다중 로봇의 작업 배정과 계획을 동시에 합성하는 탐색 방법을 제안했다. | ref-1345 | 아니오 | medium | 2025-06 | — | — |
| f21 | [사실] | Neupane·Mercer·Goodrich 는 목표 지향 LTLf 식의 부분집합을 행동 트리로 바꾸는 방법을 제안해, 계획기가 만든 성공 궤적이 해당 LTL 식을 만족하게 하고 행동 노드는 여러 계획기로 구현할 수 있게 했다. | ref-1346 | 아니오 | medium | 2023-12 | — | — |
| f22 | [추정] | 확인한 대응 사례(f10~f18)를 종합하면, 업무 분해·배정 설계 초안의 작업 모델과 로봇 관제 인터페이스로 가장 옮기기 쉬운 중간 표현은 하위 작업과 선행 의존을 그대로 담는 의존 DAG(또는 PDDL 계획을 의존 그래프로 바꾼 형태)이고, 잎 작업은 Open-RMF 작업 요청(배송·compose 단계)과 VDA 5050 주문으로 하나씩 옮기되 의존과 진행 순서는 ROP 실행기가 보유해 선행 작업 완료 뒤 다음 요청을 내보내는 구성이 선택지로 보인다. | ref-413, ref-1340, ref-111, ref-1341, ref-1343, ref-059, ref-181 | 아니오 | low | 2026-10-09 | — | — |
| f23 | [추정] | 중간 표현을 VDA 5050 주문·Open-RMF 작업 요청으로 옮기면 작업 사이 선행 의존, 행동 트리의 selector 같은 대안 경로, 기한(VDA 5050 은 우선순위도), 지시 원문·배정 근거·확인 여부가 빠지므로 이 항목은 ROP 작업 모델과 실행기에 남겨야 하고, 행동 트리의 제어 흐름을 바꾸려면 Mission Dispatch 처럼 취소·재제출이 필요해지는 것으로 보인다. | ref-413, ref-125, ref-111, ref-1341 | 아니오 | low | 2026-10-09 | — | — |
| f24 | [추정] | LTL 계열 표현은 계획이 아니라 명세여서 계획기(계층 LTL 계획, LTLf→행동 트리 변환)를 거친 뒤에야 로봇 관제 인터페이스로 옮길 수 있으므로, ROP 에서는 직접 변환 대상보다 의존 DAG·계획이 금지 구역·순서 같은 현장 규칙을 지키는지 검사하는 명세층으로 쓰는 편이 맞아 보인다. | ref-1344, ref-1345, ref-1346 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

- **f1**: 저장소 초록 기준: 팔레트 물류 도메인, LLM 이 자연어 과제 기술을 구조화된 목표로 바꿔 PDDL 문제 파일을 부분 구성, 고전 계획기가 최종 계획. 정량 결과는 초록에 없음(IFAC PapersOnline 59(18), 301–306).
- **f2**: Warehouse: 로봇이 허용 경로를 좌우 이동·인접 상자 집기·목표 구역에 놓기, 같은 칸 두 대는 충돌. 로봇 4·6·8·10대, 40회 평균 성공률 DMAS 0.0%, HMAS-1 5.0%, CMAS 15.0%, HMAS-2 62.5%(저자 보고, 격자 시뮬레이션).
- **f3**: 팀 수준 PDDL 도메인의 move-product 행동, 과제 6·7에 의도적 오탈자. 성공률 PIP-LLM 과제 1–4·8–10 100%, 5 90%, 6 80%, 7 70%; 기준선은 과제 1 만 100%(저자 보고, 시뮬레이션, Table III).
- **f4**: 한계: LLM 이 도메인을 자동 설계하기 어려워 사전 정의 도메인 필요, 물체 변화·확률적 행동 성공 같은 불확실성은 재계획이 필요하나 포함하지 않음, 오탈자로 간헐적 실패(저자 보고).
- **f5**: 검색 요약 기준: SAP S/4HANA 2023·EWM·ABAP REST 서비스·Raspberry Pi 로봇·Python API·BTP 로 구현, 로봇 LALLU 가 QR 로 저장 칸 확인 후 EWM 에 작업 확정. 저자·게시일·정량 결과 미확인(발행일 미확인, 확인일 기준).
- **f6**: DBpia 서지: 논문집 75–89쪽, 2023-11. 초록·본문은 페이지에 없어 미열람. 정형화·되묻기·최적 경로 설정 서술은 검색 결과 요약에만 나타남.
- **f7**: 초록 인용: "LLM performance falls quite short, even with the SOTA models." 물류(Logistics) 도메인 포함 여부는 2차 요약에서만 확인(원문 표 미열람).
- **f8**: 이 위키의 종합(추론). 근거는 모두 시뮬레이션·격자 시나리오·도메인 실험이며 실제 물류센터 운영 평가는 확인하지 못함.
- **f9**: 검색 범위의 관찰이며 부재의 확인은 아님. 과제 집합의 공개 여부·라이선스는 원문에서 확인하지 못함.
- **f10**: 필수: headerId·timestamp·version·manufacturer·serialNumber·orderId·orderUpdateId·nodes·edges. released 는 베이스·호라이즌 구분, orderUpdateId 는 갱신용. 연 스키마 범위의 부재 관찰(발행일 미확인, 확인일 기준).
- **f11**: task_new: 작업은 단계(Phase)의 순서·조합, RequestLift 단계는 내부적으로 자동 추가. event_description__sequence.json: 'A sequence of activities', 각 활동은 category·description 필수(발행일 미확인, 확인일 기준).
- **f12**: event_state.deps 설명: "Event IDs are isolated within the scope of this task phase." 연 스키마 범위의 부재 관찰(발행일 미확인, 확인일 기준).
- **f13**: required: category, description. fleet_name 을 지정하면 그 플릿만 입찰. 기한 필드 없음(발행일 미확인, 확인일 기준; 재인용: 2026-09-25-37).
- **f14**: README: "Each route or action mission tree node will be translated into a separate VDA5050 Order message." 노드 상태 IDLE·RUNNING·SUCCESS·FAILURE, sequence 는 실패 시 멈추고 selector 는 성공할 때까지 다음 자식 시도(발행일 미확인, 확인일 기준).
- **f15**: 실행 중 임무 취소는 needs_canceled 표시 뒤 현재 임무가 끝난 다음 처리, 경로 중간 경유점은 건너뛸 수 있으나 마지막 경유점은 도달해야 함(발행일 미확인, 확인일 기준).
- **f16**: 벤더 주장: README 기준 점유 격자 지도·CSR 그래프·cuOpt 경로로 계획, 'VDA5050 Action node'(4.6.0), SAP EWM 작업→이동 임무 변환. 확장 열거형은 Mission Client 3.2.0 이상 필요(발행일 미확인, 확인일 기준).
- **f17**: 설계 문서 인용: "the Executor converts it to a Behavior Tree to execute it." 구성: Domain Expert·Problem Expert·Planner(기본 POPF)·Executor(발행일 미확인, 확인일 기준).
- **f18**: arXiv v2 기준: 형식에 로봇 id 필드 없음, Actuation 모듈이 비동기 실행, 이동은 ROS Navigation, 모듈 간 ROS2 토픽. 평가는 건설 시나리오(Unity·PhysX, Yanmar C30R 2대·Hitachi ZX120).
- **f19**: 초록 기준: 사람 참가 시뮬레이션·실기 실험에서 성공률·배정 비용 개선 주장(저자 보고, 동료심사 게재처 미확인). 계획기 이름은 초록에 없음.
- **f20**: 초록 기준: 평면 LTLf 보다 표현력이 높음을 증명, 사용자 연구에서 계층 명세 이해가 쉬웠고, 서비스 과제에서 계획 시간을 줄이며 해 품질은 비슷했다(저자 보고).
- **f21**: AAMAS 2023 부속 ARMS 워크숍 발표(arXiv v2 2023-12). 변환되는 연산자 목록은 초록에 없음.
- **f22**: 이 위키의 종합(추론). 근거: VDA 5050 주문은 한 줄 경로(f10), Open-RMF 의존은 단계 안에만(f12), Mission Dispatch 는 잎마다 주문 하나(f14), PlanSys2·DART-LLM 은 의존 그래프를 실행기가 위상 순서로 집행(f17·f18).
- **f23**: 이 위키의 종합(추론). 각 형식의 필드 관찰은 연 스키마·README 범위의 부재 관찰이며 부재의 확인은 아님.
- **f24**: 이 위키의 종합(추론). 근거 연구는 서비스·가정·실험실 과제 조건이며 물류 플릿 적용은 확인하지 못함.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1337 | Göbel, K., Lorang, P., Staderini, V., & Zips, P. (AIT Austrian Institute of Technology, IFAC PapersOnline 59(18)) | Integrating LLMs and Classical Planning for Pallet Logistics: A Case Study | 2025 | 논문 | medium | 2026-10-09 | https://publications.ait.ac.at/de/publications/integrating-llms-and-classical-planning-for-pallet-logistics-a-ca/ | 아니오 |
| ref-1338 | Chen, Y., Arkin, J., Zhang, Y., Roy, N., & Fan, C. (MIT, ICRA 2024) | Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems? | 2023-09 | 논문 | high | 2026-10-09 | https://arxiv.org/abs/2309.15943 | 아니오 |
| ref-1339 | Research Square 프리프린트(저자 미확인) | An Intelligent Warehouse Execution Framework Integrating SAP Extended WarehouseManagement, Large Language Models, SAP Business Technology Platform, and Autonomous Mobile Robots | 미확인 | 논문 | low | 2026-10-09 | https://www.researchsquare.com/article/rs-10351090 | 예 |
| ref-1340 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__sequence.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__sequence.json | 아니오 |
| ref-1341 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/nvidia-isaac/isaac_mission_dispatch | 아니오 |
| ref-1342 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_control — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/nvidia-isaac/isaac_mission_control | 아니오 |
| ref-1343 | PlanSys2 (ROS 2 Planning System 프로젝트) | PlanSys2 Design | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://plansys2.github.io/design/index.html | 아니오 |
| ref-1344 | Xu, S., Luo, X., Huang, Y., Leng, L., Liu, R., & Liu, C. | Nl2Hltl2Plan: Scaling Up Natural Language Understanding for Multi-Robots Through Hierarchical Temporal Logic Task Representation | 2024-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2408.08188 | 아니오 |
| ref-1345 | Luo, X., & Liu, C. (IEEE Transactions on Robotics 2025 게재 표기) | Simultaneous Task Allocation and Planning for Multi-Robots under Hierarchical Temporal Logic Specifications | 2024-01 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2401.04003 | 아니오 |
| ref-1346 | Neupane, A., Mercer, E. G., & Goodrich, M. A. (AAMAS 2023 ARMS 워크숍) | Designing Behavior Trees from Goal-Oriented LTLf Formulas | 2023-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2307.06399 | 아니오 |
| ref-1347 | Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S., & Kambhampati, S. (NeurIPS 2023 Datasets and Benchmarks) | PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change | 2022-06 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2206.10498 | 아니오 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.22784 | 아니오 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-780 | 강건(대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 2023-11 | 논문 | medium | 2026-10-09 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 | 예 |

### 출처 요약

- **ref-1337**: 14th IFAC Symposium on Robotics(2025) 논문의 기관 저장소 서지·초록. 팔레트 물류 PDDL 도메인에서 LLM 직접 계획의 한계와 LLM 목표 정식화 + 고전 계획기 하이브리드를 제안(DOI 10.1016/j.ifacol.2025.10.237, 본문 미열람).
- **ref-1338**: LLM 다중 로봇 계획의 중앙·분산·혼합 통신 구조를 창고에서 착안한 2D 시나리오 네 개(BoxNet1·2, Warehouse, BoxLift)와 3D 시뮬레이션으로 비교한 ICRA 2024 논문(v2 2024-03 본문 열람).
- **ref-1339**: 원문 미열람. 동료심사 전 프리프린트. 검색 요약 기준 자연어 명령→LLM→SAP EWM 창고 작업→REST→AMR, QR 저장 칸 확인 뒤 작업 확정 구조의 시제품.
- **ref-1340**: Open-RMF 플릿 어댑터의 활동 순서(Activity Sequence) JSON 스키마. 플릿이 지원하는 범주·기술을 가진 활동의 배열.
- **ref-1341**: 행동 트리 형태의 임무 트리(sequence·selector·route·action·notify)를 VDA 5050 주문으로 옮겨 MQTT 로 로봇에 보내는 임무 배치 서비스의 README.
- **ref-1342**: 임무로 작업 행동 트리를 조립하고 Mission Dispatch 로 VDA 5050 실행하는 플릿 관리 서비스 README. SAP EWM 작업 변환 등 기능 설명은 벤더 주장.
- **ref-1343**: PDDL 기반 ROS 2 계획 시스템의 설계 문서. 실행기가 계획을 의존 그래프 기반 행동 트리로 변환해 병렬 실행한다.
- **ref-1344**: 자연어→계층 작업 트리→평면 LTL→계층 LTL 명세→계획기의 다중 로봇 계획 틀(arXiv 프리프린트, 초록 열람, v4 2024-12).
- **ref-1345**: 계층 LTLf(H-LTLf) 명세에서 다중 로봇 작업 배정과 계획을 동시에 합성하는 탐색 방법(초록 열람, v4 2025-06).
- **ref-1346**: 목표 지향 LTLf 식의 부분집합을 행동 트리로 바꾸고 계획기가 행동 노드를 구현하게 하는 방법(초록 열람, v2 2023-12).
- **ref-1347**: IPC 계열 계획 도메인으로 LLM 의 계획·변화 추론 능력을 평가하는 벤치마크(초록 열람, v4 2023-11).
- **ref-181**: LLM 이 팀 수준 PDDL 문제를 만들고 계획을 의존 그래프로 바꾼 뒤 정수계획으로 로봇을 배정하는 틀. 이번 실행에서 HTML 본문으로 창고 실험·한계를 열람.
- **ref-059**: LLM 이 의존 DAG 형태의 구조화 JSON 으로 다중 로봇 작업을 분해하고 위상 순서로 실행하는 틀. 이번 실행에서 v2 HTML 본문 열람.
- **ref-413**: VDA 5050 공식 저장소 main 브랜치의 주문 JSON 스키마. 노드·간선·동작의 필드 구성.
- **ref-110**: Open-RMF 작업 V2 의 단계(Phase) 개념, 공개 단계, 사용자 정의 작업 요청 구성 방법.
- **ref-111**: Open-RMF 작업 상태 JSON 스키마(배정·배치·진행·단계·사건 상태).
- **ref-125**: Open-RMF 작업 요청 JSON 스키마(범주·기술 필수, 시작 시각·우선순위 등 선택).
- **ref-780**: 원문 미열람. DBpia 서지(KAIST 강건·강서연·배정찬, 75–89쪽)만 확인했고 초록·본문은 페이지에 없음.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 9 | q1-05 답: f1·f2·f3·f4·f5·f6·f7·f8 (신뢰도 low) / q1-06 답: f2·f3·f8·f9 (신뢰도 low) / q2-04 답: f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24 (신뢰도 low) — 단계 2 질문 목록에서 q2-04 상태를 답함으로, 3절에 q2-04 소절(중간 표현별 작업 모델·VDA 5050 주문·Open-RMF 작업 요청 대응과 빠지는 항목, 표는 이 위키 구성), 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건 현황(여전히 미충족), 9절 이력 갱신. q1-05·q1-06 답 본문은 단계 1 페이지에 싣는다 |
| update | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md | 2, 3, 4, 5 | 앞 단계로 되돌아온 질문 q1-05·q1-06 의 답 소절 추가(f1~f9: 팔레트 물류 PDDL 하이브리드, 창고 격자 시나리오, PIP-LLM 창고 시뮬레이션과 한계, SAP EWM 연동 시제품(물류창고 사례, 동료심사 전), 국내 KAIST 제조 물류 발표(추정), 가정→물류 전환 시 달라지는 점(추정), 공개 물류 지시–작업 데이터셋 미발견(추정)). 두 질문은 뜻이 겹쳐 한 소절로 답하고 질문 목록 상태를 갱신. 질문–finding 대응은 단계 2 페이지 제안 rationale 참조 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | 2, 6 | 온톨로지 변경 제안 1건(작업 개념 속성 '선후관계'를 작업 사이 선행 의존으로 정리하고 외부 형식에 자리가 없어 작업 모델이 보유한다는 메모 추가, 근거 f10·f12·f14·f18·f22), 6절 '작업 사이 선행 의존' 질문에 q2-04 답 연결(f22·f23), 'LTL 을 명세 검사층으로 둘지' 질문 추가(f24) |
| update | docs/ideas/chat-based-configuration-and-operation.md | 3, 4 | 아이디어 페이지 3절: 물류 지향 LLM 분해 연구와 물류 적용 공백 갱신(f1~f9) / 아이디어 페이지 4절: 중간 표현과 로봇 관제 인터페이스 대응 소절 추가(f10~f24) |
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | 5, 6, 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (finding f5·f14·f17·f18·f22·f23): 5절 물류창고 사례(SAP EWM 연동 시제품, 동료심사 전, 6항목 대부분 미확인), 6절 중간 표현과 의존 DAG 실행 구조, 7절 Isaac Mission Dispatch(행동 트리→VDA 5050 주문)·PlanSys2. 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결 |
| update | docs/categories/planning-and-optimization/task-and-workflow-modeling.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (finding f14·f17·f18·f21): 행동 트리 임무를 VDA 5050 주문으로 옮기는 Mission Dispatch, PDDL 계획을 행동 트리로 실행하는 PlanSys2, 의존 DAG(DART-LLM), LTLf→행동 트리 변환 |
| update | docs/categories/site-type-applications/warehouse.md | 6 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (finding f1·f2·f3·f5·f9): 물류·창고 지시를 다룬 LLM 작업 분해 연구(모두 시뮬레이션·시제품 조건)와 공개 물류 지시–작업 데이터셋 미발견 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 유한 트레이스 선형 시간 논리 | Linear Temporal Logic on Finite Traces (LTLf) | 유한한 길이의 실행 궤적에 대해 '언젠가', '항상', '다음' 같은 시간 조건을 표현하는 선형 시간 논리의 변형으로, 끝이 있는 로봇 임무 명세에 쓰인다. |
| 작업 의존 그래프 | Task Dependency Graph (Dependency DAG) | 하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 실행기는 위상 순서에 따라 의존이 풀린 작업부터 실행한다. |

## 열린 질문

새로 생긴 질문:

- 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 24. 작업·워크플로 모델링 | 근거: f23 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 11건
- 미확인 항목:
    - f5 SAP EWM 연동 프리프린트의 저자·게시일·정량 결과(검색 요약의 98%·4.7초 수치 포함) 미확인, 원문 미열람
    - f6 KAIST 2023 발표의 초록·본문 미열람(검색 요약만), 되묻기 구성은 추정
    - f7 PlanBench 의 물류(Logistics) 도메인 포함과 도메인별 수치는 2차 요약에만 있어 미확인
    - f1 팔레트 물류 논문은 저장소 초록만 열람, 정량 결과 미확인
    - f16 Isaac Mission Control 의 SAP EWM 작업 변환 기능은 벤더 주장(독립 확인 없음)
    - f19·f20·f21 은 초록만 열람, 계획기 이름·로봇 수 등 세부 미확인
    - Open-RMF 플릿 어댑터 schemas 디렉터리 목록(병렬·분기 활동 범주 유무)은 GitHub 403 으로 확인하지 못해 f11 은 열람한 두 문서 범위의 관찰
- 범위 경계 위반 의심:
    - f14·f15·f16: Isaac Mission Dispatch·Mission Control 은 플릿 관리 소프트웨어이며, 로봇 쪽 주행·경로 실행은 분류 원문 19장 '로봇 자체 지능·제어'의 연계 대상이다. ROP 몫은 행동 트리·의존 그래프를 주문으로 내보내는 경계까지로 한정해 서술해야 함
    - f17·f18: PlanSys2 실행기와 DART-LLM Actuation 모듈의 ROS 내비게이션·스킬 실행은 로봇 쪽 연계 대상이며, 의존 그래프를 위상 순서로 집행한다는 구조만 ROP 설계 근거로 씀
    - f5: SAP EWM 은 상위 업무 시스템(연계 대상)이며 ROP 몫은 작업 수신·확정 반영 경계
- 한계: 트랙 실행(단계 2). 검색 17회/40, 신규 출처 11건/20(ref-1337~ref-1347, 예약 구간 안). 재사용 7건(ref-181·ref-059 webfetch 재열람, ref-413 github_raw, ref-110·ref-111·ref-125 inbox 원문, ref-780 서지 페이지만 열어 미열람 처리). target.json 이 고른 세 질문(q1-05, q1-06, q2-04)을 다뤘다. q1-05 와 q1-06 은 뜻이 거의 같아(q1-06 이 데이터셋 부분을 더함) 같은 finding 으로 함께 답했고, 답 본문은 단계 1 페이지에, 질문–finding 대응은 규약대로 현재 단계(단계 2) 페이지 제안 rationale 에 적었다. 세 질문 모두 신뢰도 low 의 답이다: 물류 지향 근거가 모두 시뮬레이션·도메인 실험·시제품이고 실제 물류센터 운영 평가는 찾지 못했으며, 중간 표현 대응의 결론(f22~f24)은 이 위키의 종합이다. 교차 확인 0건, 모든 사실 finding 은 단일 출처라 medium 이하. 벤더 문서 성격의 기능 주장 f16 은 vendor_claim·추정·'벤더 주장: ' 표시. 현장 유형 finding 은 물류창고(f5)·제조 공장(f6, 추정)뿐이다. 국내 자료는 KAIST 2023 학술대회 발표(ref-780) 서지뿐이며 본문을 열지 못했다. 후속 질문 4건 제안. 온톨로지 변경 1건(작업 개념 '선후관계' 속성 정리) 제안 — 기존 6절 질문 '작업 사이 선행 의존'과 겹치므로 관계 추가 대신 속성 메모로 냈다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 f1~f9·f19 는 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과, 적용 대상인 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링과 함께 연결하도록 제안한다. 단계 2 완료 조건은 여전히 미충족(작업 요구 적재물 속성·완료 조건 미확정, q2-05·q2-06·q2-07 열림). 입력 누락 없음. 우선 지정 질문 없음.

## 트랙 블록

- 트랙: chat-based-configuration-and-operation · 단계: 2
- 답한 질문 id: q1-05, q1-06, q2-04

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 행동 트리의 selector 같은 대안 경로·제어 흐름을 VDA 5050 주문(한 줄 노드–간선)과 Open-RMF 순차 단계로 옮길 때, ROP 는 그 흐름을 자체 실행기에 두고 잎 작업만 주문·작업 요청으로 하나씩 내보내야 하는가, 그때 제어 흐름 변경에 따른 취소·재제출 비용과 로봇 이동 연속성은 어떻게 되는가? (q2-04 에서 파생) | 3 | f15 |
| — | LLM 이 만든 작업 의존 그래프나 계획을 배치 전에 금지 구역·순서 같은 현장 규칙을 담은 LTLf 명세로 검사하는 방식을 다중 플릿 오케스트레이션에 적용한 사례가 있는가, 검사층과 사람 승인을 어떻게 나누는가? (q2-04 에서 파생) | 4 | f24 |
| — | 팔레트 물류 PDDL 도메인(IFAC 2025)이나 PIP-LLM 창고 과제 10개 같은 물류 과제 집합이 공개되어 있어 물류 지시 평가 자료(q5-04)의 출발점으로 쓸 수 있는가? (q1-06 에서 파생) | 5 | f9 |
| — | PIP-LLM 에서 오탈자가 새 품목·새 선반으로 해석된 것처럼, 물류 지시 속 품목 코드·선반·도크 식별자의 표기 오류를 이름 사전(q2-05)과 대조해 정규화할지 되물을지 정하는 기준은 무엇인가? (q1-05 에서 파생) | 2 | f4 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 작업 (Task) | f10, f12, f14, f18, f22 | 주요 속성 '선후관계'를 '선후관계(작업 사이 선행 의존, 의존 그래프로 표현)'로 정리하고 외부 표현 메모를 더한다: VDA 5050 주문 스키마와 Open-RMF 작업 상태 스키마에서는 작업 사이 의존 필드가 확인되지 않으므로(Open-RMF deps 는 단계 안 사건 사이만) 작업 모델이 보유하고, 잎 작업만 주문·작업 요청으로 내보낸다(추정 메모, f22). 초안 6절 '작업 사이 선행 의존을 관계로 드러낼 것인가' 질문과 겹치며, 이 제안은 관계를 새로 추가하지 않고 기존 속성을 유지하는 쪽을 택한다. 플릿 사이 의존의 집행 방식(oq-049, q3-09)은 정하지 않는다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 작업 모델의 정보 항목이 업무 분해·배정 설계 초안 개념 목록 표에 충분히 반영되지 않음(작업 요구 적재물 속성·완료 조건 미확정)
    - 단계 2 열린 질문 q2-05·q2-06·q2-07 미답
    - 아이디어 페이지 4절 반영 조건은 자체 평가상 충족이나 검증 승인 전
