# 리서치 브리프 2026-09-25-79

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-79 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 4 · 답한 질문 q4-01

## 갭(비어 있거나 약한 섹션)

- 단계 4 질문 q4-01 열림(target.json 지정, CLI 지정 질문 id). 단계 4 페이지는 seed 상태로 3~6·8절 비어 있음(단계 4 첫 실행)
- 완료 조건: 실행 전 검증 단계·명령 권한·제한 운영 기준을 담은 확인 절차 초안이 업무 분해·배정 설계 초안 6절과 아이디어 2. 자연어 업무 지시 챗봇 5절에 없음
- 업무 분해·배정 설계 초안 6절: '사용자 확인(승인)을 별도 개념으로 둘지, 배정의 속성(확인 여부)으로 둘지' 미해결(q4-01·q4-04 관련), 실행 2026-09-25-71 에서 개념 '검증 기록' 제안 미반영
- 13. 작업 배정 — MRTA 섹션 6에 배정 결과를 실행 전에 검증·확인하는 단계의 근거 없음
- 18. 사람–로봇 협업·운영 인터페이스 섹션 6에 승인 절차와 자동화 편향(승인 피로) 근거 약함
- 27. AI·학습·적응과 모델 운영 섹션 6에 LLM 출력의 실행 전 안전 가드레일(형식 논리 기반) 근거 약함

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q4-01 LLM의 잘못된 해석이 로봇 배정으로 이어지지 않게 하는 확인 절차는 어떻게 두는가?
3. LLM 로봇 계획·배정 출력을 실행 전에 거르는 가드레일(형식 논리 기반 안전 모듈, 규칙 추론기, 결정적 게이트)은 어느 단계에서 무엇을 검사하는가? (단계 4 페이지 3절, 27. AI·학습·적응과 모델 운영 겨냥)
4. LLM 에이전트 설계 지침·도구 규격(OWASP LLM Top 10, 모델 컨텍스트 프로토콜, LangChain 사람 참여 미들웨어)은 사람 확인을 어떤 행동에, 어떤 형태(승인·수정·거부)로 요구하는가? (18. 사람–로봇 협업·운영 인터페이스, 26. 사이버보안·접근권한·개인정보 연결)
5. 로봇 관제 인터페이스(VDA 5050, Open-RMF)에서 확인이 어느 시점 전에 끝나야 하며, 로봇·디스패처 쪽의 마지막 거절 장치는 무엇인가? (12. 명령·작업 실행의 신뢰성 연결)
6. 사람 승인은 실제로 오류를 걸러내는가 — 계획 승인·행동 확인의 사용자 연구, 자동화 편향과 이를 다루는 규제(EU AI Act 제14조, 한국 인공지능기본법 제34조)는 무엇을 말하는가? (25. 안전·위험 관리 연결, 한국 자료 우선 규칙)
7. 대화 시스템의 명시적·암시적 확인 방식은 확인 부담과 오류 교정 사이에서 어떻게 나뉘는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | OWASP LLM 애플리케이션 Top 10(2025판)의 과도한 에이전시(Excessive Agency) 항목은 원인을 과도한 기능·과도한 권한·과도한 자율성 셋으로 나누고, 대응으로 영향이 큰 행동 전 사람 승인, 최소 권한, 완전한 중재(complete mediation)를 든다. | ref-713 | 아니오 | medium | 2024-11 | — | — |
| f2 | [사실] | 모델 컨텍스트 프로토콜(MCP) 명세(2025-06-18판) 도구 절은 도구 호출을 거부할 수 있는 사람이 항상 루프에 있어야 한다고(SHOULD) 적고, 클라이언트가 민감한 작업에 사용자 확인을 묻고 서버 호출 전 도구 입력을 사용자에게 보여 주며 도구 사용 감사 기록을 남기도록 권고한다. | ref-714 | 아니오 | medium | 2025-06-18 | — | — |
| f3 | [사실] | LangChain 의 사람 참여(Human-in-the-Loop) 미들웨어는 설정한 도구 호출에서 에이전트 실행을 멈추고 사람이 승인(approve)·인자 수정(edit)·거부(reject, 피드백 포함)·직접 응답(respond) 가운데 하나로 결정하게 하며, 중단 상태를 보존하려면 체크포인터가 필요하다. | ref-715 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | Safety Chip(Yang 외, ICRA 2024)은 자연어로 준 금지 제약을 선형 시간 논리(LTL) 식으로 옮겨 오토마톤으로 두고, LLM 에이전트의 결정을 감시해 안전하지 않은 동작을 걸러내고 위반 이유를 설명·재프롬프트에 쓰는 질의 가능한 제약 모듈이며, VirtualHome 과 실제 로봇(Spot)에서 실험했다. | ref-716, ref-717 | 아니오 | medium | 2023-09 | — | — |
| f5 | [사실] | RoboGuard 는 미리 정한 안전 규칙을 신뢰 기반(root-of-trust) LLM 이 로봇 환경의 의미 그래프에 접지해 시간 논리 안전 명세를 만들고, 후보 계획(사람 또는 LLM 이 만든)과 명세가 충돌하면 시간 논리 제어 합성으로 해소하는 2단계 가드레일이며, 저자들은 탈옥 공격 조건에서 안전하지 않은 계획 실행을 92% 넘음에서 3% 미만으로 줄였다고 보고했다. | ref-718, ref-719 | 아니오 | medium | 2025-03 | — | — |
| f6 | [사실] | SafePlan 은 LLM 이 여러 로봇·사람에게 작업 계획, 팀 구성, 작업 배정을 만드는 시스템에서 프롬프트 건전성 추론기와 불변·전제·사후 조건 추론기로 자연어 지시, 작업 계획, 배정 결과의 안전성을 각각 검사하며, 저자들은 전문가가 만든 621개 지시 벤치마크에서 유해 작업 수용을 90.5% 줄였다고 보고했다. | ref-720 | 아니오 | medium | 2025-03 | — | 원문 미열람 |
| f7 | [사실] | SafeGate 는 자연어 명령의 안전 속성을 뽑아 결정적 판정으로 실행을 승인·거부하고, 통과한 명령을 불변 조건·가드·중단 조건으로 된 작업 안전 계약으로 분해하는 실행 전 게이트다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f8 | [사실] | Tang 외는 산업용 다중 로봇에서 에이전트의 제안을 결정적 검증과 원자적 반영(atomic commit)을 거쳐야만 작업 숲·관리형 블랙보드에 받아들이고 검증 기록을 남기는 구조를 제안했다. | ref-711 | 아니오 | medium | 2026-06 | — | 원문 미열람 |
| f9 | [사실] | Rasa 폼은 필수 슬롯을 정해 두고 비어 있는 다음 필수 슬롯을 사용자에게 묻고, 추출한 값을 사용자 정의 검증 동작으로 검사한다. | ref-356 | 아니오 | medium | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f10 | [사실] | VDA 5050 3.0.0 은 관제가 로봇에 풀어 준 베이스는 바꿀 수 없어 관제가 이를 이미 실행된 것으로 가정해야 하고 주문 취소도 통신 한계로 신뢰할 수 없다고 보며, 로봇은 수행할 수 없는 동작이 든 주문을 내부 버퍼에 받지 않고 INVALID_ORDER_ACTION 경고로 거절한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f11 | [사실] | Open-RMF 디스패처는 입찰 기간에 어떤 플릿 어댑터도 입찰하지 않으면 작업의 배정 상태를 FailedToAssign 으로 두고 오류를 기록하며, 그 작업은 수행되지 않는다. | ref-656 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f12 | [사실] | He·Demartini·Gadiraju(CHI 2025)는 LLM 에이전트를 계획 후 실행 방식으로 쓰는 일상 비서 과제(위험도가 다른 6개 과제, 참가자 248명, 시뮬레이션 환경)에서 사용자 참여를 조사해, 계획 품질이 높고 실행 단계 사용자 참여가 있을 때는 잘 작동하지만 그럴듯해 보이는 계획을 사용자가 쉽게 잘못 신뢰했다고 보고했다. | ref-721, ref-722 | 아니오 | medium | 2025-04 | — | — |
| f13 | [사실] | 컴퓨터 사용 에이전트의 사람 감독 전략(행동마다 확인, 위험 기반 선택적 승인, 계획 수준 감독)을 비교한 연구(arXiv 2604.04918)는 모든 전략에서 최종 공격 성공률이 상당히 남았고, 감독 전략은 문제 행동이 사용자에게 보이게 하는 데는 영향을 주었지만 보인 뒤 사용자가 멈추게 하는 데는 영향이 작았다고 보고했다. | ref-723 | 아니오 | low | 2026-04 | — | 원문 미열람 |
| f14 | [사실] | EU AI Act 제14조 제4항 (b)호는 고위험 AI 시스템을 감독하는 사람이 시스템 출력에 자동으로 의존하거나 과도하게 의존하는 경향(자동화 편향)을 계속 인식할 수 있게 설계하도록 요구한다. | ref-724, ref-725 | 예 | medium | 2024 | — | 원문 미열람 |
| f15 | [사실] | 한국 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법(법률 제20676호, 2025-01-21 제정) 제34조는 고영향 인공지능 사업자가 위험관리방안, 설명 방안, 이용자 보호 방안과 함께 사람의 관리·감독 조치를 이행하도록 정한다. | ref-726 | 아니오 | medium | 2025-01-21 | — | 원문 미열람 |
| f16 | [사실] | Sagawa(INTERSPEECH 2004)는 음성 대화 시스템의 오류 처리에서 명시적 확인, 최종 확인, 암시적 확인 세 방식을 비교해 사용자 만족과 효율을 평가했다. | ref-727 | 아니오 | low | 2004-10 | — | 원문 미열람 |
| f17 | [추정] | Mecalux 는 WMS 에 통합한 대화형 비서가 긴급 주문 출고 같은 WMS 작업을 채팅 요청으로 실행하되 실행 전에 동작과 영향 항목의 요약을 보여 주고 확인을 받는다고 밝힌다. | ref-418 | 아니오 | low | 2026-09-25 | 출하 / 시작 조건 | 원문 미열람, 벤더 주장 |
| f18 | [사실] | KnowNo 는 LLM 계획기가 낸 선택지 가운데 등각 예측으로 정한 문턱을 넘는 것이 둘 이상이면 사람에게 도움을 요청하고 하나면 스스로 실행한다. | ref-350 | 아니오 | medium | 2023-07 | — | 원문 미열람 |
| f19 | [추정] | q4-01 에 대해 확인한 자료를 이 위키가 묶으면, 확인 절차는 (1) 해석 게이트: 필수 슬롯·형식 검사와 불확실성 기준에 따른 되묻기, (2) 제약 게이트: 해석 결과·계획·배정을 안전 규칙·권한·능력 제약과 결정적으로 대조, (3) 사람 확인: 영향이 크거나 불확실할 때만 해석 요약을 승인·수정·거부로 받기, (4) 검증 뒤 기록과 함께 상태에 반영, (5) 디스패처·로봇 쪽의 마지막 거절(무입찰·수행 불가 동작 거절)의 다섯 겹으로 두는 구성이 근거가 가장 많은 것으로 보인다. | ref-356, ref-350, ref-716, ref-718, ref-720, ref-417, ref-713, ref-714, ref-715, ref-711, ref-656, ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f20 | [추정] | VDA 5050 에서 로봇에 풀어 준 베이스는 바꿀 수 없고 취소도 신뢰할 수 없으므로, 해석 확인은 배정 계산 전에, 배정 결과 확인은 배치(베이스 해제) 전에 끝나야 하며, 사람 확인이 필요한 작업은 확인이 날 때까지 배치를 보류하는 중단점(체크포인트)으로 두는 것이 선택지로 보인다. | ref-031, ref-715, ref-711 | 아니오 | low | 2026-09-25 | 제약 | — |
| f21 | [추정] | 사람 승인만으로는 오해석을 걸러내기 어렵다는 보고(그럴듯한 계획에 대한 잘못된 신뢰, 문제 행동이 보여도 멈추지 못함)와 자동화 편향 인식을 요구하는 규정을 보면, 결정적 게이트를 먼저 두고 사람 확인은 영향이 큰 작업에 한정해 해석 결과와 결정적 검사 결과의 차이를 드러내는 형태로 두는 편이 맞는 것으로 보인다. | ref-721, ref-722, ref-723, ref-724, ref-725, ref-713 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f22 | [추정] | 확인 방식은 작업의 영향도와 해석 불확실성에 따라 나누어, 위험 구역 진입·적재 화물 취소·일괄 정지 같은 영향이 큰 작업은 명시적 확인(승인 전 대기)으로, 일상적 운반 지시는 응답에 해석 결과를 되풀이해 보여 주는 암시적 확인으로 두는 차등 구성이 선택지로 보인다. | ref-727, ref-713, ref-714, ref-350 | 아니오 | low | 2026-09-25 | 제약 | — |
| f23 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 확인 화면이 사용자에게 로봇 선택 자체를 고르게 하기보다 해석한 업무(대상·장소·기한)와 디스패처가 쓴 배정 기준(가장 빨리 끝남 등)을 보여 주면, 사람은 해석 오류를 확인하고 배정의 전체 기준 일관성은 결정적 배정기가 지키는 분담이 가능해 보인다. | ref-656, ref-715, ref-714 | 아니오 | low | 2026-09-25 | 피킹 / 수행 자원 | — |
| f24 | [추정] | 피킹 구역 관리자가 채팅으로 '피킹 끝난 토트를 10시 전까지 2번 도크로'라고 지시하면, 해석 게이트가 대상·장소·기한 슬롯을 검사해 빠진 값을 되묻고, 제약 게이트가 지시자의 구역·작업 권한과 도크 도달 가능성을 대조한 뒤, 일상 운반이면 해석 요약을 응답에 보여 주고 바로 반영하며 다른 사람의 진행 작업 취소를 포함하면 명시적 승인을 받을 때까지 배치를 보류하는 흐름이 가능해 보인다(설명용 가정 사례). | ref-356, ref-714, ref-711, ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f25 | [추정] | 이번에 확인한 확인·가드레일 근거의 평가 환경은 가정 시뮬레이터·실험실 로봇, 일상 비서·컴퓨터 사용 에이전트, 음성 대화 시스템이었고, 물류 창고 로봇에 채팅으로 준 지시의 확인 절차를 평가한 연구와 국내 사례는 한국어 검색 3회를 포함한 검색 범위에서 찾지 못했다(부재의 확인은 아님). | ref-716, ref-718, ref-720, ref-722, ref-723 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: LLM06 문서: 세 원인(excessive functionality·permissions·autonomy). 대응: "require a human to approve high-impact actions before they are taken", 확장 기능 최소화, 사용자 맥락 실행.
- **f2**: tools.mdx 보안 고려: 서버는 입력 검증·접근 통제·호출 속도 제한, 클라이언트는 민감 작업 확인 요청·호출 전 입력 표시·결과 검증·시간 초과·감사 기록.
- **f3**: interrupt_on 설정에 든 도구 호출(파일 쓰기·SQL 실행 등)만 중단. 네 결정 유형. 체크포인팅 필요 명시(docs 저장소 human-in-the-loop.mdx). (발행일 미확인, 확인일 기준)
- **f4**: README: constraint_module 이 자연어→LTL 변환(lang2ltl 확장), precond 모듈이 계획 생성 중 제약 검사, VirtualHome·Spot 실험. 논문 요약: 위반 추론·설명과 불안전 동작 가지치기.
- **f5**: README: 입력 의미 그래프·규칙집·후보 계획, 출력 안전 명세·계획 평가, Clearpath Jackal 실험. 수치(>92%→<3%)는 arXiv 초록 요약 기준 저자 보고값(RA-L 2026 채택 표기).
- **f6**: 원문 미열람. 검색 요약: 형식 논리와 사고 연쇄 추론기 결합, 계획·팀 구성·배정 출력의 검토·수정·거부, 621 프롬프트–장면 쌍, 유해 작업 수용 90.5% 감소(저자 보고).
- **f7**: ISO 13482 기반 결정적 판정(개인 돌봄 로봇 표준이라 물류 적용 미확인). (재인용: 2026-09-25-71)
- **f8**: 검증 게이트 뒤 원자적 반영, 블랙보드에 제안·검증 기록 보관. (재인용: 2026-09-25-71)
- **f9**: 해석 단계 출력(슬롯)을 규칙으로 검사하는 결정적 구성 요소의 예. (재인용: 2026-09-25-71)
- **f10**: 6.1.2: base cannot be changed, 관제는 베이스 실행을 가정, 취소 절차도 unreliable. 6.1.4.3: 인상 높이 초과 등 수행 불가 동작 주문은 버퍼에 넣지 않고 오류 보고(공식 저장소 main 3.0.0).
- **f11**: Dispatcher.cpp: 무입찰 시 FailedToAssign 과 'No fleet adapters offered a bid' 오류. (재인용: 2026-09-25-74)
- **f12**: 저장소 README: 248명, 항공권 예약·카드 결제 등 6개 과제, 계획 단계·실행 단계 사용자 참여 비교, 그럴듯한 계획에 대한 잘못된 신뢰. 물류·로봇 조건 아님.
- **f13**: 원문 미열람. 검색 요약: Action Confirmation·Risk-Gated·Supervisory Co-Execution 비교, 개입 성공률은 낮았다고 요약되나 조건별 수치는 요약마다 달라 넣지 않음.
- **f14**: 원문 미열람. 조문 게재본 요약과 법학 논문(2502.10036) 요약이 모두 14(4)(b)의 자동화 편향 인식 요구를 적음. 물류 로봇 배정 AI 의 고위험 해당 여부는 미확인.
- **f15**: 원문 미열람. 검색 요약 기준 제34조 제1항에 '고영향 인공지능에 대한 사람의 관리·감독' 포함. 물류 로봇 배정 AI 의 고영향 해당 여부는 oq-105 로 미해결.
- **f16**: 원문 미열람. 검색 요약: CAMMIA 대화 시스템에서 explicit·final·implicit 확인 비교. 결과 수치와 우열은 확인하지 못해 넣지 않음.
- **f17**: 벤더 주장: 실행 전 동작·영향 요약 확인. WMS 제품 기능이라 ROP 에게는 연계 대상 사례. (재인용: 2026-09-25-37)
- **f18**: 불확실성에 따라 확인을 발동하는 기준의 사례. (재인용: 2026-09-25-74)
- **f19**: 이 위키의 종합. 다섯 겹을 한 번에 제시한 단일 출처는 찾지 못함. 근거 조건은 가정·실험실 로봇, 소프트웨어 에이전트, 로봇 관제 규격.
- **f20**: 베이스 불변·취소 불신(VDA 5050)과 중단·재개 체크포인트(LangChain), 검증 뒤 원자적 반영(Tang 외)을 대응시킨 추론.
- **f21**: 근거는 일상 비서·컴퓨터 사용 에이전트 조건. 물류 관제 요원의 승인 행동을 잰 자료는 찾지 못함.
- **f22**: 확인 방식 비교(대화 시스템), 영향 큰 행동 승인(OWASP), 민감 작업 확인(MCP), 불확실성 기준(KnowNo)을 대응시킨 추론. 영향도 기준 목록은 출처 없음.
- **f23**: 평가기 기반 자동 배정(Open-RMF)과 도구 입력 표시·수정 결정(MCP·LangChain)을 대응시킨 추론.
- **f24**: 설명용 가정 사례. 슬롯 검사(Rasa), 접근 통제·확인(MCP), 검증 뒤 반영(Tang 외), 베이스 해제 전 확인(VDA 5050)을 조합.
- **f25**: 한국어 검색 결과는 해외 논문 번역 페이지와 법령 해설뿐이었음. 검색 범위 관찰.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-713 | OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub) | LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md) | 2024-11 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md | 아니오 |
| ref-714 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Server Features: Tools (docs/specification/2025-06-18/server/tools.mdx) | 2025-06-18 | 표준 | medium | 2026-09-25 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx | 아니오 |
| ref-715 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://docs.langchain.com/oss/python/langchain/human-in-the-loop | 아니오 |
| ref-716 | Yang, Z. 외(Brown University H2R Lab) | Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.09919 | 예 |
| ref-717 | YzyLmc (Safety Chip 공식 저장소) | ltl_safety — README (Plug in the Safety Chip) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/YzyLmc/ltl_safety | 아니오 |
| ref-718 | RoboGuard 저자(KumarRobotics, arXiv 2503.07885) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-719 | KumarRobotics (RoboGuard 공식 저장소) | RoboGuard — Safety guardrails for LLM-enabled robots (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/KumarRobotics/RoboGuard | 아니오 |
| ref-720 | SafePlan 저자(arXiv 2503.06892, 저자 미확인) | SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.06892 | 예 |
| ref-721 | RichardHGL (CHI 2025 Plan-then-Execute 공식 저장소) | CHI2025_Plan-then-Execute_LLMAgent — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/RichardHGL/CHI2025_Plan-then-Execute_LLMAgent | 아니오 |
| ref-722 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 2025-04 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/3706598.3713218 | 예 |
| ref-723 | arXiv 2604.04918 저자(미확인) | Comparing Human Oversight Strategies for Computer-Use Agents | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.04918 | 예 |
| ref-724 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 14: Human Oversight \| EU Artificial Intelligence Act | 2024 | 정부·연구기관 | medium | 2026-09-25 | https://artificialintelligenceact.eu/article/14/ | 예 |
| ref-725 | arXiv 2502.10036 저자(미확인) | Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI | 2025-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2502.10036 | 예 |
| ref-726 | 국가법령정보센터(법제처) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 (법률 제20676호, 2025-01-21) | 2025-01-21 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 예 |
| ref-727 | Sagawa, H. (INTERSPEECH 2004) | A comparison of confirmation styles for error handling in a speech dialog system | 2004-10 | 논문 | medium | 2026-09-25 | https://www.isca-archive.org/interspeech_2004/sagawa04_interspeech.pdf | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://robot-help.github.io/ | 예 |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux | 예 |
| ref-656 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 예 |
| ref-711 | Tang, G. 외(arXiv 2606.31339) | Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.31339 | 예 |

### 출처 요약

- **ref-713**: 과도한 에이전시의 세 원인(기능·권한·자율성)과 사람 승인·최소 권한·완전한 중재 같은 대응을 정리한 OWASP 프로젝트 문서.
- **ref-714**: MCP 도구 명세. 도구 호출을 거부할 수 있는 사람 참여, 민감 작업 확인, 호출 전 입력 표시, 입력 검증·접근 통제·감사 기록을 권고한다.
- **ref-715**: 설정한 도구 호출에서 실행을 멈추고 승인·수정·거부·응답 결정을 받는 미들웨어 문서. 체크포인터가 필요하다.
- **ref-716**: 원문 미열람. 자연어 제약을 LTL 오토마톤으로 바꿔 LLM 로봇 에이전트의 불안전 동작을 걸러내는 모듈(ICRA 2024).
- **ref-717**: Safety Chip 코드 저장소. 자연어→LTL 제약 모듈, 전제 조건 검사, VirtualHome·Spot 실험 구성.
- **ref-718**: 원문 미열람. 신뢰 기반 LLM 으로 안전 규칙을 환경에 접지해 시간 논리 명세를 만들고 제어 합성으로 불안전 계획을 해소하는 2단계 가드레일.
- **ref-719**: 의미 그래프·규칙집·후보 계획을 받아 안전 명세를 만들고 계획을 평가하는 구현. SPINE 계획기·Jackal 로봇과 연동.
- **ref-720**: 원문 미열람. 지시·계획·팀 구성·배정 출력을 불변·전제·사후 조건 추론기로 검사하는 틀과 621개 지시 벤치마크.
- **ref-721**: 계획 후 실행 LLM 에이전트 사용자 연구(248명, 6개 과제)의 저장소. 그럴듯한 계획에 대한 잘못된 신뢰를 요약한다.
- **ref-722**: 원문 미열람. CHI 2025 논문. 계획·실행 단계 사용자 참여가 신뢰와 팀 성과에 주는 영향을 조사.
- **ref-723**: 원문 미열람. 행동 확인·위험 기반 승인·계획 수준 감독 전략을 비교한 사용자 연구. 모든 전략에서 공격 성공이 상당히 남음.
- **ref-724**: 원문 미열람. EU AI Act 제14조(사람의 감독) 조문 게재본. 공식 관보(EUR-Lex) 판이 아님.
- **ref-725**: 원문 미열람. EU AI Act 제14조의 자동화 편향 인식 요구의 법적 함의를 분석한 논문.
- **ref-726**: 원문 미열람. 한국 인공지능기본법. 제34조가 고영향 인공지능 사업자의 위험관리·설명·이용자 보호·사람의 관리·감독 조치를 정한다.
- **ref-727**: 원문 미열람. 음성 대화 시스템에서 명시적·최종·암시적 확인 방식을 비교한 연구.
- **ref-031**: VDA 5050 3.0.0 명세(공식 저장소 main). 베이스·호라이즌, 주문 거절, 취소 규칙.
- **ref-350**: 원문 미열람. 등각 예측 기반으로 불확실할 때 사람에게 도움을 요청하는 LLM 계획기 프로젝트 페이지(이번 실행 재열람 안 함).
- **ref-356**: 원문 미열람. 필수 슬롯 질문과 추출 값 검증을 다루는 Rasa 폼 문서(이번 실행 재열람 안 함).
- **ref-417**: 원문 미열람. 자연어 명령의 안전 속성을 결정적으로 판정하는 실행 전 게이트와 작업 안전 계약.
- **ref-418**: 원문 미열람. WMS 대화형 비서가 실행 전 요약을 보여 주고 확인을 받는다는 벤더 발표.
- **ref-656**: 원문 미열람. Open-RMF 디스패처 구현. 무입찰 시 FailedToAssign 기록(이번 실행 재열람 안 함).
- **ref-711**: 원문 미열람. 에이전트 제안을 결정적 검증과 원자적 반영을 거쳐 받아들이는 관리형 블랙보드 구조.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | 2, 3, 4, 5, 6, 8, 9 | q4-01 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25 (신뢰도 low) — 2절 q4-01 상태 답함, 3절 q4-01 소제목 신설({#q4-01}): 에이전트 설계 지침·도구 규격의 사람 확인(OWASP f1, MCP f2, LangChain f3), 로봇 가드레일(Safety Chip f4, RoboGuard f5, SafePlan f6 — 배정 출력 검사 포함, SafeGate f7), 검증 뒤 반영(f8), 해석 게이트(f9·f18), 로봇·디스패처 쪽 마지막 거절과 베이스 불변(f10·f11), 사람 승인의 한계(f12·f13)와 규제(EU AI Act f14, 한국 인공지능기본법 f15), 확인 방식(f16), 벤더 사례(f17 벤더 주장), 종합: 다섯 겹 확인 절차(f19, mermaid 흐름 권장)·확인 시점(f20)·사람 확인 한정(f21)·차등 확인 방식(f22)·SCM 질문 연결(f23)·피킹 시나리오(f24)·근거 공백(f25) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 5 | 아이디어 페이지 5절(트랙 산출물): '오해석 방지 확인 절차' 소절 신설 — 다섯 겹 확인 절차 f19, 확인 시점 f20, 사람 확인 한정과 자동화 편향 f21, 차등 확인 방식 f22(모두 추정), 근거 f1·f2·f3·f4·f5·f6·f10·f12·f13·f14. 명령 권한(q4-03)·제한 운영 기준(q4-04)은 미조사임을 명시 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes(개념 '사용자 확인' 추가)가 승인되면 2절 반영과 초안 버전 인상(f2·f3·f16·f19·f22). 미승인 시 6절 '사용자 확인(승인)을 별도 개념으로 둘지, 배정의 속성(확인 여부)으로 둘지' 질문에 q4-01 답(f19·f20) 연결, 실행 2026-09-25-71 의 '검증 기록' 질문과의 경계 메모 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f6, f10, f11, f19, f23): LLM 배정 출력의 실행 전 검사(SafePlan), 디스패처 무입찰·로봇 수행 불가 거절을 마지막 거절 장치로, 확인 화면에 배정 기준을 보이는 분담과 분류 원문 질문 연결. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f3, f12, f13, f16, f21, f22): 승인·수정·거부 확인 인터페이스, 계획 승인 사용자 연구와 감독 전략 비교에서 드러난 사람 승인의 한계, 명시적·암시적 확인의 차등 적용 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6, 8 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f4, f5, f6, f14, f15): LLM 로봇 계획의 형식 논리 가드레일(Safety Chip, RoboGuard, SafePlan), 자동화 편향 인식 요구(EU AI Act 제14조)와 인공지능기본법 제34조 사람의 관리·감독. 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결 |
| update | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md | 6 | 트랙 nl-task-chatbot 단계 4 반영 제안 (f1, f2): 과도한 에이전시의 세 원인과 최소 권한·완전한 중재, MCP 도구 명세의 접근 통제·감사 기록 권고(q4-03 명령 권한 조사와 이어짐) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 과도한 에이전시 | Excessive Agency | LLM 기반 시스템이 필요 이상의 기능·권한·자율성을 가져 잘못되거나 조작된 출력이 해로운 행동으로 이어지는 위험으로, OWASP LLM Top 10(2025)의 한 항목이다. |
| 자동화 편향 | Automation Bias | 사람이 자동화 시스템의 출력이나 권고를 충분히 따져 보지 않고 과도하게 믿고 따르는 경향으로, 사람 승인 절차를 형식적 확인으로 만들 수 있다. |
| 명시적 확인·암시적 확인 | Explicit / Implicit Confirmation | 대화 시스템이 이해한 내용을 사용자에게 직접 물어 승인받는 방식(명시적)과, 다음 응답 속에 이해한 내용을 되풀이해 보여 주고 사용자가 고치지 않으면 진행하는 방식(암시적)이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - f5 RoboGuard 수치(>92%→<3%)는 arXiv 초록 요약 기준 저자 보고값, 원문 미열람
    - f6 SafePlan 수치(90.5%, 621개)는 검색 요약 기준 저자 보고값, 저자 목록 미확인
    - f13 감독 전략 비교 연구의 조건별 수치는 요약마다 달라 넣지 않음, 저자 미확인
    - f16 Sagawa 2004 의 비교 결과(우열·수치) 미확인
    - f14 EU AI Act 조문은 공식 관보(EUR-Lex)가 아닌 게재본·논문 요약 기준
    - f15 인공지능기본법 제34조 조문 문구는 검색 요약 기준, 시행령의 구체 조치 미확인, 물류 배정 AI 의 고영향 해당 여부 미확인(oq-105)
    - f19~f25 는 이 위키의 종합이며 다섯 겹 확인 절차를 한 번에 제시한 단일 출처는 찾지 못함
    - 물류 창고 로봇 채팅 지시의 확인 절차 평가 연구·국내 사례 부재는 검색 범위 관찰
- 범위 경계 위반 의심:
    - f10: 로봇의 주문 거절은 로봇 쪽 기능(연계 대상)이며, ROP 는 거절 오류를 받아 확인 절차의 마지막 결과로 다루는 쪽만 서술하도록 제안
    - f4·f5: 로봇 쪽 안전 모듈·가드레일 연구는 가정·실험실 로봇 조건이며, 보호 정지 같은 안전 기능 자체는 로봇·통합자 쪽 연계 대상. ROP 는 작업·배정 수준의 제약 대조만 맡는 것으로 서술
    - f17: WMS 대화형 비서는 상위 업무 시스템 제품 기능(연계 대상) 사례로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 신규 출처: ref-713(OWASP LLM06)·ref-714(MCP 도구 명세)·ref-715(LangChain HITL 문서)·ref-717(Safety Chip README)·ref-719(RoboGuard README)·ref-721(CHI 2025 저장소 README). ref-031 은 입력 원문 텍스트(inbox). 나머지 신규 9건(ref-716·ref-718·ref-720·ref-722~ref-727)과 재사용 ref-350·ref-356·ref-417·ref-418·ref-656·ref-711 은 이번 실행에서 원문을 열지 않아 신뢰도 상한 medium. 원문을 연 출처도 공통 규칙 0절 6항에 따라 high 를 주지 않음. 검색 18회/40(한국어 3회), 신규 출처 15건/20(ref-713~ref-727, 예약 구간 안), 재사용 7건. 질문 선택: target.json 지정 q4-01 1건. q4-01 은 에이전트 설계 지침·도구 규격의 사람 확인(사실), 로봇 가드레일 연구(사실), 로봇 관제의 확인 시점 제약(사실), 사람 승인의 한계와 규제(사실)로 답했으나 다섯 겹 확인 절차·확인 시점·차등 확인(f19~f24)은 이 위키의 종합이고 근거가 물류 플릿 조건이 아니라 질문 종합 신뢰도 low. 교차 확인은 f14 1건(EU AI Act 제14조 제4항 (b)호, 게재본과 법학 논문 요약). 한국 자료: 인공지능기본법 제34조(ref-726); 국내 물류 사례는 찾지 못함. 교차 규칙: LLM 가드레일·확인 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스 양쪽에 반영 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(모의 실행 검증은 q4-02 범위로 남김). 정정 요청 없음. 새 일반 열린 질문 없음: 고영향 AI 해당 여부는 기존 oq-105, 배정 실패의 상위 반환은 oq-114 와 겹친다. 후속 질문 3건, 온톨로지 변경 제안 1건. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 4건(갱신 상한과 별도). 백로그 참고: q4-09·q4-10, q3-12·q3-13, q3-09·q3-10, q5-05·q5-06, q1-05·q1-06 중복 등록 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 4
- 답한 질문 id: q4-01

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 물류 지시에서 사람의 명시적 확인이 필요한 영향이 큰 작업(위험 구역 진입, 적재 화물 취소·되돌림, 일괄 정지, 다른 사람의 진행 작업 우선순위 변경 등)과 암시적 확인으로 충분한 일상 작업을 어떤 기준으로 가르고, 그 기준 목록은 누가 정하고 갱신하는가? (q4-01 에서 파생) (관련: q4-04) | 4 | f22 |
| — | 현장 안전·권한 규칙(금지 구역, 시간대 제한, 적재 제한)을 Safety Chip·RoboGuard 처럼 시간 논리 제약으로 옮겨 작업·배정 수준에서 대조하려면, 규칙을 공간 그래프·로봇 기능 온톨로지의 어떤 개념으로 표현해야 하는가? (q4-01 에서 파생) | 4 | f5 |
| — | 물류 지시 시나리오에서 관제 요원의 승인 지연 시간·거부율·수정률을 재어 승인 피로와 자동화 편향이 나타나는지, 확인 요약에 결정적 검사 결과를 함께 보이면 잘못된 지시를 멈추는 비율이 달라지는지를 어떤 실험으로 측정하는가? (q4-01 에서 파생) | 5 | f21 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| add | concept | 사용자 확인 (Confirmation) | f2, f3, f16, f19 | 해석 결과·배정·지시 변경을 실행 전에 사람이 확인한 기록. 속성 후보: 확인 대상(해석 결과 / 배정 / 지시 변경), 확인 방식(명시적 / 암시적, f16), 응답(승인 / 수정 / 거부, f3), 확인자, 확인 시각, 보여 준 입력 요약(f2). 초안 6절 질문 '사용자 확인을 별도 개념으로 둘지, 배정의 속성(확인 여부)으로 둘지'에 대한 제안이며 배정 속성 '확인 여부'와 겹친다. 실행 2026-09-25-71 에서 반영되지 않은 '검증 기록'(결정적 검사 기록)과는 사람 확인만 담는 것으로 경계를 나누는 안이다. 확인이 필요한 작업의 기준(f22)은 추정이라 정의에 넣지 않는다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 확인 절차 초안(이번 q4-01 답 f19·f20)은 검증 승인 전이며 업무 분해·배정 설계 초안 6절과 아이디어 2. 자연어 업무 지시 챗봇 5절에 아직 반영되지 않음
    - 명령 권한(q4-03)과 제한 운영 기준(q4-04) 미조사
    - 열린 질문 q4-02~q4-12(q4-09·q4-10 중복 정리 필요)
