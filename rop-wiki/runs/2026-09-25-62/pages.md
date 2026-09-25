# 스토리텔러 산출 2026-09-25-62

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | draft | q2-03 답함(3절 {#q2-03} 신설: 지시–정답 공개 데이터셋·지표·쌍 구조·물류 공백), 상태 줄·2·4·5·6·7·8·9절 갱신, 후속 질문 q5-04·q5-05 |
| update | docs/ideas/nl-task-chatbot.md | draft | 4절 도입 문단과 q2-02 소절 끝의 q2-03 미조사 문장을 새 소절 안내로 바꾸고 '해석·분해 평가 데이터' 소절 신설, 새 각주 정의 추가 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 산출물 링크 갱신: 아이디어 2 4절에 해석·분해 평가 데이터(q2-03) 소절 작성, 초안 변경 없음(실행 2026-09-25-62) 기록 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 2 | q2-03 답함(지시–정답 공개 데이터셋·지표 비교, 필요한 쌍 구조·물류 데이터 공백·배정 정답 부재는 추정), 새 질문 q5-04·q5-05, 아이디어 2 4절 평가 데이터 소절 추가, 초안 변경 없음 | run 2026-09-25-62
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: q2-03 답함 — 해석·분해 평가용 지시–정답 공개 데이터셋(ALFRED·SMART-LLM·AmbiK 등) 비교, 물류 창고 지시 데이터셋은 검색 범위에서 찾지 못함(추정)
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: 13. 작업 배정 — MRTA 관련 LLM 다중 로봇 배정 평가 데이터셋(SMART-LLM, MAT-THOR)과 지표 정리, 배정 최적성을 정답으로 둔 자료는 확인되지 않음(추정)
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇 단계 2(q2-03)에서 LLM 배정 평가 데이터셋·지표를 8. 대표 연구와 자료에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 목표 조건 | Goal Condition | 작업이 끝났을 때 환경이 만족해야 하는 상태 조건의 집합으로, 지시 수행 벤치마크에서 계획·실행 결과가 맞았는지를 판정하는 정답으로 쓰인다. | 23, 27, 13 | ref-540, ref-090, ref-544 |
| new | 신호 시간 논리 | Signal Temporal Logic (STL) | 연속 시간 신호에 대해 시간 구간이 붙은 조건(예: 10초 안에 도착)을 기술하는 형식 논리로, 로봇 임무 명세에 쓰인다. | 27, 23 | ref-548 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 오픈소스 문서 | high | https://github.com/askforalfred/alfred |
| ref-540 | Shridhar, M. 외 | ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | 논문 | medium | https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 오픈소스 문서 | high | https://github.com/lbaa2022/LLMTaskPlanning |
| ref-542 | LoTa-Bench 저자(arXiv 2402.08178) | LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents | 논문 | medium | https://arxiv.org/abs/2402.08178 |
| ref-543 | Amazon Alexa (alexa/teach GitHub) | TEACh: Task-driven Embodied Agents that Chat (GitHub README) | 오픈소스 문서 | high | https://github.com/alexa/teach |
| ref-544 | Zhang, X. 외(LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner | 논문 | medium | https://arxiv.org/abs/2409.20560 |
| ref-545 | Snips (sonos/nlu-benchmark GitHub) | nlu-benchmark — 2017-06-custom-intent-engines (README) | 오픈소스 문서 | high | https://github.com/sonos/nlu-benchmark/tree/master/2017-06-custom-intent-engines |
| ref-546 | 한국지능정보사회진흥원(AI Hub) | 일상생활 작업 및 명령 수행 데이터(임무수행 명령어) | 정부·연구기관 | medium | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71547 |
| ref-547 | OpenBench 저자(arXiv 2502.09238) | OpenBench: A New Benchmark and Baseline for Semantic Navigation in Smart Logistics | 논문 | medium | https://arxiv.org/abs/2502.09238 |
| ref-548 | Högskolan Väst (DiVA 학위논문, 저자 미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 논문 | low | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 오픈소스 문서 | medium | https://github.com/SMARTlab-Purdue/SMART-LLM |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-164 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 오픈소스 문서 | medium | https://github.com/tasl-lab/LaMMA-P |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 오픈소스 문서 | medium | https://github.com/cog-model/AmbiK-dataset |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 논문 | medium | https://arxiv.org/abs/2409.00557 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 논문 | medium | https://arxiv.org/abs/2302.11649 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 2 페이지 3절 q2-03: TEACh 논문(arXiv 2110.00534)을 출처로 등록해 TATC 를 포함한 세 벤치마크 구성을 원문으로 확인할 필요가 있다(현재 README 에서 TATC 미확인).
- 단계 2 페이지 3절 q2-03: LoTa-Bench 의 성공률 지표와 SMART-LLM·ALFRED·MAT-THOR 데이터셋 수치는 논문 원문 미열람 저자 보고값이다. 원문 또는 독립 출처로 교차 확인이 필요하다.
- 단계 2 페이지 3절 q2-03: Lang2LTL OSM 평가 자료의 지역 수(21·22개)와 명령 수가 판마다 다르게 요약된다. 판별 수치 확인이 필요하다.
- 단계 2 페이지 3절 q2-03: AI Hub '일상생활 작업 및 명령 수행 데이터'의 구축 기관·규모·정답 형식·발행일과 Högskolan Väst 학위논문의 저자·발행일·평가 자료 규모 확인이 필요하다.
- 단계 5 준비: PlanBench 에 Logistics 도메인이 포함되는지 확인하면 물류 계획 평가 자료 후보를 판단할 수 있다(이번 실행에서 README 로 확인하지 못해 제외).
- 운영 참고: 단계 페이지 상태 줄(H1 아래)은 H2 절 밖이라 patches 로 바꿀 수 없어, 이번 실행은 단계 2 페이지만 전체 content 로 냈다. 상태 줄을 patches 로 갱신할 수단을 pipeline 담당에게 요청한다.
- 백로그 정리 요청: q3-09 와 q3-10, q1-05 와 q1-06 이 사실상 같은 질문으로 중복 등록되어 있다(1차 검증 지적). 백로그 담당의 폐기·병합 판단이 필요하다.

## 이행한 수정 지시

- f11 — 단계 2 페이지 3절 q2-03 에서 말뭉치(47개 템플릿·2,125개 식·약 5만 개 발화)만 '저자 보고, 원문 미열람'과 함께 [사실]로 쓰고, OSM 평가 자료는 '지역 수는 요약에 따라 21·22개로 다르고 명령 수는 미확인'으로 [추정] 처리했다.
- f4 — TEACh 문장을 README 근거(Commander 와 수행 역할 README 표기 Driver·논문 표기 Follower, AI2-THOR, EDH·TfD, 세 라이선스)로만 쓰고 TATC 는 README 에서 확인되지 않아 미확인이라고 적었다.
- f3 — README(ref-541)는 자동 정량화와 두 데이터셋·시뮬레이터 쌍의 근거로만 쓰고, 성공률 비교 문장에는 원문 미열람 논문 ref-542 각주를 달았다(단계 페이지·아이디어 페이지 모두).
- f1 — AI2-THOR 버전을 'README 기준 2.1.0'으로 적었다.
- f7 — README(ref-164)의 '두 복잡도 수준' 표현과 논문(ref-544)의 '복합 30·복잡 20·모호 지시 20' 구성을 함께 적고, 70개 작업·5개 평면도가 저자 보고(원문 미열람)임을 같은 문장에 밝혔다.
- f2·f6·f7·f9·f11 — 수치 문장마다 '저자 보고, 원문 미열람'을 적었고, f2 에는 README 와 논문이 같은 저자 계열이라 독립 교차 확인이 아님을 같은 문장에 적었다. 아이디어 페이지 비교표에는 수치를 넣지 않았다.
- f12 — AI Hub 문장에 '구축 기관·규모·정답 형식·발행일 미확인'을 병기하고 가정(일상생활) 환경이며 물류 지시 데이터가 아님을 적었다.
- f14 — 학위논문 문장에 '저자·발행일·평가 자료 규모 미확인, 학위논문 단일 출처'를 같은 문장에 적고 학위 수준은 쓰지 않았다.
- f13 — '연계 대상:' 표시를 유지하고 실외 배송 항법은 분류 원문 9장 업종별 조건 경계에 속하는 평가 자료 사례로만 본다고 적었다.
- f15·f16·f17·f18 — 모두 [추정]을 유지하고 '이 위키의 정리(추론)'임을 밝혔으며, f16 에는 '부재의 확인은 아님'을 유지했고 흐름 매트릭스 갱신(flow_matrix_updates)에 넣지 않았다.
- 원문 미열람 표시 — ref-540·542·544·546·547·548·090·359·056 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-548 각주의 기관 자리는 'Högskolan Väst (DiVA 학위논문, 저자 미확인)', 발행일 자리는 '미확인'으로 두었다.
- open_questions_new 1건 — open_question_updates 에 넣지 않았고, 국내 물류 지시 데이터셋을 찾지 못한 점을 단계 2 페이지 4절 남은 불확실성에 f16 근거로 적어 트랙 백로그 q1-06 에 연결했다.
- 단계 2 페이지 2절 — q2-03 을 '답함', 답한 실행 id 2026-09-25-62, 답 위치 #q2-03 으로 바꾸고 3절에 '### q2-03 … {#q2-03}' 소제목을 신설했으며, 상태 줄을 열린 질문 4건·답한 질문 3건으로 맞췄다(상태 줄이 H2 절 밖이라 이 페이지는 전체 content 로 냈다).
- 단계 2 페이지 6절 — 첫 항목을 평가 데이터 소절 반영으로 '충족', 둘째 항목을 '미충족', 검증 판정 칸을 두 항목 모두 '미충족 · 미승인'으로 두고, 아래 줄을 지시 문구 그대로 '다음 단계로 전환: 아니오(작업 모델 정보 항목 일부만 반영 — 작업 요구 적재물 속성·완료 조건 미확정, 열린 질문 q2-04·q2-05·q2-06·q2-07)'로 썼다.
- 아이디어 2 페이지 4절 — 도입 문단과 q2-02 소절 끝의 'q2-03 은 아직 조사하지 않았다' 문장을 새 소절 '해석·분해 평가 데이터' 안내로 바꾸고, 새 소절 비교표가 README·논문의 표를 옮긴 것이 아니라 이 위키가 구성한 것임을 밝혔으며, 지표는 6. 검증 방법에서 단계 5 결과로 다룬다고 적었다.
- 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영, 23. 시험·형식 검증·벤치마크 — 세부영역 페이지를 고치지 않고 area_reflection_proposals 로만 냈으며, 13 과 27 의 제안과 단계 페이지 7절에 서로 연결을 표시했다.
- 새 질문 두 건 — q5-04(f16), q5-05(f17)로 단계 5 에 등록하고, 정답 배정 생성 질문 문장 끝에 '(관련: q3-05, q5-01)'을 붙였다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.5
- 트랙 로그 항목: 답한 질문: q2-03(해석·분해 평가용 지시–정답 공개 데이터셋과 지표, f1~f18) / 새 질문: q5-04(f16), q5-05(f17, 관련 q3-05·q5-01) / 온톨로지 변경: 없음(평가 데이터는 업무 분해·배정 설계 초안의 개념·관계가 아니라 검증 자료, v0.5 유지) / 완료 조건 평가: 미충족(부족: 작업 요구 적재물 속성·업무 완료 조건 미확정; 아이디어 2 4절 평가 데이터 소절은 이번 반영으로 채움) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영, 23. 시험·형식 검증·벤치마크 3건 / 다음 실행 제안: q2-04, q2-05, q2-06, q2-07 / 백로그 정리 요청: q3-09·q3-10, q1-05·q1-06 중복(1차 검증 지적)
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 4, 답함 3, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-03 | 답함 | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md#q2-03 | — | — | — |
| q5-04 | 열림 | — | 물류 지시 평가 자료를 자체 구축할 때 지시–정답 쌍의 정답을 무엇(업무 분해·배정 설계 초안의 작업 모델 인스턴스, 최종 상태·목표 조건, 배정 결과)으로 두고, ALFRED 목표 조건·SMART-LLM 최종 상태·AmbiK 명확화 질문 형식을 화물·로케이션·기한 항목으로 어떻게 확장하는가? (q2-03 에서 파생) | 5 | f16 |
| q5-05 | 열림 | — | 배정 적합성을 평가하려면 목표 상태 달성 외에 정답 배정이나 목적함수 기준값이 필요한데, 이를 최적화 해법기(MILP 등)로 생성해 LLM 배정 결과와 비교하는 정답으로 쓸 수 있는가? (q2-03 에서 파생) (관련: q3-05, q5-01) | 5 | f17 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 8. 대표 연구와 자료 | LLM 다중 로봇 계획·배정 평가 데이터셋(SMART-LLM 네 범주 상위 지시와 가용 로봇·최종 상태, MAT-THOR 정답 PDDL·목표 조건)과 지표(목표 조건 재현율 GCR, 정답 전이 수 대비 로봇 활용도 RU, 논문 기준 저자 보고)를 추가하고, 이 벤치마크들이 배정의 전체 최적성(이동거리·납기)을 정답으로 두지 않는 것으로 보인다는 점(추정)을 분류 원문 질문·oq-052 와 연결한다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽에 연결한다. |
| 27 | 8. 대표 연구와 자료 | LLM 지시 해석·계획 평가 벤치마크(LoTa-Bench 자동 정량화, AmbiK 모호 지시 1000쌍, NoisyToolBench 불완전 지시, Lang2LTL 발화–LTL 말뭉치, Snips 의도·슬롯)와 해석 정확도·계획 목표 달성도를 나눠 재는 두 층 평가(추정)를 추가하고, 적용 대상 13. 작업 배정 — MRTA 와 18. 사람–로봇 협업·운영 인터페이스에 연결한다. |
| 23 | 8. 대표 연구와 자료 | 지시 수행 벤치마크(ALFRED 목표 조건·전문가 시연, LoTa-Bench 시뮬레이터 기반 자동 평가)와 시뮬레이터 최종 상태·목표 조건으로 판정하는 평가 방식을 추가하고, 물류 창고 지시를 정답과 짝지은 평가 자료를 검색 범위에서 찾지 못했다는 점(추정, 부재 확인 아님)을 적는다. |
