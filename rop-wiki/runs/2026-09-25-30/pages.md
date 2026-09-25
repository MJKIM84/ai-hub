# 스토리텔러 산출 2026-09-25-30

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md | draft | q1-04 답함(3절 소제목 신설), 상태 줄·2절·4절·5절(q3-07, q4-07)·6절·7절·8절·9절 갱신 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | v0.2 → v0.3: 상황 개념에 속성 '값 출처' 추가·확정, 6절에 추론 값 확인 근거와 모호 시간 표현 질문 추가 |
| update | docs/ideas/nl-task-chatbot.md | draft | 3절에 '상황 정보 추출과 되묻기' 소절 추가(q1-04, 실행 2026-09-25-30) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6. 살아있는 산출물 링크: 초안 v0.3, 아이디어 3절 q1-04 반영 현황 갱신 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 1 | q1-04 답함(상황 정보 추출과 빠진 정보 처리 세 방식), 업무 분해·배정 설계 초안 v0.2 → v0.3(상황 개념에 값 출처), 새 질문 q3-07·q4-07 | run 2026-09-25-30
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: q1-04(지시의 상황 정보 추출과 되묻기) 답함, 업무 분해·배정 설계 초안 v0.3
- 대분류 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: 지시에서 뽑은 위치·긴급도·기한이 13. 작업 배정 — MRTA의 입력이 되는 연구와 되묻기 방식 정리(q1-04)
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 트랙 단계 1(q1-04): 픽업·배송 위치 추출(DELIVER)과 모호한 기한을 만족도 함수로 넘기는 연구를 6. 대표 접근법과 기술 반영 제안으로 냄

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 의도 인식 | Intent Recognition (Intent Detection) | 사용자 발화가 어떤 요청(의도)인지 미리 정한 의도 유형 가운데 하나로 분류하는 자연어 이해 과제이다. | 18, 27, 13 | ref-565 |
| new | 슬롯 채우기 | Slot Filling | 발화에서 요청 처리에 필요한 인자 값(장소·대상·시간 등)을 찾아 미리 정한 항목(슬롯)에 채우는 자연어 이해 과제로, 비어 있는 필수 슬롯은 사용자에게 되묻는 데 쓰인다. | 18, 27, 13 | ref-565, ref-564 |
| new | 구조화 출력 | Structured Output | LLM 의 응답을 JSON 스키마 같은 정해진 형식의 필드와 값으로 내도록 제약하는 방식이다. | 27, 18 | ref-570 |
| new | 환각 | Hallucination | LLM이 근거 없이 그럴듯한 내용을 만들어 내는 현상이다. | 27, 18, 13 | ref-567 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-055 | Brown University H2R Lab | Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README) | 오픈소스 문서 | high | https://github.com/h2r/Lang2LTL |
| ref-558 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 오픈소스 문서 | medium | https://robot-help.github.io/ |
| ref-559 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-560 | Park, J. 외(고려대학교·연세대학교·Google Research, CLARA 프로젝트) | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents — project page (clararobot.github.io) | 오픈소스 문서 | medium | https://clararobot.github.io/ |
| ref-561 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 논문 | medium | https://arxiv.org/abs/2306.10376 |
| ref-562 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 오픈소스 문서 | high | https://github.com/cog-model/AmbiK-dataset |
| ref-563 | Ivanova, A. 외(AmbiK 저자, dblp 기록 기준) | AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment | 논문 | medium | https://aclanthology.org/2025.acl-long.1593/ |
| ref-564 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 오픈소스 문서 | high | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |
| ref-565 | Weld, H., Huang, X., Long, S., Poon, J., & Han, S. C. | A Survey of Joint Intent Detection and Slot Filling Models in Natural Language Understanding | 논문 | medium | https://dl.acm.org/doi/10.1145/3547138 |
| ref-566 | Chen, H. 외 | Enabling Robots to Understand Incomplete Natural Language Instructions Using Commonsense Reasoning | 논문 | medium | https://arxiv.org/abs/1904.12907 |
| ref-567 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 논문 | medium | https://arxiv.org/abs/2409.00557 |
| ref-568 | arXiv 2508.19114 저자(미확인) | DELIVER: A System for LLM-Guided Coordinated Multi-Robot Pickup and Delivery using Voronoi-Based Relay Planning | 논문 | medium | https://arxiv.org/abs/2508.19114 |
| ref-569 | Sucker, S., Neubauer, M., & Henrich, D. | Robot Tasks with Fuzzy Time Requirements from Natural Language Instructions | 논문 | medium | https://arxiv.org/abs/2411.09436 |
| ref-570 | OpenAI | Introducing Structured Outputs in the API | 벤더 문서 | low | https://openai.com/index/introducing-structured-outputs-in-the-api/ |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Rasa 폼(Forms, Rasa 3.x) | 오픈소스 | Rasa Technologies | 18, 27 | ref-564 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |

