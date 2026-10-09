# 스토리텔러 산출 2026-10-09-02

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/index.md | draft | '다른 대분류와의 연결' 절 신규 작성(A~Q 가운데 15개 대분류와의 연결, 연결 도식, 아직 다루지 않은 연결), 페이지 끝 '참고 자료' 절 신설과 각주 정의 35건, 프런트매터 category·sources 추가. 2차 수정: 66. 실외 줄에 추정 태그·각주, f33 의 '벤더 주장'을 태그 앞으로 이동 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | D. 공간·지도 모델 | 다른 대분류와의 연결 절 신규 작성(A·B·C·E·F·G·H·I·J·K·L·M·O·P·Q 대분류와의 연결, 아직 다루지 않은 연결 명시), 참고 자료 절 신설과 각주 정의 | run 2026-10-09-02
- 홈 최근 업데이트: 2026-10-09 — D. 공간·지도 모델: 다른 대분류와의 연결 절 신규 작성(14·15·16 세부영역의 지도·좌표·장소 이름이 15개 대분류로 이어지는 연결, N. 보안·개인정보 등은 근거 없음으로 표시)
- 대분류 최근 업데이트: 2026-10-09 — D. 공간·지도 모델: 다른 대분류와의 연결 절 신규 작성(연결마다 단일 출처, 교차 확인 0건)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 위치추정 품질 점수 | Localization Score (VDA 5050 localizationScore) | 로봇이 보고하는 0.0(최저)~1.0(최고)의 위치추정 신뢰 값으로, VDA 5050 3.0.0 은 이를 편차 범위(deviationRange)와 함께 기록·시각화 용도로만 둔다. | 15, 18, 38 | ref-031 |
| new | 지도 배포 | Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap) | 관제가 즉시 동작으로 로봇에게 지도 서버에서 특정 판의 지도를 내려받게 하고, 활성화·삭제를 지시해 로봇마다 올바른 지도 판이 쓰이게 하는 절차다. | 16, 43, 57 | ref-031 |
| new | 무결성 위험 | Integrity Risk | 항공 항법에서 위치 추정 결과를 얼마나 믿을 수 있는지 정량화하는 데 쓰던 성능 지표로, 이동로봇의 SLAM 기반 위치추정 안전성을 평가하는 데도 적용된다. | 15, 48 | ref-161 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 논문 | high | https://arxiv.org/abs/2404.05050 |
| ref-721 | ISO | ISO 18646-2:2024 Robotics — Performance criteria and related test methods for service robots — Part 2: Navigation | 표준 | medium | https://www.iso.org/standard/82643.html |
| ref-1271 | Xie, F., & Schwertfeger, S. (ROBIO 2024, arXiv) | Empowering Robot Path Planning with Large Language Models: osmAG Map Topology & Hierarchy Comprehension with LLMs | 논문 | medium | https://arxiv.org/abs/2403.08228 |
| ref-1272 | Byers, G., & RazaviAlavi, S. (Northumbria University), 2022 Modular and Offsite Construction Summit | Layout Modelling of the Built Environment for Autonomous Mobile Robots Using Building Information Modelling (BIM) and Simulation | 논문 | medium | https://researchportal.northumbria.ac.uk/en/publications/layout-modelling-of-the-built-environment-for-autonomous-mobile-r/ |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README (web-based interface to visualize and control Open-RMF deployments) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-154 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/location_2D.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/location_2D.json |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 표준 | high | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl |
| ref-1018 | Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv) | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning | 논문 | medium | https://arxiv.org/abs/2507.12753 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 논문 | medium | https://arxiv.org/abs/2409.12842 |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 논문 | medium | https://journals.sagepub.com/doi/10.1177/02783649241287797 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부만 확인) | 기사 | low | https://zdnet.co.kr/view/?no=20230728173101 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 의 지도 배포(downloadMap·enableMap·deleteMap)로 로봇마다 활성화된 지도 판과 Open-RMF 빌딩 맵·LIF 레이아웃의 판을 ROP 한 곳에서 대응시켜 관리하는 공개 구현이나 운영 절차가 있는가? | 16, 43, 57 | 열림 | — |
| new | — | 시간대별 사람 흐름을 담은 움직임 지도(maps of dynamics)를 ROP 의 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? | 16, 19, 27 | 열림 | — |
| new | — | 비전 언어 모델의 평면도 해석이 큰 개방 구역에서 성능이 떨어진다는 보고가 물류창고·제조 공장처럼 넓은 개방 구역이 많은 비주거 시설 도면에서 어떤 오류로 나타나는가? | 14, 45, 61 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- ref-1171 각주: 참고문헌 페이지 docs/references/ref-1171.md 의 '각주 형식' 줄이 입력에 없어 브리프의 ref-1270 서지(Aalto 연구 포털 URL)로 각주 정의를 만들었다. 퍼블리셔가 ref-1171 페이지의 줄과 다르면 그 줄로 바꾸도록 확인이 필요하다.
- D. 공간·지도 모델 대분류 시드 페이지에 '참고 자료' 절이 없어, 이번에는 '최근 업데이트' 절 끝(auto 마커 밖)에 append 패치로 '## 참고 자료' 절을 새로 만들었다. 패치 적용기가 없는 절을 새로 만드는 방식(section 미존재 시 끝에 추가)을 지원하도록, 그리고 다른 대분류 시드에도 '참고 자료' 절이 있는지 pipeline·시드 담당의 확인이 필요하다.
- N. 보안·개인정보(51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터)와 D. 공간·지도 모델을 잇는 근거: 건물 지도·장소 목록의 접근 통제, 로봇 지도에 담기는 개인정보를 다룬 학술·기관 자료가 '다른 대분류와의 연결' 절에 필요하다(RO-MAN 2023 로봇 지도 개인정보 논문 본문 확인 포함).
- Q. 현장 유형별 적용의 61. 물류창고, 62. 제조 공장, 64. 상업 시설에서 도면·지도 정합이나 장소 목록·지도 판 관리를 다룬 현장 사례가 연결 절의 Q 항목에 필요하다(현장 유형을 밝힌 출처).
- B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동·7. 온톨로지 검증·변경 관리와 장소·지도 표현(IndoorGML·BOT 등)을 잇는 근거, 40. 운영 절차·요청 창구의 임시 통제 구역 운영 절차(oq-203), 58. 다사업자 책임·계약·데이터의 지도 데이터 권리(oq-281)가 연결 절에 필요하다.
- ISO 21423 은 2026-10 발행 예정이므로 다음 월간 재검증에서 발행 여부와 공통 좌표계 내용(oq-027)을 다시 확인해야 한다.
- ref-1214·ref-721·ref-1271·ref-1272·ref-302 의 id 가 보류된 실행 2026-09-30-24 의 번호와 겹친다는 1·2차 검증 지적이 있으므로 퍼블리셔의 번호·URL 병합 확인이 필요하다(특히 ref-302·ref-721 은 기존 번호 범위 안).

