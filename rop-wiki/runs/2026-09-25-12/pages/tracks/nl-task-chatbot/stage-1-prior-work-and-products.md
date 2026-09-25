---
title: "단계 1. 선행 연구·제품 사례 조사"
type: track-stage
track: nl-task-chatbot
stage: 1
related_areas: [27, 13, 18, 2]
tags: [선행 연구, 제품 사례, 작업 분해, LLM, 작업 배정]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-053, ref-054, ref-055, ref-056, ref-057, ref-058, ref-059, ref-061, ref-089, ref-090, ref-091, ref-092, ref-093, ref-094, ref-095, ref-087, ref-088, ref-220, ref-221, ref-222, ref-223, ref-224, ref-225, ref-226, ref-227, ref-228, ref-229, ref-230, ref-231, ref-232, ref-138, ref-233, ref-234, ref-235, ref-236, ref-237]
last_run: 2026-09-25
version: 3
---

[홈](../../index.md) › 중점 연구 트랙 › [자연어 업무 지시 챗봇](index.md) › 단계 1. 선행 연구·제품 사례 조사

# 단계 1. 선행 연구·제품 사례 조사

> 단계 상태: 진행 중 · 열린 질문: 4건 · 답한 질문: 2건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 자연어 지시를 작업으로 바꾸고 로봇에 배정하는 기존 연구와 제품은 무엇을 자동화하고 무엇을 사람에게 남기는가.

위 문장은 트랙 정의의 "밝힐 것"이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 조사 결과는 [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)과 [업무 분해·배정 설계 초안](task-model-draft.md)으로 이어진다.

## 2. 질문 목록

