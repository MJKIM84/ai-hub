# 리서치 브리프 2026-10-09-25

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-25 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 12. 채팅으로 업무 지시·오케스트레이션 |
| 대분류 | C. 채팅 기반 구성·운영 |

트랙 실행: 트랙 `chat-based-configuration-and-operation` · 단계 2 · 답한 질문 q1-05, q1-06, q2-04

## 갭(비어 있거나 약한 섹션)

- 앞 단계로 되돌아온 단계 1 질문 q1-05·q1-06 열림 — 단계 1 페이지 3절에 답 소절 없음(target.json 지정: 사용자 지정 0건, 되돌아온 질문 2건, 현재 단계 열린 질문 4건 중 오래된 순)
- 단계 2 질문 q2-04 열림 — 단계 2 페이지 3절에 {#q2-04} 소절 없음(보류된 실행 2026-10-09-20 의 답은 2차 검증 불통과로 반영되지 않음)
- 단계 2 완료 조건: 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정, q2-05·q2-06·q2-07 열림
- 업무 분해·배정 설계 초안 6절 '작업 사이 선행 의존을 관계로 드러낼 것인가' 질문에 외부 형식(VDA 5050 주문·Open-RMF 작업) 대응 근거 없음
- 12. 채팅으로 업무 지시·오케스트레이션 섹션 5. 적용 사례 — 물류창고·제조 공장 사례 없음(병원·실외만), oq-142 국내 사례 미해결

## 조사 질문

1. 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
2. q1-05 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구가 있는가, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 무엇이 달라지는가?
3. q1-06 팔레트 이동·출하 준비 같은 물류·창고 현장 지시를 대상으로 한 LLM 작업 분해 연구나 지시–작업 데이터셋이 있는가, 가정용 시뮬레이터(VirtualHome, AI2-THOR) 결과를 물류 지시로 옮길 때 무엇이 달라지는가?
4. q2-04 분해 결과의 중간 표현(PDDL, LTL, 행동 트리, 의존 DAG) 가운데 업무 분해·배정 설계 초안의 작업 모델과 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업)로 옮기기 쉬운 것은 무엇이고 옮길 때 무엇이 빠지는가?
5. 행동 트리보다 표현력이 큰 워크플로 형식(Open-RMF 차세대 워크플로 다이어그램 등)은 분기·동기화·순환을 어떻게 다루며, ROP 실행기가 작업 사이 제어 흐름을 보관하는 형식으로 쓸 수 있는가? (단계 2 페이지 3절 q2-04 겨냥)
6. 국내(한국어) 자료 가운데 물류·제조 물류 현장의 자연어 로봇 지시를 다룬 연구나 운영 사례가 있는가? (12. 채팅으로 업무 지시·오케스트레이션 섹션 5, oq-142 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Göbel·Lorang·Staderini·Zips(IFAC PapersOnline 59(18), 14th IFAC Symposium on Robotics 2025)는 공간 추론과 긴 계획이 필요한 팔레트 물류 PDDL 도메인에서 GPT-4o·GPT-o1 이 신뢰할 수 있고 실행 가능한 계획을 만드는 데 어려움을 겪고 계산 비용이 커 실시간 로봇 계획에 비실용적이라고 보고하고, LLM 은 자연어 과제를 구조화된 목표로 옮겨 PDDL 문제 파일 일부를 만들고 고전 계획기가 최종 계획을 내는 하이브리드 구조를 제안했다. | ref-1391 | 아니오 | medium | 2025 | — | — |
| f2 | [사실] | Chen 외(ICRA 2024)는 창고에서 착안한 2D 격자 시뮬레이션의 Warehouse 시나리오(이동 매니퓰레이터가 상자를 목표 구역으로 옮김, 로봇 4·6·8·10대, 로봇 수마다 10회·합 40회)에서 LLM 다중 로봇 계획 구조별 성공률을 분산형 0.0%, 혼합형 HMAS-1 5.0%, 중앙형 15.0%, 혼합형 HMAS-2 62.5%로 보고했다(저자 보고). | ref-1392 | 아니오 | medium | 2024-03 | — | — |
| f3 | [사실] | PIP-LLM 저자들은 Gazebo 로 만든 창고 환경에서 로봇 12대가 선반 사이로 상품 블록을 옮기는 과제 10개(과제마다 초기 위치를 바꿔 10회)를 평가해, PIP-LLM 이 과제 1–4·8–10 에서 100%, 과제 5 에서 90%, 오탈자를 넣은 과제 6·7 에서 80%·70% 성공한 반면 비교 기준(CoT, SMART-LLM, LaMMA-P)은 과제 1 에서만 성공했다고 보고했다. | ref-181 | 아니오 | medium | 2025-10 | — | — |
| f4 | [사실] | PIP-LLM 저자들은 미리 정의한 팀 수준 PDDL 도메인에 기대고 닫힌 정적 세계를 가정한다는 한계를 밝혔고, 'prodcut3'·'shelve4' 같은 오탈자가 새 품목·새 선반으로 해석되어 실패할 수 있다고 보고했다. | ref-181 | 아니오 | medium | 2025-10 | 작업 대상 | — |
| f5 | [사실] | Choe 외(arXiv 2505.13376, 2025-05)는 창고 배치를 동기로 이종 로봇이 자연어 도움 요청을 문법 제약 디코딩으로 신호 시간 논리(STL)로 옮기고 MILP 로 풀어 도움 줄 로봇을 고르는 분산 구조를 제안했고, 지게차 6대 격자 시뮬레이션 100회에서 시스템 전체 영향 기준 선택이 최근접 로봇 선택보다 추가 시간 합계를 평균 약 26% 줄였으며 최근접 선택이 최적과 일치한 비율은 42%였다고 보고했다. | ref-1402 | 아니오 | medium | 2025-05 | — | — |
| f6 | [사실] | IMR-LLM(arXiv 2603.02669, 2026-03)의 저자들은 산업 제조 작업이 가정 작업보다 순서 제약이 엄격하고 의존이 복잡해 LLM 에 어렵다고 보고, LLM 이 이접 그래프(disjunctive graph) 구성을 돕고 결정적 해법기가 상위 작업 계획을 푸는 2단 구조와 세 복잡도 수준의 산업 다중 로봇 벤치마크 IMR-Bench 를 제안했다. | ref-170 | 아니오 | medium | 2026-03 | — | — |
| f7 | [사실] | Research Square 에 올라온 동료심사 전 프리프린트는 운영자의 자연어 명령을 LLM 이 창고 작업으로 바꾸고, SAP EWM 의 창고 작업을 자율이동로봇(LALLU)에 보내며, 로봇이 목적 저장 칸을 QR 코드로 확인한 뒤 EWM 에 작업을 확정하는 시제품(SAP S/4HANA 2023·ABAP REST·Raspberry Pi 기반) 구조를 기술한다. | ref-1393 | 아니오 | low | 2026-10-09 | 물류창고 / 완료·인계 | 원문 미열람 |
| f8 | [추정] | 국내 자료로 KAIST 강건·강서연·배정찬이 2023-11 대한산업공학회 추계학술대회 논문집(75–89쪽)에 제조 물류 로봇의 LLM 활용 로봇 협업 인터페이스 구축을 발표했으나, 초록·본문을 확인하지 못해 지시를 어떤 형식으로 바꾸는지는 미확인이다. | ref-780 | 아니오 | low | 2023-11 | — | 원문 미열람 |
| f9 | [추정] | 확인한 물류·산업 지향 연구(f1·f3·f4·f6)를 종합하면, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 (1) 대상이 상식 이름이 아니라 품목·선반 식별자와 수량이어서 정확 일치 접지가 필요하고 표기 오류에 취약하며, (2) 같은 모양의 팔레트·상자가 많은 긴 공간 계획과 엄격한 순서 제약에서 LLM 직접 계획의 신뢰성이 떨어져 결정적 계획기·해법기를 함께 두는 구조가 반복되고, (3) 사람이 미리 설계한 닫힌 도메인 모델과 실시간 계산 비용 제약이 함께 걸리는 점이 달라지는 것으로 보인다. | ref-1391, ref-181, ref-170, ref-1392 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | Keramat·Salimi·Westerlund(arXiv 2602.08421, 2026-02)는 자연어 사용자 의도를 하위 작업으로 바꿔 여러 제조사 로봇을 조정하는 분산 다중 로봇 작업 계획기를 제안하며 평가용 벤치마크 SkillChain-RTD 를 만들어 공개했다고 밝혔으나, 초록에는 창고·물류 언급이 없다. | ref-1401 | 아니오 | medium | 2026-02 | — | — |
| f11 | [추정] | 이번 검색 범위(영어·한국어)에서 물류창고 지시를 정답 작업과 짝지어 공개한 지시–작업 데이터셋은 찾지 못했고, 가장 가까운 것은 논문 안의 시뮬레이션 과제 집합(Chen 외 Warehouse 시나리오, PIP-LLM 창고 과제 10개, Choe 외 지게차 도움 요청 시뮬레이션), 산업 제조 벤치마크 IMR-Bench(공개 여부 미확인), 일반 의도 분해 벤치마크 SkillChain-RTD(물류 아님), EWM 연동 시제품 시연이다(부재 확인 아님). | ref-1392, ref-181, ref-1402, ref-170, ref-1401, ref-1393 | 아니오 | low | 2026-10-09 | — | — |
| f12 | [사실] | VDA 5050 공식 저장소의 주문 스키마(main 브랜치)는 주문 id·갱신 id·노드·간선을 필수로 두고, 노드·간선을 공유 sequenceId 순서의 한 줄 경로로 두며 released 로 베이스·호라이즌을 나누고, 동작에 blockingType(NONE·SOFT·SINGLE·HARD)을 붙이지만, 우선순위·기한·주문 사이 의존·대안 경로(분기)를 담는 필드는 이 스키마에 없다. | ref-413 | 아니오 | medium | 2026-10-09 | — | — |
| f13 | [사실] | Open-RMF 의 사용자 정의 작업(compose)은 GoToPlace·PickUp·DropOff·PerformAction 같은 공개 단계를 순서대로 이어 만들고, 활동 순서(Activity Sequence) 스키마는 범주·기술을 필수로 가진 활동의 배열로 정의되며, 승강기 요청 같은 단계는 RMF 가 필요할 때 자동으로 넣는다. | ref-110, ref-1394 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | Open-RMF 작업 상태 스키마에서 사건 사이 의존(deps)은 같은 작업 단계(phase) 안의 사건 id 로만 표현되므로, 작업과 작업 사이의 선행 의존을 담는 자리는 이 스키마에서 확인되지 않는다. | ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [사실] | Open-RMF 작업 요청 스키마는 범주·기술만 필수로 두고 가장 이른 시작 시각·요청 시각·우선순위·라벨·요청자·허용 플릿 이름을 선택 필드로 두며 마감 시각(기한) 필드는 없다. | ref-125 | 아니오 | medium | 2026-10-09 | — | — |
| f16 | [사실] | NVIDIA Isaac Mission Dispatch 는 임무를 sequence·selector·route·action·notify 노드로 된 행동 트리(암묵적 루트 sequence)로 받아 route·action 노드마다 별도의 VDA 5050 주문으로 옮기고 행동 트리 진행에 따라 주문을 차례로 보내며, action 노드의 동작은 로봇 현재 위치에 해당하는 주문 첫 노드에 붙인다. | ref-1395 | 아니오 | medium | 2026-10-09 | — | — |
| f17 | [사실] | Isaac Mission Dispatch README 는 작업 배정·충돌 해결을 다루지 않고 VDA 5050 만 지원하며, 완료된 route 노드는 갱신할 수 없고 sequence·selector 구조를 바꾸려면 임무를 취소하고 다시 제출해야 하며, 실행 중 임무의 취소는 현재 임무가 끝난 뒤 처리된다고 밝힌다. | ref-1395 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f18 | [추정] | NVIDIA Isaac Mission Control README 는 제출된 임무로 작업 행동 트리를 조립해 Mission Dispatch 가 VDA 5050 으로 실행하게 하고, 선택 기능으로 SAP EWM 창고 작업을 받아 이동 임무로 바꿔 로봇을 배정하고 상태를 되돌리며, VDA 5050 차량 유형에 MANIPULATOR·HUMANOID 를 더한 확장을 제공한다고 밝힌다. | ref-1396 | 아니오 | low | 2026-10-09 | — | 벤더 주장 |
| f19 | [사실] | ROS 2 계획 시스템 PlanSys2 의 실행기(Executor)는 PDDL 계획을 받아 앞 행동의 효과와 뒤 행동의 요구를 짝지은 계획 그래프로 의존 관계를 만들고, 그 그래프의 실행 흐름들을 병렬로 돌리는 행동 트리로 변환해 실행하며, 기본 계획기는 POPF 이다. | ref-1397 | 아니오 | medium | 2026-10-09 | — | — |
| f20 | [사실] | DART-LLM 의 질의응답 LLM 은 하위 작업마다 실행 함수 이름·선행 의존 작업·대상 물체 키워드를 담은 구조화 출력(의존 DAG)을 내고, QA LLM 이 특정 로봇을 지명하면 그 로봇에 배정하고 그렇지 않을 때 파서가 맞는 스킬을 가진 가용 로봇을 고르며, 하위 작업은 위상 순서로 실행되고 의존이 없는 작업은 병렬로 실행된다(평가는 건설 기계 시나리오). | ref-059 | 아니오 | medium | 2024-11 | — | — |
| f21 | [사실] | Nl2Hltl2Plan(Xu 외, arXiv v4 2024-12-05, 게재처 표기 없음)은 LLM 이 계층 작업 트리를 만들고 미세 조정한 LLM 이 하위 작업을 평면 LTL 식으로 옮긴 뒤 최하위가 순서 있는 로봇 행동인 계층 LTL 명세로 모아 기성 계획기로 풀며, 같은 지시가 여러 형식 명세로 번역될 수 있어 정확도와 다중 로봇 계획 효율이 떨어질 수 있다고 지적하고, 작업 배정과 계획의 비용을 개선했다고 보고했다. | ref-1398 | 아니오 | medium | 2024-12 | — | — |
| f22 | [사실] | Luo·Liu(IEEE T-RO 2025 게재 예정 표기)는 유한 트레이스 LTL 의 계층 확장 H-LTLf 를 정의하고, 명세별 하위 탐색 공간을 오가며 다중 로봇의 작업 배정과 계획을 동시에 합성하는 탐색 방법을 제안해 서비스 과제 시뮬레이션에서 계획 시간을 줄였다고 보고했다. | ref-1399 | 아니오 | medium | 2025-06 | — | — |
| f23 | [사실] | Neupane·Mercer·Goodrich(AAMAS 2023 ARMS 워크숍)는 목표 지향 LTLf 식의 부분집합을 행동 트리로 바꾸는 방법을 제안해, 성공한 실행 궤적이 해당 LTL 식을 만족하게 하고 행동 노드는 여러 계획기로 구현할 수 있게 했다. | ref-1400 | 아니오 | medium | 2023-12 | — | — |
| f24 | [사실] | Open-RMF 상호운용 관심 그룹 공지(2024-07-25 게시, 2024-08-01 발표)는 행동 트리의 트리 구조가 임의의 분기·동기화·순환을 표현하기 어렵게(때로 불가능하게) 만들며, 행동 트리는 모두 동등한 워크플로로 바꿀 수 있지만 모든 워크플로를 행동 트리로 나타낼 수는 없다고 설명한다. | ref-1403 | 아니오 | medium | 2024-07-25 | — | — |
| f25 | [사실] | Open-RMF 상호운용 관심 그룹 공지(2025-05-31 게시)는 그래픽 다이어그램으로 나타낼 수 있는 워크플로를 사람이 읽을 수 있는 JSON 스키마('워크플로 다이어그램')로 정의하고, 라이브러리가 실행 시 이를 빌드해 실행하며, 빌드 단계에서 호환되지 않는 메시지·끝나지 않는 워크플로·정의되지 않은 연산 같은 오류를 실행 전에 보고한다고 밝힌다. | ref-1404 | 아니오 | medium | 2025-05-31 | — | — |
| f26 | [사실] | open-rmf 조직의 crossflow 저장소 README 는 crossflow 를 bevy ECS 기반 반응형 프로그래밍 라이브러리로 소개하고, 그 워크플로가 병렬 분기·동기화·경주(race)·순환을 포함할 수 있으며 ROS 2 통합은 별도 브랜치에 있다고 적는다. | ref-1405 | 아니오 | medium | 2026-10-09 | — | — |
| f27 | [추정] | 확인한 대응 사례(f12~f20)를 종합하면, 업무 분해·배정 설계 초안의 작업 모델과 로봇 관제 인터페이스로 가장 옮기기 쉬운 중간 표현은 하위 작업과 선행 의존을 그대로 담는 의존 DAG(또는 PDDL 계획을 의존 그래프로 바꾼 형태)이고, 잎 작업은 Open-RMF 작업 요청(배송·compose 단계)과 VDA 5050 주문으로 하나씩 옮기되 의존과 진행 순서는 ROP 실행기가 보유해 선행 작업 완료 뒤 다음 요청을 내보내는 구성이 선택지로 보인다. | ref-413, ref-1394, ref-111, ref-1395, ref-1397, ref-059, ref-181 | 아니오 | low | 2026-10-09 | — | — |
| f28 | [추정] | 중간 표현을 VDA 5050 주문·Open-RMF 작업 요청으로 옮기면 작업 사이 선행 의존, 행동 트리 selector 같은 대안 경로, 기한(VDA 5050 은 우선순위도), 지시 원문·배정 근거·확인 여부가 빠지므로 이 항목은 ROP 작업 모델과 실행기에 남겨야 하고, 행동 트리의 제어 흐름을 바꾸려면 Mission Dispatch 처럼 취소·재제출이 필요해지는 것으로 보인다. | ref-413, ref-125, ref-111, ref-1395 | 아니오 | low | 2026-10-09 | — | — |
| f29 | [추정] | LTL 계열 표현은 계획이 아니라 명세여서 계획기(계층 LTL 계획, LTLf→행동 트리 변환)를 거친 뒤에야 로봇 관제 인터페이스로 옮길 수 있으므로, ROP 에서는 직접 변환 대상보다 의존 DAG·계획이 금지 구역·순서 같은 현장 규칙을 지키는지 검사하는 명세층으로 쓰는 편이 맞아 보인다. | ref-1398, ref-1399, ref-1400 | 아니오 | low | 2026-10-09 | — | — |
| f30 | [추정] | 행동 트리로 나타내기 어려운 임의의 분기·동기화·순환을 표현하는 워크플로 형식(Open-RMF 진영의 워크플로 다이어그램·crossflow)이 등장하고 있어, ROP 실행기가 작업 사이 제어 흐름을 보관하는 형식의 후보가 행동 트리·의존 DAG 외에 워크플로 다이어그램까지 넓어질 수 있는 것으로 보이나, 이를 VDA 5050 주문·Open-RMF 작업 요청 송출과 연결한 공개 사례는 이번 범위에서 확인하지 못했다. | ref-1403, ref-1404, ref-1405 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

- **f1**: AIT 저장소 서지·초록 열람(DOI 10.1016/j.ifacol.2025.10.237, 301–306쪽). 초록에 빈도 표현('자주')은 없음. 정량 결과·사용 계획기 미확인.
- **f2**: arXiv HTML v2(2024-03-22, Journal reference ICRA 2024) Table I. 같은 위치 두 로봇은 충돌·실패, 로봇당 행동 6개. 로봇 수별 성공률 수치는 본문에 없음(그림만).
- **f3**: arXiv HTML 열람, Table III(저자 보고, 시뮬레이션 조건). 표 캡션은 'tabletop experiments'로 적어 본문 Gazebo 서술과 어긋남. 기준선 실패를 과제 1 의 초기 분포가 목표에 가깝기 때문이라 설명.
- **f4**: arXiv HTML 열람. 한계: LLM 이 팀 수준 도메인을 자동 설계하기 어렵고, 불확실성(물체 변화·확률적 결과)에는 재계획 장치가 필요. 오탈자 예는 저자 서술.
- **f5**: arXiv HTML 열람(동료심사 게재처 미확인). 시뮬레이션 전용, VLM 장면 설명이 정확하다고 가정, 맨해튼 거리 근사. 번역 시험은 7,500쌍 항법 데이터에서 500쌍 표본(저자 보고).
- **f6**: arXiv 초록 열람(v1). IMR-Bench 의 장면·로봇·작업 수와 공개 여부는 초록에 없음. 저자 보고로 모든 지표에서 기존 방법을 앞섰다고 함.
- **f7**: 원문 미열람(페이지 열람 시 제목만 반환). 검색 결과 요약 기준. 저자·게시일·정량 결과·실제 창고 운영 여부 미확인. (발행일 미확인, 확인일 기준)
- **f8**: DBpia 서지 페이지 열람(초록 칸 비어 있음). 재검색에서도 구성 서술을 확인하지 못함. 서지 사실만 사용.
- **f9**: 이 위키의 종합. 근거는 모두 시뮬레이션·도메인 실험·초록 수준이며 실제 물류센터 운영 평가는 확인하지 못함. 로봇 수 증가에 따른 성공률 변화는 수치 미확인이라 넣지 않음.
- **f10**: arXiv 초록 열람. 벤치마크의 규모·정답 형식은 초록에 없음(검색 요약은 의도 30개·선형 하위 작업 순서라 전하나 미확인). Hyperledger Fabric 기반 접근 통제 포함.
- **f11**: 검색 범위의 관찰(한국어 검색 4회 포함). 각 과제 집합이 데이터셋으로 공개되었는지는 미확인. 단계 2 페이지 q2-03 의 '물류 지시 데이터셋 미발견'과 같은 방향.
- **f12**: raw 원문 열람. 주문 사이 연결 필드는 orderId·orderUpdateId(한 주문의 갱신 묶음)뿐. 기한·우선순위 부재는 단계 2 페이지 q2-01 의 기존 관찰과 같음. (발행일 미확인, 확인일 기준)
- **f13**: ref-110 입력 원문과 ref-1394 raw 원문 열람(같은 Open Robotics 계열이라 독립 교차 아님). 순서 스키마 설명 'A sequence of activities'. 병렬·분기 활동 범주 유무는 미확인. (발행일 미확인, 확인일 기준)
- **f14**: 입력 원문 대조: deps 항목 설명 'Event IDs are isolated within the scope of this task phase.' 단계 2 페이지 q2-02·초안 6절의 기존 관찰과 같음. (발행일 미확인, 확인일 기준)
- **f15**: 입력 원문 대조(required: category, description). 단계 2 페이지 q2-01 의 기존 주장과 같음 — 새로 반복하지 말고 #q2-01 을 가리킬 것. (발행일 미확인, 확인일 기준)
- **f16**: README raw 열람: "Each route or action mission tree node will be translated into a separate VDA5050 Order message." (발행일 미확인, 확인일 기준)
- **f17**: README raw 열람. 실행 중 취소는 needs_canceled 표시 뒤 임무 종료 후 처리. 원격 조작은 사용자 정의 동작(startTeleop 등)으로 처리. (발행일 미확인, 확인일 기준)
- **f18**: 벤더 주장: README raw 열람. 버전 이력 5.0.0 스킬 추가, 4.6.0 VDA5050 Action 노드 추가. 확장 유형은 Mission Client 3.2.0 이상 필요. 독립 확인 없음. (발행일 미확인, 확인일 기준)
- **f19**: PlanSys2 설계 문서 열람. 공유 행동은 Singleton 방식으로 중복되지 않음. 행동 실행용 사용자 정의 BT 템플릿 지정 가능. (발행일 미확인, 확인일 기준)
- **f20**: arXiv HTML 열람. 벤치마크 102개 지시(L1 47·L2 33·L3 22), Unity/PhysX 와 Yanmar C30R 2대·Hitachi ZX120. 템플릿은 instruction_function 키가 반복되는 형식.
- **f21**: arXiv 초록 열람. 사람 참가 시뮬레이션·실기 실험의 성공률·비용 개선은 저자 보고. 계획기 이름·로봇 수 미확인.
- **f22**: arXiv 초록 열람(v4 2025-06-05, 'Accepted to appear in IEEE Transactions on Robotics 2025'). 해 품질은 기존 방법과 비슷(저자 보고), 사용자 연구 포함.
- **f23**: arXiv 초록 열람(v2 2023-12-19, 'Most Visionary Paper'). Fetch 로봇의 순차 열쇠–문 문제로 시연.
- **f24**: Open Robotics Discourse 공지 열람(작성자 grey): "every behavior tree can be converted into an equivalent workflow". 발표 내용 자체는 미열람.
- **f25**: Discourse 공지 열람. 연산 예: Listen, Scope(분기 경주), Section Template, Spread/Collect(병렬·수집), Trim(노드 취소), Gate(분기 차단) — 일부는 JSON 연산으로 점차 제공 중이라 적음.
- **f26**: README raw 열람. JSON 다이어그램 형식의 세부와 Open-RMF 차세대와의 관계는 README 에 서술 없음(검색 요약은 차세대 Open-RMF 기반 요소라 전함). (발행일 미확인, 확인일 기준)
- **f27**: 이 위키의 종합. Mission Dispatch(BT→주문 순차 송출)·PlanSys2(PDDL→계획 그래프→BT)·DART-LLM(DAG 위상 실행)이 같은 '잎 단위 송출, 의존은 상위 보유' 구조를 보임. 물류 플릿 적용 사례 미확인.
- **f28**: 이 위키의 종합. 각 '필드 없음'은 연 스키마 범위의 부재 관찰이며 부재 확인 아님. 배정 근거·확인 여부 누락은 단계 2 q2-02 결론과 같은 방향.
- **f29**: 이 위키의 종합. 근거 연구는 서비스·실험실 조건이고 물류 플릿 적용은 미확인. 검사층 설계는 백로그 q4-14·oq-302·oq-314 와 이어짐.
- **f30**: 이 위키의 종합. 근거는 프로젝트 포럼 공지와 README 이며 JSON 스키마 원문·운영 사례는 미확인. 부재 확인 아님.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1391 | Göbel, K., Lorang, P., Staderini, V., & Zips, P. (AIT Austrian Institute of Technology, IFAC PapersOnline 59(18)) | Integrating LLMs and Classical Planning for Pallet Logistics: A Case Study | 2025 | 논문 | medium | 2026-10-09 | https://publications.ait.ac.at/de/publications/integrating-llms-and-classical-planning-for-pallet-logistics-a-ca/ | 아니오 |
| ref-1392 | Chen, Y., Arkin, J., Zhang, Y., Roy, N., & Fan, C. (MIT, ICRA 2024) | Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems? | 2023-09 | 논문 | high | 2026-10-09 | https://arxiv.org/abs/2309.15943 | 아니오 |
| ref-1393 | Research Square 프리프린트(저자 미확인) | An Intelligent Warehouse Execution Framework Integrating SAP Extended WarehouseManagement, Large Language Models, SAP Business Technology Platform, and Autonomous Mobile Robots | 미확인 | 논문 | low | 2026-10-09 | https://www.researchsquare.com/article/rs-10351090 | 예 |
| ref-1394 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__sequence.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__sequence.json | 아니오 |
| ref-1395 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/nvidia-isaac/isaac_mission_dispatch | 아니오 |
| ref-1396 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_control — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/nvidia-isaac/isaac_mission_control | 아니오 |
| ref-1397 | PlanSys2 (ROS 2 Planning System 프로젝트) | PlanSys2 Design | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://plansys2.github.io/design/index.html | 아니오 |
| ref-1398 | Xu, S., Luo, X., Huang, Y., Leng, L., Liu, R., & Liu, C. | Nl2Hltl2Plan: Scaling Up Natural Language Understanding for Multi-Robots Through Hierarchical Temporal Logic Task Representation | 2024-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2408.08188 | 아니오 |
| ref-1399 | Luo, X., & Liu, C. (IEEE Transactions on Robotics 2025 게재 예정 표기) | Simultaneous Task Allocation and Planning for Multi-Robots under Hierarchical Temporal Logic Specifications | 2024-01 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2401.04003 | 아니오 |
| ref-1400 | Neupane, A., Mercer, E. G., & Goodrich, M. A. (AAMAS 2023 ARMS 워크숍) | Designing Behavior Trees from Goal-Oriented LTLf Formulas | 2023-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2307.06399 | 아니오 |
| ref-1401 | Keramat, F., Salimi, S., & Westerlund, T. | Decentralized Intent-Based Multi-Robot Task Planner with LLM Oracles on Hyperledger Fabric | 2026-02-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.08421 | 아니오 |
| ref-1402 | Choe, D. B., Sangeetha, S. V., Emanuel, S., Chiu, C.-Y., Coogan, S., & Kousik, S. | Seeing, Saying, Solving: An LLM-to-TL Framework for Cooperative Robots | 2025-05-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2505.13376 | 아니오 |
| ref-1403 | Open Source Robotics Alliance Interoperability SIG, Open Robotics Discourse | Interoperability Interest Group August 01, 2024: Multi-Agent Process Workflows | 2024-07-25 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interoperability-interest-group-august-01-2024-multi-agent-process-workflows/38794 | 아니오 |
| ref-1404 | Open Source Robotics Alliance Interoperability SIG, Open Robotics Discourse | Interoperability Interest Group June 5, 2025: Execution of Workflow Diagrams | 2025-05-31 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interoperability-interest-group-june-5-2025-execution-of-workflow-diagrams/44032 | 아니오 |
| ref-1405 | Open Robotics (open-rmf GitHub) | crossflow — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/crossflow | 아니오 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/task_new.html | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.22784 | 아니오 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-780 | 강건(대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 2023-11 | 논문 | medium | 2026-10-09 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 | 예 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2603.02669 | 아니오 |

### 출처 요약

- **ref-1391**: 14th IFAC Symposium on Robotics(2025) 발표. 팔레트 물류 PDDL 도메인에서 LLM 직접 계획의 한계와 LLM→부분 PDDL 문제 파일→고전 계획기 하이브리드 구조. 저장소 서지·초록만 열람.
- **ref-1392**: LLM 다중 로봇 계획의 중앙·분산·혼합 구조 4종을 2D 과제 4개(Warehouse 포함)와 3D 시뮬레이션에서 비교. v2(2024-03) HTML 본문 열람.
- **ref-1393**: 원문 미열람. 검색 요약 기준: 자연어 명령→LLM→SAP EWM 창고 작업→AMR(LALLU) 송출, QR 로 저장 칸 확인 뒤 EWM 확정하는 시제품. 동료심사 전.
- **ref-1394**: Open-RMF 활동 순서(Activity Sequence) 스키마. 활동 배열(각 활동은 category·description 필수).
- **ref-1395**: 행동 트리 임무를 route·action 노드별 VDA 5050 주문으로 옮겨 순차 송출하는 디스패처. 배정·충돌 해결 미처리, VDA 5050 만 지원, 구조 변경은 취소·재제출.
- **ref-1396**: 경량 플릿 관리자. 임무→작업 행동 트리 조립, Mission Dispatch 로 VDA 5050 실행, 선택적 SAP EWM 연동, VDA 5050 차량 유형 확장(MANIPULATOR·HUMANOID). 기능 서술은 벤더 주장.
- **ref-1397**: PlanSys2 실행기가 PDDL 계획을 효과–요구 짝짓기 계획 그래프로 만들고 실행 흐름을 병렬 실행하는 행동 트리로 변환하는 구조. 기본 계획기 POPF.
- **ref-1398**: 자연어→계층 작업 트리→평면 LTL→계층 LTL 명세→기성 계획기의 다중 로봇 파이프라인. 초록만 열람(v4 2024-12-05).
- **ref-1399**: 계층 유한 트레이스 LTL(H-LTLf) 정의와 다중 로봇 작업 배정·계획 동시 합성 탐색. 초록만 열람(v4 2025-06-05).
- **ref-1400**: 목표 지향 LTLf 부분집합을 행동 트리로 변환하는 방법. 초록만 열람(v2 2023-12-19).
- **ref-1401**: 자연어 의도를 하위 작업으로 바꿔 여러 제조사 로봇을 조정하는 분산 계획기와 공개 벤치마크 SkillChain-RTD. 초록만 열람.
- **ref-1402**: 창고를 동기로 한 이종 로봇 도움 요청: 자연어→STL(문법 제약)→MILP 로 도움 로봇 선택. 지게차 6대 격자 시뮬레이션에서 최근접 선택 대비 추가 시간 감소(저자 보고). HTML 본문 열람.
- **ref-1403**: Open-RMF 진영 공지. 행동 트리의 분기·동기화·순환 표현 한계와 워크플로의 일반성(BT→워크플로 변환은 가능, 역은 불가).
- **ref-1404**: 워크플로 다이어그램 JSON 스키마, 빌드 시 오류 검사, Listen·Scope·Spread/Collect·Trim·Gate 등 연산 소개.
- **ref-1405**: bevy ECS 기반 반응형 워크플로 라이브러리. 병렬 분기·동기화·경주·순환을 포함한 계층 워크플로, 워크플로 편집기 데모, ROS 2 통합은 별도 브랜치.
- **ref-413**: VDA 5050 주문 메시지 JSON 스키마(main 브랜치). 노드·간선·동작·베이스/호라이즌 구조.
- **ref-110**: RMF Task V2 의 단계(phase) 기반 사용자 정의 작업 구성, 공개 단계 GoToPlace·PickUp·DropOff·PerformAction, 자동 RequestLift.
- **ref-111**: Open-RMF 작업 상태 스키마. 단계·사건 상태, deps(단계 안 사건 의존), dispatch·status 값.
- **ref-125**: Open-RMF 작업 요청 스키마. category·description 필수, 시작 시각·우선순위 등 선택, 기한 필드 없음.
- **ref-181**: 자연어→팀 수준 PDDL→정수계획 배정. Gazebo 창고 과제 10개 평가와 한계(사전 정의 도메인, 닫힌 정적 세계, 오탈자 취약). HTML 본문 열람.
- **ref-059**: LLM 이 하위 작업 의존 DAG 를 구조화 출력으로 내고 위상 순서·병렬로 실행. 건설 기계 시나리오 평가. HTML 본문 열람.
- **ref-780**: 원문 미열람. DBpia 서지 기준: KAIST 강건·강서연·배정찬, 2023 대한산업공학회 추계학술대회 논문집 75–89쪽. 초록·본문 미확인.
- **ref-170**: 산업 제조 다중 로봇 작업: LLM 보조 이접 그래프+결정적 해법기 계획, 공정 트리 기반 프로그램 생성, IMR-Bench. 초록만 열람.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q1-05 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 (신뢰도 low) / q1-06 답: f2·f3·f6·f10·f11 (신뢰도 low) / q2-04 답: f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26·f27·f28·f29·f30 (신뢰도 low) — 2절 q2-04 를 답함(답한 실행 2026-10-09-25, #q2-04)으로, 3절 '### q2-04 … {#q2-04}' 소절 신설(중간 표현별 작업 모델·VDA 5050 주문·Open-RMF 작업 요청 대응표는 이 위키 구성[추정] f27~f30; f12·f14·f15 는 #q2-01·#q2-02 기존 서술을 가리키고 기존 각주 재사용; Mission Dispatch·PlanSys2·DART-LLM 의 로봇 쪽 주행·스킬 실행은 '연계 대상: 로봇 자체 지능·제어'로 짧게; Open-RMF 워크플로 다이어그램 f24~f26), 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건(조건 1 충족, 조건 2 미충족, 전환 아니오), 8절 출처, 9절 이력. q1-05·q1-06 답 본문은 단계 1 페이지에 싣는다. |
| update | docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md | 2, 3, 4, 5, 8, 9 | 트랙 산출물 갱신: 되돌아온 질문 q1-05·q1-06 을 3절 '### q1-05 … {#q1-05}'(f1~f9: 팔레트 물류 PDDL 하이브리드, 창고 격자 시나리오(조건 병기), PIP-LLM 창고 시뮬레이션과 한계, 창고 동기 지게차 도움 요청 STL·MILP 와 최근접 비교(f5), 산업 제조 작업의 엄격한 순서 제약(f6), SAP EWM 연동 시제품(동료심사 전·원문 미열람, f7), KAIST 2023 발표 서지만(f8), 가정→물류 차이 종합(f9))와 '### q1-06 … {#q1-06}'(q1-05 를 가리키고 데이터셋 부분 f10·f11 만 추가) 두 소절로 나누어 답하고, 2절 상태를 답함(2026-10-09-25)으로. 두 질문 신뢰도 low, 실제 물류센터 운영 평가는 확인하지 못함을 명시. |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: 온톨로지 변경 제안 1건(작업 개념 속성 '선후관계' 정리와 외부 표현 메모, 근거 f12·f14·f16·f20, 추정 메모 f27). 6절 '작업 사이 선행 의존을 관계로 드러낼 것인가' 질문은 닫지 않고 q2-04 답 링크(f27·f28)를 덧붙이며, 'LTL 계열을 명세 검사층으로 둘 것인가'(f29, 관련 q4-14)와 '작업 사이 제어 흐름을 행동 트리·의존 DAG·워크플로 다이어그램 가운데 무엇으로 보관할 것인가'(f30) 질문 추가. |
| update | docs/ideas/chat-based-configuration-and-operation.md | 3, 4 | 아이디어 페이지 3절: '물류 지시를 직접 다룬 예는 … G3뿐이었다'를 지우지 말고 '(실행 2026-09-25 기준)'을 붙인 뒤, 실행 2026-10-09-25 에서 물류·산업 지향 LLM 분해 연구(f1~f6, 모두 시뮬레이션·도메인 실험·초록 수준)와 EWM 연동 시제품 프리프린트(f7)를 확인했다는 갱신 문장 추가(f9·f11 추정). 아이디어 페이지 4절: '중간 표현과 로봇 관제 인터페이스 대응' 소절 추가(f12~f30, 대응 결론은 추정). |
| update | docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md | 5, 6, 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f7, f16, f19, f20, f27, f28): 5절 '물류창고·제조 공장·상업 시설 사례 확인되지 않음' 문장 갱신 필요 — 물류창고 사례 후보(SAP EWM 연동 시제품, 동료심사 전 프리프린트, 원문 미열람, 실제 운영 여부 미확인; SAP EWM 은 상위 업무 시스템 연계 대상이며 ROP 몫은 작업 수신과 완료 확정 반영; 제약·예외·성과는 미확인), 6절 의존 DAG 실행 구조, 7절 Isaac Mission Dispatch(행동 트리→VDA 5050 주문)·PlanSys2. 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을 함께 연결. 반영은 다음 해당 영역 실행에서. |
| update | docs/categories/planning-and-optimization/task-and-workflow-modeling.md | 7 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f16, f19, f20, f23, f24, f25): 행동 트리 임무를 VDA 5050 주문으로 옮기는 Mission Dispatch, PDDL 계획을 행동 트리로 실행하는 PlanSys2, 의존 DAG(DART-LLM), LTLf→행동 트리 변환, 분기·동기화·순환을 표현하는 Open-RMF 워크플로 다이어그램. |
| update | docs/categories/planning-and-optimization/task-allocation-mrta.md | 8 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f5): 핵심 질문 '가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?'와 관련해, 창고 동기 지게차 도움 요청 시뮬레이션에서 시스템 전체 영향 기준 선택이 최근접 선택보다 추가 시간 합계를 평균 약 26% 줄이고 최근접 선택이 최적과 일치한 비율은 42%였다는 저자 보고(시뮬레이션·프리프린트 조건). 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획과 연결. |
| update | docs/categories/site-type-applications/warehouse.md | 6 | 트랙 chat-based-configuration-and-operation 단계 2 반영 제안 (f1, f2, f3, f5, f7, f11): 물류·창고 지시를 다룬 LLM 작업 분해 연구(모두 시뮬레이션·도메인 실험·시제품 조건)와 공개 물류 지시–작업 데이터셋 미발견(추정). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 유한 트레이스 선형 시간 논리 | Linear Temporal Logic on Finite Traces (LTLf) | 기존 용어 '선형 시간 논리(LTL)'를 끝이 있는 실행 궤적에 맞게 바꾼 변형으로, '언젠가'·'항상'·'다음' 같은 시간 조건으로 끝이 있는 로봇 임무를 명세하는 데 쓰인다. |
| 작업 의존 그래프 | Task Dependency Graph (Dependency DAG) | 하위 작업을 노드로, 먼저 끝나야 하는 선행 관계를 방향 간선으로 둔 방향 비순환 그래프로, 로봇 행동 단위인 '행동 의존 그래프(ADG)'와 달리 하위 작업 단위이며 '선후 제약'을 표현하고 실행기는 위상 순서대로 의존이 풀린 작업부터 실행한다. |
| 워크플로 다이어그램 | Workflow Diagram (Open-RMF / crossflow) | Open-RMF 진영이 제안한, 그래픽 다이어그램으로 나타낼 수 있는 워크플로를 사람이 읽을 수 있는 JSON 스키마로 정의한 형식으로, 행동 트리로 표현하기 어려운 분기·동기화·순환을 담고 실행 전에 빌드 오류를 검사한다. |

