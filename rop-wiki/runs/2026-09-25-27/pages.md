# 스토리텔러 산출 2026-09-25-27

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md | draft | 섹션 3~11 신규 작성(외부망 단절 운영 범위, VDA 5050 무선망 전제·QoS·베이스/호라이즌, ROS 2 DDS·Zenoh, 엣지 단절 운영, 계산 배치 선례, 피킹 시나리오), 페이지 상태 표식 추가, 조건부 승인 수정 16건 이행, 4·6·7·8·10절 주제 페이지 분리 상태 유지 |
| create | docs/topics/2026/2026-09-25-area11-s6.md | draft | 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "6. 대표 접근법과 기술" 절(2,039자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area11-s4.md | draft | 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "4. 핵심 개념과 용어" 절(1,171자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area11-s8.md | draft | 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "8. 대표 연구와 자료" 절(855자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area11-s7.md | draft | 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "7. 관련 표준·프레임워크·오픈소스" 절(769자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area11-s10.md | draft | 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(737자)을 옮겼다. 형식 수정: 본문 세부영역 링크 8개를 주제 페이지 위치 기준(../../categories/…) 경로로 고쳤다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 11. 분산 시스템·통신·컴퓨팅 구조 | 섹션 3~11 신규 작성(외부망 단절 운영 범위 추론, VDA 5050 무선망 전제·QoS·베이스/호라이즌, ROS 2 DDS·Zenoh, 엣지 단절 운영, 계산 배치 선례, 피킹 시나리오), 1차 조건부 승인 수정 16건 이행 | run 2026-09-25-27
- 홈 최근 업데이트: 2026-09-25 — 11. 분산 시스템·통신·컴퓨팅 구조: 외부망이 끊겨도 현장에서 어디까지 운영하는가를 VDA 5050·ROS 2·엣지 플랫폼 문서로 정리(신뢰도 low, 핵심 답은 추정)
- 대분류 최근 업데이트: 2026-09-25 — 11. 분산 시스템·통신·컴퓨팅 구조: 섹션 3~11 신규 작성(통신 손실 전제 설계, 엣지 단절 운영, 층별 역할 분담, 피킹 시나리오)
- 세부영역 최근 업데이트: 2026-09-25 — 11. 분산 시스템·통신·컴퓨팅 구조: 섹션 3~11 신규 작성, 새 열린 질문 3건 (실행 2026-09-25-27)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 포그 컴퓨팅 | Fog Computing | 클라우드와 말단 장치 사이에 계산·저장·네트워크 자원을 계층으로 두어 지연에 민감한 분산 애플리케이션을 현장 가까이에서 처리하게 하는 컴퓨팅 모델이다. | 11 | ref-474 |
| new | CAP 정리 | CAP Theorem | 네트워크 분할이 일어날 수 있는 분산 서비스는 일관성과 가용성을 동시에 완전히 보장할 수 없다는 정리이다. | 11, 8 | ref-481 |
| new | 5G 특화망(이음5G) | Private 5G Network (e-Um 5G) | 이동통신사가 아닌 기업·기관이 건물·공장 같은 특정 구역 단위로 5G 주파수를 할당받아 직접 구축해 쓰는 국내 5G 통신망이다. | 11 | ref-478 |
| new | 베이스·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 관제가 이미 해제해 로봇이 주행해도 되는 경로(베이스)와 계획만 되어 있고 아직 해제되지 않은 경로(호라이즌)를 구분하는 개념이다. | 11, 9, 12 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 오픈소스 문서 | high | https://github.com/open-rmf/free_fleet |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 벤더 문서 | low | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 |
| ref-468 | ROS 2 Design | ROS on DDS | 오픈소스 문서 | high | https://design.ros2.org/articles/ros_on_dds.html |
| ref-469 | ROS 2 Design | ROS 2 Quality of Service policies | 오픈소스 문서 | high | https://design.ros2.org/articles/qos.html |
| ref-470 | ROS 2 (ros2/rmw_zenoh GitHub) | rmw_zenoh — README (A ROS 2 RMW implementation based on Zenoh) | 오픈소스 문서 | high | https://github.com/ros2/rmw_zenoh |
| ref-471 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 오픈소스 문서 | high | https://github.com/kubeedge/kubeedge |
| ref-472 | Microsoft | Operate Azure IoT Edge devices offline | 벤더 문서 | medium | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities |
| ref-473 | Open Robotics (open-rmf) | rmf-web — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web |
| ref-474 | NIST | NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model | 정부·연구기관 | medium | https://csrc.nist.gov/pubs/sp/500/325/final |
| ref-475 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 논문 | medium | https://arxiv.org/abs/2205.09778 |
| ref-476 | Kehoe, B., Patil, S., Abbeel, P., & Goldberg, K. | A Survey of Research on Cloud Robotics and Automation | 논문 | medium | https://escholarship.org/uc/item/3t04p9m1 |
| ref-477 | OASIS | MQTT Version 5.0 | 표준 | medium | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html |
| ref-478 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 벤더 문서 | low | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 |
| ref-479 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 논문 | medium | https://arxiv.org/abs/2512.15215 |
| ref-480 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 기사 | low | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms |
| ref-481 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 논문 | medium | https://dl.acm.org/doi/10.1145/564585.564601 |
| ref-482 | ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행) | Ultra-low-latency services in 5G systems: A perspective from 3GPP standards | 논문 | medium | https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? | 11, 1, 20 | 열림 | — |
| new | — | 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? | 11, 9 | 열림 | — |
| new | — | 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? | 11, 3 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 피킹 | 작업 대상 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 피킹 | 수행 자원 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 피킹 | 제약 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 피킹 | 완료·인계 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 피킹 | 예외·성과 | docs/categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 11. 분산 시스템·통신·컴퓨팅 구조 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ROS 2 설계 문서 — ROS on DDS · QoS 정책 | 프레임워크 | ROS 2 Design | 11, 9 | ref-469 | https://design.ros2.org/articles/qos.html |
| rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) | 오픈소스 | ROS 2 (ros2/rmw_zenoh) | 11, 9 | ref-470 | https://github.com/ros2/rmw_zenoh |
| KubeEdge | 오픈소스 | KubeEdge (CNCF) | 11, 20 | ref-471 | https://github.com/kubeedge/kubeedge |
| Open-RMF rmf-web (대시보드·API 서버) | 오픈소스 | Open Robotics (open-rmf) | 11, 9 | ref-473 | https://github.com/open-rmf/rmf-web |
| MQTT Version 5.0 | 표준 | OASIS | 11, 9 | ref-477 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html |
| NIST SP 500-325 Fog Computing Conceptual Model | 프레임워크 | NIST | 11 | ref-474 | https://csrc.nist.gov/pubs/sp/500/325/final |

## 추가 조사 요청

- 5절·9절: 외부망 단절 중 물류센터 운영 범위(주문 지속·재고 확정·재연결 후 대사)를 정한 공개 운영 기준이나 국내 사례 — 현재 답(f22)이 추론뿐이다.
- 5절 제약: 3GPP TS 22.104 등 AGV·이동로봇 통신의 허용 지연·가용성 요구값 원문 — 리서치가 확인했으나 출처 상한으로 넣지 못했다.
- 5절·6절: VDA 5050 3.0.0 이 MQTT 5 세션 만료·메시지 만료를 쓰는지, 재연결 뒤 상태 재구성 절차를 규정하는지 — f17 추정을 사실로 확인할 근거가 없다.
- 8절: FogROS2 실험 조건(네트워크·클라우드 사양)과 Tanwani 외 포그 로보틱스 논문 원문 — 수치가 저자 보고값에 머문다.
- 6절: MiR Fleet Enterprise·HoST 등 관제 서버 이중화 방식(능동·대기 등)의 원문 확인 — 현재 벤더 주장 검색 요약뿐이다.
- 6절·10절: Open-RMF 또는 다른 오픈소스의 다거점 운영 공개 사례와 거점 간 WAN 장애 처리 자료.
- 3절: 창고 운영 중단 통계의 독립 출처(판매사 조사가 아닌 것)와 FreightWaves 기사의 비용 하한·발행일.

## 이행한 수정 지시

- f3 메시지 크기 상한 구절 삭제 — 6절 '손실을 전제한 메시지 설계'에서 [추정]을 유지하고 '브로커 위치·허용 지연·대역폭·무선랜 요건 규정은 찾지 못했다(전문 대조 아님)'로만 썼다.
- f3·f17 30초 표현 수정 — 5절 서술에서 '사건 발생 시와 적어도 30초마다(최대 간격 30초)'로 썼고 '최소 30초' 표현은 어디에도 쓰지 않았다.
- f13 강등 — 6절·8절에서 [추정]으로 쓰고 '저자 보고값, 실험 조건 미확인'을 병기했으며 쿠버네티스·UDP 보안 통신·H.264 구절을 넣지 않았다.
- f14 강등 — 6절·8절에서 [추정]으로 쓰고 '인프라 장착 센서·클라우드 컴퓨팅·로봇 탑재 지능을 결합한 참조 구조를 제시했다'까지만 썼으며 무선 TSN·on-premise 구절을 뺐다.
- ref-479 기관 수정 — 각주와 reference_updates 의 기관을 'Brorsson, E. 외'로 고쳤다.
- f20 비용 수정 — 3절에서 '시간당 최대 10만 달러, 하한 미확인'으로 쓰고 하이브리드 WMS 판매사 Synergy Logistics 의 조사 주장임을 유지했다.
- f25 표현 수정 — 6절에서 'ROS 2 기반 RMF와 웹 클라이언트 사이의 별도 서비스인 rmf-web API 서버'로 썼고 별도 기계 배치 표현을 쓰지 않았다.
- f23 범위 표시 — 6절 층별 역할 분담·도식과 9절 표에서 로봇 탑재부의 실시간 주행·회피를 분류 원문 9장 '로봇 자체 지능·제어'의 연계 대상으로 표시했다.
- f13·f14·f19 범위 — 6절에 계산 이전을 '계산 배치 선례로만 참고'한다고 밝히고, 9절 표·주석에서 계산 이전은 연계 대상, 이음5G 무선망 구축은 통신 기반 연계 대상으로만 두었다.
- 10절 26. 사이버보안·접근권한·개인정보 연결 — f13 을 빼고 용어집 'DDS 보안 규격' 링크와 ref-009 각주로만 연결했다.
- 10절 8. 실시간 세계 상태·데이터 일관성 연결 — 이전 실행 finding 을 인용하지 않고 f17(재연결 뒤 상태 재구성) 근거의 연결 문장만 두었다.
- 10절 27. AI·학습·적응과 모델 운영 연결 — 연결 한 줄만 두고 내용은 그 페이지에서 다룬다고 적었으며 본문에 풀어 쓰지 않았다.
- 원문 미열람 각주 — ref-227, ref-474~ref-482 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- 벤더 주장 병기 — f10(Azure IoT Edge, 6절), f19(이음5G, 3절), f21(MiR 이중화, 6절)을 '[추정] 벤더 주장' 으로 썼다.
- ref-031 직접 인용 1회 — 5절 서술의 'fulfills the order up to the last released node' 한 구절만 원문 인용하고 나머지 VDA 5050 내용은 재서술했다.
- 기준일 명시 — f18 은 '2020년 논문 기준'(5절·7절·8절), f1·f2 는 'VDA 5050 3.0.0(main, 확인일 2026-09-25) 기준'(4절·5절·6절·7절)으로 본문에 밝혔다.
- 분량 초과 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 본문 8,611자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,711자
- 형식 수정: docs/topics/2026/2026-09-25-area11-s10.md 본문의 세부영역 링크 8개(9·12·8·1·20·26·3·27)를 주제 페이지 위치 기준 ../../categories/<대분류 slug>/<파일>.md 로 고쳤다. 세부영역 페이지 프런트매터 sources 를 분리 뒤 남은 각주 정의(ref-031, ref-256, ref-471, ref-472, ref-475, ref-477~ref-482)와 일치시켰다. 주장·태그·각주 내용은 바꾸지 않았다.
