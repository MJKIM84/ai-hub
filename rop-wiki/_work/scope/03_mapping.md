# 03. 매핑 — 옛 구조에서 새 구조로

> 작성 2026-09-28 · 루프 프롬프트 B단계 · 입력: [02. 카테고리화](02_categories.md) · 다음 문서: [04. 검증](04_verify.md)  
> 이 문서는 `build_scope.py`가 `data/*.yaml`에서 만든다. 고칠 때는 데이터를 고치고 다시 생성한다.

이 문서는 옛 이름을 그대로 인용한다(무엇이 어디로 가는지 보여 주는 문서이기 때문이다). 새 구조의 이름·정의는 [02](02_categories.md)가 기준이다.

## 0. 요약

| 대상 | 결과 |
|---|---|
| 대분류 7개 → 카테고리 17개 | 분할 5, 유지 1, 이름 변경 1. 새 카테고리 가운데 옛 대분류를 잇는 것 7, 신규 10 |
| 세부영역 28개 → 영역 67개 | 유지 10, 이동 5, 이름 변경 4, 분할 9, 병합 0. 갈 곳 없는 옛 영역 0 |
| 새 영역 67개의 출처 | 옛 영역을 주로 잇는 것 28, 옛 영역 일부에서 시작 13, 신규 26 |
| 트랙 3개 | 유지 1(온톨로지), 확장·이름 변경 1(챗봇 → 채팅 기반 구성·운영), 두 안 1(도면 인식) |
| 확장 아이디어 | 유지 3(연결 구조 페이지 포함), 이름 변경·정의 확장 1(아이디어 2) |
| 주소가 바뀌는 기존 페이지 | 안 1: 최소 35, 선택에 따라 최대 56. 안 2: 0 (6절) |

처리 종류는 스크립트가 계산한다: 일부가 다른 영역으로 가면 **분할**, 이름이 바뀌면 **이름 변경**, 이름이 같고 이어받는 카테고리로 가면 **유지**, 이름이 같고 다른 카테고리로 가면 **이동**. 옛 영역 둘 이상이 한 영역으로 합쳐지는 **병합**은 이번 안에 없다.

## 1. 대분류 7개

| 옛 대분류 | 옛 경로 | 처리 | 잇는 새 카테고리 | 영역이 가는 곳 |
|---|---|---|---|---|
| A. 업무·공급망 설계 | `categories/a-business-supply-chain-design/index.md` | 분할 | A. 기획·사업 | 1→F4, 2→G1, 3→I3, 4→J3(주)·A3. 대분류 페이지는 새 A(기획·사업)가 잇는다. 핵심 질문(무슨 일을 왜, 얼마나)이 같은 계열이다. |
| B. 공통 정보·환경 모델 | `categories/b-common-information-and-environment-model/index.md` | 분할 | B. 로봇 온톨로지 — 이기종 로봇 등록·능력 표현·시스템·로봇 연동 | 5→B, 6→D, 7·8→E. 대분류 페이지는 새 B(로봇 온톨로지)가 잇는다. ‘같은 의미로 이해’가 온톨로지의 일이다. |
| C. 연결·실행 기반 | `categories/c-connectivity-and-execution-foundation/index.md` | 분할 | F. 연동 — 로봇·설비·업무 시스템 | 9·10→F, 11→K, 12→H. 대분류 페이지는 새 F(연동)가 잇는다. |
| D. 계획·최적화 | `categories/d-planning-and-optimization/index.md` | 유지 | G. 계획·최적화 | 13~16은 그대로 G로. 옛 2번이 G1로 들어온다. |
| E. 협업·현장 운영 | `categories/e-collaboration-and-field-operations/index.md` | 분할 | H. 실행·협업·예외 복구 | 17·18(주)·20→H, 18(일부)·19→J. 대분류 페이지는 새 H(실행·협업·예외 복구)가 잇는다. |
| F. 도입·검증·유지관리 | `categories/f-deployment-verification-and-maintenance/index.md` | 이름 변경 | O. 검증·도입·수명주기 | 23·24→O, 21→O2(주)·B1, 22→I2. 새 O(검증·도입·수명주기)가 잇는다. |
| G. 안전·보안·지능·거버넌스 | `categories/g-safety-security-intelligence-and-governance/index.md` | 분할 | P. 거버넌스·법규·사회 | 25→M, 26→N, 27→L, 28→F2(주)·P1. 대분류 페이지는 새 P(거버넌스·법규·사회)가 잇는다. 핵심 질문(공통 제약과 관리 체계)이 거버넌스 계열이다. |

