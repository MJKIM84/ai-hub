# 리서치 브리프 2026-09-25-86

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-86 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 5 · 답한 질문 q5-03

## 갭(비어 있거나 약한 섹션)

- 단계 5 질문 q5-03 열림(target.json 지정, CLI 지정 질문 id). 단계 5 페이지 3절에 q5-03 소제목 없음
- 완료 조건: 가설 판정표가 트랙 개요 3절에 없음(가설 1~3 모두 미판정, 판정 규칙도 정해지지 않음)
- 완료 조건: 사용자에게 제안하는 실험 계획이 실험 페이지에 없음(현재 제안된 실험 없음)
- 아이디어 2. 자연어 업무 지시 챗봇 6절에 가설 판정 절차(근거 확실성 평가와 판정 값 규칙) 없음
- 13. 작업 배정 — MRTA 섹션 6에 LLM 직접 배정과 결정적 해법 배정의 비교 근거를 가설 판정 관점으로 정리한 내용 없음
- 23. 시험·형식 검증·벤치마크 섹션 6에 여러 출처의 근거로 기술 가설을 판정하는 방법 근거 약함

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q5-03 가설 1~3은 단계 1~4의 결과로 어떻게 판정되는가?
3. 여러 출처의 근거로 결론의 확실성을 매기는 체계(GRADE)와 기술 성숙도(TRL)는 가설 판정의 규칙·보조 축으로 어떻게 쓸 수 있는가? (단계 5 페이지 3절, 23. 시험·형식 검증·벤치마크 겨냥)
4. 가설 1(작업 모델로 먼저 구조화하면 LLM 직접 명령 생성보다 잘못된 배정이 줄어든다)을 지지·반박하는 비교 연구(LLM 직접 배정 대 해법기 배정, 모듈형 구조 대 직접 코드 생성)는 무엇인가? (13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 겨냥)
5. 가설 2(온톨로지 질의로 로봇을 고르면 배정 근거를 설명·재현할 수 있다)의 근거와 반대 근거(선언 능력과 운용 능력의 차이, LLM 비결정성)는 무엇인가? (5. 로봇 능력·작업 온톨로지 연결)
6. 가설 3(스케줄링은 최적화 엔진, 해석·설명은 LLM)의 근거와 반례(LLM 이 설계한 규칙이 롤링 MILP 를 앞선 보고)는 무엇인가? (14. 작업 순서·스케줄링 연결)
7. 물류 현장 조건에서 세 가설을 직접 시험한 연구나 국내 자료가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | GRADE 접근법은 근거 묶음의 확실성을 결과(outcome)별로 높음·중간·낮음·매우 낮음 네 수준으로 매기고, 비뚤림 위험·비일관성·비직접성·비정밀성·출판 비뚤림 다섯 영역에서 심각한 우려가 있으면 한 단계, 매우 심각하면 두 단계 낮춘다. | ref-811 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | NASA 의 기술 준비 수준(TRL) 정의는 TRL 4 를 실험실 환경에서의 구성품·하위 시스템 검증으로, TRL 5 를 실제 조건을 가깝게 모사한 관련 환경에서의 검증으로 두어 통제된 실험실 검증과 관련 환경 검증을 구분한다. | ref-812 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f3 | [사실] | LiP-LLM 저자들은 LLM 이 기술 목록·의존 그래프를 만들고 배정은 선형계획이 맡는 구조에서, LLM 기반 배정은 추적 한계로 어려움을 겪었지만 선형계획 배정은 배정 실패가 거의 없었다고 보고했다. | ref-166 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f4 | [사실] | Garrabé 외(arXiv 2411.05474)는 LLM 출력을 기대 결과 모듈과 피드백으로 접지하는 모듈형 구조가 GPT-4o 기반 code-as-policies(직접 코드 생성) 기준선보다 픽앤플레이스·조작 과제 성공률이 높았다고 보고하고, 기준선 실패 원인으로 환경 접지 부족과 개루프 실행을 들었다. | ref-815 | 아니오 | medium | 2024-11 | — | 원문 미열람 |
| f5 | [사실] | Wang 외(EMNLP 2025)는 LLM 에이전트가 불명확한 지시에서 빠진 도구 호출 인자를 임의로 지어내는 경향을 보고했다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f6 | [사실] | CoMuRoS 는 작업 관리자 LLM 이 해석·배정·재계획을 맡는 구조로 22개 시나리오·약 20대 로봇 벤치마크에서 정답률 최대 0.91 을 보고했고, LTAA 는 LLM 배정의 우위를 두고 2차 요약끼리 충돌한다. | ref-677, ref-168 | 아니오 | medium | 2025-11 | — | 원문 미열람 |
| f7 | [사실] | Liu 외(KTH)는 기호 검증기를 같은 방식으로 프롬프트한 LLM 으로 바꾸면 전체 성공률이 98.1% 에서 3.8% 로 떨어졌다고 보고했다. | ref-674 | 아니오 | medium | 2026-06 | — | 원문 미열람 |
| f8 | [사실] | Electronics(2026) 논문은 온톨로지 기반 실행 가능성 판정 결과(ReasonerOutput)를 특정 배정기에 묶이지 않게 정형화해 세 가지 플릿 구성과 네 가지 배정기에서 공통 실행 가능성 제약으로 쓰였다고 보고했다. | ref-236 | 아니오 | medium | 2026-08-11 | 수행 자원 | 원문 미열람 |
| f9 | [사실] | 로봇 능력 온톨로지(RCO) 연구는 제조사가 광고한 능력과 측정한 운용 능력을 함께 표현하고 비교해, 선언 능력과 실제 성능이 다를 수 있음을 온톨로지 안에서 다룬다. | ref-041 | 아니오 | medium | 2025-10-02 | — | 원문 미열람 |
| f10 | [사실] | Atil 외는 결정적으로 설정한 LLM 5종을 8개 과제에서 10회 반복했을 때 정확도가 최대 15% 달라졌고 어느 모델도 모든 과제에서 반복 가능한 정확도를 내지 못했다고 보고했다. | ref-746 | 아니오 | medium | 2024-08 | — | 원문 미열람 |
| f11 | [사실] | ConstraintBench 저자들은 10개 운영과학 영역 200개 과제에서 가장 좋은 모델의 실행 가능 해 비율이 65.0% 였고 실행 가능성과 최적성을 함께 만족한 비율은 어느 모델도 30.5% 를 넘지 못했다고 보고했다. | ref-592 | 아니오 | medium | 2026-02 | — | 원문 미열람 |
| f12 | [사실] | SCHEDBench 저자들은 같은 스케줄링 문제를 의미가 같은 다른 문장으로 주면 LLM 의 실행 가능 비율이 떨어지고 제약 위반이 달라진다고 보고했다. | ref-594 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f13 | [사실] | Li·Li(arXiv 2608.09343)는 LLM 이 시뮬레이션 추적을 진단해 설계한 동적 생산·AGV 스케줄링 정책 가운데 최선 정책이 대응 시드 100개 모두에서 롤링 MILP·규칙·메타휴리스틱 정책보다 높은 점수를 냈고 무작위 고장에서도 재최적화 없이 우위를 유지했다고 보고했다. | ref-612 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f14 | [사실] | RACE-Sched 는 LLM 추론 지연이 산업 제어의 밀리초 단위 결정 주기와 맞지 않는다고 보고 실시간 디스패치를 저지연 기호 휴리스틱에 맡기는 구조를 제안했다. | ref-611 | 아니오 | medium | 2026-05 | — | 원문 미열람 |
| f15 | [사실] | RobotFleet 은 LLM 기반 추론과 혼합 정수 계획(MILP) 두 작업 배정기를 바꿔 끼울 수 있는 오픈소스 다중 로봇 계획 틀로, 논문은 MILP 배정기를 능력 제약 아래 로봇별 최대 작업 부하를 최소화하는 모델로 설명하며 공식 README 에는 두 배정기의 비교 결과가 없다. | ref-813, ref-814 | 아니오 | medium | 2025-10 | — | — |
| f16 | [추정] | q5-03 에 대해 이 위키가 확인한 근거 평가 체계를 묶으면, 각 가설을 하위 주장으로 나누고 하위 주장마다 근거의 확실성을 GRADE 식 영역(비직접성: 가정·건설·제조 대 물류 창고, 비정밀성: 단일 출처, 비뚤림: 저자·벤더 보고)으로 낮춰 매긴 뒤 판정 값으로 모으고 TRL 을 보조 축으로 병기하는 절차가 선택지로 보인다. | ref-811, ref-812 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f17 | [추정] | 판정 값은 지지(핵심 하위 주장 모두에 물류 조건의 직접 근거가 있고 확실성 중간 이상), 부분 지지(일부 하위 주장만 근거가 있거나 빠지는 조건이 확인됨), 기각(핵심 하위 주장에 직접 반대 근거), 미판정(핵심 하위 주장에 직접 근거 없음)으로 가르는 규칙이 가능해 보인다. | ref-811, ref-812 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f18 | [추정] | 위 규칙을 적용하면 가설 1 은 LLM 직접 배정·직접 코드 생성보다 구조화·분해 뒤 결정적 해법·검사를 거친 방식이 실패가 적었다는 비교가 있으나, 비교 형태가 이 트랙의 작업 모델 구조화와 같지 않고 LLM 직접 배정이 높은 정답률을 보인 반례가 있으며 물류 조건 근거가 없어 잠정 '부분 지지'(확실성 낮음)로 보인다. | ref-166, ref-815, ref-359, ref-677, ref-168, ref-674 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f19 | [추정] | 가설 2 는 온톨로지 판정을 배정기 독립 제약으로 쓰는 구조와 LLM 출력의 반복 불일치 보고가 있어 재현성 쪽 근거는 있으나, 온톨로지 질의와 LLM 선택의 설명 가능성·재현성을 같은 조건으로 잰 연구가 없고 선언 능력과 운용 능력이 다를 수 있어, 잠정 '부분 지지'(표현 수단과 재현성의 간접 근거만, 확실성 매우 낮음~낮음)로 보인다. | ref-236, ref-746, ref-041, ref-674 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f20 | [추정] | 가설 3 은 LLM 직접 스케줄링의 실행 가능성·일관성 한계와 LLM 지연 때문에 실시간 결정을 결정적 구성 요소에 두는 근거가 있으나, LLM 이 루프 밖에서 설계한 규칙이 롤링 MILP 를 앞선 보고가 있어 '최적화 엔진'을 해법기로만 읽으면 반례가 되고, 운영 안정성은 물류 운영에서 잰 자료가 없어 잠정 '부분 지지'(확실성 낮음)로 보인다. | ref-592, ref-594, ref-611, ref-612, ref-377 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f21 | [추정] | 판정을 부분 지지에서 옮기려면 같은 물류 지시 세트로 작업 모델 경유 대 LLM 직접 명령 생성의 오배정률(가설 1), 온톨로지 질의 대 LLM 선택의 반복 시행 일치율과 근거 추적 가능성(가설 2), 해법기·검증된 규칙 대 LLM 직접 스케줄의 실행 가능성·납기 지연·재스케줄 뒤 시작 시각 편차(가설 3)를 재는 사용자 실험이 필요할 것으로 보인다. | ref-746, ref-592, ref-734 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f22 | [추정] | 분류 원문 질문과 관련해 피킹 운반 지시 시나리오에서 가설 3 을 판정할 때 최근접 배정 기준선을 함께 두면, 결정적 배정·일정이 최근접 규칙보다 대기·지연을 줄이는지와 LLM 직접 스케줄의 격차를 한 실험에서 볼 수 있어 보인다(설명용 가정 사례). | ref-400, ref-592 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | 원문 미열람 |
| f23 | [추정] | 이번 검색 범위(한국어 2회 포함 9회)에서는 물류 창고 로봇 채팅 지시에서 세 가설을 직접 시험한 연구를 찾지 못했고, 국내 자료로는 제조 물류 로봇에 LLM 협업 인터페이스를 구축한 2023 학술대회 논문이 확인되나 내용을 확인하지 못해 판정 근거로 쓰지 못했다(부재 확인 아님). | ref-816 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 세 가설의 근거가 된 구성(구조화·결정적 검증·해법기 배정)은 확인한 범위에서 시뮬레이션·실험실 검증 수준에 머물러 TRL 로 보면 관련 환경(물류 현장 모사) 검증 전 단계로 보이며, 이 성숙도 축을 판정표에 병기할 수 있어 보인다. | ref-812, ref-674, ref-677 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: Cochrane Handbook 14장 검색 요약: 확실성을 'high', 'moderate', 'low', 'very low'로 결과별 분류, 다섯 영역 우려 시 한 단계(심각)·두 단계(매우 심각) 하향. (발행일 미확인, 확인일 기준)
- **f2**: 검색 요약: TRL 4 'Component/subsystem validation in laboratory environment', TRL 5 'validation in relevant environment'. (발행일 미확인, 확인일 기준)
- **f3**: 저자 보고, 독립 재현과 실험 조건 미확인(시뮬레이션 과제). (재인용: 2026-09-25-21)
- **f4**: 검색 요약: 'code-as-policy approach obtains a lower success rate'; 원인은 접지 부족과 개루프 실행(시뮬레이션·실기, 조작 과제 조건, 저자 보고).
- **f5**: 도구 호출 API 조건, 저자 보고. 필수 슬롯을 둔 작업 모델 구조화의 근거로 쓰일 수 있으나 배정 오류를 직접 잰 것은 아님. (재인용: 2026-09-25-30)
- **f6**: 실험실 텍스트 벤치마크 조건, 저자 보고. 결정적 배정기와 같은 조건의 비교는 미확인(LTAA 출처 충돌은 oq-030). (재인용: 2026-09-25-71)
- **f7**: 52개 명령 부분집합, 산업용 로봇 셀 조건, 저자 보고. (재인용: 2026-09-25-71)
- **f8**: 원문 미열람, 필드 구성·설명 가능성 측정 여부 미확인. (재인용: 2026-09-25-74)
- **f9**: Scientific Reports 2025, 원문 미열람. 선언 능력만으로 질의하면 배정 근거가 재현되어도 틀릴 수 있다는 반대 방향 근거(oq-024). (재인용: 2026-09-25-74)
- **f10**: arXiv 판 기준, 일반 NLP 과제 조건, 저자 보고. LLM 이 로봇을 직접 고를 때 재현성의 반대 근거. (재인용: 2026-09-25-99)
- **f11**: LLM 이 제약 최적화를 직접 푼 조건, 저자 보고, 원문 미열람. (재인용: 2026-09-25-66)
- **f12**: 자연어 조합 스케줄링 조건, 저자 보고, 원문 미열람. (재인용: 2026-09-25-66)
- **f13**: 검색 요약: 최선 평균 점수 62.49→78.61, 'outscored representative rolling-MILP, rule-based, and metaheuristic policies on every seed'. 제조·AGV 시뮬레이션 조건, 저자 보고.
- **f14**: 원문 미열람, 동적 스케줄링 조건. (재인용: 2026-09-25-77)
- **f15**: README(raw 열람): Task Allocator 가 'LLM-based reasoning' 과 'Mixed-Integer Linear Programming (MILP)' 을 제공, 평가 결과 없음. 논문 비교 수치는 미확인. 두 출처는 같은 저자.
- **f16**: 이 위키의 종합. 같은 날 건축 도면 자동 인식 트랙 단계 5(실행 2026-09-25-84)가 쓴 판정 절차와 같은 틀.
- **f17**: 이 위키의 종합. 판정 값 네 가지는 트랙 개요 3절의 값(지지/부분 지지/기각/미판정)을 따름.
- **f18**: 이 위키의 잠정 판정. 비직접성(가정·조작·산업 셀 조건)과 비정밀성(단일 출처·저자 보고)으로 두 단계 하향.
- **f19**: 이 위키의 잠정 판정. 설명 가능성 하위 주장은 직접 근거가 없어 미판정 상태로 남음.
- **f20**: 이 위키의 잠정 판정. 분담의 핵심을 '결정 루프 안은 결정적 실행기'로 읽으면 지지 방향, '해법기 전담'으로 읽으면 반례 존재.
- **f21**: 이 위키의 종합. q5-01 의 네 층 지표와 q5-02 의 가상 현장 시험 네 층을 실험 설계에 그대로 쓰는 안.
- **f22**: 작업장 사례 연구에서 조합 최적화 배차가 무작위·최근접 규칙보다 대기 시간을 잘 통제했다는 저자 보고(2019)를 기준선 설계 근거로 씀.
- **f23**: DBpia 서지 정보만 확인(대한산업공학회 추계학술대회 논문집 2023-11). 초록·결과 미확인.
- **f24**: 이 위키의 종합. TRL 매김은 공식 평가가 아니라 설명용 대응.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-811 | Cochrane | Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 | 예 |
| ref-812 | NASA ESTO | Definition Of Technology Readiness Levels | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://esto.nasa.gov/files/trl_definitions.pdf | 예 |
| ref-813 | Gupta, R. 외(RobotFleet 저자, arXiv 2510.10379) | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2510.10379 | 예 |
| ref-814 | therohangupta (RobotFleet 공식 저장소) | robot-fleet — RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/therohangupta/robot-fleet | 아니오 |
| ref-815 | Garrabé, É., Teixeira, P., Khoramshahi, M., & Doncieux, S. | Enhancing Robustness in Language-Driven Robotics: A Modular Approach to Failure Reduction | 2024-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2411.05474 | 예 |
| ref-816 | 강건(대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 2023-11 | 논문 | low | 2026-09-25 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 | 예 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21040 | 예 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.08214 | 예 |
| ref-592 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 2026-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.22465 | 예 |
| ref-594 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.00991 | 예 |
| ref-611 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 2026-05 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2605.29262 | 예 |
| ref-612 | Li, J., & Li, C.(소속 미확인) | LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.09343 | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | 논문 | medium | 2026-09-25 | https://www.nature.com/articles/s41598-025-16649-3 | 예 |
| ref-746 | Atil, B. 외 | Non-Determinism of "Deterministic" LLM Settings | 2024-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2408.04667 | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.22354 | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-734 | Rangsaritratsamee, R., Ferrell Jr., W. G., & Kurz, M. B.(Computers & Industrial Engineering 46) | Dynamic rescheduling that simultaneously considers efficiency and stability | 2004 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835203000950 | 예 |
| ref-400 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 2019 | 논문 | medium | 2026-09-25 | https://www.inderscience.com/info/inarticle.php?artid=103016 | 예 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 예 |

### 출처 요약

- **ref-811**: 원문 미열람. GRADE 로 결과별 근거 확실성을 네 수준으로 매기고 다섯 영역으로 낮추는 방법(실행 2026-09-25-84 의 ref-807 과 같은 URL).
- **ref-812**: 원문 미열람. TRL 1~9 정의, TRL 4 실험실 검증과 TRL 5 관련 환경 검증 구분(실행 2026-09-25-84 의 ref-809 와 같은 URL).
- **ref-813**: 원문 미열람. LLM 기반 계획과 LLM·MILP 배정기를 모듈로 둔 중앙 다중 로봇 계획 틀.
- **ref-814**: README 원문 열람. 배정기로 LLM 기반 추론과 MILP 를 제공하고 선언적 세계 상태를 유지하며, 평가 결과는 README 에 없음.
- **ref-815**: 원문 미열람. 기대 결과 모듈과 피드백을 둔 모듈형 구조가 GPT-4o code-as-policies 기준선보다 조작 과제 성공률이 높았다는 보고.
- **ref-816**: 원문 미열람. 제조 물류 로봇에 LLM 협업 인터페이스를 구축한 국내 학술대회 논문(서지만 확인).
- **ref-166**: 원문 미열람. LLM 이 기술 목록·의존 그래프를 만들고 선형계획이 배정하는 다중 로봇 계획.
- **ref-674**: 원문 미열람. 언어 이해만 LLM 에 맡기고 검증·순서·실행을 결정적으로 둔 구조와 기호 검증기 절제 실험.
- **ref-592**: 원문 미열람. LLM 이 제약 최적화를 직접 풀 때 실행 가능성·최적성을 평가한 벤치마크.
- **ref-594**: 원문 미열람. 문장 표현 변화에 따른 LLM 스케줄링 제약 충실도 평가.
- **ref-611**: 원문 미열람. 실시간 디스패치는 기호 휴리스틱, LLM 은 비동기 장기 추론을 맡는 구조.
- **ref-612**: 원문 미열람. LLM 이 시뮬레이션 추적으로 AGV·생산 스케줄링 정책을 설계하고 롤링 MILP 등과 비교.
- **ref-236**: 원문 미열람. 온톨로지 기반 실행 가능성 판정을 배정기 독립 제약으로 쓰는 방법.
- **ref-041**: 원문 미열람. 광고 능력과 운용 능력을 함께 표현·비교하는 로봇 능력 온톨로지.
- **ref-746**: 원문 미열람. 결정적 설정 LLM 의 반복 실행 정확도 변동 보고.
- **ref-359**: 원문 미열람. 불명확한 지시에서 LLM 에이전트가 빠진 인자를 지어내는 경향과 되묻기 틀.
- **ref-677**: 원문 미열람. 작업 관리자 LLM 이 해석·배정·재계획을 맡는 이종 로봇 팀 구조.
- **ref-168**: 원문 미열람. 건설 로봇 LLM 배정과 전통 최적화 비교(2차 요약 충돌, oq-030).
- **ref-734**: 원문 미열람. 재스케줄링의 효율(makespan·지연)과 안정성(시작 시각 편차)을 함께 다룸.
- **ref-400**: 원문 미열람. 조합 최적화 배차와 무작위·최근접 규칙의 작업 대기 시간 비교.
- **ref-377**: 원문 미열람. 이번 실행에서 다시 열지 않음. 로봇별 작업 순서를 정하는 결정적 작업 계획기.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md | 2, 3, 4, 5, 6, 8, 9 | q5-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24 (신뢰도 low) — 2절 q5-03 상태 답함, 3절 q5-03 소제목 신설({#q5-03}): 판정 절차(GRADE f1·f16, TRL 보조 축 f2·f24), 판정 값 규칙(f17, 표 권장), 가설별 근거(가설 1 f3~f7, 가설 2 f8~f10, 가설 3 f11~f15), 잠정 판정표(가설 1 부분 지지 f18, 가설 2 부분 지지 f19, 가설 3 부분 지지 f20, 표 권장), 필요 실험(f21), SCM 질문 연결·피킹 시나리오(f22), 근거 공백(f23) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황(가설 판정표·실험 계획 행) / 8절 출처 / 9절 이력 |
| update | docs/tracks/nl-task-chatbot/index.md | 3 | 트랙 산출물(가설 판정표): 검증이 승인하면 3절 판정 칸에 가설 1 부분 지지(f18)·가설 2 부분 지지(f19)·가설 3 부분 지지(f20)와 근거 단계·실행 id 2026-09-25-86 을 적고 판정 규칙(f17) 한 단락을 둔다. 승인되지 않으면 미판정 유지. |
| update | docs/ideas/nl-task-chatbot.md | 6 | 아이디어 페이지 6절(트랙 산출물): '가설 판정 절차' 소절 신설 — 근거 확실성 평가·TRL 보조 축(f1·f2·f16·f24), 판정 값 규칙(f17), 잠정 판정 요약(f18~f20), 필요 실험(f21). 모두 추정 중심 |
| update | docs/tracks/nl-task-chatbot/experiments.md | — | 트랙 산출물(단계 5 stage_artifacts): 제안 실험 후보 E5-01 작업 모델 경유 대 LLM 직접 명령 생성의 오배정률(가설 1), E5-02 온톨로지 질의 대 LLM 로봇 선택의 반복 일치율·근거 추적(가설 2), E5-03 해법기·검증된 규칙 대 LLM 직접 스케줄의 실행 가능성·납기 지연·시작 시각 편차, 최근접 기준선 포함(가설 3) — 근거 f21·f22, 시험 구성은 q5-02 가상 현장 네 층 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 6 | 트랙 nl-task-chatbot 단계 5 반영 제안 (f3, f13, f15, f20, f22): LLM 직접 배정 대 해법기 배정의 비교 근거와 LLM 설계 규칙이 롤링 MILP 를 앞선 반례, 최근접 기준선을 둔 판정 실험. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 6 | 트랙 nl-task-chatbot 단계 5 반영 제안 (f1, f2, f16, f17, f24): GRADE 식 확실성 평가와 TRL 보조 축으로 기술 가설을 판정하는 방법(추정) |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6 | 트랙 nl-task-chatbot 단계 5 반영 제안 (f4, f7, f10, f13): 모듈형 구조 대 직접 코드 생성, 결정적 검증기 절제, LLM 비결정성, 루프 밖 규칙 설계. 적용 대상 13. 작업 배정 — MRTA 와 함께 연결 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 절제 실험 | Ablation Study | 시스템의 한 구성 요소를 빼거나 다른 것으로 바꿔 성능 변화를 재어 그 구성 요소의 기여를 확인하는 실험이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 9회 · 신규 출처 6건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 가설 근거는 연구마다 단일 출처이며 RobotFleet 논문·README 는 같은 저자
    - f1·f2 GRADE·TRL 정의는 검색 요약 기준(원문 미열람)
    - f4 Garrabé 외 성공률 수치 미확인
    - f13 Li·Li 수치는 검색 요약 기준 저자 보고
    - f15 RobotFleet 논문의 LLM 대 MILP 비교 결과 미확인
    - f23 국내 학술대회 논문 초록·결과 미확인
    - f16~f22·f24 는 이 위키의 종합·잠정 판정이며 가설 판정 규칙을 직접 정한 출처는 없음
    - 물류 창고 조건에서 세 가설을 직접 시험한 자료는 검색 범위에서 찾지 못함
- 범위 경계 위반 의심:
    - f4: 조작 과제의 접지·재시도는 분류 원문 9장 로봇 자체 지능·제어 경계와 맞닿아 구조 비교 근거로만 씀
    - f13: 제조·AGV 스케줄링 시뮬레이션 근거라 물류 적용은 미확인으로 서술
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처는 신규 ref-814(RobotFleet README) 1건이며, 나머지 신규 5건과 재사용 15건은 원문 미열람이라 신뢰도 상한 medium(종합 finding 은 low). 검색 9회/40(한국어 2회), 신규 출처 6건/20(ref-811~ref-816, 예약 구간 안), 재사용 15건. ref-811·ref-812 는 실행 2026-09-25-84 의 ref-807·ref-809 와 같은 URL 이지만 입력 참고문헌 목록에 없어 새 id 로 적었다(퍼블리셔가 URL 로 합침). 질문 선택: target.json 지정 q5-03 1건. q5-03 은 판정 절차·규칙(f16·f17)과 가설별 근거(f3~f15)로 답했으나 잠정 판정(f18~f20)은 이 위키의 종합이고 물류 조건 직접 근거가 없어 질문 종합 신뢰도 low. 잠정 판정은 제안이며 트랙 개요 3절 반영은 검증 승인 뒤. 한국 자료: 국내 학술대회 논문 1건(서지만) 외 국내 사례 없음. 교차 규칙: LLM 방법 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA 양쪽에 반영 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 새 주장 없음. 정정 요청 없음. 새 일반 열린 질문 없음: 창고 조건 비교 실측은 oq-052, LTAA 충돌은 oq-030, 선언·운용 능력 차이는 oq-024 와 겹친다. 온톨로지 변경 없음: 가설 판정은 작업 모델의 개념·관계가 아니라 검증 방법이다. 후속 질문 2건. 페이지 제안: 트랙 산출물 4건(단계 페이지·트랙 개요 3절·아이디어 6절·실험), 세부영역 반영 제안 3건(갱신 상한과 별도). 이 실행도 단계 3·4 완료가 승인되지 않은 상태에서 지정된 질문으로 단계 5 를 다뤘다.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 5
- 답한 질문 id: q5-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 가설 판정표에서 '잘못된 배정'(가설 1), '설명·재현 가능'(가설 2), '운영 안정성'(가설 3)을 q5-01 의 어떤 지표와 문턱으로 조작적으로 정의해야 지지·부분 지지·기각을 가를 수 있는가? (q5-03 에서 파생) | 5 | f17 |
| — | LLM 이 루프 밖에서 설계한 규칙이 롤링 MILP 를 앞선 보고를 고려할 때, 가설 3 의 '최적화 엔진'을 해법기로 한정할지 검증을 거친 결정적 규칙 실행기까지 넓힐지, 그에 따라 스케줄링 분담 설계를 어떻게 바꾸는가? (q5-03 에서 파생) (관련: q4-08) | 3 | f13 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 가설 판정표(q5-03 답 f18~f20)는 검증 승인 전이며 트랙 개요 3절에 아직 반영되지 않음
    - 사용자에게 제안하는 실험 계획이 실험 페이지에 아직 없음(f21 후보만 제안)
    - 평가 지표·검증 절차 소절이 검증 승인 전 미충족 상태
    - 앞 단계 3·4 완료 미승인
    - 열린 질문 q5-04~q5-05, q5-07~q5-18
