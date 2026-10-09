# 스토리텔러 산출 2026-10-09-10

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/index.md | draft | 다른 대분류와의 연결 절 첫 작성(A~Q 가운데 16개 대분류와의 연결, 현장 유형별 재묶음, 아직 다루지 않은 연결 목록), 참고 자료 절 끝에 각주 정의 43건 추가, 2차 수정 3건(장면 인식 모델 단정 삭제, C. 채팅 기반 구성·운영 호칭, 약어 풀어쓰기) 반영 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | N. 보안·개인정보 | 다른 대분류와의 연결 절 첫 작성(A~Q 가운데 16개 대분류, 현장 유형별 재묶음, 아직 다루지 않은 연결 목록), 참고 자료 각주 정의 43건 추가, 1차 수정 26건·2차 수정 3건 반영 | run 2026-10-09-10
- 홈 최근 업데이트: 2026-10-09 — N. 보안·개인정보: 다른 대분류와의 연결 절 첫 작성(16개 대분류와의 연결, EU 사이버복원력법 보고 의무·EU 데이터법·로봇 관리 API 인가 결함 사례 포함, 열린 질문 4건 추가)
- 대분류 최근 업데이트: 2026-10-09 — N. 보안·개인정보: 다른 대분류와의 연결 절 첫 작성 — 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 A~Q 16개 대분류의 연결, 참고 자료 각주 43건 추가
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 적극 악용 취약점 | Actively Exploited Vulnerability (EU Cyber Resilience Act) | 악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다. | 52, 57, 59 | ref-1228 |
| new | 연결 제품 | Connected Product (EU Data Act) | 사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다. | 53, 58 | ref-1376 |
| new | 원격 증명 | Remote Attestation | 원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다. | 52, 18 | ref-1374 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_dds_security.html |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_threat_model.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 논문 | medium | https://arxiv.org/abs/2608.25690 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_access_control_policies.html |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 업계 보고서 | medium | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 정부·연구기관 | medium | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 논문 | medium | https://arxiv.org/abs/2503.07885 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG | Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 논문 | medium | https://arxiv.org/abs/2410.13691 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 정부·연구기관 | medium | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 기사 | low | https://byline.network/2025/10/31-283/ |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 논문 | medium | https://arxiv.org/abs/2602.17822 |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 표준 | medium | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ |
| ref-1106 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 오픈소스 문서 | medium | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| ref-1107 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 정부·연구기관 | medium | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 |
| ref-1109 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 업계 보고서 | medium | https://www.ies.co.uk/reference-library/machinery-regulation-guide |
| ref-1110 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 논문 | medium | https://arxiv.org/abs/2403.09567 |
| ref-1111 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시 | 기사 | low | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 |
| ref-1112 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 논문 | medium | https://arxiv.org/abs/2608.00747 |
| ref-1113 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 논문 | medium | https://arxiv.org/abs/2408.03515 |
| ref-1114 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 논문 | medium | https://files01.core.ac.uk/download/pdf/84891817.pdf |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 업계 보고서 | medium | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 |
| ref-1136 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 기사 | low | https://www.koit.co.kr/news/articleView.html?idxno=125844 |
| ref-1138 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용 | 정부·연구기관 | medium | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 |
| ref-1141 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 기사 | low | https://view.asiae.co.kr/article/2026091410054053414 |
| ref-1145 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 논문 | medium | https://arxiv.org/abs/2609.03055 |
| ref-1146 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 논문 | medium | https://doi.org/10.1145/3776734.3794481 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 오픈소스 문서 | medium | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst |
| ref-1299 | ST Engineering Aethon (Newswire 게재 보도자료) | ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals | 벤더 문서 | low | https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264 |
| ref-1301 | 경향신문 (곽희양) | 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 | 기사 | low | https://www.khan.co.kr/article/202007031130001 |
| ref-1242 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 논문 | medium | https://arxiv.org/abs/2211.09507 |
| ref-1263 | 메트로신문 | AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원 | 기사 | low | https://www.metroseoul.co.kr/article/20260506500296 |
| ref-1228 | European Commission (Shaping Europe's digital future) | CRA reporting | 정부·연구기관 | high | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting |
| ref-1368 | The Register | Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots | 기사 | medium | https://www.theregister.com/2025/08/29/pudu_robots_hackable/ |
| ref-1369 | Hackmag | Researcher finds a way to hack Chinese Pudu service robots | 기사 | low | https://hackmag.com/news/pudu-bugs |
| ref-1370 | Silicon UK | France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance | 기사 | medium | https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858 |
| ref-1371 | CNIL (Commission nationale de l'informatique et des libertés) | Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million | 정부·연구기관 | medium | https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million |
| ref-1372 | 바이라인네트워크 (곽중희) | 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어" | 기사 | medium | https://byline.network/2026/09/14-623/ |
| ref-1373 | 바이라인네트워크 | 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개 | 기사 | medium | https://byline.network/2026/03/6-340/ |
| ref-1374 | Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv) | Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics | 논문 | medium | https://arxiv.org/abs/2609.08280 |
| ref-1375 | KUKA (Robotics Tomorrow 게재 보도자료) | KUKA is First to Achieve Security Level 2 Certification for Robotics Industry | 벤더 문서 | low | https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/ |
| ref-1376 | European Commission (Shaping Europe's digital future) | Data Act explained | 정부·연구기관 | high | https://digital-strategy.ec.europa.eu/en/policies/data-act-explained |
| ref-1260 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 표준 | medium | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? | 51, 20, 54 | 열림 | — |
| new | — | 로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? (관련: oq-082) | 52, 18, 38 | 열림 | — |
| new | — | EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? (관련: oq-259) | 58, 53 | 열림 | — |
| new | — | 작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? (관련: oq-285) | 53, 60, 39 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 가정 | 작업 대상 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 가정 | 제약 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 병원 | 완료·인계 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 병원 | 예외·성과 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 상업 시설 | 예외·성과 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 제조 공장 | 예외·성과 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 실외 | 제약 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |
| 기타 | 예외·성과 | docs/categories/security-and-privacy/index.md#다른-대분류와의-연결 | N. 보안·개인정보 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 51. 인증·권한·격리 페이지(이전 분류 기준)의 10절에 VDA 5050 updateCertificate(f5), Pudu 관리 API 인가 결함(f20·f22), Open-RMF OIDC·SROS 2(f37) 연결을 반영할 갱신 실행이 필요하다 — 대분류 연결 절과 세부영역 페이지의 근거를 맞추기 위해서다.
- 52. 통신 보호·위협 관리·감사 7절에 EU 사이버복원력법 보고 의무(2026-09-11 시행, ref-1228)를 반영하고, 규정 원문 제14조를 열어 통지 경로·시한을 원문으로 확인해야 한다 — 이번에는 집행위원회 안내 페이지만 확인했다.
- D. 공간·지도 모델 페이지의 '다른 대분류와의 연결'에서 N. 보안·개인정보 연결이 '근거 없음'으로 남아 있으므로, 이번 f14·f15 근거로 그 대분류 페이지를 갱신하는 실행이 필요하다.
- Pudu 사례의 연구자 원문 공개와 제조사 공식 공지를 열어, 신고 지연 이유에 대한 두 기사(The Register·Hackmag)의 엇갈린 설명을 원문으로 확인해야 한다 — 현재는 같은 공개를 옮긴 기사 두 건뿐이다.
- KISA 로봇 보안모델 고도화판·로봇 보안요구사항 해설서 원문의 요구 항목(oq-250)과 ISO 10218-1:2025 사이버보안 조항 번호(oq-102)를 확인해야 A. 기획·사업·M. 안전 연결을 구체화할 수 있다.
- 배달로봇 원본 영상 실증특례(ref-1263)·개인정보위 원본 활용 허용(ref-1138)에서 원본 영상으로 학습하는 모델의 종류(예: 장면 인식·주행 모델)를 원문으로 확인해야 L. AI·학습 기술의 45. 문서·도면·장면 이해 연결을 구체화할 수 있다 — 2차 검증에서 브리프 밖 단정으로 삭제했다.
- N. 보안·개인정보와 5. 로봇 능력·작업 표현, 8~11. 채팅 영역, 23. 업무 시스템 연동, 24·26·28. 계획 영역, 30. 로봇 간 협업·물리적 인계, 33·35. 설계 영역, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육의 연결 근거가 없다 — 다음 대분류 연결 실행의 조사 대상이다.
- 물류창고 현장의 로봇(작업자 스캐너가 아닌) 보안·개인정보 사례가 없어 물류창고 × N. 보안·개인정보 칸을 채우지 못했다 — 물류창고 로봇 관제의 보안 사고·감독기관 결정을 찾아야 한다.

## 이행한 수정 지시

- 절 이름 — patches 의 section 을 번호 없는 '다른 대분류와의 연결'로 쓰고, 그 밖에는 '참고 자료' 절에 각주 정의만 append 했다.
- 각주 정의 — 새로 인용한 출처 43건의 정의를 '참고 자료' 절 끝에 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 2026-10-09' 형식으로 더했고 기존 ref-009·ref-010 정의는 그대로 두었다.
- 원문 미열람 표기 — 지시된 31개 출처(ref-494 ~ ref-1260, ref-1371 포함)의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- ref-009·ref-010·ref-031·ref-405·ref-579 — 각주에 '(원문 미열람)'을 붙이지 않았고, reference_updates 에서 summary 의 '원문 미열람.' 문구를 빼고 입력 원문 텍스트로 대조했다고 고쳐 source_unopened: false 로 두었다.
- ref-1228·ref-1376 발행일 — 각주 발행일 자리에 각각 '미확인(페이지 최종 갱신 2026-09-11)', '미확인(페이지 최종 갱신 2025-12-15)'을 썼다.
- f2 — A. 기획·사업 항목에서 [추정] 뒤에 '벤더 주장'을 병기하고, 인증 사실과 '최초'가 모두 KUKA 보도자료의 주장이며 인증 기관이 적혀 있지 않음을 밝혔다.
- f18 — E. 사물·사람·실시간 상태 항목에서 [추정]과 '벤더 주장'을 유지하고, Zena RX 는 제조사 보도자료(2024-04-29), 공동주택 비밀번호 방식은 2020-07 계획 단계 보도임을 밝혔다.
- 범위 경계 — 첫머리 범위 경계 단락에 제어기·설비·기기 쪽 연계 대상을 밝히고, f2·f3·f44 는 제어기 보안을 로봇 제조사 쪽 연계 대상으로, f21·f25·f55 의 방화벽·VPN·승강기 제어는 시설·설비 제어 경계의 연계 대상으로, f14·f18·f56 의 앱·기기 보안·잠금 칸 인증·얼굴 가림은 제조사 기능의 연계 대상으로 각 항목에 짧게 적었다.
- 법 적용 판단 — 첫머리 범위 경계 단락에서 법령·규정 적용 판단은 운영 사업자·법무가 맡는 연계 대상이고 ROP 몫은 기록·통보·데이터 흐름 규칙 제공까지라고 한 번 밝혔다.
- f5 — B. 로봇 온톨로지 항목에서 키·인증서 내려받기 링크는 필수, 인증 기관 내려받기 링크만 선택 매개변수라고 고쳐 썼다.
- f5·f28 — ref-031 은 직접 인용 없이 모두 재서술했다(B. 로봇 온톨로지, H. 실행·협업·예외 복구, F. 연동 항목).
- f11 — RoboGuard 수치(92% 초과→3% 미만)를 arXiv 개정판 v2(2026-03-03) 기준으로 적고, v1 은 다른 수치를 보고했으며 RoboPAIR·RoboGuard 두 수치 모두 저자 보고값·독립 재현 미확인임을 병기했다.
- f16 — E. 사물·사람·실시간 상태 항목에서 프리프린트임을 밝히고 87%·약 3 ms 가 저자 보고값이며 독립 재현이 확인되지 않았음을 병기했다.
- f17 — '위치 스푸핑이 배정을 무너뜨린다'를 '위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있다(GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인)'로 고쳤다.
- f35 — 통지 경로를 'ENISA 단일 보고 플랫폼을 통해 주 사업장 국가의 CSIRT 에 알려야'로 고치고, 집행위원회 안내 페이지 기준이며 규정 원문은 열지 않았다고 밝혔다.
- f49 — '(보통 제조사)'를 삭제했다.
- f39 — K. 플랫폼 아키텍처·인프라 항목에서 보관 기간 연장 조치의 적용 대상(점검 사업자 한정 여부)과 근거 조항이 미확인임을 바로 뒤 문장에 밝히고 oq-214 를 붙였다.
- f20·f29·f34·f55 — 두 기사가 같은 연구자 공개를 옮긴 것으로 교차 확인이 아니라는 점, 실제 악용·피해 보도가 없다는 점, f29·f55 의 플릿 정지·사무실 시스템 피해는 연구자·매체의 가능성 평가라는 점을 F. 연동, H. 실행·협업·예외 복구, J. 현장 운영·관제, Q. 현장 유형별 적용 항목에 밝혔다.
- f34 — 신고 지연 이유를 The Register 는 제조사가 신고 창구 부재를 인정했다고, Hackmag 은 제조사가 다른 경로로 보고를 받았다고 설명했다고 전한다며 두 설명을 함께 적었다.
- f33 — J. 현장 운영·관제 항목에서 '업계 해설에 따르면'으로 시작하고 규정 원문 미열람과 오케스트레이션 플랫폼 적용 여부가 oq-249 임을 유지했다.
- f1 — A. 기획·사업 항목에서 같은 정부 발표를 옮긴 기사 기준이라 독립 교차 확인이 아니며 구체 요구 항목은 미확인(oq-250)임을 밝혔다.
- f52 — P. 거버넌스·법규·사회 항목에서 로봇이 아니라 작업자 휴대 스캐너 기록 사례이며 Amazon 이 사실과 다르다며 이의 제기 권리를 유보했다고 밝혔고, Q. 현장 유형별 적용의 61. 물류창고 항목에서 ROP 적용 사례로 보지 않는다고 적었으며 site_matrix_updates 에 물류창고 칸을 넣지 않았다.
- 18·34 구분 — f16·f17 은 E. 사물·사람·실시간 상태 항목에 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽으로, f30·f31 은 I. 설계·시뮬레이션 항목에 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 나눠 쓰고 서로 구분된다고 밝혔다.
- L. AI·학습 기술 교차 규칙 — f11 은 13. 대화형 기능의 신뢰·기반과 44. 로봇 기반 모델·언어 모델 계획을 함께, f40 은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 66. 실외 적용 사례를 함께, f41 은 47. AI·학습·적응과 모델 운영과 적용 대상 13. 대화형 기능의 신뢰·기반을 함께 적었다.
- 열린 질문 등록 — 위조 텔레메트리 질문 끝에 '(관련: oq-082)', CNIL 판단 적용 질문에 '(관련: oq-285)', 데이터법상 플랫폼 지위 질문에 '(관련: oq-259)'를 붙여 open_question_updates 로 냈다.
- 아직 다루지 않은 연결 — 절 끝 '아직 다루지 않은 연결' 소제목 아래에 5. 로봇 능력·작업 표현, 8~11. 채팅 영역, 23·24·26·28·30·33·35·46·49·56번 세부영역을 대분류별로 번호와 이름을 함께 써서 목록으로 남겼다.
- 2차: L. AI·학습 기술 항목 장면 인식 모델 단정 — '45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 ↔ 53. 개인정보·영상 데이터' 항목에서 '학습 데이터로 쓰이는 대상은 장면 인식 모델이며,'를 삭제하고 '현장 유형으로는 Q. 현장 유형별 적용의 66. 실외 사례다.'만 남겼으며, 학습 모델 종류 확인은 additional_research_requests 에 적었다.
- 2차: 대분류 호칭 — C. 채팅 기반 구성·운영 소제목 아래 안내 문장의 '분류 원문 C 주석은'을 '분류 원문의 C. 채팅 기반 구성·운영 주석은'으로 고쳤다.
- 2차: 약어 풀어쓰기 — 첫 등장에서 OWASP(Open Worldwide Application Security Project), 미국 사이버보안·기반시설보안청(Cybersecurity and Infrastructure Security Agency, CISA), 공통 취약점 식별 번호(Common Vulnerabilities and Exposures, CVE), 공통 취약점 점수 체계(Common Vulnerability Scoring System, CVSS), SROS 2(Secure ROS 2, F. 연동의 22. 설비·건물 시스템 연동 항목), 데이터 분산 서비스(Data Distribution Service, DDS)로 풀어 썼고 문장 내용·태그·각주는 바꾸지 않았다.