## 열린 질문

새로 생긴 질문:

- 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 24. 작업·워크플로 모델링 | 근거: f28 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 15건
- 미확인 항목:
    - f7 SAP EWM 연동 프리프린트의 저자·게시일·정량 결과·실제 창고 운영 여부 미확인(Research Square 페이지 열람 시 제목만 반환, 원문 미열람)
    - f8 KAIST 2023 발표의 초록·본문 미확인(서지 사실만)
    - f2 로봇 수별 Warehouse 성공률 수치 미확인(그림만 존재)
    - f6 IMR-Bench 의 장면·로봇·작업 수와 공개 여부 미확인(초록만)
    - f10 SkillChain-RTD 의 규모·정답 형식 미확인(초록만)
    - f13 Open-RMF 플릿 어댑터 schemas 디렉터리 전체(병렬·분기 활동 범주 유무) 미확인
    - f21·f22·f23 초록만 열람, 계획기 이름·로봇 수 미확인
    - f25·f26 워크플로 다이어그램 JSON 스키마 원문과 차세대 Open-RMF 와의 공식 관계 미확인
    - PDDL+행동 트리 ARIAC 2023 논문(PMC11504948)은 브라우저 확인 화면으로 열지 못해 쓰지 않음
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
- 범위 경계 위반 의심:
    - f16·f17·f18: Isaac Mission Dispatch·Mission Control 은 플릿 관리 소프트웨어이며 로봇 쪽 주행·경로 실행은 분류 원문 19장 '로봇 자체 지능·제어'의 연계 대상 — ROP 몫은 행동 트리·의존 그래프를 주문으로 내보내는 경계까지로 한정해 서술해야 함
    - f19·f20: PlanSys2 행동 실행과 DART-LLM 의 ROS 내비게이션·스킬 실행은 로봇 쪽 연계 대상이며 의존 그래프 위상 집행 구조만 ROP 설계 근거로 씀
    - f5: VLM 기반 충돌 감지와 지게차 경로 실행은 로봇 쪽 연계 대상이며, 도움 로봇 선택(배정) 결과만 25. 작업 배정 — MRTA 근거로 씀
    - f7: SAP EWM 은 상위 업무 시스템(연계 대상)이며 ROP 몫은 작업 수신·완료 확정 반영 경계
