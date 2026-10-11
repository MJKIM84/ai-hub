---
area: 23
title: "23. 업무 시스템 연동"
researched: 2026-10-11
researcher: "OpenAI Codex"
---

# 23. 업무 시스템 연동 — 보완 조사

## 요약

- OPC Job Control의 Update·Cancel·Stop·Abort를 상태별로 구별하고, 작업 완료와 후처리 종료를 분리한다. 표준 간 자동 매핑은 확인하지 못했다.[^n1]
- Open-RMF의 요청 응답·작업 상태·phase별 취소 반응과 SAP의 과거 FMS 콜백 계약을 보강한다. 요청 성공을 재고 확정으로 확대하지 않는다.[^n2][^n3][^n4]
- GreenAuto의 MES·ERP용 REST/MQTT와 VDA 5050은 미래 확장 설계였다. Lorenz 연구는 단일 피커 모델의 분석·계산실험이며 현장 연동 검증과 구별한다.[^n9][^n10]
- 국내 발표는 공급자 설명으로 제한한다. 2026년 SAP 참조구조와 NVIDIA MCP 코드는 최근 변화로 기록하되, 다사업자 WMS 재고 처리가 검증됐다고 결론 내리지 않는다.[^n8][^n11][^n14]

조사 범위는 상위 업무 지시·상태·확정과 로봇 관제 사이 경계다. API 계약의 [사실]은 문서/코드에 정의된 구조를 뜻한다. 공급자의 현장 구축·성능 주장은 [추정]으로 구별한다. 보완 항목의 K번호와 사실 문장의 F번호는 이 문서의 검증용 식별자다. 최종 제출 전 재대조 기록은 부록 D에 있다.

## 보완 항목

### [4. 주요 개념·용어 / 6. 대표 접근법] — 추가 (K01: OPC 작업 변경·종료 조건)

- 새 내용 F01: OPC 10031-4 v2.00.0의 Update는 아직 시작하지 않은 작업 지시의 기존 정보를 새 정보로 전부 교체한다. [사실][^n1]
- 새 내용 F02: Cancel은 AllowedToStart 또는 NotAllowedToStart 작업을 취소하고 저장 정보를 제거한다. [사실][^n1]
- 새 내용 F03: Stop이 성공하면 작업은 Ended 상태여야 한다. [사실][^n1]
- 새 내용 F04: Abort가 성공하면 작업은 Aborted 상태여야 한다. [사실][^n1]
- 새 내용 F05: Ended의 Completed는 실행이 끝난 상태이고, Closed는 후처리도 더 수행하지 않는 상태다. [사실][^n1]
- 근거 메모: §6.2.1.9~12, §6.2.4 표45. 원문 발췌는 D의 E01~E04. 단일 규격 근거다. 기존 메서드 목록·Pause/Resume/Abort 설명을 다시 나열하는 대신 Update의 전부 교체, Cancel의 시작 전 조건, 완료·후처리 구분을 추가한다.
- ROP 시사점: 업무의 ‘취소’를 단일 로봇 명령 이름으로 변환하기 전에 현재 상태, 제거할 기록, 유지할 이력, 실행 종료 후 처리 여부를 결정해야 한다. [의견]
- 한계: 이 상태와 WMS 입고 확정 또는 VDA 5050 상태가 같다는 주장은 하지 않는다. 표준화된 매핑은 U01로 남는다.

### [6. 대표 접근법 / 7. 표준·프레임워크] — 추가 (K02: RMF 요청과 상태 계약)

- 새 내용 F06: 고정 커밋의 task_request.priority는 fleet이 지원하는 우선순위 스키마와 맞아야 한다. [사실][^n2]
- 새 내용 F07: dispatch_task_response의 성공 분기는 success와 state를 필수로 요구한다. [사실][^n2]
- 새 내용 F08: cancel_task_request는 type과 task_id를 필수로 요구한다. [사실][^n2]
- 새 내용 F09: cancel_task_response는 simple_response를 참조하고, 작업의 canceled·completed 상태는 task_state의 별도 열거값이다. [사실][^n2]
- 근거 메모: task_request.json /properties/priority; dispatch_task_response.json /oneOf/0/required; cancel_task_request.json /required; cancel_task_response.json /$ref; task_state.json /$defs/status. E05~E08. 동일 RMF 프로젝트의 파일 묶음이며 독립 교차 확인은 아니다. 위키의 상태 목록·priority 존재 자체는 이미 있으므로 재추가하지 않는다.
- ROP 시사점: 업무 주문 키와 RMF booking.id/task_id의 대응, 취소 요청 응답, 후속 상태 관측을 분리해 저장하는 것이 좋다. [의견]
- 한계: 스키마만으로 취소 응답과 실제 정지의 시간 관계, 중복 요청 효과, WMS 재고 확정을 보장할 수 있는지는 확인 못 했다. WMS 납기·운송 마감에서 fleet 우선순위로 변환하는 정책도 미확인이다.

### [6. 대표 접근법 / 9. 책임 경계] — 추가 (K03: RMF 취소 후 반응의 구현 위치)

- 새 내용 F10: rmf_task README는 각 phase에서 취소·중단에 대한 로봇의 반응을 사용자가 지정할 수 있다고 설명한다. [사실][^n3]
- 근거 메모: 고정 커밋 README Usage; E09. 실제 로봇 동작을 지시하는 Active 구성요소는 fleet adapter 쪽에 둔다는 문맥까지 읽었다. n2와 같은 프로젝트여서 독립 증거로 합산하지 않는다.
- ROP 시사점: 적재 전·적재 후·인계 후 단계마다 반송 목적지와 사람 확인 조건을 상위 업무 규칙으로 명시하고, 해당 단계의 반응에 연결하는 구성을 검토할 수 있다. [의견]
- 한계: README는 국내 WMS의 재고 취소 권한이나 회계 반제 규칙을 제시하지 않는다. 이를 자동 보상 기능이 완성됐다는 근거로 사용하지 않는다.

### [4. 주요 개념·용어 / 6. 대표 접근법] — 추가 (K04: 과거 SAP FMS API의 응답·콜백 구분)

- 새 내용 F11: SAP의 2024-07-10 FMS 연동 문서는 해당 API를 Deprecated로 표시한다. [사실][^n4]
- 새 내용 F12: 그 문서는 요청 응답을 관련 콜백보다 먼저 반환하도록 요구한다. [사실][^n4]
- 새 내용 F13: 그 계약에서 취소 성공은 CANCELLED 작업 상태로 통지하고, 취소 불가는 별도의 취소 상태 API로 통지한다. [사실][^n4]
- 근거 메모: 표지·§1, §1.5 pp7~8, §1.6.2 p12; E10~E12. §1.3에는 messageId, §1.6.1 예제에는 robotTaskId가 있어 메시지와 작업 식별 계층도 구분된다. 실제 운영의 exactly-once 보장이나 새 API의 계약으로 해석하지 않는다. 공급자 공식 문서 한 곳의 명세이며 독립 실증은 없다.
- ROP 시사점: 인터페이스 비교표에 ‘접수 응답’, ‘진행 통지’, ‘취소 결과’, ‘업무 확정’을 별도 열로 두는 것이 좋다. [의견]
- 한계: 이 문서는 과거 계약의 구체적 예시다. 최신 시스템에 적용할 문서와 중복·재시도 계약은 U09로 남긴다.

### [5. 적용 사례 / 6. 대표 접근법] — 추가 (K05: WMS 우선순위 변경의 허용 범위)

- 새 내용 F14a: Oracle WMS 26c Change Priority 문서는 Ready·Held·Created 상태의 작업을 변경 대상으로 명시한다. [사실][^n5]
- 새 내용 F14b: 그 API에는 Task/Change task priority 권한이 필요하다. [사실][^n5]
- 새 내용 F15: SAP Integration Services 경로의 2308 문서는 최적화를 끄면 큐 순서를 따르고, 큐 안의 주문은 latest starting date가 있으면 이를 기준으로 정렬한다고 설명한다. [사실][^n18]
- 근거 메모: Oracle 도입 문단·Task ID/Task Number 절, SAP §2 p4; E13~E14. 두 업체는 독립이지만 서로 다른 제품의 계약이므로 동일 기능의 교차 확인은 0건이다. Oracle 문서의 26c는 판 식별자이며 발행일로 환산하지 않았다. SAP n18은 n4의 FMS API와 다른 Integration Services 경로다.
- ROP 시사점: 우선순위 변경 가능 여부를 업무 작업의 상태와 로봇 실행 단계에 대해 따로 검사하는 것이 좋다. 대기열 재정렬과 진행 중 작업 선점은 별도 정책으로 정해야 한다. [의견]
- 한계: 이것으로 RMF 진행 중 작업의 재정렬 방법이 답해지지는 않는다. 업체 간 우선순위 숫자의 동등성도 검증하지 않았다.

### [4. 주요 개념·용어 / 9. 책임 경계] — 추가 (K06: 업무 입고와 물리적 이동의 의미)

