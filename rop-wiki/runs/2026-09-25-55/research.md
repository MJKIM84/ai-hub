# 리서치 브리프 2026-09-25-55

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-55 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | D. 계획·최적화 |

## 갭(비어 있거나 약한 섹션)

- D. 계획·최적화 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음). 같은 대상의 이전 실행 2026-09-25-49 브리프가 있으나 게시되지 않았다
- E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석과 D. 계획·최적화를 잇는 근거가 게시 페이지에 없음
- G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보와 D. 계획·최적화를 잇는 근거 없음
- C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조와의 직접 연결 근거 약함
- B. 공통 정보·환경 모델의 7. 화물·재고·자산 식별과 추적과 D. 계획·최적화를 잇는 근거 없음
- 이전 브리프 2026-09-25-49 의 VDA 5050·Open-RMF 근거 가운데 일부(ref-125, ref-228)는 원문 미열람 상태였음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. D. 계획·최적화의 네 세부영역(13. 작업 배정 — MRTA ~ 16. 공용 자원·충전·에너지 최적화)은 A. 업무·공급망 설계에서 어떤 입력(주문·시작 시각·우선순위·물동량)을 받고 어떤 성과를 되돌리는가?
3. B. 공통 정보·환경 모델의 능력 선언·경로망·배터리 상태는 D. 계획·최적화의 배정·교통·충전 계획에 어떤 입력으로 들어가는가?
4. C. 연결·실행 기반의 인터페이스(Open-RMF 디스패처·제어 수준·승강기 세션·작업 요청 스키마, VDA 5050 관제 기능·기반 경로)는 D. 계획·최적화의 결정을 어디까지 집행하고 어디서 제한하며, 통신 저하(11. 분산 시스템·통신·컴퓨팅 구조)는 배정 방식에 어떤 영향을 주는가?
5. E. 협업·현장 운영과 F. 도입·검증·유지관리의 어느 세부영역(사람 협업, 인계, 모니터링, 예외 복구, 시뮬레이션, 시험, 수명주기)이 D. 계획·최적화의 결정과 맞물리는가?
6. G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스와 D. 계획·최적화를 잇는 근거는 무엇인가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: VDA 5050 명세는 이동로봇에 대한 주문 배정을 관제(fleet control)의 기능으로 두면서, 주변 설비·인프라·외부 IT 시스템과의 인터페이스는 명세 범위에서 제외한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 로봇 인터페이스 표준이 상위 시스템 연동을 범위 밖에 두고 Open-RMF 작업 요청에도 마감 필드가 없으므로, 배정의 입력인 주문·납기·출하 마감 제약은 WMS 등 상위 업무 시스템에서 받아 ROP 가 배정 기준으로 옮겨야 할 것으로 보인다(결합 방법은 oq-054). | ref-031, ref-125 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f3 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: Open-RMF 작업 요청 스키마(task_request.json)는 시각·순서 관련 필드로 가장 이른 시작 시각(unix_millis_earliest_start_time)과 우선순위(priority)를 두고, 마감 시각이나 다른 작업과의 선후를 지정하는 필드는 두지 않는다. | ref-125 | 아니오 | medium | 2026-09-25 | 출하 / 시작 조건 | — |
| f4 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 웨이브·웨이브리스 출고 지시 정책 연구(2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. | ref-134, ref-133 | 아니오 | low | 2025 | 피킹 / 시작 조건 | 원문 미열람 |
| f5 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 랙 이동 로봇 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는 저자 계산 실험에서 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. | ref-381 | 아니오 | medium | 2017 | 피킹 / 수행 자원 | 원문 미열람 |
| f6 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: 풋월 주문 통합 연구는 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다고 보아, 포장 작업자 대기가 순서 결정의 성과 지표로 이어진다(지표 정의는 oq-051). | ref-385 | 아니오 | medium | 2019 | 포장 / 예외·성과 | 원문 미열람 |
| f7 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ A. 업무·공급망 설계의 2. 공정·워크플로 모델링: B2MML 공통 스키마의 Dependency1Type 은 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등)을 표현하며, 창고 물류 작업에 적용한 사례는 확인되지 않았다(oq-013). | ref-117 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f8 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획: 충전 정책 연구(2024)와 창고 충전소 배치 최적화 연구(2024)가 있어, 충전 정책 결정이 충전기 수·위치 같은 설비 계획으로 이어지는 것으로 보인다. | ref-533, ref-109 | 아니오 | low | 2024 | 수행 자원 | 원문 미열람 |
| f9 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선: Omega(2024) 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했으며, 이는 모델·시뮬레이션 조건의 저자 보고값이다. | ref-146 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f10 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026-08). | ref-236, ref-237 | 아니오 | medium | 2026-08 | 수행 자원 | 원문 미열람 |
| f11 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: VDA 5050 팩트시트는 임계 저충전 수준(criticalLowChargingLevel)과 최소·최대 희망 충전 수준·최소 충전 시간을 로봇 선언으로 두고, Open-RMF 플릿 어댑터 템플릿은 운영 설정 recharge_threshold(예시값 0.10)와 충전 목표 recharge_soc(예시값 1.0)를 둔다. | ref-228, ref-105 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f12 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: Open-RMF traffic-editor 는 차선의 양방향 여부와 대기 지점(holding point)·충전소·주차 지점 같은 경유점 속성, 문·승강기를 주석하게 하고, 이 그래프를 building_map_generator 로 주행 그래프로 내보내 플릿 어댑터의 경로 계획에 쓰게 한다. | ref-079 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f13 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: Open-RMF 는 로봇이 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 시점 계획은 로봇이 보고하는 현재 배터리 상태를 입력으로 쓰며 이 현재 상태 표현은 8. 실시간 세계 상태·데이터 일관성 쪽에 속하는 것으로 보인다. | ref-104, ref-051 | 아니오 | low | 2026-09-25 | 시작 조건 | — |
| f14 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 디스패처는 작업 요청을 받으면 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리 가능한 플릿이 비용을 담은 입찰(BidProposal)을 내면 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. | ref-376 | 아니오 | medium | 2026-09-25 | 피킹 / 수행 자원 | — |
| f15 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 작업 요청 스키마의 fleet_name 필드는 작업을 수행할 수 있는 플릿 이름(하나 또는 목록)을 지정해, 요청 단계에서 배정 후보 플릿을 제한할 수 있게 한다. | ref-125 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f16 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: Open-RMF 는 플릿 연동을 전체 제어·신호등(일시정지·재개)·읽기 전용으로 나누고 공유 공간마다 읽기 전용 플릿을 최대 하나만 허용하며, 충돌이 나면 플릿들이 선호 경로와 상대를 수용하는 경로를 내고 시스템 통합사가 배치한 제3자 판정자가 조합을 고른다. | ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f17 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 명세에서 제외하면서도, 막힘 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 관제 기능으로 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f18 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 승강기 요청은 요청자 사이에서 유일한 세션 id 로 승강기를 점유하고 세션 종료 요청(REQUEST_END_SESSION)을 보낼 때까지 제어권이 그 세션에 남으며, AGV 모드에서는 승강기가 정지해 있는 동안 문이 열린 채 유지된다. | ref-312, ref-286 | 아니오 | medium | 2026-09-25 | 출하 / 제약 | — |
| f19 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다는 것을 관제의 에너지 관리 기능으로 두고, 과충전 보호는 이동로봇의 책임으로 명시한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f20 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f21 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조: Lott·Honary(arXiv 2609.13711, 2026-09)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 등 통신 저하 조건에서 비교해, 통신이 나빠지면 일부 배정기(ACBBA·PI·DGA)가 안정성이나 실행 가능성을 잃었다고 보고했다. | ref-539 | 아니오 | medium | 2026-09 | 제약 | 원문 미열람 |
| f22 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ C. 연결·실행 기반의 11. 분산 시스템·통신·컴퓨팅 구조: 통신 조건에 따라 분산 배정기의 안정성이 달라진다는 보고와 클라우드에 연결된 로봇·로봇그룹의 작업 계획을 다룬 국내 과제 보고서가 있어, 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 영역을 잇는 설계 쟁점이 될 것으로 보인다. | ref-539, ref-401 | 아니오 | low | 2026-09 | — | 원문 미열람 |
| f23 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 작업자가 피킹하고 자율이동로봇이 운반하는 동적 주문 피킹 연구(2025)가 있어, 로봇 배정이 사람 작업자의 배치와 맞물린다. | ref-132 | 아니오 | medium | 2025 | 피킹 / 수행 자원 | 원문 미열람 |
| f24 | [사실] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구(2025)가 있다. | ref-388 | 아니오 | medium | 2025 | 포장 / 수행 자원 | 원문 미열람 |
| f25 | [추정] | D. 계획·최적화의 14. 작업 순서·스케줄링 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계: Open-RMF 배정이 플릿 단위 입찰로 이루어지고 작업 요청 스키마에 작업 간 선후 필드가 없으므로, 피킹 로봇 완료 뒤 운반 로봇 출발 같은 제조사 간 인계 선후는 ROP 가 작업 흐름 수준에서 관리해야 할 것으로 보인다(oq-049). | ref-376, ref-125 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | — |
| f26 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 창고 MAPF 실행 연구(2019)는 지연이 쌓일 때 행동 의존 그래프로 순서를 지키며 실행을 이어가는 방법을 다루어, 계획 유지와 재계획의 판단이 두 영역을 잇는다. | ref-188 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f27 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: VDA 5050 에서 브로커 연결이 끊긴 로봇은 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행하므로, 통신 단절 때 ROP 가 다시 배정할 수 있는 몫은 아직 해제하지 않은 구간과 새 작업으로 한정될 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f28 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보: arXiv 2608.25690(2026-08)은 위치 스푸핑으로 오염된 에이전트가 계획 정보와 실행을 어긋나게 하면 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선이 사라질 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 제외하는 방법을 제안한다. | ref-540 | 아니오 | medium | 2026-08 | 예외·성과 | 원문 미열람 |
| f29 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: 같은 연구의 신뢰 인지 모니터는 위치 신뢰도와 작업 실행 행동 증거를 결합해 에이전트를 분류하므로, 실행 기록으로 이상 로봇을 가려 배정 입력에서 빼는 일이 모니터링과 배정을 잇는 지점이 될 것으로 보인다. | ref-540 | 아니오 | low | 2026-08 | 예외·성과 | 원문 미열람 |
| f30 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보: Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고, 웹 대시보드는 TLS 로 제공하며 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용한다고 설명한다. | ref-405 | 아니오 | medium | 2026-09-25 | — | — |
| f31 | [추정] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보: 작업 요청이 대시보드·API 서버를 거쳐 디스패처로 들어가고 배정이 플릿의 입찰 비용과 위치 보고에 기대므로, 누가 작업을 요청·우선 지정할 수 있는지와 입찰·위치 보고를 얼마나 믿을지가 배정의 보안 경계가 될 것으로 보인다. | ref-405, ref-376, ref-540 | 아니오 | low | 2026-09-25 | 제약 | — |
| f32 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 로봇 이동형 풀필먼트 시스템과 국내 자동물류센터의 이산 사건 시뮬레이션 연구가 배정 규칙을 가정한 미래에서 실험하는 도구로 쓰였고, 한 연구에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398, ref-402 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f33 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구가 있어, 경로망 설계 평가는 가정한 미래를 실험하는 쪽에 속하는 것으로 보인다. | ref-267 | 아니오 | low | 2024 | — | 원문 미열람 |
| f34 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전: 현장 도입 때 플릿별 경로망과 차선 방향, 대기·충전·주차 경유점을 traffic-editor 로 주석해 설정하는 일이 온보딩 작업이 될 것으로 보인다. | ref-079 | 아니오 | low | 2026-09-25 | — | — |
| f35 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: MAPF 연구는 정의·변형·벤치마크를 정리한 공통 틀을 가지고 있으나, 격자·단위 시간 가정의 벤치마크 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). | ref-186 | 아니오 | medium | 2019-06 | — | 원문 미열람 |
| f36 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 분산 배정기를 같은 사례 묶음과 통신 조건에서 이동 거리·안정성·계산 시간으로 비교하는 벤치마크(2026-09)가 있어, 배정 방식 선택을 시험 조건과 함께 평가하는 틀이 된다. | ref-539 | 아니오 | medium | 2026-09 | — | 원문 미열람 |
| f37 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 일정을 정하는 연구(2026-03)가 있어, 충전·배정 계획이 배터리 열화 관리와 이어진다. | ref-403 | 아니오 | medium | 2026-03 | 제약 | 원문 미열람 |
| f38 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있고(설정은 사람·AGV 모드만 가능), Open-RMF 데모는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-286, ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f39 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리: VDA 5050 은 진입 금지(BLOCKED)·속도 제한(SPEED_LIMIT)·해제(RELEASE)·우선(PRIORITY)·벌점(PENALTY) 등 구역 유형을 교통 관리 수단으로 정의하면서, 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f40 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 학습 기반 배차(이종 그래프 어텐션 스케줄러)와 LLM 기반 다중 로봇 작업 배정 연구가 있어, 분류 원문 8장의 '학습 기반 배차' 교차 규칙에 따라 두 영역이 이어진다. | ref-399, ref-090, ref-168 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f41 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있어, 학습 기반 경로 계획이 두 영역을 잇는다. | ref-199 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f42 | [추정] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영: 자율 피킹 로봇의 충전소 선택·충전 시간 결정에 심층 강화학습을 쓰는 연구(2026-07)가 있어, 학습 기반 충전 결정이 두 영역을 잇는 것으로 보인다. | ref-531 | 아니오 | low | 2026-07 | — | 원문 미열람 |
| f43 | [추정] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스: VDA 5050 은 구역·경로 해제로 교통 규칙을 정하되 조율 전략은 빼고, Open-RMF 는 여러 플릿의 교통 협상에서 시스템 통합사가 배치한 판정자가 조합을 고르게 하므로, 한 현장에서 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-057). | ref-031, ref-004 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 관제 기능 목록에 주문의 이동로봇 배정(Assignment of orders to the mobile robots)이 있고, 범위 절은 "interfaces to peripheral equipment, infrastructure components, or external IT systems"를 제외한다. (원문: 공식 저장소 main, 3.0.0 판)
- **f2**: f1 의 범위 제외와 f3 의 작업 요청 필드 구성(마감 필드 없음)에서 도출한 추정. (재인용: 2026-09-25-49)
- **f3**: 스키마 속성: unix_millis_earliest_start_time "(Optional) The earliest time that this task may start", unix_millis_request_time, priority, category, description, labels, requester, fleet_name. 마감·의존 필드 없음. (원문 열람: raw.githubusercontent.com)
- **f4**: 두 논문 제목·게시 페이지 주장 기준(출고 지시 정책, 동적 도착 주문의 재최적화). 원문 미열람. (재인용: 2026-09-25-49)
- **f5**: 저자 계산 실험 조건의 보고값이며 독립 재현 미확인. 14. 작업 순서·스케줄링 게시 페이지 3절 주장. (재인용: 2026-09-25-49)
- **f6**: 14. 작업 순서·스케줄링 게시 페이지 5절 예외·성과 칸 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f7**: 14. 작업 순서·스케줄링 게시 페이지 7절 표 주장. 이번 실행에서 스키마 재열람 안 함. (재인용: 2026-09-25-49)
- **f8**: 16. 공용 자원·충전·에너지 최적화 게시 페이지 10절 연결 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f9**: A. 업무·공급망 설계 대분류 페이지 D 연결 절의 검증된 주장. 현장 실측 아님. (재인용: 2026-09-25-49)
- **f10**: 13. 작업 배정 — MRTA 게시 페이지 10절과 B. 공통 정보·환경 모델 대분류 페이지 D 연결 절의 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f11**: 팩트시트 스키마: criticalLowChargingLevel 이하에서는 관제가 충전소로 보내는 주문만 보내야 한다. 템플릿: "recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate". (두 원문 모두 raw.githubusercontent.com 열람)
- **f12**: "The annotated Graphs are eventually exported as navigation graphs using the building_map_generator which are then used by respective rmf_fleet_adapters for path planning." (원문: ros2multirobotbook src/traffic-editor.md)
- **f13**: rmf_demos README: 충전량이 부족한 로봇의 일정에 충전 작업을 자동으로 삽입(로봇마다 지도에 표시된 충전 위치가 있다고 가정). 상태 스키마의 배터리 상태는 재열람 안 함.
- **f14**: "There are a couple different ways the Dispatcher evaluates the proposals such as fastest to finish, lowest cost, etc which can be configured." (원문: ros2multirobotbook src/task.md)
- **f15**: fleet_name: 이 작업을 수행하도록 허용된 플릿 이름 또는 플릿 이름 배열(선택 필드). (원문 열람, f3 과 같은 스키마)
- **f16**: "Any shared space is allowed to have a maximum of just one 'Read Only' fleet in operation." 협상은 제3자 판정자(시스템 통합사 배치)가 제안 조합을 고른다. (원문: ros2multirobotbook src/rmf-core.md)
- **f17**: 교통 조율의 전략·알고리즘·결정 과정(예: 경로, 우선순위, 혼잡, 교착 해소)은 포함하지 않는다고 적고, 관제 기능에 막힘 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 둔다. (원문 열람, 재서술)
- **f18**: LiftState 의 session_id 는 REQUEST_END_SESSION 요청을 보낼 때까지 승강기 제어권을 받은 세션을 기록한다. LiftRequest: AGV 모드에서는 "the doors are always held open when the lift cabin is stopped". (두 메시지 원문 열람)
- **f19**: 관제 기능 목록의 에너지 관리 항목(충전 주문이 운반 주문을 중단시킬 수 있음)과 충전 절의 과충전 보호 책임 문장(이동로봇 책임). (원문 열람, 재서술)
- **f20**: 명세는 MQTT 가 비동기이고 무선 전송이 믿을 수 없으므로 기반을 바꿀 수 없다고 적는다. 재정렬 범위는 여기서 도출한 추정. (원문 열람)
- **f21**: 검색 요약 기준: 10개 목표 500쌍 사례, 이상적·저하 통신 25개 조건(베르누이 손실, 길버트–엘리엇 손실, 레일리 페이딩), 협력 방문 시나리오. 사전 배정에서 HIPC·DMCHBA 는 모든 조건에서 안정. 원문 미열람, 프리프린트.
- **f22**: ref-401 은 KISTI ScienceON 수록 과제 보고서 '클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발'(제목 기준, 본문 미열람). 물류센터 적용 근거는 없음.
- **f23**: 13. 작업 배정 — MRTA 게시 페이지 5절 수행 자원 칸 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f24**: 14. 작업 순서·스케줄링 게시 페이지 5절·10절 주장(결과 수치 미확인). 원문 미열람. (재인용: 2026-09-25-49)
- **f25**: f14(플릿 단위 입찰)와 f3(선후 필드 없음)에서 도출. 공개 구현은 확인하지 못함.
- **f26**: 15. 다중 로봇 경로·교통 관리 — MAPF 게시 페이지 5절 예외·성과 칸 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f27**: "If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node." 재배정 범위는 이 규칙에서 도출한 추정. (원문 열람)
- **f28**: 검색 요약 기준: 온라인 다중 로봇 라우팅, 거리 제약 스푸핑 모델, 실제 GPS 스푸핑 데이터와 샌프란시스코 택시 수요로 실험(물류센터 조건 아님). 원문 미열람, 프리프린트.
- **f29**: 모니터가 확률적 위치 신뢰와 작업 실행의 행동 증거를 결합해 에이전트를 분류하고 탐지된 적대자를 이후 계획에서 제외한다는 검색 요약. 창고 적용은 추정. 원문 미열람.
- **f30**: "an enclave is a process or group of processes that will share the same identity and access control rules." 대시보드는 TLS 와 Keycloak 기반 OIDC 역할 토큰을 쓴다. (원문: ros2multirobotbook src/security.md)
- **f31**: f14(입찰 비용 기반 선정), f30(역할 기반 접근), f28(위치 스푸핑이 배정을 오염)을 결합한 추정. 창고 배정의 보안 사례는 찾지 못함.
- **f32**: 13. 작업 배정 — MRTA 게시 페이지 3절·10절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f33**: 15. 다중 로봇 경로·교통 관리 — MAPF 게시 페이지 10절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f34**: f12 의 주석 대상(차선 방향, 대기·충전 경유점)을 현장 설정 작업으로 해석한 추정.
- **f35**: 15. 다중 로봇 경로·교통 관리 — MAPF 게시 페이지 3절·11절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f36**: 검색 요약 기준: MinMax·MinSum 이동, 통신 강건성·요구량, 배정 신뢰성, 계산 부담, 규모 민감도를 비교. 이상 전달 조건의 계산 시간 중앙값 4.88 ms(DMCHBA)~1.346 s(DGA). 원문 미열람.
- **f37**: 13. 작업 배정 — MRTA 게시 페이지 10절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f38**: rmf_demos README: "All robots will get directed to the nearest parking spot when the emergency alarm is triggered." LiftState 모드 상수 MODE_FIRE·MODE_OFFLINE·MODE_EMERGENCY 등. (두 원문 열람)
- **f39**: 구역 유형 목록과, 이 문서가 기능·운영·시스템 안전 요구를 정하지 않고 안전 표준으로 간주·적용해서는 안 된다는 문장. (원문 열람, 재서술)
- **f40**: 13. 작업 배정 — MRTA 게시 페이지 10절 주장. LLM 배정 결과 수치는 출처 충돌(oq-030)이라 연결 서술에 쓰지 않음. 원문 미열람. (재인용: 2026-09-25-49)
- **f41**: 15. 다중 로봇 경로·교통 관리 — MAPF 게시 페이지 10절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f42**: 16. 공용 자원·충전·에너지 최적화 게시 페이지 10절 주장. 원문 미열람. (재인용: 2026-09-25-49)
- **f43**: f16(제3자 판정자)과 f17(조율 전략 제외)에서 도출한 추정.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/task.html | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 예 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 예 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | 논문 | medium | 2026-09-25 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 예 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 예 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2192437620300315 | 예 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 예 |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.17003 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/electronics15163562 | 예 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | 논문 | medium | 2026-09-25 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 예 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 예 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 2025 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 | 예 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | 논문 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 예 |
| ref-401 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 예 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21415 | 예 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.05683 | 예 |
| ref-539 | Lott, J., & Honary, V. | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 2026-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2609.13711 | 예 |
| ref-540 | arXiv 2608.25690 저자(미확인) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.25690 | 예 |

