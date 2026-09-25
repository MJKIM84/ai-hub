# 스토리텔러 산출 2026-09-25-50

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md | draft | 영역 심화: 3~11절 신규 작성(VDA 5050·Open-RMF 예외 동작, 통신 단절, 실행 중 재계획 연구, 보상·정정, BCP 참조 틀, 피킹→포장 운반 중 고장 시나리오), 페이지 상태 자동 영역 추가 |
| create | docs/topics/2026/2026-09-25-area20-s6.md | draft | 자동 분리: 20. 예외 복구·재계획·업무 연속성 의 "6. 대표 접근법과 기술" 절(1,542자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area20-s4.md | draft | 자동 분리: 20. 예외 복구·재계획·업무 연속성 의 "4. 핵심 개념과 용어" 절(1,199자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area20-s11.md | draft | 자동 분리: 20. 예외 복구·재계획·업무 연속성 의 "11. 열린 질문" 절(1,125자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area20-s7.md | draft | 자동 분리: 20. 예외 복구·재계획·업무 연속성 의 "7. 관련 표준·프레임워크·오픈소스" 절(837자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area20-s10.md | draft | 자동 분리: 20. 예외 복구·재계획·업무 연속성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(736자)을 옮겼다. 본문 링크를 주제 페이지 기준 경로(../../categories/…)로 고침 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 20. 예외 복구·재계획·업무 연속성 | 영역 심화: 3~11절 신규 작성(VDA 5050·Open-RMF 예외 동작, 통신 단절, 실행 중 재계획 연구, 보상·정정, BCP 참조 틀, 피킹→포장 운반 중 고장 시나리오) | run 2026-09-25-50
- 홈 최근 업데이트: 2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 영역 심화로 3~11절 작성(운반 중 고장 로봇의 화물·남은 주문 처리 흐름, VDA 5050·Open-RMF 중단·취소·재계획, 업무 연속성 참조 틀)
- 대분류 최근 업데이트: 2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 영역 심화 3~11절 신규 작성, 열린 질문 3건 추가
- 세부영역 최근 업데이트: 2026-09-25 — 20. 예외 복구·재계획·업무 연속성: 3~11절 신규 작성(실행 2026-09-25-50)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 보상 트랜잭션 | Compensating Transaction | 여러 단계로 이루어진 작업이 도중에 실패했을 때 이미 완료된 단계의 효과를 업무 규칙에 맞게 되돌리는 작업이다. | 20, 1, 12 | ref-578 |
| new | 업무 연속성 관리 시스템 | Business Continuity Management System (BCMS) | 교란 사건에 대비하고 핵심 업무를 지속·복구하기 위한 조직의 관리 체계로, ISO 22301 이 요구사항을 정한다. | 20 | ref-575 |
| new | 주문 취소 즉시 동작 | cancelOrder (VDA 5050 instant action) | VDA 5050 에서 관제가 보내면 로봇이 가능한 한 빨리 정지하고 남은 동작을 실패로 보고한 뒤 유휴 상태가 되게 하는 즉시 동작이다. | 20, 9, 12 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-188 | Hönig, W., Kiesel, S., Tinka, A., Durham, J. W., & Ayanian, N. | Persistent and Robust Execution of MAPF Schedules in Warehouses | 논문 | medium | https://ieeexplore.ieee.org/abstract/document/8620328/ |
| ref-251 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-537 | Open Robotics (open-rmf/rmf_ros2) | rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp |
| ref-572 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 논문 | medium | https://arxiv.org/abs/2403.18145 |
| ref-573 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 논문 | medium | https://www.mdpi.com/1424-8220/21/19/6536 |
| ref-574 | Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH) | Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning | 논문 | medium | https://arxiv.org/abs/2211.08201 |
| ref-575 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 표준 | medium | https://www.iso.org/standard/75106.html |
| ref-576 | 행정안전부 | 재해경감 우수기업 인증제도 | 정부·연구기관 | medium | https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do |
| ref-577 | 고용노동부 | 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내 | 정부·연구기관 | medium | https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591 |
| ref-578 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 오픈소스 문서 | medium | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction |
| ref-579 | Element Logic | FAQ - Element Logic (AutoStore) | 벤더 문서 | low | https://www.elementlogic.net/solutions-and-services/autostore/faq/ |
| ref-580 | Swisslog | The benefits of using AutoStore for high-throughput retail fulfillment | 벤더 문서 | low | https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp |
| ref-581 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 표준 | medium | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf |
| ref-374 | Open Robotics (open-rmf/rmf_ros2) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/issues/224 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가? | 20, 7 | 열림 | — |
| new | — | 국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가? | 20, 18 | 열림 | — |
| new | — | 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? | 20, 22 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 피킹 | 작업 대상 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 피킹 | 수행 자원 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 피킹 | 제약 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 피킹 | 완료·인계 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 피킹 | 예외·성과 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 시작 조건 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 작업 대상 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 수행 자원 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 제약 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 완료·인계 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |
| 포장 | 예외·성과 | docs/categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 20. 예외 복구·재계획·업무 연속성 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) | 표준 | ISO | 20 | ref-575 | https://www.iso.org/standard/75106.html |
| 기업재난관리표준·재해경감 우수기업 인증제 | 평가 프로그램 | 행정안전부 | 20 | ref-576 | https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do |
| 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) | 프레임워크 | 고용노동부 | 20 | ref-577 | https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591 |
| 보상 트랜잭션 패턴(Compensating Transaction pattern) | 프레임워크 | Microsoft (Azure Architecture Center) | 20, 1, 12 | ref-578 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction |
| Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) | 오픈소스 | Open Robotics (open-rmf) | 20, 9, 12 | ref-537 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp |

