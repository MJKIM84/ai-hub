# 리서치 브리프 2026-09-25-46

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-46 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 18. 사람–로봇 협업·운영 인터페이스 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 피킹 단계의 사람 피커–운반 로봇 대기 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 nl-task-chatbot 반영 제안 4건(지시·확인·되묻기·실행 전 확인) 대기
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안 2건 대기
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-009(교대조별 작업자 수와 로봇 수)가 이 영역과 관련

## 조사 질문

1. 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [분류원문]
2. 사람 피커와 AMR(Autonomous Mobile Robot, 자율이동로봇)이 함께 피킹할 때 대기·배치(batch)·속도·인원 구성을 어떻게 정하는가, 교대조별 작업자 수와 로봇 수를 함께 정하는 모델이 있는가? (oq-009 관련, 섹션 5·6·8 겨냥)
3. 승인·수동 전환·일시정지·비상정지 같은 사람 개입을 로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 어떤 필드·기능으로 다루는가? (섹션 6·7 겨냥)
4. 사람과 이동로봇이 같은 공간에서 일할 때 적용되는 안전 표준과 국내 규제·지침은 무엇이며, ROP 인터페이스가 맡을 부분은 어디까지인가? (섹션 7·9 겨냥)
5. 운영자에게 로봇 상태와 실패를 설명 가능하게 보여 주는 방법과 한 운영자가 감독할 수 있는 로봇 수에 관한 연구는 무엇이 있는가? (섹션 4·6·8 겨냥)
6. 트랙 nl-task-chatbot 이 제안한 반영 내용 6건(자연어 지시 제품, 음성 피킹 확인, 되묻기 방식, 실행 전 확인)은 이 영역 6·8절에 어떻게 넣을 수 있는가? (섹션 6·8, 27. AI·학습·적응과 모델 운영 연결)
7. 사람–로봇 협업 인터페이스에서 ROP 직접 범위와 연계 대상(로봇 본체 안전 기능, WMS 화면)의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Žulj 외(2022)는 창고를 구역으로 나눠 구역마다 피커 1명을 두고, 피커가 통로에서 배치를 채운 뒤 교차 통로에서 기다리는 AMR에 넘기면 AMR이 출하 거점까지 운반하는 AMR 보조 피커–부품(picker-to-parts) 시스템을 다루며, AMR 보조로 피커의 비생산적 보행 시간을 줄일 수 있다고 본다. | ref-467 | 아니오 | medium | 2022 | 피킹 / 수행 자원 | 원문 미열람 |
| f2 | [사실] | Löffler·Boysen·Schneider(2023)는 AMR이 주문 용기를 싣고 선반 앞에서 기다리고 피커가 물품을 넣은 뒤 다른 대기 AMR로 옮겨 가며 출발점으로 돌아가지 않는 로봇 보조 피킹에서, 여러 AMR과 여러 피커의 조율을 작업 완료 시각(makespan) 최소화 문제로 다룬다. | ref-468 | 아니오 | medium | 2023 | 피킹 / 수행 자원 | 원문 미열람 |
| f3 | [사실] | Löffler 외(2023)는 확률적 피킹 시간이 일으키는 연쇄 지연(ripple effect)을 작업자를 작은 하위 집단으로 나누어 줄일 수 있고, 피커와 AMR의 이동 속도가 비슷해야 하며 AMR이 더 느리면 시스템 성과가 나빠진다고 보고한다. | ref-468 | 아니오 | medium | 2023 | 피킹 / 예외·성과 | 원문 미열람 |
| f4 | [사실] | Yang 외(IISE Transactions, 2026)는 협동 피킹을 로봇1–피커1, 로봇1–피커 다수, 피커1–로봇 다수, 피커 다수–로봇 다수의 네 모드로 나누고, 모드마다 포크–조인 대기행렬 네트워크(fork-join queueing network)와 피로–회복 모델로 투입할 피커 수와 로봇 수를 분석한다. | ref-469 | 아니오 | medium | 2026-03 | 피킹 / 수행 자원 | 원문 미열람 |
| f5 | [추정] | f1~f4 에 따르면 분류 원문의 질문(사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하기)은 인터페이스 단독이 아니라 구역·배치 구성, 피커와 로봇의 수 비율, 로봇 속도, 다음 작업 안내의 결합으로 풀리는 것으로 보이며, ROP 운영 인터페이스는 그 결정 결과(다음 대기 로봇 위치, 넘겨줄 배치)를 작업자에게 전달하는 접점이 될 것으로 보인다. | ref-467, ref-468, ref-469 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람 |
| f6 | [사실] | VDA 5050 최신판 상태(state) 메시지 스키마는 이동로봇의 운용 모드(operatingMode)를 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값으로 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f7 | [사실] | VDA 5050 최신판 명세는 SEMIAUTOMATIC 모드에서 로봇이 관제 주문을 받되 운영자가 로봇 HMI(Human-Machine Interface)로 실행을 확인해야 하고, INTERVENED 모드에서는 운영자가 HMI로 제어를 넘겨받아 새 주문을 받지 않으며, MANUAL 모드에서는 관제가 주문을 보낼 수 없다고 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | VDA 5050 최신판 상태 스키마는 안전 상태(safetyState)로 비상정지 종류(activeEmergencyStop: 로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범(fieldViolation)을 필수로 두고, 물리 버튼이나 즉시 동작으로 일시정지된 상태(paused)를 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF Web(rmf-web)은 Open-RMF 배치를 웹에서 시각화하고 제어하기 위한 패키지 모음으로, API 서버·API 클라이언트·대시보드 프레임워크로 구성된다. | ref-302 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 데모(rmf_demos)는 웹 대시보드에서 작업을 제출하고 로봇·작업 상태를 볼 수 있게 하며, 비상 경보(/fire_alarm_trigger 토픽)를 켜면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f11 | [사실] | ISO 3691-4:2023(제2판, 2020판 대체)은 무인 산업용 트럭과 그 시스템(차량, 제어 시스템, 하역 장치, 배터리 충전소, 적재물 인계 스테이션)의 안전 요구사항을 정하며, 사람 감지 설정·운전 모드·제동 같은 안전 기능 요구를 포함한다. | ref-470 | 아니오 | medium | 2023-06 | 제약 | 원문 미열람 |
| f12 | [사실] | ISO 10218-1:2025·ISO 10218-2:2025 개정판은 협동 적용(collaborative application) 안전 요구를 본문에 넣어 ISO/TS 15066 의 내용을 흡수하고, 기능 안전 요구를 명확히 하며 사이버보안 요구를 더했고, '협동로봇' 대신 '협동 적용'이라는 용어를 쓴다. | ref-471 | 아니오 | medium | 2025 | 제약 | 원문 미열람 |
| f13 | [사실] | ANSI/A3 R15.08 계열은 산업용 이동로봇(IMR)의 안전을 제조사 요구(1부), 현장 통합·적용 요구(2부, 2023), 사용자 책임(3부)으로 나누고, 2부는 IMR 또는 IMR 플릿을 현장에 통합·설정하는 요구를 정하며 조작기를 단 이동로봇(유형 C)까지 다룬다. | ref-472 | 아니오 | medium | 2023-10 | 제약 | 원문 미열람 |
| f14 | [사실] | 고용노동부·한국산업안전보건공단은 2023-07 '고정식·이동식 산업용 로봇의 협동작업 안전 가이드'를 배포해 감지기를 활용한 충돌방지 조치, 작업자의 안전한 이동·작업 방법, 충돌방지조치 점검표, 이동식 로봇 예시(완제품 이송 공정)를 제시했다. | ref-473, ref-474 | 아니오 | medium | 2023-07 | 제약 | 원문 미열람 |
| f15 | [사실] | 로봇신문 보도에 따르면 이 가이드는 로봇 이동 플랫폼이 비정상 작동할 때 긴급 정지할 수 있도록 작업자가 접근 가능한 위치에 비상정지장치를 두도록 한다. | ref-474 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f16 | [사실] | 중소벤처기업부·대구광역시 발표에 따르면 대구 이동식 협동로봇 규제자유특구 실증을 거쳐 이동식 협동로봇 안전기준 한국산업표준(KS)이 제정되었으며, 그 전에는 명확한 안전기준이 없어 작업공간 분리나 안전 울타리 설치가 필요했다. | ref-475 | 아니오 | medium | 2024-11 | 제약 | 원문 미열람 |
| f17 | [사실] | Das·Banerjee·Chernova(HRI 2021)는 계획 실행 중 예기치 않은 실패의 원인을 비전문가에게 설명하는 방식을 비교해, 실패의 맥락과 지난 행동 이력을 담은 설명이 비전문가의 실패·해결책 파악에 가장 효과적이었다고 보고한다. | ref-476 | 아니오 | medium | 2021-01 | 예외·성과 | 원문 미열람 |
| f18 | [사실] | 상황 인식 기반 에이전트 투명성(SAT) 모델은 에이전트의 현재 행동·계획(1수준), 추론(2수준), 미래 결과 예측(3수준)을 운영자에게 보여 주는 틀이며, 관련 연구에서 높은 수준의 투명성 화면이 운영자의 상황 인식과 신뢰를 높였다고 보고된다. | ref-477 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [사실] | 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수(팬아웃, fan-out)는 운영자가 방치해도 로봇 성과가 유지되는 정도(neglect tolerance)와 로봇 하나를 다루는 데 드는 상호작용 시간에 따라 정해진다는 척도가 제안되어 있다. | ref-478 | 아니오 | medium | 2004 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 독일 연방산업안전보건연구소(BAuA) 연구자의 문헌 고찰(Rey-Becerra·Wischniewski, Ergonomics, 2025)은 한 사람이 여러 로봇을 감독하는 시스템 연구 44건을 분석해 효율·유연성의 이점과 함께 주의·인지 부하 관리의 어려움을 지적하고, 설계·평가용 점검표를 제시했다. | ref-479 | 아니오 | medium | 2025-07-11 | 수행 자원 | 원문 미열람 |
| f21 | [추정] | 국내 물류 로봇 업체 플로틱스는 100평 규모 물류센터 환경에서 작업자 2명이 로봇 6대와 존피킹을 수행하는 구성을 시연했다고 보도되었다. | ref-480 | 아니오 | low | 2023-12-22 | 피킹 / 수행 자원 | 원문 미열람, 벤더 주장 |
| f22 | [사실] | 음성 피킹은 시스템이 위치와 수량을 음성으로 지시하고 작업자가 위치 체크 디지트·수량 같은 짧은 음성 응답으로 동작마다 확인하는 방식이다. | ref-272, ref-275 | 예 | medium | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람 |
| f23 | [추정] | Locus Robotics 는 협동 피킹 로봇 화면에 품목·위치·수량을 보여 주고 선택 기능으로 위치·용기 바코드 스캔 뒤 화면 확인을 받는다고 설명한다. | ref-279 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람, 벤더 주장 |
| f24 | [추정] | InOrbit 는 RobOps Copilot 을 2024년에 로봇 운영 데이터에 대한 자연어 질의·설명 기능으로 발표했다. | ref-176, ref-278 | 아니오 | low | 2024-05 | — | 원문 미열람, 벤더 주장 |
| f25 | [사실] | Rasa 3.x 의 폼(Forms)은 필요한 슬롯 목록을 정해 두고 비어 있는 필수 슬롯을 사용자에게 차례로 묻는 방식으로 작업 지향 대화의 되묻기를 구현한다. | ref-356 | 아니오 | medium | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f26 | [사실] | KnowNo(CoRL 2023)는 LLM 계획기의 선택지 불확실성을 등각 예측(conformal prediction)으로 재어 불확실할 때 사람에게 도움을 요청하게 하는 방법이다. | ref-351 | 아니오 | medium | 2023-07 | 시작 조건 | 원문 미열람 |
| f27 | [사실] | CLARA(IEEE RA-L 2024, 고려대 등)는 사용자 명령을 명확·모호·수행 불가로 분류하고 모호한 명령에는 되묻는 질문을 생성하는 방법이다. | ref-353 | 아니오 | medium | 2024 | 시작 조건 | 원문 미열람 |
| f28 | [사실] | SafeGate(Purdue, 2026)는 LLM 이 해석한 자연어 명령에서 안전 속성을 추출해 실행 전에 결정적 규칙으로 승인·거부하는 게이트를 제안하며, ISO 13482(개인 돌봄 로봇) 기반이고 물류 현장 평가는 없다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f29 | [추정] | 연계 대상: Mecalux 는 WMS(Easy WMS)의 생성형 AI 비서가 채팅 지시를 실행하기 전에 수행할 동작과 영향을 요약해 보여 주고 채팅으로 확인을 받는다고 설명한다. | ref-418 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람, 벤더 주장 |
| f30 | [추정] | f7·f22·f25~f29 를 나란히 놓으면 운영 인터페이스의 확인은 대상과 시점에 따라 로봇 동작 실행 전 운영자 확인(VDA 5050 SEMIAUTOMATIC), 작업자 동작마다의 확인(음성 체크 디지트), 자연어 지시의 해석 확인(되묻기·실행 전 게이트)으로 구분되는 것으로 보인다. | ref-031, ref-272, ref-275, ref-356, ref-417 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f31 | [추정] | 연계 대상: 사람 감지·보호 필드·비상정지 회로·속도와 거리 감시 같은 안전 기능은 로봇 제조사와 현장 통합사가 ISO 3691-4·ISO 10218·R15.08 에 따라 갖추는 것이므로, 이종 로봇을 연결하는 ROP 는 운용 모드·안전 상태의 표시, 작업 재개·수동 전환의 승인 흐름, 구역·권한 설정 반영을 맡는 경계가 될 것으로 보인다. | ref-470, ref-472, ref-051 | 아니오 | low | 2026-09-25 | 제약 | — |

### 근거 발췌

- **f1**: 검색 요약: 'handing over the completed batch to an AMR waiting at the cross aisle'; 구역당 피커 1명, 배치 구성과 배치 순서를 함께 결정(EJOR 298(1)). 원문 미열람.
- **f2**: 검색 요약: AMRs 'carry bins ... wait in front of shelves'; pickers 'continuously moving between different waiting AMRs without returning to the depot'; 목표 makespan 최소화(Transportation Science 57(4)). 원문 미열람.
- **f3**: 검색 요약: 'ripple effect caused by stochastic picking times can be effectively mitigated by separating the workforce into smaller subgroups'; 'slower AMRs deteriorate system performance'. 저자 계산 실험 결과. 원문 미열람.
- **f4**: 검색 요약: four modes (couple, SR-to-MP, SP-to-MR, multiple pickers to multiple robots); 'fork-join queuing network (FJQN) model' 과 'fatigue-recovery model'. IISE Transactions 58(3), 304-323. 교대조 단위 결정 여부는 요약에 없음. 원문 미열람.
- **f5**: f1(교차 통로 인계), f2(대기 AMR 사이 이동), f3(하위 집단·속도), f4(모드별 인원 투입)를 SCM 질문에 대응시킨 이 위키의 추론. 결합 방식을 제시한 단일 출처는 찾지 못함.
- **f6**: state.schema 원문: "operatingMode" description 'Current operating mode of the mobile robot.', enum 7개 값. (발행일 미확인, 확인일 기준)
- **f7**: 원문 열람 응답(요약 도구 경유): SEMIAUTOMATIC 'an operator must confirm execution via HMI before proceeding'; INTERVENED 'operator has taken control via HMI, overriding fleet control'. 문구가 도구 요약일 수 있어 명세 표와 글자 단위 대조는 미확인. (발행일 미확인, 확인일 기준)
- **f8**: state.schema 원문: activeEmergencyStop 'MANUAL: e-stop shall be acknowledged manually at the mobile robot. REMOTE: facility e-stop shall be acknowledged remotely.'; paused 'either because of the push of a physical button ... or because of an instantAction'. (발행일 미확인, 확인일 기준)
- **f9**: README 원문: 'a collection of packages that provide a web-based interface for users to visualize and control all aspects of Open-RMF deployments.' (발행일 미확인, 확인일 기준)
- **f10**: README 원문: 'All robots will get directed to the nearest parking spot when the emergency alarm is triggered.' 대시보드는 fleet adapter 의 server_uri 연결로 상태를 받음. (발행일 미확인, 확인일 기준)
- **f11**: 검색 요약: 2023-06 발행, 제1판(2020) 대체, 'active detection field'·'operational stop' 용어 추가. 적용 범위에 battery charging stations, load transfer stations 포함. 원문(유료) 미열람.
- **f12**: 검색 요약(A3 FAQ 등): 2011판 이후 첫 개정, 협동 적용 요구 통합·기능 안전 명확화·사이버보안 추가, 'cobot' 대신 'collaborative applications'. 표준 원문 미열람.
- **f13**: 검색 요약: Part 2 'specifies requirements for integrating, configuring, and customizing an IMR or fleet of IMRs into a site'; Type A/B/C. 원문 미열람.
- **f14**: 검색 요약: 가이드 구성 '로봇 사용 시 필요한 충돌방지 조치, 로봇 충돌방지조치 점검표, ... 이동식 로봇 충돌방지조치 예시(완제품 이송 공정)'. 기사는 같은 보도자료 기반이라 독립 교차 아님. 원문 미열람.
- **f15**: 검색 요약: '작업자가 접근 가능한 위치에 비상정지장치가 설치되어야 한다'. 가이드 원문 대조 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f16**: 검색 요약: '11월 1일부터 ... 안전기준에 관한 한국산업표준(KS)이 제정'; 표준은 적용범위·용어·안전 요구사항과 위험성 감소 대책 포함. KS 번호는 요약에 없음. 원문 미열람.
- **f17**: 검색 요약: 'explanations capturing the context of a failure and history of past actions are the most effective for failure and solution identification among non-experts'. 가정 환경 실험. 원문 미열람.
- **f18**: 검색 요약: Level 1 current actions and plans, Level 2 reasoning process, Level 3 projection of future outcomes; higher SAT interfaces → greater situation awareness and trust. 군사·다중 로봇 중재 연구 맥락. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f19**: 검색 요약: 'The number of robots that can be operated simultaneously is called the fan-out'; 'Robots that have high neglect tolerance and lower interaction time will achieve higher fan-out.' CHI 2004 논문. 원문 미열람.
- **f20**: 검색 요약: 658건 중 44건 분석; 'challenges in managing attention and cognitive load'; 'practical checklist for designing and evaluating SHMR systems'. 원문 미열람.
- **f21**: 벤더 주장: 기사 검색 요약 '100평 규모로 구현한 물류센터 환경에서 2명의 작업자가 6대 로봇과 함께 존피킹'. 실측 생산성 수치는 독립 확인 없음. 원문 미열람.
- **f22**: Lucas Systems 음성 지시 창고 자료와 VOCOLLECT 양수 미국 특허 US 8868519(위치 체크 디지트 불일치 경고)가 각각 기술. 두 출처 원문 미열람. (재인용: 2026-09-25-26)
- **f23**: 벤더 주장: LocusONE 사용자 인터페이스 페이지 요약. 원문 미열람. (재인용: 2026-09-25-26)
- **f24**: 벤더 주장: 2024-05 보도자료와 제품 페이지 요약. 미션 정의 방식과 실행 전 확인·승인 절차는 미확인. 같은 회사 자료라 독립 교차 아님. 원문 미열람. (재인용: 2026-09-25-21)
- **f25**: Rasa 문서 forms.mdx 요약: required_slots 를 채울 때까지 질문. 이번 실행에서 다시 열지 않음. (재인용: 2026-09-25-30)
- **f26**: Ren 외(2023) 'Robots That Ask For Help' 초록 요약. 가정·실험실 환경. 원문 미열람. (재인용: 2026-09-25-30)
- **f27**: Park 외(2024) 초록 요약: classifying and disambiguating user commands. 원문 미열람. (재인용: 2026-09-25-30)
- **f28**: Obi 외(2026-04) 초록 요약: pre-execution safety gate, task safety contracts. 성능은 저자 보고. 원문 미열람. (재인용: 2026-09-25-37)
- **f29**: 벤더 주장: Mecalux 뉴스 페이지 요약. WMS 쪽 사례이며 로봇 지시가 아님. 원문 미열람. (재인용: 2026-09-25-37)
- **f30**: 각 출처의 확인 방식을 대상(로봇 동작·작업자 동작·지시 해석)과 시점(실행 전·동작 중)으로 묶은 이 위키의 정리. 이 구분을 제시한 단일 출처는 찾지 못함.
- **f31**: f8(safetyState·paused 는 로봇이 보고), f11·f13(안전 기능은 차량·시스템·통합 요구)을 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 경계에 대응시킨 추론.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 2022 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 | 예 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 2023 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 | 예 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 2026-03 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 예 |
| ref-474 | 로봇신문 | '이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나? | 미확인 | 기사 | low | 2026-09-25 | https://www.irobotnews.com/news/articleView.html?idxno=32130 | 예 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 예 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2101.01625 | 예 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 미확인 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 예 |
| ref-478 | Olsen, D. R. 외(CHI 2004) | Fan-out: measuring human control of multiple robots | 2004 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/985692.985722 | 예 |
| ref-479 | Rey-Becerra, E., & Wischniewski, S. | Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance | 2025-07-11 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316 | 예 |
| ref-480 | ZDNet Korea | "대형 물류센터 집품 작업, 로봇 6대로 효율화" | 2023-12-22 | 기사 | low | 2026-09-25 | https://zdnet.co.kr/view/?no=20231222165139 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-272 | Lucas Systems | Voice-Directed Warehousing - Solutions \| Lucas Systems | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.lucasware.com/voice-directed-warehousing/ | 예 |
| ref-275 | USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.) | System and method for generating and updating location check digits (US 8868519) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519 | 예 |
| ref-279 | Locus Robotics | Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://locusrobotics.com/locusone/automated-warehouse-software/user-interface | 예 |
| ref-176 | InOrbit.AI | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 2024-05 | 벤더 문서 | low | 2026-09-25 | https://www.inorbit.ai/press/inorbit-robops-copilot | 예 |
| ref-278 | InOrbit.AI | InOrbit RobOps Copilot - Bring AI power to robot operations | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.inorbit.ai/robopscopilot | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux | 예 |

