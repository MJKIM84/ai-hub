# 스토리텔러 산출 2026-09-25-46

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md | draft | 영역 심화: 3~11절 신규 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 자연어 업무 지시 챗봇 반영 제안 6건 검토 반영), 페이지 상태 자동 영역 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 18. 사람–로봇 협업·운영 인터페이스 | 3~11절 신규 작성: 협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 반영 제안 6건 검토 | run 2026-09-25-46
- 홈 최근 업데이트: 2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 영역 심화 초안 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 안전 표준·국내 가이드, 자연어 지시 확인 방식)
- 대분류 최근 업데이트: 2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 3~11절 신규 작성, 피킹 단계 시나리오와 ROP 직접·연계 범위 정리
- 세부영역 최근 업데이트: 2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 3~11절 신규 작성(트랙 자연어 업무 지시 챗봇 반영 제안 6건을 6·8절에 검토 반영)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 팬아웃 | Fan-out (human-robot team) | 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇의 방치 허용도와 로봇 하나를 다루는 상호작용 시간으로 추정한다. | 18, 19 | ref-478 |
| new | 운용 모드 | Operating Mode (VDA 5050 operatingMode) | VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, HMI가 주행 속도를 제어하는지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다. | 9, 18 | ref-051, ref-031 |
| new | 상황 인식 기반 에이전트 투명성 | Situation Awareness-based Agent Transparency (SAT) | 자율 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주어 상황 인식과 신뢰를 돕는 인터페이스 설계 모델이다. | 18, 19 | ref-477 |
| new | 협동 적용 | Collaborative Application | ISO 10218:2025 에서 로봇 자체가 아니라 사람과 로봇이 함께 일하도록 설계된 적용 방식을 기준으로 안전을 판단하기 위해 '협동로봇' 대신 쓰는 용어이다. | 18, 25 | ref-471 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 논문 | medium | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 업계 보고서 | medium | https://www.automate.org/robotics/blogs/updated-iso-10218-faq |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 표준 | medium | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 정부·연구기관 | medium | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 |
| ref-474 | 로봇신문 | '이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나? | 기사 | low | https://www.irobotnews.com/news/articleView.html?idxno=32130 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 정부·연구기관 | medium | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 논문 | medium | https://arxiv.org/abs/2101.01625 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 |
| ref-478 | Olsen, D. R. 외(CHI 2004) | Fan-out: measuring human control of multiple robots | 논문 | medium | https://dl.acm.org/doi/10.1145/985692.985722 |
| ref-479 | Rey-Becerra, E., & Wischniewski, S. | Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316 |
| ref-480 | ZDNet Korea | "대형 물류센터 집품 작업, 로봇 6대로 효율화" | 기사 | low | https://zdnet.co.kr/view/?no=20231222165139 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-272 | Lucas Systems | Voice-Directed Warehousing - Solutions \| Lucas Systems | 벤더 문서 | low | https://www.lucasware.com/voice-directed-warehousing/ |
| ref-275 | USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.) | System and method for generating and updating location check digits (US 8868519) | 정부·연구기관 | medium | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519 |
| ref-279 | Locus Robotics | Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface) | 벤더 문서 | low | https://locusrobotics.com/locusone/automated-warehouse-software/user-interface |
| ref-176 | InOrbit.AI | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 벤더 문서 | low | https://www.inorbit.ai/press/inorbit-robops-copilot |
| ref-278 | InOrbit.AI | InOrbit RobOps Copilot - Bring AI power to robot operations | 벤더 문서 | low | https://www.inorbit.ai/robopscopilot |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 논문 | medium | https://arxiv.org/abs/2306.10376 |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 오픈소스 문서 | medium | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 벤더 문서 | low | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? | 18, 25 | 열림 | — |
| new | — | 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? | 18, 4 | 열림 | — |
| new | — | 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? | 18, 19 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |
| 피킹 | 작업 대상 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |
| 피킹 | 수행 자원 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |
| 피킹 | 제약 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |
| 피킹 | 완료·인계 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |
| 피킹 | 예외·성과 | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 18. 사람–로봇 협업·운영 인터페이스 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 | 표준 | ISO | 18, 25 | ref-470 | https://www.iso.org/standard/83545.html |
| ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) | 표준 | ISO (A3 해설 경유) | 18, 25 | ref-471 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq |
| ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 | 표준 | A3(Association for Advancing Automation) | 18, 25 | ref-472 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available |
| 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 | 프레임워크 | 고용노동부·한국산업안전보건공단 | 18, 25 | ref-473 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 |
| 이동식 협동로봇 안전기준 KS(표준 번호 미확인) | 표준 | 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) | 18, 25 | ref-475 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 |
| Open-RMF rmf_demos | 오픈소스 | Open Robotics (open-rmf) | 18, 20 | ref-104 | https://github.com/open-rmf/rmf_demos |

