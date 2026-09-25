# 리서치 브리프 2026-09-25-29

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-29 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | A. 업무·공급망 설계 |

## 갭(비어 있거나 약한 섹션)

- A. 업무·공급망 설계 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음)
- 연결 상대 세부영역 가운데 9. 로봇·제조사 관제 연동만 published 이고 나머지(10~28 대부분)는 seed 라, 연결의 근거는 A 쪽 게시 페이지 각주에 기댄다
- 11. 분산 시스템·통신·컴퓨팅 구조와의 연결(클라우드 WMS 단절 시 현장 운영)은 2026-09-25-27 브리프에만 근거가 있고 게시 전이라 이번에 쓰지 않음
- 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영과 A. 업무·공급망 설계 세부영역 사이의 연결은 게시 페이지에 검증된 근거가 없음

## 조사 질문

1. 무슨 일을 왜, 얼마나 해야 하는가? [분류원문]
2. 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [분류원문]
3. 1. 주문·업무 시스템 연계와 2. 공정·워크플로 모델링의 작업 요청·변경·완료 조건은 C. 연결·실행 기반(9. 로봇·제조사 관제 연동, 12. 명령·작업 실행의 신뢰성)의 어떤 인터페이스·상태로 넘어가는가?
4. 2. 공정·워크플로 모델링의 완료 조건은 B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적과 E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계의 어떤 확인 신호에 기대는가?
5. 3. 처리능력·거점·설비 계획은 D. 계획·최적화(13. 작업 배정 — MRTA, 16. 공용 자원·충전·에너지 최적화), C. 연결·실행 기반의 10. 설비·건물 시스템 연동, F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈과 어떤 설정·제약·도구를 공유하는가?
6. 4. 성과·경제성·프로세스 개선의 지표 계산은 8. 실시간 세계 상태·데이터 일관성, 19. 모니터링·이상 탐지·원인 분석, 16. 공용 자원·충전·에너지 최적화와 어떤 데이터를 주고받는가?
7. 상위 작업 지시 표준(ISA-95 계열)과 로봇 인터페이스 사이 매핑 부재는 G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스와 어떻게 이어지는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 명세는 관제–이동로봇 통신과 무관한 인터페이스(주변 설비·인프라·외부 IT 시스템 인터페이스)를 범위에서 제외한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [추정] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: 로봇 인터페이스가 상위 시스템 연동을 범위 밖에 두므로, 상위 주문을 로봇 작업 요청(Open-RMF 작업 요청 등)으로 번역하는 계층이 두 대분류가 넘겨받는 지점이 될 것으로 보인다. | ref-031, ref-125 | 아니오 | low | 2026-09-25 | 시작 조건 | — |
| f3 | [사실] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 은 진행 중 다른 주문을 받으면 로봇이 OTHER_ORDER_ACTIVE 오류(WARNING)를 보고하게 하고, 취소할 수 없는 동작은 cancelOrder 뒤에도 RUNNING 을 거쳐 FINISHED 또는 FAILED 로 보고하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 피킹 / 예외·성과 | — |
| f4 | [사실] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: 상위 쪽 B2MML 거래 프로파일은 CHANGE·CANCEL 등 거래 동사를, OPC UA for ISA-95 Job Control 은 Update·Pause·Resume·Abort·Cancel 등 작업 지시 메서드를 정의한다. | ref-129, ref-130 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f5 | [사실] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계와 2. 공정·워크플로 모델링 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: Open-RMF 작업 상태 스키마는 queued·underway·completed·canceled·killed·failed 등 상태 값과 시작·종료 시각, 소요 시간 추정, 취소·강제 종료·중단 요청 기록을 담아 상위 시스템에 되돌릴 결과의 원천이 된다. | ref-111 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f6 | [추정] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ D. 계획·최적화의 14. 작업 순서·스케줄링: 웨이브·웨이브리스 출고 지시 방식과 동적 주문 도착 시 재최적화 연구는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다룬다. | ref-134, ref-133 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | 원문 미열람 |
| f7 | [추정] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 작업자가 피킹하고 AMR 이 운반하는 동적 주문 피킹 연구는 AMR 가용성에 따른 개입 전략을 다루어 주문 변경과 로봇 배정이 맞물리는 사례가 된다. | ref-132 | 아니오 | low | 2025 | 피킹 / 수행 자원 | 원문 미열람 |
| f8 | [추정] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 상위 시스템의 CANCEL 이 로봇이 이미 화물을 실은 뒤 오거나 취소 불가 동작이 끝까지 수행되면 되돌림 작업과 재고 반영이 복구·재계획 과제로 넘어갈 것으로 보인다. | ref-031, ref-129 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f9 | [사실] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: GS1 CBV 는 arriving(객체가 위치에 도착), receiving(수령자 재고에 추가), accepting(점유·소유 변경)을 서로 다른 업무 단계로 정의하고, VDA 5050 은 drop 완료를 적재물이 로봇을 떠나 로봇이 새 적재 상태를 보고한 때로 정의한다. | ref-044, ref-031 | 아니오 | medium | 2026-09-25 | 입고 / 완료·인계 | — |
| f10 | [추정] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: 로봇 완료 신호는 arriving 수준의 물리적 인도에 가까우므로, 공정 모델의 '인수 확인·재고 반영 완료' 조건은 7번이 다루는 식별자와 receiving·accepting 이벤트에 기대야 할 것으로 보인다. | ref-044, ref-031, ref-049 | 아니오 | low | 2026-09-25 | 입고 / 완료·인계 | — |
| f11 | [사실] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계: Open-RMF 배송 작업에서 로봇은 하역 지점 워크셀에 IngestorResult 를 받을 때까지 IngestorRequest 를 보내며, IngestorResult 는 요청 id·워크셀 id·상태(ACKNOWLEDGED, SUCCESS, FAILED)만 담는다. | ref-023, ref-049 | 아니오 | medium | 2026-09-25 | 입고 / 완료·인계 | — |
| f12 | [추정] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구가 있어, 공정 모델의 형식적 설계 점검이 형식 검증과 이어질 것으로 보인다. | ref-121 | 아니오 | low | 2022 | — | 원문 미열람 |
| f13 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화: AMR 물류센터 시뮬레이션 연구에서 충전기가 부족하면 큰 지연이, 과잉이면 불필요한 비용이 생겼고, RMFS 의 충전·배터리 교환 전략 비교도 연구되어 있다. | ref-102, ref-098 | 아니오 | medium | 2025 | 피킹 / 제약 | 원문 미열람 |
| f14 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: Open-RMF 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold(예 0.10) 아래인 로봇은 작업하지 않게 하고 충전 목표(recharge_soc), 로봇별 충전기, 작업 종료 후 동작(park·charge·nothing)을 둔다. | ref-105 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f15 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 데모의 호텔 환경은 승강기 2대·여러 문·3개 플릿(로봇 4대)이 다층 건물에서 함께 일하는 통합을 보이며, 공간과 승강기·문 같은 건물 설비를 공유하는 로봇 교통을 관리한다고 설명한다. | ref-104 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f16 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 병원 약품 배송 로봇 사례에서는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었으며, 호텔 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다(물류센터 적용 여부는 미확인). | ref-060, ref-103 | 아니오 | medium | 2026 | 제약 | 원문 미열람 |
| f17 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 RMFS 운영의 여러 결정 문제의 효과를 연구하는 이산 사건 시뮬레이션으로, 증차·증설 같은 가정한 미래의 실험 도구가 된다. | ref-101 | 아니오 | medium | 2026-09-25 | — | — |
| f18 | [사실] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: Open-RMF 로봇 상태 스키마는 상태(idle·charging·working·error 등), 배터리(0~1), 현재 작업 id, 운영자가 처리할 문제 목록, 위치, 기록 시각을 담아 가동률·충전·오류 시간 지표의 원천이 된다. | ref-148 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f19 | [추정] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: 제조 병목 탐지 방법과 창고 이벤트 로그 프로세스 마이닝 연구를 로봇 상태 기록에 적용하면 성과 분석과 이상·원인 분석이 같은 로그를 공유할 것으로 보인다. | ref-115, ref-149, ref-148 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f20 | [사실] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 ↔ D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화: Omega(2024) 게재 연구는 RMFS 에서 동적 우선순위 규칙이 선착순 대비 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다(모델·시뮬레이션 조건, 저자 보고값). | ref-146 | 아니오 | medium | 2024 | 피킹 / 예외·성과 | 원문 미열람 |
| f21 | [추정] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 우선순위 정책·충전 대안을 운영 전에 비교하는 일은 가정한 미래를 실험하는 쪽이며, 현재 상태를 표현하는 8. 실시간 세계 상태·데이터 일관성과 역할을 나눠 연결될 것으로 보인다. | ref-146, ref-102 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f22 | [추정] | A. 업무·공급망 설계의 1. 주문·업무 시스템 연계 ↔ G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스: ISA-95 계열 작업 지시 동사·메서드와 VDA 5050·Open-RMF 의 주문·작업 요청 사이 표준 매핑은 이번까지 확인되지 않아, 번역 규칙의 소유와 변경 승인이 상호운용성 거버넌스 과제로 넘어갈 것으로 보인다. | ref-129, ref-130, ref-031, ref-125 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 명세 원본: 'Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to ... external IT systems.' (발행일 미확인, 확인일 기준)
- **f2**: f1 과 Open-RMF task_request 스키마(1. 주문·업무 시스템 연계 페이지 9절 인용)를 대응시킨 추론. 번역 계층을 규정한 표준은 확인하지 못함. (재인용: 2026-09-25-13)
- **f3**: 명세 원본: 'report an error of type OTHER_ORDER_ACTIVE and level WARNING'; 취소 불가 동작은 'RUNNING while it is running, and after that ... FINISHED ... FAILED'. (발행일 미확인, 확인일 기준)
- **f4**: B2MML-TransactionProfile.xsd 의 TransactionVerb1Type: NOTIFY, GET, PROCESS, CHANGE, CANCEL, CONFIRM, SYNC ADD 등. Job Control 노드셋 문서: Store, StoreAndStart, Start, RevokeStart, Pause, Resume, Update, Abort, Stop, Cancel, Clear.
- **f5**: task_state.json 원본: status enum uninitialized, blocked, error, failed, queued, standby, underway, delayed, skipped, canceled, killed, completed; unix_millis_start_time/finish_time, estimate_millis, cancellation, killed, interruptions. (발행일 미확인, 확인일 기준)
- **f6**: 1. 주문·업무 시스템 연계 페이지 8·10절의 두 연구(Gallien & Weber 2010, Lorenz 외 2025)를 순서 결정과 대응시킨 추론. 원문 미열람. (재인용: 2026-09-25-13)
- **f7**: Yu & Srinivas(2025) 동적 주문 피킹 연구의 설정·개입 전략을 1. 주문·업무 시스템 연계 페이지 10절이 13. 작업 배정 — MRTA 와 잇는 근거로 인용. 원문 미열람. (재인용: 2026-09-25-13)
- **f8**: f3(취소 불가 동작)·f4(CANCEL 동사)를 대응시킨 추론. 되돌림 규칙을 정한 표준·사례는 확인하지 못함(oq-021).
- **f9**: CBV.ttl: receiving 'is added to the receiver's inventory', accepting 'changes possession and/or ownership'. VDA 5050: 'Load has left the mobile robot and mobile robot reports new load state.'
- **f10**: f9 와 IngestorResult 필드(f11)를 대응시킨 추론. 이 구성을 적용한 표준·사례는 확인하지 못함(oq-001, oq-012). (재인용: 2026-09-25-09)
- **f11**: 워크셀 장 원본: 'Requests a IngestorRequest till receives a IngestorResult'. IngestorResult.msg: request_guid, source_guid, status ACKNOWLEDGED=0 SUCCESS=1 FAILED=2. (발행일 미확인, 확인일 기준)
- **f12**: 2. 공정·워크플로 모델링 페이지 6절이 네 접근 가운데 하나로 든 Blondin 외(LICS 2022). 물류 로봇 공정에 적용한 사례는 확인하지 못함. 원문 미열람. (재인용: 2026-09-25-09)
- **f13**: 3. 처리능력·거점·설비 계획 페이지 3·10절 인용(FAIM 2025 시뮬레이션, Zou 외 2018). 두 출처는 서로 다른 주장을 뒷받침하며 교차 확인이 아님. 원문 미열람. (재인용: 2026-09-25-10)
- **f14**: config.yaml 원본: 'recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate', finishing_request: 'park' # [park, charge, nothing]. (발행일 미확인, 확인일 기준)
- **f15**: rmf_demos README 원본: 'The hotel has two lifts, multiple doors and 3 robot fleets (4 robots).' (발행일 미확인, 확인일 기준)
- **f16**: 3. 처리능력·거점·설비 계획 페이지 3·9절 인용. 병원·호텔 사례이며 물류센터 근거 아님(oq-010). 원문 미열람. (재인용: 2026-09-25-10)
- **f17**: README 원본: 'a discrete event-based simulation for Robotic Mobile Fulfillment Systems ... researching effects of multiple decision problems'. 8. 실시간 세계 상태·데이터 일관성과 구분. (발행일 미확인, 확인일 기준)
- **f18**: robot_state.json 원본: status uninitialized, offline, shutdown, idle, charging, working, error; battery 0.0~1.0; task_id; issues; location; unix_millis_time. (발행일 미확인, 확인일 기준)
- **f19**: 4. 성과·경제성·프로세스 개선 페이지 10절의 연결 근거(병목 탐지 리뷰 2023, 창고 프로세스 마이닝 사례 2015)를 f18 과 대응시킨 추론. 적용 연구는 미확인(oq-018). (재인용: 2026-09-25-14)
- **f20**: 4. 성과·경제성·프로세스 개선 페이지 5절 인용 수치. 현장 실측 아님. 원문 미열람. (재인용: 2026-09-25-14)
- **f21**: 4. 성과·경제성·프로세스 개선 페이지 10절 연결 서술과 분류 원문 7장의 8·22 구분을 대응시킨 추론. 원문 미열람. (재인용: 2026-09-25-14)
- **f22**: f1·f4 와 1. 주문·업무 시스템 연계 페이지 10절 28번 연결을 대응시킨 추론. 매핑 부재는 검색 범위의 관찰(oq-020).

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2201.05588 | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 예 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | 논문 | medium | 2026-09-25 | https://doi.org/10.1177/20552076261437181 | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-09-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 아니오 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-115 | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 2023 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031 | 예 |
| ref-149 | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 2015 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 공식 명세(main 3.0.0). 범위 제외, OTHER_ORDER_ACTIVE, 취소 불가 동작, drop 완료 정의를 원문으로 확인.
- **ref-125**: 원문 미열람. Open-RMF 작업 요청 스키마(이번 실행에서 다시 열지 않음).
- **ref-111**: Open-RMF 작업 상태 스키마. 상태 값, 시작·종료 시각, 추정 시간, 취소·강제 종료·중단 기록을 원문으로 확인.
- **ref-129**: B2MML 거래 프로파일 스키마. TransactionVerb1Type 의 동사(CHANGE, CANCEL 등)를 원문으로 확인.
- **ref-130**: OPC UA for ISA-95 Job Control 노드셋 문서. 작업 지시 수신 객체의 메서드(Store~Clear)를 원문으로 확인.
- **ref-132**: 원문 미열람. 작업자 피킹·AMR 운반 협업의 동적 주문 피킹과 개입 전략 연구.
- **ref-133**: 원문 미열람. 동적으로 도착하는 주문에서 피킹 재최적화 효과를 다룬 연구.
- **ref-134**: 원문 미열람. 웨이브·웨이브리스 출고 지시 정책 비교 연구.
- **ref-044**: CBV 온톨로지 원본. arriving·receiving·accepting·loading·unloading 업무 단계 정의를 원문으로 확인.
- **ref-023**: Open-RMF 워크셀(디스펜서·인제스터) 연동 장. 배송 작업의 요청–결과 반복을 mdBook 원본으로 확인.
- **ref-049**: IngestorResult 메시지 정의. 요청 id·워크셀 id·상태 세 값을 원문으로 확인.
- **ref-121**: 원문 미열람. 워크플로 넷 건전성 판정의 계산 복잡도 연구.
- **ref-102**: 원문 미열람. 유통 물류센터 팔레트 이동 데이터로 AMR 플릿·충전기 규모를 시뮬레이션한 연구.
- **ref-098**: 원문 미열람. RMFS 의 충전·배터리 교환 전략을 대기행렬 모델로 비교한 연구.
- **ref-104**: Open-RMF 데모 README. 호텔·클리닉·공항 환경의 다중 플릿·승강기·문 공유를 원문으로 확인.
- **ref-060**: 원문 미열람. 병원 약품 배송 로봇의 승강기 가동률과 배송 실패·시간 관계를 관찰한 연구.
- **ref-103**: 원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기 대기·운행 시간을 모델링한 연구.
- **ref-105**: Open-RMF 플릿 어댑터 템플릿 설정. 충전 임계값·충전 목표·충전기·작업 종료 후 동작을 원문으로 확인.
- **ref-101**: RMFS 용 이산 사건 시뮬레이션 프레임워크 README를 원문으로 확인.
- **ref-148**: Open-RMF 로봇 상태 스키마. 상태 값·배터리·작업 id·문제 목록·위치·시각을 원문으로 확인.
- **ref-115**: 원문 미열람. 제조 처리량 병목 탐지 방법의 체계적 문헌 검토.
- **ref-149**: 원문 미열람. 창고 자재 이동 이벤트 로그에 프로세스 마이닝을 적용한 사례 연구.
- **ref-146**: 원문 미열람. RMFS 에너지 소비와 동적 우선순위 운영 정책의 성과 평가 연구.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/index.md | 5. 다른 대분류와의 연결 | 대분류 페이지의 다섯째 절 '다른 대분류와의 연결'만 patches 로 채운다. B. 공통 정보·환경 모델: f9·f10(2 ↔ 7), f18(4 ↔ 8) / C. 연결·실행 기반: f1·f2(1 ↔ 9), f3·f4·f5(1·2 ↔ 12), f15·f16(3 ↔ 10) / D. 계획·최적화: f6(1 ↔ 14), f7(1 ↔ 13), f13(3 ↔ 16), f14(3 ↔ 13), f20(4 ↔ 16) / E. 협업·현장 운영: f8(1 ↔ 20), f11(2 ↔ 17), f19(4 ↔ 19) / F. 도입·검증·유지관리: f12(2 ↔ 23), f17(3 ↔ 22), f21(4 ↔ 22, 8. 실시간 세계 상태·데이터 일관성과 구분) / G. 안전·보안·지능·거버넌스: f22(1 ↔ 28). 11. 분산 시스템·통신·컴퓨팅 구조와 27. AI·학습·적응과 모델 운영 등은 검증된 근거가 없어 쓰지 않는다. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 2회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 연결마다 게시 페이지의 단일 출처 또는 서로 다른 주장을 뒷받침하는 출처
    - f6·f7·f12·f13·f16·f19·f20·f21 근거 출처 원문 미열람(게시 페이지 인용 재사용)
    - f2·f8·f10·f22 는 추론이며 두 대분류 사이 매핑·규칙을 정한 표준·사례 미확인
