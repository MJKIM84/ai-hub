# 리서치 브리프 2026-10-10-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-04 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 27. 다중 로봇 경로·교통 관리 — MAPF |
| 대분류 | G. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 설명용 가정 시나리오뿐이며 확인된 다른 현장 유형(제조 공장 등) 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 첫 문장이 단일 로봇 계획인 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶음. PIBT의 '완전·최적 아님' 명시와 마감을 목적으로 하는 정식화(MAPF-DL) 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 은 main 판 기준(2026-09-25 확인)이며 3.0.0 태그의 예정 경로 공유(§6.8)·구역 요청 통신(§6.4.3) 미반영. Open-RMF 2026-09-25 이후 변경(신호등 수준 연동 수정) 미반영
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — SILLM 이 '2024, 프리프린트'로 적혀 있고 계산 규모(10,000)와 실물 검증 규모, WPPL 비교 조건이 구분돼 있지 않음. 실행 조건을 평가한 LSMART 미수록. ref-189·ref-192·ref-195·ref-199 원문 미열람
- 섹션 11. 열린 질문 — oq-058·oq-059 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
2. SIPP·PIBT의 이론 보장(완전성·최적성·도달성)은 어떤 문제 설정과 그래프 조건에서 성립하며, 다중 로봇 현장 경로망에 그대로 옮길 수 있는가? (섹션 6 겨냥)
3. 좁은 통로와 이종 대형 AGV가 있는 산업 현장에 MAPF 기반 교통 관리를 적용한 공개 사례는 현장 유형·평가 방식·교착 처리를 어떻게 밝히는가? (섹션 5·6 겨냥)
4. VDA 5050 3.0.0 과 Open-RMF 의 최신 판은 교통 관리에 쓰이는 어떤 정보(예정 경로·구역 요청·신호등 수준 연동)를 바꾸거나 더했는가? (섹션 7 겨냥)
5. oq-058 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (섹션 8·11 겨냥)
6. oq-059 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? (섹션 6·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Phillips·Likhachev(ICRA 2011)의 안전 구간 경로 계획(Safe Interval Path Planning, SIPP)은 동적 장애물마다 예측 궤적(predicted trajectories)이 주어졌다고 보고, 상태를 위치와 안전 구간의 쌍으로 묶어 로봇 한 대의 경로를 찾으며, 시간 차원을 더한 계획과 같은 최적성·완전성 보장을 준다고 밝힌다. | ref-195 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [추정] | SIPP의 완전성·최적성은 주어진 장애물 궤적에 대해 로봇 한 대의 시간 최소 경로를 찾는 범위의 결과이므로, 여러 로봇의 경로를 함께 정하는 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF) 전체의 최적성 보장으로 옮길 수 없는 것으로 보인다. | ref-195, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f3 | [사실] | Bonetti 외(2026)의 관련 연구 절은 Yan·Li(2024)가 우선순위 기반 탐색(Priority Based Search, PBS)·SIPP·베지에 곡선 최적화를 결합한 3단 다중 로봇 계획기를 우선순위 탐색에 기대므로 전역 최적성을 보장하지 않는다고 평가해, SIPP가 상위 다중 로봇 조율 아래의 저수준 계획으로 쓰이는 예를 보여 준다. | ref-192 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [의견] | 기존 6절 첫 문장처럼 SIPP를 CBS와 함께 '최적해를 보장하는 다중 로봇 탐색'으로 묶기보다, SIPP는 다른 로봇의 예정 궤적 같은 동적 장애물을 피하는 단일 로봇 저수준 경로 탐색으로 분리해 소개하는 편이 정확하다고 이 위키는 본다. | ref-195, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f5 | [사실] | Okumura 외의 우선순위 상속과 되돌리기(Priority Inheritance with Backtracking, PIBT) 논문(arXiv v5 2022-06-27, Artificial Intelligence 2022 게재판, 초판 IJCAI-19)은 §2.1에서 PIBT가 MAPF에 대해 완전하지도 최적이지도 않다고 명시하고, 도달성은 모든 에이전트가 동시에 목표에 있음을 보장하지 않으므로 일반 MAPF에는 불완전하다고 설명한다. | ref-189 | 아니오 | medium | 2026-10-10 | — | — |
| f6 | [사실] | Bonetti 외 §9는 작업 갱신 같은 예측 못 한 사건과, 시간 지평이 부족해 복도 밖 구역의 시공간 충돌을 다 풀지 못할 때 교착이 생긴다고 보고, AGV 사이 선행 관계 그래프로 순환·비순환(중첩) 교착을 탐지한 뒤 관련 AGV의 경로를 갱신해 해소하는 별도 모듈을 둔다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f7 | [의견] | PIBT의 도달 보장은 그래프 조건과 지속형 설정을 전제로 하므로, 막다른 통로가 있는 실제 경로망에는 그 보장을 그대로 적용하지 말고 후퇴 공간과 별도 교착 탐지·해소 장치(f6)를 함께 확인해야 한다고 이 위키는 본다. | ref-189, ref-192 | 아니오 | low | 2026-10-10 | — | — |
| f8 | [사실] | Bonetti 외의 교통 관리 연구(The International Journal of Robotics Research 2026 게재, DOI 10.1177/02783649261470035; arXiv 2609.10400, 2026-09-09)는 생산라인 말단 설비 업체 Gruppo TecnoFerrari와 함께 개발했으며, 평가는 그 업체가 제공한 경로망·배치로 팔레타이징·보관·팔레트 포장 공장을 모사한 소·중·대 규모 세 배치에서 했다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 | — |
| f9 | [사실] | Bonetti 외의 배치 1에서 AGV는 팔레타이저에서 포장기로 팔레트를 나르고 포장기가 바쁘거나 쓸 수 없으면 임시 보관 구역으로 돌리며, 빈 팔레트를 디스펜서에서 받아 팔레타이저에 보충한다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 작업 대상 | — |
| f10 | [사실] | Bonetti 외의 배치 1은 같은 등급 AGV가 복도 4개를 포함한 8개 구역의 좁은 비정형 공간을, 배치 2는 두 등급의 이종 AGV가 고밀도 중형 공간을, 배치 3은 이종 AGV가 좁은 양방향 복도가 없는 넓은 공간을 다니며, 그림 10·11은 막다른 좁은 복도를 표시한다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 제약 | — |
| f11 | [사실] | Bonetti 외의 시스템은 NURBS 곡선 경로망 위 지속형 MAPF(L-MAPF) 조율기(수정 Bounded Horizon CBS를 순환 지평 충돌 해소에 넣고 복도 구간에 시간 지평을 늘림), 조율된 궤적을 실행 중 안전하게 할당하는 경로 할당기(§8), 교착 탐지·처리기(§9)를 결합하고 업체의 AGV 관제 소프트웨어(TecnoFerrari Supervisor)에 C#으로 통합됐다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 수행 자원 | — |
| f12 | [사실] | Bonetti 외 논문의 공장 실험 사진은 자동화 공장에서 찍은 그림 9 한 장이고 그림 10–12는 TecnoFerrari Supervisor 소프트웨어의 2D 재구성 화면이며, 성과 지표는 Supervisor 안에서 연속 작업 배정으로 시나리오당 약 10시간 실행하며 수집했다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Bonetti 외는 업체가 배치한 규칙 기반 교통 관리, Pratissoli 외(2023)의 산업용 방법, PBS로 바꾼 L-MAPF 변형과 비교해 처리량이 최대 약 11% 높았다고 보고하며, 배치 2에서는 규칙 기반 대비 약 11%, PBS 변형 대비 약 10%, Pratissoli 외 대비 약 7%였다. | ref-192 | 아니오 | medium | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f14 | [의견] | Bonetti 외의 배치별 수치는 업체가 제공한 실제 배치를 모사한 실행 결과로 제시되고 실제 운행은 사진 한 장으로만 보이며 업체 소속 공동저자가 있고 독립 재현은 확인하지 못했으므로, 처리량 최대 11%를 상용 공장 실측 개선율이나 다른 현장의 일반 개선율로 옮기지 않아야 한다고 이 위키는 본다. | ref-192 | 아니오 | low | 2026-10-10 | 제조 공장 / 예외·성과 | — |
| f15 | [사실] | Ma 외의 마감이 있는 다중 에이전트 경로 찾기(MAPF with Deadlines, MAPF-DL, IJCAI 2018, pp.417–423)는 공통 마감 시점에 자기 목표 정점을 점유한 에이전트를 성공으로 보고 충돌 없는 성공 에이전트 수를 최대화하는 문제로 정식화하며, 최적 풀이가 NP-hard임을 보이고 흐름 문제 환원 정수 계획법과 탐색 기반 해법을 낸다. | ref-1514 | 아니오 | medium | 2026-10-10 | — | — |
| f16 | [사실] | MAPF-DL의 목적함수는 도착 시각 합이나 전체 완료 시각(makespan)을 줄이는 일반 MAPF 목적과 달리 마감 안 성공 대수를 최대화하는, 교통 계획에 마감을 넣는 공개 정식화의 예다. | ref-1514 | 아니오 | medium | 2026-10-10 | — | — |
| f17 | [의견] | MAPF-DL은 모든 에이전트에 공통 마감 하나를 두므로, 작업별로 다른 출하 마감이나 업무 중요도를 이종 플릿의 통로 양보 규칙으로 바꾸는 산업 기준으로 볼 수는 없다고 이 위키는 본다. | ref-1514, ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f18 | [사실] | VDA 5050 3.0.0 §6.8은 자유 주행 이동 로봇이 상태(state) 메시지로 관제에 예정 궤적을 알리게 하며, 주문 안의 긴 경로 plannedPath(NURBS, 최소한 현재 베이스를 포함하고 지날 nodeId 를 담을 수 있음)와 센서로 볼 수 있는 가까운 경유점별 예상 도착 시각(ETA)을 담은 폴리라인 intermediatePath를 매 상태 메시지마다 공유하게 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f19 | [사실] | VDA 5050 3.0.0 §6.4.3은 로봇이 협조 재계획(COORDINATED_REPLANNING) 구역에 들어가거나 구역 안에서 경로를 바꿀 때 zoneRequest 의 requestType 을 REPLANNING 으로 하고 예정 경로를 NURBS 궤적으로 실어 요청하게 하며, 응답을 제때 받지 못하면 구역에 들어가지 않게 한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | VDA 5050 3.0.0은 §2 Scope에서 경로·우선순위·혼잡·교착 해소 같은 교통 관리 로직을 다루지 않으므로, 예정 경로 공유·구역 요청 메시지의 상호운용성과 그 정보를 쓰는 현장 교통 최적화의 성능은 따로 검토해야 한다고 이 위키는 본다. | ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0(2026-09-26)의 변경 이력은 EasyTrafficLight의 플릿 상태 발행 수정(#525)과 EasyTrafficLight 누적 지연 계산 수정(#524)을 기록한다. | ref-1513 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [의견] | Open-RMF의 신호등(일시정지·재개) 수준 연동을 비교·시험할 때는 제어 수준뿐 아니라 EasyTrafficLight 수정(f21)이 포함된 rmf_fleet_adapter 판도 기록해야 하며, 이 변경 이력은 수정의 존재를 보여 줄 뿐 제어 수준별 처리량 비교 실험은 아니라고 이 위키는 본다. | ref-1513 | 아니오 | low | 2026-10-10 | — | — |
| f23 | [사실] | Jiang 외의 SILLM 논문(Deploying Ten Thousand Robots, ICRA 2025 채택, arXiv 초판 2024-10-28, v2 2025-05-18)은 최대 10,000 에이전트의 6개 대형 지도 벤치마크와 별도로, 초록과 서론에서 실물 로봇 10대·가상 로봇 100대로 모사 창고(mock warehouse)에서 검증했다고 적는다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f24 | [사실] | SILLM의 실물 검증(부록 VI-D)은 계획이 모든 에이전트 위치를 정확히 안다고 가정하므로 실물 로봇 위치를 외부 모션 캡처(Optitrack)로 얻고, 교란·제어 오차로 생기는 실행 오차는 행동 의존 그래프(Action Dependency Graph, ADG)로 없앴다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f25 | [사실] | SILLM 논문은 2023 League of Robot Runners 우승 해법 WPPL과 비교할 때 다른 기준선에 맞추려고 회전 동작을 없애고, 원래의 단계당 계획 시간 1초 제한 대신 대규모 이웃 탐색 개선 반복 횟수를 40,000회로 제한했다. | ref-199 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [의견] | SILLM 제목의 10,000은 계산 벤치마크의 에이전트 수이지 실물 배치 대수가 아니고, WPPL 비교는 회전 제거·반복 수 제한으로 바꾼 조건의 결과이므로 원래 대회 조건의 재현으로 읽어서는 안 된다고 이 위키는 본다. | ref-199 | 아니오 | low | 2026-10-10 | — | — |
| f27 | [사실] | Yan 외의 LSMART(2026-02-17 프리프린트)는 운동 제약·통신 지연·실행 불확실성·계획과 실행의 동시 진행·계획 실패 복구를 고려해 AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터이며, 계획기·인스턴스 생성기·계획 호출 정책·실패 정책을 설계 선택으로 비교한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f28 | [사실] | LSMART 실험은 지도와 에이전트 수 조건마다 600초 시뮬레이션을 10회 돌려 평균과 95% 신뢰구간을 제시한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f29 | [사실] | LSMART 실험에서 재계획을 더 자주 하는 것은 모든 지도·밀도에서 유리하지 않았으며(room-64-64-16과 낮은 밀도에서 이점이 일관되지 않음), 저자들은 ADG로 추정한 확정 지점이 실제 진행과 맞지 않는 실행–계획 불일치를 원인으로 든다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f30 | [사실] | LSMART 실험에서 더 정확한 로봇 모델과 더 강한 최적성 보장은 계획기의 확장성을 떨어뜨려, 저자들은 이를 계획기의 해 품질과 확장성(solution quality and scalability) 사이의 절충으로 설명한다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f31 | [사실] | LSMART는 4-연결 격자 기반 시뮬레이션이며 논문에 실물 로봇 실험은 없고, 저자들은 4-연결 격자를 넘는 그래프 지원을 향후 과제로 든다. | ref-604 | 아니오 | medium | 2026-10-10 | — | — |
| f32 | [추정] | LSMART가 격자 시뮬레이션만 다루므로(f31), 이종 제조사 로봇이 섞인 실물 창고에서의 개선율을 직접 제공하지는 않는 것으로 보인다. | ref-604 | 아니오 | low | 2026-10-10 | — | — |
| f33 | [의견] | oq-058에 대해 SILLM의 실물 10대 모사 창고 검증(f23·f24)과 LSMART의 실행 불확실성을 넣은 처리량 실험(f27~f29)이 부분 근거가 되지만, 벤치마크 개선율을 상용 물류센터 실측 개선율로 환산한 자료나 국내 사례는 확인하지 못해 정량 전이 질문은 열린 채로 둔다고 이 위키는 본다. | ref-199, ref-604 | 아니오 | low | 2026-10-10 | — | — |
| f34 | [사실] | oq-059에 대해 MAPF-DL은 공통 마감을 교통 계획의 목적함수에 넣는 정식화를 주지만 작업별 업무 우선순위를 통로 양보 우선권으로 바꾸는 규칙은 다루지 않고, VDA 5050 3.0.0도 우선순위·교착 해소 같은 교통 관리 로직을 범위에서 뺀다. | ref-1514, ref-031 | 아니오 | medium | 2026-10-10 | — | — |

### 근거 발췌

- **f1**: §I: 동적 장애물이 가까운 미래에 어디로 갈지 예측(predicted trajectory)해야 한다는 전제. §III Notations and Assumptions: 반경과 궤적(시각별 위치 목록)을 가진 동적 장애물 목록이 주어짐. 초록: "the same optimality and completeness guarantees as planning with time as an additional dimension". §III 정리 1~2에서 완전성·최적성 증명 개요. 저자 연구실 PDF 열람
- **f2**: SIPP §II: 주어진 장애물 궤적 전체에 대해 최적이며 비용은 그 로봇의 도착 시간. SIPP 논문은 다중 로봇 전체 최적성을 직접 다루지 않음. Bonetti 외 §2.1은 SIPP를 결합한 우선순위 기반 다중 로봇 계획기에 전역 최적성 보장이 없다고 평가(f3). 두 출처에서 도출
- **f3**: §2.1 Related Works: Yan and Li (2024)의 three-level MAPF-based motion planner(PBS + SIPP + Bézier 최적화)는 "does not provide any global optimality guarantees". Kasaura 외(2022)의 우선순위 SIPP(PSIPP/CTCs)도 최적성 보장이 없다고 설명
- **f4**: f1(SIPP 문제 설정: 로봇 한 대·주어진 예측 궤적)과 f3(다중 로봇 계획기 안 저수준 계층으로 쓰인 예)에서 도출한 서술 권고. 대상 문장: 6절·s6 첫 문장 'MAPF 해법은 최적해를 보장하는 탐색(CBS·SIPP)부터…'
- **f5**: §2.1: "PIBT, is neither complete nor optimal for MAPF". §1: 도달성(reachability)은 동시 목표 도달을 보장하지 않아 일반 MAPF에 불완전하나 지속형 배송(MAPD)에는 완전성을 확보한다고 설명. DOI 10.1016/j.artint.2022.103752. 그래프 조건(인접 정점 쌍의 단순 순환)은 기존 s6 에 있어 이번에 다시 싣지 않음
- **f6**: §9 Deadlock Detector and Handler: 교착 원인 (1) task updates 등 예측 못 한 사건 (2) bounded horizon 부족. Pratissoli 외(2023)의 분류로 cyclic·acyclic 교착을 나누고 precedence graph 로 탐지, 관련 AGV 경로 갱신으로 해소(그림 8)
- **f7**: PIBT 정리 1의 그래프 조건(인접 정점 쌍마다 단순 순환)과 §2.1의 불완전성 명시(f5), Bonetti 외 그림 10·11의 막다른 좁은 복도(magenta)와 §9 교착 처리(f6)에서 도출한 설계 권고
- **f8**: §10: developed in collaboration with Gruppo TecnoFerrari S.p.A. §10.1: "three realistic layouts that simulate a palletizing, storage, and pallet-wrapping plant located at the end of a production line". 경로망·배치는 업체 제공. 저자 Guidetti 는 업체 소속. arXiv 초록 페이지에 저널 게재·DOI 표시
- **f9**: §10.1 배치 1 설명: palletizers → wrapping machine, 포장기 점유 시 temporary storage, 빈 팔레트는 dispenser 에서 공급. 배치 2도 팔레타이저 → 포장기, 불가 시 창고 구역, 빈 팔레트 디스펜서 2대
- **f10**: §10.1: 배치 1 homogeneous AGV, 8 sectors including 4 corridors. 배치 2 heterogeneous 두 등급, 7 sectors including 4 corridors. 배치 3은 넓고 덜 제약된 환경(§10.2.3: 좁은 양방향 복도 없음). 그림 10·11 캡션: magenta = dead-end (narrow) corridors
- **f11**: 초록: L-MAPF on NURBS roadmaps, modified Bounded Horizon CBS within Rolling Horizon Conflict Resolution, extended time horizon in corridors. §4 구조, §8 Path Allocator, §9 Deadlock Detector and Handler. §10.1: implemented in C#, integrated into the TecnoFerrari Supervisor software
- **f12**: §10.1: 실험은 "validated in a real industrial environment in collaboration with the company (see Fig. 9)". 그림 9 캡션: 자동화 공장 실험 사진. 그림 10–12 캡션: 2D reconstruction of the plant. KPI 는 Supervisor 실행 중 수집, 시나리오당 약 10시간
- **f13**: 초록·§11: improvements of up to 11%. §10.2.4 Comparative Evaluation: 배치 1 규칙 기반 대비 약 10%·Pratissoli 대비 7%·PBS 대비 6%, 배치 2 약 11%·7%·10%. 저자 보고 수치
- **f14**: f8·f12·f13에서 도출. 원문은 세 배치를 공장을 모사한(simulate) 현실적 배치로 설명하면서 실제 산업 환경에서 검증했다고도 적어, 배치별 계산·모사 결과와 실제 운행 결과를 나눈 수치는 확인 못 함
- **f15**: §2: 에이전트 ai 는 "successful iff it occupies its goal vertex at the deadline Tend". 목적은 성공 에이전트 수 Msucc 최대화(실패 수 최소화). NP-hard 증명, §3 CBS-DL 등 탐색 해법과 흐름 환원 ILP. 학회 공식 PDF
- **f16**: §1: 일반 MAPF 목적은 도착 시각 합 또는 makespan 최소화. 기존 일반화는 마감 충족을 직접 다루지 않으며 G-TAPF 도 마감 안 완료 대수를 직접 최대화하지 않는다고 설명
- **f17**: MAPF-DL §2 정의(공통 마감 Tend 하나, 성공 대수 최대화)와 VDA 5050 3.0.0 §2 Scope(교통 관리 로직의 우선순위·교착 해소 제외)에서 도출
- **f18**: §6.8 Sharing of planned paths for freely navigating mobile robots: 두 경로 모두 로봇의 현재 위치에서 시작하고 길이는 로봇이 정함. 더 높은 빈도는 visualization 토픽. 두 필드는 로봇이 스스로 계획한 궤적에만 쓰고 edgeState 의 trajectory 는 미리 정한 궤적의 확인용. 3.0.0 태그 명세 원문 (발행일 미확인, 확인일 기준)
- **f19**: §6.4.3 Communication for interactive zones: 해제 구역은 ACCESS, 협조 재계획 구역은 REPLANNING 요청, 같은 구역에 서로 다른 궤적으로 여러 요청 가능, 응답은 responses 토픽. 구역 4종 표와 §2 범위 제외는 기존 s7 에 있어 다시 싣지 않음 (발행일 미확인, 확인일 기준)
- **f20**: §2 Scope 'Traffic Management Logic' 제외(기존 s7 에 같은 사실 있음)와 §6.8·§6.4.3(f18·f19)에서 도출한 검토 권고
- **f21**: 태그 2.14.0 CHANGELOG.rst: 'Fix EasyTrafficLight publish fleet state (#525)', 'Fix cumulative delay calculation in EasyTrafficLight (#524)'. 같은 판에 #558·#543·#534 등 다른 수정도 있음. 2.13.0(2026-06-15)에는 누적 지연을 expected_finish_state 에 반영(#518)
- **f22**: f21에서 도출. oq-032(제어 수준에 따른 교통 성능 차이)는 이 자료로 답해지지 않음
- **f23**: arXiv comment: Accepted by ICRA 2025. 초록: six large-scale maps with up to 10,000 agents; "validated SILLM with 10 real robots and 100 virtual robots in a mock warehouse environment"(서론 끝에도 같은 문장). §V-C 본문은 대수 없이 프로젝트 웹페이지를 가리킴
- **f24**: 부록 VI-D Real-World Mini Example: 가상 로봇은 참값 위치, 실물은 Optitrack Motion Capture 외부 위치 추정, 실행 오차는 ADG 로 제거. 가상 실험에서 Learnable PIBT 가 PIBT 보다 처리량이 높았다고 보고
- **f25**: 부록 VI-F1(WPPL): "We remove the rotation action to align with the settings in other baselines". 단계당 1초 대신 LNS 개선 반복 40,000회(모방 학습에 쓴 총 반복 수 수준)로 제한. 공개 저장소 MAPF-LRR2023 기반 구현
- **f26**: f23·f25에서 도출. 성능 우위는 같은 논문의 저자 보고
- **f27**: §2–3 모델·구조: FMS 는 (1) 통신 지연 (2) 행동 완료 시각의 실행 불확실성 (3) 동시 계획·실행 (4) 계획 실패 복구를 고려. §5: 네 가지 설계 선택을 모듈로 제공. arXiv v1 HTML 본문 열람
- **f28**: §4.1 General Experiment Setup: 'we run 10 simulations, each lasting for 600 simulation seconds', 평균은 실선, 95% 신뢰구간은 음영. warehouse-33-36 과 MAPF 벤치마크 지도 5종
- **f29**: §4.3 Planner Invocation Policy, 그림 4·5: 에이전트가 적으면 짧은 지평·잦은 호출, 많으면 덜 잦은 호출·긴 지평이 유리. 재계획 빈도 이점은 room-64-64-16·저밀도에서 일관되지 않음. 원인: commit cut 추정 불일치
- **f30**: §4.5 Optimality and Robot Model Accuracy, 그림 7: 실패 정책을 쓰지 않으면 정확한 모델이 항상 처리량이 높고, 최적·준최적 계획기는 둘 다 풀 수 있을 때 해 품질이 비슷함. room-64-64-16·warehouse-10-20-10-2-1 에서 절충이 뚜렷
- **f31**: §3: 2D 작업 공간을 격자로 나누고 AGV 는 한 칸 점유, 대기·회전·인접 칸 이동. §5 Conclusion: 'Future work includes adding support for graphs beyond the 4-connected grid'. 본문에 실물 로봇 실험 없음
- **f32**: f31에서 도출. 실험 지도는 격자 벤치마크이고 AGV 모델은 한 종류 기준
- **f33**: 두 자료 모두 모사 창고 또는 격자 시뮬레이션이며 상용 물류센터 처리량 실측과의 비교를 담지 않음
- **f34**: MAPF-DL §2: 공통 마감 Tend 하나와 성공 대수 최대화만 정의. VDA 5050 §2 Scope: 'Traffic Management Logic: … routing, prioritization, congestion handling, or deadlock resolution … are not included'

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-195 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 2011 | 논문 | high | 2026-10-10 | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments | 아니오 |
| ref-189 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 2019-01 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/1901.11282 | 아니오 |
| ref-192 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 2026-09-09 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/2609.10400 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1513 | Open-RMF (open-rmf/rmf_ros2 저장소) | Changelog for package rmf_fleet_adapter | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10-28 | 논문 | high | 2026-10-10 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-10-10 | https://arxiv.org/abs/2602.15721 | 아니오 |
| ref-1514 | Ma, H., Wagner, G., Felner, A., Li, J., Kumar, T. K. S., & Koenig, S. | Multi-Agent Path Finding with Deadlines | 2018 | 논문 | high | 2026-10-10 | https://www.ijcai.org/proceedings/2018/0058.pdf | 아니오 |

### 출처 요약

- **ref-195**: 동적 장애물의 예측 궤적이 주어질 때 위치·안전 구간 상태로 로봇 한 대의 경로를 찾는 SIPP 를 제시한 ICRA 2011 논문. 이번에 저자 연구실 PDF로 원문을 열람했다.
- **ref-189**: 우선순위 상속과 되돌림으로 반복형 MAPF 를 푸는 PIBT 논문. 이번에 Artificial Intelligence 2022 게재판인 arXiv v5(2022-06-27, DOI 10.1016/j.artint.2022.103752)를 열람했다.
- **ref-192**: NURBS 경로망 위 지속형 MAPF·경로 할당·교착 탐지·해소로 좁은 산업 현장의 이종 대형 AGV 를 조율하는 교통 관리 시스템. The International Journal of Robotics Research 2026 게재(DOI 10.1177/02783649261470035)이며 이번에 arXiv v1 본문을 열람했다.
- **ref-031**: VDA 5050 공식 명세 본문. 이번에 3.0.0 태그 판을 열어 §2 범위, §6.4 구역, §6.8 예정 경로 공유를 확인했다.
- **ref-1513**: rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그 고정). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행·누적 지연 계산 수정이 기록돼 있다.
- **ref-199**: 지속형 MAPF 에 확장형 모방 학습(SILLM)을 적용한 ICRA 2025 채택 논문. 이번에 v2(2025-05-18) 본문을 열람해 계산 벤치마크와 실물 10대·가상 100대 검증, WPPL 비교 조건을 확인했다.
- **ref-604**: AGV 플릿 관리 시스템 안에서 MAPF 알고리즘을 현실적으로 평가하는 오픈소스 시뮬레이터 LSMART 와 설계 선택 비교 연구(프리프린트). 이번에 v1 본문을 열람했다.
- **ref-1514**: 공통 마감까지 목표에 도달하는 에이전트 수를 최대화하는 MAPF-DL 을 정식화하고 NP-hard 증명과 흐름 환원·탐색 해법을 낸 IJCAI 2018 논문(pp.417–423). 학회 공식 PDF를 열람했다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md | 5, 6, 7, 8, 11 | 갱신(차등): 섹션 5 — 제조 공장 사례 추가: Bonetti 외(IJRR 2026) 팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 Gruppo TecnoFerrari 제공)(f8), 팔레트 운반 흐름(f9), 배치별 차량·복도 제약(f10), 시스템 구성(f11), 그림 9 실험 사진 한 장·그림 10–12 Supervisor 2D 재구성·10시간 실행(f12), 처리량 최대 약 11%는 저자 보고(f13), 현장 일반 개선율로 옮기지 않음(f14). 기존 ref-192 의 '프리프린트' 표기를 IJRR 게재로 고친다 / 섹션 6(주제 페이지 s6 요약) — 첫 문장 수정: SIPP 는 예측 궤적이 주어진 단일 로봇 경로 탐색(f1)이며 MAPF 전체 최적성으로 옮길 수 없음(f2), 다중 로봇 계획기 안 저수준 계층 예(f3), 서술 분리 권고(f4). PIBT '완전·최적 아님'(f5)과 현장 권고(f7), 교착 탐지·해소 모듈(f6). 그래프 조건 문장은 s6 기존 내용 확인(중복 추가 안 함). MAPF-DL 정식화(f15·f16)와 산업 기준이 아니라는 한정(f17) / 섹션 7(주제 페이지 s7 요약) — VDA 5050 3.0.0 §6.8 예정 경로 공유(f18), §6.4.3 협조 재계획 구역 REPLANNING 요청(f19), 메시지 상호운용성과 교통 최적화 성능 별도 검토(f20). 구역 4종 표·§2 범위 제외는 s7 기존 내용 확인(중복 추가 안 함), 발표일은 쓰지 않음. Open-RMF rmf_fleet_adapter 2.14.0 EasyTrafficLight 수정(f21)과 판 기록 권고(f22) / 섹션 8(주제 페이지 s8 요약) — SILLM 항목 수정: '2024, 프리프린트' → ICRA 2025 채택, 계산 벤치마크 10,000과 실물 10대·가상 100대(초록·서론 기준) 구분(f23), 모션 캡처·ADG(f24), WPPL 비교 조건 변경(f25), 해석 한정(f26). LSMART 추가(f27~f32): 시뮬레이터 구성, 600초×10회, 재계획 빈도 결과, 해 품질과 확장성 절충, 4-연결 격자·실물 실험 없음(사실)과 실물 창고 개선율 미제공(추정) / 섹션 11 — oq-058 부분 근거(f33), oq-059 부분 근거(f34), oq-032 는 f21·f22 가 관련 판 정보만 주며 답하지 않음. 새 질문 2건. 출처: ref-189·ref-192·ref-195·ref-199·ref-604·ref-031 원문 열람으로 갱신, 신규 ref-1513·ref-1514. 다음 실행 후보: 62. 제조 공장(f8~f14 사례 연결), 54. 시험·형식 검증·벤치마크(f27~f32), 20. 로봇·제조사 관제 연동(f18·f19·f21). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 막다른 통로·승강기 입구를 포함한 비격자 경로망에서 PIBT 같은 반복형 해법과 별도 교착 탐지·해소 장치 사이의 전환 기준은 무엇인가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f7 | 종류: 일반
- 실행 지연이 큰 환경에서 계획 호출 주기와 미리 확정하는 경로 길이를 함께 조절하는 공개 운영 기준이 있는가? | 관련 영역: 27. 다중 로봇 경로·교통 관리 — MAPF, 32. 예외 복구·재계획·업무 연속성 | 근거: f29 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 8 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 2건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-04/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 발표일(메모의 2026-03-19)은 근거를 확인하지 못해 쓰지 않았고(published null), GitHub release notes 출처(메모 n4)는 원문 확인이 안 돼 제외했다. '주요 변경' 서술은 명세 본문 §6.8·§6.4.3 으로 근거를 옮겼다
    - ref-031 은 main 판 URL 의 기존 출처이며 이번 열람은 3.0.0 태그 판이다. main 판이 3.0.0 과 같은지는 다시 대조하지 않았다
    - f13·f14: Bonetti 외의 배치별 처리량 수치가 모사 실행인지 실제 공장 운행인지 원문이 수치 단위로 구분하지 않아 확인 못 함. 독립 현장 재현 미확인
    - f23: SILLM 의 실물 10대·가상 100대는 초록과 서론 끝 문장 기준이며 §V-C 본문은 대수 없이 프로젝트 웹페이지를 가리킨다(웹페이지 미열람)
    - 모든 사실 finding 은 단일 출처라 교차 확인 0건
    - oq-058·oq-059 는 부분 근거만 있어 해결 제안하지 않음. oq-032·oq-057 근거 없음