## 2. 세부영역 28개

| 옛 영역 | 옛 경로 | 처리 | 주 영역(새) | 일부가 가는 곳 | 안 1 새 경로 | 비고 |
|---|---|---|---|---|---|---|
| 1. 주문·업무 시스템 연계 | `categories/a-business-supply-chain-design/01-order-and-business-system-integration.md` | 이름 변경 | F4 업무 시스템 연동 | - | `categories/integration/business-system-integration.md` | ‘주문’을 빼고 업무 요청 전반(병원·호텔·빌딩 시스템 포함)으로 넓힘 |
| 2. 공정·워크플로 모델링 | `categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md` | 이름 변경 | G1 작업·워크플로 모델링 | - | `categories/planning-and-optimization/task-and-workflow-modeling.md` | ‘공정’을 작업 전반으로 넓히고 계획의 입력으로 옮김 |
| 3. 처리능력·거점·설비 계획 | `categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md` | 이름 변경 | I3 처리능력·규모·배치 설계 | - | `categories/design-and-simulation/capacity-sizing-and-layout-design.md` | ‘거점’을 빼고 설계 사용자의 일로 옮김 |
| 4. 성과·경제성·프로세스 개선 | `categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md` | 분할 | J3 운영 성과 측정·개선 | A3 경제성·조달·사업 모델 | `categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md` | 성과 측정·개선은 J3, 경제성은 A3 |
| 5. 로봇 능력·작업 온톨로지 | `categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md` | 분할 | B2 로봇 능력·작업 표현 | B1 이기종 로봇 등록, B3 온톨로지 기반 시스템·로봇 연동 | `categories/robot-ontology/robot-capability-and-task-representation.md` | 능력·작업 표현은 B2, 등록·문서 추출은 B1, 질의·실행 연결은 B3 |
| 6. 지도·공간·위치 모델 | `categories/b-common-information-and-environment-model/06-map-space-and-location-model.md` | 분할 | D2 지도·공간·위치 모델 | D1 도면·BIM에서 지도 만들기, D3 장소 의미·지도 관리 | `categories/space-and-map-model/map-space-and-location-model.md` | 통합 공간 모델은 D2, 도면·BIM·CAD는 D1, 장소 이름·지도 버전은 D3 |
| 7. 화물·재고·자산 식별과 추적 | `categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md` | 이름 변경 | E1 작업 대상·자산 식별과 인계 추적 | - | `categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md` | ‘화물·재고’를 작업 대상 전반(물품·도구·검체·세탁물 등)으로 넓힘 |
| 8. 실시간 세계 상태·데이터 일관성 | `categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md` | 이동 | E2 실시간 세계 상태·데이터 일관성 | - | `categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md` | - |
| 9. 로봇·제조사 관제 연동 | `categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md` | 유지 | F1 로봇·제조사 관제 연동 | - | `categories/integration/robot-and-vendor-fleet-manager-integration.md` | - |
| 10. 설비·건물 시스템 연동 | `categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md` | 유지 | F3 설비·건물 시스템 연동 | - | `categories/integration/facility-and-building-system-integration.md` | - |
| 11. 분산 시스템·통신·컴퓨팅 구조 | `categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md` | 분할 | K2 분산 시스템·통신·컴퓨팅 구조 | K1 플랫폼 아키텍처·외부 API | `categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md` | 네트워크·가용성·다거점은 K2, 클라우드·현장 서버·로봇 역할 분담은 K1 |
| 12. 명령·작업 실행의 신뢰성 | `categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md` | 이동 | H1 명령·작업 실행의 신뢰성 | - | `categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md` | - |
| 13. 작업 배정 — MRTA | `categories/d-planning-and-optimization/13-task-allocation-mrta.md` | 유지 | G2 작업 배정 — MRTA | - | `categories/planning-and-optimization/task-allocation-mrta.md` | - |
| 14. 작업 순서·스케줄링 | `categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md` | 유지 | G3 작업 순서·스케줄링 | - | `categories/planning-and-optimization/task-sequencing-and-scheduling.md` | - |
| 15. 다중 로봇 경로·교통 관리 — MAPF | `categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md` | 유지 | G4 다중 로봇 경로·교통 관리 — MAPF | - | `categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md` | - |
| 16. 공용 자원·충전·에너지 최적화 | `categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md` | 유지 | G5 공용 자원·충전·에너지 최적화 | - | `categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md` | - |
| 17. 로봇 간 협업·물리적 인계 | `categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md` | 유지 | H2 로봇 간 협업·물리적 인계 | - | `categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md` | - |
| 18. 사람–로봇 협업·운영 인터페이스 | `categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md` | 분할 | H3 사람–로봇 협업 | J1 관제 화면·실행 기록 | `categories/execution-collaboration-and-recovery/human-robot-collaboration.md` | 협업은 H3, 운영 인터페이스(상태 표시·관제 화면)는 J1 |
| 19. 모니터링·이상 탐지·원인 분석 | `categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md` | 이동 | J2 모니터링·이상 탐지·원인 분석 | - | `categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md` | - |
| 20. 예외 복구·재계획·업무 연속성 | `categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md` | 유지 | H4 예외 복구·재계획·업무 연속성 | - | `categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md` | - |
| 21. 온보딩·설정·현장 시운전 | `categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md` | 분할 | O2 현장 조사·설치·시운전 | B1 이기종 로봇 등록 | `categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md` | 설치·설정·시운전은 O2, 로봇 등록·기능 탐색·문서 분석은 B1 |
| 22. 시뮬레이션·예측용 디지털 트윈 | `categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md` | 이동 | I2 시뮬레이션·예측용 디지털 트윈 | - | `categories/design-and-simulation/simulation-and-predictive-digital-twin.md` | - |
| 23. 시험·형식 검증·벤치마크 | `categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md` | 유지 | O1 시험·형식 검증·벤치마크 | - | `categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md` | - |
| 24. 자산·소프트웨어 수명주기 관리 | `categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md` | 유지 | O4 자산·소프트웨어 수명주기 관리 | - | `categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md` | - |
| 25. 안전·위험 관리 | `categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md` | 이동 | M1 안전·위험 관리 | - | `categories/safety/safety-and-risk-management.md` | - |
| 26. 사이버보안·접근권한·개인정보 | `categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md` | 분할 | N1 인증·권한·격리 | N2 통신 보호·위협 관리·감사, N3 개인정보·영상 데이터 | `categories/security-and-privacy/authentication-authorization-and-isolation.md` | 인증·권한·격리는 N1, 통신 보호·위협은 N2, 개인정보는 N3 |
| 27. AI·학습·적응과 모델 운영 | `categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md` | 분할 | L4 AI·학습·적응과 모델 운영 | L1 로봇 기반 모델·언어 모델 계획, L2 문서·도면·장면 이해, L3 예측·학습 기반 최적화 | `categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md` | 실행 사용 기준·모델 운영은 L4, 언어 모델 계획은 L1, 문서·도면 해석은 L2, 학습 기반 최적화·예측은 L3 |
| 28. 표준·상호운용성·다사업자 거버넌스 | `categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md` | 분할 | F2 상호운용 표준·적합성 | P1 다사업자 책임·계약·데이터 | `categories/integration/interoperability-standards-and-conformance.md` | 표준·상호운용성은 F2, 다사업자 거버넌스는 P1 |

