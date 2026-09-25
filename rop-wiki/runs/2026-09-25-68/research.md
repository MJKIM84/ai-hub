# 리서치 브리프 2026-09-25-68

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-68 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 27. AI·학습·적응과 모델 운영 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(LLM 에이전트·환각은 용어집에 있으나 등각 예측·AI 관리 시스템·모델 레지스트리 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 반영 제안 6건 대기)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 반영 제안 8건 대기)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음(교차 규칙 적용 대상 5·6·13·19·21 연결 필요)
- 섹션 11. 열린 질문 비어 있음(oq-030 걸려 있음)

## 조사 질문

1. AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
2. AI 시스템의 위험 관리·거버넌스를 다루는 표준·법(NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, EU AI Act, 한국 인공지능 기본법)은 무엇을 요구하며 로봇 운영 AI에 어떻게 걸리는가? (섹션 3·7·9 겨냥)
3. LLM 이 만든 계획·해석을 실행 전에 접지·검증하고 불확실할 때 사람에게 묻는 방법(SayCan, LLM+P, Code as Policies, KnowNo, SafeGate)은 무엇인가? (섹션 4·6·8 겨냥, 트랙 nl-task-chatbot 반영 제안 확인)
4. 창고 다중 로봇 작업 배정에 학습 기반 방법(강화학습)은 어떻게 쓰이며 어떤 성능이 보고되는가? (섹션 6·8·10 겨냥, 교차 규칙상 13. 작업 배정 — MRTA)
5. 운영 중인 학습 모델의 변경·버전·시험·감시를 관리하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)
6. oq-030 LTAA(arXiv 2512.02810)의 LLM 배정 완료율 77% 주장과 동적 계획법 우위라는 2차 요약 중 어느 쪽이 원문 결과인가?
7. 국내 물류 현장에서 AI 예측·계획을 운영에 쓴 사례와 국내 규제 요구는 무엇인가? (섹션 3·5 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST 는 2023-01-26 AI 위험관리 프레임워크(AI RMF 1.0)를 자율 적용 프레임워크로 발표했으며, 핵심은 거버넌스(Govern)·맵(Map)·측정(Measure)·관리(Manage) 네 기능이고 거버넌스가 나머지 세 기능을 가로지른다. | ref-586 | 아니오 | medium | 2023-01-26 | — | 원문 미열람 |
| f2 | [사실] | ISO/IEC 42001:2023 은 AI 시스템을 개발·제공·사용하는 조직이 AI 관리 시스템(AIMS)을 수립·실행·유지·지속 개선하기 위한 요구사항을 정하는 관리 시스템 표준이다. | ref-592 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f3 | [사실] | ISO/IEC 23894:2023 은 ISO 31000 의 위험관리 원칙을 AI 에 맞게 적용한 지침으로, AI 를 개발·배치·사용하는 조직이 위험 평가·처리·감시·검토·기록을 AI 관련 활동에 통합하도록 안내한다. | ref-593 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f4 | [사실] | 한국의 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI 를 고영향 인공지능으로 두어 별도 책무를 부과한다. | ref-594 | 아니오 | medium | 2026-01-22 | 제약 | 원문 미열람 |
| f5 | [사실] | EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I 의 EU 조화 법령(기계류 등)이 적용되는 제품의 안전 구성요소로 쓰이며 제3자 적합성 평가를 받아야 하는 AI 시스템을 고위험 AI 로 분류한다. | ref-595 | 아니오 | medium | 2024-06-13 | 제약 | 원문 미열람 |
| f6 | [사실] | SayCan 은 LLM 이 상위 지시에 유용한 행동을 고르는 과제 접지(Say)와, 사전 학습된 기술의 가치 함수가 현재 실행 가능성을 판정하는 세계 접지(Can)를 곱해 실행 가능하고 맥락에 맞는 기술만 선택하게 한다. | ref-088 | 아니오 | medium | 2022-04 | — | 원문 미열람 |
| f7 | [사실] | LLM+P 는 자연어 문제 설명을 LLM 으로 PDDL 파일로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 구조로, 저자는 LLM 단독으로는 대부분 문제에서 실행 가능한 계획도 못 냈으나 LLM+P 는 대부분에서 최적 해를 냈다고 보고한다. | ref-092 | 아니오 | medium | 2023-04 | — | 원문 미열람 |
| f8 | [사실] | KnowNo 는 등각 예측(conformal prediction)으로 LLM 계획기의 불확실성을 보정해, 과제 완수에 통계적 보장을 두면서 후보 행동이 하나로 좁혀지지 않을 때만 사람에게 도움을 요청하게 하며, 모델 미세조정 없이 쓸 수 있다고 저자가 보고한다. | ref-351 | 아니오 | medium | 2023-07 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | Code as Policies 는 코드 생성 LLM 이 자연어 명령과 소수 예시를 받아 인식 출력 처리와 제어 기본 API 호출을 조합한 로봇 정책 코드를 쓰게 하는 방법으로, 사람이 정한 API 범위 안에서 명령을 재조합한다. | ref-596 | 아니오 | medium | 2022-09 | — | 원문 미열람 |
| f10 | [사실] | AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍(보정 100, 시험 900)에 모호성 유형, 명확화 질문과 답, 작업 계획을 필드로 두어 LLM 의 모호성 탐지·되묻기를 평가하게 한다. | ref-354 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | Wang 외(Learning to Ask)는 도구 호출 LLM 에이전트가 불완전한 지시에서 빠진 인자를 지어내는 문제를 다루고, 불명확 지시 벤치마크 NoisyToolBench 와 필요할 때 되묻는 방법(Ask-when-Needed)을 제안했다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f12 | [사실] | Lang2LTL 연구는 자연어 명령을 선형 시간 논리(LTL) 식으로 바꿔 접지하는 방법과, LTL 식 템플릿에서 나온 식에 영어 발화를 대응시킨 말뭉치를 제시했다. | ref-056 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f13 | [사실] | LoTa-Bench 는 언어 기반 작업 계획기의 성능을 시뮬레이터(AI2-THOR 기반 ALFRED, VirtualHome 기반 Watch-And-Help 확장)의 성공률로 자동 정량화하는 벤치마크다. | ref-541 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f14 | [사실] | SafeGate 는 자연어 작업 명령에서 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람 확인 요청·거부를 정하고, 승인된 작업을 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했다. | ref-417 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f15 | [사실] | RTAW 는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 정식화하고 주의(attention) 기반 정책을 PPO 로 학습해 총 이동 지연을 줄이며, 저자는 500개 작업에서 탐욕·후회 기반 기준 대비 최대 10% 개선과 로봇·작업 수에 독립적인 정책 크기를 보고한다. | ref-597 | 아니오 | medium | 2022-09 | 수행 자원 | 원문 미열람 |
| f16 | [사실] | Sculley 외(NeurIPS 2015)는 실제 ML 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성, 설정 문제, 외부 세계 변화 같은 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. | ref-598 | 아니오 | medium | 2015 | — | 원문 미열람 |
| f17 | [사실] | Breck 외의 ML Test Score(IEEE Big Data 2017)는 데이터·모델·인프라 시험과 감시를 1급 관심사로 두는 28개 시험·감시 항목으로 ML 시스템의 운영 준비도를 점수화하는 기준표를 제시했다. | ref-610 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f18 | [사실] | 오픈소스 MLflow 의 모델 레지스트리는 등록 모델마다 버전·별칭·태그와 계보(어느 실험·실행이 만들었는지)를 관리하며, 운영 대상 버전에 별칭(예: champion)을 붙이고 별칭을 다른 버전으로 옮겨 운영 모델을 교체하게 한다. | ref-611 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [추정] | 국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. | ref-612 | 아니오 | low | 2026-09-19 | 출하 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f20 | [추정] | 분류 원문 질문과 관련해, 확인한 접근을 종합하면 AI 가 만든 계획·해석을 실행에 쓰는 기준은 (1) 실행 가능성 접지(SayCan), (2) 형식 명세·계획기 경유 검증(LLM+P, Lang2LTL), (3) 불확실할 때 사람 확인(KnowNo, Ask-when-Needed), (4) 실행 전 안전 판정(SafeGate), (5) 승인된 모델 버전·시험 기준(ML Test Score, 모델 레지스트리, ISO/IEC 42001)의 겹 구조로 정리될 수 있어 보인다. | ref-088, ref-092, ref-056, ref-351, ref-359, ref-417, ref-610, ref-611, ref-592 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f21 | [추정] | 피킹 단계에서 관리자가 '오늘 마감 주문을 B구역부터 피킹'처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. | ref-092, ref-351, ref-354 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | 원문 미열람 |
| f22 | [추정] | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려면 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고, 교체 전 시험·감시 기준을 통과시켜야 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. | ref-611, ref-610, ref-597, ref-598 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f23 | [추정] | ROP 가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리이고, 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 이를 둘러싼 운영 틀로 보인다. | ref-592, ref-586, ref-593, ref-351, ref-611 | 아니오 | low | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f24 | [추정] | 연계 대상: 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(Code as Policies 의 저수준 정책 코드, SayCan 의 사전 학습 기술)과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP 는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. | ref-596, ref-088 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f25 | [추정] | 27. AI·학습·적응과 모델 운영의 방법은 교차 규칙에 따라 학습 기반 배차로 13. 작업 배정 — MRTA(RTAW), 실행 전 안전 판정과 제품 안전 구성요소 규제로 25. 안전·위험 관리(SafeGate, EU AI Act), 사람 확인 요청으로 18. 사람–로봇 협업·운영 인터페이스(KnowNo), 모델 버전·변경으로 24. 자산·소프트웨어 수명주기 관리, 평가 벤치마크로 23. 시험·형식 검증·벤치마크(LoTa-Bench)와 맞물리는 것으로 보인다. | ref-597, ref-417, ref-595, ref-351, ref-611, ref-541 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: NIST AI 100-1(AI RMF 1.0), 2023-01 발표. 네 기능 Govern·Map·Measure·Manage, Playbook 이 하위 범주별 권장 행동을 제공(검색 요약 기준).
- **f2**: requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (검색 요약 기준).
- **f3**: 2023-02 발행, ISO 31000 기반 AI 위험관리 지침. 소통, 맥락 설정, 위험 평가·처리, 감시·검토, 기록·보고를 다룸(검색 요약 기준).
- **f4**: 기본법·시행령 2026-01-22 시행, 고영향 인공지능은 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI. 과태료 부과 유예(검색 요약 기준, 법령 원문 미열람).
- **f5**: AI 시스템이 부속서 I 조화 법령 대상 제품의 안전 구성요소이고 제3자 적합성 평가가 필요하면 고위험(검색 요약 기준). 적용 시점은 개정 논의가 있어 이번에 확정하지 않음.
- **f6**: the LLM (Say) provides a task-grounding ... the learned affordance functions (Can) provide a world-grounding (초록, 검색 요약 기준).
- **f7**: 자연어→PDDL→고전 계획기→자연어. 저자 보고: 대부분 문제에서 최적 해, LLM 단독은 실행 가능한 계획도 대부분 실패(벤치마크 도메인 조건, 검색 요약 기준).
- **f8**: conformal prediction 기반으로 과제 완수 통계적 보장과 사람 도움 최소화, 공간·수치·선호 모호성 과제의 시뮬레이션·실로봇 실험(저자 보고, 검색 요약 기준).
- **f9**: LLM 이 지각 출력(물체 검출기 등)을 처리하고 제어 기본 API 를 매개변수화하는 정책 코드를 few-shot 으로 생성(초록, 검색 요약 기준).
- **f10**: 1000쌍(보정 100·시험 900), 환경 설명·지시문·모호성 유형·명확화 질문과 답·작업 계획 필드. 주방 환경 조건 (재인용: 2026-09-25-62)
- **f11**: ToolBench 정상 표본 200건을 불완전 지시로 변형, 정확도와 되묻기 효율을 자동 평가 (재인용: 2026-09-25-62)
- **f12**: 47개 템플릿·2,125개 LTL 식에 약 5만 발화 대응(저자 보고, 판에 따라 수치 차이 가능) (재인용: 2026-09-25-62)
- **f13**: 가정 서비스 에이전트 언어 기반 계획 성능을 자동 정량화, 두 환경 쌍에서 성공률 비교 (재인용: 2026-09-25-62)
- **f14**: ISO 13482 근거 안전 속성 추출, 승인/확인 요청/거부, 작업 안전 계약. 평가는 저자 보고, 개인 돌봄 로봇 표준 기반 (재인용: 2026-09-25-63)
- **f15**: global embeddings independent of the number of robots/tasks; 500 tasks 기준 최대 10%(25~1000초) 개선, ICRA 2023(저자 보고, 시뮬레이션 창고 조건, 검색 요약 기준).
- **f16**: ML-specific risk factors: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, changes in the external world(검색 요약 기준).
- **f17**: 28 specific tests and monitoring needs ... production readiness 점수화(검색 요약 기준).
- **f18**: model lineage, model versioning, model aliasing ... reassigning the champion alias to a different model version(공식 문서, 검색 요약 기준).
- **f19**: 벤더 주장: 기업이 밝힌 적용 효과를 기사가 전한 것으로 수치·검증 조건 미확인(기사, 검색 요약 기준).
- **f20**: 각 출처가 서로 다른 단계(접지·검증·확인·안전 판정·모델 관리)를 다루며, 이를 하나의 채택 기준으로 묶은 것은 이 위키의 종합이다.
- **f21**: LLM+P 의 형식 변환·계획기 검증과 KnowNo·AmbiK 의 모호성 확인을 물류 피킹 지시에 옮긴 가상 시나리오(출처는 가정·주방·벤치마크 환경).
- **f22**: 별칭 재지정으로 운영 모델 교체(MLflow), 운영 준비도 시험(ML Test Score), 외부 세계 변화 위험(Sculley)을 학습 배차(RTAW 유형)에 적용한 가상 시나리오.
- **f23**: 분류 원문 9장 경계(로봇 자체 지능·제어는 연계)에 비추어 이 위키가 나눈 범위 판단이다.
- **f24**: 분류 원문 9장: 센서 인식·파지·모터 제어는 로봇 쪽, 수요예측은 상위 업무 시스템 쪽 연계 대상.
- **f25**: 각 출처가 다루는 기능을 분류 원문 영역에 대응시킨 이 위키의 판단. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-586 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | 정부·연구기관 | medium | 2026-09-25 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 예 |
| ref-592 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/42001 | 예 |
| ref-593 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/77304.html | 예 |
| ref-594 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 예 |
| ref-595 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-088 | Ahn, M. 외 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2204.01691 | 예 |
| ref-092 | Liu, B. 외 | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2304.11477 | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-596 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.07753 | 예 |
| ref-597 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.05738 | 예 |
| ref-598 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | 논문 | medium | 2026-09-25 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 예 |
| ref-610 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | 논문 | medium | 2026-09-25 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 예 |
| ref-611 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry \| MLflow AI Platform | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://mlflow.org/docs/latest/ml/model-registry/ | 예 |
| ref-612 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | 기사 | low | 2026-09-25 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 예 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/cog-model/AmbiK-dataset | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2302.11649 | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-417 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |

### 출처 요약

- **ref-586**: 원문 미열람. NIST AI RMF 1.0(NIST AI 100-1) 발표문. 네 기능 Govern·Map·Measure·Manage.
- **ref-592**: 원문 미열람. AI 관리 시스템(AIMS)의 수립·실행·유지·개선 요구사항 표준 소개 페이지.
- **ref-593**: 원문 미열람. ISO 31000 을 AI 에 적용한 위험관리 지침 소개 페이지.
- **ref-594**: 원문 미열람. 한국 인공지능 기본법 법령 본문. 고영향 인공지능 정의와 사업자 책무, 2026-01-22 시행(검색 요약 기준).
- **ref-595**: 원문 미열람. Regulation (EU) 2024/1689(AI Act)의 위험 기반 규제와 고위험 AI 분류 안내 페이지.
- **ref-088**: 원문 미열람. SayCan: LLM 과제 접지와 기술 가치 함수의 세계 접지를 결합한 로봇 계획.
- **ref-092**: 원문 미열람. 자연어를 PDDL 로 바꿔 고전 계획기로 푸는 LLM+P 프레임워크.
- **ref-351**: 원문 미열람. KnowNo: 등각 예측으로 LLM 계획기의 불확실성을 보정해 필요할 때만 사람에게 묻는 방법.
- **ref-596**: 원문 미열람. 코드 생성 LLM 이 인식·제어 API 를 조합한 로봇 정책 코드를 쓰는 방법.
- **ref-597**: 원문 미열람. 창고 다중 로봇 작업 배정의 주의 기반 강화학습(ICRA 2023).
- **ref-598**: 원문 미열람. ML 시스템 고유의 기술 부채와 위험 요인(NeurIPS 2015).
- **ref-610**: 원문 미열람. 28개 시험·감시 항목으로 ML 운영 준비도를 점수화하는 기준표(IEEE Big Data 2017).
- **ref-611**: 원문 미열람. 모델 버전·별칭·태그·계보를 관리하는 MLflow 모델 레지스트리 공식 문서.
- **ref-612**: 원문 미열람. 국내 물류기업의 로봇·AI 적용 사례 기사(한진 적재량 예측, CJ대한통운 포장 로봇 등).
- **ref-354**: 원문 미열람. 모호 작업 데이터셋 AmbiK 공식 저장소 README(이번 실행에서 다시 열지 않음).
- **ref-359**: 원문 미열람. 불명확 지시 벤치마크 NoisyToolBench 와 Ask-when-Needed.
- **ref-056**: 원문 미열람. Lang2LTL: 자연어 명령을 LTL 로 바꿔 접지하는 방법과 말뭉치.
- **ref-541**: 원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크 LoTa-Bench 공식 저장소(이번 실행에서 다시 열지 않음).
- **ref-417**: 원문 미열람. LLM 명령의 실행 전 안전 판정과 작업 안전 계약 SafeGate.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f20(분류 원문 질문, 추정), f4·f5(국내외 규제 맥락), f16 / 4절: f8(등각 예측), f2(AIMS), f18(모델 레지스트리), f6(접지) / 5절: f21(피킹·시작 조건), f22(출하·예외·성과), f19(출하, 벤더 주장 병기) / 6절: f6·f7·f9·f8·f11·f14(LLM 계획 접지·검증·되묻기·안전 판정 — 트랙 nl-task-chatbot 반영 제안 2026-09-25-04·21·30·37 확인분), f15(학습 기반 배차), f16·f17·f18(모델 운영) / 7절: f1·f2·f3·f4·f5, f18 / 8절: f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17(트랙 반영 제안 2026-09-25-04·30·62 확인분) / 9절: f23(직접), f24('연계 대상') / 10절: f25와 교차 규칙 원문(5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석) / 11절: oq-030 유지와 open_questions_new 3건. 다음 실행 후보: 도면 해석(2026-09-25-05·36·54)과 매뉴얼 추출(2026-09-25-57) 반영 제안, LLM 다중 로봇 서베이·ROSA·RAI(2026-09-25-21)는 출처 메타데이터가 입력에 없어 이번 브리프에서 재확인하지 못함 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 등각 예측 | Conformal Prediction | 보정 데이터로 예측 집합의 크기를 정해, 정답이 집합에 들어갈 확률을 사용자가 정한 수준 이상으로 통계적으로 보장하는 불확실성 정량화 방법이다. |
| AI 관리 시스템 | Artificial Intelligence Management System (AIMS) | 조직이 AI 의 책임 있는 개발·제공·사용을 위한 정책·목표·프로세스를 세우고 운영하는 관리 체계로, ISO/IEC 42001 이 요구사항을 정한다. |
| 고영향 인공지능 | High-impact AI (Korea AI Basic Act) | 한국 인공지능 기본법에서 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있어 별도 책무가 부과되는 영역의 AI 시스템이다. |
| 모델 레지스트리 | Model Registry | 학습된 모델의 버전·별칭·태그·계보를 한곳에서 관리해 어떤 버전을 운영에 쓰는지 정하고 교체·되돌림을 추적하게 하는 저장소다. |

## 열린 질문

새로 생긴 질문:

- 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반
- LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 25. 안전·위험 관리 | 근거: f5 | 종류: 일반
- KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f8 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 12회 · 신규 출처 14건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처 또는 종합 추정)
    - oq-030 LTAA 출처 충돌 미조사: 예산 배분상 이번 실행에서 원문 결과 확인 못 함(미해결 유지)
    - f5 EU AI Act 고위험 적용 시점은 개정 논의로 요약 간 차이가 있어 넣지 않음
    - f4 인공지능 기본법 고영향 영역 목록과 개정 법률 시행일(2026-07-21 언급) 원문 미확인
    - f15 RTAW 개선 수치는 저자 보고, 원문 미열람
    - f19 한진 사례의 수치·검증 조건 미확인(기사, 벤더 주장)
    - ref-594·ref-595·ref-611·ref-354·ref-541 발행일 미확인
    - 현대자동차·마키나락스 로봇 고장 예측 사례는 검색 요약에만 있고 출처 기사를 특정하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f24: 저수준 정책·파지 학습과 수요예측은 분류 원문 9장 로봇 자체 지능·제어, 상위 업무 시스템 쪽이라 '연계 대상:'으로 표시
    - f19: 간선차량 상·하차 시점 예측은 거점 간 운송과 맞닿아 있어 입출고 시간·접안 동기화 범위로만 제안
    - f14: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f8 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 다시 작성했다(검색 12회/30). 이번 브리프의 f8 은 KnowNo 논문(ref-351) 근거이며 벤더 문서가 아니다. 벤더·기업 주장은 f19 한 건뿐이고 vendor_claim: true, 태그 추정, evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다. web_fetch_available: false · fetch_mode mirror_only: 이번 출처는 GitHub 공식 저장소 미러가 없어 모두 원문 미열람(fetched false, 신뢰도 상한 medium). 신규 출처 14건(ref-586~ref-612, 예약 구간 안), 재사용 5건(ref-354·ref-359·ref-056·ref-541·ref-417, 참고문헌 목록 요약이 입력에 없어 이전 브리프 표의 값 사용, 신뢰도는 high 금지 규칙으로 medium). 트랙 반영 제안 15건 중 LLM 접지·검증·불확실성·안전 판정·평가 벤치마크 관련(2026-09-25-04·30·37·62 일부)은 f6~f14 로 확인했고, 도면 해석(2026-09-25-05·36·54)·매뉴얼 추출(2026-09-25-57)·LLM 다중 로봇 서베이(2026-09-25-21) 제안은 출처 메타데이터가 입력에 없고 예산 배분상 재확인하지 못해 '다음 실행 후보'로 남겼다. 교차 규칙: 학습 배차는 13. 작업 배정 — MRTA 와 양쪽 연결(f15·f25). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 한국 자료: 인공지능 기본법(ref-594), 국내 물류 AI 기사(ref-612). 정정 요청 없음.