## 추가 조사 요청

- 단계 1 페이지 3절 q1-04·q1-05·q1-06: 화물 식별자·긴급도·기한을 필수 항목으로 둔 물류·창고 지시의 추출·되묻기 연구나 지시–작업 데이터셋(예: Ieva 외, Sensors 2025 물류 LLM 비서의 빠진 정보 처리 방식)을 원문으로 확인할 필요가 있다. 현재 답이 가정·도구 호출·내비게이션 연구에 기댄다.
- 단계 1 페이지 3절 q1-04: 손승아·강태민·하동수(KAIST) '자연어 로봇 제어 기술 동향'(정보과학회지 2024-10)의 내용 확인 — 국내 자료 우선 규칙에 따라 되묻기·모호성 판별 동향을 보강하려면 필요하다.
- 단계 1 페이지 3절 q1-04: CLARA 논문 원문에서 수행 불가능한 명령을 '거절'하는 동작의 확인, KnowNo·AmbiK·LMCR·AwN 논문 원문 열람으로 원문 미열람 표시를 해소할 필요가 있다.
- 단계 1 페이지 3절 q1-04: DELIVER(arXiv 2508.19114) 저자 목록 확인이 필요하다.
- 단계 4 확인 절차 설계: OpenAI 구조화 출력의 엄격 모드에서 선택 값을 null 허용 유형으로 표현하는 방식은 제3자 요약에만 있어 넣지 않았다. 필수 항목 검사와 빠진 값 표현을 다루려면 공식 문서 원문 확인이 필요하다.

## 이행한 수정 지시

