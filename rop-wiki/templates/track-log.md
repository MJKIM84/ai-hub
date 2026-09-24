---
title: "트랙 로그 — {{track_name}}"          # 예: "트랙 로그 — 매뉴얼 기반 로봇 기능 온톨로지"
type: track-log
track: {{track_slug}}                       # 예: manual-capability-ontology
tags: []
status: published
created: {{created}}                        # YYYY-MM-DD. 구축일
updated: {{updated}}                        # YYYY-MM-DD. 마지막 트랙 실행 날짜
version: {{version}}                        # 정수. 실행 기록을 추가할 때마다 +1
---
<!--
[템플릿] 트랙 로그 (type: track-log)
경로: docs/tracks/<트랙 slug>/log.md
쓰임: 퍼블리셔 스크립트가 트랙 실행마다 "실행 기록" 블록을 최신순으로 추가한다(갱신 주체: 퍼블리셔). 스토리텔러는 블록 본문을 pages.json 의 track_updates.log_entry 로 내고, 퍼블리셔가 verification.json(단계 완료 판정·전환 승인)과 research.json 의 track 블록으로 나머지 칸을 채운다. 머리말과 "항목 형식" 절은 구축자가 쓰고(마커 밖), "실행 기록" 절의 본문은 auto:track-log 마커 안에 두어 퍼블리셔만 다시 쓴다. 시드 docs/tracks/manual-capability-ontology/log.md 와 같은 구성이다. track-log 는 공통 규약의 auto key 목록에 없는 시드 값이며, pipeline/lib/autoregion.py 의 AUTO_KEYS 와 pipeline/lib/render.py 의 render_for 에 아직 등록되어 있지 않다. 등록되기 전까지는 마커 안의 내용이 그대로 남는다(퍼블리셔가 원천 data/tracks/<트랙 slug>/log.json 에서 다시 만든다는 시드의 설명도 등록 후에 성립한다) [가정]. 등록은 pipeline 담당에게 요청한다(templates/README.md).
여덟 항목(5.4)을 실행마다 모두 담는다: 실행 id, 단계, 답한 질문, 새 질문, 온톨로지 변경, 완료 조건 평가, 세부영역 반영 제안, 다음 실행 제안. 값이 없으면 "없음"과 이유.
이 페이지에는 사실 태그를 붙이지 않는다(운영 기록). 질문·세부영역·단계는 번호와 이름을 함께 쓴다.

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