- 한계: 트랙 실행(단계 2), web_fetch_available: true · fetch_mode full. 검색 12회/40, 신규 출처 15건/20(ref-1391~ref-1405, 예약 구간 안), 재사용 8건(ref-413 github_raw 재열람, ref-110·ref-111·ref-125 inbox 원문(fetched_via inbox, fetch_url null로 정정 기록), ref-181·ref-059·ref-170 webfetch 재열람, ref-780 서지 페이지만이라 미열람 처리). 같은 세 질문을 다룬 보류 실행 2026-10-09-20 의 브리프를 출발점으로 원문을 다시 열어 확인하고, 그 1차 검증 수정 지시를 finding 단계에서 반영했다: f1 빈도 표현 삭제, f2 조건·회수·ICRA 2024 병기, f8 서지 사실로 범위 축소, PlanBench 근거 삭제와 '로봇 수 증가 시 성공률 하락' 절 삭제(f9), f20 로봇 지명 조건·건설 시나리오 병기, f21 개선 대상을 '작업 배정과 계획의 비용'으로, f18 벤더 주장 유지, f12·f14·f15 는 단계 2 #q2-01·#q2-02 기존 관찰과 같음을 표시. 보류 실행의 출처 id(ref-1337~ref-1347)는 입력 참고문헌 목록에 없어 새 id 로 다시 부여했다(같은 URL 이면 퍼블리셔가 합침). 새로 더한 근거: 창고 동기 지게차 도움 요청 STL·MILP(f5), 산업 제조 다중 로봇 IMR-LLM(f6), SkillChain-RTD(f10), Open-RMF 워크플로 다이어그램·crossflow(f24~f26, f30). 질문 선택: target.json 지정 q1-05·q1-06·q2-04(되돌아온 질문 2건 + 현재 단계 오래된 순). 세 질문 모두 신뢰도 low 의 답이다: 물류 지향 근거가 모두 시뮬레이션·도메인 실험·시제품·초록 수준이고 실제 물류센터 운영 평가는 찾지 못했으며, 중간 표현 대응 결론(f27~f30)은 이 위키의 종합이다. q1-05 와 q1-06 은 뜻이 겹쳐 같은 finding 을 공유하되 단계 1 페이지에서 두 소제목으로 나누도록 제안했다. 벤더 근거 f18 은 vendor_claim·추정·'벤더 주장: ' 표시. 한국 자료는 KAIST 2023 학술대회 서지(ref-780)뿐이며 한국어 검색 4회에서 국내 물류 자연어 지시 연구·데이터셋은 찾지 못했다(oq-142 미해결). 교차 규칙: L. AI·학습 기술 관련 f1~f11·f21 은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과, 적용 대상 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링에 함께 연결하도록 제안. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않음. 후속 질문 3건(보류 실행 검증이 중복으로 판정한 LTLf 검사층 질문은 q4-14·oq-302·oq-314 와 같아 내지 않음, 오탈자 정규화 질문은 단계 4 로). 온톨로지 변경 1건(작업 개념 '선후관계' 정리, 관계 추가 없음). 페이지 제안: 트랙 산출물 4건, 세부영역 반영 제안 4건(갱신 상한과 별도). 정정 요청 없음, 입력 누락 없음, 우선 지정 질문 없음.

