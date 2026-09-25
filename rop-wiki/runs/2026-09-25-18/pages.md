# 스토리텔러 산출 2026-09-25-18

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md | draft | 영역 심화: 섹션 3~11 신규 작성(분량 초과 절은 주제 페이지로 분리하고 요약·링크를 남김), 페이지 상태 자동 영역 표식 추가, 프런트매터 related_areas·tags·sources·confidence 채움 |
| create | docs/topics/2026/2026-09-25-area08-s7.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,700자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s6.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "6. 대표 접근법과 기술" 절(1,644자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s4.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "4. 핵심 개념과 용어" 절(1,467자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s11.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "11. 열린 질문" 절(1,104자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s8.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "8. 대표 연구와 자료" 절(1,046자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area08-s10.md | draft | 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(860자)을 옮겼다. 본문 연결 목록의 링크 8개를 주제 페이지 위치 기준 경로(../../categories/…)로 고쳤다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 8. 실시간 세계 상태·데이터 일관성 | 영역 심화: 섹션 3~11 신규 작성(시각·품질 표시, 오래된 상태 처리, 정정 이력, 22. 시뮬레이션·예측용 디지털 트윈과의 구분), 신규 출처 15건 인용, 열린 질문 4건 제기 | run 2026-09-25-18
- 홈 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 영역 심화로 섹션 3~11 작성. 표준이 대상별 허용 경과 시간을 정하지 않아 ROP 규칙이 필요하다는 추정과 시각·품질·정정 표현 방식 정리
- 대분류 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 영역 심화, 섹션 3~11 신규 작성(VDA 5050·Open-RMF·Sparkplug·EPCIS 시각·품질 비교, 22. 시뮬레이션·예측용 디지털 트윈과의 구분)
- 세부영역 최근 업데이트: 2026-09-25 — 8. 실시간 세계 상태·데이터 일관성: 영역 심화, 섹션 3~11 신규 작성, 열린 질문 4건 제기 (실행 2026-09-25-18)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 정보 나이 | Age of Information (AoI) | 수신 측이 가진 최신 상태 갱신이 생성된 뒤 흐른 시간으로, 정보가 얼마나 최신인지를 재는 지표이다. | 8, 11 | ref-189 |
| new | 디지털 섀도 | Digital Shadow | Kritzinger 외(2018)의 분류에서 물리 대상의 상태가 디지털 표현으로 한 방향 자동 흐름으로만 반영되는 단계의 디지털 표현으로, 디지털 모델·디지털 트윈과 구분된다. | 8, 22 | ref-191 |
| new | 무충돌 복제 데이터 타입 | Conflict-free Replicated Data Type (CRDT) | 여러 복제본을 조율 없이 수정해도 같은 갱신을 받으면 정해진 규칙으로 같은 상태에 수렴하도록 설계된 데이터 타입이다. | 8, 11 | ref-196 |

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
| ref-182 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 표준 | medium | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 |
| ref-183 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 오픈소스 문서 | high | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| ref-184 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-185 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_lifts.html |
| ref-186 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg |
| ref-187 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-188 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 표준 | high | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| ref-189 | Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. | Age of Information: An Introduction and Survey | 논문 | medium | https://arxiv.org/abs/2007.08564 |
| ref-190 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 정부·연구기관 | medium | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 |
| ref-191 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2405896318316021 |
| ref-192 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 논문 | medium | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 |
| ref-193 | Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. | Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments | 논문 | medium | https://arxiv.org/abs/2507.18808 |
| ref-194 | Massawe, L. V. 외(Sensors) | Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach | 논문 | medium | https://doi.org/10.3390/s120404187 |
| ref-195 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 |
| ref-196 | Preguiça, N., Baquero, C., & Shapiro, M. | Conflict-free Replicated Data Types (CRDTs) | 논문 | medium | https://arxiv.org/abs/1805.06358 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? | 8, 10 | 열림 | — |
| new | — | 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? | 8, 9, 11 | 열림 | — |
| new | — | 로봇이 보고한 적재물 식별·판독 결과와 WMS 재고 기록이 어긋날 때 어느 쪽을 기준으로 삼고 정정 기록을 누가 발행하는가(국내 물류센터 사례 포함)? oq-007·oq-003 과 관련된다. | 8, 7 | 열림 | — |
| new | — | 출처 충돌: 김지형(2023) 'OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현'의 게재 학술지가 Korea Science 표기로는 한국인터넷방송통신학회논문지(DOI 10.7236/JIIBC.2023.23.4.189), 다른 검색 요약으로는 지능정보논문지 23권 4호로 다르게 나온다. 어느 쪽이 맞는가? | 8 | 열림 | — |

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

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROS 2 Quality of Service 정책 (Jazzy 판 문서) | 오픈소스 | Open Robotics (ROS 2 Documentation) | 8, 11 | ref-183 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| Eclipse Sparkplug | 표준 | Eclipse Foundation | 8, 11, 19 | ref-188 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| OPC UA Part 4: Services — DataValue (OPC 10000-4 7.11) | 표준 | OPC Foundation | 8, 10 | ref-182 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 |
| ISO 23247 제조 디지털 트윈 프레임워크 | 표준 | ISO (NIST 해설 경유) | 8, 22 | ref-190 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 |

## 추가 조사 요청

- 3·5·11절: 문·승강기·충전기 등 대상별 허용 경과 시간(상태를 몇 초까지 믿을지)을 정한 표준·가이드·국내 현장 기준 — 현재 추정(f13)만 있고 값을 정한 출처가 없다.
- 7절: VDA 5050 3.0.0 명세 나머지 부분(입력 원문은 약 53%)에서 오래된 상태·연결 끊김 대응과 시각 동기화 규정 유무 확인 — f3 의 부재 관찰을 확정하거나 뒤집기 위해 필요하다.
- 7절: Open-RMF 문·승강기 어댑터 구현 코드에서 상태 발행 주기와 오래된 상태 처리 여부 확인(f8).
- 7·10절: ISO 23247 원문(특히 동기화 기술을 다루는 Part 4)을 직접 확인 — 현재는 NIST 해설 경유 [추정]이며 계층 구분 서술은 근거가 없어 삭제했다.
- 3·8절: 물류센터(소매 매장이 아닌) 재고 기록 정확도 자료와 국내 물류센터의 설비 상태 신선도·로봇–WMS 재고 불일치 사례 — 현재 65% 수치는 소매 매장 조건뿐이다.
- 전반: 교차 확인 0건 — VDA 5050·Open-RMF·Sparkplug·EPCIS 주장에 발행 주체와 독립된 두 번째 출처가 필요하다.
- 8절: Toris·Chernova(ICRA 2017) 시간 지속성 모델 등 출처 상한으로 넣지 못한 자료의 URL 확인.
- 다음 실행 후보: 10. 설비·건물 시스템 연동 페이지에 f6·f7·f8(문·승강기 상태 메시지와 어댑터 감독) 반영.
- pipeline 담당: 자동 분리 시 세부영역 페이지 기준 상대 링크(같은 대분류 파일명, ../<대분류 slug>/…)를 주제 페이지 위치 기준(../../categories/…)으로 다시 써 주는 처리가 필요하다 — 이번 실행의 10절 분리 페이지에서 링크 8개가 깨졌다.

## 이행한 수정 지시

- f26 계층 구분 삭제 — 7절 ISO 23247 행에서 '장치 통신 계층/디지털 트윈 계층' 부분을 빼고 'NIST 해설에 따르면 ISO 23247 은 …로 정의한다'로 쓰고 표준 원문과 NIST 해설 모두 원문 미열람임을 적었으며 태그를 [추정]으로 강등했다.
- f28 근거 한정 — 10절 첫 문단을 Kritzinger 외(2018)의 디지털 섀도 분류(f27)와 NIST 해설의 '동기화된 표현' 정의(f26 정의 부분)만으로 쓰고 계층 구분은 쓰지 않았다.
- f20 귀속 — 3절과 8절에서 65% 수치를 'DeHoratius·Raman(2008)이 한 소매업체 37개 매장 조사에서 보고했다'로 쓰고 같은 문장에 소매 매장 조건(물류센터 수치 아님)임을 밝혔다.
- f22 귀속 — 6절·8절에서 약 30% 수치를 Massawe 외(2012)가 이동 태그 환경 실험에서 보고한 저자 보고 값으로 쓰고 실험 조건은 원문 미열람임을 적었다.
- f3·f8 표현 — 3절·7절에서 '규정이 없다'고 단정하지 않고 '이번에 연 범위에서 찾지 못했다'로 쓰고, VDA 5050 입력 원문이 일부만 담겨 부재를 확정하지 않는다고 밝혔다.
- 추정 주체 명시 — f13·f16·f18·f21·f25·f28·f30·f31 문장을 '확인한 표준들로 볼 때 …할 것으로 보인다', '이 위키는 …로 본다' 형식으로 고쳐 출처가 결론을 말한 것처럼 쓰지 않았다.
- f6·f7 범위 — 6절·9절에서 문·승강기 어댑터의 감독 역할을 'Open-RMF 의 구성'으로 서술하고, 9절 표에서 문·승강기 자체 제어와 설비 안전 제어를 '연계 대상'으로 두며 ROP 직접 범위를 상태 확인·요청·인계로 한정했다.
- f23 성격 — 6절·8절에서 Perpetua 를 로봇 지도·환경 모델 연구로 소개하고 ROP 세계 상태에 적용할 방법 참고로만 다룬다고 밝혔다.
- f29 배치 — 8절에서는 제조 현장 대상의 이기종 로봇·PLC 실시간 수집·표현 국내 사례로만 쓰고, 3D 시뮬레이션 측면은 10절 22. 시뮬레이션·예측용 디지털 트윈 항목에서 연결만 했으며, 각주 게재지를 '미확인(출처 충돌, 열린 질문)'으로 두고 출처 충돌 열린 질문에 한국인터넷방송통신학회논문지(DOI 10.7236/JIIBC.2023.23.4.189)와 지능정보논문지를 둘 다 적었다.
- 10절 구분 — 22. 시뮬레이션·예측용 디지털 트윈과의 구분을 2절 원문 주석을 따른다고 밝혀 제시했고 원문 주석 인용 블록은 한 글자도 고치지 않았다.
- 11절 연결 — 새 질문 3(로봇 적재물 식별과 WMS 재고 불일치)에 oq-007·oq-003 과의 관련을 적고 열린 질문 페이지로 링크했으며, 기존 oq-024 를 이 영역의 열린 질문으로 연결했다.
- 인용 제한 — 직접 인용은 ref-031 의 'at least every 30 seconds' 한 곳만 두고 ref-045(f14·f15)·ref-051(f4) 등 나머지 문구는 요약·재서술했다.
- 미열람 각주 — ref-030·ref-182·ref-189·ref-190·ref-191·ref-192·ref-193·ref-194·ref-195·ref-196 각주 끝에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었으며, ref-030 각주에 W3C/OGC 작업반 저장소 편집본 sosa.ttl 로 정의를 확인했음을 적었다.
- f9 기준 — 4절·6절·7절에 ROS 2 QoS 가 Jazzy 판 문서 기준(2026-09-25 확인)임을 밝혔고, ref-182~ref-188 과 VDA 5050 계열(ref-031·ref-051) 각주의 발행일을 '미확인'으로 두었다.
- 용어집 — '디지털 섀도' 정의에 Kritzinger 외(2018)의 분류임을 밝히고 설명에 기존 '디지털 트윈' 용어 페이지 링크를 두었으며 기존 '디지털 트윈' 정의는 바꾸지 않았다.
- 분량 초과 자동 분리: 8. 실시간 세계 상태·데이터 일관성 본문 10,331자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,649자
- 형식 검증 재작성: docs/topics/2026/2026-09-25-area08-s10.md 3절 연결 목록의 깨진 링크 8개(세부영역 페이지 기준 상대 경로)를 주제 페이지 위치 기준 경로 ../../categories/<대분류 slug>/<파일>.md 로 고쳤다. 세부영역 페이지 프런트매터 sources 를 남은 본문의 각주 정의 17건과 일치시키고, reference_updates 의 cited_by 를 실제 인용 페이지로 맞췄다. 주장·태그·각주 내용은 바꾸지 않았다.
