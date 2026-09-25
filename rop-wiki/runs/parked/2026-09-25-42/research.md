# 리서치 브리프 2026-09-25-42

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-42 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 17. 로봇 간 협업·물리적 인계 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시) 비어 있음
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 — 기존 각주는 ref-007 1건뿐
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(기존 oq-001, oq-006, oq-042 가 이 영역에 걸림)

## 조사 질문

1. AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? [분류원문] (섹션 3·5·6 겨냥)
2. 로봇–로봇·로봇–설비 인계를 요청·결과 메시지나 단계 신호로 표현하는 공개 규격·오픈소스(Open-RMF 워크셀, VDA 5050 pick/drop, SEMI E84)는 무엇을 규정하고 무엇을 비워 두는가? — oq-001·oq-042 관련 (섹션 4·7 겨냥)
3. 이동로봇이 작업대·로봇팔 앞에 정확히 섰는지(도킹·정지 위치 정밀도)를 재는 시험 방법과 도구는 무엇인가? (섹션 6·7·8 겨냥)
4. 서로 다른 로봇 작업 사이의 선후·동기화(스케줄 간 의존, 인계 스테이션·릴레이)를 다루는 배정·계획 연구는 무엇인가? (섹션 6·8·10 겨냥)
5. 공동 운반과 인식 결과 공유(협동 인지)는 연구에서 어떻게 정의되고 분류되는가? (섹션 4·8 겨냥)
6. 인계 완료를 재고·업무 이벤트로 기록할 때 GS1 CBV 업무 단계 어휘는 어떤 값을 제공하는가? — oq-006 관련 (섹션 4·10 겨냥)
7. 모바일 매니퓰레이터·이동로봇 협업의 안전 표준과 국내 자료·사례는 무엇이 있는가? (섹션 8·9·10 겨냥, 한국 자료 우선)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | NIST 의 Performance of Collaborative Robot Systems 프로젝트는 사람–로봇·로봇–로봇 협업 팀의 안전성과 효과를 평가하는 방법·프로토콜·지표를 목표로 하며, 제조사·기종이 다른 로봇이 함께 일하는 이종 로봇 워크셀의 통합·평가를 대상으로 삼고 로봇 간·사람–로봇 간 협업 통신 프로토콜 개발을 과제 영역 하나로 둔다. | ref-007 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | Open-RMF 배송 작업에서 로봇은 픽업 지점에서 DispenserResult 를 받을 때까지 DispenserRequest 를 반복해 보내고, 하역 지점에서 IngestorResult 를 받을 때까지 IngestorRequest 를 반복해 보내며, 워크셀은 주기적으로 상태(DispenserState·IngestorState)를 발행하고 이 흐름은 플릿 어댑터의 perform_deliveries 설정을 켜야 동작한다. | ref-023 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f3 | [사실] | Open-RMF 디스펜서 요청 메시지는 시각·요청 id(request_guid)·대상 워크셀 이름(target_guid)·운반체 유형(transporter_type)·품목 목록(품목 유형 id, 수량, 칸 이름)을 담고, 디스펜서 결과 메시지는 시각·요청 id·보낸 워크셀 id(source_guid)·상태(ACKNOWLEDGED, SUCCESS, FAILED)를 담는다. | ref-047, ref-048, ref-930 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f4 | [추정] | Open-RMF 워크셀 결과 메시지는 요청 단위의 성공·실패 상태만 담고 넘겨받은 화물의 개별 식별자나 실측 수량 필드가 없어, 인수 확인의 근거는 워크셀 자체 판단에 기대며 ROP 가 화물 식별·적재 상태 같은 별도 확인과 결합해야 할 것으로 보인다. | ref-930, ref-047, ref-048 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f5 | [사실] | VDA 5050 최신판(3.0.0)의 pick·drop 동작은 적재 장치(lhd), 스테이션 유형(예: 바닥, 랙, 수동·능동 컨베이어), 스테이션 이름, 적재물 유형·식별 번호(loadType, loadId), 높이·깊이 파라미터를 두며, pick 은 적재물이 로봇에 들어오고 로봇이 새 적재 상태를 보고하면 완료(FINISHED)로 본다. | ref-031 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f6 | [사실] | VDA 5050 은 관제–이동로봇 통신과 무관한 인터페이스(주변 설비, 인프라, 외부 IT 시스템)를 범위에서 제외하며, 3.0.0 판에도 로봇과 컨베이어·스테이션 사이 인계 신호 절차는 들어 있지 않다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f7 | [사실] | 반도체 업종의 SEMI E84 는 자동 반송 시스템(AMHS)과 생산 장비 로드포트 사이 캐리어 인계용 병렬 I/O 신호를 정하며, 장비가 인계 준비가 되었는지, 어느 로드포트를 쓸지, 인계가 진행 중인지·완료되었는지를 신호로 주고받는다. | ref-918, ref-919 | 예 | medium | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f8 | [추정] | SEMI E84 처럼 준비–진행–완료를 양쪽이 단계별로 확인하는 인계 신호 구조는, VDA 5050 이 비워 둔 이동로봇–작업대·로봇팔 인계 확인의 상태 모델을 ROP 가 정할 때 참고할 수 있을 것으로 보이나, 물류 업종에서 같은 역할을 하는 제조사 중립 공개 규격은 이번 조사에서 확인하지 못했다. | ref-918, ref-919, ref-031 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f9 | [사실] | NIST ARIAC 2025 시나리오에서 AGV 는 검사·조립·출하·재활용 스테이션 사이로 셀 트레이를 옮기고 검사 로봇팔이 합격 셀을 AGV 트레이에 올리며, 완성 키트를 실은 AGV 를 움직이기 전에 참가 팀은 키트 품질 확인 서비스를 호출해야 하고 트레이에 놓인 셀은 고정되어 검사 스테이션에서 다시 옮길 수 없다. | ref-008 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f10 | [사실] | ASTM F3499-21 은 무인운반차·자율이동로봇(A-UGV)이 전역 위치나 도크 같은 현장 설비 기준 위치에 정지할 때의 위치 반복성과, 포크 같은 적재 이송 장치의 높이 제어 반복성을 확인하는 시험 방법이다. | ref-920 | 아니오 | medium | 2021 | 제약 | 원문 미열람 |
| f11 | [사실] | NIST 는 ASTM F45 위원회에서 이동로봇·모바일 매니퓰레이터 시험 방법 개발에 참여하며, 매니퓰레이터에 단 카메라·센서로 기준 표식을 측정해 모바일 매니퓰레이터의 위치 불확도를 재는 재구성형 시험 기물(RMMA)을 설계했고 그 측정 불확도가 2 mm 수준이라고 보고했다. | ref-921, ref-922 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f12 | [사실] | ROS 2 Nav2 도킹 프레임워크는 충전 도크와 컨베이어·팔레트 같은 비충전 도크를 모두 지원하며, 준비 위치(staging pose)로 간 뒤 센서로 도크 위치를 다듬어 접근하고, 관절 부하 급증이나 거리 임계값으로 도킹 여부를 판정하며, 실패하면 기본 3회까지 재시도한다. | ref-216 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f13 | [사실] | Korsah·Stentz·Dias 의 다중 로봇 작업 배정 분류(iTax)는 작업 사이 의존을 의존 없음(ND)·일정 내 의존(ID)·스케줄 간 의존(XD)·복합 의존(CD)으로 나누며, 서로 다른 로봇에 배정된 작업 사이에 선후 제약 같은 관계가 있으면 스케줄 간 의존으로 본다. | ref-394 | 아니오 | medium | 2013 | 제약 | 원문 미열람 |
| f14 | [사실] | Coltin·Veloso(ICRA 2014)는 여러 이동로봇이 서로 물건을 옮겨 주는 전달(transfer)을 허용해 픽업·배송 계획을 개선하는 온라인 계획 알고리즘을 제시했다. | ref-924 | 아니오 | medium | 2014 | — | 원문 미열람 |
| f15 | [사실] | Zang 외(2026)는 구역에 묶인 플릿들이 도크 1개와 유한 버퍼를 가진 인계 스테이션으로 화물을 주고받는 지속형 다중 에이전트 픽업·배송 문제를 정식화하고, 공유 도크 예약 달력과 버퍼 점유 예측으로 경로를 승인하는 제어기(HARR)가 시뮬레이션에서 고정 도크 비교안보다 처리량을 최대 77% 높이고 적체를 92% 줄였다고 보고했다. | ref-925 | 아니오 | medium | 2026-07 | 예외·성과 | 원문 미열람 |
| f16 | [사실] | DELIVER(2025)는 보로노이 경계에서 로봇끼리 화물을 넘기는 릴레이 배송에서, 넘기는 로봇이 ROS 메시지나 LED 색 변화로 준비를 알리고 받는 로봇이 그 신호를 감지하면 움직이기 시작하는 가벼운 신호 방식을 쓴다. | ref-360 | 아니오 | medium | 2025-08 | 완료·인계 | 원문 미열람 |
| f17 | [사실] | Tuci 외(2018)는 로봇 한 대로 다루기에 너무 크거나 무거운 물체를 여러 로봇이 행동을 조율해 목적지까지 옮기는 협동 운반(cooperative object transport)을 검토하고, 운반·조율·제어 전략이 다양하게 제안되어 왔다고 정리했다. | ref-923 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f18 | [사실] | Singh 외(2024)는 로봇 플릿의 협동 인지를 여러 에이전트가 센서 정보를 공유·융합해 환경을 더 넓게 이해하고 판단을 돕는 능력으로 정의하고 관련 연구를 체계적으로 검토했다. | ref-928 | 아니오 | medium | 2024-03 | — | 원문 미열람 |
| f19 | [사실] | ANSI/A3 R15.08-2-2023 은 산업용 이동로봇(IMR)과 그 플릿을 현장에 통합·배치할 때의 안전 요구사항을 정하며, AMR·AGV 플랫폼에 매니퓰레이터를 부착한 IMR 유형 C(모바일 매니퓰레이터)를 다룬다. | ref-926 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f20 | [사실] | 국내에는 로봇 시스템과 그 통합의 안전 요구사항을 정한 한국산업표준 KS B ISO 10218-2(로봇 및 로봇 장치 — 산업용 로봇의 안전에 관한 요구사항 — 제2부: 로봇 시스템 및 통합)가 있다. | ref-927 | 아니오 | medium | 2026-09-25 | 제약 | 원문 미열람 |
| f21 | [사실] | GS1 CBV 온톨로지는 업무 단계 accepting 을 물체의 점유·소유가 바뀌는 활동으로, receiving 을 물체가 한 위치에서 받아들여져 받는 쪽 재고에 더해지는 활동으로 정의하고, loading·unloading 은 운송 수단(shipping conveyance)에 싣고 내리는 활동으로 정의한다. | ref-044 | 아니오 | medium | 2021-09-30 | 완료·인계 | — |
| f22 | [추정] | 시설 안 로봇 사이·로봇과 작업대 사이의 물리적 인계는 CBV 에서 점유 이동을 뜻하는 accepting 이나 재고 편입을 뜻하는 receiving 에 가깝고 운송 수단 기준의 loading·unloading 과는 맞지 않아, 인계 이벤트의 업무 단계 값은 ROP 가 정해야 할 것으로 보인다. | ref-044 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f23 | [사실] | 국내에서는 유진로봇이 과학기술정보통신부·정보통신기획평가원의 스마트제조혁신기술개발사업으로 자율이송 모바일 매니퓰레이터 기반 지능형 제조 물류시스템 개발을 추진한다고 보도되었다. | ref-929 | 아니오 | low | 2025-11-04 | — | 원문 미열람 |
| f24 | [추정] | 분류 원문 질문(AMR 이 가져온 물건을 로봇팔이 안전하게 인수했음을 어떻게 확인할까)에 대해, 이동로봇의 도킹·정지 위치 확인, 로봇팔·워크셀의 인수 결과(SUCCESS), 이동로봇의 적재 상태 변경 보고라는 서로 독립된 신호가 모두 일치할 때 인계 완료로 인정하는 방식이 가능할 것으로 보인다. | ref-216, ref-930, ref-031, ref-920 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f25 | [추정] | 피킹 단계에서 인계가 실패하면(워크셀 결과 FAILED, 도킹 재시도 한도 초과, 동작 FAILED) 인계 재시도·다른 작업대로 재배정·사람 확인 가운데 하나로 넘겨야 하며, 대기 동안 이동로봇과 작업대가 함께 묶여 처리량 손실이 생길 것으로 보인다. | ref-930, ref-216, ref-031, ref-925 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f26 | [추정] | 보충 단계에서 이동로봇 운반과 로봇팔 적치처럼 서로 다른 로봇의 작업이 선후로 이어지면 스케줄 간 의존이 생기고, 인계 스테이션의 도크·버퍼가 공용 자원 제약이 되므로 인계 시점을 두 로봇 일정에 함께 맞춰야 할 것으로 보인다. | ref-394, ref-925 | 아니오 | low | 2026-09-25 | 보충 / 제약 | 원문 미열람 |
| f27 | [추정] | ROP 가 직접 맡을 범위는 인계 작업의 순서·시점 동기화, 인계 요청·결과 신호의 중계, 여러 확인 신호를 모은 인계 완료 판정, 그 결과의 재고·업무 시스템 반영일 것으로 보인다. | ref-023, ref-031, ref-044 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f28 | [추정] | 연계 대상: 로봇팔의 파지·동작 제어, 이동로봇의 도킹 주행 제어와 센서 인식, 컨베이어 PLC 와 설비 안전 제어는 로봇·설비 제조사가 맡고 ROP 는 그 결과 상태와 실패 신호를 받는 것으로 보인다. | ref-216, ref-031, ref-926 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f29 | [추정] | 이 영역은 워크셀·컨베이어 인계로 10. 설비·건물 시스템 연동과, 인계 이벤트 기록으로 7. 화물·재고·자산 식별과 추적과, 스케줄 간 의존으로 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링과, 인계 스테이션 도크 예약으로 16. 공용 자원·충전·에너지 최적화와, 인계 실패 처리로 20. 예외 복구·재계획·업무 연속성과, 도킹 시험·ARIAC 로 23. 시험·형식 검증·벤치마크와, 모바일 매니퓰레이터 안전으로 25. 안전·위험 관리와 이어질 것으로 보인다. | ref-023, ref-044, ref-394, ref-925, ref-920, ref-008, ref-926 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 검색 요약: 'heterogeneous robot workcells (i.e., robots of different makes and models working together)'; 네 과제 영역에 협업 통신 프로토콜 개발 포함. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f2**: integration_workcells.md 원본(github_raw): 'Requests a DispenserRequest till receives a DispenserResult. (Done Dispensing)', 하역도 같은 방식. (발행일 미확인, 확인일 기준)
- **f3**: DispenserRequest.msg·DispenserRequestItem.msg·DispenserResult.msg 원본(github_raw): type_guid, quantity, compartment_name; status ACKNOWLEDGED=0 SUCCESS=1 FAILED=2. 같은 저장소라 독립 교차 아님. (발행일 미확인, 확인일 기준)
- **f4**: f3 의 필드 목록에서 도출. 결과 메시지에 품목 필드 없음, 요청 품목은 유형 id·수량뿐. 이 위키의 추론(oq-001 관련).
- **f5**: VDA5050_EN.md 원본(github_raw): pick 완료 = 'Load has entered the mobile robot and mobile robot reports new load state'; 적재 장치가 여럿이면 lhd 필요(예: LHD1). (발행일 미확인, 확인일 기준)
- **f6**: VDA5050_EN.md 원본: 'interfaces to peripheral equipment, infrastructure components, or external IT systems' 제외. stationType 은 파라미터일 뿐 설비와의 핸드셰이크는 규정하지 않음. (발행일 미확인, 확인일 기준)
- **f7**: 검색 요약: 'handoff carriers between the production equipment and the AMHS'; 신호가 준비 여부·사용 로드포트·진행·완료를 나타냄. 개별 신호 이름·순서는 원문(유료) 미열람으로 확인 못함. (발행일 미확인, 확인일 기준)
- **f8**: f6(주변 설비 인터페이스 범위 제외)과 f7(E84 인계 신호)을 대응시킨 이 위키의 추론. 한·영 검색 각 1회에서 물류 AMR–컨베이어 공개 핸드셰이크 규격 미발견(oq-042).
- **f9**: scenario.rst 원본(github_raw): move agv action, check kit quality service, 'Cells lock to the tray after they are placed and cannot be moved at the inspection station'. (발행일 미확인, 확인일 기준)
- **f10**: 검색 요약: positioning 은 'repeatability of A-UGV location when stationary after completing maneuvers to a stop location'; 'height control of load transfer equipment, for example an A-UGV with fork tines'. 원문 미열람.
- **f11**: 검색 요약: RMMA 는 'positioning uncertainty of mobile manipulators within a measurement uncertainty of 2 mm'; 도킹 실험 결과 반복 가능. 두 출처 모두 NIST 계열이라 독립 교차 아님. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f12**: nav2_docking README 원본(github_raw): isDocked()·isCharging(), 'N retries may be made, driving back to the dock's staging pose'. (발행일 미확인, 확인일 기준)
- **f13**: 검색 요약: 'no dependencies (ND), in-schedule dependencies (ID), cross-schedule dependencies (XD), and complex dependencies (CD)'. 원문 미열람.
- **f14**: 검색 요약: 'robots transfer objects to optimize a pickup and delivery plan', ICRA 2014, 5786–5791쪽. 원문 미열람.
- **f15**: 검색 요약: 'handover stations equipped with single docks and finite buffers, which are vulnerable to blocking and starvation'; 수치는 저자 보고·시뮬레이션·중간 부하 조건. 원문 미열람.
- **f16**: 검색 요약: 'the sending robot signals readiness via a ROS message or LED color change, and the receiving robot initiates motion upon detecting this signal'. 원문 미열람.
- **f17**: 검색 요약: 'coordinate their actions to transport objects from a starting position to a final destination'; Frontiers in Robotics and AI 5:59. 원문 미열람.
- **f18**: 검색 요약: 'share and integrate their sensory information for a more comprehensive understanding of their environment'. ECCV 2024 워크숍 게재. 원문 미열람.
- **f19**: 검색 요약: Part 2 는 'integrating, configuring, and customizing an IMR or fleet of IMRs into a site'; 'IMR Type C: ... mobile platform with a manipulator as the attachment'. 원문 미열람.
- **f20**: KSSN 표준 정보 검색 결과의 표준 번호·제목. 판·확인 연도와 이동식 로봇 적용 조항은 원문 미열람으로 확인 못함. (발행일 미확인, 확인일 기준)
- **f21**: CBV.ttl 원본(github_raw): accepting 'an object changes possession and/or ownership'; receiving '... added to the receiver's inventory'; loading 'loaded into shipping conveyance'.
- **f22**: f21 정의에서 도출한 이 위키의 추론. 로봇 인계에 쓸 CBV 값을 권고한 GS1 문서는 확인 못함(oq-006).
- **f23**: 검색 요약(기사): '자율이송 모바일 매니플레이터 기반 지능형 제조 물류시스템 개발 사업', 스마트제조혁신기술개발사업 일환. 1차 출처(과제 공고) 미확인. 원문 미열람.
- **f24**: f10·f12(도킹 확인), f3(워크셀 결과 상태), f5(pick 완료 = 새 적재 상태 보고)를 SCM 질문에 대응시킨 추론. 세 신호를 결합하는 규정은 어느 표준에서도 확인 못함.
- **f25**: f3(FAILED 상태), f12(재시도 3회 기본), f5(동작 상태), f15(인계 스테이션의 차단·고갈)를 예외·성과 항목에 대응시킨 추론. 현장 사례 미확인.
- **f26**: f13(XD)과 f15(도크 예약·버퍼 제약)를 보충 흐름의 제약 항목에 대응시킨 추론.
- **f27**: f2(요청–결과 중계), f6(VDA 5050 이 비워 둔 설비 인계), f21(업무 이벤트 어휘)을 분류 원문 9장 경계에 대응시킨 추론.
- **f28**: f12(도킹은 로봇 쪽 내비게이션 스택 기능), f6(주변 설비 인터페이스 범위 밖), f19(IMR 통합 안전)에서 도출. 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 경계.
- **f29**: f2·f21·f13·f15·f25·f10·f9·f19 를 영역 연결로 정리한 추론. 적재 장치 선언(lhd)은 5. 로봇 능력·작업 온톨로지와도 연결.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-007 | NIST | Performance of Collaborative Robot Systems | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/performance-collaborative-robot-systems | 예 |
| ref-008 | NIST | ARIAC Documentation | 미확인 | 정부·연구기관 | high | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/ | 아니오 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | high | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 아니오 |
| ref-048 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 아니오 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md | 아니오 |
| ref-360 | arXiv 2508.19114 저자(미확인) | DELIVER: A System for LLM-Guided Coordinated Multi-Robot Pickup and Delivery using Voronoi-Based Relay Planning | 2025-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2508.19114 | 예 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 예 |
| ref-918 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | 표준 | medium | 2026-09-25 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 예 |
| ref-919 | PEER Group | SEMI E84: Carrier Handoff | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.peergroup.com/definition-of-standard/semi-e84/ | 예 |
| ref-920 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | 표준 | medium | 2026-09-25 | https://www.astm.org/f3499-21.html | 예 |
| ref-921 | NIST | Design and Application of the Reconfigurable Mobile Manipulator Artifact (RMMA) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/publications/design-and-application-reconfigurable-mobile-manipulator-artifact-rmma | 예 |
| ref-922 | Bostelman, R. 외(NIST) | Mobile Robot and Mobile Manipulator Research Towards ASTM Standards Development | 미확인 | 논문 | medium | 2026-09-25 | https://pubmed.ncbi.nlm.nih.gov/28690359/ | 예 |
| ref-923 | Tuci, E., Alkilabi, M. H. M., & Akanyeti, O. | Cooperative Object Transport in Multi-Robot Systems: A Review of the State-of-the-Art | 2018 | 논문 | medium | 2026-09-25 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00059/full | 예 |
| ref-924 | Coltin, B., & Veloso, M. | Online pickup and delivery planning with transfers for mobile robots | 2014 | 논문 | medium | 2026-09-25 | https://www.researchgate.net/publication/289338501_Online_pickup_and_delivery_planning_with_transfers_for_mobile_robots | 예 |
| ref-925 | Zang, C. 외 | Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.17724 | 예 |
| ref-926 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 2023 | 표준 | medium | 2026-09-25 | https://webstore.ansi.org/standards/ria/ansia3r15082023 | 예 |
| ref-927 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 예 |
| ref-928 | Singh, A., Raut, G., & Choudhary, A. | Multi-agent Collaborative Perception for Robotic Fleet: A Systematic Review | 2024-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2405.15777 | 예 |
| ref-929 | 다음뉴스 게재 기사(원 언론사 미확인) | 유진로봇, 지능형 제조 물류시스템 공개 | 2025-11-04 | 기사 | low | 2026-09-25 | https://v.daum.net/v/20251104092138920 | 예 |
| ref-930 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserResult.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg | 아니오 |

