---
title: "ROP 연구 위키"
type: home
tags: [ROP, SCM, 로봇 오케스트레이션]
status: published
created: {{created}}                        # YYYY-MM-DD. 구축일
updated: {{updated}}                        # YYYY-MM-DD. 퍼블리셔가 자동 갱신 영역을 다시 쓸 때 함께 올린다
version: {{version}}                        # 정수
---
<!--
[템플릿] 홈(소개) 페이지 (type: home)
경로: docs/index.md
쓰임: 구축 시 한 번 작성한다. 7절(진행 중인 중점 연구 트랙)과 9절(최근 업데이트)만 퍼블리셔가 자동 갱신한다. 자동 생성 문구만으로 홈을 채우지 않는다.
열한 항목(4.1)을 아래 순서로 둔다. 1은 제목과 한 줄 설명, 2~11은 절 제목. 원문 인용은 이 템플릿에 이미 넣어 두었으며 _source/ 와 글자 단위로 같아야 한다. 퍼블리셔(pipeline/checks/protect_source.py check_home)는 정의 문장·SCOR 문단·범위 문장이 한 줄 그대로(인용 부호 없이, 태그 뒤에 각주 없이) 들어 있는지와 대분류 표 각 행의 앞 3칸이 원문 표와 같은지 검사한다. 홈에는 각주 절이 없으므로 [^ref-NNN] 각주 대신 참고문헌 페이지 링크(references/ref-NNN.md)를 쓴다 [가정].
링크는 docs/index.md 기준 상대 경로: about/<파일>.md, categories/<대분류 slug>/index.md, categories/<대분류 slug>/<파일>.md, tracks/manual-capability-ontology/index.md, glossary/index.md, references/index.md, standards/index.md, open-questions.md, flow-matrix.md, changelog.md, metrics.md, logs/index.md.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 SCM·로봇·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_SCM_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다. 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일" 형식으로 둔다. 발행일을 모르면 "발행일 미확인"으로 쓴다. 원문을 열지 못한 출처는 접근일 뒤에 "(원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 12장의 1~10번에 대응한다(ref-001 ASCM SCOR, ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 9장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 재고정책 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: 27. AI·학습·적응과 모델 운영의 AI는 매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 27. AI·학습·적응과 모델 운영 페이지와 적용 대상 영역 페이지 양쪽에 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
-->
홈

# ROP 연구 위키

{{one_line_description}}
<!-- 한 줄 설명. 기본값: "공급망 관리(Supply Chain Management, SCM) 관점에서 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)의 연구 범위를 7개 대분류·28개 세부 연구영역으로 정리하고, 리서치·내용 검증·스토리텔러 에이전트가 매일 한 영역씩 조사·검증·서술한 내용을 쌓는 위키이다." 부제는 "SCM 관점의 로봇 오케스트레이션 플랫폼 연구". -->

## ROP란 무엇인가

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다. [분류원문]

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1] [분류원문]

{{scor_vs_rop}}
<!--
위 두 단락(정의 문장, SCOR 문단)은 분류 원문 1장에서 그대로 가져온 것이다. 수정 금지. 두 단락 모두 한 줄이며 " [분류원문]" 으로 끝나고 그 뒤에 각주를 붙이지 않는다(퍼블리셔가 줄 단위로 대조). 원문의 [1] 표기는 그대로 둔다.
이어서 SCOR 오케스트레이션과 로봇 오케스트레이션의 범위 차이를 두세 문장으로 재서술한다([의견], 또는 원문 12장 1번 자료에 근거하면 [사실]과 참고문헌 링크). 원문의 [1] 에 대응하는 참고문헌은 별도 문장으로 가리킨다. 예: "원문의 [1]은 참고문헌 [ref-001](references/ref-001.md)에 해당한다." 자세한 내용은 [SCM 관점의 ROP란 무엇인가](about/what-is-rop.md)로 링크한다.
-->

## 이 위키가 다루는 범위

이 위키는 7개 대분류와 28개 세부 연구영역을 뼈대로 한다. 분류 원문은 이 분류를 다음과 같이 설명한다.

공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다. [분류원문]

{{scope_note}}
<!-- 위 문장은 원문 머리말에서 그대로 가져온 것이다. 수정 금지. 인용 부호(>)·굵게 표기·각주를 덧붙이지 않는다(퍼블리셔가 이 문장이 한 줄 그대로 있는지 대조한다). 아래에 한두 문장으로 분류 원문(_source/)이 읽기 전용이며 에이전트가 명칭·번호·정의·질문을 바꾸지 않는다는 점, 분류 확장 제안은 [열린 질문](open-questions.md)으로만 낸다는 점을 쓴다. -->

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
<!-- 분류 원문 1장의 표(대분류 / 핵심 질문 / 세부영역)를 그대로 옮기고, 각 행에 대분류 페이지 링크와 세부영역 4개의 이름·링크를 뒤 두 열로 추가한 것이다(4.1 허용). 앞 3열(대분류 이름, 핵심 질문, "1–4" 같은 범위 표기)은 원문 셀과 글자 단위로 같아야 하며 링크를 씌우거나 문구를 바꾸지 않는다. 링크는 뒤 열(대분류 페이지, 세부 연구영역)에만 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_home)가 각 행의 앞 3칸을 원문 표와 대조한다. 번호만 쓰지 않는다. -->