- 새 내용 F16: GS1 CBV 2.0은 receiving을 특정 위치에서 물품을 받고 수취인의 재고에 추가하는 업무 단계로 정의한다. [사실][^n6]
- 새 내용 F17a: 같은 표준은 arriving을 특정 위치에 도착하는 단계로 정의한다. [사실][^n6]
- 새 내용 F17b: accepting은 점유 또는 소유권이 바뀌는 단계다. [사실][^n6]
- 새 내용 F17c: unloading은 운송 수단에서 물품을 내리는 단계다. [사실][^n6]
- 근거 메모: §7.1.3 pp36·40·43; E15~E18. GS1 어휘 정의이며 특정 WMS 트랜잭션 API나 로봇 신호 명세가 아니다. n16과는 같은 GS1 계열이다.
- ROP 시사점: 로봇의 도착·하역 상태를 receiving으로 기록하기 전에 누가 재고 반영을 승인하는지 별도 계약을 두는 것이 좋다. 업무 규칙에 따라 어떤 이벤트를 쓸지 정해야 한다. [의견]
- 한계: receiving과 arriving/accepting의 상호 배타 규칙이 있으므로 모든 이름을 무조건 차례로 발행하는 보편 절차로 제시하지 않는다. 국내 운영 키·확정 대기 시간은 U04·U05로 남는다.

### [8. 대표 연구] — 수정 (K07: GreenAuto의 구현·미래 설계 구분)

- 대상 문장: “MES·ERP 에는 REST API 로 정형 데이터를 내주고” — 분리8 본문 네 번째 연구 문장의 짧은 발췌. 전체 대상은 보존본 wiki-s8.txt 14행.
- 새 내용 F18: Lopes 등의 논문 §5.2는 IIoT 연결이 당시 구현에서 아직 활성화되지 않았다고 명시한다. [사실][^n9]
- 새 내용 F19: 같은 문단의 MES·ERP REST API, MQTT broker, VDA 5050은 미래 확장 설계에 속한다. [사실][^n9]
- 새 내용 F20a: §4의 개발 대상은 두 AMR과 한 AGV다. [사실][^n9]
- 새 내용 F20b: §7은 시스템의 주된 역할을 제조사 API에서 얻은 위치·상태의 통합 감시로 한정한다. [사실][^n9]
- 근거 메모: pp6, 11 그림9 아래, 21~22; E19~E21. Stellantis 관련 연구팀의 자체 보고다. 서지의 저자 미확인을 David Lopes 외16명으로 보완한다. 논문이 정식 게재됐다는 것과 업무 연동 기능이 가동됐다는 것은 다르다.
- 충돌·한계: §6.2는 최대20대 동시 감시를 보고하지만 §4의 개발3대와 어떻게 연결되는지, 실물/가상 구성·시험 기간·로그는 이번에 확인하지 못했다(U07). 20대를 MES·ERP 업무 연동 실증 규모로 쓰지 않는다.
- ROP 시사점: 위키 연구표에 ‘통합 감시 구현’, ‘상위 업무 인터페이스 설계’, ‘업무 확정 실증’을 별도 칸으로 두는 것이 좋다. [의견]

### [8. 대표 연구] — 추가 (K08: 재최적화 연구의 적용 조건)

- 대상 문장: “확률적 가정 아래 거의 확실하게 점근적 최적임을 보였고” — 분리8 본문 Lorenz 문장의 짧은 발췌. 전체 대상은 wiki-s8.txt 12행. 기존 결과를 부정하는 수정이 아니라 조건 추가다.
- 새 내용 F21: Lorenz·Otto·Gendreau의 OOBSRP 모델은 한 피커가 맡는 하나의 피킹 구역을 다룬다. [사실][^n10]
- 새 내용 F22: 로봇 카트 조건은 피커가 배치를 마치면 빈 로봇을 즉시 사용할 수 있다고 가정한다. [사실][^n10]
- 새 내용 F23: §4.1의 비교는 2,600개 생성 인스턴스의 계산실험으로 보고됐다. [사실][^n10]
- 근거 메모: §2 p160, §4~4.1 pp168~169, §5 pp171~172; E22~E24. 출판사와 대학 저장소 PDF는 같은 논문 한 출처다. 복수 피커·주문 납기 등의 확장은 향후 연구로 적혀 있다. 최적성 증명의 확률 조건을 현장 전체에 확대하지 않는다.
- ROP 시사점: 이 연구는 상위 계획 갱신 정책을 비교할 참고자료로 두되, 메시지 멱등성·재고 확정·VDA 실행 제약의 검증 근거로 사용하지 않는 것이 좋다. [의견]

### [5. 적용 사례 / 8. 대표 연구] — 수정 (K09: 국내 30대 발표의 1차 근거)

- 대상: 분리8의 테크타카·플로틱 협력 발표 문장(wiki-s8.txt 15행)과 본문5 국내 사례. 기존의 ‘실증 결과 미확인’ 단서를 유지한다.
- 새 내용: 아르고는 2025-01-21 발표에서 자사 WMS와 플로틱 로봇을 연결해 남이천에서 실증하고, 플로틱이 오더 피킹 로봇 30대를 지원한다고 밝혔다. [추정][^n7]
- 근거 메모: 발표 본문 협업·남이천 문단; E25. 기존 보도와 같은 사업이므로 새 사례 두 건으로 세지 않는다. 공식 발표 원문을 추가하는 보강이다.
- 충돌·한계: 같은 글의 20분→10분 미만 발언은 ‘앞서 실증사업’의 성과다. 남이천 30대 사업의 완료 성과로 합치지 않는다. 후속 결과, SSCC/EPCIS, 취소·재고 반영 규칙은 확인 못 했다.
- ROP 시사점: 국내 사례표에는 발표일, 지원 예정 규모, 시험 완료 여부를 분리해 기록하는 것이 좋다. [의견]

### [5. 적용 사례] — 추가 (K10: 제조 물류 WCS·SCADA 역할)

- 새 내용: LG CNS는 2026-07-16 고객 사례에서 HD현대일렉트릭 청주 배전캠퍼스 신공장에 WCS를 통한 자재 입고·보관·생산라인 공급·완제품 출하 조율과 SCADA 통합 관제를 구축했다고 설명한다. [추정][^n8]
- 근거 메모: Solution2, 발행일 표시; E26. 공급자 단독 사례이며 국내 제조 물류에 한정한다. ACR·AMR 구성 설명은 있으나 다제조사 수, API, 주문 상관키, 생산계획 변경 승인 규칙은 확인하지 못했다.
- ROP 시사점: 제조 시나리오에서 생산계획을 실행 작업으로 바꾸는 제어 역할과 상태를 보여 주는 관제 역할을 구분해 기술하는 것이 좋다. [의견]
- 한계: 보관 면적·작업량 성과 수치는 측정 조건을 검증하지 못해 채택하지 않았다. MES 또는 ERP의 특정 인터페이스가 공개됐다고 쓰지 않는다.

### [5. 적용 사례 / 7. 표준·프레임워크] — 추가 (K11: SAP Embodied AI의 문서와 시험 수준)

- 새 내용 F24: 2026-05-12 갱신된 SAP 참조구조는 업무 객체의 의미 이해를 창고 AI 에이전트의 능력 중 하나로 설명한다. [사실][^n11]
- 새 내용: SAP의 현재 뉴스 본문은 Bosch·Aimbo 사례에서 SAP EWM의 배송 정보·주문 우선순위·보관 위치를 이용한 단일 Anigon 로봇 개념검증을 소개한다. [추정][^n12]
- 근거 메모: n11 Key Components, n12 Enabling autonomous warehouse execution at Bosch; E27~E28. n12는 탐색 단계와 전용 beta/test 환경을 명시한다. 두 문서는 SAP 계열이며 독립 교차 검증이 아니다.
- 날짜 처리: 뉴스에 표시된 최초 날짜는 2025-11-05지만 현재 본문에는 후속 사례가 포함된다. Bosch 사례의 별도 실시일·문서 수정일은 미확인이다. ‘2025년11월에 모든 사례가 완료됐다’고 적지 않는다.
- ROP 시사점: 업무 객체를 물리 작업으로 해석하는 계층을 검토하되, 파일럿 결과와 생산 서비스의 지원 계약을 별도로 확인하는 것이 좋다. [의견]
- 한계: 이 자료는 다제조사 WMS 확정의 범용 제품 출시 또는 MCP 적용 증거로 사용하지 않는다.

### [7. 표준·오픈소스 / 6. 대표 접근법] — 추가 (K12: MCP 연결의 실제 코드 범위)

- 새 내용 F25a: NVIDIA Mission Dispatch 고정 README의 변경표는 2026-03에 Mission Dispatch MCP를 기록한다. [사실][^n14]
- 새 내용 F25b: 같은 변경표는 2026-08에 VDA5050 3.0 지원을 기록한다. [사실][^n14]
- 새 내용 F26: 해당 커밋의 MCP 서버는 로봇·미션 상태 조회, 로봇 등록, 좌표로 이동 미션을 보내는 도구를 등록한다. [사실][^n14]
- 새 내용 F27: 이동 미션 핸들러는 queries.py의 dispatch_move_mission을 호출하며, 이 함수는 mission REST 경로로 데이터를 보낸다. [사실][^n14]
- 새 내용 F28: 별도 robotmcp Tugbot README는 ROS2 Humble·Gazebo Fortress에서 자연어 이동·센서 조회를 하는 단일 로봇 시뮬레이션 예시를 설명한다. [사실][^n13]
- 근거 메모: n14 README Latest Update; server.py list_tools/_handle_dispatch_mission; queries.py dispatch_move_mission; MCP tutorial Requirements. n13 Introduction/Tested On/Sample Prompts; E29~E32. 각 저장소는 커밋 고정. 같은 프로젝트 파일은 한 출처다. 코드를 실행하거나 로봇을 제어하지 않았다.
- ROP 시사점: MCP를 업무 요청의 접점으로 평가할 때 주문 ID·허용 상태·승인·결과 대조를 별도 요구사항으로 두는 것이 좋다. [의견]
- 한계: NVIDIA의 일반 REST 미션 서비스와 MCP가 노출하는 도구는 범위가 다르다. MCP에서 WMS 주문 변경·재고 반제·전체 취소 API까지 제공한다고 쓰지 않는다. 공개 코드의 존재와 운영 검증을 구별한다(U10).

