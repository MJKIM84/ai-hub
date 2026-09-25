# 리서치 브리프 2026-09-25-49

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-49 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- D. 계획·최적화 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음)
- E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석과 D. 계획·최적화 세부영역을 잇는 근거가 게시 페이지에 없음
- G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보와 D. 계획·최적화를 잇는 근거 없음
- C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조, B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적과의 직접 연결 근거 약함
- F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크 연결은 MAPF 벤치마크 정의뿐이고 현장 처리량과의 관계는 열린 질문(oq-058)

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. D. 계획·최적화의 네 세부영역(13. 작업 배정 — MRTA ~ 16. 공용 자원·충전·에너지 최적화)은 A. 업무·공급망 설계에서 어떤 입력(주문·시작 시각·우선순위·물동량)을 받고 어떤 성과를 되돌리는가?
3. B. 공통 정보·환경 모델의 능력 선언·경로망·배터리 상태가 D. 계획·최적화의 배정·교통·충전 계획에 어떤 입력으로 들어가는가?
4. C. 연결·실행 기반의 인터페이스(Open-RMF 디스패처·제어 수준·승강기 세션, VDA 5050 관제 기능·기반 경로)는 D. 계획·최적화의 결정을 어디까지 집행하고 어디서 제한하는가?
5. E. 협업·현장 운영과 F. 도입·검증·유지관리의 어느 세부영역(사람 협업, 예외 복구, 시뮬레이션, 시험, 수명주기)이 D. 계획·최적화의 결정과 맞물리는가?
6. G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스와 D. 계획·최적화를 잇는 검증된 근거는 무엇이고, 26. 사이버보안·접근권한·개인정보와의 근거는 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: VDA 5050 3.0.0 은 이동로봇에 대한 주문 배정을 관제(fleet control)의 기능으로 두면서, 외부 IT 시스템과의 인터페이스는 명세 범위에서 제외한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 로봇 인터페이스 표준이 상위 시스템 연동을 범위 밖에 두므로, 배정의 입력인 주문·납기·출하 마감 제약은 WMS 등 상위 업무 시스템에서 받아 ROP 가 배정 기준으로 옮겨야 할 것으로 보인다(결합 방법은 oq-054). | ref-031, ref-125 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f3 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: Open-RMF 작업 요청 스키마(task_request.json)는 시각·순서 관련 필드로 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후 필드는 두지 않는다. | ref-125 | 아니오 | medium | 2026-09-25 | 출하 / 시작 조건 | 원문 미열람 |
| f4 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 웨이브·웨이브리스 출고 지시 정책 연구(2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. | ref-134, ref-133 | 아니오 | low | 2025 | 피킹 / 시작 조건 | 원문 미열람 |
| f5 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 랙 이동 로봇 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는 저자 계산 실험에서 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. | ref-381 | 아니오 | medium | 2017 | 피킹 / 수행 자원 | 원문 미열람 |
| f6 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: 풋월 주문 통합 연구는 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다고 보아, 포장 작업자 대기가 순서 결정의 성과 지표로 이어진다(지표 정의는 oq-051). | ref-385 | 아니오 | medium | 2019 | 포장 / 예외·성과 | 원문 미열람 |
| f7 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 2. 공정·워크플로 모델링: B2MML 공통 스키마의 Dependency1Type 은 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등)을 표현하며, 창고 물류 작업에 적용한 사례는 확인되지 않았다(oq-013). | ref-117 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f8 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 충전기 대수 결정과 창고 충전소 배치 최적화 연구가 있어, 충전 정책 결정이 충전기 수·위치 같은 설비 계획으로 이어지는 것으로 보인다. | ref-533, ref-109 | 아니오 | low | 2024 | 수행 자원 | 원문 미열람 |
| f9 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: Omega(2024) 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했으며, 이는 모델·시뮬레이션 조건의 저자 보고값이다. | ref-146 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f10 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026). | ref-236, ref-237 | 아니오 | medium | 2026-08 | 수행 자원 | 원문 미열람 |
| f11 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: VDA 5050 팩트시트는 임계 저충전 수준(criticalLowChargingLevel)을 선언하게 하고 그 이하에서는 관제가 충전소로 가는 주문만 보내야 하며, Open-RMF 템플릿은 운영 설정 recharge_threshold(예시값 0.10)와 충전 목표 recharge_soc(예시값 1.0)를 둔다. | ref-228, ref-105 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f12 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: Open-RMF traffic-editor 는 플릿별 경유점·차선(양방향·단방향) 그래프와 주차·충전·대기 지점 속성, 문·승강기·층을 주석하게 하고, 이 그래프를 building_map_generator 로 주행 그래프로 내보내 플릿 어댑터의 경로 계획에 쓰게 한다. | ref-079 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f13 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: 충전 시점 계획은 로봇이 보고하는 현재 배터리 상태(충전 상태·충전 중 여부)를 입력으로 쓰며, 이 현재 상태 표현은 8. 실시간 세계 상태·데이터 일관성 쪽에 속하는 것으로 보인다. | ref-051, ref-104 | 아니오 | low | 2026-09-25 | 시작 조건 | — |
| f14 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 디스패처는 작업 요청을 받으면 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리 가능한 플릿이 비용을 담은 입찰(BidProposal)을 내면 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. | ref-376 | 아니오 | medium | 2026-09-25 | 피킹 / 수행 자원 | — |
| f15 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 는 플릿 연동을 전체 제어·신호등(일시정지·재개)·읽기 전용으로 나누고 공유 공간마다 읽기 전용 플릿을 하나만 허용하며, 중앙 교통 스케줄에서 충돌이 나면 플릿들이 제안을 내고 시스템 통합사가 배치한 제3자 판정자가 조합을 고른다. | ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f16 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 명세에서 제외하면서도, 교착 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 관제 기능으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f17 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 승강기 요청은 세션 id 로 승강기를 점유하고 세션 종료 요청(REQUEST_END_SESSION)을 보낼 때까지 제어권이 그 세션에 남으며, AGV 모드에서는 정지 시 문이 열린 채 유지된다. | ref-312, ref-286 | 아니오 | medium | 2026-09-25 | 출하 / 제약 | — |
| f18 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다는 것을 관제의 에너지 관리 기능으로 두고, 과충전 보호는 이동로봇의 책임으로 명시한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f19 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f20 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 작업자가 피킹하고 자율이동로봇이 운반하는 동적 주문 피킹 연구(2025)가 있어, 로봇 배정이 사람 작업자의 배치와 맞물린다. | ref-132 | 아니오 | medium | 2025 | 피킹 / 수행 자원 | 원문 미열람 |
| f21 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구(2025)가 있다. | ref-388 | 아니오 | medium | 2025 | 포장 / 수행 자원 | 원문 미열람 |
| f22 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계: Open-RMF 배정이 플릿 단위 입찰로 이루어지고 요청 스키마에 작업 간 선후 필드가 없으므로, 피킹 로봇 완료 뒤 운반 로봇 출발 같은 제조사 간 인계 선후는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다(oq-049). | ref-376, ref-125 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f23 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 창고 MAPF 실행 연구(2019)는 지연이 쌓일 때 행동 의존 그래프로 순서를 지키며 실행을 이어가는 방법을 다루어, 계획 유지와 재계획의 판단이 두 영역을 잇는다. | ref-188 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f24 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있고, Open-RMF 데모는 비상 경보가 켜지면 로봇을 가장 가까운 주차 위치로 보낸다. | ref-286, ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f25 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: VDA 5050 3.0.0 은 진입 금지(BLOCKED)·속도 제한(SPEED_LIMIT)·해제(RELEASE) 등 구역 유형을 교통 관리 수단으로 정의하면서, 이 문서가 기능·운영·시스템 안전을 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f26 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 로봇 이동형 풀필먼트 시스템과 국내 자동물류센터의 이산 사건 시뮬레이션 연구가 배정 규칙을 가정한 미래에서 실험하는 도구로 쓰였고, 한 연구에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398, ref-402 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f27 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구가 있어, 경로망 설계 평가는 가정한 미래를 실험하는 쪽에 속하는 것으로 보인다. | ref-267 | 아니오 | low | 2024 | — | 원문 미열람 |
| f28 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전: 현장 도입 때 플릿별 경로망과 차선 속성, 주차·충전 경유점을 traffic-editor 로 주석해 설정하는 일이 온보딩 작업이 될 것으로 보인다. | ref-079 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: MAPF 연구는 정의·변형·벤치마크를 정리한 공통 틀을 가지고 있으나, 격자·단위 시간 가정의 벤치마크 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). | ref-186 | 아니오 | medium | 2019-06 | — | 원문 미열람 |
| f30 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 일정을 정하는 연구(2026-03)가 있어, 충전·배정 계획이 배터리 열화 관리와 이어진다. | ref-403 | 아니오 | medium | 2026-03 | 제약 | 원문 미열람 |
| f31 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 학습 기반 배차(이종 그래프 어텐션 스케줄러)와 LLM 기반 다중 로봇 작업 배정 연구가 있어, 분류 원문 8장의 '학습 기반 배차' 교차 규칙에 따라 두 영역이 이어진다. | ref-399, ref-090, ref-168 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f32 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있어, 학습 기반 경로 계획이 두 영역을 잇는다. | ref-199 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f33 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 자율 피킹 로봇의 충전소 선택·충전 시간 결정에 심층 강화학습을 쓰는 연구(2026-07)가 있어, 학습 기반 충전 결정이 두 영역을 잇는 것으로 보인다. | ref-531 | 아니오 | low | 2026-07 | — | 원문 미열람 |
| f34 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스: VDA 5050 은 구역·경로 해제로 교통 규칙을 정하되 조율 전략은 빼고, Open-RMF 는 여러 플릿의 교통 스케줄·협상을 구현하므로, 한 현장에서 둘을 함께 쓸 때 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-057). | ref-031, ref-004 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 관제 기능 목록에 'Assignment of orders to the mobile robots'가 있고, 범위 제외 대상으로 주변 설비·인프라·외부 IT 시스템 인터페이스를 든다(3.0.0, main 브랜치 원문).
- **f2**: f1 의 범위 제외와, Open-RMF 작업 요청 스키마에 마감 필드가 없다는 점(f3)에서 도출. 게시된 13. 작업 배정 — MRTA 9절 표와 같은 방향.
- **f3**: 게시된 14. 작업 순서·스케줄링 5절 시작 조건 칸의 [사실] 주장. 이번 실행에서 원문 재열람 안 함. (재인용: 2026-09-25-34)
- **f4**: A. 업무·공급망 설계 페이지 연결 절의 [추정] 주장과 같은 각주. 원문 미열람.
- **f5**: 게시된 14. 작업 순서·스케줄링 3절·10절의 [사실] 주장(저자 계산 실험, 독립 재현 미확인). (재인용: 2026-09-25-34)
- **f6**: 게시된 14. 작업 순서·스케줄링 5절 예외·성과 칸과 10절의 [사실] 주장. (재인용: 2026-09-25-34)
- **f7**: 게시된 14. 작업 순서·스케줄링 7절 표와 10절의 [사실] 주장. 이번 실행 원문 재열람 안 함. (재인용: 2026-09-25-34)
- **f8**: 게시된 16. 공용 자원·충전·에너지 최적화 10절의 [추정] 연결(Chen 외 2024, Stark 외 2024). 원문 미열람.
- **f9**: A. 업무·공급망 설계 페이지 연결 절의 [사실] 주장(현장 실측 아님). (재인용: 2026-09-25-29)
- **f10**: 게시된 13. 작업 배정 — MRTA 10절과 B. 공통 정보·환경 모델 연결 절의 [사실] 주장. 선언 능력과 관측 능력 중 기준 문제는 oq-024. 원문 미열람.
- **f11**: config.yaml 원문: recharge_threshold 0.10, recharge_soc 1.0, 로봇별 charger, finishing_request park. 팩트시트 부분은 게시된 16절 5절 제약 칸 [사실] 재인용. 두 값 중 기준은 oq-068.
- **f12**: 원문: 'The annotated Graphs are eventually exported as navigation graphs using the building_map_generator' — 플릿 어댑터 경로 계획에 쓰인다.
- **f13**: rmf_demos 원문: 'ChargeBattery tasks are optimally injected into a robot's schedule when the robot has insufficient charge'. VDA 5050 상태 스키마의 배터리 상태는 게시된 16절 10절 [추정] 재인용.
- **f14**: 원문: 평가 방법으로 'fastest to finish, lowest cost, etc which can be configured'. 플릿 안에서 로봇을 고르는 일은 플릿 어댑터 쪽(두 수준 배정의 최적성 손실은 oq-053).
- **f15**: 원문: 'any shared space is allowed to have a maximum of just one "Read Only" fleet in operation.' 제어 수준별 교통 성능 차이는 oq-032.
- **f16**: 원문 요지: 교통 조율 전략(routing, prioritization, congestion handling, deadlock resolution)은 포함하지 않으며, 관제 기능에 'Detection and resolution of blockages ("deadlocks")'가 있다.
- **f17**: LiftState 원문: session_id 는 'has been granted control of the lift until it sends a request with a request_type of REQUEST_END_SESSION'. 여러 제조사 호출의 배분 규칙은 oq-067.
- **f18**: 원문: 'Charging orders can interrupt transfer orders' / 'Protection against overcharging is the responsibility of the mobile robot.'
- **f19**: 원문: 'the base cannot be changed. The fleet control shall therefore assume that the base has already been executed'. 재정렬 범위는 C. 연결·실행 기반 페이지의 [추정]과 같은 해석.
- **f20**: 게시된 13. 작업 배정 — MRTA 5절 수행 자원 칸의 [사실] 주장. 18번 페이지는 아직 seed. (재인용: 2026-09-25-33)
- **f21**: 게시된 14. 작업 순서·스케줄링 5절·10절의 [사실] 주장(결과 수치 미확인). (재인용: 2026-09-25-34)
- **f22**: 게시된 14. 작업 순서·스케줄링 5절 완료·인계 칸·9절의 [추정] 주장과 같다. 공개 구현은 찾지 못함.
- **f23**: 게시된 15. 다중 로봇 경로·교통 관리 — MAPF 5절 예외·성과 칸의 [사실] 주장. 20번 페이지는 seed. (재인용: 2026-09-25-39)
- **f24**: LiftState 원문: MODE_HUMAN, MODE_AGV, MODE_FIRE, MODE_OFFLINE, MODE_EMERGENCY. rmf_demos README: 경보 시 로봇을 가장 가까운 주차 위치로 보냄. 설비 안전 제어는 분류 원문 9장 연계 대상.
- **f25**: 원문: 'This document does not define functional, operational, or system safety'. 구역 유형 10종(BLOCKED, LINE_GUIDED, RELEASE, COORDINATED_REPLANNING, SPEED_LIMIT, ACTION, PRIORITY, PENALTY, DIRECTED, BIDIRECTED).
- **f26**: 게시된 13. 작업 배정 — MRTA 3절·10절의 [사실] 주장. 22번 페이지는 seed. (재인용: 2026-09-25-33)
- **f27**: 게시된 15. 다중 로봇 경로·교통 관리 — MAPF 10절의 [추정] 연결. 현재 상태 표현(8. 실시간 세계 상태·데이터 일관성)과 구분. 원문 미열람.
- **f28**: traffic-editor 원문의 주석 대상(차선·경유점·주차·충전·문·승강기·층)에서 도출. 게시된 15번 10절의 [추정]과 같다. 온보딩 소요 측정 자료 없음.
- **f29**: Stern 외(2019) 'Definitions, Variants, and Benchmarks'. 게시된 15번 3절 [사실] 주장과 11절 열린 질문. 원문 미열람.
- **f30**: 제목 'Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots'. 게시된 13번 10절에 [사실]로 인용됨. 원문 미열람.
- **f31**: 게시된 13번 10절의 [사실] 주장. LLM 배정 결과 수치에는 출처 충돌(oq-030)이 있어 수치는 싣지 않음. 원문 미열람.
- **f32**: 게시된 15번 10절의 [사실] 주장('Scalable Imitation Learning for Lifelong Multi-Agent Path Finding'). 원문 미열람.
- **f33**: 게시된 16번 10절의 [추정] 연결. 원문 미열람.
- **f34**: f15·f16·f25 에서 도출. 제3자 판정자를 시스템 통합사가 배치한다는 Open-RMF 설명이 판정 주체 문제를 드러낸다. 공개 설계 미확인.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 예 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 예 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2192437620300315 | 예 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.17003 | 예 |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | 논문 | medium | 2026-09-25 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 예 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 2025 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 | 예 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | 논문 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 예 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21415 | 예 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.05683 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 관제 기능(주문 배정, 교착 탐지·해소, 교통 제어, 에너지 관리), 범위 제외, 기반·호라이즌, 구역 유형, 안전 비규정 문구 확인.
- **ref-004**: 플릿 제어 수준(전체 제어·신호등·읽기 전용), 중앙 교통 스케줄과 제3자 판정자 협상 설명.
- **ref-376**: 디스패처의 입찰 공고·입찰·배정 요청 흐름과 설정 가능한 평가 기준 설명.
- **ref-079**: 경유점·차선 그래프, 주차·충전·대기 지점, 문·승강기·층 주석과 주행 그래프 내보내기 설명.
- **ref-105**: 플릿 어댑터 템플릿 설정: recharge_threshold 0.10, recharge_soc 1.0, 로봇별 충전기, finishing_request, task_capabilities.
- **ref-312**: 승강기 요청 유형(세션 종료·AGV 모드·사람 모드), session_id, 목적층 필드 정의.
- **ref-286**: 승강기 상태: 운영 모드(사람·AGV·화재·오프라인·비상), 세션 점유, lift_time, 층 이름 필드.
- **ref-104**: 충전 작업 자동 삽입, 비상 경보 시 주차 위치 이동, 호텔 다층 다플릿 데모 설명.
- **ref-125**: 원문 미열람. Open-RMF 작업 요청 스키마(가장 이른 시작 시각·우선순위, 마감·선후 필드 없음).
- **ref-134**: 원문 미열람. 자동 분류기 창고의 웨이브·웨이브리스 출고 지시 정책 연구.
- **ref-133**: 원문 미열람. 동적으로 도착하는 주문의 피킹 재최적화 연구.
- **ref-381**: 원문 미열람. 랙 이동 로봇 작업대의 주문·랙 순서 결정과 필요 로봇 대수.
- **ref-385**: 원문 미열람. 풋월 주문 통합의 빈 순서 문제와 포장 작업자 대기.
- **ref-117**: 원문 미열람(이번 실행 재열람 안 함). B2MML 공통 스키마의 실행 의존 유형(Dependency1Type).
- **ref-109**: 원문 미열람. 창고 충전소 배치 최적화.
- **ref-533**: 원문 미열람. 자가 등반 로봇 창고의 배터리 관리 정책과 충전기 수.
- **ref-146**: 원문 미열람. RMFS 에너지 소비와 동적 우선순위 운영 정책.
- **ref-236**: 원문 미열람. 온톨로지 기반 실행 가능성 판정을 배정 입력으로 쓰는 연구.
- **ref-237**: 원문 미열람. 이종 자원의 온톨로지 기반 작업 배정.
- **ref-228**: 원문 미열람(이번 실행 재열람 안 함). VDA 5050 팩트시트 스키마(충전 설정·임계 저충전 수준 등).
- **ref-051**: 원문 미열람(이번 실행 재열람 안 함). VDA 5050 상태 스키마(배터리 상태 등).
- **ref-132**: 원문 미열람. 작업자 피킹·AMR 운반 협업의 동적 주문 피킹.
- **ref-388**: 원문 미열람. 국내 물류센터 피킹-포장 작업자 스케줄링 연구.
- **ref-188**: 원문 미열람. 행동 의존 그래프로 창고 MAPF 계획을 강건하게 실행.
- **ref-398**: 원문 미열람. RMFS 결정 규칙의 이산 사건 시뮬레이션 평가.
- **ref-402**: 원문 미열람. 국내 자동물류센터 시뮬레이션 설계 최적화.
- **ref-267**: 원문 미열람. 시뮬레이션 기반 다중 AGV 경로망 자동 설계.
- **ref-186**: 원문 미열람. MAPF 정의·변형·벤치마크 정리.
- **ref-403**: 원문 미열람. 배터리 건강을 고려한 플릿 수준 AMR 일정 계획.
- **ref-399**: 원문 미열람. 이종 그래프 어텐션 기반 학습형 다중 로봇 스케줄링.
- **ref-090**: 원문 미열람. LLM 기반 다중 로봇 작업 계획·배정.
- **ref-168**: 원문 미열람. 건설 로봇 LLM 배정과 전통 최적화 비교(결과 수치 출처 충돌 oq-030).
- **ref-199**: 원문 미열람. 모방 학습 기반 지속형 MAPF.
- **ref-531**: 원문 미열람. 자율 피킹 로봇의 심층 강화학습 기반 배터리·충전 관리.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 절 신규 작성: A. 업무·공급망 설계(f1~f9), B. 공통 정보·환경 모델(f10~f13), C. 연결·실행 기반(f14~f19), E. 협업·현장 운영(f20~f23), F. 도입·검증·유지관리(f26~f30), G. 안전·보안·지능·거버넌스(f24·f25·f31~f34). 27. AI·학습·적응과 모델 운영 연결(f31~f33)은 분류 원문 8장 '학습 기반 배차' 교차 규칙에 따라 표기. 22. 시뮬레이션·예측용 디지털 트윈 연결(f26·f27)은 가정한 미래 실험으로, 8. 실시간 세계 상태·데이터 일관성 연결(f13)은 현재 상태 표현으로 구분. '아직 다루지 않은 연결'에 19. 모니터링·이상 탐지·원인 분석, 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적 명시. 새 각주 정의는 참고 자료 절에 추가(기존 ref-005·ref-006 유지). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 플릿 제어 수준 | Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read-Only) | Open-RMF 가 제조사 플릿과 연동하는 정도를 경로 지시까지 하는 전체 제어, 일시정지·재개만 하는 신호등, 상태만 받는 읽기 전용으로 나눈 구분이다. |
| 기반·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 로봇이 주행하도록 해제된 경로 구간(기반, 변경 불가)과 아직 해제되지 않아 주문 갱신으로 바꿀 수 있는 예정 구간(호라이즌)을 가리킨다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 의 우선(PRIORITY)·벌점(PENALTY) 구역 가중치를 출하 마감 같은 업무 우선순위와 연결해 ROP 가 설정하는 공개 설계나 사례가 있는가? | 관련 영역: 15. 다중 로봇 경로·교통 관리 — MAPF, 1. 주문·업무 시스템 연계 | 근거: f25 | 종류: 일반
- 제조사가 다른 이동로봇이 배터리 건강(열화) 상태를 관제에 보고하는 표준 필드가 있어, 충전·배정 계획이 이를 공통으로 쓸 수 있는가? | 관련 영역: 16. 공용 자원·충전·에너지 최적화, 24. 자산·소프트웨어 수명주기 관리 | 근거: f30 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 33 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - f11 팩트시트 criticalLowChargingLevel 규칙은 이번 실행에서 factsheet.schema 를 다시 열지 않고 게시 페이지 주장을 재인용
    - f3 task_request.json 필드 구성은 원문 재열람 안 함(게시 페이지 재인용)
    - f26~f33 논문 근거는 모두 원문 미열람, 게시 페이지 주장 재인용
    - 19. 모니터링·이상 탐지·원인 분석, 26. 사이버보안·접근권한·개인정보와 D. 계획·최적화를 잇는 근거 미확보
