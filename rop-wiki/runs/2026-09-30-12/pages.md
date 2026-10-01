# 스토리텔러 산출 2026-09-30-12

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | draft | 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건. 2차 수정: 4절 요약 태그 [추정]으로 정정, 5절 병원·제조 공장 사례 서술의 사실·추정 분리 |
| create | docs/topics/2026/2026-09-30-area33-s7.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,795자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area33-s10.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,571자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area33-s6.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(1,360자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area33-s4.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "4. 핵심 개념과 용어" 절(1,249자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장 태그를 [사실]에서 [추정]으로 정정 |
| create | docs/topics/2026/2026-09-30-area33-s8.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "8. 대표 연구와 자료" 절(951자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area33-s11.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "11. 열린 질문" 절(919자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area33-s3.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "3. 왜 중요한가" 절(886자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 33. 시나리오 모델·편집 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건), 1차 조건부 승인 수정 13건 반영(MAPF 벤치마크 수치 주장 강등 등), 2차 수정 3건 반영(4절 요약·5절 해석 문장 태그를 추정으로 정정) | run 2026-09-30-12
- 홈 최근 업데이트: 2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성(시나리오 형식·예제 라이브러리·편집기, 상업 시설·병원·실외·가정·제조 공장 시뮬레이션 사례)
- 대분류 최근 업데이트: 2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성(OpenSCENARIO·Open-RMF rmf_demos·ARIAC·BEHAVIOR-1K 등 15개 출처, 신뢰도 low)
- 세부영역 최근 업데이트: 2026-09-30 — 33. 시나리오 모델·편집: 영역 심화로 3~11절 신규 작성, 열린 질문 4건 추가(실행 2026-09-30-12)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 오픈시나리오 | ASAM OpenSCENARIO | ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다. | 33, 34, 54 | ref-1141 |
| new | 행동 영역 정의 언어 | Behavior Domain Definition Language (BDDL) | BEHAVIOR 벤치마크가 일상 가정 활동을 형식 명세하는 데 쓰는 도메인 특화 언어다. | 33, 65 | ref-971 |
| new | 시뮬레이션 기술 형식 | Simulation Description Format (SDFormat) | Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다. | 33, 34 | ref-1148 |
| new | 반증 기반 시험 | Falsification | 시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다. | 33, 54 | ref-1135 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1135 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 논문 | medium | https://arxiv.org/abs/2307.03325 |
| ref-104 | Open-RMF (open-rmf/rmf_demos) | rmf_demos — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-079 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Traffic Editor | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 논문 | medium | https://arxiv.org/abs/2403.09227 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Challenges | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html |
| ref-1140 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html |
| ref-1141 | ASAM e.V. | ASAM OpenSCENARIO® XML | 표준 | high | https://www.asam.net/standards/detail/openscenario-xml/ |
| ref-726 | Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv) | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2206.05728 |
| ref-1143 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 논문 | medium | https://arxiv.org/abs/2409.12471 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 논문 | medium | https://arxiv.org/abs/2312.09067 |
| ref-1145 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 벤더 문서 | medium | https://www.behaviortree.dev/groot/ |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 논문 | medium | https://arxiv.org/abs/2603.15427 |
| ref-1147 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 오픈소스 문서 | medium | https://movingai.com/benchmarks/mapf/index.html |
| ref-1148 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 오픈소스 문서 | high | http://sdformat.org/ |
| ref-046 | VDMA (Intralogistics-2X-LIF) | Layout Interchange Format (LIF) — README | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 33, 34 | 열림 | — |
| new | — | 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 33, 57 | 열림 | — |
| new | — | ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 33, 32 | 열림 | — |
| new | — | 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 33, 65 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 상업 시설 | 시작 조건 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 상업 시설 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 상업 시설 | 수행 자원 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 상업 시설 | 제약 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 병원 | 시작 조건 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 병원 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 병원 | 수행 자원 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 병원 | 제약 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 실외 | 시작 조건 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 실외 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 실외 | 수행 자원 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 가정 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 제조 공장 | 시작 조건 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 제조 공장 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 제조 공장 | 수행 자원 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 제조 공장 | 완료·인계 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 제조 공장 | 예외·성과 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ASAM OpenSCENARIO XML (1.4.0) | 표준 | ASAM e.V. | 33, 34, 54 | ref-1141 | https://www.asam.net/standards/detail/openscenario-xml/ |
| SDFormat (Simulation Description Format) | 오픈소스 | Open Source Robotics Foundation | 33, 34 | ref-1148 | http://sdformat.org/ |
| BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) | 평가 프로그램 | Stanford 등 (Li, C. 외) | 33, 54, 65 | ref-971 | https://arxiv.org/abs/2403.09227 |
| Moving AI MAPF 벤치마크 | 평가 프로그램 | Moving AI Lab (Sturtevant 외) | 27, 33, 54 | ref-1147 | https://movingai.com/benchmarks/mapf/index.html |
| Arena-Bench | 평가 프로그램 | Kästner, L. 외 (RA-L 2022) | 33, 54 | ref-726 | https://arxiv.org/abs/2206.05728 |

## 추가 조사 요청

- 5절 물류창고 사례: 물류창고 현장(입고~반품 흐름 가운데 어느 단계든)의 시나리오 예제·템플릿을 공개한 자료와 국내 자료가 필요하다. 이번 브리프에는 현장 사례가 없어 물류창고 사례를 세우지 못했다.
- 7절 Moving AI MAPF 벤치마크: 지도 수와 총 시나리오 파일 수를 출처 페이지에서 직접 확인해야 한다. 브리프(36개·1,800개)와 검증자가 연 목록(33개)이 맞지 않아 '미확인'으로 두었다.
- 5절 상업 시설·병원·실외 사례의 완료·인계·예외·성과 칸: Open-RMF 작업이 완료로 인정되는 조건과 실패 처리를 rmf_demos 시나리오 단위로 기술한 자료가 있으면 칸을 채울 수 있다.
- 5절 제조 공장 사례 제약 칸: ARIAC 셀 전압 허용치(±0.2 V) 같은 품질 제약은 발견 사항 본문에 없어 쓰지 않았다. 다음 조사에서 claim 으로 확인하면 제약 칸에 넣을 수 있다.
- 4절 BDDL: 활동을 초기 조건·목표 조건 쌍으로 정의한다는 구조와 Scenic 의 표본 추출 방식은 검색 요약에만 있어 쓰지 않았다. 원문 확인이 필요하다. 확인되면 4절 요약 문장의 '확률 분포' 재사용 부분을 사실로 뒷받침할 수 있다.
- 11절 oq-135: 시나리오 구성 시 되물을 항목의 표준 질문 목록은 이번 조사에서 검색하지 못했다. oq-131 도 공개 변환 형식을 찾지 못했다.
- 다음 실행 반영 후보(브리프 제안): 9. 채팅으로 시나리오 구성 페이지에 Arena 4.0·Holodeck(ref-1143·ref-815), 36. 가상 시운전·실제 상황 재현 페이지에 ARIAC 장애 주입·Groot2 로그 재생(ref-528·ref-1145, 벤더 주장)을 반영한다.
- 파이프라인 확인(2차 검증 참고): 자동 분리 주제 페이지의 9. 검증 노트가 '1차·2차 검증을 거쳤다'로 고정돼 1차 판정·건수 형식과 다르고, 본문의 '2절 원문 주석'·'(5절)' 표기가 원 페이지 절을 가리킨다는 점이 드러나지 않는다. pipeline 담당의 확인이 필요하다.

## 이행한 수정 지시

- f18 강등 — 7절 MAPF 벤치마크 행을 [추정]으로 쓰고 지도 수·총 파일 수를 '미확인'으로 두었으며 '36개·1,800개'와 창고 지도 추상화 서술을 넣지 않았다(reference_updates 의 ref-1147 요약에서도 '36개' 표현을 뺐다).
- f11 문구 수정 — 5절 제조 공장 사례의 완료·인계 칸을 '아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 주문 완료로 바뀌지 않는다'로 고쳐 썼다.
- 5절 시뮬레이션 명시 — 도입 문장과 각 사례 제목·서술에 시뮬레이션 예제 월드(rmf_demos)·벤치마크(BEHAVIOR-1K)·경진대회 시나리오(ARIAC)이며 실제 현장 배치가 아님을 밝혔다.
- f7 분리 — 캠퍼스 월드만 '실외' 사례로 세우고, 제조·물류 월드는 사례로 쓰지 않고 7절 rmf_demos 행에서 영상 데모로만 언급했다.
- f10 가정 분류 — 가정 사례 서술에 활동이 일상 가정 활동이라 '가정'으로 분류했고 장면에 정원·식당·사무실도 들어 있음을 밝혔다.
- 물류창고 — 5절 끝에 물류창고 현장 사례를 찾지 못했다고 밝히고, MAPF 시나리오 파일(f18)과 LIF(f20)는 적용 사례로 쓰지 않고 7절에서만 다뤘다.
- f16 — 6절·7절·10절에서 Groot2 기능을 '[추정] 벤더 주장' 으로 병기하고 6절에 출처가 제품 페이지(ref-1145)뿐임을 적었다.
- 9절 f24 — '버전 있는 시나리오 모델'을 1절 리스트업이 정한 목표로 서술하고, 개별 시나리오 인스턴스 버전 관리 방식을 공개 자료에서 찾지 못했다는 f21 을 함께 밝혔다.
- 10절 f26 — 35. 처리능력·규모·배치 설계 연결은 넣지 않았고(related_areas 에서도 제외), 9. 채팅으로 시나리오 구성·11. 채팅으로 실제 상황 시뮬레이션 재현 연결은 2절 원문 주석을 근거로 들었다.
- 10절 교차 규칙 — 언어 모델 기반 생성(f14·f15)을 44. 로봇 기반 모델·언어 모델 계획과 9. 채팅으로 시나리오 구성 양쪽에 연결했고, 시나리오가 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력임을 18. 실시간 세계 상태·데이터 일관성과 구분하는 항목을 두었다.
- 4절 용어 — 장애 주입·선형 시간 논리·행동 트리·BPMN·계층적 작업 네트워크·ARIAC 는 4절에서, 레이아웃 교환 형식·Open-RMF 는 7절에서 기존 용어집 항목에 링크했고, glossary_updates 는 오픈시나리오·행동 영역 정의 언어·시뮬레이션 기술 형식·반증 기반 시험 4건으로 한정했다.
- 참고 자료 ref-528·ref-1140 — 새 id 를 그대로 쓰고, 7절 ARIAC 행과 reference_updates 요약에 NIST ARIAC 참고문헌 ref-008 과 같은 경진대회의 개별 문서 페이지임을 밝혔다(ref-008 링크 포함).
- 11절 — oq-131·oq-135 는 '열림' 그대로 두고, open_questions_new 4건을 11절에 싣고 open_question_updates 에 new 4건으로 냈다.
- 분량 초과 자동 분리: 33. 시나리오 모델·편집 본문 12,268자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,610자
- 2차: 4절 요약 태그 — 원 페이지 4절 요약 문장과 주제 페이지 2026-09-30-area33-s4 의 1. 세 줄 요약 첫 줄·3. 본문 첫 문장의 태그를 [사실]에서 [추정]으로 고쳤고, outline 의 4절 summary 태그도 [추정]으로 맞췄다.
- 2차: 5절 병원 사례 — 서술 문장을 나눠 사실 부분은 f6 의 시설 구성('이 월드는 승강기 2대가 있는 2개 층 시설이고, 로봇이 층을 오가며 순찰한다. [사실]')으로만 남기고, 해석 부분('설비를 시나리오 요소로 담는 예로 볼 수 있다')은 [추정]으로 분리했다.
- 2차: 5절 제조 공장 사례 — 서술 문장을 f12 표현대로 'ARIAC는 장애와 긴급 요청을 매개변수로 선언해 시나리오에 주입한다. [사실]'로 고치고('시나리오 파일' 표현 삭제), '이 영역이 참고할 점으로 보인다'는 평가를 [추정]으로 분리했다.
