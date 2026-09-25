# 리서치 브리프 2026-09-25-60

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-60 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- E. 협업·현장 운영 대분류 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음)
- 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(제한 운영 처리량 추정, oq-081): 22. 시뮬레이션·예측용 디지털 트윈 페이지가 seed 상태라 게시된 근거 없음
- 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스 ↔ 26. 사이버보안·접근권한·개인정보, 24. 자산·소프트웨어 수명주기 관리, 21. 온보딩·설정·현장 시운전: 게시된 E. 협업·현장 운영 세부영역 페이지에 검증된 근거 없음
- 5. 로봇 능력·작업 온톨로지·6. 지도·공간·위치 모델 ↔ E. 협업·현장 운영 세부영역: E 쪽 게시 페이지에 직접 근거 없음

## 조사 질문

1. 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]
2. 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [분류원문] — 20. 예외 복구·재계획·업무 연속성이 A. 업무·공급망 설계, B. 공통 정보·환경 모델, C. 연결·실행 기반, D. 계획·최적화와 넘겨받는 지점은 무엇인가? (oq-021, oq-038, oq-048, oq-079 관련)
3. 17. 로봇 간 협업·물리적 인계의 인계 확인 신호는 7. 화물·재고·자산 식별과 추적, 10. 설비·건물 시스템 연동, 14. 작업 순서·스케줄링, 23. 시험·형식 검증·벤치마크, 25. 안전·위험 관리와 어떻게 이어지는가? (oq-001, oq-006, oq-042, oq-062, oq-063, oq-064)
4. 18. 사람–로봇 협업·운영 인터페이스는 3. 처리능력·거점·설비 계획, 9. 로봇·제조사 관제 연동, 13. 작업 배정 — MRTA, 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영과 무엇을 주고받는가? (oq-009, oq-070, oq-072)
5. 19. 모니터링·이상 탐지·원인 분석은 4. 성과·경제성·프로세스 개선, 8. 실시간 세계 상태·데이터 일관성, 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스와 어떻게 연결되는가? (oq-018, oq-033, oq-073)
6. E. 협업·현장 운영과 다른 대분류의 연결 가운데 근거가 아직 없는 쌍은 무엇인가? (다루지 않은 연결 목록)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: VDA 5050 3.0.0 에서 관제가 주문 취소(cancelOrder)를 보내면 예정된 동작은 취소되어 동작 상태를 FAILED 로 보고한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [추정] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 상위 시스템의 취소가 로봇이 화물을 실은 뒤에 오면 로봇 쪽 동작 실패 보고만으로는 화물 위치가 정해지지 않으므로, 되돌림 작업과 재고 반영 규칙을 정하는 일이 두 대분류가 넘겨받는 지점이 될 것으로 보이며 이를 정한 표준·사례는 확인되지 않았다(oq-021). | ref-031, ref-489 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f3 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: 시설 안 로봇 사이·로봇과 작업대 사이의 물리적 인계는 CBV 의 accepting·receiving 에 가깝고 운송 수단 기준의 loading·unloading 과 맞지 않아, 인계 이벤트의 업무 단계 값을 ROP 쪽에서 정해야 할 것으로 보인다(oq-006). | ref-044 | 아니오 | low | 2021-09-30 | 완료·인계 | 원문 미열람 |
| f4 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: VDA 5050 상태 스키마의 선택 필드 loads 의 loadId 는 바코드·RFID 같은 적재물 식별 번호로, 멈춘 로봇에 어떤 화물이 실렸는지 관제가 알 수 있게 하지만 적재물을 식별할 수 없는 로봇은 생략할 수 있다. | ref-051 | 아니오 | medium | 2026-09-25 | 피킹 / 작업 대상 | — |
| f5 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적: EPCIS 1.2 는 이미 기록된 이벤트를 오류 선언(errorDeclaration)으로 정정하게 하므로, 회수한 화물의 재고·이벤트 기록 정정이 식별·추적 쪽 기록 규칙에 기대게 된다. | ref-492 | 아니오 | medium | 2016-09-29 | 완료·인계 | 원문 미열람 |
| f6 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: 지연 원인을 문·로봇·통신으로 가르려면 같은 시각의 문 모드(closed·moving·open·offline·unknown)와 작업 상태(delayed·blocked 등)를 한 시간축에 맞춘 현재 상태 기록이 필요할 것으로 보이며, 이는 현재 상태를 표현하는 쪽이지 가정한 미래를 실험하는 22. 시뮬레이션·예측용 디지털 트윈의 일이 아니다. | ref-313, ref-111 | 아니오 | low | 2026-09-25 | 보충 / 예외·성과 | 원문 미열람 |
| f7 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석·20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 상태 스키마의 오류 수준은 WARNING·URGENT·CRITICAL·FATAL 네 값이고, 연결 스키마는 연결 끊김을 CONNECTION_BROKEN 으로 보고한다. | ref-051, ref-449 | 아니오 | medium | 2026-09-25 | 시작 조건 | — |
| f8 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 작업 상태·VDA 5050 오류·MassRobotics 운용 상태(waitingExternalEvent 등)가 서로 다른 어휘로 보고되어, 이를 ROP 의 공통 원인 범주로 옮기는 매핑이 두 대분류 사이에 필요할 것으로 보이며 공통 매핑 표준은 확인되지 않았다(oq-033). | ref-051, ref-230, ref-111 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 문 노드는 문 상태를 /door_states 로 발행하고 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 해, 설비 원인 판정의 근거가 된다. | ref-313, ref-283 | 아니오 | medium | 2026-09-25 | 보충 / 제약 | 원문 미열람 |
| f10 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 배송 작업에서 로봇은 픽업 지점에서 DispenserResult 를, 하역 지점에서 IngestorResult 를 받을 때까지 요청을 반복해 보내고 워크셀은 /dispenser_states·/ingestor_states 로 상태를 주기적으로 발행하며, 이 흐름은 플릿 어댑터의 perform_deliveries 설정이 켜져야 동작한다. | ref-023 | 아니오 | medium | 2026-09-25 | 보충 / 완료·인계 | — |
| f11 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 반도체 업종 SEMI E84 처럼 준비–진행–완료를 양쪽이 단계별로 확인하는 인계 신호 구조는 이동로봇–작업대 인계 상태 모델의 참고가 될 수 있으나, VDA 5050 은 주변 설비 인터페이스를 범위에서 제외하고 물류 업종의 제조사 중립 인계 신호 규격은 확인되지 않았다(oq-042, oq-062). | ref-202, ref-203, ref-031 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f12 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f13 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 은 교착(deadlock)과 통신 오류의 탐지·해소를 관제(fleet control)의 기능으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f14 | [추정] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: 오류·연결 상태 수신, 주문 일시정지·취소, Open-RMF 로봇 갱신 핸들을 통한 재계획 요청·작업 수락 중지가 실행 신뢰성 계층과 복구 결정이 맞물리는 지점이 될 것으로 보인다. | ref-031, ref-537 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f15 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 교통 스케줄은 지연·취소·경로 변경을 반영해 계속 바뀌는 데이터베이스이고, 충돌이 예상되면 관련 플릿 관리자가 서로를 수용하는 경로로 협상한다. | ref-004 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f16 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: 지연에 강건한 계획 실행(행동 의존 그래프, Hönig 외 2019)과 지연된 로봇의 통과 순서 재스케줄(Feng 외 2024)이 연구되어, 실행 중 지연 복구가 경로 계획 연구와 이어진다. | ref-188, ref-483 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 작업 의존성·우선순위 선점·고장 복구를 함께 다루는 다중 로봇 작업 배정 방법(Kalempa 외 2021)이 있어, 고장 로봇의 남은 작업 재배정이 배정 문제로 넘어간다. | ref-484 | 아니오 | medium | 2021-09-30 | 수행 자원 | 원문 미열람 |
| f18 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링: 사람 피커와 AMR 의 협동 피킹 연구는 두 자원의 조율을 배치 구성·배치 순서와 작업 완료 시각(makespan) 최소화 문제로 다룬다. | ref-467, ref-468 | 아니오 | medium | 2023 | 피킹 / 수행 자원 | 원문 미열람 |
| f19 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ D. 계획·최적화의 14. 작업 순서·스케줄링·16. 공용 자원·충전·에너지 최적화: 이동로봇 운반과 로봇팔 적치가 선후로 이어지면 스케줄 간 의존이 생기고 인계 스테이션의 도크·버퍼가 공용 자원 제약이 되어 인계 시점을 두 로봇 일정에 함께 맞춰야 할 것으로 보인다. | ref-394, ref-209 | 아니오 | low | 2026-07 | 보충 / 제약 | 원문 미열람 |
| f20 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 협동 피킹 시스템에서 피커와 로봇의 투입 수를 정하는 연구(Yang 외 2026-03)가 있어 인원·로봇 비율 결정이 처리능력 계획과 이어지나, 교대조 단위 결정 여부는 미확인이다(oq-009). | ref-469 | 아니오 | medium | 2026-03 | 피킹 / 수행 자원 | 원문 미열람 |
| f21 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: AGV 시스템 병목 탐지 방법 비교 연구(Roser 외 2003)는 가동률·대기 시간 기반 방법에 이동 병목 탐지 대비 한계가 있다고 보고해, 원인·병목 판정 방식이 개선 대상 선정과 이어진다(oq-018). | ref-451 | 아니오 | medium | 2003 | 예외·성과 | 원문 미열람 |
| f22 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 상태 메시지는 운용 모드(STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN)와 비상정지 종류(MANUAL·REMOTE·NONE)를 보고해, 사람 개입 상태가 관제 연동을 통해 운영 인터페이스로 들어온다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f23 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 데모는 시설 비상 경보 때 로봇을 가장 가까운 주차 위치로 보내는 흐름을 보인다. | ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f24 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 도킹 정지 위치의 반복성을 확인하는 시험 방법 ASTM F3499-21 이 있고, NIST ARIAC 2025 는 완성 키트를 실은 AGV 를 움직이기 전에 품질 확인 서비스를 호출하게 해 이동 전 인계 확인을 평가한다. | ref-204, ref-008 | 아니오 | medium | 2021 | 완료·인계 | — |
| f25 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: NIST 협업 로봇 시스템 성능 프로젝트는 사람–로봇·로봇–로봇 협업 팀의 안전성과 효과를 평가하는 방법·지표 개발을 목표로 한다. | ref-007 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f26 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: ANSI/A3 R15.08-2-2023 은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C 로 다루며 시스템·적용 단위 안전 요구를 정한다. | ref-210 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f27 | [추정] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: 사람 감지·보호 필드·비상정지 같은 안전 기능은 로봇 제조사·현장 통합사가 갖추고, ROP 는 로봇이 보고한 안전 상태를 표시하고 재개·수동 전환 승인을 작업 흐름에 반영하는 경계가 될 것으로 보인다. | ref-470, ref-051, ref-210 | 아니오 | low | 2026-09-25 | 제약 | — |
| f28 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: 국내에서는 고용노동부가 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했고, 중소벤처기업부는 2024-11 대구 규제자유특구 실증을 거쳐 이동식 협동로봇 산업표준이 제정되었다고 발표했다. | ref-473, ref-475 | 아니오 | medium | 2024-11 | 제약 | 원문 미열람 |
| f29 | [사실] | E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, Ren 외 2023)와 사용자 명령을 분류·모호성 해소하는 연구(CLARA, Park 외 2024), 실행 전 안전 게이트 연구(Obi 외 2026-04)가 있어 자연어 지시 인터페이스가 AI 연구 방법과 이어진다. | ref-351, ref-353, ref-417 | 아니오 | medium | 2026-04 | — | 원문 미열람 |
| f30 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석·18. 사람–로봇 협업·운영 인터페이스 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 로봇 실패에 대한 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구(Das 외 2021)가 있어, 분류 원문 8장 교차 규칙의 장애 분석이 원인 분석 결과를 사람에게 전달하는 인터페이스까지 이어진다. | ref-476 | 아니오 | medium | 2021-01 | 예외·성과 | 원문 미열람 |
| f31 | [추정] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스: 표준마다 상태·오류 어휘가 다르고 공통 매핑 표준이 확인되지 않으므로, 이종 플릿의 오류 수준·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-033, oq-073). | ref-051, ref-230, ref-111 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 명세 원문: 예정된 동작이 있으면 "these actions shall be cancelled and report 'FAILED' in their actionState". (VDA 5050 3.0.0, GitHub main)
- **f2**: cancelOrder 뒤 남은 동작은 FAILED 로 보고(ref-031). 보상 트랜잭션 패턴은 이미 완료된 단계의 효과를 되돌리는 별도 작업을 정의(ref-489). 20. 예외 복구·재계획·업무 연속성 페이지 9절 서술 기반.
- **f3**: CBV 2.0 온톨로지는 arriving·receiving·accepting 과 운송 수단 적재 기준의 loading·unloading 을 별도 업무 단계로 정의. 17. 로봇 간 협업·물리적 인계 페이지 10절의 [추정] 서술 재인용.
- **f4**: state.schema: loadId 설명 "Unique identification number of the load (e.g., barcode or RFID)"; 식별 전이면 비우고, 식별할 수 없는 로봇은 생략 가능.
- **f5**: EPCIS 1.2(2016-09-29)의 오류 선언으로 기존 이벤트를 정정. 회수 때 어떤 확인(스캔·무게·위치)을 요구할지는 미확인(oq-079). 20. 예외 복구·재계획·업무 연속성 페이지 5절 재인용.
- **f6**: DoorMode.msg 다섯 모드 값, task_state.json 의 상태 토큰(delayed·blocked·completed 등). 19. 모니터링·이상 탐지·원인 분석 페이지 5·10절 서술 기반.
- **f7**: state.schema errorLevel 열거값 WARNING, URGENT, CRITICAL, FATAL("No immediate attention required"~"User intervention is required"). connection.schema 의 CONNECTION_BROKEN. 판 간 해석 차이는 oq-073.
- **f8**: 각 스키마는 자기 필드만 정의하고 서로 간 대응표를 두지 않음. 19. 모니터링·이상 탐지·원인 분석 페이지 3절 [추정] 재인용.
- **f9**: DoorMode 값 closed·moving·open·offline·unknown(ref-313), 문 어댑터의 상태 감독 역할(ref-283). 19. 모니터링·이상 탐지·원인 분석 페이지 5절 [사실] 재인용.
- **f10**: mdBook 원본 integration_workcells.md: 로봇은 "will first move to the pickup_waypoint" 한 뒤 요청–결과 주기를 거쳐 하역 지점으로 이동. perform_deliveries 필요.
- **f11**: VDA 5050 원문: 범위 제외 "interfaces to peripheral equipment, infrastructure components, or external IT systems". SEMI E84 는 반도체 AMHS–로드포트 규격(원문 미열람).
- **f12**: 명세 원문: "it keeps all the order information and fulfills the order up to the last released node". 외부망 단절 시 운영 기준은 oq-038.
- **f13**: 명세 원문의 관제 기능 목록: "Detection and resolution of blockages ('deadlocks')", 통신 오류의 탐지·해소.
- **f14**: 20. 예외 복구·재계획·업무 연속성 페이지 9절 [추정] 재인용(RobotUpdateHandle.hpp 의 재계획·작업 수락 관련 인터페이스). 어댑터 재시작 시 작업 복원 여부는 oq-048.
- **f15**: rmf-core 원문: 스케줄은 "living database whose contents will change over time to reflect delays, cancellations, or route changes"; 협상 결과는 제3자 판정자가 고름.
- **f16**: 20. 예외 복구·재계획·업무 연속성 페이지 8절 [사실] 재인용. 두 논문 모두 원문 미열람, 속도 수치는 저자 보고값.
- **f17**: Sensors 2021, MRPF(선점 스케줄링+고장 복구). 20. 예외 복구·재계획·업무 연속성 페이지 5·8절 재인용.
- **f18**: Žulj 외 2022(배치 구성·순서), Löffler 외 2023(AMR·피커 조율). 18. 사람–로봇 협업·운영 인터페이스 페이지 3절 [사실] 재인용. 원문 미열람.
- **f19**: Korsah 외 2013 분류의 스케줄 간 의존(XD), Zang 외 2026-07 버퍼 제한 인계 스테이션 연구. 17. 로봇 간 협업·물리적 인계 페이지 5절 제약 칸 [추정] 재인용.
- **f20**: IISE Transactions 게재 'Deploying pickers and robots in cobot-based collaborative order picking systems'. 18. 사람–로봇 협업·운영 인터페이스 페이지 10·11절 기반. 원문 미열람.
- **f21**: WSC 2003 Proceedings 1192–1198쪽. 19. 모니터링·이상 탐지·원인 분석 페이지 3절 [사실] 재인용. 원문 미열람.
- **f22**: state.schema operatingMode 7개 값, safetyState 비상정지: 로봇에서 수동 확인(MANUAL)과 원격 확인(REMOTE) 구분.
- **f23**: rmf_demos README 의 비상 경보 데모. 18. 사람–로봇 협업·운영 인터페이스 페이지 9절 [사실] 재인용. 이번 실행에서 원문 재열람 안 함.
- **f24**: 17. 로봇 간 협업·물리적 인계 페이지 5·8절 [사실] 재인용. 시험 결과와 파지 허용 오차를 잇는 기준은 oq-063.
- **f25**: 17. 로봇 간 협업·물리적 인계 페이지 3절 [사실] 재인용(확인일 2026-09-25). 원문 미열람. (발행일 미확인, 확인일 기준)
- **f26**: 17. 로봇 간 협업·물리적 인계 페이지 4절 [사실] 재인용. 국내 대응 KS 여부는 oq-064. 원문 미열람.
- **f27**: 18. 사람–로봇 협업·운영 인터페이스 페이지 9절, 17. 로봇 간 협업·물리적 인계 페이지 9절의 [추정] 재인용. ISO 3691-4:2023(원문 미열람).
- **f28**: 두 기관 게시물 제목 기준(원문 미열람). 제정된 KS 의 번호·내용은 미확인(oq-070).
- **f29**: 18. 사람–로봇 협업·운영 인터페이스 페이지 10절(27. AI·학습·적응과 모델 운영 연결) 근거 논문. 모두 arXiv, 원문 미열람.
- **f30**: arXiv 2101.01625 'Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery'. 원문 미열람.
- **f31**: VDA 5050 errorLevel 4값, MassRobotics 운용 상태, Open-RMF 작업 상태 토큰이 서로 대응표 없이 정의됨.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-007 | NIST | Performance of Collaborative Robot Systems | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/performance-collaborative-robot-systems | 예 |
| ref-008 | NIST | ARIAC Documentation | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/ | 아니오 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | medium | 2026-09-25 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-202 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | 표준 | medium | 2026-09-25 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 예 |
| ref-203 | PEER Group | SEMI E84: Carrier Handoff | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.peergroup.com/definition-of-standard/semi-e84/ | 예 |
| ref-204 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | 표준 | medium | 2026-09-25 | https://www.astm.org/f3499-21.html | 예 |
| ref-209 | Zang, C. 외 | Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.17724 | 예 |
| ref-210 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 2023 | 표준 | medium | 2026-09-25 | https://webstore.ansi.org/standards/ria/ansia3r15082023 | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | 논문 | medium | 2026-09-25 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 예 |
| ref-451 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | 논문 | medium | 2026-09-25 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 예 |
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 2022 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 | 예 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 2023 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 | 예 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 2026-03 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 예 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 예 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2101.01625 | 예 |
| ref-483 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.18145 | 예 |
| ref-484 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 2021-09-30 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/1424-8220/21/19/6536 | 예 |
| ref-489 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 2026-04-16 | 벤더 문서 | medium | 2026-09-25 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction | 예 |
| ref-492 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 예 |
| ref-537 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 예 |

