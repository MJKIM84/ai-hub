# 스토리텔러 산출 2026-09-25-59

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | draft | 영역 심화: 3~11절 신규 작성(4·6·7·10·11절은 주제 페이지로 분리), 2차 수정: 9절 f8 태그 분리, 3절 첫 문장 범위 정정, 10절 요약 의견 주체 표시, 3·9절 약어 풀이 |
| create | docs/topics/2026/2026-09-25-area23-s6.md | draft | 자동 분리: 23. 시험·형식 검증·벤치마크 의 "6. 대표 접근법과 기술" 절을 옮겼다(2차 수정 없음) |
| create | docs/topics/2026/2026-09-25-area23-s7.md | draft | 자동 분리: 23. 시험·형식 검증·벤치마크 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 없음) |
| create | docs/topics/2026/2026-09-25-area23-s4.md | draft | 자동 분리: 23. 시험·형식 검증·벤치마크 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차 수정: 적합성 시험 항목에 '벤더 주장' 병기 |
| create | docs/topics/2026/2026-09-25-area23-s11.md | draft | 자동 분리: 23. 시험·형식 검증·벤치마크 의 "11. 열린 질문" 절을 옮겼다(2차 수정 없음) |
| create | docs/topics/2026/2026-09-25-area23-s10.md | draft | 자동 분리: 23. 시험·형식 검증·벤치마크 의 "10. 다른 연구영역과의 연결" 절을 옮겼다. 2차 수정: 1절·3절 요약 문장에 '구축자 의견' 표시 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 23. 시험·형식 검증·벤치마크 | 영역 심화: 3~11절 신규 작성(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크), 1차 조건부 승인 수정 16건·2차 수정 5건 반영 | run 2026-09-25-59
- 홈 최근 업데이트: 2026-09-25 — 23. 시험·형식 검증·벤치마크: 영역 심화로 3~11절 첫 작성(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크, 피킹 단계 회귀 시험 가상 시나리오)
- 대분류 최근 업데이트: 2026-09-25 — 23. 시험·형식 검증·벤치마크: 영역 심화로 3~11절 첫 작성, ROP 시험 몫과 로봇 안전·성능 시험(연계 대상) 경계 정리
- 세부영역 최근 업데이트: 2026-09-25 — 23. 시험·형식 검증·벤치마크: 3~11절 신규 작성, 열린 질문 3건 추가, oq-055·oq-058 부분 근거 기록

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 장애 주입 | Fault Injection | 시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다. | 23, 12, 20 | ref-629, ref-633 |
| new | 회귀 시험 | Regression Testing | 소프트웨어나 설정을 바꾼 뒤 기존에 통과하던 정상·장애 시나리오를 다시 실행해 변경이 기존 동작을 깨뜨리지 않았는지 확인하는 시험이다. | 23, 24 | ref-633, ref-406 |
| new | 런타임 검증 | Runtime Verification | 실행 중인 시스템의 사건을 감시기로 관찰해 명세한 성질의 위반을 판정하고 기록하거나 차단하는 검증 기법이다. | 23, 12, 19 | ref-634 |
| new | 모델 검사 | Model Checking | 시스템을 상태 전이 모델로 표현하고 교착 부재 같은 성질이 도달 가능한 모든 상태에서 성립하는지 자동으로 확인하는 형식 검증 기법이다. | 23, 15 | ref-631, ref-643 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-008 | NIST | ARIAC Documentation | 정부·연구기관 | medium | https://pages.nist.gov/ARIAC_docs/en/latest/ |
| ref-629 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html |
| ref-630 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Scoring | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html |
| ref-631 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 논문 | medium | https://arxiv.org/abs/1807.00048 |
| ref-632 | Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S. | A Study on Challenges of Testing Robotic Systems | 논문 | medium | https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc |
| ref-633 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 오픈소스 문서 | medium | https://github.com/reeceholland/ros2_fault_injection |
| ref-634 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 오픈소스 문서 | high | https://github.com/autonomy-and-verification-uol/ROSMonitoring |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 논문 | medium | https://arxiv.org/abs/1906.08291 |
| ref-636 | IDM Lab (USC) 게재 초록, 저자 미확인 | The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration] | 논문 | medium | https://idm-lab.org/bib/abstracts/Koen24p.html |
| ref-637 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 논문 | medium | https://arxiv.org/abs/2602.15721 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-639 | NIST | ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles | 정부·연구기관 | medium | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles |
| ref-640 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 |
| ref-641 | 한국로봇산업진흥원(KIRIA) | 시험평가 \| KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 정부·연구기관 | medium | https://kiria.org/rp/kiria/tva/inr/page.dn |
| ref-642 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 벤더 문서 | low | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ |
| ref-643 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? | 23, 24 | 열림 | — |
| new | — | BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? | 23, 15 | 열림 | — |
| new | — | 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? | 23, 28 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |
| 피킹 | 작업 대상 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |
| 피킹 | 수행 자원 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |
| 피킹 | 제약 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |
| 피킹 | 완료·인계 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |
| 피킹 | 예외·성과 | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 23. 시험·형식 검증·벤치마크 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| League of Robot Runners | 평가 프로그램 | League of Robot Runners (Amazon Robotics 후원) | 23, 15 | ref-636 | https://idm-lab.org/bib/abstracts/Koen24p.html |
| ASTM F45 위원회(무인 자동 유도 산업 차량) | 표준 | ASTM International (NIST 참여) | 23, 25 | ref-639 | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles |
| KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 | 표준 | 국가표준인증종합정보센터(KSSN) | 23 | ref-640 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 |
| 한국로봇산업진흥원 로봇 시험평가 | 평가 프로그램 | 한국로봇산업진흥원(KIRIA) | 23 | ref-641 | https://kiria.org/rp/kiria/tva/inr/page.dn |
| ros2_fault_injection | 오픈소스 | reeceholland (GitHub) | 23 | ref-633 | https://github.com/reeceholland/ros2_fault_injection |
| ROSMonitoring | 오픈소스 | University of Liverpool Autonomy and Verification | 23, 12, 19 | ref-634 | https://github.com/autonomy-and-verification-uol/ROSMonitoring |
| LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) | 오픈소스 | Yan, J. 외(arXiv 2602.15721) | 23, 15 | ref-637 | https://arxiv.org/abs/2602.15721 |

