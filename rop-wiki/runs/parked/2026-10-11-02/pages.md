# 스토리텔러 산출 2026-10-11-02

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/integration/business-system-integration.md | draft | 차등 갱신: 3절 GreenAuto REST·MQTT 서술 정정(미래 확장·미가동)과 상태 조건 문단, 4절 OPC Job Control 상태별 메서드, 5절 국내 문단 1차 출처 병기·제조 공장·병원 사례 추가, 6절 응답·취소 결과 분리·우선순위 허용 상태·업무 객체 해석·MCP 범위, 7절 표준·API 표, 8절 서지 정정·적용 조건, 9절 경계 보강, 10절 연결 8건 추가, 11절 질문 id·부분 근거·새 질문, 13절 각주 갱신 |

## 변경 이력·색인

- 변경 이력: 2026-10-11 | 23. 업무 시스템 연동 | 차등 갱신: OPC Job Control 상태별 변경·취소, 응답과 취소 결과 통지 분리, 우선순위 변경 허용 상태·정렬, MCP 도구 범위, 제조 공장·병원 사례 추가, GreenAuto REST·MQTT 서술 정정(미래 확장·미가동), 국내 발표 1차 출처 병기 | run 2026-10-11-02
- 홈 최근 업데이트: 2026-10-11 — 23. 업무 시스템 연동: 작업 지시 상태별 변경·취소 규칙, 취소 응답과 실제 취소 결과의 구분, 제조 공장·병원 사례를 더하고 GreenAuto 연동 서술을 원문 기준으로 정정했다
- 대분류 최근 업데이트: 2026-10-11 — 23. 업무 시스템 연동: OPC Job Control·Open-RMF 응답 스키마·SAP·Oracle API 근거로 4·6·7·9절을 보강하고 제조 공장·병원 사례와 연결 8건을 더했다
- 세부영역 최근 업데이트: 2026-10-11 — 23. 업무 시스템 연동: 3~11·13절 차등 갱신(GreenAuto 정정, OPC Job Control 상태, 응답·취소 결과 분리, 우선순위 허용 상태, MCP 범위, 제조 공장·병원 사례, 열린 질문 부분 근거)

## 용어집 갱신

- 없음

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-131 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 표준 | high | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 논문 | high | https://www.mdpi.com/2076-3417/15/13/7235 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 논문 | high | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 |
| ref-1453 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json |
| ref-1454 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json |
| ref-1455 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json |
| ref-1456 | SAP | APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated)) | 벤더 문서 | medium | https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf |
| ref-1457 | Oracle | WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c) | 벤더 문서 | medium | https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html |
| ref-1458 | SAP | End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308) | 벤더 문서 | medium | https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf |
| ref-1459 | 아르고 풀필먼트(테크타카) | 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시 | 벤더 문서 | medium | https://blog.argoport.com/pr-robotcooperation250121 |
| ref-1460 | LG CNS | 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다 | 벤더 문서 | medium | https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1 |
| ref-1461 | SAP Architecture Center | Warehouse Pick & Place with Embodied AI Robotics | 벤더 문서 | medium | https://architecture.learning.sap.com/docs/ref-arch/7e4168 |
| ref-1462 | SAP (Lukasz Ostrowski, SAP News Center) | How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases | 벤더 문서 | medium | https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/ |
| ref-1463 | robotmcp | demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README | 오픈소스 문서 | high | https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md |
| ref-1341 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 오픈소스 문서 | high | https://github.com/nvidia-isaac/isaac_mission_dispatch |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 아르고(테크타카)–플로틱 남이천 물류센터 협력(오더 피킹 로봇 30대 지원 발표) 이후 실증의 시험 기간·성공 기준·완료 결과가 공개됐는가? | 23, 61 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 수행 자원 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |
| 물류창고 | 예외·성과 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |
| 제조 공장 | 작업 대상 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |
| 제조 공장 | 수행 자원 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |
| 병원 | 수행 자원 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |
| 병원 | 완료·인계 | docs/categories/integration/business-system-integration.md#5-적용-사례-현장-유형-명시 | 23. 업무 시스템 연동 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF 작업 배정·취소 응답 스키마(rmf_api_msgs dispatch_task_response·cancel_task_response·simple_response) | 오픈소스 | Open Robotics (open-rmf) | 23, 20, 29 | ref-1453 | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json |