- 범위 경계 위반 의심:
    - f6·f11: 교착 탐지·해소와 경로 할당은 ROP 직접 범위(여러 플릿의 공유 공간 조율)에 해당하나, Bonetti 외 시스템은 단일 업체 관제 안의 기능이므로 9절 책임 경계와 섞지 않도록 사례 근거로만 쓴다
    - f24: 실물 로봇 위치 추정(모션 캡처)과 실행 오차 보정은 로봇 쪽 위치 인식·제어(외부 연계 대상)와 맞닿아 있어 실험 조건 설명으로만 쓴다
- 한계: 외부 조사 변환이라 검색 집계 없음(queries 0 은 이 실행 안의 WebSearch 호출이 없다는 뜻이며, 외부 AI의 검색 횟수는 알 수 없다). 원문 대조는 2026-10-10 검증 서브에이전트가 WebFetch·GitHub raw 로 연 사본(9건 중 release notes 제외 8건)으로 했다. 출처 8건: 기존 6건(ref-031·ref-189·ref-192·ref-195·ref-199·ref-604, 이번에 원문 열람으로 fetched true), 신규 2건(ref-1513 rmf_fleet_adapter 변경 이력, ref-1514 MAPF-DL; 예약 구간 ref-1513~ref-1542 안). 동료심사 게재가 확인된 논문(ref-189 AIJ 2022, ref-192 IJRR 2026, ref-195 ICRA 2011, ref-199 ICRA 2025, ref-1514 IJCAI 2018)은 원문 열람 기준에 따라 신뢰도 high 로 적었고 프리프린트 ref-604 는 medium. 검증 수정 반영: ref-192 를 프리프린트가 아닌 IJRR 게재로, 현장 유형을 '팔레타이징·보관·팔레트 포장 공장을 모사한 세 배치(산업체 제공)'로, 사진은 그림 9 한 장·그림 10–12 는 Supervisor 2D 재구성으로 정정. PIBT 는 v5=AIJ 게재판으로 적고 그래프 조건은 s6 기존 문장이 있어 다시 넣지 않음. SILLM ICRA 2025 채택 반영. VDA 5050 발표일 null·release notes 제외, 구역 4종·§2 범위 제외는 s7 기존 내용이라 사실 finding 으로 다시 내지 않음. LSMART 마지막 문장을 사실(f31: 4-연결 격자·실물 실험 없음)과 추정(f32: 실물 창고 개선율 미제공)으로 나누고 절충 표현은 원문 'solution quality and scalability'. SIPP 는 '예측 궤적'으로. 현장 유형 finding 은 제조 공장(f6·f8~f14)뿐이며 물류창고 사례는 모사 창고(SILLM)라 site_type null. 국내 자료 없음. 용어 후보 없음(MAPF·SIPP·PIBT·ADG 계열 용어는 기존 페이지에 있고 MAPF-DL 은 본문 정의로 충분). 입력 누락 없음. 정정 요청·우선 지정 질문 없음.
