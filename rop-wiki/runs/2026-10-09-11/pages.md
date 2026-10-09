# 스토리텔러 산출 2026-10-09-11

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md | draft | 갱신: 5절 병원 2건·기타 1건·제조 공장 1건 적용 사례 추가(물류창고 시나리오 유지), 6·7·8절에 시각·품질·만료·지속성 필터·시계 동기화와 로봇–승강기 표준 초안 추가, 9절 위치 신뢰 판단 행을 VDA 5050 3.0.0 7.8절에 맞춰 수정, 10절 건축 도면 자동 인식 트랙 반영 제안 2건 반영, 11절 기존 열린 질문 4건 근거 추가·새 질문 3건, 6·7·8·10·11절에 2026-09-25 판 분리 페이지 링크 유지, 13절 각주 갱신(ref-288 원문 열람 반영, 신규 15건)·프런트매터 sources 는 기존 22건에 신규·재사용 출처를 더함 |
| create | docs/topics/2026/2026-10-09-area18-s6.md | draft | 자동 분리: 18. 실시간 세계 상태·데이터 일관성 의 "6. 대표 접근법과 기술" 절(2,348자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area18-s10.md | draft | 자동 분리: 18. 실시간 세계 상태·데이터 일관성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,925자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area18-s7.md | draft | 자동 분리: 18. 실시간 세계 상태·데이터 일관성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,700자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area18-s11.md | draft | 자동 분리: 18. 실시간 세계 상태·데이터 일관성 의 "11. 열린 질문" 절(1,638자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area18-s8.md | draft | 자동 분리: 18. 실시간 세계 상태·데이터 일관성 의 "8. 대표 연구와 자료" 절(1,245자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 18. 실시간 세계 상태·데이터 일관성 | 갱신: 병원·기타·제조 공장 적용 사례 추가, 시각·품질·만료·지속성 필터·시계 동기화 접근과 로봇–승강기 표준 초안 추가, 9절 위치 신뢰 판단 서술을 VDA 5050 3.0.0 용도 규정에 맞춤, 건축 도면 자동 인식 트랙 반영 제안 2건 반영 | run 2026-10-09-11
- 홈 최근 업데이트: 2026-10-09 — 18. 실시간 세계 상태·데이터 일관성: 병원·기타·제조 공장 적용 사례 추가, 위치 신뢰 판단 서술을 VDA 5050 3.0.0 규정에 맞춰 수정, 건축 도면 자동 인식 트랙 반영 제안 2건 반영
- 대분류 최근 업데이트: 2026-10-09 — 18. 실시간 세계 상태·데이터 일관성: 적용 사례 4건(병원 2·기타 1·제조 공장 1) 추가, 9절 위치 신뢰 판단 행 수정, 34. 시뮬레이션·예측용 디지털 트윈과의 초기값 연결 정리
- 세부영역 최근 업데이트: 2026-10-09 — 18. 실시간 세계 상태·데이터 일관성: 5절 병원·기타·제조 공장 사례, 6~8절 시각·품질·만료·지속성 필터·시계 동기화와 표준 초안, 9절 위치 신뢰 판단 수정, 10절 트랙 반영 제안 2건, 11절 근거 추가·새 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 지속성 필터 | Persistence Filter | 반정적 환경의 특징이 마지막 관측 뒤에도 아직 남아 있을 확률을 시간에 따라 재귀적으로 계산하는 베이즈 추정기다. | 18, 15 | ref-1454, ref-1455 |
| new | 허가 만료 시각 | Lease Expiry (VDA 5050 leaseExpiry) | VDA 5050 에서 관제가 구역·간선 사용 허가에 붙이는 만료 시각으로, 이 시각이 지나면 허가는 무효가 되어 요청 상태가 EXPIRED 로 바뀐다. | 18, 20, 27 | ref-031 |
| new | 온라인 시뮬레이션 | Online Simulation | 운영 중인 실제 시스템의 현재 상태로 초기화하거나 동기화해 가까운 미래의 결과를 예측하는 데 쓰는 시뮬레이션이다. | 34, 18 | ref-1449, ref-1450 |
| new | 정밀 시간 프로토콜 | Precision Time Protocol (PTP) | 네트워크로 연결된 장치들의 시계를 하드웨어 시각 기록의 도움을 받아 마이크로초 수준으로 맞추는 시계 동기화 프로토콜이다. | 18, 42 | ref-1463 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 표준 | medium | https://www.w3.org/TR/vocab-ssn/ |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 표준 | medium | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| ref-288 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 표준 | high | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 |
| ref-296 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 |
| ref-1449 | Deubert, D., Klingel, L., & Selig, A. (arXiv; The International Journal of Advanced Manufacturing Technology 2024 표기) | Online Simulation at Machine Level: A Systematic Review | 논문 | medium | https://arxiv.org/abs/2401.07841 |
| ref-1450 | Galka, S. (Winter Simulation Conference 2024) | Reducing Transient Behavior in Simulation-Based Digital Twins: A Novel Initialization Approach for Order Picking Systems | 논문 | medium | https://informs-sim.org/wsc24papers/con211.pdf |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |
| ref-1452 | Open Robotics Discourse (open-rmf 질의응답 #414) | How to inform RMF that lift or door are not available? (#414) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/how-to-inform-rmf-that-lift-or-door-are-not-available-414/44744 |
| ref-1453 | Open Robotics (open-rmf, rmf_traffic API 문서) | Class LaneClosure — rmf_traffic API documentation | 오픈소스 문서 | high | https://openrmf.readthedocs.io/projects/rmf-traffic/en/latest/api/classrmf__traffic_1_1agv_1_1LaneClosure.html |
| ref-1454 | Rosen, D. M., Mason, J., & Leonard, J. J. (MIT DSpace; ICRA 2016) | Towards lifelong feature-based mapping in semi-static environments | 논문 | medium | https://dspace.mit.edu/handle/1721.1/107620 |
| ref-1455 | Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. (arXiv; IROS 2025 채택 표기) | Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments | 논문 | medium | https://arxiv.org/abs/2507.18808 |
| ref-1456 | ISO (ISO/TC 299 Robotics) | ISO/AWI 26159-2 Robotics — Infrastructure for robot applications — Part 2: Requirements for interfacing with lifts (elevators) and automatic doorways | 표준 | medium | https://www.iso.org/standard/92741.html |
| ref-1457 | ISO (ISO/TC 178 Lifts, escalators and moving walks) | ISO/CD TS 8100-11 Lifts for the transport of persons and goods — Part 11: Interoperability between lift and other systems | 표준 | medium | https://www.iso.org/standard/73063.html |
| ref-1458 | Changi General Hospital (CGH) | Changi General Hospital, CapitaLand Investment and KONE collaborate to advance the integration of robotics in buildings | 정부·연구기관 | medium | https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings |
| ref-1459 | The Straits Times (SingHealth 게재, Wong Shiying) | New software enables different robots to communicate with each other and building infrastructure | 기사 | medium | https://www.singhealth.com.sg/news/tomorrows-medicine/new-software-enables-different-robots-to-communicate-with-each-other-and-building-infrastructure |
| ref-575 | Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau; Frontiers in Robotics and AI) | On realizing autonomous transport services in multi story buildings with doors and elevators | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full |
| ref-1461 | 메디포뉴스 (이형규) | 용인세브란스병원, 지능형 의료서비스로봇 생태계 구축 | 기사 | low | https://medifonews.com/news/article.html?no=172554 |
| ref-1462 | 김지형 (KoreaScience 수록, 한국인터넷방송통신학회논문지 표기) | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 (Design and Implementation of Real-time Digital Twin in Heterogeneous Robots using OPC UA) | 논문 | medium | https://koreascience.or.kr/journal/view.jsp?kj=OTNBBE&py=2023&vnc=v23n4&sp=189 |
| ref-1463 | Yang, Q., & Liew, S. C. (The Chinese University of Hong Kong, arXiv) | Multi-robot Rigid Formation Navigation via Synchronous Motion and Discrete-time Communication-Control Optimization | 논문 | medium | https://arxiv.org/abs/2510.02624 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇이 직접 관측한 승강기·문 상태와 설비 제어기가 보고한 상태가 다를 때 어느 쪽을 기준으로 통과·탑승을 확정하는지 정한 표준이나 현장 사례가 있는가? | 18, 22 | 열림 | — |
| new | — | 지속성 필터처럼 마지막 관측 뒤 시간에 따라 믿음을 낮추는 확률 모델을 문·승강기·충전기 같은 설비 상태의 허용 경과 시간 판단에 적용한 연구나 사례가 있는가? | 18, 46 | 열림 | — |
| new | — | 실시간 세계 상태를 예측 시뮬레이션의 초기값으로 넘길 때 어떤 상태 항목·품질·시각 정보를 넘겨야 하는지 정한 인터페이스가 다중 이동로봇 운영에 쓰인 사례가 있는가? | 18, 34 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 작업 대상 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 병원 | 수행 자원 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 병원 | 제약 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 기타 | 수행 자원 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 기타 | 제약 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 기타 | 예외·성과 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 제조 공장 | 작업 대상 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 제조 공장 | 수행 자원 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 제조 공장 | 제약 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |
| 제조 공장 | 예외·성과 | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md#5-적용-사례-현장-유형-명시 | 18. 실시간 세계 상태·데이터 일관성 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) | 표준 | ISO (ISO/TC 299 Robotics) | 18, 22 | ref-1456 | https://www.iso.org/standard/92741.html |
| ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) | 표준 | ISO (ISO/TC 178 Lifts, escalators and moving walks) | 18, 22 | ref-1457 | https://www.iso.org/standard/73063.html |
| 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 | 표준 | 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) | 18, 22 | ref-1458 | https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings |

## 추가 조사 요청

- 5절 병원(용인세브란스·CGH)·기타(요양 시설·대학 건물)·제조 공장 사례의 시작 조건·완료·인계 칸: 작업 발생 계기와 완료 확인 방식이 브리프에 없어 '미확인'으로 두었다. 해당 사례의 운영 절차 자료가 필요하다.
- oq-034: 싱가포르 TR 93, ISO/AWI 26159-2, ISO/CD TS 8100-11 본문과 국내 TTA·KS 로봇–승강기 연동 표준에 설비 상태 갱신 주기·유효 시간 조항이 있는지 확인이 필요하다(7·11절).
- 10절: Galka(WSC 2024) 원문을 열어 과도 구간 개선 폭 수치를 확인해야 한다(현재 초록 기준으로만 기술).
- 10절: 건축 도면 자동 인식 트랙 반영 제안이 든 IFAC 2024 연구(운영 중 예측 시뮬레이션의 실부하 상태 초기화)와 어포던스 상태 연구(트랙 실행 2026-09-25-65 의 f20)를 재확인해야 반영할 수 있다.
- 6절·oq-035: VDA 5050 3.0.0 명세 마지막 약 7,700자에 시계 동기화 요구가 있는지와 이기종 로봇 환경의 허용 시계 오차 기준 자료가 필요하다.
- 5절: 상업 시설·가정·실외 현장에서 설비·로봇 상태를 통합하거나 오래된 상태를 다룬 사례가 없어 해당 현장 유형 사례를 조사해야 한다.
- 다음 실행 후보: 15. 지도·공간·위치 모델 페이지의 위치추정 신뢰도 서술과 용어집 localization-score 정의에 VDA 5050 3.0.0 7.8절 용도 규정(localizationScore·deviationRange 는 로그·시각화 전용) 반영 검토.
- pipeline 담당: 자동 분리 코드가 기존 절의 '자세한 내용은 주제 페이지 …' 링크 줄을 새 분리 페이지로 옮기지 않고 버린 것으로 보인다(2차 검증 지적). 이번 재실행에서는 append 패치 첫머리에 다른 문구의 링크 줄을 넣어 보존했으나, 분리 코드가 기존 분리 페이지 링크를 유지하도록 확인이 필요하다.

## 이행한 수정 지시

- f9 문구 수정 — 5절 사례 3 수행 자원 칸을 '통합반응상황실에 5G 기반 통합 관제 플랫폼을 더해 여러 로봇의 상태·위치를 실시간으로 모니터링하도록 구축을 진행 중이라고 보도되었다(2022-11-18 기준)'로 쓰고 참여 기업을 'LG전자·리드앤·트위니 등'으로 적었다.
- f26 문구 수정 — 7절 ISO/AWI 26159-2 행에 '디지털·이산(discrete) 방식 승강기 제어'로 적었다.
- f6·f7·f8 ref-1450 — 13절 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1450 에 source_unopened: true 를 넣었으며, 10절 f6 문장은 수치 없이 '과도 거동이 유의하게 개선되었다고 보고(초록 기준, 원문 미열람)'로만 썼다.
- ref-1449 — 13절 각주 제목 뒤에 IJAMT 2024 저널 판 DOI 10.1007/s00170-024-13065-1 을 적었고, 본문에는 검토 편수를 쓰지 않았다.
- f16 ref-288 — 13절 각주에서 '(원문 미열람)'을 빼고 접근일을 2026-10-09 로, 제목 뒤에 'OPC 10000-4 v1.05.07 웹 판 기준'을 밝혔으며 6·7절 본문에도 v1.05.07 웹 판을 적었다.
- f17 ref-030 — 13절 각주에 ' (원문 미열람)'을 유지하고 6절 문장에 'W3C·OGC 작업반 편집자 초안 sosa.ttl 기준, 권고안 문구와 다를 수 있음'을 병기했다(7절 표에도 편집자 초안 기준 표기).
- 9절 — 로봇 자체 지능·제어 행을 VDA 5050 3.0.0 용도 규정([사실] ref-031·ref-051)과 '위치추정 여부·지도 id·보고 시각으로 믿을지 판단하고 품질 점수·편차 범위는 기록·표시에만 쓴다'([추정])로 고쳤고, 외부 연계 열 '연계 대상: 로봇의 위치추정과 그 품질 계산, 센서 융합'은 유지했으며 표 아래에 수정 사유를 적었다.
- 10절 — 트랙 반영 제안 1은 f1~f4 로만, 제안 2는 f5~f8 로만 반영했고 어포던스 상태 연구와 IFAC 2024 연구는 근거로 쓰지 않는다고 밝혔으며, 영역은 5. 로봇 능력·작업 표현, 15. 지도·공간·위치 모델, 18. 실시간 세계 상태·데이터 일관성, 34. 시뮬레이션·예측용 디지털 트윈, 22. 설비·건물 시스템 연동, 27. 다중 로봇 경로·교통 관리 — MAPF 로 표기했다.
- 10절·6절 — 온라인 시뮬레이션 초기화와 예측 실험은 34. 시뮬레이션·예측용 디지털 트윈의 기능으로, 18. 실시간 세계 상태·데이터 일관성은 현재 상태를 시각·품질 정보와 함께 넘기는 쪽([추정], f8)으로만 썼고 6절에는 시뮬레이션 초기화를 넣지 않았다.
- 5절 — 사례를 병원(사례 3 용인세브란스 f9, 사례 4 CGH f10·f11), 기타(사례 5 요양 시설·대학 건물 f12·f13, '연계 대상:' 표시와 '이 14%는 전체 작업 기준' 명시), 제조 공장(사례 6 f14)으로 나눴고 f6 은 10절에만 썼으며 site_matrix_updates 는 실제로 채운 칸 10개만 냈다.
- f10·f11 — CGH 사례에서 ref-1458·ref-1459 를 교차 확인으로 쓰지 않는다고 본문에 밝히고, TR 93·KONE 연동은 'CGH 보도자료에 따르면'으로 적었다.
- f14·f15 — 김지형(2023) 내용은 기존 각주 ref-296 으로만 인용하고 ref-1462 는 11절 oq-037 의 KoreaScience 표기 근거로만 썼으며, oq-037 은 해결로 바꾸지 않고 'KCI 는 지능정보논문지, KoreaScience 는 한국인터넷방송통신학회논문지로 적으며 DOI·권호·쪽·발행기관(국제인공지능학회)은 같다; 현재 공식 명칭은 미확인'을 덧붙였다.
- f4·f8·f13·f20·f22·f25·f28·f31 — 모두 [추정] 태그와 '것으로 보인다' 표현으로 썼다(5·6·7·9·10·11절).
- 11절 — oq-028·oq-034·oq-035·oq-037 은 열림을 유지하고 새 근거만 덧붙였으며, open_questions_new 3건을 open_question_updates 에 new 로 등록하고 11절에도 적었다.
- 2차: 6·7·8·10·11절 링크 복원 — 각 절 append 패치 내용 첫머리에 2026-09-25 판 분리 페이지(2026-09-25-area08-s6·s7·s8·s10·s11)로 가는 링크 줄을 넣었다. 링크 텍스트는 기존과 같은 '18. 실시간 세계 상태·데이터 일관성 — <절 이름>'이고 경로는 ../../topics/2026/2026-09-25-area08-sN.md 로, 자동 분리 뒤 새 주제 페이지(docs/topics/2026/)로 옮겨져도 같은 대상에 닿는다. 문구는 '2026-09-25 판에서 정리한 … 기존 내용은 주제 페이지 […](…)에 있다'로 써서 분리 코드가 옛 '자세한 내용은' 줄과 혼동해 지우지 않게 했다.
- 2차: 프런트매터 sources 복원 — 13절 패치 frontmatter.sources 를 기존 22건(ref-004·ref-285·ref-294·ref-295 포함)을 그대로 두고 신규·재사용 출처 15건(ref-1449·ref-1450·ref-569·ref-1452·ref-1453·ref-1454·ref-1455·ref-1456·ref-1457·ref-1458·ref-1459·ref-575·ref-1461·ref-1462·ref-1463)을 더하는 방식으로만 바꿨다.
- 2차: 용어집 online-simulation — description 을 '예측 실험은 34. 시뮬레이션·예측용 디지털 트윈의 기능으로, 18. 실시간 세계 상태·데이터 일관성은 현재 상태를 초기값으로 넘기는 쪽으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다(추정)'로 바꿨다.
- 분량 초과 자동 분리: 18. 실시간 세계 상태·데이터 일관성 본문 14,992자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 6,926자