## 추가 조사 요청

- 7·9절: ISO 3691-4:2023 의 사람 감지·안정성 시험과 부속서 검증 절차 세부 — 검증에서 확인되지 않아 본문에서 뺐다(유료 표준, 공개 해설 자료 필요).
- 7절: ASTM F45 개별 시험 방법(F3244 등)의 내용 — 개별 시험 방법이 미확인이라 본문에 쓰지 않았다.
- 7절: KS B ISO 18646 제2부의 존재·내용과 각 부의 KS 제정일·판 — 제2부가 미확인이다.
- 9·11절(oq-055): VDA 5050 공식 적합성 시험 절차·인증 기관(VDMA 시험 환경 계획 여부)과 arculus 등 제3자 적합성 시험 도구 — 부재 여부가 확인되지 않았다.
- 5·6절: 물류 오케스트레이션 소프트웨어에 장애 주입·회귀 시험을 적용해 결과를 공개한 현장 사례 — 2절 질문의 답(f21)이 추정에 머문다.
- 3·8절: f4(Luckcuck 외)·f6(Afzal 외)·f11(Stern 외) 원문 또는 독립 출처 교차 확인 — 검증자가 재검색하지 못하고 서지만 대조했다.
- 11절: oq-063(도킹 정밀도 시험과 파지 허용 오차 연결)·oq-077(지도 정합 합격 기준) 조사 — 이번 실행에서 다루지 않았다.
- 6·7절: 예산으로 미룸 — Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터.

## 이행한 수정 지시