### 출처 요약

- **ref-467**: 원문 미열람. 구역별 피커가 배치를 채워 교차 통로의 AMR에 넘기는 AMR 보조 피킹에서 배치 구성·순서를 최적화한 EJOR 논문.
- **ref-468**: 원문 미열람. 선반 앞에서 기다리는 AMR과 여러 피커의 조율을 makespan 최소화로 다룬 Transportation Science 57(4) 논문.
- **ref-469**: 원문 미열람. 네 가지 사람–로봇 협동 피킹 모드를 포크–조인 대기행렬 네트워크와 피로–회복 모델로 분석해 피커·로봇 투입 수를 정하는 IISE Transactions 논문.
- **ref-470**: 원문 미열람. 무인 산업용 트럭(AGV·AMR)과 그 시스템의 안전 요구·검증 표준 제2판 소개 페이지.
- **ref-471**: 원문 미열람. ISO 10218-1/2:2025 개정의 주요 변경(협동 적용 통합, 기능 안전, 사이버보안)을 설명하는 로봇 산업 협회 자료.
- **ref-472**: 원문 미열람. 산업용 이동로봇 시스템·적용의 현장 통합 안전 요구(R15.08-2) 발행을 알리는 표준 개발 기관 공지.
- **ref-473**: 원문 미열람. 고용노동부·한국산업안전보건공단의 고정식·이동식 산업용 로봇 협동작업 안전 가이드 게시 자료.
- **ref-474**: 원문 미열람. 2023-07 이동식 산업용 로봇 안전 가이드의 충돌방지·비상정지 내용을 소개한 기사.
- **ref-475**: 원문 미열람. 대구 규제자유특구 실증을 거친 이동식 협동로봇 안전기준 KS 제정을 알린 보도자료.
- **ref-476**: 원문 미열람. 로봇 실행 실패를 비전문가에게 설명하는 설명 유형을 비교·자동 생성한 HRI 2021 논문의 프리프린트.
- **ref-477**: 원문 미열람. 에이전트의 행동·추론·예측을 세 수준으로 보여 주는 SAT 모델과 그 효과를 정리한 논문.
- **ref-478**: 원문 미열람. 한 사람이 동시에 다룰 수 있는 로봇 수(팬아웃)를 방치 허용도와 상호작용 시간으로 재는 척도를 제안한 논문.
- **ref-479**: 원문 미열람. 한 사람이 여러 로봇을 감독하는 시스템 연구 44건을 고찰하고 설계·평가 점검표를 낸 Ergonomics 논문(BAuA).
- **ref-480**: 원문 미열람. 플로틱스의 존피킹 로봇 시연(작업자 2명·로봇 6대)을 전한 기사.
- **ref-031**: VDA 5050 최신판(3.0.0) 명세 원문. 이번 실행에서 운용 모드별 설명과 일시정지 동작을 확인했다.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마 원본. 이번 실행에서 operatingMode·paused·safetyState 정의를 확인했다.
- **ref-302**: Open-RMF 배치를 웹에서 시각화·제어하는 패키지 모음(API 서버·클라이언트·대시보드)의 공식 README.
- **ref-104**: Open-RMF 데모 README. 이번 실행에서 웹 대시보드 연동과 비상 경보 시 로봇의 주차 위치 이동을 확인했다.
- **ref-272**: 원문 미열람. 음성 지시 창고 작업(음성 피킹)과 체크 디지트 확인 방식을 설명하는 벤더 자료.
- **ref-275**: 원문 미열람. 위치 체크 디지트 생성·갱신과 불일치 경고를 기술한 미국 특허 공보.
- **ref-279**: 원문 미열람. 협동 피킹 로봇의 작업자용 화면 인터페이스를 소개하는 벤더 페이지.
- **ref-176**: 원문 미열람. RobOps Copilot 발표 보도자료.
- **ref-278**: 원문 미열람. RobOps Copilot 제품 페이지.
- **ref-351**: 원문 미열람. 등각 예측으로 LLM 계획기의 불확실성을 재어 도움을 요청하게 하는 KnowNo 논문.
- **ref-353**: 원문 미열람. 사용자 명령을 명확·모호·수행 불가로 분류하고 되묻는 CLARA 논문.
- **ref-356**: 원문 미열람. 이번 실행에서 다시 열지 않았다. 필수 슬롯을 채울 때까지 되묻는 Rasa 폼 문서(참고문헌 목록 신뢰도 high, 이번 실행 미열람으로 medium 상한).
- **ref-417**: 원문 미열람. LLM 이 해석한 명령의 안전 속성을 실행 전 결정적 게이트로 판정하는 SafeGate 프리프린트.
- **ref-418**: 원문 미열람. WMS 의 생성형 AI 대화형 비서 기능을 알리는 벤더 뉴스.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f1·f2·f3·f5(사람 피커–로봇 대기 문제), f20(감독 인지 부하) / 4절 용어: f6·f7(운용 모드), f18(SAT), f19(팬아웃), f12(협동 적용) / 5절 시나리오: 피킹 단계 f1·f2·f3·f5·f22 (시작 조건·수행 자원·완료·인계·예외·성과), f21 은 벤더 주장 병기 / 6절 접근법: 협동 피킹 조율 f1~f4, 운용 모드·일시정지·비상정지 f6~f8, 관제 대시보드 f9·f10, 설명·투명성 f17·f18, 트랙 nl-task-chatbot 반영 제안 6건 검토 결과 f22~f30(음성 확인, 벤더 자연어 제품 f23·f24 벤더 주장, 되묻기 f25~f27, 실행 전 게이트 f28, WMS 연계 사례 f29, 확인 유형 정리 f30) — 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 7절 표준·오픈소스: f6~f8(VDA 5050), f9·f10(Open-RMF), f11(ISO 3691-4), f12(ISO 10218:2025), f13(R15.08), f14~f16(국내 가이드·KS) / 8절 연구·자료: f1~f4, f17~f20, 트랙 제안 자료 f25~f28 / 9절 범위: f31(안전 기능은 연계 대상, ROP 는 모드 표시·승인 흐름), f29(WMS 는 연계 대상) / 10절 연결: 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링(f1~f4), 3. 처리능력·거점·설비 계획(f4, oq-009), 9. 로봇·제조사 관제 연동(f6~f8), 20. 예외 복구·재계획·업무 연속성(f10·f17), 19. 모니터링·이상 탐지·원인 분석(f17·f18), 25. 안전·위험 관리(f11~f16), 27. AI·학습·적응과 모델 운영(f24~f28) / 11절 열린 질문: oq-009 와 새 질문 4건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 팬아웃 | Fan-out (human-robot team) | 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇의 방치 허용도와 로봇 하나를 다루는 상호작용 시간으로 추정한다. |
| 운용 모드 | Operating Mode (VDA 5050 operatingMode) | VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, 운영자 확인이 필요한지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다. |
| 상황 인식 기반 에이전트 투명성 | Situation Awareness-based Agent Transparency (SAT) | 자율 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주어 상황 인식과 신뢰를 돕는 인터페이스 설계 모델이다. |
| 협동 적용 | Collaborative Application | ISO 10218:2025 에서 로봇 자체가 아니라 사람과 로봇이 함께 일하도록 설계된 적용 방식을 기준으로 안전을 판단하기 위해 '협동로봇' 대신 쓰는 용어이다. |