## 추가 조사 요청

- 형식 검증 오류(재작성 요청) 대응 — 리서치·1차 검증·pipeline 담당 요청: 퍼블리셔 사전 검사가 반려한 항목은 모두 research.json 의 finding f10·f11·f12·f13·f15·f16·f17·f30 에 vendor_claim 표시가 없다는 것(6.2 항목 13)이며, 스토리텔러 출력(pages.json)이 아니라 리서치 브리프의 필드다. 스토리텔러는 research.json 을 고칠 수 없고, 재작성 지시도 '내용(주장·태그·각주·판정)은 바꾸지 말라'고 하므로 이번 재작성은 이전 원고와 같은 내용·태그로 다시 냈다. 따라서 이 재작성만으로는 같은 검사가 다시 실패한다. 해결 방법은 둘 중 하나다: (1) 리서치 재실행 또는 pipeline 이 research.json 의 해당 finding 에 vendor_claim: true 를 넣고 1차 검증이 태그 처분을 다시 내린다(유지 또는 [추정] 벤더 주장으로 강등). 강등되면 다음 스토리텔러 재실행에서 3·6·7·9·11절의 해당 문장(SAP Warehouse Robotics FMS·integration services, Oracle Change Task Priority, SAP 참조구조)을 '[추정] 벤더 주장'으로 고친다. (2) 1차 검증이 '인터페이스·참조구조 문서 내용에 관한 진술'로 [사실] 유지를 판정한 finding 을 6.2 항목 13 의 예외로 인정하도록 검사 규칙을 정한다(사용자 결정 항목).
- 2026-09-25-area01-s3·s8 주제 페이지 직접 정정 필요 — 두 페이지의 본문이 이번 입력에 없어 s3 39행 GreenAuto 문장과 s8 42행 GreenAuto 항목(저자 '미확인' 포함)을 그 자리에서 고치지 못했고, s8 43행 머니투데이 항목에도 1차 출처 ref-1459 를 병기하지 못했다. 세부영역 3·8절에 정정 문장을 넣어 두었으므로, 다음 실행에서 두 주제 페이지를 입력으로 받아 patches 로 해당 줄을 'MES·ERP 용 REST API, AMR 실시간 이벤트·IIoT 용 MQTT broker, VDA 5050 연동은 미래 확장 계획(당시 미가동)'으로 바꾸고 각주 ref-136 정의를 갱신해야 한다(예산 page_updates 2 도 함께 고려).
- oq-021·oq-046 보강(6·9절): 취소 응답과 실제 정지 사이의 시간 관계, 중복 취소 요청의 효과, SAP Warehouse Robotics 현재 권장 연동 경로의 API 계약과 폐기 FMS API 의 대체 관계 — 폐기 문서만으로는 현재 계약을 서술할 수 없다.
- oq-020 보강(4·7절): ISA-95 JobOrderID·JobResponse 와 VDA 5050 orderId·Open-RMF booking.id 의 공개 매핑 명세나 구현.
- 1차 검증이 다음 해당 실행으로 넘긴 질문: Yu·Srinivas(2025) 동적 주문 피킹 논문 원문으로 기존 AOCT·ATT·AWTD 결과 서술과 서지(권·호·쪽)를 재검증(26. 작업 순서·스케줄링 연계), ISA-95 Part 1(ANSI/ISA-95.00.01-2025) 본문의 바뀐 조항과 Job Control 2.0·B2MML 관계(21. 상호운용 표준·적합성 연계) — 이번 브리프에 근거 finding 이 없어 열린 질문으로 등록하지 않았다.
- 채팅 기반 구성·운영 트랙 반영 제안 2026-09-25-37 두 건(7절: Job Control 작업 지시의 선택 필드·종료 시각·우선순위를 채팅 지시 기한의 원천으로 쓰는 문제, 6절: Mecalux Easy WMS 대화형 비서의 실행 전 확인 사례)은 이번 브리프에 근거 finding 이 없어 반영하지 않았다. 다음 23. 업무 시스템 연동 실행에서 원문 확인이 필요하다.
- 5절 병원·제조 공장 사례의 빈 칸(시작 조건·제약·예외·성과): Tartu 병원 시험의 운반 요청 발생 방식과 실패 처리, LG CNS 사례의 생산계획 변경 승인 규칙·주문 상관키에 대한 1차 근거.

