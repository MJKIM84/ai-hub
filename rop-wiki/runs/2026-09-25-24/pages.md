# 스토리텔러 산출 2026-09-25-24

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md | draft | 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 각주 22건, 1차 조건부 승인 수정 14건 이행 |
| create | docs/topics/2026/2026-09-25-area08-s7.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,454자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s4.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "4. 핵심 개념과 용어" 절(1,436자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s6.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "6. 대표 접근법과 기술" 절(1,386자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s8.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "8. 대표 연구와 자료" 절(1,250자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s10.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,091자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s11.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "11. 열린 질문" 절(1,060자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s3.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "3. 왜 중요한가" 절(694자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 8. 실시간 세계 상태·데이터 일관성 | 영역 심화: 섹션 3~11 신규 작성(허용 경과 시간·두 시각·품질·정정 이벤트, 22. 시뮬레이션·예측용 디지털 트윈과의 구분), 1차 조건부 승인 수정 14건 이행 | run 2026-09-25-24
- 홈 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 영역 심화로 섹션 3~11 작성. 표준은 시각·품질 장치만 주고 대상별 허용 경과 시간은 정하지 않는다는 점을 정리(신뢰도 low)
- 대분류 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 영역 심화로 섹션 3~11 작성, 22. 시뮬레이션·예측용 디지털 트윈과의 구분 근거와 열린 질문 4건 추가
- 세부영역 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 섹션 3~11 신규 작성(VDA 5050·Open-RMF·ROS 2 QoS·Sparkplug·OPC UA·EPCIS·SOSA·ISO 23247 비교, 입고 → 적치·보충 시나리오)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 정보 나이 | Age of Information (AoI) | 수신 측이 가진 최신 상태 갱신이 생성된 뒤 흐른 시간으로, 받은 정보가 얼마나 최신인지를 재는 지표이다. | 8, 11 | ref-385 |
| new | 디지털 섀도 | Digital Shadow | 물리 대상의 상태가 디지털 표현으로 한 방향 자동 흐름으로만 반영되는 단계의 디지털 표현으로, 디지털 모델·디지털 트윈과 구분된다(Kritzinger 외(2018) 분류 기준). | 8, 22 | ref-387 |
| new | 무충돌 복제 데이터 타입 | Conflict-free Replicated Data Type (CRDT) | 여러 복제본을 조율 없이 수정해도 같은 갱신을 받으면 정해진 규칙으로 같은 상태에 수렴하도록 설계된 데이터 타입이다. | 8, 11 | ref-391 |
| new | 오류 선언 | Error Declaration (EPCIS errorDeclaration) | 앞선 EPCIS 이벤트의 내용이 틀렸음을 선언 시각·사유·정정 이벤트 id 와 함께 기록해 원 기록을 지우지 않고 바로잡게 하는 EPCIS 요소이다. | 8, 7 | ref-045, ref-044 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 표준 | medium | https://www.w3.org/TR/vocab-ssn/ |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 표준 | high | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-378 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 오픈소스 문서 | high | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| ref-379 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-380 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_lifts.html |
| ref-381 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg |
| ref-382 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-383 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 표준 | high | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| ref-384 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 표준 | medium | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 |
| ref-385 | Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. | Age of Information: An Introduction and Survey | 논문 | medium | https://arxiv.org/abs/2007.08564 |
| ref-386 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 정부·연구기관 | medium | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 |
| ref-387 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2405896318316021 |
| ref-388 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 논문 | medium | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 |
| ref-389 | Massawe, L. V. 외(Sensors) | Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach | 논문 | medium | https://doi.org/10.3390/s120404187 |
| ref-390 | 이동건, 송승현, 이찬혁, 노상도, 윤상문, 이현영(한국CDE학회 논문집) | 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002781294 |
| ref-391 | Preguiça, N., Baquero, C., & Shapiro, M. | Conflict-free Replicated Data Types (CRDTs) | 논문 | medium | https://arxiv.org/abs/1805.06358 |
| ref-392 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? | 8, 10 | 열림 | — |
| new | — | 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? | 8, 9, 11 | 열림 | — |
| new | — | 로봇이 보고한 적재물 식별·판독 결과와 WMS 재고 기록이 어긋날 때 어느 쪽을 기준으로 삼고 정정 기록을 누가 발행하는가(국내 물류센터 사례 포함)? | 8, 7 | 열림 | — |
| new | — | 출처 충돌: 김지형(2023) 'OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현'의 게재 학술지를 한 검색 요약은 지능정보논문지로, KoreaScience 는 한국인터넷방송통신학회논문지(DOI 10.7236/JIIBC.2023.23.4.189)로 적는다. 어느 쪽이 맞는가? | 8 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 입고 | 시작 조건 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 입고 | 작업 대상 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 입고 | 수행 자원 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 입고 | 제약 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 입고 | 완료·인계 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 입고 | 예외·성과 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 시작 조건 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 작업 대상 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 수행 자원 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 제약 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 완료·인계 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 적치 | 예외·성과 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 보충 | 시작 조건 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 보충 | 작업 대상 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 보충 | 수행 자원 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 보충 | 완료·인계 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |
| 보충 | 예외·성과 | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 8. 실시간 세계 상태·데이터 일관성 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) | 오픈소스 | Open Robotics (ROS 2 Documentation) | 8, 11 | ref-378 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| Eclipse Sparkplug (Chapter 5 Operational Behavior) | 표준 | Eclipse Foundation | 8, 11, 19 | ref-383 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| OPC UA Part 4: Services (7.11 DataValue) | 표준 | OPC Foundation | 8, 11 | ref-384 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 |
| ISO 23247 제조 디지털 트윈 프레임워크 | 표준 | ISO (NIST 해설 경유) | 8, 22 | ref-386 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 |

## 추가 조사 요청

- 3·5·9절: 문·승강기·충전기 상태의 허용 경과 시간(몇 초까지 믿는가)을 정한 표준·가이드·국내 현장 기준 — 현재 이 절들의 핵심 주장(f13)이 출처 없는 [추정]이다.
- 3·5·8절: 물류센터(소매 매장이 아닌) 재고 기록 정확도 자료 — 현재 65% 수치는 한 소매업체 37개 매장 조건이라 물류센터 시나리오에 유추로만 썼다.
- 7절: VDA 5050 3.0.0 명세 전문에서 오래된 상태·연결 끊김 대응·시각 동기화 규정 유무를 전문 대조로 확인 — 현재 '이번에 연 문서 범위에서 찾지 못함'([추정])이다.
- 7절: Open-RMF 문·승강기 노드 구현 코드의 상태 발행 주기와 오래됨 처리 확인 — 문서에는 없고 코드는 보지 않았다.
- 7·10절: ISO 23247 표준 원문(또는 NIST 해설 원문)으로 참조 구조의 도메인 구성과 관측 요소 목록 확인 — 이번에는 정의와 참조 구조 존재만 [사실]로 썼다.
- 6·8절: 로봇 세계 상태에서 대상 지속성(object persistence)을 다룬 연구(Perpetua, Toris·Chernova 2017 등) — 신규 출처 상한으로 브리프에 들어오지 않았다.
- 5·6절: 로봇 관측으로 WMS 재고를 정정한 공개 사례와 로봇 관제 표준의 정정 기록 구조 — f16·f21 의 [추정]을 사실로 뒷받침할 근거가 없다.
- 10절: 이동건 외(2021) 원문에서 설계 검증과 운영 모니터링 기능 구분 방식 확인 — 원문 미열람으로 f30 은 [추정]이다.

## 이행한 수정 지시

- 원문 미열람 표시 — 13절 각주에서 ref-030·ref-384·ref-385·ref-386·ref-387·ref-388·ref-389·ref-390·ref-391·ref-392 의 접근일 뒤에만 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었으며, github_raw 로 연 ref-004·031·044·045·051·148·378~383 에는 붙이지 않았다(ref-030 요약도 '원문 미열람. '으로 시작하게 고침).
- f17·ref-030 — 4절·7절 SOSA 문장에 'W3C/OGC 작업반 저장소 편집본 기준, 권고안 문구와 다를 수 있음'을 밝히고 ref-030 각주에 (원문 미열람)을 붙였다.
- f1·f2·f3·f4 — 3·4·5·6·7·10절의 VDA 5050 문장마다 '3.0.0 판(공식 저장소 main) 기준, 확인일 2026-09-25'를 남겼고 각주 발행일은 미확인으로 두었다.
- f3·f8 — 5절 제약 칸과 7절 표 아래 문장을 '이번에 연 문서 범위에서 찾지 못했다'로 쓰고 [추정]을 유지했으며 전문 대조·구현 코드 미확인임을 덧붙였다.
- f12 — 4·8절과 ref-385 각주·reference_updates 의 기준일을 2021-05(IEEE JSAC 39(5))로 적었다.
- f20 — 3·8절 65% 문장 안에 '한 소매업체 37개 매장 조건이며 물류센터 값이 아니다'를 붙이고, 5절 보충 시나리오 예외·성과 칸과 서술에 소매 자료의 유추임을 밝혔다.
- f22 — 6·8절의 '약 30%'에 '저자 보고값, 실험 조건 미확인'을 표기했다.
- f25 — 7절 ISO 23247 행에서 도메인 이름과 관측 요소 8종 나열을 빼고 정의와 참조 구조 존재만 [사실]로 쓰며 '도메인 구성과 관측 요소 목록은 미확인'으로 표시했다.
- f28·f30 — 8절에는 이동건 외(2021)의 운영 단계 실시간 모니터링 부분만 두고, 설계 단계 가상 검증은 10절 22. 시뮬레이션·예측용 디지털 트윈 연결에만 두었다.
- f29 — 8절·각주·참고문헌 항목에서 게재지 이름을 빼고 '게재지 미확인(열린 질문)'으로 두었으며, 출처 충돌 질문에는 검색 요약(지능정보논문지)과 KoreaScience(한국인터넷방송통신학회논문지) 표기를 한쪽 선택 없이 함께 적었다.
- 11절 — f31 의 위치 신뢰도 문제는 새 질문을 만들지 않고 oq-028 에 연결했고, oq-024 도 이 영역 관련 질문으로 연결했다(open_question_updates 에 새로 넣지 않음).
- 직접 인용 — ref-031·ref-045 는 원문 구절을 인용하지 않고 모두 재서술해 출처당 1회 규칙을 넘지 않게 했다.
- 4절 용어 — '디지털 섀도'를 용어집 '디지털 트윈'과 구분되는 별도 항목으로 두고 정의 끝에 Kritzinger 외(2018) 분류 기준임을 밝혔으며(glossary_updates 포함), '오류 선언'은 4절에서 용어집 EPCIS 페이지로 링크하고 용어집 항목 설명에도 연결을 적었다.
- f2·f10 과 f6·f7 경계 — 연결 끊김·STALE 은 10절에서 19. 모니터링·이상 탐지·원인 분석과 연결만 했고, 문·승강기 제어 자체는 9절 표와 10절 10. 설비·건물 시스템 연동 항목에서 연계 대상으로만 짧게 썼다.
- 분량 초과 자동 분리: 8. 실시간 세계 상태·데이터 일관성 본문 10,730자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,735자