## 열린 질문

새로 생긴 질문:

- 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 25. 안전·위험 관리 | 근거: f16 | 종류: 일반
- 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 4. 성과·경제성·프로세스 개선 | 근거: f5 | 종류: 일반
- VDA 5050 SEMIAUTOMATIC 모드의 실행 확인을 로봇 HMI 가 아닌 관제·ROP 화면에서 원격으로 할 수 있는지, 원격 확인에 필요한 안전 조건을 정한 규정이나 사례가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 9. 로봇·제조사 관제 연동 | 근거: f7 | 종류: 일반
- 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 19. 모니터링·이상 탐지·원인 분석 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 28 · 교차 확인: 1
- 예산 사용량: 검색 28회 · 신규 출처 14건
- 미확인 항목:
    - 이동식 협동로봇 안전기준 KS 번호와 본문 미확인(f16)
    - f7 운용 모드 설명은 요약 도구 경유 원문 열람이라 명세 표 문구와 글자 단위 대조 미확인
    - f11~f13 표준 원문(유료) 미열람, 검색 요약·발행 기관 소개 기준
    - f12 ISO 10218:2025 는 ISO 공식 페이지가 아닌 A3 자료 기준
    - ref-477 발행 연도 미확인(TIES 게재, 2017 온라인 공개 추정)
    - ref-478 공저자 전체 미확인
    - f21 플로틱스 시연 수치 벤더 주장, 독립 확인 없음
    - oq-009 부분 관련: f4 가 피커·로봇 수 결정 모델을 주지만 교대조 단위 결정 여부 미확인 — 해결 제안하지 않음
    - 특구 참여기업 생산성 9.3% 증가(검색 요약)는 단일 발표·방법 미공개라 finding 으로 내지 않음