### 출처 요약

- **ref-007**: 원문 미열람. 사람–로봇·로봇–로봇 협업 팀과 이종 로봇 워크셀의 협업 성능을 평가하는 시험 방법·지표·통신 프로토콜 개발 프로젝트(검색 요약 기준).
- **ref-008**: ARIAC 문서. 이번 실행은 2025 시나리오의 AGV 스테이션 이동, 로봇팔의 트레이 적재, 이동 전 키트 품질 확인 서비스를 원본으로 확인했다.
- **ref-023**: 디스펜서·인제스터 워크셀과 배송 작업의 요청–결과 반복 방식을 설명한 장. 이번 실행에서 mdBook 원본을 열었다.
- **ref-031**: VDA 5050 최신판(3.0.0) 명세 원문. 이번 실행은 pick·drop 파라미터와 완료 조건, 주변 설비 인터페이스의 범위 제외를 확인했다.
- **ref-044**: CBV 업무 단계·상태 어휘 온톨로지. 이번 실행은 accepting·receiving·loading·unloading 등의 정의를 원본으로 확인했다.
- **ref-047**: 디스펜서 요청 메시지(시각, 요청 id, 대상 워크셀, 운반체 유형, 품목 목록). 이번 실행에서 원본을 열었다.
- **ref-048**: 디스펜서 요청 품목(품목 유형 id, 수량, 칸 이름). 이번 실행에서 원본을 열었다.
- **ref-216**: 충전·비충전 도크 도킹 절차(준비 위치, 도크 위치 보정, 도킹 판정, 재시도)를 설명한 README. 이번 실행에서 원본을 열었다.
- **ref-360**: 원문 미열람. 보로노이 경계에서 로봇끼리 화물을 넘기는 릴레이 배송과 가벼운 준비 신호 방식을 다룬 프리프린트.
- **ref-394**: 원문 미열람. 작업 사이 의존(ND·ID·XD·CD)을 포함한 다중 로봇 작업 배정 분류 iTax 를 제시한 논문.
- **ref-918**: 원문 미열람. 자동 반송 시스템과 생산 장비 로드포트 사이 캐리어 인계용 병렬 I/O 신호를 정한 SEMI 표준의 발행 기관 판매 페이지(유료 원문).
- **ref-919**: 원문 미열람. 반도체 자동화 소프트웨어 업체의 SEMI E84 해설 페이지로, 도착 뒤 신호 교환으로 인계 준비·진행·완료를 확인한다고 설명한다.
- **ref-920**: 원문 미열람. A-UGV 의 정지·도킹 위치 반복성과 적재 이송 장치 높이 제어 반복성을 확인하는 시험 방법.
- **ref-921**: 원문 미열람. 모바일 매니퓰레이터의 위치 불확도를 기준 표식으로 재는 시험 기물(RMMA)의 설계와 적용을 다룬 NIST 발행물.
- **ref-922**: 원문 미열람. ASTM F45 표준 개발을 위한 NIST 의 이동로봇 도킹·모바일 매니퓰레이터 성능 측정 연구를 정리한 논문.
- **ref-923**: 원문 미열람. 여러 로봇이 행동을 조율해 크거나 무거운 물체를 옮기는 협동 운반 연구를 검토한 Frontiers in Robotics and AI 리뷰.
- **ref-924**: 원문 미열람. 이동로봇 사이 물건 전달을 허용해 픽업·배송 계획을 개선하는 온라인 알고리즘(ICRA 2014).
- **ref-925**: 원문 미열람. 도크 1개·유한 버퍼의 인계 스테이션으로 화물을 주고받는 다중 서브시스템 픽업·배송 문제와 도크 예약·버퍼 예측 제어기(HARR)를 제시한 프리프린트.
- **ref-926**: 원문 미열람. 산업용 이동로봇 시스템·응용·플릿의 현장 통합 안전 요구사항을 정한 미국 국가표준으로, 매니퓰레이터를 단 이동로봇(유형 C)을 다룬다.
- **ref-927**: 원문 미열람. 산업용 로봇 시스템과 그 통합의 안전 요구사항을 정한 한국산업표준의 표준 정보 페이지.
- **ref-928**: 원문 미열람. 로봇 플릿에서 여러 에이전트가 센서 정보를 공유·융합하는 협동 인지 연구를 검토한 논문(ECCV 2024 워크숍).
- **ref-929**: 원문 미열람. 유진로봇의 자율이송 모바일 매니퓰레이터 기반 지능형 제조 물류시스템 국책과제를 전한 기사(검색 요약 기준).
- **ref-930**: 디스펜서 결과 메시지(시각, 요청 id, 워크셀 id, 상태 ACKNOWLEDGED·SUCCESS·FAILED). 이번 실행에서 원본을 열었다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절: f1(NIST 이종 로봇 협업 평가), f6·f8(인계 신호의 표준 공백), f24(SCM 질문) / 4절: f13(스케줄 간 의존), f17(협동 운반), f18(협동 인지), f21(CBV accepting·receiving), f2·f3(디스펜서·인제스터 요청–결과) / 5절: f24(피킹, 완료·인계), f25(피킹, 예외·성과), f26(보충, 제약) / 6절: f2·f4·f5·f12·f14·f15·f16·f24 / 7절: f2·f3(Open-RMF 워크셀), f5·f6(VDA 5050 pick·drop과 범위 제외), f7(SEMI E84), f10(ASTM F3499), f12(Nav2 도킹), f19·f20(R15.08-2, KS B ISO 10218-2) / 8절: f1·f9·f11·f13·f14·f15·f16·f17·f18·f23(국내 자료 f20·f23 포함) / 9절: f27(직접 범위), f28(연계 대상: 파지·도킹 주행·PLC·설비 안전 제어) / 10절: f29(7·10·13·14·16·20·23·25번, 5번은 lhd 선언), f22(7. 화물·재고·자산 식별과 추적, oq-006) / 11절: 기존 oq-001·oq-006·oq-042 연결과 새 열린 질문. f7 은 반도체 업종 규격이라 업종 차이를 병기, f23 은 기사 1건이라 한계 병기. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 모바일 매니퓰레이터 | Mobile Manipulator | AMR·AGV 같은 이동 플랫폼에 로봇팔을 결합해 이동과 집기·놓기 작업을 함께 수행하는 로봇이다. |
| 협동 운반 | Cooperative Object Transport | 로봇 한 대로 다루기 어려운 크거나 무거운 물체를 여러 로봇이 행동을 조율해 목적지까지 함께 옮기는 일이다. |
| 협동 인지 | Collaborative Perception | 여러 로봇이 센서 정보나 인식 결과를 공유·융합해 한 대가 볼 때보다 넓고 정확하게 환경을 파악하는 방식이다. |
| 스케줄 간 의존 | Cross-schedule Dependency (XD) | 서로 다른 로봇에 배정된 작업 사이에 선후 같은 관계가 있어, 한 로봇의 작업 적합성이 다른 로봇의 일정에 따라 달라지는 작업 의존 유형이다. |

