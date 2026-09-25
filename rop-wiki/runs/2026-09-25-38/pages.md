# 스토리텔러 산출 2026-09-25-38

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/c-connectivity-and-execution-foundation/index.md | draft | '다른 대분류와의 연결' 절 신규 작성(A·B·D·E·F·G 대분류 연결 31건, 아직 다루지 않은 연결), 참고 자료 절에 각주 정의 41건 덧붙임 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | C. 연결·실행 기반 | 다른 대분류와의 연결 절 신규 작성(A·B·D·E·F·G 대분류 연결 31건, 27. AI·학습·적응과 모델 운영은 근거 없음), 조건부 승인 수정 15건 이행 | run 2026-09-25-38
- 홈 최근 업데이트: 2026-09-25 — C. 연결·실행 기반: 다른 대분류와의 연결 절 작성(작업 요청 번역·변경·취소, 능력·좌표·적재물·상태 모델, 교통·충전·구역 점유, 예외·인계, 시뮬레이션·적합성 시험·수명주기, 안전·보안·표준 제약)
- 대분류 최근 업데이트: 2026-09-25 — C. 연결·실행 기반: 다른 대분류와의 연결 절 신규 작성(A. 업무·공급망 설계부터 G. 안전·보안·지능·거버넌스까지 여섯 대분류, 27. AI·학습·적응과 모델 운영은 아직 다루지 않은 연결로 표시)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 인클레이브 | Enclave (SROS 2) | SROS 2 에서 같은 신원과 접근통제 규칙을 공유하는 프로세스 또는 프로세스 묶음으로, 보안 인증서·권한 파일을 이 단위로 발급·적용한다. | 26, 11, 10 | ref-798, ref-009 |
| new | 적합성 시험 | Conformance Test | 구현이 표준·명세가 정한 메시지 형식과 동작 규칙을 지키는지 정해진 시나리오로 확인하는 시험이다. | 23, 9, 28 | ref-800 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 오픈소스 문서 | high | https://design.ros2.org/articles/ros2_dds_security.html |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://doi.org/10.1177/20552076261437181 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 표준 | medium | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | medium | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 오픈소스 문서 | medium | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_lifts.html |
| ref-285 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 표준 | medium | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 오픈소스 문서 | medium | https://github.com/kubeedge/kubeedge |
| ref-310 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 논문 | medium | https://dl.acm.org/doi/10.1145/564585.564601 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 정부·연구기관 | medium | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 |
| ref-316 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 기사 | low | https://www.ctman.kr/35296 |
| ref-317 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 기사 | low | https://www.electimes.com/news/articleView.html?idxno=320147 |
| ref-364 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 오픈소스 문서 | high | https://design.ros2.org/articles/node_lifecycle.html |
| ref-365 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json |
| ref-367 | IETF HTTPAPI Working Group (Jena, J., & Dalal, S.) | The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) | 표준 | medium | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md |
| ref-374 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_ros2/issues/224 |
| ref-798 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-799 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-800 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 오픈소스 문서 | medium | https://github.com/gpue/vda5050-sim |
| ref-801 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 오픈소스 문서 | medium | https://github.com/ekusiadadus/vda5050-lab |
| ref-802 | 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인) | 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? | 9, 23, 28 | 열림 | — |
| new | — | 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? | 10, 26 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 다른 대분류와의 연결 절 '아직 다루지 않은 연결': 27. AI·학습·적응과 모델 운영이 9. 로봇·제조사 관제 연동~12. 명령·작업 실행의 신뢰성과 잇는 근거(예: 학습 기반 이상 탐지·배정이 관제 연동 데이터를 쓰는 사례)가 없어 서술하지 못했다.
- 다른 대분류와의 연결 절: 18. 사람–로봇 협업·운영 인터페이스와 4. 성과·경제성·프로세스 개선이 C. 연결·실행 기반 세부영역과 이어지는 근거(운영자 개입 명령 경로, 연동 오류가 성과 지표에 주는 영향)를 조사하지 않았다.
- G. 안전·보안·지능·거버넌스 연결: VDA·VDMA 공식 적합성 시험·인증 절차의 유무를 1차 출처로 확인해야 f30 추정을 사실로 정리할 수 있다.
- G. 안전·보안·지능·거버넌스 연결: 대한승강기협회 엘리베이터–로봇 연동 단체표준의 원문·발행일(1차 출처)을 확인해야 [추정]으로 둔 문장을 정리할 수 있다.
- G. 안전·보안·지능·거버넌스 연결: ISO 21423 의 발행 완료 여부와 발행일을 확인해야 한다.

