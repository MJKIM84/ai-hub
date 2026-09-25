# 스토리텔러 산출 2026-09-25-25

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md | draft | 섹션 3~11 신규 작성(Open-RMF 문·승강기 어댑터와 설비 메시지, 디스펜서·인제스터, VDA 5050 3.0.0 해제·동작 구역, KS B 7317·단체표준·제조사 API, 출하 시나리오), 페이지 상태 표식 추가 |
| create | docs/topics/2026/2026-09-25-area10-s7.md | draft | 자동 분리: 10. 설비·건물 시스템 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,209자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area10-s4.md | draft | 자동 분리: 10. 설비·건물 시스템 연동 의 "4. 핵심 개념과 용어" 절(1,050자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area10-s10.md | draft | 자동 분리: 10. 설비·건물 시스템 연동 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(754자)을 옮겼다. 형식 수정: 본문 영역 링크를 주제 페이지 위치 기준 경로(../../categories/…)로 고침 |
| create | docs/topics/2026/2026-09-25-area10-s8.md | draft | 자동 분리: 10. 설비·건물 시스템 연동 의 "8. 대표 연구와 자료" 절(671자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area10-s11.md | draft | 자동 분리: 10. 설비·건물 시스템 연동 의 "11. 열린 질문" 절(655자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 10. 설비·건물 시스템 연동 | 섹션 3~11 신규 작성(Open-RMF 문·승강기 어댑터·설비 메시지, 디스펜서·인제스터 예시 구현, VDA 5050 3.0.0 해제·동작 구역, KS B 7317·승강기협회 단체표준·제조사 API, 출하 시나리오) | run 2026-09-25-25
- 홈 최근 업데이트: 2026-09-25 — 10. 설비·건물 시스템 연동: 섹션 3~11 신규 작성(문·승강기 어댑터, 승강기 세션·모드, VDA 5050 해제 구역, KS B 7317, 출하 시나리오)
- 대분류 최근 업데이트: 2026-09-25 — 10. 설비·건물 시스템 연동: 섹션 3~11 신규 작성(Open-RMF 설비 메시지, VDA 5050 3.0.0 주변 설비 범위, 국내 승강기–로봇 표준·API, 출하 작업대 인계 시나리오)
- 세부영역 최근 업데이트: 2026-09-25 — 10. 설비·건물 시스템 연동: 섹션 3~11 신규 작성, 열린 질문 oq-010 연결과 새 질문 3건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 승강기 어댑터 | Lift Adapter | Open-RMF 에서 플릿 어댑터·핵심 시스템의 승강기 요청을 받아 적절할 때만 승강기 노드에 전달하는 감독 구성요소이다. | 10, 12, 16 | ref-409 |
| new | 디스펜서·인제스터 | Dispenser / Ingestor | Open-RMF 에서 로봇에 물건을 내주는 작업대(디스펜서)와 로봇에서 물건을 받아들이는 작업대(인제스터)로, 각각 요청·결과·상태 메시지로 배송 작업과 연동된다. | 10, 17 | ref-023 |
| new | 해제 구역 | Release Zone | VDA 5050 3.0.0 에서 관제의 진입 허가를 받아야 이동로봇이 들어갈 수 있는 구역이다. | 10, 9, 15 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://doi.org/10.1177/20552076261437181 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |
| ref-408 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-409 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_lifts.html |
| ref-410 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-411 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-412 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg |
| ref-413 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 |
| ref-414 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 정부·연구기관 | medium | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 |
| ref-415 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 기사 | low | https://www.ctman.kr/35296 |
| ref-416 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 기사 | low | https://www.electimes.com/news/articleView.html?idxno=320147 |
| ref-417 | KONE | KONE Service Robot API | 벤더 문서 | low | https://dev.kone.com/api-portal/service-robot-api/ |
| ref-418 | 한국경제 | 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 | 기사 | low | https://www.hankyung.com/economy/article/202203314153Y |
| ref-419 | 파이낸셜뉴스 | 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" | 기사 | low | https://www.fnnews.com/news/202302140913318867 |
| ref-420 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 논문 | medium | https://doi.org/10.3390/electronics14050982 |
| ref-421 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 정부·연구기관 | medium | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? | 10, 28 | 열림 | — |
| new | — | 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? | 10, 17 | 열림 | — |
| new | — | 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? | 10, 26 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 출하 | 작업 대상 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 출하 | 수행 자원 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 출하 | 제약 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 출하 | 완료·인계 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 출하 | 예외·성과 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |
| 적치 | 예외·성과 | docs/categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 10. 설비·건물 시스템 연동 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | 산업통상자원부 국가기술표준원 | 10, 25 | ref-413 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 |
| Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) | 오픈소스 | Open Robotics (open-rmf) | 10, 12, 16 | ref-410 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |

## 추가 조사 요청

- 7절·9절: KS B 7317 본문의 조항 구성(속도 제어·보호 정지·틈새 극복 등이 실제 요구사항 항목인지)과 승강기 쪽 요구사항 포함 여부 — 현재 보도자료 설명만 있다.
- 7절·11절: 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준의 번호·제정일·메시지 구성 — 새 열린 질문과 연결된다.
- 8절: Electronics 2025(ref-420)의 승강기 선택 기준이 총 경로 길이인지 대기 시간인지 원문 확인 — 검색 요약끼리 어긋나 구절을 삭제했다.
- 2절 SCM 질문·5절: 컨베이어·작업대 준비와 로봇 도착을 함께 맞추는 공개 표준·연구(컨베이어–로봇 인계 핸드셰이크) — 현재 추정 수준 답만 있다.
- 3절·11절(oq-010): 물류센터 화물용 승강기·층간 반송 설비의 대기·처리량 정량 자료.
- 8절: 국토교통부 로봇 친화형 건축물 보도자료(ref-421)의 발행일과 2025-05-28 스마트+빌딩 착수 보도와 같은 문서인지 확인.
- 7절: 제조사 승강기 API(KONE, 현대엘리베이터)의 메시지 구조·인증 방식과 독립 출처 확인, VDMA 40001(OPC UA for Machinery)의 물류 설비 적용 범위.
- 퍼블리셔 확인: ref-408·ref-409·ref-410 은 실행 2026-09-25-24 의 ref-379·ref-380·ref-382 와 URL 이 같으므로 참고문헌 이중 등록 여부를 확인해야 한다.
- pipeline 담당 요청: 절 자동 분리 시 세부영역 페이지 기준 상대 링크(같은 대분류 파일명, ../<대분류 slug>/…)를 주제 페이지 위치 기준(../../categories/…)으로 다시 쓰는 처리가 없어 이번 실행에서 깨진 링크가 생겼다.

## 이행한 수정 지시

- f8 — 3절·9절·10절에서 '설비 연동 책임을 관제 쪽에 둔다' 구절 없이 'VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제 시스템의 최소 기능 목록에 넣는다'만 [사실][^ref-031]로 썼고, 9절에서 VDA 5050 이 책임을 배분한다고 쓰지 않았다.
- f14 — 8절 협의체 항목을 [추정][^ref-416]으로 강등하고 'API 로 실시간 정보를 주고받는' 구절을 뺐다.
- f17 — 7절 문장에 [추정] 벤더 주장을 유지하고 '배송로봇 40여 대' 수치를 삭제했다.
- f18 — 8절 Electronics 항목을 [추정][^ref-420]으로 강등하고 '승강기 선택을 최적화하는 그래프 기반 다층 경로계획 방법을 제안했다'만 남겼으며 선택 기준은 미확인으로 적었다.
- f22 — 3절·8절의 국토교통부 문장을 [추정][^ref-421]으로 강등하고 '로봇이 승강기 등을 이용해 건물 안을 이동할 수 있게 하는' 구절을 뺐으며 발행일은 미확인으로 두었다.
- f10 — 4절·6절에서 동작 구역을 진입·통과·이탈 때 action 을 수행하게 하는 장치로만 쓰고, 6절에 명세가 이를 문·승강기 연동 수단으로 규정하지 않는다고 적었다.
- f6 — 4절·6절·7절에서 디스펜서·인제스터를 Open-RMF 의 예시(sample) 작업대, 표준 규격이 아닌 예시 구현으로 서술했다.
- f11·f12 — KS B 7317 을 7절 표에서 로봇 자체 탑승 안전 요구사항·제약 조건으로, 9절에서는 연계 대상으로, 10절에서 25. 안전·위험 관리 연결로만 썼고, f12 는 보도자료의 설명이며 표준 본문 조항은 미확인이라고 7절에 밝혔다.
- f15·f16·f17 — 7절 제조사 API 세 문장 모두에 [추정] 벤더 주장을 병기하고, f16·f17 은 기사 출처이며 회사 발표에 기댄다고 적었다.
- 9절 — 승강기·자동문·컨베이어·PLC 제어와 설비 안전 제어를 '연계 대상:'으로 짧게 두고, ROP 쪽은 작업 요청·점유 예약·상태 확인·완료 확인으로 한정했으며 f26 은 [추정]을 유지했다.
- 원문 미열람 표기 — 13절 각주 정의에서 ref-047·ref-049·ref-060·ref-103·ref-163·ref-413~ref-421 의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었으며, ref-023·ref-031·ref-408~ref-412 에는 붙이지 않았다.
- 인용 — 모든 출처를 재서술로 쓰고 직접 인용을 두지 않아 ref-031·ref-408·ref-409 를 포함한 모든 출처가 출처당 1회 한도 안에 있다.
- ref-103 — reference_updates 와 13절 각주의 발행일을 2025 로 갱신하고 Sensors DOI 확인 사실을 요약에 적었다.
- 11절 — 기존 oq-010 을 연결하고 새 질문 3건을 올렸으며(open_question_updates 에 new 3건), 3절과 11절에 f24 의 승강기 대기 영향은 물류센터 정량 자료가 없어 추정이라는 점을 oq-010 과 함께 적었다.
- 분량 초과 자동 분리: 10. 설비·건물 시스템 연동 본문 7,260자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,511자
- 형식 검증(재작성): docs/topics/2026/2026-09-25-area10-s10.md 3절의 영역 링크 11개를 세부영역 페이지 기준 경로에서 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤다. 주장·태그·각주는 바꾸지 않았고, 이미 분리된 페이지 구성을 그대로 보내 재분리가 일어나지 않게 했다.