### 출처 요약

- **ref-031**: 관제–이동로봇 통신 명세(main 브랜치, 3.0.0). 범위 제외, 관제 기능(주문 배정·에너지 관리·교통 제어), 기반·호라이즌, 구역 유형, 연결 끊김 동작을 원문으로 확인.
- **ref-004**: 플릿 제어 수준(전체 제어·신호등·읽기 전용), 공유 공간당 읽기 전용 플릿 1개 제한, 제3자 판정자 협상을 원문으로 확인.
- **ref-376**: 디스패처의 BidNotice·BidProposal 입찰과 평가 기준 설정을 원문으로 확인.
- **ref-079**: 차선 양방향 속성, 대기·충전·주차 경유점, 문·승강기 주석, building_map_generator 주행 그래프 내보내기를 원문으로 확인.
- **ref-105**: recharge_threshold(0.10)·recharge_soc(1.0)·task_capabilities·finishing_request·로봇별 charger 설정을 원문으로 확인.
- **ref-125**: 작업 요청 스키마의 속성(가장 이른 시작 시각, 요청 시각, 우선순위, 범주, 설명, 라벨, 요청자, 플릿 이름)을 원문으로 확인. 마감·의존 필드 없음.
- **ref-228**: 팩트시트 스키마의 충전 파라미터(criticalLowChargingLevel, 최소·최대 희망 충전 수준, 최소 충전 시간)를 원문으로 확인.
- **ref-312**: 승강기 요청의 세션 id, 요청 유형(세션 종료·AGV 모드·사람 모드), 문 요청을 원문으로 확인.
- **ref-286**: 승강기 상태의 층·문·운행 상태, 운영 모드(사람·AGV·화재·오프라인·비상), 세션 id 를 원문으로 확인.
- **ref-104**: 비상 경보 시 가장 가까운 주차 위치로 이동, 충전량 부족 시 충전 작업 삽입, 데모 세계 구성을 원문으로 확인.
- **ref-405**: SROS 2 인클레이브 정의와 RMF 구성요소 권한 분리, 웹 대시보드의 TLS·OIDC 역할 인증을 원문으로 확인.
- **ref-051**: 원문 미열람. 이번 실행에서 다시 열지 않음. 로봇 상태 스키마(배터리 상태 등) 참고.
- **ref-134**: 원문 미열람. 자동 분류기가 있는 창고의 웨이브·웨이브리스 출고 지시 정책 연구.
- **ref-133**: 원문 미열람. 동적으로 도착하는 주문의 피킹 재최적화 연구.
- **ref-381**: 원문 미열람. 랙 이동 로봇 작업대의 주문·랙 순서 최적화 연구.
- **ref-385**: 원문 미열람. 풋월 주문 통합의 빈 방출 순서 문제.
- **ref-117**: 원문 미열람. 이번 실행에서 다시 열지 않음. B2MML 공통 스키마(Dependency1Type 등).
- **ref-533**: 원문 미열람. 자가 등반 로봇 창고의 배터리 관리 정책 평가.
- **ref-109**: 원문 미열람. 창고 충전소 배치 최적화.
- **ref-146**: 원문 미열람. RMFS 에너지 소비와 동적 우선순위 정책 평가.
- **ref-236**: 원문 미열람. 온톨로지 기반 실행 가능성 추론을 이종 다중 로봇 배정에 쓰는 연구.
- **ref-237**: 원문 미열람. 라인리스 이동 조립 시스템의 온톨로지 기반 작업 배정.
- **ref-132**: 원문 미열람. 작업자 피킹·AMR 운반 협업의 동적 주문 피킹 연구.
- **ref-388**: 원문 미열람. 국내 물류센터 작업자 스케줄링 연구.
- **ref-188**: 원문 미열람. 창고 MAPF 일정의 지속적·강건한 실행(행동 의존 그래프).
- **ref-398**: 원문 미열람. RMFS 결정 규칙의 이산 사건 시뮬레이션 평가.
- **ref-402**: 원문 미열람. 국내 자동물류센터 시뮬레이션·메타모델 설계 최적화.
- **ref-401**: 원문 미열람. 클라우드 연결 로봇·로봇그룹 작업 계획 과제 보고서(제목 기준).
- **ref-267**: 원문 미열람. 시뮬레이션 기반 다중 AGV 경로망 자동 설계.
- **ref-186**: 원문 미열람. MAPF 정의·변형·벤치마크 정리.
- **ref-403**: 원문 미열람. 플릿 수준 배터리 건강 인지 일정 계획.
- **ref-399**: 원문 미열람. 이종 그래프 어텐션 기반 학습 스케줄러.
- **ref-090**: 원문 미열람. LLM 기반 다중 로봇 작업 계획.
- **ref-168**: 원문 미열람. LLM 기반 건설 로봇 작업 배정과 전통 기법 비교.
- **ref-199**: 원문 미열람. 모방 학습 기반 지속형 MAPF.
- **ref-531**: 원문 미열람. 자율 피킹 로봇의 강화학습 기반 배터리 관리.
- **ref-539**: 원문 미열람. 분산 작업 배정기 6종을 패킷 손실·페이딩 등 통신 저하 조건에서 이동 거리·안정성·계산 시간으로 비교한 벤치마크(프리프린트, 검색 요약 기준).
- **ref-540**: 원문 미열람. 위치 스푸핑 하 온라인 다중 로봇 라우팅에서 공격 모델과 신뢰 인지 모니터로 적대 에이전트를 탐지·제외하는 방법(프리프린트, 택시 수요 데이터 실험, 검색 요약 기준).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 절 신규 작성(patches 로 이 절만 교체): A. 업무·공급망 설계(f1~f9), B. 공통 정보·환경 모델(f10~f13), C. 연결·실행 기반(f14~f22, 11. 분산 시스템·통신·컴퓨팅 구조 연결 f21·f22 신규), E. 협업·현장 운영(f23~f27, f29 — 19. 모니터링·이상 탐지·원인 분석 연결 신규), F. 도입·검증·유지관리(f32~f37), G. 안전·보안·지능·거버넌스(f28·f30·f31 — 26. 사이버보안·접근권한·개인정보 연결 신규, f38·f39 25. 안전·위험 관리, f40~f42 27. AI·학습·적응과 모델 운영, f43 28. 표준·상호운용성·다사업자 거버넌스). 27. AI·학습·적응과 모델 운영 연결은 분류 원문 8장 '학습 기반 배차' 교차 규칙으로 표기. 22. 시뮬레이션·예측용 디지털 트윈 연결(f32·f33)은 가정한 미래 실험, 8. 실시간 세계 상태·데이터 일관성 연결(f13)은 현재 상태 표현으로 구분. f28·f29 는 택시 수요 데이터 기반 프리프린트라 물류 적용이 확인되지 않았음을 함께 적는다. '아직 다루지 않은 연결'에 7. 화물·재고·자산 식별과 추적 명시. 새 각주 정의는 참고 자료 절에 추가(기존 ref-005·ref-006 유지). 같은 연결이 A·B·C 대분류 페이지에도 실려 있으면 같은 각주를 쓴다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 플릿 제어 수준 | Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only) | Open-RMF 가 제조사 플릿과 연동하는 정도를 경로 지시까지 하는 전체 제어, 일시정지·재개만 하는 신호등, 상태만 받는 읽기 전용으로 나눈 구분이다. |
| 기반·호라이즌 | Base / Horizon (VDA 5050) | VDA 5050 주문에서 로봇이 주행하도록 해제되어 바꿀 수 없는 경로 구간(기반)과 아직 해제되지 않아 주문 갱신으로 바꿀 수 있는 예정 구간(호라이즌)을 가리킨다. |