- 범위 경계 위반 의심:
    - 없음
- 한계: web_fetch_available: false · fetch_mode mirror_only. 재사용 출처 가운데 10건(ref-031, ref-111, ref-129, ref-130, ref-044, ref-023, ref-049, ref-104, ref-105, ref-101, ref-148 중 GitHub 원본이 있는 것)을 raw.githubusercontent.com 으로 열어 확인했고, 나머지 재사용 출처는 원문 미열람(신뢰도 상한 medium). 근거는 게시된 1~4 세부영역 페이지 각주를 재사용했고 신규 출처는 0건이다. 검색 2회(영어 1, 한국어 1)는 WES–플릿 관리 연동 자료를 찾았으나 벤더·블로그 자료뿐이라 출처로 넣지 않았다. 연결 상대 세부영역 대부분이 seed 라 연결의 반대편 서술은 A 쪽 근거에 기댄다. 11. 분산 시스템·통신·컴퓨팅 구조 연결은 게시 전 브리프(2026-09-25-27)에만 있어 제외했다. 27. AI·학습·적응과 모델 운영과의 연결(자연어 업무 지시 챗봇 트랙이 1·2를 함께 필요한 영역으로 둠)은 검증된 주장이 없어 제외했다. 8. 실시간 세계 상태·데이터 일관성(f18)과 22. 시뮬레이션·예측용 디지털 트윈(f17·f21)을 구분했다. 새 열린 질문 없음: 관련 질문이 이미 oq-001·oq-010·oq-012·oq-018·oq-020·oq-021 로 열려 있다. 정정 요청 없음. 페이지 제안의 섹션 번호 '5'는 대분류 페이지의 다섯째 절(다른 대분류와의 연결)을 가리킨다.