## 3. 새 영역 67개의 출처

| 새 영역 | 카테고리 | 구분 | 옛 영역(주) | 옛 영역(일부) | 기존 페이지에서 가져올 것 | 항목 수 |
|---|---|---|---|---|---|---|
| A1 기술·시장·업체 동향 | A | 신규 | - | - | - | 3 |
| A2 사용 사례·요구·책임 범위 | A | 신규 | - | - | about/scope-boundary.md(원문 9장 경계표) | 3 |
| A3 경제성·조달·사업 모델 | A | 일부에서 시작 | - | 4 | - | 3 |
| B1 이기종 로봇 등록 | B | 일부에서 시작 | - | 5, 21 | - | 5 |
| B2 로봇 능력·작업 표현 | B | 계승 | 5 | - | - | 5 |
| B3 온톨로지 기반 시스템·로봇 연동 | B | 일부에서 시작 | - | 5 | - | 4 |
| B4 온톨로지 검증·변경 관리 | B | 신규 | - | - | tracks/manual-capability-ontology 단계 5·6 페이지(링크) | 2 |
| C1 채팅으로 맵 작성 | C | 신규 | - | - | tracks/floorplan-recognition 공간 그래프 스키마 초안(링크); about/simulator.md | 2 |
| C2 채팅으로 시나리오 구성 | C | 신규 | - | - | about/simulator.md(대화로 작업 구성하기) | 2 |
| C3 채팅으로 로봇 구성 | C | 신규 | - | - | - | 2 |
| C4 채팅으로 실제 상황 시뮬레이션 재현 | C | 신규 | - | - | - | 3 |
| C5 채팅으로 업무 지시·오케스트레이션 | C | 신규 | - | - | tracks/nl-task-chatbot 단계 1~5·업무 분해·배정 설계 초안(링크); ideas/nl-task-chatbot.md | 3 |
| C6 대화형 기능의 신뢰·기반 | C | 신규 | - | - | tracks/nl-task-chatbot 단계 4 오해석 방지(링크) | 6 |
| D1 도면·BIM에서 지도 만들기 | D | 일부에서 시작 | - | 6 | - | 3 |
| D2 지도·공간·위치 모델 | D | 계승 | 6 | - | - | 5 |
| D3 장소 의미·지도 관리 | D | 일부에서 시작 | - | 6 | - | 3 |
| E1 작업 대상·자산 식별과 인계 추적 | E | 계승 | 7 | - | - | 4 |
| E2 실시간 세계 상태·데이터 일관성 | E | 계승 | 8 | - | - | 2 |
| E3 사람·보행자 모델 | E | 신규 | - | - | - | 2 |
| F1 로봇·제조사 관제 연동 | F | 계승 | 9 | - | - | 4 |
| F2 상호운용 표준·적합성 | F | 계승 | 28 | - | - | 2 |
| F3 설비·건물 시스템 연동 | F | 계승 | 10 | - | - | 4 |
| F4 업무 시스템 연동 | F | 계승 | 1 | - | - | 2 |
| G1 작업·워크플로 모델링 | G | 계승 | 2 | - | - | 3 |
| G2 작업 배정 — MRTA | G | 계승 | 13 | - | - | 2 |
| G3 작업 순서·스케줄링 | G | 계승 | 14 | - | - | 2 |
| G4 다중 로봇 경로·교통 관리 — MAPF | G | 계승 | 15 | - | - | 2 |
| G5 공용 자원·충전·에너지 최적화 | G | 계승 | 16 | - | - | 2 |
| H1 명령·작업 실행의 신뢰성 | H | 계승 | 12 | - | - | 3 |
| H2 로봇 간 협업·물리적 인계 | H | 계승 | 17 | - | - | 3 |
| H3 사람–로봇 협업 | H | 계승 | 18 | - | - | 3 |
| H4 예외 복구·재계획·업무 연속성 | H | 계승 | 20 | - | - | 2 |
| I1 시나리오 모델·편집 | I | 신규 | - | - | about/simulator.md | 3 |
| I2 시뮬레이션·예측용 디지털 트윈 | I | 계승 | 22 | - | - | 4 |
| I3 처리능력·규모·배치 설계 | I | 계승 | 3 | - | - | 4 |
| I4 가상 시운전·실제 상황 재현 | I | 신규 | - | - | - | 5 |
| J1 관제 화면·실행 기록 | J | 일부에서 시작 | - | 18 | - | 3 |
| J2 모니터링·이상 탐지·원인 분석 | J | 계승 | 19 | - | - | 5 |
| J3 운영 성과 측정·개선 | J | 계승 | 4 | - | - | 3 |
| J4 운영 절차·요청 창구 | J | 신규 | - | - | - | 2 |
| K1 플랫폼 아키텍처·외부 API | K | 일부에서 시작 | - | 11 | - | 3 |
| K2 분산 시스템·통신·컴퓨팅 구조 | K | 계승 | 11 | - | - | 4 |
| K3 데이터·관측성·배포 | K | 신규 | - | - | - | 4 |
| L1 로봇 기반 모델·언어 모델 계획 | L | 일부에서 시작 | - | 27 | - | 2 |
| L2 문서·도면·장면 이해 | L | 일부에서 시작 | - | 27 | - | 2 |
| L3 예측·학습 기반 최적화 | L | 일부에서 시작 | - | 27 | - | 2 |
| L4 AI·학습·적응과 모델 운영 | L | 계승 | 27 | - | - | 2 |
| M1 안전·위험 관리 | M | 계승 | 25 | - | - | 4 |
| M2 사람 근접 안전 | M | 신규 | - | - | - | 2 |
| M3 안전 표준·인증·사고 조사 | M | 신규 | - | - | - | 2 |
| N1 인증·권한·격리 | N | 계승 | 26 | - | - | 4 |
| N2 통신 보호·위협 관리·감사 | N | 일부에서 시작 | - | 26 | - | 4 |
| N3 개인정보·영상 데이터 | N | 일부에서 시작 | - | 26 | - | 2 |
| O1 시험·형식 검증·벤치마크 | O | 계승 | 23 | - | - | 6 |
| O2 현장 조사·설치·시운전 | O | 계승 | 21 | - | - | 5 |
| O3 운영 이관·확대·교육 | O | 신규 | - | - | - | 3 |
| O4 자산·소프트웨어 수명주기 관리 | O | 계승 | 24 | - | - | 4 |
| P1 다사업자 책임·계약·데이터 | P | 일부에서 시작 | - | 28 | - | 4 |
| P2 법·규제·보험·라이선스 | P | 신규 | - | - | - | 3 |
| P3 노동·수용성·접근성 | P | 신규 | - | - | - | 2 |
| Q1 물류창고 | Q | 신규 | - | - | flow-matrix.md(물류 흐름 7단계 × 여섯 항목); 28개 영역 페이지 5절의 물류창고 시나리오(절 이동) | 1 |
| Q2 제조 공장 | Q | 신규 | - | - | - | 1 |
| Q3 병원·의료 | Q | 신규 | - | - | - | 1 |
| Q4 상업 시설 | Q | 신규 | - | - | - | 1 |
| Q5 가정·공동주택 | Q | 신규 | - | - | - | 1 |
| Q6 실외 | Q | 신규 | - | - | - | 1 |
| Q7 기타 현장 | Q | 신규 | - | - | - | 2 |