[경로 규약] 이 페이지에서 홈은 ../../index.md, 트랙 개요는 index.md, 단계 페이지·산출물은 <파일>.md, 세부영역은 ../../categories/<대분류 slug>/<파일>.md, 일일 로그는 ../../logs/daily/YYYY-MM-DD.md, 실행 산출물은 저장소의 runs/<실행 id>/ (위키 밖이므로 링크하지 않고 경로만 적는다) 이다.
| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 주문·업무 시스템 연계 | A. 업무·공급망 설계 | a-business-supply-chain-design/01-order-and-business-system-integration.md |
| 2 | 2. 공정·워크플로 모델링 | A. 업무·공급망 설계 | a-business-supply-chain-design/02-process-and-workflow-modeling.md |
| 3 | 3. 처리능력·거점·설비 계획 | A. 업무·공급망 설계 | a-business-supply-chain-design/03-capacity-site-and-facility-planning.md |
| 4 | 4. 성과·경제성·프로세스 개선 | A. 업무·공급망 설계 | a-business-supply-chain-design/04-performance-economics-and-process-improvement.md |
| 5 | 5. 로봇 능력·작업 온톨로지 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md |
| 6 | 6. 지도·공간·위치 모델 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/06-map-space-and-location-model.md |
| 7 | 7. 화물·재고·자산 식별과 추적 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md |
| 8 | 8. 실시간 세계 상태·데이터 일관성 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md |
| 9 | 9. 로봇·제조사 관제 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md |
| 10 | 10. 설비·건물 시스템 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md |
| 11 | 11. 분산 시스템·통신·컴퓨팅 구조 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md |
| 12 | 12. 명령·작업 실행의 신뢰성 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md |
| 13 | 13. 작업 배정 — MRTA | D. 계획·최적화 | d-planning-and-optimization/13-task-allocation-mrta.md |
| 14 | 14. 작업 순서·스케줄링 | D. 계획·최적화 | d-planning-and-optimization/14-task-sequencing-and-scheduling.md |
| 15 | 15. 다중 로봇 경로·교통 관리 — MAPF | D. 계획·최적화 | d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md |
| 16 | 16. 공용 자원·충전·에너지 최적화 | D. 계획·최적화 | d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md |
| 17 | 17. 로봇 간 협업·물리적 인계 | E. 협업·현장 운영 | e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md |
| 18 | 18. 사람–로봇 협업·운영 인터페이스 | E. 협업·현장 운영 | e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md |
| 19 | 19. 모니터링·이상 탐지·원인 분석 | E. 협업·현장 운영 | e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md |
| 20 | 20. 예외 복구·재계획·업무 연속성 | E. 협업·현장 운영 | e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md |
| 21 | 21. 온보딩·설정·현장 시운전 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md |
| 22 | 22. 시뮬레이션·예측용 디지털 트윈 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md |
| 23 | 23. 시험·형식 검증·벤치마크 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md |
| 24 | 24. 자산·소프트웨어 수명주기 관리 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md |
| 25 | 25. 안전·위험 관리 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md |
| 26 | 26. 사이버보안·접근권한·개인정보 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md |
| 27 | 27. AI·학습·적응과 모델 운영 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md |
| 28 | 28. 표준·상호운용성·다사업자 거버넌스 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md |
-->
[홈](../../index.md) › 중점 연구 트랙 › [{{track_name}}](index.md) › 트랙 로그

# 트랙 로그 — {{track_name}}

{{intro}}
<!-- 한두 문장. 이 로그가 트랙 실행마다 무엇을 기록하는지와 [트랙 개요](index.md)·[질문 백로그](question-backlog.md)·[능력 온톨로지 초안](ontology-draft.md) 링크. 구축 시 작성하고 이후 바꾸지 않는다. -->

## 항목 형식

실행마다 "실행 <실행 id> — 단계 <번호>. <이름>" 소제목 하나와 여덟 항목 표 하나를 둔다. 여덟 항목은 사양서 5.4의 트랙 로그 항목이다.

| 항목 | 내용 |
|---|---|
| 실행 id | 트랙 실행의 id(예 `2026-09-26-01`)와 그날의 일일 로그 링크. 구축 시드는 `build-{{created}}` |
| 단계 | 그 실행이 다룬 단계. 번호와 이름을 함께 쓰고 단계 페이지에 링크한다 |
| 답한 질문 | 질문 id, 질문 앞부분, 답 위치 링크. 없으면 "없음"과 이유 |
| 새 질문 | 질문 id, 질문 문장, 보낸 단계(번호와 이름), 근거 finding id. 없으면 "없음"과 이유 |
| 온톨로지 변경 | 버전 변화(예 v0 → v0.1)와 추가·변경·폐기된 개념·관계, 근거 finding id, 검증 승인 여부. 승인되지 않은 제안은 "보류"로 적는다. 없으면 "변경 없음"과 이유 |
| 완료 조건 평가 | 리서치 에이전트의 자체 평가, 내용 검증 에이전트의 판정, 단계 전환 여부 |
| 세부영역 반영 제안 | 관련 세부영역(번호와 이름)의 어느 절에 무엇을 반영하자는 제안(`pages.json`의 `area_reflection_proposals`). 없으면 "없음" |
| 다음 실행 제안 | 다음에 다룰 질문 id(우선순위 순), 되돌아온 앞 단계 질문, 사용자에게 요청할 것, 예산·환경 메모 |