## 추가 조사 요청

- 5절 예외·성과: 로봇 일부 고장·제한 운영 시 처리량·시간·비용 영향 수치(독립 출처 2개 이상)가 없어 '미확인'으로 두었다.
- 5절 완료·인계·11절: 고장 로봇 화물 회수 시 재고 위치 확인(스캔·무게·위치) 운영 기준과 국내 사례가 필요하다.
- 7절: ISO 22301 의 업무 영향 분석·목표 복구 시간(RTO) 요구와 KS A ISO 22301 부합화 연도를 1차 출처로 확인할 필요가 있다.
- 4·6절: EPCIS 현행 판(2.0, ISO/IEC 19987:2024)에서 오류 선언 방식이 유지되는지 확인이 필요하다(현재 EPCIS 1.2 기준으로만 서술).
- 6절: VDA 5050 에서 cancelOrder 뒤 적재물 처리 규정 유무를 다른 절(3.0.0 전체)과 교차 확인할 필요가 있다.
- 6·7절: 표준 목록이 20. 예외 복구·재계획·업무 연속성과 연결한 ARIAC(ref-008)·KubeEdge(ref-300)·rmf_task(ref-366)·rmf_demos(ref-104)의 예외 복구 관련 내용이 이번 브리프에 없어 본문에 넣지 못했다.
- 3절: 국내 물류센터의 로봇·관제 장애 수동 전환 사례(한국어 자료)가 필요하다.

## 이행한 수정 지시

- ref-188 중복 방지 — 브리프의 ref-188 을 기존 ref-188(같은 논문·같은 URL)로 통합해 f11 을 쓴 4·6·8·10절 각주와 13절 정의, reference_updates 모두 기존 ref-188 로 두고 새로 등록하지 않았다.
- f11·f21 기존 용어 재사용 — 4절에서 행동 의존 그래프·오류 선언을 용어집 action-dependency-graph·epcis-error-declaration 에 링크했고 glossary_updates 에 넣지 않았다.
- '업무 연속성 관리 시스템' 띄어쓰기 — 4절 용어와 glossary_updates 의 term_ko 를 '업무 연속성 관리 시스템'으로 적었다.
- f2 connectionState 네 값 — 4절에 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 네 값을 적었다.
- f6 통로 이탈 문맥 — 6절에서 '통로(corridor) 이탈 오류 같은 상황에서'로 쓰고 교착 해소 전략·알고리즘 자체는 명세 범위 밖이라는 문장을 더했다.
- f1 적재물 처리 — 4절에 '명세 6.1.3 절에는 취소 시 실린 적재물을 어떻게 처리하는지에 대한 언급이 없다'를 [추정]으로 적었다.
- f9 Read Only 각주 — 6절의 읽기 전용 문장에는 ref-004 만, 전체 제어·신호등 제어 문장에는 ref-251 를 달았다.
- f12 수치 — 6절에 '저자 보고값(ICAPS 2024, 단일 출처)', 8절에 '속도 수치는 저자 보고값'을 명시했다.
- f15 판 명시 — 7절 표에 'ISO 22301:2019 기준(개정 1:2024 별도)'으로 적었다.
- f21 기준 판 — 4·5·6절에 'EPCIS 1.2(2016-09-29) 기준'을 명시하고 6절에 현행 판 유지 여부는 확인하지 않았다고 적었다.
- f15·f16·f17 범위 — 3절·7절·9절에서 기업 BCP·BCMS 체계를 ROP 직접 범위가 아닌 참조 틀(연계 대상)로 짧게 서술하고 f17 을 감염병 대응 권고 가이드로 밝혔다.
- f19·f20 벤더 주장 — 3·5절에서 [추정] 뒤에 '벤더 주장'을 병기하고 AutoStore 제어 소프트웨어의 XHandler 모듈·Swisslog 자사 소프트웨어 SynQ 의 기능으로 서술했으며 ROP 기능으로 쓰지 않았다.
- f18 물리 적용 — 6절에서 보상 트랜잭션을 화물 되돌림·재고 반영에 적용하는 문장을 [추정]으로 썼다.
- ref-574 기관 — 각주와 reference_updates 의 기관을 'Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH)'로 고쳤다.
- ref-580 URL — 각주와 reference_updates 의 URL 을 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 고쳤다.
- 원문 미열람 표시 — ref-188·572·573·574·575·576·577·579·580·581·374 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-576·579·374 의 발행일 자리에 '미확인'을 썼다.
- 열린 질문 상태 — 11절에서 oq-003·oq-021·oq-038·oq-048 을 모두 '열림'으로 두고 부분 근거로만 적었으며 open_question_updates 에 해결로 내지 않았다.
- 분량 초과 자동 분리: 20. 예외 복구·재계획·업무 연속성 본문 8,408자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,648자
- 형식 검증 재작성: docs/topics/2026/2026-09-25-area20-s10.md 3절의 세부영역 링크 10개를 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤고, 세부영역 페이지 프런트매터 sources 를 13절 각주 정의(14건)와 일치시켰다. 주장·태그·각주 내용은 바꾸지 않았다.