## 추가 조사 요청

- 6절 원격 조작(teleoperation): 분류 원문 정의에 있으나 공개 근거가 없어 쓰지 못했다. 물류 이동로봇의 원격 조작 방식·표준·연구 자료가 필요하다.
- 7·11절: 이동식 협동로봇 안전기준 KS 의 표준 번호와 본문(KSSN 등) 확인이 필요하다.
- 7절: ISO 10218-1·10218-2:2025 개정 내용을 ISO 공식 자료로 확인해야 한다(현재 A3 해설 기준).
- 7절: ANSI/A3 R15.08-3(사용자 책임) 발행 여부 확인이 필요하다.
- 8절: Rey-Becerra·Wischniewski(2025)의 분석 건수(44건/35건)와 설계·평가 점검표 제시 여부를 원문으로 확인해야 한다.
- 8·11절: Yang 외(2026) 모델이 교대조 단위 인원·로봇 수 결정을 다루는지(oq-009 해결 여부) 원문 확인이 필요하다.
- 6·8절: 트랙 반영 제안 가운데 이번 브리프에 없는 자료(Formant F3, 다임리서치 다비스, Amazon Proteus 2026-06 발표, Locus Aila 사례 ref-280, CLARA ref-352, KnowNo ref-350, 작업 지향 대화 서베이 ref-357)는 브리프에 없어 넣지 못했다. 다음 실행에서 재확인 후 반영을 검토한다.
- 5절: 국내 물류센터의 피커 유휴·로봇 대기 실측 자료가 필요하다.

## 이행한 수정 지시

- f7 운용 모드 설명 교정 — 'SEMIAUTOMATIC 운영자 HMI 실행 확인'과 'INTERVENED 새 주문 불수신'을 본문·용어집에서 빼고, 6절에 명세 표 10·11 그대로(SEMIAUTOMATIC 관제 제어·속도 HMI·조향 자동, INTERVENED 운영자 HMI 제어·복귀 뒤 실행될 주문 수신·즉시 동작은 cancelOrder 만, MANUAL 주문·동작 불가)를 [사실][^ref-031]로 썼다.
- f30 확인 유형 — 6절에서 VDA 5050 SEMIAUTOMATIC 항목을 빼고 작업자 동작마다의 확인과 자연어 지시의 해석 확인 두 유형으로 [추정] 서술했다(각주에서 ref-031 제외).
- 용어집 '운용 모드' 정의 — '운영자 확인이 필요한지'를 'HMI가 주행 속도를 제어하는지'로 고쳐 glossary_updates 에 냈다.
- 열린 질문 후보 3(SEMIAUTOMATIC 원격 확인) — 11절과 open_question_updates 에 등록하지 않았다.
- f15 강등 — 7절 국내 가이드 행에서 비상정지장치 위치 내용을 '보도에 따르면 … [추정]'으로 썼다.
- f20 강등 — 3·8절에서 '44건'을 쓰지 않고 분석 건수 미확인으로 두었으며 [추정]으로 썼다(검증되지 않은 점검표 제시도 넣지 않음).
- f11 — 7절 ISO 3691-4 행에서 '운전 모드·제동'을 빼고 판·대체·적용 범위(충전소·적재물 인계 스테이션 포함)만 [사실]로 썼다.
- f13 — 7절 R15.08 행에 '사용자 책임(3부, 발행 여부 미확인)'을 병기했다.
- f12 — 4절 협동 적용과 7절 ISO 10218 행에 'A3 해설 기준, ISO 원문 미열람'을 병기했다.
- f28 — 6절 SafeGate 문장을 '초록에서 물류 현장 평가는 확인되지 않는다'로 바꿨다.
- f3·f17·f26 — 5·6·8절에 '저자 계산 실험 기준', '가정 환경 실험', '가정·실험실 환경'을 병기했다.
- f21·f23·f24·f29 — 5·6·9절에서 [추정] 벤더 주장 병기를 유지했고 f29 에 '연계 대상: ' 표시를 유지했다.
- 7·9절 경계 — 안전 표준·국내 가이드·KS를 로봇 제조사·현장 통합사의 안전 기능 요구로 서술하고 ROP 역할은 f31 [추정](모드·안전 상태 표시, 재개·수동 전환 승인, 구역·권한 반영)으로만 썼으며 10절에서 25. 안전·위험 관리로 연결했다.
- 10절 — f24~f28 을 27. AI·학습·적응과 모델 운영과 연결했다(6절 본문에도 링크).
- 각주 — fetched:false 출처 전부의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-031·ref-051·ref-302·ref-104 는 붙이지 않았다.
- ref-477·ref-471·ref-474 발행일 — 각주 발행일을 '미확인'으로 적고 2017 추정은 쓰지 않았다.