## 4. 트랙 개편안 (멈춤 1에서 결정)

### 매뉴얼 기반 로봇 기능 온톨로지 (`manual-capability-ontology`) — 유지

- 중심 영역: 옛 5 → 새 B2 로봇 능력·작업 표현
- 제안: 이름·주소·7단계를 그대로 둔다. 중심 영역을 B2로 바꾸고 함께 필요한 영역에 B1·B3·B4를 더한다. 옛 관련 영역 번호는 매핑표로 새 영역에 옮긴다. 단계 4 이름에 시스템 연동을 드러내는 것을 제안한다(‘온톨로지를 실행·시스템 연동에 연결하는 방법 조사’) [가정].

### 자연어 업무 지시 챗봇 (`nl-task-chatbot`) — 확장·이름 변경

- 중심 영역: 옛 13 → 새 C5 채팅으로 업무 지시·오케스트레이션
- 제안: 이름을 ‘채팅 기반 구성·운영’으로 바꾸고, 중심 영역을 C1~C6 전체로 넓힌다(대표 C5). 연구 목표에 맵 작성·시나리오 구성·로봇 구성·실제 상황 시뮬레이션 재현을 더한다.
- 새 이름: 채팅 기반 구성·운영 (주소 정책 안 1이면 슬러그 `chat-based-configuration-and-operation`, 안 2이면 `nl-task-chatbot` 유지)
- 현재 페이지 10개, 단계 1~5 페이지의 고유 출처 219개.

