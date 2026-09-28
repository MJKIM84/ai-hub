---
title: "ROP 연구 위키"
type: home
tags: [ROP, 로봇 오케스트레이션, 기술 지형도]
status: published
created: {{created}}                        # YYYY-MM-DD. 구축일
updated: {{updated}}                        # YYYY-MM-DD. 퍼블리셔가 자동 갱신 영역을 다시 쓸 때 함께 올린다
version: {{version}}                        # 정수
---
<!--
[템플릿] 홈(소개) 페이지 (type: home)
경로: docs/index.md
쓰임: 구축 시 한 번 작성한다(pipeline/scaffold.py build_home 이 같은 구조로 시드를 만든다). 7절(진행 중인 중점 연구 트랙)과 9절(최근 업데이트)만 퍼블리셔가 자동 갱신한다. 자동 생성 문구만으로 홈을 채우지 않는다.
열한 항목(4.1)을 아래 순서로 둔다. 1은 제목과 한 줄 설명, 2~11은 절 제목. 원문 인용(원문 1장의 정의 문장·분류의 성격 문단·필수 기능 문단, 머리말의 범위 문장, 1장 표)은 이 템플릿에 이미 넣어 두었으며 _source/ROP_연구분야_분류.md 와 글자 단위로 같아야 한다. 퍼블리셔(pipeline/checks/protect_source.py check_home)는 정의 문장·범위 문장이 한 줄 그대로(인용 부호 없이, 태그 뒤에 각주 없이) 들어 있는지와 대분류 표 각 행의 앞 3칸이 원문 표와 같은지 검사한다. 홈에는 각주 절이 없으므로 [^ref-NNN] 각주 대신 참고문헌 페이지 링크(references/ref-NNN.md)를 쓴다 [가정].
링크는 docs/index.md 기준 상대 경로: about/<파일>.md, categories/<대분류 slug>/index.md, categories/<대분류 slug>/<파일>.md, tracks/<트랙 slug>/index.md, glossary/index.md, references/index.md, standards/index.md, open-questions.md, site-matrix.md, changelog.md, metrics.md, logs/index.md.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.
-->
홈

# ROP 연구 위키

{{one_line_description}}
<!-- 한 줄 설명. 기본값(시드 홈과 같은 문장): "로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)을 구현하고 운영하는 데 관여하는 모든 일을 빠짐없이 나열해 17개 대분류·67개 세부 연구영역으로 묶고, 대분류마다 연구 논문·기사·업체 발표를 모아 가는 기술 지형도다. 리서치·내용 검증·스토리텔러 에이전트가 매일 한 영역씩 조사한 내용을 쌓는다." 대분류·세부영역 수는 원문 머리말(17개 대분류·67개 세부 연구영역)과 같게 쓴다. 한 줄 설명 아래의 시뮬레이터 버튼 단락은 시드 홈에 있는 그대로 둔다. -->

## ROP란 무엇인가

ROP는 **서로 다른 제조사의 로봇과 현장 설비·업무 시스템을 하나로 연결해, 사람이 정한 일을 여러 로봇이 함께 실제로 해내게 하고 그 결과를 다시 시스템에 돌려주는 플랫폼**으로 볼 수 있다. [분류원문]

이 분류는 ROP를 구현하고 운영하는 데 관여하는 모든 일을 처음부터 끝까지 빠짐없이 나열하고, 같은 일을 하는 것끼리 세부 연구영역으로, 핵심 질문이 같은 영역끼리 대분류로 묶은 것이다. 대분류마다 연구 논문·기사·업체 발표를 모아 기술 지형도를 만든다. 물류창고·제조 공장·병원·상업 시설·가정·실외는 모두 ROP가 쓰이는 현장 유형이다. [분류원문]

**B. 로봇 온톨로지와 C. 채팅 기반 구성·운영은 반드시 갖춰야 할 기능이다.** B는 이기종 로봇을 등록하고 능력을 표현해 시스템과 로봇을 쉽게 연동하게 하고, C는 채팅으로 맵을 그리고, 시나리오를 구성하고, 로봇을 구성하고, 실제 상황을 시뮬레이션으로 재현하고, 업무를 지시하게 한다. [분류원문]

