# 스토리텔러 산출 2026-10-09-09

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/safety/index.md | draft | '다른 대분류와의 연결' 절 첫 작성: 16개 대분류와의 연결(주장 70건 근거), Q. 현장 유형별 적용 현장별 정리, 아직 다루지 않은 연결 7건, 각주 정의 48건 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | M. 안전 | 다른 대분류와의 연결 절 첫 작성(16개 대분류와의 연결, 현장 유형별 근거, 아직 다루지 않은 연결 7건) | run 2026-10-09-09
- 홈 최근 업데이트: 2026-10-09 — M. 안전: '다른 대분류와의 연결' 절을 처음 채웠다(16개 대분류와의 연결, VDA 5050 안전 상태·운용 모드, R15.08-3 사용자 의무, 실외 보험·인증, 아직 다루지 않은 연결 7건)
- 대분류 최근 업데이트: 2026-10-09 — M. 안전: '다른 대분류와의 연결' 절 첫 작성(48. 안전·위험 관리·49. 사람 근접 안전·50. 안전 표준·인증·사고 조사와 A~Q 대분류의 연결, 새 열린 질문 4건)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 변경 관리 | Management of Change (MOC) | 설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다. | 48, 57, 40 | ref-1421, ref-1420, ref-1419 |
| new | 안전 상태 보고 | Safety State (VDA 5050 safetyState) | VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다. | 48, 29 | ref-031 |
| new | 무선 안전 비상정지 | Wireless Safety-rated Emergency Stop | 관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이며, 이 위키에서는 FORT Robotics 업체 사례 소개(ref-1422)에 기댄 용어다. | 48, 42 | ref-1422 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_demos |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 논문 | medium | https://journals.sagepub.com/doi/10.1177/02783649241287797 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 표준 | medium | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 정부·연구기관 | medium | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 논문 | medium | https://arxiv.org/abs/2502.20693 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf/issues/658 |
| ref-621 | European Commission | AI Act \| Shaping Europe's digital future | 정부·연구기관 | medium | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 정부·연구기관 | medium | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 정부·연구기관 | medium | https://www.kiria.org/portal/cert/portalCertEstiSafe.do |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 논문 | medium | https://arxiv.org/abs/2602.17822 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 논문 | medium | https://arxiv.org/abs/2306.16740 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 벤더 문서 | low | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 논문 | medium | https://arxiv.org/abs/2508.19731 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 기사 | low | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 업계 보고서 | medium | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 표준 | medium | https://iss.rs/en/project/show/iso:proj:83498 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 정부·연구기관 | medium | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 논문 | medium | https://arxiv.org/abs/2205.06564 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 논문 | medium | https://eprints.whiterose.ac.uk/id/eprint/217393/ |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 기사 | low | https://www.khan.co.kr/article/202311081103001 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 기사 | low | https://www.idomin.com/news/articleView.html?idxno=2015923 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 정부·연구기관 | medium | https://iliad-project.eu/concluding-iliad/ |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 기사 | low | https://v.daum.net/v/bc4riunbUE |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 논문 | medium | https://arxiv.org/abs/2404.05050 |
| ref-1241 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 논문 | medium | https://arxiv.org/abs/2011.10294 |
| ref-1242 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 논문 | medium | https://arxiv.org/abs/2211.09507 |
| ref-1249 | Wind River (Engblom, J. 인터뷰, Buchwieser, A.) | Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser | 벤더 문서 | low | https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv) | Jailbreaking LLM-Controlled Robots | 논문 | medium | https://arxiv.org/abs/2410.13691 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv) | Safety Guardrails for LLM-Enabled Robots | 논문 | medium | https://arxiv.org/abs/2503.07885 |
| ref-1341 | 법무법인 태평양(BKL) AI팀 | AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 | 업계 보고서 | medium | https://www.bkl.co.kr/law/insight/newsletter/6248 |
| ref-1419 | ANSI (American National Standards Institute) Blog | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 표준 | medium | https://blog.ansi.org/?p=190868 |
| ref-1420 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 표준 | medium | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download |
| ref-1421 | Robotics 24/7 | A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available | 기사 | medium | https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available |
| ref-1422 | FORT Robotics (A3 Case Studies 게재) | Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs | 벤더 문서 | low | https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs |
| ref-1423 | 법제처 (네플라 위키 게재본, 법제처 원문 미열람) | [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련) | 정부·연구기관 | medium | https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k |
| ref-1424 | 메트로신문 (한용수) | 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막 | 기사 | medium | https://www.metroseoul.co.kr/article/20231116500208 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 표준 | medium | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 |
| ref-1426 | Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS) | ROSMonitoring: A Runtime Verification Framework for ROS | 논문 | medium | https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/ |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? | 48, 42, 29 | 열림 | — |
| new | — | ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가? | 50, 22 | 열림 | — |
| new | — | 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? | 48, 38, 54 | 열림 | — |
| new | — | 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? | 59, 58, 66 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 예외·성과 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 물류창고 | 제약 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 제조 공장 | 제약 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 병원 | 제약 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 가정 | 예외·성과 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 실외 | 제약 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 실외 | 작업 대상 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |
| 기타 | 제약 | docs/categories/safety/index.md#다른-대분류와의-연결 | M. 안전 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 다른 대분류와의 연결 절의 '아직 다루지 않은 연결': 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화와 M. 안전(48·49·50)을 잇는 검증 가능한 근거가 필요하다(예: 안전 정지가 처리량 지표에 주는 영향, 외부 API 의 정지·재개 권한, 안전 기록의 보존·관측성).
- Q. 현장 유형별 적용의 64. 상업 시설에서 실제 현장의 사람 근접 안전 사례(속도·거리 규칙, 혼잡 대응)가 필요하다. 이번 근거(Open-RMF 공항 터미널 crowdsim)는 시뮬레이션 예제라 현장 사례로 쓰지 않았다.
- ISO 13482 개정 최종판에 승강기 협동 로봇(부속서 H)·사이버보안·데이터 보호 절이 남았는지 확인이 필요하다(oq-254).
- EN ISO 10218-1/-2:2025 가 기계류 규정 (EU) 2023/1230 에 따른 조화 표준으로도 지정되는지 확인이 필요하다(본문에서 미확인으로 남김).
- ANSI/A3 R15.08-3-2026 본문의 사용자 의무 조항(교육·안전 작업 절차·변경 관리)과, 고용노동부의 서비스 로봇 운영 인력 대상 로봇작업 특별교육 적용 지침 확인이 필요하다(oq-265, oq-275).
- 다음 실행 후보(이번 실행 범위 밖): 48. 안전·위험 관리 페이지 10절에 이번 실행의 f32·f33(VDA 5050 안전 상태·재개 판단), f47·f61(R15.08-3 사용자 의무·배치 후 변경), f54(ISO 10218:2025 사이버보안) 반영.