단계 배치 — 이어 붙이기 (권장):

- 1 선행 연구·제품 사례 조사 (유지)
- 2 필요한 데이터와 표준 조사 (유지)
- 3 업무 지시 구현 가설 설계 (표시 이름만 변경)
- 4 오해석 방지와 확인 절차 (유지)
- 5 업무 지시 검증과 가설 판정 (표시 이름만 변경)
- 6 채팅으로 맵 작성 (신규)
- 7 채팅으로 시나리오 구성 (신규)
- 8 채팅으로 로봇 구성 (신규)
- 9 채팅으로 실제 상황 시뮬레이션 재현 (신규)
- 10 대화형 구성·운영 통합 검증과 가설 판정 (신규)

6~9단계는 각 기능의 선행 연구·구현 가설·확인 절차·검증 지표를 한 단계 안에서 다룬다. 내용이 있는 기존 1~5단계 페이지의 번호와 파일이 그대로다.

단계 배치 — 재배열:

- 1 선행 연구·제품 사례 조사
- 2 필요한 데이터와 표준 조사
- 3 채팅으로 맵 작성
- 4 채팅으로 시나리오 구성
- 5 채팅으로 로봇 구성
- 6 채팅으로 실제 상황 시뮬레이션 재현
- 7 채팅으로 업무 지시(기존 3)
- 8 오해석 방지와 확인 절차(기존 4)
- 9 검증 방법과 가설 판정(기존 5)