## 이행한 수정 지시

- f6·f14·f18·f26·f36 구축자 의견 명시 — 6절(f6·f14·f18·f36), 8절(f26), 3·9절의 [의견] 문장을 모두 ‘구축자 의견으로는’으로 시작하고 근거 finding 의 출처 각주(ref-131, ref-1456·ref-1453·ref-1454, ref-1457·ref-1458, ref-133, ref-1341·ref-1463)를 붙였다.
- f22 GreenAuto 정정 — 주제 페이지 2026-09-25-area01-s3·s8 본문이 이번 입력에 없어 해당 줄을 직접 패치하지 못했다. 대신 세부영역 3절에 ‘정정(2026-10-11)’ 문단으로, 8절에 GreenAuto 항목으로 ‘MES·ERP 용 REST API, AMR 실시간 이벤트·IIoT 용 MQTT broker, VDA 5050 연동은 미래 확장 계획(당시 미가동)’을 [사실][^ref-136]으로 넣고 주제 페이지 서술이 원문과 다르다고 밝혔으며, 주제 페이지 직접 수정은 additional_research_requests 에 요청했다.
- ref-136 — reference_updates 의 기관을 ‘Lopes, D., Pereira, T., Gonçalves, A. 외(저자 17명; Applied Sciences, MDPI)’, 발행일을 2025-06-27 로 고쳤고, 13절 각주 정의를 같은 값으로 새로 두되 ‘(원문 미열람)’을 붙이지 않았다(source_unopened: false).
- ref-131 — 13절 각주 정의를 발행일 2024-01-31, 접근일 2026-10-11, 원문 미열람 표시 없이 두었고, 프런트매터 sources 에 ref-131 을 다시 넣었다(3·4·6·7·11절에서 인용).
- f11 — 6절에서 ‘시스템 설계를 단순하게 하려고’라는 목적 문구를 빼고 ‘FMS 가 요청에 대한 응답을 관련 콜백 메서드 호출보다 먼저 돌려주도록 요구한다(요청 → 응답 → 콜백 순서)’만 썼다.
- f10·f17 — 6·7절에서 제품명을 ‘SAP Warehouse Robotics(SAP BTP 기반)’로 쓰고 SAP EWM 과 다른 제품임을 밝혔으며, FMS 연동 API(ref-1456)는 폐기(Deprecated) 문서로 현재 권장 계약이 아니고 integration services 경로(ref-1458)는 그와 다른 연동 경로임을 본문과 7절 표에 적었다.
- f15·f16 — ref-1457 각주를 확인된 제목과 26c URL 로만 쓰고 문서 ID G55063-04 는 넣지 않았으며, 발행일 자리에 ‘2026-08-14(페이지 메타데이터 기준)’을 병기했다.
- f23~f25 — 8절 Lorenz 외 항목에 학술지판 쪽수를 쓰지 않고 §2·§4·§4.1·§4.2 절 번호만 썼으며, 주제 페이지의 기존 결과(점근적 최적성) 서술은 유지한다고 밝히고 적용 조건만 덧붙였다.
- f27·f28 — 5절 국내 문단의 기존 [사실][^ref-137] 문장 뒤에 1차 출처 [^ref-1459] 문장을 병기하고, f28 의 ‘20분 이상→10분 이내’를 [추정] 벤더 주장으로 쓰며 ‘앞선 실증의 성과이며 남이천 30대 사업 결과가 아님’을 함께 적었다. 주제 페이지 s8 43행은 입력에 없어 세부영역 8절에 1차 출처 항목을 두었다.
- f29 — 5절 제조 공장 사례를 [추정] 벤더 주장으로 쓰고 WCS·SCADA 통합 관제를 연계 대상으로 짧게 다뤘으며(9절 시설·설비 제어 행과 문단), 10절에 22. 설비·건물 시스템 연동과 38. 모니터링·이상 탐지·원인 분석 연결을 더했다.
- f30·f31 — 6절에서 두 자료를 업무 객체 해석 계층의 예로만 쓰고 휴머노이드 작업 수행은 44. 로봇 기반 모델·언어 모델 계획으로 넘겼으며 10절에 44번 연결을 더했다. f31 은 [추정] 벤더 주장으로 ‘탐색 단계, 전용 beta·test 시스템 환경 검증, Anigon 1대’를 병기했고 각주 발행일은 2025-11-05 만 썼다.
- f33~f36 — 6·9절에서 MCP 도구 범위를 업무 요청 접점 판단으로만 다루고 공개 코드를 다사업자 WMS 운영 검증으로 쓰지 않는다고 밝혔으며, 승인된 계획만 실행하는 문제는 12. 채팅으로 업무 지시·오케스트레이션으로 넘기고 10절에 연결했다.
- f37·f38 — 5절 병원 사례에서 ingestor 를 ‘인제스터(디스펜서·인제스터)’로 쓰고 용어집 dispenser-ingestor 링크를 달았으며, 도착과 인수 확인 분리를 ‘완료·인계’ 칸에, ‘TIAGo 1대 실증·TIAGo·Jackal 이기종 관리는 별도 시험 환경’을 ‘수행 자원’ 칸에 두었다.
- 5절 적용 사례 — 새 사례마다 현장 유형(물류창고 국내 사례·제조 공장·병원)을 밝히고 근거 있는 칸만 채웠으며 나머지는 ‘확인되지 않음/다루지 않음’으로 두었고, site_matrix_updates 를 물류창고(수행 자원·예외·성과), 제조 공장(작업 대상·수행 자원), 병원(수행 자원·완료·인계)으로 실제 채운 칸과 일치시켰다.
- 직접 인용 — 어느 출처도 원문을 직접 인용하지 않고 모두 재서술했다(ref-131·ref-1456 포함).
- open_questions_new — 1번(아르고–플로틱 실증 결과)만 open_question_updates 에 new 로 등록했고, 2번(Yu·Srinivas 재검증)과 3번(ISA-95 Part 1 2025 조항)은 등록하지 않고 additional_research_requests 로 넘겼다.
- open_questions_resolved 없음 — 11절에서 oq-019·oq-020·oq-021(관련 oq-351)·oq-012·oq-046·oq-141·oq-365 를 모두 ‘상태: 열림’으로 두고 부분 근거와 각주만 적었으며, oq-002 는 ‘이번 실행에서 새 근거 없음’으로 두었다. 상태 변경 update 는 내지 않았다.
- 트랙 반영 제안 — 2026-09-25-77 제안은 7절 OPC Job Control 행에 f1·f3 범위(시작 전 Update, Stop→Ended, Abort→Aborted)로만 반영하고 ref-681·‘원문 미열람’ 표기는 쓰지 않았다. 2026-09-25-37 의 두 제안은 반영하지 않고 additional_research_requests 에 근거 필요로 적었다.
- reference_updates — 신규 출처 ref-1453~ref-1463 11건을 모두 등록하고 source_unopened: false 를 유지했으며, 발행일을 모르는 ref-1453·ref-1454·ref-1455·ref-1463·ref-1341·ref-1461 은 published null, 각주 발행일 자리에 ‘미확인’을 썼다.