## 이행한 수정 지시

- 섹션 이름 — patches 의 section 을 대분류 페이지의 기존 H2 그대로 번호 없는 '다른 대분류와의 연결'로 썼고, 다른 절과 auto 마커는 보내지 않았다.
- f3 — A. 기획·사업 항목에서 R15.08-3 발행일을 'A3 판매 페이지 기준 2026-04-23, 공개 발표 보도 2026-10-04(Robotics 24/7)'로 함께 쓰고, '2025~2026년에 몰려 있다'는 별도 [추정] 문장으로 분리했으며, ISO 13482 FDIS 단계에 기준일 2026-09-15 와 근거 페이지 원문 미열람을 밝혔다.
- f4 — 보험(또는 공제) 의무 가입과 손해보장사업 실시기관 지정만 [사실]로 쓰고 '기사 1건, 2023-11-16 보도 기준'을 밝혔으며, 폭 기준(800mm 미만)과 조항 번호는 쓰지 않았다.
- f39 — I. 설계·시뮬레이션 항목에서 공항 터미널 crowdsim 을 '현장 사례가 아니라 시뮬레이션 예제'로만 썼고, Q 항목의 64. 상업 시설 줄에는 현장 사례로 넣지 않고 '아직 다루지 않은 연결'에 64. 상업 시설 실제 사례를 두었으며, site_matrix_updates 에 상업 시설을 넣지 않았다.
- f40·f69·f35·f20 — f40 에 '모의 병원 환경의 시뮬레이션 평가', f69 에 '실제 사고가 아닌 모의 사고 시나리오', f35 에 '2026-09-29 보도 기준, 원인 미확정', f20 에 '기사 1건, 2024-07-12 기준'을 문장 안에 밝혔다(Q 항목의 재언급에도 같은 병기).
- f10·f11 — C. 채팅 기반 구성·운영 항목의 92% 이상→3% 미만과 공격 성공률 100% 뒤에 각각 '(저자 보고값, 독립 재현 미확인)'을 병기했다.
- f47·f61 — J. 현장 운영·관제 항목에 'ANSI 블로그·Robotics 24/7·A3 판매 페이지의 요약 기준이며 표준 본문은 열람하지 않았다'를 밝히고, 안전 작업 절차는 ref-1419, 변경 관리는 ref-1421·ref-1420 각주로 나눠 달았다. O 항목의 f61 에도 'ANSI 블로그 2026-09-17 요약 기준, 표준 본문 미열람'을 넣었다.
- f49·f68 — 두 주장 모두 '[추정] 벤더 주장' 형식으로 쓰고, f49 에 '소규모 시범 운영 단계, 플릿 관리 시스템·WMS 연동 언급 없음'을 함께 썼다. 용어집 '무선 안전 비상정지' 정의에 ref-1422 업체 사례에 기댄 용어임을 밝히고 PLd 같은 성능 주장은 넣지 않았다.
- f17·f41 및 안전 기능 경계 — f17·f41 을 각각 '연계 대상으로'로 시작하는 한 문장으로 짧게 썼고, 머리 단락과 C·H·K 항목에서 비상정지 회로·보호 필드·무선 안전 정지를 제조사·통합자 몫의 연계 대상으로, ROP 몫을 상태 수신과 작업 보류·재배정·재개 지시로 한정했다.
- f55 — P. 거버넌스·법규·사회 항목에서 시행결정 (EU) 2026/2015 로 2026-09-07 관보 게재, 기계류 지침 2006/42/EC 조화까지만 쓰고 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 미확인으로 남겼다.
- f64 — 58. 다사업자 책임·계약·데이터 연결에서 R15.08-2 발행 사실만 [사실]로 쓰고, 통합자·ROP 사업자 역할 분담은 A 항목의 f2 [추정]과 oq-096 으로만 연결했다.
- 18 대 34 구분 — E. 사물·사람·실시간 상태 항목(f18·f19)에 '현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽', I. 설계·시뮬레이션 항목(f38·f39·f40)에 '가정한 미래를 실험하는 34·36 쪽이며 18 과 섞지 않는다'를 문장으로 밝혀 따로 썼다.
- 각주 정의 — 이번 실행에서 연 ref-004·ref-031·ref-286·ref-406·ref-1116·ref-1419~ref-1426 은 접근일 2026-10-09 만 쓰고, 나머지 재사용 출처 35건은 접근일 뒤에 ' (원문 미열람)'을 붙였으며 reference_updates 에 source_unopened: true 를 넣었다. ref-1423 은 각주와 reference_updates 의 기관 표기를 '법제처 (네플라 위키 게재본, 법제처 원문 미열람)'으로 썼다. ref-004·ref-286·ref-406 의 요약에서 '원문 미열람.' 접두어를 뺐다.
- 새 열린 질문 2 — 질문을 'ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가?'로 줄였고, 최종판 반영 여부는 F. 연동 항목 본문에서 oq-254 로 연결했다.
- 기존 연결 표시 — f13·f14·f16·f17(ref-031·ref-470·ref-161), f18~f21(ref-286·ref-1181·ref-1180), f29(ref-104)는 같은 각주 id 를 다시 쓰고 D·E·G 항목 첫머리에 '같은 연결은 … 페이지의 연결 절에도 있다'를 밝혔다.
- 미근거 연결 — 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설 실제 사례를 내용 없이 '아직 다루지 않은 연결' 소절에 번호와 이름으로 나열했다.