읽는 순서는 자연스럽지만, 내용이 있는 기존 3~5단계 페이지 3개의 번호와 파일 이름이 바뀐다.


### 건축 도면 자동 인식 (`floorplan-recognition`) — 두 안

- 중심 영역: 옛 6 → 새 D1 도면·BIM에서 지도 만들기
- 현재 페이지 10개, 단계 1~5 페이지의 고유 출처 208개.

1. (가) 채팅 트랙에 합치기: 트랙을 끝내고(status done), 단계 페이지 5개·공간 그래프 스키마 초안·실험 페이지를 D1 영역과 채팅 트랙 ‘채팅으로 맵 작성’ 단계의 참고 자료로 옮긴다. 트랙 페이지 10개의 주소가 바뀐다(리다이렉트). 일일 실행이 채팅 트랙에 모이지만, 따로 큰 도면 인식 문헌이 채팅 한 단계 밑으로 들어간다.
2. (나) 별도 트랙 유지 (권장): 트랙을 그대로 두고 중심 영역을 D1로 바꾼다. 채팅 트랙의 ‘채팅으로 맵 작성’ 단계가 이 트랙의 공간 그래프 초안을 입력으로 쓴다고 명시한다. 주소 변경 0.

## 5. 확장 아이디어와 기타 페이지

