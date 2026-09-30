# 스토리텔러 산출 2026-09-30-09

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md | draft | 영역 심화: 섹션 3~11 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 프런트매터 related_areas·tags·sources·confidence 추가(2차 재실행: 이 페이지 본문 변경 없음) |
| create | docs/topics/2026/2026-09-30-area46-s6.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "6. 대표 접근법과 기술" 절(1,868자)을 옮겼다. 2차: DeepFleet·34. 시뮬레이션·예측용 디지털 트윈 구분 문장의 태그를 [의견]에서 [추정]으로 되돌렸다 |
| create | docs/topics/2026/2026-09-30-area46-s8.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "8. 대표 연구와 자료" 절(1,712자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area46-s4.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "4. 핵심 개념과 용어" 절(1,029자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area46-s10.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(942자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area46-s11.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "11. 열린 질문" 절(669자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area46-s3.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "3. 왜 중요한가" 절(613자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area46-s7.md | draft | 자동 분리: 46. 예측·학습 기반 최적화 의 "7. 관련 표준·프레임워크·오픈소스" 절(463자)을 옮겼다. 2차: League of Robot Runners 행에서 대회 성격 서술(브리프 밖)을 뺐다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 46. 예측·학습 기반 최적화 | 영역 심화: 3~11절 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 1차 수정 지시 11건·2차 수정 지시 2건 이행 | run 2026-09-30-09
- 홈 최근 업데이트: 2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 학습 기반 배정·경로(탐색 기반 대비), 결정 중심 학습, 배터리·고장 예측과 물류창고·병원·제조 공장·기타 현장 사례를 새로 정리했다
- 대분류 최근 업데이트: 2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 3~11절 신규 작성, 개선 근거는 주로 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장이라는 잠정 답을 정리했다
- 세부영역 최근 업데이트: 2026-09-30 — 46. 예측·학습 기반 최적화: 영역 심화 — 3~11절 신규 작성, 각주 14건, 열린 질문 5건 제기

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 결정 중심 학습 | Decision-Focused Learning | 예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다. 대표 방법으로 Smart "Predict, then Optimize"(SPO)가 있다. | 46, 26 | ref-1115 |
| new | 예지 정비 | Predictive Maintenance | 설비·로봇의 상태 신호로 고장이나 성능 저하를 미리 예측해 고장 전에 정비 시점과 조치를 정하는 정비 방식이다. | 46, 38, 57 | ref-1111, ref-1113 |
| new | 모방 학습 | Imitation Learning | 전문가(예: 탐색 기반 계획기)가 만든 해나 행동 기록을 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다. | 46, 27 | ref-1107, ref-199 |
| new | 안내 그래프 | Guidance Graph | 지속형 다중 에이전트 경로 찾기에서 로봇이 지나는 격자 간선에 가중치를 매겨 교통 흐름을 유도하는 그래프로, 배치 전에 최적화하거나 학습된 모델로 생성한다. | 46, 27 | ref-1118 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1105 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 논문 | medium | https://arxiv.org/abs/2508.08574 |
| ref-1106 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 벤더 문서 | medium | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination |
| ref-1107 | Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv) | MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale | 논문 | medium | https://arxiv.org/abs/2409.00134 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2410.21415 |
| ref-1109 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 논문 | high | https://arxiv.org/abs/2407.14931 |
| ref-623 | Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023) | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 논문 | medium | https://arxiv.org/abs/2209.05738 |
| ref-1111 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ |
| ref-1112 | Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors) | Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/ |
| ref-1113 | 파이낸셜뉴스 | 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지 | 기사 | low | https://www.fnnews.com/news/202605280925297568 |
| ref-1114 | ISO (ISO/TC 108) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements | 표준 | medium | https://www.iso.org/standard/88029.html |
| ref-1115 | Elmachtoub, A. N., & Grigas, P. (arXiv) | Smart "Predict, then Optimize" | 논문 | medium | https://arxiv.org/abs/1710.08005 |
| ref-1116 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 논문 | medium | https://arxiv.org/abs/2608.21554 |
| ref-1117 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명 | 벤더 문서 | medium | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 |
| ref-1118 | Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024) | Guidance Graph Optimization for Lifelong Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2402.01446 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? | 46, 54 | 열림 | — |
| new | — | 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? | 46, 38 | 열림 | — |
| new | — | 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? | 46, 47 | 열림 | — |
| new | — | 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? | 46, 23 | 열림 | — |
| new | — | 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? | 46, 61 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 작업 대상 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 물류창고 | 수행 자원 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 물류창고 | 제약 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 물류창고 | 예외·성과 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 병원 | 시작 조건 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 병원 | 작업 대상 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 병원 | 수행 자원 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 병원 | 제약 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 병원 | 예외·성과 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 제조 공장 | 시작 조건 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 제조 공장 | 작업 대상 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 제조 공장 | 수행 자원 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 제조 공장 | 예외·성과 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 기타 | 시작 조건 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 기타 | 작업 대상 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 기타 | 수행 자원 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |
| 기타 | 예외·성과 | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md#5-적용-사례-현장-유형-명시 | 46. 예측·학습 기반 최적화 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) | 평가 프로그램 | Skrynnik, A. 외 (ICLR 2025) | 27, 46, 54 | ref-1109 | https://arxiv.org/abs/2407.14931 |
| ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 | 표준 | ISO (ISO/TC 108) | 38, 46, 57 | ref-1114 | https://www.iso.org/standard/88029.html |

## 추가 조사 요청

- 5절 적용 사례: 상업 시설·가정·실외 현장에서 학습·예측(수요·고장·배터리 예측, 학습 기반 배정·경로)을 로봇 운영에 적용한 1차 자료가 필요하다 — 이번 브리프에는 물류창고·병원·제조 공장·기타 사례만 있다.
- 5절 적용 사례: 네 사례 모두 '완료·인계' 항목(무엇이 확인돼야 작업이 끝났다고 인정하는가)의 근거가 없고, 물류창고(DeepFleet)의 시작 조건과 제조 공장·기타 사례의 제약도 미확인이다. 해당 칸을 채울 자료가 필요하다.
- 3·6·8절: 학습 기반 배정·경로 정책의 실제 운영 개선을 제3자가 측정한 공개 자료가 필요하다 — 현재 운영 수치(DeepFleet 효율 10%, 현대차 5일 전 90% 이상, iFlex)는 벤더·회사 발표뿐이고 교차 확인된 수치가 없다.
- 7절: ISO 13381-1:2025 원문(또는 공식 요약) 열람과, 같은 시리즈 다른 부(13381-2 이후)의 범위 확인이 필요하다 — 이번 실행은 검색 결과·EVS 목록 페이지로만 확인했고 다른 부의 범위 서술은 수정 지시로 뺐다.
- 7절: League of Robot Runners 의 성격(어떤 문제를 겨루는 대회인지, 주최·후원 기관)을 공식 자료로 확인해야 한다 — 이번 브리프 f5 에는 SILLM 이 2023년 우승 해법을 앞섰다는 저자 보고만 있어, 2차 수정 지시로 '지속형 MAPF 경진대회'라는 성격 서술을 뺐다.
- 8절: MAPF-GPT 의 학회 게재(AAAI 2025 여부)와 Smart "Predict, then Optimize" 의 학술지 게재 연도를 공식 페이지에서 확인해야 한다 — 이번 실행은 미확인으로 두었다.
- 6·8절: 제조 공장의 다중 에이전트 강화학습 AMR 주문 배차(Malus 외, CIRP Annals 2020)와 다중 로봇 작업 배정 체계적 문헌 고찰(ACM Computing Surveys 2024)은 원문 접근 실패(403)로 넣지 못했다. 열람 가능한 판본으로 재확인이 필요하다.
- 11절 관련: 국내 학술지·국내 현장의 학습 기반 다중 로봇 배정·경로 적용 사례와 국내 예지 정비 표준·지침 자료가 필요하다.
- 교차 규칙에 따른 다음 실행 후보: 25. 작업 배정 — MRTA 페이지에 학습 기반 배정(RTAW, Garces 외)과 핵심 질문 잠정 답, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 POGEMA·MAPF-GPT·SILLM·안내 그래프 최적화, 38. 모니터링·이상 탐지·원인 분석 페이지에 청소 로봇 예지 정비·현대차 고장 예측 반영을 검토해야 한다(하루 갱신 예산 안에서).

## 이행한 수정 지시

- f3 MARL 일반화 수정 — 6절 '학습 기반 경로·교통 관리'에서 'MARL 방법(QPLEX·VDN·QMIX 등)은 크게 뒤처졌고, 그 가운데 MAMBA 는 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했다'로 좁혀 [사실][^ref-1109]로 썼고, 3절 핵심 질문 답도 MAMBA 사례로 한정했다.
- f15 다른 부 범위 삭제 — 4절·7절의 ISO 13381-1 서술에서 '같은 시리즈의 다른 부가 성능 추세·사이클 기반 수명 사용·잔여 유효 수명 모델을 다룬다'는 부분을 넣지 않고 3판·2015년 2판 대체·목적만 [사실]로 썼다.
- ref-1114 제목·미열람 표시 — 13절 각주와 reference_updates·standards_updates 의 제목을 'ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements'로 고치고, 각주 접근일 뒤에 ' (원문 미열람)'을 붙였으며 reference_updates 항목에 source_unopened: true 를 넣고 summary 를 '원문 미열람. '으로 시작했다.
- ref-1117 제목 — 13절 각주와 reference_updates 의 제목을 "'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명"으로 고쳤다(게시일 2021-07-28).
- f4 AAAI 표기 — 6절·8절 본문에 'arXiv 2409.00134(2024-08 제출, 2025-04 개정)'로 적고, 각주·reference_updates 의 기관 표기에서 'AAAI 2025'를 뺐다(reference_updates summary 에는 'AAAI 2025 게재는 미확인'으로 적었다).
- f11 게재 연도 — 8절에 'arXiv 1710.08005, 2017-10 제출, 2020-11 개정, 학술지 게재 연도 미확인'으로 적고, 각주·reference_updates 기관 표기에서 Management Science 를 뺐으며 summary 를 '학술지 게재 연도는 미확인'으로 고쳤다.
- f20 배터리 셀 관리 삭제 — 9절 연계 대상 문장과 표에서 '배터리 셀 관리'를 빼고 로봇 부품 수준 상태 감시(모터 전류·진동·IMU)와 전사 주문 수요예측만 연계 대상으로 두었다. 배터리 예측(f12)은 ROP 직접 범위 쪽에만 썼다.
- f2·f14·f16 벤더 주장 병기 — 5절 표·서술과 9절 표에서 이 세 finding 을 쓴 모든 문장을 '[추정] 벤더 주장[^ref-…]'로 쓰고, 효율 10%·5일 전 90% 이상 수치를 [사실]로 쓰지 않았으며, iFlex 서술은 '연계 대상:'으로 시작했다.
- 5절 현장 유형 — 사례를 물류창고(DeepFleet, iFlex 는 연계 대상 보충 서술)·병원(Garces 외)·제조 공장(현대차)·기타(대학 캠퍼스 청소 로봇) 네 묶음으로 쓰고, f12 는 6절 '배터리·고장 예측' 근거로만 썼으며, 상업 시설·가정·실외 사례는 찾지 못했다고 적었다. site_matrix_updates 는 이 네 현장 유형의 칸만 냈다.
- 용어집 '결정 중심 학습' — term_en 을 'Decision-Focused Learning'으로 두고 SPO 는 정의 안에서 대표 방법으로 적었으며, 4절 본문도 같은 방식(대표 방법인 SPO)으로 썼다.
- 8절 저자 보고 — 8절 도입에 모든 수치가 단일 출처 저자 보고이고 교차 확인된 수치가 없다고 밝히고, SILLM(+137.7%·+16.0%)·RTAW(14%)·Pookkuttath 외(91%)·Poskart 외(결정계수) 수치를 '저자 보고:'로 표시했다(5절·6절의 같은 수치도 '저자는 … 보고했다'로 썼다).
- 분량 초과 자동 분리: 46. 예측·학습 기반 최적화 본문 10,784자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,283자
- 2차: 6절 DeepFleet·34. 시뮬레이션·예측용 디지털 트윈 구분 문장 태그 되돌림 — 분리 페이지 docs/topics/2026/2026-09-30-area46-s6.md 3절 '대규모 플릿 기반 모델' 소제목의 '이 모델의 미래 교통 예측은 … 34. 시뮬레이션·예측용 디지털 트윈과 구분해 다룬다.' 문장 태그를 [의견][^ref-1106]에서 f21 의 1차 처분대로 [추정][^ref-1106]으로 고쳤다. 원 세부영역 페이지에는 이 문장이 없어 바꿀 곳이 없었다.
- 2차: 7절 League of Robot Runners 성격 서술 삭제 — 분리 페이지 docs/topics/2026/2026-09-30-area46-s7.md 3절 표의 'League of Robot Runners' 행에서 '지속형 MAPF 경진대회'를 빼고 '이 영역과의 관계' 칸을 'SILLM 저자는 이 대회 2023년 우승 해법을 앞섰다고 보고했다'로만 두었으며, 태그·각주 [사실][^ref-199] 는 다른 행과 같은 형식으로 출처 칸에 두었다. 대회 성격 확인은 additional_research_requests 로 넘겼다.
