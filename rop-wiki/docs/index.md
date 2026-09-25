---
title: "ROP 연구 위키"
type: home
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
---

홈

# ROP 연구 위키

SCM(공급망 관리, Supply Chain Management) 관점에서 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)의 연구 범위를 정리하고, 리서치·내용 검증·스토리텔러 에이전트가 매일 한 영역씩 조사한 내용을 쌓아 가는 연구 위키다.

## ROP란 무엇인가

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다. [분류원문]

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1] [분류원문]

SCOR(Supply Chain Operations Reference)의 오케스트레이션은 계획부터 반품까지 공급망 프로세스 전체를 하나로 조정하는 상위 개념이고, 로봇 오케스트레이션은 그 가운데 물리적인 작업이 실제로 일어나는 구간에서 로봇과 현장 설비의 행동을 연결하는 실행 계층이다. [의견] 따라서 이 위키에서 ROP는 SCOR의 오케스트레이션을 대체하는 것이 아니라, 업무 시스템의 계획을 현장 행동으로 옮기고 그 결과를 다시 업무 시스템에 되돌려 주는 역할로 다룬다. [의견] 원문의 [1]은 참고문헌 [ref-001](references/ref-001.md)에 해당한다. 자세한 설명은 [SCM 관점의 ROP란 무엇인가](about/what-is-rop.md)에 있다.

## 이 위키가 다루는 범위

이 위키는 7개 대분류와 28개 세부 연구영역을 뼈대로 한다. 분류 원문은 이 분류의 성격을 다음과 같이 밝힌다.

공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다. [분류원문]

대분류·세부영역의 명칭·번호·정의·질문은 원문 그대로 쓰며 바꾸지 않는다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 [열린 질문](open-questions.md)에 "분류 확장 제안"으로 기록한다.

## 대분류 표

아래 표의 대분류·핵심 질문·세부영역 열은 원문 1장의 표를 그대로 옮긴 것이고, 대분류 페이지와 세부 연구영역 열은 위키에서 덧붙인 것이다.

