# 스토리텔러 산출 2026-09-25-20

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md | draft | 섹션 3~11 신규 작성(제어 수준 4범주, 어댑터 API 요구, VDA 5050 3.0.0, MassRobotics, 출하 시나리오), 트랙 반영 제안 7절 반영, 페이지 상태 표식 추가. 2차 수정: 9절 설비 행 태그 분리·free_fleet 문장 태그와 ref-264 각주 추가, 8절 요약 문장 교체 |
| create | docs/topics/2026/2026-09-25-area09-s7.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,784자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area09-s8.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "8. 대표 연구와 자료" 절(1,706자)을 옮겼다. 2차 수정: 1절·3절 첫 요약 문장을 ref-267 범위 문장과 조사 범위 설명 두 문장으로 교체 |
| create | docs/topics/2026/2026-09-25-area09-s6.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "6. 대표 접근법과 기술" 절(1,498자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area09-s11.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "11. 열린 질문" 절(1,297자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area09-s4.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "4. 핵심 개념과 용어" 절(1,070자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area09-s10.md | draft | 자동 분리: 9. 로봇·제조사 관제 연동 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(815자)을 옮겼다. 세부영역 링크를 주제 페이지 위치 기준 경로로 고쳤다. 2차 수정: 12. 명령·작업 실행의 신뢰성 연결 문장 태그를 [추정]으로 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 9. 로봇·제조사 관제 연동 | 영역 심화: 3~11절 신규 작성(제어 수준·어댑터 API·VDA 5050 3.0.0·MassRobotics·출하 시나리오), 트랙 반영 제안 1건 반영 | run 2026-09-25-20
- 홈 최근 업데이트: 2026-09-25 — 9. 로봇·제조사 관제 연동: 3~11절 신규 작성(Open-RMF 제어 수준 4범주, VDA 5050 3.0.0 주문·오류·연결 상태, 출하 운반 시나리오)
- 대분류 최근 업데이트: 2026-09-25 — 9. 로봇·제조사 관제 연동: 영역 심화 초안(직접 제어 대 제조사 관제 위임, 어댑터가 맡는 변환과 연계 경계)
- 세부영역 최근 업데이트: 2026-09-25 — 9. 로봇·제조사 관제 연동: 3~11절 신규 작성, 트랙 반영 제안(2026-09-25-02)을 7절에 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| update | VDA 5050 | VDA 5050 | 서로 다른 제조사의 AGV·AMR을 하나의 관제로 운용하기 위한 제조사 중립 통신 인터페이스이다. | 9, 5, 7, 28 | ref-031, ref-267 |
| new | 플릿 관리 시스템 | Fleet Management System (FMS) | 여러 이동로봇에 작업을 배정하고 경로·상태를 관리하는 관제 소프트웨어로, 로봇 제조사가 자사 로봇용으로 제공하는 경우가 많다. | 9, 13 | ref-266 |
| new | 다중 플릿 오케스트레이션 | Multi-Fleet Orchestration | 제조사가 다른 여러 로봇 플릿을 제3자 관제가 한곳에서 조율하는 것으로, 로봇을 직접 제어하는 저수준 방식과 제조사 관제에 작업을 넘기는 고수준 방식이 있다. | 9, 13, 15 | ref-265 |
| new | 메시지 큐잉 원격 측정 전송 | Message Queuing Telemetry Transport (MQTT) | 브로커를 거쳐 토픽 단위로 메시지를 발행·구독하는 경량 메시징 프로토콜로, VDA 5050이 관제와 이동로봇 사이 통신에 쓴다. | 9, 11 | ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 표준 | medium | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-136 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 논문 | medium | https://www.mdpi.com/2076-3417/15/13/7235 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-258 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-259 | Open Robotics | Integration (integration) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration.html |
| ref-260 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-261 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-262 | Open Robotics (open-rmf) | awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/awesome_adapters |
| ref-263 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 오픈소스 문서 | high | https://github.com/inorbit-ai/ros_amr_interop |
| ref-264 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 오픈소스 문서 | high | https://github.com/open-rmf/free_fleet |
| ref-265 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 업계 보고서 | medium | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ |
| ref-266 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 정부·연구기관 | medium | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ |
| ref-267 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 논문 | medium | https://www.researchgate.net/publication/374741902_Identification_of_requirements_and_opportunities_for_new_types_of_standardized_interfaces_for_AGV_systems_based_on_the_VDA_5050_concept |
| ref-268 | ScienceDirect 게재 논문(저자 미확인) | Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0278612526000166 |
| ref-269 | 헬로티(HelloT) | 미르, 다기종 모바일 로봇 연동 SW 어댑터 ‘MiR VDA 5050’ 론칭 | 기사 | low | https://www.hellot.net/news/article.html?no=99467 |
| ref-270 | 클로봇(Clobot) | 통합 로봇 관제 플랫폼 크롬스[CROMS] | 벤더 문서 | low | https://clobot.co.kr/croms |
| ref-271 | 디지털투데이 | 카카오모빌리티, 로봇 플랫폼 사업 본격화..."이기종 로봇 통합 운영" | 기사 | low | https://www.digitaltoday.co.kr/news/articleView.html?idxno=665333 |
| ref-272 | 머니투데이 | "로봇 통합 관제 기술, 인정받았다"..노바테크, 70억원 투자 유치 | 기사 | low | https://www.mt.co.kr/industry/2026/07/14/2026071409414468672 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가? | 9, 3 | 열림 | — |
| new | — | 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? | 9, 15 | 열림 | — |
| new | — | Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? | 9, 12, 19 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 9. 로봇·제조사 관제 연동 |
| 출하 | 수행 자원 | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 9. 로봇·제조사 관제 연동 |
| 출하 | 제약 | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 9. 로봇·제조사 관제 연동 |
| 출하 | 완료·인계 | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 9. 로봇·제조사 관제 연동 |
| 출하 | 예외·성과 | docs/categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 9. 로봇·제조사 관제 연동 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| free_fleet (Open-RMF 플릿 어댑터) | 오픈소스 | Open Robotics (open-rmf) | 9 | ref-264 | https://github.com/open-rmf/free_fleet |
| ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) | 오픈소스 | InOrbit | 9, 28 | ref-263 | https://github.com/inorbit-ai/ros_amr_interop |
| Open-RMF fleet_adapter_template | 오픈소스 | Open Robotics (open-rmf) | 9 | ref-105 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |

## 추가 조사 요청

- 3·5절: 개별 로봇 직접 제어와 제조사 관제 위임의 처리량·연동 비용을 정량 비교한 자료(국내 물류센터 우선) — 현재 f34 는 추정 수준이다.
- 7절·11절: VDA 5050 3.0.0 의 정확한 발행일(ref-032 보도자료 원문 열람) — oq-005 출처 충돌 해소에 필요하다.
- 7절: awesome_adapters(ref-262) 각 어댑터가 Open-RMF 의 어느 제어 수준(전체 제어·신호등·읽기 전용)으로 붙는지 — 브리프에서 미확인이라 본문에 쓰지 않았다.
- 8절: 국내 표준(TTA·KS)이나 공공 연구기관 자료 가운데 이기종 로봇 관제 인터페이스를 다룬 것 — 이번에는 기사·벤더 자료뿐이었다.
- 8절: ref-136 의 120 ms 지연 측정 조건과 ref-268 의 저자·권호 확인(원문 열람).
- 대분류 C. 연결·실행 기반 페이지의 '다른 대분류와의 연결' 절은 C 대분류 세부영역 심화가 끝난 뒤로 미룬다(예산·규칙).
- 퍼블리셔: 신규 참고문헌 ref-258~ref-272 가 미게시 실행의 번호와 충돌하지 않는지 확인이 필요하다(1차 검증 지적). ref-228·ref-230 의 게시 신뢰도(high)를 이번 medium 으로 낮출지도 판단이 필요하다(2차 검증 참고).
- pipeline 담당: 자동 분리 코드가 세부영역 절을 주제 페이지로 옮길 때 상대 링크를 주제 페이지 위치 기준으로 다시 쓰고, reference_updates 의 cited_by 에 분리 주제 페이지를 더하며, '아래 표는'·'(6절)' 같은 원 절 기준 지시어를 처리해야 한다(2차 검증 참고).

## 이행한 수정 지시

- f4: 어댑터 역할만 [사실] — 4절 플릿 어댑터 항목에 '하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리'만 [사실][^ref-259]로 쓰고 ROS 1·ROS 2·REST·XMLRPC·SQL DB 연동 경로 열거는 넣지 않았다.
- f15: connection 상태 네 값 — 6절 VDA 5050 소제목에 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 으로 적었다.
- f9: free_fleet — 6절 '로봇 내비게이션 스택에 직접 붙는 방식'에 연동 방식 사례로만 쓰고 'Nav1 통합은 시뮬레이션과 ROS 1 Noetic 에서만 시험됐다'를 병기했으며, 9절에서 주행 기능은 ROP 로 가져오지 않음을 밝혔다.
- f21: ros_amr_interop — 7절 표 행에 README 빌드 표 기준(확인일 2026-09-25) VDA5050 패키지 Galactic, MassRobotics 송신 노드 Foxy·Galactic 을 병기했다.
- f10: 7절 awesome_adapters 행에 어댑터 목록만 쓰고 어댑터별 제어 수준은 적지 않았다(추가 조사 요청으로 이동).
- f22: 3·4절의 [의견] 문장에 'Interact Analysis 는 자사 분석(의견)에서' / 'Interact Analysis 의 구분(의견)'으로 주체를 밝히고 [^ref-265] 각주를 달았다.
- f25·f30: 8절에서 f25 는 '제조 공장 대상 연구이므로 방법 참고로 본다', f30 은 '[추정] 벤더 주장' 과 '대상은 전기차 생산 공장이며 물류센터 사례가 아니다'를 명시했다.
- f26: 8절에서 120 ms 수치를 별도 문장으로 두고 '단일 출처이고 측정 조건은 미확인'을 병기했으며 결론 근거로 쓰지 않았다.
- f27·f28·f29·f30: 8절 보조 자료와 10절 13. 작업 배정 — MRTA 연결에서 모두 '[추정] 벤더 주장'으로 쓰고 가동률 배수 등 성과 수치는 넣지 않았다.
- f19: 7절 VDA 5050 3.0.0 행에 발행일 '미확인'과 oq-005 를 적고, 11절에 oq-005 를 열림 상태로 연결했다(해결로 바꾸지 않음).
- 트랙 반영 제안: 7절 표에 팩트시트를 3.0.0 명세 근거 f18 [사실][^ref-031][^ref-228]로, MassRobotics 메시지를 identityReport·statusReport(f20)로 적고, 오류·action 보고(f14·f16)와 Open-RMF 작업 능력·사용자 정의 동작(f7·f5)도 반영했다.
- f32~f36: [추정] 태그를 유지했고, 5절 시나리오를 '출하' 단계와 여섯 항목 표로 썼으며(작업 대상은 해당 없음), f35 는 9절 표에 '연계 대상:' 표시로 두고, f34 뒤에 '두 방식의 처리량·비용을 정량 비교한 자료는 찾지 못했다'를 남겼다.
- 인용: ref-031·ref-260 을 포함한 모든 출처에서 직접 인용을 쓰지 않고 evidence_excerpt 내용을 한국어로 재서술했다.
- 각주·참고문헌: ref-032·136·228·230·261·265·266·267·268·269·270·271·272 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다(ref-261 summary 도 '원문 미열람. '으로 시작).
- 용어집: glossary_updates 에 'VDA 5050' 항목을 action update 로 내고 정의를 '서로 다른 제조사의 AGV·AMR을 하나의 관제로 운용하기 위한 제조사 중립 통신 인터페이스'로 바꿨다(근거 ref-031·ref-267).
- 용어집: MQTT 후보의 term_ko 를 '메시지 큐잉 원격 측정 전송'으로 바꾸고 term_en 에 Message Queuing Telemetry Transport (MQTT)를 두었으며 본문 4절도 같은 표기로 썼다.
- 10절: 연결 여덟 개를 모두 번호와 이름(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 10. 설비·건물 시스템 연동, 11. 분산 시스템·통신·컴퓨팅 구조, 12. 명령·작업 실행의 신뢰성, 13. 작업 배정 — MRTA, 15. 다중 로봇 경로·교통 관리 — MAPF, 20. 예외 복구·재계획·업무 연속성)으로 쓰고 related_areas 와 맞췄다.
- 분량 초과 자동 분리: 9. 로봇·제조사 관제 연동 본문 10,808자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,585자
- 형식 검증 재작성: docs/topics/2026/2026-09-25-area09-s10.md 의 세부영역 링크 9개(1절 1개, 3절 8개)를 주제 페이지 위치 기준 ../../categories/<대분류 slug>/<파일>.md 경로로 고쳤다. 세부영역 페이지 9절의 오탈자 '이이종'을 '이종'으로 고치고, 세부영역 페이지 프런트매터 sources 를 남은 본문 각주 정의(11건)와 일치시켰다. 주장·태그·각주 내용은 바꾸지 않았다.
- 2차: 9절 표 '시설·설비 제어' 행 — 'ROP가 직접 맡는 것' 칸을 '로봇 작업과 설비를 잇는 별도 인터페이스. [추정][^ref-031][^ref-258][^ref-105][^ref-260]'과 별도 문장 'VDA 5050은 AGV·관제와 주변 설비 사이 인터페이스를 다루지 않는다. [사실][^ref-267]'로 나눴다.
- 2차: 8절 요약 문장 — 세부영역 페이지 8절과 주제 페이지 2026-09-25-area09-s8 의 1절 첫 항목·3절 첫 문장을 'VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실][^ref-267]'과 태그·각주 없는 '이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.'로 바꿨다(이종 플릿 중앙 제어 구조는 3절 목록의 ref-268 항목에 이미 [사실][^ref-268]로 있어 요약에서는 뺐다).
- 2차: 주제 페이지 2026-09-25-area09-s10 3절 '12. 명령·작업 실행의 신뢰성' 항목의 태그를 [사실]에서 [추정]으로 바꿨다(각주 [^ref-031] 유지).
- 2차: 세부영역 페이지 9절 마지막 단락 free_fleet 문장 끝에 [추정][^ref-264]를 붙이고, 13절에 ref-264 각주 정의(주제 페이지 s6 의 정의 줄 그대로, 원문 미열람 표기 없음)를 더했으며, 프런트매터 sources 에 ref-264 를 넣고 reference_updates 의 ref-264 cited_by 에 세부영역 페이지를 더했다.