## 열린 질문

새로 생긴 질문:

- 로봇팔·워크셀의 인수 결과와 이동로봇의 적재 상태 보고가 어긋날 때(한쪽은 성공, 다른 쪽은 적재 유지) 어느 신호를 기준으로 인계 완료를 판정하는지 정한 표준이나 현장 사례가 있는가? | 관련 영역: 17. 로봇 간 협업·물리적 인계, 8. 실시간 세계 상태·데이터 일관성 | 근거: f24 | 종류: 일반
- 반도체 업종의 SEMI E84 같은 단계별 인계 신호를 물류센터의 이동로봇–컨베이어·작업대 인계에 적용하거나 옮긴 사례가 있는가? | 관련 영역: 17. 로봇 간 협업·물리적 인계, 10. 설비·건물 시스템 연동 | 근거: f7 | 종류: 일반
- ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? | 관련 영역: 17. 로봇 간 협업·물리적 인계, 23. 시험·형식 검증·벤치마크 | 근거: f10 | 종류: 일반
- 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? | 관련 영역: 17. 로봇 간 협업·물리적 인계, 25. 안전·위험 관리 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 1
- 예산 사용량: 검색 21회 · 신규 출처 13건
- 미확인 항목:
    - f7 SEMI E84 개별 신호 이름·순서는 유료 원문 미열람으로 확인 못함
    - f11 RMMA 2 mm 수치는 NIST 계열 출처뿐으로 독립 교차 확인 실패
    - f15 처리량·적체 수치는 저자 보고 시뮬레이션 결과
    - f20 KS B ISO 10218-2 의 판·확인 연도와 이동식 로봇 적용 조항 미확인
    - f23 국책과제 1차 출처(공고·과제 정보) 미확인, 기사 원 언론사 미확인
    - ref-922 발행연도 미확인
    - 물류 업종의 이동로봇–컨베이어 제조사 중립 인계 규격은 찾지 못함(oq-042 미해결)
    - 공동 운반(협동 운반)의 물류센터 적용 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f28: 로봇팔 파지·도킹 주행 제어·컨베이어 PLC·설비 안전 제어는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 영역이라 claim 을 '연계 대상: '으로 표시함
    - f7·f8: SEMI E84 는 반도체 업종 규격이라 물류센터 직접 적용 근거가 아니라 참고 사례로만 제안함
    - f19·f20: 안전 표준은 25. 안전·위험 관리의 내용이며 이 영역에서는 제약으로만 연결하도록 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-008(ARIAC scenario.rst)·ref-023(workcells)·ref-031(VDA 5050 main)·ref-044(CBV.ttl)·ref-047·ref-048(디스펜서 요청 메시지)·ref-216(nav2_docking README), 신규 ref-930(DispenserResult.msg). 그 밖의 신규 12건과 재사용 ref-007·ref-360·ref-394 는 원문 미열람(신뢰도 상한 medium). 검색 21회/30(영어 13, 한국어 8), 신규 출처 13건/15(ref-918~ref-930, 예약 구간 안), 재사용 10건. 교차 확인 1건(f7). 입력의 정정 요청 없음. 한국 자료: KS B ISO 10218-2(ref-927), 유진로봇 국책과제 기사(ref-929); 국내 학술 논문으로 이동로봇–로봇팔 인계 확인을 다룬 것은 찾지 못했다. oq-042 는 f6·f7·f8 로 일부 답했으나(VDA 5050 은 범위 밖, 반도체 E84 존재) 물류 업종 중립 규격을 찾지 못해 해결 제안하지 않았다. oq-006 은 f21·f22 로 CBV 정의를 보강했을 뿐 해결하지 않았다. 27. AI·학습·적응과 모델 운영 관련 finding 은 내지 않았다(f16 의 LLM 은 계획용이며 인계 신호 방식만 인용). 8. 실시간 세계 상태·데이터 일관성(현재 인계 상태 판정)과 22. 시뮬레이션·예측용 디지털 트윈(ARIAC 같은 시뮬레이션 평가)은 섞지 않고 ARIAC 는 23. 시험·형식 검증·벤치마크 쪽으로 연결했다.
