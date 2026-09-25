# 스토리텔러 산출 2026-09-25-42

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md | draft | 영역 심화: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 10절 첫 항목 목록 기호 보정 |
| create | docs/topics/2026/2026-09-25-area17-s11.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "11. 열린 질문" 절(1,494자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area17-s8.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "8. 대표 연구와 자료" 절(1,462자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area17-s7.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,323자)을 옮겼다. 25. 안전·위험 관리 링크를 주제 페이지 기준 경로로 고침 |
| create | docs/topics/2026/2026-09-25-area17-s4.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "4. 핵심 개념과 용어" 절(1,232자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area17-s6.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "6. 대표 접근법과 기술" 절(1,226자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area17-s10.md | draft | 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(647자)을 옮겼다. 세부영역 링크를 주제 페이지 기준 경로로 고침 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 17. 로봇 간 협업·물리적 인계 | 영역 심화: 3~11절 신규 작성(인계 확인 신호·도킹 시험·스케줄 간 의존), 새 열린 질문 4건 | run 2026-09-25-42
- 홈 최근 업데이트: 2026-09-25 — 17. 로봇 간 협업·물리적 인계: 3~11절 신규 작성(Open-RMF 워크셀·VDA 5050 pick 완료 조건·도킹 시험·스케줄 간 의존, 인계 완료 판정은 이 위키의 추론)
- 대분류 최근 업데이트: 2026-09-25 — 17. 로봇 간 협업·물리적 인계: 영역 심화 초안, 물류 업종 제조사 중립 인계 규격은 미확인(oq-042)
- 세부영역 최근 업데이트: 2026-09-25 — 17. 로봇 간 협업·물리적 인계: 3~11절 신규 작성, 새 열린 질문 4건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 모바일 매니퓰레이터 | Mobile Manipulator | AMR·AGV 같은 이동 플랫폼에 로봇팔을 결합해 이동과 집기·놓기 작업을 함께 수행하는 로봇이다. | 17, 25 | ref-926 |
| new | 협동 운반 | Cooperative Object Transport | 로봇 한 대로 다루기 어려운 크거나 무거운 물체를 여러 로봇이 행동을 조율해 목적지까지 함께 옮기는 일이다. | 17 | ref-923 |
| new | 협동 인지 | Collaborative Perception | 여러 로봇이 센서 정보나 인식 결과를 공유·융합해 한 대가 볼 때보다 넓고 정확하게 환경을 파악하는 방식이다. | 17 | ref-928 |
| new | 스케줄 간 의존 | Cross-schedule Dependency (XD) | 서로 다른 로봇에 배정된 작업 사이에 선후 같은 관계가 있어, 한 로봇의 작업 적합성이 다른 로봇의 일정에 따라 달라지는 작업 의존 유형이다. | 17, 13, 14 | ref-394 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-007 | NIST | Performance of Collaborative Robot Systems | 정부·연구기관 | medium | https://www.nist.gov/programs-projects/performance-collaborative-robot-systems |
| ref-008 | NIST | ARIAC Documentation | 정부·연구기관 | high | https://pages.nist.gov/ARIAC_docs/en/latest/ |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg |
| ref-048 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md |
| ref-360 | arXiv 2508.19114 저자(미확인) | DELIVER: A System for LLM-Guided Coordinated Multi-Robot Pickup and Delivery using Voronoi-Based Relay Planning | 논문 | medium | https://arxiv.org/abs/2508.19114 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 논문 | medium | https://journals.sagepub.com/doi/10.1177/0278364913496484 |
| ref-918 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 표준 | medium | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface |
| ref-919 | PEER Group | SEMI E84: Carrier Handoff | 벤더 문서 | low | https://www.peergroup.com/definition-of-standard/semi-e84/ |
| ref-920 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 표준 | medium | https://www.astm.org/f3499-21.html |
| ref-921 | NIST | Design and Application of the Reconfigurable Mobile Manipulator Artifact (RMMA) | 정부·연구기관 | medium | https://www.nist.gov/publications/design-and-application-reconfigurable-mobile-manipulator-artifact-rmma |
| ref-922 | Bostelman, R. 외(NIST) | Mobile Robot and Mobile Manipulator Research Towards ASTM Standards Development | 논문 | medium | https://pubmed.ncbi.nlm.nih.gov/28690359/ |
| ref-923 | Tuci, E., Alkilabi, M. H. M., & Akanyeti, O. | Cooperative Object Transport in Multi-Robot Systems: A Review of the State-of-the-Art | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00059/full |
| ref-924 | Coltin, B., & Veloso, M. | Online pickup and delivery planning with transfers for mobile robots | 논문 | medium | https://www.researchgate.net/publication/289338501_Online_pickup_and_delivery_planning_with_transfers_for_mobile_robots |
| ref-925 | Zang, C. 외 | Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations | 논문 | medium | https://arxiv.org/abs/2607.17724 |
| ref-926 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 표준 | medium | https://webstore.ansi.org/standards/ria/ansia3r15082023 |
| ref-927 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 |
| ref-928 | Singh, A., Raut, G., & Choudhary, A. | Multi-agent Collaborative Perception for Robotic Fleet: A Systematic Review | 논문 | medium | https://arxiv.org/abs/2405.15777 |
| ref-929 | 다음뉴스 게재 기사(원 언론사 미확인) | 유진로봇, 지능형 제조 물류시스템 공개 | 기사 | low | https://v.daum.net/v/20251104092138920 |
| ref-930 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserResult.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇팔·워크셀의 인수 결과와 이동로봇의 적재 상태 보고가 어긋날 때(한쪽은 성공, 다른 쪽은 적재 유지) 어느 신호를 기준으로 인계 완료를 판정하는지 정한 표준이나 현장 사례가 있는가? | 17, 8 | 열림 | — |
| new | — | 반도체 업종의 SEMI E84 같은 단계별 인계 신호를 물류센터의 이동로봇–컨베이어·작업대 인계에 적용하거나 옮긴 사례가 있는가? | 17, 10 | 열림 | — |
| new | — | ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? | 17, 23 | 열림 | — |
| new | — | 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? | 17, 25 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 피킹 | 작업 대상 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 피킹 | 수행 자원 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 피킹 | 제약 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 피킹 | 완료·인계 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 피킹 | 예외·성과 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |
| 보충 | 제약 | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 17. 로봇 간 협업·물리적 인계 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface | 표준 | SEMI | 17, 10 | ref-918 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface |
| ASTM F3499-21 A-UGV 도킹 성능 시험 방법 | 표준 | ASTM International | 17, 23 | ref-920 | https://www.astm.org/f3499-21.html |
| ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 | 표준 | ANSI / A3 | 25, 17 | ref-926 | https://webstore.ansi.org/standards/ria/ansia3r15082023 |
| KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 | 표준 | 국가표준인증통합정보시스템(KSSN) | 25, 17 | ref-927 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 |
| Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) | 오픈소스 | Open Robotics (open-rmf) | 17, 10 | ref-930 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg |

## 추가 조사 요청

- 6절·11절: Open-RMF IngestorResult(ref-049)의 필드를 원본으로 대조해 하역 쪽 결과 메시지에도 화물 식별·실측 수량 필드가 없는지 확인이 필요하다(f4 는 디스펜서 쪽만 대조).
- 3절·7절·11절(oq-042): 물류 업종에서 이동로봇–컨베이어·작업대 인계 신호를 제조사 중립으로 정한 공개 규격과, SEMI E84 개별 신호 이름·순서(유료 원문)를 확인할 필요가 있다.
- 4절·8절: 협동 운반·협동 인지의 물류센터 적용 사례를 찾지 못해 개념 정의만 실었다.
- 8절: 이동로봇–로봇팔 인계 확인을 다룬 국내 학술 논문과 유진로봇 과제의 1차 출처(과제 정보)가 필요하다.
- 7절: KS B ISO 10218-2 의 판·확인 연도(KSSN 2017 확인판 항목 K001010116494 포함)와 이동식 로봇 적용 조항 확인이 필요하다.
- 8절: RMMA 2 mm 측정 불확도의 NIST 밖 독립 확인과 ref-922 발행연도 확인이 필요하다.
- 5절: 인계 실패 시 재시도·재배정·사람 확인에 따른 처리량 영향의 현장 사례가 필요하다(f25 는 추론).
- pipeline 담당: 분량 자동 분리 코드가 세부영역 절을 주제 페이지로 옮길 때 상대 링크(../<대분류>/…, 같은 대분류 파일명)를 docs/topics/YYYY/ 기준(../../categories/…)으로 다시 써야 한다. 이번 실행의 깨진 링크는 그 누락에서 생겼다.

## 이행한 수정 지시

- f23 강등·문장 수정 — 8절 국내 자료 항목을 [추정]으로 바꾸고 '과제 결과물을 공개했다고 보도되었다(2025-11-04)'로 고쳤으며 정보통신기획평가원·'추진한다'를 빼고 기사 1건 기반·1차 출처 미확인 한계를 병기했다.
- f12 표현 수정 — 6절 도킹 위치 확인에서 '관절 부하 급증'을 '모터 전류 급증(도크 접촉 감지)'으로 썼다.
- f15 조건 병기 — 8절 Zang 외 항목에 저자 보고·시뮬레이션·중간 부하 조건·고정 도크 비교안 대비·프리프린트를 함께 적었다.
- f11 병기 — 8절 RMMA 항목에 2 mm 가 NIST 보고치이며 두 출처 모두 NIST 계열이라 독립 확인이 없음을 적었다.
- f7·f8 업종 병기 — 3절·7절·9절·11절의 SEMI E84 서술마다 '반도체 업종(AMHS–생산 장비 로드포트) 규격이며 물류센터 적용 근거는 아니다'를 넣고 7절에 개별 신호 이름·순서 미확인을 적었다.
- [추정] 유지 — f4·f8·f22·f24~f29 를 쓴 모든 문장을 [추정]과 '…것으로 보인다' 표현으로 두었고 [사실]로 올리지 않았다.
- 원문 미열람 표시 — ref-007·ref-360·ref-394·ref-918~ref-929 각주 정의 끝에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-008·ref-023·ref-031·ref-044·ref-047·ref-048·ref-216·ref-930 에는 붙이지 않았다.
- 기존 각주 재사용 — ref-007 은 시드 각주 정의 줄을 그대로 쓰고(앞 지시에 따라 끝에 원문 미열람 표시만 덧붙임), 다른 기존 참고문헌은 참고문헌 색인의 기관·제목·발행일·URL·접근일로 각주 형식 줄을 만들었다.
- 인용 제한 — ref-031 은 원문 직접 인용 없이 모두 재서술했다(0회).
- f19·f20 범위 — 7절 표 아래와 9절에서 안전 표준을 25. 안전·위험 관리와 연결되는 제약으로만 서술하고 ROP 가 이행 주체가 아니라고 적었으며, f20 에 판·확인 연도와 이동식 로봇 적용 조항 미확인을 병기했다.
- 11절 연결 — oq-001·oq-006·oq-042·oq-049 를 두고 새 질문 2(SEMI E84 물류 적용)를 oq-042 바로 아래에 나란히 두었으며, 새 질문 3 은 근거를 f10·f11 로 보고 ASTM F3499·NIST RMMA 를 함께 언급했다(근거 필드는 JSON 에 넣지 않음).
- 4절 용어 — 디스펜서·인제스터는 기존 용어집 페이지(docs/glossary/dispenser-ingestor.md)에 링크만 하고 glossary_updates 에는 새 용어 4건(모바일 매니퓰레이터, 협동 운반, 협동 인지, 스케줄 간 의존)만 냈다.
- 분량 초과 자동 분리: 17. 로봇 간 협업·물리적 인계 본문 9,774자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,969자
- 형식 검증: 분리된 주제 페이지 2026-09-25-area17-s10.md·2026-09-25-area17-s7.md 의 세부영역 링크(../<대분류>/…, 20-exception-… 파일명만)를 docs/topics/2026/ 기준 ../../categories/<대분류>/<파일>.md 로 고쳤다. 세부영역 페이지 10절 첫 항목에 빠진 목록 기호 '- '를 넣었다. 주장·태그·각주는 바꾸지 않았다.
