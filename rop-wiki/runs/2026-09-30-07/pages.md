# 스토리텔러 산출 2026-09-30-07

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | draft | 영역 심화: seed → draft, 3~11절 신규 작성(자동 분리 후 요약·링크), 각주 15건, 1차 수정 지시 10건 이행. 2차: 5절 도입 문장을 가정 [사실]과 제조 공장·물류창고 [추정] 벤더 주장으로 분리, 5절에 VLA(용어집 링크)·PoC, 7절에 PDDL 풀어쓰기 |
| create | docs/topics/2026/2026-09-30-area44-s6.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "6. 대표 접근법과 기술" 절(1,491자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area44-s4.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "4. 핵심 개념과 용어" 절(1,296자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area44-s8.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차: RT-2 '출발점' 평가 삭제·f1·f3 범위로 재서술, LLM+P 문장을 분리해 [사실][^ref-092] 부여(각주 정의·sources 추가), [의견]은 Kambhampati 외 주장에만 |
| create | docs/topics/2026/2026-09-30-area44-s10.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(953자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area44-s7.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "7. 관련 표준·프레임워크·오픈소스" 절(651자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area44-s3.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "3. 왜 중요한가" 절(584자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area44-s11.md | draft | 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "11. 열린 질문" 절(527자)을 옮겼다(2차 재실행에서 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 44. 로봇 기반 모델·언어 모델 계획 | 영역 심화: 3~11절 신규 작성(VLA·교차 형태 학습, 언어 모델 계획 검증·불확실도 기반 도움 요청, 가정·제조 공장·물류창고 사례), 각주 15건, 1차 수정 지시 10건·2차 수정 지시 4건 이행 | run 2026-09-30-07
- 홈 최근 업데이트: 2026-09-30 — 44. 로봇 기반 모델·언어 모델 계획: 영역 심화로 3~11절 신규 작성(시각–언어–행동 모델·교차 형태 학습, 언어 모델 계획과 기호 계획기·불확실도 기반 사람 확인, 가정·제조 공장·물류창고 사례)
- 대분류 최근 업데이트: 2026-09-30 — 44. 로봇 기반 모델·언어 모델 계획: 영역 심화 초안 작성(로봇 기반 모델 5건·언어 모델 계획 6건 논문, 제조 공장·물류창고 사례는 벤더 주장·실증 계획으로 표시)
- 세부영역 최근 업데이트: 2026-09-30 — 44. 로봇 기반 모델·언어 모델 계획: 3~11절 신규 작성, 각주 15건, 열린 질문 4건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 로봇 기반 모델 | Robot Foundation Model | 여러 로봇·작업·환경의 대규모 데이터로 사전 학습해 새 작업·물체·로봇에 미세조정하거나 바로 쓸 수 있게 한 범용 로봇 모델로, 시각–언어–행동 모델이 대표적이다. | 44, 4, 5 | ref-1045, ref-1048, ref-1046 |
| new | 교차 형태 학습 | Cross-embodiment Learning | 형태·센서·구동 방식이 다른 여러 로봇의 데이터를 함께 학습해 한 로봇의 경험이 다른 로봇의 성능을 높이게 하는 학습 방식이다. | 44, 4 | ref-1048 |
| new | 이중 시스템 구조 | Dual-system Architecture (System 1 / System 2) | 환경을 해석하는 시각–언어 추론 모듈(System 2)과 실시간 운동 명령을 만드는 행동 생성 모듈(System 1)을 나눈 로봇 기반 모델 구조다. | 44 | ref-1054 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1045 | Brohan, A., Brown, N. 외 (Google DeepMind, arXiv) | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 논문 | medium | https://arxiv.org/abs/2307.15818 |
| ref-1046 | Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv) | OpenVLA: An Open-Source Vision-Language-Action Model | 논문 | medium | https://arxiv.org/abs/2406.09246 |
| ref-1047 | Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv) | π0.5: a Vision-Language-Action Model with Open-World Generalization | 논문 | medium | https://arxiv.org/abs/2504.16054 |
| ref-1048 | Open X-Embodiment Collaboration (arXiv) | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 논문 | medium | https://arxiv.org/abs/2310.08864 |
| ref-088 | Ahn, M., Brohan, A., Brown, N. 외 (arXiv) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 논문 | medium | https://arxiv.org/abs/2204.01691 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X. 외 (arXiv) | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 논문 | medium | https://arxiv.org/abs/2304.11477 |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv) | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 논문 | medium | https://arxiv.org/abs/2402.01817 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-1054 | NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv) | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 논문 | medium | https://arxiv.org/abs/2503.14734 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv) | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 논문 | medium | https://arxiv.org/abs/2603.02669 |
| ref-171 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — README | 오픈소스 문서 | high | https://github.com/nasa-jpl/rosa |
| ref-1057 | 지디넷코리아 | K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과 | 기사 | low | https://zdnet.co.kr/view/?no=20250501140356 |
| ref-1058 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 벤더 문서 | medium | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en |
| ref-1059 | 헬로티 | VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입 | 기사 | low | https://www.hellot.net/news/article.html?no=107567 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? | 44, 5 | 열림 | — |
| new | — | 언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? | 44, 54 | 열림 | — |
| new | — | 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? | 44, 61 | 열림 | — |
| new | — | 출처 충돌: BMW 그룹 보도자료(2026-06-25) 안에서 Figure 02의 스파턴버그 배치 기간이 10개월과 11개월로 엇갈리는데, 실제 배치 기간은 얼마인가? | 44, 62 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 가정 | 작업 대상 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 가정 | 제약 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 제조 공장 | 작업 대상 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 제조 공장 | 수행 자원 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 제조 공장 | 완료·인계 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 제조 공장 | 예외·성과 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 물류창고 | 작업 대상 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 물류창고 | 수행 자원 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |
| 물류창고 | 예외·성과 | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시 | 44. 로봇 기반 모델·언어 모델 계획 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open X-Embodiment 데이터셋·RT-X 모델 | 오픈소스 | Open X-Embodiment Collaboration | 44, 4, 5 | ref-1048 | https://arxiv.org/abs/2310.08864 |
| OpenVLA | 오픈소스 | Kim, M. J., Pertsch, K., Karamcheti, S. 외 | 44 | ref-1046 | https://arxiv.org/abs/2406.09246 |
| GR00T N1 | 오픈소스 | NVIDIA | 44 | ref-1054 | https://arxiv.org/abs/2503.14734 |

## 추가 조사 요청

- 5. 적용 사례 (현장 유형 명시): 병원·상업 시설·실외 현장에서 로봇 기반 모델·언어 모델 계획을 적용한 사례가 브리프에 없어 쓰지 못했다. 현장 유형 균형을 위해 해당 사례 조사가 필요하다.
- 5. 적용 사례 (현장 유형 명시): 세 사례의 시작 조건·제약·완료·인계(가정 사례는 수행 자원·예외·성과 포함)가 '미확인'이다. 논문 본문(π0.5 평가 절차)과 BMW·로보티즈 1차 자료로 채울 사실이 필요하다.
- 5절 제조 공장 사례: Figure 02 배치 기간(10개월 대 11개월)을 Figure AI 자체 발표(figure.ai) 등 독립 출처로 교차 확인해야 한다.
- 5절 물류창고 사례: 로보티즈·BGF로지스 1차 발표와 실증 측정 결과(자동화율·성공률 실측치)가 필요하다. 현재는 기사가 전한 목표치뿐이다.
- 8. 대표 연구와 자료: K-휴머노이드 연합 관련 산업통상자원부 보도자료(korea.kr, 2025-04-10) 원문으로 f15 를 교차 확인해야 한다.
- 7. 관련 표준·프레임워크·오픈소스: OpenVLA·GR00T N1 의 라이선스와 공개 범위(가중치·코드)를 공식 저장소에서 확인해야 한다.
- 6. 대표 접근법과 기술: 논문 수치(RT-2·OpenVLA·LLM+P 등)는 초록 기준 자체 보고이므로, 본문 실험 조건이나 독립 재현 결과가 있으면 교차 확인이 필요하다.
- 참고문헌 id 정리(퍼블리셔·다음 실행 확인 요청): ref-088(SayCan)·ref-092(LLM+P)·ref-351(KnowNo)는 기존 ref-088·ref-092·ref-351 과 같은 논문으로 보이므로 URL 기준 병합이 필요하다. 또 1·2차 검증이 지적한 대로 ref-1045·ref-1046·ref-1048·ref-088·ref-586·ref-090 는 같은 날 실행 2026-09-30-06 의 다른 출처 id 와 겹칠 수 있어 등록 전 URL 대조 확인이 필요하다.
- 분량(퍼블리셔 확인 요청): 2차 수정으로 영역 페이지 5·7절에 약어 풀어쓰기와 용어집 링크를 더해 3~11절 본문이 기준(4,000자) 가까이 늘었다. 넘치면 코드의 자동 분리 규칙을 따르되, 5절의 VLA·PoC 풀어쓰기와 용어집 링크는 영역 페이지에 남아야 한다.

## 이행한 수정 지시

- 용어(f1·f3·4절) — 4절 첫 항목에서 분류 원문 표기 '시각–언어–행동(Vision-Language-Action, VLA) 모델'을 쓰고 용어집 '비전 언어 행동 모델'(../../glossary/vision-language-action-model.md)로 링크해 같은 개념임을 밝혔다(본문에서 이 용어의 첫 등장).
- f13 — 5절 제조 공장 사례의 예외·성과 칸과 서술에서 기간을 단정하지 않고 같은 BMW 그룹 보도자료 안에 10개월(3만 대 이상 생산 지원)과 11개월 배치가 함께 있다고 둘 다 제시했으며, [추정] 벤더 주장을 병기하고 11절에 출처 충돌 열린 질문을 올렸다.
- f14 — Figure 03 순서 공급 물류 작업을 '스파턴버그에서 시작한다고 밝혔다(착수 발표)'로 서술하고, 5절 제조 공장 사례 완료·인계 칸에 '계획 내용(착수 발표) … 수행 결과가 아니다'를 표시했다.
- f16 — 5절 물류창고 사례를 'BGF로지스 물류센터 실증(PoC)을 수행할 계획'으로 고치고, 작업 대상을 '입·출고·오발주 등 고난도 작업과 분류·피킹·반품 등 수작업 공정(비정형 작업)'으로 썼으며 '비정형 상품 분류' 표현은 쓰지 않았다.
- f19 — 3절에서 '적용이 시작됐다'를 쓰지 않고 '제조 공장의 휴머노이드 배치 결과와 물류센터의 실증 계획이 발표되고 있으며, 둘 다 … 발표다'로 쓰고 [추정] 벤더 주장을 병기했다.
- f11 — 5절 제조 공장 사례와 site_matrix_updates 의 제조 공장 칸 근거에서 빼고(제조 공장 칸은 ref-1058 의 f13·f14 만 근거), 6절 '다중 로봇 계획'과 8절에 벤치마크 연구로 두었으며, 저수준 로봇 프로그램 생성 부분은 9절에서 연계 대상(로봇 자체 제어) 문맥으로만 언급했다.
- f4 — 5절 가정 사례 서술에 '연구 평가(처음 보는 가정집에서의 실험)이며 상용 배치가 아니다'를 밝히고, 시작 조건·수행 자원·완료·인계·예외·성과 칸을 '미확인'으로 두었다.
- f8 — 4절·6절·8절의 [의견] 문장을 'Kambhampati 외는 …라고 보고/본다'로 써서 의견의 주체를 밝혔다.
- f10 — 6절·8절에서 SMART-LLM 을 'IROS 2024 게재(arXiv 주석 기준)'로 적었다(reference_updates 요약에도 반영).
- f13·f14·f16·f17·f15 — 본문의 해당 문장·표 칸마다 [추정] 뒤에 '벤더 주장'을 병기하고 f17 은 '목표치(실측 아님)'를 함께 적었으며, f15 는 8절에서 '지디넷코리아 보도(2025-05-01)에 따르면'으로 기사 귀속을 유지했다.
- 분량 초과 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 본문 9,316자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,861자
- 2차: 5절 도입 문장 태그 분리 — 영역 페이지 5절 첫 문장을 둘로 나눠 '가정 사례는 처음 보는 가정집에서의 연구 평가다. [사실][^ref-1047]'와 '제조 공장 사례는 도입 기업의 발표이고, 물류창고 사례는 국내 실증 계획이다. [추정] 벤더 주장[^ref-1058][^ref-1059]'로 고쳤다.
- 2차: 8절 LLM+P 각주 — docs/topics/2026/2026-09-30-area44-s8.md 본문의 LLM+P·LLM-모듈로 항목에서 LLM+P 서술(자연어를 PDDL로 옮겨 고전 계획기로 푸는 방식)을 따로 한 문장으로 떼어 [사실][^ref-092]를 붙이고, [의견][^ref-586]은 Kambhampati 외의 주장 문장에만 남겼으며, 그 페이지의 각주 정의와 프런트매터 sources 에 ref-092 를 더했다.
- 2차: 8절 RT-2 '출발점' 삭제 — 같은 주제 페이지 첫 항목에서 '출발점' 평가와 '여러 로봇·작업에 일반화' 표현을 지우고 'RT-2는 새 물체·학습에 없던 명령에 대한 일반화를, OpenVLA는 실제 로봇 시연 97만 건 학습과 29개 작업 성능을 자체 보고했다. [사실][^ref-1045][^ref-1046]'로 f1·f3 범위에 맞춰 고쳤다.
- 2차: 약어 풀어쓰기 — 영역 페이지 3~11절에서 VLA가 처음 나오는 5절 물류창고 사례 제목에 '시각–언어–행동(Vision-Language-Action, VLA) 모델'을 풀어 쓰고 용어집 [비전 언어 행동 모델](../../glossary/vision-language-action-model.md) 링크를 달았으며, 같은 제목의 PoC 첫 등장을 '개념 검증, Proof of Concept, PoC'로, 7절 요약문의 PDDL을 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)'로 풀어 썼다.