| 페이지 | 처리 | 내용 |
|---|---|---|
| `ideas/robot-capability-ontology.md` (아이디어 1. 로봇 기능 온톨로지) | 유지 | 관련 영역을 새 영역(B1~B4 중심)으로 바꾼다 |
| `ideas/nl-task-chatbot.md` (아이디어 2. 자연어 업무 지시 챗봇) | 이름 변경 → 아이디어 2. 채팅 기반 구성·운영 | 사용자 09-28 정의(맵 작성·시나리오 구성·로봇 구성·실제 상황 시뮬레이션 재현·업무 지시)를 새 정의로 싣고, 옛 정의 문구는 이력으로 남긴다 |
| `ideas/floorplan-recognition.md` (아이디어 3. 건축 도면 자동 인식) | 유지 | 중심 영역을 D1로, C1(채팅으로 맵 작성)과 연결 |
| `ideas/index.md` (확장 아이디어 연결 구조) | 유지 | 28영역 매핑표를 새 영역 기준으로 다시 만든다 |
| `flow-matrix.md` | 이름 변경 | ‘물류 흐름 매트릭스’를 ‘현장 유형 × 카테고리 적용 사례 매트릭스’로 바꾸고, 물류 7단계 내용은 Q1(물류창고) 사례로 옮긴다 |
| `index.md` | 내용 교체 | 홈 첫 문단·대분류 표를 새 개념과 17개 카테고리로 |
| `about/what-is-rop.md` | 내용 교체 | ROP란 무엇인가를 새 개념 문장으로 |
| `about/research-method.md` | 내용 교체 | 연구 방법을 리스트업 → 카테고리화 → 출처 수집으로 |
| `about/scope-boundary.md` | 문구 수정 | 경계표는 유지하고 A2의 근거로 연결 |
| `about/idea-mapping.md` | 내용 교체 | 아이디어–영역 매핑을 새 영역 기준으로 |
| `topics/** (주제 페이지)` | 프런트매터 갱신 | primary_area_no 를 새 영역 ID로. 주소는 그대로 |
| `glossary/**·references/** 등 링크가 있는 페이지` | 링크 갱신 | 주소 정책 안 1이면 스크립트로 링크를 새 경로로 바꾼다 |

## 6. 주소(URL) 영향

- 안 1 — 새 경로 + 리다이렉트 (권장): 카테고리·영역 경로를 새 슬러그로 바꾸고(문자·번호 접두어 없이, 순서가 바뀌어도 주소 유지), 옛 주소는 mkdocs-redirects(버전 고정)로 새 주소에 잇는다. 옛 슬러그의 ‘business-supply-chain-design’ 같은 옛 틀이 주소에서 사라진다.
- 안 2 — 옛 경로 유지: 기존 파일 경로는 그대로 두고 내비게이션·제목만 새 구조로 바꾼다. 새 영역만 새 경로에 만든다. 주소는 안 바뀌지만, 옛 디렉터리 이름이 주소에 남고 카테고리와 디렉터리가 어긋난다.

| 바뀌는 기존 페이지 | 안 1 | 안 2 |
|---|---|---|
| 대분류 페이지 | 7 | 0 |
| 세부영역 페이지 | 28 | 0 |
| 챗봇 트랙 페이지(슬러그를 새 이름으로 바꿀 때) | 10 | 0 |
| 흐름 매트릭스 페이지(이름을 바꿀 때) | 1 | 0 |
| 도면 트랙 페이지((가) 합치기를 고를 때) | 10 | 0 |
| **합계** | 최소 35, 최대 56 | 0 |

새로 생기는 페이지: 영역 39개(옛 영역을 잇지 않는 영역), 카테고리 페이지 10개.