### 출처 요약

- **ref-004**: Open-RMF 핵심 구조. 교통 스케줄이 지연·취소·경로 변경을 반영하는 데이터베이스이며 충돌 시 플릿 관리자 간 협상을 한다고 설명.
- **ref-007**: 원문 미열람. 사람–로봇·로봇–로봇 협업 팀의 성능 평가 방법·지표 개발 프로젝트.
- **ref-008**: 원문 미열람. ARIAC 2025 시나리오·평가 문서(이동 전 키트 품질 확인 등). 이번 실행에서 재열람하지 않음.
- **ref-023**: 디스펜서·인제스터 워크셀과 배송 작업의 요청–결과 반복, 상태 토픽, perform_deliveries 설정을 설명.
- **ref-031**: VDA 5050 3.0.0 명세. 범위 제외(주변 설비·외부 IT), 관제의 교착·통신 오류 해소 기능, 연결 끊김 시 마지막 해제 노드까지 수행, cancelOrder 시 동작 FAILED 보고를 확인.
- **ref-044**: 원문 미열람. CBV 업무 단계 어휘(arriving·receiving·accepting·loading·unloading 등) 온톨로지. 이번 실행에서 재열람하지 않음.
- **ref-051**: VDA 5050 상태 메시지 스키마. errorLevel(WARNING·URGENT·CRITICAL·FATAL), operatingMode 7값, 비상정지 종류, 선택 필드 loads·loadId 를 정의.
- **ref-104**: 원문 미열람. Open-RMF 데모 환경과 비상 경보 시 로봇 주차 흐름. 이번 실행에서 재열람하지 않음.
- **ref-111**: 원문 미열람. Open-RMF 작업 상태 스키마(상태 토큰, 시각, 취소·중단 요청 기록). 이번 실행에서 재열람하지 않음.
- **ref-188**: 원문 미열람. 행동 의존 그래프로 창고 다중 로봇 계획을 지연에도 충돌 없이 실행하는 틀.
- **ref-202**: 원문 미열람. 반도체 AMHS–장비 로드포트 간 캐리어 인계 병렬 I/O 인터페이스 규격.
- **ref-203**: 원문 미열람. SEMI E84 단계별 인계 신호 구조 설명.
- **ref-204**: 원문 미열람. 무인 지상 이동로봇의 도킹 성능 확인 시험 방법.
- **ref-209**: 원문 미열람. 버퍼 제한 인계 스테이션을 둔 다중 하위 시스템 지속형 픽업·배송 연구.
- **ref-210**: 원문 미열람. 산업용 이동로봇 시스템·적용의 안전 요구(유형 C 모바일 매니퓰레이터 포함).
- **ref-230**: 원문 미열람. MassRobotics AMR 상호운용 표준 JSON 스키마(운용 상태 등). 이번 실행에서 재열람하지 않음.
- **ref-283**: 원문 미열람. 문 노드·문 어댑터(상태 감독자) 연동 설명. 이번 실행에서 재열람하지 않음.
- **ref-313**: 원문 미열람. 문 모드 다섯 값(closed·moving·open·offline·unknown) 정의. 이번 실행에서 재열람하지 않음.
- **ref-351**: 원문 미열람. LLM 계획기의 불확실성 정렬로 필요할 때 사람에게 도움을 요청하는 방법(KnowNo).
- **ref-353**: 원문 미열람. 로봇 에이전트가 사용자 명령을 분류하고 모호성을 해소하는 방법.
- **ref-394**: 원문 미열람. 스케줄 간 의존을 포함한 다중 로봇 작업 배정 분류 체계.
- **ref-417**: 원문 미열람. LLM 제어 로봇 시스템의 실행 전 안전 게이트와 작업 안전 계약.
- **ref-449**: 원문 미열람. 연결 상태(ONLINE·OFFLINE·CONNECTION_BROKEN) 스키마. 이번 실행에서 재열람하지 않음.
- **ref-451**: 원문 미열람. AGV 시스템 병목 탐지 방법 비교(이동 병목 탐지 대 가동률·대기 시간 방법).
- **ref-467**: 원문 미열람. AMR 보조 피커–부품 시스템의 배치 구성·배치 순서 결정.
- **ref-468**: 원문 미열람. AMR 과 사람 피커의 조율 문제와 작업 완료 시각 최소화.
- **ref-469**: 원문 미열람. 협동 피킹 시스템의 피커·로봇 투입 결정.
- **ref-470**: 원문 미열람. 무인 산업용 트럭과 그 시스템의 안전 요구·검증.
- **ref-473**: 원문 미열람. 고정식·이동식 산업용 로봇 협동작업 안전 가이드 배포 게시물.
- **ref-475**: 원문 미열람. 이동식 협동로봇 산업표준 제정 보도자료.
- **ref-476**: 원문 미열람. 로봇 실패 설명 생성으로 사용자의 고장 복구 지원을 개선하는 연구.
- **ref-483**: 원문 미열람. 지연된 로봇의 통과 순서를 실시간 재스케줄하는 알고리즘(SES).
- **ref-484**: 원문 미열람. 선점 스케줄링과 고장 복구를 결합한 다중 로봇 작업 배정.
- **ref-489**: 원문 미열람. 완료된 단계의 효과를 되돌리는 보상 트랜잭션 설계 패턴. 이번 실행에서 재열람하지 않음.
- **ref-492**: 원문 미열람. EPCIS 1.2 표준(오류 선언을 통한 이벤트 정정 포함).
- **ref-537**: 원문 미열람. 플릿 어댑터 로봇 갱신 핸들 헤더(재계획 요청·작업 수락 관련 인터페이스). 이번 실행에서 재열람하지 않음.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 실행: '다른 대분류와의 연결' 절만 patches 로 채움. A. 업무·공급망 설계: f1·f2(20↔1), f20(18↔3), f21(19↔4) / B. 공통 정보·환경 모델: f3(17↔7), f4·f5(20↔7), f6(19↔8, 8·22 구분 유지) / C. 연결·실행 기반: f7·f8(19·20↔9), f22(18↔9), f9(19↔10), f10·f11(17↔10), f23(18↔10), f12(20↔11), f13·f14(20↔12) / D. 계획·최적화: f15·f16(20↔15), f17(20↔13), f18(18↔13·14), f19(17↔14·16) / F. 도입·검증·유지관리: f24·f25(17↔23) / G. 안전·보안·지능·거버넌스: f26·f27·f28(17·18↔25), f29·f30(18·19↔27, 분류 원문 8장 교차 규칙), f31(19↔28). 아직 다루지 않은 연결: 20↔22(oq-081, 22 페이지 seed), 21·24·26 과의 연결, 5·6 과의 연결. 추정 태그 finding 은 추정 그대로, 관련 열린 질문 id 병기. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 35 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(연결 서술은 게시된 세부영역 페이지의 단일 출처 주장 재인용 중심)
    - 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거 미확보(oq-081)
    - f28: 2024-11 제정 KS 의 번호·내용 미확인(oq-070)
    - ref-007·ref-008·ref-104 등 재사용 출처 원문 이번 실행에서 재열람 안 함