이 단계의 시작 질문 4개와 실행 2026-09-25-04에서 생긴 후속 질문 2개다. q1-01은 사용자 요청의 시작 질문 문구 그대로이고, q1-02~q1-04는 구축자가 이 단계의 밝힐 것에서 정한 시작 질문이다. [가정] 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커 또는 주제 페이지 링크를 적는다. 제기 근거 칸에는 finding id 또는 "사용자"만 쓴다. q1-05와 q1-06은 사실상 같은 질문이어서 백로그 정리가 필요하다는 것이 실행 2026-09-25-12 검증의 지적이며, 정리 전까지 둘 다 열림으로 둔다.

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q1-01 | 자연어 지시를 작업 단위로 분해하는 기존 접근은 무엇이 있는가? | 답함 | 사용자 | 2026-09-25-04 | [#q1-01](#q1-01) |
| q1-02 | LLM을 로봇 작업 계획이나 여러 로봇의 작업 배정에 쓴 연구·제품 사례는 무엇이 있고, 각각 LLM이 맡는 범위(해석·분해·배정·명령 생성)는 어디까지인가? | 답함 | 사용자 | 2026-09-25-12 | [#q1-02](#q1-02) |
| q1-03 | 물류·시설 현장에서 채팅이나 음성으로 로봇·작업자에게 일을 지시하는 운영 인터페이스 제품은 무엇이 있고, 지시를 받은 뒤 확인·승인을 어떻게 받는가? | 열림 | 사용자 | | |
| q1-04 | 자연어 지시에서 장소·대상 화물·긴급도·기한 같은 상황 정보를 뽑아내는 기존 방법은 무엇이고, 빠진 정보는 어떻게 되묻는가? | 열림 | 사용자 | | |
| q1-05 | 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구가 있는가, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 무엇이 달라지는가? | 열림 | f15, 실행 2026-09-25-04 | | |
| q1-06 | 팔레트 이동·출하 준비 같은 물류·창고 현장 지시를 대상으로 한 LLM 작업 분해 연구나 지시–작업 데이터셋이 있는가, 가정용 시뮬레이터(VirtualHome, AI2-THOR) 결과를 물류 지시로 옮길 때 무엇이 달라지는가? (q1-01 에서 파생) | 열림 | f15, 실행 2026-09-25-04 | | |

## 3. 조사 결과

### q1-01 자연어 지시를 작업 단위로 분해하는 기존 접근 {#q1-01}

자연어 지시를 작업으로 나누는 기존 접근은 분해 결과를 어떤 형태로 내놓는지에 따라 여섯 유형으로 묶을 수 있다는 것이 이 위키의 정리이며, 이 분류 자체를 제시한 출처는 확인하지 못했다. [추정][^ref-057][^ref-093][^ref-087][^ref-054][^ref-095][^ref-091][^ref-055][^ref-061][^ref-059][^ref-089] 이번 실행(2026-09-25-04)에서 논문 원문은 열지 못했고(검색 요약 범위), 공식 코드 저장소 README 일부만 원문으로 읽었다. 각 접근의 논문과 README는 같은 저자 계열이라 독립 교차 확인은 없다.

#### 분해 결과 형태로 본 여섯 유형

| 유형 | 분해 결과의 형태 | 조사한 접근 |
|---|---|---|
| 유형 1. 확률 그래프 접지 | 명령의 의미 구조에 맞춰 만든 확률 그래프 모델 | G3(Tellex 외 2011) |
| 유형 2. 기술·허용 동작 순서 | 미리 정한 기술·허용 동작의 순서 | Huang 외 2022, SayCan |
| 유형 3. 프로그램 코드 | 실행 가능한 계획 프로그램·정책 코드 | ProgPrompt, Code as Policies |
| 유형 4. 형식 명세를 계획기에 넘김 | 계획 도메인 정의 언어 문제 파일, 선형 시간 논리 식 | LLM+P, Lang2LTL |
| 유형 5. 실행 구조 그래프 | 행동 트리, 하위 작업 의존 그래프 | BTGenBot, DART-LLM |
| 유형 6. 다중 로봇 파이프라인 | 분해·팀 구성·할당을 잇는 단계 | SMART-LLM, DART-LLM |

#### 접근별로 확인된 내용

- **G3**: Tellex 외(AAAI 2011)의 일반화 접지 그래프(Generalized Grounding Graphs, G3)는 자연어 명령의 계층적·조합적 의미 구조에 따라 확률 그래프 모델을 명령마다 동적으로 만들고, 크라우드소싱으로 모은 명령–로봇 행동 쌍 말뭉치로 파라미터를 학습해 명령에 맞는 계획을 찾는다. [사실][^ref-057]
- **Huang 외**: ICML 2022 논문은 충분히 큰 사전학습 언어모델이 추가 학습 없이 상위 과업을 중간 단계 계획으로 분해할 수 있으나 그 단계가 환경의 허용 동작에 정확히 대응하지 않는 경우가 많아, 시연 예시로 조건을 주고 생성된 단계를 의미가 가까운 허용 동작으로 옮기는 절차를 제안했다. [사실][^ref-093][^ref-094]
- **SayCan**: Ahn 외(2022)는 언어모델이 상위 목표에 대해 각 로봇 기술의 쓸모를 평가하고, 강화학습으로 학습한 언어 조건 가치 함수(어포던스)가 그 기술이 현재 상태에서 실행 가능한지를 평가해 둘을 결합한 점수로 다음 기술을 고른다. [사실][^ref-087][^ref-088]
- **ProgPrompt**: Singh 외(2022)는 환경의 가용 동작과 객체를 프로그램 형태로 명세하고 예시 프로그램을 함께 넣은 프롬프트로 LLM이 실행 가능한 계획 프로그램 전체를 생성하게 하며, 계획 안의 확인문(assertion)으로 실행 결과를 점검한다. [사실][^ref-054] 구현 코드는 공식 저장소로 따로 공개되어 있다. [사실][^ref-053]
- **Code as Policies**: 공식 README(확인일 2026-09-25 기준)에 따르면 코드 생성 LLM이 자연어 명령과 몇 개의 예시(주석 형태 명령과 정책 코드)를 받아 인식 API와 제어 기본 동작 API 호출을 조합한 로봇 정책 코드를 쓰고, 정의되지 않은 함수를 재귀적으로 정의하는 계층적 코드 생성을 둔다. [사실][^ref-095]
- **LLM+P**: Liu 외(2023)는 자연어로 기술된 계획 문제를 LLM이 [계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)](../../glossary/pddl.md) 문제 파일로 바꾸고, 고전 계획기(Fast Downward)가 해를 찾은 뒤 그 해를 다시 자연어로 옮긴다. 계획 탐색 자체는 LLM이 아니라 계획기가 맡는다. [사실][^ref-091][^ref-092]
- **Lang2LTL**: Liu 외(2023)는 사전학습 LLM으로 명령에서 지칭 표현(랜드마크·객체)을 뽑고, 그것을 실제 환경의 랜드마크에 접지한 뒤, 명령을 기호 명제를 쓴 선형 시간 논리(Linear Temporal Logic, LTL) 식으로 옮기는 모듈형 구조를 쓴다. [사실][^ref-055][^ref-056]
- **BTGenBot**: 2024년 프리프린트는 70억 파라미터 이하의 경량 LLM을 미세조정해 텍스트 과업 기술에서 XML 형식의 행동 트리(Behavior Tree)를 생성하고, 정적 구문 분석·검증 시스템·시뮬레이션·실제 로봇으로 생성 결과를 평가했다. [사실][^ref-061]
- **SMART-LLM**: Kannan 외(2023)는 상위 지시를 받아 LLM이 프로그램형 few-shot 프롬프트로 작업 분해, 팀 구성(coalition formation), 작업 할당을 차례로 수행해 다중 로봇 작업 계획을 만들고, 로봇별 능력 목록을 담은 4개 난이도 범주의 벤치마크를 AI2-THOR 시뮬레이터에서 공개했다. [사실][^ref-089][^ref-090]
- **DART-LLM**: 2024년 프리프린트는 자연어 지시를 하위 작업으로 분해하면서 하위 작업 사이 의존을 방향 비순환 그래프(Directed Acyclic Graph, DAG)로 표현하고, 분해용 질의응답 LLM 모듈, 로봇 배정용 분해 함수 모듈, 실행 모듈, 시각-언어 모델 기반 객체 검출기로 구성된다. [사실][^ref-059]

가치 함수·제어 기본 동작·객체 검출은 여기서 분해 결과를 현장에 접지하는 방식의 설명으로만 다룬다. 센서 인식·파지·모터 제어 자체는 분류 원문 9장 기준으로 로봇 자체 지능·제어 쪽의 연계 대상이다.

#### 연구 지형: 형식 표현과 임베딩 사이

Cohen 외(IJCAI-24)의 로봇 언어 접지 서베이는 연구를 두 극 사이의 스펙트럼으로 정리한다. 한쪽은 언어를 사람이 정의한 형식 표현으로 옮기는 방식, 다른 쪽은 언어를 저수준 로봇 정책으로 바로 이어지는 고차원 벡터 공간으로 옮기는 방식이다. [사실][^ref-058] 서베이 저자들(Cohen 외, IJCAI-24)의 평가로는 형식 표현 방식이 의미를 정확히 표현하고 학습 문제를 줄이며 해석 가능성과 형식적 안전 보장의 틀을 주는 반면, 임베딩 방식은 수작업 기호 구조가 없어 더 일반적일 수 있으나 더 많은 데이터와 연산이 필요하다. [의견][^ref-058]

#### 무엇을 자동화하고 무엇을 사람에게 남기는가

- Huang 외, SayCan, ProgPrompt, Code as Policies, LLM+P, Lang2LTL, SMART-LLM 일곱 접근은 실행 가능한 단위(기술 목록, 가용 동작·객체, 제어 API, PDDL 도메인, 랜드마크 목록, 로봇 능력 목록)를 사람이 미리 정의해 두고 LLM은 그 어휘 안에서 분해하므로, 실행 단위의 정의와 예시 작성은 사람에게 남는 일로 보인다는 것이 이 위키의 정리(추론)다. [추정][^ref-094][^ref-087][^ref-054][^ref-095][^ref-091][^ref-055][^ref-089]
- SMART-LLM의 할당은 프롬프트에 넣은 로봇 능력 목록을 LLM이 추론해 정하는 방식이다. 이동 거리·납기·부하 같은 비용을 최적화 엔진으로 푸는 구조는 공식 저장소 README 기준으로 확인되지 않으며 논문 본문의 할당 세부는 미확인이다. [추정][^ref-089][^ref-090]
- LLM+P와 Lang2LTL처럼 LLM이 형식 명세만 만들고 계획·검증은 결정적 계획기나 논리 검사에 맡기는 구조는, LLM 출력을 실행 전에 형식적으로 점검할 수 있다는 점에서 오해석 방지와 이어지는 선행 사례로 보인다는 것이 이 위키의 정리다. 이 구조가 잘못된 배정을 실제로 줄이는지는 확인하지 못했다(트랙 가설 1의 판정 대상). [추정][^ref-091][^ref-055][^ref-058]
- 조사한 LLM 기반 분해 연구의 평가 환경은 가정·주방 시뮬레이터(VirtualHome, AI2-THOR), 실내·도시 내비게이션, 건설 기계 시나리오였고, 팔레트 적재 같은 물류 지시를 직접 다룬 예는 이번 검색 범위에서 LLM 이전 연구인 G3뿐이었다. 이는 이번 검색 범위의 결과이며 부재의 확인은 아니다. [추정][^ref-094][^ref-054][^ref-089][^ref-055][^ref-059][^ref-057]

### q1-02 LLM을 로봇 작업 계획·다중 로봇 배정에 쓴 연구·제품 사례와 LLM의 담당 범위 {#q1-02}

조사한 연구에서 LLM이 맡는 범위는 LLM이 분해와 배정을 모두 하는 방식, LLM은 분해·의존 그래프·정식화를 만들고 배정·계획은 결정적 해법이 맡는 방식, 사람이 정한 로봇 API·도구 안에서 LLM이 명령·코드를 생성하는 방식의 세 가지로 나뉘는 것으로 보인다는 것이 이 위키의 정리(추론)이며, 이 3분류를 제시한 단일 출처는 확인하지 못했다. [추정][^ref-089][^ref-226][^ref-225][^ref-223][^ref-224][^ref-220][^ref-227][^ref-091][^ref-231][^ref-229][^ref-138][^ref-237] 이 3분류는 q1-01의 여섯 유형(분해 결과의 형태)과 달리 "LLM이 어디까지 맡는가"를 축으로 삼는다. 이번 실행(2026-09-25-12)에서는 공식 GitHub 저장소 README 7건만 원문으로 읽었고, 논문·보도자료·기사·학술대회 초록은 검색 요약 범위다. 연구 수치는 모두 저자 보고값이며 독립 재현은 확인하지 못했고, 제품 사례는 모두 보도자료·기사에 근거한 벤더 주장이다.

| 방식 | LLM이 맡는 일 | 결정적 구성 요소가 맡는 일 | 조사한 사례 |
|---|---|---|---|
| 방식 1. LLM이 분해와 배정을 모두 함 | 작업 분해, 로봇 배정 | 없음(실행 피드백으로 LLM이 계획 수정) | SMART-LLM, COHERENT, LTAA |
| 방식 2. LLM 정식화 + 결정적 해법 | 분해, 의존 그래프, 문제 정식화 | 배정·계획(선형계획, MILP, PDDL 계획기, 결정적 해법) | LiP-LLM, Peng 외, LaMMA-P(계획 단계), IMR-LLM, LLM+P |
| 방식 3. 사람이 정한 도구 안에서 명령 생성 | 도구·함수 선택, 명령·코드 생성 | 도구·함수의 구현 | ChatGPT for Robotics, ROSA, RAI, 한국전자기술연구원 사례 |

LaMMA-P는 배정은 LLM이, 계획은 계획기가 맡아 방식 1과 방식 2에 걸친다. LLM 기반 다중 로봇 시스템 서베이(Autonomous Robots 게재, arXiv 2025-02)는 LLM의 적용을 상위 작업 배정, 중간 수준 동작 계획, 저수준 동작 생성, 사람 개입의 네 층으로 분류한다. [사실][^ref-222]

#### 방식 2: LLM이 분해·정식화하고 결정적 해법이 배정·계획

- **LaMMA-P**: 공식 README(ICRA 2025 게재 표기)에 따르면 이종 다중 로봇의 장기 작업에서 LLM이 하위 작업 분해와 로봇 배정을 맡고, 하위 작업별 [PDDL](../../glossary/pddl.md) 문제를 거쳐 고전 계획기(Fast Downward)가 계획을 생성한다. [사실][^ref-220] 논문 검색 요약 기준으로 이 프레임워크는 전제조건 식별·작업 배정·문제 생성·PDDL 검증·계획·하위 계획 결합의 여섯 모듈로 구성된다. [사실][^ref-221] 저자들은 AI2-THOR 시뮬레이터 기반 가정 작업 벤치마크 MAT-THOR(두 복잡도 수준)에서 기존 언어모델 기반 다중 에이전트 계획기보다 성공률이 105%, 효율이 36% 높았다고 보고했다. 이 수치는 저자 보고값이며 독립 재현은 확인되지 않았다. [사실][^ref-220]
- **LiP-LLM**: IEEE RA-L 게재 논문(arXiv 2024-10)은 LLM이 기술(skill) 목록과 기술 사이 선후 의존 그래프를 생성하고, 로봇에 대한 작업 배정은 선형계획(Linear Programming)으로 푸는 3단계 구조를 쓴다. [사실][^ref-223] 저자들은 선형계획으로 배정할 때 배정 오류가 적었고 의존 그래프 덕분에 병렬 실행되는 작업이 늘어 실행 효율이 좋아졌다고 보고했다. 저자 보고값이며 독립 재현은 확인되지 않았고, 실험 환경·비교 대상 같은 평가 조건은 원문 미확인이다. [사실][^ref-223]
- **Peng 외**: 2025-03 프리프린트는 로컬 LLM과 도메인 지식 베이스를 결합해 자연어 작업 기술을 혼합 정수 선형 계획(Mixed Integer Linear Programming, MILP) 모델로 바꾸고 다시 실행 가능한 코드로 옮기는 2단계 자동 정식화 틀을 제안했다. [사실][^ref-224] 저자들은 제조 생산 제약을 대상으로 한 평가에서 시공간 제약 추출 평균 정확도 82%, MILP 코드 생성 평균 정확도 90%를 보고했다. 저자 보고값이며 독립 재현은 확인되지 않았다. [사실][^ref-224]
- **IMR-LLM**: 2026-03 논문(ICRA 2026)은 산업용 다중 로봇 작업에서 LLM이 선언 그래프(disjunctive graph) 구성을 돕고 결정적 해법으로 상위 작업 계획을 구한 뒤, 공정 트리(process tree)로 LLM이 저수준 실행 프로그램을 생성하게 하며, 세 복잡도 수준의 IMR-Bench를 공개했다. [사실][^ref-227] 공식 코드 저장소 README는 논문 제목과 ICRA 2026 게재 표기를 담는다. [사실][^ref-228]
- **LLM+P**는 q1-01에서 다룬 대로 LLM이 PDDL 문제 파일을 만들고 계획기가 해를 찾는 구조로, 이 방식의 단일 로봇 선행 사례다([q1-01](#q1-01)).

#### 방식 1: LLM이 배정까지 직접 한다

- **COHERENT**: 공식 README에 따르면 중앙 작업 배정자 LLM이 작업을 하위 작업으로 분해해 쿼드로터·로봇 개·로봇 팔에 배정하고, 각 로봇 실행자가 실행 가능한 동작을 골라 자기 성찰 피드백을 보내면 배정자가 계획을 고치는 제안–실행–피드백–조정(PEFA) 반복을 쓴다. [사실][^ref-226]
- **LTAA**: LangGraph 기반 작업 배정 에이전트(LTAA) 연구(arXiv 2025-12)는 건설 작업 시나리오에서 LLM 기반 배정을 동적 계획법·Q-러닝·DQN과 비교했으며, 저자들은 로봇 전문화가 강한 설정에서 작업 완료율 77%를 보고했다. 저자 보고값이며 독립 재현은 확인되지 않았고, 동적 계획법 0.95 등 비교 결과의 세부와 TEACh 데이터 출처 표기는 원문 미확인이다. [추정][^ref-225]
- SMART-LLM의 분해·팀 구성·할당은 q1-01에서 다뤘다([q1-01](#q1-01)).

#### 방식 3: 사람이 정한 도구 안에서 명령·코드를 만든다

- **ChatGPT for Robotics**: Microsoft 연구(arXiv 2023-07 판)는 로봇의 저수준 구현에 대응하는 고수준 함수 라이브러리를 사람이 정의해 프롬프트에 주고 ChatGPT가 그 함수를 호출하는 코드를 생성하게 하며, 프롬프트 사례를 공유하는 PromptCraft-Robotics 저장소를 공개했다. [사실][^ref-232][^ref-231]
- **ROSA**: NASA JPL의 ROSA는 LangChain 기반 에이전트로 ROS 1(Noetic)·ROS 2(Humble·Iron·Jazzy) 시스템을 자연어로 조회·진단·조작하며, 개발자는 LangChain 도구 함수를 추가해 에이전트가 쓸 수 있는 행동을 정한다(확인일 2026-09-25 기준). [사실][^ref-229][^ref-230] 이번에 연 README와 사용자 정의 에이전트 문서에는 LLM이 고른 로봇 조작 도구를 실행 전에 사람이 확인하거나 권한을 제한하는 장치에 대한 설명이 없었다. 연 문서 두 건 범위의 관찰이며 부재의 확인은 아니다. [추정][^ref-229][^ref-230]
- **RAI**: Robotec.ai의 RAI는 ROS 2(Jazzy·Humble)용 제조사 무관 에이전트 프레임워크로, 다중 에이전트·음성 인식·음성 합성·인식 도구·시뮬레이션 연동·벤치마크(rai_bench) 패키지를 Apache 2.0 라이선스로 공개한다(확인일 2026-09-25 기준). [사실][^ref-138]
- **한국전자기술연구원 사례**: 한국전자기술연구원 연구진(이종록·황정훈·박민철)은 LangChain 에이전트의 도구를 ROS 2 토픽·서비스 인터페이스로 정의해 사용자의 자연어 명령을 ROS 2 로봇 제어 명령으로 바꾸고 로봇별 위치·상태를 실시간 모니터링하는 다중 로봇 관제 시스템을 구현했다고 국내 학술대회 초록으로 발표했다(학술대회 이름·발표일 미확인, 확인일 2026-09-25 기준). [사실][^ref-237]

이 방식들이 호출하는 저수준 주행·조작 제어는 분류 원문 9장 기준으로 로봇 자체 지능·제어 쪽의 연계 대상이며, 여기서는 LLM이 맡는 범위를 설명하는 데만 다룬다.

#### 로봇 운영 제품 사례 (벤더 주장)

- **InOrbit RobOps Copilot(2024)**: InOrbit은 2024년 5월 Automate 2024에서 RobOps Copilot을 LLM으로 로봇 운영 데이터에 대해 사용자가 선호하는 언어로 질문하고 설명·분석을 받는 도구로 발표했으며, Microsoft Teams·Slack 같은 메신저에서 쓰게 했다고 밝혔다. [추정] 벤더 주장[^ref-233]
- **InOrbit RobOps Copilot(2026)**: InOrbit은 2026년 6월 Automate 2026에서 RobOps Copilot을 운영자가 음성을 포함한 자연어로 로봇 동작 정의, 실시간 데이터 조회, 성능 분석, 로봇 미션 실행, 보고서 생성을 하는 에이전트형 AI 계층으로 소개했다. [추정] 벤더 주장[^ref-234]
- **Formant F3**: Formant는 2025-06-30에 F3를 자연어 질의응답·시각화를 제공하고 상시 에이전트가 플릿을 감시·분석·권고하는 로봇 운영 플랫폼으로 발표했다. [추정] 벤더 주장[^ref-235]
- **다임리서치 다비스(DARVIS)**: 국내 로봇 통합관제 기업 다임리서치는 통합관제 솔루션 xMS의 운영 데이터를 바탕으로 자연어 질문에 답하고 장애 원인과 대응 방안을 제시하는 온프레미스 AI 에이전트 다비스(DARVIS)를 개발 중이며 2027년 상반기 1.0 출시를 계획한다고 밝혔다(2026-08-27 기사 기준). [추정] 벤더 주장[^ref-236]

확인한 제품 자료에서 LLM의 역할은 운영 데이터 질의·설명·진단에서 시작해 자연어로 미션을 실행하는 쪽으로 넓어지는 흐름이 보이지만, 공개 자료에서는 미션이 미리 정의된 것을 호출하는지 새로 분해하는지와 실행 전 확인·권한 장치가 확인되지 않는다. 보도자료·기사 검색 요약에 기댄 관찰이며 부재의 확인은 아니다. [추정] 벤더 주장[^ref-233][^ref-234][^ref-235][^ref-236]

#### 평가 환경의 한계

이번에 확인한 LLM 다중 로봇 배정 연구의 평가 환경은 가정 작업 시뮬레이터(AI2-THOR 기반 MAT-THOR, OmniGibson), 건설 시나리오, 산업 조립 벤치마크(IMR-Bench)였고, 물류센터·창고 작업 지시를 다룬 연구는 이번 검색 범위에서 찾지 못했다. 검색 범위의 결과이며 부재의 확인은 아니다(q1-05·q1-06으로 이어짐). [추정][^ref-220][^ref-226][^ref-225][^ref-227] 제조 생산 제약을 다룬 Peng 외의 MILP 연구도 물류 지시를 대상으로 하지는 않는다. [사실][^ref-224]

## 4. 결론과 남은 불확실성

**결론**
- 자연어 지시의 분해 결과는 확률 그래프, 기술·허용 동작 순서, 프로그램 코드, 형식 명세, 실행 구조 그래프, 다중 로봇 파이프라인의 여섯 형태로 정리된다(이 위키의 정리). [추정][^ref-057][^ref-089]
- 조사한 일곱 LLM 기반 접근에서 실행 단위의 정의는 사람이 미리 해 두며, LLM은 그 어휘 안에서 분해한다. [추정][^ref-094][^ref-089]
- 여러 로봇을 대상으로 분해와 팀 구성·할당을 잇는 연구(SMART-LLM, DART-LLM)가 있다. [사실][^ref-089][^ref-059]
- LLM이 맡는 범위는 분해·배정을 모두 맡는 방식, 정식화만 맡고 결정적 해법이 배정·계획하는 방식, 사람이 정한 도구 안에서 명령을 만드는 방식으로 나뉘는 것으로 보인다(이 위키의 정리). [추정][^ref-226][^ref-223][^ref-229]
- LLM이 의존 그래프나 MILP 정식화를 만들고 배정·계획은 선형계획·MILP·PDDL 계획기·결정적 해법이 맡는 다중 로봇 연구가 있다(LiP-LLM, Peng 외, IMR-LLM, LaMMA-P(LaMMA-P는 계획 단계만 계획기가 맡고 배정은 LLM이 맡는다)). [사실][^ref-223][^ref-224][^ref-227][^ref-220]
- 사람이 정한 도구로 LLM 에이전트의 행동 범위를 정하는 공개 프레임워크(ROSA)와 국내 연구 사례(한국전자기술연구원)가 있다. [사실][^ref-229][^ref-237]
- 로봇 운영 제품에서 LLM의 역할은 운영 데이터 질의·설명에서 자연어 미션 실행으로 넓어지는 흐름으로 보이나, 근거는 보도자료·기사다. [추정] 벤더 주장[^ref-233][^ref-234]

**남은 불확실성**
- q1-01의 모든 접근이 논문 원문 미열람이며, 논문과 README가 같은 저자 계열이라 독립 교차 확인이 없다. q1-02도 교차 확인된 주장이 없다.
- SMART-LLM 논문 본문의 할당 방식 세부는 미확인이다.
- 연구 수치(LaMMA-P 105%·36%, Peng 외 82%·90%, LTAA 77%)는 모두 저자 보고값이며 독립 재현이 확인되지 않았다. LiP-LLM·Peng 외·LTAA는 원문을 열지 못했고, LaMMA-P의 여섯 모듈 이름과 IMR-LLM의 방법 세부는 검색 요약 기준이다.
- LTAA의 비교 결과는 검증 검색에서 요약끼리 엇갈렸다. LLM 배정이 비교 기법보다 높았다는 요약과, 동적 계획법의 완료율이 더 높고(0.95) 강화학습 에이전트와 대등했다는 요약이 함께 나와 비교 우위는 판단하지 않았다(단계 3 후속 질문 q3-05).
- 운영 제품의 자연어 미션 실행이 미리 정의된 미션을 호출하는 것인지 지시를 새로 분해하는 것인지는 공개 자료로 확인되지 않았다. [추정] 벤더 주장[^ref-234][^ref-235] 제품의 실행 전 확인·권한 장치는 q1-03에서 조사한다.
- ROSA의 확인·권한 장치 부재는 연 문서 두 건 기준이며 FAQ·개발자 문서는 열지 않았다. 한국전자기술연구원 초록의 학술대회 이름·발표일은 미확인이다.
- 물류·창고 지시를 다룬 LLM 분해·배정 연구는 이번 검색 범위에서 확인되지 않았다(q1-05·q1-06으로 이어짐). 국내 자료는 학술대회 초록 1건과 기업 기사 1건만 찾았다.
- 채팅·음성 지시 제품의 확인·승인(q1-03)과 상황 정보 추출·되묻기(q1-04)는 아직 조사하지 않았다.
- 업무 분해·배정 설계 초안은 v0 → v0.1로 올렸다(개념 로봇 팀 추가). 허용 동작 목록, 형식 작업 명세, 작업 사이 선행 의존 관계는 기존 개념·속성과의 중복 또는 단계 3 판단 사항이라 표에 넣지 않고 [미해결 모델링 질문](task-model-draft.md#6-미해결-모델링-질문)으로 두었다.
- 실행 2026-09-25-12에서 초안을 v0.1 → v0.2로 올렸다(배정에 속성 '배정 산출 방식' 추가, 값은 LLM 직접 추론과 선형계획·MILP 같은 최적화 해법). 같은 제안의 '규칙' 값은 근거 finding이 없어 넣지 않고 미해결 모델링 질문으로 두었다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q1-05 | 물류·창고 현장 지시를 다룬 LLM 작업 분해 연구가 있는가, 가정용 시뮬레이터 결과를 물류 지시로 옮길 때 무엇이 달라지는가? | 단계 1. 선행 연구·제품 사례 조사 | f15(실행 2026-09-25-04) | 열림 |
| q3-05 | 같은 다중 로봇 배정 작업에서 LLM이 직접 배정하는 방식과 LLM이 정식화하고 선형계획·MILP 해법기가 배정하는 방식을 배정 오류율·일정 품질·계산 시간으로 비교한 연구가 있는가? (q1-02 에서 파생) | 단계 3. 구현 가설 설계 | f8(실행 2026-09-25-12) | 열림 |

실행 2026-09-25-04에서 함께 제기된 두 질문(분해 결과의 중간 표현을 작업 모델·관제 인터페이스로 옮기는 문제, 허용 동작 밖의 동작을 걸러내는 장치)은 각각 기존 백로그 질문 q2-02, q4-02와 겹쳐 새로 등록하지 않았다. 실행 2026-09-25-12에서 제기된 운영 제품의 자연어 미션 실행 방식과 실행 전 확인·권한 장치에 관한 질문은 확인·승인 부분이 기존 q1-03과 겹쳐 새로 등록하지 않았고, 미리 정의된 미션 호출과 새 분해의 구분이 미확인이라는 점은 4절 남은 불확실성에 두었다.

## 6. 완료 조건 충족 현황

충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 선행 연구·제품 사례 비교가 [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)의 "3. 선행 연구·제품 사례" 절에 실림 | 미충족 | 선행 연구(q1-01·q1-02)와 제품 사례(q1-02, 벤더 주장 수준)는 실렸으나 채팅·음성 지시 제품의 확인·승인(q1-03)은 미조사 | 미충족 · 미승인 |
| 지시 분해 접근의 유형 목록이 [업무 분해·배정 설계 초안](task-model-draft.md)에 반영됨 | 미충족 | 유형 목록은 이 페이지 3절에 있고, 초안에는 로봇 팀 개념(v0.1)과 배정의 속성 '배정 산출 방식'(v0.2)만 반영 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(아이디어 2 3절 제품 사례의 확인·승인(q1-03) 미조사, 지시 분해 접근 유형 목록 초안 미반영, 열린 질문 q1-03·q1-04·q1-05·q1-06)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 확인된 사실은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안"으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 이 영역 정의의 LLM 에이전트와, AI가 만든 작업 계획을 실행에 쓰는 기준을 묻는 이 영역의 질문이 해석과 오해석 방지 단계에 그대로 걸린다. 실행 2026-09-25-04: LLM 출력을 기술 가치 함수·계획기·LTL로 접지·점검하는 방법과 형식 표현–임베딩 서베이를 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료"에 반영 제안(적용 대상 13. 작업 배정 — MRTA와 양쪽 연결). 실행 2026-09-25-12: LLM 다중 로봇 서베이의 네 층 분류와 도구·함수 기반 LLM 에이전트(ChatGPT for Robotics, ROSA, RAI, 한국전자기술연구원 사례)를 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료"에, 공개 프레임워크를 "7. 관련 표준·프레임워크·오픈소스"에 반영 제안(적용 대상 13. 작업 배정 — MRTA와 양쪽 연결)
- [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — '온톨로지로 적합한 로봇을 찾아 배정'하는 일이 이 영역의 배정 문제다. 실행 2026-09-25-04: LLM 기반 분해·팀 구성·할당 파이프라인(SMART-LLM, DART-LLM)을 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료"에 반영 제안. 실행 2026-09-25-12: LLM 직접 배정(COHERENT)과 LLM 정식화 + 선형계획·MILP·계획기 배정(LiP-LLM, Peng 외, LaMMA-P)의 두 방식을 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료"에 반영 제안(학습 기반 배차의 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결)
- [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) — 채팅은 작업자·관리자가 일을 지시하고 확인·승인하는 운영 인터페이스다. 실행 2026-09-25-12: 로봇 운영 제품의 자연어·음성 인터페이스(InOrbit, Formant, 다임리서치 — 모두 벤더 주장, 확인·승인 절차 미확인)를 "6. 대표 접근법과 기술"에 반영 제안
- [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) — 분해 결과가 들어갈 작업 단계·선후관계·완료 조건의 틀을 이 영역이 정의한다

## 8. 출처

[^ref-053]: NVIDIA Research (NVlabs), progprompt-vh — ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (GitHub README), 미확인, https://github.com/NVlabs/progprompt-vh, 접근일 2026-09-25
[^ref-054]: Singh, I. 외, ProgPrompt: Generating Situated Robot Task Plans using Large Language Models, 2022-09, https://arxiv.org/abs/2209.11302, 접근일 2026-09-25 (원문 미열람)
[^ref-055]: Brown University H2R Lab, Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README), 미확인, https://github.com/h2r/Lang2LTL, 접근일 2026-09-25
[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-057]: Tellex, S. 외, Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation, 2011-08, https://ojs.aaai.org/index.php/AAAI/article/view/7979, 접근일 2026-09-25 (원문 미열람)
[^ref-058]: Cohen, V., Liu, J. X., Mooney, R., Tellex, S., & Watkins, D., A Survey of Robotic Language Grounding: Tradeoffs between Symbols and Embeddings, 2024-08, https://www.ijcai.org/proceedings/2024/885, 접근일 2026-09-25 (원문 미열람)
[^ref-059]: Wang, Y. 외(DART-LLM 저자), DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models, 2024-11, https://arxiv.org/abs/2411.09022, 접근일 2026-09-25 (원문 미열람)
[^ref-061]: Izzo, R. A., Bardaro, G., & Matteucci, M. (Politecnico di Milano AIRLab), BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs, 2024-03, https://arxiv.org/abs/2403.12761, 접근일 2026-09-25 (원문 미열람)
[^ref-089]: SMARTlab-Purdue (Purdue University), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README), 미확인, https://github.com/SMARTlab-Purdue/SMART-LLM, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-091]: Cranial-XIX (LLM+P 저자), llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README), 미확인, https://github.com/Cranial-XIX/llm-pddl, 접근일 2026-09-25
[^ref-092]: Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P., LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-093]: Huang, W., Abbeel, P., Pathak, D., & Mordatch, I., Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents, 2022-07, https://proceedings.mlr.press/v162/huang22a.html, 접근일 2026-09-25 (원문 미열람)
[^ref-094]: Huang, W. (language-planner 공식 저장소), language-planner — Official Code for "Language Models as Zero-Shot Planners" (GitHub README), 미확인, https://github.com/huangwl18/language-planner, 접근일 2026-09-25
[^ref-095]: Google Research, Code as Policies: Language Model Programs for Embodied Control (google-research/code_as_policies README), 미확인, https://github.com/google-research/google-research/blob/master/code_as_policies/README.md, 접근일 2026-09-25
[^ref-087]: Google Research, SayCan (google-research/saycan README), 미확인, https://github.com/google-research/google-research/blob/master/saycan/README.md, 접근일 2026-09-25
[^ref-088]: Ahn, M. 외(Google), Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-220]: TASL Lab (LaMMA-P 저자), LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README), 미확인, https://github.com/tasl-lab/LaMMA-P, 접근일 2026-09-25
[^ref-221]: Zhang, X. 외(LaMMA-P 저자), LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner, 2024-09, https://arxiv.org/abs/2409.20560, 접근일 2026-09-25 (원문 미열람)
[^ref-222]: Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자, Large Language Models for Multi-Robot Systems: A Survey, 2025-02, https://arxiv.org/abs/2502.03814, 접근일 2026-09-25 (원문 미열람)
[^ref-223]: Obata, K. 외(Taniguchi 연구실), LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning, 2024-10, https://arxiv.org/abs/2410.21040, 접근일 2026-09-25 (원문 미열람)
[^ref-224]: Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L., Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models, 2025-03, https://arxiv.org/abs/2503.13813, 접근일 2026-09-25 (원문 미열람)
[^ref-225]: arXiv 2512.02810 저자(미확인), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-226]: SHAILAB-IPEC (COHERENT 저자), COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models (GitHub README), 미확인, https://github.com/SHAILAB-IPEC/COHERENT, 접근일 2026-09-25
[^ref-227]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R., IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03, https://arxiv.org/abs/2603.02669, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: Su, X. (IMR-LLM 공식 저장소), IMR-LLM-Code — Industrial Multi-Robot Task Planning and Program Generation using Large Language Models (ICRA 2026) (GitHub README), 미확인, https://github.com/XiangyuSu611/IMR-LLM-Code, 접근일 2026-09-25
[^ref-229]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — ROS Agent (GitHub README), 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-09-25
[^ref-230]: NASA Jet Propulsion Laboratory (nasa-jpl), Custom Agents · nasa-jpl/rosa Wiki, 미확인, https://github.com/nasa-jpl/rosa/wiki/Custom-Agents, 접근일 2026-09-25
[^ref-231]: Microsoft, PromptCraft-Robotics (GitHub README), 미확인, https://github.com/microsoft/PromptCraft-Robotics, 접근일 2026-09-25
[^ref-232]: Vemprala, S. 외(Microsoft), ChatGPT for Robotics: Design Principles and Model Abilities, 2023-07, https://arxiv.org/abs/2306.17582, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: Robotec.ai (RobotecAI), RAI — vendor agnostic agentic framework for Physical AI robotics (GitHub README), 미확인, https://github.com/RobotecAI/rai, 접근일 2026-09-25
[^ref-233]: InOrbit.AI (RoboticsTomorrow 게재 보도자료), InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024, 2024-05-01, https://www.roboticstomorrow.com/news/2024/05/01/inorbit-unveils-robops-copilot-for-ai-powered-robot-optimization-at-automate-2024/22505/, 접근일 2026-09-25 (원문 미열람)
[^ref-234]: InOrbit.AI (RoboticsTomorrow 게재 보도자료), InOrbit.AI Demonstrates the Future of Multi-Vendor Robot Orchestration and Physical AI at Automate 2026, 2026-06-22, https://www.roboticstomorrow.com/news/2026/06/22/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-at-automate-2026/26757/, 접근일 2026-09-25 (원문 미열람)
[^ref-235]: Formant (Business Wire 보도자료), Formant F3 Brings Generative AI and Agentic Reasoning to Robot Ops, 2025-06-30, https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: 와우테일, 다임리서치, 중기부-인텔 '인지니어스' 글로벌 협업 기업 선정, 2026-08-27, https://wowtale.net/2026/08/27/263530/, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: 이종록, 황정훈, 박민철(한국전자기술연구원), LLM 기반 로봇관제시스템의 Agent AI 구축, 미확인, https://d2j16w31g89z0j.cloudfront.net/site/2026w/abs/0560-YDVVV.pdf, 접근일 2026-09-25 (원문 미열람)

## 9. 이력

실행 id `build-2026-09-25`는 확장 아이디어 편입 때의 트랙 시드 생성을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 초안 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-12 | q1-02 | q3-05 | v0.1 → v0.2(배정에 속성 '배정 산출 방식' 추가) | 3 |
| 2026-09-25 | 2026-09-25-04 | q1-01 | q1-05 | v0 → v0.1(개념 로봇 팀 추가) | 2 |
| 2026-09-25 | build-2026-09-25(트랙 시드, 파이프라인 실행 아님) | 없음 | 시드 q1-01~q1-04(4건, [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [업무 분해·배정 설계 초안](task-model-draft.md)에서 생성) | 1 |