## 열린 질문

새로 생긴 질문:

- 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? | 관련 영역: 13. 작업 배정 — MRTA, 26. 사이버보안·접근권한·개인정보, 19. 모니터링·이상 탐지·원인 분석 | 근거: f28 | 종류: 일반
- 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 11. 분산 시스템·통신·컴퓨팅 구조 | 근거: f21 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 38 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 2건
- 미확인 항목:
    - f21·f36: ref-539 원문 미열람, 수치는 검색 요약 범위
    - f28·f29: ref-540 원문 미열람, 택시 수요 기반 실험이라 물류센터 적용 미확인
    - f22: ref-401 은 제목만 확인, 본문·수행기관 미확인
    - 재인용 finding(f4~f10, f23·f24·f26, f32·f33·f35·f37, f40~f42)은 게시 페이지 주장 재인용이며 원문 미열람
    - 7. 화물·재고·자산 식별과 추적과 D. 계획·최적화를 잇는 근거 미확보
    - 모든 finding 교차 확인 없음(단일 출처이거나 같은 발행 주체)
- 범위 경계 위반 의심:
    - f19: 과충전 보호는 분류 원문 9장 '로봇 자체 지능·제어' 경계의 연계 대상이며 ROP 는 충전 시작·중지 요청과 상태 확인만 맡는다고 구분
    - f18·f38: 승강기 운행·설비 안전 제어는 '시설·설비 제어' 경계의 연계 대상, ROP 는 세션 요청·모드 확인만
    - f2·f3: 납기·출하 마감 결정은 상위 업무 시스템 쪽 연계 대상
    - f39: VDA 5050 구역은 안전 표준이 아니라고 명세가 밝히므로 25. 안전·위험 관리 연결은 교통 관리 수단과 안전 기능의 구분으로만 서술해야 함
