# 스토리텔러 산출 2026-09-25-63

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md | draft | seed → draft: 3~11절 첫 작성(표준 책임 분담, 정지·재개·비상 대응, STPA, SafeGate 트랙 반영), 페이지 상태 자동 영역 추가, 각주 11건(3·6·7·8·11절 상세는 주제 페이지로 분리). 2차: 9절 마지막 문장 어미를 추정형으로 수정 |
| create | docs/topics/2026/2026-09-25-area25-s6.md | draft | 자동 분리: 25. 안전·위험 관리 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '운영 조율 수단' 문장을 [사실]·[추정] 두 문장으로 나눴다 |
| create | docs/topics/2026/2026-09-25-area25-s7.md | draft | 자동 분리: 25. 안전·위험 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: VDA 5050 행의 관계 칸을 [사실]·[추정]으로 나눴다 |
| create | docs/topics/2026/2026-09-25-area25-s11.md | draft | 자동 분리: 25. 안전·위험 관리 의 "11. 열린 질문" 절(910자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area25-s8.md | draft | 자동 분리: 25. 안전·위험 관리 의 "8. 대표 연구와 자료" 절(767자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area25-s3.md | draft | 자동 분리: 25. 안전·위험 관리 의 "3. 왜 중요한가" 절(694자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 25. 안전·위험 관리 | 영역 심화: 3~11절 첫 작성(표준별 책임 분담, 정지·재개·비상 대응, STPA 위험 분석, SafeGate 트랙 반영) | run 2026-09-25-63
- 홈 최근 업데이트: 2026-09-25 — 25. 안전·위험 관리: 3~11절 첫 작성(차량·통합 안전 표준, VDA 5050·Open-RMF 정지·재개·비상 대응, STPA, SafeGate)
- 대분류 최근 업데이트: 2026-09-25 — 25. 안전·위험 관리: 영역 심화 초안(3~11절), 새 열린 질문 3건
- 세부영역 최근 업데이트: 2026-09-25 — 25. 안전·위험 관리: 3~11절 첫 작성, 피킹·출하 시나리오와 ROP 직접·연계 경계 정리

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 위험성평가 | Risk Assessment (ISO 12100) | 위험원을 찾고 위험을 추정·평가해 위험 감소가 필요한지 판단하는 절차로, ISO 12100 이 기계 설계의 일반 원칙으로 정한다. | 25 | ref-579 |
| new | 3단계 위험 감소 방법 | Three-Step Method (ISO 12100) | 본질적 안전 설계, 방호·보완 보호 조치, 사용 정보의 순서로 앞 단계를 다한 뒤 다음 단계로 가며 위험을 줄이는 ISO 12100 의 우선순위 원칙이다. | 25 | ref-579 |
| new | 운용 구역 | Operating Zone (ISO 3691-4) | 무인 산업 차량이 운행하는 구역으로, ISO 3691-4 는 구역 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. | 25 | ref-470 |
| new | 시스템 이론적 프로세스 분석 | System-Theoretic Process Analysis (STPA) | 제어 구조를 기준으로 구성요소 사이의 안전하지 않은 제어 상호작용에서 위험 시나리오와 원인 요인을 찾는 위험 분석 기법이다. | 25, 15 | ref-577, ref-578 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-472 | Association for Advancing Automation (A3) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 표준 | medium | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available |
| ref-572 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 표준 | medium | https://www.iso.org/standard/73934.html |
| ref-573 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 정부·연구기관 | medium | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 |
| ref-574 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 정부·연구기관 | medium | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 |
| ref-417 | Obi, I. 외(arXiv) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-576 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 논문 | medium | https://arxiv.org/abs/2502.20693 |
| ref-577 | Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회) | 논문 | medium | https://ieeexplore.ieee.org/document/8910126/ |
| ref-578 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 |
| ref-579 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 표준 | medium | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 |
| ref-580 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf/issues/658 |
| ref-581 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 (2022-10-12 확인판 있음) | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? | 25, 12 | 열림 | — |
| new | — | 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? | 25, 28 | 열림 | — |
| new | — | 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? | 25, 18 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 피킹 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 피킹 | 제약 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 피킹 | 완료·인계 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 피킹 | 예외·성과 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 출하 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 출하 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 출하 | 제약 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |
| 출하 | 예외·성과 | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 25. 안전·위험 관리 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 | 표준 | ISO (CEN EN ISO 12100:2010) | 25 | ref-579 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 |
| KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 | 표준 | 국가기술표준원(KSSN) | 25, 18 | ref-581 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 |

## 추가 조사 요청

- 11절 oq-070: 이동식 협동로봇 안전기준 KS 의 표준 번호와 ISO 10218-2:2025·ISO 3691-4:2023 대응 관계 — 정부 발표에 번호가 없어 7절 표에 '미확인'으로 두었다.
- 11절 oq-064: R15.08-2 유형 C(모바일 매니퓰레이터) 대응 국내 KS·인증 기준 — 이번 실행에서 확인하지 못했다.
- 5·7절: Open-RMF 이슈 #658 이후 rmf_fleet_adapter 에 플릿 이름별 화재경보 분리 옵션이 구현됐는지 공식 저장소 원문(변경 이력)으로 확인 필요 — 현재 '이슈 작성 시점 기준, 이후 미확인'으로만 썼다.
- 4·6·7절: VDA 5050 3.0.0 state.schema 의 비상정지 필드(activeEmergencyStop)와 operatingMode 전체 값 목록을 새 finding 으로 정리하면 강등된 f2 를 원문 기준 [사실]로 다시 쓸 수 있다.
- 3·9절: ISO 3691-4 의 제조사–통합자–사용자 책임 분담을 1차 자료로 확인 필요 — 2차 해설뿐이라 브리프에서 빠졌다. R15.08-1(로봇 자체 요구) 출처도 따로 필요하다.
- 5절: 출하 단계 시나리오의 작업 대상(출하 대기 화물·운반구)과 완료·인계 조건에 대한 근거 finding 이 없어 '해당 없음'으로 두었다.

## 이행한 수정 지시

- f2 강등·eStop 필드 열거 삭제 — 4·6절과 5절 표에서 f2 를 [추정]으로 쓰고 'eStop: AUTOACK·MANUAL·REMOTE·NONE' 을 빼고 '안전 상태(safetyState)로 비상정지 상태와 보호 필드 침범 여부(fieldViolation)를 보고한다'로만 썼다.
- f2 operatingMode 표기 — 6절에 '자동(AUTOMATIC)·수동(MANUAL) 등의 운용 모드(operatingMode)'로 썼고, 9절도 값 열거 없이 '운용 모드'로 썼다.
- open_questions_new 첫 항목 — 11절과 open_question_updates 에서 'VDA 5050 eStop REMOTE' 를 'VDA 5050 의 원격(REMOTE) 비상정지'로 고쳤다.
- f12 강등·축약 — 6절과 8절에서 [추정]으로 쓰고 '관련 표준·방법론을 검토해 건설 현장 이동 로봇 배치용 위험성평가를 제안하고 현장 전문가 검증을 거쳤다고 저자가 보고한다'로 줄였다(정량 지표·ISO/TS 15066·R15.08 검토 표현 삭제).
- f10 defer 삭제 — 6절에서 '사람에게 확인 요청'을 빼고 '실행을 승인 또는 거부'로 썼으며, ISO 13482 는 개인 돌봄 로봇 표준·저자 보고 평가·물류 현장 대상 아님 병기는 유지했다.
- f7 '로봇 응용 강조' 삭제·용어 통일 — 4·7절에서 해당 부분을 지우고 '협동 운전 요구'를 용어집 표기 '협동 적용'(링크 포함)으로 바꿨다.
- f4·f20 시점 한정 — 5절 제약 칸과 reference 요약에 '이슈 작성 시점(2025-04-04) 기준'으로 한정하고 이후 구현 여부는 미확인으로 두었다.
- f13·f14 대상 병기 — 6절과 8절에 두 연구의 대상이 화학 분석 실험실의 다중 로봇이며 물류 현장이 아님을 적고 방법론 근거로만 썼다.
- ref-417 — 각주와 reference_updates 의 기관을 'Obi, I. 외(arXiv)', 발행일을 2026-04 로 썼다.
- ref-577 — 각주와 reference_updates 의 기관을 'Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore)', 발행일을 2018-12 로 쓰고 제목 뒤에 '(EECS 2018 학회)'를 붙였다.
- ref-580 — 각주와 reference_updates 의 발행일을 2025-04-04 로 고쳤다.
- ref-581 — 발행일을 2017-02-28 로 고치고 각주 제목 뒤 괄호에 '2022-10-12 확인판 있음'을 적었으며, 7절 표에서 ISO/TS 15066 내용이 ISO 10218-2:2025 에 통합됐다는 f7 과 함께(ref-581·ref-572 각주) 제시했다.
- 원문 미열람 표시 — ref-470~ref-581 12건 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-031·ref-004 에는 붙이지 않았다.
- 10절 24번 연결 — 24. 자산·소프트웨어 수명주기 관리 항목을 태그·각주 없이 링크와 연결 문장(11절 oq-092·oq-093 안내)으로만 썼다.
- SafeGate 교차 연결 — f10 내용을 6절에 두고 같은 소제목에 27. AI·학습·적응과 모델 운영 링크를 걸었으며 10절에도 27번과 18번 연결을 두었다.
- 11절 oq-064·oq-070 — 해결로 바꾸지 않고 '열림'으로 유지했으며 open_question_updates 에도 상태 변경을 내지 않았다.
- 분량 초과 자동 분리: 25. 안전·위험 관리 본문 7,080자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,728자
- 형식 재작성(퍼블리셔 4단계 링크 검사) — docs/topics/2026/2026-09-25-area25-s6.md 3절의 27. AI·학습·적응과 모델 운영 링크를 이 페이지 위치 기준 경로 ../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md 로 고쳤다. 아울러 세부영역 페이지 프런트매터 sources 를 13절 각주 정의에 있는 11건으로 맞췄다(ref-574·ref-578·ref-581 은 분리된 주제 페이지에만 있다). 주장·태그·각주 내용은 바꾸지 않았다.
- 2차: 6절 '운영 조율 수단' 문장 분리 — docs/topics/2026/2026-09-25-area25-s6.md 3절 '상호운용 규격의 정지·재개 메시지'에서 '이 규격은 안전 표준이 아니다. [사실][^ref-031]'과 '따라서 이 메시지는 운영 조율 수단으로 보인다. [추정][^ref-031]' 두 문장으로 나눴다.
- 2차: 7절 VDA 5050 행 태그 분리 — docs/topics/2026/2026-09-25-area25-s7.md 3절 표의 VDA 5050 3.0.0 행 '이 영역과의 관계' 칸을 '안전 요구를 정의하지 않는 상호운용 규격이다. [사실] 안전 상태 보고와 정지·재개 동작을 담는다. [추정]'으로 고쳤다.
- 2차: 9절 단정형 어미 수정 — 세부영역 페이지 9절 마지막 문장을 '… 그 상태와 결과를 받는 쪽에 설 수 있는 것으로 보인다'로 고쳤다([추정] 태그·각주 유지).