항목은 최신순으로 쌓인다(가장 최근 실행이 맨 위). "실행 기록" 절의 본문은 자동 갱신 영역(auto 마커, 키 `track-log`) 안에 있으며, 퍼블리셔가 원천 데이터 `data/tracks/{{track_slug}}/log.json`에서 다시 만든다. 구축 시드 항목(build-{{created}})도 그 파일에 들어 있어 다시 만들어도 사라지지 않는다. `track-log`는 공통 규약의 auto 키 목록에 없는 키이므로 퍼블리셔가 키 목록(`pipeline/lib/autoregion.py`의 `AUTO_KEYS`)과 렌더러에 추가해야 자동 추가가 동작하며, 그 전까지는 마커 안의 내용이 그대로 남는다. [가정] 이 페이지에는 사실 태그를 붙이지 않는다(운영 기록). [가정]
<!-- 시드(docs/tracks/manual-capability-ontology/log.md)의 "항목 형식" 절과 같은 내용이다. 구축 시 작성하고 이후 바꾸지 않는다. 새 트랙에서는 트랙 slug·구축일만 바꾼다. 이 절은 사양서 5.4 의 트랙 로그 8항목 밖의 구축자 추가 절이다 [가정]. -->

## 실행 기록

<!-- auto:track-log:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:track-log:end -->
<!--
퍼블리셔가 실행마다 아래 블록(### 소제목 + 표)을 마커 안에 최신순으로 넣는다. 구축 시 첫 항목(실행 id build-<구축일>)을 넣을 때는 마커 안의 안내 문구 대신 이 블록을 둔다(시드와 같다). 마커 밖에는 실행 블록을 두지 않는다.
블록 형식(표 구분 행은 실제 페이지에서 칸마다 하이픈 세 개로 쓴다. 아래는 주석 안이라 하이픈 하나로 줄였다):
### 실행 <실행 id> — 단계 <번호>. <이름>
| 항목 | 내용 |
|-|-|
| 실행 id | <실행 id> ([일일 로그](../../logs/daily/<YYYY-MM-DD>.md)) |
| 단계 | [단계 <번호>. <이름>](<단계 파일>.md) |
| 답한 질문 | … |
| 새 질문 | … |
| 온톨로지 변경 | … |
| 완료 조건 평가 | … |
| 세부영역 반영 제안 | … |
| 다음 실행 제안 | … |
소제목은 "### 실행 <실행 id> — 단계 <번호>. <이름>" 형식을 지킨다.
답한 질문: "q1-01 (질문 앞부분…) → [답 위치](stage-1-existing-models-and-standards.md#q1-01)" 을 질문마다 줄바꿈(<br>) 또는 세미콜론으로 나열. 없으면 "없음(이유)".
새 질문: "q1-07 질문 문장 → 단계 1. 기존 능력 표현 모델과 표준 조사, 근거 f3" 형식. 없으면 "없음(이유)".
온톨로지 변경: "v0.1 → v0.2: 개념 '완료 확인 방법' 추가(f2), 관계 '기능은 완료 확인 방법을 가진다' 추가(f2) · 검증 승인" 또는 "변경 없음(이유)". 검증이 승인하지 않은 제안은 "보류: …" 로 적는다.
완료 조건 평가: "자체 평가: 미충족(비교표 미작성) · 검증 판정: 미충족 · 단계 전환: 아니오" 형식.
세부영역 반영 제안: "5. 로봇 능력·작업 온톨로지 — 7. 관련 표준·프레임워크·오픈소스: 요약" 을 제안마다 나열(pages.json 의 area_reflection_proposals). 없으면 "없음".
다음 실행 제안: 다음에 다룰 질문 id(우선순위 순), 되돌아온 앞 단계 질문, 사용자에게 요청할 것(experiments/, priority.yaml 의 track_questions), 예산·환경 메모.
-->