- 범위 경계 위반 의심:
    - f31: 사람 감지·보호 필드·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 표시·승인 흐름만 맡는다고 구분
    - f29: WMS 화면 기능은 상위 업무 시스템 쪽 연계 대상으로 표시
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031(VDA 5050 명세)·ref-051(state.schema)·ref-302(rmf-web README)·ref-104(rmf_demos README). 신규 ref-467~ref-480(예약 구간 안)과 그 밖의 재사용 출처는 원문 미열람(신뢰도 상한 medium). 검색 28회/30, 신규 출처 14건/15. 트랙 반영 제안 6건 처리: 제안 1(InOrbit 등)→f24, 제안 2(음성·Locus 확인)→f22·f23·f30, 제안 3(자료)→f22~f24 출처 재사용(Amazon Proteus·Formant·다임리서치는 이번 브리프에 다시 넣지 않음, 다음 실행 후보), 제안 4·5(되묻기 방식·자료)→f25~f27, 제안 6(실행 전 확인)→f28·f29. 한국 자료: 고용노동부 가이드(f14·f15), 중기부 KS 제정(f16), 국내 업체 시연 기사(f21). 27. AI·학습·적응과 모델 운영 관련 finding(f24~f28)은 27번 영역과 양쪽 연결하도록 10절 제안에 적음. 8. 실시간 세계 상태·데이터 일관성, 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 원격 조작(teleoperation) 관련 공개 자료는 벤더 블로그 위주라 finding 으로 내지 못함 — 원격 조작은 섹션 6에서 약한 부분으로 남음.