## 다루지 않는 것

ROP는 전체 영역을 연구하되 직접 소유할 범위를 따로 정한다. 분류 원문 9장은 다섯 경계마다 ROP가 다룰 내용과 주로 연계할 외부 영역을 나눈다. 아래 목록은 원문 9장 표의 "경계" 열과 "주로 연계할 외부 영역" 열을 위키에서 한 줄씩 이어 붙인 요약이다. 셀의 문구는 원문과 같지만 이 줄 자체는 원문에 없는 문장이므로 `[분류원문]` 태그를 붙이지 않는다.

- **상위 업무 시스템** — 수요예측, 구매, 재무, 전사 재고정책
- **로봇 자체 지능·제어** — 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어
- **시설·설비 제어** — 승강기·컨베이어·PLC·설비 안전 제어
- **거점 간 운송** — 배차·운송계획·운임·국제물류
- **업종별 조건** — 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항

{{boundary_note}}
<!-- 요약 목록의 각 줄은 원문 9장 표의 "경계" 셀과 "주로 연계할 외부 영역" 셀을 " — " 로 이어 붙인 것이다. 셀 문구는 바꾸지 않되, 두 셀을 이은 줄은 원문에 있는 줄도 셀도 아니므로 [분류원문] 태그를 붙이지 않는다. 퍼블리셔(protect_source.py check_tagged_lines)는 홈·소개·대분류 페이지에서 " [분류원문]" 으로 끝나는 줄이 원문의 한 줄 또는 표 셀 하나와 글자 단위로 같은지 검사하므로, 태그를 붙이면 반려된다. 표 전체를 원문 그대로 인용하려면 소개 페이지(about/scope-boundary.md)처럼 표를 옮기고 표 아래에 [분류원문] 한 줄을 둔다. 위 안내 문장(태그를 붙이지 않는 이유)은 시드 홈 페이지와 같은 문장이며 그대로 두어도 된다. 표 전체와 설명 원문은 [ROP가 직접 소유할 범위와 외부 연계 경계](about/scope-boundary.md)에 있다. 아래 한 문장으로 그 페이지를 링크하고, 경계가 제품 전략에 따라 이동할 수 있다는 원문 취지를 짧게 쓴다. -->

## 콘텐츠가 만들어지는 방식

{{how_content_is_made}}
<!--
2~3단락. 리서치 에이전트(조사 브리프 작성) → 내용 검증 에이전트(1차 검증: 출처·주장 검증과 판정, 2차 검증: 서술 검증) → 스토리텔러 에이전트(위키 페이지 작성) → 퍼블리셔 스크립트(스키마·원문 보호·링크 검사 후 반영) 순으로 매일 1회 한 영역(또는 주제·트랙 단계)을 다룬다는 것, 검증을 통과하지 않은 내용은 게시되지 않는다는 것, 1주기(첫 28회)는 세부영역 본문을 채우고 2주기부터 주제 페이지를 쓴다는 것, 주 2회는 중점 연구 트랙에 배정된다는 것을 쓴다. 자세한 내용은 [에이전트 소개](about/agents.md)로 링크한다. 이 절의 문장은 위키 운영 설명이므로 사실 태그를 붙이지 않는다.
-->

## 진행 중인 중점 연구 트랙