## 이행한 수정 지시

- page_proposals 절 제목 — patches 의 section 을 번호 없는 '다른 대분류와의 연결'로 썼다.
- 참고 자료 — 페이지 끝(최근 업데이트 절 뒤)에 '## 참고 자료' 절을 새로 만들어 각주 정의 35건을 그 절로 옮겼다. 현재 페이지에 없는 절이라 '최근 업데이트' 절에 append 패치(auto 마커 끝 뒤에 덧붙임)로 넣었고, 마커 사이 내용과 그 밖의 절은 바꾸지 않았다. 연결 절 끝에는 각주가 참고 자료 절에 있다는 한 줄만 남겼다.
- 대분류 표기 — 연결 절의 소제목·링크 텍스트·도식을 새 17개 대분류의 문자와 이름, 세부영역 번호+이름으로 썼고 옛 대분류 이름은 쓰지 않았다.
- f13·f14 — E. 사물·사람·실시간 상태 항목의 두 문장 각주를 ref-1171 로 썼고 reference_updates 에 ref-1270 을 넣지 않았다(ref-1171 페이지의 각주 줄이 입력에 없어 브리프 서지로 정의를 만들고 추가 조사 요청에 적었다).
- ref-1214 — reference_updates 에 기관·제목·발행일 2024-04-07·URL·접근일 2026-10-09 를 모두 채운 새 항목으로 냈고 각주 정의도 두었다.
- f21 — F. 연동 항목에서 IfcTransportElement 정의를 [사실] 문장(개발 브랜치 ifc4.3-main·ADD2 문구 차이 단서 유지)으로, 공용 자원 후보 입력이라는 활용을 별도 [추정] 문장으로 나눴다.
- f35 — K. 플랫폼 아키텍처·인프라 항목을 'location_2D 스키마를 쓰는 위치에는 지도 이름이 필수로 붙는다'로 좁혔다.
- f18 — IEEE 1873-2015 를 현행 표준으로 단정하지 않고 이후 상태를 열린 질문 oq-202 로 연결해 같은 문장에 적었으며, ref-1016·ref-1019 각주는 참고문헌 목록의 서지와 이전 접근일(2026-09-30)로 썼다.
- f16 — ISO 21423 의 단계 60.00(2026-07-21)·발행 예정 2026-10 을 '확인일 2026-10-09 기준'과 함께 쓰고 공통 좌표계 내용은 미확인(oq-027)으로 두었다.
- f17 — LIF 판·날짜를 README 기준 1.0.0(2023-09)으로만 쓰고 VDMA 2024-03 인용과의 출처 충돌(oq-025·oq-078·oq-200)을 한쪽으로 정하지 않고 함께 밝혔다.
- f24 — G. 계획·최적화 항목의 충전소 속성 문장 뒤에 출처 충돌 oq-069(is_parking_spot 대 is_charger)를 함께 적었다.
- f45 — '2023-07 입법예고안 기준 보도'임과 2023-07-28 기준일을 문장에 유지하고 현행·확정 기준과 다를 수 있다고 적었다.
- f33 — J. 현장 운영·관제 항목을 '[추정] 벤더 주장' 으로 표기하고 독립 확인이 없음을 문장에 남겼다.
- f40·f48·f2 — SLAM 위치추정 안전성(M. 안전 항목의 '연계 대상' 표시), 청소 로봇의 의미 지도 갱신(Q 항목에서 연계 대상 명시), BIM 기반 위치 추정(A 항목에서 '로봇 자체 지능·제어' 경계의 연계 대상 명시)을 ROP 직접 범위로 쓰지 않았다.
- f12·f29~f31 — 18. 실시간 세계 상태·데이터 일관성 연결은 E 항목에 현재 상태 표현으로, 34·35·36 연결은 I 항목 머리에 가정한 미래를 실험하는 쪽이라고 밝혀 나눠 썼다.
- f38·f37 — f38 은 L 항목에 45. 문서·도면·장면 이해와 14. 도면·BIM에서 지도 만들기를 함께 적었고(원문 13장 교차 규칙 명시), f37 은 44. 로봇 기반 모델·언어 모델 계획과 16. 장소 의미·지도 관리 양쪽을 한 줄에 연결했다.
- 각주 — fetched: false 인 출처는 참고문헌 목록의 서지와 이전 접근일로 각주를 썼고, 원문을 연 적 없는 ref-162·ref-063·ref-071 에는 접근일 뒤 ' (원문 미열람)'을 붙였으며 이 출처들은 reference_updates 에 넣지 않았다.
- open_questions_new — 세 질문을 형식대로 open_question_updates 에 new 로 등록하고, 연결 절의 O 항목에서 첫 질문과 oq-201 의 관계를, L 항목에서 셋째 질문과 oq-196 의 관계를 밝혔다.
- 아직 다루지 않은 연결 — N. 보안·개인정보(51·52·53), 40. 운영 절차·요청 창구(oq-203), 58. 다사업자 책임·계약·데이터(oq-281) 등을 근거 없음으로만 적고 내용을 추정해 채우지 않았다.
- 형식 검증 재작성 — H2 순서를 템플릿(핵심 질문 … 최근 업데이트, 참고 자료)과 맞추기 위해 '## 참고 자료' 절을 페이지 끝에 두고 각주 정의를 연결 절에서 그 절로 옮겼다. 주장·태그·각주 참조는 바꾸지 않았다.
- 2차: Q. 현장 유형별 적용의 66. 실외 줄 — 방법 (가)를 택해 '…장소 목록에 들어갈 속성 요구가 될 것으로 보인다. [추정][^ref-992][^ref-1214]'로 고쳐 f47 과 같은 태그·각주를 붙였다.
- 2차: J. 현장 운영·관제의 f33 문장 — '벤더 주장'을 태그 앞 문장 안으로 옮겨 '…2026-08-24 발표했으며(벤더 주장), 독립 확인은 없다. [추정][^ref-817]'로 고쳤다. 태그·각주·벤더 주장 병기는 유지했다.
- 2차: 위 두 줄 말고는 patches 본문·참고 자료 절·reference_updates·glossary_updates·open_question_updates 를 바꾸지 않았다(diff_summary 에 2차 수정 2건만 덧붙였다).