- f3 부분 강등 — 단계 1 페이지 q1-04 '상황 정보의 추출'에서 Lang2LTL은 '지칭 표현 인식 → 랜드마크 접지 → LTL 번역' 모듈 구조만 [사실][^ref-055][^ref-056](q1-01 기존 각주 재사용)으로 쓰고, 텍스트·시각 설명 접지는 'Lang2LTL-2 … 소개한다'로 [추정][^ref-055]에 두었다. 아이디어 페이지에는 f3을 쓰지 않았다.
- f5 — '종 모양보다'를 삭제하고 '사다리꼴 함수가 사용자 만족도를 가장 잘 근사했다(저자 보고, 사용자 연구 조건)'로 썼으며, '퍼지 기술'을 '퍼지 스킬(fuzzy skill)'로 표기했다(단계 1 페이지 q1-04, 초안 6절).
- f6 — '사용자에게 묻지 않고'를 삭제하고 '빠진 정보를 주변 관찰 객체와 언어 모델의 상식 추론으로 자동으로 채운다'로 썼다. 되묻기 방식과의 대비는 f13 [추정] 문장에서만 했다(단계 1 페이지, 아이디어 페이지, 초안 2절).
- f11 — 수치를 쓴 문장마다 '저자 보고값, 독립 재현 미확인, 주방 텍스트 작업(AmbiK) 조건'을 같은 문장에 적었고, KnowNo(f8)와 같은 절에서 두 결과의 평가 조건·지표가 달라 한쪽이 다른 쪽을 반박하지 않는다고 밝혔다(단계 1 페이지 '되묻기 판단의 한계', 아이디어 페이지).
- f12 — 단계 1 페이지 3절, 아이디어 페이지 3절, 27. AI·학습·적응과 모델 운영 반영 제안 요약 모두에서 [추정]과 '벤더 주장'을 병기했고 엄격 모드 설명은 넣지 않았다.
- 용어 — '과업 지향 대화 시스템'을 '작업 지향 대화 시스템(task-oriented dialogue system)'으로, AmbiK를 '2000개 작업'으로 쓰고 '과업'을 '작업'으로 통일했다. 의도 인식(intent detection)·슬롯 채우기(slot filling)·구조화 출력·등각 예측(conformal prediction)은 첫 등장 때 영문을 병기했고, LLM 에이전트는 용어집 링크(llm-agent.md)를 썼다.
- glossary_updates — 의도 인식·슬롯 채우기·구조화 출력·환각 4건을 new로 냈고, 환각 정의는 'LLM이 근거 없이 그럴듯한 내용을 만들어 내는 현상'까지만 두고 Wang 외 설명은 description으로 옮겼다.
- reference_updates — ref-565 기관을 'Weld, H., Huang, X., Long, S., Poon, J., & Han, S. C.'·발행일 2022-12로, ref-563 기관을 'Ivanova, A. 외(AmbiK 저자, dblp 기록 기준)'로 고쳤고, ref-561 요약에 'ICRA 2024 발표', ref-568 요약에 'SII 2026 게재(IEEE Xplore)'를 더했다. 페이지 각주 정의에도 같은 값을 썼다.
- 원문 미열람 표시 — ref-559·561·563·565·566·567·568·569·570 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates에 source_unopened: true를 넣었다. ref-055·558·560·562·564에는 붙이지 않았다.
- f2 — Rasa 폼 서술에 'Rasa 3.x 문서, main 브랜치, 확인일 2026-09-25 기준'을 적었다(단계 1 페이지, 아이디어 페이지).
- f16 — 흐름 단계 '출하'를 쓰지 않았고 flow_matrix_updates는 빈 배열로 냈다.
- 온톨로지 변경 1 승인 반영 — 초안 2절 상황 행 주요 속성에 '값 출처'(지시 원문에서 추출 / 환경·상식으로 추론 / 사용자 되묻기 응답)를 더하고 근거 칸에 f1·f2, f6, f2·f7·f8과 ref-565·564·566·560·558 각주를 적었으며 상태를 초안 → 확정으로 바꿨다. 버전 '0.3'을 H1·프런트매터 ontology_version·track_updates.ontology_draft_version에 맞췄다(auto 상태 줄은 프런트매터에서 퍼블리셔가 채움). f15는 6절 '상황의 항목' 질문에 [추정] 근거로 덧붙였다.
- 온톨로지 변경 2 미반영 — 초안 6절에 '모호한 시간 표현(예: 몇 분 뒤)을 상황의 시간 조건과 일정 개념 가운데 어디에 만족도 함수(허용 창)로 둘 것인가 — 관련: q3-01, q2-01' 질문을 두고 f5 근거를 [사실][^ref-569]로 달았다.
- 새 질문 2건 — backlog_updates에 q4-07(단계 4, origin f11)과 q3-07(단계 3, origin f6)을 등록했고, 단계 1 페이지 5절에 q3-07이 q3-03·q2-01과 이어지되 추론 허용 항목과 되묻기 필수 항목의 기준을 묻는 점이 다르다고 적었다.
- 단계 1 페이지 — 2절 q1-04를 답함(2026-09-25-30, #q1-04)으로 바꾸고 3절에 '### q1-04 … {#q1-04}' 소제목을 두었으며, 상태 줄을 '열린 질문: 2건 · 답한 질문: 4건'으로 했다. 6절은 첫째 '충족(1차 예비, 2차에서 확정)', 둘째 '미충족 · 미승인', 아래 줄 '다음 단계로 전환: 아니오(지시 분해 접근 유형 목록이 업무 분해·배정 설계 초안에 미반영, 열린 질문 q1-05·q1-06)'로 썼고 q1-05·q1-06 중복 정리 문장은 유지했다. 상태 줄이 H2 밖에 있어 이 페이지는 patches 대신 전체 content로 냈다.
- 아이디어 2 페이지 3절 — '상황 정보 추출과 되묻기' 소절에 f13([추정], 이 위키의 정리), f2·f6·f7·f8·f9 근거, f11(저자 보고값 조건), f14(부재의 확인 아님), f12([추정] 벤더 주장)만 썼다.
- 세부영역 페이지 — 13. 작업 배정 — MRTA, 18. 사람–로봇 협업·운영 인터페이스, 27. AI·학습·적응과 모델 운영 페이지는 고치지 않고 area_reflection_proposals로만 냈으며, 13·18 제안 요약과 27 제안 요약에 서로 연결을 표시했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: q1-04(상황 정보 추출과 빠진 정보 처리 세 방식 — 필수 슬롯 되묻기, 추론으로 채움, 불확실성 기반 되묻기; 근거 f1·f2·f4·f5·f6·f7·f8·f9·f10·f11·f13·f14·f15·f16, f3 부분 강등, f12 벤더 주장) / 새 질문: q3-07(f6, 추론 허용 항목과 되묻기 필수 항목의 기준), q4-07(f11, 물류 지시에서의 모호성 탐지 성능과 되묻기·오배정) / 온톨로지 변경: v0.2 → v0.3: 개념 '상황 (Situation)'에 속성 '값 출처'(지시 원문에서 추출 f1·f2 / 환경·상식으로 추론 f6 / 사용자 되묻기 응답 f2·f7·f8) 추가, 초안 → 확정. 거부 1건(상황의 시간 조건에 모호 시간 표현·만족도 함수, f5·f16 → 6절 질문) / 완료 조건 평가: 미충족(부족: 지시 분해 접근의 유형 목록이 업무 분해·배정 설계 초안에 미반영, 열린 질문 q1-05·q1-06 중복 정리 필요) / 세부영역 반영 제안: 13. 작업 배정 — MRTA 1건, 18. 사람–로봇 협업·운영 인터페이스 2건, 27. AI·학습·적응과 모델 운영 2건 / 다음 실행 제안: q1-05·q1-06 중복 정리 후 물류 지시 LLM 분해 연구 조사, 지시 분해 접근 유형 목록의 초안 반영 제안
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 2, 답함 4, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-04 | 답함 | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-04 | — | — | — |
| q4-07 | 열림 | — | 필수 슬롯 누락은 규칙(스키마)으로 검사하고 지시의 모호성은 KnowNo·CLARA 같은 불확실성 추정으로 판단하는 식으로 두 방식을 나눠 쓸 때, 가정용 벤치마크(AmbiK)에서 보고된 모호성 탐지의 낮은 구분 성능이 물류 지시(화물·장소·기한)에서도 나타나는가, 되묻기 횟수와 오배정은 어떻게 달라지는가? (q1-04 에서 파생) | 4 | f11 |
| q3-07 | 열림 | — | LMCR 처럼 환경 관찰·상식으로 빠진 정보를 스스로 채워도 되는 상황 항목(예: 가장 가까운 출하 도크)과 반드시 사용자에게 되물어야 하는 항목(예: 기한·대상 화물)을 어떤 기준으로 나누는가? (q1-04 에서 파생) | 3 | f6 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 6. 대표 접근법과 기술 | 자연어 지시에서 뽑은 픽업·배송 위치(DELIVER, LLaMA3 추출 + 보로노이 분할·중계 지점)와 긴급도·기한이 배정의 입력이 되는 구조, 모호한 시간 요구를 만족도 함수(허용 창)로 넘기는 연구(Sucker 외, IEEE IRC 2024)와 SCM 관점 질문(가까움 대 기한 준수)의 연결([추정]). 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| 18 | 6. 대표 접근법과 기술 | 지시를 받는 운영 인터페이스의 되묻기 방식: 필수 슬롯 폼(Rasa 3.x), 불확실성 기반 도움 요청(KnowNo, 등각 예측), 명령의 명확·모호·수행 불가 판별과 질문 생성(CLARA, 국내 연구), 세 방식의 정리는 이 위키의 [추정]. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| 18 | 8. 대표 연구와 자료 | Rasa 폼 문서(ref-564), CLARA(고려대 등, IEEE RA-L 2024, ref-560·ref-561), KnowNo(CoRL 2023, ref-558·ref-559), 작업 지향 대화의 의도 인식·슬롯 채우기 서베이(Weld 외 2022, ref-565) |
| 27 | 6. 대표 접근법과 기술 | LLM 불확실성 정량화(등각 예측, KnowNo)로 필요할 때만 사람에게 묻는 방법, LLM 에이전트의 빠진 인자 지어내기와 Ask-when-Needed, 모호성 탐지의 낮은 구분 성능(AmbiK, 저자 보고값·주방 텍스트 작업 조건), 구조화 출력([추정] 벤더 주장). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결 |
| 27 | 8. 대표 연구와 자료 | KnowNo(ref-558·ref-559), AmbiK 데이터셋·논문(ref-562·ref-563), Wang 외 Learning to Ask(EMNLP 2025, ref-567), LMCR(ICRA 2020, ref-566), OpenAI 구조화 출력 발표문(ref-570, [추정] 벤더 주장) |
