# 스토리텔러 산출 2026-09-30-10

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | draft | seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계, 연결 16건, 열린 질문 4건), 각주 15건 |
| create | docs/topics/2026/2026-09-30-area49-s6.md | draft | 자동 분리: 49. 사람 근접 안전 의 "6. 대표 접근법과 기술" 절(1,762자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s7.md | draft | 자동 분리: 49. 사람 근접 안전 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,599자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s8.md | draft | 자동 분리: 49. 사람 근접 안전 의 "8. 대표 연구와 자료" 절(1,128자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s10.md | draft | 자동 분리: 49. 사람 근접 안전 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,041자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s4.md | draft | 자동 분리: 49. 사람 근접 안전 의 "4. 핵심 개념과 용어" 절(888자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s11.md | draft | 자동 분리: 49. 사람 근접 안전 의 "11. 열린 질문" 절(579자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area49-s3.md | draft | 자동 분리: 49. 사람 근접 안전 의 "3. 왜 중요한가" 절(545자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 49. 사람 근접 안전 | seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계), 각주 15건, 열린 질문 4건 | run 2026-09-30-10
- 홈 최근 업데이트: 2026-09-30 — 49. 사람 근접 안전: 3~11절 첫 작성(보호 분리 거리 계산, 구역별 속도 제한·진입 금지, 물류창고·병원·실외 사례, ROP 책임 경계)
- 대분류 최근 업데이트: 2026-09-30 — 49. 사람 근접 안전: seed → draft, 보호 분리 거리·구역별 속도 제한·적용 유형별 표준·인증과 물류창고·병원·실외 사례 작성
- 세부영역 최근 업데이트: 2026-09-30 — 49. 사람 근접 안전: 3~11절 첫 작성(각주 15건, 열린 질문 4건)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 속도·분리 감시 | Speed and Separation Monitoring (SSM) | 로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다. | 49, 31 | ref-1075, ref-1082 |
| new | 보호 분리 거리 | Protective Separation Distance | 사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다. | 49 | ref-1075 |
| new | 동력·힘 제한 | Power and Force Limiting (PFL) | 로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다. | 49, 31 | ref-1082 |
| new | 움직임 지도 | Maps of Dynamics (MoD) | 과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다. | 49, 19, 25 | ref-1087 |
| new | 제어 장벽 함수 | Control Barrier Function (CBF) | 로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다. | 49, 27 | ref-1086 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 논문 | medium | https://arxiv.org/abs/2602.17822 |
| ref-470 | ISO (ISO/TC 110) | ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-1078 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 오픈소스 문서 | high | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md |
| ref-031 | VDA / VDMA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 정부·연구기관 | high | https://www.kiria.org/portal/cert/portalCertEstiSafe.do |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준) | 기사 | medium | https://zdnet.co.kr/view/?no=20230728173101 |
| ref-1082 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 기사 | low | https://zdnet.co.kr/view/?no=20240305160245 |
| ref-1083 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 논문 | medium | https://arxiv.org/abs/2306.16740 |
| ref-1084 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 벤더 문서 | medium | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order |
| ref-1085 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ |
| ref-1086 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 논문 | medium | https://arxiv.org/abs/2503.21141 |
| ref-1087 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 논문 | medium | https://arxiv.org/abs/2508.19731 |
| ref-1088 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 기사 | low | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ |
| ref-1089 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 논문 | medium | https://arxiv.org/abs/2604.13677 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? | 49, 48 | 열림 | — |
| new | — | 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? | 49, 50 | 열림 | — |
| new | — | 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? | 49, 59 | 열림 | — |
| new | — | 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? | 49, 21 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 시작 조건 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 물류창고 | 작업 대상 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 물류창고 | 수행 자원 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 물류창고 | 제약 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 병원 | 작업 대상 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 병원 | 수행 자원 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 병원 | 제약 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 병원 | 예외·성과 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 실외 | 시작 조건 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 실외 | 작업 대상 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 실외 | 수행 자원 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 실외 | 제약 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |
| 실외 | 예외·성과 | docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시 | 49. 사람 근접 안전 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Nav2 Collision Monitor (nav2_collision_monitor) | 오픈소스 | Open Navigation (ros-navigation/navigation2) | 49, 27 | ref-1078 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md |

## 추가 조사 요청

- 7절·3절: 산업안전보건기준에 관한 규칙 제223조 조문 원문(국가법령정보센터)을 열어 울타리 기본 요구·안전매트 요구 범위·면제 요건을 확인해야 한다. 이번 본문은 기사(ref-1082) 전달 수준의 [추정]으로만 썼다. 기존 참고문헌 ref-562 가 같은 조문을 가리키는지도 함께 확인이 필요하다.
- 4절·7절: ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s 제한, 시험편 치수를 표준 원문 또는 공식 해설로 확인해야 한다(ref-470 원문 미열람, 기존 참고문헌 ref-470 과 같은 표준).
- 5절: 제조 공장·상업 시설·가정·기타 현장에서 사람 근접 감속·정지·양보를 적용한 실제 도입 사례(속도·거리 값 포함)가 없다. 물류창고 사례도 벤더 주장뿐이라 독립 출처와 완료·인계·예외·성과 칸의 근거가 필요하다.
- 7절·11절: 실외이동로봇 운행안전인증의 현행 심사 항목 목록과 질량별 속도 구간이 현행 기준에 들어갔는지(2023-07 개정안 이후) 확인해야 한다.
- 7절: ISO 13482(개인 돌봄 로봇)와 ISO 13855 원문의 사람 근접 관련 요구가 이번 브리프에 없어 넣지 못했다.
- 운영 참고: 참고문헌 id ref-1075~ref-1089 가 이전 브리프 2026-09-30-08 과 충돌하고 VDA 5050·ISO 3691-4·KIRIA 인증 페이지가 기존 참고문헌과 같은 URL 일 가능성이 있어 퍼블리셔의 id 충돌·병합 확인이 필요하다(1차 검증 지적).

## 이행한 수정 지시

- f5 [사실]→[추정] 강등·귀속·울타리 문구 축소 — 3절과 7절 표 '산업안전보건기준에 관한 규칙 제223조' 행을 '지디넷코리아 기사(2024-03-09)에 따르면 … 높이 1.8미터 이상 울타리 설치를 기본으로 하되 일정 안전기준을 충족하면 면제될 수 있다(법령 원문 미확인). [추정]'으로 쓰고 안전매트·협동로봇 한정 면제·2016년 표현을 넣지 않았다.
- f5 협동 방식 분리 — 7절 표에서 SSM·HGC·PFL 을 제223조의 내용이 아니라 기사가 소개한 국제 기준(ISO/TS 15066 계열)의 협동 방식으로 별도 문장에 썼고, 4절 동력·힘 제한 항목도 같은 귀속으로 [추정] 표기했다.
- ref-1082 발행일 — 13절 각주 정의와 reference_updates 의 published 를 2024-03-09 로 고쳤다.
- f2 표현 수정 — 6절에 'ISO 13855 가 사람 속도로 최대 2,000 mm/s 를 쓰고 분리 거리가 500 mm 보다 크면 1,600 mm/s 를 선택할 수 있다', 침입 거리는 센서 구성·접근 방향에 따라 850 mm·1,200 mm 처럼 달라지는 값, 반응 시간 약 0.113초는 '레일 장착 6자유도 매니퓰레이터'의 측정값으로 썼다.
- f3 표현 완화 — 6절에서 '제동 거리와 반응 시간이 보호 거리에 크게 영향을 준다'로 썼다.
- f6·f7 원문 미확인 표시 — 4절 운용 구역과 7절 ISO 3691-4 행을 [추정]으로 두고 '표준 원문 미확인, 검색 요약 기준'을 밝혔으며, ref-470 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-470 에 source_unopened: true 를 넣었다.
- f8 수정 — 7절 ANSI/A3 R15.08-2 행에서 '잔여 위험'을 빼고 'The Robot Report(2023-10-26)가 전했다'는 귀속과 '표준 본문은 유료라 열람하지 못했다'를 유지했다.
- f10 개정안 표기와 출처 충돌 — 5절 실외 사례 제약 칸에서 질량별 속도 구간·횡단보도 대기를 '2023-07-28 기사가 전한 당시 개정안 기준'으로 쓰고, 심사 항목 수를 인증기관 페이지(8개 항목)와 기사(16가지)로 함께 제시해 한쪽을 고르지 않은 채 11절 두 번째 열린 질문과 연결했다.
- f13 한정 — 6절·7절에서 'README 는 이 기능이 하드 실시간 안전 인증을 제공하지 않는다고 밝힌다'로만 썼고, '안전 등급 하드웨어를 대신하지 않는다'는 표현은 쓰지 않았다(9절의 보조 계층 판단은 f22 의 [추정]으로 분리).
- f14 벤더 주장 병기 — 5절 물류창고 사례 표·서술과 6절에서 모두 '[추정] 벤더 주장'으로 쓰고 발행일을 '미확인'으로 적었다(각주 발행일도 미확인).
- f17 수정 — 5절 병원 사례에서 '최고 속도에서 방향 오차가 커졌고 정확도는 중간 속도에서 가장 높았다'로 고치고, 실제 병원이 아닌 모의 병원 환경의 시뮬레이션 평가임을 사례 제목과 서술에 밝혔다.
- f18 표시 — 5절 물류창고 서술에서 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가임을 밝히고 정량 결과를 '미확인'으로 두었으며, 사례 표 칸에는 넣지 않았다(6절·8절도 정량 결과 미확인 표기).
- f19 '최대' 추가 — 6절과 8절에서 '최대 26%', '최대 19%'로 썼다.
- f15 학술지판 병기 — ref-1083 각주에 학술지판(ACM Transactions on Human-Robot Interaction 14(2), 2025-02)을 병기하고 발행일은 arXiv 제출일 2023-06-29 를 유지했다.
- 7절 범위 한정 — 표를 사람 근접 안전과 관련된 구역·속도·감지·정지 항목으로 한정해 요약하고, 절 첫머리에서 표준 상세를 '50. 안전 표준·인증·사고 조사' 페이지로 연결했다.
- 9절 경계 — 표의 '외부와 연계하는 것' 칸에 Nav2 Collision Monitor(f13)와 안전 등급 인력 감지·보호 정지·SSM·PFL·울타리(f1~f3·f5~f7)를 '연계 대상:'으로 썼고, 표 아래에 실외 인증 대상이 로봇과 관제장치의 조합이라 ROP 범위와 겹칠 수 있는 경계임(f9)과 운영 사업자 몫이라는 판단이 추론임을 밝혔다.
- 분량 초과 자동 분리: 49. 사람 근접 안전 본문 10,522자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,209자
