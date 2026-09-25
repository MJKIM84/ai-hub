# 스토리텔러 산출 2026-09-25-98

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md | draft | q5-01 답함(네 층 평가 지표, 3절 신설), 2절에 단계 5 백로그 질문 반영(q5-06 폐기 제외)·새 질문 q5-11·q5-12, 4·5·6·8·9절 갱신, 상태 줄 진행 중. 시드 단계 페이지라 상태 줄(H1 아래)까지 고치려고 전체 content 로 보냄 |
| update | docs/ideas/nl-task-chatbot.md | draft | 6절 '아직 조사되지 않음'을 바꾸고 '평가 지표' 소절 신설(네 층 지표 구성·배정 분리 보고·슬롯별 지표 병행, 모두 추정), 새 출처 각주 추가 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 산출물 링크 갱신: 초안 v0.8 유지(실행 2026-09-25-98 변경 없음), 아이디어 2 링크 설명에 CLI 지정 질문으로 단계 5 q5-01 을 다뤘음과 현재 단계 3 유지를 적음. 상태 줄은 입력 그대로(현재 단계 3, 마지막 트랙 실행 2026-09-25) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 5 | q5-01 답함(해석·분해·배정 적합성·일정 품질 네 층 평가 지표, 신뢰도 low), 후속 질문 2건, q5-06 폐기, 아이디어 2 6절 평가 지표 소절 신설, 초안 v0.8 유지 | run 2026-09-25-98
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: q5-01 에 답해 해석·분해·배정 적합성·일정 품질 네 층의 평가 지표를 정리(신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: 13. 작업 배정 — MRTA 의 배정 적합성을 실행 가능성과 최적성 간격으로 나눠 재는 지표와 14. 작업 순서·스케줄링 의 일정 품질 지표 정리(반영 제안)
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 5: 배정 결과를 최근접 기준선·해법기 기준값과 견주는 평가 지표 정리, 6. 대표 접근법과 기술 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 결합 목표 정확도 | Joint Goal Accuracy (JGA) | 대화 상태 추적에서 한 턴의 모든 슬롯 값을 정답과 똑같이 맞힌 턴의 비율로, 하나라도 틀리면 그 턴을 오답으로 세는 엄격한 지표다. | 27, 18, 23 | ref-730 |
| new | 최적성 간격 | Optimality Gap | 어떤 해의 목적함수 값이 최적값(또는 해법기가 찾은 최선 값·하한)과 얼마나 떨어져 있는지를 비율로 나타낸 값으로, 실행 가능한 해의 품질을 재는 데 쓴다. | 13, 14, 23, 27 | ref-592 |
| new | 일정 안정성 | Schedule Stability | 재스케줄링 뒤 일정이 원래 일정에서 얼마나 바뀌었는지(작업 시작·완료 시각의 편차 등)를 재는 성질로, 성과 지표의 변화를 재는 강건성과 구분된다. | 14, 20 | ref-734, ref-733 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-730 | Kim, T., Yoon, H., Lee, Y., Kang, P., Bang, J., & Kim, M.(ACL 2022 Short Papers, 소속 미확인) | Mismatch between Multi-turn Dialogue and its Evaluation Metric in Dialogue State Tracking | 논문 | medium | https://aclanthology.org/2022.acl-short.33/ |
| ref-731 | Qin, L., Xie, T., Che, W., & Liu, T.(IJCAI 2021) | A Survey on Spoken Language Understanding: Recent Advances and New Frontiers | 논문 | medium | https://www.ijcai.org/proceedings/2021/0622.pdf |
| ref-732 | Gramopadhye, M., & Szafir, D. | Generating Executable Action Plans with Environmentally-Aware Language Models | 논문 | medium | https://arxiv.org/abs/2210.04964 |
| ref-733 | Goren, S., & Sabuncuoglu, I.(IIE Transactions 40(1), 66-83) | Robustness and stability measures for scheduling: single-machine environment | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/07408170701283198 |
| ref-734 | Rangsaritratsamee, R., Ferrell Jr., W. G., & Kurz, M. B.(Computers & Industrial Engineering 46) | Dynamic rescheduling that simultaneously considers efficiency and stability | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0360835203000950 |
| ref-623 | Agrawal, A. 외(RTAW 저자, ICRA 2023) | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 논문 | medium | https://arxiv.org/abs/2209.05738 |
| ref-736 | Aakriti05 (RTAW 공식 저장소) | RTAW-Centralised-multi-robot-task-allocation — README | 오픈소스 문서 | medium | https://github.com/Aakriti05/RTAW-Centralised-multi-robot-task-allocation |
| ref-737 | Patil, S. G. 외(Gorilla/BFCL 저자, ICML 2025 PMLR v267) | The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models | 논문 | medium | https://proceedings.mlr.press/v267/patil25a.html |
| ref-738 | ShishirPatil (gorilla GitHub) | berkeley-function-call-leaderboard — README | 오픈소스 문서 | medium | https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 작업 대상 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 완료·인계 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 5 페이지 3절과 아이디어 2 6절: 가상 현장·가상 로봇으로 지시 시나리오를 재현하는 검증 절차와 한계(q5-02)가 필요하다 — 완료 조건 '평가 지표와 검증 절차'의 절반이 비어 있다.
- 트랙 개요 3절: 가설 1~3 판정(q5-03)에 쓸 단계 1~4 결과의 판정 근거가 필요하다 — 가설 판정표 완료 조건.
- 실험 페이지: 사용자에게 제안할 실험 계획(네 층 지표를 물류 지시 시나리오에서 산출하는 실험)을 쓰려면 대상 시뮬레이터·데이터 구성 근거가 필요하다.
- 단계 5 3절: 물류 지시 해석·분해·배정·일정을 함께 평가한 벤치마크나 국내 자료가 있는지 추가 검색이 필요하다(이번 검색 18회 범위에서는 없음).
- 단계 5 3절: Goren·Sabuncuoglu(ref-733)의 강건성·안정성 정의 원문 문구 확인이 필요하다.
- 참고문헌: ref-623 저자 목록 전체와 ref-730 저자 소속 확인이 필요하다.
- 퍼블리셔: 보류된 실행 2026-09-25-82 가 ref-730~ref-744 를 다른 출처에 쓴 기록이 있어 id 병합 충돌 확인이 필요하다.
- 백로그 정리: q3-09·q3-10, q3-12·q3-13, q4-09·q4-10, q1-05·q1-06 중복 등록을 해당 단계 실행에서 정리해야 한다.

## 이행한 수정 지시

- f3 연구 이름 표기 — 'G-PlanET'을 쓰지 않고 'Gramopadhye·Szafir(arXiv 2210.04964, 2022-10, IROS 2023)'로만 표기했고, 310%·147% 뒤에 '(저자 보고, 원문 미열람, VirtualHome·ActivityPrograms 조건)'을 붙였다.
- f11 정의 분리 — 대리 척도 두 가지 개발만 [사실]로 쓰고 강건성·안정성 정의는 별도 [추정] 문장에 '원문 문구는 확인하지 못했다'를 병기했다. 용어 '일정 안정성' 설명에도 같은 한계를 적었다.
- f1 PLW·SPL 구분 — 경로 길이 가중 지표를 용어집 SPL 과 같은 지표로 다루지 않는다고 명시하고, 목표 조건을 glossary goal-condition 페이지로 링크했다.
- f7 출처 분리 — 2,000개 쌍과 세 평가 범주는 ref-737 각주에만, '실행 가능한 함수 호출 평가'와 v1 AST 평가는 ref-738 각주에만 달았고, 같은 저자라 독립 교차가 아님을 본문과 4절 불확실성에 적었다.
- f6·f8·f9 수치 조건 — 1.09%p·5.47%p(MultiWOZ), 85.0%·0%·9.41%(모든 모델), TTD 최대 14%(25~1000초)·최대 1000대 시뮬레이션 뒤에 조건과 '저자 보고, 원문 미열람'을 두었고, '고려대학교 등'을 빼고 ref-730 기관 표기를 '소속 미확인'으로 바꿨다.
- f2 연결 — SMART-LLM 지표를 새로 서술하지 않고 단계 2 q2-03 답 링크와 기존 각주 ref-090 으로만 연결했다.
- f14 재사용 — 13. 작업 배정 — MRTA 3절의 ref-400 문장과 각주를 그대로 쓰고 창고 조건 실측 부재는 oq-052 로 연결했으며 새 열린 질문은 만들지 않았다.
- f12·f13·f15·f16·f17 태그 — 모두 [추정]으로 싣고 네 층 표 아래에 '이 위키의 종합이며 네 층을 한 번에 제시한 출처는 없고, 근거 환경이 물류 지시 조건이 아니다'를 두었으며, f16 은 설명용 가상 시나리오로 밝히고 시각·도크 번호 같은 수치를 뺐다.
- 각주·reference_updates — 신규 미열람 ref-730~735·737 은 접근일 뒤 ' (원문 미열람)'과 source_unopened: true, ref-736·738 은 표시 없이 두었고, 재사용 ref-540·545·090·592·400·111 은 기존 페이지 각주 줄을 그대로 썼다.
- 단계 5 2절 — q5-01 을 답함·2026-09-25-98·[답](#q5-01)로 바꾸고 3절에 '### q5-01 … {#q5-01}' 소제목을 두었으며, 새 질문 q5-11·q5-12 를 2절 표와 5절 표에 단계 5 로 올리고 q5-12 의 '(관련: q5-05, oq-052)'를 유지했다.
- backlog q5-06 — backlog_updates 에 status 폐기로 내고 단계 5 페이지 2절 표에서 뺐다(표 머리 설명에 q5-05 중복 사유 기재).
- 단계 5 6절 — 세 행을 미충족 · 미승인으로, 첫 행 근거를 지시 문구대로, 전환 줄을 지시 문구대로 썼고 stage_transition 은 넣지 않았으며, 상태 줄을 '진행 중 · 열린 질문: 10건 · 답한 질문: 1건 · 완료 조건: 미충족'으로 2절 표와 맞췄다.
- 트랙 개요 — 상태 줄(현재 단계 3, 마지막 트랙 실행 2026-09-25)은 입력 그대로 두고, 6절 아이디어 2 링크 설명에 이번 실행이 CLI 지정 질문으로 단계 5 를 다뤘음과 현재 단계 3 유지를 적었다.
- 아이디어 2 6절 — '아직 조사되지 않음'을 바꾸고 '평가 지표' 소절에 f12·f13·f15 를 [추정]으로, f1·f4·f5(슬롯별 지표 근거)·f6·f7·f8·f9·f10·f11 을 요약 수준으로 싣고 4절 '해석·분해 평가 데이터' 소절로 링크했으며 q5-02·q5-03 미조사를 적었다.
- 용어집 — 결합 목표 정확도·최적성 간격·일정 안정성 3건을 신규로 내고, 본문에서 intent-recognition·slot-filling·goal-condition·milp 용어집 페이지로 링크했다.
- 세부영역 반영 제안 — 13·14·23·27 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그 항목으로만 남겼으며, f9 강화학습 배차는 27. AI·학습·적응과 모델 운영과 13. 작업 배정 — MRTA 양쪽 연결로만, f10·f11 은 물류 적용 미확인을 제안 문안에 밝혔다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q5-01(해석·분해·배정 적합성·일정 품질 네 층 지표, 근거 f1~f18, 신뢰도 low) / 새 질문: q5-11(슬롯별 오류 비용·치명 오류 집계, f15), q5-12(해법기 기준값·최적성 간격 기준, f13, 관련 q5-05·oq-052) / 백로그 정리: q5-06 폐기(q5-05 중복 등록) / 온톨로지 변경: 없음(업무 분해·배정 설계 초안 v0.8 유지 — 평가 지표는 작업 모델의 개념·관계가 아니라 검증 방법) / 완료 조건 평가: 미충족(부족: 검증 절차 q5-02, 가설 판정표 q5-03, 실험 계획; 앞 단계 3·4 완료 미승인) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 14. 작업 순서·스케줄링, 23. 시험·형식 검증·벤치마크, 27. AI·학습·적응과 모델 운영 4건(각 6. 대표 접근법과 기술) / 다음 실행 제안: q5-02, 이어서 q5-05·q5-12, q5-03. 참고: 이 실행은 CLI 지정 질문으로 단계 5 를 다뤘고 트랙 현재 단계는 단계 3 으로 둔다.
- 개요 진행 현황: 단계 5 진행 중 — 열린 질문 10, 답함 1, 완료 조건 미충족(CLI 지정 질문 q5-01 로 다뤘으며 트랙 현재 단계는 단계 3 유지)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q5-01 | 답함 | docs/tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md#q5-01 | — | — | — |
| q5-06 | 폐기 | — | — | — | — |
| q5-11 | 열림 | — | 물류 지시 해석 평가에서 슬롯별 오류 비용(기한·대상 화물·장소 오류가 오배정·납기 지연으로 이어지는 정도)을 어떻게 추정해 슬롯 가중치나 치명 오류 집계 기준으로 정하며, 모두 맞아야 정답인 전체 정확도와 어떻게 함께 보고하는가? (q5-01 에서 파생) | 5 | f15 |
| q5-12 | 열림 | — | 배정 적합성의 최적성 간격을 재기 위한 해법기 기준값을 창고 규모 사례에서 시간 제한 때문에 최적해로 인증하지 못할 때, 최선 해·하한 가운데 무엇을 기준으로 삼고 최근접 배정 기준선과 함께 어떻게 보고하는가? (q5-01 에서 파생) (관련: q5-05, oq-052) | 5 | f13 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 배정 결과를 실행 가능 배정 비율과 해법기 기준값 대비 최적성 간격으로 나눠 평가하는 방식(ConstraintBench 시설 입지 85.0%·0%·9.41%, 저자 보고), 창고 배정의 총 이동 지연(TTD) 지표와 탐욕 픽업 거리 기준선(RTAW, 저자 보고), 분류 원문 질문을 최근접 기준선·해법기 기준값과 비교하는 설계(추정, oq-052 연결). RTAW 의 강화학습 배차는 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 양쪽 연결로만 적는다. |
| 14 | 6. 대표 접근법과 기술 | 재스케줄링 일정 품질을 효율(makespan·납기 지연)과 안정성(작업 시작 시각 편차)으로 재는 지표(2004)와 강건성·안정성 대리 척도(2008, 정의 원문 문구 미확인). 두 연구는 제조 작업장·단일 기계 조건이며 물류 적용은 미확인이다. |
| 23 | 6. 대표 접근법과 기술 | 지시 수행·계획 평가 지표: ALFRED 목표 조건 성공률과 경로 길이 가중 지표, Gramopadhye·Szafir 의 LCS 순서 일치, BFCL 의 도구 호출 AST·실행 평가, 그리고 해석·분해·배정 적합성·일정 품질 네 층 지표 구성(이 위키의 종합, 추정). |
| 27 | 6. 대표 접근법과 기술 | LLM 해석·출력 평가 지표: 의도 정확도·슬롯 F1·전체 정확도(SLU 서베이), 결합 목표 정확도의 과소평가와 상대 슬롯 정확도(ACL 2022), 도구 호출 AST·실행 평가(BFCL), LLM 직접 최적화의 실행 가능성–최적성 분리(ConstraintBench). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결한다. |