링크 갱신 범위: 옛 대분류 슬러그를 본문에 담은 파일 826개. 안 1이면 스크립트로 새 경로로 바꾸고, 안 2이면 이름이 바뀐 영역의 링크 글자만 바꾼다. 영역 번호 필드(area_no·primary_area_no·related_areas)가 있는 페이지 1215개(그중 주제 페이지 145개)는 두 안 모두 새 영역 ID로 바꾼다. 주제·용어·참고문헌 페이지 자체의 주소는 바뀌지 않는다.

### 안 1 리다이렉트 목록 (옛 경로 → 새 경로)

| 옛 경로 | 새 경로 |
|---|---|
| `categories/a-business-supply-chain-design/index.md` | `categories/planning-and-business/index.md` |
| `categories/b-common-information-and-environment-model/index.md` | `categories/robot-ontology/index.md` |
| `categories/c-connectivity-and-execution-foundation/index.md` | `categories/integration/index.md` |
| `categories/d-planning-and-optimization/index.md` | `categories/planning-and-optimization/index.md` |
| `categories/e-collaboration-and-field-operations/index.md` | `categories/execution-collaboration-and-recovery/index.md` |
| `categories/f-deployment-verification-and-maintenance/index.md` | `categories/verification-deployment-and-lifecycle/index.md` |
| `categories/g-safety-security-intelligence-and-governance/index.md` | `categories/governance-law-and-society/index.md` |
| `categories/a-business-supply-chain-design/01-order-and-business-system-integration.md` | `categories/integration/business-system-integration.md` |
| `categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md` | `categories/planning-and-optimization/task-and-workflow-modeling.md` |
| `categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md` | `categories/design-and-simulation/capacity-sizing-and-layout-design.md` |
| `categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md` | `categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md` |
| `categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md` | `categories/robot-ontology/robot-capability-and-task-representation.md` |
| `categories/b-common-information-and-environment-model/06-map-space-and-location-model.md` | `categories/space-and-map-model/map-space-and-location-model.md` |
| `categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md` | `categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md` |
| `categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md` | `categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md` |
| `categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md` | `categories/integration/robot-and-vendor-fleet-manager-integration.md` |
| `categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md` | `categories/integration/facility-and-building-system-integration.md` |
| `categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md` | `categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md` |
| `categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md` | `categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md` |
| `categories/d-planning-and-optimization/13-task-allocation-mrta.md` | `categories/planning-and-optimization/task-allocation-mrta.md` |
| `categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md` | `categories/planning-and-optimization/task-sequencing-and-scheduling.md` |
| `categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md` | `categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md` |
| `categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md` | `categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md` |
| `categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md` | `categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md` |
| `categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md` | `categories/execution-collaboration-and-recovery/human-robot-collaboration.md` |
| `categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md` | `categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md` |
| `categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md` | `categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md` |
| `categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md` | `categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md` |
| `categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md` | `categories/design-and-simulation/simulation-and-predictive-digital-twin.md` |
| `categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md` | `categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md` |
| `categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md` | `categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md` |
| `categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md` | `categories/safety/safety-and-risk-management.md` |
| `categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md` | `categories/security-and-privacy/authentication-authorization-and-isolation.md` |
| `categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md` | `categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md` |
| `categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md` | `categories/integration/interoperability-standards-and-conformance.md` |

## 7. 수정 단계(D)에서 이 매핑을 쓰는 방법

페이지 이동·이름 변경·번호 재부여는 손으로 하지 않는다. D2 스크립트가 `data/mapping.yaml`의 `old_areas`(main·parts)와 `data/structure.yaml`의 `slug`를 읽어 새 페이지 뼈대, 본문·각주 이동, 링크 갱신, 리다이렉트 설정을 한 번에 만든다. 분할은 원 페이지의 절을 항목이 속한 영역으로 나누고, 원 페이지 자리에는 요약과 링크를 남긴다.