- 범위 경계 위반 의심:
    - f18: 과충전 보호는 분류 원문 9장 '로봇 자체 지능·제어' 경계의 연계 대상이며 ROP 는 충전 시작·중지 요청과 상태 확인만 맡는다고 구분
    - f24·f17: 승강기 운행·설비 안전 제어는 '시설·설비 제어' 경계의 연계 대상, ROP 는 세션 요청·모드 확인만
    - f2·f3: 납기·출하 마감 결정은 상위 업무 시스템 쪽 연계 대상
- 한계: web_fetch_available: false · fetch_mode mirror_only. 대분류 연결 실행(R-3)이므로 근거를 게시된 13. 작업 배정 — MRTA ~ 16. 공용 자원·충전·에너지 최적화 페이지와 A·B·C 대분류 페이지의 검증된 주장·각주에서 찾았고, 신규 검색·신규 출처 없이 기존 참고문헌만 재사용했다(검색 0/30, 신규 출처 0/15). raw.githubusercontent.com 으로 원문을 연 재사용 출처: ref-031(VDA 5050 명세, 두 번 열람), ref-004, ref-376, ref-079, ref-105, ref-312, ref-286, ref-104. 나머지 재사용 출처는 원문 미열람(신뢰도 상한 medium). 모든 finding 은 단일 출처이거나 같은 발행 주체라 교차 확인 0건, 신뢰도 medium 이하. E. 협업·현장 운영의 18·19·20, F. 도입·검증·유지관리, G. 안전·보안·지능·거버넌스 세부영역은 대부분 seed 라 연결 서술이 D. 계획·최적화 쪽 근거에 기댄다. 26. 사이버보안·접근권한·개인정보, 19. 모니터링·이상 탐지·원인 분석, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적과의 연결은 검증된 근거가 없어 finding 을 내지 않았다(스토리텔러가 '아직 다루지 않은 연결'로 표기). 실행 2026-09-25-46 의 18. 사람–로봇 협업 관련 자료(ISO 3691-4 등)는 아직 게시 전이라 쓰지 않았다. 정정 요청 없음.