- 한계: web_fetch_available: false · fetch_mode mirror_only. 대분류 연결 실행(R-3). 같은 대상의 이전 브리프 2026-09-25-49 가 있으나 D. 계획·최적화 페이지가 여전히 비어 있어 이번에 전체 브리프를 다시 냈다. 그 finding 을 재인용하되, raw.githubusercontent.com 으로 원문을 다시 연 재사용 출처 11건(ref-031, ref-004, ref-376, ref-079, ref-105, ref-125, ref-228, ref-312, ref-286, ref-104, ref-405)으로 f1·f3·f11·f12·f14~f20·f27·f30·f38·f39 를 원문 문구 기준으로 보강했다(ref-125·ref-228 은 이전 실행에서 미열람이었음; fleet_adapter_template·rmf_api_msgs·rmf_internal_msgs·rmf_demos 는 미러 목록에 없어 github blob→raw 경로로 열었다). 새로 f15(fleet_name), f21·f22·f36(11. 분산 시스템·통신·컴퓨팅 구조, 23. 시험·형식 검증·벤치마크), f28~f31(26. 사이버보안·접근권한·개인정보, 19. 모니터링·이상 탐지·원인 분석) 연결을 추가했다. 검색 7회/30, 신규 출처 2건/15(ref-539·ref-540, 예약 구간 안), 둘 다 원문 미열람 프리프린트(신뢰도 상한 medium). PMC 논문(Multi-Robot Preemptive Task Scheduling with Fault Recovery) 열람은 프록시 거절로 실패해 넣지 않았다. 한국어 검색 1회는 업체 블로그뿐이라 출처로 쓰지 않았다. E·F·G 세부영역 다수가 seed 이거나(19·20·21·22·23·24·25·26·27·28) 요약만 입력되어, 연결 서술이 D. 계획·최적화 쪽 근거에 기댄다. 실행 2026-09-25-52(21. 온보딩·설정·현장 시운전)의 자료는 아직 게시 전이라 쓰지 않았다. 7. 화물·재고·자산 식별과 추적과의 연결은 근거가 없어 finding 을 내지 않았다(스토리텔러가 '아직 다루지 않은 연결'로 표기). 정정 요청 없음. 해결된 열린 질문 없음.