- 원문 미열람 표기 — 13절과 분리 주제 페이지 8절에서 ref-631·632·186·636·637·470·639·640·641·642·643 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-629·630·633·634·406 에는 붙이지 않았다.
- ref-637 서지 정정 — 각주와 reference_updates 의 기관을 'Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.'로, 발행일을 2026-02-17 로 고쳤다.
- ref-642 발행일·벤더 주장 — 발행일을 2026-04 로 적고, 9절 f18 문장은 [추정] 벤더 주장을 유지하며 대상 기종(OTTO 100·600·1200·1500)과 파트너 세 곳만 쓰고 인증 시험 항목을 '미확인'으로 두었다.
- f14 한정 — 7·9절에서 '안전 요구사항과 검증 수단을 정한다'까지만 [사실]로 쓰고 사람 감지·안정성 시험·부속서 절차는 빼고 '세부 미확인'으로 표기했다.
- f15 한정 — 7절 ASTM F45 행에 분과 구성과 NIST 참여만 쓰고 F3244 등 개별 시험 방법은 쓰지 않았다.
- f16 기준일 — 7절에 'KS B ISO 18646-1, 2022 확인'을 적고 다른 부는 '제3부 조작 등'으로만 쓰며 제2부 내용은 미확인으로 두었다.
- f1·f2 기준일과 ref-008 재사용 — 6·7절에 'ARIAC 문서 main 브랜치, 2026-09-25 확인(ARIAC 2025 기준)'을 적고 ARIAC 소개 문장과 7절 ARIAC 행에 [^ref-008]을 재사용했으며, 원문에 연도가 없으므로 ref-629·630 각주의 발행일을 '미확인'(JSON null)으로 두었다.
- f4 인용 금지 — 3·6·8절에서 영어 구절을 직접 인용하지 않고 한국어로 재서술했다.
- f6 자기 규정 — 3절에 '저자들은 이 연구를 로봇 시스템 시험에 초점을 둔 첫 연구로 소개했다'로 썼다.
- f7 README 한정 — 4·6·7절 기능 서술을 'README 기준'으로 한정하고 6절에 개인 주도 프로젝트로 성숙도·라이선스가 미확인임을 한 번 밝혔다.
- f8 Twist 분류 — 9절에서 센서 신호를 오도메트리·레이저 스캔·IMU·점군으로 적고 속도 명령(Twist)은 명령 조작 대상으로 따로 적었다.
- f20 의견 주체 — 10절 22. 시뮬레이션·예측용 디지털 트윈 항목의 [의견] 문장에 '구축자 의견'임을 밝혔다.
- f22 가상 표기 — 5절 표와 서술 문장 안에 가상 시나리오임을 밝히고 수치를 넣지 않았으며 흐름 단계 '피킹', 항목 '완료·인계'를 명시했다.
- f19·f21·f23·f24 표현 — 5·9·11절에서 [추정]을 유지하고 '~로 보인다' 수준으로 썼으며, 9절 표 아래에 교착 검증 근거(ref-643)가 원문 미열람 자료임을 적고 각주에도 원문 미열람을 표기했다.
- 11절 열린 질문 — oq-055(ref-642)·oq-058(ref-637)은 부분 근거만 적고 열림을 유지했고, oq-063·oq-077 은 상태를 바꾸지 않고 미조사로 적었으며, 새 질문 3건을 open_question_updates 에 new 로 냈다.
- 용어 표기 — 장애 주입·회귀 시험·런타임 검증·모델 검사를 glossary_updates 로 내고, 본문에 기존 용어집 표기 '교착 (Deadlock)', '적합성 시험 (Conformance Test)', '다중 에이전트 경로 찾기 (MAPF)', '플릿 관리 시스템 (FMS)', '산업 자동화용 민첩 로봇 경진대회 (ARIAC)'를 그대로 쓰고 용어집에 링크했다.
- 분량 초과 자동 분리: 23. 시험·형식 검증·벤치마크 본문 8,450자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,667자
- 형식 검증 오류 수정 — docs/topics/2026/2026-09-25-area23-s10.md 3절의 세부영역 링크 9개를 세부영역 페이지 기준 상대 경로에서 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤다. 주장·태그·각주는 바꾸지 않았다.
- 2차: 9절 f8 문장 분리 — 지원 메시지 유형(오도메트리·레이저 스캔·IMU·점군은 주입 대상, 속도 명령 Twist 는 명령 조작 대상)은 README 기준 [사실][^ref-633]으로 두고, '센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하는 것으로 보인다'는 [추정][^ref-633]으로 되돌렸다.
- 2차: 3절 첫 문장 범위 정정 — '로봇 시스템을 바꾼 뒤에도 장애 상황을 여전히 처리하는지 확인하는 일은'을 '로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며'로 줄여 f6 범위에 맞췄다.
- 2차: 의견 주체 표시 — 세부영역 페이지 10절 요약 문장과 docs/topics/2026/2026-09-25-area23-s10.md 1절 세 줄 요약·3절 첫 문장을 '…받는다는 것이 구축자 의견이다. [의견][^ref-406]'으로 고쳤다.
- 2차: 벤더 주장 병기 — docs/topics/2026/2026-09-25-area23-s4.md 3절 적합성 시험 항목의 태그를 '[추정] 벤더 주장[^ref-642]'로 고쳤다.
- 2차: 약어 풀이 — 세부영역 페이지 3절에 '[다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)](../../glossary/mapf.md)', '[플릿 관리 시스템(Fleet Management System, FMS)](../../glossary/fleet-management-system.md)'를 쓰고, 9절에서 '무인운반차(Automated Guided Vehicle, AGV)', '자율이동로봇(Autonomous Mobile Robot, AMR)', '관성 측정 장치(Inertial Measurement Unit, IMU)'로 첫 등장을 풀어 썼다.