자세한 설명은 [ROP란 무엇인가](about/what-is-rop.md)에 있다.
<!--
위 세 단락(정의 문장, 분류의 성격 문단, 필수 기능 문단)은 분류 원문 1장에서 그대로 가져온 것이다. 수정 금지. 세 단락 모두 한 줄이며 " [분류원문]" 으로 끝나고 그 뒤에 각주를 붙이지 않는다(퍼블리셔가 줄 단위로 대조). 이 위키는 특정 산업의 관점이 아니라 ROP를 구현·운영하는 일 전체를 다루며, 물류창고는 현장 유형 가운데 하나다. 정의를 특정 현장(예: 물류)의 흐름으로 좁혀 재서술하지 않는다.
-->

## 이 위키가 다루는 범위

분류 원문은 이 분류의 성격을 다음과 같이 밝힌다.

공식 단일 분류가 아니라 로봇 연구·실제 플랫폼 구조·현장 사례를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다. [분류원문]

{{scope_note}}
<!-- 위 문장은 원문 머리말에서 그대로 가져온 것이다. 수정 금지. 인용 부호(>)·굵게 표기·각주를 덧붙이지 않는다(퍼블리셔가 이 문장이 한 줄 그대로 있는지 대조한다). 아래에 한두 문장으로 대분류·세부영역의 명칭·번호·정의·질문을 원문 그대로 쓰며 바꾸지 않는다는 점, 분류 확장 제안은 [열린 질문](open-questions.md)으로만 낸다는 점, 2026-09-28에 분류를 7개 대분류·28개 영역에서 지금 구조(17개 대분류·67개 세부영역)로 개정했고 옛 영역 페이지의 본문은 새 영역 페이지로 옮겼다는 점을 쓴다. -->

## 대분류 표

아래 표의 대분류·핵심 질문·세부영역 열은 원문 1장의 표를 그대로 옮긴 것이고, 대분류 페이지와 세부 연구영역 열은 위키에서 덧붙인 것이다.