| 대분류 | 핵심 질문 | 세부영역 | 대분류 페이지 | 세부 연구영역 |
|---|---|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 | [A. 업무·공급망 설계](categories/a-business-supply-chain-design/index.md) | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 | [B. 공통 정보·환경 모델](categories/b-common-information-and-environment-model/index.md) | [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 | [C. 연결·실행 기반](categories/c-connectivity-and-execution-foundation/index.md) | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 | [D. 계획·최적화](categories/d-planning-and-optimization/index.md) | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 | [E. 협업·현장 운영](categories/e-collaboration-and-field-operations/index.md) | [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 | [F. 도입·검증·유지관리](categories/f-deployment-verification-and-maintenance/index.md) | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 | [G. 안전·보안·지능·거버넌스](categories/g-safety-security-intelligence-and-governance/index.md) | [25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) |

[분류원문]

## 다루지 않는 것

ROP가 직접 소유하지 않고 외부 시스템과 연계하는 영역을 원문 9장은 다섯 가지 경계로 정리한다. 아래 목록은 원문 9장 표의 "경계" 열과 "주로 연계할 외부 영역" 열을 위키에서 한 줄씩 이어 붙인 요약이다. 셀의 문구는 원문과 같지만 이 줄 자체는 원문에 없는 문장이므로 `[분류원문]` 태그를 붙이지 않는다.

- **상위 업무 시스템** — 수요예측, 구매, 재무, 전사 재고정책
- **로봇 자체 지능·제어** — 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어
- **시설·설비 제어** — 승강기·컨베이어·PLC·설비 안전 제어
- **거점 간 운송** — 배차·운송계획·운임·국제물류
- **업종별 조건** — 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항

이 영역들은 ROP가 직접 만들지 않고 "연계 대상"으로 다룬다. 원문 9장의 표 전체(ROP에서 다룰 내용 열 포함)와 이 경계가 제품 전략에 따라 이동할 수 있다는 원문 설명은 [ROP가 직접 소유할 범위와 외부 연계 경계](about/scope-boundary.md)에 원문 그대로 있다.

## 콘텐츠가 만들어지는 방식

세 에이전트가 매일 1회 한 영역을 다룬다. 리서치 에이전트가 근거 있는 조사 브리프를 만들고, 내용 검증 에이전트가 출처의 실재와 주장–출처 일치를 검증해 게시 가능 여부를 판정하며, 스토리텔러 에이전트가 검증을 통과한 브리프만으로 페이지를 쓴다. 마지막으로 퍼블리셔 스크립트가 원문 보호·링크·프런트매터 검사를 거쳐 위키에 반영한다. 첫 주기(28회)는 세부영역 1. 주문·업무 시스템 연계부터 28. 표준·상호운용성·다사업자 거버넌스까지 번호순으로 본문을 채우고, 그 뒤에는 오래된 영역·열린 질문·비어 있는 매트릭스 칸을 기준으로 대상을 고른다. 각 에이전트의 역할·입력·출력과 사람이 개입하는 지점은 [에이전트 소개](about/agents.md)에 있다.

## 진행 중인 중점 연구 트랙

트랙은 분류를 바꾸지 않고 여러 세부영역을 가로지르는 집중 연구 프로그램이다. 현재 트랙은 세 개다. 첫 트랙 [매뉴얼 기반 로봇 기능 온톨로지](tracks/manual-capability-ontology/index.md)에 더해, 사용자가 제안한 세 확장 아이디어(아이디어 1. 로봇 기능 온톨로지, 아이디어 2. 자연어 업무 지시 챗봇, 아이디어 3. 건축 도면 자동 인식)를 연구하기 위해 첫 트랙을 넓히고(아이디어 1) 트랙 [자연어 업무 지시 챗봇](tracks/nl-task-chatbot/index.md)과 [건축 도면 자동 인식](tracks/floorplan-recognition/index.md)을 더했다. 세 아이디어가 이어지는 구조, 공통 데이터 모델, 28개 세부 연구영역 매핑표는 [확장 아이디어 연결 구조](ideas/index.md)에 있다. 아래 현황은 퍼블리셔가 자동으로 갱신한다.

<!-- auto:home-track-status:start -->
| 트랙 | 현재 단계 | 상태 | 열린 질문 수 | 최근 답한 질문 | 개요 |
|---|---|---|---|---|---|
| 매뉴얼 기반 로봇 기능 온톨로지 | [단계 1. 기존 능력 표현 모델과 표준 조사](tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md) (1 / 7) | active | 39 | q1-02 — 산업 상호운용 규격은 로봇 기능을 어떤 형식으로 기술하는가? (후보: VDA 5050의 팩트시트, MassRobotics AMR 상호운용 표준, OPC UA Robotics, Asset Administration Shell의 능력·스킬·서비스 모델, Open-RMF Fleet Adapter의 기능 기술) ([답](tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-02)) | [트랙 개요](tracks/manual-capability-ontology/index.md) |
| 자연어 업무 지시 챗봇 | [단계 1. 선행 연구·제품 사례 조사](tracks/nl-task-chatbot/stage-1-prior-work-and-products.md) (1 / 5) | active | 21 | q1-01 — 자연어 지시를 작업 단위로 분해하는 기존 접근은 무엇이 있는가? ([답](tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-01)) | [트랙 개요](tracks/nl-task-chatbot/index.md) |
| 건축 도면 자동 인식 | [단계 1. 선행 연구·제품 사례 조사](tracks/floorplan-recognition/stage-1-prior-work-and-products.md) (1 / 5) | active | 23 | q1-02 — 건축 도면(CAD·BIM·스캔 이미지)에서 로봇용 지도나 공간 모델을 자동으로 만드는 연구·제품 사례는 무엇이 있고, 입력 형식마다 무엇을 자동화하는가? ([답](tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-02)) | [트랙 개요](tracks/floorplan-recognition/index.md) |
<!-- auto:home-track-status:end -->

## 표기 범례

페이지 상태는 프런트매터 `status` 로 표시한다.

| 상태 | 의미 |
|---|---|
| seed | 원문 정의만 있고 본문이 없음 |
| draft | 스토리텔러 초안, 2차 검증 전 |
| verified | 2차 검증 통과, 게시 대기 |
| published | 게시됨 |
| needs_update | 정정 요청이 있거나 기준일이 오래되어 재검증 필요 |
| deprecated | 대체되었거나 더 이상 유효하지 않음. 대체 페이지 링크 필수 |

신뢰도(`confidence`)는 내용 검증 에이전트가 부여한다. high 는 핵심 주장이 2개 이상의 독립 출처로 확인된 것, medium 은 단일 출처이거나 벤더·기사 중심인 것, low 는 추정·의견 비중이 높은 것이다.

본문의 주장에는 태그를 붙인다. `[사실]`은 출처로 확인된 주장, `[추정]`은 근거는 있으나 확인이 부족한 주장(벤더 주장 포함), `[의견]`은 작성자의 해석이다. `[분류원문]`은 분류 원문에서 한 글자도 바꾸지 않고 옮긴 문장, `[가설]`은 중점 연구 트랙에서 검증할 가설, `[사용자 실험]`은 사용자가 직접 수행한 실험 결과다. 출처는 `[^ref-001]` 형식의 각주로 붙인다. 자세한 읽는 법은 [읽기 가이드](about/reading-guide.md)에 있다.

## 최근 업데이트

<!-- auto:home-recent:start -->
- 2026-09-25 · 갱신 · agents/storyteller.md — 스토리텔러 에이전트 프롬프트 1.3 → 1.4: 유니코드 제목 앵커 규칙과 답 소제목 명시 id({#q1-01}) 규칙 추가 (실행 manual-2026-09-25)
- 2026-09-25 · 갱신 · agents/verifier.md — 내용 검증 에이전트 프롬프트 1.3 → 1.4: 유니코드 제목 앵커 규칙과 답 소제목 명시 id 검사 추가 (실행 manual-2026-09-25)
- 2026-09-25 · 갱신 · agents/storyteller.md — 스토리텔러 에이전트 프롬프트 1.4 → 1.5: 태그 바로 뒤 괄호 금지 규칙 추가 (실행 manual-2026-09-25)
- 2026-09-25 · 갱신 · agents/shared-rules.md — 공통 규칙 1.1 → 1.2: 운영 전환 추가 규칙(원문 열람 표시·신뢰도 상한·상태 줄 금지·형식 검증·분량 분리·차등 갱신·트랙 3개) (실행 manual-2026-09-25)
- 2026-09-25 · 갱신 · agents/researcher.md — 리서치 에이전트 1.1 → 1.2: 원문 열기(GitHub raw·inbox), 갱신 차등 조사, 대분류 연결 절차 (실행 manual-2026-09-25)
- 전체 목록: [변경 이력](changelog.md)
<!-- auto:home-recent:end -->

## 시작하기 좋은 페이지

- [SCM 관점의 연구 시작 방법](about/research-method.md) — 물류 흐름 7단계와 여섯 항목으로 기술을 교차해 보는 방법
- [물류 흐름 매트릭스](flow-matrix.md) — 입고부터 반품까지 각 단계에서 어떤 페이지가 어떤 항목을 다루는지
- [매뉴얼 기반 로봇 기능 온톨로지 트랙 개요](tracks/manual-capability-ontology/index.md) — 진행 중인 중점 연구 트랙(첫 트랙)
- [확장 아이디어 연결 구조](ideas/index.md) — 세 확장 아이디어와 세 트랙이 이어지는 구조, 공통 데이터 모델, 28개 세부 연구영역 매핑표
- [용어집](glossary/index.md) — SCOR, ISA-95, EPCIS, Open-RMF, MRTA, MAPF 같은 용어의 한 줄 정의
- [열린 질문](open-questions.md) — 아직 답하지 못한 질문과 그 상태

## 정정과 요청

틀린 문장, 오래된 사실, 우선 조사할 주제가 있으면 [기여·정정 방법](about/how-to-contribute.md)의 절차를 따른다. 정정 요청은 다음 실행의 검증 항목에 포함되고, 처리 결과는 [변경 이력](changelog.md)에 남는다.