### [7. 표준·프레임워크 / 12. 갱신 이력] — 추가 (K13: 판·발행 상태 정리)

- 새 내용 F29: OPC 공식 목록의 현행 표시는 Job Control 2.00.0, 발행일 2024-01-31이다. [사실][^n1]
- 새 내용 F30: Job Control 2.0은 1.0과 호환되지 않는 변경을 포함하며 새 namespace를 정의한다. [사실][^n1]
- 새 내용 F31: ISA는 2025-04-10 발표에서 ANSI/ISA-95.00.01-2025의 발행을 알렸다. [사실][^n17]
- 근거 메모: OPC 공식 Version History·§1 Scope, ISA 발표 첫 문단; E33~E35. 기존 위키가 인용한 발표를 원문 확인한 보강이다. Part1 개정은 2025-10~2026-10의 최근1년 밖이므로 최근 개정으로 세지 않는다.
- 한계: ISA Part1 전체 본문은 열람하지 않았다(U11). 발표가 OPC Job Control·B2MML·VDA 매핑을 개정했다는 뜻은 아니다. 표준의 발행과 소프트웨어 배포·법령 시행을 섞지 않는다.

### [5. 적용 사례 / 9. 책임 경계] — 추가 (K14: 병원 인계 확인의 실물 예시)

- 새 내용 F32: Tartu 병원 연구의 시료 운반 절차에서는 실험실 도착 후 직원이 시료를 넘겨받고 배달을 확인한 다음 로봇이 ICU로 복귀했다. [사실][^n15]
- 새 내용 F33: 병원 내 운반 실증은 TIAGo로 했고, TIAGo·Jackal 두 이기종 로봇의 검증은 별도 시험 환경에서 이뤄졌다고 논문이 구분한다. [사실][^n15]
- 근거 메모: §3.1 그림8, §4의 Increasing the number and diversity of robots; E36~E37. 병원 인력의 인수 확인을 보여 주는 2022년 실물 사례다. WMS/ERP 재고 API 연동이나 병원 내 이기종 플릿 상시 운영 사례로 쓰지 않는다. 저자 자체 실증 보고 한 건이다.
- ROP 시사점: 비물류센터 현장에서도 ‘도착’과 ‘인수 확인’을 분리하는 업무 단계가 있는지 확인할 필요가 있다. [의견]

## 답한 열린 질문

질문은 원문 위치와 짧은 발췌로 식별한다. 전체 문장은 [보존본](.research-work/F-23/wiki-s11.txt) 11~15행에 있다. 아래 ‘부분 답변’은 원래 질문을 닫을 수 있다는 뜻이 아니다.

|질문 식별·발췌|판정|답변과 남은 부분|
|---|---|---|
|새1, 11행: “진행 중 작업을 재정렬하는 공개 설계나 사례”|부분 답변|WMS 상태별 변경 계약과 RMF priority 입력 조건은 확인했다. 납기→RMF의 진행 중 재정렬 정책은 확인 못 했다. [사실][^n2][^n5][^n18]|
|새2, 12행: “표준 매핑이나 공개 구현”|부분 답변|OPC 상태·메서드와 RMF 요청 계약을 확인했다. ISA95/B2MML→VDA/RMF 표준 매핑은 확인 못 했다. 단순 REST→VDA 연결을 그 답으로 세지 않는다. [사실][^n1][^n2][^n14]|
|새3, 13행: “되돌림 작업과 재고 반영”|부분 답변|phase별 취소 반응을 지정하는 지점과 과거 SAP 취소 콜백은 확인했다. 국내 적재 후 취소의 결정권·재고 반제 규칙은 확인 못 했다. [사실][^n3][^n4]|
|oq-002, 14행: “SSCC 라벨이나 EPCIS 이벤트”|미해결|GS1 Korea의 SSCC 설명은 물류단위 식별 정의다. 국내 로봇 결과 연결 운영 사례는 확인 못 했다.[^n16]|
|oq-012, 15행: “확정 대기 시간 기준”|부분 답변|CBV의 입고 의미와 해외 인계 확인 사례를 확보했다. 국내의 식별키·확정 대기 기준은 확인 못 했다.[^n6][^n15]|

관련 oq-014·oq-001은 새2와 연결된 질문이다. 이번 조사에서 이를 독립적으로 해결했다고 집계하지 않는다. 완전히 답한 질문은 0개다.

## 새로 생긴 열린 질문

|id|확인 못 한 내용·다음 검증 자료|
|---|---|
|U01|ISA95 JobOrderID·JobResponse와 VDA orderId·RMF booking.id의 공개 매핑 명세 및 상태 전이 시험 자료|
|U02|WMS 납기/운송 마감 변경이 진행 중 RMF 작업에 반영되는 승인 규칙·선점 비용·재정렬 구현|
|U03|국내 적재 후 취소 시 반송 목적지·재고 반제·부분 완료의 결정권자와 업무 규칙|
|U04|국내 로봇 적재·하역 결과에 SSCC/EPCIS를 연결하는 실제 메시지·운영 사례|
|U05|국내 WMS 입고/인수 확정의 상관키·시간 초과·수동 대조 기준|
|U06|남이천 30대 협력 발표 이후 시험 기간·성공 기준·완료 결과|
|U07|GreenAuto 개발3대와 최대20대 감시 시험 사이의 실물/가상 구성·기간·데이터|
|U08|Yu·Srinivas 2025 논문 원문, 실험 조건·서지 및 기존 위키의 AOCT/ATT/AWTD 결과 재검증|
|U09|SAP 현재 권장 연동 경로의 API 계약, 중복·재시도·이벤트 순서 보장 및 폐기 API의 정확한 대체 관계|
|U10|MCP를 거친 다사업자 WMS 주문/재고 처리의 생산 운영 결과·권한·실패 후 복구 시험|
|U11|ISA95 Part1 2025 규격 본문 조항 및 OPC/B2MML과의 관계 재검증|

확인 못 함 집계는 U01~U11의 11개 고유 항목이다. 동일 공백을 각 절에서 다시 언급해도 추가 집계하지 않는다. 이 조사에서 찾지 못했다는 기록이지 전 세계에 자료가 없다는 결론이 아니다.

## 출처

집계: 총 18개, 원문 열람 18/18, 1차 자료 18개, 독립 교차 확인된 동일 주장 0개. 기존 위키와 동일 문헌은 n1·n2·n9·n10·n17의 5개이며, 새 출처는 13개다. 기존 논문의 미러·새 커밋·규격의 다른 절은 새 문헌으로 세지 않았다. n7은 기존 2차 보도와 같은 사건이지만 새로 확인한 1차 문헌이다. 탈락 후보와 실패한 원문은 부록 C에 모두 남겼다. ‘원문 열람’은 관련 본문 열람이며 저장소 실행·현장 재현을 뜻하지 않는다. 접근일은 모두 2026-10-11이다.