## 이행한 수정 지시

- 차등 갱신 — '다른 대분류와의 연결' 절만 patches(replace)로 바꾸고, 새 각주 정의 41건은 '참고 자료' 절에 append 로 덧붙였으며 기존 ref-004 정의는 다시 넣지 않았다.
- f31 강등 — 대한승강기협회 단체표준 문장을 [추정]으로 쓰고 '기사 보도 기준, 단체표준 원문·발행일 미확인'을 같은 문장에 병기했다.
- f5 — 인증 모델 구성(4개 분야 28개 항목, 총점 176점, 2023년)만 [사실]로 쓰고 공동주택 대상·물류센터 아님을 병기했으며, 3. 처리능력·거점·설비 계획과 10·11 세부영역을 잇는 해석은 별도 문장의 [추정]으로 나눴다.
- ref-802 — 각주와 reference_updates 의 발행일을 2023 으로, 기관·제목에 '지적과 국토정보 53(1), 83-105'를 반영하고 각주 접근일 뒤에 ' (원문 미열람)'을 붙였다.
- f15 — 해제 구역 허가·대기·철회·거절 응답과 승강기 세션 점유를 [사실]로 쓰고, '공용 자원으로 예약·배분하는 입력'은 별도 문장의 [추정]으로 나눴다.
- f24 — 'README 에 적는다' 형식을 유지하고 바로 뒤 문장에 두 도구가 개인 프로젝트이며 VDA·VDMA 공식 적합성 시험이 아님을 병기했다.
- f29 — ISO 21423 을 '개발 중인 국제표준(검색 결과상 FDIS 단계, 발행 여부 미확인)'으로 표기하고 ref-159 각주에 ' (원문 미열람)'을 붙였다.
- f26 — KS B 7317·승강기 운영 모드 문장 뒤에 ROP 는 운영 모드 확인과 작업·경로 제약 반영만 맡고 탑승 안전·설비 안전 제어는 분류 원문 9장 '시설·설비 제어' 경계의 연계 대상임을 적었다.
- f4 — 병원·호텔 사례이며 물류센터 적용 미확인(oq-010)을 적고, 승강기 제어 자체는 연계 대상이며 3. 처리능력·거점·설비 계획은 제약 입력으로만 받는다고 썼다.
- f23 — 시뮬레이션 세계 생성·lift_supervisor 재현은 22. 시뮬레이션·예측용 디지털 트윈 항목으로, 배치 전 시험은 23. 시험·형식 검증·벤치마크 항목으로 나눴고, 8. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 구분한다고 밝혔다.
- 원문 미열람 표기 — 지시된 fetched=false 출처 33건의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 원문을 연 ref-009·023·031·364·798·799·800·801(ref-004 는 기존 정의 유지)에는 붙이지 않았다.
- A·B 대분류 기존 연결 — f1·f2·f4·f7~f12·f14·f17 을 해당 페이지와 같은 태그·각주 id 로 쓰고, A. 업무·공급망 설계·B. 공통 정보·환경 모델 페이지의 '다른 대분류와의 연결' 절을 링크했다.
- 27. AI·학습·적응과 모델 운영 — '아직 다루지 않은 연결' 소절에 번호와 이름을 함께 적고 근거 부재를 밝혔으며, 다른 대분류·세부영역도 모두 문자·번호와 이름을 함께 썼다.
- 용어 링크 — 관리형 노드, 지도 정합, 승강기 어댑터, 해제 구역, 디스펜서·인제스터, 플릿 어댑터, DDS 보안 규격을 첫 등장 시 용어집에 링크했고, glossary_updates 에는 인클레이브와 적합성 시험만 신규로 넣었다.
- 직접 인용 — ref-031 에서 짧은 구절 한 번(f20)만 인용하고, ref-798 을 포함한 나머지는 재서술했다.