| 대분류 | 핵심 질문 | 세부영역 | 대분류 페이지 | 세부 연구영역 |
|---|---|---|---|---|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | 1–3 | [A. 기획·사업](categories/planning-and-business/index.md) | [1. 기술·시장·업체 동향](categories/planning-and-business/technology-market-and-vendor-trends.md)<br>[2. 사용 사례·요구·책임 범위](categories/planning-and-business/use-cases-requirements-and-scope.md)<br>[3. 경제성·조달·사업 모델](categories/planning-and-business/economics-procurement-and-business-models.md) |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | 4–7 | [B. 로봇 온톨로지](categories/robot-ontology/index.md) | [4. 이기종 로봇 등록](categories/robot-ontology/heterogeneous-robot-registration.md)<br>[5. 로봇 능력·작업 표현](categories/robot-ontology/robot-capability-and-task-representation.md)<br>[6. 온톨로지 기반 시스템·로봇 연동](categories/robot-ontology/ontology-based-system-and-robot-integration.md)<br>[7. 온톨로지 검증·변경 관리](categories/robot-ontology/ontology-verification-and-change-management.md) |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | 8–13 | [C. 채팅 기반 구성·운영](categories/chat-based-configuration-and-operation/index.md) | [8. 채팅으로 맵 작성](categories/chat-based-configuration-and-operation/chat-map-authoring.md)<br>[9. 채팅으로 시나리오 구성](categories/chat-based-configuration-and-operation/chat-scenario-composition.md)<br>[10. 채팅으로 로봇 구성](categories/chat-based-configuration-and-operation/chat-robot-configuration.md)<br>[11. 채팅으로 실제 상황 시뮬레이션 재현](categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)<br>[12. 채팅으로 업무 지시·오케스트레이션](categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)<br>[13. 대화형 기능의 신뢰·기반](categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | 14–16 | [D. 공간·지도 모델](categories/space-and-map-model/index.md) | [14. 도면·BIM에서 지도 만들기](categories/space-and-map-model/maps-from-floor-plans-and-bim.md)<br>[15. 지도·공간·위치 모델](categories/space-and-map-model/map-space-and-location-model.md)<br>[16. 장소 의미·지도 관리](categories/space-and-map-model/place-semantics-and-map-management.md) |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | 17–19 | [E. 사물·사람·실시간 상태](categories/objects-people-and-live-state/index.md) | [17. 작업 대상·자산 식별과 인계 추적](categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)<br>[18. 실시간 세계 상태·데이터 일관성](categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)<br>[19. 사람·보행자 모델](categories/objects-people-and-live-state/people-and-pedestrian-model.md) |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | 20–23 | [F. 연동](categories/integration/index.md) | [20. 로봇·제조사 관제 연동](categories/integration/robot-and-vendor-fleet-manager-integration.md)<br>[21. 상호운용 표준·적합성](categories/integration/interoperability-standards-and-conformance.md)<br>[22. 설비·건물 시스템 연동](categories/integration/facility-and-building-system-integration.md)<br>[23. 업무 시스템 연동](categories/integration/business-system-integration.md) |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | 24–28 | [G. 계획·최적화](categories/planning-and-optimization/index.md) | [24. 작업·워크플로 모델링](categories/planning-and-optimization/task-and-workflow-modeling.md)<br>[25. 작업 배정 — MRTA](categories/planning-and-optimization/task-allocation-mrta.md)<br>[26. 작업 순서·스케줄링](categories/planning-and-optimization/task-sequencing-and-scheduling.md)<br>[27. 다중 로봇 경로·교통 관리 — MAPF](categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)<br>[28. 공용 자원·충전·에너지 최적화](categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | 29–32 | [H. 실행·협업·예외 복구](categories/execution-collaboration-and-recovery/index.md) | [29. 명령·작업 실행의 신뢰성](categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)<br>[30. 로봇 간 협업·물리적 인계](categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)<br>[31. 사람–로봇 협업](categories/execution-collaboration-and-recovery/human-robot-collaboration.md)<br>[32. 예외 복구·재계획·업무 연속성](categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | 33–36 | [I. 설계·시뮬레이션](categories/design-and-simulation/index.md) | [33. 시나리오 모델·편집](categories/design-and-simulation/scenario-model-and-editing.md)<br>[34. 시뮬레이션·예측용 디지털 트윈](categories/design-and-simulation/simulation-and-predictive-digital-twin.md)<br>[35. 처리능력·규모·배치 설계](categories/design-and-simulation/capacity-sizing-and-layout-design.md)<br>[36. 가상 시운전·실제 상황 재현](categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | 37–40 | [J. 현장 운영·관제](categories/field-operations-and-monitoring/index.md) | [37. 관제 화면·실행 기록](categories/field-operations-and-monitoring/control-screen-and-execution-records.md)<br>[38. 모니터링·이상 탐지·원인 분석](categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)<br>[39. 운영 성과 측정·개선](categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)<br>[40. 운영 절차·요청 창구](categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | 41–43 | [K. 플랫폼 아키텍처·인프라](categories/platform-architecture-and-infrastructure/index.md) | [41. 플랫폼 아키텍처·외부 API](categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)<br>[42. 분산 시스템·통신·컴퓨팅 구조](categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)<br>[43. 데이터·관측성·배포](categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | 44–47 | [L. AI·학습 기술](categories/ai-and-learning/index.md) | [44. 로봇 기반 모델·언어 모델 계획](categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)<br>[45. 문서·도면·장면 이해](categories/ai-and-learning/document-drawing-and-scene-understanding.md)<br>[46. 예측·학습 기반 최적화](categories/ai-and-learning/prediction-and-learning-based-optimization.md)<br>[47. AI·학습·적응과 모델 운영](categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | 48–50 | [M. 안전](categories/safety/index.md) | [48. 안전·위험 관리](categories/safety/safety-and-risk-management.md)<br>[49. 사람 근접 안전](categories/safety/human-proximity-safety.md)<br>[50. 안전 표준·인증·사고 조사](categories/safety/safety-standards-certification-and-incident-investigation.md) |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | 51–53 | [N. 보안·개인정보](categories/security-and-privacy/index.md) | [51. 인증·권한·격리](categories/security-and-privacy/authentication-authorization-and-isolation.md)<br>[52. 통신 보호·위협 관리·감사](categories/security-and-privacy/communication-protection-threat-management-and-audit.md)<br>[53. 개인정보·영상 데이터](categories/security-and-privacy/privacy-and-video-data.md) |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | 54–57 | [O. 검증·도입·수명주기](categories/verification-deployment-and-lifecycle/index.md) | [54. 시험·형식 검증·벤치마크](categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)<br>[55. 현장 조사·설치·시운전](categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)<br>[56. 운영 이관·확대·교육](categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)<br>[57. 자산·소프트웨어 수명주기 관리](categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | 58–60 | [P. 거버넌스·법규·사회](categories/governance-law-and-society/index.md) | [58. 다사업자 책임·계약·데이터](categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md)<br>[59. 법·규제·보험·라이선스](categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)<br>[60. 노동·수용성·접근성](categories/governance-law-and-society/labor-acceptance-and-accessibility.md) |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | 61–67 | [Q. 현장 유형별 적용](categories/site-type-applications/index.md) | [61. 물류창고](categories/site-type-applications/warehouse.md)<br>[62. 제조 공장](categories/site-type-applications/manufacturing-plant.md)<br>[63. 병원·의료](categories/site-type-applications/hospital-and-healthcare.md)<br>[64. 상업 시설](categories/site-type-applications/commercial-facilities.md)<br>[65. 가정·공동주택](categories/site-type-applications/home-and-apartment.md)<br>[66. 실외](categories/site-type-applications/outdoor.md)<br>[67. 기타 현장](categories/site-type-applications/other-sites.md) |

[분류원문]
<!-- 분류 원문 1장의 표(대분류 / 핵심 질문 / 세부영역)를 그대로 옮기고, 각 행에 대분류 페이지 링크와 소속 세부영역의 이름·링크를 뒤 두 열로 추가한 것이다(4.1 허용). 앞 3열(대분류 이름, 핵심 질문, "1–3" 같은 범위 표기)은 원문 셀과 글자 단위로 같아야 하며 링크를 씌우거나 문구를 바꾸지 않는다. 링크는 뒤 열(대분류 페이지, 세부 연구영역)에만 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_home)가 각 행의 앞 3칸을 원문 표와 대조한다. 번호만 쓰지 않는다. -->

## 다루지 않는 것

ROP가 직접 소유하지 않고 외부 시스템과 연계하는 영역을 원문 19장은 다섯 가지 경계로 정리한다. 아래 목록은 경계표의 "경계" 열과 "주로 연계할 외부 영역" 열을 위키에서 한 줄씩 이어 붙인 요약이다. 셀의 문구는 원문과 같지만 이 줄 자체는 원문에 없는 문장이므로 `[분류원문]` 태그를 붙이지 않는다.

- **상위 업무 시스템** — 수요예측, 구매, 재무, 전사 자원 계획
- **로봇 자체 지능·제어** — 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어
- **시설·설비 제어** — 승강기·컨베이어·PLC·설비 안전 제어
- **현장 간 운송** — 배차·운송계획·운임·국제물류
- **업종별 조건** — 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항

{{boundary_note}}
<!-- 요약 목록의 각 줄은 원문 19장 표의 "경계" 셀과 "주로 연계할 외부 영역" 셀을 " — " 로 이어 붙인 것이다. 셀 문구는 바꾸지 않되, 두 셀을 이은 줄은 원문에 있는 줄도 셀도 아니므로 [분류원문] 태그를 붙이지 않는다. 퍼블리셔(protect_source.py check_tagged_lines)는 홈·소개·대분류 페이지에서 " [분류원문]" 으로 끝나는 줄이 원문의 한 줄 또는 표 셀 하나와 글자 단위로 같은지 검사하므로, 태그를 붙이면 반려된다. 표 전체를 원문 그대로 인용하려면 소개 페이지(about/scope-boundary.md)처럼 표를 옮기고 표 아래에 [분류원문] 한 줄을 둔다. 위 안내 문장(태그를 붙이지 않는 이유)은 시드 홈 페이지와 같은 문장이며 그대로 두어도 된다. 표 전체와 설명 원문은 [ROP가 직접 소유할 범위와 외부 연계 경계](about/scope-boundary.md)에 있다. 아래 한 문장으로 그 페이지를 링크하고, 이 영역들을 "연계 대상"으로 다룬다는 점과 경계가 제품 전략에 따라 이동할 수 있다는 원문 취지를 짧게 쓴다. -->

## 콘텐츠가 만들어지는 방식

{{how_content_is_made}}
<!--
1~3단락. 리서치 에이전트(조사 브리프 작성) → 내용 검증 에이전트(1차 검증: 출처·주장 검증과 판정, 2차 검증: 서술 검증) → 스토리텔러 에이전트(위키 페이지 작성) → 퍼블리셔 스크립트(스키마·원문 보호·링크 검사 후 반영) 순으로 매일 1회 한 영역(또는 주제·트랙 단계)을 다룬다는 것, 검증을 통과하지 않은 내용은 게시되지 않는다는 것, 아직 본문이 없는 세부영역부터 번호순으로 채우고 그 뒤에는 오래된 영역·열린 질문·비어 있는 현장 유형 칸을 기준으로 대상을 고른다는 것, 주 2회는 중점 연구 트랙에 배정된다는 것을 쓴다. 자세한 내용은 [에이전트 소개](about/agents.md)로 링크한다. 이 절의 문장은 위키 운영 설명이므로 사실 태그를 붙이지 않는다.
-->

## 진행 중인 중점 연구 트랙

트랙은 분류를 바꾸지 않고 여러 세부영역을 가로지르는 집중 연구 프로그램이다. 아래 현황은 퍼블리셔가 자동으로 갱신한다.

<!-- auto:home-track-status:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:home-track-status:end -->
<!-- 퍼블리셔가 활성 트랙마다 다음을 넣는다: 트랙 이름(트랙 개요 링크), 트랙 상태(active | paused | done), 현재 단계(번호와 이름), 열린 질문 수, 최근 답한 질문(id 와 질문, 답이 실린 페이지 링크), 마지막 트랙 실행 id. 트랙 개요: tracks/<트랙 slug>/index.md(예: tracks/manual-capability-ontology/index.md, tracks/chat-based-configuration-and-operation/index.md, tracks/floorplan-recognition/index.md). 마커 사이는 사람과 스토리텔러가 건드리지 않는다. -->

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

본문의 주장에는 태그를 붙인다. `[사실]`은 출처로 확인된 주장, `[추정]`은 근거는 있으나 확인이 부족한 주장(벤더 주장 포함), `[의견]`은 작성자의 해석이다. `[분류원문]`은 분류 원문에서 한 글자도 바꾸지 않고 옮긴 문장, `[옛 분류원문]`은 2026-09-28 개정 전 원문(보관본)에서 옮긴 문장, `[가설]`은 중점 연구 트랙에서 검증할 가설, `[사용자 실험]`은 사용자가 직접 수행한 실험 결과다. 출처는 `[^ref-001]` 형식의 각주로 붙인다. 자세한 읽는 법은 [읽기 가이드](about/reading-guide.md)에 있다.
<!-- 이 절의 표와 문단은 5.2·5.3의 고정 내용이다. 문구를 바꾸지 않는다. 각주 표기 예시는 반드시 백틱(`)으로 감싼다. 감싸지 않으면 check_links 가 정의 없는 각주 참조로 반려한다. -->

## 최근 업데이트

<!-- auto:home-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:home-recent:end -->
<!-- 퍼블리셔가 최신 5건을 넣는다(날짜 | 실행 id | 페이지 링크 | 변경 요약). 전체는 [변경 이력](changelog.md). 마커 사이는 건드리지 않는다. -->

## 시작하기 좋은 페이지

- [연구 방법](about/research-method.md) — 할 일을 빠짐없이 나열하고, 묶고, 묶음마다 자료를 모으는 방법
- [B. 로봇 온톨로지](categories/robot-ontology/index.md) — 이기종 로봇 등록·능력 표현·시스템과 로봇의 연동
- [C. 채팅 기반 구성·운영](categories/chat-based-configuration-and-operation/index.md) — 채팅으로 맵 작성·시나리오 구성·로봇 구성·실제 상황 재현·업무 지시
- [현장 유형 × 대분류 적용 사례 매트릭스](site-matrix.md) — 물류창고·공장·병원·상업 시설·가정·실외에서 어떤 대분류가 다뤄졌는지
- [용어집](glossary/index.md) — ISA-95, EPCIS, Open-RMF, VDA 5050, MRTA, MAPF 같은 용어의 한 줄 정의
- [열린 질문](open-questions.md) — 아직 답하지 못한 질문과 그 상태
<!-- 여섯 항목은 시드 홈의 고정 목록이다. 설명 문구는 다듬어도 항목과 링크는 유지한다. -->

## 정정과 요청

{{corrections_note}}
<!-- 한두 문장. 잘못된 내용을 발견하면 inbox/corrections.md 에 정정 요청(페이지, 문제 문장, 근거, 요청일)을 쓰고, 우선 다룰 영역·주제·질문은 config/priority.yaml 로 지정한다는 것. [기여·정정 방법](about/how-to-contribute.md)과 [정정 요청 안내](corrections.md)로 링크한다. -->