- 범위 경계 위반 의심:
    - f11: SEMI E84 는 업종별 인계 규격(분류 원문 9장 업종별 조건)이므로 참고 사례로만 서술
    - f26·f27·f28: 설비 안전 기능·안전 표준 이행은 로봇 제조사·현장 통합사 몫(연계 대상), ROP 는 상태 표시·승인 흐름만 맡는 것으로 서술
    - f23: 시설 비상정지·설비 안전 제어는 연계 대상, ROP 는 경보 상태 반영만
- 한계: 대분류 연결 실행으로 근거를 게시된 17. 로봇 간 협업·물리적 인계, 18. 사람–로봇 협업·운영 인터페이스, 19. 모니터링·이상 탐지·원인 분석, 20. 예외 복구·재계획·업무 연속성 페이지의 검증된 주장과 각주(기존 참고문헌 재사용)에서 찾았고, 새 출처는 필요하지 않아 WebSearch 0회·신규 출처 0건이다(한국어·영어 신규 검색 없음; 국내 자료는 ref-473·ref-475 재사용). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 다시 연 출처: ref-004(rmf-core), ref-023(workcells), ref-031(VDA 5050 3.0.0 명세), ref-051(state.schema). 나머지 재사용 출처는 원문 미열람 표시, 신뢰도 상한 medium. ref-031 원문 요약 도구는 본문에서 WARNING·CRITICAL 만 언급했으나 state.schema(ref-051) 원문의 errorLevel 열거값이 WARNING·URGENT·CRITICAL·FATAL 이므로 f7 은 ref-051 기준으로 적음. 22. 시뮬레이션·예측용 디지털 트윈·23·24·25·26·27·28 페이지는 seed 상태라 상대편 서술도 E. 협업·현장 운영 쪽 근거에 기댐. 27. AI·학습·적응과 모델 운영 연결(f29·f30)은 교차 규칙에 따라 18·19 적용 대상과 함께 제안. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f6 에서 구분. 새 열린 질문 없음(관련 질문은 기존 oq-001·006·009·018·021·033·038·042·048·062~064·070·073·079·081 로 이미 등록됨). 정정 요청 없음.