## 트랙 블록

- 트랙: chat-based-configuration-and-operation · 단계: 2
- 답한 질문 id: q1-05, q1-06, q2-04

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 행동 트리의 selector 같은 대안 경로나 Open-RMF 워크플로 다이어그램의 분기·동기화 같은 제어 흐름을 VDA 5050 주문(한 줄 노드–간선)과 Open-RMF 순차 단계로 옮길 때, ROP 는 그 흐름을 자체 실행기에 두고 잎 작업만 주문·작업 요청으로 하나씩 내보내야 하는가, 그때 제어 흐름 변경에 따른 취소·재제출 비용과 로봇 이동 연속성은 어떻게 되는가? (q2-04 에서 파생) (관련: q3-08, q3-15) | 3 | f17 |
| — | PIP-LLM 에서 오탈자가 새 품목·새 선반으로 해석된 것처럼, 물류 지시 속 품목 코드·선반·도크 식별자의 표기 오류를 이름 사전과 대조해 정규화할지 되물을지 정하는 기준은 무엇인가? (q1-05 에서 파생) (관련: q2-05, q4-07) | 4 | f4 |
| — | 팔레트 물류 PDDL 도메인(IFAC 2025), PIP-LLM 창고 과제 10개, 창고 동기 지게차 도움 요청 시뮬레이션 같은 과제 집합이 공개되어 있어 물류 지시 평가 자료의 출발점으로 쓸 수 있는가? (q1-06 에서 파생) (관련: q5-04) | 5 | f11 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 작업 (Task) | f12, f14, f16, f20, f27 | 주요 속성 '선후관계'를 '선후관계(작업 사이 선행 의존; 표현 형식 후보: 의존 그래프)'로 정리하고 외부 표현 메모를 더한다: VDA 5050 주문 스키마는 sequenceId 순서의 한 줄 노드–간선 경로이고 주문 사이 의존 필드가 없으며(f12, 사실), Open-RMF 작업 상태의 deps 는 같은 단계 안 사건 사이에만 있고(f14, 사실), Isaac Mission Dispatch 는 route·action 잎마다 별도 주문을 낸다(f16, 사실); DART-LLM 은 하위 작업 의존을 DAG 로 표현한다(f20, 사실). '작업 사이 의존은 작업 모델이 보유하고 잎 작업만 주문·작업 요청으로 내보내는 구성이 선택지로 보인다'는 추정 메모(f27)로만 둔다. 관계를 새로 추가하지 않으며 초안 6절 '작업 사이 선행 의존을 관계로 드러낼 것인가' 질문은 닫지 않는다. 플릿 사이 의존의 집행 방식(oq-049, q3-09)은 정하지 않는다. 기존 개념 상태 '확정' 유지. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 업무 분해·배정 설계 초안 개념 목록 표에 작업 요구 적재물 속성·완료 조건 미확정
    - 단계 2 열린 질문 q2-05·q2-06·q2-07 미답
    - q2-04 답과 아이디어 페이지 4절 반영은 검증 승인 전