[^n1]: OPC Foundation/ISA, *OPC UA for ISA-95 - Part 4: Job Control*, OPC10031-4, 2.00.0, 2024-01-31. [원문](https://reference.opcfoundation.org/specs/OPC-10031-4/full), [판 목록](https://reference.opcfoundation.org/specs/OPC-10031-4). 규격, DOI 없음. 원문 열람.
[^n2]: Open-RMF, *rmf_api_msgs schemas*: task_request, dispatch_task_response, cancel_task_request, cancel_task_response, simple_response, task_state. 커밋 `e9b7630c73a6fb41448ac143c0d7061f2b4389a2`, 커밋일2026-09-19(최초 발행일 미확인). [고정 스키마 폴더](https://github.com/open-rmf/rmf_api_msgs/tree/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas). 코드, DOI 없음. 원문 열람.
[^n3]: Open-RMF, *rmf_task*, README, 커밋 `3a6af296089e7faacb17609fa8c02bfd41133499`, 커밋일2026-09-25(최초 발행일 미확인). [고정 README](https://github.com/open-rmf/rmf_task/blob/3a6af296089e7faacb17609fa8c02bfd41133499/README.md). 구현 문서, DOI 없음. 원문 열람.
[^n4]: SAP, *APIs for Integration via Fleet Management Systems*, 문서일2024-07-10, 본문 *API for Integration with Fleet Management Systems (Deprecated)*. [공식 PDF](https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf). 제품 명세, DOI 없음. 원문 열람. LATEST URL이므로 이번 확보본의 날짜를 고정해 해석.
[^n5]: Oracle, *WMS REST API Guide—Change Priority*, 26c, 발행일 미확인. [공식 API 문서](https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html). 제품 명세, DOI 없음. 원문 열람.
[^n6]: GS1, *Core Business Vocabulary Standard*, Release2.0, Ratified2022-06. [공식 PDF](https://ref.gs1.org/standards/cbv/2.0.0/). 표준, DOI 없음. 원문 열람.
[^n7]: 테크타카/아르고 풀필먼트, *아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시*, 2025-01-21. [공식 발표](https://blog.argoport.com/pr-robotcooperation250121). 기업 발표, 판·DOI 없음. 원문 열람.
[^n8]: LG CNS, *로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다*, 2026-07-16. [고객 사례](https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1). 공급자 사례, 판·DOI 없음. 원문 열람.
[^n9]: David Lopes, Tiago Pereira, André Gonçalves, Francisco Cunha, Fernando Lopes, João Antunes, Victor Santos, Fernanda Coutinho, Jorge Barreiros, João Durães, Patrícia Santos, Fernando Simões, Pedro Ferreira, Elisabete Dinora Caldas de Freitas, João Pedro F. Trovão, João P. Ferreira, Nuno Miguel Fonseca Ferreira, *Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector*. Applied Sciences15(13),7235, 정식 게재본, 2025-06-27. DOI[10.3390/app15137235](https://doi.org/10.3390/app15137235), [출판사 PDF](https://mdpi-res.com/d_attachment/applsci/applsci-15-07235/article_deploy/applsci-15-07235.pdf). 원문 열람.
[^n10]: Catherine Lorenz, Alena Otto, Michel Gendreau, *Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?* Networks86(2),157–173, 정식 게재본, 최초 온라인 발행2025-05-01. DOI[10.1002/net.22281](https://doi.org/10.1002/net.22281), [대학 저장소 PDF](https://mediatum.ub.tum.de/doc/1835706/document.pdf). 원문 열람. 심사 승인2025-04-07과 발행일을 구분.
[^n11]: SAP Architecture Center, *Warehouse Pick & Place with Embodied AI Robotics*, 판 미표시, 갱신2026-05-12(adelyafatykhova), 최초 발행일 미확인. [참조구조](https://architecture.learning.sap.com/docs/ref-arch/7e4168). 제품 설계 설명, DOI 없음. 원문 열람.
[^n12]: Lukasz Ostrowski/SAP, *How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases*. 페이지 표시2025-11-05, 후속 수정일 미확인. [현재 공식 뉴스](https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/). 기업 발표, 판·DOI 없음. 원문 열람. 현재 본문의 사례 실시일을 최초 발행일로 추정하지 않음.
[^n13]: robotmcp, *Example 1: Tugbot Warehouse Simulation (Ignition Gazebo)*, demos-ros-mcp-server, 커밋 `edbc642849bdde1187771a15e557ec9e219184a5`, 커밋일2026-07-09(최초 발행일 미확인). [고정 README](https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md). 데모 문서, DOI 없음. 원문 열람.
[^n14]: NVIDIA, *Isaac Mission Dispatch* README, *Mission Dispatch MCP Tutorial (Cursor)*, MCP server.py·queries.py, 커밋 `56455eb757173cb6c0babe2e52cfb2a8e3a8bdee`, 커밋일2026-09-15. [고정 저장소](https://github.com/nvidia-isaac/isaac_mission_dispatch/tree/56455eb757173cb6c0babe2e52cfb2a8e3a8bdee), [MCP 코드](https://github.com/nvidia-isaac/isaac_mission_dispatch/tree/56455eb757173cb6c0babe2e52cfb2a8e3a8bdee/packages/agentic-utilities/mission-dispatch-mcp/src), [튜토리얼](https://github.com/nvidia-isaac/isaac_mission_dispatch/blob/56455eb757173cb6c0babe2e52cfb2a8e3a8bdee/docs/mcp_tutorial/README.md). 코드·문서, DOI 없음. 원문 열람. 최초 발행과 개별 기능 도입일은 README의 연월 표기까지만 사용.
[^n15]: Robert Valner, Houman Masnavi, Igor Rybalskii, Rauno Põlluäär, Erik Kõiv, Alvo Aabloo, Karl Kruusamäe, Arun Kumar Singh, *Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test*. Frontiers in Robotics and AI9:922835, Technology and Code 정식 게재본, 2022-08-23. DOI[10.3389/frobt.2022.922835](https://doi.org/10.3389/frobt.2022.922835), [논문 원문](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full). 원문 열람.
[^n16]: GS1 Korea, *SSCC(Serial Shipping Container Code) / 물류라벨*, 판·발행일 미확인. [공식 설명](https://www.gs1kr.org/front/std/appl/SSCC.asp). 기관 설명, DOI 없음. 원문 열람. 국내 로봇 실증의 출처로 세지 않음.
[^n17]: ISA, *Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems*, 2025-04-10. [공식 발표](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of). 개정 발표, DOI 없음. 원문 열람은 발표문을 뜻하며 유료 표준 본문은 미열람.
[^n18]: SAP, *End-User Information for Integration via Integration Services*, Document Version2308—2023-08-19. [공식 PDF](https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf). 제품 문서, DOI 없음. 원문 열람; 이번 확보본 기준.

## 부록 A. 1단계 진단표와 조사 질문

### A0. 진단 원문 보존과 발췌 위치

진단표의 각 행은 아래 보존본의 해당 절 문장을 대상으로 한다. 긴 원문을 반복 전재하지 않고 짧은 원문 발췌와 행 위치를 붙였다. 보존본 HTML·텍스트는 분석 전에 확보한 원문이며 문장을 고쳐 쓰지 않았다.

|진단 묶음|원문 그대로의 짧은 발췌|전체 문장·문맥|
|---|---|---|
|상위 매핑 미발견|“표준 매핑을 찾지 못했고”|[분리3 보존본](.research-work/F-23/wiki-s3.txt), 11행|
|B2MML 의미 공백|“동사별 의미 설명은 이 스키마 파일에 없다.”|[분리4 보존본](.research-work/F-23/wiki-s4.txt), 13행|
|취소·되돌림 추론|“되돌림 작업이 추가로 필요할 것으로 보인다.”|[분리6 보존본](.research-work/F-23/wiki-s6.txt), 15행|
|미열람 규격·판|“원문 미열람”|[분리7 보존본](.research-work/F-23/wiki-s7.txt), 출처59·69행|
|논문 저자 미확인|“게재 논문 저자(미확인)”|[분리8 보존본](.research-work/F-23/wiki-s8.txt), 38행; K07·K08의 대상 발췌도 참조|
|국내 사례·가상 시나리오|“창고 상위 시스템의 변경이 이런 형태로 올 수 있을 것으로 보인다.”|[본문 보존본](.research-work/F-23/wiki.txt), 33행; 적용 사례 절 전체|

분리 페이지의 실제 위키 주소는 `https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area01-s{절번호}/`이며 조사한 번호는3·4·6·7·8·11이다. 현재 본문은 [업무 시스템 연동](https://mjkim84.github.io/ai-hub/categories/integration/business-system-integration/)이다. 열린 질문 원문 보존 위치는 본문의 ‘답한 열린 질문’ 표와 연결된다.

### F-23 1단계 진단 — 2026-10-11

검색 전에 현재 본문 및 분리된 3·4·6·7·8·11절을 끝까지 읽었다. 본문 버전 2, 분리 페이지 버전 1, 표시 갱신일 2026-09-25. HTML과 추출문을 이 폴더에 저장했다. 아래는 짧은 인용과 위치·진단 요약이며 원문 전체는 각 스냅샷에 보존했다. 결론은 아직 내리지 않았다.

#### 약한 주장 목록

| 위치 | 대상 | 약한 이유·조사 방향 |
|---|---|---|
| 본문3·분리3 | VDA 범위에서 상위 번역 역할을 도출 | 단일 명세 뒤에 추론이 이어짐; 표준 범위와 설계 권고 분리 |
| 분리3 | ISA-95→VDA/RMF 표준 매핑 미발견 | 부재 증명 아님; Q1 |
| 분리3 | SCOR Order/Fulfill 정의 | 원문 미열람 단일 자료; 직접 로봇 연동과 구별 |
| 분리3·본문6 | 변경 수단에서 대기열·재계획 책임 도출 | 추정; 실행 인터페이스와 업무 결정 경계 Q1~Q3 |
| 본문5 시작 | B2MML·OPC 명령이 WMS에서 올 수 있음 | 규격 존재와 현장 사용 추정 혼합 |
| 본문5 자원 | 작업자·AMR 협업 연구 설정 | 논문 미열람; Q5 |
| 본문5 제약 | base 불변, 새 주문 거부, 우선순위 미발견 | 단일 규격·우선순위는 추정; 이 영역은 상위 변경 처리에만 한정 |
| 본문5 완료 | 로봇 상태와 상위 업무 완료의 연결 | RMF 스키마가 WMS 확정을 보장하는지 공백; Q2~Q3 |
| 본문5 예외 | 취소 불가 동작·적재 후 되돌림·교란 비용 | 규범·추론·미열람 연구 혼합; Q3·Q5 |
| 본문5 국내 | 테크타카·플로틱 30대 협력 발표 | 2차 보도, 결과 미확인; Q4 |
| 분리4 | VDA 주문 갱신 | 단일 명세·이미 있음; 상위 매핑 조건으로만 사용 |
| 분리4 | OPC 메서드·상태 전이 | 노드셋과 미열람 명세; Q1 |
| 분리4 | B2MML 동사, “동사별 의미 설명은 이 스키마 파일에 없다.” | 개별 파일로 전체 규격 의미를 판단하지 말 것; Q1 |
| 분리4 | RMF 상태·요청 필드 | 움직이는 main 스키마, 동작 보장과 차이; Q2 |
| 분리4 | 웨이브/웨이브리스 | 2010년 미열람 논문, 로봇 플릿 직접 근거인지 구별 |
| 분리6 | 취소·일시정지 규칙 | 단일 VDA 명세, 이미 자세히 있음 |
| 분리6 | RMF priority·dispatch·cancel·rewind | 스키마를 동작 구현으로 확대하지 말 것; Q2 |
| 분리6 | 상위 지시 번역·되돌림 | 추정; 물리적 완료와 재고 확정의 구분 Q3 |
| 분리6 | 동적 피킹 연구에서 실행 수정 설계 도출 | 논문 미열람, VDA 제약 반영 미확인; Q5 |
| 분리7 | ISA-95 2025 개정 보도자료 | 원문 미열람; 표준 본문과 발표 구분 |
| 분리7 | OPC 상태 전이, SCOR 범위 | 원문 미열람 사실 태그; Q1 중심 보완 |
| 분리8 | Yu·Srinivas의 AOCT·ATT·AWTD | 원문 미열람 결과 수치/범위 확인 필요 |
| 분리8 | Lorenz 등 재최적화의 점근 최적성 | 원문 미열람, 업무 메시지 연동과 조건 차이 |
| 분리8 | Gallien·Weber 2010 웨이브리스 성과 | 원문 미열람·오래된 자동분류기 현장 |
| 분리8 | GreenAuto REST/MQTT·VDA 향후과제 | 저자 미확인·본문 미열람; Q5 |
| 분리8 | 국내 30대 발표 | 2차 보도 미열람; Q4 |
| 본문9 | 상위 요청 번역·결과 반환 책임 | 추정; 공급자 공개 계약/인터페이스가 필요 |

#### 1~13절 공백

| 절 | 진단 |
|---|---|
|1|정의와 범위 있음|
|2|취소·변경 핵심 질문 있음, 종료 판정 없음|
|3|상위/하위 경계는 있으나 변환 계약 근거 부족|
|4|명령·상태 용어 있음, 접수 응답·업무 확정·상관키 구분 부족|
|5|가상 물류 사례와 국내 협력 발표; 제조·병원 등 실증 범위 공백|
|6|제어 메서드 열거 위주; 동기화·재시도·실행 결과 처리 근거 부족|
|7|2023 B2MML·2024 OPC와 main 링크; 최신 판·상태 확인 필요|
|8|논문 전부 원문 미열람, 조건·저자 미확인|
|9|경계가 설계 추정이며 재고 확정과 물리적 인계 구분 부족|
|10|연결 목록 있음, 타 영역 본조사는 이번에 섞지 않음|
|11|신규3질문+oq002·012, 연관 oq014·001; 미해결|
|12|2026-09-25 이후 표시 갱신 없음|
|13|원문 미열람·main 링크·판날짜 미상 다수|

#### 열린 질문

전체 원문은 wiki-s11.txt에 보존했다. 새 질문에는 별도 id가 없다.

| id | 요지 | 조사 |
|---|---|---|
|새1|납기·운송 마감을 RMF 우선순위/대기열로 바꾸는 공개 설계|Q2·Q3|
|새2|ISA-95 작업 지시·응답과 VDA/RMF 사이 표준 매핑|Q1·Q2|
|새3|적재·운반 후 취소 시 되돌림·재고 반영 주체와 규칙|Q3·Q4|
|oq-002|국내 SSCC/EPCIS와 적재·하역 완료 연결 운영|Q4|
|oq-012|로봇 운반 완료와 WMS 입고·인수 확정, 식별키·대기시간|Q3·Q4|
|관련 oq-014·oq-001|업무/로봇 상태 동기화 및 적재·하역–EPCIS 매핑|Q3; 사건 모델 일반론으로 범위 확장 안 함|

#### 2025년 이전 후보

- OPC Job Control 노드셋 2.0.0 / 2024-01-31.
- B2MML 0701 / 2023, 기반 ISA-95 Part2·5 / 2018.
- Gallien·Weber / 2010. 오래됐다는 이유로 오류라고 판정하지 않음.

#### 검색 전 조사 질문

| id·우선순위 | 질문 | 완료 기준 |
|---|---|---|
|Q1 1|ISA-95/OPC Job Control의 변경·취소 의미와 상위→로봇 매핑 범위는?|명세의 상태별 메서드 조건·공개 매핑 구현·표준 판을 확인|
|Q2 2|Open-RMF에서 업무 요청의 식별·취소·진행 상태를 어떤 API 계약으로 연결하는가?|고정 스키마와 구현 문서로 접수·최종 상태·우선순위 변경 지원을 분리|
|Q3 3|WMS/ERP의 업무 확정과 로봇 운반 완료를 분리하는 공개 연동 설계가 있는가?|상관키·명령/확인·재시도·재고 확정의 실제 제품 문서 확인|
|Q4 4|국내 테크타카·플로틱 등의 발표 이후 실증 결과와 식별키·인계 기준이 공개됐는가?|국내 공급자/운영사 원문, 실제 규모·결과·기간·한계 확인|
|Q5 5|기존 인용 논문은 실물 다사업자 업무 연동과 동적 변경을 어디까지 검증했는가?|논문 본문·서지·실험 규모·메시지/재고/취소 제약을 대조|
|Q6 6|최근 1년 다사업자 업무 연동 및 LLM/MCP 시도는 어느 수준인가?|2025-10~2026-10 공식 출시/구현/논문, 실험·생산/제안·권한 경계를 구별|


## 부록 B. 검색 기록

### F-23 검색 기록

날짜: 2026-10-11. 건진 수는 검색 결과 전체 수가 아니라 candidates.md에 선정한 검토 자료 수다. 기본 검색은 질문마다 세 쿼리를 한 요청에 전달하여 결과가 합쳐졌다. 따라서 개별 쿼리별 수를 만들어내지 않고 묶음 합계와 후보 id를 기록한다. 추가 쿼리는 개별 실행했다. 반복 발견도 해당 검색의 건진 수에 포함하지만 질문별 후보 총수에서는 중복 제거한다. 원문 열람 비율과는 별도다.

|질문·관점|검색어|날짜|건진 출처 수|
|---|---|---|---|
|Q1 ①|site.reference.opcfoundation.org OPC 10031-4 Update Cancel Abort JobOrder state|2026-10-11|세 쿼리 공동 2 (C01, C03)|
|Q1 ②|site.github.com ISA95 VDA5050 B2MML robot mapping|2026-10-11|같은 묶음|
|Q1 ⑤|ISA-95 로봇 MES 작업 지시 연동 표준 OPC UA|2026-10-11|같은 묶음|
|Q2 ②|site.github.com/open-rmf/rmf_api_msgs task_request cancel_task_response request_id priority|2026-10-11|세 쿼리 공동 4 (C04, C05, C06, C11)|
|Q2 ②|site.open-rmf.org task API integration cancellation task state warehouse|2026-10-11|같은 묶음|
|Q2 ⑥|Open RMF task API priority update limitations WMS integration|2026-10-11|같은 묶음|
|Q3 ④|site.help.sap.com warehouse robotics integration warehouse order confirmation robot|2026-10-11|세 쿼리 공동 3 (C07, C08, C09)|
|Q3 ④|site.learn.microsoft.com dynamics365 warehouse automation external warehouse robots confirmation|2026-10-11|같은 묶음|
|Q3 ③|warehouse robot WMS integration order confirmation idempotency REST API study|2026-10-11|같은 묶음|
|Q4 ⑤|site.flotic.com 테크타카 아르고 30대 실증 2025 2026|2026-10-11|세 쿼리 공동 2 (C13, C15)|
|Q4 ①|site.gs1kr.org EPCIS 로봇 물류 SSCC 인수 완료|2026-10-11|같은 묶음|
|Q4 ③|Korea warehouse WMS autonomous mobile robot integration case study 2025 2026|2026-10-11|같은 묶음|
|Q5 ③|"Integrated Fleet Management" "7235" robots MES ERP|2026-10-11|세 쿼리 공동 3 (C16, C17, C18)|
|Q5 ③|"Picking Operations" "How Good is Reoptimization" full text|2026-10-11|같은 묶음|
|Q5 ③|"Collaborative Human" "Interventionist" AMR order picking limitations|2026-10-11|같은 묶음|
|Q6 ④|site.sap.com warehouse robotics integration 2026 2025 MCP|2026-10-11|세 쿼리 공동 2 (C10, C19)|
|Q6 ②|site.github.com robot MCP WMS MES warehouse task|2026-10-11|같은 묶음|
|Q6 ③|warehouse robot orchestration LLM MCP integration paper 2026 2025|2026-10-11|같은 묶음|
|Q2 ③ 보완|Open RMF task request cancel priority warehouse integration research paper|2026-10-11|5 (C04, C05, C07, C22, C23)|
|Q3 ① 보완|site.ref.gs1.org CBV receiving accepting unloading bizStep EPCIS|2026-10-11|1 (C12)|
|Q5 ② 보완|site.github.com GreenAuto fleet management mobile robots REST MQTT|2026-10-11|2 (C16, C26)|
|Q5 ① 보완|site.reference.opcfoundation.org ISA95 JobOrder Ended Closed post processing|2026-10-11|1 (C01)|
|Q5 ④ 보완|GreenAuto Stellantis mobile robots fleet management MES ERP project|2026-10-11|1 (C16)|
|Q4 ⑤ 보완|site.techtaka.com 플로틱 로봇 2025|2026-10-11|2 (C14, C25)|
|Q4 ⑤ 보완|site.flotic.com "테크타카"|2026-10-11|1 (C25)|
|Q6 ② 보완|site.github.com MCP robot warehouse SAP ROS mission|2026-10-11|4 (C07, C08, C20, C24)|

추가 직접 추적: 기존 위키 각주의 C02 B2MML, C21 ISA 발표; 검색에서 찾은 후보의 원문·태그·공식 PDF. 미러 URL을 출처 수에 추가하지 않는다. Q4의 flotic 도메인 한정 쿼리는 해당 도메인 직접 근거를 얻지 못했고 공급자 플랫폼 설명 C25만 검토 후보로 남겼다. 국내 직접 실증 결과를 확보했다는 뜻이 아니다.

### 2단계 후보 수집

검색일 2026-10-11. 실행 쿼리와 응답 원본은 search-results.json에 보존. Q1~Q6 각 기본3쿼리, Q2·Q3·Q4·Q5·Q6 보완검색. 같은 문서의 절·번역·미러는 1개 자료 묶음으로 집계. 아래는 검토 후보이며 최종 채택·원문 열람을 뜻하지 않는다.

| id | 후보 |
|---|---|
| C01 | OPC 10031-4 Job Control v2.00.0 공개 본문·판 목록 |
| C02 | MESA B2MML 거래 프로파일 고정 코드 |
| C03 | VDA 5050 3.0.0 상위 인터페이스 범위 |
| C04 | Open-RMF rmf_api_msgs 고정 스키마 묶음 |
| C05 | Open-RMF rmf_task 고정 README |
| C06 | Open-RMF API Server 공식 문서 |
| C07 | SAP Warehouse Robotics 로봇 작업 API 문서 |
| C08 | SAP Warehouse Order Processing 문서 |
| C09 | SAP EWM FAQ robotic integration 공식 저자 글 |
| C10 | SAP Warehouse Pick & Place Architecture, 2026 갱신 |
| C11 | Oracle WMS 26c Change Priority |
| C12 | GS1 CBV 비즈니스 단계 정의 |
| C13 | GS1 Korea SSCC 설명 |
| C14 | 아르고 2025-01-21 로봇 협력 공식 발표 |
| C15 | LG CNS 2026-07-16 HD현대일렉트릭 고객 사례 |
| C16 | GreenAuto Applied Sciences 2025 논문 |
| C17 | Lorenz 등 Networks 2025 논문; arXiv·대학 저장소는 같은 출처 |
| C18 | Yu·Srinivas 2025 논문 및 저자 학위논문 후보(별도 문헌임을 구별) |
| C19 | SAP 2025-11 Physical AI 파일럿 발표 |
| C20 | ROS-MCP Server와 Tugbot 창고 예시, 고정 코드 |
| C21 | ISA 2025-04-10 ISA95 Part1 개정 발표 |
| C22 | Open-RMF Discourse Dispatch Queue vs Direct Queue #512 |
| C23 | Frontiers 2022 병원 RMF 현장 시험 논문 |
| C24 | ROSBag MCP Server arXiv 2511.03497 |
| C25 | 테크타카 ARGO 플랫폼 공식 설명 |
| C26 | NVIDIA Isaac Mission Dispatch 고정 README |

| 질문 | 후보(서로 다른 자료 5개 이상) | 검색 관점 |
|---|---|---|
|Q1|C01 C02 C03 C21 C26|표준·공개 구현·국내, 3개|
|Q2|C04 C05 C06 C22 C23|공개 구현·한계·학술, 3개; 학술은 보완검색|
|Q3|C07 C08 C09 C11 C12 C01|산업·학술·표준, 3개; 표준은 보완검색|
|Q4|C13 C14 C15 C25 C12|국내산업·표준·학술, 3개; 국내 직접 학술 근거 미확보|
|Q5|C16 C17 C18 C01 C26|학술·공개 구현·표준·산업, 4개; 같은 논문 미러 합산 안 함|
|Q6|C09 C10 C15 C19 C20 C24|산업·공개 구현·학술, 3개|

후보 제외: 일반 SEO 연동 글, 위키백과, 무관한 기업 정보·마케팅 통계, GreenAuto와 연결되지 않은 개인 FMS 저장소는 원문 평가 대상으로 선정하지 않았다. 플로틱 구조조정 기사는 2차 보도이므로 기술 결론에 채택하지 않고 실증 완료를 추정하지 않는 계기로만 삼았다.


## 부록 C. 출처 평가표

### 3단계 원문 평가 — 2026-10-11

관련 본문을 직접 읽은 상태를 뜻한다. PDF는 관련 절을 텍스트로 읽고 핵심 쪽을 이미지로 확인했다. 코드는 정적 열람이며 실행 시험이 아니다. 아래 최종 n번호의 서지·URL은 최종 출처 절에 상세 기재한다. 같은 저장소의 파일 묶음과 논문 미러는 하나로 센다.

|후보 → 최종|기관·제목·판/발행일|열람 상태·종류|독립성|평가·채택 판단|
|---|---|---|---|---|
|C01 → n1|OPC Foundation/ISA, OPC 10031-4 Job Control, 2.00.0, 2024-01-31|원문 열람; 1차 규격, §1·6.2.1·6.2.4·부록B|ISA와 공동 표준 계열; n17과 독립 아님|high: 메서드 조건 직접 규정. 로봇 매핑의 표준화까지 확장하지 않음|
|C02 제외|MESA International, B2MML-TransactionProfile.xsd, 0701/2023, 커밋65cc665(2023-07-11)|원문 열람; 1차 코드, 열거형·SupportedActionType·머리말|MESA 구현; ISA 개념 기반|high: 고정 스키마 정의. 위키의 동사 목록이 이미 있어 새 항목 제외. 전체 ISA 의미가 없다고 일반화하지 않음|
|C03 제외|VDA, VDA 5050, 3.0.0/2026-03|원문 열람; 1차 규격 §Scope, F-21 확보 PDF 재대조|VDA/VDMA 계열|high: 외부 IT 제외는 이미 위키/F-21에 있음. F-23 새 출처로 중복 계산 안 함|
|C04 → n2|Open-RMF, rmf_api_msgs, e9b7630(2026-09-19)|원문 열람; 1차 JSON 6개|n3·C06·C22와 동일 RMF 프로젝트|high: 필드·필수값·응답 구조 확인. 구현 실행/재고 트랜잭션 보장 아님|
|C05 → n3|Open-RMF, rmf_task README, 3a6af29(2026-09-25)|원문 열람; 1차 구현 문서 Usage|n2와 같은 프로젝트|high: phase별 취소 반응 설명. 어댑터 실제 동작 시험 아님|
|C06 제외|Open-RMF API Server, 발행일 미확인, 접근일 현재 문서|원문 열람; 1차 프로젝트 문서 Overview·Authentication·Authorization|RMF 계열|medium: 움직이는 문서; 작업 API 존재 확인용. 신원·권한 일반론은 영역 밖이어서 제외|
|C07 → n4|SAP, APIs for Integration via Fleet Management Systems, 2024-07-10|HTML 열람 실패(본문0행), 공식 PDF 원문 열람; 1차 제품 명세|n11·n12·n18과 SAP 계열|high(과거 계약)/현재 권장성 제한: 문서에 Deprecated. 최신 API의 증거로 쓰지 않음|
|C08 → n18|SAP, End-User Information for Integration via Integration Services, 2308, 2023-08-19|원문 열람; 1차 공식 PDF §2·3|SAP 계열; n4와 별도 연동 경로|high(해당 판의 규칙): FMS 경로와 혼합 금지|
|C09 제외|SAP Community, The SAP Extended Warehouse Management FAQ Series: Robotic Integration… (페이지14261381), 발행일·저자 미확인|열람 실패(web·curl HTTP403); 1차 후보, 본문 평가 불가|SAP 계열|low: 검색 요약을 기술 결론에 쓰지 않음|
|C10 → n11|SAP, Warehouse Pick & Place with Embodied AI Robotics, 갱신2026-05-12|원문 열람; 1차 참조구조 설명|SAP 계열|medium: 설계 설명. 상용 성능/고객 운영의 독립 검증 아님|
|C11 → n5|Oracle, WMS REST API Guide—Change Priority, 26c, 발행일 미확인|원문 열람; 1차 제품 API 명세|Oracle; SAP와 다른 기관|high(계약): 상태·권한·식별키 명시. RMF 우선순위 변환 검증 아님|
|C12 → n6|GS1, Core Business Vocabulary Standard, Release2.0, Ratified2022-06|원문 열람; 1차 PDF §7.1.3 pp36·40·43|GS1; n16과 같은 계열|high: 업무 단계 의미. 로봇별 이벤트 매핑은 별도|
|C13 → n16|GS1 Korea, SSCC(Serial Shipping Container Code) / 물류라벨, 발행일 미확인|원문 열람; 1차 기관 설명|GS1 계열, n6과 독립 아님|high(기본 식별 정의): 국내 로봇 운영 증거는 아님|
|C14 → n7|테크타카/아르고, 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시, 2025-01-21|원문 열람; 1차 공급자 발표|테크타카·플로틱 공동 사업; 기존 재보도와 같은 사건|medium: 발표 계획. 단일 벤더 주장; 후속 결과 미확인|
|C15 → n8|LG CNS, 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다, 2026-07-16|원문 열람; 1차 공급자 고객 사례|LG CNS 공급 사례; 고객 독립 자료 없음|medium: WCS/SCADA 역할의 벤더 설명. 수치 성과 제외|
|C16 → n9|David Lopes 외16명, Integrated Fleet Management…Automotive Sector, Appl.Sci.15(13):7235, 2025-06-27, DOI10.3390/app15137235|원문 열람; 1차 논문 PDF §4·5.2·6.2·7·8|GreenAuto 연구팀; 자체 실험|medium: 현재 구현/미래 기능 명확. 개발3대와 성능절최대20대 사이 실험 구성 미상|
|C17 → n10|Catherine Lorenz·Alena Otto·Michel Gendreau, Picking Operations…Reoptimization?, Networks86(2):157–173, 2025-05-01, DOI10.1002/net.22281|원문 열람; 1차 논문, 대학 저장소 PDF와 출판사 서지|동일 논문 미러 1개|high(수학·계산실험 조건): 단일 피커 모델. 실물 다사업자 업무 연동 아님|
|C18 제외|Shitao Yu·Sharan Srinivas, Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025(기존 위키 표기), 정확한 발행일·권호·DOI 미확인|열람 실패(ScienceDirect HTTP403); 본문 미열람|Yu·Srinivas 연구팀|low: 기존 결과 재확정 안 함. 저널 논문 대신 학위논문으로 근거 바꾸지 않음|
|C18 부속 제외|Shitao Yu, Collaborative Human-Robot Order Picking System: Algorithms for Task Allocation and Routing in Complex Environments, University of Missouri-Columbia 박사학위논문, 2022-07|원문 미열람(표지·승인지만 열람); 1차 학위논문 후보|Yu·Srinivas 동일 연구 계열|low(이번 질문 근거): 제목·연도부터 다른 문헌. 2025 논문의 원문 열람으로 세지 않음|
|C19 → n12|Lukasz Ostrowski/SAP, How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases, 표시2025-11-05, 후속 수정일 미확인|원문 열람; 1차 공급자 발표 Bosch 절|SAP·협력사 공동 사업|medium: 현재 본문에 후속2026 사례 포함. Bosch beta/test 조건 유지, 최초일에 모든 사례를 귀속하지 않음|
|C20 → n13|robotmcp, Example1: Tugbot Warehouse Simulation (Ignition Gazebo), edbc642(2026-07-09)|원문 열람; 1차 데모 README|robotmcp 프로젝트; NVIDIA와 별도|medium: 단일 로봇 시뮬레이션 설명. WMS 생산 운영 증거 아님|
|C21 → n17|ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025-04-10|원문 열람; 1차 개정 발표. ISA95 Part1 표준 본문은 미열람|ISA/OPC 계열|high(발행 사실)/본문 평가 불가: 발표와 규격 본문 구분|
|C22 제외|ItamarEliakim-R·Yadunund·mxgrey, Dispatch Queue vs Direct Queue #512, 2024-08-17~27 토론|원문 열람; 1차 개발자 토론|RMF 프로젝트 계열|medium: 당시 direct/dispatched 분리 설명. 2026 기본 구현 보장으로 확대하지 않음|
|C23 → n15|Robert Valner 외7명, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, Front.Robot.AI9:922835, 2022-08-23, DOI10.3389/frobt.2022.922835|원문 열람; 1차 논문 §2.2·2.3·3·4|Tartu 연구팀, RMF 활용자; SAP/GS1과 독립|medium: 병원 TIAGo 실물 한 대; 이기종 두 대는 별도 시험. 수동 인계 확인 사례 채택|
|C24 제외|Lei Fu·Sahar Salimpour·Leonardo Militano·Harry Edelman·Jorge Peña Queralta·Giovanni Toffetti, ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications, arXiv2511.03497v1, 2025-11-05, DOI10.48550/arXiv.2511.03497; 학술지 게재 미확인|원문 열람; 1차 프리프린트 §III–V|ZHAW/Binabik 연구팀|medium: ROSbag 사후 분석 평가. 실시간 업무 시스템 연동 근거가 아니어서 제외|
|C25 제외|테크타카, ARGO 플랫폼 소개, 발행일 미확인|원문 열람; 1차 공급자 제품 소개|C14와 같은 업체|low(연동 질문): WMS·재고 설명은 있으나 필요한 로봇 인계 계약 미확보|
|C26 → n14|NVIDIA, Isaac Mission Dispatch README·MCP tutorial·server.py·queries.py, 56455eb(2026-09-15)|원문 열람; 1차 고정 코드·문서|NVIDIA 단일 프로젝트, 파일4개를 1출처로 집계|high(정적 코드 존재)/운영 평가 없음: MCP 등록·이동 지시 핸들러·REST호출 확인. 기업 업무 확정 검증 아님|

최종 채택: 18개, 관련 원문 열람18/18, 1차18개. 후보 탈락은 분모에서 제외하며 위 표로 공개한다. 실제 시험을 수행했다는 뜻은 아니다. 동일한 구체적 주장에 대한 독립 자료 2개 교차 확인은 0건이다. 표준·제품·현장 사례가 유사한 구분을 보여도 같은 구현의 검증으로 합치지 않았다.


## 부록 D. 검증 기록

### D1. 4단계 질문별 종합·충돌·범위 판정

|질문|주장·출처|교차 확인·충돌 처리|위키 반영 판정·한계|
|---|---|---|---|
|Q1|K01·K13, n1·n17|공동 표준 계열이며 독립 아님. OPC2024와 ISA Part1 2025는 문서가 달라 판 충돌이 아님|메서드 조건 추가, 기존 규격 정보 원문 확인. 표준 매핑은 미해결|
|Q2|K02·K03, n2·n3|동일 프로젝트의 스키마·README를 대조. 독립 검증으로 합산 안 함. C22의2024 토론을2026 구현으로 일반화하지 않음|기존 상태 목록은 제외하고 응답 구조·취소 반응 지점 추가. 정적 열람 한계|
|Q3|K04~K06·K14, n4·n5·n6·n15·n18|다른 기관이 유사한 단계 구분을 보이지만 같은 제품/같은 주장을 반복 검증한 자료가 아님. SAP FMS와 Integration Services 경로 구분|구체적 계약 예시와 의미 차이 추가. 국내 확정 키·대기 기준은 미해결|
|Q4|K09·K10, n7·n8·n16|ARGO 기존 보도와 발표는 같은 사업. LG는 다른 현장이므로 ARGO의 결과 교차 확인이 아님. 선행 피킹 시간 성과를 남이천에 귀속하지 않음|기존 국내 발표의 1차 출처 보강, 제조 사례 신규 추가. 모든 현장 구축 주장 추정 유지|
|Q5|K07·K08, n9·n10|논문끼리 다른 문제·실험. GreenAuto3대/20대의 조건 차이 미해결. Yu2022학위논문과2025저널논문을 동일시하지 않음|구현/미래 설계와 이론 가정 보강. 위키에 이미 있는 점근 최적성은 재발견으로 세지 않음|
|Q6|K11·K12, n11~n14|SAP 자료 둘은 동일 계열. robotmcp와 NVIDIA는 독립 프로젝트지만 동일 업무 연동의 교차 실증 아님. 뉴스 최초일과 현재 본문 변경 분리|최근1년 공식 설계 갱신·코드 기능 기록 추가. GA·운영 성과·WMS 재고 확정 미확인|

### D2. 초안 이후 원문 재대조

초안을 저장한 다음, 확보 원문 파일을 다시 열어 사실 문장별 발췌를 대조했다. 아래 인용은 주변 절·표·코드와 함께 읽었다. 동일 짧은 구절은 중복 인용을 피하고 연결된 문장 id를 표시했다. OPC 판 목록은 웹 원문을 재열람했다. PDF p11(GreenAuto), p160/파일4쪽(Lorenz), p40(CBV), p7(SAP API)는 이미지로도 대조해 표 열/그림을 확인했다. 발췌 검색의 성공만으로 의미가 입증됐다고 보지 않았다.

|증거 id·연결 문장|직접 인용(짧은 발췌)|원문 위치·근거|
|---|---|---|
|E01 / F01|“not yet been started”|§6.2.1.9; `opc.txt` [^n1]|
|E01b / F01|“All previously stored information is replaced.”|§6.2.1.9; `opc.txt` [^n1]|
|E02 / F02|“removes the stored information”|§6.2.1.12; `opc.txt` [^n1]|
|E03 / F03|“state Ended”|§6.2.1.11; `opc.txt` [^n1]|
|E03b / F04|“state Aborted”|§6.2.1.10; `opc.txt` [^n1]|
|E04 / F05|“no further post processing”|§6.2.4 표45; `opc.txt` [^n1]|
|E05 / F06|“must match a priority schema supported by a fleet”|properties.priority; `task_request.json` [^n2]|
|E06 / F07|“"required": ["success", "state"]”|oneOf/0; `dispatch_task_response.json` [^n2]|
|E07 / F08|“"required": ["type", "task_id"]”|required; `cancel_task_request.json` [^n2]|
|E08 / F09|“simple_response.json”|$ref; `cancel_task_response.json` [^n2]|
|E08b / F09|“"canceled", "killed", "completed"”|$defs/status; `task_state.json` [^n2]|
|E09 / F10|“Each phase can have its own unique response”|Usage; `rmf-task-readme.md` [^n3]|
|E10 / F11|“Deprecated”|§1; `sap-apis.txt` [^n4]|
|E11 / F12|“response to be returned before”|§1.5 p7; `sap-apis.txt` [^n4]|
|E12 / F13|“If the robot task can’t be canceled”|§1.6.2 p12; `sap-apis.txt` [^n4]|
|E12b / F13|“CANCELLED”|§1.6.2 p12; `sap-apis.txt` [^n4]|
|E13 / F14a|“Ready, Held or Created”|도입; `oracle.txt` [^n5]|
|E13b / F14b|“Permission is enabled”|도입; `oracle.txt` [^n5]|
|E14 / F15|“sorts the warehouse orders in a queue by the latest starting dates”|§2 p4; `sap-orders.txt` [^n18]|
|E15 / F16|“added to the receiver's inventory”|§7.1.3 p40; `cbv.txt` [^n6]|
|E16 / F17a|“an object arrives at a location”|§7.1.3 p36; `cbv.txt` [^n6]|
|E17 / F17b|“changes possession and/or ownership”|§7.1.3 p36; `cbv.txt` [^n6]|
|E18 / F17c|“unloaded from a shipping conveyance”|§7.1.3 p43; `cbv.txt` [^n6]|
|E19 / F18|“not yet active”|§5.2 p11; `green.txt` [^n9]|
|E20 / F19|“future capability”|§5.2 p11; `green.txt` [^n9]|
|E21 / F20a|“two AMRs and one AGV”|§4 p6; `green.txt` [^n9]|
|E21b / F20b|“centralized monitoring and supervision”|§7 p21; `green.txt` [^n9]|
|E22 / F21|“one picking zone of a single picker”|§2 p160; `lorenz.txt` [^n10]|
|E23 / F22|“an empty robot is immediately available”|§2 p160; `lorenz.txt` [^n10]|
|E24 / F23|“2 600 instances”|§4.1 p169; `lorenz.txt` [^n10]|
|E25 / K09|“로봇 30대를 지원한다”|남이천 문단; `argo.txt` [^n7]|
|E26 / K10|“WCS와 SCADA 기반 통합 제어·관제 체계 구축”|Solution2; `lg.txt` [^n8]|
|E27 / F24|“Semantic Understanding of Business Objects”|Key Components; `sap-architecture.txt` [^n11]|
|E28 / K11|“dedicated beta and test system environments”|Bosch; `sap-news.txt` [^n12]|
|E29 / F25a|“2026-03 \| Mission Dispatch MCP”|Latest Update; `nvidia-readme.md` [^n14]|
|E29b / F25b|“2026-08 \| VDA5050 3.0 support”|Latest Update; `nvidia-readme.md` [^n14]|
|E30 / F26|“TOOL_DISPATCH_MISSION”|list_tools; `nvidia-server.py` [^n14]|
|E31 / F27|“return self._post_request("mission", data)”|dispatch_move_mission; `nvidia-queries.py` [^n14]|
|E32 / F28|“Tugbot mobile robot”|Introduction; `mcp-demo.md` [^n13]|
|E34 / F30|“not compatible”|§1; `opc.txt` [^n1]|
|E35 / F31|“publication of ANSI/ISA-95.00.01-2025”|첫문단; `isa.txt` [^n17]|
|E36 / F32|“verified that the samples were delivered”|§3.1; `frontiers.txt` [^n15]|
|E37 / F33|“we are yet to apply multiple delivery robots inside the Hospital”|§4; `frontiers.txt` [^n15]|

F29의 E33은 OPC 공식 판 목록의 발행일 표시 “2024-01-31”을 직접 재대조했다. 2.00.0의 current 표시는 같은 행에서 확인했다. API의 [사실]은 해당 판의 명세를 기술한 것으로, 공급자 성능이나 현장 보급의 확정으로 바꾸지 않았다. F01~F33의 분할 식별자를 포함한 모든 사실 문장을 위 표와 연결했다. 요약과 열린 질문의 반복 문장은 같은 F번호 근거를 따른다.

### D3. 필수 9항목 검증 기록

|항목|처음 태그 → 최종 태그|바꾼 이유·검증 결과|
|---|---|---|
|1 사실 재대조: K09 ARGO 지원·실증|사실 → 추정|원문 발표를 확보했어도 현장 수행은 단일 공급자 주장. 원문 공개와 결과 입증을 분리|
|1 사실 재대조: K10 LG 구축|사실 → 추정|공급자 고객 사례 외 독립 운영 증거 없음|
|1 사실 재대조: K11 SAP/Bosch 파일럿|사실 → 추정|공동 공급자 발표이며 beta/test 조건. 뉴스 보도 형식으로 사실 태그를 우회하지 않음|
|1 그 밖의 F문장|사실 → 사실(변경 없음)|원문 구절·위치 연결. 문서의 정의·코드 구조·논문 조건으로 범위 제한|
|2 추론 분리: F23|사실 → 사실(표현 수정)|계산실험과 ‘실물 다사업자 시험이 아니다’를 한 문장에 두지 않고, 직접 확인한 계산실험 문장만 사실로 남김. 업무 연동에 적용할지는 의견으로 분리|
|2 복수 주장 분리|사실 → 사실(문장 분리)|F14 상태/권한, F17 세 어휘, F20 개발 대상/감시 범위, F25 두 변경 연월을 분리|
|3 숫자·번호: OPC|사실 → 사실(정정)|Ended 상태 설명은 표44가 아니라 표45. Stop/Abort 성공 후 shall 조건 유지|
|3 숫자·번호: 실증|변경 없음|ARGO30대는 지원 발표, GreenAuto3대와20대 관계는 미확인, Lorenz2,600은 생성 인스턴스 수, Tartu 병원1대와 별도시험2대를 구분|
|3 성과 번역|변경 없음|ARGO 선행시험 시간과 LG 면적·작업량 수치는 신규 사례 성과로 인용하지 않음|
|4 서지|변경 없음 / 기관 페이지 제목 정정|GreenAuto17저자와2025-06-27, Lorenz3저자·DOI·2025-05-01 첫발행을 대조. GS1 Korea 실제 제목으로 수정. Oracle 발행일 미확인. 커밋일은 최초 발행일이 아님|
|4 SAP 뉴스 날짜|변경 없음|표시2025-11-05와 갱신된 현재 내용의 사례 실시일을 동일시하지 않음. 후속 수정일 미확인|
|5 표현 강도|변경 없음|OPC shall과 SAP requires는 해당 명세 조건으로 기술. README의 사용자 지정 가능성을 모든 어댑터 동작 보장으로 바꾸지 않음|
|6 발행·시행 상태|변경 없음|CBV Ratified, OPC release, ISA 발표문, 정식 게재 논문, ROSBag프리프린트를 구분. SAP Deprecated 표시 유지. 법령 시행 판단 없음|
|7 독립성|변경 없음|SAP 계열4자료, RMF 계열, GS1 계열, ISA/OPC 계열은 각기 독립 교차 확인으로 세지 않음. 논문 미러 중복 제거. 동일 주장 독립 교차 확인0건|
|8 위키 중복|변경 없음|VDA 외부IT 제외·취소/주문 갱신, B2MML 동사, RMF 상태 목록, Lorenz 일반 결과는 새 내용으로 재수록하지 않음|
|9 영역 범위|변경 없음|교통 제어·지도·안전·모델 성능·권한 구현 일반론은 확장하지 않음. MCP는 업무 요청과 로봇 명령의 접점만 검토|

태그를 낮춘 문장은 K09·K10·K11의 3개다. 번호·문장 분리·서지 정정은 태그 하향에 합산하지 않았다. 불확실성을 제거한 것이 아니라 확인 못 한 U01~U11을 명시적으로 보존했다.

### D4. 수량·파일 검증 기준

- 보완 항목: K01~K14, 14개.
- 채택 문헌: n1~n18, 18개. 모두 관련 본문 열람, 새 문헌13개.
- 출처 평가의 실패·제외 후보를 채택 출처 분모에 끼워 넣지 않았다.
- 확인 못 함: U01~U11, 11개. 완전히 해결한 기존 열린 질문0개.
- 저장 전 필수 제목, 각주18개 정의·참조 대응, 보완14개, 사실 문장38개와 증거 연결, U01~U11, 임시 자리표시자 없음, 본문이 비어 있지 않음을 검사했다. 이 검사는 원문 대조를 대신하지 않는다.

### D5. 탈락 후보의 추적 링크

부록 C의 후보 서지에서 최종 각주가 없는 자료의 원문 경로다. 인용 근거로 채택하지 않았다.

- C02 [B2MML 고정 스키마](https://github.com/MESAInternational/B2MML-BatchML/blob/65cc66534343c86a1ce953561e121f906a0a0cbe/Schema/B2MML-TransactionProfile.xsd).
- C03 [VDA 공식 PDF](https://www.vda.de/dam/jcr%3A09f03b91-13e2-4db3-bf30-4f221710071b/VDA5050-V3.0.0-2025-03.pdf). 파일명보다 표지의2026-03판을 기준으로 읽음.
- C06 [RMF API Server 문서](https://open-rmf.github.io/rmf-web/packages/api-server/).
- C09 [SAP Community FAQ 후보](https://community.sap.com/t5/supply-chain-management-blog-posts-by-sap/the-sap-extended-warehouse-management-faq-series-robotic-integration-for/ba-p/14261381). HTTP403.
- C18 [Yu·Srinivas 저널 후보](https://www.sciencedirect.com/science/article/pii/S1366554525001231), [별도2022학위논문](https://mospace.umsystem.edu/bitstreams/e629b2ef-f667-4148-b113-fec8c1a8e541/download). 학위논문 표지는 원저널 대체 근거가 아님.
- C22 [RMF #512 토론](https://discourse.openrobotics.org/t/other-issue-dispatch-queue-vs-direct-queue-512/44673).
- C24 [ROSBag MCP v1 본문](https://arxiv.org/html/2511.03497v1), [서지·제출 이력](https://arxiv.org/abs/2511.03497).
- C25 [ARGO 플랫폼 소개](https://www.techtaka.com/ko/platform/).

### D6. 다음 담당자에게 남기는 원문 기록

원문·고정 코드·PDF·검색 응답은 `.research-work/F-23/`에 보존했다. `evidence.json`은 짧은 구절과 로컬 원문 위치를 연결한다. `source-evaluation.md`, `search-results.json`, `search-log.md`, `wiki*.html/txt`로 진단·검색·열람 경로를 추적할 수 있다. 본 문서는 위키 반영 제안이며 위키를 수정하거나 커밋하지 않았다.