<!-- auto:home-track-status:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:home-track-status:end -->
<!-- 퍼블리셔가 활성 트랙마다 다음을 넣는다: 트랙 이름(트랙 개요 링크), 트랙 상태(active | paused | done), 현재 단계(번호와 이름), 열린 질문 수, 최근 답한 질문(id 와 질문, 답이 실린 페이지 링크), 마지막 트랙 실행 id. 트랙 개요: tracks/manual-capability-ontology/index.md. 마커 사이는 사람과 스토리텔러가 건드리지 않는다. -->

## 표기 범례

**페이지 상태**

| 상태 | 의미 |
|---|---|
| seed | 원문 정의만 있고 본문이 없음 |
| draft | 스토리텔러 초안, 2차 검증 전 |
| verified | 2차 검증 통과, 게시 대기 |
| published | 게시됨 |
| needs_update | 정정 요청이 있거나 기준일이 오래되어 재검증 필요 |
| deprecated | 대체되었거나 더 이상 유효하지 않음. 대체 페이지 링크 필수 |

**신뢰도** — high: 핵심 주장이 2개 이상의 독립 출처로 확인됨 / medium: 단일 출처이거나 벤더·기사 중심 / low: 추정·의견 비중이 높음. 내용 검증 에이전트가 부여한다.

**주장 태그** — 문장 끝에 붙는다.

| 태그 | 의미 |
|---|---|
| [사실] | 출처로 확인된 주장. 각주가 함께 붙는다 |
| [추정] | 단일 출처·벤더 주장·간접 근거에 기댄 주장. 벤더 주장은 "벤더 주장"을 병기 |
| [의견] | 에이전트 또는 구축자의 해석·판단 |
| [가설] | 중점 연구 트랙에서 검증 중인 가설. 판정 전까지 사실로 쓰지 않음 |
| [사용자 실험] | 사용자가 experiments/ 에 넣은 실험 결과. 검증 판정 전까지 사실로 쓰지 않음 |
| [분류원문] | 분류 원문에서 한 글자도 바꾸지 않고 옮긴 문장. 에이전트가 수정하지 않음 |

출처는 `[^ref-001]` 형식의 각주로 붙이며, ref-NNN 은 [참고문헌](references/index.md)의 항목 id 이다. 자세한 읽는 법은 [읽기 가이드](about/reading-guide.md)에 있다.
<!-- 이 절의 표는 5.2·5.3의 고정 내용이다. 문구를 바꾸지 않는다. 각주 표기 예시는 반드시 백틱(`)으로 감싼다. 감싸지 않으면 check_links 가 정의 없는 각주 참조로 반려한다. -->

## 최근 업데이트

<!-- auto:home-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:home-recent:end -->
<!-- 퍼블리셔가 최신 5건을 넣는다(날짜 | 실행 id | 페이지 링크 | 변경 요약). 전체는 [변경 이력](changelog.md). 마커 사이는 건드리지 않는다. -->

## 시작하기 좋은 페이지

- [SCM 관점의 연구 시작 방법](about/research-method.md) — 물류 흐름 7단계와 여섯 항목으로 기술을 교차해 보는 방법
- [물류 흐름 매트릭스](flow-matrix.md) — 입고부터 반품까지 각 단계 × 여섯 항목에 어떤 페이지가 채워졌는지
- [매뉴얼 기반 로봇 기능 온톨로지 트랙 개요](tracks/manual-capability-ontology/index.md) — 진행 중인 중점 연구 트랙
- [용어집](glossary/index.md) — SCOR, ISA-95, EPCIS, Open-RMF, MRTA, MAPF 같은 용어의 정의
- [열린 질문](open-questions.md) — 아직 답하지 못한 질문과 상태
<!-- 다섯 항목은 4.1의 고정 목록이다. 설명 문구는 다듬어도 항목과 링크는 유지한다. -->

## 정정과 요청

{{corrections_note}}
<!-- 한두 문장. 잘못된 내용을 발견하면 inbox/corrections.md 에 정정 요청(페이지, 문제 문장, 근거, 요청일)을 쓰고, 우선 다룰 영역·주제·질문은 config/priority.yaml 로 지정한다는 것. [기여·정정 방법](about/how-to-contribute.md)과 [정정 요청 안내](corrections.md)로 링크한다. -->
