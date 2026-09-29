# 스토리텔러 산출 2026-09-29-04

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md | draft | 3~11절 신규 작성(seed → draft), 출처 15건(ref-351~ref-853), 병원 사례 1건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행 |
| create | docs/topics/2026/2026-09-29-area09-s6.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "6. 대표 접근법과 기술" 절(2,863자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s8.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "8. 대표 연구와 자료" 절(1,570자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s4.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "4. 핵심 개념과 용어" 절(1,364자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s3.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "3. 왜 중요한가" 절(1,211자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s7.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,204자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s10.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,022자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area09-s11.md | draft | 자동 분리: 9. 채팅으로 시나리오 구성 의 "11. 열린 질문" 절(677자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 9. 채팅으로 시나리오 구성 | 3~11절 신규 작성(seed → draft), 출처 15건, 병원 사례 1건, 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 7건 이행 | run 2026-09-29-04
- 홈 최근 업데이트: 2026-09-29 — 9. 채팅으로 시나리오 구성: 3~11절 신규 작성(seed → draft), 출처 15건, 병원 사례 1건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행
- 대분류 최근 업데이트: 2026-09-29 — 9. 채팅으로 시나리오 구성: 3~11절 신규 작성(seed → draft), 출처 15건(논문 13·오픈소스 문서 2), 병원 사례 1건(원문 미열람 명시), 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행
- 세부영역 최근 업데이트: 2026-09-29 — 9. 채팅으로 시나리오 구성: 3~11절 신규 작성. 되묻기 기준(불확실도·정보 이득), 구조화 시나리오 상태, 텍스트→워크플로 생성·실행 지향 검사, Open-RMF 작업 요청 스키마의 빈 자리(기한·반복·실패 처리)를 정리 (실행 2026-09-29-04)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 불확실도 정렬 | Uncertainty Alignment | 언어 모델 계획기가 자신의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻도록 맞추는 것이다. | 9, 13, 44 | ref-351 |
| new | 과소명세 | Underspecification | 사용자 지시에 실행에 필요한 조건(대상·장소·수량·기한 등)이 빠져 여러 해석이 가능한 상태로, 명확화 질문이나 기본값 규칙으로 채워야 한다. | 9, 12, 13 | ref-840 |
| new | 미션 명세 패턴 | Mission Specification Pattern | 이동 로봇 임무 요구에서 반복되는 명세 문제와 그 시간 논리 템플릿을 목록으로 정리한 것으로, 패턴을 채우고 조합해 형식 명세를 만든다. | 9, 24, 33 | ref-848 |
| new | 상황 상태 추적 | Situation State Tracking | 다중 턴 대화에서 대화 이력과 별도로 사용자 의도·필요 변수·제약·실행 상태를 명시적 상태로 유지해 확인된 사실과 판단을 구분하는 기법이다. | 9, 13 | ref-843 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-840 | Deng, M., Li, Z., Li, X., Zhu, T., Zhao, Y., Guo, Z., & Wang, W. | Uncertainty-Aware Clarification in LLM Agents with Information Gain | 논문 | medium | https://arxiv.org/abs/2606.03135 |
| ref-841 | Laban, P., Hayashi, H., Zhou, Y., & Neville, J. | LLMs Get Lost In Multi-Turn Conversation | 논문 | medium | https://arxiv.org/abs/2505.06120 |
| ref-842 | Tack, J., Laban, P., & Neville, J. | LLMs Get Lost in Evolving User Intent | 논문 | medium | https://arxiv.org/abs/2607.20734 |
| ref-843 | Tao, M., Tao, Y., & Wang, P. | Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents | 논문 | medium | https://arxiv.org/abs/2608.15755 |
| ref-844 | Kourani, H., Berti, A., Schuster, D., & van der Aalst, W. M. P. | Process Modeling With Large Language Models | 논문 | medium | https://arxiv.org/abs/2403.07541 |
| ref-845 | Matei, I., Zhenirovskyy, M., Menaka Sekar, P. K., & Wong, H. Y. | Automated BPMN Model Generation from Textual Process Descriptions: A Multi-Stage LLM-Driven Approach | 논문 | medium | https://arxiv.org/abs/2604.12105 |
| ref-061 | Izzo, R. A., Bardaro, G., & Matteucci, M. | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 논문 | medium | https://arxiv.org/abs/2403.12761 |
| ref-847 | Sundarsingh, D. S., Wang, J., Deshmukh, J. V., & Kantaros, Y. | ConformalNL2LTL: Translating Natural Language Instructions into Temporal Logic Formulas with Conformal Correctness Guarantees | 논문 | medium | https://arxiv.org/abs/2504.21022 |
| ref-848 | Menghi, C., Tsigkanos, C., Pelliccione, P., Ghezzi, C., & Berger, T. | Specification Patterns for Robotic Missions | 논문 | medium | https://arxiv.org/abs/1901.02077 |
| ref-110 | Open Robotics | Supporting a new Task in RMF (task_new) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_new.html |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-548 | University West (Högskolan Väst, DiVA) 학위논문 저자(미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 논문 | medium | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf |
| ref-852 | Chiang, Y.-C., Lee, I.-P., Fu, L.-C. 외 (Autonomous Robots 50, Article 28, 2026) | Agile assistive hospital robot for suboptimal Task execution in dynamic environments | 논문 | medium | https://link.springer.com/article/10.1007/s10514-026-10255-6 |
| ref-853 | 손승아, 강태민, 하동수 (한국과학기술원), 정보과학회지 42(10) | 자연어 로봇 제어 기술 동향: 분류, 기술, 응용 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11940459 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? | 9, 33 | 열림 | — |
| new | — | 대화로 정한 시나리오에서 사용자가 확정한 값과 모델이 추정한 값을 구분해 저장·표시하고 턴마다 바뀐 부분만 보여 주는 공개 데이터 형식이나 편집기 구현이 있는가? | 9, 13 | 열림 | — |
| new | — | 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? | 9, 24, 26, 20 | 열림 | — |
| new | — | 국내 물류창고·병원·제조 공장에서 대화로 로봇 작업 시나리오를 구성한 사례가 있는가(이번 조사에서 확인된 국내 자료는 자연어 로봇 제어 동향 논문뿐이다)? | 9, 61, 63 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시 | 9. 채팅으로 시나리오 구성 |
| 병원 | 작업 대상 | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시 | 9. 채팅으로 시나리오 구성 |
| 병원 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시 | 9. 채팅으로 시나리오 구성 |
| 병원 | 제약 | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시 | 9. 채팅으로 시나리오 구성 |
| 병원 | 예외·성과 | docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md#5-적용-사례-현장-유형-명시 | 9. 채팅으로 시나리오 구성 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) | 오픈소스 | Open Robotics (open-rmf) | 9, 20, 24, 26 | ref-125 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) | 오픈소스 | Open Robotics | 9, 20, 24 | ref-110 | https://osrf.github.io/ros2multirobotbook/task_new.html |

## 추가 조사 요청

- 5. 적용 사례 (현장 유형 명시): 병원 사례(ref-852)의 저자가 밝힌 정량 결과(작업 완료율·시간)와 완료 확인 절차 — 원문 미열람으로 '완료·인계' 칸이 미확인이며 성과 수치를 쓰지 못했다.
- 5. 적용 사례 (현장 유형 명시): 제조 공장·물류창고·상업 시설 등 병원 이외 현장 유형에서 대화로 로봇 작업 시나리오를 구성한 실제 운영 사례 — 이번 브리프에는 병원 한 건(원문 미열람)뿐이고 물류 학위논문(ref-548)은 현장 유형을 특정하지 않아 사례로 쓰지 못했다.
- 3·6절: University West 학위논문(ref-548)의 저자·연도·실험 결과(구조화 프롬프트의 번역 정확도 수치) — 원문 미열람으로 문제 제기만 옮겼다.
- 4·6절: Menghi 외(ref-848) 미션 명세 패턴 22개의 개별 이름·분류(이동·트리거·회피 등) — 초록에서 확인하지 못해 되묻기 질문 목록의 뼈대로 구체화하지 못했다.
- 6절: BTGenBot(ref-061)의 실패 처리(fallback) 노드 생성 방식 — 초록에 없어 실패 처리 조건을 로봇 수준 표현으로 넘기는 방법을 쓰지 못했다.
- 6절: 시나리오 값마다 출처(사용자 확정·모델 추정·미정)를 구분해 저장·표시하는 구현이나 실험 연구 — f7 은 일반 언어 모델 대화 연구에서 도출한 추정이며 직접 근거가 없다.
- 7절: Open-RMF 플릿별 description 스키마나 상위 스케줄러가 완료 기한·반복 주기를 다루는지 여부 — f19 의 한계로 남아 있다.
- 8절: 손승아·강태민·하동수(ref-853) 동향 논문의 본문 내용(인지 수준별 분류 기준) — DBpia 서지만 확인해 국내 자료의 요지를 쓰지 못했다.

## 이행한 수정 지시

- f20 강등·원문 미열람·문제 제기 서술 — 3절과 6절 '로봇 수준 표현·형식 명세로의 번역' 소제목에서 [추정][^ref-548]로 쓰고 '(원문 미열람, 저자·연도·실험 결과 미확인)'을 병기했으며, 'STL 공식을 일관되게 내지 못한다'는 문장을 '연구가 풀려는 문제로 제기했다'로 서술하고 정확도 수치는 넣지 않았다.
- f21 강등·원문 미열람·병원 이름 삭제 — 5절 여섯 항목 표와 서술, 8절 목록, 10절 연결 항목에서 모두 [추정][^ref-852]로 쓰고 '원문 미열람'을 병기했으며 '국립대만대학병원' 문구를 빼고 '간호 인력'으로만 썼다.
- ref-852 기관·저자 항목 — 13절 각주 정의와 reference_updates 의 org 를 'Chiang, Y.-C., Lee, I.-P., Fu, L.-C. 외 (Autonomous Robots 50, Article 28, 2026)' 로 적었다.
- 5절 현장 유형 병원 하나만 — 5절에 병원 사례 하나만 두고 f20 은 사례로 쓰지 않았으며(3절·6절에서만 다룸), 다른 현장 유형 사례가 없음을 괄호 안내로 밝히고 site_matrix_updates 는 병원 칸 5건(시작 조건·작업 대상·수행 자원·제약·예외·성과)만 냈다('완료·인계'는 미확인이라 내지 않음).
- ref-548·ref-852·ref-853 원문 미열람 표시 — 13절 세 각주 정의의 접근일 뒤에 ' (원문 미열람)' 을 붙이고 reference_updates 의 세 항목에 source_unopened: true 를 넣었다.
- f1 모호성 유형 — 6절 KnowNo 문장의 모호성 유형을 '공간·수량·사람 선호·대명사 지시'로만 쓰고 '속성·안전'은 넣지 않았다.
- 용어 후보 '불확실도 정렬' — glossary_updates 의 definition 에서 등각 예측을 다시 정의하지 않고 description 에서 기존 용어집 항목 [등각 예측](conformal-prediction.md)을 링크로 참조하게 했으며, 4절 용어 설명도 ../../glossary/conformal-prediction.md 링크로 두었다.
- 분량 초과 자동 분리: 9. 채팅으로 시나리오 구성 본문 12,079자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,653자
